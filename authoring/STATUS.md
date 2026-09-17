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
| 7–23 | | see plan | not started |

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
- [ ] Ch 1 → Ch 8: eigenspaces of a diagonalizable operator give a direct sum
- [ ] Ch 1 → Ch 3: coordinate map is an isomorphism; shift map injective not surjective; (ℝⁿ)_ℂ ≅ ℂⁿ
- [ ] Ch 1 → Ch 8/11: complexification gives real matrices complex eigenvalues; used in real spectral theory
- [ ] Ch 2 → Ch 3, 6, 8, 12: invertible-matrix TFAE grows (kernel/image; det; eigenvalues; singular values)
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
- [ ] Ch 5 → Ch 8: minimal polynomial = monic generator of I_T (`thm-annihilator-ideal`); invariant subspaces defined; Cayley–Hamilton; primary decomposition via `thm-kernel-splitting` and `exr-polynomials-of-operators-c2`
- [ ] Ch 5 → Ch 9: canonical forms from primary decomposition
- [ ] Ch 5 → Ch 8: diagonalizable ⇔ minimal polynomial splits with distinct roots; every complex operator has an eigenvalue (FTA)
- Ch 6 §03: disjoint cycle decomposition only asserted (Ch 0 shows by example) — consider a short proof in M7.
- [ ] Ch 6 → Ch 8: (xI − A)·adj(xI − A) = det(xI − A)·I reappears (Cayley–Hamilton route)
- [ ] Ch 6 → Ch 7: Schur complements cite `thm-det-block-triangular`
- [ ] Ch 6 → Ch 8: eigenvalues from `thm-charpoly-root-iff-singular`; Cayley–Hamilton; p_AB = p_BA in general
- [ ] Ch 6 → Ch 9: complete similarity invariants
- [ ] Ch 6 → Ch 10/12: Gram matrices, √det(AᵀA) area via inner products
- [ ] Ch 6 → Ch 11: circulants of every size
- [ ] Ch 6 → Ch 23: matrix-tree theorem
