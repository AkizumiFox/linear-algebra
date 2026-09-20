# Means and Matrix Cauchy–Schwarz

Two inequalities about numbers refuse to die: \( \lvert \conj{a}b\rvert^2 \le \lvert a\rvert^2\lvert b\rvert^2 \), and \( 2\lvert \conj{a}b \rvert \le \lvert a\rvert^2 + \lvert b\rvert^2 \). For matrices the products do not commute and the absolute values are matrices themselves, so it is not obvious what either statement should say. Sections 4 and 6 have given the right language: measure a matrix by a unitarily invariant norm, and compare two matrices by weak majorization of their singular values. In that language both inequalities survive, for **every** unitarily invariant norm at once. The second half of the section then builds a genuine geometric mean of two positive definite matrices, which is where two order facts from the earlier chapters pay off again: the operator monotonicity of \( t \mapsto t^{1/2} \) from Chapter 12 §05 and that of \( t \mapsto -1/t \) from Chapter 16 §11.

**Throughout, \( F = \nR \) or \( F = \nC \) and all matrices are \( n \times n \) over \( F \)**, with \( \uinorm{\cdot} \) an arbitrary unitarily invariant norm on \( M_n(F) \) (@def-unitarily-invariant-norm). As always \( \sigma_1(\A) \ge \dots \ge \sigma_n(\A) \ge 0 \) are the singular values in decreasing order and \( \lambda_1(\A) \ge \dots \ge \lambda_n(\A) \) the eigenvalues of a Hermitian \( \A \); for \( \A \succeq 0 \) the two lists agree. The order \( \succeq \) is the Loewner order (@def-loewner-order).

## An off-diagonal block is small

Everything in the first half comes from one observation about a positive semidefinite matrix cut into four blocks: the corner blocks control the off-diagonal one, and they do so eigenvalue by eigenvalue.

