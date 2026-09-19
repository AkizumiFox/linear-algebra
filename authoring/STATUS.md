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
| 18–23 | | see plan | not started |

## Open forward promises

Add a line when a section promises something later ("proved in Chapter 5"); tick it when it is paid off.

- [x] Ch 0 → Ch 5: Fundamental Theorem of Algebra proved
- [x] Ch 0 → Ch 2 §07 (`lem-root-bound`): a polynomial over an infinite field is determined by its values
- [x] Ch 0 → Ch 5: division algorithm in general
- [x] Ch 0 → Ch 2 (`thm-one-sided-inverse`): for square matrices AB = I implies BA = I (Ch 0 text may say Chapter 3: fix to Chapter 2)
- [x] Ch 0 → Ch 2: A invertible ⇔ Ax = 0 only trivial solution
- [ ] Ch 0 → Ch 1: independence/"not all zero"; {0} subspace, ∅ not; intersection vs union of subspaces; span as intersection; Fⁿ as a vector space
- [ ] Ch 0 → Ch 3: kernel test for injectivity; quotient vector spaces; similarity
- [ ] Ch 0 → Ch 5: unique prime factorization in F[x] (Ch 0 mentions uniqueness for integers without proof)
- [x] Ch 0 → Ch 6: sign of a permutation
- [ ] Ch 0 → Ch 13: char ≠ 2 in forms
- [ ] Ch 0 (09-matrices) → Ch 2: every elementary row operation is left multiplication by an invertible matrix; row equivalence = reachable by row operations
- [ ] Ch 0 (09-matrices) → Ch 3: similar matrices represent the same linear map in different bases; matrix of a composition is the product
- [ ] Ch 0 (09-matrices) → Ch 6: ad − bc is the determinant of a 2×2 matrix; det is a homomorphism GL_n(F) → F \ {0} (10-groups)
- [ ] Ch 0 (10-groups) → Ch 6: parity of the number of transpositions is well defined (sign homomorphism)

## Notation added beyond NOTATION.md

(none yet)
- [ ] Ch 1 → Ch 3: Rank–Nullity by the same "basis, extend, Big Claim, count" move
- [ ] Ch 1 → Ch 3: external direct sums; projection onto U along W (different complements, different projections)
- [x] Ch 1 → Ch 8: eigenspaces of a diagonalizable operator give a direct sum
- [ ] Ch 1 → Ch 3: coordinate map is an isomorphism; shift map injective not surjective; (ℝⁿ)_ℂ ≅ ℂⁿ
- [~] Ch 1 → Ch 8/11: complexification gives real matrices complex eigenvalues (Ch 8 half paid); used in real spectral theory (Ch 11)
- [x] Ch 2 → Ch 3, 6, 8, 12: invertible-matrix TFAE grows (kernel/image; det; eigenvalues; singular values)
- [ ] Ch 2 → Ch 3: Rank–Nullity for linear maps
- [x] Ch 2 §06 → Ch 12 §02: Cholesky, derived from `thm-ldlt` by absorbing the square root of the diagonal
- [ ] Ch 2 → Ch 23: partial pivoting, rounding; graph Laplacian
- [x] Ch 2 → Ch 5: Lagrange interpolation formula
- [ ] Ch 2 → Ch 10: least squares

## Deferred to the whole-book pass (M7)

- Proof endings: STYLE asks every proof to close with "This shows …"/"as claimed". Observance is uneven — Ch 8 has 9 closers for 52 proofs, Ch 9 has 20 for 57, Ch 10 has 24 for 56. Make it consistent book-wide rather than chapter by chapter.
- Display widths: 215 displays exceed the 39rem text column (39 of them at 130%+), spread over Ch 0–9; Ch 10 has three. Measure with `tools/_measure.html` (see `authoring/measure-displays.md`) and break them with `aligned`.
- `thm-trace-properties` (Ch 0 §09) numbers its parts 1, 2, 3 with a bare list while almost every other multi-part theorem uses `label=(\alph*)`. Two citations had already drifted to "(c)". Consider converting the theorem and its ~6 numeric citations together.

