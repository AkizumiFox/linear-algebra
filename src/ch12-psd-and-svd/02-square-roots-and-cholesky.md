# Square Roots and the Cholesky Factorization

A non-negative real number has exactly one non-negative square root, and it is the reason "non-negative" is a useful class of numbers at all: it lets us take lengths, define standard deviations, and undo a squaring. Section 1 produced the matrix analogue as one clause of a theorem. This section makes it an object with a name, adds the one property the clause did not mention — that the square root is a **polynomial** in the matrix — and then turns the same idea into the triangular factorization that elimination discovers, the one Chapter 2 promised and could not yet explain.

Throughout, \( F = \nR \) or \( F = \nC \), and all matrices are over \( F \).

## The positive square root

@thm-psd-characterizations (d) already says that a positive semidefinite \( \A \) has exactly one positive semidefinite square root. That is an existence-and-uniqueness statement, so by the usual convention it deserves a notation.

*The square root of a positive matrix is what you get by taking square roots of its eigenvalues and leaving the eigenvectors alone.*

::: {#thm-psd-square-root}
[The Positive Square Root]

Let \( \A \in M_n(F) \) with \( \A \succeq 0 \). Then there is exactly one \( \C \in M_n(F) \) with \( \C \succeq 0 \) and \( \C^2 = \A \). We write \( \C = \A^{1/2} \), also \( \sqrt{\A} \). Moreover:

::: {.enumerate options="label=(\alph*)"}
1. \( \A^{1/2} = p(\A) \) for some polynomial \( p \) with real coefficients (the nodes \( \lambda_i \) and the values \( \sqrt{\lambda_i} \) are real, so the interpolation of @thm-lagrange-interpolation may be run over \( \nR \), and \( \nR[x] \subseteq \nC[x] \));
2. \( \A^{1/2}\B = \B\A^{1/2} \) for **every** \( \B \in M_n(F) \) with \( \A\B = \B\A \);
3. \( \nul(\A^{1/2}) = \nul(\A) \) and \( \rank \A^{1/2} = \rank \A \); in particular \( \A^{1/2} \) is invertible if and only if \( \A \) is.
:::

The eigenvalues of \( \A^{1/2} \) are the non-negative square roots of those of \( \A \), with the same eigenvectors.
:::

::: {.idea}
Existence and uniqueness are Section 1. What is new is (a), and it is the reason (b) is free. On the spectrum, the square root is just a function \( \lambda \mapsto \sqrt\lambda \) defined at finitely many points, and a function defined at finitely many points is a polynomial — that is Lagrange interpolation from Chapter 5. The functional calculus of Chapter 11 says that applying a polynomial to \( \A \) and applying the corresponding function to the spectrum are the same operation, so the interpolating polynomial evaluated at \( \A \) *is* the square root. Once \( \A^{1/2} \) is a polynomial in \( \A \), anything commuting with \( \A \) commutes with it, with no further work.
:::

::: {.proof}
Existence and uniqueness are @thm-psd-characterizations (d).

(a) Let \( \lambda_1, \dots, \lambda_k \) be the **distinct** eigenvalues of \( \A \) and let \( \A = \sum_i\lambda_i\P_i \) be its spectral resolution (@def-spectral-resolution, @thm-spectral-resolution), which exists because a Hermitian matrix has an orthonormal basis of eigenvectors. Every \( \lambda_i \) is a non-negative real number by @thm-psd-characterizations (b), so the numbers \( \sqrt{\lambda_i} \) are defined and real. Let \( f(\lambda) = \sqrt{\lambda} \) on \( \spec(\A) \). By @thm-functional-calculus-properties (b) and (a),
\[
f(\A)^2 = (f^2)(\A) = \A ,
\]
and by (c) and (d) of the same theorem \( f(\A) \) is Hermitian with spectrum \( \{\sqrt{\lambda_1}, \dots, \sqrt{\lambda_k}\} \subseteq [0, \infty) \), so \( f(\A) \succeq 0 \) by @thm-psd-characterizations (b). Uniqueness gives \( f(\A) = \A^{1/2} \).

The numbers \( \lambda_1, \dots, \lambda_k \) are distinct, so by Lagrange interpolation (@thm-lagrange-interpolation) there is a polynomial \( p \) of degree at most \( k - 1 \), with real coefficients, such that \( p(\lambda_i) = \sqrt{\lambda_i} \) for every \( i \). By @thm-functional-calculus-properties (a), \( p(\A) = \sum_i p(\lambda_i)\P_i = f(\A) = \A^{1/2} \).

(b) Suppose \( \A\B = \B\A \). Then \( \B \) commutes with every power of \( \A \), hence with every polynomial in \( \A \), hence with \( p(\A) = \A^{1/2} \).

(c) If \( \A^{1/2}\x = \0 \) then \( \A\x = \A^{1/2}(\A^{1/2}\x) = \0 \). Conversely, if \( \A\x = \0 \), then since \( \A^{1/2} \) is Hermitian,
\[
\norm{\A^{1/2}\x}^2 = \inner{\A^{1/2}\x}{\A^{1/2}\x} = \inner{\A\x}{\x} = 0 ,
\]
so \( \A^{1/2}\x = \0 \). Hence the two null spaces agree, and the ranks agree by @thm-rank-nullity-matrix. Invertibility is the case \( \nul = \{\0\} \) (@thm-invertible-tfae).

The last sentence is the spectral mapping statement of @thm-functional-calculus-properties (d) for \( f = \sqrt{\ } \).
:::

Two routes to the same matrix, then, and both are worth practicing: assemble \( \sum_i\sqrt{\lambda_i}\P_i \) from the projections, or find one interpolating polynomial and substitute.

::: {#exm-square-root-computed}
[Two Square Roots]

Compute \( \A^{1/2} \) for

::: {.enumerate options="label=(\alph*)"}
1. \( \A = \begin{pmatrix} 13 & 12 \\ 12 & 13\end{pmatrix} \);
2. \( \B = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2\end{pmatrix} \),
:::

in each case by the spectral resolution and by a polynomial.
:::

::: {.solution}
(a) \( \A \) is symmetric. Since \( \A(1,1) = (25, 25) \) and \( \A(1,-1) = (1,-1) \), the eigenvalues are \( 25 \) and \( 1 \), with eigenlines spanned by \( (1,1) \) and \( (1,-1) \). Both are positive, so \( \A \succ 0 \). The orthogonal projections onto the two eigenlines are
\[
\P_1 = \tfrac12\begin{pmatrix} 1 & 1 \\ 1 & 1\end{pmatrix},
\qquad
\P_2 = \tfrac12\begin{pmatrix} 1 & -1 \\ -1 & 1\end{pmatrix},
\]
so \( \A = 25\P_1 + \P_2 \) and
\[
\A^{1/2} = 5\P_1 + 1\cdot\P_2 = \begin{pmatrix} 3 & 2 \\ 2 & 3\end{pmatrix} .
\]
By the polynomial route: we need \( p \) with \( p(25) = 5 \) and \( p(1) = 1 \). The line through the two points is \( p(x) = \tfrac16 x + \tfrac56 \), and
\[
\tfrac16\A + \tfrac56\I = \tfrac16\begin{pmatrix} 18 & 12 \\ 12 & 18\end{pmatrix} = \begin{pmatrix} 3 & 2 \\ 2 & 3\end{pmatrix} .
\]
Check: \( \begin{pmatrix} 3 & 2 \\ 2 & 3\end{pmatrix}^2 = \begin{pmatrix} 13 & 12 \\ 12 & 13\end{pmatrix} \).

(b) Here \( \B = \I + \J \) with \( \J \) the all-ones matrix. Since \( \J\1 = 3\1 \) and \( \J\x = \0 \) for every \( \x \) with entries summing to \( 0 \), the eigenvalues of \( \J \) are \( 3 \) and \( 0 \), so those of \( \B \) are \( 4 \) and \( 1 \); both are positive, so \( \B \succ 0 \). We need \( p \) with \( p(4) = 2 \) and \( p(1) = 1 \), namely \( p(x) = \tfrac13x + \tfrac23 \), giving
\[
\B^{1/2} = \tfrac13\B + \tfrac23\I = \tfrac13\begin{pmatrix} 4 & 1 & 1 \\ 1 & 4 & 1 \\ 1 & 1 & 4\end{pmatrix} .
\]
Check by squaring: the diagonal entry of the square is \( \tfrac19(16 + 1 + 1) = 2 \) and an off-diagonal entry is \( \tfrac19(4 + 4 + 1) = 1 \), which reproduces \( \B \). Only two distinct eigenvalues appear, so a polynomial of degree \( 1 \) suffices even though \( \B \) is \( 3 \times 3 \).
:::

::: {.warning}
**\( \A^{1/2} \) is not the entrywise square root, and it is not the only square root.** For \( \A = \begin{pmatrix} 13 & 12 \\ 12 & 13\end{pmatrix} \) the entrywise roots \( \begin{pmatrix} \sqrt{13} & \sqrt{12} \\ \sqrt{12} & \sqrt{13}\end{pmatrix} \) form a matrix whose square is not \( \A \). And \( \A \) has other square roots: \( -\A^{1/2} \) is one, and \( 5\P_1 - \P_2 = \begin{pmatrix} 2 & 3 \\ 3 & 2\end{pmatrix} \) is another symmetric one. The word **positive** in "positive square root" is what makes the object unique; drop it and this \( \A \), whose two eigenvalues are distinct and positive, has four symmetric square roots, one for each choice of sign on each eigenline. When an eigenvalue repeats there are infinitely many, symmetric ones included: every reflection \( \begin{psmallmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta\end{psmallmatrix} \) is a symmetric square root of \( \I_2 \).
:::

::: {.check}
Let \( \A \succeq 0 \) and let \( \U \) be unitary. What is \( (\U^{*}\A\U)^{1/2} \)?
:::

::: {.solution}
\( \U^{*}\A^{1/2}\U \). It is positive semidefinite by @prp-congruence-positivity (a), since \( \A^{1/2} \succeq 0 \), and its square is \( \U^{*}\A^{1/2}\U\U^{*}\A^{1/2}\U = \U^{*}\A\U \) because \( \U\U^{*} = \I \). Uniqueness in @thm-psd-square-root does the rest. In words: the square root does not care which orthonormal coordinates we use, which is exactly what one wants of an operation defined on the spectrum.
:::

## The absolute value of a matrix

A complex number has a modulus \( \lvert z\rvert = \sqrt{\conj{z}z} \), and the polar form \( z = e^{i\theta}\lvert z\rvert \) splits it into a rotation and a non-negative stretch. Section 9 will split a matrix the same way, and the stretching factor it needs is built now. For **any** matrix, square or not, \( \A^{*}\A \) is positive semidefinite (@thm-invertible-tfae-positive), so it has a square root.

::: {#def-matrix-absolute-value}
[Absolute Value of a Matrix]

Let \( \A \in M_{m \times n}(F) \). The **absolute value** of \( \A \) is
\[
\lvert\A\rvert \coloneqq (\A^{*}\A)^{1/2} \in M_n(F) ,
\]
the unique positive semidefinite square root of \( \A^{*}\A \).
:::

Note the size: \( \lvert\A\rvert \) is \( n \times n \), not \( m \times n \), because \( \A^{*}\A \) acts on the domain of \( \A \). It is well defined because \( \A^{*}\A \succeq 0 \) and @thm-psd-square-root gives exactly one root.

::: {#prp-absolute-value-properties}
[What the absolute value preserves]

Let \( \A \in M_{m\times n}(F) \). Then for every \( \x \in F^n \),
\[
\norm{\lvert\A\rvert\x} = \norm{\A\x} .
\]
Consequently \( \nul\lvert\A\rvert = \nul \A \) and \( \rank\lvert\A\rvert = \rank \A \).
:::

::: {.proof}
Since \( \lvert\A\rvert \) is Hermitian and \( \lvert\A\rvert^2 = \A^{*}\A \),
\[
\norm{\lvert\A\rvert\x}^2 = \inner{\lvert\A\rvert^2\x}{\x} = \inner{\A^{*}\A\x}{\x} = \norm{\A\x}^2 ,
\]
using @lem-conjugate-transpose-pairing twice. Both sides are non-negative reals, so the norms agree. Hence \( \lvert\A\rvert\x = \0 \) if and only if \( \A\x = \0 \), and the rank statement follows by @thm-rank-nullity-matrix.
:::

So \( \lvert\A\rvert \) does exactly what \( \A \) does to lengths, and nothing else. That single identity is the whole engine of the polar decomposition: the map \( \lvert\A\rvert\x \mapsto \A\x \) preserves norms, so it extends to a unitary matrix, and \( \A = \W\lvert\A\rvert \) follows.

::: {#exm-absolute-value-two}
[Two Absolute Values]

Compute \( \lvert\A\rvert \) for \( \A = \begin{pmatrix} 0 & -1 \\ 1 & 0\end{pmatrix} \) and for \( \B = \begin{pmatrix} 3 & 0 \\ 4 & 0\end{pmatrix} \), both over \( \nR \).
:::

::: {.solution}
For the quarter turn, \( \A\tp\A = \I \), so \( \lvert\A\rvert = \I^{1/2} = \I \). This is right: a rotation changes no length, so the matrix that does the same thing to lengths and nothing else is the identity.

For \( \B \), \( \B\tp\B = \begin{pmatrix} 25 & 0 \\ 0 & 0\end{pmatrix} \), whose positive square root is \( \lvert\B\rvert = \begin{pmatrix} 5 & 0 \\ 0 & 0\end{pmatrix} \). Check @prp-absolute-value-properties: \( \norm{\B\x} = \norm{(3x_1, 4x_1)} = 5\lvert x_1\rvert = \norm{\lvert\B\rvert\x} \). Both have rank \( 1 \) and null space \( \Span(\e_2) \).
:::

::: {.warning}
**\( \lvert\A\rvert \) is not the entrywise absolute value, and \( \lvert\A\B\rvert \ne \lvert\A\rvert\lvert\B\rvert \).** For the quarter turn above, the entrywise absolute value is \( \begin{pmatrix} 0 & 1 \\ 1 & 0\end{pmatrix} \), while \( \lvert\A\rvert = \I \). For the product rule, take
\[
\A = \begin{pmatrix} 1 & 0 \\ 0 & 0\end{pmatrix}, \qquad \B = \begin{pmatrix} 0 & 0 \\ 1 & 1\end{pmatrix} .
\]
Then \( \A\B = 0 \), so \( \lvert\A\B\rvert = 0 \), while \( \lvert\A\rvert = \A \) and \( \lvert\B\rvert = \tfrac1{\sqrt2}\begin{pmatrix} 1 & 1 \\ 1 & 1\end{pmatrix} \), giving
\[
\lvert\A\rvert\lvert\B\rvert = \tfrac1{\sqrt2}\begin{pmatrix} 1 & 1 \\ 0 & 0\end{pmatrix} \ne 0 .
\]
That product is not even Hermitian, so it could not be the absolute value of anything. The modulus of a product of **numbers** is the product of the moduli because numbers commute; matrices do not.
:::

## Cholesky: elimination on a positive definite matrix

Chapter 2 ran elimination on a symmetric matrix and found that the two triangular factors are secretly the same one: \( \A = \L\D\L\tp \) (@thm-ldlt). It then observed that when every entry of \( \D \) is positive one can split \( \D = \D^{1/2}\D^{1/2} \) and write \( \A = (\L\D^{1/2})(\L\D^{1/2})\tp \), called this the **Cholesky factorization**, and promised that Chapter 12 would connect it with positive definite matrices. Here is the connection, and it is the best kind: the hypothesis "every entry of \( \D \) is positive" is not an extra assumption at all. It holds exactly when \( \A \) is positive definite, and it can be checked while the elimination runs.

::: {#thm-cholesky}
[Cholesky Factorization]

Let \( \A \in M_n(F) \) be Hermitian. Then \( \A \succ 0 \) if and only if
\[
\A = \L\L^{*}
\]
for some lower triangular \( \L \in M_n(F) \) whose diagonal entries are **real and strictly positive**. In that case \( \L \) is unique.
:::

::: {.idea}
\( (\Leftarrow) \) is one line: such an \( \L \) is invertible, and \( \L\L^{*} = (\L^{*})^{*}\L^{*} \) is @thm-pd-characterizations (c) with \( \B = \L^{*} \).

\( (\Rightarrow) \) is Chapter 2's construction with its hypothesis supplied. Sylvester's criterion makes every leading corner invertible, which is exactly what elimination without row swaps needs; the \( \L\D\L^{*} \) factorization then appears, and the pivots are the ratios \( \det\A_k/\det\A_{k-1} \), hence positive. Absorbing \( \D^{1/2} \) into \( \L \) finishes it. For uniqueness, strip the positive diagonal off each candidate \( \L \); what is left is an LU factorization of \( \A \), and Chapter 2 already proved those unique.
:::

::: {.proof}
\( (\Leftarrow) \) Suppose \( \A = \L\L^{*} \) with \( \L \) lower triangular and every \( \ell_{kk} > 0 \). Then \( \L \) is invertible by @lem-triangular-invertible, hence so is \( \L^{*} \), and \( \A = (\L^{*})^{*}\L^{*} \) is positive definite by @thm-pd-characterizations ((c) \( \Rightarrow \) (a)).

\( (\Rightarrow) \) Suppose \( \A \succ 0 \). By Sylvester's criterion (@thm-pd-characterizations (d)), \( \det \A_k > 0 \) for every \( k \), so every leading principal submatrix \( \A_k \) is invertible (@thm-invertible-tfae-det). By @exr-lu-factorization-c1 (c) there is an LU factorization \( \A = \M\U \) with \( \M \) unit lower triangular and \( \U \) upper triangular and invertible. Let \( \D = \diag(u_{11}, \dots, u_{nn}) \), which is invertible by @lem-triangular-invertible.

::: {.claim}
\( \A = \M\D\M^{*} \), and the entries \( u_{11}, \dots, u_{nn} \) of \( \D \) are real.
:::

::: {.proof}
Let \( \V = \D^{-1}\U \), which is unit upper triangular, so that \( \A = \M\D\V \). Since \( \A^{*} = \A \),
\[
\A = \A^{*} = (\M\D\V)^{*} = \V^{*}\D^{*}\M^{*} = \V^{*}\,(\D^{*}\M^{*}) .
\]
Here \( \V^{*} \) is unit lower triangular and \( \D^{*}\M^{*} \) is upper triangular with diagonal \( \conj{u_{11}}, \dots, \conj{u_{nn}} \), so this is a second LU factorization of the invertible matrix \( \A \). By @thm-lu-unique, \( \V^{*} = \M \) and \( \D^{*}\M^{*} = \U = \D\V = \D\M^{*} \). Canceling the invertible \( \M^{*} \) gives \( \D^{*} = \D \), that is, every \( u_{kk} \) is real; and \( \A = \M\D\V = \M\D\M^{*} \).
:::

Over \( \nR \) the claim is @thm-ldlt, and the proof just given is that proof with \( {}^{*} \) in place of \( \tp \).

Write \( d_k = u_{kk} \). Leading principal submatrices of a product of a lower and an upper triangular matrix multiply (@exr-lu-factorization-c1 (a)); applying that twice, first to \( \A = \M(\D\M^{*}) \) and then to \( \D\M^{*} \), gives \( \A_k = \M_k\D_k(\M^{*})_k = \M_k\D_k\M_k^{*} \) for every \( k \). Taking determinants with @thm-det-multiplicative and @thm-det-triangular,
\[
\det \A_k = 1 \cdot (d_1\cdots d_k) \cdot 1 = d_1\cdots d_k .
\]
Hence \( d_1 = \det \A_1 > 0 \) and, for \( k \ge 2 \), \( d_k = \det \A_k/\det \A_{k-1} > 0 \). So \( \D^{1/2} \coloneqq \diag(\sqrt{d_1}, \dots, \sqrt{d_n}) \) is a real matrix, and putting
\[
\L = \M\D^{1/2}
\]
gives a lower triangular matrix — its \( (i, j) \)-entry is \( m_{ij}\sqrt{d_j} \), which vanishes for \( i < j \) — whose \( k \)-th diagonal entry is \( \sqrt{d_k} > 0 \), and
\[
\L\L^{*} = \M\D^{1/2}(\D^{1/2})^{*}\M^{*} = \M\D\M^{*} = \A .
\]

*Uniqueness.* Suppose \( \A = \L_1\L_1^{*} = \L_2\L_2^{*} \), with each \( \L_i \) lower triangular with positive diagonal entries. Split off the diagonal: write \( \vDelta_i = \diag((\L_i)_{11}, \dots, (\L_i)_{nn}) \), a real diagonal matrix with positive entries, and \( \M_i = \L_i\vDelta_i^{-1} \), which is lower triangular with every diagonal entry \( 1 \). Then \( \L_i = \M_i\vDelta_i \) and
\[
\A = \M_i\vDelta_i^2\M_i^{*} = \M_i\bigl(\vDelta_i^2\M_i^{*}\bigr) .
\]
The second factor is upper triangular, its \( (k, l) \)-entry being \( (\vDelta_i^2)_{kk}\conj{(\M_i)_{lk}} \), which vanishes for \( k > l \). So for \( i = 1 \) and \( i = 2 \) this displays an LU factorization of \( \A \), which is invertible: \( \L_1 \) is triangular with non-zero diagonal, hence invertible by @lem-triangular-invertible, and \( \A = \L_1\L_1^{*} \) is a product of two invertible matrices. By @thm-lu-unique the two agree:
\[
\M_1 = \M_2 \qquad\text{and}\qquad \vDelta_1^2\M_1^{*} = \vDelta_2^2\M_2^{*} .
\]
Canceling the invertible \( \M_1^{*} = \M_2^{*} \) gives \( \vDelta_1^2 = \vDelta_2^2 \), and since both have positive diagonal entries, \( \vDelta_1 = \vDelta_2 \). Hence \( \L_1 = \M_1\vDelta_1 = \M_2\vDelta_2 = \L_2 \). This proves the theorem.
:::

Reading the equation \( \A = \L\L^{*} \) entry by entry turns it into a recipe, and the recipe is the standard way to factor by hand. Comparing the \( (j, j) \) entry of both sides gives \( a_{jj} = \sum_{k \le j}\lvert \ell_{jk}\rvert^2 \), and comparing the \( (i, j) \) entry for \( i > j \) gives \( a_{ij} = \sum_{k \le j}\ell_{ik}\conj{\ell_{jk}} \). Solving each for its one new unknown, column by column:
\[
\begin{aligned}
\ell_{jj} &= \Bigl(a_{jj} - \textstyle\sum_{k < j}\lvert \ell_{jk}\rvert^2\Bigr)^{1/2}, \\
\ell_{ij} &= \Bigl(a_{ij} - \textstyle\sum_{k < j}\ell_{ik}\conj{\ell_{jk}}\Bigr)\big/\ell_{jj} \qquad (i > j).
\end{aligned}
\]

::: {#exm-cholesky-by-hand}
[A Cholesky Factorization, and One That Fails]

Factor
\[
\A = \begin{pmatrix} 4 & -2 & 6 \\ -2 & 5 & -1 \\ 6 & -1 & 26 \end{pmatrix}
\]
as \( \L\L\tp \), and run the same algorithm on the matrix \( \A' \) obtained from \( \A \) by changing the \( (3,3) \) entry to \( 9 \).
:::

::: {.solution}
*Column 1.* \( \ell_{11} = \sqrt{4} = 2 \); then \( \ell_{21} = -2/2 = -1 \) and \( \ell_{31} = 6/2 = 3 \).

*Column 2.* \( \ell_{22} = \sqrt{5 - (-1)^2} = \sqrt4 = 2 \); then
\[
\ell_{32} = \frac{a_{32} - \ell_{31}\ell_{21}}{\ell_{22}} = \frac{-1 - 3(-1)}{2} = 1 .
\]

*Column 3.* \( \ell_{33} = \sqrt{26 - 3^2 - 1^2} = \sqrt{16} = 4 \). So
\[
\L = \begin{pmatrix} 2 & 0 & 0 \\ -1 & 2 & 0 \\ 3 & 1 & 4 \end{pmatrix},
\]
and multiplying back confirms \( \L\L\tp = \A \). The diagonal entries \( 2, 2, 4 \) are positive, so \( \A \succ 0 \) by @thm-cholesky; their squares \( 4, 4, 16 \) are the pivots \( d_k = \det\A_k/\det\A_{k-1} \), consistent with \( \det \A_1 = 4 \), \( \det\A_2 = 16 \), \( \det \A = 256 \).

*The failure.* For \( \A' \), columns \( 1 \) and \( 2 \) are unchanged, and the last step asks for
\[
\ell_{33} = \sqrt{9 - 3^2 - 1^2} = \sqrt{-1} ,
\]
which is not a positive real number. The algorithm stops, and by @thm-cholesky its stopping is a proof: \( \A' \) is not positive definite. Indeed \( \det \A' = -16 < 0 \), so Sylvester's criterion fails at \( k = 3 \).
:::

The example shows the practical point. **The algorithm is the test.** To decide whether a numerical Hermitian matrix is positive definite, one does not compute eigenvalues and one does not compute \( n \) determinants; one starts the Cholesky recursion and watches whether every quantity under a square root stays positive. Sylvester's criterion guarantees that this verdict is correct, because \( d_1\cdots d_k = \det \A_k \).

::: {.remark}
Two remarks on cost, both of which belong properly to Chapter 23. First, Cholesky does about half the arithmetic of a general LU factorization, because it computes only \( \L \) and never the second triangular factor. Second, and less obvious, it needs no pivoting: the recursion above never divides by something that positive definiteness allows to be zero, so the row swaps that Chapter 2 introduced for stability are simply not required here. Positive definiteness is the one structural hypothesis under which elimination is unconditionally safe.
:::

::: {.warning}
**Cholesky needs definiteness, not just semidefiniteness, for uniqueness.** The matrix \( \A = \begin{pmatrix} 0 & 0 \\ 0 & 1\end{pmatrix} \) is positive semidefinite and does factor as \( \L\L\tp \), for instance with \( \L = \A \). But the diagonal entry \( \ell_{11} = 0 \) is not positive, so @thm-cholesky does not apply — and indeed uniqueness fails, since \( \begin{pmatrix} 0 & 0 \\ 0 & 1\end{pmatrix} \) and \( \begin{pmatrix} 0 & 0 \\ 0 & -1\end{pmatrix} \) are two different lower triangular matrices \( \L \) with \( \L\L\tp = \A \). Also note that the \( \L \) of Cholesky is **not** the \( \L \) of Chapter 2's LU factorization: the latter is unit lower triangular, and the two differ by the factor \( \D^{1/2} \).
:::

::: {.check}
Let \( \A \succ 0 \) with Cholesky factor \( \L \). What is \( \det \A \) in terms of \( \L \), and what is the Cholesky factor of \( \A^{-1} \)?
:::

::: {.solution}
\( \det \A = \det\L\,\det\L^{*} = \lvert\ell_{11}\cdots\ell_{nn}\rvert^2 = (\ell_{11}\cdots\ell_{nn})^2 \), by @thm-det-multiplicative and @thm-det-triangular, the last step because the \( \ell_{kk} \) are positive reals. For the inverse, \( \A^{-1} = (\L\L^{*})^{-1} = (\L^{*})^{-1}\L^{-1} = \M\M^{*} \) with \( \M = (\L^{*})^{-1} \), which is **upper** triangular; so this is not itself a Cholesky factorization. The Cholesky factor of \( \A^{-1} \) is a different matrix, which is why solving \( \A\x = \b \) is done by two triangular substitutions with \( \L \) rather than by inverting anything.
:::

## Exercises

### A. Check your understanding

:::: {#exr-square-roots-and-cholesky-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State what \( \A^{1/2} \) is, including the two conditions that pin it down.
2. Define \( \lvert\A\rvert \) for \( \A \in M_{m \times n}(F) \) and say what size it is.
3. State the Cholesky factorization theorem.
4. True or false: every Hermitian matrix has exactly one Hermitian square root. Justify your answer.
5. Explain in one sentence why the Cholesky algorithm is a test for positive definiteness.
:::
::::

::: {.solution}
(a) For \( \A \succeq 0 \), \( \A^{1/2} \) is the unique matrix \( \C \) with \( \C \succeq 0 \) and \( \C^2 = \A \) (@thm-psd-square-root). Both conditions are needed: positivity, and squaring to \( \A \).

(b) \( \lvert\A\rvert = (\A^{*}\A)^{1/2} \), which is \( n \times n \), the size of the domain of \( \A \) (@def-matrix-absolute-value).

(c) A Hermitian \( \A \) is positive definite if and only if \( \A = \L\L^{*} \) with \( \L \) lower triangular with positive real diagonal entries, and then \( \L \) is unique (@thm-cholesky).

(d) False, twice over. A Hermitian matrix with a negative eigenvalue has no Hermitian square root at all, since \( \C^2 \succeq 0 \) always. And a positive semidefinite \( \A \) with two distinct eigenvalues has at least two Hermitian square roots, \( \pm\A^{1/2} \). Uniqueness needs the root itself to be positive semidefinite.

(e) Because the algorithm computes \( \ell_{jj}^2 = \det\A_j/\det\A_{j-1} \) one step at a time, so it produces a positive real \( \ell_{jj} \) at every step exactly when Sylvester's criterion holds.
:::

### B. Practice

:::: {#exr-square-roots-and-cholesky-b1}
[B1: Square roots]

Compute \( \A^{1/2} \) for each of the following, and in each case give a polynomial \( p \) with \( p(\A) = \A^{1/2} \).

::: {.enumerate options="label=(\alph*)"}
1. \( \A = \begin{pmatrix} 5 & 4 \\ 4 & 5\end{pmatrix} \).
2. \( \A = \begin{pmatrix} 10 & -6 \\ -6 & 10\end{pmatrix} \).
:::
::::

::: {.solution}
(a) \( \A(1,1) = (9,9) \) and \( \A(1,-1) = (1,-1) \), so the eigenvalues are \( 9 \) and \( 1 \) with eigenlines \( \Span((1,1)) \) and \( \Span((1,-1)) \); both positive, so \( \A \succ 0 \). With \( \P_1, \P_2 \) the projections onto those lines,
\[
\A^{1/2} = 3\P_1 + \P_2 = \begin{pmatrix} 2 & 1 \\ 1 & 2\end{pmatrix} .
\]
For the polynomial, solve \( p(9) = 3 \), \( p(1) = 1 \): \( p(x) = \tfrac14x + \tfrac34 \), and \( \tfrac14\A + \tfrac34\I = \begin{pmatrix} 2 & 1 \\ 1 & 2\end{pmatrix} \). Check: \( \begin{pmatrix} 2&1\\1&2\end{pmatrix}^2 = \begin{pmatrix} 5&4\\4&5\end{pmatrix} \).

(b) \( \A(1,-1) = (16,-16) \) and \( \A(1,1) = (4,4) \), so the eigenvalues are \( 16 \) and \( 4 \). Then
\[
\A^{1/2} = 4\cdot\tfrac12\begin{pmatrix} 1 & -1 \\ -1 & 1\end{pmatrix} + 2\cdot\tfrac12\begin{pmatrix} 1 & 1 \\ 1 & 1\end{pmatrix} = \begin{pmatrix} 3 & -1 \\ -1 & 3\end{pmatrix} .
\]
For the polynomial, \( p(16) = 4 \) and \( p(4) = 2 \) give \( p(x) = \tfrac16x + \tfrac43 \), and \( \tfrac16\A + \tfrac43\I = \begin{pmatrix} 3 & -1 \\ -1 & 3\end{pmatrix} \). Check: \( \begin{pmatrix} 3&-1\\-1&3\end{pmatrix}^2 = \begin{pmatrix} 10&-6\\-6&10\end{pmatrix} \).
:::

:::: {#exr-square-roots-and-cholesky-b2}
[B2: Cholesky, and a planted failure]

::: {.enumerate options="label=(\alph*)"}
1. Find the Cholesky factor of \( \A = \begin{pmatrix} 1 & 2 & -1 \\ 2 & 5 & 1 \\ -1 & 1 & 14\end{pmatrix} \), and hence write down \( \det \A \).
2. Run the same algorithm on \( \A' = \begin{pmatrix} 1 & 2 & -1 \\ 2 & 5 & 1 \\ -1 & 1 & 9\end{pmatrix} \) and say what the outcome proves.
:::
::::

::: {.solution}
(a) \( \ell_{11} = \sqrt1 = 1 \), \( \ell_{21} = 2 \), \( \ell_{31} = -1 \). Then \( \ell_{22} = \sqrt{5 - 4} = 1 \) and
\[
\ell_{32} = \frac{1 - (-1)(2)}{1} = 3 .
\]
Finally \( \ell_{33} = \sqrt{14 - 1 - 9} = \sqrt4 = 2 \). So
\[
\L = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ -1 & 3 & 2\end{pmatrix},
\]
and \( \L\L\tp = \A \). All diagonal entries are positive, so \( \A \succ 0 \). By the Quick check above, \( \det \A = (1\cdot 1\cdot 2)^2 = 4 \).

(b) Columns \( 1 \) and \( 2 \) are identical, and the last step asks for \( \ell_{33} = \sqrt{9 - 1 - 9} = \sqrt{-1} \). The algorithm fails, so \( \A' \) is not positive definite (@thm-cholesky). Confirming by Sylvester: \( \det \A'_1 = 1 \), \( \det \A'_2 = 1 \), and \( \det \A' = 1\cdot 44 - 2\cdot 19 - 7 = -1 < 0 \).
:::

:::: {#exr-square-roots-and-cholesky-b3}
[B3: An absolute value]

Let \( \A = \begin{pmatrix} 1 & 1 \\ 1 & 1\end{pmatrix} \in M_2(\nR) \). Compute \( \lvert\A\rvert \), verify \( \norm{\lvert\A\rvert\x} = \norm{\A\x} \) directly, and determine whether \( \lvert\A\rvert = \A \).
::::

::: {.solution}
\( \A\tp\A = \begin{pmatrix} 2 & 2 \\ 2 & 2\end{pmatrix} \), whose eigenvalues are \( 4 \) and \( 0 \) with eigenlines \( \Span((1,1)) \) and \( \Span((1,-1)) \). Hence
\[
\lvert\A\rvert = 2\cdot\tfrac12\begin{pmatrix} 1 & 1 \\ 1 & 1\end{pmatrix} + 0 = \begin{pmatrix} 1 & 1 \\ 1 & 1\end{pmatrix} = \A .
\]
Directly: \( \A\x = (x_1 + x_2)(1,1) \), so \( \norm{\A\x} = \sqrt2\,\lvert x_1 + x_2\rvert \), and the same computation applies to \( \lvert\A\rvert = \A \). The equality \( \lvert\A\rvert = \A \) is no accident: \( \A \succeq 0 \) here, and for a positive semidefinite \( \A \) one has \( \A^{*}\A = \A^2 \), so \( \lvert\A\rvert = (\A^2)^{1/2} = \A \) by uniqueness in @thm-psd-square-root.
:::

### C. Going deeper

:::: {#exr-square-roots-and-cholesky-c1}
[C1: The trace of a product of positive matrices]

Let \( \A, \B \in M_n(F) \) with \( \A \succeq 0 \) and \( \B \succeq 0 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \tr(\A\B) = \tr(\A^{1/2}\B\A^{1/2}) \), and deduce that \( \tr(\A\B) \ge 0 \).
2. Prove that \( \tr(\A\B) = 0 \) if and only if \( \A\B = 0 \).
:::

*Hint for (b): a positive semidefinite matrix of trace \( 0 \) is \( 0 \).*
::::

::: {.solution}
(a) By @thm-trace-properties, \( \tr(\X\Y) = \tr(\Y\X) \). With \( \X = \A^{1/2} \) and \( \Y = \A^{1/2}\B \),
\[
\tr(\A\B) = \tr(\A^{1/2}\A^{1/2}\B) = \tr(\A^{1/2}\B\A^{1/2}) .
\]
Now \( \A^{1/2}\B\A^{1/2} = (\A^{1/2})^{*}\B\A^{1/2} \succeq 0 \) by @prp-congruence-positivity (a), since \( \A^{1/2} \) is Hermitian. The trace of a positive semidefinite matrix is \( \ge 0 \) by @exr-positive-definite-matrices-c1 (a). Hence \( \tr(\A\B) \ge 0 \).

(b) \( (\Leftarrow) \) is clear. \( (\Rightarrow) \) Suppose \( \tr(\A\B) = 0 \). By (a), \( \C \coloneqq \A^{1/2}\B\A^{1/2} \succeq 0 \) and \( \tr \C = 0 \), so \( \C = 0 \) by @exr-positive-definite-matrices-c1 (b). Put \( \M = \B^{1/2}\A^{1/2} \). Then
\[
\M^{*}\M = \A^{1/2}\B^{1/2}\B^{1/2}\A^{1/2} = \A^{1/2}\B\A^{1/2} = \C = 0 ,
\]
so \( \M = 0 \) by @lem-kernel-normal-equations (its null space is all of \( F^n \), hence so is \( \nul \M \)). Therefore
\[
\A\B = \A^{1/2}(\A^{1/2}\B^{1/2})\B^{1/2} = \A^{1/2}\M^{*}\B^{1/2} = 0 .
\]
:::

:::: {#exr-square-roots-and-cholesky-c2}
[C2: Commuting positive matrices]

Let \( \A \in M_n(F) \) with \( \A \succeq 0 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove **without** using @thm-psd-square-root (a) that if \( \B\A = \A\B \), then \( \B\A^{1/2} = \A^{1/2}\B \). *Hint: show that \( \B \) maps each eigenspace of \( \A \) into itself.*
2. Let \( \B \succeq 0 \) with \( \A\B = \B\A \). Prove that \( \A\B \succeq 0 \) and that \( (\A\B)^{1/2} = \A^{1/2}\B^{1/2} \).
:::
::::

::: {.solution}
(a) Let \( \lambda \in \spec(\A) \) and \( \A\v = \lambda\v \). Then \( \A(\B\v) = \B(\A\v) = \lambda\B\v \), so \( \B \) maps \( E_\lambda(\A) \) into itself. Since \( \A \succeq 0 \), its distinct eigenvalues \( \lambda_1, \dots, \lambda_k \) are non-negative reals, and \( \A^{1/2} = \sum_i\sqrt{\lambda_i}\,\P_i \) with \( \P_i \) the orthogonal projection onto \( E_{\lambda_i}(\A) \) (proof of @thm-psd-square-root). For \( \v \in E_{\lambda_j}(\A) \) we have \( \P_i\v = \0 \) for \( i \ne j \) and \( \P_j\v = \v \), so \( \A^{1/2}\v = \sqrt{\lambda_j}\,\v \). Now \( F^n = E_{\lambda_1}(\A) \oplus \dots \oplus E_{\lambda_k}(\A) \) (@thm-spectral-resolution), so it suffices to check \( \B\A^{1/2}\v = \A^{1/2}\B\v \) for \( \v \in E_{\lambda_j}(\A) \). The left side is \( \sqrt{\lambda_j}\,\B\v \); the right side is \( \A^{1/2}(\B\v) = \sqrt{\lambda_j}\,\B\v \) as well, because \( \B\v \in E_{\lambda_j}(\A) \) by the first sentence. Hence \( \B\A^{1/2} = \A^{1/2}\B \).

(b) By (a), \( \A^{1/2} \) commutes with \( \B \). Applying (a) once more, this time to \( \B \succeq 0 \) with the commuting matrix \( \A^{1/2} \), gives that \( \A^{1/2} \) commutes with \( \B^{1/2} \). Put \( \C = \A^{1/2}\B^{1/2} \). Then
\[
\C^{*} = (\B^{1/2})^{*}(\A^{1/2})^{*} = \B^{1/2}\A^{1/2} = \C ,
\]
so \( \C \) is Hermitian, and \( \C^2 = \A^{1/2}\B^{1/2}\A^{1/2}\B^{1/2} = \A\B \) after one commutation. It remains to see \( \C \succeq 0 \). The matrices \( \A^{1/2} \) and \( \B^{1/2} \) are commuting Hermitian matrices, so by @cor-simultaneous-unitary-matrix (over \( \nC \)) or @cor-simultaneous-orthogonal-real (over \( \nR \)) there is a unitary \( \U \) with \( \U^{*}\A^{1/2}\U = \diag(\alpha_i) \) and \( \U^{*}\B^{1/2}\U = \diag(\beta_i) \), all \( \alpha_i, \beta_i \ge 0 \). Then \( \U^{*}\C\U = \diag(\alpha_i\beta_i) \succeq 0 \), so \( \C \succeq 0 \) by @prp-congruence-positivity (a). Hence \( \A\B = \C^2 \succeq 0 \) and, by uniqueness in @thm-psd-square-root, \( (\A\B)^{1/2} = \C = \A^{1/2}\B^{1/2} \).
:::

:::: {#exr-square-roots-and-cholesky-c3}
[C3: Why definiteness is needed]

::: {.enumerate options="label=(\alph*)"}
1. Give a positive semidefinite \( \A \in M_2(\nR) \), not positive definite, together with two different lower triangular \( \L \) satisfying \( \A = \L\L\tp \). Which hypothesis of @thm-cholesky fails?
2. Prove that if \( \A \succeq 0 \) then \( \A + t\I \succ 0 \) for every real \( t > 0 \), and hence that every positive semidefinite matrix is a limit of positive definite ones in the entrywise sense.
:::
::::

::: {.solution}
(a) Take \( \A = \diag(0, 1) \). Then \( \L_1 = \diag(0, 1) \) and \( \L_2 = \diag(0, -1) \) are both lower triangular with \( \L_i\L_i\tp = \A \). The hypothesis that fails is that the diagonal entries of \( \L \) be strictly positive: \( \ell_{11} = 0 \) here, which is exactly the first pivot vanishing. Uniqueness in @thm-cholesky is not available without it.

(b) \( \A + t\I \) is Hermitian, and for \( \x \ne \0 \),
\[
\inner{(\A + t\I)\x}{\x} = \inner{\A\x}{\x} + t\norm{\x}^2 \ge t\norm{\x}^2 > 0 ,
\]
so \( \A + t\I \succ 0 \). Each entry of \( \A + t\I \) differs from the corresponding entry of \( \A \) by \( t \) or by \( 0 \), so letting \( t \) decrease to \( 0 \) recovers \( \A \) entry by entry. This is the standard device for extending a statement from positive definite to positive semidefinite matrices whenever the statement survives taking limits; @thm-psd-characterizations already used it in the form \( \det(\A + t\I) > 0 \).
:::
