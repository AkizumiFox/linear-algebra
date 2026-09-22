# Singular Values and Polar Factors

Chapter 16 §09 proved that singular values are perfectly conditioned: \( \lvert\sigma_i(\A + \E) - \sigma_i(\A)\rvert \le \norm{\E}_2 \), for any matrices at all. This section finishes that story and then starts a new one. First the Frobenius-norm version, Mirsky's theorem, which follows from Section 5's Hoffman–Wielandt inequality once the Hermitian dilation of Chapter 16 turns singular values into eigenvalues. Then the polar decomposition \( \A = \U\P \): how far do the unitary factor and the positive factor move when \( \A \) does? Both answers come from one tool used twice, the bound of Section 7 for a Sylvester equation with positive coefficients.

**Throughout**, the field is \( \nC \), \( \norm{\cdot}_2 \) is the spectral norm and \( \norm{\cdot}_F \) the Frobenius norm, and @lem-spectral-frobenius-toolkit of Section 9 is used freely to move unitary factors and conjugate transposes in and out of either norm. For \( \A \in M_{m \times n}(\nC) \) we put \( p = \min(m, n) \), and \( \sigma_1(\A) \ge \dots \ge \sigma_p(\A) \ge 0 \) are its singular values (@def-singular-values).

## Singular values in the Frobenius norm

Here is where Chapter 16 left the question. Its @cor-singular-value-perturbation says that for **any** \( \A, \E \in M_{m \times n}(\nC) \),
\[
\lvert\sigma_i(\A + \E) - \sigma_i(\A)\rvert \le \norm{\E}_2
\qquad (1 \le i \le p) ,
\]
with no symmetry, squareness or smallness assumed. In the language of Section 5 this is a bound on the largest entry of the vector of differences, and the matching is simply by index. What it does not give is a good bound on **all** the differences together. Squaring and adding \( p \) copies of it gives
\[
\sum_{i=1}^{p}\bigl(\sigma_i(\A + \E) - \sigma_i(\A)\bigr)^2 \le p\,\norm{\E}_2^2 ,
\]
and the factor \( p \) grows with the size of the matrices. For Hermitian eigenvalues, Section 5 removed that factor: @cor-hoffman-wielandt-hermitian bounds the sum of squares by \( \norm{\E}_F^2 \), with no dependence on \( n \). Chapter 16 recorded, in @prp-hermitian-dilation, a device for carrying any theorem about Hermitian eigenvalues over to singular values, and promised that this chapter would lean on it. Here it is.

