# Loewner's Theorem

Chapter 17 §11 stated Loewner's theorem, said four times that this chapter would prove it, and named the one thing it was missing. Section 9 supplied the elementary half: a continuously differentiable function is monotone of order \( n \) exactly when every Loewner matrix of size \( n \) built from it is positive semidefinite (@thm-loewner-matrix-criterion). What is left is to turn that infinite family of conditions into a single formula, and to run the formula back. Turning it into a formula is the one thing this book does not prove; running it back costs about a page of integration, which we build first.

**Throughout, \( F = \nR \) or \( F = \nC \)**, every matrix whose eigenvalues are indexed is Hermitian, and \( f(\A) \) is the functional calculus of @def-function-of-normal-operator. The letter \( I \) denotes an **interval** of real numbers, not the identity matrix \( \I \), as in Chapter 17 §11. Three things from the analysis list of Chapter 16's introduction are used: completeness (A1), monotone convergence (A2) and the compactness of closed bounded sets (A3). Everything imported beyond those is named where it appears.

## Integrating a matrix-valued function

Chapter 17 §11 read the integral formula of @thm-loewner-statement (ii) and said what stopped it there:

> What this book lacks is the analysis that carries the Loewner order through an integral, which is not on the list (A1)–(A6) in Chapter 16's introduction.

That analysis is one definition and one lemma. It is not a theory of integration; it is the least that makes the sentence "an integral of positive semidefinite matrices is positive semidefinite" mean something.

A **tagged partition** of a compact interval \( [a, b] \) is a list of division points \( a = s_0 < s_1 < \dots < s_N = b \) together with **tags** \( \tau_i \in [s_{i-1}, s_i] \); we call the whole package \( P \). Its **mesh** is \( \max_i (s_i - s_{i-1}) \). For \( \M \colon [a, b] \to M_{p \times q}(\nC) \) the associated **Riemann sum** is
\[
S(\M, P) \coloneqq \sum_{i=1}^{N} \M(\tau_i)\,(s_i - s_{i-1}) .
\]
Call \( \M \) **continuous** when each of its \( pq \) entries is a continuous complex-valued function of \( s \); by @cor-entrywise-convergence-is-the-convergence this is the same as continuity for any norm on \( M_{p \times q}(\nC) \).

