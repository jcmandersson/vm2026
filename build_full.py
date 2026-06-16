import json
D=json.load(open("dataset.json",encoding="utf-8"))
ISO={"Algeriet":"dz","Argentina":"ar","Australien":"au","Belgien":"be","Bosnien":"ba","Brasilien":"br","Colombia":"co","DR Kongo":"cd","Egypten":"eg","Elfenbenskusten":"ci","England":"gb-eng","Equador":"ec","Frankrike":"fr","Ghana":"gh","Haiti":"ht","Irak":"iq","Iran":"ir","Japan":"jp","Jordanien":"jo","Kanada":"ca","Kap Verde":"cv","Kroatien":"hr","Marocko":"ma","Mexiko":"mx","Nederländerna":"nl","Norge":"no","Nya Zeeland":"nz","Panama":"pa","Paraguay":"py","Portugal":"pt","Qatar":"qa","Saudiarabien":"sa","Schweiz":"ch","Senegal":"sn","Skottland":"gb-sct","Spanien":"es","Sverige":"se","Sydafrika":"za","Sydkorea":"kr","Tjeckien":"cz","Tunisien":"tn","Turkiet":"tr","Tyskland":"de","USA":"us","Uruguay":"uy","Uzbekistan":"uz","Österrike":"at","Curacao":"cw","Ecuador":"ec","Bosnien-Hercegovina":"ba"}
RES=json.load(open("results.json",encoding="utf-8"))
RJS={"group":RES.get("group",{}),"r32":RES.get("r32",[]),"r16":RES.get("r16",[]),"qf":RES.get("qf",[]),"sf":RES.get("sf",[]),"final":RES.get("final",[]),"champion":RES.get("champion"),"snapshot":RES.get("snapshot",{})}
UPD=RES.get("updated","")

