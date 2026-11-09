"""Build www.pcninja.pro in English (/), Spanish (/es/) and Hebrew (/he/).

Home page: text in tools/strings.py, layout in tools/template.html.
Tools section and tool pages (/apps/<slug>/): text in tools/tools_text.py,
layout in tools/tool_template.html and the functions below.
Run:
    python tools/build.py   (Python 3)
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from strings import EN, ES, HE
import tools_text as TT

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://www.pcninja.pro"
LANGS = [
    # code, path, dir, label, strings, help site, help form
    ("en", "/", "ltr", "EN", EN, "https://help.pcninja.pro/en/", "https://help.pcninja.pro/en/contact/"),
    ("es", "/es/", "ltr", "ES", ES, "https://help.pcninja.pro/es/", "https://help.pcninja.pro/es/contact/"),
    ("he", "/he/", "rtl", "עב", HE, "https://help.pcninja.pro/", "https://help.pcninja.pro/aboutMe/contact/"),
]
PATHS = {code: path for code, path, *_ in LANGS}

# Runs before the page paints. Only the home address "/" ever redirects:
#  1. a language the visitor picked with the buttons (remembered in this browser), else
#  2. the first browser language we have (es / he), else stay in English.
# Links to /es/ or /he/ always open as asked. "?lang=xx" (used by the buttons) saves the choice.
LANG_JS = """(function(){var P=%s,K='pcninja-lang',s=null,q=/[?&]lang=(en|es|he)\\b/.exec(location.search);
try{if(q){localStorage.setItem(K,q[1]);}s=localStorage.getItem(K);}catch(e){}
if(q){history.replaceState(null,'',location.pathname+location.hash);return;}
if(location.pathname!=='/')return;
if(!s){var L=navigator.languages||[navigator.language||''];for(var i=0;i<L.length;i++){var c=String(L[i]).slice(0,2).toLowerCase();if(c==='iw')c='he';if(P[c]){s=c;break;}}}
if(s&&s!=='en'&&P[s])location.replace(P[s]+location.hash);})();""" % (
    "{" + ",".join("%s:'%s'" % (c, p) for c, p in PATHS.items()) + "}")

def langs_menu(current):
    items = []
    for code, path, _d, label, *_ in LANGS:
        cur = ' aria-current="true"' if code == current else ""
        items.append('<li><a href="%s?lang=%s" hreflang="%s" lang="%s"%s>%s</a></li>' % (path, code, code, code, cur, label))
    return '        <ul class="langs" aria-label="Language">' + "".join(items) + "</ul>"

ALTERNATES = "\n".join(
    '  <link rel="alternate" hreflang="%s" href="%s%s">' % (c, SITE, p) for c, p in PATHS.items()
) + '\n  <link rel="alternate" hreflang="x-default" href="%s/">' % SITE

# ---------------------------------------------------------------- tools
GH = "https://github.com/JavierTorresFelendler/"
SLUG = {"wintool": "wintool", "upgrade": "windows-upgrade-tool", "v2": "winupdate-tool-v2",
        "v1": "winupdate-tool-v1", "office": "smart-office-installer"}
REPO = {"wintool": "WinTool-by-PcNinja", "upgrade": "Win-Upgrade-Tool-by-PcNinja", "v2": "PcNinja-WinUpdateTool-V2",
        "v1": "PcNinja-WinUpdateTool-V1", "office": "pcninja-smart-office-installer"}
DL = {k: GH + r + "/releases/latest" for k, r in REPO.items()}
DL["office"] = "https://office.pcninja.pro/"

def tool_path(code, key):
    return PATHS[code] + "apps/" + SLUG[key] + "/"

def month(code, key):
    m, y = TT.MONTH[key]
    return "%s %d" % (TT.L[code]["months"][m - 1], y)

def arrows(d):
    return ("&#8592;", "&#8594;") if d == "rtl" else ("&#8594;", "&#8592;")  # forward, back

def tl_row(code, d, key, last):
    t = TT.L[code]; x = t["T"][key]; fwd, _ = arrows(d)
    label = t["today"] if key == "wintool" else "%s %d" % (t["step"], TT.STEP[key])
    tag = t["latest"] if key == "wintool" else (t["retired"] if key == "v1" else t["in_wt"])
    cls = "tl" + (" now" if key == "wintool" else "") + (" last" if last else "")
    if key == "wintool":
        links = '<a class="more" href="%s">%s %s</a>' % (tool_path(code, key), t["more_wt"], fwd)
    else:
        links = ('<a class="more" href="%s">%s %s</a><a class="btn link-dl" href="%s">%s</a>'
                 '<a class="btn link-src" href="%s">%s</a>') % (
            tool_path(code, key), t["story"], fwd, DL[key], t["dl"], GH + REPO[key], t["src"])
    return """        <div class="%s">
          <div class="when"><div class="lane">%s</div><div class="date">%s</div></div>
          <div class="rail" aria-hidden="true"><i></i><b></b><i></i></div>
          <article class="tool">
            <div>
              <h3><bdi>%s</bdi> <span class="ver" data-repo="%s">%s</span> <span class="tag">%s</span></h3>
              <p>%s</p>
              <div class="became"><b aria-hidden="true">&#8593;</b>%s</div>
            </div>
            <div class="links">%s</div>
          </article>
        </div>