- Long sections to consider splitting or trimming: Ch 0 §04 functions, §05 relations, §09 matrices; Ch 1 §01–§04; Ch 2 §02 Gaussian elimination (~11.7k raw words), §05 rank.
- Ch 2 §03: "pivot columns of A" is defined inside `cor-pivot-columns-well-defined`; consider a separate def block.
- Ch 2 §05 symbol reuse (r, **r**ᵢ, **b**) — tidy in M7.
- Ch 3 §01 and §04 both define "operator" and the shorthand Tv; §04 should defer to §01 (check at Ch 3 referee).
- Ch 3: 'every linear map Fⁿ → Fᵐ is T_A' proved twice (§04 C1(b), §06 inline) — consolidate into one result in M7. §06 long; rank/invertibility subsection could move to §08.
- Ch 3 §09 long (~11k raw): consider splitting products/cosets from isomorphism theorems. §08 Sylvester proof duplicates exr-rank-nullity-c1.
- [x] Ch 4 → Ch 5: Lagrange interpolation formula; evaluation functionals dual to Lagrange basis
- [ ] Ch 4 → Ch 10: orthogonal complement vs annihilator; inner product gives chosen V ≅ V*; adjoint T*
- Ch 4: ε_{ij} vs ε_c overload; zero functional notation — tidy in M7.
- Ch 4: restriction map V* → U* named R (§02), ρ (§05), ι′ (§04) — unify to ρ in M7. §06 extra early Quick check.
- [x] Ch 5 → Ch 8: minimal polynomial = monic generator of I_T (`thm-annihilator-ideal`); invariant subspaces defined; Cayley–Hamilton; primary decomposition via `thm-kernel-splitting` and `exr-polynomials-of-operators-c2`
- [ ] Ch 5 → Ch 9: canonical forms from primary decomposition
- [ ] Ch 5 → Ch 8: diagonalizable ⇔ minimal polynomial splits with distinct roots; every complex operator has an eigenvalue (FTA)
- Ch 6 §03: disjoint cycle decomposition only asserted (Ch 0 shows by example) — consider a short proof in M7.
- [ ] Ch 6 → Ch 8: (xI − A)·adj(xI − A) = det(xI − A)·I reappears (Cayley–Hamilton route)
- [ ] Ch 6 → Ch 7: Schur complements cite `thm-det-block-triangular`
- [x] Ch 6 → Ch 8: eigenvalues from `thm-charpoly-root-iff-singular`; Cayley–Hamilton; p_AB = p_BA in general
- [ ] Ch 6 → Ch 9: complete similarity invariants
- [ ] Ch 6 → Ch 10/12: Gram matrices, √det(AᵀA) area via inner products
- [ ] Ch 6 → Ch 11: circulants of every size
- [ ] Ch 6 → Ch 23: matrix-tree theorem
- [ ] Ch 7 → Ch 11: AX − XB = C uniquely solvable ⇔ no common eigenvalue (over ℂ); Ch 19 quantitative form
- [ ] Ch 7 → Ch 14: tensor product of maps has matrix A ⊗ B
- [x] Ch 7 → Ch 8: tr C^k = 0 for all k ⇒ nilpotent, via eigenvalues (over ℂ and its subfields)
- [x] Ch 7 → Ch 8: p_T = p_{T|U} · p_{T̄} for T mapping U into U
- [ ] Ch 7 → Ch 12: positive definiteness via Schur complements
- [ ] Ch 7 → Ch 23: Gaussian elimination as repeated Schur complements
- [ ] Ch 8 → Ch 9: recurrences with repeated roots (k^jλ^k) via the Jordan form; generalized eigenspaces named; cyclic vector when deg m = dim V; m and p together do not decide similarity
- [ ] Ch 8 → Ch 11: Schur's orthonormal triangularization
- [ ] Ch 8 → Ch 18: Perron–Frobenius gives the Markov limit for regular stochastic matrices
- [x] Ch 3/6/8 → Ch 9: similarity decided; complete invariants (split case); generalized eigenspaces named; best matrix when g < a
- [ ] Ch 9 → Ch 9 §06: canonical form over every field (rational form); §07 removes the splitting hypothesis from A ~ Aᵀ
- [ ] Ch 9 → Ch 19: numerical instability of the Jordan form
- [x] Ch 3 → Ch 9: A ~ Aᵀ over any field (`cor-a-similar-to-transpose`)
- [x] Ch 8 §11 → Ch 9: Markov powers without diagonalizability (`cor-markov-powers-converge`)
- [ ] Ch 9 → Ch 15: norms give quantitative bounds for e^A and for powers; ρ(A) ≤ ‖A‖ and the spectral radius as a limit
- Ch 9 §07 is long (~10k raw); natural seam after the Smith theorem. Ch 9 §04, §06 also long. Consider in M7.

