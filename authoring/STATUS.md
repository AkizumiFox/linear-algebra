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
| 9 | ch09-canonical-forms | Canonical forms | drafting |
| 9–23 | | see plan | not started |

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
- [ ] Ch 2 → Ch 12: Cholesky
- [ ] Ch 2 → Ch 23: partial pivoting, rounding; graph Laplacian
- [x] Ch 2 → Ch 5: Lagrange interpolation formula
- [ ] Ch 2 → Ch 10: least squares

## Deferred to the whole-book pass (M7)

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
