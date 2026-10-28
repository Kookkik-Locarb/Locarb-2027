import re, json, html, sys
TH=json.load(open('/tmp/TH.json'))
NAV_OLD='<button aria-label="ภาษาไทย">TH</button>\n<button class="on" aria-label="English">EN</button>'
NAV_NEW='<button class="{{thOn}}" onClick="{{setTH}}" aria-label="ภาษาไทย" lang="th">TH</button>\n<button class="{{enOn}}" onClick="{{setEN}}" aria-label="English">EN</button>'
FT_OLD='<a href="#th">TH</a><a href="#en" class="on" aria-current="true">EN</a>'
FT_NEW='<button class="{{thOn}}" onClick="{{setTH}}" lang="th">TH</button><button class="{{enOn}}" onClick="{{setEN}}">EN</button>'
CSS='''
/* ---- Thai language rendering ---- */
.th-root{font-family:"Anakotmai",sans-serif}
.th-root *:not(svg):not(svg *):not(.hh):not(.hh *){font-family:"Anakotmai",sans-serif !important;letter-spacing:0 !important}
.th-root h1:not(.hh),.th-root h2,.th-root h3,.th-root h4,.th-root .display:not(.hh),.th-root .ptitle2,.th-root .ftitle,.th-root .i2-big,.th-root .f2-tag,.th-root .mission,.th-root .statement{line-height:1.3 !important}
.th-root .it{font-style:normal}
.f2-lang button{min-width:36px;height:30px;padding:0 10px;border:0;border-radius:999px;background:transparent;font-family:"Termina",sans-serif;font-weight:700;font-size:10.5px;color:#B9B6A3;cursor:pointer}
.f2-lang button.on{background:#F3F0DF;color:var(--ink)}
'''
def tr_text(body):
    def seg(m):
        raw=m.group(1)
        if '{{' in raw: return m.group(0)
        core=html.unescape(raw).strip()
        if core and core in TH:
            lead=raw[:len(raw)-len(raw.lstrip())]; trail=raw[len(raw.rstrip()):]
            return '>'+lead+html.escape(TH[core],quote=False).replace('\n','<br>')+trail+'<'
        return m.group(0)
    body=re.sub(r'>([^<>]+)<',seg,body)
    def att(m):
        v=html.unescape(m.group(2))
        if '{{' in v or v not in TH: return m.group(0)
        return '%s="%s"'%(m.group(1),html.escape(TH[v]))
    body=re.sub(r'\b(alt|aria-label|placeholder)="([^"]*)"',att,body)
    return body
