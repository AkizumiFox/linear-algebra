# Book-wide notation

This list is fixed. A chapter that needs a new symbol adds it here, and a new macro in `latex/macros.tex`, before using it. The left column is what to type.

## Numbers, sets, logic

| Type | Renders / meaning |
|---|---|
| `\nN, \nZ, \nQ, \nR, \nC` | ℕ = {0, 1, 2, …} (zero included), ℤ, ℚ, ℝ, ℂ |
| `F` | a general field, plain italic F. Use `\nF_p` for the field with p elements |
| `\coloneqq` | "is defined to be" |
| `\conj{z}`, `\lvert z \rvert` | complex conjugate, modulus |
| `\{ x \in S : P(x) \}` | set-builder notation, with a colon (not a bar) |
| `S \setminus T`, `S^{c}`, `\lvert S \rvert` | difference, complement, cardinality |
| `f \colon X \to Y`, `x \mapsto f(x)` | functions. Composition is `g \circ f` for general functions |
| `\id_X` | identity function |
| `S_n`, `\sgn(\sigma)` | symmetric group, sign of a permutation |
| `\operatorname{inv}(\sigma)` | number of inversions of σ |

## Vectors and spaces

| Type | Meaning |
|---|---|
| `V, W, U` | vector spaces over F (U is usually a subspace) |
| `\v, \u, \w, \x, \y` | vectors, **bold** lowercase (`\mathbf`) |
| `\0` | zero vector (bold). The scalar zero is `0` |
| `a, b, c, \lambda, \mu` | scalars, plain |
| `F^n` | column vectors. In running text write \( (x_1, \dots, x_n) \) and treat it as a column |
| `\e_1, \dots, \e_n` | standard basis of F^n |
| `\1` | the all-ones vector |
| `\cF` | a family of operators in 𝓛(V) |
| `F[x]`, `F[x]_{\le n}` | polynomials; polynomials of degree at most n |
| `M_{m \times n}(F)`, `M_n(F)` | matrices |
| `\Span(S)` | span. The span of the empty set is {0} |
| `\dim V` | dimension (over F; write `\dim_F V` when the field matters) |
| `U + W`, `U \oplus W` | sum; direct sum (internal) |
| `V / U`, `\v + U` | quotient space, coset |
| `\sB = (\v_1, \dots, \v_n)` | an **ordered** basis, in parentheses. Calligraphic `\sB, \sC, \sE` |
| `\coord{\v}{\sB}` | coordinate vector, rendered [v]_𝓑 |

## Linear maps and matrices

**Bold is for matrices and vectors, never for maps or spaces.** A matrix is bold (`\A`), a vector is bold lowercase (`\v`), an operator or linear map is plain italic (T, S), and a vector space is plain italic (V, U, W). A Greek letter that names a matrix is bold too, through `\vLambda`, `\vPi`, … , which render bold upright like `\A`. A letter that names a matrix is bold everywhere it appears, including in `[T]_{\sB}`-style expressions where the result is a matrix but the letter T is a map.

