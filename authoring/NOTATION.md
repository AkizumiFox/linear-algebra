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

**Bold is for matrices and vectors, never for maps or spaces.** A matrix is bold (`\A`), a vector is bold lowercase (`\v`), an operator or linear map is plain italic (T, S), and a vector space is plain italic (V, U, W). A Greek letter that names a matrix is bold too, through `\vLambda`, `\vPi`, … , which render bold upright like `\A`. A letter that names a matrix is bold everywhere it appears. The converse matters too: the argument of `\mtx` is the **map**, so it stays plain italic even though the result is a matrix — write `\mtx{T}{\sB}{\sB}`, never `\mtx{\T}{\sB}{\sB}`.

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
| `\mtx{T}{\sB}{\sC}` | matrix of T from basis 𝓑 (input) to 𝓒 (output), rendered [T]_𝓑^𝓒. The subscript is the basis on the first slot, the superscript the basis on the second; **both are always written**, so an operator in one basis is `\mtx{T}{\sB}{\sB}`, never the same call with the third argument left empty |
| `\mtx{\id}{\sB}{\sC}` | change-of-coordinates matrix from 𝓑 to 𝓒 |
| `\tr A`, `\det A` | trace, determinant |
| `\adj A` | adjugate |
| `M_{ij}`, `C_{ij} = (-1)^{i+j}M_{ij}` | minor (det of A with row i and column j deleted) and cofactor |
| `\diag(d_1, \dots, d_n)` | diagonal matrix |
| `A \oplus B`, `A_1 \oplus \dots \oplus A_r` | direct sum of **square** matrices: the block diagonal matrix with diagonal blocks A, B (Ch 8). A matrix, not a subspace; order matters. It is the matrix of an operator on U ⊕ W that maps U into U and W into W, in an adapted basis |
| `M/A`, `M/D` | Schur complement of an invertible block of the block matrix M with blocks A, B (top) and C, D (bottom): M/A = D − CA⁻¹B, M/D = A − BD⁻¹C (Ch 8). Not a quotient space V/U |
| `A \sim B` | similar |
| `M \approx N` | equivalent over F[x] (Ch 10 §07): N = UMV with U, V invertible over F[x]. Elsewhere `\approx` means "approximately equal"; the two uses never meet |
| `A \simeq B` | **congruent** (Ch 14 §02): B = P⊤AP for some invertible P, over the field named. The relation of forms, as `\sim` is the relation of maps. Chosen to sit beside `\sim` without colliding with it, with `\approx` (equivalence over F[x]) or with `\cong` (isomorphic); `\simeq` has no other use in the book |
| `T'` | dual map (transpose of T) W* → V*. The star is reserved for adjoints |
| `\A'(t)`, `\x'(t)` | the derivative of a matrix- or vector-valued function of a real variable, taken entrywise (Ch 10 §09, Ch 16 §06). The prime on a **map** is the dual map above; the two never meet, since a dual map is not a function of t |
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
| `a_T(\lambda)`, `g_T(\lambda)` | algebraic multiplicity mult_λ(p_T) and geometric multiplicity dim E_λ(T) of λ (Ch 9); `a(\lambda)`, `g(\lambda)` when T is clear. For a matrix, `a_A`, `g_A` |
| `G_\lambda(T) = \ker(T - \lambda I)^{n}` | generalized eigenspace |
| `\J_k(\lambda)` | k×k Jordan block (a matrix, so bold), λ on the diagonal, 1 on the **super**diagonal |
| `\vLambda(\lambda)` | rotation-scaling block of a conjugate pair: the 2×2 real matrix with rows (a, −b), (b, a), for λ = a + bi (Ch 10) |
| `\C_k(\lambda)` | 2k×2k **real** Jordan block for the pair {λ, λ̄}, λ ∉ ℝ: **Λ**(λ) on the diagonal, I₂ on the **super**diagonal, in 2×2 blocks (Ch 10). Not a companion matrix |
| `\C(p)` | companion matrix of a monic p: 1 just below the diagonal, last column (−a₀, …, −a_{n−1}) |
| `Z(\v; T)` | cyclic subspace generated by v: the span of v, Tv, T²v, … (Ch 10) |
| `m_{T,\v}` | the T-annihilator of v: the monic generator of { p ∈ F[x] : p(T)v = 0 }. For a matrix, `m_{A,\v}` |
| `d_1 \mid d_2 \mid \dots \mid d_r` | invariant factors of T, with **d_r = m_T** and d₁⋯d_r = p_T (Ch 10). Their prime-power factors are the elementary divisors |
| `\vPi` | the limit matrix of a convergent stochastic A: lim Aᵐ (Ch 10 §10) |
| `\rho(A)` | spectral radius |
| `e^{A}` | matrix exponential |

## Inner products and spectral theory

