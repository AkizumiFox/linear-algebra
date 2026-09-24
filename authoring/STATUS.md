# Book status

The plan is at `~/.claude/plans/cached-gathering-sedgewick.md`. The outline of all chapters is in §1 of the plan.

## Chapters

| Ch | Dir | Topic | State |
|---|---|---|---|
| 0 | ch00-foundations | Preliminaries | deployed |
| 1 | ch01-vector-spaces | Vector spaces | deployed |
| 2 | ch02-linear-maps | Linear maps | deployed |
| 3 | ch03-linear-systems | Linear systems | deployed |
| 4 | ch04-matrices-of-maps | Matrices of maps | deployed |
| 5 | ch05-duality | Duality | deployed |
| 6 | ch06-polynomials | Polynomials | deployed |
| 7 | ch07-determinants | Determinants | deployed |
| 8 | ch08-block-matrices | Block matrices | deployed |
| 9 | ch09-eigenvalues | Eigenvalues and diagonalization | deployed |
| 10 | ch10-canonical-forms | Canonical forms | deployed |
| 11 | ch11-inner-products | Inner product spaces | deployed |
| 12 | ch12-spectral-theory | Spectral theory | deployed |
| 13 | ch13-psd-and-svd | Positive matrices and the SVD | deployed |
| 14 | ch14-forms | Bilinear and quadratic forms | deployed |
| 15 | ch15-tensors | Tensors and exterior algebra | deployed |
| 16 | ch16-norms | Norms and matrix analysis | deployed |
| 17 | ch17-variational | Variational principles and interlacing | deployed |
| 18 | ch18-convexity | Convexity | deployed |
| 19 | ch19-nonnegative | Non-negative matrices | deployed |
| 20 | ch20-perturbation | Perturbation theory | deployed |
| 21 | ch21-inequalities | Matrix inequalities | deployed |
| 22 | ch22-geometry | Affine and projective geometry | deployed |
| 23 | ch23-algebras | Algebras and representations | deployed |
| 24 | ch24-applied | Computation and applications | deployed |

## Open forward promises

Add a line when a section promises something later ("proved in Chapter 6"); tick it when it is paid off.

- [x] Ch 0 → Ch 6: Fundamental Theorem of Algebra proved
- [x] Ch 0 → Ch 3 §07 (`lem-root-bound`): a polynomial over an infinite field is determined by its values
- [x] Ch 0 → Ch 6: division algorithm in general
- [x] Ch 0 → Ch 3 (`thm-one-sided-inverse`): for square matrices AB = I implies BA = I (Ch 0 text may say Chapter 2: fix to Chapter 3)
- [x] Ch 0 → Ch 3: A invertible ⇔ Ax = 0 only trivial solution
- [x] Ch 0 → Ch 1: independence/"not all zero"; {0} subspace, ∅ not; intersection vs union of subspaces; span as intersection; Fⁿ as a vector space
- [x] Ch 0 → Ch 2: kernel test for injectivity
- [x] Ch 0 → Ch 4: quotient vector spaces; similarity
- [x] Ch 0 → Ch 6: unique prime factorization in F[x] (Ch 0 mentions uniqueness for integers without proof)
- [x] Ch 0 → Ch 7: sign of a permutation
- [x] Ch 0 → Ch 14: char ≠ 2 in forms
- [x] Ch 0 (09-matrices) → Ch 3: every elementary row operation is left multiplication by an invertible matrix; row equivalence = reachable by row operations
- [x] Ch 0 (09-matrices) → Ch 4: similar matrices represent the same linear map in different bases; matrix of a composition is the product
- [x] Ch 0 (09-matrices) → Ch 7: ad − bc is the determinant of a 2×2 matrix; det is a homomorphism GL_n(F) → F \ {0} (10-groups)
- [x] Ch 0 (10-groups) → Ch 7: parity of the number of transpositions is well defined (sign homomorphism)

## Notation added beyond NOTATION.md

(none yet)
- [x] Ch 1 → Ch 2: Rank–Nullity by the same "basis, extend, Big Claim, count" move
- [x] Ch 1 → Ch 4: external direct sums; projection onto U along W (different complements, different projections)
- [x] Ch 1 → Ch 9: eigenspaces of a diagonalizable operator give a direct sum
- [x] Ch 1 → Ch 2: coordinate map is an isomorphism; shift map injective not surjective; (ℝⁿ)_ℂ ≅ ℂⁿ
- [~] Ch 1 → Ch 9/12: complexification gives real matrices complex eigenvalues (Ch 9 half paid); used in real spectral theory (Ch 12)
- [x] Ch 3 → Ch 7, 9, 13 (and Ch 2 before it): invertible-matrix TFAE grows (kernel/image; det; eigenvalues; singular values)
- [x] Ch 2 ← Ch 3: Rank–Nullity for linear maps (the reorder inverted this: maps now come first and Ch 3 refers back)
- [x] Ch 3 §06 → Ch 13 §02: Cholesky, derived from `thm-ldlt` by absorbing the square root of the diagonal
- [x] Ch 3 → Ch 24: partial pivoting, rounding (§02); graph Laplacian (§11)
- [x] Ch 3 → Ch 6: Lagrange interpolation formula
- [x] Ch 3 → Ch 11: least squares

## Deferred to the whole-book pass (M7)

- Proof endings: STYLE asks every proof to close with "This shows …"/"as claimed". Observance is uneven — Ch 9 has 9 closers for 52 proofs, Ch 10 has 20 for 57, Ch 11 has 24 for 56. Make it consistent book-wide rather than chapter by chapter.
- [x] **Formula widths, web: clean, displays and inline.** At the 39rem text column the harness reports `none (6587 displays measured on 263 pages)` and, in its new inline mode (`tools/_measure.html?mode=inline`), `none (164629 inline formulas measured on 263 pages)` — the 215 over-width displays this line used to record are all gone, and the 18 over-width inline formulas the first inline pass found (Chapters 2–23, 101%–161%) are broken or shortened. Inline maths had never been measured before. Re-measure in both modes with `tools/_measure.html` (see `authoring/measure-displays.md`) after any bulk edit.
- [ ] **Display widths, print: not clean, and never was measured before.** The book PDF’s LaTeX log carries **845 overfull hboxes over 364 of its 3308 pages**, worst 81pt. This is a different measurement from the web one — a different column width and it counts prose lines as well as displays — and it is pre-existing, not caused by M7. The notation page contributes zero. Attribute them with a scan of `_build/tmp/latex-book/book.log` that tracks the `[N` page markers
- [x] `thm-trace-properties` (Ch 0 §09) numbers its parts 1, 2, 3 with a bare list while almost every other multi-part theorem uses `label=(\alph*)`. **M7 closed the drift**: twelve citations had gone lettered (seven "(c)" and three "(a)" for this theorem, two "(d)" for `thm-transpose-properties`) and all now use the numeric style; a re-scan checked 3330 part references across the book and found 0 out of range and 0 style mismatches. Converting the theorem itself would now cost 41 citation edits and is **not** recommended

