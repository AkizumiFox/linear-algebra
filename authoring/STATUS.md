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
| 13 | ch13-forms | Bilinear and quadratic forms | drafting |
| 14 | ch14-tensors | Tensors and exterior algebra | blueprint written |
| 15–23 | | see plan | not started |

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
- [ ] Ch 12 → Ch 20: operator monotone functions, unitarily invariant norms, the spectral-norm Eckart–Young
- [ ] Ch 12 → Ch 23: PCA and the numerical SVD

### Chapter 13 (bilinear and quadratic forms)

- [x] Ch 0 §07 → Ch 13 §03: "characteristic ≠ 2" earns its keep (`thm-alternating-vs-skew`, with the 𝔽₂ counterexample)
- [x] Ch 11 §05 and Ch 12 §04 → Ch 13 §05: why the signs of a congruent diagonal match the signs of the eigenvalues
- [x] Ch 12 §01 → Ch 13 §02: congruence studied for its own sake, with what it preserves and what it destroys
- [ ] Ch 13 §12 → Ch 14: tensor algebras; the construction of Cl(q) as a quotient of one; the independence half of `thm-clifford-dimension`. **Chapter 13 states that theorem with its gap marked in the text**, so this debt is visible to readers
- [ ] Ch 13 §09/§10 → nothing: the Pfaffian transformation rule and Sp(2m,F) ⊆ SL are recorded without proof and nothing may cite them
- Polish deferred to M7: Ch 13 §§07–08 have no labelled worked examples (`exm-`), and §10 has no Idea blocks, both against the STYLE checklist
