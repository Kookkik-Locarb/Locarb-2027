import re, sys
def recolor(s):
    s=s.replace('--mint:#8FE3B0','--mint:#0EA552')
    s=re.sub(r'(fill|stroke|stop-color)="#8FE3B0"',r'\1="#0EA552"',s)
    s=s.replace('#8FE3B0','var(--mint)').replace('#8fe3b0','var(--mint)')
    for a,b in [('#0B7A3E','#0EA552'),('#0b7a3e','#0EA552'),('#075F30','#000000'),('#06331B','#000000'),('#0A4426','#000000'),('#086332','#000000'),('#12B05E','#0EA552'),('#0E0E0C','#000000'),('#0A3A20','#000000'),('#1E4A2C','#000000'),('#0A8A44','#0EA552')]:
        s=s.replace(a,b)
    s=re.sub(r'rgba\(\s*143\s*,\s*227\s*,\s*176\s*,',  'rgba(14,165,82,',s)
    s=re.sub(r'rgba\(\s*11\s*,\s*122\s*,\s*62\s*,',    'rgba(14,165,82,',s)
    s=re.sub(r'rgba\(\s*(6\s*,\s*51\s*,\s*27|4\s*,\s*34\s*,\s*18|14\s*,\s*14\s*,\s*12)\s*,','rgba(0,0,0,',s)
    s=s.replace('class="it" style="color:#0EA552"','class="it" style="color:var(--forest)"')
    if '/* CI palette */' not in s and '@media (max-width:1080px){' in s:
        i=s.index('@media (max-width:1080px){')
        s=s[:i]+'/* CI palette */\n.values,.mintro,.pcta,.banner,.psec.green,.okmsg,.inlinecta,.story.green{--mint:#F3F0DF}\n'+s[i:]
    return s
if __name__=='__main__':
    for f in sys.argv[1:]:
        t=open(f).read(); n=recolor(t); open(f,'w').write(n); print(f, t!=n)
