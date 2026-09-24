# Subspaces and Sums of Eigenvalues

Section 4 deleted a row and the matching column, which is a coordinate-dependent operation, and got a coordinate-free conclusion: the spectra interlace. That is a hint. This section replaces "delete some coordinates" by "restrict to a subspace", which is the same operation with the accident of a basis removed, and the interlacing survives in a stronger form. Then it asks a question Courant–Fischer cannot answer one eigenvalue at a time: not "what is \( \lambda_2 \)?" but "what is \( \lambda_1 + \lambda_2 \)?" That sum turns out to be a maximum over a set of subspaces, and the answer discharges a promise Chapter 13 made about singular values.

**Throughout this section \( F = \nR \) or \( F = \nC \), every matrix whose eigenvalues are indexed is Hermitian, and the indexing is decreasing**, \( \lambda_1(\A) \ge \dots \ge \lambda_n(\A) \).

## Restricting a matrix to a subspace

A principal submatrix of \( \A \) records what the quadratic form \( \x \mapsto \inner{\A\x}{\x} \) does to vectors supported on a few coordinates. Nothing in that description needs the coordinates to be the standard ones: any subspace \( W \) and any orthonormal basis of it will do, and the matrix that results plays the same role.

::: {#def-compression}
[Compression to a subspace]

Let \( \A \in M_n(F) \), let \( 1 \le k \le n \), and let \( \q_1, \dots, \q_k \) be an **orthonormal** list in \( F^{n} \), so that the matrix \( \Q \in M_{n \times k}(F) \) with these columns satisfies \( \Q^{*}\Q = \I_k \). The **compression** of \( \A \) to \( W = \Span(\q_1, \dots, \q_k) \) with respect to this basis is the \( k \times k \) matrix
\[
\Q^{*}\A\Q, \qquad (\Q^{*}\A\Q)_{ij} = \inner{\A\q_j}{\q_i} .
\]
:::

The entry formula is just \( (\Q^{*}\A\Q)_{ij} = \q_i^{*}\A\q_j \), and \( \q_i^{*}\y = \inner{\y}{\q_i} \) for the standard inner product. If \( \A \) is Hermitian so is \( \Q^{*}\A\Q \), since \( (\Q^{*}\A\Q)^{*} = \Q^{*}\A^{*}\Q = \Q^{*}\A\Q \).

**The eigenvalues do not depend on the basis chosen.** Let \( (\q'_1, \dots, \q'_k) \) be another orthonormal basis of the same \( W \), with matrix \( \Q' \). Each \( \q'_j \) lies in \( W = \col(\Q) \), so \( \Q' = \Q\U \) for some \( \U \in M_k(F) \), and then \( \I_k = (\Q')^{*}\Q' = \U^{*}\Q^{*}\Q\U = \U^{*}\U \), so \( \U \) is unitary. Hence
\[
(\Q')^{*}\A\Q' = \U^{*}(\Q^{*}\A\Q)\U ,
\]
a unitary similarity, which leaves the eigenvalues alone. So it is legitimate to speak of *the* eigenvalues of the compression of \( \A \) to \( W \), and we do.

Three cases to keep in mind.

- **Coordinate subspaces.** If \( \q_j = \e_{i_j} \) for indices \( i_1 < \dots < i_k \), then \( (\Q^{*}\A\Q)_{lj} = a_{i_l i_j} \): the compression is the principal submatrix \( \A_{I,I} \) of @def-submatrix-minor on the index set \( I = \{i_1, \dots, i_k\} \). Compression generalizes "delete rows and the matching columns".
- **\( k = n \).** Then \( \Q \) is a unitary matrix and \( \Q^{*}\A\Q \) is unitarily similar to \( \A \): nothing is lost and nothing is learned.
- **\( k = 1 \).** Then \( \Q^{*}\A\Q \) is the \( 1 \times 1 \) matrix \( \inner{\A\q_1}{\q_1} = R_{\A}(\q_1) \), the Rayleigh quotient of @def-rayleigh-quotient at a unit vector. Everything below is a statement about \( k \) Rayleigh quotients at once.

Drop the orthonormality and the notion collapses. With \( \A = \diag(1, 0) \) and the single column \( \Q = (2, 0)\tp \), which has \( \Q^{*}\Q = (4) \ne \I_1 \), the "compression" is the \( 1 \times 1 \) matrix \( (4) \), whose eigenvalue \( 4 \) is larger than every eigenvalue of \( \A \). The clause that fails is \( \Q^{*}\Q = \I_k \), and with it every conclusion of this section.

## Interlacing without coordinates

::: {#thm-poincare-separation}
[Poincaré Separation Theorem]

Let \( \A \in M_n(F) \) be Hermitian, let \( 1 \le k \le n \), and let \( \B = \Q^{*}\A\Q \) be the compression of \( \A \) to a \( k \)-dimensional subspace \( W \subseteq F^{n} \), as in @def-compression. Then
\[
\lambda_i(\A) \ \ge\ \lambda_i(\B) \ \ge\ \lambda_{i + n - k}(\A)
\qquad (1 \le i \le k) .
\]
:::

::: {.idea}
Both inequalities come from the same observation, used twice. The map \( \y \mapsto \Q\y \) carries \( F^{k} \) isometrically onto \( W \), and it carries the Rayleigh quotient of \( \B \) to the Rayleigh quotient of \( \A \). So each of the two Courant–Fischer descriptions of \( \lambda_i(\B) \) — a maximum of minima, and a minimum of maxima — is the corresponding description of \( \lambda_i(\A) \) with the competing subspaces restricted to those lying inside \( W \). A maximum over fewer competitors is smaller; a minimum over fewer competitors is larger. That is the whole proof; the only care needed is in matching the dimensions, and it is there that \( n - k \) appears.
:::

::: {.proof}
**Step 1: transport.** Throughout, \( R_{\A} \) and \( R_{\B} \) are the Rayleigh quotients of @def-rayleigh-quotient. For \( \0 \ne \y \in F^{k} \) we have \( \Q\y \ne \0 \), since \( \norm{\Q\y}^{2} = \y^{*}\Q^{*}\Q\y = \norm{\y}^{2} \) and \( \y \ne \0 \). The same computation with \( \A \) inserted gives
\[
\inner{\B\y}{\y} = \y^{*}\Q^{*}\A\Q\y = \inner{\A(\Q\y)}{\Q\y} ,
\]
so \( R_{\B}(\y) = R_{\A}(\Q\y) \). Moreover \( \y \mapsto \Q\y \) is injective and linear, so it maps the subspaces of \( F^{k} \) of dimension \( j \) bijectively onto the subspaces of \( W \) of dimension \( j \), for every \( j \). Consequently, for each \( j \),
\[
\bigl\{\,R_{\B}(\y) : \0 \ne \y \in S \,\bigr\}
= \bigl\{\,R_{\A}(\x) : \0 \ne \x \in \Q S \,\bigr\}
\]
for every subspace \( S \subseteq F^{k} \).

**Step 2: the upper bound.** By the max–min form of @thm-courant-fischer applied to \( \B \in M_k(F) \),
\[
\begin{aligned}
\lambda_i(\B)
 &= \max_{\substack{S \subseteq F^{k} \\ \dim S = i}} \ \min_{\0 \ne \y \in S} R_{\B}(\y) \\
 &= \max_{\substack{U \subseteq W \\ \dim U = i}} \ \min_{\0 \ne \x \in U} R_{\A}(\x) ,
\end{aligned}
\]
the second equality by Step 1. The subspaces \( U \subseteq W \) of dimension \( i \) form a subfamily of the subspaces \( U \subseteq F^{n} \) of dimension \( i \), and enlarging the family over which a maximum is taken cannot decrease it. So by the max–min form of @thm-courant-fischer applied to \( \A \), the right-hand side is at most \( \lambda_i(\A) \).

**Step 3: the lower bound.** By the min–max form of @thm-courant-fischer applied to \( \B \in M_k(F) \), with the complementary dimension \( k - i + 1 \),
\[
\begin{aligned}
\lambda_i(\B)
 &= \min_{\substack{S \subseteq F^{k} \\ \dim S = k-i+1}} \ \max_{\0 \ne \y \in S} R_{\B}(\y) \\
 &= \min_{\substack{U \subseteq W \\ \dim U = k-i+1}} \ \max_{\0 \ne \x \in U} R_{\A}(\x) ,
\end{aligned}
\]
again by Step 1. Put \( l = i + n - k \), so that \( 1 \le l \le n \) and \( n - l + 1 = k - i + 1 \). The min–max form of @thm-courant-fischer applied to \( \A \) therefore reads
\[
\lambda_{l}(\A) = \min_{\substack{U \subseteq F^{n} \\ \dim U = k-i+1}} \ \max_{\0 \ne \x \in U} R_{\A}(\x) ,
\]
a minimum over a **larger** family than the one above, hence no larger. So \( \lambda_i(\B) \ge \lambda_{i+n-k}(\A) \). This proves the theorem.
:::

::: {.remark}
Taking \( W \) to be the coordinate hyperplane \( \Span(\e_j : j \ne l) \) makes \( \B \) the principal submatrix obtained by deleting row \( l \) and column \( l \), and \( k = n-1 \) turns the conclusion into \( \lambda_i(\A) \ge \lambda_i(\B) \ge \lambda_{i+1}(\A) \). That is @thm-cauchy-interlacing. What the present theorem adds is that the coordinates played no part, and that deleting \( n - k \) dimensions at once costs exactly \( n - k \) indices.
:::

::: {#exm-compression-3x3}
[A compression of a diagonal matrix]

Let \( \A = \diag(5, 3, -2) \) and let
\[
\q_1 = \tfrac13(2, 2, 1), \qquad \q_2 = \tfrac13(-2, 1, 2) .
\]
Check that \( (\q_1, \q_2) \) is orthonormal, compute the compression \( \B \) of \( \A \) to \( W = \Span(\q_1, \q_2) \) and its eigenvalues, and verify @thm-poincare-separation.
:::

::: {.solution}
*Orthonormality.* \( \norm{\q_1}^{2} = (4 + 4 + 1)/9 = 1 \) and \( \norm{\q_2}^{2} = (4 + 1 + 4)/9 = 1 \), while \( 9\inner{\q_1}{\q_2} = -4 + 2 + 2 = 0 \).

*The compression.* Multiplying by the diagonal matrix, \( 3\A\q_1 = (10, 6, -2) \) and \( 3\A\q_2 = (-10, 3, -4) \). Hence
\[
\begin{aligned}
b_{11} &= \tfrac19(2, 2, 1)\cdot(10, 6, -2) = \tfrac{20 + 12 - 2}{9} = \tfrac{10}{3}, \\
b_{21} &= \tfrac19(-2, 1, 2)\cdot(10, 6, -2) = \tfrac{-20 + 6 - 4}{9} = -2, \\
b_{22} &= \tfrac19(-2, 1, 2)\cdot(-10, 3, -4) = \tfrac{20 + 3 - 8}{9} = \tfrac53 ,
\end{aligned}
\]
and \( b_{12} = b_{21} \) because \( \B \) is symmetric. So
\[
\B = \begin{pmatrix} 10/3 & -2 \\ -2 & 5/3 \end{pmatrix} .
\]

*Its eigenvalues.* \( \tr\B = 5 \) and \( \det\B = \tfrac{50}{9} - 4 = \tfrac{14}{9} \), so the characteristic polynomial is \( x^{2} - 5x + \tfrac{14}{9} \), that is \( 9x^{2} - 45x + 14 \). Its discriminant is \( 2025 - 504 = 1521 = 39^{2} \), so the roots are \( (45 \pm 39)/18 \), namely \( \lambda_1(\B) = \tfrac{14}{3} \) and \( \lambda_2(\B) = \tfrac13 \).

*The separation.* Here \( n = 3 \) and \( k = 2 \), so the theorem says \( \lambda_i(\A) \ge \lambda_i(\B) \ge \lambda_{i+1}(\A) \) for \( i = 1, 2 \):
\[
5 \ \ge\ \tfrac{14}{3} \ \ge\ 3 \ \ge\ \tfrac13 \ \ge\ -2 ,
\]
and every inequality is strict. Note also \( \tr\B = 5 \le 5 + 3 = \lambda_1(\A) + \lambda_2(\A) \); the next theorem says that this is no accident and that \( 8 \) is the best possible ceiling.
:::

::: {.check}
Let \( \A \) be Hermitian \( n \times n \) and let \( \B \) be its compression to a \( k \)-dimensional subspace. Which single inequality of @thm-poincare-separation says that a compression of a positive semidefinite matrix is positive semidefinite?
:::

::: {.solution}
The case \( i = k \) of the lower bound: \( \lambda_k(\B) \ge \lambda_{k+n-k}(\A) = \lambda_n(\A) \). If \( \A \succeq 0 \) then \( \lambda_n(\A) \ge 0 \) by @thm-psd-characterizations (b), so every eigenvalue of \( \B \) is \( \ge 0 \), and \( \B \) is Hermitian, so \( \B \succeq 0 \) by the same theorem. (A direct proof is also one line: \( \inner{\B\y}{\y} = \inner{\A\Q\y}{\Q\y} \ge 0 \). The point of the check is to locate the statement inside the interlacing.)
:::

## The top eigenvalues, summed

Chapter 13 described \( \lambda_1 \) as a maximum over the unit sphere (@lem-extreme-eigenvalues-quadratic-form), and Section 1 pointed out that \( \lambda_2 \) is not the "second largest value" of anything. But \( \lambda_1 + \lambda_2 \) is a maximum again — over pairs of orthonormal vectors rather than single ones. The pattern continues for every \( k \), and it is the sum, never the individual eigenvalue, that behaves.

::: {#thm-ky-fan}
[Ky Fan Maximum Principle]

Let \( \A \in M_n(F) \) be Hermitian and let \( 1 \le k \le n \). Then
\[
\begin{aligned}
\sum_{i=1}^{k}\lambda_i(\A)
 &= \max\Bigl\{ \sum_{i=1}^{k}\inner{\A\q_i}{\q_i} \ :\
   \q_1, \dots, \q_k \text{ orthonormal} \Bigr\} \\
 &= \max\bigl\{ \tr(\Q^{*}\A\Q) \ :\
   \Q \in M_{n \times k}(F),\ \Q^{*}\Q = \I_k \bigr\} ,
\end{aligned}
\]
and the maximum is attained by \( \Q = (\u_1 \ \dots \ \u_k) \) for any orthonormal basis \( (\u_1, \dots, \u_n) \) of \( F^{n} \) with \( \A\u_i = \lambda_i(\A)\u_i \).
:::

::: {.idea}
The two right-hand sides are the same number written twice, since the diagonal entries of \( \Q^{*}\A\Q \) are exactly the \( k \) numbers \( \inner{\A\q_i}{\q_i} \). That reformulation is the whole idea: the quantity to be maximized is the **trace of a compression**, and @thm-poincare-separation already bounds every eigenvalue of a compression by the matching eigenvalue of \( \A \). Add \( k \) such bounds and read the left-hand side as a trace. The maximizing \( \Q \) is the one that makes the compression diagonal with the top eigenvalues on it, and there is no cleverness in guessing it.
:::

::: {.proof}
Write \( \B = \Q^{*}\A\Q \) for a matrix \( \Q \) with orthonormal columns \( \q_1, \dots, \q_k \). Its diagonal entries are \( b_{ii} = \inner{\A\q_i}{\q_i} \) by @def-compression, so
\[
\tr\B = \sum_{i=1}^{k}\inner{\A\q_i}{\q_i} ,
\]
and the two sets over which the maxima are taken consist of the same numbers. It therefore suffices to prove the statement for \( \tr(\Q^{*}\A\Q) \).

**The bound.** Let \( \Q^{*}\Q = \I_k \) and put \( \B = \Q^{*}\A\Q \), a Hermitian matrix in \( M_k(F) \). By @cor-trace-sum-eigenvalues-again, \( \tr\B = \sum_{i=1}^{k}\lambda_i(\B) \). By @thm-poincare-separation, \( \lambda_i(\B) \le \lambda_i(\A) \) for every \( 1 \le i \le k \). Summing these \( k \) inequalities,
\[
\tr(\Q^{*}\A\Q) = \sum_{i=1}^{k}\lambda_i(\B) \ \le\ \sum_{i=1}^{k}\lambda_i(\A) .
\]

**Attainment.** Since \( \A \) is Hermitian, @cor-spectral-complex-matrix (for \( F = \nC \)) or @cor-spectral-real-matrix (for \( F = \nR \)) provides an orthonormal basis \( (\u_1, \dots, \u_n) \) of \( F^{n} \) of eigenvectors, in any prescribed order; take the order with \( \A\u_i = \lambda_i(\A)\u_i \). Let \( \Q \) have columns \( \u_1, \dots, \u_k \); these are orthonormal, so \( \Q^{*}\Q = \I_k \). Then
\[
\inner{\A\u_i}{\u_i} = \lambda_i(\A)\inner{\u_i}{\u_i} = \lambda_i(\A) ,
\]
so \( \tr(\Q^{*}\A\Q) = \sum_{i \le k}\lambda_i(\A) \).

The bound is therefore attained, so the supremum is a maximum and equals \( \sum_{i\le k}\lambda_i(\A) \). This proves the theorem.
:::

For \( k = 1 \) this is @lem-extreme-eigenvalues-quadratic-form of Chapter 13: \( \lambda_1 \) is the largest value of \( \inner{\A\x}{\x} \) on the unit sphere. For \( k = n \) it degenerates in an instructive way: every \( \Q \) is unitary, every \( \Q^{*}\A\Q \) is unitarily similar to \( \A \), and the "maximum" is attained everywhere, at the common value \( \tr\A \). The content is in between.

::: {#exm-ky-fan-sums}
[Which pairs of directions capture the most]

Let
\[
\A = \begin{pmatrix} 2 & 1 & 0 \\ 1 & 2 & 0 \\ 0 & 0 & -1 \end{pmatrix} .
\]
Find \( \max\{\tr(\Q\tp\A\Q) : \Q\tp\Q = \I_2\} \) and a maximizer, and compare the values at \( \Q = (\e_1\ \e_2) \) and \( \Q = (\e_1\ \e_3) \).
:::

::: {.solution}
The eigenvalues: \( \e_3 \) is an eigenvector for \( -1 \), and the top-left block \( \begin{psmallmatrix} 2 & 1 \\ 1 & 2\end{psmallmatrix} \) has eigenvectors \( (1, 1) \) and \( (1, -1) \) for \( 3 \) and \( 1 \). So \( \lambda_1 = 3 \), \( \lambda_2 = 1 \), \( \lambda_3 = -1 \), with orthonormal eigenvectors \( \u_1 = \tfrac1{\sqrt2}(1,1,0) \), \( \u_2 = \tfrac1{\sqrt2}(1,-1,0) \), \( \u_3 = \e_3 \). By @thm-ky-fan the maximum is \( 3 + 1 = 4 \), attained at \( \Q = (\u_1\ \u_2) \).

At \( \Q = (\e_1\ \e_2) \) the trace is \( a_{11} + a_{22} = 4 \): this is also a maximizer. That is no accident — \( \Span(\e_1, \e_2) = \Span(\u_1, \u_2) \), and the trace of a compression, like its eigenvalues, depends only on the subspace. At \( \Q = (\e_1\ \e_3) \) the trace is \( 2 + (-1) = 1 \), well below the ceiling, as @thm-ky-fan requires.
:::

The simplest competitors are the standard basis vectors, and they give a statement about the diagonal of \( \A \) for free.

::: {#cor-ky-fan-diagonal}
[Partial Sums of the Diagonal]

Let \( \A \in M_n(F) \) be Hermitian with diagonal entries \( a_{11}, \dots, a_{nn} \), and let \( 1 \le i_1 < \dots < i_k \le n \). Then
\[
\sum_{j=1}^{k} a_{i_j i_j} \ \le\ \sum_{i=1}^{k}\lambda_i(\A) ,
\]
with equality for \( k = n \).
:::

::: {.proof}
The list \( (\e_{i_1}, \dots, \e_{i_k}) \) is orthonormal, and \( \inner{\A\e_{i}}{\e_{i}} = a_{ii} \). Apply @thm-ky-fan. For \( k = n \) both sides equal \( \tr\A \), by @cor-trace-sum-eigenvalues-again.
:::

::: {.check}
Can a Hermitian \( 3 \times 3 \) matrix with diagonal entries \( 5, 1, 0 \) have eigenvalues \( 4, 2, 0 \)? Can it have eigenvalues \( 6, 0, 0 \)?
:::

::: {.solution}
Not the first: the case \( k = 1 \) of @cor-ky-fan-diagonal says every diagonal entry is at most \( \lambda_1 \), and \( 5 > 4 \). The second passes every test — \( 5 \le 6 \), \( 5 + 1 \le 6 \), \( 6 = 6 \) — and is realized: with \( \v = (\sqrt5, 1, 0) \), the matrix \( \v\v\tp \) has diagonal \( 5, 1, 0 \); it sends \( \v \) to \( \norm{\v}^{2}\v = 6\v \) and kills the plane orthogonal to \( \v \), so its eigenvalues are \( 6, 0, 0 \). Whether passing every test is always enough is the converse question, which Section 8 takes up.
:::

## The promise from Chapter 13

Chapter 13 §10 proved a bound on how much of a matrix an orthonormal list can capture (@lem-orthonormal-capture-bound), and said of it: it "is the extreme case of a family of statements about sums of the largest eigenvalues of a Hermitian matrix; Chapter 17 develops the family through the Courant–Fischer min–max theorem". @thm-ky-fan is that family. Here is the lemma, recovered from it in four lines.

::: {#cor-capture-bound-revisited}
[The Capture Bound as a Case of Ky Fan]

Let \( \A \in M_{m \times n}(F) \) with singular values \( \sigma_1 \ge \dots \ge \sigma_p \), \( p = \min(m,n) \), extended by \( \sigma_i = 0 \) for \( p < i \le m \), and let \( \q_1, \dots, \q_s \) be an orthonormal list in \( F^{m} \). Then
\[
\sum_{j=1}^{s}\norm{\A^{*}\q_j}^{2} \ \le\ \sum_{i=1}^{s}\sigma_i^{2} .
\]
:::

::: {.proof}
If \( s = 0 \) both sides are empty sums, equal to \( 0 \); so assume \( s \ge 1 \). Put \( \M = \A\A^{*} \in M_m(F) \), which is Hermitian. For each \( j \),
\[
\norm{\A^{*}\q_j}^{2} = (\A^{*}\q_j)^{*}(\A^{*}\q_j) = \q_j^{*}\M\q_j = \inner{\M\q_j}{\q_j} .
\]
Fix a singular value decomposition \( \A = \U\vSigma\V^{*} \) (@thm-svd). Since \( \V^{*}\V = \I_n \),
\[
\M = \U\vSigma\V^{*}\V\vSigma^{*}\U^{*} = \U(\vSigma\vSigma^{*})\U^{*} ,
\]
and \( \vSigma\vSigma^{*} \) is the \( m \times m \) diagonal matrix with diagonal \( \sigma_1^{2}, \dots, \sigma_p^{2} \) followed by \( m - p \) zeros — that is, \( \sigma_1^{2} \ge \dots \ge \sigma_m^{2} \) in the extended notation. So this display is a unitary diagonalization of \( \M \), and @cor-spectral-complex-matrix identifies its diagonal as the eigenvalue list: \( \lambda_i(\M) = \sigma_i^{2} \) for \( 1 \le i \le m \). Now @thm-ky-fan applied to \( \M \) with \( k = s \) gives
\[
\sum_{j=1}^{s}\inner{\M\q_j}{\q_j} \ \le\ \sum_{i=1}^{s}\lambda_i(\M) = \sum_{i=1}^{s}\sigma_i^{2} ,
\]
which is the claim.
:::

This is @lem-orthonormal-capture-bound exactly, hypotheses and conclusion, so the debt is paid. Two things are worth saying about the shape of the payment.

First, Chapter 13 had to prove the inequality by hand, weight by weight, because it had no min–max theorem; the argument there is a careful estimate on a weighted sum of a decreasing sequence. Here the same estimate is invisible: it has been absorbed into @thm-courant-fischer, whose proof is a dimension count, and passed on through @thm-poincare-separation.

Second, the words "extreme case". Strictly, the lemma is a *special* case of the family rather than an extreme one: it is the instance in which the Hermitian matrix is a product \( \A\A^{*} \), so that every eigenvalue is a squared singular value. Its crudest instance, \( s = 1 \), says \( \norm{\A^{*}\q}^{2} \le \sigma_1^{2} \) for a unit \( \q \), that is, \( \norm{\A^{*}}_2 = \sigma_1 \). The same one line of Ky Fan, run with the other product — @thm-ky-fan with \( k = 1 \) applied to the Hermitian matrix \( \A^{*}\A \in M_n(F) \) — whose largest eigenvalue is \( \sigma_1^{2} \) by @def-singular-values — gives
\[
\max_{\norm{\x} = 1}\norm{\A\x}^{2}
= \max_{\norm{\x} = 1}\inner{\A^{*}\A\x}{\x}
= \lambda_1(\A^{*}\A) = \sigma_1^{2} .
\]
So the largest singular value is the largest stretching factor, which is @thm-operator-norm-formulas (c), \( \norm{\A}_2 = \sigma_1(\A) \). Chapter 16 proved that from the singular value decomposition; here it is one line of Ky Fan.

## Sums are convex; individual eigenvalues are not

::: {#cor-ky-fan-subadditive}
[Subadditivity of the Top Partial Sums]

Let \( \A, \B \in M_n(F) \) be Hermitian and let \( 1 \le k \le n \). Then
\[
\sum_{i=1}^{k}\lambda_i(\A + \B)
\ \le\ \sum_{i=1}^{k}\lambda_i(\A) + \sum_{i=1}^{k}\lambda_i(\B) .
\]
:::

::: {.proof}
By @thm-ky-fan applied to the Hermitian matrix \( \A + \B \), there is a \( \Q \in M_{n\times k}(F) \) with \( \Q^{*}\Q = \I_k \) attaining the maximum, so that
\[
\sum_{i=1}^{k}\lambda_i(\A+\B) = \tr\bigl(\Q^{*}(\A+\B)\Q\bigr) .
\]
By @thm-trace-properties (1) the right-hand side is \( \tr(\Q^{*}\A\Q) + \tr(\Q^{*}\B\Q) \). This one \( \Q \) is a competitor in each of the two maximization problems of @thm-ky-fan, for \( \A \) and for \( \B \), so each summand is at most the corresponding maximum. Adding the two bounds proves the corollary.
:::

Write \( s_k(\A) = \sum_{i \le k}\lambda_i(\A) \) for the function just bounded. Two properties have now been proved: it is **subadditive**, \( s_k(\A + \B) \le s_k(\A) + s_k(\B) \), and it is **positively homogeneous**, \( s_k(t\A) = ts_k(\A) \) for \( t \ge 0 \), since multiplying a Hermitian matrix by \( t \ge 0 \) multiplies each eigenvalue by \( t \) without disturbing the order. Together these say that for \( t \in [0,1] \),
\[
s_k\bigl(t\A + (1-t)\B\bigr) \ \le\ ts_k(\A) + (1-t)s_k(\B) :
\]
\( s_k \) is a **convex** function on the real vector space of Hermitian matrices. That is exactly what one expects of a maximum of linear functions, which is what @thm-ky-fan says \( s_k \) is: each fixed \( \Q \) makes \( \A \mapsto \tr(\Q^{*}\A\Q) \) linear, and \( s_k \) is the pointwise maximum of this family. Chapter 18 studies convex functions in general, and the observation that a pointwise supremum of linear functions is convex is one of its basic facts.

::: {#cor-trace-min}
[The Bottom Partial Sums as a Minimum]

Let \( \A \in M_n(F) \) be Hermitian and let \( 1 \le k \le n \). Then
\[
\sum_{i=n-k+1}^{n}\lambda_i(\A)
= \min\bigl\{\tr(\Q^{*}\A\Q) : \Q^{*}\Q = \I_k\bigr\} ,
\]
the minimum being attained at the bottom \( k \) eigenvectors.
:::

::: {.proof}
The eigenvalues of \( -\A \), with multiplicity, are the negatives of those of \( \A \), and negation reverses order, so
\[
\lambda_i(-\A) = -\lambda_{n+1-i}(\A) \qquad (1 \le i \le n) .
\]
Apply @thm-ky-fan to \( -\A \). Its left-hand side is
\[
\sum_{i=1}^{k}\lambda_i(-\A) = -\sum_{i=1}^{k}\lambda_{n+1-i}(\A)
= -\sum_{i=n-k+1}^{n}\lambda_i(\A) ,
\]
the last step re-indexing the sum. Its right-hand side is
\[
\max_{\Q^{*}\Q = \I_k}\tr\bigl(\Q^{*}(-\A)\Q\bigr)
= -\min_{\Q^{*}\Q = \I_k}\tr(\Q^{*}\A\Q) ,
\]
using @thm-trace-properties (1) and the fact that maximizing \( -g \) is minimizing \( g \). Negating both sides gives the claim, and the maximizer for \( -\A \) is a list of top eigenvectors of \( -\A \), which are bottom eigenvectors of \( \A \).
:::

::: {.warning}
**Only the sums are convex. A single eigenvalue \( \lambda_k \) with \( 1 < k < n \) is neither convex nor concave in \( \A \).** Both failures happen among \( 3 \times 3 \) diagonal matrices, where \( \lambda_2 \) is just the middle entry; for general \( n \) and \( 1 < k < n \), take the direct sum of each witness with \( 2\I_{k-2} \) above and \( -\I_{n-k-1} \) below, which moves the middle entry to position \( k \) without changing the computation.

*Not convex.* Take \( \A = \diag(1,0,0) \) and \( \B = \diag(0,1,0) \), so \( \lambda_2(\A) = \lambda_2(\B) = 0 \). Their midpoint is \( \tfrac12(\A+\B) = \diag(\tfrac12, \tfrac12, 0) \), with \( \lambda_2 = \tfrac12 \). Convexity would require \( \tfrac12 \le 0 \).

*Not concave.* Take \( \A = \diag(1,1,0) \) and \( \B = \diag(1,0,1) \), so \( \lambda_2(\A) = \lambda_2(\B) = 1 \). Their midpoint is \( \diag(1, \tfrac12, \tfrac12) \), with \( \lambda_2 = \tfrac12 \). Concavity would require \( \tfrac12 \ge 1 \).

The partial sum \( s_2 \) satisfies the **convexity** inequality on both pairs, as it must: in the first pair its values at the two matrices and their midpoint are \( 1, 1, 1 \), and in the second \( 2, 2, \tfrac32 \). The moral is that \( \lambda_k = s_k - s_{k-1} \) is a **difference** of two convex functions, and a difference of convex functions has, in general, no convexity property at all. This is why the sharpest statements in this chapter are about sums, and why a statement about a single intermediate eigenvalue usually has to be proved as a statement about two sums.
:::

## Exercises

### A. Check your understanding

:::: {#exr-poincare-and-ky-fan-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the compression of \( \A \) to a subspace, and say what has to be checked before the phrase "the eigenvalues of the compression" makes sense.
2. State @thm-ky-fan, including where the maximum is attained.
3. Explain why the maximum in @thm-ky-fan does not need an appeal to compactness.
4. Is \( \A \mapsto \lambda_1(\A) \) convex on the Hermitian matrices? Is \( \A \mapsto \lambda_n(\A) \)? Justify each answer.
5. State @thm-poincare-separation and say which case of it is @thm-cauchy-interlacing.
:::
::::

::: {.solution}
(a) For an orthonormal list \( \q_1, \dots, \q_k \) with matrix \( \Q \), the compression of \( \A \) to \( W = \Span(\q_1,\dots,\q_k) \) is \( \Q^{*}\A\Q \), the \( k \times k \) matrix with entries \( \inner{\A\q_j}{\q_i} \). What must be checked is that changing the orthonormal basis of \( W \) changes \( \Q^{*}\A\Q \) only by a unitary similarity, so the eigenvalues depend on \( W \) alone.

(b) For Hermitian \( \A \in M_n(F) \) and \( 1 \le k \le n \), \( \sum_{i\le k}\lambda_i(\A) \) is the maximum of \( \tr(\Q^{*}\A\Q) \) over all \( \Q \in M_{n\times k}(F) \) with \( \Q^{*}\Q = \I_k \), equivalently the maximum of \( \sum_{i\le k}\inner{\A\q_i}{\q_i} \) over orthonormal lists. It is attained at \( \Q = (\u_1\ \dots\ \u_k) \) for an orthonormal eigenbasis ordered with \( \A\u_i = \lambda_i(\A)\u_i \).

(c) Because the proof exhibits both a bound valid for every competitor and a competitor achieving it. A supremum that is achieved is a maximum, whatever the topology of the competing set.

(d) Incorrect. Take \( \A = \diag(1,0,0) \) and \( \B = \diag(0,1,0) \) as in the warning: \( \lambda_2(\A) = \lambda_2(\B) = 0 \) while \( \A + \B = \diag(1,1,0) \) has \( \lambda_2 = 1 \). What is true is the statement about sums, @cor-ky-fan-subadditive: here \( \lambda_1 + \lambda_2 \) of the sum is \( 2 \), and \( (1+0) + (1+0) = 2 \).

(e) If \( \B \) is the compression of the Hermitian \( \A \in M_n(F) \) to a \( k \)-dimensional subspace, then \( \lambda_i(\A) \ge \lambda_i(\B) \ge \lambda_{i+n-k}(\A) \) for \( 1 \le i \le k \). Cauchy interlacing is the case \( k = n-1 \) with the subspace a coordinate hyperplane.
:::

### B. Practice

:::: {#exr-poincare-and-ky-fan-b1}
[B1: A compression, and two bounds]

Let \( \A = \diag(5, 0, -2) \) and let \( \q_1 = \tfrac13(1, 2, 2) \), \( \q_2 = \tfrac13(2, 1, -2) \).

::: {.enumerate options="label=(\alph*)"}
1. Verify that \( (\q_1, \q_2) \) is orthonormal and compute the compression \( \B \) of \( \A \) to \( \Span(\q_1, \q_2) \).
2. Find the eigenvalues of \( \B \) and verify @thm-poincare-separation.
3. Compare \( \tr\B \) with the bound of @thm-ky-fan, and say how far this subspace is from optimal.
:::
::::

::: {.solution}
(a) \( \norm{\q_1}^{2} = (1+4+4)/9 = 1 \), \( \norm{\q_2}^{2} = (4+1+4)/9 = 1 \) and \( 9\inner{\q_1}{\q_2} = 2 + 2 - 4 = 0 \). Next \( 3\A\q_1 = (5, 0, -4) \) and \( 3\A\q_2 = (10, 0, 4) \), so
\[
\begin{aligned}
b_{11} &= \tfrac19(1,2,2)\cdot(5,0,-4) = \tfrac{5 - 8}{9} = -\tfrac13, \\
b_{12} &= \tfrac19(1,2,2)\cdot(10,0,4) = \tfrac{10 + 8}{9} = 2, \\
b_{22} &= \tfrac19(2,1,-2)\cdot(10,0,4) = \tfrac{20 - 8}{9} = \tfrac43 ,
\end{aligned}
\]
so \( \B = \begin{psmallmatrix} -1/3 & 2 \\ 2 & 4/3\end{psmallmatrix} \).

(b) \( \tr\B = 1 \) and \( \det\B = -\tfrac49 - 4 = -\tfrac{40}{9} \), so \( 9x^{2} - 9x - 40 = 0 \), with discriminant \( 81 + 1440 = 1521 = 39^{2} \) and roots \( (9 \pm 39)/18 \). Hence \( \lambda_1(\B) = \tfrac83 \) and \( \lambda_2(\B) = -\tfrac53 \). The separation \( \lambda_i(\A) \ge \lambda_i(\B) \ge \lambda_{i+1}(\A) \) reads
\[
5 \ \ge\ \tfrac83 \ \ge\ 0 \ \ge\ -\tfrac53 \ \ge\ -2 ,
\]
all strict.

(c) \( \tr\B = 1 \), while @thm-ky-fan gives \( \lambda_1(\A) + \lambda_2(\A) = 5 + 0 = 5 \) as the maximum, attained at \( \Span(\e_1, \e_2) \). So this subspace scores \( 1 \) out of a possible \( 5 \); it is far from optimal, and one can see why. Between them \( \q_1 \) and \( \q_2 \) put weight \( \tfrac49 + \tfrac49 = \tfrac89 \) on the third coordinate, where \( \A \) is \( -2 \), and only \( \tfrac19 + \tfrac49 = \tfrac59 \) on the first, where it is \( 5 \): indeed \( 5\cdot\tfrac59 + 0 - 2\cdot\tfrac89 = 1 \).
:::

:::: {#exr-poincare-and-ky-fan-b2}
[B2: Reading the sums off the spectrum]

A Hermitian \( \A \in M_4(\nR) \) has eigenvalues \( 6, 4, 1, -3 \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \max\{\tr(\Q\tp\A\Q) : \Q\tp\Q = \I_k\} \) for \( k = 1, 2, 3, 4 \).
2. Compute the corresponding minima, using @cor-trace-min.
3. For \( \A = \diag(6, 4, 1, -3) \) and \( \q_1 = \tfrac1{\sqrt2}(1,1,0,0) \), \( \q_2 = \tfrac1{\sqrt2}(0,0,1,1) \), compute \( \tr(\Q\tp\A\Q) \) and check it against (a) and (b).
:::
::::

::: {.solution}
(a) By @thm-ky-fan the maxima are the partial sums from the top: \( 6 \), \( 10 \), \( 11 \), \( 8 \).

(b) By @cor-trace-min the minima are the partial sums from the bottom: \( -3 \), \( -2 \), \( 2 \), \( 8 \). The two agree at \( k = 4 \), as they must, both being \( \tr\A \).

(c) \( \inner{\A\q_1}{\q_1} = \tfrac12(6 + 4) = 5 \) and \( \inner{\A\q_2}{\q_2} = \tfrac12(1 - 3) = -1 \), so \( \tr(\Q\tp\A\Q) = 4 \). Indeed \( -2 \le 4 \le 10 \), as (a) and (b) require for \( k = 2 \).
:::

:::: {#exr-poincare-and-ky-fan-b3}
[B3: Subadditivity, and how loose it can be]

Let
\[
\A = \begin{pmatrix} 1 & 1 \\ 1 & 1\end{pmatrix}, \qquad
\B = \begin{pmatrix} 1 & -1 \\ -1 & 1\end{pmatrix} .
\]

::: {.enumerate options="label=(\alph*)"}
1. Compute the eigenvalues of \( \A \), of \( \B \) and of \( \A + \B \).
2. Verify @cor-ky-fan-subadditive for \( k = 1 \) and \( k = 2 \), and say for which \( k \) it is strict.
3. Give a pair of Hermitian \( 2 \times 2 \) matrices for which the \( k = 1 \) inequality is an equality.
:::
::::

::: {.solution}
(a) \( \A \) has trace \( 2 \) and determinant \( 0 \), so its eigenvalues are \( 2, 0 \); the same for \( \B \). And \( \A + \B = 2\I_2 \) has eigenvalues \( 2, 2 \).

(b) For \( k = 1 \): \( \lambda_1(\A+\B) = 2 \) and \( \lambda_1(\A) + \lambda_1(\B) = 4 \), so \( 2 \le 4 \), strictly. For \( k = 2 \): \( 4 \le 2 + 2 = 4 \), an equality — as it must be, since for \( k = n \) both sides are traces and @thm-trace-properties (1) makes the trace additive.

(c) Take \( \A = \B = \diag(1,0) \). Then \( \A + \B = \diag(2,0) \) and \( \lambda_1(\A+\B) = 2 = 1 + 1 \). More generally equality holds at \( k = 1 \) whenever \( \A \) and \( \B \) have a common top eigenvector, because then that one vector attains all three maxima at once.
:::

### C. Going deeper

:::: {#exr-poincare-and-ky-fan-c1}
[C1: The Loewner order and the partial sums]

Let \( \A, \B \in M_n(F) \) be Hermitian.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \A \succeq \B \) implies \( \sum_{i\le k}\lambda_i(\A) \ge \sum_{i\le k}\lambda_i(\B) \) for every \( k \). *Hint: compare the two maximization problems of @thm-ky-fan competitor by competitor.*
2. Show that the converse fails: give Hermitian \( \A, \B \) satisfying all \( n \) of these inequalities with \( \A \not\succeq \B \).
:::
::::

::: {.solution}
(a) Let \( \Q^{*}\Q = \I_k \) with columns \( \q_1, \dots, \q_k \). Since \( \A - \B \succeq 0 \), clause (P2) of @def-positive-semidefinite gives \( \inner{(\A-\B)\q_i}{\q_i} \ge 0 \) for each \( i \), that is, \( \inner{\A\q_i}{\q_i} \ge \inner{\B\q_i}{\q_i} \). Summing over \( i \),
\[
\tr(\Q^{*}\A\Q) \ \ge\ \tr(\Q^{*}\B\Q) .
\]
Now take \( \Q \) to be a maximizer for \( \B \) in @thm-ky-fan. Then
\[
\sum_{i\le k}\lambda_i(\B) = \tr(\Q^{*}\B\Q) \le \tr(\Q^{*}\A\Q) \le \sum_{i\le k}\lambda_i(\A) ,
\]
the last step because \( \Q \) is one competitor in the maximization for \( \A \).

(b) Take \( \A = \diag(2, 0) \) and \( \B = \diag(1, 1) \). The partial sums are \( 2 \ge 1 \) for \( k = 1 \) and \( 2 \ge 2 \) for \( k = 2 \). But \( \A - \B = \diag(1, -1) \) has a negative eigenvalue, so \( \A - \B \not\succeq 0 \) by @thm-psd-characterizations (b), and \( \A \not\succeq \B \). Concretely, \( \inner{(\A-\B)\e_2}{\e_2} = -1 < 0 \).
:::

:::: {#exr-poincare-and-ky-fan-c2}
[C2: Partial sums that behave like a norm]

For positive semidefinite \( \A \in M_n(F) \) and \( 1 \le k \le n \), consider \( s_k(\A) = \sum_{i\le k}\lambda_i(\A) \), the partial sum of this section, now restricted to the positive semidefinite matrices.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( N_k(\A) \ge 0 \), with equality if and only if \( \A = \0 \).
2. Prove that \( N_k(c\A) = cN_k(\A) \) for every real \( c \ge 0 \), and that \( N_k(\A + \B) \le N_k(\A) + N_k(\B) \) for positive semidefinite \( \A, \B \).
3. The positive semidefinite matrices form a **cone**, not a vector space, so a norm cannot be defined on them. Deduce instead that \( s_k \) is positive, positively homogeneous and subadditive on this cone. Which step of your argument for (a) uses positive semidefiniteness, and what goes wrong without it?
:::
::::

::: {.solution}
(a) By @thm-psd-characterizations (b) every eigenvalue of \( \A \) is \( \ge 0 \), so \( N_k(\A) \ge \lambda_1(\A) \ge 0 \) for \( k \ge 1 \). If \( N_k(\A) = 0 \) then in particular \( \lambda_1(\A) = 0 \), so every eigenvalue is \( 0 \); by @cor-spectral-complex-matrix (or @cor-spectral-real-matrix) \( \A = \U\0\U^{*} = \0 \). Conversely \( N_k(\0) = 0 \).

(b) Multiplying a Hermitian matrix by \( c \ge 0 \) multiplies each eigenvalue by \( c \) and preserves the decreasing order, so \( \lambda_i(c\A) = c\lambda_i(\A) \) and the first claim follows by summing. The second is @cor-ky-fan-subadditive, which needs no positivity at all.

(c) Positivity with \( N_k(\A) = 0 \) only for \( \A = \0 \) is (a); homogeneity under scalars \( c \ge 0 \) is (b); subadditivity is (b). So \( N_k \) behaves as a norm wherever it is defined. It cannot be extended to all Hermitian matrices by the same formula: for \( \A = \diag(0, -1) \) and \( k = 1 \) we get \( N_1(\A) = 0 \) with \( \A \ne \0 \), so the positivity clause fails, and for \( c = -1 \) the value \( N_1(-\A) = 1 \) differs from \( \lvert c\rvert N_1(\A) = 0 \). The repair is to apply \( N_k \) to the singular values instead of the eigenvalues, which is what Chapter 21 does.
:::

:::: {#exr-poincare-and-ky-fan-c3}
[C3: How much of a matrix a subspace holds]

Let \( \A \in M_{m\times n}(F) \) with singular values \( \sigma_1 \ge \dots \ge \sigma_p \) extended by zeros as in @cor-capture-bound-revisited, let \( S \subseteq F^{m} \) have dimension \( k \), and let \( \Q \) have as columns an orthonormal basis of \( S \), so that \( P_S = \Q\Q^{*} \) by @thm-projection-formula (a).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \norm{P_S\A}_F^{2} = \tr(\Q^{*}\A\A^{*}\Q) \).
2. Deduce from @thm-ky-fan that \( \norm{P_S\A}_F^{2} \le \sigma_1^{2} + \dots + \sigma_k^{2} \), with equality when \( S \) is spanned by the first \( k \) left singular vectors.
3. Hence recover the value \( \sum_{i>k}\sigma_i^{2} \) of the minimum in @cor-best-fitting-subspace. *Hint: \( \a - P_S\a \) is orthogonal to \( P_S\a \).*
:::
::::

::: {.solution}
(a) The Frobenius norm satisfies \( \norm{\X}_F^{2} = \tr(\X^{*}\X) \), because the \( (j,j) \) entry of \( \X^{*}\X \) is the squared length of the \( j \)-th column of \( \X \). With \( P_S = \Q\Q^{*} \), which is Hermitian and satisfies \( P_S^{2} = \Q(\Q^{*}\Q)\Q^{*} = P_S \),
\[
\norm{P_S\A}_F^{2} = \tr(\A^{*}P_S^{*}P_S\A) = \tr(\A^{*}\Q\Q^{*}\A)
= \tr(\Q^{*}\A\A^{*}\Q) ,
\]
the last step by @thm-trace-properties (3) applied to \( \A^{*}\Q \) and \( \Q^{*}\A \).

(b) The matrix \( \M = \A\A^{*} \) is Hermitian with \( \lambda_i(\M) = \sigma_i^{2} \), as computed in the proof of @cor-capture-bound-revisited. By @thm-ky-fan with \( k \) columns,
\[
\tr(\Q^{*}\M\Q) \le \sum_{i\le k}\lambda_i(\M) = \sum_{i\le k}\sigma_i^{2} ,
\]
with equality when the columns of \( \Q \) are top eigenvectors of \( \M \). From \( \A = \U\vSigma\V^{*} \) the columns \( \u_1, \dots, \u_m \) of \( \U \) are exactly such an eigenbasis, so equality holds for \( S = \Span(\u_1, \dots, \u_k) \).

(c) Write \( \a_1, \dots, \a_n \) for the columns of \( \A \). For each \( j \) the vectors \( P_S\a_j \) and \( \a_j - P_S\a_j \) are orthogonal, so @thm-pythagoras gives \( \norm{\a_j}^{2} = \norm{P_S\a_j}^{2} + \norm{\a_j - P_S\a_j}^{2} \). Summing over \( j \),
\[
\sum_{j} d(\a_j, S)^{2} = \norm{\A}_F^{2} - \norm{P_S\A}_F^{2} .
\]
By @lem-frobenius-sum-of-squares, \( \norm{\A}_F^{2} = \sum_i \sigma_i^{2} \). By (b) the subtracted term is at most \( \sum_{i\le k}\sigma_i^{2} \), with equality for \( S = \Span(\u_1,\dots,\u_k) \). Hence the total squared distance is at least \( \sum_{i>k}\sigma_i^{2} \), and equals it for that \( S \); a subspace of smaller dimension \( k' < k \) does no better, since the same argument bounds what it captures by \( \sum_{i \le k'}\sigma_i^{2} \le \sum_{i\le k}\sigma_i^{2} \) — which is @cor-best-fitting-subspace, now read as a statement about a maximum of traces rather than a minimum of distances.
:::
