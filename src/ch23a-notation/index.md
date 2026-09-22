# Notation

::: {.content-visible when-format="latex"}
\markboth{NOTATION}{NOTATION}
:::

This page is a reference, not a section: there is nothing to work through here, and it carries no exercises and no quick checks. Use it when you meet a symbol and want to know what it means and where the book fixed it. The symbols are grouped by the kind of thing they name, not by chapter, because a reader arrives with a symbol and not with a chapter number. Every entry links to the place where the book defines it; follow the link for the hypotheses, which a one-line gloss cannot carry.

Read the conventions first. Most of what looks like a clash between two symbols is resolved by one of them.

## The standing conventions

**The field.** \( F \) is an arbitrary field throughout, and \( \nF_p \) is the field with \( p \) elements (@def-field). Chapters 10 to 12 and much of Part V need \( \nR \) or \( \nC \), and say so where they do. Vector spaces are \( V, U, W \), plain italic, and are finite-dimensional unless the statement says otherwise.

**Bold is for matrices and vectors, never for maps or spaces.** A matrix is a bold upright capital, \( \A \); a vector is a bold lowercase letter, \( \v \); an operator or linear map is plain italic, \( T \); a space is plain italic, \( V \). Entries stay plain: \( a_{ij} \), or \( (\A)_{ij} \). A Greek letter naming a matrix is bold too, as \( \vLambda \) or \( \vSigma \).

**Maps and composition.** Linear maps are \( T, S \colon V \to W \), never \( f \). Composition is written \( ST \), and it means: first \( T \), then \( S \). For functions in general the book writes \( g \circ f \).

**Coordinates.** \( \coord{\v}{\sB} \) is the coordinate vector of \( \v \) in the ordered basis \( \sB \) (@def-coordinates), and \( \mtx{T}{\sB}{\sC} \) is the matrix of \( T \) with input basis \( \sB \) and output basis \( \sC \) (@def-matrix-of-linear-map). The subscript is the basis read into the first slot and the superscript the basis read into the second: for a map that is the input basis below and the output basis above, and for a bilinear form \( \mtx{\beta}{\sB}{\sB} \) it is the basis used on the first argument below and the one used on the second above. Both slots are always written out, even when they hold the same basis. A basis is an **ordered** list, written in parentheses.

