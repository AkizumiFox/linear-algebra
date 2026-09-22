# Book status

The plan is at `~/.claude/plans/cached-gathering-sedgewick.md`. The outline of all chapters is in §1 of the plan.

## Chapters

| Ch | Dir | Topic | State |
|---|---|---|---|
| 0 | ch00-foundations | Preliminaries | deployed |
| 1 | ch01-vector-spaces | Vector spaces | deployed |
| 2 | ch02-linear-systems | Linear systems | deployed |
| 3 | ch03-linear-maps | Linear maps | deployed |
| 4 | ch04-duality | Duality | deployed |
| 5 | ch05-polynomials | Polynomials | deployed |
| 6 | ch06-determinants | Determinants | deployed |
| 7 | ch07-block-matrices | Block matrices | deployed |
| 8 | ch08-eigenvalues | Eigenvalues and diagonalization | deployed |
| 9 | ch09-canonical-forms | Canonical forms | deployed |
| 10 | ch10-inner-products | Inner product spaces | deployed |
| 11 | ch11-spectral-theory | Spectral theory | deployed |
| 12 | ch12-psd-and-svd | Positive matrices and the SVD | deployed |
| 13 | ch13-forms | Bilinear and quadratic forms | deployed |
| 14 | ch14-tensors | Tensors and exterior algebra | deployed |
| 15 | ch15-norms | Norms and matrix analysis | deployed |
| 16 | ch16-variational | Variational principles and interlacing | deployed |
| 17 | ch17-convexity | Convexity | deployed |
| 18 | ch18-nonnegative | Non-negative matrices | deployed |
| 19 | ch19-perturbation | Perturbation theory | deployed |
| 20 | ch20-inequalities | Matrix inequalities | deployed |
| 21 | ch21-geometry | Affine and projective geometry | deployed |
| 22 | ch22-algebras | Algebras and representations | deployed |
| 23 | ch23-applied | Computation and applications | deployed |

## Open forward promises

Add a line when a section promises something later ("proved in Chapter 5"); tick it when it is paid off.

- [x] Ch 0 → Ch 5: Fundamental Theorem of Algebra proved
- [x] Ch 0 → Ch 2 §07 (`lem-root-bound`): a polynomial over an infinite field is determined by its values
- [x] Ch 0 → Ch 5: division algorithm in general
- [x] Ch 0 → Ch 2 (`thm-one-sided-inverse`): for square matrices AB = I implies BA = I (Ch 0 text may say Chapter 3: fix to Chapter 2)
- [x] Ch 0 → Ch 2: A invertible ⇔ Ax = 0 only trivial solution
- [x] Ch 0 → Ch 1: independence/"not all zero"; {0} subspace, ∅ not; intersection vs union of subspaces; span as intersection; Fⁿ as a vector space
- [x] Ch 0 → Ch 3: kernel test for injectivity; quotient vector spaces; similarity
- [x] Ch 0 → Ch 5: unique prime factorization in F[x] (Ch 0 mentions uniqueness for integers without proof)
- [x] Ch 0 → Ch 6: sign of a permutation
- [x] Ch 0 → Ch 13: char ≠ 2 in forms
- [x] Ch 0 (09-matrices) → Ch 2: every elementary row operation is left multiplication by an invertible matrix; row equivalence = reachable by row operations
- [x] Ch 0 (09-matrices) → Ch 3: similar matrices represent the same linear map in different bases; matrix of a composition is the product
- [x] Ch 0 (09-matrices) → Ch 6: ad − bc is the determinant of a 2×2 matrix; det is a homomorphism GL_n(F) → F \ {0} (10-groups)
- [x] Ch 0 (10-groups) → Ch 6: parity of the number of transpositions is well defined (sign homomorphism)

## Notation added beyond NOTATION.md

(none yet)
- [x] Ch 1 → Ch 3: Rank–Nullity by the same "basis, extend, Big Claim, count" move
- [x] Ch 1 → Ch 3: external direct sums; projection onto U along W (different complements, different projections)
- [x] Ch 1 → Ch 8: eigenspaces of a diagonalizable operator give a direct sum
- [x] Ch 1 → Ch 3: coordinate map is an isomorphism; shift map injective not surjective; (ℝⁿ)_ℂ ≅ ℂⁿ
- [~] Ch 1 → Ch 8/11: complexification gives real matrices complex eigenvalues (Ch 8 half paid); used in real spectral theory (Ch 11)
- [x] Ch 2 → Ch 3, 6, 8, 12: invertible-matrix TFAE grows (kernel/image; det; eigenvalues; singular values)
- [x] Ch 2 → Ch 3: Rank–Nullity for linear maps
- [x] Ch 2 §06 → Ch 12 §02: Cholesky, derived from `thm-ldlt` by absorbing the square root of the diagonal
- [x] Ch 2 → Ch 23: partial pivoting, rounding (§02); graph Laplacian (§11)
- [x] Ch 2 → Ch 5: Lagrange interpolation formula
- [x] Ch 2 → Ch 10: least squares

## Deferred to the whole-book pass (M7)

- Proof endings: STYLE asks every proof to close with "This shows …"/"as claimed". Observance is uneven — Ch 8 has 9 closers for 52 proofs, Ch 9 has 20 for 57, Ch 10 has 24 for 56. Make it consistent book-wide rather than chapter by chapter.
- [x] **Display widths, web: clean.** The harness now reports `none (6569 displays measured on 263 pages)` at the 39rem text column — the 215 over-width displays this line used to record are all gone. Re-measure with `tools/_measure.html` (see `authoring/measure-displays.md`) after any bulk edit.
- [ ] **Display widths, print: not clean, and never was measured before.** The book PDF’s LaTeX log carries **845 overfull hboxes over 364 of its 3308 pages**, worst 81pt. This is a different measurement from the web one — a different column width and it counts prose lines as well as displays — and it is pre-existing, not caused by M7. The notation page contributes zero. Attribute them with a scan of `_build/tmp/latex-book/book.log` that tracks the `[N` page markers
- [x] `thm-trace-properties` (Ch 0 §09) numbers its parts 1, 2, 3 with a bare list while almost every other multi-part theorem uses `label=(\alph*)`. **M7 closed the drift**: twelve citations had gone lettered (seven "(c)" and three "(a)" for this theorem, two "(d)" for `thm-transpose-properties`) and all now use the numeric style; a re-scan checked 3330 part references across the book and found 0 out of range and 0 style mismatches. Converting the theorem itself would now cost 41 citation edits and is **not** recommended

