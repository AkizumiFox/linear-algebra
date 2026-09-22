# The Bauer–Fike Theorem

Section 3 bounded the movement of the eigenvalues of an arbitrary matrix by a constant times \( \norm{\E}_2^{1/n} \), and the Jordan block showed that nothing better holds in general. The culprit was the Jordan block itself. This section removes it by assuming that \( \A \) is diagonalizable, and the exponent \( 1/n \) becomes \( 1 \): every eigenvalue of \( \A + \E \) lies within \( \kappa_2(\X)\norm{\E}_2 \) of some eigenvalue of \( \A \), where \( \X \) is a matrix of eigenvectors.

This is the theorem several earlier chapters pointed to. Chapter 11 §11 described it as the statement "that for a diagonalizable \( \A \) every eigenvalue of a perturbed \( \A + \E \) lies within \( \kappa\norm{\E} \) of some eigenvalue of \( \A \), where \( \kappa \) measures how far from unitary the diagonalizing matrix is, and that \( \kappa = 1 \) exactly in the normal case", and said that it "needs matrix norms and a little analysis, and Chapter 19 develops both and proves it". Chapter 15 §07 and Chapter 16 §03 promised a bound "for a diagonalizable matrix" carrying "an extra factor that measures how far the eigenvector basis of \( \A \) is from orthonormal". Chapter 16 §11 left the bounds for non-Hermitian matrices, "beginning with Bauer–Fike", to this chapter, and Chapter 15 §08 recorded that "the bounds that do exist, Weyl's and Bauer–Fike's, are Chapters 16 and 19". We prove the theorem, identify the factor, prove the "exactly", and then return to the defective case. There the \( m \)-th root comes back, where \( m \) is the size of the largest Jordan block.

Throughout, \( \A \in M_n(\nC) \), the perturbation is \( \E \in M_n(\nC) \), and \( \kappa_p(\X) = \norm{\X}_p\norm{\X^{-1}}_p \) is the condition number of @def-condition-number. No fact of analysis is imported in this section beyond those already used by the results it cites.

## Factoring out the inverse

The whole section runs on one estimate. If \( \mu \) is an eigenvalue of \( \A + \E \) but not of \( \A \), then \( \A - \mu\I \) is invertible while \( \A + \E - \mu\I \) is not. A small \( \E \) cannot destroy invertibility (@cor-invertible-matrices-open), so \( \E \) must be large compared with the inverse of \( \A - \mu\I \). The matrix \( (\A - \mu\I)^{-1} \), a function of \( \mu \), is called the **resolvent** of \( \A \), up to a sign convention. Chapter 15 asked for this estimate in @exr-continuity-of-eigenvalues-c1. Since the theorems below rest on it, we prove it here in full.

