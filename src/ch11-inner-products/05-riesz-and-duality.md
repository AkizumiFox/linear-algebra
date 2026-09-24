# The Riesz Representation Theorem

Chapter 5 built the dual space \( V^{*} \) of all linear functionals on \( V \), proved that \( \dim V^{*} = \dim V \) in finite dimension, and then delivered a warning: the resulting isomorphism \( V \cong V^{*} \) is not canonical. Every basis of \( V \) gives one, different bases give different ones, and no argument singles out a preferred choice (@cor-dimension-dual-space, and the contrast with the natural map \( \ev_V \colon V \to V^{**} \) of @thm-evaluation-natural). The chapter closed by promising that an inner product would supply the missing ingredient. This section keeps the promise.

The mechanism is simple to state. Fix \( \w \in V \) and let \( \varphi_{\w}(\v) = \inner{\v}{\w} \). Because the inner product is linear in the **first** slot, \( \varphi_{\w} \) is a linear functional. The Riesz Representation Theorem says that in finite dimension there are no others.

Throughout, \( V \) is a finite-dimensional inner product space over \( F = \nR \) or \( F = \nC \), unless the text says otherwise.

## Every functional is an inner product

In \( F^n \), @thm-functionals-on-fn already told us that every functional has the form \( \x \mapsto a_1x_1 + \dots + a_nx_n \) for a unique row of coefficients. With the standard inner product \( \inner{\x}{\y} = \sum_i x_i\conj{y_i} \), that reads \( \varphi(\x) = \inner{\x}{\w} \) with \( \w = (\conj{a_1}, \dots, \conj{a_n}) \). So in coordinates the theorem is a restatement of a fact we already have; the content is that it survives the removal of coordinates.

