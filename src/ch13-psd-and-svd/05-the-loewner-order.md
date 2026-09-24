# The Loewner Order

Every theorem so far in this chapter has compared a self-adjoint matrix with \( 0 \). Comparing it with \( 0 \) is only the first case of comparing it with something, and the analogy with real numbers suggests the general one: say that \( \A \) is at least \( \B \) when the difference is non-negative. That is a genuine order, and a surprising amount of ordinary arithmetic survives it. A little does not, and what fails is the point of the section: squaring both sides of an inequality between matrices is not allowed.

Throughout, \( F = \nR \) or \( F = \nC \), all matrices are in \( M_n(F) \), and \( \lambda_1(\A) \ge \dots \ge \lambda_n(\A) \) are the eigenvalues of a Hermitian \( \A \) in decreasing order.

## Comparing two self-adjoint matrices

The relation \( \A \succeq 0 \) already behaves like "\( \ge 0 \)" for numbers: it is preserved by sums, by non-negative scalars and by congruence (@prp-congruence-positivity). For real numbers, \( a \ge b \) means nothing other than \( a - b \ge 0 \). Copying that sentence is the whole definition.

*One self-adjoint matrix dominates another when their difference is positive semidefinite.*

::: {#def-loewner-order}
[The Loewner order]

Let \( \A, \B \in M_n(F) \) be Hermitian. Write
\[
\A \succeq \B \quad \text{to mean} \quad \A - \B \succeq 0 ,
\]
and \( \A \succ \B \) to mean \( \A - \B \succ 0 \). This relation on the set of Hermitian matrices is the **Loewner order**.
:::

In words: \( \A \succeq \B \) says that \( \inner{\A\x}{\x} \ge \inner{\B\x}{\x} \) for **every** \( \x \in F^n \), since \( \inner{(\A - \B)\x}{\x} = \inner{\A\x}{\x} - \inner{\B\x}{\x} \). So the order compares the two quadratic forms pointwise, and it is exactly as strong as that comparison. Note also that the difference of two Hermitian matrices is Hermitian, so clause (P1) of @def-positive-semidefinite is automatic here and only (P2) has to be checked. Taking \( \B = \0 \) recovers \( \A \succeq 0 \), so the notation is consistent.

Three examples, each of which will be used later.

- **Diagonal matrices.** \( \diag(a_1, \dots, a_n) \succeq \diag(b_1, \dots, b_n) \) if and only if \( a_i \ge b_i \) for every \( i \), since the difference is diagonal and a diagonal Hermitian matrix is positive semidefinite exactly when its entries, which are its eigenvalues, are \( \ge 0 \) (@thm-psd-characterizations).
- **Eigenvalue bounds.** For Hermitian \( \A \), \( \lambda_1(\A)\I \succeq \A \succeq \lambda_n(\A)\I \). Indeed \( \lambda_1(\A)\I - \A \) is Hermitian with eigenvalues \( \lambda_1(\A) - \lambda_i(\A) \ge 0 \).
- **Projections.** If \( \P \in M_n(F) \) is the matrix of an orthogonal projection onto a subspace of \( F^n \), then \( \I \succeq \P \succeq 0 \): it is Hermitian, and its eigenvalues are \( 0 \) and \( 1 \).

A **non-example by minimal change**: replace \( \diag(1, 1) \) by \( \diag(1, -1) \) in the first item. Then \( \diag(1, -1) \succeq \diag(0, 0) \) fails, and it fails only in the second coordinate — the test is coordinatewise for diagonal matrices, and one bad coordinate is enough.

::: {#prp-loewner-partial-order}
[The Loewner order is a partial order]

On the set of Hermitian matrices in \( M_n(F) \), the relation \( \succeq \) is reflexive, transitive and antisymmetric: \( \A \succeq \A \); if \( \A \succeq \B \) and \( \B \succeq \C \) then \( \A \succeq \C \); and if \( \A \succeq \B \) and \( \B \succeq \A \) then \( \A = \B \).
:::

::: {.proof}
Reflexivity: \( \A - \A = \0 \), and \( \inner{\0\x}{\x} = 0 \ge 0 \).

Transitivity: \( \A - \C = (\A - \B) + (\B - \C) \), and for every \( \x \),
\[
\inner{(\A - \C)\x}{\x} = \inner{(\A - \B)\x}{\x} + \inner{(\B - \C)\x}{\x} \ \ge\ 0 ,
\]
both summands being \( \ge 0 \) by hypothesis.

Antisymmetry: put \( \S = \A - \B \), which is Hermitian. From \( \A \succeq \B \) we get \( \inner{\S\x}{\x} \ge 0 \) for every \( \x \), and from \( \B \succeq \A \) we get \( \inner{-\S\x}{\x} \ge 0 \), that is \( \inner{\S\x}{\x} \le 0 \). Hence \( \inner{\S\x}{\x} = 0 \) for every \( \x \in F^n \), and \( \S \) is self-adjoint, so \( \S = \0 \) by @thm-self-adjoint-zero-test. Thus \( \A = \B \).
:::

Antisymmetry is the clause that needed an argument, and the argument is the one the chapter keeps reusing: a self-adjoint matrix is determined by its quadratic form. Over \( \nR \) this is genuinely a theorem — the quarter turn of @def-positive-semidefinite's warning has vanishing quadratic form and is not \( \0 \) — and it is self-adjointness that rules that out.

::: {.warning}
**The Loewner order is partial, and it is not the entrywise order.** Two things go wrong if one forgets this. First, most pairs are incomparable: \( \A = \diag(1, 0) \) and \( \B = \diag(0, 1) \) satisfy neither \( \A \succeq \B \) nor \( \B \succeq \A \), so an argument that splits into "either \( \A \succeq \B \) or \( \B \succeq \A \)" is not an argument. Second, \( \A \succeq \B \) says nothing entrywise, in either direction:
\[
\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} \succeq \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix},
\qquad\text{yet the off-diagonal entries went down;}
\]
the difference is \( \begin{psmallmatrix} 1 & -1 \\ -1 & 1\end{psmallmatrix} \), with eigenvalues \( 0 \) and \( 2 \). Conversely \( \begin{psmallmatrix} 1 & 2 \\ 2 & 1\end{psmallmatrix} \) has every entry \( \ge 0 \) and is **not** \( \succeq 0 \), its eigenvalues being \( 3 \) and \( -1 \).
:::