TPL=r"""<!doctype html>
<html lang="sv" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Loftahammarstipset – VM 2026 ⚽</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Outfit:wght@600;700;800;900&family=Schoolbell&display=swap" rel="stylesheet">
<meta name="theme-color" content="#0a0e1f">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Cdefs%3E%3ClinearGradient id='g' x1='0' y1='0' x2='1' y2='1'%3E%3Cstop offset='0' stop-color='%232563ff'/%3E%3Cstop offset='1' stop-color='%238b5cf6'/%3E%3C/linearGradient%3E%3C/defs%3E%3Crect width='100' height='100' rx='24' fill='url(%23g)'/%3E%3Ccircle cx='50' cy='50' r='24' fill='none' stroke='white' stroke-width='7'/%3E%3C/svg%3E">
<style>
:root{--blue:#2563ff;--blue-deep:#0b3bd6;--indigo:#5b6cff;--yellow:#ffc400;--yellow-deep:#f5a700;--grass:#15c26b;--grass-deep:#0f9a55;--up:#15c26b;--down:#ff4d63;--flat:#9aa6bd;--gold:#f3b015;--silver:#9fb0c6;--bronze:#cd8a52;--r:20px;--r-sm:14px;--ease:cubic-bezier(.22,1,.36,1)}
[data-theme=light]{--ink:#0b1530;--ink2:#43507060;--muted:#6b7794;--bg:#eef2fb;--card:rgba(255,255,255,.82);--soft:#f1f5fc;--soft2:#e7eefb;--line:rgba(11,21,48,.09);--line2:rgba(11,21,48,.06);--sh:0 14px 40px -20px rgba(15,35,90,.4);--shs:0 6px 18px -10px rgba(15,35,90,.35);--ma:rgba(37,99,255,.16);--mb:rgba(255,196,0,.18);--mc:rgba(91,108,255,.14)}
[data-theme=dark]{--ink:#eaf0ff;--ink2:#b8c4e6;--muted:#8b97b8;--bg:#070b1a;--card:rgba(255,255,255,.05);--soft:rgba(255,255,255,.05);--soft2:rgba(255,255,255,.09);--line:rgba(255,255,255,.1);--line2:rgba(255,255,255,.06);--sh:0 24px 60px -22px rgba(0,0,0,.7);--shs:0 10px 26px -14px rgba(0,0,0,.6);--ma:rgba(37,99,255,.28);--mb:rgba(245,167,0,.16);--mc:rgba(91,108,255,.26)}
*{box-sizing:border-box}html,body{margin:0}
body{font-family:'Plus Jakarta Sans',system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--ink);background:var(--bg);min-height:100vh;-webkit-font-smoothing:antialiased;overflow-x:clip;transition:background .4s var(--ease),color .4s}
body::before{content:"";position:fixed;inset:-15% -10% auto -10%;height:90vh;z-index:0;pointer-events:none;background:radial-gradient(46% 40% at 16% 10%,var(--ma),transparent 60%),radial-gradient(44% 38% at 86% 6%,var(--mb),transparent 60%),radial-gradient(52% 44% at 72% 82%,var(--mc),transparent 62%);animation:drift 20s ease-in-out infinite alternate}
@keyframes drift{to{transform:translate3d(0,-3%,0) scale(1.07)}}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:18px 16px 90px}
@keyframes rise{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}
@keyframes pop{0%{transform:scale(.6);opacity:0}60%{transform:scale(1.12)}to{transform:scale(1);opacity:1}}
.bar{display:flex;align-items:center;gap:12px;margin-bottom:14px}
.bar .logo{font-size:30px;animation:spin 11s linear infinite}@keyframes spin{to{transform:rotate(360deg)}}
.bar h1{margin:0;font-size:21px;font-weight:900;letter-spacing:-.5px;line-height:1.1;background:linear-gradient(120deg,var(--ink),var(--blue) 65%,var(--indigo));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.bar .sub{font-size:12px;color:var(--muted);font-weight:500;margin-top:1px}
.bar .tog{margin-left:auto;width:42px;height:42px;border-radius:13px;border:1px solid var(--line);background:var(--card);backdrop-filter:blur(12px);color:var(--ink);font-size:18px;cursor:pointer;transition:.3s var(--ease)}
.bar .tog:hover{transform:translateY(-2px) rotate(-8deg)}
.updated{font-size:11.5px;color:var(--muted);margin:-4px 0 12px;font-weight:500}
.updated .dot{display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--grass);margin-right:5px;animation:pulse 1.8s infinite}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(21,194,107,.6)}70%{box-shadow:0 0 0 8px rgba(21,194,107,0)}}
.tabs{display:flex;gap:7px;overflow-x:auto;padding-bottom:4px;margin-bottom:16px;-webkit-overflow-scrolling:touch;scrollbar-width:none}
.tabs::-webkit-scrollbar{display:none}
.tab{flex:0 0 auto;border:1px solid var(--line);background:var(--card);backdrop-filter:blur(10px);color:var(--ink2);font-weight:700;font-size:13px;border-radius:999px;padding:9px 15px;cursor:pointer;transition:.25s var(--ease);color:var(--muted)}
.tab.active{background:linear-gradient(135deg,var(--blue),var(--indigo));color:#fff;border-color:transparent}
.view{display:none;animation:rise .4s var(--ease)}.view.active{display:block}
.card{background:var(--card);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);border:1px solid var(--line);border-radius:var(--r);box-shadow:var(--sh);padding:18px;margin-bottom:16px}
.ttl{font-weight:800;font-size:12.5px;text-transform:uppercase;letter-spacing:.7px;color:var(--ink2);margin:0 0 14px;display:flex;align-items:center;gap:7px}
.ttl .more{margin-left:auto;font-size:11.5px;font-weight:700;color:var(--blue);cursor:pointer;text-transform:none;letter-spacing:0}
.flag-img{border-radius:3px;vertical-align:middle;box-shadow:0 1px 2px rgba(0,0,0,.25);object-fit:cover;display:inline-block}
.flagfb{display:inline-grid;place-items:center;background:linear-gradient(135deg,var(--soft2),var(--soft));border:1px solid var(--line2);border-radius:4px;font-weight:800;color:var(--muted);vertical-align:middle;letter-spacing:.3px}
.flag-round{border-radius:50%;object-fit:cover;box-shadow:0 5px 14px rgba(0,0,0,.2);border:3px solid var(--card)}
.flagfb-round{display:grid;place-items:center;border-radius:50%;background:linear-gradient(135deg,var(--soft2),var(--soft));border:3px solid var(--card);font-weight:800;color:var(--muted);box-shadow:0 5px 14px rgba(0,0,0,.2)}
.ava{border-radius:50%;display:grid;place-items:center;color:#fff;font-weight:800;flex:0 0 auto;box-shadow:var(--shs)}
/* PODIUM */
.podium{display:grid;grid-template-columns:1fr 1.15fr 1fr;align-items:end;gap:8px;max-width:460px;margin:6px auto 4px}
.pod{display:flex;flex-direction:column;align-items:center;gap:8px;cursor:pointer}
.pod .medal{font-size:22px;filter:drop-shadow(0 3px 5px rgba(0,0,0,.2))}
.pod .ava{width:52px;height:52px;font-size:17px;border:3px solid var(--card)}
.pod.p1 .ava{width:66px;height:66px;font-size:21px;box-shadow:0 0 0 3px var(--gold),var(--shs)}
.pod .nm{font-weight:800;font-size:12.5px;text-align:center;line-height:1.15;max-width:96px}
.pod .pts{font-weight:900;font-size:15px}
.pod .step{width:100%;border-radius:12px 12px 0 0;display:grid;place-items:center;color:#fff;font-weight:900;font-size:20px;box-shadow:var(--shs)}
.pod.p1 .step{height:92px;background:linear-gradient(180deg,var(--gold),#e09a00)}
.pod.p2 .step{height:66px;background:linear-gradient(180deg,var(--silver),#7d90a8)}
.pod.p3 .step{height:48px;background:linear-gradient(180deg,var(--bronze),#a86a36)}
.pod .step small{font-size:10px;opacity:.9;font-weight:700;display:block;margin-top:-2px}
.podnote{text-align:center;font-size:11.5px;color:var(--muted);margin-top:8px}
/* FEATURED MATCH */
.fhead{display:flex;align-items:center;gap:10px;margin-bottom:6px}
.fhead .ph{background:linear-gradient(135deg,var(--blue),var(--indigo));color:#fff;font-size:11px;font-weight:800;padding:4px 12px;border-radius:999px}
.fhead .nav{margin-left:auto;display:flex;gap:6px}
.fhead .nav button{width:38px;height:38px;border-radius:11px;border:1px solid var(--line);background:var(--soft);color:var(--ink);font-size:18px;cursor:pointer;transition:.2s var(--ease)}
.fhead .nav button:hover:not(:disabled){background:var(--blue);color:#fff}
.fhead .nav button:disabled{opacity:.3}
.fbody{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:8px;padding:14px 4px 6px}
.team{display:flex;flex-direction:column;align-items:center;gap:9px;text-align:center}
.team .tn{font-weight:800;font-size:14px;line-height:1.15}
.sb{text-align:center;min-width:84px}
.sb .sc{font-size:34px;font-weight:900;line-height:1;background:linear-gradient(120deg,var(--ink),var(--blue));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.sb .sc.pend{font-size:18px;color:var(--muted);-webkit-text-fill-color:var(--muted)}
.sb .sc.pop{animation:pop .5s var(--ease)}
.sb .ft{font-size:10px;color:var(--muted);font-weight:800;text-transform:uppercase;letter-spacing:1px;margin-top:6px}
.fmeta{text-align:center;color:var(--muted);font-size:12px;font-weight:600;padding-top:6px}
.dots{display:flex;justify-content:center;gap:5px;flex-wrap:wrap;padding-top:12px}
.dots i{width:6px;height:6px;border-radius:50%;background:var(--line);cursor:pointer;transition:.3s var(--ease)}
.dots i.on{background:var(--blue);width:18px;border-radius:3px}
.prog{display:flex;align-items:center;gap:10px;padding-top:14px}
.ptrack{flex:1;height:6px;border-radius:999px;background:var(--soft2);overflow:hidden}
.pfill{height:100%;border-radius:999px;background:linear-gradient(90deg,var(--blue),var(--indigo));transition:width .35s var(--ease)}
.plbl{font-size:11px;font-weight:800;color:var(--muted);white-space:nowrap}
.picks{display:block}
.picks::-webkit-scrollbar{height:6px}.picks::-webkit-scrollbar-thumb{background:var(--line);border-radius:9px}
.pchip{flex:0 0 auto;display:flex;align-items:center;gap:8px;background:var(--soft);border:1px solid var(--line2);border-radius:999px;padding:6px 11px 6px 6px}
.pchip.hit{background:color-mix(in srgb,var(--grass) 15%,transparent);border-color:color-mix(in srgb,var(--grass) 35%,transparent)}
.pchip.close{background:color-mix(in srgb,var(--yellow) 18%,transparent)}
.pchip .ava{width:26px;height:26px;font-size:10px}
.pchip .pn{font-size:12px;font-weight:700}.pchip .pg{font-size:12px;color:var(--muted);font-weight:600}
.pchip .pt{font-weight:800;font-size:11px;color:var(--grass-deep)}
.catblock{margin-bottom:12px;border:1px solid var(--line2);border-radius:14px;overflow:hidden}
.cathead{font-weight:800;font-size:12.5px;padding:9px 13px;display:flex;align-items:center;gap:8px}
.cathead .cp{margin-left:auto;font-weight:900;font-size:12px;opacity:.85}
.cat-exact .cathead{background:color-mix(in srgb,var(--grass) 16%,transparent);color:var(--grass-deep)}
.cat-right .cathead{background:color-mix(in srgb,var(--yellow) 26%,transparent);color:#a35400}
.cat-wrong .cathead{background:color-mix(in srgb,var(--down) 18%,transparent);color:#a8102b}
[data-theme=dark] .cat-right .cathead{color:#ffb454}
[data-theme=dark] .cat-wrong .cathead{color:#ff8a9c}
.scoregrp{display:flex;align-items:center;gap:11px;padding:9px 13px;border-top:1px solid var(--line2);flex-wrap:wrap}
.catblock>.scoregrp:first-child,.cathead+.scoregrp{border-top:none}
.sline{font-weight:900;font-size:15px;background:var(--soft2);border:1px solid var(--line2);border-radius:9px;padding:3px 10px;min-width:48px;text-align:center}
.scoregrp .cnt{font-size:11px;color:var(--muted);font-weight:700}
.ppl{display:flex;flex-wrap:wrap;gap:6px;flex:1;min-width:0}
.pp2{display:inline-flex;align-items:center;gap:5px;font-size:12px;font-weight:600;background:var(--soft);border:1px solid var(--line2);border-radius:999px;padding:3px 10px 3px 3px}
.pp2 .ava{width:22px;height:22px;font-size:9px}
.mebar{display:flex;align-items:center;gap:8px;font-size:12.5px;font-weight:700;color:var(--muted);margin:-2px 0 14px}
.mebar select{flex:0 0 auto;width:auto;min-width:160px}
.rk.me{background:color-mix(in srgb,var(--blue) 16%,transparent);box-shadow:inset 0 0 0 2px var(--blue),0 8px 20px -10px var(--blue);transform:scale(1.015)}
.rk.me .nm{color:var(--blue)}
.rk.me .tot{color:var(--blue)}
.mebanner{display:flex;align-items:center;gap:13px;background:linear-gradient(135deg,var(--blue),var(--indigo));color:#fff;border-radius:16px;padding:14px 16px;margin-bottom:14px;box-shadow:0 12px 26px -12px var(--blue)}
.mebanner .ava{width:46px;height:46px;font-size:16px;border:2px solid rgba(255,255,255,.55);background:rgba(255,255,255,.18)}
.mebanner .bi{flex:1;min-width:0}
.mebanner .bl{font-size:10.5px;opacity:.88;font-weight:800;text-transform:uppercase;letter-spacing:.6px}
.mebanner .bn{font-weight:800;font-size:16px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.mebanner .bp{text-align:center;display:flex;flex-direction:column;align-items:center;justify-content:center;line-height:1.05}
.mebanner .bpv{font-size:26px;font-weight:900;line-height:1}
.mebanner .bpu{font-size:12px;font-weight:700;opacity:.9;line-height:1.25}
.mebanner .bps{font-size:10px;opacity:.85;font-weight:700}
.pod.me .nm{color:var(--blue)}
.pod.me .ava{box-shadow:0 0 0 3px var(--blue),var(--shs)}
.pod.p1.me .ava{box-shadow:0 0 0 3px var(--blue),var(--shs)}
.pp2.me{background:color-mix(in srgb,var(--blue) 14%,transparent);border-color:color-mix(in srgb,var(--blue) 45%,transparent)}
.dut{font-size:9.5px;font-weight:900;background:var(--blue);color:#fff;border-radius:6px;padding:2px 6px;vertical-align:middle;margin-left:6px;letter-spacing:.6px;box-shadow:0 2px 6px -2px var(--blue)}
.mright{display:flex;flex-direction:column;align-items:flex-end;gap:3px}
.mpts{font-size:10px;font-weight:800;border-radius:6px;padding:1px 7px}
.mpts.g{background:color-mix(in srgb,var(--grass) 18%,transparent);color:var(--grass-deep)}
.mpts.y{background:color-mix(in srgb,var(--yellow) 24%,transparent);color:var(--yellow-deep)}
.mpts.z{background:var(--soft);color:var(--muted)}
.mtabs{display:flex;gap:5px;overflow-x:auto;padding:2px 2px 4px;margin-bottom:6px;scrollbar-width:thin;scroll-behavior:smooth}
.mtabs::-webkit-scrollbar{height:5px}.mtabs::-webkit-scrollbar-thumb{background:var(--line);border-radius:9px}
.mtabs{align-items:center}
.mtab{flex:0 0 auto;width:13px;height:13px;padding:0;min-width:0;border:none;border-radius:50%;cursor:pointer;transition:.18s var(--ease)}
.mtab.done{background:var(--grass)}
.mtab.up{background:var(--soft2)}
.mtab.cur{width:30px;border-radius:7px;background:var(--blue);box-shadow:var(--shs)}
.mtab:hover{transform:scale(1.25)}.mtab.cur:hover{transform:none}
.mleg{display:flex;gap:12px;align-items:center;font-size:10.5px;color:var(--muted);font-weight:700;margin:0 0 8px}
.mleg .ld{width:11px;height:11px;border-radius:3px;display:inline-block;margin-right:5px;vertical-align:-1px}
.mleg .ld.done{background:var(--grass)}.mleg .ld.up{background:var(--soft2)}.mleg .ld.cur{background:var(--blue)}
.cdwrap{text-align:center}
.cd{display:inline-block;font-size:12px;font-weight:800;color:var(--blue);background:color-mix(in srgb,var(--blue) 12%,transparent);border-radius:999px;padding:5px 13px;margin-top:10px}
.mebar2{height:5px;background:rgba(255,255,255,.28);border-radius:999px;margin-top:7px;overflow:hidden}
.mefill{height:100%;background:#fff;border-radius:999px;transition:width .4s var(--ease)}
.mrow{position:relative}
.mrow.today{box-shadow:inset 3px 0 0 var(--grass)}
.mrow.next{box-shadow:inset 3px 0 0 var(--blue);background:color-mix(in srgb,var(--blue) 8%,transparent)}
.nbadge{font-size:9px;font-weight:900;background:var(--blue);color:#fff;border-radius:5px;padding:1px 6px;margin-right:6px;letter-spacing:.5px}
.myguess{display:inline-block;font-size:11px;font-weight:700;color:var(--blue);margin-top:4px;background:color-mix(in srgb,var(--blue) 10%,transparent);border-radius:6px;padding:2px 8px}
.mx-row{background:var(--soft);border:1px solid var(--line2);border-radius:14px;padding:11px 14px;margin-bottom:9px;cursor:pointer;transition:.2s var(--ease)}
.mx-row:hover{box-shadow:var(--shs);transform:translateY(-1px)}
.mx-row.today{border-left:3px solid var(--grass)}
.mx-row.next{border:1px solid color-mix(in srgb,var(--blue) 45%,transparent);background:color-mix(in srgb,var(--blue) 8%,transparent);box-shadow:var(--shs)}
.mx-meta{font-size:9.5px;font-weight:800;color:var(--muted);text-transform:uppercase;letter-spacing:.4px;display:flex;align-items:center;gap:7px;margin-bottom:8px}
.mx-main{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:12px}
.mx-team{display:flex;align-items:center;gap:8px;min-width:0;font-weight:700;font-size:14px}
.mx-team.h{justify-content:flex-end;text-align:right}
.mx-team.a{justify-content:flex-start}
.mx-team .tn{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.mx-team .tn.slot{font-weight:600;font-size:11.5px;color:var(--muted)}
.mx-score{font-weight:900;min-width:60px;text-align:center}
.mx-score.done{background:var(--ink);color:var(--bg);border-radius:10px;padding:5px 8px;font-size:16px;letter-spacing:.5px}
.mx-score.soon{font-size:12.5px;color:var(--muted);font-weight:800}
.mx-score.vs{font-size:11px;color:var(--muted);font-weight:800;letter-spacing:1px}
.mx-foot{display:flex;align-items:center;gap:8px;margin-top:9px;padding-top:8px;border-top:1px dashed var(--line2)}
.mx-foot .sp{flex:1}.mx-foot .myguess{margin-top:0}
.tbadge{font-size:9px;font-weight:900;background:var(--grass);color:#fff;border-radius:5px;padding:1px 6px;letter-spacing:.5px}
.exb{font-size:9px;font-weight:800;background:var(--soft2);color:var(--muted);border-radius:5px;padding:1px 6px;margin-left:auto;display:inline-flex;align-items:center;gap:4px}
.exb::before{content:"";width:6px;height:6px;border-radius:50%;background:currentColor;opacity:.5}
.exb.b1{background:color-mix(in srgb,var(--blue) 15%,var(--soft2));color:var(--blue-deep)}
.exb.b2{background:color-mix(in srgb,var(--blue) 32%,transparent);color:var(--blue-deep)}
.exb.b3{background:color-mix(in srgb,var(--blue) 60%,transparent);color:#fff}
.exb.b4{background:var(--blue);color:#fff;box-shadow:0 2px 9px -3px var(--blue)}
.exb.b1::before,.exb.b2::before,.exb.b3::before,.exb.b4::before{opacity:.9}
[data-theme=dark] .exb.b1{color:#a8c2ff}[data-theme=dark] .exb.b2{color:#cfe0ff}
.mx-guess{display:flex;align-items:center;gap:11px;margin-top:11px;padding:11px 14px;border-radius:13px;background:color-mix(in srgb,var(--blue) 9%,transparent);border:1px solid color-mix(in srgb,var(--blue) 22%,transparent)}
.mx-guess .gl{font-size:10.5px;font-weight:900;letter-spacing:.7px;color:var(--blue);text-transform:uppercase;opacity:.95}
.mx-guess .gv{font-size:21px;font-weight:900;color:var(--blue);letter-spacing:.5px}
.mx-guess .go{margin-left:auto;font-size:12px;font-weight:800;padding:4px 11px;border-radius:999px;background:var(--blue);color:#fff}
.mx-guess.exact{background:color-mix(in srgb,var(--grass) 15%,transparent);border-color:color-mix(in srgb,var(--grass) 34%,transparent)}
.mx-guess.exact .gv,.mx-guess.exact .gl{color:var(--grass-deep)}.mx-guess.exact .go{background:var(--grass);color:#fff}
.mx-guess.right{background:color-mix(in srgb,var(--yellow) 22%,transparent);border-color:color-mix(in srgb,var(--yellow-deep) 32%,transparent)}
.mx-guess.right .gv,.mx-guess.right .gl{color:#a35400}.mx-guess.right .go{background:var(--yellow-deep);color:#3d2a00}
.mx-guess.wrong{background:color-mix(in srgb,var(--down) 15%,transparent);border-color:color-mix(in srgb,var(--down) 32%,transparent)}
.mx-guess.wrong .gv,.mx-guess.wrong .gl{color:#a8102b}.mx-guess.wrong .go{background:var(--down);color:#fff}
.reg h3{font-size:14px;margin:18px 0 8px}.reg p{font-size:13px;color:var(--ink);line-height:1.6;margin:0 0 8px}
.reg table{width:100%;border-collapse:collapse;font-size:13px;margin-top:6px}.reg td{padding:7px 8px;border-bottom:1px solid var(--line2)}.reg td:last-child{text-align:right;font-weight:800;white-space:nowrap;color:var(--blue)}
.reg .big{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:6px}.reg .pcard{flex:1;min-width:110px;background:var(--soft);border:1px solid var(--line2);border-radius:12px;padding:12px;text-align:center}.reg .pcard .v{font-size:20px;font-weight:900;color:var(--blue)}.reg .pcard .l{font-size:11px;color:var(--muted);font-weight:700}
/* RANKING ROWS */
.rk{display:flex;align-items:center;gap:11px;padding:10px 6px;border-radius:var(--r-sm);cursor:pointer;transition:.2s var(--ease)}
.rk:hover{background:var(--soft)}
.rk .pos{width:26px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1px;line-height:1}
.rk .pos .rkn{font-weight:800;color:var(--muted);font-size:14px;line-height:1}
.rk.top .pos .rkn{font-size:16px}
.rk .ava{width:34px;height:34px;font-size:12px}
.rk .who{flex:1;min-width:0;display:flex;flex-direction:column;gap:1px}.rk .nm{font-weight:700;font-size:14px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.rk .pp{font-size:11px;color:var(--muted);font-weight:500}
.rk .tot{font-weight:900;font-size:17px;margin-left:6px;display:flex;align-items:baseline;gap:3px}
.rk .fire{font-size:15px;line-height:1;align-self:center;filter:drop-shadow(0 0 5px rgba(255,120,0,.55));animation:flick 1.1s ease-in-out infinite}
@keyframes flick{0%,100%{transform:scale(1) rotate(-3deg)}50%{transform:scale(1.14) rotate(3deg)}}
.totu{font-size:10px;font-weight:700;color:var(--muted)}
.tr{display:inline-flex;align-items:center;gap:1px;font-size:9.5px;font-weight:800;line-height:1}
.tr svg{width:9px;height:9px;display:block}
.tr.up{color:var(--up)}.tr.down{color:var(--down)}
/* MATCH LIST */
.mfilter{display:flex;gap:6px;margin-bottom:12px;background:var(--soft);padding:4px;border-radius:12px}
.mfilter button{flex:1;border:none;background:transparent;color:var(--ink2);font-weight:700;border-radius:9px;padding:8px;cursor:pointer;font-size:12px;transition:.25s var(--ease);color:var(--muted)}
.mfilter button.active{background:var(--card);color:var(--blue);box-shadow:var(--shs)}
.mrow{display:flex;align-items:center;gap:10px;padding:11px 8px;border-radius:var(--r-sm);cursor:pointer;border:1px solid transparent;transition:.2s var(--ease)}
.mrow:hover{background:var(--soft)}.mrow.active{border-color:color-mix(in srgb,var(--blue) 40%,transparent);background:color-mix(in srgb,var(--blue) 7%,transparent)}
.mrow .ph2{font-size:9.5px;color:var(--muted);font-weight:800;text-transform:uppercase;letter-spacing:.4px}
.mrow .tt{flex:1;min-width:0;font-size:13px;font-weight:700;display:flex;flex-direction:column;gap:2px}
.mrow .tt .ln{display:flex;align-items:center;gap:6px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.mrow .res{font-weight:900;font-size:15px}.mrow .res.soon{font-size:11px;font-weight:700;color:var(--muted)}
/* TABLES / BRACKET / H2H */
.grid2{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:13px}
.gtab{border:1px solid var(--line);border-radius:var(--r-sm);overflow:hidden;background:var(--card)}
.gtab h4{margin:0;background:linear-gradient(135deg,var(--blue),var(--indigo));color:#fff;padding:9px 12px;font-size:13.5px}
.gtab table{width:100%;border-collapse:collapse;font-size:11.5px;table-layout:fixed}.gtab td,.gtab th{padding:6px 3px;text-align:center;border-bottom:1px solid var(--line2)}
.gtab th{font-size:10px;text-transform:uppercase;color:var(--muted)}.gtab td:first-child,.gtab th:first-child{text-align:left}
.gtab th:nth-child(n+2),.gtab td:nth-child(n+2){width:20px}
.gtab th.gd,.gtab td.gd{width:26px}
.gtab td.gd.pos{color:var(--up);font-weight:800}.gtab td.gd.neg{color:var(--down);font-weight:800}
.gtab td:first-child .flag-img,.gtab td:first-child .flagfb{margin-right:7px}
@media(min-width:561px){.grid2{grid-template-columns:repeat(auto-fill,minmax(420px,1fr))}.gtab td,.gtab th{padding:7px 6px}.gtab th:nth-child(n+2),.gtab td:nth-child(n+2){width:30px}.gtab th.gd,.gtab td.gd{width:38px}}
.gtab tr.qual td:first-child{box-shadow:inset 3px 0 0 var(--grass)}
.bracket{display:flex;gap:20px;overflow-x:auto;padding:4px 2px 12px;-webkit-overflow-scrolling:touch}
.round{display:flex;flex-direction:column;justify-content:space-around;gap:12px;min-width:175px}
.round h3{font-size:11px;text-transform:uppercase;letter-spacing:.6px;color:var(--muted);text-align:center;margin:0 0 4px;font-weight:800}
.tie{background:var(--soft);border:1px solid var(--line);border-radius:12px;padding:8px 10px;box-shadow:var(--shs)}
.tie .row{display:flex;justify-content:space-between;gap:8px;padding:2px 0;font-size:12px}
.tie .meta{font-size:9.5px;color:var(--muted);text-align:center;margin-top:3px}
.h2h-pick{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin-bottom:16px}
select{font-size:14px;padding:10px 12px;border-radius:11px;border:1px solid var(--line);font-weight:700;color:var(--ink);background:var(--soft);font-family:inherit;flex:1;min-width:130px}
.h2h-grid{display:grid;grid-template-columns:1fr 78px 1fr;gap:8px;align-items:center}
.h2h-cell{padding:11px 6px;border-radius:11px;background:var(--soft);text-align:center;font-weight:800;font-size:13px;word-break:break-word}
.h2h-cell.win{background:color-mix(in srgb,var(--grass) 16%,transparent);color:var(--grass-deep)}
.h2h-lbl{text-align:center;color:var(--muted);font-size:11px;font-weight:700;text-transform:uppercase}
.h2h-head{font-size:14px;font-weight:800;text-align:center;padding:9px 4px;border-radius:12px;color:#fff}
/* MODAL */
.overlay{position:fixed;inset:0;background:rgba(5,10,25,.6);backdrop-filter:blur(6px);display:none;place-items:center;z-index:60;padding:14px;animation:rise .25s var(--ease)}
.overlay.open{display:grid}
.modal{background:var(--bg);border:1px solid var(--line);border-radius:22px;max-width:540px;width:100%;max-height:88vh;overflow:auto;box-shadow:var(--sh)}
.mhead{background:linear-gradient(135deg,var(--blue-deep),var(--indigo));color:#fff;padding:18px;display:flex;align-items:center;gap:13px;position:sticky;top:0;z-index:2}
.mhead .ava{width:46px;height:46px;font-size:17px}.mhead h3{margin:0;font-size:19px}.mhead p{margin:2px 0 0;opacity:.9;font-size:12.5px}
.mhead .x{margin-left:auto;background:rgba(255,255,255,.2);border:none;color:#fff;width:34px;height:34px;border-radius:50%;font-size:17px;cursor:pointer}
.mbody{padding:16px}
.statrow{display:flex;gap:9px;margin-bottom:14px}.stat{flex:1;background:var(--soft);border:1px solid var(--line2);border-radius:13px;padding:12px 6px;text-align:center}
.stat .v{font-size:22px;font-weight:900;color:var(--blue)}.stat .l{font-size:10.5px;color:var(--muted);text-transform:uppercase;font-weight:700}
.kbox{background:var(--soft);border:1px solid var(--line2);border-radius:12px;padding:11px 13px;font-size:13px;line-height:1.7}
.kchips{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:4px}
.kchip{display:inline-flex;align-items:center;gap:5px;background:var(--soft);border:1px solid var(--line2);border-radius:999px;padding:4px 10px;font-size:12px;font-weight:600}
.psheet{display:flex;flex-direction:column;gap:6px;max-height:42vh;overflow:auto;padding-right:3px}
.ps{display:grid;grid-template-columns:auto 1fr auto auto;gap:9px;align-items:center;background:var(--soft);border:1px solid var(--line2);border-radius:11px;padding:8px 10px;font-size:12.5px}
.ps .ph{font-size:9.5px;color:var(--muted);font-weight:800}.ps .mt{font-weight:700;display:flex;align-items:center;gap:5px;flex-wrap:wrap}
.ps .gp{font-weight:800;color:var(--blue)}.ps .rs{color:var(--muted);font-weight:700;font-size:11.5px}.ps .bd{font-weight:800;min-width:26px;text-align:right}
.ps.hit{background:color-mix(in srgb,var(--grass) 13%,transparent)}.ps.hit .bd{color:var(--grass-deep)}
.ps.close{background:color-mix(in srgb,var(--yellow) 15%,transparent)}.ps.miss .bd{color:var(--flat)}
.ps.pshead{background:none;border:none;padding:0 10px 2px;font-size:9.5px;text-transform:uppercase;letter-spacing:.03em}
.ps.pshead .mt,.ps.pshead .rs,.ps.pshead .bd{font-weight:800;color:var(--muted)}
h4{font-weight:800;letter-spacing:-.2px}
@media(max-width:560px){.wrap{padding:14px 11px 80px}.bar h1{font-size:18px}.sb .sc{font-size:28px}.fbody{gap:4px}.team .tn{font-size:12.5px}.card{padding:15px}}

/* ===================== POLISH PASS ===================== */
:root{--grad:linear-gradient(135deg,#2563ff 0%,#5b6cff 52%,#8b5cf6 100%)}
[data-theme=dark]{--bg:#080c1a;--card:rgba(255,255,255,.05);--soft:rgba(255,255,255,.05);--soft2:rgba(255,255,255,.09)}
body{letter-spacing:-.011em}
.tot,.bpv,.gv,.mx-score,.stat .v,.reg .pcard .v,.rk .pos,.sb .sc,.cvn{font-variant-numeric:tabular-nums}
/* sticky flikrad */
.tabs{position:sticky;top:0;z-index:30;margin:0 -16px 16px;padding:9px 16px;background:color-mix(in srgb,var(--bg) 80%,transparent);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}
.tab{transition:transform .2s var(--ease),background .25s,color .25s,box-shadow .25s}
.tab:active{transform:translateY(1px)}
.tab.active{background:var(--grad);box-shadow:0 9px 22px -11px #5b6cff}
/* scrollbars / fokus / markering */
*{scrollbar-width:thin;scrollbar-color:var(--line) transparent}
::-webkit-scrollbar{width:9px;height:9px}::-webkit-scrollbar-thumb{background:var(--line);border-radius:9px;border:2px solid transparent;background-clip:padding-box}::-webkit-scrollbar-thumb:hover{background:var(--muted)}
:focus-visible{outline:2px solid var(--blue);outline-offset:2px;border-radius:8px}
::selection{background:color-mix(in srgb,var(--blue) 28%,transparent)}
/* mjuk vy-övergång */
.view.active{animation:viewin .45s var(--ease)}
@keyframes viewin{from{opacity:0;transform:translateY(10px) scale(.995)}to{opacity:1;transform:none}}
/* gradient-accenter */
.bar h1{background:var(--grad);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.mebanner{background:var(--grad)}
.h2h-head{background:var(--grad)!important}
/* prispall-lyx */
.podium{max-width:480px}
.pod .step{position:relative;overflow:hidden;animation:grow .6s var(--ease) both}
@keyframes grow{from{height:0;opacity:0}}
.pod.p1 .step{background:var(--grad)}
.pod .step::after{content:"";position:absolute;inset:0;background:linear-gradient(115deg,transparent 35%,rgba(255,255,255,.4) 50%,transparent 65%);transform:translateX(-130%);animation:shine 4s ease-in-out infinite}
@keyframes shine{0%,55%{transform:translateX(-130%)}100%{transform:translateX(130%)}}
.pod .ava{transition:transform .3s var(--ease)}.pod:hover .ava{transform:translateY(-4px) scale(1.05)}
/* spelade matchkort */
.mx-row.played{background:color-mix(in srgb,var(--grass) 6%,transparent);border-color:color-mix(in srgb,var(--grass) 16%,transparent)}
.ftb{font-size:9px;font-weight:900;background:var(--grass);color:#fff;border-radius:5px;padding:1px 6px;letter-spacing:.5px}
/* mästartips-stapel */
.cv{display:flex;flex-direction:column;gap:8px}
.cvrow{display:flex;align-items:center;gap:9px;font-size:13px;font-weight:700}
.cvname{width:130px;display:flex;align-items:center;gap:7px;flex:0 0 auto;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.cvbar{flex:1;height:18px;background:var(--soft);border-radius:7px;overflow:hidden}
.cvfill{height:100%;background:var(--grad);border-radius:7px;transition:width .9s var(--ease)}
.cvn{width:22px;text-align:right;color:var(--muted);font-weight:800}
.ic{display:inline-flex;width:16px;height:16px;vertical-align:-3px;margin-right:7px;flex:0 0 auto}.ic svg{width:100%;height:100%}.tab{display:inline-flex;align-items:center}.ttl .ic{margin-right:8px}
.h2h-cols{display:grid;grid-template-columns:1fr 1fr;gap:12px}
@media(max-width:720px){.h2h-cols{grid-template-columns:1fr}}
.h2col{border:1px solid var(--line);border-radius:14px;overflow:hidden;background:var(--soft)}
.h2col .h2head{padding:11px 12px;color:#fff;display:flex;align-items:center;gap:10px}
.h2col .h2head .ava{width:38px;height:38px;font-size:14px;border:2px solid rgba(255,255,255,.5);background:rgba(255,255,255,.18)}
.h2col .h2head .hn{font-weight:800;font-size:14px;line-height:1.1}
.h2col .h2head .hp{font-size:11px;opacity:.92;font-weight:600}
.h2col .h2body{padding:12px}.h2col .kbox{font-size:12px}.h2col .psheet{max-height:none}
.brow{display:flex;align-items:center;gap:6px;padding:3px 0;font-size:12.5px}
.brow .slot{color:var(--muted);font-size:11px;font-weight:600}
.brow .bt{font-weight:700}
.brow.win .bt{font-weight:800;color:var(--grass-deep)}
.brow .chk{margin-left:auto;color:var(--blue);font-weight:900}
.brow.mine{background:color-mix(in srgb,var(--blue) 8%,transparent);border-radius:6px;padding-left:5px;padding-right:5px}
.ksbox{background:var(--soft);border:1px solid var(--line2);border-radius:14px;padding:13px;margin-bottom:14px}
.kstot{display:flex;justify-content:space-between;align-items:center;font-weight:800;font-size:14px;margin-bottom:9px;padding-bottom:9px;border-bottom:1px solid var(--line2)}
.kstot b{font-size:20px;color:var(--blue)}
.ksrow{display:flex;align-items:center;gap:8px;font-size:12.5px;padding:3px 0;font-weight:600}
.ksrow .ksv{margin-left:auto;color:var(--muted)}
.ksrow .ksp{width:30px;text-align:right;font-weight:800;color:var(--ink)}
.koround{display:flex;gap:6px;overflow-x:auto;margin-bottom:14px;padding-bottom:2px;scrollbar-width:none}
.koround::-webkit-scrollbar{display:none}
.krchip{flex:0 0 auto;border:1px solid var(--line);background:var(--soft);color:var(--muted);font-weight:700;font-size:12.5px;border-radius:999px;padding:8px 14px;cursor:pointer;transition:.2s var(--ease)}
.krchip:active{transform:translateY(1px)}
.krchip.active{background:var(--grad);color:#fff;border-color:transparent;box-shadow:0 8px 18px -10px #5b6cff}
.kogrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(215px,1fr));gap:11px}
.kocard{background:var(--soft);border:1px solid var(--line2);border-radius:13px;padding:11px 13px;transition:.2s var(--ease)}
.kocard:hover{box-shadow:var(--shs)}
.kometa{font-size:9.5px;color:var(--muted);font-weight:800;text-transform:uppercase;letter-spacing:.4px;margin-bottom:8px}
.kocard .brow{padding:5px 0}.kocard .brow+.brow{border-top:1px solid var(--line2)}
.hdr{position:relative;overflow:hidden;border-radius:22px;padding:20px 20px 15px;margin-bottom:16px;color:#fff;background:linear-gradient(130deg,#1b39d6 0%,#3b56ff 42%,#7c3aed 100%);box-shadow:0 20px 46px -20px rgba(40,60,210,.65)}
.hdr-deco{position:absolute;inset:0;pointer-events:none;background:radial-gradient(140px 140px at 92% -20%,rgba(255,255,255,.28),transparent 60%),radial-gradient(180px 180px at 6% 130%,rgba(255,255,255,.12),transparent 60%)}
.hdr::after{content:"";position:absolute;right:-46px;bottom:-66px;width:190px;height:190px;border:2px solid rgba(255,255,255,.16);border-radius:50%;pointer-events:none}
.hdr::before{content:"";position:absolute;left:0;right:0;bottom:0;height:3px;background:linear-gradient(90deg,transparent,rgba(255,255,255,.5),transparent)}
.hdr-main{position:relative;z-index:2;display:flex;align-items:center;gap:15px}
.ballwrap{position:relative;width:60px;height:66px;flex:0 0 auto;-webkit-tap-highlight-color:transparent}
.ball{position:absolute;top:2px;left:6px;width:48px;height:48px;animation:bob 1.5s cubic-bezier(.5,0,.5,1) infinite;-webkit-tap-highlight-color:transparent;-webkit-touch-callout:none;user-select:none;-webkit-user-select:none}
.egg-ball{position:fixed;z-index:65;pointer-events:none;will-change:transform,top,left;filter:drop-shadow(0 6px 10px rgba(0,10,40,.35))}
.egg-ball svg{width:100%;height:100%;display:block}
.ball svg{width:100%;height:100%;display:block;animation:roll 3s linear infinite;filter:drop-shadow(0 7px 9px rgba(0,0,0,.3))}
@keyframes roll{to{transform:rotate(360deg)}}
@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-11px)}}
.ballsh{position:absolute;bottom:3px;left:13px;width:34px;height:8px;background:rgba(0,0,0,.32);border-radius:50%;filter:blur(2px);animation:ballsh 1.5s cubic-bezier(.5,0,.5,1) infinite}
@keyframes ballsh{0%,100%{transform:scale(1);opacity:.5}50%{transform:scale(.62);opacity:.28}}
.hdr-txt{flex:1;min-width:0}
.hdr h1{margin:0;font-size:27px;font-weight:900;letter-spacing:-.6px;line-height:1.05;color:#fff;-webkit-text-fill-color:#fff;text-shadow:0 2px 10px rgba(0,0,0,.2)}
.hdr p{margin:4px 0 0;font-size:13px;font-weight:600;opacity:.92}
.hdr .tog{flex:0 0 auto;width:42px;height:42px;border-radius:13px;border:1px solid rgba(255,255,255,.3);background:rgba(255,255,255,.16);backdrop-filter:blur(8px);color:#fff;font-size:18px;cursor:pointer;transition:.3s var(--ease)}
.hdr .tog:hover{transform:translateY(-2px) rotate(-10deg);background:rgba(255,255,255,.26)}
.hdr-foot{position:relative;z-index:2;margin-top:14px;display:flex;align-items:center;gap:7px;font-size:11.5px;font-weight:600;opacity:.95}
.hdr-foot .dot{width:8px;height:8px;border-radius:50%;background:#7CFFB2;animation:pulse 1.8s infinite}
@media(max-width:560px){.hdr h1{font-size:22px}.hdr{padding:17px 16px 13px}}
.hdr-foot{flex-wrap:wrap}
.hdr-me{margin-left:auto;display:inline-flex;align-items:center;gap:7px;font-weight:700}
.hdr select{background:rgba(255,255,255,.18);border:1px solid rgba(255,255,255,.32);color:#fff;border-radius:9px;padding:5px 10px;font-weight:700;font-size:12.5px;font-family:inherit;backdrop-filter:blur(8px);cursor:pointer;min-width:auto;flex:0 0 auto}
.hdr select:hover{background:rgba(255,255,255,.26)}
.hdr select option{color:#0b1530}
@media(max-width:560px){.hdr-me{margin-left:0;width:100%}}
.msel{position:relative;display:inline-block}
.msel-btn{display:inline-flex;align-items:center;gap:7px;background:rgba(255,255,255,.18);border:1px solid rgba(255,255,255,.32);color:#fff;border-radius:11px;padding:5px 10px 5px 6px;font-weight:700;font-size:12.5px;cursor:pointer;backdrop-filter:blur(8px);transition:.2s var(--ease);font-family:inherit;max-width:200px}
.msel-btn:hover{background:rgba(255,255,255,.27)}
.msel-btn .msl{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.msel-btn .msl.muted{opacity:.9;font-weight:600;padding-left:4px}
.msa{width:22px;height:22px;border-radius:50%;display:grid;place-items:center;color:#fff;font-size:9px;font-weight:800;flex:0 0 auto;box-shadow:0 1px 3px rgba(0,0,0,.3)}
.msc{margin-left:2px;font-size:11px;opacity:.85;transition:transform .2s var(--ease)}
.msel.open .msc{transform:rotate(180deg)}
.msel-pop{position:fixed;min-width:215px;max-height:330px;overflow:auto;background:var(--card);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border:1px solid var(--line);border-radius:15px;box-shadow:0 26px 54px -18px rgba(0,0,0,.5);padding:6px;z-index:1000;opacity:0;transform:translateY(-6px) scale(.97);pointer-events:none;transition:.18s var(--ease)}
.msel-pop.open{opacity:1;transform:none;pointer-events:auto}
.mopt{display:flex;align-items:center;gap:9px;width:100%;border:none;background:transparent;color:var(--ink);font-weight:600;font-size:13px;padding:8px 10px;border-radius:10px;cursor:pointer;text-align:left;font-family:inherit}
.mopt:hover{background:var(--soft)}
.mopt.sel{background:color-mix(in srgb,var(--blue) 13%,transparent);color:var(--blue);font-weight:800}
.mopt .mck{margin-left:auto;color:var(--blue);font-weight:900}
/* svensk flagg-känsla: gult kors över blå ytor */
.hdr-deco{background:
  radial-gradient(140px 140px at 92% -20%,rgba(255,255,255,.26),transparent 60%),
  radial-gradient(180px 180px at 6% 130%,rgba(255,255,255,.12),transparent 60%),
  linear-gradient(90deg,transparent 29%,rgba(255,200,0,.22) 29% 36%,transparent 36%),
  linear-gradient(180deg,transparent 41%,rgba(255,200,0,.22) 41% 57%,transparent 57%)}
.mebanner{position:relative;overflow:hidden}
.mebanner::before{content:"";position:absolute;inset:0;pointer-events:none;background:
  linear-gradient(90deg,transparent 29%,rgba(255,200,0,.24) 29% 36%,transparent 36%),
  linear-gradient(180deg,transparent 40%,rgba(255,200,0,.24) 40% 60%,transparent 60%)}
.mebanner>*{position:relative;z-index:1}
/* ===== Sverige-tema: blått fält + guldkors ===== */
.hdr{background:linear-gradient(135deg,#0a57c0 0%,#1572d8 50%,#064a92 100%)}
.hdr-deco{background:
  radial-gradient(150px 150px at 93% -25%,rgba(255,255,255,.20),transparent 60%),
  radial-gradient(170px 170px at 5% 130%,rgba(255,255,255,.10),transparent 60%),
  linear-gradient(90deg,transparent 30%,rgba(255,204,2,.85) 30% 37.5%,transparent 37.5%),
  linear-gradient(180deg,transparent 40%,rgba(255,204,2,.85) 40% 58%,transparent 58%)}
.hdr h1,.hdr p,.hdr-foot{text-shadow:0 1px 6px rgba(0,40,90,.45)}
.mebanner{background:linear-gradient(135deg,#0a57c0,#1572d8 55%,#064a92)}
.mebanner::before{background:
  linear-gradient(90deg,transparent 30%,rgba(255,204,2,.8) 30% 37.5%,transparent 37.5%),
  linear-gradient(180deg,transparent 36%,rgba(255,204,2,.8) 36% 64%,transparent 64%)}
.mebanner .bn,.mebanner .bl,.mebanner .bpv,.mebanner .bpu,.mebanner .bps{text-shadow:0 1px 5px rgba(0,40,90,.4)}
.mebanner::before{display:none}
.mebanner{box-shadow:inset 5px 0 0 rgba(255,204,2,.95)}
/* ===== ARENA: fotbollsplan-header ===== */
.hdr{color:#fff;background:
  repeating-linear-gradient(90deg, rgba(255,255,255,.055) 0 44px, rgba(0,0,0,.045) 44px 88px),
  linear-gradient(165deg,#0e8a4d 0%,#0a6a36 100%);
  box-shadow:0 20px 46px -20px rgba(6,80,40,.6)}
.hdr-deco{inset:9px;border:2px solid rgba(255,255,255,.42);border-radius:11px;background:
  linear-gradient(90deg,transparent calc(50% - 1px),rgba(255,255,255,.42) calc(50% - 1px),rgba(255,255,255,.42) calc(50% + 1px),transparent calc(50% + 1px))}
.hdr::after{content:"";position:absolute;left:50%;top:50%;width:92px;height:92px;transform:translate(-50%,-50%);border:2px solid rgba(255,255,255,.42);border-radius:50%;background:none;right:auto;bottom:auto}
.hdr::before{display:none}
.hdr h1{text-shadow:0 1px 2px rgba(0,0,0,.55),0 2px 12px rgba(0,0,0,.42);letter-spacing:-.4px}
.hdr p,.hdr-foot{text-shadow:0 1px 7px rgba(0,0,0,.45)}
.hdr-foot .dot{background:#FFCC02;box-shadow:0 0 0 0 rgba(255,204,2,.6)}
.ball svg{filter:drop-shadow(0 7px 10px rgba(0,0,0,.45))}
.hdr .tog{border-color:rgba(255,255,255,.35);background:rgba(255,255,255,.16)}
@media(max-width:560px){
 .hdr{padding:16px 15px 12px}
 .hdr-main{gap:11px}
 .ballwrap{width:46px;height:50px}
 .ball{width:38px;height:38px;left:4px}
 .ballsh{width:26px;left:9px}
 .hdr h1{font-size:19px;line-height:1.08;word-break:break-word}
 .hdr p{font-size:11.5px}
 .hdr .tog{width:38px;height:38px;font-size:16px}
 .hdr-foot{font-size:11px;gap:5px}
 .msel-btn{max-width:165px}
 .ttl{flex-wrap:wrap;gap:6px}
 .ttl .more{margin-left:0;flex-basis:100%}
 .scoregrp{gap:8px}
 .tab[data-view="h2h"]{display:none}
 #h2h{display:none!important}
}
.sgl{display:flex;flex-direction:column;align-items:center;gap:3px;flex:0 0 auto;min-width:50px}
.sgl .cnt{font-size:10.5px}
@media(max-width:560px){.upd-extra{display:none}}
.mday{font-size:11px;font-weight:800;color:var(--muted);text-transform:uppercase;letter-spacing:.6px;margin:14px 4px 8px;display:flex;align-items:center;gap:8px}
.mday::after{content:"";flex:1;height:1px;background:var(--line2)}
.pp2[data-name]{cursor:pointer}
/* sök/sortering i poänglistan */
.rk-ctrl{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px}
#rkSearch{flex:1;min-width:150px;padding:9px 12px;border-radius:11px;border:1px solid var(--line);background:var(--soft);color:var(--ink);font-family:inherit;font-size:13px}
.rk-sort{display:flex;gap:4px;background:var(--soft);border-radius:11px;padding:3px}
.rk-sort button{border:none;background:transparent;color:var(--muted);font-weight:700;font-size:12px;padding:6px 10px;border-radius:8px;cursor:pointer;font-family:inherit}
.rk-sort button.active{background:var(--card);color:var(--blue);box-shadow:var(--shs)}
/* fokus/kontrast */
:focus-visible{outline:2.5px solid var(--blue);outline-offset:2px;border-radius:8px}
.rk:focus-visible,.mx-row:focus-visible,.tab:focus-visible{outline:2.5px solid var(--blue);outline-offset:2px}
/* app-lik bottom-nav på mobil */
@media(max-width:560px){
 .tabs{position:fixed;top:auto;bottom:0;left:0;right:0;margin:0;padding:6px 4px;gap:0;justify-content:space-around;background:color-mix(in srgb,var(--bg) 90%,transparent);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border-top:1px solid var(--line);border-radius:0;overflow:visible;z-index:60}
 .tab{flex:1;flex-direction:column;gap:3px;font-size:9px;line-height:1.05;text-align:center;padding:6px 2px;border:none;background:transparent;color:var(--muted);box-shadow:none;border-radius:10px;min-width:0}
 .tab .ic{margin-right:0;width:21px;height:21px}
 .tab.active{background:transparent;color:var(--blue);box-shadow:none}
 .wrap{padding-bottom:76px}
}
@media(min-width:561px){.tabs{position:static;margin:0 0 16px;padding:0;background:none;backdrop-filter:none;-webkit-backdrop-filter:none}}
@media(max-width:560px){.mebanner .bn{white-space:normal;line-height:1.22;font-size:14px}.mebanner .bl{font-size:10px}.mebanner{gap:11px}}
@media(max-width:560px){.hdr-foot{gap:8px}.hdr-me{width:100%;margin-left:0;margin-top:2px;display:flex;align-items:center;gap:7px}.hdr-me .msel{flex:1;min-width:0}.hdr-me .msel-btn{max-width:none;width:100%;justify-content:flex-start}.hdr-me .msel-btn .msl{flex:1;text-align:left}}
@media(max-width:560px){.hdr{display:flex;flex-direction:column;justify-content:center;min-height:142px}.hdr-foot .dot,.hdr-foot #updatedAt{display:none}.hdr-foot{margin-top:12px}}
.dash-grid{display:grid;grid-template-columns:1fr 312px;gap:18px;align-items:start}
.dash-main{min-width:0}
.dash-side{position:sticky;top:14px}
.uprow{display:flex;align-items:center;gap:11px;padding:9px 4px;border-radius:10px;cursor:pointer;border-bottom:1px solid var(--line2)}
.uprow:last-child{border-bottom:none}.uprow:hover{background:var(--soft)}
.utime{flex:0 0 auto;width:48px;text-align:center;font-size:10.5px;font-weight:800;color:var(--blue);line-height:1.25;display:flex;flex-direction:column}
.utime span{color:var(--muted);font-weight:700}
.ubody{flex:1;min-width:0}
.uteams{font-size:12.5px;font-weight:700;display:flex;align-items:center;gap:5px;flex-wrap:wrap}
.uteams .uvs{color:var(--muted)}.uteams .un{white-space:nowrap}
.uslot{font-size:11.5px;color:var(--muted);font-weight:600}
.utag{font-size:9px;color:var(--muted);font-weight:800;text-transform:uppercase;letter-spacing:.3px;margin-top:2px}
@media(max-width:860px){.dash-grid{grid-template-columns:1fr}.dash-side{position:static}}
.duo{display:grid;grid-template-columns:1.45fr 1fr;gap:18px;align-items:stretch;margin-bottom:16px}
.duo .card{margin-bottom:0;height:100%}
.duo #upcoming{display:flex;flex-direction:column}
@media(max-width:760px){.duo{grid-template-columns:1fr;gap:16px}}
.mgroup{position:relative;margin-bottom:16px}
.mgroup>.card:first-child{margin-bottom:0}
.mgroup>.card:last-child{margin-bottom:0}
.mlink{position:relative;height:13px;z-index:4}
.mlink i{position:absolute;top:-7px;height:27px;width:6px;border-radius:4px;background:linear-gradient(180deg,var(--blue),var(--indigo));box-shadow:0 3px 8px -2px var(--blue)}
.mlink i.l{left:calc(50% - 66px)}.mlink i.r{left:calc(50% + 60px)}
@media(max-width:560px){.mlink i.l{left:calc(50% - 46px)}.mlink i.r{left:calc(50% + 40px)}}
.sgl{min-width:62px}
.slrow{display:flex;align-items:center;gap:6px;justify-content:center}
.wf{display:inline-flex;align-items:center;flex:0 0 auto}
.wf.draw{width:17px;height:17px;border-radius:50%;background:var(--soft2);color:var(--muted);font-size:10px;font-weight:800;justify-content:center}
.scoregrp{flex-wrap:nowrap;gap:11px}
.rchip{display:inline-flex;align-items:center;gap:7px;background:var(--soft2);border:1px solid var(--line2);border-radius:11px;padding:5px 11px;flex:0 0 auto}
.rchip .wf{display:inline-flex}
.rsc{font-weight:900;font-size:15px;letter-spacing:.3px}
.cntr{margin-left:auto;flex:0 0 auto;font-size:11px;font-weight:700;color:var(--muted);white-space:nowrap}
@media(max-width:560px){.rsc{font-size:14px}.cntr{display:none}}
.tvsub{font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:.5px;color:var(--ink2);margin:0 0 9px;display:flex;align-items:center;gap:6px}
.cvrow{cursor:pointer;border-radius:9px;padding:5px 5px;transition:.15s var(--ease)}
.cvrow:hover{background:var(--soft)}
.t-ex{color:var(--grass-deep);font-weight:800}
.t-ru{color:#a35400;font-weight:800}
[data-theme=dark] .t-ex{color:#3fd98a}
[data-theme=dark] .t-ru{color:#ffb454}
.cvk{font-weight:700;font-size:13px;white-space:nowrap}
.champ-wrap .scoregrp:first-of-type{border-top:none}
.mdaygroup{background:var(--card);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);border:1px solid var(--line);border-radius:var(--r);box-shadow:var(--sh);padding:9px 15px 6px;margin-bottom:14px}
.mdaygroup .mday{margin:5px 2px 6px}
.mdc{font-weight:700;color:var(--muted);text-transform:none;letter-spacing:0;font-size:10.5px}
.mdaygroup .mx-row{background:none;border:none;border-radius:9px;box-shadow:none;padding:11px 6px;margin-bottom:0;border-bottom:1px solid var(--line2)}
.mdaygroup .mx-row:last-child{border-bottom:none}
.mdaygroup .mx-row:hover{background:var(--soft)}
.mdaygroup .mx-row.today{box-shadow:inset 3px 0 0 var(--grass)}
.mdaygroup .mx-row.next{box-shadow:inset 3px 0 0 var(--blue);background:color-mix(in srgb,var(--blue) 7%,transparent)}
.mdaygroup .mx-row.today,.mdaygroup .mx-row.next{box-shadow:none;background:none}
.mdaygroup .mx-row.today:hover,.mdaygroup .mx-row.next:hover{background:var(--soft)}
.fcard{position:relative}
.mstamp{display:none;position:absolute;top:14px;right:16px;z-index:6;transform:rotate(-9deg);align-items:center;font-weight:900;font-size:14px;letter-spacing:2.5px;text-transform:uppercase;color:#1f9c5a;border:3px solid #1f9c5a;border-radius:9px;padding:5px 11px;opacity:.5;pointer-events:none;box-shadow:inset 0 0 0 2px rgba(31,156,90,.25);text-shadow:0 1px 0 rgba(255,255,255,.2)}
@media(max-width:560px){.mstamp{font-size:11px;letter-spacing:1.5px;padding:4px 8px;top:10px;right:10px}}
.mstamp{position:static;top:auto;right:auto;display:inline-flex}
#fStamp{display:none;margin:0 auto 8px}
.mdaygroup .mx-row{position:relative}
.mdaygroup .mx-row .mstamp{position:absolute;right:8px;top:50%;transform:translateY(-50%) rotate(-9deg);font-size:8.5px;letter-spacing:1px;padding:3px 7px;border-width:2px}
@media(max-width:560px){.mdaygroup .mx-row .mstamp{font-size:7.5px;padding:2px 5px;right:4px}}
/* Matcher: stämpel uppe i högra hörnet, roterad andra hållet */
.mdaygroup .mx-row .mstamp{top:8px;transform:translateY(0) rotate(9deg)}
/* Hem: stämpel rak och lite högre upp */
#fStamp{margin:-8px auto 16px;transform:none}
.mx-cscol{display:flex;flex-direction:column;align-items:center;gap:5px}
.mdaygroup .mx-row .mstamp{position:static;top:auto;right:auto;transform:rotate(-4deg);font-size:7.5px;letter-spacing:.8px;padding:2px 6px;border-width:2px}
.mdaygroup .mx-row .mstamp{position:absolute;top:8px;right:8px;transform:rotate(-8deg);font-size:8.5px;letter-spacing:1px;padding:3px 7px;border-width:2px}
.mdaygroup .mx-row .mstamp{transform:rotate(8deg);font-size:10px;letter-spacing:1.2px;padding:4px 9px}
.mdaygroup .mx-team{font-size:15px}
.mdaygroup .mx-score.done{font-size:18px;padding:6px 12px}
.mdaygroup .mx-score{min-width:66px}
.mdaygroup .mx-row .mstamp{position:static;top:auto;right:auto;margin-left:auto}
.mdaygroup .mx-meta{flex-wrap:wrap}
.mdaygroup .mx-row .mstamp{transform:translateY(5px) rotate(8deg)}
/* ===== UX-PASS 1: identitet, kontrast, rörelse ===== */
/* enhetlig blå header (behåller planlinjer) */
.hdr{background:repeating-linear-gradient(90deg,rgba(255,255,255,.05) 0 44px,rgba(0,0,0,.04) 44px 88px),linear-gradient(135deg,#0b3bd6 0%,#2f5bff 50%,#5b6cff 100%);box-shadow:0 20px 46px -20px rgba(20,40,160,.6)}
/* nedtonad mesh */
body::before{opacity:.5}
/* ta bort häftklammer-stagen, behåll luft mellan korten */
.mlink{display:none}
.mgroup>.card:first-child{margin-bottom:14px}
/* högre kontrast på text */
[data-theme=light]{--muted:#586883;--ink2:#45556f}
/* reducerad rörelse */
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation-duration:.001ms!important;animation-iteration-count:1!important;transition-duration:.001ms!important;scroll-behavior:auto!important}}
/* mobilnav: större tryckyta */
@media(max-width:560px){.tabs{padding:7px 4px 9px}.tab{padding:8px 2px;font-size:9.5px}.tab .ic{width:22px;height:22px}}
.mehint{background:var(--soft);border:1px dashed var(--line);border-radius:16px;padding:14px 16px;font-size:13px;font-weight:600;color:var(--ink2);margin-bottom:16px}
.infobtn{margin-left:8px;border:1px solid var(--line);background:var(--soft);color:var(--blue);font-weight:700;font-size:11.5px;border-radius:999px;padding:4px 11px;cursor:pointer;font-family:inherit}
.infobtn:hover{background:var(--soft2)}
.emptynote{background:var(--soft);border:1px dashed var(--line);border-radius:14px;padding:14px 16px;font-size:13px;font-weight:600;color:var(--ink2);margin-bottom:14px}
.needpick .msel-btn{animation:needpick 1.9s ease-in-out infinite}
@keyframes needpick{0%,100%{box-shadow:0 0 0 0 rgba(255,255,255,0)}50%{box-shadow:0 0 0 4px rgba(255,255,255,.4)}}
/* Tippade mästare & skyttekung: linjera */
#champviz .scoregrp{align-items:center;gap:12px}
#champviz .rchip{flex:0 0 170px;width:170px;justify-content:flex-start}
#champviz .rchip .cvk{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
#champviz .ppl{flex:1}
#champviz .cntr{flex:0 0 auto;width:44px;text-align:right}
@media(max-width:560px){#champviz .rchip{flex-basis:124px;width:124px}}
.mdaygroup .mx-guess.exact{background:color-mix(in srgb,var(--grass) 7%,transparent);border-color:color-mix(in srgb,var(--grass) 16%,transparent)}
.mdaygroup .mx-guess.right{background:color-mix(in srgb,var(--yellow) 9%,transparent);border-color:color-mix(in srgb,var(--yellow-deep) 16%,transparent)}
.mdaygroup .mx-guess.wrong{background:color-mix(in srgb,var(--down) 7%,transparent);border-color:color-mix(in srgb,var(--down) 16%,transparent)}
/* ===== mjukare skuggor ===== */
[data-theme=light]{--sh:0 10px 30px -18px rgba(20,40,90,.20);--shs:0 4px 13px -8px rgba(20,40,90,.15)}
[data-theme=dark]{--sh:0 16px 40px -22px rgba(0,0,0,.55);--shs:0 8px 20px -13px rgba(0,0,0,.5)}
.hdr{box-shadow:0 14px 36px -22px rgba(20,40,160,.42)}
.tab.active{box-shadow:0 5px 14px -8px rgba(91,108,255,.45)}
.mebanner{box-shadow:inset 5px 0 0 rgba(255,204,2,.95),0 8px 22px -16px rgba(20,40,160,.34)}
.ava{box-shadow:0 1px 4px -1px rgba(0,0,0,.18)}
/* ===== Topp 3: stilren pall ===== */
.podium{display:grid;grid-template-columns:1fr 1.12fr 1fr;align-items:end;gap:12px;max-width:440px;margin:12px auto 6px}
.pod{display:flex;flex-direction:column;align-items:center;gap:6px;cursor:pointer;transition:transform .2s var(--ease)}
.pod:hover{transform:translateY(-3px)}
.pod .pod-cr{height:21px;font-size:19px;line-height:1}
.pod.p1{--ring:var(--gold)}.pod.p2{--ring:var(--silver)}.pod.p3{--ring:var(--bronze)}
.pod .ava{width:52px;height:52px;font-size:17px;box-shadow:0 0 0 3px var(--card),0 0 0 5px var(--ring)}
.pod.p1 .ava{width:62px;height:62px;font-size:20px}
.pod .nm{font-weight:800;font-size:12.5px;text-align:center;line-height:1.15;max-width:106px}
.pod .pts{font-weight:900;font-size:14px;color:var(--ink)}
.pod .ped{width:100%;margin-top:3px;border-radius:13px 13px 0 0;display:grid;place-items:center;font-weight:900;font-size:17px;color:var(--ink2);border:1px solid var(--line2);border-bottom:none;background:var(--soft)}
.pod.p1 .ped{height:60px;color:var(--ink);background:linear-gradient(180deg,color-mix(in srgb,var(--gold) 20%,var(--card)),var(--card))}
.pod.p2 .ped{height:46px;background:linear-gradient(180deg,color-mix(in srgb,var(--silver) 20%,var(--card)),var(--card))}
.pod.p3 .ped{height:34px;background:linear-gradient(180deg,color-mix(in srgb,var(--bronze) 24%,var(--card)),var(--card))}
.pod.me .nm{color:var(--blue)}
.pod.me .ava{box-shadow:0 0 0 3px var(--card),0 0 0 5px var(--blue)}
.podnote{text-align:center;font-size:12px;color:var(--muted);margin-top:10px}
/* gula planlinjer + gul undertext i headern */
.hdr-deco{border-color:rgba(255,206,0,.6);background:linear-gradient(90deg,transparent calc(50% - 1px),rgba(255,206,0,.6) calc(50% - 1px),rgba(255,206,0,.6) calc(50% + 1px),transparent calc(50% + 1px))}
.hdr::after{border-color:rgba(255,206,0,.6)}
.hdr p{color:#ffd24a}
.pod.p1 .ped{height:94px}
.pod.p2 .ped{height:66px}
.pod.p3 .ped{height:48px}
.pod{gap:7px}
.podium{margin-top:6px}
.hdr-deco{border-color:rgba(255,221,0,.95);border-width:2.5px;background:linear-gradient(90deg,transparent calc(50% - 1.5px),rgba(255,221,0,.95) calc(50% - 1.5px),rgba(255,221,0,.95) calc(50% + 1.5px),transparent calc(50% + 1.5px))}
.hdr::after{border-color:rgba(255,221,0,.95);border-width:2.5px}
.duocard{display:flex;flex-direction:column}
#podnote{margin-top:auto;padding-top:12px}
.rk.me{box-shadow:inset 0 0 0 2px var(--blue),0 5px 16px -14px rgba(37,99,255,.4)}
@media(min-width:561px){.hdr{display:flex;flex-direction:column;justify-content:center;min-height:162px;padding-top:24px;padding-bottom:18px}}
.rk.me{background:color-mix(in srgb,var(--blue) 7%,transparent);box-shadow:inset 0 0 0 1.5px color-mix(in srgb,var(--blue) 36%,transparent),0 4px 14px -16px rgba(37,99,255,.28);transform:none}
.mfilter2{margin-top:-4px}
.mfilter2 button{font-size:11.5px}
@media(max-width:560px){.mfilter2{flex-wrap:wrap}.mfilter2 button{flex:1 1 30%}}
/* ===== Matcher-fliken: sammanfattning, kompakt vy, sticky dag ===== */
.mxsum{font-size:12px;font-weight:600;color:var(--muted);margin:-2px 2px 12px;display:flex;flex-wrap:wrap;gap:5px;align-items:center}
.mxsum .mxs-main{font-weight:800;color:var(--ink2)}
.mxsum b{font-weight:800}
.ttl .more#mxJump{cursor:pointer}
.mxopts{display:flex;justify-content:flex-end;margin:-4px 2px 10px}
.mxr{margin-left:auto;display:inline-flex;align-items:center;gap:6px;flex-wrap:wrap;justify-content:flex-end}
.mxp{display:none;font-size:9.5px;font-weight:800;border-radius:6px;padding:2px 7px;background:var(--soft);color:var(--muted);text-transform:none;white-space:nowrap}
.mxp.exact{background:color-mix(in srgb,var(--grass) 18%,transparent);color:var(--grass-deep)}
.mxp.right{background:color-mix(in srgb,var(--yellow) 26%,transparent);color:#a35400}
.mxp.wrong{background:color-mix(in srgb,var(--down) 16%,transparent);color:#a8102b}
.mxp.pend{background:color-mix(in srgb,var(--blue) 10%,transparent);color:var(--blue)}
[data-theme=dark] .mxp.right{color:#ffb454}[data-theme=dark] .mxp.wrong{color:#ff8a9c}
.mdaygroup .mday{position:sticky;top:6px;z-index:6;background:color-mix(in srgb,var(--card) 92%,var(--bg));backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);padding:7px 8px;margin:0 -6px 6px;border-radius:9px}
@media(max-width:560px){.mdaygroup .mday{top:4px}}
.mxbar{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:14px}
.mxbar .mxstatus{flex:1 1 auto;margin-bottom:0}
.mxbar-right{display:flex;align-items:center;gap:8px;flex:0 0 auto;margin-left:auto}
.mxtype{min-width:auto;width:auto;flex:0 0 auto;padding:8px 12px;font-size:12.5px;border-radius:11px}
@media(max-width:560px){.mxbar-right{width:100%}.mxbar .mxstatus{flex:1 1 100%}.mxtype{flex:1}}
/* Matcher: nästa-match-hero + Kommande/Spelade-segment */
.mxbar-right{margin-left:0}
.mxseg{display:flex;gap:4px;background:var(--soft);border-radius:12px;padding:4px;margin-bottom:12px}
.mxseg button{flex:1;border:none;background:transparent;color:var(--muted);font-weight:800;font-size:13px;border-radius:9px;padding:9px;cursor:pointer;font-family:inherit;transition:.2s var(--ease)}
.mxseg button:active{transform:translateY(1px)}
.mxseg button.active{background:var(--card);color:var(--blue);box-shadow:var(--shs)}
.mxhero{cursor:pointer;margin-bottom:14px;padding:36px 16px;transition:transform .2s var(--ease)}
.mxhero .fbody{padding:6px 4px 4px}
.mxhero:hover{transform:translateY(-2px)}
/* ===== Prispall – gult & blått (matchar "Din ställning") ===== */
.podium{display:grid;grid-template-columns:1fr 1.15fr 1fr;align-items:end;gap:10px;max-width:460px;margin:16px auto 4px}
.pod{display:flex;flex-direction:column;align-items:center;gap:4px;cursor:pointer;transition:transform .25s var(--ease)}
.pod:hover{transform:translateY(-4px)}
.pod .ava{width:54px;height:54px;font-size:18px;border:none;box-shadow:0 7px 18px -8px rgba(15,35,90,.45)}
.pod.p1 .ava{width:66px;height:66px;font-size:21px;box-shadow:0 9px 22px -8px rgba(15,35,90,.5)}
.pod.me .ava{box-shadow:0 0 0 3px var(--card),0 0 0 5px var(--blue),0 7px 18px -8px rgba(37,99,255,.5)}
.pod .nm{font-weight:800;font-size:12.5px;text-align:center;line-height:1.15;max-width:104px;color:var(--ink);margin-top:7px}
.pod.p1 .nm{font-size:13.5px}
.pod.me .nm{color:var(--blue)}
.pod .pts{font-weight:900;font-size:14px;color:var(--ink)}
.pod.p1 .pts{font-size:15px;color:var(--blue-deep)}
[data-theme=dark] .pod.p1 .pts{color:var(--indigo)}
.pod .dut{display:inline-block;margin-top:3px;font-size:9px;font-weight:900;letter-spacing:.8px;background:var(--gold);color:#3a2a00;border-radius:999px;padding:2px 10px;box-shadow:0 2px 7px -2px rgba(243,176,21,.7)}
.pod .ped{width:100%;margin-top:6px;border-radius:14px 14px 0 0;display:grid;place-items:center;font-weight:900;font-size:18px;border:none;position:relative;overflow:hidden;color:#fff}
.pod .ped .ped-rank{position:relative;z-index:1;text-shadow:0 1px 4px rgba(0,30,80,.45)}
.pod.p1 .ped{height:96px;font-size:22px;color:#fff;background:linear-gradient(135deg,#0a57c0,#1572d8 55%,#064a92);box-shadow:inset 0 5px 0 rgba(255,204,2,.95),0 14px 28px -14px rgba(20,60,160,.6)}
.pod.p2 .ped{height:68px;color:#fff;background:linear-gradient(135deg,#2f6fd0,#4f86dd);box-shadow:inset 0 5px 0 rgba(208,217,233,.97),0 12px 24px -16px rgba(20,60,160,.5)}
.pod.p3 .ped{height:50px;color:#fff;background:linear-gradient(135deg,#5a83c8,#7099d6);box-shadow:inset 0 5px 0 rgba(216,151,95,.97),0 12px 24px -16px rgba(20,60,160,.45)}
.pod.p1 .ped::after{content:"";position:absolute;inset:0;background:linear-gradient(115deg,transparent 38%,rgba(255,255,255,.3) 50%,transparent 62%);transform:translateX(-130%);animation:shine 4.5s ease-in-out infinite}
.podnote{text-align:center;font-size:12px;color:var(--muted);margin-top:12px}
/* ===== Mobilmeny: motsatt tema för kontrast ===== */
@media(max-width:560px){
 [data-theme=light] .tabs{background:color-mix(in srgb,#0b1530 92%,transparent);border-top:1px solid rgba(255,255,255,.10)}
 [data-theme=light] .tab{color:rgba(234,240,255,.6)}
 [data-theme=light] .tab.active{color:#fff}
 [data-theme=dark] .tabs{background:color-mix(in srgb,#eef2fb 94%,transparent);border-top:1px solid rgba(11,21,48,.10)}
 [data-theme=dark] .tab{color:#5a6b86}
 [data-theme=dark] .tab.active{color:var(--blue)}
}
.mbadge{font-size:9px;font-weight:900;background:var(--yellow-deep);color:#3d2a00;border-radius:5px;padding:1px 6px;letter-spacing:.5px}
.mx-guess.pending{justify-content:center}
@media(max-width:560px){#standings #partCount{flex-basis:auto}#standings #poengInfo{margin-left:auto}.mxstatus{flex-wrap:wrap}.mxstatus button{flex:1 1 42%}}
/* ===== Intro "Avspark" – loading-screen + reveal, täcker hela sidan ===== */
.intro{position:fixed;inset:0;z-index:9999;pointer-events:none;overflow:hidden;animation:fxFail 4s linear forwards}
@keyframes fxFail{0%,97%{opacity:1;visibility:visible}100%{opacity:0;visibility:hidden}}
.intro .ibg{position:absolute;inset:0;overflow:hidden;background:linear-gradient(135deg,#0a3bd0 0%,#2f5bff 52%,#5b6cff 100%)}
.intro .decowrap{position:absolute;inset:0;animation:fxDrift 7s linear infinite}
.intro .cross{position:absolute;left:50%;top:50%;width:220vmax;height:220vmax;transform:translate(-50%,-50%);background:linear-gradient(90deg,transparent calc(50% - 2px),rgba(255,204,2,.26) calc(50% - 2px),rgba(255,204,2,.26) calc(50% + 2px),transparent calc(50% + 2px)),linear-gradient(0deg,transparent calc(50% - 2px),rgba(255,204,2,.26) calc(50% - 2px),rgba(255,204,2,.26) calc(50% + 2px),transparent calc(50% + 2px))}
.intro .deco{position:absolute;left:50%;top:50%;border-radius:50%;border:2px solid rgba(255,204,2,.5)}
.intro .ring1{width:38vmin;height:38vmin;margin:-19vmin}
.intro .ring2{width:66vmin;height:66vmin;margin:-33vmin;border-style:dashed;border-color:rgba(255,204,2,.3)}
.intro .wave{position:absolute;left:50%;top:50%;width:220vmax;height:220vmax;margin:-110vmax;border-radius:50%;border:.8vmin solid rgba(255,204,2,.85);opacity:0}
.intro .ball{position:absolute;left:50%;top:50%;width:30vmin;height:30vmin;max-width:150px;max-height:150px;transform:translate(-50%,-50%);filter:drop-shadow(0 1.4vmin 3vmin rgba(0,10,40,.45));animation:fxSpin 1.15s linear infinite}
.intro .ball svg{width:100%;height:100%;display:block}
.intro .load{position:absolute;left:50%;bottom:13vh;transform:translateX(-50%);color:rgba(255,255,255,.92);font-weight:800;font-size:13px;letter-spacing:.4px;text-shadow:0 1px 6px rgba(0,20,60,.5)}
@keyframes fxSpin{from{transform:translate(-50%,-50%) rotate(0)}to{transform:translate(-50%,-50%) rotate(360deg)}}
@keyframes fxDrift{from{transform:rotate(0)}to{transform:rotate(360deg)}}
.intro.reveal{animation:none;opacity:1;visibility:visible}
.intro.reveal .ibg{animation:fxIris .85s cubic-bezier(.66,0,.32,1) forwards}
.intro.reveal .ball{animation:fxBallOut .85s cubic-bezier(.6,0,.3,1) forwards}
.intro.reveal .wave{animation:fxWave .85s ease-out forwards}
.intro.reveal .load{animation:fxFade .3s ease forwards}
@keyframes fxIris{0%{clip-path:circle(150% at 50% 50%)}100%{clip-path:circle(0% at 50% 50%)}}
@keyframes fxBallOut{0%{transform:translate(-50%,-50%) scale(1) rotate(0)}55%{transform:translate(-50%,-50%) scale(1.08) rotate(45deg)}100%{transform:translate(-50%,-50%) scale(0) rotate(160deg);opacity:0}}
@keyframes fxWave{0%{transform:translate(-50%,-50%) scale(.05);opacity:0}40%{opacity:.85}100%{transform:translate(-50%,-50%) scale(1);opacity:0}}
@keyframes fxFade{to{opacity:0}}
@media(prefers-reduced-motion:reduce){.intro{display:none}}
.stat .vp{font-size:11px;font-weight:700;color:var(--muted);letter-spacing:0}
.sitefoot{display:flex;flex-direction:column;align-items:center;gap:10px;text-align:center;font-size:12px;color:var(--muted);font-weight:600;padding:22px 14px 10px;margin-top:10px;border-top:1px solid var(--line2)}
.sitefoot b{font-weight:800;color:var(--ink2)}
.meprof{align-items:center;justify-content:center;width:36px;height:36px;border-radius:11px;border:1px solid rgba(255,255,255,.34);background:rgba(255,255,255,.18);color:#fff;cursor:pointer;padding:0;flex:0 0 auto;transition:.2s var(--ease)}
.meprof:hover{background:rgba(255,255,255,.3);transform:translateY(-1px)}
.meprof svg{width:19px;height:19px}
.mxh-top{position:absolute;top:14px;left:22px;right:22px;display:flex;align-items:center;justify-content:space-between;gap:10px}
.mxh-meta{font-size:12px;font-weight:700;color:var(--muted)}
.mxh-eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:11px;font-weight:900;letter-spacing:1.6px;text-transform:uppercase;color:var(--blue)}
.mxh-eyebrow .mxh-dot{width:8px;height:8px;border-radius:50%;background:var(--blue);animation:bpulse 1.9s infinite}
@keyframes bpulse{0%{box-shadow:0 0 0 0 rgba(37,99,255,.5)}70%{box-shadow:0 0 0 7px rgba(37,99,255,0)}100%{box-shadow:0 0 0 0 rgba(37,99,255,0)}}
.mxh-gwrap{text-align:center;margin-top:8px}
.mxh-guess{display:inline-flex;align-items:center;gap:10px;font-size:14px;font-weight:800;color:var(--blue);background:color-mix(in srgb,var(--blue) 10%,transparent);border:1px solid color-mix(in srgb,var(--blue) 22%,transparent);border-radius:999px;padding:9px 20px}
.mxh-guess b{font-weight:900;font-size:22px}
.mxh-cd{margin:0 0 4px;text-align:center}
.cdtop{font-size:10px;font-weight:800;letter-spacing:1.4px;text-transform:uppercase;color:var(--muted);margin-bottom:4px}
.cdrow{display:inline-flex;align-items:flex-start;gap:6px;color:var(--blue);font-variant-numeric:tabular-nums}
.cdu{display:flex;flex-direction:column;align-items:center}
.cdn{font-family:'Outfit',system-ui,sans-serif;font-size:32px;font-weight:900;line-height:1}
.cdt{font-size:9px;font-weight:800;letter-spacing:.8px;color:var(--muted);margin-top:3px}
.cdsep{font-family:'Outfit',system-ui,sans-serif;font-size:27px;font-weight:900;color:color-mix(in srgb,var(--blue) 35%,transparent);line-height:1.05}
.cdlive{font-size:13px;font-weight:800;color:var(--grass-deep)}
.mxh-eyebrow.live{color:var(--down)}
.mxh-eyebrow.live .mxh-dot{background:var(--down);animation:lpulse 1.2s infinite}
@keyframes lpulse{0%{box-shadow:0 0 0 0 rgba(255,77,99,.55)}70%{box-shadow:0 0 0 7px rgba(255,77,99,0)}100%{box-shadow:0 0 0 0 rgba(255,77,99,0)}}
.mxh-live{display:inline-flex;align-items:center;gap:8px;font-size:14px;font-weight:800;color:var(--down)}
.mxh-livedot{width:9px;height:9px;border-radius:50%;background:var(--down);animation:lpulse 1.2s infinite}
.pbadge{display:inline-flex;align-items:center;gap:5px;font-size:9px;font-weight:900;background:var(--down);color:#fff;border-radius:5px;padding:1px 6px;letter-spacing:.5px}
.pbadge i{width:6px;height:6px;border-radius:50%;background:#fff;animation:lpulse 1.2s infinite}
.fhead .fmeta{padding-top:0;white-space:nowrap}
.hdr h1,.bar h1{font-family:'Schoolbell',system-ui,cursive}
body::before{-webkit-mask-image:linear-gradient(to bottom,#000 55%,transparent);mask-image:linear-gradient(to bottom,#000 55%,transparent)}
.footimg{width:76px;height:76px;border-radius:50%;object-fit:cover;box-shadow:0 8px 20px -10px rgba(15,35,90,.5)}
.foottxt{display:flex;flex-direction:column;gap:2px}
</style></head>
<body>
<div class="intro" id="introFx"><div class="ibg"><div class="decowrap"><span class="cross"></span><span class="deco ring1"></span><span class="deco ring2"></span></div></div><div class="wave"></div><div class="ball"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><defs><clipPath id="ibc"><circle cx="50" cy="50" r="46"/></clipPath></defs><circle cx="50" cy="50" r="46" fill="#fff" stroke="#0b1530" stroke-width="2.5"/><g clip-path="url(#ibc)" fill="#0b1530"><polygon points="69.4,23.3 63.9,6.5 78.2,-3.8 92.5,6.5 87.0,23.3"/><polygon points="81.4,60.2 95.7,49.8 109.9,60.2 104.5,77.0 86.8,77.0"/><polygon points="50.0,83.0 64.3,93.4 58.8,110.1 41.2,110.1 35.7,93.4"/><polygon points="18.6,60.2 13.2,77.0 -4.5,77.0 -9.9,60.2 4.3,49.8"/><polygon points="30.6,23.3 13.0,23.3 7.5,6.5 21.8,-3.8 36.1,6.5"/><polygon points="50.0,32.0 67.1,44.4 60.6,64.6 39.4,64.6 32.9,44.4"/></g><g clip-path="url(#ibc)" stroke="#0b1530" stroke-width="2.4" fill="none" stroke-linecap="round"><path d="M50.0 32.0 L50.0 4.0"/><path d="M67.1 44.4 L93.7 35.8"/><path d="M60.6 64.6 L77.0 87.2"/><path d="M39.4 64.6 L23.0 87.2"/><path d="M32.9 44.4 L6.3 35.8"/></g><circle cx="50" cy="50" r="46" fill="none" stroke="#0b1530" stroke-width="2.5"/></svg></div><div class="load">Laddar resultat…</div></div>
<script>(function(){try{var t=localStorage.getItem("loftahammar_theme");if(!t)t="light";document.documentElement.setAttribute("data-theme",t);}catch(e){}})();(function(){try{var fx=document.getElementById("introFx");if(!fx)return;var r=window.matchMedia&&window.matchMedia("(prefers-reduced-motion:reduce)").matches;if(r){if(fx.parentNode)fx.parentNode.removeChild(fx);return;}}catch(e){var f=document.getElementById("introFx");if(f&&f.parentNode)f.parentNode.removeChild(f);}})();</script>
<div class="wrap">
  <header class="hdr">
    <div class="hdr-deco"></div>
    <div class="hdr-main">
      <div class="ballwrap">
        <span class="ball"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><defs><clipPath id="bc"><circle cx="50" cy="50" r="46"/></clipPath></defs><circle cx="50" cy="50" r="46" fill="#fff" stroke="#0b1530" stroke-width="2.5"/><g clip-path="url(#bc)" fill="#0b1530"><polygon points="69.4,23.3 63.9,6.5 78.2,-3.8 92.5,6.5 87.0,23.3"/><polygon points="81.4,60.2 95.7,49.8 109.9,60.2 104.5,77.0 86.8,77.0"/><polygon points="50.0,83.0 64.3,93.4 58.8,110.1 41.2,110.1 35.7,93.4"/><polygon points="18.6,60.2 13.2,77.0 -4.5,77.0 -9.9,60.2 4.3,49.8"/><polygon points="30.6,23.3 13.0,23.3 7.5,6.5 21.8,-3.8 36.1,6.5"/><polygon points="50.0,32.0 67.1,44.4 60.6,64.6 39.4,64.6 32.9,44.4"/></g><g clip-path="url(#bc)" stroke="#0b1530" stroke-width="2.4" fill="none" stroke-linecap="round"><path d="M50.0 32.0 L50.0 4.0"/><path d="M67.1 44.4 L93.7 35.8"/><path d="M60.6 64.6 L77.0 87.2"/><path d="M39.4 64.6 L23.0 87.2"/><path d="M32.9 44.4 L6.3 35.8"/></g><circle cx="50" cy="50" r="46" fill="none" stroke="#0b1530" stroke-width="2.5"/></svg></span>
        <span class="ballsh"></span>
      </div>
      <div class="hdr-txt"><h1>Loftahammarstipset</h1><p>VM 2026 · 11 juni – 19 juli</p></div>
      <button class="tog" id="themeBtn" aria-label="Växla mörkt/ljust läge">🌙</button>
    </div>
    <div class="hdr-foot"><span class="dot"></span><span id="updatedAt">—</span><span class="hdr-me"><button class="meprof" id="meProf" type="button" aria-label="Visa min tipslapp" title="Min tipslapp" style="display:none"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg></button><span id="meLabel">Jag är:</span> <div class="msel" id="meDD"><button class="msel-btn" id="meBtn"></button><div class="msel-pop" id="mePop"></div></div></span></div>
  </header>
  <div class="tabs" id="tabs">
    <button class="tab active" data-view="dash"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/></svg></span>Hem</button>
    <button class="tab" data-view="standings"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 4h12v3a6 6 0 0 1-12 0V4z"/><path d="M6 5H3v2a3 3 0 0 0 3 3"/><path d="M18 5h3v2a3 3 0 0 1-3 3"/><path d="M9 18h6M12 14v4"/></svg></span>Poänglista</button>
    <button class="tab" data-view="matches"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="17" rx="2"/><path d="M3 9h18M8 2v4M16 2v4"/></svg></span>Matcher</button>
    <button class="tab" data-view="bracket"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="6" cy="6" r="2"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="9" r="2"/><path d="M6 8v8"/><path d="M18 11c0 5-6 2-6 7"/></svg></span>Slutspel</button>
    <button class="tab" data-view="tables"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg></span>Grupper</button>
    <button class="tab" data-view="h2h"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8" r="3"/><circle cx="17.5" cy="9" r="2.2"/><path d="M3.5 20a5.5 5.5 0 0 1 11 0"/><path d="M15 20a5 5 0 0 1 6-4"/></svg></span>Head-to-head</button>
    <button class="tab" data-view="regler"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2h9l4 4v16H6z"/><path d="M14 2v5h5"/><path d="M9 13h7M9 17h6"/></svg></span>Regler</button>
  </div>

  <section class="view active" id="dash">
    <div id="meHem"></div>
    <div class="duo">
      <div class="card duocard"><div class="ttl"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 4h12v3a6 6 0 0 1-12 0V4z"/><path d="M6 5H3v2a3 3 0 0 0 3 3"/><path d="M18 5h3v2a3 3 0 0 1-3 3"/><path d="M9 18h6M12 14v4"/></svg></span>Topp 3 just nu <span class="more" id="toStandings">Visa poänglista</span></div><div class="podium" id="podium"></div><div class="podnote" id="podnote"></div></div>
      <div class="card duocard"><div class="ttl"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="17" rx="2"/><path d="M3 9h18M8 2v4M16 2v4"/></svg></span>Nästkommande matcher</div><div id="upcoming"></div></div>
    </div>
    <div class="mgroup">
      <div class="card fcard">
        <div class="fhead"><span class="ph" id="fPhase">Match</span><span class="fmeta" id="fMeta"></span><div class="nav"><button id="prevM" aria-label="Föregående match">‹</button><button id="nextM" aria-label="Nästa match">›</button></div></div>
        <div class="mxh-cd" id="fCd"></div>
        <div class="fbody">
          <div class="team"><div id="hFlag"></div><span class="tn" id="hName"></span></div>
          <div class="sb"><div class="mstamp" id="fStamp">FÄRDIGSPELAD</div><div class="sc" id="fScore"></div><div class="ft" id="fStatus"></div></div>
          <div class="team"><div id="aFlag"></div><span class="tn" id="aName"></span></div>
        </div>
        <div class="mxh-gwrap" id="fGuess"></div>
      </div>
      <div class="mlink"><i class="l"></i><i class="r"></i></div>
      <div class="card">
        <div class="ttl"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/></svg></span>Allas tips för matchen <span class="more" id="pickSum"></span></div>
        <div class="picks" id="picks"></div>
      </div>
    </div>
  </section>

  <section class="view" id="standings"><div class="card"><div class="ttl"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 4h12v3a6 6 0 0 1-12 0V4z"/><path d="M6 5H3v2a3 3 0 0 0 3 3"/><path d="M18 5h3v2a3 3 0 0 1-3 3"/><path d="M9 18h6M12 14v4"/></svg></span>Poänglista <span class="more" id="partCount"></span><button class="infobtn" id="poengInfo">ⓘ Så funkar poängen</button></div><div class="rk-ctrl"><input id="rkSearch" type="search" placeholder="Sök deltagare…" aria-label="Sök deltagare"><div class="rk-sort" id="rkSort"><button data-k="total" class="active">Total</button><button data-k="pig">Gruppspel</button><button data-k="pis">Slutspel</button></div></div><div id="rankList"></div>
    <div class="podnote" style="margin-top:10px">Poäng samlas i gruppspelet och i slutspelet · klicka på ett namn för hela tipslappen</div></div>
    <div class="card"><div class="ttl"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7l4 4 5-7 5 7 4-4v11H3z"/></svg></span>Tippade mästare &amp; skyttekung</div><div class="cv" id="champviz"></div></div>
  </section>
  <section class="view" id="matches"><div class="ttl"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="17" rx="2"/><path d="M3 9h18M8 2v4M16 2v4"/></svg></span>Matcher</div>
    <div id="mxHero"></div>
    <div class="mxseg" id="mxSeg"><button data-seg="played">Spelade matcher</button><button class="active" data-seg="upcoming">Kommande matcher</button></div>
    <div id="mxSummary" class="mxsum"></div>
    <div class="mxbar">
      <div class="mfilter mxstatus" id="mfilter2"><button class="active" data-r="all">Alla</button><button class="needsme" data-r="exact">Exakt rätt</button><button class="needsme" data-r="right">Rätt utfall</button><button class="needsme" data-r="wrong">Fel utfall</button></div>
      <div class="mxbar-right"><select id="mTypeSel" class="mxtype" aria-label="Visa matchtyp"><option value="all">Alla matcher</option><option value="group">Bara gruppspel</option><option value="ko">Bara slutspel</option></select></div>
    </div>
    <div id="matchList"></div></section>
  <section class="view" id="bracket"><div class="card"><div class="ttl"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="6" cy="6" r="2"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="9" r="2"/><path d="M6 8v8"/><path d="M18 11c0 5-6 2-6 7"/></svg></span>Slutspelsträd</div><div id="koScore"></div>
<div id="koNote"></div>
<div class="koround" id="koRoundSel"></div>
<div class="kogrid" id="bracketWrap"></div></div></section>
  <section class="view" id="tables"><div class="card"><div class="ttl"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg></span>Grupptabeller (facit)</div><div class="grid2" id="tablesWrap"></div></div></section>
  <section class="view" id="h2h"><div class="card"><div class="ttl"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8" r="3"/><circle cx="17.5" cy="9" r="2.2"/><path d="M3.5 20a5.5 5.5 0 0 1 11 0"/><path d="M15 20a5 5 0 0 1 6-4"/></svg></span>Head-to-head</div><div class="h2h-pick"><select id="h2hA"></select><select id="h2hB"></select></div><div id="h2hResult"></div></div></section><section class="view" id="regler"><div class="card reg">
  <div class="ttl"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2h9l4 4v16H6z"/><path d="M14 2v5h5"/><path d="M9 13h7M9 17h6"/></svg></span>Regler & priser</div>
  <div class="big"><div class="pcard"><div class="v">100 kr</div><div class="l">Insats</div></div><div class="pcard"><div class="v">494</div><div class="l">Maxpoäng</div></div><div class="pcard"><div class="v">16</div><div class="l">Deltagare</div></div><div class="pcard"><div class="v">1600 kr</div><div class="l">Prispott</div></div></div>
  <h3>💰 Vinstfördelning</h3>
  <p>Prispotten är <b>1600 kr</b> (100 kr × 16 deltagare).</p><table><tbody><tr><td>🥇 1:an · 50 %</td><td>800 kr</td></tr><tr><td>🥈 2:an · 25 %</td><td>400 kr</td></tr><tr><td>🥉 3:an · 10 %</td><td>160 kr</td></tr><tr><td>Gruppspelsledare (siffertipset) · 10 %</td><td>160 kr</td></tr><tr><td>Skyttekung · 5 %</td><td>80 kr</td></tr></tbody></table>
  <p style="color:var(--muted);font-size:12px;margin-top:8px">Skyttekung vid lika: den som är närmast antal gjorda mål vinner.</p>
  <h3>🎯 Poäng – gruppspel (max 288)</h3>
  <table><tbody><tr><td>Rätt tecken (1X2)</td><td>1 p</td></tr><tr><td>Rätt matchresultat (exakt)</td><td>+3 p</td></tr></tbody></table>
  <h3>🏆 Poäng – slutspel (max 206)</h3>
  <table><tbody><tr><td>Rätt lag till 16-delsfinal</td><td>2 p/lag</td></tr><tr><td>Rätt lag till åttondelsfinal</td><td>3 p/lag</td></tr><tr><td>Rätt kvartsfinallag</td><td>5 p/lag</td></tr><tr><td>Rätt semifinallag</td><td>7 p/lag</td></tr><tr><td>Rätt finallag</td><td>8 p/lag</td></tr><tr><td>Rätt världsmästare</td><td>10 p</td></tr></tbody></table>
  <h3>⚖️ Vid lika poäng</h3>
  <p>Flest poäng i gruppspelet (siffertipset) avgör. Är det fortfarande lika delas vinsten.</p>
  <p style="color:var(--muted);font-size:12px">Resultaten hämtas automatiskt och bör dubbelkollas vid tvist. Arrangör: Sven Tholén.</p>
</div></section>
<footer class="sitefoot"><img class="footimg" src="https://img.charma.io/sven-profilbild.png" alt="Sven Tholén" loading="lazy"><div class="foottxt"><span>Loftahammarstipset · VM 2026</span><span>Arrangeras av <b>Sven Tholén</b></span></div></footer>
</div>

<div class="overlay" id="overlay"><div class="modal">
  <div class="mhead"><div class="ava" id="mAva"></div><div><h3 id="mName"></h3><p id="mSub"></p></div><button class="x" id="mClose">✕</button></div>
  <div class="mbody" id="mBody"></div>
</div></div>

<script>
const D=__DATA__;const ISO=__ISO__;
/*RESULTS_START*/const RESULTS=__RESULTS__;/*RESULTS_END*/
const totalUpdated="Senast uppdaterad __UPD__";
function abbr(team){const i=ISO[team];if(!i)return (team||"?").slice(0,3).toUpperCase();if(i.indexOf("-")>0)return i.split("-")[1].toUpperCase();return i.toUpperCase();}
window.flagFB=function(img){const h=+img.dataset.h||16,ab=img.dataset.ab,rnd=img.dataset.rnd==="1";const s=document.createElement("span");if(rnd){s.className="flagfb-round";s.style.width=h+"px";s.style.height=h+"px";s.style.fontSize=Math.round(h*.32)+"px";}else{s.className="flagfb";s.style.height=h+"px";s.style.width=Math.round(h*1.4)+"px";s.style.fontSize=Math.round(h*.5)+"px";}s.textContent=ab;img.replaceWith(s);};
function flag(team,h){h=h||16;const i=ISO[team];const ab=abbr(team);if(!i)return `<span class="flagfb" style="height:${h}px;width:${Math.round(h*1.4)}px;font-size:${Math.round(h*.5)}px">${ab}</span>`;return `<img class="flag-img" loading="lazy" decoding="async" src="https://flagcdn.com/h40/${i}.png" srcset="https://flagcdn.com/h80/${i}.png 2x" alt="${team}" width="${Math.round(h*1.36)}" height="${h}" style="height:${h}px;width:${Math.round(h*1.36)}px" data-ab="${ab}" data-h="${h}" onerror="flagFB(this)">`;}
function flagRound(team,sz){const i=ISO[team];const ab=abbr(team);if(!i)return `<span class="flagfb-round" style="width:${sz}px;height:${sz}px;font-size:${Math.round(sz*.32)}px">${ab}</span>`;return `<img class="flag-round" loading="lazy" decoding="async" src="https://flagcdn.com/h240/${i}.png" alt="${team}" style="width:${sz}px;height:${sz}px" data-ab="${ab}" data-h="${sz}" data-rnd="1" onerror="flagFB(this)">`;}
const COLORS=["#2563ff","#15c26b","#f5a700","#ff4d63","#7b5bff","#0f9a55","#d1700a","#0aa3d1"];
const initials=n=>n.split(/[ &]+/).filter(Boolean).map(p=>p[0]).slice(0,2).join("").toUpperCase();
const first=n=>n.split(/[ &]+/)[0];
function colorFor(n){let s=0;for(const c of n)s+=c.charCodeAt(0);return COLORS[s%COLORS.length];}
D.participants.forEach(p=>{p._g={};p.groups.forEach(g=>{p._g[g[0]]=[g[2],g[3],g[5]];});});
const inter=(a,b)=>a.filter(x=>b.includes(x)).length;
function scoreOf(p){let pig=0,signs=0,exact=0;p.groups.forEach(g=>{const r=RESULTS.group[g[0]];if(!r)return;const as=r[0]>r[1]?'1':r[0]<r[1]?'2':'X';if(g[5]===as){pig+=1;signs++;}if(g[2]===r[0]&&g[3]===r[1]){pig+=3;exact++;}});let pis=inter(p.r32,RESULTS.r32)*2+inter(p.r16,RESULTS.r16)*3+inter(p.qf,RESULTS.qf)*5+inter(p.sf,RESULTS.sf)*7+inter(p.final,RESULTS.final)*8+((RESULTS.champion&&p.champion===RESULTS.champion)?10:0);return{pig,pis,total:pig+pis,signs,exact};}
function buildPlist(){const l=D.participants.map(p=>{const s=scoreOf(p);return{name:p.name,ref:p,pig:s.pig,pis:s.pis,total:s.total,signs:s.signs,exact:s.exact};});l.sort((a,b)=>b.total-a.total||b.pig-a.pig||b.signs-a.signs||a.name.localeCompare(b.name));l.forEach((p,i)=>{p.rank=i+1;const pv=(RESULTS.snapshot||{})[p.name];p.delta=pv?pv-p.rank:0;});return l;}
let PLIST=buildPlist();
const MATCHES=D.fixtures.map(f=>({t:"group",ph:"Grupp "+f.grp,nr:f.nr,home:f.home,away:f.away,time:f.date,score:RESULTS.group[f.nr]||null})).concat(D.knockout.map(k=>({t:"ko",ph:k.round,nr:k.nr,homeSlot:k.homeSlot,awaySlot:k.awaySlot,time:k.date,score:null})));
MATCHES.sort((a,b)=>{const A=parseKick(a.time),B=parseKick(b.time);return (A?+A:8.64e15)-(B?+B:8.64e15);});
let cur=MATCHES.findIndex(m=>m.t==="group"&&!m.score);if(cur<0)cur=0;
let mFilter="all";
let rankSort="total",rankQ="";
let resFilter="all";let mSeg="upcoming";let LIVE={};
let ME=null;try{ME=localStorage.getItem("loftahammar_me")||null;}catch(e){}
function fillMe(){const btn=document.getElementById("meBtn"),pop=document.getElementById("mePop"),dd=document.getElementById("meDD");if(!btn)return;
if(pop.parentNode!==document.body)document.body.appendChild(pop);
function label(){btn.innerHTML=ME?`<span class="msa" style="background:${colorFor(ME)}">${initials(ME)}</span><span class="msl">${ME}</span><span class="msc">\u25be</span>`:`<span class="msl muted">\u2013 v\u00e4lj ditt namn \u2013</span><span class="msc">\u25be</span>`;}
function close(){dd.classList.remove("open");pop.classList.remove("open");}
function pick(v){ME=v||null;try{ME?localStorage.setItem("loftahammar_me",ME):localStorage.removeItem("loftahammar_me");}catch(e){}close();label();build();renderMeHem();renderPodium();renderRank();renderFeatured();renderMatchList();renderBracket();}
function build(){pop.innerHTML=`<button class="mopt ${!ME?"sel":""}" data-v="">\u2013 ingen \u2013</button>`+D.participants.map(p=>`<button class="mopt ${p.name===ME?"sel":""}" data-v="${p.name}"><span class="msa" style="background:${colorFor(p.name)}">${initials(p.name)}</span>${p.name}${p.name===ME?'<span class="mck">\u2713</span>':""}</button>`).join("");pop.querySelectorAll(".mopt").forEach(o=>o.onclick=()=>pick(o.dataset.v));dd.classList.toggle("needpick",!ME);}
function openPop(){const r=btn.getBoundingClientRect();pop.style.top=(r.bottom+8)+"px";pop.style.right=Math.max(8,window.innerWidth-r.right)+"px";dd.classList.add("open");pop.classList.add("open");}
btn.onclick=e=>{e.stopPropagation();pop.classList.contains("open")?close():openPop();};
document.addEventListener("click",e=>{if(!dd.contains(e.target)&&!pop.contains(e.target))close();});
window.addEventListener("scroll",close);window.addEventListener("resize",close);
label();build();}
document.getElementById("updatedAt").innerHTML=totalUpdated;
document.getElementById("partCount").textContent=D.participants.length+" deltagare";
const anyPts=PLIST.some(p=>p.total>0);

function trendHtml(p){if(!p.delta)return"";var u=p.delta>0,n=Math.abs(p.delta);var c=u?'<svg viewBox="0 0 10 10" aria-hidden="true"><path d="M1.7 6.4 5 3.1l3.3 3.3" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>':'<svg viewBox="0 0 10 10" aria-hidden="true"><path d="M1.7 3.6 5 6.9l3.3-3.3" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>';return '<span class="tr '+(u?"up":"down")+'" title="'+(u?"Upp ":"Ner ")+n+' placeringar sedan senaste matchen">'+c+n+'</span>';}

function renderPodium(){
  const top=PLIST.slice(0,3);const order=[top[1],top[0],top[2]];const cls=["p2","p1","p3"];const rank=[2,1,3];
  document.getElementById("podium").innerHTML=order.map((p,i)=>p?`<div class="pod ${cls[i]} ${p.name===ME?"me":""}" data-name="${p.name}"><span class="ava" style="background:${colorFor(p.name)}">${initials(p.name)}</span><span class="nm">${p.name}</span>${p.name===ME?'<span class="dut">DU</span>':""}<span class="pts">${p.total} poäng</span><div class="ped"><span class="ped-rank">${rank[i]}:a</span></div></div>`:'<div></div>').join("");
  document.getElementById("podium").querySelectorAll(".pod").forEach(el=>el.onclick=()=>openPerson(el.dataset.name));
  var _pn;
  if(!anyPts){_pn="Turneringen har precis börjat – poängen tickar in efter varje match";}
  else{
    var _grp=[];PLIST.forEach(function(p,i){if(i>0&&p.total===PLIST[i-1].total)_grp[_grp.length-1].names.push(p.name);else _grp.push({total:p.total,place:i+1,names:[p.name]});});
    var _tie=null;for(var _k=0;_k<_grp.length;_k++){if(_grp[_k].names.length>=2&&_grp[_k].place<=3&&_grp[_k].total>0){_tie=_grp[_k];break;}}
    if(_tie){var _ns=_tie.names;if(_ns.length>3){_pn=_ns.length+" spelare delar "+_tie.place+":a platsen";}else{var _who=_ns.length===2?_ns[0]+" och "+_ns[1]:_ns.slice(0,-1).join(", ")+" och "+_ns[_ns.length-1];_pn=_who+" ligger på delad "+_tie.place+":a plats";}}
    else{_pn=PLIST[0].name+" leder med "+(PLIST[0].total-PLIST[1].total)+" poäng före tvåan";}
  }
  document.getElementById("podnote").textContent=_pn;
}
function parseKick(t){const m=/(\d{1,2})\/(\d{1,2})\s+(\d{1,2})[.:](\d{2})/.exec(t||"");if(!m)return null;return new Date(2026,+m[2]-1,+m[1],+m[3],+m[4]);}
function setupCountdown(m){var el=document.getElementById("fCd");if(!el)return;if(window._cd)clearInterval(window._cd);var nx=MATCHES.findIndex(function(x){return !x.score;}),_nm=(nx>=0&&MATCHES[nx]===m);if(m.t==="group"&&!m.score&&_nm&&isLive(m)){el.style.display="";el.innerHTML='<div class="mxh-live"><span class="mxh-livedot"></span>Inväntar resultat</div>';return;}var k=(m.t==="group"&&!m.score&&_nm)?parseKick(m.time):null;if(!k){el.innerHTML="";el.style.display="none";return;}el.style.display="";var _seg=function(n,l){return '<span class="cdu"><span class="cdn">'+("0"+n).slice(-2)+'</span><span class="cdt">'+l+'</span></span>';};function tick(){var d=k-Date.now();if(d<=0){el.innerHTML='<div class="cdlive">🟢 Avspark passerad – inväntar resultat</div>';if(window._cd)clearInterval(window._cd);return;}var dd=Math.floor(d/864e5),hh=Math.floor(d%864e5/36e5),mm=Math.floor(d%36e5/6e4),ss=Math.floor(d%6e4/1e3);el.innerHTML='<div class="cdtop">Avspark om</div><div class="cdrow">'+(dd>0?_seg(dd,"DGR")+'<span class="cdsep">:</span>':"")+_seg(hh,"TIM")+'<span class="cdsep">:</span>'+_seg(mm,"MIN")+'<span class="cdsep">:</span>'+_seg(ss,"SEK")+'</div>';}tick();window._cd=setInterval(tick,1000);}
function animCount(node){const t=+node.dataset.c;if(!t){node.textContent=0;return;}const d=650,t0=performance.now();(function st(n){const p=Math.min((n-t0)/d,1);node.textContent=Math.round(t*(1-Math.pow(1-p,3)));if(p<1)requestAnimationFrame(st);})(t0);}
function renderUpcoming(){const el=document.getElementById("upcoming");if(!el)return;const up=[];for(let i=0;i<MATCHES.length&&up.length<7;i++){if(!MATCHES[i].score)up.push(i);}
  if(!up.length){el.innerHTML='<div class="hint" style="padding:6px">Inga kommande matcher.</div>';return;}
  el.innerHTML=up.map(i=>{const m=MATCHES[i];const pr=(m.time||"").split(" ");const teams=m.t==="group"?`${flag(m.home,15)} <span class="un">${m.home}</span> <span class="uvs">–</span> <span class="un">${m.away}</span> ${flag(m.away,15)}`:`<span class="uslot">${m.homeSlot} – ${m.awaySlot}</span>`;return `<div class="uprow" data-i="${i}"><div class="utime">${pr[0]||""}<span>${pr[1]||""}</span></div><div class="ubody"><div class="uteams">${teams}</div><div class="utag">${m.ph}</div></div></div>`;}).join("");
  el.querySelectorAll(".uprow").forEach(r=>r.onclick=()=>openMatch(+r.dataset.i));}
function normSkytt(x){if(!x)return null;let k=x.trim().toLowerCase().replace(/[áàâä]/g,"a").replace(/[éè]/g,"e").replace(/[óò]/g,"o").replace(/[íì]/g,"i");
  if(k.includes("mbappe"))return "Kylian Mbappé";if(k.includes("yamal"))return "Lamine Yamal";if(k.includes("haaland"))return "Erling Haaland";if(k.includes("kane"))return "Harry Kane";if(k.includes("alvarez"))return "Julián Álvarez";if(k.includes("olise"))return "Michael Olise";
  return x.trim();}
function openList(title,sub,names){const av=document.getElementById("mAva");av.style.display="none";document.getElementById("mName").textContent=title;document.getElementById("mSub").textContent=sub;document.getElementById("mBody").innerHTML=`<div class="kchips" style="gap:8px">${names.map(n=>`<span class="pp2" data-name="${n}"><span class="ava" style="background:${colorFor(n)}">${initials(n)}</span>${n}</span>`).join("")}</div>`;document.getElementById("overlay").classList.add("open");}
function openScoring(){const av=document.getElementById("mAva");av.style.display="none";document.getElementById("mName").textContent="Så funkar poängen";document.getElementById("mSub").textContent="Poängsystem · max 494 poäng";document.getElementById("mBody").innerHTML=`<div class="reg"><h3>🎯 Gruppspel (max 288)</h3><table><tbody><tr><td>Rätt tecken (1X2)</td><td>1 p</td></tr><tr><td>Rätt matchresultat (exakt)</td><td>+3 p</td></tr></tbody></table><h3 style="margin-top:14px">🏆 Slutspel (max 206)</h3><table><tbody><tr><td>Rätt lag till 16-delsfinal</td><td>2 p/lag</td></tr><tr><td>Rätt lag till åttondelsfinal</td><td>3 p/lag</td></tr><tr><td>Rätt kvartsfinallag</td><td>5 p/lag</td></tr><tr><td>Rätt semifinallag</td><td>7 p/lag</td></tr><tr><td>Rätt finallag</td><td>8 p/lag</td></tr><tr><td>Rätt världsmästare</td><td>10 p</td></tr></tbody></table><p style="margin-top:12px">Vid lika totalpoäng avgör flest poäng i gruppspelet (siffertipset).</p></div>`;document.getElementById("overlay").classList.add("open");}
function renderChampViz(){const el=document.getElementById("champviz");if(!el)return;
  const champMap={},skyMap={};
  D.participants.forEach(p=>{if(p.champion){(champMap[p.champion]=champMap[p.champion]||[]).push(p.name);}const sk=normSkytt(p.skyttekung);if(sk){(skyMap[sk]=skyMap[sk]||[]).push(p.name);}});
  const chips=names=>names.map(n=>`<span class="pp2" data-name="${n}"><span class="ava" style="background:${colorFor(n)}">${initials(n)}</span>${first(n)}</span>`).join("");
  const section=(map,withFlag)=>{const arr=Object.entries(map).sort((a,b)=>b[1].length-a[1].length);return arr.map(([k,names])=>`<div class="scoregrp"><span class="rchip">${withFlag?flag(k,15):""}<span class="cvk">${k}</span></span><div class="ppl">${chips(names)}</div><span class="cntr">${names.length} st</span></div>`).join("");};
  el.innerHTML=`<div class="tvsub">🏆 Världsmästare</div>${section(champMap,true)}<div class="tvsub" style="margin-top:15px">👟 Skyttekung</div>${section(skyMap,false)}`;
}
function meBannerHtml(me){if(!me)return "";return `<div class="mebanner" data-name="${me.name}" style="cursor:pointer" title="Visa min tipslapp"><span class="ava">${initials(me.name)}</span><div class="bi"><div class="bl">⭐ Din ställning</div><div class="bn">${me.name} · plats #${me.rank} av ${PLIST.length}</div><div class="mebar2"><div class="mefill" style="width:${(me.total/494*100).toFixed(1)}%"></div></div></div><div class="bp"><div class="bpv">${me.total}</div><div class="bpu">poäng</div><div class="bps">av 494</div></div></div>`;}
function updMeProf(){var _mp=document.getElementById("meProf"),_ml=document.getElementById("meLabel");if(_mp){_mp.style.display=ME?"inline-flex":"none";_mp.onclick=function(){if(ME)openPerson(ME);};}if(_ml)_ml.style.display=ME?"none":"";}
function renderMeHem(){updMeProf();const el=document.getElementById("meHem");if(el)el.innerHTML=ME?meBannerHtml(PLIST.find(p=>p.name===ME)):'<div class="mehint">👋 Välj ditt namn där uppe för en personlig vy – din placering, dina gissningar och din poäng.</div>';}
function renderFeatured(){
  const m=MATCHES[cur];document.getElementById("fPhase").textContent=m.ph;
  const sc=document.getElementById("fScore"),st=document.getElementById("fStatus");
  if(m.t==="group"){
    document.getElementById("hFlag").innerHTML=flagRound(m.home,72);document.getElementById("aFlag").innerHTML=flagRound(m.away,72);
    document.getElementById("hName").textContent=m.home;document.getElementById("aName").textContent=m.away;
    if(m.score){sc.textContent=`${m.score[0]} – ${m.score[1]}`;sc.className="sc pop";st.textContent="Slutresultat";}
    else{sc.textContent="VS";sc.className="sc pend pop";st.textContent="Kommande";}
  }else{
    document.getElementById("hFlag").innerHTML=flagRound("?",72);document.getElementById("aFlag").innerHTML=flagRound("?",72);
    document.getElementById("hName").textContent=m.homeSlot||"TBD";document.getElementById("aName").textContent=m.awaySlot||"TBD";
    sc.textContent="VS";sc.className="sc pend pop";st.textContent="Slutspel";
  }
  void sc.offsetWidth;const _st=document.getElementById("fStamp");if(_st)_st.style.display=m.score?"inline-flex":"none";
  document.getElementById("fMeta").innerHTML=`📅 ${fmtMatchDate(m.time)||"–"}`;
  document.getElementById("prevM").disabled=cur===0;document.getElementById("nextM").disabled=cur===MATCHES.length-1;
  var _fg=document.getElementById("fGuess");if(_fg){var meF=ME?D.participants.find(p=>p.name===ME):null;var pkF=(m.t==="group"&&!m.score&&meF&&meF._g[m.nr])?meF._g[m.nr]:null;_fg.innerHTML=pkF?'<span class="mxh-guess">Din gissning <b>'+pkF[0]+'–'+pkF[1]+'</b></span>':"";}
  renderPicks();setupCountdown(m);
}
function gpoints(pk,r){if(!r)return null;const as=r[0]>r[1]?'1':r[0]<r[1]?'2':'X';let p=0;if(pk[2]===as)p+=1;if(pk[0]===r[0]&&pk[1]===r[1])p+=3;return p;}
function picksGrouped(m){
  if(m.t!=="group")return {sum:"",html:'<div style="color:var(--muted);font-size:12.5px;padding:6px">Slutspelslag tippas i bracket-steget – se varje persons tipslapp via Poänglistan.</div>'};
  const groups={};
  PLIST.forEach(pp=>{const pk=pp.ref._g[m.nr];if(!pk)return;const k=pk[0]+"–"+pk[1];(groups[k]=groups[k]||[]).push(pp.name);});
  const chips=names=>names.map(n=>`<span class="pp2 ${n===ME?"me":""}" data-name="${n}"><span class="ava" style="background:${colorFor(n)}">${initials(n)}</span>${first(n)}</span>`).join("");
  const wflag=ss=>{if(m.t!=="group")return "";const p=ss.split("–").map(Number);if(p[0]>p[1])return `<span class="wf">${flag(m.home,15)}</span>`;if(p[0]<p[1])return `<span class="wf">${flag(m.away,15)}</span>`;return `<span class="wf draw">X</span>`;};
  const grp=(s,names)=>`<div class="scoregrp"><span class="rchip">${wflag(s)}<span class="rsc">${s}</span></span><div class="ppl">${chips(names)}</div><span class="cntr">${names.length} st</span></div>`;
  const entries=Object.entries(groups);
  if(!m.score){entries.sort((a,b)=>b[1].length-a[1].length);return {sum:`${PLIST.length} tips · ${entries.length} olika resultat`,html:`<div class="catblock">`+entries.map(([s,n])=>grp(s,n)).join("")+`</div>`};}
  const res=m.score,sign=res[0]>res[1]?"1":res[0]<res[1]?"2":"X";const cats={exact:[],right:[],wrong:[]};
  entries.forEach(([s,names])=>{const p=s.split("–").map(Number);const sg=p[0]>p[1]?"1":p[0]<p[1]?"2":"X";if(p[0]===res[0]&&p[1]===res[1])cats.exact.push([s,names]);else if(sg===sign)cats.right.push([s,names]);else cats.wrong.push([s,names]);});
  const block=(title,cls,arr,pts)=>{if(!arr.length)return "";const tot=arr.reduce((a,x)=>a+x[1].length,0);arr.sort((a,b)=>b[1].length-a[1].length);return `<div class="catblock ${cls}"><div class="cathead">${title} · ${tot} st <span class="cp">${pts}</span></div>${arr.map(([s,n])=>grp(s,n)).join("")}</div>`;};
  return {sum:`facit ${res[0]}–${res[1]} · ${cats.exact.reduce((a,x)=>a+x[1].length,0)} exakt rätt`,html:block("✅ Exakt rätt","cat-exact",cats.exact,"+4 p")+block("🟡 Rätt utfall","cat-right",cats.right,"+1 p")+block("⚪ Fel","cat-wrong",cats.wrong,"0 p")};
}
function renderPicks(){const m=MATCHES[cur];const r=picksGrouped(m);document.getElementById("pickSum").textContent=r.sum;document.getElementById("picks").innerHTML=r.html;}
function openMatch(i){const m=MATCHES[i];const r=picksGrouped(m);const av=document.getElementById("mAva");av.style.display="none";
  document.getElementById("mName").textContent=m.t==="group"?(m.score?`${m.home} ${m.score[0]}–${m.score[1]} ${m.away}`:`${m.home} – ${m.away}`):`${m.homeSlot} – ${m.awaySlot}`;
  document.getElementById("mSub").textContent=`${m.ph} · ${m.time||""}`;
  document.getElementById("mBody").innerHTML=`<div class="ttl" style="margin:0 0 10px">🎯 Allas tips${r.sum?` <span class="more">${r.sum}</span>`:""}</div>${r.html||'<div class="hint">Inga tips än.</div>'}`;
  document.getElementById("overlay").classList.add("open");
}
document.getElementById("prevM").onclick=()=>{if(cur>0){cur--;renderFeatured();}};
document.getElementById("nextM").onclick=()=>{if(cur<MATCHES.length-1){cur++;renderFeatured();}};

function renderRank(){
  const el=document.getElementById("rankList");
  let rows=PLIST.filter(p=>p.name.toLowerCase().includes(rankQ));
  rows.sort((a,b)=>rankSort==="name"?a.name.localeCompare(b.name):(b[rankSort]-a[rankSort])||(b.total-a.total)||a.name.localeCompare(b.name));
  let banner=ME?meBannerHtml(PLIST.find(p=>p.name===ME)):"";
  const _hd=new Date(),_htoday=("0"+_hd.getDate()).slice(-2)+"/"+("0"+(_hd.getMonth()+1)).slice(-2);
  const hotNrs=MATCHES.filter(m=>m.t==="group"&&m.score&&(m.time||"").indexOf(_htoday)===0).map(m=>m.nr);
  const hotPts=p=>{let s=0;p.ref.groups.forEach(g=>{if(hotNrs.indexOf(g[0])<0)return;const pp=gpoints([g[2],g[3],g[5]],RESULTS.group[g[0]]);if(pp)s+=pp;});return s;};
  el.innerHTML=banner+(rows.map((p,i)=>{const hot=hotPts(p)>=5;return `<div class="rk ${p.rank===1&&anyPts?"top":""} ${p.name===ME?"me":""}" data-name="${p.name}" tabindex="0" style="animation:rise .4s var(--ease) ${i*.025}s both"><span class="pos"><span class="rkn">${p.rank===1&&anyPts?"👑":p.rank}</span>${trendHtml(p)}</span><span class="ava" style="background:${colorFor(p.name)}">${initials(p.name)}</span><span class="who"><span class="nm">${p.name}${p.name===ME?' <span class="dut">DU</span>':""}</span><span class="pp"><span class="t-ru">Rätt tecken: ${p.signs} st</span> <span class="t-ex">· varav ${p.exact} exakt</span></span></span><span class="tot">${hot?'<span class="fire" title="5+ poäng idag">🔥</span>':""}<span class="cn" data-c="${rankSort==="pig"?p.pig:rankSort==="pis"?p.pis:p.total}">0</span><span class="totu">poäng</span></span></div>`}).join("")||'<div class="hint" style="padding:8px 4px">Ingen deltagare matchar sökningen.</div>');
  el.querySelectorAll(".rk").forEach(r=>{r.onclick=()=>openPerson(r.dataset.name);r.onkeydown=e=>{if(e.key==="Enter")openPerson(r.dataset.name);};});
  el.querySelectorAll(".cn").forEach(animCount);
}
function setupRankControls(){const se=document.getElementById("rkSearch");if(se)se.oninput=()=>{rankQ=se.value.toLowerCase();renderRank();};document.querySelectorAll("#rkSort button").forEach(b=>b.onclick=()=>{document.querySelectorAll("#rkSort button").forEach(x=>x.classList.remove("active"));b.classList.add("active");rankSort=b.dataset.k;renderRank();});}

function renderMatchList(){
  const el=document.getElementById("matchList");
  const me=ME?D.participants.find(p=>p.name===ME):null;
  const meP=ME?PLIST.find(p=>p.name===ME):null;
  const _f2=document.getElementById("mfilter2");if(_f2){_f2.style.display=(mSeg==="played")?"":"none";_f2.querySelectorAll(".needsme").forEach(b=>b.style.display=meP?"":"none");if((mSeg!=="played"||!meP)&&(resFilter==="exact"||resFilter==="right"||resFilter==="wrong")){resFilter="all";_f2.querySelectorAll("button").forEach(x=>x.classList.toggle("active",x.dataset.r==="all"));}}
  const _sumEl=document.getElementById("mxSummary");if(_sumEl){const _pl=MATCHES.filter(x=>x.score).length,_up=MATCHES.length-_pl;if(mSeg==="played"){_sumEl.innerHTML=`<span class="mxs-main">${_pl} spelade matcher</span>${meP?` <span>· du: <b class="t-ru">${meP.signs} rätt tecken</b> <b class="t-ex">(varav ${meP.exact} exakt)</b> · <b>${meP.pig} p</b></span>`:` <span>· välj ditt namn där uppe för din egen facit</span>`}`;}else{_sumEl.innerHTML=`<span class="mxs-main">${_up} kommande matcher</span> <span>· nästa visas överst</span>`;}}
  const ng=MATCHES.findIndex(x=>x.t==="group"&&!x.score);
  const _d=new Date(),today=("0"+_d.getDate()).slice(-2)+"/"+("0"+(_d.getMonth()+1)).slice(-2);const _tm=new Date(Date.now()+864e5),tomorrow=("0"+_tm.getDate()).slice(-2)+"/"+("0"+(_tm.getMonth()+1)).slice(-2);
  const WD=["Söndag","Måndag","Tisdag","Onsdag","Torsdag","Fredag","Lördag"],MO=["jan","feb","mars","apr","maj","juni","juli","aug","sep","okt","nov","dec"];
  const dayLabel=t=>{const d=parseKick(t);return d?`${WD[d.getDay()]} ${d.getDate()} ${MO[d.getMonth()]}`:"Övriga";};
  let out="",curDay=null,buf="",cnt=0;
  const flush=()=>{if(buf){out+=`<div class="mdaygroup"><div class="mday">${curDay} <span class="mdc">${cnt} ${cnt===1?"match":"matcher"}</span></div>${buf}</div>`;buf="";cnt=0;}};
  let _list=MATCHES.map((m,i)=>({m,i})).filter(o=>mSeg==="played"?!!o.m.score:!o.m.score);
  if(mSeg==="played")_list.reverse();
  _list.forEach(({m,i})=>{if(mFilter!=="all"&&m.t!==mFilter)return;
    const _v=(m.t==="group"&&m.score&&me&&me._g[m.nr])?gpoints(me._g[m.nr],m.score):null;
    if(resFilter==="exact"&&_v!==4)return;if(resFilter==="right"&&_v!==1)return;if(resFilter==="wrong"&&_v!==0)return;
    const dl=dayLabel(m.time);if(dl!==curDay){flush();curDay=dl;}
    cnt++;
    const isNext=i===ng,isToday=(m.time||"").indexOf(today)===0,isTomorrow=(m.time||"").indexOf(tomorrow)===0,to=(m.time||"").split(" ").slice(-1)[0]||"";
    let exCount=0;if(m.t==="group"&&m.score){exCount=PLIST.filter(p=>{const pk=p.ref._g[m.nr];return pk&&gpoints(pk,m.score)===4;}).length;}
    var _lv=isLive(m);const badges=`${_lv?'<span class="pbadge"><i></i>Pågår</span>':isNext?'<span class="nbadge">NÄSTA</span>':""}${!_lv&&isToday&&!isNext?'<span class="tbadge">I DAG</span>':""}${!_lv&&isTomorrow&&!isNext?'<span class="mbadge">IMORGON</span>':""}`;const exb=(m.t==="group"&&m.score)?`<span class="exb ${exCount>=7?"b4":exCount>=4?"b3":exCount>=2?"b2":exCount>=1?"b1":""}">${exCount}× exakt</span>`:"";
    let home,away,sc;
    if(m.t==="group"){home=`<div class="mx-team h">${flag(m.home,18)}<span class="tn">${m.home}</span></div>`;away=`<div class="mx-team a"><span class="tn">${m.away}</span>${flag(m.away,18)}</div>`;sc=m.score?`<div class="mx-score done">${m.score[0]}–${m.score[1]}</div>`:`<div class="mx-score soon">${to||"–"}</div>`;}
    else{home=`<div class="mx-team h"><span class="tn slot">${m.homeSlot}</span></div>`;away=`<div class="mx-team a"><span class="tn slot">${m.awaySlot}</span></div>`;sc=`<div class="mx-score vs">VS</div>`;}
    let guess="",mxp="";
    if(m.t==="group"&&me&&me._g[m.nr]){const pk=me._g[m.nr];let oc="",go="";if(m.score){const v=gpoints(pk,m.score);oc=v===4?"exact":v===1?"right":"wrong";go=`<span class="go">${v===4?"Exakt rätt · +4 poäng":v===1?"Rätt utfall · +1 poäng":"Fel · 0 poäng"}</span>`;mxp=`<span class="mxp ${oc}">${pk[0]}–${pk[1]} · ${v===4?"+4":v===1?"+1":"0"} p</span>`;}else{mxp=`<span class="mxp pend">Du: ${pk[0]}–${pk[1]}</span>`;}guess=`<div class="mx-guess ${m.score?oc:"pending"}"><span class="gl">Din gissning</span><span class="gv">${pk[0]}–${pk[1]}</span>${go}</div>`;}
    buf+=`<div class="mx-row ${m.score?"played":""} ${isNext?"next":""} ${isToday?"today":""}" data-i="${i}"><div class="mx-meta">${m.ph}${m.score?` · ${to}`:""}${badges}<span class="mxr">${exb}${mxp}</span></div><div class="mx-main">${home}${sc}${away}</div>${guess}</div>`;
  });
  flush();
  el.innerHTML=out||('<div class="emptynote">Inga matcher matchar filtret'+((!me&&(resFilter==="exact"||resFilter==="right"||resFilter==="wrong"))?' – välj ditt namn där uppe för att filtrera på dina träffar.':'.')+'</div>');
  el.querySelectorAll(".mx-row").forEach(r=>r.onclick=()=>openMatch(+r.dataset.i));renderHero();
}
const _mt=document.getElementById("mTypeSel");if(_mt)_mt.onchange=()=>{mFilter=_mt.value;renderMatchList();};
document.querySelectorAll("#mfilter2 button").forEach(b=>b.onclick=()=>{document.querySelectorAll("#mfilter2 button").forEach(x=>x.classList.remove("active"));b.classList.add("active");resFilter=b.dataset.r;renderMatchList();});
function scrollToNext(){const e=document.querySelector("#matchList .mx-row.next")||document.querySelector("#matchList .mx-row.today")||document.querySelector("#matchList .mx-row");if(e)e.scrollIntoView({block:"center",behavior:"smooth"});}document.querySelectorAll("#mxSeg button").forEach(b=>b.onclick=()=>{document.querySelectorAll("#mxSeg button").forEach(x=>x.classList.remove("active"));b.classList.add("active");mSeg=b.dataset.seg;renderMatchList();const h=document.getElementById("mxHero");if(h)h.scrollIntoView({block:"start",behavior:"smooth"});});
function fmtMatchDate(t){if(!t)return "";var d=parseKick(t),to=(t.split(" ").slice(-1)[0]||""),MO=["jan","feb","mars","apr","maj","juni","juli","aug","sep","okt","nov","dec"];return d?(d.getDate()+" "+MO[d.getMonth()]+" "+to):t;}
function isLive(m){if(m.t!=="group"||m.score)return false;if(LIVE&&LIVE[m.nr])return true;var k=parseKick(m.time);if(k){var dd=Date.now()-k;return dd>=0&&dd<9000000;}return false;}
function renderHero(){const el=document.getElementById("mxHero");if(!el)return;if(mSeg!=="upcoming"){el.innerHTML="";if(window._hcd)clearInterval(window._hcd);return;}const idx=MATCHES.findIndex(m=>!m.score);if(idx<0){el.innerHTML="";if(window._hcd)clearInterval(window._hcd);return;}const m=MATCHES[idx],isG=m.t==="group";var _me=ME?D.participants.find(p=>p.name===ME):null,_pk=(isG&&_me&&_me._g[m.nr])?_me._g[m.nr]:null;var _live=isLive(m);const teams=isG?`<div class="team"><div>${flagRound(m.home,72)}</div><span class="tn">${m.home}</span></div><div class="sb"><div class="sc pend">VS</div><div class="ft">Kommande</div></div><div class="team"><div>${flagRound(m.away,72)}</div><span class="tn">${m.away}</span></div>`:`<div class="team"><div>${flagRound("?",72)}</div><span class="tn">${m.homeSlot||"TBD"}</span></div><div class="sb"><div class="sc pend">VS</div><div class="ft">Slutspel</div></div><div class="team"><div>${flagRound("?",72)}</div><span class="tn">${m.awaySlot||"TBD"}</span></div>`;el.innerHTML=`<div class="card fcard mxhero" data-i="${idx}"><div class="mxh-top"><span class="mxh-meta">📅 ${fmtMatchDate(m.time)||"TBD"}</span><span class="mxh-eyebrow${_live?" live":""}"><span class="mxh-dot"></span>${_live?"Pågår":"Nästa match"}</span></div><div class="mxh-cd" id="mxHeroCd"></div><div class="fbody">${teams}</div>${_pk?`<div class="mxh-gwrap"><span class="mxh-guess">Din gissning <b>${_pk[0]}–${_pk[1]}</b></span></div>`:""}</div>`;const hb=el.querySelector(".mxhero");if(hb)hb.onclick=()=>openMatch(idx);const cd=document.getElementById("mxHeroCd"),k=parseKick(m.time);if(window._hcd)clearInterval(window._hcd);if(cd&&_live){cd.innerHTML='<div class="mxh-live"><span class="mxh-livedot"></span>Inväntar resultat</div>';}else if(cd&&k){const _seg=function(n,l){return '<span class="cdu"><span class="cdn">'+("0"+n).slice(-2)+'</span><span class="cdt">'+l+'</span></span>';};const tick=()=>{const d=k-Date.now();if(d<=0){cd.innerHTML='<div class="cdlive">🟢 Avspark passerad – inväntar resultat</div>';if(window._hcd)clearInterval(window._hcd);return;}var dd=Math.floor(d/864e5),hh=Math.floor(d%864e5/36e5),mm=Math.floor(d%36e5/6e4),ss=Math.floor(d%6e4/1e3);cd.innerHTML='<div class="cdtop">Avspark om</div><div class="cdrow">'+(dd>0?_seg(dd,"DGR")+'<span class="cdsep">:</span>':"")+_seg(hh,"TIM")+'<span class="cdsep">:</span>'+_seg(mm,"MIN")+'<span class="cdsep">:</span>'+_seg(ss,"SEK")+'</div>';};tick();window._hcd=setInterval(tick,1000);}else if(cd){cd.textContent="";}}

let koRound=0;
function renderBracket(){
  const ROUNDS=[["16-delsfinal","r32","16-delsfinal"],["Åttondelsfinal","r16","Åttondel"],["Kvartsfinal","qf","Kvart"],["Semifinal","sf","Semi"],["Final","final","Final"]];
  const me=ME?D.participants.find(p=>p.name===ME):null;
  const kf=RESULTS.koFixtures||{}, kw=RESULTS.ko||{};
  const sel=document.getElementById("koRoundSel");
  sel.innerHTML=ROUNDS.map((r,i)=>`<button class="krchip ${i===koRound?"active":""}" data-i="${i}">${r[2]}</button>`).join("");
  sel.querySelectorAll(".krchip").forEach(b=>b.onclick=()=>{koRound=+b.dataset.i;renderBracket();});
  const rd=ROUNDS[koRound][0], key=ROUNDS[koRound][1], mineSet=me?me[key]:[];
  const entry=(team,slot,win)=>{const mine=team&&mineSet.includes(team);return `<div class="brow ${win?"win":""} ${mine?"mine":""}">${team?`${flag(team,14)} <span class="bt">${team}</span>`:`<span class="slot">${slot}</span>`}${mine?'<span class="chk">✓</span>':""}</div>`;};
  const ms=D.knockout.filter(k=>k.round===rd);
  document.getElementById("bracketWrap").innerHTML=ms.map(k=>{const fx=kf[k.nr],w=kw[k.nr];const h=fx?fx[0]:null,a=fx?fx[1]:null;
    return `<div class="kocard"><div class="kometa">match #${k.nr} \u00b7 ${k.date}</div>${entry(h,k.homeSlot,w&&h===w)}${entry(a,k.awaySlot,w&&a===w)}</div>`;}).join("");
  const _kn=document.getElementById("koNote");if(_kn)_kn.innerHTML=(!Object.keys(RESULTS.koFixtures||{}).length)?'<div class="emptynote">⚽ Slutspelet börjar 28 juni – lagen och poängen fylls i automatiskt när gruppspelet är avgjort.</div>':"";renderKoScore(me);
}
function renderKoScore(me){const el=document.getElementById("koScore");if(!el)return;
  if(!me){el.innerHTML='<div class="hint" style="margin-bottom:12px">⭐ Välj ditt namn där uppe för att se din slutspelspoäng här.</div>';return;}
  const R=[["Lag till 16-delsfinal","r32",2],["Lag till åttondelsfinal","r16",3],["Kvartsfinallag","qf",5],["Semifinallag","sf",7],["Finallag","final",8]];
  let tot=0;const rows=R.map(([l,k,p])=>{const c=inter(me[k],RESULTS[k]||[]);tot+=c*p;return `<div class="ksrow"><span>${l}</span><span class="ksv">${c} r\u00e4tt \u00d7 ${p}p</span><span class="ksp">${c*p}</span></div>`;}).join("");
  const champ=(RESULTS.champion&&me.champion===RESULTS.champion)?10:0;tot+=champ;
  el.innerHTML=`<div class="ksbox"><div class="kstot"><span>Din slutspelspo\u00e4ng</span><b>${tot} p</b></div>${rows}<div class="ksrow"><span>V\u00e4rldsm\u00e4stare</span><span class="ksv">${RESULTS.champion?(me.champion===RESULTS.champion?"r\u00e4tt":"fel"):"ej avgjort"}</span><span class="ksp">${champ}</span></div></div>`;}
function groupTable(letter){const teams=D.groups[letter];const row={};teams.forEach(t=>row[t]={P:0,W:0,D:0,L:0,GF:0,GA:0,Pts:0});
  D.fixtures.filter(f=>f.grp===letter).forEach(f=>{const r=RESULTS.group[f.nr];if(!r)return;const h=row[f.home],a=row[f.away];if(!h||!a)return;h.P++;a.P++;h.GF+=r[0];h.GA+=r[1];a.GF+=r[1];a.GA+=r[0];if(r[0]>r[1]){h.W++;a.L++;h.Pts+=3;}else if(r[0]<r[1]){a.W++;h.L++;a.Pts+=3;}else{h.D++;a.D++;h.Pts++;a.Pts++;}});
  return teams.map(t=>[t,row[t]]).sort((x,y)=>y[1].Pts-x[1].Pts||(y[1].GF-y[1].GA)-(x[1].GF-x[1].GA));}
function renderTables(){document.getElementById("tablesWrap").innerHTML=Object.keys(D.groups).sort().map(L=>{const rows=groupTable(L);
  return `<div class="gtab"><h4>Grupp ${L}</h4><table><thead><tr><th>Lag</th><th>S</th><th>V</th><th>O</th><th>F</th><th>GM</th><th>IM</th><th class="gd">MS</th><th>P</th></tr></thead><tbody>${rows.map((r,i)=>`<tr class="${i<2?'qual':''}"><td style="white-space:nowrap;overflow:hidden;text-overflow:ellipsis">${flag(r[0],13)}${r[0]}</td><td>${r[1].P}</td><td>${r[1].W}</td><td>${r[1].D}</td><td>${r[1].L}</td><td>${r[1].GF}</td><td>${r[1].GA}</td><td class="gd ${r[1].GF-r[1].GA>0?'pos':r[1].GF-r[1].GA<0?'neg':''}">${r[1].GF-r[1].GA>0?"+"+(r[1].GF-r[1].GA):r[1].GF-r[1].GA}</td><td><b>${r[1].Pts}</b></td></tr>`).join("")}</tbody></table></div>`;}).join("");}
function fillSelects(){const a=document.getElementById("h2hA"),b=document.getElementById("h2hB");const o=PLIST.map(p=>`<option>${p.name}</option>`).join("");a.innerHTML=o;b.innerHTML=o;a.selectedIndex=0;b.selectedIndex=Math.min(1,PLIST.length-1);a.onchange=b.onchange=renderH2H;renderH2H();}
function groupRows(pr){
  let exact=0,right=0,gained=0,played=0;
  const head=`<div class="ps pshead"><span class="ph"></span><span class="mt">Lag · <b style="color:var(--blue)">din gissning</b></span><span class="rs">Facit</span><span class="bd">P</span></div>`;
  const rows=head+pr.groups.map(g=>{const r=RESULTS.group[g[0]];const pk=[g[2],g[3],g[5]];const pts=gpoints(pk,r);let c="";if(pts===4){c="hit";exact++;}else if(pts===1){c="close";right++;}else if(pts===0)c="miss";if(pts!=null){gained+=pts;played++;}
    return `<div class="ps ${c}"><span class="ph">#${g[0]}</span><span class="mt">${flag(g[1],13)} ${abbr(g[1])} <span class="gp">${g[2]}\u2013${g[3]}</span> ${abbr(g[4])} ${flag(g[4],13)}</span><span class="rs">${r?`${r[0]}\u2013${r[1]}`:"\u2014"}</span><span class="bd">${pts==null?"":(pts>0?"+"+pts:"0")}</span></div>`;}).join("");
  return {rows,exact,right,gained,played};
}
function kboxHtml(pr){const chips=a=>a.map(t=>`<span class="kchip">${flag(t,13)} ${t}</span>`).join("");return `<div class="kbox"><b>🏆 Världsmästare:</b> ${pr.champion?flag(pr.champion,14)+" "+pr.champion:"–"}<br><b>👟 Skyttekung:</b> ${pr.skyttekung||"–"}${pr.goals?` (${pr.goals} mål)`:""}</div><h4 style="margin:12px 0 6px">🥇 Final-tips</h4><div class="kchips">${chips(pr.final)}</div>`;}
function renderH2H(){
  const A=PLIST.find(p=>p.name===document.getElementById("h2hA").value),B=PLIST.find(p=>p.name===document.getElementById("h2hB").value);if(!A||!B)return;
  const col=p=>{const g=groupRows(p.ref);return `<div class="h2col"><div class="h2head" style="background:${colorFor(p.name)}"><span class="ava">${initials(p.name)}</span><div><div class="hn">${p.name}</div><div class="hp">#${p.rank} \u00b7 ${p.total} poäng</div></div></div><div class="h2body">${kboxHtml(p.ref)}<h4 style="margin:12px 0 6px">🎯 Gruppspel <span style="font-weight:500;color:var(--muted);font-size:12px">(${g.exact+g.right} rätt tecken, varav ${g.exact} exakt \u00b7 ${g.gained} p)</span></h4><div class="psheet">${g.rows}</div></div></div>`;};
  document.getElementById("h2hResult").innerHTML=`<div class="h2h-cols">${col(A)}${col(B)}</div>`;
}
function openPerson(name){const p=PLIST.find(x=>x.name===name),pr=p.ref;
  document.getElementById("mAva").style.display="";document.getElementById("mAva").textContent=initials(name);document.getElementById("mAva").style.background=colorFor(name);
  document.getElementById("mName").textContent=name;document.getElementById("mSub").textContent=`Placering #${p.rank} av ${PLIST.length} \u00b7 ${p.total} poäng`;
  const g=groupRows(pr);
  document.getElementById("mBody").innerHTML=`<div class="statrow"><div class="stat"><div class="v">${p.pig} <span class="vp">poäng</span></div><div class="l">Gruppspel</div></div><div class="stat"><div class="v">${p.pis} <span class="vp">poäng</span></div><div class="l">Slutspel</div></div><div class="stat"><div class="v">${p.total} <span class="vp">poäng</span></div><div class="l">Total</div></div></div>${kboxHtml(pr)}<h4 style="margin:14px 0 6px">🎯 Gruppspel <span style="font-weight:500;color:var(--muted);font-size:12px">(${g.exact+g.right} rätt tecken, varav ${g.exact} exakt \u00b7 ${g.gained} p på ${g.played} spelade)</span></h4><div class="psheet">${g.rows}</div>`;
  document.getElementById("overlay").classList.add("open");
}
document.getElementById("mClose").onclick=()=>document.getElementById("overlay").classList.remove("open");
document.getElementById("overlay").onclick=e=>{if(e.target.id==="overlay")e.currentTarget.classList.remove("open");};
function goto(v,fromHash){document.querySelectorAll(".tab").forEach(b=>b.classList.toggle("active",b.dataset.view===v));document.querySelectorAll(".view").forEach(s=>s.classList.toggle("active",s.id===v));if(!fromHash&&location.hash!=="#"+v)location.hash=v;window.scrollTo({top:0,behavior:"smooth"});}
window.addEventListener("hashchange",()=>{const v=location.hash.slice(1);if(v&&document.getElementById(v))goto(v,true);});
document.querySelectorAll(".tab").forEach(b=>b.onclick=()=>goto(b.dataset.view));
document.addEventListener("click",e=>{const c=e.target.closest?e.target.closest(".pp2[data-name],.mebanner[data-name]"):null;if(c)openPerson(c.dataset.name);});
const tb=document.getElementById("themeBtn");if(tb){tb.textContent=document.documentElement.getAttribute("data-theme")==="dark"?"☀️":"🌙";tb.onclick=()=>{var d=document.documentElement.getAttribute("data-theme")==="dark",nt=d?"light":"dark";document.documentElement.setAttribute("data-theme",nt);tb.textContent=nt==="dark"?"☀️":"🌙";try{localStorage.setItem("loftahammar_theme",nt);}catch(e){}};}
fillMe();renderMeHem();renderPodium();renderFeatured();renderRank();renderMatchList();renderBracket();renderTables();renderChampViz();renderUpcoming();fillSelects();setupRankControls();(function(){const _pi=document.getElementById("poengInfo");if(_pi)_pi.onclick=openScoring;})();(function(){var _ts=document.getElementById("toStandings");if(_ts)_ts.onclick=function(){goto("standings");};})();(function(){const _h=location.hash.slice(1);if(_h&&document.getElementById(_h))goto(_h,true);})();
(function(){
  var mqMob=window.matchMedia("(max-width:560px)"),mqRm=window.matchMedia("(prefers-reduced-motion:reduce)");
  var ball=document.querySelector(".hdr .ballwrap .ball")||document.querySelector(".hdr .ball");
  var tabs=document.querySelector(".tabs");
  if(!ball||!tabs)return;
  ball.style.cursor="pointer";
  var taps=0,running=false;
  function run(){
    if(running)return;running=true;
    var prevSB=document.documentElement.style.scrollBehavior;document.documentElement.style.scrollBehavior="auto";
    var r=ball.getBoundingClientRect(),size=r.width;
    var clone=document.createElement("div");clone.className="egg-ball";
    clone.style.width=size+"px";clone.style.height=size+"px";clone.style.left=r.left+"px";clone.style.top=r.top+"px";
    clone.innerHTML=ball.innerHTML.replace(/id="bc"/g,'id="ebc"').replace(/url\(#bc\)/g,'url(#ebc)');document.body.appendChild(clone);
    ball.style.visibility="hidden";
    var startX=r.left,startY=r.top,landY=mqMob.matches?(tabs.getBoundingClientRect().top-size+4):(window.innerHeight-size-6);
    var scrollMax=Math.max(0,document.documentElement.scrollHeight-window.innerHeight),rot=0;
    function set(x,y,d){clone.style.left=x+"px";clone.style.top=y+"px";clone.style.transform="rotate("+d+"deg)";}
    var t0=null;
    function fall(ts){if(t0===null)t0=ts;var p=Math.min(1,(ts-t0)/850),ip=p*p;rot=432*ip;set(startX,startY+(landY-startY)*ip,rot);window.scrollTo(0,scrollMax*ip);if(p<1)requestAnimationFrame(fall);else requestAnimationFrame(bounce);}
    var b0=null,amps=[72,40,20,8];
    function bounce(ts){if(b0===null)b0=ts;var p=Math.min(1,(ts-b0)/780),seg=1/amps.length,idx=Math.min(amps.length-1,Math.floor(p/seg)),lp=(p-idx*seg)/seg,h=amps[idx]*Math.sin(Math.PI*lp);rot+=7;set(startX,landY-h,rot);if(p<1)requestAnimationFrame(bounce);else{set(startX,landY,rot);rest();}}
    function rest(){document.documentElement.style.scrollBehavior=prevSB;var last=window.scrollY,fired=false;function onS(){var y=window.scrollY;if(!fired&&y<last-2){fired=true;window.removeEventListener("scroll",onS);rollOff();}last=y;}window.addEventListener("scroll",onS,{passive:true});}
    function rollOff(){var c0=null,rot0=rot,fromX=parseFloat(clone.style.left)||startX;function step(ts){if(c0===null)c0=ts;var p=Math.min(1,(ts-c0)/1100),ip=p*(0.4+0.6*p),toX=window.innerWidth+size,x=fromX+(toX-fromX)*ip,rr=rot0+((x-fromX)/(Math.PI*size))*360;set(x,landY,rr);if(p<1)requestAnimationFrame(step);else{if(clone.parentNode)clone.parentNode.removeChild(clone);ball.style.visibility="";running=false;}}requestAnimationFrame(step);}
    requestAnimationFrame(fall);
  }
  ball.addEventListener("click",function(){if(mqRm.matches||running)return;taps++;if(taps>=10){taps=0;run();}});
})();
function fmtUpd(iso){try{var d=new Date(iso);if(isNaN(d))return null;var MO=["januari","februari","mars","april","maj","juni","juli","augusti","september","oktober","november","december"];return d.getDate()+" "+MO[d.getMonth()]+" "+d.getFullYear()+", "+("0"+d.getHours()).slice(-2)+"."+("0"+d.getMinutes()).slice(-2);}catch(e){return null;}}
function mapFeed(j){if(!j||!j.matches)return null;var alias={"Bosnia-Herzegovina":"Bosnien","Cape Verde Islands":"Kap Verde","Curaçao":"Curacao","Congo DR":"DR Kongo","Ecuador":"Equador"};var fx={};D.fixtures.forEach(function(f){fx[f.grp+"|"+f.home+"|"+f.away]=f.nr;});var out={},live={};j.matches.forEach(function(m){if(m.stage!=="GROUP_STAGE")return;var g=(m.group||"").replace("GROUP_","");var hn=alias[m.homeTeam]||m.homeTeam,an=alias[m.awayTeam]||m.awayTeam;var nr=fx[g+"|"+hn+"|"+an];if(nr==null)return;if(m.status==="IN_PLAY"||m.status==="PAUSED"){live[nr]=true;return;}if(m.status==="FINISHED"&&m.homeScore!=null&&m.awayScore!=null)out[nr]=[m.homeScore,m.awayScore];});return {group:out,updated:j.updatedAt||null,live:live};}
function applyResults(res){if(!res||!res.group)return;LIVE=res.live||{};Object.assign(RESULTS.group,res.group);PLIST=buildPlist();MATCHES.forEach(function(m){if(m.t==="group")m.score=RESULTS.group[m.nr]||null;});cur=MATCHES.findIndex(function(m){return m.t==="group"&&!m.score;});if(cur<0)cur=0;if(res.updated){var _f=fmtUpd(res.updated),_eu=document.getElementById("updatedAt");if(_f&&_eu)_eu.innerHTML="Senast uppdaterad "+_f;}renderPodium();renderFeatured();renderRank();renderMatchList();renderTables();renderChampViz();renderUpcoming();renderMeHem();}
function fetchLiveResults(cb){var url="https://n8n.charma.io/webhook/vm2026-resultat.json";var done=false;var to=setTimeout(function(){if(done)return;done=true;cb(null);},2800);try{fetch(url,{cache:"no-store"}).then(function(r){return r.json();}).then(function(j){if(done)return;done=true;clearTimeout(to);try{cb(mapFeed(j));}catch(e){cb(null);}}).catch(function(){if(done)return;done=true;clearTimeout(to);cb(null);});}catch(e){if(done)return;done=true;clearTimeout(to);cb(null);}}
(function(){var fx=document.getElementById("introFx");var start=Date.now();function reveal(){if(!fx)return;fx.classList.add("reveal");setTimeout(function(){if(fx&&fx.parentNode)fx.parentNode.removeChild(fx);},900);}fetchLiveResults(function(res){try{if(res&&res.group&&(Object.keys(res.group).length||Object.keys(res.live||{}).length))applyResults(res);}catch(e){}if(fx){var wait=Math.max(0,900-(Date.now()-start));setTimeout(reveal,wait);}});})();
</script></body></html>"""

out=TPL.replace("__DATA__",json.dumps(D,ensure_ascii=False)).replace("__ISO__",json.dumps(ISO,ensure_ascii=False)).replace("__RESULTS__",json.dumps(RJS,ensure_ascii=False)).replace("__UPD__",UPD)
open("index.html","w",encoding="utf-8").write(out)
print("written",len(out),"bytes")
