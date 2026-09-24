# Linear Systems and Matrices

Chapter 1 kept asking questions that end in a system of equations. Is this vector in the span of those? Is this list independent? Extend this list to a basis. Each time we solved a small system by hand and promised a systematic method. This chapter keeps that promise. Every question about finitely many vectors in \( F^n \) turns into a linear system, and linear systems have a complete algorithm: Gaussian elimination.

We do not treat the algorithm as a recipe. We prove that row operations never change the answer, that the fully reduced form of a matrix does not depend on the choices made along the way, and that the numbers it produces, pivots and free variables, measure exactly the dimensions of Chapter 1. Along the way the invertible matrices get their first full characterization, and we prove a fact Chapter 0 had to postpone: for square matrices, \( \A\B = \I \) already forces \( \B\A = \I \).

**What you need.** From Chapter 0, matrix multiplication read column by column (@thm-matrix-times-vector-columns) and invertible matrices (@def-invertible-matrix). From Chapter 1, span (@def-span), linear independence (@def-linear-independence), bases (@def-basis) and dimension (@def-dimension).

## Roadmap

- **Three views of a linear system.** Intersecting lines and planes, combinations of columns, and a single matrix equation; the shape of the solution set as a particular solution plus the homogeneous solutions.
- **Gaussian elimination.** Row operations, echelon and reduced echelon forms, and how to read the solutions off the reduced form.
- **Uniqueness of the reduced form.** Different sequences of row operations always reach the same reduced matrix, so pivot columns are well defined.
- **Elementary matrices and inverses.** Row operations as left multiplication, the invertible matrix theorem, computing inverses by row reduction, and the permutation matrices that later chapters use to relabel coordinates.
- **Rank.** Row space, column space and null space; row rank equals column rank; the Rouché–Capelli theorem; and a toolkit for the questions of Chapter 1.
- **LU factorization.** Storing elimination as a product of triangular matrices, with and without row swaps.
- **Applications.** Polynomial interpolation, balancing chemical equations, networks, and a puzzle over \( \nF_2 \).

## Named moves

- **Row operations do not change the solution set.** So simplify first, then read the answer.
- **Put it in reduced form, then read off.** Consistency, free variables, bases of the column, row and null spaces all come from the reduced row echelon form.
- **A question about vectors is a question about a matrix.** Put the vectors in as columns; independence, spanning and membership become statements about pivots.
- **Pivots count dimensions.** The number of pivots is the rank, and the free variables count the dimension of the null space.
