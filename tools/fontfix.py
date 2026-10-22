import sys
R=[('"Anakotmai","Noto Sans Thai",system-ui,sans-serif','"Anakotmai",sans-serif'),
   ('"STIX Two Text",Georgia,serif','"STIX Two Text",serif'),
   ('STIX Two Text, Georgia, serif','STIX Two Text, serif'),
   ('"Montserrat", sans-serif','sans-serif')]
for f in sys.argv[1:]:
    s=open(f).read(); o=s
    for a,b in R: s=s.replace(a,b)
    if f.endswith('Main.en.html') and '/* Fonts: attached files only */' not in s:
        i=s.index('@media (max-width:1080px){')
        s=s[:i]+'/* Fonts: attached files only */\n.lc{font-synthesis:none}\n.lc button,.lc input,.lc textarea,.lc select{font-family:inherit}\n.lc em,.lc i,.lc address,.lc cite{font-style:normal}\n.lc .it,.lc [class*="it"] em{font-style:italic}\n'+s[i:]
    open(f,'w').write(s); print(f, o!=s)
