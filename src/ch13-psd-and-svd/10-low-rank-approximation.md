# Low-Rank Approximation

The compact singular value decomposition writes a matrix as a sum of rank-one pieces arranged in decreasing order of size. A sum can be cut short. This section shows that cutting it short after \( k \) terms produces the **best** approximation to \( \A \) by a matrix of rank \( k \), measured in the Frobenius norm, and that the error it leaves is a quantity we can write down before doing any work. One theorem answers three questions at once: how to compress a matrix, which \( k \)-dimensional subspace best fits a cloud of data, and how far a given matrix is from being singular.

Throughout, \( F = \nR \) or \( F = \nC \), \( \A \in M_{m \times n}(F) \), \( p = \min(m, n) \), \( r = \rank\A \), and
\[
\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_p \ge 0
\]
are the singular values of \( \A \) (@def-singular-values), so that \( \sigma_i > 0 \) exactly for \( i \le r \). We fix a singular value decomposition \( \A = \U\vSigma\V^{*} \) (@thm-svd) and write \( \u_1, \dots, \u_m \) for the columns of \( \U \) and \( \v_1, \dots, \v_n \) for the columns of \( \V \).

## Cutting the sum short

Multiplying out \( \U\vSigma\V^{*} \) column by column gives the rank-one expansion
\[
\A = \sum_{i=1}^{p} \sigma_i\u_i\v_i^{*} = \sum_{i=1}^{r} \sigma_i\u_i\v_i^{*} ,
\]
the second equality because the terms with \( i > r \) have \( \sigma_i = 0 \); this is the compact form @thm-compact-svd. Each summand is a matrix of rank one, and the coefficients decrease. The natural thing to do with such a sum is to keep the large terms and discard the small ones.

*Keep the first \( k \) rank-one pieces and throw the rest away.*

