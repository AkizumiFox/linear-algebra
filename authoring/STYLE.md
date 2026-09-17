# Writing standard for the book

This file is for anyone who writes a section: me, or a drafting agent. Read all of it before you write. Also read `authoring/NOTATION.md` and the chapter's blueprint in `authoring/blueprints/`.

The method comes from the kwok-proof skill (`/home/akizumi/coding/kw/skill/kwok-proof/`). Read these parts of it before your first section:

- `SKILL.md`: the sections "How he thinks", "Typeset register" and "Board register".
- `references/explaining.md`: §1–§7, and the exemplar in §8 closest to your topic.
- `references/written-solutions.md`: §1–§3 and two exemplars.
- `references/la1.md` or `references/la2.md`: §1 heuristics, for proof routes in the topics they cover.
- `references/problem-setting.md`: §1–§4, for the exercises.

**Hard rules**
- **Nobody is named.** The book never names, quotes or alludes to the lecturer the skill was distilled from. It uses his method silently. Never write "as X would say", course weeks or theorem numbers from his notes.
- **No copying.** The reference PDFs in `linear-algebra-textbook/` are copyrighted. You may use them to check which topics exist and whether a statement is true. Do not paraphrase their prose or copy their examples or exercises. Standard theorems are common property, but the explanation, the examples and the exercises must be our own.
- **No forward references in proofs.** A proof may cite only results that appear **earlier** in the book: an earlier section, or earlier in the same section. The blueprint lists what each section may use. A forward pointer in the prose ("we will prove in Chapter 9 that …") is fine. It must never be a step in an argument.
- **Every claim is true.** Check every computation, and state every hypothesis (field, finite dimension, char ≠ 2, …). If you are unsure, compute it (sympy) or leave a `TODO(verify)` comment. Never guess.

---

## 1. The reader

The reader is a motivated student working **alone**. They have no lecture to fill gaps and no one to ask. Care for them:

- **Say why before what.** Explain what problem a definition or theorem solves before stating it.
- **Recall before use.** When an earlier result is used, recall it in a clause, name it, and link it with `@label`.
- **Warn early.** Name a known trap *before* the reader can fall into it, with a concrete failing case.
- **Let the reader check themselves.** Put a Quick check with a folded answer in every section.
- **Show every move.** Where a move is not visible ("why this basis?"), give one clause of reason. The written proof stays minimal and forward; the Idea block carries the discovery.
- **Stay calm.** No hype and no "clearly" or "obviously" hiding a step. "Trivially" is allowed only for something that really is one line and is then written out.
- **One new notion at a time.** Use at most two new **major** notions per section. Minor definitions (notation, auxiliary terms) may exceed this when they are introduced just before their first use; if a section carries more than two major notions, the blueprint splits it.

## 2. Page skeleton

Each section is one Markdown file, `src/chNN-slug/MM-slug.md`, whose first line is `# Title`.

```markdown
# Title of the Section

Opening frame: 2–4 sentences. Where we are, what question is open, what this section
does. Plain prose, no heading.

## First subsection heading

...notion or theorem blocks...

## Exercises

### A. Check your understanding
### B. Practice
### C. Going deeper
```

