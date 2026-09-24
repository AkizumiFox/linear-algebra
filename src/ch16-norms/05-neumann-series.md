# Inverting a Perturbation of the Identity

Chapter 10 §10 summed the series \( \I + \A + \A^2 + \dots \) and identified its sum as \( (\I - \A)^{-1} \), under the exact hypothesis that every eigenvalue of \( \A \) has modulus less than \( 1 \). What it could not say is how large that inverse is. This section reruns the argument with a norm in hand. The hypothesis becomes cruder — \( \norm{\A} < 1 \) instead of \( \rho(\A) < 1 \) — and the conclusion becomes quantitative, which is the trade this chapter keeps making. The payoff is immediate: the invertible matrices turn out to form an open set, inversion turns out to be continuous, and a first estimate appears for how far the solution of \( \A\x = \b \) moves when \( \A \) and \( \b \) are disturbed.

**Throughout, \( \norm{\cdot} \) is the operator norm on \( M_n(\nC) \) induced by a norm on \( \nC^{n} \)** (@def-operator-norm), so that \( \norm{\I} = 1 \) and \( \norm{\X\Y} \le \norm{\X}\norm{\Y} \) by @thm-operator-norm-properties (c) and (d). Both properties are used in every proof below, and the first of them is not free: the closing warning shows what happens without it.

## The geometric series, with a number attached

The scalar identity behind everything here is \( 1 + r + r^2 + \dots = 1/(1-r) \) for \( 0 \le r < 1 \). Chapter 10 §10 gave the matrix version of the *identity*. What a norm adds is the matrix version of the *inequality* \( \lvert 1 + r + \dots\rvert \le 1/(1-r) \): a ceiling on the inverse, expressed in the data.

