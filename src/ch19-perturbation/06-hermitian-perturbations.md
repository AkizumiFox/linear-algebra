# Hermitian Perturbations

For Hermitian matrices, Chapter 16 already gave the basic perturbation bound: each eigenvalue moves by at most \( \norm{\E}_2 \), and no smaller constant is possible. This section asks what that bound does **not** tell us, and answers two such questions. The first is practical. A computation rarely hands us \( \E \); it hands us an approximate eigenvector, and the question is how good the eigenvalue estimate it yields is. The answer is a residual bound, and when the eigenvalue is separated from the others it improves from linear to **quadratic** in the residual; that is the Kato–Temple theorem. The second concerns small eigenvalues. An absolute bound of size \( \norm{\E}_2 \) says nothing about an eigenvalue much smaller than \( \norm{\E}_2 \), and for perturbations of the form \( \A \mapsto \S\A\S^{*} \) we prove a **relative** bound instead, Ostrowski's theorem, which is Sylvester's law of inertia made quantitative.

Throughout, \( F = \nC \), matrices whose eigenvalues are ordered are Hermitian, and \( \lambda_1(\A) \ge \dots \ge \lambda_n(\A) \) are the eigenvalues of \( \A \) in decreasing order, with multiplicity. Vectors are measured in \( \norm{\cdot}_2 \), written \( \norm{\cdot} \) when no other norm is in sight, and \( \inner{\x}{\y} = \y^{*}\x \).

## What Weyl's bound leaves open

Recall @cor-weyl-perturbation: if \( \A \) and \( \E \) are Hermitian, then \( \lvert\lambda_i(\A + \E) - \lambda_i(\A)\rvert \le \norm{\E}_2 \) for every \( i \). By @cor-hermitian-eigenvalues-well-conditioned the constant \( 1 \) cannot be lowered, since \( \E = t\I \) moves every eigenvalue by exactly \( t = \norm{\E}_2 \). As a bound on **absolute** error, for an **unknown** Hermitian perturbation of known size, there is nothing more to be said.

The two assumptions in bold are where there is room. First, in practice \( \E \) is not known at all. An iterative method stops with a unit vector \( \x \) and a number \( \mu \) that it believes to be an eigenpair, and what can be measured is the **residual** \( \r = \A\x - \mu\x \). Second, an absolute error bound is only informative for eigenvalues larger than the error. For the matrix \( \diag(1, 10^{-6}) \) and a Hermitian perturbation of size \( 10^{-2} \), Weyl's bound allows the eigenvalue \( 10^{-6} \) to end up anywhere in an interval of radius \( 10^{-2} \), including negative numbers. Whether that is a fair description depends on the kind of perturbation, and for an important kind it is not.

## Residual bounds

Suppose \( \x \) is a unit vector and \( \mu \) a real number, and \( \r = \A\x - \mu\x \) is small. If \( \r = \0 \), then \( \mu \) is an eigenvalue. The next theorem says that if \( \r \) is merely small, \( \mu \) is **near** an eigenvalue, with the size of \( \r \) as the distance.