::: {#prp-riemann-sums-converge}
[Riemann Sums of a Continuous Matrix Function Converge]

Let \( \M \colon [a, b] \to M_{p \times q}(\nC) \) be continuous. Then there is a matrix \( J \in M_{p \times q}(\nC) \) such that \( S(\M, P_k) \to J \) for **every** sequence \( (P_k) \) of tagged partitions of \( [a, b] \) whose meshes tend to \( 0 \).
:::

::: {.idea}
Two Riemann sums of small mesh are close because each is close to the sum over their common refinement, and on a refinement the tag moves by less than the mesh. So the sums form a Cauchy sequence and converge. The one analytic input is that a continuous function on a compact interval does not merely move a little near each point but moves a little **uniformly**, which is compactness.
:::

:::: {.proof}
::: {.claim}
For every \( \varepsilon > 0 \) there is \( \delta > 0 \) such that \( \norm{\M(s) - \M(s')}_F \le \varepsilon \) whenever \( s, s' \in [a, b] \) and \( \lvert s - s' \rvert < \delta \).
:::

::: {.proof}
Suppose not. Then for some \( \varepsilon > 0 \) and every \( k \ge 1 \) the value \( \delta = 1/k \) fails, so there are \( s_k, s'_k \in [a, b] \) with \( \lvert s_k - s'_k \rvert < 1/k \) and \( \norm{\M(s_k) - \M(s'_k)}_F > \varepsilon \). The interval \( [a, b] \) is a closed bounded subset of \( \nR \), so by the compactness of closed bounded sets, **fact (A3) of Chapter 16's introduction**, a subsequence \( s_{k_j} \) converges to some \( s \in [a, b] \). Then \( s'_{k_j} \to s \) as well, since \( \lvert s'_{k_j} - s \rvert \le \lvert s'_{k_j} - s_{k_j}\rvert + \lvert s_{k_j} - s \rvert \to 0 \). Continuity of \( \M \) gives \( \M(s_{k_j}) \to \M(s) \) and \( \M(s'_{k_j}) \to \M(s) \), so \( \norm{\M(s_{k_j}) - \M(s'_{k_j})}_F \to 0 \), contradicting the lower bound \( \varepsilon \).
:::

Fix \( \varepsilon > 0 \) and let \( \delta \) be as in the claim. Let \( P \) be a tagged partition of mesh \( < \delta \), and let \( Q \) be a tagged partition whose division points include those of \( P \). Each interval \( q \) of \( Q \) lies inside exactly one interval of \( P \); write \( \tau(q) \) for the tag of that interval of \( P \) and \( \rho(q) \) for the tag of \( q \). Splitting each term of \( S(\M, P) \) along the intervals of \( Q \) inside it,
\[
S(\M, P) - S(\M, Q) = \sum_{q}\bigl(\M(\tau(q)) - \M(\rho(q))\bigr)\lvert q \rvert ,
\]
where \( \lvert q \rvert \) is the length of \( q \). Both \( \tau(q) \) and \( \rho(q) \) lie in one interval of \( P \), of length \( < \delta \), so each bracket has Frobenius norm at most \( \varepsilon \). The triangle inequality gives
\[
\norm{S(\M, P) - S(\M, Q)}_F \ \le\ \varepsilon\sum_q\lvert q\rvert \ =\ \varepsilon(b - a) .
\]
If \( P \) and \( P' \) both have mesh \( < \delta \), take for \( Q \) the partition whose division points are those of \( P \) together with those of \( P' \), with any tags; applying the bound twice,
\[
\norm{S(\M, P) - S(\M, P')}_F \ \le\ 2\varepsilon(b - a) . \tag{$\ast$}
\]

Now let \( (P_k) \) be tagged partitions with meshes tending to \( 0 \). Given \( \eta > 0 \), apply \( (\ast) \) with \( \varepsilon = \eta/(2(b - a) + 1) \): for all \( k, l \) large enough that both meshes are \( < \delta \), \( \norm{S(\M, P_k) - S(\M, P_l)}_F < \eta \). So each entry of \( S(\M, P_k) \) is a Cauchy sequence of complex numbers, hence convergent by **completeness, fact (A1)**; call the entrywise limit \( J \). If \( (P'_k) \) is a second such sequence, interleaving the two produces a third sequence of meshes tending to \( 0 \), whose sums converge; both subsequences must have that common limit, so the limits agree. This proves the proposition.
::::

::: {#def-matrix-integral}
[Integral of a Continuous Matrix-Valued Function]

Let \( \M \colon [a, b] \to M_{p \times q}(\nC) \) be continuous. Its **integral**
\[
\int_a^b \M(s)\,\dd s \ \in\ M_{p \times q}(\nC)
\]
is the matrix \( J \) of @prp-riemann-sums-converge. For a continuous \( \M \) on an open or half-open interval with endpoints \( a < b \), where \( a = -\infty \) or \( b = +\infty \) is allowed, the **improper integral** \( \int_a^b \M(s)\,\dd s \) is
the matrix \( J' \), if one exists, such that
\[
\int_{\alpha_k}^{\beta_k}\M(s)\,\dd s \ \longrightarrow\ J' \quad \text{entrywise}
\]
for every pair of sequences with \( \alpha_k \to a \), \( \beta_k \to b \) and \( a < \alpha_k < \beta_k < b \). The integral is then said to **converge**.
:::

Five properties are used below, and each is read off the Riemann sums together with the algebra of limits.

- **Entrywise.** The \( (i,j) \) entry of \( \int_a^b\M \) is \( \int_a^b m_{ij} \), because that is true of every Riemann sum. In particular @def-matrix-integral for \( p = q = 1 \) is the ordinary Riemann integral of a continuous complex function.
- **Linear.** \( \int(\M + \N) = \int\M + \int\N \) and \( \int c\M = c\int\M \) for a scalar \( c \).
- **Additive in the interval.** For \( a < c < b \), \( \int_a^b\M = \int_a^c\M + \int_c^b\M \): joining a tagged partition of \( [a, c] \) to one of \( [c, b] \) gives a tagged partition of \( [a, b] \) whose Riemann sum is the sum of the two, and the meshes tend to \( 0 \) together.
- **Constant factors pass out.** For constant \( \X \in M_{r \times p}(\nC) \) and \( \Y \in M_{q \times r'}(\nC) \), \( \int_a^b \X\M(s)\Y\,\dd s = \X\bigl(\int_a^b\M\bigr)\Y \), since \( S(\X\M\Y, P) = \X\,S(\M, P)\,\Y \).
- **Pairing passes in.** Taking \( \X = \x^{*} \) and \( \Y = \x \) in the previous item, \( \x^{*}\bigl(\int_a^b\M\bigr)\x = \int_a^b \x^{*}\M(s)\x\,\dd s \).

All five hold for a convergent improper integral, by taking the limit in \( \alpha \) and \( \beta \).

Now the lemma the whole section is for.

::: {#lem-integral-preserves-loewner}
[The Integral of a Positive Semidefinite Integrand]

Let \( \M \colon [a, b] \to M_n(\nC) \) be continuous with \( \M(s) \succeq 0 \) for every \( s \in [a, b] \). Then
\[
\int_a^b \M(s)\,\dd s \ \succeq\ 0 .
\]
The same conclusion holds for a **convergent improper** integral of a continuous integrand that is \( \succeq 0 \) at every point of the interval.
:::

::: {.proof}
Let \( \x \in \nC^n \). For a tagged partition \( P \),
\[
\x^{*}S(\M, P)\x = \sum_{i=1}^{N}\bigl(\x^{*}\M(\tau_i)\x\bigr)(s_i - s_{i-1}) ,
\]
a sum of products of two non-negative real numbers, since \( \M(\tau_i) \succeq 0 \) (@def-positive-semidefinite) and the interval lengths are positive. Hence \( \x^{*}S(\M, P)\x \ge 0 \) for every \( P \). Taking any sequence of tagged partitions with meshes tending to \( 0 \) and using @prp-riemann-sums-converge, \( \x^{*}S(\M, P_k)\x \to \x^{*}\bigl(\int_a^b\M\bigr)\x \); a non-strict inequality survives a limit, so that number is \( \ge 0 \).

It remains to check that \( \int_a^b\M \) is Hermitian. Each \( \M(s) \) is Hermitian, so each Riemann sum is, and the entrywise limit of Hermitian matrices is Hermitian: \( \conj{(\int m_{ji})} = \int\conj{m_{ji}} = \int m_{ij} \), since conjugation is continuous and commutes with sums. So \( \int_a^b\M \succeq 0 \).

For the improper case, each proper integral \( \int_{\alpha}^{\beta}\M \) is \( \succeq 0 \) by what has just been proved, and \( \x^{*}\bigl(\int_a^b\M\bigr)\x \) is the limit of the numbers \( \x^{*}\bigl(\int_{\alpha}^{\beta}\M\bigr)\x \ge 0 \), and the limit is Hermitian for the same reason.
:::

That is the whole of the promised analysis. Nothing in it is deep: the positive semidefinite matrices are closed under sums and under multiplication by non-negative numbers, and they are closed under limits, so a limit of sums of them stays inside.

::: {.check}
Let \( \M(t) = \begin{psmallmatrix} 1 & t \\ t & t^2\end{psmallmatrix} \) for \( t \in [0, 1] \). Is \( \M(t) \succeq 0 \) for each \( t \)? Compute \( \int_0^1\M(t)\,\dd t \) and check that the answer is \( \succeq 0 \). Does it have rank \( 1 \)?
:::

::: {.solution}
For each \( t \), \( \M(t) = \v(t)\v(t)\tp \) with \( \v(t) = (1, t) \), so \( \x\tp\M(t)\x = (x_1 + tx_2)^2 \ge 0 \) and \( \M(t) \succeq 0 \). Integrating entrywise, and using \( \int_0^1 t\,\dd t = \tfrac12 \) and \( \int_0^1 t^2\,\dd t = \tfrac13 \) (for a continuous integrand these can be read off the Riemann sums \( N^{-2}\sum_{i\le N} i \) and \( N^{-3}\sum_{i \le N}i^2 \)),
\[
\int_0^1\M(t)\,\dd t = \begin{pmatrix} 1 & \tfrac12 \\[2pt] \tfrac12 & \tfrac13\end{pmatrix} ,
\]
whose determinant is \( \tfrac13 - \tfrac14 = \tfrac1{12} > 0 \) and whose \( (1,1) \) entry is positive, so it is positive definite by Sylvester's criterion (@thm-pd-characterizations (d)). It has rank \( 2 \), not \( 1 \): every integrand was a rank-one matrix, and the integral is not. @lem-integral-preserves-loewner preserves positivity and nothing else.
:::

## The one fact this chapter quotes

Two statements in this chapter are not proved from Chapters 1–20: the one below, and Lieb's concavity theorem, which §12 states and nothing in the book uses. Beside them this section quotes two standard facts of one-variable calculus, the fundamental theorem of calculus and the substitution rule, each named at the point where it is used. The book's practice for such a fact is fixed — Chapter 11 with the theorem of Abel and Ruffini, Chapter 14 §06 with Taylor's theorem — and it is followed here: the statement is given in full, in a block of its own, named at every use, and never buried inside a proof that presents itself as self-contained.

:::: {#thm-pick-nevanlinna}
[(A7) The Theorem of Pick and Nevanlinna]

Let \( I \subseteq \nR \) be an open interval and let \( f \colon I \to \nR \).

::: {.enumerate options="label=(\alph*)"}
1. Suppose that \( f \) is differentiable and that for every \( n \ge 1 \) and all \( t_1, \dots, t_n \in I \) the Loewner matrix \( L_f(t_1, \dots, t_n) \) of @def-loewner-matrix is positive semidefinite. Then \( f \) is the restriction to \( I \) of a function analytic on \( \nC \setminus (\nR \setminus I) \) that maps every point of the upper half-plane \( \{ z : \operatorname{Im} z > 0 \} \) to a point with non-negative imaginary part.
2. Conversely, every function analytic on \( \nC \setminus (-\infty, 0] \) that maps the upper half-plane into \( \{ \operatorname{Im} z \ge 0 \} \) has, on \( I = (0, \infty) \), the integral representation of @thm-loewner-statement (ii): there are \( \alpha \in \nR \), \( \beta \ge 0 \) and a positive measure \( \nu \) on \( [0, \infty) \) with \( \int(1 + s^2)^{-1}\dd\nu(s) < \infty \) such that
\[
\begin{aligned}
f(t) &= \alpha + \beta t \\
 &\quad + \int_{[0,\infty)}\Bigl(\frac{s}{1 + s^2} - \frac{1}{t + s}\Bigr)\dd\nu(s)
\end{aligned}
\]
for every \( t > 0 \).
3. A function that is operator monotone on an open interval is continuously differentiable there.
:::
::::

**What it gives.** Exactly one thing: it converts an infinite family of matrix conditions — one positive semidefinite Loewner matrix for each size and each choice of points — into a single formula with two constants and one measure. Nothing in the statement is about matrices at all after clause (a) is applied.

**What it costs.** Clause (a) is complex analysis: one shows that the positivity of the Loewner matrices forces \( f \) to extend analytically across \( I \), and that the extension preserves the upper half-plane. Clause (b) is the Herglotz–Riesz representation of such a function, which produces the measure \( \nu \) by a compactness argument in a space of measures. Clause (c) is a regularity theorem. None of these is within reach of Chapters 1–20, and Chapter 17 §11 said so when it stated the theorem: "Its proof needs complex analysis and some measure theory, which lie outside Chapter 16's list (A1)–(A6)."

**A second cost, worth naming separately.** The integral in (b) is taken against a measure, and this book constructs no such integral. @def-matrix-integral covers the case \( \dd\nu(s) = w(s)\,\dd s \) with \( w \) continuous, and that is the only case the corollaries below need: each of them starts from a representation written down and verified by hand, with a continuous density. For a general \( \nu \), which is what (b) allows, the argument uses exactly two properties of the integral: it is **linear** in the integrand, and it sends a **non-negative** integrand to a non-negative number. Both are part of the meaning of "integral against a positive measure". For the integral the book does construct they are proved — linearity in the list of properties after @def-matrix-integral, positivity in @lem-integral-preserves-loewner; for a general measure they are quoted, along with (A7) itself.

**Which half rests on it.** Only the hard half. In @thm-loewner below, the implication (ii) \( \Rightarrow \) (i) is proved here from Chapter 17 §11 and @lem-integral-preserves-loewner, with no appeal to (A7) — subject only to the second cost just named, since for a general \( \nu \) the linearity and the positivity of the integral are quoted rather than constructed. The implications (i) \( \Rightarrow \) (iii) \( \Rightarrow \) (ii) — the classification itself — use (A7) and cannot be had without it. Nothing else in this chapter uses (A7); in particular @cor-power-operator-monotone, @cor-log-operator-monotone and @cor-operator-convex-log below, which are what the earlier chapters actually asked for, are proved without it.

## Loewner's theorem

::: {#thm-loewner}
[Loewner's Theorem]

Let \( f \colon (0, \infty) \to \nR \). The following are equivalent.

::: {.enumerate options="label=(\roman*)"}
1. \( f \) is operator monotone on \( (0, \infty) \).
2. There are \( \alpha \in \nR \), \( \beta \ge 0 \) and a positive measure \( \nu \) on \( [0, \infty) \) with \( \int(1 + s^2)^{-1}\dd\nu(s) < \infty \) such that for every \( t > 0 \)
\[
\begin{aligned}
f(t) &= \alpha + \beta t \\
 &\quad + \int_{[0,\infty)}\Bigl(\frac{s}{1 + s^2} - \frac{1}{t + s}\Bigr)\dd\nu(s) .
\end{aligned}
\]
3. \( f \) is the restriction to \( (0, \infty) \) of a function analytic on \( \nC \setminus (-\infty, 0] \) that sends every point of the upper half-plane to a point with non-negative imaginary part.
:::

These are the three conditions of @thm-loewner-statement.
:::

::: {.idea}
Three steps, in a cycle.

① (ii) \( \Rightarrow \) (i). At each fixed \( s \ge 0 \) the integrand is \( -1/(t+s) \) plus a constant, and @cor-shifted-inverse-operator-monotone already knows those are operator monotone. Subtracting \( f(\B) \) from \( f(\A) \) kills the constants and leaves an integral of positive semidefinite matrices, which @lem-integral-preserves-loewner declares positive semidefinite.

② (i) \( \Rightarrow \) (iii). Operator monotonicity is monotonicity of every order, and §09 converts that into positivity of every Loewner matrix. (A7) converts that into analyticity.

③ (iii) \( \Rightarrow \) (ii). (A7) again.
:::

::: {.proof}
**Step 1: (ii) \( \Rightarrow \) (i).** Let \( \A, \B \in M_n(F) \) be Hermitian with spectra in \( (0, \infty) \) and \( \A \succeq \B \). For \( s \ge 0 \) put \( g_s(t) = -1/(t+s) \) on \( (0, \infty) \). By @cor-shifted-inverse-operator-monotone, \( g_s \) is operator monotone there, so
\[
\R(s) \coloneqq g_s(\A) - g_s(\B) = (\B + s\I)^{-1} - (\A + s\I)^{-1}
\]
satisfies \( \R(s) \succeq 0 \) for every \( s \ge 0 \); the identification of \( g_s(\A) \) with \( -(\A + s\I)^{-1} \) is @def-function-of-normal-operator applied to the spectral resolution of \( \A \).

Write \( \A = \sum_j\mu_j\P_j \) for that resolution (@thm-spectral-resolution). By @def-function-of-normal-operator and the hypothesis (ii),
\[
\begin{aligned}
f(\A) &= \sum_j f(\mu_j)\P_j \\
 &= \alpha\I + \beta\A \\
 &\quad + \int_{[0,\infty)}\Bigl(\frac{s}{1+s^2}\I - (\A + s\I)^{-1}\Bigr)\dd\nu(s) ,
\end{aligned}
\]
where the second line substitutes the formula (ii) for each \( f(\mu_j) \) and moves the finite sum \( \sum_j(\cdot)\P_j \) inside the integral, which is legitimate because the integral is **linear** in its integrand and the \( \P_j \) do not depend on \( s \); the identities \( \sum_j\P_j = \I \) and \( \sum_j\mu_j\P_j = \A \) are @thm-spectral-resolution (c) and (d). The same computation applies to \( \B \). Subtracting, the terms \( \alpha\I \) and \( \tfrac{s}{1+s^2}\I \) cancel, and
\[
f(\A) - f(\B) = \beta(\A - \B) + \int_{[0,\infty)}\R(s)\,\dd\nu(s) .
\]
Let \( \x \in F^n \). Pairing passes inside the integral, so
\[
\begin{aligned}
\x^{*}\bigl(f(\A) - f(\B)\bigr)\x
 &= \beta\,\x^{*}(\A - \B)\x \\
 &\quad + \int_{[0,\infty)}\x^{*}\R(s)\x\,\dd\nu(s) \ \ge\ 0 ,
\end{aligned}
\]
because \( \beta \ge 0 \), \( \x^{*}(\A-\B)\x \ge 0 \), and the integrand \( \x^{*}\R(s)\x \) is non-negative for every \( s \). This last step is @lem-integral-preserves-loewner when \( \dd\nu(s) = w(s)\dd s \) with \( w \) continuous, and in general uses only the linearity and positivity of the integral against a positive measure, as recorded with @thm-pick-nevanlinna. Hence \( f(\A) \succeq f(\B) \). The size \( n \) was arbitrary, so \( f \) is operator monotone (@def-operator-monotone (a)).

**Step 2: (i) \( \Rightarrow \) (iii).** Let \( f \) be operator monotone on \( (0, \infty) \). By @thm-pick-nevanlinna (c), \( f \) is continuously differentiable there. Fix \( n \ge 1 \) and \( t_1, \dots, t_n \in (0, \infty) \). Being operator monotone, \( f \) is in particular monotone of order \( n \), so @thm-loewner-matrix-criterion gives \( L_f(t_1, \dots, t_n) \succeq 0 \). As \( n \) and the points were arbitrary, the hypothesis of @thm-pick-nevanlinna (a) holds with \( I = (0, \infty) \). Since \( \nR \setminus (0, \infty) = (-\infty, 0] \), that clause produces an analytic function on \( \nC \setminus (-\infty, 0] \) restricting to \( f \) and mapping the upper half-plane into its closure. That is (iii).

**Step 3: (iii) \( \Rightarrow \) (ii).** This is @thm-pick-nevanlinna (b).

The cycle (i) \( \Rightarrow \) (iii) \( \Rightarrow \) (ii) \( \Rightarrow \) (i) closes, so the three conditions are equivalent.
:::

Step 1 is the step Chapter 17 §11 identified as missing, and it turned out to cost one lemma. Steps 2 and 3 are where the content is, and they are quoted. It is worth being precise about the division: **the book proves that every function of the form (ii) is operator monotone, and quotes that there are no others.**

::: {.warning}
**Analytic and increasing is not enough.** Condition (iii) is not "extends analytically"; it is "extends analytically **and keeps the upper half-plane**". The function \( e^{t} \) extends to an entire function and is increasing on \( \nR \), yet \( \operatorname{Im} e^{z} = e^{x}\sin y \) for \( z = x + iy \), which is negative at \( z = 3\pi i/2 \), where \( e^{z} = -i \). So \( e^{t} \) fails (iii), and @exm-exp-not-monotone below confirms the failure directly with two \( 2 \times 2 \) matrices.
:::

## The powers

Chapter 13 §05 announced the answer and deferred the proof:

> The dividing line is at \( s = 1 \): the functions preserving the order are called **operator monotone**, and \( t \mapsto t^{s} \) is operator monotone on \( [0, \infty) \) exactly for \( 0 \le s \le 1 \). Chapter 21 proves this, along with the companion fact that \( t \mapsto \log t \) is operator monotone while \( t \mapsto e^{t} \) is not.

Chapter 17 §11 repeated it, adding that "the operator monotonicity of \( t^p \) for every \( p \in (0, 1) \) needs a new idea, an integral representation of the kind in @thm-loewner-statement". Here is the representation, and it is elementary. Real powers \( t^{r} = e^{r\log t} \) are Chapter 18 §11's (@lem-exp-log).

::: {#lem-power-integral}
[The Integral That Represents a Power]

Let \( 0 < p < 1 \). Then the improper integral
\[
K_p \coloneqq \int_0^{\infty}\frac{u^{p-1}}{1 + u}\,\dd u
\]
converges, with \( 0 < K_p < \infty \), and for every \( \lambda > 0 \)
\[
\int_0^{\infty}s^{p-1}\,\frac{\lambda}{\lambda + s}\,\dd s \ =\ K_p\,\lambda^{p} .
\]
:::

::: {.idea}
Both halves are one idea. For convergence, cut \( (0, \infty) \) at the powers of \( 2 \): on each piece the integrand is bounded by its value at one endpoint, and the resulting bounds form a geometric series, convergent exactly because \( 0 < p < 1 \). For the identity, substitute \( s = \lambda u \); since the substitution is linear it can be made inside the Riemann sums, where it is visible as a relabeling of the partition together with a factor \( \lambda^{p} \).
:::

::: {.proof}
**Convergence.** The integrand is positive and continuous on \( (0, \infty) \), so interval additivity makes \( \delta \mapsto \int_{\delta}^{1} \) increase as \( \delta \) decreases and \( R \mapsto \int_1^{R} \) increase with \( R \); the same property splits each range at the powers of \( 2 \) below. It is enough to bound both families above: bounded above, they have a least upper bound \( L \) by **completeness, fact (A1) of Chapter 16's introduction**, and monotonicity in the parameter makes \( L \) the limit along *every* sequence of parameters tending to the endpoint, which is the form @def-matrix-integral asks for; along a decreasing sequence \( \delta_k \to 0^{+} \) that limit is **monotone convergence, fact (A2)**. Since \( p - 1 < 0 \), the function \( u^{p-1} \) is decreasing, so on \( [2^{-k-1}, 2^{-k}] \) it is at most \( (2^{-k-1})^{p-1} = 2^{(k+1)(1-p)} \); as \( 1/(1+u) \le 1 \) and the interval has length \( 2^{-k-1} \), the integral over it is at most \( 2^{-(k+1)p} \). Summing the geometric series,
\[
\int_{\delta}^{1}\frac{u^{p-1}}{1+u}\,\dd u \ \le\ \sum_{k \ge 0}2^{-(k+1)p} = \frac{1}{2^{p} - 1} ,
\]
for every \( \delta \in (0,1) \). For the other end use \( u^{p-1}/(1+u) \le u^{p-2} \), which on \( [2^{k}, 2^{k+1}] \) is at most \( 2^{k(p-2)} \); the interval has length \( 2^{k} \), so the integral over it is at most \( 2^{k(p-1)} \), and
\[
\int_1^{R}\frac{u^{p-1}}{1+u}\,\dd u \ \le\ \sum_{k \ge 0}2^{k(p-1)} = \frac{1}{1 - 2^{p-1}} ,
\]
which is finite because \( p - 1 < 0 \). So \( K_p < \infty \), and \( K_p > 0 \) because the integrand is positive and \( \int_1^2 \) is already positive.

**The identity.** Fix \( \lambda > 0 \) and \( 0 < \delta < R \). Let \( P \) be a tagged partition \( \delta/\lambda = u_0 < \dots < u_N = R/\lambda \) with tags \( v_i \). Multiplying every point by \( \lambda \) gives a tagged partition \( \lambda P \) of \( [\delta, R] \), with tags \( \lambda v_i \) and mesh \( \lambda \) times that of \( P \). Writing \( g(s) = s^{p-1}\lambda/(\lambda + s) \) and \( h(u) = u^{p-1}/(1+u) \),
\[
\begin{aligned}
g(\lambda v_i)\cdot\lambda(u_i - u_{i-1})
 &= \frac{\lambda^{p-1}v_i^{p-1}\lambda}{\lambda(1 + v_i)}\,\lambda(u_i - u_{i-1}) \\
 &= \lambda^{p}\,h(v_i)(u_i - u_{i-1}) ,
\end{aligned}
\]
using \( (\lambda v)^{p-1} = \lambda^{p-1}v^{p-1} \) (@lem-exp-log and the rules for real powers recorded after it). Summing over \( i \), \( S(g, \lambda P) = \lambda^{p}S(h, P) \). Letting the mesh of \( P \) tend to \( 0 \) — which sends that of \( \lambda P \) to \( 0 \) as well — and using @prp-riemann-sums-converge on both sides,
\[
\int_{\delta}^{R}g(s)\,\dd s = \lambda^{p}\int_{\delta/\lambda}^{R/\lambda}h(u)\,\dd u .
\]
Now let \( \delta \to 0^{+} \) and \( R \to \infty \). The right side tends to \( \lambda^{p}K_p \) by the first part, so the left side converges to it. This proves the lemma.
:::

::: {.remark}
The number \( K_p \) equals \( \pi/\sin(p\pi) \). That evaluation is a standard exercise in contour integration, and the constant \( \sin(p\pi)/\pi \) is the one Chapter 17 §11 displayed. Nothing below needs its value: only \( 0 < K_p < \infty \) is used, and that was proved. Exercise B2 computes \( K_{1/2} = \pi \) by hand.
:::

Two more small tools, both elementary, and then the corollary.

::: {#lem-operator-monotone-composite}
[Composites of Operator Monotone Functions]

Let \( I, J \) be intervals, let \( g \colon I \to \nR \) be operator monotone on \( I \) with \( g(I) \subseteq J \), and let \( h \colon J \to \nR \) be operator monotone on \( J \). Then \( h \circ g \) is operator monotone on \( I \).
:::

::: {.proof}
Let \( \A, \B \in M_n(F) \) be Hermitian with spectra in \( I \) and \( \A \succeq \B \). Then \( g(\A) \succeq g(\B) \), and both are Hermitian (@thm-functional-calculus-properties (c)) with spectra \( g(\spec(\A)) \) and \( g(\spec(\B)) \) by @thm-functional-calculus-properties (d), hence contained in \( g(I) \subseteq J \). So \( h(g(\A)) \succeq h(g(\B)) \).

It remains to see that \( h(g(\A)) = (h\circ g)(\A) \). Let \( \A = \sum_j\mu_j\P_j \) be the spectral resolution. Group the indices by the value of \( g \): let \( \nu_1, \dots, \nu_r \) be the distinct numbers among \( g(\mu_1), \dots, g(\mu_k) \) and put \( \Q_l = \sum_{j : g(\mu_j) = \nu_l}\P_j \). Each \( \Q_l \) is a non-zero orthogonal projection, \( \Q_l\Q_{l'} = \0 \) for \( l \ne l' \), and \( \sum_l\Q_l = \I \), by @thm-spectral-resolution (b) and (c). Since \( g(\A) = \sum_l\nu_l\Q_l \) with the \( \nu_l \) distinct, @thm-spectral-resolution-unique says this is the spectral resolution of \( g(\A) \). Hence, by @def-function-of-normal-operator applied twice,
\[
h(g(\A)) = \sum_l h(\nu_l)\Q_l = \sum_j h(g(\mu_j))\P_j = (h\circ g)(\A) .
\]
The same holds for \( \B \), so \( (h\circ g)(\A) \succeq (h\circ g)(\B) \).
:::

::: {#lem-operator-monotone-limit}
[Pointwise Limits Stay Operator Monotone]

Let \( f_k \colon I \to \nR \) be operator monotone on \( I \) for every \( k \), and suppose \( f_k(t) \to f(t) \) for every \( t \in I \). Then \( f \) is operator monotone on \( I \).
:::

::: {.proof}
Let \( \A \succeq \B \) be Hermitian of the same size with spectra in \( I \), with spectral resolutions \( \A = \sum_j\mu_j\P_j \) and \( \B = \sum_l\nu_l\Q_l \). By @def-function-of-normal-operator, \( f_k(\A) = \sum_jf_k(\mu_j)\P_j \), a fixed finite combination of fixed matrices with scalar coefficients converging to \( f(\mu_j) \); so \( f_k(\A) \to f(\A) \) entrywise, and likewise \( f_k(\B) \to f(\B) \). For each \( \x \) and each \( k \), \( \x^{*}(f_k(\A) - f_k(\B))\x \ge 0 \), and the left side tends to \( \x^{*}(f(\A) - f(\B))\x \). A non-strict inequality survives a limit, so \( f(\A) \succeq f(\B) \).
:::

::: {#cor-power-operator-monotone}
[The Operator Monotone Powers]

Let \( p \in \nR \). The function \( t \mapsto t^{p} \) is operator monotone on \( (0, \infty) \) **if and only if** \( 0 \le p \le 1 \). For those \( p \) the statement extends to \( [0, \infty) \): if \( \A \succeq \B \succeq 0 \) are Hermitian of the same size, then \( \A^{p} \succeq \B^{p} \).
:::

::: {.idea}
For \( 0 < p < 1 \), @lem-power-integral rewrites \( t^{p} \) as a positive superposition of the functions \( t/(t+s) \) that Chapter 17 §11 already proved operator monotone, and the superposition is an honest Riemann integral, so @lem-integral-preserves-loewner finishes it. For \( p > 1 \) the trick is that operator monotone functions compose: if \( t^{p} \) were operator monotone for one \( p > 1 \), enough compositions with each other and with a small power would manufacture \( t^{2} \), which is not.
:::

::: {.proof}
**The cases \( p = 0 \) and \( p = 1 \).** These are the constant \( 1 \) and the identity, operator monotone by @prp-affine-operator-monotone.

**The case \( p < 0 \).** Then \( t \mapsto t^{p} \) is strictly decreasing on \( (0, \infty) \), since \( t \mapsto t^{-p} \) is strictly increasing there (Chapter 18 §11). An operator monotone function is increasing (@prp-operator-monotone-increasing), so it is not operator monotone.

**The case \( 0 < p < 1 \), on \( (0, \infty) \).** Let \( \A \succeq \B \) be Hermitian in \( M_n(F) \) with spectra in \( (0, \infty) \). Write \( \A = \U\D\U^{*} \) with \( \U \) unitary and \( \D = \diag(\lambda_1, \dots, \lambda_n) \) the eigenvalues, all positive (@cor-spectral-complex-matrix, @cor-spectral-real-matrix, @thm-pd-characterizations (b)). For \( s > 0 \),
\[
s^{p-1}\A(\A + s\I)^{-1} = \U\,\diag\Bigl(\frac{s^{p-1}\lambda_i}{\lambda_i + s}\Bigr)\U^{*} ,
\]
where we are using that \( f(\A) = \U\diag(f(\lambda_1), \dots, f(\lambda_n))\U^{*} \) for every function \( f \) on \( \spec(\A) \): writing \( \u_1, \dots, \u_n \) for the columns of \( \U \), the spectral projection \( \P_j \) of @def-spectral-resolution is \( \sum_{i : \lambda_i = \mu_j}\u_i\u_i^{*} \), so the two expressions for \( f(\A) \) have the same terms. Every entry of the integrand is therefore a fixed linear combination of the \( n \) scalar functions of @lem-power-integral. By that lemma each of their improper integrals converges, so the matrix integral converges, and by the linearity of the integral together with the rule that constant factors pass out,
\[
\int_0^{\infty}s^{p-1}\A(\A + s\I)^{-1}\dd s = K_p\,\U\diag(\lambda_i^{p})\U^{*} = K_p\,\A^{p} ,
\]
the last equality by @def-function-of-normal-operator. The same holds for \( \B \). Subtracting,
\[
\A^{p} - \B^{p} = \frac{1}{K_p}\int_0^{\infty}s^{p-1}\bigl(\C(s) - \Y(s)\bigr)\dd s ,
\]
with \( \C(s) = \A(\A + s\I)^{-1} \) and \( \Y(s) = \B(\B + s\I)^{-1} \). Fix \( s > 0 \). The function \( t \mapsto t/(t+s) \) is operator monotone on \( (0, \infty) \) by @cor-shifted-inverse-operator-monotone, and it sends \( \A \) to \( \C(s) \) and \( \B \) to \( \Y(s) \); hence \( \C(s) - \Y(s) \succeq 0 \), and multiplying by the positive number \( s^{p-1} \) keeps it so. The integrand is continuous in \( s \) on \( (0, \infty) \) and the integral converges, so @lem-integral-preserves-loewner in its improper form gives \( \A^{p} - \B^{p} \succeq 0 \). As \( K_p > 0 \) and \( n \) was arbitrary, \( t \mapsto t^{p} \) is operator monotone on \( (0, \infty) \).

**The case \( p > 1 \).** Suppose, for a contradiction, that \( t \mapsto t^{p} \) is operator monotone on \( (0, \infty) \) for some \( p > 1 \). It maps \( (0, \infty) \) into itself, so by @lem-operator-monotone-composite it may be composed with itself: \( t \mapsto t^{p^{k}} \) is operator monotone for every \( k \ge 1 \). Choose \( k \) with \( p^{k} \ge 2 \) and put \( q = 2/p^{k} \in (0, 1] \). By the cases already proved, \( t \mapsto t^{q} \) is operator monotone on \( (0, \infty) \) and maps it into itself, so @lem-operator-monotone-composite applied to \( g(t) = t^{q} \) and \( h(u) = u^{p^{k}} \) makes
\[
t \longmapsto (t^{q})^{p^{k}} = t^{\,qp^{k}} = t^{2}
\]
operator monotone on \( (0, \infty) \).

Now let \( \A \succeq \B \succeq 0 \) be Hermitian and let \( \varepsilon > 0 \). Then \( \A + \varepsilon\I \succeq \B + \varepsilon\I \succ 0 \), both with spectra in \( (0, \infty) \), so \( (\A + \varepsilon\I)^2 \succeq (\B + \varepsilon\I)^2 \). Expanding both squares, that says
\[
\A^2 - \B^2 + 2\varepsilon(\A - \B) \ \succeq\ 0 .
\]
Fix \( \x \) and let \( \varepsilon \to 0^{+} \): the number \( \x^{*}(\A^2 - \B^2)\x + 2\varepsilon\,\x^{*}(\A - \B)\x \) is \( \ge 0 \) for every \( \varepsilon > 0 \), so its limit \( \x^{*}(\A^2 - \B^2)\x \) is \( \ge 0 \). Hence \( \A^2 \succeq \B^2 \) whenever \( \A \succeq \B \succeq 0 \), contradicting @exm-loewner-not-monotone. So no \( p > 1 \) works.

**Extension to \( [0, \infty) \) for \( 0 \le p \le 1 \).** Let \( \A \succeq \B \succeq 0 \) and \( \varepsilon > 0 \). As above \( \A + \varepsilon\I \succeq \B + \varepsilon\I \succ 0 \), so \( (\A + \varepsilon\I)^{p} \succeq (\B + \varepsilon\I)^{p} \). If \( \A = \sum_j\mu_j\P_j \) is the spectral resolution, then \( \A + \varepsilon\I = \sum_j(\mu_j + \varepsilon)\P_j \) is the spectral resolution of \( \A + \varepsilon\I \) (@thm-spectral-resolution-unique, as the shifted eigenvalues are still distinct), so
\[
(\A + \varepsilon\I)^{p} = \sum_j(\mu_j + \varepsilon)^{p}\P_j \ \longrightarrow\ \sum_j\mu_j^{p}\P_j = \A^{p}
\]
as \( \varepsilon \to 0^{+} \): for \( \mu_j > 0 \) this is the continuity of \( u \mapsto e^{p\log u} \) on \( (0, \infty) \) (@lem-exp-log), and for \( \mu_j = 0 \) it says \( \varepsilon^{p} \to 0 \), which holds because \( u \mapsto u^{p} \) is a strictly increasing bijection of \( [0, \infty) \) with itself, so \( \varepsilon^{p} < \eta \) as soon as \( \varepsilon < \eta^{1/p} \). The same for \( \B \). Pairing with \( \x \) and letting \( \varepsilon \to 0^{+} \) gives \( \x^{*}(\A^{p} - \B^{p})\x \ge 0 \). This proves the corollary.
:::

This pays Chapter 13 §05 and Chapter 17 §11 in full for the powers, and it is worth recording what it cost: @cor-shifted-inverse-operator-monotone from Chapter 17 §11, @lem-integral-preserves-loewner from the first part of this section, and facts (A1)–(A3). **Neither the theorem of Pick and Nevanlinna nor @thm-loewner itself was used** — Chapter 17 §11 expected the powers to arrive with Loewner's theorem, and they arrived without it. What (A7) adds is the knowledge that the representation exists for *every* operator monotone function; for the particular function \( t^{p} \) the representation was written down and verified by hand.

::: {.check}
In @thm-loewner (ii), why does the term \( s/(1+s^2) \) inside the integral play no part in the proof that \( f \) is operator monotone?
:::

::: {.solution}
Because it does not depend on \( t \). Applying the functional calculus turns it into \( \bigl(s/(1+s^2)\bigr)\I \), the same matrix for \( \A \) as for \( \B \), so it cancels in \( f(\A) - f(\B) \). Its only job is to make the integral converge: without it the integrand \( -1/(t+s) \) alone need not be integrable at \( s = \infty \) against \( \nu \), while the difference \( s/(1+s^2) - 1/(t+s) \) decays like \( s^{-2} \).
:::

## The logarithm and the exponential

::: {#cor-log-operator-monotone}
[The Logarithm Is Operator Monotone]

The function \( t \mapsto \log t \) is operator monotone on \( (0, \infty) \).
:::

::: {.idea}
The logarithm is a limit of powers: \( (t^{p} - 1)/p \to \log t \) as \( p \to 0^{+} \), because that quotient is a difference quotient for the exponential. Each \( (t^{p}-1)/p \) is an increasing affine function of an operator monotone function, and @lem-operator-monotone-limit passes to the limit.
:::

::: {.proof}
For \( 0 < p < 1 \) put \( f_p(t) = (t^{p} - 1)/p \) on \( (0, \infty) \). By @cor-power-operator-monotone, \( t \mapsto t^{p} \) is operator monotone there, and \( f_p = -\tfrac1p + \tfrac1p\,t^{p} \) with \( 1/p > 0 \), so \( f_p \) is operator monotone by @prp-operator-monotone-cone (a).

Fix \( t > 0 \). If \( t = 1 \) then \( f_p(1) = 0 = \log 1 \) for every \( p \). If \( t \ne 1 \), write \( c = \log t \ne 0 \) and \( x = pc \), so that \( t^{p} = e^{pc} = e^{x} \) by the definition of real powers (Chapter 18 §11) and
\[
f_p(t) = \frac{e^{x} - 1}{p} = c\,\frac{e^{x} - 1}{x} .
\]
As \( p \to 0^{+} \) we have \( x \to 0 \), and \( (e^{x}-1)/x \to 1 \), this being the difference quotient of \( \exp \) at \( 0 \), whose value is \( e^{0} = 1 \) (@thm-exponential-properties (b) in size \( 1 \), as recorded in the proof of @lem-exp-log). Hence \( f_p(t) \to c = \log t \).

Taking \( p = 1/k \) and letting \( k \to \infty \), @lem-operator-monotone-limit applies and \( \log \) is operator monotone on \( (0, \infty) \).
:::

::: {.remark}
The logarithm's place in @thm-loewner (ii) is as simple as it can be: \( \alpha = 0 \), \( \beta = 0 \) and \( \nu \) the ordinary length measure, so that
\[
\log t = \int_0^{\infty}\Bigl(\frac{s}{1+s^2} - \frac{1}{t+s}\Bigr)\dd s
\]
for every \( t > 0 \). To verify this, take \( 0 < \delta < R \) and use the fundamental theorem of calculus — an imported fact of one-variable calculus, quoted here and named again in the one proof that uses this representation, @cor-operator-convex-log — with the antiderivative \( \tfrac12\log(1+s^2) - \log(t+s) \), whose derivative is the integrand. The value at \( R \) is \( \log\bigl(\sqrt{1+R^2}/(t+R)\bigr) \to 0 \), and the value at \( \delta \) is \( \log\bigl(\sqrt{1+\delta^2}/(t+\delta)\bigr) \to \log(1/t) = -\log t \). The difference is \( \log t \).
:::

That representation has one more use, and it pays a debt of §08. The list of operator convex functions there stopped short of two, \( -\log t \) and \( t\log t \), because each needs an integral representation. The display above is that representation, and it settles both at once.

::: {#cor-operator-convex-log}
[Two Operator Convex Functions from the Logarithm]

The functions \( t \mapsto -\log t \) and \( t \mapsto t\log t \) are operator convex on \( (0, \infty) \).
:::

::: {.idea}
Read the representation of \( \log t \) for a fixed \( s \) instead of for a fixed \( t \). The integrand of \( -\log t \) is then \( 1/(t + s) \) plus a constant, and @thm-operator-convex-examples (d) already knows that function is operator convex; multiplying the representation through by \( t \) turns the integrand into \( -t/(t+s) \) plus an affine function, and the same clause knows \( t/(t+s) \) is operator **concave**. Either way the convexity defect is an integral of positive semidefinite matrices, which @lem-integral-preserves-loewner declares positive semidefinite.
:::

::: {.proof}
Write \( c(s) = s/(1 + s^2) \). The representation in the remark above says that for every \( t > 0 \)
\[
-\log t = \int_0^{\infty}\Bigl(\frac{1}{t+s} - c(s)\Bigr)\dd s ,
\qquad
t\log t = \int_0^{\infty}\Bigl(t\,c(s) - \frac{t}{t+s}\Bigr)\dd s ,
\]
the second display being the first multiplied by \( -t \), a constant as far as \( s \) is concerned.

Let \( \A, \B \in M_n(F) \) be Hermitian with spectra in \( (0, \infty) \), let \( \theta \in [0,1] \) and put \( \C = \theta\A + (1-\theta)\B \), whose spectrum again lies in \( (0, \infty) \), as Chapter 17 §11 checked.

**The logarithm.** Write \( \A = \sum_j\mu_j\P_j \) for the spectral resolution (@thm-spectral-resolution). Substituting the first display for each \( -\log\mu_j \) and moving the finite sum \( \sum_j(\cdot)\P_j \) inside the integral — legitimate because the integral is linear in its integrand and the \( \P_j \) do not depend on \( s \) — gives
\[
-\log\A = \int_0^{\infty}\bigl((\A + s\I)^{-1} - c(s)\I\bigr)\dd s ,
\]
where \( \sum_j\P_j = \I \) is @thm-spectral-resolution (c) and the identification of \( \sum_j(\mu_j + s)^{-1}\P_j \) with \( (\A + s\I)^{-1} \) is @def-function-of-normal-operator, exactly as in Step 1 of @thm-loewner. Every entry of the integrand is a fixed linear combination of the \( n \) convergent scalar integrals above, so the matrix integral converges. The same holds for \( \B \) and for \( \C \). Forming \( \theta(\cdot) + (1-\theta)(\cdot) - (\cdot) \), the terms \( c(s)\I \) cancel at each \( s \), and the three convergent integrals combine into one:
\[
\begin{aligned}
&\theta(-\log\A) + (1-\theta)(-\log\B) - (-\log\C) \\
&\quad = \int_0^{\infty}\bigl(\theta(\A+s\I)^{-1} + (1-\theta)(\B+s\I)^{-1} - (\C+s\I)^{-1}\bigr)\dd s .
\end{aligned}
\]
Fix \( s > 0 \) and put \( g_s(t) = 1/(t+s) \), so that \( g_s(\A) = (\A + s\I)^{-1} \) by @def-function-of-normal-operator. By @thm-operator-convex-examples (d), \( g_s \) is operator convex on \( (0, \infty) \), so the integrand is \( \theta g_s(\A) + (1-\theta)g_s(\B) - g_s(\C) \succeq 0 \). It is continuous in \( s \) on \( (0, \infty) \) and the integral converges, so @lem-integral-preserves-loewner in its improper form makes the left side \( \succeq 0 \). Since \( n \), the two matrices and \( \theta \) were arbitrary, \( -\log t \) is operator convex on \( (0, \infty) \).

**The function \( t\log t \).** Its functional calculus at \( \A \) is \( \A\log\A \), the product of \( \A \) and \( \log\A \), by @thm-functional-calculus-properties (b). The same substitution, now with the second display, gives
\[
\A\log\A = \int_0^{\infty}\bigl(c(s)\A - \A(\A + s\I)^{-1}\bigr)\dd s ,
\]
its entries again convergent, and likewise for \( \B \) and \( \C \). Forming the same combination, the terms \( c(s)\A \) contribute \( c(s)\bigl(\theta\A + (1-\theta)\B - \C\bigr) = \0 \) at each \( s \), so
\[
\begin{aligned}
&\theta\,\A\log\A + (1-\theta)\,\B\log\B - \C\log\C \\
&\quad = \int_0^{\infty}\bigl(\theta h_s(\A) + (1-\theta)h_s(\B) - h_s(\C)\bigr)\dd s ,
\end{aligned}
\]
where \( h_s(t) = -t/(t+s) \) and \( h_s(\A) = -\A(\A + s\I)^{-1} \). By @thm-operator-convex-examples (d) the function \( t/(t+s) \) is operator concave on \( (0, \infty) \), so \( h_s \) is operator convex and each integrand is \( \succeq 0 \). By @lem-integral-preserves-loewner again the left side is \( \succeq 0 \), and \( t\log t \) is operator convex on \( (0, \infty) \).
:::

Both proofs quote the fundamental theorem of calculus once, through the representation of \( \log t \) that the remark verified with it; nothing else outside Chapters 1–20 enters, and in particular @thm-pick-nevanlinna does not. With this, the two functions §08 left over are on its list.

The companion negative fact is the one Chapter 13 §05 named beside it.

::: {#exm-exp-not-monotone}
[The exponential is not operator monotone]

Show that \( t \mapsto e^{t} \) is not operator monotone on \( \nR \), and exhibit two \( 2 \times 2 \) Hermitian matrices witnessing the failure.
:::

::: {.solution}
*Order two already fails.* The exponential is infinitely differentiable, so @thm-loewner-matrix-criterion applies. Take \( t_1 = 1 \) and \( t_2 = -1 \). The divided differences (@def-divided-difference) are \( f[1,1] = e \), \( f[-1,-1] = e^{-1} \) and
\[
f[1,-1] = \frac{e - e^{-1}}{1 - (-1)} = \sinh 1 ,
\]
so the Loewner matrix and its determinant are
\[
\begin{aligned}
L_{\exp}(1, -1) &= \begin{pmatrix} e & \sinh 1 \\ \sinh 1 & e^{-1}\end{pmatrix} , \\
\det L_{\exp}(1, -1) &= 1 - (\sinh 1)^2 .
\end{aligned}
\]
Subtracting the series for \( e^{-1} \) from that for \( e \) leaves only the odd terms, so \( \sinh 1 = 1 + \tfrac{1}{3!} + \tfrac{1}{5!} + \dots > 1 \). The determinant is therefore negative, and \( L_{\exp}(1,-1) \) is not positive semidefinite. By @thm-loewner-matrix-criterion, \( \exp \) is not monotone of order \( 2 \), hence not operator monotone.

*An explicit pair.* Take
\[
\A = \begin{pmatrix} 2 & 1 \\ 1 & 0\end{pmatrix},
\qquad
\B = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} ,
\]
so that \( \A - \B = \begin{psmallmatrix}1&1\\1&1\end{psmallmatrix} \succeq 0 \) and \( \A \succeq \B \). Write \( \A = \I + \N \) with \( \N = \begin{psmallmatrix}1&1\\1&-1\end{psmallmatrix} \). Then \( \N^2 = 2\I \), so \( \N^{2m} = 2^{m}\I \) and \( \N^{2m+1} = 2^{m}\N \), and summing the series of @def-matrix-exponential in two halves,
\[
e^{\N} = (\cosh\sqrt2)\,\I + \frac{\sinh\sqrt2}{\sqrt2}\,\N .
\]
Since \( \I \) and \( \N \) commute, \( e^{\A} = e\cdot e^{\N} \) by @thm-exponential-properties (d), while \( e^{\B} = \diag(e, e^{-1}) \). Writing \( c = \cosh\sqrt2 \) and \( d = (\sinh\sqrt2)/\sqrt2 \), a direct expansion of the \( 2 \times 2 \) determinant, using \( c^2 - 2d^2 = \cosh^2\sqrt2 - \sinh^2\sqrt2 = 1 \), gives
\[
\det\bigl(e^{\A} - e^{\B}\bigr) = e^{2}(1 - c + d) + (1 - c - d) .
\]
With \( c = 2.17818\ldots \) and \( d = 1.36830\ldots \) this is \( -1.1417\ldots \), a negative number, so \( e^{\A} - e^{\B} \) has one positive and one negative eigenvalue and \( e^{\A} \not\succeq e^{\B} \).
:::

::: {.remark}
The two halves of Chapter 13 §05's "companion fact" are now both in hand: \( \log \) is operator monotone on \( (0, \infty) \) (@cor-log-operator-monotone) and \( e^{t} \) is not operator monotone (@exm-exp-not-monotone). Neither proof used @thm-pick-nevanlinna. The logarithm and the exponential are inverse to each other and increasing, which shows that operator monotonicity is not inherited by inverse functions.
:::

## Exercises

### A. Check your understanding

:::: {#exr-loewners-theorem-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State what @thm-pick-nevanlinna gives, and say which implication of @thm-loewner rests on it.
2. Explain in one sentence why an integral of positive semidefinite matrices is positive semidefinite, naming the two properties of the positive semidefinite matrices that the argument uses.
3. Decide whether the following is correct, and justify your answer: "a function that extends to an entire function of \( z \) and is increasing on \( (0, \infty) \) is operator monotone there".
4. For which real \( p \) is \( t \mapsto t^{p} \) operator monotone on \( (0, \infty) \)? Name the result and say which of its cases needed (A7).
5. Where in the proof of @thm-loewner is the hypothesis \( \beta \ge 0 \) used, and what would go wrong without it?
:::
::::

::: {.solution}
(a) It gives two things: that positivity of all the Loewner matrices of \( f \) forces \( f \) to extend analytically across the interval preserving the upper half-plane, and that such a function has the integral representation (ii); a third clause says an operator monotone function is automatically \( C^1 \). The implications (i) \( \Rightarrow \) (iii) and (iii) \( \Rightarrow \) (ii) rest on it. The implication (ii) \( \Rightarrow \) (i) does not.

(b) Every Riemann sum is a sum of non-negative multiples of the values of the integrand, and the integral is a limit of such sums: the positive semidefinite matrices are closed under non-negative combinations and closed under limits (@lem-integral-preserves-loewner).

(c) Incorrect. \( e^{t} \) is entire and increasing on \( (0, \infty) \), and is not operator monotone there: @exm-exp-not-monotone gives a witness with spectra in \( \nR \), and @exr-loewners-theorem-b3 (vi) shifts it into \( (0, \infty) \). Condition (iii) of @thm-loewner asks in addition that the upper half-plane be mapped into its closure, which \( e^{z} \) fails at \( z = 3\pi i/2 \).

(d) Exactly for \( 0 \le p \le 1 \) (@cor-power-operator-monotone). No case needed (A7): the positive cases came from @lem-power-integral and @lem-integral-preserves-loewner, and the failure for \( p > 1 \) from @lem-operator-monotone-composite together with @exm-loewner-not-monotone.

(e) In the final display of Step 1, where \( \beta\,\x^{*}(\A - \B)\x \) is asserted to be \( \ge 0 \). With \( \beta < 0 \) that term is \( \le 0 \) and can dominate: at \( n = 1 \) the function \( f(t) = \beta t \) with \( \beta < 0 \) is decreasing, hence not operator monotone (@prp-operator-monotone-increasing).
:::

### B. Practice

:::: {#exr-loewners-theorem-b1}
[B1: One matrix integral]

Let
\[
\M(t) = \begin{pmatrix} 2 + t & 1 \\ 1 & 2 - t\end{pmatrix}, \qquad t \in [-1, 1] .
\]
Show that \( \M(t) \succeq 0 \) for every \( t \in [-1,1] \), compute \( \int_{-1}^{1}\M(t)\,\dd t \), and confirm the conclusion of @lem-integral-preserves-loewner for it.
::::

::: {.solution}
\( \M(t) \) is real symmetric. Its leading entry is \( 2 + t \ge 1 > 0 \) and its determinant is \( (2+t)(2-t) - 1 = 3 - t^2 \ge 2 > 0 \) for \( \lvert t\rvert \le 1 \), so \( \M(t) \succ 0 \) by Sylvester's criterion (@thm-pd-characterizations (d)); in particular \( \M(t) \succeq 0 \).

Integrating entrywise, \( \int_{-1}^{1}(2 \pm t)\,\dd t = 4 \) since \( \int_{-1}^{1}t\,\dd t = 0 \), and \( \int_{-1}^{1}1\,\dd t = 2 \). So
\[
\int_{-1}^{1}\M(t)\,\dd t = \begin{pmatrix} 4 & 2 \\ 2 & 4\end{pmatrix} ,
\]
whose eigenvalues are \( 6 \) and \( 2 \), both positive; so it is \( \succeq 0 \) by @thm-psd-characterizations (b), as @lem-integral-preserves-loewner predicts.
:::

:::: {#exr-loewners-theorem-b2}
[B2: The constant for the square root]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( K_{1/2} = \int_0^{\infty}u^{-1/2}(1+u)^{-1}\dd u = \pi \). *Hint: substitute \( u = w^2 \).*
2. Let \( \A = \begin{psmallmatrix} 5 & 4 \\ 4 & 5\end{psmallmatrix} \). Using @lem-power-integral with \( p = \tfrac12 \), evaluate
\[
\frac{1}{\pi}\int_0^{\infty}s^{-1/2}\A(\A + s\I)^{-1}\,\dd s
\]
and check the answer against the positive square root of \( \A \).
:::
::::

::: {.solution}
(a) With \( u = w^2 \), so \( \dd u = 2w\,\dd w \) and \( u^{-1/2} = 1/w \) for \( w > 0 \), the substitution rule of one-variable calculus gives
\[
\int_0^{\infty}\frac{u^{-1/2}}{1+u}\dd u = \int_0^{\infty}\frac{1}{w}\cdot\frac{2w}{1 + w^2}\dd w = 2\int_0^{\infty}\frac{\dd w}{1+w^2} .
\]
The last integral is \( \lim_{R\to\infty}\arctan R - \arctan 0 = \pi/2 \), by the fundamental theorem of calculus with the antiderivative \( \arctan \). Hence \( K_{1/2} = \pi \). (Both calculus facts are quoted, not proved here.)

(b) \( \A \) has eigenvalues \( 9 \) and \( 1 \), with orthonormal eigenvectors \( \tfrac{1}{\sqrt2}(1,1) \) and \( \tfrac{1}{\sqrt2}(1,-1) \), so its spectral resolution is \( \A = 9\P_1 + \P_2 \) with
\[
\P_1 = \tfrac12\begin{pmatrix}1&1\\1&1\end{pmatrix},
\qquad
\P_2 = \tfrac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix} .
\]
By the computation in the proof of @cor-power-operator-monotone, the integral equals \( K_{1/2}\A^{1/2} \), so dividing by \( \pi \) gives
\[
\A^{1/2} = 9^{1/2}\P_1 + 1^{1/2}\P_2 = 3\P_1 + \P_2 = \begin{pmatrix}2&1\\1&2\end{pmatrix} .
\]
Squaring confirms it: \( \begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}^2 = \begin{psmallmatrix}5&4\\4&5\end{psmallmatrix} = \A \), and the matrix is positive definite, so it is *the* positive square root (@thm-psd-square-root).
:::

:::: {#exr-loewners-theorem-b3}
[B3: Which are operator monotone?]

Determine which of the following are operator monotone on \( (0, \infty) \). Justify your answer.

::: {.enumerate options="label=(\roman*)"}
1. \( f(t) = t^{2/3} \).
2. \( f(t) = t^{4/3} \).
3. \( f(t) = 3 + 2\log t \).
4. \( f(t) = -t^{-1/3} \).
5. \( f(t) = \log(1 + t) \).
6. \( f(t) = e^{t} \).
:::
::::

::: {.solution}
(i) Operator monotone: \( 0 \le \tfrac23 \le 1 \), so @cor-power-operator-monotone applies.

(ii) Not operator monotone: \( \tfrac43 > 1 \) (@cor-power-operator-monotone).

(iii) Operator monotone: \( \log \) is (@cor-log-operator-monotone), and \( 3 + 2\log t \) is \( \alpha + c\log t \) with \( c = 2 \ge 0 \), so @prp-operator-monotone-cone (a) applies.

(iv) Operator monotone. The function \( g(t) = t^{1/3} \) is operator monotone on \( (0, \infty) \) with \( g((0,\infty)) = (0,\infty) \), and \( h(u) = -1/u \) is operator monotone on \( (0, \infty) \) (@prp-inverse-operator-monotone); by @lem-operator-monotone-composite the composite \( h(g(t)) = -t^{-1/3} \) is operator monotone.

(v) Operator monotone. The affine map \( g(t) = t + 1 \) is operator monotone on \( (0, \infty) \) (@prp-affine-operator-monotone) with image \( (1, \infty) \subseteq (0, \infty) \), and \( \log \) is operator monotone on \( (0, \infty) \); apply @lem-operator-monotone-composite.

(vi) Not operator monotone, by @exm-exp-not-monotone. (The witness there has spectra in \( \nR \), not \( (0,\infty) \); restrict it by replacing \( \A \) and \( \B \) with \( \A + 2\I \) and \( \B + 2\I \), which are \( \succ 0 \) and satisfy \( e^{\A + 2\I} = e^{2}e^{\A} \), so the same determinant is negative after multiplication by \( e^{4} > 0 \).)
:::

### C. Going deeper

:::: {#exr-loewners-theorem-c1}
[C1: When the integral loses information]

::: {.enumerate options="label=(\alph*)"}
1. Give a continuous \( \M \colon [0,1] \to M_2(\nR) \) with every \( \M(t) \) symmetric, \( \int_0^1\M \succeq 0 \), and \( \M(t) \not\succeq 0 \) for some \( t \). Hence the converse of @lem-integral-preserves-loewner fails.
2. Prove that if \( \M \colon [a,b] \to M_n(\nC) \) is continuous with \( \M(t) \succeq 0 \) for every \( t \) and \( \int_a^b\M = \0 \), then \( \M(t) = \0 \) for every \( t \).
:::

*Hint for (b): a continuous non-negative scalar function with zero integral is zero.*
::::

::: {.solution}
(a) Take \( \M(t) = \diag(1, 2t - 1) \). It is continuous and symmetric, \( \M(0) = \diag(1,-1) \) is indefinite, and \( \int_0^1\M = \diag(1, 0) \succeq 0 \).

(b) Fix \( \x \in \nC^n \) and put \( g(t) = \x^{*}\M(t)\x \), a continuous real-valued function with \( g \ge 0 \). Because pairing passes inside the integral, \( \int_a^b g = \x^{*}\bigl(\int_a^b\M\bigr)\x = 0 \). Suppose \( g(t_0) > 0 \) for some \( t_0 \in [a,b] \). By continuity there is a subinterval \( [c,d] \subseteq [a,b] \) with \( d > c \) on which \( g \ge g(t_0)/2 \). By interval additivity, \( \int_a^b g = \int_a^c g + \int_c^d g + \int_d^b g \), with the outer terms absent if \( c = a \) or \( d = b \); each outer term is \( \ge 0 \), because \( g \ge 0 \) and so every Riemann sum over that piece is \( \ge 0 \). On \( [c, d] \) every Riemann sum of \( g \) is at least \( \tfrac12g(t_0)(d - c) \), since each tag value is at least \( \tfrac12g(t_0) \) and the interval lengths sum to \( d - c \); a non-strict inequality survives a limit, so \( \int_c^d g \) is at least that too. Hence
\[
\int_a^b g \ \ge\ \int_c^d g \ \ge\ \frac{g(t_0)}{2}(d - c) \ >\ 0 ,
\]
a contradiction. So \( g \equiv 0 \), that is \( \x^{*}\M(t)\x = 0 \) for every \( t \) and every \( \x \). A positive semidefinite matrix with \( \x^{*}\M\x = 0 \) for every \( \x \) is \( \0 \): by @thm-psd-characterizations (c) write \( \M(t) = \C^{*}\C \), so \( \norm{\C\x}^2 = 0 \) for every \( \x \), hence \( \C = \0 \).
:::

:::: {#exr-loewners-theorem-c2}
[C2: The cube, by a Loewner matrix]

::: {.enumerate options="label=(\alph*)"}
1. Write down the Loewner matrix \( L_f(t_1, t_2) \) for \( f(t) = t^3 \) and general \( t_1 \ne t_2 \), and evaluate its determinant at \( t_1 = 1 \), \( t_2 = 2 \). What does @thm-loewner-matrix-criterion conclude?
2. Do the same for \( f(t) = t^{1/2} \) at \( t_1 = 1 \), \( t_2 = 4 \), and say which result of this section the sign of the determinant illustrates.
:::
::::

::: {.solution}
(a) For \( f(t) = t^3 \) we have \( f'(t) = 3t^2 \) and, factoring the difference of cubes,
\[
f[t_1, t_2] = \frac{t_1^3 - t_2^3}{t_1 - t_2} = t_1^2 + t_1t_2 + t_2^2 ,
\]
so \( L_f(t_1,t_2) \) has diagonal \( (3t_1^2, 3t_2^2) \) and off-diagonal \( t_1^2 + t_1t_2 + t_2^2 \) (@def-loewner-matrix). At \( t_1 = 1 \), \( t_2 = 2 \) the entries are \( 3, 12 \) and \( 1 + 2 + 4 = 7 \), so
\[
\det L_f(1,2) = 3\cdot 12 - 7^2 = 36 - 49 = -13 < 0 .
\]
So \( L_f(1,2) \not\succeq 0 \), and by @thm-loewner-matrix-criterion \( t \mapsto t^3 \) is not monotone of order \( 2 \), hence not operator monotone on \( (0, \infty) \). This agrees with @cor-power-operator-monotone, since \( 3 > 1 \).

(b) For \( f(t) = t^{1/2} \), \( f'(t) = \tfrac12 t^{-1/2} \) and
\[
f[t_1,t_2] = \frac{\sqrt{t_1} - \sqrt{t_2}}{t_1 - t_2} = \frac{1}{\sqrt{t_1} + \sqrt{t_2}} .
\]
At \( t_1 = 1 \), \( t_2 = 4 \) the matrix is \( \begin{psmallmatrix} 1/2 & 1/3 \\ 1/3 & 1/4\end{psmallmatrix} \), with determinant \( \tfrac18 - \tfrac19 = \tfrac{1}{72} > 0 \) and positive diagonal, so it is positive semidefinite. That is consistent with @cor-power-operator-monotone at \( p = \tfrac12 \): an operator monotone function has all its Loewner matrices positive semidefinite, for every size and all points, and this is one instance of it.
:::

:::: {#exr-loewners-theorem-c3}
[C3: Half of the representation, by hand]

Let \( 0 < p < 1 \), let \( \A \succeq \B \succ 0 \) be Hermitian in \( M_n(F) \), and let \( 0 < \delta < R \). Put
\[
\Z(\delta, R) = \int_{\delta}^{R}s^{p-1}\bigl(\A(\A+s\I)^{-1} - \B(\B+s\I)^{-1}\bigr)\dd s .
\]

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \Z(\delta, R) \succeq 0 \) for every such \( \delta, R \), **without** any statement about improper integrals.
2. Deduce \( \A^{p} \succeq \B^{p} \) from (a) and the convergence statement of @lem-power-integral.
3. Explain why the same argument does not show \( \A^{2} \succeq \B^{2} \), by pointing at the step that fails.
:::
::::

::: {.solution}
(a) For each \( s \in [\delta, R] \), the function \( t \mapsto t/(t+s) \) is operator monotone on \( (0,\infty) \) by @cor-shifted-inverse-operator-monotone, and it sends \( \A \) to \( \A(\A+s\I)^{-1} \) and \( \B \) to \( \B(\B+s\I)^{-1} \) (@def-function-of-normal-operator). So the bracket is \( \succeq 0 \), and \( s^{p-1} > 0 \) keeps it so. The integrand is continuous on the compact interval \( [\delta, R] \), because each entry is a rational function of \( s \) with non-vanishing denominator times \( s^{p-1} \). Hence @lem-integral-preserves-loewner gives \( \Z(\delta, R) \succeq 0 \).

(b) By @lem-power-integral and the diagonalization in the proof of @cor-power-operator-monotone, \( \Z(\delta, R) \to K_p(\A^{p} - \B^{p}) \) entrywise as \( \delta \to 0^{+} \) and \( R \to \infty \). For each \( \x \), the numbers \( \x^{*}\Z(\delta,R)\x \) are \( \ge 0 \) by (a), and a non-strict inequality survives a limit, so \( K_p\,\x^{*}(\A^{p}-\B^{p})\x \ge 0 \); as \( K_p > 0 \), \( \A^{p} \succeq \B^{p} \).

(c) The failure is at the very start. For \( p = 2 \) the integral \( \int_0^{\infty}s^{p-1}\lambda/(\lambda+s)\,\dd s \) diverges at \( s = \infty \): the integrand behaves like \( \lambda s^{p-2} = \lambda \), which is not integrable there. There is no representation of \( t^2 \) as a positive superposition of the functions \( t/(t+s) \) to begin with — and by @cor-power-operator-monotone there cannot be one, since \( t^2 \) is not operator monotone.
:::
