# Block Matrices

A large matrix often has structure that its entries hide. Split it into blocks, smaller matrices arranged in a grid, and the structure shows. A direct sum of subspaces becomes a block-diagonal matrix. A subspace that an operator maps into itself becomes a block of zeros in the corner. A system of equations that splits into two groups becomes a two-by-two system whose "entries" are matrices.

This chapter makes block arithmetic rigorous and then puts it to work. Multiplying block by block, eliminating a whole block at once, and taking the Schur complement \( \D - \C \A^{-1}\B \) turn statements about big matrices into statements about small ones: ranks, determinants and inverses. The Kronecker product rewrites matrix equations such as \( \A \X + \X \B = \C \) as ordinary linear systems. The chapter ends with a question that looks like it needs heavy machinery but does not: which matrices can be written as a commutator \( \X \Y - \Y \X \)?

**What you need.** From Chapter 0, matrix multiplication (@def-matrix-multiplication) and polynomials without zero divisors (@cor-polynomial-no-zero-divisors). From Chapter 1, subspaces, spans and bases with the dimension formula for a sum (@thm-span-subspace, @thm-basis-extension, @thm-size-bounds, @thm-subspace-dimension, @prp-sum-of-spans, @thm-dimension-formula-subspace-dim), the unique representation of a vector in a basis (@thm-unique-representation, @thm-independence-unique-combination) and the direct sum criteria (@thm-direct-sum-k-criteria), which is what §01 reads off a block decomposition; §05 also uses the standard bases and the trace-free matrices as examples (@exm-standard-bases, @exm-trace-free-matrices, @thm-zero-product). From Chapter 2, rank (@def-rank-matrix). From Chapter 3, the matrix of a linear map and change of basis (@def-matrix-of-linear-map, @thm-change-of-basis-maps), quotient spaces (@def-quotient-space), the rank inequalities (@thm-sylvester-rank-inequality) and the trace (@def-trace-operator). From Chapter 6, determinants of block triangular matrices and the characteristic polynomial (@thm-det-block-triangular, @thm-charpoly-coefficients).

## Roadmap

- **Partitions and block multiplication.** Multiplying matrices block by block, and what block-diagonal and block-triangular shapes say about a linear map.
- **Rank and block matrices.** Rank inequalities proved by clearing blocks, including Frobenius's inequality.
- **Schur complements.** The Schur complement, the determinant, rank and inverse of a block matrix, the Woodbury formula, and determinants with commuting blocks over any field.
- **The Kronecker product.** A product of matrices of different sizes, and matrix equations turned into linear systems.
- **Commutators and trace-zero matrices.** Every trace-zero matrix over a field of characteristic zero is a commutator.

## Named moves

- **Partition to match the structure.** Choose the blocks so that the zeros you know about sit in whole blocks.
- **Eliminate a block.** Multiply by an invertible block triangular matrix to clear a block, just as a row operation clears an entry.
- **Pass to the Schur complement.** Reduce a question about \( \begin{pmatrix} \A & \B \\ \C & \D \end{pmatrix} \) with \( \A \) invertible to a question about \( \A \) and \( \D - \C \A^{-1}\B \).
- **Vectorize.** Turn a linear equation in an unknown matrix \( \X \) into a linear system in the entries of \( \X \).
- **Adjoin an indeterminate.** To remove an invertibility hypothesis, replace \( \D \) by \( \D + x\I \), work over \( F[x] \), and set \( x = 0 \) at the end.
