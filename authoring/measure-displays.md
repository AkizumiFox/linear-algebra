# Finding displays that overflow the text column

The built pages are served locally; the helper page `_build/html/_measure.html` renders each
section into a 39rem column (the book's text width) and lists every display formula wider
than that column, as `percent<TAB>page<TAB>first characters of the formula`.

Run it with the site built and a server on port 8772:

```bash
cd /home/akizumi/coding/linear-algebra
./build.py html
(python3 -m http.server 8772 --directory _build/html >/dev/null 2>&1 &)
S=/tmp/claude-1000/-home-akizumi-coding-linear-algebra/a94af3e4-997a-4bae-952a-80d79d82cd90/scratchpad
timeout 300 google-chrome --headless=new --disable-gpu --user-data-dir=$S/measure \
  --virtual-time-budget=120000 --dump-dom "http://localhost:8772/_measure.html" 2>/dev/null \
  | python3 -c "
import sys, re, html
m = re.search(r'<pre id=\"out\">(.*?)</pre>', sys.stdin.read(), re.S)
print(html.unescape(m.group(1)).strip() if m else '(no output)')"
```

To measure a phone-width column instead, edit `#stage{width:39rem}` in `_measure.html`
(20rem is a reasonable phone target) before running, and put it back afterwards.
