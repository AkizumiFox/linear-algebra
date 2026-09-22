# The Sylvester Equation Revisited

Chapter 11 settled when the equation \( \A\X - \X\B = \C \) can be solved: over \( \nC \) it has exactly one solution for every \( \C \) if and only if \( \A \) and \( \B \) have no common eigenvalue (@thm-sylvester-equation). It then set a question aside. "The quantitative version — *how badly* conditioned the equation is when the spectra are close but disjoint — is a separate matter, and belongs with perturbation theory in Chapter 19." Chapter 7, which first wrote the equation as a linear system, said the same thing more briefly: "its quantitative form appears in Chapter 19." This section pays both debts. It attaches to each pair \( (\A, \B) \) a number that says how large a solution can be, computes it exactly for normal pairs, shows how badly it can behave otherwise, and proves a bound in the spectral norm for Hermitian pairs whose spectra sit on opposite sides of a gap.

The reason to want these bounds now is that Sections 9 and 10 need them. In Section 9 the error in a computed invariant subspace turns out to satisfy a Sylvester equation, and in Section 10 so does the error in a square root or a polar factor. Each of those three errors is measured by one of the bounds proved here, applied once.

**Throughout**, the field is \( \nC \), \( \A \in M_m(\nC) \) and \( \B \in M_n(\nC) \), and \( \X, \C \in M_{m \times n}(\nC) \). We write \( \cS = \cS_{\A,\B} \) for the Sylvester operator \( \X \mapsto \A\X - \X\B \) of @def-sylvester-operator, and \( \K = \I_n \otimes \A - \B\tp \otimes \I_m \) for its matrix, so that \( \vecop(\cS(\X)) = \K\vecop\X \) by @eq-sylvester-kronecker. The eigenvalues of \( \A \) are \( \lambda_1, \dots, \lambda_m \) and those of \( \B \) are \( \mu_1, \dots, \mu_n \), with multiplicity. Every bound names its norm: \( \norm{\cdot}_F \) is the Frobenius norm and \( \norm{\cdot}_2 \) the spectral norm.

## How large can the solution be?

Start with the smallest case, \( m = n = 1 \). The equation is \( (a - b)x = c \), and when \( a \ne b \) its solution is \( x = c/(a - b) \). So the size of the answer is governed by one number, the distance \( \lvert a - b\rvert \) between the two "spectra": the closer they are, the larger \( x \) can be for a given \( c \).

The natural guess for larger matrices is that the distance between the two spectra, \( \min_{i,j}\lvert\lambda_i - \mu_j\rvert \), plays the same role, so that \( \norm{\X}_F \le \norm{\C}_F / \min_{i,j}\lvert\lambda_i - \mu_j\rvert \). We will see that this guess is right for normal pairs and can be wrong by any factor otherwise. The number that really controls the solution is the smallest amount by which \( \cS \) can stretch a matrix, and it deserves a name.

*The separation of \( \A \) and \( \B \) is the least that the Sylvester operator can shrink a matrix of unit size.*

::: {#def-sep}
[Separation]

Let \( \A \in M_m(\nC) \) and \( \B \in M_n(\nC) \). The **separation** of \( \A \) and \( \B \) is
\[
\begin{aligned}
\operatorname{sep}_F(\A, \B) \coloneqq \min\bigl\{ &\norm{\A\X - \X\B}_F : \\
&\X \in M_{m \times n}(\nC),\ \norm{\X}_F = 1 \bigr\} .
\end{aligned}
\]
:::

In words: we run over **every** matrix \( \X \) of the right shape whose Frobenius norm is exactly \( 1 \), apply the Sylvester operator, measure the result in the Frobenius norm, and take the **smallest** value. By homogeneity, \( \norm{\A\X - \X\B}_F \ge \operatorname{sep}_F(\A, \B)\norm{\X}_F \) for **every** \( \X \), and \( \operatorname{sep}_F(\A, \B) \) is the largest constant with this property. The order matters: \( \operatorname{sep}_F(\A, \B) \) belongs to \( \X \mapsto \A\X - \X\B \), and \( \operatorname{sep}_F(\B, \A) \) to a different operator on a different space. The subscript \( F \) records the norm, as in \( \norm{\cdot}_F \).

**Well-definedness.** A minimum over an infinite set needs to exist, and the first part of @prp-sep-properties below shows that it does, without any appeal to compactness: it is the smallest singular value of \( \K \).

**Examples.**

1. **\( m = n = 1 \).** Then \( \X = (x) \) with \( \lvert x\rvert = 1 \), and \( \lvert ax - xb\rvert = \lvert a - b\rvert \). So \( \operatorname{sep}_F(a, b) = \lvert a - b\rvert \), the one-dimensional picture above.
2. **Equal matrices.** For square \( \A \), \( \operatorname{sep}_F(\A, \A) = 0 \): the matrix \( \X = \I_m/\sqrt{m} \) has \( \norm{\X}_F = 1 \) and \( \A\X - \X\A = \0 \). This degenerate case matters because it is the extreme of a shared eigenvalue, and the first property below says that any shared eigenvalue forces the separation to \( 0 \).
3. **Diagonal matrices.** If \( \A = \diag(\lambda_1, \dots, \lambda_m) \) and \( \B = \diag(\mu_1, \dots, \mu_n) \), then \( (\A\X - \X\B)_{ij} = (\lambda_i - \mu_j)x_{ij} \), so \( \cS \) multiplies each entry by its own factor. The smallest stretch is the smallest factor in modulus, and \( \operatorname{sep}_F(\A, \B) = \min_{i,j}\lvert\lambda_i - \mu_j\rvert \). The proof of @thm-sep-normal below writes this out.

**Non-example by minimal change.** Drop the normalization and take \( \min\{\norm{\A\X - \X\B}_F : \X \ne \0\} \) instead. The set of values is still non-empty and bounded below, but its infimum is \( 0 \) for every pair, and when the spectra are disjoint it is never attained: replacing \( \X \) by \( t\X \) multiplies the value by \( t \), and \( t \) can be as small as we like, while the value \( 0 \) is taken at some \( \X \ne \0 \) exactly when the two spectra meet (@thm-sylvester-equation), as they do in the second example above, where \( \A = \B \) and \( \X = \I_m \). It is exactly the clause \( \norm{\X}_F = 1 \) that fails, and it is what turns a meaningless infimum into a measurement of the operator.

**Why the Frobenius norm.** Vectorization lists the entries of \( \X \) in one column, so \( \norm{\vecop\X}_2 = \norm{\X}_F \): \( \vecop \) is an isometry from \( (M_{m \times n}(\nC), \norm{\cdot}_F) \) to \( (\nC^{mn}, \norm{\cdot}_2) \). That turns \( \operatorname{sep}_F \) into a question about the ordinary matrix \( \K \), which the singular value decomposition answers. With \( \norm{\cdot}_2 \) on both sides the minimum is also a sensible quantity, but it has no such formula, and we will not need it: the spectral-norm results below go through a different argument.

::: {.warning}
**The separation is not the distance between the spectra.** It is at most that distance, by part (c) of the proposition below, but it can be far smaller. For \( \A = \begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix} \) and the \( 1 \times 1 \) matrix \( \B = (0) \), the spectra \( \{1\} \) and \( \{0\} \) are at distance \( 1 \) for every \( t \), yet \( \operatorname{sep}_F(\A, \B) < 1/t \) for \( t > 0 \) (@exm-sep-far-below-gap). Whenever \( \A \) or \( \B \) is not normal, compute the separation; do not read it off the eigenvalues.
:::

