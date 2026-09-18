# Polar Decomposition and Takagi's Factorization

Every non-zero complex number is a rotation times a stretch, \( z = e^{i\theta}r \) with \( r = \lvert z\rvert > 0 \). Section 8 has put the matrix version within reach: if \( \A = \U\vSigma\V^{*} \), then inserting \( \V^{*}\V = \I \) in the middle splits the factorization into a unitary part and a positive semidefinite part. This section carries that out, proves that the unitary part is the closest unitary matrix to \( \A \), and then treats a factorization that looks like the singular value decomposition but is not: Takagi's, for complex **symmetric** matrices.

The field is \( \nC \) unless stated otherwise, and \( \lvert\A\rvert = (\A^{*}\A)^{1/2} \) is the matrix absolute value of @def-matrix-absolute-value.

## Rotation times stretch

::: {#thm-polar-decomposition}
[Polar Decomposition]

Let \( \A \in M_n(\nC) \). Then there is a unitary \( \W \in M_n(\nC) \) with
\[
\A = \W\lvert\A\rvert .
\]
The positive semidefinite factor \( \lvert\A\rvert \) is determined by \( \A \). The unitary factor \( \W \) is determined by \( \A \) if and only if \( \A \) is invertible, and then \( \W = \A\lvert\A\rvert^{-1} \). Moreover the same \( \W \) satisfies the right-handed identity
\[
\A = \lvert\A^{*}\rvert\,\W ,
\qquad \lvert\A^{*}\rvert = \W\lvert\A\rvert\W^{*} .
\]
:::

::: {.idea}
The singular value decomposition already separates the two kinds of behavior: \( \U \) and \( \V^{*} \) rotate, and \( \vSigma \) stretches along the axes. Writing \( \U\vSigma\V^{*} = (\U\V^{*})(\V\vSigma\V^{*}) \) puts all the rotating in the first bracket and all the stretching in the second, and the second bracket is a positive semidefinite matrix whose square is \( \A^{*}\A \). Uniqueness of the positive semidefinite square root does the rest. For the uniqueness of \( \W \), notice that \( \W \) is pinned down only where \( \lvert\A\rvert \) is invertible; when \( \A = \0 \), every unitary works.
:::

::: {.proof}
**Existence.** By @thm-svd write \( \A = \U\vSigma\V^{*} \) with \( \U, \V \in M_n(\nC) \) unitary and \( \vSigma = \diag(\sigma_1, \dots, \sigma_n) \) with \( \sigma_i \ge 0 \). Put
\[
\W \coloneqq \U\V^{*}, \qquad \P \coloneqq \V\vSigma\V^{*} .
\]
Then \( \W \) is unitary, being a product of unitary matrices, and
\[
\W\P = \U\V^{*}\V\vSigma\V^{*} = \U\vSigma\V^{*} = \A .
\]
The matrix \( \P \) is self-adjoint, since \( \P^{*} = \V\vSigma^{*}\V^{*} = \P \), and positive semidefinite: its eigenvalues are the \( \sigma_i \ge 0 \) because \( \V^{*}\P\V = \vSigma \), so @thm-psd-characterizations applies. Finally
\[
\P^2 = \V\vSigma\V^{*}\V\vSigma\V^{*} = \V\vSigma^2\V^{*} = \A^{*}\A ,
\]
the last equality because \( \A^{*}\A = \V\vSigma\U^{*}\U\vSigma\V^{*} = \V\vSigma^2\V^{*} \). A positive semidefinite matrix has exactly one positive semidefinite square root (@thm-psd-square-root), so \( \P = (\A^{*}\A)^{1/2} = \lvert\A\rvert \), and \( \A = \W\lvert\A\rvert \).

**The factor \( \lvert\A\rvert \) is determined**, since \( \A^{*}\A \) is and the square root is unique.

**Uniqueness of \( \W \).** \( (\Rightarrow) \) Suppose \( \A \) is invertible. Then \( \lvert\A\rvert^2 = \A^{*}\A \) is invertible, so \( \lvert\A\rvert \) is, and any \( \W \) with \( \A = \W\lvert\A\rvert \) satisfies \( \W = \A\lvert\A\rvert^{-1} \): there is only one. \( (\Leftarrow) \) Suppose \( \A \) is not invertible, so there is a non-zero \( \z \in \ker\A \). Let \( \H = \H_{\z} \) be the Householder reflection of @def-householder-reflection, which is unitary with \( \H\z = -\z \) and \( \H\v = \v \) for every \( \v \perp \z \) (@prp-householder-properties (c), (d)). By @prp-absolute-value-properties, \( \nul\lvert\A\rvert = \nul\A \), and \( \lvert\A\rvert \) is self-adjoint, so
\[
\col\lvert\A\rvert = \col\bigl(\lvert\A\rvert^{*}\bigr) = \bigl(\nul\lvert\A\rvert\bigr)^{\perp} = (\nul\A)^{\perp} \subseteq \z^{\perp}
\]
by @thm-four-subspaces-orthogonal (b). Hence \( \H \) fixes every vector of \( \col\lvert\A\rvert \), that is, \( \H\lvert\A\rvert = \lvert\A\rvert \), and therefore \( (\W\H)\lvert\A\rvert = \A \) as well, with \( \W\H \) unitary and \( \W\H \neq \W \) because \( \H \neq \I \) and \( \W \) is invertible. So \( \W \) is not determined.

**The right-handed form.** Set \( \Q \coloneqq \W\lvert\A\rvert\W^{*} \). It is self-adjoint and positive semidefinite, being a unitary congruence of a positive semidefinite matrix: \( \x^{*}\Q\x = (\W^{*}\x)^{*}\lvert\A\rvert(\W^{*}\x) \ge 0 \). And
\[
\Q^2 = \W\lvert\A\rvert^2\W^{*} = \W\A^{*}\A\W^{*} = \A\A^{*} ,
\]
using \( \A = \W\lvert\A\rvert \), so \( \A^{*} = \lvert\A\rvert\W^{*} \) and \( \A\A^{*} = \W\lvert\A\rvert^2\W^{*} \). By uniqueness of the square root again, \( \Q = (\A\A^{*})^{1/2} = \lvert\A^{*}\rvert \). Therefore \( \lvert\A^{*}\rvert\W = \W\lvert\A\rvert\W^{*}\W = \W\lvert\A\rvert = \A \). This proves the theorem.
:::

::: {.remark}
There is a second route to existence, the one @prp-absolute-value-properties was pointing at: the identity \( \norm{\lvert\A\rvert\x} = \norm{\A\x} \) says that \( \lvert\A\rvert\x \mapsto \A\x \) is a well-defined isometry from \( \col\lvert\A\rvert \) onto \( \col\A \), and extending it by any isometry between the orthogonal complements produces \( \W \) directly. That proof shows more clearly *where* the freedom in \( \W \) lives, but it needs the extension step written out; the route above borrows all of that from @thm-svd.
:::

For \( n = 1 \) the theorem is exactly \( z = e^{i\theta}\lvert z\rvert \): a \( 1 \times 1 \) unitary matrix is a complex number of modulus \( 1 \), and \( \lvert\A\rvert \) is the modulus. The non-uniqueness for singular \( \A \) is the matrix version of the fact that \( \theta \) is undefined when \( z = 0 \).

::: {#exm-polar-2x2}
[A polar decomposition]

Find the left and right polar decompositions of \( \A = \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix} \).
:::

::: {.solution}
@exr-singular-value-decomposition-b1 gives the singular value decomposition
\[
\U = \tfrac{1}{\sqrt{10}}\begin{pmatrix} 1 & 3 \\ 3 & -1 \end{pmatrix},
\quad
\vSigma = \sqrt5\begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix},
\quad
\V = \tfrac{1}{\sqrt2}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}.
\]
Hence
\[
\begin{aligned}
\W &= \U\V\tp = \tfrac{1}{\sqrt{20}}\begin{pmatrix} 1 & 3 \\ 3 & -1 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}
= \tfrac{1}{\sqrt5}\begin{pmatrix} 2 & -1 \\ 1 & 2 \end{pmatrix}, \\[4pt]
\lvert\A\rvert &= \V\vSigma\V\tp = \sqrt5\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} .
\end{aligned}
\]
Check: \( \lvert\A\rvert^2 = 5\begin{pmatrix} 5 & 4 \\ 4 & 5 \end{pmatrix} = \begin{pmatrix} 25 & 20 \\ 20 & 25 \end{pmatrix} = \A\tp\A \), the columns of \( \W \) are orthonormal, and \( \W\lvert\A\rvert = \A \). Here \( \W \) is a rotation, since \( \det\W = (4+1)/5 = 1 \).

