# Loftahammarstipset – VM 2026 ⚽

En webbsida för familjens/gängets VM-tips under fotbolls-VM 2026 (11 juni – 19 juli). 16 deltagare tippar gruppspel och slutspel, och sidan visar ställning, matcher, grupptabeller, head-to-head och regler.

**Live:** https://jcmandersson.github.io/vm2026/
**Arrangör:** Sven Tholén

---

## Vad sidan gör

- **Hem** – din ställning, topp 3-pall, nästkommande match (med nedräkning) och allas tips.
- **Poänglista** – full ställning med sök, sortering (Total/Gruppspel/Slutspel) och trend.
- **Matcher** – nästa match-block + alla matcher uppdelat i Kommande/Spelade, med din gissning per match.
- **Slutspel** – slutspelsträd och din slutspelspoäng.
- **Grupper** – grupptabeller (facit).
- **Head-to-head** – jämför två deltagare.
- **Regler** – poängsystem och prisfördelning.

Sidan har ljust/mörkt läge (sparas), en intro-animation vid första besöket per session, och hämtar resultat live (se nedan).

## Poäng (sammanfattning)

- **Gruppspel:** 1 p för rätt tecken (1X2), +3 p för exakt resultat (alltså 4 p på en exakt träff). Max 288.
- **Slutspel:** 2/3/5/7/8 p per rätt lag (16-del/åttondel/kvart/semi/final), 10 p för rätt världsmästare. Max 206.
- **Totalt max:** 494 p. Fullständiga regler finns under fliken *Regler* i appen.

---

## Filer i projektet

| Fil | Roll |
|-----|------|
| `vm-tipset-2026.html` | Den färdiga, självständiga sidan (det som servas). All CSS/JS är inbäddad. |
| `index.html` | Liten omdirigering till `vm-tipset-2026.html` (så GitHub Pages-roten funkar). |
| `build_full.py` | Full generator. Innehåller hela mallen (HTML/CSS/JS) och bygger om `vm-tipset-2026.html` från `dataset.json` + `results.json`. |
| `build_site.py` | Lätt uppdaterare. Petar bara in färska resultat (`results.json`) i den befintliga HTML:en. Körs t.ex. av en schemalagd uppgift efter varje match. |
| `dataset.json` | Statisk data: deltagare, allas tips, matchprogram (fixtures), grupper, slutspelsstruktur. |
| `results.json` | Facit: gruppresultat per match-nr, tidsstämpel, ranking-snapshot (för trendpilar) m.m. |

## Så uppdateras resultat

Det finns två lager:

1. **Live i webbläsaren (primärt).** Vid varje sidladdning hämtas
   `https://n8n.charma.io/webhook/vm2026-resultat.json`, färdigspelade gruppresultat
   mappas in, och "Senast uppdaterad" sätts från feedens tid. Pågående matcher
   (`IN_PLAY`) visas som "PÅGÅR · inväntar resultat" (ingen liveställning – feeden ger
   bara slutresultat). **Detta kräver att webhooken tillåter CORS** för sidans origin
   (`https://jcmandersson.github.io` eller `*`). Annars faller sidan tillbaka på de
   inbyggda resultaten.

2. **Inbyggt (fallback).** `build_site.py` skriver in `results.json` i HTML:en. Kör det
   (manuellt eller schemalagt) och deploya om för att uppdatera utan att förlita sig på CORS.

> Obs: live-uppdatering sker vid sidladdning/refresh, inte löpande medan fliken är öppen.

## Bygga lokalt

Kör från projektmappen (läser `dataset.json`/`results.json` relativt):

```bash
python build_full.py      # bygger om hela vm-tipset-2026.html (struktur + data)
python build_site.py      # uppdaterar bara resultaten i vm-tipset-2026.html
```

## Teknik

- En enda självständig HTML-fil – inga byggsteg krävs för att visa den.
- Typsnitt: **Plus Jakarta Sans** (brödtext) och **Outfit** (logotyp/nedräkning) via Google Fonts.
- Flaggor från `flagcdn.com`.
- Inga ramverk, ingen localStorage utöver tema- och intro-flagga.

## Deploy (GitHub Pages)

1. Pusha repot till `git@github.com:jcmandersson/vm2026.git`.
2. GitHub → repo → **Settings → Pages → Deploy from a branch → main → / (root)**.
3. Sidan hamnar på https://jcmandersson.github.io/vm2026/ (roten omdirigerar till appen).
4. Sätt `Access-Control-Allow-Origin: https://jcmandersson.github.io` (eller `*`) i n8n
   (Respond to Webhook) så live-hämtningen funkar.

Endast `index.html` + `vm-tipset-2026.html` behövs för att sidan ska fungera. Bygg-filerna
(`build_*.py`, `*.json`) kan versionshanteras för bekvämlighet – men tänk på att
`dataset.json` då blir publikt läsbart (samma data finns dock redan i den publika HTML:en).
