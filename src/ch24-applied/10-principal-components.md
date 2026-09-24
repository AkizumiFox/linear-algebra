# Principal Components

Chapter 13 §10 proved that the \( k \)-dimensional subspace **through the origin** closest to a cloud of points is spanned by the leading left singular vectors, and then said plainly what it had not proved: the centering, the covariance matrix, and the reading of \( \sigma_i^2/\sum_l\sigma_l^2 \) as a fraction of variance. This section supplies all three — and the variance fraction turns out to be a theorem, not a convention — and then marks exactly where linear algebra stops and statistics begins. The honest answer is: more is provable than one might expect, and less than the phrase "explained variance" usually suggests.

Throughout, the field is \( \nR \). The data are \( N \ge 1 \) points \( \x_1, \dots, \x_N \in \nR^n \), written as the columns of a matrix, and \( \norm{\cdot} \) is the Euclidean norm.

## Centering

An **affine subspace** of \( \nR^n \) is a coset \( A = \p + U = \{\p + \z : \z \in U\} \) of a subspace \( U \), and its dimension is \( \dim U \); Chapter 18 §01 calls \( U \) the direction space and shows in @prp-affine-hull-coset that every affine hull has this form. The subspaces of \( \nR^n \) are the affine subspaces containing \( \0 \).

Chapter 13 §10 fitted subspaces, which all pass through \( \0 \). That is the wrong family for data: a cloud of points far from the origin is badly described by any line through the origin, and the quantity minimized is then dominated by the distance from \( \0 \) to the cloud rather than by its shape. Widening the competition to all affine subspaces fixes this, and it costs nothing: the extra freedom is used up in one place, and we can say in advance where.

*Subtract the mean once, and the affine problem becomes the linear problem Chapter 13 solved.*

