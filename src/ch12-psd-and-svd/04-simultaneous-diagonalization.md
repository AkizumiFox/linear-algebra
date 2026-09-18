# Two Forms at Once

Chapter 11 asked when several operators can be diagonalized in one orthonormal basis, and answered: when they commute and each is normal (@thm-simultaneous-unitary-diagonalization). That theorem is about **operators**, and its currency is the unitary similarity \( \U^{*}T\U \). This section asks a question that looks similar and is not. Given two **forms** — two self-adjoint matrices, each thought of as the recipe \( \x \mapsto \x^{*}\A\x \) — can one change of variable make both of them diagonal at once? No commuting is assumed, and in general the two matrices do not commute. The price is that the change of variable is no longer unitary, and the hypothesis is that one of the two forms is positive definite.

Throughout, \( F = \nR \) or \( F = \nC \), and "self-adjoint" means \( \A^{*} = \A \) (over \( \nR \): symmetric).

## Similarity is for operators, congruence is for forms

A matrix can play two roles, and the two roles come with different change-of-variable rules.

As an **operator**, \( \A \) eats a vector and returns a vector. Rewriting \( \x = \S\y \) in the equation \( \z = \A\x \) turns it into \( \S^{-1}\z = (\S^{-1}\A\S)\y \): the new matrix is \( \S^{-1}\A\S \), and the relation is **similarity**. Eigenvalues, trace, determinant and characteristic polynomial all survive it.

As a **form**, \( \A \) eats a vector and returns the scalar \( \x^{*}\A\x \). Rewriting \( \x = \S\y \) turns that scalar into
\[
(\S\y)^{*}\A(\S\y) = \y^{*}(\S^{*}\A\S)\y ,
\]
so the new matrix is \( \S^{*}\A\S \). Two matrices \( \A \) and \( \S^{*}\A\S \) with \( \S \) invertible are called **congruent**; this is the operation of @prp-congruence-positivity, where it was already shown to preserve the sign of a form. Congruence is the right relation here for the plain reason that it is the one the question is phrased in: "make both forms diagonal" means "make both \( \x^{*}\A\x \) and \( \x^{*}\B\x \) into sums of squares in the same new coordinates", and that is a statement about \( \S^{*}\A\S \) and \( \S^{*}\B\S \). Chapter 13 studies congruence in its own right, including what it does preserve; for now, note that it certainly does **not** preserve eigenvalues, since \( \S^{*}\I\S = \S^{*}\S \) can be any positive definite matrix at all.

Congruence and similarity coincide in exactly one situation: when \( \S \) is unitary, \( \S^{*} = \S^{-1} \). That is the situation of Chapter 11, and it is what makes that chapter's theorems so strong and its hypotheses so restrictive.

::: {.warning}
**This is not Chapter 11's simultaneous diagonalization.** @thm-simultaneous-unitary-diagonalization needs the operators to **commute** and produces a **unitary** \( \U \) with every \( \U^{*}T\U \) diagonal; eigenvalues are preserved. The theorem below needs **no commuting** and one of the two matrices to be **positive definite**, and produces a merely invertible \( \S \); the eigenvalues of \( \B \) are destroyed, and even \( \A \) comes out as \( \I \). The two theorems have no common generalization: neither hypothesis implies the other. When the matrices both commute and one is positive definite, both theorems apply and give different factorizations.
:::

## Diagonalizing two forms at once

