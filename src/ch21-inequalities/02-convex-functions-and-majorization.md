# Convex Functions of a Majorization

Section 1 turned the \( n \) inequalities of a majorization into a single identity, \( \x = \D\y \) with \( \D \) doubly stochastic. This section spends it. Chapter 17 §07 left to this chapter "the general consequences of a majorization \( \x \prec \y \), namely \( \sum_i\phi(x_i) \le \sum_i\phi(y_i) \) for every convex \( \phi \colon \nR \to \nR \), …"; that is the first theorem below, and its converse says that the convex functions see nothing but the majorization. Two more promises are paid from it: Chapter 17 §08's claim that for non-negative vectors "\( \x \prec \y \) implies \( x_1\cdots x_n \ge y_1\cdots y_n \)", and Chapters 18 §10 and §11's claim that "\( \A \mapsto \tr f(\A) = \sum_i f(\lambda_i(\A)) \) is convex on the Hermitian matrices with spectrum in that interval" for every convex \( f \).

**Conventions.** Vectors are real and \( \prec \), \( \prec_w \) are @def-majorization. A **convex** function is one in the sense of @def-convex-function, and an interval of \( \nR \) is a convex subset of \( \nR \), since it contains every number lying between two of its points. In the last subsection \( F = \nR \) or \( \nC \), matrices in \( M_n(F) \) written \( \A, \B, \C \) are **Hermitian**, and \( f(\A) \) is the spectral functional calculus of Chapter 12 §08, @def-function-of-normal-operator. There \( \P_j \), with an integer subscript, is an orthogonal projection of a spectral resolution; \( \P_\sigma \) always means a permutation matrix. No analysis is imported here: the only facts used from outside linear algebra reach us through Chapter 18's already proved results.

## Karamata's inequality

A majorization is a statement about sums of the largest entries. A convex function is one whose graph lies below its chords. The link between them is that an averaging matrix turns one into the other, and §01 says that a majorization *is* an averaging matrix.

