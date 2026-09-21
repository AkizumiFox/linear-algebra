# Steepest Descent and Conjugate Gradients

Section 2 solved \( \A\x = \b \) by elimination: about \( \tfrac23 n^3 \) operations, an exact answer after finitely many of them, and a factorization that fills in most of the zeros the matrix had. For a large sparse matrix that is the wrong bargain. This section builds two iterations that touch \( \A \) only through the product \( \x \mapsto \A\x \), for the case where \( \A \) is positive definite, and counts what each of them buys. The first costs about \( \kappa \) steps per decimal digit of accuracy, the second about \( \sqrt{\kappa} \). Where that square root comes from is the point of the section.

**Throughout, \( \A \in M_n(\nR) \) is symmetric and positive definite, \( \b \in \nR^n \), and \( \x^{\star} = \A^{-1}\b \) is the exact solution.** Iteration indices are superscripts in parentheses. We work over \( \nR \) because the function this section minimizes is built from \( \b\tp\x \), which over \( \nC \) is not a real number; everything below survives over \( \nC \) with \( \b^{*}\x \) replaced by its real part, and nothing else changes.

## A linear system is a minimization problem

Positive definiteness is a statement about the number \( \x\tp\A\x \) (@def-positive-semidefinite), so it invites us to look for a *quantity* that the solution makes small, rather than an equation the solution satisfies. There is one, and it is the simplest possible candidate: a quadratic minus a linear term.

*Solving \( \A\x = \b \) is the same as sitting at the bottom of a bowl.*

