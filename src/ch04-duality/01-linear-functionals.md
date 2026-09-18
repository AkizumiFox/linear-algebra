# Linear Functionals and the Dual Space

Chapter 3 studied linear maps \( V \to W \) into arbitrary targets. The smallest non-zero target is the field \( F \) itself, and maps into it are everywhere: a coordinate, the value of a polynomial at a point, an integral, the trace. This section names these maps and shows that they form a vector space \( V^{*} \), of the same dimension as \( V \) when \( V \) is finite-dimensional. It also proves the fact that makes them useful: every non-zero vector is detected by at least one of them.

## Measuring a vector by a number

After studying vector spaces and the maps between them, we look at the simplest possible target. Here are four maps we have already met, from four different families.

- **A coordinate.** Fix a basis \( \sB = (\v_1, \dots, \v_n) \) of \( V \). The map \( V \to F \) sending \( \v \) to the first entry of \( \coord{\v}{\sB} \) respects sums and multiples, by @thm-coordinates-linear.
- **Evaluation.** The map \( F[x] \to F \), \( p \mapsto p(3) \), satisfies \( (p + q)(3) = p(3) + q(3) \) and \( (cp)(3) = c\,p(3) \), by @thm-evaluation-respects-operations (a constant \( c \) is a polynomial with value \( c \)).
- **Integration.** The map \( \nR[x] \to \nR \), \( p \mapsto \int_0^1 p(t)\,\dd t \), is linear by the linearity of the integral from calculus.
- **Trace.** The map \( \tr \colon M_n(F) \to F \) is linear (@exm-trace-matrices).

The inputs are columns, polynomials and matrices. The outputs are always single scalars. Each map is a way of **measuring** a vector by one number, and each measurement respects sums and scalar multiples. The same expression keeps recurring, "a linear map whose target is \( F \)", and we will see that these maps form a space with a structure of its own. So we give them a name.

*A linear functional is a linear measurement: it assigns a scalar to each vector, and the measurement of a linear combination is the same combination of the measurements.*