- Long sections to consider splitting or trimming: Ch 0 §04 functions, §05 relations, §09 matrices; Ch 1 §01–§04; Ch 3 §02 Gaussian elimination (~11.7k raw words), §05 rank.
- Ch 3 §03: "pivot columns of A" is defined inside `cor-pivot-columns-well-defined`; consider a separate def block.
- Ch 3 §05 symbol reuse (r, **r**ᵢ, **b**) — tidy in M7.
- Ch 2 §01 and §04 both define "operator" and the shorthand Tv; §04 should defer to §01 (check at Ch 2 referee).
- Ch 2 §04 C1(b) and Ch 4 §01 both prove 'every linear map Fⁿ → Fᵐ is T_A' — consolidate into one result in M7. Ch 4 §01 is long; its rank/invertibility subsection could move to Ch 4 §03.
- Ch 4 §04 long (~11k raw): consider splitting products/cosets from isomorphism theorems. §08 Sylvester proof duplicates exr-rank-nullity-c1.
- [x] Ch 5 → Ch 6: Lagrange interpolation formula; evaluation functionals dual to Lagrange basis
- [x] Ch 5 → Ch 11: orthogonal complement vs annihilator; inner product gives chosen V ≅ V*; adjoint T*
- Ch 5: ε_{ij} vs ε_c overload; zero functional notation — tidy in M7.
- Ch 5: restriction map V* → U* named R (§02), ρ (§05), ι′ (§04) — unify to ρ in M7. §06 extra early Quick check.
- [x] Ch 6 → Ch 9: minimal polynomial = monic generator of I_T (`thm-annihilator-ideal`); invariant subspaces defined; Cayley–Hamilton; primary decomposition via `thm-kernel-splitting` and `exr-polynomials-of-operators-c2`
- [x] Ch 6 → Ch 10: canonical forms from primary decomposition
- [x] Ch 6 → Ch 9: diagonalizable ⇔ minimal polynomial splits with distinct roots; every complex operator has an eigenvalue (FTA)
- Ch 7 §03: disjoint cycle decomposition only asserted (Ch 0 shows by example) — consider a short proof in M7.
- [x] Ch 7 → Ch 9: (xI − A)·adj(xI − A) = det(xI − A)·I reappears (Cayley–Hamilton route)
- [x] Ch 7 → Ch 8: Schur complements cite `thm-det-block-triangular`
- [x] Ch 7 → Ch 9: eigenvalues from `thm-charpoly-root-iff-singular`; Cayley–Hamilton; p_AB = p_BA in general
- [x] Ch 7 → Ch 10: complete similarity invariants
- [x] Ch 7 → Ch 11/13: Gram matrices, √det(AᵀA) area via inner products
- [x] Ch 7 → Ch 12: circulants of every size
- [x] Ch 7 → Ch 24: matrix-tree theorem (§11 `thm-matrix-tree`, proved in full; Ch 7's pieces are in an exercise, so §11 reproves them and credits it)
- [x] Ch 8 → Ch 12: AX − XB = C uniquely solvable ⇔ no common eigenvalue (over ℂ); Ch 20 quantitative form (`prp-sep-properties` (d))
- [x] Ch 8 → Ch 15: tensor product of maps has matrix A ⊗ B
- [x] Ch 8 → Ch 9: tr C^k = 0 for all k ⇒ nilpotent, via eigenvalues (over ℂ and its subfields)
- [x] Ch 8 → Ch 9: p_T = p_{T|U} · p_{T̄} for T mapping U into U
- [x] Ch 8 → Ch 13: positive definiteness via Schur complements
- [x] Ch 8 → Ch 24: Gaussian elimination as repeated Schur complements (§02 `thm-elimination-is-schur-complements`)
- [x] Ch 9 → Ch 10: recurrences with repeated roots (k^jλ^k) via the Jordan form; generalized eigenspaces named; cyclic vector when deg m = dim V; m and p together do not decide similarity
- [x] Ch 9 → Ch 12: Schur's orthonormal triangularization
- [x] Ch 9 → Ch 19: Perron–Frobenius gives the Markov limit for regular stochastic matrices
- [x] Ch 4/7/9 → Ch 10: similarity decided; complete invariants (split case); generalized eigenspaces named; best matrix when g < a
- [x] Ch 10 → Ch 10 §06: canonical form over every field (rational form); §07 removes the splitting hypothesis from A ~ Aᵀ
- [x] Ch 10 → Ch 20: numerical instability of the Jordan form (§03's `exm-jordan-root-perturbation`, §04's `thm-bauer-fike-defective`, §11's remark)
- [x] Ch 4 → Ch 10: A ~ Aᵀ over any field (`cor-a-similar-to-transpose`)
- [x] Ch 9 §11 → Ch 10: Markov powers without diagonalizability (`cor-markov-powers-converge`)
- [x] Ch 10 → Ch 16: norms give quantitative bounds for e^A and for powers; ρ(A) ≤ ‖A‖ and the spectral radius as a limit
- Ch 10 §07 is long (~10k raw); natural seam after the Smith theorem. Ch 10 §04, §06 also long. Consider in M7.

### Chapter 11 (inner product spaces)

- [x] Ch 7 §07 → Ch 11: Gram determinants (`cor-gram-determinant-nonnegative` becomes `thm-gram-matrix-properties`, §02)
- [x] Ch 5 → Ch 11 §05: the inner product is the data that picks an isomorphism V ≅ V\*; Ch 5's basis map Θ_𝓑 is the Riesz map of the inner product making 𝓑 orthonormal. (Ch 5's warning carries no label, so §05 cites `cor-dimension-dual-space` and `thm-evaluation-natural`; give that warning a label if a hard link is ever wanted.)
- [x] Ch 5 → Ch 11 §05: annihilator U⁰ corresponds to U^⊥ (`thm-annihilator-vs-orthogonal-complement`)
- [x] Ch 11 §03/§04/§05 → Ch 11 §06: P_U is self-adjoint; ker(T\*T) = ker T; (nul A)^⊥ = col(A\*) as the four-subspaces theorem; the dual map read through Riesz is the adjoint
- [x] Ch 3 §07 → Ch 11 §04: the low-degree approximate fit promised where interpolation follows the noise (`exm-least-squares-line`, `exm-least-squares-quadratic`). Chapter 3 itself states no orthogonality, so §06's four subspaces extend Ch 3 rather than discharging a promise.
- [x] Ch 11 §01 → Ch 16: general norms; not every norm comes from an inner product, the parallelogram law is the test
- [x] Ch 11 §02/§08 → Ch 24: §03 gives the rates (classical loses orthogonality like uκ², modified like uκ — **stated with credit, not proved**, and demonstrated by simulation), and proves the one-reflection backward error
- [x] Ch 11 §04 → Ch 13: the pseudoinverse A⁺ packages the least-squares and minimum-norm answers (note: §04 writes the minimum-norm solution x_min; Ch 13 may prefer A⁺b — rename then if so)
- [x] Ch 11 §05 → Hilbert spaces: representability needs completeness and continuity. **Not a debt** — §05 states this as the boundary of the finite-dimensional theorem, names no chapter and promises nothing. Ticked to take it off the open list, not because anything paid it
- [x] Ch 11 §06 → Ch 12: all spectral theory of self-adjoint and normal operators
- [x] Ch 11 §02 → Ch 12: what an inner product adds once an operator is also given

### Chapter 12 (spectral theory)

- [x] Ch 12 §01 → Ch 16: norms and limits for matrices, making the "diagonalizable, then take a limit" argument precise
- [x] Ch 12 §02 → Ch 13: positive operators (`exr-self-adjoint-operators-c1` proves half the characterization)
- [x] Ch 12 §02 → Ch 17: the Rayleigh quotient and Courant–Fischer, the optimization route to eigenvalues of a self-adjoint operator
- [x] Ch 8 §04 → Ch 12 §10: the Sylvester equation is uniquely solvable exactly when the spectra are disjoint (Ch 8 states the promise at the end of the Kronecker section)
- [x] Ch 12 §08 → Ch 13: positive operators — paid by `thm-psd-square-root`, `thm-polar-decomposition` and `thm-svd`, which are exactly what the square root built in §08 was for
- [ ] **Still open:** Ch 12 §10 → Ch 13, positive definite solutions of the Lyapunov equation. Chapter 13 never mentions Lyapunov — the word does not occur anywhere in `src/ch13-psd-and-svd/`. The promise is real and nothing pays it. **Ch 12 §10’s wording is not to be changed** (that edit was proposed and declined), so this is paid by adding the result to Chapter 13 or not at all
- [x] Ch 12 §05 → Ch 14: congruence versus similarity, and Sylvester's law of inertia (promised twice in §05)
- [x] Ch 12 §11 → Ch 20: Bauer–Fike and eigenvalue perturbation (`thm-bauer-fike`; the "κ = 1 exactly in the normal case" half is `cor-bauer-fike-normal` (b), proved with an infimum over diagonalizing X)
- [x] Ch 12 §10 → Ch 16: Lyapunov stability of \( \dot{\x} = \A\x \)
- [x] Ch 12 §10 → Ch 20: conditioning of the Sylvester equation (Ch 20 §07, `def-sep` and `prp-sep-properties`)
- [x] Ch 12 §09 → Ch 24: the FFT (§12), with the exact cost (3/2)n log₂ n − n + 1
- Stated but deliberately not proved in Ch 12, each flagged in the text: Roth's removal rule (§10, route via Ch 10 §07's characteristic-matrix equivalence), the general Fuglede theorem (§07), general Cartan–Dieudonné (§06), and the connectedness of the unitary group (§08). Nothing later depends on any of them.
- `\norm{\A}_F` and its unitary invariance (`lem-frobenius-unitarily-invariant`) live in Ch 11 §07, next to the unitary matrices the invariance is about; §11 recalls both. They were in §11 until the reading-path measurement showed that §11 joined seven of the ten published paths on that lemma alone. Ch 12 §01's exercise C2 re-proves it by hand and says so.