::: {#lem-perturbed-eigenvalue-resolvent}
[A Perturbed Eigenvalue Forces a Large Resolvent]

Let \( \A, \E \in M_n(\nC) \), let \( \norm{\cdot} \) be an operator norm on \( M_n(\nC) \) (@def-operator-norm), and let \( \mu \) be an eigenvalue of \( \A + \E \) that is **not** an eigenvalue of \( \A \). Then
\[
1 \le \norm{(\A - \mu\I)^{-1}\E} \le \norm{(\A - \mu\I)^{-1}}\,\norm{\E} .
\]
:::

::: {.proof}
Since \( \mu \notin \spec(\A) \), the matrix \( \A - \mu\I \) is invertible (@thm-eigenvalue-characterizations), and
\[
\A + \E - \mu\I = (\A - \mu\I)\bigl(\I + (\A - \mu\I)^{-1}\E\bigr) .
\]
The left side is singular, because \( \mu \) is an eigenvalue of \( \A + \E \). If the second factor on the right were invertible, the product of two invertible matrices would be invertible. So \( \I - \F \) is singular, where \( \F = -(\A - \mu\I)^{-1}\E \). By @thm-neumann-series (a), \( \norm{\F} < 1 \) would make \( \I - \F \) invertible, hence \( \norm{\F} \ge 1 \). Since \( \norm{\F} = \norm{(\A - \mu\I)^{-1}\E} \), this is the first inequality, and the second is submultiplicativity (@thm-operator-norm-properties (d)).
:::

The lemma holds for every matrix and needs no eigenvectors. To turn it into a bound on \( \lvert \lambda_i - \mu\rvert \), we need to compute \( \norm{(\A - \mu\I)^{-1}} \) in terms of the distances from \( \mu \) to the eigenvalues. For a diagonal matrix that is immediate, and diagonalizable matrices are diagonal in the right coordinates.

## The theorem

We need one fact about diagonal matrices. Let \( \D = \diag(d_1, \dots, d_n) \) and \( p \in \{1, 2, \infty\} \). For every \( \x \), each coordinate of \( \D\x \) is \( d_ix_i \), with \( \lvert d_ix_i\rvert \le (\max_j\lvert d_j\rvert)\lvert x_i\rvert \), so \( \norm{\D\x}_p \le (\max_j\lvert d_j\rvert)\norm{\x}_p \). Equality holds at \( \x = \e_k \), where \( k \) is an index with \( \lvert d_k\rvert = \max_j\lvert d_j\rvert \). Hence
\[
\norm{\diag(d_1, \dots, d_n)}_p = \max_j\lvert d_j\rvert \qquad (p = 1, 2, \infty) .
\]{#eq-diagonal-norm}

::: {#thm-bauer-fike}
[Bauer–Fike Theorem]

Let \( \A \in M_n(\nC) \) be diagonalizable. Write \( \A = \X\vLambda\X^{-1} \), where \( \X \) is invertible and \( \vLambda \) is the diagonal matrix with diagonal entries \( \lambda_1, \dots, \lambda_n \). Let \( \E \in M_n(\nC) \) be arbitrary, and let \( p \in \{1, 2, \infty\} \). Then every eigenvalue \( \mu \) of \( \A + \E \) satisfies
\[
\min_{1 \le i \le n}\lvert \lambda_i - \mu\rvert \le \kappa_p(\X)\,\norm{\E}_p .
\]
:::

::: {.idea}
Change coordinates so that \( \A \) becomes \( \vLambda \). Then \( \A + \E \) becomes \( \vLambda + \X^{-1}\E\X \), with the same eigenvalues, and the perturbation has grown by at most the factor \( \kappa_p(\X) \). For the diagonal matrix \( \vLambda \), the resolvent \( (\vLambda - \mu\I)^{-1} \) has norm exactly \( 1/\min_i\lvert \lambda_i - \mu\rvert \), and @lem-perturbed-eigenvalue-resolvent finishes the proof.
:::

::: {.proof}
If \( \mu = \lambda_i \) for some \( i \), the left side is \( 0 \) and there is nothing to prove. So suppose \( \mu \ne \lambda_i \) for every \( i \), and put \( \delta = \min_i\lvert \lambda_i - \mu\rvert > 0 \).

Since \( \X^{-1}(\A + \E)\X = \vLambda + \F \) with \( \F = \X^{-1}\E\X \), the matrices \( \A + \E \) and \( \vLambda + \F \) are similar, so \( \mu \) is an eigenvalue of \( \vLambda + \F \) (@thm-charpoly-similarity-invariant). The eigenvalues of \( \vLambda \) are the \( \lambda_i \), so \( \mu \notin \spec(\vLambda) \). By @lem-perturbed-eigenvalue-resolvent with the operator norm \( \norm{\cdot}_p \),
\[
1 \le \norm{(\vLambda - \mu\I)^{-1}}_p\,\norm{\F}_p .
\]
Now \( (\vLambda - \mu\I)^{-1} = \diag\bigl(1/(\lambda_1 - \mu), \dots, 1/(\lambda_n - \mu)\bigr) \), whose norm is \( \max_i 1/\lvert \lambda_i - \mu\rvert = 1/\delta \) by @eq-diagonal-norm. By submultiplicativity (@thm-operator-norm-properties (d)), \( \norm{\F}_p \le \norm{\X^{-1}}_p\norm{\E}_p\norm{\X}_p = \kappa_p(\X)\norm{\E}_p \). Therefore \( 1 \le \kappa_p(\X)\norm{\E}_p/\delta \), that is, \( \delta \le \kappa_p(\X)\norm{\E}_p \). This proves the theorem.
:::

The proof used only two properties of \( \norm{\cdot}_p \): it is an operator norm, and it gives a diagonal matrix the norm \( \max_j\lvert d_j\rvert \). So the theorem holds for every operator norm with that second property. The spectral norm is the one used in practice, and \( \kappa_2(\X) \) is the headline constant.

Read the theorem as a picture. Draw the closed disc of radius \( \kappa_p(\X)\norm{\E}_p \) about each \( \lambda_i \); every eigenvalue of \( \A + \E \) lies in the union. The bound is **one-sided**, like Elsner's (@thm-elsner-spectral-variation). It does not say that each disc holds one perturbed eigenvalue. When the discs are disjoint, @lem-eigenvalue-count-constant adds that, and Exercise C1 does it.

::: {.check}
Let \( \A = \diag(1, 2) \). Which matrices \( \X \) satisfy \( \X^{-1}\A\X \) diagonal, and what does @thm-bauer-fike give for each of them?
:::

::: {.solution}
The eigenvalues \( 1, 2 \) are distinct and each eigenspace is a line: \( E_1(\A) = \Span(\e_1) \) and \( E_2(\A) = \Span(\e_2) \). The columns of \( \X \) must be eigenvectors (@thm-diagonalization), so \( \X = \diag(a, b) \) or \( \X = \begin{psmallmatrix} 0 & a \\ b & 0 \end{psmallmatrix} \) with \( a, b \ne 0 \). In both cases the singular values of \( \X \) are \( \lvert a\rvert \) and \( \lvert b\rvert \), so \( \kappa_2(\X) = \max(\lvert a\rvert, \lvert b\rvert)/\min(\lvert a\rvert, \lvert b\rvert) \) (@prp-condition-number-properties (d)). The theorem gives \( \min_i\lvert \lambda_i - \mu\rvert \le \kappa_2(\X)\norm{\E}_2 \). This is \( \norm{\E}_2 \) when \( \lvert a\rvert = \lvert b\rvert \), and arbitrarily weak as \( \lvert a\rvert/\lvert b\rvert \) grows. The theorem is true for every choice, and one uses the best.
:::

## Normal matrices

For a normal matrix the eigenvectors can be chosen orthonormal, and then the factor is \( 1 \). The second half of the next result proves the converse, in the form Chapter 11 §11 stated it: \( \kappa = 1 \) **exactly** in the normal case.

::: {#cor-bauer-fike-normal}
[Bauer–Fike for Normal Matrices]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \A \in M_n(\nC) \) be normal with eigenvalues \( \lambda_1, \dots, \lambda_n \), and let \( \E \in M_n(\nC) \). Then every eigenvalue \( \mu \) of \( \A + \E \) satisfies \( \min_i\lvert \lambda_i - \mu\rvert \le \norm{\E}_2 \).
2. Let \( \A \in M_n(\nC) \) be diagonalizable. Then
   \[
   \inf\bigl\{\kappa_2(\X) : \X^{-1}\A\X \text{ is diagonal}\bigr\} = 1 ,
   \]
   the infimum over invertible \( \X \), if and only if \( \A \) is normal.
:::
:::

::: {.idea}
Part (a) is the theorem with a unitary \( \X \). For (b), write \( \X = \W\vSigma\V^{*} \) by the singular value decomposition. Then \( \A \) is \( \W\vSigma\M\vSigma^{-1}\W^{*} \) with \( \M \) normal. If all the singular values of \( \X \) are nearly equal, \( \vSigma\M\vSigma^{-1} \) is nearly \( \M \), so \( \A \) is nearly the normal matrix \( \W\M\W^{*} \), and its commutator \( \A^{*}\A - \A\A^{*} \) is nearly \( \0 \). A commutator that is arbitrarily small is zero.
:::

::: {.proof}
(a) By @cor-spectral-complex-matrix, \( \A = \U\vLambda\U^{*} \) with \( \U \) unitary and \( \vLambda = \diag(\lambda_1, \dots, \lambda_n) \), so \( \U^{-1} = \U^{*} \). A unitary matrix preserves \( \norm{\cdot}_2 \) (@thm-isometry-characterizations), so \( \norm{\U}_2 = \norm{\U^{*}}_2 = 1 \) and \( \kappa_2(\U) = 1 \). Now apply @thm-bauer-fike with \( \X = \U \) and \( p = 2 \).

(b) \( (\Leftarrow) \) If \( \A \) is normal, the \( \U \) of (a) diagonalizes \( \A \) with \( \kappa_2(\U) = 1 \), and every \( \kappa_2(\X) \ge 1 \) by @prp-condition-number-properties (a). So the infimum is \( 1 \).

\( (\Rightarrow) \) First we prove that every invertible \( \X \) with \( \X^{-1}\A\X = \vLambda \) diagonal satisfies
\[
\begin{aligned}
\norm{\A^{*}\A - \A\A^{*}}_F
&\le 2\bigl(\kappa_2(\X) - 1\bigr)\norm{\vLambda}_F \\
&\quad \cdot \bigl(\norm{\A}_F + \norm{\vLambda}_F\bigr) .
\end{aligned}
\]{#eq-commutator-bound}
Write \( \X = \W\vSigma\V^{*} \) (@thm-svd), with \( \W, \V \) unitary and \( \vSigma = \diag(\sigma_1, \dots, \sigma_n) \). Here \( \sigma_n > 0 \), because \( \X \) is invertible and so has rank \( n \). Then \( \X^{-1} = \V\vSigma^{-1}\W^{*} \), and
\[
\A = \X\vLambda\X^{-1} = \W\vSigma\M\vSigma^{-1}\W^{*},
\qquad \M = \V^{*}\vLambda\V .
\]
Put \( \N = \W\M\W^{*} = (\W\V^{*})\vLambda(\W\V^{*})^{*} \). It is unitarily diagonalizable, hence normal by @cor-spectral-complex-matrix. The \( (i, j) \) entry of \( \vSigma\M\vSigma^{-1} - \M \) is \( m_{ij}(\sigma_i/\sigma_j - 1) \). Write \( \kappa = \kappa_2(\X) = \sigma_1/\sigma_n \) (@prp-condition-number-properties (d)). If \( \sigma_i \ge \sigma_j \), then \( 0 \le \sigma_i/\sigma_j - 1 \le \kappa - 1 \). If \( \sigma_i < \sigma_j \), then \( 0 < 1 - \sigma_i/\sigma_j \le 1 - 1/\kappa \le \kappa - 1 \), the last step because \( (\kappa - 1) - (1 - 1/\kappa) = (\kappa - 1)^2/\kappa \ge 0 \). So every entry is at most \( (\kappa - 1)\lvert m_{ij}\rvert \) in modulus. In the display below, the first equality is @lem-frobenius-unitarily-invariant applied to \( \A - \N = \W(\vSigma\M\vSigma^{-1} - \M)\W^{*} \); the inequality is the entrywise bound just proved, summed over the entries; and the last equality is the same lemma again, applied to \( \M = \V^{*}\vLambda\V \). So
\[
\norm{\A - \N}_F = \norm{\vSigma\M\vSigma^{-1} - \M}_F
\le (\kappa - 1)\norm{\M}_F = (\kappa - 1)\norm{\vLambda}_F .
\]
Now \( \N^{*}\N = \N\N^{*} \), and a direct expansion gives
\[
\begin{aligned}
\A^{*}\A - \A\A^{*}
&= \bigl(\A^{*}\A - \N^{*}\N\bigr) - \bigl(\A\A^{*} - \N\N^{*}\bigr) \\
&= \A^{*}(\A - \N) + (\A - \N)^{*}\N \\
&\quad - \A(\A - \N)^{*} - (\A - \N)\N^{*} .
\end{aligned}
\]
The Frobenius norm is submultiplicative (@exm-frobenius-is-a-matrix-norm), \( \norm{\Y^{*}}_F = \norm{\Y}_F \) for every \( \Y \), since the entries of \( \Y^{*} \) are the conjugates of those of \( \Y \) and conjugation preserves the modulus, and \( \norm{\N}_F = \norm{\vLambda}_F \) by @lem-frobenius-unitarily-invariant. So each of the four terms has norm at most \( \norm{\A - \N}_F \) times \( \norm{\A}_F \) or \( \norm{\vLambda}_F \), and
\[
\norm{\A^{*}\A - \A\A^{*}}_F
\le 2\norm{\A - \N}_F\bigl(\norm{\A}_F + \norm{\vLambda}_F\bigr) ,
\]
which with the previous display gives @eq-commutator-bound.

Now suppose the infimum is \( 1 \). Every diagonalizing \( \X \) produces the same \( \norm{\vLambda}_F = (\sum_i\lvert \lambda_i\rvert^2)^{1/2} \), since \( \vLambda \) lists the eigenvalues of \( \A \) in some order. So the right side of @eq-commutator-bound can be made smaller than any positive number, while the left side does not depend on \( \X \). Hence \( \norm{\A^{*}\A - \A\A^{*}}_F = 0 \), so \( \A^{*}\A = \A\A^{*} \) and \( \A \) is normal. This proves the corollary.
:::

Part (b) says more than the bare equivalence. By @eq-commutator-bound, a diagonalizable matrix whose eigenvector matrix is **nearly** unitary is **nearly** normal. It also shows that \( \kappa_2(\X) = 1 \) forces \( \A \) to be normal. In fact \( \kappa_2(\X) = 1 \) says that \( \sigma_1 = \sigma_n \), so \( \vSigma = \sigma_1\I \) and \( \X = \sigma_1\W\V^{*} \), a non-zero multiple of a unitary matrix.

Part (a) is sharp, and the example that shows it is the one Chapter 16 §03 used to warn that Weyl's inequality needs Hermitian matrices. Take \( \A = \0 \), which is normal with the single eigenvalue \( 0 \), and \( \E = \begin{psmallmatrix} 0 & -1 \\ 1 & 0 \end{psmallmatrix} \), with \( \norm{\E}_2 = 1 \) because \( \E \) is unitary. The eigenvalues of \( \A + \E \) are \( \pm i \), since \( p_{\E}(x) = x^2 + 1 \). Weyl's comparison of the \( i \)-th eigenvalues cannot even be stated, because \( \pm i \) are not real. The Bauer–Fike bound can: each of \( \pm i \) is within \( \norm{\E}_2 = 1 \) of \( 0 \), and the distance is exactly \( 1 \). So the constant \( 1 \) in (a) cannot be lowered.

## Residuals

In practice one rarely knows \( \E \). What one has is an approximate eigenpair \( (\mu, \widehat{\x}) \), computed somehow, and the **residual** \( \r = \A\widehat{\x} - \mu\widehat{\x} \), which can be evaluated. The residual turns into a perturbation: a small residual means that \( (\mu, \widehat{\x}) \) is an exact eigenpair of a nearby matrix.

::: {#thm-residual-bound}
[Residual Bound]

Let \( \A = \X\vLambda\X^{-1} \in M_n(\nC) \) be diagonalizable, with \( \vLambda = \diag(\lambda_1, \dots, \lambda_n) \). Let \( \mu \in \nC \) and \( \widehat{\x} \in \nC^n \) with \( \widehat{\x} \ne \0 \), and let \( \eta \ge 0 \) satisfy
\[
\norm{\A\widehat{\x} - \mu\widehat{\x}}_2 \le \eta\,\norm{\widehat{\x}}_2 .
\]
Then some eigenvalue \( \lambda_i \) of \( \A \) satisfies \( \lvert \lambda_i - \mu\rvert \le \kappa_2(\X)\,\eta \). If \( \A \) is normal, some eigenvalue satisfies \( \lvert \lambda_i - \mu\rvert \le \eta \).
:::

::: {.proof}
Put \( \r = \A\widehat{\x} - \mu\widehat{\x} \) and \( \E = -\r\widehat{\x}^{*}/\norm{\widehat{\x}}_2^2 \). Then
\[
(\A + \E)\widehat{\x}
= \A\widehat{\x} - \r\,\frac{\widehat{\x}^{*}\widehat{\x}}{\norm{\widehat{\x}}_2^2}
= \A\widehat{\x} - \r = \mu\widehat{\x} ,
\]
so \( \mu \) is an eigenvalue of \( \A + \E \) with eigenvector \( \widehat{\x} \). For every \( \z \), the Cauchy–Schwarz inequality (@thm-cauchy-schwarz) gives \( \lvert \widehat{\x}^{*}\z\rvert \le \norm{\widehat{\x}}_2\norm{\z}_2 \), hence
\[
\norm{\E\z}_2 = \frac{\lvert \widehat{\x}^{*}\z\rvert\,\norm{\r}_2}{\norm{\widehat{\x}}_2^2}
\le \frac{\norm{\r}_2}{\norm{\widehat{\x}}_2}\,\norm{\z}_2 ,
\]
so \( \norm{\E}_2 \le \norm{\r}_2/\norm{\widehat{\x}}_2 \le \eta \). (The first inequality is an equality, since \( \E\widehat{\x} = -\r \).) By @thm-bauer-fike with \( p = 2 \), some \( \lambda_i \) satisfies \( \lvert \lambda_i - \mu\rvert \le \kappa_2(\X)\norm{\E}_2 \le \kappa_2(\X)\eta \). If \( \A \) is normal, use @cor-bauer-fike-normal (a) instead.
:::

The theorem reverses the usual question. Instead of asking how far the eigenvalues of a given perturbed matrix have moved, it asks: of which nearby matrix is my computed answer exactly right? The answer is \( \A + \E \) with \( \norm{\E}_2 = \norm{\r}_2/\norm{\widehat{\x}}_2 \). An error analysis of this kind, which measures an answer by a change in the data that makes it exact, is a **backward error analysis**. Chapter 23 builds on it. For a normal matrix, the scaled residual norm \( \norm{\r}_2/\norm{\widehat{\x}}_2 \) is itself a certified error bar for \( \mu \).

::: {#exm-residual-certificate}
[An error bar from one product]

Let \( \A = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} \), \( \widehat{\x} = (1, 2) \) and \( \mu = \tfrac72 \). Compute the residual, and say what interval @thm-residual-bound certifies around \( \mu \). Then compare it with the truth.
:::

::: {.solution}
\( \A\widehat{\x} = (4, 7) \) and \( \mu\widehat{\x} = (\tfrac72, 7) \), so \( \r = (\tfrac12, 0) \), with \( \norm{\r}_2 = \tfrac12 \) and \( \norm{\widehat{\x}}_2 = \sqrt5 \). Take \( \eta = \norm{\r}_2/\norm{\widehat{\x}}_2 = \sqrt5/10 \approx 0.2236 \). The matrix \( \A \) is real symmetric, hence normal, so @thm-residual-bound gives an eigenvalue of \( \A \) within \( \eta \) of \( \tfrac72 \), and that eigenvalue is real (@thm-self-adjoint-real-eigenvalues). So \( \A \) has an eigenvalue in \( [\tfrac72 - \eta, \tfrac72 + \eta] \approx [3.276, 3.724] \), and no eigenvalue was computed to say so: one matrix–vector product did it.

*The truth.* \( p_{\A}(x) = (x - 2)(x - 3) - 1 = x^2 - 5x + 5 \), with roots \( (5 \pm \sqrt5)/2 \). The larger is \( \approx 3.618 \), which does lie in the interval, at distance \( \approx 0.118 \) from \( \tfrac72 \) — about half of \( \eta \), so the certificate costs a factor of \( 2 \) in sharpness.
:::

## A worked example

Chapter 11 §11 perturbed a corner of \( \begin{psmallmatrix} 1 & M \\ 0 & 1 \end{psmallmatrix} \), with a double eigenvalue, and found the eigenvalues moving by \( \sqrt{M\varepsilon} \) (@exm-eigenvalue-sensitivity). Its closing remark said that "a matrix with well-separated eigenvalues and a large defect behaves less dramatically". Bauer–Fike says how much less.

::: {#exm-bauer-fike-two-by-two}
[A large corner, separated eigenvalues]

Let \( M > 0 \), \( \A = \begin{pmatrix} 1 & M \\ 0 & 2 \end{pmatrix} \), and \( \E = \varepsilon\,\e_2\e_1\tp \) with \( 0 < \varepsilon \le 1 \). Diagonalize \( \A \) in two ways, compute \( \kappa_2 \) of each eigenvector matrix, and compare the Bauer–Fike bound with the exact movement of the eigenvalues.
:::

::: {.solution}
*Eigenvectors.* \( \A \) is upper triangular with distinct diagonal entries \( 1, 2 \), which are its eigenvalues. For \( 1 \), \( \A - \I = \begin{psmallmatrix} 0 & M \\ 0 & 1 \end{psmallmatrix} \) has kernel \( \Span(\e_1) \). For \( 2 \), \( \A - 2\I = \begin{psmallmatrix} -1 & M \\ 0 & 0 \end{psmallmatrix} \) has kernel spanned by \( (M, 1) \). Two natural choices are
\[
\X_1 = \begin{pmatrix} 1 & M \\ 0 & 1 \end{pmatrix},
\qquad
\X_2 = \begin{pmatrix} 1 & M/s \\ 0 & 1/s \end{pmatrix},
\quad s = \sqrt{1 + M^2} .
\]
The second has columns of length \( 1 \). Both satisfy \( \X^{-1}\A\X = \diag(1, 2) \).

*\( \kappa_2(\X_1) \).* \( \X_1^{*}\X_1 = \begin{psmallmatrix} 1 & M \\ M & 1 + M^2 \end{psmallmatrix} \) has trace \( 2 + M^2 \) and determinant \( 1 \). Its eigenvalues \( \sigma_1^2 \ge \sigma_2^2 \) therefore have product \( 1 \), and \( \kappa_2(\X_1) = \sigma_1/\sigma_2 = \sigma_1^2 \). Solving the quadratic,
\[
\kappa_2(\X_1) = \frac{2 + M^2 + M\sqrt{M^2 + 4}}{2} ,
\]
which exceeds \( M^2 \).

*\( \kappa_2(\X_2) \).* \( \X_2^{*}\X_2 = \begin{psmallmatrix} 1 & q \\ q & 1 \end{psmallmatrix} \) with \( q = M/s \), since the columns are unit vectors whose inner product is \( M/s \). Its eigenvalues are \( 1 \pm q \), so
\[
\kappa_2(\X_2)^2 = \frac{1 + q}{1 - q} = \frac{s + M}{s - M} = (s + M)^2 ,
\]
using \( (s + M)(s - M) = s^2 - M^2 = 1 \). Hence \( \kappa_2(\X_2) = M + \sqrt{1 + M^2} \), which lies between \( 2M \) and \( 2M + 1 \).

*The bound.* \( \norm{\E}_2 = \varepsilon \), since \( \E \) has a single non-zero entry. With \( \X_2 \), @thm-bauer-fike gives movement at most \( (M + \sqrt{1 + M^2})\varepsilon \), about \( 2M\varepsilon \). With \( \X_1 \) it gives about \( M^2\varepsilon \).

*The truth.* \( p_{\A + \E}(x) = (x - 1)(x - 2) - M\varepsilon = x^2 - 3x + 2 - M\varepsilon \), with roots \( \bigl(3 \pm \sqrt{1 + 4M\varepsilon}\bigr)/2 \). Each eigenvalue has moved by
\[
\frac{\sqrt{1 + 4M\varepsilon} - 1}{2}
= \frac{2M\varepsilon}{1 + \sqrt{1 + 4M\varepsilon}} ,
\]
multiplying top and bottom by \( \sqrt{1 + 4M\varepsilon} + 1 \). The denominator is at least \( 2 \), and at most \( 2 + 2M\varepsilon \) because \( \sqrt{1 + 4M\varepsilon} \le 1 + 2M\varepsilon \). So the movement lies between \( M\varepsilon/(1 + M\varepsilon) \) and \( M\varepsilon \).

*Numbers.* For \( M = 100 \) and \( \varepsilon = 10^{-6} \), the eigenvalues move by about \( 0.9999 \times 10^{-4} \), and the bound with \( \X_2 \) is about \( 2.0 \times 10^{-4} \). The bound with \( \X_1 \) is about \( 10^{-2} \). By comparison, in @exm-eigenvalue-sensitivity, the same corner and the same \( \varepsilon \) moved a **double** eigenvalue by \( \sqrt{M\varepsilon} = 10^{-2} \). Separating the eigenvalues turns a square-root amplification into a linear one, with a constant of about \( M \). The constant is still large, and \( \kappa_2(\X_2) \) predicts it correctly to within a factor of about \( 2 \).
:::

::: {.warning}
**\( \kappa_2(\X) \) belongs to the choice of \( \X \), not to \( \A \).** Eigenvectors can be rescaled, and rescaling changes \( \kappa_2 \): in @exm-bauer-fike-two-by-two the same matrix gave \( \kappa_2(\X_1) \approx 10^4 \) and \( \kappa_2(\X_2) \approx 200 \) at \( M = 100 \). The theorem holds for every choice, so use the best one you can find; normalizing the columns is a reasonable first step. And even the best \( \X \) measures all the eigenvalues at once. Section 11 attaches a separate condition number to each simple eigenvalue, and one eigenvalue can be well conditioned while \( \X \) is badly conditioned.
:::

## Defective matrices

When \( \A \) is not diagonalizable, write \( \A = \X\J\X^{-1} \) with \( \J \) a Jordan form (@thm-jordan-canonical-form). The letter \( \J \) is local to this subsection; elsewhere in the book \( \J \) is the all-ones matrix, which does not appear here. The proof of @thm-bauer-fike goes through verbatim, except that \( (\J - \mu\I)^{-1} \) is no longer diagonal. Its norm is no longer \( 1/\delta \); it grows like \( 1/\delta^m \) as \( \delta \to 0 \), where \( m \) is the size of the largest Jordan block. Taking \( m \)-th roots brings back the exponent of Section 3.

::: {#thm-bauer-fike-defective}
[Bauer–Fike for a Jordan Form]

Let \( \A = \X\J\X^{-1} \in M_n(\nC) \), where \( \X \) is invertible and \( \J \) is a Jordan form of \( \A \) whose largest block has size \( m \). Let \( \lambda_1, \dots, \lambda_n \) be the eigenvalues of \( \A \), let \( \E \in M_n(\nC) \), and put \( \theta = m\,\kappa_2(\X)\norm{\E}_2 \). Then every eigenvalue \( \mu \) of \( \A + \E \) satisfies
\[
\min_{1 \le i \le n}\lvert \lambda_i - \mu\rvert \le \max\bigl(\theta, \theta^{1/m}\bigr) .
\]
:::

::: {.idea}
Run the proof of @thm-bauer-fike with \( \J \) in place of \( \vLambda \). The only new work is to bound \( \norm{(\J_k(\lambda) - \mu\I)^{-1}}_2 \) for one block. The block is \( (\lambda - \mu)\I + \N \), with \( \N \) nilpotent of norm at most \( 1 \), so its inverse is a **finite** Neumann series \( \sum_{j<k}(-1)^j\N^j/(\lambda - \mu)^{j+1} \) with at most \( m \) terms. Bound it by \( m\delta^{-1} \) when \( \delta \ge 1 \) and by \( m\delta^{-m} \) when \( \delta < 1 \).
:::

::: {.proof}
Put \( \delta = \min_i\lvert \lambda_i - \mu\rvert \). If \( \delta = 0 \) there is nothing to prove, so suppose \( \delta > 0 \). The upper triangular \( \J \) has its diagonal entries as eigenvalues (@thm-diagonal-of-triangular-form (b)), and these are the \( \lambda_i \) because \( \J \) and \( \A \) are similar (@thm-charpoly-similarity-invariant); so \( \mu \notin \spec(\J) \). As in the proof of @thm-bauer-fike, \( \mu \) is an eigenvalue of \( \J + \X^{-1}\E\X \), and @lem-perturbed-eigenvalue-resolvent with submultiplicativity gives
\[
1 \le \norm{(\J - \mu\I)^{-1}}_2\,\kappa_2(\X)\,\norm{\E}_2 .
\]

*One block.* Let \( \J_k(\lambda) \) be a block of \( \J \), so \( k \le m \) and \( \lvert \lambda - \mu\rvert \ge \delta \), and write \( \J_k(\lambda) - \mu\I = a\I + \N \) with \( a = \lambda - \mu \ne 0 \) and \( \N = \J_k(0) \). The matrix \( \N \) sends \( \e_1 \) to \( \0 \) and \( \e_j \) to \( \e_{j-1} \) for \( j \ge 2 \), so \( \N^k \) sends every \( \e_j \) to \( \0 \) and \( \N^k = \0 \). Then
\[
(a\I + \N)\sum_{j=0}^{k-1}\frac{(-1)^j\N^j}{a^{j+1}}
= \sum_{j=0}^{k-1}\frac{(-1)^j\N^j}{a^{j}} - \sum_{j=1}^{k}\frac{(-1)^{j}\N^{j}}{a^{j}}
= \I - \frac{(-1)^k\N^k}{a^k} = \I ,
\]
so the sum is the inverse of \( a\I + \N \). The same description of \( \N \) gives \( \norm{\N\x}_2^2 = \sum_{j \ge 2}\lvert x_j\rvert^2 \le \norm{\x}_2^2 \), so \( \norm{\N}_2 \le 1 \). Hence \( \norm{\N^j}_2 \le 1 \) for every \( j \ge 0 \) by submultiplicativity, and the triangle inequality (@thm-operator-norm-properties (b)) gives
\[
\norm{(\J_k(\lambda) - \mu\I)^{-1}}_2
\le \sum_{j=1}^{k}\lvert a\rvert^{-j}
\le \sum_{j=1}^{m}\delta^{-j} ,
\]
using \( \lvert a\rvert \ge \delta \) and \( k \le m \).

*All blocks.* \( (\J - \mu\I)^{-1} \) is block diagonal, with the inverses of the blocks \( \J_k(\lambda) - \mu\I \) on its diagonal. Split \( \x \) into the matching pieces \( \x_1, \dots, \x_r \) and let \( \C_1, \dots, \C_r \) be the diagonal blocks. Then \( \norm{(\J - \mu\I)^{-1}\x}_2^2 = \sum_l\norm{\C_l\x_l}_2^2 \le (\max_l\norm{\C_l}_2)^2\norm{\x}_2^2 \). So \( \norm{(\J - \mu\I)^{-1}}_2 \le \sum_{j=1}^{m}\delta^{-j} \), and
\[
1 \le \frac{\theta}{m}\sum_{j=1}^{m}\delta^{-j} .
\]

*Two cases.* If \( \delta \ge 1 \), each \( \delta^{-j} \le \delta^{-1} \), so \( 1 \le \theta/\delta \) and \( \delta \le \theta \). If \( \delta < 1 \), each \( \delta^{-j} \le \delta^{-m} \), so \( 1 \le \theta\delta^{-m} \), that is \( \delta^m \le \theta \) and \( \delta \le \theta^{1/m} \). In both cases \( \delta \le \max(\theta, \theta^{1/m}) \). This proves the theorem.
:::

For \( m = 1 \), \( \J \) is diagonal, \( \theta = \kappa_2(\X)\norm{\E}_2 \), and the theorem is @thm-bauer-fike with \( p = 2 \). For \( m \ge 2 \) and small \( \E \), the term \( \theta^{1/m} \) dominates, and the eigenvalues move like the \( m \)-th root of the perturbation. That exponent is the Jordan block's signature, and it is the answer to Chapter 9 §03's warning that the Jordan form is not stable. Section 3's @exm-jordan-root-perturbation shows it cannot be improved. There \( \A = \J_n(0) \), \( \X = \I \), \( m = n \) and \( \norm{\E}_2 = \varepsilon \le 1/n \), so \( \theta = n\varepsilon \le 1 \) and the theorem gives \( \max(\theta, \theta^{1/n}) = (n\varepsilon)^{1/n} \) while the eigenvalues actually move \( \varepsilon^{1/n} \). The two differ by the factor \( n^{1/n} \), which never exceeds \( 3^{1/3} < 1.45 \).

Only the size of the largest block enters, and a diagonalizable part of \( \A \) is charged the same \( m \)-th root as the defective part. Section 11 separates the eigenvalues. There a simple eigenvalue gets its own first-order condition number, and that number becomes infinite exactly when two eigenvalues merge into a Jordan block.

## Exercises

### A. Check your understanding

:::: {#exr-bauer-fike-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State @thm-bauer-fike with all its hypotheses.
2. True or false: the constant \( \kappa_2(\X) \) in @thm-bauer-fike is determined by \( \A \). Justify your answer.
3. True or false: for every \( \A, \E \in M_n(\nC) \), every eigenvalue of \( \A + \E \) lies within \( \norm{\E}_2 \) of an eigenvalue of \( \A \). Justify your answer.
4. What does @cor-bauer-fike-normal (a) give when \( \A \) is normal, and which example shows that its constant cannot be lowered?
5. In @thm-bauer-fike-defective, what exponent appears for small \( \norm{\E}_2 \), and what decides it?
:::
::::

::: {.solution}
(a) See @thm-bauer-fike: \( \A = \X\vLambda\X^{-1} \) diagonalizable, \( \E \) arbitrary, \( p \in \{1, 2, \infty\} \); every eigenvalue \( \mu \) of \( \A + \E \) is within \( \kappa_p(\X)\norm{\E}_p \) of some \( \lambda_i \).

(b) False. The columns of \( \X \) can be rescaled, and \( \kappa_2 \) changes. The Quick check gave \( \X = \diag(a, b) \) for \( \A = \diag(1, 2) \), with \( \kappa_2(\X) = \max(\lvert a\rvert, \lvert b\rvert)/\min(\lvert a\rvert, \lvert b\rvert) \), any number \( \ge 1 \).

(c) False. By @exm-jordan-root-perturbation with \( n = 2 \), \( \A = \J_2(0) \) and \( \E = \varepsilon\e_2\e_1\tp \) with \( 0 < \varepsilon < 1 \) give eigenvalues \( \pm\sqrt\varepsilon \) of \( \A + \E \), at distance \( \sqrt\varepsilon > \varepsilon = \norm{\E}_2 \) from \( 0 \). The hypothesis that fails is diagonalizability.

(d) Every eigenvalue of \( \A + \E \) is within \( \norm{\E}_2 \) of an eigenvalue of \( \A \). The example \( \A = \0 \), \( \E = \begin{psmallmatrix} 0 & -1 \\ 1 & 0 \end{psmallmatrix} \) has perturbed eigenvalues \( \pm i \) at distance exactly \( 1 = \norm{\E}_2 \).

(e) The exponent \( 1/m \), where \( m \) is the size of the largest Jordan block of \( \A \).
:::

### B. Practice

:::: {#exr-bauer-fike-b1}
[B1: A Bauer–Fike region]

Let \( \A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Find an eigenvector matrix \( \X \) with columns of length \( 1 \), and compute \( \kappa_2(\X) \).
2. Hence find \( r \) such that every eigenvalue of \( \A + \E \) lies within \( r \) of \( 1 \) or of \( 3 \) whenever \( \norm{\E}_2 \le 0.01 \).
3. Compute the eigenvalues of \( \A + 0.01\,\e_2\e_1\tp \) exactly, and compare their movement with \( r \).
:::
::::

::: {.solution}
(a) The eigenvalues are \( 1 \) and \( 3 \), with eigenvectors \( \e_1 \) and \( (1, 1) \), since \( (\A - 3\I)(1, 1) = (-2 + 2, 0) = \0 \). So \( \X = \begin{psmallmatrix} 1 & 1/\sqrt2 \\ 0 & 1/\sqrt2 \end{psmallmatrix} \). Then \( \X^{*}\X = \begin{psmallmatrix} 1 & q \\ q & 1 \end{psmallmatrix} \) with \( q = 1/\sqrt2 \), with eigenvalues \( 1 \pm q \), so
\[
\kappa_2(\X)^2 = \frac{1 + q}{1 - q} = \frac{\sqrt2 + 1}{\sqrt2 - 1} = (\sqrt2 + 1)^2 ,
\]
and \( \kappa_2(\X) = 1 + \sqrt2 \approx 2.414 \).

(b) By @thm-bauer-fike with \( p = 2 \), \( r = (1 + \sqrt2)(0.01) \approx 0.0241 \) works.

(c) \( p(x) = (x - 1)(x - 3) - 0.02 = x^2 - 4x + 2.98 \), with roots \( 2 \pm \sqrt{1.02} \). Each eigenvalue has moved by \( \sqrt{1.02} - 1 \approx 0.00995 \), well within \( r \approx 0.0241 \).
:::

:::: {#exr-bauer-fike-b2}
[B2: A residual certificate]

Let \( \A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \), \( \widehat{\x} = (10, 9) \) and \( \mu = 3 \).

::: {.enumerate options="label=(\alph*)"}
1. Compute the residual \( \r = \A\widehat{\x} - \mu\widehat{\x} \) and \( \eta = \norm{\r}_2/\norm{\widehat{\x}}_2 \).
2. Hence show that \( \A \) has an eigenvalue in the interval \( [3 - \eta, 3 + \eta] \), without computing the eigenvalues of \( \A \).
:::
::::

::: {.solution}
(a) \( \A\widehat{\x} = (29, 28) \) and \( 3\widehat{\x} = (30, 27) \), so \( \r = (-1, 1) \), \( \norm{\r}_2 = \sqrt2 \), \( \norm{\widehat{\x}}_2 = \sqrt{181} \), and \( \eta = \sqrt{2/181} \approx 0.105 \).

(b) \( \A \) is real symmetric, hence normal. By @thm-residual-bound, some eigenvalue \( \lambda \) satisfies \( \lvert \lambda - 3\rvert \le \eta \). The eigenvalues of a real symmetric matrix are real (@thm-self-adjoint-real-eigenvalues), so \( \lambda \in [3 - \eta, 3 + \eta] \). (In fact \( \lambda = 3 \), with eigenvector \( (1, 1) \).)
:::

:::: {#exr-bauer-fike-b3}
[B3: A defective bound]

Let \( \A = \J_2(3) \).

::: {.enumerate options="label=(\alph*)"}
1. Explain why @thm-bauer-fike does not apply to \( \A \).
2. Use @thm-bauer-fike-defective to find \( r \) such that every eigenvalue of \( \A + \E \) lies within \( r \) of \( 3 \) whenever \( \norm{\E}_2 \le 10^{-4} \).
3. Compute the eigenvalues of \( \A + 10^{-4}\e_2\e_1\tp \), and compare.
:::
::::

::: {.solution}
(a) \( \A \) has the single eigenvalue \( 3 \) with algebraic multiplicity \( 2 \), and \( \A - 3\I = \J_2(0) \) has rank \( 1 \), so the eigenspace has dimension \( 1 \). Hence \( \A \) is not diagonalizable (@thm-diagonalization), and there is no \( \X \) to put in @thm-bauer-fike.

(b) \( \A \) is its own Jordan form, so take \( \X = \I \), with \( \kappa_2(\I) = 1 \), and \( m = 2 \). Then \( \theta = 2 \cdot 1 \cdot 10^{-4} = 2 \times 10^{-4} \), and \( \max(\theta, \theta^{1/2}) = \sqrt2 \times 10^{-2} \approx 0.0141 \). So \( r = \sqrt2 \times 10^{-2} \) works.

(c) \( p(x) = (x - 3)^2 - 10^{-4} \), with roots \( 3 \pm 10^{-2} \). The movement \( 0.01 \) is below \( r \approx 0.0141 \), and it is a hundred times the size \( 10^{-4} \) of the perturbation: the square root at work.
:::

### C. Going deeper

:::: {#exr-bauer-fike-c1}
[C1: One eigenvalue in each disc]

Let \( \A = \X\vLambda\X^{-1} \) have \( n \) distinct eigenvalues \( \lambda_1, \dots, \lambda_n \), put \( g = \min_{i \ne j}\lvert \lambda_i - \lambda_j\rvert \), and let \( \E \) satisfy \( r = \kappa_2(\X)\norm{\E}_2 < g/2 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that for each \( i \), \( \A + \E \) has exactly one eigenvalue in the disc \( \{z : \lvert z - \lambda_i\rvert \le r\} \), and that \( \A + \E \) is diagonalizable.
2. Deduce that if \( \A \) and \( \E \) are real and every \( \lambda_i \) is real, then every eigenvalue of \( \A + \E \) is real.
:::

*Hint: apply @lem-eigenvalue-count-constant to the path \( \A + t\E \).*
::::

::: {.solution}
(a) Let \( Q_i = \{z : \lvert z - \lambda_i\rvert \le r\} \). For \( i \ne j \), \( z \in Q_i \) and \( w \in Q_j \), the triangle inequality (@thm-complex-triangle-inequality) gives \( \lvert z - w\rvert \ge \lvert \lambda_i - \lambda_j\rvert - 2r \ge g - 2r > 0 \). So \( Q_i \) and the union \( L_i \) of the other \( Q_j \) are at distance at least \( g - 2r > 0 \). For \( t \in [0, 1] \), @thm-bauer-fike applied to \( \A \) and \( t\E \) puts every eigenvalue of \( \A + t\E \) within \( \kappa_2(\X)\norm{t\E}_2 \le r \) of some \( \lambda_j \), that is, in \( Q_i \cup L_i \). The path \( \A + t\E = (1 - t)\A + t(\A + \E) \) is of the form in @lem-eigenvalue-count-constant, so the number of eigenvalues in \( Q_i \) is the same at \( t = 0 \) and \( t = 1 \). At \( t = 0 \) it is \( 1 \): \( \lambda_i \in Q_i \), and \( \lambda_j \in Q_j \subseteq L_i \) is not in \( Q_i \) for \( j \ne i \). So \( \A + \E \) has exactly one eigenvalue in each \( Q_i \). The \( Q_i \) are pairwise disjoint, so these \( n \) eigenvalues are distinct, and \( \A + \E \) is diagonalizable by @cor-distinct-eigenvalues-diagonalizable.

(b) Let \( \mu \) be the eigenvalue of \( \A + \E \) in \( Q_i \). Since \( \lambda_i \) is real, \( \lvert \conj{\mu} - \lambda_i\rvert = \lvert \mu - \lambda_i\rvert \le r \), so \( \conj{\mu} \in Q_i \). Since \( \A + \E \) is real, \( \conj{\mu} \) is also an eigenvalue (@thm-real-matrix-complex-eigenvalues). By (a), \( Q_i \) holds only one eigenvalue, so \( \conj{\mu} = \mu \), and \( \mu \) is real. Every eigenvalue of \( \A + \E \) lies in some \( Q_i \), so all of them are real.
:::

:::: {#exr-bauer-fike-c2}
[C2: The best shift for a residual]

Let \( \A \in M_n(\nC) \) and \( \widehat{\x} \in \nC^n \) with \( \widehat{\x} \ne \0 \), and put \( \rho = \widehat{\x}^{*}\A\widehat{\x}/\widehat{\x}^{*}\widehat{\x} \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \norm{\A\widehat{\x} - \mu\widehat{\x}}_2 \ge \norm{\A\widehat{\x} - \rho\widehat{\x}}_2 \) for every \( \mu \in \nC \), with equality only for \( \mu = \rho \).
2. Deduce that if \( \A \) is normal, then \( \A \) has an eigenvalue \( \lambda \) with \( \lvert \lambda - \rho\rvert \le \norm{\A\widehat{\x} - \mu\widehat{\x}}_2/\norm{\widehat{\x}}_2 \) for **every** \( \mu \in \nC \).
:::
::::

::: {.solution}
(a) Put \( \w = \A\widehat{\x} - \rho\widehat{\x} \). Then \( \inner{\w}{\widehat{\x}} = \widehat{\x}^{*}\w = \widehat{\x}^{*}\A\widehat{\x} - \rho\,\widehat{\x}^{*}\widehat{\x} = 0 \) by the choice of \( \rho \). For any \( \mu \), \( \A\widehat{\x} - \mu\widehat{\x} = \w + (\rho - \mu)\widehat{\x} \) is a sum of two orthogonal vectors, so by the Pythagorean theorem (@thm-pythagoras)
\[
\norm{\A\widehat{\x} - \mu\widehat{\x}}_2^2
= \norm{\w}_2^2 + \lvert \rho - \mu\rvert^2\norm{\widehat{\x}}_2^2 .
\]
This is at least \( \norm{\w}_2^2 \), with equality exactly when \( \lvert \rho - \mu\rvert\,\norm{\widehat{\x}}_2 = 0 \), that is, when \( \mu = \rho \), since \( \widehat{\x} \ne \0 \).

(b) Apply @thm-residual-bound for normal \( \A \) with the shift \( \rho \) and \( \eta = \norm{\A\widehat{\x} - \rho\widehat{\x}}_2/\norm{\widehat{\x}}_2 \). It gives an eigenvalue \( \lambda \) with \( \lvert \lambda - \rho\rvert \le \eta \), and \( \eta \le \norm{\A\widehat{\x} - \mu\widehat{\x}}_2/\norm{\widehat{\x}}_2 \) for every \( \mu \) by (a).
:::
