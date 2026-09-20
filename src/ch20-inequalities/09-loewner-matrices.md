# Loewner Matrices

Chapter 16 §11 left operator monotonicity as an infinite list of conditions: one for every matrix size, each quantified over all pairs of Hermitian matrices of that size. Nothing in that list can be checked. This section replaces the condition at size \( n \) by a condition on **numbers**: a single symmetric \( n \times n \) matrix built out of \( f \) alone, at \( n \) chosen points, must be positive semidefinite. Two ingredients do the work — a formula for the derivative of \( s \mapsto f(\A + s\H) \), and the Schur product theorem of Chapter 12 §07. They are the elementary half of Loewner's theorem, and they are proved here in full.

**Throughout, \( F = \nR \) or \( F = \nC \)**, every matrix whose spectrum is named is Hermitian, and \( I \) denotes an **interval** of real numbers with more than one point. The letter \( I \) is plain italic and is not the identity matrix \( \I \). For \( f \colon I \to \nR \) and Hermitian \( \A \) with \( \spec(\A) \subseteq I \), the matrix \( f(\A) \) is the one built by the functional calculus of Chapter 11 §08 (@def-function-of-normal-operator). We write \( f \in C^1(I) \) to mean that \( f \) is differentiable on \( I \), with one-sided derivatives at any endpoint belonging to \( I \), and that \( f' \) is continuous on \( I \).

## Slopes between two points

Operator monotonicity compares \( f(\A) \) with \( f(\B) \), and the difference of two values of \( f \) is what a slope measures. Everything below is assembled from slopes.

*The divided difference of f at two points is the slope of the chord joining them, and at a repeated point it is the slope of the tangent.*

::: {#def-divided-difference}
[Divided Difference]

Let \( f \colon I \to \nR \) be differentiable. For \( s, t \in I \), the **divided difference** of \( f \) is
\[
f[s, t] \coloneqq
\begin{cases}
\dfrac{f(s) - f(t)}{s - t}, & s \ne t, \\[2mm]
f'(t), & s = t .
\end{cases}
\]
:::

In words: for two distinct points it is the slope of the chord through \( (s, f(s)) \) and \( (t, f(t)) \); the second clause is the value that makes the first one continuous as \( s \) approaches \( t \), which is exactly what the derivative is. It is symmetric, \( f[s,t] = f[t,s] \), since swapping \( s \) and \( t \) negates both numerator and denominator, and it is additive in \( f \): \( (f+g)[s,t] = f[s,t] + g[s,t] \) and \( (cf)[s,t] = c\,f[s,t] \).

**Examples.**

- \( f(t) = \alpha + \beta t \): then \( f[s,t] = \beta \) for all \( s, t \), including \( s = t \). The divided difference of an affine function is constant — it has one slope.
- \( f(t) = t^2 \): then \( f[s,t] = (s^2 - t^2)/(s-t) = s + t \) for \( s \ne t \), and \( f[t,t] = 2t = t + t \). So \( f[s,t] = s + t \) throughout.
- \( f(t) = t^k \) for \( k \ge 1 \): dividing \( s^k - t^k \) by \( s - t \) gives \( f[s,t] = \sum_{p=0}^{k-1}s^{p}t^{k-1-p} \), which at \( s = t \) reads \( kt^{k-1} = f'(t) \), so again one formula covers both clauses.
- \( f(t) = -1/t \) on \( (0, \infty) \): then \( -1/s + 1/t = (s - t)/(st) \), so \( f[s,t] = 1/(st) \), and at \( s = t \) this is \( 1/t^2 = f'(t) \).
- \( f(t) = \sqrt{t} \) on \( (0, \infty) \): rationalizing, \( (\sqrt s - \sqrt t)/(s - t) = 1/(\sqrt s + \sqrt t) \), and at \( s = t \) this is \( 1/(2\sqrt t) = f'(t) \).

**Non-example by minimal change.** Drop differentiability and keep continuity: for \( f(t) = \lvert t \rvert \) on \( \nR \) the first clause still makes sense, but \( f[0,0] \) has no value, since the chord slopes \( f[s,0] = \sgn(s) \) do not settle down as \( s \to 0 \). Differentiability fills in the diagonal; continuous differentiability makes the filled-in function continuous.

::: {#lem-divided-difference-continuous}
[Divided Differences Are Continuous]

Let \( f \in C^1(I) \). If \( (s_k) \) and \( (t_k) \) are sequences in \( I \) with \( s_k \to s_0 \in I \) and \( t_k \to t_0 \in I \), then \( f[s_k, t_k] \to f[s_0, t_0] \). In particular, for each fixed \( \alpha \in I \) the function \( t \mapsto f[\alpha, t] \) is continuous on \( I \).
:::

::: {.proof}
*Case 1: \( s_0 \ne t_0 \).* For large \( k \) we have \( s_k \ne t_k \), since \( s_k - t_k \to s_0 - t_0 \ne 0 \). So \( f[s_k, t_k] = (f(s_k) - f(t_k))/(s_k - t_k) \) for large \( k \), and the algebra of limits applies, the denominator having non-zero limit: the quotient tends to \( (f(s_0) - f(t_0))/(s_0 - t_0) = f[s_0, t_0] \), using that \( f \) is continuous because it is differentiable.

*Case 2: \( s_0 = t_0 \).* Let \( \varepsilon > 0 \). Since \( f' \) is continuous at \( t_0 \), there is \( \delta > 0 \) with \( \lvert f'(c) - f'(t_0)\rvert < \varepsilon \) for every \( c \in I \) with \( \lvert c - t_0 \rvert < \delta \). Take \( k \) large enough that \( \lvert s_k - t_0\rvert < \delta \) and \( \lvert t_k - t_0 \rvert < \delta \). If \( s_k = t_k \) then \( f[s_k,t_k] = f'(s_k) \), which is within \( \varepsilon \) of \( f'(t_0) \). If \( s_k \ne t_k \), then by the mean value theorem (A6), applied to \( f \) on the interval with endpoints \( s_k \) and \( t_k \) — an interval contained in \( I \) — there is \( c_k \) strictly between them with
\[
f[s_k, t_k] = \frac{f(s_k) - f(t_k)}{s_k - t_k} = f'(c_k) .
\]
Then \( \lvert c_k - t_0 \rvert < \delta \), so again \( \lvert f[s_k,t_k] - f'(t_0)\rvert < \varepsilon \). Since \( f[t_0,t_0] = f'(t_0) \), this proves the claim.
:::

## The Loewner matrix

Collect the slopes between all pairs drawn from a list of points, and a matrix appears.

*The Loewner matrix of f at n points is the table of all the chord slopes between them.*

::: {#def-loewner-matrix}
[Loewner Matrix]

Let \( f \colon I \to \nR \) be differentiable and let \( t_1, \dots, t_n \in I \). The **Loewner matrix** of \( f \) at these points is
\[
L_f(t_1, \dots, t_n) \coloneqq \bigl(f[t_i, t_j]\bigr)_{i,j=1}^{n} \in M_n(\nR) .
\]
:::

Every entry is real and the matrix is **symmetric**, because the divided difference is; its diagonal entries are \( f'(t_1), \dots, f'(t_n) \). A real symmetric matrix is Hermitian, so it makes sense to ask whether it is positive semidefinite — the only question this section asks about it. The points need not be distinct; if \( t_i = t_j \) then rows \( i \) and \( j \) coincide.

**Examples.** All four use the divided differences computed above.

- \( f(t) = \alpha + \beta t \): every entry is \( \beta \), so \( L_f = \beta\J \), where \( \J \) is the all-ones matrix. Since \( \J = \1\1\tp \) is positive semidefinite, \( L_f \succeq 0 \) exactly when \( \beta \ge 0 \) — which is precisely when the affine function is operator monotone, by @prp-affine-operator-monotone one way and @prp-operator-monotone-increasing the other.
- \( f(t) = -1/t \) on \( (0, \infty) \): the \( (i,j) \) entry is \( 1/(t_it_j) \), so \( L_f = \d\d\tp \) with \( \d = (1/t_1, \dots, 1/t_n) \). A matrix of the form \( \d\d\tp \) is positive semidefinite, so **every** Loewner matrix of \( -1/t \) is \( \succeq 0 \), at every \( n \). Compare @prp-inverse-operator-monotone.
- \( f(t) = -1/(t + c) \) with \( c \ge 0 \): the same computation with \( t_i + c \) in place of \( t_i \) gives the rank-one matrix with entries \( 1/((t_i+c)(t_j+c)) \), again \( \succeq 0 \). Compare @cor-shifted-inverse-operator-monotone.
- \( f(t) = \sqrt t \) on \( (0, \infty) \): the \( (i,j) \) entry is \( 1/(\sqrt{t_i} + \sqrt{t_j}) \). A matrix of the form \( (1/(x_i + x_j)) \) with \( x_i > 0 \) is called a **Cauchy matrix**.

**Non-example by minimal change.** In the first example take \( \alpha = 0 \) and \( \beta = 1 \), so that \( f(t) = t \) and \( L_f = \J \succeq 0 \). Raise the exponent from \( 1 \) to \( 2 \), and positivity is lost at once.

:::: {#exm-loewner-matrix-square}
[The Loewner Matrix of the Square]

Let \( f(t) = t^2 \) on \( [0, \infty) \) and let \( s \ne t \) be points of \( [0,\infty) \). Compute \( L_f(s, t) \) and decide whether it is positive semidefinite.
::::

::: {.solution}
Since \( f[s,t] = s + t \) and \( f'(t) = 2t \),
\[
L_f(s, t) = \begin{pmatrix} 2s & s + t \\ s + t & 2t \end{pmatrix},
\qquad
\det L_f(s,t) = 4st - (s+t)^2 = -(s - t)^2 .
\]
The determinant is a principal minor, and it is \( < 0 \) because \( s \ne t \). By @thm-psd-characterizations (e), \( L_f(s,t) \) is not positive semidefinite — it is indefinite, its determinant being negative. So the square already fails at \( n = 2 \), at **every** pair of distinct points, which is the numerical shadow of @exm-loewner-not-monotone.
:::

:::: {#exm-loewner-matrix-sqrt}
[A Cauchy Matrix]

Let \( f(t) = \sqrt t \) on \( (0, \infty) \) and take the points \( 1, 4, 9 \). Compute \( L_f(1,4,9) \) and decide whether it is positive semidefinite.
::::

::: {.solution}
The square roots are \( 1, 2, 3 \), and the \( (i,j) \) entry is \( 1/(\sqrt{t_i} + \sqrt{t_j}) \), so
\[
L_f(1, 4, 9) =
\begin{pmatrix}
\tfrac12 & \tfrac13 & \tfrac14 \\[1mm]
\tfrac13 & \tfrac14 & \tfrac15 \\[1mm]
\tfrac14 & \tfrac15 & \tfrac16
\end{pmatrix}.
\]
The first two leading principal minors are
\[
\tfrac12 \qquad\text{and}\qquad \tfrac12\cdot\tfrac14 - \bigl(\tfrac13\bigr)^2 = \tfrac18 - \tfrac19 = \tfrac{1}{72} .
\]
For the third, expand along the first row. The three minors are
\[
\tfrac{1}{24} - \tfrac{1}{25} = \tfrac{1}{600}, \qquad
\tfrac{1}{18} - \tfrac{1}{20} = \tfrac{1}{180}, \qquad
\tfrac{1}{15} - \tfrac{1}{16} = \tfrac{1}{240} ,
\]
so, with the alternating signs,
\[
\det L_f(1,4,9) = \tfrac12\cdot\tfrac{1}{600} - \tfrac13\cdot\tfrac{1}{180} + \tfrac14\cdot\tfrac{1}{240}
= \tfrac{1}{1200} - \tfrac{1}{540} + \tfrac{1}{960} .
\]
Over the common denominator \( 43200 \) the three terms are \( 36 \), \( 80 \) and \( 45 \), and \( 36 - 80 + 45 = 1 \), so \( \det L_f(1,4,9) = 1/43200 \). All three leading principal minors are positive, so \( L_f(1,4,9) \succ 0 \) by Sylvester's criterion (@thm-pd-characterizations (d)), and in particular \( \succeq 0 \).
:::

The contrast between the two examples is the point of the section: \( \sqrt t \) is operator monotone and \( t^2 \) is not, and the Loewner matrices see the difference with no matrix inequality tested. The theorem below says this is no coincidence.

::: {.warning}
**One size at a time.** A Loewner matrix is built from **one** choice of \( n \) points. Positivity for one choice says nothing about another, and positivity at all choices of \( n \) points is not by itself a statement about \( n + 1 \) points: \( f(t) = t^2 \) has \( L_f(t) = (2t) \succeq 0 \) at every point of \( [0, \infty) \), and already at two points it fails (@exm-loewner-matrix-square). The criterion below is an equivalence *size by size*: it matches the \( n \times n \) Loewner matrices with order-preservation on \( n \times n \) matrices, and operator monotonicity is the conjunction of all of these.
:::

Since the criterion works one size at a time, the property it characterizes needs a name.

::: {#def-monotone-of-order-n}
[Monotone of Order n]

Let \( n \ge 1 \) and let \( f \colon I \to \nR \). Then \( f \) is **monotone of order \( n \) on \( I \)** if, for all Hermitian \( \A, \B \in M_n(F) \) whose spectra lie in \( I \),
\[
\A \succeq \B \quad \Longrightarrow \quad f(\A) \succeq f(\B) .
\]
:::

Comparing with @def-operator-monotone (a): **\( f \) is operator monotone on \( I \) exactly when it is monotone of order \( n \) for every \( n \ge 1 \).** Order \( 1 \) is plain monotonicity (@prp-operator-monotone-increasing), and order \( 2 \) is already a strictly stronger demand: \( t \mapsto t^2 \) is increasing on \( [0, \infty) \) and fails at \( n = 2 \) (@exm-loewner-not-monotone). Whether each further order is in turn strictly stronger than the one before is not decided here.

## Differentiating a matrix function

The link between the Loewner matrix and the order is a derivative, and the derivative comes out of one exact algebraic identity. Write both matrices in their spectral resolutions, insert the identity on both sides, and the difference of the two functional calculi factors through the difference of the matrices, with divided differences as the coefficients.

::: {#lem-double-resolution-identity}
[The Two-Resolution Identity]

Let \( f \colon I \to \nR \) be differentiable and let \( \A, \B \in M_n(F) \) be Hermitian with spectra in \( I \). Write the spectral resolutions
\[
\A = \sum_{i}\alpha_i\P_i , \qquad \B = \sum_{k}\beta_k\Q_k
\]
with \( \alpha_i \) the distinct eigenvalues of \( \A \) and \( \beta_k \) those of \( \B \) (@thm-spectral-resolution). Then
\[
f(\B) - f(\A) = \sum_{i,k} f[\alpha_i, \beta_k]\;\P_i(\B - \A)\Q_k .
\]
:::

::: {.idea}
The resolutions of the identity \( \sum_i\P_i = \I \) and \( \sum_k\Q_k = \I \) can be inserted on the two sides of any matrix, which splits it into \( i \times k \) pieces. On the piece \( \P_i \,\cdot\, \Q_k \), the matrix \( \A \) acts as the number \( \alpha_i \) from the left and \( \B \) acts as \( \beta_k \) from the right. So both \( f(\B) - f(\A) \) and \( \B - \A \) become numbers on each piece, namely \( f(\beta_k) - f(\alpha_i) \) and \( \beta_k - \alpha_i \), and the ratio of those two numbers is the divided difference.
:::

::: {.proof}
By @thm-spectral-resolution (c), \( \sum_i\P_i = \I \) and \( \sum_k\Q_k = \I \). By @thm-spectral-resolution (e), \( \P_i\A = \alpha_i\P_i \) and \( \B\Q_k = \beta_k\Q_k \); and \( \P_if(\A) = f(\alpha_i)\P_i \), \( f(\B)\Q_k = f(\beta_k)\Q_k \) follow from @def-function-of-normal-operator together with @thm-spectral-resolution (b). Hence
\[
\begin{aligned}
f(\B) - f(\A) &= \sum_{i,k}\P_i\bigl(f(\B) - f(\A)\bigr)\Q_k \\
  &= \sum_{i,k}\bigl(f(\beta_k) - f(\alpha_i)\bigr)\P_i\Q_k ,
\end{aligned}
\]
and in the same way
\[
\P_i(\B - \A)\Q_k = (\beta_k - \alpha_i)\,\P_i\Q_k .
\]
Fix \( i \) and \( k \). If \( \alpha_i \ne \beta_k \), then by @def-divided-difference
\[
\bigl(f(\beta_k) - f(\alpha_i)\bigr)\P_i\Q_k
= f[\alpha_i, \beta_k](\beta_k - \alpha_i)\P_i\Q_k
= f[\alpha_i, \beta_k]\,\P_i(\B - \A)\Q_k .
\]
If \( \alpha_i = \beta_k \), then both \( f(\beta_k) - f(\alpha_i) \) and \( \beta_k - \alpha_i \) are \( 0 \), so both sides of that equation are the zero matrix and it holds as well. Summing over \( i \) and \( k \) gives the identity.
:::

The identity is exact, with no limit in it. To turn it into a derivative we let \( \B \) approach \( \A \), which needs the functional calculus to be continuous. It is, and the proof shows what a mixed pair of eigenbases is for.

::: {#lem-functional-calculus-continuous}
[Continuity of the Functional Calculus]

Let \( J = [a, b] \) be a closed bounded interval, let \( g \colon J \to \nR \) be continuous and let \( n \ge 1 \). For every \( \varepsilon > 0 \) there is \( \eta > 0 \) such that all Hermitian \( \X, \Y \in M_n(F) \) with spectra in \( J \) and \( \norm{\X - \Y}_F < \eta \) satisfy
\[
\norm{g(\X) - g(\Y)}_F < \varepsilon .
\]
:::

::: {.idea}
Diagonalize \( \X \) and \( \Y \) separately, and read both \( g(\X) - g(\Y) \) and \( \X - \Y \) in the **mixed** basis, one eigenbasis on the left and the other on the right. In that basis the two matrices have entries \( (g(a_i) - g(b_k))w_{ik} \) and \( (a_i - b_k)w_{ik} \) with the same \( w_{ik} \), so they differ only in how the scalar factor is built. Where \( a_i \) and \( b_k \) are close, continuity of \( g \) makes the first factor small; where they are far apart, the second factor is large and can pay for the first. The Frobenius norm is the right yardstick because it is computed from the entries and is unchanged by a unitary factor on either side.
:::

::: {.proof}
By the extreme value theorem (A4), \( g \) is bounded on the compact interval \( J \); let \( M = \max_{t \in J}\lvert g(t)\rvert \). If \( M = 0 \), then \( g \) is identically \( 0 \) and there is nothing to prove, so assume \( M > 0 \).

**Step 1: \( g \) is uniformly continuous on \( J \).** Suppose not. Then there is \( \varepsilon_0 > 0 \) such that for every \( k \ge 1 \) there are \( a_k, b_k \in J \) with \( \lvert a_k - b_k\rvert \le 1/k \) and \( \lvert g(a_k) - g(b_k)\rvert \ge \varepsilon_0 \). By compactness (A3), a subsequence \( a_{k_j} \) converges to some \( a \in J \); then \( b_{k_j} \to a \) too, since \( \lvert b_{k_j} - a_{k_j}\rvert \to 0 \). Continuity of \( g \) at \( a \) gives \( g(a_{k_j}) \to g(a) \) and \( g(b_{k_j}) \to g(a) \), so \( \lvert g(a_{k_j}) - g(b_{k_j})\rvert \to 0 \), contradicting the lower bound \( \varepsilon_0 \).

**Step 2: the mixed basis.** Let \( \X \) and \( \Y \) be Hermitian with spectra in \( J \). By @cor-spectral-complex-matrix over \( \nC \), or @cor-spectral-real-matrix over \( \nR \), there are unitary \( \U, \V \in M_n(F) \) whose columns \( \u_1, \dots, \u_n \) and \( \v_1, \dots, \v_n \) are orthonormal eigenbases, with \( \X\u_i = a_i\u_i \) and \( \Y\v_k = b_k\v_k \), all \( a_i, b_k \in J \). Put \( w_{ik} = \u_i^{*}\v_k \), the entries of the unitary matrix \( \W = \U^{*}\V \); then \( \sum_{i,k}\lvert w_{ik}\rvert^2 = \norm{\W}_F^2 = n \).

Write \( \X = \sum_j\mu_j\P_j \) for the spectral resolution. Exactly one \( \mu_j \) equals \( a_i \), and \( \u_i \) lies in its eigenspace, so \( \P_j\u_i = \u_i \) for that \( j \) and \( \P_j\u_i = \0 \) for the others, the eigenspaces being orthogonal (@thm-spectral-resolution (a)). Hence \( g(\X)\u_i = g(a_i)\u_i \) by @def-function-of-normal-operator, and likewise \( g(\Y)\v_k = g(b_k)\v_k \); since \( g(a_i) \) is real and \( g(\X) \) is Hermitian, also \( \u_i^{*}g(\X) = g(a_i)\u_i^{*} \). Hence the \( (i,k) \) entry of \( \U^{*}\bigl(g(\X) - g(\Y)\bigr)\V \) is
\[
\u_i^{*}\bigl(g(\X) - g(\Y)\bigr)\v_k = \bigl(g(a_i) - g(b_k)\bigr)w_{ik} ,
\]
and the same computation with \( g \) replaced by the identity function gives \( \u_i^{*}(\X - \Y)\v_k = (a_i - b_k)w_{ik} \). By @lem-frobenius-unitarily-invariant,
\[
\begin{aligned}
\norm{g(\X) - g(\Y)}_F^2 &= \sum_{i,k}\lvert g(a_i) - g(b_k)\rvert^2\lvert w_{ik}\rvert^2 , \\
\norm{\X - \Y}_F^2 &= \sum_{i,k}\lvert a_i - b_k\rvert^2\lvert w_{ik}\rvert^2 .
\end{aligned}
\]

**Step 3: the split.** Let \( \varepsilon > 0 \). By Step 1 there is \( \delta > 0 \) with \( \lvert g(a) - g(b)\rvert \le \varepsilon/(2\sqrt n) \) whenever \( a, b \in J \) and \( \lvert a - b \rvert < \delta \). Split the index pairs \( (i,k) \) into those with \( \lvert a_i - b_k\rvert < \delta \) and those with \( \lvert a_i - b_k\rvert \ge \delta \). The first group contributes at most
\[
\frac{\varepsilon^2}{4n}\sum_{i,k}\lvert w_{ik}\rvert^2 = \frac{\varepsilon^2}{4n}\cdot n = \frac{\varepsilon^2}{4} .
\]
In the second group \( \lvert g(a_i) - g(b_k)\rvert \le 2M \le (2M/\delta)\lvert a_i - b_k\rvert \), so that group contributes at most \( (2M/\delta)^2\norm{\X - \Y}_F^2 \). Therefore
\[
\norm{g(\X) - g(\Y)}_F^2 \ \le\ \frac{\varepsilon^2}{4} + \Bigl(\frac{2M}{\delta}\Bigr)^2\norm{\X - \Y}_F^2 .
\]
Take \( \eta = \varepsilon\delta/(4M) > 0 \). If \( \norm{\X - \Y}_F < \eta \), the second term is less than \( \varepsilon^2/4 \), so \( \norm{g(\X) - g(\Y)}_F^2 < \varepsilon^2/2 < \varepsilon^2 \). This proves the lemma.
:::

Now the theorem. With the two lemmas in hand it is bookkeeping.

::: {#thm-derivative-of-a-matrix-function}
[The Derivative of a Matrix Function]

Let \( f \in C^1(I) \), let \( \A, \H \in M_n(F) \) be Hermitian, and suppose there are \( s_0 > 0 \) and a closed bounded interval \( J \subseteq I \) with
\[
\spec(\A + s\H) \subseteq J \qquad\text{for every real } s \text{ with } \lvert s\rvert < s_0 .
\]
Then the matrix-valued function \( \G(s) \coloneqq f(\A + s\H) \), defined for \( \lvert s\rvert < s_0 \), is differentiable at \( s = 0 \) in the sense of @def-matrix-valued-derivative, and:

::: {.enumerate options="label=(\alph*)"}
1. If \( \A = \diag(t_1, \dots, t_n) \), then
\[
\G'(0) = L_f(t_1, \dots, t_n) \circ \H ,
\]
the Hadamard product of @def-hadamard-product.
2. In general, if \( \A = \U\D\U^{*} \) with \( \U \) unitary and \( \D = \diag(\lambda_1, \dots, \lambda_n) \), then
\[
\G'(0) = \U\Bigl(L_f(\lambda_1, \dots, \lambda_n) \circ (\U^{*}\H\U)\Bigr)\U^{*} .
\]
:::
:::

::: {.remark}
The hypothesis on \( J \) is automatic when \( I \) is **open**. Write \( I = (c, d) \) with \( -\infty \le c < d \le \infty \). Then \( c < \lambda_n(\A) \le \lambda_1(\A) < d \), so there is \( \rho > 0 \) with \( [\lambda_n(\A) - \rho, \lambda_1(\A) + \rho] \subseteq I \); taking \( s_0 = \rho/(\norm{\H}_2 + 1) \) and \( J \) that closed interval works, because \( \lvert\lambda_i(\A + s\H) - \lambda_i(\A)\rvert \le \lvert s\rvert\norm{\H}_2 < \rho \) by @cor-weyl-perturbation.
:::

::: {.idea}
Apply @lem-double-resolution-identity with \( \B = \A + s\H \). The right-hand side is a sum over pairs (eigenvalue of \( \A \), eigenvalue of \( \B \)), and the sum over the second index is nothing but a functional calculus: freezing the first argument of the divided difference turns \( f[\alpha_i, \cdot] \) into an ordinary continuous function \( g_i \), and \( \sum_k g_i(\beta_k)\Q_k \) is \( g_i(\B) \). So the identity collapses to
\[
f(\A + s\H) - f(\A) = s\sum_i \P_i\,\H\,g_i(\A + s\H) ,
\]
with the factor \( s \) already pulled out. Now let \( s \to 0 \): by @lem-functional-calculus-continuous, \( g_i(\A + s\H) \to g_i(\A) \), and the limit of the sum is the Hadamard product in disguise.
:::

::: {.proof}
Write \( \A = \sum_i\alpha_i\P_i \) for the spectral resolution, with \( \alpha_1, \dots, \alpha_r \) the distinct eigenvalues of \( \A \), and put \( \B_s = \A + s\H \), so that \( \G(s) = f(\B_s) \), for \( \lvert s\rvert < s_0 \). For each \( i \) define
\[
g_i \colon J \to \nR , \qquad g_i(x) = f[\alpha_i, x] ,
\]
which is continuous by @lem-divided-difference-continuous, since \( f \in C^1(I) \) and \( J \subseteq I \).

**Step 1: an exact formula.** Let \( \B_s = \sum_k\beta_k(s)\Q_k(s) \) be the spectral resolution of \( \B_s \). By @lem-double-resolution-identity with \( \B = \B_s \), and \( \B_s - \A = s\H \),
\[
\begin{aligned}
f(\B_s) - f(\A)
&= \sum_{i,k}f[\alpha_i, \beta_k(s)]\;\P_i(s\H)\Q_k(s) \\
&= s\sum_i\P_i\H\Bigl(\sum_k g_i(\beta_k(s))\Q_k(s)\Bigr)
 = s\sum_i\P_i\,\H\,g_i(\B_s) ,
\end{aligned}
\]
the last equality being @def-function-of-normal-operator applied to \( g_i \) and \( \B_s \), whose spectrum lies in \( J \), the domain of \( g_i \).

**Step 2: the limit.** Since \( \norm{\B_s - \A}_F = \lvert s\rvert\,\norm{\H}_F \to 0 \) as \( s \to 0 \), and since \( \A \) and every \( \B_s \) are Hermitian with spectra in \( J \), @lem-functional-calculus-continuous gives \( \norm{g_i(\B_s) - g_i(\A)}_F \to 0 \) for each \( i \). By @def-function-of-normal-operator,
\[
g_i(\A) = \sum_j g_i(\alpha_j)\P_j = \sum_j f[\alpha_i, \alpha_j]\,\P_j .
\]
Dividing the formula of Step 1 by \( s \ne 0 \) and letting \( s \to 0 \), the algebra of limits (applied entry by entry, and using \( \lvert m_{pq} \rvert \le \norm{\M}_F \) for any matrix) gives
\[
\frac{\G(s) - \G(0)}{s} \ \longrightarrow\ \sum_{i,j} f[\alpha_i, \alpha_j]\;\P_i\H\P_j .
\]
Entrywise, this says exactly that each entry of \( \G \) is differentiable at \( s = 0 \), with derivative the corresponding entry of the right-hand side. So \( \G'(0) \) exists in the sense of @def-matrix-valued-derivative and equals \( \sum_{i,j}f[\alpha_i,\alpha_j]\P_i\H\P_j \).

**Step 3: reading it as a Hadamard product.** Let \( \A = \U\D\U^{*} \) with \( \U \) unitary, \( \D = \diag(\lambda_1, \dots, \lambda_n) \), and let \( \u_1, \dots, \u_n \) be the columns of \( \U \), so \( \A\u_p = \lambda_p\u_p \). Each \( \P_i \) is the orthogonal projection onto the eigenspace of \( \alpha_i \), which is spanned by those \( \u_p \) with \( \lambda_p = \alpha_i \); hence \( \P_i = \sum_{p : \lambda_p = \alpha_i}\u_p\u_p^{*} \), and these sums partition \( \{1, \dots, n\} \). Therefore
\[
\sum_{i,j}f[\alpha_i,\alpha_j]\P_i\H\P_j
= \sum_{p,q}f[\lambda_p, \lambda_q]\,\u_p\u_p^{*}\H\u_q\u_q^{*} .
\]
Now \( \u_p^{*}\H\u_q = (\U^{*}\H\U)_{pq} \), and for any \( \M \in M_n(F) \) we have \( \U\M\U^{*} = \sum_{p,q}m_{pq}\u_p\u_q^{*} \). Taking \( \M = L_f(\lambda_1,\dots,\lambda_n) \circ (\U^{*}\H\U) \), whose \( (p,q) \) entry is \( f[\lambda_p,\lambda_q](\U^{*}\H\U)_{pq} \), the displayed sum is \( \U\M\U^{*} \). This proves (b), and (a) is the case \( \U = \I \).
:::

::: {.remark}
Two sanity checks. For \( f(t) = t \) the Loewner matrix is \( \J \), the identity for \( \circ \), and the formula returns \( \H \) — as it must, since \( f(\A + s\H) = \A + s\H \). And the diagonal entries of (a) are \( f'(t_i)h_{ii} \): to first order the \( i \)-th eigenvalue of \( \diag(t_1,\dots,t_n) + s\H \) moves by \( h_{ii} \) when the \( t_i \) are distinct (@thm-simple-eigenvalue-derivative, as computed in Chapter 19 §11), and the chain rule then moves \( f \) of it by \( f'(t_i)h_{ii} \). What the theorem adds is the **off-diagonal** part, where the eigenvectors turn, and there the chord slope \( f[t_i,t_j] \) appears in place of the tangent slope.
:::

::: {.check}
Take \( n = 2 \), \( \A = \diag(t_1, t_2) \) with \( t_1 \ne t_2 \), and \( \H = \begin{psmallmatrix} 0 & 1 \\ 1 & 0\end{psmallmatrix} \). What does @thm-derivative-of-a-matrix-function (a) predict, and what does it say about the eigenvalues of \( \A + s\H \) to first order?
:::

::: {.solution}
The Hadamard product with \( \H \) keeps only the off-diagonal entries, so the derivative is \( \begin{psmallmatrix} 0 & f[t_1,t_2] \\ f[t_1,t_2] & 0\end{psmallmatrix} \). Its diagonal is zero, which matches the eigenvalue statement: \( h_{11} = h_{22} = 0 \), so to first order neither eigenvalue of \( \A + s\H \) moves. All of the first-order change in \( f(\A + s\H) \) is in the eigenvectors, and the coefficient that measures it is the chord slope between \( t_1 \) and \( t_2 \), not a derivative.
:::

## The criterion

Everything is now in place. One direction walks along the segment from \( \B \) to \( \A \), using the Schur product theorem to keep the derivative positive semidefinite; the other reads the derivative off in a single well-chosen direction.

::: {#thm-loewner-matrix-criterion}
[Loewner's Matrix Criterion]

Let \( I \) be an interval with more than one point, let \( f \in C^1(I) \) and let \( n \ge 1 \). The following are equivalent.

::: {.enumerate options="label=(\roman*)"}
1. \( f \) is monotone of order \( n \) on \( I \).
2. \( L_f(t_1, \dots, t_n) \succeq 0 \) for all \( t_1, \dots, t_n \in I \).
:::
:::

::: {.idea}
For (ii) \( \Rightarrow \) (i): walk from \( \B \) to \( \A \) along the segment \( \B_s = \B + s(\A - \B) \), and watch the number \( \varphi(s) = \inner{f(\B_s)\x}{\x} \) for a fixed \( \x \). Its derivative is, in the eigenbasis of \( \B_s \), the quadratic form of a Hadamard product of two positive semidefinite matrices: the Loewner matrix, positive by hypothesis, and the direction \( \A - \B \), positive because \( \A \succeq \B \). The Schur product theorem says that such a product is positive semidefinite, so \( \varphi' \ge 0 \), and the mean value theorem does the rest.

For (i) \( \Rightarrow \) (ii): the derivative formula turns order-preservation into \( L_f \circ \H \succeq 0 \) for every \( \H \succeq 0 \). Choose the one \( \H \) that leaves \( L_f \) alone, namely the all-ones matrix \( \J = \1\1\tp \), which is positive semidefinite and is the identity for \( \circ \).
:::

::: {.proof}
**(ii) \( \Rightarrow \) (i).** Let \( \A, \B \in M_n(F) \) be Hermitian with spectra in \( I \) and \( \A \succeq \B \). Put \( \H = \A - \B \succeq 0 \) and \( \B_s = \B + s\H \) for \( s \in [0,1] \). For such \( s \), both \( \A - \B_s = (1-s)\H \) and \( \B_s - \B = s\H \) are \( \succeq 0 \), so \( \A \succeq \B_s \succeq \B \) and @cor-loewner-eigenvalue-monotone gives
\[
\lambda_i(\B) \ \le\ \lambda_i(\B_s) \ \le\ \lambda_i(\A) \qquad (i = 1, \dots, n) .
\]
Hence \( \spec(\B_s) \subseteq J \coloneqq [\lambda_n(\B), \lambda_1(\A)] \) for every \( s \in [0,1] \), and \( J \subseteq I \) because its two endpoints are eigenvalues of \( \B \) and of \( \A \), hence lie in \( I \), and \( I \) is an interval.

Fix \( \x \in F^n \) and put \( \varphi(s) = \inner{f(\B_s)\x}{\x} \) for \( s \in [0,1] \), a real number because \( f(\B_s) \) is Hermitian (@thm-functional-calculus-properties (c)).

*\( \varphi \) is continuous on \( [0,1] \).* We have \( \norm{\B_s - \B_{s'}}_F = \lvert s - s'\rvert\norm{\H}_F \), so @lem-functional-calculus-continuous applied to \( f \) on \( J \) makes \( s \mapsto f(\B_s) \) continuous in the Frobenius norm, and \( \lvert\inner{\M\x}{\x}\rvert \le \norm{\M}_F\norm{\x}^2 \) transfers this to \( \varphi \).

*\( \varphi'(s) \ge 0 \) for \( 0 < s < 1 \).* Fix such an \( s \) and put \( s_0 = \min(s, 1-s) > 0 \). For \( \lvert\sigma\rvert < s_0 \) we have \( \B_s + \sigma\H = \B_{s+\sigma} \) with \( s + \sigma \in (0,1) \), so its spectrum lies in \( J \). Thus @thm-derivative-of-a-matrix-function applies to the pair \( \B_s, \H \). Write \( \B_s = \U\D\U^{*} \) with \( \U \) unitary and \( \D = \diag(\lambda_1(\B_s), \dots, \lambda_n(\B_s)) \), and set
\[
\C = L_f\bigl(\lambda_1(\B_s), \dots, \lambda_n(\B_s)\bigr), \qquad \M = \U^{*}\H\U .
\]
Then \( \C \succeq 0 \) by hypothesis (ii), since the \( \lambda_i(\B_s) \) lie in \( J \subseteq I \), and \( \M \succeq 0 \) by @prp-congruence-positivity (a). By the Schur product theorem (@thm-schur-product (a)), \( \C \circ \M \succeq 0 \). A quadratic form \( \inner{\X\x}{\x} \) is a fixed linear combination of the entries of \( \X \), so an entrywise derivative of a matrix-valued function differentiates it; hence \( \varphi \) is differentiable at \( s \) with
\[
\varphi'(s) = \inner{\U(\C \circ \M)\U^{*}\x}{\x} = \inner{(\C \circ \M)\y}{\y} \ \ge\ 0 ,
\]
where \( \y = \U^{*}\x \).

*Conclusion.* Let \( 0 < a < b < 1 \). By the mean value theorem (A6) applied to \( \varphi \) on \( (0,1) \), there is \( c \) between \( a \) and \( b \) with \( \varphi(b) - \varphi(a) = \varphi'(c)(b - a) \ge 0 \). Letting \( a \to 0^{+} \) and \( b \to 1^{-} \) and using the continuity of \( \varphi \) on \( [0,1] \), we get \( \varphi(1) - \varphi(0) \ge 0 \), that is
\[
\inner{f(\A)\x}{\x} \ \ge\ \inner{f(\B)\x}{\x} .
\]
As \( \x \) was arbitrary, \( f(\A) \succeq f(\B) \) by @def-loewner-order.

**(i) \( \Rightarrow \) (ii).** Suppose first that \( t_1, \dots, t_n \) all lie in the interior of \( I \), an open interval \( (c, d) \). Put
\[
\A = \diag(t_1, \dots, t_n) , \qquad \H = \J = \1\1\tp ,
\]
so \( \H \succeq 0 \). Let \( \rho > 0 \) be small enough that \( [\min_i t_i - \rho, \max_i t_i + \rho] \subseteq (c,d) \); this is possible because \( c < \min_i t_i \le \max_i t_i < d \). Put \( s_0 = \rho/(\norm{\H}_2 + 1) \) and \( J = [\min_i t_i - \rho, \max_i t_i + \rho] \). By @cor-weyl-perturbation, \( \spec(\A + s\H) \subseteq J \subseteq I \) for \( \lvert s\rvert < s_0 \), so @thm-derivative-of-a-matrix-function applies.

For \( 0 < s < s_0 \) we have \( (\A + s\H) - \A = s\H \succeq 0 \), and both matrices have spectra in \( I \), so (i) gives \( f(\A + s\H) \succeq f(\A) \), that is
\[
\frac{f(\A + s\H) - f(\A)}{s} \ \succeq\ 0 .
\]
For each fixed \( \x \) the number \( \inner{\,\cdot\,\x}{\x} \) of the left-hand side is \( \ge 0 \), and it converges as \( s \to 0^{+} \) to the quadratic form of the derivative, by @thm-derivative-of-a-matrix-function (a); a non-strict inequality survives a limit, so the derivative is \( \succeq 0 \). But the derivative is \( L_f(t_1,\dots,t_n) \circ \J = L_f(t_1, \dots, t_n) \), because every entry of \( \J \) is \( 1 \), so \( \J \) is the identity for the Hadamard product (@def-hadamard-product). Hence \( L_f(t_1,\dots,t_n) \succeq 0 \).

Now let \( t_1, \dots, t_n \) be arbitrary points of \( I \). Since \( I \) has more than one point, it has an interior point \( m \); put \( t_i^{(k)} = (1 - 1/k)t_i + (1/k)m \) for \( k \ge 1 \). Each \( t_i^{(k)} \) lies in \( I \), being a convex combination of two of its points, and it is an **interior** point: if \( (m - \varepsilon, m + \varepsilon) \subseteq I \), then every point within \( \varepsilon/k \) of \( t_i^{(k)} \) is of the form \( (1-1/k)t_i + (1/k)(m + u) \) with \( \lvert u\rvert < \varepsilon \), hence lies in \( I \). Also \( t_i^{(k)} \to t_i \). By the case just proved, \( L_f(t_1^{(k)}, \dots, t_n^{(k)}) \succeq 0 \) for every \( k \), and by @lem-divided-difference-continuous each entry converges to the corresponding entry of \( L_f(t_1,\dots,t_n) \). For each \( \x \), the quadratic forms are \( \ge 0 \) and converge to the quadratic form of \( L_f(t_1,\dots,t_n) \), which is therefore \( \ge 0 \). This proves the theorem.
:::

::: {.remark}
The hypothesis \( f \in C^1(I) \) enters in three places: it gives the diagonal entries \( f'(t_i) \) of the Loewner matrix a meaning, it makes @lem-divided-difference-continuous available, and through that lemma it supplies the continuous functions \( g_i \) that the derivative formula needs. Whether it can be dropped is not settled here: a monotone-of-order-\( n \) function is not obviously differentiable. The next section returns to that point for operator monotone functions, where the answer turns out to be yes, at the price of an imported theorem.
:::

Taking \( n = 1 \) recovers @prp-operator-monotone-increasing: \( L_f(t) = (f'(t)) \), so monotone of order \( 1 \) means \( f' \ge 0 \), which for a \( C^1 \) function is the same as increasing, by the mean value theorem (A6). The first genuinely new case is \( n = 2 \), and there the criterion is two inequalities about numbers.

::: {#cor-monotone-order-two}
[The Criterion at Order Two]

Let \( I \) be an interval with more than one point and let \( f \in C^1(I) \). Then \( f \) is monotone of order \( 2 \) on \( I \) if and only if
\[
f'(t) \ge 0 \ \text{ for all } t \in I ,
\qquad\text{and}\qquad
f[s,t]^2 \le f'(s)f'(t) \ \text{ for all } s, t \in I .
\]
:::

::: {.proof}
By @thm-loewner-matrix-criterion with \( n = 2 \), monotonicity of order \( 2 \) is equivalent to \( L_f(s,t) \succeq 0 \) for all \( s, t \in I \). The matrix
\[
L_f(s,t) = \begin{pmatrix} f'(s) & f[s,t] \\ f[s,t] & f'(t)\end{pmatrix}
\]
is real symmetric, and its principal minors are the two diagonal entries \( f'(s), f'(t) \) and the determinant \( f'(s)f'(t) - f[s,t]^2 \). By @thm-psd-characterizations (e), \( L_f(s,t) \succeq 0 \) if and only if all three are \( \ge 0 \). Ranging over all \( s, t \in I \), these are exactly the two displayed conditions; the case \( s = t \) of the second is the tautology \( f'(t)^2 \le f'(t)^2 \).
:::

In words: **\( f \) increases, and the slope of every chord is at most the geometric mean of the slopes of the tangents at its ends.** Three of Chapter 16 §11's examples can now be re-derived, and its non-example refuted, without touching a matrix.

- \( f(t) = -1/t \) on \( (0,\infty) \): \( f'(t) = 1/t^2 \ge 0 \), and \( f[s,t] = 1/(st) \), so \( f[s,t]^2 = 1/(s^2t^2) = f'(s)f'(t) \). The condition holds with **equality** everywhere, which is the numerical form of the fact that \( L_f \) has rank one.
- \( f(t) = \sqrt t \) on \( (0, \infty) \): \( f'(t) = 1/(2\sqrt t) \ge 0 \), and \( f[s,t] = 1/(\sqrt s + \sqrt t) \), so
\[
f'(s)f'(t) - f[s,t]^2 = \frac{(\sqrt s + \sqrt t)^2 - 4\sqrt{st}}{4\sqrt{st}\,(\sqrt s + \sqrt t)^2}
= \frac{(\sqrt s - \sqrt t)^2}{4\sqrt{st}\,(\sqrt s + \sqrt t)^2} \ \ge\ 0 .
\]
- \( f(t) = \alpha + \beta t \): \( f' = \beta \) and \( f[s,t] = \beta \), so the conditions are \( \beta \ge 0 \) and \( \beta^2 \le \beta^2 \).
- \( f(t) = t^2 \) on \( [0,\infty) \): \( f' = 2t \ge 0 \), but \( f[s,t]^2 - f'(s)f'(t) = (s+t)^2 - 4st = (s-t)^2 > 0 \) for \( s \ne t \). So \( t^2 \) is **not** monotone of order \( 2 \), and therefore not operator monotone. This is @exm-loewner-not-monotone again, now with the failure located at every pair of distinct points rather than at one pair of matrices.

::: {.warning}
**Order two is not "increasing and concave".** The second condition of @cor-monotone-order-two looks like a concavity statement and is not one, in either direction. The function \( f(t) = t - t^2/2 \) on \( (0,1) \) is increasing (\( f' = 1 - t > 0 \)) and concave, yet
\[
f'(s)f'(t) - f[s,t]^2 = (1-s)(1-t) - \Bigl(1 - \frac{s+t}{2}\Bigr)^2 = st - \Bigl(\frac{s+t}{2}\Bigr)^2 ,
\]
which equals \( -\bigl((s-t)/2\bigr)^2 \), negative for \( s \ne t \); so \( f \) is not monotone of order \( 2 \). In the other direction, \( g(t) = -\log(1 - t) \) on \( (0,1) \) is increasing and **convex** and *is* monotone of order \( 2 \). Writing \( a = 1 - s \) and \( b = 1 - t \), so that \( s - t = b - a \), we have \( g'(s)g'(t) = 1/(ab) \) and \( g[s,t] = (\log b - \log a)/(b - a) \), so the second condition reads
\[
(\log b - \log a)^2 \ \le\ \frac{(b - a)^2}{ab} ,
\]
an inequality about the logarithm alone; @exr-loewner-matrices-c2 proves it.
:::

## What this gives, and what it does not

The criterion is an equivalence, so it reads either way. Right to left it manufactures operator monotone functions: exhibit positive semidefinite Loewner matrices at every order and the function preserves the order at every size. Left to right it refutes them cheaply, since one bad pair of points kills order \( 2 \) and hence operator monotonicity.

What it does not give is the classification. The conditions "\( L_f(t_1,\dots,t_n) \succeq 0 \) for all \( n \) and all points" are still infinitely many, and turning them into the integral representation of @thm-loewner-statement is the analytic half of Loewner's theorem — the business of the next section, and the one place where the chapter spends an imported theorem. What is proved here needs no analysis beyond three items of the chapter's list: the mean value theorem (A6), which turns a non-negative derivative into monotonicity along the segment; and, inside @lem-functional-calculus-continuous, the extreme value theorem (A4), which bounds \( g \), and the compactness of a closed bounded interval (A3), which makes \( g \) uniformly continuous.

## Exercises

### A. Check your understanding

:::: {#exr-loewner-matrices-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define \( f[s,t] \) for \( s = t \), and say what hypothesis on \( f \) the definition needs.
2. Write down \( L_f(t_1, t_2, t_3) \) in terms of divided differences, and say why it is Hermitian.
3. State @thm-loewner-matrix-criterion, and say which of its two directions uses the Schur product theorem.
4. Decide whether the following is correct, and justify your answer: if \( L_f(t_1, t_2) \succeq 0 \) for all \( t_1, t_2 \in I \), then \( f \) is operator monotone on \( I \).
5. What does @thm-derivative-of-a-matrix-function give when \( \H \) is diagonal?
:::
::::

::: {.solution}
(a) \( f[t,t] = f'(t) \) (@def-divided-difference); the definition needs \( f \) to be differentiable on \( I \), and the continuity statement @lem-divided-difference-continuous needs \( f' \) continuous as well.

(b) It is the \( 3 \times 3 \) matrix whose \( (i,j) \) entry is \( f[t_i,t_j] \), with diagonal \( f'(t_1), f'(t_2), f'(t_3) \). It is real and symmetric, because \( f \) is real-valued and \( f[s,t] = f[t,s] \); a real symmetric matrix is Hermitian.

(c) For \( f \in C^1(I) \) and \( n \ge 1 \): \( f \) is monotone of order \( n \) on \( I \) if and only if \( L_f(t_1,\dots,t_n) \succeq 0 \) for all \( t_1, \dots, t_n \in I \). The Schur product theorem (@thm-schur-product) is used in the direction (ii) \( \Rightarrow \) (i), to show that the derivative along the segment is positive semidefinite.

(d) Incorrect. Positivity of all \( 2 \times 2 \) Loewner matrices gives monotonicity of order \( 2 \) only (@cor-monotone-order-two); operator monotonicity demands every order. The warning after @exm-loewner-matrix-sqrt makes the point, and @def-operator-monotone (a) quantifies over all \( n \).

(e) If \( \H = \diag(h_1, \dots, h_n) \) and \( \A = \diag(t_1,\dots,t_n) \), then \( L_f \circ \H \) is the diagonal matrix \( \diag(f'(t_1)h_1, \dots, f'(t_n)h_n) \): the two matrices commute, the problem is scalar in each coordinate, and the answer is the ordinary chain rule \( n \) times.
:::

### B. Practice

:::: {#exr-loewner-matrices-b1}
[B1: Loewner matrices by hand]

Compute \( L_f(1, 2) \) for each of the following, and determine whether it is positive semidefinite. Justify your answer.

::: {.enumerate options="label=(\roman*)"}
1. \( f(t) = 4 + 3t \) on \( \nR \).
2. \( f(t) = t^2 \) on \( (0, \infty) \).
3. \( f(t) = -1/t \) on \( (0, \infty) \).
4. \( f(t) = \sqrt t \) on \( (0, \infty) \), at the points \( 1 \) and \( 4 \) instead.
:::
::::

::: {.solution}
(i) Every entry is \( 3 \), so \( L_f(1,2) = 3\J = \begin{psmallmatrix} 3 & 3 \\ 3 & 3\end{psmallmatrix} \). Its principal minors are \( 3, 3 \) and \( 0 \), all \( \ge 0 \), so it is \( \succeq 0 \) (@thm-psd-characterizations (e)).

(ii) \( f'(t) = 2t \) and \( f[1,2] = 3 \), so \( L_f(1,2) = \begin{psmallmatrix} 2 & 3 \\ 3 & 4\end{psmallmatrix} \), with determinant \( 8 - 9 = -1 < 0 \). Not positive semidefinite.

(iii) \( f'(t) = 1/t^2 \) and \( f[1,2] = 1/2 \), so \( L_f(1,2) = \begin{psmallmatrix} 1 & 1/2 \\ 1/2 & 1/4\end{psmallmatrix} \), with determinant \( \tfrac14 - \tfrac14 = 0 \) and diagonal entries \( > 0 \). Positive semidefinite, of rank one; indeed it is \( \d\d\tp \) with \( \d = (1, \tfrac12) \).

(iv) \( f'(t) = 1/(2\sqrt t) \) and \( f[1,4] = 1/(1+2) = \tfrac13 \), so \( L_f(1,4) = \begin{psmallmatrix} 1/2 & 1/3 \\ 1/3 & 1/4\end{psmallmatrix} \), with determinant \( \tfrac18 - \tfrac19 = \tfrac{1}{72} > 0 \) and positive diagonal. Positive definite, and in particular \( \succeq 0 \); it is the top-left corner of the matrix of @exm-loewner-matrix-sqrt.
:::

:::: {#exr-loewner-matrices-b2}
[B2: A derivative, two ways]

Let \( \A = \diag(1, 4) \), let \( \H = \begin{psmallmatrix} 1 & 2 \\ 2 & 3\end{psmallmatrix} \) and let \( f(t) = t^2 \) on \( (0, \infty) \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( L_f(1,4) \circ \H \).
2. Expand \( (\A + s\H)^2 \) and differentiate at \( s = 0 \) directly. Check that the two answers agree.
:::
::::

::: {.solution}
(a) \( L_f(1,4) = \begin{psmallmatrix} 2 & 5 \\ 5 & 8 \end{psmallmatrix} \), so
\[
L_f(1,4) \circ \H = \begin{pmatrix} 2\cdot 1 & 5\cdot 2 \\ 5\cdot 2 & 8\cdot 3\end{pmatrix} = \begin{pmatrix} 2 & 10 \\ 10 & 24 \end{pmatrix} .
\]

(b) \( (\A + s\H)^2 = \A^2 + s(\A\H + \H\A) + s^2\H^2 \), so the derivative at \( s = 0 \) is \( \A\H + \H\A \). Now
\[
\A\H = \begin{pmatrix} 1 & 2 \\ 8 & 12\end{pmatrix}, \qquad
\H\A = \begin{pmatrix} 1 & 8 \\ 2 & 12 \end{pmatrix},
\qquad
\A\H + \H\A = \begin{pmatrix} 2 & 10 \\ 10 & 24\end{pmatrix} ,
\]
which agrees with (a). In general \( (\A\H + \H\A)_{ij} = (t_i + t_j)h_{ij} \) for diagonal \( \A \), and \( t_i + t_j \) is exactly the divided difference of \( t^2 \).
:::

:::: {#exr-loewner-matrices-b3}
[B3: Refuting order two]

For each function, use @cor-monotone-order-two to decide whether it is monotone of order \( 2 \) on the interval given. Justify your answer.

::: {.enumerate options="label=(\roman*)"}
1. \( f(t) = t/(t+1) \) on \( (0, \infty) \).
2. \( f(t) = t^{2} - 6t \) on \( (0, 1) \).
3. \( f(t) = 2t - 1/t \) on \( (0, \infty) \).
4. \( f(t) = t + t^{2} \) on \( (0, \infty) \).
:::
::::

::: {.solution}
(i) Monotone of order \( 2 \). Here \( f(t) = 1 - 1/(t+1) \), so \( f'(t) = 1/(t+1)^2 \ge 0 \) and, by the computation for \( -1/(t+c) \) with \( c = 1 \), \( f[s,t] = 1/((s+1)(t+1)) \). Hence \( f[s,t]^2 = f'(s)f'(t) \), with equality. (In fact the Loewner matrices of every order are rank one and \( \succeq 0 \), which recovers @cor-shifted-inverse-operator-monotone.)

(ii) Not monotone of order \( 2 \) — indeed it fails already at order \( 1 \), since \( f'(t) = 2t - 6 < 0 \) on \( (0,1) \), so the first condition fails.

(iii) Monotone of order \( 2 \). Here \( f' (t)= 2 + 1/t^2 > 0 \) and \( f[s,t] = 2 + 1/(st) \), by additivity of divided differences and the two computations after @def-divided-difference. So
\[
f'(s)f'(t) - f[s,t]^2 = \frac{2}{s^2} + \frac{2}{t^2} - \frac{4}{st} = 2\Bigl(\frac1s - \frac1t\Bigr)^2 \ \ge\ 0 ,
\]
the terms \( 4 \) and \( 1/(s^2t^2) \) canceling between the two products.

(iv) Not monotone of order \( 2 \). Here \( f'(t) = 1 + 2t > 0 \) and \( f[s,t] = 1 + s + t \), so
\[
\begin{aligned}
f'(s)f'(t) - f[s,t]^2 &= (1 + 2s)(1+2t) - (1 + s + t)^2 \\
 &= 4st - (s+t)^2 = -(s-t)^2 ,
\end{aligned}
\]
which is \( < 0 \) for \( s \ne t \). Adding the operator monotone function \( t \) to the non-monotone \( t^2 \) does not repair it.
:::

### C. Going deeper

:::: {#exr-loewner-matrices-c1}
[C1: Powers, directly]

Let \( k \ge 1 \), let \( \A = \diag(t_1, \dots, t_n) \) and let \( \H \in M_n(F) \) be Hermitian.

::: {.enumerate options="label=(\alph*)"}
1. Expand \( (\A + s\H)^{k} \) and show that the coefficient of \( s \) is \( \sum_{p+q = k-1}\A^{p}\H\A^{q} \), the sum being over integers \( p, q \ge 0 \).
2. Compute the \( (i,j) \) entry of that matrix and identify it with \( f[t_i,t_j]h_{ij} \) for \( f(t) = t^{k} \).
3. Hence prove @thm-derivative-of-a-matrix-function (a) for every polynomial \( f \), without using @lem-functional-calculus-continuous.
:::
::::

::: {.solution}
(a) Expanding the product \( (\A + s\H)(\A + s\H)\cdots(\A + s\H) \) of \( k \) factors and keeping the order of every product, the terms are indexed by the choice of \( \A \) or \( s\H \) in each factor. The terms with no \( \H \) give \( \A^k \); the terms with exactly one \( \H \), in position \( p + 1 \), give \( s\,\A^{p}\H\A^{k-1-p} \) for \( p = 0, \dots, k-1 \); the remaining terms carry a factor \( s^{m} \) with \( m \ge 2 \). So
\[
(\A + s\H)^{k} = \A^{k} + s\sum_{p+q=k-1}\A^{p}\H\A^{q} + s^2\R(s)
\]
with \( \R \) a matrix whose entries are polynomials in \( s \).

(b) Since \( \A^{p} = \diag(t_1^{p}, \dots, t_n^{p}) \), the matrix \( \A^{p}\H\A^{q} \) has \( (i,j) \) entry \( t_i^{p}h_{ij}t_j^{q} \). Summing,
\[
\Bigl(\sum_{p+q=k-1}\A^{p}\H\A^{q}\Bigr)_{ij} = h_{ij}\sum_{p=0}^{k-1}t_i^{p}t_j^{k-1-p} = h_{ij}\,f[t_i,t_j] ,
\]
the last equality by the third example after @def-divided-difference, which covers \( t_i = t_j \) as well.

(c) Each entry of \( (\A + s\H)^{k} \) is a polynomial in \( s \), so it is differentiable at \( s = 0 \), and by (a) and (b) its derivative there is \( f[t_i,t_j]h_{ij} \), that is, the \( (i,j) \) entry of \( L_f(t_1,\dots,t_n) \circ \H \). By @thm-functional-calculus-properties (a) the functional calculus of \( t^{k} \) is the \( k \)-th power, so this is the assertion for \( f(t) = t^{k} \). For a general polynomial \( f = \sum_k c_kt^{k} \), both \( \A \mapsto f(\A) \) and \( f \mapsto L_f \) are linear in \( f \) (@thm-functional-calculus-properties (b) and the additivity of divided differences), so the identity for the powers gives it for \( f \).
:::

:::: {#exr-loewner-matrices-c2}
[C2: The logarithm at order two]

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( r - 1/r - 2\log r \ge 0 \) for every \( r \ge 1 \).
2. Deduce that \( \log \) is monotone of order \( 2 \) on \( (0, \infty) \).
3. Deduce that \( f(t) = -\log(1 - t) \) is monotone of order \( 2 \) on \( (0,1) \), and verify that \( f \) is convex there.
:::

*Hint for (a): differentiate, and recognize a square.*
::::

::: {.solution}
(a) Let \( h(r) = r - 1/r - 2\log r \) on \( [1, \infty) \). Then \( h(1) = 0 \) and, for \( r > 0 \),
\[
h'(r) = 1 + \frac{1}{r^2} - \frac{2}{r} = \Bigl(1 - \frac1r\Bigr)^2 \ \ge\ 0 .
\]
For \( r > 1 \), the mean value theorem (A6) gives \( h(r) - h(1) = h'(c)(r-1) \) for some \( c \in (1,r) \), and both factors are \( \ge 0 \). Hence \( h(r) \ge 0 \).

(b) By @cor-monotone-order-two with \( f = \log \) we must check \( f'(t) = 1/t \ge 0 \), which holds on \( (0,\infty) \), and
\[
\Bigl(\frac{\log s - \log t}{s - t}\Bigr)^2 \ \le\ \frac{1}{st} \qquad (s \ne t) ,
\]
the case \( s = t \) being the tautology. Both sides are unchanged by swapping \( s \) and \( t \), so assume \( s > t > 0 \) and write \( s = tr^2 \) with \( r > 1 \). Then \( \log s - \log t = 2\log r \), while
\[
\frac{s - t}{\sqrt{st}} = \frac{t(r^2 - 1)}{tr} = r - \frac1r .
\]
Both \( 2\log r \) and \( r - 1/r \) are \( \ge 0 \), and (a) says \( 2\log r \le r - 1/r \). Squaring the inequality between non-negative numbers gives \( (\log s - \log t)^2 \le (s-t)^2/(st) \), which is the required inequality after dividing by \( (s-t)^2 > 0 \).

(c) Put \( a = 1 - s \) and \( b = 1 - t \) for \( s, t \in (0,1) \), so \( a, b \in (0,1) \) and \( s - t = b - a \). Then \( f'(t) = 1/(1-t) \), so \( f'(s)f'(t) = 1/(ab) \), and
\[
f[s,t] = \frac{-\log(1-s) + \log(1-t)}{s-t} = \frac{\log b - \log a}{b - a} ,
\]
which is the divided difference of \( \log \) at \( a \) and \( b \). By (b) its square is at most \( 1/(ab) = f'(s)f'(t) \), and \( f' > 0 \), so @cor-monotone-order-two applies. Finally \( f''(t) = 1/(1-t)^2 > 0 \), so \( f \) is convex on \( (0,1) \) by @thm-convex-second-derivative. So an increasing **convex** function can be monotone of order \( 2 \).
:::

:::: {#exr-loewner-matrices-c3}
[C3: Orders are nested]

Let \( 1 \le m \le n \) and let \( f \colon I \to \nR \); in (b) and (c) assume in addition that \( f \in C^1(I) \), so that the Loewner matrices are defined and @thm-loewner-matrix-criterion applies.

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( f \) is monotone of order \( n \) on \( I \), then it is monotone of order \( m \) on \( I \).
2. Give the corresponding statement about Loewner matrices, and prove it directly from @def-loewner-matrix, without using @thm-loewner-matrix-criterion.
3. Explain why (a) and (b) together mean that a single failing pair of points rules out operator monotonicity at every order \( n \ge 2 \).
:::

*Hint for (a): pad with a scalar block.*
::::

::: {.solution}
(a) Let \( \A, \B \in M_m(F) \) be Hermitian with spectra in \( I \), \( \A \succeq \B \). Fix \( c \in I \) and put
\[
\widetilde{\A} = \A \oplus c\I_{n-m}, \qquad \widetilde{\B} = \B \oplus c\I_{n-m} ,
\]
both Hermitian in \( M_n(F) \) with spectra in \( I \). Their difference is \( (\A - \B) \oplus \0 \), whose quadratic form at \( (\x, \y) \) is \( \inner{(\A-\B)\x}{\x} \ge 0 \), so \( \widetilde{\A} \succeq \widetilde{\B} \). By hypothesis \( f(\widetilde{\A}) \succeq f(\widetilde{\B}) \). By @lem-functional-calculus-conjugation (c), \( f(\widetilde{\A}) = f(\A) \oplus f(c)\I_{n-m} \) and likewise for \( \B \), so the difference is \( (f(\A) - f(\B)) \oplus \0 \). Evaluating its quadratic form at \( (\x, \0) \) gives \( \inner{(f(\A)-f(\B))\x}{\x} \ge 0 \) for every \( \x \in F^m \), that is \( f(\A) \succeq f(\B) \).

(b) If \( L_f(t_1,\dots,t_n) \succeq 0 \) for all \( t_1, \dots, t_n \in I \), then \( L_f(t_1,\dots,t_m) \succeq 0 \) for all \( t_1, \dots, t_m \in I \). Indeed, given \( t_1, \dots, t_m \), pad the list with any \( t_{m+1}, \dots, t_n \in I \); then \( L_f(t_1,\dots,t_m) \) is the leading principal \( m \times m \) submatrix of \( L_f(t_1,\dots,t_n) \), because the \( (i,j) \) entry of each is \( f[t_i,t_j] \) for \( i, j \le m \). A principal submatrix of a positive semidefinite matrix is positive semidefinite, since its quadratic form is the quadratic form of the big matrix at vectors supported on those coordinates (compare the proof of @thm-psd-characterizations).

(c) By (b), a pair \( s, t \in I \) with \( L_f(s,t) \not\succeq 0 \) forces \( L_f(t_1,\dots,t_n) \not\succeq 0 \) for the padded list at every \( n \ge 2 \), so by @thm-loewner-matrix-criterion \( f \) is monotone of no order \( n \ge 2 \). Equivalently, by (a), failure at order \( 2 \) propagates upward — which is why @cor-monotone-order-two is the cheapest refutation available.
:::