**Transpose and adjoint.** \( \A\tp \) is the transpose (@def-transpose) and \( \A^{*} \) the conjugate transpose (@def-conjugate-transpose), which is also the symbol for the adjoint of an operator (@def-adjoint). The prime \( T' \) is the dual map (@def-dual-map), and never a derivative of a map.

**Inner products are linear in the first slot** and conjugate-linear in the second (@def-inner-product). Over \( \nR \) the distinction disappears.

**Ordering of eigenvalues and singular values.** For Hermitian \( \A \), the eigenvalues are listed **decreasing**, \( \lambda_1(\A) \ge \dots \ge \lambda_n(\A) \), with multiplicity. Singular values are listed decreasing as well, \( \sigma_1(\A) \ge \sigma_2(\A) \ge \dots \ge 0 \) (@def-singular-values). Where a proof wants the increasing order it says so.

**Indices start at 1**, with three announced exceptions: Chapter 11 §09, where circulant and Fourier subscripts run from \( 0 \) to \( n-1 \) and are read modulo \( n \); Chapter 21 §§06 to 10, where the coordinates of \( F^{n+1} \) run from \( 0 \) so that \( \nP^n(F) \) has dimension \( n \) (@def-homogeneous-coordinates); and Chapter 22 §09, which follows Chapter 11 §09 for group elements and characters.

**Defining, not asserting.** \( \coloneqq \) means "is defined to be". A plain \( = \) asserts an equality that has been or will be proved.

## Numbers, sets and fields

| Symbol | Meaning | Defined at |
|:-----------|:------------------------------|:-------------|
| \( \nN, \nZ, \nQ, \nR, \nC \) | natural numbers (with \( 0 \)), integers, rationals, reals, complex numbers | @def-common-number-sets |
| \( F \), \( \nF_p \) | a field; the field with \( p \) elements | @def-field |
| \( \operatorname{char} F \) | characteristic of a field: the least \( n > 0 \) with \( n \cdot 1 = 0 \), or \( 0 \) | @def-characteristic |
| \( \conj{z} \), \( \lvert z \rvert \) | complex conjugate and modulus | @def-conjugate-modulus |
| \( \{ x \in S : P(x) \} \) | set-builder notation, with a colon | @def-set-builder |
| \( \emptyset \), \( S \subseteq T \) | the empty set; inclusion | @def-empty-set, @def-subset |
| \( S \cup T \), \( S \cap T \), \( S \setminus T \), \( S^{c} \) | union, intersection, difference, complement | @def-union, @def-intersection, @def-set-difference |
| \( S \times T \), \( (x_1, \dots, x_n) \) | Cartesian product and \( n \)-tuples | @def-cartesian-product, @def-n-tuple |
| \( \powerset{S} \) | power set, the set of all subsets | @def-power-set |
| \( f \colon X \to Y \), \( x \mapsto f(x) \) | a function and its rule | @def-function |
| \( f(A) \), \( f^{-1}(B) \) | image of a subset, preimage of a subset | @def-image-preimage |
| \( g \circ f \), \( \id_X \), \( f^{-1} \) | composition, identity function, inverse function | @def-composition, @def-identity-function, @def-inverse-function |
| \( x \sim y \), \( [x] \), \( X/{\sim} \) | equivalence relation, equivalence class, quotient set | @def-equivalence-relation, @def-equivalence-class, @def-quotient-set |
| \( S_n \), \( \sgn(\sigma) \), \( \operatorname{inv}(\sigma) \) | symmetric group; sign of a permutation; number of inversions | @exm-groups, @def-sign-permutation, @def-inversion |
| \( A_n \) | alternating group, the even permutations | @def-alternating-group |
| \( F[x] \), \( F[x]_{\le n} \) | polynomials over \( F \); those of degree at most \( n \) | @def-polynomial-ring, @def-polynomials-bounded-degree |
| \( \deg p \), \( p(c) \) | degree; evaluation at a scalar | @def-degree, @def-polynomial-evaluation |
| \( p \mid q \), \( \gcd(p,q) \), \( \operatorname{lcm}(p,q) \) | divisibility, greatest common divisor, least common multiple in \( F[x] \) | @def-divisibility-polynomials, @def-gcd-polynomials, @def-lcm-polynomials |
| \( \langle p \rangle \) | the ideal of \( F[x] \) generated by \( p \): all multiples of \( p \) | @def-ideal-polynomials |
| \( \operatorname{mult}_c(f) \) | multiplicity of \( c \) as a root of \( f \) | @def-root-multiplicity |
| \( p' \) | formal derivative of a polynomial | @def-formal-derivative |
| \( \ell_i \) | Lagrange basis polynomial, \( \ell_i(c_j) = \delta_{ij} \) | @def-lagrange-basis |

## Spaces

| Symbol | Meaning | Defined at |
|:-----------|:------------------------------|:-------------|
| \( V, U, W \) | vector spaces over \( F \); \( U \) is usually a subspace | @def-vector-space, @def-subspace |
| \( F^n \), \( F^{S} \) | column vectors; **all** functions \( S \to F \) | @def-vector-space |
| \( F^{(S)} \) | the free vector space on \( S \): the **finitely supported** functions \( S \to F \) | @def-free-vector-space |
| \( M_{m \times n}(F) \), \( M_n(F) \) | matrices over \( F \) | @def-matrix |
| \( \Span(S) \) | span; the span of the empty set is \( \{\0\} \) | @def-span |
| \( \dim V \), \( \dim_F V \) | dimension, over \( F \) when the field matters | @def-dimension |
| \( \sB = (\v_1, \dots, \v_n) \) | an **ordered** basis; \( \sE \) is the standard basis | @def-basis, @exm-standard-bases |
| \( \coord{\v}{\sB} \) | coordinate vector of \( \v \) in \( \sB \) | @def-coordinates |
| \( U + W \), \( U \oplus W \) | sum of subspaces; internal direct sum | @def-sum-of-subspaces, @def-direct-sum |
| \( V \times W \) | product of vector spaces (the external direct sum) | @def-product-of-spaces |
| \( \v + U \), \( V/U \) | coset; quotient space | @def-coset, @def-quotient-space |
| \( \codim U \) | codimension, \( \dim V/U \) | @def-codimension |
| \( V^{*} \), \( \varphi \) | dual space; a linear functional, always a Greek letter | @def-dual-space, @def-linear-functional |
| \( \varphi_1, \dots, \varphi_n \) | the dual basis of \( \sB \) | @def-dual-basis |
| \( U^{0} \) | annihilator of \( U \) inside \( V^{*} \) | @def-annihilator |
| \( V^{**} \), \( \ev_{\v} \) | double dual; evaluation at \( \v \) | @def-evaluation-map |
| \( V_{\nC} \) | complexification of a real space | @def-complexification |
| \( \cF \) | a family of operators in \( \cL(V) \) | @def-simultaneously-diagonalizable |

## Vectors, matrices and their operations

| Symbol | Meaning | Defined at |
|:-----------|:------------------------------|:-------------|
| \( \v, \u, \w, \x, \y \) | vectors: bold lowercase | @def-vectors-scalars |
| \( \0 \), \( \1 \) | the zero vector; the all-ones vector | @def-vectors-scalars, @def-stochastic-matrix |
| \( \e_1, \dots, \e_n \) | the standard basis of \( F^n \) | @exm-standard-bases |
| \( \E_{ij} \) | matrix unit: \( 1 \) in entry \( (i,j) \), zeros elsewhere | @exm-standard-bases |
| \( \A, \B, \C \), \( a_{ij} \) | matrices, bold upright capitals; their entries, plain | @def-matrix |
| \( 0_{m \times n} \), \( \I \), \( \I_n \) | zero matrix, plain (bold \( \0 \) as a block); identity matrix | @def-zero-matrix, @def-identity-matrix |
| \( \delta_{ij} \) | Kronecker delta: \( 1 \) when \( i = j \), else \( 0 \) | @def-identity-matrix |
| \( \diag(d_1, \dots, d_n) \) | the diagonal matrix with these diagonal entries | @def-diagonal-matrix |
| \( \A\tp \), \( \A^{*} \) | transpose; conjugate transpose | @def-transpose, @def-conjugate-transpose |
| \( \tr \A \) | trace, the sum of the diagonal entries | @def-trace |
| \( \det \A \) | determinant | @def-determinant |
| \( \adj \A \) | adjugate, the transposed matrix of cofactors | @def-adjugate |
| \( M_{ij} \), \( C_{ij} \) | minor and cofactor \( (-1)^{i+j}M_{ij} \) | @def-minor-cofactor |
| \( \A^{-1} \) | inverse of a non-singular matrix | @def-invertible-matrix |
| \( p(\A) \) | a polynomial evaluated at a matrix | @def-polynomial-of-matrix |
| \( \P_{ij} \), \( \D_i(c) \), \( \I + c\E_{ij} \) | the three elementary matrices: swap, scale, add | @def-elementary-matrix |
| \( \P_{\sigma} \) | permutation matrix | @def-permutation-matrix |
| \( \A = \L\U \), \( \P\A = \L\U \) | the LU and PLU factorizations | @def-lu-factorization, @def-plu-factorization |
| \( \col(\A) \), \( \row(\A) \), \( \nul(\A) \) | column space, row space, null space | @def-column-space, @def-row-space, @def-null-space |
| \( \rank \A \), \( \nullity \A \) | rank and nullity of a matrix | @def-rank-matrix, @def-nullity-matrix |
| \( \A \sim \B \) | similar: \( \B = \P^{-1}\A\P \) | @def-similar-matrices |
| \( \A \simeq \B \) | congruent: \( \B = \P\tp\A\P \) | @def-congruent |
| \( \A \approx \B \) | equivalent over \( F[x] \): \( \B = \U\A\V \) with \( \U, \V \) invertible over \( F[x] \) | @def-polynomial-matrix-equivalence |
| equivalent matrices | \( \B = \Q\A\P \) with \( \P, \Q \) non-singular | @def-equivalent-matrices |
| \( \A \oplus \B \) | block diagonal matrix with the given square diagonal blocks | @def-block-diagonal |
| \( \M/\A \), \( \M/\D \) | Schur complement of an invertible block of a block matrix | @def-schur-complement |
| \( \A \otimes \B \) | Kronecker product | @def-kronecker-product |
| \( \vecop \X \) | vectorization: the columns of \( \X \) stacked into one column | @def-vec-operator |
| \( \A \circ \B \) | Hadamard (entrywise) product | @def-hadamard-product |
| \( [\A, \B] = \A\B - \B\A \) | commutator | @def-commutator |
| \( \J \) | the all-ones matrix, every entry \( 1 \) | @exm-symmetric-3x3-spectral |
| \( \A'(t) \), \( \x'(t) \) | entrywise derivative of a matrix- or vector-valued function of a real variable | @def-matrix-valued-derivative |
| \( e^{\A} \), \( f(\A) \) | matrix exponential; a function of a matrix through its Jordan form | @def-matrix-exponential, @def-matrix-function-jordan |
| \( \lim_m \A^m \) | entrywise convergence of matrices | @def-entrywise-convergence |
| \( \A \x = \b \), \( \A\x = \0 \) | a linear system and its homogeneous version | @def-linear-system, @def-homogeneous-system |
| echelon form | the staircase shapes elimination produces | @def-row-echelon-form, @def-reduced-row-echelon-form |

## Maps and their spaces

| Symbol | Meaning | Defined at |
|:-----------|:------------------------------|:-------------|
| \( T, S \colon V \to W \) | linear maps; \( ST \) means first \( T \), then \( S \) | @def-linear-transformation |
| \( T_{\A} \) | the map \( F^n \to F^m \), \( \x \mapsto \A\x \) | @exm-matrix-transformation |
| \( \ker T \), \( \im T \) | kernel and image | @def-kernel, @def-image |
| \( \rank T \), \( \nullity T \) | \( \dim \im T \) and \( \dim \ker T \) | @def-rank, @def-nullity |
| \( \cL(V, W) \), \( \cL(V) \) | all linear maps \( V \to W \); the operators on \( V \) | @def-space-of-linear-maps |
| \( \End(V) \) | the same space \( \cL(V) \), named as an **algebra** under composition | @def-subalgebra |
| \( p(T) \), \( \id_V \) | a polynomial in an operator; the identity operator | @def-polynomial-of-operator, @def-linear-transformation |
| \( \mtx{T}{\sB}{\sC} \) | matrix of \( T \) from the input basis \( \sB \) to the output basis \( \sC \) | @def-matrix-of-linear-map |
| \( \mtx{\id}{\sB}{\sC} \) | change-of-coordinates matrix from \( \sB \) to \( \sC \) | @def-change-of-coordinates-matrix |
| \( V \cong W \) | isomorphic vector spaces | @def-isomorphism, @def-isomorphic |
| \( T' \) | dual map \( W^{*} \to V^{*} \); the star is kept for adjoints | @def-dual-map |
| \( \tr T \), \( \det T \) | trace and determinant of an operator | @def-trace-operator, @def-det-operator |
| \( T\vert_U \), \( \bar T \) | restriction of \( T \) to an invariant subspace; the operator it induces on \( V/U \) | @def-invariant-subspace, @def-restriction-operator |
| \( \GL_n(F) \), \( \SL_n(F) \) | general and special linear groups | @exm-groups, @thm-det-homomorphism |
| \( \cM(V_1, \dots, V_k; W) \) | multilinear maps \( V_1 \times \dots \times V_k \to W \); the semicolon separates inputs from output | @def-space-of-multilinear-maps |

## Inner products and norms

| Symbol | Meaning | Defined at |
|:-----------|:------------------------------|:-------------|
| \( \inner{\u}{\v} \) | inner product: **linear in the first slot**, conjugate-linear in the second | @def-inner-product |
| \( \inner{\A}{\B} = \tr(\B^{*}\A) \) | the Frobenius inner product on matrices | @def-inner-product |
| \( \norm{\v} \) | norm; the induced norm \( \sqrt{\inner{\v}{\v}} \) unless said otherwise | @def-induced-norm, @def-norm |
| \( \u \perp \v \), \( \theta \) | orthogonal vectors; the angle between two non-zero real vectors | @def-orthogonal, @def-angle |
| \( \G \) | Gram matrix of a list, \( (\G)_{ij} = \inner{\v_j}{\v_i} \) | @def-gram-matrix |
| \( U^{\perp} \) | orthogonal complement | @def-orthogonal-complement |
| \( P_U \), \( d(\v, U) \) | orthogonal projection onto \( U \); distance to \( U \) | @def-orthogonal-projection, @def-distance-to-subspace |
| \( T^{*} \) | adjoint of an operator | @def-adjoint |
| self-adjoint, normal | \( T^{*} = T \); \( T^{*}T = TT^{*} \) | @def-self-adjoint, @def-normal-operator |
| \( \Orth(n) \), \( \SO(n) \), \( \Unit(n) \) | orthogonal, special orthogonal and unitary groups | @def-unitary-orthogonal-groups |
| \( \H_{\w} \), \( \G(i,j;c,s) \) | Householder reflection; Givens rotation | @def-householder-reflection, @def-givens-rotation |
| \( P_n \), \( T_n \) | Legendre and Chebyshev polynomials | @def-orthogonal-polynomial-sequence, @def-chebyshev-polynomials |
| \( \norm{\x}_p \) | the \( p \)-norm; \( q \) is the conjugate exponent, \( 1/p + 1/q = 1 \) | @def-norm, @cor-minkowski-inequality |
| \( \norm{f}_{\infty} \) | sup norm on \( C[0,1] \) | @def-norm |
| \( B_{\norm{\cdot}} \), \( B_1, B_2, B_\infty \) | closed unit ball of a norm; the balls of the three \( p \)-norms | @def-unit-ball |
| \( \norm{\A}_F \) | Frobenius norm, \( \sqrt{\tr(\A^{*}\A)} \); the subscript is obligatory | @lem-frobenius-unitarily-invariant |
| \( \norm{\A} \), \( \norm{\A}_1 \), \( \norm{\A}_{\infty} \) | operator norm induced by a vector norm; largest column sum; largest row sum | @def-operator-norm |
| \( \kappa(\A) = \norm{\A}\norm{\A^{-1}} \) | condition number | @def-condition-number |
| \( \norm{\y}_{*} \) | dual norm, \( \max_{\norm{\x} \le 1}\inner{\x}{\y} \) | @def-dual-norm |
| \( \uinorm{\A} \), \( \uinorm{\A}_{(k)} \) | unitarily invariant norm; the Ky Fan \( k \)-norm \( \sigma_1 + \dots + \sigma_k \) | @def-unitarily-invariant-norm, @def-ky-fan-norm |
| \( \Phi \), \( \Phi^{*} \) | symmetric gauge function and its dual, with \( \uinorm{\A} = \Phi(\sigma(\A)) \) | @def-symmetric-gauge, @def-dual-gauge |
| \( \inner{\x}{\y}_{\A} \), \( \norm{\x}_{\A} \) | the inner product \( \y^{*}\A\x \) of a positive definite \( \A \), and its energy norm | @thm-generalized-eigenvalues-real, @def-energy-norm |
| \( \Theta(U, W) \), \( \theta_1 \le \dots \le \theta_k \) | principal angles between two subspaces, in \( [0, \pi/2] \) | @def-principal-angles |

## Bilinear forms, tensors and exterior algebra

| Symbol | Meaning | Defined at |
|:-----------|:------------------------------|:-------------|
| \( \beta \colon V \times V \to F \), \( q(\v) = \beta(\v,\v) \) | bilinear form; the quadratic form it carries | @def-bilinear-form, @def-quadratic-form |
| \( \mtx{\beta}{\sB}{\sB} \) | Gram matrix of a form, \( \beta(\v_i, \v_j) \), indices uncrossed; \( \sB \) is written twice because each slot of the form is given a basis | @def-form-matrix |
| \( \operatorname{rad}(\beta) \) | radical of a form; \( \beta \) is non-degenerate exactly when it is \( \{\0\} \) | @def-radical, @def-nondegenerate |
| discriminant | the square class of \( \det\mtx{\beta}{\sB}{\sB} \) in \( F^{\times} \), the same for every basis | @def-discriminant |
| \( (n_+, n_-, n_0) \) | inertia of a real symmetric form; the signature is the pair \( (n_+, n_-) \) | @def-signature |
| \( \operatorname{In}(\A) \) | inertia triple of a Hermitian matrix, by sign of eigenvalue | @def-inertia-triple |
| \( \H_f(\a) \) | Hessian matrix of a twice-differentiable function at a point | @def-hessian |
| isotropic, totally isotropic | \( q(\v) = 0 \) with \( \v \ne \0 \); a subspace on which \( \beta \) vanishes | @def-isotropic-vector, @def-totally-isotropic-subspace |
| hyperbolic plane, \( \operatorname{ind}(\beta) \) | the plane of a hyperbolic pair; the Witt index | @def-hyperbolic-plane, @def-witt-index |
| \( U \perp W \) | orthogonal direct sum for a form: the summands pair to zero | @def-hyperbolic-plane |
| \( (V,\beta) \cong (V',\beta') \) | **isometric** bilinear spaces (this use of \( \cong \) is local to forms) | @def-form-isometry |
| \( \operatorname{Isom}(\beta) \) | isometry group of a form, \( \{\P : \P\tp\A\P = \A\} \) | @def-isometry-group-of-form |
| \( \Orth(p,q) \), \( \I_{p,q} \), \( \Sp(2m,F) \), \( \vOmega_{2m} \) | the indefinite orthogonal and symplectic groups and their standard matrices | @def-classical-groups |
| \( V \otimes W \), \( \v \otimes \w \) | tensor product and a simple tensor | @def-tensor-product, @def-tensor-notation |
| \( S \otimes T \), \( \sB \otimes \sC \) | tensor product of maps; the product basis, first factor slow | @def-tensor-of-maps, @def-tensor-basis-ordering |
| \( \Theta \) | the isomorphism \( V^{*} \otimes W \to \cL(V,W) \) | @thm-tensor-hom-iso |
| \( C \), \( C^a_b \) | contraction \( V^{*} \otimes V \to F \); contraction of one upper against one lower slot | @def-contraction, @def-contraction-slots |
| \( T^{p}_{q}(V) \), \( T^{i_1 \dots i_p}_{j_1 \dots j_q} \) | mixed tensors of type \( (p,q) \) and their components | @def-tensor-type, @def-tensor-components |
| \( V^{\otimes k} \), \( \operatorname{T}(V) \) | \( k \)-th tensor power, with \( V^{\otimes 0} = F \); the tensor algebra | @def-tensor-power, @def-tensor-algebra |
| \( \Sym^{k} V \), \( \Sym(V) \) | \( k \)-th symmetric power; the symmetric algebra, written by juxtaposition | @def-symmetric-power, @def-symmetric-algebra |
| \( (V^{\otimes k})^{S_k} \) | the symmetric tensors, fixed by every permutation of the slots | @def-symmetric-tensor |
| \( F[x_1, \dots, x_n] \) | the polynomial algebra in \( n \) variables | @def-polynomial-algebra-several-variables |
| \( \Lambda^{k} V \), \( \v_1 \wedge \dots \wedge \v_k \) | \( k \)-th exterior power and a wedge | @def-exterior-power |
| \( \Lambda V \), \( \e_{S} \) | exterior algebra; its basis element for an increasing index set | @def-exterior-algebra |
| \( \Lambda^k T \) | exterior power of a linear map; on the top power it is \( \det T \) | @def-exterior-power-of-map |
| \( \varepsilon_{\v} \) | wedging by a fixed vector, \( \omega \mapsto \v \wedge \omega \) | @lem-wedge-by-a-vector |
| \( \cI \), \( \cI_q \) | a two-sided ideal of an algebra; the one whose quotient is the Clifford algebra | @def-two-sided-ideal, @def-clifford-algebra |
| \( \nH \) | the quaternions | @def-quaternions |

## Spectra and canonical forms

| Symbol | Meaning | Defined at |
|:-----------|:------------------------------|:-------------|
| \( p_T(x) = \det(x\I - T) \) | characteristic polynomial, monic | @def-characteristic-polynomial, @def-charpoly-operator |
| \( m_T(x) \) | minimal polynomial: the monic generator of the annihilating ideal | @def-minimal-polynomial, @def-annihilating-polynomial |
| \( \spec(T) \) | spectrum, the set of eigenvalues | @def-spectrum |
| \( E_\lambda(T) = \ker(T - \lambda I) \) | eigenspace | @def-eigenvalue, @def-eigenspace |
| \( a_T(\lambda) \), \( g_T(\lambda) \) | algebraic and geometric multiplicity of \( \lambda \) | @def-algebraic-multiplicity, @def-geometric-multiplicity |
| \( G_\lambda(T) \) | generalized eigenspace, \( \ker(T - \lambda I)^{n} \) | @def-generalized-eigenvector, @def-generalized-eigenspace |
| \( \J_k(\lambda) \) | \( k \times k \) Jordan block: \( \lambda \) on the diagonal, \( 1 \) on the **super**diagonal | @def-jordan-block, @def-jordan-form |
| \( \vLambda(\lambda) \), \( \C_k(\lambda) \) | rotation-scaling block of a conjugate pair; the real Jordan block built from it | @def-real-jordan-block |
| \( \C(p) \) | companion matrix of a monic \( p \) | @def-companion-matrix |
| \( Z(\v; T) \), \( m_{T,\v} \) | cyclic subspace generated by \( \v \); the \( T \)-annihilator of \( \v \) | @def-cyclic-subspace, @def-t-annihilator |
| \( d_1 \mid d_2 \mid \dots \mid d_r \) | invariant factors, with \( d_r = m_T \); their prime powers are the elementary divisors | @def-invariant-factors |
| \( \rho(\A) \) | spectral radius, the largest modulus in the spectrum | @def-spectral-radius |
| \( \vPi \) | the limit \( \lim_m \A^{m} \) of a convergent matrix | @thm-matrix-powers-converge |
| \( \A \succeq 0 \), \( \A \succ 0 \) | positive semidefinite, positive definite; Hermitian is implied | @def-positive-semidefinite |
| \( \A \succeq \B \) | the Loewner order, \( \A - \B \succeq 0 \) | @def-loewner-order |
| \( \A^{1/2} \) | the unique positive semidefinite square root | @thm-psd-square-root |
| \( \lvert \A \rvert = (\A^{*}\A)^{1/2} \) | absolute value of a matrix | @def-matrix-absolute-value |
| \( \sigma_1(\A) \ge \dots \ge \sigma_{\min(m,n)}(\A) \) | singular values, decreasing | @def-singular-values |
| \( \A = \U\vSigma\V^{*} \) | a singular value decomposition: \( \U \) and \( \V \) unitary, \( \vSigma \) the same size as \( \A \) with the singular values on its diagonal and zeros elsewhere | @thm-svd |
| \( \A^{+} \) | Moore–Penrose pseudoinverse | @def-pseudoinverse |
| \( \lambda_1(\A) \ge \dots \ge \lambda_n(\A) \), \( \vlambda(\A) \) | eigenvalues of a Hermitian matrix, decreasing; the vector of them | @def-rayleigh-quotient, @def-majorization |
| \( R_{\A}(\x) \), \( R_T(\v) \) | Rayleigh quotient \( \inner{\A\x}{\x}/\inner{\x}{\x} \) | @def-rayleigh-quotient |
| \( s_k(\A) \) | Ky Fan partial sum \( \lambda_1(\A) + \dots + \lambda_k(\A) \) | @cor-ky-fan-subadditive |
| \( \d(\A) \) | the diagonal vector \( (a_{11}, \dots, a_{nn}) \) of a Hermitian matrix | @def-majorization |
| \( \cW = (W_1, \dots, W_k) \) | a flag of subspaces, and a list adapted to it | @def-flag-adapted-list |
| \( \cH(\A) \) | Hermitian dilation, whose eigenvalues are \( \pm\sigma_i(\A) \) and zeros | @prp-hermitian-dilation |
| \( r_i(\A) \), \( D_i(\A) \) | Gershgorin radius and disc | @def-gershgorin-discs |
| \( O_{ij}(\A) \) | Brauer oval of Cassini | @thm-brauer-ovals |
| \( W(\A) \) | numerical range, \( \{\x^{*}\A\x : \norm{\x}_2 = 1\} \) | @def-numerical-range |
| \( \E \), \( \widetilde{\A} \) | a perturbation, in \( \A + \E \); a perturbed matrix when it is not of that shape | @def-condition-number |
| \( \operatorname{sep}_F(\A,\B) \) | separation of two matrices in the Frobenius norm | @def-sep |
| \( \kappa_{\A}(\lambda) \) | condition number of a simple eigenvalue | @def-eigenvalue-condition-number |
| \( \cS_{\A,\B} \) | Sylvester operator \( \X \mapsto \A\X - \X\B \) | @def-sylvester-operator |
| \( \B - \lambda\A \) | a matrix pencil; its generalized eigenvalues solve \( \B\x = \lambda\A\x \) | @def-generalized-eigenvalue |

## Orders, convexity and non-negative matrices

| Symbol | Meaning | Defined at |
|:-----------|:------------------------------|:-------------|
| \( \x \ge \0 \), \( \A \ge 0 \), \( \A > 0 \) | the **entrywise** order; a positive matrix has every entry positive | @def-entrywise-order |
| \( \nR^m_{\ge 0} \) | the non-negative orthant | @def-convex-cone |
| \( \x \prec \y \), \( \x \prec_w \y \), \( \x^{\downarrow} \) | majorization, weak majorization, decreasing rearrangement | @def-majorization |
| \( \conv S \), \( \operatorname{aff} S \) | convex hull; affine hull, a coset of a subspace | @def-convex-hull, @def-affine-hull |
| \( [\x, \y] \) | the segment from \( \x \) to \( \y \) | @def-convex-set |
| \( \Delta_n \) | standard simplex: \( n \) non-negative weights adding to \( 1 \) | @def-standard-simplex |
| \( \interior{S} \), \( \closure{S} \) | interior and closure in a finite-dimensional real space | @def-interior-point, @def-closed-set |
| \( P_C(\x) \), \( d(\x, C) \) | nearest point of a closed convex set, and the distance to it | @thm-nearest-point |
| \( p_K \), \( h_K \), \( K^{\circ} \) | gauge, support function and polar set of a convex set | @def-gauge, @def-support-function, @def-polar-set |
| \( K^{*} \) | dual cone, inside \( V \) itself | @def-dual-cone |
| \( \operatorname{cone}(\a_1, \dots, \a_m) \) | finitely generated cone | @def-finitely-generated-cone |
| \( \operatorname{epi} f \) | epigraph, \( \{(\x, s) : s \ge f(\x)\} \) | @def-convex-function |
| \( \operatorname{ext} C \) | extreme points of a convex set | @def-extreme-point, @def-face |
| \( \cD_n \), \( \Omega_n \) | real density matrices; doubly stochastic matrices | @def-density-matrix, @def-doubly-stochastic |
| \( v(\A) \) | value of the matrix game with payoff matrix \( \A \) | @def-value-of-game, @def-mixed-strategy |
| \( \A \# \B \) | geometric mean of two positive definite matrices | @def-geometric-mean |
| \( L_f(t_1, \dots, t_n) \) | Loewner matrix of divided differences | @def-loewner-matrix, @def-divided-difference |
| \( G(\A) \) | directed graph of a square matrix: an edge \( j \to i \) when \( a_{ij} \ne 0 \) | @def-directed-graph-of-matrix |
| irreducible, primitive | no proper invariant coordinate subspace; some power is positive | @def-irreducible, @def-primitive |
| \( h \), \( \omega = e^{2\pi i/h} \) | period of an irreducible non-negative matrix, and the root of unity it names | @def-period |
| \( \underline{r}_{\A}(\x) \), \( \overline{r}_{\A}(\x) \) | lower and upper Collatz–Wielandt functions; the bars are not conjugation | @def-collatz-wielandt-functions |
| Perron root and vectors | \( \rho(\A) \), the right vector \( \v > \0 \) with \( \1\tp\v = 1 \), the left vector \( \w \) with \( \w\tp\v = 1 \) | @def-perron-vector, @def-perron-root-and-vectors |
| \( \Q \), \( \R \), \( \N \) | transient block, absorbing block and fundamental matrix of an absorbing chain | @def-absorbing-chain |
| \( \G \), \( \H \), \( \alpha \) | Google matrix, raw link matrix, damping factor | @def-google-matrix, @def-link-matrix |
| \( \K_n \) | the second-difference matrix, a non-singular M-matrix | @def-m-matrix, @def-z-matrix |
| stochastic matrix, steady state | column sums \( 1 \) and non-negative entries; a fixed probability vector | @def-stochastic-matrix, @def-markov-chain |

## Algebras, groups and representations

| Symbol | Meaning | Defined at |
|:-----------|:------------------------------|:-------------|
| \( A \), \( 1_A \) | an associative algebra over \( F \) and its unit; plain italic, never bold | @def-algebra-over-field |
| \( \cT_n \), \( \cN \) | the upper triangular matrices in \( M_n(F) \); its ideal of strictly upper triangular ones | @exm-first-subalgebras |
| \( F\langle S \rangle \) | the subalgebra generated by a set: the span of the words in \( S \) | @def-generated-subalgebra |
| \( F[T] \), \( F[\A] \) | the algebra of polynomials in one operator or matrix, of dimension \( \deg m_T \) | @prp-polynomial-algebra-dimension |
| \( F[G] \), \( \delta_g \) | group algebra of a finite group and its basis of point masses | @def-group-algebra |
| \( L_a \) | left multiplication by \( a \); the regular representation is \( a \mapsto L_a \) | @thm-cayley-for-algebras |
| \( S' \), \( S'' \), \( Z(A) \) | commutant, double commutant, center | @def-commutant, @prp-center-of-matrix-algebra |
| \( C_j \), \( L_W \), \( R_U \) | the column ideals of \( M_n(F) \), and the left and right ideals of a subspace | @def-left-ideal, @prp-left-ideals-of-matrix-algebra |
| \( A/\cI \), \( \pi \) | quotient algebra by a two-sided ideal, and the quotient homomorphism | @def-quotient-algebra |
| \( \operatorname{rad} A \) | radical of an algebra: killed by every irreducible representation | @def-algebra-radical |
| \( a\v \), an \( A \)-space | an action of \( A \) on \( V \), that is a homomorphism \( A \to \End(V) \) | @def-representation-of-an-algebra |
| simple, semisimple | an \( A \)-space with no proper non-zero invariant subspace; a direct sum of such | @def-simple-module, @def-semisimple-algebra |
| \( \End_A(V) \), \( \Hom_A(V,W) \) | equivariant maps, \( f(a\v) = af(\v) \); the subscript is never dropped | @def-intertwining-map |
| \( A(\cF) \) | the subalgebra generated by a family of operators | @lem-family-and-generated-algebra |
| \( \v\varphi \) | the rank-one operator \( \x \mapsto \varphi(\x)\v \) | @thm-burnside |
| \( e_i \) | orthogonal idempotents of a product of algebras: italic, never bold | @def-product-of-algebras |
| \( \rho \), \( \chi_\rho(g) = \tr\rho(g) \) | a representation of a group and its character | @def-representation, @def-character |
| irreducible, equivalent | no proper non-zero subrepresentation; conjugate by one isomorphism | @def-irreducible-representation, @def-equivalent-representations |
| \( \operatorname{Cl}(G) \), \( \inner{f}{f'} \) | class functions on \( G \), and their averaged inner product | @def-class-function, @def-character-inner-product |
| \( V^{G} \) | the fixed space of a representation | @lem-average-projection |
| \( \langle g \rangle \), \( G \times H \) | the cyclic subgroup generated by \( g \); a direct product of groups | @def-cyclic-group, @def-direct-product-of-groups |
| \( \widehat G \), \( \widehat f \), \( \ev_g \) | dual group of a finite abelian group, Fourier transform, evaluation at \( g \) | @def-dual-group, @def-fourier-transform-on-a-group |
| \( \U \) | character matrix, \( (\U)_{mj} = \chi_j(g_m)/\sqrt n \), indices from \( 0 \) | @def-character-matrix |
| \( \C \), \( \F \) | circulant matrix; the Fourier matrix | @def-circulant, @thm-fourier-matrix-unitary |
| \( \c \ast \d \) | cyclic convolution, subscripts read modulo \( n \) | @def-circulant |

## Geometry

| Symbol | Meaning | Defined at |
|:-----------|:------------------------------|:-------------|
| \( \cA, \cB, \cC \) | affine spaces, plain calligraphic | @def-affine-space |
| \( P, Q, R \), \( \overrightarrow{PQ} \), \( P + \v \) | points of an affine space, **not bold**; the vector between two points; translation of a point | @def-affine-space |
| \( \nA^n(F) \) | affine \( n \)-space: \( F^n \) with its origin forgotten | @def-affine-space |
| \( \theta_O \) | the choice-of-origin bijection \( \cA \to V \), \( P \mapsto \overrightarrow{OP} \) | @prp-choice-of-origin |
| \( \vec f \), \( \widehat f \) | linear part of an affine map; its block matrix, homogenizing coordinate **last** | @thm-affine-map-is-linear-plus-translation, @prp-affine-map-block-matrix |
| \( \operatorname{Aff}(\cA) \), \( \tau_{\v} \) | the affine group, and translation by \( \v \) | @thm-affine-group |
| \( \vec A \), \( A \vee B \), \( A \parallel B \) | direction space of a flat; the join; parallelism | @def-flat, @def-affine-join, @def-parallel-flats |
| \( P_J \) | the face of a polyhedron cut out by making the rows \( i \in J \) tight | @prp-face-is-polyhedron, @def-polyhedron-face |
| \( \operatorname{E}(n) \), \( t_{\b} \), \( \operatorname{Fix}(f) \) | the Euclidean group, translation by \( \b \), fixed set of a motion | @def-euclidean-motion |
| \( \R_{\theta} \), \( \M_{\theta} \) | plane rotation and plane reflection matrices | @thm-orthogonal-2x2 |
| \( \widetilde{\A} \), \( \tilde{\x} \) | big matrix and big vector of a quadric, with \( Q(\x) = \tilde{\x}\tp\widetilde{\A}\tilde{\x} \) | @def-quadric |
| \( \nP(V) \), \( \nP^n(F) \) | projective space of \( V \), of dimension \( \dim V - 1 \); \( \nP(F^{n+1}) \) | @def-projective-space |
| \( [\x] = [x_0 : \dots : x_n] \) | homogeneous coordinates; coordinates run from \( 0 \) | @def-homogeneous-coordinates |
| \( U_0 \), \( U_j \), \( H_{\infty} \), \( \iota \) | the standard affine chart, the other charts, the hyperplane at infinity, the chart bijection | @thm-affine-chart |
| \( S \vee T \), \( S \cap T \) | join and meet of projective subspaces | @prp-join-and-meet, @def-projective-subspace |
| \( [T] \), \( [\A] \) | the projectivity induced by an isomorphism or an invertible matrix | @def-projective-transformation |
| \( \operatorname{PGL}(V) \), \( F^{\times} \) | projective linear group; the multiplicative group of the field | @thm-pgl |
| \( (A, B; C, D) \) | cross-ratio of four points: itself a point of \( \nP^1(F) \), not a scalar | @def-cross-ratio |
| \( S^{0} \) | projective annihilator, Chapter 4's \( U^{0} \) read in \( \nP(V^{*}) \) | @thm-duality-correspondence, @def-dual-projective-space |
| \( \o \) | a chosen representative vector of a projective point | @lem-collinear-representatives |
| \( Z(q) \), \( P^{\beta} \) | zero set of a quadratic form; the polar of a point with respect to a conic | @def-projective-quadric, @def-pole-and-polar |
| \( p_{ij} \), \( [L] \), \( \cK \) | Plücker coordinates of a line, the point they form, and the Klein quadric | @def-plucker-coordinates |
| \( \vol \) | volume: of a parallelepiped it is \( \lvert\det\rvert \); extended to \( k \)-dimensional volume | @def-parallelepiped-volume, @def-k-volume |
| \( (\operatorname{In}\A, \operatorname{In}\widetilde{\A}) \) | the pair of inertia triples of a real quadric, an invariant of its affine equivalence class | @def-affine-equivalence, @def-inertia-triple |

## Computation

| Symbol | Meaning | Defined at |
|:-----------|:------------------------------|:-------------|
| \( u \), \( \fl \), \( \cR \), \( \delta \) | unit roundoff, the rounding map, the representable numbers, one rounding | @def-floating-point-model |
| \( \gamma_k = ku/(1-ku) \) | the accumulated-rounding constant | @lem-gamma-bound |
| \( \widehat{\x} \), \( \Delta\A \) | a computed object; a data perturbation produced by an algorithm | @def-forward-error, @def-backward-stable |
| flop, \( g_n \) | one arithmetic operation; the growth factor of elimination | @def-growth-factor, @def-arithmetic-cost |
| \( \cK_k(\A,\b) \), \( \theta_1, \dots, \theta_k \) | Krylov space \( \Span(\b, \A\b, \dots, \A^{k-1}\b) \); the Ritz values from it | @def-krylov-subspace, @def-ritz-values |
| \( \L \), \( \L_0 \), \( \mu_2(\L) \) | graph Laplacian \( \D - \A \), the reduced Laplacian, the Fiedler value | @def-graph-laplacian, @def-fiedler-value |
| \( \X \), \( \X_c \), \( \S \) | data matrix, its centered form, the sample covariance | @def-centered-data-matrix, @def-sample-covariance |
| \( \M \), \( \K \), \( \omega_j \) | mass matrix, stiffness matrix, natural frequencies | @def-mass-spring-system |
| \( \W_n \), \( \P_n \), \( \D_m \), \( \B_n \) | unnormalized transform matrix, even-odd permutation, twiddle matrix, butterfly | @def-dft-matrix, @def-butterfly-and-twiddle |
| \( \omega \) | the exponent of matrix multiplication | @def-matrix-multiplication-exponent |

## Where the book overrides itself

Twenty-four chapters do not have twenty-four alphabets. Several letters carry more than one meaning, and a few English words carry more than one definition. In every case the local meaning is declared where it is used, and in every case there is a tell — an argument, a subscript, a typeface — that decides which one is meant. The rows below list the clashes worth knowing before you meet them.

| Symbol or word | The meanings | How to tell |
|:--------|:---------------------------------|:--------------|
| \( \U \) | a generic upper triangular matrix (@def-upper-triangular, @def-lu-factorization); a unitary matrix, in the Schur and singular value factorizations (@cor-schur-matrix, @def-singular-values); the character matrix of a finite abelian group (@def-character-matrix) | the chapter: triangular in Chapters 2 and 22, unitary from Chapter 11 on, the character matrix only in Chapter 22 §09 |
| \( \V \) | the right factor of a singular value decomposition, \( \A = \U\vSigma\V^{*} \) (@thm-svd); the Vandermonde matrix \( \V(x_1, \dots, x_n) \) (@thm-vandermonde-determinant); one of the two matrices invertible over \( F[x] \) in \( \B = \U\A\V \) (@def-polynomial-matrix-equivalence). Plain \( V \) is a vector space | the Vandermonde matrix always carries its nodes; the typeface for the space, and Chapter 9 §07 is the one place \( \V \) is invertible only over \( F[x] \) |
| **irreducible** | a polynomial with no non-trivial factorization (@def-irreducible-polynomial); a non-negative matrix with no invariant coordinate subspace (@def-irreducible); an \( A \)-space or a representation with no proper non-zero invariant subspace (@def-simple-module, @def-irreducible-representation) | what the word is applied to. The three notions are unrelated |
| \( e_i \) versus \( \e_i \) | italic \( e_i \) is an idempotent of a product of algebras (@def-product-of-algebras); bold \( \e_i \) is the \( i \)-th standard basis vector (@exm-standard-bases) | the typeface, and that is the whole reason Chapter 22 chose italic |
| \( \G \) | Gram matrix (@def-gram-matrix); Givens rotation \( \G(i,j;c,s) \) (@def-givens-rotation); Google matrix (@def-google-matrix); the alternating Gram matrix of the Plücker form (@def-plucker-coordinates). Plain \( G(\A) \) is the directed graph of a matrix (@def-directed-graph-of-matrix) | the Givens rotation always carries its four arguments; the graph is plain italic with its matrix in brackets |
| \( \H \), \( \K \) | Hessian \( \H_f(\a) \) (@def-hessian); Householder reflection \( \H_{\w} \) (@def-householder-reflection); the Hermitian and skew parts of a matrix (@lem-hermitian-parts); the raw link matrix (@def-link-matrix); the second-difference matrix \( \K_n \) (@def-m-matrix); the stiffness matrix (@def-mass-spring-system). Calligraphic \( \cK_k(\A,\b) \) is a Krylov space (@def-krylov-subspace) and \( \cK \) the Klein quadric (@def-plucker-coordinates); blackboard \( \nH \) is the quaternions (@def-quaternions) | the Hessian and the Householder reflection always carry their argument, the second-difference matrix always its size \( \K_n \), the Krylov space its subscript and arguments |
| \( \L \) | the lower triangular factor of an elimination (@def-lu-factorization); the graph Laplacian (@def-graph-laplacian); the Lax matrix (@def-lax-pair). Plain \( L_a \) is left multiplication in an algebra (@thm-cayley-for-algebras) and \( L_f \) a Loewner matrix (@def-loewner-matrix); calligraphic \( \cL(V,W) \) is a space of maps (@def-space-of-linear-maps) | Chapter 23 §§08 and 11 each declare their use at the head of the section; the plain letters carry a subscript |
| \( \R \), \( r \) | the \( \R \) of a \( QR \) factorization; the plane rotation \( \R_\theta \) (@thm-orthogonal-2x2); the rotation through \( 2\pi/n \) in Chapter 22; the absorbing block of a Markov chain (@def-absorbing-chain). Plain \( R_{\A}(\x) \) is the Rayleigh quotient (@def-rayleigh-quotient) and \( r_i(\A) \) a Gershgorin radius (@def-gershgorin-discs) | the Rayleigh quotient is plain italic and takes a vector; the Gershgorin radius is plain and takes an index |
| \( \Q \) | the orthogonal factor of a \( QR \) factorization; the orthogonal linear part of a Euclidean motion (@def-euclidean-motion); the quarter turn in Chapter 22; the transient block of an absorbing chain (@def-absorbing-chain). Blackboard \( \nQ \) is the rationals (@def-common-number-sets) | the chapter, and the blackboard face for the field |
| \( \S \), \( \cS \) | a congruence or a similarity matrix; a Schur complement in Chapter 23 §02; the sample covariance (@def-sample-covariance); the cyclic shift in Chapter 11 §09. Calligraphic \( \cS_{\A,\B} \) is the Sylvester operator (@def-sylvester-operator) | each section of Chapter 23 says which it means; the Sylvester operator carries both its matrices |
| \( \N \), \( \cN \) | the fundamental matrix \( (\I - \Q)^{-1} \) of an absorbing chain (@def-absorbing-chain); an incidence matrix, with \( \L = \N\N\tp \) (@def-incidence-matrix); the strictly upper triangular matrices \( \cN \) (@exm-first-subalgebras). Blackboard \( \nN \) is the natural numbers | the calligraphic face for the algebra, the blackboard face for the number set |
| \( \J \) | the all-ones matrix (@exm-symmetric-3x3-spectral); the Jordan block \( \J_k(\lambda) \) (@def-jordan-block) | the Jordan block always carries its size and its eigenvalue |
| \( \C \) | the companion matrix \( \C(p) \) (@def-companion-matrix); the real Jordan block \( \C_k(\lambda) \) (@def-real-jordan-block); a circulant (@def-circulant). Plain \( C \) and \( C^a_b \) are contractions (@def-contraction) and \( C_{ij} \) a cofactor (@def-minor-cofactor); blackboard \( \nC \) is the complex numbers | the companion matrix always carries its polynomial, the Jordan blocks their size and eigenvalue; a bare \( \C \) in Chapter 22 is a circulant |
| \( \W \), \( W \) | the Wielandt matrix \( \W_n \) (@thm-wielandt-bound); the unnormalized transform matrix \( \W_n \) of Chapter 23 §12; the accumulated orthogonal factor \( \W_k \) of Chapter 23 §08. Plain \( W \) is a subspace, \( W(\A) \) the numerical range (@def-numerical-range), and \( W_n \) the zero-sum matrices of Chapter 18 §07 (@lem-doubly-stochastic-sum-conditions) | the numerical range always carries its matrix as an argument; the subspace never carries one |
| \( \Theta \), \( \theta \) | the isomorphism \( \nC \to \nR^2 \) (@exm-standard-isomorphisms); the basis-dependent \( V \to V^{*} \) (@thm-double-dual-isomorphism); the natural isomorphism \( V^{*} \otimes W \to \cL(V,W) \) (@thm-tensor-hom-iso); the diagonal matrix of principal angles (@def-principal-angles). Lowercase: the angle between vectors (@def-angle), the choice-of-origin map \( \theta_O \) (@prp-choice-of-origin), the Ritz values \( \theta_1, \dots, \theta_k \) (@def-ritz-values) | the principal-angle \( \Theta \) appears only inside \( \sin\Theta \) and \( \cos\Theta \); lowercase \( \theta \) is an angle unless the section says otherwise, and the choice-of-origin map carries the point \( O \) |
| \( \Pi \), \( \pi \) | bold \( \vPi \) is the limit of a convergent stochastic matrix (@thm-matrix-powers-converge); plain \( \Pi \) is a plane in Chapter 21 §§04, 08, 09 and the quotient map \( \GL(V) \to \operatorname{PGL}(V) \) in §07; \( \pi \) is the quotient map \( X \to X/{\sim} \) of a set (@def-quotient-set), a quotient homomorphism of algebras (@def-quotient-algebra) and, locally, a slot projection | the typeface, and that no section of Chapter 21 uses both meanings |
| \( \Phi \), \( \Psi \) | a symmetric gauge function and its dual (@def-symmetric-gauge, @def-dual-gauge); the two isomorphisms of Chapter 22 §09 (@def-fourier-transform-on-a-group) | the argument: a gauge eats a real vector, Chapter 22's maps eat an element of a group algebra |
| \( \Omega \), \( \omega \) | plain \( \Omega_n \) is the doubly stochastic matrices (@def-doubly-stochastic), bold \( \vOmega_{2m} \) the standard alternating matrix (@def-classical-groups). Lowercase \( \omega \) is a root of unity (@def-period, @def-dft-matrix), an angular frequency (@def-mass-spring-system), the exponent of matrix multiplication (@def-matrix-multiplication-exponent), and a differential form being wedged (@def-exterior-algebra) | the typeface for \( \Omega \); for \( \omega \), the section, each of which declares its use |
| \( \rho \) | spectral radius (@def-spectral-radius); a representation of a group or an algebra (@def-representation) | the argument: a matrix for the radius, a group element for the representation |
| \( \sigma \) | a permutation (@def-sign-permutation); a singular value \( \sigma_i(\A) \) (@def-singular-values) | the singular value always carries an index and a matrix |
| \( \lambda \), \( \mu \) | a scalar or an eigenvalue throughout; also the linear-part homomorphism \( \operatorname{E}(n) \to \Orth(n) \) (@def-euclidean-motion) and the Fiedler value \( \mu_2 \) (@def-fiedler-value) | Chapter 21 §04 is the one place \( \lambda \) is not a scalar, and it says so |
| \( \lvert \cdot \rvert \) | modulus of a complex number (@def-conjugate-modulus); cardinality of a set; the matrix absolute value \( (\A^{*}\A)^{1/2} \) (@def-matrix-absolute-value); the **entrywise** absolute value in Chapter 18 (@def-entrywise-order) | what sits inside. Chapter 18 states its override, and the Chapter 12 meaning does not appear there |
| \( \Lambda \) | plain \( \Lambda^k V \) is an exterior power (@def-exterior-power); bold \( \vLambda(\lambda) \) is a rotation-scaling block (@def-real-jordan-block) | the typeface, and the block always carries its eigenvalue |
| \( \delta \) | Kronecker delta \( \delta_{ij} \) (@def-identity-matrix); a point mass \( \delta_g \) in a group algebra (@def-group-algebra); a basis element \( \delta_s \) of a free vector space (@def-free-vector-space); one rounding error (@def-floating-point-model) | the Kronecker delta always carries two **numerical** subscripts |
| \( \perp \) | orthogonal complement \( U^{\perp} \) (@def-orthogonal-complement); the complement \( U^{\perp_\beta} \) for a bilinear form (@def-radical); orthogonal direct sum \( U \perp W \) of a form (@def-hyperbolic-plane); a polarity \( S^{\perp} \) in projective space (@thm-duality-correspondence) | the unadorned \( U^{\perp} \) is always the inner-product one |
| \( \cong \), \( \sim \), \( \simeq \), \( \approx \) | isomorphic spaces (@def-isomorphic) or, between spaces carrying forms, isometric (@def-form-isometry); similar matrices (@def-similar-matrices); congruent matrices (@def-congruent); equivalent over \( F[x] \) (@def-polynomial-matrix-equivalence), or "approximately equal" in prose | what stands on either side; the four relation symbols are never interchanged |
| brackets | \( \coord{\v}{\sB} \) a coordinate vector (@def-coordinates); \( \mtx{T}{\sB}{\sC} \) a matrix of a map (@def-matrix-of-linear-map); \( [\A,\B] \) a commutator (@def-commutator); \( [\x,\y] \) a segment (@def-convex-set); \( [\x] \) a projective point (@def-homogeneous-coordinates) and \( [T] \) a projectivity (@def-projective-transformation); \( F[x] \) and \( F[G] \) rings and algebras (@def-polynomial-ring, @def-group-algebra) | the number of arguments and whether they are bold: a segment takes two bold vectors, a commutator two bold matrices |
| the superscript of \( \mtx{\,\cdot\,}{\sB}{\sC} \) | for a linear map it is the **output** basis, \( \mtx{T}{\sB}{\sC} \) (@def-matrix-of-linear-map); for a bilinear form it is the basis read into the **second slot**, \( \mtx{\beta}{\sB}{\sB} \) (@def-form-matrix) | what sits inside the brackets. The two readings are the same rule — the basis on the second slot — since a map's second slot is its output; a form on \( V \times V \) always gives both slots the same basis, so its two labels agree, and neither is ever left off |
| \( T \) | a linear map throughout; the transpose \( \A\tp \); Chebyshev polynomials \( T_n \) (@def-chebyshev-polynomials); the tensor algebra \( \operatorname{T}(V) \) (@def-tensor-algebra) and mixed tensors \( T^p_q(V) \) (@def-tensor-type); a \( T \)-transform (@def-t-transform) | the tensor algebra is upright and takes a space; the Chebyshev polynomial and the \( T \)-transform carry subscripts |
| \( P \), \( p \) | orthogonal projection \( P_U \) (@def-orthogonal-projection); Legendre polynomials \( P_n \) (@def-orthogonal-polynomial-sequence); a point of an affine space (@def-affine-space); the nearest-point map \( P_C \) (@thm-nearest-point); a face \( P_J \) (@prp-face-is-polyhedron); the even-odd permutation \( \P_n \) (@def-butterfly-and-twiddle); characteristic polynomial \( p_T \) (@def-characteristic-polynomial); a gauge \( p_K \) (@def-gauge) | a subspace subscript means a projection, an integer subscript a polynomial; bold means a matrix |
| \( Z \) | the cyclic subspace \( Z(\v;T) \) (@def-cyclic-subspace); the center \( Z(A) \) of an algebra (@def-commutant); the zero set \( Z(q) \) of a quadratic form (@def-projective-quadric); a Z-matrix (@def-z-matrix) | the argument decides: a vector and an operator, an algebra, or a form |
| \( \E \), \( E \) | the perturbation in \( \A + \E \); a matrix unit \( \E_{ij} \) (@exm-standard-bases); an elementary matrix (@def-elementary-matrix); an eigenspace \( E_\lambda(T) \) (@def-eigenspace); the Euclidean group \( \operatorname{E}(n) \) (@def-euclidean-motion) | subscripts again: two indices give a matrix unit, an eigenvalue gives an eigenspace, a bare \( \E \) is the perturbation |
| \( \D \), \( D \) | a diagonal matrix (@def-diagonal-matrix); the elementary scaling \( \D_i(c) \) (@def-elementary-matrix); the twiddle matrix \( \D_m \) (@def-butterfly-and-twiddle); the degree matrix in \( \L = \D - \A \) (@def-graph-laplacian); a Gershgorin disc \( D_i(\A) \) (@def-gershgorin-discs); density matrices \( \cD_n \) (@def-density-matrix) | the Gershgorin disc is plain italic, since the bold letter is a diagonal matrix |
| \( \M \), \( M \) | a block matrix, as in the Schur complement \( \M/\A \) (@def-schur-complement); the mass matrix (@def-mass-spring-system); the plane reflection \( \M_\theta \) (@thm-orthogonal-2x2); a minor \( M_{ij} \) (@def-minor-cofactor); the space \( M_n(F) \) (@def-matrix); an M-matrix (@def-m-matrix) | plain italic with two indices is a minor; \( M_n(F) \) always carries its size and field |
| \( u \) | the unit roundoff (@def-floating-point-model); bold \( \u \) is a vector | the typeface; Chapter 23 §01 warns about the pair |
| \( h \) | the period of an irreducible non-negative matrix (@def-period); a support function \( h_K \) (@def-support-function); a mesh width in Chapter 18 §09 | the support function always carries its convex set |
| **simple** | a simple algebra (@def-simple-algebra); a simple \( A \)-space (@def-simple-module); a simple eigenvalue, of multiplicity one (@def-eigenvalue-condition-number); a simple tensor (@def-tensor-notation) | what the word is applied to |
| **equivalent** | equivalent matrices \( \B = \Q\A\P \) (@def-equivalent-matrices); equivalence over \( F[x] \) (@def-polynomial-matrix-equivalence); equivalent norms (@def-equivalent-norms); equivalent representations (@def-equivalent-representations); affine equivalence of quadrics (@def-affine-equivalence) | the objects being compared |
| **positive** | \( \A > 0 \) entrywise, every entry positive (@def-entrywise-order); \( \A \succ 0 \) positive definite (@def-positive-semidefinite) | the symbol: \( > \) is entrywise, \( \succ \) is the Loewner order. A positive matrix need not be positive definite, nor conversely |
| **radical**, **contraction** | radical of a bilinear form (@def-radical) or of an algebra (@def-algebra-radical); contraction of tensor slots (@def-contraction) or a matrix of norm at most one (@def-matrix-contraction) | the argument, in both cases |
| **signature** | the pair \( (n_+, n_-) \), and also the single integer \( n_+ - n_- \) | @def-signature says which is meant where the word appears |