::: {#thm-hermitian-residual-bound}
[Residual Bound for Hermitian Matrices]

Let \( \A \in M_n(\nC) \) be Hermitian, let \( \x \in \nC^n \) with \( \norm{\x} = 1 \), let \( \mu \in \nR \), and put \( \r = \A\x - \mu\x \). Then some eigenvalue \( \lambda \) of \( \A \) satisfies \( \lvert\lambda - \mu\rvert \le \norm{\r} \); that is, the interval \( [\mu - \norm{\r}, \mu + \norm{\r}] \) contains an eigenvalue of \( \A \).
:::

This is the normal case of §04's @thm-residual-bound, since a Hermitian matrix is normal. We give the direct proof from the spectral theorem instead, because the expansion it uses is the one Kato–Temple needs.

::: {.proof}
By @cor-spectral-complex-matrix there is an orthonormal basis \( (\q_1, \dots, \q_n) \) of \( \nC^n \) with \( \A\q_i = \lambda_i\q_i \), where \( \lambda_i = \lambda_i(\A) \). Write \( \x = \sum_i c_i\q_i \), with \( \sum_i\lvert c_i\rvert^2 = \norm{\x}^2 = 1 \) by @thm-orthonormal-coordinates (c). Then \( \r = \sum_i c_i(\lambda_i - \mu)\q_i \), and by the same result
\[
\norm{\r}^2 = \sum_{i=1}^{n}\lvert c_i\rvert^2(\lambda_i - \mu)^2 \ \ge\ \Bigl(\min_i(\lambda_i - \mu)^2\Bigr)\sum_{i=1}^{n}\lvert c_i\rvert^2 = \min_i(\lambda_i - \mu)^2 .
\]
Taking square roots, \( \min_i\lvert\lambda_i - \mu\rvert \le \norm{\r} \), as claimed.
:::

The bound holds for every real \( \mu \), and one choice of \( \mu \) makes the residual smallest: the **Rayleigh quotient** \( R_{\A}(\x) = \x^{*}\A\x \) of @def-rayleigh-quotient, which for a unit vector needs no denominator. With that choice the residual is orthogonal to \( \x \), since
\[
\inner{\r}{\x} = \x^{*}\A\x - \mu\,\x^{*}\x = \mu - \mu = 0 ,
\]
and Pythagoras (@thm-pythagoras) applied to \( \A\x = \mu\x + \r \) gives
\[
\norm{\r}^2 = \norm{\A\x}^2 - \mu^2 \qquad \bigl(\mu = R_{\A}(\x),\ \norm{\x} = 1\bigr) .
\]{#eq-rayleigh-residual}
Exercise B3 shows that any other \( \mu \) gives a larger residual. From now on, \( \mu \) is the Rayleigh quotient and \( \varepsilon = \norm{\A\x - \mu\x} \) its residual.

::: {.check}
Let \( \A = \diag(1, 3) \) and \( \x = \tfrac{1}{\sqrt2}(1, 1) \). Compute \( \mu = R_{\A}(\x) \), the residual \( \r \) and \( \varepsilon = \norm{\r} \). Which eigenvalues does the interval \( [\mu - \varepsilon, \mu + \varepsilon] \) contain?
:::

::: {.solution}
\( \A\x = \tfrac{1}{\sqrt2}(1, 3) \), so \( \mu = \x^{*}\A\x = \tfrac12(1 + 3) = 2 \) and \( \r = \tfrac{1}{\sqrt2}(1 - 2, 3 - 2) = \tfrac{1}{\sqrt2}(-1, 1) \), with \( \varepsilon = 1 \). As a check, @eq-rayleigh-residual gives \( \norm{\A\x}^2 - \mu^2 = 5 - 4 = 1 \). The interval is \( [1, 3] \), and it contains both eigenvalues, at its two ends. The bound is attained: a vector halfway between two eigenvectors is as bad an approximation as it can be.
:::

## The Kato–Temple bound

The residual bound is linear in \( \varepsilon \), and in general no better is possible: in the Quick check, \( \lvert\lambda - \mu\rvert = \varepsilon \) for both eigenvalues. But that example had \( \x \) equally far from both eigenvectors. When \( \x \) is close to one eigenvector, the Rayleigh quotient is a much better estimate than \( \varepsilon \) suggests. @exr-rayleigh-quotient-c1 of Chapter 16 found that an eigenvector error of size \( \delta \) costs only about \( \delta^2 \) in the Rayleigh quotient. The trouble is that the eigenvector error cannot be measured, while the residual can. The next theorem restates the \( \delta^2 \) phenomenon in terms of the residual, and the price is a hypothesis on how far the other eigenvalues are.

Here is where the gap comes in. If no eigenvalue of \( \A \) lies strictly between two real numbers \( \lambda \) and \( \beta \), then \( (t - \lambda)(t - \beta) \ge 0 \) at every eigenvalue \( t \), so the matrix \( (\A - \lambda\I)(\A - \beta\I) \) is positive semidefinite. Evaluating its quadratic form at \( \x \) gives an inequality that involves only \( \mu \), \( \varepsilon \), \( \lambda \) and \( \beta \).

::: {#thm-kato-temple}
[Kato–Temple Theorem]

Let \( \A \in M_n(\nC) \) be Hermitian, let \( \x \in \nC^n \) with \( \norm{\x} = 1 \), let \( \mu = \x^{*}\A\x \), and let \( \varepsilon = \norm{\A\x - \mu\x} \).

::: {.enumerate options="label=(\alph*)"}
1. Let \( \beta > \mu \), and let \( \lambda < \beta \) be an eigenvalue of \( \A \) such that **no** eigenvalue of \( \A \) lies in the open interval \( (\lambda, \beta) \). Then
   \[
   \lambda \ \ge\ \mu - \frac{\varepsilon^2}{\beta - \mu} .
   \]
2. Let \( \alpha < \mu \), and let \( \lambda > \alpha \) be an eigenvalue of \( \A \) such that **no** eigenvalue of \( \A \) lies in the open interval \( (\alpha, \lambda) \). Then
   \[
   \lambda \ \le\ \mu + \frac{\varepsilon^2}{\mu - \alpha} .
   \]
:::

In particular, if \( \alpha < \mu < \beta \) and \( \lambda \) is the **only** eigenvalue of \( \A \) in \( (\alpha, \beta) \), then
\[
\mu - \frac{\varepsilon^2}{\beta - \mu} \ \le\ \lambda \ \le\ \mu + \frac{\varepsilon^2}{\mu - \alpha} .
\]
:::

::: {.idea}
Compute the number \( \x^{*}(\A - \lambda\I)(\A - \beta\I)\x \) two ways. ① In the eigenbasis it is \( \sum_i\lvert c_i\rvert^2(\lambda_i - \lambda)(\lambda_i - \beta) \), and the gap hypothesis makes every term non-negative: each eigenvalue lies on or outside the interval between \( \lambda \) and \( \beta \). ② Expanding the product, it is \( \norm{\A\x}^2 - (\lambda + \beta)\mu + \lambda\beta \), and @eq-rayleigh-residual turns this into \( \varepsilon^2 + (\mu - \lambda)(\mu - \beta) \). So \( (\mu - \lambda)(\beta - \mu) \le \varepsilon^2 \); divide by the positive number \( \beta - \mu \). Part (b) is the same with \( \alpha \) in place of \( \beta \).
:::

::: {.proof}
(a) As in the proof of @thm-hermitian-residual-bound, write \( \x = \sum_i c_i\q_i \) in an orthonormal eigenbasis, \( \A\q_i = \lambda_i\q_i \), \( \sum_i\lvert c_i\rvert^2 = 1 \). Then \( (\A - \lambda\I)(\A - \beta\I)\x = \sum_i c_i(\lambda_i - \lambda)(\lambda_i - \beta)\q_i \), and by @thm-orthonormal-coordinates (b),
\[
\x^{*}(\A - \lambda\I)(\A - \beta\I)\x = \sum_{i=1}^{n}\lvert c_i\rvert^2(\lambda_i - \lambda)(\lambda_i - \beta) .
\]
Each eigenvalue \( \lambda_i \) satisfies \( \lambda_i \le \lambda \) or \( \lambda_i \ge \beta \), because none lies in \( (\lambda, \beta) \). In the first case both factors are \( \le 0 \), in the second both are \( \ge 0 \), since \( \lambda < \beta \). So every term is \( \ge 0 \), and the left-hand side is \( \ge 0 \).

On the other hand, expanding the product and using \( \x^{*}\x = 1 \), \( \x^{*}\A\x = \mu \) and \( \x^{*}\A^2\x = (\A\x)^{*}(\A\x) = \norm{\A\x}^2 \), where \( \A^{*} = \A \),
\[
\begin{aligned}
\x^{*}(\A - \lambda\I)(\A - \beta\I)\x
&= \norm{\A\x}^2 - (\lambda + \beta)\mu + \lambda\beta \\
&= \varepsilon^2 + \mu^2 - (\lambda + \beta)\mu + \lambda\beta \\
&= \varepsilon^2 + (\mu - \lambda)(\mu - \beta) ,
\end{aligned}
\]
where the second line is @eq-rayleigh-residual. Hence \( \varepsilon^2 + (\mu - \lambda)(\mu - \beta) \ge 0 \), that is, \( (\mu - \lambda)(\beta - \mu) \le \varepsilon^2 \). Since \( \beta - \mu > 0 \), dividing gives \( \mu - \lambda \le \varepsilon^2/(\beta - \mu) \), which is (a).

(b) Apply (a) to \( -\A \), the unit vector \( \x \), the eigenvalue \( -\lambda \) and the number \( -\alpha \). The Rayleigh quotient of \( -\A \) at \( \x \) is \( -\mu \), its residual is \( -(\A\x - \mu\x) \), of the same norm \( \varepsilon \), and \( -\alpha > -\mu \). The eigenvalues of \( -\A \) are the negatives of those of \( \A \), so \( -\lambda < -\alpha \) and none lies in \( (-\lambda, -\alpha) \). Part (a) gives \( -\lambda \ge -\mu - \varepsilon^2/(-\alpha + \mu) \), which is (b).

The final statement follows: if \( \lambda \) is the only eigenvalue in \( (\alpha, \beta) \), then no eigenvalue lies in \( (\lambda, \beta) \) or in \( (\alpha, \lambda) \), so (a) and (b) both apply. This proves the theorem.
:::

Compare the two bounds on the error \( \lvert\lambda - \mu\rvert \). The residual bound gives \( \varepsilon \). Kato–Temple gives \( \varepsilon^2 \) divided by the distance from \( \mu \) to the neighboring part of the spectrum. When \( \varepsilon \) is small compared with that gap, the square wins by a wide margin: a residual of \( 10^{-4} \) and a gap of \( 1 \) give an error of at most \( 10^{-8} \). *The Rayleigh quotient's error is quadratic in the residual, provided there is a gap.* That is the reason the Rayleigh quotient is the eigenvalue estimate of choice, and Chapter 23 builds an iteration on it.

The theorem needs a number \( \alpha \) or \( \beta \) that is known to lie beyond the neighboring eigenvalue, and in practice that information has to come from somewhere. The next example gets it from interlacing.

::: {#exm-kato-temple-tridiagonal}
[Bracketing the top eigenvalue]

Let
\[
\A = \begin{pmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2 \end{pmatrix} , \qquad \x = \tfrac{1}{\sqrt3}(1, 1, 1) .
\]
Estimate \( \lambda_1(\A) \) from \( \x \): compute \( \mu \) and \( \varepsilon \), the interval given by @thm-hermitian-residual-bound, and the interval given by @thm-kato-temple, using only information that can be read off \( \A \) without computing its eigenvalues. Compare with the true value \( \lambda_1(\A) = 2 + \sqrt2 \).
:::

::: {.solution}
*Rayleigh quotient and residual.* \( \A(1, 1, 1) = (3, 4, 3) \), so \( \A\x = \tfrac{1}{\sqrt3}(3, 4, 3) \) and
\[
\mu = \x^{*}\A\x = \tfrac13(3 + 4 + 3) = \tfrac{10}{3} , \qquad
\norm{\A\x}^2 = \tfrac13(9 + 16 + 9) = \tfrac{34}{3} .
\]
By @eq-rayleigh-residual, \( \varepsilon^2 = \tfrac{34}{3} - \tfrac{100}{9} = \tfrac{2}{9} \), so \( \varepsilon = \tfrac{\sqrt2}{3} \approx 0.471 \). Directly: \( \r = \tfrac{1}{\sqrt3}\bigl(3 - \tfrac{10}{3}, 4 - \tfrac{10}{3}, 3 - \tfrac{10}{3}\bigr) = \tfrac{1}{3\sqrt3}(-1, 2, -1) \), of squared norm \( \tfrac{6}{27} = \tfrac29 \).

*Residual bound.* Some eigenvalue lies in \( [\tfrac{10}{3} - 0.471, \tfrac{10}{3} + 0.471] \approx [2.862, 3.805] \).

*Kato–Temple.* By @prp-rayleigh-basic, \( \lambda_1(\A) \ge \mu = \tfrac{10}{3} \). For an upper bound we need \( \alpha < \mu \) with no eigenvalue in \( (\alpha, \lambda_1) \), which says \( \lambda_2(\A) \le \alpha \). Deleting the second row and column leaves \( \B = \diag(2, 2) \), and Cauchy's interlacing theorem (@thm-cauchy-interlacing, with \( I = \{1, 3\} \)) gives \( \lambda_2(\A) \le \lambda_1(\B) = 2 \). So \( \alpha = 2 \) is allowed: \( \alpha < \mu \), and no eigenvalue lies in \( (2, \lambda_1) \), because \( \lambda_2 \le 2 \) and \( \lambda_1 \ge \tfrac{10}{3} > 2 \). Part (b) gives
\[
\lambda_1(\A) \ \le\ \frac{10}{3} + \frac{2/9}{10/3 - 2} = \frac{10}{3} + \frac{2}{9}\cdot\frac{3}{4} = \frac{10}{3} + \frac16 = \frac72 .
\]
So \( \tfrac{10}{3} \le \lambda_1(\A) \le \tfrac72 \), an interval of width \( \tfrac16 \approx 0.167 \), against width \( 2\varepsilon \approx 0.943 \) for the residual bound.

*Check.* The true value is \( 2 + \sqrt2 \approx 3.414 \), which lies in both intervals; the other eigenvalues are \( 2 \) and \( 2 - \sqrt2 \). The actual error of the Rayleigh quotient is \( 2 + \sqrt2 - \tfrac{10}{3} \approx 0.081 \), about a sixth of \( \varepsilon \).
:::

Kato–Temple cannot be improved in general: for \( \A = \diag(\lambda_1, \lambda_2) \) with \( \lambda_1 > \lambda_2 \), and \( \alpha = \lambda_2 \) the other eigenvalue, the upper bound in (b) is an **equality** at every real unit \( \x \) that is not an eigenvector for \( \lambda_2 \) (Exercise C3). At such an eigenvector the hypothesis \( \alpha < \mu \) fails, since there \( \mu = \lambda_2 \).

::: {.warning}
**The gap hypothesis is not decoration.** Take \( \A = \diag(1, 0) \) and \( \x = \tfrac{1}{\sqrt2}(1, 1) \), so \( \mu = \tfrac12 \) and \( \r = \tfrac{1}{\sqrt2}(\tfrac12, -\tfrac12) \), \( \varepsilon^2 = \tfrac14 \). With \( \lambda = 1 \) and \( \alpha = 0 \), part (b) gives \( 1 \le \tfrac12 + \tfrac{1/4}{1/2} = 1 \), true with equality. With \( \alpha = -\tfrac12 \) instead, the eigenvalue \( 0 \) lies in \( (\alpha, \lambda) \), the hypothesis fails, and the formula would claim \( 1 \le \tfrac12 + \tfrac{1/4}{1} = \tfrac34 \), which is false. A number \( \alpha \) chosen too far from \( \mu \), past an unseen eigenvalue, gives a bound that is simply wrong.
:::

## Relative perturbations and congruence

Now the second question: small eigenvalues. Weyl's bound is absolute, and an absolute bound is useless for an eigenvalue smaller than itself. Some perturbations deserve better. In a change of variables \( \x = \S^{*}\y \) with \( \S \) invertible, the quadratic form \( \x^{*}\A\x \) becomes \( \y^{*}(\S\A\S^{*})\y \); the matrix undergoes a **congruence**, as in Chapter 13 and in Chapter 16 §10. When \( \S \) is close to \( \I \), for instance when it comes from a slightly inaccurate elimination step or from rounding in a factor, \( \S\A\S^{*} \) is a perturbation of \( \A \), but a very structured one. Its effect on the eigenvalues is **multiplicative**.

Two facts are known already. By @thm-inertia-second-proof (b), applied with \( \P = \S^{*} \), a congruence preserves the numbers of positive, negative and zero eigenvalues; it cannot change a sign. And by Chapter 13 §05's warning, it can still move eigenvalues a long way: with \( \P = \diag(2, 3) \), \( \P\tp\diag(1, -1)\P = \diag(4, -9) \). Ostrowski's theorem measures how far.

::: {#thm-ostrowski-relative}
[Ostrowski's Theorem]

Let \( \A \in M_n(\nC) \) be Hermitian and let \( \S \in M_n(\nC) \) be invertible. Then \( \S\S^{*} \) is positive definite, and for each \( k = 1, \dots, n \) there is a real number \( \theta_k \) with
\[
\lambda_k(\S\A\S^{*}) = \theta_k\,\lambda_k(\A) , \qquad
\lambda_n(\S\S^{*}) \ \le\ \theta_k \ \le\ \lambda_1(\S\S^{*}) .
\]
In particular \( \theta_k > 0 \), and
\[
\bigl\lvert\lambda_k(\S\A\S^{*}) - \lambda_k(\A)\bigr\rvert \ \le\ \norm{\S\S^{*} - \I}_2\,\lvert\lambda_k(\A)\rvert .
\]
:::

::: {.idea}
**Step roadmap.** Fix \( k \) and put \( \mu = \lambda_k(\A) \).

① **Shift, so the \( k \)-th eigenvalue is \( 0 \).** \( \A - \mu\I \) has at most \( k - 1 \) positive eigenvalues and at least \( k \) non-negative ones. A congruence preserves both counts (Sylvester's law), so \( \S(\A - \mu\I)\S^{*} \) has the same property, and that forces its \( k \)-th eigenvalue to be exactly \( 0 \).

② **Split.** \( \S\A\S^{*} = \S(\A - \mu\I)\S^{*} + \mu\S\S^{*} \).

③ **Weyl.** Adding \( \mu\S\S^{*} \) moves the \( k \)-th eigenvalue from \( 0 \) to somewhere between the smallest and the largest eigenvalue of \( \mu\S\S^{*} \), which are \( \mu\lambda_n(\S\S^{*}) \) and \( \mu\lambda_1(\S\S^{*}) \) in some order, depending on the sign of \( \mu \).
:::

::: {.proof}
For \( \x \ne \0 \), \( \x^{*}\S\S^{*}\x = \norm{\S^{*}\x}^2 > 0 \), because \( \S^{*} \) is invertible. So \( \S\S^{*} \), which is Hermitian, is positive definite, and its eigenvalues are positive by @thm-pd-characterizations; write \( m = \lambda_n(\S\S^{*}) > 0 \) and \( M = \lambda_1(\S\S^{*}) \).

Fix \( k \) and put \( \mu = \lambda_k(\A) \). The eigenvalues of the Hermitian matrix \( \A - \mu\I \) are \( \lambda_i(\A) - \mu \), in the same decreasing order. Those with \( i \ge k \) are \( \le 0 \), so at most \( k - 1 \) of them are positive; those with \( i \le k \) are \( \ge 0 \), so at least \( k \) are non-negative. In the notation of @def-inertia-triple, \( n_+(\A - \mu\I) \le k - 1 \) and \( n_+(\A - \mu\I) + n_0(\A - \mu\I) \ge k \). Put \( \Y = \S(\A - \mu\I)\S^{*} \). This is \( \P^{*}(\A - \mu\I)\P \) with \( \P = \S^{*} \) invertible, so by @thm-inertia-second-proof (b), \( \Y \) is Hermitian with the same inertia triple. Hence \( \Y \) has at most \( k - 1 \) positive eigenvalues, so \( \lambda_k(\Y) \le 0 \); and at least \( k \) non-negative ones, so \( \lambda_k(\Y) \ge 0 \). Thus \( \lambda_k(\Y) = 0 \).

Now \( \S\A\S^{*} = \Y + \mu\S\S^{*} \), a sum of two Hermitian matrices. By @cor-weyl-monotone,
\[
\lambda_n(\mu\S\S^{*}) \ \le\ \lambda_k(\S\A\S^{*}) - \lambda_k(\Y) \ \le\ \lambda_1(\mu\S\S^{*}) ,
\]
and \( \lambda_k(\Y) = 0 \). If \( \mu \ge 0 \), multiplying by \( \mu \) keeps the order of the eigenvalues, so \( \lambda_n(\mu\S\S^{*}) = \mu m \) and \( \lambda_1(\mu\S\S^{*}) = \mu M \). If \( \mu < 0 \), then \( \mu\S\S^{*} = -(\lvert\mu\rvert\S\S^{*}) \), and by @lem-eigenvalues-of-negation its extreme eigenvalues are \( \lambda_n = -\lvert\mu\rvert M = \mu M \) and \( \lambda_1 = -\lvert\mu\rvert m = \mu m \). In both cases \( \lambda_k(\S\A\S^{*}) \) lies between \( \mu m \) and \( \mu M \). If \( \mu \ne 0 \), put \( \theta_k = \lambda_k(\S\A\S^{*})/\mu \); dividing by \( \mu \) (and reversing the inequalities when \( \mu < 0 \)) gives \( m \le \theta_k \le M \). If \( \mu = 0 \), both ends are \( 0 \), so \( \lambda_k(\S\A\S^{*}) = 0 \), and \( \theta_k = m \) will do. In either case \( \theta_k \ge m > 0 \).

For the last inequality, \( \lvert\lambda_k(\S\A\S^{*}) - \lambda_k(\A)\rvert = \lvert\theta_k - 1\rvert\,\lvert\mu\rvert \), and \( \theta_k - 1 \) lies in \( [m - 1, M - 1] \). The numbers \( m - 1 \) and \( M - 1 \) are the smallest and largest eigenvalues of the Hermitian matrix \( \S\S^{*} - \I \), so by @lem-hermitian-spectral-norm both have absolute value at most \( \norm{\S\S^{*} - \I}_2 \), and so does everything between them. This proves the theorem.
:::

This is a quantitative Sylvester's law of inertia. Sylvester's law says that a congruence cannot change the sign of an eigenvalue; Ostrowski's theorem says that it multiplies the \( k \)-th eigenvalue by a factor \( \theta_k \) that is always positive and always between the extreme eigenvalues of \( \S\S^{*} \). These are \( \lambda_1(\S\S^{*}) = \max_{\norm{\y} = 1}\norm{\S^{*}\y}^2 \) and \( \lambda_n(\S\S^{*}) = \min_{\norm{\y} = 1}\norm{\S^{*}\y}^2 \), by @prp-rayleigh-basic, since \( \y^{*}\S\S^{*}\y = \norm{\S^{*}\y}^2 \): the most and the least that the change of variables stretches a vector, squared. When \( \S \) is close to a unitary matrix, both are close to \( 1 \), and **every** eigenvalue, however small, keeps most of its significant digits.

::: {.check}
Chapter 13 §05's warning used \( \A = \diag(1, -1) \) and \( \P = \diag(2, 3) \), with \( \P\tp\A\P = \diag(4, -9) \). Take \( \S = \P\tp = \P \). Find \( \theta_1 \), \( \theta_2 \) and the interval \( [\lambda_n(\S\S^{*}), \lambda_1(\S\S^{*})] \). Can the interval in @thm-ostrowski-relative be shortened?
:::

::: {.solution}
\( \S\S^{*} = \diag(4, 9) \), so the interval is \( [4, 9] \). The eigenvalues of \( \S\A\S^{*} = \diag(4, -9) \) in decreasing order are \( 4 \) and \( -9 \), and those of \( \A \) are \( 1 \) and \( -1 \). So \( \theta_1 = 4/1 = 4 \) and \( \theta_2 = -9/(-1) = 9 \). They sit at the two ends of the interval, so neither end can be moved inwards: the interval is sharp.
:::

The next example shows the difference between the absolute and the relative view on a matrix whose eigenvalues differ greatly in size.

::: {#exm-ostrowski-graded}
[A tiny eigenvalue under a change of variables]

Let \( \A = \diag(1, 10^{-6}) \) and \( \S = \begin{psmallmatrix} 1 & 0 \\ t & 1 \end{psmallmatrix} \) with \( t = 10^{-2} \), the change of variables that adds \( t \) times the first coordinate to the second. Compute \( \S\A\S^{*} \) and \( \E = \S\A\S^{*} - \A \). What do @cor-weyl-monotone and @thm-ostrowski-relative say about \( \lambda_2(\S\A\S^{*}) \), and what is its true value?
:::

::: {.solution}
Write \( \eta = 10^{-6} \). Multiplying out,
\[
\S\A\S^{*} = \begin{pmatrix} 1 & t \\ t & t^2 + \eta \end{pmatrix} , \qquad
\E = \begin{pmatrix} 0 & t \\ t & t^2 \end{pmatrix} ,
\]
with \( t^2 + \eta = 1.01 \times 10^{-4} \).

*Weyl.* \( \E \) has trace \( t^2 \) and determinant \( -t^2 \), so its eigenvalues are \( \tfrac12\bigl(t^2 \pm t\sqrt{t^2 + 4}\bigr) \), approximately \( 0.01005 \) and \( -0.00995 \). By @cor-weyl-monotone,
\[
10^{-6} - 0.00995 \ \le\ \lambda_2(\S\A\S^{*}) \ \le\ 10^{-6} + 0.01005 .
\]
This interval is about \( 10^4 \) times wider than the eigenvalue it is meant to locate, and it contains negative numbers.

*Ostrowski.* \( \S\S^{*} = \begin{psmallmatrix} 1 & t \\ t & 1 + t^2 \end{psmallmatrix} \) has trace \( 2 + t^2 \) and determinant \( 1 \), so its eigenvalues are \( \tfrac12\bigl(2 + t^2 \pm t\sqrt{4 + t^2}\bigr) \), approximately \( 1.01005 \) and \( 0.99005 \). By @thm-ostrowski-relative,
\[
0.99005 \times 10^{-6} \ \le\ \lambda_2(\S\A\S^{*}) \ \le\ 1.01005 \times 10^{-6} :
\]
the eigenvalue is positive and known to within about \( 1\% \).

*The truth.* \( \det(\S\A\S^{*}) = \det(\S)^2\det\A = \eta \), since \( \det\S = 1 \), and the trace is \( 1 + t^2 + \eta \). So the two eigenvalues multiply to \( \eta \), and the larger is \( 1.0001\ldots \); hence \( \lambda_2(\S\A\S^{*}) = \eta/\lambda_1(\S\A\S^{*}) \approx 0.99990 \times 10^{-6} \). The relative change is about \( 10^{-4} \), well inside Ostrowski's \( 1\% \); Weyl's bound, by contrast, cannot even decide the sign.
:::

::: {.warning}
**Weyl's bound is sharp and still useless for small eigenvalues.** It is the best possible bound on **absolute** error for **arbitrary** Hermitian \( \E \) of a given norm, and for exactly that reason it cannot distinguish an eigenvalue of size \( 10^{-6} \) from \( 0 \) once \( \norm{\E}_2 \ge 10^{-6} \). A general Hermitian \( \E \) really can destroy a small eigenvalue: \( \E = -10^{-6}\e_2\e_2\tp \) sends the eigenvalue \( 10^{-6} \) of \( \diag(1, 10^{-6}) \) to \( 0 \). Relative accuracy needs a structured perturbation, such as a congruence \( \S\A\S^{*} \) with \( \S \) near \( \I \).
:::

## Exercises

### A. Check your understanding

:::: {#exr-hermitian-perturbations-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the Kato–Temple theorem, with its hypotheses.
2. True or false: for Hermitian \( \A \), a unit vector \( \x \) and real \( \mu \), the eigenvalue of \( \A \) **closest** to \( \mu \) is within \( \norm{\A\x - \mu\x} \) of \( \mu \). Justify your answer.
3. True or false: for Hermitian \( \A \) and invertible \( \S \), \( \lambda_k(\S\A\S^{*}) \) and \( \lambda_k(\A) \) have the same sign for every \( k \). Justify your answer.
4. Which of the three bounds of this section need information that is not contained in \( \A \), \( \x \) and \( \mu \)? What information?
5. Why can the constant \( 1 \) in @cor-weyl-perturbation not be lowered, and why does that not contradict Ostrowski's theorem?
:::
::::

::: {.solution}
(a) Let \( \A \) be Hermitian, \( \x \) a unit vector, \( \mu = \x^{*}\A\x \), \( \varepsilon = \norm{\A\x - \mu\x} \). If \( \beta > \mu \) and \( \lambda < \beta \) is an eigenvalue with no eigenvalue in \( (\lambda, \beta) \), then \( \lambda \ge \mu - \varepsilon^2/(\beta - \mu) \). If \( \alpha < \mu \) and \( \lambda > \alpha \) is an eigenvalue with no eigenvalue in \( (\alpha, \lambda) \), then \( \lambda \le \mu + \varepsilon^2/(\mu - \alpha) \).

(b) True. @thm-hermitian-residual-bound gives some eigenvalue within \( \norm{\A\x - \mu\x} \) of \( \mu \), and the closest one is at least as close.

(c) True. By @thm-ostrowski-relative, \( \lambda_k(\S\A\S^{*}) = \theta_k\lambda_k(\A) \) with \( \theta_k > 0 \); a positive multiple has the same sign, and \( 0 \) goes to \( 0 \).

(d) The residual bound needs nothing more. Kato–Temple needs a number \( \alpha \) or \( \beta \) beyond the neighboring eigenvalue, that is, a lower bound on the gap; in @exm-kato-temple-tridiagonal it came from interlacing. Ostrowski's theorem is not about an approximate eigenvector, but it needs \( \S \), or at least the extreme eigenvalues of \( \S\S^{*} \).

(e) \( \E = t\I \) moves every eigenvalue by exactly \( t = \norm{\E}_2 \). Ostrowski's theorem is about the perturbations \( \S\A\S^{*} - \A \), which form a special class; \( \A + t\I \) is not of the form \( \S\A\S^{*} \) in general (for \( \A = \0 \) it never is, when \( t \ne 0 \)). A better bound for a smaller class contradicts nothing.
:::

### B. Practice

:::: {#exr-hermitian-perturbations-b1}
[B1: Three bounds for one estimate]

Let \( \A = \begin{psmallmatrix} 5 & 2 \\ 2 & 2 \end{psmallmatrix} \) and \( \x = \tfrac{1}{\sqrt{10}}(3, 1) \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \mu = \x^{*}\A\x \) and \( \varepsilon = \norm{\A\x - \mu\x} \), and the interval given by @thm-hermitian-residual-bound.
2. Using @thm-cauchy-interlacing to bound \( \lambda_2(\A) \), apply @thm-kato-temple to bracket \( \lambda_1(\A) \).
3. Find the eigenvalues of \( \A \) exactly. Hence compare the actual error of \( \mu \) with \( \varepsilon \) and with the Kato–Temple bound.
:::
::::

::: {.solution}
(a) \( \A(3, 1) = (17, 8) \), so \( \mu = \tfrac{1}{10}(3 \cdot 17 + 1 \cdot 8) = \tfrac{59}{10} = 5.9 \). The residual is \( \tfrac{1}{\sqrt{10}}\bigl((17, 8) - 5.9(3, 1)\bigr) = \tfrac{1}{\sqrt{10}}(-0.7, 2.1) \), so \( \varepsilon^2 = \tfrac{1}{10}(0.49 + 4.41) = 0.49 \) and \( \varepsilon = 0.7 \). Some eigenvalue lies in \( [5.2, 6.6] \).

(b) Deleting the first row and column leaves \( (2) \), so @thm-cauchy-interlacing gives \( \lambda_2(\A) \le 2 \). Also \( \lambda_1(\A) \ge \mu = 5.9 \) by @prp-rayleigh-basic. So with \( \alpha = 2 < \mu \), no eigenvalue lies in \( (2, \lambda_1) \), and part (b) of @thm-kato-temple gives
\[
\lambda_1(\A) \ \le\ 5.9 + \frac{0.49}{5.9 - 2} = 5.9 + \frac{0.49}{3.9} \approx 6.026 .
\]
Hence \( 5.9 \le \lambda_1(\A) \le 6.026 \).

(c) \( \A \) has trace \( 7 \) and determinant \( 6 \), so its eigenvalues are \( 6 \) and \( 1 \); indeed \( \A(2, 1) = (12, 6) \). The actual error of \( \mu \) is \( 6 - 5.9 = 0.1 \). The residual bound allows \( 0.7 \), seven times too much; Kato–Temple allows \( 0.126 \), within about \( 26\% \) of the truth.
:::

:::: {#exr-hermitian-perturbations-b2}
[B2: Ostrowski's factors]

Let \( \A = \diag(2, -1) \) and \( \S = \begin{psmallmatrix} 1 & 1 \\ 0 & 1 \end{psmallmatrix} \). Compute \( \S\A\S^{*} \) and its eigenvalues, the eigenvalues of \( \S\S^{*} \), and the factors \( \theta_1, \theta_2 \) of @thm-ostrowski-relative. Hence verify the theorem for this pair.
::::

::: {.solution}
\( \A\S^{*} = \diag(2, -1)\begin{psmallmatrix} 1 & 0 \\ 1 & 1 \end{psmallmatrix} = \begin{psmallmatrix} 2 & 0 \\ -1 & -1 \end{psmallmatrix} \), and
\[
\S\A\S^{*} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 2 & 0 \\ -1 & -1 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ -1 & -1 \end{pmatrix} ,
\]
with trace \( 0 \) and determinant \( -2 \), so eigenvalues \( \pm\sqrt2 \). Next \( \S\S^{*} = \begin{psmallmatrix} 2 & 1 \\ 1 & 1 \end{psmallmatrix} \), with trace \( 3 \) and determinant \( 1 \), so eigenvalues \( \tfrac{3 \pm \sqrt5}{2} \approx 2.618 \) and \( 0.382 \).

Then \( \theta_1 = \lambda_1(\S\A\S^{*})/\lambda_1(\A) = \sqrt2/2 \approx 0.707 \) and \( \theta_2 = (-\sqrt2)/(-1) = \sqrt2 \approx 1.414 \). Both lie in \( [0.382, 2.618] \), as the theorem says, and both are positive, so the signs \( +, - \) are preserved.
:::

:::: {#exr-hermitian-perturbations-b3}
[B3: The Rayleigh quotient minimizes the residual]

Let \( \A \) be Hermitian and \( \x \) a unit vector, with \( \rho = \x^{*}\A\x \). Prove that for every real \( \nu \),
\[
\norm{\A\x - \nu\x}^2 = \norm{\A\x - \rho\x}^2 + (\nu - \rho)^2 .
\]
Hence deduce that among all real \( \nu \), the residual bound of @thm-hermitian-residual-bound is sharpest at \( \nu = \rho \).
::::

::: {.solution}
Write \( \A\x - \nu\x = (\A\x - \rho\x) + (\rho - \nu)\x \). The first vector is orthogonal to \( \x \), since \( \inner{\A\x - \rho\x}{\x} = \x^{*}\A\x - \rho = 0 \). By @thm-pythagoras,
\[
\norm{\A\x - \nu\x}^2 = \norm{\A\x - \rho\x}^2 + (\rho - \nu)^2\norm{\x}^2 = \norm{\A\x - \rho\x}^2 + (\nu - \rho)^2 .
\]
Hence \( \norm{\A\x - \nu\x} \ge \norm{\A\x - \rho\x} \), with equality only for \( \nu = \rho \). The interval \( [\nu - \norm{\A\x - \nu\x}, \nu + \norm{\A\x - \nu\x}] \) of @thm-hermitian-residual-bound therefore has its smallest radius at \( \nu = \rho \).
:::

### C. Going deeper

:::: {#exr-hermitian-perturbations-c1}
[C1: A residual that guarantees an eigenvalue]

Let \( \A \) be Hermitian, \( \x \) a unit vector, \( \mu = \x^{*}\A\x \) and \( \varepsilon = \norm{\A\x - \mu\x} \).

::: {.enumerate options="label=(\alph*)"}
1. Let \( \alpha < \mu < \beta \). Prove that if \( \varepsilon^2 < (\mu - \alpha)(\beta - \mu) \), then \( \A \) has an eigenvalue in \( (\alpha, \beta) \).
2. Deduce that \( \A \) has an eigenvalue in \( [\mu - \varepsilon, \mu + \varepsilon] \), which is @thm-hermitian-residual-bound again, for this choice of \( \mu \).
:::

*Hint for (a): if there is none, consider \( \x^{*}(\A - \alpha\I)(\A - \beta\I)\x \).*
::::

::: {.solution}
(a) Suppose no eigenvalue lies in \( (\alpha, \beta) \). Then every eigenvalue \( t \) satisfies \( t \le \alpha \) or \( t \ge \beta \), so \( (t - \alpha)(t - \beta) \ge 0 \). As in the proof of @thm-kato-temple, with \( \alpha \) in place of \( \lambda \),
\[
0 \ \le\ \x^{*}(\A - \alpha\I)(\A - \beta\I)\x = \varepsilon^2 + (\mu - \alpha)(\mu - \beta) ,
\]
so \( \varepsilon^2 \ge (\mu - \alpha)(\beta - \mu) \), contradicting the hypothesis. Hence some eigenvalue lies in \( (\alpha, \beta) \).

(b) Let \( d \) be the smallest distance from \( \mu \) to an eigenvalue of \( \A \), and suppose \( d > \varepsilon \). Choose \( s \) with \( \varepsilon < s < d \), and apply (a) with \( \alpha = \mu - s \) and \( \beta = \mu + s \): the hypothesis holds, since \( (\mu - \alpha)(\beta - \mu) = s^2 > \varepsilon^2 \). So some eigenvalue lies in \( (\mu - s, \mu + s) \), at distance less than \( s < d \) from \( \mu \), contradicting the choice of \( d \). Hence \( d \le \varepsilon \), which is the claim.
:::

:::: {#exr-hermitian-perturbations-c2}
[C2: Relative bounds need structured perturbations]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \A \) be Hermitian and \( \S = \I + \F \) with \( \F \in M_n(\nC) \). Prove that
\[
\bigl\lvert\lambda_k(\S\A\S^{*}) - \lambda_k(\A)\bigr\rvert \ \le\ \bigl(2\norm{\F}_2 + \norm{\F}_2^2\bigr)\,\lvert\lambda_k(\A)\rvert
\]
for every \( k \), whenever \( \S \) is invertible.
2. Show that there is **no** constant \( c \) such that \( \lvert\lambda_k(\A + \E) - \lambda_k(\A)\rvert \le c\norm{\E}_2\lvert\lambda_k(\A)\rvert \) for all Hermitian \( \A \), \( \E \) and all \( k \).
:::

*Hint for (a): expand \( \S\S^{*} - \I \), and show first that \( \norm{\F^{*}}_2 = \norm{\F}_2 \).*
::::

::: {.solution}
(a) First, \( \norm{\F^{*}}_2 \le \norm{\F}_2 \): for every \( \x \), by @thm-cauchy-schwarz and @thm-operator-norm-properties (a),
\[
\norm{\F^{*}\x}^2 = \inner{\F\F^{*}\x}{\x} \le \norm{\F\F^{*}\x}\,\norm{\x} \le \norm{\F}_2\norm{\F^{*}\x}\,\norm{\x} ,
\]
so \( \norm{\F^{*}\x} \le \norm{\F}_2\norm{\x} \) (trivially if \( \F^{*}\x = \0 \)), and the reverse inequality follows by applying this to \( \F^{*} \), since \( (\F^{*})^{*} = \F \). Now \( \S\S^{*} - \I = \F + \F^{*} + \F\F^{*} \), so by the triangle inequality for \( \norm{\cdot}_2 \), which is a norm by @thm-operator-norm-properties (b), and by part (d) of the same theorem,
\[
\norm{\S\S^{*} - \I}_2 \le \norm{\F}_2 + \norm{\F^{*}}_2 + \norm{\F}_2\norm{\F^{*}}_2 = 2\norm{\F}_2 + \norm{\F}_2^2 .
\]
The last inequality of @thm-ostrowski-relative then gives the claim.

(b) Take \( \A = \diag(1, 0) \) and \( \E = \diag(0, t) \) with \( t > 0 \). Then \( \lambda_2(\A) = 0 \) and \( \lambda_2(\A + \E) = \min(1, t) > 0 \), so the left side is positive while the right side is \( c\,t \cdot 0 = 0 \). No constant \( c \) works. By (a), such an \( \E \) is not of the form \( \S\A\S^{*} - \A \): congruence can never move the eigenvalue \( 0 \).
:::

:::: {#exr-hermitian-perturbations-c3}
[C3: Kato–Temple is sharp]

Let \( \lambda_1 > \lambda_2 \) be real, \( \A = \diag(\lambda_1, \lambda_2) \), and \( \x = (\cos\phi, \sin\phi) \) with \( 0 < \phi < \pi/2 \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \mu = \x^{*}\A\x \) and show that \( \varepsilon^2 = (\lambda_1 - \lambda_2)^2\cos^2\phi\,\sin^2\phi \).
2. Show that @thm-kato-temple (b), with \( \lambda = \lambda_1 \) and \( \alpha = \lambda_2 \), holds with **equality**. Hence the constant in the Kato–Temple bound cannot be improved.
:::
::::

::: {.solution}
Write \( c = \cos\phi \), \( s = \sin\phi \) and \( d = \lambda_1 - \lambda_2 > 0 \).

(a) \( \A\x = (\lambda_1c, \lambda_2s) \), so \( \mu = \lambda_1c^2 + \lambda_2s^2 \). Using \( c^2 + s^2 = 1 \), \( \lambda_1 - \mu = ds^2 \) and \( \lambda_2 - \mu = -dc^2 \). The residual is \( \A\x - \mu\x = \bigl((\lambda_1 - \mu)c, (\lambda_2 - \mu)s\bigr) = (ds^2c, -dc^2s) \), so
\[
\varepsilon^2 = d^2s^4c^2 + d^2c^4s^2 = d^2c^2s^2(s^2 + c^2) = d^2c^2s^2 .
\]

(b) Here \( \alpha = \lambda_2 < \mu \), since \( \mu - \lambda_2 = dc^2 > 0 \), and no eigenvalue lies in \( (\lambda_2, \lambda_1) \). The bound reads
\[
\mu + \frac{\varepsilon^2}{\mu - \lambda_2} = \mu + \frac{d^2c^2s^2}{dc^2} = \mu + ds^2 = \lambda_1 .
\]
So equality holds for every \( \phi \in (0, \pi/2) \), and no smaller multiple of \( \varepsilon^2/(\mu - \alpha) \) would give a valid bound.
:::