WRAP_JS='''
  renderVals() {
    const v = this.renderVals0();
    let lang = this.state.lang;
    if (!lang) { try { lang = localStorage.getItem('locarb-lang') || 'en'; } catch (e) { lang = 'en'; } }
    const th = lang === 'th';
    const setLang = (l) => {
      try { localStorage.setItem('locarb-lang', l); } catch (e) {}
      const go = () => this.setState({ lang: l });
      try {
        const reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        if (!reduce && document.startViewTransition) { document.startViewTransition(go); return; }
      } catch (e) {}
      go();
    };
    const TH = __TH__;
    const tr = (x) => {
      if (!th) return x;
      if (typeof x === 'string') return Object.prototype.hasOwnProperty.call(TH, x) ? TH[x] : x;
      if (Array.isArray(x)) return x.map(tr);
      if (x && typeof x === 'object' && Object.getPrototypeOf(x) === Object.prototype) { const o = {}; for (const k in x) o[k] = tr(x[k]); return o; }
      return x;
    };
    const out = {};
    for (const k in v) out[k] = tr(v[k]);
    // ---- site search ----
    const IDX = __IDX__;
    const q = this.state.q || '';
    const terms = q.trim().toLowerCase().split(/\s+/).filter(Boolean);
    const loc = (x) => ({ h: x.h, t: th ? x.tt : x.t, d: th ? x.dt : x.d, g: th ? x.gt : x.g });
    const hits = terms.length ? IDX.filter((x) => { const hay = (x.t + ' ' + x.tt + ' ' + x.d + ' ' + x.dt + ' ' + x.k + ' ' + x.g + ' ' + x.gt).toLowerCase(); return terms.every((w) => hay.indexOf(w) >= 0); }).slice(0, 8).map(loc) : [];
    const sugg = th ? ['IFRS S2', 'CarbonCal', 'Scope 3', 'ISSB', 'ติดต่อ'] : ['IFRS S2', 'CarbonCal', 'Scope 3', 'ISSB', 'Contact'];
    const search = {
      searchOpen: !!this.state.searchOpen, q: q,
      openSearch: () => this.setState({ searchOpen: true, q: '' }),
      closeSearch: () => this.setState({ searchOpen: false }),
      stopS: (e) => { if (e && e.stopPropagation) e.stopPropagation(); },
      onQ: (e) => this.setState({ q: (e && e.target) ? e.target.value : '' }),
      onKey: (e) => { if (e && e.key === 'Escape') this.setState({ searchOpen: false }); },
      showSuggest: terms.length === 0,
      suggest: sugg.map((w) => ({ label: w, pick: () => this.setState({ q: w }) })),
      quick: IDX.filter((x) => x.g === 'Solutions').slice(0, 5).map(loc),
      results: hits, hasResults: terms.length > 0 && hits.length > 0, noResults: terms.length > 0 && hits.length === 0,
      resultCount: th ? ('ผลการค้นหา ' + hits.length + ' รายการ') : (hits.length + (hits.length === 1 ? ' result' : ' results')),
      emptyTitle: th ? ('ไม่พบผลลัพธ์สำหรับ “' + q.trim() + '”') : ('No results for “' + q.trim() + '”')
    };
    let ck = this.state.cookie;
    if (ck === undefined) { try { ck = localStorage.getItem('locarb-cookie') || ''; } catch (e) { ck = ''; } }
    const saveCk = (val) => { try { localStorage.setItem('locarb-cookie', val); } catch (e) {} this.setState({ cookie: val, showCookie: false }); };
    const cookie = {
      showCookie: this.state.showCookie !== undefined ? !!this.state.showCookie : !ck,
      acceptCookies: () => saveCk('all'),
      rejectCookies: () => saveCk('essential'),
      openCookies: () => this.setState({ showCookie: true })
    };
    if (!this._motionInit) {
      this._motionInit = true;
      try {
        const reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        const SEL = 'nav.ftabs, nav.asub';
        if (!window.__lcTabClick) {
          window.__lcTabClick = true;
          document.addEventListener('click', (ev) => {
            const a = ev.target && ev.target.closest ? ev.target.closest('nav.ftabs a, nav.asub a') : null;
            if (!a) return;
            const nav = a.closest(SEL); const on = nav && nav.querySelector('a.on');
            if (!nav || !on) return;
            const nr = nav.getBoundingClientRect(), r = on.getBoundingClientRect();
            try { sessionStorage.setItem('locarb-tabfrom', JSON.stringify({ g: nav.getAttribute('aria-label') || '', l: r.left - nr.left, w: r.width })); } catch (e) {}
          }, true);
        }
        const run = () => {
          let from = null;
          try { from = JSON.parse(sessionStorage.getItem('locarb-tabfrom') || 'null'); sessionStorage.removeItem('locarb-tabfrom'); } catch (e) {}
          document.querySelectorAll(SEL).forEach((nav) => {
            const on = nav.querySelector('a.on'); if (!on || nav.querySelector('.tab-ink')) return;
            const nr = nav.getBoundingClientRect(), r = on.getBoundingClientRect();
            const ink = document.createElement('span'); ink.className = 'tab-ink'; ink.setAttribute('aria-hidden', 'true');
            ink.style.left = (r.left - nr.left) + 'px'; ink.style.top = (r.top - nr.top) + 'px'; ink.style.width = r.width + 'px'; ink.style.height = r.height + 'px';
            nav.classList.add('has-ink'); nav.insertBefore(ink, nav.firstChild);
            if (reduce) return;
            const same = from && from.g === (nav.getAttribute('aria-label') || '');
            if (same) {
              const dx = from.l - (r.left - nr.left), sx = from.w / r.width;
              ink.animate([{ transform: 'translateX(' + dx + 'px) scaleX(' + sx + ')' }, { transform: 'none' }], { duration: 480, easing: 'cubic-bezier(.2,.8,.2,1)' });
            } else {
              ink.animate([{ transform: 'scale(.85)', opacity: 0 }, { transform: 'none', opacity: 1 }], { duration: 360, easing: 'cubic-bezier(.3,1.3,.5,1)' });
            }
          });
        };
        setTimeout(run, 60);
      } catch (e) {}
    }
    if (this._intro === undefined) {
      try { this._intro = !sessionStorage.getItem('locarb-intro'); sessionStorage.setItem('locarb-intro', '1'); sessionStorage.removeItem('locarb-intro-force'); } catch (e) { this._intro = true; }
      try { if (!this._intro && document.readyState !== 'complete') window.addEventListener('load', () => this.setState({ pageLoaded: true }), { once: true }); } catch (e) {}
    }
    if (this._t0 === undefined) this._t0 = Date.now();
    let pageLoaded = !!this.state.pageLoaded; try { pageLoaded = pageLoaded || document.readyState === 'complete'; } catch (e) { pageLoaded = true; }
    const loaderV = { ldCls: this.state.skipIntro ? 'skip' : (this._intro ? ((this._replay || 0) % 2 ? 'full rep' : 'full') : (pageLoaded ? 'gone' : 'wait')), ldFull: !!this._intro, ldQuick: !this._intro, skipIntro: () => this.setState({ skipIntro: true }), skipLabel: th ? 'ข้ามอินโทร' : 'Skip intro',
      goHome: () => { /* logo is a normal link; the intro only plays on the first page of a visit or when loading is slow */ }, introDelay: this.state.skipIntro ? '0.3s' : ((this._intro && this._t0 !== undefined) ? Math.max(0, 6.4 - (Date.now() - this._t0) / 1000).toFixed(2) + 's' : (this._intro ? '6.4s' : '0s')), ldNonce: (this._nonce = this._nonce || String(Date.now())) };
    const sm = !!this.state.sizeOpen, lm = !!this.state.langOpen;
    const menus = {
      sizeOpen: sm, langOpen: lm, sizeBtn: sm ? 'open' : '', langBtn: lm ? 'open' : '', sizeExp: sm ? 'true' : 'false', langExp: lm ? 'true' : 'false',
      toggleSize: () => this.setState({ sizeOpen: !sm, langOpen: false }), toggleLang: () => this.setState({ langOpen: !lm, sizeOpen: false }),
      closeMenus: () => { if (sm || lm) this.setState({ sizeOpen: false, langOpen: false }); },
      pickS: () => { if (v.setS) v.setS(); this.setState({ sizeOpen: false }); }, pickM: () => { if (v.setM) v.setM(); this.setState({ sizeOpen: false }); }, pickL: () => { if (v.setL) v.setL(); this.setState({ sizeOpen: false }); },
      pickTH: () => { this.setState({ langOpen: false }); setLang('th'); }, pickEN: () => { this.setState({ langOpen: false }); setLang('en'); },
      langCode: th ? 'TH' : 'EN',
      navOpen: !!this.state.navOpen, navExp: this.state.navOpen ? 'true' : 'false',
      toggleNav: () => this.setState({ navOpen: !this.state.navOpen, sizeOpen: false, langOpen: false }),
      closeNav: () => { if (this.state.navOpen) this.setState({ navOpen: false }); },
      navKey: (e) => { if (e && e.key === 'Escape') this.setState({ navOpen: false }); }
    };
    return Object.assign(out, search, cookie, loaderV, menus, { isEN: !th, isTH: th, thOn: th ? 'on' : '', enOn: th ? '' : 'on', setTH: () => setLang('th'), setEN: () => setLang('en') });
  }
  renderVals0() {'''
