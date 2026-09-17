# Interpolation and the Chinese Remainder Theorem

Chapter 2 proved that through \( n + 1 \) points with distinct \( x \)-values there passes exactly one polynomial of degree at most \( n \) (@thm-interpolation-unique). The proof went through an invertible matrix, and it never wrote the polynomial down. This section gives the formula. Then it reads interpolation in the arithmetic of this chapter: "\( p(c) = y \)" says that \( p \) leaves remainder \( y \) on division by \( x - c \). Prescribing remainders modulo several pairwise coprime polynomials at once is the Chinese Remainder Theorem. We prove it twice, once with Bézout's identity, which gives a formula, and once by counting dimensions in the quotient spaces \( F[x]/\langle m \rangle \).

## The Lagrange basis

Suppose we want the polynomial of degree at most \( n \) taking prescribed values \( y_0, \dots, y_n \) at distinct points \( c_0, \dots, c_n \). The problem is linear in the data: if \( p \) fits the values \( (y_i) \) and \( q \) fits \( (y_i') \), then \( p + q \) fits \( (y_i + y_i') \), by @thm-evaluation-respects-operations. So it is enough to solve the simplest data sets, a single \( 1 \) and zeros everywhere else, and add up.

The polynomial that vanishes at every \( c_j \) with \( j \ne i \) is easy to write: \( \prod_{j \ne i}(x - c_j) \). At \( c_i \) it takes the value \( \prod_{j \ne i}(c_i - c_j) \), which is a product of non-zero scalars, so we can divide by it. In @exm-dual-basis-polynomials we met these polynomials for the three points \( -1, 0, 1 \). Here is the general case.

*The \( i \)-th Lagrange polynomial is the polynomial of degree \( n \) that is \( 1 \) at the \( i \)-th node and \( 0 \) at every other node.*