| Type | Meaning |
|---|---|
| `T, S \colon V \to W` | linear maps (always T, S, R; never f for a linear map) |
| `ST` | composition of linear maps: first T, then S |
| `\cL(V, W)`, `\cL(V)` | all linear maps V → W; operators on V |
| `T_A` | the map \( F^n \to F^m \), \( \x \mapsto A\x \) |
| `\ker T`, `\im T` | kernel, image |
| `\col(A)`, `\row(A)`, `\nul(A)` | column space (in F^m), row space (in M_{1×n}(F)), null space (in F^n) |
| `P_{ij}`, `D_i(c)`, `I + cE_{ij}` | elementary matrices: swap, scale, add; `E_{ij}` is the matrix unit |
| `\rank T`, `\nullity T` | dim im T, dim ker T |
| `\I`, `\I_n`, `\id_V` | identity matrix (bold); identity operator |
| `\A, \B, \C` | matrices, **bold** upright capitals (`\mathbf`), like vectors. Entries stay plain: `a_{ij}`, or `(\A)_{ij}`. The macros `\A … \Z` give the bold letters |
| `\A\tp` | transpose: `\tp` is `^{\top}`, rendered **A**⊤ |
| `\A^{*}` | conjugate transpose (and adjoint of an operator) |
| `\mtx{T}{\sB}{\sC}` | matrix of T from basis 𝓑 (input) to 𝓒 (output), rendered [T]_𝓑^𝓒; `[T]_{\sB}` when 𝓑 = 𝓒 |
| `\mtx{\id}{\sB}{\sC}` | change-of-coordinates matrix from 𝓑 to 𝓒 |
| `\tr A`, `\det A` | trace, determinant |
| `\adj A` | adjugate |
| `M_{ij}`, `C_{ij} = (-1)^{i+j}M_{ij}` | minor (det of A with row i and column j deleted) and cofactor |
| `\diag(d_1, \dots, d_n)` | diagonal matrix |
| `A \oplus B`, `A_1 \oplus \dots \oplus A_r` | direct sum of **square** matrices: the block diagonal matrix with diagonal blocks A, B (Ch 7). A matrix, not a subspace; order matters. It is the matrix of an operator on U ⊕ W that maps U into U and W into W, in an adapted basis |
| `M/A`, `M/D` | Schur complement of an invertible block of the block matrix M with blocks A, B (top) and C, D (bottom): M/A = D − CA⁻¹B, M/D = A − BD⁻¹C (Ch 7). Not a quotient space V/U |
| `A \sim B` | similar |
| `M \approx N` | equivalent over F[x] (Ch 9 §07): N = UMV with U, V invertible over F[x]. Elsewhere `\approx` means "approximately equal"; the two uses never meet |
| `A \simeq B` | **congruent** (Ch 13 §02): B = P⊤AP for some invertible P, over the field named. The relation of forms, as `\sim` is the relation of maps. Chosen to sit beside `\sim` without colliding with it, with `\approx` (equivalence over F[x]) or with `\cong` (isomorphic); `\simeq` has no other use in the book |
| `T'` | dual map (transpose of T) W* → V*. The star is reserved for adjoints |
| `\A'(t)`, `\x'(t)` | the derivative of a matrix- or vector-valued function of a real variable, taken entrywise (Ch 9 §09, Ch 15 §06). The prime on a **map** is the dual map above; the two never meet, since a dual map is not a function of t |
| `V^{*}`, `\v^{*}` / `\varphi` | dual space; functionals are Greek letters φ, ψ |
| `U^{0}` | annihilator of U in V* |
| `\codim U` | codimension, dim V/U |
| `V^{**}`, `\ev_{\v}`, `\ev_V` | double dual; evaluation at v, φ ↦ φ(v), an element of V**; the evaluation map V → V**, v ↦ ev_v |
| `\GL_n(F)`, `\SL_n(F)` | general and special linear groups |

## Polynomials, eigenvalues, canonical forms

| Type | Meaning |
|---|---|
| `p_T(x) = \det(xI - T)` | characteristic polynomial (monic) |
| `m_T(x)` | minimal polynomial |
| `\operatorname{mult}_c(f)` | multiplicity of c as a root of f |
| `\langle p \rangle`, `\langle f_1, \dots, f_k \rangle` | ideal of F[x] generated by p (all multiples hp) or by f_1, …, f_k (all a_1f_1 + ⋯ + a_kf_k, a_i ∈ F[x]). Not an inner product (that is `\inner{\u}{\v}`) |
| `\spec(T)` | set of eigenvalues |
| `E_\lambda(T) = \ker(T - \lambda I)` | eigenspace |
| `a_T(\lambda)`, `g_T(\lambda)` | algebraic multiplicity mult_λ(p_T) and geometric multiplicity dim E_λ(T) of λ (Ch 8); `a(\lambda)`, `g(\lambda)` when T is clear. For a matrix, `a_A`, `g_A` |
| `G_\lambda(T) = \ker(T - \lambda I)^{n}` | generalized eigenspace |
| `\J_k(\lambda)` | k×k Jordan block (a matrix, so bold), λ on the diagonal, 1 on the **super**diagonal |
| `\vLambda(\lambda)` | rotation-scaling block of a conjugate pair: the 2×2 real matrix with rows (a, −b), (b, a), for λ = a + bi (Ch 9) |
| `\C_k(\lambda)` | 2k×2k **real** Jordan block for the pair {λ, λ̄}, λ ∉ ℝ: **Λ**(λ) on the diagonal, I₂ on the **super**diagonal, in 2×2 blocks (Ch 9). Not a companion matrix |
| `\C(p)` | companion matrix of a monic p: 1 just below the diagonal, last column (−a₀, …, −a_{n−1}) |
| `Z(\v; T)` | cyclic subspace generated by v: the span of v, Tv, T²v, … (Ch 9) |
| `m_{T,\v}` | the T-annihilator of v: the monic generator of { p ∈ F[x] : p(T)v = 0 }. For a matrix, `m_{A,\v}` |
| `d_1 \mid d_2 \mid \dots \mid d_r` | invariant factors of T, with **d_r = m_T** and d₁⋯d_r = p_T (Ch 9). Their prime-power factors are the elementary divisors |
| `\vPi` | the limit matrix of a convergent stochastic A: lim Aᵐ (Ch 9 §10) |
| `\rho(A)` | spectral radius |
| `e^{A}` | matrix exponential |

