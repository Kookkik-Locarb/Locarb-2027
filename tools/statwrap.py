import re,sys
for f in sys.argv[1:]:
    s=open(f).read()
    n=re.sub(r'(<p class="anum-s">)(.*?)(</p>)',lambda m: m.group(1)+re.sub(r'(?<!<b>)\[x\]','<b>[x]</b>',m.group(2))+m.group(3),s)
    open(f,'w').write(n)