::: {#lem-off-diagonal-block-bound}
[The Off-Diagonal Block of a Positive Semidefinite Matrix]

Let \( k, l \ge 1 \), let \( \P \in M_k(F) \), \( \Q \in M_l(F) \) and \( \X \in M_{k \times l}(F) \), and suppose that
\[
\M = \begin{pmatrix} \P & \X \\ \X^{*} & \Q \end{pmatrix} \ \succeq\ 0 .
\]
Then \( 2\sigma_j(\X) \le \lambda_j(\M) \) for every \( j = 1, \dots, \min(k, l) \).
:::

::: {.idea}
Flipping the sign of the second block of coordinates is a unitary congruence, so it turns \( \M \) into another positive semidefinite matrix — the same one with \( \X \) replaced by \( -\X \). Half the difference of the two is the Hermitian dilation of \( \X \), whose eigenvalues are exactly \( \pm\sigma_i(\X) \) and zeros. Since what was subtracted is itself positive semidefinite, the dilation is dominated by \( \tfrac12\M \) in the Loewner order, and Chapter 16 §02 turns that into a comparison of eigenvalues index by index.
:::

::: {.proof}
Put \( \S = \I_k \oplus (-\I_l) \), which is Hermitian and unitary. By @thm-block-multiplication,
\[
\S^{*}\M\S = \begin{pmatrix} \P & -\X \\ -\X^{*} & \Q\end{pmatrix} ,
\]
and \( \S^{*}\M\S \succeq 0 \) because a congruence by an invertible matrix preserves positive semidefiniteness (@prp-congruence-positivity (a)). Subtracting,
\[
\tfrac12\bigl(\M - \S^{*}\M\S\bigr) = \begin{pmatrix} \0 & \X \\ \X^{*} & \0\end{pmatrix} = \cH(\X) ,
\]
the Hermitian dilation of \( \X \) (@prp-hermitian-dilation). Since \( \tfrac12\S^{*}\M\S \succeq 0 \), this says
\[
\cH(\X) = \tfrac12\M - \tfrac12\S^{*}\M\S \ \preceq\ \tfrac12\M .
\]
By @cor-loewner-eigenvalue-monotone the Loewner order compares every eigenvalue, so \( \lambda_j(\cH(\X)) \le \lambda_j(\tfrac12\M) = \tfrac12\lambda_j(\M) \) for every \( j \).

Finally, by @prp-hermitian-dilation the eigenvalues of \( \cH(\X) \), with multiplicity, are \( \pm\sigma_1(\X), \dots, \pm\sigma_p(\X) \) together with \( k + l - 2p \) zeros, where \( p = \min(k,l) \). Sorted decreasingly, the first \( p \) of them are \( \sigma_1(\X) \ge \dots \ge \sigma_p(\X) \), since every remaining entry is \( \le 0 \le \sigma_p(\X) \). Hence \( \lambda_j(\cH(\X)) = \sigma_j(\X) \) for \( j \le p \), and the displayed inequality reads \( 2\sigma_j(\X) \le \lambda_j(\M) \).
:::

## A product against a sum of squares

The lemma becomes an inequality about products as soon as one remembers where positive semidefinite block matrices come from: \( \D^{*}\D \), for \( \D \) the block row built from the two matrices in question.

::: {#thm-matrix-am-gm}
[Arithmetic–Geometric Mean Inequality for Matrices]

Let \( \A, \B \in M_n(F) \). Then
\[
2\sigma_j(\A^{*}\B) \ \le\ \lambda_j(\A\A^{*} + \B\B^{*}) \qquad (j = 1, \dots, n) ,
\]
and consequently, for every unitarily invariant norm on \( M_n(F) \),
\[
2\uinorm{\A^{*}\B} \ \le\ \uinorm{\A\A^{*} + \B\B^{*}} .
\]
:::

::: {.idea}
Put the two matrices side by side in one \( n \times 2n \) block row \( \D = (\A \ \ \B) \). Then \( \D^{*}\D \) is the \( 2n \times 2n \) positive semidefinite matrix whose off-diagonal block is exactly \( \A^{*}\B \), so @lem-off-diagonal-block-bound applies; and \( \D\D^{*} \), which has the same non-zero eigenvalues, is the sum \( \A\A^{*} + \B\B^{*} \). The norm statement is then the singular value statement read through §06's dominance theorem.
:::

::: {.proof}
Let \( \D = (\A \ \ \B) \in M_{n \times 2n}(F) \), the block row with \( \A \) then \( \B \). By @thm-block-multiplication,
\[
\D^{*}\D = \begin{pmatrix} \A^{*}\A & \A^{*}\B \\ \B^{*}\A & \B^{*}\B\end{pmatrix},
\qquad
\D\D^{*} = \A\A^{*} + \B\B^{*} .
\]
The matrix \( \D^{*}\D \) is Hermitian and satisfies \( \x^{*}\D^{*}\D\x = \norm{\D\x}^2 \ge 0 \) for every \( \x \in F^{2n} \), so \( \D^{*}\D \succeq 0 \) (@def-positive-semidefinite). Its off-diagonal block is \( \A^{*}\B \), so @lem-off-diagonal-block-bound with \( k = l = n \) gives
\[
2\sigma_j(\A^{*}\B) \ \le\ \lambda_j(\D^{*}\D) \qquad (j = 1, \dots, n) .
\]
It remains to identify \( \lambda_j(\D^{*}\D) \) with \( \lambda_j(\D\D^{*}) \) for \( j \le n \). Applying @thm-ab-ba-eigenvalues to the pair \( \D^{*} \in M_{2n \times n} \) and \( \D \in M_{n \times 2n} \) gives \( x^{n}p_{\D^{*}\D}(x) = x^{2n}p_{\D\D^{*}}(x) \), that is \( p_{\D^{*}\D} = x^{n}p_{\D\D^{*}} \): the eigenvalue list of \( \D^{*}\D \) is that of \( \D\D^{*} \) with \( n \) extra zeros. Both matrices are positive semidefinite, so all their eigenvalues are \( \ge 0 \) (@thm-psd-characterizations (b)) and the first \( n \) entries of the two decreasing lists agree. This proves the first display.

For the second, both \( 2\A^{*}\B \) and \( \A\A^{*} + \B\B^{*} \) lie in \( M_n(F) \), and the singular values of the positive semidefinite \( \A\A^{*} + \B\B^{*} \) are its eigenvalues. So the first display says \( \sigma_j(2\A^{*}\B) \le \sigma_j(\A\A^{*} + \B\B^{*}) \) for every \( j \). Two decreasing lists of non-negative numbers with the first dominated entry by entry satisfy \( \sigma(2\A^{*}\B) \prec_w \sigma(\A\A^{*}+\B\B^{*}) \), since each top-\( k \) partial sum is dominated term by term (@def-majorization). Now @thm-ky-fan-dominance turns that weak majorization into \( \uinorm{2\A^{*}\B} \le \uinorm{\A\A^{*}+\B\B^{*}} \), and \( \uinorm{2\A^{*}\B} = 2\uinorm{\A^{*}\B} \) by homogeneity of a norm.
:::

::: {.warning}
**The two sums are not interchangeable.** It is tempting to write \( \A^{*}\A + \B^{*}\B \) on the right, since that is what pairs with \( \A^{*}\B \) in the block matrix \( \D^{*}\D \). The resulting statement is **false**. Take
\[
\A = \begin{pmatrix} 1 & 0 \\ 0 & 0\end{pmatrix},
\qquad
\B = \begin{pmatrix} 0 & 1 \\ 0 & 0\end{pmatrix} .
\]
Then \( \A^{*}\A = \diag(1,0) \) and \( \B^{*}\B = \diag(0,1) \), so \( \A^{*}\A + \B^{*}\B = \I \) and \( \norm{\I}_2 = 1 \); while \( \A^{*}\B = \B \) has \( \norm{\B}_2 = 1 \), so \( 2\uinorm{\A^{*}\B} = 2 > 1 \) in the spectral norm. The correct right-hand side is \( \A\A^{*} + \B\B^{*} = \diag(2,0) \), of spectral norm \( 2 \) — and here the inequality is an equality.
:::

## Cauchy–Schwarz

::: {#thm-matrix-cauchy-schwarz}
[Cauchy–Schwarz for Unitarily Invariant Norms]

Let \( \A, \B \in M_n(F) \). Then for every unitarily invariant norm on \( M_n(F) \),
\[
\uinorm{\A^{*}\B}^{2} \ \le\ \uinorm{\A^{*}\A}\ \uinorm{\B^{*}\B} .
\]
:::

::: {.idea}
The scalar inequality \( 2\lvert\conj ab\rvert \le \lvert a\rvert^2 + \lvert b\rvert^2 \) becomes \( \lvert\conj ab\rvert \le \lvert a\rvert\lvert b\rvert \) by the classical trick of replacing \( a \) by \( ta \) and \( b \) by \( b/t \) and choosing \( t \) to balance the two terms. The product \( \A^{*}\B \) is unchanged by that substitution, so the same trick upgrades @thm-matrix-am-gm. The one thing to check is that the two sides of the balance are the right quantities, and that is the identity \( \uinorm{\A\A^{*}} = \uinorm{\A^{*}\A} \).
:::

::: {.proof}
Put \( a = \uinorm{\A^{*}\A} \) and \( b = \uinorm{\B^{*}\B} \). If \( a = 0 \), then \( \A^{*}\A = \0 \) by the positivity clause of @def-norm, so \( \norm{\A\x}^2 = \x^{*}\A^{*}\A\x = 0 \) for every \( \x \) and \( \A = \0 \); then both sides of the asserted inequality are \( 0 \). Likewise if \( b = 0 \). So assume \( a > 0 \) and \( b > 0 \).

First, \( \uinorm{\A\A^{*}} = \uinorm{\A^{*}\A} \). Indeed \( \A\A^{*} \) and \( \A^{*}\A \) are positive semidefinite with the same eigenvalues, namely \( \sigma_i(\A)^2 \) (@def-singular-values and @thm-ab-ba-eigenvalues (b), the two matrices being of equal size \( n \)), hence the same singular values; and a unitarily invariant norm depends only on the singular values (@lem-ui-norm-of-diagonal).

Let \( t > 0 \) and apply @thm-matrix-am-gm to the pair \( t\A \) and \( t^{-1}\B \). Their product is \( (t\A)^{*}(t^{-1}\B) = \A^{*}\B \), unchanged, while
\[
(t\A)(t\A)^{*} + (t^{-1}\B)(t^{-1}\B)^{*} = t^{2}\A\A^{*} + t^{-2}\B\B^{*} .
\]
So, using the triangle inequality and homogeneity of \( \uinorm{\cdot} \) and then the identity just proved,
\[
2\uinorm{\A^{*}\B} \ \le\ t^{2}\uinorm{\A\A^{*}} + t^{-2}\uinorm{\B\B^{*}} = t^{2}a + t^{-2}b .
\]
By the arithmetic–geometric mean inequality for two positive numbers (@lem-am-gm), \( t^2a + t^{-2}b \ge 2\sqrt{ab} \), with equality when \( t^2a = t^{-2}b \); choosing \( t = (b/a)^{1/4} \), which is legitimate since \( a, b > 0 \), makes the two terms equal and gives
\[
2\uinorm{\A^{*}\B} \ \le\ 2\sqrt{ab} .
\]
Dividing by \( 2 \) and squaring proves the theorem.
:::

::: {.remark}
Three familiar inequalities are special cases. With \( \uinorm{\cdot} = \norm{\cdot}_F \) it is \( \norm{\A^{*}\B}_F^2 \le \norm{\A^{*}\A}_F\norm{\B^{*}\B}_F \); with the spectral norm it is \( \norm{\A^{*}\B}_2^2 \le \norm{\A}_2^2\norm{\B}_2^2 \), which also follows from submultiplicativity; and with the trace norm \( \uinorm{\cdot}_{(n)} = \sum_i\sigma_i(\cdot) \) it compares \( \sum_i\sigma_i(\A^{*}\B) \) with \( \bigl(\sum_i\sigma_i(\A)^2\bigr)^{1/2}\bigl(\sum_i\sigma_i(\B)^2\bigr)^{1/2} \). At \( n = 1 \) all of them are \( \lvert\conj ab\rvert^2 \le \lvert a\rvert^2\lvert b\rvert^2 \).
:::

## The geometric mean of two positive definite matrices

The inequalities above were about *norms* of products. The rest of the section is about an operation: given \( \A, \B \succ 0 \), produce a positive definite matrix that deserves the name \( \sqrt{\A\B} \).

The arithmetic mean gives no trouble: \( \tfrac12(\A + \B) \) is positive definite, symmetric in the two arguments, and monotone in each. The geometric mean is the problem. The naive candidate is \( (\A\B)^{1/2} \), and it does not exist: \( \A\B \) need not be Hermitian, so @thm-psd-square-root has nothing to say about it. The next candidate, \( \A^{1/2}\B^{1/2} \), is a matrix, but usually not a Hermitian one. What works is to measure \( \B \) in the coordinates that make \( \A \) the identity, take the square root there, and translate back.

*The geometric mean of two positive definite matrices is the square root of the second one, computed after the first has been turned into the identity, and then translated back.*

:::: {#def-geometric-mean}
[Geometric Mean of Positive Definite Matrices]

Let \( \A, \B \in M_n(F) \) with \( \A \succ 0 \) and \( \B \succ 0 \). Their **geometric mean** is
\[
\A \# \B \ \coloneqq\ \A^{1/2}\bigl(\A^{-1/2}\B\A^{-1/2}\bigr)^{1/2}\A^{1/2} ,
\]
where \( \A^{1/2} \) is the positive square root of @thm-psd-square-root, \( \A^{-1/2} \coloneqq (\A^{1/2})^{-1} \), and the outer exponent \( \tfrac12 \) is again the positive square root.
::::

In words: conjugate \( \B \) by \( \A^{-1/2} \) — this is the **whitening** move of Chapter 12 §05, which replaces the pair \( (\A, \B) \) by \( (\I, \C) \) with \( \C = \A^{-1/2}\B\A^{-1/2} \) — take the positive square root of \( \C \), and undo the conjugation.

**Everything in the definition makes sense.** \( \A \succ 0 \) gives \( \A^{1/2} \succ 0 \) (its eigenvalues are the positive square roots of those of \( \A \), by @thm-psd-square-root), so \( \A^{1/2} \) is invertible and \( \A^{-1/2} \) is Hermitian. Hence \( \C = \A^{-1/2}\B\A^{-1/2} = (\A^{-1/2})^{*}\B\A^{-1/2} \) is a congruence of \( \B \succ 0 \) by an invertible matrix and is therefore \( \succ 0 \) (@prp-congruence-positivity (b)); so \( \C^{1/2} \) exists, is unique, and is \( \succ 0 \). Finally \( \A\#\B = (\A^{1/2})^{*}\C^{1/2}\A^{1/2} \) is another such congruence, so \( \A\#\B \succ 0 \). In particular \( \A\#\B \) is Hermitian, which \( \A^{1/2}\B^{1/2} \) is not.

**Examples.**

- **Numbers.** For \( n = 1 \) with \( \A = (a) \), \( \B = (b) \) and \( a, b > 0 \), the formula reads \( \sqrt a\,(b/a)^{1/2}\sqrt a = \sqrt{ab} \). This is where the name comes from.
- **One argument the identity.** \( \A\#\I = \A^{1/2}(\A^{-1})^{1/2}\A^{1/2} = \A^{1/2}\A^{-1/2}\A^{1/2} = \A^{1/2} \), using \( (\A^{-1})^{1/2} = \A^{-1/2} \), which holds because \( (\A^{-1/2})^2 = \A^{-1} \) and \( \A^{-1/2} \succ 0 \), so uniqueness in @thm-psd-square-root applies. Likewise \( \A\#\A = \A^{1/2}\I\A^{1/2} = \A \).
- **Commuting arguments.** If \( \A\B = \B\A \) then \( \A\#\B = (\A\B)^{1/2} \). Indeed \( \A^{1/2} \) commutes with \( \B \) (@thm-psd-square-root (b)), hence so does \( \A^{-1/2} \), so \( \C = \B\A^{-1} \) commutes with \( \A \), and \( \C^{1/2} \), being a polynomial in \( \C \) (@thm-psd-square-root (a)), commutes with \( \A \) too. Therefore
\[
\begin{aligned}
(\A\#\B)^2 &= \A^{1/2}\C^{1/2}\A\,\C^{1/2}\A^{1/2}
  = \A^{1/2}\A\,\C\,\A^{1/2} \\
 &= \A^{1/2}\A\B\A^{-1}\A^{1/2} = \A^{1/2}\B\A^{1/2} = \A\B ,
\end{aligned}
\]
using \( \C = \B\A^{-1} \) and \( \A\B = \B\A \) once more; and \( \A\#\B \succ 0 \), so it is the positive square root of \( \A\B \). For instance \( \diag(4,1)\#\diag(1,9) = \diag(2,3) \).
- **A non-commuting pair, exactly.** Let
\[
\A = \begin{pmatrix} 5 & 4 \\ 4 & 5\end{pmatrix},
\qquad
\B = \begin{pmatrix} 8 & 10 \\ 10 & 17\end{pmatrix} .
\]
Then \( \A^{1/2} = \begin{psmallmatrix}2&1\\1&2\end{psmallmatrix} \), and \( \A^{-1/2} = \tfrac13\begin{psmallmatrix}2&-1\\-1&2\end{psmallmatrix} \), so \( \C = \A^{-1/2}\B\A^{-1/2} = \diag(1,4) \) and \( \C^{1/2} = \diag(1,2) \). Hence
\[
\A\#\B = \begin{pmatrix}2&1\\1&2\end{pmatrix}\begin{pmatrix}1&0\\0&2\end{pmatrix}\begin{pmatrix}2&1\\1&2\end{pmatrix} = \begin{pmatrix}6&6\\6&9\end{pmatrix} .
\]
Here \( \A\B \ne \B\A \), as the \( (1,2) \) entries \( 118 \) and \( 82 \) show. Note \( \det(\A\#\B) = 18 = \sqrt{9 \cdot 36} = \sqrt{\det\A\,\det\B} \); Exercise C1 explains why.

**A non-example by minimal change.** Drop the middle square root and take \( \A^{1/2}\B^{1/2} \). With \( \A = \diag(4,1) \) and \( \B = \begin{psmallmatrix}5&4\\4&5\end{psmallmatrix} \), the two square roots are \( \diag(2,1) \) and \( \begin{psmallmatrix}2&1\\1&2\end{psmallmatrix} \), and
\[
\A^{1/2}\B^{1/2} = \begin{pmatrix}4&2\\1&2\end{pmatrix} ,
\]
which is not Hermitian, so it is not \( \succ 0 \) and is not a mean of anything. Its square is \( \begin{psmallmatrix}18&12\\6&6\end{psmallmatrix} \), not \( \A\B = \begin{psmallmatrix}20&16\\4&5\end{psmallmatrix} \).

::: {.warning}
**Half of \( \A \) times half of \( \B \) is not a mean.** \( \A^{1/2}\B^{1/2} \) is Hermitian only when \( \A \) and \( \B \) commute: \( (\A^{1/2}\B^{1/2})^{*} = \B^{1/2}\A^{1/2} \), and if this equals \( \A^{1/2}\B^{1/2} \), then squaring gives \( \A\B = \B\A \). The sandwich in @def-geometric-mean exists precisely to repair this, and the price is that the formula no longer *looks* symmetric in \( \A \) and \( \B \). It is; that is the content of @thm-geometric-mean-properties (b), and it is the one property here that needs an argument.
:::

::: {.check}
Compute \( \A\#\B \) for \( \A = \diag(4,1) \) and \( \B = \diag(1,9) \) straight from @def-geometric-mean, and check the answer against \( (\A\B)^{1/2} \).
:::

::: {.solution}
\( \A^{1/2} = \diag(2,1) \) and \( \A^{-1/2} = \diag(\tfrac12, 1) \), so \( \C = \A^{-1/2}\B\A^{-1/2} = \diag(\tfrac14, 9) \) and \( \C^{1/2} = \diag(\tfrac12, 3) \). Hence
\[
\A\#\B = \diag(2,1)\diag(\tfrac12,3)\diag(2,1) = \diag(2, 3) .
\]
The two matrices commute, and \( \A\B = \diag(4,9) \), whose positive square root is \( \diag(2,3) \). The two agree.
:::

## What the geometric mean does

The key is a description of \( \A\#\B \) that never mentions \( \A^{1/2} \). Chapter 12 §06's block test supplies it.

:::: {#thm-geometric-mean-properties}
[Properties of the Geometric Mean]

Let \( \A, \B, \A', \B' \in M_n(F) \) be positive definite and let \( \S \in M_n(F) \) be invertible.

::: {.enumerate options="label=(\alph*)"}
1. **Extremal characterization.** \( \A\#\B \) is the largest Hermitian \( \X \in M_n(F) \) for which
\[
\begin{pmatrix} \A & \X \\ \X & \B\end{pmatrix} \ \succeq\ 0 :
\]
this holds for \( \X = \A\#\B \), and every Hermitian \( \X \) for which it holds satisfies \( \X \preceq \A\#\B \).
2. **Symmetry.** \( \A\#\B = \B\#\A \).
3. **Congruence.** \( (\S^{*}\A\S)\#(\S^{*}\B\S) = \S^{*}(\A\#\B)\S \).
4. **Monotonicity.** If \( \A \succeq \A' \) and \( \B \succeq \B' \), then \( \A\#\B \succeq \A'\#\B' \).
5. **Arithmetic–geometric mean, and inversion.** \( \A\#\B \preceq \tfrac12(\A + \B) \), and \( (\A\#\B)^{-1} = \A^{-1}\#\B^{-1} \).
:::
::::

::: {.idea}
Everything rests on (a), and (a) rests on whitening. With \( \A \succ 0 \) the block test @thm-block-psd-schur turns the block condition into \( \B - \X\A^{-1}\X \succeq 0 \); substituting \( \X = \A^{1/2}\Y\A^{1/2} \) and conjugating by \( \A^{-1/2} \) turns *that* into \( \Y^2 \preceq \C \), with \( \C = \A^{-1/2}\B\A^{-1/2} \). The largest Hermitian \( \Y \) with \( \Y^2 \preceq \C \) is \( \C^{1/2} \), because \( \Y \preceq \lvert\Y\rvert = (\Y^2)^{1/2} \) and the square root is operator monotone. Once (a) is available, (b), (c) and (d) are all statements about the *set* of admissible \( \X \), and they read off the symmetry, the congruence-invariance and the monotonicity of that set without any further computation.
:::

::: {.proof}
Write \( \C = \A^{-1/2}\B\A^{-1/2} \succ 0 \), so that \( \A\#\B = \A^{1/2}\C^{1/2}\A^{1/2} \), and for Hermitian \( \X \) put
\[
\M(\X) = \begin{pmatrix} \A & \X \\ \X & \B\end{pmatrix} ,
\]
which is Hermitian because \( \X^{*} = \X \). Call \( \X \) **admissible** for \( (\A, \B) \) when \( \M(\X) \succeq 0 \).

**(a).** Since \( \A \succ 0 \), @thm-block-psd-schur (b) says that \( \X \) is admissible exactly when the Schur complement \( \B - \X\A^{-1}\X \) is \( \succeq 0 \). Every Hermitian \( \X \) is uniquely \( \X = \A^{1/2}\Y\A^{1/2} \) with \( \Y = \A^{-1/2}\X\A^{-1/2} \) Hermitian, and then
\[
\X\A^{-1}\X = \A^{1/2}\Y\A^{1/2}\A^{-1}\A^{1/2}\Y\A^{1/2} = \A^{1/2}\Y^{2}\A^{1/2} .
\]
Conjugating by the invertible Hermitian \( \A^{-1/2} \) and using @prp-congruence-positivity (a) in both directions,
\[
\B - \A^{1/2}\Y^2\A^{1/2} \succeq 0
\quad\Longleftrightarrow\quad
\C - \Y^{2} \succeq 0 .
\]

::: {.claim}
If \( \Y \) is Hermitian and \( \Y^2 \preceq \C \), then \( \Y \preceq \C^{1/2} \).
:::

::: {.proof}
Let \( \Y = \sum_j\mu_j\P_j \) be the spectral resolution (@thm-spectral-resolution), so that \( \Y^2 = \sum_j\mu_j^2\P_j \) and the matrix \( \sum_j\lvert\mu_j\rvert\P_j \) is \( \succeq 0 \) with square \( \Y^2 \); by uniqueness in @thm-psd-square-root it is \( (\Y^2)^{1/2} \). Then
\[
(\Y^2)^{1/2} - \Y = \sum_j\bigl(\lvert\mu_j\rvert - \mu_j\bigr)\P_j \ \succeq\ 0 ,
\]
because \( \x^{*}\P_j\x = \norm{\P_j\x}^2 \ge 0 \) and every coefficient is \( \ge 0 \). So \( \Y \preceq (\Y^2)^{1/2} \). Also \( \Y^2 \preceq \C \) with \( \Y^2 \succeq 0 \), so @prp-square-root-monotone gives \( (\Y^2)^{1/2} \preceq \C^{1/2} \). Chaining the two (@prp-loewner-partial-order) gives \( \Y \preceq \C^{1/2} \).
:::

The choice \( \Y = \C^{1/2} \) itself satisfies \( \C - \Y^2 = \0 \succeq 0 \). So among the Hermitian \( \Y \) with \( \C - \Y^2 \succeq 0 \) the largest is \( \C^{1/2} \). Translating back by the order-preserving bijection \( \Y \mapsto \A^{1/2}\Y\A^{1/2} \) (again @prp-congruence-positivity (a), in both directions), the largest admissible \( \X \) is \( \A^{1/2}\C^{1/2}\A^{1/2} = \A\#\B \).

**(b).** Let \( \W = \begin{psmallmatrix} \0 & \I \\ \I & \0\end{psmallmatrix} \), which is Hermitian and unitary, hence invertible. By @thm-block-multiplication,
\[
\W^{*}\begin{pmatrix} \A & \X \\ \X & \B\end{pmatrix}\W = \begin{pmatrix} \B & \X \\ \X & \A\end{pmatrix} ,
\]
so by @prp-congruence-positivity (a), applied to \( \W \) and to \( \W^{-1} \), a Hermitian \( \X \) is admissible for \( (\A, \B) \) if and only if it is admissible for \( (\B, \A) \). The two admissible sets coincide, so they have the same largest element; by (a) that element is \( \A\#\B \) on one side and \( \B\#\A \) on the other, and a partial order has at most one largest element (@prp-loewner-partial-order).

**(c).** Put \( \T = \S \oplus \S \). By @thm-block-multiplication,
\[
\T^{*}\begin{pmatrix} \A & \X \\ \X & \B\end{pmatrix}\T = \begin{pmatrix} \S^{*}\A\S & \S^{*}\X\S \\ \S^{*}\X\S & \S^{*}\B\S\end{pmatrix} ,
\]
and \( \T \) is invertible, so \( \X \) is admissible for \( (\A, \B) \) exactly when \( \S^{*}\X\S \) is admissible for \( (\S^{*}\A\S, \S^{*}\B\S) \) (@prp-congruence-positivity (a), both ways). The map \( \X \mapsto \S^{*}\X\S \) is a bijection of the Hermitian matrices that preserves \( \preceq \) in both directions, so it carries the largest element of one admissible set to the largest element of the other. Both \( \S^{*}\A\S \) and \( \S^{*}\B\S \) are \( \succ 0 \) by @prp-congruence-positivity (b), so (a) applies to them, and the claim follows.

**(d).** Let \( \X \) be admissible for \( (\A', \B') \). Then
\[
\begin{pmatrix} \A & \X \\ \X & \B\end{pmatrix}
= \begin{pmatrix} \A' & \X \\ \X & \B'\end{pmatrix} +
\begin{pmatrix} \A - \A' & \0 \\ \0 & \B - \B'\end{pmatrix} ,
\]
a sum of two positive semidefinite matrices — the second because its quadratic form is \( \y_1^{*}(\A - \A')\y_1 + \y_2^{*}(\B - \B')\y_2 \ge 0 \). So \( \X \) is admissible for \( (\A, \B) \). Taking \( \X = \A'\#\B' \), which is admissible for \( (\A', \B') \) by (a), gives \( \A'\#\B' \preceq \A\#\B \) by the maximality in (a).

**(e).** Since \( \C^{1/2} \) is Hermitian, \( (\I - \C^{1/2})^2 \succeq 0 \) by @thm-psd-characterizations (c), and \( (\C^{1/2})^2 = \C \) gives
\[
\tfrac12(\I + \C) - \C^{1/2} = \tfrac12\bigl(\I - \C^{1/2}\bigr)^{2} \ \succeq\ 0 .
\]
Conjugating by \( \A^{1/2} \) and using \( \A^{1/2}\C\A^{1/2} = \B \),
\[
\tfrac12(\A + \B) - \A\#\B = \tfrac12\A^{1/2}\bigl(\I - \C^{1/2}\bigr)^{2}\A^{1/2} \ \succeq\ 0 ,
\]
by @prp-congruence-positivity (a). For the inversion formula, \( \A\#\B = \A^{1/2}\C^{1/2}\A^{1/2} \) is a product of invertible matrices, with inverse \( \A^{-1/2}\C^{-1/2}\A^{-1/2} \), where \( \C^{-1/2} = (\C^{1/2})^{-1} \). On the other side, using \( (\A^{-1})^{1/2} = \A^{-1/2} \) and \( (\A^{-1})^{-1/2} = \A^{1/2} \),
\[
\A^{-1}\#\B^{-1} = \A^{-1/2}\bigl(\A^{1/2}\B^{-1}\A^{1/2}\bigr)^{1/2}\A^{-1/2} ,
\]
and \( \A^{1/2}\B^{-1}\A^{1/2} = (\A^{-1/2}\B\A^{-1/2})^{-1} = \C^{-1} \), whose positive square root is \( \C^{-1/2} \), since \( (\C^{-1/2})^2 = \C^{-1} \) and \( \C^{-1/2} \succ 0 \). So \( \A^{-1}\#\B^{-1} = \A^{-1/2}\C^{-1/2}\A^{-1/2} = (\A\#\B)^{-1} \).
:::

Part (a) is the statement to remember, because it is the one with no square roots in it: \( \A\#\B \) is the best Hermitian matrix that can sit in the off-diagonal corner above \( \A \) and \( \B \). Read beside @lem-off-diagonal-block-bound, which says that such a corner cannot be too large in singular value, part (a) says exactly how large it can be in the Loewner order.

::: {.check}
Take \( \B = \A \). Part (a) then says that \( \A \) is the largest Hermitian \( \X \) with \( \begin{psmallmatrix}\A&\X\\\X&\A\end{psmallmatrix} \succeq 0 \). Check by hand that \( \X = \A \) is admissible and that \( \X = 2\A \) is not.
:::

::: {.solution}
For \( \X = \A \) the quadratic form at \( (\y_1, \y_2) \) is
\[
\y_1^{*}\A\y_1 + \y_1^{*}\A\y_2 + \y_2^{*}\A\y_1 + \y_2^{*}\A\y_2 = (\y_1 + \y_2)^{*}\A(\y_1 + \y_2) \ \ge\ 0 ,
\]
so \( \X = \A \) is admissible — as it must be, since \( \A\#\A = \A \) by the second example after @def-geometric-mean. For \( \X = 2\A \) take \( \y_2 = -\y_1 \): the four terms give \( \y_1^{*}\A\y_1 - 4\y_1^{*}\A\y_1 + \y_1^{*}\A\y_1 = -2\y_1^{*}\A\y_1 \), which is \( < 0 \) for \( \y_1 \ne \0 \) because \( \A \succ 0 \). So \( 2\A \) is not admissible.
:::

## The chain of three means

Beside the arithmetic mean \( \tfrac12(\A + \B) \) and the geometric mean \( \A\#\B \) sits a third. The **harmonic mean** of two positive definite matrices is the inverse of the arithmetic mean of their inverses,
\[
\Bigl(\frac{\A^{-1} + \B^{-1}}{2}\Bigr)^{-1} ,
\]
which at \( n = 1 \) is the familiar \( 2ab/(a+b) \). For two positive numbers the three are ordered harmonic \( \le \) geometric \( \le \) arithmetic, and the same order holds for matrices.

::: {#cor-harmonic-geometric-arithmetic}
[Harmonic, Geometric and Arithmetic]

Let \( \A, \B \in M_n(F) \) be positive definite. Then
\[
\Bigl(\frac{\A^{-1} + \B^{-1}}{2}\Bigr)^{-1} \ \preceq\ \A\#\B \ \preceq\ \frac{\A + \B}{2} .
\]
:::

::: {.proof}
The right inequality is @thm-geometric-mean-properties (e). For the left, apply that same part to the positive definite matrices \( \A^{-1} \) and \( \B^{-1} \):
\[
\A^{-1}\#\B^{-1} \ \preceq\ \tfrac12(\A^{-1} + \B^{-1}) .
\]
Both sides are positive definite — the left by the remark after @def-geometric-mean, the right as a positive combination of positive definite matrices. Since \( t \mapsto -1/t \) is operator monotone on \( (0, \infty) \) (@prp-inverse-operator-monotone), applying it reverses the inequality between the inverses:
\[
\Bigl(\tfrac12(\A^{-1} + \B^{-1})\Bigr)^{-1} \ \preceq\ \bigl(\A^{-1}\#\B^{-1}\bigr)^{-1} .
\]
By @thm-geometric-mean-properties (e) the right side is \( \A\#\B \).
:::

The three means agree when \( \A = \B \), and for the pair of the worked example they are
\[
\tfrac15\begin{pmatrix}28&26\\26&37\end{pmatrix}
\ \preceq\
\begin{pmatrix}6&6\\6&9\end{pmatrix}
\ \preceq\
\begin{pmatrix}\tfrac{13}{2}&7\\7&11\end{pmatrix} ,
\]
the two differences being \( \tfrac25\begin{psmallmatrix}1&2\\2&4\end{psmallmatrix} \) and \( \tfrac12\begin{psmallmatrix}1&2\\2&4\end{psmallmatrix} \), each a non-negative multiple of a rank-one positive semidefinite matrix.

::: {.remark}
The geometric mean is the first genuinely non-commutative *average* in the book, and it is built out of two order facts proved long before this chapter: the operator monotonicity of \( t \mapsto t^{1/2} \), which is Chapter 12 §05's @prp-square-root-monotone, used in the claim inside @thm-geometric-mean-properties, and the operator monotonicity of \( t \mapsto -1/t \), which is Chapter 16 §11's @prp-inverse-operator-monotone, used in @cor-harmonic-geometric-arithmetic. Without the first, the extremal characterization would fail; without the second, the chain would have no left-hand end.
:::

## Exercises

### A. Check your understanding

:::: {#exr-matrix-means-and-inequalities-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define \( \A\#\B \) for positive definite \( \A, \B \), and say why each square root in the formula exists.
2. State the extremal characterization of \( \A\#\B \), and explain in one sentence how it makes the symmetry \( \A\#\B = \B\#\A \) obvious.
3. Decide whether the following is correct, and justify your answer: "\( \A^{1/2}\B^{1/2} \) is positive definite whenever \( \A \) and \( \B \) are".
4. State the matrix Cauchy–Schwarz inequality and the arithmetic–geometric mean inequality for singular values, @thm-matrix-am-gm — not the one for the geometric mean \( \A\#\B \) — and say which one implies the other and how.
5. Which of \( \A^{*}\A + \B^{*}\B \) and \( \A\A^{*} + \B\B^{*} \) bounds \( 2\uinorm{\A^{*}\B} \), and what goes wrong with the other?
:::
::::

::: {.solution}
(a) \( \A\#\B = \A^{1/2}(\A^{-1/2}\B\A^{-1/2})^{1/2}\A^{1/2} \) (@def-geometric-mean). The outer square root exists because \( \A \succ 0 \) (@thm-psd-square-root), and \( \A^{1/2} \succ 0 \) is invertible; the inner one because \( \A^{-1/2}\B\A^{-1/2} \) is a congruence of \( \B \succ 0 \) by an invertible matrix, hence \( \succ 0 \) (@prp-congruence-positivity (b)).

(b) It is the largest Hermitian \( \X \) with \( \begin{psmallmatrix}\A&\X\\\X&\B\end{psmallmatrix} \succeq 0 \) (@thm-geometric-mean-properties (a)). Swapping the two diagonal blocks is a congruence by the unitary \( \begin{psmallmatrix}\0&\I\\\I&\0\end{psmallmatrix} \), which changes neither the condition nor \( \X \), so \( (\A,\B) \) and \( (\B,\A) \) have the same admissible set and therefore the same largest element.

(c) Incorrect. It need not even be Hermitian: with \( \A = \diag(4,1) \) and \( \B = \begin{psmallmatrix}5&4\\4&5\end{psmallmatrix} \), \( \A^{1/2}\B^{1/2} = \begin{psmallmatrix}4&2\\1&2\end{psmallmatrix} \). It is Hermitian exactly when \( \A\B = \B\A \).

(d) Cauchy–Schwarz: \( \uinorm{\A^{*}\B}^2 \le \uinorm{\A^{*}\A}\uinorm{\B^{*}\B} \) (@thm-matrix-cauchy-schwarz). Arithmetic–geometric mean for singular values: \( 2\uinorm{\A^{*}\B} \le \uinorm{\A\A^{*}+\B\B^{*}} \) (@thm-matrix-am-gm). The second implies the first: replace \( \A \) by \( t\A \) and \( \B \) by \( t^{-1}\B \), which leaves \( \A^{*}\B \) alone, use the triangle inequality, and pick \( t \) to balance the two terms.

(e) \( \A\A^{*} + \B\B^{*} \) does (@thm-matrix-am-gm). With \( \A^{*}\A + \B^{*}\B \) the statement is false: the warning after that theorem gives \( \A, \B \) with \( \A^{*}\A + \B^{*}\B = \I \) of spectral norm \( 1 \) and \( 2\norm{\A^{*}\B}_2 = 2 \).
:::

### B. Practice

:::: {#exr-matrix-means-and-inequalities-b1}
[B1: A geometric mean, exactly]

Let
\[
\A = \begin{pmatrix} 5 & 4 \\ 4 & 5\end{pmatrix},
\qquad
\B = \begin{pmatrix} 13 & 20 \\ 20 & 37\end{pmatrix} .
\]

::: {.enumerate options="label=(\alph*)"}
1. Verify that \( \A^{1/2} = \begin{psmallmatrix}2&1\\1&2\end{psmallmatrix} \) and compute \( \C = \A^{-1/2}\B\A^{-1/2} \) and \( \A\#\B \).
2. Check the arithmetic–geometric mean inequality \( \A\#\B \preceq \tfrac12(\A+\B) \) directly, by computing the difference and its eigenvalues.
3. Verify the extremal characterization for your answer by computing the Schur complement \( \B - \X\A^{-1}\X \) with \( \X = \A\#\B \).
:::
::::

::: {.solution}
(a) \( \begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}^2 = \begin{psmallmatrix}5&4\\4&5\end{psmallmatrix} = \A \), and \( \begin{psmallmatrix}2&1\\1&2\end{psmallmatrix} \) has eigenvalues \( 3 \) and \( 1 \), both positive, so it is \( \succ 0 \) and is the positive square root (@thm-psd-square-root). Its determinant is \( 3 \), so \( \A^{-1/2} = \tfrac13\begin{psmallmatrix}2&-1\\-1&2\end{psmallmatrix} \). Then
\[
\A^{-1/2}\B = \tfrac13\begin{pmatrix} 6 & 3 \\ 27 & 54\end{pmatrix} = \begin{pmatrix}2&1\\9&18\end{pmatrix},
\]
and multiplying on the right by \( \A^{-1/2} \) gives \( \C = \tfrac13\begin{psmallmatrix}3&0\\0&27\end{psmallmatrix} = \diag(1,9) \). Hence \( \C^{1/2} = \diag(1,3) \) and
\[
\A\#\B = \begin{pmatrix}2&1\\1&2\end{pmatrix}\begin{pmatrix}1&0\\0&3\end{pmatrix}\begin{pmatrix}2&1\\1&2\end{pmatrix} = \begin{pmatrix}7&8\\8&13\end{pmatrix} .
\]

(b) \( \tfrac12(\A+\B) = \begin{psmallmatrix}9&12\\12&21\end{psmallmatrix} \), so the difference is
\[
\tfrac12(\A+\B) - \A\#\B = \begin{pmatrix}2&4\\4&8\end{pmatrix} = 2\begin{pmatrix}1\\2\end{pmatrix}\begin{pmatrix}1&2\end{pmatrix} ,
\]
of trace \( 10 \) and determinant \( 16 - 16 = 0 \), so its eigenvalues are \( 10 \) and \( 0 \) and it is \( \succeq 0 \) (@thm-psd-characterizations (b)). The inequality holds, with the difference singular.

(c) \( \det\A = 9 \), so \( \A^{-1} = \tfrac19\begin{psmallmatrix}5&-4\\-4&5\end{psmallmatrix} \). With \( \X = \begin{psmallmatrix}7&8\\8&13\end{psmallmatrix} \),
\[
\X\A^{-1} = \tfrac19\begin{pmatrix}3&12\\-12&33\end{pmatrix} = \tfrac13\begin{pmatrix}1&4\\-4&11\end{pmatrix},
\]
and \( \X\A^{-1}\X = \tfrac13\begin{psmallmatrix}39&60\\60&111\end{psmallmatrix} = \begin{psmallmatrix}13&20\\20&37\end{psmallmatrix} = \B \). So the Schur complement is \( \0 \), which is \( \succeq 0 \): \( \X \) is admissible, and the block matrix is singular, as it must be at the largest admissible \( \X \).
:::

:::: {#exr-matrix-means-and-inequalities-b2}
[B2: The two inequalities on one pair]

Let \( \A = \begin{psmallmatrix}1&1\\0&1\end{psmallmatrix} \) and \( \B = \begin{psmallmatrix}1&0\\1&1\end{psmallmatrix} \) in \( M_2(\nR) \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \A^{*}\B \) and \( \A\A^{*} + \B\B^{*} \), and verify \( 2\sigma_j(\A^{*}\B) \le \lambda_j(\A\A^{*}+\B\B^{*}) \) for \( j = 1, 2 \) using traces and determinants.
2. Verify @thm-matrix-cauchy-schwarz for this pair in the Frobenius norm.
:::
::::

::: {.solution}
(a) \( \A^{*} = \begin{psmallmatrix}1&0\\1&1\end{psmallmatrix} \), so \( \A^{*}\B = \begin{psmallmatrix}1&0\\2&1\end{psmallmatrix} \), and \( \A\A^{*} = \begin{psmallmatrix}2&1\\1&1\end{psmallmatrix} \), \( \B\B^{*} = \begin{psmallmatrix}1&1\\1&2\end{psmallmatrix} \), so \( \A\A^{*}+\B\B^{*} = \begin{psmallmatrix}3&2\\2&3\end{psmallmatrix} \), with eigenvalues \( 5 \) and \( 1 \).

The singular values of \( \M = \A^{*}\B \) come from \( \M^{*}\M = \begin{psmallmatrix}5&2\\2&1\end{psmallmatrix} \), of trace \( 6 \) and determinant \( 1 \), so \( \sigma_1^2, \sigma_2^2 = 3 \pm 2\sqrt2 = (\sqrt2 \pm 1)^2 \) and \( \sigma_1 = \sqrt2+1 \), \( \sigma_2 = \sqrt2-1 \). Then \( 2\sigma_1 = 2\sqrt2 + 2 \approx 4.83 \le 5 \) and \( 2\sigma_2 = 2\sqrt2 - 2 \approx 0.83 \le 1 \). Both hold; the first is \( 2\sqrt2 \le 3 \), that is \( 8 \le 9 \), and the second is \( 2\sqrt 2 \le 3 \) again.

(b) \( \A^{*}\A = \begin{psmallmatrix}1&1\\1&2\end{psmallmatrix} \) and \( \B^{*}\B = \begin{psmallmatrix}2&1\\1&1\end{psmallmatrix} \), each of Frobenius norm \( \sqrt{1+1+1+4} = \sqrt7 \). And \( \norm{\A^{*}\B}_F^2 = 1 + 4 + 1 = 6 \). So the inequality reads \( 6 \le \sqrt7\cdot\sqrt7 = 7 \), which holds.
:::

:::: {#exr-matrix-means-and-inequalities-b3}
[B3: Means of commuting matrices]

Let \( \A = \diag(a_1, \dots, a_n) \) and \( \B = \diag(b_1, \dots, b_n) \) with all \( a_i, b_i > 0 \). Compute the three means of @cor-harmonic-geometric-arithmetic and deduce the classical chain of inequalities between the harmonic, geometric and arithmetic means of two positive numbers.
::::

::: {.solution}
The matrices commute, so \( \A\#\B = (\A\B)^{1/2} = \diag(\sqrt{a_ib_i}) \) by the third example after @def-geometric-mean. Also \( \tfrac12(\A+\B) = \diag\bigl(\tfrac{a_i+b_i}{2}\bigr) \) and
\[
\Bigl(\frac{\A^{-1}+\B^{-1}}{2}\Bigr)^{-1} = \diag\Bigl(\frac{2a_ib_i}{a_i+b_i}\Bigr) .
\]
A diagonal matrix is \( \succeq 0 \) exactly when its entries are \( \ge 0 \), so @cor-harmonic-geometric-arithmetic says precisely
\[
\frac{2a_ib_i}{a_i+b_i} \ \le\ \sqrt{a_ib_i} \ \le\ \frac{a_i+b_i}{2}
\]
for every \( i \), the classical chain for the two positive numbers \( a_i, b_i \). The right inequality is @lem-am-gm with two terms, and the left is the right one applied to \( 1/a_i \) and \( 1/b_i \) and inverted.
:::

### C. Going deeper

:::: {#exr-matrix-means-and-inequalities-c1}
[C1: The determinant of a geometric mean]

Let \( \A, \B \in M_n(F) \) be positive definite.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \det(\A\#\B) = \sqrt{\det\A\,\det\B} \).
2. Deduce from @cor-harmonic-geometric-arithmetic that \( \sqrt{\det\A\,\det\B} \le \det\bigl(\tfrac12(\A+\B)\bigr) \).
:::

*Hint for (b): the Loewner order compares determinants of positive definite matrices.*
::::

::: {.solution}
(a) Write \( \C = \A^{-1/2}\B\A^{-1/2} \). Taking determinants in @def-geometric-mean and using multiplicativity (@thm-det-multiplicative),
\[
\det(\A\#\B) = \det(\A^{1/2})^2\det(\C^{1/2}) = \det\A\cdot\det(\C^{1/2}) .
\]
Now \( (\C^{1/2})^2 = \C \) gives \( \det(\C^{1/2})^2 = \det\C \), and \( \det(\C^{1/2}) > 0 \) because \( \C^{1/2} \succ 0 \) has positive eigenvalues, so \( \det(\C^{1/2}) = \sqrt{\det\C} \). Finally \( \det\C = \det(\A^{-1/2})^2\det\B = \det\B/\det\A \). Hence
\[
\det(\A\#\B) = \det\A\cdot\sqrt{\det\B/\det\A} = \sqrt{\det\A\,\det\B} .
\]

(b) By @cor-harmonic-geometric-arithmetic, \( \A\#\B \preceq \tfrac12(\A+\B) \), and both are positive definite. For positive definite \( \X \preceq \Y \) we have \( \det\X \le \det\Y \): by @cor-loewner-eigenvalue-monotone, \( \lambda_i(\Y) \ge \lambda_i(\X) > 0 \) for every \( i \), and the determinant of a Hermitian matrix is the product of its eigenvalues with multiplicity (@thm-trace-det-eigenvalues, whose hypothesis holds because the characteristic polynomial of a Hermitian matrix splits over \( \nR \) by @thm-self-adjoint-real-eigenvalues), a product of positive numbers increasing in each factor. Applying this and part (a) gives the inequality. At \( n = 1 \) it is again the classical arithmetic–geometric mean inequality.
:::

:::: {#exr-matrix-means-and-inequalities-c2}
[C2: The geometric mean solves an equation]

Let \( \A, \B \in M_n(F) \) be positive definite.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \X = \A\#\B \) is the **only** positive definite solution of \( \X\A^{-1}\X = \B \).
2. Use (a) to give a second proof that \( \A\#\B = \B\#\A \).
:::
::::

::: {.solution}
(a) Write \( \C = \A^{-1/2}\B\A^{-1/2} \). A positive definite \( \X \) may be written uniquely as \( \X = \A^{1/2}\Y\A^{1/2} \) with \( \Y = \A^{-1/2}\X\A^{-1/2} \), and \( \Y \succ 0 \) by @prp-congruence-positivity (b). As computed in the proof of @thm-geometric-mean-properties (a), \( \X\A^{-1}\X = \A^{1/2}\Y^2\A^{1/2} \). So \( \X\A^{-1}\X = \B \) is equivalent to \( \A^{1/2}\Y^2\A^{1/2} = \A^{1/2}\C\A^{1/2} \), that is to \( \Y^2 = \C \), since \( \A^{1/2} \) is invertible. By the uniqueness of the positive square root (@thm-psd-square-root), the only positive definite solution is \( \Y = \C^{1/2} \), that is \( \X = \A\#\B \).

(b) Let \( \X = \A\#\B \), so \( \X\A^{-1}\X = \B \) by (a) and \( \X \succ 0 \) is invertible. Multiplying that identity on the left and on the right by \( \X^{-1} \) gives \( \A^{-1} = \X^{-1}\B\X^{-1} \), and inverting both sides gives \( \A = \X\B^{-1}\X \). So \( \X \) is a positive definite solution of \( \X\B^{-1}\X = \A \), which by (a), with the roles of \( \A \) and \( \B \) exchanged, has \( \B\#\A \) as its only positive definite solution. Hence \( \A\#\B = \B\#\A \).
:::

:::: {#exr-matrix-means-and-inequalities-c3}
[C3: Cauchy–Schwarz for the Ky Fan norms, directly]

Let \( \A, \B \in M_n(F) \) and \( 1 \le k \le n \).

::: {.enumerate options="label=(\alph*)"}
1. Let \( \A^{*}\B = \W\vSigma\Z^{*} \) be a singular value decomposition (@thm-svd), and let \( \U_k \) and \( \V_k \) be the matrices of the first \( k \) columns of \( \W \) and of \( \Z \). Show that \( \tr(\U_k^{*}\A^{*}\B\V_k) = \sum_{j \le k}\sigma_j(\A^{*}\B) \).
2. Deduce, using the Cauchy–Schwarz inequality for the Frobenius inner product (@thm-cauchy-schwarz) and the Ky Fan maximum principle (@thm-ky-fan), that
\[
\sum_{j \le k}\sigma_j(\A^{*}\B) \le \Bigl(\sum_{j \le k}\lambda_j(\A^{*}\A)\Bigr)^{1/2}\Bigl(\sum_{j\le k}\lambda_j(\B^{*}\B)\Bigr)^{1/2} .
\]
:::
::::

::: {.solution}
(a) The columns of \( \W \) and \( \Z \) are orthonormal, so \( \U_k^{*}\W = (\I_k \ \ \0) \) and \( \Z^{*}\V_k = \begin{psmallmatrix}\I_k\\\0\end{psmallmatrix} \). Hence
\[
\U_k^{*}\A^{*}\B\V_k = \U_k^{*}\W\vSigma\Z^{*}\V_k = \diag\bigl(\sigma_1, \dots, \sigma_k\bigr) ,
\]
the top-left \( k \times k \) corner of \( \vSigma \), whose trace is \( \sum_{j\le k}\sigma_j(\A^{*}\B) \).

(b) Writing the trace as the Frobenius inner product \( \inner{\X}{\Y} = \tr(\Y^{*}\X) \) of Chapter 10 §01,
\[
\tr\bigl(\U_k^{*}\A^{*}\B\V_k\bigr) = \tr\bigl((\A\U_k)^{*}(\B\V_k)\bigr) = \inner{\B\V_k}{\A\U_k} ,
\]
so by @thm-cauchy-schwarz it is at most \( \norm{\A\U_k}_F\norm{\B\V_k}_F \). Now \( \U_k^{*}\U_k = \I_k \), so \( \U_k \) is an isometry and
\[
\norm{\A\U_k}_F^2 = \tr\bigl(\U_k^{*}\A^{*}\A\U_k\bigr) \ \le\ \sum_{j\le k}\lambda_j(\A^{*}\A)
\]
by @thm-ky-fan applied to the Hermitian matrix \( \A^{*}\A \). The same bound holds for \( \norm{\B\V_k}_F^2 \) with \( \B^{*}\B \). Combining with (a) gives the display. (Taking \( k = n \) recovers @thm-matrix-cauchy-schwarz for the trace norm.)
:::
