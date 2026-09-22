# Perturbation Theory

Every matrix that comes from a measurement or a computation is slightly wrong, so the eigenvalues one actually knows are those of a nearby matrix \( \A + \E \). Two earlier chapters began to say what that costs. Chapter 15 showed that the eigenvalues move continuously with the matrix (@cor-eigenvalues-continuous), and that "continuously" can be very bad: a perturbation of size \( \varepsilon \) moves the eigenvalue of a \( k \times k \) Jordan block by \( \varepsilon^{1/k} \) (@exm-jordan-block-perturbation). Chapter 16 showed that Hermitian matrices are as good as one could hope: each eigenvalue moves by at most \( \norm{\E}_2 \) (@cor-weyl-perturbation). Most matrices are neither Jordan blocks nor Hermitian, and this chapter handles them. It asks four questions.

- **Where are the eigenvalues,** before any of them is computed? Discs and ovals read off the entries, and the numerical range, locate them.
- **How far do they move** when \( \A \) is not Hermitian? For every matrix there is a bound with an \( n \)-th root, and the Jordan block shows that the root cannot be removed. For a diagonalizable matrix, the Bauer–Fike theorem gives a bound proportional to \( \norm{\E} \), with a factor that measures how far the eigenvectors are from orthonormal.
- **Which eigenvalue goes where?** A bound saying that each new eigenvalue is near **some** old one does not say that they can be paired off. For normal matrices they can, and the pairing comes from Birkhoff's theorem of Chapter 18.
- **What happens to the rest?** Eigenvectors and invariant subspaces, singular values, and the factors of the polar decomposition all move, and the chapter bounds each of them. It ends with the first-order sensitivity of a single simple eigenvalue.

One result settles an old account. Chapter 15 quoted the theorem that the roots of a polynomial depend continuously on its coefficients (@thm-roots-depend-continuously) and left the proof to this chapter. §03 gives it from compactness and unique factorization alone, so @cor-eigenvalues-continuous, and everything Chapter 15 built on it, now rests on a proved theorem.

**The field is \( \nC \)** throughout, unless a statement says \( \nR \). A real matrix is read in \( M_n(\nC) \) when its eigenvalues are wanted. Three conventions hold in every section.

- **The perturbation is \( \E \),** and the perturbed matrix is \( \A + \E \), as in Chapters 15 and 16. A different letter, \( \widetilde\A \), is used only where the perturbed matrix is not naturally written as a sum.
- **Every bound names its norm.** \( \norm{\cdot}_2 \) is the spectral norm and \( \norm{\cdot}_F \) the Frobenius norm. A norm without a subscript means an arbitrary operator norm, and it is written that way only where the statement holds for all of them. There is one other use, announced where it starts: in §§09–10 a norm without a subscript stands for either the spectral or the Frobenius norm, the same one throughout the statement, and there it ranges over just those two.
- **Near some eigenvalue is not the same as matched.** "Every eigenvalue of \( \A + \E \) lies within \( r \) of some eigenvalue of \( \A \)" is a one-sided statement. "The eigenvalues can be **numbered** so that each pair is within \( r \)" is a matching, and it is stronger. §§03–05 are largely about the difference, and the chapter never blurs it.

## The analysis this chapter imports

The list is Chapter 15's, facts (A1)–(A6) of that chapter's introduction, together with the algebra of limits, and each fact is named again where it is used. Two carry most of the weight. **(A3)**, compactness of closed bounded sets, is the engine of §03's proof of the continuity of roots, and it is also what makes the numerical range of §02 compact. **(A5)**, the intermediate value theorem, gives the convexity of the numerical range in §02. **(A4)**, the extreme value theorem, is used once, also in §02, to know that the numerical radius — the largest modulus on the numerical range — is attained. §03's counting theorem needs one more fact, that an integer-valued function on an interval that is locally constant is constant, and it derives this from (A5) as well. Nothing else analytic is used. In particular, the first-order formula of §11 for the derivative of a simple eigenvalue is proved without the implicit function theorem.

## What you need

