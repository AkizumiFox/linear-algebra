# Orthogonal Polynomials

Section 2 ran Gram–Schmidt on \( (1, x, x^2) \) with \( \inner{p}{q} = \int_{-1}^{1} pq \), and stopped at degree \( 2 \) only because the space did (@exm-gram-schmidt-legendre). Nothing in the process cared. Feed it \( (1, x, x^2, x^3, \dots) \) and it returns an infinite orthogonal sequence, one polynomial of each degree. Three things make such sequences worth a section. Each member is computable from the two before it. Each member of degree \( k \) has \( k \) distinct real roots inside the interval. And those roots are the best possible points at which to sample a function to estimate its integral. The first fact rests on one small identity; the other two rest on the first.

**Throughout this section the field is \( \nR \).**

## Two ways to make an inner product on polynomials

Both constructions we need appeared in Section 1.

**From a weight.** Fix an interval with endpoints \( -\infty \le a < b \le \infty \) and a **weight** \( w \): a function continuous and **strictly positive** on the open interval \( (a, b) \), with \( \int_a^b \lvert t \rvert^k w(t)\,\dd t \) finite for every \( k \in \nN \). Define
\[
\inner{p}{q} = \int_a^b p(t)\,q(t)\,w(t)\,\dd t .
\]
Finiteness of the moments makes this a real number for all \( p, q \in \nR[x] \), and bilinearity and symmetry come from linearity of the integral. For positivity, let \( p \ne 0 \). Then \( p^2w \) is continuous and \( \ge 0 \) on \( (a, b) \), and \( > 0 \) off the finitely many roots of \( p \) (@cor-root-bound-general), so \( \inner{p}{p} > 0 \). That last step is the one calculus fact this section leans on: a continuous non-negative function on an interval whose integral is \( 0 \) vanishes identically. As in @def-inner-product it follows from the local fact that a continuous function non-zero at a point stays bounded away from \( 0 \) on a small interval around it, which then contributes a positive amount to the integral.

**From nodes.** Fix distinct \( c_0 < \dots < c_n \) in \( \nR \) and put \( \inner{p}{q} = \sum_{i=0}^{n} p(c_i)q(c_i) \). Section 1 checked that this is an inner product **on \( \nR[x]_{\le n} \)**, positivity coming from the root bound. It is not one on \( \nR[x] \): the polynomial \( (x - c_0)\cdots(x - c_n) \) is non-zero and pairs with itself to give \( 0 \). So in the node case everything below stops at degree \( n \).

The two constructions share one property, and it is the engine of the section.

