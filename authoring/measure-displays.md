# Finding displays that overflow the text column

The harness lives in the repo at `tools/_measure.html`. Copy it into the built site and drive
it headless: it renders every display formula of every section into a 39rem column (the
book's text width) and lists the ones that stick out, as
`percent<TAB>page<TAB>first characters of the formula`, widest first.

```bash
cd /home/akizumi/coding/linear-algebra
./build.py html
cp tools/_measure.html _build/html/_measure.html
(python3 -m http.server 8772 --directory _build/html >/dev/null 2>&1 &)
S=<your scratchpad>
timeout 300 google-chrome --headless=new --disable-gpu --no-sandbox --user-data-dir=$S/measure \
  --virtual-time-budget=120000 --dump-dom "http://localhost:8772/_measure.html" 2>/dev/null \
  | python3 -c "
import sys, re, html
m = re.search(r'<pre id=\"out\">(.*?)</pre>', sys.stdin.read(), re.S)
print(html.unescape(m.group(1)).strip() if m else '(no output)')"
```

**Measure `mjx-math`, not `mjx-container`.** The container is a block with `max-width: 100%`
and `overflow-x: auto`, so it always reports exactly the column width and a naive measurement
says every formula fits. The typeset mathematics inside it is what sticks out and what the
reader has to scroll. A harness that reports "none" for the whole book is measuring the wrong
box; sanity-check it against a formula you can see overflowing.

A formula over 100% overflows at all; at 110% and above it is clearly scrolling and should be
broken with `aligned`, `split` or `cases` (a `\tag` goes after `\end{aligned}`, never inside).

To measure a phone-width column instead, change `#stage { width: 39rem }` to 20rem.