Use `##` for subsections (they appear in the page's table of contents) and `###` only inside Exercises or for a long worked computation. Aim for **2,500–5,000 words**. Split a longer section at a natural seam.

A chapter's `index.md` contains, in this order:
1. `# Chapter Title`.
2. A 1–2 paragraph story of the chapter: the question it answers and why the reader should care.
3. **What you need:** the earlier chapters or sections used, with links.
4. **Roadmap:** a bullet per section, with one sentence each.
5. **Named moves:** a short list of the proof techniques this chapter introduces, so the reader can transfer them.

## 3. Introducing a notion (the explain template)

For each new definition, in order:

1. **Situate** (1–2 sentences). Where does it sit? Objects then maps, an object then its subobjects, or a question left open.
2. **Hook.** Choose **one**:
   - a naive notion that fails, shown failing;
   - a recurring expression that deserves a name;
   - the standard example, generalised;
   - a goal theorem stated first ("we want to prove …; we need a word for …");
   - an everyday word.
3. **Slogan.** One sentence in plain words, written in *italics* as its own paragraph.
4. **Definition.**
   - Every quantifier, the field, and what it is defined on.
   - **Bold** the term defined and the small words that carry weight: **not all zero**, **for every**, **strictly**, **a** vs **the**, **over F**, **non-zero**.
5. **Paraphrase** clause by clause ("In words: the first condition says …").
6. **Well-definedness**, if there is anything to check: independence of choices, existence, uniqueness.
7. **Examples**, 2–4 of them, simplest first.
   - Check each against the definition clause by clause.
   - Spread them across the families: Fⁿ, F[x], function spaces, matrices.
   - Include one degenerate case ({0}, the empty set, the identity, 1×1) and say why it matters.
8. **Non-example by minimal change.** Change one example slightly, say what still works, and name the exact clause that fails.
9. **Why this definition.** What breaks if a clause is dropped or a convention changed. Where the name comes from, if it helps.
10. **Warning** (`::: {.warning}`). The misconception, with a concrete failing case.
11. **Payoff.** The first small result, a link to an earlier concept, and one sentence on where this is going.

Not every notion needs every step at full size. A minor auxiliary definition may use steps 4, 7 and 8 only. **Major notions get all eleven.** These include: vector space, subspace, span, independence, basis, dimension, linear map, kernel/image, isomorphism, matrix of a map, determinant, eigenvalue, minimal polynomial, generalized eigenspace, inner product, adjoint, normal operator, positive operator, SVD, bilinear form, tensor product, norm, and similar.

## 4. Theorems and proofs

For each theorem:

1. **Lead-in sentence.** Say what the result does or what need it fills ("It turns out that distinct eigenvalues force independence:").
2. **The statement**, complete and self-contained, with all hypotheses. Give it a short `[Name]` title when it has a standard name or will be cited later.
3. **Idea** (`::: {.idea}`, 2–6 lines, plain prose).
   - The reasoning found backwards, a picture described in words (or TikZ), a small case, or a numbered plan ① ② ③.
   - This is where "why do we do this?" is answered.
   - Omit it for proofs of 3 lines or fewer.
4. **Proof** (`::: {.proof}`), in the typeset register:
   - **First sentence does mathematics:** "Let …", "Suppose …", "Since …", "By @thm-x, …". Never motivation (that went in the Idea).
   - **Chain the steps** with Therefore / Hence / Thus / In particular / Then.
   - **Every step names its reason**: a hypothesis, a definition, or a cited result (`@label`, not restated). Where a display hides a reason, add "where the second equality uses …".
   - **Always justify:**
     - each axiom or subspace check;
     - why a choice is possible;
     - "linearly independent with dim V elements, hence a basis", written out;
     - non-zero before dividing;
     - commuting before swapping;
     - invertible before cancelling.
   - **You may skip:** a symmetric half ("swapping the roles of U and W gives the reverse inclusion"), and a repeat of an argument just given.
   - **Labels:** (⇒)/(⇐), (⊆)/(⊇), *Case 1.*/*Case 2.*, and `::: {.claim}` with a nested `::: {.proof}` for a genuinely separate fact inside a long proof.
   - **Ending:** "This shows …" / "This proves …" / "as claimed".
   - **Length:** most proofs are 5–20 lines. For a long theorem (Steinitz, Jordan form, spectral theorem, Perron–Frobenius, Courant–Fischer, Loewner), write a **Step roadmap** in the Idea, then `**Step 1.**` … inside the proof, with Claims.
   - **One proof per theorem.** A second route gets at most one short "Alternatively," paragraph, and only when it teaches something.
5. **Aftermath** (1–2 sentences). What is this result for? What does it let us do now? Use a `::: {.remark}` only if it needs a separate block, e.g. "the converse fails: …".

**Preferred proof routes.** Use whichever fits. When a brute-force route exists, it is fine to say in the Idea that it is legitimate but messy, then take the structural one.

- **Givens and goal first.** Unwind the definitions; the definition tells you what to fix arbitrarily.
- **Plug in a theorem.** If a big structure theorem applies (spectral, Jordan, SVD), its conclusion is the first real line.
- **Find the job of each hypothesis.** An unused hypothesis is where the finish comes from.
- **Count instead of check.** Rank–Nullity; "independent + right size ⇒ basis"; one inclusion + equal dimension ⇒ equality.
- **Dimension formulas.** Take a basis of the smallest space, extend it (Basis Extension), make a Big Claim that the combined list is a basis (spanning, then independence), and count.
- **Independence template.** "Let a₁v₁ + ⋯ + a_kv_k = 0." Move a block across, name the common vector, and ask which subspaces it lies in.
- **Injectivity via the kernel.** Surjectivity via rank or dimension.
- **Abstract space → write down a matrix** in a well-chosen basis. Draw the change-of-basis square.
- **Contradiction for "cannot", "unique", "at most".** Negate carefully, quantifier by quantifier.
- **Induction:** say "induction on what", then find the smaller object inside.
- **Polynomial identities in A** → an annihilating polynomial → m_A divides it.
- **Inner products:**
  - to show a vector is 0, pair it with itself;
  - to move T across, use T\*;
  - compute ⟨Tv, v⟩ two ways;
  - work with the norm squared;
  - fix an orthonormal basis to make things concrete.
- **Hermitian case before normal.** Real-symmetric picture before complex.
- **A limiting auxiliary matrix** (A + tI, t → 0⁺) to pass from invertible to general.
- **Dominant coordinate + triangle inequality** (Gershgorin-type bounds).
- **Refute with one small witness** and name what fails.

## 5. Examples, checks, warnings, remarks

- **Examples** `::: {#exm-slug}` with a `[Title]` first line. State the question inside the example. Put the worked answer in a following `::: {.solution}`; it starts folded on the web. Use integer data chosen so the computation is clean (characteristic polynomials that factor, pivots that are ±1 or small).
- **Quick check** `::: {.check}`: one short question, with its answer in a nested `::: {.solution}`. Put at least one per section, placed right after the idea it tests. Good checks:
  - a non-example failing only clause k;
  - "why must this be strict?";
  - "is this look-alike an example?";
  - a tiny computation.
- **Warning** `::: {.warning}`: one misconception, a concrete failing case, 1–4 sentences.
- **Remark** `::: {.remark}`: 1–3 sentences with one job (converse fails, other names or notations, in other words, outlook).
- **Pictures:** TikZ inside `\begin{center}\begin{tikzpicture}…\end{tikzpicture}\end{center}` in a raw LaTeX block, or with the tikz syntax already used in `src/`. Use one idea per figure. Colour must never be the only carrier of meaning.
- **Interactive:** `::: {.plot fn= x= y= params=}` for functions with sliders, `{.python .run}` for small numpy/sympy experiments, and `::: {.widget src=}` with a `::: {.print}` fallback. Use them sparingly and only where exploring helps (2×2 maps, eigenvectors, projections, power iteration).

## 6. Exercises

Each section ends with `## Exercises` and three groups.

**A. Check your understanding.** Exactly one exercise with 2–6 lettered parts: define, state, decide true/false with a reason, name the method. Readers should be able to answer before moving on.

**B. Practice.** 2–4 exercises "like the examples", each with a worked example type in the section:
- A "Determine which of the following … Justify your answer." batch with one or two planted failures.
- An integer-data computation ending in "Hence …".
- A routine proof applying one theorem once.

**C. Going deeper.** 1–4 exercises:
- a (a) Prove / (b) Deduce pair;
- a counterexample, construction or change-of-field item ("Is this still true over 𝔽₂?");
- optionally one harder problem, made reachable with scaffolded parts and a hint.

**Format.** Every exercise is `::: {#exr-<section-slug>-a1}` (then `-b1`, `-b2`, `-c1`, …) whose first line is a title `[A1]`, `[B2: Short name]`, etc. It is followed by a `::: {.solution}` written in the typeset register (complete, not a sketch).

**Parts** use a lettered list:

```markdown
::: {.enumerate options="label=(\alph*)"}
1. ...
2. ...
:::
```

**Wording:** "Prove that", "Determine whether … Justify your answer.", "Give an example of …", "Explain why … is **not** …", "Hence deduce …".

**Hints** go at the end in italics: *Hint: consider the kernel of …*. A hint names a tool or an object, never a step.

**Calibration:**
- B uses one theorem once.
- C combines two ideas, generalises to n, or changes the field.
- A harder C item uses three ingredients, one from an earlier chapter.
- A later exercise may cite an earlier one ("By @exr-span-b2 …").

## 7. Prose

- **Voice.** "We" for the author and reader together; "you" sparingly, for direct advice. Median sentence 12–18 words. Paragraphs of 1–4 sentences. Vary rhythm; no walls of text.
- **Emphasis.** Bold is for defined terms and load-bearing small words, italics for slogans and light emphasis. No exclamation marks, and no "Note that" at the start of every other sentence.
- **Names.** Name results by content ("the Rank–Nullity Theorem"), with `@label`. Titles of named theorems match exactly so the dependency graph picks up mentions.
- **Promises.** Every forward promise ("we will see in @sec…" or "in Chapter 8") must be paid off. When writing, add each promise to `authoring/STATUS.md`.
- **Spelling.** American spelling: "normalize", "color", "behavior", "center". Mathematical names keep their accents (Gershgorin, Schur, Cauchy–Schwarz with an en dash).
- **Math delimiters.** `\( … \)` inline and `\[ … \]` display, never `$`. Numbered equations take `{#eq-slug}` right after `\]`.
- **Macros** are in `latex/macros.tex`; use those listed in `NOTATION.md`. Define nothing ad hoc. If a new macro is needed, add it to `macros.tex` and `NOTATION.md`.

## 8. Authoring syntax reference

```markdown
::: {#thm-rank-nullity}
[Rank–Nullity Theorem]

Let \( V \) be a finite-dimensional vector space ...
:::

::: {.idea}
We want ...
:::

::: {.proof}
Let ...  This proves the theorem.
:::
```

- **Environment prefixes:** `thm`, `lem`, `cor`, `prp` (shared counter); `def`; `exm`; `exr`; `cnj`. Small blocks with no label: `.proof`, `.solution`, `.remark`, `.claim`, `.idea`, `.warning`, `.check`, `.algorithm`.
- **Labels** are lowercase-hyphenated and describe content (`thm-steinitz-exchange`, not `thm-3`). They are global across the book and must be unique.
- **References:** `@thm-rank-nullity` renders as "Theorem 3.12" with a hover preview; `@eq-slug` works for equations.
- **Labeled lists:** `::: {.enumerate options="label=(VS\arabic*)"}` wraps an ordered list.
- **Web-only content:** `::: {.content-visible when-format="html"}`.

## 9. Before handing a section back

- [ ] Every definition is preceded by its need. Major notions follow §3 in full.
- [ ] Every proof cites only earlier results, and every step names its reason.
- [ ] Every example's arithmetic is verified (sympy for anything with more than two steps).
- [ ] There is at least one Quick check, one warning and one non-example. The exercises have A, B and C groups, each exercise with a complete solution.
- [ ] Every B-type task has a worked example in the text.
- [ ] Notation matches `NOTATION.md`. No symbol is used before it is introduced, and none is reused with a new meaning.
- [ ] Labels are unique (grep `src/`), and every `@ref` target exists or is created in this chapter.
- [ ] No copied text or examples from the references, and no attribution to any person.
