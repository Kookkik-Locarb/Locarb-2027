import re, sys
PAT=re.compile(r'(<(a|button)\b[^>]*\bclass="btn\b[^"]*"[^>]*>)(\s*)([^<]+?)(\s*)(?=<svg|</\2>)')
def wrap(s):
    def r(m):
        if 'class="bl"' in m.group(0): return m.group(0)
        return m.group(1)+m.group(3)+'<span class="bl"><span>'+m.group(4)+'</span></span>'+m.group(5)
    return PAT.sub(r,s)
if __name__=='__main__':
    for f in sys.argv[1:]:
        t=open(f).read(); n=wrap(t); open(f,'w').write(n); print(f, n.count('class="bl"'))