| Type | Meaning |
|---|---|
| `\inner{\u}{\v}` | inner product, **linear in the first slot**, conjugate-linear in the second |
| `\inner{\x}{\y}_{\A}` | the A-inner product \( \y^{*}\A\x \) of a positive definite A (Ch 13 §04); the plain \( \inner{\cdot}{\cdot} \) is always the ambient one |
| `\B - \lambda\A` | a matrix pencil; its generalized eigenvalues solve \( \B\x = \lambda\A\x \) (Ch 13 §04) |
| `\delta_{ij}` | Kronecker delta: 1 when i = j, 0 otherwise |
| `\G` | Gram matrix of a list \( (\v_1, \dots, \v_k) \): \( (\G)_{ij} = \inner{\v_j}{\v_i} \), the index order chosen so that \( \G \) is Hermitian and \( \x^{*}\G\x = \norm{\sum x_j\v_j}^2 \) (Ch 11 §02, §06). **Local override:** in Ch 11 §08 `\G(i, j; c, s)` is a Givens rotation, which is the universal letter for it; no Gram matrix appears in that section, and the Givens form always carries its arguments on first use |
| `P_n`, `T_n` | Legendre and Chebyshev polynomials (Ch 11 §§09–10), where both names are universal. §09 does use `P_U` and `P_{W_n}` for projections a few lines away, so keep the subscript doing the work: a subspace subscript means a projection, an integer subscript a polynomial, and §09 never abbreviates Legendre as `P_n` |
| `\norm{\v}` | norm (induced unless stated) |
| `\norm{\A}_F` | Frobenius norm of a matrix: \( \bigl(\sum_{i,j}\lvert a_{ij}\rvert^2\bigr)^{1/2} = \sqrt{\tr(\A^{*}\A)} \), the norm induced by the Frobenius inner product \( \inner{\A}{\B} = \tr(\B^{*}\A) \) of Ch 11 §01, given this symbol in Ch 11 §07. Unitarily invariant: \( \norm{\U\A\V}_F = \norm{\A}_F \) for unitary \( \U, \V \). The subscript is obligatory, since bare `\norm{\cdot}` is the vector norm |
| `U^{\perp}` | orthogonal complement |
| `P_U` | orthogonal projection onto U |
| `T^{*}` | adjoint |
| `\Orth(n), \SO(n), \Unit(n)` | orthogonal, special orthogonal, unitary groups |
| `\Orth(p, q)`, `\I_{p,q}` | the isometry group of the real form of signature (p, q), and its standard matrix \( \I_p \oplus (-\I_q) \) (Ch 14 §10) |
| `\Sp(2m, F)`, `\vOmega_{2m}` | symplectic group, and the standard alternating matrix with blocks \( \0, \I_m; -\I_m, \0 \) (Ch 14 §§09–10). Both macros already exist in `latex/macros.tex` |
| `\operatorname{Isom}(\beta)` | the isometry group of a form, \( \{\P : \P\tp\A\P = \A\} \) (Ch 14 §10). Spelled with `\operatorname`, matching `\operatorname{rad}`; deliberately not written \( \Orth(\A) \), which would call the symplectic group orthogonal |
| `U \perp W` | orthogonal direct sum with respect to a form: a direct sum whose summands pair to zero (Ch 14 §§07–09) |
| `\operatorname{ind}(\beta)` | Witt index: the largest dimension of a totally isotropic subspace, equal to the number of hyperbolic planes in any Witt decomposition (Ch 14 §07) |
| `\H_f(\a)` | Hessian matrix of a twice-differentiable f at a point a (Ch 14 §06) |
| `(V, \beta) \cong (V', \beta')` | **isometric** bilinear spaces (Ch 14 §08). This overloads `\cong`, which elsewhere means isomorphic as vector spaces; between spaces *carrying forms* it always means isometric, and Ch 14 §08 says so at the definition. An isometry is in particular an isomorphism, so the two never disagree |
| `U^{\perp_\beta}` | the orthogonal complement of U with respect to a bilinear form \( \beta \) (Ch 14 §§01, 07, 09). The unadorned \( U^{\perp} \) is always the inner-product one |
| `A \succeq 0`, `A \succ 0` | positive semidefinite / definite (Hermitian implied) |
| `A \succeq B` | Loewner order |
| `\lambda_1(A) \ge \dots \ge \lambda_n(A)` | eigenvalues of a Hermitian A, **decreasing** |
| `R_{\A}(\x)`, `R_T(\v)` | the **Rayleigh quotient** \( \inner{\A\x}{\x}/\inner{\x}{\x} \) of a Hermitian A at x ≠ 0 (Ch 17 §01, `def-rayleigh-quotient`), and of a self-adjoint operator T. Plain italic R: it is a function, not a matrix, so it is never the bold macro `\R`. The increasing-index form of the min–max theorem appears once, as a remark in Ch 17 §02, and nowhere else |
| `\sigma_1(A) \ge \dots \ge \sigma_{\min(m,n)}(A) \ge 0` | singular values, decreasing |
| `A^{+}` | Moore–Penrose pseudoinverse |
| `A^{1/2}` | positive square root |
| `\lvert A \rvert = (A^{*}A)^{1/2}` | absolute value |

## Forms, tensors, analysis