### Chapter 10 (inner product spaces)

- [x] Ch 6 §07 → Ch 10: Gram determinants (`cor-gram-determinant-nonnegative` becomes `thm-gram-matrix-properties`, §02)
- [x] Ch 4 → Ch 10 §05: the inner product is the data that picks an isomorphism V ≅ V\*; Ch 4's basis map Θ_𝓑 is the Riesz map of the inner product making 𝓑 orthonormal. (Ch 4's warning carries no label, so §05 cites `cor-dimension-dual-space` and `thm-evaluation-natural`; give that warning a label if a hard link is ever wanted.)
- [x] Ch 4 → Ch 10 §05: annihilator U⁰ corresponds to U^⊥ (`thm-annihilator-vs-orthogonal-complement`)
- [x] Ch 10 §03/§04/§05 → Ch 10 §06: P_U is self-adjoint; ker(T\*T) = ker T; (nul A)^⊥ = col(A\*) as the four-subspaces theorem; the dual map read through Riesz is the adjoint
- [x] Ch 2 §07 → Ch 10 §04: the low-degree approximate fit promised where interpolation follows the noise (`exm-least-squares-line`, `exm-least-squares-quadratic`). Chapter 2 itself states no orthogonality, so §06's four subspaces extend Ch 2 rather than discharging a promise.
- [ ] Ch 10 §01 → Ch 15: general norms; not every norm comes from an inner product, the parallelogram law is the test
- [ ] Ch 10 §02/§08 → Ch 23: classical Gram–Schmidt is numerically unstable; why the reflection route is used instead
- [ ] Ch 10 §04 → Ch 12: the pseudoinverse A⁺ packages the least-squares and minimum-norm answers (note: §04 writes the minimum-norm solution x_min; Ch 12 may prefer A⁺b — rename then if so)
- [ ] Ch 10 §05 → Hilbert spaces: representability needs completeness and continuity (stated as a boundary, not promised)
- [ ] Ch 10 §06 → Ch 11: all spectral theory of self-adjoint and normal operators
- [ ] Ch 10 §02 → Ch 11: what an inner product adds once an operator is also given

### Chapter 11 (spectral theory)