### Chapter 13 (positive matrices and the SVD)

- [x] Ch 12 §02 → Ch 13 §01: positive operators; `exr-self-adjoint-operators-c1` supplies one implication of `thm-psd-characterizations`
- [x] Ch 3 → Ch 2/7/9/13: the invertible-matrix TFAE grows; the Ch 13 instalment is `thm-invertible-tfae-positive`
- [x] Ch 7 §07 → Ch 13 §03: Gram determinants, sharpened to "a Gram matrix is exactly a positive semidefinite matrix"
- [x] Ch 7 §09 → Ch 13 §03: the area of a parallelogram in \( \nR^3 \) as \( \sqrt{\det(\A\tp\A)} \). Ch 7 said "Chapter 11 justifies this"; Chapter 11 never did, and the Ch 7 sentence now points at Chapter 13, which does
- [x] Ch 11 §02 → Ch 13 §03: the converse — a positive semidefinite matrix *is* a Gram matrix, with the list unique up to isometry
- [x] Ch 8 §03 → Ch 13 §06: positive definiteness tested one block at a time by Schur complements
- [x] Ch 11 §04 → Ch 13 §11: the pseudoinverse packages least squares and minimum norm; the notation is settled, \( \x_{\min} = \A^{+}\b \)
- [x] Ch 13 §06 → Ch 13 §11: the semidefinite block criterion with a singular corner (`prp-block-psd-general`). §06 promised it and §11 had not delivered; added by hand
- [x] Ch 13 §01 → Ch 14: congruence studied for its own sake
- [x] Ch 13 §02 → Ch 24: Cholesky's half cost and no pivoting (§02 `prp-lu-cost`, `thm-cholesky-stability`)
- [x] Ch 13 → Ch 16: the operator norm, and \( \norm{\A}_2 = \sigma_1 \)
- [x] Ch 13 → Ch 17: Courant–Fischer, interlacing, eigenvalue monotonicity in the Loewner order
- [x] Ch 13 → Ch 20: perturbation of singular values (Ch 17 §09's spectral bound plus Ch 20 §10's `thm-mirsky-frobenius`; §10 also does the polar factors)
- [x] Ch 13 → Ch 21: operator monotone functions, unitarily invariant norms, Eckart–Young in every unitarily invariant norm (Ch 21 §04 `thm-von-neumann-correspondence`, §06 `cor-eckart-young-ui`, §10 `thm-loewner` and `cor-power-operator-monotone`). *The spectral-norm case moved to Ch 17 §09 and is paid there*
- [x] Ch 13 → Ch 24: PCA (§10). **Partly unpaid, and Ch 13 §10's sentence was reworded to say so:** §10 gives the finite-population model and the reasons for squared error, but the inference from a sample to a larger population needs probability the book does not develop, and **no SVD algorithm is assembled anywhere in the book** — §10 says only why one never forms A*A

### Chapter 14 (bilinear and quadratic forms)

- [x] Ch 0 §07 → Ch 14 §03: "characteristic ≠ 2" earns its keep (`thm-alternating-vs-skew`, with the 𝔽₂ counterexample)
- [x] Ch 12 §05 and Ch 13 §04 → Ch 14 §05: why the signs of a congruent diagonal match the signs of the eigenvalues
- [x] Ch 13 §01 → Ch 14 §02: congruence studied for its own sake, with what it preserves and what it destroys
- [x] Ch 14 §12 → Ch 15: tensor algebras; the construction of Cl(q) as a quotient of one; the independence half of `thm-clifford-dimension`. **Chapter 14 states that theorem with its gap marked in the text**, so this debt is visible to readers
- [x] Ch 14 §09/§10 → nothing: the Pfaffian transformation rule and Sp(2m,F) ⊆ SL are recorded without proof and nothing may cite them
- Polish deferred to M7: Ch 14 §§07–08 have no labelled worked examples (`exm-`), and §10 has no Idea blocks, both against the STYLE checklist

### Chapter 15 (tensors and exterior algebra)