| Type | Meaning |
|---|---|
| `\beta \colon V \times V \to F` | bilinear form. `q(\v) = \beta(\v, \v)` is a quadratic form |
| `\mtx{\beta}{\sB}{\sB}` | Gram matrix of a bilinear form: \( (\mtx{\beta}{\sB}{\sB})_{ij} = \beta(\v_i, \v_j) \), indices **uncrossed** (Ch 14 §01). The subscript is the basis fed to the first slot of the form and the superscript the basis fed to the second; Ch 14 uses the same basis on both, and writes it twice rather than leaving the superscript empty. Chapter 11's `\G` (`def-gram-matrix`) crosses them, \( \inner{\v_j}{\v_i} \), to stay Hermitian under a conjugate-linear second slot. The two agree for real symmetric data and are transposes otherwise; Ch 14 §01 says so where it matters |
| `(n_+, n_-, n_0)` | inertia of a real symmetric form: the counts of positive, negative and zero entries in any diagonalization, the same for all of them by Sylvester's law (Ch 14 §05). The **signature** is the pair \( (n_+, n_-) \); the single integer \( n_+ - n_- \) is also called that elsewhere, and Ch 14 §05 says so. Plain subscripts, no macro |
| `\operatorname{In}(\A)` | the **inertia triple** \( (n_+(\A), n_-(\A), n_0(\A)) \) of a Hermitian \( \A \): its numbers of positive, negative and zero eigenvalues with multiplicity, added entrywise (Ch 17 §10). For real symmetric \( \A \) it is the triple of the row above, by Ch 14 §05's thm-inertia-from-eigenvalues. Spelled with `\operatorname`, like `\operatorname{rad}`; no macro |
| `\cH(\A)` | the **Hermitian dilation** of \( \A \in M_{m \times n} \): the \( (m+n) \times (m+n) \) Hermitian matrix with blocks \( \0, \A \) on top and \( \A^{*}, \0 \) below, whose eigenvalues are \( \pm\sigma_i(\A) \) and zeros (Ch 17 §09). Calligraphic, so it never meets the Hessian \( \H_f(\a) \) of Ch 14 §06, which is bold |
| `\operatorname{rad}(\beta)` | radical of a bilinear form (Ch 14 §01): { v ∈ V : β(u, v) = 0 for every u ∈ V }, the kernel of v ↦ β(·, v). β is non-degenerate exactly when it is {0}. Spelled out with `\operatorname`, not a macro |
| `V \otimes W`, `\v \otimes \w` | tensor product |
| `\cM(V_1, \dots, V_k; W)` | the space of **multilinear maps** \( V_1 \times \dots \times V_k \to W \) (Ch 15 §01), with the pointwise operations. The semicolon separates inputs from output, which is what distinguishes it from `\cL(V, W)`; for \( k = 1 \) the two agree, and for \( W = F \) its elements are the multilinear forms of Ch 7 §02 |
| `F^{(S)}` | the **free vector space** on a set \( S \) over \( F \) (Ch 15 §02): the finitely supported functions \( S \to F \), with basis \( \{\delta_s\}_{s \in S} \). The parentheses are obligatory: \( F^{S} \) is **all** functions \( S \to F \) (Ch 1 §01), and the two differ as soon as \( S \) is infinite. Ch 1 §08 met the case \( S = \nN \) |
| `\Lambda^{k} V`, `\v_1 \wedge \dots \wedge \v_k` | exterior power |
| `\Sym^{k} V` | symmetric power |
| `V^{\otimes k}` | the k-th tensor power of V (Ch 15 §06): the universal target for k-linear maps out of V^k, with basis the simple tensors on index k-tuples and dim = n^k. `V^{\otimes 0} = F` and `V^{\otimes 1} = V` by convention |
| `\operatorname{T}(V)` | the tensor algebra ⊕_{k≥0} V^{⊗k} (Ch 15 §06). Spelled with `\operatorname`, like `\operatorname{rad}` and `\operatorname{Cl}`, so the upright T is never read as the italic T of a linear map; no macro |
| `\Sym(V)`, `\v_1\v_2\cdots\v_k` | the symmetric algebra ⊕_{k≥0} Sym^k V (Ch 15 §07), and the symmetric product of k vectors, written by **juxtaposition** of the bold letters. Juxtaposition is chosen so that the isomorphism Sym(V) ≅ F[x_1, …, x_n] reads as an equality of monomials |
| `F[x_1, \dots, x_n]` | the polynomial algebra in n variables (Ch 15 §07): the space with basis the monomials x^a, a ∈ ℕ^n, multiplied by x^a x^b = x^{a+b}. For n = 1 it is the ring F[x] of def-polynomial-ring; `F[x_1, \dots, x_n]_k` is the span of the monomials of degree k |
| `\Lambda^{k} V` (plain Λ) | plain `\Lambda` is free for the exterior power: the bold `\vLambda` of Chapter 10 is a matrix and always carries its argument λ, so the two never collide (Ch 15 §08) |
| `A \otimes B` | Kronecker product of matrices |
| `\Lambda V`, `\e_{S}` | the exterior algebra \( \bigoplus_k \Lambda^k V \), and the basis element \( \e_{i_1} \wedge \dots \wedge \e_{i_k} \) for an increasing index set S, written \( \e_{12} \) for \( S = \{1,2\} \) (Ch 15 §§08–10). Distinct from the bold \( \vLambda \) of Ch 10 §04 |
| `\varepsilon_{\v}` | wedging by a fixed vector, \( \omega \mapsto \v \wedge \omega \) (Ch 15 §09) |
| `\cI`, `\cI_q` | a two-sided ideal of an algebra, and the one generated by \( \v \otimes \v - q(\v)1 \) whose quotient is the Clifford algebra (Ch 15 §10). Not Ch 6's ideal of F[x], though the idea is the same |
| `\sB \otimes \sC` | the ordered product basis of \( V \otimes W \): \( \v_i \otimes \w_k \) in dictionary order, first factor slow (Ch 15 §03). That ordering is what makes the matrix of \( S \otimes T \) equal \( [S] \otimes [T] \); the other order gives \( [T] \otimes [S] \) |
| `V^{\otimes p}`, `T^p_q(V)` | tensor powers, with \( V^{\otimes 0} = F \), and mixed tensors \( V^{\otimes p} \otimes (V^{*})^{\otimes q} \) of type (p, q) (Ch 15 §§04, 06) |
| `C`, `C^a_b` | contraction \( V^{*} \otimes V \to F \), and contraction of the a-th upper against the b-th lower slot (Ch 15 §04). Under \( \Theta \) it is the trace |
| `\Theta` | the natural isomorphism \( V^{*} \otimes W \to \cL(V, W) \) (Ch 15 §§02–04). §02's matrix model \( F^m \otimes F^n \cong M_{m \times n} \) is the same map, and §11 uses the letter again for \( V \otimes W \to \cL(W^{*}, V) \) — the same construction with the factors read the other way round, which §11 says where it does it |
| `(V^{\otimes k})^{S_k}` | the symmetric tensors: the elements fixed by every permutation of the slots (Ch 15 §07). Equal in dimension to \( \Sym^k V \) over every field, but **not** the same object — the natural map between them fails to be an isomorphism when \( \operatorname{char} F \le k \) |
| `T^{i_1 \dots i_p}_{j_1 \dots j_q}` | components of a tensor: upper indices for \( V \), lower for \( V^{*} \) (Ch 15 §05, which also states the summation convention and confines it to that section) |
| `\vecop X` | vectorization of a matrix: its columns stacked into one column, rendered vec X (Ch 8) |
| `A \circ B` | Hadamard (entrywise) product |
| `\J` | the all-ones matrix, every entry \( 1 \) (Ch 3 §07, Ch 12 §§02, 05, 08, 09). Distinct from the Jordan block \( \J_k(\lambda) \), which always carries its size and eigenvalue |
| `\cS_{\A,\B}` | the Sylvester operator \( \X \mapsto \A\X - \X\B \) on \( M_{m \times n} \) (Ch 12 §10) |
| index origin | subscripts start at 1 everywhere, with three announced exceptions: Ch 12 §09 runs rows, columns and entries from \( 0 \) to \( n-1 \), because circulant and Fourier subscripts are read modulo n; and Ch 22 §§06–10 run the coordinates of \( F^{n+1} \) and its standard basis from \( 0 \), so that \( \nP^n(F) \) has \( n+1 \) coordinates and dimension \( n \) (announced at Ch 22 §06's `def-homogeneous-coordinates` and again at the head of §07); and Ch 23 §09 runs group elements, characters and the entries of the character matrix from \( 0 \) to \( n-1 \), following Ch 12 §09, announced at the head of that section (Ch 23 §08's table for \( \nZ/4\nZ \) is 0-based for the same reason) |
| `\c \ast \d` | cyclic convolution of two vectors of length n, \( (\c \ast \d)_k = \sum_t c_t d_{k-t} \) with subscripts read modulo n (Ch 12 §09). The product of two circulants is the circulant of the convolution |
| `[A, B] = AB - BA` | commutator |
| `\norm{\x}_p` | p-norm. `\norm{A}_F` Frobenius, `\norm{A}_2` spectral/operator 2-norm. Ch 16 §01 defines and verifies \( p = 1, 2, \infty \); for general \( 1 \le p \le \infty \) the triangle inequality is Minkowski's inequality, proved in Ch 18 §11 (`cor-minkowski-inequality`) from Hölder's. \( q \) denotes the conjugate exponent, \( 1/p + 1/q = 1 \) |
| `\norm{f}_\infty` | the **sup norm** \( \max_{t \in [0,1]}\lvert f(t)\rvert \) on \( C[0,1] \) (Ch 16 §01), the same symbol as the \( \infty \)-norm on \( F^n \) and for the same reason. It is the standing infinite-dimensional example, where Ch 16 §02's equivalence theorem fails |
| `B_{\norm{\cdot}}` | the **closed unit ball** \( \{\v : \norm{\v} \le 1\} \) of a norm (Ch 16 §01). In \( F^n \), `B_1`, `B_2`, `B_\infty` are the balls of the three p-norms; the integer subscript names the norm, not a dimension |
| `\norm{A}` | operator norm induced by the named vector norm |
| `\norm{\A}_1`, `\norm{\A}_{\infty}` | the operator norms induced by the vector 1- and ∞-norms (Ch 16 §03): the largest column sum and the largest row sum. Distinct from the entrywise maximum, which is not even submultiplicative, and from \( \norm{f}_{\infty} \), the sup norm on a function space |
| `\kappa(A)` | condition number |
| `\conv S` | the **convex hull** of S, the set of all convex combinations of points of S (Ch 18 §01, `def-convex-hull`, `thm-convex-hull-combinations`) |
| `\operatorname{aff} S` | the **affine hull**, the set of affine combinations; a coset \( \x_0 + W_S \) (Ch 18 §01, `def-affine-hull`, `prp-affine-hull-coset`). No macro |
| `[\x, \y]` | the **segment** \( \{(1-t)\x + t\y : 0 \le t \le 1\} \) (Ch 18 §01). Always with bold vector arguments; not the commutator \( [A, B] \) |
| `\Delta_n` | the **standard simplex** \( \{t \in \nR^n : t_i \ge 0,\ \sum t_i = 1\} = \conv\{\e_1, \dots, \e_n\} \): n weights (Ch 18 §01, `def-standard-simplex`). Mixed strategies of a game live here (Ch 18 §07) |
| `\interior S`, `\closure S` | interior and closure of a subset of a finite-dimensional real space (Ch 18 §03, `def-interior-point`); closed and open are defined sequentially in `def-closed-set` (§01) |
| `P_C(\x)`, `d(\x, C)` | the **nearest point** of a non-empty closed convex set C to x, and the distance (Ch 18 §03, `thm-nearest-point`). For a subspace this is the orthogonal projection of Ch 11 |
| `p_K`, `h_K`, `K^{\circ}` | the **gauge**, **support function** (value \( +\infty \) allowed) and **polar set** of K (Ch 18 §04) |
| `\norm{\cdot}_{*}`, `\norm{\cdot}_{**}` | the **dual norm** \( \norm{\y}_* = \max_{\norm{\x}\le 1}\inner{\x}{\y} \) and the bidual, which is the norm itself (Ch 18 §04, `def-dual-norm`, `thm-dual-dual-norm`). Dual of \( \norm{\cdot}_p \) is \( \norm{\cdot}_q \) |
| `K^{*}` | the **dual cone** \( \{\y : \inner{\x}{\y} \ge 0 \ \forall \x \in K\} \) of a subset K, inside V itself (Ch 18 §05, `def-dual-cone`). Not the dual space \( V^* \); for a subspace it equals \( U^\perp \) and is not written this way |
| `\operatorname{cone}(\a_1, \dots, \a_m)`, `\operatorname{cone}(\A)` | the **finitely generated cone** (Ch 18 §05, `def-finitely-generated-cone`); \( \operatorname{cone}() = \{\0\} \). No macro |
| `\x \ge \0`, `\u \le \v`, `\nR^m_{\ge 0}` | **entrywise** order on real vectors, and the non-negative orthant (Ch 18 §05), extended to matrices in Ch 19: \( \A \ge 0 \), \( \A > 0 \) (every entry positive), \( \A \ge \B \). Unrelated to the Loewner \( \succeq \): a positive matrix need not be positive definite, nor conversely |
| `\lvert\M\rvert` (Ch 19) | the **entrywise** absolute value \( (\lvert m_{ij}\rvert) \). **Local override** of the Ch 13 row \( \lvert A\rvert = (A^*A)^{1/2} \), which does not appear in Ch 19 |
| `G(\A)` | the **directed graph** of a square matrix: vertices \( 1, \dots, n \), an edge \( j \to i \) whenever \( a_{ij} \ne 0 \) (column index to row index, matching \( \x_{k+1} = \A\x_k \)); walks, paths, strong connectivity (Ch 19 §02). No macro |
| Perron root, `\v`, `\w` | for \( \A > 0 \) or irreducible \( \A \ge 0 \): the Perron root \( \rho(\A) \), the right Perron vector \( \v > \0 \) with \( \1\tp\v = 1 \), and the left Perron vector \( \w > \0 \) with \( \w\tp\A = \rho\w\tp \) and **\( \w\tp\v = 1 \)** (Ch 19 §01 `def-perron-vector`, §03 `def-perron-root-and-vectors`) |
| `\underline{r}_{\A}(\x)`, `\overline{r}_{\A}(\x)` | the lower and upper **Collatz–Wielandt functions** (Ch 19 §04). The bars are **not** conjugation (`\conj`) or closure (`\closure`); R_A is the Rayleigh quotient, so these avoid it |
| \( h \), \( \omega = e^{2\pi i/h} \) | the **period** of an irreducible \( \A \ge 0 \) (gcd of closed-walk lengths), equal to the number of peripheral eigenvalues (Ch 19 §05, `def-period`, `thm-peripheral-spectrum`) |
| `\W_n` (Ch 19 §05) | the Wielandt matrix, primitive with exponent exactly \( (n-1)^2+1 \). Bold W, not the subspace W |
| `\Q`, `\R`, `\N` (Ch 19 §06) | an absorbing chain's transient block, absorbing block, and fundamental matrix \( \N = (\I - \Q)^{-1} \); absorption probabilities \( \R\N \) |
| `W_n` (Ch 19 §07) | the real \( n\times n \) matrices with all row and column sums zero; \( \dim W_n = (n-1)^2 \), and \( \Omega_n \) lies in the coset \( \tfrac1n\J + W_n \) |
| `\G`, `\H`, \( \alpha \) (Ch 19 §08) | the Google matrix \( \alpha\P + \tfrac{1-\alpha}{n}\J \) and the raw hyperlink matrix, **local overrides** of the Gram matrix and the Hessian; \( \alpha \in (0,1) \) the damping factor |
| `\K_n` | the \( n\times n \) second-difference matrix (2 on the diagonal, \( -1 \) beside it), a non-singular M-matrix (Ch 19 §09; Ch 7 exercise) |
| `v(\A)` | the **value** of the matrix game with payoff matrix A (Ch 18 §07, `def-value-of-game`) |
| `\operatorname{ext} C`, `W_C`, `\dim C` | the **extreme points** of C; the direction space and dimension of a non-empty convex set, \( \dim C = \dim \operatorname{aff} C \) (Ch 18 §01, §08) |
| `\cD_n`, `\Omega_n` | the real **density matrices** \( \{X = X\tp \succeq 0, \tr X = 1\} \) and the **doubly stochastic** matrices (Ch 18 §08, `def-density-matrix`, `def-doubly-stochastic`). Plain \( \Omega \), not the bold symplectic \( \vOmega_{2m} \) of Ch 14 |
| `I(\x)`, `\A_I` | the active set of a point of \( \{\A\x \le \b\} \) and the matrix of its active rows (Ch 18 §09) |
| `\operatorname{epi} f` | the **epigraph** \( \{(\x, s) : s \ge f(\x)\} \) (Ch 18 §10) |
| `\log`, `t^r` | the natural logarithm, built as the inverse of exp in Ch 18 §11 (`lem-exp-log`), and real powers \( t^r = e^{r\log t} \) for \( t > 0 \), \( 0^r = 0 \) for \( r > 0 \). This gives Ch 16 §01's \( \norm{\cdot}_p \) its meaning |
| `s_k(\A)` | \( \lambda_1(\A) + \dots + \lambda_k(\A) \), the Ky Fan partial sum (Ch 17 §06, reused in Ch 18 §10) |
| `\vol` | volume: of a parallelepiped, \|det\| (Ch 7); extended in Ch 13 §03 to the k-dimensional volume of a list of any length in any inner product space, by the base-times-height recursion of `def-k-volume`. The two agree wherever both apply, and Ch 13 §03 proves it |
| `\x \prec \y`, `\x \prec_w \y`, `\x^{\downarrow}` | **majorization** and **weak (sub)majorization** of real vectors, written with bold vectors (Ch 17 §08, `def-majorization`). \( \x^{\downarrow} \) is \( \x \) sorted decreasingly. \( \x \prec_w \y \): every top-\( k \) partial sum of \( \x^{\downarrow} \) is at most that of \( \y^{\downarrow} \); \( \x \prec \y \) adds equal totals. **It is a preorder on \( \nR^n \), not a partial order** — (1,0) ≺ (0,1) ≺ (1,0) |
| `\d(\A)` | the **diagonal vector** \( (a_{11}, \dots, a_{nn}) \in \nR^n \) of a Hermitian \( \A \), in its given order (Ch 17 §08). Bold because it is a vector; distinct from `\diag(d_1,\dots,d_n)`, which **builds a matrix** |
| `\vlambda(\A)` | the **eigenvalue vector** \( (\lambda_1(\A), \dots, \lambda_n(\A)) \) of a Hermitian \( \A \), decreasing (Ch 17 §§07–08) |
| `\cW = (W_1, \dots, W_k)` | a **flag** of subspaces \( W_1 \subset \dots \subset W_k \) of type \( (i_1 < \dots < i_k) \), \( \dim W_j = i_j \), and a list **adapted** to it (Ch 17 §07, `def-flag-adapted-list`) |
| `x^{\downarrow}` | decreasing rearrangement |
| `r_i(\A)`, `D_i(\A)` | the i-th **Gershgorin radius** \( \sum_{j \ne i}\lvert a_{ij}\rvert \) and the closed **Gershgorin disc** \( \{z : \lvert z - a_{ii}\rvert \le r_i(\A)\} \) (Ch 20 §01). Plain r, since `R_{\A}` is the Rayleigh quotient; plain D, since `\D` is a diagonal matrix. Column radii are \( r_i(\A\tp) \) |
| `O_{ij}(\A)` | the **Brauer oval of Cassini** \( \{z : \lvert z - a_{ii}\rvert\lvert z - a_{jj}\rvert \le r_i r_j\} \) (Ch 20 §02) |
| `W(\A)` | the **numerical range** \( \{\x^{*}\A\x : \norm{\x}_2 = 1\} \) (Ch 20 §02), always written with its argument, so it never meets the subspace W |
| `\H`, `\K` (Ch 20 §02) | the **Hermitian and skew parts** of \( \A \): \( \H = (\A + \A^{*})/2 \) and \( \K = (\A - \A^{*})/(2i) \), both Hermitian, with \( \A = \H + i\K \) (`lem-hermitian-parts`, used again in `thm-bendixson`). **Local overrides** of Ch 14 §06's Hessian \( \H_f(\a) \) and Ch 19 §08's hyperlink matrix, neither of which appears in Ch 20. The bare \( \K \) never means the second-difference matrix: that one always carries its subscript, \( \K_n \), as it does in Ch 20 §01 |
| `\E` | the **perturbation**, in \( \A + \E \) (Ch 16, Ch 17, Ch 20). Ch 20 writes \( \widetilde{\A} \) for a perturbed matrix only where it is not naturally \( \A + \E \) |
| `\operatorname{sep}_F(\A,\B)` | the **separation** \( \min_{\norm{\X}_F = 1}\norm{\A\X - \X\B}_F \), the smallest singular value of the Kronecker-sum matrix (Ch 20 §07, `def-sep`). The subscript records the norm; the equation's data matrix stays \( \C \), as in Ch 12 §10 |
| \( \theta_1 \le \dots \le \theta_k \), `\Theta(U,W)` | the **principal angles** between two subspaces, with \( \cos\theta_i \) the singular values of \( \Q_W^{*}\Q_U \), and the diagonal matrix of them (Ch 20 §08, `def-principal-angles`). Plain \( \Theta \), an exception to the bold-matrix rule, because it appears only inside \( \sin\Theta \) and \( \cos\Theta \); unrelated to Ch 15's natural isomorphism. Angles lie in \( [0, \pi/2] \): subspaces have no orientation, unlike Ch 11's `def-angle` |
| `\kappa_{\A}(\lambda)` | the **condition number of a simple eigenvalue**, \( \norm{\x}_2\norm{\y}_2/\lvert\y^{*}\x\rvert \) for right and left eigenvectors x, y (Ch 20 §11). Subscripted by the matrix so it never meets \( \kappa(\A) = \norm{\A}\norm{\A^{-1}} \) of Ch 16 §08. Ch 20 §11 writes left eigenvectors as \( \y^{*}\A = \lambda\y^{*} \), and says so where Ch 9 §10's transpose convention differs |
| `\operatorname{dis}(\u, \v)`, `\operatorname{supp}(\z)` | the number of indices at which two real vectors **disagree**, and the **support** \( \{i : z_i \ne 0\} \) of a vector (Ch 21 §01, in the proof of `thm-hardy-littlewood-polya` and in its exercise C3). Both spelled with `\operatorname`, like `\operatorname{rad}`; no macro |
| `\uinorm{\A}` | a **unitarily invariant norm**: \( \uinorm{\U\A\V} = \uinorm{\A} \) for all unitary U, V (Ch 21 §04, `def-unitarily-invariant-norm`). Triple bars, so it never reads as \( \norm{\cdot} \); subscripted \( \uinorm{\A}_{(k)} \) for the **Ky Fan k-norm** \( \sigma_1 + \dots + \sigma_k \) (Ch 21 §04, `def-ky-fan-norm`) |
| \( \Phi \), \( \Phi^{*} \) | a **symmetric gauge function** on \( \nR^n \) — a norm invariant under permuting the coordinates and changing their signs — and its dual (Ch 21 §03, `def-symmetric-gauge`, `def-dual-gauge`). **Not** Ch 18 §04's gauge \( p_K \) of a convex set, which is a different object with the same word; Ch 21 §03 says so once. Ch 21 §04 pairs the two: \( \uinorm{\A} = \Phi(\sigma(\A)) \) |
| `\diag_{m,n}(\x)` | the \( m \times n \) matrix carrying \( \x \) on its main diagonal and zeros elsewhere (Ch 21 §04); it is `\diag` when \( m = n \) |
| \( L_f(t_1, \dots, t_n) \) | the **Loewner matrix** of divided differences \( f[t_i, t_j] \) of a real function (Ch 21 §09, `def-loewner-matrix`). Plain italic L, an announced exception to the bold-matrix rule, like \( \Theta \) for the principal angles: it is indexed by a function, not by the data of a linear map |
| \( \A \# \B \) | the **geometric mean** \( \A^{1/2}(\A^{-1/2}\B\A^{-1/2})^{1/2}\A^{1/2} \) of two positive definite matrices (Ch 21 §11, `def-geometric-mean`). Written with the plain symbol \( \# \), no macro; it is symmetric in its arguments, which the section proves
| `u`, `\fl`, `\cR`, \( \gamma_k \) | the **unit roundoff**, the rounding map, the set of representable numbers, and \( \gamma_k = ku/(1-ku) \), the accumulated-rounding constant (Ch 24 §01, `def-floating-point-model`, `lem-gamma-bound`). Plain italic u; it never meets the bold vector \( \u \), which Ch 24 §09 uses in a different section. A single rounding is \( \delta \), with \( \lvert\delta\rvert \le u \) |
| \( \widehat{\x} \), \( \Delta\A \) | a **computed** object, and a data perturbation **produced by an algorithm** (Ch 24). Chapters 16, 17 and 20 write \( \E \) for a perturbation whose size is given; \( \Delta \) is reserved for one an algorithm made |
| flop, \( g_n \) | one arithmetic operation, and the **growth factor** of elimination (Ch 24 §02, `def-growth-factor`) |
| `\cK_k(\A,\b)` | the **Krylov space** \( \Span(\b, \A\b, \dots, \A^{k-1}\b) \) (Ch 24 §06, `def-krylov-subspace`); \( \theta_i^{(k)} \) are the Ritz values |
| \( \inner{\x}{\y}_{\A} \), \( \norm{\x}_{\A} \) | the **energy** inner product and norm of a positive definite \( \A \) (Ch 24 §07, `def-energy-norm`); \( T_k \) are the Chebyshev polynomials, as in Ch 11 §10 |
| \( \X \), \( \X_c \), \( \S \) | the **data matrix**, its centered form, and the **sample covariance** \( \tfrac1N\X_c\X_c\tp \) (Ch 24 §10). \( \S \) is a **local override**: Ch 13 §04 and Ch 24 §09 use it for a congruence, Ch 24 §02 for a Schur complement, Ch 24 §08 for a similarity curve. Each section says which it means |
| \( \L \) (Ch 24) | the **graph Laplacian** \( \D - \A = \N\N\tp \) in §11, following Ch 3 §07, with \( \L_0 \) the reduced Laplacian and \( \mu_2(\L) \) the Fiedler value — but the **Lax matrix** in §08, and the lower triangular factor in §02. §08 and §11 each declare their use at the head of the section |
| \( \M \), \( \K \) (Ch 24 §09) | the **mass** and **stiffness** matrices, and \( \omega_j \) the natural frequencies. \( \K \) is a local override of Ch 19 §09's second-difference \( \K_n \), which always carries its subscript, and of Ch 20 §02's skew part; §09 says so |
| \( \W_n \) (Ch 24 §12) | the **unnormalized transform matrix** \( \sqrt n\,\F_n \), with \( \P_n \) the even–odd permutation, \( \D_m \) the twiddle matrix and \( \B_n \) the butterfly. A local override: Ch 19 §05's \( \W_n \) is the Wielandt matrix, and Ch 24 §08 writes \( \W_k \) for an accumulated orthogonal factor |
| \( \omega \) (Ch 24) | three meanings, each local and each declared: an angular frequency (§09), a primitive root of unity \( \omega_n \) (§12), and the **exponent of matrix multiplication** (§13, `def-matrix-multiplication-exponent`) |

## Affine and projective geometry (Ch 22)

| Type | Meaning |
|---|---|
| `\cA, \cB, \cC` | **affine spaces** (Ch 22 §§01, 02, 05). Plain calligraphic, like a space, never bold. Ch 15 §08 uses \( \cA \) once inside a proof for a space of alternating forms; the two never meet |
| `P, Q, R`, `\overrightarrow{PQ}`, `P + \v` | **points of an affine space are not bold**, unlike every vector in the book; \( \overrightarrow{PQ} \in V \) is the vector from \( P \) to \( Q \), and \( P + \v \) is the point \( P \) translated by \( \v \) (Ch 22 §01, `def-affine-space`) |
| `\nA^n(F)`, `\nA^n` | **affine \( n \)-space**: the set \( F^n \) with its origin forgotten (Ch 22 §01). The bare \( \nA^n \) is over \( \nR \) |
| `\theta_O` | the **choice-of-origin bijection** \( \cA \to V \), \( P \mapsto \overrightarrow{OP} \) (Ch 22 §01, `prp-choice-of-origin`). Plain \( \theta \): it is a map, not a matrix |
| `\vec f` | the **linear part** of an affine map (Ch 22 §§01–02, `thm-affine-map-is-linear-plus-translation`). Ch 22 §04 writes the bare \( \Q \in \Orth(n) \) for the linear part of a Euclidean motion and says at `thm-motion-is-affine` that it is \( \vec f \) |
| `\operatorname{Aff}(\cA)`, `\tau_{\v}` | the **affine group** of \( \cA \), and **translation by \( \v \)**, the kernel of \( \operatorname{Aff}(\cA) \to \GL(V) \) (Ch 22 §01, `thm-affine-group`). Ch 22 §04 writes the same map as \( t_{\b} \), the kernel of \( \operatorname{E}(n) \to \Orth(n) \); the two sections use the two letters and mean one object |
| `\widehat f` | the **block matrix of an affine map**, \( \begin{psmallmatrix}\A&\b\\\0\tp&1\end{psmallmatrix} \), acting on \( \binom{\x}{1} \) (Ch 22 §§01, 05, `prp-affine-map-block-matrix`): the homogenizing coordinate sits **last**. Ch 22 §§06–10 put it **first**, as \( x_0 \), and the two matrices are conjugate by the cyclic permutation that moves the last coordinate to the front; §§01 and 07 each say so where they meet |
| `\vec A`, `A \vee B`, `A \parallel B` | the **direction space** of a flat, a subspace of \( V \); the **join**, the smallest flat containing both; and **parallelism** of flats, equality of direction spaces (Ch 22 §02, `def-flat`, `def-affine-join`, `def-parallel-flats`) |
| `P_J` | the face of a polyhedron cut out by making the rows \( i \in J \) of \( \A\x \le \b \) **tight** (Ch 22 §03, `prp-face-is-polyhedron`). Ch 18 §09's active set \( I(\x) \) and active-row matrix \( \A_I \), and Ch 18 §01's \( \conv \), \( \operatorname{aff} \), \( [\v,\w] \), \( \Delta_n \), \( B_1 \), \( B_\infty \), \( \operatorname{ext}P \), are used unchanged |
| `\operatorname{E}(n)`, `\operatorname{Trans}(n)`, `t_{\b}`, `\operatorname{Fix}(f)` | the **Euclidean group** of \( \nR^n \), its translation subgroup, **translation by \( \b \)**, and the **fixed set** of a motion (Ch 22 §04). Spelled with `\operatorname`, like `\operatorname{rad}`; \( \lambda \) is the linear-part homomorphism \( \operatorname{E}(n) \to \Orth(n) \), the one place \( \lambda \) is not a scalar |
| `\R_{\theta}`, `\M_{\theta}`, `\Q`, `\Q_L`, `s_L`, `\Q_{\Pi}`, `s_{\Pi}`, `\H_{\w}` | Ch 11's plane **rotation** and **reflection** matrices, kept; the orthogonal linear part \( \Q \) of a motion; the linear reflection in a line \( L \) or a plane \( \Pi \) through \( \0 \) and the affine reflections \( s_L \), \( s_{\Pi} \) they define; and Ch 11 §08's **Householder reflection** (Ch 22 §04) |
| `\Pi` | a **plane** in Ch 22 §§04, 08, 09 — but in Ch 22 §07 the **quotient homomorphism** \( \GL(V) \to \operatorname{PGL}(V) \). Each section uses one of the two and no section uses both |
| `\widetilde\A = \begin{psmallmatrix}\A&\b\\\b\tp&c\end{psmallmatrix}`, `\tilde\x` | the **big matrix** of a quadric polynomial \( \x\tp\A\x + 2\b\tp\x + c \) and the big vector \( \binom{\x}{1} \), with \( Q(\x) = \tilde\x\tp\widetilde\A\tilde\x \) (Ch 22 §05, `def-quadric`). The inertia \( \operatorname{In}\A \) is Ch 17 §10's, unchanged. The zero set is written out, not lettered |
| `\nP(V)`, `\nP^n(F)`, `[\x] = [x_0 : \dots : x_n]` | the **projective space** of \( V \), of dimension \( \dim V - 1 \); \( \nP^n(F) = \nP(F^{n+1}) \); and **homogeneous coordinates** (Ch 22 §§06–10, `def-projective-space`, `def-homogeneous-coordinates`). \( \dim\emptyset = -1 \) is used, not merely tolerated. Coordinates run from \( 0 \): see the index-origin row above |
| `U_0`, `U_j`, `H_{\infty}`, `\iota` | the **standard affine chart** \( \{x_0 \ne 0\} \) of \( \nP^n(F) \), the other charts \( \{x_j \ne 0\} \), the **hyperplane at infinity** \( \{x_0 = 0\} \), and the chart bijection \( F^n \to U_0 \), \( \a \mapsto [1 : a_1 : \dots : a_n] \) (Ch 22 §§06–07, `thm-affine-chart`) |
| `S \vee T`, `S \cap T` | the **join** and **meet** of projective subspaces, \( \nP(U + W) \) and \( \nP(U \cap W) \) (Ch 22 §06, `prp-join-and-meet`), matching the affine \( A \vee B \) of §02. Ch 22 §09 writes \( AB \) for the join of two points, the line through them |
| `[T]`, `[\A]` | the **projectivity** induced by an isomorphism \( T \) or an invertible matrix \( \A \), \( [\x] \mapsto [T\x] \) (Ch 22 §§07–10, `def-projective-transformation`). The bracket is the same one that turns a vector into a point |
| `\operatorname{PGL}(V)`, `\operatorname{PGL}_{n+1}(F)` | the **projective linear group** (Ch 22 §07, `thm-pgl`), spelled with `\operatorname` throughout: there is no `\PGL` macro, deliberately, since \( \GL \) has one and the two would look alike. \( F^{\times} = F \setminus \{0\} \) is the multiplicative group |
| `(A, B; C, D)` | the **cross-ratio** of four points of a projective line, itself a **point of \( \nP^1(F) \)** and not a scalar (Ch 22 §07, `def-cross-ratio`); in an affine chart it is the familiar number, and \( [1:0] \) is the value the number cannot take |
| `S^{0}`, `S^{\perp}` | the **projective annihilator** of a projective subspace, Ch 5's \( U^{0} \) read in \( \nP(V^{*}) \) (Ch 22 §08, `thm-duality-correspondence`), and the polarity attached to a non-degenerate form (Ch 22 §08, exercise C2). Distinct from Ch 18 §04's polar set \( K^{\circ} \), which is a convex set in \( V \) itself |
| `\o` | a **chosen representative vector** of a projective point, the one held fixed while the others are scaled to it (Ch 22 §§09–10, `lem-collinear-representatives`). Bold, like every vector |
| `Z(q)`, `P^{\beta}` | the **zero set** of a quadratic form, \( \{[\x] : q(\x) = 0\} \) (Ch 22 §10, `def-projective-quadric`), and the **polar** of a point with respect to a conic with polar form \( \beta \) (`def-pole-and-polar`) |
| `p_{ij}`, `[L]`, `\e_{ij}`, `\e_{0123}`, `\cK`, `\G` | the **Plücker coordinates** of a line \( L \subseteq \nP^3(F) \), the point \( [L] \in \nP^5(F) \) they form, Ch 15's basis \( \e_S \) of \( \Lambda^2F^4 \) and \( \Lambda^4F^4 \) with 0-based indices, the **Klein quadric**, and the alternating Gram matrix of the form \( B(\v,\v')\e_{0123} = \v\wedge\v'\wedge\omega \) (Ch 22 §10). \( \cK \) is a **local override** of Ch 24 §06's Krylov space \( \cK_k(\A,\b) \), which always carries its subscript and arguments; \( \G \) is the book's Gram matrix, here for an alternating form |