- [ ] Ch 11 §01 → Ch 15: norms and limits for matrices, making the "diagonalizable, then take a limit" argument precise
- [ ] Ch 11 §02 → Ch 12: positive operators (`exr-self-adjoint-operators-c1` proves half the characterization)
- [ ] Ch 11 §02 → Ch 16: the Rayleigh quotient and Courant–Fischer, the optimization route to eigenvalues of a self-adjoint operator
- [x] Ch 7 §04 → Ch 11 §10: the Sylvester equation is uniquely solvable exactly when the spectra are disjoint (Ch 7 states the promise at the end of the Kronecker section)
- [ ] Ch 11 §08/§10 → Ch 12: positive operators (the square root built in §08 is what Ch 12 needs for the polar decomposition and the SVD); positive definite solutions of the Lyapunov equation
- [ ] Ch 11 §05 → Ch 13: congruence versus similarity, and Sylvester's law of inertia (promised twice in §05)
- [ ] Ch 11 §11 → Ch 19: Bauer–Fike and eigenvalue perturbation
- [ ] Ch 11 §10 → Ch 15: Lyapunov stability of \( \dot{\x} = \A\x \)
- [ ] Ch 11 §10 → Ch 19: conditioning of the Sylvester equation (restates Ch 7 §04's own pointer)
- [ ] Ch 11 §09 → Ch 23: the FFT as a fast way to apply the Fourier matrix, not a different theorem
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
- [ ] Ch 12 §01 → Ch 13: congruence studied for its own sake
- [ ] Ch 12 §02 → Ch 23: Cholesky costs about half of LU and needs no pivoting
- [ ] Ch 12 → Ch 15: the operator norm, and \( \norm{\A}_2 = \sigma_1 \)
- [ ] Ch 12 → Ch 16: Courant–Fischer, interlacing, eigenvalue monotonicity in the Loewner order
- [ ] Ch 12 → Ch 19: perturbation of singular values
- [ ] Ch 12 → Ch 20: operator monotone functions (first look now in Ch 16 §11; Loewner's theorem still owed), unitarily invariant norms, Eckart–Young in every unitarily invariant norm. *The spectral-norm case moved to Ch 16 §09 and is paid there*
- [ ] Ch 12 → Ch 23: PCA and the numerical SVD

### Chapter 13 (bilinear and quadratic forms)

- [x] Ch 0 §07 → Ch 13 §03: "characteristic ≠ 2" earns its keep (`thm-alternating-vs-skew`, with the 𝔽₂ counterexample)
- [x] Ch 11 §05 and Ch 12 §04 → Ch 13 §05: why the signs of a congruent diagonal match the signs of the eigenvalues
- [x] Ch 12 §01 → Ch 13 §02: congruence studied for its own sake, with what it preserves and what it destroys
- [ ] Ch 13 §12 → Ch 14: tensor algebras; the construction of Cl(q) as a quotient of one; the independence half of `thm-clifford-dimension`. **Chapter 13 states that theorem with its gap marked in the text**, so this debt is visible to readers
- [ ] Ch 13 §09/§10 → nothing: the Pfaffian transformation rule and Sp(2m,F) ⊆ SL are recorded without proof and nothing may cite them
- Polish deferred to M7: Ch 13 §§07–08 have no labelled worked examples (`exm-`), and §10 has no Idea blocks, both against the STYLE checklist

### Chapter 14 (tensors and exterior algebra)

- [x] Ch 7 §04 → Ch 14 §03: the Kronecker product is the matrix of a tensor product of maps, in the dictionary-ordered product basis with the first factor slow. The other ordering gives the *swapped* Kronecker product, not a transpose
- [x] Ch 13 §12 → Ch 14 §10: `Cl(q)` constructed as `T(V)/⟨v ⊗ v − q(v)1⟩`, hence existence, and `dim Cl(q) = 2ⁿ` proved via creation/deletion operators on `Λ V` with no division by 2. The half Chapter 13 marked as missing was independence
- [x] Ch 3 §10 → Ch 14 §04: the trace as a contraction, with no basis chosen
- [ ] Ch 14 §08 → Ch 21: Plücker coordinates (hinted, chapter not named in the text)
- Polish deferred to M7: §10 is the book's longest section (~10.6k words) and carries four major notions against STYLE's two; §03 is also long. Both have natural seams recorded in the referee reports

### Book-wide gates

- **PDF errors now fail the build.** pdflatex runs in nonstopmode and writes a PDF even after an error, and the build used to judge success by the file existing. When the check was tightened (Ch 16 release), **38 of 178 sections** turned out to have been shipping damaged PDFs: 12 `.algorithm` blocks (the environment was never defined for LaTeX), 21 displays with a blank line inside `\[ … \]` (one bulk edit, all `\end{aligned}` / blank / `\]`), 20 display lines beginning like list items, 7 environment titles containing `]` (e.g. `\(F[x]\)`), 4 unmapped Unicode characters, one double superscript. All fixed; the web pages had the same displays as stray `[` `]` text, invisible because MathJax still rendered the loose `aligned`. Guards: `build/pdf.py` fails on any TeX error with an `l.<n>` context (an Overfull-box dump line that starts with `!` is not one); `tests/test_pdf_errors.py`; `tests/test_display_math_source.py` lints `src/` for both display shapes
- `tools/check_forward_deps.py` — fails if any label cites one from a later section. The book passes: 2476 labels, zero forward citations, zero dangling. It compares **sections only**, because the third component of a label number counts within a type (`def-connectives` and `thm-contrapositive-equivalent` are both 0.1.1); 3107 within-section citations therefore go unordered and remain the referee's job. Verified against planted violations
- **M7 triage, 42 sites:** `tools/check_forward_deps.py --exercises` lists every theorem, proposition, corollary or lemma that cites an exercise, across 27 files in Chapters 0, 5, 7, 8, 9, 10, 11, 12, 13, 14 and 15. **This is a candidate list, not a defect list.** Citing an exercise for attribution is fine; a proof that *depends* on one is the rule this book has broken and repaired seven times. Each site needs reading. The two Chapter 15 §01 entries were triaged during that chapter's referee pass and are attribution only

### Chapter 17 (convexity)

- [x] Ch 15 → Ch 17 §04: **dual norms** (`def-dual-norm`, `thm-dual-dual-norm`; pairs 1↔∞ and 2↔2 in §04, general p in §11's `thm-dual-p-norm`). Ch 15's outline and blueprint listed them, but Ch 15 never defined one (and makes no claim to). Ch 17 §04 delivers `def-dual-norm` and ‖·‖** = ‖·‖
- [x] Ch 16 §06 → Ch 17 §10: a pointwise supremum of linear functions is convex (`prp-sup-of-affine-convex`, quoted verbatim)
- [x] Ch 15 §01 → Ch 17 §11: Minkowski's inequality. Ch 15 said the book "does not prove and never uses" it; Ch 17 §11 proves it from Hölder (`cor-minkowski-inequality`) and uses it for the dual p-norms, so the Ch 15 sentence was updated to point there (a pointer update, as Ch 15 §08's Eckart–Young pointer was for Ch 16)
- Ch 15 §01 wrote \( |x_i|^p \) and the exponent \( 1/p \) for real p without defining real powers; the book had **no logarithm**. Ch 17 §11 builds log from Ch 9 §09's exp (`lem-exp-log`) and defines \( t^r = e^{r\log t} \). Ch 15's use was a remark, not a proof step
- [x] Ch 2 §07 → Ch 17 §06: inequalities and linear programming (`exm-traffic-lp`; Ch 2 names no chapter)
- [x] Ch 13 §06 said nothing later depends on its imported (A1) symmetry / (A2) Taylor; Ch 17 §10's `thm-convex-second-derivative` does, so the Ch 13 sentence was updated (a pointer update, like the Minkowski one)
- [ ] Ch 17 §10 → Ch 20: A ↦ tr f(A) is convex for convex f (plan: "Convex and Schur-convex functions")
- [x] Ch 17 §04 (~line 344): an earlier draft promised §10 a circular "second proof of the triangle inequality" from `cor-norm-as-max`; the final text says only that norms are examples of a max of linear functions, and the revision adds that their convexity was already the triangle inequality

### Chapter 16 (variational principles and interlacing)

Discharged (to be confirmed by referee):
- [x] Ch 11 §02 → Ch 16 §§01–02: the optimization description of every eigenvalue of a self-adjoint operator (`cor-courant-fischer-operator`). No analytic fact is *invoked*; the analysis underneath is the fundamental theorem of algebra (Ch 5 §05, via the extreme value theorem), which the spectral theorem rests on
- [ ] **M7, overclaim in deployed text:** Ch 11 §02 (~line 110) says it avoided the extreme value theorem "so that nothing in this chapter depends on it". Chapter 11 depends on it through the fundamental theorem of algebra. Not edited, since the text is deployed and outside this chapter; reword in the whole-book pass
- [x] Ch 12 §05 → Ch 16 §02: λ_i(A) ≥ λ_i(B) for every i when A ⪰ B (`cor-loewner-eigenvalue-monotone`)
- [x] Ch 12 §12 → Ch 16 §01: eigenvalues as extrema of ⟨Ax, x⟩
- [x] Ch 15 §07 → Ch 16 §03: Hermitian eigenvalues move by at most ‖E‖₂ (`cor-weyl-perturbation`)
- [x] Ch 12 §10 and Ch 15 §08 → Ch 16 §09: the spectral-norm Eckart–Young (`thm-eckart-young-spectral`)
- [x] Ch 10 §10 → Ch 16 §04: strict interlacing of the zeros of consecutive orthogonal polynomials (`cor-orthogonal-polynomial-zeros-interlace`). **Missed by the blueprint.** Ch 10 had only *asserted*, inside an exercise solution, that p_k is the characteristic polynomial of the Jacobi matrix; §04 proves it
- [x] Ch 12 §10 → Ch 16 §06: `lem-orthonormal-capture-bound` recovered as a special case of Ky Fan (`cor-capture-bound-revisited`); the text now says *special*, not *extreme*

Created:
- [ ] Ch 16 §01 → Ch 23: Rayleigh quotient iteration
- [ ] Ch 16 §08 → Ch 18: Birkhoff's theorem on doubly stochastic matrices (no longer needed for Horn; the plan has it in Ch 18 in its own right). **Ch 17 §08 defines `def-doubly-stochastic` (Ω_n), proves the permutation matrices are extreme, and states Birkhoff in two equivalent forms with the equivalence proved — Ch 18 need only prove one form**
- [x] Ch 16 §08: Horn's converse is **proved in §08** (`lem-horn-two-by-two`, `thm-horn`, `thm-schur-horn`), by induction from a 2×2 rotation. It was first deferred to Ch 20 on the false premise that it needs Birkhoff; the approved outline puts Schur–Horn in Ch 16
- [ ] Ch 16 §08 → Ch 20: Schur-concavity of the product (x ≺ y, non-negative ⟹ ∏xᵢ ≥ ∏yᵢ) and Schur-concave functions in general
- [ ] Ch 16 §09 → Ch 19: the Hermitian dilation, used for singular-value perturbation (§10's exercises already use it)
- Ch 12 → Ch 19 "perturbation of singular values" is now **partly** paid by Ch 16 §09's `cor-singular-value-perturbation` (|σᵢ(A+E) − σᵢ(A)| ≤ ‖E‖₂, no hypothesis on E); Chapter 19 keeps the rest
- [ ] Ch 16 §09 → Ch 20: Eckart–Young in every unitarily invariant norm (restates Ch 12 §10's promise)
- [ ] Ch 16 §06 → Ch 17: a pointwise supremum of linear functions is convex (the plan's "Convex functions")
- [ ] Ch 16 §06 → Ch 20: the Ky Fan partial sums applied to singular values, i.e. the Ky Fan k-norms (plan: "Unitarily invariant norms", "Ky Fan dominance")
- [ ] Ch 16 §07 → Ch 20: from λ(A)−λ(B) ≺ λ(A−B) (proved in full in §07), the consequences Σφ(xᵢ) ≤ Σφ(yᵢ) for every convex φ and the matching statement for unitarily invariant norms. φ(t) = |t| is §07 exercise C2. This is what §11 means by "the strongest form of Lidskii"
- [ ] Ch 16 §11 → Ch 20: Loewner's theorem (`thm-loewner-statement`), both directions
- [ ] Ch 16 §11 → Ch 20: t^p operator monotone on (0,∞) for 0 < p < 1, and not for p > 1. Only p = 1/2 (text) and p = 1/2^k (exercise C1) are proved

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
- [ ] Ch 15 §07 → Ch 19: Bauer–Fike (§07's exercise C1 is its engine and could be moved there)
- [ ] Ch 15 §08 → Ch 16: the spectral-norm Eckart–Young that Ch 12 §10 could not state (Ch 16 §09 proves it from the min–max for singular values; the Ch 15 text originally sent this to Ch 20 and was corrected)
- [ ] Ch 15 §08 → Ch 20: unitarily invariant norms, and the Eckart–Young theorem for all of them at once
- [ ] Ch 15 §08 → Ch 23: the conditioning of the least-squares *problem* (which involves the residual, not just κ₂(A)); the floating-point model and backward error analysis; the digit-loss comparison between the normal equations and QR
- Maintenance hazard: Ch 15 §06 cites Chapter 9 §09's imported analysis facts by **number** — (A1), (A4), (A5) — and that list is a plain enumerate with no labels. The three numbers are correct today (checked), but renumbering or inserting an item in Ch 9 §09 would break Ch 15 silently. Same pattern for Ch 15's own (A1)–(A4) list, cited from §§01–06
- **OUTSTANDING, and older than this chapter:** Ch 11 §10 says the positive definite solution of the Lyapunov equation "is the subject of Chapter 12", and **Chapter 12 never proves it** — "Lyapunov" appears nowhere in Ch 12. Ch 15 §06 delivers the decay half and the conditional half (any positive definite X solving it makes x*Xx decrease), and states in its own text that the existence half is not proved in the book. The Ch 11 §10 sentence still points readers at Chapter 12; **a proposed rewording of it was declined, so the misdirection stands in the deployed text and is recorded here instead**. The usual proof integrates `e^{tA*}Q e^{tA}` over `[0, ∞)`, which needs matrix-valued integrals the book does not set up. **Exactly what Ch 15 does establish** (refereed): `thm-exponential-decay` gives the decay of every solution of `ẋ = Ax` for stable `A`, with an explicit rate, and uses no Lyapunov equation at all; `exr-matrix-exponential-and-calculus-c3` shows that `x*Xx` strictly decreases along every non-zero solution **given** a positive definite `X` solving the equation — but that is an exercise, not body text. The existence of such an `X` is proved nowhere in the book, and §06 says so in its own text