- Long sections to consider splitting or trimming: Ch 0 §04 functions, §05 relations, §09 matrices; Ch 1 §01–§04; Ch 2 §02 Gaussian elimination (~11.7k raw words), §05 rank.
- Ch 2 §03: "pivot columns of A" is defined inside `cor-pivot-columns-well-defined`; consider a separate def block.
- Ch 2 §05 symbol reuse (r, **r**ᵢ, **b**) — tidy in M7.
- Ch 3 §01 and §04 both define "operator" and the shorthand Tv; §04 should defer to §01 (check at Ch 3 referee).
- Ch 3: 'every linear map Fⁿ → Fᵐ is T_A' proved twice (§04 C1(b), §06 inline) — consolidate into one result in M7. §06 long; rank/invertibility subsection could move to §08.
- Ch 3 §09 long (~11k raw): consider splitting products/cosets from isomorphism theorems. §08 Sylvester proof duplicates exr-rank-nullity-c1.
- [x] Ch 4 → Ch 5: Lagrange interpolation formula; evaluation functionals dual to Lagrange basis
- [x] Ch 4 → Ch 10: orthogonal complement vs annihilator; inner product gives chosen V ≅ V*; adjoint T*
- Ch 4: ε_{ij} vs ε_c overload; zero functional notation — tidy in M7.
- Ch 4: restriction map V* → U* named R (§02), ρ (§05), ι′ (§04) — unify to ρ in M7. §06 extra early Quick check.
- [x] Ch 5 → Ch 8: minimal polynomial = monic generator of I_T (`thm-annihilator-ideal`); invariant subspaces defined; Cayley–Hamilton; primary decomposition via `thm-kernel-splitting` and `exr-polynomials-of-operators-c2`
- [x] Ch 5 → Ch 9: canonical forms from primary decomposition
- [x] Ch 5 → Ch 8: diagonalizable ⇔ minimal polynomial splits with distinct roots; every complex operator has an eigenvalue (FTA)
- Ch 6 §03: disjoint cycle decomposition only asserted (Ch 0 shows by example) — consider a short proof in M7.
- [x] Ch 6 → Ch 8: (xI − A)·adj(xI − A) = det(xI − A)·I reappears (Cayley–Hamilton route)
- [x] Ch 6 → Ch 7: Schur complements cite `thm-det-block-triangular`
- [x] Ch 6 → Ch 8: eigenvalues from `thm-charpoly-root-iff-singular`; Cayley–Hamilton; p_AB = p_BA in general
- [x] Ch 6 → Ch 9: complete similarity invariants
- [x] Ch 6 → Ch 10/12: Gram matrices, √det(AᵀA) area via inner products
- [x] Ch 6 → Ch 11: circulants of every size
- [x] Ch 6 → Ch 23: matrix-tree theorem (§11 `thm-matrix-tree`, proved in full; Ch 6's pieces are in an exercise, so §11 reproves them and credits it)
- [x] Ch 7 → Ch 11: AX − XB = C uniquely solvable ⇔ no common eigenvalue (over ℂ); Ch 19 quantitative form (`prp-sep-properties` (d))
- [x] Ch 7 → Ch 14: tensor product of maps has matrix A ⊗ B
- [x] Ch 7 → Ch 8: tr C^k = 0 for all k ⇒ nilpotent, via eigenvalues (over ℂ and its subfields)
- [x] Ch 7 → Ch 8: p_T = p_{T|U} · p_{T̄} for T mapping U into U
- [x] Ch 7 → Ch 12: positive definiteness via Schur complements
- [x] Ch 7 → Ch 23: Gaussian elimination as repeated Schur complements (§02 `thm-elimination-is-schur-complements`)
- [x] Ch 8 → Ch 9: recurrences with repeated roots (k^jλ^k) via the Jordan form; generalized eigenspaces named; cyclic vector when deg m = dim V; m and p together do not decide similarity
- [x] Ch 8 → Ch 11: Schur's orthonormal triangularization
- [x] Ch 8 → Ch 18: Perron–Frobenius gives the Markov limit for regular stochastic matrices
- [x] Ch 3/6/8 → Ch 9: similarity decided; complete invariants (split case); generalized eigenspaces named; best matrix when g < a
- [x] Ch 9 → Ch 9 §06: canonical form over every field (rational form); §07 removes the splitting hypothesis from A ~ Aᵀ
- [x] Ch 9 → Ch 19: numerical instability of the Jordan form (§03's `exm-jordan-root-perturbation`, §04's `thm-bauer-fike-defective`, §11's remark)
- [x] Ch 3 → Ch 9: A ~ Aᵀ over any field (`cor-a-similar-to-transpose`)
- [x] Ch 8 §11 → Ch 9: Markov powers without diagonalizability (`cor-markov-powers-converge`)
- [x] Ch 9 → Ch 15: norms give quantitative bounds for e^A and for powers; ρ(A) ≤ ‖A‖ and the spectral radius as a limit
- Ch 9 §07 is long (~10k raw); natural seam after the Smith theorem. Ch 9 §04, §06 also long. Consider in M7.

### Chapter 10 (inner product spaces)

- [x] Ch 6 §07 → Ch 10: Gram determinants (`cor-gram-determinant-nonnegative` becomes `thm-gram-matrix-properties`, §02)
- [x] Ch 4 → Ch 10 §05: the inner product is the data that picks an isomorphism V ≅ V\*; Ch 4's basis map Θ_𝓑 is the Riesz map of the inner product making 𝓑 orthonormal. (Ch 4's warning carries no label, so §05 cites `cor-dimension-dual-space` and `thm-evaluation-natural`; give that warning a label if a hard link is ever wanted.)
- [x] Ch 4 → Ch 10 §05: annihilator U⁰ corresponds to U^⊥ (`thm-annihilator-vs-orthogonal-complement`)
- [x] Ch 10 §03/§04/§05 → Ch 10 §06: P_U is self-adjoint; ker(T\*T) = ker T; (nul A)^⊥ = col(A\*) as the four-subspaces theorem; the dual map read through Riesz is the adjoint
- [x] Ch 2 §07 → Ch 10 §04: the low-degree approximate fit promised where interpolation follows the noise (`exm-least-squares-line`, `exm-least-squares-quadratic`). Chapter 2 itself states no orthogonality, so §06's four subspaces extend Ch 2 rather than discharging a promise.
- [x] Ch 10 §01 → Ch 15: general norms; not every norm comes from an inner product, the parallelogram law is the test
- [x] Ch 10 §02/§08 → Ch 23: §03 gives the rates (classical loses orthogonality like uκ², modified like uκ — **stated with credit, not proved**, and demonstrated by simulation), and proves the one-reflection backward error
- [x] Ch 10 §04 → Ch 12: the pseudoinverse A⁺ packages the least-squares and minimum-norm answers (note: §04 writes the minimum-norm solution x_min; Ch 12 may prefer A⁺b — rename then if so)
- [x] Ch 10 §05 → Hilbert spaces: representability needs completeness and continuity. **Not a debt** — §05 states this as the boundary of the finite-dimensional theorem, names no chapter and promises nothing. Ticked to take it off the open list, not because anything paid it
- [x] Ch 10 §06 → Ch 11: all spectral theory of self-adjoint and normal operators
- [x] Ch 10 §02 → Ch 11: what an inner product adds once an operator is also given

### Chapter 11 (spectral theory)

- [x] Ch 11 §01 → Ch 15: norms and limits for matrices, making the "diagonalizable, then take a limit" argument precise
- [x] Ch 11 §02 → Ch 12: positive operators (`exr-self-adjoint-operators-c1` proves half the characterization)
- [x] Ch 11 §02 → Ch 16: the Rayleigh quotient and Courant–Fischer, the optimization route to eigenvalues of a self-adjoint operator
- [x] Ch 7 §04 → Ch 11 §10: the Sylvester equation is uniquely solvable exactly when the spectra are disjoint (Ch 7 states the promise at the end of the Kronecker section)
- [x] Ch 11 §08 → Ch 12: positive operators — paid by `thm-psd-square-root`, `thm-polar-decomposition` and `thm-svd`, which are exactly what the square root built in §08 was for
- [ ] **Still open:** Ch 11 §10 → Ch 12, positive definite solutions of the Lyapunov equation. Chapter 12 never mentions Lyapunov — the word does not occur anywhere in `src/ch12-psd-and-svd/`. The promise is real and nothing pays it. **Ch 11 §10’s wording is not to be changed** (that edit was proposed and declined), so this is paid by adding the result to Chapter 12 or not at all
- [x] Ch 11 §05 → Ch 13: congruence versus similarity, and Sylvester's law of inertia (promised twice in §05)
- [x] Ch 11 §11 → Ch 19: Bauer–Fike and eigenvalue perturbation (`thm-bauer-fike`; the "κ = 1 exactly in the normal case" half is `cor-bauer-fike-normal` (b), proved with an infimum over diagonalizing X)
- [x] Ch 11 §10 → Ch 15: Lyapunov stability of \( \dot{\x} = \A\x \)
- [x] Ch 11 §10 → Ch 19: conditioning of the Sylvester equation (Ch 19 §07, `def-sep` and `prp-sep-properties`)
- [x] Ch 11 §09 → Ch 23: the FFT (§12), with the exact cost (3/2)n log₂ n − n + 1
- Stated but deliberately not proved in Ch 11, each flagged in the text: Roth's removal rule (§10, route via Ch 9 §07's characteristic-matrix equivalence), the general Fuglede theorem (§07), general Cartan–Dieudonné (§06), and the connectedness of the unitary group (§08). Nothing later depends on any of them.
- Note for §11's drafter: `\norm{\A}_F` is already used in Ch 11 §01 exercise C2, defined locally there from the Frobenius inner product of Ch 10 §01. §11 owes the NOTATION.md row.