For the right-handed form, \( \A\A\tp = \begin{pmatrix} 9 & 12 \\ 12 & 41 \end{pmatrix} \) and
\[
\lvert\A^{*}\rvert = \W\lvert\A\rvert\W\tp = \tfrac{\sqrt5}{5}\begin{pmatrix} 6 & 3 \\ 3 & 14 \end{pmatrix},
\]
whose square is indeed \( \tfrac15\begin{pmatrix} 45 & 60 \\ 60 & 205 \end{pmatrix} = \A\A\tp \). The two absolute values differ, and that is not an accident.
:::

::: {.remark}
\( \lvert\A\rvert = \lvert\A^{*}\rvert \) exactly when \( \A \) is normal. Indeed \( \A^{*}\A = \A\A^{*} \) if and only if the two positive semidefinite square roots agree, by uniqueness. So for a normal matrix — and only then — the stretching looks the same before and after the rotation, and \( \W \) commutes with \( \lvert\A\rvert \) by the identity \( \lvert\A^{*}\rvert = \W\lvert\A\rvert\W^{*} \).
:::

::: {.check}
What is the polar decomposition of a unitary matrix? Of a positive semidefinite matrix?
:::

::: {.solution}
If \( \A \) is unitary then \( \A^{*}\A = \I \), so \( \lvert\A\rvert = \I \) and \( \W = \A \): all rotation, no stretch. If \( \A \succeq 0 \) then \( \A^{*}\A = \A^2 \) and \( \A \) is itself a positive semidefinite square root of \( \A^2 \), so \( \lvert\A\rvert = \A \) by uniqueness (@thm-psd-square-root) and \( \W = \I \) whenever \( \A \) is invertible: all stretch, no rotation.
:::

## The nearest unitary matrix

The polar factor is not merely *a* unitary matrix attached to \( \A \). It is the one closest to \( \A \), measured in the Frobenius norm of Chapter 11 §11. This is the reason the polar decomposition is used in practice: given a matrix that ought to be unitary but has drifted, \( \W \) is how to put it back.

