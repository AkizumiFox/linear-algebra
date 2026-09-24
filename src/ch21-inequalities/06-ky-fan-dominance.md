# Ky Fan Dominance

Three earlier chapters have deferred the same kind of statement to this one: that a matrix is closest to another in **every** unitarily invariant norm at once. Such a statement looks like infinitely many theorems, one for each norm. This section shows that it is one theorem about singular values, and that it can be tested on a short finite list of norms. Then it collects the debts.

## One weak majorization, every norm

Section 3 proved that a symmetric gauge respects weak majorization, and Section 4 matched the gauges with the unitarily invariant norms. Put together, they say that a weak majorization of singular values forces an inequality of norms. What is new here is the **converse**: nothing else forces it, and the Ky Fan \( k \)-norms already see everything.

*To compare two matrices in every unitarily invariant norm, compare the running totals of their singular values.*

::: {#thm-ky-fan-dominance}
[Ky Fan Dominance Theorem]

Let \( \A, \B \in M_{m \times n}(F) \) with \( F = \nR \) or \( \nC \), and let \( p = \min(m, n) \). The following are equivalent.

::: {.enumerate options="label=(\alph*)"}
1. \( \sigma(\A) \prec_w \sigma(\B) \), that is, \( \sum_{i \le k}\sigma_i(\A) \le \sum_{i \le k}\sigma_i(\B) \) for every \( k = 1, \dots, p \).
2. \( \uinorm{\A} \le \uinorm{\B} \) for **every** unitarily invariant norm \( \uinorm{\cdot} \) on \( M_{m\times n}(F) \).
:::
:::

::: {.idea}
(a) \( \Rightarrow \) (b) is the dictionary of Sections 3 and 4 read in one direction: a unitarily invariant norm is a symmetric gauge evaluated at the singular values, and a symmetric gauge is monotone under weak majorization of non-negative vectors. For (b) \( \Rightarrow \) (a) we need, for each \( k \), a unitarily invariant norm that computes the \( k \)-th running total. The Ky Fan \( k \)-norm is exactly that, so the \( p \) inequalities in (a) are \( p \) of the infinitely many inequalities in (b).
:::

::: {.proof}
(a) \( \Rightarrow \) (b). Let \( \uinorm{\cdot} \) be a unitarily invariant norm and let \( \Phi \) be its symmetric gauge, so that \( \uinorm{\M} = \Phi(\sigma(\M)) \) for every \( \M \) (@thm-von-neumann-correspondence). The vectors \( \sigma(\A) \) and \( \sigma(\B) \) have non-negative entries (@def-singular-values), so @thm-gauge-monotone-under-majorization (b) applies to the hypothesis \( \sigma(\A) \prec_w \sigma(\B) \) and gives \( \Phi(\sigma(\A)) \le \Phi(\sigma(\B)) \), which is \( \uinorm{\A} \le \uinorm{\B} \).

(b) \( \Rightarrow \) (a). Fix \( k \in \{1, \dots, p\} \). Section 3's \( k \)-th Ky Fan gauge \( \Phi_k(\x) = \sum_{i\le k}\lvert x\rvert^{\downarrow}_i \) (@def-ky-fan-gauge) is a symmetric gauge function, so by @thm-von-neumann-correspondence
\[
\uinorm{\M}_{(k)} \coloneqq \Phi_k(\sigma(\M)) = \sum_{i=1}^{k}\sigma_i(\M)
\]
is a unitarily invariant norm on \( M_{m\times n}(F) \) — the Ky Fan \( k \)-norm of @def-ky-fan-norm — the second equality holding because \( \sigma(\M) \) is already non-negative and decreasing, so that its \( k \) largest absolute values are its first \( k \) entries. Applying (b) to this one norm gives
\[
\sum_{i=1}^{k}\sigma_i(\A) \ \le\ \sum_{i=1}^{k}\sigma_i(\B) .
\]
As \( k \) was arbitrary and both lists are decreasing, this is (a), by @def-majorization. This proves the theorem.
:::

The theorem is a translation device, and it will be used in one direction almost every time: to prove an inequality for every unitarily invariant norm, produce the weak majorization. Note also what it says about testing: the condition "for every unitarily invariant norm" is equivalent to "for the \( p \) Ky Fan norms", so a statement quantified over an infinite family of norms is decided by finitely many numbers.

::: {.warning}
One norm is never enough. For \( \A = \diag(1, 1) \) and \( \B = \diag(1, 0) \) the spectral norms agree, \( \norm{\A}_2 = \norm{\B}_2 = 1 \), yet \( \sigma(\A) = (1,1) \) is not weakly majorized by \( \sigma(\B) = (1, 0) \), and indeed the trace norms are \( 2 \) and \( 1 \). Dominance needs **all** the running totals, and it compares matrices of the **same size**, since otherwise the two sides are norms on different spaces.
:::

::: {.check}
Let \( \A, \B \in M_{m\times n}(F) \) satisfy \( \sigma_i(\A) \le \sigma_i(\B) \) for every \( i \). Does \( \uinorm{\A} \le \uinorm{\B} \) hold for every unitarily invariant norm?
:::

::: {.solution}
Yes. Entrywise domination of two decreasing non-negative lists gives \( \sum_{i\le k}\sigma_i(\A) \le \sum_{i\le k}\sigma_i(\B) \) for every \( k \), which is \( \sigma(\A) \prec_w \sigma(\B) \); now apply @thm-ky-fan-dominance. The converse fails: \( \sigma(\A) = (1,1) \) and \( \sigma(\B) = (2, 0) \) satisfy \( \sigma(\A) \prec_w \sigma(\B) \) with \( \sigma_2(\A) > \sigma_2(\B) \).
:::

## Low-rank approximation in every unitarily invariant norm

Chapter 13 §10 proved that the truncated singular value decomposition \( \A_k \) is the best rank-\( k \) approximation in the Frobenius norm, and Chapter 17 §09 proved the same for the spectral norm. Both promised more. Chapter 13 §10 said that the two statements are "instances of one theorem: \( \A_k \) is a best rank-\( k \) approximation in **every** unitarily invariant norm", and predicted the shape of the proof: "it needs inequalities between the singular values of \( \A \) and of \( \A - \B \), not a projection argument". Chapter 16 §08 recorded the same debt — "The version covering every unitarily invariant norm at once is Chapter 21's" — and Chapter 17 §09 said that the common minimizer "is optimal in every unitarily invariant norm at once, which is Chapter 21's theorem". Here it is, by the predicted route.

::: {#cor-eckart-young-ui}
[Eckart–Young Theorem in Every Unitarily Invariant Norm]

Let \( \A \in M_{m\times n}(F) \) with singular values \( \sigma_1 \ge \dots \ge \sigma_p \), \( p = \min(m,n) \), let \( 0 \le k \le p \), and let \( \A_k \) be a truncation of @def-truncated-svd. Then for **every** \( \B \in M_{m\times n}(F) \) with \( \rank\B \le k \) and **every** unitarily invariant norm on \( M_{m\times n}(F) \),
\[
\uinorm{\A - \A_k} \ \le\ \uinorm{\A - \B} ,
\]
and the minimum value is \( \uinorm{\A - \A_k} = \Phi(\sigma_{k+1}, \dots, \sigma_p, 0, \dots, 0) \), where \( \Phi \) is the symmetric gauge of the norm.
:::

::: {.idea}
The singular values of the error \( \A - \A_k \) are the discarded \( \sigma_{k+1}, \dots, \sigma_p \), padded with zeros. For an arbitrary competitor \( \B \) of rank at most \( k \), Weyl's inequality for singular values, applied with the splitting \( \A = (\A - \B) + \B \), says that \( \B \) can shift the singular value list of \( \A \) by at most \( k \) places, because \( \sigma_{k+1}(\B) = 0 \). That is precisely \( \sigma_i(\A - \B) \ge \sigma_{k+i}(\A) \): the truncation wins index by index, which is more than dominance needs.
:::

::: {.proof}
**The error of the truncation.** Fix the singular value decomposition \( \A = \U\vSigma\V^{*} \) (@thm-svd) used to form \( \A_k = \sum_{i \le k}\sigma_i\u_i\v_i^{*} \) (@def-truncated-svd). Then
\[
\A - \A_k = \sum_{i > k}\sigma_i\u_i\v_i^{*} = \U\vSigma^{(k)}\V^{*} ,
\]
where \( \vSigma^{(k)} \) is \( \vSigma \) with its first \( k \) diagonal entries replaced by \( 0 \). Since \( \U \) and \( \V \) are unitary, \( (\A - \A_k)^{*}(\A-\A_k) = \V(\vSigma^{(k)})^{*}\vSigma^{(k)}\V^{*} \) has eigenvalues \( \sigma_{k+1}^2, \dots, \sigma_p^2 \) together with zeros, so by @def-singular-values
\[
\sigma_i(\A - \A_k) = \sigma_{k+i}(\A) \qquad (1 \le i \le p) ,
\]{#eq-truncation-error-singular-values}
with the convention \( \sigma_j(\A) = 0 \) for **every** \( j > p \). Chapter 17 §09 states it for \( p < j \le n \); we extend it here, because the indices \( k + i \) above run as far as \( 2p \), which may exceed \( n \).

**The competitor.** Let \( \rank\B \le k \). Then \( \sigma_{k+1}(\B) = 0 \), since a matrix has exactly \( \rank\B \) non-zero singular values (@thm-svd). Fix \( i \le p \). If \( i + k > n \), then \( \sigma_{k+i}(\A) = 0 \le \sigma_i(\A - \B) \) by the convention. Otherwise \( i + (k+1) - 1 = i + k \le n \), so @thm-weyl-singular-values applies to the sum \( \A = (\A - \B) + \B \) with indices \( i \) and \( k+1 \) and gives
\[
\sigma_{k+i}(\A) \ \le\ \sigma_i(\A - \B) + \sigma_{k+1}(\B) = \sigma_i(\A - \B) .
\]
Either way, with @eq-truncation-error-singular-values,
\[
\sigma_i(\A - \A_k) \ \le\ \sigma_i(\A - \B) \qquad (1 \le i \le p) .
\]
Summing the first \( k' \) of these for each \( k' \le p \) gives \( \sigma(\A - \A_k) \prec_w \sigma(\A - \B) \), so @thm-ky-fan-dominance gives \( \uinorm{\A - \A_k} \le \uinorm{\A - \B} \) for every unitarily invariant norm.

**The value.** By @thm-von-neumann-correspondence and @eq-truncation-error-singular-values, \( \uinorm{\A - \A_k} = \Phi(\sigma(\A-\A_k)) = \Phi(\sigma_{k+1}, \dots, \sigma_p, 0, \dots, 0) \). This proves the corollary.
:::

The proof gives more than was asked: the error of the truncation is smaller than that of any competitor **singular value by singular value**, not merely in every norm. Specializing \( \Phi \) recovers the two known cases — \( \Phi = \norm{\cdot}_\infty \) gives \( \sigma_{k+1} \), which is @thm-eckart-young-spectral, and \( \Phi = \norm{\cdot}_2 \) gives \( (\sum_{i>k}\sigma_i^2)^{1/2} \), which is @thm-eckart-young — and now every other norm comes with them.

::: {#exm-eckart-young-four-norms}
[One matrix, four norms]

Let
\[
\A = \begin{pmatrix} 6 & -4 & 0 \\ 8 & 3 & 0 \\ 0 & 0 & 1\end{pmatrix} \in M_3(\nR) .
\]
Find \( \A_1 \) and \( \A_2 \), and tabulate the approximation errors in the spectral, Frobenius, trace and Ky Fan \( 2 \)-norms. Compare \( \A_1 \) with the rank-one competitor \( \C = \diag(0, 0, 1) \).
:::

::: {.solution}
Write \( \Q = \tfrac15\begin{psmallmatrix} 3 & -4 & 0 \\ 4 & 3 & 0 \\ 0 & 0 & 5\end{psmallmatrix} \), which is orthogonal, since its columns are orthonormal. Then \( \A = \Q\diag(10, 5, 1) \), so this is a singular value decomposition with \( \U = \Q \), \( \V = \I \), and \( \sigma(\A) = (10, 5, 1) \). Hence
\[
\A_1 = \begin{pmatrix} 6 & 0 & 0 \\ 8 & 0 & 0 \\ 0 & 0 & 0\end{pmatrix},
\qquad
\A_2 = \begin{pmatrix} 6 & -4 & 0 \\ 8 & 3 & 0 \\ 0 & 0 & 0\end{pmatrix} ,
\]
with errors \( \A - \A_1 = \Q\diag(0,5,1) \) and \( \A - \A_2 = \Q\diag(0,0,1) \), whose singular value lists are \( (5, 1, 0) \) and \( (1, 0, 0) \), as @eq-truncation-error-singular-values predicts.

| error measured in | \( \A - \A_1 \) | \( \A - \A_2 \) | \( \A - \C \) |
|---|---|---|---|
| spectral \( \norm{\cdot}_2 \) | \( 5 \) | \( 1 \) | \( 10 \) |
| Frobenius \( \norm{\cdot}_F \) | \( \sqrt{26} \) | \( 1 \) | \( \sqrt{125} \) |
| trace norm | \( 6 \) | \( 1 \) | \( 15 \) |
| Ky Fan \( 2 \)-norm (@def-ky-fan-norm) | \( 6 \) | \( 1 \) | \( 15 \) |

The competitor \( \C = \diag(0,0,1) \) has rank \( 1 \), and \( \A - \C = \A_2 = \Q\diag(10,5,0) \) has singular values \( (10, 5, 0) \). It loses to \( \A_1 \) in all four norms at once, as it must: \( (5,1,0) \) is dominated entry by entry by \( (10,5,0) \). Note also that the Ky Fan \( 2 \)-norm and the trace norm agree on these three errors, because each has at most two non-zero singular values.
:::

## The nearest unitary matrix

Chapter 13 §09 proved that the unitary polar factor \( \W \) of \( \A = \W\lvert\A\rvert \) is the nearest unitary matrix in the Frobenius norm (@cor-unitary-nearest) and warned: "It is true, though not proved here, that \( \W \) also minimizes the distance in every unitarily invariant norm; Chapter 21 takes up that family of norms." That is this corollary.

The proof passes through a symmetric list of the form \( (z_1, \dots, z_q, 0, \dots, 0, -z_q, \dots, -z_1) \), and has to read off its top-\( k \) sums. Section 7 meets the same list again, so we settle the counting once.

::: {#lem-symmetric-list-top-sums}
[Top Sums of a Symmetric List]

Let \( z_1, \dots, z_q \) be real numbers, let \( r \ge 0 \) be an integer, and let \( \c \in \nR^{2q+r} \) be the list
\[
\c = \bigl(z_1, \dots, z_q,\ \underbrace{0, \dots, 0}_{r},\ -z_q, \dots, -z_1\bigr) .
\]
Then for every \( k \le q \), the largest sum of \( k \) entries of \( \c \), which is the running total \( \sum_{j\le k}c^{\downarrow}_j \), equals the sum of the \( k \) largest of the numbers \( \lvert z_1\rvert, \dots, \lvert z_q\rvert \).
:::

::: {.proof}
Fix \( k \le q \). Write \( S \) for the sum of the \( k \) largest of the \( \lvert z_i\rvert \). Since the largest sum of \( k \) entries of \( \c \) is obtained by taking the \( k \) largest entries, it is \( \sum_{j\le k}c^{\downarrow}_j \), and the two descriptions agree.

\( (\ge) \) For each index \( i \), the number \( \lvert z_i\rvert \) is an entry of \( \c \): it is \( z_i \) in position \( i \) if \( z_i \ge 0 \), and \( -z_i \) in position \( 2q + r + 1 - i \) otherwise. Distinct indices \( i \) give distinct positions, so the \( k \) largest of the \( \lvert z_i\rvert \) occur at \( k \) distinct positions of \( \c \), and their sum \( S \) is one of the sums being maximized.

\( (\le) \) Let \( k \) positions be given. The entries in the middle range contribute \( 0 \), and the remaining positions belong to at most \( k \) of the indices \( i \). For one such index, the chosen positions contribute \( z_i \), or \( -z_i \), or (if both are chosen) \( 0 \), hence at most \( \lvert z_i\rvert \) in every case. So the sum of the chosen entries is at most \( \sum_{i \in J}\lvert z_i\rvert \) for a set \( J \) of at most \( k \) indices, and since every \( \lvert z_i\rvert \ge 0 \) that is at most \( S \). This proves the lemma.
:::

::: {#cor-polar-nearest-ui}
[The Polar Factor Is Nearest in Every Unitarily Invariant Norm]

Let \( \A \in M_n(\nC) \) with polar decomposition \( \A = \W\lvert\A\rvert \) (@thm-polar-decomposition). Then for every unitary \( \Q \in M_n(\nC) \) and every unitarily invariant norm on \( M_n(\nC) \),
\[
\uinorm{\A - \W} \ \le\ \uinorm{\A - \Q} .
\]
:::

::: {.idea}
Peel off \( \W \). Unitary invariance turns the comparison of \( \A - \Q \) with \( \A - \W \) into a comparison of \( \lvert\A\rvert - \U \) with \( \lvert\A\rvert - \I \), where \( \U = \W^{*}\Q \) runs over all unitary matrices: the question is why the identity is the unitary matrix closest to a positive semidefinite one. By dominance it is enough to weakly majorize singular values, and singular values of a difference of two matrices are eigenvalues of a difference of two Hermitian ones, through the dilation of Chapter 17 §09. There, Lidskii's theorem is waiting: it already says that the vector of eigenvalue shifts is majorized by the eigenvalues of the difference, and choosing the right \( k \) entries of that majorization is the whole computation.
:::

::: {.proof}
**Step 1: reduce to \( \lvert\A\rvert \) and \( \I \).** Let \( \Q \) be unitary and put \( \U \coloneqq \W^{*}\Q \), which is unitary. Then
\[
\A - \Q = \W\lvert\A\rvert - \Q = \W\bigl(\lvert\A\rvert - \W^{*}\Q\bigr) = \W(\lvert\A\rvert - \U) ,
\]
so \( \uinorm{\A - \Q} = \uinorm{\lvert\A\rvert - \U} \) by unitary invariance (@def-unitarily-invariant-norm). Taking \( \Q = \W \) gives \( \U = \I \) and \( \uinorm{\A - \W} = \uinorm{\lvert\A\rvert - \I} \). Writing \( \S = \lvert\A\rvert \succeq 0 \), it suffices to prove
\[
\uinorm{\S - \I} \le \uinorm{\S - \U} \qquad \text{for every unitary } \U .
\]
By @thm-ky-fan-dominance this is the weak majorization \( \sigma(\S - \I) \prec_w \sigma(\S - \U) \).

**Step 2: the singular values of \( \S - \I \).** Let \( t_1 \ge \dots \ge t_n \ge 0 \) be the eigenvalues of \( \S \), which are non-negative because \( \S \succeq 0 \) (@thm-psd-characterizations). The spectral theorem writes \( \S = \Y\diag(t_1, \dots, t_n)\Y^{*} \) with \( \Y \) unitary, and this is a singular value decomposition, so \( \sigma_i(\S) = t_i \). The matrix \( \S - \I \) is Hermitian with eigenvalues \( t_i - 1 \), and \( (\S - \I)^{*}(\S-\I) = (\S-\I)^2 \) has eigenvalues \( (t_i-1)^2 \), so by @def-singular-values
\[
\sigma(\S - \I) = \bigl(\lvert t_1 - 1\rvert, \dots, \lvert t_n - 1\rvert\bigr)^{\downarrow} .
\]
Write \( s_j = \sigma_j(\S - \U) \) for the numbers we must bound from below.

**Step 3: dilate.** Let \( \cH(\cdot) \) be the Hermitian dilation of @prp-hermitian-dilation. Conjugate transposition is additive, so \( \cH(\S) - \cH(\U) = \cH(\S - \U) \), and all three are Hermitian matrices in \( M_{2n}(\nC) \). By @prp-hermitian-dilation, the eigenvalues of \( \cH(\M) \) are \( \pm\sigma_i(\M) \), and since the \( \sigma_i \) are non-negative and decreasing, the decreasing list is
\[
\vlambda(\cH(\M)) = \bigl(\sigma_1(\M), \dots, \sigma_n(\M), -\sigma_n(\M), \dots, -\sigma_1(\M)\bigr) .
\]
Applied to \( \S \), to \( \U \) (all of whose singular values are \( 1 \)) and to \( \S - \U \), this gives the three lists
\[
\begin{aligned}
\vlambda(\cH(\S)) &= (t_1, \dots, t_n, -t_n, \dots, -t_1), \\
\vlambda(\cH(\U)) &= (1, \dots, 1, -1, \dots, -1), \\
\vlambda(\cH(\S - \U)) &= (s_1, \dots, s_n, -s_n, \dots, -s_1) .
\end{aligned}
\]

**Step 4: apply Lidskii's theorem.** Chapter 17 §07 proved, in the remark following @thm-lidskii-inequality, that \( \vlambda(\X) - \vlambda(\Y) \prec \vlambda(\X - \Y) \) for Hermitian \( \X, \Y \). Applied to \( \X = \cH(\S) \) and \( \Y = \cH(\U) \),
\[
\vlambda(\cH(\S)) - \vlambda(\cH(\U)) \ \prec\ \vlambda(\cH(\S - \U)) .
\]
By Step 3 the vector on the left is
\[
\d = \bigl(t_1 - 1, \dots, t_n - 1,\ -(t_n - 1), \dots, -(t_1 - 1)\bigr) \in \nR^{2n} ,
\]
which is the symmetric list of @lem-symmetric-list-top-sums with \( q = n \), \( r = 0 \) and \( z_i = t_i - 1 \). Fix \( k \le n \). By that lemma the \( k \)-th running total of \( \d^{\downarrow} \) is the sum of the \( k \) largest of the numbers \( \lvert t_i - 1\rvert \), which by Step 2 is \( \sum_{j\le k}\sigma_j(\S - \I) \). The right-hand list is decreasing with non-negative first half, so its \( k \)-th running total is \( \sum_{j\le k}s_j \). So (M1) of @def-majorization, at the index \( k \), reads
\[
\sum_{j=1}^{k}\sigma_j(\S - \I) \ \le\ \sum_{j=1}^{k}\sigma_j(\S - \U) .
\]
As this holds for every \( k \le n \), it is the weak majorization required in Step 1. This proves the corollary.
:::

The mechanism deserves a name, because Section 7 runs it again in general: **a Hermitian dilation turns a statement about singular values into one about eigenvalues**, where Lidskii's theorem applies. What was special here is that both matrices were **square**, so that their dilations had no zeros in the middle of the spectrum and no bookkeeping was needed; that one of the two was unitary is what made its dilated eigenvalue list the constant \( \pm1 \).

::: {.remark}
The inequality of @cor-polar-nearest-ui cannot be improved to \( \sigma_j(\A - \W) \le \sigma_j(\A - \Q) \) index by index. Take \( \A = \S = \diag(2, 0) \), which is positive semidefinite, so that \( \lvert\A\rvert = \A \) and \( \W = \I \) is a polar factor, and take \( \Q = \begin{psmallmatrix} 0 & 1 \\ 1 & 0\end{psmallmatrix} \). Then the matrix \( \S - \Q = \begin{psmallmatrix} 2 & -1 \\ -1 & 0\end{psmallmatrix} \) is symmetric with eigenvalues \( 1 \pm \sqrt2 \), so \( \sigma(\S - \Q) = (1 + \sqrt2, \sqrt2 - 1) \approx (2.414, 0.414) \), while \( \sigma(\S - \I) = (1, 1) \). The second singular value is smaller for \( \Q \), and only the running totals, \( 1 \le 2.414 \) and \( 2 \le 2.828 \), go the right way. So the weak majorization, and not something cruder, is what the corollary needs.
:::

## Two smaller consequences

A compression never increases a unitarily invariant norm.

::: {#cor-compression-ui}
[Compressions Are Contractions]

Let \( \A \in M_n(F) \) and let \( \P \in M_n(F) \) be an orthogonal projection. Then \( \uinorm{\P\A\P} \le \uinorm{\A} \) for every unitarily invariant norm.
:::

::: {.proof}
If \( \P = \0 \) the left side is \( \uinorm{\0} = 0 \le \uinorm{\A} \). Otherwise \( \P \) is Hermitian with eigenvalues in \( \{0, 1\} \), at least one of them equal to \( 1 \), so \( \norm{\P}_2 = 1 \) by @lem-hermitian-spectral-norm. Applying the two bounds of @prp-ui-norm-properties (b) in turn,
\[
\uinorm{\P\A\P} \le \norm{\P}_2\,\uinorm{\A\P} \le \norm{\P}_2\,\uinorm{\A}\,\norm{\P}_2 = \uinorm{\A} ,
\]
as claimed.
:::

And a negative result, about the subadditivity of singular values. Section 4 proved \( \sigma(\A + \B) \prec_w \sigma(\A) + \sigma(\B) \) (@lem-singular-value-subadditive), where the right-hand side is the entrywise sum of the two decreasing lists. The weak majorization cannot be upgraded to majorization.

::: {#exm-sum-not-majorization}
[Weak majorization is the most that holds]

Let \( \A = \diag(1, 0) \) and \( \B = \diag(-1, 0) \). Then \( \sigma(\A) = \sigma(\B) = (1, 0) \), so \( \sigma(\A) + \sigma(\B) = (2, 0) \), while \( \A + \B = \0 \) has \( \sigma(\A + \B) = (0,0) \). The totals are \( 0 \) and \( 2 \), so \( \sigma(\A+\B) \prec \sigma(\A) + \sigma(\B) \) is false, although the weak majorization holds with room to spare.
:::

The failure is not an accident of the example. Take \( \B = -\A \) for any \( \A \ne \0 \): then \( \sigma(\B) = \sigma(\A) \), so the right-hand list has total \( 2\sum_i\sigma_i(\A) > 0 \), while \( \sigma(\A + \B) = \0 \) has total \( 0 \). Cancellation destroys singular value mass, and clause (M2) of @def-majorization — equal totals — therefore fails for every non-zero \( \A \). Weak majorization is the most @lem-singular-value-subadditive can assert.

## Exercises

### A. Check your understanding

:::: {#exr-ky-fan-dominance-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State @thm-ky-fan-dominance, and say which family of norms proves the direction that is not a direct consequence of Sections 3 and 4.
2. Define the Ky Fan \( k \)-norm and say why it is a unitarily invariant norm.
3. Determine whether the following is true, and justify your answer: if \( \norm{\A}_F \le \norm{\B}_F \) and \( \norm{\A}_2 \le \norm{\B}_2 \), then \( \uinorm{\A} \le \uinorm{\B} \) for every unitarily invariant norm.
4. In the proof of @cor-eckart-young-ui, where is the hypothesis \( \rank\B \le k \) used?
5. Determine whether the following is true, and justify your answer: for \( \A \in M_n(\nC) \) invertible, the nearest unitary matrix in the trace norm is the same as the nearest one in the Frobenius norm.
:::
::::

::: {.solution}
(a) For \( \A, \B \) of the same size, \( \sigma(\A) \prec_w \sigma(\B) \) if and only if \( \uinorm{\A} \le \uinorm{\B} \) for every unitarily invariant norm. The direction (b) \( \Rightarrow \) (a) is the one needing new input, and it is proved by applying the hypothesis to the Ky Fan \( k \)-norms.

(b) \( \uinorm{\M}_{(k)} = \sum_{i\le k}\sigma_i(\M) \) (@def-ky-fan-norm). It is the unitarily invariant norm attached by @thm-von-neumann-correspondence to the \( k \)-th Ky Fan gauge @def-ky-fan-gauge, evaluated at \( \sigma(\M) \).

(c) False. Two norms do not decide the family. Take \( \A = \diag(1,1,0) \) and \( \B = \diag(\sqrt2, 0, 0) \): then \( \norm{\A}_F = \sqrt2 = \norm{\B}_F \) and \( \norm{\A}_2 = 1 \le \sqrt2 = \norm{\B}_2 \), but the trace norms are \( 2 \) and \( \sqrt2 \), so \( \uinorm{\A} \le \uinorm{\B} \) fails for the trace norm.

(d) Only to give \( \sigma_{k+1}(\B) = 0 \), which is what makes the Weyl inequality with second index \( k+1 \) say something about \( \A - \B \) alone.

(e) False: in the trace norm the minimizer need not be unique, so there is no *the* nearest unitary matrix. The polar factor \( \W \) is nearest in both norms, by @cor-polar-nearest-ui, and for invertible \( \A \) it is the **only** Frobenius minimizer (@cor-unitary-nearest); in the trace norm it can share the minimum. Take \( \A = \diag(2, \tfrac12) \), which is positive definite, so \( \lvert\A\rvert = \A \) and \( \W = \I \). Then \( \A - \I = \diag(1, -\tfrac12) \) has trace norm \( \tfrac32 \). The rotation \( \Q = \tfrac15\begin{psmallmatrix} 4 & -3 \\ 3 & 4\end{psmallmatrix} \) is unitary, and
\[
\A - \Q = \tfrac1{10}\begin{pmatrix} 12 & 6 \\ -6 & -3\end{pmatrix}
\]
has determinant \( 0 \) and is non-zero, so it has rank \( 1 \): its second singular value is \( 0 \), and the first is \( \norm{\A - \Q}_F = \tfrac{1}{10}\sqrt{144 + 36 + 36 + 9} = \tfrac32 \). Its trace norm is therefore \( \tfrac32 \) as well, so \( \I \) and \( \Q \) are both nearest in the trace norm. In the Frobenius norm they are not tied: \( \norm{\A - \I}_F = \tfrac{\sqrt5}2 < \tfrac32 = \norm{\A - \Q}_F \).
:::

### B. Practice

:::: {#exr-ky-fan-dominance-b1}
[B1: Dominance by hand]

Let \( \A, \B \in M_3(\nR) \) have singular values \( \sigma(\A) = (3, 2, 2) \) and \( \sigma(\B) = (4, 3, 1) \).

::: {.enumerate options="label=(\alph*)"}
1. Determine whether \( \uinorm{\A} \le \uinorm{\B} \) for every unitarily invariant norm.
2. Answer the same question for \( \sigma(\A') = (3, 3, 2) \) in place of \( \sigma(\A) \).
:::
::::

::: {.solution}
(a) The running totals are \( 3, 5, 7 \) for \( \A \) and \( 4, 7, 8 \) for \( \B \), and \( 3 \le 4 \), \( 5 \le 7 \), \( 7 \le 8 \). So \( \sigma(\A) \prec_w \sigma(\B) \) and @thm-ky-fan-dominance gives the inequality for every unitarily invariant norm.

(b) The running totals of \( \sigma(\A') \) are \( 3, 6, 8 \), all at most \( 4, 7, 8 \), so again yes. This one is worth noticing, because the index-by-index comparison **fails**: \( \sigma_3(\A') = 2 > 1 = \sigma_3(\B) \). Dominance is a statement about running totals, and it is strictly weaker than entrywise domination.
:::

:::: {#exr-ky-fan-dominance-b2}
[B2: Best approximations of a 2 by 2 matrix]

Let \( \A = \begin{psmallmatrix} 3 & 4 \\ 4 & -3\end{psmallmatrix} \). Compute \( \sigma(\A) \), find the best rank-one approximation, and compute the error in the spectral, Frobenius and trace norms. What is unusual about this matrix?
::::

::: {.solution}
\( \A\tp\A = \begin{psmallmatrix} 25 & 0 \\ 0 & 25\end{psmallmatrix} \), so \( \sigma(\A) = (5, 5) \). By @cor-eckart-young-ui the best rank-one approximation is \( \A_1 = 5\u_1\v_1^{*} \) for a singular value decomposition of \( \A \). One such decomposition is \( \A = \U\diag(5,5)\V\tp \) with \( \V = \I \) and \( \U = \A/5 \), which is orthogonal because \( \A\tp\A = 25\I \); it gives \( \u_1 = \tfrac15(3, 4) \), \( \v_1 = \e_1 \) and
\[
\A_1 = \begin{pmatrix} 3 & 0 \\ 4 & 0\end{pmatrix},
\qquad
\A - \A_1 = \begin{pmatrix} 0 & 4 \\ 0 & -3\end{pmatrix} .
\]
The error has singular values \( (\sigma_2, 0) = (5, 0) \), as @cor-eckart-young-ui predicts: spectral error \( 5 \), Frobenius error \( 5 \), trace-norm error \( 5 \). What is unusual is that \( \sigma_1 = \sigma_2 \), so the truncation is not unique: \( \A/5 \) is symmetric and orthogonal, and **every** unit vector is a right singular vector. Every rank-one matrix of the form \( 5\u\v^{*} \) arising from a singular value decomposition is a best approximation, and they are genuinely different matrices.
:::

:::: {#exr-ky-fan-dominance-b3}
[B3: A compression]

Let \( \A = \begin{psmallmatrix} 2 & 1 \\ 1 & 3\end{psmallmatrix} \) and let \( \P = \e_1\e_1\tp \). Compute \( \uinorm{\P\A\P} \) and \( \uinorm{\A} \) for the trace norm, and check @cor-compression-ui.
::::

::: {.solution}
\( \P\A\P = \begin{psmallmatrix} 2 & 0 \\ 0 & 0\end{psmallmatrix} \), whose singular values are \( (2, 0) \), so its trace norm is \( 2 \). The matrix \( \A \) is symmetric with \( \tr\A = 5 \) and \( \det\A = 5 \), so its eigenvalues are \( (5 \pm\sqrt5)/2 \), both positive; hence \( \A \succ 0 \), its singular values are its eigenvalues, and its trace norm is \( \tr\A = 5 \). Indeed \( 2 \le 5 \).
:::

### C. Going deeper

:::: {#exr-ky-fan-dominance-c1}
[C1: Dominance for sums]

Let \( \A, \B \in M_{m\times n}(\nC) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \uinorm{\A + \B} \le \uinorm{\A} + \uinorm{\B} \) follows from @lem-singular-value-subadditive together with @thm-gauge-monotone-under-majorization (b), without using that \( \uinorm{\cdot} \) is a norm.
2. Deduce that \( \sum_{i\le k}\sigma_i(\A + \B) \le \sum_{i \le k}\sigma_i(\A) + \sum_{i\le k}\sigma_i(\B) \) for every \( k \).
:::
::::

::: {.solution}
(a) By @lem-singular-value-subadditive, \( \sigma(\A + \B) \prec_w \sigma(\A) + \sigma(\B) \), and all three vectors have non-negative entries. Let \( \Phi \) be the gauge of the norm. By @thm-gauge-monotone-under-majorization (b), \( \Phi(\sigma(\A+\B)) \le \Phi(\sigma(\A) + \sigma(\B)) \), and by the triangle inequality for the norm \( \Phi \) on \( \nR^{p} \) the right side is at most \( \Phi(\sigma(\A)) + \Phi(\sigma(\B)) \). By @thm-von-neumann-correspondence these are \( \uinorm{\A+\B} \), and \( \uinorm{\A} + \uinorm{\B} \). (The triangle inequality used is that of \( \Phi \), a norm on \( \nR^p \), not that of \( \uinorm{\cdot} \).)

(b) Apply (a) to the Ky Fan \( k \)-norm, whose value at \( \M \) is \( \sum_{i\le k}\sigma_i(\M) \).
:::

:::: {#exr-ky-fan-dominance-c2}
[C2: Distance to the singular matrices, in every norm]

Let \( \A \in M_n(\nC) \) be invertible with singular values \( \sigma_1 \ge \dots \ge \sigma_n > 0 \), and let \( \uinorm{\cdot} \) be a unitarily invariant norm with gauge \( \Phi \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \min\{\uinorm{\A - \B} : \B \in M_n(\nC) \text{ singular}\} = \Phi(\sigma_n, 0, \dots, 0) \).
2. Deduce that this minimum equals \( \sigma_n\,\Phi(\e_1) \), and identify it for the spectral, Frobenius and trace norms.
:::

*Hint: a matrix is singular exactly when its rank is at most \( n - 1 \).*
::::

::: {.solution}
(a) By @thm-invertible-tfae-det (d), \( \B \) is singular if and only if \( \rank\B \le n-1 \). So the minimum is over the set appearing in @cor-eckart-young-ui with \( k = n-1 \), and that corollary gives the value \( \Phi(\sigma_{n}, 0, \dots, 0) \), attained at the truncation \( \A_{n-1} \), which is singular because its rank is \( n - 1 \).

(b) The vector \( (\sigma_n, 0, \dots, 0) \) is \( \sigma_n\e_1 \), and \( \Phi \) is a norm, so \( \Phi(\sigma_n\e_1) = \sigma_n\Phi(\e_1) \) as \( \sigma_n > 0 \). For the spectral norm \( \Phi = \norm{\cdot}_\infty \) and \( \Phi(\e_1) = 1 \); for the Frobenius norm \( \Phi = \norm{\cdot}_2 \) and \( \Phi(\e_1) = 1 \); for the trace norm \( \Phi = \norm{\cdot}_1 \) and \( \Phi(\e_1) = 1 \). All three give \( \sigma_n \). This is not an accident: the normalization \( \Phi(\e_1) = 1 \) of Section 4 is exactly the condition that makes every unitarily invariant norm agree on rank-one matrices with one non-zero singular value.
:::

:::: {#exr-ky-fan-dominance-c3}
[C3: Unitary matrices are far apart]

Let \( \U, \Q \in M_n(\nC) \) be unitary with \( \U \ne \Q \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \sigma(\U - \Q) = (\lvert\mu_1 - 1\rvert, \dots, \lvert\mu_n-1\rvert)^{\downarrow} \), where \( \mu_1, \dots, \mu_n \) are the eigenvalues of \( \Q^{*}\U \).
2. Deduce that \( \uinorm{\U - \Q} = \uinorm{\diag(\mu_1 - 1, \dots, \mu_n-1)} \) for every unitarily invariant norm, and that the trace-norm distance between two distinct unitary matrices can be as large as \( 2n \).
:::
::::

::: {.solution}
(a) \( \U - \Q = \Q(\Q^{*}\U - \I) \), and multiplying on the left by a unitary matrix does not change singular values, since \( (\Q\M)^{*}(\Q\M) = \M^{*}\M \) (@def-singular-values). The matrix \( \Z \coloneqq \Q^{*}\U \) is unitary, hence normal, so by the spectral theorem \( \Z = \Y\diag(\mu_1, \dots, \mu_n)\Y^{*} \) with \( \Y \) unitary, and \( \Z - \I = \Y\diag(\mu_i - 1)\Y^{*} \). Then \( (\Z-\I)^{*}(\Z-\I) = \Y\diag(\lvert\mu_i-1\rvert^2)\Y^{*} \), so the singular values are the numbers \( \lvert\mu_i-1\rvert \) sorted decreasingly (@def-singular-values).

(b) Both matrices in the claimed equality have the same singular value list, so @thm-von-neumann-correspondence gives equal norms. Each \( \mu_i \) has modulus \( 1 \), so \( \lvert\mu_i - 1\rvert \le 2 \), with equality when \( \mu_i = -1 \). Taking \( \Q = \I \) and \( \U = -\I \) gives every \( \mu_i = -1 \) and trace-norm distance \( \sum_i 2 = 2n \).
:::