Everything we need about the separation is collected in one proposition.

::: {#prp-sep-properties}
[Properties of the Separation]

Let \( \A \in M_m(\nC) \), \( \B \in M_n(\nC) \), and \( \K = \I_n \otimes \A - \B\tp \otimes \I_m \).

::: {.enumerate options="label=(\alph*)"}
1. The minimum defining \( \operatorname{sep}_F(\A, \B) \) exists, and \( \operatorname{sep}_F(\A, \B) = \sigma_{mn}(\K) \), the smallest singular value of \( \K \).
2. \( \operatorname{sep}_F(\A, \B) > 0 \) if and only if \( \spec(\A) \cap \spec(\B) = \varnothing \).
3. \( \operatorname{sep}_F(\A, \B) \le \min_{i,j}\lvert\lambda_i - \mu_j\rvert \).
4. If \( \spec(\A) \cap \spec(\B) = \varnothing \), then for every \( \C \) the unique solution of \( \A\X - \X\B = \C \) satisfies
   \[
   \norm{\X}_F \le \frac{\norm{\C}_F}{\operatorname{sep}_F(\A, \B)} ,
   \]
   and equality holds for some \( \C \ne \0 \).
5. For unitary \( \U \in \Unit(m) \) and \( \V \in \Unit(n) \), \( \operatorname{sep}_F(\U^{*}\A\U, \V^{*}\B\V) = \operatorname{sep}_F(\A, \B) \).
6. If \( n = 1 \) and \( \B = (\mu) \), then \( \operatorname{sep}_F(\A, \B) = \sigma_m(\A - \mu\I_m) \), the smallest singular value of \( \A - \mu\I_m \).
:::
:::

::: {.idea}
Part (a) is the isometry \( \vecop \) plus the fact that the smallest stretch of a square matrix is its smallest singular value. Part (b) is Sylvester's theorem, read through (a). Part (c) needs one good test matrix: an eigenvector of \( \A \) times a left eigenvector of \( \B \) is multiplied by \( \lambda - \mu \) under \( \cS \), exactly as in the \( 1 \times 1 \) case. Part (d) is the definition read backwards. Part (e) holds because unitary factors change neither the set of unit matrices nor the Frobenius norm. Part (f) is the case \( n = 1 \) of (a), where \( \K \) is nothing but \( \A - \mu\I_m \).
:::

::: {.proof}
(a) Let \( \X \in M_{m \times n}(\nC) \) and \( \x = \vecop\X \). The entries of \( \x \) are those of \( \X \), so \( \norm{\x}_2 = \norm{\X}_F \), and likewise \( \norm{\A\X - \X\B}_F = \norm{\K\x}_2 \) by @eq-sylvester-kronecker. Since \( \vecop \) is a bijection from \( M_{m \times n}(\nC) \) onto \( \nC^{mn} \) (@def-vec-operator), the set whose minimum defines \( \operatorname{sep}_F(\A, \B) \) equals \( \{\norm{\K\x}_2 : \norm{\x}_2 = 1\} \). By @lem-stretch-in-singular-coordinates (b) with \( k \) equal to the size \( mn \) of \( \K \), the head subspace is all of \( \nC^{mn} \), and the minimum of \( \norm{\K\x}/\norm{\x} \) over \( \x \ne \0 \) exists and equals \( \sigma_{mn}(\K) \). Restricting to unit vectors changes nothing, since the quotient is unchanged when \( \x \) is scaled.

(b) By @thm-svd, the number of non-zero singular values of \( \K \) is \( \rank\K \). Since \( \sigma_{mn}(\K) \) is the smallest, it is non-zero exactly when all \( mn \) of them are, that is, when \( \rank\K = mn \), which says that \( \K \) is invertible (@thm-invertible-tfae-det (d)). By @eq-sylvester-kronecker, \( \K \) is invertible exactly when \( \cS \) is, and by @thm-sylvester-equation ((a) \( \Leftrightarrow \) (b)) that happens exactly when \( \spec(\A) \cap \spec(\B) = \varnothing \). Combining with (a) proves (b).

(c) Fix \( i, j \). Choose an eigenvector \( \x \) of \( \A \) for \( \lambda_i \), and, by @prp-left-eigenvectors-transpose (b), a left eigenvector \( \y \) of \( \B \) for \( \mu_j \), so that \( \y\tp\B = \mu_j\y\tp \) (@def-left-eigenvector). Scale both to length \( 1 \), and put \( \X = \x\y\tp \). Its \( (p, q) \) entry is \( x_py_q \), so
\[
\norm{\X}_F^2 = \sum_{p,q}\lvert x_p\rvert^2\lvert y_q\rvert^2 = \norm{\x}^2\norm{\y}^2 = 1 .
\]
By associativity, \( \A\X - \X\B = (\A\x)\y\tp - \x(\y\tp\B) = (\lambda_i - \mu_j)\X \). Hence \( \operatorname{sep}_F(\A, \B) \le \norm{(\lambda_i - \mu_j)\X}_F = \lvert\lambda_i - \mu_j\rvert \). This holds for every pair \( (i, j) \), so it holds for the minimum.

(d) By @thm-sylvester-equation the solution \( \X \) exists and is unique. If \( \X = \0 \) there is nothing to prove. Otherwise \( \X/\norm{\X}_F \) has Frobenius norm \( 1 \), so by @def-sep
\[
\operatorname{sep}_F(\A, \B) \le \frac{\norm{\A\X - \X\B}_F}{\norm{\X}_F} = \frac{\norm{\C}_F}{\norm{\X}_F} ,
\]
and \( \operatorname{sep}_F(\A, \B) > 0 \) by (b), so we may rearrange. For equality, take \( \X_0 \) with \( \norm{\X_0}_F = 1 \) attaining the minimum, which exists by (a), and put \( \C = \A\X_0 - \X_0\B \). Then \( \C \ne \0 \), because \( \norm{\C}_F = \operatorname{sep}_F(\A, \B) > 0 \), and the unique solution is \( \X_0 \), for which the two sides are both \( 1 \).

(e) Put \( \A' = \U^{*}\A\U \) and \( \B' = \V^{*}\B\V \). For every \( \X \),
\[
\A'(\U^{*}\X\V) - (\U^{*}\X\V)\B' = \U^{*}(\A\X - \X\B)\V ,
\]
because \( \U\U^{*} = \I_m \) and \( \V\V^{*} = \I_n \). By @lem-frobenius-unitarily-invariant, \( \norm{\U^{*}\X\V}_F = \norm{\X}_F \) and the right side has Frobenius norm \( \norm{\A\X - \X\B}_F \). The map \( \X \mapsto \U^{*}\X\V \) is a bijection of \( M_{m \times n}(\nC) \), with inverse \( \Y \mapsto \U\Y\V^{*} \), so it carries the matrices of Frobenius norm \( 1 \) onto themselves. Hence the two minima are taken over the same set of values, and they are equal.

(f) With \( n = 1 \) and \( \B = (\mu) \), the Kronecker matrix is \( \K = \I_1 \otimes \A - (\mu) \otimes \I_m = \A - \mu\I_m \), of size \( mn = m \). So (a) gives \( \operatorname{sep}_F(\A, \B) = \sigma_m(\A - \mu\I_m) \).
:::

Part (d) is the quantitative form that Chapter 7 and Chapter 11 promised, and it says more than an inequality. The number \( 1/\operatorname{sep}_F(\A, \B) \) is **exactly** the largest factor by which solving the equation can magnify the data, measured in the Frobenius norm. Since \( \cS \) is linear, it is also the factor for errors: if \( \C \) is replaced by \( \C + \Delta\C \), the solution moves by \( \cS^{-1}(\Delta\C) \), whose norm is at most \( \norm{\Delta\C}_F/\operatorname{sep}_F(\A, \B) \), and some \( \Delta\C \) achieves this. A small separation is the precise meaning of "badly conditioned". Part (c) says that close spectra always make the separation small. The rest of the section asks whether the converse holds, that is, whether well-separated spectra make it large.

::: {.check}
Part (f) of @prp-sep-properties was read off the Kronecker matrix. Prove it instead straight from @def-sep, without vectorizing: for \( \B = (\mu) \), unwind what the matrices \( \X \) of Frobenius norm \( 1 \) are.
:::

::: {.solution}
Here \( n = 1 \), so \( \X = \x \) is a column in \( \nC^m \) with \( \norm{\x}_F = \norm{\x} \), and \( \A\x - \x\mu = (\A - \mu\I_m)\x \). So \( \operatorname{sep}_F(\A, \B) = \min_{\norm{\x} = 1}\norm{(\A - \mu\I_m)\x} \), which is \( \sigma_m(\A - \mu\I_m) \) by @lem-stretch-in-singular-coordinates (b) with \( k = m \).
:::

## Normal pairs: the separation is the gap

For normal matrices the naive guess is right, and the proof is the diagonal example written out.

::: {#thm-sep-normal}
[Separation of Normal Matrices]

Let \( \A \in M_m(\nC) \) and \( \B \in M_n(\nC) \) be **normal**, with eigenvalues \( \lambda_1, \dots, \lambda_m \) and \( \mu_1, \dots, \mu_n \). Then
\[
\operatorname{sep}_F(\A, \B) = \min_{i,j}\lvert\lambda_i - \mu_j\rvert .
\]
Consequently, if \( \delta = \min_{i,j}\lvert\lambda_i - \mu_j\rvert > 0 \), the unique solution of \( \A\X - \X\B = \C \) satisfies \( \norm{\X}_F \le \norm{\C}_F/\delta \).
:::

::: {.idea}
Unitary diagonalization costs nothing in the Frobenius norm, by @prp-sep-properties (e). Once both matrices are diagonal, the operator scales the \( (i, j) \) entry by \( \lambda_i - \mu_j \), so the total shrinkage is a weighted average of the \( \lvert\lambda_i - \mu_j\rvert^2 \), and a weighted average is at least the smallest weight.
:::

::: {.proof}
By @cor-spectral-complex-matrix there are unitary \( \U \in \Unit(m) \) and \( \V \in \Unit(n) \) with \( \U^{*}\A\U = \vLambda \coloneqq \diag(\lambda_1, \dots, \lambda_m) \) and \( \V^{*}\B\V = \M \coloneqq \diag(\mu_1, \dots, \mu_n) \). By @prp-sep-properties (e), \( \operatorname{sep}_F(\A, \B) = \operatorname{sep}_F(\vLambda, \M) \).

Let \( \X = (x_{ij}) \) have \( \norm{\X}_F = 1 \), and put \( \delta = \min_{i,j}\lvert\lambda_i - \mu_j\rvert \). The \( (i, j) \) entry of \( \vLambda\X - \X\M \) is \( \lambda_ix_{ij} - x_{ij}\mu_j = (\lambda_i - \mu_j)x_{ij} \), since multiplying by a diagonal matrix on the left scales rows and on the right scales columns. Hence
\[
\begin{aligned}
\norm{\vLambda\X - \X\M}_F^2 &= \sum_{i,j}\lvert\lambda_i - \mu_j\rvert^2\lvert x_{ij}\rvert^2 \\
&\ge \delta^2\sum_{i,j}\lvert x_{ij}\rvert^2 = \delta^2 .
\end{aligned}
\]
Therefore \( \operatorname{sep}_F(\vLambda, \M) \ge \delta \). The reverse inequality is @prp-sep-properties (c). This proves the equality, and the bound on \( \X \) is then @prp-sep-properties (d).
:::

The theorem answers the question of the opening completely in the normal case: there, how badly conditioned the equation is depends on the spectra and on nothing else. In particular it applies to Hermitian pairs, which is the case Section 9 needs.

::: {#exm-sep-normal-pair}
[A Normal Pair]

Let
\[
\A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}, \qquad \B = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} .
\]
Compute \( \operatorname{sep}_F(\A, \B) \) in two ways: from @thm-sep-normal, and from the singular values of \( \K \).
:::

::: {.solution}
The matrix \( \A \) is real symmetric, hence normal, with \( p_{\A}(x) = (x - 2)^2 - 1 = (x - 1)(x - 3) \), so its eigenvalues are \( 1, 3 \). The matrix \( \B \) is real with \( \B\tp\B = \I_2 = \B\B\tp \), hence normal, and \( p_{\B}(x) = x^2 + 1 \), so its eigenvalues are \( \pm i \). The four distances are
\[
\lvert 1 \mp i\rvert = \sqrt2, \qquad \lvert 3 \mp i\rvert = \sqrt{10} ,
\]
so @thm-sep-normal gives \( \operatorname{sep}_F(\A, \B) = \sqrt2 \).

For the second computation, \( \B\tp = \begin{psmallmatrix} 0 & 1 \\ -1 & 0 \end{psmallmatrix} \), and by @def-kronecker-product, in \( 2 \times 2 \) blocks,
\[
\K = \I_2 \otimes \A - \B\tp \otimes \I_2 = \begin{pmatrix} \A & -\I_2 \\ \I_2 & \A \end{pmatrix} .
\]
Since \( \K \) is real, \( \K^{*} = \K\tp \), so the singular values of \( \K \) are the non-negative square roots of the eigenvalues of \( \K\tp\K \) (@def-singular-values). Since \( \A \) is real symmetric, block multiplication (@thm-block-multiplication) gives
\[
\begin{aligned}
\K\tp\K &= \begin{pmatrix} \A & \I_2 \\ -\I_2 & \A \end{pmatrix}\begin{pmatrix} \A & -\I_2 \\ \I_2 & \A \end{pmatrix} \\
&= \begin{pmatrix} \A^2 + \I_2 & \0 \\ \0 & \A^2 + \I_2 \end{pmatrix} .
\end{aligned}
\]
The eigenvalues of \( \A^2 + \I_2 \) are \( 1^2 + 1 = 2 \) and \( 3^2 + 1 = 10 \) (@thm-spectral-mapping), so the singular values of \( \K \) are \( \sqrt{10}, \sqrt{10}, \sqrt2, \sqrt2 \). The smallest is \( \sqrt2 \), in agreement with @prp-sep-properties (a).
:::

## Non-normal pairs: the separation can collapse

For a non-normal pair the inequality of @prp-sep-properties (c) can be strict, and by as large a factor as we please. The smallest example uses a \( 1 \times 1 \) matrix \( \B \), so that @prp-sep-properties (f) computes the separation.

::: {#exm-sep-far-below-gap}
[Separation Far Below the Gap]

For a real number \( t \ge 0 \), let
\[
\A = \begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix}, \qquad \B = (0) .
\]
Compute \( \operatorname{sep}_F(\A, \B) \) and compare it with the distance between the spectra. Then, for \( t = 99/10 \), solve \( \A\X - \X\B = \C \) with \( \C = \e_2 \) and compare the size of the solution with the guess \( \norm{\C}_F/\min\lvert\lambda_i - \mu_j\rvert \).
:::

::: {.solution}
The spectra are \( \spec(\A) = \{1\} \) (triangular, @thm-diagonal-of-triangular-form) and \( \spec(\B) = \{0\} \), at distance \( 1 \) for every \( t \). By @prp-sep-properties (f) with \( \mu = 0 \), \( \operatorname{sep}_F(\A, \B) = \sigma_2(\A) \), the square root of the smaller eigenvalue of
\[
\A\tp\A = \begin{pmatrix} 1 & t \\ t & 1 + t^2 \end{pmatrix} .
\]
Its characteristic polynomial is \( (z - 1)(z - 1 - t^2) - t^2 = z^2 - (2 + t^2)z + 1 \). Both roots are positive and their product is \( 1 \), so the smaller is the reciprocal of the larger, \( \sigma_2(\A) = 1/\sigma_1(\A) \). Solving the quadratic,
\[
\sigma_2(\A)^2 = \frac{2 + t^2 - t\sqrt{t^2 + 4}}{2} = \Bigl(\frac{\sqrt{t^2 + 4} - t}{2}\Bigr)^2 ,
\]
as expanding the square confirms. Hence
\[
\operatorname{sep}_F(\A, \B) = \frac{\sqrt{t^2 + 4} - t}{2} = \frac{2}{\sqrt{t^2 + 4} + t} ,
\]
where the second form multiplies top and bottom by \( \sqrt{t^2 + 4} + t \). The second form is less than \( 2/(2t) = 1/t \) for \( t > 0 \), because \( \sqrt{t^2 + 4} > t \). The spectra stay at distance \( 1 \), and the separation tends to \( 0 \) as \( t \to \infty \).

For \( t = 99/10 \) we have \( t^2 + 4 = 10201/100 \), whose square root is \( 101/10 \), so
\[
\operatorname{sep}_F(\A, \B) = \frac{1}{2}\Bigl(\frac{101}{10} - \frac{99}{10}\Bigr) = \frac{1}{10} .
\]
The equation is \( \A\x = \e_2 \) for the column \( \x = \X \), so \( \x = \A^{-1}\e_2 = (-t, 1) \), since \( \A^{-1} = \begin{psmallmatrix} 1 & -t \\ 0 & 1 \end{psmallmatrix} \). Its length is \( \sqrt{t^2 + 1} = \sqrt{9901}/10 \approx 9.95 \). The guess from the eigenvalues was \( \norm{\C}_F/1 = 1 \), wrong by a factor of almost \( 10 \). The true bound \( \norm{\C}_F/\operatorname{sep}_F(\A, \B) = 10 \) from @prp-sep-properties (d) is almost attained, and it is attained when \( \C \) is a unit left singular vector of \( \A \) for \( \sigma_2 \).
:::

The example has a second reading. The eigenvalue \( 1 \) of \( \A \) is far from \( 0 \), yet a perturbation of \( \A \) of size \( \operatorname{sep}_F(\A, \B) = 1/10 \) in the spectral norm makes \( 0 \) an eigenvalue, because that is how far \( \A \) is from the singular matrices (@cor-distance-to-singular). Exercise C1 below shows that, for every pair, no perturbation of spectral norm less than \( \operatorname{sep}_F(\A, \B) \) can create a common eigenvalue, and that when \( \B \) is \( 1 \times 1 \) one of exactly that size can. For a non-normal pair, the distance between the spectra measures the wrong thing, and the separation measures the right one.

## A one-sided bound in the spectral norm

Section 9 will measure the angle between two invariant subspaces, and the largest such angle is a spectral norm, not a Frobenius norm. For Hermitian pairs, @thm-sep-normal already gives \( \norm{\X}_F \le \norm{\C}_F/\delta \). The spectral-norm analogue with the same constant is **false** in general: Exercise C2 below exhibits real diagonal \( \A \) and \( \B \) whose spectra interlace at distance \( 1 \), yet \( \norm{\X}_2 > \norm{\C}_2 \). What rescues the spectral norm is a stronger hypothesis on where the spectra lie: all of \( \spec(\A) \) on one side of a gap and all of \( \spec(\B) \) on the other.

::: {#thm-sylvester-one-sided}
[One-Sided Sylvester Bound]

Let \( \A \in M_m(\nC) \) and \( \B \in M_n(\nC) \) be Hermitian, and let \( \alpha > \beta \) be real numbers with
\[
\A \succeq \alpha\I_m, \qquad \B \preceq \beta\I_n .
\]
Then for every \( \C \in M_{m \times n}(\nC) \) the equation \( \A\X - \X\B = \C \) has exactly one solution, and it satisfies
\[
\norm{\X}_2 \le \frac{\norm{\C}_2}{\alpha - \beta}, \qquad \norm{\X}_F \le \frac{\norm{\C}_F}{\alpha - \beta} .
\]
:::

::: {.idea}
The **singular-pair trick.** A single pair of vectors sees the whole spectral norm of \( \X \): by the singular value decomposition there are unit vectors \( \u, \v \) with \( \X\v = s\u \) and \( \X^{*}\u = s\v \), where \( s = \norm{\X}_2 \). Sandwich the equation between them. The left side becomes \( \u^{*}\A\X\v - \u^{*}\X\B\v = s(\u^{*}\A\u - \v^{*}\B\v) \), a real number at least \( s(\alpha - \beta) \) because of the two one-sided hypotheses. The right side becomes \( \u^{*}\C\v \), which is at most \( \norm{\C}_2 \) in modulus. The one-sided hypotheses are used exactly once, to make both quadratic forms pull in the same direction.
:::

::: {.proof}
**Existence and uniqueness.** Let \( \lambda \in \spec(\A) \) with unit eigenvector \( \x \). Then \( \lambda = \inner{\A\x}{\x} \ge \alpha \), because \( \inner{(\A - \alpha\I_m)\x}{\x} \ge 0 \) by @def-positive-semidefinite and @def-loewner-order. Likewise every \( \mu \in \spec(\B) \) satisfies \( \mu \le \beta < \alpha \). So \( \spec(\A) \cap \spec(\B) = \varnothing \), and @thm-sylvester-equation gives exactly one solution \( \X \).

**The spectral norm.** Put \( s = \norm{\X}_2 \), which equals \( \sigma_1(\X) \) by @thm-operator-norm-formulas (c). If \( s = 0 \) there is nothing to prove. Otherwise \( \X \) has rank at least \( 1 \), and @thm-svd with @eq-singular-vector-pairing (for \( i = 1 \)) gives unit vectors \( \u \in \nC^m \) and \( \v \in \nC^n \) with
\[
\X\v = s\u, \qquad \X^{*}\u = s\v .
\]{#eq-singular-pair}
Taking adjoints in the second, \( \u^{*}\X = s\v^{*} \). Multiply \( \A\X - \X\B = \C \) by \( \u^{*} \) on the left and \( \v \) on the right:
\[
\begin{aligned}
\u^{*}\C\v &= \u^{*}\A(\X\v) - (\u^{*}\X)\B\v \\
&= s\,\u^{*}\A\u - s\,\v^{*}\B\v .
\end{aligned}
\]
Since \( \A - \alpha\I_m \succeq 0 \) and \( \u \) is a unit vector, \( \u^{*}\A\u - \alpha = \inner{(\A - \alpha\I_m)\u}{\u} \ge 0 \). Since \( \beta\I_n - \B \succeq 0 \), likewise \( \v^{*}\B\v \le \beta \). Hence \( \u^{*}\C\v \) is real and
\[
\u^{*}\C\v \ge s(\alpha - \beta) .
\]
On the other hand, by the Cauchy–Schwarz inequality (@thm-cauchy-schwarz) and @thm-operator-norm-properties (a),
\[
\lvert\u^{*}\C\v\rvert \le \norm{\u}\,\norm{\C\v} \le \norm{\C}_2 .
\]
Combining, \( s(\alpha - \beta) \le \norm{\C}_2 \), and dividing by \( \alpha - \beta > 0 \) gives the first bound.

**The Frobenius norm.** Hermitian matrices are normal. Every \( \lambda_i \ge \alpha \) and every \( \mu_j \le \beta \), as shown above, so \( \lambda_i - \mu_j \ge \alpha - \beta \) for all \( i, j \). By @thm-sep-normal, \( \operatorname{sep}_F(\A, \B) = \min_{i,j}(\lambda_i - \mu_j) \ge \alpha - \beta \), and @prp-sep-properties (d) gives \( \norm{\X}_F \le \norm{\C}_F/\operatorname{sep}_F(\A, \B) \le \norm{\C}_F/(\alpha - \beta) \). This proves the theorem.
:::

The trick deserves its name because it is portable. Whenever a matrix \( \X \) satisfies a linear equation and one wants \( \norm{\X}_2 \), take a top singular pair of \( \X \) itself and test the equation against it. The spectral norm is then attained on the test, and the rest is a pair of scalar inequalities. Notice what was **not** used: the size of the gap between individual eigenvalues. Only the two half-lines \( [\alpha, \infty) \) and \( (-\infty, \beta] \) matter, which is why the bound survives when \( \A \) and \( \B \) have many eigenvalues each.

::: {.remark}
The one-sided hypothesis does real work in the spectral-norm bound, as Exercise C2 shows. When the spectra of two Hermitian matrices are merely at distance \( \delta \), in any interlaced pattern, the spectral-norm bound does hold with a larger constant: \( \norm{\X}_2 \le (\pi/2)\norm{\C}_2/\delta \), and \( \pi/2 \) cannot be improved. We do not prove this, and nothing in the book depends on it.
:::

The form of the theorem used most often has a plus sign and two positive definite matrices. It is a direct translation.

::: {#cor-positive-sylvester}
[Sylvester Bound for Positive Matrices]

Let \( \S \in M_m(\nC) \) and \( \T \in M_n(\nC) \) be Hermitian with \( \S \succeq \alpha\I_m \) and \( \T \succeq \beta\I_n \), where \( \alpha + \beta > 0 \). Then for every \( \C \in M_{m \times n}(\nC) \) the equation
\[
\S\X + \X\T = \C
\]
has exactly one solution, and it satisfies
\[
\norm{\X}_2 \le \frac{\norm{\C}_2}{\alpha + \beta}, \qquad \norm{\X}_F \le \frac{\norm{\C}_F}{\alpha + \beta} .
\]
:::

::: {.proof}
The equation reads \( \S\X - \X(-\T) = \C \). The matrix \( -\T \) is Hermitian, and \( -\beta\I_n - (-\T) = \T - \beta\I_n \succeq 0 \), so \( -\T \preceq -\beta\I_n \). Since \( \alpha > -\beta \), @thm-sylvester-one-sided applies to the pair \( (\S, -\T) \) with the numbers \( \alpha \) and \( -\beta \), and \( \alpha - (-\beta) = \alpha + \beta \).
:::

The hypothesis is weaker than it looks: \( \alpha \) or \( \beta \) may be negative, provided their sum is positive. The typical case is \( \S, \T \succ 0 \) with \( \alpha = \lambda_m(\S) \) and \( \beta = \lambda_n(\T) \), the smallest eigenvalues, which are the best constants because \( \S \succeq \lambda_m(\S)\I_m \) (@lem-extreme-eigenvalues-quadratic-form). Section 10 applies the corollary twice in this form, once with \( \S \) and \( \T \) the square roots of two positive definite matrices and once with them the positive factors of two polar decompositions.

::: {#exm-positive-sylvester-sharp}
[The Bound Can Be Attained]

Let \( \S = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \), \( \T = (1) \) and \( \C = \begin{pmatrix} 4 \\ -4 \end{pmatrix} \). Solve \( \S\X + \X\T = \C \) and compare with @cor-positive-sylvester.
:::

::: {.solution}
The eigenvalues of \( \S \) are \( 1 \) and \( 3 \) (as for \( \A \) in @exm-sep-normal-pair), so \( \S \succeq 1\cdot\I_2 \) by @lem-extreme-eigenvalues-quadratic-form, and \( \T \succeq 1 \). The corollary applies with \( \alpha = \beta = 1 \) and predicts \( \norm{\X}_2 \le \norm{\C}_2/2 \).

Here \( \X = \x \) is a column and the equation is \( (\S + \I_2)\x = \C \), with
\[
\S + \I_2 = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}, \qquad (\S + \I_2)^{-1} = \frac{1}{8}\begin{pmatrix} 3 & -1 \\ -1 & 3 \end{pmatrix} .
\]
So \( \x = \tfrac18(12 + 4, -4 - 12) = (2, -2) \). For a column, the spectral and Frobenius norms are both the Euclidean length, so \( \norm{\X}_2 = 2\sqrt2 \), while \( \norm{\C}_2/2 = 4\sqrt2/2 = 2\sqrt2 \). The bound is an equality.

The reason is visible: \( \C \) is an eigenvector of \( \S \) for its smallest eigenvalue \( 1 \), so \( (\S + \I_2)\C = 2\C \), and the solution is \( \x = \C/2 \), of norm exactly \( \norm{\C}_2/(\alpha + \beta) \). The data sits where both one-sided hypotheses are tight.
:::

## Exercises

### A. Check your understanding

:::: {#exr-sylvester-bounds-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define \( \operatorname{sep}_F(\A, \B) \) for \( \A \in M_m(\nC) \) and \( \B \in M_n(\nC) \), and state how it is computed from the Kronecker matrix \( \K \).
2. True or false: \( \operatorname{sep}_F(\A, \B) = \min_{i,j}\lvert\lambda_i - \mu_j\rvert \) for all square \( \A, \B \). Justify your answer.
3. True or false: \( \operatorname{sep}_F(\A + c\I_m, \B + c\I_n) = \operatorname{sep}_F(\A, \B) \) for every \( c \in \nC \). Justify your answer.
4. State the bound on the solution of \( \A\X - \X\B = \C \) in terms of the separation, including its hypothesis.
5. In the proof of @thm-sylvester-one-sided, which vectors are the equation multiplied by, and where are the hypotheses \( \A \succeq \alpha\I_m \) and \( \B \preceq \beta\I_n \) used?
:::
::::

::: {.solution}
(a) \( \operatorname{sep}_F(\A, \B) = \min\{\norm{\A\X - \X\B}_F : \norm{\X}_F = 1\} \), the minimum over \( \X \in M_{m \times n}(\nC) \) (@def-sep). It equals \( \sigma_{mn}(\K) \), the smallest singular value of \( \K = \I_n \otimes \A - \B\tp \otimes \I_m \) (@prp-sep-properties (a)).

(b) False. It is true for normal pairs (@thm-sep-normal), but @exm-sep-far-below-gap has spectra at distance \( 1 \) and separation \( 1/10 \) when \( t = 99/10 \). What is always true is the inequality \( \le \) of @prp-sep-properties (c).

(c) True. For every \( \X \), \( (\A + c\I_m)\X - \X(\B + c\I_n) = \A\X + c\X - \X\B - c\X = \A\X - \X\B \), so the two minima are taken over the same set of values.

(d) If \( \spec(\A) \cap \spec(\B) = \varnothing \), the unique solution satisfies \( \norm{\X}_F \le \norm{\C}_F/\operatorname{sep}_F(\A, \B) \), and equality holds for some \( \C \ne \0 \) (@prp-sep-properties (d)).

(e) By \( \u^{*} \) on the left and \( \v \) on the right, where \( \u, \v \) are unit vectors with \( \X\v = s\u \) and \( \X^{*}\u = s\v \), \( s = \norm{\X}_2 \). The hypotheses give \( \u^{*}\A\u \ge \alpha \) and \( \v^{*}\B\v \le \beta \), which make \( \u^{*}\C\v = s(\u^{*}\A\u - \v^{*}\B\v) \) at least \( s(\alpha - \beta) \).
:::

### B. Practice

:::: {#exr-sylvester-bounds-b1}
[B1: A positive Sylvester equation]

Let
\[
\S = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}, \quad \T = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}, \quad \C = \begin{pmatrix} 3 & 4 \\ -3 & -4 \end{pmatrix} .
\]

::: {.enumerate options="label=(\alph*)"}
1. Find the largest \( \alpha \) and \( \beta \) with \( \S \succeq \alpha\I_2 \) and \( \T \succeq \beta\I_2 \), and state the bound that @cor-positive-sylvester gives for \( \norm{\X}_2 \).
2. Solve \( \S\X + \X\T = \C \), column by column.
3. Compute \( \norm{\X}_2 \) and \( \norm{\C}_2 \), and check the bound. Hence decide whether the bound is attained here.
:::
::::

::: {.solution}
(a) \( p_{\S}(x) = (x - 3)^2 - 1 = (x - 2)(x - 4) \), so \( \lambda_2(\S) = 2 \), and \( \lambda_2(\T) = 1 \). By @lem-extreme-eigenvalues-quadratic-form, \( \inner{\S\x}{\x} \ge 2 \) for unit \( \x \), with equality at an eigenvector, so \( \alpha = 2 \) is the largest constant with \( \S \succeq \alpha\I_2 \); likewise \( \beta = 1 \). The corollary gives \( \norm{\X}_2 \le \norm{\C}_2/3 \).

(b) Since \( \T \) is diagonal, column \( j \) of \( \X\T \) is \( t_{jj} \) times column \( j \) of \( \X \). So column \( j \) of the equation is \( (\S + t_{jj}\I_2)\x_j = \c_j \). For \( j = 1 \): \( \begin{psmallmatrix} 4 & 1 \\ 1 & 4 \end{psmallmatrix}\x_1 = (3, -3) \), and \( \x_1 = (1, -1) \) works, since \( 4 - 1 = 3 \) and \( 1 - 4 = -3 \). For \( j = 2 \): \( \begin{psmallmatrix} 5 & 1 \\ 1 & 5 \end{psmallmatrix}\x_2 = (4, -4) \), and \( \x_2 = (1, -1) \) works. The solution is unique by @cor-positive-sylvester, so
\[
\X = \begin{pmatrix} 1 & 1 \\ -1 & -1 \end{pmatrix} .
\]

(c) Both matrices have rank one: \( \X = \a\b\tp \) with \( \a = (1, -1) \), \( \b = (1, 1) \), and \( \C = \a\c\tp \) with \( \c = (3, 4) \). For a rank-one matrix \( \a\b\tp \), the spectral norm equals the Frobenius norm (@prp-spectral-vs-frobenius), which is \( \norm{\a}\,\norm{\b} \) by the computation in @prp-sep-properties (c). So \( \norm{\X}_2 = \sqrt2\cdot\sqrt2 = 2 \) and \( \norm{\C}_2 = \sqrt2\cdot 5 = 5\sqrt2 \). The bound reads \( 2 \le 5\sqrt2/3 \approx 2.357 \), which holds. It is not attained. Each column of \( \C \) lies along the eigenvector \( (1, -1) \) of \( \S \) for \( \alpha = 2 \), but the second column is paired with \( t_{22} = 2 \) rather than \( \beta = 1 \), so the second column of \( \X \) is \( \c_2/4 \), not \( \c_2/3 \).
:::

:::: {#exr-sylvester-bounds-b2}
[B2: Separations of four pairs]

For each pair, compute \( \operatorname{sep}_F(\A, \B) \) and decide whether it equals \( \min_{i,j}\lvert\lambda_i - \mu_j\rvert \). Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \A = \diag(1, 3) \), \( \B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \).
2. \( \A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \), \( \B = (-1) \).
3. \( \A = \begin{pmatrix} 0 & -2 \\ 2 & 0 \end{pmatrix} \), \( \B = \diag(1, -1) \).
4. \( \A = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix} \), \( \B = (0) \).
:::
::::

::: {.solution}
(a) \( \B \) is real symmetric with eigenvalues \( \pm1 \), and \( 1 \in \spec(\A) \cap \spec(\B) \). So \( \operatorname{sep}_F(\A, \B) = 0 \) by @prp-sep-properties (b), which equals the minimum distance \( \lvert 1 - 1\rvert = 0 \).

(b) Both matrices are real symmetric, hence normal. The eigenvalues of \( \A \) are \( 1, 3 \) and that of \( \B \) is \( -1 \), so @thm-sep-normal gives \( \operatorname{sep}_F(\A, \B) = \min(2, 4) = 2 \). It equals the minimum distance.

(c) \( \A\tp\A = 4\I_2 = \A\A\tp \), so \( \A \) is normal, with \( p_{\A}(x) = x^2 + 4 \) and eigenvalues \( \pm2i \). \( \B \) is diagonal. The distances \( \lvert\pm2i \mp 1\rvert \) all equal \( \sqrt5 \), so \( \operatorname{sep}_F(\A, \B) = \sqrt5 \) by @thm-sep-normal, equal to the minimum distance.

(d) This is @exm-sep-far-below-gap with \( t = 4 \): \( \operatorname{sep}_F(\A, \B) = (\sqrt{20} - 4)/2 = \sqrt5 - 2 \approx 0.236 \), while the spectra \( \{1\} \) and \( \{0\} \) are at distance \( 1 \). They are not equal. The theorem does not apply because \( \A \) is not normal: \( \A\tp\A = \begin{psmallmatrix} 1 & 4 \\ 4 & 17 \end{psmallmatrix} \ne \begin{psmallmatrix} 17 & 4 \\ 4 & 1 \end{psmallmatrix} = \A\A\tp \).
:::

:::: {#exr-sylvester-bounds-b3}
[B3: A symmetric Sylvester equation]

Let \( \A \in M_n(\nC) \) be Hermitian with \( \A \succeq 2\I_n \), and let \( \C \in M_n(\nC) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \A\X + \X\A = \C \) has exactly one solution, and that it satisfies \( \norm{\X}_2 \le \norm{\C}_2/4 \).
2. Prove that if \( \C \) is Hermitian, then so is \( \X \).
:::
::::

::: {.solution}
(a) Apply @cor-positive-sylvester with \( \S = \T = \A \) and \( \alpha = \beta = 2 \). Since \( \alpha + \beta = 4 > 0 \), the equation has exactly one solution, and \( \norm{\X}_2 \le \norm{\C}_2/4 \).

(b) Take the adjoint of \( \A\X + \X\A = \C \). Since \( \A^{*} = \A \) and \( \C^{*} = \C \), we get \( \X^{*}\A + \A\X^{*} = \C \), so \( \X^{*} \) is also a solution. By the uniqueness in (a), \( \X^{*} = \X \).
:::

### C. Going deeper

:::: {#exr-sylvester-bounds-c1}
[C1: The separation is stable, and it measures a distance]

Let \( \A \in M_m(\nC) \), \( \B \in M_n(\nC) \), \( \E \in M_m(\nC) \) and \( \F \in M_n(\nC) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \norm{\E\X}_F \le \norm{\E}_2\norm{\X}_F \) and \( \norm{\X\F}_F \le \norm{\F}_2\norm{\X}_F \) for every \( \X \in M_{m \times n}(\nC) \).
2. Prove that \( \lvert\operatorname{sep}_F(\A + \E, \B + \F) - \operatorname{sep}_F(\A, \B)\rvert \le \norm{\E}_2 + \norm{\F}_2 \).
3. Now let \( n = 1 \) and \( \B = (\mu) \). Prove that there is \( \E \) with \( \norm{\E}_2 = \operatorname{sep}_F(\A, \B) \) such that \( \mu \) is an eigenvalue of \( \A + \E \).
4. Hence, for \( t = 99/10 \) in @exm-sep-far-below-gap, exhibit the size of a perturbation of \( \A \) that makes \( 0 \) an eigenvalue, and explain why the eigenvalue gap \( 1 \) is a poor guide to how close the pair is to having a common eigenvalue.
:::

*Hint for (c): use a singular value decomposition of \( \A - \mu\I_m \).*
::::

::: {.solution}
(a) Let \( \x_1, \dots, \x_n \) be the columns of \( \X \). The columns of \( \E\X \) are \( \E\x_q \), so by @thm-operator-norm-properties (a)
\[
\norm{\E\X}_F^2 = \sum_{q}\norm{\E\x_q}^2 \le \norm{\E}_2^2\sum_q\norm{\x_q}^2 = \norm{\E}_2^2\norm{\X}_F^2 .
\]
For the second, \( \norm{\X\F}_F = \norm{(\X\F)^{*}}_F = \norm{\F^{*}\X^{*}}_F \), since conjugate transposition does not change the moduli of the entries. By the first part this is at most \( \norm{\F^{*}}_2\norm{\X^{*}}_F = \norm{\F^{*}}_2\norm{\X}_F \). Finally \( \norm{\F^{*}}_2 = \norm{\F}_2 \): if \( \F = \U\vSigma\V^{*} \) is a singular value decomposition, then \( \F^{*} = \V\vSigma\tp\U^{*} \) is one for \( \F^{*} \), with the same diagonal, so \( \sigma_1(\F^{*}) = \sigma_1(\F) \) by @thm-singular-values-unique and @thm-operator-norm-formulas (c).

(b) Let \( \norm{\X}_F = 1 \). By the triangle inequality (@cor-triangle-inequality, the Frobenius norm being induced by an inner product) and (a),
\[
\begin{aligned}
\norm{(\A + \E)\X - \X(\B + \F)}_F &\ge \norm{\A\X - \X\B}_F - \norm{\E\X}_F - \norm{\X\F}_F \\
&\ge \operatorname{sep}_F(\A, \B) - \norm{\E}_2 - \norm{\F}_2 .
\end{aligned}
\]
Taking the minimum over \( \X \) gives \( \operatorname{sep}_F(\A + \E, \B + \F) \ge \operatorname{sep}_F(\A, \B) - \norm{\E}_2 - \norm{\F}_2 \). Applying this to the pair \( (\A + \E, \B + \F) \) with the perturbations \( -\E, -\F \) gives the reverse inequality, and together they are the claim.

(c) By @prp-sep-properties (f), \( s \coloneqq \operatorname{sep}_F(\A, \B) = \sigma_m(\A - \mu\I_m) \). Let \( \A - \mu\I_m = \U\vSigma\V^{*} \) be a singular value decomposition (@thm-svd), with last columns \( \u_m \) of \( \U \) and \( \v_m \) of \( \V \). Then \( (\A - \mu\I_m)\v_m = s\u_m \), comparing column \( m \) of \( (\A - \mu\I_m)\V = \U\vSigma \). Put \( \E = -s\,\u_m\v_m^{*} \). Then \( (\A + \E - \mu\I_m)\v_m = s\u_m - s\u_m(\v_m^{*}\v_m) = \0 \) with \( \v_m \ne \0 \), so \( \mu \) is an eigenvalue of \( \A + \E \). Also \( \norm{\E\x} = s\lvert\v_m^{*}\x\rvert \le s\norm{\x} \) by Cauchy–Schwarz, with equality at \( \x = \v_m \), so \( \norm{\E}_2 = s \).

(d) With \( \mu = 0 \) and \( \operatorname{sep}_F(\A, (0)) = 1/10 \), part (c) gives a perturbation of spectral norm \( 1/10 \) after which \( 0 \) is an eigenvalue of \( \A + \E \), so \( \A + \E \) and \( \B \) share an eigenvalue. The eigenvalues \( 1 \) and \( 0 \) are at distance \( 1 \), but a perturbation ten times smaller than that distance destroys the solvability of the equation. By (b) with \( \F = \0 \), no perturbation of spectral norm less than \( 1/10 \) can do it, since it leaves the separation positive. So the separation, not the eigenvalue gap, is the distance to a shared eigenvalue here.
:::

:::: {#exr-sylvester-bounds-c2}
[C2: Interlaced spectra break the spectral-norm bound]

Let \( \A = \diag(0, 2) \), \( \B = \diag(1, 3) \) and \( \C = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Show that every eigenvalue of \( \A \) is at distance at least \( 1 \) from every eigenvalue of \( \B \), and explain why @thm-sylvester-one-sided does not apply with \( \alpha - \beta = 1 \).
2. Solve \( \A\X - \X\B = \C \).
3. Show that \( \norm{\X}_2 > \norm{\C}_2 \).
4. Verify directly that \( \norm{\X}_F \le \norm{\C}_F \), as @thm-sep-normal requires.
:::

*Hint for (c): compute \( \C\tp\C \), and test \( \X \) on the vector \( (1, 1) \).*
::::

::: {.solution}
(a) The eigenvalues are \( 0, 2 \) and \( 1, 3 \), and the four differences \( \lambda_i - \mu_j \) are \( -1, -3, 1, -1 \), all of modulus at least \( 1 \). The theorem needs \( \A \succeq \alpha\I \) and \( \B \preceq \beta\I \) with \( \alpha > \beta \), that is, every eigenvalue of \( \A \) above every eigenvalue of \( \B \), or, applying it to \( (-\A, -\B) \), every one below. Neither holds, since \( 0 < 1 < 2 < 3 \) interlace. Applied honestly, the best one-sided constants are \( \alpha = 0 \) and \( \beta = 3 \), and \( \alpha > \beta \) fails.

(b) As in the diagonal example after @def-sep, \( (\A\X - \X\B)_{ij} = (a_{ii} - b_{jj})x_{ij} \), so \( x_{ij} = c_{ij}/(a_{ii} - b_{jj}) \):
\[
\X = \begin{pmatrix} 1/(0 - 1) & 1/(0 - 3) \\ 1/(2 - 1) & -1/(2 - 3) \end{pmatrix} = \begin{pmatrix} -1 & -1/3 \\ 1 & 1 \end{pmatrix} .
\]

(c) \( \C\tp\C = 2\I_2 \), so both singular values of \( \C \) are \( \sqrt2 \) and \( \norm{\C}_2 = \sqrt2 \) (@thm-operator-norm-formulas (c)). For \( \x = (1, 1)/\sqrt2 \), a unit vector, \( \X\x = (-4/3, 2)/\sqrt2 \), so
\[
\norm{\X\x}^2 = \frac{1}{2}\Bigl(\frac{16}{9} + 4\Bigr) = \frac{26}{9} > 2 .
\]
Hence \( \norm{\X}_2 \ge \sqrt{26}/3 > \sqrt2 = \norm{\C}_2 \).

(d) \( \norm{\X}_F^2 = 1 + \tfrac19 + 1 + 1 = \tfrac{28}{9} \) and \( \norm{\C}_F^2 = 4 \), so \( \norm{\X}_F \le \norm{\C}_F \), in agreement with @thm-sep-normal, which gives \( \operatorname{sep}_F(\A, \B) = 1 \). So the Frobenius bound with constant \( 1/\delta \) survives interlacing, while the spectral-norm bound with the same constant does not.
:::
