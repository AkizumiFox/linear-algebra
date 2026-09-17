# Determinants

A square matrix is invertible or it is not, and so far deciding which has meant row reducing it. The determinant packages that decision into a single number. The same number measures how the linear map scales areas and volumes, and its sign records whether the map preserves or reverses orientation. It also produces the characteristic polynomial, the gateway to eigenvalues in Chapter 8.

This chapter does not start from a formula. It starts from what a signed volume must do. Scaling one edge scales the volume. Sliding one edge along another does not change it. The unit cube has volume 1. We prove that exactly one function has these properties, write it down, and then derive every property of the determinant from that uniqueness: multiplicativity, the transpose rule, cofactor expansion, the inverse formula and Cramer's rule. Nothing is assumed, and no formula is used before it is proved.

**What you need.** From Chapter 0, permutations and transpositions (@thm-transpositions-generate) and the characteristic of a field (@def-characteristic). From Chapter 1, linear independence and the Linear Dependence Lemma (@def-linear-independence, @thm-linear-dependence-lemma). From Chapter 2, elementary matrices and the invertible matrix theorem (@def-elementary-matrix, @thm-invertible-tfae). From Chapter 3, the matrix of a linear map and similarity (@def-matrix-of-linear-map, @thm-similar-iff-same-operator). From Chapter 4, linear functionals (@def-linear-functional). From Chapter 5, the root bound for polynomials (@cor-root-bound-general).

## Roadmap

- **Signed area and volume.** Three rules that any reasonable notion of signed volume obeys, and the formula \( ad - bc \) forced by them.
- **Multilinear alternating forms.** The rules made precise for functions of \( n \) vectors, and their first consequences.
- **Permutations and sign.** Counting inversions, and why the parity of a permutation is well defined.
- **Existence and uniqueness of the determinant.** Exactly one alternating form takes the value 1 on the identity; the Leibniz formula.
- **Row operations and multiplicativity.** Computing determinants by elimination, \( \det(AB) = \det A \det B \), and the determinant of an operator.
- **Cofactor expansion, the adjugate and Cramer's rule.** Expanding along a row or column, and a formula for the inverse.
- **Minors, rank and Cauchy–Binet.** Rank read off from minors, and the determinant of a product of rectangular matrices.
- **Special determinants.** Vandermonde, tridiagonal and block triangular matrices, and rank-one updates.
- **Orientation and volume.** The determinant as a volume scaling factor, and the two orientations of \( \nR^n \).
- **The characteristic polynomial.** \( \det(xI - A) \), its coefficients, and why similar matrices share it.

## Named moves

- **Derive from the rules, not the formula.** Prove determinant facts from multilinearity, alternation and normalization, so no property is assumed before it is proved.
- **Uniqueness does the work.** To prove two expressions agree, show both are alternating multilinear in the columns and agree on the identity.
- **Build from elementary matrices.** Check a claim for elementary matrices, then extend it to products.
- **Look-alike matrices.** A matrix with two equal rows has determinant zero; expanding such a matrix proves the adjugate identity.
- **Induct on size.** Expand along a row or column to reduce an \( n \times n \) determinant to smaller ones.
