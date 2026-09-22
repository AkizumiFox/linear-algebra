# The Dual Map and the Transpose

So far each space has had its own dual, but the duals of different spaces have not talked to each other. Linear algebra is about maps, so the question is: what does a linear map \( T \colon V \to W \) do to functionals? This section shows that \( T \) moves vectors forward but moves measurements **backward**, giving the dual map \( T' \colon W^{*} \to V^{*} \). In dual bases its matrix is the transpose of the matrix of \( T \), which finally explains what the transpose of Chapter 0 means. The kernel and image of \( T' \) are annihilators of the image and kernel of \( T \), and counting dimensions gives a third proof that row rank equals column rank. At the end we return to the double dual and prove that the evaluation map is compatible with every linear map.

## Pulling functionals back

After spaces come the maps between them. We have a linear map \( T \colon V \to W \) and the two spaces of measurements \( V^{*} \) and \( W^{*} \). We want to know how \( T \) relates them.

Start with the standard example, a matrix map \( T_{\A} \colon F^n \to F^m \), \( \x \mapsto \A\x \), with \( \A \in M_{m \times n}(F) \). A functional on \( F^m \) is \( \psi(\y) = \b\tp\y \) for a unique \( \b \in F^m \) (@thm-functionals-on-fn). Given \( \psi \), there is one obvious way to measure a vector \( \x \in F^n \): move it to \( F^m \) with \( T_{\A} \), then measure. The result is
\[
\psi(T_{\A}\x) = \b\tp \A\x = (\A\tp\b)\tp\x,
\]
using \( (\A\tp\b)\tp = \b\tp \A \) (@thm-transpose-properties). So "move, then measure" is again a functional, now on \( F^n \), and it is given by the vector \( \A\tp\b \). The transpose appears by itself. The recipe "compose with \( T \)" makes sense for any linear map, and it deserves a name.

*The dual map pulls a measurement of \( W \) back to a measurement of \( V \): first move the vector with \( T \), then measure it in \( W \).*