## Inner products and spectral theory

| Type | Meaning |
|---|---|
| `\inner{\u}{\v}` | inner product, **linear in the first slot**, conjugate-linear in the second |
| `\inner{\x}{\y}_{\A}` | the A-inner product \( \y^{*}\A\x \) of a positive definite A (Ch 12 §04); the plain \( \inner{\cdot}{\cdot} \) is always the ambient one |
| `\B - \lambda\A` | a matrix pencil; its generalized eigenvalues solve \( \B\x = \lambda\A\x \) (Ch 12 §04) |
| `\delta_{ij}` | Kronecker delta: 1 when i = j, 0 otherwise |
| `\G` | Gram matrix of a list \( (\v_1, \dots, \v_k) \): \( (\G)_{ij} = \inner{\v_j}{\v_i} \), the index order chosen so that \( \G \) is Hermitian and \( \x^{*}\G\x = \norm{\sum x_j\v_j}^2 \) (Ch 10 §02, §06). **Local override:** in Ch 10 §08 `\G(i, j; c, s)` is a Givens rotation, which is the universal letter for it; no Gram matrix appears in that section, and the Givens form always carries its arguments on first use |
| `P_n`, `T_n` | Legendre and Chebyshev polynomials (Ch 10 §§09–10), where both names are universal. §09 does use `P_U` and `P_{W_n}` for projections a few lines away, so keep the subscript doing the work: a subspace subscript means a projection, an integer subscript a polynomial, and §09 never abbreviates Legendre as `P_n` |
| `\norm{\v}` | norm (induced unless stated) |
| `\norm{\A}_F` | Frobenius norm of a matrix: \( \bigl(\sum_{i,j}\lvert a_{ij}\rvert^2\bigr)^{1/2} = \sqrt{\tr(\A^{*}\A)} \), the norm induced by the Frobenius inner product \( \inner{\A}{\B} = \tr(\B^{*}\A) \) of Ch 10 §01, given this symbol in Ch 11 §11. Unitarily invariant: \( \norm{\U\A\V}_F = \norm{\A}_F \) for unitary \( \U, \V \). The subscript is obligatory, since bare `\norm{\cdot}` is the vector norm |
| `U^{\perp}` | orthogonal complement |
| `P_U` | orthogonal projection onto U |
| `T^{*}` | adjoint |
| `\Orth(n), \SO(n), \Unit(n)` | orthogonal, special orthogonal, unitary groups |
| `\Orth(p, q)`, `\I_{p,q}` | the isometry group of the real form of signature (p, q), and its standard matrix \( \I_p \oplus (-\I_q) \) (Ch 13 §10) |
| `\Sp(2m, F)`, `\vOmega_{2m}` | symplectic group, and the standard alternating matrix with blocks \( \0, \I_m; -\I_m, \0 \) (Ch 13 §§09–10). Both macros already exist in `latex/macros.tex` |
| `\operatorname{Isom}(\beta)` | the isometry group of a form, \( \{\P : \P\tp\A\P = \A\} \) (Ch 13 §10). Spelled with `\operatorname`, matching `\operatorname{rad}`; deliberately not written \( \Orth(\A) \), which would call the symplectic group orthogonal |
| `U \perp W` | orthogonal direct sum with respect to a form: a direct sum whose summands pair to zero (Ch 13 §§07–09) |
| `\operatorname{ind}(\beta)` | Witt index: the largest dimension of a totally isotropic subspace, equal to the number of hyperbolic planes in any Witt decomposition (Ch 13 §07) |
| `\H_f(\a)` | Hessian matrix of a twice-differentiable f at a point a (Ch 13 §06) |
| `(V, \beta) \cong (V', \beta')` | **isometric** bilinear spaces (Ch 13 §08). This overloads `\cong`, which elsewhere means isomorphic as vector spaces; between spaces *carrying forms* it always means isometric, and Ch 13 §08 says so at the definition. An isometry is in particular an isomorphism, so the two never disagree |
| `U^{\perp_\beta}` | the orthogonal complement of U with respect to a bilinear form \( \beta \) (Ch 13 §§01, 07, 09). The unadorned \( U^{\perp} \) is always the inner-product one |
| `A \succeq 0`, `A \succ 0` | positive semidefinite / definite (Hermitian implied) |
| `A \succeq B` | Loewner order |
| `\lambda_1(A) \ge \dots \ge \lambda_n(A)` | eigenvalues of a Hermitian A, **decreasing** |
| `R_{\A}(\x)`, `R_T(\v)` | the **Rayleigh quotient** \( \inner{\A\x}{\x}/\inner{\x}{\x} \) of a Hermitian A at x ≠ 0 (Ch 16 §01, `def-rayleigh-quotient`), and of a self-adjoint operator T. Plain italic R: it is a function, not a matrix, so it is never the bold macro `\R`. The increasing-index form of the min–max theorem appears once, as a remark in Ch 16 §02, and nowhere else |
| `\sigma_1(A) \ge \dots \ge \sigma_{\min(m,n)}(A) \ge 0` | singular values, decreasing |
| `A^{+}` | Moore–Penrose pseudoinverse |
| `A^{1/2}` | positive square root |
| `\lvert A \rvert = (A^{*}A)^{1/2}` | absolute value |