""" % (cls, label, month(code, key), TT.NAME[key], REPO[key], TT.VER[key], tag, x["short"], x["became"], links)

def tools_section(code, d, s):
    t = TT.L[code]; v = TT.V[code]
    caps = "".join("<li><strong>%s</strong><span>%s</span></li>" % c for c in t["caps"])
    nxt = """        <div class="tl next">
          <div class="when"><div class="lane">%s</div><div class="date">%s</div></div>
          <div class="rail" aria-hidden="true"><i></i><b></b><i></i></div>
          <article class="tool"><div><h3>%s</h3><p>%s</p></div></article>
        </div>
""" % (v["label"], v["when"], v["title"], v["short"])
    rows = "".join(tl_row(code, d, k, i == len(TT.ORDER) - 1) for i, k in enumerate(TT.ORDER))
    return """    <section id="tools">
      <div class="wrap">
        <h2>%s</h2>
        <p class="intro">%s</p>

        <div class="feat">
          <div>
            <p class="prompt" aria-hidden="true">PS C:\\Users\\Javier&gt; <span class="cmd">.\\WinTool-by-PcNinja.exe</span></p>
            <h3><bdi>WinTool by PcNinja</bdi> <span class="ver" data-repo="%s">%s</span> <span class="pill">%s</span></h3>
            <p>%s</p>
            <div class="actions">
              <a class="btn btn-primary" href="%s">%s</a>
              <a class="btn btn-quiet" href="%s">%s</a>
              <a class="btn btn-quiet" href="%s">%s</a>
            </div>
            <p class="small">%s</p>
          </div>
          <ul class="caps">%s</ul>
        </div>

        <h3 class="sub">%s</h3>
        <p class="subintro">%s</p>