### Chapter 12 (positive matrices and the SVD)

- [x] Ch 11 §02 → Ch 12 §01: positive operators; `exr-self-adjoint-operators-c1` supplies one implication of `thm-psd-characterizations`
- [x] Ch 2 → Ch 3/6/8/12: the invertible-matrix TFAE grows; the Ch 12 instalment is `thm-invertible-tfae-positive`
- [x] Ch 6 §07 → Ch 12 §03: Gram determinants, sharpened to "a Gram matrix is exactly a positive semidefinite matrix"
- [x] Ch 6 §09 → Ch 12 §03: the area of a parallelogram in \( \nR^3 \) as \( \sqrt{\det(\A\tp\A)} \). Ch 6 said "Chapter 10 justifies this"; Chapter 10 never did, and the Ch 6 sentence now points at Chapter 12, which does
- [x] Ch 10 §02 → Ch 12 §03: the converse — a positive semidefinite matrix *is* a Gram matrix, with the list unique up to isometry
- [x] Ch 7 §03 → Ch 12 §06: positive definiteness tested one block at a time by Schur complements
- [x] Ch 10 §04 → Ch 12 §11: the pseudoinverse packages least squares and minimum norm; the notation is settled, \( \x_{\min} = \A^{+}\b \)
- [x] Ch 12 §06 → Ch 12 §11: the semidefinite block criterion with a singular corner (`prp-block-psd-general`). §06 promised it and §11 had not delivered; added by hand
- [x] Ch 12 §01 → Ch 13: congruence studied for its own sake
- [x] Ch 12 §02 → Ch 23: Cholesky's half cost and no pivoting (§02 `prp-lu-cost`, `thm-cholesky-stability`)
- [x] Ch 12 → Ch 15: the operator norm, and \( \norm{\A}_2 = \sigma_1 \)
- [x] Ch 12 → Ch 16: Courant–Fischer, interlacing, eigenvalue monotonicity in the Loewner order
- [x] Ch 12 → Ch 19: perturbation of singular values (Ch 16 §09's spectral bound plus Ch 19 §10's `thm-mirsky-frobenius`; §10 also does the polar factors)
- [x] Ch 12 → Ch 20: operator monotone functions, unitarily invariant norms, Eckart–Young in every unitarily invariant norm (Ch 20 §04 `thm-von-neumann-correspondence`, §06 `cor-eckart-young-ui`, §10 `thm-loewner` and `cor-power-operator-monotone`). *The spectral-norm case moved to Ch 16 §09 and is paid there*
- [x] Ch 12 → Ch 23: PCA (§10). **Partly unpaid, and Ch 12 §10's sentence was reworded to say so:** §10 gives the finite-population model and the reasons for squared error, but the inference from a sample to a larger population needs probability the book does not develop, and **no SVD algorithm is assembled anywhere in the book** — §10 says only why one never forms A*A

### Chapter 13 (bilinear and quadratic forms)

- [x] Ch 0 §07 → Ch 13 §03: "characteristic ≠ 2" earns its keep (`thm-alternating-vs-skew`, with the 𝔽₂ counterexample)
- [x] Ch 11 §05 and Ch 12 §04 → Ch 13 §05: why the signs of a congruent diagonal match the signs of the eigenvalues
- [x] Ch 12 §01 → Ch 13 §02: congruence studied for its own sake, with what it preserves and what it destroys
- [x] Ch 13 §12 → Ch 14: tensor algebras; the construction of Cl(q) as a quotient of one; the independence half of `thm-clifford-dimension`. **Chapter 13 states that theorem with its gap marked in the text**, so this debt is visible to readers
- [x] Ch 13 §09/§10 → nothing: the Pfaffian transformation rule and Sp(2m,F) ⊆ SL are recorded without proof and nothing may cite them
- Polish deferred to M7: Ch 13 §§07–08 have no labelled worked examples (`exm-`), and §10 has no Idea blocks, both against the STYLE checklist

### Chapter 14 (tensors and exterior algebra)