::: {#def-truncated-svd}
[Truncated singular value decomposition]

For \( 0 \le k \le p \), the **rank-\( k \) truncation** of \( \A \) relative to the chosen singular value decomposition \( \A = \U\vSigma\V^{*} \) (@thm-svd) is
\[
\A_k \coloneqq \sum_{i=1}^{k} \sigma_i\u_i\v_i^{*} ,
\]
with \( \A_0 = \0 \); for \( k \ge p \) we set \( \A_k = \A \).
:::

Two clauses need comment. The subscript counts **terms kept**, not rows and columns: \( \A_k \) is the same size as \( \A \), not a submatrix of it. (Section 1 used \( \A_k \) for the top-left \( k \times k \) corner; that meaning is gone for the rest of this section.) And the definition says "relative to the chosen decomposition", because @thm-singular-values-unique leaves the unitary factors some freedom, and different choices can give different truncations. Everything proved below holds for **every** choice; the warning at the end of the section shows that the dependence is real.

The rank of \( \A_k \) is exactly \( \min(k, r) \): the vectors \( \u_1, \dots, \u_k \) are orthonormal, hence independent, so the columns of \( \A_k \) span \( \Span(\u_1, \dots, \u_{\min(k,r)}) \) once the vanishing terms are dropped.

::: {#exm-truncation-diagonal}
[Truncating a diagonal matrix]

Let \( \A = \diag(5, 3, 1) \in M_3(\nR) \). Write down \( \A_1 \) and \( \A_2 \).
:::

::: {.solution}
A diagonal matrix with positive decreasing entries is already in the form \( \U\vSigma\V^{*} \) with \( \U = \V = \I_3 \), so \( \sigma_i = 5, 3, 1 \) and \( \u_i = \v_i = \e_i \). Hence
\[
\A_1 = 5\e_1\e_1^{*} = \diag(5, 0, 0), \qquad \A_2 = \diag(5, 3, 0) .
\]
Truncation of a diagonal matrix is just deleting its smallest diagonal entries. Everything in this section is this statement, conjugated by two unitary matrices.
:::

The first thing to compute is how much was thrown away.

::: {#lem-frobenius-sum-of-squares}
[The Frobenius norm counts singular values]

Let \( \A \in M_{m \times n}(F) \) have singular values \( \sigma_1 \ge \dots \ge \sigma_p \). Then (the first identity is the one Section 8 already obtained, recorded here with a label because the proof of the main theorem uses it repeatedly)
\[
\norm{\A}_F^2 = \sum_{i=1}^{p} \sigma_i^2 ,
\qquad
\norm{\A - \A_k}_F^2 = \sum_{i > k} \sigma_i^2
\]
for every \( 0 \le k \le p \).
:::

::: {.proof}
The Frobenius norm does not see unitary factors (@lem-frobenius-unitarily-invariant), so from \( \A = \U\vSigma\V^{*} \),
\[
\norm{\A}_F = \norm{\vSigma\V^{*}}_F = \norm{\vSigma}_F .
\]
The only non-zero entries of \( \vSigma \) are \( \sigma_1, \dots, \sigma_p \) on the diagonal, so \( \norm{\vSigma}_F^2 = \sum_i \sigma_i^2 \).

For the second identity, subtract the first \( k \) terms of the rank-one expansion:
\[
\A - \A_k = \sum_{i > k} \sigma_i\u_i\v_i^{*} = \U\vSigma^{(k)}\V^{*} ,
\]
where \( \vSigma^{(k)} \) is \( \vSigma \) with its first \( k \) diagonal entries replaced by \( 0 \). Applying the first identity to this matrix — the display is a singular value decomposition of it in the sense of @thm-svd, up to reordering the diagonal — gives \( \norm{\A - \A_k}_F^2 = \sum_{i > k}\sigma_i^2 \).
:::

So the truncation error is decided in advance by the singular values, and it is small exactly when the discarded \( \sigma_i \) are small. The content of the section is that no other matrix of rank \( k \) does better.

::: {.check}
A matrix has singular values \( 5, 4, 3 \). What is the smallest \( k \) for which the relative error \( \norm{\A - \A_k}_F/\norm{\A}_F \) is at most \( \tfrac12 \)?
:::

::: {.solution}
By @lem-frobenius-sum-of-squares, \( \norm{\A}_F^2 = 25 + 16 + 9 = 50 \). For \( k = 1 \) the error squared is \( 16 + 9 = 25 \), so the relative error is \( \sqrt{25/50} = 1/\sqrt2 \approx 0.71 \), too big. For \( k = 2 \) the error squared is \( 9 \), and \( \sqrt{9/50} \approx 0.42 \le \tfrac12 \). So \( k = 2 \). Note that the test is on the *squares*: halving the error means keeping three quarters of \( \sum\sigma_i^2 \).
:::

## How much a subspace can hold

The proof of the theorem needs one inequality, and it is the only place where any work happens. The question it answers is: if we are allowed to keep only an \( s \)-dimensional subspace of \( F^m \), how much of \( \A \) can we capture? The answer is \( \sigma_1^2 + \dots + \sigma_s^2 \), and the best subspace is the span of the leading left singular vectors.

::: {#lem-orthonormal-capture-bound}
[An orthonormal list captures at most the leading singular values]

Let \( \A \in M_{m \times n}(F) \) with singular values \( \sigma_1 \ge \dots \ge \sigma_p \), extended by \( \sigma_i = 0 \) for \( p < i \le m \). Let \( \q_1, \dots, \q_s \) be an orthonormal list in \( F^m \), so that \( s \le m \). Then
\[
\sum_{j=1}^{s} \norm{\A^{*}\q_j}^2 \ \le\ \sum_{i=1}^{s} \sigma_i^2 .
\]
:::

::: {.idea}
Write each \( \q_j \) in the orthonormal basis \( (\u_1, \dots, \u_m) \). The quantity \( \norm{\A^{*}\q_j}^2 \) then becomes \( \sum_i \sigma_i^2\lvert c_{ji}\rvert^2 \), so the total is \( \sum_i \sigma_i^2 t_i \) with weights \( t_i = \sum_j \lvert c_{ji}\rvert^2 \). Two facts pin the weights down: each \( t_i \le 1 \), because the \( \q_j \) are orthonormal and Bessel's inequality applies to \( \u_i \); and \( \sum_i t_i = s \), because each \( \q_j \) is a unit vector. A weighted sum of a decreasing sequence with weights in \( [0, 1] \) that sum to \( s \) is largest when the first \( s \) weights are \( 1 \) — which is the last display of the proof.
:::

::: {.proof}
If \( s = 0 \) both sides are empty sums, so assume \( s \ge 1 \). Fix \( j \) and put \( c_{ji} = \inner{\q_j}{\u_i} \) for \( 1 \le i \le m \), so that the \( i \)-th entry of \( \U^{*}\q_j \) is \( c_{ji} \). Since \( \A^{*} = \V\vSigma^{*}\U^{*} \) and \( \V \) is unitary, hence an isometry (@def-unitary-orthogonal, @thm-isometry-characterizations),
\[
\norm{\A^{*}\q_j}^2 = \norm{\vSigma^{*}\U^{*}\q_j}^2 = \sum_{i=1}^{m} \sigma_i^2\lvert c_{ji}\rvert^2 ,
\]
because \( \vSigma^{*} \) multiplies the \( i \)-th entry by \( \sigma_i \) and discards the entries beyond the \( p \)-th, which is the same as using \( \sigma_i = 0 \) there. Summing over \( j \) and exchanging the two finite sums,
\[
\sum_{j=1}^{s} \norm{\A^{*}\q_j}^2 = \sum_{i=1}^{m} \sigma_i^2 t_i ,
\qquad t_i \coloneqq \sum_{j=1}^{s} \lvert c_{ji}\rvert^2 .
\]

Now bound the weights. Since \( \lvert c_{ji}\rvert = \lvert\inner{\u_i}{\q_j}\rvert \) and \( (\q_1, \dots, \q_s) \) is an orthonormal list, Bessel's inequality (@thm-bessel-inequality) applied to the vector \( \u_i \) gives
\[
t_i = \sum_{j=1}^{s} \lvert \inner{\u_i}{\q_j}\rvert^2 \ \le\ \norm{\u_i}^2 = 1 .
\]
Since \( (\u_1, \dots, \u_m) \) is an orthonormal **basis** of \( F^m \), Parseval's identity (@thm-parseval-identity) gives \( \sum_{i=1}^m \lvert c_{ji}\rvert^2 = \norm{\q_j}^2 = 1 \) for each \( j \), and therefore
\[
\sum_{i=1}^{m} t_i = \sum_{j=1}^{s} \sum_{i=1}^{m} \lvert c_{ji}\rvert^2 = s .
\]
Finally, using \( \sigma_i^2 \ge \sigma_s^2 \) together with \( t_i - 1 \le 0 \) for \( i \le s \), and \( \sigma_i^2 \le \sigma_s^2 \) together with \( t_i \ge 0 \) for \( i > s \),
\[
\begin{aligned}
\sum_{i=1}^{m} \sigma_i^2 t_i - \sum_{i=1}^{s} \sigma_i^2
 &= \sum_{i \le s} \sigma_i^2(t_i - 1) + \sum_{i > s} \sigma_i^2 t_i \\
 &\le \sigma_s^2\Bigl(\sum_{i \le s}(t_i - 1) + \sum_{i > s} t_i\Bigr) \\
 &= \sigma_s^2\Bigl(\sum_{i=1}^{m} t_i - s\Bigr) = 0 .
\end{aligned}
\]
This is the stated inequality.
:::

Equality is attainable: take \( \q_j = \u_j \) for \( j \le s \). Then \( \A^{*}\u_j = \sigma_j\v_j \) by the rank-one expansion, so \( \norm{\A^{*}\u_j}^2 = \sigma_j^2 \) and the two sides agree. The lemma is the extreme case of a family of statements about sums of the largest eigenvalues of a Hermitian matrix; Chapter 17 develops the family through the Courant–Fischer min–max theorem, of which the inequality above is the crudest and most useful consequence.

## The Eckart–Young theorem

Now the theorem. Read it as a statement about a minimization problem: over the set of matrices of rank at most \( k \) — which is not a subspace, so no earlier optimization theorem applies to it directly — the minimum of \( \norm{\A - \B}_F \) exists, is attained at a matrix we can write down, and has a value we already computed.

::: {#thm-eckart-young}
[Eckart–Young Theorem, Frobenius case]

Let \( \A \in M_{m \times n}(F) \) with singular values \( \sigma_1 \ge \dots \ge \sigma_p \), and let \( 0 \le k \le p \). Then for **every** \( \B \in M_{m \times n}(F) \) with \( \rank\B \le k \),
\[
\norm{\A - \B}_F \ \ge\ \Bigl(\sum_{i > k}\sigma_i^2\Bigr)^{1/2} ,
\]
and equality holds for \( \B = \A_k \). In words: the truncation \( \A_k \) minimizes \( \norm{\A - \B}_F \) over all matrices of rank at most \( k \), and the minimum value is \( \bigl(\sum_{i>k}\sigma_i^2\bigr)^{1/2} \).
:::

::: {.idea}
The difficulty is that \( \B \) is an arbitrary matrix of rank \( \le k \), and there is no formula for such a thing. The rescue is to stop looking at \( \B \) and look only at its column space \( S \), a subspace of dimension \( s \le k \). ① Every column of \( \B \) lies in \( S \), so column by column the Best Approximation Theorem says \( \B \) cannot beat \( P_S\A \), the matrix obtained by projecting every column of \( \A \) onto \( S \). So it suffices to minimize over subspaces. ② For a subspace, Pythagoras splits the error into "all of \( \A \)" minus "the part \( S \) captures", and the captured part is exactly the quantity @lem-orthonormal-capture-bound bounds. ③ The bound is \( \sigma_1^2 + \dots + \sigma_k^2 \), and subtracting it from \( \norm{\A}_F^2 = \sum_i\sigma_i^2 \) leaves \( \sum_{i>k}\sigma_i^2 \), which @lem-frobenius-sum-of-squares says is exactly what \( \A_k \) achieves.
:::

::: {.proof}
**Step 1: reduce to a projection.** Let \( \B \) have rank \( \le k \) and put \( S = \col(\B) \), so \( s \coloneqq \dim S = \rank\B \le k \). Write \( \a_1, \dots, \a_n \) and \( \b_1, \dots, \b_n \) for the columns of \( \A \) and of \( \B \). By the definition of the Frobenius norm, summing squares of entries column by column,
\[
\norm{\A - \B}_F^2 = \sum_{j=1}^{n} \norm{\a_j - \b_j}^2 .
\]
Each \( \b_j \) lies in \( S \), so @thm-best-approximation gives \( \norm{\a_j - \b_j} \ge \norm{\a_j - P_S\a_j} \) for every \( j \), where \( P_S \) is the orthogonal projection onto \( S \) (@def-orthogonal-projection), identified throughout with its matrix in the standard basis of \( F^m \). Hence
\[
\norm{\A - \B}_F^2 \ \ge\ \sum_{j=1}^{n} \norm{\a_j - P_S\a_j}^2 = \norm{\A - P_S\A}_F^2 ,
\]
the last equality because the \( j \)-th column of \( P_S\A \) is \( P_S\a_j \).

**Step 2: what a subspace captures.** Choose an orthonormal basis \( (\q_1, \dots, \q_s) \) of \( S \). For each \( j \), the vectors \( \a_j - P_S\a_j \) and \( P_S\a_j \) are orthogonal, so @thm-pythagoras gives \( \norm{\a_j - P_S\a_j}^2 = \norm{\a_j}^2 - \norm{P_S\a_j}^2 \), and summing over \( j \),
\[
\norm{\A - P_S\A}_F^2 = \norm{\A}_F^2 - \norm{P_S\A}_F^2 .
\]
By @thm-projection-formula (a), \( P_S\a_j = \sum_{l \le s}\inner{\a_j}{\q_l}\q_l \), whose summands are pairwise orthogonal, so @thm-pythagoras gives \( \norm{P_S\a_j}^2 = \sum_{l=1}^{s}\lvert\inner{\a_j}{\q_l}\rvert^2 \). Exchanging the sums,
\[
\norm{P_S\A}_F^2 = \sum_{l=1}^{s} \sum_{j=1}^{n} \lvert\inner{\a_j}{\q_l}\rvert^2 = \sum_{l=1}^{s} \norm{\A^{*}\q_l}^2 ,
\]
where the last equality holds because \( \inner{\a_j}{\q_l} = \q_l^{*}\a_j \) is the \( j \)-th entry of the row vector \( \q_l^{*}\A \), whose entries are the conjugates of those of \( \A^{*}\q_l \).

**Step 3: apply the bound.** By @lem-orthonormal-capture-bound and \( s \le k \), and since all \( \sigma_i^2 \ge 0 \),
\[
\norm{P_S\A}_F^2 \ \le\ \sum_{i=1}^{s} \sigma_i^2 \ \le\ \sum_{i=1}^{k} \sigma_i^2 .
\]
Combining the three steps with \( \norm{\A}_F^2 = \sum_{i}\sigma_i^2 \) (@lem-frobenius-sum-of-squares),
\[
\norm{\A - \B}_F^2 \ \ge\ \norm{\A}_F^2 - \sum_{i=1}^{k}\sigma_i^2 = \sum_{i > k}\sigma_i^2 .
\]

**Equality.** The matrix \( \A_k \) has rank \( \min(k, r) \le k \), and \( \norm{\A - \A_k}_F^2 = \sum_{i>k}\sigma_i^2 \) by @lem-frobenius-sum-of-squares. So the lower bound is attained, and it is the minimum. This proves the theorem.
:::

Three remarks are worth extracting. First, the theorem is a genuine minimum, not an infimum: the minimizing matrix is exhibited. Second, the minimum value depends on \( \A \) only through its singular values, so it is unchanged if \( \A \) is replaced by \( \U'\A\V' \) with \( \U', \V' \) unitary. Third, the case \( k = r - 1 \) reads: the Frobenius distance from \( \A \) to the matrices of rank \( < r \) is \( \sigma_r \), the smallest non-zero singular value. Exercise C1 turns that into a statement about how far an invertible matrix is from being singular.

::: {.remark}
The same matrix \( \A_k \) is also optimal in the **spectral norm** \( \norm{\cdot}_2 \), where the minimum value is \( \sigma_{k+1} \) rather than \( \bigl(\sum_{i>k}\sigma_i^2\bigr)^{1/2} \). We cannot state that here, because the spectral norm is defined only in Chapter 16. In fact both statements are instances of one theorem: \( \A_k \) is a best rank-\( k \) approximation in **every** unitarily invariant norm. Chapter 21 proves that, and the proof is genuinely different from the one above — it needs inequalities between the singular values of \( \A \) and of \( \A - \B \), not a projection argument.
:::

## A worked example

::: {#exm-best-rank-one}
[The best rank-one approximation of a 3 × 2 matrix]

Let
\[
\A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{pmatrix} \in M_{3 \times 2}(\nR) .
\]
Find the best rank-one approximation of \( \A \) in the Frobenius norm, and compute the error in two ways.
:::

::: {.solution}
*Singular values and vectors.* Since \( \A \) has more rows than columns, work with the \( 2 \times 2 \) matrix
\[
\A\tp\A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix},
\]
whose eigenvalues are \( 3 \) and \( 1 \) with orthonormal eigenvectors
\[
\v_1 = \tfrac{1}{\sqrt2}(1, 1), \qquad \v_2 = \tfrac{1}{\sqrt2}(1, -1) .
\]
Hence \( \sigma_1 = \sqrt3 \) and \( \sigma_2 = 1 \), and the left singular vectors are \( \u_i = \A\v_i/\sigma_i \):
\[
\u_1 = \tfrac{1}{\sqrt6}(1, 1, 2), \qquad \u_2 = \tfrac{1}{\sqrt2}(1, -1, 0) .
\]
(Both are unit vectors, as they must be: \( 1 + 1 + 4 = 6 \) and \( 1 + 1 = 2 \).)

*The approximation.* By @thm-eckart-young the answer is \( \A_1 = \sigma_1\u_1\v_1\tp \). The scalar in front is \( \sqrt3/(\sqrt6\sqrt2) = \sqrt3/\sqrt{12} = \tfrac12 \), so
\[
\A_1 = \frac12 \begin{pmatrix} 1 & 1 \\ 1 & 1 \\ 2 & 2 \end{pmatrix} .
\]
It has rank one, its two columns being equal and non-zero.

*The error, twice.* Directly,
\[
\A - \A_1 = \frac12\begin{pmatrix} 1 & -1 \\ -1 & 1 \\ 0 & 0 \end{pmatrix},
\qquad
\norm{\A - \A_1}_F^2 = 4 \cdot \tfrac14 = 1 .
\]
From the theorem, the error squared is \( \sigma_2^2 = 1 \). The two agree. As a further check, \( \norm{\A}_F^2 = 1 + 1 + 1 + 1 = 4 \) and \( \sigma_1^2 + \sigma_2^2 = 3 + 1 = 4 \), as @lem-frobenius-sum-of-squares requires; the relative error of the rank-one approximation is \( \sqrt{1/4} = \tfrac12 \).
:::

## Best-fitting subspaces

Step 1 of the proof did more than its job. It showed that the optimal \( \B \) may be taken of the form \( P_S\A \), and Steps 2 and 3 identified the best \( S \). That identification is a theorem in its own right, and it is the statement people mean when they speak of fitting a low-dimensional structure to data.

::: {#cor-best-fitting-subspace}
[The best-fitting subspace]

Let \( \a_1, \dots, \a_n \in F^m \) be the columns of \( \A \), and let \( 1 \le k \le p \). Among all subspaces \( S \subseteq F^m \) with \( \dim S \le k \), the total squared distance
\[
D(S) \coloneqq \sum_{j=1}^{n} d(\a_j, S)^2
\]
is smallest for \( S = \Span(\u_1, \dots, \u_k) \), and its smallest value is \( \sum_{i > k}\sigma_i^2 \).
:::

::: {.proof}
By @def-distance-to-subspace, \( d(\a_j, S) = \norm{\a_j - P_S\a_j} \), so \( D(S) = \norm{\A - P_S\A}_F^2 \) as in Step 1 of @thm-eckart-young. Since \( \rank(P_S\A) \le \dim S \le k \), the theorem gives \( D(S) \ge \sum_{i>k}\sigma_i^2 \). For \( S_0 = \Span(\u_1, \dots, \u_k) \) the columns \( \u_1, \dots, \u_k \) are orthonormal, so @thm-projection-formula (a) gives
\[
P_{S_0}\A = \sum_{i=1}^{k} \u_i\u_i^{*}\A = \sum_{i=1}^{k} \sigma_i\u_i\v_i^{*} = \A_k ,
\]
using \( \u_i^{*}\A = \sigma_i\v_i^{*} \), which is the rank-one expansion read one row at a time. Hence \( D(S_0) = \norm{\A - \A_k}_F^2 = \sum_{i>k}\sigma_i^2 \).
:::

**What this is used for, honestly.** Two applications are within reach of what we have proved, and a third is not.

The first is **compression**. Storing \( \A \) costs \( mn \) numbers; storing \( \A_k \) as the list \( \sigma_1, \u_1, \v_1, \dots, \sigma_k, \u_k, \v_k \) costs \( k(m + n + 1) \). When \( k \) is much smaller than \( m \) and \( n \) that is a large saving, and @thm-eckart-young says no other rank-\( k \) object stored the same way is closer to \( \A \) in the Frobenius norm. The relative error is \( \bigl(\sum_{i>k}\sigma_i^2 / \sum_i\sigma_i^2\bigr)^{1/2} \), computable before choosing \( k \). Whether that error is acceptable is not a mathematical question.

The second is **principal components**. Take \( n \) data points in \( \nR^m \) and place them as the columns of \( \A \). Then @cor-best-fitting-subspace says: the \( k \)-dimensional subspace through the origin that minimizes the total squared distance to the data is spanned by \( \u_1, \dots, \u_k \), the leading left singular vectors. These directions are the **principal components** of the data, and the numbers \( \sigma_i^2 \) measure how much of \( \sum_j\norm{\a_j}^2 \) each one accounts for. That is a theorem of linear algebra, and it is the whole of what this book has proved.

What is *not* proved here is the statistics. The usual procedure subtracts the mean of the data first, so that \( \tfrac{1}{n}\A\A\tp \) becomes a sample covariance matrix, and then interprets \( \sigma_i^2/\sum_l\sigma_l^2 \) as a fraction of variance explained. Those steps need a probabilistic model, a reason to prefer squared error, and an argument that the sample answer says something about a larger population. Chapter 24 §10 supplies the first two — the model for the finite population of the data themselves, where expectation is an average and no measure theory is needed, and three reasons to prefer squared error — and says plainly that the third belongs to probability and statistics, which this book does not develop. It also says why a singular value decomposition is never computed by forming \( \A^{*}\A \) and finding its eigenvalues, the route taken in every hand computation in this chapter; the algorithm that replaces it is assembled nowhere in this book.

::: {.warning}
**The truncation is optimal for this norm, and low rank does not mean small.** Two mistakes to avoid.

*Other measures of error give other answers.* Let \( \A = \diag(2, 1) \), so \( \sigma_1 = 2 \), \( \sigma_2 = 1 \), and \( \A_1 = \diag(2, 0) \), whose error matrix \( \diag(0, 1) \) has a largest entry of modulus \( 1 \). The rank-one matrix
\[
\B = \frac12\begin{pmatrix} 3 & \sqrt3 \\ \sqrt3 & 1 \end{pmatrix},
\qquad
\A - \B = \frac12\begin{pmatrix} 1 & -\sqrt3 \\ -\sqrt3 & 1 \end{pmatrix},
\]
has \( \det\B = \tfrac34 - \tfrac34 = 0 \), so \( \rank\B = 1 \), and every entry of \( \A - \B \) has modulus at most \( \sqrt3/2 \approx 0.87 < 1 \). So \( \B \) beats \( \A_1 \) if the error is measured entrywise. It loses in the Frobenius norm, as it must: \( \norm{\A - \B}_F^2 = 2 > 1 = \norm{\A - \A_1}_F^2 \).

*Small rank and small size are unrelated.* The \( n \times n \) all-ones matrix \( \J \) has rank \( 1 \) and \( \norm{\J}_F = n \), while \( \varepsilon\I_n \) has rank \( n \) and \( \norm{\varepsilon\I_n}_F = \varepsilon\sqrt n \), as small as we like. "Approximating by a matrix of low rank" is a statement about structure, never about magnitude.
:::

## Exercises

### A. Check your understanding

:::: {#exr-low-rank-approximation-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the Eckart–Young Theorem, including the value of the minimum.
2. Express \( \norm{\A}_F \) in terms of the singular values of \( \A \).
3. Let \( \rank\A = r \). What is \( \A_k \) for \( k \ge r \), and what is the minimum of \( \norm{\A - \B}_F \) over \( \rank\B \le k \) in that case?
4. True or false: the truncation \( \A_k \) is the *unique* matrix of rank at most \( k \) nearest to \( \A \) in the Frobenius norm. Justify your answer.
5. A matrix of rank \( 1 \) is close to \( \0 \) in the Frobenius norm. True or false? Justify your answer.
:::
::::

::: {.solution}
(a) For \( \A \in M_{m \times n}(F) \) with singular values \( \sigma_1 \ge \dots \ge \sigma_p \) and \( 0 \le k \le p \): every \( \B \) with \( \rank\B \le k \) satisfies \( \norm{\A - \B}_F \ge \bigl(\sum_{i>k}\sigma_i^2\bigr)^{1/2} \), with equality for \( \B = \A_k = \sum_{i \le k}\sigma_i\u_i\v_i^{*} \).

(b) \( \norm{\A}_F = \bigl(\sum_{i=1}^{p}\sigma_i^2\bigr)^{1/2} \) (@lem-frobenius-sum-of-squares).

(c) \( \A_k = \A \), since the terms with \( i > r \) are zero; the minimum is \( 0 \), attained at \( \B = \A \) itself, which has rank \( r \le k \).

(d) False in general. Take \( \A = \I_2 \), so \( \sigma_1 = \sigma_2 = 1 \). Both \( \B_1 = \diag(1, 0) \) and \( \B_2 = \tfrac12\begin{psmallmatrix} 1 & 1 \\ 1 & 1\end{psmallmatrix} \) have rank \( 1 \), and \( \norm{\I_2 - \B_1}_F^2 = 1 = \norm{\I_2 - \B_2}_F^2 \), which is the minimum \( \sigma_2^2 \). (Both are truncations of \( \I_2 \), for two different singular value decompositions.)

(e) False. Rank is unrelated to size: the all-ones matrix \( \J \in M_n(\nR) \) has rank \( 1 \) and \( \norm{\J}_F = n \).
:::

### B. Practice

:::: {#exr-low-rank-approximation-b1}
[B1: Errors from the singular values alone]

A matrix \( \A \) has singular values \( 6, 3, 2, 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \norm{\A}_F \) and the minimum of \( \norm{\A - \B}_F \) over matrices \( \B \) of rank at most \( k \), for \( k = 1, 2, 3 \).
2. Find the smallest \( k \) for which the relative error \( \norm{\A - \A_k}_F/\norm{\A}_F \) is at most \( 0.3 \).
:::
::::

::: {.solution}
(a) \( \norm{\A}_F^2 = 36 + 9 + 4 + 1 = 50 \), so \( \norm{\A}_F = \sqrt{50} = 5\sqrt2 \). By @thm-eckart-young the minima are
\[
\sqrt{9 + 4 + 1} = \sqrt{14}, \qquad \sqrt{4 + 1} = \sqrt5, \qquad \sqrt{1} = 1
\]
for \( k = 1, 2, 3 \).

(b) The condition is \( \sum_{i>k}\sigma_i^2 \le 0.09 \cdot 50 = 4.5 \). For \( k = 2 \) the left side is \( 5 > 4.5 \); for \( k = 3 \) it is \( 1 \le 4.5 \). So \( k = 3 \).
:::

:::: {#exr-low-rank-approximation-b2}
[B2: A best rank-one approximation]

Let \( \A = \begin{pmatrix} 3 & 1 \\ 1 & 3\end{pmatrix} \in M_2(\nR) \). Find the singular values of \( \A \), the best rank-one approximation \( \A_1 \) in the Frobenius norm, and the error, computed both directly and from the theorem.
::::

::: {.solution}
\( \A \) is symmetric with eigenvalues \( 4 \) and \( 2 \) (trace \( 6 \), determinant \( 8 \)) and orthonormal eigenvectors \( \q_1 = \tfrac{1}{\sqrt2}(1, 1) \), \( \q_2 = \tfrac{1}{\sqrt2}(1, -1) \). Both eigenvalues are positive, so \( \A \succ 0 \), and \( \A\tp\A = \A^2 \) has eigenvalues \( 16 \) and \( 4 \); hence \( \sigma_1 = 4 \), \( \sigma_2 = 2 \), with \( \u_i = \v_i = \q_i \).

Therefore
\[
\A_1 = 4\q_1\q_1\tp = 4 \cdot \frac12\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix},
\]
which has rank one. Directly,
\[
\A - \A_1 = \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix},
\qquad \norm{\A - \A_1}_F^2 = 4 .
\]
From @thm-eckart-young the error squared is \( \sigma_2^2 = 4 \). The two agree, and \( \norm{\A}_F^2 = 9 + 1 + 1 + 9 = 20 = 16 + 4 \) checks @lem-frobenius-sum-of-squares.
:::

:::: {#exr-low-rank-approximation-b3}
[B3: Pythagoras for the truncation]

Let \( \A \in M_{m \times n}(F) \) and \( 0 \le k \le p \). Prove that
\[
\norm{\A}_F^2 = \norm{\A_k}_F^2 + \norm{\A - \A_k}_F^2 ,
\]
and deduce that \( k \mapsto \norm{\A - \A_k}_F \) is non-increasing.
::::

::: {.solution}
By @lem-frobenius-sum-of-squares applied to \( \A \) and to \( \A - \A_k \), and by the same lemma applied to \( \A_k \), whose singular values are \( \sigma_1, \dots, \sigma_k \) followed by zeros (it equals \( \U\vSigma'\V^{*} \) with \( \vSigma' \) the matrix keeping only the first \( k \) diagonal entries of \( \vSigma \)),
\[
\norm{\A_k}_F^2 + \norm{\A - \A_k}_F^2 = \sum_{i \le k}\sigma_i^2 + \sum_{i > k}\sigma_i^2 = \norm{\A}_F^2 .
\]
Since \( \norm{\A - \A_k}_F^2 = \sum_{i>k}\sigma_i^2 \) and the \( \sigma_i^2 \) are non-negative, increasing \( k \) by one removes a non-negative term, so the sequence is non-increasing. This proves both claims.
:::

### C. Going deeper

:::: {#exr-low-rank-approximation-c1}
[C1: How far is a matrix from being singular?]

Let \( \A \in M_n(F) \) be invertible, with singular values \( \sigma_1 \ge \dots \ge \sigma_n > 0 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \norm{\A - \B}_F \ge \sigma_n \) for every singular \( \B \in M_n(F) \).
2. Exhibit a singular \( \B \) with \( \norm{\A - \B}_F = \sigma_n \).
3. Deduce that the distance from \( \A \) to the set of singular matrices, measured in the Frobenius norm, is exactly \( \sigma_n \), and illustrate this with \( \A = \begin{pmatrix} 3 & 1 \\ 1 & 3\end{pmatrix} \).
:::
::::

::: {.solution}
(a) A singular \( \B \in M_n(F) \) has \( \rank\B \le n - 1 \) (@thm-invertible-tfae-det (d)). By @thm-eckart-young with \( k = n - 1 \),
\[
\norm{\A - \B}_F \ \ge\ \Bigl(\sum_{i > n-1}\sigma_i^2\Bigr)^{1/2} = \sigma_n .
\]

(b) Take \( \B = \A_{n-1} = \sum_{i \le n-1}\sigma_i\u_i\v_i^{*} \). Its rank is \( n - 1 < n \), so it is singular, and \( \norm{\A - \B}_F = \sigma_n \) by @lem-frobenius-sum-of-squares.

(c) By (a) the distance is at least \( \sigma_n \) and by (b) it is at most \( \sigma_n \), so it equals \( \sigma_n \); in particular the minimum is attained. For the given \( \A \), Exercise B2 found \( \sigma_2 = 2 \) and \( \A_1 = \begin{psmallmatrix} 2 & 2 \\ 2 & 2\end{psmallmatrix} \), which is singular and at Frobenius distance \( 2 \). So no singular matrix is closer to \( \A \) than \( 2 \). The smallest singular value is therefore a quantitative version of invertibility: \( \A \) is invertible exactly when \( \sigma_n > 0 \), and it is *far* from singular exactly when \( \sigma_n \) is large.
:::

:::: {#exr-low-rank-approximation-c2}
[C2: The best line through a cloud of points]

The four points \( (1, 1), (2, 2), (1, -1) \) and \( (0, 0) \) of \( \nR^2 \) are to be fitted by a line through the origin, minimizing the total squared distance from the points to the line.

::: {.enumerate options="label=(\alph*)"}
1. Write the points as the columns of a matrix \( \A \) and compute \( \A\A\tp \) and the singular values of \( \A \).
2. Use @cor-best-fitting-subspace to find the best line and the minimum total squared distance.
3. Verify the answer by computing the four distances directly.
:::
::::

::: {.solution}
(a) With the points as columns,
\[
\A = \begin{pmatrix} 1 & 2 & 1 & 0 \\ 1 & 2 & -1 & 0 \end{pmatrix},
\qquad
\A\A\tp = \begin{pmatrix} 6 & 4 \\ 4 & 6 \end{pmatrix} .
\]
The eigenvalues of \( \A\A\tp \) are \( 10 \) and \( 2 \) (trace \( 12 \), determinant \( 20 \)), with orthonormal eigenvectors \( \u_1 = \tfrac{1}{\sqrt2}(1, 1) \) and \( \u_2 = \tfrac{1}{\sqrt2}(1, -1) \). The eigenvalues of \( \A\A\tp \) are the squares of the singular values, since \( \A\A\tp = \U\vSigma\vSigma^{*}\U^{*} \); hence \( \sigma_1 = \sqrt{10} \) and \( \sigma_2 = \sqrt2 \).

(b) By @cor-best-fitting-subspace with \( k = 1 \), the best line is \( S_0 = \Span(\u_1) \), the line \( y = x \), and the minimum total squared distance is \( \sigma_2^2 = 2 \).

(c) The points \( (1, 1), (2, 2) \) and \( (0, 0) \) lie on \( y = x \), contributing \( 0 \). For \( (1, -1) \), the projection onto \( \Span\bigl((1,1)\bigr) \) is \( \tfrac{1 - 1}{2}(1, 1) = (0, 0) \), so the distance squared is \( 1 + 1 = 2 \). The total is \( 2 \), as predicted. (The point \( (0, 0) \) contributes nothing to any subspace through the origin; it is there as a reminder that the corollary counts all columns, including zero ones.)
:::

:::: {#exr-low-rank-approximation-c3}
[C3: Truncation respects unitaries but not sums]

Let \( \A \in M_{m \times n}(F) \), and let \( \Q \in M_m(F) \) and \( \R \in M_n(F) \) be unitary (orthogonal, when \( F = \nR \)).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \Q\A_k\R^{*} \) is a best rank-\( k \) approximation of \( \Q\A\R^{*} \) in the Frobenius norm.
2. Deduce that the function \( \A \mapsto \min\{\norm{\A - \B}_F : \rank\B \le k\} \) is unchanged by \( \A \mapsto \Q\A\R^{*} \).
3. Give \( \A, \B \in M_2(\nR) \) with \( (\A + \B)_1 \ne \A_1 + \B_1 \) for every choice of the truncations involved. *Hint: two rank-one matrices whose sum is a multiple of the identity.*
:::
::::

::: {.solution}
(a) If \( \A = \U\vSigma\V^{*} \) is a singular value decomposition (@thm-svd), then
\[
\Q\A\R^{*} = (\Q\U)\vSigma(\R\V)^{*}
\]
is one as well, since a product of unitary matrices is unitary (@prp-orthogonal-group-properties (a)) and \( \vSigma \) is unchanged. Its left and right singular vectors are \( \Q\u_i \) and \( \R\v_i \), so its rank-\( k \) truncation for this decomposition is
\[
\sum_{i \le k}\sigma_i(\Q\u_i)(\R\v_i)^{*} = \Q\Bigl(\sum_{i \le k}\sigma_i\u_i\v_i^{*}\Bigr)\R^{*} = \Q\A_k\R^{*} .
\]
By @thm-eckart-young applied to \( \Q\A\R^{*} \), this is a best rank-\( k \) approximation.

(b) The two matrices have the same singular values, so by @thm-eckart-young both minima equal \( \bigl(\sum_{i>k}\sigma_i^2\bigr)^{1/2} \).

(c) Take \( \A = \diag(1, 0) \) and \( \B = \diag(0, 1) \). Each has rank one, so \( \A_1 = \A \) and \( \B_1 = \B \) for every singular value decomposition, and \( \A_1 + \B_1 = \I_2 \). But \( \A + \B = \I_2 \), whose rank-one truncations all have rank one, hence are never \( \I_2 \). So \( (\A + \B)_1 \ne \A_1 + \B_1 \). Truncation is not a linear operation, which is why "keep the biggest pieces" cannot be analyzed one summand at a time.
:::
