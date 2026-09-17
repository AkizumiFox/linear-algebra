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

## Vectors and spaces

| Type | Meaning |
|---|---|
| `V, W, U` | vector spaces over F (U is usually a subspace) |
| `\v, \u, \w, \x, \y` | vectors, **bold** lowercase (`\mathbf`) |
| `\0` | zero vector (bold). The scalar zero is `0` |
| `a, b, c, \lambda, \mu` | scalars, plain |
| `F^n` | column vectors. In running text write \( (x_1, \dots, x_n) \) and treat it as a column |
| `\e_1, \dots, \e_n` | standard basis of F^n |
| `F[x]`, `F[x]_{\le n}` | polynomials; polynomials of degree at most n |
| `M_{m \times n}(F)`, `M_n(F)` | matrices |
| `\Span(S)` | span. The span of the empty set is {0} |
| `\dim V` | dimension (over F; write `\dim_F V` when the field matters) |
| `U + W`, `U \oplus W` | sum; direct sum (internal) |
| `V / U`, `\v + U` | quotient space, coset |
| `\sB = (\v_1, \dots, \v_n)` | an **ordered** basis, in parentheses. Calligraphic `\sB, \sC, \sE` |
| `\coord{\v}{\sB}` | coordinate vector, rendered [v]_𝓑 |

## Linear maps and matrices

| Type | Meaning |
|---|---|
| `T, S \colon V \to W` | linear maps (always T, S, R; never f for a linear map) |
| `ST` | composition of linear maps: first T, then S |
| `\cL(V, W)`, `\cL(V)` | all linear maps V → W; operators on V |
| `\ker T`, `\im T` | kernel, image |
| `\rank T`, `\nullity T` | dim im T, dim ker T |
| `I`, `I_n`, `\id_V` | identity matrix; identity operator |
| `A, B, C` | matrices, plain capitals. Entries `a_{ij}`, or `(A)_{ij}` |
| `A\tp` | transpose, rendered Aᵀ |
| `A^{*}` | conjugate transpose (and adjoint of an operator) |
| `\mtx{T}{\sB}{\sC}` | matrix of T from basis 𝓑 (input) to 𝓒 (output), rendered [T]_𝓑^𝓒; `[T]_{\sB}` when 𝓑 = 𝓒 |
| `\mtx{\id}{\sB}{\sC}` | change-of-coordinates matrix from 𝓑 to 𝓒 |
| `\tr A`, `\det A` | trace, determinant |
| `\adj A` | adjugate |
| `\diag(d_1, \dots, d_n)` | diagonal matrix |
| `A \sim B` | similar |
| `T'` | dual map (transpose of T) W* → V*. The star is reserved for adjoints |
| `V^{*}`, `\v^{*}` / `\varphi` | dual space; functionals are Greek letters φ, ψ |
| `U^{0}` | annihilator of U in V* |
| `\GL_n(F)`, `\SL_n(F)` | general and special linear groups |

## Polynomials, eigenvalues, canonical forms

| Type | Meaning |
|---|---|
| `p_T(x) = \det(xI - T)` | characteristic polynomial (monic) |
| `m_T(x)` | minimal polynomial |
| `\spec(T)` | set of eigenvalues |
| `E_\lambda(T) = \ker(T - \lambda I)` | eigenspace |
| `G_\lambda(T) = \ker(T - \lambda I)^{n}` | generalized eigenspace |
| `J_k(\lambda)` | k×k Jordan block, λ on the diagonal, 1 on the **super**diagonal |
| `C(p)` | companion matrix of a monic p |
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
| `A \circ B` | Hadamard (entrywise) product |
| `\norm{\x}_p` | p-norm. `\norm{A}_F` Frobenius, `\norm{A}_2` spectral/operator 2-norm |
| `\norm{A}` | operator norm induced by the named vector norm |
| `\kappa(A)` | condition number |
| `\conv(S)` | convex hull |
| `x \prec y`, `x \prec_w y` | majorization, weak majorization |
| `x^{\downarrow}` | decreasing rearrangement |

## Label naming

Labels are global and must be unique across the book.

- **Format:** `<env>-<topic words>`, e.g. `def-linear-independence`, `thm-rank-nullity`, `lem-exchange`, `exm-rotation-no-real-eigenvalues`.
- **Exercises:** `exr-<section-slug>-<group><n>`, e.g. `exr-span-b2`.
- **Before creating a label**, check it is free: `grep -rn "#thm-rank-nullity" src`.
- **Existing labels** of results that survive a rewrite keep their exact label, so links stay stable.