::: {#prp-multiplication-by-x-symmetric}
[Multiplication by x is symmetric]

Let \( \inner{\cdot}{\cdot} \) be an inner product on \( \nR[x] \) coming from a weight, or the node inner product on \( \nR[x]_{\le n} \). Then
\[
\inner{xp}{q} = \inner{p}{xq}
\]
for all polynomials \( p, q \) in the space (in the node case, for all \( p, q \) of degree at most \( n - 1 \), so that \( xp \) and \( xq \) still lie in it).
:::

::: {.proof}
In the weight case both sides equal \( \int_a^b t\,p(t)q(t)w(t)\,\dd t \), and in the node case both sides equal \( \sum_{i=0}^{n} c_i\,p(c_i)q(c_i) \).
:::

The proof is one line, but the statement is not a triviality: multiplication by \( x \) moves from one slot to the other for free. That is exactly the identity \( \inner{T\u}{\v} = \inner{\u}{T\v} \) defining a **self-adjoint** operator (@def-self-adjoint), and it is the reason the recurrence below has three terms instead of \( k + 2 \).

::: {.warning}
**Multiplication by \( x \) is not an operator on \( \nR[x]_{\le n} \).** It raises degree, so it maps that space out of itself; on \( \nR[x] \) it is an operator, but there the space is infinite-dimensional, and @def-self-adjoint was stated for a finite-dimensional one. "Self-adjoint" is here a name for @prp-multiplication-by-x-symmetric, not a literal application of the definition. It is the identity, not the name, that the proofs use.
:::

## Orthogonal polynomial sequences

Applied to the independent list \( (1, x, x^2, \dots) \), Gram–Schmidt never stalls. What comes out is one polynomial of each degree, pairwise orthogonal, and that combination deserves a name.

*An orthogonal polynomial sequence is one polynomial of every degree, no two of them pairing to anything but zero.*

:::: {#def-orthogonal-polynomial-sequence}
[Orthogonal Polynomial Sequence]

Let \( \inner{\cdot}{\cdot} \) be an inner product on \( \nR[x] \), or on \( \nR[x]_{\le n} \). An **orthogonal polynomial sequence** for it is a sequence \( p_0, p_1, p_2, \dots \) of polynomials (a finite list \( p_0, \dots, p_n \) in the second case) such that

::: {.enumerate options="label=(OP\arabic*)"}
1. \( \deg p_k = k \) for **every** index \( k \);
2. \( \inner{p_j}{p_k} = 0 \) whenever \( j \ne k \).
:::

The sequence is **monic** if every \( p_k \) has leading coefficient \( 1 \).
::::

In words. (OP1) says one polynomial of each degree: no gaps, no repeats, no accidental drop in degree. (OP2) says the members are pairwise orthogonal. Together they say more than either alone, because by (OP1) the list \( (p_0, \dots, p_{k-1}) \) is a basis of \( \nR[x]_{\le k-1} \), so (OP2) upgrades to
\[
\inner{p_k}{q} = 0 \qquad \text{for every } q \in \nR[x]_{\le k-1},
\]
and that is the form in which the condition always gets used.

Two things need checking: that such a sequence exists, and that fixing the scale pins it down.

::: {#prp-monic-orthogonal-sequence}
[Existence and uniqueness of the monic sequence]

Let \( \inner{\cdot}{\cdot} \) be an inner product on \( \nR[x] \). For each \( k \in \nN \) there is **exactly one** monic \( p_k \) of degree \( k \) with \( \inner{p_k}{q} = 0 \) for every \( q \in \nR[x]_{\le k-1} \). These \( p_k \) form the unique monic orthogonal polynomial sequence, and \( (p_0, \dots, p_k) \) is an orthogonal basis of \( \nR[x]_{\le k} \) for every \( k \). The same holds on \( \nR[x]_{\le n} \) for \( k \le n \).
:::

::: {.idea}
Existence is Gram–Schmidt, once we know the \( k \)-th output really has degree \( k \); it does, because it lies in \( \nR[x]_{\le k} \) but not in the span of its predecessors, which is \( \nR[x]_{\le k-1} \). Uniqueness is the standard move: two candidates differ by a polynomial of lower degree that is orthogonal to everything of lower degree, hence to itself.
:::

::: {.proof}
*Existence.* The list \( (1, x, \dots, x^k) \) is independent, so @thm-gram-schmidt applies and returns an orthonormal list \( (\e_0, \dots, \e_k) \) with \( \Span(\e_0, \dots, \e_j) = \Span(1, x, \dots, x^j) = \nR[x]_{\le j} \) for every \( j \le k \). Fix \( j \). Then \( \e_j \in \nR[x]_{\le j} \), and \( \e_j \notin \nR[x]_{\le j-1} = \Span(\e_0, \dots, \e_{j-1}) \), since an orthonormal list is independent (@thm-orthogonal-independent). Hence \( \deg \e_j = j \) exactly. Let \( a_j \ne 0 \) be its leading coefficient and put \( p_j = \e_j/a_j \), monic of degree \( j \). For \( q \in \nR[x]_{\le j-1} = \Span(\e_0, \dots, \e_{j-1}) \) we get \( \inner{p_j}{q} = 0 \) by orthogonality of the list.

*Uniqueness.* Suppose \( p \) and \( p' \) are both monic of degree \( k \) and orthogonal to every element of \( \nR[x]_{\le k-1} \). Their leading terms cancel, so \( p - p' \in \nR[x]_{\le k-1} \). Therefore \( \inner{p - p'}{p - p'} = \inner{p}{p - p'} - \inner{p'}{p - p'} = 0 \), and positive definiteness gives \( p = p' \).

Finally, \( (p_0, \dots, p_k) \) is an orthogonal list of non-zero vectors, hence independent (@thm-orthogonal-independent), with \( k + 1 = \dim \nR[x]_{\le k} \) members, hence a basis (@thm-right-size-basis).
:::

**Examples.** For \( \inner{p}{q} = \int_{-1}^{1} pq \) the first three monic members are \( 1 \), \( x \), \( x^2 - \tfrac13 \) (@exm-gram-schmidt-legendre); these are the monic **Legendre polynomials**. For the node inner product with nodes \( -1, 0, 1 \) on \( \nR[x]_{\le 2} \) we have \( \inner{1}{1} = 3 \), \( \inner{x}{1} = 0 \), \( \inner{x}{x} = 2 \), \( \inner{x^2}{1} = 2 \), \( \inner{x^2}{x} = 0 \), so \( p_0 = 1 \), \( p_1 = x \), \( p_2 = x^2 - \tfrac23 \) — and there the sequence ends, since \( \nR[x]_{\le 2} \) holds nothing of degree \( 3 \). The degenerate member is always \( p_0 = 1 \), the only monic polynomial of degree \( 0 \), with an empty condition on it.

**A non-example by minimal change.** Replace the Legendre \( p_2 = x^2 - \tfrac13 \) by \( \tilde p_2 = x^2 + x - \tfrac13 \). Still monic of degree \( 2 \), so (OP1) survives; but \( \inner{\tilde p_2}{x} = \inner{x}{x} = \tfrac23 \ne 0 \), so (OP2) fails. Adding a multiple of a lower member is exactly the freedom orthogonality removes.

**Why monic?** Rescaling each \( p_k \) by a non-zero \( \lambda_k \) gives another orthogonal polynomial sequence, so a normalization has to be chosen, and traditions differ: the classical Legendre polynomials \( P_k \) are fixed by \( P_k(1) = 1 \), and Gram–Schmidt as run in Section 2 fixes \( \norm{p_k} = 1 \). Monic is the convenient choice here, because it is the one for which the recurrence below needs no extra factor.

::: {.warning}
**The sequence belongs to the inner product, not to the polynomials.** "The orthogonal polynomials" is meaningless without a weight and an interval. Exercise B2 of Section 2 (@exr-orthonormal-bases-b2) ran the same process with \( \int_0^1 \) instead of \( \int_{-1}^{1} \) and got \( 1 \), \( x - \tfrac12 \), \( x^2 - x + \tfrac16 \): same degrees, different polynomials.
:::

::: {.check}
For \( \inner{p}{q} = \int_{-1}^{1} pq \), how many polynomials of degree \( 2 \) with \( \norm{p} = 1 \) are orthogonal to \( \nR[x]_{\le 1} \)? Write them down.
:::

::: {.solution}
Exactly two. If \( p \) has degree \( 2 \) and \( p \perp \nR[x]_{\le 1} \), let \( \lambda \ne 0 \) be its leading coefficient; then \( p/\lambda \) is monic of degree \( 2 \) and still orthogonal to \( \nR[x]_{\le 1} \), so \( p/\lambda = x^2 - \tfrac13 \) by @prp-monic-orthogonal-sequence. Thus \( p = \lambda(x^2 - \tfrac13) \), and \( \norm{p} = 1 \) leaves \( \lambda = \pm 1/\norm{x^2 - \tfrac13} \). Since @exm-gram-schmidt-legendre computed \( \norm{x^2 - \tfrac13}^2 = \tfrac{8}{45} \), the two answers are \( \pm\tfrac{\sqrt{10}}{4}(3x^2 - 1) \). Fixing the scale by the norm leaves a sign; fixing it by "monic" leaves nothing.
:::

## The three-term recurrence

Computing \( p_n \) by Gram–Schmidt costs one inner product for every earlier member, so reaching degree \( n \) costs about \( n^2/2 \) integrals. Almost all of them return \( 0 \). The next theorem says which ones do not, and reduces the cost to two integrals per step.

::: {#thm-three-term-recurrence}
[Three-Term Recurrence]

Let \( (p_k) \) be the monic orthogonal polynomial sequence of @prp-monic-orthogonal-sequence, for an inner product satisfying @prp-multiplication-by-x-symmetric. For a weight on an interval this covers every \( k \); for the node inner product on \( n \) nodes, where @prp-multiplication-by-x-symmetric holds only up to degree \( n - 1 \), read the statement for \( k + 1 \le n \). Put \( p_{-1} = 0 \) and, for \( k \ge 0 \),
\[
a_k = \frac{\inner{xp_k}{p_k}}{\inner{p_k}{p_k}}, \qquad b_k = \frac{\inner{p_k}{p_k}}{\inner{p_{k-1}}{p_{k-1}}} \ \ (k \ge 1).
\]
Then \( p_0 = 1 \), \( p_1 = x - a_0 \), and
\[
p_{k+1} = (x - a_k)\,p_k - b_k\,p_{k-1} \qquad \text{for every } k \ge 1 .
\]
Moreover \( b_k > 0 \) for every \( k \ge 1 \).
:::

::: {.idea}
The polynomial \( xp_k \) is monic of degree \( k + 1 \), so it is \( p_{k+1} \) plus something of degree at most \( k \), and that something expands in the orthogonal basis \( (p_0, \dots, p_k) \) with coefficients \( \inner{xp_k}{p_j}/\inner{p_j}{p_j} \) (@cor-projection-orthogonal-basis). The point is that almost every coefficient is \( 0 \): move the \( x \) across with @prp-multiplication-by-x-symmetric, and the coefficient becomes \( \inner{p_k}{xp_j} \), which vanishes as soon as \( \deg(xp_j) = j + 1 \) is still below \( k \). Only \( j = k \) and \( j = k - 1 \) can survive.
:::

::: {.proof}
\( p_0 = 1 \) is the unique monic polynomial of degree \( 0 \), and \( p_1 = x - a_0 \) is the unique monic polynomial of degree \( 1 \) with \( \inner{p_1}{p_0} = 0 \), since \( \inner{x - a_0}{1} = \inner{x}{1} - a_0\inner{1}{1} = 0 \) exactly for \( a_0 = \inner{x\cdot 1}{1}/\inner{1}{1} \).

Now fix \( k \ge 1 \). By @prp-monic-orthogonal-sequence, \( (p_0, \dots, p_{k+1}) \) is an orthogonal basis of \( \nR[x]_{\le k+1} \), and \( xp_k \) lies in that space. By @cor-projection-orthogonal-basis applied inside \( \nR[x]_{\le k+1} \),
\[
xp_k = \sum_{j=0}^{k+1} c_j\,p_j, \qquad c_j = \frac{\inner{xp_k}{p_j}}{\inner{p_j}{p_j}} .
\]
Both \( xp_k \) and \( p_{k+1} \) are monic of degree \( k + 1 \), and every other term of the sum has degree at most \( k \); comparing coefficients of \( x^{k+1} \) gives \( c_{k+1} = 1 \).

Let \( j \le k - 2 \). By @prp-multiplication-by-x-symmetric, \( \inner{xp_k}{p_j} = \inner{p_k}{xp_j} \), and \( \deg(xp_j) = j + 1 \le k - 1 \), so \( xp_j \in \nR[x]_{\le k-1} \) and the pairing is \( 0 \) by @prp-monic-orthogonal-sequence. Hence \( c_j = 0 \) for every \( j \le k - 2 \), and
\[
xp_k = p_{k+1} + c_k\,p_k + c_{k-1}\,p_{k-1},
\]
which rearranges to \( p_{k+1} = (x - c_k)p_k - c_{k-1}p_{k-1} \).

It remains to identify the two coefficients. By definition \( c_k = \inner{xp_k}{p_k}/\inner{p_k}{p_k} = a_k \). For the other, \( xp_{k-1} \) is monic of degree \( k \), so \( xp_{k-1} - p_k \) has degree at most \( k - 1 \) and therefore pairs to \( 0 \) with \( p_k \). Hence, using @prp-multiplication-by-x-symmetric again,
\[
\inner{xp_k}{p_{k-1}} = \inner{p_k}{xp_{k-1}} = \inner{p_k}{p_k},
\]
so \( c_{k-1} = \inner{p_k}{p_k}/\inner{p_{k-1}}{p_{k-1}} = b_k \). Finally \( b_k \) is a quotient of \( \norm{p_k}^2 \) by \( \norm{p_{k-1}}^2 \), both strictly positive because \( p_k \) and \( p_{k-1} \) are non-zero, so \( b_k > 0 \).
:::

Two inner products per step generate the whole sequence. The positivity of \( b_k \) is not decoration either: it is the sign that drives the interlacing argument of @exr-orthogonal-polynomials-c1.

::: {.remark}
If the interval is symmetric, \( (a, b) = (-c, c) \), and the weight is even, \( w(-t) = w(t) \), then \( a_k = 0 \) for every \( k \) and \( p_k(-x) = (-1)^kp_k(x) \). Induct on \( k \): \( p_0 = 1 \) is even, and \( a_0 = \inner{x}{1}/\inner{1}{1} = 0 \) because \( t\,w(t) \) is odd, so \( p_1 = x \) is odd. If \( p_{k-1} \) and \( p_k \) have parities \( (-1)^{k-1} \) and \( (-1)^k \), then \( t\,p_k(t)^2w(t) \) is odd, so \( a_k = 0 \), and \( p_{k+1} = xp_k - b_kp_{k-1} \) is a combination of two polynomials of parity \( (-1)^{k+1} \).
:::

::: {#exm-legendre-recurrence}
[The monic Legendre polynomials, continued]

For \( \inner{p}{q} = \int_{-1}^{1} pq \), @exm-gram-schmidt-legendre gave \( p_0 = 1 \), \( p_1 = x \), \( p_2 = x^2 - \tfrac13 \), with \( \inner{p_0}{p_0} = 2 \), \( \inner{p_1}{p_1} = \tfrac23 \) and \( \inner{p_2}{p_2} = \tfrac{8}{45} \). Use @thm-three-term-recurrence to obtain \( p_3 \), and check the recurrence reproduces \( p_2 \).
:::

::: {.solution}
The weight \( w = 1 \) is even on \( (-1, 1) \), so every \( a_k = 0 \) by the remark above. Then
\[
b_1 = \frac{\inner{p_1}{p_1}}{\inner{p_0}{p_0}} = \frac{2/3}{2} = \frac13, \qquad
b_2 = \frac{\inner{p_2}{p_2}}{\inner{p_1}{p_1}} = \frac{8/45}{2/3} = \frac{4}{15}.
\]
The recurrence at \( k = 1 \) gives \( p_2 = x\cdot x - \tfrac13\cdot 1 = x^2 - \tfrac13 \), which is what Gram–Schmidt produced. At \( k = 2 \),
\[
p_3 = x\Big(x^2 - \tfrac13\Big) - \tfrac{4}{15}\,x = x^3 - \tfrac35 x .
\]
*Check.* \( \inner{p_3}{1} = \inner{p_3}{x^2} = 0 \) because the integrands are odd, and
\[
\inner{p_3}{x} = \int_{-1}^{1}\Big(t^4 - \tfrac35 t^2\Big)\dd t = \tfrac25 - \tfrac35\cdot\tfrac23 = 0 .
\]
So \( p_3 \perp \nR[x]_{\le 2} \), as it should be. Two integrals produced a polynomial that Gram–Schmidt would have charged three for, and the saving grows with the degree.
:::

## Where the roots are

The roots of \( p_2 = x^2 - \tfrac13 \) are \( \pm 1/\sqrt3 \approx \pm 0.577 \), and those of \( p_3 = x^3 - \tfrac35 x \) are \( 0 \) and \( \pm\sqrt{3/5} \approx \pm 0.775 \). All five lie inside \( (-1, 1) \), where the weight lives. No coincidence. The argument first needs one fact about real polynomials, in which \( \operatorname{mult}_r(f) \) is the multiplicity of \( r \) as a root of \( f \) (@def-root-multiplicity).

::: {#lem-even-multiplicity-no-sign-change}
[Even multiplicities mean no sign change]

Let \( I \subseteq \nR \) be an open interval and let \( f \in \nR[x] \) be non-zero. If \( \operatorname{mult}_r(f) \) is even for every \( r \in I \), then \( f \ge 0 \) throughout \( I \), or \( f \le 0 \) throughout \( I \).
:::

::: {.proof}
By @thm-roots-with-multiplicity over \( \nR \), write \( f = (x - d_1)^{m_1}\cdots(x - d_l)^{m_l}\,g \), where \( d_1, \dots, d_l \) are the distinct real roots of \( f \), \( m_i = \operatorname{mult}_{d_i}(f) \), and \( g \) has no real root. Separate the factors according to whether \( d_i \in I \):
\[
f = h \cdot \Big(\textstyle\prod_{d_i \in I} (x - d_i)^{m_i}\Big), \qquad h = g\cdot\textstyle\prod_{d_i \notin I}(x - d_i)^{m_i} .
\]
Each \( m_i \) with \( d_i \in I \) is even by hypothesis, so the second factor is the square of a real polynomial and is \( \ge 0 \) everywhere. The polynomial \( h \) has no root in \( I \): its roots are the \( d_i \) outside \( I \), and \( g \) has none. Being continuous and nowhere zero on the interval \( I \), \( h \) has constant sign there by the intermediate value theorem. Hence \( f \) has that same sign throughout \( I \), weakly, with equality only at the \( d_i \) inside \( I \).
:::

::: {#thm-orthogonal-polynomial-roots}
[Roots of an Orthogonal Polynomial]

Let \( w \) be a weight on \( (a, b) \), let \( \inner{p}{q} = \int_a^b pqw \), and let \( (p_k) \) be the monic orthogonal polynomial sequence. For every \( k \ge 1 \), the polynomial \( p_k \) has \( k \) **distinct real** roots, and every one of them lies in the **open** interval \( (a, b) \).
:::

::: {.idea}
Suppose \( p_k \) changed sign at only a few points \( c_1, \dots, c_m \) of \( (a, b) \), with \( m < k \). Build the polynomial \( q = (x - c_1)\cdots(x - c_m) \). It is cheap — degree at most \( k - 1 \) — so \( p_k \) is orthogonal to it. But \( q \) was designed to change sign at exactly the points where \( p_k \) does, so the product \( p_kq \) changes sign nowhere, and a function of one sign that is not identically zero cannot integrate to zero against a positive weight. The contradiction forces \( m \ge k \), and \( k \) distinct roots is all a polynomial of degree \( k \) can hold.
:::

::: {.proof}
Fix \( k \ge 1 \). Let \( c_1 < \dots < c_m \) be the roots of \( p_k \) in \( (a, b) \) whose multiplicity is **odd** (possibly \( m = 0 \)), and set \( q = (x - c_1)\cdots(x - c_m) \), with \( q = 1 \) when \( m = 0 \).

Suppose, for contradiction, that \( m \le k - 1 \). Then \( q \in \nR[x]_{\le k-1} \), so \( \inner{p_k}{q} = 0 \) by @prp-monic-orthogonal-sequence.

Put \( f = p_kq \), a non-zero polynomial (@thm-degree-of-product). Let \( r \in (a, b) \) be a root of \( f \). By @thm-multiplicity-of-product, \( \operatorname{mult}_r(f) = \operatorname{mult}_r(p_k) + \operatorname{mult}_r(q) \). If \( r = c_i \) for some \( i \), then \( \operatorname{mult}_r(q) = 1 \) and \( \operatorname{mult}_r(p_k) \) is odd by the choice of the \( c_i \), so the sum is even. If \( r \) is none of the \( c_i \), then \( q(r) \ne 0 \), so \( \operatorname{mult}_r(q) = 0 \) and \( \operatorname{mult}_r(p_k) \) is even, again by the choice of the \( c_i \). Either way \( \operatorname{mult}_r(f) \) is even.

By @lem-even-multiplicity-no-sign-change, \( f \ge 0 \) throughout \( (a, b) \) or \( f \le 0 \) throughout \( (a, b) \); replacing \( q \) by \( -q \) if necessary, which changes neither \( \inner{p_k}{q} = 0 \) nor \( \deg q \), we may assume \( f \ge 0 \) there. Then \( fw \) is continuous and \( \ge 0 \) on \( (a, b) \), and it is \( > 0 \) off the finitely many roots of \( f \), because \( w > 0 \). By the calculus fact recalled when the inner product was set up — a continuous non-negative function with integral \( 0 \) vanishes identically — an integrand of that shape cannot integrate to \( 0 \). Therefore
\[
\inner{p_k}{q} = \int_a^b f(t)\,w(t)\,\dd t > 0,
\]
contradicting \( \inner{p_k}{q} = 0 \).

Hence \( m \ge k \). Each \( c_i \) is a root of \( p_k \), and \( p_k \) is non-zero of degree \( k \), so \( m \le k \) by @cor-root-bound-general; thus \( m = k \) and \( p_k \) has \( k \) distinct roots \( c_1, \dots, c_k \), all in \( (a, b) \). By @cor-root-bound-general again, \( (x - c_1)\cdots(x - c_k) \) divides \( p_k \), and both are monic of degree \( k \), so \( p_k = (x - c_1)\cdots(x - c_k) \). In particular each root is simple and \( p_k \) has no roots outside \( (a, b) \), real or complex. This proves the theorem.
:::

So the weight hands us \( k \) points inside its interval, chosen by the inner product rather than by us. The next subsection says what they are good for.

::: {.check}
The monic Laguerre polynomial of degree \( 2 \) for the weight \( w(t) = e^{-t} \) on \( (0, \infty) \) is \( p_2 = x^2 - 4x + 2 \). Check that @thm-orthogonal-polynomial-roots is not lying.
:::

::: {.solution}
The roots are \( 2 \pm \sqrt2 \), that is \( \approx 0.586 \) and \( \approx 3.414 \): real, distinct, and both in \( (0, \infty) \). An unbounded interval is no obstacle, since the theorem asks only that the weight be positive with finite moments, and \( \int_0^\infty t^ke^{-t}\,\dd t = k! \).
:::

## Gaussian quadrature

Chapter 5 wrote \( \int_0^1 p \) as a fixed combination of \( p(0) \), \( p(\tfrac12) \) and \( p(1) \), valid for every \( p \in \nR[x]_{\le 2} \) (@exm-quadrature-weights). The construction works for any prescribed nodes: integrate the Lagrange interpolation formula (@thm-lagrange-interpolation) and \( k \) distinct nodes give a rule exact on \( \nR[x]_{\le k-1} \).

But a \( k \)-point rule has \( 2k \) numbers at its disposal, \( k \) nodes and \( k \) coefficients, and only \( k \) of them were spent. Spending the nodes too should buy degree \( 2k - 1 \). Where to put them is the question, and the answer is the one place we have not chosen: the roots of \( p_k \).

::: {#thm-gaussian-quadrature}
[Gaussian Quadrature]

Let \( w \) be a weight on \( (a, b) \) with \( \inner{p}{q} = \int_a^b pqw \), let \( k \ge 1 \), and let \( t_1 < \dots < t_k \) be the roots of the monic orthogonal polynomial \( p_k \), which lie in \( (a, b) \) by @thm-orthogonal-polynomial-roots. Let \( \ell_1, \dots, \ell_k \in \nR[x]_{\le k-1} \) be the Lagrange polynomials for these nodes (@def-lagrange-basis) and set
\[
\alpha_i = \int_a^b \ell_i(t)\,w(t)\,\dd t \qquad (i = 1, \dots, k).
\]
Then every \( \alpha_i \) is **strictly positive**, and
\[
\int_a^b f(t)\,w(t)\,\dd t = \sum_{i=1}^{k} \alpha_i\,f(t_i)
\]
for **every** \( f \in \nR[x]_{\le 2k-1} \).
:::

::: {.idea}
Two moves, one for each side of the identity. On the left, divide \( f \) by \( p_k \): \( f = qp_k + r \). The degree bookkeeping — \( \deg f \le 2k - 1 \) against \( \deg p_k = k \) — forces \( \deg q \le k - 1 \), which is exactly the condition under which \( \int qp_kw = \inner{p_k}{q} \) vanishes. So the integral of \( f \) is the integral of its remainder. On the right, \( p_k \) vanishes at every node, so the sum also only sees the remainder. And the remainder has degree at most \( k - 1 \), which is precisely the range on which \( k \) nodes reproduce a polynomial exactly. The two sides meet there.
:::

::: {.proof}
Let \( f \in \nR[x]_{\le 2k-1} \). Since \( p_k \ne 0 \), @thm-polynomial-division gives \( q, r \in \nR[x] \) with
\[
f = qp_k + r, \qquad \deg r < k .
\]
If \( q = 0 \) then \( q \in \nR[x]_{\le k-1} \) trivially. Otherwise \( qp_k = f - r \) has degree at most \( 2k - 1 \), while \( \deg(qp_k) = \deg q + k \) by @thm-degree-of-product; hence \( \deg q \le k - 1 \). Either way \( q \in \nR[x]_{\le k-1} \), so @prp-monic-orthogonal-sequence gives \( \inner{p_k}{q} = 0 \), that is, \( \int_a^b qp_kw = 0 \). Therefore
\[
\int_a^b f w = \int_a^b qp_kw + \int_a^b rw = \int_a^b rw . \tag{$\ast$}
\]
At each node, \( p_k(t_i) = 0 \), so
\[
f(t_i) = q(t_i)p_k(t_i) + r(t_i) = r(t_i) \qquad (i = 1, \dots, k). \tag{$\ast\ast$}
\]
Since \( \deg r \le k - 1 \) and \( t_1, \dots, t_k \) are \( k \) distinct points, @thm-lagrange-interpolation (b) gives \( r = \sum_{i} r(t_i)\ell_i \). Integrating against \( w \) and using the definition of \( \alpha_i \),
\[
\int_a^b rw = \sum_{i=1}^{k} r(t_i)\,\alpha_i = \sum_{i=1}^{k} \alpha_i f(t_i),
\]
the last step by \( (\ast\ast) \). Combining with \( (\ast) \) proves the quadrature identity.

For positivity, fix \( j \) and apply the identity to \( f = \ell_j^2 \), which is legitimate because \( \deg \ell_j^2 = 2k - 2 \le 2k - 1 \). By @thm-lagrange-interpolation (a), \( \ell_j(t_i) = \delta_{ij} \), so the right-hand side collapses to \( \alpha_j \), while the left-hand side is \( \inner{\ell_j}{\ell_j} = \norm{\ell_j}^2 \). Since \( \ell_j \ne 0 \), positive definiteness gives \( \alpha_j = \norm{\ell_j}^2 > 0 \).
:::

Each hypothesis did one job. Orthogonality to lower degrees killed the quotient on the left; the nodes being roots of \( p_k \) killed it again on the right. That is also why the nodes cannot be moved: shift one and the second cancellation fails. @exr-orthogonal-polynomials-c2 shows \( 2k - 1 \) is a ceiling, not just what this proof happens to reach.

::: {#exm-two-point-gauss-legendre}
[Two-point Gauss–Legendre]

Take \( w = 1 \) on \( (-1, 1) \) and \( k = 2 \). Find the nodes and weights, and test the resulting rule on \( f = 1 + 2x + 3x^2 + 4x^3 \) and on \( f = x^4 \).
:::

::: {.solution}
The monic \( p_2 \) is \( x^2 - \tfrac13 \) (@exm-gram-schmidt-legendre), so the nodes are \( t_1 = -1/\sqrt3 \) and \( t_2 = 1/\sqrt3 \). The Lagrange polynomials are \( \ell_1 = (x - t_2)/(t_1 - t_2) \) and \( \ell_2 = (x - t_1)/(t_2 - t_1) \), with \( t_1 - t_2 = -2/\sqrt3 \). Since \( \int_{-1}^{1} t\,\dd t = 0 \) and \( \int_{-1}^{1} 1\,\dd t = 2 \),
\[
\alpha_1 = \frac{0 - 2t_2}{t_1 - t_2} = \frac{-2/\sqrt3}{-2/\sqrt3} = 1,
\]
and \( \alpha_2 = 1 \) by the same computation with the roles swapped. The rule is
\[
\int_{-1}^{1} f(t)\,\dd t = f\Big(\!-\tfrac{1}{\sqrt3}\Big) + f\Big(\tfrac{1}{\sqrt3}\Big) \qquad \text{for } f \in \nR[x]_{\le 3}.
\]
Two evaluations, no coefficients to remember, every cubic exactly.

*The cubic test.* Exactly, \( \int_{-1}^{1}(1 + 2t + 3t^2 + 4t^3)\dd t = 2 + 0 + 3\cdot\tfrac23 + 0 = 4 \). By the rule, \( f(-1/\sqrt3) = 2 - \tfrac{10\sqrt3}{9} \) and \( f(1/\sqrt3) = 2 + \tfrac{10\sqrt3}{9} \), whose sum is \( 4 \). The odd parts cancel and the constant and quadratic parts contribute \( 1 + 1 \) and \( 1 + 1 \).

*The quartic test.* Exactly, \( \int_{-1}^{1} t^4\,\dd t = \tfrac25 \). By the rule, \( (1/\sqrt3)^4 + (1/\sqrt3)^4 = \tfrac29 \). These differ, so degree \( 4 = 2k \) is already out of reach. Compare @exm-quadrature-weights, where the nodes were fixed in advance and **three** of them guaranteed exactness only up to degree \( 2 \) — guaranteed by the construction, that is; that particular symmetric rule happens to integrate cubics exactly as well, which is luck of the symmetry and not something the construction promises.
:::

::: {.warning}
**"Exact" means exact on polynomials.** @thm-gaussian-quadrature says nothing about \( \int_a^b fw \) for a general \( f \), and nothing about what happens as \( k \) grows; on a non-polynomial the rule returns an approximation whose error is a question for analysis. What linear algebra delivers is exactness on a subspace, and the reason that subspace is the largest available.
:::

## The classical families

Four weights account for most of the orthogonal polynomials that occur in practice. The table records them; the entries are statements, and @exr-orthogonal-polynomials-b2 asks you to verify two of the rows by integration.

| Family | Interval | Weight \( w(t) \) | \( p_1 \) | \( p_2 \) |
|---|---|---|---|---|
| Legendre | \( (-1, 1) \) | \( 1 \) | \( x \) | \( x^2 - \tfrac13 \) |
| Chebyshev | \( (-1, 1) \) | \( (1 - t^2)^{-1/2} \) | \( x \) | \( x^2 - \tfrac12 \) |
| Hermite | \( (-\infty, \infty) \) | \( e^{-t^2} \) | \( x \) | \( x^2 - \tfrac12 \) |
| Laguerre | \( (0, \infty) \) | \( e^{-t} \) | \( x - 1 \) | \( x^2 - 4x + 2 \) |

The last two columns give the monic members of degrees \( 1 \) and \( 2 \); \( p_0 = 1 \) in every row. The Chebyshev weight is unbounded at \( \pm 1 \) and the Hermite and Laguerre intervals are unbounded, so in those three rows the integrals defining the inner product are improper; they converge, which is the finiteness condition our definition of a weight demanded. The first three weights are even on symmetric intervals, so their \( a_k \) all vanish and their members alternate in parity; the Laguerre weight is not, and \( a_0 = 1 \) there. Section 9 of this chapter meets the Chebyshev family again from the Fourier side, where the substitution \( t = \cos\theta \) turns its awkward weight into \( \dd\theta \).

## Exercises

### A. Check your understanding

:::: {#exr-orthogonal-polynomials-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define what it means for \( p_0, p_1, p_2, \dots \) to be a **monic orthogonal polynomial sequence** for an inner product on \( \nR[x] \).
2. State the three-term recurrence, including the formulas for \( a_k \) and \( b_k \) and the starting values.
3. True or false: \( b_k > 0 \) for every \( k \ge 1 \). Justify your answer.
4. For \( \inner{p}{q} = \int_{-1}^{1} pq \), how many roots does \( p_7 \) have, of what kind, and where?
5. True or false: for **every** inner product on \( \nR[x] \) one has \( \inner{xp}{q} = \inner{p}{xq} \). Justify your answer.
6. How many nodes does a Gaussian rule need in order to integrate every polynomial of degree at most \( 11 \) exactly?
:::
::::

::: {.solution}
(a) A sequence with \( \deg p_k = k \) and leading coefficient \( 1 \) for every \( k \), and \( \inner{p_j}{p_k} = 0 \) whenever \( j \ne k \) (@def-orthogonal-polynomial-sequence).

(b) With \( p_{-1} = 0 \), \( p_0 = 1 \) and \( p_1 = x - a_0 \), one has \( p_{k+1} = (x - a_k)p_k - b_kp_{k-1} \) for \( k \ge 1 \), where \( a_k = \inner{xp_k}{p_k}/\inner{p_k}{p_k} \) and \( b_k = \inner{p_k}{p_k}/\inner{p_{k-1}}{p_{k-1}} \) (@thm-three-term-recurrence).

(c) True. Both \( \inner{p_k}{p_k} = \norm{p_k}^2 \) and \( \inner{p_{k-1}}{p_{k-1}} = \norm{p_{k-1}}^2 \) are strictly positive, since \( p_k \) and \( p_{k-1} \) are non-zero and the inner product is positive definite.

(d) Seven roots, all real, all distinct, all in the open interval \( (-1, 1) \) (@thm-orthogonal-polynomial-roots). In particular \( p_7 \) has no complex roots and no repeated ones.

(e) False. Take the coefficient inner product \( \inner{p}{q} = \sum_k u_kv_k \) on \( \nR[x] \), where \( p = \sum_k u_kx^k \) and \( q = \sum_k v_kx^k \) (@exm-functional-with-no-riesz-vector). Then \( \inner{x\cdot 1}{x} = \inner{x}{x} = 1 \), while \( \inner{1}{x\cdot x} = \inner{1}{x^2} = 0 \). The identity is a property of the weight and node constructions (@prp-multiplication-by-x-symmetric), not of inner products in general.

(f) Six. A \( k \)-point rule is exact up to degree \( 2k - 1 \), and \( 2\cdot 6 - 1 = 11 \).
:::

### B. Practice

::: {#exr-orthogonal-polynomials-b1}
[B1: A weighted interval]

On \( \nR[x] \) put \( \inner{p}{q} = \int_0^1 p(t)q(t)\,t\,\dd t \). Compute the monic \( p_0 \), \( p_1 \) and \( p_2 \), and verify directly that \( p_2 \perp \nR[x]_{\le 1} \).
:::

::: {.solution}
The moments are \( \inner{x^k}{1} = \int_0^1 t^{k+1}\dd t = 1/(k+2) \), so \( \tfrac12, \tfrac13, \tfrac14, \tfrac15 \) for \( k = 0, 1, 2, 3 \).

\( p_0 = 1 \). Then \( a_0 = \inner{x}{1}/\inner{1}{1} = (1/3)/(1/2) = \tfrac23 \), so \( p_1 = x - \tfrac23 \), and
\[
\inner{p_1}{p_1} = \tfrac14 - \tfrac43\cdot\tfrac13 + \tfrac49\cdot\tfrac12 = \tfrac14 - \tfrac29 = \tfrac{1}{36}.
\]
Next \( \inner{xp_1}{p_1} = \int_0^1 (t^4 - \tfrac43t^3 + \tfrac49t^2)\dd t = \tfrac15 - \tfrac13 + \tfrac{4}{27} = \tfrac{2}{135} \), so
\[
a_1 = \frac{2/135}{1/36} = \frac{8}{15}, \qquad b_1 = \frac{1/36}{1/2} = \frac{1}{18},
\]
and @thm-three-term-recurrence gives
\[
p_2 = \Big(x - \tfrac{8}{15}\Big)\Big(x - \tfrac23\Big) - \tfrac{1}{18} = x^2 - \tfrac65 x + \tfrac{3}{10}.
\]
*Verification.* \( \inner{p_2}{1} = \int_0^1 (t^3 - \tfrac65t^2 + \tfrac{3}{10}t)\dd t = \tfrac14 - \tfrac25 + \tfrac{3}{20} = 0 \), and \( \inner{p_2}{x} = \int_0^1 (t^4 - \tfrac65t^3 + \tfrac{3}{10}t^2)\dd t = \tfrac15 - \tfrac{3}{10} + \tfrac{1}{10} = 0 \). Since \( (1, x) \) spans \( \nR[x]_{\le 1} \), this is the whole check.
:::

:::: {#exr-orthogonal-polynomials-b2}
[B2: Two rows of the table]

Verify the degree-\( 1 \) and degree-\( 2 \) entries of the table for two of the classical families.

::: {.enumerate options="label=(\alph*)"}
1. Chebyshev: \( w(t) = (1 - t^2)^{-1/2} \) on \( (-1, 1) \). You may use, without proof, that \( \int_{-1}^{1} (1 - t^2)^{-1/2}\dd t = \pi \) and \( \int_{-1}^{1} t^2(1 - t^2)^{-1/2}\dd t = \pi/2 \).
2. Laguerre: \( w(t) = e^{-t} \) on \( (0, \infty) \). You may use, without proof, that \( \int_0^\infty t^ke^{-t}\,\dd t = k! \).
:::
::::

::: {.solution}
(a) The weight is even, so \( \inner{x^j}{x^i} = 0 \) whenever \( i + j \) is odd. Hence \( \inner{x}{1} = 0 \), and \( x \) is monic of degree \( 1 \) and orthogonal to \( \nR[x]_{\le 0} \), so \( p_1 = x \) by @prp-monic-orthogonal-sequence. Write \( p_2 = x^2 + \beta x + \gamma \). Then \( \inner{p_2}{x} = \inner{x^2}{x} + \beta\inner{x}{x} + \gamma\inner{1}{x} = 0 + \beta\cdot\tfrac{\pi}{2} + 0 \), forcing \( \beta = 0 \); and \( \inner{p_2}{1} = \tfrac{\pi}{2} + 0 + \gamma\pi = 0 \), forcing \( \gamma = -\tfrac12 \). So \( p_2 = x^2 - \tfrac12 \).

(b) The moments are \( \inner{x^k}{1} = k! \), so \( 1, 1, 2, 6 \) for \( k = 0, 1, 2, 3 \). For \( p_1 = x + \beta \): \( \inner{p_1}{1} = 1 + \beta = 0 \), so \( p_1 = x - 1 \). For \( p_2 = x^2 + \beta x + \gamma \), the two conditions \( \inner{p_2}{1} = 0 \) and \( \inner{p_2}{x} = 0 \) read
\[
2 + \beta + \gamma = 0, \qquad 6 + 2\beta + \gamma = 0 .
\]
Subtracting gives \( \beta = -4 \), then \( \gamma = 2 \). So \( p_2 = x^2 - 4x + 2 \), whose roots \( 2 \pm \sqrt2 \) we already located in the Quick check above.
:::

::: {#exr-orthogonal-polynomials-b3}
[B3: One more Legendre polynomial]

Continue @exm-legendre-recurrence: compute \( \inner{p_3}{p_3} \) for \( p_3 = x^3 - \tfrac35 x \), then use @thm-three-term-recurrence to find \( p_4 \). Verify that \( \inner{p_4}{1} = \inner{p_4}{x^2} = 0 \).
:::

::: {.solution}
\[
\inner{p_3}{p_3} = \int_{-1}^{1}\Big(t^6 - \tfrac65 t^4 + \tfrac{9}{25}t^2\Big)\dd t = \tfrac27 - \tfrac65\cdot\tfrac25 + \tfrac{9}{25}\cdot\tfrac23 = \tfrac27 - \tfrac{6}{25} = \tfrac{8}{175}.
\]
Since the weight is even, \( a_3 = 0 \), and \( b_3 = \inner{p_3}{p_3}/\inner{p_2}{p_2} = (8/175)/(8/45) = \tfrac{9}{35} \). Hence
\[
p_4 = x\Big(x^3 - \tfrac35 x\Big) - \tfrac{9}{35}\Big(x^2 - \tfrac13\Big) = x^4 - \tfrac67 x^2 + \tfrac{3}{35}.
\]
*Verification.* \( \inner{p_4}{1} = \tfrac25 - \tfrac67\cdot\tfrac23 + \tfrac{3}{35}\cdot 2 = \tfrac{14 - 20 + 6}{35} = 0 \), and
\[
\inner{p_4}{x^2} = \tfrac27 - \tfrac67\cdot\tfrac25 + \tfrac{3}{35}\cdot\tfrac23 = \tfrac{10 - 12 + 2}{35} = 0 .
\]
Orthogonality to \( x \) and \( x^3 \) is automatic by parity.
:::

:::: {#exr-orthogonal-polynomials-b4}
[B4: A two-point rule on the unit interval]

Work on \( (0, 1) \) with \( w = 1 \). Exercise B2 of Section 2 (@exr-orthonormal-bases-b2) found the monic orthogonal polynomials \( 1 \), \( x - \tfrac12 \), \( x^2 - x + \tfrac16 \).

::: {.enumerate options="label=(\alph*)"}
1. Write down the two-point Gaussian rule for \( \int_0^1 f \).
2. Check it on \( f = x^3 \), and show that it fails on \( f = x^4 \).
:::
::::

::: {.solution}
(a) The nodes are the roots of \( x^2 - x + \tfrac16 \), namely
\[
t_{1,2} = \tfrac12 \mp \tfrac{\sqrt3}{6}, \qquad t_2 - t_1 = \tfrac{\sqrt3}{3},
\]
both in \( (0, 1) \), as @thm-orthogonal-polynomial-roots promises. With \( \ell_1 = (x - t_2)/(t_1 - t_2) \) and \( \int_0^1 t\,\dd t = \tfrac12 \),
\[
\alpha_1 = \frac{\tfrac12 - t_2}{t_1 - t_2} = \frac{-\sqrt3/6}{-\sqrt3/3} = \tfrac12,
\]
and \( \alpha_2 = \tfrac12 \) likewise. So \( \int_0^1 f = \tfrac12\big(f(t_1) + f(t_2)\big) \) for \( f \in \nR[x]_{\le 3} \).

(b) Write \( t_{1,2} = \tfrac12 \mp u \) with \( u = \sqrt3/6 \), so \( u^2 = \tfrac{1}{12} \). The odd powers of \( u \) cancel in a sum over \( t_1 \) and \( t_2 \), so
\[
t_1^3 + t_2^3 = 2\Big(\tfrac18 + 3\cdot\tfrac12\cdot\tfrac{1}{12}\Big) = 2\cdot\tfrac14 = \tfrac12,
\]
and half of that is \( \tfrac14 = \int_0^1 t^3\,\dd t \). For the quartic,
\[
t_1^4 + t_2^4 = 2\Big(\tfrac{1}{16} + 6\cdot\tfrac14\cdot\tfrac{1}{12} + \tfrac{1}{144}\Big) = 2\cdot\tfrac{28}{144} = \tfrac{7}{18},
\]
so the rule returns \( \tfrac{7}{36} \), whereas \( \int_0^1 t^4\,\dd t = \tfrac15 \). The rule is exact to degree \( 3 = 2k - 1 \) and no further.
:::

### C. Going deeper

:::: {#exr-orthogonal-polynomials-c1}
[C1: Interlacing roots]

Let \( w \) be a weight on \( (a, b) \) and let \( (p_k) \) be its monic orthogonal polynomial sequence. The roots of \( p_k \) are said to **interlace** those of \( p_{k+1} \) when exactly one root of \( p_k \) lies strictly between each pair of consecutive roots of \( p_{k+1} \). This is true for every \( k \); prove the first two cases by hand.

::: {.enumerate options="label=(\alph*)"}
1. Let \( r \) be the root of \( p_1 \) and \( s_1 < s_2 \) the roots of \( p_2 \). Prove that \( s_1 < r < s_2 \).
2. Let \( u_1 < u_2 < u_3 \) be the roots of \( p_3 \). Prove that \( u_1 < s_1 < u_2 < s_2 < u_3 \).
:::

*Hint: evaluate the three-term recurrence at a root.*
::::

::: {.solution}
(a) By @thm-three-term-recurrence with \( k = 1 \), \( p_2 = (x - a_1)p_1 - b_1p_0 = (x - a_1)(x - r) - b_1 \). Evaluating at \( r \) gives \( p_2(r) = -b_1 < 0 \), since \( b_1 > 0 \). By @thm-orthogonal-polynomial-roots, \( p_2 = (x - s_1)(x - s_2) \) with \( s_1 < s_2 \) real, and this product is negative exactly on \( (s_1, s_2) \). Hence \( s_1 < r < s_2 \).

(b) By @thm-three-term-recurrence with \( k = 2 \), \( p_3 = (x - a_2)p_2 - b_2p_1 \). At a root of \( p_2 \) the first term dies, so
\[
p_3(s_i) = -b_2\,p_1(s_i) = -b_2(s_i - r) \qquad (i = 1, 2).
\]
By (a), \( s_1 - r < 0 \) and \( s_2 - r > 0 \), and \( b_2 > 0 \), so \( p_3(s_1) > 0 \) and \( p_3(s_2) < 0 \).

By @thm-orthogonal-polynomial-roots, \( p_3 = (x - u_1)(x - u_2)(x - u_3) \) with \( u_1 < u_2 < u_3 \). Such a product is negative on \( (-\infty, u_1) \), positive on \( (u_1, u_2) \), negative on \( (u_2, u_3) \), and positive on \( (u_3, \infty) \). So \( p_3(s_1) > 0 \) puts \( s_1 \) in \( (u_1, u_2) \) or in \( (u_3, \infty) \), and \( p_3(s_2) < 0 \) puts \( s_2 \) in \( (-\infty, u_1) \) or in \( (u_2, u_3) \). The option \( s_1 > u_3 \) is impossible: it would give \( s_2 > s_1 > u_3 \), where \( p_3 \) is positive, contradicting \( p_3(s_2) < 0 \). The option \( s_2 < u_1 \) is impossible too: it would give \( s_1 < s_2 < u_1 \), where \( p_3 \) is negative, contradicting \( p_3(s_1) > 0 \). Hence \( u_1 < s_1 < u_2 \) and \( u_2 < s_2 < u_3 \), which is the assertion.

The general case is not proved this way. The coefficients \( a_k \) and \( b_k \) assemble into a symmetric tridiagonal matrix whose characteristic polynomial is \( p_k \), and the interlacing then follows from the interlacing theorem for the eigenvalues of a symmetric matrix and its leading submatrices, which is Chapter 16's business.
:::

:::: {#exr-orthogonal-polynomials-c2}
[C2: The ceiling is 2k − 1]

Let \( w \) be a weight on \( (a, b) \) and let \( k \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Let \( t_1, \dots, t_k \) be **any** \( k \) distinct real numbers and \( \alpha_1, \dots, \alpha_k \) **any** real numbers. Prove that there is an \( f \in \nR[x]_{\le 2k} \) with \( \int_a^b fw \ne \sum_i \alpha_i f(t_i) \).
2. Hence deduce that the Gaussian rule of @thm-gaussian-quadrature is exact on \( \nR[x]_{\le 2k-1} \) and on no larger space \( \nR[x]_{\le d} \).
:::
::::

::: {.solution}
(a) Put \( g = (x - t_1)\cdots(x - t_k) \) and \( f = g^2 \), a polynomial of degree \( 2k \). Every node is a root of \( g \), so \( f(t_i) = 0 \) for every \( i \) and the right-hand side is \( 0 \), whatever the \( \alpha_i \) are. The left-hand side is \( \int_a^b g^2w = \inner{g}{g} \), and \( g \ne 0 \), so \( \inner{g}{g} > 0 \) by positive definiteness. The two sides differ.

(b) Exactness on \( \nR[x]_{\le 2k-1} \) is @thm-gaussian-quadrature. Suppose the rule were exact on \( \nR[x]_{\le d} \) for some \( d \ge 2k \). Since \( \nR[x]_{\le 2k} \subseteq \nR[x]_{\le d} \), it would then be exact on every polynomial of degree at most \( 2k \). But its nodes are \( k \) distinct real numbers (@thm-orthogonal-polynomial-roots), so (a) supplies a polynomial of degree \( 2k \) on which it is not. Hence no such \( d \) exists, and \( 2k - 1 \) is the largest degree for which the rule is exact. The concrete instance \( k = 2 \), \( f = x^4 \) is the failure computed in @exm-two-point-gauss-legendre.
:::
