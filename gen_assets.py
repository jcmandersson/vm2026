#!/usr/bin/env python3
"""Genererar app-ikoner och OG-delningsbild för Loftahammarstipset.

Ritar rena PNG:er med enbart stdlib (zlib) – ingen Pillow behövs.
Designen matchar faviconen: blå→lila gradient med en vit fotbolls-ring.
Kör: python3 gen_assets.py  → skriver icon-180.png, icon-192.png,
icon-512.png och og.png i projektmappen. Skriver över befintliga filer.
"""
import zlib, struct, math

BLUE = (37, 99, 255)
PURPLE = (139, 92, 246)
WHITE = (255, 255, 255)


def write_png(path, w, h, buf):
    def chunk(typ, data):
        c = typ + data
        return struct.pack(">I", len(data)) + c + struct.pack(">I", zlib.crc32(c) & 0xffffffff)
    raw = bytearray()
    for y in range(h):
        raw.append(0)
        raw += buf[y * w * 4:(y + 1) * w * 4]
    out = b"\x89PNG\r\n\x1a\n"
    out += chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0))
    out += chunk(b"IDAT", zlib.compress(bytes(raw), 9))
    out += chunk(b"IEND", b"")
    open(path, "wb").write(out)


def lerp(a, b, t):
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


def clamp01(v):
    return 0.0 if v < 0 else 1.0 if v > 1 else v


def ring_cov(dx, dy, R, halfsw):
    d = math.hypot(dx, dy)
    return clamp01(1.0 - (abs(d - R) - halfsw))


def icon(path, s):
    buf = bytearray(s * s * 4)
    cr = s * 0.22
    half = s / 2.0
    R = s * 0.30
    halfsw = s * 0.055
    for y in range(s):
        for x in range(s):
            px, py = x + 0.5, y + 0.5
            qx = abs(px - half) - (half - cr)
            qy = abs(py - half) - (half - cr)
            sd = math.hypot(max(qx, 0), max(qy, 0)) + min(max(qx, qy), 0) - cr
            a = clamp01(0.5 - sd)
            i = (y * s + x) * 4
            if a <= 0:
                continue
            t = (px + py) / (2 * s)
            col = lerp(BLUE, PURPLE, t)
            rc = ring_cov(px - half, py - half, R, halfsw)
            col = lerp(col, WHITE, rc)
            buf[i] = col[0]; buf[i + 1] = col[1]; buf[i + 2] = col[2]; buf[i + 3] = round(255 * a)
    write_png(path, s, s, buf)


def og(path, w=1200, h=630):
    buf = bytearray(w * h * 4)
    cx, cy = w / 2.0, h / 2.0
    R = 150.0
    halfsw = 19.0
    for y in range(h):
        for x in range(w):
            px, py = x + 0.5, y + 0.5
            t = (px / w + py / h) / 2.0
            col = lerp(BLUE, PURPLE, t)
            # faint outer pitch ring
            oc = ring_cov(px - cx, py - cy, 250.0, 1.5) * 0.18
            col = lerp(col, WHITE, oc)
            # faint center line
            cl = clamp01(1.0 - abs(px - cx) / 2.0) * 0.16
            col = lerp(col, WHITE, cl)
            # main ball ring
            rc = ring_cov(px - cx, py - cy, R, halfsw)
            col = lerp(col, WHITE, rc)
            i = (y * w + x) * 4
            buf[i] = col[0]; buf[i + 1] = col[1]; buf[i + 2] = col[2]; buf[i + 3] = 255
    write_png(path, w, h, buf)


if __name__ == "__main__":
    icon("icon-180.png", 180)
    icon("icon-192.png", 192)
    icon("icon-512.png", 512)
    og("og.png")
    print("klart: icon-180.png icon-192.png icon-512.png og.png")
