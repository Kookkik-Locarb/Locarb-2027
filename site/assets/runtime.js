/* LO-CARB static runtime — renders the page template with the page's Component logic.
   Supports {{path}} bindings, on* handlers, <sc-if value> and <sc-for list as>. */
(function () {
  var VOID = {area:1,base:1,br:1,col:1,embed:1,hr:1,img:1,input:1,link:1,meta:1,source:1,track:1,wbr:1};
  var BOOL = {autoplay:1,muted:1,loop:1,playsinline:1,autofocus:1,disabled:1,checked:1,disablepictureinpicture:1,hidden:1,required:1,readonly:1,selected:1};
  function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
  function get(scope, expr){
    expr = expr.trim();
    if (expr === 'true') return true; if (expr === 'false') return false;
    var parts = expr.split('.'), v = scope;
    for (var i=0;i<parts.length;i++){ if (v == null) return undefined; v = v[parts[i]]; }
    return v;
  }
  function interp(str, scope){
    return str.replace(/\{\{([^}]*)\}\}/g, function(_, e){ var v = get(scope, e); return v == null ? '' : v; });
  }
  function whole(str){ var m = /^\s*\{\{([^}]*)\}\}\s*$/.exec(str); return m ? m[1] : null; }
  var handlers, hid;
  function walk(node, scope, out){
    if (node.nodeType === 3){ out.push(esc(interp(node.nodeValue, scope)).replace(/&quot;/g,'"')); return; }
    if (node.nodeType !== 1) return;
    var tag = node.localName;
    if (tag === 'sc-if'){
      var e = whole(node.getAttribute('value') || '');
      if (e !== null && get(scope, e)) kids(node, scope, out);
      return;
    }
    if (tag === 'sc-for'){
      var le = whole(node.getAttribute('list') || ''), as = node.getAttribute('as') || 'item';
      var list = le !== null ? get(scope, le) : null;
      if (list && list.length) for (var i=0;i<list.length;i++){ var s = Object.create(scope); s[as] = list[i]; kids(node, s, out); }
      return;
    }
    var name = node.namespaceURI === 'http://www.w3.org/2000/svg' ? node.tagName : tag;
    out.push('<' + name);
    for (var a=0; a<node.attributes.length; a++){
      var at = node.attributes[a], an = at.name, av = at.value;
      if (an.indexOf('hint-') === 0) continue;
      if (an.length > 2 && an.slice(0,2) === 'on'){
        var fe = whole(av); if (fe === null) continue;
        var fn = get(scope, fe); if (typeof fn !== 'function') continue;
        var id = 'h' + (hid++); handlers[id] = fn;
        out.push(' data-' + an + '="' + id + '"');
        continue;
      }
      if (BOOL[an] && av === '') { out.push(' ' + an); continue; }
      out.push(' ' + an + '="' + esc(interp(av, scope)) + '"');
    }
    out.push('>');
    if (VOID[tag]) return;
    kids(node.content || node, scope, out);
    out.push('</' + name + '>');
  }
  function kids(node, scope, out){ for (var c = node.firstChild; c; c = c.nextSibling) walk(c, scope, out); }
  var EVENTS = ['onclick','oninput','onkeydown','onmouseleave','onmousemove','onchange','onsubmit','onmouseenter'];
  function bind(root){
    EVENTS.forEach(function(ev){
      var els = root.querySelectorAll('[data-' + ev + ']');
      for (var i=0;i<els.length;i++){ (function(el){ var fn = handlers[el.getAttribute('data-' + ev)]; el[ev] = function(e){ return fn(e); }; })(els[i]); }
    });
  }
  window.LocarbRuntime = { mount: function(factory){
    var tpl = document.getElementById('tpl'), app = document.getElementById('app');
    function DCLogic(props){ this.props = props || {}; this.state = {}; }
    DCLogic.prototype.setState = function(o){ var self = this; if (typeof o === 'function') o = o(this.state); for (var k in o) this.state[k] = o[k]; schedule(); };
    var Component = factory(DCLogic), comp = new Component({}), pending = false, first = true;
    function render(){
      pending = false; handlers = {}; hid = 0;
      var out = [], vals = comp.renderVals();
      kids(tpl.content, vals, out);
      var html = '<div id="app">' + out.join('') + '</div>';
      if (first){ app.innerHTML = out.join(''); first = false; }
      else window.morphdom(app, html, { onBeforeElUpdated: function(from, to){ if (from.tagName === 'VIDEO') return false; if (from === document.activeElement && from.tagName === 'INPUT') { to.value = from.value; } return true; } });
      bind(app);
      var af = app.querySelector('input[autofocus]');
      if (af && !af.__f) { af.__f = true; try { af.focus(); } catch (e) {} }
    }
    function schedule(){ if (!pending){ pending = true; requestAnimationFrame(render); } }
    render();
  } };
})();