- [x] Ch 8 §04 → Ch 15 §03: the Kronecker product is the matrix of a tensor product of maps, in the dictionary-ordered product basis with the first factor slow. The other ordering gives the *swapped* Kronecker product, not a transpose
- [x] Ch 14 §12 → Ch 15 §10: `Cl(q)` constructed as `T(V)/⟨v ⊗ v − q(v)1⟩`, hence existence, and `dim Cl(q) = 2ⁿ` proved via creation/deletion operators on `Λ V` with no division by 2. The half Chapter 14 marked as missing was independence
- [x] Ch 4 §05 → Ch 15 §04: the trace as a contraction, with no basis chosen
- [x] Ch 15 §08 → Ch 22: Plücker coordinates (Ch 22 §10 `def-plucker-coordinates`, `prp-plucker-well-defined`, `thm-plucker-relation`, with the Klein quadric; Ch 15 §10's version is an exercise, credited and reproved)
- Polish deferred to M7: §10 is the book's longest section (~10.6k words) and carries four major notions against STYLE's two; §03 is also long. Both have natural seams recorded in the referee reports

### Book-wide gates

- **PDF errors now fail the build.** pdflatex runs in nonstopmode and writes a PDF even after an error, and the build used to judge success by the file existing. When the check was tightened (Ch 17 release), **38 of 178 sections** turned out to have been shipping damaged PDFs: 12 `.algorithm` blocks (the environment was never defined for LaTeX), 21 displays with a blank line inside `\[ … \]` (one bulk edit, all `\end{aligned}` / blank / `\]`), 20 display lines beginning like list items, 7 environment titles containing `]` (e.g. `\(F[x]\)`), 4 unmapped Unicode characters, one double superscript. All fixed; the web pages had the same displays as stray `[` `]` text, invisible because MathJax still rendered the loose `aligned`. Guards: `build/pdf.py` fails on any TeX error with an `l.<n>` context (an Overfull-box dump line that starts with `!` is not one); `tests/test_pdf_errors.py`; `tests/test_display_math_source.py` lints `src/` for both display shapes
- `tools/check_forward_deps.py` — fails if any label cites one from a later section. The book passes: 2476 labels, zero forward citations, zero dangling. It compares **sections only**, because the third component of a label number counts within a type (`def-connectives` and `thm-contrapositive-equivalent` are both 0.1.1); 3107 within-section citations therefore go unordered and remain the referee's job. Verified against planted violations
- **The scanner credits proofs by position, and it was wrong in two ways** (fixed in `9e2e712`): a proof after an example went to the example, and a proof under its own heading went to nothing — the proofs of the fundamental theorem of algebra and Cayley–Hamilton were invisible to the gate. Now: proofs skip over examples to the last result, and a separated proof names its result, `::: {.proof of="thm-..."}`; `tests/test_proof_ownership.py` fails on an orphan.
- **M7 triage, 27 sites:** a label followed by *two* proofs before the next label. Most are a theorem with a second proof (then both are correctly credited). But a lemma-with-proof placed between a theorem and its proof credits the theorem's proof to the lemma — Ch 19 §01's Perron was this, fixed by reordering. List with `python3` scan in the Ch 19 session; re-run and read each: ch01 §06 thm-steinitz, §07, §08; ch02 §04, §06; ch03 §03; ch06 §04, §06; ch08 §10; ch09 §07; ch10 §07, §08 (×2); ch11 §05, §07; ch12 §02, §06, §09; ch13 §07, §08; ch16 §02, §04, §07, §08; ch18 §05, §08
- **M7 triage, 44 sites (42 before the scanner fix exposed two more):** `tools/check_forward_deps.py --exercises` lists every theorem, proposition, corollary or lemma that cites an exercise, across 27 files in Chapters 0, 6, 8, 9, 10, 11, 12, 13, 14, 15 and 16. **This is a candidate list, not a defect list.** Citing an exercise for attribution is fine; a proof that *depends* on one is the rule this book has broken and repaired seven times. Each site needs reading. The two Chapter 16 §01 entries were triaged during that chapter's referee pass and are attribution only

### Chapter 22 (affine and projective geometry)

- **Drafted, refereed and revised by a workflow** rather than by hand-launched agents: five section pairs, each flowing draft → referee → revise on its own clock, then an index written against the delivered text, a consistency referee over the seams, and one pass applying its findings. 18 agents, no failures
- The chapter **imports no analysis at all**, and quotes six results it does not prove, each flagged where a reader meets it and listed in the index
- Blueprint corrections the drafters made: `def-face` was already taken by Ch 18 §08 (the polyhedron face here is `def-polyhedron-face`); the affine join formula's second case needed the direction-space count, not the naive one; and the duality correspondence's dimension shift had to be stated in projective dimension throughout
- Pappus over a non-commutative division ring is **stated with credit and not proved** — the book builds neither division rings nor synthetic planes — and nothing depends on it
- `--exercises` lists three Ch 22 sites: **all triaged, attribution only** — §09's remark about the small-field cases, and §10's two credits to Chapter 15's exercise, which §10 reproves rather than uses

### The print edition, rebased on sleek

- **`latex/sleek/` vendors `sleek.sty` and `sleek-theorems.sty`** from `~/coding/packages`, cut to the 17 packages this book uses. That directory is outside the repo and committed nowhere, so referencing it by path would build here and nowhere else. `latex/sleek/README.md` records every change made to upstream, and each removal is also left in the `.sty` as a comment saying what went and why.
- **Removed from the vendored copy, deliberately:** biblatex and biber (no chapter has a bibliography); `\abs`, `\norm`, `\diff` and `\tr`, so `latex/macros.tex` stays the only definition of each. This is not tidiness — sleek declares `\tr` with `\DeclareMathOperator` and `latex-template.sty` already defines it, which is a hard error, and sleek's `\diff` has worse spacing than the book's, so keeping it would have silently reflowed math throughout.
- **`parfill` dropped.** It sets `\parfillskip=30pt plus 1fil`, adding 30pt of unshrinkable glue to the natural width of every single-line paragraph. Measured across five full builds it was the single largest source of overfull lines: 357 with it, 290 without, across the sections. **Do not put it back.**
- **Geometry kept as the book's uniform 2.5cm**, not sleek's `top=3.5cm`. Left and right already agreed, so the measure and every line break are identical either way; sleek's version only costs about 5% more pages.
- **Theorem environments** are now `latex/theorem-envs.sty` (the style, built on sleek's `\mdfdefinestyle{thicc}`) filled by `_build/tmp/environments.tex`, generated from `config.json` by `build/pandoc.py`'s `environments_tex()`. Colours still come from the config. `latex/latex-template.sty` gained a `skipenv` option that skips its own theorem styles and boxes.
- **`\qedsymbol` must stay OUTSIDE the `skipenv` block.** It was inside it, so every proof in the book ended with amsthm's hollow box instead of the filled square — no error, no failed gate, just wrong. Found by the regression port, which hit the same thing. `theorem-envs.sty` calls `\qed` and sets no symbol, so anything `\qed` needs has to live outside that block.
- **The print edition is better set than before, not merely different:** overfull `\hbox` 845 → 773, pages carrying one 364 → 306, worst box 81.4pt → 72.2pt. Pages 3309 → 3326, the extra 17 from restoring the space above a box that follows a heading — without it the title bar landed on the heading's descenders.
- Section numbering did not move (3965 labels, 19408 references) and the HTML edition is unaffected; this changes print only.
- One content fix came with it: an exercise item in Chapter 17 §02 ran off the page clipped mid-formula, and is a display now, as 91 other exercise items already are.

- **`latex/sleek/` is gone (2026-09-24).** The two vendored files were replaced by
  `latex/page-style.sty` (base packages, the 2.5cm page, the fancyhdr frame,
  `\arraystretch`) and `latex/theorem-frame.sty` (the `bookframe` mdframed style and the
  `mdthm` key for `\declaretheorem`), written from the documentation of `geometry`,
  `fancyhdr`, `parskip`, `mdframed` and `thmtools` rather than from the vendored code,
  because the upstream repository was gone and the licence could not be established.
  `LICENSE` no longer carves a directory out. The print edition did not move: 3,326 pages
  either way, 110 overfull boxes, worst 72.2pt, the same `\newlabel` numbering, and all 262
  section PDFs pixel-identical. `latex/README.md` says what the two files hold.
  **`parfill` still must not come back.**

### M7, the whole-book pass

- **Run as a workflow**, 11 agents: six over disjoint chapter bands (00–03, 04–07, 08–11, 12–15, 16–19, 20–23) doing the same four jobs on their own chapters, a preface author and a notation-page author beside them, then a TFAE auditor and a whole-book referee, then one pass applying the findings. The run was interrupted once by a session ending and resumed from cache; bands C–F were told to treat the half-finished edits already on disk as unverified proposals, which is how the duplicated-`@`-reference failure mode was avoided
- **The forward-promise ledger went from 50 open lines to 3.** 46 were verified paid, each against the label that pays it, and the 138 labels cited as payment across the six reports were checked to exist. The three that remain: Ch 12 §10 → Ch 13 (Lyapunov, genuinely unpaid), Ch 24 → a later book (no SVD algorithm, target outside the book), and Ch 20 §10's norm restriction (recorded, both sides now agree)
- **One band report was wrong and was caught.** Band C reported that Chapter 9 makes no Schur promise — that "Schur", "orthonormal" and "Chapter 12" appear nowhere in `src/ch09-eigenvalues/`. All three are on `07-triangularization.md:219`, and `thm-schur-triangularization` pays it. Ticked over the band's verdict. This is the reason the coordinator verifies ticks rather than applying them
- **The dependency graph was drawing every edge.** One forward cross-chapter reference (Ch 18 §08 → Ch 19) made the chapters cite each other in a circle, so the graph page fell back to drawing all 251 edges. With it gone the graph reads 248 edges, 217 implied, 31 drawn, and the build's circle warning is gone. A book-wide scan now finds **zero** forward cross-chapter references, index pages included
- **Twelve lettered citations of numerically-numbered theorem parts** were repaired (`thm-trace-properties`, `thm-transpose-properties`); a re-scan of 3330 part references across the book found 0 out of range and 0 style mismatches
- **The only software mention in the book's prose is gone** — Ch 3 §02's "A computer algebra system does the same computation exactly" is now "The same computation can be carried out in exact arithmetic". The `{.python .run}` cell it sat beside is a widget and was left alone
- **The preface** was rewritten from 343 words to 1,630. It states the book's two-state proof promise, points at Chapter 16's (A1)–(A6) as the clearest instance, describes the shape of a section, and gives reading paths; the referee checked its counts and the repair pass corrected four of its prerequisite claims against the measured reference counts
- **The notation page is `src/ch24a-notation/index.md`**, 299 rows over twelve groups, 528 `@`-references to 355 distinct labels, plus 39 overridden symbols. **Its registration is a deliberate trick and is fragile — do not rename the directory.** `Chapter.number` comes from `re.match(r"ch(\d+)", dir_name)`, so `ch24a` reads as 24, the same number as the preceding `ch24-applied`; `filters/theorems.lua` emits a part banner only when the chapter number *changes*, so no banner and no Chapter 25 is created. Any other name gives the page a chapter number and a full banner page. It also needs its `\markboth` line, because an unnumbered `\chapter*` never calls `\chaptermark` and the running head would otherwise stay on Chapter 24 §13
- [ ] `tools/check_forward_deps.py`'s `from_file` regex reads `ch24a-notation/index` as chapter 24, section 0 — i.e. *before* Chapter 24's own sections. Harmless while the page defines no labels, and it defines none; any label added there would be misreported
- **Still deferred after M7:** the 37 remaining `--exercises` sites (all triaged as attribution, none reclassified by the referee), the 223 "names X without a reference" warnings (down from 266; the rest were judged wrong to silence — the scanner attributes a section's trailing prose to the last labelled block, so many name a result in a heading or a warning rather than citing one), and STATUS 107's over-length sections in Ch 10, which were not split because splitting renumbers labels

### Reading paths

- **The dependency graph now answers "which sections do I actually need?"** `tools/reading_path.py` builds the graph section by section from `crossref_labels.json`'s `uses_kinds`, splitting a citation made by a proof, a proof idea or a claim (hard) from one made by a statement, a remark, an example or a solution (soft). A path is the transitive closure over the hard edges, and the property that matters is that it is **closed**: every prerequisite of every section on it is on it. An unclosed path fails the build
- **Ten reader profiles live in `config/config.json` under `reading-paths`**, each a slug, a name, a one-line description and a list of target sections; `build/extras.py` generates `paths.html` and one `path-<slug>.html` per profile from them, and `tools/reading_path.py --profile <slug>` computes the same thing on the command line. To add or retarget a path, edit the config; no code changes
- **Every path is published twice.** `solution` is 5,778 of the book's 11,612 citations, and a solution is the proof of its exercise, so the policy is a parameter (`HARD_KINDS`, `EXERCISE_KINDS`) and both answers are printed: the reading path, and the longer path for a reader who works the exercises. The difference runs from +5 sections (coding theory) to +36 (optimization, control)
- **The preface's five hand-written paths were wrong in every entry**, always understating; `src/index.md` now points at the generated pages instead
- **The graph page uses the same data.** It used to count `scan.json`'s per-page `refs`, which includes the chapter introductions whose job is to cite the rest of the book; that is why it was dense. Edges now carry the hard count as their weight and the soft count alongside, and the page has a picker: choose any section or profile and the chapters its path never reaches are dimmed, with the sections needed from each of the rest named
- **Four weakest links were cut**, each a whole section dragged onto many paths by one small citation. Ch 11 §06's adjoint-versus-dual-map theorem became exercise C4 (Ch 5 §§03–04 and Ch 1 §08 leave the reading path; SVD 81 → 78, spectral 73 → 70). Ch 12 §03's proof recalled `def-nilpotent` in a step it did not use it in; the recall moved into the statement (spectral 70 → 64, characters 95 → 93). `lem-frobenius-unitarily-invariant` moved from Ch 12 §11 to Ch 11 §07 (Perron 96 → 95, seven profiles one section shorter). `def-permutation-matrix` and `lem-permutation-matrices` (a)-(c) moved from Ch 3 §06 to Ch 3 §04, part (d) staying behind as `lem-swap-past-gauss-transform` because it is about this section's Gauss transforms (characters 95 → 94)
- **Left alone as real.** `thm-adjoint-exists` needs `thm-riesz-representation`, and Ch 11 §05 is on nine of the ten paths for that one proof; Ch 5 §§01–02 stay on the SVD path because `thm-annihilator-vs-orthogonal-complement` needs the annihilator, which is what §05 is for. Ch 10 §02 is a real prerequisite of the Jordan form and stays on the Jordan path

### Chapter 23 (algebras and representations)

- **Drafted, refereed and revised by a workflow**, the same shape as Chapter 22: five section pairs each flowing draft → referee → revise on its own clock, then an index written against the delivered text, a consistency referee over the seams, and one pass applying its findings. 18 agents, no failures
- **The chapter imports no analysis.** No limit, no continuity, no compactness; it adds nothing to Chapter 16's list (A1)–(A6) and does not use it. Roots of unity are Chapter 0 §06 and nothing more
- **Six things are quoted with credit and proved nowhere**, each flagged where a reader meets it, with nothing depending on any of them: Wedderburn–Artin over a division ring and Wedderburn's little theorem (§06 — the book has never built division rings); that the character table does not determine the group (§08, the two order-8 groups named and neither constructed); the structure theorem for finite abelian groups (§09 — what *is* proved is |Ĝ| = |G| for every finite abelian G, and Ĝ ≅ G for cyclic groups and products of them); the converse of `prp-semisimple-has-zero-radical` (§03); and the criterion for {A}' = F[A] (§01). Jacobson's density theorem and von Neumann's double commutant theorem are named in §05 as the shapes this proof is a shadow of, and neither is used
- **The group theory the book lacks was built in place, not assumed.** Chapter 0 §10 has only groups, subgroups, homomorphisms and cycle notation. §08 proves conjugacy classes, the finite order of an element and the cycle-conjugation rule where it needs them, and `lem-group-order-invertible` (char F ∤ m ⟹ m·1_F ≠ 0) because Chapter 0's division algorithm is an exercise and a theorem may not rest on one. §09 builds the order of an element, the cyclic group and the direct product. No use of Lagrange, cosets or quotient groups survives
- **The blueprint was wrong ten times**, each caught by a drafter or referee with evidence. The worst three: it filed the double commutant theorem under the algebraically-closed heading, where the theorem in fact needs only finite dimension, 1 ∈ A and semisimple action; it listed `cor-weyr-commutant-revisited` as a corollary of that theorem, which is false, since Chapter 10's `F[W]` does not act semisimply; and §10 was told that Chapter 24 precedes Chapter 23 in reading order, which `config/config.json` contradicts, so the section now says nothing about ordering. Also: "the column ideals `{X : col(X) ⊆ U}`" are *right* ideals under the book's column convention (§02 proves the left-ideal classification in its correct form); `def-semisimple-algebra` was glossed as a property of an action rather than of an algebra; `def-algebra-radical` was specified as the largest nilpotent ideal where the Jacobson radical is what makes the upper-triangular computation come out; Burnside was routed through Schur, which that proof does not need; `cor-sum-of-squares` was routed through §06 where decomposing the regular character is self-contained; the verified-labels list put `def-alternating-group` in Ch 0 §10 when it is Ch 7 §03; and the blueprint overstated Chapter 10 §07, whose Smith normal form is over F[x], the integer version being an exercise that assumes its own input
- **A correction to Chapter 12's indexing, found by §09.** "A circulant is an element of ℂ[ℤ/nℤ] acting by multiplication" is true only after reversing the basis, because Chapter 12 fixes (C)_jk = c_{k−j}; in the natural basis the matrix of multiplication is the transpose. §09 proves the clean form and gives the basis in which it is literally left multiplication, with a warning. Related and also stated there: Cx is correlation, not convolution — it is the *product* of circulants that convolves
- **Burnside is proved in full, including the step that usually has a hole**: that {φ₀ ∘ c : c ∈ A} is all of V*, by showing its common kernel is a proper invariant subspace and then counting dimensions. Burnside is *not* used for Wedderburn along the route §06 takes, and §06 says so
- `--exercises` lists two Ch 23 sites: **both triaged, attribution only** — §09's two remarks after `thm-dual-group-iso`, one pointing at Chapter 10's Smith normal form exercise while saying an exercise is not a proof, one pointing at this section's own C2 for the canonical double-dual isomorphism
- **Nothing in the book pointed forward to Chapter 23**, so the chapter opened no promises and closed none

### Chapter 24 (computation and applications)

- **The chapter's rule was: prove it, or state it with credit and mark it unproved, with nothing depending on it.** Seven referees tested that rule. What is quoted and not proved, by section: the same LU backward bound for Chapter 3's row ordering and the seam between the model bound and the exact-arithmetic growth bound (§02); Wilkinson's accumulated Householder backward error, of which the one-reflection case is proved, and the Gram–Schmidt rates (§03); the quadratic rate of Rayleigh quotient iteration for non-Hermitian matrices — **the cubic Hermitian rate is proved in full** (§04); Abel–Ruffini and the general QR convergence theorem, of which the first column is proved (§05); Kaniel–Paige–Saad and Paige's loss-of-orthogonality analysis (§06); differentiability of the orthogonal factor, on which only the *continuous* Toda/QR statement rests — the discrete one is proved (§08); the sample-to-population inference (§10); Brent's recursive bound, Winograd's lower bound, and every bound on ω below log₂ 7 (§13)
- **A second model, beside floating point.** §09 states Newton's second law and Hooke's law as `def-mass-spring-model`, in the same register as `def-floating-point-model`: an idealization, with everything after it a theorem about the model
- **The blueprint was wrong nine times**, each caught by a drafter or referee with evidence. The worst: it sent §09's normal-mode proof to Ch 9's `thm-simultaneous-diagonalization` (commuting operators) where the theorem needed is Ch 13 §04's `thm-simultaneous-congruence` — Ch 13 §04's own warning says the two have no common generalization, so following the pointer would have produced a false proof. Also: the Cholesky entry bound with the wrong index (false, with a counterexample now in the text); the classical Gram–Schmidt rate given as uκ where it is uκ²; "a QR step preserves Hessenberg form" for an arbitrary factorization (false for a singular matrix — the Givens route is the repair, with a witness); an incomplete proof sketch for the incidence-minor lemma; a "diagonal twiddle factor" that is a butterfly; a quadratic that is not real-valued over ℂ; `thm-tridiagonal-recurrence` placed in Ch 11 (it is Ch 7 §08); and a fabricated quotation from Ch 16 §08
- **Proved beyond the scope the blueprint allowed:** the LU backward error for general n, the Kantorovich inequality in full, the cubic RQI rate, ω ≥ 2, and the isospectral theorem via Jacobi's formula — which needs no matrix flow at all, and so avoids the ODE the book cannot solve
- `--exercises` lists five Ch 24 sites: **all triaged, attribution only** — §01's remark after the inner-product theorem, §06's warning (which now carries the numbers inline), §08's credit line in a Quick check solution, §11's example naming Chapter 7's graph, and §12's warning. The scanner credits blocks that follow a result; no proof step in the chapter cites an exercise
- [ ] Ch 24 → a later book: no SVD algorithm is assembled here (see the Ch 13 line above). Bidiagonalization and the singular-value iteration are the natural next section if the chapter is ever extended

### Chapter 21 (matrix inequalities)

- **The book's first and only permanent import beyond (A1)–(A6).** Loewner's theorem was promised *proved* here four times by Ch 17 §11, and its classification half cannot be proved with the book's analysis. With the author's decision, §10 quotes the Nevanlinna–Pick theory once, as **(A7)** (`thm-pick-nevanlinna`), states what it costs, and proves everything else. Verified by a referee: (A7) appears in no other section, and `cor-power-operator-monotone`, `cor-log-operator-monotone` and `exm-exp-not-monotone` do not use it. The elementary half — operator monotone of order n exactly when every Loewner matrix is positive semidefinite, **for C¹ functions** — is proved in full in §09
- **The blueprint was wrong three times, each caught by a drafter with a counterexample:** the matrix AM–GM it specified (2|||A*B||| ≤ |||A*A + B*B|||) is false, and the true form is 2σⱼ(A*B) ≤ λⱼ(AA* + BB*); the route given for the polar-factor corollary fails, as do two obvious repairs; and the order-2 criterion is f' ≥ 0 with f[s,t]² ≤ f'(s)f'(t), not a concavity condition
- **§09 rejected both proof routes the blueprint offered** for the derivative of a matrix function (one needs eigenprojection derivatives Ch 20 does not supply, the other needs polynomial approximation, which is not an imported fact) and proved an exact spectral-projection identity instead. The resulting theorem allows **repeated eigenvalues**, which the criterion's proof needs, since the segment it walks has them at uncountably many points. A referee confirmed the identity symbolically and numerically
- [x] Ch 13 §09 → Ch 21: the polar factor minimizes the distance in every unitarily invariant norm (Ch 21 §06 `cor-polar-nearest-ui`). *This promise was never in this ledger; it is recorded now because the chapter paid it*
- Stated with credit and **not proved**, with nothing depending on either: Lieb's concavity theorem (§12) and the Lieb–Thirring extension of the trace power inequality beyond powers of two
- Golden–Thompson fails for three matrices, with an exact counterexample (three projections at 120°); for three Hermitian matrices the quantity need not even be real, so there is no inequality to state
- `--exercises` lists one Ch 21 site, `cor-monotone-order-two` → `exr-loewner-matrices-c2` (§09): **triaged, attribution only** — the corollary's proof inlines the logarithm estimate, and the exercise is credited for proving it at leisure

### Chapter 20 (perturbation theory)

- **The theorem Chapter 16 quoted is now proved.** Ch 16 §07 said of `thm-roots-depend-continuously` that the book "neither proves nor can prove" it and that a proof "needs complex analysis". Both were false: compactness, fact (A3), plus unique factorization in ℂ[x] suffice. Ch 20 §03 proves it as `thm-roots-continuous`, and **Ch 16 §07's two sentences were reworded** (the only edit this chapter made outside its own directory) to say that the chapter quotes the theorem and Chapter 20 proves it. Ch 19 §03's remark, which says Chapter 16 quotes it without proof, is still accurate and was left alone
- **A silent PDF defect, found by a referee and now gated.** A non-ASCII character inside a math span is dropped by pdflatex with **no error**, so the PDF gate passed while the printed page read "the angle is less than 13". Six raw degree signs in §§09–10 became `^\circ`, and `tests/test_display_math_source.py` gained `test_no_non_ascii_inside_math`, verified to fail on a planted glyph. The rest of the book was clean
- Blueprint errors the drafters and referees caught: a repeated eigenvalue was said to have infinite condition number (true only when it is **defective** — I₂ is the counterexample); §06 was sent to Ch 14's `thm-sylvester-inertia`, which covers only real symmetric forms, where Ch 17 §10's `thm-inertia-second-proof` (b) is what the complex case needs; the one-sided Sylvester bound was said to follow in both norms from the singular-pair trick, which gives only the spectral one; Ch 12 §11's "κ = 1 exactly" was stated with a minimum where the infimum is what can be proved
- Stated but deliberately not proved, each flagged in the text, and nothing depends on either: the π/2 bound for Hermitian pairs with separated spectra (§07) and the two-sided interval form of Davis–Kahan in the spectral norm (§09)
- [x] Ch 20 §05, §10 → Ch 21: the Hoffman–Wielandt and Mirsky bounds inside one statement covering every unitarily invariant norm (Ch 21 §07 `thm-lidskii-ui`, `cor-hoffman-wielandt-again`, `thm-mirsky-ui`)
- [ ] **Still open, and now recorded:** Ch 20 §10's square-root and polar-factor bounds (`thm-sqrt-perturbation`, `thm-polar-positive-perturbation`, `thm-polar-unitary-perturbation`) hold only in the spectral and Frobenius norms. Ch 20 §11's sentence sweeps them into the Ch 21 promise; Ch 21 does not extend them, and §07 now says so
- [x] Ch 20 §04, §06, §11 → Ch 24: backward error (§01), the residual as a certificate (§06's Ritz bounds), and the algorithms (§§04–06)
- Elsner's matching bound is proved with the factor 2n − 1 (`thm-elsner-matching`); the text says better constants are known and does not pursue them
- `--exercises` lists one Ch 20 site, `thm-sqrt-perturbation` → `exr-singular-values-and-polar-c1` (§10): **triaged, attribution only** — the citation is in the warning after the theorem, which the scanner sweeps; the proof cites only Ch 13's square root and §07's `cor-positive-sylvester`
- Pre-existing chain worth knowing (M7): Ch 20 §01 cites `prp-left-eigenvectors-transpose` (b) for σ(Aᵀ) = σ(A), and that Ch 9 proposition gets p_{Aᵀ} = p_A from an exercise. Same chain as the Ch 19 §01 entry above; one line in Ch 9 fixes all of them

### Chapter 19 (nonnegative matrices)

- [x] Ch 9 §11 → Ch 19 §06 (`thm-markov-limit-primitive`): Perron–Frobenius gives the Markov limit for every stochastic matrix with a positive power, without diagonalizability
- [x] Ch 18 §08, §11 → Ch 19 §07 (`thm-birkhoff`): Birkhoff's theorem (Ch 18 proved the two forms equivalent and the permutation matrices extreme)
- [x] Ch 19 §07, §09 → Ch 21: Hardy–Littlewood–Pólya (Ch 21 §01 `thm-hardy-littlewood-polya`, by T-transforms, with D a product of at most n−1 of them for sorted vectors)
- [x] Ch 19 §04, §08, §09 → Ch 24: the power method and its rate (§04 `thm-power-method`)
- **Transitive exercise dependency (M7 triage):** Ch 9 §10's `prp-left-eigenvectors-transpose` (b) gets p_{Aᵀ} = p_A from `exr-characteristic-polynomial-b2`, and Ch 19 §01's proof of Perron cites that proposition. It is one of the 42 sites `--exercises` lists; fixing it (one line: det(xI − Aᵀ) = det((xI − A)ᵀ)) settles both

### Chapter 18 (convexity)

- [x] Ch 16 → Ch 18 §04: **dual norms** (`def-dual-norm`, `thm-dual-dual-norm`; pairs 1↔∞ and 2↔2 in §04, general p in §11's `thm-dual-p-norm`). Ch 16's outline and blueprint listed them, but Ch 16 never defined one (and makes no claim to). Ch 18 §04 delivers `def-dual-norm` and ‖·‖** = ‖·‖
- [x] Ch 17 §06 → Ch 18 §10: a pointwise supremum of linear functions is convex (`prp-sup-of-affine-convex`, quoted verbatim)
- [x] Ch 16 §01 → Ch 18 §11: Minkowski's inequality. Ch 16 said the book "does not prove and never uses" it; Ch 18 §11 proves it from Hölder (`cor-minkowski-inequality`) and uses it for the dual p-norms, so the Ch 16 sentence was updated to point there (a pointer update, as Ch 16 §08's Eckart–Young pointer was for Ch 17)
- Ch 16 §01 wrote \( |x_i|^p \) and the exponent \( 1/p \) for real p without defining real powers; the book had **no logarithm**. Ch 18 §11 builds log from Ch 10 §09's exp (`lem-exp-log`) and defines \( t^r = e^{r\log t} \). Ch 16's use was a remark, not a proof step
- [x] Ch 3 §07 → Ch 18 §06: inequalities and linear programming (`exm-traffic-lp`; Ch 3 names no chapter)
- [x] Ch 14 §06 said nothing later depends on its imported (A1) symmetry / (A2) Taylor; Ch 18 §10's `thm-convex-second-derivative` does, so the Ch 14 sentence was updated (a pointer update, like the Minkowski one)
- [x] Ch 18 §10, §11 → Ch 21: A ↦ tr f(A) is convex for convex f (Ch 21 §02 `thm-trace-convex`, from `lem-peierls`)
- [x] Ch 18 §04 (~line 344): an earlier draft promised §10 a circular "second proof of the triangle inequality" from `cor-norm-as-max`; the final text says only that norms are examples of a max of linear functions, and the revision adds that their convexity was already the triangle inequality

### Chapter 17 (variational principles and interlacing)

Discharged (to be confirmed by referee):
- [x] Ch 12 §02 → Ch 17 §§01–02: the optimization description of every eigenvalue of a self-adjoint operator (`cor-courant-fischer-operator`). No analytic fact is *invoked*; the analysis underneath is the fundamental theorem of algebra (Ch 6 §05, via the extreme value theorem), which the spectral theorem rests on
- [x] **M7, overclaim in deployed text:** Ch 12 §02 (~line 110) says it avoided the extreme value theorem "so that nothing in this chapter depends on it". Chapter 12 depends on it through the fundamental theorem of algebra. Not edited, since the text is deployed and outside this chapter; reword in the whole-book pass
- [x] Ch 13 §05 → Ch 17 §02: λ_i(A) ≥ λ_i(B) for every i when A ⪰ B (`cor-loewner-eigenvalue-monotone`)
- [x] Ch 13 §12 → Ch 17 §01: eigenvalues as extrema of ⟨Ax, x⟩
- [x] Ch 16 §07 → Ch 17 §03: Hermitian eigenvalues move by at most ‖E‖₂ (`cor-weyl-perturbation`)
- [x] Ch 13 §10 and Ch 16 §08 → Ch 17 §09: the spectral-norm Eckart–Young (`thm-eckart-young-spectral`)
- [x] Ch 11 §10 → Ch 17 §04: strict interlacing of the zeros of consecutive orthogonal polynomials (`cor-orthogonal-polynomial-zeros-interlace`). **Missed by the blueprint.** Ch 11 had only *asserted*, inside an exercise solution, that p_k is the characteristic polynomial of the Jacobi matrix; §04 proves it
- [x] Ch 13 §10 → Ch 17 §06: `lem-orthonormal-capture-bound` recovered as a special case of Ky Fan (`cor-capture-bound-revisited`); the text now says *special*, not *extreme*

Created:
- [x] Ch 17 §01 → Ch 24: Rayleigh quotient iteration (§04 `thm-rqi-cubic`, cubic rate proved in full for the Hermitian case)
- [x] Ch 17 §08 → Ch 19: Birkhoff's theorem on doubly stochastic matrices (paid in Ch 19 §07) (no longer needed for Horn; the plan has it in Ch 19 in its own right). **Ch 18 §08 defines `def-doubly-stochastic` (Ω_n), proves the permutation matrices are extreme, and states Birkhoff in two equivalent forms with the equivalence proved — Ch 19 need only prove one form**
- [x] Ch 17 §08: Horn's converse is **proved in §08** (`lem-horn-two-by-two`, `thm-horn`, `thm-schur-horn`), by induction from a 2×2 rotation. It was first deferred to Ch 21 on the false premise that it needs Birkhoff; the approved outline puts Schur–Horn in Ch 17
- [x] Ch 17 §08 → Ch 21: Schur-concavity of the product and Schur-concave functions in general (Ch 21 §02 `def-schur-concave`, `cor-product-schur-concave`)
- [x] Ch 17 §09 → Ch 20: the Hermitian dilation, used for singular-value perturbation (Ch 20 §10 proves Mirsky's bound with it)
- Ch 13 → Ch 20 "perturbation of singular values" is now **partly** paid by Ch 17 §09's `cor-singular-value-perturbation` (|σᵢ(A+E) − σᵢ(A)| ≤ ‖E‖₂, no hypothesis on E); Chapter 20 keeps the rest
- [x] Ch 17 §09 → Ch 21: Eckart–Young in every unitarily invariant norm (Ch 21 §06 `cor-eckart-young-ui`, by Ch 13 §10's predicted route through Weyl's singular-value inequality)
- [x] Ch 17 §06 → Ch 18: a pointwise supremum of linear functions is convex (the plan's "Convex functions")
- [x] Ch 17 §06 → Ch 21: the Ky Fan partial sums applied to singular values (Ch 21 §04 `def-ky-fan-norm`, §06 `thm-ky-fan-dominance`)
- [x] Ch 17 §07 → Ch 21: the consequences of λ(A)−λ(B) ≺ λ(A−B) for every convex φ and for every unitarily invariant norm (Ch 21 §02 `thm-karamata`, §07 `thm-lidskii-convex`, `thm-lidskii-ui`)
- [x] Ch 17 §11 → Ch 21: Loewner's theorem, both directions (Ch 21 §10 `thm-loewner`). **The classification half rests on the chapter's one import, (A7)**, the Nevanlinna–Pick theory, quoted once in §10; the elementary half (operator monotonicity of every order = positivity of every Loewner matrix, for C¹ functions) is proved in full in §09
- [x] Ch 17 §11 → Ch 21: t^p operator monotone exactly for 0 ≤ p ≤ 1 (Ch 21 §10 `cor-power-operator-monotone`), log operator monotone (`cor-log-operator-monotone`), e^t not (`exm-exp-not-monotone`). **None of the three uses (A7)**; Ch 17 §11 predicted they would need Loewner's theorem and they do not

Deferred polish (M7), from the Chapter 17 referees; none affects correctness:
- §04: the letter m means three things (deleted index, number of deleted rows, eigenspace dimension, where NOTATION's g_B(ν) should be used), and Step 3's p collides with p_A. §03/§04 write the eigenvalue list as plain λ(A) where NOTATION now registers bold `\vlambda(\A)`. §03 uses bold E both for the perturbation and for matrix units (Ch 16's precedent)
- §04 is ~5,300 words; the referee suggested ~400 words of trims (permutation paragraph, the I = {2,3} discussion, the B2 solution tail). §03's `lem-rayleigh-on-eigenspan` (b) is used nowhere
- **Deployed Ch 11 §10 (~line 111)** says "the node inner product on n nodes"; the section's own setup has n+1 nodes c₀…cₙ on ℝ[x]_{≤n}. Not edited, since it is outside this chapter

### Chapter 16 (norms and matrix analysis)

- [x] Ch 11 §01 → Ch 16 §01: not every norm comes from an inner product; the parallelogram law is the test. Ch 11's exercise proved the ℝ² case granting homogeneity; §01 supplies the homogeneity limit, drops the dimension hypothesis and adds the complex case
- [x] Ch 10 §10 → Ch 16 §04: `ρ(A) ≤ ‖A‖` for every induced norm, plus Gelfand. What is new is the **rate**, not the convergence criterion
- [x] Ch 13 §08 and §12 → Ch 16 §03: the operator norm named, and `‖A‖₂ = σ₁`
- [x] Ch 10 §09 → Ch 16 §06: quantitative bounds for `e^A` in place of exact formulas
- [x] Ch 12 §01 → Ch 16 §05/§07: the "perturb and take a limit" argument made routine
- [x] Ch 16 §07 → Ch 17: Weyl's inequality, from Courant–Fischer (duplicate of the §03 line above; paid by `thm-weyl-inequalities`, `cor-weyl-perturbation`)
- [x] Ch 16 §07 → Ch 20: Bauer–Fike (Ch 20 §04 reproves the exercise as `lem-perturbed-eigenvalue-resolvent`, crediting it, so no theorem rests on an exercise)
- [x] Ch 16 §08 → Ch 17: the spectral-norm Eckart–Young that Ch 13 §10 could not state (Ch 17 §09 proves it from the min–max for singular values; the Ch 16 text originally sent this to Ch 21 and was corrected)
- [x] Ch 16 §08 → Ch 21: unitarily invariant norms (Ch 21 §04), and Eckart–Young for all of them at once (§06)
- [x] Ch 16 §08 → Ch 24: the conditioning of the least-squares *problem* (which involves the residual, not just κ₂(A)); the floating-point model and backward error analysis; the digit-loss comparison between the normal equations and QR
- Maintenance hazard: Ch 16 §06 cites Chapter 10 §09's imported analysis facts by **number** — (A1), (A4), (A5) — and that list is a plain enumerate with no labels. The three numbers are correct today (checked), but renumbering or inserting an item in Ch 10 §09 would break Ch 16 silently. Same pattern for Ch 16's own (A1)–(A4) list, cited from §§01–06
- **OUTSTANDING, and older than this chapter:** Ch 12 §10 says the positive definite solution of the Lyapunov equation "is the subject of Chapter 13", and **Chapter 13 never proves it** — "Lyapunov" appears nowhere in Ch 13. Ch 16 §06 delivers the decay half and the conditional half (any positive definite X solving it makes x*Xx decrease), and states in its own text that the existence half is not proved in the book. The Ch 12 §10 sentence still points readers at Chapter 13; **a proposed rewording of it was declined, so the misdirection stands in the deployed text and is recorded here instead**. The usual proof integrates `e^{tA*}Q e^{tA}` over `[0, ∞)`, which needs matrix-valued integrals the book does not set up. **Exactly what Ch 16 does establish** (refereed): `thm-exponential-decay` gives the decay of every solution of `ẋ = Ax` for stable `A`, with an explicit rate, and uses no Lyapunov equation at all; `exr-matrix-exponential-and-calculus-c3` shows that `x*Xx` strictly decreases along every non-zero solution **given** a positive definite `X` solving the equation — but that is an exercise, not body text. The existence of such an `X` is proved nowhere in the book, and §06 says so in its own text
