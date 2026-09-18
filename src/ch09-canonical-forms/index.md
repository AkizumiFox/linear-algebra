# Canonical Forms

Chapter 8 left one question open. Two matrices represent the same operator in different bases exactly when they are similar, and we can now decide similarity in easy cases: diagonalizable matrices are similar precisely when they have the same eigenvalues with the same multiplicities. But the matrices \( \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) and \( I_2 \) share their characteristic and minimal polynomials, their rank, their trace and their determinant, and they are still not similar. Something is missing.

This chapter supplies it. When the characteristic polynomial splits, every operator has a **Jordan form**: a direct sum of blocks with one eigenvalue on the diagonal and ones just above it, unique up to the order of the blocks. Two matrices are similar exactly when their Jordan forms agree, so the similarity problem is solved. Over a field where the polynomial does not split, the **rational canonical form** does the same job, and the Smith normal form of \( x\I - \A \) computes it. The chapter closes with what these forms are for: functions of matrices, the exponential \( e^{t\A} \) and linear differential equations, and a complete answer to when the powers \( \A^m \) converge.

**What you need.** From Chapter 1, direct sums, basis extension and complexification (@thm-direct-sum-k-criteria, @thm-basis-extension, @def-complexification). From Chapter 5, the arithmetic of \( F[x] \): division, gcds, Bézout and unique factorization (@thm-polynomial-division, @cor-bezout-polynomials, @thm-unique-factorization-polynomials), and interpolation (@thm-crt-polynomials). From Chapter 6, determinants of block triangular matrices, Cauchy–Binet and the companion matrix of a monic polynomial (@thm-det-block-triangular, @thm-cauchy-binet, @exr-characteristic-polynomial-c1). From Chapter 8, the minimal polynomial, primary decomposition and triangularization (@def-minimal-polynomial, @thm-primary-decomposition, @thm-triangularization).

## Roadmap

- **Generalized eigenspaces.** Enlarging an eigenspace until it is big enough, and the decomposition it produces.
- **Nilpotent operators.** Chains of vectors, the block structure they give, and how ranks of powers determine it.
- **The Jordan canonical form.** Existence, uniqueness, and the complete answer to the similarity question over a splitting field.
- **The real Jordan form and the Weyr form.** Avoiding complex numbers for a real matrix, and a rearrangement of the Jordan form with its own uses.
- **Cyclic subspaces and companion matrices.** One vector and its images can generate everything.
- **The rational canonical form.** A canonical form over every field, with invariant factors as the complete invariants.
- **Polynomial matrices and the Smith normal form.** Row and column operations on \( x\I - \A \) compute the invariant factors.
- **Semisimple operators and the Jordan–Chevalley decomposition.** Every operator splits uniquely into a diagonalizable part plus a commuting nilpotent part.
- **Functions of matrices, the exponential and linear differential equations.** \( f(\A) \) from the Jordan form, and \( x' = \A x \) solved by \( e^{t\A} \).
- **Convergent and power-bounded matrices.** Exactly when \( \A^m \) converges, and to what.

## Named moves

- **Enlarge the kernel.** When \( \ker(T - \lambda I) \) is too small, pass to \( \ker(T - \lambda I)^k \) until the chain stops growing.
- **Reduce to the nilpotent case.** On each generalized eigenspace, \( T - \lambda I \) is nilpotent, so the whole structure question is about nilpotent operators.
- **Read the chain off the columns.** The columns of a Jordan block say \( N\v_1 = \0 \) and \( N\v_{j} = \v_{j-1} \): a chain.
- **Count ranks of powers.** The block sizes are second differences of \( \rank N^j \), so they can be found without finding a single chain.
- **A cyclic vector gives a companion matrix.** If \( \v, T\v, \dots \) span, the matrix of \( T \) is built from one polynomial.
