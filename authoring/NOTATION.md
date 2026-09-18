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

**Bold is for matrices and vectors, never for maps or spaces.** A matrix is bold (`\A`), a vector is bold lowercase (`\v`), an operator or linear map is plain italic (T, S), and a vector space is plain italic (V, U, W). A letter that names a matrix is bold everywhere it appears, including in `[T]_{\sB}`-style expressions where the result is a matrix but the letter T is a map.

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
| `T'` | dual map (transpose of T) W* → V*. The star is reserved for adjoints |
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
| `J_k(\lambda)` | k×k Jordan block, λ on the diagonal, 1 on the **super**diagonal |
| `\Lambda(\lambda)` | rotation-scaling block of a conjugate pair: the 2×2 real matrix with rows (a, −b), (b, a), for λ = a + bi (Ch 9) |
| `C_k(\lambda)` | 2k×2k **real** Jordan block for the pair {λ, λ̄}, λ ∉ ℝ: Λ(λ) on the diagonal, I₂ on the **super**diagonal, in 2×2 blocks (Ch 9). Not a companion matrix |
| `C(p)` | companion matrix of a monic p: 1 just below the diagonal, last column (−a₀, …, −a_{n−1}) |
| `Z(\v; T)` | cyclic subspace generated by v: the span of v, Tv, T²v, … (Ch 9) |
| `m_{T,\v}` | the T-annihilator of v: the monic generator of { p ∈ F[x] : p(T)v = 0 }. For a matrix, `m_{A,\v}` |
| `d_1 \mid d_2 \mid \dots \mid d_r` | invariant factors of T, with **d_r = m_T** and d₁⋯d_r = p_T (Ch 9). Their prime-power factors are the elementary divisors |
| `\rho(A)` | spectral radius |
| `e^{A}` | matrix exponential |

## Inner products and spectral theory

| Type | Meaning |
|---|---|
| `\inner{\u}{\v}` | inner product, **linear in the first slot**, conjugate-linear in the second |
| `\norm{\v}` | norm (induced unless stated) |
| `U^{\perp}` | orthogonal complement |
| `P_U` | orthogonal projection onto U |
| `T^{*}` | adjoint |
| `\Orth(n), \SO(n), \Unit(n)` | orthogonal, special orthogonal, unitary groups |
| `A \succeq 0`, `A \succ 0` | positive semidefinite / definite (Hermitian implied) |
| `A \succeq B` | Loewner order |
| `\lambda_1(A) \ge \dots \ge \lambda_n(A)` | eigenvalues of a Hermitian A, **decreasing** |
| `\sigma_1(A) \ge \dots \ge \sigma_{\min(m,n)}(A) \ge 0` | singular values, decreasing |
| `A^{+}` | Moore–Penrose pseudoinverse |
| `A^{1/2}` | positive square root |
| `\lvert A \rvert = (A^{*}A)^{1/2}` | absolute value |

## Forms, tensors, analysis

| Type | Meaning |
|---|---|
| `\beta \colon V \times V \to F` | bilinear form. `q(\v) = \beta(\v, \v)` is a quadratic form |
| `\mtx{\beta}{\sB}{}` | Gram matrix of a form: `[\beta]_{\sB}` |
| `V \otimes W`, `\v \otimes \w` | tensor product |
| `\Lambda^{k} V`, `\v_1 \wedge \dots \wedge \v_k` | exterior power |
| `\Sym^{k} V` | symmetric power |
| `A \otimes B` | Kronecker product of matrices |
| `\vecop X` | vectorization of a matrix: its columns stacked into one column, rendered vec X (Ch 7) |
| `A \circ B` | Hadamard (entrywise) product |
| `[A, B] = AB - BA` | commutator |
| `\norm{\x}_p` | p-norm. `\norm{A}_F` Frobenius, `\norm{A}_2` spectral/operator 2-norm |
| `\norm{A}` | operator norm induced by the named vector norm |
| `\kappa(A)` | condition number |
| `\conv(S)` | convex hull |
| `\vol` | volume of a parallelepiped, \|det\| (Ch 6) |
| `x \prec y`, `x \prec_w y` | majorization, weak majorization |
| `x^{\downarrow}` | decreasing rearrangement |

## Label naming

Labels are global and must be unique across the book.

- **Format:** `<env>-<topic words>`, e.g. `def-linear-independence`, `thm-rank-nullity`, `lem-exchange`, `exm-rotation-no-real-eigenvalues`.
- **Exercises:** `exr-<section-slug>-<group><n>`, e.g. `exr-span-b2`.
- **Before creating a label**, check it is free: `grep -rn "#thm-rank-nullity" src`.
- **Existing labels** of results that survive a rewrite keep their exact label, so links stay stable.
