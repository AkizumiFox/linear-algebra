# Division with Remainder

Integers can be divided with a remainder: \( 17 = 3 \cdot 5 + 2 \), and the remainder \( 2 \) is smaller than the divisor \( 5 \). Polynomials over a field can be divided in the same way, with "smaller" measured by degree. Chapter 0 stated this fact without proof, and Chapter 3 proved the special case of dividing by \( x - c \). This section proves division with remainder in general, over any field, and draws the first consequences: the language of divisibility, the Remainder and Factor Theorems for every divisor \( x - c \), a sharper root bound, and the fact that over an infinite field a polynomial is determined by its values. Throughout, \( F \) is a field unless we say otherwise, and it matters: the warning in the second subsection shows division failing when the coefficients only form \( \nZ \).

## Long division by hand

At school one divides \( x^4 + 2x^3 - x + 3 \) by \( x^2 + x - 1 \) with a layout that imitates long division of numbers. Let us do it in words, so that we can see what each step does.

Write \( f = x^4 + 2x^3 - x + 3 \) and \( g = x^2 + x - 1 \), in \( \nQ[x] \).

1. The leading term of \( f \) is \( x^4 \), and the leading term of \( g \) is \( x^2 \). The quotient \( x^4 / x^2 = x^2 \) is the first term of the answer. Subtract \( x^2 g = x^4 + x^3 - x^2 \):
\[
f - x^2 g = x^3 + x^2 - x + 3 .
\]
2. The leading term is now \( x^3 \), and \( x^3 / x^2 = x \). Subtract \( x g = x^3 + x^2 - x \):
\[
f - x^2 g - x g = 3 .
\]
3. What is left, \( 3 \), has degree \( 0 \), smaller than \( \deg g = 2 \). No multiple \( c\,x^k g \) with \( k \ge 0 \) can remove it without creating terms of degree at least \( 2 \). We stop.

So \( f = (x^2 + x)\,g + 3 \): the **quotient** is \( x^2 + x \) and the **remainder** is \( 3 \). Expanding \( (x^2 + x)(x^2 + x - 1) = x^4 + 2x^3 - x \) confirms it.

Two questions are hidden in this routine. **Why does it always stop?** Each step removes the current leading term, so the degree of what is left drops by at least one. Degrees are natural numbers, and a strictly decreasing sequence of natural numbers cannot go on forever. **Why is the answer unique?** Someone else might hope to find a different quotient and a different remainder of degree less than \( 2 \). We will see that they cannot, by comparing degrees.

There is also a third, quieter question. In step 1 we divided the leading coefficient of the current polynomial by the leading coefficient of \( g \). Here that coefficient was \( 1 \). In general it is some \( b \neq 0 \), and we need \( b^{-1} \). Over a field this always exists. That is exactly where the field enters.

## The Division Theorem

The routine above works for every pair of polynomials with non-zero divisor. Here is the precise statement.

