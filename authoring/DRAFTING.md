# Drafting brief (shared by all section-drafting agents)

You are drafting sections of a comprehensive, reader-caring linear algebra textbook (Pandoc Markdown → static site + PDF) in /home/akizumi/coding/linear-algebra.

## Read before writing
1. `authoring/STYLE.md` — the writing standard. Follow it exactly (explain template, Idea/Proof registers, Quick checks, warnings, A/B/C exercises with complete solutions, syntax).
2. `authoring/NOTATION.md` — fixed notation; `latex/macros.tex` for available macros.
3. The chapter blueprint `authoring/blueprints/chNN.md` — your sections' entries are the spec (content, labels to keep, labels to create, proof routes, examples, exercises) and the "Cross-section label use" list.
4. The kwok-proof skill: `/home/akizumi/coding/kw/skill/kwok-proof/SKILL.md` (sections "How he thinks", "Typeset register", "Board register"), `references/explaining.md` (§1–§8), `references/written-solutions.md` (§1–§3 + two exemplars), `references/problem-setting.md` (§1–§4), and the subject reference (`references/la1.md` or `la2.md`) §1 heuristics and the exemplars nearest your topic. Never name or quote the person behind the skill in the book.
5. The earlier chapters' label lists: `grep -rho "{#[a-z]*-[^} ]*" src/ch0N-*/` for each earlier chapter, and read the specific earlier results you cite so your recall of them is accurate.
6. Old versions of your files (if any) to preserve labels.

## Rules
- Original prose only. Do not copy from any textbook. The reference PDFs in `linear-algebra-textbook/` may be consulted only to check that a statement is true / coverage is complete — never paraphrase their text, examples or exercises.
- Keep every display inside the text column: a formula wider than about 60 characters of ordinary math is broken with `aligned` or `cases` (a `\tag` goes after `\end{aligned}`, never inside).
- Section length ~2,500–5,000 prose words (math spans count as one word); complete: opening frame, notions per the explain template, theorems with lead-in / Idea / Proof / aftermath, ≥1 `::: {.check}` followed (not nested) by a `::: {.solution}` block, ≥1 `::: {.warning}`, `## Exercises` with `### A. Check your understanding` / `### B. Practice` / `### C. Going deeper`, each exercise `::: {#exr-<section-slug>-a1}` titled `[A1]` followed by a complete `::: {.solution}`.
- Math: `\( \)` and `\[ \]` only. Relation symbols are typeset, never unicode characters: proof-direction tags are `\( (\Rightarrow) \)`, `\( (\Leftarrow) \)`, `\( (\subseteq) \)`, `\( (\supseteq) \)`, and a chain reads `(a) \( \Rightarrow \) (b)`. Matrices are bold (`\A`, `\B`), vectors bold lowercase (`\v`), operators and spaces plain italic. Pandoc fenced divs must be closed, blank lines around them.
- Labels globally unique: grep `src/` before creating one. Keep every "keep label" exactly.
- `@label` refs only to earlier material (earlier chapters, earlier sections of this chapter per the blueprint, or earlier in your file). Forward pointers in prose say "in Chapter N" without @ref.
- Verify every non-trivial computation with sympy (`python3 -c 'import sympy'` works with the default python3). Never mention sympy, Python or "verified by computer" in the book text itself (runnable `{.python .run}` cells are the only exception).
- American spelling. Add genuine new words to `spelling.txt` (append only).
- Do not delete or rename files other than those assigned; do not edit other sections, config, or `authoring/STATUS.md` (report forward promises instead).

## When done
Run `./build.py html 2>&1 | grep -i "warn\|error" | head -30` and fix warnings originating in YOUR files (other agents build concurrently; ignore issues from files that aren't yours, and duplicate-label warnings against old content that the blueprint moves elsewhere). Reply with: files written, prose word counts, labels created, blueprint deviations and why, forward promises made (for STATUS.md), claims you were unsure about.

## Building while other agents work

Several drafting agents run at once, and **the scratchpad directory is shared between all of them**. Never build in the shared source tree (concurrent builds corrupt `_build/cache`), and never build in a generically named scratch folder such as `scratchpad/repo/`: in Chapter 18 two agents used the same one and one `rsync --delete`d the other's copy. Copy the repo into a directory named after your own sections, for example `scratchpad/ch17-s05-s07/repo/`, and build there.