::: {#thm-neumann-series}
[Neumann Series with a Bound]

Let \( \A \in M_n(\nC) \) with \( \norm{\A} < 1 \), and write \( a = \norm{\A} \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \I - \A \) is invertible, and \( \sum_{k \ge 0}\A^{k} = (\I - \A)^{-1} \);
2. \( \displaystyle \norm{(\I - \A)^{-1}} \le \frac{1}{1 - a} \);
3. for every \( K \ge 0 \), the partial sum \( \S_K = \sum_{k=0}^{K}\A^{k} \) satisfies
   \[
   \norm{(\I - \A)^{-1} - \S_K} \le \frac{a^{K+1}}{1 - a} ;
   \]
4. \( \displaystyle \norm{(\I - \A)^{-1}} \ge \frac{1}{1 + a} \).
:::
:::

::: {.idea}
Part (a) is not new work: \( \norm{\A} < 1 \) forces \( \rho(\A) < 1 \) by @thm-spectral-radius-le-norm, which is exactly the hypothesis of Chapter 10's @thm-neumann-series-spectral. Everything else is the tail-bounding move. Submultiplicativity turns \( \norm{\A^{k}} \) into \( a^{k} \), so each partial sum is bounded by a scalar geometric sum; the bound then has to be carried across the limit, and what carries it is the fact that a norm is continuous. For (c), the tail of the series factors as \( \A^{K+1} \) times the whole series again, so (b) bounds it. For (d), read \( \I = (\I - \A)(\I - \A)^{-1} \) through submultiplicativity.
:::

::: {.proof}
(a) By @thm-spectral-radius-le-norm (a), \( \rho(\A) \le \norm{\A} = a < 1 \), so every eigenvalue of \( \A \) has modulus less than \( 1 \). That is the hypothesis of @thm-neumann-series-spectral, which gives both the invertibility of \( \I - \A \) and the value of the sum.

(b) Submultiplicativity (@thm-operator-norm-properties (d)) gives \( \norm{\A^{k}} \le a^{k} \) for every \( k \ge 1 \), by induction on \( k \); and \( \norm{\A^{0}} = \norm{\I} = 1 = a^{0} \) by part (c) of the same theorem. Hence, by subadditivity applied \( K \) times,
\[
\norm{\S_K} \le \sum_{k=0}^{K}\norm{\A^{k}} \le \sum_{k=0}^{K}a^{k}
= \frac{1 - a^{K+1}}{1 - a} \le \frac{1}{1-a},
\]
the last step because \( a^{K+1} \ge 0 \) and \( 1 - a > 0 \). By (a) the sequence \( (\S_K) \) converges entrywise to \( (\I - \A)^{-1} \), so \( \norm{\S_K - (\I-\A)^{-1}} \to 0 \) by @cor-entrywise-convergence-is-the-convergence. Then @lem-reverse-triangle-norm gives
\[
\bigl\lvert\,\norm{\S_K} - \norm{(\I-\A)^{-1}}\,\bigr\rvert \le \norm{\S_K - (\I-\A)^{-1}} \to 0,
\]
so \( \norm{\S_K} \to \norm{(\I - \A)^{-1}} \). A non-strict inequality survives a limit, so a limit of numbers each at most \( 1/(1-a) \) is at most \( 1/(1-a) \), which proves (b).

(c) Fix \( K \). For every \( M \ge 1 \), multiplying out and canceling,
\[
\S_{K+M} - \S_K = \sum_{k=K+1}^{K+M}\A^{k} = \A^{K+1}\,\S_{M-1} .
\]
Let \( M \to \infty \). The left-hand side tends to \( (\I-\A)^{-1} - \S_K \) by (a). The right-hand side tends to \( \A^{K+1}(\I-\A)^{-1} \), because
\[
\norm{\A^{K+1}\S_{M-1} - \A^{K+1}(\I-\A)^{-1}}
\le \norm{\A^{K+1}}\,\norm{\S_{M-1} - (\I-\A)^{-1}} ,
\]
which tends to \( 0 \) by (a) and @cor-entrywise-convergence-is-the-convergence again. A sequence has at most one limit, so
\[
(\I - \A)^{-1} - \S_K = \A^{K+1}(\I - \A)^{-1} .
\]
Taking norms and using submultiplicativity together with (b),
\[
\norm{(\I-\A)^{-1} - \S_K} \le \norm{\A^{K+1}}\,\norm{(\I-\A)^{-1}} \le \frac{a^{K+1}}{1-a} .
\]

(d) \( 1 = \norm{\I} = \norm{(\I - \A)(\I-\A)^{-1}} \le \norm{\I - \A}\,\norm{(\I-\A)^{-1}} \), and \( \norm{\I - \A} \le \norm{\I} + \norm{\A} = 1 + a \) by subadditivity. Since \( 1 + a > 0 \) we may divide, which proves (d). This proves the theorem.
:::

Parts (b) and (d) together pin the inverse between two numbers computed from \( a \) alone:
\[
\frac{1}{1+a} \le \norm{(\I-\A)^{-1}} \le \frac{1}{1-a} .
\]
As \( a \) approaches \( 1 \) the upper bound escapes to infinity while the lower one stays near \( \tfrac12 \), and the gap is real rather than an artifact of the proof: \( \A = a\I \) attains the upper bound, and \( \A = -a\I \) attains the lower one.

::: {#exm-neumann-bound-two-by-two}
[The bound and the truth]

Let
\[
\A = \begin{pmatrix} 0 & 1/2 \\ 1/3 & 0 \end{pmatrix} .
\]
Using the \( \infty \)-norm, check the hypothesis, compute \( (\I - \A)^{-1} \) exactly, and compare it with the bound of @thm-neumann-series (b). Then compare \( \S_3 \) with the true inverse and with the tail bound of (c).
:::

::: {.solution}
*The hypothesis.* The absolute row sums are \( \tfrac12 \) and \( \tfrac13 \), so \( \norm{\A}_{\infty} = \tfrac12 < 1 \) by @thm-operator-norm-formulas (b). So @thm-neumann-series applies with \( a = \tfrac12 \).

*The inverse.* \( \I - \A = \begin{psmallmatrix} 1 & -1/2 \\ -1/3 & 1\end{psmallmatrix} \) has determinant \( 1 - \tfrac16 = \tfrac56 \), so by @thm-two-by-two-inverse
\[
(\I - \A)^{-1} = \tfrac65\begin{pmatrix} 1 & 1/2 \\ 1/3 & 1 \end{pmatrix}
= \begin{pmatrix} 6/5 & 3/5 \\ 2/5 & 6/5 \end{pmatrix},
\]
whose largest absolute row sum is \( \tfrac65 + \tfrac35 = \tfrac95 = 1.8 \). The bound is \( 1/(1 - \tfrac12) = 2 \). So the estimate is correct and loses only ten percent.

*The partial sum.* Here \( \A^{2} = \tfrac16\I \), so \( \A^{3} = \tfrac16\A \) and
\[
\S_3 = \bigl(1 + \tfrac16\bigr)(\I + \A) = \tfrac76\begin{pmatrix} 1 & 1/2 \\ 1/3 & 1\end{pmatrix} .
\]
Hence \( (\I-\A)^{-1} - \S_3 = \bigl(\tfrac65 - \tfrac76\bigr)(\I + \A) = \tfrac1{30}(\I + \A) \), with \( \infty \)-norm \( \tfrac1{30}\cdot\tfrac32 = \tfrac1{20} = 0.05 \). The bound of (c) with \( K = 3 \) is \( (\tfrac12)^{4}/(1 - \tfrac12) = \tfrac18 = 0.125 \). Again correct, and this time loose by a factor of \( 2.5 \) — the price of replacing four matrices by four copies of one number.
:::

## Which theorem is stronger

The two Neumann theorems must be compared honestly, because neither contains the other.

Chapter 10's @thm-neumann-series-spectral assumes \( \rho(\A) < 1 \) and concludes that the series converges, with sum \( (\I-\A)^{-1} \); and its hypothesis is **sharp**, since the statement is an "if and only if". @thm-neumann-series assumes \( \norm{\A} < 1 \), which by @thm-spectral-radius-le-norm is a **strictly stronger** demand: \( \rho(\A) \le \norm{\A} \) always, and the inequality is often strict. For
\[
\A = \begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix}
\]
we have \( \rho(\A) = 0 \), so Chapter 10's theorem applies and returns \( \sum_k \A^{k} = \I + \A \); but \( \norm{\A} = 2 \) in each of the \( 1 \)-, \( 2 \)- and \( \infty \)-norms, so this section's theorem says nothing at all about it.

In the other direction, when this section's theorem does apply it says strictly more: a ceiling on the inverse, a rate at which the partial sums approach it, and a floor as well. Chapter 10 could not have stated any of the three, having no way to measure a matrix.

There is a third thing to say, and it dissolves most of the apparent conflict. If \( \rho(\A) < 1 \), then by @thm-norm-close-to-spectral-radius there is a norm \( \norm{\cdot}_t \) with \( \norm{\A}_t \le \rho(\A) + \varepsilon < 1 \), and @thm-neumann-series applies **in that norm**. For the matrix above, taking \( \D = \diag(1, 4) \) and \( \norm{\x}_t = \norm{\D\x}_{\infty} \) gives \( \norm{\A}_t = \norm{\D\A\D^{-1}}_{\infty} = \tfrac12 \), so the bound reads \( \norm{(\I-\A)^{-1}}_t \le 2 \); and indeed \( \D(\I + \A)\D^{-1} = \begin{psmallmatrix} 1 & 1/2 \\ 0 & 1\end{psmallmatrix} \) has \( \infty \)-norm \( \tfrac32 \le 2 \). So the quantitative theorem can always be brought to bear on a matrix Chapter 10 accepts — at the cost of changing the norm, and the bound it then produces is a bound in that new norm, which may be a strange unit of measurement.

::: {.check}
Both theorems need a hypothesis. Which of the two hypotheses, \( \rho(\A) < 1 \) and \( \norm{\A} < 1 \), can be checked by looking at the entries of \( \A \) and doing no linear algebra?
:::

::: {.solution}
The second, for a suitable norm: \( \norm{\A}_1 \) and \( \norm{\A}_{\infty} \) are the largest absolute column and row sums (@thm-operator-norm-formulas), read straight off the entries. Deciding \( \rho(\A) < 1 \) requires the eigenvalues, that is, the roots of a degree-\( n \) polynomial. This is the practical reason the cruder hypothesis is worth having: it is the one a reader can verify at a glance, and @cor-spectral-radius-row-column-bound is the same observation used in the other direction.
:::

::: {.warning}
**The hypothesis \( \norm{\A} < 1 \) is sufficient and never necessary.** A matrix can be as far from \( \I \) as one likes and still have \( \I - \A \) invertible: \( \A = 5\I \) gives \( (\I - \A)^{-1} = -\tfrac14\I \). What fails when \( \norm{\A} \ge 1 \) is not the invertibility but the *argument*, and with it the bound. Read \( \norm{\A} < 1 \) as "\( \A \) is a small perturbation", not as a criterion.
:::

## The invertible matrices form an open set

The theorem above concerns perturbations of \( \I \). Every invertible matrix can be moved to \( \I \) by multiplication, so the general statement follows at once, and it is the statement several earlier arguments wanted: a matrix near an invertible matrix is invertible, and its inverse is near.

::: {#cor-invertible-matrices-open}
[Invertibility Is an Open Condition, and Inversion Is Continuous]

Let \( \B \in M_n(\nC) \) be invertible and let \( \E \in M_n(\nC) \) satisfy
\[
\norm{\E} < \frac{1}{\norm{\B^{-1}}} .
\]
Write \( r = \norm{\B^{-1}}\norm{\E} < 1 \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \B + \E \) is invertible, and \( \displaystyle \norm{(\B+\E)^{-1}} \le \frac{\norm{\B^{-1}}}{1 - r} \);
2. \( \displaystyle \norm{(\B+\E)^{-1} - \B^{-1}} \le \frac{\norm{\B^{-1}}^{2}\norm{\E}}{1 - r} \).
:::

Consequently \( \GL_n(\nC) \) is an open subset of \( M_n(\nC) \): around every invertible \( \B \) the ball of radius \( 1/\norm{\B^{-1}} \) consists of invertible matrices. And inversion is continuous on it: if \( \B_m \to \B \) with \( \B \) invertible, then \( \B_m \) is invertible for all large \( m \) and \( \B_m^{-1} \to \B^{-1} \).
:::

::: {.idea}
Factor the perturbed matrix as \( \B + \E = \B(\I + \B^{-1}\E) \) — legitimate because \( \B \) is invertible — and notice that \( \norm{\B^{-1}\E} \le r < 1 \), so the second factor is a perturbation of the identity of exactly the kind @thm-neumann-series handles, with \( \A = -\B^{-1}\E \). For (b), the difference of two inverses always factors as \( \X^{-1} - \Y^{-1} = \X^{-1}(\Y - \X)\Y^{-1} \), and both inverses are now bounded.
:::

::: {.proof}
Put \( \A = -\B^{-1}\E \). By submultiplicativity, \( \norm{\A} \le \norm{\B^{-1}}\norm{\E} = r < 1 \).

(a) Since \( \B \) is invertible, \( \B + \E = \B(\I + \B^{-1}\E) = \B(\I - \A) \). By @thm-neumann-series (a) the factor \( \I - \A \) is invertible, so \( \B + \E \) is a product of invertible matrices and is invertible, with
\[
(\B + \E)^{-1} = (\I - \A)^{-1}\B^{-1} .
\]
By submultiplicativity and @thm-neumann-series (b),
\[
\norm{(\B+\E)^{-1}} \le \norm{(\I-\A)^{-1}}\,\norm{\B^{-1}}
\le \frac{\norm{\B^{-1}}}{1 - \norm{\A}} \le \frac{\norm{\B^{-1}}}{1 - r} ,
\]
the last step because \( \norm{\A} \le r \) and \( t \mapsto 1/(1-t) \) increases on \( [0,1) \).

(b) Multiplying the identity \( \B - (\B + \E) = -\E \) on the left by \( (\B+\E)^{-1} \) and on the right by \( \B^{-1} \) gives
\[
(\B+\E)^{-1} - \B^{-1} = -(\B+\E)^{-1}\E\,\B^{-1} .
\]
Taking norms and applying submultiplicativity twice and then (a),
\[
\norm{(\B+\E)^{-1} - \B^{-1}}
\le \frac{\norm{\B^{-1}}}{1-r}\,\norm{\E}\,\norm{\B^{-1}}
= \frac{\norm{\B^{-1}}^{2}\norm{\E}}{1-r} .
\]

For the two consequences: openness is the statement of (a) with \( \E \) ranging over the ball of radius \( 1/\norm{\B^{-1}} \). For continuity, let \( \B_m \to \B \) with \( \B \) invertible, and put \( \E_m = \B_m - \B \). By @cor-entrywise-convergence-is-the-convergence, \( \norm{\E_m} \to 0 \), so \( \norm{\E_m} < 1/(2\norm{\B^{-1}}) \) for all large \( m \); for those \( m \), part (a) applies with \( r \le \tfrac12 \) and \( \B_m \) is invertible, and part (b) gives
\[
\norm{\B_m^{-1} - \B^{-1}} \le 2\norm{\B^{-1}}^{2}\norm{\E_m} \to 0 .
\]
This proves the corollary.
:::

::: {#exm-openness-with-numbers}
[How far an invertible matrix can be pushed]

Take \( \B = \begin{psmallmatrix} 2 & 1 \\ 0 & 2\end{psmallmatrix} \) and work with \( \norm{\cdot}_\infty \). Then \( \B^{-1} = \begin{psmallmatrix} \tfrac12 & -\tfrac14 \\ 0 & \tfrac12\end{psmallmatrix} \), whose largest absolute row sum is \( \tfrac12 + \tfrac14 = \tfrac34 \), so \( \norm{\B^{-1}}_\infty = \tfrac34 \). @cor-invertible-matrices-open therefore keeps \( \B + \E \) invertible for every \( \E \) with
\[
\norm{\E}_\infty < \frac{1}{\norm{\B^{-1}}_\infty} = \frac43 .
\]
For a perturbation of size \( \norm{\E}_\infty \le \tfrac12 \) we get \( r = \tfrac34\cdot\tfrac12 = \tfrac38 \), and part (a) bounds
\[
\norm{(\B+\E)^{-1}}_\infty \ \le\ \frac{3/4}{1 - 3/8} \ =\ \frac65 .
\]
The bound is honest rather than tight: pushing every entry of \( \E \) to \( \pm\tfrac14 \) gives at worst \( \norm{(\B+\E)^{-1}}_\infty = \tfrac{12}{11} \approx 1.09 \), against the promised \( 1.2 \). What the corollary buys is not the sharpest constant but a radius inside which no invertibility check is needed at all.
:::

Part (a) has a reading worth recording, since the relative-error theorem of §08 is the same sentence with the constant named: **the distance from an invertible \( \B \) to the nearest singular matrix is at least \( 1/\norm{\B^{-1}} \).** A large \( \norm{\B^{-1}} \) is therefore not an abstract complaint; it says that \( \B \) is close, in the literal sense of the norm, to a matrix that cannot be inverted at all.

::: {.remark}
Chapter 12 §01 proved that every matrix has diagonalizable matrices arbitrarily close to it (@cor-schur-normal-matrix-nearby) and used the word "close" before this chapter existed. @cor-invertible-matrices-open is the first of the two facts that argument needs; the second is the continuity of the eigenvalues, and the two are put together in §07.
:::

## Perturbing a solve

The question the rest of the chapter circles is this. A linear system \( \A\x = \b \) is solved; the data \( \A \) and \( \b \) were only known approximately; how wrong can \( \x \) be? With @cor-invertible-matrices-open available the answer is three lines, and it already contains the quantity §08 will name.

::: {#thm-perturbed-inverse-bound}
[Relative Error in a Perturbed Solve]

Let \( \A \in M_n(\nC) \) be invertible, let \( \b \ne \0 \), and let \( \x \) be the solution of \( \A\x = \b \). Let \( \E \in M_n(\nC) \) and \( \f \in \nC^{n} \) be perturbations with
\[
r = \norm{\A^{-1}}\norm{\E} < 1 ,
\]
and let \( \widetilde{\x} \) be the solution of \( (\A + \E)\widetilde{\x} = \b + \f \), which exists and is unique by @cor-invertible-matrices-open. Then
\[
\frac{\norm{\widetilde{\x} - \x}}{\norm{\x}}
\le \frac{\norm{\A}\,\norm{\A^{-1}}}{1 - r}
\left( \frac{\norm{\E}}{\norm{\A}} + \frac{\norm{\f}}{\norm{\b}} \right) .
\]
:::

::: {.idea}
Subtract the two equations to isolate \( \A(\widetilde{\x} - \x) \); what is left on the other side is \( \f - \E\widetilde{\x} \). Apply \( \A^{-1} \) and take norms. The one awkward term is \( \norm{\widetilde{\x}} \), which is not data; write \( \widetilde{\x} = \x + (\widetilde{\x} - \x) \) and move the resulting copy of \( \norm{\widetilde{\x} - \x} \) to the left, which is where the factor \( 1/(1-r) \) comes from. Finally \( \norm{\b} \le \norm{\A}\norm{\x} \) converts \( 1/\norm{\x} \) into \( \norm{\A}/\norm{\b} \), and the two perturbations appear only through their relative sizes.
:::

::: {.proof}
Write \( \d = \widetilde{\x} - \x \). Subtracting \( \A\x = \b \) from \( (\A+\E)\widetilde{\x} = \b + \f \) gives \( \A\widetilde{\x} + \E\widetilde{\x} - \A\x = \f \), that is, \( \A\d = \f - \E\widetilde{\x} \). Since \( \A \) is invertible, \( \d = \A^{-1}(\f - \E\widetilde{\x}) \), and @thm-operator-norm-properties (a) with subadditivity gives
\[
\norm{\d} \le \norm{\A^{-1}}\bigl(\norm{\f} + \norm{\E}\,\norm{\widetilde{\x}}\bigr) .
\]
Now \( \norm{\widetilde{\x}} \le \norm{\x} + \norm{\d} \), so
\[
\norm{\d} \le \norm{\A^{-1}}\norm{\f} + \norm{\A^{-1}}\norm{\E}\norm{\x} + r\norm{\d} ,
\]
using \( \norm{\A^{-1}}\norm{\E} = r \) on the last term. Since \( r < 1 \) we may subtract \( r\norm{\d} \) and divide by \( 1 - r > 0 \):
\[
\norm{\d} \le \frac{\norm{\A^{-1}}}{1-r}\bigl(\norm{\f} + \norm{\E}\norm{\x}\bigr) .
\]
Divide by \( \norm{\x} \), which is non-zero because \( \b \ne \0 \):
\[
\frac{\norm{\d}}{\norm{\x}} \le \frac{\norm{\A^{-1}}}{1-r}
\left( \frac{\norm{\f}}{\norm{\x}} + \norm{\E} \right) .
\]
Finally \( \norm{\b} = \norm{\A\x} \le \norm{\A}\norm{\x} \), so \( 1/\norm{\x} \le \norm{\A}/\norm{\b} \). Substituting this in the first term and writing \( \norm{\E} = \norm{\A}\cdot\norm{\E}/\norm{\A} \) in the second gives the stated inequality. This proves the theorem.
:::

The shape of the conclusion is the point. On the right, the two perturbations appear only as **relative** sizes, \( \norm{\E}/\norm{\A} \) and \( \norm{\f}/\norm{\b} \); on the left is the relative size of the error. Between them stands one number built from \( \A \) alone,
\[
\norm{\A}\,\norm{\A^{-1}} ,
\]
inflated slightly by \( 1/(1-r) \), which is close to \( 1 \) whenever the perturbation of \( \A \) is small. That number is the condition number of §08. Everything that section does is to give it a name, compute it for the \( 2 \)-norm, and show that the bound is attained.

::: {#exm-perturbed-solve-numeric}
[A perturbation of the matrix]

Let
\[
\A = \begin{pmatrix} 2 & 1 \\ 1 & 1\end{pmatrix}, \quad
\b = \begin{pmatrix} 3 \\ 2\end{pmatrix}, \quad
\E = \begin{pmatrix} 0 & 0 \\ 0 & 1/10 \end{pmatrix}, \quad \f = \0 .
\]
Solve both systems in the \( \infty \)-norm, compute the relative error, and compare it with @thm-perturbed-inverse-bound.
:::

::: {.solution}
*The two solutions.* \( \det \A = 1 \), so \( \A^{-1} = \begin{psmallmatrix} 1 & -1 \\ -1 & 2\end{psmallmatrix} \) by @thm-two-by-two-inverse, and \( \x = \A^{-1}\b = (3 - 2,\ -3 + 4) = (1, 1) \). For the perturbed matrix, \( \A + \E = \begin{psmallmatrix} 2 & 1 \\ 1 & 11/10 \end{psmallmatrix} \) has determinant \( \tfrac{22}{10} - 1 = \tfrac65 \), so
\[
\widetilde{\x} = \tfrac56\begin{pmatrix} 11/10 & -1 \\ -1 & 2 \end{pmatrix}\begin{pmatrix} 3 \\ 2\end{pmatrix}
= \tfrac56\begin{pmatrix} 13/10 \\ 1 \end{pmatrix}
= \begin{pmatrix} 13/12 \\ 5/6 \end{pmatrix} .
\]

*The error.* \( \widetilde{\x} - \x = (\tfrac1{12}, -\tfrac16) \), so \( \norm{\widetilde{\x} - \x}_{\infty} = \tfrac16 \) and, since \( \norm{\x}_{\infty} = 1 \), the relative error is \( \tfrac16 \approx 0.167 \).

*The bound.* The absolute row sums give \( \norm{\A}_{\infty} = 3 \) and \( \norm{\A^{-1}}_{\infty} = 3 \), so \( \norm{\A}_{\infty}\norm{\A^{-1}}_{\infty} = 9 \). Also \( \norm{\E}_{\infty} = \tfrac1{10} \) and \( r = 3\cdot\tfrac1{10} = \tfrac3{10} < 1 \). With \( \f = \0 \) the bound is
\[
\frac{9}{1 - \tfrac3{10}}\cdot\frac{1/10}{3} = \frac{9}{7/10}\cdot\frac1{30} = \frac37 \approx 0.429 .
\]
So \( 0.167 \le 0.429 \): correct, and loose by a factor of about \( 2.6 \). Note the accounting. The matrix was disturbed by \( 3.3\% \) of its size and the answer moved by \( 16.7\% \), an amplification of about \( 5 \); the theorem promised at most \( 9/(1 - 0.3) \approx 12.9 \).
:::

::: {.warning}
**All four bounds of this section need \( \norm{\I} = 1 \), which is a property of *induced* norms only.** The Frobenius norm is submultiplicative (@exm-frobenius-is-a-matrix-norm) but has \( \norm{\I_n}_F = \sqrt n \). Take \( \A = 0 \) in \( M_2(\nC) \): then \( \norm{\A}_F = 0 < 1 \), while
\[
\norm{(\I - \A)^{-1}}_F = \norm{\I_2}_F = \sqrt2 > 1 = \frac{1}{1 - \norm{\A}_F} ,
\]
so @thm-neumann-series (b) is false for it. The repair is easy — @exr-neumann-series-c3 — but it is not the same inequality, and using the Frobenius norm here is the most common way to arrive at a wrong constant.
:::

## Exercises

### A. Check your understanding

:::: {#exr-neumann-series-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State @thm-neumann-series in full, including which kind of norm it assumes.
2. Chapter 10 §10 already proved that \( \sum_k\A^{k} \) converges to \( (\I-\A)^{-1} \) when \( \rho(\A) < 1 \). Say precisely what this section adds, and what it gives up.
3. Determine whether the following statement is correct, and justify your answer: if \( \I - \A \) is invertible then \( \norm{\A} < 1 \).
4. Where in the proof of @thm-neumann-series is \( \norm{\I} = 1 \) used?
5. State what @cor-invertible-matrices-open says about the distance from an invertible matrix to the singular matrices.
:::
::::

::: {.solution}
(a) If \( \norm{\cdot} \) is the operator norm induced by a vector norm and \( \norm{\A} = a < 1 \), then \( \I - \A \) is invertible with \( \sum_{k\ge0}\A^{k} = (\I-\A)^{-1} \); moreover \( \norm{(\I-\A)^{-1}} \le 1/(1-a) \), the partial sums satisfy \( \norm{(\I-\A)^{-1} - \S_K} \le a^{K+1}/(1-a) \), and \( \norm{(\I-\A)^{-1}} \ge 1/(1+a) \).

(b) It adds three numbers: a ceiling on the inverse, a geometric rate for the partial sums, and a floor. It gives up sharpness of the hypothesis: \( \rho(\A) < 1 \) is necessary and sufficient for convergence, whereas \( \norm{\A} < 1 \) is only sufficient, and strictly stronger by @thm-spectral-radius-le-norm.

(c) Incorrect. \( \A = 5\I \) has \( \I - \A = -4\I \), invertible, while \( \norm{\A} = 5 \) in every induced norm. Invertibility of \( \I - \A \) says only \( 1 \notin \spec(\A) \).

(d) Twice, and both times to make a geometric sum start at \( 1 \): in (b), where \( \norm{\A^{0}} = \norm{\I} = 1 \) is the \( k = 0 \) term of \( \sum_k a^{k} \); and in (d), where \( 1 = \norm{\I} \) is the left-hand side of the estimate.

(e) It is at least \( 1/\norm{\B^{-1}} \): every \( \E \) with \( \norm{\E} < 1/\norm{\B^{-1}} \) leaves \( \B + \E \) invertible.
:::

### B. Practice

:::: {#exr-neumann-series-b1}
[B1: Check, sum, compare]

Let \( \A = \begin{pmatrix} 1/4 & 1/4 \\ 0 & 1/2 \end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Verify the hypothesis of @thm-neumann-series for \( \norm{\cdot}_{\infty} \).
2. Compute \( (\I - \A)^{-1} \) exactly and compare \( \norm{(\I-\A)^{-1}}_{\infty} \) with the bound of (b) and with the lower bound of (d).
:::
::::

::: {.solution}
(a) The absolute row sums are \( \tfrac12 \) and \( \tfrac12 \), so \( \norm{\A}_{\infty} = \tfrac12 < 1 \) by @thm-operator-norm-formulas (b).

(b) \( \I - \A = \begin{psmallmatrix} 3/4 & -1/4 \\ 0 & 1/2\end{psmallmatrix} \), upper triangular with determinant \( \tfrac38 \), so by @thm-two-by-two-inverse
\[
(\I-\A)^{-1} = \tfrac83\begin{pmatrix} 1/2 & 1/4 \\ 0 & 3/4\end{pmatrix}
= \begin{pmatrix} 4/3 & 2/3 \\ 0 & 2 \end{pmatrix} .
\]
The absolute row sums are \( 2 \) and \( 2 \), so \( \norm{(\I-\A)^{-1}}_{\infty} = 2 \). The upper bound is \( 1/(1-\tfrac12) = 2 \), attained exactly; the lower bound is \( 1/(1+\tfrac12) = \tfrac23 \), comfortably satisfied. The upper bound is attained because both rows of \( \A \) have the same absolute sum and no cancellation occurs anywhere in the geometric series.
:::

:::: {#exr-neumann-series-b2}
[B2: A perturbed right-hand side]

Let \( \A = \begin{pmatrix} 3 & 1 \\ 1 & 2\end{pmatrix} \), \( \b = (4, 3) \) and \( \f = (1/10, 0) \), with \( \E = 0 \). Solve both systems, compute the relative error in the \( \infty \)-norm, and compare with @thm-perturbed-inverse-bound.
::::

::: {.solution}
\( \det \A = 5 \), so \( \A^{-1} = \tfrac15\begin{psmallmatrix} 2 & -1 \\ -1 & 3\end{psmallmatrix} \) by @thm-two-by-two-inverse, and \( \x = \A^{-1}\b = \tfrac15(8 - 3, -4 + 9) = (1, 1) \).

With \( \b + \f = (\tfrac{41}{10}, 3) \) we get \( \widetilde{\x} = \tfrac15(\tfrac{82}{10} - 3, -\tfrac{41}{10} + 9) = (\tfrac{52}{50}, \tfrac{49}{50}) \). Hence \( \widetilde{\x} - \x = (\tfrac{2}{50}, -\tfrac{1}{50}) \) and \( \norm{\widetilde{\x} - \x}_{\infty} = \tfrac1{25} = 0.04 \), a relative error of \( 0.04 \) since \( \norm{\x}_{\infty} = 1 \).

For the bound: \( \norm{\A}_{\infty} = 4 \), \( \norm{\A^{-1}}_{\infty} = \tfrac45 \), so \( \norm{\A}_{\infty}\norm{\A^{-1}}_{\infty} = \tfrac{16}{5} \). Here \( \E = 0 \), so \( r = 0 \), and \( \norm{\f}_{\infty}/\norm{\b}_{\infty} = \tfrac{1/10}{4} = \tfrac1{40} \). The bound is \( \tfrac{16}{5}\cdot\tfrac1{40} = \tfrac2{25} = 0.08 \). So \( 0.04 \le 0.08 \), loose by a factor of exactly \( 2 \).
:::

:::: {#exr-neumann-series-b3}
[B3: Staying invertible]

Let \( \B = \begin{pmatrix} 2 & 0 \\ 0 & 1/2 \end{pmatrix} \). Using \( \norm{\cdot}_{\infty} \), find a radius \( \delta > 0 \) such that every \( \E \) with \( \norm{\E}_{\infty} < \delta \) leaves \( \B + \E \) invertible, and bound \( \norm{(\B+\E)^{-1}}_{\infty} \) for \( \norm{\E}_{\infty} \le \tfrac14 \). Is your \( \delta \) the largest possible?
::::

::: {.solution}
\( \B^{-1} = \diag(\tfrac12, 2) \), so \( \norm{\B^{-1}}_{\infty} = 2 \) and @cor-invertible-matrices-open gives \( \delta = 1/\norm{\B^{-1}}_{\infty} = \tfrac12 \).

For \( \norm{\E}_{\infty} \le \tfrac14 \) we get \( r = 2\cdot\tfrac14 = \tfrac12 \), so part (a) of the corollary gives
\[
\norm{(\B+\E)^{-1}}_{\infty} \le \frac{2}{1 - \tfrac12} = 4 .
\]

It is the largest possible here. Taking \( \E = \diag(0, -\tfrac12) \) gives \( \norm{\E}_{\infty} = \tfrac12 \) and \( \B + \E = \diag(2, 0) \), which is singular. So no radius larger than \( \tfrac12 \) works, and the estimate \( 1/\norm{\B^{-1}} \) is attained by this \( \B \). (It is not attained by every \( \B \) in every norm; @exr-neumann-series-c2 returns to this.)
:::

### C. Going deeper

:::: {#exr-neumann-series-c1}
[C1: The inverse to first order]

Let \( \norm{\A} < 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \norm{(\I - \A)^{-1} - \I - \A} \le \dfrac{\norm{\A}^{2}}{1 - \norm{\A}} \).
2. Deduce that for a fixed \( \M \in M_n(\nC) \) and small real \( t \),
   \[
   (\I - t\M)^{-1} = \I + t\M + \R(t), \qquad \norm{\R(t)}/\lvert t\rvert \to 0
   \]
   as \( t \to 0 \).
:::

*Hint for (a): this is @thm-neumann-series (c) with a particular \( K \).*
::::

::: {.solution}
(a) Take \( K = 1 \) in @thm-neumann-series (c): \( \S_1 = \I + \A \), so
\[
\norm{(\I-\A)^{-1} - \I - \A} \le \frac{\norm{\A}^{1+1}}{1 - \norm{\A}} = \frac{\norm{\A}^{2}}{1-\norm{\A}} .
\]

(b) If \( \M = 0 \) the claim is trivial, so assume \( \M \ne 0 \) and let \( \lvert t\rvert < 1/(2\norm{\M}) \). Then \( \norm{t\M} = \lvert t\rvert\norm{\M} < \tfrac12 \), so (a) applies with \( \A = t\M \) and gives, with \( \R(t) = (\I - t\M)^{-1} - \I - t\M \),
\[
\norm{\R(t)} \le \frac{t^{2}\norm{\M}^{2}}{1 - \lvert t\rvert\norm{\M}} \le 2t^{2}\norm{\M}^{2} ,
\]
using \( 1 - \lvert t\rvert\norm{\M} > \tfrac12 \). Hence \( \norm{\R(t)}/\lvert t\rvert \le 2\lvert t\rvert\norm{\M}^{2} \to 0 \) as \( t \to 0 \). So \( t \mapsto (\I - t\M)^{-1} \) is differentiable at \( t = 0 \) with derivative \( \M \), which is the case \( \A(t) = \I - t\M \) of the general formula for differentiating an inverse, proved in §06.
:::

:::: {#exr-neumann-series-c2}
[C2: Distance to the singular matrices]

Let \( \B \in M_n(\nC) \) be invertible and let \( \norm{\cdot} \) be an induced matrix norm.

::: {.enumerate options="label=(\alph*)"}
1. Prove that every singular \( \S \in M_n(\nC) \) satisfies \( \norm{\B - \S} \ge 1/\norm{\B^{-1}} \).
2. For \( \B = \diag(1, \varepsilon) \) with \( 0 < \varepsilon < 1 \) and the \( 2 \)-norm, exhibit a singular \( \S \) attaining the bound.
3. Hence say what \( \norm{\B^{-1}}_2 \) measures.
:::
::::

::: {.solution}
(a) Suppose \( \norm{\B - \S} < 1/\norm{\B^{-1}} \). Apply @cor-invertible-matrices-open with \( \E = \S - \B \): since \( \norm{\E} < 1/\norm{\B^{-1}} \), the matrix \( \B + \E = \S \) is invertible, contradicting the assumption that \( \S \) is singular. Hence \( \norm{\B - \S} \ge 1/\norm{\B^{-1}} \) for every singular \( \S \).

(b) \( \B^{-1} = \diag(1, 1/\varepsilon) \), a normal matrix, so its singular values are the moduli of its eigenvalues and \( \norm{\B^{-1}}_2 = 1/\varepsilon \) by @thm-operator-norm-formulas (c). The bound is therefore \( \varepsilon \). Take \( \S = \diag(1, 0) \), which is singular; then \( \B - \S = \diag(0, \varepsilon) \) and \( \norm{\B - \S}_2 = \varepsilon \). So the bound is attained.

(c) The reciprocal \( 1/\norm{\B^{-1}}_2 \) is a lower bound for the distance from \( \B \) to the singular matrices, attained in the example. So \( \norm{\B^{-1}}_2 \) is large exactly when \( \B \) is close to being singular, which is the geometric content behind the condition number of §08.
:::

:::: {#exr-neumann-series-c3}
[C3: Without \( \norm{\I} = 1 \)]

Let \( \norm{\cdot} \) be any matrix norm on \( M_n(\nC) \) in the sense of @def-matrix-norm, not necessarily induced, and let \( \norm{\A} < 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \I - \A \) is invertible and that
   \[
   \norm{(\I-\A)^{-1}} \le \norm{\I} + \frac{\norm{\A}}{1 - \norm{\A}} .
   \]
2. Verify that this bound is correct for the Frobenius norm on \( M_2(\nC) \) with \( \A = 0 \), where the bound of @thm-neumann-series (b) fails.
3. Explain why the argument of (a) cannot be improved to \( 1/(1 - \norm{\A}) \) for a general matrix norm.
:::
::::

::: {.solution}
(a) By @thm-spectral-radius-le-norm (b), which holds for every matrix norm, \( \rho(\A) \le \norm{\A} < 1 \); so @thm-neumann-series-spectral applies and gives both the invertibility of \( \I - \A \) and \( \S_K \to (\I-\A)^{-1} \). Submultiplicativity gives \( \norm{\A^{k}} \le \norm{\A}^{k} \) for \( k \ge 1 \), so separating the term \( k = 0 \),
\[
\norm{\S_K} \le \norm{\I} + \sum_{k=1}^{K}\norm{\A}^{k}
\le \norm{\I} + \frac{\norm{\A}}{1 - \norm{\A}} .
\]
As in the proof of @thm-neumann-series (b), @cor-entrywise-convergence-is-the-convergence and @lem-reverse-triangle-norm let the bound pass to the limit.

(b) With \( \A = 0 \), the right-hand side is \( \norm{\I_2}_F + 0 = \sqrt2 \), and the left-hand side is \( \norm{\I_2}_F = \sqrt2 \). The bound holds, with equality; the bound \( 1/(1-0) = 1 \) of @thm-neumann-series (b) does not.

(c) The case \( \A = 0 \) already decides it: the left-hand side is \( \norm{\I} \), so any valid bound must be at least \( \norm{\I} \), and \( 1/(1 - \norm{\A}) = 1 \) there. A norm with \( \norm{\I} > 1 \) therefore falsifies the sharper form at once, and by @thm-operator-norm-properties (c) an induced norm never has \( \norm{\I} > 1 \). This is exactly the difference between a matrix norm and an induced one.
:::