::: {#thm-riesz-representation}
[Riesz Representation Theorem]

Let \( V \) be a finite-dimensional inner product space over \( F \) and let \( \varphi \in V^{*} \). Then there is a **unique** \( \w \in V \) such that
\[
\varphi(\v) = \inner{\v}{\w} \qquad \text{for every } \v \in V .
\]
If \( (\e_1, \dots, \e_n) \) is any orthonormal basis of \( V \), then \( \w = \sum_{i=1}^{n} \conj{\varphi(\e_i)}\,\e_i \).
:::

::: {.idea}
Fix an orthonormal basis. Then a linear functional is determined by the \( n \) numbers \( \varphi(\e_i) \), and a vector is determined by its \( n \) coordinates, which @thm-orthonormal-coordinates reads off as inner products. Matching the two lists tells us what \( \w \) must be, and the only care needed is the conjugate: \( \w \) sits in the second slot, so its coordinates come out conjugated. Uniqueness is the standard move — if two vectors pair identically with everything, subtract and pair the difference with itself.
:::

::: {.proof}
*Existence.* Let \( (\e_1, \dots, \e_n) \) be an orthonormal basis of \( V \), which exists by @thm-gram-schmidt, and put
\[
\w = \sum_{i=1}^{n} \conj{\varphi(\e_i)}\,\e_i .
\]
For each \( j \), conjugate-linearity in the second slot and \( \inner{\e_j}{\e_i} = \delta_{ij} \) give
\[
\inner{\e_j}{\w} = \sum_{i=1}^{n} \conj{\conj{\varphi(\e_i)}}\,\inner{\e_j}{\e_i} = \varphi(\e_j).
\]
So the two linear functionals \( \v \mapsto \inner{\v}{\w} \) and \( \varphi \) agree on a basis, hence are equal by @thm-linear-transform-basis. (The first is linear because the inner product is linear in the first slot.)

*Uniqueness.* Suppose \( \inner{\v}{\w} = \inner{\v}{\w'} \) for every \( \v \). Then \( \inner{\v}{\w - \w'} = 0 \) for every \( \v \), by additivity in the second slot. Taking \( \v = \w - \w' \) gives \( \norm{\w - \w'}^2 = 0 \), so \( \w = \w' \) by positive definiteness.
:::

Call \( \w \) the **Riesz vector** of \( \varphi \). The formula is worth reading twice: the coordinates of \( \w \) in an orthonormal basis are the conjugates of the values of \( \varphi \) on that basis. Over \( \nR \) the conjugation is invisible, which is why real textbooks can omit it and complex ones cannot.

:::: {#exm-riesz-vectors}
[Two Riesz vectors]

::: {.enumerate options="label=(\alph*)"}
1. On \( V = \nR[x]_{\le 1} \) with \( \inner{p}{q} = \int_{0}^{1} p(t)q(t)\,\dd t \), find the Riesz vector of \( \varphi(p) = p(0) \).
2. On \( V = M_n(\nC) \) with the Frobenius inner product \( \inner{\A}{\B} = \tr(\B^{*}\A) \), find the Riesz vector of \( \varphi(\A) = \tr\A \).
:::
::::

::: {.solution}
(a) We look for \( w = a + bx \) with \( \inner{p}{w} = p(0) \) for all \( p \). By linearity it is enough to impose this on the basis \( (1, x) \):
\[
\int_{0}^{1}(a + bt)\,\dd t = a + \tfrac{b}{2} = 1, \qquad \int_{0}^{1} t(a + bt)\,\dd t = \tfrac{a}{2} + \tfrac{b}{3} = 0 .
\]
The second equation gives \( a = -\tfrac23 b \); substituting into the first gives \( -\tfrac23 b + \tfrac12 b = -\tfrac16 b = 1 \), so \( b = -6 \) and \( a = 4 \). Hence \( w = 4 - 6x \).

*Check.* \( \int_0^1 (4 - 6t)\,\dd t = 4 - 3 = 1 \) and \( \int_0^1 t(4 - 6t)\,\dd t = 2 - 2 = 0 \), as required; and for a general \( p = c + dx \) the pairing gives \( c\cdot 1 + d\cdot 0 = c = p(0) \). Note how little \( w \) resembles "evaluation at \( 0 \)": the Riesz vector is manufactured by the inner product, not by the point \( 0 \).

(b) We look for \( \W \) with \( \tr(\W^{*}\A) = \tr\A \) for every \( \A \). Taking \( \W = \I_n \) works, since \( \I_n^{*} = \I_n \) and \( \tr(\I_n\A) = \tr\A \). By uniqueness, \( \W = \I_n \) is the answer. (This example was not solved by the basis formula, but by guessing and then invoking uniqueness — a legitimate and often faster route.)
:::

## The Riesz map, and the data Chapter 5 was missing

Uniqueness in @thm-riesz-representation lets us read the theorem as a statement about a map.

::: {#cor-riesz-isomorphism}
[The Riesz map]

Let \( V \) be a finite-dimensional inner product space over \( F \). Define
\[
\Phi \colon V \to V^{*}, \qquad \Phi(\w) = \inner{\cdot}{\w} .
\]
Then \( \Phi \) is a bijection, and for all \( \w, \w' \in V \) and \( c \in F \),
\[
\Phi(\w + \w') = \Phi(\w) + \Phi(\w'), \qquad \Phi(c\w) = \conj{c}\,\Phi(\w).
\]
In particular \( \Phi \) is an isomorphism of vector spaces when \( F = \nR \), and is **conjugate-linear** when \( F = \nC \).
:::

::: {.proof}
Each \( \Phi(\w) \) lies in \( V^{*} \) because the inner product is linear in the first slot. Surjectivity is the existence half of @thm-riesz-representation and injectivity is the uniqueness half (if \( \Phi(\w) = \Phi(\w') \), then \( \w = \w' \)). For the two rules, evaluate at an arbitrary \( \v \): additivity in the second slot gives \( \inner{\v}{\w + \w'} = \inner{\v}{\w} + \inner{\v}{\w'} \), and conjugate-homogeneity in the second slot gives \( \inner{\v}{c\w} = \conj{c}\inner{\v}{\w} \). Over \( \nR \) we have \( \conj{c} = c \), so \( \Phi \) is linear, and a linear bijection is an isomorphism (@thm-bijective-iff-invertible).
:::

This is the payoff Chapter 5 promised. There, \( V \cong V^{*} \) was proved by choosing a basis \( \sB \) and sending \( \v_i \mapsto \varphi_i \), and the warning was that the isomorphism changes when \( \sB \) does: a vector does not come with "its" functional. Here \( \Phi \) is written down with no basis at all. It is not free of choices — it depends on \( \inner{\cdot}{\cdot} \) — but the choice has been made once, in advance, and it is a choice of *geometry* rather than of coordinates. **The inner product is exactly the extra data that turns \( V \cong V^{*} \) from a counting fact into a formula.**

The two descriptions fit together neatly. Let \( \sB = (\v_1, \dots, \v_n) \) be an **orthonormal** basis of \( V \), with dual basis \( (\varphi_1, \dots, \varphi_n) \) (@thm-dual-basis). Then \( \Phi(\v_i) \) is the functional \( \v \mapsto \inner{\v}{\v_i} \), which sends \( \v_j \) to \( \delta_{ij} \); that is,
\[
\Phi(\v_i) = \varphi_i \qquad (i = 1, \dots, n),
\]
over either field. Over \( \nR \), where \( \Phi \) is linear, this says that \( \Phi \) **is** Chapter 5's basis-dependent isomorphism \( \v_i \mapsto \varphi_i \), for the inner product that declares \( \sB \) orthonormal. Choosing a basis and choosing an inner product are two ways of supplying the same missing data.

::: {.check}
Let \( \sB = (\v_1, \dots, \v_n) \) be an orthonormal basis of a **complex** inner product space and let \( (\varphi_1, \dots, \varphi_n) \) be its dual basis. What is the Riesz vector of \( i\varphi_1 \)?
:::

::: {.solution}
By the identity \( \Phi(\v_i) = \varphi_i \) above, which holds over \( \nC \) as well, \( \varphi_1 \) has Riesz vector \( \v_1 \). For \( i\varphi_1 \), use conjugate-homogeneity in reverse: \( \Phi(-i\v_1) = \conj{(-i)}\Phi(\v_1) = i\varphi_1 \). So the Riesz vector of \( i\varphi_1 \) is \( -i\v_1 \), not \( i\v_1 \). Alternatively, apply the formula of @thm-riesz-representation: the coordinates of the Riesz vector are \( \conj{(i\varphi_1)(\v_j)} = \conj{i\delta_{1j}} = -i\delta_{1j} \).
:::

::: {.warning}
**Over \( \nC \), the Riesz map is not linear, so it is not an isomorphism of complex vector spaces.** It is a bijection, and it is linear over \( \nR \), but \( \Phi(i\w) = -i\Phi(\w) \). Complex spaces \( V \) and \( V^{*} \) are still isomorphic — they have the same dimension — but the isomorphism produced by an inner product is the conjugate-linear \( \Phi \). Most of what we do with \( \Phi \) (Section 6 builds the adjoint from it) is unaffected, because the conjugation cancels when \( \Phi \) is used twice.
:::

::: {.warning}
**The Riesz vector depends on the inner product, not on \( \varphi \) alone.** On \( \nR^2 \) let \( \varphi(\x) = x_1 + x_2 \). With the dot product, \( \varphi(\x) = \inner{\x}{(1, 1)} \), so \( \w = (1, 1) \). With the weighted inner product \( \inner{\x}{\y} = 2x_1y_1 + x_2y_2 \), we need \( 2w_1 = 1 \) and \( w_2 = 1 \), so \( \w = \bigl(\tfrac12, 1\bigr) \). Same functional, different representing vector. Whenever two inner products are in play, the notation must say which \( \Phi \) is meant.
:::

## Annihilators become orthogonal complements

Section 3 warned that the annihilator \( U^{0} \subseteq V^{*} \) and the orthogonal complement \( U^{\perp} \subseteq V \) are different objects that happen to have the same dimension. The Riesz map explains the coincidence: it carries one onto the other.

::: {#thm-annihilator-vs-orthogonal-complement}
[Perp corresponds to the annihilator]

Let \( V \) be a finite-dimensional inner product space over \( F \), let \( U \) be a subspace and let \( \Phi \) be the Riesz map. Then
\[
\Phi(U^{\perp}) = U^{0} .
\]
Equivalently, a functional \( \varphi \in V^{*} \) annihilates \( U \) if and only if its Riesz vector lies in \( U^{\perp} \).
:::

::: {.proof}
Let \( \w \in V \). Then
\[
\Phi(\w) \in U^{0} \iff \inner{\u}{\w} = 0 \text{ for every } \u \in U \iff \w \in U^{\perp},
\]
the first equivalence being the definition of the annihilator (@def-annihilator) applied to the functional \( \Phi(\w) = \inner{\cdot}{\w} \), and the second the definition of the orthogonal complement (@def-orthogonal-complement). Since \( \Phi \) is a bijection (@cor-riesz-isomorphism), the set \( \Phi(U^{\perp}) \) is therefore exactly \( U^{0} \).
:::

The dimension count now has a reason rather than a coincidence: \( \dim U^{0} = \dim V - \dim U \) (@thm-dimension-annihilator) and \( \dim U^{\perp} = \dim V - \dim U \) (@thm-orthogonal-decomposition (c)) agree because the two spaces correspond under a bijection. (Over \( \nC \) the bijection is only conjugate-linear, but a conjugate-linear bijection still carries subspaces to subspaces of the same dimension, since \( c\Phi(\w) = \Phi(\conj{c}\w) \).)

Here is the correspondence in \( \nR^3 \). Let \( U = \Span((1, 2, 0)) \) with the dot product. Then \( U^{\perp} = \{ (a, b, c) : a + 2b = 0 \} = \Span\bigl((2, -1, 0), (0, 0, 1)\bigr) \), and \( U^{0} \) consists of the functionals \( \x \mapsto \alpha x_1 + \beta x_2 + \gamma x_3 \) with \( \alpha + 2\beta = 0 \), spanned by \( 2x_1 - x_2 \) and \( x_3 \). These are precisely \( \Phi((2, -1, 0)) \) and \( \Phi((0, 0, 1)) \).

Section 6 uses @thm-annihilator-vs-orthogonal-complement in the same way for maps: the dual map \( T' \colon W^{*} \to V^{*} \) of Chapter 5 and the adjoint \( T^{*} \colon W \to V \) are the same map, read through the two Riesz maps.

## What happens in infinite dimension

The proof used an orthonormal basis of the whole of \( V \), so finite dimension was essential, and the theorem genuinely fails without it.

::: {#exm-functional-with-no-riesz-vector}
[A functional with no Riesz vector]

Let \( V = \nR[x] \) with the coefficient inner product \( \inner{p}{q} = \sum_{k \ge 0} a_kb_k \) for \( p = \sum_k a_kx^k \) and \( q = \sum_k b_kx^k \) (a finite sum, and an inner product by @exr-orthogonal-complements-and-projections-c2 (a)). Show that \( \varphi(p) = p(1) \) has no Riesz vector.
:::

::: {.solution}
Suppose \( w = \sum_{k} b_kx^k \) satisfied \( \inner{p}{w} = p(1) \) for every \( p \in V \). Taking \( p = x^i \) gives
\[
b_i = \inner{x^i}{w} = \varphi(x^i) = 1^i = 1 \qquad \text{for every } i \ge 0 .
\]
So every coefficient of \( w \) equals \( 1 \). But a polynomial has only finitely many non-zero coefficients, so no such \( w \) exists.
:::

What fails is not "infinite dimension" as a slogan. Two things are missing at once, and the same example shows both. First, \( V \) has gaps: @exr-orthogonal-complements-and-projections-c2 exhibits polynomials \( p_m \in \ker\varphi \) with \( \norm{p_m - 1} = 1/\sqrt m \), so the vectors \( p_m \) crowd around the polynomial \( 1 \) without any limit being forced to lie in \( \ker\varphi \). Second, \( \varphi \) is wildly discontinuous with respect to \( \norm{\cdot} \): along the same sequence, \( \varphi(p_m) = 0 \) for every \( m \), while \( \varphi(1) = 1 \).

Repairing both defects — completing the space, and restricting attention to functionals \( \varphi \) with \( |\varphi(\v)| \le C\norm{\v} \) — restores the theorem. That statement is the Riesz representation theorem for Hilbert spaces, and it belongs to analysis, not to linear algebra; we record its existence and go no further. What survives here with no hypotheses at all is the easy direction: for every \( \w \in V \), the map \( \inner{\cdot}{\w} \) *is* a linear functional. Only the converse needs finite dimension.

## Exercises

### A. Check your understanding

:::: {#exr-riesz-and-duality-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the Riesz Representation Theorem, including every hypothesis.
2. Write down the formula for the Riesz vector of \( \varphi \) in terms of an orthonormal basis, and say where the conjugate comes from.
3. True or false: over \( \nC \), the Riesz map \( \Phi \colon V \to V^{*} \) is a linear isomorphism. Justify your answer.
4. In what sense does an inner product answer the question Chapter 5 left open about \( V \cong V^{*} \)?
5. Under \( \Phi \), which subspace of \( V^{*} \) corresponds to \( U^{\perp} \)?
6. Give an example showing that the theorem fails in infinite dimension.
:::
::::

::: {.solution}
(a) If \( V \) is a **finite-dimensional** inner product space over \( \nR \) or \( \nC \) and \( \varphi \in V^{*} \), then there is a unique \( \w \in V \) with \( \varphi(\v) = \inner{\v}{\w} \) for all \( \v \in V \) (@thm-riesz-representation).

(b) \( \w = \sum_i \conj{\varphi(\e_i)}\e_i \) for any orthonormal basis \( (\e_1, \dots, \e_n) \). The conjugate appears because \( \w \) occupies the second slot, where scalars come out conjugated: to make \( \inner{\e_j}{\w} \) equal \( \varphi(\e_j) \), the coefficient of \( \e_j \) in \( \w \) must be \( \conj{\varphi(\e_j)} \).

(c) False. \( \Phi \) is a bijection, but \( \Phi(c\w) = \conj{c}\Phi(\w) \), so it is conjugate-linear and not \( \nC \)-linear (@cor-riesz-isomorphism). It is linear over \( \nR \), and over \( \nR \) it is an isomorphism.

(d) Chapter 5 showed \( V \cong V^{*} \) by counting dimensions, with an isomorphism depending on a chosen basis and no preferred choice available (@cor-dimension-dual-space). An inner product supplies a specific map \( \Phi(\w) = \inner{\cdot}{\w} \), written without reference to any basis. The inner product is the extra data; picking an orthonormal basis and picking an inner product that makes a given basis orthonormal are the same act.

(e) \( U^{0} \), the annihilator of \( U \) (@thm-annihilator-vs-orthogonal-complement).

(f) On \( \nR[x] \) with the coefficient inner product, \( \varphi(p) = p(1) \) has no Riesz vector: such a vector would need every coefficient equal to \( 1 \) (@exm-functional-with-no-riesz-vector).
:::

### B. Practice

:::: {#exr-riesz-and-duality-b1}
[B1: Riesz vectors for evaluation]

On \( V = \nR[x]_{\le 2} \) use the node inner product \( \inner{p}{q} = p(-1)q(-1) + p(0)q(0) + p(1)q(1) \). Find the Riesz vectors of \( \varphi(p) = p(0) \) and of \( \psi(p) = p(1) \).
::::

::: {.solution}
Since \( -1, 0, 1 \) are three distinct nodes and \( \dim V = 3 \), a polynomial of \( V \) is determined by its values there (@thm-interpolation-unique). Writing \( w \) for a candidate Riesz vector of \( \varphi \), the requirement \( \inner{p}{w} = p(0) \) reads
\[
p(-1)w(-1) + p(0)w(0) + p(1)w(1) = p(0) \qquad \text{for all } p \in V .
\]
Taking for \( p \) the three Lagrange polynomials at the nodes, which have value \( 1 \) at one node and \( 0 \) at the others (@def-lagrange-basis), the three equations become \( w(-1) = 0 \), \( w(0) = 1 \), \( w(1) = 0 \). The unique quadratic with those values is \( w = 1 - x^2 \).

For \( \psi \) the same argument gives \( w(-1) = 0 \), \( w(0) = 0 \), \( w(1) = 1 \), whose interpolant is \( w = \tfrac12 x(x + 1) \).

*Check.* For \( p = 3 + 2x - x^2 \) we get \( p(-1) = 0 \), \( p(0) = 3 \), \( p(1) = 4 \). Pairing with \( 1 - x^2 \), whose values are \( 0, 1, 0 \), gives \( 3 = p(0) \); pairing with \( \tfrac12x(x+1) \), whose values are \( 0, 0, 1 \), gives \( 4 = p(1) \).
:::

:::: {#exr-riesz-and-duality-b2}
[B2: Riesz vectors on matrices]

On \( M_n(\nC) \) with the Frobenius inner product \( \inner{\A}{\B} = \tr(\B^{*}\A) \), find the Riesz vector of:

::: {.enumerate options="label=(\alph*)"}
1. \( \varphi(\A) = a_{12} \) (assume \( n \ge 2 \));
2. \( \varphi_{\C}(\A) = \tr(\C\A) \), for a fixed \( \C \in M_n(\nC) \).
:::
::::

::: {.solution}
(a) Let \( \E_{12} \) be the matrix unit with a \( 1 \) in position \( (1, 2) \) and zeros elsewhere. Then \( \E_{12}^{*} = \E_{21} \), and \( (\E_{21}\A)_{kk} = \sum_j (\E_{21})_{kj}a_{jk} \), which is \( 0 \) unless \( k = 2 \), where it equals \( a_{12} \). Hence \( \tr(\E_{12}^{*}\A) = a_{12} = \varphi(\A) \), and by uniqueness in @thm-riesz-representation the Riesz vector is \( \E_{12} \).

(b) We need \( \W \) with \( \tr(\W^{*}\A) = \tr(\C\A) \) for all \( \A \). Taking \( \W^{*} = \C \), that is \( \W = \C^{*} \), works. By uniqueness it is the only answer. Part (a) is the case \( \C = \E_{21} \), and the example in the text is the case \( \C = \I_n \).
:::

:::: {#exr-riesz-and-duality-b3}
[B3: The correspondence in \( \nR^4 \)]

In \( \nR^4 \) with the dot product, let \( U = \Span\bigl((1, 0, 1, 0), (0, 1, 0, 1)\bigr) \). Find a basis of \( U^{\perp} \) and a basis of \( U^{0} \), and verify that \( \Phi \) carries the first to the second.
::::

::: {.solution}
A vector \( (a, b, c, d) \) lies in \( U^{\perp} \) exactly when \( a + c = 0 \) and \( b + d = 0 \) (@prp-orthogonal-complement-subspace, testing against the two spanning vectors). So
\[
U^{\perp} = \Span\bigl((1, 0, -1, 0),\ (0, 1, 0, -1)\bigr),
\]
of dimension \( 2 = 4 - 2 \).

A functional \( \varphi(\x) = \alpha x_1 + \beta x_2 + \gamma x_3 + \delta x_4 \) lies in \( U^{0} \) exactly when it kills both spanning vectors, that is, when \( \alpha + \gamma = 0 \) and \( \beta + \delta = 0 \). So \( U^{0} = \Span(\varphi_1, \varphi_2) \) with
\[
\varphi_1(\x) = x_1 - x_3, \qquad \varphi_2(\x) = x_2 - x_4 .
\]
Over \( \nR \), \( \Phi(\w)(\x) = \inner{\x}{\w} = \sum_i x_iw_i \), so \( \Phi((1,0,-1,0)) = \varphi_1 \) and \( \Phi((0,1,0,-1)) = \varphi_2 \). Since \( \Phi \) is linear over \( \nR \) and bijective, it carries the span of the two vectors onto the span of the two functionals, confirming @thm-annihilator-vs-orthogonal-complement.
:::

### C. Going deeper

:::: {#exr-riesz-and-duality-c1}
[C1: Riesz without an orthonormal basis]

Let \( V \) be a finite-dimensional inner product space and let \( \varphi \in V^{*} \) be non-zero. Write \( K = \ker\varphi \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \dim K^{\perp} = 1 \).
2. Let \( \u \) span \( K^{\perp} \) with \( \norm{\u} = 1 \). Prove that \( \w = \conj{\varphi(\u)}\,\u \) satisfies \( \varphi(\v) = \inner{\v}{\w} \) for all \( \v \in V \).
3. Deduce @thm-riesz-representation, including the case \( \varphi = 0 \).
:::

*Hint for (b): split \( \v \) using \( V = K \oplus K^{\perp} \).*
::::

::: {.solution}
(a) Since \( \varphi \neq 0 \), its image is a non-zero subspace of the \( 1 \)-dimensional space \( F \), so \( \im\varphi = F \) and \( \rank\varphi = 1 \). By @thm-rank-nullity, \( \dim K = \dim V - 1 \), and by @thm-orthogonal-decomposition (c), \( \dim K^{\perp} = \dim V - \dim K = 1 \).

(b) By @thm-orthogonal-decomposition (a), \( V = K \oplus K^{\perp} \), so each \( \v \in V \) is \( \v = \k + c\u \) with \( \k \in K \) and \( c \in F \). Then \( \varphi(\v) = \varphi(\k) + c\varphi(\u) = c\varphi(\u) \). On the other side,
\[
\inner{\v}{\w} = \inner{\k + c\u}{\conj{\varphi(\u)}\u} = \varphi(\u)\bigl(\inner{\k}{\u} + c\inner{\u}{\u}\bigr) = \varphi(\u)\,c,
\]
using conjugate-homogeneity in the second slot (which conjugates \( \conj{\varphi(\u)} \) back to \( \varphi(\u) \)), then \( \inner{\k}{\u} = 0 \) because \( \u \in K^{\perp} \) and \( \k \in K \), and \( \inner{\u}{\u} = \norm{\u}^2 = 1 \). The two sides agree.

(c) If \( \varphi = 0 \), then \( \w = \0 \) represents it. If \( \varphi \neq 0 \), part (a) supplies a unit vector \( \u \) spanning the line \( K^{\perp} \) — any non-zero vector of that line divided by its norm — and part (b) supplies \( \w \). Uniqueness is unchanged: if \( \inner{\v}{\w} = \inner{\v}{\w'} \) for all \( \v \), take \( \v = \w - \w' \) to get \( \norm{\w - \w'}^2 = 0 \). Note that this proof never mentions a basis of \( V \); it uses only the orthogonal decomposition along the hyperplane \( \ker\varphi \).
:::

:::: {#exr-riesz-and-duality-c2}
[C2: Evaluation at \( 0 \) is not represented]

Let \( V = \nR[x] \) with \( \inner{p}{q} = \int_{0}^{1}p(t)q(t)\,\dd t \), and let \( \varphi(p) = p(0) \). Suppose, for a contradiction, that \( w = \sum_{j=0}^{d} c_jx^j \) satisfied \( \inner{p}{w} = p(0) \) for every \( p \in V \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \displaystyle\sum_{j=0}^{d} \frac{c_j}{k + j + 1} = 0 \) for every integer \( k \ge 1 \), and that the same sum equals \( 1 \) for \( k = 0 \).
2. Let \( N(s) = \sum_{j=0}^{d} c_j \prod_{i \neq j}(s + i + 1) \), the product running over \( i \in \{0, \dots, d\}\setminus\{j\} \). Show that \( N(k) = 0 \) for every integer \( k \ge 1 \), and deduce that \( N \) is the zero polynomial.
3. Deduce that every \( c_j = 0 \), and hence a contradiction.
:::
::::

::: {.solution}
(a) Take \( p = x^k \). Then \( p(0) = 0 \) for \( k \ge 1 \) and \( p(0) = 1 \) for \( k = 0 \), while
\[
\inner{x^k}{w} = \int_{0}^{1} t^k\sum_{j=0}^{d}c_jt^j\,\dd t = \sum_{j=0}^{d} c_j\int_0^1 t^{k+j}\,\dd t = \sum_{j=0}^{d}\frac{c_j}{k + j + 1}.
\]

(b) For an integer \( k \ge 1 \), multiply the identity of (a) by \( \prod_{i=0}^{d}(k + i + 1) \), a non-zero number. Each term \( c_j/(k + j + 1) \) becomes \( c_j\prod_{i \neq j}(k + i + 1) \), so the result is exactly \( N(k) = 0 \). Thus the polynomial \( N \), of degree at most \( d \), has the infinitely many distinct roots \( 1, 2, 3, \dots \). A non-zero polynomial of degree \( d \) has at most \( d \) distinct roots (@cor-root-bound-general), so \( N = 0 \).

(c) Evaluate \( N \) at \( s = -(j_0 + 1) \) for a fixed \( j_0 \in \{0, \dots, d\} \). Every product \( \prod_{i \neq j}(s + i + 1) \) with \( j \neq j_0 \) contains the factor \( s + j_0 + 1 = 0 \) and so vanishes; the term \( j = j_0 \) contributes \( c_{j_0}\prod_{i \neq j_0}(i - j_0) \), and that product is non-zero because the factors \( i - j_0 \) are non-zero integers. Since \( N = 0 \), we get \( c_{j_0} = 0 \). This holds for every \( j_0 \), so \( w = 0 \). But then the case \( k = 0 \) of (a) reads \( 0 = 1 \), a contradiction. Hence no Riesz vector exists.

The moral matches @exm-functional-with-no-riesz-vector: point evaluation is a perfectly good linear functional, but on an infinite-dimensional space it is not represented by any vector, whichever of these two inner products we use.
:::