::: {#def-centered-data-matrix}
[Data matrix, mean and centered data matrix]

Let \( \x_1, \dots, \x_N \in \nR^n \). The **data matrix** is the matrix \( \X \in M_{n \times N}(\nR) \) whose \( j \)-th **column** is \( \x_j \). The **mean** of the data is
\[
\bar\x \coloneqq \frac1N\sum_{j=1}^{N}\x_j \in \nR^n ,
\]
and the **centered data matrix** is
\[
\X_c \coloneqq \X - \bar\x\,\1\tp \in M_{n \times N}(\nR) ,
\]
whose \( j \)-th column is \( \c_j \coloneqq \x_j - \bar\x \).
:::

Two clauses deserve comment. **Columns** are the data points, so \( n \) is the number of measured quantities and \( N \) the number of records; the opposite convention is also in use, and every formula below would be transposed under it. And \( \bar\x\,\1\tp \) is the \( n \times N \) matrix all of whose columns equal \( \bar\x \), since \( \1 \in \nR^N \) is the all-ones vector.

The defining property of the centered matrix is that its own mean is zero:
\[
\X_c\1 = \X\1 - \bar\x(\1\tp\1) = N\bar\x - N\bar\x = \0 ,
\]
using \( \1\tp\1 = N \). In words, each **row** of \( \X_c \) sums to \( 0 \).

::: {#exm-centering-examples}
[Centering three data sets]

::: {.enumerate options="label=(\alph*)"}
1. \( N = 4 \) points in \( \nR^2 \): \( (5,4), (4,1), (2,3), (1,0) \). Their sum is \( (12, 8) \), so \( \bar\x = (3,2) \) and
\[
\X_c = \begin{pmatrix} 2 & 1 & -1 & -2 \\ 2 & -1 & 1 & -2\end{pmatrix} .
\]
Both rows sum to \( 0 \).
2. \( N = 1 \). Then \( \bar\x = \x_1 \) and \( \X_c = \0 \): a single point carries no shape at all. This degenerate case matters, because every ratio below has \( 0/0 \) here and the statements must exclude it or say what they mean.
3. Data already centered: if \( \X\1 = \0 \) then \( \bar\x = \0 \) and \( \X_c = \X \). Centering is idempotent, since \( \X_c\1 = \0 \) always.
:::
:::

Change one clause and the object changes. Suppose one subtracts the mean of each *column* instead of forming the mean of the columns, replacing \( \x_j \) by \( \x_j - \bigl(\tfrac1n\1_n\tp\x_j\bigr)\1_n \) with \( \1_n \in \nR^n \). That removes the average of the measured quantities inside each record, which is a meaningful operation for some data and a meaningless one for most, and in any case is not the one below. The clause that matters is *which index is averaged over*.

## The best-fitting affine subspace

Distances to an affine subspace reduce to distances to its direction space, and the reduction is Chapter 11's Best Approximation Theorem.

::: {#lem-mean-minimizes-spread}
[Distance to a flat, and where its translate wants to be]

Let \( U \subseteq \nR^n \) be a subspace, let \( Q = \I_n - P_U \) be the orthogonal projection onto \( U^{\perp} \), and let \( \p \in \nR^n \).

::: {.enumerate options="label=(\alph*)"}
1. For every \( \x \in \nR^n \), \( \ d(\x, \p + U) = \norm{Q(\x - \p)} \), and the nearest point of \( \p + U \) exists.
2. For points \( \x_1, \dots, \x_N \) with mean \( \bar\x \),
\[
\sum_{j=1}^{N}\norm{Q(\x_j - \p)}^2
= \sum_{j=1}^{N}\norm{Q(\x_j - \bar\x)}^2 + N\norm{Q(\bar\x - \p)}^2 .
\]
In particular the left side is smallest exactly when \( \bar\x \in \p + U \).
:::
:::

::: {.idea}
Part (a) is the Best Approximation Theorem after sliding the whole picture by \( -\p \). Part (b) is the one-dimensional identity "sum of squares about a point = sum of squares about the mean + \( N \) times the squared displacement", proved the way it always is: expand the square and notice that the cross term is a multiple of \( \sum_j(\x_j - \bar\x) \), which is \( \0 \) by the definition of the mean.
:::

::: {.proof}
(a) A point of \( \p + U \) is \( \p + \z \) with \( \z \in U \), and \( \norm{\x - (\p+\z)} = \norm{(\x - \p) - \z} \). By @thm-best-approximation the quantity \( \norm{(\x-\p) - \z} \) over \( \z \in U \) is smallest exactly at \( \z = P_U(\x - \p) \), where its value is \( \norm{(\x-\p) - P_U(\x-\p)} = \norm{Q(\x-\p)} \). So the minimum is attained and equals \( \norm{Q(\x-\p)} \), which is \( d(\x, \p+U) \) by @def-distance-to-subspace applied after the translation.

(b) Put \( \y_j = Q(\x_j - \bar\x) \) and \( \d = Q(\bar\x - \p) \), so that \( Q(\x_j - \p) = \y_j + \d \) by linearity of \( Q \). Since \( Q \) is linear and \( \sum_j(\x_j - \bar\x) = N\bar\x - N\bar\x = \0 \),
\[
\sum_{j}\y_j = Q\Bigl(\sum_j(\x_j - \bar\x)\Bigr) = \0 .
\]
Therefore, expanding each square,
\[
\begin{aligned}
\sum_j\norm{\y_j + \d}^2
&= \sum_j\bigl(\norm{\y_j}^2 + 2\inner{\y_j}{\d} + \norm{\d}^2\bigr) \\
&= \sum_j\norm{\y_j}^2 + 2\Bigl\langle \sum_j\y_j, \d\Bigr\rangle + N\norm{\d}^2 \\
&= \sum_j\norm{\y_j}^2 + N\norm{\d}^2 ,
\end{aligned}
\]
which is the identity. The second term is \( \ge 0 \) and vanishes exactly when \( \d = \0 \), that is when \( \bar\x - \p \in \ker Q = U \) (@thm-orthogonal-decomposition), that is when \( \bar\x \in \p + U \). This proves the lemma.
:::

Part (b) is the whole of "the best affine subspace passes through the mean". It holds for **every** direction space \( U \), before any optimization over \( U \) has happened, which is why the affine problem costs nothing extra.

::: {#thm-best-fitting-affine-subspace}
[The Best-Fitting Affine Subspace]

Let \( \x_1, \dots, \x_N \in \nR^n \) have mean \( \bar\x \) and centered data matrix \( \X_c \) (@def-centered-data-matrix), let \( \sigma_1 \ge \sigma_2 \ge \dots \ge 0 \) be the singular values of \( \X_c \) (@def-singular-values), and let \( \u_1, \u_2, \dots \) be the left singular vectors of a fixed singular value decomposition of \( \X_c \) (@thm-svd). Let \( 1 \le k \le \min(n, N) \). Among all affine subspaces \( A \subseteq \nR^n \) of dimension at most \( k \), the total squared distance
\[
D(A) \coloneqq \sum_{j=1}^{N} d(\x_j, A)^2
\]
is smallest for
\[
A_0 = \bar\x + \Span(\u_1, \dots, \u_k) ,
\]
and its smallest value is \( \sum_{i > k}\sigma_i^2 \). Moreover **every** minimizing \( A \) contains \( \bar\x \).
:::

::: {.idea}
Two optimizations in sequence, and @lem-mean-minimizes-spread does the outer one first. ① For a *fixed* direction space \( U \), the best translate is the one through \( \bar\x \), whatever \( U \) is. ② With the translate fixed at \( \bar\x \), the objective becomes the total squared distance from the **centered** points to the subspace \( U \) — which is exactly the quantity Chapter 13 §10 minimized. So nothing new has to be proved about subspaces; the work is entirely in noticing that step ① does not interact with step ②.
:::

::: {.proof}
Write \( A = \p + U \) with \( \dim U \le k \), and let \( Q = \I_n - P_U \). By @lem-mean-minimizes-spread (a),
\[
D(\p + U) = \sum_j \norm{Q(\x_j - \p)}^2 ,
\]
and by part (b) of the same lemma this is at least \( \sum_j\norm{Q(\x_j - \bar\x)}^2 = D(\bar\x + U) \), with equality exactly when \( \bar\x \in \p + U \). So it suffices to minimize \( D(\bar\x + U) \) over subspaces \( U \) with \( \dim U \le k \).

Now \( \norm{Q(\x_j - \bar\x)} = \norm{\c_j - P_U\c_j} = d(\c_j, U) \) by @def-distance-to-subspace, where \( \c_j = \x_j - \bar\x \) is the \( j \)-th column of \( \X_c \). Hence
\[
D(\bar\x + U) = \sum_{j=1}^{N} d(\c_j, U)^2 ,
\]
which is the quantity \( D(U) \) of @cor-best-fitting-subspace for the matrix \( \X_c \in M_{n \times N}(\nR) \). That corollary, applicable because \( 1 \le k \le \min(n,N) \), says that the minimum over \( \dim U \le k \) is \( \sum_{i>k}\sigma_i^2 \) and is attained at \( U_0 = \Span(\u_1, \dots, \u_k) \). Combining, \( D(A) \ge \sum_{i>k}\sigma_i^2 \) for every admissible \( A \), with equality at \( A_0 = \bar\x + U_0 \).

Finally let \( A = \p + U \) be any minimizer. Then \( D(\p+U) = D(\bar\x + U) \), since the right side is admissible and no smaller; by the equality clause of @lem-mean-minimizes-spread (b) this forces \( \bar\x \in \p + U = A \). This proves the theorem.
:::

::: {.check}
Is the minimizing \( A_0 \) unique? Take the four centered points \( (1,0), (-1,0), (0,1), (0,-1) \) in \( \nR^2 \) and \( k = 1 \).
:::

::: {.solution}
No. Here \( \bar\x = \0 \) and \( \X_c\X_c\tp = \diag(2,2) \), so \( \sigma_1 = \sigma_2 = \sqrt2 \) and the theorem's minimum is \( \sigma_2^2 = 2 \). Every line through the origin attains it: for \( \Span(\e_1) \) the four squared distances are \( 0, 0, 1, 1 \); for \( \Span\bigl((1,1)\bigr) \) each point is at squared distance \( 1 - \tfrac12 = \tfrac12 \). Total \( 2 \) in both cases. What the theorem asserts is that \( A_0 \) is *a* minimizer and that \( \sum_{i>k}\sigma_i^2 \) is *the* minimum value; uniqueness fails exactly when \( \sigma_k = \sigma_{k+1} \), just as the truncation of @def-truncated-svd is non-unique then.
:::

## The sample covariance matrix

Fix a direction \( \w \in \nR^n \) with \( \w \ne \0 \) and look at the data through it: each point \( \x_j \) has the single coordinate \( t_j = \w\tp\x_j \) along \( \w \). The mean of these numbers is
\[
\frac1N\sum_j \w\tp\x_j = \w\tp\bar\x ,
\]
and their spread about that mean is the number
\[
\begin{aligned}
\frac1N\sum_{j=1}^{N}\bigl(\w\tp\x_j - \w\tp\bar\x\bigr)^2
&= \frac1N\sum_{j=1}^{N}\bigl(\w\tp\c_j\bigr)^2 \\
&= \frac1N\,\w\tp\X_c\X_c\tp\,\w ,
\end{aligned}
\]
the last step because \( \sum_j(\w\tp\c_j)^2 = \norm{\X_c\tp\w}^2 = \w\tp\X_c\X_c\tp\w \). The direction \( \w \) enters only through a quadratic form, and the matrix of that form does not depend on \( \w \). That is a recurring expression, so it gets a name.

*The sample covariance matrix is the single matrix that answers "how spread out are the data in direction \( \w \)?" for every \( \w \) at once.*

::: {#def-sample-covariance}
[Sample covariance matrix]

Let \( \x_1, \dots, \x_N \in \nR^n \) with centered data matrix \( \X_c \) (@def-centered-data-matrix). The **sample covariance matrix** of the data is
\[
\S \coloneqq \frac1N\,\X_c\X_c\tp \in M_n(\nR) ,
\]
with entries
\[
s_{ab} = \frac1N\sum_{j=1}^{N}(x_{aj} - \bar x_a)(x_{bj} - \bar x_b)
\qquad (1 \le a, b \le n) .
\]
For \( \w \in \nR^n \) with \( \w \ne \0 \), the **variance of the data in the direction \( \w \)** is the number \( \w\tp\S\w/\norm{\w}^2 \), which for a **unit** \( \w \) is \( \w\tp\S\w \); and the **total variance** of the data is \( \tr\S \).
:::

Clause by clause. The factor \( 1/N \) makes \( \S \) an average, so it does not grow when data are duplicated. The entry \( s_{aa} \) is the ordinary variance of the \( a \)-th measured quantity, and \( s_{ab} \) for \( a \ne b \) says whether quantities \( a \) and \( b \) tend to deviate from their means in the same direction (positive) or in opposite directions (negative). The centering is inside the definition, not optional: without it the same formula would measure spread about \( \0 \) rather than about the data.

Note also what \( \S \) does **not** depend on: the order of the columns, since the defining sum runs over all of them. It does depend on the units of each coordinate, which is the subject of the warning below.

::: {#exm-covariance-examples}
[Three covariance matrices]

::: {.enumerate options="label=(\alph*)"}
1. The four points of @exm-centering-examples (a). Then
\[
\X_c\X_c\tp = \begin{pmatrix} 10 & 6 \\ 6 & 10\end{pmatrix},
\qquad
\S = \begin{pmatrix} 5/2 & 3/2 \\ 3/2 & 5/2\end{pmatrix} .
\]
Both coordinates have variance \( 5/2 \), and the positive off-diagonal entry says they rise and fall together.
2. Two points \( \pm\v \) in \( \nR^n \) with \( \v \ne \0 \), so \( N = 2 \) and \( \bar\x = \0 \). Then \( \X_c\X_c\tp = 2\v\v\tp \) and \( \S = \v\v\tp \), of rank one: all the spread is in one direction, and \( \w\tp\S\w = (\w\tp\v)^2 \) vanishes for every \( \w \perp \v \).
3. \( N = 1 \). Then \( \X_c = \0 \) and \( \S = \0 \): no direction has any spread.
:::
:::

Change the definition in one place and it stops being a covariance. Replacing \( \X_c \) by \( \X \) gives \( \tfrac1N\X\X\tp \), whose \( (a,a) \) entry is the mean of \( x_{aj}^2 \) rather than the variance; for the data of (a) it is \( \begin{psmallmatrix} 46/4 & 30/4 \\ 30/4 & 26/4\end{psmallmatrix} \), which is not \( \S \), and its top eigenvector is a multiple of \( (1, 0.72\ldots) \) rather than of \( (1,1) \). The clause that fails is the subtraction of the mean, and with it every statement below.

::: {#prp-covariance-and-svd}
[The Covariance Matrix and the Singular Value Decomposition]

Let \( \X_c \in M_{n \times N}(\nR) \) be a centered data matrix with singular values \( \sigma_1 \ge \sigma_2 \ge \dots \) (padded with zeros to length \( n \)), and let \( \X_c = \U\vSigma\V\tp \) be a singular value decomposition with columns \( \u_1, \dots, \u_n \) of \( \U \). Put \( \S = \tfrac1N\X_c\X_c\tp \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \S \) is symmetric and \( \S \succeq 0 \);
2. \( \S\u_i = \dfrac{\sigma_i^2}{N}\,\u_i \) for every \( i \), so the eigenvalues of \( \S \) are \( \sigma_1^2/N \ge \dots \ge \sigma_n^2/N \) and the \( \u_i \) are an orthonormal eigenbasis;
3. for every \( \w \ne \0 \), the variance of the data in the direction \( \w \) is the Rayleigh quotient \( R_{\S}(\w) \) of @def-rayleigh-quotient;
4. \( \tr\S = \dfrac1N\sum_{j=1}^{N}\norm{\x_j - \bar\x}^2 = \dfrac1N\sum_{i}\sigma_i^2 \).
:::
:::

::: {.idea}
Every part is one line once \( \X_c = \U\vSigma\V\tp \) is written down: (a) and (b) because \( \X_c\X_c\tp = \U(\vSigma\vSigma\tp)\U\tp \) is already a diagonalization, (c) because the computation before @def-sample-covariance *was* the Rayleigh quotient, and (d) because the trace does not notice the unitary factors and reads the same quantity off the rows and off the columns.
:::

::: {.proof}
(a) \( \S\tp = \tfrac1N(\X_c\X_c\tp)\tp = \tfrac1N\X_c\X_c\tp = \S \), and for every \( \w \), \( \w\tp\S\w = \tfrac1N\norm{\X_c\tp\w}^2 \ge 0 \); with symmetry this is @def-positive-semidefinite.

(b) Since \( \V \) is orthogonal, \( \V\tp\V = \I_N \), so
\[
\X_c\X_c\tp = \U\vSigma\V\tp\V\vSigma\tp\U\tp = \U(\vSigma\vSigma\tp)\U\tp ,
\]
and \( \vSigma\vSigma\tp = \diag(\sigma_1^2, \dots, \sigma_n^2) \) by the shape of \( \vSigma \) in @thm-svd. Multiplying on the right by \( \u_i \) and using \( \U\tp\u_i = \e_i \) gives \( \X_c\X_c\tp\u_i = \sigma_i^2\u_i \); divide by \( N \). The \( \u_i \) are orthonormal and there are \( n \) of them, so they are an orthonormal basis of \( \nR^n \), and the list \( \sigma_i^2/N \) is decreasing.

(c) By the computation preceding @def-sample-covariance, the variance in direction \( \w \) is \( \w\tp\S\w/\norm{\w}^2 \). Since \( \S \) is symmetric, \( R_{\S}(\w) = \inner{\S\w}{\w}/\inner{\w}{\w} = \w\tp\S\w/\norm{\w}^2 \) by @def-rayleigh-quotient, which is the same number.

(d) The \( j \)-th diagonal entry of \( \X_c\tp\X_c \) is \( \norm{\c_j}^2 \), so \( \tr(\X_c\tp\X_c) = \sum_j\norm{\c_j}^2 \); and \( \tr(\X_c\X_c\tp) = \tr(\X_c\tp\X_c) \) by @thm-trace-properties (3). On the other hand the display in (b) and the same trace identity give
\[
\begin{aligned}
\tr(\X_c\X_c\tp) &= \tr\bigl(\U(\vSigma\vSigma\tp)\U\tp\bigr) \\
&= \tr\bigl((\vSigma\vSigma\tp)\U\tp\U\bigr) = \sum_i\sigma_i^2 ,
\end{aligned}
\]
using \( \U\tp\U = \I_n \). Dividing by \( N \) gives both equalities. This proves the proposition.
:::

Part (c) connects this section to Chapter 17. The question "which direction has the most spread?" is the question "where is \( R_{\S} \) largest?", and @prp-rayleigh-basic answers it: the maximum is \( \lambda_1(\S) = \sigma_1^2/N \), attained at \( \u_1 \). "Which direction has the most spread among those orthogonal to \( \u_1, \dots, \u_{k-1} \)?" is answered the same way by @prp-rayleigh-deflation, with maximum \( \sigma_k^2/N \) at \( \u_k \). So the leading left singular vectors are not only the best-fitting directions of @thm-best-fitting-affine-subspace; they are also, one at a time, the directions of greatest remaining spread. The two descriptions agree because they are the two halves of one Pythagorean identity, which is the next theorem.

::: {#def-principal-directions}
[Principal directions and components]

In the situation of @prp-covariance-and-svd, the unit vectors \( \u_1, \u_2, \dots \) are the **principal directions** of the data, and the numbers \( \u_i\tp\c_1, \dots, \u_i\tp\c_N \) are the \( i \)-th **principal components**: the coordinates of the centered data along \( \u_i \).
:::

## How much variance a subspace explains

::: {#thm-variance-explained}
[Variance Captured by the Principal Directions]

In the situation of @prp-covariance-and-svd, let \( 1 \le k \le \min(n, N) \), let \( U_0 = \Span(\u_1, \dots, \u_k) \) and let \( P \) be the orthogonal projection onto a subspace \( U \) with \( \dim U \le k \). Write
\[
\operatorname{var}(U) \coloneqq \frac1N\sum_{j=1}^{N}\norm{P(\x_j - \bar\x)}^2 .
\]
Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \operatorname{var}(U) \) is the total variance of the projected points \( P\x_1, \dots, P\x_N \), whose mean is \( P\bar\x \);
2. \( \operatorname{var}(U) + \dfrac1N D(\bar\x + U) = \tr\S \), where \( D \) is as in @thm-best-fitting-affine-subspace;
3. \( \operatorname{var}(U) \le \operatorname{var}(U_0) = \dfrac1N\sum_{i \le k}\sigma_i^2 \);
4. if \( \X_c \ne \0 \), the fraction of the total variance captured by \( U_0 \) is
\[
\frac{\operatorname{var}(U_0)}{\tr\S} = \frac{\sigma_1^2 + \dots + \sigma_k^2}{\sigma_1^2 + \sigma_2^2 + \dots} .
\]
:::
:::

::: {.idea}
Everything is Pythagoras applied \( N \) times and then added up. For each centered point, \( \norm{\c_j}^2 \) splits into the part \( P \) keeps and the part it throws away; averaging the first over \( j \) is \( \operatorname{var}(U) \), averaging the second is the fitting error of @thm-best-fitting-affine-subspace, and averaging the total is \( \tr\S \) by @prp-covariance-and-svd (d). Once (b) is available, (c) and (d) are just the theorem already proved, divided by \( N \).
:::

::: {.proof}
(a) The mean of \( P\x_1, \dots, P\x_N \) is \( \tfrac1N\sum_j P\x_j = P\bar\x \) by linearity of \( P \), so the \( j \)-th centered projected point is \( P\x_j - P\bar\x = P\c_j \). By @prp-covariance-and-svd (d) applied to these \( N \) points, their total variance is \( \tfrac1N\sum_j\norm{P\c_j}^2 = \operatorname{var}(U) \).

(b) Fix \( j \). The vectors \( P\c_j \) and \( \c_j - P\c_j \) are orthogonal, the first lying in \( U \) and the second in \( U^{\perp} \) (@thm-orthogonal-decomposition), so @thm-pythagoras gives
\[
\norm{\c_j}^2 = \norm{P\c_j}^2 + \norm{\c_j - P\c_j}^2 .
\]
Summing over \( j \) and dividing by \( N \): the left side is \( \tr\S \) by @prp-covariance-and-svd (d), the first term on the right is \( \operatorname{var}(U) \), and the second is \( \tfrac1N\sum_j d(\c_j, U)^2 = \tfrac1N D(\bar\x + U) \), as computed in the proof of @thm-best-fitting-affine-subspace.

(c) By (b), maximizing \( \operatorname{var}(U) \) over \( \dim U \le k \) is the same as minimizing \( D(\bar\x + U) \), and @thm-best-fitting-affine-subspace says the minimum is \( \sum_{i>k}\sigma_i^2 \), attained at \( U_0 \). Hence \( \operatorname{var}(U) \le \operatorname{var}(U_0) \), and by (b) again,
\[
\begin{aligned}
\operatorname{var}(U_0) &= \tr\S - \frac1N\sum_{i>k}\sigma_i^2 \\
&= \frac1N\sum_i\sigma_i^2 - \frac1N\sum_{i>k}\sigma_i^2
= \frac1N\sum_{i\le k}\sigma_i^2 .
\end{aligned}
\]

(d) If \( \X_c \ne \0 \) then some \( \sigma_i > 0 \), so \( \tr\S = \tfrac1N\sum_i\sigma_i^2 > 0 \) and the quotient is defined; dividing the value in (c) by it cancels the \( 1/N \). This proves the theorem.
:::

So "the first \( k \) principal directions explain \( \bigl(\sum_{i\le k}\sigma_i^2\bigr)/\bigl(\sum_i\sigma_i^2\bigr) \) of the variance" is a theorem about the \( N \) given points, not a convention: the numerator is the variance of the projected cloud, the denominator is the variance of the original cloud, and part (b) is what makes the two add up with nothing left over.

::: {#exm-pca-four-points}
[Four points, done exactly]

Take the four points \( (5,4), (4,1), (2,3), (1,0) \) of @exm-centering-examples (a). Find the mean, the sample covariance matrix, the principal directions, the best-fitting line, the total squared distance to it, and the fraction of variance it explains.
:::

::: {.solution}
*Mean and centering.* \( \bar\x = (3,2) \), and \( \X_c \) has columns \( (2,2), (1,-1), (-1,1), (-2,-2) \), as computed above.

*Covariance.* \( \X_c\X_c\tp = \begin{psmallmatrix} 10 & 6 \\ 6 & 10\end{psmallmatrix} \), so \( \S = \begin{psmallmatrix} 5/2 & 3/2 \\ 3/2 & 5/2\end{psmallmatrix} \). Since \( \X_c\X_c\tp \) has the form \( a\I + b\J \) it sends \( (1,1) \) to \( 16(1,1) \) and \( (1,-1) \) to \( 4(1,-1) \), so its eigenvalues are \( 16 \) and \( 4 \) with
\[
\u_1 = \tfrac{1}{\sqrt2}(1,1), \qquad \u_2 = \tfrac1{\sqrt2}(1,-1) .
\]
By @prp-covariance-and-svd (b), \( \sigma_1^2 = 16 \) and \( \sigma_2^2 = 4 \), that is \( \sigma_1 = 4 \) and \( \sigma_2 = 2 \), and the eigenvalues of \( \S \) are \( 4 \) and \( 1 \). Check: \( \tr\S = 5 \) and \( 4 + 1 = 5 \).

*Total variance, two ways.* The squared distances of the centered points from \( \0 \) are \( 8, 2, 2, 8 \), of average \( 5 \). And \( \tfrac1N\sum_i\sigma_i^2 = \tfrac14(16+4) = 5 \), as @prp-covariance-and-svd (d) requires.

*Best-fitting line.* By @thm-best-fitting-affine-subspace with \( k = 1 \) it is
\[
A_0 = (3,2) + \Span\bigl((1,1)\bigr),
\]
the line \( y = x - 1 \), and the total squared distance is \( \sigma_2^2 = 4 \). Directly: \( (5,4) \) and \( (1,0) \) lie on the line, contributing \( 0 \); for \( (4,1) \) the centered point is \( (1,-1) \), whose projection onto \( \Span\bigl((1,1)\bigr) \) is \( \0 \), so its squared distance is \( 2 \); likewise \( 2 \) for \( (2,3) \). Total \( 4 \), as predicted.

*Variance explained.* \( \operatorname{var}(U_0) = \tfrac14\sigma_1^2 = 4 \), out of \( \tr\S = 5 \): the first principal direction explains \( 16/20 = 80\% \) of the variance, and the remaining \( 20\% \) is the average squared distance \( 4/4 = 1 \) to the line. The two add to \( 5 \), which is @thm-variance-explained (b).
:::

::: {.warning}
**Principal directions are not "the important directions": they change when you change the units.** Take the four centered points \( (1,0), (-1,0), (0,2), (0,-2) \). Then \( \X_c\X_c\tp = \diag(2, 8) \), so the first principal direction is \( \e_2 \). Now suppose the first coordinate was measured in meters and we re-express it in units three times smaller, which multiplies row \( 1 \) by \( 3 \). The data are the same data; the new centered matrix is \( \D\X_c \) with \( \D = \diag(3,1) \), and
\[
(\D\X_c)(\D\X_c)\tp = \D\,\diag(2,8)\,\D = \diag(18, 8) ,
\]
so the first principal direction is now \( \e_1 \). It has turned by a right angle because of a choice of units. Nothing is wrong with the theorem — \( \D\X_c \) really is a different matrix — but "the direction of greatest variance" is a statement about a coordinate system, not about the data alone. Rescaling each coordinate to variance \( 1 \) before starting is one common repair; it is a modeling decision, and it is not forced by anything proved here.
:::

## Computing it, and what is not proved

Two closing matters, one computational and one about scope.

**Never form \( \X_c\X_c\tp \).** Everything above is stated in terms of \( \S \), and \( \S \) is the natural object to state it with; but forming \( \S \) and then finding its eigenvalues is the worst available way to compute the principal directions. The reason is @thm-normal-equations-squares-conditioning: passing from \( \A \) to \( \A^{*}\A \) squares the condition number, \( \kappa_2(\A^{*}\A) = \kappa_2(\A)^2 \), and Section 3 of this chapter turns that into a count of lost digits — @thm-normal-equations-lose-twice says the product route loses about \( 2\log_{10}\kappa_2 \) decimal digits where a backward stable factorization of \( \A \) itself loses about \( \log_{10}\kappa_2 \). The same arithmetic applies with \( \A = \X_c\tp \) — but only when that matrix has full column rank, which is the hypothesis of @thm-normal-equations-squares-conditioning. That asks for \( \rank\X_c = n \), and \( \X_c\1 = \0 \) already forces \( \rank\X_c \le N - 1 \), so it fails whenever \( N \le n \): for three records of ten measured quantities there is nothing to apply. The count that follows needs no hypothesis on the rank, and it is the one to remember.

Here is the count in this setting. Each entry of \( \X_c\X_c\tp \) is an inner product of two rows, each of length \( N \), so by @thm-inner-product-backward-error the computed product is \( \X_c\X_c\tp + \vDelta \) with \( \norm{\vDelta}_2 \) of order \( c(n, N)\,u\,\sigma_1^2 \), where \( u \) is the unit roundoff of Section 1 and \( c \) is a modest dimensional factor. It is a factor and not a constant because the entrywise bound has to be aggregated over the whole \( n \times n \) product, by the same count as in Section 3, where the corresponding step reads \( \norm{\C - \A^{*}\A} \le \gamma_m\norm{\A}_F^2 \le n\gamma_m\norm{\A}^2 \): the length of the inner products sits inside \( \gamma \), and passing from the Frobenius norm to the spectral norm puts their number in front. Here that makes \( c(n, N) \) of size about \( nN \).

If the implementation forms only the upper triangle and reflects it — an assumption about the computation, not something proved here — then \( \vDelta \) is symmetric, and @cor-weyl-perturbation says a symmetric perturbation of that size moves every eigenvalue by at most \( \norm{\vDelta}_2 \). So every \( \sigma_i^2 \) below \( c(n,N)\,u\,\sigma_1^2 \) — that is, up to the factor \( \sqrt{c} \), every \( \sigma_i \) below \( \sqrt u\,\sigma_1 \) — is indistinguishable from \( 0 \) in the computed product, while a backward stable factorization of \( \X_c \) itself keeps it. Those are exactly the singular values a low-rank fit has to decide about. The right computation therefore works on \( \X_c \) directly and never builds the product.

What this chapter does **not** do is assemble that computation. The ingredients are here — the Householder reductions of Section 3, the shifted \( \Q\R \) iteration of Section 5 — but no algorithm for the singular values of a given matrix is written down or analyzed anywhere in this book. So the paragraph above pays the parenthesis of the last clause of Chapter 13 §10's promise, that a singular value decomposition is "never" computed by forming \( \A^{*}\A \) and finding its eigenvalues; the clause itself, how one is actually computed for a large matrix, is left unpaid.

**The finite population, and the boundary.** Chapter 13 §10 said that the statistics needs "a probabilistic model, a reason to prefer squared error, and an argument that the sample answer says something about the population". Here is exactly what has been delivered.

*A probabilistic model, for the finite population of the data themselves.* Regard the \( N \) columns as a population of \( N \) equally likely outcomes, each of weight \( 1/N \). Then "expectation" means the average \( \tfrac1N\sum_j \), which needs no measure theory and no limit, and the mean of the population is \( \bar\x \). For two real-valued quantities \( f, g \) on it, with averages \( \bar f = \tfrac1N\sum_j f(\x_j) \) and \( \bar g = \tfrac1N\sum_j g(\x_j) \), the **covariance** of the population is
\[
\operatorname{Cov}(f, g) \coloneqq \frac1N\sum_{j=1}^{N}\bigl(f(\x_j) - \bar f\bigr)\bigl(g(\x_j) - \bar g\bigr) ,
\]
and the variance of \( f \) is \( \operatorname{Cov}(f, f) \). With that reading, the variance of \( \x \mapsto \w\tp\x \) is \( \w\tp\S\w \), which for a **unit** \( \w \) is the variance in the direction \( \w \) of @def-sample-covariance, hence the Rayleigh quotient of @prp-covariance-and-svd (c); and the covariance of \( \x \mapsto x_a \) with \( \x \mapsto x_b \) is \( s_{ab} \), which is the displayed formula of @def-sample-covariance read backwards. So \( \S \) **is** the covariance matrix of that population, and @thm-variance-explained is a statement about it. This much is a theorem, and it is what was proved above.

*A reason to prefer squared error.* Three, none of them a proof that squared error is the right criterion, which is a modeling question. (i) It does not depend on the coordinate frame: an orthogonal change of coordinates is an isometry, so it leaves every distance \( d(\x_j, A) \), hence \( D(A) \), unchanged. The largest entry of the error has no such property — the matrix \( \diag(1,0) \) has largest entry \( 1 \), while the same matrix read in the frame \( \tfrac1{\sqrt2}(1,\pm1) \) is \( \tfrac12\begin{psmallmatrix} 1 & 1 \\ 1 & 1\end{psmallmatrix} \), with largest entry \( \tfrac12 \) — and Chapter 13 §10's warning shows that it really does prefer a different answer. (ii) It splits: @thm-variance-explained (b) says captured plus lost equals total, exactly, which is what makes a *fraction* of variance meaningful at all. (iii) It has a closed-form minimizer, computable by a single factorization (@thm-eckart-young); for the sum of **unsquared** distances \( \sum_j d(\x_j, A) \), nothing proved in this book produces a minimizer at all.

*An argument that the sample says something about a larger population.* This is **not** proved here, and it cannot be with the tools of this book. Such an argument requires a probability model in which the \( N \) points are drawn from a distribution on \( \nR^n \), an expectation defined by an integral rather than a finite sum, and theorems saying that \( \S \) converges to the distribution's covariance and that its eigenvectors converge to the distribution's principal directions. Every one of those belongs to probability and statistics, which this book does not develop. Chapter 13 §10's sentence promised it; the honest correction is that linear algebra supplies the finite-population model and the reasons for squared error, and hands the inference to a subject this book does not enter.

::: {.remark}
**The divisor \( N \) versus \( N-1 \).** Statistics usually defines the sample covariance with \( 1/(N-1) \), which presupposes \( N \ge 2 \), because that makes it an unbiased estimator of a population covariance — a statement inside the probability model just excluded, and one we therefore cannot prove. With the finite-population reading the divisor is \( N \), and that is the convention of @def-sample-covariance, which makes sense for every \( N \ge 1 \). For \( N \ge 2 \) the choice changes nothing here: it multiplies \( \S \) by \( N/(N-1) \), which scales every eigenvalue by the same factor, changes no eigenvector, and leaves every ratio such as @thm-variance-explained (d) exactly as it was.
:::

## Exercises

### A. Check your understanding

:::: {#exr-principal-components-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the centered data matrix and the sample covariance matrix, and say what \( \w\tp\S\w \) means for a unit vector \( \w \).
2. State @thm-best-fitting-affine-subspace, including the value of the minimum and the claim about the mean.
3. True or false: the principal directions of a data set are the eigenvectors of \( \X\X\tp \). Justify your answer.
4. True or false: if \( N = 3 \) points in \( \nR^{10} \) are given, then \( \S \) has rank at most \( 2 \). Justify your answer.
5. Why should a computation of the principal directions avoid forming \( \X_c\X_c\tp \)?
:::
::::

::: {.solution}
(a) \( \X_c = \X - \bar\x\1\tp \), the data matrix with the mean column subtracted from every column, and \( \S = \tfrac1N\X_c\X_c\tp \) (@def-centered-data-matrix, @def-sample-covariance). For a unit \( \w \), \( \w\tp\S\w \) is the variance of the \( N \) numbers \( \w\tp\x_j \), that is the spread of the data in the direction \( \w \).

(b) Among all affine subspaces of \( \nR^n \) of dimension at most \( k \le \min(n,N) \), the total squared distance \( \sum_j d(\x_j, A)^2 \) is smallest at \( A_0 = \bar\x + \Span(\u_1, \dots, \u_k) \), the minimum value is \( \sum_{i>k}\sigma_i^2 \) with \( \sigma_i \) the singular values of \( \X_c \), and every minimizer contains \( \bar\x \).

(c) False in general; they are the eigenvectors of \( \X_c\X_c\tp \). For the four points of @exm-pca-four-points, \( \X\X\tp = \begin{psmallmatrix} 46 & 30 \\ 30 & 26\end{psmallmatrix} \), whose eigenvalues are \( 36 \pm 10\sqrt{10} \) and whose top eigenvector is not \( (1,1) \), while the top principal direction is. The two **matrices** agree exactly when \( \bar\x = \0 \), since \( \X\X\tp = \X_c\X_c\tp + N\bar\x\bar\x\tp \). Their **eigenvectors** can agree without that: for the two points \( (0,0) \) and \( (2,0) \) the mean is \( (1,0) \ne \0 \), yet \( \X\X\tp = \diag(4,0) \) and \( \X_c\X_c\tp = \diag(2,0) \) have the same eigenvectors.

(d) True. \( \rank\S = \rank\X_c \) — since \( \nul(\X_c\tp) = \nul(\X_c\X_c\tp) \), because \( \X_c\X_c\tp\w = \0 \) gives \( \norm{\X_c\tp\w}^2 = \w\tp\X_c\X_c\tp\w = 0 \) — and \( \X_c\1 = \0 \) with \( \X_c \) having \( 3 \) columns forces \( \rank\X_c \le 2 \). Centering costs at most one from the rank and sometimes nothing:
\[
\rank\X - 1 \ \le\ \rank\X_c \ \le\ \rank\X ,
\]
the right inequality because \( \X_c = \X(\I_N - \tfrac1N\1\1\tp) \) is a product (@thm-rank-product-inequality), the left because \( \X = \X_c + \bar\x\1\tp \) adds to it a matrix of rank at most \( 1 \) (@exr-rank-c1). The drop need not happen: for \( \x_1 = (1,0) \), \( \x_2 = (2,0) \), \( \x_3 = (0,1) \) the mean is \( (1, \tfrac13) \ne \0 \), yet \( \rank\X = \rank\X_c = 2 \).

(e) Because forming the product destroys the small singular values. Each entry of \( \X_c\X_c\tp \) is an inner product, so the computed product is \( \X_c\X_c\tp + \vDelta \) with \( \norm{\vDelta}_2 \) of order \( c(n,N)\,u\,\sigma_1^2 \) (@thm-inner-product-backward-error); if \( \vDelta \) is symmetric, @cor-weyl-perturbation moves every eigenvalue by at most that, so every \( \sigma_i \) below about \( \sqrt u\,\sigma_1 \) becomes indistinguishable from \( 0 \), while a backward stable factorization of \( \X_c \) itself keeps it — and those are exactly the singular values a low-rank fit has to decide about. The conditioning statement \( \kappa_2(\X_c\X_c\tp) = \kappa_2(\X_c)^2 \) says the same thing in digits (@thm-normal-equations-squares-conditioning, @thm-normal-equations-lose-twice), but it needs \( \X_c\tp \) to have full column rank, which fails in part (d) above; the Weyl count needs no hypothesis on the rank.
:::

### B. Practice

:::: {#exr-principal-components-b1}
[B1: A four-point cloud]

The points \( (1,1), (3,5), (5,3), (7,7) \) are given in \( \nR^2 \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \bar\x \), \( \X_c \), \( \X_c\X_c\tp \) and \( \S \).
2. Find the singular values of \( \X_c \) and the principal directions.
3. Find the best-fitting line, the total squared distance to it, and the fraction of variance it explains. Verify the total squared distance directly.
:::
::::

::: {.solution}
(a) The sum of the four points is \( (16, 16) \), so \( \bar\x = (4,4) \) and
\[
\X_c = \begin{pmatrix} -3 & -1 & 1 & 3 \\ -3 & 1 & -1 & 3\end{pmatrix},
\qquad
\X_c\X_c\tp = \begin{pmatrix} 20 & 16 \\ 16 & 20\end{pmatrix},
\]
so \( \S = \begin{psmallmatrix} 5 & 4 \\ 4 & 5\end{psmallmatrix} \).

(b) \( \X_c\X_c\tp \) sends \( (1,1) \) to \( 36(1,1) \) and \( (1,-1) \) to \( 4(1,-1) \), so \( \sigma_1^2 = 36 \), \( \sigma_2^2 = 4 \), that is \( \sigma_1 = 6 \), \( \sigma_2 = 2 \), with \( \u_1 = \tfrac1{\sqrt2}(1,1) \) and \( \u_2 = \tfrac1{\sqrt2}(1,-1) \). The eigenvalues of \( \S \) are \( 9 \) and \( 1 \), which are \( \sigma_i^2/4 \) (@prp-covariance-and-svd (b)).

(c) By @thm-best-fitting-affine-subspace the best line is \( (4,4) + \Span\bigl((1,1)\bigr) \), that is \( y = x \), with total squared distance \( \sigma_2^2 = 4 \). By @thm-variance-explained (d) it explains \( 36/40 = 90\% \) of the variance. Directly: \( (1,1) \) and \( (7,7) \) lie on \( y = x \); the centered points \( (-1,1) \) and \( (1,-1) \) both project to \( \0 \) on \( \Span\bigl((1,1)\bigr) \), so each contributes \( 2 \). Total \( 4 \).
:::

:::: {#exr-principal-components-b2}
[B2: Variance direction by direction]

For the data of Exercise B1, compute the variance in the directions \( \e_1 \), \( \e_2 \), \( \tfrac1{\sqrt2}(1,1) \) and \( \tfrac1{\sqrt2}(1,-1) \), and say which of them is largest and why that was predictable.
::::

::: {.solution}
With \( \S = \begin{psmallmatrix} 5 & 4 \\ 4 & 5\end{psmallmatrix} \) and @def-sample-covariance, the variance in a unit direction \( \w \) is \( \w\tp\S\w \):
\[
\e_1 \mapsto 5,
\quad
\e_2 \mapsto 5,
\quad
\tfrac{(1,1)}{\sqrt2} \mapsto 9,
\quad
\tfrac{(1,-1)}{\sqrt2} \mapsto 1 .
\]
The largest is \( 9 \), in the direction \( \u_1 \). This was predictable from @prp-covariance-and-svd (c) and @prp-rayleigh-basic: the variance in a unit direction is the Rayleigh quotient of \( \S \), whose maximum is \( \lambda_1(\S) = 9 \) and is attained at a unit eigenvector for \( \lambda_1 \). Note also \( 5 + 5 = 9 + 1 = \tr\S \): the total variance is the same however the orthonormal frame is chosen.
:::

:::: {#exr-principal-components-b3}
[B3: Changing the units]

The centered data matrix of a two-coordinate data set is \( \X_c = \begin{psmallmatrix} 3 & -3 & 0 & 0 \\ 0 & 0 & 4 & -4\end{psmallmatrix} \). The second coordinate is then re-expressed in units \( c \) times smaller, which multiplies row \( 2 \) by \( c > 0 \).

::: {.enumerate options="label=(\alph*)"}
1. Find the principal directions before the change.
2. Find the value of \( c \) at which the first principal direction switches from one coordinate axis to the other, and say what happens exactly at that value.
:::
::::

::: {.solution}
(a) \( \X_c\X_c\tp = \diag(18, 32) \), so the principal directions are \( \u_1 = \e_2 \) (variance \( 32/4 = 8 \)) and \( \u_2 = \e_1 \) (variance \( 18/4 = 4.5 \)).

(b) After the change the centered matrix is \( \D\X_c \) with \( \D = \diag(1, c) \), and \( (\D\X_c)(\D\X_c)\tp = \diag(18, 32c^2) \). The first principal direction is \( \e_2 \) when \( 32c^2 > 18 \), that is \( c > 3/4 \), and \( \e_1 \) when \( c < 3/4 \). At \( c = 3/4 \) the two eigenvalues are equal, \( \sigma_1 = \sigma_2 \), and **every** direction is a direction of greatest variance: the principal directions are not determined at all, and the best-fitting line of @thm-best-fitting-affine-subspace is not unique, exactly as in the Quick check above.
:::

### C. Going deeper

:::: {#exr-principal-components-c1}
[C1: The mean is forced, and the projection is not a shortcut]

Let \( \x_1, \dots, \x_N \in \nR^n \) with mean \( \bar\x \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that the point \( \p \in \nR^n \) minimizing \( \sum_j\norm{\x_j - \p}^2 \) is unique and equals \( \bar\x \). (This is the case \( k = 0 \), which @thm-best-fitting-affine-subspace excludes, so it has to be proved rather than quoted.)
2. Hence deduce that for every subspace \( U \), the affine subspace \( \p + U \) minimizing \( D \) over translates of \( U \) is \( \bar\x + U \).
3. Give an example of data and a subspace \( U \) for which \( \bar\x + U \) is **not** the best-fitting affine subspace of its dimension, so that the choice of \( U \) still matters.
:::
::::

::: {.solution}
(a) Apply @lem-mean-minimizes-spread (b) with \( U = \{\0\} \), so that \( Q = \I_n \):
\[
\sum_j\norm{\x_j - \p}^2 = \sum_j\norm{\x_j - \bar\x}^2 + N\norm{\bar\x - \p}^2 .
\]
The first term does not depend on \( \p \) and the second is \( \ge 0 \), vanishing exactly when \( \p = \bar\x \). So the minimum is attained at \( \bar\x \) and nowhere else.

(b) By @lem-mean-minimizes-spread (a), \( D(\p+U) = \sum_j\norm{Q(\x_j-\p)}^2 \), and by part (b) of that lemma this exceeds \( D(\bar\x+U) \) unless \( \bar\x \in \p+U \) — in which case \( \p + U = \bar\x + U \), the two cosets having a common point and the same direction space. So the minimizing translate is \( \bar\x + U \), and as a set it is unique.

(c) Take the four points of @exm-pca-four-points and \( U = \Span(\e_1) \). Then \( \bar\x + U \) is the horizontal line \( y = 2 \), and the centered points \( (2,2), (1,-1), (-1,1), (-2,-2) \) are at squared distances \( 4, 1, 1, 4 \) from \( U \), total \( 10 \). The best line is \( \bar\x + \Span\bigl((1,1)\bigr) \), with total \( 4 \). Both pass through the mean; only one has the right direction. Choosing the translate is free, choosing the direction space is the whole problem.
:::

:::: {#exr-principal-components-c2}
[C2: Total variance is a trace, and what that buys]

Let \( \x_1, \dots, \x_N \in \nR^n \) with sample covariance \( \S \), and let \( \Q \in M_n(\nR) \) be orthogonal.

::: {.enumerate options="label=(\alph*)"}
1. Prove that the data \( \Q\x_1, \dots, \Q\x_N \) have sample covariance \( \Q\S\Q\tp \), and deduce that the total variance \( \tr\S \) is unchanged.
2. Prove that for any orthonormal basis \( (\q_1, \dots, \q_n) \) of \( \nR^n \), the sum of the variances of the data in the \( n \) directions \( \q_i \) equals \( \tr\S \).
3. Deduce that no orthonormal frame can make every coordinate variance small: some \( \q_i \) always has variance at least \( \tr\S/n \). For the data of @exm-pca-four-points, which frames attain that bound?
:::
::::

::: {.solution}
(a) The mean of the transformed data is \( \tfrac1N\sum_j\Q\x_j = \Q\bar\x \), so the transformed centered matrix is \( \Q\X - \Q\bar\x\1\tp = \Q\X_c \). Hence its sample covariance is \( \tfrac1N(\Q\X_c)(\Q\X_c)\tp = \Q\S\Q\tp \). By @thm-trace-properties, \( \tr(\Q\S\Q\tp) = \tr(\S\Q\tp\Q) = \tr\S \), since \( \Q\tp\Q = \I_n \).

(b) By @def-sample-covariance the variance in the unit direction \( \q_i \) is \( \q_i\tp\S\q_i \). Let \( \Q \) be the orthogonal matrix with columns \( \q_1, \dots, \q_n \). Then \( \q_i\tp\S\q_i \) is the \( (i,i) \) entry of \( \Q\tp\S\Q \), so the sum over \( i \) is \( \tr(\Q\tp\S\Q) = \tr\S \) by part (a) applied to \( \Q\tp \).

(c) A sum of \( n \) numbers equal to \( \tr\S \) has a term at least the average \( \tr\S/n \), since otherwise the sum would be \( < \tr\S \). For @exm-pca-four-points, \( \tr\S = 5 \) and the bound is \( 5/2 \); the variances in a frame \( (\q_1, \q_2) \) are \( \q_1\tp\S\q_1 \) and \( \q_2\tp\S\q_2 \), which sum to \( 5 \), so both equal \( 5/2 \) exactly when \( \q_1\tp\S\q_1 = 5/2 \). Writing \( \q_1 = a\u_1 + b\u_2 \) with \( a^2 + b^2 = 1 \) and using \( \S\u_1 = 4\u_1 \), \( \S\u_2 = \u_2 \), this reads \( 4a^2 + b^2 = 5/2 \), and subtracting \( a^2 + b^2 = 1 \) gives \( 3a^2 = 3/2 \), that is \( a^2 = b^2 = 1/2 \). So the bound is attained exactly by the frames whose vectors split their weight equally between \( \u_1 \) and \( \u_2 \) — for instance the standard frame \( (\e_1, \e_2) \), since \( \e_1 = \tfrac1{\sqrt2}(\u_1 + \u_2) \); its two variances are indeed \( 5/2 \) each. The extreme case of the spread is visible only in the principal frame; an arbitrary frame hides it.
:::
