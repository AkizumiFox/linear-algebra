# The Algebra of Linear Maps

So far we have studied one linear map at a time: its kernel, its image, and the count that ties them together. But linear maps rarely come alone. The map \( p \mapsto p + p' \) is the identity plus differentiation, and rotating then projecting is one map followed by another. This section shows that linear maps can be added, scaled and composed, that these operations obey almost all the rules of arithmetic, and that an operator can be plugged into a polynomial just as a square matrix can.

## Adding and scaling linear maps

Look at three maps on \( \nR[x]_{\le 2} \) that have already appeared in this chapter or will soon:
\[
p \mapsto p + p', \qquad p \mapsto 3p', \qquad p \mapsto p' - 2p .
\]
Each is built from two simpler maps, the identity \( \id \) and differentiation \( D \), by the recipe "apply both to \( p \), then combine the outputs with the operations of the target space". The first is "\( \id + D \)", the second "\( 3D \)", the third "\( D - 2\id \)". Instead of checking linearity for each such combination separately, we would like to check it once for the recipe. The recipe itself deserves a name.

*Linear maps into the same space can be added and scaled output by output, and the results are again linear maps.*

::: {#def-space-of-linear-maps}
[The space of linear maps]

Let \( V \) and \( W \) be vector spaces over **the same field** \( F \). We write \( \cL(V, W) \) for the set of **all** linear maps \( V \to W \), and \( \cL(V) \coloneqq \cL(V, V) \) for the set of linear operators on \( V \) (@def-linear-transformation). For \( S, T \in \cL(V, W) \) and \( c \in F \), the **sum** \( S + T \) and the **scalar multiple** \( cT \) are the functions \( V \to W \) defined by
\[
(S + T)(\v) \coloneqq S\v + T\v, \qquad (cT)(\v) \coloneqq c\,(T\v) \qquad \text{for every } \v \in V .
\]
:::

As in @def-linear-transformation, we write \( T\v \) for \( T(\v) \) when no brackets are needed. In words: to evaluate \( S + T \) at \( \v \), evaluate both maps at \( \v \) and add the results **in \( W \)**; to evaluate \( cT \), evaluate \( T \) and scale the result in \( W \). The operations of \( V \) play no role in the definition. That is why \( S \) and \( T \) must have the **same codomain**: the sum \( S\v + T\v \) has to be computed in one space. Both maps must also be defined on the same \( V \).

We have used these operations before without naming them: the operations on \( F^X \) in @exm-vector-spaces (d) are defined by the same pointwise recipe, with values added in \( F \) instead of \( W \).

It turns out that the recipe never leaves the world of linear maps, and that \( \cL(V, W) \) is itself a vector space. This is the first sign that maps between vector spaces are as good as vectors.

::: {#thm-linear-maps-vector-space}
[\( \cL(V, W) \) Is a Vector Space]

Let \( V \) and \( W \) be vector spaces over \( F \). If \( S, T \in \cL(V, W) \) and \( c \in F \), then \( S + T \) and \( cT \) are linear. With the operations of @def-space-of-linear-maps, \( \cL(V, W) \) is a vector space over \( F \). Its zero vector is the zero map \( \v \mapsto \0_W \), and the negative of \( T \) is \( (-1)T \colon \v \mapsto -T\v \).
:::

::: {.idea}
There are two layers. The set \( W^V \) of **all** functions \( V \to W \), with the pointwise operations, is a vector space, for the same reason \( F^X \) is: each axiom is checked one input at a time, where it becomes an axiom of \( W \). Then \( \cL(V, W) \) sits inside \( W^V \), so the Subspace Test finishes the job, and its three conditions are exactly "the zero map is linear", "a sum of linear maps is linear" and "a multiple of a linear map is linear".
:::

::: {.proof}
Let \( W^V \) be the set of all functions \( V \to W \), with the operations of @def-space-of-linear-maps applied to arbitrary functions. The verification in @exm-vector-spaces (d) goes through word for word with \( W \) in place of \( F \): two functions \( V \to W \) are equal when they agree at every \( \v \in V \) (@def-function), and at each \( \v \) every axiom for \( W^V \) becomes the same axiom in \( W \), with zero function \( \v \mapsto \0_W \) and negative \( \v \mapsto -f(\v) \). Hence \( W^V \) is a vector space over \( F \), and \( \cL(V, W) \subseteq W^V \). We apply @thm-subspace-test.

(1) The zero map is linear: \( \0_W = \0_W + \0_W \) and \( \0_W = c\,\0_W \) by @thm-scalar-zero-vector. So \( \0 \in \cL(V, W) \).

(2) Let \( S, T \in \cL(V, W) \), \( \u, \v \in V \) and \( a \in F \). By the definition of \( S + T \), the linearity of \( S \) and \( T \), and the axioms of \( W \),
\[
(S + T)(\u + \v) = S\u + S\v + T\u + T\v = (S + T)\u + (S + T)\v,
\]
\[
(S + T)(a\v) = aS\v + aT\v = a\,(S\v + T\v) = a\,(S + T)\v .
\]
So \( S + T \in \cL(V, W) \).

(3) Let \( c \in F \) and \( T \in \cL(V, W) \). Then \( (cT)(\u + \v) = c\,(T\u + T\v) = (cT)\u + (cT)\v \), and \( (cT)(a\v) = c\,(aT\v) = (ca)T\v = (ac)T\v = a\,(cT)\v \), using the axioms of \( W \) and commutativity of multiplication in \( F \). So \( cT \in \cL(V, W) \).

By @thm-subspace-test, \( \cL(V, W) \) is a subspace of \( W^V \), hence a vector space over \( F \) with the same zero and negatives. The negative of \( T \) in \( W^V \) is \( \v \mapsto -T\v = (-1)T\v \), by @thm-negation-scalar. This proves the theorem.
:::

The step that used commutativity of \( F \) is worth a second look: \( cT \) is linear because \( c \) can be moved past the scalar \( a \). This is one place where "\( F \) is a field" is used silently.

::: {#exm-sum-of-matrix-maps}
[Sums of Matrix Maps and Other First Examples]

For \( \A \in M_{m \times n}(F) \), write \( T_\A \colon F^n \to F^m \), \( \x \mapsto \A\x \), for the matrix map of @exm-matrix-transformation.

::: {.enumerate options="label=(\alph*)"}
1. Show that \( T_\A + T_\B = T_{\A + \B} \) and \( cT_\A = T_{c\A} \) for \( \A, \B \in M_{m \times n}(F) \) and \( c \in F \).
2. Describe \( \cL(V, W) \) when \( V = \{\0\} \), and when \( W = \{\0\} \).
3. On \( \nR[x]_{\le 2} \), write \( T(p) = p' - 2p \) in terms of \( \id \) and \( D \), and compute \( T(1 + x^2) \).
:::
:::

::: {.solution}
(a) Let \( \x \in F^n \). By @def-space-of-linear-maps and distributivity (@thm-matrix-multiplication-properties),
\[
\begin{aligned}
(T_\A + T_\B)(\x) &= \A\x + \B\x = (\A + \B)\x = T_{\A + \B}(\x), \\
(cT_\A)(\x) &= c(\A\x) = (c\A)\x = T_{c\A}(\x).
\end{aligned}
\]
The maps agree at every \( \x \), so they are equal. So adding and scaling matrix maps is adding and scaling matrices.

(b) If \( V = \{\0\} \), a linear map must send \( \0 \) to \( \0_W \), so the zero map is the **only** element: \( \cL(\{\0\}, W) = \{0\} \). If \( W = \{\0\} \), every function \( V \to \{\0\} \) is the zero map, and it is linear, so again \( \cL(V, \{\0\}) = \{0\} \). These degenerate cases matter because formulas like "\( \dim \cL(V, W) = \dim V \cdot \dim W \)", which we prove later in this chapter, must give \( 0 \) here, and they do.

(c) \( T = D - 2\id \), which is linear by @thm-linear-maps-vector-space. With \( p = 1 + x^2 \), \( p' = 2x \), so \( T(p) = 2x - 2 - 2x^2 \).
:::

Here is a non-example by minimal change. Keep \( D \) on \( \nR[x]_{\le 2} \), but replace \( \id \) by the evaluation map \( E(p) = p(0) \in \nR \). Both maps are linear and both are defined on \( \nR[x]_{\le 2} \). But \( D \) lands in \( \nR[x]_{\le 2} \) and \( E \) lands in \( \nR \), so \( D + E \) would require adding a polynomial to a number. The clause that fails is "\( S, T \in \cL(V, W) \)" with the **same \( W \)**: the sum is not defined.

## Composition

Addition makes \( \cL(V, W) \) a vector space, but the operation that really matters for maps is doing one after another. For functions, Chapter 0 wrote this as \( S \circ T \) (@def-composition). For linear maps we drop the circle.

::: {.remark}
**Notation.** For \( T \in \cL(U, V) \) and \( S \in \cL(V, W) \), we write \( ST \coloneqq S \circ T \colon U \to W \), so \( (ST)\u = S(T\u) \). **The map written on the right acts first.** For an operator \( T \in \cL(V) \), \( T^2 = TT \) means "apply \( T \) twice", never "square the output".
:::

Is \( ST \) linear, and how does composition interact with the sum? It turns out that composition behaves like a multiplication: associative, with identities, and distributive over addition on both sides.

::: {#thm-composition-linear}
[Composition of Linear Maps]

Let \( U, V, W, X \) be vector spaces over \( F \).

::: {.enumerate options="label=(\alph*)"}
1. **(Linearity)** If \( T \in \cL(U, V) \) and \( S \in \cL(V, W) \), then \( ST \in \cL(U, W) \).
2. **(Associativity)** If \( T \in \cL(U, V) \), \( S \in \cL(V, W) \) and \( R \in \cL(W, X) \), then \( R(ST) = (RS)T \).
3. **(Identities)** If \( T \in \cL(U, V) \), then \( T\id_U = T = \id_V T \).
4. **(Distributivity)** If \( T, T_1, T_2 \in \cL(U, V) \), \( S, S_1, S_2 \in \cL(V, W) \) and \( c \in F \), then
\[
\begin{aligned}
(S_1 + S_2)T &= S_1T + S_2T, \\
S(T_1 + T_2) &= ST_1 + ST_2, \\
(cS)T &= c(ST) = S(cT).
\end{aligned}
\]
:::
:::

::: {.idea}
Parts (b) and (c) hold for all functions, so there is nothing new to do. Part (a) is a two-line check. The interesting point is in (d): the three identities are not equally cheap. In \( (S_1 + S_2)T \) the map \( T \) acts first and the sum is taken afterwards, so the identity is just the definition of the sum. In \( S(T_1 + T_2) \) the sum is taken **before** \( S \) acts, and pulling it out of \( S \) needs \( S \) to be linear. So we should watch where the linearity of the **left** factor is spent.
:::

::: {.proof}
(a) Let \( \u, \u' \in U \) and \( a \in F \). Since \( T \) and then \( S \) are linear,
\[
ST(\u + \u') = S(T\u + T\u') = ST\u + ST\u', \qquad ST(a\u) = S(aT\u) = a\,ST\u .
\]

(b) and (c) hold for arbitrary functions, by @thm-composition-associative and the observation after @def-identity-function.

(d) Each side is a function \( U \to W \), so we compare values at \( \u \in U \). By @def-space-of-linear-maps,
\[
(S_1 + S_2)T\u = S_1(T\u) + S_2(T\u) = (S_1T + S_2T)\u,
\]
with no linearity used. Next, since \( S \) is linear,
\[
S(T_1 + T_2)\u = S(T_1\u + T_2\u) = ST_1\u + ST_2\u = (ST_1 + ST_2)\u .
\]
Finally \( (cS)(T\u) = c\,(ST\u) \) by definition, and \( S(cT\u) = c\,(ST\u) \) because \( S \) is linear. This proves the theorem.
:::

In short, \( \cL(V) \) carries a vector space structure and a multiplication (composition) that is associative, has the unit \( \id_V \), distributes over addition, and lets scalars move freely through products. A vector space with such a multiplication is called an **algebra** over \( F \); \( M_n(F) \) is the other algebra we know (@thm-matrix-multiplication-properties). The two will turn out to be the same algebra in disguise when we write operators as matrices later in this chapter.

::: {#exm-rotation-projection-dont-commute}
[Rotate, Then Project]

Let \( R \colon \nR^2 \to \nR^2 \) be the rotation by \( 90^\circ \) counterclockwise, \( R(x, y) = (-y, x) \), and let \( P \colon \nR^2 \to \nR^2 \), \( P(x, y) = (x, 0) \), be the projection onto the \( x \)-axis. Compute \( PR \) and \( RP \).
:::

::: {.solution}
In \( PR \) the rotation acts first:
\[
PR(x, y) = P(-y, x) = (-y, 0), \qquad RP(x, y) = R(x, 0) = (0, x).
\]
At \( (1, 0) \): \( PR(1, 0) = (0, 0) \), while \( RP(1, 0) = (0, 1) \). So \( PR \neq RP \). Geometrically, \( PR \) rotates \( \e_1 \) onto the \( y \)-axis and then squashes it to \( \0 \); \( RP \) leaves \( \e_1 \) alone under the projection and then rotates it to \( \e_2 \). In matrix form, \( P = T_{\A} \) and \( R = T_{\B} \) with \( \A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \) and \( \B = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \), and indeed \( \A\B = \begin{pmatrix} 0 & -1 \\ 0 & 0 \end{pmatrix} \neq \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} = \B\A \).
:::

::: {.warning}
**Composition is not commutative, and the order is read right to left.** In @exm-rotation-projection-dont-commute, \( PR \neq RP \). It can be worse: for \( T \in \cL(\nR^2, \nR^3) \) and \( S \in \cL(\nR^3, \nR^2) \), both \( ST \in \cL(\nR^2) \) and \( TS \in \cL(\nR^3) \) are defined, but they live on different spaces, so they cannot even be compared. And for \( T \in \cL(\nR^2, \nR^3) \), \( S \in \cL(\nR^3, \nR^4) \), \( ST \) is defined but \( TS \) is not. The thing you do first goes on the **right**.
:::

::: {.check}
Let \( T \colon \nR^3 \to \nR^2 \) and \( S \colon \nR^2 \to \nR^4 \) be linear. Which of \( ST \) and \( TS \) is defined, and between which spaces does it go?
:::

::: {.solution}
\( ST = S \circ T \) first applies \( T \colon \nR^3 \to \nR^2 \), then \( S \colon \nR^2 \to \nR^4 \), so \( ST \in \cL(\nR^3, \nR^4) \). \( TS \) would apply \( S \) first, landing in \( \nR^4 \), where \( T \) is not defined; so \( TS \) is not defined.
:::

Because of the missing commutativity, school identities about products must be rechecked. By distributivity (@thm-composition-linear (d)),
\[
(S + T)^2 = (S + T)(S + T) = S^2 + ST + TS + T^2,
\]
which equals \( S^2 + 2ST + T^2 \) only if \( ST = TS \). With \( P \) and \( R \) as above, \( PR + RP \colon (x, y) \mapsto (-y, x) \), while \( 2PR \colon (x, y) \mapsto (-2y, 0) \); so \( (P + R)^2 \neq P^2 + 2PR + R^2 \). This is the operator version of the matrix warning in Chapter 0, §9.

## Operators, powers and polynomials

Composition of operators on one space \( V \) never leaves \( \cL(V) \), so we may compose an operator with itself as often as we like. Repeated composition leads to powers, and combinations of powers to polynomials, exactly as for square matrices (@def-polynomial-of-matrix).

::: {#def-polynomial-of-operator}
[Powers and Polynomials of an Operator]

Let \( V \) be a vector space over \( F \) and \( T \in \cL(V) \). The **powers** of \( T \) are defined recursively by
\[
T^0 \coloneqq \id_V, \qquad T^{k+1} \coloneqq T^k T \quad (k \in \nN).
\]
For \( p = a_0 + a_1x + \dots + a_Nx^N \in F[x] \), the operator \( p(T) \in \cL(V) \) is
\[
p(T) \coloneqq a_0\id_V + a_1T + a_2T^2 + \dots + a_NT^N .
\]
:::

In words: \( T^k \) applies \( T \) exactly \( k \) times, and \( T^0 \) does nothing. In \( p(T) \), the **constant term becomes \( a_0\id_V \)**, because an operator cannot be added to a scalar. Each \( T^k \) is linear by @thm-composition-linear (a) and induction, and \( p(T) \) is linear by @thm-linear-maps-vector-space. As for matrices, \( p(T) \) does not depend on how many zero coefficients we write, since \( 0 \cdot T^k \) is the zero map.

Plugging in an operator respects sums and products of polynomials, just as plugging in a matrix does.

::: {#thm-polynomial-of-operator-properties}
[Polynomials in One Operator]

Let \( T \in \cL(V) \) and \( p, q \in F[x] \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( T^jT^k = T^{j+k} \) for all \( j, k \in \nN \);
2. \( (p + q)(T) = p(T) + q(T) \) and \( (pq)(T) = p(T)\,q(T) \);
3. \( p(T)\,q(T) = q(T)\,p(T) \).
:::
:::

::: {.idea}
The proof of @thm-polynomial-of-matrix-properties used four matrix rules: associativity, identity, distributivity and "scalars move through products". @thm-composition-linear supplies exactly these four rules for operators. So the old proof transfers line by line. Part (c) is the surprise: \( T \) need not commute with other operators, but it commutes with every polynomial in itself.
:::

::: {.proof}
(a) Fix \( j \) and use induction on \( k \) (@thm-induction). For \( k = 0 \), \( T^jT^0 = T^j\id_V = T^j \) by @thm-composition-linear (c). If \( T^jT^k = T^{j+k} \), then by @def-polynomial-of-operator and associativity (@thm-composition-linear (b)),
\[
T^jT^{k+1} = T^j(T^kT) = (T^jT^k)T = T^{j+k}T = T^{j+k+1} .
\]

(b) Let \( p = \sum_{i=0}^{m} a_ix^i \) and \( q = \sum_{j=0}^{l} b_jx^j \). The statement for sums holds because \( (a_i + b_i)T^i = a_iT^i + b_iT^i \) in the vector space \( \cL(V) \) (@thm-linear-maps-vector-space). For products, the coefficient of \( x^k \) in \( pq \) is \( \sum_{i+j=k} a_ib_j \) (@def-polynomial-ring), so
\[
\begin{aligned}
(pq)(T) &= \sum_k \Bigl( \sum_{i+j=k} a_ib_j \Bigr) T^k = \sum_{i=0}^{m} \sum_{j=0}^{l} (a_ib_j)\,T^iT^j \\
&= \Bigl( \sum_{i=0}^{m} a_iT^i \Bigr)\Bigl( \sum_{j=0}^{l} b_jT^j \Bigr) = p(T)\,q(T),
\end{aligned}
\]
where the second equality uses (a), and the third uses both distributive laws and \( (a_iT^i)(b_jT^j) = (a_ib_j)\,T^iT^j \), all from @thm-composition-linear (d).

(c) Since \( pq = qp \) in \( F[x] \) (@thm-polynomial-ring-laws), part (b) gives \( p(T)q(T) = (pq)(T) = (qp)(T) = q(T)p(T) \). This proves the theorem.
:::

In practice, (b) says that **a factorization of \( p \) is a factorization of \( p(T) \)**: for instance \( T^2 - 3T + 2\id_V = (T - \id_V)(T - 2\id_V) = (T - 2\id_V)(T - \id_V) \).

::: {#exm-differentiation-nilpotent}
[Differentiation Is Nilpotent]

Let \( n \ge 0 \) and let \( D \in \cL(F[x]_{\le n}) \) be (formal) differentiation (@exm-differentiation), \( D(a_0 + a_1x + \dots + a_nx^n) = a_1 + 2a_2x + \dots + na_nx^{n-1} \), where \( ka_k \) means \( a_k \) added to itself \( k \) times. Show that \( D^{n+1} = 0 \). Show also that \( D^n \neq 0 \) when \( F = \nR \).
:::

::: {.solution}
For \( 0 \le k \le n \), \( D(x^k) = kx^{k-1} \) if \( k \ge 1 \) and \( D(1) = 0 \). So \( D \) sends each \( x^k \) to a scalar multiple of \( x^{k-1} \), or to \( 0 \) when \( k = 0 \). Applying this \( k + 1 \) times, \( D^{k+1}(x^k) \) is a scalar multiple of \( D(1) = 0 \), so \( D^{k+1}(x^k) = 0 \). Since \( k \le n \), also \( D^{n+1}(x^k) = D^{n-k}\bigl(D^{k+1}(x^k)\bigr) = D^{n-k}(\0) = \0 \), by @thm-polynomial-of-operator-properties (a).

Now let \( p = a_0 + a_1x + \dots + a_nx^n \). Since \( D^{n+1} \) is linear, @thm-linear-combination gives
\[
D^{n+1}(p) = a_0D^{n+1}(1) + a_1D^{n+1}(x) + \dots + a_nD^{n+1}(x^n) = \0 .
\]
Hence \( D^{n+1} = 0 \).

Over \( \nR \), \( D^n(x^n) = n(n-1) \cdots 1 = n! \neq 0 \), so \( D^n \neq 0 \). Over \( \nF_2 \) with \( n = 2 \), however, \( D(x^2) = 2x = 0 \), and \( D^2 = 0 \) already; the field matters for the exact power, but never for \( D^{n+1} = 0 \).
:::

An operator \( T \) with \( T^k = 0 \) for some \( k \ge 1 \) is called **nilpotent**. The example shows that a non-zero operator can have a power equal to zero, just as the matrix \( \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) can. Differentiation is the model nilpotent operator, and it returns when we study canonical forms.

::: {#exm-operator-polynomial-relations}
[Operators That Satisfy a Polynomial]

With \( P \) and \( R \) as in @exm-rotation-projection-dont-commute, find non-zero polynomials \( p \) and \( q \) with \( p(P) = 0 \) and \( q(R) = 0 \). Also, for an arbitrary \( p \in F[x] \), compute \( p(\id_V) \) and \( p(Z) \), where \( Z \in \cL(V) \) is the zero operator.
:::

::: {.solution}
For the projection, \( P^2(x, y) = P(x, 0) = (x, 0) = P(x, y) \), so \( P^2 = P \) and \( p = x^2 - x \) satisfies \( p(P) = P^2 - P = 0 \). By @thm-polynomial-of-operator-properties (b), this says \( P(P - \id) = 0 \): whatever \( P - \id \) produces is killed by \( P \), and indeed \( (P - \id)(x, y) = (0, -y) \) lies on the \( y \)-axis.

For the rotation, \( R^2(x, y) = R(-y, x) = (-x, -y) \), so \( R^2 = -\id \), and \( q = x^2 + 1 \) satisfies \( q(R) = R^2 + \id = 0 \). Rotating twice by \( 90^\circ \) is rotating by \( 180^\circ \). Since \( q \) has no real roots, \( q \) has no real linear factor, so the trick "factor \( q \), then factor \( q(R) \)" gives nothing over \( \nR \).

For \( p = a_0 + a_1x + \dots + a_Nx^N \): every power of \( \id_V \) is \( \id_V \), so \( p(\id_V) = (a_0 + a_1 + \dots + a_N)\id_V = p(1)\,\id_V \). Every power \( Z^k \) with \( k \ge 1 \) is the zero map, but \( Z^0 = \id_V \), so \( p(Z) = a_0\id_V \), the scalar \( p(0) \) times \( \id_V \). The second computation is the reason for the convention \( T^0 = \id_V \): with it, "the constant term" of \( p(T) \) is what survives when \( T \) is the zero operator.
:::

::: {.warning}
**The constant term is \( a_0\id_V \), not \( a_0 \).** Writing "\( P^2 - P + 3 \)" for an operator is a type error: \( P^2 - P \) is a map and \( 3 \) is a number. For \( p = x^2 - x + 3 \), \( p(P) = P^2 - P + 3\id \), which is \( 3\id \) since \( P^2 = P \). Forgetting the \( \id \) leads to "\( p(P) = 3 \)", which is not an operator at all.
:::

::: {.check}
With \( P \) the projection above, compute \( p(P) \) for \( p = x^3 - 2x + 1 \).
:::

::: {.solution}
Since \( P^2 = P \), also \( P^3 = P^2P = PP = P \). So \( p(P) = P^3 - 2P + \id = P - 2P + \id = \id - P \), which is the map \( (x, y) \mapsto (0, y) \): the projection onto the \( y \)-axis.
:::

Polynomial relations such as \( P^2 = P \), \( R^2 = -\id \) and \( D^{n+1} = 0 \) carry real information about an operator. In the next section we use one to write down an inverse without solving any equations, and later in the book the polynomials that kill an operator lead to the minimal polynomial and to canonical forms.

## Exercises

### A. Check your understanding

::: {#exr-algebra-of-linear-maps-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. For \( S, T \in \cL(V, W) \) and \( c \in F \), define \( S + T \) and \( cT \). Why must \( S \) and \( T \) have the same codomain?
2. True or false: for all \( S, T \in \cL(V) \), \( ST = TS \). Justify your answer.
3. Let \( T \in \cL(\nR^5, \nR^2) \) and \( S \in \cL(\nR^2, \nR^5) \). Which of \( ST \), \( TS \) are defined, and in which spaces do they lie?
4. For \( T \in \cL(V) \) and \( p = 4 \) (a constant polynomial), what is \( p(T) \)?
5. True or false: for all \( S, T \in \cL(V) \), \( (S + T)^2 = S^2 + 2ST + T^2 \). Justify your answer.
:::
:::

::: {.solution}
(a) \( (S + T)(\v) = S\v + T\v \) and \( (cT)(\v) = c\,T\v \) for every \( \v \in V \) (@def-space-of-linear-maps). The sum \( S\v + T\v \) must be computed in a single vector space, so both values must lie in the same \( W \).

(b) False. In @exm-rotation-projection-dont-commute, \( PR(1, 0) = (0, 0) \) but \( RP(1, 0) = (0, 1) \).

(c) Both are defined. \( ST \) applies \( T \) first: \( ST \in \cL(\nR^5) \). \( TS \) applies \( S \) first: \( TS \in \cL(\nR^2) \).

(d) \( p(T) = 4\id_V \), by @def-polynomial-of-operator.

(e) False. By @thm-composition-linear (d), \( (S + T)^2 = S^2 + ST + TS + T^2 \), which differs from \( S^2 + 2ST + T^2 \) by \( TS - ST \). With \( S = P \), \( T = R \) of @exm-rotation-projection-dont-commute, \( RP - PR \colon (x, y) \mapsto (y, x) \) is not the zero map, so the identity fails.
:::

### B. Practice

::: {#exr-algebra-of-linear-maps-b1}
[B1: Computing compositions]

Let \( S, T \in \cL(\nR^2) \) be given by \( S(x, y) = (x + y, \, y) \) and \( T(x, y) = (y, \, x) \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( ST \), \( TS \) and \( 2S - T \).
2. Compute \( S^2 \) and \( S^k \) for every \( k \in \nN \).
3. Hence show that \( (S - \id)^2 = 0 \).
:::
:::

::: {.solution}
(a) Applying the right-hand map first,
\[
ST(x, y) = S(y, x) = (x + y, \, x), \qquad TS(x, y) = T(x + y, \, y) = (y, \, x + y).
\]
So \( ST \neq TS \); for instance \( ST(1, 0) = (1, 1) \) and \( TS(1, 0) = (0, 1) \). By @def-space-of-linear-maps, \( (2S - T)(x, y) = (2x + 2y, \, 2y) - (y, \, x) = (2x + y, \, 2y - x) \).

(b) \( S^2(x, y) = S(x + y, \, y) = (x + 2y, \, y) \). We claim \( S^k(x, y) = (x + ky, \, y) \) for all \( k \in \nN \), by induction on \( k \). For \( k = 0 \), \( S^0 = \id \) sends \( (x, y) \) to \( (x + 0y, \, y) \). If the claim holds for \( k \), then
\[
S^{k+1}(x, y) = S^k\bigl(S(x, y)\bigr) = S^k(x + y, \, y) = (x + y + ky, \, y) = (x + (k + 1)y, \, y),
\]
where the first equality is @def-polynomial-of-operator, \( S^{k+1} = S^kS \).

(c) \( (S - \id)(x, y) = (y, \, 0) \), so \( (S - \id)^2(x, y) = (S - \id)(y, 0) = (0, 0) \). Hence \( (S - \id)^2 = 0 \), that is, \( S - \id \) is nilpotent. Expanding with @thm-polynomial-of-operator-properties (b), \( S^2 - 2S + \id = 0 \), which matches (b): \( (x + 2y, y) - 2(x + y, y) + (x, y) = (0, 0) \).
:::

::: {#exr-algebra-of-linear-maps-b2}
[B2: Operators that preserve a subspace]

Let \( U \) be a subspace of \( V \), and let
\[
\mathcal{A}_U \coloneqq \{ T \in \cL(V) : T\u \in U \text{ for every } \u \in U \} .
\]
Prove that \( \mathcal{A}_U \) is a subspace of \( \cL(V) \), that \( \id_V \in \mathcal{A}_U \), and that \( ST \in \mathcal{A}_U \) whenever \( S, T \in \mathcal{A}_U \).
:::

::: {.solution}
We use @thm-subspace-test in the vector space \( \cL(V) \) (@thm-linear-maps-vector-space).

(1) The zero map sends every \( \u \in U \) to \( \0 \), and \( \0 \in U \) because \( U \) is a subspace. So \( 0 \in \mathcal{A}_U \).

(2) Let \( S, T \in \mathcal{A}_U \) and \( \u \in U \). Then \( S\u \in U \) and \( T\u \in U \), so \( (S + T)\u = S\u + T\u \in U \), since \( U \) is closed under addition. Therefore \( S + T \in \mathcal{A}_U \).

(3) Let \( c \in F \) and \( T \in \mathcal{A}_U \). For \( \u \in U \), \( (cT)\u = c\,T\u \in U \), since \( U \) is closed under scalar multiplication. Therefore \( cT \in \mathcal{A}_U \).

Hence \( \mathcal{A}_U \) is a subspace of \( \cL(V) \). Next, \( \id_V\u = \u \in U \) for every \( \u \in U \), so \( \id_V \in \mathcal{A}_U \). Finally let \( S, T \in \mathcal{A}_U \) and \( \u \in U \). Then \( T\u \in U \), and applying the hypothesis on \( S \) to the vector \( T\u \in U \) gives \( ST\u = S(T\u) \in U \). This shows \( ST \in \mathcal{A}_U \).
:::

::: {#exr-algebra-of-linear-maps-b3}
[B3: A polynomial that kills \( D \)]

Let \( D \in \cL(\nR[x]_{\le 2}) \) be differentiation.

::: {.enumerate options="label=(\alph*)"}
1. Find a non-zero polynomial \( p \) with \( p(D) = 0 \).
2. Show that no non-zero polynomial \( q \) of degree at most \( 2 \) satisfies \( q(D) = 0 \).
3. Hence, or otherwise, compute \( (\id + D)^3 \) as a combination of \( \id, D, D^2 \), and evaluate \( (\id + D)^3(x^2) \).
:::
:::

::: {.solution}
(a) By @exm-differentiation-nilpotent with \( n = 2 \), \( D^3 = 0 \). So \( p = x^3 \) works.

(b) Let \( q = a + bx + cx^2 \) with \( q(D) = a\id + bD + cD^2 = 0 \). Applying this operator to \( x^2 \), with \( D(x^2) = 2x \) and \( D^2(x^2) = 2 \),
\[
0 = ax^2 + 2bx + 2c .
\]
A polynomial is zero exactly when all its coefficients are, so \( a = 0 \), \( 2b = 0 \) and \( 2c = 0 \). Hence \( a = b = c = 0 \) and \( q = 0 \).

(c) The operator \( \id + D \) is \( q(D) \) for \( q = 1 + x \). Applying the product rule of @thm-polynomial-of-operator-properties (b) twice, \( (\id + D)^3 = q(D)q(D)q(D) = (q^3)(D) \), and \( q^3 = 1 + 3x + 3x^2 + x^3 \). So
\[
(\id + D)^3 = \id + 3D + 3D^2 + D^3 = \id + 3D + 3D^2,
\]
using \( D^3 = 0 \) from (a). Therefore \( (\id + D)^3(x^2) = x^2 + 3 \cdot 2x + 3 \cdot 2 = x^2 + 6x + 6 \).
:::

### C. Going deeper

::: {#exr-algebra-of-linear-maps-c1}
[C1: The Heisenberg relation]

Let \( F \) be a field, let \( D \in \cL(F[x]) \) be formal differentiation, \( D(\sum_k a_kx^k) = \sum_{k \ge 1} ka_kx^{k-1} \) (@exm-differentiation), and let \( S \in \cL(F[x]) \) be multiplication by \( x \), \( S(p) = xp \) (the map \( M \) of @exm-multiplication-by-x).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( DS - SD = \id \).
2. Let \( T \in \cL(F^n, F^m) \). Prove that \( T = T_\A \), where \( \A \in M_{m \times n}(F) \) is the matrix with columns \( T\e_1, \dots, T\e_n \).
3. Now suppose that \( F \) has **characteristic \( 0 \)** (@def-characteristic), and let \( n \ge 1 \). Deduce that there are no operators \( D', S' \in \cL(F^n) \) with \( D'S' - S'D' = \id \).
4. Show that the assumption on the characteristic in (c) cannot be dropped.
:::

*Hint: for (c), use (b) and consider traces.*
:::

::: {.solution}
(a) Both sides are linear (@thm-linear-maps-vector-space, @thm-composition-linear). We first compare them on \( x^k \), \( k \in \nN \). We have \( DS(x^k) = D(x^{k+1}) = (k + 1)x^k \). If \( k \ge 1 \), \( SD(x^k) = x \cdot kx^{k-1} = kx^k \); if \( k = 0 \), \( SD(1) = x \cdot 0 = 0 = 0 \cdot x^0 \). In both cases
\[
(DS - SD)(x^k) = (k + 1)x^k - kx^k = x^k = \id(x^k).
\]
Every \( p \in F[x] \) is a finite combination \( p = \sum_k a_kx^k \), so by @thm-linear-combination, \( (DS - SD)(p) = \sum_k a_k(DS - SD)(x^k) = \sum_k a_kx^k = p \). Hence \( DS - SD = \id \).

(b) Let \( \x = (x_1, \dots, x_n) = x_1\e_1 + \dots + x_n\e_n \in F^n \). By @thm-linear-combination and @thm-matrix-times-vector-columns,
\[
T\x = x_1T\e_1 + \dots + x_nT\e_n = \A\x = T_\A(\x).
\]
Since \( \x \) was arbitrary, \( T = T_\A \).

(c) Suppose, for a contradiction, that \( D', S' \in \cL(F^n) \) satisfy \( D'S' - S'D' = \id \). By (b), \( D' = T_\A \) and \( S' = T_\B \) for some \( \A, \B \in M_n(F) \), and \( \id = T_{\I_n} \). By associativity of matrix multiplication, \( T_\A T_\B(\x) = \A(\B\x) = (\A\B)\x \), so \( T_\A T_\B = T_{\A\B} \), and similarly \( T_\B T_\A = T_{\B\A} \). With @exm-sum-of-matrix-maps (a),
\[
T_{\A\B - \B\A} = T_\A T_\B - T_\B T_\A = \id = T_{\I_n} .
\]
Evaluating at \( \e_j \) gives equal \( j \)-th columns (@thm-matrix-times-vector-columns), so \( \A\B - \B\A = \I_n \). Taking traces and using @thm-trace-properties,
\[
n \cdot 1 = \tr \I_n = \tr(\A\B) - \tr(\B\A) = 0 .
\]
Since \( n \ge 1 \) and \( F \) has characteristic \( 0 \), \( n \cdot 1 \neq 0 \) by @def-characteristic. This is a contradiction, so no such \( D', S' \) exist. In words: over \( \nQ \), \( \nR \), \( \nC \) or any field of characteristic \( 0 \), the relation \( DS - SD = \id \) of (a) has no analogue on \( F^n \), \( n \ge 1 \). Since every \( n \)-dimensional space is isomorphic to \( F^n \), as we show in the next section, the same holds on every non-zero finite-dimensional space. (On the zero space \( \id = 0 \), so the relation holds trivially there; that is why \( n \ge 1 \).)

(d) Over \( \nF_2 \) (characteristic \( 2 \)), take \( \A = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \) and \( \B = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) as in @exr-matrices-c1. There \( \A\B - \B\A = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix} = \I_2 \), because \( -1 = 1 \) in \( \nF_2 \). By the computation in (c), \( D' = T_\A \) and \( S' = T_\B \) satisfy \( D'S' - S'D' = T_{\A\B - \B\A} = \id \) on \( \nF_2^2 \). So the conclusion of (c) fails without the characteristic assumption; the proof breaks exactly at \( n \cdot 1 \neq 0 \), since \( 2 \cdot 1 = 0 \) in \( \nF_2 \).
:::

::: {#exr-algebra-of-linear-maps-c2}
[C2: Commuting nilpotent operators]

Let \( S, T \in \cL(V) \).

::: {.enumerate options="label=(\alph*)"}
1. Suppose \( ST = TS \). Prove that \( (S + T)^n = \sum_{k=0}^{n} \binom{n}{k} S^kT^{n-k} \) for every \( n \in \nN \), where \( \binom{n}{k} S^kT^{n-k} \) means \( S^kT^{n-k} \) added to itself \( \binom{n}{k} \) times.
2. Deduce that if \( ST = TS \), \( S^a = 0 \) and \( T^b = 0 \) for some \( a, b \ge 1 \), then \( (S + T)^{a+b-1} = 0 \).
3. Show that (b) fails without \( ST = TS \): give nilpotent \( S, T \in \cL(\nR^2) \) such that \( S + T \) is not nilpotent.
:::

*Hint: for (c), try maps that send one standard basis vector to the other and the other to \( \0 \).*
:::

::: {.solution}
(a) First, \( T^jS = ST^j \) for all \( j \in \nN \), by induction on \( j \): it holds for \( j = 0 \), and if \( T^jS = ST^j \), then \( T^{j+1}S = T^j(TS) = T^j(ST) = (T^jS)T = (ST^j)T = ST^{j+1} \), using associativity (@thm-composition-linear (b)) and @thm-polynomial-of-operator-properties (a) in the form \( T^{j+1} = T^jT \).

Now induct on \( n \). For \( n = 0 \) both sides are \( \id_V \). Suppose the formula holds for \( n \). By @thm-composition-linear (d),
\[
(S + T)^{n+1} = (S + T)^n(S + T) = \sum_{k=0}^{n} \binom{n}{k} S^kT^{n-k}S + \sum_{k=0}^{n} \binom{n}{k} S^kT^{n-k+1} .
\]
By the first paragraph, \( S^kT^{n-k}S = S^k(T^{n-k}S) = S^kST^{n-k} = S^{k+1}T^{n-k} \). Shifting the index in the first sum, the coefficient of \( S^kT^{n+1-k} \) becomes \( \binom{n}{k-1} + \binom{n}{k} = \binom{n+1}{k} \) (Pascal's rule, with \( \binom{n}{-1} = \binom{n}{n+1} = 0 \)). This is the formula for \( n + 1 \).

(b) By (a) with \( n = a + b - 1 \), \( (S + T)^{a+b-1} \) is a sum of multiples of \( S^kT^{a+b-1-k} \), \( 0 \le k \le a + b - 1 \). If \( k \ge a \), then \( S^k = S^{k-a}S^a = 0 \) by @thm-polynomial-of-operator-properties (a), so the term is \( 0 \) by @thm-composition-linear (d). If \( k \le a - 1 \), then \( a + b - 1 - k \ge b \), so \( T^{a+b-1-k} = 0 \) likewise. Every term vanishes, so \( (S + T)^{a+b-1} = 0 \).

(c) Let \( S(x, y) = (y, 0) \) and \( T(x, y) = (0, x) \). Then \( S^2(x, y) = S(y, 0) = (0, 0) \) and \( T^2(x, y) = T(0, x) = (0, 0) \), so both are nilpotent. But \( (S + T)(x, y) = (y, x) \), so \( (S + T)^2(x, y) = (x, y) \), that is, \( (S + T)^2 = \id \). Then \( (S + T)^{2k} = \id \neq 0 \) and \( (S + T)^{2k+1} = S + T \neq 0 \) for every \( k \), so \( S + T \) is not nilpotent. Here \( ST(x, y) = (x, 0) \neq (0, y) = TS(x, y) \), so the hypothesis of (b) indeed fails.
:::
