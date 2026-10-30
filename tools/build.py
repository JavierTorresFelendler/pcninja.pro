"""Build www.pcninja.pro in English (/), Spanish (/es/) and Hebrew (/he/).

Edit text in tools/strings.py, layout in tools/template.html, then run:
    python tools/build.py   (Python 3)
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from strings import EN, ES, HE

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

def main():
    tpl = open(os.path.join(ROOT, "tools", "template.html"), encoding="utf-8").read()
    for code, path, d, _label, s, help_url, form_url in LANGS:
        v = dict(s, lang=code, dir=d, path=path, alternates=ALTERNATES, langjs=LANG_JS,
                 langs=langs_menu(code), help=help_url, help_form=form_url,
                 font_extra="&family=Assistant:wght@400;600;700" if code == "he" else "")
        out = re.sub(r"{{(\w+)}}", lambda m: v[m.group(1)], tpl)
        dest = os.path.join(ROOT, path.strip("/"), "index.html")
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "w", encoding="utf-8", newline="\n").write(out)
        print("wrote", os.path.relpath(dest, ROOT))
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for p in PATHS.values():
            f.write("  <url><loc>%s%s</loc></url>\n" % (SITE, p))
        f.write("</urlset>\n")

if __name__ == "__main__":
    main()
