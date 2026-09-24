# Eigenvalues and Diagonalization

Chapter 4 showed that one operator has many matrices, one for each basis, and asked how simple the matrix can be made. This chapter answers the first half of that question. The simplest possible matrix is diagonal, and a matrix of an operator is diagonal exactly when every basis vector is only stretched, never turned. Such vectors are **eigenvectors**, and the stretching factors are **eigenvalues**.

Not every operator has enough eigenvectors, and the chapter explains precisely when it does. Two polynomials carry the information: the characteristic polynomial from Chapter 7 and the **minimal polynomial**, the smallest polynomial that kills the operator. The Cayley–Hamilton Theorem ties them together. When eigenvectors run short, operators over \( \nC \) can still be made triangular, and the space splits into pieces on which the operator is easier to understand. The chapter ends with what diagonalization is for: powers of matrices, linear recurrences such as the Fibonacci numbers, and the long-run behavior of Markov chains.

**What you need.** From Chapter 0, the arithmetic every computation here runs on: degree, evaluation and the absence of zero divisors in \( F[x] \) (@def-polynomial, @thm-degree-of-sum, @thm-degree-of-product, @cor-polynomial-no-zero-divisors, @thm-evaluation-respects-operations), field arithmetic (@thm-field-basic-properties) and conjugation (@thm-conjugate-properties), the matrix product with its three views, the transpose and polynomials of a matrix (@def-matrix-multiplication, @thm-matrix-multiplication-properties, @thm-matrix-times-vector-columns, @thm-three-views-of-product, @thm-transpose-properties, @def-polynomial-of-matrix), and that a composition of bijections is a bijection (@thm-composition-preserves). From Chapter 1, the dimension theory, used constantly: subspaces and intersections (@thm-subspace-test, @thm-intersection-subspaces), span and independence with the Linear Dependence Lemma (@def-span, @thm-linear-dependence-lemma, @thm-independence-unique-combination, @lem-append-independent, @thm-zero-product), bases and the counting arguments (@thm-unique-representation, @thm-basis-extension, @thm-right-size-basis, @thm-dim-impl-eq, @thm-size-bounds, @thm-subspace-dimension), and above all sums and direct sums (@thm-subspace-sum, @thm-direct-sum-k-criteria), since every decomposition theorem in the chapter is the claim that some sum is direct. From Chapter 3, that a one-sided inverse of a square matrix is two-sided (@thm-one-sided-inverse), and rank with Rank–Nullity for matrices (@thm-rank-nullity-matrix, @thm-row-rank-equals-column-rank). From Chapter 2, the matrix of a linear map, change of basis and similarity (@def-matrix-of-linear-map, @thm-change-of-basis-maps, @thm-similar-iff-same-operator), and quotient spaces (@def-quotient-space). From Chapter 6, polynomials of an operator, the ideal of polynomials that kill it, and the kernel splitting lemma (@thm-evaluation-homomorphism, @thm-annihilator-ideal, @thm-kernel-splitting), and the Fundamental Theorem of Algebra (@thm-fundamental-theorem-of-algebra). From Chapter 7, the characteristic polynomial and the adjugate (@def-characteristic-polynomial, @thm-adjugate-identity). From Chapter 8, block triangular matrices (@thm-invariant-subspace-block-triangular).

## Roadmap

- **Invariant subspaces.** Subspaces an operator maps into themselves, and the block triangular matrices they produce.
- **Eigenvalues and eigenvectors.** Directions that are only stretched; eigenvalues as roots of the characteristic polynomial; every complex operator has one.
- **Algebraic and geometric multiplicity.** Two ways to count a repeated eigenvalue, and why the second never exceeds the first.
- **Diagonalization.** Exactly when an operator has a basis of eigenvectors, and how to compute with one.
- **The minimal polynomial.** The monic polynomial of least degree that kills an operator, and why its roots are the eigenvalues.
- **The Cayley–Hamilton Theorem.** Every square matrix satisfies its own characteristic polynomial.
- **Triangularization.** An operator has a triangular matrix exactly when its characteristic polynomial splits.
- **Primary decomposition.** The factorization of the minimal polynomial splits the space, and decides diagonalizability.
- **Commuting operators.** Operators that commute share eigenvectors, and can be triangularized or diagonalized together.
- **Spectral mapping, AB and BA.** Eigenvalues of polynomials in an operator, and why \( \A \B \) and \( \B \A \) share their non-zero eigenvalues.
- **Powers, recurrences and Markov chains.** Diagonalization at work.

## Named moves

- **Ask when the matrix is diagonal.** Unwinding the columns of a diagonal matrix gives the eigenvector equation \( T\v = \lambda\v \).
- **Eigenvalue means a kernel.** \( \lambda \) is an eigenvalue exactly when \( T - \lambda I \) is not injective.
- **Apply \( T - \lambda I \) to a relation.** Kills one eigenvector and shortens a dependence, the heart of "distinct eigenvalues give independent eigenvectors".
- **Turn a relation into a divisibility.** If \( p(T) = 0 \), then the minimal polynomial divides \( p \).
- **One eigenvector, extend, recurse.** Split off an eigenvector, pass to the quotient, and use induction on dimension.
- **Search inside an eigenspace.** A commuting operator maps each eigenspace into itself, so look for a common eigenvector there.