::: {#thm-simultaneous-congruence}
[Diagonalizing Two Forms by Congruence]

Let \( \A, \B \in M_n(F) \) be self-adjoint with \( \A \succ 0 \). Then there is an invertible \( \S \in M_n(F) \) with
\[
\S^{*}\A\S = \I_n \qquad\text{and}\qquad \S^{*}\B\S = \D
\]
for some **real** diagonal \( \D \). Over \( \nR \), with \( \A, \B \) symmetric, \( \S \) may be taken real.
:::

::: {.idea}
Two steps, and the first one is the whole idea. ① *Whiten.* The hypothesis \( \A \succ 0 \) gives an invertible positive definite square root \( \A^{1/2} \), and the congruence by \( \A^{-1/2} \) turns \( \A \) into \( \I \). That uses up the definiteness of \( \A \) and nothing else. ② Now \( \I \) is invariant under every **unitary** congruence, because a unitary congruence is a similarity; so we still have the whole spectral theorem available for the transformed \( \B \), and it is self-adjoint. Diagonalize it and compose the two changes of variable.
:::

::: {.proof}
Since \( \A \succ 0 \), @thm-psd-square-root gives a unique \( \A^{1/2} \succeq 0 \) with \( (\A^{1/2})^2 = \A \). Its eigenvalues are the non-negative square roots of the eigenvalues of \( \A \), which are \( > 0 \) by @thm-pd-characterizations; hence \( \A^{1/2} \succ 0 \) and in particular \( \A^{1/2} \) is invertible. Write \( \A^{-1/2} = (\A^{1/2})^{-1} \), which is again self-adjoint, since the inverse of an invertible self-adjoint matrix is self-adjoint.

Put \( \C = \A^{-1/2}\B\A^{-1/2} \). Then \( \C^{*} = \A^{-1/2}\B^{*}\A^{-1/2} = \C \), so \( \C \) is self-adjoint. By the spectral theorem for matrices there is a unitary \( \U \) and a real diagonal \( \D \) with \( \C = \U\D\U^{*} \) (@cor-spectral-complex-matrix over \( \nC \); @cor-spectral-real-matrix over \( \nR \), with \( \U \) orthogonal and real).

Set \( \S = \A^{-1/2}\U \), a product of invertible matrices, hence invertible. Then
\[
\S^{*}\A\S = \U^{*}\A^{-1/2}\A\A^{-1/2}\U = \U^{*}\U = \I_n ,
\]
where the middle equality uses \( \A^{-1/2}\A\A^{-1/2} = \A^{-1/2}\A^{1/2}\A^{1/2}\A^{-1/2} = \I_n \). And
\[
\S^{*}\B\S = \U^{*}\A^{-1/2}\B\A^{-1/2}\U = \U^{*}\C\U = \D .
\]
Over \( \nR \) every matrix named here is real: \( \A^{1/2} \) is real because it is a polynomial in \( \A \) (@thm-psd-square-root), and \( \U \) is real by @cor-spectral-real-matrix. This proves the theorem.
:::

The theorem says more than "both become diagonal": the definite one becomes the **identity**, which is the strongest normalization available, and it costs nothing extra. Note also which hypothesis did which job. Definiteness of \( \A \) was used exactly once, to invert \( \A^{1/2} \). Self-adjointness of \( \B \) was used exactly once, to apply the spectral theorem to \( \C \). Nothing at all was assumed about \( \A\B \) versus \( \B\A \).

::: {.check}
Why can \( \S \) not be taken unitary in @thm-simultaneous-congruence?
:::

::: {.solution}
A unitary \( \S \) has \( \S^{*} = \S^{-1} \), so \( \S^{*}\A\S = \I \) would give \( \A = \S\I\S^{*} = \I \). So a unitary \( \S \) can only work when \( \A \) is already the identity — and then the theorem is just the spectral theorem for \( \B \).
:::

## The generalized eigenvalue problem

The matrix \( \S \) of the theorem is not an abstract object: its columns solve an eigenvalue problem in which the identity has been replaced by \( \A \).

::: {#def-generalized-eigenvalue}
[Generalized eigenvalue]

Let \( \A, \B \in M_n(F) \). A scalar \( \lambda \in F \) is a **generalized eigenvalue** of the **pair** \( (\A, \B) \) if
\[
\B\x = \lambda\A\x \qquad \text{for some } \x \ne \0 ,
\]
and such an \( \x \) is a **generalized eigenvector** for \( \lambda \). The family of matrices \( \B - \lambda\A \) is called the **pencil** of the pair.
:::

Taking \( \A = \I \) recovers @def-eigenvalue, so the word "generalized" is honest. The condition \( \B\x = \lambda\A\x \) with \( \x \ne \0 \) says that \( \B - \lambda\A \) is singular, that is \( \det(\B - \lambda\A) = 0 \); so the generalized eigenvalues are the roots of the polynomial \( \det(\B - \lambda\A) \) in \( \lambda \), the **characteristic polynomial of the pencil**. Its degree is at most \( n \), and exactly \( n \) when \( \A \) is invertible, since the \( \lambda^n \)-coefficient is \( (-1)^n\det\A \). When \( \A \) is singular the degree can drop, and the polynomial can even be a non-zero constant, in which case the pair has no generalized eigenvalues at all; exercise C3 below is such a pair. From here on \( \A \succ 0 \), so this does not arise.

Nothing so far forces those roots to be real: for \( \A = \I \) they are just eigenvalues, and a general \( \B \) has complex ones. Self-adjointness of \( \B \) alone is not enough either, as the warning at the end of this section shows. It is definiteness of \( \A \) that makes the problem behave.

:::: {#thm-generalized-eigenvalues-real}
[The Definite Generalized Eigenvalue Problem]

Let \( \A, \B \in M_n(F) \) be self-adjoint with \( \A \succ 0 \), and let \( \S \) and \( \D = \diag(d_1, \dots, d_n) \) be as in @thm-simultaneous-congruence, with columns \( \s_1, \dots, \s_n \) of \( \S \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \B\s_i = d_i\A\s_i \) for every \( i \), and \( \s_i^{*}\A\s_j = \delta_{ij} \): the columns of \( \S \) are a basis of \( F^n \) of generalized eigenvectors, orthonormal for the inner product \( \inner{\x}{\y}_{\A} = \y^{*}\A\x \);
2. the generalized eigenvalues of \( (\A, \B) \) are exactly \( d_1, \dots, d_n \), all **real**, and
\[
\det(\B - \lambda\A) = \frac{1}{\lvert\det\S\rvert^{2}}\prod_{i=1}^{n}(d_i - \lambda) ;
\]
3. \( \A^{-1}\B = \S\D\S^{-1} \); in particular \( \A^{-1}\B \) is diagonalizable with real eigenvalues \( d_1, \dots, d_n \), although it need not be self-adjoint.
:::
::::

::: {.idea}
Everything is already in the two equations \( \S^{*}\A\S = \I \) and \( \S^{*}\B\S = \D \). Substituting the first into the second turns \( \D \) into \( \S^{*}\A\S\D \), and canceling the invertible \( \S^{*} \) leaves \( \B\S = \A\S\D \), which read column by column is (a). Then (b) and (c) are two ways of undoing the substitution.
:::

::: {.proof}
(a) From \( \S^{*}\A\S = \I \) we get \( \D = \I\D = \S^{*}\A\S\D \), and also \( \D = \S^{*}\B\S \). Therefore \( \S^{*}(\B\S - \A\S\D) = \0 \), and \( \S^{*} \) is invertible, so
\[
\B\S = \A\S\D .
\]
Column \( i \) of the left side is \( \B\s_i \) and of the right side is \( d_i\A\s_i \), since \( \D \) is diagonal. Each \( \s_i \neq \0 \) because \( \S \) is invertible, so each \( d_i \) is a generalized eigenvalue with eigenvector \( \s_i \). The entry \( (i, j) \) of \( \S^{*}\A\S = \I \) is \( \s_i^{*}\A\s_j \), which is therefore \( \delta_{ij} \). Finally \( \inner{\x}{\y}_{\A} = \y^{*}\A\x \) is an inner product on \( F^n \), exactly because \( \A \succ 0 \): it is sesquilinear, \( \conj{\inner{\y}{\x}_{\A}} = \conj{\x^{*}\A\y} = \y^{*}\A^{*}\x = \inner{\x}{\y}_{\A} \), and \( \inner{\x}{\x}_{\A} = \x^{*}\A\x > 0 \) for \( \x \ne \0 \).

(b) From \( \S^{*}\A\S = \I \) and \( \S^{*}\B\S = \D \) we get \( \A = (\S^{*})^{-1}\S^{-1} \) and \( \B = (\S^{*})^{-1}\D\S^{-1} \), hence
\[
\B - \lambda\A = (\S^{*})^{-1}(\D - \lambda\I)\S^{-1} .
\]
Taking determinants with @thm-det-multiplicative, and using \( \det(\S^{*}) = \conj{\det\S} \),
\[
\det(\B - \lambda\A) = \frac{\det(\D - \lambda\I)}{\conj{\det\S}\,\det\S} = \frac{1}{\lvert\det\S\rvert^{2}}\prod_{i}(d_i - \lambda) ,
\]
the last step by @thm-det-triangular. Since \( \lvert\det\S\rvert^2 \neq 0 \), the roots of \( \det(\B - \lambda\A) \) are exactly \( d_1, \dots, d_n \); and \( \lambda \) is a generalized eigenvalue if and only if \( \B - \lambda\A \) is singular, that is if and only if \( \det(\B - \lambda\A) = 0 \) (@thm-invertible-tfae). The \( d_i \) are real because \( \D = \S^{*}\B\S \) is self-adjoint, so its diagonal entries equal their own conjugates.

(c) Inverting \( \A = (\S^{*})^{-1}\S^{-1} \) gives \( \A^{-1} = \S\S^{*} \), so
\[
\A^{-1}\B = \S\S^{*}(\S^{*})^{-1}\D\S^{-1} = \S\D\S^{-1} .
\]
This proves the theorem.
:::

Part (c) explains the phenomenon. The matrix \( \A^{-1}\B \) is what one would naively form to turn \( \B\x = \lambda\A\x \) into an ordinary eigenvalue problem, and it is usually not self-adjoint, so there is no reason from Chapter 11 for its eigenvalues to be real. But it **is** self-adjoint with respect to the inner product \( \inner{\cdot}{\cdot}_{\A} \), and reality and the orthogonal eigenbasis come from that inner product rather than the standard one. The congruence \( \S \) is exactly the change of variable that turns \( \inner{\cdot}{\cdot}_{\A} \) into the standard inner product.

:::: {#exm-generalized-eigenproblem-2x2}
[A pencil that does not commute]

Let
\[
\A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}, \qquad
\B = \begin{pmatrix} 0 & 3 \\ 3 & 6 \end{pmatrix} .
\]
Check that \( \A \succ 0 \), that \( \A\B \ne \B\A \), and that \( \B \) is indefinite. Find the generalized eigenvalues and an \( \A \)-orthonormal basis of generalized eigenvectors, and write down \( \S \).
::::

::: {.solution}
*Setting up.* \( \A \) is symmetric with leading principal minors \( 2 > 0 \) and \( 4 - 1 = 3 > 0 \), so \( \A \succ 0 \) by @thm-pd-characterizations. Its own eigenvalues are \( 1 \) and \( 3 \). The products are
\[
\A\B = \begin{pmatrix} 3 & 12 \\ 6 & 15 \end{pmatrix}, \qquad
\B\A = \begin{pmatrix} 3 & 6 \\ 12 & 15 \end{pmatrix},
\]
which differ, so Chapter 11's theorem does not apply. Also \( \det\B = -9 < 0 \), so \( \B \) has one positive and one negative eigenvalue and is neither positive nor negative semidefinite.

*The pencil.* 
\[
\B - \lambda\A = \begin{pmatrix} -2\lambda & 3 - \lambda \\ 3 - \lambda & 6 - 2\lambda \end{pmatrix},
\]
so
\[
\begin{aligned}
\det(\B - \lambda\A) &= -2\lambda(6 - 2\lambda) - (3 - \lambda)^2 \\
&= 4\lambda^2 - 12\lambda - 9 + 6\lambda - \lambda^2 \\
&= 3\lambda^2 - 6\lambda - 9 = 3(\lambda - 3)(\lambda + 1) .
\end{aligned}
\]
The generalized eigenvalues are \( \lambda = -1 \) and \( \lambda = 3 \), both real, as @thm-generalized-eigenvalues-real (b) promises.

*Eigenvectors.* For \( \lambda = -1 \), \( \B + \A = \begin{pmatrix} 2 & 4 \\ 4 & 8 \end{pmatrix} \), whose kernel is spanned by \( \x_1 = (2, -1) \). For \( \lambda = 3 \), \( \B - 3\A = \begin{pmatrix} -6 & 0 \\ 0 & 0 \end{pmatrix} \), whose kernel is spanned by \( \x_2 = (0, 1) \). Checking directly: \( \B\x_1 = (-3, 0) \) and \( \A\x_1 = (3, 0) \), so \( \B\x_1 = -\A\x_1 \); and \( \B\x_2 = (3, 6) = 3(1, 2) = 3\A\x_2 \).

*Normalizing.* \( \x_1\tp\A\x_1 = (2, -1)\cdot(3, 0) = 6 \) and \( \x_2\tp\A\x_2 = (0,1)\cdot(1,2) = 2 \), while \( \x_1\tp\A\x_2 = (2,-1)\cdot(1,2) = 0 \): the two are already \( \A \)-orthogonal, as they must be, having different generalized eigenvalues. Scaling to \( \A \)-length \( 1 \),
\[
\S = \begin{pmatrix} 2/\sqrt6 & 0 \\ -1/\sqrt6 & 1/\sqrt2 \end{pmatrix},
\qquad
\S\tp\A\S = \I_2, \qquad \S\tp\B\S = \begin{pmatrix} -1 & 0 \\ 0 & 3 \end{pmatrix} .
\]
So in the coordinates \( \x = \S\y \) the two forms read \( \x\tp\A\x = y_1^2 + y_2^2 \) and \( \x\tp\B\x = -y_1^2 + 3y_2^2 \). The signs \( (-, +) \) match the signs of the eigenvalues of \( \B \) itself, which are \( 3 \pm 3\sqrt2 \); Chapter 13 shows that this is no coincidence.
:::

The problem \( \B\x = \lambda\A\x \) with \( \A \succ 0 \) is the one an engineer meets first: for a vibrating structure, \( \A \) is the mass matrix and \( \B \) the stiffness matrix, the generalized eigenvalues are the squared natural frequencies, and the \( \A \)-orthonormal eigenvectors are the normal modes, in which the motion decouples into independent one-dimensional oscillations.

## When neither form is definite

Definiteness of one of the two matrices is not decoration.

::: {.warning}
**Two self-adjoint matrices, neither definite, need not be simultaneously diagonalizable by congruence.** Take the real symmetric pair
\[
\A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \qquad
\B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} .
\]
Suppose \( \S\tp\A\S \) and \( \S\tp\B\S \) were both diagonal for some invertible real \( \S \), say \( \D_{\A} \) and \( \D_{\B} \). Since \( \A \) is invertible, so is \( \D_{\A} \), and from \( \A = (\S\tp)^{-1}\D_{\A}\S^{-1} \) and \( \B = (\S\tp)^{-1}\D_{\B}\S^{-1} \) we get
\[
\A^{-1}\B = \S\D_{\A}^{-1}\S\tp(\S\tp)^{-1}\D_{\B}\S^{-1} = \S\big(\D_{\A}^{-1}\D_{\B}\big)\S^{-1} ,
\]
so \( \A^{-1}\B \) would be similar to a real diagonal matrix and would have real eigenvalues. But \( \A^{-1} = \A \) here, and
\[
\A^{-1}\B = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}
\]
has characteristic polynomial \( \lambda^2 + 1 \), with roots \( \pm i \). So no such \( \S \) exists — and the pencil has **no** generalized eigenvalues in \( \nR \) at all.
:::

The obstruction in the warning is exactly the failure of part (c) of @thm-generalized-eigenvalues-real. That part is in fact the right way to test a pair: if \( \A \) is invertible, a necessary condition for simultaneous diagonalization by congruence is that \( \A^{-1}\B \) be diagonalizable with real eigenvalues, and the theorem says that \( \A \succ 0 \) is enough to guarantee it.

## Exercises

### A. Check your understanding

:::: {#exr-simultaneous-diagonalization-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define what it means for two matrices to be **congruent**, and say which of similarity and congruence is the natural relation for a form.
2. State @thm-simultaneous-congruence, with all hypotheses.
3. Name two differences between @thm-simultaneous-congruence and @thm-simultaneous-unitary-diagonalization.
4. Determine whether the following statement is correct, and justify your answer: the generalized eigenvalues of \( (\A, \B) \) are eigenvalues of \( \B \).
5. For \( \A \succ 0 \) and \( \B \) self-adjoint, what inner product makes \( \A^{-1}\B \) self-adjoint?
:::
::::

::: {.solution}
(a) \( \A \) and \( \C \) are congruent if \( \C = \S^{*}\A\S \) for some invertible \( \S \). Congruence is the natural relation for a form, since the substitution \( \x = \S\y \) turns \( \x^{*}\A\x \) into \( \y^{*}(\S^{*}\A\S)\y \); similarity \( \S^{-1}\A\S \) is the natural relation for an operator.

(b) If \( \A, \B \in M_n(F) \) are self-adjoint and \( \A \succ 0 \), there is an invertible \( \S \) with \( \S^{*}\A\S = \I_n \) and \( \S^{*}\B\S \) real diagonal.

(c) Chapter 11's theorem assumes the operators commute and are normal, and delivers a **unitary** change of basis preserving eigenvalues; this one assumes nothing about commuting but assumes one matrix is positive definite, and delivers a merely invertible \( \S \) under which eigenvalues are not preserved.

(d) Incorrect. In @exm-generalized-eigenproblem-2x2 the generalized eigenvalues are \( -1 \) and \( 3 \), while the eigenvalues of \( \B \) are \( 3 \pm 3\sqrt2 \). They agree when \( \A = \I \), and not in general.

(e) \( \inner{\x}{\y}_{\A} = \y^{*}\A\x \) (@thm-generalized-eigenvalues-real (a)).
:::

### B. Practice

:::: {#exr-simultaneous-diagonalization-b1}
[B1: A generalized eigenvalue problem]

Let
\[
\A = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}, \qquad
\B = \begin{pmatrix} 2 & 2 \\ 2 & 1 \end{pmatrix} .
\]

::: {.enumerate options="label=(\alph*)"}
1. Verify that \( \A \succ 0 \) and find the generalized eigenvalues of \( (\A, \B) \).
2. Find generalized eigenvectors and an invertible \( \S \) with \( \S\tp\A\S = \I_2 \) and \( \S\tp\B\S \) diagonal.
:::
::::

::: {.solution}
(a) The leading principal minors of \( \A \) are \( 1 > 0 \) and \( 2 - 1 = 1 > 0 \), so \( \A \succ 0 \) by @thm-pd-characterizations. Then
\[
\B - \lambda\A = \begin{pmatrix} 2 - \lambda & 2 - \lambda \\ 2 - \lambda & 1 - 2\lambda \end{pmatrix},
\]
so
\[
\begin{aligned}
\det(\B - \lambda\A) &= (2-\lambda)(1-2\lambda) - (2-\lambda)^2 \\
&= (2-\lambda)\big[(1 - 2\lambda) - (2 - \lambda)\big] \\
&= (2 - \lambda)(-1 - \lambda) = (\lambda - 2)(\lambda + 1) .
\end{aligned}
\]
The generalized eigenvalues are \( 2 \) and \( -1 \).

(b) For \( \lambda = 2 \): \( \B - 2\A = \begin{pmatrix} 0 & 0 \\ 0 & -3 \end{pmatrix} \), with kernel spanned by \( \x_1 = (1, 0) \). For \( \lambda = -1 \): \( \B + \A = \begin{pmatrix} 3 & 3 \\ 3 & 3 \end{pmatrix} \), with kernel spanned by \( \x_2 = (1, -1) \). Check: \( \B\x_1 = (2,2) = 2\A\x_1 \) since \( \A\x_1 = (1,1) \); and \( \B\x_2 = (0, 1) \) while \( \A\x_2 = (0, -1) \), so \( \B\x_2 = -\A\x_2 \).

Now \( \x_1\tp\A\x_1 = (1,0)\cdot(1,1) = 1 \) and \( \x_2\tp\A\x_2 = (1,-1)\cdot(0,-1) = 1 \), and \( \x_1\tp\A\x_2 = (1,0)\cdot(0,-1) = 0 \). Both are already \( \A \)-unit vectors, so
\[
\S = \begin{pmatrix} 1 & 1 \\ 0 & -1 \end{pmatrix}, \qquad
\S\tp\A\S = \I_2, \qquad
\S\tp\B\S = \begin{pmatrix} 2 & 0 \\ 0 & -1 \end{pmatrix} .
\]
:::

:::: {#exr-simultaneous-diagonalization-b2}
[B2: Whitening by hand]

Let \( \A = \diag(4, 9) \) and \( \B = \begin{pmatrix} 4 & 6 \\ 6 & 9 \end{pmatrix} \). Follow the two steps of the proof of @thm-simultaneous-congruence: compute \( \A^{-1/2} \), then \( \C = \A^{-1/2}\B\A^{-1/2} \), diagonalize \( \C \), and write down \( \S \) and \( \S\tp\B\S \).
::::

::: {.solution}
\( \A \) is diagonal with positive entries, so \( \A^{1/2} = \diag(2, 3) \) and \( \A^{-1/2} = \diag(\tfrac12, \tfrac13) \). Then
\[
\C = \begin{pmatrix} \tfrac12 & 0 \\ 0 & \tfrac13 \end{pmatrix}
\begin{pmatrix} 4 & 6 \\ 6 & 9 \end{pmatrix}
\begin{pmatrix} \tfrac12 & 0 \\ 0 & \tfrac13 \end{pmatrix}
= \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} .
\]
Its eigenvalues are \( 2 \), with unit eigenvector \( \tfrac{1}{\sqrt2}(1,1) \), and \( 0 \), with unit eigenvector \( \tfrac{1}{\sqrt2}(1,-1) \). So \( \U = \tfrac{1}{\sqrt2}\begin{pmatrix} 1 & 1 \\ 1 & -1\end{pmatrix} \) and \( \D = \diag(2, 0) \), and
\[
\S = \A^{-1/2}\U = \frac{1}{\sqrt2}\begin{pmatrix} \tfrac12 & \tfrac12 \\[2pt] \tfrac13 & -\tfrac13 \end{pmatrix},
\qquad \S\tp\A\S = \I_2, \qquad \S\tp\B\S = \begin{pmatrix} 2 & 0 \\ 0 & 0 \end{pmatrix} .
\]
As a check, \( \det(\B - \lambda\A) = (4 - 4\lambda)(9 - 9\lambda) - 36 = 36\lambda^2 - 72\lambda = 36\lambda(\lambda - 2) \), whose roots \( 0 \) and \( 2 \) are the diagonal entries of \( \S\tp\B\S \).
:::

:::: {#exr-simultaneous-diagonalization-b3}
[B3: A pair that resists]

Let \( \A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) and \( \B = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \). Determine whether there is an invertible real \( \S \) making \( \S\tp\A\S \) and \( \S\tp\B\S \) both diagonal. Justify your answer.
::::

::: {.solution}
There is not. Both matrices are symmetric and \( \A \) is invertible, with \( \A^{-1} = \A \). If such an \( \S \) existed, the computation in the warning above would give \( \A^{-1}\B = \S(\D_{\A}^{-1}\D_{\B})\S^{-1} \), so \( \A^{-1}\B \) would be diagonalizable. But
\[
\A^{-1}\B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix},
\]
which is non-zero with \( (\A^{-1}\B)^2 = \0 \), hence has \( 0 \) as its only eigenvalue and is not diagonalizable (a diagonalizable matrix with only the eigenvalue \( 0 \) is \( \0 \)). Here the generalized eigenvalues are both \( 0 \) and real, so reality of the spectrum is not the obstruction; diagonalizability is.
:::

### C. Going deeper

:::: {#exr-simultaneous-diagonalization-c1}
[C1: The \( \A \)-inner product]

Let \( \A \succ 0 \) and \( \B \) be self-adjoint in \( M_n(F) \), and write \( \inner{\x}{\y}_{\A} = \y^{*}\A\x \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \inner{\cdot}{\cdot}_{\A} \) is an inner product on \( F^n \).
2. Prove that \( T = T_{\A^{-1}\B} \) is self-adjoint on \( (F^n, \inner{\cdot}{\cdot}_{\A}) \).
3. Deduce @thm-generalized-eigenvalues-real (a) and (b) from the spectral theorem applied to \( T \), without using @thm-simultaneous-congruence.
:::
::::

::: {.solution}
(a) Sesquilinearity in the first slot is clear from the formula. Conjugate symmetry: \( \conj{\inner{\y}{\x}_{\A}} = \conj{\x^{*}\A\y} = \y^{*}\A^{*}\x = \y^{*}\A\x = \inner{\x}{\y}_{\A} \), using \( \A^{*} = \A \). Positive definiteness: \( \inner{\x}{\x}_{\A} = \x^{*}\A\x > 0 \) for \( \x \ne \0 \), which is @def-positive-semidefinite for \( \A \succ 0 \).

(b) For all \( \x, \y \),
\[
\inner{T\x}{\y}_{\A} = \y^{*}\A\A^{-1}\B\x = \y^{*}\B\x ,
\]
and
\[
\inner{\x}{T\y}_{\A} = (\A^{-1}\B\y)^{*}\A\x = \y^{*}\B^{*}\A^{-1}\A\x = \y^{*}\B\x ,
\]
using \( (\A^{-1})^{*} = \A^{-1} \) and \( \B^{*} = \B \). The two agree, so \( T \) is self-adjoint for this inner product (@def-adjoint).

(c) By @thm-spectral-real (over \( \nR \)) or @thm-spectral-complex (over \( \nC \)) applied to the self-adjoint \( T \) on the inner product space \( (F^n, \inner{\cdot}{\cdot}_{\A}) \), there is a basis \( \s_1, \dots, \s_n \) of \( F^n \), orthonormal for \( \inner{\cdot}{\cdot}_{\A} \), with \( T\s_i = d_i\s_i \) and \( d_i \in \nR \) (@thm-self-adjoint-real-eigenvalues). The equation \( \A^{-1}\B\s_i = d_i\s_i \) is \( \B\s_i = d_i\A\s_i \), and \( \s_i^{*}\A\s_j = \inner{\s_j}{\s_i}_{\A} = \delta_{ij} \); this is (a). For (b), \( \lambda \) is a generalized eigenvalue exactly when \( \A^{-1}\B - \lambda\I \) is singular, that is when \( \lambda \) is an eigenvalue of \( \A^{-1}\B \), and those are \( d_1, \dots, d_n \).
:::

:::: {#exr-simultaneous-diagonalization-c2}
[C2: Signs of the generalized eigenvalues]

Let \( \A \succ 0 \) and \( \B \) be self-adjoint in \( M_n(F) \), with generalized eigenvalues \( d_1, \dots, d_n \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \B \succeq 0 \) if and only if every \( d_i \ge 0 \), and \( \B \succ 0 \) if and only if every \( d_i > 0 \).
2. Deduce that if \( \A \succ 0 \) and \( \B \succ 0 \), then \( \det\B/\det\A = \prod_i d_i > 0 \).
:::
::::

::: {.solution}
(a) Let \( \S \) be as in @thm-simultaneous-congruence, so \( \S^{*}\B\S = \D = \diag(d_1, \dots, d_n) \). For \( \x \in F^n \) put \( \y = \S^{-1}\x \); as \( \x \) runs over \( F^n \) so does \( \y \), and \( \x \ne \0 \) exactly when \( \y \ne \0 \). Then
\[
\x^{*}\B\x = \y^{*}\S^{*}\B\S\y = \y^{*}\D\y = \sum_{i} d_i\lvert y_i\rvert^2 .
\]
If every \( d_i \ge 0 \), this is \( \ge 0 \) for all \( \y \), so \( \B \succeq 0 \). Conversely, taking \( \y = \e_i \) gives \( d_i \ge 0 \). The same argument with strict inequalities gives the second claim, using that \( \sum_i d_i\lvert y_i\rvert^2 > 0 \) for \( \y \ne \0 \) when every \( d_i > 0 \).

(b) Taking determinants in \( \S^{*}\B\S = \D \) and \( \S^{*}\A\S = \I \) gives \( \lvert\det\S\rvert^2\det\B = \prod_i d_i \) and \( \lvert\det\S\rvert^2\det\A = 1 \). Dividing, \( \det\B/\det\A = \prod_i d_i \), which is \( > 0 \) by (a).
:::

:::: {#exr-simultaneous-diagonalization-c3}
[C3: Dropping definiteness of \( \A \)]

Let \( \A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \) and \( \B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \), so that \( \A \succeq 0 \) but \( \A \not\succ 0 \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \det(\B - \lambda\A) \) and deduce that the pair has no generalized eigenvalues at all.
2. Prove that no invertible \( \S \in M_2(\nR) \) makes \( \S\tp\A\S \) and \( \S\tp\B\S \) both diagonal.
:::

*Hint for (b): compare the degree in \( \lambda \) of \( \det(\B - \lambda\A) \) on both sides.*
::::

::: {.solution}
(a) \( \B - \lambda\A = \begin{pmatrix} -\lambda & 1 \\ 1 & 0 \end{pmatrix} \), with determinant \( -1 \). This is never \( 0 \), so \( \B - \lambda\A \) is invertible for every \( \lambda \) and there is no \( \x \ne \0 \) with \( \B\x = \lambda\A\x \).

(b) Suppose \( \S\tp\A\S = \diag(a_1, a_2) \) and \( \S\tp\B\S = \diag(b_1, b_2) \). As in the proof of @thm-generalized-eigenvalues-real (b),
\[
\det(\B - \lambda\A) = \frac{1}{(\det\S)^{2}}(b_1 - \lambda a_1)(b_2 - \lambda a_2) .
\]
By (a) the left side is the constant \( -1 \), so the right side is a non-zero constant. It is non-zero, so \( b_1b_2 \ne 0 \) and hence \( \det(\S\tp\B\S) \ne 0 \); it is constant in \( \lambda \), so \( a_1 = a_2 = 0 \), which forces \( \S\tp\A\S = \0 \) and therefore \( \A = \0 \). That is false, so no such \( \S \) exists. (Alternatively: \( \rank(\S\tp\A\S) = \rank\A = 1 \), so exactly one \( a_i \) is non-zero, and the right side then has degree \( 1 \) in \( \lambda \), not \( 0 \).)
:::