::: {#def-lagrange-basis}
[Lagrange Basis]

Let \( n \in \nN \), and let \( c_0, c_1, \dots, c_n \in F \) be **distinct**. For \( i = 0, \dots, n \), the \( i \)-th **Lagrange polynomial** for these nodes is
\[
\ell_i(x) \coloneqq \prod_{\substack{j = 0 \\ j \ne i}}^{n} \frac{x - c_j}{c_i - c_j} \in F[x].
\]
The list \( (\ell_0, \dots, \ell_n) \) is the **Lagrange basis** for the nodes \( c_0, \dots, c_n \).
:::

In words: the numerator makes \( \ell_i \) vanish at every node except \( c_i \), and the denominator rescales so that the value at \( c_i \) is exactly \( 1 \). The points \( c_i \) are called **nodes**.

**Well-definedness.** Each denominator \( c_i - c_j \) with \( j \ne i \) is non-zero because the nodes are **distinct**, so the quotients exist in \( F \). The product has \( n \) linear factors, each with leading coefficient \( (c_i - c_j)^{-1} \ne 0 \), so \( \deg \ell_i = n \) by @thm-degree-of-product. The name "basis" is justified by the theorem below.

**Examples.**

- **One node.** For \( n = 0 \) the product is empty, so \( \ell_0 = 1 \). The degenerate case is consistent: a polynomial of degree at most \( 0 \) with value \( y_0 \) at \( c_0 \) is the constant \( y_0 = y_0\ell_0 \).
- **Two nodes.** For \( c_0 = 0 \), \( c_1 = 1 \) we get \( \ell_0 = \frac{x - 1}{0 - 1} = 1 - x \) and \( \ell_1 = \frac{x - 0}{1 - 0} = x \). The line through \( (0, y_0) \) and \( (1, y_1) \) is \( y_0(1 - x) + y_1x \).
- **Three nodes.** For \( -1, 0, 1 \), \( \ell_{-1} = \frac{x(x - 1)}{(-1)(-2)} = \tfrac12x(x - 1) \), \( \ell_0 = \frac{(x + 1)(x - 1)}{(1)(-1)} = 1 - x^2 \) and \( \ell_1 = \tfrac12x(x + 1) \), the polynomials of @exm-dual-basis-polynomials. (Here we index the nodes by their values.)

**Non-example by minimal change.** Take the nodes \( 0, 1, 1 \). The numerator of \( \ell_1 \) is still defined, \( (x - 0)(x - 1) \), but the denominator contains \( c_1 - c_2 = 0 \), which has no inverse. No rescaling helps: a polynomial that vanishes at \( c_2 = 1 \) cannot take the value \( 1 \) at \( c_1 = 1 \). The clause that fails is "distinct".

Everything about the Lagrange polynomials follows from one table of values, the Kronecker delta \( \ell_i(c_j) = \delta_{ij} \).

::: {#thm-lagrange-interpolation}
[Lagrange Interpolation]

Let \( n \in \nN \), let \( c_0, \dots, c_n \in F \) be distinct, and let \( (\ell_0, \dots, \ell_n) \) be the Lagrange basis for these nodes.

::: {.enumerate options="label=(\alph*)"}
1. \( \ell_i(c_j) = \delta_{ij} \) for all \( i, j \in \{0, \dots, n\} \).
2. \( (\ell_0, \dots, \ell_n) \) is a basis of \( F[x]_{\le n} \), and every \( p \in F[x]_{\le n} \) satisfies
   \[
   p = \sum_{i=0}^{n} p(c_i)\,\ell_i .
   \]
3. For all \( y_0, \dots, y_n \in F \), the unique \( p \in F[x]_{\le n} \) with \( p(c_i) = y_i \) for every \( i \) is
   \[
   p = \sum_{i=0}^{n} y_i\,\ell_i .
   \]
:::
:::

::: {.idea}
① The delta table is a direct evaluation. ② Evaluating a vanishing combination \( \sum a_i\ell_i \) at \( c_j \) kills every term but \( a_j \), so the list is independent, and it has the right length, so we count instead of checking spanning. ③ The expansion of \( p \) and the interpolation formula are the same computation: both sides of a candidate identity are polynomials of degree at most \( n \) with the same values at \( n + 1 \) nodes.
:::

::: {.proof}
(a) By @thm-evaluation-respects-operations, \( \ell_i(c_j) = \prod_{k \ne i} \frac{c_j - c_k}{c_i - c_k} \). If \( j = i \), every factor is \( 1 \), so \( \ell_i(c_i) = 1 \). If \( j \ne i \), the factor with \( k = j \) is \( 0 \), so \( \ell_i(c_j) = 0 \).

(b) Each \( \ell_i \) has degree \( n \), so it lies in \( F[x]_{\le n} \). Let \( a_0\ell_0 + \dots + a_n\ell_n = 0 \). Evaluating at \( c_j \) and using (a) gives \( 0 = \sum_i a_i\delta_{ij} = a_j \) for each \( j \). Hence the list is linearly independent. It has length \( n + 1 = \dim F[x]_{\le n} \) (@exm-standard-bases), so it is a basis by @thm-right-size-basis (a).

Now let \( p \in F[x]_{\le n} \), and put \( q = p - \sum_i p(c_i)\ell_i \in F[x]_{\le n} \). By (a), \( q(c_j) = p(c_j) - p(c_j) = 0 \) for every \( j \). So \( q \) has the \( n + 1 \) distinct roots \( c_0, \dots, c_n \) and degree at most \( n \). By @cor-root-bound-general, \( q = 0 \), which is the expansion of \( p \).

(c) By (a), \( \bigl(\sum_i y_i\ell_i\bigr)(c_j) = \sum_i y_i\delta_{ij} = y_j \), so \( \sum_i y_i\ell_i \) has the required values, and it lies in \( F[x]_{\le n} \). By @thm-interpolation-unique, it is the only such polynomial. This proves the theorem.
:::

So Chapter 2's existence statement now comes with a formula, and the uniqueness half of (c) is the expansion in (b) read backwards: a polynomial of degree at most \( n \) is determined by its values at the nodes, because those values are its coordinates in the Lagrange basis.

::: {#exm-lagrange-cubic}
[The Chapter 2 Cubic by Lagrange's Formula]

Use @thm-lagrange-interpolation to find the \( p \in \nQ[x]_{\le 3} \) with \( p(-1) = 2 \), \( p(0) = 1 \), \( p(1) = 2 \) and \( p(2) = 11 \), and compare with @exm-interpolation-cubic.
:::

::: {.solution}
The nodes \( -1, 0, 1, 2 \) are distinct. Write \( \ell_{-1}, \ell_0, \ell_1, \ell_2 \) for the Lagrange polynomials, indexed by the node. The denominators are \( \prod_{j \ne i}(c_i - c_j) \):
\[
\ell_{-1} = \frac{x(x - 1)(x - 2)}{(-1)(-2)(-3)} = -\tfrac16x(x - 1)(x - 2), \qquad
\ell_0 = \frac{(x + 1)(x - 1)(x - 2)}{(1)(-1)(-2)} = \tfrac12(x + 1)(x - 1)(x - 2),
\]
\[
\ell_1 = \frac{(x + 1)x(x - 2)}{(2)(1)(-1)} = -\tfrac12(x + 1)x(x - 2), \qquad
\ell_2 = \frac{(x + 1)x(x - 1)}{(3)(2)(1)} = \tfrac16(x + 1)x(x - 1).
\]
Expanding,
\[
\ell_{-1} = -\tfrac16x^3 + \tfrac12x^2 - \tfrac13x, \quad \ell_0 = \tfrac12x^3 - x^2 - \tfrac12x + 1, \quad \ell_1 = -\tfrac12x^3 + \tfrac12x^2 + x, \quad \ell_2 = \tfrac16x^3 - \tfrac16x .
\]
By @thm-lagrange-interpolation (c), \( p = 2\ell_{-1} + \ell_0 + 2\ell_1 + 11\ell_2 \). Collecting coefficients:
\[
x^3\colon\ -\tfrac13 + \tfrac12 - 1 + \tfrac{11}{6} = 1, \qquad x^2\colon\ 1 - 1 + 1 + 0 = 1, \qquad x\colon\ -\tfrac23 - \tfrac12 + 2 - \tfrac{11}{6} = -1, \qquad 1\colon\ 1 .
\]
Hence \( p = x^3 + x^2 - x + 1 \), the polynomial found by elimination in @exm-interpolation-cubic, as uniqueness demands. The elimination solved a \( 4 \times 4 \) system for these particular values. The Lagrange polynomials were computed once, and would serve for any other values at the same nodes.
:::

::: {.warning}
**The interpolant has degree at most \( n \), not exactly \( n \).** Through the three points \( (0, 0), (1, 1), (2, 2) \) the formula gives \( 0 \cdot \ell_0 + 1 \cdot \ell_1 + 2\ell_2 \), where \( \ell_1 = -x(x - 2) \) and \( \ell_2 = \tfrac12x(x - 1) \); this is \( -x^2 + 2x + x^2 - x = x \). The degree-\( 2 \) terms cancel, because the points lie on a line. Each \( \ell_i \) has degree exactly \( n \), but a combination of them need not.
:::

::: {.check}
Let \( n \ge 1 \) and let \( (\ell_0, \dots, \ell_n) \) be the Lagrange basis for distinct nodes \( c_0, \dots, c_n \). What is \( \sum_{i=0}^{n} c_i\ell_i \)?
:::

::: {.solution}
It is the polynomial \( x \). Indeed \( x \in F[x]_{\le n} \) since \( n \ge 1 \), and its values at the nodes are \( c_0, \dots, c_n \), so @thm-lagrange-interpolation (b) gives \( x = \sum_i c_i\ell_i \).
:::

## Evaluations are the dual basis

The delta table \( \ell_i(c_j) = \delta_{ij} \) can be read the other way round. For \( c \in F \), evaluation at \( c \) is the linear functional \( \varepsilon_c \colon p \mapsto p(c) \) (@exm-linear-functionals), which we restrict to \( F[x]_{\le n} \). Then the table says \( \varepsilon_{c_j}(\ell_i) = \delta_{ji} \): the evaluations at the nodes behave on the Lagrange basis exactly as a dual basis must (@thm-dual-basis). @exr-linear-functionals-c3 proved from @thm-interpolation-unique that the evaluations form the dual basis of **some** basis. We can now name that basis.

::: {#cor-evaluations-dual-to-lagrange}
[Evaluations Are Dual to the Lagrange Basis]

Let \( c_0, \dots, c_n \in F \) be distinct, with Lagrange basis \( (\ell_0, \dots, \ell_n) \). Then \( (\varepsilon_{c_0}, \dots, \varepsilon_{c_n}) \) is the dual basis of \( (\ell_0, \dots, \ell_n) \) in \( F[x]_{\le n}^{*} \). In particular, every linear functional \( \varphi \) on \( F[x]_{\le n} \) is a combination of evaluations at the nodes:
\[
\varphi = \sum_{i=0}^{n} \varphi(\ell_i)\,\varepsilon_{c_i} .
\]
:::

::: {.proof}
The evaluations are linear (@exm-linear-functionals), and \( \varepsilon_{c_i}(\ell_j) = \ell_j(c_i) = \delta_{ij} \) by @thm-lagrange-interpolation (a). Since \( (\ell_0, \dots, \ell_n) \) is a basis (@thm-lagrange-interpolation (b)), the uniqueness in @thm-dual-basis (a) shows that the evaluations are its dual basis. The formula for \( \varphi \) is the second formula of @thm-dual-basis (c).
:::

The first formula of @thm-dual-basis (c), \( p = \sum_i \varepsilon_{c_i}(p)\,\ell_i \), is the expansion in @thm-lagrange-interpolation (b). So Lagrange's formula is the statement "a vector is recovered from its dual-basis coordinates", for the space \( F[x]_{\le n} \) and the measurements "value at \( c_i \)".

The formula for \( \varphi \) has a practical reading: **any** linear measurement of a polynomial of degree at most \( n \) can be computed from \( n + 1 \) of its values, with weights \( \varphi(\ell_i) \) that do not depend on the polynomial.

::: {#exm-quadrature-weights}
[Integrals and Slopes from Values]

::: {.enumerate options="label=(\alph*)"}
1. Find \( w_0, w_1, w_2 \in \nR \) such that \( \int_0^1 p(t)\,\dd t = w_0\,p(0) + w_1\,p(\tfrac12) + w_2\,p(1) \) for every \( p \in \nR[x]_{\le 2} \).
2. Express \( p \mapsto p'(0) \) on \( \nR[x]_{\le 2} \) as a combination of \( \varepsilon_{-1}, \varepsilon_0, \varepsilon_1 \).
:::
:::

::: {.solution}
(a) Integration over \( [0, 1] \) is a linear functional on \( \nR[x]_{\le 2} \) (@exm-linear-functionals). For the nodes \( 0, \tfrac12, 1 \),
\[
\ell_0 = \frac{(x - \frac12)(x - 1)}{(-\frac12)(-1)} = 2x^2 - 3x + 1, \qquad \ell_{1/2} = \frac{x(x - 1)}{(\frac12)(-\frac12)} = -4x^2 + 4x, \qquad \ell_1 = \frac{x(x - \frac12)}{(1)(\frac12)} = 2x^2 - x .
\]
Their integrals are \( \tfrac23 - \tfrac32 + 1 = \tfrac16 \), \( -\tfrac43 + 2 = \tfrac23 \) and \( \tfrac23 - \tfrac12 = \tfrac16 \). By @cor-evaluations-dual-to-lagrange,
\[
\int_0^1 p(t)\,\dd t = \tfrac16\,p(0) + \tfrac23\,p(\tfrac12) + \tfrac16\,p(1) \qquad \text{for all } p \in \nR[x]_{\le 2}.
\]
Check with \( p = x^2 \): the right side is \( \tfrac23 \cdot \tfrac14 + \tfrac16 = \tfrac13 = \int_0^1 t^2\,\dd t \). This is Simpson's rule, which here is exact rather than approximate because \( p \) has degree at most \( 2 \).

(b) With \( \ell_{-1} = \tfrac12x(x - 1) \), \( \ell_0 = 1 - x^2 \) and \( \ell_1 = \tfrac12x(x + 1) \), the derivatives at \( 0 \) are \( -\tfrac12 \), \( 0 \) and \( \tfrac12 \). Hence \( p'(0) = \tfrac12\bigl(p(1) - p(-1)\bigr) \) for every \( p \in \nR[x]_{\le 2} \), the symmetric difference quotient, exact on quadratics.
:::

## Congruences and the Chinese Remainder Theorem

Now we change the point of view. By @thm-remainder-theorem, the remainder of \( p \) on division by \( x - c \) is \( p(c) \). So the interpolation conditions \( p(c_i) = y_i \) say that \( p \) leaves the remainder \( y_i \) on division by \( x - c_i \), for each \( i \). Nothing in this reformulation needs the divisors to be linear. What happens if we prescribe the remainders modulo arbitrary polynomials \( m_1, \dots, m_k \)? The integers faced the same question long ago, which explains the name of the answer. We first need the language of congruences, copied from \( \nZ \).

::: {#def-congruence-polynomials}
[Congruence Modulo a Polynomial]

Let \( m \in F[x] \). Two polynomials \( f, g \in F[x] \) are **congruent modulo \( m \)**, written \( f \equiv g \pmod{m} \), if \( m \mid f - g \).
:::

For example, \( x^2 \equiv -1 \pmod{x^2 + 1} \), and \( f \equiv f(c) \pmod{x - c} \) for every \( f \), by @thm-remainder-theorem. Congruence modulo \( m \) is an equivalence relation, and it respects sums and products: if \( f \equiv f' \) and \( g \equiv g' \pmod m \), then \( f + g - (f' + g') = (f - f') + (g - g') \) and \( fg - f'g' = f(g - g') + (f - f')g' \) are divisible by \( m \). By @thm-polynomial-division, if \( m \ne 0 \), every \( f \) is congruent modulo \( m \) to **exactly one** polynomial of degree less than \( \deg m \), its remainder: \( f = qm + r \) gives \( f \equiv r \), and if \( f \equiv r \equiv r' \) with both degrees below \( \deg m \), then \( m \mid r - r' \) with \( \deg(r - r') < \deg m \), which forces \( r - r' = 0 \).

Interpolation needed distinct nodes. The general condition is that the moduli share no factor, and the proof needs a way to pass from "coprime in pairs" to "coprime to the product".

::: {#lem-coprime-product}
[Coprime to Each, Coprime to the Product]

::: {.enumerate options="label=(\alph*)"}
1. Let \( p, q_1, \dots, q_s \in F[x] \). If \( p \) is coprime to each \( q_j \), then there are \( a, b \in F[x] \) with \( ap + b\,q_1 \cdots q_s = 1 \), and \( p \) is coprime to \( q_1 \cdots q_s \).
2. Let \( m_1, \dots, m_k \in F[x] \) be non-zero and **pairwise coprime**, that is, \( \gcd(m_i, m_j) = 1 \) whenever \( i \ne j \). If \( m_i \mid h \) for every \( i \), then \( m_1 \cdots m_k \mid h \).
:::
:::

::: {.proof}
(a) By @cor-bezout-polynomials, for each \( j \) there are \( a_j, b_j \) with \( a_jp + b_jq_j = 1 \). Multiplying these \( s \) identities,
\[
1 = \prod_{j=1}^{s} (a_jp + b_jq_j) = ap + (b_1 \cdots b_s)\,q_1 \cdots q_s
\]
for some \( a \in F[x] \), because every term of the expanded product except \( (b_1q_1) \cdots (b_sq_s) \) contains a factor \( a_jp \). Let \( d = \gcd(p, q_1 \cdots q_s) \). By @thm-gcd-properties, \( d \) divides \( p \) and \( q_1 \cdots q_s \), hence divides \( ap + b\,q_1 \cdots q_s = 1 \), where \( b = b_1 \cdots b_s \). So \( d \) is a non-zero constant by @thm-degree-of-product, and being monic, \( d = 1 \). Hence \( p \) and \( q_1 \cdots q_s \) are coprime (@def-coprime).

(b) We use induction on \( k \). For \( k = 1 \) there is nothing to prove. Let \( k \ge 2 \). The moduli \( m_1, \dots, m_{k-1} \) are pairwise coprime and each divides \( h \), so by the induction hypothesis \( M \coloneqq m_1 \cdots m_{k-1} \) divides \( h \), say \( h = Mg \). Since \( m_k \mid h = Mg \), and \( m_k \) is coprime to \( M \) by (a), @thm-coprime-divides-product gives \( m_k \mid g \), say \( g = m_kg' \). Then \( h = m_1 \cdots m_k\,g' \), as claimed.
:::

::: {#thm-crt-polynomials}
[Chinese Remainder Theorem for Polynomials]

Let \( m_1, \dots, m_k \in F[x] \) be non-zero and pairwise coprime, and put \( m = m_1 \cdots m_k \). For all \( r_1, \dots, r_k \in F[x] \):

::: {.enumerate options="label=(\alph*)"}
1. there is \( f \in F[x] \) with \( f \equiv r_i \pmod{m_i} \) for every \( i \);
2. if \( f \) and \( g \) both satisfy (a), then \( f \equiv g \pmod{m} \);
3. there is **exactly one** such \( f \) with \( \deg f < \deg m \).
:::
:::

::: {.idea}
Copy Lagrange. There, \( \ell_i \) was \( 1 \) at \( c_i \) and \( 0 \) at the other nodes; in the new language, \( \ell_i \equiv 1 \pmod{x - c_i} \) and \( \ell_i \equiv 0 \pmod{x - c_j} \). So we look for \( e_i \) with \( e_i \equiv 1 \pmod{m_i} \) and \( e_i \equiv 0 \pmod{m_j} \) for \( j \ne i \), and then \( f = \sum_i r_ie_i \) works. To be \( 0 \) modulo every other \( m_j \), \( e_i \) should be a multiple of \( M_i = \prod_{j \ne i} m_j \); to be \( 1 \) modulo \( m_i \), it should be \( 1 - a\,m_i \). Bézout's identity \( a\,m_i + b\,M_i = 1 \) provides exactly such an element: \( e_i = b\,M_i \).
:::

::: {.proof}
(a) Fix \( i \), and let \( M_i = \prod_{j \ne i} m_j \). Since \( m_i \) is coprime to each \( m_j \) with \( j \ne i \), @lem-coprime-product (a) gives \( a_i, b_i \in F[x] \) with \( a_im_i + b_iM_i = 1 \). Put \( e_i = b_iM_i \). Then \( e_i - 1 = -a_im_i \), so \( e_i \equiv 1 \pmod{m_i} \), and \( m_j \mid M_i \mid e_i \) for \( j \ne i \), so \( e_i \equiv 0 \pmod{m_j} \). Let \( f = r_1e_1 + \dots + r_ke_k \). Since congruence modulo \( m_j \) respects sums and products,
\[
f \equiv r_1 \cdot 0 + \dots + r_j \cdot 1 + \dots + r_k \cdot 0 = r_j \pmod{m_j}
\]
for each \( j \).

(b) If \( f \) and \( g \) satisfy (a), then \( f - g \equiv r_i - r_i = 0 \pmod{m_i} \), that is, \( m_i \mid f - g \), for every \( i \). By @lem-coprime-product (b), \( m \mid f - g \).

(c) Since each \( m_i \ne 0 \), \( m \ne 0 \) (@thm-degree-of-product). Let \( f \) be as in (a), and let \( f_0 \) be its remainder on division by \( m \) (@thm-polynomial-division). Then \( m_i \mid m \mid f - f_0 \), so \( f_0 \equiv f \equiv r_i \pmod{m_i} \) for each \( i \), and \( \deg f_0 < \deg m \). If \( g \) is another solution with \( \deg g < \deg m \), then \( m \mid f_0 - g \) by (b), and \( \deg(f_0 - g) < \deg m \), so \( f_0 = g \). This proves the theorem.
:::

**Lagrange is the case \( m_i = x - c_i \).** For distinct nodes, \( (x - c_j) - (x - c_i) = c_i - c_j \) is a non-zero constant, so \( \frac{1}{c_i - c_j}(x - c_j) - \frac{1}{c_i - c_j}(x - c_i) = 1 \), and any common divisor of \( x - c_i \) and \( x - c_j \) divides \( 1 \): the moduli are pairwise coprime. The congruence \( f \equiv y_i \pmod{x - c_i} \) means \( f(c_i) = y_i \) by @thm-remainder-theorem, and \( \deg m = n + 1 \). So part (c) is @thm-interpolation-unique. The element \( e_i \) has degree less than \( n + 1 \) after reduction modulo \( m \), is \( 1 \) at \( c_i \) and \( 0 \) at the other nodes, so after reduction it is \( \ell_i \).

::: {#exm-crt-polynomials}
[A Linear and a Quadratic Modulus]

Find the polynomial \( f \in \nQ[x] \) of degree less than \( 3 \) with
\[
f \equiv 1 \pmod{x - 2}, \qquad f \equiv 2x - 1 \pmod{x^2 + 1}.
\]
:::

::: {.solution}
*Bézout.* Divide \( x^2 + 1 \) by \( x - 2 \): \( x^2 + 1 = (x + 2)(x - 2) + 5 \). Hence
\[
\tfrac15(x^2 + 1) - \tfrac15(x + 2)(x - 2) = 1,
\]
and the moduli are coprime, since any common divisor divides \( 1 \).

*The elements \( e_i \).* Put \( e_1 = \tfrac15(x^2 + 1) \) and \( e_2 = -\tfrac15(x + 2)(x - 2) = 1 - e_1 \). Then \( e_1 \) is a multiple of \( x^2 + 1 \) and \( e_1 = 1 + \tfrac15(x + 2)(x - 2) \equiv 1 \pmod{x - 2} \); symmetrically, \( e_2 \equiv 0 \pmod{x - 2} \) and \( e_2 \equiv 1 \pmod{x^2 + 1} \).

*Combine and reduce.* By the proof of @thm-crt-polynomials, \( f \equiv 1 \cdot e_1 + (2x - 1)e_2 \pmod{(x - 2)(x^2 + 1)} \). Expanding,
\[
e_1 + (2x - 1)e_2 = \tfrac15(x^2 + 1) - \tfrac15(2x - 1)(x^2 - 4) = \tfrac15\bigl(-2x^3 + 2x^2 + 8x - 3\bigr).
\]
Dividing by \( m = (x - 2)(x^2 + 1) = x^3 - 2x^2 + x - 2 \) gives quotient \( -\tfrac25 \) and remainder
\[
f = \tfrac15\bigl(-2x^2 + 10x - 7\bigr).
\]
*Check.* \( f(2) = \tfrac15(-8 + 20 - 7) = 1 \), so \( f \equiv 1 \pmod{x - 2} \). Modulo \( x^2 + 1 \), \( x^2 \equiv -1 \), so \( f \equiv \tfrac15(2 + 10x - 7) = 2x - 1 \).
:::

::: {.warning}
**The moduli must be coprime in pairs; coprime as a whole family is not enough.** Without coprimality a system can be unsolvable: with \( m_1 = x \) and \( m_2 = x^2 \), the system \( f \equiv 0 \pmod{x} \), \( f \equiv 1 \pmod{x^2} \) has no solution: the first condition says \( f(0) = 0 \), the second says \( f = 1 + x^2q \), so \( f(0) = 1 \). For three moduli, \( x \), \( x - 1 \) and \( x(x - 1) \) have no common factor, yet the first and third share \( x \), and \( f \equiv 0 \pmod x \), \( f \equiv 1 \pmod{x(x - 1)} \) is again impossible.
:::

::: {#exm-hermite-via-crt}
[Values and Slopes by CRT]

::: {.enumerate options="label=(\alph*)"}
1. Let \( c, a, b \in F \) and \( f \in F[x] \). Show that \( f \equiv a + b(x - c) \pmod{(x - c)^2} \) if and only if \( f(c) = a \) and \( f'(c) = b \).
2. Find the \( p \in \nQ[x]_{\le 3} \) with \( p(0) = 2 \), \( p'(0) = -1 \), \( p(1) = 1 \) and \( p'(1) = 3 \).
:::
:::

::: {.solution}
(a) Divide by \( (x - c)^2 \): \( f = q(x - c)^2 + r \) with \( \deg r \le 1 \) (@thm-polynomial-division). Writing \( r = r_0 + r_1(x - c) \), which is possible because \( (1, x - c) \) is a basis of \( F[x]_{\le 1} \) by @thm-distinct-degrees-independent and @thm-right-size-basis, the uniqueness of the remainder says \( f \equiv a + b(x - c) \) exactly when \( r_0 = a \) and \( r_1 = b \). Now \( f(c) = r_0 \). By @thm-formal-derivative-rules, \( f' = q'(x - c)^2 + 2q(x - c) + r_1 \), so \( f'(c) = r_1 \). Hence the congruence holds if and only if \( f(c) = a \) and \( f'(c) = b \).

(b) By (a), the conditions are \( p \equiv 2 - x \pmod{x^2} \) and \( p \equiv 1 + 3(x - 1) \pmod{(x - 1)^2} \). The moduli are coprime, since
\[
(2x + 1)(x - 1)^2 - (2x - 3)x^2 = (2x^3 - 3x^2 + 1) - (2x^3 - 3x^2) = 1 .
\]
So \( e_0 = (2x + 1)(x - 1)^2 \) is \( \equiv 0 \pmod{(x - 1)^2} \) and \( \equiv 1 \pmod{x^2} \), while \( e_1 = -(2x - 3)x^2 = 3x^2 - 2x^3 \) is \( \equiv 0 \pmod{x^2} \) and \( \equiv 1 \pmod{(x - 1)^2} \). The polynomial \( e_1 \) is the smooth step \( 3x^2 - 2x^3 \) of @exm-hermite-existence: value \( 0 \) and slope \( 0 \) at \( 0 \), value \( 1 \) and slope \( 0 \) at \( 1 \). By @thm-crt-polynomials, \( p \) is the remainder of
\[
(2 - x)e_0 + (3x - 2)e_1 = -8x^4 + 20x^3 - 12x^2 - x + 2
\]
on division by \( x^2(x - 1)^2 = x^4 - 2x^3 + x^2 \). Adding \( 8(x^4 - 2x^3 + x^2) \) gives
\[
p = 4x^3 - 4x^2 - x + 2 .
\]
*Check.* \( p(0) = 2 \); \( p' = 12x^2 - 8x - 1 \), so \( p'(0) = -1 \); \( p(1) = 4 - 4 - 1 + 2 = 1 \); \( p'(1) = 12 - 8 - 1 = 3 \).
:::

The same recipe handles any finite set of nodes \( c_i \) with multiplicities \( k_i \): the moduli \( (x - c_i)^{k_i} \) are pairwise coprime for distinct nodes, by @lem-coprime-product (a) applied twice: first \( x - c_i \) is coprime to \( (x - c_j)^{k_j} \), and then \( (x - c_j)^{k_j} \) is coprime to \( (x - c_i)^{k_i} \). So for any prescribed remainders modulo \( (x - c_i)^{k_i} \), there is exactly one polynomial of degree less than \( k_1 + \dots + k_s \) with those remainders. In characteristic \( 0 \), the Taylor expansion of @thm-polynomial-taylor translates "the remainder modulo \( (x - c)^k \)" into the values \( f(c), f'(c), \dots, f^{(k-1)}(c) \), and this is **Hermite interpolation**.

## The quotient space \( F[x]/\langle m \rangle \)

Congruence modulo \( m \) is equality of cosets. The ideal \( \langle m \rangle \) is a subspace of \( F[x] \): it is non-empty and closed under addition and under multiplication by constant polynomials (@def-ideal-polynomials). So the quotient space \( F[x]/\langle m \rangle \) of @def-quotient-space exists, and by @lem-coset-equality (b),
\[
f + \langle m \rangle = g + \langle m \rangle \iff f - g \in \langle m \rangle \iff f \equiv g \pmod{m} .
\]
An element of \( F[x]/\langle m \rangle \) is a polynomial "known only modulo \( m \)". We cannot quote @thm-dimension-quotient for its dimension, because \( F[x] \) is infinite-dimensional (@thm-polynomials-infinite-dimensional). The remainder does the job instead.

::: {#thm-dimension-polynomial-quotient}
[Dimension of \( F[x]/\langle m \rangle \)]

Let \( m \in F[x] \) be non-zero of degree \( d \). Then \( F[x]/\langle m \rangle \) is finite-dimensional with
\[
\dim F[x]/\langle m \rangle = \deg m = d .
\]
If \( d \ge 1 \), the cosets \( (1 + \langle m \rangle, x + \langle m \rangle, \dots, x^{d-1} + \langle m \rangle) \) form a basis.
:::

::: {.proof}
If \( d = 0 \), then \( m \) is a non-zero constant, and every \( f = (m^{-1}f)m \) lies in \( \langle m \rangle \). So \( \langle m \rangle = F[x] \) and the quotient is the zero space, of dimension \( 0 \).

Let \( d \ge 1 \), and define \( \rho \colon F[x] \to F[x]_{\le d-1} \) by letting \( \rho(f) \) be the remainder of \( f \) on division by \( m \) (@thm-polynomial-division). *Linear.* If \( f = q_1m + \rho(f) \) and \( g = q_2m + \rho(g) \), then for \( c \in F \),
\[
cf + g = (cq_1 + q_2)m + \bigl(c\rho(f) + \rho(g)\bigr),
\]
and \( \deg(c\rho(f) + \rho(g)) < d \) by @thm-degree-of-sum. By the uniqueness in @thm-polynomial-division, \( \rho(cf + g) = c\rho(f) + \rho(g) \). *Surjective.* If \( \deg r < d \), then \( r = 0 \cdot m + r \), so \( \rho(r) = r \). *Kernel.* \( \rho(f) = 0 \) exactly when \( f = qm \) for some \( q \), that is, \( f \in \langle m \rangle \).

By the First Isomorphism Theorem (@thm-first-isomorphism), \( \bar\rho \colon F[x]/\langle m \rangle \to F[x]_{\le d-1} \), \( f + \langle m \rangle \mapsto \rho(f) \), is a well-defined injective linear map with image \( \im \rho = F[x]_{\le d-1} \), so it is an isomorphism. Since \( \bar\rho(x^j + \langle m \rangle) = x^j \) for \( j < d \), and \( (1, x, \dots, x^{d-1}) \) is a basis of \( F[x]_{\le d-1} \) (@exm-standard-bases), the inverse isomorphism \( \bar\rho^{-1} \) carries it to the basis \( (x^j + \langle m \rangle)_{j < d} \) (@thm-isomorphism-preserves-bases). Hence \( \dim F[x]/\langle m \rangle = d \).
:::

For example, \( \nR[x]/\langle x^2 + 1 \rangle \) has basis \( (1 + \langle x^2 + 1 \rangle, x + \langle x^2 + 1 \rangle) \), so each element is \( a + bx + \langle x^2 + 1 \rangle \) for unique \( a, b \in \nR \).

::: {.remark}
Cosets can also be **multiplied**: \( (f + \langle m \rangle)(g + \langle m \rangle) \coloneqq fg + \langle m \rangle \) is well defined, because congruence modulo \( m \) respects products. In \( \nR[x]/\langle x^2 + 1 \rangle \), \( x \cdot x = x^2 \equiv -1 \), so the coset of \( x \) squares to minus the coset of \( 1 \), and \( (a + bx)(a' + b'x) \equiv (aa' - bb') + (ab' + a'b)x \): this is multiplication in \( \nC \), with the coset of \( x \) playing the role of \( i \).
:::

The Chinese Remainder Theorem now becomes a statement about linear maps. Reducing a polynomial modulo each \( m_i \) records its \( k \) remainders; the theorem says that this record, taken modulo \( m \), is a perfect dictionary. Recall from @def-product-of-spaces that \( V_1 \times \dots \times V_k \) is the space of lists with entrywise operations.

::: {#thm-crt-isomorphism}
[CRT as an Isomorphism]

Let \( m_1, \dots, m_k \in F[x] \) be non-zero and pairwise coprime, and put \( m = m_1 \cdots m_k \). Then
\[
\Phi \colon F[x]/\langle m \rangle \to F[x]/\langle m_1 \rangle \times \dots \times F[x]/\langle m_k \rangle, \qquad f + \langle m \rangle \mapsto \bigl(f + \langle m_1 \rangle, \dots, f + \langle m_k \rangle\bigr),
\]
is a well-defined isomorphism of vector spaces.
:::

::: {.idea}
The map that does not care about well-definedness is \( \Psi \colon f \mapsto (f + \langle m_i \rangle)_i \) on \( F[x] \) itself. Its kernel is the set of polynomials divisible by every \( m_i \), which is \( \langle m \rangle \) by @lem-coprime-product. So the First Isomorphism Theorem makes \( \Phi \) well defined and injective in one stroke. For surjectivity we do **not** construct a preimage. We count: both sides have dimension \( \deg m \), because degrees add under products.
:::

::: {.proof}
Let \( \Psi \colon F[x] \to F[x]/\langle m_1 \rangle \times \dots \times F[x]/\langle m_k \rangle \), \( \Psi(f) = (f + \langle m_1 \rangle, \dots, f + \langle m_k \rangle) \). Each entry is a quotient map, which is linear by @thm-quotient-space-operations-well-defined (c), and the operations in the product are entrywise, so \( \Psi \) is linear. By @lem-coset-equality (b), \( \Psi(f) = \0 \) if and only if \( m_i \mid f \) for every \( i \). If \( m \mid f \), then \( m_i \mid f \) for all \( i \), since \( m_i \mid m \); conversely, if every \( m_i \mid f \), then \( m \mid f \) by @lem-coprime-product (b). Hence \( \ker \Psi = \langle m \rangle \).

By the First Isomorphism Theorem (@thm-first-isomorphism), the rule \( f + \langle m \rangle \mapsto \Psi(f) \) is a well-defined injective linear map; this is \( \Phi \). By @thm-dimension-polynomial-quotient, @thm-degree-of-product and @thm-dimension-of-product,
\[
\dim F[x]/\langle m \rangle = \deg m = \sum_{i=1}^{k} \deg m_i = \sum_{i=1}^{k} \dim F[x]/\langle m_i \rangle = \dim\Bigl(F[x]/\langle m_1 \rangle \times \dots \times F[x]/\langle m_k \rangle\Bigr).
\]
Since \( \Phi \) is injective between spaces of the same finite dimension, it is bijective by @cor-rank-nullity-consequences (e), hence an isomorphism (@def-isomorphism).
:::

Surjectivity of \( \Phi \) is the existence part of @thm-crt-polynomials, and injectivity is the uniqueness part. So the count has given a second proof of the Chinese Remainder Theorem, one that never uses Bézout's identity for existence. It is the same trade as in @exm-interpolation-by-counting: counting proves that a solution exists, and the Bézout construction says what it is. By the remark above, \( \Phi \) also respects products of cosets, since reduction modulo each \( m_i \) does. In Chapter 8 this splitting of \( F[x]/\langle m \rangle \) into pieces, one for each coprime factor of \( m \), reappears as a splitting of a space on which an operator acts. The next section begins that story.

::: {.check}
What is \( \dim \nQ[x]/\langle x^3 - x \rangle \)? Into which three spaces does @thm-crt-isomorphism split it, and what does \( \Phi \) do to the coset of \( x^2 \)?
:::

::: {.solution}
By @thm-dimension-polynomial-quotient, the dimension is \( 3 \). Since \( x^3 - x = x(x - 1)(x + 1) \) with distinct linear factors, which are pairwise coprime, \( \Phi \) maps it isomorphically onto \( \nQ[x]/\langle x \rangle \times \nQ[x]/\langle x - 1 \rangle \times \nQ[x]/\langle x + 1 \rangle \), a product of three one-dimensional spaces. Modulo \( x - c \), a polynomial is congruent to its value at \( c \), so \( \Phi(x^2 + \langle x^3 - x \rangle) \) is the list of cosets of the constants \( 0, 1, 1 \): the values of \( x^2 \) at \( 0, 1, -1 \).
:::

## Exercises

### A. Check your understanding

:::: {#exr-interpolation-and-crt-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the Lagrange basis for distinct nodes \( c_0, \dots, c_n \), and state the value of \( \ell_i \) at \( c_j \).
2. True or false: for four distinct nodes, the polynomial of degree at most \( 3 \) through the four points always has degree exactly \( 3 \). Justify your answer.
3. State the Chinese Remainder Theorem for polynomials, with all hypotheses.
4. True or false: if \( \gcd(m_1, m_2, m_3) = 1 \), then every system \( f \equiv r_i \pmod{m_i} \), \( i = 1, 2, 3 \), has a solution. Justify your answer.
5. What is \( \dim_{\nR} \nR[x]/\langle x^4 + 1 \rangle \)? Give a basis.
6. Which functional on \( F[x]_{\le n} \) is the \( i \)-th vector of the dual basis (@thm-dual-basis) of the Lagrange basis?
:::
::::

::: {.solution}
(a) For distinct \( c_0, \dots, c_n \in F \), \( \ell_i = \prod_{j \ne i} \frac{x - c_j}{c_i - c_j} \) (@def-lagrange-basis), and \( \ell_i(c_j) = \delta_{ij} \) (@thm-lagrange-interpolation (a)).

(b) False. The points \( (0, 0), (1, 0), (2, 0), (3, 0) \) are fitted by the zero polynomial, of degree \( -\infty \); by uniqueness (@thm-interpolation-unique), that is the interpolant.

(c) If \( m_1, \dots, m_k \in F[x] \) are non-zero and pairwise coprime and \( m = m_1 \cdots m_k \), then for all \( r_1, \dots, r_k \in F[x] \) there is \( f \) with \( f \equiv r_i \pmod{m_i} \) for each \( i \), unique modulo \( m \), and exactly one such \( f \) has \( \deg f < \deg m \) (@thm-crt-polynomials).

(d) False. \( x \), \( x - 1 \), \( x(x - 1) \) have gcd \( 1 \) as a family, but \( f \equiv 0 \pmod x \), \( f \equiv 0 \pmod{x - 1} \), \( f \equiv 1 \pmod{x(x - 1)} \) has no solution: the last condition gives \( f(0) = 1 \), contradicting the first.

(e) \( 4 \), with basis \( (1, x, x^2, x^3) \) of cosets modulo \( \langle x^4 + 1 \rangle \), by @thm-dimension-polynomial-quotient.

(f) Evaluation at the \( i \)-th node, \( \varepsilon_{c_i} \colon p \mapsto p(c_i) \) (@cor-evaluations-dual-to-lagrange).
:::

### B. Practice

:::: {#exr-interpolation-and-crt-b1}
[B1: A Lagrange interpolant]

Let \( c_0, c_1, c_2, c_3 = 0, 1, 2, 3 \). Write down the Lagrange basis for these nodes in factored form, and use it to find the \( p \in \nQ[x]_{\le 3} \) with \( p(0) = 1 \), \( p(1) = 0 \), \( p(2) = 1 \) and \( p(3) = 10 \). Hence compute \( p(4) \).
::::

::: {.solution}
The denominators \( \prod_{j \ne i}(c_i - c_j) \) are \( (-1)(-2)(-3) = -6 \), \( (1)(-1)(-2) = 2 \), \( (2)(1)(-1) = -2 \) and \( (3)(2)(1) = 6 \). So
\[
\ell_0 = -\tfrac16(x - 1)(x - 2)(x - 3), \quad \ell_1 = \tfrac12x(x - 2)(x - 3), \quad \ell_2 = -\tfrac12x(x - 1)(x - 3), \quad \ell_3 = \tfrac16x(x - 1)(x - 2).
\]
By @thm-lagrange-interpolation (c), \( p = \ell_0 + 0 \cdot \ell_1 + \ell_2 + 10\ell_3 \). Expanding each needed term,
\[
\ell_0 = -\tfrac16(x^3 - 6x^2 + 11x - 6), \qquad \ell_2 = -\tfrac12(x^3 - 4x^2 + 3x), \qquad 10\ell_3 = \tfrac53(x^3 - 3x^2 + 2x).
\]
The coefficient of \( x^3 \) is \( -\tfrac16 - \tfrac12 + \tfrac53 = 1 \); of \( x^2 \), \( 1 + 2 - 5 = -2 \); of \( x \), \( -\tfrac{11}{6} - \tfrac32 + \tfrac{10}{3} = 0 \); the constant is \( 1 \). Hence
\[
p = x^3 - 2x^2 + 1 .
\]
Check: \( p(0) = 1 \), \( p(1) = 0 \), \( p(2) = 8 - 8 + 1 = 1 \), \( p(3) = 27 - 18 + 1 = 10 \). Hence \( p(4) = 64 - 32 + 1 = 33 \).
:::

:::: {#exr-interpolation-and-crt-b2}
[B2: A CRT system]

Find the polynomial \( f \in \nQ[x] \) of degree less than \( 3 \) with \( f \equiv 2 \pmod{x - 1} \) and \( f \equiv x \pmod{x^2 + 1} \). Hence describe all \( g \in \nQ[x] \) satisfying both congruences.
::::

::: {.solution}
*Bézout.* \( x^2 + 1 = (x + 1)(x - 1) + 2 \), so \( \tfrac12(x^2 + 1) - \tfrac12(x + 1)(x - 1) = 1 \), and the moduli are coprime.

*The elements \( e_i \).* \( e_1 = \tfrac12(x^2 + 1) \) is a multiple of \( x^2 + 1 \) and \( e_1 = 1 + \tfrac12(x + 1)(x - 1) \equiv 1 \pmod{x - 1} \). And \( e_2 = 1 - e_1 = -\tfrac12(x + 1)(x - 1) \) is a multiple of \( x - 1 \) with \( e_2 \equiv 1 \pmod{x^2 + 1} \).

*Combine and reduce.* By the proof of @thm-crt-polynomials, \( f \equiv 2e_1 + xe_2 = (x^2 + 1) - \tfrac12x(x^2 - 1) = -\tfrac12x^3 + x^2 + \tfrac12x + 1 \). Modulo \( m = (x - 1)(x^2 + 1) = x^3 - x^2 + x - 1 \), add \( \tfrac12m \):
\[
f = -\tfrac12x^3 + x^2 + \tfrac12x + 1 + \tfrac12(x^3 - x^2 + x - 1) = \tfrac12x^2 + x + \tfrac12 = \tfrac12(x + 1)^2 .
\]
*Check.* \( f(1) = 2 \). Modulo \( x^2 + 1 \), \( f \equiv \tfrac12(-1) + x + \tfrac12 = x \).

By @thm-crt-polynomials (b), and since every \( g \equiv f \pmod m \) satisfies both congruences (because \( x - 1 \) and \( x^2 + 1 \) divide \( m \)), the solutions are exactly \( g = \tfrac12(x + 1)^2 + h\,(x - 1)(x^2 + 1) \) with \( h \in \nQ[x] \).
:::

:::: {#exr-interpolation-and-crt-b3}
[B3: The Lagrange basis sums to one]

Let \( c_0, \dots, c_n \in F \) be distinct with Lagrange basis \( (\ell_0, \dots, \ell_n) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \ell_0 + \ell_1 + \dots + \ell_n = 1 \).
2. Prove more generally that \( \sum_{i=0}^{n} c_i^{\,k}\,\ell_i = x^k \) for \( k = 0, 1, \dots, n \) (with \( c^0 = 1 \)).
3. For \( n = 2 \) and nodes \( 0, 1, 2 \), verify (a) by expanding.
:::
::::

::: {.solution}
(a) This is (b) with \( k = 0 \).

(b) Let \( 0 \le k \le n \). Then \( x^k \in F[x]_{\le n} \), and its value at \( c_i \) is \( c_i^{\,k} \) (@def-polynomial-evaluation). By @thm-lagrange-interpolation (b), \( x^k = \sum_i c_i^{\,k}\ell_i \).

(c) \( \ell_0 = \frac{(x - 1)(x - 2)}{2} = \tfrac12x^2 - \tfrac32x + 1 \), \( \ell_1 = \frac{x(x - 2)}{-1} = -x^2 + 2x \), \( \ell_2 = \frac{x(x - 1)}{2} = \tfrac12x^2 - \tfrac12x \). Adding: \( x^2 \) has coefficient \( \tfrac12 - 1 + \tfrac12 = 0 \), \( x \) has \( -\tfrac32 + 2 - \tfrac12 = 0 \), and the constant is \( 1 \). So the sum is \( 1 \).
:::

### C. Going deeper

:::: {#exr-interpolation-and-crt-c1}
[C1: Interpolation over a finite field]

Let \( p \) be a prime and \( F = \nF_p \).

::: {.enumerate options="label=(\alph*)"}
1. Explain why @thm-lagrange-interpolation cannot be applied with more than \( p \) nodes.
2. Let \( E \colon \nF_p[x]_{\le p} \to \nF_p^{\,p} \), \( E(f) = (f(0), f(1), \dots, f(p - 1)) \). Prove that \( E \) is linear and surjective but not injective, and find a non-zero polynomial in \( \ker E \).
3. Deduce that every function \( \nF_p \to \nF_p \) is the polynomial function of exactly one polynomial of degree at most \( p - 1 \), but of more than one polynomial of degree at most \( p \).
:::
::::

::: {.solution}
(a) The theorem needs distinct nodes, and \( \nF_p \) has only \( p \) elements, so there are no \( p + 1 \) distinct nodes.

(b) *Linear.* Each entry \( f \mapsto f(c) \) is linear by @thm-evaluation-respects-operations. *Surjective.* The \( p \) elements \( 0, 1, \dots, p - 1 \) of \( \nF_p \) are distinct nodes, so for every \( (y_0, \dots, y_{p-1}) \), @thm-lagrange-interpolation (c) with \( n = p - 1 \) gives \( f = \sum_i y_i\ell_i \in \nF_p[x]_{\le p - 1} \subseteq \nF_p[x]_{\le p} \) with \( E(f) = (y_0, \dots, y_{p-1}) \). *Not injective.* \( \dim \nF_p[x]_{\le p} = p + 1 > p = \dim \nF_p^{\,p} \), so \( E \) is not injective by @cor-rank-nullity-consequences (c). Concretely, \( g = \prod_{c \in \nF_p}(x - c) \) is monic of degree \( p \), hence non-zero, and \( g(c) = 0 \) for every \( c \in \nF_p \), because one factor vanishes (@thm-evaluation-respects-operations).

(c) A function \( \nF_p \to \nF_p \) is the same as its list of values \( (y_0, \dots, y_{p-1}) \). By (b), the restriction of \( E \) to \( \nF_p[x]_{\le p-1} \) is surjective, and it is injective because a polynomial of degree at most \( p - 1 \) vanishing at \( p \) distinct points is \( 0 \) (@cor-root-bound-general). So exactly one polynomial of degree at most \( p - 1 \) has the given values. In degree at most \( p \), if \( f \) has the given values, so does \( f + g \ne f \), with \( g \) from (b). Unlike over \( \nR \), a polynomial over \( \nF_p \) is not determined by its function.
:::

:::: {#exr-interpolation-and-crt-c2}
[C2: Newton's form of the interpolant]

Let \( c_0, \dots, c_n \in F \) be distinct. Put \( N_0 = 1 \) and \( N_k = (x - c_0)(x - c_1) \cdots (x - c_{k-1}) \) for \( 1 \le k \le n + 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( (N_0, \dots, N_n) \) is a basis of \( F[x]_{\le n} \).
2. Let \( p = \sum_{k=0}^{n} a_kN_k \). Show that \( p(c_i) = \sum_{k=0}^{i} a_kN_k(c_i) \) and \( N_i(c_i) \ne 0 \). Explain why the coefficients \( a_0, a_1, \dots \) of the interpolant can be found one at a time, and show that \( a_0 = y_0 \) and \( a_1 = \frac{y_1 - y_0}{c_1 - c_0} \).
3. Let \( p_n \in F[x]_{\le n} \) interpolate \( y_0, \dots, y_n \) at \( c_0, \dots, c_n \), and let \( c_{n+1} \) be a further node, distinct from the others, with a value \( y_{n+1} \). Prove that the interpolant \( p_{n+1} \in F[x]_{\le n+1} \) is
   \[
   p_{n+1} = p_n + \frac{y_{n+1} - p_n(c_{n+1})}{N_{n+1}(c_{n+1})}\,N_{n+1} .
   \]
4. Find the Newton form of the interpolant of @exr-interpolation-and-crt-b1, and then the interpolant after adding the point \( (4, 0) \). Why is this more economical than recomputing with Lagrange's formula?
:::

*Hint: for (c), check the values of the right-hand side at all \( n + 2 \) nodes.*
::::

::: {.solution}
(a) \( N_k \) is a product of \( k \) monic linear factors, so it is monic of degree \( k \) (@thm-degree-of-product). The polynomials \( N_0, \dots, N_n \) are non-zero with pairwise distinct degrees, hence linearly independent by @thm-distinct-degrees-independent. The list has length \( n + 1 = \dim F[x]_{\le n} \), so it is a basis by @thm-right-size-basis (a).

(b) For \( k > i \), \( N_k \) contains the factor \( x - c_i \), so \( N_k(c_i) = 0 \); this gives the formula for \( p(c_i) \). And \( N_i(c_i) = \prod_{j < i}(c_i - c_j) \) is a product of non-zero scalars, since the nodes are distinct, so it is non-zero. The conditions \( p(c_i) = y_i \) therefore form a lower triangular system: the \( i \)-th equation involves only \( a_0, \dots, a_i \), with coefficient \( N_i(c_i) \ne 0 \) on \( a_i \). Solving in the order \( i = 0, 1, \dots, n \) determines each \( a_i \) from the earlier ones. For \( i = 0 \): \( p(c_0) = a_0 \), so \( a_0 = y_0 \). For \( i = 1 \): \( y_1 = a_0 + a_1(c_1 - c_0) \), so \( a_1 = \frac{y_1 - y_0}{c_1 - c_0} \), the slope of the chord, the first "divided difference".

(c) Let \( q \) be the right-hand side; the division is legal because \( N_{n+1}(c_{n+1}) \ne 0 \) by (b). Then \( \deg q \le n + 1 \). For \( i \le n \), \( N_{n+1}(c_i) = 0 \), so \( q(c_i) = p_n(c_i) = y_i \). At \( c_{n+1} \), \( q(c_{n+1}) = p_n(c_{n+1}) + y_{n+1} - p_n(c_{n+1}) = y_{n+1} \). By @thm-interpolation-unique, \( q = p_{n+1} \).

(d) With nodes \( 0, 1, 2, 3 \): \( N_1 = x \), \( N_2 = x(x - 1) \), \( N_3 = x(x - 1)(x - 2) \). Forward substitution: \( a_0 = p(0) = 1 \); \( 0 = p(1) = 1 + a_1 \), so \( a_1 = -1 \); \( 1 = p(2) = 1 - 2 + 2a_2 \), so \( a_2 = 1 \); \( 10 = p(3) = 1 - 3 + 6 + 6a_3 \), so \( a_3 = 1 \). Thus
\[
p_3 = 1 - x + x(x - 1) + x(x - 1)(x - 2) = x^3 - 2x^2 + 1,
\]
agreeing with @exr-interpolation-and-crt-b1. Adding \( (4, 0) \): \( p_3(4) = 33 \) and \( N_4(4) = 4 \cdot 3 \cdot 2 \cdot 1 = 24 \), so by (c)
\[
p_4 = x^3 - 2x^2 + 1 - \tfrac{33}{24}\,x(x - 1)(x - 2)(x - 3) = x^3 - 2x^2 + 1 - \tfrac{11}{8}\,x(x - 1)(x - 2)(x - 3).
\]
One checks \( p_4(4) = 33 - \tfrac{11}{8} \cdot 24 = 0 \). Adding a node changes **every** Lagrange polynomial, since each \( \ell_i \) acquires a new factor; in Newton's form the old coefficients \( a_0, \dots, a_n \) survive and only one new coefficient is computed.
:::