## Forms, tensors, analysis

| Type | Meaning |
|---|---|
| `\beta \colon V \times V \to F` | bilinear form. `q(\v) = \beta(\v, \v)` is a quadratic form |
| `\mtx{\beta}{\sB}{}` | Gram matrix of a bilinear form: \( (\mtx{\beta}{\sB}{})_{ij} = \beta(\v_i, \v_j) \), indices **uncrossed** (Ch 13 §01). Chapter 10's `\G` (`def-gram-matrix`) crosses them, \( \inner{\v_j}{\v_i} \), to stay Hermitian under a conjugate-linear second slot. The two agree for real symmetric data and are transposes otherwise; Ch 13 §01 says so where it matters |
| `(n_+, n_-, n_0)` | inertia of a real symmetric form: the counts of positive, negative and zero entries in any diagonalization, the same for all of them by Sylvester's law (Ch 13 §05). The **signature** is the pair \( (n_+, n_-) \); the single integer \( n_+ - n_- \) is also called that elsewhere, and Ch 13 §05 says so. Plain subscripts, no macro |
| `\operatorname{In}(\A)` | the **inertia triple** \( (n_+(\A), n_-(\A), n_0(\A)) \) of a Hermitian \( \A \): its numbers of positive, negative and zero eigenvalues with multiplicity, added entrywise (Ch 16 §10). For real symmetric \( \A \) it is the triple of the row above, by Ch 13 §05's thm-inertia-from-eigenvalues. Spelled with `\operatorname`, like `\operatorname{rad}`; no macro |
| `\cH(\A)` | the **Hermitian dilation** of \( \A \in M_{m \times n} \): the \( (m+n) \times (m+n) \) Hermitian matrix with blocks \( \0, \A \) on top and \( \A^{*}, \0 \) below, whose eigenvalues are \( \pm\sigma_i(\A) \) and zeros (Ch 16 §09). Calligraphic, so it never meets the Hessian \( \H_f(\a) \) of Ch 13 §06, which is bold |
| `\operatorname{rad}(\beta)` | radical of a bilinear form (Ch 13 §01): { v ∈ V : β(u, v) = 0 for every u ∈ V }, the kernel of v ↦ β(·, v). β is non-degenerate exactly when it is {0}. Spelled out with `\operatorname`, not a macro |
| `V \otimes W`, `\v \otimes \w` | tensor product |
| `\cM(V_1, \dots, V_k; W)` | the space of **multilinear maps** \( V_1 \times \dots \times V_k \to W \) (Ch 14 §01), with the pointwise operations. The semicolon separates inputs from output, which is what distinguishes it from `\cL(V, W)`; for \( k = 1 \) the two agree, and for \( W = F \) its elements are the multilinear forms of Ch 6 §02 |
| `F^{(S)}` | the **free vector space** on a set \( S \) over \( F \) (Ch 14 §02): the finitely supported functions \( S \to F \), with basis \( \{\delta_s\}_{s \in S} \). The parentheses are obligatory: \( F^{S} \) is **all** functions \( S \to F \) (Ch 1 §01), and the two differ as soon as \( S \) is infinite. Ch 1 §08 met the case \( S = \nN \) |
| `\Lambda^{k} V`, `\v_1 \wedge \dots \wedge \v_k` | exterior power |
| `\Sym^{k} V` | symmetric power |
| `V^{\otimes k}` | the k-th tensor power of V (Ch 14 §06): the universal target for k-linear maps out of V^k, with basis the simple tensors on index k-tuples and dim = n^k. `V^{\otimes 0} = F` and `V^{\otimes 1} = V` by convention |
| `\operatorname{T}(V)` | the tensor algebra ⊕_{k≥0} V^{⊗k} (Ch 14 §06). Spelled with `\operatorname`, like `\operatorname{rad}` and `\operatorname{Cl}`, so the upright T is never read as the italic T of a linear map; no macro |
| `\Sym(V)`, `\v_1\v_2\cdots\v_k` | the symmetric algebra ⊕_{k≥0} Sym^k V (Ch 14 §07), and the symmetric product of k vectors, written by **juxtaposition** of the bold letters. Juxtaposition is chosen so that the isomorphism Sym(V) ≅ F[x_1, …, x_n] reads as an equality of monomials |
| `F[x_1, \dots, x_n]` | the polynomial algebra in n variables (Ch 14 §07): the space with basis the monomials x^a, a ∈ ℕ^n, multiplied by x^a x^b = x^{a+b}. For n = 1 it is the ring F[x] of def-polynomial-ring; `F[x_1, \dots, x_n]_k` is the span of the monomials of degree k |
| `\Lambda^{k} V` (plain Λ) | plain `\Lambda` is free for the exterior power: the bold `\vLambda` of Chapter 9 is a matrix and always carries its argument λ, so the two never collide (Ch 14 §08) |
| `A \otimes B` | Kronecker product of matrices |
| `\Lambda V`, `\e_{S}` | the exterior algebra \( \bigoplus_k \Lambda^k V \), and the basis element \( \e_{i_1} \wedge \dots \wedge \e_{i_k} \) for an increasing index set S, written \( \e_{12} \) for \( S = \{1,2\} \) (Ch 14 §§08–10). Distinct from the bold \( \vLambda \) of Ch 9 §04 |
| `\varepsilon_{\v}` | wedging by a fixed vector, \( \omega \mapsto \v \wedge \omega \) (Ch 14 §09) |
| `\cI`, `\cI_q` | a two-sided ideal of an algebra, and the one generated by \( \v \otimes \v - q(\v)1 \) whose quotient is the Clifford algebra (Ch 14 §10). Not Ch 5's ideal of F[x], though the idea is the same |
| `\sB \otimes \sC` | the ordered product basis of \( V \otimes W \): \( \v_i \otimes \w_k \) in dictionary order, first factor slow (Ch 14 §03). That ordering is what makes the matrix of \( S \otimes T \) equal \( [S] \otimes [T] \); the other order gives \( [T] \otimes [S] \) |
| `V^{\otimes p}`, `T^p_q(V)` | tensor powers, with \( V^{\otimes 0} = F \), and mixed tensors \( V^{\otimes p} \otimes (V^{*})^{\otimes q} \) of type (p, q) (Ch 14 §§04, 06) |
| `C`, `C^a_b` | contraction \( V^{*} \otimes V \to F \), and contraction of the a-th upper against the b-th lower slot (Ch 14 §04). Under \( \Theta \) it is the trace |
| `\Theta` | the natural isomorphism \( V^{*} \otimes W \to \cL(V, W) \) (Ch 14 §§02–04). §02's matrix model \( F^m \otimes F^n \cong M_{m \times n} \) is the same map, and §11 uses the letter again for \( V \otimes W \to \cL(W^{*}, V) \) — the same construction with the factors read the other way round, which §11 says where it does it |
| `(V^{\otimes k})^{S_k}` | the symmetric tensors: the elements fixed by every permutation of the slots (Ch 14 §07). Equal in dimension to \( \Sym^k V \) over every field, but **not** the same object — the natural map between them fails to be an isomorphism when \( \operatorname{char} F \le k \) |
| `T^{i_1 \dots i_p}_{j_1 \dots j_q}` | components of a tensor: upper indices for \( V \), lower for \( V^{*} \) (Ch 14 §05, which also states the summation convention and confines it to that section) |
| `\vecop X` | vectorization of a matrix: its columns stacked into one column, rendered vec X (Ch 7) |
| `A \circ B` | Hadamard (entrywise) product |
| `\J` | the all-ones matrix, every entry \( 1 \) (Ch 2 §07, Ch 11 §§02, 05, 08, 09). Distinct from the Jordan block \( \J_k(\lambda) \), which always carries its size and eigenvalue |
| `\cS_{\A,\B}` | the Sylvester operator \( \X \mapsto \A\X - \X\B \) on \( M_{m \times n} \) (Ch 11 §10) |
| index origin | subscripts start at 1 everywhere, with one announced exception: Ch 11 §09 runs rows, columns and entries from \( 0 \) to \( n-1 \), because circulant and Fourier subscripts are read modulo n |
| `\c \ast \d` | cyclic convolution of two vectors of length n, \( (\c \ast \d)_k = \sum_t c_t d_{k-t} \) with subscripts read modulo n (Ch 11 §09). The product of two circulants is the circulant of the convolution |
| `[A, B] = AB - BA` | commutator |
| `\norm{\x}_p` | p-norm. `\norm{A}_F` Frobenius, `\norm{A}_2` spectral/operator 2-norm. Ch 15 §01 defines and verifies \( p = 1, 2, \infty \); for general \( 1 \le p \le \infty \) the triangle inequality is Minkowski's inequality, proved in Ch 17 §11 (`cor-minkowski-inequality`) from Hölder's. \( q \) denotes the conjugate exponent, \( 1/p + 1/q = 1 \) |
| `\norm{f}_\infty` | the **sup norm** \( \max_{t \in [0,1]}\lvert f(t)\rvert \) on \( C[0,1] \) (Ch 15 §01), the same symbol as the \( \infty \)-norm on \( F^n \) and for the same reason. It is the standing infinite-dimensional example, where Ch 15 §02's equivalence theorem fails |
| `B_{\norm{\cdot}}` | the **closed unit ball** \( \{\v : \norm{\v} \le 1\} \) of a norm (Ch 15 §01). In \( F^n \), `B_1`, `B_2`, `B_\infty` are the balls of the three p-norms; the integer subscript names the norm, not a dimension |
| `\norm{A}` | operator norm induced by the named vector norm |
| `\norm{\A}_1`, `\norm{\A}_{\infty}` | the operator norms induced by the vector 1- and ∞-norms (Ch 15 §03): the largest column sum and the largest row sum. Distinct from the entrywise maximum, which is not even submultiplicative, and from \( \norm{f}_{\infty} \), the sup norm on a function space |
| `\kappa(A)` | condition number |
| `\conv S` | the **convex hull** of S, the set of all convex combinations of points of S (Ch 17 §01, `def-convex-hull`, `thm-convex-hull-combinations`) |
| `\operatorname{aff} S` | the **affine hull**, the set of affine combinations; a coset \( \x_0 + W_S \) (Ch 17 §01, `def-affine-hull`, `prp-affine-hull-coset`). No macro |
| `[\x, \y]` | the **segment** \( \{(1-t)\x + t\y : 0 \le t \le 1\} \) (Ch 17 §01). Always with bold vector arguments; not the commutator \( [A, B] \) |
| `\Delta_n` | the **standard simplex** \( \{t \in \nR^n : t_i \ge 0,\ \sum t_i = 1\} = \conv\{\e_1, \dots, \e_n\} \): n weights (Ch 17 §01, `def-standard-simplex`). Mixed strategies of a game live here (Ch 17 §07) |
| `\interior S`, `\closure S` | interior and closure of a subset of a finite-dimensional real space (Ch 17 §03, `def-interior-point`); closed and open are defined sequentially in `def-closed-set` (§01) |
| `P_C(\x)`, `d(\x, C)` | the **nearest point** of a non-empty closed convex set C to x, and the distance (Ch 17 §03, `thm-nearest-point`). For a subspace this is the orthogonal projection of Ch 10 |
| `p_K`, `h_K`, `K^{\circ}` | the **gauge**, **support function** (value \( +\infty \) allowed) and **polar set** of K (Ch 17 §04) |
| `\norm{\cdot}_{*}`, `\norm{\cdot}_{**}` | the **dual norm** \( \norm{\y}_* = \max_{\norm{\x}\le 1}\inner{\x}{\y} \) and the bidual, which is the norm itself (Ch 17 §04, `def-dual-norm`, `thm-dual-dual-norm`). Dual of \( \norm{\cdot}_p \) is \( \norm{\cdot}_q \) |
| `K^{*}` | the **dual cone** \( \{\y : \inner{\x}{\y} \ge 0 \ \forall \x \in K\} \) of a subset K, inside V itself (Ch 17 §05, `def-dual-cone`). Not the dual space \( V^* \); for a subspace it equals \( U^\perp \) and is not written this way |
| `\operatorname{cone}(\a_1, \dots, \a_m)`, `\operatorname{cone}(\A)` | the **finitely generated cone** (Ch 17 §05, `def-finitely-generated-cone`); \( \operatorname{cone}() = \{\0\} \). No macro |
| `\x \ge \0`, `\u \le \v`, `\nR^m_{\ge 0}` | **entrywise** order on real vectors, and the non-negative orthant (Ch 17 §05), extended to matrices in Ch 18: \( \A \ge 0 \), \( \A > 0 \) (every entry positive), \( \A \ge \B \). Unrelated to the Loewner \( \succeq \): a positive matrix need not be positive definite, nor conversely |
| `\lvert\M\rvert` (Ch 18) | the **entrywise** absolute value \( (\lvert m_{ij}\rvert) \). **Local override** of the Ch 12 row \( \lvert A\rvert = (A^*A)^{1/2} \), which does not appear in Ch 18 |
| `G(\A)` | the **directed graph** of a square matrix: vertices \( 1, \dots, n \), an edge \( j \to i \) whenever \( a_{ij} \ne 0 \) (column index to row index, matching \( \x_{k+1} = \A\x_k \)); walks, paths, strong connectivity (Ch 18 §02). No macro |
| Perron root, `\v`, `\w` | for \( \A > 0 \) or irreducible \( \A \ge 0 \): the Perron root \( \rho(\A) \), the right Perron vector \( \v > \0 \) with \( \1\tp\v = 1 \), and the left Perron vector \( \w > \0 \) with \( \w\tp\A = \rho\w\tp \) and **\( \w\tp\v = 1 \)** (Ch 18 §01 `def-perron-vector`, §03 `def-perron-root-and-vectors`) |
| `\underline{r}_{\A}(\x)`, `\overline{r}_{\A}(\x)` | the lower and upper **Collatz–Wielandt functions** (Ch 18 §04). The bars are **not** conjugation (`\conj`) or closure (`\closure`); R_A is the Rayleigh quotient, so these avoid it |
| \( h \), \( \omega = e^{2\pi i/h} \) | the **period** of an irreducible \( \A \ge 0 \) (gcd of closed-walk lengths), equal to the number of peripheral eigenvalues (Ch 18 §05, `def-period`, `thm-peripheral-spectrum`) |
| `\W_n` (Ch 18 §05) | the Wielandt matrix, primitive with exponent exactly \( (n-1)^2+1 \). Bold W, not the subspace W |
| `\Q`, `\R`, `\N` (Ch 18 §06) | an absorbing chain's transient block, absorbing block, and fundamental matrix \( \N = (\I - \Q)^{-1} \); absorption probabilities \( \R\N \) |
| `W_n` (Ch 18 §07) | the real \( n\times n \) matrices with all row and column sums zero; \( \dim W_n = (n-1)^2 \), and \( \Omega_n \) lies in the coset \( \tfrac1n\J + W_n \) |
| `\G`, `\H`, \( \alpha \) (Ch 18 §08) | the Google matrix \( \alpha\P + \tfrac{1-\alpha}{n}\J \) and the raw hyperlink matrix, **local overrides** of the Gram matrix and the Hessian; \( \alpha \in (0,1) \) the damping factor |
| `\K_n` | the \( n\times n \) second-difference matrix (2 on the diagonal, \( -1 \) beside it), a non-singular M-matrix (Ch 18 §09; Ch 6 exercise) |
| `v(\A)` | the **value** of the matrix game with payoff matrix A (Ch 17 §07, `def-value-of-game`) |
| `\operatorname{ext} C`, `W_C`, `\dim C` | the **extreme points** of C; the direction space and dimension of a non-empty convex set, \( \dim C = \dim \operatorname{aff} C \) (Ch 17 §01, §08) |
| `\cD_n`, `\Omega_n` | the real **density matrices** \( \{X = X\tp \succeq 0, \tr X = 1\} \) and the **doubly stochastic** matrices (Ch 17 §08, `def-density-matrix`, `def-doubly-stochastic`). Plain \( \Omega \), not the bold symplectic \( \vOmega_{2m} \) of Ch 13 |
| `I(\x)`, `\A_I` | the active set of a point of \( \{\A\x \le \b\} \) and the matrix of its active rows (Ch 17 §09) |
| `\operatorname{epi} f` | the **epigraph** \( \{(\x, s) : s \ge f(\x)\} \) (Ch 17 §10) |
| `\log`, `t^r` | the natural logarithm, built as the inverse of exp in Ch 17 §11 (`lem-exp-log`), and real powers \( t^r = e^{r\log t} \) for \( t > 0 \), \( 0^r = 0 \) for \( r > 0 \). This gives Ch 15 §01's \( \norm{\cdot}_p \) its meaning |
| `s_k(\A)` | \( \lambda_1(\A) + \dots + \lambda_k(\A) \), the Ky Fan partial sum (Ch 16 §06, reused in Ch 17 §10) |
| `\vol` | volume: of a parallelepiped, \|det\| (Ch 6); extended in Ch 12 §03 to the k-dimensional volume of a list of any length in any inner product space, by the base-times-height recursion of `def-k-volume`. The two agree wherever both apply, and Ch 12 §03 proves it |
| `\x \prec \y`, `\x \prec_w \y`, `\x^{\downarrow}` | **majorization** and **weak (sub)majorization** of real vectors, written with bold vectors (Ch 16 §08, `def-majorization`). \( \x^{\downarrow} \) is \( \x \) sorted decreasingly. \( \x \prec_w \y \): every top-\( k \) partial sum of \( \x^{\downarrow} \) is at most that of \( \y^{\downarrow} \); \( \x \prec \y \) adds equal totals. **It is a preorder on \( \nR^n \), not a partial order** — (1,0) ≺ (0,1) ≺ (1,0) |
| `\d(\A)` | the **diagonal vector** \( (a_{11}, \dots, a_{nn}) \in \nR^n \) of a Hermitian \( \A \), in its given order (Ch 16 §08). Bold because it is a vector; distinct from `\diag(d_1,\dots,d_n)`, which **builds a matrix** |
| `\vlambda(\A)` | the **eigenvalue vector** \( (\lambda_1(\A), \dots, \lambda_n(\A)) \) of a Hermitian \( \A \), decreasing (Ch 16 §§07–08) |
| `\cW = (W_1, \dots, W_k)` | a **flag** of subspaces \( W_1 \subset \dots \subset W_k \) of type \( (i_1 < \dots < i_k) \), \( \dim W_j = i_j \), and a list **adapted** to it (Ch 16 §07, `def-flag-adapted-list`) |
| `x^{\downarrow}` | decreasing rearrangement |

## Label naming

Labels are global and must be unique across the book.

- **Format:** `<env>-<topic words>`, e.g. `def-linear-independence`, `thm-rank-nullity`, `lem-exchange`, `exm-rotation-no-real-eigenvalues`.
- **Exercises:** `exr-<section-slug>-<group><n>`, e.g. `exr-span-b2`.
- **Before creating a label**, check it is free: `grep -rn "#thm-rank-nullity" src`.
- **Existing labels** of results that survive a rewrite keep their exact label, so links stay stable.