::: {#thm-mirsky-frobenius}
[Mirsky's Theorem]

Let \( \A, \B \in M_{m \times n}(\nC) \) and \( p = \min(m, n) \). Then
\[
\sum_{i=1}^{p}\bigl(\sigma_i(\A) - \sigma_i(\B)\bigr)^2 \ \le\ \norm{\A - \B}_F^2 .
\]
:::

::: {.idea}
Replace each matrix by its Hermitian dilation \( \cH(\cdot) \), whose eigenvalues are \( \pm\sigma_i \) and zeros. Listed decreasingly, the eigenvalues of \( \cH(\A) \) are \( \sigma_1(\A), \dots, \sigma_p(\A) \), then the zeros, then \( -\sigma_p(\A), \dots, -\sigma_1(\A) \), and the positions depend only on \( m \) and \( n \), so \( \cH(\B) \) has the same pattern. Apply the Hermitian Hoffman–Wielandt inequality to the two dilations. On the left each difference \( \sigma_i(\A) - \sigma_i(\B) \) appears twice, once from the top and once from the bottom, while the zeros cancel against zeros. On the right each entry of \( \A - \B \) appears twice, once in each off-diagonal block. The two factors of \( 2 \) cancel.
:::

::: {.proof}
For \( \M \in M_{m \times n}(\nC) \), \( \cH(\M) = \begin{psmallmatrix} \0 & \M \\ \M^{*} & \0 \end{psmallmatrix} \) is Hermitian (@prp-hermitian-dilation). Since conjugate transposition is additive,
\[
\cH(\A) - \cH(\B) = \begin{pmatrix} \0 & \A - \B \\ (\A - \B)^{*} & \0 \end{pmatrix} = \cH(\A - \B) ,
\]
and since the entries of \( \cH(\M) \) are those of \( \M \), those of \( \M^{*} \) and zeros,
\[
\norm{\cH(\M)}_F^2 = \norm{\M}_F^2 + \norm{\M^{*}}_F^2 = 2\norm{\M}_F^2 .
\]{#eq-dilation-frobenius}

By @prp-hermitian-dilation, the eigenvalues of \( \cH(\A) \in M_{m+n}(\nC) \), with multiplicity, are \( \pm\sigma_1(\A), \dots, \pm\sigma_p(\A) \) together with \( m + n - 2p \) zeros. Since every \( \sigma_i(\A) \ge 0 \), the list
\[
\begin{aligned}
&\sigma_1(\A) \ge \dots \ge \sigma_p(\A) \ \ge\ \underbrace{0 \ge \dots \ge 0}_{m+n-2p} \\
&\qquad \ge\ -\sigma_p(\A) \ge \dots \ge -\sigma_1(\A)
\end{aligned}
\]
is decreasing, and a multiset of real numbers has only one decreasing listing. So, with \( N = m + n \),
\[
\lambda_i(\cH(\A)) =
\begin{cases}
\sigma_i(\A) & 1 \le i \le p, \\
0 & p < i \le N - p, \\
-\sigma_{N+1-i}(\A) & N - p < i \le N .
\end{cases}
\]
The same formula holds for \( \B \), with the **same** three ranges of \( i \), because \( m \), \( n \) and \( p \) are the same. Hence, summing over the three ranges, and writing \( j = N + 1 - i \) in the third,
\[
\begin{aligned}
\sum_{i=1}^{N}\bigl(\lambda_i(\cH(\A)) - \lambda_i(\cH(\B))\bigr)^2
&= \sum_{i=1}^{p}\bigl(\sigma_i(\A) - \sigma_i(\B)\bigr)^2 + 0 \\
&\qquad + \sum_{j=1}^{p}\bigl(-\sigma_j(\A) + \sigma_j(\B)\bigr)^2 \\
&= 2\sum_{i=1}^{p}\bigl(\sigma_i(\A) - \sigma_i(\B)\bigr)^2 .
\end{aligned}
\]
By @cor-hoffman-wielandt-hermitian, applied to the Hermitian matrices \( \cH(\A) \) and \( \cH(\B) \), the left-hand side is at most \( \norm{\cH(\A) - \cH(\B)}_F^2 = \norm{\cH(\A - \B)}_F^2 = 2\norm{\A - \B}_F^2 \), by @eq-dilation-frobenius. Dividing by \( 2 \) proves the theorem.
:::

This is the payment Chapter 16 §09 promised when it said that Chapter 19 leans on the dilation for perturbation bounds. Together with @cor-singular-value-perturbation, it bounds the vector of singular-value differences in the two norms one reaches for first: its largest entry by \( \norm{\A - \B}_2 \), its Euclidean length by \( \norm{\A - \B}_F \). Chapter 20 puts both inside one statement covering every unitarily invariant norm.

Note what was **not** assumed. @thm-hoffman-wielandt needs normal matrices, and Section 5 showed by a Jordan-block pair that it fails without normality. Mirsky's theorem holds for every pair of matrices, square or not, because the dilation manufactures the Hermitian hypothesis instead of assuming it.

::: {#exm-mirsky-one-entry}
[Two matrices that differ in one entry]

Let \( \A = \begin{psmallmatrix} 2 & 1 \\ 1 & 2 \end{psmallmatrix} \) and \( \B = \begin{psmallmatrix} 2 & 1 \\ 0 & 2 \end{psmallmatrix} \). Compute the singular values of both, and compare the two sides of @thm-mirsky-frobenius with what @cor-singular-value-perturbation alone would give.
:::

::: {.solution}
\( \A \) is symmetric with \( \A(1,1) = 3(1,1) \) and \( \A(1,-1) = (1,-1) \), so \( \A\tp\A = \A^2 \) has eigenvalues \( 9 \) and \( 1 \), and \( \sigma(\A) = (3, 1) \). For \( \B \),
\[
\B\tp\B = \begin{pmatrix} 4 & 2 \\ 2 & 5 \end{pmatrix},
\]
with trace \( 9 \) and determinant \( 16 \), so its eigenvalues are \( \tfrac{9 \pm \sqrt{17}}{2} \). These are perfect squares: \( \bigl(\tfrac{\sqrt{17} \pm 1}{2}\bigr)^2 = \tfrac{18 \pm 2\sqrt{17}}{4} = \tfrac{9 \pm \sqrt{17}}{2} \). Hence
\[
\sigma_1(\B) = \tfrac{\sqrt{17} + 1}{2} \approx 2.562,
\qquad
\sigma_2(\B) = \tfrac{\sqrt{17} - 1}{2} \approx 1.562 .
\]
The difference \( \A - \B = \begin{psmallmatrix} 0 & 0 \\ 1 & 0 \end{psmallmatrix} \) has \( \norm{\A - \B}_F = \norm{\A - \B}_2 = 1 \). The left side of Mirsky's inequality is
\[
\Bigl(\tfrac{5 - \sqrt{17}}{2}\Bigr)^2 + \Bigl(\tfrac{3 - \sqrt{17}}{2}\Bigr)^2
= \tfrac{(42 - 10\sqrt{17}) + (26 - 6\sqrt{17})}{4}
= 17 - 4\sqrt{17} \approx 0.508 ,
\]
comfortably below \( 1 \). The index-by-index bound gives \( \lvert\sigma_i(\A) - \sigma_i(\B)\rvert \le 1 \) for each \( i \); the actual values are about \( 0.438 \) and \( 0.562 \). On its own it bounds the sum of squares only by \( 2 \), and Mirsky halves that.
:::

::: {.check}
Let \( \A = \diag(3, 1) \) and \( \B = \diag(1, 3) \). Compute both sides of @thm-mirsky-frobenius. Why is the left side not \( (3 - 1)^2 + (1 - 3)^2 \)?
:::

::: {.solution}
Both matrices have singular values \( (3, 1) \) in decreasing order, so the left side is \( 0 \), while \( \norm{\A - \B}_F^2 = \norm{\diag(2, -2)}_F^2 = 8 \). The theorem compares the **sorted** lists, the \( i \)-th largest with the \( i \)-th largest. Pairing the diagonal entries by position would give \( 8 \), which is also allowed, but it is not what the theorem measures.
:::

::: {.warning}
**Stable singular values do not mean stable singular vectors.** Take \( 0 < \eta < 1 \), \( \A = \diag(1 + \eta, 1 - \eta) \) and \( \B = \begin{psmallmatrix} 1 & \eta \\ \eta & 1 \end{psmallmatrix} \), the pair of @exm-davis-kahan-small-gap. Both are positive definite with eigenvalues \( 1 \pm \eta \), so both have singular values \( 1 \pm \eta \), and the left side of Mirsky's inequality is \( 0 \). But the right singular vector for \( \sigma_1 \) is \( \e_1 \) for \( \A \) and \( \tfrac{1}{\sqrt2}(1, 1) \) for \( \B \), a \( 45^\circ \) turn, while \( \norm{\A - \B}_F = 2\eta \) is as small as we like. As with eigenvectors, singular vectors are controlled by gaps. Applying Section 9 to the dilations \( \cH(\A) \) and \( \cH(\B) \), whose eigenvectors are built from the singular vectors, is one way to bound them.
:::

## The square root is Lipschitz away from zero

The second half of the section is about the polar decomposition, and its positive factor is a square root, \( \lvert\A\rvert = (\A^{*}\A)^{1/2} \). So we start with square roots.

For positive numbers there is an exact formula for how far a square root moves:
\[
\sqrt{p} - \sqrt{q} = \frac{p - q}{\sqrt{p} + \sqrt{q}} ,
\]
the usual trick of multiplying by the conjugate. It shows that the square root is Lipschitz on \( [c, \infty) \) with constant \( 1/(2\sqrt{c}) \), and that no constant works near \( 0 \). For matrices the trick fails as written: with \( \S = \P^{1/2} \) and \( \T = \Q^{1/2} \), the product \( (\S - \T)(\S + \T) = \S^2 + \S\T - \T\S - \T^2 \) is \( \P - \Q \) only when \( \S \) and \( \T \) commute. But a different grouping of the same terms works with no commuting at all:
\[
\S(\S - \T) + (\S - \T)\T = \S^2 - \S\T + \S\T - \T^2 = \P - \Q .
\]{#eq-sqrt-sylvester}
This says that \( \X = \S - \T \) solves the Sylvester equation \( \S\X + \X\T = \P - \Q \), whose coefficients are positive definite. That is exactly the situation of @cor-positive-sylvester.

::: {#thm-sqrt-perturbation}
[Perturbation of the Square Root]

Let \( \P, \Q \in M_n(\nC) \) be positive definite. Then
\[
\norm{\P^{1/2} - \Q^{1/2}} \ \le\ \frac{\norm{\P - \Q}}{\lambda_n(\P)^{1/2} + \lambda_n(\Q)^{1/2}} ,
\]
where \( \norm{\cdot} \) is either \( \norm{\cdot}_2 \) or \( \norm{\cdot}_F \).
:::

::: {.proof}
Put \( \S = \P^{1/2} \) and \( \T = \Q^{1/2} \), the positive square roots of @thm-psd-square-root. By that theorem the eigenvalues of \( \S \) are the non-negative square roots of those of \( \P \), and \( t \mapsto \sqrt{t} \) is increasing, so the smallest eigenvalue of \( \S \) is \( \alpha \coloneqq \lambda_n(\P)^{1/2} \), which is positive because \( \P \succ 0 \). Every eigenvalue of the Hermitian matrix \( \S - \alpha\I \) is therefore non-negative, so \( \S \succeq \alpha\I \) by @thm-psd-characterizations (b). In the same way \( \T \succeq \beta\I \) with \( \beta \coloneqq \lambda_n(\Q)^{1/2} > 0 \).

By @eq-sqrt-sylvester, \( \X = \S - \T \) satisfies \( \S\X + \X\T = \P - \Q \). Since \( \alpha + \beta > 0 \), @cor-positive-sylvester applies to this equation, whose solution is therefore unique and equal to \( \X \), and gives
\[
\norm{\S - \T} \le \frac{\norm{\P - \Q}}{\alpha + \beta}
\]
in both the spectral and the Frobenius norm. This proves the theorem.
:::

For \( n = 1 \) this is the scalar identity, as an inequality that happens to be an equality. It is sharp for every \( n \): with \( \P = \diag(4, 100) \) and \( \Q = \diag(1, 100) \), \( \P^{1/2} - \Q^{1/2} = \diag(1, 0) \) has both norms equal to \( 1 \), and the bound is \( 3/(2 + 1) = 1 \); padding both matrices with a further block \( 100\,\I_{n-2} \) changes neither side of the inequality, so the equality holds for every \( n \ge 2 \). The difference sits exactly in the direction where both matrices are smallest, which is the worst place for it.

::: {.remark}
The proof used only \( \alpha + \beta > 0 \), so the conclusion holds as soon as one of \( \P \) and \( \Q \) is positive definite and the other positive semidefinite.
:::

::: {.warning}
**The square root is not Lipschitz on all positive semidefinite matrices.** Take \( \P = \varepsilon\I_n \) with \( 0 < \varepsilon < 1 \) and \( \Q = \0 \). Then \( \norm{\P - \Q}_2 = \varepsilon \), while \( \P^{1/2} - \Q^{1/2} = \sqrt{\varepsilon}\,\I_n \) has spectral norm \( \sqrt{\varepsilon} \), which is larger by the factor \( 1/\sqrt{\varepsilon} \). That factor is unbounded as \( \varepsilon \to 0^{+} \), so no inequality \( \norm{\P^{1/2} - \Q^{1/2}}_2 \le C\norm{\P - \Q}_2 \) can hold for all \( \P, \Q \succeq 0 \). The denominator of the theorem is what records this. By the remark the theorem still applies, with denominator \( \sqrt{\varepsilon} + 0 \), and the bound \( \varepsilon/\sqrt{\varepsilon} = \sqrt{\varepsilon} \) is attained. @exr-singular-values-and-polar-c1 shows that the square root is nevertheless continuous everywhere, with a square-root modulus.
:::

## The positive polar factor

Recall @thm-polar-decomposition: every \( \A \in M_n(\nC) \) is a unitary matrix times the positive semidefinite \( \lvert\A\rvert = (\A^{*}\A)^{1/2} \), and when \( \A \) is invertible both factors are unique. In this section we write the decomposition as
\[
\A = \U\P, \qquad \U \text{ unitary}, \qquad \P = \lvert\A\rvert ,
\]
keeping the letter \( \W \) for another use below. For invertible \( \A \) the matrix \( \A^{*}\A \) is positive definite, since \( \x^{*}\A^{*}\A\x = \norm{\A\x}^2 > 0 \) for \( \x \ne \0 \). Its eigenvalues are the \( \sigma_i(\A)^2 \) (@def-singular-values), so
\[
\lambda_n(\A^{*}\A) = \sigma_n(\A)^2 > 0,
\qquad
\P = \lvert\A\rvert \succeq \sigma_n(\A)\,\I ,
\]
the second because the eigenvalues of \( \lvert\A\rvert \) are the square roots \( \sigma_i(\A) \) (@thm-psd-square-root) and @thm-psd-characterizations (b) applies to \( \lvert\A\rvert - \sigma_n(\A)\I \) as before.

::: {#thm-polar-positive-perturbation}
[Perturbation of the Positive Polar Factor]

Let \( \A, \B \in M_n(\nC) \) be invertible. Then
\[
\norm{\,\lvert\A\rvert - \lvert\B\rvert\,} \ \le\ \frac{\bigl(\norm{\A}_2 + \norm{\B}_2\bigr)\,\norm{\A - \B}}{\sigma_n(\A) + \sigma_n(\B)} ,
\]
where \( \norm{\cdot} \) is either \( \norm{\cdot}_2 \) or \( \norm{\cdot}_F \).
:::

::: {.proof}
Both \( \A^{*}\A \) and \( \B^{*}\B \) are positive definite, with \( \lambda_n(\A^{*}\A)^{1/2} = \sigma_n(\A) \) and \( \lambda_n(\B^{*}\B)^{1/2} = \sigma_n(\B) \), as just shown. So @thm-sqrt-perturbation gives
\[
\norm{\,\lvert\A\rvert - \lvert\B\rvert\,} \le \frac{\norm{\A^{*}\A - \B^{*}\B}}{\sigma_n(\A) + \sigma_n(\B)} .
\]
Now \( \A^{*}\A - \B^{*}\B = \A^{*}(\A - \B) + (\A - \B)^{*}\B \), as expanding the right side shows. By @lem-spectral-frobenius-toolkit (b) and (a),
\[
\norm{\A^{*}(\A - \B)} \le \norm{\A^{*}}_2\norm{\A - \B} = \norm{\A}_2\norm{\A - \B},
\]
and likewise \( \norm{(\A - \B)^{*}\B} \le \norm{(\A - \B)^{*}}\,\norm{\B}_2 = \norm{\A - \B}\,\norm{\B}_2 \). The triangle inequality for the norm (@thm-operator-norm-properties (b) for \( \norm{\cdot}_2 \), @cor-triangle-inequality for the Frobenius norm, which is induced by an inner product) gives \( \norm{\A^{*}\A - \B^{*}\B} \le (\norm{\A}_2 + \norm{\B}_2)\norm{\A - \B} \), and substituting proves the theorem.
:::

When \( \B \) is close to \( \A \), the constant is about \( 2\norm{\A}_2/(2\sigma_n(\A)) = \kappa_2(\A) \), the condition number of Chapter 15. So by this estimate \( \lvert\A\rvert \) is as sensitive as \( \A \) is ill-conditioned. It is a crude estimate, as the example below shows. Sharper ones are known, but this is the one the Sylvester bound gives with no extra work.

## The unitary polar factor

For a non-zero complex number, the unitary polar factor is the phase \( z/\lvert z\rvert \). If two numbers \( z \) and \( w \) have the same modulus \( r \), their phases differ by exactly \( \lvert z - w\rvert/r \). So the phase moves at the rate of the perturbation divided by the modulus, and it is undefined at \( z = 0 \). The theorem below is the matrix form of this, with \( \sigma_n \) as the modulus.

::: {#thm-polar-unitary-perturbation}
[Perturbation of the Unitary Polar Factor]

Let \( \A, \B \in M_n(\nC) \) be invertible, with polar decompositions (@thm-polar-decomposition) \( \A = \U\P \) and \( \B = \V\Q \), where \( \U, \V \) are unitary, \( \P = \lvert\A\rvert \) and \( \Q = \lvert\B\rvert \). Then
\[
\norm{\U - \V} \ \le\ \frac{2\,\norm{\A - \B}}{\sigma_n(\A) + \sigma_n(\B)} ,
\]
where \( \norm{\cdot} \) is either \( \norm{\cdot}_2 \) or \( \norm{\cdot}_F \).
:::

::: {.idea}
Measure \( \U \) against \( \V \) by the single unitary matrix \( \W = \V^{*}\U \), which equals \( \I \) exactly when \( \U = \V \); then \( \norm{\U - \V} = \norm{\W - \I} \). Now write \( \A - \B \) in the two polar frames. Seen through \( \V^{*} \) on the left it is \( \W\P - \Q \). Its conjugate transpose, seen through \( \U \) on the right, is \( \P - \Q\W \). The difference of these two expressions is \( (\W - \I)\P + \Q(\W - \I) \), a Sylvester equation for \( \W - \I \) with positive definite coefficients \( \Q \) and \( \P \), and its right-hand side has norm at most \( 2\norm{\A - \B} \).
:::

::: {.proof}
Put \( \W = \V^{*}\U \), which is unitary. Since \( \U^{*}\U = \V^{*}\V = \I \), \( \P^{*} = \P \) and \( \Q^{*} = \Q \),
\[
\begin{aligned}
\V^{*}(\A - \B) &= \V^{*}\U\P - \V^{*}\V\Q = \W\P - \Q, \\
(\A - \B)^{*}\U &= \P\U^{*}\U - \Q\V^{*}\U = \P - \Q\W .
\end{aligned}
\]
Subtracting the second identity from the first,
\[
\begin{aligned}
\V^{*}(\A - \B) - (\A - \B)^{*}\U
&= \W\P - \P + \Q\W - \Q \\
&= \Q(\W - \I) + (\W - \I)\P .
\end{aligned}
\]{#eq-polar-factor-identity}
So \( \X = \W - \I \) solves \( \Q\X + \X\P = \Y \), with \( \Y \) the left side of @eq-polar-factor-identity. As shown before @thm-polar-positive-perturbation, \( \Q \succeq \sigma_n(\B)\I \) and \( \P \succeq \sigma_n(\A)\I \), and \( \sigma_n(\A) + \sigma_n(\B) > 0 \). So @cor-positive-sylvester, applied with \( \Q \) and \( \P \) as its two coefficients, gives
\[
\norm{\W - \I} \le \frac{\norm{\Y}}{\sigma_n(\A) + \sigma_n(\B)}
\]
in both norms. By @lem-spectral-frobenius-toolkit (c) and (a), \( \norm{\V^{*}(\A - \B)} = \norm{\A - \B} \) and \( \norm{(\A - \B)^{*}\U} = \norm{(\A - \B)^{*}} = \norm{\A - \B} \), so \( \norm{\Y} \le 2\norm{\A - \B} \) by the triangle inequality in either norm (@thm-operator-norm-properties (b), @cor-triangle-inequality). Finally \( \U - \V = \V(\V^{*}\U - \I) = \V(\W - \I) \), so \( \norm{\U - \V} = \norm{\W - \I} \) by @lem-spectral-frobenius-toolkit (c). Combining the three displays proves the theorem.
:::

Notice the difference from @thm-polar-positive-perturbation. There the constant was a condition number, but here only \( \sigma_n \) appears. The unitary factor feels how close \( \A \) is to the singular matrices, which is \( \sigma_n(\A) \) by @cor-distance-to-singular, and nothing else.

::: {.check}
For \( n = 1 \), what does the theorem say about two non-zero complex numbers \( z \) and \( w \)? Test it on \( z = 1 \), \( w = -1 \).
:::

::: {.solution}
A non-zero \( z \in \nC = M_1(\nC) \) has polar decomposition \( z = \tfrac{z}{\lvert z\rvert}\cdot\lvert z\rvert \), with \( \sigma_1(z) = \lvert z\rvert \), and both norms are the modulus. So the theorem says
\[
\Bigl\lvert\frac{z}{\lvert z\rvert} - \frac{w}{\lvert w\rvert}\Bigr\rvert \le \frac{2\lvert z - w\rvert}{\lvert z\rvert + \lvert w\rvert} .
\]
For \( z = 1 \), \( w = -1 \) both sides equal \( 2 \). So the constant \( 2 \) in the theorem cannot be lowered, even for \( n = 1 \).
:::

::: {#exm-polar-factors-nearby}
[The polar factors of two nearby matrices]

Let \( \A = \begin{psmallmatrix} 3 & 0 \\ 4 & 5 \end{psmallmatrix} \), whose polar decomposition @exm-polar-2x2 found to be \( \U = \tfrac{1}{\sqrt5}\begin{psmallmatrix} 2 & -1 \\ 1 & 2 \end{psmallmatrix} \), \( \lvert\A\rvert = \sqrt5\begin{psmallmatrix} 2 & 1 \\ 1 & 2 \end{psmallmatrix} \), with \( \sigma(\A) = (3\sqrt5, \sqrt5) \). Let \( \B = \begin{psmallmatrix} 3 & 0 \\ 6 & 5 \end{psmallmatrix} \). Find the polar decomposition of \( \B \), compute \( \norm{\U - \V} \), and compare it with @thm-polar-unitary-perturbation.
:::

::: {.solution}
*Finding \( \V \).* For a real \( 2 \times 2 \) matrix of positive determinant, look for \( \V \) among the rotations \( \R_{\varphi} = \begin{psmallmatrix} c & -s \\ s & c \end{psmallmatrix} \), with \( c = \cos\varphi \), \( s = \sin\varphi \). For \( \B = (b_{ij}) \), the off-diagonal entries of \( \R_{\varphi}\tp\B \) are \( cb_{12} + sb_{22} \) and \( -sb_{11} + cb_{21} \), and they agree exactly when \( (b_{11} + b_{22})s = (b_{21} - b_{12})c \). For our \( \B \) this reads \( 8s = 6c \), so \( (c, s) = (\tfrac45, \tfrac35) \), and
\[
\begin{aligned}
\V &= \tfrac15\begin{pmatrix} 4 & -3 \\ 3 & 4 \end{pmatrix}, \\
\V\tp\B &= \tfrac15\begin{pmatrix} 4 & 3 \\ -3 & 4 \end{pmatrix}\begin{pmatrix} 3 & 0 \\ 6 & 5 \end{pmatrix} = \begin{pmatrix} 6 & 3 \\ 3 & 4 \end{pmatrix} .
\end{aligned}
\]
This symmetric matrix has trace \( 10 \) and determinant \( 15 \), so both its eigenvalues, \( 5 \pm \sqrt{10} \), are positive, and it is positive definite. Thus \( \B = \V(\V\tp\B) \) is a unitary matrix times a positive definite one. Squaring gives \( (\V\tp\B)^2 = \B\tp\V\V\tp\B = \B\tp\B \), so \( \V\tp\B = \lvert\B\rvert \) by uniqueness of the positive square root (@thm-psd-square-root). Since \( \B \) is invertible, @thm-polar-decomposition now gives \( \V \) as its unitary polar factor. Its singular values are the eigenvalues of \( \lvert\B\rvert \), \( \sigma(\B) = (5 + \sqrt{10}, 5 - \sqrt{10}) \approx (8.162, 1.838) \). The same recipe applied to \( \A \) gives \( 8s = 4c \), which recovers \( \U \).

*The distance.* \( \U \) and \( \V \) are the rotations through angles \( \varphi_{\A} \) and \( \varphi_{\B} \) with
\[
\cos(\varphi_{\B} - \varphi_{\A}) = \tfrac{2}{\sqrt5}\cdot\tfrac45 + \tfrac{1}{\sqrt5}\cdot\tfrac35 = \tfrac{11}{5\sqrt5} .
\]
For two rotations, \( (\U - \V)\tp(\U - \V) = 2\I - (\U\tp\V + \V\tp\U) = \bigl(2 - 2\cos(\varphi_{\B} - \varphi_{\A})\bigr)\I \), so both singular values of \( \U - \V \) equal \( \sqrt{2 - 22/(5\sqrt5)} \) and
\[
\norm{\U - \V}_2 \approx 0.180, \qquad \norm{\U - \V}_F \approx 0.254 .
\]

*The bound.* \( \A - \B = \begin{psmallmatrix} 0 & 0 \\ -2 & 0 \end{psmallmatrix} \), so \( \norm{\A - \B}_2 = \norm{\A - \B}_F = 2 \), and
\[
\frac{2 \cdot 2}{\sigma_2(\A) + \sigma_2(\B)} = \frac{4}{\sqrt5 + 5 - \sqrt{10}} \approx 0.982
\]
in both norms. The theorem holds, with a factor of about \( 5 \) to spare in the spectral norm and \( 4 \) in the Frobenius norm. For the positive factors, @thm-polar-positive-perturbation gives
\[
\norm{\,\lvert\A\rvert - \lvert\B\rvert\,} \le \frac{(3\sqrt5 + 5 + \sqrt{10}) \cdot 2}{\sqrt5 + 5 - \sqrt{10}} \approx 7.30 ,
\]
while \( \lvert\A\rvert - \lvert\B\rvert = \begin{psmallmatrix} 2\sqrt5 - 6 & \sqrt5 - 3 \\ \sqrt5 - 3 & 2\sqrt5 - 4 \end{psmallmatrix} \) has spectral norm about \( 1.79 \) and Frobenius norm about \( 1.93 \). That bound is correct but crude, as promised.
:::

::: {.warning}
**At a singular matrix the unitary factor jumps, and no bound of this kind survives.** For \( 0 < \varepsilon \le 1 \) let
\[
\begin{aligned}
\A_{\varepsilon} &= \diag(1, \varepsilon) = \I\,\diag(1, \varepsilon), \\
\B_{\varepsilon} &= \diag(1, -\varepsilon) = \diag(1, -1)\,\diag(1, \varepsilon) .
\end{aligned}
\]
These are polar decompositions: the unitary factors are \( \U = \I \) and \( \V = \diag(1, -1) \), and both positive factors are \( \diag(1, \varepsilon) \). As \( \varepsilon \to 0^{+} \), both matrices tend to the singular \( \diag(1, 0) \), and \( \norm{\A_{\varepsilon} - \B_{\varepsilon}} = 2\varepsilon \to 0 \) in both norms. Yet \( \U - \V = \diag(0, 2) \) has spectral and Frobenius norm \( 2 \) for every \( \varepsilon \). So the unitary factor has no limit at \( \diag(1, 0) \), and it cannot be chosen continuously there. This matches the non-uniqueness in @thm-polar-decomposition: both \( \I \) and \( \diag(1, -1) \) are unitary polar factors of \( \diag(1, 0) \). The theorem, with \( \sigma_2(\A_{\varepsilon}) = \sigma_2(\B_{\varepsilon}) = \varepsilon \), gives the bound \( (2 \cdot 2\varepsilon)/(2\varepsilon) = 2 \), which is attained. Padding both matrices with an identity block, \( \A_{\varepsilon} \oplus \I_{n-2} \) and \( \B_{\varepsilon} \oplus \I_{n-2} \), gives the same equality for every \( n \ge 2 \): the constant \( 2 \) cannot be improved, and the denominator cannot be dropped.
:::

@cor-unitary-nearest identified the unitary polar factor as the unitary matrix nearest to \( \A \) in the Frobenius norm. @thm-polar-unitary-perturbation adds that for invertible \( \A \) this nearest unitary matrix moves continuously with \( \A \), at a rate no worse than \( 2/(\sigma_n(\A) + \sigma_n(\B)) \). A matrix that has drifted from unitarity can therefore be put back reliably, as long as it stays well away from the singular matrices.

## Exercises

### A. Check your understanding

:::: {#exr-singular-values-and-polar-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State Mirsky's theorem. In its proof by the Hermitian dilation of @prp-hermitian-dilation, where does each of the two factors of \( 2 \) come from?
2. True or false: \( \lvert\sigma_i(\A) - \sigma_i(\B)\rvert \le \norm{\A - \B}_F \) for every \( i \). Justify.
3. True or false: the unitary polar factor is a continuous function of \( \A \) on the invertible matrices, and it extends continuously to all of \( M_n(\nC) \). Justify.
4. Which identity turns the perturbation of a square root into a Sylvester equation, and which result then bounds it?
5. Why does @thm-polar-unitary-perturbation hold in both the spectral and the Frobenius norm?
:::
::::

::: {.solution}
(a) @thm-mirsky-frobenius: \( \sum_{i=1}^{p}(\sigma_i(\A) - \sigma_i(\B))^2 \le \norm{\A - \B}_F^2 \). On the eigenvalue side, each difference \( \sigma_i(\A) - \sigma_i(\B) \) occurs twice in the sorted spectra of the dilations, once as \( \sigma_i \) near the top and once as \( -\sigma_i \) near the bottom. On the norm side, each entry of \( \A - \B \) occurs twice in \( \cH(\A - \B) \), once in \( \A - \B \) and once, conjugated, in \( (\A - \B)^{*} \) (@eq-dilation-frobenius).

(b) True. Every term of the sum in Mirsky's theorem is non-negative, so each one is at most the sum, which is at most \( \norm{\A - \B}_F^2 \). (It also follows from @cor-singular-value-perturbation and \( \norm{\cdot}_2 \le \norm{\cdot}_F \), @prp-spectral-vs-frobenius.)

(c) False as a whole. The first half is true: by @thm-polar-unitary-perturbation, \( \norm{\U - \V}_2 \le 2\norm{\A - \B}_2/(\sigma_n(\A) + \sigma_n(\B)) \), which tends to \( 0 \) as \( \B \to \A \) for fixed invertible \( \A \), because \( \sigma_n(\B) \ge 0 \). The second half is false: in the last warning of the section, \( \A_{\varepsilon} \) and \( \B_{\varepsilon} \) both tend to \( \diag(1, 0) \) while their unitary factors stay at distance \( 2 \), so no value at \( \diag(1, 0) \) makes the factor continuous there.

(d) \( \S(\S - \T) + (\S - \T)\T = \S^2 - \T^2 \) (@eq-sqrt-sylvester), which exhibits \( \S - \T \) as the solution of \( \S\X + \X\T = \P - \Q \). Section 7's @cor-positive-sylvester bounds that solution.

(e) Each step holds in both norms: @cor-positive-sylvester is stated for both, and so are the facts of @lem-spectral-frobenius-toolkit used to remove the unitary factors and conjugate transposes.
:::

### B. Practice

:::: {#exr-singular-values-and-polar-b1}
[B1: Mirsky by hand]

Let \( \A = \begin{psmallmatrix} 3 & 0 \\ 4 & 5 \end{psmallmatrix} \), with \( \sigma(\A) = (3\sqrt5, \sqrt5) \) from @exm-polar-2x2, and \( \B = \begin{psmallmatrix} 3 & 0 \\ 4 & 3 \end{psmallmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \sigma(\B) = (\sqrt{13} + 2, \sqrt{13} - 2) \).
2. Verify @thm-mirsky-frobenius for this pair.
3. What bound on \( \sum_i(\sigma_i(\A) - \sigma_i(\B))^2 \) does @cor-singular-value-perturbation give? Hence say what Mirsky's theorem gains here.
:::
::::

::: {.solution}
(a) \( \B\tp\B = \begin{psmallmatrix} 25 & 12 \\ 12 & 9 \end{psmallmatrix} \) has trace \( 34 \) and determinant \( 225 - 144 = 81 \), so its eigenvalues are \( 17 \pm \sqrt{289 - 81} = 17 \pm 4\sqrt{13} \). Since \( (\sqrt{13} \pm 2)^2 = 17 \pm 4\sqrt{13} \) and \( \sqrt{13} - 2 > 0 \), the singular values are \( \sqrt{13} \pm 2 \approx 5.606, 1.606 \).

(b) \( \A - \B = \diag(0, 2) \), so \( \norm{\A - \B}_F^2 = 4 \). The left side is
\[
\begin{aligned}
&(3\sqrt5 - \sqrt{13} - 2)^2 + (\sqrt5 - \sqrt{13} + 2)^2 \\
&\qquad = 84 - 8\sqrt{65} - 8\sqrt5 \approx 1.613 ,
\end{aligned}
\]
expanding each square (the \( \sqrt{13} \) terms cancel). Indeed \( 1.613 \le 4 \).

(c) \( \norm{\A - \B}_2 = 2 \), so each \( \lvert\sigma_i(\A) - \sigma_i(\B)\rvert \le 2 \), and the sum of the two squares is at most \( 8 \). Mirsky's theorem gives \( 4 \), half as much. The true value is about \( 1.613 \): the differences are about \( 1.103 \) and \( 0.631 \).
:::

:::: {#exr-singular-values-and-polar-b2}
[B2: A square root that does not commute]

Let \( \S = \begin{psmallmatrix} 3 & 2 \\ 2 & 3 \end{psmallmatrix} \), \( \T = \begin{psmallmatrix} 3 & 2 \\ 2 & 4 \end{psmallmatrix} \), \( \P = \S^2 \) and \( \Q = \T^2 \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \P \) and \( \Q \), and explain why \( \S = \P^{1/2} \) and \( \T = \Q^{1/2} \).
2. Find \( \lambda_2(\P) \) and \( \lambda_2(\Q)^{1/2} \).
3. Compute \( \norm{\P - \Q}_2 \) and \( \norm{\P - \Q}_F \), and hence the two bounds of @thm-sqrt-perturbation. Compare them with \( \norm{\S - \T} \).
:::
::::

::: {.solution}
(a) Squaring, \( \P = \begin{psmallmatrix} 13 & 12 \\ 12 & 13 \end{psmallmatrix} \) and \( \Q = \begin{psmallmatrix} 13 & 14 \\ 14 & 20 \end{psmallmatrix} \). \( \S \) is symmetric with eigenvalues \( 5 \) and \( 1 \) (eigenvectors \( (1, \pm1) \)), and \( \T \) is symmetric with trace \( 7 \) and determinant \( 8 \), so both eigenvalues of each are positive, and \( \S, \T \succ 0 \). By the uniqueness in @thm-psd-square-root, \( \S = \P^{1/2} \) and \( \T = \Q^{1/2} \).

(b) The eigenvalues of \( \P \) are \( 25 \) and \( 1 \), so \( \lambda_2(\P) = 1 \). The eigenvalues of \( \T \) are \( \tfrac{7 \pm \sqrt{17}}{2} \), and by @thm-psd-square-root those of \( \Q \) are their squares, so \( \lambda_2(\Q)^{1/2} = \lambda_2(\T) = \tfrac{7 - \sqrt{17}}{2} \approx 1.438 \).

(c) \( \P - \Q = \begin{psmallmatrix} 0 & -2 \\ -2 & -7 \end{psmallmatrix} \) is symmetric with characteristic polynomial \( t^2 + 7t - 4 \), so its eigenvalues are \( \tfrac{-7 \pm \sqrt{65}}{2} \), and by @lem-hermitian-spectral-norm \( \norm{\P - \Q}_2 = \tfrac{7 + \sqrt{65}}{2} \approx 7.531 \). Also \( \norm{\P - \Q}_F = \sqrt{4 + 4 + 49} = \sqrt{57} \approx 7.550 \). The denominator is \( 1 + 1.438 = 2.438 \), so the bounds are about \( 3.089 \) (spectral) and \( 3.096 \) (Frobenius). Since \( \S - \T = \diag(0, -1) \), both of its norms equal \( 1 \). Hence the theorem holds here with a factor of about \( 3 \) to spare. It is not an equality because \( \S - \T \) does not sit along the eigenvector of \( \P \) and \( \Q \) where both are smallest.
:::

:::: {#exr-singular-values-and-polar-b3}
[B3: A nearly sharp instance]

Let \( \A = 2\I_2 \) and \( \B = \begin{psmallmatrix} 2 & -1 \\ 1 & 2 \end{psmallmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Find the polar decompositions of \( \A \) and \( \B \).
2. Compute \( \norm{\U - \V}_2 \) and \( \norm{\U - \V}_F \), and compare them with the bounds of @thm-polar-unitary-perturbation.
3. Compute \( \norm{\,\lvert\A\rvert - \lvert\B\rvert\,}_2 \) and the bound of @thm-polar-positive-perturbation.
:::
::::

::: {.solution}
(a) \( \A = \I \cdot 2\I \), with \( \U = \I \) and \( \lvert\A\rvert = 2\I \succ 0 \). The columns of \( \B \) are orthogonal, each of length \( \sqrt5 \), so \( \V = \tfrac{1}{\sqrt5}\B \) is orthogonal and \( \B = \V \cdot \sqrt5\,\I \), with \( \sqrt5\,\I \succ 0 \). Both matrices are invertible, so these are their polar decompositions (@thm-polar-decomposition), and \( \sigma_2(\A) = 2 \), \( \sigma_2(\B) = \sqrt5 \).

(b) \( \V \) is the rotation with \( \cos\varphi = \tfrac{2}{\sqrt5} \), so, as in @exm-polar-factors-nearby, \( (\U - \V)\tp(\U - \V) = (2 - 2\cos\varphi)\I = (2 - \tfrac{4}{\sqrt5})\I \). Hence \( \norm{\U - \V}_2 = \sqrt{2 - 4/\sqrt5} \approx 0.4595 \) and \( \norm{\U - \V}_F = \sqrt2\,\norm{\U - \V}_2 \approx 0.6498 \). Next, \( \A - \B = \begin{psmallmatrix} 0 & 1 \\ -1 & 0 \end{psmallmatrix} \) is orthogonal, so \( \norm{\A - \B}_2 = 1 \) and \( \norm{\A - \B}_F = \sqrt2 \). The bounds are
\[
\frac{2 \cdot 1}{2 + \sqrt5} \approx 0.4721,
\qquad
\frac{2\sqrt2}{2 + \sqrt5} \approx 0.6677 .
\]
Both hold, and each is within \( 3\% \) of the true value.

(c) \( \lvert\A\rvert - \lvert\B\rvert = (2 - \sqrt5)\I \), of spectral norm \( \sqrt5 - 2 \approx 0.236 \). The bound is \( (\norm{\A}_2 + \norm{\B}_2)\norm{\A - \B}_2/(2 + \sqrt5) = (2 + \sqrt5) \cdot 1/(2 + \sqrt5) = 1 \), a factor of about \( 4 \) larger.
:::

### C. Going deeper

:::: {#exr-singular-values-and-polar-c1}
[C1: The square root is continuous everywhere]

Let \( \S, \T \in M_n(\nC) \) be positive semidefinite.

::: {.enumerate options="label=(\alph*)"}
1. Let \( \lambda \) be an eigenvalue of the Hermitian matrix \( \S - \T \), with unit eigenvector \( \x \). Prove that \( \S^2 - \T^2 = (\S - \T)^2 + (\S - \T)\T + \T(\S - \T) \), and that \( \x^{*}(\S^2 - \T^2)\x = \lambda^2 + 2\lambda\,\x^{*}\T\x \).
2. Deduce that if \( \lambda \ge 0 \) then \( \lambda^2 \le \norm{\S^2 - \T^2}_2 \).
3. Prove that \( \norm{\P^{1/2} - \Q^{1/2}}_2 \le \norm{\P - \Q}_2^{1/2} \) for all positive semidefinite \( \P, \Q \in M_n(\nC) \), and show that the exponent \( \tfrac12 \) cannot be replaced by anything larger.
:::

*Hint: for (c), apply (b) to the pair \( (\S, \T) \) or to the pair \( (\T, \S) \), according to the sign of the eigenvalue of \( \S - \T \) of largest modulus.*
::::

::: {.solution}
(a) Expanding, \( (\S - \T)^2 + (\S - \T)\T + \T(\S - \T) = \S^2 - \S\T - \T\S + \T^2 + \S\T - \T^2 + \T\S - \T^2 = \S^2 - \T^2 \). Since \( (\S - \T)\x = \lambda\x \) with \( \lambda \) real (@thm-self-adjoint-real-eigenvalues) and \( \S - \T \) Hermitian, also \( \x^{*}(\S - \T) = \lambda\x^{*} \). Hence \( \x^{*}(\S - \T)^2\x = \lambda^2\x^{*}\x = \lambda^2 \), \( \x^{*}(\S - \T)\T\x = \lambda\,\x^{*}\T\x \) and \( \x^{*}\T(\S - \T)\x = \lambda\,\x^{*}\T\x \). Adding gives the claim.

(b) \( \x^{*}\T\x \ge 0 \) because \( \T \succeq 0 \), so if \( \lambda \ge 0 \), (a) gives \( \lambda^2 \le \x^{*}(\S^2 - \T^2)\x \). By @thm-cauchy-schwarz and @thm-operator-norm-properties (a), \( \x^{*}\M\x \le \norm{\M\x}\norm{\x} \le \norm{\M}_2 \) for any \( \M \) and unit \( \x \). So \( \lambda^2 \le \norm{\S^2 - \T^2}_2 \).

(c) Put \( \S = \P^{1/2} \) and \( \T = \Q^{1/2} \), so \( \S^2 - \T^2 = \P - \Q \). By @lem-hermitian-spectral-norm, \( \norm{\S - \T}_2 = \lvert\lambda\rvert \) for some eigenvalue \( \lambda \) of \( \S - \T \). If \( \lambda \ge 0 \), (b) gives \( \lambda^2 \le \norm{\P - \Q}_2 \). If \( \lambda < 0 \), then \( -\lambda > 0 \) is an eigenvalue of \( \T - \S \), and (b) applied to the pair \( (\T, \S) \) gives \( \lambda^2 \le \norm{\T^2 - \S^2}_2 = \norm{\P - \Q}_2 \). In both cases \( \norm{\P^{1/2} - \Q^{1/2}}_2 = \lvert\lambda\rvert \le \norm{\P - \Q}_2^{1/2} \).

For the exponent, take \( \P = \varepsilon\I \) and \( \Q = \0 \) with \( 0 < \varepsilon < 1 \), as in the warning after @thm-sqrt-perturbation. Then \( \norm{\P^{1/2} - \Q^{1/2}}_2 = \varepsilon^{1/2} \) and \( \norm{\P - \Q}_2 = \varepsilon \). If \( \varepsilon^{1/2} \le C\varepsilon^{r} \) held for all small \( \varepsilon \) with some \( r > \tfrac12 \), then \( C \ge \varepsilon^{1/2 - r} \to \infty \) as \( \varepsilon \to 0^{+} \), which is impossible. So the square root, which is not Lipschitz near singular matrices, is still continuous on all positive semidefinite matrices, with modulus \( t \mapsto t^{1/2} \).
:::

:::: {#exr-singular-values-and-polar-c2}
[C2: Both Eckart–Young lower bounds from perturbation theory]

Let \( \A \in M_{m \times n}(\nC) \), let \( 0 \le k < p = \min(m, n) \), and let \( \B \in M_{m \times n}(\nC) \) have rank at most \( k \).

::: {.enumerate options="label=(\alph*)"}
1. Explain why \( \sigma_i(\B) = 0 \) for \( i > k \).
2. Prove, using @thm-mirsky-frobenius, that \( \norm{\A - \B}_F^2 \ge \sum_{i=k+1}^{p}\sigma_i(\A)^2 \).
3. Prove, using @cor-singular-value-perturbation, that \( \norm{\A - \B}_2 \ge \sigma_{k+1}(\A) \).
4. Compare with @thm-eckart-young and @thm-eckart-young-spectral.
:::
::::

::: {.solution}
(a) By @thm-compact-svd the number of non-zero singular values of \( \B \) is \( \rank\B \le k \), and they come first in the decreasing list, so \( \sigma_i(\B) = 0 \) for \( i > k \).

(b) By @thm-mirsky-frobenius, and dropping the non-negative terms with \( i \le k \),
\[
\begin{aligned}
\norm{\A - \B}_F^2
&\ge \sum_{i=1}^{p}\bigl(\sigma_i(\A) - \sigma_i(\B)\bigr)^2 \\
&\ge \sum_{i=k+1}^{p}\bigl(\sigma_i(\A) - 0\bigr)^2 ,
\end{aligned}
\]
using (a) in the last step.

(c) By @cor-singular-value-perturbation with \( i = k + 1 \le p \) and \( \E = \B - \A \),
\[
\sigma_{k+1}(\A) = \bigl\lvert\sigma_{k+1}(\A) - \sigma_{k+1}(\B)\bigr\rvert \le \norm{\B - \A}_2 = \norm{\A - \B}_2 ,
\]
using (a) and \( \sigma_{k+1}(\A) \ge 0 \).

(d) These are exactly the lower-bound halves of the Frobenius and the spectral Eckart–Young theorems. Both theorems also show that the bounds are attained, by the truncation \( \A_k \), which has singular values \( \sigma_1(\A), \dots, \sigma_k(\A), 0, \dots, 0 \), so that it makes every term with \( i \le k \) vanish. So "the best rank-\( k \) approximation" is a perturbation theorem read backwards: no matrix of rank \( k \) can be closer to \( \A \) than the singular values of \( \A \) allow, because singular values cannot move further than the perturbation.
:::

:::: {#exr-singular-values-and-polar-c3}
[C3: The nearest unitary to an almost-unitary matrix]

Let \( \E \in M_n(\nC) \) with \( \norm{\E}_2 < 1 \), let \( \A = \I + \E \), and let \( \U \) be the unitary polar factor of \( \A \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \sigma_n(\A) \ge 1 - \norm{\E}_2 > 0 \), so that \( \A \) is invertible.
2. Prove that \( \norm{\U - \I} \le 2\norm{\E}/(2 - \norm{\E}_2) \) in both the spectral and the Frobenius norm.
3. Deduce that if \( \norm{\E}_2 \le \tfrac12 \) then \( \norm{\U - \I}_F \le \tfrac43\norm{\E}_F \). Compare with the bound \( \norm{\U - \I}_F \le 2\norm{\E}_F \) that @cor-unitary-nearest and the triangle inequality give with no computation.
:::
::::

::: {.solution}
(a) The identity has all singular values equal to \( 1 \). By @cor-singular-value-perturbation with \( i = n \), \( \lvert\sigma_n(\I + \E) - 1\rvert \le \norm{\E}_2 \), so \( \sigma_n(\A) \ge 1 - \norm{\E}_2 > 0 \). An \( n \times n \) matrix with \( n \) non-zero singular values has rank \( n \) (@thm-compact-svd), so \( \A \) is invertible.

(b) Apply @thm-polar-unitary-perturbation to \( \A \) and \( \B = \I \), whose polar decomposition is \( \I = \I \cdot \I \), with \( \V = \I \) and \( \sigma_n(\I) = 1 \). Since \( \A - \I = \E \),
\[
\norm{\U - \I} \le \frac{2\norm{\E}}{\sigma_n(\A) + 1} \le \frac{2\norm{\E}}{2 - \norm{\E}_2} ,
\]
using (a) to bound the denominator from below. This holds in both norms because the theorem does.

(c) If \( \norm{\E}_2 \le \tfrac12 \) then \( 2 - \norm{\E}_2 \ge \tfrac32 \), and (b) in the Frobenius norm gives \( \norm{\U - \I}_F \le \tfrac43\norm{\E}_F \).

For comparison, @cor-unitary-nearest says that \( \U \) is at least as close to \( \A \) as any unitary matrix is, and \( \I \) is one, so \( \norm{\A - \U}_F \le \norm{\A - \I}_F = \norm{\E}_F \). The triangle inequality (@cor-triangle-inequality) then gives
\[
\norm{\U - \I}_F \le \norm{\U - \A}_F + \norm{\A - \I}_F \le 2\norm{\E}_F .
\]
So the soft argument already locates \( \U \) within \( 2\norm{\E}_F \) of \( \I \). Part (b) improves the constant to \( \tfrac43 \) when \( \norm{\E}_2 \le \tfrac12 \), and to \( 2/(2 - \norm{\E}_2) \), which tends to \( 1 \), as \( \E \to \0 \). It also gives the spectral-norm statement, about which @cor-unitary-nearest says nothing.
:::