::: {#thm-karamata}
[Karamata's Inequality]

Let \( I \subseteq \nR \) be an interval, let \( \phi \colon I \to \nR \) be **convex**, and let \( \x, \y \in \nR^n \) satisfy \( \x \prec \y \), with every entry of \( \y \) lying in \( I \). Then every entry of \( \x \) lies in \( I \), and
\[
\sum_{i=1}^{n}\phi(x_i) \ \le\ \sum_{i=1}^{n}\phi(y_i) .
\]
:::

::: {.idea}
Write \( \x = \D\y \) with \( \D \) doubly stochastic. Each \( x_i \) is then a weighted average of the \( y_j \), with the weights in row \( i \) of \( \D \); Jensen's inequality bounds \( \phi(x_i) \) by the same average of the \( \phi(y_j) \). Add these \( n \) inequalities. The coefficient of \( \phi(y_j) \) on the right is the sum of column \( j \) of \( \D \), which is \( 1 \). The rows and the columns do two different jobs, and this is where "doubly" earns its keep.
:::

::: {.proof}
By @thm-hardy-littlewood-polya there is a doubly stochastic \( \D = (d_{ij}) \) with \( \x = \D\y \), that is,
\[
x_i = \sum_{j=1}^{n} d_{ij}y_j \qquad (i = 1, \dots, n) .
\]
Fix \( i \). The numbers \( d_{i1}, \dots, d_{in} \) are non-negative and add up to \( 1 \), since row \( i \) of \( \D \) is a row of a doubly stochastic matrix (@def-doubly-stochastic). So \( x_i \) is a convex combination of \( y_1, \dots, y_n \), all of which lie in the convex set \( I \); by @lem-convex-contains-combinations, \( x_i \in I \). Now @thm-jensen, applied to the convex \( \phi \) on \( I \) with the points \( y_1, \dots, y_n \) and the weights \( d_{i1}, \dots, d_{in} \), gives
\[
\phi(x_i) = \phi\Bigl(\sum_j d_{ij}y_j\Bigr) \ \le\ \sum_{j=1}^{n} d_{ij}\,\phi(y_j) .
\]
Summing over \( i \) and exchanging the order of the two finite sums,
\[
\sum_{i=1}^{n}\phi(x_i) \ \le\ \sum_{j=1}^{n}\Bigl(\sum_{i=1}^{n}d_{ij}\Bigr)\phi(y_j) = \sum_{j=1}^{n}\phi(y_j) ,
\]
because every column of \( \D \) adds up to \( 1 \). This proves the theorem.
:::

The proof is three lines and uses @thm-hardy-littlewood-polya once. That is what §01 was for: without it we would be comparing sorted partial sums with the values of an arbitrary convex function, and there is no route from one to the other.

::: {#exm-karamata-numbers}
[One majorization, four inequalities]

Let \( \y = (5, 3, 1, 1) \) and \( \x = (3, 3, 2, 2) \). Check that \( \x \prec \y \), and write down what @thm-karamata gives for \( \phi(t) = t^2 \), for \( \phi(t) = \lvert t - 2\rvert \), and for \( \phi(t) = \max\{t - 2, 0\} \).
:::

::: {.solution}
Both vectors are decreasing with total \( 10 \), and the running totals are \( 3, 6, 8 \) for \( \x \) against \( 5, 8, 9 \) for \( \y \). So (M1) and (M2) hold, and \( \x \prec \y \).

All three functions are convex on \( I = \nR \): \( t^2 \) by @lem-convex-one-variable, since its derivative \( 2t \) is increasing, and the other two as pointwise maxima of affine functions, by @prp-sup-of-affine-convex (\( \lvert t - 2\rvert = \max\{t-2,\ 2-t\} \)). So:
\[
\begin{aligned}
\textstyle\sum_i x_i^2 &= 9 + 9 + 4 + 4 = 26 \ \le\ 25 + 9 + 1 + 1 = 36 = \textstyle\sum_i y_i^2 , \\
\textstyle\sum_i\lvert x_i - 2\rvert &= 1 + 1 + 0 + 0 = 2 \ \le\ 3 + 1 + 1 + 1 = 6 , \\
\textstyle\sum_i\max\{x_i - 2, 0\} &= 1 + 1 = 2 \ \le\ 3 + 1 = 4 .
\end{aligned}
\]
Each is an instance of the one theorem. The last one measures how much of each vector sits above the level \( 2 \), and it is the test function the converse below is built from.
:::

::: {.check}
Does @thm-karamata apply to \( \phi(t) = t^3 \) on \( I = \nR \)? Test it on \( \x = (0,0,0) \prec \y = (1, 1, -2) \).
:::

::: {.solution}
No. On \( \nR \) the function \( t^3 \) is not convex: at \( a = -2 \), \( b = 0 \) and \( t = \tfrac12 \) the midpoint value is \( \phi(-1) = -1 \), while the chord gives \( \tfrac12\phi(-2) + \tfrac12\phi(0) = -4 \), and \( -1 > -4 \). The conclusion of the theorem does fail here. Both vectors have total \( 0 \), and the running totals \( 0, 0 \) of \( \x \) are at most \( 1, 2 \), so \( \x \prec \y \). But \( \sum_i x_i^3 = 0 \) while \( \sum_i y_i^3 = 1 + 1 - 8 = -6 \), and \( 0 > -6 \). On \( I = (0, \infty) \), where \( t^3 \) **is** convex, since its derivative \( 3t^2 \) is increasing there (@lem-convex-one-variable), the theorem does apply, and no such failure is possible for vectors with strictly positive entries.
:::

## The converse, and the weak version

Karamata's inequality is not merely a consequence of majorization; it is equivalent to it. Two families of test functions do the work: the affine ones pin down the totals, and the "hockey sticks" \( t \mapsto \max\{t - c, 0\} \) pin down the partial sums.

::: {#prp-majorization-from-convex}
[Convex Functions Detect Majorization]

Let \( \x, \y \in \nR^n \). If
\[
\sum_{i=1}^{n}\phi(x_i) \ \le\ \sum_{i=1}^{n}\phi(y_i)
\]
for **every** convex \( \phi \colon \nR \to \nR \), then \( \x \prec \y \).
:::

::: {.idea}
Use \( \phi(t) = t \) and \( \phi(t) = -t \) to get the equal totals. For the \( k \)-th partial sum, use the function that is \( 0 \) below a level \( c \) and rises with slope \( 1 \) above it. Summed over a vector it always exceeds "top \( k \) sum minus \( kc \)", and it *equals* that when \( c \) is the \( k \)-th largest entry. Setting \( c = y^{\downarrow}_k \) makes the right-hand side exact and the left-hand side an over-estimate, which is the direction we need.
:::

::: {.proof}
Both \( \phi(t) = t \) and \( \phi(t) = -t \) are affine, hence convex by @exm-first-convex-functions (a). They give \( \sum_i x_i \le \sum_i y_i \) and \( -\sum_i x_i \le -\sum_i y_i \), so the totals are equal. This is (M2).

Fix \( k \) with \( 1 \le k \le n - 1 \), put \( c = y^{\downarrow}_k \), and let
\[
\phi_c(t) = \max\{t - c,\ 0\} ,
\]
the pointwise maximum of the two affine functions \( t \mapsto t - c \) and \( t \mapsto 0 \), hence convex by @prp-sup-of-affine-convex. For any \( \z \in \nR^n \) the sum \( \sum_i\phi_c(z_i) \) does not depend on the order of the entries, so it equals \( \sum_i\phi_c(z^{\downarrow}_i) \). Every term is \( \ge 0 \), and each of the first \( k \) terms satisfies \( \phi_c(z^{\downarrow}_i) \ge z^{\downarrow}_i - c \). Hence
\[
\sum_{i=1}^{n}\phi_c(z_i) \ \ge\ \sum_{i=1}^{k}z^{\downarrow}_i - kc .
\tag{$\ast$}
\]
For \( \z = \y \) and this particular \( c \), \( (\ast) \) is an equality: for \( i \le k \) we have \( y^{\downarrow}_i \ge y^{\downarrow}_k = c \), so \( \phi_c(y^{\downarrow}_i) = y^{\downarrow}_i - c \); and for \( i > k \) we have \( y^{\downarrow}_i \le c \), so \( \phi_c(y^{\downarrow}_i) = 0 \). Therefore
\[
\sum_{i=1}^{k}x^{\downarrow}_i - kc \ \overset{(\ast)}{\le}\ \sum_{i=1}^{n}\phi_c(x_i) \ \le\ \sum_{i=1}^{n}\phi_c(y_i) = \sum_{i=1}^{k}y^{\downarrow}_i - kc ,
\]
the middle step being the hypothesis applied to \( \phi_c \). Canceling \( kc \) gives (M1) at \( k \). As \( k \) was arbitrary, \( \x \prec \y \).
:::

Together with @thm-karamata this is an equivalence: \( \x \prec \y \) **if and only if** \( \sum_i\phi(x_i) \le \sum_i\phi(y_i) \) for every convex \( \phi \colon \nR \to \nR \). So majorization is exactly the order that all convex functions agree on. The proof also shows how few test functions are needed: the two affine ones and the \( n - 1 \) hockey sticks at the levels \( y^{\downarrow}_1, \dots, y^{\downarrow}_{n-1} \).

Weak majorization has a matching statement, with the class of test functions cut down.

::: {#prp-weak-karamata}
[Karamata for Weak Majorization]

Let \( \x, \y \in \nR^n \) with \( \x \prec_w \y \), and let \( \phi \colon \nR \to \nR \) be convex and **increasing**. Then
\[
\sum_{i=1}^{n}\phi(x_i) \ \le\ \sum_{i=1}^{n}\phi(y_i) .
\]
:::

::: {.idea}
The only thing wrong with \( \y \) is that its total may be too big. Take the excess away from the **smallest** entry of \( \y \). That keeps the vector sorted, leaves all the partial sums before the last one untouched, and produces a genuine majorization, to which @thm-karamata applies. Lowering an entry can only lower \( \phi \), which is where "increasing" is used.
:::

::: {.proof}
Let \( s = \sum_i y_i - \sum_i x_i \). Taking \( k = n \) in (M1) for \( \x \prec_w \y \) gives \( s \ge 0 \). Define \( \w \in \nR^n \) by
\[
w_i = y^{\downarrow}_i \ \ (i \le n-1) , \qquad w_n = y^{\downarrow}_n - s .
\]
Only the last entry has changed, and it has been lowered, so \( \w \) is still decreasing and \( \w^{\downarrow} = \w \). Its total is \( \sum_i y_i - s = \sum_i x_i \), which is (M2) for \( \x \prec \w \). For \( k \le n - 1 \), \( \sum_{i\le k}w_i = \sum_{i \le k}y^{\downarrow}_i \ge \sum_{i\le k}x^{\downarrow}_i \) by (M1) for \( \x \prec_w \y \). So \( \x \prec \w \).

By @thm-karamata with \( I = \nR \), \( \sum_i\phi(x_i) \le \sum_i\phi(w_i) \). Since \( w_i \le y^{\downarrow}_i \) for every \( i \) and \( \phi \) is increasing, \( \phi(w_i) \le \phi(y^{\downarrow}_i) \), so
\[
\sum_{i}\phi(w_i) \ \le\ \sum_i \phi(y^{\downarrow}_i) = \sum_i\phi(y_i) .
\]
Chaining the two inequalities proves the proposition.
:::

::: {.warning}
**"Increasing" cannot be dropped from @prp-weak-karamata.** Take \( \x = (0,0) \) and \( \y = (1, 0) \). The running totals \( 0, 0 \) of \( \x \) are at most \( 1, 1 \), so \( \x \prec_w \y \). The function \( \phi(t) = -t \) is convex but decreasing, and \( \sum_i\phi(x_i) = 0 \) while \( \sum_i\phi(y_i) = -1 \). A weak majorization allows \( \y \) to carry more total than \( \x \), and a decreasing \( \phi \) punishes exactly that.
:::

## Schur-convex functions

@thm-karamata is a statement about one particular shape of function, \( \x \mapsto \sum_i\phi(x_i) \). The property it establishes deserves a name of its own, because many functions have it that are not of that shape.

*A function is Schur-convex when spreading a vector out can only increase it.*

The domain needs a moment's thought. If \( G \) is to be compared at \( \x \) and \( \y \) whenever \( \x \prec \y \), then the domain must contain \( \x \) as soon as it contains \( \y \). Call a set \( A \subseteq \nR^n \) **symmetric** if \( \P_\sigma\x \in A \) for every \( \x \in A \) and every \( \sigma \in S_n \). A symmetric **convex** set has the property we need: if \( \y \in A \) and \( \x \prec \y \), then \( \x \in \conv\{\P_\sigma\y\} \) by @cor-majorization-convex-hull, every \( \P_\sigma\y \) lies in \( A \) by symmetry, and a convex set contains the convex combinations of its points (@lem-convex-contains-combinations), so \( \x \in A \).

::: {#def-schur-convex}
[Schur-Convex Function]

Let \( A \subseteq \nR^n \) be **symmetric and convex**, and let \( G \colon A \to \nR \). Then \( G \) is **Schur-convex** if
\[
\x \prec \y \quad\Longrightarrow\quad G(\x) \le G(\y)
\]
for **all** \( \x, \y \in A \). It is **strictly Schur-convex** if the inequality is **strict** whenever \( \x^{\downarrow} \ne \y^{\downarrow} \).
:::

::: {#def-schur-concave}
[Schur-Concave Function]

With \( A \) as in @def-schur-convex, a function \( G \colon A \to \nR \) is **Schur-concave** if \( -G \) is Schur-convex, that is, if
\[
\x \prec \y \quad\Longrightarrow\quad G(\x) \ge G(\y)
\]
for all \( \x, \y \in A \); and **strictly Schur-concave** if \( -G \) is strictly Schur-convex.
:::

In words: a Schur-convex function is one that respects the majorization order, and a Schur-concave one reverses it. The two standing examples of \( A \) below are \( \nR^n \) itself and the open orthant \( \{\x : x_i > 0 \text{ for every } i\} \), both symmetric and convex.

A Schur-convex function is automatically **symmetric**, meaning \( G(\P_\sigma\x) = G(\x) \) for every permutation. Indeed \( \x \) and \( \P_\sigma\x \) are rearrangements of each other, so each majorizes the other (@prp-majorization-basic (a) and the remark after @def-majorization), and two applications of the definition give \( G(\x) \le G(\P_\sigma\x) \le G(\x) \).

::: {#exm-schur-convex-first}
[Four functions on \( \nR^n \)]

Decide which of the following are Schur-convex, and which are Schur-concave, on \( A = \nR^n \).

::: {.enumerate options="label=(\alph*)"}
1. \( G(\x) = \sum_i x_i^2 \).
2. \( G(\x) = \max_i x_i \).
3. \( G(\x) = \sum_i x_i \).
4. \( G(\x) = \sum_i x_i^3 \), for \( n = 3 \).
:::
:::

::: {.solution}
(a) Schur-convex. \( \phi(t) = t^2 \) is convex on \( \nR \), as in @exm-karamata-numbers, so @thm-karamata gives \( \sum_i x_i^2 \le \sum_i y_i^2 \) whenever \( \x \prec \y \).

(b) Schur-convex. \( \max_i x_i = x^{\downarrow}_1 \), and (M1) at \( k = 1 \) says exactly \( x^{\downarrow}_1 \le y^{\downarrow}_1 \). No convexity is needed here; the definition of majorization already contains the statement.

(c) Both Schur-convex and Schur-concave, since (M2) makes it constant on each majorization class. This is the degenerate case, and it shows that the two notions are not exclusive.

(d) Neither, and one pair of comparisons settles both. The flat vector is majorized by every vector with the same total (@exm-majorization-first-examples (b)), so
\[
(0,0,0) \prec (2,-1,-1) , \qquad (0,0,0) \prec (1,1,-2) ,
\]
both totals being \( 0 \). Now \( G(0,0,0) = 0 \), while \( G(2,-1,-1) = 8 - 1 - 1 = 6 \) and \( G(1,1,-2) = 1 + 1 - 8 = -6 \). Schur-convexity applied to the second majorization would demand \( 0 \le -6 \), and Schur-concavity applied to the first would demand \( 0 \ge 6 \). Both fail.
:::

Part (d) is the non-example by minimal change. The function \( \sum_i\phi(x_i) \) with \( \phi(t) = t^3 \) differs from the Schur-convex \( \sum_i\phi(x_i) \) with \( \phi(t) = t^2 \) only in the exponent, and \( t^3 \) fails the one clause that matters, convexity on the interval where the entries live.

The next theorem explains why so many natural functions turn out Schur-convex: convexity plus symmetry is enough, and there is no need to be of the form \( \sum_i\phi(x_i) \).

::: {#thm-symmetric-convex-is-schur-convex}
[A Symmetric Convex Function Is Schur-Convex]

Let \( A \subseteq \nR^n \) be symmetric and convex, and let \( G \colon A \to \nR \) be **convex** and **symmetric**, that is, \( G(\P_\sigma\x) = G(\x) \) for every \( \x \in A \) and every \( \sigma \in S_n \). Then \( G \) is Schur-convex.
:::

::: {.idea}
\( \x \prec \y \) puts \( \x \) inside the permutation polytope of \( \y \), whose corners all carry the **same** value of \( G \), by symmetry. A convex function on a convex combination is at most the corresponding combination of its values, and an average of copies of one number is that number.
:::

::: {.proof}
Let \( \x, \y \in A \) with \( \x \prec \y \). By @cor-majorization-convex-hull and @thm-convex-hull-combinations,
\[
\x = \sum_{i=1}^{m} t_i\,\P_{\sigma_i}\y
\]
for some \( \sigma_1, \dots, \sigma_m \in S_n \) and weights \( t_i \ge 0 \) with \( \sum_i t_i = 1 \). Each \( \P_{\sigma_i}\y \) lies in \( A \), since \( A \) is symmetric. By @thm-jensen applied to the convex \( G \) on \( A \),
\[
G(\x) \ \le\ \sum_{i=1}^{m}t_i\,G(\P_{\sigma_i}\y) = \sum_{i=1}^{m}t_i\,G(\y) = G(\y) ,
\]
the middle equality being the symmetry of \( G \) and the last one \( \sum_i t_i = 1 \). This shows that \( G \) is Schur-convex.
:::

Now the promise from Chapter 17 §08. There the second proof of Hadamard's inequality used only the trace, and a remark recorded that a proof "by majorization in earnest" would need the fact that "for vectors with non-negative entries, \( \x \prec \y \) implies \( x_1\cdots x_n \ge y_1\cdots y_n \) (the product is **Schur-concave**)". Here it is.

::: {#cor-product-schur-concave}
[The Product Is Schur-Concave]

Let \( \y \in \nR^n \) have **non-negative** entries and let \( \x \prec \y \). Then every entry of \( \x \) is non-negative, and
\[
x_1x_2\cdots x_n \ \ge\ y_1y_2\cdots y_n .
\]
:::

::: {.idea}
Take \( -\log \), which is convex, and apply @thm-karamata: the product becomes a sum and the inequality flips. The logarithm needs positive entries, so the case of a zero entry is dealt with first — and it is the easy case, because a zero entry makes the right-hand side \( 0 \) while the left-hand side is a product of non-negative numbers.
:::

::: {.proof}
First, every entry of \( \x \) is non-negative. For \( n = 1 \), (M2) gives \( \x = \y \). For \( n \ge 2 \), subtracting (M1) at \( k = n - 1 \) from (M2) gives
\[
x^{\downarrow}_n \ \ge\ y^{\downarrow}_n \ \ge\ 0 ,
\]
and \( x^{\downarrow}_n \) is the smallest entry of \( \x \).

*Case 1: some \( y_i = 0 \).* Then \( y_1\cdots y_n = 0 \), while \( x_1\cdots x_n \ge 0 \) as a product of non-negative numbers. The inequality holds.

*Case 2: every \( y_i > 0 \).* Then \( y^{\downarrow}_n > 0 \), so \( x^{\downarrow}_n > 0 \) by the display above, and every entry of both vectors lies in \( I = (0, \infty) \). By @lem-exp-log (c) the function \( \log \) is concave on \( I \), so \( \phi = -\log \) is convex there. By @thm-karamata,
\[
\sum_{i=1}^{n}\bigl(-\log x_i\bigr) \ \le\ \sum_{i=1}^{n}\bigl(-\log y_i\bigr) ,
\qquad\text{that is,}\qquad
\sum_{i=1}^{n}\log y_i \ \le\ \sum_{i=1}^{n}\log x_i .
\]
By \( \log(ab) = \log a + \log b \) (@lem-exp-log (c)) and induction on \( n \), \( \sum_i\log x_i = \log(x_1\cdots x_n) \) and likewise for \( \y \). So \( \log(y_1\cdots y_n) \le \log(x_1\cdots x_n) \). Since \( \log \) is strictly increasing on \( I \) (@lem-exp-log (c)), two positive numbers with \( \log u \le \log v \) satisfy \( u \le v \); otherwise \( u > v \) would give \( \log u > \log v \). Hence \( y_1\cdots y_n \le x_1\cdots x_n \). This proves the corollary.
:::

So the flat vector, the bottom of the majorization order, has the largest product among non-negative vectors with a fixed total — which is @lem-am-gm again, now as a special case rather than a separate induction.

::: {.warning}
**Schur-convex does not mean convex.** By @cor-product-schur-concave the function \( G(\x) = -x_1x_2 \) is Schur-convex on the symmetric convex set \( A = \{\x \in \nR^2 : x_1, x_2 \ge 0\} \). It is not convex: at \( \x = (1,1) \), \( \y = (2,2) \) and \( t = \tfrac12 \),
\[
G\bigl(\tfrac32, \tfrac32\bigr) = -\tfrac94 = -2.25 ,
\qquad
\tfrac12G(1,1) + \tfrac12G(2,2) = \tfrac12(-1) + \tfrac12(-4) = -2.5 ,
\]
and \( -2.25 > -2.5 \). @thm-symmetric-convex-is-schur-convex is a one-way street.
:::

::: {.check}
Is the function \( G(\x) = x^{\downarrow}_1 + x^{\downarrow}_2 \) on \( \nR^3 \) Schur-convex? Is it convex?
:::

::: {.solution}
Schur-convex: the inequality \( x^{\downarrow}_1 + x^{\downarrow}_2 \le y^{\downarrow}_1 + y^{\downarrow}_2 \) is (M1) at \( k = 2 \). Convex: yes, and this gives a second proof. The two largest entries have the largest sum among all pairs, so \( G(\x) = \max_{i < j}(x_i + x_j) \), a maximum of three linear functions, convex by @prp-sup-of-affine-convex. It is also symmetric, so @thm-symmetric-convex-is-schur-convex applies. (This \( G \) is the Ky Fan sum \( s_2 \) of Chapter 17 §06, read on vectors instead of eigenvalues.)
:::

## Convex functions of a Hermitian matrix

The last payoff is about matrices. For a Hermitian \( \A \) and a convex \( f \) on an interval containing \( \spec(\A) \), the number \( \tr f(\A) \) turns out to be \( \sum_i f(\lambda_i(\A)) \). Chapter 18 §10 stated, and deferred, that this is a convex function of \( \A \). The proof needs two lemmas: a bookkeeping one about traces, and one saying that the quadratic form of \( f(\A) \) dominates \( f \) of the quadratic form of \( \A \).

::: {#lem-trace-of-a-function}
[Reading a Trace on an Orthonormal Basis]

Let \( F = \nR \) or \( \nC \).

::: {.enumerate options="label=(\alph*)"}
1. Let \( (\u_1, \dots, \u_n) \) be an orthonormal basis of \( F^n \) and \( \M \in M_n(F) \). Then \( \tr\M = \sum_{i=1}^{n}\inner{\M\u_i}{\u_i} \).
2. Let \( I \subseteq \nR \), let \( \A \in M_n(F) \) be Hermitian with \( \spec(\A) \subseteq I \), and let \( g \colon I \to \nR \). Then \( g(\A)\u = g(\lambda)\u \) for every eigenvector \( \u \) of \( \A \) with eigenvalue \( \lambda \), and \( \tr g(\A) = \sum_{i=1}^{n}g\bigl(\lambda_i(\A)\bigr) \).
:::
:::

::: {.proof}
(a) Let \( \U \in M_n(F) \) be the matrix whose \( i \)-th column is \( \u_i \). Then \( (\U^{*}\U)_{ij} = \u_i^{*}\u_j = \inner{\u_j}{\u_i} = \delta_{ij} \), so \( \U \) is unitary, and \( (\U^{*}\M\U)_{ii} = \u_i^{*}\M\u_i = \inner{\M\u_i}{\u_i} \). By @thm-trace-properties (3), used with the factors \( \U^{*} \) and \( \M\U \), \( \tr(\U^{*}\M\U) = \tr(\M\U\U^{*}) = \tr\M \). Summing the diagonal of \( \U^{*}\M\U \) gives (a).

(b) Let \( \A = \sum_{j}\mu_j\P_j \) be the spectral resolution of @def-spectral-resolution, with \( \mu_1, \dots, \mu_k \) the distinct eigenvalues; it exists by @thm-spectral-resolution, since a Hermitian matrix has an orthonormal basis of eigenvectors (@cor-spectral-complex-matrix over \( \nC \), @cor-spectral-real-matrix over \( \nR \)). Let \( \A\u = \lambda\u \) with \( \u \ne \0 \). Then \( \lambda = \mu_{j_0} \) for exactly one \( j_0 \), and \( \u \) lies in the eigenspace of \( \mu_{j_0} \), which is the image of \( \P_{j_0} \); so \( \P_{j_0}\u = \u \), and \( \P_j\u = \P_j\P_{j_0}\u = \0 \) for \( j \ne j_0 \) by @thm-spectral-resolution (b). Hence \( g(\A)\u = \sum_jg(\mu_j)\P_j\u = g(\lambda)\u \), by @def-function-of-normal-operator.

Now take an orthonormal basis \( (\u_1, \dots, \u_n) \) of \( F^n \) with \( \A\u_i = \lambda_i(\A)\u_i \), which exists by the spectral theorem just cited. By the previous paragraph, \( \inner{g(\A)\u_i}{\u_i} = g(\lambda_i(\A))\inner{\u_i}{\u_i} = g(\lambda_i(\A)) \), and (a) adds these up to \( \tr g(\A) \).
:::

::: {#lem-peierls}
[Peierls' Inequality]

Let \( I \subseteq \nR \) be an interval, let \( \A \in M_n(F) \) be Hermitian with \( \spec(\A) \subseteq I \), let \( f \colon I \to \nR \) be convex, and let \( \u \in F^n \) with \( \norm{\u} = 1 \). Then \( \inner{\A\u}{\u} \in I \) and
\[
f\bigl(\inner{\A\u}{\u}\bigr) \ \le\ \inner{f(\A)\u}{\u} ,
\]
with **equality** when \( \u \) is an eigenvector of \( \A \).
:::

::: {.idea}
Write \( \A = \sum_j\mu_j\P_j \), its spectral resolution. Then \( \inner{\A\u}{\u} = \sum_j\mu_j\norm{\P_j\u}^2 \) is a weighted average of the eigenvalues, with weights \( \norm{\P_j\u}^2 \) that add up to \( \norm{\u}^2 = 1 \). The same weights appear in \( \inner{f(\A)\u}{\u} = \sum_jf(\mu_j)\norm{\P_j\u}^2 \). So the two sides of the inequality are \( f \) of an average against the average of \( f \), which is Jensen.
:::

::: {.proof}
Let \( \A = \mu_1\P_1 + \dots + \mu_k\P_k \) be the spectral resolution of @def-spectral-resolution, with \( \mu_1, \dots, \mu_k \) the **distinct** eigenvalues of \( \A \), which exists by @thm-spectral-resolution since a Hermitian matrix has an orthonormal basis of eigenvectors (@cor-spectral-complex-matrix over \( \nC \), @cor-spectral-real-matrix over \( \nR \)). Put
\[
w_j = \inner{\P_j\u}{\u} .
\]
By @thm-spectral-resolution (b), \( \P_j = \P_j^2 \) and \( \P_j^{*} = \P_j \), so
\[
w_j = \inner{\P_j\P_j\u}{\u} = \inner{\P_j\u}{\P_j^{*}\u} = \inner{\P_j\u}{\P_j\u} = \norm{\P_j\u}^2 \ \ge\ 0 ,
\]
and by @thm-spectral-resolution (c), \( \sum_jw_j = \inner{\u}{\u} = 1 \). Hence, by @thm-spectral-resolution (d) and @def-function-of-normal-operator,
\[
\inner{\A\u}{\u} = \sum_{j=1}^{k}\mu_jw_j , \qquad
\inner{f(\A)\u}{\u} = \sum_{j=1}^{k}f(\mu_j)w_j .
\]
The first is a convex combination of \( \mu_1, \dots, \mu_k \), all of which lie in the convex set \( I \), so \( \inner{\A\u}{\u} \in I \) by @lem-convex-contains-combinations. Applying @thm-jensen to the convex \( f \) on \( I \), with points \( \mu_j \) and weights \( w_j \),
\[
f\bigl(\inner{\A\u}{\u}\bigr) = f\Bigl(\sum_j w_j\mu_j\Bigr) \ \le\ \sum_j w_jf(\mu_j) = \inner{f(\A)\u}{\u} .
\]

For the equality clause, let \( \A\u = \lambda\u \) with \( \norm{\u} = 1 \). By @lem-trace-of-a-function (b), \( f(\A)\u = f(\lambda)\u \), so the right side is \( f(\lambda)\inner{\u}{\u} = f(\lambda) \); and the left side is \( f(\inner{\lambda\u}{\u}) = f(\lambda) \) as well. This proves the lemma.
:::

::: {.check}
Take \( \A = \begin{psmallmatrix} 2 & 1 \\ 1 & 2\end{psmallmatrix} \), \( f(t) = t^2 \) and \( \u = \e_1 \). Compute both sides of @lem-peierls, and then repeat with \( \u = \tfrac1{\sqrt2}(1,1) \).
:::

::: {.solution}
\( \inner{\A\e_1}{\e_1} = a_{11} = 2 \), so the left side is \( f(2) = 4 \). Here \( f(\A) = \A^2 = \begin{psmallmatrix} 5 & 4 \\ 4 & 5\end{psmallmatrix} \), so the right side is \( (\A^2)_{11} = 5 \). Indeed \( 4 \le 5 \), and the inequality is strict because \( \e_1 \) is not an eigenvector of \( \A \).

For \( \u = \tfrac1{\sqrt2}(1,1) \), an eigenvector with \( \A\u = 3\u \), the left side is \( f(3) = 9 \) and the right side is \( \inner{\A^2\u}{\u} = 9\inner{\u}{\u} = 9 \). Equality, as the lemma says.
:::

::: {#thm-trace-convex}
[The Trace of a Convex Function Is Convex]

Let \( I \subseteq \nR \) be an interval and let \( f \colon I \to \nR \) be **convex**. Let \( \A, \B \in M_n(F) \) be Hermitian with \( \spec(\A) \subseteq I \) and \( \spec(\B) \subseteq I \), and let \( 0 \le \theta \le 1 \). Then \( \C = \theta\A + (1-\theta)\B \) is Hermitian with \( \spec(\C) \subseteq I \), and
\[
\tr f(\C) \ \le\ \theta\,\tr f(\A) + (1-\theta)\,\tr f(\B) .
\]
In words: the Hermitian matrices with spectrum in \( I \) form a **convex** set, and \( \A \mapsto \tr f(\A) \) is a **convex** function on it.
:::

::: {.idea}
Fix an orthonormal eigenbasis of the midpoint matrix \( \C = \theta\A + (1-\theta)\B \). Along each of those \( n \) directions the value of \( f \) at the eigenvalue of \( \C \) is exactly the left side of Peierls' inequality, because an eigenvector gives equality; and the eigenvalue itself splits as \( \theta \) times a quadratic form of \( \A \) plus \( (1-\theta) \) times one of \( \B \). Ordinary convexity of \( f \) handles that split, and Peierls' inequality, now as an inequality, converts the two quadratic forms into quadratic forms of \( f(\A) \) and \( f(\B) \). Summing over the basis turns quadratic forms into traces.
:::

::: {.proof}
**Step 1: the spectrum of \( \C \).** The matrix \( \C = \theta\A + (1-\theta)\B \) is Hermitian, being a real combination of Hermitian matrices. Let \( \mu \) be an eigenvalue of \( \C \), with unit eigenvector \( \x \). Then
\[
\mu = \inner{\C\x}{\x} = \theta\inner{\A\x}{\x} + (1-\theta)\inner{\B\x}{\x} .
\]
By @lem-extreme-eigenvalues-quadratic-form, \( \inner{\A\x}{\x} \) lies in \( [\lambda_n(\A), \lambda_1(\A)] \), an interval whose endpoints are eigenvalues of \( \A \), hence contained in \( I \); likewise \( \inner{\B\x}{\x} \in I \). So \( \mu \) is a convex combination of two points of \( I \) and lies in \( I \). Hence \( \spec(\C) \subseteq I \), and \( f(\C) \) is defined.

**Step 2: the inequality.** Choose an orthonormal basis \( (\u_1, \dots, \u_n) \) of \( F^n \) consisting of eigenvectors of \( \C \), which exists by @cor-spectral-complex-matrix over \( \nC \) and @cor-spectral-real-matrix over \( \nR \). Fix \( i \). By @lem-peierls applied to \( \C \) and the eigenvector \( \u_i \), with equality,
\[
\inner{f(\C)\u_i}{\u_i} = f\bigl(\inner{\C\u_i}{\u_i}\bigr) .
\]
By Step 1, \( \inner{\C\u_i}{\u_i} = \theta\alpha_i + (1-\theta)\beta_i \) with \( \alpha_i = \inner{\A\u_i}{\u_i} \in I \) and \( \beta_i = \inner{\B\u_i}{\u_i} \in I \). So @def-convex-function and then @lem-peierls, now applied to \( \A \) and to \( \B \) with the unit vector \( \u_i \), give
\[
\begin{aligned}
\inner{f(\C)\u_i}{\u_i} = f\bigl(\theta\alpha_i + (1-\theta)\beta_i\bigr)
&\le \theta f(\alpha_i) + (1-\theta)f(\beta_i) \\
&\le \theta\inner{f(\A)\u_i}{\u_i} + (1-\theta)\inner{f(\B)\u_i}{\u_i} ,
\end{aligned}
\]
where the last step uses \( \theta \ge 0 \) and \( 1 - \theta \ge 0 \). Summing over \( i = 1, \dots, n \) and using @lem-trace-of-a-function (a) three times, once for each of \( f(\C) \), \( f(\A) \) and \( f(\B) \),
\[
\tr f(\C) \ \le\ \theta\,\tr f(\A) + (1-\theta)\,\tr f(\B) .
\]
Since \( \A \), \( \B \) and \( \theta \) were arbitrary, this is @def-convex-function for \( \A \mapsto \tr f(\A) \) on the set of Hermitian matrices with spectrum in \( I \), which Step 1 shows is convex. This proves the theorem.
:::

This pays Chapter 18 §10's "it is proved in Chapter 21, and nothing in this chapter uses it", and Chapter 18 §11's closing note that "the convexity of \( \A \mapsto \tr f(\A) \) for convex \( f \), and the consequences of a majorization for every convex function, belong to Chapter 21".

::: {#exm-logdet-convex}
[The logarithm of the determinant]

Let \( f(t) = -\log t \) on \( I = (0, \infty) \), so that the matrices in play are the positive definite Hermitian ones. Identify \( \tr f(\A) \), and check the resulting inequality for
\[
\A = \begin{pmatrix} 1 & 0 \\ 0 & 4\end{pmatrix} , \qquad
\B = \begin{pmatrix} 2 & 1 \\ 1 & 2\end{pmatrix} , \qquad \theta = \tfrac12 .
\]
:::

::: {.solution}
A Hermitian \( \A \) has \( \spec(\A) \subseteq (0, \infty) \) exactly when \( \A \succ 0 \), by @thm-pd-characterizations (b). For such an \( \A \), @lem-trace-of-a-function (b), then \( \log(ab) = \log a + \log b \) (@lem-exp-log (c)) with induction on \( n \), and then @thm-trace-det-eigenvalues give
\[
\tr f(\A) = -\sum_{i}\log\lambda_i(\A) = -\log\prod_i\lambda_i(\A) = -\log\det\A .
\]
By @thm-trace-convex, **\( \A \mapsto -\log\det\A \) is convex on the positive definite matrices**; equivalently, \( \det \) is log-concave there.

For the data given, \( \det\A = 4 \) and \( \det\B = 4 - 1 = 3 \), and
\[
\C = \tfrac12(\A + \B) = \begin{pmatrix} \tfrac32 & \tfrac12 \\[2pt] \tfrac12 & 3\end{pmatrix} ,
\qquad \det\C = \tfrac92 - \tfrac14 = \tfrac{17}{4} .
\]
Both \( \A \) and \( \B \) are positive definite (\( \A \) is diagonal with positive entries; \( \B \) has eigenvalues \( 3 \) and \( 1 \)), so the theorem says \( -\log\tfrac{17}{4} \le -\tfrac12\log 4 - \tfrac12\log 3 \), that is, after multiplying by \( -1 \) and exponentiating,
\[
\det\C = \tfrac{17}{4} = 4.25 \ \ge\ \sqrt{4 \cdot 3} = \sqrt{12} \approx 3.464 ,
\]
which holds, since \( 4.25^2 = 18.0625 \ge 12 \).
:::

::: {.remark}
@thm-trace-convex holds for **every** convex \( f \), which is a very large class. It is nonetheless much weaker than the operator convexity of @def-operator-monotone (b), which asks for \( f(\theta\A + (1-\theta)\B) \preceq \theta f(\A) + (1-\theta)f(\B) \) in the Loewner order, a statement about matrices rather than about one number extracted from them. Taking traces turns the Loewner inequality into the one proved here, since the trace of a positive semidefinite matrix is the sum of its non-negative eigenvalues (@thm-psd-characterizations (b), @thm-trace-det-eigenvalues); so operator convexity implies trace convexity, but the converse fails badly, and a later section of this chapter exhibits convex functions that are not operator convex.
:::

## Exercises

### A. Check your understanding

:::: {#exr-convex-functions-and-majorization-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State Karamata's inequality, with all its hypotheses.
2. Which test functions prove @prp-majorization-from-convex, and which clause of @def-majorization does each one give?
3. Define Schur-convex and Schur-concave.
4. True or false: every Schur-convex function on \( \nR^n \) is convex. Justify your answer.
5. True or false: every convex function on \( \nR^n \) is Schur-convex. Justify your answer.
6. State what @thm-trace-convex says for \( f(t) = t^2 \), and identify the resulting function of \( \A \).
:::
::::

::: {.solution}
(a) If \( I \) is an interval, \( \phi \colon I \to \nR \) is convex, \( \x \prec \y \) in \( \nR^n \), and every entry of \( \y \) lies in \( I \), then every entry of \( \x \) lies in \( I \) and \( \sum_i\phi(x_i) \le \sum_i\phi(y_i) \) (@thm-karamata).

(b) The affine functions \( \phi(t) = t \) and \( \phi(t) = -t \) give the equal totals, (M2). The hockey stick \( \phi_c(t) = \max\{t - c, 0\} \) with \( c = y^{\downarrow}_k \) gives (M1) at \( k \).

(c) For a symmetric convex \( A \subseteq \nR^n \), \( G \colon A \to \nR \) is Schur-convex if \( \x \prec \y \) implies \( G(\x) \le G(\y) \) (@def-schur-convex), and Schur-concave if \( \x \prec \y \) implies \( G(\x) \ge G(\y) \) (@def-schur-concave).

(d) False. \( G(\x) = -x_1x_2 \) on the non-negative quadrant is Schur-convex by @cor-product-schur-concave, but the warning after that corollary shows that \( G(\tfrac32,\tfrac32) = -2.25 \) exceeds the average \( -2.5 \) of \( G(1,1) \) and \( G(2,2) \).

(e) False. A Schur-convex function must be symmetric, as shown after @def-schur-concave, and \( G(\x) = x_1 \) is linear, hence convex, but not symmetric: \( G(1,0) = 1 \ne 0 = G(0,1) \), while \( (1,0) \) and \( (0,1) \) majorize each other. Symmetry is exactly the missing hypothesis of @thm-symmetric-convex-is-schur-convex.

(f) For \( I = \nR \) and \( f(t) = t^2 \), it says that \( \A \mapsto \tr(\A^2) \) is convex on the Hermitian matrices. Since \( \A \) is Hermitian, \( \tr(\A^2) = \tr(\A^{*}\A) = \norm{\A}_F^2 \), the squared Frobenius norm.
:::

### B. Practice

:::: {#exr-convex-functions-and-majorization-b1}
[B1: Four consequences of one majorization]

Let \( \y = (6, 2, 1, 1) \) and \( \x = (4, 3, 2, 1) \).

::: {.enumerate options="label=(\alph*)"}
1. Verify that \( \x \prec \y \).
2. Compute \( \sum_i x_i^2 \) and \( \sum_i y_i^2 \), and \( \sum_i\max\{x_i - 3, 0\} \) and \( \sum_i\max\{y_i - 3, 0\} \). Name the theorem each comparison illustrates.
3. Compute \( \prod_i x_i \) and \( \prod_i y_i \). Hence check @cor-product-schur-concave.
4. Give a convex \( \phi \colon \nR \to \nR \) for which the two sides are **equal**.
:::
::::

::: {.solution}
(a) Both vectors are decreasing with total \( 10 \); the running totals are \( 4, 7, 9 \) for \( \x \) against \( 6, 8, 9 \) for \( \y \). So (M1) and (M2) hold.

(b) \( \sum_i x_i^2 = 16 + 9 + 4 + 1 = 30 \) and \( \sum_i y_i^2 = 36 + 4 + 1 + 1 = 42 \), so \( 30 \le 42 \). Also \( \sum_i\max\{x_i - 3, 0\} = 1 + 0 + 0 + 0 = 1 \) and \( \sum_i\max\{y_i-3,0\} = 3 \), so \( 1 \le 3 \). Both illustrate @thm-karamata, the first with \( \phi(t) = t^2 \) and the second with the hockey stick at level \( 3 \).

(c) \( \prod_i x_i = 4 \cdot 3 \cdot 2 \cdot 1 = 24 \) and \( \prod_i y_i = 6 \cdot 2 \cdot 1 \cdot 1 = 12 \). Indeed \( 24 \ge 12 \), as @cor-product-schur-concave requires for non-negative vectors.

(d) Any affine \( \phi \), for instance \( \phi(t) = t \): both sides are the common total \( 10 \), by (M2). Affine functions are the ones on which majorization gives no information.
:::

:::: {#exr-convex-functions-and-majorization-b2}
[B2: Which are Schur-convex?]

Determine which of the following functions are Schur-convex on the stated symmetric convex set. Justify your answer, naming the theorem used or giving a counterexample.

::: {.enumerate options="label=(\alph*)"}
1. \( G(\x) = \max_i x_i - \min_i x_i \) on \( \nR^n \).
2. \( G(\x) = \sum_i \lvert x_i \rvert \) on \( \nR^n \).
3. \( G(\x) = x_1 + 2x_2 \) on \( \nR^2 \).
4. \( G(\x) = \sum_i\sqrt{x_i} \) on \( A = \{\x \in \nR^n : x_i > 0 \text{ for every } i\} \).
:::
::::

::: {.solution}
(a) Schur-convex. \( G(\x) = x^{\downarrow}_1 - x^{\downarrow}_n \), and \( \x \prec \y \) gives \( x^{\downarrow}_1 \le y^{\downarrow}_1 \) by (M1) at \( k = 1 \) and \( x^{\downarrow}_n \ge y^{\downarrow}_n \) by subtracting (M1) at \( k = n-1 \) from (M2). Subtracting the second from the first gives \( G(\x) \le G(\y) \).

(b) Schur-convex, by @thm-karamata with \( \phi(t) = \lvert t\rvert \), convex as a maximum of two affine functions (@prp-sup-of-affine-convex).

(c) Not Schur-convex. It is not symmetric, and a Schur-convex function must be. Concretely \( (1,0) \) and \( (0,1) \) are rearrangements of each other, so \( (1,0) \prec (0,1) \) and \( (0,1) \prec (1,0) \). Schur-convexity would give \( G(1,0) \le G(0,1) \) from the first and \( G(0,1) \le G(1,0) \) from the second, hence \( G(1,0) = G(0,1) \). But \( G(1,0) = 1 \) and \( G(0,1) = 2 \).

(d) Not Schur-convex; it is Schur-**concave**. First, \( t \mapsto \sqrt t \) is concave on \( (0, \infty) \): for \( a, b > 0 \) and \( 0 \le \theta \le 1 \), @lem-am-gm gives \( 2\sqrt{ab} \le a + b \), so
\[
\begin{aligned}
\bigl(\theta\sqrt a + (1-\theta)\sqrt b\bigr)^2
&= \theta^2a + (1-\theta)^2b + 2\theta(1-\theta)\sqrt{ab} \\
&\le \theta^2a + (1-\theta)^2b + \theta(1-\theta)(a + b) \\
&= \theta a + (1-\theta)b ,
\end{aligned}
\]
using \( \theta^2 + \theta(1-\theta) = \theta \) and \( (1-\theta)^2 + \theta(1-\theta) = 1-\theta \); taking square roots of two non-negative numbers preserves the inequality. So \( \phi(t) = -\sqrt t \) is convex on \( (0,\infty) \), and @thm-karamata turns \( \x \prec \y \) into \( \sum_i(-\sqrt{x_i}) \le \sum_i(-\sqrt{y_i}) \), that is, \( G(\x) \ge G(\y) \). For a concrete instance, \( (2,2) \prec (3,1) \) and \( G(2,2) = 2\sqrt2 \approx 2.83 \), while \( G(3,1) = \sqrt3 + 1 \approx 2.73 \), so \( G \) went **down** as the vector spread out.
:::

:::: {#exr-convex-functions-and-majorization-b3}
[B3: Trace convexity on two-by-two matrices]

::: {.enumerate options="label=(\alph*)"}
1. Let \( f(t) = t^2 \), \( \A = \diag(2, 0) \), \( \B = \begin{psmallmatrix} 1 & 1 \\ 1 & 1\end{psmallmatrix} \) and \( \theta = \tfrac12 \). Compute \( \tr f(\A) \), \( \tr f(\B) \) and \( \tr f(\C) \) for \( \C = \tfrac12(\A + \B) \), and verify @thm-trace-convex.
2. Let \( f(t) = -\log t \), \( \A = \I_2 \), \( \B = \diag(4, \tfrac14) \) and \( \theta = \tfrac12 \). Do the same, and state the inequality in terms of determinants.
:::
::::

::: {.solution}
(a) Both matrices are real symmetric, hence Hermitian. \( \A^2 = \diag(4,0) \), so \( \tr f(\A) = 4 \); and \( \B^2 = \begin{psmallmatrix} 2 & 2 \\ 2 & 2\end{psmallmatrix} \), so \( \tr f(\B) = 4 \). Next
\[
\C = \tfrac12\begin{pmatrix} 3 & 1 \\ 1 & 1\end{pmatrix} = \begin{pmatrix} \tfrac32 & \tfrac12 \\[2pt] \tfrac12 & \tfrac12\end{pmatrix} ,
\qquad
\C^2 = \begin{pmatrix} \tfrac52 & 1 \\[2pt] 1 & \tfrac12\end{pmatrix} ,
\]
so \( \tr f(\C) = \tfrac52 + \tfrac12 = 3 \). The theorem asserts \( 3 \le \tfrac12\cdot 4 + \tfrac12\cdot 4 = 4 \), which holds.

(b) Both are positive definite, so their spectra lie in \( (0, \infty) \). By @exm-logdet-convex, \( \tr f(\M) = -\log\det\M \). Here \( \det\A = 1 \) and \( \det\B = 4 \cdot \tfrac14 = 1 \), so both traces are \( -\log 1 = 0 \). The midpoint is \( \C = \diag(\tfrac52, \tfrac58) \), with \( \det\C = \tfrac{25}{16} \), so \( \tr f(\C) = -\log\tfrac{25}{16} \). The theorem asserts
\[
-\log\tfrac{25}{16} \ \le\ \tfrac12\cdot 0 + \tfrac12\cdot 0 = 0 ,
\]
which holds because \( \tfrac{25}{16} > 1 \) and \( \log \) is increasing with \( \log 1 = 0 \) (@lem-exp-log (c)). In determinant form: \( \det\C = \tfrac{25}{16} \ge 1 = \sqrt{\det\A\,\det\B} \).
:::

### C. Going deeper

:::: {#exr-convex-functions-and-majorization-c1}
[C1: Entropy]

For \( \x \) in \( A = \{\x \in \nR^n : x_i > 0 \text{ for every } i\} \), let \( H(\x) = -\sum_i x_i\log x_i \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( g(t) = t\log t \) is convex on \( (0, \infty) \). *Hint: apply @thm-jensen to the concave \( \log \), with the points \( 1/a \), \( 1/b \) and cleverly chosen weights.*
2. Deduce that \( H \) is Schur-concave on \( A \).
3. Deduce that \( H(\x) \le \log n \) for every \( \x \in A \) with \( \sum_i x_i = 1 \), with equality when \( \x = (\tfrac1n, \dots, \tfrac1n) \).
:::
::::

::: {.solution}
(a) Let \( a, b > 0 \) and \( 0 \le \theta \le 1 \), and put \( c = \theta a + (1-\theta)b > 0 \). Set
\[
w_1 = \frac{\theta a}{c} , \qquad w_2 = \frac{(1-\theta)b}{c} ,
\]
which are non-negative and satisfy \( w_1 + w_2 = (\theta a + (1-\theta)b)/c = 1 \). The function \( -\log \) is convex on \( (0,\infty) \) by @lem-exp-log (c), so @thm-jensen with the points \( 1/a \) and \( 1/b \) gives
\[
-\log\Bigl(w_1\frac1a + w_2\frac1b\Bigr) \ \le\ -w_1\log\frac1a - w_2\log\frac1b .
\]
Now \( w_1/a + w_2/b = \theta/c + (1-\theta)/c = 1/c \), and \( \log(1/a) = -\log a \) since \( \log a + \log(1/a) = \log 1 = 0 \) (@lem-exp-log (c)). So the display reads
\[
\log c \ \le\ w_1\log a + w_2\log b = \frac{\theta a\log a + (1-\theta)b\log b}{c} .
\]
Multiplying by \( c > 0 \) gives \( c\log c \le \theta a\log a + (1-\theta)b\log b \), which is @def-convex-function for \( g \).

(b) By (a) and @thm-karamata with \( I = (0,\infty) \), \( \x \prec \y \) in \( A \) implies \( \sum_i x_i\log x_i \le \sum_i y_i\log y_i \), that is, \( H(\x) \ge H(\y) \). By @def-schur-concave, \( H \) is Schur-concave. (The set \( A \) is symmetric and convex, so @def-schur-concave applies.)

(c) Let \( \x \in A \) with \( \sum_i x_i = 1 \). Its mean is \( \tfrac1n \), so the flat vector \( \f = (\tfrac1n, \dots, \tfrac1n) \) satisfies \( \f \prec \x \) by @exm-majorization-first-examples (b), and \( \f \in A \). By (b), \( H(\f) \ge H(\x) \). Finally
\[
H(\f) = -\sum_{i=1}^{n}\tfrac1n\log\tfrac1n = -\log\tfrac1n = \log n ,
\]
using \( \log\tfrac1n = -\log n \). So \( H(\x) \le \log n \), with equality at \( \x = \f \).
:::

:::: {#exr-convex-functions-and-majorization-c2}
[C2: Three norms under majorization]

Let \( \x \prec \y \) in \( \nR^n \). Prove that
\[
\norm{\x}_1 \le \norm{\y}_1 , \qquad
\norm{\x}_2 \le \norm{\y}_2 , \qquad
\norm{\x}_\infty \le \norm{\y}_\infty .
\]
Which of the three needs @thm-karamata, and which follows from @def-majorization alone?
::::

::: {.solution}
For \( \norm{\cdot}_1 \), apply @thm-karamata with \( \phi(t) = \lvert t\rvert \), convex on \( \nR \) by @prp-sup-of-affine-convex: \( \sum_i\lvert x_i\rvert \le \sum_i\lvert y_i\rvert \).

For \( \norm{\cdot}_2 \), apply @thm-karamata with \( \phi(t) = t^2 \), convex on \( \nR \) by @lem-convex-one-variable, since its derivative \( 2t \) is increasing: \( \sum_i x_i^2 \le \sum_i y_i^2 \). Both sides are non-negative and \( t \mapsto \sqrt t \) is increasing on \( [0,\infty) \), so \( \norm{\x}_2 \le \norm{\y}_2 \).

For \( \norm{\cdot}_\infty \), no convexity is needed. Since \( \norm{\z}_\infty = \max_i\lvert z_i\rvert = \max\{z^{\downarrow}_1,\ -z^{\downarrow}_n\} \), and (M1) at \( k = 1 \) gives \( x^{\downarrow}_1 \le y^{\downarrow}_1 \) while subtracting (M1) at \( k = n-1 \) from (M2) gives \( x^{\downarrow}_n \ge y^{\downarrow}_n \), hence \( -x^{\downarrow}_n \le -y^{\downarrow}_n \). The maximum of the two smaller numbers is at most the maximum of the two larger ones.

So the \( \infty \)-norm follows from @def-majorization directly, and the other two from @thm-karamata. A later section of this chapter proves the same for **every** norm that is invariant under permuting and changing the signs of the coordinates.
:::

:::: {#exr-convex-functions-and-majorization-c3}
[C3: One convex function is not enough]

Let \( \x = (2, -1, -1) \) and \( \y = (1, 1, -2) \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \sum_i x_i = \sum_i y_i \) and \( \sum_i x_i^2 = \sum_i y_i^2 \), yet neither \( \x \prec \y \) nor \( \y \prec \x \).
2. Exhibit a convex \( \phi \) with \( \sum_i\phi(x_i) > \sum_i\phi(y_i) \), and another with the inequality reversed. Explain how this is consistent with @prp-majorization-from-convex.
:::
::::

::: {.solution}
(a) Both totals are \( 0 \), and \( \sum_i x_i^2 = 4 + 1 + 1 = 6 = 1 + 1 + 4 = \sum_i y_i^2 \). Both vectors are already decreasing, with running totals \( 2, 1 \) for \( \x \) and \( 1, 2 \) for \( \y \). (M1) at \( k = 1 \) fails for \( \x \prec \y \), since \( 2 > 1 \), and (M1) at \( k = 2 \) fails for \( \y \prec \x \), since \( 2 > 1 \).

(b) Take \( \phi(t) = \max\{t - 1, 0\} \), convex by @prp-sup-of-affine-convex. Then \( \sum_i\phi(x_i) = 1 + 0 + 0 = 1 \) and \( \sum_i\phi(y_i) = 0 + 0 + 0 = 0 \), so \( 1 > 0 \). This is the test function of @prp-majorization-from-convex at \( c = y^{\downarrow}_1 = 1 \), and it certifies \( \x \not\prec \y \).

Take \( \psi(t) = \max\{t + 1, 0\} \). Then \( \sum_i\psi(x_i) = 3 + 0 + 0 = 3 \) and \( \sum_i\psi(y_i) = 2 + 2 + 0 = 4 \), so \( 3 < 4 \), certifying \( \y \not\prec \x \) by the same proposition applied with the roles exchanged, at \( c = x^{\downarrow}_2 = -1 \).

There is no contradiction: @prp-majorization-from-convex asks the inequality to hold for **every** convex \( \phi \). Agreeing on the affine functions and on \( t^2 \) is far from agreeing on all of them, and here two hockey sticks pull in opposite directions.
:::
