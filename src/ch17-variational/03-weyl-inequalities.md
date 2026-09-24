# How Far Eigenvalues Move

Chapter 16 §07 asked what happens to the eigenvalues of a matrix when the matrix is nudged, and came back with a discouraging answer: they move continuously, and nothing better. @exm-jordan-block-perturbation exhibits a perturbation of size \( \varepsilon \) that moves every eigenvalue a distance \( \varepsilon^{1/k} \), so no Lipschitz constant survives. That section also promised that the Hermitian case is different, and left the proof here.

The reason the Hermitian case is different is now available. @thm-courant-fischer describes \( \lambda_k(\A) \) as an optimization over subspaces, and an optimization over subspaces reacts to a change in \( \A \) the way any optimization reacts to a change in the objective: by at most the change in the objective. Turning that sentence into inequalities is the business of this section, and the inequalities are sharper than the sentence suggests, because the index may be shifted as well.

**Throughout this section the field is \( \nR \) or \( \nC \), and every matrix whose eigenvalues are written down is Hermitian**, that is, \( \A^{*} = \A \) with \( \A \in M_n(F) \) and \( n \ge 1 \). Its eigenvalues are real and are always indexed **decreasingly**, \( \lambda_1(\A) \ge \lambda_2(\A) \ge \dots \ge \lambda_n(\A) \), as they have been since Chapter 13. Sums of Hermitian matrices are Hermitian, so \( \A + \B \) is again a matrix this section may write \( \lambda_i \) of.

## Two small facts about eigenvalue lists

One small fact is used in every proof below, and it is the reason the index bookkeeping works out. If a vector lies in the span of the *bottom* eigenvectors of \( \A \), its Rayleigh quotient cannot exceed the largest eigenvalue in that span; if it lies in the span of the *top* ones, the quotient cannot fall below the smallest eigenvalue there.

