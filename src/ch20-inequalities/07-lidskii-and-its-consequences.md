# Lidskii's Theorem in Majorization Form

Chapter 16 §07 proved Lidskii's inequality and then translated the whole family of inequalities into one majorization. It could go no further, and said so. This section spends what it banked: the majorization is already in hand, and Sections 2, 3 and 6 turn it into a statement about every convex function and every unitarily invariant norm. The last part of the section carries all of it across to singular values.

## What Chapter 16 proved, and what it left

Here is the statement we start from. For Hermitian \( \A, \B \in M_n(F) \), @thm-lidskii-inequality says that for every index set \( 1 \le i_1 < \dots < i_k \le n \),
\[
\sum_{j=1}^{k}\lambda_{i_j}(\A) - \sum_{j=1}^{k}\lambda_{i_j}(\B)
\ \le\ \sum_{j=1}^{k}\lambda_j(\A - \B) ,
\]
and the remark that closes that section observes that, since the largest \( k \) entries of a vector are the best choice of \( k \) of them, this family of inequalities is exactly clause (M1) of @def-majorization for the pair of vectors below, while clause (M2) is the identity \( \tr\A - \tr\B = \tr(\A - \B) \):
\[
\vlambda(\A) - \vlambda(\B) \ \prec\ \vlambda(\A - \B) .
\]{#eq-lidskii-majorization}

**This is proved, in Chapter 16, and we do not prove it again.** What Chapter 16 could not do it named exactly: "Not proved here, and left to Chapter 20: the general consequences of a majorization \( \x \prec \y \), namely \( \sum_i\phi(x_i) \le \sum_i\phi(y_i) \) for every convex \( \phi \colon \nR \to \nR \), together with the matching statement for the unitarily invariant norms of that chapter."

Both consequences now exist. Section 2 proved the first, as @thm-karamata. Section 3 proved that a symmetric gauge is monotone under majorization, as @thm-gauge-monotone-under-majorization, and Section 4 identified the gauges with the unitarily invariant norms. All that is left is to apply them, which takes two short proofs, and then to repeat the exercise for singular values, which takes one idea.

::: {#exm-lidskii-two-by-two}
[A pair to keep in mind]

Let
\[
\A = \begin{pmatrix} 2 & 2 \\ 2 & 2\end{pmatrix},
\qquad
\B = \begin{pmatrix} 0 & -1 \\ -1 & 0\end{pmatrix} .
\]
Compute the three eigenvalue lists and check @eq-lidskii-majorization.
:::

::: {.solution}
\( \A \) is symmetric with \( \tr\A = 4 \) and \( \det\A = 0 \), so \( \vlambda(\A) = (4, 0) \). \( \B \) is symmetric with \( \tr\B = 0 \) and \( \det\B = -1 \), so \( \vlambda(\B) = (1, -1) \). Their difference
\[
\A - \B = \begin{pmatrix} 2 & 3 \\ 3 & 2\end{pmatrix}
\]
has trace \( 4 \) and determinant \( 4 - 9 = -5 \), so \( \vlambda(\A - \B) = (5, -1) \).

The vector of shifts is \( \vlambda(\A) - \vlambda(\B) = (4 - 1,\ 0 - (-1)) = (3, 1) \), already decreasing. Now compare with \( (5, -1) \): the top sums are \( 3 \le 5 \), and the totals are \( 4 = 4 \). So \( (3,1) \prec (5,-1) \), as @eq-lidskii-majorization promises, and the majorization is strict in its one non-trivial inequality.
:::

## Every convex function at once

::: {#thm-lidskii-convex}
[Lidskii's Theorem, Convex Form]

Let \( \A, \B \in M_n(F) \) be Hermitian, \( F = \nR \) or \( \nC \). Then for every convex \( \phi \colon \nR \to \nR \),
\[
\sum_{i=1}^{n}\phi\bigl(\lambda_i(\A) - \lambda_i(\B)\bigr)
\ \le\ \sum_{i=1}^{n}\phi\bigl(\lambda_i(\A - \B)\bigr) .
\]
:::

::: {.proof}
By @eq-lidskii-majorization, \( \vlambda(\A) - \vlambda(\B) \prec \vlambda(\A - \B) \). Apply @thm-karamata to this majorization, with \( I = \nR \) and the given \( \phi \). This proves the theorem.
:::

Three readings are worth having. With \( \phi(t) = \lvert t\rvert \), which is convex, the theorem says that the total movement of the eigenvalues is at most the total size of the eigenvalues of the perturbation. With \( \phi(t) = t^2 \) it is the Hoffman–Wielandt inequality, as the next corollary spells out. With \( \phi(t) = \max(t, 0) \) it says that the total **upward** movement of the eigenvalues is at most the total of the positive eigenvalues of the perturbation, and with \( \phi(t) = e^{ct} \) it gives bounds no earlier chapter could have stated.

::: {.warning}
The left side pairs \( \lambda_i(\A) \) with \( \lambda_i(\B) \) at the **same index**, both lists being in decreasing order, and the theorem claims nothing about any other pairing. For \( \A = \diag(4, 0) \) and \( \B = \begin{psmallmatrix} 2 & 2 \\ 2 & 2\end{psmallmatrix} \) the spectra are equal, \( \vlambda(\A) = \vlambda(\B) = (4, 0) \), so the sorted pairing gives \( 0 \) with \( \phi(t) = t^2 \). The reversed pairing gives \( (4-0)^2 + (0-4)^2 = 32 \), while \( \A - \B = \begin{psmallmatrix} 2 & -2 \\ -2 & -2\end{psmallmatrix} \) has \( \sum_i\lambda_i(\A-\B)^2 = \norm{\A - \B}_F^2 = 16 \). So the same inequality with a different matching is simply false.
:::

## Every unitarily invariant norm at once

To state the norm version we need to put a vector of shifts inside a matrix, and Section 4 has already done it. By @lem-ui-norm-of-diagonal the gauge of a unitarily invariant norm is recovered from the norm by
\[
\uinorm{\diag_{m,n}(\x)} = \Phi(\x) \qquad (\x \in \nR^{p}) ,
\]{#eq-gauge-of-a-diagonal}
where \( \diag_{m,n}(\x) \) carries \( \x \) down the main diagonal and zeros elsewhere, and is written \( \diag(\x) \) when \( m = n \). One more reading will be used throughout: if \( \H \in M_n(F) \) is Hermitian then \( \H^{*}\H = \H^2 \) has eigenvalues \( \lambda_i(\H)^2 \), so \( \sigma(\H) = \lvert\vlambda(\H)\rvert^{\downarrow} \) by @def-singular-values, and hence \( \uinorm{\H} = \Phi(\sigma(\H)) = \Phi(\vlambda(\H)) \), the last step by the permutation and sign invariance of @def-symmetric-gauge.

::: {#thm-lidskii-ui}
[Lidskii's Theorem, Norm Form]

Let \( \A, \B \in M_n(F) \) be Hermitian. Then for **every** unitarily invariant norm on \( M_n(F) \),
\[
\uinorm{\diag\bigl(\vlambda(\A) - \vlambda(\B)\bigr)} \ \le\ \uinorm{\A - \B} .
\]
:::

::: {.idea}
Both sides are the same symmetric gauge evaluated at two real vectors: the vector of eigenvalue shifts on the left, the eigenvalue vector of \( \A - \B \) on the right. Chapter 16 says the first is majorized by the second, and Section 3 says a symmetric gauge respects that.
:::

::: {.proof}
Let \( \Phi \) be the symmetric gauge of the norm, so that \( \uinorm{\M} = \Phi(\sigma(\M)) \) (@thm-von-neumann-correspondence). Put \( \x = \vlambda(\A) - \vlambda(\B) \) and \( \y = \vlambda(\A - \B) \), both in \( \nR^n \). By @eq-gauge-of-a-diagonal the left-hand side is \( \Phi(\x) \); and since \( \A - \B \) is Hermitian, the discussion above gives \( \uinorm{\A - \B} = \Phi(\y) \). By @eq-lidskii-majorization, \( \x \prec \y \), so @thm-gauge-monotone-under-majorization (a) — the part for arbitrary real vectors, which is what majorization rather than weak majorization buys — gives \( \Phi(\x) \le \Phi(\y) \). This proves the theorem.
:::

That is the second half of Chapter 16 §07's promise, and it is also what Chapter 19 §11 was waiting for when it listed, among the things that chapter did not do, that its bounds "hold in the Frobenius norm" and that "extending the eigenvalue and singular value bounds to every unitarily invariant norm belongs to Chapter 20". Two specializations make the point. With the spectral norm, whose gauge is \( \norm{\cdot}_\infty \), the theorem reads \( \max_i\lvert\lambda_i(\A) - \lambda_i(\B)\rvert \le \norm{\A-\B}_2 \), which is Weyl's perturbation bound @cor-weyl-perturbation. With the Frobenius norm, whose gauge is \( \norm{\cdot}_2 \), it is Hoffman–Wielandt. One statement, two classical corollaries, and every norm in between.

::: {#cor-hoffman-wielandt-again}
[Hoffman–Wielandt for Hermitian Matrices, Again]

Let \( \A, \B \in M_n(F) \) be Hermitian. Then
\[
\sum_{i=1}^{n}\bigl(\lambda_i(\A) - \lambda_i(\B)\bigr)^2 \ \le\ \norm{\A - \B}_F^2 .
\]
:::

::: {.proof}
The function \( \phi(t) = t^2 \) is convex, by @thm-convex-second-derivative (a) with \( \phi'' = 2 > 0 \). By @thm-lidskii-convex,
\[
\sum_{i}\bigl(\lambda_i(\A) - \lambda_i(\B)\bigr)^2 \le \sum_i \lambda_i(\A-\B)^2 .
\]
The matrix \( \E = \A - \B \) is Hermitian, so the spectral theorem writes \( \E = \U\diag(\vlambda(\E))\U^{*} \) with \( \U \) unitary, and @lem-frobenius-unitarily-invariant gives \( \norm{\E}_F^2 = \norm{\diag(\vlambda(\E))}_F^2 = \sum_i\lambda_i(\E)^2 \). This proves the corollary.
:::

This is @cor-hoffman-wielandt-hermitian of Chapter 19 §05, reached by a different road. That section said so in advance: "Chapter 20 shows that a majorization \( \x \prec \y \) gives \( \sum_i\phi(x_i) \le \sum_i\phi(y_i) \) for every convex \( \phi \); with \( \phi(t) = t^2 \) this is @cor-hoffman-wielandt-hermitian again, and Chapter 20 turns the same majorization into one bound for every unitarily invariant norm. Nothing here depends on that route; the proof above goes through Birkhoff's theorem …" So the two proofs are independent: Chapter 19 argued from Birkhoff's theorem applied to the matrix of squared moduli of the entries of a unitary change of basis, and never used Lidskii's inequality; this one uses Lidskii and never mentions doubly stochastic matrices. Neither is a special case of the other, and Chapter 19 reaches further in one direction: its @cor-hoffman-wielandt-hermitian is the Hermitian case of @thm-hoffman-wielandt, which holds for all **normal** \( \A, \B \). What that theorem gives there is weaker in kind — some permutation matching the two eigenvalue lists, not the sorted one, since complex eigenvalues have no decreasing order — and the argument here, resting on @eq-lidskii-majorization, stays with Hermitian matrices throughout.

::: {.check}
Check @thm-lidskii-ui and @cor-hoffman-wielandt-again for the pair of @exm-lidskii-two-by-two, in the spectral, Frobenius and trace norms.
:::

::: {.solution}
There \( \vlambda(\A) - \vlambda(\B) = (3, 1) \) and \( \vlambda(\A-\B) = (5, -1) \), so \( \diag(3,1) \) has singular values \( (3,1) \) and \( \A - \B \) has singular values \( (5, 1) \). The three norms of the left and right sides are: spectral, \( 3 \le 5 \); Frobenius, \( \sqrt{10} \le \sqrt{26} \); trace, \( 4 \le 6 \). The Frobenius case squared is \( 9 + 1 = 10 \le 26 \), which is @cor-hoffman-wielandt-again.
:::

## The same theorem for singular values

Chapter 19 §10 proved Mirsky's theorem in the Frobenius norm and closed with: "Chapter 20 puts both inside one statement covering every unitarily invariant norm", the two being the index-by-index bound @cor-singular-value-perturbation and the Frobenius bound @thm-mirsky-frobenius. The route is the one that section used and Section 6 used again: **a Hermitian dilation turns singular values into eigenvalues**, and then Lidskii's theorem applies. The only delicate point is the bookkeeping of the zeros, because a rectangular matrix dilates to a matrix with extra zero eigenvalues in the middle of its spectrum.

::: {#thm-mirsky-ui}
[Mirsky's Theorem in Every Unitarily Invariant Norm]

Let \( \A, \B \in M_{m\times n}(\nC) \) and \( p = \min(m, n) \). Then for **every** unitarily invariant norm on \( M_{m\times n}(\nC) \),
\[
\uinorm{\diag_{m,n}\bigl(\sigma(\A) - \sigma(\B)\bigr)} \ \le\ \uinorm{\A - \B} .
\]
:::

::: {.idea}
Dilate all three matrices. The eigenvalue list of \( \cH(\M) \) is \( \sigma(\M) \), then \( m+n-2p \) zeros, then \( -\sigma(\M) \) reversed, and the **positions** of the three blocks depend only on \( m \) and \( n \) — so \( \A \) and \( \B \) have their singular values in the same slots, and subtracting the two lists subtracts them index by index. Lidskii's majorization then compares a symmetric list \( \pm(\sigma_i(\A)-\sigma_i(\B)) \) with a symmetric list \( \pm\sigma_j(\A - \B) \) in \( \nR^{m+n} \). Reading its top-\( k \) sums for \( k \le p \) turns it into a weak majorization of the two lists we care about, in \( \nR^{p} \), and Section 3 finishes.
:::

::: {.proof}
Write \( N = m + n \), let \( \delta_i = \sigma_i(\A) - \sigma_i(\B) \) for \( i \le p \) and \( \vdelta = (\delta_1, \dots, \delta_p) \), and let \( \Phi \) be the symmetric gauge of the norm.

**Step 1: what has to be proved.** By @eq-gauge-of-a-diagonal and the sign invariance of @def-symmetric-gauge, \( \uinorm{\diag_{m,n}(\vdelta)} = \Phi(\vdelta) = \Phi(\lvert\vdelta\rvert) \); and \( \uinorm{\A - \B} = \Phi(\sigma(\A - \B)) \) by @thm-von-neumann-correspondence. Both \( \lvert\vdelta\rvert \) and \( \sigma(\A-\B) \) have non-negative entries, so by @thm-gauge-monotone-under-majorization (b) it is enough to prove the weak majorization
\[
\lvert\vdelta\rvert \ \prec_w\ \sigma(\A - \B) \qquad \text{in } \nR^{p} .
\]{#eq-mirsky-weak-majorization}

**Step 2: the dilations and their spectra.** For \( \M \in M_{m\times n}(\nC) \) let \( \cH(\M) = \begin{psmallmatrix} \0 & \M \\ \M^{*} & \0\end{psmallmatrix} \in M_N(\nC) \) be the Hermitian dilation of @prp-hermitian-dilation. Conjugate transposition is additive, so
\[
\cH(\A) - \cH(\B) = \cH(\A - \B) ,
\]
and all three matrices are Hermitian. By @prp-hermitian-dilation the eigenvalues of \( \cH(\M) \) are \( \pm\sigma_1(\M), \dots, \pm\sigma_p(\M) \) together with \( N - 2p \) zeros; since the \( \sigma_i(\M) \) are non-negative and decreasing, the decreasing list is
\[
\lambda_i(\cH(\M)) =
\begin{cases}
\sigma_i(\M) & 1 \le i \le p, \\
0 & p < i \le N - p, \\
-\sigma_{N+1-i}(\M) & N - p < i \le N .
\end{cases}
\]{#eq-dilation-spectrum-positions}
The three ranges depend only on \( m \) and \( n \), so the formula applies to \( \A \), to \( \B \) and to \( \A - \B \) **with the same ranges**. This is the bookkeeping the rectangular case needs: the zeros of \( \cH(\A) \) sit in exactly the positions of the zeros of \( \cH(\B) \), and so cancel when the two lists are subtracted.

**Step 3: Lidskii.** By @eq-lidskii-majorization applied to the Hermitian pair \( \cH(\A) \), \( \cH(\B) \),
\[
\vlambda(\cH(\A)) - \vlambda(\cH(\B)) \ \prec\ \vlambda(\cH(\A - \B)) .
\]
By @eq-dilation-spectrum-positions the vector on the left has entries \( \delta_i \) in positions \( i \le p \), zeros in the middle range, and \( -\delta_{N+1-i} \) in the last \( p \) positions; the vector on the right has \( \sigma_j(\A-\B) \), zeros, and the negatives of the \( \sigma_j(\A-\B) \) in the same three ranges.

**Step 4: read the running totals.** Fix \( k \le p \). The left-hand vector is the symmetric list of @lem-symmetric-list-top-sums with \( q = p \), \( r = N - 2p \) and \( z_i = \delta_i \), so by that lemma its \( k \)-th running total — the largest sum of \( k \) of its entries — is \( \sum_{j\le k}\lvert\vdelta\rvert^{\downarrow}_j \). The right-hand vector is already decreasing, so its \( k \)-th running total is \( \sum_{j \le k}\sigma_j(\A-\B) \). Since \( k \le p < N \), clause (M1) of @def-majorization applies at this \( k \) and gives
\[
\sum_{j=1}^{k}\lvert\vdelta\rvert^{\downarrow}_j \ \le\ \sum_{j=1}^{k}\sigma_j(\A - \B) .
\]
As \( k \le p \) was arbitrary, this is @eq-mirsky-weak-majorization, and Step 1 finishes the proof.
:::

::: {.remark}
**Where the factor of two went.** Chapter 19 §10 proved the Frobenius case by taking a **norm** of the dilation, and paid for it: \( \norm{\cH(\M)}_F^2 = 2\norm{\M}_F^2 \), so a factor \( 2 \) appeared on each side and canceled. That cancellation is special to a norm which adds squares, and for a general unitarily invariant norm there is no such identity — indeed \( \uinorm{\cH(\M)} \) is a norm on a different matrix space, computed by a gauge on \( \nR^{N} \) rather than on \( \nR^{p} \). The proof above never takes a norm of a dilation. It uses the dilation only to obtain a **majorization of eigenvalue lists**, and then reads off the \( p \) running totals it needs. No factor of \( 2 \) arises, and none has to cancel.
:::

Specializing the gauge recovers both statements that Chapter 19 §10 wanted inside one: \( \Phi = \norm{\cdot}_\infty \) gives \( \max_i\lvert\sigma_i(\A)-\sigma_i(\B)\rvert \le \norm{\A-\B}_2 \), which is @cor-singular-value-perturbation, and \( \Phi = \norm{\cdot}_2 \) gives @thm-mirsky-frobenius. Chapter 19 §11's ledger entry — "extending the eigenvalue and singular value bounds to every unitarily invariant norm belongs to Chapter 20" — is now paid for the eigenvalue bounds by @thm-lidskii-ui and for the singular value bounds by @thm-mirsky-ui. Chapter 19 §10's square-root and polar bounds (@thm-sqrt-perturbation, @thm-polar-positive-perturbation, @thm-polar-unitary-perturbation) are **not** extended here: they still hold only in the two norms Chapter 19 proved them in, the spectral and the Frobenius.

The pair of @exm-lidskii-two-by-two illustrates the singular value form as well. There \( \A = \begin{psmallmatrix} 2 & 2 \\ 2 & 2\end{psmallmatrix} \) is positive semidefinite with eigenvalues \( 4, 0 \), so \( \sigma(\A) = (4, 0) \); \( \B \) has eigenvalues \( \pm1 \), so \( \sigma(\B) = (1,1) \); and \( \A - \B \) has eigenvalues \( 5, -1 \), so \( \sigma(\A - \B) = (5, 1) \). The vector of differences is \( \sigma(\A) - \sigma(\B) = (3, -1) \), whose absolute values \( (3, 1) \) have running totals \( 3 \le 5 \) and \( 4 \le 6 \): the weak majorization of @eq-mirsky-weak-majorization, and with it the norm inequality in every unitarily invariant norm.

::: {.warning}
Both @thm-lidskii-ui and @thm-mirsky-ui compare **sorted** lists, and the matching they use is the sorted one. No claim is made for any other pairing, and @thm-mirsky-ui in particular is not a statement about eigenvalues: for non-Hermitian matrices the eigenvalues can be wildly unstable while the singular values are not, which is the whole content of Chapter 19 §10's remark that Mirsky's theorem needs no normality hypothesis at all.
:::

## Exercises

### A. Check your understanding

:::: {#exr-lidskii-and-its-consequences-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the majorization @eq-lidskii-majorization, and say which chapter proves it.
2. State @thm-lidskii-ui, and say what \( \diag(\vlambda(\A) - \vlambda(\B)) \) means.
3. Determine whether the following is true for Hermitian \( \A, \B \), and justify your answer: \( \sum_i\lvert\lambda_i(\A) - \lambda_i(\B)\rvert \le \sum_i\lvert\lambda_i(\A-\B)\rvert \).
4. Determine whether the following is true, and justify your answer: @thm-mirsky-ui holds with the singular values of \( \A \) and \( \B \) listed in **increasing** order on the left.
5. Where in the proof of @thm-mirsky-ui is it used that \( \A \) and \( \B \) have the same size?
:::
::::

::: {.solution}
(a) For Hermitian \( \A, \B \in M_n(F) \), \( \vlambda(\A) - \vlambda(\B) \prec \vlambda(\A-\B) \). It is proved in Chapter 16 §07, from @thm-lidskii-inequality over all index sets together with the equality of traces.

(b) For every unitarily invariant norm, \( \uinorm{\diag(\vlambda(\A)-\vlambda(\B))} \le \uinorm{\A-\B} \). The matrix \( \diag(\x) \) is the diagonal matrix in \( M_n(F) \) whose \( i \)-th diagonal entry is \( x_i \); here \( x_i = \lambda_i(\A) - \lambda_i(\B) \), the shift of the \( i \)-th eigenvalue, the lists being in decreasing order.

(c) True. Take \( \phi(t) = \lvert t\rvert \) in @thm-lidskii-convex; it is convex, being a norm on \( \nR \). Alternatively it is @thm-lidskii-ui for the trace norm, using @eq-gauge-of-a-diagonal.

(d) True, and for a cheap reason: reversing both lists changes the vector \( \vdelta \) only by reversing it, and the gauge of a unitarily invariant norm is permutation-invariant (@def-symmetric-gauge), so the left-hand side is unchanged. What would **not** be true is to sort one list increasingly and the other decreasingly; see the warning after @thm-lidskii-convex.

(e) Twice. The two matrices must lie in the same space for \( \A - \B \) to be defined and for one norm to apply to all three matrices; and in Step 2, \( m \), \( n \) and \( p \) being the same for \( \A \) and \( \B \) is what puts the zeros of the two dilated spectra in the same positions, so that the difference of the two lists has the shape used in Step 4.
:::

### B. Practice

:::: {#exr-lidskii-and-its-consequences-b1}
[B1: Running the three consequences]

Let \( \A = \diag(5, 1, 0) \) and let \( \B = \A - \E \) with
\[
\E = \begin{pmatrix} 0 & 0 & 2 \\ 0 & 0 & 0 \\ 2 & 0 & 0\end{pmatrix} .
\]

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \vlambda(\B) \) and \( \vlambda(\E) \).
2. Verify @eq-lidskii-majorization for this pair.
3. Verify @thm-lidskii-ui in the spectral, Frobenius and trace norms, and @cor-hoffman-wielandt-again.
:::
::::

::: {.solution}
(a) \( \E \) acts as \( \begin{psmallmatrix} 0 & 2 \\ 2 & 0\end{psmallmatrix} \) on \( \Span(\e_1, \e_3) \) and as \( 0 \) on \( \e_2 \), so \( \vlambda(\E) = (2, 0, -2) \). Next,
\[
\B = \A - \E = \begin{pmatrix} 5 & 0 & -2 \\ 0 & 1 & 0 \\ -2 & 0 & 0\end{pmatrix} .
\]
On \( \Span(\e_1,\e_3) \) it is \( \begin{psmallmatrix} 5 & -2 \\ -2 & 0\end{psmallmatrix} \), with trace \( 5 \) and determinant \( -4 \), so its eigenvalues there are \( (5 \pm\sqrt{41})/2 \); together with the eigenvalue \( 1 \) from \( \e_2 \),
\[
\vlambda(\B) = \Bigl(\tfrac{5+\sqrt{41}}2,\ 1,\ \tfrac{5-\sqrt{41}}2\Bigr)
\approx (5.702,\ 1,\ -0.702) .
\]

(b) The shifts are \( \vlambda(\A) - \vlambda(\B) = (5 - \tfrac{5+\sqrt{41}}2,\ 0,\ \tfrac{\sqrt{41}-5}{2}) = (\tfrac{5 - \sqrt{41}}2,\ 0,\ \tfrac{\sqrt{41}-5}2) \approx (-0.702,\ 0,\ 0.702) \). Sorted decreasingly this is \( (0.702, 0, -0.702) \), with running totals \( 0.702,\ 0.702,\ 0 \). The list \( \vlambda(\E) = (2, 0, -2) \) has running totals \( 2, 2, 0 \). Each of the first two is larger, and the totals agree at \( 0 \). So the majorization holds.

(c) Write \( c = \tfrac{\sqrt{41}-5}{2} \approx 0.702 \). The left-hand matrix is \( \diag(-c, 0, c) \), whose singular values are \( (c, c, 0) \); the right-hand matrix is \( \E \), whose singular values are \( (2, 2, 0) \). Spectral: \( c \le 2 \). Frobenius: \( c\sqrt2 \approx 0.993 \le 2\sqrt2 \approx 2.828 \). Trace: \( 2c \approx 1.403 \le 4 \). Squaring the Frobenius comparison gives
\[
2c^2 = \tfrac{(\sqrt{41}-5)^2}{2} = \tfrac{66 - 10\sqrt{41}}{2} = 33 - 5\sqrt{41} \approx 0.984
\]
on the left and \( \norm{\E}_F^2 = 8 \) on the right, which is @cor-hoffman-wielandt-again.
:::

:::: {#exr-lidskii-and-its-consequences-b2}
[B2: Singular values of a one-entry change]

Let \( \A = \begin{psmallmatrix} 3 & 1 \\ 1 & 3\end{psmallmatrix} \) and \( \B = \begin{psmallmatrix} 3 & 1 \\ 0 & 3\end{psmallmatrix} \). Compute both sides of @thm-mirsky-ui in the trace norm, and compare with what @cor-singular-value-perturbation gives on its own.
::::

::: {.solution}
\( \A \) is symmetric with eigenvalues \( 4 \) and \( 2 \), both positive, so \( \sigma(\A) = (4, 2) \). For \( \B \), \( \B\tp\B = \begin{psmallmatrix} 9 & 3 \\ 3 & 10\end{psmallmatrix} \), with trace \( 19 \) and determinant \( 81 \), so its eigenvalues are \( \tfrac{19\pm\sqrt{37}}2 \); these are the squares of \( \tfrac{\sqrt{37}\pm1}{2} \), since \( \bigl(\tfrac{\sqrt{37}\pm1}{2}\bigr)^2 = \tfrac{38 \pm 2\sqrt{37}}{4} \). Hence
\[
\sigma(\B) = \Bigl(\tfrac{\sqrt{37}+1}2,\ \tfrac{\sqrt{37}-1}2\Bigr) \approx (3.541,\ 2.541) .
\]
The differences are \( \sigma(\A) - \sigma(\B) = \bigl(\tfrac{7 - \sqrt{37}}2,\ \tfrac{5-\sqrt{37}}2\bigr) \approx (0.459,\ -0.541) \), so the left side in the trace norm is
\[
\tfrac{7-\sqrt{37}}{2} + \tfrac{\sqrt{37}-5}{2} = 1 .
\]
On the right, \( \A - \B = \begin{psmallmatrix} 0 & 0 \\ 1 & 0\end{psmallmatrix} \) has singular values \( (1, 0) \), so \( \uinorm{\A-\B} = 1 \) in the trace norm. The inequality holds with **equality** here.

@cor-singular-value-perturbation gives only \( \lvert\sigma_i(\A)-\sigma_i(\B)\rvert \le \norm{\A-\B}_2 = 1 \) for each \( i \) separately, hence at best \( 2 \) for the sum. Mirsky's theorem halves that, and here it is exact.
:::

:::: {#exr-lidskii-and-its-consequences-b3}
[B3: A bound with no norm in sight]

Let \( \A, \B \in M_n(\nC) \) be Hermitian with \( \norm{\A - \B}_2 \le \varepsilon \). Prove that \( \sum_i\lvert\lambda_i(\A) - \lambda_i(\B)\rvert \le n\varepsilon \), and give a pair for which this is an equality.
::::

::: {.solution}
By @thm-lidskii-convex with \( \phi(t) = \lvert t\rvert \),
\[
\sum_i\lvert\lambda_i(\A)-\lambda_i(\B)\rvert \le \sum_i\lvert\lambda_i(\A-\B)\rvert \le n\max_i\lvert\lambda_i(\A-\B)\rvert = n\norm{\A-\B}_2 \le n\varepsilon ,
\]
the last equality by @lem-hermitian-spectral-norm. For equality take \( \B = \A - \varepsilon\I \): then \( \lambda_i(\B) = \lambda_i(\A) - \varepsilon \) for every \( i \), the left side is \( n\varepsilon \), and \( \norm{\A-\B}_2 = \varepsilon \).
:::

### C. Going deeper

:::: {#exr-lidskii-and-its-consequences-c1}
[C1: The Schatten norms]

Recall the Schatten \( r \)-norm \( \uinorm{\M}_{S_r} = \bigl(\sum_i\sigma_i(\M)^{r}\bigr)^{1/r} \) of @exm-schatten-norms, the unitarily invariant norm with gauge \( \norm{\cdot}_r \), and let \( 1 \le r < \infty \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that for Hermitian \( \A, \B \in M_n(\nC) \), \( \sum_i\lvert\lambda_i(\A)-\lambda_i(\B)\rvert^{r} \le \sum_i\lvert\lambda_i(\A-\B)\rvert^{r} \), in two ways: from @thm-lidskii-convex and from @thm-lidskii-ui.
2. Deduce the same statement for singular values, with \( \sigma \) in place of \( \lambda \) and \( \A, \B \) arbitrary of the same size.
:::
::::

::: {.solution}
(a) *From @thm-lidskii-convex.* First, \( \phi(t) = \lvert t\rvert^{r} \) is convex on \( \nR \). For \( r = 1 \) this is \( \lvert t\rvert = \max\{t, -t\} \), convex by @prp-sup-of-affine-convex. Let \( r > 1 \), let \( a, b \in \nR \) and let \( 0 < \theta < 1 \) (the cases \( \theta = 0, 1 \) are equalities); write \( \theta' = 1 - \theta \) and let \( q = r/(r-1) \) be the exponent conjugate to \( r \). Apply @thm-holder in \( \nR^2 \) to
\[
\x = \bigl(\theta^{1/r}\lvert a\rvert,\ (\theta')^{1/r}\lvert b\rvert\bigr),
\qquad
\y = \bigl(\theta^{1/q},\ (\theta')^{1/q}\bigr) .
\]
Since \( \tfrac1r + \tfrac1q = 1 \), the rules for powers of Chapter 17 §11 give \( \inner{\x}{\y} = \theta\lvert a\rvert + \theta'\lvert b\rvert \) and \( \norm{\y}_q = (\theta + \theta')^{1/q} = 1 \), so
\[
\theta\lvert a\rvert + \theta'\lvert b\rvert \ \le\ \norm{\x}_r
= \bigl(\theta\lvert a\rvert^{r} + \theta'\lvert b\rvert^{r}\bigr)^{1/r} .
\]
The function \( u \mapsto u^{r} \) is increasing on \( [0, \infty) \) (Chapter 17 §11), and \( \lvert\theta a + \theta'b\rvert \le \theta\lvert a\rvert + \theta'\lvert b\rvert \) by @thm-complex-triangle-inequality, so raising the displayed inequality to the power \( r \) gives
\[
\lvert\theta a + \theta'b\rvert^{r} \ \le\ \bigl(\theta\lvert a\rvert + \theta'\lvert b\rvert\bigr)^{r} \ \le\ \theta\lvert a\rvert^{r} + \theta'\lvert b\rvert^{r} ,
\]
which is @def-convex-function for \( \phi \) on \( \nR \). Now apply @thm-lidskii-convex.

*From @thm-lidskii-ui.* Take the Schatten \( r \)-norm, whose gauge is \( \norm{\cdot}_r \). The left-hand side of @thm-lidskii-ui is \( \bigl(\sum_i\lvert\lambda_i(\A)-\lambda_i(\B)\rvert^{r}\bigr)^{1/r} \) by @eq-gauge-of-a-diagonal, and the right-hand side is \( \bigl(\sum_i\lvert\lambda_i(\A-\B)\rvert^{r}\bigr)^{1/r} \), since \( \A - \B \) is Hermitian. Raise to the power \( r \).

(b) Apply @thm-mirsky-ui with the Schatten \( r \)-norm and raise to the power \( r \), reading both sides through @thm-von-neumann-correspondence as above.
:::

:::: {#exr-lidskii-and-its-consequences-c2}
[C2: What the dilation costs]

Let \( \A, \B \in M_{m\times n}(\nC) \) and let \( \cH(\cdot) \) be the Hermitian dilation of @prp-hermitian-dilation.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \uinorm{\cH(\A)} \) and \( \uinorm{\A} \) cannot be compared in general, by computing both for the Frobenius norm and for the spectral norm with \( \A = \I_2 \).
2. Explain, in one or two sentences, why the proof of @thm-mirsky-ui is nevertheless free of any such factor.
3. Deduce @cor-eckart-young-ui from @thm-mirsky-ui, and say why Section 6 nevertheless proved it another way.
:::

*Hint: for (c), a matrix of rank at most \( k \) has \( \sigma_i = 0 \) for \( i > k \).*
::::

::: {.solution}
(a) For \( \A = \I_2 \), \( \cH(\A) \in M_4(\nC) \) has singular values \( (1,1,1,1) \), so \( \norm{\cH(\A)}_F = 2 \) while \( \norm{\A}_F = \sqrt2 \): the Frobenius norm grows by \( \sqrt2 \). The spectral norms, however, are both \( 1 \). So the ratio \( \uinorm{\cH(\A)}/\uinorm{\A} \) depends on the norm, and there is no single factor to divide out. (The two norms also live on different spaces, \( M_4 \) and \( M_2 \).)

(b) Because the dilation is used only to produce a majorization between **eigenvalue lists**, from which the required inequality between running totals of the \( p \) numbers \( \lvert\delta_i\rvert \) and the \( p \) numbers \( \sigma_j(\A-\B) \) is read off directly. No norm is ever applied to a dilated matrix.

(c) Let \( \rank\B \le k \), so \( \sigma_i(\B) = 0 \) for \( i > k \) and hence \( \lvert\delta_i\rvert = \sigma_i(\A) \) for \( i > k \), in the notation of the proof of @thm-mirsky-ui. Let \( \z \in \nR^{p} \) have \( z_i = 0 \) for \( i \le k \) and \( z_i = \sigma_i(\A) \) for \( i > k \). Then \( \lvert z_i\rvert \le \lvert\delta_i\rvert \) for every \( i \), so @prp-gauge-monotone gives \( \Phi(\z) \le \Phi(\vdelta) \); and \( \Phi(\z) = \Phi(\sigma_{k+1}, \dots, \sigma_p, 0, \dots, 0) \) by the permutation invariance of @def-symmetric-gauge. Combining with @thm-mirsky-ui,
\[
\Phi(\sigma_{k+1}, \dots, \sigma_p, 0, \dots, 0) \le \Phi(\vdelta) = \uinorm{\diag_{m,n}(\vdelta)} \le \uinorm{\A - \B} ,
\]
which is the bound of @cor-eckart-young-ui, attained at \( \A_k \). Section 6 proved it earlier in the chapter, so it could not use this section; and its route gives more, namely \( \sigma_i(\A - \A_k) \le \sigma_i(\A-\B) \) index by index, which is the route Chapter 12 §10 predicted.
:::