## Algebras and representations (Ch 23)

| Type | Meaning |
|---|---|
| `\End(V)` | \( \cL(V) \) regarded as an **algebra** under composition (Ch 23 §01, and used in §§05–07 where the algebra structure is the point). The same object as \( \cL(V) \); the letter changes, not the space |
| `\cT_n` | the **upper triangular** matrices in \( M_n(F) \) (Ch 23 §01, `exm-first-subalgebras` (b); used in §02). \( \cN \) is its ideal of strictly upper triangular matrices (Ch 23 §02, reused §03) |
| `F\langle S\rangle` | the **subalgebra generated** by a set \( S \) (Ch 23 §01, `def-generated-subalgebra`): the span of the words in \( S \), with the empty word \( 1_A \). Distinct from Ch 6's \( \langle p\rangle \), the **ideal** generated by a polynomial, and from \( \langle g\rangle \), the cyclic subgroup generated by a group element (Ch 23 §08, `lem-element-has-finite-order`) |
| `F[T]`, `F[\A]` | the algebra of **polynomials in one operator or matrix**, of dimension \( \deg m_T \) (Ch 23 §01, `prp-polynomial-algebra-dimension`). The bracket is Ch 6's evaluation bracket, not Ch 23's group-algebra bracket |
| `F[G]`, `\delta_g` | the **group algebra** of a finite group and its basis of point masses, \( \delta_g\delta_h = \delta_{gh} \) (Ch 23 §01, `def-group-algebra`). The Kronecker delta always carries two **numerical** subscripts, \( \delta_{jk} \), and no group element is written as a pair of numbers (stated at Ch 23 §09's head) |
| `L_a` | **left multiplication** by \( a \), \( x \mapsto ax \) (Ch 23 §01, `thm-cayley-for-algebras`); the regular representation is \( a \mapsto L_a \) |
| `S'`, `S''`, `Z(A)` | the **commutant** of a set, the **double commutant** \( (S')' \), and the **center** \( Z(A) = A' \cap A \) (Ch 23 §01, `def-commutant`, `prp-center-of-matrix-algebra`). The prime asks nothing of \( S \): not that it be a subspace, not that its members commute |
| `C_j`, `L_W`, `R_U` | the \( j \)-th **column ideal** of \( M_n(F) \), and the left and right ideals attached to a subspace by column space and row space (Ch 23 §02, `prp-left-ideals-of-matrix-algebra`) |
| `A/\cI`, `\pi` | the **quotient algebra** by a two-sided ideal and the quotient homomorphism (Ch 23 §02, `def-quotient-algebra`). \( \cI \) is Ch 15 §10's letter for a two-sided ideal, kept. The letter \( \pi \) is re-used for the slot projections of §§05–06 and for a representation on \( \cL(V,W) \) in §08; each use is local and declared |
| `\operatorname{rad} A` | the **radical of an algebra**: the elements killed by every irreducible representation (Ch 23 §03, `def-algebra-radical`). Spelled with `\operatorname`, like Ch 14 §01's \( \operatorname{rad}(\beta) \), the radical of a bilinear form; the argument tells them apart |
| \( A \)-space, `a\v` | a space carrying an **action** of \( A \), that is, an algebra homomorphism \( A \to \End(V) \), with \( \rho(a)\v \) written \( a\v \) and \( 1_A\v = \v \) (Ch 23 §03, `def-representation-of-an-algebra`). An **irreducible**, equivalently **simple**, \( A \)-space is `def-simple-module`; the word is Ch 6's for a polynomial and Ch 19 §02's for a non-negative matrix as well |
| `\End_A(V)`, \( A \)-map | the **equivariant maps**, \( f(a\v) = af(\v) \) (Ch 23 §04, `def-intertwining-map`). The subscript is never dropped. Ch 23 §06 writes \( \operatorname{Hom}_A(V,W) \) for the same maps between two spaces, and §08 writes \( \cL_G(V,W) \) for the group version; each says where it does so |
| `A(\cF)` | the **subalgebra generated by a family** \( \cF \subseteq \cL(V) \) (Ch 23 §04, `lem-family-and-generated-algebra`): \( F\langle\cF\rangle \) with the family notation of Ch 9 |
| `\R`, `\Q` | the **rotation** of \( \nR^2 \) through \( 2\pi/n \) and the **quarter turn** \( \begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix} \) (Ch 23 §§04–06). Ch 11 writes the plane rotation as \( \R_\theta \), always with its angle; Ch 23 drops the subscript because one angle is in play at a time. Ch 22 §04's \( \Q \) is a general orthogonal linear part, a different use of the letter in a chapter Ch 23 never cites. The quarter turn is this chapter's standing witness against algebraic closure |
| `\v\varphi` | the **rank-one operator** \( \x \mapsto \varphi(\x)\v \), a bold vector times a functional (Ch 23 §05, `thm-burnside`) |
| `\tilde s`, `V^n` | the operator acting **slotwise** on \( n \) copies of \( V \), and that copied space (Ch 23 §05, `thm-double-commutant`) |
| `e_i` | the **orthogonal idempotents** of a product of algebras, italic and never bold, so that the basis vector \( \e_i \) is a different symbol (Ch 23 §06, `def-product-of-algebras`; the pulled-back idempotents of a group algebra are \( \varepsilon_\chi \) in §09) |
| `\rho`, `\chi_\rho`, `\operatorname{Cl}(G)`, `\inner{f}{f'}`, `V^G` | a **representation**, its **character** \( \chi_\rho(g) = \tr\rho(g) \), the **class functions** on \( G \), their averaged inner product \( \lvert G\rvert^{-1}\sum_g f(g)\conj{f'(g)} \), and the **fixed space** (Ch 23 §§07–08). \( \operatorname{Cl} \) is spelled with `\operatorname`, like \( \operatorname{rad} \) |
| `\widehat G`, `\widehat f`, `\ev_g` | the **dual group** of a finite abelian \( G \), the **Fourier transform** \( \widehat f(\chi) = \sum_g f(g)\chi(g) \), and **evaluation at \( g \)** (Ch 23 §09). Ch 22 §01's \( \widehat f \) is the block matrix of an affine map; the two chapters never meet |
| `\U` | the **character matrix** \( (\U)_{mj} = \chi_j(g_m)/\sqrt n \), characters in columns and indices from \( 0 \) (Ch 23 §09, `def-character-matrix`); §08's rescaled character table, inside the proof of `cor-column-orthogonality`, is its transpose. A **local override** of \( \U \) for a generic upper triangular matrix in Ch 23 §§01–02 and earlier chapters |
| `\Phi`, `\Psi`, `\varepsilon_\chi` | the isomorphism \( \nC[G] \to \nC^{\widehat G} \), the isomorphism of \( \nC[\nZ/n\nZ] \) onto the circulants, and the **idempotent** attached to a character (Ch 23 §09) |
| `\C` | the bare \( \C \) is Ch 12 §09's **circulant** in Ch 23 §§09–10; Ch 10's companion matrix, used once in Ch 23 §03, always carries its polynomial, as \( \C(p) \) |

## Label naming

Labels are global and must be unique across the book.

- **Format:** `<env>-<topic words>`, e.g. `def-linear-independence`, `thm-rank-nullity`, `lem-exchange`, `exm-rotation-no-real-eigenvalues`.
- **Exercises:** `exr-<section-slug>-<group><n>`, e.g. `exr-span-b2`.
- **Before creating a label**, check it is free: `grep -rn "#thm-rank-nullity" src`.
- **Existing labels** of results that survive a rewrite keep their exact label, so links stay stable.