::: {#def-dual-map}
[Dual Map]

Let \( V \) and \( W \) be vector spaces over \( F \), and let \( T \in \cL(V, W) \). The **dual map** of \( T \) is the map
\[
T' \colon W^{*} \to V^{*}, \qquad T'(\psi) \coloneqq \psi T = \psi \circ T .
\]
That is, \( (T'\psi)(\v) = \psi(T\v) \) for every \( \psi \in W^{*} \) and every \( \v \in V \).
:::

In words, clause by clause:

- The input of \( T' \) is a functional on the **codomain** \( W \), and the output is a functional on the **domain** \( V \). The arrow is reversed.
- The formula \( (T'\psi)(\v) = \psi(T\v) \) has two steps: to measure \( \v \) with \( T'\psi \), send \( \v \) to \( W \) with \( T \), then apply \( \psi \) there.
- No basis and no finite dimension are involved.

**Well-definedness.** Two things must be checked. First, \( T'\psi \) must lie in \( V^{*} \): it is the composite of the linear maps \( T \colon V \to W \) and \( \psi \colon W \to F \), so it is linear by @thm-composition-linear (a). Second, \( T' \) should be linear, so that \( T' \in \cL(W^{*}, V^{*}) \). By the distributive laws in @thm-composition-linear (d), for \( \psi_1, \psi_2 \in W^{*} \) and \( c \in F \),
\[
\begin{aligned}
T'(\psi_1 + \psi_2) &= (\psi_1 + \psi_2)T = \psi_1T + \psi_2T = T'\psi_1 + T'\psi_2, \\
T'(c\psi) &= (c\psi)T = c(\psi T) = cT'\psi .
\end{aligned}
\]

::: {#exm-dual-map-examples}
[Dual Maps in Four Settings]

::: {.enumerate options="label=(\alph*)"}
1. For \( \A \in M_{m \times n}(F) \), describe \( T_{\A}' \) in terms of the vectors \( \b \) and \( \A\tp\b \) that represent functionals.
2. Let \( D \colon \nR[x]_{\le 3} \to \nR[x]_{\le 2} \), \( D(p) = p' \), and let \( \varepsilon_2 \in (\nR[x]_{\le 2})^{*} \) be \( \varepsilon_2(q) = q(2) \). Compute \( D'(\varepsilon_2) \).
3. Let \( S \colon F[x] \to F[x] \), \( S(p) = xp \), and let \( \varphi_k \in F[x]^{*} \) send a polynomial to its coefficient of \( x^k \). Compute \( S'(\varphi_k) \) for every \( k \in \nN \).
4. Find \( (\id_V)' \), the dual map of the zero map \( V \to W \), and the dual map of the inclusion \( \iota \colon U \to V \), \( \iota(\u) = \u \), of a subspace \( U \subseteq V \).
:::
:::

::: {.solution}
(a) If \( \psi(\y) = \b\tp\y \), the computation before the definition shows \( (T_{\A}'\psi)(\x) = (\A\tp\b)\tp\x \). So, identifying a functional with its vector, \( T_{\A}' \) is \( \b \mapsto \A\tp\b \). In row language: \( T_{\A}' \) sends the row \( \b\tp \) to the row \( \b\tp \A \).

(b) For \( p \in \nR[x]_{\le 3} \), \( (D'\varepsilon_2)(p) = \varepsilon_2(Dp) = p'(2) \). So \( D' \) turns "the value at \( 2 \)" into "the slope at \( 2 \)".

(c) \( (S'\varphi_k)(p) = \varphi_k(xp) \). Multiplying by \( x \) shifts every coefficient up one place, so the coefficient of \( x^k \) in \( xp \) is the coefficient of \( x^{k-1} \) in \( p \) when \( k \ge 1 \), and \( 0 \) when \( k = 0 \). Hence \( S'\varphi_k = \varphi_{k-1} \) for \( k \ge 1 \), and \( S'\varphi_0 = 0 \). Here \( F[x] \) is infinite-dimensional, and the definition works all the same.

(d) \( (\id_V)'\varphi = \varphi \circ \id_V = \varphi \), so \( (\id_V)' = \id_{V^{*}} \). For the zero map \( 0 \colon V \to W \), \( (0'\psi)(\v) = \psi(\0) = 0 \) (@thm-zero-maps-to-zero), so \( 0' \) is the zero map \( W^{*} \to V^{*} \). For the inclusion, \( (\iota'\varphi)(\u) = \varphi(\u) \) for \( \u \in U \), so \( \iota'\varphi = \varphi|_U \) is the **restriction** of \( \varphi \) to \( U \). The restriction map \( V^{*} \to U^{*} \) is thus a dual map; we study it further in the next section.
:::

Here is a non-example by minimal change. Try to push functionals **forward** instead: for \( T \colon V \to W \) and \( \varphi \in V^{*} \), look for a \( \psi \in W^{*} \) with \( \psi T = \varphi \), and call it "\( T_{*}\varphi \)". Take \( T \colon \nR \to \nR^2 \), \( T(t) = (t, 0) \), and \( \varphi(t) = t \). Then \( \psi(x, y) = x + cy \) satisfies \( \psi(T(t)) = t \) for **every** \( c \in \nR \), so there is no single answer. And for the zero map \( \nR \to \nR^2 \), no \( \psi \) at all satisfies \( \psi \circ 0 = \varphi \). What fails is well-definedness: a function must assign **exactly one** value. Composition with \( T \) goes only one way, on the right, and that forces the direction \( W^{*} \to V^{*} \).

**Why this definition.** From \( T \colon V \to W \) and \( \psi \colon W \to F \), the only composite we can form is \( \psi T \); the non-example shows that the other direction is not a function. Linearity of \( T' \) comes for free from the distributive laws. The name "dual map" says that \( T' \) is the map \( T \) induces between the duals. It is also called the **transpose** of \( T \), for a reason that the matrix theorem below makes exact. We write \( T' \) rather than \( T^{*} \), because \( T^{*} \) is reserved for the adjoint of Chapter 10, which is related to \( T' \) but needs an inner product.

::: {.warning}
**The dual map goes backwards.** For \( T \colon V \to W \), the dual map is \( T' \colon W^{*} \to V^{*} \), **not** \( V^{*} \to W^{*} \). As a result, composition reverses order: if \( T \colon U \to V \) and \( S \colon V \to W \), then \( (ST)' = T'S' \), just as \( (\A\B)\tp = \B\tp \A\tp \). The other order \( S'T' \) does not even make sense: \( T' \) lands in \( U^{*} \), where \( S' \) is not defined.
:::

::: {.check}
Let \( T \colon \nR^3 \to \nR^2 \), \( T(x, y, z) = (x - z, 2y) \), and \( \psi(u, v) = u + v \). Compute \( T'\psi \). If \( T' \) is written as a matrix in some bases, what is its size?
:::

::: {.solution}
\( (T'\psi)(x, y, z) = \psi(x - z, 2y) = x + 2y - z \). The map \( T' \) goes from \( (\nR^2)^{*} \), of dimension \( 2 \), to \( (\nR^3)^{*} \), of dimension \( 3 \) (@cor-dimension-dual-space), so its matrix is \( 3 \times 2 \), the size of the transpose of the \( 2 \times 3 \) matrix of \( T \).
:::

The first payoff is that duals behave well under the operations on maps, with one reversal.

::: {#thm-dual-map-properties}
[Properties of the Dual Map]

Let \( U, V, W \) be vector spaces over \( F \).

::: {.enumerate options="label=(\alph*)"}
1. For \( S, T \in \cL(V, W) \) and \( a, b \in F \), \( (aS + bT)' = aS' + bT' \).
2. For \( T \in \cL(U, V) \) and \( S \in \cL(V, W) \), \( (ST)' = T'S' \).
3. \( (\id_V)' = \id_{V^{*}} \).
4. If \( T \in \cL(V, W) \) is invertible, then \( T' \) is invertible and \( (T')^{-1} = (T^{-1})' \).
:::
:::

::: {.idea}
Each identity is an equality of maps into a dual space, so we evaluate both sides at a functional, and then evaluate the resulting functionals at a vector. After that, each line is the definition of \( T' \) read twice. Part (d) needs no computation: apply (b) and (c) to \( T^{-1}T = \id_V \) and \( TT^{-1} = \id_W \).
:::

::: {.proof}
(a) Let \( \psi \in W^{*} \) and \( \v \in V \). Using the linearity of \( \psi \) and the pointwise operations (@def-space-of-linear-maps),
\[
\bigl((aS + bT)'\psi\bigr)(\v) = \psi(aS\v + bT\v) = a\psi(S\v) + b\psi(T\v) = \bigl(aS'\psi + bT'\psi\bigr)(\v).
\]
Hence \( (aS + bT)'\psi = (aS' + bT')\psi \) for every \( \psi \), and \( (aS + bT)' = aS' + bT' \).

(b) Let \( \psi \in W^{*} \). By @def-dual-map and associativity of composition (@thm-composition-linear (b)),
\[
(ST)'\psi = \psi(ST) = (\psi S)T = T'(\psi S) = T'(S'\psi) = (T'S')\psi .
\]
Hence \( (ST)' = T'S' \).

(c) This is @exm-dual-map-examples (d).

(d) Suppose \( T \) is invertible with inverse \( T^{-1} \in \cL(W, V) \). By (b) and (c),
\[
T'(T^{-1})' = (T^{-1}T)' = (\id_V)' = \id_{V^{*}}, \qquad (T^{-1})'T' = (TT^{-1})' = (\id_W)' = \id_{W^{*}} .
\]
The map \( (T^{-1})' \) is linear, so by @def-invertible-linear-map \( T' \) is invertible with inverse \( (T^{-1})' \). This proves the theorem.
:::

Part (a) says that \( T \mapsto T' \) is itself a linear map \( \cL(V, W) \to \cL(W^{*}, V^{*}) \). Part (b) is the reversal of the warning. Parts (c) and (d) say that dualizing turns isomorphisms into isomorphisms, so isomorphic spaces have isomorphic duals.

## The matrix of the dual map

Now we fix bases and compute. Let \( \sB = (\v_1, \dots, \v_n) \) be a basis of \( V \) with dual basis \( \sB^{*} = (\varphi_1, \dots, \varphi_n) \) (@def-dual-basis), and \( \sC = (\w_1, \dots, \w_m) \) a basis of \( W \) with dual basis \( \sC^{*} = (\psi_1, \dots, \psi_m) \). The map \( T \) has the \( m \times n \) matrix \( \mtx{T}{\sB}{\sC} \) (@def-matrix-of-linear-map). The dual map \( T' \colon W^{*} \to V^{*} \) has input basis \( \sC^{*} \) and output basis \( \sB^{*} \), so its matrix is \( \mtx{T'}{\sC^{*}}{\sB^{*}} \), of size \( n \times m \). The size already suggests the answer, and @exm-dual-map-examples (a) suggests it for matrix maps.

::: {#thm-matrix-of-dual-map}
[The Matrix of the Dual Map Is the Transpose]

Let \( V \) and \( W \) be finite-dimensional vector spaces over \( F \), with ordered bases \( \sB \) of \( V \) and \( \sC \) of \( W \), and let \( \sB^{*} \) and \( \sC^{*} \) be their dual bases. For every \( T \in \cL(V, W) \),
\[
\mtx{T'}{\sC^{*}}{\sB^{*}} = \left(\mtx{T}{\sB}{\sC}\right)\tp .
\]
:::

::: {.idea}
Both matrices are tables of the same numbers \( \psi_i(T\v_j) \). In \( \mtx{T}{\sB}{\sC} \), the \( (i, j) \) entry is the \( \w_i \)-coordinate of \( T\v_j \), and a dual basis vector **reads off** a coordinate: that coordinate is \( \psi_i(T\v_j) \). In \( \mtx{T'}{\sC^{*}}{\sB^{*}} \), column \( i \) holds the \( \sB^{*} \)-coordinates of \( T'\psi_i \), and the \( \varphi_j \)-coordinate of a functional is its value at \( \v_j \): that is \( (T'\psi_i)(\v_j) = \psi_i(T\v_j) \). The same number sits at \( (i, j) \) in one matrix and at \( (j, i) \) in the other.
:::

::: {.proof}
Write \( \sB = (\v_1, \dots, \v_n) \), \( \sB^{*} = (\varphi_1, \dots, \varphi_n) \), \( \sC = (\w_1, \dots, \w_m) \), \( \sC^{*} = (\psi_1, \dots, \psi_m) \), and \( \A = (a_{kj}) = \mtx{T}{\sB}{\sC} \). By @def-matrix-of-linear-map, \( a_{ij} \) is the \( i \)-th entry of \( \coord{T\v_j}{\sC} \), and by @thm-dual-basis (a) that entry is read off by \( \psi_i \):
\[
\psi_i(T\v_j) = a_{ij} . \tag{$\ast$}
\]
Next, by @thm-dual-basis (c), every \( \varphi \in V^{*} \) satisfies \( \varphi = \sum_{j=1}^{n} \varphi(\v_j)\varphi_j \). Since \( \sB^{*} \) is a basis, coordinates in it are unique (@thm-unique-representation), so \( \coord{\varphi}{\sB^{*}} = (\varphi(\v_1), \dots, \varphi(\v_n)) \).

By @def-matrix-of-linear-map, column \( i \) of \( \mtx{T'}{\sC^{*}}{\sB^{*}} \) is \( \coord{T'\psi_i}{\sB^{*}} \). By the previous paragraph and \( (\ast) \), its \( j \)-th entry is
\[
(T'\psi_i)(\v_j) = \psi_i(T\v_j) = a_{ij} .
\]
So the \( (j, i) \) entry of \( \mtx{T'}{\sC^{*}}{\sB^{*}} \) is \( a_{ij} \), which is the \( (j, i) \) entry of \( \A\tp \) (@def-transpose). Both matrices are \( n \times m \), so \( \mtx{T'}{\sC^{*}}{\sB^{*}} = \A\tp \). This proves the theorem.
:::

This is the meaning of the transpose. In Chapter 0, @def-transpose was a rule for rearranging entries. Now we see it as the matrix shadow of pulling functionals back: **transposing a matrix is dualizing the map**, provided we use dual bases on both sides. Every property of the transpose becomes a property of dual maps, and conversely; for instance, @thm-dual-map-properties (b) and this theorem together give \( (\A\B)\tp = \B\tp \A\tp \) a second time (Exercise B3 below).

::: {#exm-matrix-of-dual-map}
[A \( 2 \times 3 \) Example]

Let \( T \colon \nR[x]_{\le 2} \to \nR^2 \), \( T(p) = (p(1), p'(1)) \). Use the basis \( \sB = (1, x, x^2) \), whose dual basis \( \sB^{*} = (\varphi_0, \varphi_1, \varphi_2) \) consists of \( \varphi_0(p) = p(0) \), \( \varphi_1(p) = p'(0) \), \( \varphi_2(p) = p''(0)/2 \) (@exm-dual-basis-polynomials), and the standard basis \( \sC = (\e_1, \e_2) \) of \( \nR^2 \), with dual basis \( \sC^{*} = (\eta_1, \eta_2) \), \( \eta_1(u, v) = u \), \( \eta_2(u, v) = v \).

::: {.enumerate options="label=(\alph*)"}
1. Find \( \A = \mtx{T}{\sB}{\sC} \).
2. Compute \( T'\eta_1 \) and \( T'\eta_2 \) directly as combinations of \( \varphi_0, \varphi_1, \varphi_2 \), write down \( \mtx{T'}{\sC^{*}}{\sB^{*}} \), and compare with \( \A\tp \).
3. Use the matrix to compute \( T'\psi \) for \( \psi = -2\eta_1 + \eta_2 \), and check the answer directly.
:::
:::

::: {.solution}
(a) \( T(1) = (1, 0) \), \( T(x) = (1, 1) \), \( T(x^2) = (1, 2) \). These are the columns:
\[
\A = \mtx{T}{\sB}{\sC} = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \end{pmatrix}.
\]
(b) Let \( p = a + bx + cx^2 \), so \( \varphi_0(p) = a \), \( \varphi_1(p) = b \), \( \varphi_2(p) = c \). Then
\[
\begin{aligned}
(T'\eta_1)(p) &= \eta_1(Tp) = p(1) = a + b + c, \\
(T'\eta_2)(p) &= \eta_2(Tp) = p'(1) = b + 2c .
\end{aligned}
\]
So \( T'\eta_1 = \varphi_0 + \varphi_1 + \varphi_2 \) and \( T'\eta_2 = \varphi_1 + 2\varphi_2 \). Their coordinate vectors in \( \sB^{*} \) are the columns of
\[
\mtx{T'}{\sC^{*}}{\sB^{*}} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 1 & 2 \end{pmatrix} = \A\tp,
\]
as @thm-matrix-of-dual-map predicts. Read in words, the first column is Taylor's formula \( p(1) = p(0) + p'(0) + \tfrac12 p''(0) \) for quadratics, and the second is \( p'(1) = p'(0) + p''(0) \).

(c) \( \coord{\psi}{\sC^{*}} = (-2, 1) \). By @thm-matrix-of-map-coordinates,
\[
\coord{T'\psi}{\sB^{*}} = \A\tp\begin{pmatrix} -2 \\ 1 \end{pmatrix} = \begin{pmatrix} -2 \\ -1 \\ 0 \end{pmatrix},
\]
so \( T'\psi = -2\varphi_0 - \varphi_1 \). Directly: \( (T'\psi)(p) = -2p(1) + p'(1) = -2(a + b + c) + (b + 2c) = -2a - b \), which is \( (-2\varphi_0 - \varphi_1)(p) \).
:::

::: {.warning}
**Dual bases on both sides.** The transpose rule needs the **dual** bases \( \sC^{*} \) and \( \sB^{*} \). With other bases of \( W^{*} \) and \( V^{*} \) the matrix of \( T' \) is usually not \( \A\tp \). In @exm-matrix-of-dual-map, keep \( \sB^{*} \) but use the basis \( (\eta_1 + \eta_2, \eta_2) \) of \( (\nR^2)^{*} \): then \( T'(\eta_1 + \eta_2) = \varphi_0 + 2\varphi_1 + 3\varphi_2 \), so the first column is \( (1, 2, 3) \), not the first column \( (1, 1, 1) \) of \( \A\tp \).
:::

## Kernel and image of the dual map

The kernel and image of \( T' \) are subspaces of \( W^{*} \) and \( V^{*} \). The natural candidates for them are annihilators of the subspaces that \( T \) defines, and the dictionary swaps kernel and image.

::: {#thm-kernel-image-dual-map}
[Kernel and Image of the Dual Map]

Let \( V \) and \( W \) be vector spaces over \( F \), and let \( T \in \cL(V, W) \).

::: {.enumerate options="label=(\alph*)"}
1. \( \ker T' = (\im T)^{0} \).
2. If \( V \) and \( W \) are finite-dimensional, then \( \im T' = (\ker T)^{0} \).
:::
:::

::: {.idea}
(a) is a chain of definitions: \( \psi T = 0 \) says that \( \psi \) vanishes on every \( T\v \), that is, on \( \im T \). For (b), one inclusion is just as easy: \( \psi T \) kills every vector that \( T \) kills. The reverse inclusion asks us to **extend** a functional given on \( V \) to one of the form \( \psi T \), which is a construction. Instead we count. Rank–Nullity for \( T' \), together with (a) and the dimension formula for annihilators, gives \( \dim \im T' = \rank T \); the dimension formula in \( V \) and Rank–Nullity for \( T \) give \( \dim (\ker T)^{0} = \rank T \). Finite dimension is spent exactly on these counts.
:::

::: {.proof}
(a) Let \( \psi \in W^{*} \). Then \( \psi \in \ker T' \) iff \( \psi T = 0 \) iff \( \psi(T\v) = 0 \) for every \( \v \in V \) iff \( \psi(\w) = 0 \) for every \( \w \in \im T \) (@def-image) iff \( \psi \in (\im T)^{0} \) (@def-annihilator).

(b) Let \( n = \dim V \) and \( m = \dim W \), so \( \dim V^{*} = n \) and \( \dim W^{*} = m \) (@cor-dimension-dual-space).

*Inclusion.* Let \( \varphi \in \im T' \), say \( \varphi = \psi T \) with \( \psi \in W^{*} \). For \( \u \in \ker T \), \( \varphi(\u) = \psi(T\u) = \psi(\0) = 0 \). Hence \( \varphi \in (\ker T)^{0} \), and \( \im T' \subseteq (\ker T)^{0} \).

*Dimensions.* By the Rank–Nullity Theorem (@thm-rank-nullity) for \( T' \colon W^{*} \to V^{*} \), then (a), then @thm-dimension-annihilator for the subspace \( \im T \) of \( W \),
\[
\begin{aligned}
\dim \im T' &= m - \dim \ker T' = m - \dim (\im T)^{0} \\
&= m - (m - \dim \im T) = \rank T .
\end{aligned}
\]
By @thm-dimension-annihilator for the subspace \( \ker T \) of \( V \), and Rank–Nullity for \( T \),
\[
\dim (\ker T)^{0} = n - \dim \ker T = \rank T .
\]
So \( \im T' \) is a subspace of the finite-dimensional space \( (\ker T)^{0} \) with the same dimension, and @thm-dim-impl-eq gives \( \im T' = (\ker T)^{0} \). This proves the theorem.
:::

For a matrix map, this is a statement about rows. By @exm-dual-map-examples (a), \( T_{\A}' \) sends the row \( \b\tp \) to \( \b\tp \A \), so \( \im T_{\A}' \) is the set of combinations of the rows of \( \A \): it is the row space, read as functionals. Part (b) then says that **the functionals vanishing on \( \nul(\A) \) are exactly the combinations of the rows of \( \A \)**. Part (a) says that the functionals vanishing on \( \col(\A) \) are the rows \( \b\tp \) with \( \b\tp \A = 0 \), that is, \( \A\tp\b = \0 \).

::: {#exm-kernel-image-dual-map}
[Kernel and Image of a Dual Map]

Let \( T = T_{\A} \colon \nR^3 \to \nR^3 \) with
\[
\A = \begin{pmatrix} 1 & 0 & 2 \\ 0 & 1 & -1 \\ 1 & 1 & 1 \end{pmatrix}.
\]
Find bases of \( \ker T' \) and \( \im T' \), written as explicit functionals, and check @thm-kernel-image-dual-map.
:::

::: {.solution}
*The matrix world.* The third row of \( \A \) is the sum of the first two, and subtracting them leaves the RREF \( \begin{pmatrix} 1 & 0 & 2 \\ 0 & 1 & -1 \\ 0 & 0 & 0 \end{pmatrix} \). So \( \rank \A = 2 \), and \( \A\x = \0 \) gives \( x = -2z \), \( y = z \): \( \ker T = \Span\bigl((-2, 1, 1)\bigr) \). The pivot columns give \( \im T = \Span\bigl((1, 0, 1), (0, 1, 1)\bigr) \) (@thm-basis-column-space).

*Kernel of \( T' \).* By @thm-matrix-of-dual-map with standard bases and @exm-matrix-of-matrix-map (a), a functional \( \psi(u, v, w) = b_1u + b_2v + b_3w \) lies in \( \ker T' \) iff \( \A\tp\b = \0 \):
\[
b_1 + b_3 = 0, \qquad b_2 + b_3 = 0, \qquad 2b_1 - b_2 + b_3 = 0 .
\]
The first two give \( \b = t(1, 1, -1) \), and these satisfy the third. So \( \ker T' = \Span(\psi_0) \) with \( \psi_0(u, v, w) = u + v - w \). *Check:* \( \psi_0(1, 0, 1) = 0 \) and \( \psi_0(0, 1, 1) = 0 \), so \( \psi_0 \) vanishes on \( \im T \); and \( \dim (\im T)^{0} = 3 - 2 = 1 \) (@thm-dimension-annihilator). So \( \ker T' = (\im T)^{0} \).

*Image of \( T' \).* By @exm-dual-map-examples (a), \( \im T' \) is spanned by the rows of \( \A \) read as functionals, and the first two rows already span (the third is their sum):
\[
\varphi_1(x, y, z) = x + 2z, \qquad \varphi_2(x, y, z) = y - z .
\]
They are independent (neither is a multiple of the other), so \( (\varphi_1, \varphi_2) \) is a basis of \( \im T' \). *Check:* \( \varphi_1(-2, 1, 1) = 0 \) and \( \varphi_2(-2, 1, 1) = 0 \), so both vanish on \( \ker T \), and \( \dim (\ker T)^{0} = 3 - 1 = 2 \). So \( \im T' = (\ker T)^{0} \).
:::

Counting dimensions in the proof of @thm-kernel-image-dual-map already gave \( \dim \im T' = \rank T \). We record it, together with its most famous consequence.

::: {#cor-rank-dual-map}
[Rank of the Dual Map]

::: {.enumerate options="label=(\alph*)"}
1. Let \( V \) and \( W \) be finite-dimensional vector spaces over \( F \), and \( T \in \cL(V, W) \). Then \( \rank T' = \rank T \).
2. For every \( \A \in M_{m \times n}(F) \), \( \rank \A\tp = \rank \A \). Equivalently, \( \dim \row(\A) = \dim \col(\A) \): **row rank equals column rank**.
:::
:::

::: {.proof}
(a) This is the first display in the proof of @thm-kernel-image-dual-map (b).

(b) Let \( \sE_n \), \( \sE_m \) be the standard bases. By @exm-matrix-of-matrix-map (a), \( \mtx{T_{\A}}{\sE_n}{\sE_m} = \A \), so by @thm-matrix-of-dual-map, \( \mtx{T_{\A}'}{\sE_m^{*}}{\sE_n^{*}} = \A\tp \). By @thm-rank-map-equals-rank-matrix (a), applied to \( T_{\A} \) and to \( T_{\A}' \), and by (a),
\[
\rank \A = \rank T_{\A} = \rank T_{\A}' = \rank \A\tp .
\]
Finally, the transpose \( M_{1 \times n}(F) \to F^n \) is linear (@thm-transpose-properties) and bijective (it is its own inverse), and it sends row \( i \) of \( \A \) to column \( i \) of \( \A\tp \). By @thm-linear-combination it maps \( \row(\A) \) onto \( \col(\A\tp) \), so these spaces are isomorphic and \( \dim \row(\A) = \dim \col(\A\tp) = \rank \A\tp = \rank \A = \dim \col(\A) \) (@thm-isomorphic-iff-same-dimension, @def-rank-matrix).
:::

This is the third proof of this fact in the book, and each one explains it differently.

- **Chapter 2** (@thm-row-rank-equals-column-rank) counted pivots. Row reduction preserves the row space and the relations among the columns, and in the RREF both dimensions visibly equal the number of pivots. The proof is an algorithm.
- **Chapter 3, §8** factored \( \A = \B\D \) through a space of dimension \( \dim \col(\A) \), after @prp-rank-minimal-factorization, and saw that the rows of \( \A \) are combinations of the few rows of \( \D \). The proof is a factorization.
- **Here** there are no row operations and no factorizations. The equality is the dimension formula \( \dim U + \dim U^{0} = \dim V \), applied once to \( \im T \) in \( W \) and once to \( \ker T \) in \( V \), glued together by Rank–Nullity. The rows of \( \A \) are the functionals that \( T_{\A}' \) produces, and the columns span the image of \( T_{\A} \); the two counts agree because pulling back measurements loses exactly as much as pushing forward vectors.

(The dimension formula for annihilators in section 2 was proved by extending a basis of \( U \), without using ranks of matrices, so this proof does not go in a circle.)

The dictionary also swaps injective and surjective.

::: {#cor-injective-iff-dual-surjective}
[Injective and Surjective Swap Under Duality]

Let \( V \) and \( W \) be finite-dimensional vector spaces over \( F \), and \( T \in \cL(V, W) \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( T \) is surjective if and only if \( T' \) is injective;
2. \( T \) is injective if and only if \( T' \) is surjective.
:::
:::

::: {.proof}
Let \( n = \dim V \) and \( m = \dim W \). A finite-dimensional space is \( \{\0\} \) exactly when its dimension is \( 0 \).

(a) By @thm-injective-iff-trivial-kernel and @thm-kernel-image-dual-map (a), \( T' \) is injective iff \( (\im T)^{0} = \{0\} \). By @thm-dimension-annihilator, \( \dim (\im T)^{0} = m - \rank T \), so this holds iff \( \rank T = m \), that is, iff \( T \) is surjective (@cor-rank-nullity-consequences (b)).

(b) \( T' \) is surjective iff \( \im T' = V^{*} \), iff \( \dim \im T' = n \) (by @thm-dim-impl-eq for one direction, since \( \dim V^{*} = n \)). By @cor-rank-dual-map (a), \( \dim \im T' = \rank T \), so this holds iff \( \rank T = n \), that is, iff \( T \) is injective (@cor-rank-nullity-consequences (a)).
:::

For \( T_{\A} \), part (a) reads: \( \A\x = \b \) is solvable for every \( \b \) exactly when \( \A\tp\y = \0 \) has only the trivial solution. So a question about the columns of \( \A \) turns into a question about the columns of \( \A\tp \), the rows of \( \A \). Exercise C1 below sharpens this into a test for a single \( \b \).

## Naturality of the double dual

In the previous section we called \( \ev_V \colon V \to V^{**} \) natural because it needs no choice, and promised a sharper sense: compatibility with every linear map. With dual maps available, we can state it. A linear map \( T \colon V \to W \) has a dual \( T' \colon W^{*} \to V^{*} \), and that has a dual in turn,
\[
T'' \coloneqq (T')' \colon V^{**} \to W^{**},
\]
which points **forward** again, because we reversed twice.

::: {#thm-evaluation-natural}
[The Evaluation Map Is Natural]

Let \( V \) and \( W \) be vector spaces over \( F \), and let \( T \in \cL(V, W) \). Then
\[
T''\,\ev_V = \ev_W\,T .
\]
That is, \( T''(\ev_{\v}) = \ev_{T\v} \) for every \( \v \in V \). If \( V \) and \( W \) are finite-dimensional, then \( T'' = \ev_W\,T\,\ev_V^{-1} \).
:::

The statement says that the square below commutes, for **every** linear map \( T \): going right then down (apply \( T \), then evaluate) equals going down then right (evaluate, then apply \( T'' \)).

\begin{center}
\begin{tikzpicture}[>=Stealth, x=3.6cm, y=2.1cm]
  \node (V) at (0,1) {$V$};
  \node (W) at (1,1) {$W$};
  \node (Vdd) at (0,0) {$V^{**}$};
  \node (Wdd) at (1,0) {$W^{**}$};
  \draw[->] (V) -- node[above] {$T$} (W);
  \draw[->] (Vdd) -- node[below] {$T''$} (Wdd);
  \draw[->] (V) -- node[left] {$\operatorname{ev}_V$} (Vdd);
  \draw[->] (W) -- node[right] {$\operatorname{ev}_W$} (Wdd);
\end{tikzpicture}
\end{center}

::: {.proof}
Let \( \v \in V \). Both \( T''(\ev_{\v}) \) and \( \ev_{T\v} \) are functionals on \( W^{*} \), so let \( \psi \in W^{*} \). By @def-dual-map applied to \( T' \), then to \( T \),
\[
\bigl(T''(\ev_{\v})\bigr)(\psi) = \ev_{\v}(T'\psi) = (T'\psi)(\v) = \psi(T\v) = \ev_{T\v}(\psi).
\]
Hence \( T''(\ev_{\v}) = \ev_{T\v} \) for every \( \v \), which is \( T''\ev_V = \ev_W T \). If \( V \) is finite-dimensional, \( \ev_V \) is an isomorphism (@thm-double-dual-isomorphism); composing on the right with \( \ev_V^{-1} \) gives \( T'' = \ev_W T\ev_V^{-1} \).
:::

So, once \( V \) is identified with \( V^{**} \) and \( W \) with \( W^{**} \) through evaluation, the double dual map \( T'' \) **is** \( T \). The matrices agree: by @thm-double-dual-isomorphism, \( \ev \) carries \( \sB \) and \( \sC \) to the dual bases \( \sB^{**} \) and \( \sC^{**} \) of \( \sB^{*} \) and \( \sC^{*} \), and two applications of @thm-matrix-of-dual-map give \( \mtx{T''}{\sB^{**}}{\sC^{**}} = \bigl((\mtx{T}{\sB}{\sC})\tp\bigr)\tp = \mtx{T}{\sB}{\sC} \) (@thm-transpose-properties). The rule \( (\A\tp)\tp = \A \) is the matrix form of naturality.

::: {.remark}
No such statement holds for \( V \cong V^{*} \). Suppose that for every finite-dimensional real space \( V \) we had an isomorphism \( \theta_V \colon V \to V^{*} \), compatible with isomorphisms in the only way the directions allow: \( \theta_V = T'\,\theta_W\,T \) for every isomorphism \( T \colon V \to W \). Take \( V = W = \nR \) and \( T = 2\id \). Then \( T' = 2\id \) by @thm-dual-map-properties (a) and (c), so \( \theta_{\nR} = 2 \cdot 2 \cdot \theta_{\nR} = 4\theta_{\nR} \), which forces \( \theta_{\nR} = 0 \), not an isomorphism. The dual space is isomorphic to \( V \), but not naturally.
:::

## Exercises

### A. Check your understanding

::: {#exr-dual-map-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the dual map \( T' \) of \( T \in \cL(V, W) \), including its domain and codomain.
2. State the relation between \( \mtx{T'}{\sC^{*}}{\sB^{*}} \) and \( \mtx{T}{\sB}{\sC} \), with its hypotheses.
3. True or false: \( (ST)' = S'T' \) whenever \( ST \) is defined. Justify your answer.
4. True or false: \( \ker T' = (\ker T)^{0} \) for every linear map between finite-dimensional spaces. Justify your answer.
5. True or false: for \( T \in \cL(\nR^4, \nR^3) \), the dual map \( T' \) is never surjective. Justify your answer.
6. Name the two tools combined to prove \( \rank T' = \rank T \).
:::
:::

::: {.solution}
(a) For \( T \colon V \to W \), \( T' \colon W^{*} \to V^{*} \), \( T'(\psi) = \psi T \) (@def-dual-map).

(b) If \( V, W \) are finite-dimensional with bases \( \sB, \sC \) and dual bases \( \sB^{*}, \sC^{*} \), then \( \mtx{T'}{\sC^{*}}{\sB^{*}} = (\mtx{T}{\sB}{\sC})\tp \) (@thm-matrix-of-dual-map).

(c) False. The correct rule is \( (ST)' = T'S' \) (@thm-dual-map-properties (b)); for \( T \colon U \to V \), \( S \colon V \to W \) with \( U \neq W \), the composite \( S'T' \) is not even defined.

(d) False. \( \ker T' = (\im T)^{0} \). For the zero map \( T \colon \nR \to \nR \), \( \ker T = \nR \), so \( (\ker T)^{0} = \{0\} \), while \( T' = 0 \) has kernel \( \nR^{*} \neq \{0\} \).

(e) True. \( T' \) maps \( (\nR^3)^{*} \), of dimension \( 3 \), to \( (\nR^4)^{*} \), of dimension \( 4 \), so it cannot be surjective (@cor-rank-nullity-consequences (d)). This matches @cor-injective-iff-dual-surjective: \( T \) cannot be injective.

(f) The Rank–Nullity Theorem (@thm-rank-nullity) and the dimension formula for annihilators, \( \dim U + \dim U^{0} = \dim V \) (@thm-dimension-annihilator), together with \( \ker T' = (\im T)^{0} \).
:::

### B. Practice

::: {#exr-dual-map-b1}
[B1: Differentiation in dual bases]

Let \( D \colon \nR[x]_{\le 2} \to \nR[x]_{\le 2} \), \( D(p) = p' \), and let \( \sB = (1, x, x^2) \) with dual basis \( \sB^{*} = (\varphi_0, \varphi_1, \varphi_2) \), \( \varphi_k(p) = \) the coefficient of \( x^k \) in \( p \). Compute \( D'\varphi_0 \), \( D'\varphi_1 \), \( D'\varphi_2 \) directly, write down \( [D']_{\sB^{*}} \), and check that it is \( ([D]_{\sB})\tp \). Hence describe \( \ker D' \) and \( \im D' \), and verify @thm-kernel-image-dual-map.
:::

::: {.solution}
Let \( p = a + bx + cx^2 \), so \( Dp = b + 2cx \). Then \( (D'\varphi_0)(p) = \varphi_0(Dp) = b \), \( (D'\varphi_1)(p) = 2c \), \( (D'\varphi_2)(p) = 0 \). Hence
\[
D'\varphi_0 = \varphi_1, \qquad D'\varphi_1 = 2\varphi_2, \qquad D'\varphi_2 = 0 .
\]
The coordinate vectors \( (0, 1, 0) \), \( (0, 0, 2) \), \( (0, 0, 0) \) are the columns of \( [D']_{\sB^{*}} \). On the other side, \( D(1) = 0 \), \( D(x) = 1 \), \( D(x^2) = 2x \), so
\[
[D]_{\sB} = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix}, \qquad [D']_{\sB^{*}} = \begin{pmatrix} 0 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 2 & 0 \end{pmatrix} = ([D]_{\sB})\tp,
\]
as @thm-matrix-of-dual-map predicts.

From the formulas, \( D'(c_0\varphi_0 + c_1\varphi_1 + c_2\varphi_2) = c_0\varphi_1 + 2c_1\varphi_2 \), which is \( 0 \) iff \( c_0 = c_1 = 0 \). So \( \ker D' = \Span(\varphi_2) \) and \( \im D' = \Span(\varphi_1, \varphi_2) \). On the other hand \( \im D = \nR[x]_{\le 1} = \Span(1, x) \), and \( \varphi_2 \) is exactly the functional (up to scalars) vanishing on it, since \( c_0\varphi_0 + c_1\varphi_1 + c_2\varphi_2 \) kills \( 1 \) and \( x \) iff \( c_0 = c_1 = 0 \). So \( \ker D' = (\im D)^{0} \). Also \( \ker D = \Span(1) \), and a functional kills \( 1 \) iff \( c_0 = 0 \), so \( (\ker D)^{0} = \Span(\varphi_1, \varphi_2) = \im D' \).
:::

::: {#exr-dual-map-b2}
[B2: Kernel and image of a dual map]

Let \( \A = \begin{pmatrix} 1 & 2 & -1 \\ -2 & -4 & 2 \end{pmatrix} \) and \( T = T_{\A} \colon \nR^3 \to \nR^2 \). Find bases of \( \ker T' \) and \( \im T' \) as explicit functionals, and verify \( \dim \ker T' + \dim \im T' = 2 \) and \( \rank T' = \rank T \).
:::

::: {.solution}
The second row is \( -2 \) times the first, so \( \rank \A = 1 \), \( \im T = \col(\A) = \Span\bigl((1, -2)\bigr) \), and \( \ker T = \{ (x, y, z) : x + 2y - z = 0 \} \), of dimension \( 2 \).

*Kernel of \( T' \).* As in @exm-kernel-image-dual-map, \( \psi(u, v) = b_1u + b_2v \) lies in \( \ker T' \) iff \( \A\tp\b = \0 \), that is, \( b_1 - 2b_2 = 0 \), \( 2b_1 - 4b_2 = 0 \), \( -b_1 + 2b_2 = 0 \). So \( \b = t(2, 1) \), and \( \ker T' = \Span(\psi_0) \) with \( \psi_0(u, v) = 2u + v \). Check: \( \psi_0(1, -2) = 0 \), so \( \psi_0 \in (\im T)^{0} \), which has dimension \( 2 - 1 = 1 \).

*Image of \( T' \).* By @exm-dual-map-examples (a), \( \im T' \) is spanned by the rows of \( \A \) read as functionals, \( x + 2y - z \) and \( -2x - 4y + 2z \). The second is \( -2 \) times the first, so \( \im T' = \Span(\varphi_0) \) with \( \varphi_0(x, y, z) = x + 2y - z \). Check: \( \varphi_0 \) vanishes on \( \ker T \) by the description of \( \ker T \), and \( \dim (\ker T)^{0} = 3 - 2 = 1 \).

Hence \( \dim \ker T' + \dim \im T' = 1 + 1 = 2 = \dim (\nR^2)^{*} \), and \( \rank T' = 1 = \rank T \).
:::

::: {#exr-dual-map-b3}
[B3: The transpose of a product, again]

Let \( \A \in M_{m \times n}(F) \) and \( \B \in M_{n \times p}(F) \). Using \( T_{\A}T_{\B} = T_{\A\B} \) (Chapter 3, §6), @thm-dual-map-properties (b) and @thm-matrix-of-dual-map, give a new proof that \( (\A\B)\tp = \B\tp \A\tp \).
:::

::: {.solution}
Let \( \sE_p, \sE_n, \sE_m \) be the standard bases, with dual bases \( \sE_p^{*}, \sE_n^{*}, \sE_m^{*} \). By @exm-matrix-of-matrix-map (a), \( \mtx{T_{\A}}{\sE_n}{\sE_m} = \A \), \( \mtx{T_{\B}}{\sE_p}{\sE_n} = \B \), and \( \mtx{T_{\A\B}}{\sE_p}{\sE_m} = \A\B \). Since \( T_{\A\B} = T_{\A}T_{\B} \), @thm-dual-map-properties (b) gives \( T_{\A\B}' = T_{\B}'T_{\A}' \). Taking matrices, with @thm-matrix-of-composition in the middle and @thm-matrix-of-dual-map on the outside,
\[
(\A\B)\tp = \mtx{T_{\A\B}'}{\sE_m^{*}}{\sE_p^{*}} = \mtx{T_{\B}'T_{\A}'}{\sE_m^{*}}{\sE_p^{*}} = \mtx{T_{\B}'}{\sE_n^{*}}{\sE_p^{*}}\,\mtx{T_{\A}'}{\sE_m^{*}}{\sE_n^{*}} = \B\tp \A\tp .
\]
The reversal of order is now explained: it is the reversal of arrows under duality.
:::

### C. Going deeper

::: {#exr-dual-map-c1}
[C1: The Fredholm alternative]

::: {.enumerate options="label=(\alph*)"}
1. Let \( V, W \) be finite-dimensional, \( T \in \cL(V, W) \) and \( \w \in W \). Prove that \( T\v = \w \) has a solution \( \v \in V \) if and only if \( \psi(\w) = 0 \) for every \( \psi \in \ker T' \).
2. Deduce: for \( \A \in M_{m \times n}(F) \) and \( \b \in F^m \), the system \( \A\x = \b \) is consistent if and only if \( \y\tp\b = 0 \) for every \( \y \in F^m \) with \( \A\tp\y = \0 \).
3. Let \( \A = \begin{pmatrix} 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{pmatrix} \). Find a single linear condition on \( \b = (b_1, b_2, b_3) \in \nR^3 \) that is equivalent to consistency of \( \A\x = \b \).
:::

*Hint: for (a), combine @thm-kernel-image-dual-map with the description of a subspace by its annihilator in the previous section.*
:::

::: {.solution}
(a) \( T\v = \w \) has a solution iff \( \w \in \im T \). By @thm-kernel-image-dual-map (a), \( \ker T' = (\im T)^{0} \). By @cor-annihilator-of-annihilator applied to the subspace \( \im T \) of the finite-dimensional space \( W \),
\[
\begin{aligned}
\im T &= \{ \w \in W : \psi(\w) = 0 \text{ for every } \psi \in (\im T)^{0} \} \\
&= \{ \w \in W : \psi(\w) = 0 \text{ for every } \psi \in \ker T' \}.
\end{aligned}
\]
This is the claim.

(b) Apply (a) to \( T_{\A} \colon F^n \to F^m \). By @thm-functionals-on-fn, every \( \psi \in (F^m)^{*} \) is \( \psi(\u) = \y\tp\u \) for a unique \( \y \in F^m \). By @exm-dual-map-examples (a), \( T_{\A}'\psi \) is represented by \( \A\tp\y \), and the zero functional by \( \0 \); by uniqueness of the representing vector, \( \psi \in \ker T_{\A}' \) iff \( \A\tp\y = \0 \). For such \( \psi \), \( \psi(\b) = \y\tp\b \). So (a) says: \( \A\x = \b \) is consistent iff \( \y\tp\b = 0 \) for every \( \y \) with \( \A\tp\y = \0 \).

(c) \( \A\tp\y = \0 \) reads \( y_1 + y_2 + y_3 = 0 \) and \( y_1 + 2y_2 + 3y_3 = 0 \). Subtracting, \( y_2 + 2y_3 = 0 \), so \( \y = t(1, -2, 1) \). By (b), \( \A\x = \b \) is consistent iff \( \y\tp\b = 0 \) for all these \( \y \), that is, iff
\[
b_1 - 2b_2 + b_3 = 0 .
\]
In words, the system \( x_1 + kx_2 = b_k \) (\( k = 1, 2, 3 \)) asks for a line through the points \( (1, b_1), (2, b_2), (3, b_3) \), and it exists exactly when the second difference \( b_3 - 2b_2 + b_1 \) vanishes. No inner product was used: \( \y\tp\b \) is just a functional applied to \( \b \).
:::

::: {#exr-dual-map-c2}
[C2: Invariant subspaces and annihilators]

Let \( V \) be finite-dimensional, \( T \in \cL(V) \), and \( U \) a subspace of \( V \). Recall that \( U \) is **\( T \)-invariant** if \( T\u \in U \) for every \( \u \in U \). Prove that \( U \) is \( T \)-invariant if and only if \( U^{0} \) is \( T' \)-invariant.
:::

::: {.solution}
\( (\Rightarrow) \) Suppose \( U \) is \( T \)-invariant, and let \( \varphi \in U^{0} \). For every \( \u \in U \), \( (T'\varphi)(\u) = \varphi(T\u) = 0 \), because \( T\u \in U \). Hence \( T'\varphi \in U^{0} \), and \( U^{0} \) is \( T' \)-invariant.

\( (\Leftarrow) \) Suppose \( U^{0} \) is \( T' \)-invariant, and let \( \u \in U \). For every \( \varphi \in U^{0} \), \( T'\varphi \in U^{0} \), so \( \varphi(T\u) = (T'\varphi)(\u) = 0 \). Thus \( T\u \) is killed by every functional in \( U^{0} \). By @cor-annihilator-of-annihilator, \( T\u \in U \). Hence \( U \) is \( T \)-invariant.
:::

::: {#exr-dual-map-c3}
[C3: Duality without finite dimension]

Let \( V \) and \( W \) be arbitrary vector spaces over \( F \), and \( T \in \cL(V, W) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( T \) is surjective, then \( T' \) is injective.
2. Prove that if \( T \) is injective, then \( T' \) is surjective.
3. Check (b) on \( S \colon F[x] \to F[x] \), \( S(p) = xp \), from @exm-dual-map-examples (c): given \( \varphi \in F[x]^{*} \), find \( \psi \) with \( S'\psi = \varphi \). Is \( S' \) injective?
:::

*Hint: for (b), use @thm-basis-extension-general in \( W \).*
:::

::: {.solution}
(a) By @thm-kernel-image-dual-map (a), which needs no finite dimension, \( \ker T' = (\im T)^{0} = W^{0} \). A functional vanishing on all of \( W \) is the zero functional, so \( \ker T' = \{0\} \) and \( T' \) is injective (@thm-injective-iff-trivial-kernel).

(b) Let \( \varphi \in V^{*} \). By @thm-every-space-has-basis, \( V \) has a basis \( B \). Since \( T \) is injective, \( T \) is one-to-one on \( B \), and \( T(B) \) is linearly independent: a finite combination \( \sum c_i T\b_i = T(\sum c_i\b_i) = \0 \) with distinct \( \b_i \) forces \( \sum c_i\b_i = \0 \) (@thm-injective-iff-trivial-kernel), hence all \( c_i = 0 \). By @thm-basis-extension-general there is a basis \( C \supseteq T(B) \) of \( W \). By @thm-linear-map-from-any-basis, there is \( \psi \in W^{*} \) with \( \psi(T\b) = \varphi(\b) \) for \( \b \in B \), and \( \psi(\c) = 0 \) for \( \c \in C \setminus T(B) \); this is well defined because each element of \( T(B) \) is \( T\b \) for exactly one \( \b \). Then \( \psi T \) and \( \varphi \) are linear and agree on the basis \( B \), so \( T'\psi = \psi T = \varphi \) by the uniqueness part of @thm-linear-map-from-any-basis. Hence \( T' \) is surjective.

(c) Here \( B = \{1, x, x^2, \dots\} \) and \( S(B) = \{x, x^2, \dots\} \), extended to a basis by adding \( 1 \). The recipe gives \( \psi(x^{k+1}) = \varphi(x^k) \) for \( k \ge 0 \) and \( \psi(1) = 0 \). Then \( (S'\psi)(x^k) = \psi(x^{k+1}) = \varphi(x^k) \), so \( S'\psi = \varphi \). The dual map \( S' \) is not injective: \( S'\varphi_0 = 0 \) by @exm-dual-map-examples (c). This matches the contrapositive of (a): \( S \) is not surjective, since \( 1 \notin \im S \), and indeed \( \varphi_0 \) is a non-zero functional vanishing on \( \im S \).
:::
