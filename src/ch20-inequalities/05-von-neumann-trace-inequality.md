# The Trace Inequality

Sections 3 and 4 built a dictionary: a unitarily invariant norm is a symmetric gauge applied to the list of singular values, and a symmetric gauge respects weak majorization. To use that dictionary we need a supply of inequalities between singular values, and the cleanest source of them is a single scalar inequality about how two matrices pair against each other. This section proves it. The pairing is the Frobenius one, \( \tr(\A^{*}\B) \), and the theorem says that it is largest when the two matrices are *aligned*: when their singular value decompositions can be written with the same unitary factors.

## How large can a pairing be?

Chapter 10 §01 made \( M_{m \times n}(F) \) an inner product space with \( \inner{\A}{\B} = \tr(\B^{*}\A) \), whose norm is the Frobenius norm \( \norm{\A}_F \). So \( \tr(\A^{*}\B) = \inner{\B}{\A} \) is an inner product of two matrices, and Cauchy–Schwarz (@thm-cauchy-schwarz) already bounds it:
\[
\lvert\tr(\A^{*}\B)\rvert \ \le\ \norm{\A}_F\,\norm{\B}_F
= \Bigl(\sum_i\sigma_i(\A)^2\Bigr)^{1/2}\Bigl(\sum_i\sigma_i(\B)^2\Bigr)^{1/2} ,
\]
using \( \norm{\A}_F^2 = \sum_i\sigma_i(\A)^2 \). That bound depends only on the two lists of singular values, which is the right kind of answer; but it is not the best one.

Here is the smallest example. Let \( \A = \diag(2, 1) \) and \( \B = \I_2 \). Then \( \tr(\A^{*}\B) = 3 \), while Cauchy–Schwarz allows \( \sqrt5\cdot\sqrt2 \approx 3.162 \). The number \( 3 \) is \( \sigma_1(\A)\sigma_1(\B) + \sigma_2(\A)\sigma_2(\B) \), the two lists of singular values multiplied **term by term in decreasing order**. That is the true bound, and the pairing \( \sum_i\sigma_i\tau_i \) is never larger than the Cauchy–Schwarz product, by Cauchy–Schwarz applied to the two lists.

*Two matrices pair as well as their singular values allow, and no better; and the best case is when the two matrices stretch the same directions by the same ranking.*

The proof takes the two singular value decompositions apart and finds, sitting between them, a square array of non-negative weights whose rows and columns each add up to at most \( 1 \). Everything then reduces to a fact about such arrays, which is worth isolating first.

## Weights that do not add up to more than one

