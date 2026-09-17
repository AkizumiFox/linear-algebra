# Linear Maps

Chapter 1 studied vector spaces one at a time. This chapter studies the functions between them that respect the structure: **linear maps**, the functions that send sums to sums and scalar multiples to scalar multiples. Differentiation of polynomials, the trace of a matrix, a rotation of the plane and multiplication by a matrix are all linear maps, and one theory covers them all.

Two subspaces measure how far a linear map is from being injective and surjective: its kernel and its image. The Rank–Nullity Theorem ties their dimensions together, and turns many questions about maps into counting. Then we choose bases and write every linear map as a matrix. This explains why matrix multiplication is defined the way it is, and it raises the central question of the rest of the book: how does the matrix change when the bases change, and how simple can we make it?

**What you need.** From Chapter 1, bases and dimension (@def-basis, @def-dimension), basis extension (@thm-basis-extension) and counting instead of checking (@thm-right-size-basis). From Chapter 2, the null space and column space of a matrix (@def-null-space, @def-column-space), its rank (@def-rank-matrix, @thm-rank-nullity-matrix) and the invertible matrix theorem (@thm-invertible-tfae). From Chapter 0, quotient sets and well-defined functions on them (@thm-well-defined-on-quotient), for the section on quotient spaces.

## Roadmap

- **Linear maps.** The definition, a gallery of examples and non-examples, and the fact that a linear map is determined by its values on a basis.
- **Kernel and image.** The two subspaces attached to every linear map, and the kernel test for injectivity.
- **The Rank–Nullity Theorem.** \( \dim V = \nullity T + \rank T \), and what counting can decide.
- **The algebra of linear maps.** Adding, scaling and composing maps; polynomials in an operator.
- **Isomorphisms.** When two spaces are "the same", and why dimension alone decides it.
- **The matrix of a linear map.** Coordinates turn maps into matrices and composition into matrix multiplication.
- **Change of basis and similarity.** How the matrix of a map depends on the chosen bases.
- **Rank, equivalence and factorizations.** With free choice of bases on both sides, every matrix becomes \( \begin{pmatrix} I_r & 0 \\ 0 & 0 \end{pmatrix} \).
- **Products and quotient spaces.** Building new spaces from old ones, and the isomorphism theorems.
- **Projections and the trace.** Direct sums seen through operators, and a basis-free trace.

## Named moves

- **Injective via the kernel.** To show \( T \) is injective, show \( T\v = \0 \) forces \( \v = \0 \).
- **Count with Rank–Nullity.** When \( \dim V = \dim W \), injective, surjective and bijective are the same; check the easiest one.
- **Basis of the kernel, then extend.** The proof pattern behind Rank–Nullity, the same one that proved the dimension formula for sums.
- **Abstract space → write down a matrix.** Choose a basis that makes the map simple, then compute with its matrix.
- **The change-of-basis square.** Go around the square instead of across it: \( [T]_{\sB'} = P^{-1}[T]_{\sB}P \).
- **Check well-definedness on cosets.** Every operation on a quotient space, and every map out of one, starts with this check.