::: {#lem-rayleigh-on-eigenspan}
[The Quotient on a Span of Eigenvectors]

Let \( \A \in M_n(F) \) be Hermitian and let \( (\u_1, \dots, \u_n) \) be an orthonormal basis of \( F^n \) with \( \A\u_p = \lambda_p(\A)\u_p \) for every \( p \). Fix \( i \) with \( 1 \le i \le n \).

::: {.enumerate options="label=(\alph*)"}
1. If \( \x \ne \0 \) lies in \( \Span\{\u_i, \u_{i+1}, \dots, \u_n\} \), then \( R_{\A}(\x) \le \lambda_i(\A) \).
2. If \( \x \ne \0 \) lies in \( \Span\{\u_1, \u_2, \dots, \u_i\} \), then \( R_{\A}(\x) \ge \lambda_i(\A) \).
:::
:::

::: {.proof}
Such a basis exists by the spectral theorem: @cor-spectral-complex-matrix over \( \nC \), where a Hermitian matrix is normal and its eigenvalues may be listed in any prescribed order, and @cor-spectral-real-matrix over \( \nR \), where Hermitian means symmetric.

(a) Write \( \x = \sum_{p \ge i}c_p\u_p \), with the \( c_p \) not all zero. Since the \( \u_p \) are orthonormal,
\[
\begin{aligned}
\inner{\A\x}{\x} &= \Bigl\langle \sum_{p \ge i}c_p\lambda_p(\A)\u_p,\ \sum_{q \ge i}c_q\u_q\Bigr\rangle
= \sum_{p \ge i}\lambda_p(\A)\lvert c_p\rvert^2 , \\
\norm{\x}^2 &= \sum_{p \ge i}\lvert c_p\rvert^2 .
\end{aligned}
\]
Every index in these sums satisfies \( p \ge i \), so \( \lambda_p(\A) \le \lambda_i(\A) \) by the decreasing indexing, and therefore \( \inner{\A\x}{\x} \le \lambda_i(\A)\norm{\x}^2 \). Since \( \x \ne \0 \) we have \( \norm{\x}^2 > 0 \) and may divide, which gives \( R_{\A}(\x) \le \lambda_i(\A) \) by @def-rayleigh-quotient.

(b) The same computation with \( \x = \sum_{p \le i}c_p\u_p \) gives \( \inner{\A\x}{\x} = \sum_{p \le i}\lambda_p(\A)\lvert c_p\rvert^2 \), and now every index satisfies \( p \le i \), so \( \lambda_p(\A) \ge \lambda_i(\A) \) and the inequality reverses. This proves the lemma.
:::

The two halves are the two ways of using an eigenvector span: (a) caps a quotient from above, (b) props it up from below. The proof of Weyl's inequalities needs only (a), applied to a single vector for two different matrices at once; (b) is the form in which the same fact enters the witness half of a min–max argument.

A second small fact converts statements about the top of an eigenvalue list into statements about the bottom. Negating a matrix negates its eigenvalues, and negation reverses the order of real numbers.

::: {#lem-eigenvalues-of-negation}
[Negation Reverses the List]

Let \( \A \in M_n(F) \) be Hermitian. Then \( -\A \) is Hermitian and
\[
\lambda_p(-\A) = -\lambda_{n+1-p}(\A) \qquad (1 \le p \le n) .
\]
:::

::: {.proof}
\( (-\A)^{*} = -\A^{*} = -\A \), so \( -\A \) is Hermitian. By the spectral theorem quoted in the proof of @lem-rayleigh-on-eigenspan, \( \A = \U\D\U^{*} \) with \( \D = \diag(\lambda_1(\A), \dots, \lambda_n(\A)) \) and \( \U \) unitary, whence \( -\A = \U(-\D)\U^{*} \). So the eigenvalue list of \( -\A \), with multiplicity, is \( -\lambda_1(\A), \dots, -\lambda_n(\A) \). Multiplying by \( -1 \) reverses the order of real numbers, so listing these decreasingly gives
\[
-\lambda_n(\A) \ \ge\ -\lambda_{n-1}(\A) \ \ge\ \dots \ \ge\ -\lambda_1(\A) ,
\]
whose \( p \)-th entry is \( -\lambda_{n+1-p}(\A) \). This proves the lemma.
:::

## The two families of Weyl inequalities

Here is the question. Given the eigenvalues of \( \A \) and the eigenvalues of \( \B \), separately, what can be said about the eigenvalues of \( \A + \B \)? Nothing exact: \( \diag(1,0) \) and \( \diag(0,1) \) have the same eigenvalue list as \( \diag(1,0) \) and \( \diag(1,0) \), while the two sums \( \I \) and \( \diag(2,0) \) do not. But a great deal inexactly, and the shape of the answer is dictated by the index arithmetic.

::: {#thm-weyl-inequalities}
[Weyl's Inequalities]

Let \( \A, \B \in M_n(F) \) be Hermitian and let \( 1 \le i, j \le n \).

::: {.enumerate options="label=(\alph*)"}
1. If \( i + j - 1 \le n \), then
   \[
   \lambda_{i+j-1}(\A + \B) \ \le\ \lambda_i(\A) + \lambda_j(\B) .
   \]
2. If \( i + j - n \ge 1 \), then
   \[
   \lambda_{i+j-n}(\A + \B) \ \ge\ \lambda_i(\A) + \lambda_j(\B) .
   \]
:::
:::

::: {.idea}
For (a), read \( \lambda_{i+j-1}(\A+\B) \) through the **max–min** half of @thm-courant-fischer: it is the best guaranteed value of \( R_{\A+\B} \) on a subspace of dimension \( i+j-1 \). So take an arbitrary such subspace \( W \) and find one bad vector inside it — a vector on which \( R_{\A} \) is capped by \( \lambda_i(\A) \) and \( R_{\B} \) is capped by \( \lambda_j(\B) \) simultaneously. The span of the bottom \( n-i+1 \) eigenvectors of \( \A \) is a *subspace* on which \( R_{\A} \) is capped by \( \lambda_i(\A) \), and the span of the bottom \( n-j+1 \) eigenvectors of \( \B \) is one on which \( R_{\B} \) is capped by \( \lambda_j(\B) \). (The set of *all* vectors capped by \( \lambda_i(\A) \) is larger and is not a subspace; the spans are what the dimension count can use.) Three subspaces must meet, and the dimensions have been chosen so that they do — twice, by @lem-subspace-intersection. Since \( R_{\A+\B} = R_{\A} + R_{\B} \), that one vector finishes the argument.

Part (b) is not a new proof. Negating a Hermitian matrix reverses its eigenvalue list (@lem-eigenvalues-of-negation), so (a) applied to \( -\A \) and \( -\B \) at the reflected indices \( n+1-i \) and \( n+1-j \) says exactly (b), once every index is translated back.
:::

::: {.proof}
**(a)** Put \( k = i + j - 1 \), so \( 1 \le k \le n \). By the spectral theorem choose an orthonormal basis \( (\u_1, \dots, \u_n) \) of eigenvectors of \( \A \) with \( \A\u_p = \lambda_p(\A)\u_p \), and an orthonormal basis \( (\v_1, \dots, \v_n) \) of eigenvectors of \( \B \) with \( \B\v_q = \lambda_q(\B)\v_q \). Set
\[
U = \Span\{\u_i, \dots, \u_n\}, \qquad V = \Span\{\v_j, \dots, \v_n\} ,
\]
so that \( \dim U = n - i + 1 \) and \( \dim V = n - j + 1 \), the two lists being independent as parts of a basis.

Let \( W \le F^n \) be **any** subspace with \( \dim W = k \). Then
\[
\dim W + \dim U = (i + j - 1) + (n - i + 1) = n + j > n ,
\]
since \( j \ge 1 \), so \( W \cap U \ne \{\0\} \) by @lem-subspace-intersection. More than that is needed, namely how large \( W \cap U \) is, and the dimension formula @thm-dimension-formula-subspace-dim supplies it:
\[
\dim(W \cap U) = \dim W + \dim U - \dim(W + U) \ \ge\ (n + j) - n = j ,
\]
because \( W + U \) is a subspace of \( F^n \). Therefore
\[
\dim(W \cap U) + \dim V \ \ge\ j + (n - j + 1) = n + 1 > n ,
\]
and a second application of @lem-subspace-intersection, to the subspaces \( W \cap U \) and \( V \), produces a vector
\[
\x \in W \cap U \cap V, \qquad \x \ne \0 .
\]

Now evaluate. Since \( \x \in U \), part (a) of @lem-rayleigh-on-eigenspan gives \( R_{\A}(\x) \le \lambda_i(\A) \); since \( \x \in V \), the same part applied to \( \B \) gives \( R_{\B}(\x) \le \lambda_j(\B) \). The inner product is additive in its first slot, so \( \inner{(\A+\B)\x}{\x} = \inner{\A\x}{\x} + \inner{\B\x}{\x} \) and hence \( R_{\A+\B}(\x) = R_{\A}(\x) + R_{\B}(\x) \). Since \( \x \) is a non-zero vector of \( W \),
\[
\min_{\0 \ne \y \in W} R_{\A+\B}(\y) \ \le\ R_{\A+\B}(\x) \ \le\ \lambda_i(\A) + \lambda_j(\B) .
\]
The subspace \( W \) of dimension \( k \) was arbitrary, so the maximum of the left-hand side over all such \( W \) obeys the same bound; and that maximum is \( \lambda_k(\A+\B) \) by the max–min half of @thm-courant-fischer. This proves (a).

**(b)** Suppose \( i + j - n \ge 1 \) and set
\[
i' = n + 1 - i, \qquad j' = n + 1 - j ,
\]
both of which lie in \( \{1, \dots, n\} \). Then
\[
i' + j' - 1 = 2n + 1 - i - j \le n
\]
precisely because \( i + j - n \ge 1 \), so part (a) applies to the Hermitian matrices \( -\A \) and \( -\B \) at the indices \( i', j' \):
\[
\lambda_{i'+j'-1}(-\A - \B) \ \le\ \lambda_{i'}(-\A) + \lambda_{j'}(-\B) .
\]
Translate each term with @lem-eigenvalues-of-negation. On the right, \( \lambda_{i'}(-\A) = -\lambda_{n+1-i'}(\A) = -\lambda_i(\A) \), and likewise \( \lambda_{j'}(-\B) = -\lambda_j(\B) \). On the left, \( -\A-\B = -(\A+\B) \) with \( \A + \B \) Hermitian, and \( i'+j'-1 = 2n+1-i-j \), so
\[
\lambda_{i'+j'-1}\bigl(-(\A+\B)\bigr)
= -\lambda_{n+1-(2n+1-i-j)}(\A+\B)
= -\lambda_{i+j-n}(\A+\B) .
\]
The displayed inequality therefore reads \( -\lambda_{i+j-n}(\A+\B) \le -\lambda_i(\A) - \lambda_j(\B) \). Multiplying by \( -1 \) reverses it and gives (b). This proves the theorem.
:::

Two remarks on the bookkeeping, because it is the whole content. First, the index on the left is *not* \( i \) or \( j \) but \( i + j - 1 \), so a fixed eigenvalue \( \lambda_k(\A+\B) \) receives \( k \) upper bounds from (a), one for each way of splitting \( k = i + j - 1 \), and the best of them is their minimum. Second, (a) only ever bounds from above and (b) only from below. To trap one eigenvalue \( \lambda_i(\A+\B) \) from both sides with the index of \( \A \) unchanged, take \( j = 1 \) in (a) and \( j = n \) in (b); that is the next corollary.

::: {.check}
Take \( i = j = 1 \) in (a) and \( i = j = n \) in (b). What do the two inequalities say, and which earlier result are they?
:::

::: {.solution}
They say \( \lambda_1(\A+\B) \le \lambda_1(\A) + \lambda_1(\B) \) and \( \lambda_n(\A+\B) \ge \lambda_n(\A) + \lambda_n(\B) \). For \( i = j = n \) the index on the left of (b) is \( n + n - n = n \), as required. These are the statements that the largest eigenvalue is subadditive and the smallest superadditive, which one can also read straight off @lem-extreme-eigenvalues-quadratic-form: \( \inner{(\A+\B)\x}{\x} = \inner{\A\x}{\x} + \inner{\B\x}{\x} \le \lambda_1(\A) + \lambda_1(\B) \) for every unit \( \x \). Weyl's inequalities are what happens when this easy observation is run at every index instead of only at the two ends.
:::

::: {.warning}
**The eigenvalues are not subadditive index by index.** It is tempting to read Weyl as \( \lambda_i(\A+\B) \le \lambda_i(\A) + \lambda_i(\B) \), and that statement is false. Take \( \A = \diag(1, 0) \) and \( \B = \diag(0, 1) \), so that \( \lambda(\A) = \lambda(\B) = (1, 0) \) and \( \A + \B = \I_2 \) with \( \lambda(\A+\B) = (1, 1) \). At \( i = 2 \) the proposed inequality reads \( 1 \le 0 + 0 \). The reverse reading \( \lambda_i(\A+\B) \ge \lambda_i(\A) + \lambda_i(\B) \) fails on the same pair at \( i = 1 \), where it reads \( 1 \ge 2 \). Only the shifted indices \( i+j-1 \) and \( i+j-n \) are correct.
:::

Here is the theorem in full on one pair of matrices, so that the index arithmetic can be seen doing its work.

::: {#exm-weyl-table}
[Both families on one pair]

Let
\[
\A = \begin{pmatrix} 1 & 1 & 2 \\ 1 & 1 & 2 \\ 2 & 2 & 0 \end{pmatrix},
\qquad
\B = \begin{pmatrix} 3 & 2 & 0 \\ 2 & 3 & 0 \\ 0 & 0 & 0 \end{pmatrix} .
\]
Find the eigenvalues of \( \A \), \( \B \) and \( \A + \B \), and check every inequality of @thm-weyl-inequalities.
:::

::: {.solution}
All three matrices are real symmetric. Their characteristic polynomials factor over \( \nZ \):
\[
\begin{aligned}
p_{\A}(x) &= x(x-4)(x+2), \\
p_{\B}(x) &= x(x-5)(x-1), \\
p_{\A+\B}(x) &= (x-8)(x-1)(x+1) ,
\end{aligned}
\]
so, in decreasing order,
\[
\lambda(\A) = (4, 0, -2), \qquad
\lambda(\B) = (5, 1, 0), \qquad
\lambda(\A+\B) = (8, 1, -1) .
\]
For \( \A \) one can see the list without computing: the rows \( (1,1,2) \) and \( (1,1,2) \) are equal, so \( \rank \A = 2 \) and \( 0 \) is an eigenvalue; \( \tr\A = 2 \) and \( \tr(\A^2) = 20 \) then force the other two to be \( 4 \) and \( -2 \).

With \( n = 3 \), family (a) applies when \( i + j \le 4 \) and family (b) when \( i + j \ge 4 \).

| \( (i,j) \) | family (a): \( \lambda_{i+j-1}(\A+\B) \le \lambda_i(\A) + \lambda_j(\B) \) |
|---|---|
| \( (1,1) \) | \( 8 \le 4 + 5 = 9 \) |
| \( (1,2) \) | \( 1 \le 4 + 1 = 5 \) |
| \( (2,1) \) | \( 1 \le 0 + 5 = 5 \) |
| \( (1,3) \) | \( -1 \le 4 + 0 = 4 \) |
| \( (2,2) \) | \( -1 \le 0 + 1 = 1 \) |
| \( (3,1) \) | \( -1 \le -2 + 5 = 3 \) |

| \( (i,j) \) | family (b): \( \lambda_{i+j-3}(\A+\B) \ge \lambda_i(\A) + \lambda_j(\B) \) |
|---|---|
| \( (1,3) \) | \( 8 \ge 4 + 0 = 4 \) |
| \( (3,1) \) | \( 8 \ge -2 + 5 = 3 \) |
| \( (2,2) \) | \( 8 \ge 0 + 1 = 1 \) |
| \( (2,3) \) | \( 1 \ge 0 + 0 = 0 \) |
| \( (3,2) \) | \( 1 \ge -2 + 1 = -1 \) |
| \( (3,3) \) | \( -1 \ge -2 + 0 = -2 \) |

Every inequality holds, and every one of them is strict. At \( (1,1) \) one can see why. Equality there would mean a unit \( \x \) with \( R_{\A+\B}(\x) = \lambda_1(\A) + \lambda_1(\B) \); since \( R_{\A}(\x) \le \lambda_1(\A) \) and \( R_{\B}(\x) \le \lambda_1(\B) \) by @lem-rayleigh-on-eigenspan (a) at \( i = 1 \), both would have to be equalities, and the computation in that proof shows that equality in \( \sum_p \lambda_p\lvert c_p\rvert^2 \le \lambda_1\sum_p \lvert c_p\rvert^2 \) forces \( c_p = 0 \) at every \( p \) with \( \lambda_p < \lambda_1 \). So \( \x \) would lie in the \( \lambda_1 \)-eigenspace of \( \A \) and in that of \( \B \). Those are the lines through \( (1,1,1) \) and through \( (1,1,0) \) — as \( \A(1,1,1) = 4(1,1,1) \) and \( \B(1,1,0) = 5(1,1,0) \), and both eigenvalues are simple — and two distinct lines meet only at \( \0 \).
:::

## Perturbing one matrix

Setting \( j = 1 \) in family (a) and \( j = n \) in family (b) leaves the index on the left equal to \( i \). That is the case in which Weyl becomes a statement about *perturbation*: one matrix, moved.

::: {#cor-weyl-monotone}
[Perturbation, Two-Sided]

Let \( \A, \B \in M_n(F) \) be Hermitian. Then for every \( i \),
\[
\lambda_i(\A) + \lambda_n(\B) \ \le\ \lambda_i(\A + \B) \ \le\ \lambda_i(\A) + \lambda_1(\B) .
\]
:::

::: {.proof}
For the upper bound take \( j = 1 \) in @thm-weyl-inequalities (a): the hypothesis \( i + 1 - 1 = i \le n \) holds, and the conclusion is \( \lambda_i(\A+\B) \le \lambda_i(\A) + \lambda_1(\B) \). For the lower bound take \( j = n \) in @thm-weyl-inequalities (b): the hypothesis \( i + n - n = i \ge 1 \) holds, and the conclusion is \( \lambda_i(\A+\B) \ge \lambda_i(\A) + \lambda_n(\B) \). This proves the corollary.
:::

In words: adding \( \B \) shifts each eigenvalue of \( \A \), in order, by an amount trapped between the smallest and the largest eigenvalue of \( \B \). Taking \( \B \succeq 0 \), so that \( \lambda_n(\B) \ge 0 \) by @thm-psd-characterizations (b), the lower bound becomes \( \lambda_i(\A+\B) \ge \lambda_i(\A) \) — which is @cor-loewner-eigenvalue-monotone again, now as a special case of Weyl's inequalities.

To turn @cor-weyl-monotone into a bound of the kind Chapter 16 wanted, the two numbers \( \lambda_1(\B) \) and \( \lambda_n(\B) \) must be replaced by one, and the right one is a norm.

::: {#lem-hermitian-spectral-norm}
[The Spectral Norm of a Hermitian Matrix]

Let \( \E \in M_n(F) \) be Hermitian. Then
\[
\norm{\E}_2 = \max_{1 \le i \le n}\lvert \lambda_i(\E)\rvert = \max\bigl(\lambda_1(\E),\ -\lambda_n(\E)\bigr) .
\]
:::

::: {.proof}
By the spectral theorem, \( \E = \U\D\U^{*} \) with \( \U \) unitary and \( \D = \diag(\lambda_1(\E), \dots, \lambda_n(\E)) \) real. Then
\[
\E^{*}\E = \E^2 = \U\D^2\U^{*} ,
\]
so the eigenvalues of \( \E^{*}\E \) are the numbers \( \lambda_i(\E)^2 \), and the singular values of \( \E \), which are their non-negative square roots listed decreasingly (@def-singular-values), are the numbers \( \lvert\lambda_i(\E)\rvert \) listed decreasingly. Hence \( \sigma_1(\E) = \max_i \lvert\lambda_i(\E)\rvert \), and \( \norm{\E}_2 = \sigma_1(\E) \) by @thm-operator-norm-formulas (c).

For the second equality, \( \lambda_n(\E) \le \lambda_i(\E) \le \lambda_1(\E) \) for every \( i \) gives \( \lvert\lambda_i(\E)\rvert \le \max(\lvert\lambda_1(\E)\rvert, \lvert\lambda_n(\E)\rvert) \), so the maximum is attained at one end of the list. Now \( \lambda_1(\E) \le \lvert\lambda_1(\E)\rvert \) and \( -\lambda_n(\E) \le \lvert\lambda_n(\E)\rvert \), which gives one inequality between the two expressions. Conversely, \( \lvert\lambda_1(\E)\rvert \) is either \( \lambda_1(\E) \) or \( -\lambda_1(\E) \le -\lambda_n(\E) \), and \( \lvert\lambda_n(\E)\rvert \) is either \( -\lambda_n(\E) \) or \( \lambda_n(\E) \le \lambda_1(\E) \); in every case it is at most \( \max(\lambda_1(\E), -\lambda_n(\E)) \). This proves the lemma.
:::

::: {#cor-weyl-perturbation}
[Hermitian Eigenvalues Are 1-Lipschitz]

Let \( \A, \E \in M_n(F) \) be Hermitian. Then
\[
\lvert \lambda_i(\A + \E) - \lambda_i(\A)\rvert \ \le\ \norm{\E}_2
\qquad \text{for every } i = 1, \dots, n .
\]
:::

::: {.proof}
By @cor-weyl-monotone applied with \( \B = \E \),
\[
\lambda_n(\E) \ \le\ \lambda_i(\A+\E) - \lambda_i(\A) \ \le\ \lambda_1(\E) .
\]
By @lem-hermitian-spectral-norm, \( \lambda_1(\E) \le \norm{\E}_2 \) and \( -\lambda_n(\E) \le \norm{\E}_2 \), that is, \( -\norm{\E}_2 \le \lambda_n(\E) \). So the difference lies in \( [-\norm{\E}_2, \norm{\E}_2] \), which is the assertion. This proves the corollary.
:::

This is the sentence Chapter 16 §07 promised: **the eigenvalues of a Hermitian matrix move by at most \( \norm{\E}_2 \) under a Hermitian perturbation.** It is worth being precise about what it adds to @cor-eigenvalues-continuous, the continuity statement of that section, because the gain is not continuity — that was already had — but a constant.

- @cor-eigenvalues-continuous says: for each \( \A \) and each \( \varepsilon > 0 \) there is a \( \delta > 0 \) such that every matrix within \( \delta \) of \( \A \) has eigenvalues that can be numbered to lie within \( \varepsilon \) of those of \( \A \). The \( \delta \) depends on \( \A \), and @exm-jordan-block-perturbation shows that it must.
- @cor-weyl-perturbation says, for Hermitian \( \A \) and Hermitian perturbations measured in \( \norm{\cdot}_2 \): \( \delta = \varepsilon \) works, for every \( \A \) at once, and the numbering is simply the decreasing order. The movement is bounded by the perturbation itself, with **Lipschitz constant \( 1 \)**.

The constant does not depend on the size \( n \) of the matrices, it does not depend on how ill-conditioned \( \A \) is, and it does not depend on how close together the eigenvalues of \( \A \) are — three quantities that every reader of Chapter 16 has learned to expect in an error bound. It also cannot be improved: \( \E = t\I \) with \( t \in \nR \) gives \( \lambda_i(\A + t\I) = \lambda_i(\A) + t \) for every \( i \), while \( \norm{t\I}_2 = \lvert t\rvert \), so the inequality is an equality at every index. Finally, the eigenvalues are matched **by index**: the \( i \)-th of \( \A + \E \) is compared with the \( i \)-th of \( \A \), not with whichever eigenvalue of \( \A \) happens to be nearest, and no search for a good numbering is needed.

::: {#cor-hermitian-eigenvalues-well-conditioned}
[The Hermitian Eigenvalue Problem Is Perfectly Conditioned in Absolute Terms]

Let \( \A, \E \in M_n(F) \) be Hermitian and write \( \lambda(\A) = (\lambda_1(\A), \dots, \lambda_n(\A)) \) for the decreasing eigenvalue list. Then
\[
\norm{\lambda(\A + \E) - \lambda(\A)}_{\infty} \ \le\ \norm{\E}_2 ,
\]
and the constant \( 1 \) is the smallest one for which this holds.
:::

::: {.proof}
The \( \infty \)-norm of a vector is the largest modulus of its entries, so the left-hand side is \( \max_i\lvert\lambda_i(\A+\E) - \lambda_i(\A)\rvert \), and the inequality is @cor-weyl-perturbation read over all \( i \) at once. For the last clause, \( \E = t\I \) with \( t > 0 \) makes both sides equal to \( t \), so no constant below \( 1 \) can work. This proves the corollary.
:::

Chapter 16 §08 measured a linear system by \( \kappa(\A) = \norm{\A}\norm{\A^{-1}} \) (@def-condition-number), the worst factor by which \( \A \) magnifies a relative error in the data. The corollary above is the corresponding statement for a different problem — not "solve \( \A\x = \b \)" but "report the eigenvalues of \( \A \)" — and the factor there is \( 1 \), in absolute rather than relative terms. The difference between absolute and relative matters here, and it is worth being exact. \( \A = \diag(10^{6}, 10^{-6}) \) is Hermitian with \( \kappa_2(\A) = 10^{12} \), so solving with it is a delicate business, and yet its eigenvalues move by at most \( \norm{\E}_2 \) under any Hermitian \( \E \), exactly as those of every other Hermitian matrix do. **Ill-conditioning of the linear system says nothing about the *absolute* conditioning of the eigenvalues.** In *relative* terms the two numbers meet again. The Hermitian perturbation \( \E = -10^{-6}\,\e_2\e_2\tp \) has relative size \( \norm{\E}_2/\norm{\A}_2 = 10^{-12} \) and sends the eigenvalue \( 10^{-6} \) to \( 0 \), a relative change of \( 100\% \): an amplification of exactly \( 10^{12} = \kappa_2(\A) \). In general, for an invertible Hermitian \( \A \), @cor-weyl-perturbation bounds the relative change of the eigenvalue of smallest modulus by \( \norm{\E}_2/\sigma_n(\A) \), which is \( \kappa_2(\A) \) times the relative size of \( \E \), and a rank-one \( \E \) along its eigenvector attains it. So for Hermitian matrices, \( \kappa_2 \) *is* the relative condition number of the smallest eigenvalue.

The contrast that makes the corollary worth having is with @exm-jordan-block-perturbation. There \( \A = \J_k(0) \) and \( \E = \varepsilon\E_{k1} \), and the eigenvalues move a distance \( \varepsilon^{1/k} \) while \( \norm{\E}_2 = \varepsilon \), an amplification of \( \varepsilon^{-(k-1)/k} \) that is unbounded as \( \varepsilon \to 0^{+} \). Neither matrix there is Hermitian, and @cor-weyl-perturbation explains which hypothesis is doing the work: for \( k = 2 \) the perturbed matrix \( \begin{psmallmatrix} 0 & 1 \\ \varepsilon & 0\end{psmallmatrix} \) has the perfectly real eigenvalues \( \pm\sqrt{\varepsilon} \), so the conclusion of @cor-weyl-perturbation can be *stated* for it, and it is false — \( \sqrt{\varepsilon} > \varepsilon \) for \( 0 < \varepsilon < 1 \), by a factor of \( 1000 \) at \( \varepsilon = 10^{-6} \).

::: {.warning}
**Both matrices must be Hermitian, and "small" is no substitute.** If \( \A \) is not Hermitian, the corollary fails even when \( \E \) is: take \( \A = \J_2(0) \) and the Hermitian \( \E = \varepsilon\begin{psmallmatrix} 0 & 1 \\ 1 & 0\end{psmallmatrix} \), with \( \norm{\E}_2 = \varepsilon \). Then \( \A + \E = \begin{psmallmatrix} 0 & 1+\varepsilon \\ \varepsilon & 0\end{psmallmatrix} \) has the real eigenvalues \( \pm\sqrt{\varepsilon(1+\varepsilon)} \), which have moved from \( 0 \) by more than \( \varepsilon \). If \( \E \) is not Hermitian, the conclusion usually cannot even be stated: \( \A = \0 \) is Hermitian and \( \E = \begin{psmallmatrix} 0 & -1 \\ 1 & 0\end{psmallmatrix} \) has \( \norm{\E}_2 = 1 \), but \( \A + \E \) has eigenvalues \( \pm i \), so there is no decreasing list \( \lambda_i(\A+\E) \) of real numbers to compare with anything. A bound for a diagonalizable \( \A \) and an arbitrary \( \E \) does exist — the theorem of Bauer and Fike, in Chapter 20 — and it carries an extra factor that measures how far the eigenvector basis of \( \A \) is from orthonormal.
:::

::: {#exm-weyl-perturbation-estimate}
[Locating eigenvalues without recomputing them]

Let
\[
\A = \begin{pmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2\end{pmatrix},
\qquad
\E = \tfrac{1}{10}\bigl(\E_{13} + \E_{31}\bigr) .
\]
Use @cor-weyl-perturbation to locate the eigenvalues of \( \A + \E \), then compute them exactly and compare.
:::

::: {.solution}
*The unperturbed spectrum.* Expanding along the first row, \( p_{\A}(x) = (x-2)\bigl((x-2)^2 - 2\bigr) \), so
\[
\lambda(\A) = \bigl(2 + \sqrt2,\ 2,\ 2 - \sqrt2\bigr) \approx (3.41421,\ 2,\ 0.58579) .
\]

*The size of the perturbation.* \( \E \) is real symmetric with \( \E^2 = \tfrac{1}{100}(\E_{11} + \E_{33}) \), whose eigenvalues are \( \tfrac{1}{100}, \tfrac1{100}, 0 \); so the singular values of \( \E \) are \( \tfrac1{10}, \tfrac1{10}, 0 \) and \( \norm{\E}_2 = \tfrac1{10} \) by @thm-operator-norm-formulas (c). (One can also read this off @lem-hermitian-spectral-norm: the eigenvalues of \( \E \) are \( \tfrac1{10}, 0, -\tfrac1{10} \).)

*The prediction.* By @cor-weyl-perturbation each eigenvalue of \( \A + \E \) lies within \( \tfrac1{10} \) of the corresponding eigenvalue of \( \A \):
\[
\lambda_1 \in [3.31421,\ 3.51421], \qquad
\lambda_2 \in [1.9,\ 2.1], \qquad
\lambda_3 \in [0.48579,\ 0.68579] .
\]
In particular \( \A + \E \) is positive definite, since \( \lambda_3 > 0 \), and its three eigenvalues are distinct, since the three intervals are disjoint.

*The check.* The characteristic polynomial of \( \A + \E \) factors as
\[
p_{\A+\E}(x) = \Bigl(x - \tfrac{19}{10}\Bigr)\Bigl(x^2 - \tfrac{41}{10}x + \tfrac{11}{5}\Bigr) ,
\]
so
\[
\begin{aligned}
\lambda(\A+\E) &= \Bigl(\tfrac{41 + 3\sqrt{89}}{20},\ \tfrac{19}{10},\ \tfrac{41 - 3\sqrt{89}}{20}\Bigr) \\
&\approx (3.46510,\ 1.9,\ 0.63490) .
\end{aligned}
\]
All three lie in the predicted intervals. The middle one lies at the very end of its interval: \( \lambda_2 \) has moved by exactly \( \tfrac1{10} = \norm{\E}_2 \). That is not luck. The vector \( (1, 0, -1) \) is an eigenvector of \( \A \) for \( 2 \) and of \( \E \) for \( -\tfrac1{10} \), hence an eigenvector of \( \A + \E \) for \( 2 - \tfrac1{10} \); a shared eigenvector is exactly what makes the bound tight.
:::

## Perturbations of small rank

The last corollary trades size for rank. A perturbation of rank \( r \) need not be small in norm at all, but it can only disturb \( r \) directions, and Weyl converts that into a shift of the index by \( r \).

::: {#cor-weyl-rank-bound}
[A Rank-\( r \) Perturbation Shifts the Index by \( r \)]

Let \( \A, \B \in M_n(F) \) be Hermitian, let \( r \ge 0 \) be an integer, and suppose \( \rank\B \le r \). Then
\[
\begin{aligned}
\lambda_{i+r}(\A + \B) &\ \le\ \lambda_i(\A) &&(1 \le i,\ i + r \le n), \\
\lambda_i(\A) &\ \le\ \lambda_{i-r}(\A + \B) &&(i \le n,\ i - r \ge 1) .
\end{aligned}
\]
:::

::: {.idea}
A Hermitian matrix of rank at most \( r \) has at most \( r \) non-zero eigenvalues, so once one walks \( r+1 \) places down its decreasing list one is certainly at a non-positive number, and once one stops \( r \) places short of the bottom one is certainly at a non-negative number. Feed those two facts into the two Weyl families at \( j = r+1 \) and \( j = n-r \).
:::

::: {.proof}
By the spectral theorem \( \B = \U\D\U^{*} \) with \( \D = \diag(\lambda_1(\B), \dots, \lambda_n(\B)) \) and \( \U \) unitary, so \( \rank\B = \rank\D \) is the number of non-zero \( \lambda_q(\B) \), which is at most \( r \) by hypothesis.

*Two facts about the list of \( \B \).* If \( \lambda_{r+1}(\B) > 0 \), then \( \lambda_1(\B), \dots, \lambda_{r+1}(\B) \) are all positive by the decreasing indexing, giving \( r + 1 \) non-zero eigenvalues, a contradiction; hence
\[
\lambda_{r+1}(\B) \le 0 \qquad \text{whenever } r + 1 \le n .
\]
If \( \lambda_{n-r}(\B) < 0 \), then \( \lambda_{n-r}(\B), \dots, \lambda_n(\B) \) are all negative, again \( r+1 \) non-zero eigenvalues and a contradiction; hence
\[
\lambda_{n-r}(\B) \ge 0 \qquad \text{whenever } n - r \ge 1 .
\]

*First inequality.* Assume \( i \ge 1 \) and \( i + r \le n \); then \( r + 1 \le n \), so the index \( j = r+1 \) is legitimate and \( i + j - 1 = i + r \le n \). By @thm-weyl-inequalities (a) and the first fact,
\[
\lambda_{i+r}(\A+\B) \le \lambda_i(\A) + \lambda_{r+1}(\B) \le \lambda_i(\A) .
\]

*Second inequality.* Assume \( i \le n \) and \( i - r \ge 1 \); then \( n - r \ge n - i + 1 \ge 1 \), so the index \( j = n - r \) is legitimate, and \( i + j - n = i - r \ge 1 \). By @thm-weyl-inequalities (b) and the second fact,
\[
\lambda_{i-r}(\A+\B) \ge \lambda_i(\A) + \lambda_{n-r}(\B) \ge \lambda_i(\A) .
\]
This proves the corollary.
:::

Read together, the two inequalities say that the two eigenvalue lists interlace with a lag of \( r \):
\[
\lambda_{i+r}(\A+\B) \ \le\ \lambda_i(\A) \ \le\ \lambda_{i-r}(\A+\B) ,
\]
whenever all three indices make sense. For \( r = 0 \) this collapses to \( \lambda_i(\A+\B) = \lambda_i(\A) \), correctly, since a Hermitian matrix of rank \( 0 \) is \( \0 \). For \( r = 1 \) it is the statement that adding a Hermitian rank-one matrix moves each eigenvalue by at most one place in the list. That case is the subject of Section 5, and Section 9 returns to low-rank perturbations when it finishes the approximation theorem that Chapter 13 §10 could only state in the Frobenius norm.

::: {.remark}
The bound is about the *index*, not the *value*. A rank-one \( \B \) can be enormous: \( \B = 10^{6}\,\e_1\e_1^{*} \) has rank \( 1 \), and \( \lambda_1(\A + \B) \) lies within \( \norm{\A}_2 \) of \( 10^{6} \), by @cor-weyl-perturbation with the roles of the two matrices exchanged. What @cor-weyl-rank-bound guarantees is that the others are trapped all the same: \( \lambda_{k+1}(\A) \le \lambda_k(\A+\B) \le \lambda_{k-1}(\A) \) for \( 2 \le k \le n-1 \), however large the one that escapes.
:::

## Exercises

### A. Check your understanding

:::: {#exr-weyl-inequalities-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State both families of @thm-weyl-inequalities, with their index conditions, and say why the condition \( i + j - 1 \le n \) cannot be dropped from the first.
2. Determine whether the following is correct, and justify your answer: for Hermitian \( \A, \B \), \( \lambda_2(\A+\B) \le \lambda_2(\A) + \lambda_2(\B) \).
3. @cor-eigenvalues-continuous already said that eigenvalues move continuously. What does @cor-weyl-perturbation add?
4. Explain why @cor-weyl-perturbation cannot be applied to \( \A = \J_2(0) \) and \( \E = \varepsilon\E_{21} \), and what goes wrong if one applies it anyway.
5. If \( \B \) is Hermitian of rank \( 3 \) and \( \A \) is Hermitian of size \( 10 \), which eigenvalue of \( \A + \B \) is guaranteed to be at most \( \lambda_4(\A) \)?
:::
::::

::: {.solution}
(a) See @thm-weyl-inequalities. Family (a) needs \( i + j - 1 \le n \) and family (b) needs \( i + j - n \ge 1 \). Without the first condition the symbol \( \lambda_{i+j-1}(\A+\B) \) names nothing: a matrix of size \( n \) has only \( n \) eigenvalues, and there is no \( \lambda_{n+1} \).

(b) Incorrect. With \( \A = \diag(1,0) \) and \( \B = \diag(0,1) \) it reads \( \lambda_2(\I_2) = 1 \le 0 + 0 \). The correct instance of @thm-weyl-inequalities (a) at \( i = j = 2 \) needs \( i + j - 1 = 3 \le n \), so it says nothing when \( n = 2 \); when \( n \ge 3 \) it bounds \( \lambda_3 \), not \( \lambda_2 \).

(c) A constant. @cor-eigenvalues-continuous gives, for each \( \A \) and \( \varepsilon \), some unspecified \( \delta \) depending on \( \A \); @cor-weyl-perturbation gives \( \delta = \varepsilon \) for every \( \A \) simultaneously, that is, a Lipschitz constant of \( 1 \), independent of \( n \), of the conditioning of \( \A \) and of the gaps between its eigenvalues. It also matches the eigenvalues by index rather than as a multiset.

(d) Neither matrix is Hermitian, and the corollary's hypothesis is that both are. Applying it anyway predicts movement at most \( \norm{\E}_2 = \varepsilon \), whereas the eigenvalues are \( \pm\sqrt\varepsilon \) and have moved a distance \( \sqrt\varepsilon \), which exceeds \( \varepsilon \) for every \( \varepsilon \in (0,1) \) — see @exm-jordan-block-perturbation.

(e) \( \lambda_7(\A+\B) \), and hence every later one, by @cor-weyl-rank-bound with \( i = 4 \) and \( r = 3 \).
:::

### B. Practice

:::: {#exr-weyl-inequalities-b1}
[B1: A small table]

Let \( \A = \begin{pmatrix} 0 & 4 \\ 4 & 0\end{pmatrix} \) and \( \B = \begin{pmatrix} 3 & 0 \\ 0 & -3\end{pmatrix} \). Compute the eigenvalues of \( \A \), \( \B \) and \( \A + \B \), write out every inequality of @thm-weyl-inequalities for this pair, and verify @cor-weyl-perturbation with \( \E = \B \).
::::

::: {.solution}
\( p_{\A}(x) = x^2 - 16 \), so \( \lambda(\A) = (4, -4) \); \( \B \) is diagonal, so \( \lambda(\B) = (3, -3) \); and \( \A + \B = \begin{psmallmatrix} 3 & 4 \\ 4 & -3\end{psmallmatrix} \) has \( \tr = 0 \) and \( \det = -25 \), so \( p_{\A+\B}(x) = x^2 - 25 \) and \( \lambda(\A+\B) = (5, -5) \).

Family (a), for \( i + j \le 3 \):
\[
\begin{aligned}
(1,1) &: \ 5 \le 4 + 3 = 7, \\
(1,2) &: \ -5 \le 4 - 3 = 1, \\
(2,1) &: \ -5 \le -4 + 3 = -1 .
\end{aligned}
\]
Family (b), for \( i + j \ge 3 \):
\[
\begin{aligned}
(1,2) &: \ 5 \ge 4 - 3 = 1, \\
(2,1) &: \ 5 \ge -4 + 3 = -1, \\
(2,2) &: \ -5 \ge -4 - 3 = -7 .
\end{aligned}
\]
All six hold. For the last part, \( \B \) is Hermitian with eigenvalues \( \pm 3 \), so \( \norm{\B}_2 = 3 \) by @lem-hermitian-spectral-norm, and
\[
\begin{aligned}
\lvert\lambda_1(\A+\B) - \lambda_1(\A)\rvert &= \lvert 5 - 4\rvert = 1 \le 3, \\
\lvert\lambda_2(\A+\B) - \lambda_2(\A)\rvert &= \lvert -5 + 4\rvert = 1 \le 3 ,
\end{aligned}
\]
as @cor-weyl-perturbation requires.
:::

:::: {#exr-weyl-inequalities-b2}
[B2: An interval for each eigenvalue]

Let \( \A = \begin{pmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2\end{pmatrix} \), whose eigenvalues are \( 2 \pm \sqrt2 \) and \( 2 \), and let \( \E = \tfrac{1}{100}\J \), where \( \J \in M_3(\nR) \) is the all-ones matrix.

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \norm{\E}_2 \) and give an interval containing each eigenvalue of \( \A + \E \).
2. Deduce that \( \A + \E \) is positive definite.
:::
::::

::: {.solution}
(a) \( \J \) is real symmetric with \( \J^2 = 3\J \), so its eigenvalues satisfy \( \lambda^2 = 3\lambda \) and are \( 3 \) and \( 0 \); since \( \rank \J = 1 \) the list is \( (3, 0, 0) \). Hence \( \E \) has eigenvalues \( (\tfrac{3}{100}, 0, 0) \) and \( \norm{\E}_2 = \tfrac{3}{100} \) by @lem-hermitian-spectral-norm. By @cor-weyl-perturbation,
\[
\begin{aligned}
\lambda_1(\A+\E) &\in [3.38421,\ 3.44421], \\
\lambda_2(\A+\E) &\in [1.97,\ 2.03], \\
\lambda_3(\A+\E) &\in [0.55579,\ 0.61579] ,
\end{aligned}
\]
the centers being \( 2+\sqrt2 \approx 3.41421 \), \( 2 \) and \( 2 - \sqrt2 \approx 0.58579 \).

(b) Every interval lies strictly to the right of \( 0 \), so all three eigenvalues of the Hermitian matrix \( \A + \E \) are positive and \( \A + \E \succ 0 \) by @thm-pd-characterizations (b). No characteristic polynomial was computed. (For the record, the exact eigenvalues are \( 2 \) and \( \tfrac{403 \pm \sqrt{81609}}{200} \), that is \( 2 \), \( 3.44336\dots \) and \( 0.58664\dots \); the middle one is unmoved because \( (1,0,-1) \) is an eigenvector of both \( \A \) and \( \J \).)
:::

:::: {#exr-weyl-inequalities-b3}
[B3: What a low-rank update can do]

Let \( \A \in M_5(\nC) \) be Hermitian with \( \lambda(\A) = (5, 4, 3, 2, 1) \), and let \( \B \in M_5(\nC) \) be Hermitian with \( \rank\B \le 2 \). Find the best bounds that @cor-weyl-rank-bound gives for \( \lambda_3(\A+\B) \), and give examples showing that each is attained.
::::

::: {.solution}
Take \( r = 2 \). The first inequality reads \( \lambda_{i+2}(\A+\B) \le \lambda_i(\A) \), and it mentions \( \lambda_3(\A+\B) \) only at \( i = 1 \), giving \( \lambda_3(\A+\B) \le \lambda_1(\A) = 5 \). The second reads \( \lambda_i(\A) \le \lambda_{i-2}(\A+\B) \), and it mentions \( \lambda_3(\A+\B) \) only at \( i = 5 \), giving \( \lambda_3(\A+\B) \ge \lambda_5(\A) = 1 \). So the corollary gives exactly \( \lambda_3(\A+\B) \in [1, 5] \).

Both ends are attained. Write \( \A = \U\diag(5,4,3,2,1)\U^{*} \) with \( \U \) unitary (@cor-spectral-complex-matrix) and let \( \q_1, \dots, \q_5 \) be its columns, an orthonormal eigenbasis.

For the upper bound take \( \B = 4(\q_4\q_4^{*} + \q_5\q_5^{*}) \), which is Hermitian of rank \( 2 \). It adds \( 4 \) to the fourth and fifth eigenvalues and leaves the rest alone, so \( \A + \B = \U\diag(5,4,3,6,5)\U^{*} \), whose eigenvalue list sorted decreasingly is \( (6, 5, 5, 4, 3) \). Hence \( \lambda_3(\A+\B) = 5 = \lambda_1(\A) \).

For the lower bound take \( \B = -4(\q_1\q_1^{*} + \q_2\q_2^{*}) \), again Hermitian of rank \( 2 \). Then \( \A + \B = \U\diag(1, 0, 3, 2, 1)\U^{*} \), sorted \( (3, 2, 1, 1, 0) \), so \( \lambda_3(\A+\B) = 1 = \lambda_5(\A) \).
:::

### C. Going deeper

:::: {#exr-weyl-inequalities-c1}
[C1: The Loewner order through Weyl]

Let \( \A, \B \in M_n(F) \) be Hermitian.

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( \A \succeq \B \) then \( \lambda_i(\A) \ge \lambda_i(\B) \) for every \( i \), as a consequence of @cor-weyl-monotone.
2. Hence deduce that \( \lvert\lambda_i(\A) - \lambda_i(\B)\rvert \le \norm{\A - \B}_2 \) for every \( i \), without invoking @cor-weyl-perturbation.
:::
::::

::: {.solution}
(a) Put \( \C = \A - \B \), which is Hermitian, and \( \C \succeq 0 \) by hypothesis and @def-loewner-order. By @thm-psd-characterizations (b) every eigenvalue of \( \C \) is \( \ge 0 \), in particular \( \lambda_n(\C) \ge 0 \). Applying @cor-weyl-monotone to \( \B \) and \( \C \),
\[
\lambda_i(\A) = \lambda_i(\B + \C) \ \ge\ \lambda_i(\B) + \lambda_n(\C) \ \ge\ \lambda_i(\B) .
\]
This is @cor-loewner-eigenvalue-monotone.

(b) Put \( \C = \A - \B \) again, now with no sign hypothesis, and let \( t = \norm{\C}_2 \). By @lem-hermitian-spectral-norm, \( -t \le \lambda_n(\C) \) and \( \lambda_1(\C) \le t \), so \( t\I - \C \succeq 0 \) and \( \C + t\I \succeq 0 \) by @thm-psd-characterizations (b) applied to the Hermitian matrices \( t\I - \C \) and \( \C + t\I \), whose eigenvalues are \( t - \lambda_q(\C) \) and \( \lambda_q(\C) + t \). Hence \( \B + t\I \succeq \A \succeq \B - t\I \), and part (a) gives
\[
\begin{aligned}
\lambda_i(\B) + t &= \lambda_i(\B + t\I) \ \ge\ \lambda_i(\A) , \\
\lambda_i(\A) &\ge \lambda_i(\B - t\I) = \lambda_i(\B) - t ,
\end{aligned}
\]
using \( \lambda_i(\M + s\I) = \lambda_i(\M) + s \) for real \( s \), which holds because \( \M \) and \( \M + s\I \) have the same eigenvectors with eigenvalues shifted by \( s \), and shifting by a constant preserves the decreasing order. Rearranged, this is \( \lvert\lambda_i(\A) - \lambda_i(\B)\rvert \le t \), as claimed.
:::

:::: {#exr-weyl-inequalities-c2}
[C2: The largest eigenvalue is a convex function]

Let \( \A, \B \in M_n(F) \) be Hermitian and let \( t \in [0,1] \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \lambda_1(t\A + (1-t)\B) \le t\lambda_1(\A) + (1-t)\lambda_1(\B) \).
2. Deduce that for every \( c \in \nR \) the set \( \{\M \in M_n(F) : \M^{*} = \M,\ \lambda_1(\M) \le c\} \) is convex.
3. Show that \( \lambda_2 \) is **not** convex in this sense, by producing two Hermitian \( 2 \times 2 \) matrices and a value of \( t \) where the inequality fails.
:::
::::

::: {.solution}
(a) For \( s \ge 0 \) and Hermitian \( \M \) we have \( \lambda_1(s\M) = s\lambda_1(\M) \), since \( s\M = \U(s\D)\U^{*} \) and multiplying a decreasing list of reals by \( s \ge 0 \) keeps it decreasing. By @thm-weyl-inequalities (a) at \( i = j = 1 \), applied to the Hermitian matrices \( t\A \) and \( (1-t)\B \),
\[
\lambda_1\bigl(t\A + (1-t)\B\bigr) \le \lambda_1(t\A) + \lambda_1\bigl((1-t)\B\bigr)
= t\lambda_1(\A) + (1-t)\lambda_1(\B) .
\]

(b) Let \( \A, \B \) lie in the set and let \( t \in [0,1] \). The matrix \( t\A + (1-t)\B \) is Hermitian, and by (a) its largest eigenvalue is at most \( tc + (1-t)c = c \). So the set contains the whole segment between any two of its points.

(c) Take \( \A = \diag(1, 0) \), \( \B = \diag(0, 1) \) and \( t = \tfrac12 \). Then \( \lambda_2(\A) = \lambda_2(\B) = 0 \), while \( t\A + (1-t)\B = \tfrac12\I_2 \) has \( \lambda_2 = \tfrac12 \). So \( \tfrac12 \le \tfrac12\cdot 0 + \tfrac12\cdot 0 = 0 \) is false. The reason is visible in @thm-weyl-inequalities: at \( i = j = 2 \) the index on the left is \( 3 \), not \( 2 \).
:::

:::: {#exr-weyl-inequalities-c3}
[C3: Sharpness of the whole family]

Fix \( n \) and indices \( i, j \) with \( i + j - 1 \le n \). Construct Hermitian \( \A, \B \in M_n(\nR) \), both diagonal, for which
\[
\lambda_{i+j-1}(\A+\B) = \lambda_i(\A) + \lambda_j(\B) .
\]

*Hint: with diagonal matrices every quantity in sight is a sorting problem; arrange for the \( (i+j-1) \)-st largest entry of the sum to sit in a coordinate where \( \A \) contributes its \( i \)-th largest and \( \B \) its \( j \)-th largest.*
::::

::: {.solution}
Let \( k = i + j - 1 \) and let \( \A = \diag(a_1, \dots, a_n) \) and \( \B = \diag(b_1, \dots, b_n) \) with
\[
a_p = \begin{cases} 1 & p \le i - 1, \\ 0 & p \ge i,\end{cases}
\qquad
b_p = \begin{cases} 0 & p \le i-1, \\ 1 & i \le p \le k, \\ 0 & p > k .\end{cases}
\]
Both are diagonal with entries \( 0 \) and \( 1 \), hence Hermitian, and their diagonals are already their eigenvalue lists up to sorting. The matrix \( \A \) has \( i - 1 \) entries equal to \( 1 \), so \( \lambda_i(\A) = 0 \). The matrix \( \B \) has \( k - i + 1 = j \) entries equal to \( 1 \), so \( \lambda_j(\B) = 1 \). The sum is \( \A + \B = \diag(1, \dots, 1, 0, \dots, 0) \) with exactly \( k \) ones, since the ones of \( \A \) occupy coordinates \( 1, \dots, i-1 \) and those of \( \B \) occupy \( i, \dots, k \), and these two sets of coordinates do not overlap. Hence \( \lambda_k(\A+\B) = 1 = \lambda_i(\A) + \lambda_j(\B) \).

Every inequality of the first family is therefore attained, for every admissible pair \( (i, j) \), already by \( 0 \)–\( 1 \) diagonal matrices. Applying @lem-eigenvalues-of-negation to \( -\A \) and \( -\B \), as in the proof of @thm-weyl-inequalities (b), turns this family of equalities into one showing that the second family is attained as well.
:::
