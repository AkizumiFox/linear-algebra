# Three Classical Inequalities

§10 built the basic theory of convex functions. This section spends it on three classical inequalities, each obtained from the one before. Jensen's inequality for the logarithm is the weighted arithmetic–geometric mean inequality; with two weights it is Young's inequality; and Young's inequality, applied coordinate by coordinate, is Hölder's. Hölder's inequality then settles two questions the book left open: the triangle inequality for the \( p \)-norm, which Chapter 15 §01 recorded without proof, and the dual of the \( p \)-norm, which §04 computed only for \( p = 1, 2, \infty \).

**Throughout, the field is \( \nR \)**, and "increasing" and "strictly increasing" are meant as in §10.

## The logarithm and real powers

The first inequality needs a logarithm, and the book has none. It has the exponential: by fact (A1) of Chapter 9 §09, for real \( s \) the series \( \sum_i s^i/i! \) converges to a real number \( e^s \), with \( e^{s + u} = e^se^u \), \( e^0 = 1 \) and \( e^s \ge 1 \) for \( s \ge 0 \); and \( \frac{d}{dt}e^{t} = e^{t} \) is the \( 1 \times 1 \) case of @thm-exponential-properties (b). We construct the logarithm as its inverse.

::: {#lem-exp-log}
[Exponential and Logarithm]

::: {.enumerate options="label=(\alph*)"}
1. \( e^{s} > 0 \) for every real \( s \), and \( s \mapsto e^s \) is strictly increasing and strictly convex on \( \nR \).
2. For every real \( y > 0 \) there is exactly one real \( s \) with \( e^s = y \); write \( s = \log y \).
3. \( \log \colon (0, \infty) \to \nR \) is strictly increasing and **strictly concave**, with \( \log(xy) = \log x + \log y \) and \( \log 1 = 0 \).
:::
:::

::: {.idea}
The exponential is positive and is its own derivative, so it is strictly increasing with a strictly increasing derivative, hence strictly convex. The intermediate value theorem makes it take every positive value, so it has an inverse. Applying that increasing inverse to the convexity inequality of \( \exp \) turns it into concavity of \( \log \).
:::

::: {.proof}
(a) If \( s \ge 0 \) then \( e^s \ge 1 > 0 \). If \( s < 0 \) then \( e^{-s} \ge 1 \), and \( e^se^{-s} = e^0 = 1 \), so \( e^s = 1/e^{-s} > 0 \). The derivative \( e^s \) is therefore positive everywhere, and by the linearity of differentiation, fact (A3) of Chapter 9 §09, \( -\exp \) has the negative derivative \( -\exp \). By fact (A6) of Chapter 15's introduction, \( -\exp \) is strictly decreasing, so \( \exp \) is strictly increasing. So \( g = \exp \) has a strictly increasing derivative, and @lem-convex-one-variable makes it strictly convex.

(b) Uniqueness holds because \( \exp \) is strictly increasing. For existence, note first that \( \exp \) is continuous: \( e^{t + h} - e^t = e^t\,h\cdot(e^h - 1)/h \), and \( (e^h - 1)/h \to 1 \) is the derivative at \( 0 \), so the right side tends to \( 0 \). Let \( y \ge 1 \). For \( s \ge 0 \) every partial sum of the series with at least two terms is at least \( 1 + s \), so \( e^s \ge 1 + s \), since a non-strict inequality survives a limit. Hence \( e^y \ge 1 + y > y \), while \( e^0 = 1 \le y \). The intermediate value theorem, fact (A5) of Chapter 15's introduction, gives \( s \in [0, y] \) with \( e^s = y \). If \( 0 < y < 1 \), apply this to \( 1/y > 1 \) to get \( e^{s'} = 1/y \); then \( e^{-s'} = y \).

(c) If \( 0 < x < y \) and \( \log x \ge \log y \), then \( x = e^{\log x} \ge e^{\log y} = y \), since \( \exp \) is increasing, which is false. So \( \log \) is strictly increasing. Next, \( e^{\log x + \log y} = e^{\log x}e^{\log y} = xy \), so \( \log(xy) = \log x + \log y \) by uniqueness in (b), and \( e^0 = 1 \) gives \( \log 1 = 0 \). For concavity, let \( x, y > 0 \) and \( 0 \le t \le 1 \), and put \( a = \log x \), \( b = \log y \). By (a),
\[
e^{ta + (1-t)b} \le te^a + (1-t)e^b = tx + (1-t)y .
\]
Applying the increasing function \( \log \) to both sides gives \( t\log x + (1-t)\log y \le \log\bigl(tx + (1-t)y\bigr) \). If \( x \ne y \) and \( 0 < t < 1 \), then \( a \ne b \), the first inequality is strict by strict convexity, and \( \log \) keeps it strict. So \( -\log \) is strictly convex.
:::

**Real powers.** For \( t > 0 \) and real \( r \) put \( t^r = e^{r\log t} \), and \( 0^r = 0 \) for \( r > 0 \). For a positive integer \( r \) this is the usual power, since \( e^{r\log t} = (e^{\log t})^r = t^r \) by \( e^{s+u} = e^se^u \). For \( t, a, b > 0 \) and real \( r, u \), the rules \( e^{s+u} = e^se^u \) and \( \log(ab) = \log a + \log b \), with \( \log(t^r) = r\log t \) from the uniqueness in (b), give
\[
t^rt^u = t^{r+u}, \qquad (t^r)^u = t^{ru}, \qquad (ab)^r = a^rb^r, \qquad (a/b)^r = a^r/b^r .
\]
The first three extend to \( t, a, b \ge 0 \), and the last to \( a \ge 0 \), when the exponents \( r \) and \( u \) are positive: then a zero base makes both sides \( 0 \). They do not extend further, since \( 0^r \) is not defined for \( r \le 0 \). Finally, for \( r > 0 \) the function \( t \mapsto t^r \) is strictly increasing on \( [0, \infty) \): on \( (0, \infty) \) it is \( \exp \) applied to the strictly increasing \( r\log t \), and \( 0^r = 0 < t^r \) for \( t > 0 \). This is the meaning of \( \lvert x_i\rvert^{p} \) and of the exponent \( 1/p \) in the \( p \)-norm \( \norm{\x}_p = (\sum_i\lvert x_i\rvert^p)^{1/p} \) of Chapter 15 §01.

## Arithmetic and geometric means

Chapter 16 §08 proved @lem-am-gm, the arithmetic–geometric mean inequality, by pure algebra: an induction that merges a number above the mean with one below it. Concavity of the logarithm gives a second proof, and a stronger statement, with arbitrary weights.

::: {#thm-weighted-am-gm}
[Weighted Arithmetic–Geometric Mean Inequality]

Let \( t_1, \dots, t_m \ge 0 \), and let \( w_1, \dots, w_m > 0 \) with \( w_1 + \dots + w_m = 1 \). Then
\[
t_1^{w_1}t_2^{w_2}\cdots t_m^{w_m} \ \le\ w_1t_1 + w_2t_2 + \dots + w_mt_m ,
\]
with equality if and only if \( t_1 = t_2 = \dots = t_m \).
:::

::: {.idea}
Take logarithms. The product becomes the weighted average \( \sum_iw_i\log t_i \), and the inequality becomes Jensen's inequality for the concave \( \log \). Then exponentiate back.
:::

::: {.proof}
If some \( t_j = 0 \), the left side is \( 0 \), since \( 0^{w_j} = 0 \), and the right side is \( \ge 0 \). Equality then means \( \sum_iw_it_i = 0 \), which with every \( w_i > 0 \) and \( t_i \ge 0 \) forces every \( t_i = 0 \); conversely, if every \( t_i = 0 \), both sides are \( 0 \).

So let every \( t_i > 0 \). By @lem-exp-log (c), \( -\log \) is strictly convex on \( (0, \infty) \), so @thm-jensen gives
\[
\sum_{i=1}^m w_i\log t_i \ \le\ \log\Bigl(\sum_{i=1}^m w_it_i\Bigr) ,
\]
with equality only when all \( t_i \) are equal. Apply the strictly increasing function \( \exp \). The right side becomes \( \sum_iw_it_i \), and the left side becomes \( \prod_ie^{w_i\log t_i} = \prod_it_i^{w_i} \), by \( e^{s+u} = e^se^u \) and the definition of real powers. A strictly increasing function preserves both the inequality and its strictness, so equality holds exactly when all \( t_i \) are equal.
:::

**The case of equal weights is @lem-am-gm.** With \( w_i = 1/n \), the rules for powers turn the theorem into \( (t_1\cdots t_n)^{1/n} \le \tfrac1n\sum_it_i \). Since \( u \mapsto u^n \) is strictly increasing on \( [0, \infty) \), raising both sides to the \( n \)-th power gives \( t_1\cdots t_n \le (\tfrac1n\sum_it_i)^{n} \), with the same equality case. That is @lem-am-gm, now with arbitrary weights and seen as Jensen's inequality for the logarithm.

With two weights, the theorem becomes an inequality about products that is exactly what Hölder's inequality needs.

::: {#lem-young}
[Young's Inequality]

Let \( p, q > 1 \) with \( \frac1p + \frac1q = 1 \). Then for all real \( a, b \ge 0 \),
\[
ab \ \le\ \frac{a^p}{p} + \frac{b^q}{q} ,
\]
with equality if and only if \( a^p = b^q \).
:::

::: {.proof}
Apply @thm-weighted-am-gm with \( m = 2 \), \( t_1 = a^p \), \( t_2 = b^q \), \( w_1 = 1/p \) and \( w_2 = 1/q \). The weights are positive and add up to \( 1 \), and \( (a^p)^{1/p} = a \), \( (b^q)^{1/q} = b \) by the rules for powers. So the left side of the theorem is \( ab \) and the right side is \( a^p/p + b^q/q \), with equality exactly when \( a^p = b^q \).
:::

## Hölder's inequality and the dual p-norms

Two exponents \( p, q \in (1, \infty) \) with \( \frac1p + \frac1q = 1 \) are called **conjugate**; equivalently \( q = p/(p-1) \). The pair \( p = q = 2 \) is conjugate to itself. Hölder's inequality is the Cauchy–Schwarz inequality with the two factors measured in two different norms.

::: {#thm-holder}
[Hölder's Inequality]

Let \( p, q \in (1, \infty) \) be conjugate exponents. For all \( \x, \y \in \nR^n \),
\[
\lvert\inner{\x}{\y}\rvert \ \le\ \sum_{i=1}^{n}\lvert x_iy_i\rvert \ \le\ \norm{\x}_p\norm{\y}_q .
\]
:::

::: {.idea}
Both sides of the second inequality scale the same way when \( \x \) or \( \y \) is multiplied by a positive number. So normalize to \( \norm{\x}_p = \norm{\y}_q = 1 \). Then apply Young's inequality coordinate by coordinate and add: the right-hand sides add up to \( \tfrac1p + \tfrac1q = 1 \).
:::

::: {.proof}
The first inequality is the triangle inequality for numbers (@thm-complex-triangle-inequality) applied to \( \sum_ix_iy_i \). For the second, if \( \x = \0 \) or \( \y = \0 \) both sides are \( 0 \). Otherwise \( \norm{\x}_p > 0 \) and \( \norm{\y}_q > 0 \); put \( a_i = \lvert x_i\rvert/\norm{\x}_p \) and \( b_i = \lvert y_i\rvert/\norm{\y}_q \). Then \( \sum_ia_i^p = \sum_i\lvert x_i\rvert^p/\norm{\x}_p^p = 1 \), because \( \norm{\x}_p^p = \sum_i\lvert x_i\rvert^p \) by the rules for powers, and likewise \( \sum_ib_i^q = 1 \). By @lem-young for each \( i \), and adding,
\[
\sum_{i=1}^n a_ib_i \ \le\ \frac1p\sum_{i=1}^n a_i^p + \frac1q\sum_{i=1}^n b_i^q = \frac1p + \frac1q = 1 .
\]
Multiplying by \( \norm{\x}_p\norm{\y}_q \) gives \( \sum_i\lvert x_iy_i\rvert \le \norm{\x}_p\norm{\y}_q \), as claimed.
:::

For \( p = q = 2 \) this is @thm-cauchy-schwarz for the standard inner product on \( \nR^n \), reached without the inner product's geometry. The limiting pair \( p = 1 \), \( q = \infty \) holds too, and more simply: \( \sum_i\lvert x_iy_i\rvert \le \sum_i\lvert x_i\rvert\norm{\y}_\infty \).

Chapter 15 §01 recorded the \( p \)-norm for every \( p \ge 1 \), but verified only \( p = 1, 2, \infty \), because the triangle inequality for general \( p \) had not been proved. Hölder's inequality proves it.

::: {#cor-minkowski-inequality}
[Minkowski's Inequality]

Let \( 1 < p < \infty \). For all \( \x, \y \in \nR^n \), \( \norm{\x + \y}_p \le \norm{\x}_p + \norm{\y}_p \). Consequently \( \norm{\cdot}_p \) is a norm on \( \nR^n \).
:::

::: {.idea}
Split \( \lvert z_i\rvert^p = \lvert z_i\rvert\cdot\lvert z_i\rvert^{p-1} \) and use the triangle inequality on the first factor. That leaves two sums, and Hölder's inequality bounds each, with the same second factor \( (\lvert z_i\rvert^{p-1})_i \). Dividing by that common factor's norm leaves the triangle inequality.
:::

::: {.proof}
Let \( q = p/(p-1) \) be the conjugate exponent, and put \( \z = \x + \y \). If \( \z = \0 \) there is nothing to prove. Otherwise, by the triangle inequality for numbers in each coordinate (@thm-complex-triangle-inequality),
\[
\begin{aligned}
\sum_i\lvert z_i\rvert^p &= \sum_i\lvert z_i\rvert\,\lvert z_i\rvert^{p-1} \\
&\le \sum_i\lvert x_i\rvert\,\lvert z_i\rvert^{p-1} + \sum_i\lvert y_i\rvert\,\lvert z_i\rvert^{p-1} .
\end{aligned}
\]
Apply @thm-holder to each sum, with the vector \( \w = (\lvert z_1\rvert^{p-1}, \dots, \lvert z_n\rvert^{p-1}) \) as the second factor. Since \( (p-1)q = p \),
\[
\norm{\w}_q = \Bigl(\sum_i\lvert z_i\rvert^{p}\Bigr)^{1/q} = \norm{\z}_p^{p/q} .
\]
So \( \norm{\z}_p^{p} \le (\norm{\x}_p + \norm{\y}_p)\norm{\z}_p^{p/q} \). Divide by \( \norm{\z}_p^{p/q} > 0 \), and use \( p - p/q = p(1 - 1/q) = 1 \), to get \( \norm{\z}_p \le \norm{\x}_p + \norm{\y}_p \). This is (N3) of @def-norm. (N1) holds because \( \norm{\x}_p = 0 \) forces every \( \lvert x_i\rvert^p = 0 \), and (N2) because \( \bigl(\sum_i\lvert c\rvert^p\lvert x_i\rvert^p\bigr)^{1/p} = \lvert c\rvert\norm{\x}_p \) by the rules for powers.
:::

The proof uses the coordinates only through their moduli: the triangle inequality \( \lvert x_i + y_i\rvert \le \lvert x_i\rvert + \lvert y_i\rvert \), which @thm-complex-triangle-inequality proves for complex numbers as well, and Hölder's inequality for the real vectors \( (\lvert x_i\rvert)_i \), \( (\lvert y_i\rvert)_i \) and \( \w \), whose \( p \)-norms are those of \( \x \) and \( \y \). So it works verbatim on \( \nC^n \), and \( \norm{\cdot}_p \) is a norm on \( F^n \) for \( F = \nR \) and for \( F = \nC \), as Chapter 15 §01 recorded.

Now the dual norm. Recall from @def-dual-norm that the dual norm of \( \norm{\cdot} \) at \( \y \) is the largest value of \( \inner{\x}{\y} \) over the unit ball \( \norm{\x} \le 1 \). §04 computed it for \( p = 1, 2, \infty \): the \( 1 \)-norm and the \( \infty \)-norm are dual to each other, and the \( 2 \)-norm is dual to itself. Hölder's inequality supplies an upper bound for every other \( p \), and a matching vector shows it is attained.

::: {#thm-dual-p-norm}
[The Dual of the p-Norm]

Let \( p, q \in (1, \infty) \) be conjugate exponents. On \( \nR^n \) with the standard inner product, the dual norm of \( \norm{\cdot}_p \) is \( \norm{\cdot}_q \):
\[
\max\{\inner{\x}{\y} : \norm{\x}_p \le 1\} = \norm{\y}_q \qquad (\y \in \nR^n) .
\]
For \( \y \ne \0 \) the maximum is attained at \( \x \) with \( x_i = \sigma_i\lvert y_i\rvert^{q-1}/\norm{\y}_q^{q-1} \), where \( \sigma_i = 1 \) if \( y_i \ge 0 \) and \( \sigma_i = -1 \) otherwise.
:::

::: {.idea}
Hölder's inequality bounds \( \inner{\x}{\y} \) by \( \norm{\y}_q \) on the whole unit ball. To show the bound is attained, give \( x_i \) the sign of \( y_i \) and make \( \lvert x_i\rvert^p \) proportional to \( \lvert y_i\rvert^q \), which is when Young's inequality (@lem-young) is an equality in each coordinate. That is the stated witness, and a direct computation checks it.
:::

::: {.proof}
If \( \norm{\x}_p \le 1 \), then \( \inner{\x}{\y} \le \norm{\x}_p\norm{\y}_q \le \norm{\y}_q \) by @thm-holder. For \( \y = \0 \) the bound \( 0 \) is attained at \( \x = \0 \). For \( \y \ne \0 \), take \( \x \) as in the statement. Since \( (q-1)p = q \),
\[
\sum_i\lvert x_i\rvert^p = \frac{\sum_i\lvert y_i\rvert^{q}}{\norm{\y}_q^{q}} = 1 ,
\]
so \( \norm{\x}_p = 1 \); and since \( \sigma_iy_i = \lvert y_i\rvert \),
\[
\inner{\x}{\y} = \frac{\sum_i\lvert y_i\rvert^{q}}{\norm{\y}_q^{q-1}} = \frac{\norm{\y}_q^{q}}{\norm{\y}_q^{q-1}} = \norm{\y}_q .
\]
So the bound is attained, and the largest value is \( \norm{\y}_q \).
:::

::: {#exm-dual-three-halves-norm}
[A dual norm by hand]

Let \( \y = (3, -4, 5) \in \nR^3 \), and let \( p = \tfrac32 \) and \( q = 3 \). Compute the dual norm of \( \y \) with respect to \( \norm{\cdot}_{3/2} \), find a vector \( \x \) with \( \norm{\x}_{3/2} = 1 \) at which it is attained, and compare with the value at the unit vector \( \e_3 \).
:::

::: {.solution}
The exponents are conjugate, since \( \tfrac1p + \tfrac1q = \tfrac23 + \tfrac13 = 1 \). Next, \( \lvert 3\rvert^3 + \lvert -4\rvert^3 + \lvert 5\rvert^3 = 27 + 64 + 125 = 216 = 6^3 \), so \( \norm{\y}_3 = 216^{1/3} = 6 \), using \( (6^3)^{1/3} = 6 \). By @thm-dual-p-norm the dual norm is \( 6 \).

For the maximizer, \( q - 1 = 2 \), so \( x_i = \sigma_i\lvert y_i\rvert^{2}/6^{2} \) with \( \sigma_i \) the sign of \( y_i \):
\[
\x = \bigl(\tfrac{9}{36}, -\tfrac{16}{36}, \tfrac{25}{36}\bigr) = \bigl(\tfrac14, -\tfrac49, \tfrac{25}{36}\bigr) .
\]
Check: \( \lvert x_i\rvert^{3/2} = (\lvert y_i\rvert^2/36)^{3/2} = \lvert y_i\rvert^3/216 \), giving \( \tfrac18 + \tfrac{8}{27} + \tfrac{125}{216} = \tfrac{27 + 64 + 125}{216} = 1 \). So \( \norm{\x}_{3/2} = 1 \). And \( \inner{\x}{\y} = \tfrac34 + \tfrac{16}{9} + \tfrac{125}{36} = \tfrac{27 + 64 + 125}{36} = 6 \).

The unit vector \( \e_3 \) has \( \norm{\e_3}_{3/2} = 1 \) and gives \( \inner{\e_3}{\y} = 5 < 6 \). Putting all the weight on the largest coordinate of \( \y \) is not optimal; the maximizer spreads it in proportion to \( \lvert y_i\rvert^2 \).
:::

Exchanging the roles of \( p \) and \( q \) shows that the dual of \( \norm{\cdot}_q \) is \( \norm{\cdot}_p \), just as @thm-dual-dual-norm requires. Together with §04, the dual norm of \( \norm{\cdot}_p \) is now known for every \( p \in [1, \infty] \): it is \( \norm{\cdot}_q \) with \( \frac1p + \frac1q = 1 \), reading \( \frac1\infty \) as \( 0 \). This completes §04's computation. Chapter 15 measured vectors and matrices but never a linear functional; §04's dual norm filled that gap, and now it is computed for every \( p \)-norm.

Look back at the chain. One convexity fact, that \( -\log \) is strictly convex, went through Jensen's inequality to the weighted arithmetic–geometric mean inequality, through two weights to Young's inequality, and through normalization to Hölder's. Hölder's inequality then did two jobs that earlier chapters could not: it proved that every \( \norm{\cdot}_p \) is a norm, so that its unit ball is one of the convex sets this chapter began with, and it computed the dual of every such norm.

## Summary and transfer

The chapter began with a word the book had been using without studying it. Convexity turned up in the positive semidefinite cone of Chapter 12, in the unit balls of Chapter 15, and in the Ky Fan sums of Chapter 16. The chapter ends with convexity as a subject: convex sets, the hyperplanes that separate them, the duality between a cone and its dual, extreme points and polytopes, and convex functions. Six moves did the work, and each transfers beyond this chapter.

- **Nearest point, then the normal direction.** Project onto a closed convex set; the vector from the projection to the point is the normal of a separating hyperplane (§03, Separating Hyperplanes). This is Chapter 10's best approximation, with an inequality where the equation was. *Transfer:* to prove that a point lies outside a closed convex set, and to certify it, look for the nearest point.
- **Count, then drop a point.** Too many points in \( n \) dimensions are affinely dependent, and moving the weights along the dependence removes one of them without leaving the hull (§02, Carathéodory's Theorem). Among too many generators of a cone, a linear dependence does the same (§05, Cones and Farkas's Lemma). *Transfer:* when a representation uses more pieces than the dimension allows, the surplus is a dependence, and a dependence can be spent.
- **Dualize.** A closed convex cone is determined by its dual cone, and every statement about the one has a statement about the other. Farkas's lemma is this move made into a theorem, linear programming duality (§06, Linear Programming Duality) is Farkas applied to one combined system, and the minimax theorem (§07, Matrix Games and the Minimax Theorem) is a duality statement of the same kind. *Transfer:* when a feasibility question will not yield, ask for the certificate that it fails.
- **Lift, then eliminate.** A hull of finitely many points is the projection of a polyhedron in a bigger space, with the weights as extra coordinates, and Fourier–Motzkin elimination removes those coordinates one at a time while keeping a system of inequalities (§09, Polytopes, @thm-minkowski-weyl). *Transfer:* to describe the image of a set given by inequalities, add the hidden variables as coordinates and eliminate them.
- **A supremum of linear functions is convex.** Support functions, dual norms, \( \lambda_1 \) and the Ky Fan sums are convex for this one reason (§04, Gauges, Support Functions and Dual Norms, and §10, Convex Functions, @prp-sup-of-affine-convex). Its companion: a linear function on a compact convex set peaks at an extreme point (§08, Extreme Points). *Transfer:* to prove a function convex, write it as a maximum of affine functions.
- **Compactness turns a supremum into a maximum.** Once a hull, a ball or a set of weights is known to be compact, facts (A3) and (A4) of Chapter 15's introduction produce a nearest point, a maximizer or an extreme point that can be named and used. *Transfer:* before optimizing, check that the set is compact; afterwards, feed the maximizer back into the argument.

§§10–11 added two moves of their own. **Second differences**: on a segment, convexity is read off from \( f(\z + s\v) + f(\z - s\v) - 2f(\z) \) (§10, @thm-convex-second-derivative). **Normalize, then use a two-point inequality**: Hölder's inequality is Young's inequality after scaling both vectors to norm \( 1 \) (§11, @thm-holder). *Transfer:* if multiplying any one variable by \( c > 0 \) multiplies both sides by the same power of \( c \), check the cases with a zero variable directly, and then assume every variable has norm \( 1 \).

The chapter also paid promises made in earlier chapters.

| The promise | Made in | Paid by |
|---|---|---|
| "Chapter 17 studies convex functions in general, and the observation that a pointwise supremum of linear functions is convex is one of its basic facts" | Chapter 16 §06 | §10 (Convex Functions), @prp-sup-of-affine-convex, with \( \lambda_1 \) and the Ky Fan sums as its instances (@cor-eigenvalue-sums-convex) |
| Non-negativity and capacities turn traffic flow "into one about inequalities, which is the subject of linear programming" | Chapter 2 §07 | §06 (Linear Programming Duality) |
| A way to measure a linear functional: Chapter 15 measured vectors and matrices, but never a functional | Chapter 15 | §04 (Gauges, Support Functions and Dual Norms): the definition, the double dual, and \( p = 1, 2, \infty \); §11 (Three Classical Inequalities): every \( 1 < p < \infty \), @thm-dual-p-norm |
| The triangle inequality for \( \norm{\cdot}_p \), recorded without proof, "which Chapter 17 proves from Hölder's inequality" | Chapter 15 §01 | §11 (Three Classical Inequalities), @cor-minkowski-inequality |

Some things the chapter did not do. It stated Birkhoff's theorem, that the extreme points of the doubly stochastic matrices are exactly the permutation matrices, and left its proof to Chapter 18. The convexity of \( \A \mapsto \tr f(\A) \) for convex \( f \), and the consequences of a majorization for every convex function, belong to Chapter 20. Convex optimization beyond linear programs, where a duality gap can occur, lies outside this chapter.

## Exercises

### A. Check your understanding

:::: {#exr-classical-inequalities-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State Young's inequality, with its hypotheses and its equality case.
2. Decide whether the following is correct, and justify your answer: the exponent conjugate to \( p = 4 \) is \( q = \tfrac43 \).
3. Decide whether the following is correct, and justify your answer: \( (t^r)^u = t^{ru} \) for every real \( t \ge 0 \) and all real \( r, u \).
4. Decide whether the following is correct, and justify your answer: if \( p, q \) are conjugate and \( \inner{\x}{\y} = \norm{\x}_p\norm{\y}_q \) for \( \x, \y \in \nR^n \), then one of \( \x, \y \) is a scalar multiple of the other.
5. Name the convex function to which the proof of @thm-weighted-am-gm applies Jensen's inequality, and say why the equality case needs it to be **strictly** convex.
:::
::::

::: {.solution}
(a) Let \( p, q > 1 \) with \( \frac1p + \frac1q = 1 \). Then \( ab \le a^p/p + b^q/q \) for all real \( a, b \ge 0 \), with equality if and only if \( a^p = b^q \) (@lem-young).

(b) Correct. \( \tfrac14 + \tfrac34 = 1 \); equivalently \( q = p/(p-1) = 4/3 \).

(c) Incorrect. Take \( t = 0 \), \( r = 1 \) and \( u = -1 \). Then \( t^r = 0 \), and \( 0^{-1} \) is not defined, since \( 0^r \) is defined only for \( r > 0 \); neither side has a value. The rule holds for \( t > 0 \) and all real \( r, u \), and for \( t = 0 \) when \( r, u > 0 \).

(d) Incorrect. Take \( p = 3 \), \( q = \tfrac32 \), \( \x = (1, 2) \) and \( \y = (1, 4) \). Then \( \inner{\x}{\y} = 1 + 8 = 9 \), \( \norm{\x}_3 = (1 + 8)^{1/3} = 9^{1/3} \) and \( \norm{\y}_{3/2} = (1 + 4^{3/2})^{2/3} = 9^{2/3} \), since \( 4^{3/2} = 8 \); so \( \norm{\x}_3\norm{\y}_{3/2} = 9^{1/3 + 2/3} = 9 \). But neither vector is a multiple of the other, since \( 1 \cdot 4 - 2 \cdot 1 \ne 0 \). Equality asks for \( \lvert x_i\rvert^p \) to be proportional to \( \lvert y_i\rvert^q \), not \( \x \) to \( \y \) (exercise C2).

(e) It is \( -\log \) on \( (0, \infty) \), which is strictly convex by @lem-exp-log (c). @thm-jensen proves its equality clause only for strictly convex functions, and the hypothesis is needed: an affine function makes Jensen's inequality an equality for every choice of points.
:::

### B. Practice

:::: {#exr-classical-inequalities-b1}
[B1: A dual norm by hand]

Let \( \y = (1, -6, 8) \in \nR^3 \), and let \( p = \tfrac32 \) and \( q = 3 \).

::: {.enumerate options="label=(\alph*)"}
1. Check that \( p \) and \( q \) are conjugate, and compute \( \norm{\y}_3 \).
2. Find \( \x \in \nR^3 \) with \( \norm{\x}_{3/2} = 1 \) and \( \inner{\x}{\y} = \norm{\y}_3 \).
3. Hence determine the dual norm of \( \y \) with respect to \( \norm{\cdot}_{3/2} \), and compare it with the value \( \inner{\e_3}{\y} \) at the unit vector \( \e_3 \).
:::
::::

::: {.solution}
(a) \( \tfrac1p + \tfrac1q = \tfrac23 + \tfrac13 = 1 \). Next, \( \lvert 1\rvert^3 + \lvert -6\rvert^3 + \lvert 8\rvert^3 = 1 + 216 + 512 = 729 = 9^3 \), so \( \norm{\y}_3 = 729^{1/3} = 9 \), using \( (9^3)^{1/3} = 9 \).

(b) Follow @thm-dual-p-norm: \( x_i = \sigma_i\lvert y_i\rvert^{2}/9^{2} \) with \( \sigma_i \) the sign of \( y_i \), since \( q - 1 = 2 \). So
\[
\x = \bigl(\tfrac{1}{81}, -\tfrac{36}{81}, \tfrac{64}{81}\bigr) = \bigl(\tfrac{1}{81}, -\tfrac49, \tfrac{64}{81}\bigr) .
\]
Check: \( \lvert x_i\rvert^{3/2} = (\lvert y_i\rvert^2/81)^{3/2} = \lvert y_i\rvert^3/729 \), giving \( \tfrac{1}{729} + \tfrac{216}{729} + \tfrac{512}{729} = 1 \). So \( \norm{\x}_{3/2} = 1 \). And \( \inner{\x}{\y} = \tfrac{1}{81} + \tfrac{216}{81} + \tfrac{512}{81} = \tfrac{729}{81} = 9 \).

(c) By @thm-dual-p-norm the dual norm is \( \norm{\y}_3 = 9 \), attained at the \( \x \) of (b). The unit vector \( \e_3 \) has \( \norm{\e_3}_{3/2} = 1 \) and gives \( \inner{\e_3}{\y} = 8 < 9 \): even when one coordinate of \( \y \) dominates, putting all the weight on it is not optimal.
:::

:::: {#exr-classical-inequalities-b2}
[B2: Harmonic and arithmetic means]

Let \( x_1, \dots, x_n > 0 \). Prove that
\[
\frac{n}{\frac{1}{x_1} + \dots + \frac{1}{x_n}} \ \le\ \frac{x_1 + \dots + x_n}{n} ,
\]
with equality if and only if \( x_1 = \dots = x_n \).
::::

::: {.solution}
By @exr-convex-functions-b1 (d), \( g(t) = 1/t \) is strictly convex on \( (0, \infty) \). Let \( m = \tfrac1n(x_1 + \dots + x_n) > 0 \). @thm-jensen with the weights \( w_i = 1/n > 0 \) gives
\[
\frac1m = g\Bigl(\sum_{i=1}^n\frac1n x_i\Bigr) \le \sum_{i=1}^n\frac1n\,g(x_i) = \frac1n\Bigl(\frac1{x_1} + \dots + \frac1{x_n}\Bigr) ,
\]
with equality only when all \( x_i \) are equal. Both sides are positive, and taking reciprocals reverses the inequality: \( m \ge n/(\sum_i 1/x_i) \), which is the claim. If all \( x_i \) equal \( c \), both sides equal \( c \). So equality holds exactly when the \( x_i \) are all equal.
:::

### C. Going deeper

:::: {#exr-classical-inequalities-c1}
[C1: The exponential above its tangent]

::: {.enumerate options="label=(\alph*)"}
1. Deduce from @exr-convex-functions-c2 (a) that \( e^{y} \ge 1 + y \) for every real \( y \).
2. Deduce that \( \log x \le x - 1 \) for every real \( x > 0 \).
:::
::::

::: {.solution}
(a) By @lem-exp-log (a), the function \( \exp \) is convex and differentiable on the open interval \( \nR \), with derivative \( \exp \). So @exr-convex-functions-c2 (a) applies, and at \( x = 0 \) it gives \( e^{y} \ge e^0 + e^0(y - 0) = 1 + y \). For \( y \ge 0 \) this was visible from the series, as in the proof of @lem-exp-log (b); for \( y < 0 \) it is new.

(b) Let \( x > 0 \) and put \( y = \log x \), so that \( e^y = x \) by @lem-exp-log (b). Part (a) gives \( x \ge 1 + \log x \), that is, \( \log x \le x - 1 \).
:::

:::: {#exr-classical-inequalities-c2}
[C2: When Hölder is an equality]

Let \( p, q \in (1, \infty) \) be conjugate exponents, and let \( \x, \y \in \nR^n \) be non-zero.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \sum_i\lvert x_iy_i\rvert = \norm{\x}_p\norm{\y}_q \) if and only if \( \lvert x_i\rvert^p/\norm{\x}_p^p = \lvert y_i\rvert^q/\norm{\y}_q^q \) for every \( i \).
2. Deduce that the maximizer in @thm-dual-p-norm is unique: if \( \y \ne \0 \), \( \norm{\x}_p \le 1 \) and \( \inner{\x}{\y} = \norm{\y}_q \), then \( \x \) is the vector given there.
:::

*Hint: in (a), look at where the proof of @thm-holder adds up the inequalities of @lem-young.*
::::

::: {.solution}
(a) Put \( a_i = \lvert x_i\rvert/\norm{\x}_p \) and \( b_i = \lvert y_i\rvert/\norm{\y}_q \), as in the proof of @thm-holder, so that \( \sum_ia_i^p = \sum_ib_i^q = 1 \). Dividing by \( \norm{\x}_p\norm{\y}_q > 0 \), the equality \( \sum_i\lvert x_iy_i\rvert = \norm{\x}_p\norm{\y}_q \) says \( \sum_ia_ib_i = 1 = \sum_i(a_i^p/p + b_i^q/q) \). By @lem-young, \( a_ib_i \le a_i^p/p + b_i^q/q \) for each \( i \). A sum of non-negative differences \( (a_i^p/p + b_i^q/q) - a_ib_i \) is \( 0 \) exactly when each difference is \( 0 \), so equality holds exactly when \( a_ib_i = a_i^p/p + b_i^q/q \) for every \( i \), that is, by the equality case of @lem-young, when \( a_i^p = b_i^q \) for every \( i \). By the rule \( (a/b)^p = a^p/b^p \) for real powers, \( a_i^p = \lvert x_i\rvert^p/\norm{\x}_p^p \) and \( b_i^q = \lvert y_i\rvert^q/\norm{\y}_q^q \).

(b) Let \( \y \ne \0 \), \( \norm{\x}_p \le 1 \) and \( \inner{\x}{\y} = \norm{\y}_q \). By @thm-holder,
\[
\norm{\y}_q = \inner{\x}{\y} \le \sum_i\lvert x_iy_i\rvert \le \norm{\x}_p\norm{\y}_q \le \norm{\y}_q ,
\]
so every inequality is an equality. First, \( \norm{\x}_p = 1 \), since \( \norm{\y}_q > 0 \); in particular \( \x \ne \0 \). Second, \( \sum_ix_iy_i = \sum_i\lvert x_iy_i\rvert \), and since \( x_iy_i \le \lvert x_iy_i\rvert \) for each \( i \), every \( x_iy_i \ge 0 \). Third, by (a), \( \lvert x_i\rvert^p = \lvert y_i\rvert^q/\norm{\y}_q^q \) for every \( i \). Raising to the power \( 1/p \) and using \( q/p = q - 1 \), which follows from \( \frac1p + \frac1q = 1 \), gives \( \lvert x_i\rvert = \lvert y_i\rvert^{q-1}/\norm{\y}_q^{q-1} \). If \( y_i = 0 \), then \( x_i = 0 \), as in the formula. If \( y_i \ne 0 \), then \( x_i \ne 0 \) and \( x_iy_i \ge 0 \), so \( x_i \) has the sign \( \sigma_i \) of \( y_i \). Hence \( x_i = \sigma_i\lvert y_i\rvert^{q-1}/\norm{\y}_q^{q-1} \) for every \( i \), which is the vector of @thm-dual-p-norm.
:::