::: {#thm-polynomial-division}
[Polynomial Division with Remainder]

Let \( F \) be a field, and let \( f, g \in F[x] \) with \( g \neq 0 \). Then there exist **unique** polynomials \( q, r \in F[x] \) such that
\[
f = qg + r \qquad \text{and} \qquad \deg r < \deg g .
\]
:::

The polynomial \( q \) is the **quotient** and \( r \) is the **remainder** of \( f \) on division by \( g \). Because \( \deg 0 = -\infty \), the condition \( \deg r < \deg g \) allows \( r = 0 \), which is the case "\( g \) goes into \( f \) exactly".

::: {.idea}
Existence is the hand routine turned into an induction on \( \deg f \). If \( \deg f < \deg g \), there is nothing to do: \( q = 0 \), \( r = f \). Otherwise subtract \( (a/b)\,x^{n-m} g \), where \( a x^n \) and \( b x^m \) are the leading terms of \( f \) and \( g \). This kills the leading term of \( f \), so the induction hypothesis applies to what is left. Uniqueness is "take the difference": if \( qg + r = q'g + r' \), then \( (q - q')g = r' - r \). The right side has degree less than \( \deg g \), while a non-zero multiple of \( g \) has degree at least \( \deg g \).
:::

::: {.proof}
Let \( m = \deg g \), which lies in \( \nN \) since \( g \neq 0 \), and let \( b \neq 0 \) be the leading coefficient of \( g \).

*Existence.* If \( f = 0 \), then \( q = 0 \) and \( r = 0 \) work. For non-zero \( f \) we prove, by strong induction on \( n \in \nN \) (@thm-strong-induction with \( n_0 = 0 \)), the statement

> \( P(n) \): for every \( f \in F[x] \) with \( \deg f = n \), there are \( q, r \in F[x] \) with \( f = qg + r \) and \( \deg r < m \).

Let \( n \in \nN \), assume \( P(k) \) for all \( k < n \), and let \( \deg f = n \) with leading coefficient \( a \).

*Case 1: \( n < m \).* Take \( q = 0 \) and \( r = f \). Then \( f = 0 \cdot g + f \) and \( \deg r = n < m \).

*Case 2: \( n \ge m \).* Since \( F \) is a field and \( b \neq 0 \), the inverse \( b^{-1} \) exists. Put
\[
f_1 = f - a b^{-1} x^{n - m} g .
\]
By @thm-degree-of-product, the polynomial \( a b^{-1} x^{n-m} g \) has degree \( (n - m) + m = n \) and leading coefficient \( a b^{-1} \cdot b = a \). So the coefficient of \( x^n \) in \( f_1 \) is \( a - a = 0 \), and all coefficients of higher powers are \( 0 \) as well. Hence \( f_1 = 0 \) or \( \deg f_1 < n \). If \( f_1 = 0 \), then \( f = a b^{-1} x^{n-m} g + 0 \), and we take \( q = a b^{-1} x^{n-m} \), \( r = 0 \). Otherwise \( k = \deg f_1 < n \), and the induction hypothesis \( P(k) \) gives \( q_1, r_1 \) with \( f_1 = q_1 g + r_1 \) and \( \deg r_1 < m \). Then
\[
f = f_1 + a b^{-1} x^{n-m} g = \bigl( a b^{-1} x^{n-m} + q_1 \bigr) g + r_1 ,
\]
so \( q = a b^{-1} x^{n-m} + q_1 \) and \( r = r_1 \) work. This proves \( P(n) \), and by strong induction \( P(n) \) holds for every \( n \in \nN \).

*Uniqueness.* Suppose \( f = qg + r = q'g + r' \) with \( \deg r < m \) and \( \deg r' < m \). Then \( (q - q')g = r' - r \). By @thm-degree-of-sum, \( \deg(r' - r) \le \max(\deg r', \deg r) < m \), since \( -r \) has the same degree as \( r \). Suppose \( q \neq q' \). Then \( \deg(q - q') \ge 0 \), and @thm-degree-of-product gives \( \deg\bigl((q - q')g\bigr) = \deg(q - q') + m \ge m \), a contradiction. Hence \( q = q' \). Then \( r' - r = 0 \cdot g = 0 \), so \( r = r' \). This proves the theorem.
:::

The field axioms did essential work in two places: the inverse \( b^{-1} \) in Case 2, and @thm-degree-of-product in the uniqueness step, which needs a product of non-zero coefficients to be non-zero. The proof is also an algorithm. Case 2, repeated, is the long division of the previous subsection, and the induction guarantees that it stops after at most \( \deg f - \deg g + 1 \) subtractions.

The hypothesis "over a field" is not decoration. **The leading coefficient of \( g \) must be invertible.**

::: {.warning}
**Division with remainder fails over \( \nZ \).** Write \( \nZ[x] \) for the polynomials in \( \nQ[x] \) whose coefficients are all integers. Try to divide \( f = x^2 \) by \( g = 2x \) inside \( \nZ[x] \): we want \( q, r \in \nZ[x] \) with \( x^2 = 2x \cdot q + r \) and \( \deg r < 1 \), so \( r \) is a constant. Comparing coefficients of \( x^2 \) gives \( 2 q_1 = 1 \), where \( q_1 \) is the coefficient of \( x \) in \( q \). No integer \( q_1 \) satisfies this, so no such \( q, r \) exist. Over \( \nQ \) there is no problem: \( x^2 = 2x \cdot \tfrac12 x + 0 \). The obstacle is precisely that \( 2 \) has no inverse in \( \nZ \).
:::

Division by a divisor whose leading coefficient **is** invertible still works over \( \nZ \), for example by a monic polynomial; see Exercise C1.

::: {.check}
Why must the inequality \( \deg r < \deg g \) be strict? Find two different pairs \( (q, r) \) with \( x^2 = q \cdot (x^2 + 1) + r \) and \( \deg r \le 2 \).
:::

::: {.solution}
Both \( x^2 = 1 \cdot (x^2 + 1) + (-1) \) and \( x^2 = 0 \cdot (x^2 + 1) + x^2 \) work, with remainders of degree \( 0 \) and \( 2 \). With \( \deg r \le \deg g \) allowed, uniqueness fails, because we may move one copy of \( g \) between \( qg \) and \( r \). The strict inequality is exactly what rules this out: in the uniqueness proof, \( \deg(r' - r) < \deg g \) is the step that forces \( q = q' \).
:::

Now a division in which the leading coefficient of the divisor is not \( 1 \), so fractions appear.

::: {#exm-long-division}
[Long Division with a Non-Monic Divisor]

In \( \nQ[x] \), divide \( f = 2x^4 - 3x^3 + x^2 + 4x - 1 \) by \( g = 2x^2 - x + 3 \) with remainder.
:::

::: {.solution}
We follow Case 2 of the proof, where \( b = 2 \) and \( b^{-1} = \tfrac12 \).

*Step 1.* The leading term of \( f \) is \( 2x^4 \), and \( 2x^4 / 2x^2 = x^2 \). Subtracting \( x^2 g = 2x^4 - x^3 + 3x^2 \) leaves
\[
f - x^2 g = -2x^3 - 2x^2 + 4x - 1 .
\]
*Step 2.* The leading term is \( -2x^3 \), and \( -2x^3 / 2x^2 = -x \). Subtracting \( -x g = -2x^3 + x^2 - 3x \) leaves
\[
-3x^2 + 7x - 1 .
\]
*Step 3.* The leading term is \( -3x^2 \), and \( -3x^2 / 2x^2 = -\tfrac32 \). Subtracting \( -\tfrac32 g = -3x^2 + \tfrac32 x - \tfrac92 \) leaves
\[
\bigl(7 - \tfrac32\bigr)x + \bigl(-1 + \tfrac92\bigr) = \tfrac{11}{2}x + \tfrac72 .
\]
This has degree \( 1 < 2 = \deg g \), so we stop. Hence
\[
2x^4 - 3x^3 + x^2 + 4x - 1 = \bigl(x^2 - x - \tfrac32\bigr)(2x^2 - x + 3) + \tfrac{11}{2}x + \tfrac72 ,
\]
with quotient \( q = x^2 - x - \tfrac32 \) and remainder \( r = \tfrac{11}{2}x + \tfrac72 \). By the uniqueness in @thm-polynomial-division, any other correct method must produce the same \( q \) and \( r \).

Notice that the quotient has a non-integer coefficient although \( f \) and \( g \) have integer coefficients. This is the warning above in action: over \( \nZ \) this division would be impossible.
:::

## Divisibility

With integers, "\( 3 \) divides \( 12 \)" means that \( 12 \) is an integer multiple of \( 3 \) (@def-divisibility-prime), and it is the case "remainder zero" of integer division. Polynomials get the same word. The field is part of the meaning, so we put it in the definition.

*\( g \) divides \( f \) when \( f \) is a polynomial multiple of \( g \), with the multiplier taken over the same field.*

::: {#def-divisibility-polynomials}
[Divisibility, Associates]

Let \( F \) be a field and \( f, g \in F[x] \).

- We say \( g \) **divides** \( f \) **over \( F \)**, and write \( g \mid f \), if there **exists** \( h \in F[x] \) with \( f = gh \). Then \( g \) is a **divisor** (or **factor**) of \( f \), and \( f \) is a **multiple** of \( g \). We write \( g \nmid f \) if \( g \) does not divide \( f \).
- We say \( f \) and \( g \) are **associates** if \( f = cg \) for some **non-zero** constant \( c \in F \).
:::

In words: \( g \mid f \) asks for a multiplier \( h \) **in \( F[x] \)**, so the same pair can behave differently over different fields. Associates differ only by a non-zero scalar factor. Since \( c^{-1} \) exists, "associates" is symmetric: \( f = cg \) gives \( g = c^{-1} f \).

Examples, simplest first.

- **Degenerate cases.** Every \( g \) divides \( 0 \), since \( 0 = g \cdot 0 \). On the other hand \( 0 \mid f \) only for \( f = 0 \), since \( 0 \cdot h = 0 \). Every non-zero constant \( c \) divides every \( f \), since \( f = c \cdot (c^{-1} f) \). These cases matter: they say that non-zero constants are invisible to divisibility, just as \( \pm 1 \) are for integers.
- In \( \nQ[x] \), \( x - 1 \mid x^2 - 1 \), since \( x^2 - 1 = (x - 1)(x + 1) \). Also \( 2x - 2 \mid x^2 - 1 \), since \( x^2 - 1 = (2x - 2) \cdot \tfrac12 (x + 1) \). The polynomials \( x - 1 \) and \( 2x - 2 \) are associates.
- In \( \nF_2[x] \), \( x + 1 \mid x^2 + 1 \), since \( (x + 1)^2 = x^2 + 2x + 1 = x^2 + 1 \) there. In \( \nQ[x] \), however, \( x + 1 \nmid x^2 + 1 \), as the next paragraph shows.
- In \( \nC[x] \), \( x - i \mid x^2 + 1 = (x - i)(x + i) \).

For a non-example by minimal change, keep \( x^2 + 1 \) and \( x + 1 \) but move from \( \nF_2 \) to \( \nQ \). Both are still polynomials, and division with remainder still applies. What fails is the clause "there **exists** \( h \in F[x] \)". If \( x^2 + 1 = (x + 1)h \) with \( h \in \nQ[x] \), then evaluating at \( -1 \) (@thm-evaluation-respects-operations) gives \( 2 = 0 \cdot h(-1) = 0 \), which is false in \( \nQ \). Over \( \nF_2 \) the same computation reads \( 0 = 0 \), and there is no contradiction.

::: {.warning}
Divisibility depends on where the multiplier may live. In \( \nQ[x] \), \( 2x + 2 \mid x + 1 \), because \( x + 1 = (2x + 2) \cdot \tfrac12 \). If we insisted on integer coefficients, \( 2x + 2 \) would **not** divide \( x + 1 \): any integer multiple \( (2x + 2)h \) has all coefficients even. Over a field, a non-zero scalar factor never affects divisibility, so it is pointless to ask whether \( x - 1 \) or \( 3x - 3 \) is "the" factor of \( x^2 - 1 \).
:::

Why this definition? Because it makes "divides" the case of remainder zero, which is the link to division we need. The basic rules follow quickly.

::: {#prp-divisibility-properties}
[Rules for Divisibility]

Let \( F \) be a field and \( f, g, h \in F[x] \).

::: {.enumerate options="label=(\alph*)"}
1. If \( f \mid g \) and \( g \mid h \), then \( f \mid h \).
2. If \( h \mid f \) and \( h \mid g \), then \( h \mid af + bg \) **for all** \( a, b \in F[x] \).
3. If \( g \mid f \) and \( f \neq 0 \), then \( \deg g \le \deg f \).
4. \( f \mid g \) and \( g \mid f \) if and only if \( f \) and \( g \) are associates or both are \( 0 \). In particular, if \( f \mid g \), \( g \mid f \), and \( f, g \) are both monic, then \( f = g \).
5. If \( g \neq 0 \), then \( g \mid f \) if and only if the remainder of \( f \) on division by \( g \) is \( 0 \).
:::
:::

::: {.proof}
(a) Write \( g = fu \) and \( h = gv \) with \( u, v \in F[x] \). Then \( h = f(uv) \) by @thm-polynomial-ring-laws, so \( f \mid h \).

(b) Write \( f = hu \) and \( g = hv \). Then \( af + bg = h(au + bv) \) by @thm-polynomial-ring-laws, so \( h \mid af + bg \).

(c) Write \( f = gu \). Since \( f \neq 0 \), both \( g \) and \( u \) are non-zero, so \( \deg u \ge 0 \). By @thm-degree-of-product, \( \deg f = \deg g + \deg u \ge \deg g \).

(d) \( (\Leftarrow) \) If \( f = cg \) with \( c \neq 0 \), then \( g \mid f \) and \( g = c^{-1} f \) gives \( f \mid g \). If \( f = g = 0 \), both divide each other. \( (\Rightarrow) \) Suppose \( g = fu \) and \( f = gv \). If \( f = 0 \), then \( g = 0 \cdot u = 0 \), so both are \( 0 \). If \( f \neq 0 \), then \( f = f(uv) \), so \( f(1 - uv) = 0 \), and @cor-polynomial-no-zero-divisors gives \( uv = 1 \). By @thm-degree-of-product, \( \deg u + \deg v = \deg 1 = 0 \) with both degrees in \( \nN \), so \( u \) and \( v \) are non-zero constants. Hence \( f = vg \) with \( v \neq 0 \), and \( f, g \) are associates. If both are monic, comparing leading coefficients in \( f = vg \) gives \( 1 = v \cdot 1 \), so \( f = g \).

(e) If the remainder is \( 0 \), then \( f = qg \), so \( g \mid f \). Conversely, if \( f = hg \), then \( f = hg + 0 \) with \( \deg 0 = -\infty < \deg g \). This is a division with remainder, so by the uniqueness in @thm-polynomial-division, the remainder of \( f \) on division by \( g \) is \( 0 \). This proves the proposition.
:::

Part (d) is the polynomial form of a move we will use again and again: **to show two monic polynomials are equal, show that each divides the other.** It also gives each non-zero polynomial a canonical representative. If \( f \neq 0 \) has leading coefficient \( a \), then \( a^{-1} f \) is monic and an associate of \( f \), and it is the **only** monic associate: two monic associates divide each other, so they are equal by (d). For example, the monic associate of \( 3x^2 - 6 \) in \( \nQ[x] \) is \( x^2 - 2 \). The greatest common divisor in the next section will be defined as a monic polynomial for exactly this reason.

## The Remainder and Factor Theorems

Division by a polynomial of degree \( 1 \) leaves a remainder of degree less than \( 1 \), that is, a constant. Which constant? Chapter 3 already answered this. The Factor Theorem for a Linear Divisor (@lem-factor-theorem-linear) showed, by an induction that was long division in disguise, that \( p = (x - c)q + p(c) \) for some \( q \). We now read that lemma through @thm-polynomial-division. What is new is that \( q \) and the constant are **unique**, so \( p(c) \) is **the** remainder in the sense of division.

::: {#thm-remainder-theorem}
[Remainder Theorem and Factor Theorem]

Let \( F \) be a field, \( f \in F[x] \) and \( c \in F \).

::: {.enumerate options="label=(\alph*)"}
1. The remainder of \( f \) on division by \( x - c \) is the constant \( f(c) \).
2. \( c \) is a root of \( f \) if and only if \( x - c \mid f \).
:::
:::

::: {.proof}
(a) By @lem-factor-theorem-linear, \( f = (x - c)q + f(c) \) for some \( q \in F[x] \). The constant \( f(c) \) has degree \( 0 \) or \( -\infty \), which is less than \( \deg(x - c) = 1 \). So this is a division with remainder, and by the uniqueness in @thm-polynomial-division, \( f(c) \) is the remainder.

(b) By @prp-divisibility-properties (e), \( x - c \mid f \) if and only if the remainder is \( 0 \), which by (a) means \( f(c) = 0 \). This proves the theorem.
:::

In other words, the Factor Theorem of Chapter 3 is really a statement about division. Division alone would also give it: dividing \( f \) by \( x - c \) leaves a constant remainder \( r \), and evaluating \( f = (x - c)q + r \) at \( c \) gives \( r = f(c) \). Since Chapter 3 already proved the lemma, we cite it rather than prove it again, and we will use the name "Remainder Theorem" for both parts.

::: {#exm-remainder-theorem}
[Remainders Without Dividing]

(a) Find the remainder of \( f = x^5 - 3x^3 + 2x + 7 \) on division by \( x - 2 \) in \( \nQ[x] \). (b) Show that \( x + 1 \nmid x^2 + 1 \) in \( \nQ[x] \), but \( x + 1 \mid x^2 + 1 \) in \( \nF_2[x] \). (c) Find the remainder of \( x^5 \) on division by \( x^2 - x \) in \( \nQ[x] \), again without long division.
:::

::: {.solution}
(a) By @thm-remainder-theorem (a), the remainder is \( f(2) = 32 - 24 + 4 + 7 = 19 \). No long division is needed.

(b) Here \( x + 1 = x - (-1) \). In \( \nQ \), \( (-1)^2 + 1 = 2 \neq 0 \), so \( -1 \) is not a root and \( x + 1 \nmid x^2 + 1 \) by part (b) of the theorem; the remainder is \( 2 \). In \( \nF_2 \), \( -1 = 1 \) and \( 1^2 + 1 = 0 \), so \( x + 1 \mid x^2 + 1 \). Indeed \( x^2 + 1 = (x + 1)^2 \) in \( \nF_2[x] \). The same polynomial symbols, over two fields, give different answers.

(c) The divisor has degree \( 2 \), so by @thm-polynomial-division, \( x^5 = q\,(x^2 - x) + r \) with \( \deg r \le 1 \), say \( r = ax + b \). The divisor \( x^2 - x = x(x - 1) \) vanishes at \( 0 \) and at \( 1 \), so evaluating both sides there (@thm-evaluation-respects-operations) kills the term \( q\,(x^2 - x) \): at \( 0 \), \( 0 = b \); at \( 1 \), \( 1 = a + b \). Hence \( a = 1 \), \( b = 0 \), and the remainder is \( x \). As a check, \( x^5 - x = x(x^4 - 1) = (x^2 - x)(x^3 + x^2 + x + 1) \). The move is: **evaluate at the roots of the divisor**, one equation per root.
:::

The Factor Theorem peels off one root at a time. Doing it for several distinct roots at once strengthens the Root bound of Chapter 3 (@lem-root-bound), which said that a non-zero polynomial of degree at most \( n \) has at most \( n \) distinct roots. The stronger version says **why** there are so few: every root contributes its own linear factor.

::: {#cor-root-bound-general}
[Distinct Roots Give a Product of Linear Factors]

Let \( F \) be a field, \( f \in F[x] \), and let \( c_1, \dots, c_k \in F \) be **distinct** roots of \( f \), with \( k \ge 1 \). Then
\[
(x - c_1)(x - c_2) \cdots (x - c_k) \mid f .
\]
Consequently, if \( f \neq 0 \), then \( k \le \deg f \): a non-zero polynomial of degree \( n \) has at most \( n \) distinct roots in \( F \).
:::

::: {.idea}
Peel off \( x - c_1 \) by the Factor Theorem. What remains, \( h \), must still vanish at \( c_2 \), because \( f(c_2) = (c_2 - c_1)h(c_2) \) and \( c_2 - c_1 \neq 0 \). So peel off \( x - c_2 \) from \( h \), and so on. Distinctness is what makes the factors \( c_k - c_i \) non-zero.
:::

::: {.proof}
We use induction on \( k \). For \( k = 1 \), this is @thm-remainder-theorem (b).

Let \( k \ge 2 \), and assume the statement for \( k - 1 \) distinct roots. By the induction hypothesis, \( f = (x - c_1) \cdots (x - c_{k-1})\,h \) for some \( h \in F[x] \). Evaluating at \( c_k \) with @thm-evaluation-respects-operations,
\[
0 = f(c_k) = (c_k - c_1) \cdots (c_k - c_{k-1})\, h(c_k) .
\]
Since the \( c_i \) are distinct, each \( c_k - c_i \) with \( i < k \) is non-zero, and a product of non-zero elements of a field is non-zero (@thm-field-basic-properties). Hence \( h(c_k) = 0 \), and @thm-remainder-theorem (b) gives \( h = (x - c_k) h_1 \) with \( h_1 \in F[x] \). Therefore \( f = (x - c_1) \cdots (x - c_k)\, h_1 \), which completes the induction.

For the count, suppose \( f \neq 0 \) and write \( f = (x - c_1) \cdots (x - c_k)\, h_1 \) as above. Then \( h_1 \neq 0 \), and by @thm-degree-of-product, \( \deg f = k + \deg h_1 \ge k \). This proves the corollary.
:::

The count is @lem-root-bound again, now as a consequence of a divisibility statement. The divisibility statement is the more useful one. For instance, it tells us at once that a polynomial vanishing at \( 1 \), \( 2 \) and \( 3 \) is a multiple of \( (x - 1)(x - 2)(x - 3) \).

## Polynomials and polynomial functions

Chapter 0 warned that a polynomial is not the function it defines: over \( \nF_2 \), the non-zero polynomial \( x^2 + x \) has the zero function (@exm-polynomial-vs-function-f2). It also promised that over an infinite field the distinction disappears. Chapter 3 kept that promise in a paragraph right after @lem-root-bound. We record the fact here as a theorem, in a slightly sharper form that counts how many values are needed.

::: {#thm-polynomial-function-determines-polynomial}
[Values Determine a Polynomial]

Let \( F \) be a field and \( p, q \in F[x] \).

::: {.enumerate options="label=(\alph*)"}
1. Let \( n \in \nN \) with \( \deg p \le n \) and \( \deg q \le n \). If \( p(c) = q(c) \) for at least \( n + 1 \) **distinct** elements \( c \in F \), then \( p = q \).
2. If \( F \) is **infinite** and \( p(c) = q(c) \) for **every** \( c \in F \), then \( p = q \).
:::
:::

::: {.proof}
(a) Let \( h = p - q \). By @thm-degree-of-sum, \( \deg h \le n \). By @thm-evaluation-respects-operations, \( h(c) = p(c) - q(c) = 0 \) for each of the given \( n + 1 \) distinct elements, so \( h \) has at least \( n + 1 \) distinct roots. By @lem-root-bound, a non-zero polynomial of degree at most \( n \) has at most \( n \) distinct roots, so \( h \) cannot be non-zero. Hence \( h = 0 \) and \( p = q \).

(b) Let \( n = \max(\deg p, \deg q, 0) \in \nN \). Since \( F \) is infinite, it contains \( n + 1 \) distinct elements, and \( p \) and \( q \) agree at each of them. Part (a) gives \( p = q \). This proves the theorem.
:::

So over \( \nQ \), \( \nR \) and \( \nC \), we may compare polynomials by comparing their functions, and we may read off coefficients from values. Part (a) holds over **every** field, including finite ones: a quadratic over \( \nF_5 \) is determined by its values at any three distinct points.

::: {.warning}
Part (b) is false over every finite field. Over \( \nF_p \), the polynomial \( x^p - x \) is non-zero but vanishes at every element (@exr-polynomials-c2). So \( x^p \) and \( x \) define the same function \( \nF_p \to \nF_p \) although they are different polynomials. There is no contradiction with (a): the degrees are at most \( p \), and (a) would need agreement at \( p + 1 \) distinct points, but \( \nF_p \) has only \( p \) elements.
:::

::: {.check}
Over \( \nF_3 \), do the polynomials \( x^3 + 2x \) and \( 0 \) define the same function? Does this contradict @thm-polynomial-function-determines-polynomial?
:::

::: {.solution}
Yes. The values of \( x^3 + 2x \) at \( 0, 1, 2 \) are \( 0 \), \( 1 + 2 = 3 = 0 \), and \( 8 + 4 = 12 = 0 \). So the function is zero, although the polynomial is not. There is no contradiction: \( \nF_3 \) is finite, so part (b) does not apply, and part (a) with \( n = 3 \) would need \( 4 \) distinct points. In fact \( x^3 + 2x = x^3 - x \), the polynomial of the warning with \( p = 3 \).
:::

Division with remainder is the one tool this chapter keeps using. In the next section it shows that every set of polynomials closed under the right operations consists of the multiples of a single polynomial, and that gives greatest common divisors.

## Exercises

### A. Check your understanding

::: {#exr-division-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the theorem on division with remainder in \( F[x] \), including every hypothesis.
2. Determine whether the following statement is true: "for every field \( F \) and all \( f, g \in F[x] \), if \( f \mid g \) and \( g \mid f \), then \( f = g \)." Justify your answer. Does your answer change if \( F = \nF_2 \)?
3. Let \( c \in F \) be non-zero. What are the quotient and the remainder of \( f \) on division by the constant polynomial \( c \)?
4. Name the method for finding the remainder of \( f \) on division by \( x - c \) without dividing.
5. Determine whether the following statement is true: "if \( F \) is a field and \( p \in F[x] \) satisfies \( p(c) = 0 \) for every \( c \in F \), then \( p = 0 \)." Justify your answer.
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Let \( F \) be a field and \( f, g \in F[x] \) with \( g \neq 0 \). Then there are unique \( q, r \in F[x] \) with \( f = qg + r \) and \( \deg r < \deg g \) (@thm-polynomial-division).
2. False in general. In \( \nQ[x] \), take \( f = x \) and \( g = 2x \). Then \( g = 2f \) and \( f = \tfrac12 g \), so each divides the other, but \( f \neq g \). By @prp-divisibility-properties (d), mutual divisibility only gives associates. Over \( \nF_2 \), the statement is **true**: the only non-zero constant in \( \nF_2 \) is \( 1 \), so associates are equal, and if \( f \mid g \) and \( g \mid f \), then either both are \( 0 \) or \( f = 1 \cdot g \).
3. The remainder must have degree less than \( \deg c = 0 \), so \( r = 0 \). Then \( f = qc \), so \( q = c^{-1} f \). In particular every polynomial is divisible by every non-zero constant.
4. The Remainder Theorem (@thm-remainder-theorem): the remainder is the constant \( f(c) \).
5. False. Over \( \nF_2 \), \( p = x^2 + x \) is non-zero but \( p(0) = p(1) = 0 \) (@exm-polynomial-vs-function-f2). The statement is true when \( F \) is infinite, by @thm-polynomial-function-determines-polynomial (b).
:::
:::

### B. Practice

::: {#exr-division-b1}
[B1: Dividing Over Two Fields]

::: {.enumerate options="label=(\alph*)"}
1. In \( \nQ[x] \), divide \( f = x^4 - 3x^3 + 2x - 5 \) by \( g = 3x^2 - 1 \) with remainder.
2. In \( \nF_5[x] \), divide \( f = x^4 + 2x^3 + 3x + 1 \) by \( g = 2x^2 + 3 \) with remainder. Hence decide whether \( g \mid f \) in \( \nF_5[x] \).
:::

*Hint for (b): first find the inverse of \( 2 \) in \( \nF_5 \).*
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. The leading coefficient of \( g \) is \( 3 \), with inverse \( \tfrac13 \). First, \( x^4 / 3x^2 = \tfrac13 x^2 \), and \( f - \tfrac13 x^2 g = -3x^3 + \tfrac13 x^2 + 2x - 5 \). Next, \( -3x^3 / 3x^2 = -x \), and subtracting \( -xg = -3x^3 + x \) leaves \( \tfrac13 x^2 + x - 5 \). Next, \( \tfrac13 x^2 / 3x^2 = \tfrac19 \), and subtracting \( \tfrac19 g = \tfrac13 x^2 - \tfrac19 \) leaves \( x - \tfrac{44}{9} \), of degree \( 1 < 2 \). Hence
\[
x^4 - 3x^3 + 2x - 5 = \bigl( \tfrac13 x^2 - x + \tfrac19 \bigr)(3x^2 - 1) + x - \tfrac{44}{9} ,
\]
with quotient \( \tfrac13 x^2 - x + \tfrac19 \) and remainder \( x - \tfrac{44}{9} \), which are the only ones by @thm-polynomial-division.
2. In \( \nF_5 \), \( 2 \cdot 3 = 6 = 1 \), so \( 2^{-1} = 3 \). First, the leading term \( x^4 \) divided by \( 2x^2 \) is \( 3x^2 \), and \( 3x^2 g = 6x^4 + 9x^2 = x^4 + 4x^2 \). Subtracting leaves \( 2x^3 - 4x^2 + 3x + 1 = 2x^3 + x^2 + 3x + 1 \). Next, \( 2x^3 / 2x^2 = x \), and subtracting \( xg = 2x^3 + 3x \) leaves \( x^2 + 1 \). Next, \( x^2 / 2x^2 = 3 \), and subtracting \( 3g = 6x^2 + 9 = x^2 + 4 \) leaves \( 1 - 4 = -3 = 2 \). Hence
\[
x^4 + 2x^3 + 3x + 1 = (3x^2 + x + 3)(2x^2 + 3) + 2 \quad \text{in } \nF_5[x] .
\]
The remainder \( 2 \) is non-zero, so \( g \nmid f \) in \( \nF_5[x] \), by @prp-divisibility-properties (e).
:::
:::

::: {#exr-division-b2}
[B2: A Factor of \( x^n - c^n \)]

Let \( F \) be a field, \( c \in F \) and \( n \ge 1 \). Prove that \( x - c \mid x^n - c^n \) in \( F[x] \), and verify that the quotient is \( x^{n-1} + c\,x^{n-2} + \dots + c^{n-2} x + c^{n-1} \).
:::

::: {.solution}
The value of \( f = x^n - c^n \) at \( c \) is \( c^n - c^n = 0 \), so \( c \) is a root of \( f \), and @thm-remainder-theorem (b) gives \( x - c \mid f \). For the quotient, let \( s = \sum_{j=0}^{n-1} c^{j} x^{n-1-j} \). Then
\[
(x - c)s = \sum_{j=0}^{n-1} c^{j} x^{n-j} - \sum_{j=0}^{n-1} c^{j+1} x^{n-1-j} = \sum_{j=0}^{n-1} c^{j} x^{n-j} - \sum_{j=1}^{n} c^{j} x^{n-j} = x^n - c^n ,
\]
since the two sums share the terms with \( 1 \le j \le n - 1 \), leaving \( c^0 x^n \) from the first and \( c^n x^0 \) from the second. This shows \( x^n - c^n = (x - c)s \).
:::

::: {#exr-division-b3}
[B3: A Remainder Without Long Division]

::: {.enumerate options="label=(\alph*)"}
1. In \( \nQ[x] \), find the remainder of \( x^{100} \) on division by \( x^2 - 1 \) without long division.
2. Show that the answer to (a) is the remainder of \( x^{100} \) on division by \( x^2 - 1 \) over **every** field \( F \), including \( \nF_2 \). Explain why the method of (a) alone does not settle the case \( F = \nF_2 \).
:::

*Hint for (a): part (c) of @exm-remainder-theorem. Hint for (b): imitate the identity of B2.*
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. By @thm-polynomial-division, \( x^{100} = q(x^2 - 1) + r \) with \( \deg r \le 1 \), say \( r = ax + b \). Evaluating at \( 1 \) and \( -1 \), where \( x^2 - 1 \) vanishes (@thm-evaluation-respects-operations), gives \( 1 = a + b \) and \( 1 = (-1)^{100} = -a + b \). Adding and subtracting, \( 2b = 2 \) and \( 2a = 0 \), so \( b = 1 \) and \( a = 0 \). The remainder is \( 1 \).
2. Over any field, let \( s = \sum_{j=0}^{49} x^{2j} \). Then
\[
(x^2 - 1)s = \sum_{j=0}^{49} x^{2j+2} - \sum_{j=0}^{49} x^{2j} = x^{100} - 1 ,
\]
because the terms \( x^2, x^4, \dots, x^{98} \) occur in both sums. Hence \( x^{100} = s \cdot (x^2 - 1) + 1 \), and \( \deg 1 = 0 < 2 \), so by the uniqueness in @thm-polynomial-division the remainder is \( 1 \) over every field. The method of (a) divides by \( 2 \), and over \( \nF_2 \) we have \( 2 = 0 \); also \( 1 = -1 \) there, so evaluating at \( \pm 1 \) gives only the single equation \( a + b = 1 \), which does not determine \( a \) and \( b \).
:::
:::

### C. Going deeper

::: {#exr-division-c1}
[C1: Division by a Monic Polynomial Over \( \nZ \)]

As in the warning after @thm-polynomial-division, \( \nZ[x] \) denotes the set of polynomials in \( \nQ[x] \) all of whose coefficients are integers. It is closed under addition and multiplication.

::: {.enumerate options="label=(\alph*)"}
1. Let \( f, g \in \nZ[x] \) with \( g \) **monic**. Prove that there exist \( q, r \in \nZ[x] \) with \( f = qg + r \) and \( \deg r < \deg g \).
2. Prove that \( q \) and \( r \) in (a) are unique, even among \( q, r \in \nQ[x] \).
3. Does (a) remain true if the leading coefficient of \( g \) is \( -1 \) instead of \( 1 \)? Justify your answer.
:::

*Hint for (a): find the one step in the proof of @thm-polynomial-division that leaves \( \nZ[x] \).*
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. We repeat the existence proof of @thm-polynomial-division, checking that every polynomial stays in \( \nZ[x] \). Let \( m = \deg g \). The only step that could leave \( \nZ[x] \) is forming \( a b^{-1} x^{n-m} g \), where \( b \) is the leading coefficient of \( g \). Here \( b = 1 \), so \( a b^{-1} = a \in \nZ \) and \( f_1 = f - a x^{n-m} g \in \nZ[x] \). The strong induction on \( \deg f \) (@thm-strong-induction) then runs word for word inside \( \nZ[x] \): in Case 1, \( q = 0 \) and \( r = f \) are in \( \nZ[x] \); in Case 2, \( q = a x^{n-m} + q_1 \) and \( r = r_1 \) are in \( \nZ[x] \) because \( q_1, r_1 \) are, by the induction hypothesis applied to \( f_1 \in \nZ[x] \). This proves existence in \( \nZ[x] \).
2. Suppose \( f = qg + r = q'g + r' \) with \( q, q', r, r' \in \nQ[x] \) and \( \deg r, \deg r' < \deg g \). Since \( \nQ \) is a field and \( g \neq 0 \), the uniqueness part of @thm-polynomial-division in \( \nQ[x] \) gives \( q = q' \) and \( r = r' \). In particular the pair found in (a) is the unique one.
3. Yes. If the leading coefficient is \( b = -1 \), then \( b^{-1} = -1 \in \nZ \), so \( a b^{-1} = -a \in \nZ \), and the argument of (a) goes through unchanged. What matters is that the leading coefficient has an inverse **in \( \nZ \)**, which is true exactly for \( \pm 1 \).
:::
:::

::: {#exr-division-c2}
[C2: Remainders on Division by a Quadratic]

Let \( F \) be a field, \( f \in F[x] \) and \( a, b \in F \).

::: {.enumerate options="label=(\alph*)"}
1. Suppose \( a \neq b \). Prove that the remainder of \( f \) on division by \( (x - a)(x - b) \) is
\[
r = f(a)\,\frac{x - b}{a - b} + f(b)\,\frac{x - a}{b - a} ,
\]
where \( \frac{x - b}{a - b} \) means \( (a - b)^{-1}(x - b) \).
2. Now let \( a = b \). Write \( f = (x - a)h + f(a) \) by @thm-remainder-theorem. Prove that the remainder of \( f \) on division by \( (x - a)^2 \) is \( h(a)(x - a) + f(a) \).
3. Hence find the remainder of \( x^{100} \) on division by \( x^2 - 3x + 2 \) in \( \nQ[x] \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Since \( a \neq b \), \( a - b \) is invertible, so \( r \) is a well-defined polynomial of degree at most \( 1 \). By @thm-polynomial-division, \( f = q(x - a)(x - b) + s \) with \( \deg s \le 1 \). Evaluating at \( a \) and at \( b \) (@thm-evaluation-respects-operations) gives \( s(a) = f(a) \) and \( s(b) = f(b) \). Also \( r(a) = f(a) \cdot 1 + f(b) \cdot 0 = f(a) \) and \( r(b) = f(b) \). So \( s \) and \( r \) have degree at most \( 1 \) and agree at the \( 2 \) distinct points \( a, b \). By @thm-polynomial-function-determines-polynomial (a) with \( n = 1 \), \( s = r \). This proves the formula.
2. By @thm-remainder-theorem (a) applied to \( h \), \( h = (x - a)k + h(a) \) for some \( k \in F[x] \). Substituting,
\[
f = (x - a)\bigl( (x - a)k + h(a) \bigr) + f(a) = k\,(x - a)^2 + \bigl( h(a)(x - a) + f(a) \bigr) .
\]
The last bracket has degree at most \( 1 < 2 = \deg (x - a)^2 \), so by the uniqueness in @thm-polynomial-division it is the remainder.
3. Here \( x^2 - 3x + 2 = (x - 1)(x - 2) \), with \( a = 1 \neq b = 2 \), \( f(1) = 1 \) and \( f(2) = 2^{100} \). By (a),
\[
r = 1 \cdot \frac{x - 2}{1 - 2} + 2^{100} \cdot \frac{x - 1}{2 - 1} = (2^{100} - 1)x + (2 - 2^{100}) .
\]
As a check, \( r(1) = 1 \) and \( r(2) = 2^{101} - 2 + 2 - 2^{100} = 2^{100} \).
:::
:::

::: {#exr-division-c3}
[C3: Equal Functions Over \( \nF_p \)]

Let \( p \) be a prime and \( f, g \in \nF_p[x] \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( f(c) = g(c) \) for every \( c \in \nF_p \) if and only if \( x^p - x \mid f - g \) in \( \nF_p[x] \).
2. Deduce that \( f \) and its remainder on division by \( x^p - x \) define the same function \( \nF_p \to \nF_p \). Use this to find a polynomial of degree less than \( 5 \) that defines the same function on \( \nF_5 \) as \( x^7 + x \).
:::

*Hint for (a): @exr-polynomials-c2 and @cor-root-bound-general.*
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. \( (\Leftarrow) \) Suppose \( f - g = (x^p - x)h \). By @exr-polynomials-c2, \( c^p - c = 0 \) for every \( c \in \nF_p \). By @thm-evaluation-respects-operations, \( f(c) - g(c) = (c^p - c)h(c) = 0 \) for every \( c \). \( (\Rightarrow) \) Suppose \( f(c) = g(c) \) for every \( c \in \nF_p \). Then the \( p \) distinct elements \( 0, 1, \dots, p - 1 \) of \( \nF_p \) are roots of \( f - g \). Let \( P = \prod_{c \in \nF_p} (x - c) \). By @cor-root-bound-general, \( P \mid f - g \). It remains to show \( P = x^p - x \). By @exr-polynomials-c2, every \( c \in \nF_p \) is a root of \( x^p - x \), so @cor-root-bound-general gives \( x^p - x = Pu \) for some \( u \). Both \( P \) and \( x^p - x \) are monic of degree \( p \) (@thm-degree-of-product), so \( \deg u = 0 \), and comparing leading coefficients gives \( u = 1 \). Hence \( P = x^p - x \), and \( x^p - x \mid f - g \).
2. Write \( f = q(x^p - x) + r \) by @thm-polynomial-division. Then \( x^p - x \mid f - r \), so \( f \) and \( r \) define the same function by (a). For \( f = x^7 + x \) over \( \nF_5 \): \( x^7 = x^2 \cdot x^5 = x^2(x^5 - x) + x^3 \), so \( x^7 + x = x^2(x^5 - x) + (x^3 + x) \) with \( \deg(x^3 + x) = 3 < 5 \). Hence \( x^3 + x \) defines the same function as \( x^7 + x \) on \( \nF_5 \).
:::
:::
