# The Davis–Kahan Theorem

Weyl's inequality settled the eigenvalues of a Hermitian matrix: under a Hermitian perturbation \( \E \), each of them moves by at most \( \norm{\E}_2 \), whatever the matrix and however its eigenvalues are spaced. Eigenvectors are a different matter, and this section is about them. Section 8 supplied the yardstick, the principal angles between two subspaces, and Section 7 supplied the tool, bounds for the equation \( \A\X - \X\B = \Y \). The theorem of this section is what happens when the two meet: the perturbation of an invariant subspace satisfies a Sylvester equation, and the bounds of Section 7 then measure it.

**Throughout**, \( \A \) and \( \widetilde{\A} = \A + \E \) are Hermitian matrices in \( M_n(\nC) \), so \( \E = \widetilde{\A} - \A \) is Hermitian too, and \( 1 \le k \le n - 1 \). As everywhere in this chapter, \( \norm{\cdot}_2 \) is the spectral norm and \( \norm{\cdot}_F \) the Frobenius norm, and every bound names the norm it holds in. For a subspace we write \( \col(\Q) \) for the column space of a matrix \( \Q \) whose columns span it.

## Eigenvectors can move a long way

Before any theorem, here is what goes wrong. The example is as small as it can be, and every number in it is exact.

::: {#exm-davis-kahan-small-gap}
[A tiny perturbation that turns the eigenvectors through 45°]

Let \( 0 < \eta < 1 \) and
\[
\A = \begin{pmatrix} 1 + \eta & 0 \\ 0 & 1 - \eta \end{pmatrix},
\qquad
\E = \eta\begin{pmatrix} -1 & 1 \\ 1 & 1 \end{pmatrix} .
\]
Compare the eigenvalues and the eigenvectors of \( \A \) and of \( \widetilde{\A} = \A + \E \), and compute \( \norm{\E}_2 \).
:::

::: {.solution}
Adding, \( \widetilde{\A} = \begin{psmallmatrix} 1 & \eta \\ \eta & 1 \end{psmallmatrix} \). Since
\[
\widetilde{\A}\begin{pmatrix} 1 \\ 1 \end{pmatrix} = (1 + \eta)\begin{pmatrix} 1 \\ 1 \end{pmatrix},
\qquad
\widetilde{\A}\begin{pmatrix} 1 \\ -1 \end{pmatrix} = (1 - \eta)\begin{pmatrix} 1 \\ -1 \end{pmatrix},
\]
the eigenvalues of \( \widetilde{\A} \) are \( 1 + \eta \) and \( 1 - \eta \): **exactly** those of \( \A \). The eigenvectors are another story. For the eigenvalue \( 1 + \eta \), the matrix \( \A \) has the unit eigenvector \( \e_1 \) and \( \widetilde{\A} \) has \( \tfrac{1}{\sqrt2}(1, 1) \); the two lines they span meet at the angle \( \pi/4 \), because \( \lvert\inner{\e_1}{\tfrac{1}{\sqrt2}(1,1)}\rvert = \tfrac{1}{\sqrt2} = \cos\tfrac{\pi}{4} \). The same happens for \( 1 - \eta \), with \( \e_2 \) and \( \tfrac{1}{\sqrt2}(1, -1) \).

The matrix \( \E/\eta \) is Hermitian and squares to \( 2\I_2 \), so its eigenvalues are \( \pm\sqrt2 \) (it has trace \( 0 \)), and by @lem-hermitian-spectral-norm
\[
\norm{\E}_2 = \sqrt2\,\eta .
\]
So as \( \eta \to 0^{+} \) the perturbation vanishes, the eigenvalues do not move at all, and yet the eigenvectors of \( \widetilde{\A} \) stay a full \( 45^\circ \) away from those of \( \A \).
:::

The rotation does not shrink with \( \eta \). What does shrink with \( \eta \) is the distance \( 2\eta \) between the two eigenvalues of \( \A \), and that is the whole story: the two eigenvalues are so close that a perturbation of their own size can mix their eigenvectors freely. An eigenvector bound must therefore divide by a gap, and the natural guess is "angle \( \lesssim \) perturbation / gap". Here that ratio is \( \sqrt2\eta/2\eta = 1/\sqrt2 = \sin(\pi/4) \), which is exactly the sine of the angle. The theorem below turns the guess into an inequality, and this example will turn out to attain it.

::: {.warning}
**Well-conditioned eigenvalues do not make well-conditioned eigenvectors.** @cor-weyl-perturbation guarantees that every eigenvalue of a Hermitian matrix moves by at most \( \norm{\E}_2 \), with no mention of gaps, and it is tempting to expect the same of eigenvectors. @exm-davis-kahan-small-gap refutes this: a perturbation of size \( \sqrt2\,\eta \) leaves every eigenvalue fixed and turns every eigenvector through \( \pi/4 \), however small \( \eta \) is. No inequality of the form \( \sin\theta \le C\norm{\E}_2 \), with \( C \) depending only on \( n \), can hold.
:::

## Two norms, three facts

The proofs of this section and the next shuffle unitary factors and matrices with orthonormal columns in and out of norms, sometimes the spectral one and sometimes the Frobenius one. The facts needed are elementary, but they are needed so often that they are worth collecting once. Part (c) is mostly quoted: its norm identities for a matrix with orthonormal columns are @lem-orthonormal-basis-matrix (b) of Section 8, read with \( U = \col(\X) \), and for the Frobenius norm the unitary invariance is @lem-frobenius-unitarily-invariant. The rest — (a), (b) and the inequality \( \norm{\X^{*}\N} \le \norm{\N} \) — is proved below, and what the lemma is really for is to have all of it, in both norms, in one place.

::: {#lem-spectral-frobenius-toolkit}
[Moving Factors in and out of the Two Norms]

Let \( \norm{\cdot} \) stand for either \( \norm{\cdot}_2 \) or \( \norm{\cdot}_F \), the same one throughout each statement.

::: {.enumerate options="label=(\alph*)"}
1. \( \norm{\M^{*}} = \norm{\M} \) for every \( \M \in M_{m \times n}(\nC) \).
2. \( \norm{\X\M\Y} \le \norm{\X}_2\,\norm{\M}\,\norm{\Y}_2 \) whenever the product is defined.
3. If \( \X \in M_{m \times k}(\nC) \) has orthonormal columns, that is \( \X^{*}\X = \I_k \), then \( \norm{\X}_2 = 1 \), \( \norm{\X\M} = \norm{\M} \) and \( \norm{\X^{*}\N} \le \norm{\N} \) for all \( \M \in M_{k \times n}(\nC) \) and \( \N \in M_{m \times n}(\nC) \). In particular \( \norm{\U\M\V} = \norm{\M} \) for unitary \( \U \) and \( \V \).
:::
:::

::: {.proof}
(a) For \( \norm{\cdot}_F \) this holds because \( \M^{*} \) has the same entries as \( \M \) up to position and conjugation. For \( \norm{\cdot}_2 \), let \( \x \in \nC^n \). By @thm-cauchy-schwarz and @thm-operator-norm-properties (a), applied twice,
\[
\norm{\M\x}^2 = \inner{\M^{*}\M\x}{\x} \le \norm{\M^{*}\M\x}\,\norm{\x} \le \norm{\M^{*}}_2\norm{\M}_2\norm{\x}^2 .
\]
Taking the maximum over unit \( \x \) gives \( \norm{\M}_2^2 \le \norm{\M^{*}}_2\norm{\M}_2 \), hence \( \norm{\M}_2 \le \norm{\M^{*}}_2 \) when \( \M \ne \0 \) (and trivially when \( \M = \0 \)). Applying this to \( \M^{*} \), whose conjugate transpose is \( \M \), gives the reverse inequality.

(b) For \( \norm{\cdot}_2 \) this is @thm-operator-norm-properties (d) used twice. For \( \norm{\cdot}_F \), let \( \m_1, \dots, \m_n \) be the columns of \( \M \). The columns of \( \X\M \) are the \( \X\m_j \), and the squared Frobenius norm is the sum of the squared lengths of the columns, so
\[
\norm{\X\M}_F^2 = \sum_j \norm{\X\m_j}^2 \le \norm{\X}_2^2\sum_j\norm{\m_j}^2 = \norm{\X}_2^2\norm{\M}_F^2 .
\]
For a factor on the right, (a) and the left-hand case give \( \norm{\M\Y}_F = \norm{\Y^{*}\M^{*}}_F \le \norm{\Y^{*}}_2\norm{\M^{*}}_F = \norm{\Y}_2\norm{\M}_F \). Combining the two cases gives (b).

(c) For every \( \v \in \nC^k \), \( \norm{\X\v}^2 = \v^{*}\X^{*}\X\v = \norm{\v}^2 \). Hence \( \norm{\X}_2 = 1 \), and multiplying by \( \X \) changes the length of no column, so \( \norm{\X\M}_F = \norm{\M}_F \) and \( \norm{\X\M\v} = \norm{\M\v} \) for every \( \v \), which gives \( \norm{\X\M}_2 = \norm{\M}_2 \). Next, \( \norm{\X^{*}}_2 = \norm{\X}_2 = 1 \) by (a), so \( \norm{\X^{*}\N} \le \norm{\N} \) by (b). Finally, for unitary \( \U \) and \( \V \) both \( \U \) and \( \V^{*} \) have orthonormal columns, so \( \norm{\U\M\V} = \norm{\M\V} = \norm{\V^{*}\M^{*}} = \norm{\M^{*}} = \norm{\M} \), using (a) twice.
:::

Part (c) is the one used most. Its inequality \( \norm{\X^{*}\N} \le \norm{\N} \) says that reading \( \N \) in only some of the coordinates of an orthonormal basis can only lose mass, never gain it.

## The perturbation of a subspace is a Sylvester equation

Fix the data. A Hermitian matrix is normal, so by @cor-spectral-complex-matrix there is a unitary \( \Q \in M_n(\nC) \) with \( \Q^{*}\A\Q \) diagonal, the eigenvalues appearing in any order we like, and they are real by @thm-self-adjoint-real-eigenvalues. Choose \( k \) of them, list them first, and split the columns accordingly:
\[
\Q = \begin{pmatrix} \Q_1 & \Q_2 \end{pmatrix},
\qquad
\Q^{*}\A\Q = \begin{pmatrix} \vLambda_1 & \0 \\ \0 & \vLambda_2 \end{pmatrix},
\]
with \( \Q_1 \in M_{n \times k}(\nC) \) and \( \vLambda_1 \in M_k(\nR) \), \( \vLambda_2 \in M_{n-k}(\nR) \) diagonal. Do the same for \( \widetilde{\A} \), producing \( \widetilde{\Q} = \begin{pmatrix} \widetilde{\Q}_1 & \widetilde{\Q}_2 \end{pmatrix} \), \( \widetilde{\vLambda}_1 \) and \( \widetilde{\vLambda}_2 \). Reading \( \A\Q = \Q(\vLambda_1 \oplus \vLambda_2) \) column by column,
\[
\A\Q_1 = \Q_1\vLambda_1,
\qquad
\widetilde{\A}\widetilde{\Q}_2 = \widetilde{\Q}_2\widetilde{\vLambda}_2 ,
\]
so the columns of \( \Q_1 \) are orthonormal eigenvectors of \( \A \), and \( U = \col(\Q_1) \) is a \( k \)-dimensional subspace invariant under \( \A \). Likewise \( W = \col(\widetilde{\Q}_1) \) is a \( k \)-dimensional subspace invariant under \( \widetilde{\A} \). The question is how far apart \( U \) and \( W \) are, and Section 8 answers "measure the principal angles \( \theta_1 \le \dots \le \theta_k \) of @def-principal-angles".

Put
\[
\X \coloneqq \widetilde{\Q}_2^{*}\Q_1 \in M_{(n-k) \times k}(\nC) .
\]
It measures the angles, and it satisfies an equation.

*The unperturbed subspace, read in the perturbed complement, solves a Sylvester equation whose coefficients are the two spectra and whose right-hand side is the perturbation.*

::: {#lem-davis-kahan-identity}
[The Subspace Perturbation Equation]

In the notation above,
\[
\widetilde{\vLambda}_2\X - \X\vLambda_1 = \widetilde{\Q}_2^{*}\E\Q_1 ,
\]{#eq-davis-kahan-identity}
and the non-zero singular values of \( \X \) are the non-zero sines \( \sin\theta_i \) of the principal angles between \( U = \col(\Q_1) \) and \( W = \col(\widetilde{\Q}_1) \), with multiplicity. In particular
\[
\norm{\X}_F = \norm{\sin\Theta(U, W)}_F ,
\qquad
\norm{\X}_2 = \sin\theta_k = \norm{\sin\Theta(U, W)}_2 ,
\]
where \( \sin\Theta(U, W) = \diag(\sin\theta_1, \dots, \sin\theta_k) \).
:::

::: {.idea}
Compute \( \widetilde{\Q}_2^{*}\widetilde{\A}\Q_1 \) twice. Letting \( \widetilde{\A} \) act to the left, on the perturbed eigenvectors, produces \( \widetilde{\vLambda}_2 \). Writing \( \widetilde{\A} = \A + \E \) and letting \( \A \) act to the right, on the unperturbed ones, produces \( \vLambda_1 \), plus an error term that carries \( \E \). The difference of the two computations is the identity.
:::

::: {.proof}
Taking conjugate transposes in \( \widetilde{\A}\widetilde{\Q}_2 = \widetilde{\Q}_2\widetilde{\vLambda}_2 \), and using \( \widetilde{\A}^{*} = \widetilde{\A} \) and \( \widetilde{\vLambda}_2^{*} = \widetilde{\vLambda}_2 \) (a real diagonal matrix), gives \( \widetilde{\Q}_2^{*}\widetilde{\A} = \widetilde{\vLambda}_2\widetilde{\Q}_2^{*} \). Hence
\[
\widetilde{\Q}_2^{*}\widetilde{\A}\Q_1 = \widetilde{\vLambda}_2\widetilde{\Q}_2^{*}\Q_1 = \widetilde{\vLambda}_2\X .
\]
On the other hand \( \widetilde{\A} = \A + \E \) and \( \A\Q_1 = \Q_1\vLambda_1 \), so
\[
\begin{aligned}
\widetilde{\Q}_2^{*}\widetilde{\A}\Q_1
&= \widetilde{\Q}_2^{*}\Q_1\vLambda_1 + \widetilde{\Q}_2^{*}\E\Q_1 \\
&= \X\vLambda_1 + \widetilde{\Q}_2^{*}\E\Q_1 .
\end{aligned}
\]
Subtracting the two expressions gives @eq-davis-kahan-identity.

For the angles: the columns of the unitary \( \widetilde{\Q} \) form an orthonormal basis of \( \nC^n \) (@thm-isometry-characterizations), so the \( n - k \) columns of \( \widetilde{\Q}_2 \) are orthonormal and orthogonal to every column of \( \widetilde{\Q}_1 \). They therefore span a subspace of \( W^{\perp} \) of dimension \( n - k \), which is all of \( W^{\perp} \) because \( \dim W^{\perp} = n - k \) by @thm-orthogonal-decomposition (c). So \( \widetilde{\Q}_2 \) is a matrix whose columns are an orthonormal basis of \( W^{\perp} \), and @thm-sines-of-principal-angles (a) says that the singular values of \( \widetilde{\Q}_2^{*}\Q_1 = \X \) are the \( \sin\theta_i \), as a multiset completed by zeros; zeros change neither a sum of squares nor a maximum of non-negative numbers. For the two norms, \( \I - P_W = P_{W^{\perp}} = \widetilde{\Q}_2\widetilde{\Q}_2^{*} \) by @lem-orthonormal-basis-matrix (d) and (a), so \( (\I - P_W)\Q_1 = \widetilde{\Q}_2\X \), and @lem-spectral-frobenius-toolkit (c) removes the factor \( \widetilde{\Q}_2 \):
\[
\norm{\X}_F = \norm{(\I - P_W)\Q_1}_F, \qquad \norm{\X}_2 = \norm{(\I - P_W)\Q_1}_2 .
\]
By @thm-sines-of-principal-angles (b), applied with \( U \) and \( W \), these are \( \norm{\sin\Theta(U, W)}_F \) and \( \sin\theta_k = \norm{\sin\Theta(U, W)}_2 \). This proves the lemma.
:::

::: {.check}
Take \( \A = \widetilde{\A} = \I_2 \), so \( \E = \0 \), with \( k = 1 \), \( \Q_1 = \e_1 \) and \( \widetilde{\Q}_1 = \tfrac{1}{\sqrt2}(1, 1) \); both are legitimate choices of unit eigenvector. The subspaces \( U \) and \( W \) are \( 45^\circ \) apart, although the matrices are equal. What does @eq-davis-kahan-identity say here, and why is there no contradiction?
:::

::: {.solution}
Here \( \vLambda_1 = (1) \) and \( \widetilde{\vLambda}_2 = (1) \), so the equation reads \( 1\cdot\X - \X\cdot 1 = \0 \), which **every** \( 1 \times 1 \) matrix satisfies. The equation holds, as it must, but it does not determine \( \X \), and \( \X = \widetilde{\Q}_2^{*}\Q_1 = \tfrac{1}{\sqrt2}(1, -1)\cdot\e_1 = \tfrac{1}{\sqrt2} = \sin\tfrac{\pi}{4} \) is one of its many solutions. The trouble is that the spectra of \( \widetilde{\vLambda}_2 \) and \( \vLambda_1 \) overlap. The theorems below assume that they are separated, and then the equation has exactly one solution (@thm-sylvester-equation), which is small when the right-hand side is.
:::

## The \( \sin\Theta \) theorem in the Frobenius norm

With the identity in hand, the theorem is a matter of dividing by the gap. The gap that matters compares **perturbed** eigenvalues outside the subspace with **unperturbed** eigenvalues inside it, because those are the two coefficient matrices of the equation.

::: {#thm-davis-kahan-frobenius}
[The Davis–Kahan \( \sin\Theta \) Theorem]

Let \( \A, \widetilde{\A} = \A + \E \in M_n(\nC) \) be Hermitian, let \( 1 \le k \le n-1 \), and let \( \Q = \begin{pmatrix} \Q_1 & \Q_2 \end{pmatrix} \) and \( \widetilde{\Q} = \begin{pmatrix} \widetilde{\Q}_1 & \widetilde{\Q}_2 \end{pmatrix} \) be unitary, with \( \Q_1, \widetilde{\Q}_1 \in M_{n \times k}(\nC) \), such that
\[
\Q^{*}\A\Q = \vLambda_1 \oplus \vLambda_2,
\qquad
\widetilde{\Q}^{*}\widetilde{\A}\widetilde{\Q} = \widetilde{\vLambda}_1 \oplus \widetilde{\vLambda}_2
\]
are real diagonal. Suppose there is a \( \delta > 0 \) such that \( \lvert\mu - \lambda\rvert \ge \delta \) for **every** diagonal entry \( \mu \) of \( \widetilde{\vLambda}_2 \) and **every** diagonal entry \( \lambda \) of \( \vLambda_1 \). Then the principal angles \( \Theta = \Theta(\col(\Q_1), \col(\widetilde{\Q}_1)) \) satisfy
\[
\norm{\sin\Theta}_F \ \le\ \frac{\norm{\E\Q_1}_F}{\delta} \ \le\ \frac{\sqrt{k}\,\norm{\E}_2}{\delta} .
\]
:::

::: {.idea}
@eq-davis-kahan-identity is a Sylvester equation whose two coefficient matrices are diagonal, hence normal, and for a normal pair the separation of Section 7 is exactly the distance between the two spectra. The hypothesis says that this distance is at least \( \delta \), so Section 7's bound divides the right-hand side by \( \delta \). What is left is @lem-davis-kahan-identity, which reads the size of \( \X \) as the size of \( \sin\Theta \).
:::

::: {.proof}
Write \( \mu_1, \dots, \mu_{n-k} \) for the diagonal entries of \( \widetilde{\vLambda}_2 \), \( \lambda_1, \dots, \lambda_k \) for those of \( \vLambda_1 \), and \( \Y = \widetilde{\Q}_2^{*}\E\Q_1 \), so that \( \widetilde{\vLambda}_2\X - \X\vLambda_1 = \Y \) by @lem-davis-kahan-identity. A diagonal matrix is normal, and its eigenvalues are its diagonal entries, so @thm-sep-normal gives
\[
\operatorname{sep}_F(\widetilde{\vLambda}_2, \vLambda_1) = \min_{i,j}\lvert\mu_i - \lambda_j\rvert \ \ge\ \delta > 0 .
\]
In particular the two spectra are disjoint, so \( \X \) is the **unique** solution of that equation (@thm-sylvester-equation), and @prp-sep-properties (d) applies to it:
\[
\norm{\X}_F \ \le\ \frac{\norm{\Y}_F}{\operatorname{sep}_F(\widetilde{\vLambda}_2, \vLambda_1)} \ \le\ \frac{\norm{\Y}_F}{\delta} .
\]

The columns of \( \widetilde{\Q}_2 \) are orthonormal, so @lem-spectral-frobenius-toolkit (c) gives \( \norm{\Y}_F = \norm{\widetilde{\Q}_2^{*}(\E\Q_1)}_F \le \norm{\E\Q_1}_F \). By @lem-spectral-frobenius-toolkit (b), \( \norm{\E\Q_1}_F \le \norm{\E}_2\norm{\Q_1}_F \), and \( \norm{\Q_1}_F = \sqrt{k} \) because \( \Q_1 \) has \( k \) unit columns. Finally \( \norm{\X}_F = \norm{\sin\Theta}_F \) by @lem-davis-kahan-identity. Chaining the three inequalities proves the theorem.
:::

The right-hand side is a Lipschitz bound with constant \( 1/\delta \), and it is sharp. In @exm-davis-kahan-small-gap, take \( k = 1 \), \( \Q_1 = \e_1 \) with \( \vLambda_1 = (1 + \eta) \), and \( \widetilde{\Q}_2 = \tfrac{1}{\sqrt2}(1, -1) \) with \( \widetilde{\vLambda}_2 = (1 - \eta) \). Then \( \delta = 2\eta \) and \( \E\e_1 = \eta(-1, 1) \) has length \( \sqrt2\,\eta \), so the theorem gives
\[
\sin\theta_1 \le \frac{\sqrt2\,\eta}{2\eta} = \frac{1}{\sqrt2} ,
\]
and the true angle is \( \pi/4 \), whose sine is exactly \( 1/\sqrt2 \). The large rotation there was not a failure of the theorem. It is what the theorem predicts when the gap is no bigger than the perturbation.

::: {.remark}
The roles of \( \A \) and \( \widetilde{\A} \) may be exchanged, since \( \A = \widetilde{\A} + (-\E) \) and the principal angles between \( U \) and \( W \) are those between \( W \) and \( U \) (a matrix and its conjugate transpose have the same singular values). This gives the companion bound \( \norm{\sin\Theta}_F \le \norm{\E\widetilde{\Q}_1}_F/\delta' \), where \( \delta' \) separates the diagonal of \( \vLambda_2 \) from that of \( \widetilde{\vLambda}_1 \). Use whichever one's data are at hand.
:::

## A one-sided version in the spectral norm

The Frobenius theorem controls all \( k \) angles at once. Often only the largest angle matters, \( \norm{\sin\Theta}_2 = \sin\theta_k \), and the Frobenius theorem bounds it too, since \( \norm{\sin\Theta}_2 \le \norm{\sin\Theta}_F \). But its right-hand side \( \norm{\E\Q_1}_F \) can be \( \sqrt{k} \) times \( \norm{\E\Q_1}_2 \), and for large \( k \) that factor is a real loss. When the two spectra are separated by a single point, one entirely above it and the other entirely below, the one-sided bound of Section 7 removes it.

::: {#thm-davis-kahan-one-sided}
[The \( \sin\Theta \) Theorem, One-Sided Case]

In the setting of @thm-davis-kahan-frobenius, suppose instead that there are \( a \in \nR \) and \( \delta > 0 \) such that either

::: {.enumerate options="label=(\roman*)"}
1. every eigenvalue in \( \vLambda_1 \) is \( \ge a \) and every eigenvalue in \( \widetilde{\vLambda}_2 \) is \( \le a - \delta \), or
2. every eigenvalue in \( \vLambda_1 \) is \( \le a \) and every eigenvalue in \( \widetilde{\vLambda}_2 \) is \( \ge a + \delta \).
:::

Then
\[
\norm{\sin\Theta}_2 = \sin\theta_k \ \le\ \frac{\norm{\E\Q_1}_2}{\delta} \ \le\ \frac{\norm{\E}_2}{\delta} .
\]
:::

::: {.proof}
Let \( \X = \widetilde{\Q}_2^{*}\Q_1 \) and \( \Y = \widetilde{\Q}_2^{*}\E\Q_1 \), so that \( \widetilde{\vLambda}_2\X - \X\vLambda_1 = \Y \) by @lem-davis-kahan-identity. For a real diagonal matrix, \( \vLambda \succeq \alpha\I \) means that every diagonal entry is at least \( \alpha \) (@thm-psd-characterizations (b), applied to \( \vLambda - \alpha\I \)).

*Case (ii).* Here \( \widetilde{\vLambda}_2 \succeq (a + \delta)\I \) and \( \vLambda_1 \preceq a\I \), with \( a + \delta > a \). By @thm-sylvester-one-sided, applied with \( \widetilde{\vLambda}_2 \) and \( \vLambda_1 \) in the roles of its two Hermitian coefficients, the solution of \( \widetilde{\vLambda}_2\X - \X\vLambda_1 = \Y \), which is unique because the two spectra are disjoint, satisfies \( \norm{\X}_2 \le \norm{\Y}_2/\delta \).

*Case (i).* Multiply the equation by \( -1 \): \( (-\widetilde{\vLambda}_2)\X - \X(-\vLambda_1) = -\Y \), where now \( -\widetilde{\vLambda}_2 \succeq (\delta - a)\I \) and \( -\vLambda_1 \preceq -a\I \), and \( (\delta - a) - (-a) = \delta > 0 \). So case (ii)'s argument applies and gives \( \norm{\X}_2 \le \norm{-\Y}_2/\delta = \norm{\Y}_2/\delta \).

In both cases, @lem-spectral-frobenius-toolkit (c) and (b) give \( \norm{\Y}_2 \le \norm{\E\Q_1}_2 \le \norm{\E}_2\norm{\Q_1}_2 = \norm{\E}_2 \), and \( \norm{\X}_2 = \sin\theta_k \) by @lem-davis-kahan-identity. This proves the theorem.
:::

The typical use is the top of the spectrum: \( \vLambda_1 \) holds the \( k \) largest eigenvalues of \( \A \), and \( \widetilde{\vLambda}_2 \) the \( n - k \) smallest of \( \widetilde{\A} \). Then (i) holds with \( a = \lambda_k(\A) \) and \( \delta = \lambda_k(\A) - \lambda_{k+1}(\widetilde{\A}) \), provided that number is positive.

::: {.remark}
Davis and Kahan proved more. If the eigenvalues in \( \vLambda_1 \) lie in an interval \( [a, b] \) and every eigenvalue in \( \widetilde{\vLambda}_2 \) lies outside \( (a - \delta, b + \delta) \), on either side, then the spectral bound \( \sin\theta_k \le \norm{\E\Q_1}_2/\delta \) still holds. The proof needs more than the one-sided Sylvester bound, and we do not give it. Nothing in this book depends on it. When the two spectra merely avoid each other by \( \delta \), interleaved in any pattern, what we have proved is the Frobenius theorem, and through \( \norm{\sin\Theta}_2 \le \norm{\sin\Theta}_F \) the spectral consequence \( \sin\theta_k \le \norm{\E\Q_1}_F/\delta \).
:::

## Single eigenvectors

The most common question is about one eigenvector. A simple eigenvalue has a one-dimensional eigenspace, so its unit eigenvector is determined up to a unimodular factor, and the right measure of how far it moves is the angle between the two **lines**. For unit vectors \( \x \) and \( \widetilde{\x} \) we write \( \theta(\x, \widetilde{\x}) \in [0, \pi/2] \) for that angle, so that \( \cos\theta(\x, \widetilde{\x}) = \lvert\inner{\widetilde{\x}}{\x}\rvert \). This is the single principal angle between \( \Span(\x) \) and \( \Span(\widetilde{\x}) \), since the \( 1 \times 1 \) matrix \( \x^{*}\widetilde{\x} \) has the singular value \( \lvert\x^{*}\widetilde{\x}\rvert \).

The theorem needs a separation between the perturbed eigenvalues of \( \widetilde{\A} \) and the unperturbed one of \( \A \). In practice only \( \A \) is known, and Weyl's inequality converts a gap in the spectrum of \( \A \) into the separation the theorem wants.

::: {#cor-eigenvector-perturbation}
[Perturbation of a Single Eigenvector]

Let \( \A, \widetilde{\A} = \A + \E \in M_n(\nC) \) be Hermitian, let \( \lambda_i(\A) \) be a **simple** eigenvalue of \( \A \) with unit eigenvector \( \x \), and put
\[
\gamma \coloneqq \min_{j \ne i}\ \lvert\lambda_i(\A) - \lambda_j(\A)\rvert > 0 .
\]
If \( \norm{\E}_2 < \gamma/2 \), then \( \lambda_i(\widetilde{\A}) \) is a simple eigenvalue of \( \widetilde{\A} \), and every unit eigenvector \( \widetilde{\x} \) of \( \widetilde{\A} \) for it satisfies
\[
\sin\theta(\x, \widetilde{\x}) \ \le\ \frac{\norm{\E}_2}{\gamma - \norm{\E}_2} \ \le\ \frac{2\norm{\E}_2}{\gamma} .
\]
:::

::: {.idea}
Apply the theorem with \( k = 1 \). The only thing to supply is \( \delta \): every eigenvalue \( \lambda_j(\widetilde{\A}) \) with \( j \ne i \) sits within \( \norm{\E}_2 \) of \( \lambda_j(\A) \) by Weyl, which is at least \( \gamma \) away from \( \lambda_i(\A) \). So the separation is at least \( \gamma - \norm{\E}_2 \), by the triangle inequality. The hypothesis \( \norm{\E}_2 < \gamma/2 \) keeps \( \lambda_i(\widetilde{\A}) \) away from its neighbors too, so that "the" eigenvector makes sense.
:::

::: {.proof}
Put \( \varepsilon = \norm{\E}_2 \). By @cor-weyl-perturbation, \( \lvert\lambda_j(\widetilde{\A}) - \lambda_j(\A)\rvert \le \varepsilon \) for every \( j \). Hence for \( j \ne i \), by the triangle inequality in \( \nR \),
\[
\begin{aligned}
\lvert\lambda_j(\widetilde{\A}) - \lambda_i(\A)\rvert
&\ge \lvert\lambda_j(\A) - \lambda_i(\A)\rvert - \lvert\lambda_j(\widetilde{\A}) - \lambda_j(\A)\rvert \\
&\ge \gamma - \varepsilon ,
\end{aligned}
\]
and similarly \( \lvert\lambda_j(\widetilde{\A}) - \lambda_i(\widetilde{\A})\rvert \ge \gamma - 2\varepsilon > 0 \). So \( \lambda_i(\widetilde{\A}) \) differs from every other \( \lambda_j(\widetilde{\A}) \), and it is a simple eigenvalue of \( \widetilde{\A} \).

By @cor-spectral-complex-matrix there is a unitary matrix whose columns are eigenvectors of \( \widetilde{\A} \), with the eigenvalue \( \lambda_i(\widetilde{\A}) \) first. That eigenspace is one-dimensional, so the first column is \( c\widetilde{\x} \) with \( \lvert c\rvert = 1 \), and replacing it by \( \widetilde{\x} \) keeps the columns orthonormal eigenvectors. Call the result \( \widetilde{\Q} = \begin{pmatrix} \widetilde{\x} & \widetilde{\Q}_2 \end{pmatrix} \). Then \( \widetilde{\vLambda}_2 \) is diagonal with entries \( \lambda_j(\widetilde{\A}) \), \( j \ne i \). In the same way build \( \Q = \begin{pmatrix} \x & \Q_2 \end{pmatrix} \) for \( \A \), with \( \vLambda_1 = (\lambda_i(\A)) \). By the display, the hypothesis of @thm-davis-kahan-frobenius holds with \( k = 1 \) and \( \delta = \gamma - \varepsilon > 0 \), so
\[
\sin\theta(\x, \widetilde{\x}) = \norm{\sin\Theta}_F \le \frac{\norm{\E\x}}{\gamma - \varepsilon} \le \frac{\varepsilon}{\gamma - \varepsilon} ,
\]
using \( \norm{\E\x} \le \norm{\E}_2\norm{\x} = \varepsilon \). Finally \( \varepsilon < \gamma/2 \) gives \( \gamma - \varepsilon > \gamma/2 \), so \( \varepsilon/(\gamma - \varepsilon) \le 2\varepsilon/\gamma \). This proves the corollary.
:::

To first order in \( \norm{\E}_2 \) the bound reads \( \sin\theta \lesssim \norm{\E}_2/\gamma \): *an eigenvector is as well conditioned as its eigenvalue is isolated.* The constant cannot be improved, and @exr-davis-kahan-c2 shows it. The factor \( 2 \) in the cruder form is the price of the hypothesis \( \norm{\E}_2 < \gamma/2 \), nothing more. In @exm-davis-kahan-small-gap, \( \gamma = 2\eta \) and \( \norm{\E}_2 = \sqrt2\,\eta > \gamma/2 \), so the corollary does not apply there.

::: {#exm-davis-kahan-two-by-two}
[The theorem and the corollary, side by side]

Let \( \A = \diag(2, 0) \) and \( \E = \tfrac34\begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix} \). Find the exact angle between the eigenvectors of \( \A \) and of \( \widetilde{\A} = \A + \E \) for the larger eigenvalue, and compare it with the bounds of @thm-davis-kahan-frobenius and @cor-eigenvector-perturbation.
:::

::: {.solution}
*Exact.* \( \widetilde{\A} = \begin{psmallmatrix} 2 & 3/4 \\ 3/4 & 0 \end{psmallmatrix} \) has trace \( 2 \) and determinant \( -\tfrac{9}{16} \), so its eigenvalues are \( 1 \pm \sqrt{1 + 9/16} = 1 \pm \tfrac54 \), that is \( \tfrac94 \) and \( -\tfrac14 \). For \( \tfrac94 \), the first row of \( \widetilde{\A} - \tfrac94\I \) is \( (-\tfrac14, \tfrac34) \), which is orthogonal to \( (3, 1) \), and the second row \( (\tfrac34, -\tfrac94) \) is a multiple of the first; so \( \widetilde{\x} = \tfrac{1}{\sqrt{10}}(3, 1) \). With \( \x = \e_1 \),
\[
\cos\theta = \tfrac{3}{\sqrt{10}},
\qquad
\sin\theta = \tfrac{1}{\sqrt{10}} \approx 0.316 .
\]

*The theorem.* Take \( \vLambda_1 = (2) \) and \( \widetilde{\vLambda}_2 = (-\tfrac14) \), so \( \delta = \tfrac94 \). Since \( \E\e_1 = (0, \tfrac34) \), the bound is \( \tfrac34 / \tfrac94 = \tfrac13 \approx 0.333 \), within six percent of the truth.

*The corollary.* The gap is \( \gamma = 2 \), and \( \E \) is \( \tfrac34 \) times a Hermitian matrix with eigenvalues \( \pm1 \), so \( \norm{\E}_2 = \tfrac34 < 1 = \gamma/2 \). The bound is \( \tfrac{3/4}{2 - 3/4} = \tfrac35 = 0.6 \), and its cruder form is \( 2 \cdot \tfrac34/2 = \tfrac34 \).

The theorem is nearly exact because it uses the perturbed eigenvalue \( -\tfrac14 \) itself. The corollary knows only that this eigenvalue lies within \( \tfrac34 \) of \( 0 \), and it must allow for the worst case \( \tfrac34 \), which would leave a separation of only \( \tfrac54 \).
:::

## Clusters: the subspace is stable when the vectors are not

@exm-davis-kahan-small-gap looks like bad news for eigenvectors, and it is, for **individual** eigenvectors of close eigenvalues. But the theorem was stated for subspaces, and that is its real strength. The subspace spanned by the eigenvectors of a cluster of eigenvalues is governed by the gap between the cluster and the rest of the spectrum. The gaps inside the cluster do not enter.

::: {#exm-eigenvector-cluster}
[A stable plane with unstable lines inside it]

Let \( 0 < \eta < 1 \) and
\[
\A = \begin{pmatrix} 1 + \eta & 0 & 0 \\ 0 & 1 - \eta & 0 \\ 0 & 0 & -2 \end{pmatrix},
\qquad
\E = \eta\begin{pmatrix} -1 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix} .
\]
Compare what happens to the eigenvectors for \( 1 \pm \eta \) with what happens to the plane they span. Then bound the motion of that plane under **any** Hermitian perturbation \( \E' \) with \( \norm{\E'}_2 = \varepsilon < 3 - \eta \).
:::

::: {.solution}
The upper-left \( 2 \times 2 \) block is @exm-davis-kahan-small-gap. So the eigenvalues of \( \widetilde{\A} = \A + \E \) are again \( 1 + \eta, 1 - \eta, -2 \), and the eigenvectors for \( 1 \pm \eta \) turn through \( \pi/4 \), to \( \tfrac{1}{\sqrt2}(1, \pm1, 0) \). But they turn **inside** the plane \( U = \Span(\e_1, \e_2) \), which is invariant under both matrices. So the plane has not moved at all: both principal angles between \( U \) and the new plane \( W = U \) are \( 0 \).

@thm-davis-kahan-frobenius with \( k = 2 \) sees this. Take \( \Q_1 = \begin{pmatrix} \e_1 & \e_2 \end{pmatrix} \), \( \vLambda_1 = \diag(1 + \eta, 1 - \eta) \) and \( \widetilde{\vLambda}_2 = (-2) \). The separation is \( \delta = (1 - \eta) - (-2) = 3 - \eta \), and \( \norm{\E\Q_1}_F = \norm{\E}_F = 2\eta \), so
\[
\norm{\sin\Theta}_F \le \frac{2\eta}{3 - \eta} .
\]
This is small with \( \eta \), and it has no \( 2\eta \) in its denominator. (The true value is \( 0 \); the theorem does not know that \( \E \) happens to preserve \( U \).)

For a general Hermitian \( \E' \) with \( \norm{\E'}_2 = \varepsilon \), @cor-weyl-perturbation puts the smallest eigenvalue of \( \A + \E' \) at most \( -2 + \varepsilon \), while the eigenvalues of \( \vLambda_1 \) are at least \( 1 - \eta \). So case (i) of @thm-davis-kahan-one-sided holds with \( a = 1 - \eta \) and \( \delta = 3 - \eta - \varepsilon > 0 \), and the plane moves by
\[
\sin\theta_2 \le \frac{\varepsilon}{3 - \eta - \varepsilon} .
\]
The individual eigenvectors are covered by @cor-eigenvector-perturbation only when \( \varepsilon < \eta \), and then only with a bound of order \( \varepsilon/(2\eta) \).
:::

This is the practical lesson of the section. When a matrix has a cluster of close eigenvalues, do not ask for the individual eigenvectors of the cluster. They are ill-conditioned and may be meaningless at the precision of the data. Ask for an orthonormal basis of the invariant subspace of the whole cluster, which is as stable as the cluster is isolated. Numerical eigensolvers act on this advice.

## Exercises

### A. Check your understanding

:::: {#exr-davis-kahan-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the subspace perturbation equation @eq-davis-kahan-identity, and say which matrix in it measures the principal angles.
2. In @thm-davis-kahan-frobenius, which two lists of eigenvalues must be separated by \( \delta \)? Why not the eigenvalues of \( \A \) inside and outside the subspace?
3. True or false: "if \( \norm{\E}_2 \) is tiny compared with \( \norm{\A}_2 \), then every unit eigenvector of \( \A + \E \) is close to a unit eigenvector of \( \A \)". Justify.
4. Why is \( \norm{\sin\Theta}_2 \le \norm{\sin\Theta}_F \), and when does @thm-davis-kahan-one-sided improve on what the Frobenius theorem gives for \( \norm{\sin\Theta}_2 \)?
5. Which earlier result turns the bound on the matrix \( \X = \widetilde{\Q}_2^{*}\Q_1 \) into a bound on angles?
:::
::::

::: {.solution}
(a) \( \widetilde{\vLambda}_2\X - \X\vLambda_1 = \widetilde{\Q}_2^{*}\E\Q_1 \), with \( \X = \widetilde{\Q}_2^{*}\Q_1 \); by @lem-davis-kahan-identity the singular values of \( \X \) are the sines of the principal angles between \( \col(\Q_1) \) and \( \col(\widetilde{\Q}_1) \), together with zeros.

(b) The diagonal of \( \widetilde{\vLambda}_2 \), the eigenvalues of the **perturbed** matrix belonging to the complement, against the diagonal of \( \vLambda_1 \), the eigenvalues of the **unperturbed** matrix belonging to the subspace. These are the two coefficient matrices of the Sylvester equation, and the proof divides by their separation, which @thm-sep-normal computes as the smallest of those differences. A gap inside the spectrum of \( \A \) alone is useful only after @cor-weyl-perturbation converts it, as in @cor-eigenvector-perturbation.

(c) False. In @exm-davis-kahan-small-gap, \( \norm{\E}_2 = \sqrt2\,\eta \) can be as small as we like compared with \( \norm{\A}_2 = 1 + \eta \), yet each unit eigenvector of \( \A + \E \) makes the angle \( \pi/4 \) with every unit eigenvector of \( \A \), which are the multiples of \( \e_1 \) and \( \e_2 \). What controls eigenvectors is the perturbation relative to the gap, not relative to the matrix.

(d) \( \norm{\sin\Theta}_2 = \sin\theta_k \) is one of the numbers whose squares sum to \( \norm{\sin\Theta}_F^2 \). The Frobenius theorem gives \( \sin\theta_k \le \norm{\E\Q_1}_F/\delta \), and \( \norm{\E\Q_1}_F \) can be as large as \( \sqrt{k}\,\norm{\E\Q_1}_2 \). When the two spectra lie on opposite sides of a gap of width \( \delta \), @thm-davis-kahan-one-sided replaces it by \( \norm{\E\Q_1}_2 \), which is never worse and can be \( \sqrt{k} \) times smaller.

(e) @thm-sines-of-principal-angles, applied with \( W = \col(\widetilde{\Q}_1) \) and the orthonormal basis \( \widetilde{\Q}_2 \) of \( W^{\perp} \).
:::

### B. Practice

:::: {#exr-davis-kahan-b1}
[B1: How far does the top eigenvector move?]

Let
\[
\A = \begin{pmatrix} 5 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & -1 \end{pmatrix},
\qquad
\E = \frac12\begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix},
\]
and let \( \widetilde{\x} \) be a unit eigenvector of \( \widetilde{\A} = \A + \E \) for its largest eigenvalue.

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \norm{\E}_2 \) and the gap \( \gamma \) of \( \lambda_1(\A) = 5 \).
2. Use @cor-eigenvector-perturbation to bound \( \sin\theta(\e_1, \widetilde{\x}) \).
3. Use @thm-davis-kahan-frobenius, with the separation estimated by @cor-weyl-perturbation, to obtain a better bound. Hence show that the angle is less than \( 13^\circ \).
4. Check that \( 2 \) is an eigenvalue of \( \widetilde{\A} \) and find the other two. Recompute the bound of (c) with the exact separation.
:::
::::

::: {.solution}
(a) The matrix \( \M = 2\E \) is symmetric with characteristic polynomial \( t^3 - 2t = t(t^2 - 2) \), so its eigenvalues are \( 0, \pm\sqrt2 \) and \( \norm{\E}_2 = \tfrac12\sqrt2 = \tfrac{\sqrt2}{2} \approx 0.707 \) by @lem-hermitian-spectral-norm. The eigenvalues of \( \A \) are \( 5, 2, -1 \), so \( \gamma = 5 - 2 = 3 \).

(b) \( \norm{\E}_2 \approx 0.707 < 1.5 = \gamma/2 \), so the corollary applies:
\[
\sin\theta \le \frac{\sqrt2/2}{3 - \sqrt2/2} \approx 0.308 .
\]

(c) By @cor-weyl-perturbation, \( \lambda_2(\widetilde{\A}) \le 2 + \tfrac{\sqrt2}{2} \) and \( \lambda_3(\widetilde{\A}) \le -1 + \tfrac{\sqrt2}{2} \), so both lie at distance at least \( \delta = 3 - \tfrac{\sqrt2}{2} \approx 2.293 \) from \( 5 \). Apply @thm-davis-kahan-frobenius with \( k = 1 \), \( \Q_1 = \e_1 \), \( \vLambda_1 = (5) \) and \( \widetilde{\vLambda}_2 = \diag(\lambda_2(\widetilde{\A}), \lambda_3(\widetilde{\A})) \). Since \( \E\e_1 = (0, \tfrac12, 0) \),
\[
\sin\theta \le \frac{\norm{\E\e_1}}{\delta} = \frac{1/2}{3 - \sqrt2/2} \approx 0.218 .
\]
The gain over (b) comes from \( \norm{\E\e_1} = \tfrac12 \) replacing \( \norm{\E}_2 \approx 0.707 \). Since \( \sin 13^\circ \approx 0.225 > 0.218 \) and \( \sin \) increases on \( [0, \pi/2] \), the angle is less than \( 13^\circ \).

(d) \( \widetilde{\A} - 2\I = \begin{psmallmatrix} 3 & 1/2 & 0 \\ 1/2 & 0 & 1/2 \\ 0 & 1/2 & -3 \end{psmallmatrix} \) sends \( (1, -6, -1) \) to \( (3 - 3,\ \tfrac12 - \tfrac12,\ -3 + 3) = \0 \), so \( 2 \) is an eigenvalue. The other two have sum \( \tr\widetilde{\A} - 2 = 4 \) and product \( \det\widetilde{\A}/2 \), where expanding along the first row gives \( \det\widetilde{\A} = 5(-2 - \tfrac14) - \tfrac12(-\tfrac12) = -11 \). So they are the roots of \( t^2 - 4t - \tfrac{11}{2} \), namely \( 2 \pm \sqrt{19/2} \approx 5.082, -1.082 \). The exact separation of \( \{2, 2 - \sqrt{19/2}\} \) from \( 5 \) is \( 3 \), and the bound becomes \( \tfrac{1/2}{3} = \tfrac16 \approx 0.167 \). (A direct computation of \( \widetilde{\x} \) gives \( \sin\theta \approx 0.163 \).)
:::

:::: {#exr-davis-kahan-b2}
[B2: Which theorem applies?]

In each case \( \A \) and \( \widetilde{\A} \) are Hermitian \( 4 \times 4 \) matrices, \( k = 2 \), \( \vLambda_1 \) lists the eigenvalues of \( \A \) belonging to \( \Q_1 \), \( \widetilde{\vLambda}_2 \) lists the eigenvalues of \( \widetilde{\A} \) belonging to \( \widetilde{\Q}_2 \), and \( \norm{\E\Q_1}_2 = 0.2 \), \( \norm{\E\Q_1}_F = 0.25 \). Determine which of @thm-davis-kahan-frobenius and @thm-davis-kahan-one-sided apply, and give the best bound on \( \sin\theta_k \) that they yield. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \vLambda_1 = \diag(3, 2) \), \( \widetilde{\vLambda}_2 = \diag(0.4, -1) \).
2. \( \vLambda_1 = \diag(3, 0) \), \( \widetilde{\vLambda}_2 = \diag(1.9, 5) \).
3. \( \vLambda_1 = \diag(2, 1) \), \( \widetilde{\vLambda}_2 = \diag(2, -1) \).
4. \( \vLambda_1 = \diag(-1, -2) \), \( \widetilde{\vLambda}_2 = \diag(0.5, 4) \).
:::
::::

::: {.solution}
(a) Every eigenvalue in \( \vLambda_1 \) is \( \ge 2 \) and both in \( \widetilde{\vLambda}_2 \) are \( \le 0.4 = 2 - 1.6 \). So case (i) of the one-sided theorem holds with \( a = 2 \), \( \delta = 1.6 \), and \( \sin\theta_2 \le 0.2/1.6 = 0.125 \). The Frobenius theorem also applies, with the smallest of the four differences, \( \delta = 2 - 0.4 = 1.6 \), but gives only \( \sin\theta_2 \le \norm{\sin\Theta}_F \le 0.25/1.6 \approx 0.156 \).

(b) The value \( 1.9 \) lies **between** \( 0 \) and \( 3 \), so no point has one list entirely above it and the other entirely below, and the one-sided theorem does not apply. The Frobenius theorem applies with \( \delta = \min(1.1, 1.9, 2, 5) = 1.1 \), the four differences being \( \lvert 1.9 - 3\rvert \), \( \lvert 1.9 - 0\rvert \), \( \lvert 5 - 3\rvert \) and \( \lvert 5 - 0\rvert \). It gives \( \sin\theta_2 \le \norm{\sin\Theta}_F \le 0.25/1.1 \approx 0.227 \).

(c) \( \lvert 2 - 2\rvert = 0 \), so no \( \delta > 0 \) exists and **neither** theorem applies. The check after @lem-davis-kahan-identity shows why nothing can be said in general: an eigenvalue of \( \widetilde{\A} \) outside the subspace coincides with one of \( \A \) inside it, and then the equation need not determine \( \X \).

(d) Every eigenvalue in \( \vLambda_1 \) is \( \le -1 \) and both in \( \widetilde{\vLambda}_2 \) are \( \ge 0.5 = -1 + 1.5 \), so case (ii) holds with \( a = -1 \) and \( \delta = 1.5 \): \( \sin\theta_2 \le 0.2/1.5 \approx 0.133 \). The Frobenius theorem, with \( \delta = 0.5 - (-1) = 1.5 \) again, gives \( 0.25/1.5 \approx 0.167 \).
:::

:::: {#exr-davis-kahan-b3}
[B3: The same bounds for the projections]

In the setting of @thm-davis-kahan-frobenius, let \( U = \col(\Q_1) \) and \( W = \col(\widetilde{\Q}_1) \), with orthogonal projections \( P_U \) and \( P_W \). Prove that
\[
\norm{P_U - P_W}_F \le \frac{\sqrt2\,\norm{\E\Q_1}_F}{\delta},
\]
and that under the hypotheses of @thm-davis-kahan-one-sided, \( \norm{P_U - P_W}_2 \le \norm{\E\Q_1}_2/\delta \).
::::

::: {.solution}
Both subspaces have dimension \( k \), so @thm-projection-difference-norm applies: \( \norm{P_U - P_W}_F = \sqrt2\,\norm{\sin\Theta}_F \) and \( \norm{P_U - P_W}_2 = \sin\theta_k \). By @thm-davis-kahan-frobenius, \( \sqrt2\,\norm{\sin\Theta}_F \le \sqrt2\,\norm{\E\Q_1}_F/\delta \), which is the first claim. By @thm-davis-kahan-one-sided, \( \sin\theta_k \le \norm{\E\Q_1}_2/\delta \), which is the second.
:::

### C. Going deeper

:::: {#exr-davis-kahan-c1}
[C1: A bound that needs only the perturbed matrix]

Let \( \widetilde{\A} \in M_n(\nC) \) be Hermitian with \( \widetilde{\Q} = \begin{pmatrix} \widetilde{\Q}_1 & \widetilde{\Q}_2 \end{pmatrix} \) and \( \widetilde{\vLambda}_2 \) as in the text. Let \( \Z \in M_{n \times k}(\nC) \) be **any** matrix with orthonormal columns, not necessarily eigenvectors of anything, and put
\[
\M = \Z^{*}\widetilde{\A}\Z \in M_k(\nC),
\qquad
\R = \widetilde{\A}\Z - \Z\M .
\]

::: {.enumerate options="label=(\alph*)"}
1. Prove that if every eigenvalue of the Hermitian matrix \( \M \) differs from every diagonal entry of \( \widetilde{\vLambda}_2 \) by at least \( \delta > 0 \), then the principal angles between \( \col(\Z) \) and \( \col(\widetilde{\Q}_1) \) satisfy \( \norm{\sin\Theta}_F \le \norm{\R}_F/\delta \).
2. Deduce: let \( \lambda_i(\widetilde{\A}) \) be a **simple** eigenvalue of \( \widetilde{\A} \), let \( \z \) be a unit vector, \( \mu = \z^{*}\widetilde{\A}\z \) and \( \r = \widetilde{\A}\z - \mu\z \). If every eigenvalue of \( \widetilde{\A} \) other than \( \lambda_i(\widetilde{\A}) \) lies at distance at least \( \delta \) from \( \mu \), then a unit eigenvector \( \widetilde{\x} \) for \( \lambda_i(\widetilde{\A}) \) satisfies \( \sin\theta(\z, \widetilde{\x}) \le \norm{\r}/\delta \).
:::

*Hint: diagonalize \( \M \) and compute \( \widetilde{\Q}_2^{*}\R \) in two ways.*
::::

::: {.solution}
(a) \( \M^{*} = \Z^{*}\widetilde{\A}^{*}\Z = \M \), so by @cor-spectral-complex-matrix and @thm-self-adjoint-real-eigenvalues, \( \M = \V\D\V^{*} \) with \( \V \in M_k(\nC) \) unitary and \( \D \) real diagonal, holding the eigenvalues of \( \M \). Put \( \Z' = \Z\V \), which has orthonormal columns, since \( \Z'^{*}\Z' = \V^{*}\V = \I_k \), and the same column space as \( \Z \), since \( \V \) is invertible. Then \( \R\V = \widetilde{\A}\Z' - \Z\V\D = \widetilde{\A}\Z' - \Z'\D \). As in the proof of @lem-davis-kahan-identity, \( \widetilde{\Q}_2^{*}\widetilde{\A} = \widetilde{\vLambda}_2\widetilde{\Q}_2^{*} \), so with \( \X' = \widetilde{\Q}_2^{*}\Z' \),
\[
\widetilde{\Q}_2^{*}\R\V = \widetilde{\vLambda}_2\X' - \X'\D .
\]
Both coefficient matrices are real diagonal, hence normal, and their diagonal entries differ by at least \( \delta \), so, as in the proof of @thm-davis-kahan-frobenius, @thm-sep-normal and @prp-sep-properties (d) give \( \norm{\X'}_F \le \norm{\widetilde{\Q}_2^{*}\R\V}_F/\delta \). By @lem-spectral-frobenius-toolkit (c), \( \norm{\widetilde{\Q}_2^{*}\R\V}_F \le \norm{\R\V}_F = \norm{\R}_F \). Finally, by @thm-sines-of-principal-angles applied as in @lem-davis-kahan-identity, with \( \col(\Z') = \col(\Z) \) in place of \( \col(\Q_1) \), \( \norm{\X'}_F = \norm{\sin\Theta}_F \). This proves (a).

(b) Take \( k = 1 \) and \( \Z = \z \). Then \( \M = (\mu) \), \( \R = \r \), and the only eigenvalue of \( \M \) is \( \mu \). Since \( \lambda_i(\widetilde{\A}) \) is simple, its eigenspace is the line \( \Span(\widetilde{\x}) \), so we may choose \( \widetilde{\Q} \) with first column \( \widetilde{\x} \) and \( \widetilde{\vLambda}_2 \) holding the other eigenvalues of \( \widetilde{\A} \), as in the proof of @cor-eigenvector-perturbation. Part (a) gives \( \sin\theta(\z, \widetilde{\x}) \le \norm{\r}/\delta \). This is the eigenvector companion of a residual bound: everything on the right is computable from \( \z \) and \( \widetilde{\A} \) and a gap estimate, with no unperturbed matrix in sight.
:::

:::: {#exr-davis-kahan-c2}
[C2: The constant in the eigenvector bound is sharp]

Let \( g > 0 \) and \( e > 0 \), and let \( \A = \diag(g, 0) \), \( \E = e\begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Show that a unit eigenvector \( \widetilde{\x} \) of \( \A + \E \) for its larger eigenvalue makes an angle \( \theta \in [0, \pi/4) \) with \( \e_1 \) satisfying \( \tan 2\theta = 2e/g \).
2. Deduce that \( \sin\theta \cdot g/e \to 1 \) as \( e \to 0^{+} \).
3. Hence show that for no constant \( c < 1 \) is it true that \( \sin\theta(\x, \widetilde{\x}) \le c\,\norm{\E}_2/\gamma \) for all sufficiently small Hermitian \( \E \), in the setting of @cor-eigenvector-perturbation.
:::
::::

::: {.solution}
(a) The larger eigenvalue of \( \widetilde{\A} = \begin{psmallmatrix} g & e \\ e & 0 \end{psmallmatrix} \) is \( \lambda_+ = h + s \), where \( h = g/2 \) and \( s = \sqrt{h^2 + e^2} \). The first row of \( \widetilde{\A} - \lambda_+\I \) is \( (g - \lambda_+, e) = (h - s, e) \), so \( (e, s - h) \) spans the eigenline, and \( s - h > 0 \). The angle with \( \e_1 \) therefore satisfies \( \tan\theta = t \coloneqq (s - h)/e > 0 \). Using \( s^2 = h^2 + e^2 \),
\[
1 - t^2 = \frac{e^2 - (s - h)^2}{e^2} = \frac{2h(s - h)}{e^2} > 0 ,
\]
so \( t < 1 \), that is \( \theta < \pi/4 \), and
\[
\begin{aligned}
\tan 2\theta = \frac{2t}{1 - t^2}
&= \frac{2(s - h)}{e}\cdot\frac{e^2}{2h(s - h)} \\
&= \frac{e}{h} = \frac{2e}{g} .
\end{aligned}
\]

(b) From (a), \( \cos 2\theta = 1/\sqrt{1 + \tan^2 2\theta} = g/\sqrt{g^2 + 4e^2} \), since \( 2\theta \in [0, \pi/2) \). Hence
\[
\begin{aligned}
\sin^2\theta = \frac{1 - \cos 2\theta}{2}
&= \frac{\sqrt{g^2 + 4e^2} - g}{2\sqrt{g^2 + 4e^2}} \\
&= \frac{2e^2}{\sqrt{g^2 + 4e^2}\,\bigl(\sqrt{g^2 + 4e^2} + g\bigr)} ,
\end{aligned}
\]
multiplying above and below by \( \sqrt{g^2 + 4e^2} + g \). So
\[
\Bigl(\frac{g\sin\theta}{e}\Bigr)^2 = \frac{2g^2}{\sqrt{g^2 + 4e^2}\,\bigl(\sqrt{g^2 + 4e^2} + g\bigr)} ,
\]
which tends to \( 2g^2/(g \cdot 2g) = 1 \) as \( e \to 0^{+} \), by continuity of the square root.

(c) Here \( \x = \e_1 \), \( \gamma = g \), and \( \norm{\E}_2 = e \), since \( \E/e \) is Hermitian with eigenvalues \( \pm1 \). If \( \sin\theta \le c\,e/g \) held for all small \( e > 0 \) with some \( c < 1 \), then \( \sin\theta \cdot g/e \le c \) for those \( e \), contradicting (b). So to first order in \( \norm{\E}_2 \), the bound \( \norm{\E}_2/(\gamma - \norm{\E}_2) \) of @cor-eigenvector-perturbation cannot be improved by any constant factor.
:::
