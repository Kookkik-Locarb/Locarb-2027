import re,json,os,shutil,glob,html
SRC='/mnt/user-data/outputs/artifacts/f4e40824-ae7d-4cfb-9d09-67115159c811/project/'
REPO='/tmp/repo/Locarb-2027/'
OUT='/tmp/static/site/'
shutil.rmtree(OUT,ignore_errors=True); os.makedirs(OUT+'assets/fonts'); os.makedirs(OUT+'assets/images')
amap=json.load(open(REPO+'assets/asset-map.json'))
# copy asset files
for k,v in amap.items():
    src=REPO+v
    if os.path.exists(src):
        dst=OUT+v
        os.makedirs(os.path.dirname(dst),exist_ok=True); shutil.copy(src,dst)
shutil.copy('/tmp/static/runtime.js',OUT+'assets/runtime.js'); shutil.copy('/tmp/static/morphdom.js',OUT+'assets/morphdom.js')
NAME={'Main.dc.html':'index.html'}
for f in glob.glob(SRC+'*.dc.html'):
    b=os.path.basename(f)
    if b not in NAME: NAME[b]=b.replace('.dc.html','.html')
def fix_assets(s):
    def r(m):
        key='/_blob/'+m.group(1)
        v=amap.get(key)
        return ('/'+v) if v else m.group(0)
    s=re.sub(r'/_blob/([0-9a-f]{32})(\?v=\{\{[^}]*\}\})?',r,s)
    return s
missing=set()
for f in sorted(glob.glob(SRC+'*.dc.html')):
    b=os.path.basename(f); s=open(f).read()
    for m in re.findall(r'/_blob/([0-9a-f]{32})',s):
        if '/_blob/'+m not in amap: missing.add(m)
    title=re.search(r'<title>(.*?)</title>',s,re.S).group(1)
    meta=re.search(r'<meta name="description"[^>]*>',s)
    links=re.findall(r'<link rel="stylesheet"[^>]*>',s[:s.index('<body')])
    helmet=re.search(r'<helmet>(.*?)</helmet>',s,re.S).group(1)
    xa=s.index('<x-dc>')+6; xb=s.index('</x-dc>')
    body=re.sub(r'<helmet>.*?</helmet>','',s[xa:xb],flags=re.S)
    js=re.search(r'<script type="text/x-dc"[^>]*>(.*?)</script>',s,re.S).group(1)
    for k,v in NAME.items():
        body=body.replace('href="'+k,'href="'+('/' if v=='index.html' else v))
    if b=='Main.dc.html': body=body.replace('href="#top"','href="#top"')
    page='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>'''+title+'''</title>
'''+(meta.group(0)+'\n' if meta else '')+'\n'.join(links)+'''
'''+helmet+'''
<link rel="icon" href="/assets/images/logo-official.webp">
</head>
<body>
<div id="app"></div>
<template id="tpl">'''+body+'''</template>
<script src="/assets/morphdom.js"></script>
<script src="/assets/runtime.js"></script>
<script>
LocarbRuntime.mount(function (DCLogic) {
'''+js+'''
return Component;
});
</script>
</body>
</html>
'''
    page=fix_assets(page)
    open(OUT+NAME[b],'w').write(page)
# css: fix blob urls inside site.css
css=open(REPO+'assets/site.css').read(); css=fix_assets(css); open(OUT+'assets/site.css','w').write(css)
open(OUT+'vercel.json','w').write(json.dumps({"cleanUrls":True,"trailingSlash":False},indent=2))
print('pages',len(NAME),'missing blobs',missing)