::: {.check}
Is the set of Hermitian \( \A \) with \( \I \succeq \A \succeq 0 \) closed under multiplication?
:::

::: {.solution}
No. Take \( \A = \begin{psmallmatrix} 1 & 0 \\ 0 & 0\end{psmallmatrix} \) and \( \B = \tfrac12\begin{psmallmatrix} 1 & 1 \\ 1 & 1\end{psmallmatrix} \), both orthogonal projections, so both lie in the set. Then \( \A\B = \tfrac12\begin{psmallmatrix} 1 & 1 \\ 0 & 0\end{psmallmatrix} \), which is not even Hermitian, so it is not in the set and the order does not apply to it. The order lives on Hermitian matrices, and Hermitian matrices are not closed under multiplication (@exr-self-adjoint-operators-c2).
:::

## What survives

One small fact is needed first, and it is worth stating on its own because it is the elementary half of a theme Chapter 17 takes up in full: the largest and smallest eigenvalues of a Hermitian matrix are the largest and smallest values of its quadratic form on the unit sphere.

::: {#lem-extreme-eigenvalues-quadratic-form}
[The extreme eigenvalues as extreme values]

Let \( \A \in M_n(F) \) be Hermitian. Then for every \( \x \in F^n \) with \( \norm{\x} = 1 \),
\[
\lambda_n(\A) \ \le\ \inner{\A\x}{\x} \ \le\ \lambda_1(\A) ,
\]
and both bounds are attained, at unit eigenvectors for \( \lambda_n(\A) \) and \( \lambda_1(\A) \) respectively.
:::

::: {.proof}
By @cor-spectral-complex-matrix (over \( \nC \)) or @cor-spectral-real-matrix (over \( \nR \)), \( F^n \) has an orthonormal basis \( (\q_1, \dots, \q_n) \) with \( \A\q_i = \lambda_i(\A)\q_i \). Write \( \x = \sum_i c_i\q_i \); then \( \sum_i\lvert c_i\rvert^2 = \norm{\x}^2 = 1 \) by @thm-orthonormal-coordinates, and
\[
\inner{\A\x}{\x} = \Big\langle \sum_i \lambda_i(\A)c_i\q_i, \sum_j c_j\q_j\Big\rangle = \sum_{i} \lambda_i(\A)\lvert c_i\rvert^2 ,
\]
the cross terms vanishing by orthonormality. The right-hand side is a weighted average of the \( \lambda_i(\A) \) with non-negative weights summing to \( 1 \), hence lies between the smallest and the largest. Taking \( \x = \q_1 \) gives \( \lambda_1(\A) \) and \( \x = \q_n \) gives \( \lambda_n(\A) \).
:::

:::: {#thm-loewner-basic}
[Basic Properties of the Loewner Order]

Let \( \A, \B \in M_n(F) \) be Hermitian with \( \A \succeq \B \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \S^{*}\A\S \succeq \S^{*}\B\S \) for every \( \S \in M_{n \times m}(F) \);
2. \( \lambda_1(\A) \ge \lambda_1(\B) \) and \( \lambda_n(\A) \ge \lambda_n(\B) \);
3. if moreover \( \B \succeq 0 \), then \( \tr\A \ge \tr\B \) and \( \det\A \ge \det\B \);
4. if moreover \( \B \succ 0 \), then \( \A \succ 0 \) and \( \B^{-1} \succeq \A^{-1} \).
:::
::::

::: {.idea}
Each clause has a one-line mechanism. (a) is the substitution \( \x = \S\y \). (b) evaluates the quadratic form at the vector that is extremal for the *other* matrix. (c) splits: the trace is a sum of eigenvalues, and for the determinant we whiten by \( \B^{-1/2} \) so that the comparison becomes "\( \succeq \I \)", where the determinant is visibly \( \ge 1 \). (d) is the same whitening, plus the observation that inverting reverses the order for *numbers* \( \ge 1 \).
:::

::: {.proof}
(a) This is @prp-congruence-positivity (a) applied to the Hermitian matrix \( \A - \B \succeq 0 \), together with \( \S^{*}\A\S - \S^{*}\B\S = \S^{*}(\A - \B)\S \).

(b) Let \( \x \) be a unit eigenvector of \( \B \) for \( \lambda_1(\B) \). By @lem-extreme-eigenvalues-quadratic-form applied twice, and \( \A \succeq \B \) in between,
\[
\lambda_1(\B) = \inner{\B\x}{\x} \le \inner{\A\x}{\x} \le \lambda_1(\A) .
\]
Now let \( \y \) be a unit eigenvector of \( \A \) for \( \lambda_n(\A) \). Then
\[
\lambda_n(\A) = \inner{\A\y}{\y} \ge \inner{\B\y}{\y} \ge \lambda_n(\B) .
\]

(c) The matrix \( \A - \B \) is Hermitian and \( \succeq 0 \), so all its eigenvalues are \( \ge 0 \) by @thm-psd-characterizations, and \( \tr(\A - \B) \), being their sum (@thm-trace-det-eigenvalues), is \( \ge 0 \). Hence \( \tr\A \ge \tr\B \).

For the determinant, first note \( \A \succeq \B \succeq 0 \) gives \( \A \succeq 0 \) by @prp-loewner-partial-order, so \( \det\A \ge 0 \) and \( \det\B \ge 0 \), both being products of non-negative eigenvalues. If \( \B \) is singular then \( \det\B = 0 \le \det\A \) and we are done. Otherwise \( \B \succeq 0 \) with no zero eigenvalue means \( \B \succ 0 \) (@thm-pd-characterizations), so \( \B^{1/2} \succ 0 \) is invertible and we may set \( \C = \B^{-1/2}\A\B^{-1/2} \), where \( \B^{-1/2} = (\B^{1/2})^{-1} \) is Hermitian. By (a) with \( \S = \B^{-1/2} \),
\[
\C = \B^{-1/2}\A\B^{-1/2} \ \succeq\ \B^{-1/2}\B\B^{-1/2} = \I_n ,
\]
so \( \C - \I \succeq 0 \) and every eigenvalue of \( \C \) is \( \ge 1 \). Hence \( \det\C \ge 1 \). Since \( \A = \B^{1/2}\C\B^{1/2} \), @thm-det-multiplicative gives
\[
\det\A = \det(\B^{1/2})^2\det\C = \det\B\cdot\det\C \ \ge\ \det\B .
\]

(d) Suppose \( \B \succ 0 \). For \( \x \ne \0 \), \( \inner{\A\x}{\x} \ge \inner{\B\x}{\x} > 0 \), so \( \A \succ 0 \) and in particular \( \A \) is invertible (@thm-pd-characterizations). Let \( \C = \B^{-1/2}\A\B^{-1/2} \succeq \I \) as in (c). Then \( \C \succ 0 \), so \( \C \) is invertible, and \( \C^{-1} \) is Hermitian with eigenvalues the reciprocals of those of \( \C \), all lying in \( (0, 1] \). Therefore \( \I - \C^{-1} \) is Hermitian with non-negative eigenvalues, that is \( \I \succeq \C^{-1} \) (@thm-psd-characterizations). Applying (a) with \( \S = \B^{-1/2} \) to this inequality,
\[
\B^{-1} = \B^{-1/2}\I\B^{-1/2} \ \succeq\ \B^{-1/2}\C^{-1}\B^{-1/2} = \B^{-1/2}\B^{1/2}\A^{-1}\B^{1/2}\B^{-1/2} = \A^{-1} ,
\]
using \( \C^{-1} = (\B^{-1/2}\A\B^{-1/2})^{-1} = \B^{1/2}\A^{-1}\B^{1/2} \). This proves the theorem.
:::

Clause (d) is the memorable one: **the order reverses under inversion**, exactly as \( a \ge b > 0 \) gives \( 1/b \ge 1/a \) for numbers. Clause (b) is the beginning of a longer story. The full statement is that \( \lambda_i(\A) \ge \lambda_i(\B) \) for **every** \( i \), not only for \( i = 1 \) and \( i = n \); but the intermediate eigenvalues have no description as a plain maximum over the whole unit sphere, and the min–max description that does the job is the Courant–Fischer theorem of Chapter 17. Nothing in this chapter uses the intermediate cases, so we prove the two extreme ones and leave the rest there.

::: {.remark}
Clause (c) does not extend to \( \A \succeq \B \) without \( \B \succeq 0 \). Take \( \A = \diag(1, -1) \) and \( \B = \diag(0, -2) \): then \( \A - \B = \diag(1, 1) \succeq 0 \), so \( \A \succeq \B \), yet \( \det\A = -1 < 0 = \det\B \). The hypothesis \( \B \succeq 0 \) is what lets "bigger" be read off the eigenvalues one at a time, and so multiplied up into a determinant.
:::

## What fails: squaring

For positive numbers, \( a \ge b \ge 0 \) implies \( a^2 \ge b^2 \). The matrix version is false, and the smallest counterexample has integer entries.

:::: {#exm-loewner-not-monotone}
[Squaring does not preserve the Loewner order]

Let
\[
\A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}, \qquad
\B = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} .
\]
Show that \( \A \succeq \B \succeq 0 \) and that \( \A^2 \succeq \B^2 \) is false.
::::

::: {.solution}
*The hypotheses.* Both matrices are real symmetric. \( \B \succeq 0 \): its leading principal minors are \( 1 \) and \( 0 \), and directly \( \x\tp\B\x = (x_1 + x_2)^2 \ge 0 \). Its eigenvalues are \( 0 \) and \( 2 \). Next,
\[
\A - \B = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \succeq 0 ,
\]
so \( \A \succeq \B \). (In fact \( \A \succ 0 \): \( \det\A = 1 > 0 \) and \( a_{11} = 2 > 0 \), so Sylvester's criterion applies, @thm-pd-characterizations.)

*The squares.*
\[
\A^2 = \begin{pmatrix} 5 & 3 \\ 3 & 2 \end{pmatrix}, \qquad
\B^2 = \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix}, \qquad
\A^2 - \B^2 = \begin{pmatrix} 3 & 1 \\ 1 & 0 \end{pmatrix} .
\]
Its determinant is \( 0 - 1 = -1 < 0 \), so its two eigenvalues have opposite signs and it is not positive semidefinite (@thm-psd-characterizations). A witness is available without computing eigenvalues: with \( \x = (1, -2) \),
\[
\x\tp(\A^2 - \B^2)\x = 3 - 4 + 0 = -1 < 0 .
\]
So \( \A^2 \not\succeq \B^2 \).
:::

Where does the argument for numbers break? It uses \( a^2 - b^2 = (a - b)(a + b) \), a product of two non-negative numbers. For matrices, \( (\A - \B)(\A + \B) = \A^2 + \A\B - \B\A - \B^2 \), which is \( \A^2 - \B^2 \) only when \( \A \) and \( \B \) commute — and in the example \( \A\B = \begin{psmallmatrix} 3 & 3 \\ 2 & 2 \end{psmallmatrix} \) while \( \B\A = \begin{psmallmatrix} 3 & 2 \\ 3 & 2\end{psmallmatrix} \). Non-commutativity is the whole obstruction, and when it is removed the number argument goes through; that is exercise C1.

What *is* true is the same statement for the square **root**, and it is true with no commuting hypothesis at all.

::: {#prp-square-root-monotone}
[The square root is order preserving]

Let \( \A, \B \in M_n(F) \) with \( \A \succeq \B \succeq 0 \). Then \( \A^{1/2} \succeq \B^{1/2} \).
:::

::: {.idea}
Suppose not. Then \( \X - \Y \), with \( \X = \A^{1/2} \) and \( \Y = \B^{1/2} \), has a negative eigenvalue \( \mu \), with unit eigenvector \( \u \). Two different consequences of \( \X\u = \Y\u + \mu\u \) then collide. Pairing with \( \u \) says \( \inner{\Y\u}{\u} \ge \lvert\mu\rvert \), because \( \inner{\X\u}{\u} \ge 0 \). Taking norms and using \( \norm{\X\u}^2 \ge \norm{\Y\u}^2 \), which is exactly the hypothesis \( \A \succeq \B \), says \( \lvert\mu\rvert \ge 2\inner{\Y\u}{\u} \). Together: \( \lvert\mu\rvert \ge 2\lvert\mu\rvert \).
:::

::: {.proof}
Write \( \X = \A^{1/2} \) and \( \Y = \B^{1/2} \), both Hermitian and \( \succeq 0 \) with \( \X^2 = \A \) and \( \Y^2 = \B \) (@thm-psd-square-root). Then \( \X - \Y \) is Hermitian. Suppose, for a contradiction, that \( \X - \Y \not\succeq 0 \). By @thm-psd-characterizations it has a negative eigenvalue \( \mu < 0 \); choose a unit eigenvector \( \u \), so that
\[
\X\u = \Y\u + \mu\u .
\]

Pairing this with \( \u \) and using \( \norm{\u} = 1 \),
\[
\inner{\X\u}{\u} = \inner{\Y\u}{\u} + \mu .
\]
All three numbers are real (@prp-self-adjoint-immediate), and \( \inner{\X\u}{\u} \ge 0 \) because \( \X \succeq 0 \). Therefore
\[
\inner{\Y\u}{\u} \ \ge\ -\mu = \lvert\mu\rvert . \tag{$\ast$}
\]

Now take squared norms. Since \( \X \) is Hermitian, \( \norm{\X\u}^2 = \inner{\X^2\u}{\u} = \inner{\A\u}{\u} \), and likewise \( \norm{\Y\u}^2 = \inner{\B\u}{\u} \); so \( \A \succeq \B \) gives \( \norm{\X\u}^2 \ge \norm{\Y\u}^2 \). On the other hand, expanding \( \X\u = \Y\u + \mu\u \),
\[
\norm{\X\u}^2 = \norm{\Y\u}^2 + 2\mu\inner{\Y\u}{\u} + \mu^2 ,
\]
where the cross term is \( 2\mu\inner{\Y\u}{\u} \) because \( \mu \) and \( \inner{\Y\u}{\u} \) are real. Comparing the two,
\[
2\mu\inner{\Y\u}{\u} + \mu^2 \ \ge\ 0 .
\]
Substituting \( \mu = -\lvert\mu\rvert \) turns this into \( \lvert\mu\rvert^2 \ge 2\lvert\mu\rvert\inner{\Y\u}{\u} \), and dividing by \( \lvert\mu\rvert > 0 \) gives
\[
\lvert\mu\rvert \ \ge\ 2\inner{\Y\u}{\u} . \tag{$\ast\ast$}
\]
Combining \( (\ast) \) and \( (\ast\ast) \), \( \lvert\mu\rvert \ge 2\lvert\mu\rvert \), so \( \lvert\mu\rvert \le 0 \) and \( \mu = 0 \), contradicting \( \mu < 0 \). Hence \( \X - \Y \succeq 0 \), which is the assertion.
:::

So among the powers \( t \mapsto t^{s} \), the exponent \( s = 1/2 \) preserves the Loewner order while \( s = 2 \) does not. The dividing line is at \( s = 1 \): the functions preserving the order are called **operator monotone**, and \( t \mapsto t^{s} \) is operator monotone on \( [0, \infty) \) exactly for \( 0 \le s \le 1 \). Chapter 21 proves this, along with the companion fact that \( t \mapsto \log t \) is operator monotone while \( t \mapsto e^{t} \) is not.

## Exercises

### A. Check your understanding

:::: {#exr-the-loewner-order-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define \( \A \succeq \B \), and say on which set of matrices the relation is defined.
2. Determine whether the following statement is correct, and justify your answer: for Hermitian \( \A, \B \), either \( \A \succeq \B \) or \( \B \succeq \A \).
3. Determine whether the following statement is correct, and justify your answer: \( \A \succeq \B \) implies \( a_{ij} \ge b_{ij} \) for all \( i, j \).
4. State what fails when both sides of \( \A \succeq \B \succeq 0 \) are squared, and what happens instead when both sides have their square roots taken.
5. Which clause of @thm-loewner-basic reverses an inequality, and what is the analogous fact about real numbers?
:::
::::

::: {.solution}
(a) For Hermitian \( \A, \B \in M_n(F) \), \( \A \succeq \B \) means \( \A - \B \succeq 0 \), equivalently \( \inner{\A\x}{\x} \ge \inner{\B\x}{\x} \) for every \( \x \in F^n \) (@def-loewner-order). It is defined on the Hermitian matrices of a fixed size.

(b) Incorrect: the order is partial. \( \diag(1,0) \) and \( \diag(0,1) \) are incomparable, since \( \diag(1,-1) \) and \( \diag(-1,1) \) are both indefinite.

(c) Incorrect. \( \diag(2,2) \succeq \begin{psmallmatrix}1&1\\1&1\end{psmallmatrix} \), because the difference \( \begin{psmallmatrix}1&-1\\-1&1\end{psmallmatrix} \) has eigenvalues \( 0 \) and \( 2 \); yet the \( (1,2) \)-entries are \( 0 \) and \( 1 \).

(d) Squaring fails: \( \A \succeq \B \succeq 0 \) does not give \( \A^2 \succeq \B^2 \) (@exm-loewner-not-monotone). Taking square roots is legitimate: \( \A^{1/2} \succeq \B^{1/2} \) (@prp-square-root-monotone).

(e) Clause (d): \( \A \succeq \B \succ 0 \) gives \( \B^{-1} \succeq \A^{-1} \). For real numbers, \( a \ge b > 0 \) gives \( 1/b \ge 1/a \).
:::

### B. Practice

:::: {#exr-the-loewner-order-b1}
[B1: Decide the relation]

For each pair of real symmetric matrices, determine whether \( \A \succeq \B \), whether \( \B \succeq \A \), or neither. Justify your answer.

::: {.enumerate options="label=(\roman*)"}
1. \( \A = \begin{pmatrix} 3 & 1 \\ 1 & 3\end{pmatrix} \), \( \B = \I_2 \).
2. \( \A = \begin{pmatrix} 2 & 0 \\ 0 & 1\end{pmatrix} \), \( \B = \begin{pmatrix} 1 & 1 \\ 1 & 1\end{pmatrix} \).
3. \( \A = \begin{pmatrix} 1 & 0 \\ 0 & 3\end{pmatrix} \), \( \B = \begin{pmatrix} 2 & 0 \\ 0 & 1\end{pmatrix} \).
:::
::::

::: {.solution}
(i) \( \A - \B = \begin{psmallmatrix} 2 & 1 \\ 1 & 2\end{psmallmatrix} \), with leading principal minors \( 2 \) and \( 3 \), both \( > 0 \), so \( \A - \B \succ 0 \) by @thm-pd-characterizations and \( \A \succ \B \). Then \( \B \succeq \A \) would force \( \A = \B \) by @prp-loewner-partial-order, which is false, so \( \B \not\succeq \A \).

(ii) \( \A - \B = \begin{psmallmatrix} 1 & -1 \\ -1 & 0\end{psmallmatrix} \), with determinant \( -1 < 0 \), so it is indefinite and \( \A \not\succeq \B \). Also \( \B - \A \) has determinant \( -1 \), so \( \B \not\succeq \A \). Neither.

(iii) \( \A - \B = \diag(-1, 2) \), indefinite; \( \B - \A = \diag(1, -2) \), indefinite. Neither. (For diagonal matrices the comparison is entrywise, and the two entries disagree.)
:::

:::: {#exr-the-loewner-order-b2}
[B2: The order reverses]

Let \( \A = \begin{pmatrix} 3 & 1 \\ 1 & 3\end{pmatrix} \) and \( \B = \begin{pmatrix} 2 & 1 \\ 1 & 2\end{pmatrix} \). Verify that \( \A \succeq \B \succ 0 \), compute \( \A^{-1} \) and \( \B^{-1} \), and check @thm-loewner-basic (d) directly. Check the determinant clause as well.
::::

::: {.solution}
\( \A - \B = \I_2 \succ 0 \), so \( \A \succ \B \). And \( \B \succ 0 \), its leading principal minors being \( 2 \) and \( 3 \). Then \( \det\A = 8 \), \( \det\B = 3 \), so
\[
\A^{-1} = \frac{1}{8}\begin{pmatrix} 3 & -1 \\ -1 & 3 \end{pmatrix}, \qquad
\B^{-1} = \frac{1}{3}\begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix},
\]
and
\[
\B^{-1} - \A^{-1} = \frac{1}{24}\begin{pmatrix} 16 - 9 & -8 + 3 \\ -8 + 3 & 16 - 9\end{pmatrix}
= \frac{1}{24}\begin{pmatrix} 7 & -5 \\ -5 & 7\end{pmatrix} .
\]
Its leading principal minors are \( 7/24 > 0 \) and \( (49 - 25)/576 = 1/24 > 0 \), so \( \B^{-1} \succ \A^{-1} \), as @thm-loewner-basic (d) predicts. For the determinant clause, \( \det\A = 8 \ge 3 = \det\B \); and for the trace, \( 6 \ge 4 \).
:::

:::: {#exr-the-loewner-order-b3}
[B3: Another failure of squaring]

Let \( \A = \begin{pmatrix} 3 & 1 \\ 1 & 1\end{pmatrix} \) and \( \B = \begin{pmatrix} 1 & 1 \\ 1 & 1\end{pmatrix} \). Verify that \( \A \succeq \B \succeq 0 \), and exhibit a vector \( \x \) with \( \x\tp(\A^2 - \B^2)\x < 0 \).
::::

::: {.solution}
\( \A - \B = \diag(2, 0) \succeq 0 \), so \( \A \succeq \B \); and \( \x\tp\B\x = (x_1 + x_2)^2 \ge 0 \), so \( \B \succeq 0 \). Squaring,
\[
\A^2 = \begin{pmatrix} 10 & 4 \\ 4 & 2 \end{pmatrix}, \qquad
\B^2 = \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix}, \qquad
\A^2 - \B^2 = \begin{pmatrix} 8 & 2 \\ 2 & 0 \end{pmatrix},
\]
whose determinant is \( -4 < 0 \). With \( \x = (1, -3) \),
\[
\x\tp(\A^2 - \B^2)\x = 8 - 12 + 0 = -4 < 0 .
\]
So \( \A^2 \not\succeq \B^2 \). (Any \( \x = (1, t) \) with \( t < -2 \) works, since the value is \( 8 + 4t \).)
:::

### C. Going deeper

:::: {#exr-the-loewner-order-c1}
[C1: When squaring does work]

Let \( \A, \B \in M_n(F) \) with \( \A \succeq \B \succeq 0 \) and \( \A\B = \B\A \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( \P, \Q \succeq 0 \) and \( \P\Q = \Q\P \), then \( \P\Q \succeq 0 \).
2. Deduce that \( \A^2 \succeq \B^2 \).
3. Deduce that \( \A^k \succeq \B^k \) for every integer \( k \ge 1 \).
:::

*Hint for (a): \( \P^{1/2} \) is a polynomial in \( \P \).*
::::

::: {.solution}
(a) By @thm-psd-square-root, \( \P^{1/2} \) is a polynomial in \( \P \), so it commutes with every matrix that commutes with \( \P \); in particular \( \P^{1/2}\Q = \Q\P^{1/2} \). Hence
\[
\P\Q = \P^{1/2}\P^{1/2}\Q = \P^{1/2}\Q\P^{1/2} = (\P^{1/2})^{*}\Q\P^{1/2} ,
\]
which is \( \succeq 0 \) by @prp-congruence-positivity (a), since \( \Q \succeq 0 \) and \( \P^{1/2} \) is Hermitian.

(b) Put \( \P = \A - \B \) and \( \Q = \A + \B \). Both are \( \succeq 0 \): the first by hypothesis, the second as a sum of two matrices \( \succeq 0 \), using \( \A \succeq \B \succeq 0 \) and @prp-loewner-partial-order. They commute, because \( \A\B = \B\A \) makes \( \P\Q = \A^2 + \A\B - \B\A - \B^2 = \A^2 - \B^2 \) and \( \Q\P = \A^2 - \A\B + \B\A - \B^2 = \A^2 - \B^2 \) as well. By (a), \( \A^2 - \B^2 = \P\Q \succeq 0 \).

(c) Induction on \( k \). The case \( k = 1 \) is the hypothesis. Assume \( \A^{k-1} \succeq \B^{k-1} \). Then
\[
\A^k - \B^k = \A^{k-1}(\A - \B) + (\A^{k-1} - \B^{k-1})\B ,
\]
and each term is \( \succeq 0 \) by (a). Indeed \( \A \succeq 0 \) is Hermitian with eigenvalues \( \ge 0 \), so \( \A^{k-1} \) is Hermitian with eigenvalues \( \ge 0 \) and hence \( \A^{k-1} \succeq 0 \) (@thm-psd-characterizations); it commutes with \( \A - \B \), since \( \A\B = \B\A \). Likewise \( \A^{k-1} - \B^{k-1} \succeq 0 \) by the induction hypothesis and it commutes with \( \B \succeq 0 \). Finally a sum of two matrices \( \succeq 0 \) is \( \succeq 0 \), directly from @def-positive-semidefinite.
:::

:::: {#exr-the-loewner-order-c2}
[C2: Kernels and ranks]

Let \( \A, \B \in M_n(F) \) with \( \A \succeq \B \succeq 0 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \nul(\A) \subseteq \nul(\B) \).
2. Deduce that \( \rank\A \ge \rank\B \).
3. Give an example with \( \A \succeq \B \succeq 0 \) and \( \rank\A = \rank\B \) but \( \A \ne \B \).
:::

*Hint for (a): pair \( \A\x = \0 \) with \( \x \), then use \( \B^{1/2} \).*
::::

::: {.solution}
(a) Let \( \x \in \nul(\A) \). Then \( \inner{\A\x}{\x} = 0 \), and \( 0 \le \inner{\B\x}{\x} \le \inner{\A\x}{\x} = 0 \), so \( \inner{\B\x}{\x} = 0 \). Writing \( \B = \B^{1/2}\B^{1/2} \) with \( \B^{1/2} \) Hermitian (@thm-psd-square-root),
\[
0 = \inner{\B\x}{\x} = \inner{\B^{1/2}\x}{\B^{1/2}\x} = \norm{\B^{1/2}\x}^2 ,
\]
so \( \B^{1/2}\x = \0 \) and hence \( \B\x = \B^{1/2}(\B^{1/2}\x) = \0 \).

(b) By (a), \( \nullity\A \le \nullity\B \), and by Rank–Nullity (@thm-rank-nullity) applied to both matrices on \( F^n \), \( \rank\A = n - \nullity\A \ge n - \nullity\B = \rank\B \).

(c) \( \A = \diag(2, 2) \) and \( \B = \diag(1, 1) \): both have rank \( 2 \), \( \A - \B = \I_2 \succeq 0 \), and \( \A \ne \B \).
:::

:::: {#exr-the-loewner-order-c3}
[C3: Largest eigenvalue of a sum]

Let \( \A, \B \in M_n(F) \) be Hermitian.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \lambda_1(\A)\I \succeq \A \), and deduce \( \lambda_1(\A + \B) \le \lambda_1(\A) + \lambda_1(\B) \).
2. Deduce that if \( \A \succeq \B \), then \( 0 \le \lambda_1(\A) - \lambda_1(\B) \le \lambda_1(\A - \B) \).
:::
::::

::: {.solution}
(a) The matrix \( \lambda_1(\A)\I - \A \) is Hermitian with eigenvalues \( \lambda_1(\A) - \lambda_i(\A) \ge 0 \), so it is \( \succeq 0 \) by @thm-psd-characterizations; that is \( \lambda_1(\A)\I \succeq \A \). Adding the same inequality for \( \B \), and using that a sum of two matrices \( \succeq 0 \) is again \( \succeq 0 \) (@exr-positive-definite-matrices-c2 (a)),
\[
\big(\lambda_1(\A) + \lambda_1(\B)\big)\I \ \succeq\ \A + \B .
\]
By @thm-loewner-basic (b) applied to this pair, \( \lambda_1(\A) + \lambda_1(\B) = \lambda_1\big((\lambda_1(\A)+\lambda_1(\B))\I\big) \ge \lambda_1(\A + \B) \).

(b) Write \( \A = \B + (\A - \B) \). Applying (a) to the pair \( \B \) and \( \A - \B \),
\[
\lambda_1(\A) \le \lambda_1(\B) + \lambda_1(\A - \B) ,
\]
so \( \lambda_1(\A) - \lambda_1(\B) \le \lambda_1(\A - \B) \). For the lower bound, \( \A \succeq \B \) gives \( \lambda_1(\A) \ge \lambda_1(\B) \) by @thm-loewner-basic (b). Note that (a) itself used no order hypothesis at all; only the lower bound needs \( \A \succeq \B \).
:::