::: {#cor-unitary-nearest}
[The Polar Factor Is the Nearest Unitary Matrix]

Let \( \A \in M_n(\nC) \) with polar decomposition \( \A = \W\lvert\A\rvert \). Then
\[
\norm{\A - \W}_F \le \norm{\A - \Q}_F
\qquad \text{for every unitary } \Q \in M_n(\nC),
\]
and the minimum value is \( \bigl(\norm{\A}_F^2 + n - 2\sum_i\sigma_i\bigr)^{1/2} \). If \( \A \) is invertible, \( \W \) is the **only** unitary matrix attaining the minimum.
:::

::: {.idea}
Two moves. First, the Frobenius norm does not see unitary factors (@lem-frobenius-unitarily-invariant), so sandwiching by \( \U^{*} \) and \( \V \) turns the problem into: among unitary \( \Z \), which is closest to the diagonal matrix \( \vSigma \)? Second, expanding \( \norm{\vSigma - \Z}_F^2 \) leaves only the diagonal entries of \( \Z \) to be chosen, and each of them has modulus at most \( 1 \) because it sits in a unit column. So the best possible \( \Z \) is \( \I \), and translating back gives \( \Q = \U\V^{*} = \W \).
:::

::: {.proof}
Fix a singular value decomposition \( \A = \U\vSigma\V^{*} \) as in @thm-svd, so that \( \W = \U\V^{*} \) as in the proof of @thm-polar-decomposition. Let \( \Q \) be unitary and put \( \Z \coloneqq \U^{*}\Q\V \), which is unitary; as \( \Q \) runs over all unitary matrices so does \( \Z \), since \( \Q = \U\Z\V^{*} \). By @lem-frobenius-unitarily-invariant, applied with the unitary factors \( \U^{*} \) on the left and \( \V \) on the right,
\[
\norm{\A - \Q}_F = \norm{\U^{*}(\A - \Q)\V}_F = \norm{\vSigma - \Z}_F .
\]
Expanding the square in the Frobenius inner product \( \inner{\X}{\Y} = \tr(\Y^{*}\X) \) of Chapter 10 §01,

\[
\begin{aligned}
\norm{\vSigma - \Z}_F^2
&= \norm{\vSigma}_F^2 + \norm{\Z}_F^2 - 2\operatorname{Re}\tr(\Z^{*}\vSigma) \\
&= \sum_{i=1}^{n}\sigma_i^2 + n - 2\sum_{i=1}^{n}\sigma_i\operatorname{Re}z_{ii} ,
\end{aligned}
\]{#eq-nearest-unitary-expand}

where \( \norm{\Z}_F^2 = \tr(\Z^{*}\Z) = \tr\I_n = n \), and \( \tr(\Z^{*}\vSigma) = \sum_i (\Z^{*})_{ii}\sigma_i = \sum_i \conj{z_{ii}}\sigma_i \), whose real part is \( \sum_i \sigma_i\operatorname{Re}z_{ii} \).

Column \( i \) of \( \Z \) is a unit vector, so \( \lvert z_{ii}\rvert \le 1 \) and hence \( \operatorname{Re}z_{ii} \le 1 \). Since every \( \sigma_i \ge 0 \),
\[
\sum_{i=1}^{n}\sigma_i\operatorname{Re}z_{ii} \le \sum_{i=1}^{n}\sigma_i ,
\]
so @eq-nearest-unitary-expand gives \( \norm{\A - \Q}_F^2 \ge \sum_i\sigma_i^2 + n - 2\sum_i\sigma_i \) for every unitary \( \Q \). Taking \( \Q = \W = \U\V^{*} \) makes \( \Z = \U^{*}\U\V^{*}\V = \I_n \), for which \( \operatorname{Re}z_{ii} = 1 \) for every \( i \) and the bound is attained. Since \( \norm{\A}_F^2 = \sum_i\sigma_i^2 \) by @exr-singular-value-decomposition-c1, the minimum value is as stated.

Now suppose \( \A \) is invertible, so \( \sigma_i > 0 \) for every \( i \), and suppose \( \Q \) attains the minimum. Then \( \sum_i\sigma_i(1 - \operatorname{Re}z_{ii}) = 0 \) is a sum of non-negative terms, so \( \operatorname{Re}z_{ii} = 1 \) for every \( i \); with \( \lvert z_{ii}\rvert \le 1 \) this forces \( z_{ii} = 1 \). Column \( i \) of \( \Z \) then has a coordinate equal to \( 1 \) and total squared length \( 1 \), so all its other coordinates vanish and the column is \( \e_i \). Hence \( \Z = \I_n \) and \( \Q = \U\Z\V^{*} = \W \). This proves the corollary.
:::

For \( \A = \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix} \) of @exm-polar-2x2, with \( \sigma_1 = 3\sqrt5 \), \( \sigma_2 = \sqrt5 \) and \( \norm{\A}_F^2 = 50 \), the nearest unitary matrix is \( \W = \tfrac1{\sqrt5}\begin{pmatrix} 2 & -1 \\ 1 & 2 \end{pmatrix} \) and the distance to the unitary group is \( \sqrt{52 - 8\sqrt5} \), about \( 5.84 \).

::: {.warning}
The corollary is a statement about the **Frobenius** norm. A different way of measuring distance can have a different minimizer, and "nearest" always needs its yardstick named. It is true, though not proved here, that \( \W \) also minimizes the distance in every unitarily invariant norm; Chapter 20 takes up that family of norms.
:::

## Takagi's factorization

A complex matrix can be symmetric, \( \A\tp = \A \), without being Hermitian, \( \A^{*} = \A \). Over \( \nR \) the two coincide and Chapter 11 handled them; over \( \nC \) they are genuinely different conditions, and symmetry is much the weaker one. It does not imply normality, it does not imply diagonalizability, and it says nothing about the eigenvalues. Here is the standing example:
\[
\N = \begin{pmatrix} 1 & i \\ i & -1 \end{pmatrix},
\qquad \N\tp = \N, \qquad \N^2 = \0 .
\]
A non-zero matrix with \( \N^2 = \0 \) has minimal polynomial \( x^2 \) and is therefore not diagonalizable, so no version of the spectral theorem can apply to \( \N \). Nevertheless something survives, and it is a statement about singular values rather than eigenvalues.

::: {#thm-takagi}
[Takagi's Factorization]

Let \( \A \in M_n(\nC) \) be **symmetric**, \( \A\tp = \A \), with singular values \( \sigma_1 \ge \dots \ge \sigma_n \ge 0 \). Then there is a unitary \( \U \in M_n(\nC) \) with
\[
\A = \U\vSigma\U\tp ,
\qquad \vSigma = \diag(\sigma_1, \dots, \sigma_n).
\]
:::

Read the statement against the two theorems it resembles.

- **Against the singular value decomposition.** @thm-svd gives \( \A = \U\vSigma\V^{*} \) with two unrelated unitary matrices. Since \( \U\tp = (\conj{\U})^{*} \), Takagi's identity says \( \A = \U\vSigma(\conj{\U})^{*} \): it is a singular value decomposition in which the right factor is forced to be \( \V = \conj{\U} \). So the content is not a new diagonal matrix but a relation between \( \U \) and \( \V \).
- **Against the spectral theorem.** @cor-spectral-complex-matrix writes a normal \( \A \) as \( \U\D\U^{*} \), a *similarity*, with the eigenvalues of \( \A \) on the diagonal. Takagi writes a symmetric \( \A \) as \( \U\vSigma\U\tp \), which is a *congruence* \( \X \mapsto \U\X\U\tp \), with the singular values on the diagonal. The hypotheses are different (symmetric, not normal), the diagonal holds different numbers, and the transpose is not the conjugate transpose.

The difference is visible even for a real matrix. Take \( \A = \begin{pmatrix} 3 & 4 \\ 4 & -3 \end{pmatrix} \), which is real symmetric with eigenvalues \( 5 \) and \( -5 \). @cor-spectral-real-matrix gives \( \A = \Q\diag(5,-5)\Q\tp \) with \( \Q \) real orthogonal. Takagi insists on the **non-negative** diagonal \( \diag(5,5) \), and no real \( \U \) can achieve that, since \( \U\diag(5,5)\U\tp = 5\U\U\tp = 5\I \) for real orthogonal \( \U \). A genuinely complex \( \U \) is needed, and @exm-takagi-2x2 finds one.

::: {.idea}
Four steps, and the first two are the polar decomposition doing the work. ① Symmetry makes \( \A \) intertwine \( \A^{*}\A \) with its conjugate: \( \A(\A^{*}\A) = \overline{(\A^{*}\A)}\A \). Because the positive square root is a polynomial in the matrix, the same relation passes to \( \lvert\A\rvert \). ② That relation, combined with \( \A\tp = \A \), forces the polar factor \( \W \) to be a **symmetric** unitary matrix. ③ A symmetric unitary matrix factors as \( \V\V\tp \): split it into real and imaginary parts, which turn out to be commuting real symmetric matrices, and use Chapter 11's simultaneous diagonalization. ④ Conjugating \( \A \) by that \( \V \) in the right way produces a matrix that is both symmetric and Hermitian, hence **real** symmetric, and the real spectral theorem finishes the job. We prove all of this for invertible \( \A \), where the polar factor is unique and \( \lvert\A\rvert^{-1} \) exists.
:::

::: {.proof}
We prove the theorem for **invertible** \( \A \). Throughout, \( \A\tp = \A \), so \( \A^{*} = \conj{\A\tp} = \conj{\A} \). Write \( \M \coloneqq \A^{*}\A = \conj{\A}\A \) and \( \P \coloneqq \lvert\A\rvert = \M^{1/2} \). Since \( \A \) is invertible, so are \( \M \) and \( \P \), and \( \M \succ 0 \).

**Step 1: \( \A\M = \conj{\M}\A \) and \( \A\P = \conj{\P}\A \).** For the first, \( \conj{\M} = \conj{\conj{\A}\A} = \A\conj{\A} \), so
\[
\A\M = \A\conj{\A}\A = \conj{\M}\A .
\]
For the second we need a polynomial.

::: {.claim}
There is a polynomial \( p \) with **real** coefficients such that \( p(\M) = \P \) and \( p(\conj{\M}) = \conj{\P} \).
:::

::: {.proof}
By @thm-psd-square-root (a) there is a polynomial \( p \) with real coefficients such that \( p(\M) = \M^{1/2} = \P \). Conjugating every entry of the identity \( \P = p(\M) \), and using that the coefficients of \( p \) are real so that conjugation passes through them, gives \( \conj{\P} = p(\conj{\M}) \).
:::

Iterating Step 1's first identity gives \( \A\M^j = \conj{\M}^j\A \) for every \( j \ge 0 \), hence \( \A\,p(\M) = p(\conj{\M})\,\A \) for every polynomial \( p \), and with the claim's \( p \) this reads

\[
\A\P = \conj{\P}\A .
\]{#eq-takagi-intertwine}

**Step 2: the polar factor is symmetric.** By @thm-polar-decomposition, \( \A = \W\P \) with \( \W = \A\P^{-1} \) unitary. Substituting \( \A = \W\P \) into @eq-takagi-intertwine gives \( \W\P^2 = \conj{\P}\W\P \), and canceling the invertible \( \P \) on the right,
\[
\W\P = \conj{\P}\,\W .
\]
On the other hand \( \P \) is Hermitian, so \( \P\tp = \conj{\P} \), and transposing \( \A = \W\P \) while using \( \A\tp = \A \) gives
\[
\W\P = \A = \A\tp = \P\tp\W\tp = \conj{\P}\,\W\tp .
\]
Comparing the two displays, \( \conj{\P}\W = \conj{\P}\W\tp \), and \( \conj{\P} \) is invertible, so \( \W\tp = \W \).

**Step 3: a symmetric unitary matrix is \( \V\V\tp \).**

::: {.claim}
Let \( \W \in M_n(\nC) \) be unitary with \( \W\tp = \W \). Then \( \W = \V\V\tp \) for some unitary \( \V \).
:::

::: {.proof}
From \( \W^{-1} = \W^{*} = \conj{\W\tp} = \conj{\W} \) we get \( \conj{\W}\W = \I \). Write \( \W = \X + i\Y \) with \( \X = \tfrac12(\W + \conj{\W}) \) and \( \Y = \tfrac1{2i}(\W - \conj{\W}) \), both **real** matrices, and both symmetric because \( \W \) and \( \conj{\W} \) are. Then
\[
\I = \conj{\W}\W = (\X - i\Y)(\X + i\Y) = \X^2 + \Y^2 + i(\X\Y - \Y\X),
\]
and since \( \X^2 + \Y^2 \) and \( \X\Y - \Y\X \) are real matrices, comparing real and imaginary parts gives
\[
\X^2 + \Y^2 = \I, \qquad \X\Y = \Y\X .
\]
So \( \X \) and \( \Y \) are commuting real symmetric matrices, and @cor-simultaneous-orthogonal-real supplies \( \Q \in \Orth(n) \) with \( \Q\tp\X\Q = \diag(x_1, \dots, x_n) \) and \( \Q\tp\Y\Q = \diag(y_1, \dots, y_n) \). Hence \( \Q\tp\W\Q = \diag(x_1 + iy_1, \dots, x_n + iy_n) \), and \( x_j^2 + y_j^2 = 1 \) for every \( j \) by the first relation. Each \( x_j + iy_j \) therefore has modulus \( 1 \). The polynomial \( x^2 - (x_j + iy_j) \) has a root \( c_j \in \nC \) by @thm-fundamental-theorem-of-algebra, and \( \lvert c_j\rvert^2 = \lvert c_j^2\rvert = 1 \), so \( \lvert c_j \rvert = 1 \). Put \( \C = \diag(c_1, \dots, c_n) \) and \( \V \coloneqq \Q\C \), which is unitary as a product of unitary matrices. Since \( \Q \) is real orthogonal, \( \Q\tp = \Q^{-1} \), and \( \C\tp = \C \), so
\[
\V\V\tp = \Q\C\C\tp\Q\tp = \Q\C^2\Q\tp = \Q\,\diag(x_j + iy_j)\,\Q\tp = \W .
\]
This proves the claim.
:::

**Step 4: conjugate to a real matrix.** Take \( \V \) from Step 3, so \( \W = \V\V\tp \), and set
\[
\B \coloneqq \V^{*}\A\conj{\V} .
\]
Three observations. First, \( \B\tp = \B \): using \( (\conj{\V})\tp = \V^{*} \), \( (\V^{*})\tp = \conj{\V} \) and \( \A\tp = \A \),
\[
\B\tp = (\conj{\V})\tp\,\A\tp\,(\V^{*})\tp = \V^{*}\A\conj{\V} = \B .
\]
Second, \( \B \succ 0 \): since \( \A = \W\P = \V\V\tp\P \) and \( \V^{*}\V = \I \),
\[
\B = \V^{*}\V\V\tp\P\conj{\V} = \V\tp\P\conj{\V} = (\conj{\V})^{*}\,\P\,(\conj{\V}) ,
\]
a unitary congruence of the positive definite \( \P \), so \( \x^{*}\B\x = (\conj{\V}\x)^{*}\P(\conj{\V}\x) > 0 \) for \( \x \ne \0 \); in particular \( \B^{*} = \B \). Third, \( \B \) is **real**, because
\[
\conj{\B} = \conj{\B\tp} = \B^{*} = \B ,
\]
the first equality using \( \B\tp = \B \), the second the definition of the conjugate transpose, and the third Hermitian symmetry.

So \( \B \) is a real symmetric positive definite matrix. By @cor-spectral-real-matrix there is \( \Q_0 \in \Orth(n) \) with \( \B = \Q_0\vSigma\Q_0\tp \), where \( \vSigma \) is the diagonal matrix of eigenvalues of \( \B \), which we list in decreasing order. Finally, using \( \V\V^{*} = \I \) and its conjugate \( \conj{\V}\V\tp = \I \),
\[
\V\B\V\tp = \V\V^{*}\A\conj{\V}\V\tp = \A ,
\]
so with \( \U \coloneqq \V\Q_0 \), which is unitary,
\[
\A = \V\Q_0\vSigma\Q_0\tp\V\tp = \U\vSigma\U\tp .
\]
It remains to identify the diagonal. Conjugate-transposing, \( \A^{*} = \conj{\U}\vSigma\U^{*} \), so
\[
\A^{*}\A = \conj{\U}\vSigma\U^{*}\U\vSigma\U\tp = \conj{\U}\,\vSigma^2\,(\conj{\U})^{*} .
\]
This exhibits \( \vSigma^2 \) as the eigenvalue list of \( \A^{*}\A \) in decreasing order, so \( \vSigma = \diag(\sigma_1, \dots, \sigma_n) \) by @def-singular-values. This proves the theorem for invertible \( \A \).
:::

::: {.remark}
**What is left out.** The theorem as stated is true for every complex symmetric \( \A \), singular ones included, and the example below exhibits a singular case. Our proof used invertibility twice: to know that \( \P \) is invertible, so that \( \W = \A\P^{-1} \) is determined and the cancellations of Step 2 are legal. One way to remove the hypothesis is to apply the proved case to \( \A + t\I \), which is symmetric and invertible for all but finitely many \( t \), and let \( t \to 0 \) along a sequence for which the unitary factors converge — a step that needs the compactness of the unitary group, which is analysis this book has not set up. We state the general theorem and prove the invertible case.
:::

::: {#exm-takagi-2x2}
[Takagi for a real symmetric matrix]

Find a Takagi factorization of \( \A = \begin{pmatrix} 3 & 4 \\ 4 & -3 \end{pmatrix} \).
:::

::: {.solution}
First the singular values: \( \A^{*}\A = \A\tp\A = \A^2 = 25\I \), so \( \sigma_1 = \sigma_2 = 5 \) and \( \vSigma = 5\I \). We therefore need a unitary \( \U \) with
\[
\A = 5\,\U\U\tp, \qquad \text{that is} \qquad \U\U\tp = \tfrac15\A .
\]
The matrix \( \tfrac15\A \) is real symmetric and orthogonal, with eigenvalues \( 1 \) and \( -1 \). Its eigenvectors: \( (\A - 5\I)\x = \0 \) reads \( -2x_1 + 4x_2 = 0 \), giving \( \q_1 = \tfrac1{\sqrt5}(2,1) \), and orthogonally \( \q_2 = \tfrac1{\sqrt5}(1,-2) \). So with \( \Q = \tfrac1{\sqrt5}\begin{pmatrix} 2 & 1 \\ 1 & -2 \end{pmatrix} \in \Orth(2) \) we have \( \tfrac15\A = \Q\diag(1,-1)\Q\tp \). The diagonal entries \( 1 \) and \( -1 \) have square roots \( 1 \) and \( i \), so, following Step 3 of @thm-takagi, set
\[
\U = \Q\diag(1, i) = \tfrac{1}{\sqrt5}\begin{pmatrix} 2 & i \\ 1 & -2i \end{pmatrix}.
\]
Then \( \U \) is unitary — its columns \( \tfrac1{\sqrt5}(2,1) \) and \( \tfrac{i}{\sqrt5}(1,-2) \) are orthonormal, since multiplying a real orthonormal pair by unit scalars keeps it orthonormal — and
\[
\U\vSigma\U\tp = 5\,\U\U\tp = \Q\diag(5,-5)\Q\tp = \A .
\]
Note where the complex entries were needed: \( \diag(1,i) \) converted the eigenvalue \( -5 \) of \( \A \) into the singular value \( +5 \).
:::

For a singular example, return to \( \N = \begin{pmatrix} 1 & i \\ i & -1 \end{pmatrix} \). Here \( \N^{*}\N = \begin{pmatrix} 2 & 2i \\ -2i & 2 \end{pmatrix} \), with eigenvalues \( 4 \) and \( 0 \), so \( \sigma_1 = 2 \) and \( \sigma_2 = 0 \). With \( \U = \tfrac1{\sqrt2}\begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix} \), which is unitary, one checks \( \U\diag(2,0)\U\tp = 2\,\u_1\u_1\tp = \N \), where \( \u_1 = \tfrac1{\sqrt2}(1, i) \) is the first column of \( \U \). The theorem holds here even though our proof did not reach it, and even though \( \N \) has no eigenbasis at all.

::: {.warning}
**Symmetric is not Hermitian, and \( \U\tp \) is not \( \U^{*} \).** Takagi's hypothesis is \( \A\tp = \A \) with no conjugation, which over \( \nC \) is a different and weaker condition than \( \A^{*} = \A \); the matrix \( \N \) above is symmetric, is not Hermitian, is not normal and is not diagonalizable. The conclusion likewise carries \( \U\tp \), not \( \U^{*} \): writing \( \U\vSigma\U^{*} \) by mistake would assert that \( \A \) is positive semidefinite, which \( \N \) certainly is not.
:::

## Exercises

### A. Check your understanding

::: {#exr-polar-decomposition-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the polar decomposition, and say which factor is unique and when.
2. What is \( \lvert\A\rvert \), and what identity relates \( \norm{\lvert\A\rvert\x} \) to \( \norm{\A\x} \)?
3. What does the polar decomposition say when \( n = 1 \)?
4. True or false: \( \lvert\A\rvert = \lvert\A^{*}\rvert \) for every square \( \A \). Justify your answer.
5. State Takagi's factorization, and name two ways in which it differs from the singular value decomposition and from the complex spectral theorem.
6. True or false: a complex symmetric matrix is diagonalizable. Justify your answer.
:::
:::

::: {.solution}
(a) Every \( \A \in M_n(\nC) \) is \( \A = \W\lvert\A\rvert \) with \( \W \) unitary (@thm-polar-decomposition). The positive semidefinite factor \( \lvert\A\rvert \) is always unique; \( \W \) is unique exactly when \( \A \) is invertible, and then \( \W = \A\lvert\A\rvert^{-1} \).

(b) \( \lvert\A\rvert = (\A^{*}\A)^{1/2} \), the unique positive semidefinite square root of \( \A^{*}\A \) (@def-matrix-absolute-value), and \( \norm{\lvert\A\rvert\x} = \norm{\A\x} \) for every \( \x \).

(c) It says \( z = e^{i\theta}\lvert z\rvert \): a complex number is a number of modulus \( 1 \) times its modulus, with \( \theta \) undetermined exactly when \( z = 0 \).

(d) False in general, true exactly for normal \( \A \). For \( \A = \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix} \), \( \A\tp\A = \begin{pmatrix} 25 & 20 \\ 20 & 25 \end{pmatrix} \ne \begin{pmatrix} 9 & 12 \\ 12 & 41 \end{pmatrix} = \A\A\tp \), so the two square roots differ.

(e) @thm-takagi: a symmetric \( \A \in M_n(\nC) \) is \( \U\vSigma\U\tp \) with \( \U \) unitary and \( \vSigma \) the diagonal matrix of singular values. Against the singular value decomposition: the right factor is not free but forced to be \( \conj{\U} \). Against the spectral theorem: the hypothesis is symmetry rather than normality, the operation is the congruence \( \X \mapsto \U\X\U\tp \) rather than a similarity, and the diagonal carries singular values rather than eigenvalues.

(f) False. \( \N = \begin{pmatrix} 1 & i \\ i & -1 \end{pmatrix} \) is symmetric and non-zero with \( \N^2 = \0 \), so its minimal polynomial is \( x^2 \), which has a repeated root; it is not diagonalizable.
:::

### B. Practice

::: {#exr-polar-decomposition-b1}
[B1: A polar decomposition by hand]

Find both polar decompositions \( \A = \W\lvert\A\rvert = \lvert\A^{*}\rvert\W \) of
\[
\A = \begin{pmatrix} 0 & -2 \\ 3 & 0 \end{pmatrix},
\]
and say what \( \W \) is geometrically.
:::

::: {.solution}
\( \A\tp\A = \begin{pmatrix} 9 & 0 \\ 0 & 4 \end{pmatrix} \), which is diagonal with non-negative entries, so \( \lvert\A\rvert = \diag(3, 2) \): this is positive semidefinite and squares to \( \A\tp\A \), which by @thm-psd-square-root identifies it. Since \( \A \) is invertible,
\[
\W = \A\lvert\A\rvert^{-1} = \begin{pmatrix} 0 & -2 \\ 3 & 0 \end{pmatrix}\begin{pmatrix} \tfrac13 & 0 \\ 0 & \tfrac12 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix},
\]
the quarter turn of \( \nR^2 \). Check: \( \W\tp\W = \I \) and \( \W\lvert\A\rvert = \A \).

For the right-handed form, \( \A\A\tp = \diag(4, 9) \), so \( \lvert\A^{*}\rvert = \diag(2,3) \), and indeed
\[
\lvert\A^{*}\rvert\W = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & -2 \\ 3 & 0 \end{pmatrix} = \A .
\]
The two absolute values are different, which is consistent with \( \A \) not being normal. In words: \( \A \) stretches by \( 3 \) horizontally and \( 2 \) vertically, then rotates by a quarter turn; equivalently it rotates first and then stretches by \( 2 \) horizontally and \( 3 \) vertically.
:::

::: {#exr-polar-decomposition-b2}
[B2: The nearest unitary matrix]

Let \( \A = \diag(2, -3) \in M_2(\nR) \). Find the unitary matrix nearest to \( \A \) in the Frobenius norm, compute the distance, and verify the value against the formula of @cor-unitary-nearest.
:::

::: {.solution}
\( \A^{*}\A = \diag(4, 9) \), so \( \lvert\A\rvert = \diag(2, 3) \) and \( \W = \A\lvert\A\rvert^{-1} = \diag(1, -1) \), which is unitary. By @cor-unitary-nearest, \( \W \) is the nearest unitary matrix, and it is the only one since \( \A \) is invertible. Directly,
\[
\A - \W = \diag(1, -2), \qquad \norm{\A - \W}_F^2 = 1 + 4 = 5 .
\]
The formula gives \( \norm{\A}_F^2 + n - 2(\sigma_1 + \sigma_2) = 13 + 2 - 2(3 + 2) = 5 \), the same. So the distance is \( \sqrt5 \).
:::

::: {#exr-polar-decomposition-b3}
[B3: A Takagi factorization]

Find a Takagi factorization of \( \A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \), and explain why no **real** \( \U \) can work.
:::

::: {.solution}
\( \A \) is symmetric and \( \A^{*}\A = \A^2 = \I \), so \( \sigma_1 = \sigma_2 = 1 \) and \( \vSigma = \I \). We need a unitary \( \U \) with \( \U\U\tp = \A \).

Diagonalize \( \A \) over \( \nR \): its eigenvalues are \( 1 \) and \( -1 \), with unit eigenvectors \( \tfrac1{\sqrt2}(1,1) \) and \( \tfrac1{\sqrt2}(1,-1) \), so \( \A = \Q\diag(1,-1)\Q\tp \) with \( \Q = \tfrac1{\sqrt2}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \). Following Step 3 of @thm-takagi, take square roots \( 1 \) and \( i \) of the diagonal entries:
\[
\U = \Q\diag(1, i) = \tfrac1{\sqrt2}\begin{pmatrix} 1 & i \\ 1 & -i \end{pmatrix},
\qquad
\U\U\tp = \Q\diag(1,-1)\Q\tp = \A .
\]
\( \U \) is unitary, and \( \U\vSigma\U\tp = \U\U\tp = \A \).

No real \( \U \) works: a real \( \U \) with \( \U^{*}\U = \I \) is orthogonal, and then \( \U\vSigma\U\tp = \U\U\tp = \I \ne \A \).
:::

### C. Going deeper

::: {#exr-polar-decomposition-c1}
[C1: The positive factor is forced]

Let \( \A \in M_n(\nC) \).

::: {.enumerate options="label=(\alph*)"}
1. Suppose \( \A = \Q\P \) with \( \Q \) unitary and \( \P \succeq 0 \). Prove that \( \P = \lvert\A\rvert \). (Invertibility is **not** assumed.)
2. Deduce that \( \A \) is unitary if and only if \( \lvert\A\rvert = \I \).
:::
:::

::: {.solution}
(a) From \( \A = \Q\P \) we get \( \A^{*}\A = \P^{*}\Q^{*}\Q\P = \P^{*}\P = \P^2 \), using \( \Q^{*}\Q = \I \) and \( \P^{*} = \P \). So \( \P \) is a positive semidefinite square root of \( \A^{*}\A \). Such a square root is unique (@thm-psd-square-root), and \( \lvert\A\rvert \) is one by definition (@def-matrix-absolute-value). Hence \( \P = \lvert\A\rvert \).

(b) \( (\Rightarrow) \) If \( \A \) is unitary then \( \A^{*}\A = \I \), and \( \I \succeq 0 \) with \( \I^2 = \I \), so \( \lvert\A\rvert = \I \) by uniqueness. \( (\Leftarrow) \) If \( \lvert\A\rvert = \I \) then \( \A^{*}\A = \lvert\A\rvert^2 = \I \), which for a square matrix says \( \A \) is unitary (@def-unitary-orthogonal).
:::

::: {#exr-polar-decomposition-c2}
[C2: Normality through the polar factors]

Let \( \A \in M_n(\nC) \) be invertible with polar decomposition \( \A = \W\lvert\A\rvert \). Prove that the following are equivalent.

::: {.enumerate options="label=(\alph*)"}
1. \( \A \) is normal.
2. \( \lvert\A\rvert = \lvert\A^{*}\rvert \).
3. \( \W\lvert\A\rvert = \lvert\A\rvert\W \).
:::
:::

::: {.solution}
(a) \( \Rightarrow \) (b). If \( \A^{*}\A = \A\A^{*} \), then \( \lvert\A\rvert \) and \( \lvert\A^{*}\rvert \) are positive semidefinite square roots of the same matrix, hence equal by @thm-psd-square-root.

(b) \( \Rightarrow \) (c). By @thm-polar-decomposition, \( \lvert\A^{*}\rvert = \W\lvert\A\rvert\W^{*} \). If this equals \( \lvert\A\rvert \), multiply on the right by \( \W \) to get \( \lvert\A\rvert\W = \W\lvert\A\rvert \).

(c) \( \Rightarrow \) (a). Write \( \P = \lvert\A\rvert \), so \( \A = \W\P = \P\W \). Then
\[
\A\A^{*} = \W\P\P^{*}\W^{*} = \W\P^2\W^{*} = \P^2\W\W^{*} = \P^2 ,
\]
using \( \P^{*} = \P \), then \( \W\P^2 = \P^2\W \) (which follows from \( \W\P = \P\W \)), then \( \W\W^{*} = \I \). And \( \A^{*}\A = \P^{*}\W^{*}\W\P = \P^2 \). So \( \A\A^{*} = \A^{*}\A \).
:::

::: {#exr-polar-decomposition-c3}
[C3: Complex symmetric matrices are transposed squares]

Let \( \A \in M_n(\nC) \) be symmetric and invertible.

::: {.enumerate options="label=(\alph*)"}
1. Using @thm-takagi, prove that \( \A = \B\tp\B \) for some invertible \( \B \in M_n(\nC) \).
2. Show that over \( \nR \) the analogous statement is false unless \( \A \) is positive definite, and give a \( 1 \times 1 \) witness.
3. Explain in one sentence why (a) and (b) do not contradict each other.
:::
:::

::: {.solution}
(a) By @thm-takagi, \( \A = \U\vSigma\U\tp \) with \( \U \) unitary and \( \vSigma = \diag(\sigma_1, \dots, \sigma_n) \), where every \( \sigma_i > 0 \) because \( \A \) is invertible (@thm-svd). Let \( \vSigma^{1/2} = \diag(\sqrt{\sigma_1}, \dots, \sqrt{\sigma_n}) \) and put \( \B \coloneqq \vSigma^{1/2}\U\tp \), which is invertible as a product of invertible matrices. Then
\[
\B\tp\B = \U\,\vSigma^{1/2}\vSigma^{1/2}\,\U\tp = \U\vSigma\U\tp = \A ,
\]
using \( (\vSigma^{1/2})\tp = \vSigma^{1/2} \) and \( (\U\tp)\tp = \U \).

(b) Over \( \nR \), if \( \A = \B\tp\B \) with \( \B \in M_n(\nR) \) then \( \x\tp\A\x = \norm{\B\x}^2 \ge 0 \) for every \( \x \), so \( \A \succeq 0 \), and \( \A \succ 0 \) when \( \B \) is invertible. So no real \( \A \) with a negative eigenvalue is of this form: for \( n = 1 \), \( \A = (-1) \) is symmetric and invertible but \( b^2 = -1 \) has no real solution.

(c) The factor \( \B \) produced in (a) is complex, and over \( \nC \) the quantity \( \x\tp\A\x \) is not a sum of squared lengths — the transpose carries no conjugation, so \( \B\tp\B \) says nothing about positivity. Indeed \( b = i \) solves \( b^2 = -1 \).
:::