::: {#def-linear-functional}
[Linear Functional]

Let \( V \) be a vector space over \( F \), and regard \( F \) as a vector space over itself. A **linear functional** on \( V \) is a linear map \( \varphi \colon V \to F \). That is, **for all** \( \u, \v \in V \) and **all** \( c \in F \),
\[
\varphi(\u + \v) = \varphi(\u) + \varphi(\v), \qquad \varphi(c\v) = c\,\varphi(\v).
\]
:::

::: {#def-dual-space}
[Dual Space]

Let \( V \) be a vector space over \( F \). The **dual space** of \( V \) is the set of **all** linear functionals on \( V \),
\[
V^{*} \coloneqq \cL(V, F),
\]
with the pointwise operations \( (\varphi + \psi)(\v) \coloneqq \varphi(\v) + \psi(\v) \) and \( (c\varphi)(\v) \coloneqq c\,\varphi(\v) \) for \( \varphi, \psi \in V^{*} \), \( c \in F \) and \( \v \in V \).
:::

In words: a linear functional is a linear map (@def-linear-transformation) whose codomain is the one-dimensional space \( F \). Its values lie in the **same** field \( F \) over which \( V \) is a vector space. The first condition says that measuring a sum gives the sum of the measurements, and the second says that scaling a vector scales its measurement. The dual space collects **every** such measurement, and it adds them the natural way: the measurement \( \varphi + \psi \) reports the sum of the two readings. We write functionals with Greek letters \( \varphi, \psi \), which keeps them apart from vectors of \( V \).

**Well-definedness.** Two things need checking: that \( \varphi + \psi \) and \( c\varphi \) are again linear, and that the vector space axioms hold. Both are the case \( W = F \) of @thm-linear-maps-vector-space. So \( V^{*} \) is a vector space over \( F \). Its zero vector is the **zero functional** \( \v \mapsto 0 \), and the negative of \( \varphi \) is \( \v \mapsto -\varphi(\v) \). Note that \( V^{*} \) is a set of **functions on** \( V \), not a subset of \( V \).

:::: {#exm-linear-functionals}
[Four Families of Functionals]

Show that each map is a linear functional.

::: {.enumerate options="label=(\alph*)"}
1. \( \varepsilon_c \colon F[x] \to F \), \( p \mapsto p(c) \), for a fixed \( c \in F \) (**evaluation at \( c \)**).
2. \( \iota \colon \nR[x]_{\le 2} \to \nR \), \( p \mapsto \int_0^1 p(t)\,\dd t \).
3. \( \tr \colon M_n(F) \to F \).
4. The zero functional on any \( V \). Also find the dual space of the zero space \( \{\0\} \).
:::
::::

::: {.solution}
(a) By @thm-evaluation-respects-operations, \( (p + q)(c) = p(c) + q(c) \), and, regarding \( ap \) as the product of the constant polynomial \( a \) with \( p \), \( (ap)(c) = a(c)\,p(c) = a\,p(c) \), because the constant polynomial \( a \) has value \( a \) at \( c \). These are the two conditions of @def-linear-functional.

(b) By linearity of the integral, \( \int_0^1 (p + q) = \int_0^1 p + \int_0^1 q \) and \( \int_0^1 ap = a\int_0^1 p \). On coefficients, \( \iota(a_0 + a_1x + a_2x^2) = a_0 + \frac{a_1}{2} + \frac{a_2}{3} \).

(c) This is @thm-trace-properties (1): \( \tr(\A + \B) = \tr \A + \tr \B \) and \( \tr(c\A) = c\tr \A \).

(d) \( 0 = 0 + 0 \) and \( 0 = c \cdot 0 \) in \( F \), so the zero functional is linear. On \( \{\0\} \), a linear functional must send \( \0 \) to \( 0 \) (@thm-zero-maps-to-zero), and there is only one vector. So the zero functional is the only element, and \( \{\0\}^{*} = \{0\} \). This degenerate case matters: it is the case \( n = 0 \) of the count \( \dim V^{*} = \dim V \) proved below.
:::

The family \( F^n \) can be described completely. A row vector times a column is a scalar, and every functional on \( F^n \) arises this way.

::: {#thm-functionals-on-fn}
[Functionals on \( F^n \) Are Row Vectors]

For \( \a = (a_1, \dots, a_n) \in F^n \), define \( \varphi_{\a} \colon F^n \to F \) by
\[
\varphi_{\a}(\x) \coloneqq \a\tp\x = a_1x_1 + \dots + a_nx_n .
\]
Then \( \varphi_{\a} \in (F^n)^{*} \). Every \( \varphi \in (F^n)^{*} \) equals \( \varphi_{\a} \) for **exactly one** \( \a \), namely \( \a = (\varphi(\e_1), \dots, \varphi(\e_n)) \). The map \( F^n \to (F^n)^{*} \), \( \a \mapsto \varphi_{\a} \), is an isomorphism.
:::

::: {.proof}
The map \( \varphi_{\a} \) is \( T_{\a\tp} \) for the \( 1 \times n \) matrix \( \a\tp \), with a \( 1 \times 1 \) matrix read as a scalar, so it is linear by @exm-matrix-transformation. Let \( \varphi \in (F^n)^{*} \) and put \( a_i \coloneqq \varphi(\e_i) \). Then \( \varphi_{\a}(\e_i) = a_i = \varphi(\e_i) \) for each \( i \). Two linear maps that agree on the basis \( (\e_1, \dots, \e_n) \) are equal by the uniqueness part of @thm-linear-transform-basis, so \( \varphi = \varphi_{\a} \). If \( \varphi_{\a} = \varphi_{\b} \), then \( a_i = \varphi_{\a}(\e_i) = \varphi_{\b}(\e_i) = b_i \) for every \( i \), so \( \a = \b \).

Hence \( \a \mapsto \varphi_{\a} \) is a bijection \( F^n \to (F^n)^{*} \). It is linear, since \( \varphi_{\a + c\b}(\x) = \sum_i (a_i + cb_i)x_i = \varphi_{\a}(\x) + c\,\varphi_{\b}(\x) \) for every \( \x \). By @thm-inverse-is-linear it is an isomorphism.
:::

So in \( F^n \) a functional **is** a row vector acting by matrix multiplication, and its \( 1 \times n \) matrix in the standard bases is \( \bigl(\varphi(\e_1) \ \cdots \ \varphi(\e_n)\bigr) \). This is how we compute with functionals: rows act on columns.

**Non-examples by minimal change.** Each of the following changes one of the examples slightly. In each case something still works, and we name a condition that fails.

- On \( \nR^2 \), the length \( (x, y) \mapsto \sqrt{x^2 + y^2} \) (@exm-norm). It sends \( \0 \) to \( 0 \) and respects **positive** scalars. But with \( c = -1 \) and \( \v = (1, 0) \) it gives \( 1 \), not \( -1 \), so the scaling condition fails.
- On \( \nR[x] \), squaring the evaluation at \( 0 \): \( p \mapsto p(0)^2 \). The outputs are still scalars. But for \( p = q = 1 \) we get \( (1 + 1)^2 = 4 \neq 1 + 1 \), so additivity fails.
- On \( M_2(F) \), replace the trace \( a + d \) of \( \A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \) by \( ad - bc \). Then \( \E_{11} \mapsto 0 \) and \( \E_{22} \mapsto 0 \), but \( \E_{11} + \E_{22} = \I_2 \mapsto 1 \), so additivity fails. The expression \( ad - bc \) is linear in each **row** separately, which is a different property.

**Why this definition.** Why single out the target \( F \)? Because nothing is lost. A linear map \( T \colon V \to F^m \) is the same thing as \( m \) functionals: if \( \varphi_i(\v) \) denotes the \( i \)-th entry of \( T\v \), then each \( \varphi_i \) is linear and \( T\v = (\varphi_1(\v), \dots, \varphi_m(\v)) \); conversely any \( m \) functionals stacked this way give a linear map. So functionals are the "rows" of linear maps, and understanding them one at a time is a way of understanding all maps into \( F^m \). The name comes from analysis, where the vectors were themselves functions and a map such as \( f \mapsto \int_0^1 f \) was called a "functional", a function of a function. The word "dual" will explain itself in this chapter: every statement about \( V \) has a mirror statement about \( V^{*} \).

::: {.warning}
**The values must lie in the field of scalars of \( V \).** Regard \( \nC \) as a vector space over \( \nC \). The real part \( z \mapsto \operatorname{Re} z \) is additive, and it respects **real** scalars, but it is **not** a linear functional on \( \nC \) over \( \nC \): with \( c = i \) and \( z = 1 \), \( \operatorname{Re}(i \cdot 1) = 0 \neq i \cdot \operatorname{Re}(1) = i \). It is a functional on \( \nC \) regarded as a vector space over \( \nR \). The dual space depends on the field.
:::

The first payoff is a count that holds for **every** non-zero functional: it hits every scalar, and in finite dimension it kills exactly one dimension.

::: {#prp-nonzero-functional-surjective}
[A Non-Zero Functional Is Surjective]

Let \( V \) be a vector space over \( F \), and let \( \varphi \in V^{*} \) be **non-zero**. Then \( \varphi \) is surjective. If \( V \) is finite-dimensional, then \( \dim \ker\varphi = \dim V - 1 \).
:::

::: {.proof}
Since \( \varphi \neq 0 \), there is \( \u \in V \) with \( c \coloneqq \varphi(\u) \neq 0 \). For every \( a \in F \), linearity gives \( \varphi(ac^{-1}\u) = ac^{-1}c = a \), so \( \varphi \) is surjective. Hence \( \im\varphi = F \) and \( \rank\varphi = 1 \). If \( V \) is finite-dimensional, the Rank–Nullity Theorem (@thm-rank-nullity) gives \( \dim\ker\varphi = \dim V - 1 \).
:::

For example, \( \ker\tr \) in \( M_n(F) \) has dimension \( n^2 - 1 \), and the polynomials in \( F[x]_{\le n} \) with \( p(c) = 0 \) form a subspace of dimension \( n \). Every non-zero functional cuts out a subspace one dimension smaller than the whole space. Later in this chapter these kernels, the hyperplanes, become the building blocks of every subspace.

::: {.check}
Which of the following are linear functionals? (a) \( p \mapsto p(0) + 1 \) on \( \nR[x] \). (b) \( p \mapsto p(1) - 2p'(0) \) on \( \nR[x] \). (c) \( \A \mapsto a_{12} \) on \( M_2(F) \).
:::

::: {.solution}
(a) No. It sends the zero polynomial to \( 1 \), but a linear map sends \( 0 \) to \( 0 \) (@thm-zero-maps-to-zero). (b) Yes. Evaluation at \( 1 \), differentiation and evaluation at \( 0 \) are linear, and \( V^{*} \) is closed under linear combinations and composition with linear maps (@thm-linear-maps-vector-space, @thm-composition-linear). (c) Yes. It is the coordinate of \( \A \) at \( \E_{12} \) in the standard basis of @exm-standard-bases, and coordinates are linear (@thm-coordinates-linear).
:::

## The dual basis

Return to the coordinate functionals. Let \( \sB = (\v_1, \dots, \v_n) \) be a basis of \( V \), and let \( \varphi_i(\v) \) be the \( i \)-th entry of \( \coord{\v}{\sB} \). The basis vector \( \v_j \) has coordinate vector \( \e_j \), so
\[
\varphi_i(\v_j) = \delta_{ij} = \begin{cases} 1 & \text{if } i = j, \\ 0 & \text{if } i \neq j, \end{cases}
\]
with the Kronecker delta of @def-identity-matrix. Each \( \varphi_i \) reads off one coordinate and ignores the others. These \( n \) functionals are the natural candidates for a basis of \( V^{*} \), and the theorem says they are one.

::: {#thm-dual-basis}
[The Dual Basis]

Let \( V \) be a finite-dimensional vector space over \( F \), and let \( \sB = (\v_1, \dots, \v_n) \) be a basis of \( V \).

::: {.enumerate options="label=(\alph*)"}
1. There are **unique** \( \varphi_1, \dots, \varphi_n \in V^{*} \) with \( \varphi_i(\v_j) = \delta_{ij} \) for all \( i, j \). For every \( \v \in V \), \( \varphi_i(\v) \) is the \( i \)-th entry of \( \coord{\v}{\sB} \).
2. The list \( (\varphi_1, \dots, \varphi_n) \) is a basis of \( V^{*} \).
3. For every \( \v \in V \) and every \( \varphi \in V^{*} \),
\[
\v = \sum_{i=1}^{n} \varphi_i(\v)\,\v_i, \qquad \varphi = \sum_{i=1}^{n} \varphi(\v_i)\,\varphi_i .
\]
:::
:::

::: {.idea}
① A functional is a linear map into \( F \), and a linear map may be prescribed freely on a basis, so existence and uniqueness in (a) are one citation. ② Independence: apply a vanishing combination \( \sum c_i\varphi_i \) to \( \v_j \); the delta kills every term but \( c_j \). ③ Spanning: we cannot count, because \( \dim V^{*} \) is exactly what we do not know yet. So we guess the coefficients. If \( \varphi = \sum c_i\varphi_i \), then applying both sides to \( \v_j \) forces \( c_j = \varphi(\v_j) \). With this guess, the two sides are linear maps that agree on a basis, hence equal.
:::

::: {.proof}
(a) For each \( i \), apply @thm-linear-transform-basis with \( W = F \) and the prescribed values \( \delta_{i1}, \dots, \delta_{in} \in F \). It gives exactly one linear map \( \varphi_i \colon V \to F \) with \( \varphi_i(\v_j) = \delta_{ij} \) for all \( j \). If \( \v = a_1\v_1 + \dots + a_n\v_n \), then by @thm-linear-combination
\[
\varphi_i(\v) = \sum_{j=1}^{n} a_j\varphi_i(\v_j) = \sum_{j=1}^{n} a_j\delta_{ij} = a_i ,
\]
the \( i \)-th entry of \( \coord{\v}{\sB} \) (@def-coordinates).

(b) *Independence.* Let \( c_1\varphi_1 + \dots + c_n\varphi_n = 0 \) in \( V^{*} \). Applying both sides to \( \v_j \) and using the pointwise operations of @def-dual-space,
\[
0 = \sum_{i=1}^{n} c_i\varphi_i(\v_j) = \sum_{i=1}^{n} c_i\delta_{ij} = c_j
\]
for each \( j \). Hence \( (\varphi_1, \dots, \varphi_n) \) is linearly independent.

*Spanning.* Let \( \varphi \in V^{*} \), and put \( \psi \coloneqq \sum_{i=1}^{n} \varphi(\v_i)\varphi_i \in V^{*} \). For each \( j \), \( \psi(\v_j) = \sum_i \varphi(\v_i)\delta_{ij} = \varphi(\v_j) \). So \( \psi \) and \( \varphi \) are linear maps \( V \to F \) that agree on the basis \( \sB \), and \( \psi = \varphi \) by the uniqueness part of @thm-linear-transform-basis. Hence \( \varphi \in \Span(\varphi_1, \dots, \varphi_n) \), and \( (\varphi_1, \dots, \varphi_n) \) is a basis of \( V^{*} \).

(c) The second formula was proved in the spanning step. The first is the definition of coordinates, since \( \varphi_i(\v) \) is the \( i \)-th coordinate of \( \v \) by (a). This proves the theorem.
:::

The two formulas in (c) are mirror images. A vector is recovered from its measurements by the dual basis; a functional is recovered from its values on the basis.

::: {#def-dual-basis}
[Dual Basis]

Let \( \sB = (\v_1, \dots, \v_n) \) be a basis of a finite-dimensional vector space \( V \) over \( F \). The basis \( (\varphi_1, \dots, \varphi_n) \) of \( V^{*} \) given by @thm-dual-basis, characterized by \( \varphi_i(\v_j) = \delta_{ij} \), is **the dual basis** of \( \sB \). We write it \( \sB^{*} \).
:::

Counting the dual basis gives the dimension of the dual space at once.

::: {#cor-dimension-dual-space}
[Dimension of the Dual Space]

Let \( V \) be a finite-dimensional vector space over \( F \). Then \( V^{*} \) is finite-dimensional and \( \dim V^{*} = \dim V \). In particular \( V^{*} \cong V \).
:::

::: {.proof}
Let \( n = \dim V \) and choose a basis of \( V \) (@cor-basis-existence). By @thm-dual-basis (b), its dual basis is a basis of \( V^{*} \) of length \( n \). Hence \( \dim V^{*} = n \), and \( V^{*} \cong V \) by @thm-isomorphic-iff-same-dimension.
:::

For instance \( \dim M_{m \times n}(F)^{*} = mn \) and \( \dim F[x]_{\le n}^{*} = n + 1 \).

::: {.remark}
Many books write \( \v_i^{*} \) for the dual basis functional \( \varphi_i \). We avoid that notation for two reasons. It suggests that \( \varphi_i \) is determined by \( \v_i \) alone, which is false (see the warning below). And in this book the star on a map is reserved for adjoints, which come much later. We write \( \varphi_i \), and speak of "the dual basis of \( \sB \)".
:::

How do we find a dual basis in practice? In \( F^n \), functionals are rows, and the conditions \( \varphi_i(\v_j) = \delta_{ij} \) turn into a single matrix equation.

:::: {#exm-dual-basis-inverse-rows}
[The Dual Basis Is Read Off the Inverse Matrix]

::: {.enumerate options="label=(\alph*)"}
1. Find the dual basis of \( \sB = ((1, 1), (1, -1)) \) in \( \nR^2 \).
2. More generally, let \( \sB = (\v_1, \dots, \v_n) \) be a basis of \( F^n \), and let \( \P = \begin{pmatrix} \v_1 & \cdots & \v_n \end{pmatrix} \). Show that \( \P \) is invertible and that the dual basis of \( \sB \) is \( \varphi_i(\x) = \r_i\x \), where \( \r_i \) is the \( i \)-th **row** of \( \P^{-1} \).
:::
::::

::: {.solution}
(a) By @thm-functionals-on-fn, \( \varphi_1(x, y) = px + qy \) for some \( p, q \in \nR \), that is, \( \varphi_1(\x) = \begin{pmatrix} p & q \end{pmatrix}\x \). The conditions \( \varphi_1(1, 1) = 1 \) and \( \varphi_1(1, -1) = 0 \) say \( \begin{pmatrix} p & q \end{pmatrix}\P = \begin{pmatrix} 1 & 0 \end{pmatrix} \) with \( \P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \). Likewise the row \( \r_2 \) of \( \varphi_2 \) satisfies \( \r_2\P = \begin{pmatrix} 0 & 1 \end{pmatrix} \). Stacking the two rows into a matrix \( \R \), the four conditions become \( \R\P = \I_2 \), so \( \R = \P^{-1} \). By @thm-two-by-two-inverse, with \( ad - bc = -2 \),
\[
\P^{-1} = \frac{1}{-2}\begin{pmatrix} -1 & -1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} \tfrac12 & \tfrac12 \\ \tfrac12 & -\tfrac12 \end{pmatrix}.
\]
Hence
\[
\varphi_1(x, y) = \frac{x + y}{2}, \qquad \varphi_2(x, y) = \frac{x - y}{2}.
\]
Check: \( \varphi_1(1, 1) = 1 \), \( \varphi_1(1, -1) = 0 \), \( \varphi_2(1, 1) = 0 \), \( \varphi_2(1, -1) = 1 \). And the first formula of @thm-dual-basis (c) for \( \v = (3, 1) \) reads \( (3, 1) = 2(1, 1) + 1(1, -1) \), which is true. The second formula expresses a functional in the dual basis through its values on \( \sB \): for \( \psi(x, y) = x \), the values are \( \psi(1, 1) = 1 \) and \( \psi(1, -1) = 1 \), so \( \psi = \varphi_1 + \varphi_2 \), and indeed \( \frac{x + y}{2} + \frac{x - y}{2} = x \).

(b) The columns of \( \P \) form a basis of \( F^n \), so \( \P \) is invertible by @thm-invertible-tfae. Let \( \R \in M_n(F) \) have rows \( \r_1, \dots, \r_n \), and let \( \psi_i(\x) \coloneqq \r_i\x \). By the entry formula for a product (@thm-three-views-of-product), \( \psi_i(\v_j) = \r_i\v_j = (\R\P)_{ij} \). Hence \( \psi_i(\v_j) = \delta_{ij} \) for all \( i, j \) if and only if \( \R\P = \I_n \), if and only if \( \R = \P^{-1} \) (multiply by \( \P^{-1} \) on the right). Now take \( \R = \P^{-1} \): the functionals \( \psi_i(\x) = \r_i\x \) are linear (@thm-functionals-on-fn) and satisfy \( \psi_i(\v_j) = \delta_{ij} \), so by the uniqueness in @thm-dual-basis (a) they are the dual basis.

This agrees with Chapter 3: \( \P = \mtx{\id}{\sB}{\sE} \) and \( \P^{-1} = \mtx{\id}{\sE}{\sB} \) (@thm-change-of-coordinates), so \( \P^{-1}\x = \coord{\x}{\sB} \), and row \( i \) of \( \P^{-1} \) computes the \( i \)-th coordinate, as @thm-dual-basis (a) predicts. The columns of \( \P \) are the basis; the rows of \( \P^{-1} \) are the dual basis.
:::

::: {.warning}
**A dual basis functional depends on the whole basis, not only on its own vector.** In \( \nR^2 \), the basis \( ((1, 0), (0, 1)) \) has first dual functional \( \varphi_1(x, y) = x \). The basis \( ((1, 0), (1, 1)) \) has the same first vector, but \( \P^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} \), so its first dual functional is \( \varphi_1(x, y) = x - y \). Changing \( \v_2 \) changed \( \varphi_1 \), because \( \varphi_1 \) must vanish on \( \v_2 \).
:::

The same method works away from \( F^n \), once we recognize the coordinates.

:::: {#exm-dual-basis-polynomials}
[Dual Bases in \( \nR[x]_{\le 2} \)]

::: {.enumerate options="label=(\alph*)"}
1. Show that the dual basis of \( (1, x, x^2) \) in \( \nR[x]_{\le 2} \) is \( (\varphi_0, \varphi_1, \varphi_2) \) with \( \varphi_0(p) = p(0) \), \( \varphi_1(p) = p'(0) \) and \( \varphi_2(p) = \tfrac12p''(0) \). (We index from \( 0 \) to match the exponents.)
2. Let \( \ell_{-1} = \tfrac12x(x - 1) \), \( \ell_0 = 1 - x^2 \) and \( \ell_1 = \tfrac12x(x + 1) \). Show that \( (\ell_{-1}, \ell_0, \ell_1) \) is a basis of \( \nR[x]_{\le 2} \) whose dual basis is \( (\varepsilon_{-1}, \varepsilon_0, \varepsilon_1) \), the evaluations at \( -1, 0, 1 \). Deduce that \( p = p(-1)\ell_{-1} + p(0)\ell_0 + p(1)\ell_1 \) for every \( p \in \nR[x]_{\le 2} \).
:::
::::

::: {.solution}
(a) Each \( \varphi_k \) is linear, as a composition of differentiation (@exm-differentiation) with evaluation at \( 0 \), scaled. For \( p = a_0 + a_1x + a_2x^2 \), we have \( p(0) = a_0 \), \( p'(0) = a_1 \) and \( \tfrac12p''(0) = \tfrac12 \cdot 2a_2 = a_2 \). So \( \varphi_k(x^j) = \delta_{kj} \) for \( j, k \in \{0, 1, 2\} \), and by the uniqueness in @thm-dual-basis (a) these are the dual basis. Over a general field \( F \), the dual basis of \( (1, x, x^2) \) is still "the coefficient of \( x^k \)", but the formula \( \tfrac12p''(0) \) needs \( 2 \neq 0 \) in \( F \).

(b) The values of the \( \ell \)'s at the three points are
\[
\begin{aligned}
&\ell_{-1}(-1) = 1,\ \ell_{-1}(0) = 0,\ \ell_{-1}(1) = 0; \\
&\ell_0(-1) = 0,\ \ell_0(0) = 1,\ \ell_0(1) = 0; \\
&\ell_1(-1) = 0,\ \ell_1(0) = 0,\ \ell_1(1) = 1.
\end{aligned}
\]
That is, \( \varepsilon_i(\ell_j) = \delta_{ij} \) for \( i, j \in \{-1, 0, 1\} \). *Basis.* Let \( c_{-1}\ell_{-1} + c_0\ell_0 + c_1\ell_1 = 0 \). Evaluating at \( j \in \{-1, 0, 1\} \) gives \( c_j = 0 \). So the list is independent, of length \( 3 = \dim \nR[x]_{\le 2} \), hence a basis by @thm-right-size-basis. *Dual basis.* The evaluations are linear (@exm-linear-functionals) and satisfy \( \varepsilon_i(\ell_j) = \delta_{ij} \), so they are the dual basis by the uniqueness in @thm-dual-basis (a). The first formula of @thm-dual-basis (c) now reads \( p = \sum_i \varepsilon_i(p)\,\ell_i = p(-1)\ell_{-1} + p(0)\ell_0 + p(1)\ell_1 \).

The last formula rebuilds a polynomial from three of its values. It is a preview of the Lagrange interpolation formula of Chapter 5, and it explains where the \( \ell \)'s come from: they are the basis dual to the evaluations.
:::

::: {.check}
Let \( (\v_1, \v_2, \v_3) \) be a basis of \( V \) with dual basis \( (\varphi_1, \varphi_2, \varphi_3) \). Compute \( \varphi_2(3\v_1 - \v_2 + 5\v_3) \) and \( (2\varphi_1 + \varphi_3)(\v_3) \).
:::

::: {.solution}
\( \varphi_2(3\v_1 - \v_2 + 5\v_3) = 3 \cdot 0 - 1 \cdot 1 + 5 \cdot 0 = -1 \), the second coordinate. \( (2\varphi_1 + \varphi_3)(\v_3) = 2 \cdot 0 + 1 = 1 \).
:::

::: {.warning}
**\( V \cong V^{*} \) is true in finite dimension, but no isomorphism is singled out.** @cor-dimension-dual-space gives an isomorphism by sending \( \v_i \mapsto \varphi_i \), and that depends on the basis. In \( \nR^2 \) with the standard basis, it sends \( (1, 0) \) to the functional \( (x, y) \mapsto x \). With the basis \( ((1, 0), (1, 1)) \), it sends the **same** vector \( (1, 0) \) to \( (x, y) \mapsto x - y \), by the warning above. A vector does not come with "its" functional. Later in this chapter we make precise the sense in which \( V^{*} \) needs a choice to be identified with \( V \), while the double dual \( V^{**} \) does not.
:::

## Testing against functionals

In \( F^n \) a vector is zero exactly when all its entries are zero, and the entries are the values of the coordinate functionals. The same holds in any finite-dimensional space, and it gives a flexible way to prove that a vector is zero.

::: {#thm-functionals-separate-points}
[Functionals Separate Vectors]

Let \( V \) be a finite-dimensional vector space over \( F \).

::: {.enumerate options="label=(\alph*)"}
1. If \( \v \in V \) and \( \v \neq \0 \), then there is \( \varphi \in V^{*} \) with \( \varphi(\v) = 1 \).
2. If \( \v \in V \) satisfies \( \varphi(\v) = 0 \) for **every** \( \varphi \in V^{*} \), then \( \v = \0 \). It suffices that \( \varphi_i(\v) = 0 \) for the functionals \( \varphi_i \) of **one** dual basis.
3. For \( \u, \w \in V \): \( \u = \w \) if and only if \( \varphi(\u) = \varphi(\w) \) for every \( \varphi \in V^{*} \).
:::
:::

::: {.idea}
We need a functional that does not vanish at \( \v \), and the only functionals we can build at will are dual basis functionals. The first one takes the value \( 1 \) on the first basis vector. So make \( \v \) the first vector of a basis: this is possible exactly because \( \v \neq \0 \).
:::

::: {.proof}
(a) Since \( \v \neq \0 \), the list \( (\v) \) is linearly independent: if \( a\v = \0 \), then \( a = 0 \) by @thm-zero-product. By the Basis Extension Theorem (@thm-basis-extension), there is a basis \( (\v, \v_2, \dots, \v_n) \) of \( V \). Let \( (\varphi_1, \dots, \varphi_n) \) be its dual basis (@thm-dual-basis). Then \( \varphi_1(\v) = 1 \).

(b) The first statement is the contrapositive of (a). For the second, if \( (\varphi_1, \dots, \varphi_n) \) is the dual basis of a basis \( (\v_1, \dots, \v_n) \) and every \( \varphi_i(\v) = 0 \), then \( \v = \sum_i \varphi_i(\v)\v_i = \0 \) by @thm-dual-basis (c).

(c) If \( \u = \w \), the values agree. Conversely, if \( \varphi(\u) = \varphi(\w) \) for every \( \varphi \), then \( \varphi(\u - \w) = \varphi(\u) - \varphi(\w) = 0 \) for every \( \varphi \), so \( \u - \w = \0 \) by (b).
:::

This is the signature move of the chapter: **to show a vector is zero, test it against every functional, and a dual basis suffices.** It turns one equation in \( V \) into scalar equations, which are often easier to reach.

::: {.remark}
Parts (a), (b) (first sentence) and (c) hold for **every** vector space \( V \); only (a) needs a new construction. By @thm-basis-extension-general, \( \{\v\} \) extends to a basis \( B \) of \( V \). Every \( \w \in V \) is a finite combination of distinct vectors of \( B \), with coefficients that are unique because \( B \) is independent. Let \( \varphi(\w) \) be the coefficient of \( \v \) in this expansion (and \( 0 \) if \( \v \) does not occur). Adding or scaling expansions gives expansions, so by uniqueness coefficients add and scale, and \( \varphi \) is linear with \( \varphi(\v) = 1 \). The price is Zorn's Lemma (@thm-zorn): for \( \nR \) over \( \nQ \), no one has an explicit formula for such a functional.
:::

:::: {#exm-trace-test-zero-matrix}
[A Matrix Killed by Every Trace]

Let \( \A \in M_n(F) \) satisfy \( \tr(\A\X) = 0 \) for every \( \X \in M_n(F) \). Show that \( \A = 0 \). Deduce that every linear functional on \( M_n(F) \) is \( \X \mapsto \tr(\A\X) \) for exactly one \( \A \in M_n(F) \).
::::

::: {.solution}
The matrix units \( \E_{ij} \) form a basis of \( M_n(F) \) (@exm-standard-bases), and \( \A = \sum_{i,j} a_{ij}\E_{ij} \). By @thm-dual-basis (a), its dual basis consists of the coordinate functionals \( \varepsilon_{ij}(\A) = a_{ij} \). We compute \( \varepsilon_{ij}(\A) \) as a trace. By @def-matrix-multiplication, \( (\A\E_{ji})_{kk} = \sum_l a_{kl}(\E_{ji})_{lk} \), and \( (\E_{ji})_{lk} = 1 \) only for \( l = j \) and \( k = i \). So the only non-zero diagonal entry of \( \A\E_{ji} \) is \( (\A\E_{ji})_{ii} = a_{ij} \), and
\[
\tr(\A\E_{ji}) = a_{ij} = \varepsilon_{ij}(\A).
\]
Taking \( \X = \E_{ji} \) in the hypothesis gives \( \varepsilon_{ij}(\A) = 0 \) for all \( i, j \). By @thm-functionals-separate-points (b), \( \A = 0 \).

For the deduction, let \( \Theta \colon M_n(F) \to M_n(F)^{*} \), \( \Theta(\A)(\X) \coloneqq \tr(\A\X) \). Each \( \Theta(\A) \) is linear in \( \X \), and \( \Theta \) is linear in \( \A \), both by @thm-trace-properties (1) and the distributive laws of @thm-matrix-multiplication-properties. We just showed \( \ker\Theta = \{0\} \), so \( \Theta \) is injective (@thm-injective-iff-trivial-kernel). Since \( \dim M_n(F)^{*} = n^2 = \dim M_n(F) \) (@cor-dimension-dual-space), \( \Theta \) is bijective by @cor-rank-nullity-consequences (e). This is the matrix analogue of @thm-functionals-on-fn.
:::

## When \( V \) is infinite-dimensional

The main results of the last two subsections assumed finite dimension, or used a finite basis. That hypothesis does real work. Consider \( F[x] \), with its basis \( \{1, x, x^2, \dots\} \) (@exm-basis-of-polynomials). For \( k \in \nN \) let
\[
\varphi_k(p) \coloneqq \text{the coefficient of } x^k \text{ in } p .
\]
These are the coordinate functionals, and \( \varphi_k(x^j) = \delta_{kj} \), exactly as in @thm-dual-basis. But they are not a basis of the dual space.

::: {#prp-coordinate-functionals-do-not-span}
[The Coordinate Functionals Do Not Span \( F[x]^{*} \)]

The functionals \( \varphi_k \) (\( k \in \nN \)) lie in \( F[x]^{*} \) and form a linearly independent set. But they do **not** span \( F[x]^{*} \): the evaluation \( \varepsilon_1 \colon p \mapsto p(1) \) is **not** a linear combination of finitely many \( \varphi_k \).
:::

::: {.proof}
Polynomials are added and scaled coefficient by coefficient (@def-polynomial), so each \( \varphi_k \) is linear. *Independence.* Let \( k_1, \dots, k_m \) be distinct and \( c_1\varphi_{k_1} + \dots + c_m\varphi_{k_m} = 0 \). Applying both sides to \( x^{k_j} \) gives \( c_j = 0 \), since \( \varphi_{k_i}(x^{k_j}) = \delta_{k_ik_j} \).

*Not spanning.* The evaluation \( \varepsilon_1 \) is linear by @exm-linear-functionals (a), and \( \varepsilon_1(x^N) = 1^N = 1 \) for every \( N \in \nN \). Suppose, for a contradiction, that \( \varepsilon_1 = c_1\varphi_{k_1} + \dots + c_m\varphi_{k_m} \) for some \( m \in \nN \), distinct \( k_j \) and \( c_j \in F \). Choose \( N \in \nN \) larger than every \( k_j \). Then \( \varphi_{k_j}(x^N) = 0 \) for every \( j \), so the right-hand side sends \( x^N \) to \( 0 \), while \( \varepsilon_1(x^N) = 1 \). This contradiction shows \( \varepsilon_1 \notin \Span\{\varphi_k : k \in \nN\} \).
:::

Where did the proof of @thm-dual-basis break? In the spanning step. The candidate \( \sum_i \varphi(\v_i)\varphi_i \) for \( \varphi = \varepsilon_1 \) would be \( \varphi_0 + \varphi_1 + \varphi_2 + \cdots \), an infinite sum, and infinite sums mean nothing in a vector space (the warning in Chapter 1, §8). A functional on \( F[x] \) may take non-zero values on infinitely many basis vectors, while a finite combination of the \( \varphi_k \) cannot.

::: {.remark}
More is true, and we state it without proof. For every infinite-dimensional \( V \), a basis of \( V^{*} \) is **strictly larger**, as an infinite set, than a basis of \( V \); in particular \( V^{*} \not\cong V \). So "\( \dim V^{*} = \dim V \)" is a genuinely finite-dimensional fact, and this is why finite dimension appears in the hypotheses of most theorems in this chapter. A first step towards seeing how large \( F[x]^{*} \) is appears in Exercise C4 below.
:::

## Exercises

### A. Check your understanding

:::: {#exr-linear-functionals-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define a linear functional on a vector space \( V \) over \( F \), and the dual space \( V^{*} \).
2. True or false: \( p \mapsto p(1)^2 \) is a linear functional on \( \nR[x] \). Justify your answer.
3. True or false: if \( (\v_1, \v_2) \) and \( (\v_1, \w_2) \) are bases of \( V \), then the first functionals of their dual bases are equal. Justify your answer.
4. What is \( \dim M_{2 \times 3}(F)^{*} \)?
5. State the formula that expresses \( \varphi \in V^{*} \) in the dual basis of \( (\v_1, \dots, \v_n) \).
6. Name the move you would use to prove that a vector \( \v \) of a finite-dimensional space is \( \0 \) without computing \( \v \) itself.
:::
::::

::: {.solution}
(a) See @def-linear-functional and @def-dual-space: a linear functional is a linear map \( V \to F \), and \( V^{*} = \cL(V, F) \) with pointwise addition and scaling.

(b) False. For \( p = 1 \) and \( c = 2 \), the polynomial \( cp = 2 \) is sent to \( 2^2 = 4 \), while \( c \) times the image of \( p \) is \( 2 \cdot 1^2 = 2 \). So the scaling condition fails.

(c) False. By the warning after @exm-dual-basis-inverse-rows, in \( \nR^2 \) the bases \( ((1, 0), (0, 1)) \) and \( ((1, 0), (1, 1)) \) have first dual functionals \( x \) and \( x - y \).

(d) \( 6 \), by @cor-dimension-dual-space, since \( \dim M_{2 \times 3}(F) = 6 \).

(e) \( \varphi = \sum_{i=1}^n \varphi(\v_i)\varphi_i \), by @thm-dual-basis (c).

(f) Test against functionals: show \( \varphi(\v) = 0 \) for every \( \varphi \in V^{*} \), or only for the functionals of one dual basis, and apply @thm-functionals-separate-points (b).
:::

### B. Practice

:::: {#exr-linear-functionals-b1}
[B1: Finding dual bases]

::: {.enumerate options="label=(\alph*)"}
1. Find the dual basis of \( ((1, 0, 1), (0, 1, 1), (1, 1, 1)) \) in \( \nR^3 \).
2. Show that the dual basis of \( (1, x - 1, (x - 1)^2) \) in \( \nR[x]_{\le 2} \) is \( p \mapsto p(1) \), \( p \mapsto p'(1) \), \( p \mapsto \tfrac12p''(1) \). Hence write \( p = 2 + 3x - x^2 \) in this basis.
:::
::::

::: {.solution}
(a) Let \( \P \) have the three vectors as columns. Row reduction of \( [\P \mid \I_3] \) (@thm-inverse-by-row-reduction) gives
\[
\P = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix}, \qquad \P^{-1} = \begin{pmatrix} 0 & -1 & 1 \\ -1 & 0 & 1 \\ 1 & 1 & -1 \end{pmatrix},
\]
and one checks \( \P^{-1}\P = \I_3 \). By @exm-dual-basis-inverse-rows (b), the dual basis is
\[
\varphi_1(x, y, z) = -y + z, \qquad \varphi_2(x, y, z) = -x + z, \qquad \varphi_3(x, y, z) = x + y - z .
\]
For instance \( \varphi_3(1, 0, 1) = 0 \), \( \varphi_3(0, 1, 1) = 0 \) and \( \varphi_3(1, 1, 1) = 1 \).

(b) The three maps are linear, as combinations of differentiation and evaluation at \( 1 \). Call them \( \psi_1, \psi_2, \psi_3 \). On the basis:
\[
\begin{aligned}
&\psi_1(1) = 1,\ \psi_1(x - 1) = 0,\ \psi_1((x - 1)^2) = 0; \\
&\psi_2(1) = 0,\ \psi_2(x - 1) = 1,\ \psi_2((x - 1)^2) = 2(1 - 1) = 0;
\end{aligned}
\]
\[
\psi_3(1) = 0,\ \psi_3(x - 1) = 0,\ \psi_3((x - 1)^2) = \tfrac12 \cdot 2 = 1 .
\]
So \( \psi_i \) takes the value \( \delta_{ij} \) on the \( j \)-th basis vector, and by the uniqueness in @thm-dual-basis (a) they are the dual basis. (The list \( (1, x - 1, (x - 1)^2) \) is a basis: it has distinct degrees \( 0, 1, 2 \), so it is independent by @thm-distinct-degrees-independent, and it has length \( 3 = \dim \nR[x]_{\le 2} \), so @thm-right-size-basis applies.) For \( p = 2 + 3x - x^2 \): \( p(1) = 4 \), \( p'(1) = 3 - 2 = 1 \), \( \tfrac12p''(1) = -1 \). By @thm-dual-basis (c),
\[
p = 4 + (x - 1) - (x - 1)^2 .
\]
Check: \( 4 + x - 1 - (x^2 - 2x + 1) = 2 + 3x - x^2 \).
:::

:::: {#exr-linear-functionals-b2}
[B2: Which maps are functionals?]

Determine which of the following are linear functionals. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \nR^3 \to \nR \), \( (x, y, z) \mapsto 2x - z \).
2. \( \nR^3 \to \nR \), \( (x, y, z) \mapsto xy \).
3. \( M_2(\nR) \to \nR \), \( \A \mapsto a_{12} - 3a_{21} \).
4. \( \nR[x] \to \nR \), \( p \mapsto \int_0^1 t\,p(t)\,\dd t \).
5. \( \nR[x]_{\le 2} \to \nR \), \( p \mapsto p(0) + p'(0) + 1 \).
6. \( \nC^2 \to \nC \), \( (z, w) \mapsto z + \conj{w} \), where \( \nC^2 \) is a vector space over \( \nC \).
:::
::::

::: {.solution}
(a) Yes: it is \( \varphi_{\a} \) with \( \a = (2, 0, -1) \), linear by @thm-functionals-on-fn.

(b) No. \( (1, 1, 0) \mapsto 1 \), but \( 2(1, 1, 0) = (2, 2, 0) \mapsto 4 \neq 2 \), so the scaling condition fails.

(c) Yes: it is \( \varepsilon_{12} - 3\varepsilon_{21} \), a combination of coordinate functionals for the standard basis, and \( V^{*} \) is a vector space (@def-dual-space).

(d) Yes. By linearity of the integral, \( \int_0^1 t(p + q)(t)\,\dd t = \int_0^1 tp(t)\,\dd t + \int_0^1 tq(t)\,\dd t \) and \( \int_0^1 t(cp)(t)\,\dd t = c\int_0^1 tp(t)\,\dd t \).

(e) No. The zero polynomial is sent to \( 1 \neq 0 \), contradicting @thm-zero-maps-to-zero.

(f) No. With \( c = i \) and \( (z, w) = (0, 1) \): \( (0, i) \mapsto \conj{i} = -i \), while \( i \cdot (0 + \conj{1}) = i \). The map is additive and respects real scalars, but it is not linear over \( \nC \).
:::

:::: {#exr-linear-functionals-b3}
[B3: Coordinates of a functional]

::: {.enumerate options="label=(\alph*)"}
1. Let \( (\varphi_1, \varphi_2) \) be the dual basis of \( ((1, 1), (1, -1)) \) from @exm-dual-basis-inverse-rows. Write \( \psi(x, y) = 3x + 5y \) as a combination of \( \varphi_1 \) and \( \varphi_2 \).
2. Let \( (\varphi_0, \varphi_1, \varphi_2) \) be the dual basis of \( (1, x, x^2) \) from @exm-dual-basis-polynomials. Write \( \iota(p) = \int_0^1 p(t)\,\dd t \) as a combination of them.
:::
::::

::: {.solution}
(a) By @thm-dual-basis (c), \( \psi = \psi(1, 1)\varphi_1 + \psi(1, -1)\varphi_2 = 8\varphi_1 - 2\varphi_2 \). Check: \( 8 \cdot \frac{x + y}{2} - 2 \cdot \frac{x - y}{2} = 4x + 4y - x + y = 3x + 5y \).

(b) By @thm-dual-basis (c), \( \iota = \iota(1)\varphi_0 + \iota(x)\varphi_1 + \iota(x^2)\varphi_2 = \varphi_0 + \tfrac12\varphi_1 + \tfrac13\varphi_2 \). Check: for \( p = a_0 + a_1x + a_2x^2 \), the right-hand side is \( a_0 + \tfrac{a_1}{2} + \tfrac{a_2}{3} = \int_0^1 p \).
:::

### C. Going deeper

:::: {#exr-linear-functionals-c1}
[C1: Functionals with the same kernel]

Let \( V \) be **any** vector space over \( F \), and let \( \varphi, \psi \in V^{*} \) with \( \ker\varphi = \ker\psi \). Prove that \( \psi = c\varphi \) for some \( c \in F \). Is the converse true?

*Hint: if \( \varphi \neq 0 \), fix \( \u \) with \( \varphi(\u) = 1 \) and consider \( \v - \varphi(\v)\u \).*
::::

::: {.solution}
If \( \varphi = 0 \), then \( \ker\psi = \ker\varphi = V \), so \( \psi = 0 = 1 \cdot \varphi \). Suppose \( \varphi \neq 0 \). By @prp-nonzero-functional-surjective there is \( \u \in V \) with \( \varphi(\u) = 1 \). Let \( \v \in V \). Then
\[
\varphi\bigl(\v - \varphi(\v)\u\bigr) = \varphi(\v) - \varphi(\v)\varphi(\u) = 0,
\]
so \( \v - \varphi(\v)\u \in \ker\varphi = \ker\psi \). Therefore \( 0 = \psi(\v) - \varphi(\v)\psi(\u) \), that is, \( \psi(\v) = \psi(\u)\varphi(\v) \). Since \( \v \) was arbitrary, \( \psi = c\varphi \) with \( c = \psi(\u) \).

The converse holds only for \( c \neq 0 \): if \( \psi = c\varphi \) with \( c \neq 0 \), then \( \psi(\v) = 0 \iff \varphi(\v) = 0 \). For \( c = 0 \) and \( \varphi \neq 0 \), \( \ker\psi = V \neq \ker\varphi \).
:::

:::: {#exr-linear-functionals-c2}
[C2: Functionals vanishing where others vanish]

Let \( V \) be a vector space over \( F \), and let \( \varphi_1, \dots, \varphi_k, \psi \in V^{*} \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( \ker\varphi_1 \cap \dots \cap \ker\varphi_k \subseteq \ker\psi \), then \( \psi \in \Span(\varphi_1, \dots, \varphi_k) \).
2. Deduce that if \( V \) is finite-dimensional, then \( (\varphi_1, \dots, \varphi_k) \) spans \( V^{*} \) if and only if \( \ker\varphi_1 \cap \dots \cap \ker\varphi_k = \{\0\} \).
:::

*Hint: for (a), consider the linear map \( T \colon V \to F^k \), \( \v \mapsto (\varphi_1(\v), \dots, \varphi_k(\v)) \).*
::::

::: {.solution}
(a) Let \( T \) be as in the hint; it is linear because each \( \varphi_i \) is. Its kernel is \( \ker\varphi_1 \cap \dots \cap \ker\varphi_k \). Define \( S \colon \im T \to F \) by \( S(T\v) \coloneqq \psi(\v) \). This is well defined: if \( T\v = T\v' \), then \( \v - \v' \in \ker T \subseteq \ker\psi \), so \( \psi(\v) = \psi(\v') \). It is linear, since \( S(cT\v + T\v') = S(T(c\v + \v')) = \psi(c\v + \v') = cS(T\v) + S(T\v') \).

Now extend \( S \) to \( F^k \). The subspace \( \im T \subseteq F^k \) has a basis \( (\y_1, \dots, \y_r) \) (@thm-subspace-dimension, @cor-basis-existence), which extends to a basis \( (\y_1, \dots, \y_k) \) of \( F^k \) by @thm-basis-extension. By @thm-linear-transform-basis there is \( \tilde S \in (F^k)^{*} \) with \( \tilde S(\y_j) = S(\y_j) \) for \( j \le r \) and \( \tilde S(\y_j) = 0 \) for \( j > r \). Then \( \tilde S \) and \( S \) agree on a basis of \( \im T \), so \( \tilde S = S \) on \( \im T \). By @thm-functionals-on-fn, \( \tilde S(z_1, \dots, z_k) = a_1z_1 + \dots + a_kz_k \) for some \( a_i \in F \). Hence for every \( \v \in V \),
\[
\psi(\v) = S(T\v) = \tilde S\bigl(\varphi_1(\v), \dots, \varphi_k(\v)\bigr) = a_1\varphi_1(\v) + \dots + a_k\varphi_k(\v),
\]
so \( \psi = a_1\varphi_1 + \dots + a_k\varphi_k \). Note that \( V \) was arbitrary; only \( F^k \) needed to be finite-dimensional.

(b) \( (\Leftarrow) \) If the intersection is \( \{\0\} \), it lies in \( \ker\psi \) for every \( \psi \in V^{*} \), so every \( \psi \) is in the span by (a). \( (\Rightarrow) \) Suppose the \( \varphi_i \) span \( V^{*} \), and let \( \v \) lie in every \( \ker\varphi_i \). Every \( \psi \in V^{*} \) is a combination \( \sum c_i\varphi_i \), so \( \psi(\v) = \sum c_i\varphi_i(\v) = 0 \). By @thm-functionals-separate-points (b), \( \v = \0 \).
:::

:::: {#exr-linear-functionals-c3}
[C3: Evaluations as a dual basis]

Let \( n \in \nN \).

::: {.enumerate options="label=(\alph*)"}
1. Let \( x_0, \dots, x_n \in F \) be **distinct**. Prove that the evaluations \( (\varepsilon_{x_0}, \dots, \varepsilon_{x_n}) \) form a basis of \( F[x]_{\le n}^{*} \), and that they are the dual basis of some basis of \( F[x]_{\le n} \).
2. Over \( \nF_2 \) with \( n = 2 \), show that the evaluations at the elements of \( \nF_2 \) do **not** span \( \nF_2[x]_{\le 2}^{*} \).
:::

*Hint: for (a), use @thm-interpolation-unique to build the basis first.*
::::

::: {.solution}
(a) For each \( j \), @thm-interpolation-unique gives \( \ell_j \in F[x]_{\le n} \) with \( \ell_j(x_i) = \delta_{ij} \) for \( i = 0, \dots, n \), because the \( x_i \) are distinct. If \( \sum_j c_j\ell_j = 0 \), evaluating at \( x_i \) gives \( c_i = 0 \). So \( (\ell_0, \dots, \ell_n) \) is independent of length \( n + 1 = \dim F[x]_{\le n} \), hence a basis by @thm-right-size-basis. The evaluations are linear (@exm-linear-functionals) and \( \varepsilon_{x_i}(\ell_j) = \delta_{ij} \), so by the uniqueness in @thm-dual-basis (a) they are the dual basis of \( (\ell_0, \dots, \ell_n) \), and by @thm-dual-basis (b) a basis of \( F[x]_{\le n}^{*} \).

(b) \( \nF_2 = \{0, 1\} \) has only two elements, so only \( \varepsilon_0 \) and \( \varepsilon_1 \) are available, and \( \dim \nF_2[x]_{\le 2}^{*} = 3 \) by @cor-dimension-dual-space. Two functionals cannot span a \( 3 \)-dimensional space (@thm-size-bounds). Concretely, \( p = x^2 + x \) is non-zero but \( p(0) = 0 \) and \( p(1) = 1 + 1 = 0 \); the coefficient functional of \( x^2 \) takes the value \( 1 \) on \( p \), so it is not a combination of \( \varepsilon_0, \varepsilon_1 \). The hypothesis "distinct points" in (a) needs \( n + 1 \) distinct elements of \( F \), which a small field may not have.
:::

:::: {#exr-linear-functionals-c4}
[C4: How large is \( F\lbrack x\rbrack^{*} \)?]

Let \( F^{\nN} \) be the space of sequences with entries in \( F \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \Phi \colon F[x]^{*} \to F^{\nN} \), \( \varphi \mapsto (\varphi(1), \varphi(x), \varphi(x^2), \dots) \), is an isomorphism.
2. Identify \( \Phi(\varphi_k) \) for the coordinate functionals \( \varphi_k \) of @prp-coordinate-functionals-do-not-span, and \( \Phi(\varepsilon_1) \). Explain how @prp-coordinate-functionals-do-not-span matches @exm-sequence-standard-vectors.
:::

*Hint: for surjectivity, remember that a polynomial has only finitely many non-zero coefficients.*
::::

::: {.solution}
(a) *Linear.* The \( k \)-th entry of \( \Phi(c\varphi + \psi) \) is \( (c\varphi + \psi)(x^k) = c\varphi(x^k) + \psi(x^k) \), by the pointwise operations of @def-dual-space. *Injective.* If \( \Phi(\varphi) = \0 \), then \( \varphi \) vanishes on the basis \( \{x^k\} \) of @exm-basis-of-polynomials. Every polynomial is a finite combination of the \( x^k \), so \( \varphi = 0 \) by @thm-linear-combination; hence \( \Phi \) is injective by @thm-injective-iff-trivial-kernel. *Surjective.* Given \( (a_0, a_1, \dots) \in F^{\nN} \), define \( \varphi(b_0 + b_1x + \dots + b_Nx^N) \coloneqq a_0b_0 + \dots + a_Nb_N \). This is a finite sum, it is well defined because coefficients are unique, and it is linear because coefficients add and scale; it is the linear map with \( \varphi(x^k) = a_k \) given by @thm-linear-map-from-any-basis. Then \( \Phi(\varphi) = (a_0, a_1, \dots) \). By @thm-inverse-is-linear, \( \Phi \) is an isomorphism.

(b) \( \Phi(\varphi_k) = (\delta_{k0}, \delta_{k1}, \dots) = \e_k \), and \( \Phi(\varepsilon_1) = (1, 1, 1, \dots) \). An isomorphism carries spans to spans, so \( \varepsilon_1 \in \Span\{\varphi_k\} \) would give \( (1, 1, 1, \dots) \in \Span\{\e_k\} \). @exm-sequence-standard-vectors showed this is false, because finite combinations of the \( \e_k \) have only finitely many non-zero entries. So \( F[x] \), with its basis \( \{x^k\} \) indexed by \( \nN \), has a dual as large as the whole sequence space \( F^{\nN} \).
:::