- **Chapter 5** — polynomials over \( \nC \): @cor-complex-polynomial-splits, @thm-unique-factorization-polynomials, @thm-repeated-root-derivative.
- **Chapter 6** — determinants, the adjugate and minors: @def-adjugate, @thm-adjugate-identity, @thm-rank-via-minors, @thm-charpoly-coefficients, @thm-charpoly-root-iff-singular, @thm-det-block-triangular.
- **Chapter 7** — block matrices and the Kronecker and vec identities: @thm-block-multiplication, @thm-vec-identity.
- **Chapter 8** — eigenvalues, multiplicities, diagonalization and left eigenvectors: @thm-eigenvalue-characterizations, @def-algebraic-multiplicity, @thm-geometric-le-algebraic, @def-diagonalizable, @thm-diagonalization, @def-left-eigenvector, @prp-left-eigenvectors-transpose, @prp-left-right-eigen-expansion.
- **Chapter 9** — the Jordan form, and its warning that the form is unstable: @thm-jordan-canonical-form, @def-jordan-block.
- **Chapter 10** — inner products, orthogonal projections and unitary maps: @thm-cauchy-schwarz, @def-orthogonal-projection, @thm-orthogonal-decomposition, @cor-extend-orthonormal-basis, @thm-isometry-characterizations.
- **Chapter 11** — Schur's theorem, the spectral theorem, the Sylvester equation and the departure from normality: @thm-schur-triangularization, @cor-spectral-complex-matrix, @thm-normal-eigenvector-shared, @def-sylvester-operator, @thm-sylvester-equation, @cor-block-diagonalization, @lem-frobenius-unitarily-invariant, @def-departure-from-normality, @exm-eigenvalue-sensitivity.
- **Chapter 12** — the singular value and polar decompositions, and Hadamard's inequality: @thm-svd, @def-singular-values, @thm-polar-decomposition, @thm-hadamard-inequality.
- **Chapter 15** — operator norms, the Neumann series, continuity of eigenvalues and condition numbers: @def-operator-norm, @thm-operator-norm-properties, @thm-operator-norm-formulas, @thm-neumann-series, @lem-entrywise-polynomial-continuous, @thm-roots-depend-continuously, @cor-eigenvalues-continuous, @exm-jordan-block-perturbation, @def-condition-number.
- **Chapter 16** — the Rayleigh quotient, Weyl's inequalities, Lidskii's inequality, majorization, the Hermitian dilation, and §10's law of inertia for Hermitian matrices: @def-rayleigh-quotient, @thm-courant-fischer, @thm-weyl-inequalities, @cor-weyl-perturbation, @thm-lidskii-inequality, @def-majorization, @prp-hermitian-dilation, @cor-singular-value-perturbation, @def-inertia-triple, @thm-inertia-second-proof.
- **Chapter 17** — extreme points, and linear functions on compact convex sets: @def-extreme-point, @cor-linear-max-at-extreme.
- **Chapter 18** — irreducible matrices, and Birkhoff's theorem: @def-irreducible, @thm-irreducible-iff-strongly-connected, @thm-birkhoff.

## Roadmap

- **Gershgorin discs.** Every eigenvalue lies in a union of discs read off the rows, a diagonal rescaling moves the discs, and an irreducible matrix can have an eigenvalue on the boundary only if it lies on every circle.
- **Other inclusion regions.** Brauer's ovals, which are never worse than the discs, and the numerical range: it contains the spectrum, it is convex by the Toeplitz–Hausdorff theorem, and it equals the convex hull of the eigenvalues for a normal matrix.
- **Continuity of roots.** Chapter 15's quoted theorem, proved by compactness. Elsner's bound, with its exponent \( 1/n \) shown to be sharp by a Jordan block, and its matching version. The counting theorem: a group of Gershgorin discs separated from the others contains exactly as many eigenvalues as discs.
- **The Bauer–Fike theorem.** For a diagonalizable matrix, each perturbed eigenvalue lies within \( \kappa_2(\X)\norm{\E}_2 \) of an old one, with factor \( 1 \) for a normal matrix. It comes with a residual bound for computed eigenpairs and a version with an \( m \)-th root for defective matrices.
- **The Hoffman–Wielandt theorem.** The eigenvalues of two normal matrices can be matched within their Frobenius distance, by Birkhoff's theorem. The inequality fails for non-normal matrices.
- **Hermitian perturbations.** Residual bounds, the Kato–Temple bound, which is quadratic in the residual, and Ostrowski's theorem, which says that a congruence changes each eigenvalue by a bounded relative factor.
- **The Sylvester equation, quantitatively.** The separation of two matrices, which measures how badly conditioned \( \A\X - \X\B = \Y \) is. For normal matrices it is the distance between the spectra, and in general it can be much smaller. Bounds for separated Hermitian spectra follow.
- **Principal angles.** The angles between two subspaces, their sines, and the distance \( \norm{P_U - P_W}_2 \) between the orthogonal projections.
- **The Davis–Kahan theorem.** An invariant subspace of a Hermitian matrix moves by at most the perturbation divided by the spectral gap. Single eigenvectors inside a cluster may not be stable, but the subspace of the whole cluster is.
- **Singular values and polar factors.** Mirsky's Frobenius bound for singular values, and bounds for the positive and the unitary factors of the polar decomposition of an invertible matrix.
- **Condition numbers of eigenvalues.** The derivative of a simple eigenvalue, from a right and a left eigenvector, and its worst size, which is the condition number. The chapter's summary closes this section.

## Named moves

- **Dominant coordinate plus the triangle inequality.** Read the eigen-equation at the coordinate where the eigenvector is largest.
- **A determinant bounded two ways.** A product of distances to the eigenvalues is a determinant, and Hadamard's inequality bounds it by column lengths.
- **Compactness plus uniqueness.** Bound the roots, extract a convergent subsequence, and let unique factorization identify the limit.
- **An integer-valued continuous function is constant.** Count eigenvalues along a path on which none of them can escape the region.
- **Factor out the resolvent.** Write \( \A + \E - \mu\I = (\A - \mu\I)\bigl(\I + (\A - \mu\I)^{-1}\E\bigr) \) and invert the second factor by the Neumann series.
- **Birkhoff turns a doubly stochastic weight into a permutation.** Minimize a linear function over the doubly stochastic matrices, and the minimum sits at a permutation.
- **The perturbation of a subspace is a Sylvester equation.** The block coupling an invariant subspace to the new complement solves one, so the spectral gap is the conditioning.
- **The singular-pair trick.** Test a matrix equation against the top singular pair of the unknown.
- **The adjugate as a polynomial eigenvector.** A column of \( \adj(\mu\I - \B) \) is an eigenvector whose entries are polynomials, so it moves continuously with the data.