::: {#def-doubly-substochastic}
[Doubly Substochastic Matrix]

A matrix \( \D = (d_{kl}) \in M_p(\nR) \) is **doubly substochastic** if

::: {.enumerate options="label=(S\arabic*)"}
1. \( d_{kl} \ge 0 \) for all \( k, l \);
2. \( \sum_{l=1}^{p} d_{kl} \le 1 \) for **every** row index \( k \); and
3. \( \sum_{k=1}^{p} d_{kl} \le 1 \) for **every** column index \( l \).
:::
:::

In words: the entries are non-negative, and no row and no column adds up to more than one. Replacing both "\( \le 1 \)" by "\( = 1 \)" gives the doubly stochastic matrices of @def-doubly-stochastic, so every doubly stochastic matrix is doubly substochastic, and in particular so is every permutation matrix. The zero matrix is doubly substochastic, which the stochastic condition excludes; that degenerate case matters, because it is what lets a substochastic matrix throw weight away instead of merely moving it. A non-example by minimal change: \( \begin{psmallmatrix} 1 & 1 \\ 0 & 0\end{psmallmatrix} \) satisfies (S1) and (S3) but its first row adds to \( 2 \), so (S2) fails.

The lemma we need says that such an array of weights cannot help two decreasing non-negative lists pair better than they do term by term.

::: {#lem-substochastic-pairing}
[Substochastic Pairing]

Let \( x_1 \ge \dots \ge x_p \ge 0 \) and \( y_1 \ge \dots \ge y_p \ge 0 \) be real numbers, and let \( \D \in M_p(\nR) \) be doubly substochastic. Then
\[
\sum_{k=1}^{p}\sum_{l=1}^{p} d_{kl}\,x_k y_l \ \le\ \sum_{k=1}^{p} x_k y_k .
\]
:::

::: {.idea}
Decreasing non-negative lists are non-negative combinations of the "staircase" lists \( (1, \dots, 1, 0, \dots, 0) \): write \( x_k = \sum_{i \ge k}(x_i - x_{i+1}) \). Summation by parts in both variables at once turns each side into a non-negative combination of the same coefficients, and all that is left to compare is what multiplies them: on the left a partial sum of \( \D \) over a top-left rectangle, on the right the number \( \min(i, j) \). The two substochastic conditions say exactly that an \( i \times j \) rectangle of \( \D \) holds at most \( \min(i, j) \).
:::

::: {.proof}
Put \( x_{p+1} = y_{p+1} = 0 \) and, for \( 1 \le i \le p \), write \( \Delta x_i = x_i - x_{i+1} \) and \( \Delta y_i = y_i - y_{i+1} \). These are \( \ge 0 \), since the lists are decreasing and \( x_p, y_p \ge 0 \), and telescoping gives
\[
x_k = \sum_{i=k}^{p}\Delta x_i, \qquad y_l = \sum_{j=l}^{p}\Delta y_j
\qquad (1 \le k, l \le p) .
\]
Substituting both and exchanging the order of the four finite sums,
\[
\sum_{k,l} d_{kl}x_ky_l
= \sum_{i=1}^{p}\sum_{j=1}^{p}\Delta x_i\,\Delta y_j\,S_{ij},
\qquad
S_{ij} \coloneqq \sum_{k \le i}\sum_{l \le j} d_{kl} ,
\]
because the pair \( (k, l) \) contributes to \( (i, j) \) exactly when \( k \le i \) and \( l \le j \). The same substitution with \( \D \) replaced by the identity matrix gives
\[
\sum_{k=1}^{p} x_ky_k = \sum_{i=1}^{p}\sum_{j=1}^{p}\Delta x_i\,\Delta y_j\,\min(i, j) ,
\]
since the number of \( k \le \min(i,j) \) is \( \min(i,j) \).

It remains to compare \( S_{ij} \) with \( \min(i, j) \). Summing (S2) over the \( i \) rows \( k \le i \) and discarding the non-negative entries with \( l > j \) gives \( S_{ij} \le i \); summing (S3) over the \( j \) columns \( l \le j \) gives \( S_{ij} \le j \). Hence \( S_{ij} \le \min(i, j) \) for all \( i, j \). Since every \( \Delta x_i \) and every \( \Delta y_j \) is \( \ge 0 \), replacing \( S_{ij} \) by \( \min(i,j) \) can only increase the double sum. This proves the lemma.
:::

Taking \( \D \) to be the permutation matrix of \( \pi \in S_p \) gives \( \sum_k x_ky_{\pi(k)} \le \sum_k x_ky_k \): two decreasing lists pair best when they are paired in order. That is the **rearrangement inequality**, and it is the special case that carries the meaning of the lemma. The general case allows the weights to be spread out and partly thrown away, and says that neither helps.

::: {.check}
Where does the proof use \( x_p \ge 0 \) and \( y_p \ge 0 \), rather than just the decrease? Find a doubly substochastic \( \D \) and a decreasing pair with a negative entry for which the conclusion fails.
:::

::: {.solution}
It is used to make \( \Delta x_p = x_p \) and \( \Delta y_p = y_p \) non-negative, which is what allows \( S_{ij} \) to be replaced by the larger \( \min(i,j) \) in the last step. Without it the conclusion fails: take \( p = 2 \), \( \x = (1, -1) \), \( \y = (1, 1) \) and \( \D = \diag(1, 0) \), which is doubly substochastic. The left side is \( 1 \) and the right side is \( 1 - 1 = 0 \), so the asserted inequality \( 1 \le 0 \) is false. The proof breaks at the step named: here \( \Delta x_2 = x_2 = -1 < 0 \) and \( \Delta y_2 = 1 \), so replacing \( S_{22} = 1 \) by \( \min(2,2) = 2 \) lowers the double sum instead of raising it. Throwing weight away helps when a pairing is negative, and that is exactly what non-negativity rules out.
:::

## The trace inequality

::: {#thm-von-neumann-trace}
[Von Neumann's Trace Inequality]

Let \( \A, \B \in M_{m \times n}(F) \) with \( F = \nR \) or \( \nC \), and let \( p = \min(m, n) \). Then
\[
\bigl\lvert\tr(\A^{*}\B)\bigr\rvert \ \le\ \sum_{i=1}^{p}\sigma_i(\A)\,\sigma_i(\B) .
\]
The bound is attained whenever \( \A \) and \( \B \) have **aligned** singular value decompositions, that is, whenever there are unitary \( \U \in M_m(F) \) and \( \V \in M_n(F) \) with \( \A = \U\vSigma_{\A}\V^{*} \) and \( \B = \U\vSigma_{\B}\V^{*} \), where \( \vSigma_{\A}, \vSigma_{\B} \in M_{m\times n}(F) \) carry \( \sigma_i(\A) \) and \( \sigma_i(\B) \) on the main diagonal and zeros elsewhere.
:::

::: {.idea}
Write both singular value decompositions and push the four unitary factors into two: one, \( \M \), sits between the two diagonal matrices, the other, \( \N \), closes the trace up. Multiplying out, the trace becomes \( \sum_{k,l}\sigma_k(\A)\sigma_l(\B)m_{kl}n_{lk} \): every pairing of a singular value of \( \A \) with one of \( \B \) occurs, weighted by one entry of each unitary. The weights \( \lvert m_{kl}n_{lk}\rvert \) are exactly where unitarity is spent — each row of \( \M \) and each column of \( \N \) is a unit vector, so Cauchy–Schwarz makes the weight array doubly substochastic — and @lem-substochastic-pairing finishes.
:::

::: {.proof}
Fix singular value decompositions \( \A = \U_1\vSigma_{\A}\V_1^{*} \) and \( \B = \U_2\vSigma_{\B}\V_2^{*} \) (@thm-svd), with \( \U_1, \U_2 \in M_m(F) \) and \( \V_1, \V_2 \in M_n(F) \) unitary and \( \vSigma_{\A}, \vSigma_{\B} \) as in the statement. Put
\[
\M \coloneqq \U_1^{*}\U_2 \in M_m(F), \qquad \N \coloneqq \V_2^{*}\V_1 \in M_n(F) ,
\]
both unitary, being products of unitary matrices. Then \( \A^{*}\B = \V_1\vSigma_{\A}^{*}\M\vSigma_{\B}\V_2^{*} \), so by @thm-trace-properties (3), moving the factor \( \V_1 \) to the back,
\[
\tr(\A^{*}\B) = \tr\bigl(\vSigma_{\A}^{*}\,\M\,\vSigma_{\B}\,\N\bigr) .
\]
Now compute that trace entry by entry. The matrix \( \vSigma_{\A}^{*} \in M_{n \times m}(F) \) has \( (k, a) \) entry \( \sigma_k(\A)\delta_{ka} \), which vanishes unless \( k = a \le p \), and \( \vSigma_{\B} \) has \( (b, l) \) entry \( \sigma_b(\B)\delta_{bl} \), which vanishes unless \( b = l \le p \). Hence
\[
\tr(\A^{*}\B) = \sum_{k=1}^{p}\sum_{l=1}^{p}\sigma_k(\A)\,\sigma_l(\B)\,m_{kl}\,n_{lk} ,
\]{#eq-von-neumann-weights}
all indices being in range because \( p \le m \) and \( p \le n \). By the triangle inequality,
\[
\bigl\lvert\tr(\A^{*}\B)\bigr\rvert \ \le\ \sum_{k=1}^{p}\sum_{l=1}^{p}\sigma_k(\A)\,\sigma_l(\B)\,d_{kl},
\qquad d_{kl} \coloneqq \lvert m_{kl}\rvert\,\lvert n_{lk}\rvert .
\]

::: {.claim}
\( \D = (d_{kl})_{k,l \le p} \) is doubly substochastic.

::: {.proof}
Each \( d_{kl} \ge 0 \), which is (S1). Fix \( k \le p \). By Cauchy–Schwarz (@thm-cauchy-schwarz) in \( \nR^{p} \), and then by extending both sums to their full ranges \( l \le m \) and \( l \le n \), which only adds non-negative terms,
\[
\sum_{l=1}^{p}\lvert m_{kl}\rvert\lvert n_{lk}\rvert
\le \Bigl(\sum_{l=1}^{m}\lvert m_{kl}\rvert^2\Bigr)^{1/2}
   \Bigl(\sum_{l=1}^{n}\lvert n_{lk}\rvert^2\Bigr)^{1/2} = 1 ,
\]
because row \( k \) of the unitary \( \M \) and column \( k \) of the unitary \( \N \) are unit vectors. This is (S2), and (S3) is the same computation with the roles of the two indices exchanged: column \( l \) of \( \M \) and row \( l \) of \( \N \) are unit vectors as well.
:::
:::

The lists \( \sigma_1(\A) \ge \dots \ge \sigma_p(\A) \ge 0 \) and \( \sigma_1(\B) \ge \dots \ge \sigma_p(\B) \ge 0 \) are decreasing and non-negative (@def-singular-values), so @lem-substochastic-pairing applies and gives
\[
\sum_{k,l}\sigma_k(\A)\sigma_l(\B)d_{kl} \ \le\ \sum_{k=1}^{p}\sigma_k(\A)\sigma_k(\B) ,
\]
which is the stated bound.

For the last sentence, suppose \( \A = \U\vSigma_{\A}\V^{*} \) and \( \B = \U\vSigma_{\B}\V^{*} \) with the same \( \U \) and \( \V \). Then \( \A^{*}\B = \V\vSigma_{\A}^{*}\U^{*}\U\vSigma_{\B}\V^{*} = \V\vSigma_{\A}^{*}\vSigma_{\B}\V^{*} \), and \( \vSigma_{\A}^{*}\vSigma_{\B} \) is the \( n \times n \) diagonal matrix with entries \( \sigma_i(\A)\sigma_i(\B) \) for \( i \le p \) and zeros after. Taking traces and using @thm-trace-properties (3) again, \( \tr(\A^{*}\B) = \sum_{i \le p}\sigma_i(\A)\sigma_i(\B) \). This proves the theorem.
:::

Three things about the proof are worth keeping. The weight matrix \( \D \) is where all the information about the two sets of singular directions has gone; the only thing about it that survives is a pair of inequalities. Unitarity is spent exactly once, on the unit rows and columns inside the claim, and nothing else about \( \M \) and \( \N \) is used. And the equality case shows the bound is not merely an upper bound to be improved later: it is attained for every prescribed pair of singular value lists.

::: {.warning}
The singular values are paired **in matching order**, and no other pairing gives an upper bound. For \( \A = \diag(2,1) \) and \( \B = \diag(20, 15) \) the reversed pairing is \( 2 \cdot 15 + 1 \cdot 20 = 50 \), while \( \tr(\A^{*}\B) = 40 + 15 = 55 \). What is true for every permutation \( \pi \) is the **lower** bound \( \sum_i\sigma_i(\A)\sigma_{\pi(i)}(\B) \le \sum_i\sigma_i(\A)\sigma_i(\B) \), which is the rearrangement inequality above.
:::

::: {#exm-von-neumann-two-by-two}
[A strict case and an equality case]

Let
\[
\A = \begin{pmatrix} 2 & 0 \\ 0 & 1\end{pmatrix},
\qquad
\B = \begin{pmatrix} 12 & -12 \\ 16 & 9\end{pmatrix},
\qquad
\B' = \begin{pmatrix} 20 & 0 \\ 0 & 15\end{pmatrix} .
\]
Check that \( \B \) and \( \B' \) have the same singular values, and compare the two sides of @thm-von-neumann-trace for the pairs \( (\A, \B) \) and \( (\A, \B') \).
:::

::: {.solution}
For \( \B \),
\[
\B\tp\B = \begin{pmatrix} 144 + 256 & -144 + 144 \\ -144 + 144 & 144 + 81\end{pmatrix}
= \begin{pmatrix} 400 & 0 \\ 0 & 225\end{pmatrix} ,
\]
so \( \sigma(\B) = (20, 15) \) by @def-singular-values, and \( \sigma(\B') = (20, 15) \) as well since \( \B' \) is diagonal with positive decreasing entries. Also \( \sigma(\A) = (2, 1) \). So both pairs have the same right-hand side,
\[
\sigma_1(\A)\sigma_1(\B) + \sigma_2(\A)\sigma_2(\B) = 2 \cdot 20 + 1 \cdot 15 = 55 .
\]
On the left, \( \tr(\A\tp\B') = 2 \cdot 20 + 1 \cdot 15 = 55 \): equality. And \( \tr(\A\tp\B) = 2 \cdot 12 + 1 \cdot 9 = 33 < 55 \): strict.

The reason is visible in the decompositions. Both \( \A \) and \( \B' \) are diagonal with decreasing non-negative entries, so \( \A = \I\A\I^{*} \) and \( \B' = \I\B'\I^{*} \) are aligned. For \( \B \), on the other hand, \( \B = \U_2\diag(20, 15) \) with
\[
\U_2 = \tfrac15\begin{pmatrix} 3 & -4 \\ 4 & 3\end{pmatrix} ,
\]
a rotation, so in the notation of the proof \( \M = \U_1^{*}\U_2 = \U_2 \) and \( \N = \I \). The weight matrix is \( \D = \diag(\tfrac35, \tfrac35) \), doubly substochastic and far from a permutation, and @eq-von-neumann-weights reads \( 2 \cdot 20 \cdot \tfrac35 + 1 \cdot 15 \cdot \tfrac35 = 24 + 9 = 33 \). The rotation has thrown away two fifths of each weight, and that is exactly the loss.
:::

## The dual of a unitarily invariant norm

The trace inequality is a statement about a pairing, so it is really a statement about duality. Recall the dual norm of @def-dual-norm: it measures a vector by the largest value of the pairing against vectors the given norm calls short. On matrices, the pairing to use is the Frobenius one, and the result is exactly as clean as one could hope: dualizing a unitarily invariant norm dualizes its symmetric gauge and nothing else.

::: {#cor-trace-duality}
[Duality of Unitarily Invariant Norms]

Let \( \uinorm{\cdot} \) be a unitarily invariant norm on \( M_{m\times n}(F) \) (@def-unitarily-invariant-norm) with symmetric gauge \( \Phi \) on \( \nR^{p} \), \( p = \min(m,n) \), so that \( \uinorm{\A} = \Phi(\sigma(\A)) \) (@lem-ui-norm-of-diagonal). Define
\[
\uinorm{\B}^{*} \coloneqq \max\bigl\{\lvert\tr(\B^{*}\A)\rvert \ :\ \A \in M_{m\times n}(F),\ \uinorm{\A} \le 1\bigr\} .
\]
Then \( \uinorm{\B}^{*} = \Phi^{*}(\sigma(\B)) \), where \( \Phi^{*} \) is the dual gauge of @def-dual-gauge. In particular \( \uinorm{\cdot}^{*} \) is again a unitarily invariant norm, the trace norm \( \uinorm{\cdot}_{(p)} \) of @def-ky-fan-norm and the spectral norm \( \norm{\cdot}_2 \) are dual to each other, and the Frobenius norm is self-dual.
:::

::: {.idea}
Both inequalities are one line each once the trace inequality is available. For \( \le \), bound the pairing by \( \sum_i\sigma_i(\A)\sigma_i(\B) \) and then by \( \Phi(\sigma(\A))\Phi^{*}(\sigma(\B)) \), which is what a dual norm is for. For \( \ge \), build the competitor \( \A \) out of \( \B \): take the vector where \( \Phi^{*}(\sigma(\B)) \) is attained and hang it on \( \B \)'s own singular vectors, which makes the pair aligned and turns the trace inequality into an equality.
:::

::: {.proof}
Write \( \sigma(\B) \in \nR^{p} \) for the singular value list of \( \B \), and fix a singular value decomposition \( \B = \U\vSigma_{\B}\V^{*} \) (@thm-svd).

\( (\le) \) Let \( \uinorm{\A} \le 1 \). By @thm-von-neumann-trace and then by the defining property of a dual norm (@prp-dual-norm-properties (b), applied to the norm \( \Phi \) of @def-dual-gauge), which gives \( \inner{\x}{\y} \le \Phi(\x)\Phi^{*}(\y) \) for all \( \x, \y \),
\[
\lvert\tr(\B^{*}\A)\rvert \le \sum_{i=1}^{p}\sigma_i(\A)\sigma_i(\B)
\le \Phi(\sigma(\A))\,\Phi^{*}(\sigma(\B)) = \uinorm{\A}\,\Phi^{*}(\sigma(\B))
\le \Phi^{*}(\sigma(\B)) .
\]

\( (\ge) \) By @def-dual-gauge there is \( \x \in \nR^{p} \) with \( \Phi(\x) \le 1 \) and \( \inner{\x}{\sigma(\B)} = \Phi^{*}(\sigma(\B)) \). We may assume \( x_1 \ge \dots \ge x_p \ge 0 \). Indeed, replacing each \( x_i \) by \( \lvert x_i\rvert \) leaves \( \Phi(\x) \) unchanged, by the sign invariance in @def-symmetric-gauge, and does not decrease \( \inner{\x}{\sigma(\B)} \) because every \( \sigma_i(\B) \ge 0 \); sorting the result decreasingly leaves \( \Phi \) unchanged, by the permutation invariance in @def-symmetric-gauge, and does not decrease \( \inner{\x}{\sigma(\B)} \) by the rearrangement inequality (@lem-substochastic-pairing with a permutation matrix). Since \( \Phi^{*}(\sigma(\B)) \) is by definition the largest value of \( \inner{\cdot}{\sigma(\B)} \) on \( \{\Phi \le 1\} \), the value is still exactly \( \Phi^{*}(\sigma(\B)) \). Now put
\[
\A \coloneqq \U\,\X\,\V^{*}, \qquad \X \in M_{m\times n}(F) \text{ with } (\X)_{ii} = x_i \ (i \le p)
\]
and all other entries \( 0 \). Since \( x_1 \ge \dots \ge x_p \ge 0 \), this is a singular value decomposition of \( \A \), so \( \sigma(\A) = \x \) and \( \uinorm{\A} = \Phi(\x) \le 1 \). It is aligned with the chosen decomposition of \( \B \), so the equality case of @thm-von-neumann-trace gives
\[
\lvert\tr(\B^{*}\A)\rvert = \sum_{i=1}^{p}x_i\sigma_i(\B) = \Phi^{*}(\sigma(\B)) .
\]
Hence the maximum is at least \( \Phi^{*}(\sigma(\B)) \), and the two bounds together prove the formula. (The maximum is attained, by the competitor just built.)

The remaining claims follow. By @thm-dual-gauge, \( \Phi^{*} \) is a symmetric gauge, so \( \uinorm{\cdot}^{*} \) is the unitarily invariant norm it corresponds to under @thm-von-neumann-correspondence. The trace norm is the one with \( \Phi = \norm{\cdot}_1 \) and the spectral norm the one with \( \Phi = \norm{\cdot}_\infty \), by @lem-ui-norm-of-diagonal and @thm-operator-norm-formulas (c); these gauges are dual to each other by @prp-dual-of-one-two-infinity (a), (b). The Frobenius norm has \( \Phi = \norm{\cdot}_2 \), which is self-dual by @prp-dual-of-one-two-infinity (c). This proves the corollary.
:::

So the two extreme **normalized** unitarily invariant norms of Section 4 — the smallest, \( \norm{\cdot}_2 \), and the largest, the trace norm, extreme among the normalized ones by @prp-ui-norm-properties (c) — are exchanged by duality, and the Frobenius norm sits at the fixed point in the middle. Since \( \Phi^{**} = \Phi \) (@thm-dual-gauge), dualizing twice returns the original norm.

::: {.check}
What does @cor-trace-duality say for \( \B = \e_1\e_1^{*} \), a single matrix unit, and \( \uinorm{\cdot} \) the spectral norm?
:::

::: {.solution}
Here \( \sigma(\B) = (1, 0, \dots, 0) \), and the gauge of the spectral norm is \( \norm{\cdot}_\infty \), whose dual is \( \norm{\cdot}_1 \). So \( \uinorm{\B}^{*} = \norm{(1,0,\dots,0)}_1 = 1 \): the largest value of \( \lvert\tr(\B^{*}\A)\rvert = \lvert a_{11}\rvert \) over matrices with \( \norm{\A}_2 \le 1 \) is \( 1 \), attained at \( \A = \e_1\e_1^{*} \). An entry of a matrix never exceeds its spectral norm, and for a matrix unit that is sharp.
:::

## Exercises

### A. Check your understanding

:::: {#exr-von-neumann-trace-inequality-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define a doubly substochastic matrix, and say which doubly substochastic matrices are doubly stochastic.
2. State @thm-von-neumann-trace, with its hypotheses, and say what "aligned" means.
3. Determine whether the following is true for all \( \A, \B \in M_n(\nC) \), and justify your answer: \( \lvert\tr(\A\B)\rvert \le \sum_i\sigma_i(\A)\sigma_i(\B) \).
4. Where in the proof of @thm-von-neumann-trace is the unitarity of \( \M \) and \( \N \) used, and what exactly is deduced from it?
5. Determine whether the following is true, and justify your answer: if \( \tr(\A^{*}\B) = \sum_i\sigma_i(\A)\sigma_i(\B) \) then \( \A = \B \).
:::
::::

::: {.solution}
(a) A square real matrix with non-negative entries whose every row sum and every column sum is at most \( 1 \) (@def-doubly-substochastic). It is doubly stochastic exactly when all those sums equal \( 1 \).

(b) For \( \A, \B \in M_{m\times n}(F) \) and \( p = \min(m,n) \), \( \lvert\tr(\A^{*}\B)\rvert \le \sum_{i\le p}\sigma_i(\A)\sigma_i(\B) \). The pair is aligned when there are unitary \( \U, \V \) with \( \A = \U\vSigma_{\A}\V^{*} \) and \( \B = \U\vSigma_{\B}\V^{*} \), the **same** \( \U \) and \( \V \) for both; then equality holds.

(c) True. Apply @thm-von-neumann-trace to the pair \( \A^{*} \) and \( \B \), using \( \tr(\A\B) = \tr((\A^{*})^{*}\B) \) and \( \sigma(\A^{*}) = \sigma(\A) \), which is @prp-ui-norm-properties (a).

(d) Only in the claim, and only to say that each row of \( \M \) and each column of \( \N \) is a unit vector. Cauchy–Schwarz then makes the weight array doubly substochastic. Nothing else about \( \M \) and \( \N \) is used.

(e) False. Take \( \A = \I_2 \) and \( \B = 2\I_2 \): both sides are \( 4 \), and \( \A \ne \B \). The theorem says that alignment forces equality, and \( \A \) and \( \B \) are aligned, with \( \U = \V = \I \); it says nothing that would force the two matrices to be equal.
:::

### B. Practice

:::: {#exr-von-neumann-trace-inequality-b1}
[B1: Both sides of the inequality]

Let
\[
\A = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix},
\qquad
\B = \begin{pmatrix} 0 & 4 \\ 2 & 0\end{pmatrix} .
\]
Compute \( \tr(\A\tp\B) \), the singular values of both matrices, and both sides of @thm-von-neumann-trace. Then find a matrix \( \B'' \) with the same singular values as \( \B \) for which equality holds.
::::

::: {.solution}
\( \A\tp\B = \begin{psmallmatrix} 0 & 12 \\ 2 & 0\end{psmallmatrix} \), so \( \tr(\A\tp\B) = 0 \). Since \( \A \) is diagonal with positive decreasing entries, \( \sigma(\A) = (3, 1) \). For \( \B \), \( \B\tp\B = \diag(4, 16) \), so \( \sigma(\B) = (4, 2) \). The right-hand side is \( 3 \cdot 4 + 1 \cdot 2 = 14 \), and \( 0 \le 14 \) with a lot to spare: \( \B \) sends the direction \( \A \) stretches most to the one it stretches least.

For equality, align: take \( \B'' = \diag(4, 2) \). Then \( \tr(\A\tp\B'') = 12 + 2 = 14 \), and \( \sigma(\B'') = (4,2) \).
:::

:::: {#exr-von-neumann-trace-inequality-b2}
[B2: The trace against the trace norm]

Let \( \A \in M_n(\nC) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \lvert\tr\A\rvert \le \sum_{i=1}^{n}\sigma_i(\A) \).
2. Determine all \( \A \) for which equality holds with \( \A \) positive semidefinite.
:::
::::

::: {.solution}
(a) Apply @thm-von-neumann-trace with the pair \( \I_n \) and \( \A \), in that order: \( \tr(\I^{*}\A) = \tr\A \), and \( \sigma_i(\I) = 1 \) for every \( i \), so \( \lvert\tr\A\rvert \le \sum_i 1 \cdot \sigma_i(\A) \).

(b) For \( \A \succeq 0 \) the eigenvalues are non-negative (@thm-psd-characterizations) and, by the spectral theorem, \( \A = \U\diag(\lambda_1, \dots, \lambda_n)\U^{*} \) with \( \lambda_i \ge 0 \) decreasing; this is a singular value decomposition, so \( \sigma_i(\A) = \lambda_i(\A) \). Hence \( \tr\A = \sum_i\lambda_i = \sum_i\sigma_i(\A) \) by @cor-trace-sum-eigenvalues-again: equality holds for **every** positive semidefinite \( \A \). (Consistently with the theorem, \( \I \) and such an \( \A \) are aligned, with \( \V = \U \).)
:::

:::: {#exr-von-neumann-trace-inequality-b3}
[B3: A weight matrix]

Let \( \A = \diag(5, 1) \) and let \( \B = \U\diag(2, 1)\U^{*} \) with \( \U = \tfrac1{\sqrt2}\begin{psmallmatrix} 1 & -1 \\ 1 & 1\end{psmallmatrix} \). Write down the matrices \( \M \) and \( \N \) of the proof of @thm-von-neumann-trace for this pair, the weight matrix \( \D \), and verify @eq-von-neumann-weights and the inequality numerically.
::::

::: {.solution}
Take \( \U_1 = \V_1 = \I \) for \( \A \), and \( \U_2 = \U \), \( \V_2 = \U \) for \( \B \) (the decomposition given is a singular value decomposition, since \( \diag(2,1) \) is diagonal with positive decreasing entries). Then \( \M = \U_1^{*}\U_2 = \U \) and \( \N = \V_2^{*}\V_1 = \U^{*} \), so
\[
m_{kl}n_{lk} = u_{kl}\,\conj{u_{kl}} = \lvert u_{kl}\rvert^2 = \tfrac12
\]
for all \( k, l \), and \( \D = \tfrac12\begin{psmallmatrix} 1 & 1 \\ 1 & 1\end{psmallmatrix} \), which is doubly stochastic, hence doubly substochastic. Now @eq-von-neumann-weights gives
\[
\tr(\A^{*}\B) = \tfrac12(5\cdot2 + 5\cdot1 + 1\cdot2 + 1\cdot1) = \tfrac{18}{2} = 9 ,
\]
which checks against \( \B = \tfrac12\begin{psmallmatrix} 3 & 1 \\ 1 & 3\end{psmallmatrix} \) and \( \tr(\A\B) = \tfrac12(5 \cdot 3 + 1 \cdot 3) = 9 \). The bound is \( 5\cdot2 + 1\cdot1 = 11 \), and \( 9 \le 11 \).
:::

### C. Going deeper

:::: {#exr-von-neumann-trace-inequality-c1}
[C1: The triangle inequality for the trace norm]

Write \( \uinorm{\A}_{(p)} = \sum_{i}\sigma_i(\A) \) for the trace norm of @def-ky-fan-norm, \( \A \in M_{m\times n}(\nC) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \uinorm{\A}_{(p)} = \max\{\lvert\tr(\A^{*}\Q)\rvert : \Q \in M_{m \times n}(\nC),\ \norm{\Q}_2 \le 1\} \).
2. Hence deduce that \( \uinorm{\cdot}_{(p)} \) satisfies the triangle inequality, without using @lem-singular-value-subadditive.
:::

*Hint: for (a), @cor-trace-duality with the spectral norm, read the other way round.*
::::

::: {.solution}
(a) The spectral norm is a unitarily invariant norm, and its gauge is \( \Phi = \norm{\cdot}_\infty \) (@lem-ui-norm-of-diagonal, @thm-operator-norm-formulas (c)). By @cor-trace-duality applied to that norm, the maximum in the statement equals \( \Phi^{*}(\sigma(\A)) = \norm{\sigma(\A)}_1 = \sum_i\sigma_i(\A) \), using @prp-dual-of-one-two-infinity (b).

(b) Conjugate transposition is additive, so \( \tr((\A+\B)^{*}\Q) = \tr(\A^{*}\Q) + \tr(\B^{*}\Q) \) for every \( \Q \). Given \( \A, \B \), choose by (a) a \( \Q \) with \( \norm{\Q}_2 \le 1 \) attaining the maximum for \( \A + \B \); then, by the triangle inequality for the modulus and (a) again,
\[
\uinorm{\A + \B}_{(p)} = \lvert\tr((\A+\B)^{*}\Q)\rvert
\le \lvert\tr(\A^{*}\Q)\rvert + \lvert\tr(\B^{*}\Q)\rvert
\le \uinorm{\A}_{(p)} + \uinorm{\B}_{(p)} .
\]
No step used @lem-singular-value-subadditive: the route ran through the trace inequality and duality alone.
:::

:::: {#exr-von-neumann-trace-inequality-c2}
[C2: The nearest unitary, again]

Let \( \A \in M_n(\nC) \) with polar decomposition \( \A = \W\lvert\A\rvert \) (@thm-polar-decomposition).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \max\{\operatorname{Re}\tr(\Q^{*}\A) : \Q \in M_n(\nC) \text{ unitary}\} = \sum_i\sigma_i(\A) \), attained at \( \Q = \W \).
2. Deduce @cor-unitary-nearest, that \( \W \) minimizes \( \norm{\A - \Q}_F \) over unitary \( \Q \).
:::
::::

::: {.solution}
(a) For unitary \( \Q \), \( \sigma_i(\Q) = 1 \) for every \( i \), so @thm-von-neumann-trace gives \( \operatorname{Re}\tr(\Q^{*}\A) \le \lvert\tr(\Q^{*}\A)\rvert \le \sum_i\sigma_i(\A) \). For attainment, fix a singular value decomposition \( \A = \U\vSigma\V^{*} \) and recall from the proof of @thm-polar-decomposition that \( \W = \U\V^{*} \). Then \( \W^{*}\A = \V\U^{*}\U\vSigma\V^{*} = \V\vSigma\V^{*} \), whose trace is \( \tr\vSigma = \sum_i\sigma_i(\A) \) by @thm-trace-properties (3); it is real.

(b) For unitary \( \Q \), expanding in the Frobenius inner product,
\[
\norm{\A - \Q}_F^2 = \norm{\A}_F^2 + n - 2\operatorname{Re}\tr(\Q^{*}\A) ,
\]
since \( \norm{\Q}_F^2 = \tr(\Q^{*}\Q) = n \). Only the last term depends on \( \Q \), and it enters with a minus sign, so minimizing the left side is maximizing \( \operatorname{Re}\tr(\Q^{*}\A) \). By (a) the maximum is attained at \( \Q = \W \), which is @cor-unitary-nearest.
:::
