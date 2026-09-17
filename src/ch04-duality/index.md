# Duality

A linear map \( V \to F \) turns each vector into a single number. The \( i \)-th coordinate in a basis does this, and so do evaluating a polynomial at a point, integrating a function, and taking the trace of a matrix. These **linear functionals** are the measurements we can make on a vector space, and together they form a vector space of their own, the dual space \( V^{*} \).

The dual space mirrors \( V \) with every inclusion reversed. A subspace corresponds to the functionals that vanish on it. An injective map corresponds to a surjective one. The kernel of a map corresponds to the image of its dual map, whose matrix is the transpose. Passing to the dual turns a hard question into an easy one surprisingly often. It also explains facts we already know from a new angle: why a subspace of \( F^n \) is always the solution set of a homogeneous system, and why row rank equals column rank.

**What you need.** From Chapter 1, bases, dimension and complements (@def-basis, @def-dimension, @thm-complement-exists), and bases of infinite-dimensional spaces (@thm-basis-extension-general) for the remarks on infinite dimension. From Chapter 2, the row space and null space of a matrix (@def-row-space, @def-null-space) and inverses by row reduction (@thm-inverse-by-row-reduction). From Chapter 3, linear maps and the space \( \cL(V, W) \) (@def-linear-transformation, @thm-linear-maps-vector-space), the Rank–Nullity Theorem (@thm-rank-nullity), the matrix of a map and change of basis (@def-matrix-of-linear-map, @thm-change-of-coordinates), and quotient spaces with the First Isomorphism Theorem (@def-quotient-space, @thm-first-isomorphism).

## Roadmap

- **Linear functionals and the dual space.** Measurements as vectors; dual bases; separating vectors by functionals.
- **Annihilators.** The functionals that vanish on a subspace, and the formula \( \dim U + \dim U^{0} = \dim V \).
- **The double dual.** A natural isomorphism \( V \to V^{**} \) that needs no basis, and what "natural" means.
- **The dual map and the transpose.** Pulling functionals back along a map; its matrix is the transpose; kernels and images trade places.
- **Duality for subspaces and quotients.** The dual of a subspace is a quotient of the dual, and the dual of a quotient is an annihilator; hyperplanes and codimension.
- **Hyperplanes and linear systems revisited.** Every subspace is cut out by equations; converting between parametric and implicit descriptions.

## Named moves

- **Test against functionals.** To show a vector is zero, show that every functional (or every vector of a dual basis) sends it to zero.
- **Pass to the dual and count.** Replace a subspace by its annihilator and use \( \dim U + \dim U^{0} = \dim V \).
- **Natural or chosen?** Ask whether an isomorphism needs a basis. \( V \cong V^{*} \) does; \( V \cong V^{**} \) does not.
- **Dualize a statement.** Injective becomes surjective, kernel becomes image, a matrix becomes its transpose, and inclusions reverse.
