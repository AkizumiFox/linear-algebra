# Eigenvalues and Diagonalization

Chapter 3 showed that one operator has many matrices, one for each basis, and asked how simple the matrix can be made. This chapter answers the first half of that question. The simplest possible matrix is diagonal, and a matrix of an operator is diagonal exactly when every basis vector is only stretched, never turned. Such vectors are **eigenvectors**, and the stretching factors are **eigenvalues**.

Not every operator has enough eigenvectors, and the chapter explains precisely when it does. Two polynomials carry the information: the characteristic polynomial from Chapter 6 and the **minimal polynomial**, the smallest polynomial that kills the operator. The Cayley–Hamilton Theorem ties them together. When eigenvectors run short, operators over \( \nC \) can still be made triangular, and the space splits into pieces on which the operator is easier to understand. The chapter ends with what diagonalization is for: powers of matrices, linear recurrences such as the Fibonacci numbers, and the long-run behavior of Markov chains.

**What you need.** From Chapter 3, the matrix of a linear map, change of basis and similarity (@def-matrix-of-linear-map, @thm-change-of-basis-maps, @thm-similar-iff-same-operator), and quotient spaces (@def-quotient-space). From Chapter 5, polynomials of an operator, the ideal of polynomials that kill it, and the kernel splitting lemma (@thm-evaluation-homomorphism, @thm-annihilator-ideal, @thm-kernel-splitting), and the Fundamental Theorem of Algebra (@thm-fundamental-theorem-of-algebra). From Chapter 6, the characteristic polynomial and the adjugate (@def-characteristic-polynomial, @thm-adjugate-identity). From Chapter 7, block triangular matrices (@thm-invariant-subspace-block-triangular).

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
