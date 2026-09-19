# The Same Theory for Singular Values

Everything so far in this chapter has been about Hermitian matrices, and it had to be: a general square matrix need not have real eigenvalues to order, and a rectangular matrix has none at all. But every matrix has singular values, they are real and non-negative, and Chapter 12 listed them decreasingly from the moment it defined them. This section carries the apparatus across — a min–max description, a perturbation bound, an interlacing theorem — and then spends the rest of its length paying debts that earlier chapters recorded and could not settle.

**Throughout, \( F = \nR \) or \( F = \nC \)**, \( \A \in M_{m \times n}(F) \), \( p = \min(m, n) \), and \( \sigma_1(\A) \ge \dots \ge \sigma_p(\A) \ge 0 \) are the singular values of \( \A \) (@def-singular-values). Nothing here is assumed Hermitian and nothing is assumed square; where a matrix must be square, or invertible, the statement says so. Vector norms are Euclidean, and \( \norm{\A}_2 \) is the spectral norm of @def-operator-norm, which @thm-operator-norm-formulas (c) computes as \( \sigma_1(\A) \).

**One convention, stated once and used everywhere below.** We set
\[
\sigma_i(\A) \coloneqq 0 \qquad \text{for } p < i \le n .
\]
This is not new: @thm-singular-values-unique (a) already makes it, and records what it buys. With it in force, if \( \A = \U\vSigma\V^{*} \) is a singular value decomposition (@thm-svd) with columns \( \v_1, \dots, \v_n \) of \( \V \), then
\[
\A^{*}\A\,\v_i = \sigma_i(\A)^2\,\v_i \qquad (1 \le i \le n),
\]{#eq-sv-eigen}
so that \( \v_1, \dots, \v_n \) is an orthonormal eigenbasis of \( \A^{*}\A \) whose eigenvalues \( \sigma_1^2 \ge \dots \ge \sigma_n^2 \ge 0 \) are already sorted. In the notation of this chapter,
\[
\lambda_i(\A^{*}\A) = \sigma_i(\A)^2 \qquad (1 \le i \le n) .
\]
Every statement in this section is that identity, pushed through a theorem about Hermitian matrices.

## The stretch ratio is a Rayleigh quotient

Chapter 12 introduced the singular values by an algebraic route — take \( \A^{*}\A \), diagonalize it, take square roots. Their geometric meaning is stretching: how much longer \( \A\x \) is than \( \x \). The bridge between the two descriptions is one line of algebra, and it is the only computation this section needs before the theorems start.

For \( \x \ne \0 \) in \( F^n \), the matrix \( \A^{*}\A \) is Hermitian, so its Rayleigh quotient (@def-rayleigh-quotient) is defined, and

\[
R_{\A^{*}\A}(\x)
= \frac{\inner{\A^{*}\A\x}{\x}}{\inner{\x}{\x}}
= \frac{\x^{*}\A^{*}\A\x}{\x^{*}\x}
= \frac{(\A\x)^{*}(\A\x)}{\x^{*}\x}
= \frac{\norm{\A\x}^2}{\norm{\x}^2} .
\]{#eq-stretch-is-rayleigh}

*The Rayleigh quotient of \( \A^{*}\A \) is the squared stretching factor of \( \A \).*

So a statement about the Rayleigh quotient of \( \A^{*}\A \) is a statement about the function \( \x \mapsto \norm{\A\x}/\norm{\x} \), and conversely. Nothing is lost in passing between them, because \( t \mapsto \sqrt t \) is a strictly increasing bijection of \( [0, \infty) \) onto itself: it carries maxima to maxima and minima to minima, over any set whatever.

Before the min–max theorem, it is worth writing down what the singular value decomposition says about this function in coordinates. The computation is three lines, and it is used four times below — for the witness subspaces in every proof of the section — so it gets a label.

::: {#lem-stretch-in-singular-coordinates}
[Stretching in the Right Singular Basis]

Let \( \A \in M_{m \times n}(F) \) have a singular value decomposition \( \A = \U\vSigma\V^{*} \) (@thm-svd), with \( \v_1, \dots, \v_n \) the columns of \( \V \), and write \( \sigma_i = \sigma_i(\A) \) with the convention above. Then for \( \x = \sum_{i=1}^{n} c_i\v_i \),
\[
\norm{\A\x}^2 = \sum_{i=1}^{n}\sigma_i^2\,\lvert c_i\rvert^2 ,
\qquad
\norm{\x}^2 = \sum_{i=1}^{n}\lvert c_i\rvert^2 .
\]
Consequently, for each \( 1 \le k \le n \):

::: {.enumerate options="label=(\alph*)"}
1. on the **tail** subspace \( T_k = \Span(\v_k, \dots, \v_n) \), of dimension \( n - k + 1 \),
   \[
   \max\Bigl\{\tfrac{\norm{\A\x}}{\norm{\x}} : \0 \ne \x \in T_k\Bigr\} = \sigma_k ,
   \]
   attained at \( \x = \v_k \);
2. on the **head** subspace \( H_k = \Span(\v_1, \dots, \v_k) \), of dimension \( k \),
   \[
   \min\Bigl\{\tfrac{\norm{\A\x}}{\norm{\x}} : \0 \ne \x \in H_k\Bigr\} = \sigma_k ,
   \]
   attained at \( \x = \v_k \).
:::
:::


::: {.idea}
In the right singular basis \( \A \) does nothing but scale: it sends \( \v_i \) to \( \sigma_i\u_i \), and the \( \u_i \) are orthonormal. So measuring \( \A\x \) is Pythagoras applied to the scaled coordinates, and every claim about how much \( \A \) can stretch a subspace becomes a claim about a weighted sum of \( \lvert c_i\rvert^2 \).
:::

::: {.proof}
By @eq-sv-eigen the list \( (\v_1, \dots, \v_n) \) is an orthonormal basis of \( F^n \) consisting of eigenvectors of \( \A^{*}\A \), with \( \A^{*}\A\v_i = \sigma_i^2\v_i \). Hence, for \( \x = \sum_i c_i\v_i \), using @eq-stretch-is-rayleigh in the form \( \norm{\A\x}^2 = \x^{*}\A^{*}\A\x \) and expanding with orthonormality,
\[
\norm{\A\x}^2 = \Bigl(\sum_i c_i\v_i\Bigr)^{*}\Bigl(\sum_j c_j\sigma_j^2\v_j\Bigr) = \sum_{i=1}^{n}\sigma_i^2\lvert c_i\rvert^2 ,
\]
the cross terms vanishing because \( \v_i^{*}\v_j = \delta_{ij} \). The second identity is the same expansion with \( \A \) removed.

(a) For \( \0 \ne \x \in T_k \) we have \( c_i = 0 \) for \( i < k \), so \( \norm{\A\x}^2 = \sum_{i \ge k}\sigma_i^2\lvert c_i\rvert^2 \le \sigma_k^2\sum_{i\ge k}\lvert c_i\rvert^2 = \sigma_k^2\norm{\x}^2 \), since \( \sigma_i \le \sigma_k \) for \( i \ge k \) and the singular values are non-negative. Taking square roots gives \( \norm{\A\x}/\norm{\x} \le \sigma_k \), and \( \x = \v_k \) gives \( \norm{\A\v_k} = \sigma_k = \sigma_k\norm{\v_k} \), so the bound is attained.

(b) For \( \0 \ne \x \in H_k \) we have \( c_i = 0 \) for \( i > k \), so \( \norm{\A\x}^2 = \sum_{i \le k}\sigma_i^2\lvert c_i\rvert^2 \ge \sigma_k^2\norm{\x}^2 \), since now \( \sigma_i \ge \sigma_k \) for \( i \le k \); and \( \x = \v_k \) attains equality. This proves the lemma.
:::

In words: the tail subspace is a place where \( \A \) stretches **no more** than \( \sigma_k \), and the head subspace is a place where it stretches **no less**. The min–max theorem says that these two subspaces are optimal.

## Each singular value as an optimization

::: {#thm-singular-value-minmax}
[Min–Max for Singular Values]

Let \( \A \in M_{m \times n}(F) \) and let \( 1 \le k \le n \), with \( \sigma_k(\A) = 0 \) read by convention when \( k > p \). Then
\[
\begin{aligned}
\sigma_k(\A)
&= \min_{\substack{W \le F^n \\ \dim W = n-k+1}}\ \max_{\0 \ne \x \in W}\ \frac{\norm{\A\x}}{\norm{\x}} \\
&= \max_{\substack{W \le F^n \\ \dim W = k}}\ \min_{\0 \ne \x \in W}\ \frac{\norm{\A\x}}{\norm{\x}} .
\end{aligned}
\]
The outer minimum is attained at \( W = \Span(\v_k, \dots, \v_n) \) and the outer maximum at \( W = \Span(\v_1, \dots, \v_k) \), for the right singular vectors of any singular value decomposition of \( \A \).
:::

::: {.idea}
There is nothing to discover: @eq-stretch-is-rayleigh turns the objective function into the Rayleigh quotient of the Hermitian matrix \( \A^{*}\A \), @thm-courant-fischer applies to that matrix, and the square root — increasing, hence order-preserving — moves through the minima and maxima without changing which subspace attains them.
:::

::: {.proof}
Put \( \B = \A^{*}\A \in M_n(F) \), which is Hermitian, and fix \( 1 \le k \le n \). By @eq-sv-eigen, \( \lambda_k(\B) = \sigma_k(\A)^2 \). By @thm-courant-fischer applied to \( \B \),
\[
\sigma_k(\A)^2 = \lambda_k(\B) = \min_{\dim W = n-k+1}\ \max_{\0 \ne \x \in W} R_{\B}(\x) ,
\]
and by @eq-stretch-is-rayleigh, \( R_{\B}(\x) = \bigl(\norm{\A\x}/\norm{\x}\bigr)^2 \) for every \( \x \ne \0 \).

Fix a subspace \( W \). The function \( \x \mapsto \norm{\A\x}/\norm{\x} \) takes only non-negative values, and \( t \mapsto t^2 \) is strictly increasing on \( [0, \infty) \); so a vector of \( W \) maximizes \( R_{\B} \) over \( W \) exactly when it maximizes \( \norm{\A\x}/\norm{\x} \), and
\[
\max_{\0 \ne \x \in W} R_{\B}(\x) = \Bigl(\max_{\0 \ne \x \in W}\frac{\norm{\A\x}}{\norm{\x}}\Bigr)^{2} .
\]
(Both maxima exist: by homogeneity the quotient may be taken over the unit sphere of \( W \), which is compact by fact (A3) of Chapter 15's introduction, and the function is continuous, so the extreme value theorem — fact (A4) of Chapter 15's introduction — applies. This is the same appeal @thm-courant-fischer makes.) Taking square roots, and using once more that \( t \mapsto \sqrt t \) is increasing, so that it commutes with a minimum over the family of subspaces,
\[
\sigma_k(\A) = \sqrt{\lambda_k(\B)} = \min_{\dim W = n-k+1}\ \max_{\0 \ne \x \in W}\frac{\norm{\A\x}}{\norm{\x}} .
\]
The max–min form follows from the second equality of @thm-courant-fischer by the same two steps.

For the attainment claims, @lem-stretch-in-singular-coordinates (a) says that the tail subspace \( T_k \), of dimension \( n-k+1 \), has inner maximum exactly \( \sigma_k(\A) \), which is therefore the outer minimum; and part (b) says the head subspace \( H_k \), of dimension \( k \), has inner minimum exactly \( \sigma_k(\A) \). This proves the theorem.
:::

Two things are worth noticing. First, the subspaces \( W \) live in \( F^n \), the **domain**, whatever \( m \) is; the theorem compares two matrices with the same number of columns without caring how many rows they have. Second, the extremal subspaces are named, and they are spans of right singular vectors: the theorem is not only an identity but a recipe.

There is a second route to the same theorem, and it is worth recording because it converts a statement about a rectangular matrix into a statement about a Hermitian one, which is what the later chapters will want.

::: {#prp-hermitian-dilation}
[The Hermitian Dilation]

Let \( \A \in M_{m \times n}(F) \) and put
\[
\cH(\A) \coloneqq \begin{pmatrix} \0 & \A \\ \A^{*} & \0\end{pmatrix} \in M_{m+n}(F) .
\]
Then \( \cH(\A) \) is Hermitian, and its eigenvalues, with multiplicity, are
\[
\sigma_1(\A), \dots, \sigma_p(\A), \ -\sigma_1(\A), \dots, -\sigma_p(\A), \ \underbrace{0, \dots, 0}_{m + n - 2p} .
\]
:::


::: {.idea}
Guess the eigenvectors from the SVD. The pair \( (\u_i, \v_i) \), stacked, is sent by \( \cH(\A) \) to \( (\A\v_i, \A^{*}\u_i) = \sigma_i(\u_i, \v_i) \); flipping the sign of the second half flips the sign of the eigenvalue. That accounts for \( 2p \) orthonormal eigenvectors, and what is left over is a kernel whose dimension is a count.
:::

::: {.proof}
Writing out the conjugate transpose block by block, \( \cH(\A)^{*} = \begin{psmallmatrix} \0 & (\A^{*})^{*} \\ \A^{*} & \0\end{psmallmatrix} = \cH(\A) \), so \( \cH(\A) \) is Hermitian.

Fix a singular value decomposition \( \A = \U\vSigma\V^{*} \) (@thm-svd), with columns \( \u_1, \dots, \u_m \) of \( \U \) and \( \v_1, \dots, \v_n \) of \( \V \). Since \( \V^{*}\v_i = \e_i \) and \( \vSigma\e_i = \sigma_i\e_i \) for \( i \le p \) while \( \vSigma\e_j = \0 \) for \( p < j \le n \), and symmetrically for \( \A^{*} = \V\vSigma^{*}\U^{*} \),
\[
\A\v_i = \sigma_i\u_i, \quad \A^{*}\u_i = \sigma_i\v_i \ \ (i \le p),
\qquad
\A\v_j = \0, \quad \A^{*}\u_j = \0 \ \ (j > p) .
\]
For \( i \le p \) put
\[
\w_i^{\pm} = \tfrac{1}{\sqrt2}\begin{pmatrix} \u_i \\ \pm\v_i\end{pmatrix} \in F^{m+n} .
\]
Then \( \cH(\A)\w_i^{\pm} = \tfrac{1}{\sqrt2}\bigl(\pm\A\v_i,\ \A^{*}\u_i\bigr) = \tfrac{1}{\sqrt2}\bigl(\pm\sigma_i\u_i,\ \sigma_i\v_i\bigr) = \pm\sigma_i\,\w_i^{\pm} \). Likewise \( \cH(\A)(\u_j, \0) = (\0, \A^{*}\u_j) = \0 \) for \( j > p \), and \( \cH(\A)(\0, \v_j) = (\A\v_j, \0) = \0 \) for \( j > p \).

These \( 2p + (m - p) + (n - p) = m + n \) vectors are orthonormal: the \( \w_i^{\pm} \) are unit vectors because \( \u_i \) and \( \v_i \) are, and any two distinct vectors in the list pair to \( 0 \), since \( (\w_i^{+})^{*}\w_i^{-} = \tfrac12(1 - 1) = 0 \) and all other pairs have orthogonal \( \u \)-parts or orthogonal \( \v \)-parts. So they form an orthonormal eigenbasis of \( F^{m+n} \) with the stated eigenvalues, which are therefore the eigenvalue list of \( \cH(\A) \) with multiplicity. This proves the proposition.
:::

Applying @thm-courant-fischer to \( \cH(\A) \) instead of \( \A^{*}\A \) gives @thm-singular-value-minmax again, with subspaces of \( F^{m+n} \) in place of \( F^{n} \). We took the shorter road; the dilation is recorded because it turns *any* theorem about Hermitian eigenvalues into one about singular values, which Section 10's exercises and Chapter 19 both exploit.

## Perturbation, with no hypothesis at all

For Hermitian matrices, @cor-weyl-perturbation says that \( \lvert\lambda_i(\A + \E) - \lambda_i(\A)\rvert \le \norm{\E}_2 \) — provided \( \A \) and \( \E \) are Hermitian. That proviso is not decoration: Chapter 15's @exm-jordan-block-perturbation shows the conclusion failing spectacularly without it. The corresponding statement for singular values needs no proviso whatsoever.

::: {#thm-weyl-singular-values}
[Weyl's Inequalities for Singular Values]

Let \( \A, \B \in M_{m \times n}(F) \) and let \( i, j \ge 1 \) with \( i + j - 1 \le n \). Then
\[
\sigma_{i+j-1}(\A + \B) \le \sigma_i(\A) + \sigma_j(\B) .
\]
:::

::: {.idea}
Put \( k = i + j - 1 \). The min–max form of @thm-singular-value-minmax bounds \( \sigma_k(\A+\B) \) from above as soon as we produce **one** subspace of dimension \( n - k + 1 \) on which \( \A + \B \) stretches by at most \( \sigma_i(\A) + \sigma_j(\B) \). Each summand supplies a subspace where it is individually small — the tail subspaces of @lem-stretch-in-singular-coordinates — and the dimensions are chosen so that the two subspaces must overlap in something of the required size. On the overlap the triangle inequality finishes it.
:::

::: {.proof}
Put \( k = i + j - 1 \le n \). Let \( T = \Span(\v_i, \dots, \v_n) \) for the right singular vectors of \( \A \) and \( T' = \Span(\v_j', \dots, \v_n') \) for those of \( \B \), so that \( \dim T = n - i + 1 \), \( \dim T' = n - j + 1 \), and by @lem-stretch-in-singular-coordinates (a),
\[
\norm{\A\x} \le \sigma_i(\A)\norm{\x} \ \ (\x \in T),
\qquad
\norm{\B\x} \le \sigma_j(\B)\norm{\x} \ \ (\x \in T') .
\]
By the dimension formula (@thm-dimension-formula-subspace-dim) and \( \dim(T + T') \le n \),
\[
\begin{aligned}
\dim(T \cap T') &\ge (n - i + 1) + (n - j + 1) - n \\
&= n - (i + j - 1) + 1 = n - k + 1 ,
\end{aligned}
\]
which is at least \( 1 \) because \( k \le n \). Choose a subspace \( W \subseteq T \cap T' \) with \( \dim W = n - k + 1 \) exactly; this is possible because every subspace has a subspace of each smaller dimension, obtained by truncating a basis. For \( \0 \ne \x \in W \), the triangle inequality (@cor-triangle-inequality) gives
\[
\norm{(\A + \B)\x} \le \norm{\A\x} + \norm{\B\x} \le \bigl(\sigma_i(\A) + \sigma_j(\B)\bigr)\norm{\x} .
\]
Hence the inner maximum over \( W \) is at most \( \sigma_i(\A) + \sigma_j(\B) \), and since \( \sigma_k(\A+\B) \) is the **minimum** of that inner maximum over all subspaces of dimension \( n - k + 1 \) (@thm-singular-value-minmax), we get \( \sigma_k(\A+\B) \le \sigma_i(\A) + \sigma_j(\B) \). This proves the theorem.
:::

::: {#cor-singular-value-perturbation}
[Singular Values Are Perfectly Conditioned]

Let \( \A, \E \in M_{m \times n}(F) \). Then
\[
\lvert\sigma_i(\A + \E) - \sigma_i(\A)\rvert \le \norm{\E}_2
\qquad\text{for every } 1 \le i \le n .
\]
No hypothesis is placed on \( \A \) or on \( \E \).
:::


::: {.idea}
Put \( j = 1 \) in the Weyl inequality for singular values: one index passes through unchanged, and the other matrix contributes only its largest singular value, which is \( \norm{\E}_2 \). That bounds \( \sigma_i(\A + \E) \) from above; writing \( \A = (\A + \E) + (-\E) \) and doing it again bounds it from below.
:::

::: {.proof}
Take \( j = 1 \) in @thm-weyl-singular-values, so that \( i + j - 1 = i \le n \):
\[
\sigma_i(\A + \E) \le \sigma_i(\A) + \sigma_1(\E) = \sigma_i(\A) + \norm{\E}_2 ,
\]
using @thm-operator-norm-formulas (c) for the last equality. Now apply the same inequality with \( \A + \E \) in place of \( \A \) and \( -\E \) in place of \( \E \), noting \( \norm{-\E}_2 = \norm{\E}_2 \) by homogeneity (@thm-operator-norm-properties (b)):
\[
\sigma_i(\A) = \sigma_i\bigl((\A + \E) + (-\E)\bigr) \le \sigma_i(\A + \E) + \norm{\E}_2 .
\]
The two inequalities together are the claim.
:::

This is a Lipschitz bound with constant \( 1 \), exactly as @cor-weyl-perturbation is for Hermitian eigenvalues, and with no dependence on \( n \), on the conditioning of \( \A \), or on the gaps between the singular values. What is new is the absence of hypotheses. It is worth seeing the contrast on the very matrix Chapter 15 used to show that eigenvalues have no such bound.

::: {#exm-jordan-block-singular-values}
[The Jordan block again, measured by its singular values]

Let \( k \ge 2 \), let \( 0 < \varepsilon < 1 \), and let
\[
\A = \J_k(0), \qquad \A_{\varepsilon} = \J_k(0) + \varepsilon\E_{k1}
\]
be the matrices of @exm-jordan-block-perturbation. Compute the singular values of both, and compare how far they move with how far the eigenvalues move.
:::

::: {.solution}
The columns of \( \A_{\varepsilon} \) are \( \varepsilon\e_k \) in position \( 1 \), and \( \e_{j-1} \) in position \( j \) for \( 2 \le j \le k \). These \( k \) columns are pairwise orthogonal, with norms \( \varepsilon, 1, \dots, 1 \), so
\[
\A_{\varepsilon}^{*}\A_{\varepsilon} = \diag(\varepsilon^2, 1, \dots, 1) ,
\]
whose eigenvalues in decreasing order are \( 1 \) with multiplicity \( k-1 \) and then \( \varepsilon^2 \), since \( \varepsilon < 1 \). By @def-singular-values the singular values of \( \A_{\varepsilon} \) are
\[
\sigma_1 = \dots = \sigma_{k-1} = 1, \qquad \sigma_k = \varepsilon .
\]
Setting \( \varepsilon = 0 \) in the same computation, the singular values of \( \A = \J_k(0) \) are \( 1, \dots, 1, 0 \).

So every singular value moves by at most \( \varepsilon \), and exactly one of them — the last — moves by exactly \( \varepsilon \). The perturbation has \( \norm{\varepsilon\E_{k1}}_2 = \varepsilon \), computed in @exm-jordan-block-perturbation, so @cor-singular-value-perturbation is attained here and not merely satisfied.

Meanwhile @exm-jordan-block-perturbation computed that the **eigenvalues** of the same two matrices are \( 0 \) (with multiplicity \( k \)) and the \( k \)-th roots of \( \varepsilon \), all of modulus \( \varepsilon^{1/k} \). For \( k = 10 \) and \( \varepsilon = 10^{-10} \): the singular values move by \( 10^{-10} \), and the eigenvalues move by \( 10^{-1} \), a factor of a billion more. The same matrix, the same perturbation, two spectra — one of them stable and one of them not.
:::

This is not a paradox. The singular values of \( \A \) are the square roots of the eigenvalues of the Hermitian matrix \( \A^{*}\A \), and Hermitian eigenvalues are stable; the eigenvalues of \( \A \) itself are roots of a polynomial, and a repeated root is fragile. The instability lives in the passage from \( \A \) to its eigenvalues, not in \( \A \) — which is why a question that can be phrased in singular values should be.

::: {.warning}
**Weyl's inequality does not say \( \sigma_k(\A + \B) \le \sigma_k(\A) + \sigma_k(\B) \).** The index bookkeeping \( i + j - 1 \) is the content, not a technicality. Take
\[
\A = \diag(1, 0), \qquad \B = \diag(0, 1) .
\]
Then \( \sigma(\A) = \sigma(\B) = (1, 0) \), while \( \A + \B = \I_2 \) has \( \sigma(\I_2) = (1, 1) \). So \( \sigma_2(\A + \B) = 1 \) while \( \sigma_2(\A) + \sigma_2(\B) = 0 \). What @thm-weyl-singular-values does give here, with \( i = j = 1 \), is \( \sigma_1(\A + \B) \le \sigma_1(\A) + \sigma_1(\B) = 2 \), which holds. Only \( i = 1 \) or \( j = 1 \) lets an index pass through unchanged, which is why @cor-singular-value-perturbation is the case \( j = 1 \).
:::

## The best approximation of low rank

Chapter 12 §10 proved that the truncated singular value decomposition \( \A_k \) of @def-truncated-svd is the closest matrix of rank at most \( k \) to \( \A \) in the Frobenius norm (@thm-eckart-young), and then wrote, in the remark that closes its main proof:

> The same matrix \( \A_k \) is also optimal in the **spectral norm** \( \norm{\cdot}_2 \), where the minimum value is \( \sigma_{k+1} \) rather than \( \bigl(\sum_{i>k}\sigma_i^2\bigr)^{1/2} \). We cannot state that here, because the spectral norm is defined only in Chapter 15.

Chapter 15 supplied the norm and then, in its closing ledger, handed the theorem to this chapter: "the theorem itself waits for Chapter 16, which proves it from the min–max description of the singular values." That description now exists. Here is the theorem.

::: {#thm-eckart-young-spectral}
[Eckart–Young Theorem, Spectral Case]

Let \( \A \in M_{m \times n}(F) \) and let \( 0 \le k < n \). Then for **every** \( \B \in M_{m \times n}(F) \) with \( \rank\B \le k \),
\[
\norm{\A - \B}_2 \ \ge\ \sigma_{k+1}(\A) ,
\]
and equality holds for the truncation \( \B = \A_k \) of @def-truncated-svd. In words: \( \A_k \) minimizes \( \norm{\A - \B}_2 \) over all matrices of rank at most \( k \), and the minimum value is \( \sigma_{k+1}(\A) \).
:::

::: {.idea}
A matrix \( \B \) of rank at most \( k \) has a large null space — dimension at least \( n - k \) — and on that null space \( \A - \B \) acts exactly as \( \A \) does. The head subspace \( H_{k+1} = \Span(\v_1, \dots, \v_{k+1}) \) is a place where \( \A \) stretches by at least \( \sigma_{k+1} \), and it has dimension \( k+1 \). Two subspaces of \( F^n \) of dimensions \( n - k \) and \( k+1 \) cannot avoid each other, by @lem-subspace-intersection, and a vector in both settles the matter in one line.
:::

::: {.proof}
*The lower bound.* Let \( \rank\B \le k \). By Rank–Nullity for matrices (@thm-rank-nullity-matrix), \( \dim\nul(\B) = n - \rank\B \ge n - k \). Let \( H = \Span(\v_1, \dots, \v_{k+1}) \), where \( \v_1, \dots, \v_n \) are the right singular vectors of a fixed singular value decomposition of \( \A \); then \( \dim H = k + 1 \). Since
\[
\dim\nul(\B) + \dim H \ \ge\ (n - k) + (k + 1) = n + 1 > n ,
\]
@lem-subspace-intersection gives a vector \( \x \ne \0 \) with \( \x \in \nul(\B) \cap H \). For that \( \x \), \( \B\x = \0 \), so \( (\A - \B)\x = \A\x \), and by @lem-stretch-in-singular-coordinates (b) applied with \( k + 1 \) in place of \( k \),
\[
\norm{(\A - \B)\x} = \norm{\A\x} \ \ge\ \sigma_{k+1}(\A)\,\norm{\x} .
\]
Since \( \x \ne \0 \), dividing by \( \norm{\x} \) and using @thm-operator-norm-properties (a), which says \( \norm{\A - \B}_2 \) is the largest such ratio, gives \( \norm{\A - \B}_2 \ge \sigma_{k+1}(\A) \).

*Equality at the truncation.* If \( k \ge p \), then \( \A_k = \A \) by @def-truncated-svd and \( \sigma_{k+1}(\A) = 0 \) by our convention, so equality holds trivially; assume \( k < p \). By @def-truncated-svd, \( \A_k = \sum_{i\le k}\sigma_i\u_i\v_i^{*} \) has rank \( \min(k, \rank\A) \le k \), and
\[
\A - \A_k = \sum_{i > k}\sigma_i\u_i\v_i^{*} = \U\vSigma^{(k)}\V^{*} ,
\]
where \( \vSigma^{(k)} \) is \( \vSigma \) with its first \( k \) diagonal entries replaced by \( 0 \). Since \( \U \) is unitary, \( (\A - \A_k)^{*}(\A - \A_k) = \V\,(\vSigma^{(k)})^{*}\vSigma^{(k)}\,\V^{*} \), which is similar to the diagonal matrix \( (\vSigma^{(k)})^{*}\vSigma^{(k)} \); its eigenvalues are therefore \( \sigma_{k+1}^2, \dots, \sigma_p^2 \) together with zeros. By @def-singular-values the singular values of \( \A - \A_k \) are \( \sigma_{k+1} \ge \sigma_{k+2} \ge \dots \) followed by zeros, the largest being \( \sigma_{k+1} \). Hence \( \norm{\A - \A_k}_2 = \sigma_{k+1}(\A) \) by @thm-operator-norm-formulas (c). This proves the theorem.
:::

So the *minimizer* is the same matrix in both norms, and only the *minimum value* changes: \( \sigma_{k+1} \) for the spectral norm, \( \bigl(\sum_{i>k}\sigma_i^2\bigr)^{1/2} \) for the Frobenius norm. That the same \( \A_k \) works for both is not a coincidence — it is optimal in every unitarily invariant norm at once, which is Chapter 20's theorem and needs machinery neither this section nor Chapter 12 has.

::: {#exm-spectral-vs-frobenius}
[One matrix, two norms]

Let
\[
\A = \begin{pmatrix} 3 & 1 & 0 \\ 1 & 3 & 0 \\ 0 & 0 & 1 \end{pmatrix} \in M_3(\nR) .
\]
Find the best approximations of rank \( 1 \) and rank \( 2 \), and compute the error in both the spectral and the Frobenius norm.
:::

::: {.solution}
\( \A \) is symmetric and block diagonal. The \( 2 \times 2 \) block \( \begin{psmallmatrix} 3 & 1 \\ 1 & 3\end{psmallmatrix} \) has trace \( 6 \) and determinant \( 8 \), hence eigenvalues \( 4 \) and \( 2 \), with orthonormal eigenvectors \( \tfrac{1}{\sqrt2}(1,1) \) and \( \tfrac{1}{\sqrt2}(1,-1) \); the third eigenvalue is \( 1 \), with eigenvector \( \e_3 \). All three eigenvalues are positive, so \( \A \succ 0 \) and its singular values are those eigenvalues (@thm-pd-characterizations; \( \A^{*}\A = \A^2 \) has eigenvalues their squares):
\[
\sigma_1 = 4, \quad \sigma_2 = 2, \quad \sigma_3 = 1,
\]
with \( \u_i = \v_i \) the unit eigenvectors \( \tfrac{1}{\sqrt2}(1,1,0) \), \( \tfrac{1}{\sqrt2}(1,-1,0) \), \( \e_3 \).

Truncating,
\[
\A_1 = 4\v_1\v_1\tp = \begin{pmatrix} 2 & 2 & 0 \\ 2 & 2 & 0 \\ 0 & 0 & 0\end{pmatrix},
\qquad
\A_2 = \begin{pmatrix} 3 & 1 & 0 \\ 1 & 3 & 0 \\ 0 & 0 & 0\end{pmatrix},
\]
the second because \( 4\v_1\v_1\tp + 2\v_2\v_2\tp \) restores the \( 2\times2 \) block exactly. The error matrices are
\[
\A - \A_1 = \begin{pmatrix} 1 & -1 & 0 \\ -1 & 1 & 0 \\ 0 & 0 & 1\end{pmatrix},
\qquad
\A - \A_2 = \diag(0,0,1) .
\]
For \( k = 1 \): \( \norm{\A - \A_1}_2 = \sigma_2 = 2 \) and \( \norm{\A - \A_1}_F = \sqrt{\sigma_2^2 + \sigma_3^2} = \sqrt5 \approx 2.236 \). Check the first directly: \( \A - \A_1 \) is symmetric with the \( 2\times2 \) block \( \begin{psmallmatrix} 1 & -1 \\ -1 & 1\end{psmallmatrix} \), of eigenvalues \( 2 \) and \( 0 \), and the entry \( 1 \), so its largest eigenvalue in modulus is \( 2 \). Check the second directly: the sum of the squares of the five non-zero entries is \( 4 \cdot 1 + 1 = 5 \).

For \( k = 2 \): both norms of \( \diag(0,0,1) \) equal \( 1 = \sigma_3 \), and the two formulas agree because only one singular value is discarded.
:::

::: {.check}
A matrix has singular values \( 6, 3, 2, 1 \). What is the smallest spectral-norm error of a rank-\( 2 \) approximation, and how does it compare with the Frobenius-norm error found in @exr-low-rank-approximation-b1?
:::

::: {.solution}
By @thm-eckart-young-spectral with \( k = 2 \), the minimum is \( \sigma_3 = 2 \). By @thm-eckart-young the Frobenius minimum is \( \sqrt{\sigma_3^2 + \sigma_4^2} = \sqrt5 \approx 2.236 \). The Frobenius error is the larger of the two, as it must be: it counts every discarded singular value, while the spectral error counts only the largest one.
:::

## How far an invertible matrix is from being singular

Take \( k = n - 1 \) in @thm-eckart-young-spectral, with \( \A \) square. A matrix of rank at most \( n-1 \) is precisely a singular matrix, so the theorem computes the distance from \( \A \) to the set of singular matrices. That is the geometric content of Chapter 15's condition number, and it is the best payoff in this chapter.

::: {#cor-distance-to-singular}
[The Distance to Singularity]

Let \( \A \in M_n(F) \) be invertible. Then
\[
\min\bigl\{\norm{\A - \B}_2 : \B \in M_n(F) \text{ singular}\bigr\} = \sigma_n(\A) = \frac{1}{\norm{\A^{-1}}_2} ,
\]
the minimum being attained at \( \B = \A_{n-1} \). Consequently the **relative** distance from \( \A \) to the nearest singular matrix is
\[
\frac{\min\{\norm{\A - \B}_2 : \B \text{ singular}\}}{\norm{\A}_2} = \frac{\sigma_n(\A)}{\sigma_1(\A)} = \frac{1}{\kappa_2(\A)} ,
\]
the reciprocal of the spectral condition number of @def-condition-number.
:::


::: {.idea}
A singular matrix has rank at most \( n - 1 \), so this is the spectral Eckart–Young theorem with \( k = n - 1 \), and the answer is the next singular value, \( \sigma_n \). The formula \( 1/\norm{\A^{-1}}_2 \) is the same number read through the inverse, whose largest singular value is \( 1/\sigma_n \).
:::

::: {.proof}
A matrix \( \B \in M_n(F) \) is singular if and only if \( \rank\B \le n - 1 \) (@thm-invertible-tfae). So the set over which the minimum is taken is exactly the set appearing in @thm-eckart-young-spectral with \( k = n - 1 \), and that theorem gives the value \( \sigma_{(n-1)+1}(\A) = \sigma_n(\A) \), attained at \( \A_{n-1} \). The matrix \( \A_{n-1} \) is singular because its rank is \( \min(n-1, \rank\A) = n - 1 < n \).

For the second expression: since \( \rank\A = n \), exactly \( n \) singular values of \( \A \) are non-zero (@thm-svd), so \( \sigma_n(\A) > 0 \). By @def-condition-number and @prp-condition-number-properties (d), \( \norm{\A}_2\norm{\A^{-1}}_2 = \kappa_2(\A) = \sigma_1(\A)/\sigma_n(\A) \), and \( \norm{\A}_2 = \sigma_1(\A) \) by @thm-operator-norm-formulas (c); dividing, \( \norm{\A^{-1}}_2 = 1/\sigma_n(\A) \). Dividing the minimum \( \sigma_n(\A) \) by \( \norm{\A}_2 = \sigma_1(\A) \) gives \( \sigma_n/\sigma_1 = 1/\kappa_2(\A) \), the last display. This proves the corollary.
:::

**What this settles.** Chapter 15 defined \( \kappa(\A) = \norm{\A}\norm{\A^{-1}} \) as the worst factor by which \( \A \) magnifies a relative error, proved that the factor is attained, and described it geometrically through @lem-inverse-norm-min as the ratio of the largest to the smallest stretch \( \norm{\A\x} \) over unit vectors \( \x \). That is a statement about what \( \A \) *does*. @cor-distance-to-singular is a statement about where \( \A \) *is*: it says that \( 1/\kappa_2(\A) \) measures the distance from \( \A \) to the boundary of the invertible matrices, relative to the size of \( \A \). A matrix with \( \kappa_2 = 10^6 \) is not merely a matrix that magnifies errors by a million; it is a matrix that a relative perturbation of one part in a million can make singular. "Ill-conditioned" and "nearly singular" are the same property, and this is the theorem that identifies them.

Two earlier exercises reached for this. @exr-low-rank-approximation-c1 found the same distance in the Frobenius norm — also \( \sigma_n \), since only one singular value is discarded when \( k = n-1 \). @exr-condition-numbers-c2 obtained the spectral statement by hand, with a Neumann-series lower bound and the truncation as witness. Nothing above rests on either. What is new is that the distance to singularity is now the case \( k = n-1 \) of one theorem covering every rank, proved by a dimension count and stated as an attained minimum.

::: {#exm-nearest-singular-2x2}
[The nearest singular matrix, exactly and approximately]

::: {.enumerate options="label=(\alph*)"}
1. For the matrix \( \A \) of @exm-spectral-vs-frobenius, find the nearest singular matrix and the relative distance to it.
2. Do the same, to three significant figures, for \( \C = \begin{psmallmatrix} 1 & 1 \\ 1 & 1.01\end{psmallmatrix} \), the ill-conditioned matrix of @exm-ill-conditioned-system.
:::
:::

::: {.solution}
(a) The singular values are \( 4, 2, 1 \), so by @cor-distance-to-singular the nearest singular matrix is at distance \( \sigma_3 = 1 \), and it is
\[
\A_2 = \begin{pmatrix} 3 & 1 & 0 \\ 1 & 3 & 0 \\ 0 & 0 & 0\end{pmatrix},
\]
computed in @exm-spectral-vs-frobenius; it is singular because its last row is zero. Here \( \kappa_2(\A) = 4/1 = 4 \), so the relative distance is \( \tfrac14 \): a perturbation of a quarter of the size of \( \A \) is needed, and \( \A \) is very well conditioned.

(b) \( \C \) is symmetric with \( \tr\C = \tfrac{201}{100} \) and \( \det\C = \tfrac{1}{100} \), so its eigenvalues are
\[
\frac{201 \pm \sqrt{201^2 - 400}}{200} = \frac{201 \pm \sqrt{40001}}{200} ,
\]
both positive, hence equal to the singular values: \( \sigma_1 \approx 2.00501 \) and \( \sigma_2 \approx 0.0049875 \). So \( \kappa_2(\C) \approx 402.0 \) and the nearest singular matrix is at distance \( \sigma_2 \approx 0.00499 \), a **relative** distance of \( 1/\kappa_2(\C) \approx 0.00249 \), about a quarter of one percent. The nearest singular matrix itself is \( \C_1 = \sigma_1\v_1\v_1\tp \), which to five decimals is
\[
\C_1 \approx \begin{pmatrix} 0.99749 & 1.00249 \\ 1.00249 & 1.00752 \end{pmatrix} ;
\]
it is singular, and each entry differs from the corresponding entry of \( \C \) by about \( 0.0025 \). Changing \( \C \) in its third decimal place destroys its invertibility. That is what \( \kappa_2 \approx 402 \) means.
:::

::: {.warning}
**The distance to singularity is not measured by the determinant.** Chapter 15 §08 warned that no threshold on \( \lvert\det\A\rvert \) detects ill-conditioning, and @cor-distance-to-singular says exactly why: the quantity that decides nearness to singularity is \( \sigma_n \), and \( \lvert\det\A\rvert = \sigma_1\sigma_2\cdots\sigma_n \) is a product in which a tiny \( \sigma_n \) can be hidden by large partners, or a healthy \( \sigma_n \) buried by many small ones. For \( \A = 10^{-6}\I_{10} \) all singular values are \( 10^{-6} \), so \( \lvert\det\A\rvert = 10^{-60} \) while the relative distance to singularity is \( 1/\kappa_2 = 1 \), the largest it can ever be. For \( \A = \diag(10^{6}, 10^{-6}) \), \( \lvert\det\A\rvert = 1 \) while the relative distance is \( 10^{-12} \). Only the *smallest* singular value knows.
:::

## Deleting a row

The last transfer is Cauchy interlacing. For a Hermitian matrix the operation was deleting a row **and** the matching column; for a general matrix there is no matching, and deleting a single row is enough.

::: {#thm-singular-value-interlacing}
[Interlacing Under Deletion of a Row or a Column]

Let \( \A \in M_{m \times n}(F) \) with \( m \ge 2 \), and let \( \B \in M_{(m-1)\times n}(F) \) be obtained from \( \A \) by deleting one row. Then
\[
\sigma_i(\B) \le \sigma_i(\A) \quad (1 \le i \le n),
\qquad
\sigma_{i+1}(\A) \le \sigma_i(\B) \quad (1 \le i \le n-1) ,
\]
singular values beyond the \( p \)-th being read as \( 0 \). If instead \( n \ge 2 \) and \( \B \in M_{m\times(n-1)}(F) \) is obtained from \( \A \) by deleting one **column**, the same two chains hold, both over \( 1 \le i \le n-1 \); written out, \( \sigma_1(\A) \ge \sigma_1(\B) \ge \sigma_2(\A) \ge \dots \ge \sigma_{n-1}(\B) \ge \sigma_n(\A) \).
:::

::: {.idea}
Deleting a row removes one term from the sum \( \norm{\A\x}^2 = \sum_{\text{rows}} \lvert\text{row} \cdot \x\rvert^2 \). So \( \norm{\B\x} \le \norm{\A\x} \) for every \( \x \), which gives the first chain from the min–max formula at once, because both matrices are compared over the same subspaces of \( F^n \). For the second chain, the two norms **agree** on the hyperplane where the deleted row vanishes; intersecting a good subspace for \( \B \) with that hyperplane costs one dimension, and one dimension is exactly one index.
:::

::: {.proof}
Say row \( r \) of \( \A \) is deleted, and write \( \r^{*} \in M_{1\times n}(F) \) for that row. Summing squares of entries coordinate by coordinate,
\[
\norm{\A\x}^2 = \norm{\B\x}^2 + \lvert\r^{*}\x\rvert^2 \qquad (\x \in F^n) ,
\]{#eq-row-deletion-split}
since the entries of \( \A\x \) are those of \( \B\x \) together with \( \r^{*}\x \).

*First chain.* By @eq-row-deletion-split, \( \norm{\B\x}/\norm{\x} \le \norm{\A\x}/\norm{\x} \) for every \( \x \ne \0 \). Both \( \A \) and \( \B \) have \( n \) columns, so @thm-singular-value-minmax describes \( \sigma_i(\A) \) and \( \sigma_i(\B) \) as a minimum over the *same* family of subspaces of \( F^n \), of a maximum of these two objective functions. A pointwise smaller function has a smaller maximum on each subspace and hence a smaller minimum over the family, so \( \sigma_i(\B) \le \sigma_i(\A) \) for every \( i \le n \).

*Second chain.* Fix \( 1 \le i \le n - 1 \). Let \( \w_1, \dots, \w_n \) be the right singular vectors of a singular value decomposition of \( \B \), and put \( T = \Span(\w_i, \dots, \w_n) \), of dimension \( n - i + 1 \); by @lem-stretch-in-singular-coordinates (a) applied to \( \B \),
\[
\norm{\B\x} \le \sigma_i(\B)\norm{\x} \qquad (\x \in T) .
\]
Let \( H = \{\x \in F^n : \r^{*}\x = 0\} = \nul(\r^{*}) \). Since \( \r^{*} \) has at most one non-zero row, \( \rank\r^{*} \le 1 \), so \( \dim H \ge n - 1 \) by Rank–Nullity for matrices (@thm-rank-nullity-matrix). By the dimension formula (@thm-dimension-formula-subspace-dim),
\[
\dim(T \cap H) \ \ge\ (n - i + 1) + (n - 1) - n = n - i \ \ge\ 1 .
\]
Choose \( W \subseteq T \cap H \) with \( \dim W = n - i = n - (i+1) + 1 \). For \( \0 \ne \x \in W \) we have \( \r^{*}\x = 0 \), so @eq-row-deletion-split gives \( \norm{\A\x} = \norm{\B\x} \le \sigma_i(\B)\norm{\x} \). Hence the inner maximum over \( W \) is at most \( \sigma_i(\B) \), and \( \sigma_{i+1}(\A) \), being the minimum of that inner maximum over all subspaces of dimension \( n - (i+1) + 1 \) (@thm-singular-value-minmax), is at most \( \sigma_i(\B) \).

*Columns.* Deleting column \( c \) of \( \A \) is deleting row \( c \) of \( \A^{*} \). Taking conjugate transposes in \( \A = \U\vSigma\V^{*} \) gives \( \A^{*} = \V\vSigma^{*}\U^{*} \), in which \( \vSigma^{*} \) has the same diagonal \( \sigma_1, \dots, \sigma_p \); so by @thm-singular-values-unique, \( \sigma_i(\A^{*}) = \sigma_i(\A) \) for every \( i \le p \), and the same holds for \( \B \) and \( \B^{*} \). Both \( \A^{*} \) and \( \B^{*} \) have \( m \) columns, so the row statement applied to them gives \( \sigma_i(\B) \le \sigma_i(\A) \) for \( i \le m \) and \( \sigma_{i+1}(\A) \le \sigma_i(\B) \) for \( i \le m - 1 \). The remaining indices are free: if \( i > m \) then \( i \) exceeds \( \min(m, n-1) \), so \( \sigma_i(\B) = 0 \) and the first inequality is trivial; and if \( i \ge m \) then \( i + 1 > p \), so \( \sigma_{i+1}(\A) = 0 \) and the second is trivial. Hence both chains hold on the stated ranges. This proves the theorem.
:::

::: {#exm-interlacing-row-deletion}
[Interlacing on a 3 × 2 matrix]

Let \( \A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1\end{pmatrix} \), the matrix of @exm-best-rank-one. Verify @thm-singular-value-interlacing for each of the three rows that could be deleted.
:::

::: {.solution}
@exm-best-rank-one computed \( \A\tp\A = \begin{psmallmatrix} 2 & 1 \\ 1 & 2\end{psmallmatrix} \), with eigenvalues \( 3 \) and \( 1 \), so \( \sigma_1(\A) = \sqrt3 \approx 1.732 \) and \( \sigma_2(\A) = 1 \).

*Deleting row 1 or row 2.* The remaining matrix is \( \begin{psmallmatrix} 0 & 1 \\ 1 & 1\end{psmallmatrix} \) or \( \begin{psmallmatrix} 1 & 0 \\ 1 & 1\end{psmallmatrix} \). In both cases \( \B\tp\B = \begin{psmallmatrix} 1 & 1 \\ 1 & 2\end{psmallmatrix} \), with trace \( 3 \) and determinant \( 1 \), hence eigenvalues \( (3 \pm \sqrt5)/2 \). Their square roots are \( (1 + \sqrt5)/2 \approx 1.618 \) and \( (\sqrt5 - 1)/2 \approx 0.618 \) — the two are reciprocal, since \( (3+\sqrt5)/2 \cdot (3-\sqrt5)/2 = 1 \). The interlacing reads
\[
1.732 \ \ge\ 1.618 \ \ge\ 1 \ \ge\ 0.618 ,
\]
that is \( \sigma_1(\A) \ge \sigma_1(\B) \ge \sigma_2(\A) \ge \sigma_2(\B) \), as the theorem requires.

*Deleting row 3.* The remaining matrix is \( \I_2 \), with \( \sigma_1 = \sigma_2 = 1 \), and the chain reads \( 1.732 \ge 1 \ge 1 \ge 1 \). Here the second inequality of the first chain and the inequality of the second chain are both equalities: deleting the row that carried all the interaction between the two columns leaves a perfectly conditioned matrix.
:::

Everything in this section came from one move: a singular value is the square root of an eigenvalue of a Hermitian matrix, so the min–max theory transfers wholesale. What the transfer bought is worth listing. The spectral half of the Eckart–Young theorem, which Chapter 12 could state only in the Frobenius norm, is now proved. The condition number of Chapter 15 has a geometric meaning: \( 1/\kappa_2(\A) \) is how far, relatively, \( \A \) sits from the nearest singular matrix. And singular values turned out to be perfectly conditioned with no hypothesis at all, which the Jordan block showed eigenvalues are not. The Hermitian dilation \( \cH(\A) \) is the other bridge from singular values to Hermitian eigenvalues; Section 10's exercises use it, and Chapter 19 leans on it for perturbation bounds.

## Exercises

### A. Check your understanding

:::: {#exr-singular-values-variationally-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the min–max description of \( \sigma_k(\A) \), naming the dimension of the subspaces in each of the two forms.
2. Explain in one sentence why the identity \( \norm{\A\x}^2/\norm{\x}^2 = R_{\A^{*}\A}(\x) \) is what makes the whole section possible.
3. State the bound of @cor-singular-value-perturbation and say precisely which hypotheses it needs, comparing with @cor-weyl-perturbation.
4. What is \( \min\{\norm{\A - \B}_2 : \rank\B \le k\} \), and what is the corresponding Frobenius-norm minimum? Which of the two is larger, and why?
5. Decide whether the statement is correct, and justify: "a square matrix with a very small determinant is close to a singular matrix".
:::
::::

::: {.solution}
(a) See @thm-singular-value-minmax: \( \sigma_k(\A) \) is the minimum, over subspaces \( W \le F^n \) of dimension \( n - k + 1 \), of \( \max\{\norm{\A\x}/\norm{\x} : \0 \ne \x \in W\} \); equivalently the maximum, over subspaces of dimension \( k \), of the corresponding minimum.

(b) It converts a statement about the rectangular matrix \( \A \), which has no eigenvalues, into a statement about the Hermitian matrix \( \A^{*}\A \), which has the whole of Sections 1 to 8 available; and the conversion loses nothing, because the square root is increasing.

(c) \( \lvert\sigma_i(\A + \E) - \sigma_i(\A)\rvert \le \norm{\E}_2 \), for **arbitrary** \( \A, \E \in M_{m\times n}(F) \) — no symmetry, no smallness, no squareness. @cor-weyl-perturbation is the same bound for eigenvalues, but it requires both \( \A \) and \( \E \) to be Hermitian, and @exm-jordan-block-perturbation shows the bound is false without that.

(d) \( \sigma_{k+1}(\A) \) in the spectral norm (@thm-eckart-young-spectral) and \( \bigl(\sum_{i>k}\sigma_i^2\bigr)^{1/2} \) in the Frobenius norm (@thm-eckart-young). The Frobenius value is the larger, since \( \sum_{i>k}\sigma_i^2 \ge \sigma_{k+1}^2 \); it charges for every discarded singular value, the spectral norm only for the biggest.

(e) Incorrect. Nearness to singularity is measured by \( \sigma_n \), not by \( \det \) (@cor-distance-to-singular). The matrix \( 10^{-6}\I_{10} \) has determinant \( 10^{-60} \) and relative distance \( 1 \) to the singular matrices, the largest possible value. The determinant is the product of all the singular values and cannot report the smallest one.
:::

### B. Practice

:::: {#exr-singular-values-variationally-b1}
[B1: Two norms, one list of singular values]

A matrix \( \A \in M_{5\times4}(\nR) \) has singular values \( 8, 4, 4, 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \min\{\norm{\A - \B}_2 : \rank\B \le k\} \) for \( k = 0, 1, 2, 3 \).
2. Compute the corresponding Frobenius minima and say for which \( k \) the two agree.
3. Compute \( \kappa_2(\A) \) and the relative distance from \( \A \) to the set of matrices of rank at most \( 3 \).
:::
::::

::: {.solution}
(a) By @thm-eckart-young-spectral the minimum is \( \sigma_{k+1} \), so the four values are \( 8, 4, 4, 1 \) for \( k = 0, 1, 2, 3 \).

(b) By @thm-eckart-young the minimum is \( \bigl(\sum_{i>k}\sigma_i^2\bigr)^{1/2} \):
\[
\sqrt{64+16+16+1} = \sqrt{97}, \quad \sqrt{33}, \quad \sqrt{17}, \quad 1
\]
for \( k = 0, 1, 2, 3 \), approximately \( 9.849,\ 5.745,\ 4.123,\ 1 \). They agree only at \( k = 3 \), where exactly one singular value is discarded.

(c) \( \A \) has rank \( 4 \) and full column rank, so @def-condition-number gives \( \kappa_2(\A) = \sigma_1/\sigma_4 = 8 \). The distance to the matrices of rank at most \( 3 \) is \( \sigma_4 = 1 \) and \( \norm{\A}_2 = 8 \), so the relative distance is \( \tfrac18 = 1/\kappa_2(\A) \) — the rectangular analogue of @cor-distance-to-singular, and for the same reason.
:::

:::: {#exr-singular-values-variationally-b2}
[B2: The nearest singular matrix]

Let \( \A = \begin{pmatrix} 2 & 1 \\ 1 & 1\end{pmatrix} \), whose condition number \( \kappa_2(\A) = \tfrac{7 + 3\sqrt5}{2} \approx 6.854 \) was computed in @exm-condition-numbers-2x2.

::: {.enumerate options="label=(\alph*)"}
1. Find the singular values of \( \A \) and the distance from \( \A \) to the nearest singular matrix.
2. Write down a singular matrix at exactly that distance, and check that it is singular.
3. Compute the relative distance and compare it with \( 1/\kappa_2(\A) \).
:::
::::

::: {.solution}
(a) \( \A \) is symmetric with \( \tr\A = 3 \) and \( \det\A = 1 \), so its eigenvalues are \( (3 \pm \sqrt5)/2 \), both positive; hence these are also its singular values,
\[
\sigma_1 = \tfrac{3+\sqrt5}{2} \approx 2.618, \qquad \sigma_2 = \tfrac{3-\sqrt5}{2} \approx 0.382 .
\]
By @cor-distance-to-singular the distance to the nearest singular matrix is \( \sigma_2 = (3-\sqrt5)/2 \).

(b) The witness is \( \A_1 = \sigma_1\v_1\v_1\tp \), where \( \v_1 \) is a unit eigenvector for \( \sigma_1 \). From \( (2 - \sigma_1)x_1 + x_2 = 0 \) we may take \( \v_1 \) parallel to \( (2, \sqrt5 - 1) \), whose squared length is \( 4 + (6 - 2\sqrt5) = 10 - 2\sqrt5 \). Hence
\[
\A_1 = \frac{3+\sqrt5}{2}\cdot\frac{1}{10 - 2\sqrt5}\begin{pmatrix} 4 & 2(\sqrt5-1) \\ 2(\sqrt5-1) & 6 - 2\sqrt5\end{pmatrix}
= \begin{pmatrix} 1 + \tfrac{2\sqrt5}{5} & \tfrac12 + \tfrac{3\sqrt5}{10} \\[2pt] \tfrac12 + \tfrac{3\sqrt5}{10} & \tfrac12 + \tfrac{\sqrt5}{10}\end{pmatrix} ,
\]
approximately \( \begin{psmallmatrix} 1.894 & 1.171 \\ 1.171 & 0.724\end{psmallmatrix} \). It is singular: it is a scalar multiple of \( \v_1\v_1\tp \), which has rank \( 1 \), so its determinant is \( 0 \). (Directly: \( 1.894 \times 0.724 - 1.171^2 = 0 \) to three decimals.)

(c) \( \norm{\A}_2 = \sigma_1 \), so the relative distance is
\[
\frac{\sigma_2}{\sigma_1} = \frac{3 - \sqrt5}{3 + \sqrt5} = \frac{(3-\sqrt5)^2}{4} = \frac{7 - 3\sqrt5}{2} \approx 0.1459 ,
\]
using \( (3-\sqrt5)(3+\sqrt5) = 4 \). And \( 1/\kappa_2(\A) = 2/(7 + 3\sqrt5) = (7 - 3\sqrt5)/2 \), since \( (7+3\sqrt5)(7-3\sqrt5) = 49 - 45 = 4 \). The two agree, as @cor-distance-to-singular says.
:::

:::: {#exr-singular-values-variationally-b3}
[B3: Interlacing by hand]

Let \( \A = \begin{pmatrix} 2 & 0 \\ 0 & 1 \\ 0 & 2\end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Compute the singular values of \( \A \).
2. Compute the singular values of each of the three matrices obtained by deleting one row, and check @thm-singular-value-interlacing in each case.
:::
::::

::: {.solution}
(a) \( \A\tp\A = \begin{psmallmatrix} 4 & 0 \\ 0 & 5\end{psmallmatrix} \), so the eigenvalues are \( 5 \) and \( 4 \) and \( \sigma_1(\A) = \sqrt5 \approx 2.236 \), \( \sigma_2(\A) = 2 \).

(b) Deleting row \( 1 \) leaves \( \begin{psmallmatrix} 0 & 1 \\ 0 & 2\end{psmallmatrix} \), with \( \B\tp\B = \diag(0, 5) \), so \( \sigma_1 = \sqrt5 \), \( \sigma_2 = 0 \); the chain reads \( \sqrt5 \ge \sqrt5 \ge 2 \ge 0 \).

Deleting row \( 2 \) leaves \( \begin{psmallmatrix} 2 & 0 \\ 0 & 2\end{psmallmatrix} \), with singular values \( 2, 2 \); the chain reads \( \sqrt5 \ge 2 \ge 2 \ge 2 \).

Deleting row \( 3 \) leaves \( \begin{psmallmatrix} 2 & 0 \\ 0 & 1\end{psmallmatrix} \), with singular values \( 2, 1 \); the chain reads \( \sqrt5 \ge 2 \ge 2 \ge 1 \).

All three satisfy \( \sigma_1(\A) \ge \sigma_1(\B) \ge \sigma_2(\A) \ge \sigma_2(\B) \), as @thm-singular-value-interlacing requires.
:::

### C. Going deeper

:::: {#exr-singular-values-variationally-c1}
[C1: Rank cannot drop suddenly]

Let \( \A \in M_{m\times n}(F) \) have rank \( r \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that every \( \B \in M_{m\times n}(F) \) with \( \norm{\A - \B}_2 < \sigma_r(\A) \) has \( \rank\B \ge r \).
2. Deduce that for every \( \A \) there is an \( \varepsilon > 0 \) such that every \( \B \) within \( \varepsilon \) of \( \A \) in the spectral norm has \( \rank\B \ge \rank\A \).
3. Show that the reverse inequality can fail however small \( \varepsilon \) is: give matrices \( \A \) and \( \B \) with \( \norm{\A - \B}_2 \) as small as we like and \( \rank\B > \rank\A \).
:::

*Hint: for (a), argue by contradiction with @thm-eckart-young-spectral.*
::::

::: {.solution}
(a) Suppose \( \rank\B \le r - 1 \). By @thm-eckart-young-spectral with \( k = r - 1 \),
\[
\norm{\A - \B}_2 \ \ge\ \sigma_{r}(\A) ,
\]
contradicting the hypothesis. Hence \( \rank\B \ge r \).

(b) If \( \A = 0 \) any \( \varepsilon > 0 \) works, since then \( r = 0 \) and every \( \B \) has rank at least \( 0 \). Otherwise take \( \varepsilon = \sigma_r(\A) \), which is \( > 0 \) because \( \A \) has exactly \( r = \rank\A \) non-zero singular values (@thm-compact-svd). Then (a) applies.

(c) Take \( \A = \diag(1, 0) \), of rank \( 1 \), and \( \B = \diag(1, \delta) \) with \( \delta > 0 \). Then \( \A - \B = \diag(0, -\delta) \), so \( \norm{\A - \B}_2 = \delta \), as small as we like, while \( \rank\B = 2 > 1 = \rank\A \). Rank can jump **up** under an arbitrarily small perturbation, and never jumps down under a small one: that asymmetry is exactly (a), and it is why numerical rank is defined by a threshold on the singular values rather than by exact vanishing.
:::

:::: {#exr-singular-values-variationally-c2}
[C2: The dilation, and a second proof of the perturbation bound]

Let \( \A, \E \in M_{m\times n}(F) \) and let \( \cH(\cdot) \) be the Hermitian dilation of @prp-hermitian-dilation.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \cH(\A + \E) = \cH(\A) + \cH(\E) \) and that \( \cH(\E) \) is Hermitian.
2. Prove that \( \norm{\cH(\E)}_2 = \norm{\E}_2 \).
3. Hence give a second proof of @cor-singular-value-perturbation for \( 1 \le i \le p \), using @cor-weyl-perturbation, and say in one sentence why this route explains the absence of hypotheses on \( \E \).
:::

*Hint: for (b), use @prp-hermitian-dilation and @thm-operator-norm-formulas (c).*
::::

::: {.solution}
(a) Both claims are immediate from the block form: \( \cH \) is built entrywise from \( \A \) and \( \A^{*} \), and both \( \A \mapsto \A \) and \( \A \mapsto \A^{*} \) are additive, so
\[
\cH(\A + \E) = \begin{pmatrix} \0 & \A + \E \\ \A^{*} + \E^{*} & \0\end{pmatrix} = \cH(\A) + \cH(\E) .
\]
That \( \cH(\E) \) is Hermitian was proved in @prp-hermitian-dilation, which places no hypothesis on its argument.

(b) Write \( \M = \cH(\E) \), which is Hermitian by (a). Then \( \M^{*}\M = \M^2 \), whose eigenvalues are the squares of those of \( \M \) (apply @cor-spectral-complex-matrix to \( \M \) and square the diagonal). By @prp-hermitian-dilation the eigenvalues of \( \M \) are \( \pm\sigma_i(\E) \) for \( i \le p \) together with zeros, so the eigenvalues of \( \M^{*}\M \) are the numbers \( \sigma_i(\E)^2 \), each twice, together with zeros. The largest is \( \sigma_1(\E)^2 \), so \( \sigma_1(\M) = \sigma_1(\E) \) by @def-singular-values, and @thm-operator-norm-formulas (c) turns this into \( \norm{\cH(\E)}_2 = \norm{\E}_2 \).

(c) Let \( 1 \le i \le p \). By @prp-hermitian-dilation the largest \( p \) eigenvalues of \( \cH(\A) \) are \( \sigma_1(\A) \ge \dots \ge \sigma_p(\A) \), all of the remaining ones being \( \le 0 \); so \( \lambda_i(\cH(\A)) = \sigma_i(\A) \), and likewise \( \lambda_i(\cH(\A + \E)) = \sigma_i(\A + \E) \). By (a), \( \cH(\A+\E) = \cH(\A) + \cH(\E) \) with \( \cH(\A) \) and \( \cH(\E) \) both Hermitian, so @cor-weyl-perturbation applies and gives
\[
\lvert\sigma_i(\A + \E) - \sigma_i(\A)\rvert = \lvert\lambda_i(\cH(\A+\E)) - \lambda_i(\cH(\A))\rvert \le \norm{\cH(\E)}_2 = \norm{\E}_2 .
\]
The route explains the missing hypotheses: @cor-weyl-perturbation demands that the perturbation be Hermitian, and \( \cH(\E) \) **is** Hermitian for every \( \E \) whatsoever. Passing to the dilation manufactures the hypothesis instead of assuming it.
:::