def build(src):
    s=src
    assert 'class="th-root"' not in s, 'already bilingual'
    s=s.replace(NAV_OLD,NAV_NEW).replace(FT_OLD,FT_NEW)
    # css
    if '</helmet>' in s and '<style>' in s[:s.index('</helmet>')]:
        i=s.index('</style>'); s=s[:i]+CSS+s[i:]
    # body
    m=re.search(r'<div class="lc"[^>]*>',s); a=m.end()
    b=s.rindex('</div>',0,s.index('</x-dc>'))
    en=s[a:b]
    loader=''
    if '<!-- loader -->' in en:
        la=en.index('<!-- loader -->'); lb=en.index('<!-- /loader -->')+len('<!-- /loader -->')
        loader=en[la:lb]; en=en[:la]+en[lb:]
    thb=tr_text(en)
    body='\n'+loader+'\n<sc-if value="{{isEN}}" hint-placeholder-val="{{ true }}">'+en+'</sc-if>\n<sc-if value="{{isTH}}" hint-placeholder-val="{{ false }}"><div class="th-root" lang="th">'+thb+'</div></sc-if>\n'
    s=s[:a]+body+s[b:]
    # js
    sc_a=s.index('data-dc-script'); js=s[sc_a:]
    needed={k:v for k,v in TH.items() if ("'"+k.replace("'","\\'")+"'") in js or ('"'+k+'"') in js or (k.startswith('Subject: ') and 'Subject: ' in js)}
    js=js.replace('  renderVals() {',WRAP_JS.replace('__TH__',json.dumps(needed,ensure_ascii=False)).replace('__IDX__',open('/tmp/searchidx.json').read()),1)
    s=s[:sc_a]+js
    return s
if __name__=='__main__':
    for f in sys.argv[1:]:
        t=open(f).read(); n=build(t); open(f,'w').write(n); print(f,len(t),'->',len(n))
