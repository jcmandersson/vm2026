#!/usr/bin/env python3
"""Bygger om VM-tips-siten: läser facit ur results.json och patchar in det i
index.html (mellan markörerna). Tipsen/strukturen ligger redan i filen.
Körs av den schemalagda uppgiften efter varje match."""
import json, re, os
HERE=os.path.dirname(os.path.abspath(__file__))
html=open(os.path.join(HERE,"index.html"),encoding="utf-8").read()
res=json.load(open(os.path.join(HERE,"results.json"),encoding="utf-8"))
rjs={"group":res.get("group",{}),"r32":res.get("r32",[]),"r16":res.get("r16",[]),
     "qf":res.get("qf",[]),"sf":res.get("sf",[]),"final":res.get("final",[]),
     "champion":res.get("champion"),"snapshot":res.get("snapshot",{})}
newR="/*RESULTS_START*/const RESULTS = "+json.dumps(rjs,ensure_ascii=False)+";/*RESULTS_END*/"
if "/*RESULTS_START*/" in html:
    html=re.sub(r"/\*RESULTS_START\*/.*?/\*RESULTS_END\*/", lambda m:newR, html, flags=re.S)
else:
    old="const RESULTS = { group:{}, r32:[], r16:[], qf:[], sf:[], final:[], champion:null };"
    html=html.replace(old, newR, 1)
played=len(rjs["group"])
updstr=res.get("updated","")
upd='const totalUpdated="Senast uppdaterad '+updstr+'";'
html=re.sub(r'const totalUpdated="[^"]*";', lambda m:upd, html, count=1)
open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(html)
print("OK -",played,"gruppresultat inlagda, uppdaterad",updstr)
