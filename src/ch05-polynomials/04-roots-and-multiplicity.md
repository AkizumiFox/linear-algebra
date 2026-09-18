# Roots, Multiplicity and Derivatives

Chapter 2 bounded the number of roots of a polynomial, and the first section of this chapter restated the bound as @cor-root-bound-general: a non-zero polynomial of degree \( n \) has at most \( n \) roots. The bound counts each root once, and so it misses something. The polynomial \( (x - 1)^2 \) has degree \( 2 \) but only one root, and the root \( 1 \) is somehow "used twice". This section makes "used twice" precise with the multiplicity of a root, sharpens the root bound, and then gives a test for repeated roots that needs no factoring: the formal derivative. The derivative behaves differently in characteristic \( p \), and we say exactly where. The section ends with Taylor expansion of a polynomial, which turns out to be a dual basis from Chapter 4.

## Multiplicity of a root

By the Factor Theorem (@lem-factor-theorem-linear, restated in general as @thm-remainder-theorem), \( c \) is a root of \( f \) exactly when \( x - c \) divides \( f \). A repeated root should mean that a higher power of \( x - c \) divides \( f \). So we measure how many factors \( x - c \) can be pulled out.

*The multiplicity of \( c \) counts how many times \( x - c \) divides \( f \).*

::: {#def-root-multiplicity}
[Multiplicity of a Root]

Let \( F \) be a field, \( f \in F[x] \) **non-zero** and \( c \in F \). The **multiplicity of \( c \) as a root of \( f \)**, written \( \operatorname{mult}_c(f) \), is the **largest** \( m \in \nN \) such that \( (x - c)^m \mid f \).

The root \( c \) is **simple** if \( \operatorname{mult}_c(f) = 1 \), and **multiple** (or **repeated**) if \( \operatorname{mult}_c(f) \ge 2 \).
:::

In words: keep dividing \( f \) by \( x - c \) as long as the division leaves no remainder, and count the successful divisions. Divisibility is meant in the sense of @def-divisibility-polynomials, so \( (x - c)^m \mid f \) says \( f = (x - c)^m g \) for some \( g \in F[x] \).

There is something to check: a largest such \( m \) must exist. The value \( m = 0 \) always works, since \( (x - c)^0 = 1 \) divides every polynomial. And if \( f = (x - c)^m g \), then \( g \neq 0 \) because \( f \neq 0 \), so @thm-degree-of-product gives \( \deg f = m + \deg g \ge m \). The admissible \( m \) form a non-empty set of natural numbers bounded by \( \deg f \), so it has a largest element. Moreover \( \operatorname{mult}_c(f) \ge 1 \) exactly when \( x - c \mid f \), that is, exactly when \( c \) is a root. So multiplicity \( 0 \) means "not a root".

The hypothesis \( f \neq 0 \) is not decoration. Every power \( (x - c)^m \) divides the zero polynomial, since \( 0 = (x - c)^m \cdot 0 \). There is no largest \( m \), and the zero polynomial has no multiplicities.

A definition by "largest \( m \)" is awkward to use directly, because to confirm \( m \) we must rule out all larger powers. The next lemma replaces it with a single test at \( c \).

::: {#lem-multiplicity-cofactor}
[Multiplicity via the Cofactor]

Let \( f \in F[x] \) be non-zero, \( c \in F \) and \( m \in \nN \). Then \( \operatorname{mult}_c(f) = m \) if and only if
\[
f = (x - c)^m g \quad \text{for some } g \in F[x] \text{ with } g(c) \neq 0 .
\]
:::

::: {.proof}
\( (\Rightarrow) \) Suppose \( \operatorname{mult}_c(f) = m \). Then \( f = (x - c)^m g \) for some \( g \in F[x] \). If \( g(c) = 0 \), then \( g = (x - c)h \) by @lem-factor-theorem-linear, so \( f = (x - c)^{m+1}h \), contradicting the maximality of \( m \). Hence \( g(c) \neq 0 \).

\( (\Leftarrow) \) Suppose \( f = (x - c)^m g \) with \( g(c) \neq 0 \). Then \( (x - c)^m \mid f \), so \( \operatorname{mult}_c(f) \ge m \). Suppose, for a contradiction, that \( (x - c)^{m+1} \mid f \), say \( f = (x - c)^{m+1}h \). Then \( (x - c)^m g = (x - c)^m (x - c) h \). Since \( (x - c)^m \neq 0 \), cancellation (@cor-polynomial-no-zero-divisors) gives \( g = (x - c)h \), and evaluating at \( c \) gives \( g(c) = 0 \) by @thm-evaluation-respects-operations, a contradiction. Every higher power \( (x - c)^k \) with \( k > m + 1 \) would also give \( (x - c)^{m+1} \mid f \). Hence \( \operatorname{mult}_c(f) = m \).
:::

The first payoff is that multiplicities add when polynomials multiply, just as exponents do.

::: {#thm-multiplicity-of-product}
[Multiplicity of a Product]

Let \( f, g \in F[x] \) be non-zero and \( c \in F \). Then \( \operatorname{mult}_c(fg) = \operatorname{mult}_c(f) + \operatorname{mult}_c(g) \).
:::

::: {.proof}
Let \( m = \operatorname{mult}_c(f) \) and \( n = \operatorname{mult}_c(g) \). By @lem-multiplicity-cofactor, \( f = (x - c)^m u \) and \( g = (x - c)^n v \) with \( u(c) \neq 0 \) and \( v(c) \neq 0 \). Then \( fg = (x - c)^{m+n} uv \), and \( (uv)(c) = u(c)v(c) \neq 0 \) by @thm-evaluation-respects-operations and @thm-field-basic-properties. By @lem-multiplicity-cofactor again, \( \operatorname{mult}_c(fg) = m + n \).
:::

::: {#exm-multiplicity-by-division}
[Finding a Multiplicity by Repeated Division]

Let \( f = x^4 - 2x^3 + 2x - 1 \in \nQ[x] \). Find the multiplicity of \( 1 \) and of \( -1 \) as roots of \( f \).
:::

::: {.solution}
We have \( f(1) = 1 - 2 + 2 - 1 = 0 \), so we divide by \( x - 1 \). Long division gives
\[
f = (x - 1)(x^3 - x^2 - x + 1).
\]
The cofactor \( g_1 = x^3 - x^2 - x + 1 \) has \( g_1(1) = 0 \), so we divide again: \( g_1 = (x - 1)(x^2 - 1) \). The new cofactor \( g_2 = x^2 - 1 \) has \( g_2(1) = 0 \), and \( g_2 = (x - 1)(x + 1) \). Now \( g_3 = x + 1 \) has \( g_3(1) = 2 \neq 0 \). Hence
\[
f = (x - 1)^3 (x + 1), \qquad g_3(1) \neq 0,
\]
and @lem-multiplicity-cofactor gives \( \operatorname{mult}_1(f) = 3 \). For \( -1 \), write \( f = (x + 1) \cdot (x - 1)^3 \), whose cofactor \( (x - 1)^3 \) takes the value \( (-2)^3 = -8 \neq 0 \) at \( -1 \). So \( \operatorname{mult}_{-1}(f) = 1 \), a simple root. The multiplicities add up to \( 3 + 1 = 4 = \deg f \).
:::

::: {.warning}
**Multiplicity is not visible from the set of roots.** The polynomials \( (x - 1)^3(x + 1) \) and \( (x - 1)(x + 1)^3 \) have the same roots \( \{1, -1\} \), the same degree and the same leading coefficient, but they are different polynomials. "The roots of \( f \)" as a set loses information; the roots **with their multiplicities** do not, as the next theorem shows for polynomials that split.
:::

::: {.check}
Over \( \nR \), what is the multiplicity of \( 0 \) as a root of \( x^3(x^2 + 1) \)? Of \( 2 \) as a root of \( (x^2 - 4)^2 \)?
:::

::: {.solution}
For \( x^3(x^2 + 1) \), the cofactor \( x^2 + 1 \) is \( 1 \neq 0 \) at \( 0 \), so the multiplicity is \( 3 \) by @lem-multiplicity-cofactor. For \( (x^2 - 4)^2 = (x - 2)^2(x + 2)^2 \), the cofactor \( (x + 2)^2 \) is \( 16 \neq 0 \) at \( 2 \), so the multiplicity is \( 2 \).
:::

## Counting roots with multiplicity

In @exm-multiplicity-by-division the multiplicities added up to exactly the degree. That cannot always happen: \( x^2 + 1 \in \nR[x] \) has degree \( 2 \) and no real roots at all. The difference is whether \( f \) breaks into linear factors, so we give that a name.

::: {#def-polynomial-splits}
[Splitting into Linear Factors]

Let \( F \) be a field. A non-zero \( f \in F[x] \) of degree \( n \) **splits over \( F \)** if there are \( a \in F \) and \( a_1, \dots, a_n \in F \), not necessarily distinct, with
\[
f = a(x - a_1)(x - a_2) \cdots (x - a_n) .
\]
:::

A non-zero constant splits (take \( n = 0 \) and the empty product \( 1 \)). The polynomial \( x^2 - 1 = (x - 1)(x + 1) \) splits over \( \nQ \). The polynomial \( x^2 - 2 \) does not split over \( \nQ \), since a linear factor \( x - a_1 \) with \( a_1 \in \nQ \) would give a rational root, but it splits over \( \nR \) as \( (x - \sqrt{2})(x + \sqrt{2}) \). The phrase **over \( F \)** carries weight: the \( a_i \) must lie in \( F \).

It turns out that the multiplicities always fit inside the degree, and they fill it exactly when \( f \) splits:

::: {#thm-roots-with-multiplicity}
[Roots Counted with Multiplicity]

Let \( F \) be a field and \( f \in F[x] \) non-zero. Let \( c_1, \dots, c_k \) be the distinct roots of \( f \) in \( F \), with multiplicities \( m_1, \dots, m_k \). Then
\[
f = (x - c_1)^{m_1} \cdots (x - c_k)^{m_k}\, g
\]
for some \( g \in F[x] \) with **no** root in \( F \). Consequently
\[
m_1 + \dots + m_k \le \deg f ,
\]
with equality if and only if \( f \) splits over \( F \).
:::

::: {.idea}
Peel off the roots one at a time. After removing \( (x - c_1)^{m_1} \), the other roots \( c_j \) are still roots of the cofactor, because \( c_j - c_1 \neq 0 \), and by @thm-multiplicity-of-product they keep their multiplicities. Whatever is left at the end has no roots, and its degree is exactly the gap between \( \deg f \) and \( \sum m_i \). The gap is zero exactly when the leftover is a constant.
:::

::: {.proof}
The set of roots is finite by @cor-root-bound-general, so the list \( c_1, \dots, c_k \) makes sense. We prove the following claim by induction on \( j \in \{0, 1, \dots, k\} \): \( f = (x - c_1)^{m_1} \cdots (x - c_j)^{m_j}\, g_j \) for some non-zero \( g_j \in F[x] \) with
\[
\operatorname{mult}_{c_i}(g_j) = 0 \text{ for } i \le j, \qquad \operatorname{mult}_{c_i}(g_j) = m_i \text{ for } i > j .
\]

For \( j = 0 \) take \( g_0 = f \). Suppose the claim holds for some \( j < k \). By @lem-multiplicity-cofactor applied to \( g_j \), we have \( g_j = (x - c_{j+1})^{m_{j+1}} g_{j+1} \) with \( g_{j+1}(c_{j+1}) \neq 0 \), which gives the product formula for \( j + 1 \) and \( \operatorname{mult}_{c_{j+1}}(g_{j+1}) = 0 \). For \( i \neq j + 1 \), the polynomial \( (x - c_{j+1})^{m_{j+1}} \) takes the value \( (c_i - c_{j+1})^{m_{j+1}} \neq 0 \) at \( c_i \), since the roots are distinct. So its multiplicity at \( c_i \) is \( 0 \) by @lem-multiplicity-cofactor (with cofactor the polynomial itself), and @thm-multiplicity-of-product gives
\[
\operatorname{mult}_{c_i}(g_j) = 0 + \operatorname{mult}_{c_i}(g_{j+1}) .
\]
This is \( 0 \) for \( i \le j \) and \( m_i \) for \( i > j + 1 \), which completes the induction.

Put \( g = g_k \). By the claim, \( \operatorname{mult}_{c_i}(g) = 0 \), that is, \( g(c_i) \neq 0 \), for every \( i \). If \( d \in F \) were a root of \( g \), then \( f(d) = (d - c_1)^{m_1} \cdots (d - c_k)^{m_k} g(d) = 0 \), so \( d \) would be one of the \( c_i \), which is impossible. Hence \( g \) has no root in \( F \).

Since \( f \neq 0 \), also \( g \neq 0 \), and @thm-degree-of-product gives \( \deg f = m_1 + \dots + m_k + \deg g \ge m_1 + \dots + m_k \).

\( (\Rightarrow) \) If equality holds, then \( \deg g = 0 \), so \( g = a \) is a non-zero constant and \( f = a(x - c_1)^{m_1} \cdots (x - c_k)^{m_k} \) splits over \( F \).

\( (\Leftarrow) \) Suppose \( f = a(x - a_1) \cdots (x - a_n) \) with \( n = \deg f \). Group equal factors: \( f = a(x - d_1)^{n_1} \cdots (x - d_l)^{n_l} \) with \( d_1, \dots, d_l \) distinct and \( n_1 + \dots + n_l = n \). By the computation above, the cofactor \( a\prod_{s \neq r}(x - d_s)^{n_s} \) is non-zero at \( d_r \), so \( \operatorname{mult}_{d_r}(f) = n_r \) by @lem-multiplicity-cofactor. Every root \( d \) of \( f \) satisfies \( a\prod_s (d - d_s)^{n_s} = 0 \), so \( d \) is one of the \( d_r \). Hence the roots of \( f \) are exactly \( d_1, \dots, d_l \), and their multiplicities add up to \( n = \deg f \). This proves the theorem.
:::

The theorem sharpens @cor-root-bound-general, because the number \( k \) of distinct roots is at most \( m_1 + \dots + m_k \). It also shows that a split polynomial is determined by its leading coefficient and its roots with multiplicities. Whether a given polynomial splits depends on the field: the fifth-degree polynomial \( (x - 1)^3(x^2 + 1) \) has root multiplicities adding up to \( 3 < 5 \) over \( \nR \), but it splits over \( \nC \) as \( (x - 1)^3(x - i)(x + i) \). In the next section we prove that over \( \nC \) **every** polynomial splits.

## The formal derivative

How do we recognize a repeated root without factoring? Over \( \nR \) calculus has an answer. At a simple root the graph of \( f \) crosses the axis with non-zero slope, while at a double root, as for \( (x - 1)^2 \) at \( 1 \), it touches the axis and the slope is \( 0 \). We would like to use this over every field, including \( \nF_p \), where there are no limits and no slopes. So we keep the formula of the derivative and throw away the limit.

*The formal derivative is the power rule, applied coefficient by coefficient.*

::: {#def-formal-derivative}
[Formal Derivative]

Let \( F \) be a field and \( f = a_0 + a_1x + \dots + a_nx^n \in F[x] \). The **formal derivative** of \( f \) is
\[
f' = a_1 + 2a_2x + 3a_3x^2 + \dots + na_nx^{n-1} = \sum_{k=1}^{n} k a_k x^{k-1} ,
\]
where \( ka_k \) is the integer multiple of \( a_k \) (the sum of \( k \) copies of \( a_k \)). Higher derivatives are defined by \( f^{(0)} = f \) and \( f^{(k+1)} = (f^{(k)})' \); we also write \( f'' = f^{(2)} \).
:::

In words: each monomial \( a_kx^k \) becomes \( ka_kx^{k-1} \), and constants disappear. This is the map \( D \) of @exm-differentiation, where we already saw that \( D \colon F[x] \to F[x] \) is linear. Over \( \nR \) it agrees with the derivative of calculus on polynomial functions, since calculus gives the same power rule. By @lem-integer-multiples, \( ka_k = (k \cdot 1)a_k \), so the integer \( k \) acts through the element \( k \cdot 1 \) of \( F \). **That element can be \( 0 \)**, and this is the source of every difference between characteristic \( 0 \) and characteristic \( p \).

Some examples. Over \( \nQ \), \( (x^4 - 2x^3 + 2x - 1)' = 4x^3 - 6x^2 + 2 \). Over any field, the derivative of a constant is \( 0 \) and \( (x - c)' = 1 \). Over \( \nF_3 \), \( (x^3 + x)' = 3x^2 + 1 = 1 \), because \( 3 \cdot 1 = 0 \) there. Over \( \nF_2 \), \( (x^2)' = 2x = 0 \): a non-constant polynomial with derivative zero.

In characteristic \( 0 \) the last example cannot happen. If \( \deg f = n \ge 1 \), the coefficient of \( x^{n-1} \) in \( f' \) is \( (n \cdot 1)a_n \), a product of two non-zero elements, so \( \deg f' = n - 1 \) and in particular \( f' \neq 0 \). In characteristic \( p \) the same coefficient vanishes whenever \( p \mid n \), because then \( n \cdot 1 = (n/p)\cdot(p \cdot 1) = 0 \) by @lem-integer-multiples.

The derivative obeys the rules we know from calculus. The proofs cannot use limits, so they go through monomials.

::: {#thm-formal-derivative-rules}
[Rules for the Formal Derivative]

Let \( F \) be a field, \( f, g \in F[x] \), \( a, b, c \in F \) and \( m \ge 1 \) an integer. Then:

::: {.enumerate options="label=(\alph*)"}
1. \( (af + bg)' = af' + bg' \), and \( a' = 0 \) for the constant polynomial \( a \);
2. \( (fg)' = f'g + fg' \) (product rule);
3. \( (g^m)' = m\,g^{m-1}g' \); in particular \( \bigl((x - c)^m\bigr)' = m(x - c)^{m-1} \).
:::
:::

::: {.idea}
Both sides of the product rule are linear in \( f \) for fixed \( g \), and linear in \( g \) for fixed \( f \). So it is enough to check the rule when \( f \) and \( g \) are monomials, where it is the identity \( i + j = i + j \) for exponents. Checking on monomials, and extending by linearity, is the standard way to prove any identity about \( D \).
:::

::: {.proof}
(a) Linearity is @exm-differentiation. A constant has no coefficients in positions \( k \ge 1 \), so its derivative is \( 0 \).

(b) First let \( f = x^i \) and \( g = x^j \) with \( i, j \in \nN \). If \( i, j \ge 1 \), then
\[
(x^{i+j})' = (i + j)x^{i+j-1} = ix^{i-1}x^j + x^i\,jx^{j-1} = f'g + fg' ,
\]
using \( (i + j) \cdot 1 = i \cdot 1 + j \cdot 1 \) from @lem-integer-multiples. If \( i = 0 \), then \( f = 1 \), \( f' = 0 \) and both sides equal \( jx^{j-1} \) (or \( 0 \) when \( j = 0 \)); the case \( j = 0 \) is symmetric.

Now let \( f = \sum_i a_ix^i \) and \( g = \sum_j b_jx^j \). By @thm-polynomial-ring-laws, \( fg = \sum_{i,j} a_ib_j\,x^ix^j \), a finite sum. Applying (a) and the monomial case,
\[
(fg)' = \sum_{i,j} a_ib_j\bigl((x^i)'x^j + x^i(x^j)'\bigr) = \Bigl(\sum_i a_i(x^i)'\Bigr)\Bigl(\sum_j b_jx^j\Bigr) + \Bigl(\sum_i a_ix^i\Bigr)\Bigl(\sum_j b_j(x^j)'\Bigr) = f'g + fg' ,
\]
where the middle equality regroups with the distributive laws, and the last uses (a) again.

(c) We use induction on \( m \). For \( m = 1 \) both sides are \( g' \). If \( (g^m)' = mg^{m-1}g' \), then by (b)
\[
(g^{m+1})' = (g^m g)' = mg^{m-1}g'\,g + g^m g' = (m + 1)g^mg' .
\]
For \( g = x - c \) we have \( g' = 1 \) by (a). This proves the theorem.
:::

## Repeated roots and the derivative

Now we can turn the calculus picture into a theorem valid over every field.

::: {#thm-repeated-root-derivative}
[Repeated Root Test]

Let \( F \) be a field, \( f \in F[x] \) non-zero and \( c \in F \).

::: {.enumerate options="label=(\alph*)"}
1. \( c \) is a multiple root of \( f \) if and only if \( f(c) = 0 \) and \( f'(c) = 0 \).
2. Suppose \( \operatorname{mult}_c(f) = m \ge 1 \) and \( m \cdot 1 \neq 0 \) in \( F \) (this holds automatically if \( F \) has characteristic \( 0 \)). Then \( f' \neq 0 \) and \( \operatorname{mult}_c(f') = m - 1 \).
:::
:::

::: {.idea}
Write \( f = (x - c)g \) and differentiate: \( f' = g + (x - c)g' \), so \( f'(c) = g(c) \). The derivative at \( c \) reads off exactly the cofactor's value, which is what @lem-multiplicity-cofactor needs. For (b), differentiate \( (x - c)^mg \) instead; the factor \( m \) appears, and it must not be \( 0 \) in \( F \).
:::

::: {.proof}
(a) \( (\Rightarrow) \) Suppose \( f = (x - c)^2 g \). By @thm-formal-derivative-rules (b) and (c), \( f' = 2(x - c)g + (x - c)^2g' \), and evaluating at \( c \) gives \( f(c) = 0 \) and \( f'(c) = 0 \).

\( (\Leftarrow) \) Suppose \( f(c) = 0 \) and \( f'(c) = 0 \). By @lem-factor-theorem-linear, \( f = (x - c)g \) for some \( g \in F[x] \). By @thm-formal-derivative-rules, \( f' = g + (x - c)g' \), so \( 0 = f'(c) = g(c) \). By @lem-factor-theorem-linear again, \( g = (x - c)h \), so \( f = (x - c)^2h \) and \( \operatorname{mult}_c(f) \ge 2 \).

(b) By @lem-multiplicity-cofactor, \( f = (x - c)^m g \) with \( g(c) \neq 0 \). By @thm-formal-derivative-rules,
\[
f' = m(x - c)^{m-1}g + (x - c)^mg' = (x - c)^{m-1}\,h, \qquad h \coloneqq mg + (x - c)g' .
\]
Then \( h(c) = (m \cdot 1)\,g(c) \), a product of two non-zero elements of \( F \), so \( h(c) \neq 0 \). In particular \( h \neq 0 \), so \( f' \neq 0 \) by @cor-polynomial-no-zero-divisors, and \( \operatorname{mult}_c(f') = m - 1 \) by @lem-multiplicity-cofactor.
:::

Part (a) holds over **every** field. Part (b) needs its hypothesis. Over \( \nF_2 \), let \( f = x^2(x + 1) = x^3 + x^2 \). Then \( \operatorname{mult}_0(f) = 2 \), and \( f' = 3x^2 + 2x = x^2 \), so \( \operatorname{mult}_0(f') = 2 \), not \( 1 \). Here \( m \cdot 1 = 2 \cdot 1 = 0 \), and the factor \( m \) killed the term that should have lowered the multiplicity.

Part (a) finds a repeated root at a known point \( c \). To decide whether **any** repeated root exists, without knowing the roots, we use the gcd of \( f \) and \( f' \), which the Euclidean algorithm (@thm-euclidean-algorithm) computes by division alone. Repeated roots are a special case of repeated irreducible factors: \( c \) is a multiple root exactly when the irreducible polynomial \( x - c \) appears squared.

::: {#cor-squarefree-gcd-derivative}
[Repeated Factors and \( \gcd(f, f') \)]

Let \( F \) be a field and \( f \in F[x] \) non-constant.

::: {.enumerate options="label=(\alph*)"}
1. (**Any field.**) If \( p \in F[x] \) is irreducible and \( p^2 \mid f \), then \( p \mid \gcd(f, f') \). Hence, if \( \gcd(f, f') = 1 \), then no irreducible polynomial divides \( f \) twice; in particular \( f \) has no multiple root in \( F \).
2. (**Characteristic \( 0 \).**) If \( F \) has characteristic \( 0 \) and \( \gcd(f, f') \neq 1 \), then \( p^2 \mid f \) for some irreducible \( p \in F[x] \).
:::
:::

::: {.idea}
For (a), differentiate \( p^2h \): every term still contains \( p \). For (b), run it backwards. An irreducible \( p \) dividing both \( f = pg \) and \( f' = p'g + pg' \) must divide \( p'g \). If \( p \) does not divide \( p' \), then Euclid's lemma pushes \( p \) into \( g \), and \( p^2 \mid f \). The only question is whether \( p \mid p' \) can happen, and that is exactly where the characteristic enters.
:::

::: {.proof}
(a) Write \( f = p^2h \). By @thm-formal-derivative-rules, \( f' = 2pp'h + p^2h' = p(2p'h + ph') \). So \( p \) is a common divisor of \( f \) and \( f' \), and \( p \mid \gcd(f, f') \) by @thm-gcd-properties. If \( \gcd(f, f') = 1 \), this would give \( p \mid 1 \), which is impossible because \( p \) is non-constant (@def-irreducible-polynomial) and a non-zero multiple of \( p \) has degree at least \( \deg p \ge 1 \) by @thm-degree-of-product. If \( c \) were a multiple root, then \( (x - c)^2 \mid f \). But \( x - c \) is irreducible (@def-irreducible-polynomial), because a product of two non-constant polynomials has degree at least \( 2 \). This is again impossible.

(b) Let \( d = \gcd(f, f') \neq 1 \). Since \( d \mid f \) and \( f \neq 0 \), \( d \neq 0 \); as \( d \) is monic and \( d \neq 1 \), \( \deg d \ge 1 \). By @thm-unique-factorization-polynomials, \( d \) has a monic irreducible factor \( p \). Then \( p \mid f \) and \( p \mid f' \) (@thm-gcd-properties). Write \( f = pg \). By @thm-formal-derivative-rules, \( f' = p'g + pg' \), so \( p \) divides \( f' - pg' = p'g \).

Since \( F \) has characteristic \( 0 \) and \( \deg p \ge 1 \), we showed after @def-formal-derivative that \( p' \neq 0 \) and \( \deg p' = \deg p - 1 \). A non-zero multiple of \( p \) has degree at least \( \deg p \), so \( p \nmid p' \). By Euclid's lemma (@thm-euclid-lemma-polynomials), \( p \mid g \). Hence \( p^2 \mid pg = f \). This proves the corollary.
:::

::: {.warning}
**In characteristic \( p \), a non-constant polynomial can have derivative \( 0 \).** Over \( \nF_p \), \( (x^p)' = (p \cdot 1)x^{p-1} = 0 \). The proof of (b) used that an irreducible factor \( q \) of \( f \) has \( q' \neq 0 \) of smaller degree, so that \( q \nmid q' \); in characteristic \( p \) that step is no longer automatic, because \( q' \) may be \( 0 \). So the correct statements are: \( \gcd(f, f') = 1 \) implies no repeated irreducible factor, over **any** field; the converse is proved here **only in characteristic \( 0 \)**. Do not use "repeated factor if and only if \( \gcd(f, f') \neq 1 \)" over a field of characteristic \( p \) without checking that no irreducible factor of \( f \) has derivative \( 0 \).
:::

::: {.remark}
The converse really can fail in characteristic \( p \), though not over the fields \( \nF_p \). Over the field of rational functions in a variable \( t \) with coefficients in \( \nF_p \), which this book does not construct, the polynomial \( x^p - t \) is irreducible, so it has no repeated factor, yet its derivative is \( 0 \).
:::

::: {#exm-gcd-with-derivative}
[Detecting a Repeated Root with a gcd]

Decide whether \( f = x^4 - 2x^3 + 2x - 1 \in \nQ[x] \) has a repeated irreducible factor, using only \( \gcd(f, f') \). Does \( f \) have a multiple root in \( \nC \)?
:::

::: {.solution}
Here \( f' = 4x^3 - 6x^2 + 2 \). Run the Euclidean algorithm (@thm-euclidean-algorithm). Dividing \( f \) by \( f' \),
\[
f = \Bigl(\tfrac14x - \tfrac18\Bigr)f' + \Bigl(-\tfrac34x^2 + \tfrac32x - \tfrac34\Bigr),
\]
and the remainder is \( -\tfrac34(x^2 - 2x + 1) \). Dividing \( f' \) by \( x^2 - 2x + 1 \),
\[
f' = (4x + 2)(x^2 - 2x + 1) + 0 .
\]
(We divided by the monic multiple of the remainder; scaling a divisor by a non-zero constant changes only the quotient, so the next remainder is still \( 0 \).) The last non-zero remainder, made monic, is the gcd: \( \gcd(f, f') = x^2 - 2x + 1 = (x - 1)^2 \neq 1 \). By @cor-squarefree-gcd-derivative (b), since \( \nQ \) has characteristic \( 0 \), \( f \) has a repeated irreducible factor. Indeed \( x - 1 \) divides the gcd, so \( 1 \) is a common root of \( f \) and \( f' \), and by @thm-repeated-root-derivative (a) it is a multiple root. This matches @exm-multiplicity-by-division, where \( \operatorname{mult}_1(f) = 3 \), and @thm-repeated-root-derivative (b) gives \( \operatorname{mult}_1(f') = 2 \), consistent with the factor \( (x - 1)^2 \) of the gcd.

So yes, \( f \) has a multiple root in \( \nC \), namely \( 1 \in \nQ \). The gcd test is useful over \( \nC \) even for polynomials with rational coefficients: the Euclidean algorithm uses only divisions in \( \nQ[x] \), and division with remainder is unique (@thm-polynomial-division), so running it in \( \nC[x] \) produces the same remainders and the same gcd. Had the gcd been \( 1 \), part (a) over \( \nC \) would have ruled out every multiple complex root, without our finding a single root.
:::

::: {.check}
Over \( \nR \), \( f = x^3 \) satisfies \( f(0) = f'(0) = 0 \). Does @thm-repeated-root-derivative say that \( 0 \) has multiplicity \( 2 \)?
:::

::: {.solution}
No. Part (a) says only that the multiplicity is **at least** \( 2 \). The actual multiplicity is \( 3 \). Part (b) applies, since \( \nR \) has characteristic \( 0 \): \( \operatorname{mult}_0(f') = \operatorname{mult}_0(3x^2) = 2 = 3 - 1 \). To pin the multiplicity down with derivatives, find the first \( k \) with \( f^{(k)}(0) \neq 0 \): here \( f''(0) = 0 \) and \( f'''(0) = 6 \neq 0 \), so \( k = 3 \).
:::

## Taylor expansion of a polynomial

The answer to the check suggests that, in characteristic \( 0 \), the derivatives of \( f \) at \( c \) know everything about \( f \) near \( c \). Calculus makes this precise with Taylor's formula. For polynomials the formula is exact, and it has a clean linear-algebra meaning: the numbers \( f^{(k)}(c)/k! \) are the coordinates of \( f \) in the basis of powers of \( x - c \), so the maps \( f \mapsto f^{(k)}(c)/k! \) form a dual basis in the sense of @def-dual-basis. In @exm-dual-basis-polynomials we saw this for \( c = 0 \) and \( n = 2 \).

We need one derivative computation. For integers \( 0 \le j \le k \), repeated use of @thm-formal-derivative-rules (c) and (a) gives
\[
\bigl((x - c)^k\bigr)^{(j)} = k(k - 1)\cdots(k - j + 1)\,(x - c)^{k-j} ,
\]
by induction on \( j \), and \( \bigl((x - c)^k\bigr)^{(j)} = 0 \) for \( j > k \), since the \( k \)-th derivative is the constant \( k! \). Evaluating at \( c \), every term with \( j < k \) vanishes because of the factor \( (x - c)^{k-j} \). Hence
\[
\bigl((x - c)^k\bigr)^{(j)}(c) = \begin{cases} k! \cdot 1 & \text{if } j = k, \\ 0 & \text{if } j \neq k. \end{cases}
\]

::: {#thm-polynomial-taylor}
[Taylor Expansion of a Polynomial]

Let \( F \) be a field, \( n \in \nN \) and \( c \in F \).

::: {.enumerate options="label=(\alph*)"}
1. The list \( \sB_c = \bigl(1, x - c, (x - c)^2, \dots, (x - c)^n\bigr) \) is a basis of \( F[x]_{\le n} \).
2. Suppose \( F \) has characteristic \( 0 \), or characteristic \( p > n \). For \( k = 0, \dots, n \) define \( \varphi_k \colon F[x]_{\le n} \to F \) by \( \varphi_k(f) = \dfrac{f^{(k)}(c)}{k!} \). Then \( (\varphi_0, \dots, \varphi_n) \) is the dual basis of \( \sB_c \), and every \( f \in F[x]_{\le n} \) satisfies
\[
f = \sum_{k=0}^{n} \frac{f^{(k)}(c)}{k!}\,(x - c)^k .
\]
:::
:::

::: {.idea}
① The powers of \( x - c \) have degrees \( 0, 1, \dots, n \), so no combination of them can cancel down to zero; there are \( n + 1 \) of them, so counting finishes (a). ② The computation above says exactly \( \varphi_j\bigl((x - c)^k\bigr) = \delta_{jk} \), once we may divide by \( k! \). ③ A list of functionals with the \( \delta \) property is the dual basis, and the dual basis expansion \( \v = \sum \varphi_k(\v)\v_k \) of @thm-dual-basis is Taylor's formula.
:::

::: {.proof}
(a) Let \( b_0 + b_1(x - c) + \dots + b_n(x - c)^n = 0 \), and suppose not all \( b_k \) are zero. Let \( k \) be the largest index with \( b_k \neq 0 \). By @thm-degree-of-product, \( b_k(x - c)^k \) has degree \( k \), and each earlier term has degree less than \( k \), so by @thm-degree-of-sum the sum has degree \( k \ge 0 \). This contradicts the sum being \( 0 \), of degree \( -\infty \). Hence \( \sB_c \) is linearly independent. It has \( n + 1 \) elements and \( \dim F[x]_{\le n} = n + 1 \) by @exm-standard-bases, so \( \sB_c \) is a basis by @thm-right-size-basis (a).

(b) First, \( k! \cdot 1 \neq 0 \) in \( F \) for \( 0 \le k \le n \). By @lem-integer-multiples, \( k! \cdot 1 = (1 \cdot 1)(2 \cdot 1)\cdots(k \cdot 1) \). In characteristic \( 0 \) each factor is non-zero by @def-characteristic; in characteristic \( p > n \), each factor \( j \cdot 1 \) with \( 1 \le j \le k < p \) is non-zero by the minimality of \( p \). A product of non-zero elements is non-zero (@thm-field-basic-properties). So \( \varphi_k \) is defined.

Each \( \varphi_k \) is linear: \( f \mapsto f^{(k)} \) is linear as a composite of copies of \( D \) (@exm-differentiation), evaluation at \( c \) is linear by @thm-evaluation-respects-operations, and so is multiplication by \( (k!)^{-1} \). The derivatives of a polynomial of degree at most \( n \) have degree at most \( n \), so \( \varphi_k \in F[x]_{\le n}^{*} \). By the computation before the theorem,
\[
\varphi_j\bigl((x - c)^k\bigr) = \frac{1}{j!}\bigl((x - c)^k\bigr)^{(j)}(c) = \delta_{jk} \qquad (0 \le j, k \le n) .
\]
By the uniqueness in @thm-dual-basis (a), \( (\varphi_0, \dots, \varphi_n) \) is the dual basis of \( \sB_c \). The first formula of @thm-dual-basis (c), \( f = \sum_k \varphi_k(f)(x - c)^k \), is the Taylor expansion. This proves the theorem.
:::

::: {#exm-taylor-expansion}
[Re-centering a Cubic]

Expand \( f = x^3 - 2x + 5 \in \nQ[x] \) in powers of \( x - 1 \).
:::

::: {.solution}
The derivatives are \( f' = 3x^2 - 2 \), \( f'' = 6x \), \( f''' = 6 \). At \( c = 1 \): \( f(1) = 4 \), \( f'(1) = 1 \), \( f''(1) = 6 \), \( f'''(1) = 6 \). By @thm-polynomial-taylor (b), since \( \nQ \) has characteristic \( 0 \),
\[
f = 4 + 1\cdot(x - 1) + \frac{6}{2}(x - 1)^2 + \frac{6}{6}(x - 1)^3 = 4 + (x - 1) + 3(x - 1)^2 + (x - 1)^3 .
\]
Check by expanding: \( (x - 1)^3 + 3(x - 1)^2 + (x - 1) + 4 = (x^3 - 3x^2 + 3x - 1) + (3x^2 - 6x + 3) + (x - 1) + 4 = x^3 - 2x + 5 \).

The expansion also reads off root information at \( 1 \): the constant term \( f(1) = 4 \neq 0 \), so \( 1 \) is not a root. In general, \( \operatorname{mult}_c(f) \) is the index of the first non-zero coordinate of \( f \) in the basis \( \sB_c \) (over any field, by part (a); in characteristic \( 0 \) these coordinates are the Taylor coefficients), because \( f = (x - c)^m\bigl(b_m + b_{m+1}(x - c) + \cdots\bigr) \) and the bracket is \( b_m \) at \( c \).
:::

::: {.warning}
**Taylor's formula needs \( k! \neq 0 \).** Over \( \nF_2 \), take \( f = x^2 \) and \( c = 0 \). Then \( f' = 2x = 0 \), so **every** derivative of \( f \), at every point, is \( 0 \), even though \( f \neq 0 \). No formula in the values \( f^{(k)}(0) \) can recover the coefficient \( 1 \) of \( x^2 \). Part (a) of @thm-polynomial-taylor still holds over \( \nF_2 \): \( x^2 \) has coordinates \( (0, 0, 1) \) in \( (1, x, x^2) \). What fails is that these coordinates are derivatives divided by \( k! \).
:::

The two halves of this section meet in Chapter 8, where a matrix is diagonalizable exactly when its minimal polynomial splits and has no repeated roots; the gcd test above is how such a condition is checked in practice. Before that, the next section proves that over \( \nC \) the sum of the multiplicities always equals the degree.

## Exercises

### A. Check your understanding

:::: {#exr-roots-and-multiplicity-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the multiplicity of \( c \) as a root of a non-zero \( f \in F[x] \). Why is \( f \neq 0 \) required?
2. True or false: if \( f(c) = f'(c) = 0 \), then \( c \) has multiplicity exactly \( 2 \). Justify your answer.
3. True or false: over every field, \( f' = 0 \) implies that \( f \) is constant. Justify your answer.
4. True or false: if \( f \in \nR[x] \) has degree \( 4 \) and the multiplicities of its real roots add up to \( 4 \), then \( f \) splits over \( \nR \). Justify your answer.
5. True or false: if \( f \in \nQ[x] \) is non-constant and \( \gcd(f, f') \neq 1 \), then \( f \) has a repeated irreducible factor. Justify your answer.
6. Name the dual basis (@thm-dual-basis) of \( \bigl(1, x - c, \dots, (x - c)^n\bigr) \) in \( \nR[x]_{\le n} \).
:::
::::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. It is the largest \( m \in \nN \) with \( (x - c)^m \mid f \) (@def-root-multiplicity). For \( f = 0 \), every power divides \( f \), so no largest \( m \) exists.
2. False. For \( f = x^3 \) and \( c = 0 \), \( f(0) = f'(0) = 0 \), but \( \operatorname{mult}_0(f) = 3 \). @thm-repeated-root-derivative (a) only gives multiplicity at least \( 2 \).
3. False. Over \( \nF_2 \), \( (x^2)' = 2x = 0 \). (In characteristic \( 0 \) it is true: \( \deg f' = \deg f - 1 \) whenever \( \deg f \ge 1 \).)
4. True. By @thm-roots-with-multiplicity, the sum of multiplicities equals the degree if and only if \( f \) splits over \( \nR \).
5. True. \( \nQ \) has characteristic \( 0 \), so this is @cor-squarefree-gcd-derivative (b).
6. \( \varphi_k(f) = f^{(k)}(c)/k! \) for \( k = 0, \dots, n \), by @thm-polynomial-taylor (b); \( \nR \) has characteristic \( 0 \).
:::
:::

### B. Practice

:::: {#exr-roots-and-multiplicity-b1}
[B1: Multiplicities over different fields]

::: {.enumerate options="label=(\alph*)"}
1. Let \( f = x^5 - 3x^4 + 4x^3 - 4x^2 + 3x - 1 \). Find \( \operatorname{mult}_1(f) \) in \( \nQ[x] \). Hence decide whether \( f \) splits over \( \nR \), and whether it splits over \( \nC \).
2. In \( \nF_2[x] \), find the roots of \( g = x^4 + x^2 \) and their multiplicities. Does \( g \) split over \( \nF_2 \)?
:::
::::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Here \( f(1) = 1 - 3 + 4 - 4 + 3 - 1 = 0 \). Dividing by \( x - 1 \) repeatedly,
\[
f = (x - 1)(x^4 - 2x^3 + 2x^2 - 2x + 1), \quad x^4 - 2x^3 + 2x^2 - 2x + 1 = (x - 1)(x^3 - x^2 + x - 1),
\]
and \( x^3 - x^2 + x - 1 = (x - 1)(x^2 + 1) \). Since \( x^2 + 1 \) takes the value \( 2 \neq 0 \) at \( 1 \), @lem-multiplicity-cofactor gives \( f = (x - 1)^3(x^2 + 1) \) and \( \operatorname{mult}_1(f) = 3 \). Over \( \nR \), \( x^2 + 1 \) has no root (\( c^2 + 1 \ge 1 \)), so the only real root of \( f \) is \( 1 \), and \( 3 < 5 = \deg f \). By @thm-roots-with-multiplicity, \( f \) does not split over \( \nR \). Over \( \nC \), \( x^2 + 1 = (x - i)(x + i) \), so \( f = (x - 1)^3(x - i)(x + i) \) splits.
2. In \( \nF_2[x] \), \( x^4 + x^2 = x^2(x^2 + 1) \), and \( x^2 + 1 = (x + 1)^2 \) because \( (x + 1)^2 = x^2 + 2x + 1 = x^2 + 1 \). Hence \( g = x^2(x + 1)^2 = (x - 0)^2(x - 1)^2 \), using \( -1 = 1 \). The cofactor \( (x + 1)^2 \) is \( 1 \) at \( 0 \), and \( x^2 \) is \( 1 \) at \( 1 \), so \( \operatorname{mult}_0(g) = \operatorname{mult}_1(g) = 2 \) by @lem-multiplicity-cofactor. These are the only elements of \( \nF_2 \), the multiplicities add to \( 4 = \deg g \), and \( g \) splits over \( \nF_2 \).
:::
:::

:::: {#exr-roots-and-multiplicity-b2}
[B2: A gcd test]

Decide whether \( f = x^4 - 2x^2 + 1 \in \nQ[x] \) has a repeated root, by computing \( \gcd(f, f') \) with the Euclidean algorithm. Hence factor \( f \) and give all multiplicities.
::::

::: {.solution}
We have \( f' = 4x^3 - 4x \). Dividing, \( f = \tfrac14x \cdot f' + (-x^2 + 1) \), since \( \tfrac14x(4x^3 - 4x) = x^4 - x^2 \). Next, \( f' = (-4x)(-x^2 + 1) + 0 \). So the last non-zero remainder is \( -x^2 + 1 \), and by @thm-euclidean-algorithm \( \gcd(f, f') = x^2 - 1 \neq 1 \). Its roots \( 1 \) and \( -1 \) are common roots of \( f \) and \( f' \), since \( x^2 - 1 = (x - 1)(x + 1) \) divides both. By @thm-repeated-root-derivative (a), \( 1 \) and \( -1 \) are multiple roots of \( f \).

To factor, note that \( (x^2 - 1)^2 = x^4 - 2x^2 + 1 = f \), so \( f = (x - 1)^2(x + 1)^2 \). By @lem-multiplicity-cofactor, \( \operatorname{mult}_1(f) = 2 \) (cofactor \( (x + 1)^2 \), value \( 4 \) at \( 1 \)) and \( \operatorname{mult}_{-1}(f) = 2 \).
:::

:::: {#exr-roots-and-multiplicity-b3}
[B3: The multiplicity of \( 1 \)]

Let \( n \ge 2 \) and \( f = x^n - nx + n - 1 \in \nQ[x] \). Prove that \( 1 \) is a root of \( f \) of multiplicity exactly \( 2 \).
::::

::: {.solution}
We have \( f(1) = 1 - n + n - 1 = 0 \), \( f' = nx^{n-1} - n \), so \( f'(1) = 0 \), and \( f'' = n(n - 1)x^{n-2} \), so \( f''(1) = n(n - 1) \neq 0 \) since \( n \ge 2 \). In particular \( f \neq 0 \). By @thm-repeated-root-derivative (a), \( m \coloneqq \operatorname{mult}_1(f) \ge 2 \). Since \( \nQ \) has characteristic \( 0 \), part (b) gives \( \operatorname{mult}_1(f') = m - 1 \ge 1 \). Apply (a) to \( f' \neq 0 \): since \( f''(1) \neq 0 \), \( 1 \) is not a multiple root of \( f' \), so \( m - 1 = 1 \). Hence \( m = 2 \).
:::

### C. Going deeper

:::: {#exr-roots-and-multiplicity-c1}
[C1: Real roots of the derivative]

Let \( f \in \nR[x] \) have degree \( n \ge 2 \) and split over \( \nR \). Prove that \( f' \) splits over \( \nR \). You may use **Rolle's theorem** from calculus: if \( a < b \) are real and \( f(a) = f(b) = 0 \), then \( f'(\xi) = 0 \) for some \( \xi \) with \( a < \xi < b \).

*Hint: count the roots of \( f' \) with multiplicity, and compare with \( \deg f' \).*
::::

::: {.solution}
Let \( c_1 < c_2 < \dots < c_k \) be the distinct real roots of \( f \), with multiplicities \( m_1, \dots, m_k \). Since \( f \) splits over \( \nR \), @thm-roots-with-multiplicity gives \( m_1 + \dots + m_k = n \).

By Rolle's theorem, for each \( i = 1, \dots, k - 1 \) there is \( \xi_i \) with \( c_i < \xi_i < c_{i+1} \) and \( f'(\xi_i) = 0 \). These \( k - 1 \) numbers are distinct, since they lie in disjoint open intervals, and none of them is a \( c_j \). Moreover, each \( c_i \) with \( m_i \ge 2 \) is a root of \( f' \) of multiplicity \( m_i - 1 \), by @thm-repeated-root-derivative (b) (characteristic \( 0 \)); for \( m_i = 1 \) the count \( m_i - 1 = 0 \) is also correct.

Since \( \deg f = n \ge 1 \) and \( \nR \) has characteristic \( 0 \), \( \deg f' = n - 1 \), so \( f' \neq 0 \). Adding the multiplicities of the distinct roots \( \xi_1, \dots, \xi_{k-1}, c_1, \dots, c_k \) of \( f' \) gives at least
\[
(k - 1) + \sum_{i=1}^{k} (m_i - 1) = (k - 1) + n - k = n - 1 = \deg f' .
\]
By @thm-roots-with-multiplicity the sum of the multiplicities of all roots of \( f' \) is at most \( \deg f' \), so it equals \( \deg f' \), and \( f' \) splits over \( \nR \).
:::

:::: {#exr-roots-and-multiplicity-c2}
[C2: \( x^p - x \) over \( \nF_p \)]

Let \( p \) be a prime and \( f = x^p - x \in \nF_p[x] \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( f' \) and deduce that \( f \) has no repeated irreducible factor.
2. Using @exr-polynomials-c2, deduce that \( x^p - x = \prod_{a \in \nF_p} (x - a) \).
3. Explain why the argument of (a) gives nothing for \( g = x^p - 1 \). Then prove that \( g = (x - 1)^p \) in \( \nF_p[x] \).
:::

*Hint for (c): for \( 0 < k < p \), use the integer identity \( k\binom{p}{k} = p\binom{p-1}{k-1} \).*
::::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. By @def-formal-derivative, \( f' = px^{p-1} - 1 = -1 \), since \( p \cdot 1 = 0 \) in \( \nF_p \). Every common divisor of \( f \) and \( -1 \) divides \( 1 \), so \( \gcd(f, f') = 1 \), and @cor-squarefree-gcd-derivative (a), which holds over every field, shows \( f \) has no repeated irreducible factor.
2. By @exr-polynomials-c2 (c), every \( a \in \nF_p \) is a root of \( f \), so each of the \( p \) elements has multiplicity at least \( 1 \). The multiplicities add up to at least \( p = \deg f \), and at most \( \deg f \) by @thm-roots-with-multiplicity. So they add up to exactly \( p \), and each is \( 1 \). By @thm-roots-with-multiplicity, \( f = \prod_{b \in \nF_p}(x - b)\,g \) with \( \deg g = p - p = 0 \), so \( g \) is a constant; comparing leading coefficients (@thm-degree-of-product), \( g = 1 \).
3. Here \( g' = px^{p-1} = 0 \), so \( \gcd(g, g') = g \neq 1 \) (the monic generator of the ideal generated by \( g \) and \( 0 \)). Part (a) of @cor-squarefree-gcd-derivative needs \( \gcd = 1 \), so it says nothing, and part (b) is only available in characteristic \( 0 \). Still, \( g(1) = 0 \) and \( g'(1) = 0 \), so \( 1 \) is a multiple root by @thm-repeated-root-derivative (a).

   For the factorization, expand with the binomial theorem (valid in the commutative ring \( \nF_p[x] \), @thm-polynomial-ring-laws): \( (x - 1)^p = \sum_{k=0}^{p} \binom{p}{k}(-1)^{p-k}x^k \), with the integers \( \binom{p}{k} \) acting as integer multiples. For \( 0 < k < p \), the identity \( k\binom{p}{k} = p\binom{p-1}{k-1} \) and @lem-integer-multiples give \( (k \cdot 1)\bigl(\binom{p}{k} \cdot 1\bigr) = (p \cdot 1)\bigl(\binom{p-1}{k-1} \cdot 1\bigr) = 0 \) in \( \nF_p \). Since \( 0 < k < p \), \( k \cdot 1 \neq 0 \) by @def-characteristic, so \( \binom{p}{k} \cdot 1 = 0 \) (@thm-field-basic-properties). Hence \( (x - 1)^p = x^p + (-1)^p \). For odd \( p \) this is \( x^p - 1 \); for \( p = 2 \) it is \( x^2 + 1 = x^2 - 1 \). So \( g = (x - 1)^p \), and \( \operatorname{mult}_1(g) = p \) by @lem-multiplicity-cofactor.
:::
:::

:::: {#exr-roots-and-multiplicity-c3}
[C3: Removing repeated factors]

Let \( F \) be a field and \( f = a\,p_1^{e_1} \cdots p_r^{e_r} \in F[x] \), where \( a \in F \setminus \{0\} \), the \( p_i \) are **distinct** monic irreducible polynomials and \( e_i \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Suppose \( F \) has characteristic \( 0 \). Prove that \( \gcd(f, f') = p_1^{e_1 - 1} \cdots p_r^{e_r - 1} \), and deduce that \( f / \gcd(f, f') = a\,p_1 \cdots p_r \).
2. Over \( \nF_2 \), let \( f = x^2(x + 1) \). Compute \( f / \gcd(f, f') \) and show that the conclusion of (a) fails.
:::

*Hint for (a): write \( D = p_1^{e_1-1}\cdots p_r^{e_r-1} \). Show \( D \mid \gcd(f, f') \); for the reverse, show \( p_i^{e_i} \nmid f' \) using Euclid's lemma.*
::::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Let \( D = \prod_i p_i^{e_i - 1} \) and \( d = \gcd(f, f') \). By @thm-formal-derivative-rules (b) and (c), applied repeatedly,
   \[
   f' = a\sum_{i=1}^{r} e_i\,p_i^{e_i - 1}p_i'\prod_{j \neq i} p_j^{e_j} .
   \]
   Every term is divisible by \( D \), and so is \( f \). Hence \( D \mid d \) by @thm-gcd-properties.

   Conversely, \( d \mid f \), so \( f = dh \). Factoring \( d \) and \( h \) into monic irreducibles and comparing with the factorization of \( f \) by the uniqueness in @thm-unique-factorization-polynomials, \( d = \prod_i p_i^{k_i} \) with \( 0 \le k_i \le e_i \) (as \( d \) is monic). Suppose \( k_i = e_i \) for some \( i \). Then \( p_i^{e_i} \mid f' \). In the formula for \( f' \) every term with index \( j \neq i \) contains \( p_i^{e_i} \), so \( p_i^{e_i} \) divides the remaining term \( a e_i p_i^{e_i - 1}p_i'\prod_{j \neq i}p_j^{e_j} \). Canceling \( p_i^{e_i - 1} \) (@cor-polynomial-no-zero-divisors), \( p_i \mid (a e_i)\,p_i'\prod_{j \neq i}p_j^{e_j} \). Here \( a e_i = a(e_i \cdot 1) \) is a non-zero constant (characteristic \( 0 \)), \( p_i \nmid p_i' \) because \( p_i' \neq 0 \) has smaller degree, and \( p_i \nmid p_j \) for \( j \neq i \) because both are monic irreducible and distinct. Applying @thm-euclid-lemma-polynomials repeatedly gives a contradiction. Hence \( k_i \le e_i - 1 \) for all \( i \), so \( d \mid D \). Both are monic and divide each other, so they have the same degree and \( d = D \). Finally \( f = D \cdot a\,p_1 \cdots p_r \), so \( f/d = a\,p_1 \cdots p_r \).
2. In \( \nF_2[x] \), \( f = x^3 + x^2 \) and \( f' = 3x^2 + 2x = x^2 \). Since \( x^2 \mid f \), \( \gcd(f, f') = x^2 \), and \( f / \gcd(f, f') = x + 1 \). The formula of (a) would predict \( \gcd(f, f') = x \) and \( f/\gcd(f, f') = x(x + 1) \). The irreducible factor \( x \) has been lost. The step that fails is "\( a e_i \neq 0 \)": here \( e_1 = 2 \) and \( 2 \cdot 1 = 0 \) in \( \nF_2 \).
:::
:::