- [x] Ch 7 §04 → Ch 14 §03: the Kronecker product is the matrix of a tensor product of maps, in the dictionary-ordered product basis with the first factor slow. The other ordering gives the *swapped* Kronecker product, not a transpose
- [x] Ch 13 §12 → Ch 14 §10: `Cl(q)` constructed as `T(V)/⟨v ⊗ v − q(v)1⟩`, hence existence, and `dim Cl(q) = 2ⁿ` proved via creation/deletion operators on `Λ V` with no division by 2. The half Chapter 13 marked as missing was independence
- [x] Ch 3 §10 → Ch 14 §04: the trace as a contraction, with no basis chosen
- [x] Ch 14 §08 → Ch 21: Plücker coordinates (Ch 21 §10 `def-plucker-coordinates`, `prp-plucker-well-defined`, `thm-plucker-relation`, with the Klein quadric; Ch 14 §10's version is an exercise, credited and reproved)
- Polish deferred to M7: §10 is the book's longest section (~10.6k words) and carries four major notions against STYLE's two; §03 is also long. Both have natural seams recorded in the referee reports

### Book-wide gates

- **PDF errors now fail the build.** pdflatex runs in nonstopmode and writes a PDF even after an error, and the build used to judge success by the file existing. When the check was tightened (Ch 16 release), **38 of 178 sections** turned out to have been shipping damaged PDFs: 12 `.algorithm` blocks (the environment was never defined for LaTeX), 21 displays with a blank line inside `\[ … \]` (one bulk edit, all `\end{aligned}` / blank / `\]`), 20 display lines beginning like list items, 7 environment titles containing `]` (e.g. `\(F[x]\)`), 4 unmapped Unicode characters, one double superscript. All fixed; the web pages had the same displays as stray `[` `]` text, invisible because MathJax still rendered the loose `aligned`. Guards: `build/pdf.py` fails on any TeX error with an `l.<n>` context (an Overfull-box dump line that starts with `!` is not one); `tests/test_pdf_errors.py`; `tests/test_display_math_source.py` lints `src/` for both display shapes
- `tools/check_forward_deps.py` — fails if any label cites one from a later section. The book passes: 2476 labels, zero forward citations, zero dangling. It compares **sections only**, because the third component of a label number counts within a type (`def-connectives` and `thm-contrapositive-equivalent` are both 0.1.1); 3107 within-section citations therefore go unordered and remain the referee's job. Verified against planted violations
- **The scanner credits proofs by position, and it was wrong in two ways** (fixed in `9e2e712`): a proof after an example went to the example, and a proof under its own heading went to nothing — the proofs of the fundamental theorem of algebra and Cayley–Hamilton were invisible to the gate. Now: proofs skip over examples to the last result, and a separated proof names its result, `::: {.proof of="thm-..."}`; `tests/test_proof_ownership.py` fails on an orphan.
- **M7 triage, 27 sites:** a label followed by *two* proofs before the next label. Most are a theorem with a second proof (then both are correctly credited). But a lemma-with-proof placed between a theorem and its proof credits the theorem's proof to the lemma — Ch 18 §01's Perron was this, fixed by reordering. List with `python3` scan in the Ch 18 session; re-run and read each: ch01 §06 thm-steinitz, §07, §08; ch02 §04, §06; ch03 §03; ch06 §04, §06; ch08 §10; ch09 §07; ch10 §07, §08 (×2); ch11 §05, §07; ch12 §02, §06, §09; ch13 §07, §08; ch16 §02, §04, §07, §08; ch18 §05, §08
- **M7 triage, 44 sites (42 before the scanner fix exposed two more):** `tools/check_forward_deps.py --exercises` lists every theorem, proposition, corollary or lemma that cites an exercise, across 27 files in Chapters 0, 5, 7, 8, 9, 10, 11, 12, 13, 14 and 15. **This is a candidate list, not a defect list.** Citing an exercise for attribution is fine; a proof that *depends* on one is the rule this book has broken and repaired seven times. Each site needs reading. The two Chapter 15 §01 entries were triaged during that chapter's referee pass and are attribution only

### Chapter 21 (affine and projective geometry)

- **Drafted, refereed and revised by a workflow** rather than by hand-launched agents: five section pairs, each flowing draft → referee → revise on its own clock, then an index written against the delivered text, a consistency referee over the seams, and one pass applying its findings. 18 agents, no failures
- The chapter **imports no analysis at all**, and quotes six results it does not prove, each flagged where a reader meets it and listed in the index
- Blueprint corrections the drafters made: `def-face` was already taken by Ch 17 §08 (the polyhedron face here is `def-polyhedron-face`); the affine join formula's second case needed the direction-space count, not the naive one; and the duality correspondence's dimension shift had to be stated in projective dimension throughout
- Pappus over a non-commutative division ring is **stated with credit and not proved** — the book builds neither division rings nor synthetic planes — and nothing depends on it
- `--exercises` lists three Ch 21 sites: **all triaged, attribution only** — §09's remark about the small-field cases, and §10's two credits to Chapter 14's exercise, which §10 reproves rather than uses

### M7, the whole-book pass

- **Run as a workflow**, 11 agents: six over disjoint chapter bands (00–03, 04–07, 08–11, 12–15, 16–19, 20–23) doing the same four jobs on their own chapters, a preface author and a notation-page author beside them, then a TFAE auditor and a whole-book referee, then one pass applying the findings. The run was interrupted once by a session ending and resumed from cache; bands C–F were told to treat the half-finished edits already on disk as unverified proposals, which is how the duplicated-`@`-reference failure mode was avoided
- **The forward-promise ledger went from 50 open lines to 3.** 46 were verified paid, each against the label that pays it, and the 138 labels cited as payment across the six reports were checked to exist. The three that remain: Ch 11 §10 → Ch 12 (Lyapunov, genuinely unpaid), Ch 23 → a later book (no SVD algorithm, target outside the book), and Ch 19 §10's norm restriction (recorded, both sides now agree)
- **One band report was wrong and was caught.** Band C reported that Chapter 8 makes no Schur promise — that "Schur", "orthonormal" and "Chapter 11" appear nowhere in `src/ch08-eigenvalues/`. All three are on `07-triangularization.md:219`, and `thm-schur-triangularization` pays it. Ticked over the band's verdict. This is the reason the coordinator verifies ticks rather than applying them
- **The dependency graph was drawing every edge.** One forward cross-chapter reference (Ch 17 §08 → Ch 18) made the chapters cite each other in a circle, so the graph page fell back to drawing all 251 edges. With it gone the graph reads 248 edges, 217 implied, 31 drawn, and the build's circle warning is gone. A book-wide scan now finds **zero** forward cross-chapter references, index pages included
- **Twelve lettered citations of numerically-numbered theorem parts** were repaired (`thm-trace-properties`, `thm-transpose-properties`); a re-scan of 3330 part references across the book found 0 out of range and 0 style mismatches
- **The only software mention in the book's prose is gone** — Ch 2 §02's "A computer algebra system does the same computation exactly" is now "The same computation can be carried out in exact arithmetic". The `{.python .run}` cell it sat beside is a widget and was left alone
- **The preface** was rewritten from 343 words to 1,630. It states the book's two-state proof promise, points at Chapter 15's (A1)–(A6) as the clearest instance, describes the shape of a section, and gives reading paths; the referee checked its counts and the repair pass corrected four of its prerequisite claims against the measured reference counts
- **The notation page is `src/ch23a-notation/index.md`**, 299 rows over twelve groups, 528 `@`-references to 355 distinct labels, plus 39 overridden symbols. **Its registration is a deliberate trick and is fragile — do not rename the directory.** `Chapter.number` comes from `re.match(r"ch(\d+)", dir_name)`, so `ch23a` reads as 23, the same number as the preceding `ch23-applied`; `filters/theorems.lua` emits a part banner only when the chapter number *changes*, so no banner and no Chapter 24 is created. Any other name gives the page a chapter number and a full banner page. It also needs its `\markboth` line, because an unnumbered `\chapter*` never calls `\chaptermark` and the running head would otherwise stay on Chapter 23 §13
- [ ] `tools/check_forward_deps.py`'s `from_file` regex reads `ch23a-notation/index` as chapter 23, section 0 — i.e. *before* Chapter 23's own sections. Harmless while the page defines no labels, and it defines none; any label added there would be misreported
- **Still deferred after M7:** the 37 remaining `--exercises` sites (all triaged as attribution, none reclassified by the referee), the 223 "names X without a reference" warnings (down from 266; the rest were judged wrong to silence — the scanner attributes a section's trailing prose to the last labelled block, so many name a result in a heading or a warning rather than citing one), and STATUS 107's over-length sections in Ch 9, which were not split because splitting renumbers labels

### Chapter 22 (algebras and representations)

- **Drafted, refereed and revised by a workflow**, the same shape as Chapter 21: five section pairs each flowing draft → referee → revise on its own clock, then an index written against the delivered text, a consistency referee over the seams, and one pass applying its findings. 18 agents, no failures
- **The chapter imports no analysis.** No limit, no continuity, no compactness; it adds nothing to Chapter 15's list (A1)–(A6) and does not use it. Roots of unity are Chapter 0 §06 and nothing more
- **Six things are quoted with credit and proved nowhere**, each flagged where a reader meets it, with nothing depending on any of them: Wedderburn–Artin over a division ring and Wedderburn's little theorem (§06 — the book has never built division rings); that the character table does not determine the group (§08, the two order-8 groups named and neither constructed); the structure theorem for finite abelian groups (§09 — what *is* proved is |Ĝ| = |G| for every finite abelian G, and Ĝ ≅ G for cyclic groups and products of them); the converse of `prp-semisimple-has-zero-radical` (§03); and the criterion for {A}' = F[A] (§01). Jacobson's density theorem and von Neumann's double commutant theorem are named in §05 as the shapes this proof is a shadow of, and neither is used
- **The group theory the book lacks was built in place, not assumed.** Chapter 0 §10 has only groups, subgroups, homomorphisms and cycle notation. §08 proves conjugacy classes, the finite order of an element and the cycle-conjugation rule where it needs them, and `lem-group-order-invertible` (char F ∤ m ⟹ m·1_F ≠ 0) because Chapter 0's division algorithm is an exercise and a theorem may not rest on one. §09 builds the order of an element, the cyclic group and the direct product. No use of Lagrange, cosets or quotient groups survives
- **The blueprint was wrong ten times**, each caught by a drafter or referee with evidence. The worst three: it filed the double commutant theorem under the algebraically-closed heading, where the theorem in fact needs only finite dimension, 1 ∈ A and semisimple action; it listed `cor-weyr-commutant-revisited` as a corollary of that theorem, which is false, since Chapter 9's `F[W]` does not act semisimply; and §10 was told that Chapter 23 precedes Chapter 22 in reading order, which `config/config.json` contradicts, so the section now says nothing about ordering. Also: "the column ideals `{X : col(X) ⊆ U}`" are *right* ideals under the book's column convention (§02 proves the left-ideal classification in its correct form); `def-semisimple-algebra` was glossed as a property of an action rather than of an algebra; `def-algebra-radical` was specified as the largest nilpotent ideal where the Jacobson radical is what makes the upper-triangular computation come out; Burnside was routed through Schur, which that proof does not need; `cor-sum-of-squares` was routed through §06 where decomposing the regular character is self-contained; the verified-labels list put `def-alternating-group` in Ch 0 §10 when it is Ch 6 §03; and the blueprint overstated Chapter 9 §07, whose Smith normal form is over F[x], the integer version being an exercise that assumes its own input
- **A correction to Chapter 11's indexing, found by §09.** "A circulant is an element of ℂ[ℤ/nℤ] acting by multiplication" is true only after reversing the basis, because Chapter 11 fixes (C)_jk = c_{k−j}; in the natural basis the matrix of multiplication is the transpose. §09 proves the clean form and gives the basis in which it is literally left multiplication, with a warning. Related and also stated there: Cx is correlation, not convolution — it is the *product* of circulants that convolves
- **Burnside is proved in full, including the step that usually has a hole**: that {φ₀ ∘ c : c ∈ A} is all of V*, by showing its common kernel is a proper invariant subspace and then counting dimensions. Burnside is *not* used for Wedderburn along the route §06 takes, and §06 says so
- `--exercises` lists two Ch 22 sites: **both triaged, attribution only** — §09's two remarks after `thm-dual-group-iso`, one pointing at Chapter 9's Smith normal form exercise while saying an exercise is not a proof, one pointing at this section's own C2 for the canonical double-dual isomorphism
- **Nothing in the book pointed forward to Chapter 22**, so the chapter opened no promises and closed none

### Chapter 23 (computation and applications)

- **The chapter's rule was: prove it, or state it with credit and mark it unproved, with nothing depending on it.** Seven referees tested that rule. What is quoted and not proved, by section: the same LU backward bound for Chapter 2's row ordering and the seam between the model bound and the exact-arithmetic growth bound (§02); Wilkinson's accumulated Householder backward error, of which the one-reflection case is proved, and the Gram–Schmidt rates (§03); the quadratic rate of Rayleigh quotient iteration for non-Hermitian matrices — **the cubic Hermitian rate is proved in full** (§04); Abel–Ruffini and the general QR convergence theorem, of which the first column is proved (§05); Kaniel–Paige–Saad and Paige's loss-of-orthogonality analysis (§06); differentiability of the orthogonal factor, on which only the *continuous* Toda/QR statement rests — the discrete one is proved (§08); the sample-to-population inference (§10); Brent's recursive bound, Winograd's lower bound, and every bound on ω below log₂ 7 (§13)
- **A second model, beside floating point.** §09 states Newton's second law and Hooke's law as `def-mass-spring-model`, in the same register as `def-floating-point-model`: an idealization, with everything after it a theorem about the model
- **The blueprint was wrong nine times**, each caught by a drafter or referee with evidence. The worst: it sent §09's normal-mode proof to Ch 8's `thm-simultaneous-diagonalization` (commuting operators) where the theorem needed is Ch 12 §04's `thm-simultaneous-congruence` — Ch 12 §04's own warning says the two have no common generalization, so following the pointer would have produced a false proof. Also: the Cholesky entry bound with the wrong index (false, with a counterexample now in the text); the classical Gram–Schmidt rate given as uκ where it is uκ²; "a QR step preserves Hessenberg form" for an arbitrary factorization (false for a singular matrix — the Givens route is the repair, with a witness); an incomplete proof sketch for the incidence-minor lemma; a "diagonal twiddle factor" that is a butterfly; a quadratic that is not real-valued over ℂ; `thm-tridiagonal-recurrence` placed in Ch 10 (it is Ch 6 §08); and a fabricated quotation from Ch 15 §08
- **Proved beyond the scope the blueprint allowed:** the LU backward error for general n, the Kantorovich inequality in full, the cubic RQI rate, ω ≥ 2, and the isospectral theorem via Jacobi's formula — which needs no matrix flow at all, and so avoids the ODE the book cannot solve
- `--exercises` lists five Ch 23 sites: **all triaged, attribution only** — §01's remark after the inner-product theorem, §06's warning (which now carries the numbers inline), §08's credit line in a Quick check solution, §11's example naming Chapter 6's graph, and §12's warning. The scanner credits blocks that follow a result; no proof step in the chapter cites an exercise
- [ ] Ch 23 → a later book: no SVD algorithm is assembled here (see the Ch 12 line above). Bidiagonalization and the singular-value iteration are the natural next section if the chapter is ever extended

### Chapter 20 (matrix inequalities)

- **The book's first and only permanent import beyond (A1)–(A6).** Loewner's theorem was promised *proved* here four times by Ch 16 §11, and its classification half cannot be proved with the book's analysis. With the author's decision, §10 quotes the Nevanlinna–Pick theory once, as **(A7)** (`thm-pick-nevanlinna`), states what it costs, and proves everything else. Verified by a referee: (A7) appears in no other section, and `cor-power-operator-monotone`, `cor-log-operator-monotone` and `exm-exp-not-monotone` do not use it. The elementary half — operator monotone of order n exactly when every Loewner matrix is positive semidefinite, **for C¹ functions** — is proved in full in §09
- **The blueprint was wrong three times, each caught by a drafter with a counterexample:** the matrix AM–GM it specified (2|||A*B||| ≤ |||A*A + B*B|||) is false, and the true form is 2σⱼ(A*B) ≤ λⱼ(AA* + BB*); the route given for the polar-factor corollary fails, as do two obvious repairs; and the order-2 criterion is f' ≥ 0 with f[s,t]² ≤ f'(s)f'(t), not a concavity condition
- **§09 rejected both proof routes the blueprint offered** for the derivative of a matrix function (one needs eigenprojection derivatives Ch 19 does not supply, the other needs polynomial approximation, which is not an imported fact) and proved an exact spectral-projection identity instead. The resulting theorem allows **repeated eigenvalues**, which the criterion's proof needs, since the segment it walks has them at uncountably many points. A referee confirmed the identity symbolically and numerically
- [x] Ch 12 §09 → Ch 20: the polar factor minimizes the distance in every unitarily invariant norm (Ch 20 §06 `cor-polar-nearest-ui`). *This promise was never in this ledger; it is recorded now because the chapter paid it*
- Stated with credit and **not proved**, with nothing depending on either: Lieb's concavity theorem (§12) and the Lieb–Thirring extension of the trace power inequality beyond powers of two
- Golden–Thompson fails for three matrices, with an exact counterexample (three projections at 120°); for three Hermitian matrices the quantity need not even be real, so there is no inequality to state
- `--exercises` lists one Ch 20 site, `cor-monotone-order-two` → `exr-loewner-matrices-c2` (§09): **triaged, attribution only** — the corollary's proof inlines the logarithm estimate, and the exercise is credited for proving it at leisure

### Chapter 19 (perturbation theory)

- **The theorem Chapter 15 quoted is now proved.** Ch 15 §07 said of `thm-roots-depend-continuously` that the book "neither proves nor can prove" it and that a proof "needs complex analysis". Both were false: compactness, fact (A3), plus unique factorization in ℂ[x] suffice. Ch 19 §03 proves it as `thm-roots-continuous`, and **Ch 15 §07's two sentences were reworded** (the only edit this chapter made outside its own directory) to say that the chapter quotes the theorem and Chapter 19 proves it. Ch 18 §03's remark, which says Chapter 15 quotes it without proof, is still accurate and was left alone
- **A silent PDF defect, found by a referee and now gated.** A non-ASCII character inside a math span is dropped by pdflatex with **no error**, so the PDF gate passed while the printed page read "the angle is less than 13". Six raw degree signs in §§09–10 became `^\circ`, and `tests/test_display_math_source.py` gained `test_no_non_ascii_inside_math`, verified to fail on a planted glyph. The rest of the book was clean
- Blueprint errors the drafters and referees caught: a repeated eigenvalue was said to have infinite condition number (true only when it is **defective** — I₂ is the counterexample); §06 was sent to Ch 13's `thm-sylvester-inertia`, which covers only real symmetric forms, where Ch 16 §10's `thm-inertia-second-proof` (b) is what the complex case needs; the one-sided Sylvester bound was said to follow in both norms from the singular-pair trick, which gives only the spectral one; Ch 11 §11's "κ = 1 exactly" was stated with a minimum where the infimum is what can be proved
- Stated but deliberately not proved, each flagged in the text, and nothing depends on either: the π/2 bound for Hermitian pairs with separated spectra (§07) and the two-sided interval form of Davis–Kahan in the spectral norm (§09)
- [x] Ch 19 §05, §10 → Ch 20: the Hoffman–Wielandt and Mirsky bounds inside one statement covering every unitarily invariant norm (Ch 20 §07 `thm-lidskii-ui`, `cor-hoffman-wielandt-again`, `thm-mirsky-ui`)
- [ ] **Still open, and now recorded:** Ch 19 §10's square-root and polar-factor bounds (`thm-sqrt-perturbation`, `thm-polar-positive-perturbation`, `thm-polar-unitary-perturbation`) hold only in the spectral and Frobenius norms. Ch 19 §11's sentence sweeps them into the Ch 20 promise; Ch 20 does not extend them, and §07 now says so
- [x] Ch 19 §04, §06, §11 → Ch 23: backward error (§01), the residual as a certificate (§06's Ritz bounds), and the algorithms (§§04–06)
- Elsner's matching bound is proved with the factor 2n − 1 (`thm-elsner-matching`); the text says better constants are known and does not pursue them
- `--exercises` lists one Ch 19 site, `thm-sqrt-perturbation` → `exr-singular-values-and-polar-c1` (§10): **triaged, attribution only** — the citation is in the warning after the theorem, which the scanner sweeps; the proof cites only Ch 12's square root and §07's `cor-positive-sylvester`
- Pre-existing chain worth knowing (M7): Ch 19 §01 cites `prp-left-eigenvectors-transpose` (b) for σ(Aᵀ) = σ(A), and that Ch 8 proposition gets p_{Aᵀ} = p_A from an exercise. Same chain as the Ch 18 §01 entry above; one line in Ch 8 fixes all of them

### Chapter 18 (nonnegative matrices)

- [x] Ch 8 §11 → Ch 18 §06 (`thm-markov-limit-primitive`): Perron–Frobenius gives the Markov limit for every stochastic matrix with a positive power, without diagonalizability
- [x] Ch 17 §08, §11 → Ch 18 §07 (`thm-birkhoff`): Birkhoff's theorem (Ch 17 proved the two forms equivalent and the permutation matrices extreme)
- [x] Ch 18 §07, §09 → Ch 20: Hardy–Littlewood–Pólya (Ch 20 §01 `thm-hardy-littlewood-polya`, by T-transforms, with D a product of at most n−1 of them for sorted vectors)
- [x] Ch 18 §04, §08, §09 → Ch 23: the power method and its rate (§04 `thm-power-method`)
- **Transitive exercise dependency (M7 triage):** Ch 8 §10's `prp-left-eigenvectors-transpose` (b) gets p_{Aᵀ} = p_A from `exr-characteristic-polynomial-b2`, and Ch 18 §01's proof of Perron cites that proposition. It is one of the 42 sites `--exercises` lists; fixing it (one line: det(xI − Aᵀ) = det((xI − A)ᵀ)) settles both

### Chapter 17 (convexity)

- [x] Ch 15 → Ch 17 §04: **dual norms** (`def-dual-norm`, `thm-dual-dual-norm`; pairs 1↔∞ and 2↔2 in §04, general p in §11's `thm-dual-p-norm`). Ch 15's outline and blueprint listed them, but Ch 15 never defined one (and makes no claim to). Ch 17 §04 delivers `def-dual-norm` and ‖·‖** = ‖·‖
- [x] Ch 16 §06 → Ch 17 §10: a pointwise supremum of linear functions is convex (`prp-sup-of-affine-convex`, quoted verbatim)
- [x] Ch 15 §01 → Ch 17 §11: Minkowski's inequality. Ch 15 said the book "does not prove and never uses" it; Ch 17 §11 proves it from Hölder (`cor-minkowski-inequality`) and uses it for the dual p-norms, so the Ch 15 sentence was updated to point there (a pointer update, as Ch 15 §08's Eckart–Young pointer was for Ch 16)
- Ch 15 §01 wrote \( |x_i|^p \) and the exponent \( 1/p \) for real p without defining real powers; the book had **no logarithm**. Ch 17 §11 builds log from Ch 9 §09's exp (`lem-exp-log`) and defines \( t^r = e^{r\log t} \). Ch 15's use was a remark, not a proof step
- [x] Ch 2 §07 → Ch 17 §06: inequalities and linear programming (`exm-traffic-lp`; Ch 2 names no chapter)
- [x] Ch 13 §06 said nothing later depends on its imported (A1) symmetry / (A2) Taylor; Ch 17 §10's `thm-convex-second-derivative` does, so the Ch 13 sentence was updated (a pointer update, like the Minkowski one)
- [x] Ch 17 §10, §11 → Ch 20: A ↦ tr f(A) is convex for convex f (Ch 20 §02 `thm-trace-convex`, from `lem-peierls`)
- [x] Ch 17 §04 (~line 344): an earlier draft promised §10 a circular "second proof of the triangle inequality" from `cor-norm-as-max`; the final text says only that norms are examples of a max of linear functions, and the revision adds that their convexity was already the triangle inequality

### Chapter 16 (variational principles and interlacing)

Discharged (to be confirmed by referee):
- [x] Ch 11 §02 → Ch 16 §§01–02: the optimization description of every eigenvalue of a self-adjoint operator (`cor-courant-fischer-operator`). No analytic fact is *invoked*; the analysis underneath is the fundamental theorem of algebra (Ch 5 §05, via the extreme value theorem), which the spectral theorem rests on
- [x] **M7, overclaim in deployed text:** Ch 11 §02 (~line 110) says it avoided the extreme value theorem "so that nothing in this chapter depends on it". Chapter 11 depends on it through the fundamental theorem of algebra. Not edited, since the text is deployed and outside this chapter; reword in the whole-book pass
- [x] Ch 12 §05 → Ch 16 §02: λ_i(A) ≥ λ_i(B) for every i when A ⪰ B (`cor-loewner-eigenvalue-monotone`)
- [x] Ch 12 §12 → Ch 16 §01: eigenvalues as extrema of ⟨Ax, x⟩
- [x] Ch 15 §07 → Ch 16 §03: Hermitian eigenvalues move by at most ‖E‖₂ (`cor-weyl-perturbation`)
- [x] Ch 12 §10 and Ch 15 §08 → Ch 16 §09: the spectral-norm Eckart–Young (`thm-eckart-young-spectral`)
- [x] Ch 10 §10 → Ch 16 §04: strict interlacing of the zeros of consecutive orthogonal polynomials (`cor-orthogonal-polynomial-zeros-interlace`). **Missed by the blueprint.** Ch 10 had only *asserted*, inside an exercise solution, that p_k is the characteristic polynomial of the Jacobi matrix; §04 proves it
- [x] Ch 12 §10 → Ch 16 §06: `lem-orthonormal-capture-bound` recovered as a special case of Ky Fan (`cor-capture-bound-revisited`); the text now says *special*, not *extreme*

Created:
- [x] Ch 16 §01 → Ch 23: Rayleigh quotient iteration (§04 `thm-rqi-cubic`, cubic rate proved in full for the Hermitian case)
- [x] Ch 16 §08 → Ch 18: Birkhoff's theorem on doubly stochastic matrices (paid in Ch 18 §07) (no longer needed for Horn; the plan has it in Ch 18 in its own right). **Ch 17 §08 defines `def-doubly-stochastic` (Ω_n), proves the permutation matrices are extreme, and states Birkhoff in two equivalent forms with the equivalence proved — Ch 18 need only prove one form**
- [x] Ch 16 §08: Horn's converse is **proved in §08** (`lem-horn-two-by-two`, `thm-horn`, `thm-schur-horn`), by induction from a 2×2 rotation. It was first deferred to Ch 20 on the false premise that it needs Birkhoff; the approved outline puts Schur–Horn in Ch 16
- [x] Ch 16 §08 → Ch 20: Schur-concavity of the product and Schur-concave functions in general (Ch 20 §02 `def-schur-concave`, `cor-product-schur-concave`)
- [x] Ch 16 §09 → Ch 19: the Hermitian dilation, used for singular-value perturbation (Ch 19 §10 proves Mirsky's bound with it)
- Ch 12 → Ch 19 "perturbation of singular values" is now **partly** paid by Ch 16 §09's `cor-singular-value-perturbation` (|σᵢ(A+E) − σᵢ(A)| ≤ ‖E‖₂, no hypothesis on E); Chapter 19 keeps the rest
- [x] Ch 16 §09 → Ch 20: Eckart–Young in every unitarily invariant norm (Ch 20 §06 `cor-eckart-young-ui`, by Ch 12 §10's predicted route through Weyl's singular-value inequality)
- [x] Ch 16 §06 → Ch 17: a pointwise supremum of linear functions is convex (the plan's "Convex functions")
- [x] Ch 16 §06 → Ch 20: the Ky Fan partial sums applied to singular values (Ch 20 §04 `def-ky-fan-norm`, §06 `thm-ky-fan-dominance`)
- [x] Ch 16 §07 → Ch 20: the consequences of λ(A)−λ(B) ≺ λ(A−B) for every convex φ and for every unitarily invariant norm (Ch 20 §02 `thm-karamata`, §07 `thm-lidskii-convex`, `thm-lidskii-ui`)
- [x] Ch 16 §11 → Ch 20: Loewner's theorem, both directions (Ch 20 §10 `thm-loewner`). **The classification half rests on the chapter's one import, (A7)**, the Nevanlinna–Pick theory, quoted once in §10; the elementary half (operator monotonicity of every order = positivity of every Loewner matrix, for C¹ functions) is proved in full in §09
- [x] Ch 16 §11 → Ch 20: t^p operator monotone exactly for 0 ≤ p ≤ 1 (Ch 20 §10 `cor-power-operator-monotone`), log operator monotone (`cor-log-operator-monotone`), e^t not (`exm-exp-not-monotone`). **None of the three uses (A7)**; Ch 16 §11 predicted they would need Loewner's theorem and they do not

Deferred polish (M7), from the Chapter 16 referees; none affects correctness:
- §04: the letter m means three things (deleted index, number of deleted rows, eigenspace dimension, where NOTATION's g_B(ν) should be used), and Step 3's p collides with p_A. §03/§04 write the eigenvalue list as plain λ(A) where NOTATION now registers bold `\vlambda(\A)`. §03 uses bold E both for the perturbation and for matrix units (Ch 15's precedent)
- §04 is ~5,300 words; the referee suggested ~400 words of trims (permutation paragraph, the I = {2,3} discussion, the B2 solution tail). §03's `lem-rayleigh-on-eigenspan` (b) is used nowhere
- **Deployed Ch 10 §10 (~line 111)** says "the node inner product on n nodes"; the section's own setup has n+1 nodes c₀…cₙ on ℝ[x]_{≤n}. Not edited, since it is outside this chapter

### Chapter 15 (norms and matrix analysis)

- [x] Ch 10 §01 → Ch 15 §01: not every norm comes from an inner product; the parallelogram law is the test. Ch 10's exercise proved the ℝ² case granting homogeneity; §01 supplies the homogeneity limit, drops the dimension hypothesis and adds the complex case
- [x] Ch 9 §10 → Ch 15 §04: `ρ(A) ≤ ‖A‖` for every induced norm, plus Gelfand. What is new is the **rate**, not the convergence criterion
- [x] Ch 12 §08 and §12 → Ch 15 §03: the operator norm named, and `‖A‖₂ = σ₁`
- [x] Ch 9 §09 → Ch 15 §06: quantitative bounds for `e^A` in place of exact formulas
- [x] Ch 11 §01 → Ch 15 §05/§07: the "perturb and take a limit" argument made routine
- [x] Ch 15 §07 → Ch 16: Weyl's inequality, from Courant–Fischer (duplicate of the §03 line above; paid by `thm-weyl-inequalities`, `cor-weyl-perturbation`)
- [x] Ch 15 §07 → Ch 19: Bauer–Fike (Ch 19 §04 reproves the exercise as `lem-perturbed-eigenvalue-resolvent`, crediting it, so no theorem rests on an exercise)
- [x] Ch 15 §08 → Ch 16: the spectral-norm Eckart–Young that Ch 12 §10 could not state (Ch 16 §09 proves it from the min–max for singular values; the Ch 15 text originally sent this to Ch 20 and was corrected)
- [x] Ch 15 §08 → Ch 20: unitarily invariant norms (Ch 20 §04), and Eckart–Young for all of them at once (§06)
- [x] Ch 15 §08 → Ch 23: the conditioning of the least-squares *problem* (which involves the residual, not just κ₂(A)); the floating-point model and backward error analysis; the digit-loss comparison between the normal equations and QR
- Maintenance hazard: Ch 15 §06 cites Chapter 9 §09's imported analysis facts by **number** — (A1), (A4), (A5) — and that list is a plain enumerate with no labels. The three numbers are correct today (checked), but renumbering or inserting an item in Ch 9 §09 would break Ch 15 silently. Same pattern for Ch 15's own (A1)–(A4) list, cited from §§01–06
- **OUTSTANDING, and older than this chapter:** Ch 11 §10 says the positive definite solution of the Lyapunov equation "is the subject of Chapter 12", and **Chapter 12 never proves it** — "Lyapunov" appears nowhere in Ch 12. Ch 15 §06 delivers the decay half and the conditional half (any positive definite X solving it makes x*Xx decrease), and states in its own text that the existence half is not proved in the book. The Ch 11 §10 sentence still points readers at Chapter 12; **a proposed rewording of it was declined, so the misdirection stands in the deployed text and is recorded here instead**. The usual proof integrates `e^{tA*}Q e^{tA}` over `[0, ∞)`, which needs matrix-valued integrals the book does not set up. **Exactly what Ch 15 does establish** (refereed): `thm-exponential-decay` gives the decay of every solution of `ẋ = Ax` for stable `A`, with an explicit rate, and uses no Lyapunov equation at all; `exr-matrix-exponential-and-calculus-c3` shows that `x*Xx` strictly decreases along every non-zero solution **given** a positive definite `X` solving the equation — but that is an exercise, not body text. The existence of such an `X` is proved nowhere in the book, and §06 says so in its own text
