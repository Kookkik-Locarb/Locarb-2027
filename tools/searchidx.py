import json
TH=json.load(open('/tmp/TH.json'))
def t(x): return TH.get(x,x)
pages=[
('Solutions','Solution-IFRS.dc.html','IFRS S1 & S2 consulting',"End-to-end IFRS S1/S2 support, from gap analysis and climate risk and financial impact assessment to your first disclosure.",'ifrs s1 s2 issb disclosure climate gap analysis ที่ปรึกษา'),
('Solutions','Solution-CarbonCal.dc.html','CarbonCal + Carbon Camp',"Measure Scope 1, 2 and 3 emissions on one easy, accurate platform, so your carbon footprint for organization (CFO) is ready for disclosure and TGO registration, with training that brings your team on board.",'carbon accounting scope 1 2 3 ghg platform free trial คาร์บอน'),
('Solutions','Solution-ISSB.dc.html','ISSB training',"Hands-on ISSB reporting training from Thailand's first ISSB training partner.",'issb training workshop board อบรม'),
('Solutions','Solution-CarbonScout.dc.html','Carbon Scout',"Track and verify carbon on farmland and plantations, ready for carbon credits.",'carbon credit farmland plantation agriculture คาร์บอนเครดิต เกษตร สวน'),
('Solutions','Solution-Reporting.dc.html','Sustainability-related reporting & consulting',"Sustainability and ESG reports and strategy that meet GRI, CDP and other standards, through to your Net Zero pathway, led by our specialist team.",'report esg gri cdp net zero 56-1 รายงาน'),
('About','About-Story.dc.html',"LO-CARB's story",'Mission, history and key numbers','about mission history company เกี่ยวกับ'),
('About','About-Certificates.dc.html','Certificates','IFRS Sustainability Alliance and more','certificate iso tgo ใบรับรอง alliance'),
('About','About-Board.dc.html','Board of directors','The people who lead LO-CARB','board directors team กรรมการ'),
('Pages','Blog.dc.html','All posts','Client stories, explainers on IFRS, ISSB and carbon, and news from the LO-CARB team.','blog insights บทความ'),
('Pages','Contact.dc.html','Contact Us','Tell us what you need. Business enquiries go to our team; job applications go straight to HR.','contact email careers job ติดต่อ สมัครงาน'),
]
posts=[
('Blog-Story.dc.html','[Client name]: IFRS S1 & S2 readiness in [X] weeks','Portfolio'),
('Blog-Article.dc.html','What IFRS S2 means for SET-listed companies','Knowledge base'),
('Blog-Story.dc.html','[Client name]: measuring Scope 1–3 with CarbonCal','Portfolio'),
('Blog-Article.dc.html','IFRS S1 vs S2: what each standard asks for','Knowledge base'),
('Blog-Article.dc.html','ISSB for Boards workshop returns to Bangkok on 21 Nov','News & events'),
('Blog-Article.dc.html','Scope 1, 2 and 3 emissions explained','Knowledge base'),
('Blog-Article.dc.html','How to start collecting Scope 3 supplier data','Knowledge base'),
('Blog-Article.dc.html','Climate scenario analysis for first-time reporters','Knowledge base'),
('Blog-Article.dc.html','Double materiality, explained','Knowledge base'),
('Blog-Article.dc.html','What boards need to know about ISSB','Knowledge base'),
]
G={'Solutions':'โซลูชัน','About':'เกี่ยวกับเรา','Pages':'หน้า','Articles':'บทความ'}
idx=[]
for g,h,ti,d,kw in pages: idx.append({'g':g,'gt':G[g],'h':h,'t':ti,'tt':t(ti),'d':d,'dt':t(d),'k':kw})
for h,ti,c in posts: idx.append({'g':'Articles','gt':G['Articles'],'h':h,'t':ti,'tt':t(ti),'d':c,'dt':t(c),'k':''})
miss=[x['t'] for x in idx if x['tt']==x['t']]+[x['d'] for x in idx if x['dt']==x['d']]
print('untranslated:',miss)
json.dump(idx,open('/tmp/searchidx.json','w'),ensure_ascii=False)