%s%s      </div>
    </section>""" % (s["tools_h2"], s["tools_intro"], REPO["wintool"], TT.VER["wintool"], t["latest"], t["feat_p"],
                      DL["wintool"], t["dl"], tool_path(code, "wintool"), t["more_wt"], GH + REPO["wintool"], t["src"],
                      t["unsigned"], caps, t["how_h"], t["how_p"], nxt, rows)

def tool_content(code, d, key):
    t = TT.L[code]; x = t["T"][key]; fwd, back = arrows(d)
    nodes = []
    for k in reversed(TT.ORDER):  # oldest first, in reading direction
        inner = "<strong><bdi>%s</bdi></strong><span>%s</span>" % (TT.SHORT[k], month(code, k))
        if k == key:
            nodes.append('<div class="node here" aria-current="page">%s</div>' % inner)
        else:
            nodes.append('<a class="node" href="%s">%s</a>' % (tool_path(code, k), inner))
    strip = ('<div class="arrow" aria-hidden="true">%s</div>' % fwd).join(nodes)
    why = "".join("<p>%s</p>" % p.replace("{v1_url}", tool_path(code, "v1")) for p in x["why"])
    grew = "".join("<li><strong>%s</strong>%s</li>" % g for g in x["grew"])
    does = "".join("<li>%s</li>" % i for i in x["does"])
    vision = ""
    if key == "wintool":
        v = TT.V[code]
        vision = '<div class="vision"><h2>%s</h2>%s</div>' % (v["h"], "".join("<p>%s</p>" % p for p in v["paras"]))
    if x["carried"]:
        right2 = ('<h2 class="gap">%s</h2><ul class="b">%s</ul>'
                  '<div class="box"><strong>%s</strong><p>%s</p><a class="more" href="%s">%s %s</a></div>') % (
            t["carried_h"], "".join("<li>%s</li>" % c for c in x["carried"]), t["move_h"], x["move"],
            tool_path(code, "wintool"), t["go_wt"], fwd)
    else:
        right2 = '<div class="box"><strong>%s</strong><p>%s</p></div><p class="fine">%s</p>' % (t["came_h"], x["move"], t["unsigned"])
    i = TT.ORDER.index(key)
    newer = ('<a class="more" href="%s">%s %s: <bdi>%s</bdi></a>' % (tool_path(code, TT.ORDER[i - 1]), back, t["newer"], TT.SHORT[TT.ORDER[i - 1]])) if i > 0 else "<span></span>"
    older = ('<a class="more" href="%s">%s: <bdi>%s</bdi> %s</a>' % (tool_path(code, TT.ORDER[i + 1]), t["older"], TT.SHORT[TT.ORDER[i + 1]], fwd)) if i < len(TT.ORDER) - 1 else "<span></span>"
    return """    <p class="strip-h">%s</p>
    <div class="strip">%s</div>
    <div class="cols">
      <div>
        <h2>%s</h2>%s
        <h2 class="gap">%s</h2><ul class="grew">%s</ul>%s
      </div>
      <div>
        <h2>%s</h2><ul class="b">%s</ul>
        %s
      </div>
    </div>
    <nav class="pager">%s%s</nav>""" % (t["fits"], strip, t["why_h"], why, t["grew_h"], grew, vision, t["does_h"], does, right2, newer, older)

def plain(html):
    return re.sub(r"<[^>]+>", "", html).replace("&#8217;", "'").replace("&#8220;", '"').replace("&#8221;", '"').replace('"', "&quot;")

def tool_alternates(key):
    return "\n".join('  <link rel="alternate" hreflang="%s" href="%s%s">' % (c, SITE, tool_path(c, key)) for c in PATHS) + \
        '\n  <link rel="alternate" hreflang="x-default" href="%s%s">' % (SITE, tool_path("en", key))

def tool_langs_menu(current, key):
    items = []
    for code, _p, _d, label, *_ in LANGS:
        cur = ' aria-current="true"' if code == current else ""
        items.append('<li><a href="%s?lang=%s" hreflang="%s" lang="%s"%s>%s</a></li>' % (tool_path(code, key), code, code, code, cur, label))
    return '        <ul class="langs" aria-label="Language">' + "".join(items) + "</ul>"

def write(rel, text):
    dest = os.path.join(ROOT, rel.strip("/"), "index.html")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    open(dest, "w", encoding="utf-8", newline="\n").write(text)
    print("wrote", os.path.relpath(dest, ROOT))

def fill(tpl, v):
    return re.sub(r"{{(\w+)}}", lambda m: v[m.group(1)], tpl)

def main():
    tpl = open(os.path.join(ROOT, "tools", "template.html"), encoding="utf-8").read()
    ttpl = open(os.path.join(ROOT, "tools", "tool_template.html"), encoding="utf-8").read()
    urls = []
    for code, path, d, _label, s, help_url, form_url in LANGS:
        font = "&family=Assistant:wght@400;600;700" if code == "he" else ""
        v = dict(s, lang=code, dir=d, path=path, alternates=ALTERNATES, langjs=LANG_JS,
                 langs=langs_menu(code), help=help_url, help_form=form_url, font_extra=font,
                 tools_section=tools_section(code, d, s))
        write(path, fill(tpl, v)); urls.append(path)
        t = TT.L[code]
        for key in TT.ORDER:
            x = t["T"][key]
            title = "%s | PcNinja" % TT.NAME[key]
            tv = dict(s, lang=code, dir=d, path=tool_path(code, key), home=path, alternates=tool_alternates(key),
                      langjs=LANG_JS, langs=tool_langs_menu(code, key), help=help_url, font_extra=font,
                      title=title, desc=plain(x["lede"]), og_desc=plain(x["lede"]), crumb_tools=t["tools"],
                      name=TT.NAME[key], name_short=TT.SHORT[key], cmd=TT.CMD[key], repo=REPO[key], ver=TT.VER[key],
                      pill=(' <span class="pill">%s</span>' % t["latest"]) if key == "wintool" else "",
                      lede=x["lede"], dl_url=DL[key], dl=t["dl"], src_url=GH + REPO[key], src=t["src"],
                      notes_url=GH + REPO[key] + "/releases", notes=t["notes"], content=tool_content(code, d, key))
            write(tool_path(code, key), fill(ttpl, tv)); urls.append(tool_path(code, key))
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for p in urls:
            f.write("  <url><loc>%s%s</loc></url>\n" % (SITE, p))
        f.write("</urlset>\n")

if __name__ == "__main__":
    main()