::: {#def-energy-norm}
[The Energy Inner Product and the Energy Norm]

Let \( \A \in M_n(\nR) \) be symmetric positive definite. The **energy inner product** is
\[
\inner{\x}{\y}_{\A} \coloneqq \y\tp\A\x \qquad (\x, \y \in \nR^n),
\]
and the **energy norm** is \( \norm{\x}_{\A} \coloneqq \inner{\x}{\x}_{\A}^{1/2} = (\x\tp\A\x)^{1/2} \). Two vectors are **\( \A \)-orthogonal**, or **conjugate**, when \( \inner{\x}{\y}_{\A} = 0 \).
:::

This is the inner product of Chapter 12 §04, written there as \( \y^{*}\A\x \). It really is one: it is bilinear because matrix multiplication is; it is symmetric because the \( 1 \times 1 \) matrix \( \y\tp\A\x \) equals its own transpose \( \x\tp\A\y \); and \( \inner{\x}{\x}_{\A} > 0 \) for \( \x \ne \0 \) is clause (P2) of @def-positive-semidefinite in its strict form. So \( \norm{\cdot}_{\A} \) is the induced norm of @def-induced-norm, and every fact about norms and orthogonality from Chapter 10 applies verbatim. That is the reason for introducing it: it lets us reuse the Pythagorean theorem in a geometry bent by \( \A \).

The word *energy* comes from the springs of Section 9, where \( \tfrac12\x\tp\K\x \) is the potential energy stored in a displacement \( \x \).

::: {#prp-quadratic-minimizer}
[The Solution Minimizes the Energy Functional]

Let \( \A \in M_n(\nR) \) be symmetric positive definite, \( \b \in \nR^n \), and define
\[
\phi(\x) \coloneqq \tfrac12\,\x\tp\A\x - \b\tp\x \qquad (\x \in \nR^n).
\]
Then, with \( \x^{\star} = \A^{-1}\b \),
\[
\phi(\x) - \phi(\x^{\star}) = \tfrac12\norm{\x - \x^{\star}}_{\A}^{2}
\qquad \text{for every } \x \in \nR^n .
\]
In particular \( \x^{\star} \) is the **unique** minimizer of \( \phi \).
:::

::: {.proof}
\( \A \) is invertible, since \( \A \succ 0 \) has only positive eigenvalues (@thm-pd-characterizations, (a) \( \Rightarrow \) (b)), so \( \x^{\star} \) is defined and \( \A\x^{\star} = \b \). Expand, using \( \A\tp = \A \):
\[
\begin{aligned}
\tfrac12\norm{\x - \x^{\star}}_{\A}^{2}
&= \tfrac12\x\tp\A\x - \x\tp\A\x^{\star} + \tfrac12(\x^{\star})\tp\A\x^{\star}\\
&= \tfrac12\x\tp\A\x - \b\tp\x + \tfrac12\,\b\tp\x^{\star} ,
\end{aligned}
\]
where the second line uses \( \A\x^{\star} = \b \) twice and \( \x\tp\b = \b\tp\x \). The first two terms are \( \phi(\x) \). Putting \( \x = \x^{\star} \) gives \( 0 = \phi(\x^{\star}) + \tfrac12\b\tp\x^{\star} \), so the leftover constant is \( -\phi(\x^{\star}) \), which is the identity. Since \( \norm{\cdot}_{\A} \) is a norm, the right-hand side is \( \ge 0 \) with equality only at \( \x = \x^{\star} \). This proves the proposition.
:::

So every iteration below may be read twice: as an attempt to solve a linear system, and as an attempt to walk downhill on a bowl whose shape is \( \A \). The identity also tells us which error to measure. The natural yardstick is not \( \norm{\x - \x^{\star}}_2 \) but \( \norm{\x - \x^{\star}}_{\A} \), because that is the one the algorithms actually make small.

Two quantities recur. The **error** is \( \boldsymbol{\varepsilon} = \x - \x^{\star} \) and the **residual** is \( \r = \b - \A\x \), and they are related by
\[
\r = \b - \A\x = \A\x^{\star} - \A\x = -\A\boldsymbol{\varepsilon} .
\]{#eq-residual-error}
The residual is computable and the error is not; @eq-residual-error is the exchange rate between them.

## Steepest descent

Fix \( \x \) and a direction \( \d \ne \0 \), and ask what happens along the line \( \x + t\d \). Expanding \( \phi \) and using \( \A\tp = \A \),
\[
\phi(\x + t\d) = \phi(\x) - t\,\d\tp\r + \tfrac12 t^2\,\d\tp\A\d ,
\]{#eq-line-search}
where \( \r = \b - \A\x \). Since \( \d\tp\A\d > 0 \), the right-hand side is a parabola in \( t \) opening upwards, so it has one minimum, at

\[
t = \frac{\d\tp\r}{\d\tp\A\d},
\qquad\text{with decrease}\quad
\frac{(\d\tp\r)^2}{2\,\d\tp\A\d} .
\]{#eq-exact-line-search}

Choosing \( t \) this way is an **exact line search**; it costs one product \( \A\d \).

Which \( \d \) should we take? Read @eq-line-search for small \( t \): the decrease is \( t\,\d\tp\r \) to first order, and among unit vectors \( \d \) the quantity \( \d\tp\r \) is largest exactly at \( \d = \r/\norm{\r}_2 \), by Cauchy--Schwarz (@thm-cauchy-schwarz) with its equality case. So the residual is the direction in which \( \phi \) falls fastest *at the starting point*, measured in the ordinary Euclidean norm.

::: {.warning}
**"Steepest" is a statement about the first instant, not about the step.** The direction that minimizes \( \phi \) over the whole line is not \( \r \) but \( \A^{-1}\r \): with \( \d = \A^{-1}\r \), @eq-exact-line-search gives \( t = 1 \) and \( \x + \d = \x + \A^{-1}(\b - \A\x) = \x^{\star} \), the exact answer in one step. That direction is unavailable, because producing it means solving the very system we are trying to solve. Every method in this section is an attempt to approximate \( \A^{-1}\r \) cheaply.
:::

::: {#def-steepest-descent}
[Steepest Descent]

Let \( \A \succ 0 \) and \( \b \in \nR^n \), and let \( \x^{(0)} \in \nR^n \). **Steepest descent** is the iteration: for \( k = 0, 1, 2, \dots \), set \( \r^{(k)} = \b - \A\x^{(k)} \); if \( \r^{(k)} = \0 \), stop, since \( \x^{(k)} = \x^{\star} \); otherwise put
\[
t_k = \frac{(\r^{(k)})\tp\r^{(k)}}{(\r^{(k)})\tp\A\r^{(k)}},
\qquad
\x^{(k+1)} = \x^{(k)} + t_k\,\r^{(k)} .
\]
:::

The denominator is positive because \( \r^{(k)} \ne \0 \) and \( \A \succ 0 \), so \( t_k \) is defined, and \( t_k > 0 \). One step costs one matrix--vector product.

To see how fast this is we need one inequality, and it is a statement about weighted averages, not about matrices at all.

::: {#lem-kantorovich}
[Kantorovich's Inequality]

Let \( \A \in M_n(\nR) \) be symmetric positive definite with eigenvalues \( \lambda_1 \ge \dots \ge \lambda_n > 0 \). Then for every \( \y \in \nR^n \),
\[
(\y\tp\A\y)(\y\tp\A^{-1}\y) \le \frac{(\lambda_1 + \lambda_n)^2}{4\lambda_1\lambda_n}\,(\y\tp\y)^2 .
\]
:::

::: {.idea}
In an orthonormal eigenbasis both factors become weighted averages of the eigenvalues, one of \( \lambda \) and one of \( 1/\lambda \), with the same weights. The obstacle is that \( 1/\lambda \) is not linear, so the second average is not determined by the first. It is, however, *bounded* by it: on the interval \( [\lambda_n, \lambda_1] \) the curve \( 1/\lambda \) lies below the straight line joining its endpoints. Replacing the curve by that line makes the second average a linear function of the first, and the product becomes a scalar quadratic that we maximize by hand.
:::

::: {.proof}
Write \( a = \lambda_1 \) and \( c = \lambda_n \). For every \( \lambda \) with \( c \le \lambda \le a \),
\[
\frac{a + c - \lambda}{ac} - \frac{1}{\lambda}
= \frac{\lambda(a + c - \lambda) - ac}{ac\lambda}
= \frac{-(\lambda - a)(\lambda - c)}{ac\lambda} \ \ge\ 0 ,
\tag{$\ast$}
\]
because \( \lambda - a \le 0 \), \( \lambda - c \ge 0 \) and \( ac\lambda > 0 \).

We may assume \( \y \ne \0 \), the case \( \y = \0 \) being an equality \( 0 = 0 \), and by homogeneity (both sides scale by \( s^4 \) under \( \y \mapsto s\y \)) we may assume \( \y\tp\y = 1 \). By the spectral theorem (@cor-spectral-real-matrix) there is an orthonormal basis \( \q_1, \dots, \q_n \) of \( \nR^n \) with \( \A\q_i = \lambda_i\q_i \). Let \( u_i = \q_i\tp\y \) be the coordinates of \( \y \) in that basis, and put \( w_i = u_i^2 \). Then \( \sum_i w_i = \norm{\y}_2^2 = 1 \) by Parseval's identity (@thm-parseval-identity), every \( w_i \ge 0 \), and
\[
\y\tp\A\y = \sum_i \lambda_i w_i \eqqcolon \mu ,
\qquad
\y\tp\A^{-1}\y = \sum_i \frac{w_i}{\lambda_i} ,
\]
the second because \( \A^{-1}\q_i = \lambda_i^{-1}\q_i \). Since the \( w_i \) are weights summing to \( 1 \) and every \( \lambda_i \in [c, a] \), the number \( \mu \) lies in \( [c, a] \). Averaging \( (\ast) \) with the weights \( w_i \),
\[
\y\tp\A^{-1}\y \le \sum_i w_i\,\frac{a + c - \lambda_i}{ac} = \frac{a + c - \mu}{ac} .
\]
Hence \( (\y\tp\A\y)(\y\tp\A^{-1}\y) \le \mu(a + c - \mu)/(ac) \). Finally, for any real \( \mu \),
\[
\mu(a + c - \mu) = \frac{(a+c)^2}{4} - \Bigl(\frac{a+c}{2} - \mu\Bigr)^{2} \le \frac{(a+c)^2}{4} ,
\]
and dividing by \( ac \) gives the bound. This proves the lemma.
:::

::: {.remark}
Equality is attainable: take \( \y = (\q_1 + \q_n)/\sqrt2 \), so that \( w_1 = w_n = \tfrac12 \) and every other weight is \( 0 \). Then \( (\ast) \) is an equality at each \( \lambda_i \) carrying weight, since those are \( a \) and \( c \), and \( \mu = (a+c)/2 \) makes the last step an equality too. Only the weights \( w_i = u_i^2 \) enter, so \( (\q_1 - \q_n)/\sqrt2 \) serves just as well, and so does any non-zero multiple of either. @exm-steepest-descent-sharp does exactly this, up to sign and scale.
:::

We also record the condition number in the form we shall use it. For \( \A \succ 0 \), @lem-hermitian-spectral-norm gives \( \norm{\A}_2 = \lambda_1 \), since all eigenvalues are positive; the eigenvalues of \( \A^{-1} \) are the \( \lambda_i^{-1} \), so the same lemma gives \( \norm{\A^{-1}}_2 = \lambda_n^{-1} \). Hence, by @def-condition-number,
\[
\kappa \coloneqq \kappa_2(\A) = \frac{\lambda_1}{\lambda_n} \ \ge 1 .
\]{#eq-kappa-of-a-positive-matrix}

::: {#thm-steepest-descent}
[Convergence of Steepest Descent]

Let \( \A \in M_n(\nR) \) be symmetric positive definite with \( \kappa = \kappa_2(\A) \), let \( \b \in \nR^n \), and let \( \x^{(0)}, \x^{(1)}, \dots \) be the steepest descent iterates. Then for every \( k \) for which \( \x^{(k)} \) is defined,
\[
\norm{\x^{(k)} - \x^{\star}}_{\A}
\le \Bigl(\frac{\kappa - 1}{\kappa + 1}\Bigr)^{k}\,\norm{\x^{(0)} - \x^{\star}}_{\A} .
\]
:::

::: {.idea}
One step at a time. Write the new energy-norm error in terms of the old one; the exact line search makes the difference a single explicit fraction, whose numerator and denominator are exactly the three quantities Kantorovich's inequality compares. What comes out is \( 1 - 4\lambda_1\lambda_n/(\lambda_1+\lambda_n)^2 \), and that number is the square of \( (\kappa-1)/(\kappa+1) \).
:::

::: {.proof}
It is enough to prove the estimate for one step and then iterate. Fix \( k \) and write \( \x = \x^{(k)} \), \( \r = \r^{(k)} \), \( t = t_k \) and \( \boldsymbol{\varepsilon} = \boldsymbol{\varepsilon}^{(k)} \coloneqq \x^{(k)} - \x^{\star} \), and assume \( \r \ne \0 \). By @eq-residual-error, \( \r = -\A\boldsymbol{\varepsilon} \), so
\[
\norm{\boldsymbol{\varepsilon}}_{\A}^2 = \boldsymbol{\varepsilon}\tp\A\boldsymbol{\varepsilon} = (\A^{-1}\r)\tp\A(\A^{-1}\r) = \r\tp\A^{-1}\r ,
\]
using \( \A\tp = \A \) and \( (\A^{-1})\tp = \A^{-1} \). The new error is \( \boldsymbol{\varepsilon} + t\r \), so
\[
\begin{aligned}
\norm{\boldsymbol{\varepsilon} + t\r}_{\A}^2
&= \norm{\boldsymbol{\varepsilon}}_{\A}^2 + 2t\,\r\tp\A\boldsymbol{\varepsilon} + t^2\,\r\tp\A\r\\
&= \norm{\boldsymbol{\varepsilon}}_{\A}^2 - 2t\,\r\tp\r + t^2\,\r\tp\A\r ,
\end{aligned}
\]
the second line because \( \A\boldsymbol{\varepsilon} = -\r \). Substituting \( t = (\r\tp\r)/(\r\tp\A\r) \) collapses the last two terms:
\[
\norm{\boldsymbol{\varepsilon} + t\r}_{\A}^2
= \norm{\boldsymbol{\varepsilon}}_{\A}^2 - \frac{(\r\tp\r)^2}{\r\tp\A\r}
= \norm{\boldsymbol{\varepsilon}}_{\A}^2\Bigl(1 - \frac{(\r\tp\r)^2}{(\r\tp\A\r)(\r\tp\A^{-1}\r)}\Bigr),
\]
where the last step divides and multiplies by \( \norm{\boldsymbol{\varepsilon}}_{\A}^2 = \r\tp\A^{-1}\r \), which is non-zero because \( \r \ne \0 \). By @lem-kantorovich applied to \( \y = \r \),
\[
\frac{(\r\tp\r)^2}{(\r\tp\A\r)(\r\tp\A^{-1}\r)} \ \ge\ \frac{4\lambda_1\lambda_n}{(\lambda_1+\lambda_n)^2},
\]
so the bracket is at most
\[
1 - \frac{4\lambda_1\lambda_n}{(\lambda_1 + \lambda_n)^2}
= \frac{(\lambda_1 - \lambda_n)^2}{(\lambda_1 + \lambda_n)^2}
= \Bigl(\frac{\kappa - 1}{\kappa + 1}\Bigr)^{2},
\]
the last equality on dividing numerator and denominator by \( \lambda_n^2 \) and using @eq-kappa-of-a-positive-matrix. Since \( \boldsymbol{\varepsilon} + t\r = \x^{(k+1)} - \x^{\star} = \boldsymbol{\varepsilon}^{(k+1)} \), taking square roots gives \( \norm{\boldsymbol{\varepsilon}^{(k+1)}}_{\A} \le \frac{\kappa-1}{\kappa+1}\norm{\boldsymbol{\varepsilon}^{(k)}}_{\A} \), and an induction on \( k \) proves the theorem.
:::

::: {#exm-steepest-descent-sharp}
[The bound is attained]

Let \( \A = \diag(9, 1) \), \( \b = (9, 1) \) and \( \x^{(0)} = (2, -8) \). Run three steps of steepest descent and compare with @thm-steepest-descent.
:::

::: {.solution}
Here \( \x^{\star} = (1, 1) \) and \( \kappa = 9 \), so the bound's factor is \( \tfrac45 \). The first residual is
\[
\r^{(0)} = \b - \A\x^{(0)} = (9,1) - (18, -8) = (-9, 9),
\]
so \( \r\tp\r = 162 \) and \( \r\tp\A\r = 9\cdot 81 + 81 = 810 \), giving \( t_0 = \tfrac15 \). Then
\[
\x^{(1)} = (2,-8) + \tfrac15(-9,9) = \bigl(\tfrac15, -\tfrac{31}{5}\bigr),
\qquad
\r^{(1)} = \bigl(\tfrac{36}{5}, \tfrac{36}{5}\bigr).
\]
The two components of \( \r^{(1)} \) are again equal in absolute value, so \( t_1 = \tfrac15 \) as well, and
\( \x^{(2)} = \bigl(\tfrac{41}{25}, -\tfrac{119}{25}\bigr) \), \( \x^{(3)} = \bigl(\tfrac{61}{125}, -\tfrac{451}{125}\bigr) \). The squared energy-norm errors are
\[
90, \qquad \tfrac{288}{5}, \qquad \tfrac{4608}{125}, \qquad \tfrac{73728}{3125},
\]
and each is exactly \( \tfrac{16}{25} \) times the one before. So the ratio is \( \tfrac45 \) at every step: the bound of @thm-steepest-descent holds with equality here, and no better constant is possible.
:::

The picture behind the example is a staircase. On an elongated bowl the steepest direction points across the valley rather than along it, so the iterates cross and re-cross. The residuals \( \r^{(0)} \) and \( \r^{(2)} \) in @exm-steepest-descent-sharp are parallel: the method keeps searching in directions it has already used.

::: {.check}
Show that consecutive steepest descent residuals are always orthogonal, \( (\r^{(k+1)})\tp\r^{(k)} = 0 \). What does that say about the shape of the path?
:::

::: {.solution}
\( \r^{(k+1)} = \b - \A\x^{(k+1)} = \b - \A\x^{(k)} - t_k\A\r^{(k)} = \r^{(k)} - t_k\A\r^{(k)} \), so
\[
(\r^{(k+1)})\tp\r^{(k)} = \r\tp\r - t_k\,\r\tp\A\r = 0
\]
by the choice of \( t_k \), writing \( \r = \r^{(k)} \). So each step turns a right angle: the path is a staircase. In two dimensions that forces every second direction to be parallel, which is why @exm-steepest-descent-sharp never escapes its worst case.
:::

## Conjugate directions

The defect is now visible: each line search spoils the minimality achieved along the previous direction. We want directions \( \p^{(0)}, \p^{(1)}, \dots \) for which a search along \( \p^{(k)} \) leaves the earlier work intact, so that after \( k \) steps the iterate is optimal over the whole \( k \)-dimensional affine piece explored so far.

Read the requirement off the goal. Being optimal over \( \x^{(0)} + \Span(\p^{(0)}, \dots, \p^{(k-1)}) \) means, by @prp-quadratic-minimizer, that the error is \( \A \)-orthogonal to that span; and one step changes the error by \( t_k\p^{(k)} \). So the condition that preserves the earlier orthogonality is that \( \p^{(k)} \) itself be \( \A \)-orthogonal to \( \p^{(0)}, \dots, \p^{(k-1)} \). That is forced, not guessed. Which conjugate directions? The cheapest answer: take the residual and remove only what \( \A \)-orthogonality forbids.

::: {#def-conjugate-gradient}
[The Conjugate Gradient Iteration]

Let \( \A \in M_n(\nR) \) be symmetric positive definite, \( \b \in \nR^n \) and \( \x^{(0)} \in \nR^n \). Set
\[
\r^{(0)} = \b - \A\x^{(0)}, \qquad \p^{(0)} = \r^{(0)} .
\]
For \( k = 0, 1, 2, \dots \): if \( \r^{(k)} = \0 \), stop. Otherwise put
\[
\begin{aligned}
\alpha_k &= \frac{(\r^{(k)})\tp\r^{(k)}}{(\p^{(k)})\tp\A\p^{(k)}}, &
\x^{(k+1)} &= \x^{(k)} + \alpha_k\p^{(k)},\\
\r^{(k+1)} &= \r^{(k)} - \alpha_k\A\p^{(k)}, &
\beta_k &= \frac{(\r^{(k+1)})\tp\r^{(k+1)}}{(\r^{(k)})\tp\r^{(k)}},
\end{aligned}
\]
and \( \p^{(k+1)} = \r^{(k+1)} + \beta_k\p^{(k)} \). This is the **conjugate gradient** iteration, or **CG**.
:::

**A non-example, by dropping one clause.** Keep everything about the recursion and only weaken \( \A \succ 0 \) to "symmetric and invertible". Take
\[
\A = \begin{pmatrix} 1 & 0 \\ 0 & -1\end{pmatrix},
\qquad \b = (1, 1), \qquad \x^{(0)} = \0 .
\]
Then \( \p^{(0)} = \r^{(0)} = (1,1) \) and \( (\p^{(0)})\tp\A\p^{(0)} = 1 - 1 = 0 \): the very first \( \alpha_0 \) divides by zero, and the iteration does not start. What failed is exactly clause (P2) of @def-positive-semidefinite in its strict form, which is what guarantees \( \p\tp\A\p > 0 \) for \( \p \ne \0 \). Symmetry alone is not enough, and nor is invertibility; both @prp-quadratic-minimizer (the bowl has a bottom) and @thm-cg-optimality (the search directions are usable) need definiteness.

Three remarks on the shape of the recursion. The update of \( \r \) is not a fresh evaluation of \( \b - \A\x \) but a consequence of the update of \( \x \); the two agree, since \( \b - \A\x^{(k+1)} = \r^{(k)} - \alpha_k\A\p^{(k)} \). Only one product \( \A\p^{(k)} \) is formed per step, serving both \( \alpha_k \) and \( \r^{(k+1)} \). And the new direction corrects the residual by a multiple of the **single** previous direction, not of all of them — the surprise, and the reason CG is short.

::: {#thm-cg-optimality}
[Conjugate Gradients: Orthogonality and Optimality]

Let \( \A \succ 0 \), \( \b \in \nR^n \), \( \x^{(0)} \in \nR^n \), and write \( \cK_k = \cK_k(\A, \r^{(0)}) \) for the Krylov subspaces of @def-krylov-subspace, with \( \cK_0 = \{\0\} \). Suppose the iteration of @def-conjugate-gradient has produced non-zero \( \r^{(0)}, \dots, \r^{(k)} \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \p^{(0)}, \dots, \p^{(k)} \) are non-zero and pairwise \( \A \)-orthogonal, and every \( \alpha_j \) and \( \beta_j \) with \( j \le k \) is defined, with \( \alpha_j > 0 \);
2. \( \r^{(0)}, \dots, \r^{(k)} \) are pairwise orthogonal, and \( (\r^{(k+1)})\tp\p^{(j)} = 0 \) for every \( j \le k \);
3. \( \Span(\r^{(0)}, \dots, \r^{(k)}) = \Span(\p^{(0)}, \dots, \p^{(k)}) = \cK_{k+1} \), a space of dimension \( k+1 \);
4. \( \x^{(k+1)} \) is the **unique** minimizer of \( \norm{\x - \x^{\star}}_{\A} \) over the affine set \( \x^{(0)} + \cK_{k+1} \).
:::
:::

::: {.idea}
Everything is one induction, and the two coefficients are exactly what the induction needs. Step \( k \) has to deliver two orthogonality relations: the new residual against the old directions, and the new direction against the old directions in the \( \A \)-inner product. The first is forced by \( \alpha_k \), the second by \( \beta_k \), and each forces it only against the *latest* predecessor; the older ones come free, because \( \A\p^{(j)} \) is a combination of \( \r^{(j)} \) and \( \r^{(j+1)} \), and the new residual is already orthogonal to both. Optimality (d) is then the Pythagorean theorem, applied in the energy inner product.
:::

::: {.proof}
Parts (a), (b) and (c) are proved together by induction on \( k \). Throughout, \( \A\tp = \A \) is used silently to move \( \A \) across a dot product, and \( \A\cK_j \subseteq \cK_{j+1} \) directly from @def-krylov-subspace.

**Base \( k = 0 \).** Here \( \p^{(0)} = \r^{(0)} \ne \0 \), so \( (\p^{(0)})\tp\A\p^{(0)} > 0 \) and \( \alpha_0 = \norm{\r^{(0)}}_2^2/(\p^{(0)})\tp\A\p^{(0)} \) is defined and positive; that is (a). Part (c) is \( \Span(\r^{(0)}) = \Span(\p^{(0)}) = \cK_1 \), which is @def-krylov-subspace, and the dimension is \( 1 \) because \( \r^{(0)} \ne \0 \). For (b), a single vector is vacuously an orthogonal list, and
\[
(\r^{(1)})\tp\p^{(0)} = (\r^{(0)})\tp\p^{(0)} - \alpha_0(\p^{(0)})\tp\A\p^{(0)}
= \norm{\r^{(0)}}_2^2 - \norm{\r^{(0)}}_2^2 = 0 ,
\]
using \( \r^{(1)} = \r^{(0)} - \alpha_0\A\p^{(0)} \), \( \p^{(0)} = \r^{(0)} \) and the definition of \( \alpha_0 \).

**Inductive step.** Assume (a), (b), (c) for \( k \), and assume \( \r^{(k+1)} \ne \0 \), so that \( \beta_k \) and \( \p^{(k+1)} \) are formed. We prove (a), (b), (c) for \( k+1 \).

**Step 1: the residuals stay orthogonal.** By (b), \( \r^{(k+1)} \) is orthogonal to \( \p^{(0)}, \dots, \p^{(k)} \), and by (c) that list spans the same space as \( \r^{(0)}, \dots, \r^{(k)} \). Hence \( \r^{(k+1)} \perp \r^{(j)} \) for every \( j \le k \), and with (b) this makes \( \r^{(0)}, \dots, \r^{(k+1)} \) pairwise orthogonal.

**Step 2: (c) for \( k+1 \).** From \( \r^{(k+1)} = \r^{(k)} - \alpha_k\A\p^{(k)} \) with \( \r^{(k)}, \p^{(k)} \in \cK_{k+1} \), we get \( \r^{(k+1)} \in \cK_{k+2} \), and then \( \p^{(k+1)} = \r^{(k+1)} + \beta_k\p^{(k)} \in \cK_{k+2} \) as well. Moreover
\[
\Span(\p^{(0)}, \dots, \p^{(k+1)}) = \Span(\p^{(0)}, \dots, \p^{(k)}, \r^{(k+1)})
= \Span(\r^{(0)}, \dots, \r^{(k+1)}),
\]
the first equality because \( \p^{(k+1)} \) differs from \( \r^{(k+1)} \) by a multiple of \( \p^{(k)} \), the second by (c). By Step 1 the vectors \( \r^{(0)}, \dots, \r^{(k+1)} \) are non-zero and pairwise orthogonal, hence independent (@thm-orthogonal-independent), so this common span has dimension \( k+2 \). It sits inside \( \cK_{k+2} \), which is spanned by \( k+2 \) vectors and so has dimension at most \( k+2 \); equal dimensions force equal spaces.

**Step 3: \( \p^{(k+1)} \ne \0 \), and \( \alpha_{k+1} \) is defined.** By (b), \( (\r^{(k+1)})\tp\p^{(k)} = 0 \), so
\[
(\p^{(k+1)})\tp\r^{(k+1)} = \norm{\r^{(k+1)}}_2^2 + \beta_k(\p^{(k)})\tp\r^{(k+1)} = \norm{\r^{(k+1)}}_2^2 > 0 .
\tag{$\dagger$}
\]
Hence \( \p^{(k+1)} \ne \0 \), so \( (\p^{(k+1)})\tp\A\p^{(k+1)} > 0 \) and \( \alpha_{k+1} \) is defined and positive.

**Step 4: (a) for \( k+1 \).** We must show \( (\p^{(k+1)})\tp\A\p^{(j)} = 0 \) for \( j \le k \). For \( j = k \), use \( \A\p^{(k)} = (\r^{(k)} - \r^{(k+1)})/\alpha_k \):
\[
(\p^{(k+1)})\tp\A\p^{(k)}
= (\r^{(k+1)})\tp\A\p^{(k)} + \beta_k(\p^{(k)})\tp\A\p^{(k)} .
\]
By Step 1 the first term is \( \bigl(0 - \norm{\r^{(k+1)}}_2^2\bigr)/\alpha_k \), and \( (\p^{(k)})\tp\A\p^{(k)} = \norm{\r^{(k)}}_2^2/\alpha_k \) by the definition of \( \alpha_k \). The two cancel exactly when \( \beta_k = \norm{\r^{(k+1)}}_2^2/\norm{\r^{(k)}}_2^2 \), which is how \( \beta_k \) was defined. For \( j < k \), the term \( \beta_k(\p^{(k)})\tp\A\p^{(j)} \) vanishes by (a), and
\[
\A\p^{(j)} = \frac{\r^{(j)} - \r^{(j+1)}}{\alpha_j} \in \Span(\r^{(0)}, \dots, \r^{(k)}),
\]
so \( (\r^{(k+1)})\tp\A\p^{(j)} = 0 \) by Step 1.

**Step 5: (b) for \( k+1 \).** The first half is Step 1. For the second, \( \r^{(k+2)} = \r^{(k+1)} - \alpha_{k+1}\A\p^{(k+1)} \), so for \( j = k+1 \),
\[
(\r^{(k+2)})\tp\p^{(k+1)} = (\r^{(k+1)})\tp\p^{(k+1)} - \alpha_{k+1}(\p^{(k+1)})\tp\A\p^{(k+1)} = 0
\]
by \( (\dagger) \) and the definition of \( \alpha_{k+1} \); and for \( j \le k \),
\[
(\r^{(k+2)})\tp\p^{(j)} = (\r^{(k+1)})\tp\p^{(j)} - \alpha_{k+1}(\p^{(k+1)})\tp\A\p^{(j)} = 0 - 0 = 0
\]
by (b) and Step 4. This completes the induction.

**Proof of (d).** By construction \( \x^{(k+1)} = \x^{(0)} + \sum_{j \le k}\alpha_j\p^{(j)} \), which lies in \( \x^{(0)} + \cK_{k+1} \) by (c). Let \( \boldsymbol{\varepsilon} = \x^{(k+1)} - \x^{\star} \). By @eq-residual-error, \( \A\boldsymbol{\varepsilon} = -\r^{(k+1)} \), so for every \( \w \in \cK_{k+1} = \Span(\p^{(0)}, \dots, \p^{(k)}) \),
\[
\inner{\boldsymbol{\varepsilon}}{\w}_{\A} = \w\tp\A\boldsymbol{\varepsilon} = -\w\tp\r^{(k+1)} = 0
\]
by (b). Now take any \( \x = \x^{(0)} + \z \) with \( \z \in \cK_{k+1} \), and write \( \x - \x^{\star} = \boldsymbol{\varepsilon} + \w \) with \( \w = \z - \sum_{j\le k}\alpha_j\p^{(j)} \in \cK_{k+1} \). By the Pythagorean theorem (@thm-pythagoras) in the energy inner product,
\[
\norm{\x - \x^{\star}}_{\A}^2 = \norm{\boldsymbol{\varepsilon}}_{\A}^2 + \norm{\w}_{\A}^2 \ \ge\ \norm{\boldsymbol{\varepsilon}}_{\A}^2 ,
\]
with equality only for \( \w = \0 \), that is only for \( \x = \x^{(k+1)} \). This proves the theorem.
:::

::: {#cor-cg-finite-termination}
[Finite Termination]

In exact arithmetic the conjugate gradient iteration reaches \( \r^{(m)} = \0 \), and hence \( \x^{(m)} = \x^{\star} \), for some \( m \le n \). If \( \A \) has only \( d \) distinct eigenvalues, then \( m \le d \).
:::

::: {.proof}
Suppose \( \r^{(0)}, \dots, \r^{(k)} \) are all non-zero. By @thm-cg-optimality (c), \( \dim\cK_{k+1} = k+1 \). Since \( \cK_{k+1} \subseteq \nR^n \), this forces \( k + 1 \le n \); so the residuals cannot all be non-zero for \( k = n \), and \( \r^{(m)} = \0 \) for some \( m \le n \). Then \( \A\x^{(m)} = \b \), so \( \x^{(m)} = \x^{\star} \).

For the refinement, let \( \mu_1, \dots, \mu_d \) be the distinct eigenvalues and put \( q(x) = (x - \mu_1)\cdots(x - \mu_d) \). By @cor-spectral-real-matrix, \( \A = \Q\D\Q\tp \) with \( \Q \) orthogonal and \( \D \) diagonal carrying the eigenvalues, so \( q(\A) = \Q\,q(\D)\,\Q\tp = 0 \), every diagonal entry of \( q(\D) \) being \( q \) at an eigenvalue. Hence \( \A^{d}\r^{(0)} \) is a combination of \( \r^{(0)}, \A\r^{(0)}, \dots, \A^{d-1}\r^{(0)} \), so \( \cK_{d+1} = \cK_d \) and \( \dim\cK_{k} \le d \) for every \( k \). If \( \r^{(0)}, \dots, \r^{(d)} \) were all non-zero we would get \( \dim\cK_{d+1} = d+1 > d \), a contradiction. So \( m \le d \).
:::

::: {#exm-cg-two-eigenvalues}
[Two distinct eigenvalues, two steps]

Let \( \A = \I_3 + \J \), where \( \J \) is the all-ones matrix, let \( \b = \e_1 \) and \( \x^{(0)} = \0 \). Run CG.
:::

::: {.solution}
\( \A \) has rows \( (2,1,1) \), \( (1,2,1) \), \( (1,1,2) \). Since \( \J\1 = 3\1 \) and \( \J \) kills \( \1^{\perp} \), the eigenvalues of \( \A \) are \( 4 \) (once) and \( 1 \) (twice): \( d = 2 \). Also \( \A^{-1} = \I - \tfrac14\J \), so \( \x^{\star} = \e_1 - \tfrac14\1 = \bigl(\tfrac34, -\tfrac14, -\tfrac14\bigr) \).

*Step 0.* \( \r^{(0)} = \p^{(0)} = (1,0,0) \), \( (\r^{(0)})\tp\r^{(0)} = 1 \), \( \A\p^{(0)} = (2,1,1) \), \( (\p^{(0)})\tp\A\p^{(0)} = 2 \), so \( \alpha_0 = \tfrac12 \) and
\[
\x^{(1)} = \bigl(\tfrac12, 0, 0\bigr), \qquad
\r^{(1)} = (1,0,0) - \tfrac12(2,1,1) = \bigl(0, -\tfrac12, -\tfrac12\bigr).
\]
Then \( \beta_0 = \tfrac12/1 = \tfrac12 \) and \( \p^{(1)} = \bigl(0,-\tfrac12,-\tfrac12\bigr) + \tfrac12(1,0,0) = \bigl(\tfrac12,-\tfrac12,-\tfrac12\bigr) \).

*Step 1.* The rows of \( \A \) applied to \( \p^{(1)} \) give \( 1 - \tfrac12 - \tfrac12 = 0 \), then \( \tfrac12 - 1 - \tfrac12 = -1 \), then \( \tfrac12 - \tfrac12 - 1 = -1 \); so \( \A\p^{(1)} = (0,-1,-1) \) and \( (\p^{(1)})\tp\A\p^{(1)} = 1 \). With \( (\r^{(1)})\tp\r^{(1)} = \tfrac12 \) this gives \( \alpha_1 = \tfrac12 \) and
\[
\x^{(2)} = \bigl(\tfrac12,0,0\bigr) + \tfrac12\bigl(\tfrac12,-\tfrac12,-\tfrac12\bigr)
= \bigl(\tfrac34, -\tfrac14, -\tfrac14\bigr) = \x^{\star},
\]
with \( \r^{(2)} = \bigl(0,-\tfrac12,-\tfrac12\bigr) - \tfrac12(0,-1,-1) = \0 \). Two steps, as @cor-cg-finite-termination predicts, for a \( 3 \times 3 \) system. Checks: \( (\r^{(1)})\tp\r^{(0)} = 0 \) and \( (\p^{(1)})\tp\A\p^{(0)} = \bigl(\tfrac12,-\tfrac12,-\tfrac12\bigr)\cdot(2,1,1) = 1 - \tfrac12 - \tfrac12 = 0 \).
:::

::: {.warning}
**Finite termination is a theorem about exact arithmetic, and it is not how CG is used.** In the floating-point model of Section 1 the computed residuals lose their orthogonality, as the Lanczos vectors of Section 6 do. The two algorithms are closely related: started from the same \( \A \) and the same vector they build bases of the same Krylov spaces, and the tridiagonal matrix of @thm-lanczos can be assembled from the CG coefficients — which are *not* the \( \alpha_j \) and \( \beta_j \) of @thm-lanczos, those being the entries of that tridiagonal matrix, but different numbers. **That correspondence, due to Lanczos and to Hestenes and Stiefel, and the rounding behavior it carries across, due to Paige and Greenbaum, are described here and not proved; nothing in this section depends on either.** A run of CG on a matrix of order \( 10^6 \) is stopped after a few hundred steps, and the theorem that matters is @thm-cg-convergence below.
:::

## Chebyshev polynomials

@thm-cg-optimality (d) has an equivalent form that turns the whole question of speed into a question about polynomials, and that question has a classical answer. We need one family of polynomials and two facts about it.

*The Chebyshev polynomials stay within \( 1 \) on \( [-1,1] \) and then grow geometrically outside it.*

::: {#def-chebyshev-polynomials}
[Chebyshev Polynomials]

The **Chebyshev polynomials** \( T_0, T_1, T_2, \dots \in \nR[x] \) are defined by
\[
T_0 = 1, \qquad T_1 = x, \qquad
T_{k+1} = 2x\,T_k - T_{k-1} \ \ (k \ge 1).
\]
:::

The name comes from Chapter 10. Its table at the end of §10 lists the **monic** orthogonal polynomial sequence of @def-orthogonal-polynomial-sequence for the weight \( (1-t^2)^{-1/2} \) on \( (-1,1) \), and the \( T_k \) above are its members rescaled — which is why the recurrence here is not the one of @thm-three-term-recurrence, that theorem being stated for the monic normalization, where no factor \( 2 \) appears. The book has not proved that identification and nothing below uses it. Here the recurrence *is* the definition, and we prove what we need from it directly. The first few are
\[
T_2 = 2x^2 - 1, \quad T_3 = 4x^3 - 3x, \quad T_4 = 8x^4 - 8x^2 + 1 .
\]

We shall need the degrees, and the recurrence supplies them by induction on \( k \). For \( k = 0 \) and \( k = 1 \), \( \deg T_k = k \), with leading coefficient \( 1 \) in both cases. Let \( k \ge 1 \) and suppose \( \deg T_{k-1} = k-1 \) and \( \deg T_k = k \) with leading coefficient \( c_k \). Then \( 2xT_k \) has degree \( k+1 \) with leading coefficient \( 2c_k \), while \( \deg T_{k-1} = k - 1 < k+1 \), so no cancellation is possible in \( T_{k+1} = 2xT_k - T_{k-1} \) and \( \deg T_{k+1} = k+1 \) with leading coefficient \( 2c_k \). Hence \( \deg T_k = k \) for every \( k \), and since \( c_1 = 1 \) the doubling gives \( c_k = 2^{k-1} \) for \( k \ge 1 \).

The one trick in the subject is a change of variable. Every complex number \( x \) can be written as \( \tfrac12(w + w^{-1}) \) for some \( w \ne 0 \): the equation \( w^2 - 2xw + 1 = 0 \) has two roots in \( \nC \), neither of them \( 0 \) since their product is \( 1 \). In that variable the recurrence becomes trivial.

::: {#lem-chebyshev-extremal}
[Chebyshev Polynomials: Size Inside and Growth Outside]

For every \( k \ge 0 \) and every \( w \in \nC \setminus\{0\} \),
\[
T_k\Bigl(\frac{w + w^{-1}}{2}\Bigr) = \frac{w^{k} + w^{-k}}{2} .
\]{#eq-chebyshev-substitution}
Consequently:

::: {.enumerate options="label=(\alph*)"}
1. \( \lvert T_k(x)\rvert \le 1 \) for every real \( x \in [-1, 1] \), and \( T_k(1) = 1 \);
2. for every real \( z > 1 \),
\[
T_k(z) = \tfrac12\Bigl(\bigl(z + \sqrt{z^2-1}\bigr)^{k} + \bigl(z + \sqrt{z^2-1}\bigr)^{-k}\Bigr)
\ \ge\ \tfrac12\bigl(z + \sqrt{z^2-1}\bigr)^{k} ,
\]
and, separately, \( T_k(z) \ge 1 \).
:::
:::

::: {.idea}
Under \( x = \tfrac12(w + w^{-1}) \) the recurrence of @def-chebyshev-polynomials says nothing more than \( w^{k+1} + w^{-(k+1)} = (w + w^{-1})(w^k + w^{-k}) - (w^{k-1} + w^{-(k-1)}) \), which is true because the cross terms cancel. The two facts are then two choices of \( w \): on \( [-1,1] \) take \( \lvert w\rvert = 1 \), so that \( w^{k} \) and \( w^{-k} \) are again on the unit circle; outside, take \( w \) real and greater than \( 1 \), so that \( w^{k} \) grows geometrically.
:::

::: {.proof}
*The identity @eq-chebyshev-substitution.* Induct on \( k \). For \( k = 0 \) both sides are \( 1 \), and for \( k = 1 \) both are \( \tfrac12(w + w^{-1}) \). Assume the identity for \( k-1 \) and \( k \), with \( k \ge 1 \), and write \( x = \tfrac12(w + w^{-1}) \). Then
\[
\begin{aligned}
T_{k+1}(x) &= 2x\,T_k(x) - T_{k-1}(x)\\
&= (w + w^{-1})\frac{w^k + w^{-k}}{2} - \frac{w^{k-1} + w^{-(k-1)}}{2}\\
&= \frac{w^{k+1} + w^{-(k-1)} + w^{k-1} + w^{-(k+1)} - w^{k-1} - w^{-(k-1)}}{2},
\end{aligned}
\]
which is \( \tfrac12(w^{k+1} + w^{-(k+1)}) \), as required.

*(a).* Let \( x \in [-1,1] \) and put \( w = x + i\sqrt{1 - x^2} \). Then \( \lvert w\rvert^2 = x^2 + (1 - x^2) = 1 \), so \( w \ne 0 \) and \( w^{-1} = \conj{w} \) (@thm-conjugate-properties), whence \( \tfrac12(w + w^{-1}) = \tfrac12(w + \conj w) = x \). By @eq-chebyshev-substitution and \( \lvert u + v\rvert \le \lvert u\rvert + \lvert v\rvert \) (@thm-complex-triangle-inequality),
\[
\lvert T_k(x)\rvert = \tfrac12\lvert w^k + w^{-k}\rvert \le \tfrac12\bigl(\lvert w\rvert^k + \lvert w\rvert^{-k}\bigr) = 1 .
\]
For \( x = 1 \) take \( w = 1 \), giving \( T_k(1) = \tfrac12(1 + 1) = 1 \).

*(b).* Let \( z > 1 \) and put \( w = z + \sqrt{z^2 - 1} \), a real number \( > 1 \). Then
\[
w\bigl(z - \sqrt{z^2-1}\bigr) = z^2 - (z^2 - 1) = 1 ,
\]
so \( w^{-1} = z - \sqrt{z^2-1} \) and \( \tfrac12(w + w^{-1}) = z \). Now @eq-chebyshev-substitution gives the displayed formula. Both \( w^{k} \) and \( w^{-k} \) are positive, so dropping the second gives the displayed inequality. For the separate bound, \( \tfrac12(s + s^{-1}) \ge 1 \) for every \( s > 0 \), because \( s + s^{-1} - 2 = (s^{1/2} - s^{-1/2})^2 \ge 0 \); applying this with \( s = w^{k} > 0 \) gives \( T_k(z) = \tfrac12(w^k + w^{-k}) \ge 1 \). This proves the lemma.
:::

::: {.warning}
**Part (a) is false the moment \( x \) leaves \( [-1,1] \), and spectacularly so.** \( T_{10}(1.1) \) is already about \( 42.2 \), and \( T_{50}(1.1) \) exceeds \( 2 \times 10^{9} \). That explosion is not a defect; it is the whole resource. The polynomial in the next theorem is small where the eigenvalues live and large at \( 0 \), and the ratio of the two is what CG converts into speed.
:::


::: {.remark}
That the Chebyshev polynomials are also **extremal** — among monic polynomials of degree \( k \), the scaled \( T_k/2^{k-1} \) has the smallest maximum modulus on \( [-1,1] \) — is classical, is not proved here, and is not needed. What @thm-cg-convergence uses is only that \( T_k \), rescaled, is an admissible competitor in the minimum of @eq-cg-polynomial-min: small on the interval where the eigenvalues lie, and large at \( 0 \).
:::

## The square root

::: {#thm-cg-convergence}
[Convergence of Conjugate Gradients]

Let \( \A \in M_n(\nR) \) be symmetric positive definite with \( \kappa = \kappa_2(\A) \), let \( \b \in \nR^n \), and let \( \x^{(k)} \) be the conjugate gradient iterates from \( \x^{(0)} \), with \( \x^{(k)} \coloneqq \x^{\star} \) once the iteration has terminated. Then for every \( k \ge 0 \),
\[
\norm{\x^{(k)} - \x^{\star}}_{\A}
\ \le\ 2\Bigl(\frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1}\Bigr)^{k}\,\norm{\x^{(0)} - \x^{\star}}_{\A} .
\]
:::

::: {.idea}
Three moves. ① @thm-cg-optimality says the CG error is the smallest among all errors reachable from the Krylov space; writing out what "reachable" means turns that into: the smallest value of \( \norm{q(\A)\boldsymbol{\varepsilon}^{(0)}}_{\A} \) over polynomials \( q \) of degree \( \le k \) with \( q(0) = 1 \). ② In an eigenbasis that quantity is at most \( \max_i\lvert q(\lambda_i)\rvert \) times the initial error, so we need one polynomial that is \( 1 \) at \( 0 \) and small on \( [\lambda_n, \lambda_1] \). ③ Chebyshev's polynomial, rescaled so that the interval becomes \( [-1,1] \), is that polynomial, and @lem-chebyshev-extremal measures it.
:::

::: {.proof}
If \( \kappa = 1 \) then \( \lambda_1 = \lambda_n \), so \( \A = \lambda_1\I \) by the spectral theorem, and \( \p^{(0)} = \r^{(0)} \) gives \( \alpha_0 = 1/\lambda_1 \) and \( \x^{(1)} = \x^{\star} \); the bound then reads \( 0 \le 0 \) for \( k \ge 1 \) and \( \norm{\boldsymbol{\varepsilon}^{(0)}}_{\A} \le 2\norm{\boldsymbol{\varepsilon}^{(0)}}_{\A} \) for \( k = 0 \), both true. So assume \( \kappa > 1 \). We may also assume the iteration has not terminated before step \( k \), since once it has, the left-hand side is \( 0 \).

**Step 1: the error is a polynomial in \( \A \) applied to the initial error.** Write \( \boldsymbol{\varepsilon}^{(0)} = \x^{(0)} - \x^{\star} \), so \( \r^{(0)} = -\A\boldsymbol{\varepsilon}^{(0)} \) by @eq-residual-error. A vector of \( \x^{(0)} + \cK_k \) has the form \( \x = \x^{(0)} + \sum_{j=0}^{k-1}c_j\A^{j}\r^{(0)} \), and then
\[
\x - \x^{\star} = \boldsymbol{\varepsilon}^{(0)} - \sum_{j=0}^{k-1}c_j\A^{j+1}\boldsymbol{\varepsilon}^{(0)} = q(\A)\,\boldsymbol{\varepsilon}^{(0)},
\qquad q(x) = 1 - \sum_{j=0}^{k-1}c_jx^{j+1} .
\]
As the \( c_j \) range over \( \nR^k \), \( q \) ranges over **all** polynomials of degree at most \( k \) with \( q(0) = 1 \). So @thm-cg-optimality (d) says
\[
\norm{\boldsymbol{\varepsilon}^{(k)}}_{\A}
= \min\bigl\{\norm{q(\A)\boldsymbol{\varepsilon}^{(0)}}_{\A} : \deg q \le k,\ q(0) = 1\bigr\} .
\]{#eq-cg-polynomial-min}

**Step 2: one eigenbasis estimate.** By @cor-spectral-real-matrix take an orthonormal basis \( \q_1, \dots, \q_n \) with \( \A\q_i = \lambda_i\q_i \), and write \( \boldsymbol{\varepsilon}^{(0)} = \sum_i u_i\q_i \). Then \( q(\A)\q_i = q(\lambda_i)\q_i \), so
\[
\norm{q(\A)\boldsymbol{\varepsilon}^{(0)}}_{\A}^2 = \sum_i \lambda_i\,q(\lambda_i)^2u_i^2
\le \Bigl(\max_i \lvert q(\lambda_i)\rvert\Bigr)^{2}\sum_i\lambda_iu_i^2 ,
\]
and \( \sum_i\lambda_iu_i^2 = \norm{\boldsymbol{\varepsilon}^{(0)}}_{\A}^2 \). Every \( \lambda_i \) lies in \( [\lambda_n, \lambda_1] \), so with @eq-cg-polynomial-min, for any admissible \( q \),
\[
\norm{\boldsymbol{\varepsilon}^{(k)}}_{\A} \le \Bigl(\max_{\lambda_n \le \lambda \le \lambda_1}\lvert q(\lambda)\rvert\Bigr)\norm{\boldsymbol{\varepsilon}^{(0)}}_{\A} .
\]{#eq-cg-any-polynomial}

**Step 3: the polynomial.** Put
\[
z = \frac{\lambda_1 + \lambda_n}{\lambda_1 - \lambda_n} = \frac{\kappa + 1}{\kappa - 1} > 1,
\qquad
q(\lambda) = \frac{1}{T_k(z)}\,T_k\Bigl(\frac{\lambda_1 + \lambda_n - 2\lambda}{\lambda_1 - \lambda_n}\Bigr).
\]
The inner expression is an affine function of \( \lambda \) carrying \( \lambda_n \) to \( 1 \) and \( \lambda_1 \) to \( -1 \), so it maps \( [\lambda_n, \lambda_1] \) into \( [-1,1] \); and it sends \( \lambda = 0 \) to \( z \). By @lem-chebyshev-extremal (b), \( T_k(z) \ge 1 > 0 \), so \( q \) is a well-defined polynomial of degree at most \( k \), and \( q(0) = T_k(z)/T_k(z) = 1 \). By @lem-chebyshev-extremal (a),
\[
\max_{\lambda_n \le \lambda \le \lambda_1}\lvert q(\lambda)\rvert \le \frac{1}{T_k(z)} .
\]

**Step 4: measuring \( T_k(z) \).** Since \( \kappa > 1 \),
\[
z^2 - 1 = \frac{(\kappa+1)^2 - (\kappa-1)^2}{(\kappa-1)^2} = \frac{4\kappa}{(\kappa-1)^2},
\qquad \sqrt{z^2-1} = \frac{2\sqrt\kappa}{\kappa - 1},
\]
so, using \( \kappa - 1 = (\sqrt\kappa-1)(\sqrt\kappa+1) \),
\[
z + \sqrt{z^2-1} = \frac{\kappa + 1 + 2\sqrt\kappa}{\kappa - 1}
= \frac{(\sqrt\kappa + 1)^2}{(\sqrt\kappa-1)(\sqrt\kappa+1)}
= \frac{\sqrt\kappa + 1}{\sqrt\kappa - 1} .
\]
By @lem-chebyshev-extremal (b), \( T_k(z) \ge \tfrac12\bigl((\sqrt\kappa+1)/(\sqrt\kappa-1)\bigr)^{k} \), so \( 1/T_k(z) \le 2\bigl((\sqrt\kappa-1)/(\sqrt\kappa+1)\bigr)^{k} \). Feeding this into @eq-cg-any-polynomial proves the theorem.
:::

The square root is the whole gain. Take \( \kappa = 100 \). Steepest descent contracts by at most \( 99/101 \approx 0.9802 \) per step, so reducing the energy-norm error by \( 10^{-6} \) needs about \( 691 \) steps; conjugate gradients contracts by \( 9/11 \approx 0.8182 \), and \( 2(9/11)^k \le 10^{-6} \) already at \( k = 73 \). Both cost one product with \( \A \) per step, so the ratio of the counts is the ratio of the work.

::: {.check}
Why does the factor \( 2 \) in @thm-cg-convergence cost so little, and why is it there at all?
:::

::: {.solution}
It costs little because it is a constant against a geometric factor: absorbing it changes the step count by \( \log 2/\log\bigl((\sqrt\kappa+1)/(\sqrt\kappa-1)\bigr) \), about \( 3.5 \) steps out of \( 73 \) when \( \kappa = 100 \). It is there because the lower bound for \( T_k(z) \) in @lem-chebyshev-extremal (b) throws away the term \( w^{-k} \); the surviving \( \tfrac12 \) is exactly this \( 2 \).
:::

::: {.remark}
The bound uses only the two ends of the spectrum, and it is often pessimistic. @eq-cg-any-polynomial holds for *every* admissible polynomial, so if the eigenvalues fall into a few tight clusters one may take \( q \) small near each cluster and do far better; @cor-cg-finite-termination is the extreme case. Conjugate gradients sees the whole spectrum, not just its ends.
:::

## Two footnotes: Chebyshev iteration and preconditioning

The polynomial in Step 3 depends only on \( \lambda_1 \) and \( \lambda_n \), so one can *fix* it in advance and update the iterates by the recurrence of @def-chebyshev-polynomials. This is the **Chebyshev iteration**. Three things are said about it: that it attains the bound of @thm-cg-convergence rather than beating it; that it needs estimates of \( \lambda_1 \) and \( \lambda_n \) which CG does not; and that in exchange it forms no inner products, which matters when the work is split across many processors. **None of the three is proved here.** The method and its analysis are due to Golub and Varga, and nothing in this section depends on them.

Since the cost is governed by \( \sqrt\kappa \), it pays to replace \( \A\x = \b \) by an equivalent system of smaller condition number. Choosing a symmetric positive definite \( \M \) close to \( \A \), and writing \( \M = \C\C\tp \), one applies CG to
\[
(\C^{-1}\A\C^{-\top})\y = \C^{-1}\b, \qquad \x = \C^{-\top}\y ,
\]
whose matrix is symmetric positive definite (@prp-congruence-positivity) and whose eigenvalues are the generalized eigenvalues of the pencil \( \A - \lambda\M \) of @def-generalized-eigenvalue, as Exercise C3 below asks you to check. This is **preconditioning**, and it is a subject rather than a theorem: which \( \M \) to choose depends on where \( \A \) came from, and no theorem of linear algebra answers that. We state the mechanism and stop.

## Exercises

### A. Check your understanding

:::: {#exr-conjugate-gradient-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the energy inner product of a symmetric positive definite \( \A \), and say which clause of @def-positive-semidefinite makes it an inner product.
2. State @prp-quadratic-minimizer, and explain in one sentence why it makes \( \norm{\cdot}_{\A} \) the natural yardstick for the error.
3. State the optimality property of the \( k \)-th conjugate gradient iterate, naming the set over which it is optimal.
4. Determine whether the following statement is correct, and justify your answer: in exact arithmetic, conjugate gradients applied to a \( 1000 \times 1000 \) positive definite matrix with \( 5 \) distinct eigenvalues terminates after at most \( 5 \) steps.
5. Write down the two Chebyshev facts of @lem-chebyshev-extremal, and say which of the two supplies the \( \sqrt\kappa \) in @thm-cg-convergence.
:::
::::

::: {.solution}
(a) \( \inner{\x}{\y}_{\A} = \y\tp\A\x \). Symmetry and bilinearity hold for any symmetric \( \A \); what makes it an inner product is \( \inner{\x}{\x}_{\A} = \x\tp\A\x > 0 \) for \( \x \ne \0 \), which is clause (P2) of @def-positive-semidefinite in its strict form.

(b) \( \phi(\x) - \phi(\x^{\star}) = \tfrac12\norm{\x-\x^{\star}}_{\A}^2 \), where \( \phi(\x) = \tfrac12\x\tp\A\x - \b\tp\x \) and \( \x^{\star} = \A^{-1}\b \). So the energy norm of the error *is* the excess of \( \phi \) over its minimum, up to the factor \( \tfrac12 \): it is the quantity every descent method is built to decrease.

(c) By @thm-cg-optimality (d), \( \x^{(k)} \) is the unique minimizer of \( \norm{\x - \x^{\star}}_{\A} \) over the affine set \( \x^{(0)} + \cK_k(\A, \r^{(0)}) \).

(d) Correct. By @cor-cg-finite-termination the number of steps is at most the number \( d \) of distinct eigenvalues, here \( 5 \), and the order \( 1000 \) plays no part. The proof is that \( q(\A) = 0 \) for the degree-\( 5 \) polynomial with the distinct eigenvalues as roots, so the Krylov spaces stop growing at dimension \( 5 \).

(e) \( \lvert T_k\rvert \le 1 \) on \( [-1,1] \), and \( T_k(z) \ge \tfrac12(z + \sqrt{z^2-1})^k \) for \( z > 1 \). The second supplies the square root: at \( z = (\kappa+1)/(\kappa-1) \) the number \( z + \sqrt{z^2-1} \) equals \( (\sqrt\kappa+1)/(\sqrt\kappa-1) \), and the square root enters through \( \sqrt{z^2-1} = 2\sqrt\kappa/(\kappa-1) \).
:::

### B. Practice

:::: {#exr-conjugate-gradient-b1}
[B1: Steepest descent by hand]

Let \( \A = \begin{pmatrix} 2 & 0 \\ 0 & 1\end{pmatrix} \), \( \b = (2, 1) \) and \( \x^{(0)} = (0, 0) \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \x^{(1)} \) and \( \x^{(2)} \) by steepest descent.
2. Compute \( \norm{\x^{(k)} - \x^{\star}}_{\A}^2 \) for \( k = 0, 1, 2 \) and compare the ratios with the bound of @thm-steepest-descent.
:::
::::

::: {.solution}
Here \( \x^{\star} = (1,1) \) and \( \kappa = 2 \), so the bound's factor is \( (\kappa-1)/(\kappa+1) = \tfrac13 \).

(a) \( \r^{(0)} = (2,1) \), \( \r\tp\r = 5 \), \( \r\tp\A\r = 2\cdot4 + 1 = 9 \), so \( t_0 = \tfrac59 \) and \( \x^{(1)} = \bigl(\tfrac{10}{9}, \tfrac59\bigr) \). Then \( \r^{(1)} = (2,1) - \A\x^{(1)} = \bigl(2 - \tfrac{20}{9},\ 1 - \tfrac59\bigr) = \bigl(-\tfrac29, \tfrac49\bigr) \). Now \( \r\tp\r = \tfrac{20}{81} \) and \( \r\tp\A\r = 2\cdot\tfrac{4}{81} + \tfrac{16}{81} = \tfrac{24}{81} \), so \( t_1 = \tfrac{20}{24} = \tfrac56 \) and
\[
\x^{(2)} = \Bigl(\tfrac{10}{9} - \tfrac56\cdot\tfrac29,\ \tfrac59 + \tfrac56\cdot\tfrac49\Bigr)
= \Bigl(\tfrac{25}{27}, \tfrac{25}{27}\Bigr).
\]

(b) The errors are \( (-1,-1) \), \( \bigl(\tfrac19, -\tfrac49\bigr) \), \( \bigl(-\tfrac{2}{27}, -\tfrac{2}{27}\bigr) \), with squared energy norms
\[
3, \qquad 2\cdot\tfrac1{81} + \tfrac{16}{81} = \tfrac{18}{81} = \tfrac29, \qquad
3\cdot\tfrac{4}{729} = \tfrac{4}{243}.
\]
The ratios are \( \tfrac{2}{27} \) and \( \tfrac{2}{27} \), both well below the bound's \( (\tfrac13)^2 = \tfrac19 \). The bound is not attained here because the initial residual does not split its weight equally between the two eigenvector directions, which is what equality in @lem-kantorovich demands.
:::

:::: {#exr-conjugate-gradient-b2}
[B2: Conjugate gradients by hand]

Let \( \A = \begin{pmatrix} 4 & 1 \\ 1 & 3\end{pmatrix} \), \( \b = (1, 2) \) and \( \x^{(0)} = (0,0) \). Run conjugate gradients to termination, and verify at each stage that the residuals are orthogonal and the directions \( \A \)-orthogonal.
::::

::: {.solution}
\( \det\A = 11 \), so \( \x^{\star} = \tfrac1{11}(3\cdot1 - 1\cdot2,\ -1\cdot1 + 4\cdot2) = \bigl(\tfrac1{11}, \tfrac7{11}\bigr) \).

*Step 0.* \( \r^{(0)} = \p^{(0)} = (1,2) \); \( (\r^{(0)})\tp\r^{(0)} = 5 \); \( \A\p^{(0)} = (6, 7) \); \( (\p^{(0)})\tp\A\p^{(0)} = 6 + 14 = 20 \). So \( \alpha_0 = \tfrac14 \), \( \x^{(1)} = \bigl(\tfrac14, \tfrac12\bigr) \) and
\[
\r^{(1)} = (1,2) - \tfrac14(6,7) = \bigl(-\tfrac12, \tfrac14\bigr).
\]
Check: \( (\r^{(1)})\tp\r^{(0)} = -\tfrac12 + \tfrac12 = 0 \). Then \( (\r^{(1)})\tp\r^{(1)} = \tfrac14 + \tfrac1{16} = \tfrac5{16} \), \( \beta_0 = \tfrac{5/16}{5} = \tfrac1{16} \) and
\[
\p^{(1)} = \bigl(-\tfrac12, \tfrac14\bigr) + \tfrac1{16}(1,2) = \bigl(-\tfrac7{16}, \tfrac38\bigr).
\]
Check: \( (\p^{(1)})\tp\A\p^{(0)} = \bigl(-\tfrac7{16}\bigr)6 + \tfrac38\cdot 7 = -\tfrac{42}{16} + \tfrac{42}{16} = 0 \).

*Step 1.* \( \A\p^{(1)} = \bigl(4(-\tfrac7{16}) + \tfrac38,\ -\tfrac7{16} + 3\cdot\tfrac38\bigr) = \bigl(-\tfrac{11}{8}, \tfrac{11}{16}\bigr) \), so
\[
(\p^{(1)})\tp\A\p^{(1)} = \tfrac{77}{128} + \tfrac{33}{128} = \tfrac{55}{64},
\qquad
\alpha_1 = \frac{5/16}{55/64} = \frac{4}{11} .
\]
Then
\[
\x^{(2)} = \bigl(\tfrac14, \tfrac12\bigr) + \tfrac4{11}\bigl(-\tfrac7{16}, \tfrac38\bigr)
= \bigl(\tfrac{11}{44} - \tfrac{7}{44},\ \tfrac{11}{22} + \tfrac{3}{22}\bigr)
= \bigl(\tfrac1{11}, \tfrac7{11}\bigr) = \x^{\star} ,
\]
and
\[
\r^{(2)} = \bigl(-\tfrac12, \tfrac14\bigr) - \tfrac4{11}\bigl(-\tfrac{11}{8}, \tfrac{11}{16}\bigr)
= \bigl(-\tfrac12 + \tfrac12,\ \tfrac14 - \tfrac14\bigr) = \0 .
\]
Two steps for a \( 2 \times 2 \) system, which is what @cor-cg-finite-termination allows.
:::

:::: {#exr-conjugate-gradient-b3}
[B3: Chebyshev by recurrence]

::: {.enumerate options="label=(\alph*)"}
1. Compute \( T_5 \) from @def-chebyshev-polynomials.
2. Evaluate \( T_5(1) \), \( T_5(-1) \) and \( T_5(0) \), and check them against @lem-chebyshev-extremal (a).
3. Evaluate \( T_5(2) \) from the polynomial, and check it against the closed formula of @lem-chebyshev-extremal (b).
:::
::::

::: {.solution}
(a) \( T_2 = 2x^2-1 \), \( T_3 = 2x(2x^2-1) - x = 4x^3-3x \), \( T_4 = 2x(4x^3-3x) - (2x^2-1) = 8x^4 - 8x^2 + 1 \), and
\[
T_5 = 2x(8x^4-8x^2+1) - (4x^3-3x) = 16x^5 - 20x^3 + 5x .
\]

(b) \( T_5(1) = 16 - 20 + 5 = 1 \), \( T_5(-1) = -1 \), \( T_5(0) = 0 \). All three have absolute value at most \( 1 \), as (a) of the lemma requires, and the first is the equality \( T_k(1) = 1 \).

(c) \( T_5(2) = 16\cdot32 - 20\cdot8 + 10 = 512 - 160 + 10 = 362 \). By the closed formula with \( z = 2 \), \( w = 2 + \sqrt3 \) and \( w^{-1} = 2 - \sqrt3 \), so
\[
T_5(2) = \tfrac12\bigl((2+\sqrt3)^5 + (2-\sqrt3)^5\bigr) .
\]
Expanding, \( (2\pm\sqrt3)^5 = 362 \pm 209\sqrt3 \), so the half-sum is \( 362 \). The two agree, and the growth is visible: \( T_5 \) is at most \( 1 \) on \( [-1,1] \) and already \( 362 \) at \( 2 \).
:::

### C. Going deeper

:::: {#exr-conjugate-gradient-c1}
[C1: Sharpness of Kantorovich]

Let \( a \ge c > 0 \) and let \( \A = \diag(a, c) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that for \( \y = (1, 1) \) the inequality of @lem-kantorovich is an equality.
2. Hence deduce that the constant \( (\kappa-1)/(\kappa+1) \) in @thm-steepest-descent cannot be replaced by any smaller one.
:::
::::

::: {.solution}
(a) \( \y\tp\A\y = a + c \), \( \y\tp\A^{-1}\y = a^{-1} + c^{-1} = (a+c)/(ac) \), and \( \y\tp\y = 2 \). So the left side is \( (a+c)^2/(ac) \) and the right side is \( \bigl((a+c)^2/(4ac)\bigr)\cdot 4 = (a+c)^2/(ac) \). They agree.

(b) Take \( \b = (a, c) \), so that \( \x^{\star} = (1,1) \), and \( \x^{(0)} = \bigl(1 - \tfrac1a,\ 1 - \tfrac1c\bigr) \), so that \( \boldsymbol{\varepsilon}^{(0)} = \bigl(-\tfrac1a, -\tfrac1c\bigr) \). Then \( \r^{(0)} = -\A\boldsymbol{\varepsilon}^{(0)} = (1,1) \), which is the vector of part (a). By the proof of @thm-steepest-descent the one-step ratio is
\[
1 - \frac{(\r\tp\r)^2}{(\r\tp\A\r)(\r\tp\A^{-1}\r)} = 1 - \frac{4ac}{(a+c)^2} = \Bigl(\frac{\kappa-1}{\kappa+1}\Bigr)^2 ,
\]
so the first step attains the bound exactly. Moreover \( \r^{(1)} = \r^{(0)} - t_0\A\r^{(0)} = (1 - t_0a,\ 1 - t_0c) \) with \( t_0 = 2/(a+c) \), giving \( \r^{(1)} = \bigl((c-a)/(a+c)\bigr)(1, -1) \); its two components again have equal absolute value, so part (a) applies to it up to sign and scale. That is enough: replacing \( \y \) by \( s\y \) multiplies both sides of @lem-kantorovich by \( s^4 \), and changing the sign of a coordinate changes neither side, since \( \A \) and \( \A^{-1} \) are diagonal. So every step attains the bound. Hence no constant smaller than \( (\kappa-1)/(\kappa+1) \) can work. (@exm-steepest-descent-sharp is the case \( a = 9 \), \( c = 1 \), rescaled.)
:::

:::: {#exr-conjugate-gradient-c2}
[C2: Finite termination, from polynomials]

Give a second proof of the second statement of @cor-cg-finite-termination — that \( d \) distinct eigenvalues force termination in at most \( d \) steps — using @eq-cg-polynomial-min instead of a dimension count. *Hint: consider \( q(x) = \prod_{i=1}^{d}(1 - x/\mu_i) \).*
::::

::: {.solution}
Let \( \mu_1, \dots, \mu_d \) be the distinct eigenvalues of \( \A \); all are positive, so \( q(x) = \prod_{i=1}^{d}(1 - x/\mu_i) \) is defined, has degree \( d \), and satisfies \( q(0) = 1 \). It is therefore admissible in @eq-cg-polynomial-min with \( k = d \). By Step 2 of the proof of @thm-cg-convergence,
\[
\norm{\boldsymbol{\varepsilon}^{(d)}}_{\A}^2 \le \sum_i\lambda_i\,q(\lambda_i)^2u_i^2 = 0 ,
\]
since every eigenvalue \( \lambda_i \) of \( \A \) equals some \( \mu_j \) and so is a root of \( q \). Hence \( \boldsymbol{\varepsilon}^{(d)} = \0 \) and \( \x^{(d)} = \x^{\star} \). (@eq-cg-polynomial-min was stated for iterates before termination; if the iteration stops earlier the conclusion is immediate.)
:::

:::: {#exr-conjugate-gradient-c3}
[C3: What preconditioning does to the spectrum]

Let \( \A, \M \in M_n(\nR) \) be symmetric positive definite and write \( \M = \C\C\tp \) with \( \C \) invertible, which is possible by @thm-cholesky.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \C^{-1}\A\C^{-\top} \) is symmetric positive definite.
2. Prove that \( \C^{-1}\A\C^{-\top} \) and \( \M^{-1}\A \) are similar, and deduce that their eigenvalues coincide.
3. Hence show that those eigenvalues are exactly the generalized eigenvalues of the pencil \( \A - \lambda\M \) in the sense of @def-generalized-eigenvalue, and say what @thm-cg-convergence then predicts for preconditioned conjugate gradients.
:::
::::

::: {.solution}
(a) It is symmetric because \( (\C^{-1}\A\C^{-\top})\tp = \C^{-1}\A\tp\C^{-\top} = \C^{-1}\A\C^{-\top} \). It is positive definite by @prp-congruence-positivity (b) applied with \( \S = \C^{-\top} \), which is invertible.

(b) Put \( \P = \C^{-\top} \), which is invertible. Then
\[
\P\bigl(\C^{-1}\A\C^{-\top}\bigr)\P^{-1}
= \C^{-\top}\C^{-1}\A\C^{-\top}\C\tp
= \C^{-\top}\C^{-1}\A
= (\C\C\tp)^{-1}\A = \M^{-1}\A ,
\]
using \( (\C\C\tp)^{-1} = \C^{-\top}\C^{-1} \). So the two matrices are similar, and similar matrices have the same characteristic polynomial (@thm-charpoly-similarity-invariant), hence the same eigenvalues with multiplicity.

(c) By @def-generalized-eigenvalue, \( \lambda \) is a generalized eigenvalue of the pencil \( \A - \lambda\M \) exactly when \( \A\v = \lambda\M\v \) for some \( \v \ne \0 \), that is when \( \M^{-1}\A\v = \lambda\v \); so the generalized eigenvalues are the eigenvalues of \( \M^{-1}\A \), which by (b) are those of \( \C^{-1}\A\C^{-\top} \). Running conjugate gradients on \( (\C^{-1}\A\C^{-\top})\y = \C^{-1}\b \) therefore converges at the rate of @thm-cg-convergence with \( \kappa \) replaced by the ratio of the largest to the smallest generalized eigenvalue of \( \A \) relative to \( \M \). Choosing \( \M \) close to \( \A \) makes that ratio close to \( 1 \); choosing \( \M = \A \) makes it exactly \( 1 \), at the cost of having to solve with \( \A \).
:::
