# Least Squares in Practice

Chapter 10 solved the least-squares problem twice. Section 4 of that chapter produced the normal equations \( \A^{*}\A\x = \A^{*}\b \) (@thm-least-squares), and Section 8 rewrote them, once a \( \Q\R \) factorization was available, as the triangular system \( \R\x = \Q^{*}\b \). It then recommended the second route and postponed the reason: "forming \( \A^{*}\A \) squares the sensitivity of the problem to rounding, while \( (\dagger) \) never forms that product at all. Chapter 23 makes 'sensitivity' precise and proves the comparison; here we record only the practice."

Chapter 15 supplied half of the reason. Its @thm-normal-equations-squares-conditioning proved \( \kappa_2(\A^{*}\A) = \kappa_2(\A)^2 \) and then listed what was still missing: the conditioning of the fitting problem itself, which involves the residual; the arithmetic, which needed a model; and the comparison of the two algorithms in digits. Sections 1 and 2 of this chapter built the model and the vocabulary. This section pays the three debts, in that order, and ends with the reason the reflections of Chapter 10 are the right way to produce \( \Q \) and \( \R \).

Throughout, \( F = \nR \) or \( F = \nC \), \( \A \in M_{m \times n}(F) \) with \( m \ge n \) and \( \rank\A = n \), and \( \b \in F^m \) is non-zero. By @cor-least-squares-unique there is then exactly one least-squares solution \( \x \), and \( \A^{*}\A \) is invertible. All norms are \( \norm{\cdot}_2 \) unless a subscript says otherwise.

## How sensitive is the problem?

Before any algorithm is judged, the problem has to be measured. Write

\[
\r = \b - \A\x, \qquad \A\x = P_{\col(\A)}\b ,
\]

the residual and the projection of @thm-least-squares (b). Since \( \r \perp \col(\A) \) and \( \A\x \in \col(\A) \), Pythagoras (@thm-pythagoras) gives \( \norm{\b}^2 = \norm{\A\x}^2 + \norm{\r}^2 \). So there is a unique \( \theta \in [0, \pi/2] \) with

\[
\cos\theta = \frac{\norm{\A\x}}{\norm{\b}}, \qquad
\sin\theta = \frac{\norm{\r}}{\norm{\b}} ,
\]{#eq-ls-angle}

the angle between \( \b \) and the column space of \( \A \). It is \( 0 \) exactly when the system is consistent and \( \pi/2 \) exactly when \( \A^{*}\b = \0 \), in which case \( \x = \0 \) and no relative error can be spoken of. **We assume \( \theta < \pi/2 \) throughout**, so \( \x \ne \0 \).

One number is now missing from Chapter 15's account, and @eq-ls-angle supplies it. Here is the sensitivity of \( \x \) to a perturbation of the data.

:::: {#thm-least-squares-conditioning}
[Conditioning of the Least-Squares Problem]

Let \( \A \in M_{m \times n}(F) \) have rank \( n \le m \), let \( \b \ne \0 \), let \( \x \) be the least-squares solution of \( \A\z = \b \), and let \( \theta < \pi/2 \) be as in @eq-ls-angle. Let \( \E \in M_{m \times n}(F) \) and \( \f \in F^m \), and for real \( t \) near \( 0 \) let \( \x(t) \) be the least-squares solution of \( (\A + t\E)\z = \b + t\f \). Then \( \x(t) \) is defined and differentiable near \( t = 0 \), with \( \x(0) = \x \), and

\[
\frac{\norm{\x'(0)}}{\norm{\x}}
\ \le\ \kappa_2(\A)\Bigl(\varepsilon_{\A} + \frac{\varepsilon_{\b}}{\cos\theta}\Bigr)
\ +\ \kappa_2(\A)^2\,\varepsilon_{\A}\tan\theta ,
\]

where \( \varepsilon_{\A} = \norm{\E}/\norm{\A} \) and \( \varepsilon_{\b} = \norm{\f}/\norm{\b} \).
::::

::: {.idea}
The least-squares solution is \( \x(t) = \N(t)^{-1}\A(t)^{*}\b(t) \) with \( \N(t) = \A(t)^{*}\A(t) \), which is a differentiable function of \( t \) because \( \N(0) \) is invertible. Rather than differentiate that formula, differentiate the equation \( \N(t)\x(t) = \A(t)^{*}\b(t) \) it comes from: the product rule gives three terms, two of them combine into \( \E^{*}(\b - \A\x) = \E^{*}\r \), and the residual appears by itself. Then read every norm off a singular value decomposition: \( \norm{(\A^{*}\A)^{-1}} = \sigma_n^{-2} \) is where the square comes from, and the only inequality used to finish is \( \sigma_1\norm{\x} \ge \norm{\A\x} = \norm{\b}\cos\theta \).
:::

::: {.proof}
Write \( \A(t) = \A + t\E \), \( \b(t) = \b + t\f \) and \( \N(t) = \A(t)^{*}\A(t) \). Every entry of \( \N(t) \) is a polynomial in \( t \), so \( \N \) is differentiable in the sense of @def-matrix-valued-derivative, and \( \N(0) = \A^{*}\A \) is invertible by @cor-least-squares-unique (c). By @thm-derivative-of-inverse, \( \N(t) \) is invertible on an open interval around \( 0 \) and \( t \mapsto \N(t)^{-1} \) is differentiable there. On that interval \( \rank\A(t) = n \), again by @cor-least-squares-unique, so @thm-least-squares has the unique solution
\[
\x(t) = \N(t)^{-1}\A(t)^{*}\b(t) ,
\]
differentiable by @lem-matrix-product-rule. (Conjugation is applied entrywise and commutes with differentiation in the real variable \( t \), so \( (\A(t)^{*})' = \E^{*} \).)

Differentiate the identity \( \N(t)\x(t) = \A(t)^{*}\b(t) \) at \( t = 0 \) with @lem-matrix-product-rule. Since \( \N'(0) = \E^{*}\A + \A^{*}\E \),
\[
(\E^{*}\A + \A^{*}\E)\x + \A^{*}\A\,\x'(0) = \E^{*}\b + \A^{*}\f .
\]
Move the first bracket across and collect the two terms carrying \( \E^{*} \):
\[
\A^{*}\A\,\x'(0) = \E^{*}(\b - \A\x) - \A^{*}(\E\x) + \A^{*}\f = \E^{*}\r - \A^{*}(\E\x) + \A^{*}\f .
\]
Hence
\[
\x'(0) = (\A^{*}\A)^{-1}\E^{*}\r \;-\; (\A^{*}\A)^{-1}\A^{*}(\E\x) \;+\; (\A^{*}\A)^{-1}\A^{*}\f .
\tag{$\ast$}
\]

Now the two norms. Write \( \A = \U\vSigma\V^{*} \) as in @thm-svd, with \( \sigma_1 \ge \dots \ge \sigma_n > 0 \). As in the proof of @thm-normal-equations-squares-conditioning, \( \A^{*}\A = \V\diag(\sigma_1^2, \dots, \sigma_n^2)\V^{*} \), so
\[
(\A^{*}\A)^{-1} = \V\diag(\sigma_1^{-2}, \dots, \sigma_n^{-2})\V^{*},
\qquad
(\A^{*}\A)^{-1}\A^{*} = \V\vSigma^{+}\U^{*} ,
\]
where \( \vSigma^{+} \) is the \( n \times m \) matrix with \( \sigma_1^{-1}, \dots, \sigma_n^{-1} \) on its diagonal — the second identity because \( \diag(\sigma_i^{-2})\vSigma^{*} = \vSigma^{+} \). Unitary factors do not change singular values, rectangular ones included: for unitary \( \U_1, \V_1 \) of the right sizes, \( (\U_1\M\V_1)^{*}(\U_1\M\V_1) = \V_1^{*}(\M^{*}\M)\V_1 \) is unitarily similar to \( \M^{*}\M \), so the two have the same eigenvalues and @def-singular-values reads the same singular values off them. Hence by @thm-operator-norm-formulas (c),
\[
\norm{(\A^{*}\A)^{-1}} = \sigma_n^{-2},
\qquad
\norm{(\A^{*}\A)^{-1}\A^{*}} = \sigma_n^{-1} .
\]
Applying these to \( (\ast) \) with @thm-operator-norm-properties (a),
\[
\norm{\x'(0)} \ \le\ \frac{\norm{\E}\,\norm{\r}}{\sigma_n^{2}}
\;+\; \frac{\norm{\E}\,\norm{\x}}{\sigma_n}
\;+\; \frac{\norm{\f}}{\sigma_n} .
\]

Divide by \( \norm{\x} \) and use \( \norm{\A} = \sigma_1 \) (@thm-operator-norm-formulas (c)) and \( \kappa_2(\A) = \sigma_1/\sigma_n \) (@def-condition-number). The middle term becomes \( \norm{\E}/\sigma_n = \kappa_2(\A)\varepsilon_{\A} \) exactly. For the other two, note that \( \sigma_1\norm{\x} \ge \norm{\A\x} = \norm{\b}\cos\theta \), so
\[
\frac{\norm{\r}}{\sigma_1\norm{\x}} \le \frac{\norm{\b}\sin\theta}{\norm{\b}\cos\theta} = \tan\theta,
\qquad
\frac{\norm{\b}}{\sigma_1\norm{\x}} \le \frac{1}{\cos\theta} .
\]
Therefore
\[
\begin{aligned}
\frac{\norm{\E}\norm{\r}}{\sigma_n^2\norm{\x}}
 &= \frac{\sigma_1^2}{\sigma_n^2}\cdot\frac{\norm{\E}}{\sigma_1}\cdot\frac{\norm{\r}}{\sigma_1\norm{\x}}
 \le \kappa_2(\A)^2\varepsilon_{\A}\tan\theta , \\
\frac{\norm{\f}}{\sigma_n\norm{\x}}
 &= \frac{\sigma_1}{\sigma_n}\cdot\frac{\norm{\f}}{\norm{\b}}\cdot\frac{\norm{\b}}{\sigma_1\norm{\x}}
 \le \frac{\kappa_2(\A)\varepsilon_{\b}}{\cos\theta} .
\end{aligned}
\]
Adding the three estimates gives the stated bound. This proves the theorem.
:::

**What is linearized, and what is not.** The theorem itself is exact: it bounds a derivative, and no term has been discarded. What is an approximation is the use one makes of it. Reading it as

\[
\frac{\norm{\Delta\x}}{\norm{\x}} \ \lesssim\ \Bigl[\kappa_2(\A)\bigl(1 + \tfrac{1}{\cos\theta}\bigr) + \kappa_2(\A)^2\tan\theta\Bigr]\,\varepsilon
\]{#eq-ls-first-order}

for data perturbed by \( \norm{\Delta\A} \le \varepsilon\norm{\A} \) and \( \norm{\Delta\b} \le \varepsilon\norm{\b} \) drops a remainder of size \( O(\varepsilon^2) \), exactly as @thm-relative-error-bound (b) drops the factor \( 1/(1-r) \). For the \( \varepsilon \approx 10^{-16} \) of the floating-point model that remainder is invisible, and every statement below that carries a \( \lesssim \) is a statement of this kind.

Two readings of the bound matter.

- **When the residual is zero**, \( \theta = 0 \) and the bound is \( 2\kappa_2(\A)\varepsilon \): the least-squares problem is exactly as sensitive as a square linear system with the same condition number. A square invertible \( \A \) is always this case, and @thm-relative-error-bound is recovered.
- **When the residual is large**, the term \( \kappa_2(\A)^2\tan\theta \) dominates the bound, and what it measures belongs to the *problem*: no algorithm can return an answer more accurate than data of that quality determine. This is the sentence Chapter 15 §08 promised, where the least-squares problem was said to have "a sensitivity that depends on \( \kappa_2(\A) \), on the residual \( \norm{\A\x^{+} - \b} \) and on the angle between \( \b \) and \( \col(\A) \)". @exr-numerical-least-squares-c1 exhibits data on which the \( \kappa_2(\A)^2\varepsilon_{\A}\tan\theta \) term is attained exactly, so it is not an artifact of the estimates.

::: {.check}
Take \( m = n \) with \( \A \) invertible. What does @eq-ls-angle give for \( \theta \), and what does @eq-ls-first-order reduce to? Compare with @thm-relative-error-bound.
:::

::: {.solution}
For an invertible square \( \A \) the system \( \A\z = \b \) is consistent, so its least-squares solution has residual \( \r = \0 \) and @eq-ls-angle gives \( \sin\theta = 0 \), that is \( \theta = 0 \). Then \( \cos\theta = 1 \) and \( \tan\theta = 0 \), and @eq-ls-first-order reads \( \norm{\Delta\x}/\norm{\x} \lesssim 2\kappa(\A)\varepsilon \). That is @thm-relative-error-bound (a) and (b) added together, with the factor \( 1/(1-r) \) replaced by the \( O(\varepsilon^2) \) that the linearization discards. The square case carries no \( \kappa^2 \) at all.
:::

## Two routes, and the digits they lose

The problem is measured; now the two algorithms. Both are run in the arithmetic of @def-floating-point-model, with \( u \) the unit roundoff and \( \gamma_k = ku/(1-ku) \) the constant of @lem-gamma-bound.

The **normal-equation route** forms \( \C = \fl(\A^{*}\A) \) and \( \d = \fl(\A^{*}\b) \) entry by entry as inner products, then solves \( \C\z = \d \). The matrix it hands to the solver need **not** be positive definite. The exact \( \A^{*}\A \) is: \( \x^{*}\A^{*}\A\x = \norm{\A\x}^2 > 0 \) for \( \x \ne \0 \), the columns of \( \A \) being independent. The computed \( \C \) is Hermitian, only one triangle of it being formed, but its eigenvalues are those of \( \A^{*}\A \) displaced by the rounding, and the smallest of them, \( \sigma_n(\A)^2 \), can be displaced past \( 0 \) — @exm-normal-equations-fail below exhibits a \( \C \) that comes out singular, on which the Cholesky factorization of @thm-cholesky fails outright. **When \( \C \) is positive definite** — which it is while the rounding stays below \( \sigma_n(\A)^2 \) — Cholesky, and the analysis Section 2 gives it, apply.

The cost is \( mn^2 \) flops to form the product — there are \( \tfrac12n(n+1) \) entries to compute, each an inner product of length \( m \) costing \( 2m \) flops — plus \( \tfrac13n^3 \) for the factorization (@prp-lu-cost (c)) and \( 2n^2 \) for the two triangular solves. The **\( \Q\R \) route** never forms that product: it computes a factorization \( \A = \Q\R \) by reflections (@thm-qr-householder), applies \( \Q^{*} \) to \( \b \), and solves the triangular system \( \R\x = \Q^{*}\b \) by back substitution, which @thm-triangular-solve-backward-error showed to be backward stable. Its cost is \( 2mn^2 - \tfrac23 n^3 \) flops by a sum of the same kind as @prp-lu-cost, which we do not write out: about twice the first when \( m \gg n \).

The rule of thumb of @thm-forward-from-backward says: forward relative error \( \le \) condition number \( \times \) backward relative error. The two routes solve *different problems*, and that is the whole story. The first solves a square linear system whose matrix is \( \A^{*}\A \), of condition number \( \kappa_2(\A)^2 \) by @thm-normal-equations-squares-conditioning. The second solves the least-squares problem itself, of sensitivity given by @thm-least-squares-conditioning. Here is the comparison. Part (a) is @thm-forward-from-backward applied to the system \( \A^{*}\A\x = \A^{*}\b \), except that here the right-hand side is perturbed as well, so we give the short direct argument instead of appealing to it.

:::: {#thm-normal-equations-lose-twice}
[The Normal Equations Lose Twice the Digits]

Let \( \A \in M_{m \times n}(F) \) have rank \( n \le m \), let \( \b \ne \0 \), let \( \x \) be the least-squares solution and let \( \theta < \pi/2 \) be as in @eq-ls-angle. Work in the model of @def-floating-point-model, and suppose \( mu \le \tfrac12 \).

::: {.enumerate options="label=(\alph*)"}
1. **(Normal equations.)** Suppose \( \C = \fl(\A^{*}\A) \) and \( \d = \fl(\A^{*}\b) \) are formed by inner products, and that \( \C\z = \d \) is then solved by a method that is backward stable in the sense of @def-backward-stable, so that the computed \( \widehat{\x} \) satisfies \( (\C + \Delta\C)\widehat{\x} = \d + \Delta\d \) with \( \norm{\Delta\C} \le c_su\norm{\C} \) and \( \norm{\Delta\d} \le c_su\norm{\d} \). Then there is a constant \( c \), depending only on \( m \), \( n \) and \( c_s \) and of size \( O(mn) \), such that if \( c\,u\,\kappa_2(\A)^2 < 1 \) then
   \[
   \frac{\norm{\widehat{\x} - \x}}{\norm{\x}}
   \ \le\ \frac{c\,u\,\kappa_2(\A)^2\bigl(1 + \tfrac{1}{\cos\theta}\bigr)}{1 - c\,u\,\kappa_2(\A)^2} .
   \]
   The bound carries \( \kappa_2(\A)^2 \) **even when the residual is zero**.
2. **(A backward stable least-squares solver.)** Suppose instead that \( \widehat{\x} \) is the exact least-squares solution of \( (\A + \Delta\A)\z = \b + \Delta\b \) for some \( \Delta\A, \Delta\b \) with \( \norm{\Delta\A} \le c'u\norm{\A} \) and \( \norm{\Delta\b} \le c'u\norm{\b} \). Then, to first order in \( u \) as in @eq-ls-first-order,
   \[
   \frac{\norm{\widehat{\x} - \x}}{\norm{\x}}
   \ \lesssim\ c'u\Bigl[\kappa_2(\A)\bigl(1 + \tfrac{1}{\cos\theta}\bigr) + \kappa_2(\A)^2\tan\theta\Bigr] .
   \]
:::
::::

::: {.idea}
For (a), the two sources of error — forming the product, and solving the system — are both perturbations of the *exact* normal equations, and both are bounded by a constant times \( u\norm{\A}^2 \) or \( u\norm{\A}\norm{\b} \). Subtract the exact equations from the perturbed ones and multiply by \( (\A^{*}\A)^{-1} \), whose norm is \( \sigma_n^{-2} \): the two factors of \( \sigma_1/\sigma_n \) appear there and nowhere else. The one nuisance is that the estimate produces \( \norm{\widehat{\x}} \) rather than \( \norm{\x} \); subadditivity of the norm (@cor-triangle-inequality) trades one for the other at the cost of the denominator, exactly as in @thm-relative-error-bound (b). For (b) there is nothing to do: the hypothesis says the computed answer is the exact answer to perturbed data, which is what @thm-least-squares-conditioning measures.
:::

::: {.proof}
*(a).* We argue over \( \nR \), the field in which @thm-inner-product-backward-error is stated; over \( \nC \) each complex multiplication and addition is a bounded number of real ones, and the same argument gives the same bound with a larger constant \( c \). Write \( \a_1, \dots, \a_n \) for the columns of \( \A \), so that \( (\A^{*}\A)_{ij} = \a_i^{*}\a_j \) and \( (\A^{*}\b)_i = \a_i^{*}\b \), each an inner product of length \( m \). By @thm-inner-product-backward-error, \( \fl(\a_i^{*}\a_j) = (\a_i + \Delta\a)^{*}\a_j \) with \( \lvert\Delta\a\rvert \le \gamma_m\lvert\a_i\rvert \) entrywise, so
\[
\bigl\lvert c_{ij} - \a_i^{*}\a_j \bigr\rvert \le \gamma_m \lvert\a_i\rvert\tp\lvert\a_j\rvert \le \gamma_m\norm{\a_i}\norm{\a_j} ,
\]
the last step by Cauchy–Schwarz (@thm-cauchy-schwarz). Summing squares and using \( \norm{\M} \le \norm{\M}_F \) — true because \( \norm{\M}_F^2 = \tr(\M^{*}\M) \) is the sum of the eigenvalues of \( \M^{*}\M \), hence of the \( \sigma_i(\M)^2 \), while \( \norm{\M} = \sigma_1(\M) \) by @thm-operator-norm-formulas (c) —
\[
\norm{\C - \A^{*}\A} \le \norm{\C - \A^{*}\A}_F \le \gamma_m\Bigl(\sum_i\norm{\a_i}^2\Bigr) = \gamma_m\norm{\A}_F^2 \le n\gamma_m\norm{\A}^2 .
\]
The same argument on \( \d \) gives \( \norm{\d - \A^{*}\b} \le \gamma_m\norm{\b}\norm{\A}_F \le \sqrt n\,\gamma_m\norm{\A}\norm{\b} \).

Now add the solver's backward error. Put \( \vDelta = (\C + \Delta\C) - \A^{*}\A \) and \( \h = (\d + \Delta\d) - \A^{*}\b \). Since \( \norm{\C} \le (1 + n\gamma_m)\norm{\A}^2 \) and \( \norm{\d} \le (1 + \sqrt n\gamma_m)\norm{\A}\norm{\b} \),
\[
\norm{\vDelta} \le c\,u\norm{\A}^2,
\qquad
\norm{\h} \le c\,u\norm{\A}\norm{\b},
\]
with \( c = 2nm + c_s(1 + 2nm) \) serving, say, since the hypothesis \( mu \le \tfrac12 \) gives \( \gamma_m \le 2mu \), and \( \sqrt n \le n \).

The exact solution satisfies \( \A^{*}\A\x = \A^{*}\b \) and the computed one satisfies \( (\A^{*}\A + \vDelta)\widehat{\x} = \A^{*}\b + \h \). Subtracting,
\[
\A^{*}\A(\widehat{\x} - \x) = \h - \vDelta\widehat{\x},
\qquad
\norm{\widehat{\x} - \x} \le \sigma_n^{-2}\bigl(c\,u\norm{\A}\norm{\b} + c\,u\norm{\A}^2\norm{\widehat{\x}}\bigr) ,
\]
using \( \norm{(\A^{*}\A)^{-1}} = \sigma_n^{-2} \) from the proof of @thm-least-squares-conditioning. Divide by \( \norm{\x} \), write \( \rho = \norm{\widehat{\x} - \x}/\norm{\x} \), and use \( \sigma_1\norm{\x} \ge \norm{\b}\cos\theta \) together with \( \norm{\widehat{\x}} \le \norm{\x}(1 + \rho) \):
\[
\rho \ \le\ c\,u\,\kappa_2(\A)^2\Bigl(\frac{1}{\cos\theta} + 1 + \rho\Bigr) .
\]
Since \( c\,u\,\kappa_2(\A)^2 < 1 \) we may collect the \( \rho \) terms and divide, which gives the stated bound. Nothing in the argument used \( \r \), so it holds for \( \theta = 0 \) as it stands.

*(b).* By hypothesis \( \widehat{\x} = \x(1) \) for the family of @thm-least-squares-conditioning with \( \E = \Delta\A \) and \( \f = \Delta\b \), and \( \varepsilon_{\A}, \varepsilon_{\b} \le c'u \). The stated bound is @eq-ls-first-order for that family. This proves the theorem.
:::

**In digits.** A relative error of \( \eta \) means about \( \log_{10}(1/\eta) \) correct decimal digits, and an arithmetic with unit roundoff \( u \approx 10^{-16} \) offers about \( 16 \) of them. Part (a) says the normal-equation route returns an answer with relative error about \( u\kappa_2(\A)^2 \): it **loses about \( 2\log_{10}\kappa_2(\A) \) digits**, whatever the residual. Part (b) says a backward stable least-squares solver returns an answer with relative error about \( u\kappa_2(\A) \) when the residual is small, and so **loses about \( \log_{10}\kappa_2(\A) \) digits**.

The comparison Chapter 15 §08 left open has two halves, and only one of them is settled here. The half that is proved is the *implication*: **a** backward stable least-squares solver loses about \( \log_{10}\kappa_2(\A) \) digits, while forming \( \A^{*}\A \) loses about twice that — and part (a), which carries no stability hypothesis at all, is unconditional.

The half that is **not** proved is that the reflection route of Chapter 10 §08 supplies such a solver. That is the accumulated statement of the remark after @thm-householder-backward-stable below, which this book records with credit and does not prove; what @thm-householder-backward-stable itself proves is the backward stability of **one** reflection. A further qualification is the content of the next warning.

::: {.warning}
**The two-versus-one comparison is a small-residual statement, and the reason is not symmetric.** For a large residual the bound in (b) also carries a \( \kappa_2(\A)^2 \), through the term \( \kappa_2(\A)^2\tan\theta \). The difference is *where that square comes from*. In (b) it is the sensitivity of the problem, certified by @thm-least-squares-conditioning, and no method whatever can avoid it. In (a) it is manufactured by the algorithm: it is there when \( \theta = 0 \), where the problem's own sensitivity is only \( \kappa_2(\A) \). So the honest form of the comparison is: **a backward stable method loses what the problem costs; forming \( \A^{*}\A \) loses \( \kappa_2(\A) \) times more than that whenever \( \tan\theta \lesssim 1/\kappa_2(\A) \), and never less.**
:::

::: {#exm-normal-equations-fail}
[A matrix where one route survives and the other does not]

Let \( \varepsilon > 0 \) and
\[
\A = \begin{pmatrix} 1 & 1 \\ \varepsilon & 0 \\ 0 & \varepsilon \end{pmatrix},
\qquad
\b = \begin{pmatrix} 1 \\ 2\varepsilon \\ -\varepsilon \end{pmatrix} .
\]
Find \( \kappa_2(\A) \), the exact least-squares solution and the residual. Then run both routes in the model with \( u = 2^{-53} \), for \( \varepsilon = 10^{-6} \) and for \( \varepsilon = 10^{-9} \), and compare.
:::

::: {.solution}
*Exact data.* \( \A\tp\A = \begin{psmallmatrix} 1 + \varepsilon^2 & 1 \\ 1 & 1 + \varepsilon^2\end{psmallmatrix} \), which sends \( (1,1) \) to \( (2+\varepsilon^2)(1,1) \) and \( (1,-1) \) to \( \varepsilon^2(1,-1) \). So its eigenvalues are \( 2 + \varepsilon^2 \) and \( \varepsilon^2 \), the singular values of \( \A \) are \( \sqrt{2+\varepsilon^2} \) and \( \varepsilon \), and
\[
\kappa_2(\A) = \frac{\sqrt{2+\varepsilon^2}}{\varepsilon} .
\]
Also \( \A(2, -1) = (2 - 1,\ 2\varepsilon,\ -\varepsilon) = \b \), so the system is **consistent**: the least-squares solution is \( \x = (2, -1) \) exactly, the residual is \( \r = \0 \), and \( \theta = 0 \). By @thm-least-squares-conditioning the problem's sensitivity is exactly \( 2\kappa_2(\A) \) — there is no \( \kappa_2^2 \) in the problem at all.

*\( \varepsilon = 10^{-6} \).* Here \( \kappa_2(\A) = 1.4142136 \cdot 10^{6} \), so \( u\kappa_2(\A) = 1.6\cdot10^{-10} \) and \( u\kappa_2(\A)^2 = 2.2\cdot10^{-4} \). Forming the product rounds \( 1 + \varepsilon^2 = 1 + 10^{-12} \) to \( 1.0000000000010000889 \); the last four digits are the rounding, and they are a relative perturbation of about \( 10^{-4} \) in the *difference* \( \varepsilon^2 \) that carries the small eigenvalue. Cholesky and the two triangular solves then return
\[
\widehat{\x} = (1.99983348134991,\ -0.99983348134991) ,
\]
a relative error of \( \norm{\widehat{\x} - \x}/\norm{\x} = 1.05\cdot10^{-4} \) — about four correct digits out of sixteen, and within a factor of \( 2 \) of the bound \( u\kappa_2(\A)^2 = 2.2\cdot10^{-4} \). (Entry by entry the relative errors are \( 8.3\cdot10^{-5} \) and \( 1.7\cdot10^{-4} \); it is the \( 2 \)-norm figure that the theorem bounds.) The reflection route returns \( (2, -1) \), every digit correct.

*\( \varepsilon = 10^{-9} \).* Now \( \kappa_2(\A) = 1.4142136\cdot10^{9} \) and \( u\kappa_2(\A)^2 = 222 \), so part (a) promises nothing at all — and nothing is what it delivers. Since \( \varepsilon^2 = 10^{-18} \) is below \( u \), the computed product is
\[
\C = \fl(\A\tp\A) = \begin{pmatrix} 1 & 1 \\ 1 & 1\end{pmatrix},
\]
a **singular** matrix: its Cholesky factorization (@thm-cholesky) fails at the second pivot, and the route cannot even be run. The reflection route again returns \( (2, -1) \).

*The bound is an upper bound.* For \( \varepsilon = 10^{-9} \) the reflection route is entitled to lose \( \log_{10}\kappa_2(\A) \approx 9 \) digits and in fact loses none: the answer is exactly representable and the arithmetic happens to reach it. Part (b) is a worst case over perturbations, as @thm-relative-error-bound was. Part (a) is an upper bound too, and it is not attained exactly either; what this example shows is that it is not a pessimistic one — the normal-equation route does lose its \( 2\log_{10}\kappa_2(\A) \) digits here, to within a factor of \( 2 \) in the error.
:::

::: {.warning}
**Forming \( \A^{*}\A \) is not forbidden, it is limited.** If \( \kappa_2(\A) = 10^{3} \) then \( u\kappa_2(\A)^2 \approx 10^{-10} \), and the normal equations return ten correct digits for half the arithmetic. The rule is quantitative, not moral: the route is safe exactly while \( u\kappa_2(\A)^2 \) is small enough for the purpose, and it collapses — as @exm-normal-equations-fail shows — once \( \kappa_2(\A) \) approaches \( u^{-1/2} \approx 10^{8} \). What is never acceptable is forming the product without knowing which side of that threshold one is on.
:::

## Why the reflection route is the stable one

Part (b) above assumed a backward stable least-squares solver. That hypothesis has to be earned, and earning it is what Chapter 10 §08's reflections are for. The claim to be supported is: applying a Householder reflection by the formula

\[
\H_{\w}\v = \v - \frac{2\inner{\v}{\w}}{\norm{\w}^2}\,\w
\]{#eq-reflection-applied}

of Chapter 10 §08 — **applying it, never forming the matrix** — commits a backward error of size \( u \), with no dependence on the conditioning of anything. Here is that statement, proved.

:::: {#thm-householder-backward-stable}
[Backward Stability of One Reflection]

Work in the model of @def-floating-point-model over \( \nR \), and suppose \( (10m+16)u \le \tfrac14 \). Let \( \w \in \nR^m \) be non-zero and let \( \H = \H_{\w} \) be the reflection of @def-householder-reflection, and suppose \( \w \) and the input are stored exactly.

::: {.enumerate options="label=(\alph*)"}
1. For \( \v \in \nR^m \), let \( \widehat{\y} \) be the vector computed from \( \v \) and \( \w \) by @eq-reflection-applied. Then
   \[
   \widehat{\y} = \H(\v + \Delta\v),
   \qquad
   \norm{\Delta\v}_2 \le (10m + 16)\,u\,\norm{\v}_2 .
   \]
2. For \( \A \in M_{m \times n}(\nR) \), let \( \widehat{\B} \) be the matrix whose columns are computed from those of \( \A \) in this way. Then
   \[
   \widehat{\B} = \H(\A + \Delta\A),
   \qquad
   \norm{\Delta\A}_F \le (10m+16)\,u\,\norm{\A}_F .
   \]
:::
::::

::: {.idea}
Three quantities are computed before anything is subtracted: \( \norm{\w}^2 \), the inner product \( \inner{\v}{\w} \), and their quotient \( \beta \). Each is an inner product or a division, so @thm-inner-product-backward-error and @lem-gamma-bound bound them at once, and the crude estimate \( \lvert\beta\rvert \le 2\norm{\v}/\norm{\w} \) — which is Cauchy–Schwarz and nothing more — keeps every error proportional to \( \norm{\v} \), not to \( \norm{\v}/\norm{\w} \). Then the forward error \( \norm{\widehat\y - \H\v} \) is converted into a backward error for free, because \( \H \) is an isometry and its own inverse: \( \Delta\v = \H(\widehat\y - \H\v) \) has exactly the same length. Part (b) is part (a) column by column, since the Frobenius norm adds the columns in squares.
:::

::: {.proof}
*(a).* Write \( \nu = \norm{\w}_2 \), \( \beta = 2\inner{\v}{\w}/\nu^2 \), so that \( \H\v = \v - \beta\w \), and abbreviate \( \gamma_k = ku/(1-ku) \). The hypothesis \( (10m+16)u \le \tfrac14 \) gives in particular \( (m+2)u \le \tfrac14 \), so \( \gamma_k \le \tfrac43 ku \le \tfrac13 \) for every \( k \le m+2 \).

**Step 1: the two inner products.** The computed \( s = \fl(\w^{*}\w) \) is a sum of \( m \) non-negative terms \( w_i^2 \), each carrying at most \( m \) rounding factors, so by @lem-gamma-bound \( s = \sum_i w_i^2(1 + \theta_i) \) with \( \lvert\theta_i\rvert \le \gamma_m \); as every \( w_i^2 \ge 0 \) this gives \( s = \nu^2(1+\theta) \) with \( \lvert\theta\rvert \le \gamma_m \). By @thm-inner-product-backward-error the computed \( p = \fl(\v^{*}\w) \) satisfies \( p = \inner{\v}{\w} + \eta \) with
\[
\lvert\eta\rvert \le \gamma_m\lvert\v\rvert\tp\lvert\w\rvert \le \gamma_m\norm{\v}\nu ,
\]
by Cauchy–Schwarz (@thm-cauchy-schwarz).

**Step 2: the coefficient.** The computed \( \widehat\beta \) is \( (2p/s) \) times two rounding factors, so \( \widehat\beta = (2p/s)(1+\theta_2) \) with \( \lvert\theta_2\rvert \le \gamma_2 \), by @lem-gamma-bound. Writing \( 2p/s = (\beta + \zeta)/(1+\theta) \) with \( \zeta = 2\eta/\nu^2 \) and \( \lvert\zeta\rvert \le 2\gamma_m\norm{\v}/\nu \),
\[
\Bigl\lvert\frac{1+\theta_2}{1+\theta} - 1\Bigr\rvert
\le \frac{\gamma_m + \gamma_2}{1 - \gamma_m} \le \tfrac32(\gamma_m + \gamma_2) \le 2(m+2)u ,
\]
using \( 1 - \gamma_m \ge \tfrac23 \) and \( \gamma_k \le \tfrac43 ku \); in particular the factor itself has modulus at most \( 2 \). Since \( \lvert\beta\rvert \le 2\norm{\v}/\nu \) by Cauchy–Schwarz,
\[
\lvert\widehat\beta - \beta\rvert
\le \lvert\beta\rvert\cdot 2(m+2)u + 2\lvert\zeta\rvert
\le \frac{\norm{\v}}{\nu}\bigl(4(m+2)u + 6mu\bigr)
\le K\,u\,\frac{\norm{\v}}{\nu},
\]
with \( K = 10m + 8 \). In particular \( \lvert\widehat\beta\rvert \le 3\norm{\v}/\nu \), since \( Ku \le (10m+16)u \le \tfrac14 \).

**Step 3: the subtraction.** Entry \( i \) is computed as \( \widehat y_i = (v_i - \widehat\beta w_i(1+\delta_i))(1+\delta_i') \) with \( \lvert\delta_i\rvert, \lvert\delta_i'\rvert \le u \). Subtracting \( (\H\v)_i = v_i - \beta w_i \) and regrouping,
\[
\widehat y_i - (\H\v)_i = (v_i - \widehat\beta w_i)\delta_i' + (\beta - \widehat\beta)w_i - \widehat\beta w_i\delta_i(1+\delta_i') .
\]
Take \( 2 \)-norms over \( i \), one term at a time. The first is at most \( u(\norm{\v} + \lvert\widehat\beta\rvert\nu) \le 4u\norm{\v} \); the second is \( \lvert\beta - \widehat\beta\rvert\nu \le Ku\norm{\v} \); the third is at most \( \lvert\widehat\beta\rvert\nu\,u(1+u) \le 4u\norm{\v} \). Hence
\[
\norm{\widehat{\y} - \H\v}_2 \le (K + 8)u\norm{\v}_2 = (10m+16)u\norm{\v}_2 .
\]

**Step 4: forward to backward.** Put \( \Delta\v = \H(\widehat{\y} - \H\v) \). Then \( \H(\v + \Delta\v) = \H\v + \H^2(\widehat\y - \H\v) = \widehat\y \) by @prp-householder-properties (b), and \( \norm{\Delta\v}_2 = \norm{\widehat\y - \H\v}_2 \) because \( \H \) is unitary (@prp-householder-properties (c)). This is (a).

*(b).* Apply (a) to each column \( \a_j \), obtaining \( \Delta\a_j \) with \( \norm{\Delta\a_j}_2 \le (10m+16)u\norm{\a_j}_2 \), and let \( \Delta\A \) have these columns. Then \( \widehat{\B} = \H(\A + \Delta\A) \) column by column, and squaring and summing over \( j \) gives \( \norm{\Delta\A}_F \le (10m+16)u\norm{\A}_F \). This proves the theorem.
:::

The constants are crude on purpose; what matters is their shape. **The bound is a multiple of \( u \) and of \( m \), and of nothing else.** No condition number appears, and none can: a reflection is an isometry, so it neither stretches nor shrinks, and there is no small quantity anywhere for a rounding error to be measured against.

::: {.remark}
**What the accumulation says, and that we do not prove it.** Running \( \min(n, m-1) \) reflections as in @thm-qr-householder, one obtains computed \( \widehat{\R} \) and stored reflection vectors. The classical theorem — due to Wilkinson, and proved by inducting the argument above over the reflections while tracking how the perturbations compose — states that there is an **exactly** unitary \( \widetilde{\Q} \in M_m(\nR) \), not in general the product of the computed reflections, with
\[
\widetilde{\Q}\,\widehat{\R} = \A + \Delta\A,
\qquad
\norm{\Delta\A}_F \le c(m,n)\,u\,\norm{\A}_F ,
\]
and that the resulting least-squares solution is the exact solution of a problem with data perturbed by \( O(u) \) — the hypothesis of @thm-normal-equations-lose-twice (b). **This accumulated statement is not proved here**, and nothing in this book depends on it: every theorem above either proves its own case or carries backward stability as a stated hypothesis. The induction is not deep, but it is long, and the honest thing is to say so.
:::

## What goes wrong with Gram–Schmidt

Chapter 10 §02 warned that "the classical process is numerically fragile" and promised that this chapter would say why the reflection route is the stable one. Half of the answer is @thm-householder-backward-stable. The other half is what the Gram–Schmidt recursion of @thm-gram-schmidt does instead.

The recursion subtracts from \( \a_k \) its components along the vectors already produced. When the columns are nearly dependent, what is left is a small difference of large quantities, and the leading digits cancel, exactly as in the subtraction of nearly equal numbers examined in Section 1. The computed \( \q_k \) is then a unit vector in a noticeably wrong direction, and, worse, the error is not random: it is inherited by every later step. The measured consequence is a loss of *orthogonality*: the computed \( \widehat{\Q} \) satisfies \( \widehat{\Q}\tp\widehat{\Q} \ne \I \) by an amount that grows with \( \kappa_2(\A) \). The classical analyses, which we state with credit and **do not prove here**, say how fast:

- for the **classical** process, \( \norm{\widehat{\Q}\tp\widehat{\Q} - \I} \) is of order \( u\,\kappa_2(\A)^2 \) (Kielbasinski; Giraud, Langou and Rozloznik);
- for the **modified** process, in which each new vector is projected against the \( \q_i \) one at a time as it is formed rather than all at once from the original \( \a_k \), it is of order \( u\,\kappa_2(\A) \) (Bjorck);
- for the reflection route it is of order \( u \), independently of \( \kappa_2(\A) \), which is the content of @thm-householder-backward-stable.

::: {#exm-gram-schmidt-loses-orthogonality}
[Three columns and three answers]

Let \( \varepsilon = 10^{-6} \) and
\[
\A = \begin{pmatrix} 1 & 1 & 1 \\ \varepsilon & 0 & 0 \\ 0 & \varepsilon & 0\end{pmatrix} .
\]
Show that \( \kappa_2(\A) = 3/\varepsilon + O(\varepsilon) \), then run the classical and the modified recursion in the model with \( u = 2^{-53} \) and compare the inner products of the computed vectors.
:::

::: {.solution}
*The condition number.* \( \A\tp\A = \begin{psmallmatrix} 1+\varepsilon^2 & 1 & 1 \\ 1 & 1+\varepsilon^2 & 1 \\ 1 & 1 & 1\end{psmallmatrix} \). Its characteristic polynomial factors as
\[
\det(t\I - \A\tp\A) = (t - \varepsilon^2)\bigl(t^2 - (3+\varepsilon^2)t + \varepsilon^2\bigr) ,
\]
as one checks by expanding both sides. The quadratic has roots \( t_{\pm} \) with \( t_+t_- = \varepsilon^2 \) and \( t_+ + t_- = 3 + \varepsilon^2 \), so \( t_+ = 3 + O(\varepsilon^2) \) and \( t_- = \varepsilon^2/3 + O(\varepsilon^4) \). Hence \( \sigma_1 = \sqrt3 + O(\varepsilon^2) \) and \( \sigma_3 = \varepsilon/\sqrt3 + O(\varepsilon^3) \), and
\[
\kappa_2(\A) = \frac{\sqrt3}{\varepsilon/\sqrt3} + O(\varepsilon) = \frac{3}{\varepsilon} + O(\varepsilon) = 3.000000 \cdot 10^{6} .
\]
So \( u\kappa_2(\A) = 3.3\cdot10^{-10} \) and \( u\kappa_2(\A)^2 = 1.0\cdot10^{-3} \).

*The computed vectors.* Both recursions produce the same \( \q_1 \) and \( \q_2 \), with \( \inner{\q_1}{\q_2} = 6.3\cdot10^{-11} \): that is the unavoidable \( u\kappa_2(\A) \), and it is already five to six digits worse than \( u \), being larger by a factor of \( 5.7\cdot10^{5} \). The two differ at the third step, which is where the cancellation bites:
\[
\begin{aligned}
\text{classical:}\quad &\inner{\q_2}{\q_3} = -8.89\cdot10^{-5}, \\
\text{modified:}\quad &\inner{\q_2}{\q_3} = 0 .
\end{aligned}
\]
The classical figure is within a factor of \( 12 \) of \( u\kappa_2(\A)^2 = 1.0\cdot10^{-3} \); the modified figure is at the level of \( u\kappa_2(\A) \) or below. Two vectors at inner product \( 9\cdot10^{-5} \) are at about \( 89.995 \) degrees to each other, and a basis that is orthonormal only to five digits is worth five digits in everything computed from it.
:::

## The sign in the reflection, quantified

Chapter 10 §08 chose \( \w = \x + \alpha\norm{\x}\e_1 \) rather than \( \w' = \x - \alpha\norm{\x}\e_1 \), where \( \alpha \) is the phase of \( x_1 \), and said: "Chapter 23 quantifies the loss; the summary here is that both signs are correct mathematics and only one is correct arithmetic." Here is the quantity.

Take \( \x \in \nR^m \) non-zero with \( x_1 > 0 \), so \( \alpha = 1 \), and write \( \widetilde{\x} = (x_2, \dots, x_m) \). Expanding as in @thm-householder-maps-vector,

\[
\norm{\w}^2 = 2\norm{\x}\bigl(\norm{\x} + x_1\bigr),
\qquad
\norm{\w'}^2 = 2\norm{\x}\bigl(\norm{\x} - x_1\bigr) ,
\]

and \( (\norm{\x}+x_1)(\norm{\x}-x_1) = \norm{\widetilde{\x}}^2 \). Both vectors are built by the same two operations: compute \( \norm{\x} \), then add it to or subtract it from \( x_1 \). The computed norm carries an error of absolute size about \( u\norm{\x} \), and every other entry is copied from \( \x \) exactly. So in both cases the computed vector is \( \w + \Delta\w \) with \( \norm{\Delta\w} \approx u\norm{\x} \) — *the same absolute error*. What differs is what that error is measured against, because \( \H_{\w} \) depends on \( \w \) only through the line it spans. Writing \( \p = \w/\norm{\w} \) and \( \q = (\w + \Delta\w)/\norm{\w+\Delta\w} \), @def-householder-reflection gives \( \H_{\w} - \H_{\w + \Delta\w} = -2(\p\p^{*} - \q\q^{*}) \), and
\[
\norm{\p\p^{*} - \q\q^{*}} \le \norm{\p(\p-\q)^{*}} + \norm{(\p - \q)\q^{*}} = 2\norm{\p - \q}
\le \frac{8\norm{\Delta\w}}{\norm{\w}} .
\]
For the last step, abbreviate \( \s = \Delta\w \) and split
\[
\p - \q = \w\Bigl(\frac{1}{\norm{\w}} - \frac{1}{\norm{\w+\s}}\Bigr) - \frac{\s}{\norm{\w+\s}} .
\]
The second piece has norm \( \norm{\s}/\norm{\w+\s} \), and the first has norm \( \bigl\lvert\norm{\w+\s} - \norm{\w}\bigr\rvert/\norm{\w+\s} \), which is at most the same quantity by the reverse triangle inequality (@lem-reverse-triangle-norm); and \( \norm{\w + \s} \ge \norm{\w}/2 \) as soon as \( \norm{\s} \le \norm{\w}/2 \), which is certainly the case here, \( \norm{\s} \) being of size \( u\norm{\x} \). So the computed reflection differs from the intended one by a small multiple of

\[
u\,\frac{\norm{\x}}{\norm{\w}},
\qquad\text{where}\qquad
\frac{\norm{\x}}{\norm{\w}} = \sqrt{\frac{\norm{\x}}{2(\norm{\x}+x_1)}} \ \le\ \frac{1}{\sqrt2} .
\]

The safe sign therefore never amplifies: its reflection is accurate to a small multiple of \( u \), no matter what \( \x \) is. The other sign amplifies by the factor

\[
\frac{\norm{\w}}{\norm{\w'}} = \sqrt{\frac{\norm{\x}+x_1}{\norm{\x}-x_1}} = \frac{\norm{\x}+x_1}{\norm{\widetilde{\x}}} ,
\]

which is **unbounded**: it blows up precisely as \( \x \) approaches a positive multiple of \( \e_1 \), where \( \norm{\widetilde{\x}} \to 0 \) and \( \w' \to \0 \).

::: {#exm-householder-sign-loss}
[The same vector, the two signs]

Let \( \varepsilon = 10^{-8} \) and \( \x = (1, \varepsilon, \varepsilon) \in \nR^3 \). Predict the amplification factor for each sign, then apply each computed reflection to \( \x \) in the model with \( u = 2^{-53} \) and measure how flat the answer is.
:::

::: {.solution}
*Prediction.* \( \norm{\widetilde{\x}} = \sqrt2\,\varepsilon = 1.41\cdot10^{-8} \) and \( \norm{\x} = \sqrt{1+2\varepsilon^2} \), so \( \norm{\x}/\norm{\w} = 0.5 \) for the safe sign, while
\[
\frac{\norm{\x}}{\norm{\w'}} = \sqrt{\frac{\norm{\x}}{2(\norm{\x}-1)}} = 7.07\cdot10^{7},
\qquad
u\,\frac{\norm{\x}}{\norm{\w'}} = 7.9\cdot10^{-9} .
\]

*The arithmetic.* The computed \( \norm{\x} \) is exactly \( 1 \): the true value exceeds \( 1 \) by \( \varepsilon^2 = 10^{-16} \), which is below the unit roundoff, so the addition returns \( 1 \). Hence
\[
\widehat{\w} = (2, \varepsilon, \varepsilon), \qquad \widehat{\w}' = (0, \varepsilon, \varepsilon) .
\]
The first is right to full relative accuracy in every entry. The second has lost its first entry altogether: it should be \( -10^{-16} \) and it is \( 0 \). Applying @eq-reflection-applied,
\[
\H_{\widehat{\w}}\,\x = (-1, 0, 0),
\qquad
\H_{\widehat{\w}'}\,\x = (1,\ -10^{-8},\ -10^{-8}) .
\]
The safe sign flattens \( \x \) exactly: the two entries that were supposed to be annihilated are true zeros. The other sign leaves behind entries of size \( 10^{-8} \) beside a vector of norm \( 1 \) — a failure of \( 1.4\cdot10^{-8} \) where \( 10^{-16} \) was available, and within a factor of \( 2 \) of the estimate \( u\norm{\x}/\norm{\w'} = 7.9\cdot10^{-9} \). Eight digits, thrown away by a sign.

For \( \varepsilon = 10^{-6} \) and \( \varepsilon = 10^{-4} \) the same computation leaves residues of \( 1.3\cdot10^{-10} \) and \( 1.5\cdot10^{-13} \), against estimates \( 7.9\cdot10^{-11} \) and \( 7.9\cdot10^{-13} \). The estimates fall by exactly \( 100 \) each time, as \( 1/\norm{\widetilde{\x}} \) does; the residues fall by \( 112 \) and then by \( 825 \), because a residue depends on the actual rounding error committed in \( \norm{\x} \), which varies with the binary expansion of \( \norm{\x} \) and not only with its size. Over four orders of magnitude the estimate stays within a factor of \( 6 \) of the measurement, which is all an order-of-magnitude estimate promises.
:::

**Non-example by minimal change.** Change one character of @exm-householder-sign-loss: take \( \x = (-1, \varepsilon, \varepsilon) \) with \( \varepsilon = 10^{-8} \). The arithmetic is unaltered — the computed \( \norm{\x} \) is again exactly \( 1 \) — and the rule of @thm-householder-maps-vector still works: the phase of \( x_1 \) is now \( \alpha = -1 \), so \( \w = \x + \alpha\norm{\x}\e_1 = (-2, \varepsilon, \varepsilon) \), again with \( \norm{\x}/\norm{\w} = 0.5 \) and again flattening \( \x \) to \( (1, 0, 0) \) exactly. What fails is the rule with the phase dropped, \( \w = \x + \norm{\x}\e_1 \): it returns \( (0, \varepsilon, \varepsilon) \), and that reflection leaves \( \x \) with the same residue \( 1.4\cdot10^{-8} \) as before. So the clause carrying the weight is not the plus sign but the **phase \( \alpha \)**: what the rule requires is that \( \alpha\norm{\x} \) be added to \( x_1 \) so that the first entry grows in modulus, never so that it cancels. Reading the plus sign literally is correct mathematics for every \( \x \) and correct arithmetic only for \( x_1 > 0 \).

::: {.warning}
**The bad sign is not merely inaccurate; on one input it does not exist.** If \( \x = c\,\e_1 \) with \( c > 0 \), then \( \w' = \0 \) and @def-householder-reflection does not apply at all. That is not an accident of the arithmetic but the limit of the cancellation: the quantity whose leading digits are being destroyed is \( \norm{\x} - x_1 \), and on that input it is zero. An algorithm that is undefined at a point is inaccurate near it, and the sign rule of @thm-householder-maps-vector is exactly the rule that keeps the point out of reach.
:::

## Exercises

### A. Check your understanding

:::: {#exr-numerical-least-squares-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define \( \theta \) for a least-squares problem \( \A\z \approx \b \) with \( \rank\A = n \), and say what \( \theta = 0 \) means about the system.
2. State @thm-least-squares-conditioning, and say which of its two terms survives when the residual is zero.
3. Explain in one sentence why \( \kappa_2(\A)^2 \) appears in the normal-equation route even for a consistent system, and why it need not appear in the reflection route.
4. True or false: "a matrix with \( \kappa_2(\A) = 10^{3} \) should never be handled by the normal equations". Justify your answer.
5. What quantity does @thm-householder-backward-stable bound, and which quantity does it **not** depend on?
:::
::::

::: {.solution}
(a) By @eq-ls-angle, \( \theta \in [0, \pi/2] \) is determined by \( \sin\theta = \norm{\r}/\norm{\b} \) with \( \r = \b - \A\x \) the residual, equivalently \( \cos\theta = \norm{\A\x}/\norm{\b} \); it is the angle between \( \b \) and \( \col(\A) \). Then \( \theta = 0 \) says \( \r = \0 \), that is, the system \( \A\z = \b \) is consistent.

(b) See @thm-least-squares-conditioning: the relative sensitivity is at most \( \kappa_2(\A)(\varepsilon_{\A} + \varepsilon_{\b}/\cos\theta) + \kappa_2(\A)^2\varepsilon_{\A}\tan\theta \). With \( \r = \0 \) we get \( \tan\theta = 0 \), and only the \( \kappa_2(\A) \) term survives, with \( \cos\theta = 1 \).

(c) The normal-equation route solves a *different* linear system, the one with matrix \( \A^{*}\A \), whose condition number is \( \kappa_2(\A)^2 \) by @thm-normal-equations-squares-conditioning, and the rounding committed in forming that matrix is magnified by its condition number, not by \( \A \)'s; the reflection route never forms the product, and \( \kappa_2(\R) = \kappa_2(\A) \).

(d) False. By @thm-normal-equations-lose-twice (a) the loss is about \( 2\log_{10}\kappa_2(\A) = 6 \) digits out of sixteen, which is usually ample; the route costs about half the arithmetic. The warning after @exm-normal-equations-fail states the rule quantitatively: what matters is whether \( u\kappa_2(\A)^2 \) is small enough for the purpose.

(e) It bounds the **backward** error of applying one reflection by the formula @eq-reflection-applied: the computed output is the exact output for an input perturbed by at most \( (10m+16)u \) relatively. It does not depend on any condition number, only on \( m \) and \( u \).
:::

### B. Practice

:::: {#exr-numerical-least-squares-b1}
[B1: Reading the bound]

Let \( \A \in M_{50 \times 3}(\nR) \) have \( \kappa_2(\A) = 10^{5} \), and suppose the data are accurate to \( \varepsilon = 10^{-10} \) relatively. Using @eq-ls-first-order with \( u \approx 10^{-16} \) where needed:

::: {.enumerate options="label=(\alph*)"}
1. Bound the relative error of the exact least-squares solution caused by the data error, when the residual is zero.
2. Do the same when \( \tan\theta = 1 \).
3. In case (b), how many digits does the normal-equation route lose on top of the data error, and how many does a backward stable method lose?
:::
::::

::: {.solution}
(a) With \( \theta = 0 \), @eq-ls-first-order gives \( 2\kappa_2(\A)\varepsilon = 2\cdot10^{5}\cdot10^{-10} = 2\cdot10^{-5} \): about five correct digits, and no algorithm can restore them.

(b) With \( \tan\theta = 1 \) we have \( \cos\theta = 1/\sqrt2 \), so the bracket is \( \kappa_2(1 + \sqrt2) + \kappa_2^2 = 2.4\cdot10^{5} + 10^{10} \approx 10^{10} \), and the bound is \( 10^{10}\cdot10^{-10} = 1 \). The data alone determine nothing: the \( \kappa_2^2\tan\theta \) term has swallowed the problem.

(c) The arithmetic contributes \( u\kappa_2(\A)^2 = 10^{-16}\cdot10^{10} = 10^{-6} \) for the normal equations and \( u\,(\kappa_2 + \kappa_2^2\tan\theta) \approx 10^{-6} \) for a backward stable method as well, by @thm-normal-equations-lose-twice. In this case the two lose the same six digits — because the \( \kappa_2^2 \) is the problem's, not the algorithm's. Both are far below the \( 10^{0} \) already lost to the data, so the choice of method is irrelevant here; it is for \( \tan\theta \) small that it decides everything.
:::

:::: {#exr-numerical-least-squares-b2}
[B2: Where the product goes singular]

Let \( \A = \begin{psmallmatrix} 1 & 1 \\ \varepsilon & 0 \\ 0 & \varepsilon\end{psmallmatrix} \) as in @exm-normal-equations-fail, in the model with \( u = 2^{-53} \).

::: {.enumerate options="label=(\alph*)"}
1. For which \( \varepsilon \) does \( \fl(1 + \varepsilon^2) = 1 \) hold, and what is \( \fl(\A\tp\A) \) then?
2. Express the threshold in (a) in terms of \( \kappa_2(\A) \) and \( u \).
3. Explain why the reflection route is untroubled at that threshold.
:::
::::

::: {.solution}
(a) By @def-floating-point-model, \( \fl(1+\delta) = 1 \) exactly when \( \delta \) is at most the largest quantity that rounds away beside \( 1 \), which is \( u = 2^{-53} \approx 1.11\cdot10^{-16} \). So \( \fl(1+\varepsilon^2) = 1 \) for \( \varepsilon^2 \le u \), that is \( \varepsilon \lesssim 1.05\cdot10^{-8} \). Then every entry of \( \fl(\A\tp\A) \) is \( 1 \) and the computed matrix is \( \begin{psmallmatrix}1&1\\1&1\end{psmallmatrix} \), which is singular: the information distinguishing the two columns has been rounded away.

(b) From @exm-normal-equations-fail, \( \kappa_2(\A) = \sqrt{2+\varepsilon^2}/\varepsilon \approx \sqrt2/\varepsilon \), so \( \varepsilon^2 \le u \) says \( \kappa_2(\A)^2 \ge 2/u \), that is \( u\kappa_2(\A)^2 \ge 2 \). The normal equations collapse exactly when the bound of @thm-normal-equations-lose-twice (a) exceeds \( 1 \), which is the same as saying that the route promises no correct digit.

(c) The reflection route never computes \( 1 + \varepsilon^2 \). It works with \( \A \) itself, whose entries record \( \varepsilon \) and not \( \varepsilon^2 \), and by @thm-householder-backward-stable each reflection perturbs the data relatively by \( O(u) \). A relative perturbation of \( 10^{-16} \) in \( \varepsilon = 10^{-9} \) leaves \( \varepsilon \) intact; a relative perturbation of \( 10^{-16} \) in \( 1 \) destroys \( \varepsilon^2 = 10^{-18} \). Squaring is what moves the small quantity below the rounding level.
:::

:::: {#exr-numerical-least-squares-b3}
[B3: One reflection, by hand]

Let \( \x = (3, 0, 4) \in \nR^3 \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \w \) and \( \w' \) as in @thm-householder-maps-vector, and the two amplification factors \( \norm{\x}/\norm{\w} \) and \( \norm{\x}/\norm{\w'} \).
2. Verify the identity \( \norm{\w}^2\norm{\w'}^2 = 4\norm{\x}^2\norm{\widetilde{\x}}^2 \) on this example.
3. Is the sign choice important for this \( \x \)? Justify your answer.
:::
::::

::: {.solution}
(a) \( \norm{\x} = 5 \) and \( x_1 = 3 > 0 \), so \( \alpha = 1 \), \( \w = (8, 0, 4) \) and \( \w' = (-2, 0, 4) \). Then \( \norm{\w}^2 = 80 \) and \( \norm{\w'}^2 = 20 \), so
\[
\frac{\norm{\x}}{\norm{\w}} = \frac{5}{\sqrt{80}} = \frac{\sqrt5}{4} \approx 0.559,
\qquad
\frac{\norm{\x}}{\norm{\w'}} = \frac{5}{\sqrt{20}} = \frac{\sqrt5}{2} \approx 1.118 .
\]
Both are of order \( 1 \). (The general formulas agree: \( \norm{\w}^2 = 2\cdot5\cdot(5+3) = 80 \) and \( \norm{\w'}^2 = 2\cdot5\cdot(5-3) = 20 \).)

(b) \( \widetilde{\x} = (0,4) \) has \( \norm{\widetilde{\x}}^2 = 16 \), and \( 4\norm{\x}^2\norm{\widetilde{\x}}^2 = 4\cdot25\cdot16 = 1600 = 80\cdot20 \). The identity is \( \norm{\w}^2\norm{\w'}^2 = 4\norm{\x}^2(\norm{\x}+x_1)(\norm{\x}-x_1) = 4\norm{\x}^2\norm{\widetilde{\x}}^2 \).

(c) No. The amplification factor of the bad sign is \( (\norm{\x}+x_1)/\norm{\widetilde{\x}} = 8/4 = 2 \), so the two choices differ by a factor of \( 2 \) in accuracy, which is nothing. The sign matters only when \( \x \) is close to a multiple of \( \e_1 \), that is when \( \norm{\widetilde{\x}} \ll \norm{\x} \); here \( \norm{\widetilde{\x}} = 4 \) is comparable with \( \norm{\x} = 5 \).
:::

### C. Going deeper

:::: {#exr-numerical-least-squares-c1}
[C1: The squared term is attained]

Let \( \varepsilon, \delta > 0 \) and take
\[
\A = \begin{pmatrix} 1 & 0 \\ 0 & \varepsilon \\ 0 & 0 \end{pmatrix},
\qquad
\b = \begin{pmatrix} 1 \\ 0 \\ \delta \end{pmatrix},
\qquad
\E = \begin{pmatrix} 0 & 0 \\ 0 & 0 \\ 0 & 1 \end{pmatrix},
\qquad
\f = \0 .
\]

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \kappa_2(\A) \), the least-squares solution \( \x \), the residual \( \r \) and \( \tan\theta \).
2. Using \( (\ast) \) in the proof of @thm-least-squares-conditioning, compute \( \x'(0) \) exactly.
3. Hence show that the squared term of @thm-least-squares-conditioning is attained, in the sense that \( \norm{\x'(0)}/\norm{\x} \) equals \( \kappa_2(\A)^2\varepsilon_{\A}\tan\theta \) exactly, and explain what this says about any algorithm for this problem.
:::
::::

::: {.solution}
(a) \( \A\tp\A = \diag(1, \varepsilon^2) \), so the singular values are \( 1 \) and \( \varepsilon \) and \( \kappa_2(\A) = 1/\varepsilon \) by the rectangular clause of @def-condition-number. The normal equations \( \diag(1,\varepsilon^2)\x = \A\tp\b = (1, 0) \) give \( \x = (1, 0) \). Then \( \A\x = (1,0,0) \), so \( \r = \b - \A\x = (0,0,\delta) \) and, by @eq-ls-angle,
\[
\tan\theta = \frac{\norm{\r}}{\norm{\A\x}} = \delta .
\]
Also \( \norm{\E} = 1 = \norm{\A} \), so \( \varepsilon_{\A} = 1 \), and \( \varepsilon_{\b} = 0 \).

(b) The three terms of \( (\ast) \). First, \( \E\tp\r = \e_2(\e_3\tp\r) = \delta\,\e_2 \), and \( (\A\tp\A)^{-1} = \diag(1, \varepsilon^{-2}) \), so the first term is \( (\delta/\varepsilon^2)\e_2 \). Second, \( \E\x = \e_3(\e_2\tp\x) = \0 \) because \( x_2 = 0 \), so the second term vanishes. Third, \( \f = \0 \). Hence
\[
\x'(0) = \Bigl(0, \frac{\delta}{\varepsilon^2}\Bigr) .
\]

(c) \( \norm{\x} = 1 \) and \( \norm{\x'(0)} = \delta/\varepsilon^2 \), while
\[
\kappa_2(\A)^2\,\varepsilon_{\A}\tan\theta = \frac{1}{\varepsilon^2}\cdot1\cdot\delta = \frac{\delta}{\varepsilon^2} .
\]
The two agree exactly: the squared term is **attained**. The bound as a whole is not, and the reason is that the other two terms are non-negative — here the first of them contributes a further \( \kappa_2(\A)\varepsilon_{\A} = 1/\varepsilon \), so the bound exceeds \( \norm{\x'(0)}/\norm{\x} \) by exactly that much. It is the squared term that matters, and what it says is that the sensitivity is a property of the data \( (\A, \b) \) alone: a perturbation of \( \A \) of relative size \( \varepsilon_{\A} \) really does move the exact answer by \( \kappa_2(\A)^2\tan\theta\,\varepsilon_{\A} \) relatively, so **no** algorithm, however stable, can return an answer better than that from data known only to within \( \varepsilon_{\A} \). Compare @thm-normal-equations-lose-twice (b): a backward stable method achieves this and no more.
:::

:::: {#exr-numerical-least-squares-c2}
[C2: Why the residual has to appear]

Let \( \A \in M_{m \times n}(F) \) have rank \( n \), and let \( \x^{+} = \A^{+}\b \) be the least-squares solution, where \( \A^{+} \) is the pseudoinverse of @def-pseudoinverse.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \A^{+} = (\A^{*}\A)^{-1}\A^{*} \) when \( \rank\A = n \), and deduce \( \norm{\A^{+}} = 1/\sigma_n(\A) \).
2. Deduce from \( (\ast) \) in the proof of @thm-least-squares-conditioning that if \( \E = \0 \) — only \( \b \) is perturbed — then no \( \kappa_2(\A)^2 \) term can appear, whatever the residual.
3. Explain, in one or two sentences, why perturbing \( \A \) is different: which term of \( (\ast) \) carries the residual, and why it cannot be present when \( \E = \0 \).
:::
::::

::: {.solution}
(a) Write \( \A = \U\vSigma\V^{*} \) (@thm-svd). Since \( \rank\A = n \), \( \sigma_1, \dots, \sigma_n > 0 \), so \( \vSigma^{+} \) of @def-pseudoinverse has \( \sigma_i^{-1} \) on its diagonal and \( \A^{+} = \V\vSigma^{+}\U^{*} \). On the other hand \( \A^{*}\A = \V(\vSigma^{*}\vSigma)\V^{*} = \V\diag(\sigma_i^2)\V^{*} \), so
\[
(\A^{*}\A)^{-1}\A^{*} = \V\diag(\sigma_i^{-2})\V^{*}\,\V\vSigma^{*}\U^{*} = \V\bigl(\diag(\sigma_i^{-2})\vSigma^{*}\bigr)\U^{*} = \V\vSigma^{+}\U^{*} = \A^{+} ,
\]
because \( \diag(\sigma_i^{-2})\vSigma^{*} \) is the \( n \times m \) matrix with entries \( \sigma_i^{-2}\sigma_i = \sigma_i^{-1} \) on the diagonal and zeros elsewhere. Unitary factors leave singular values alone — \( (\V\vSigma^{+}\U^{*})^{*}(\V\vSigma^{+}\U^{*}) = \U(\vSigma^{+*}\vSigma^{+})\U^{*} \) is unitarily similar to \( \vSigma^{+*}\vSigma^{+} \), so the two have the same eigenvalues and @def-singular-values reads the same singular values off them — so \( \norm{\A^{+}} = \norm{\vSigma^{+}} = \max_i \sigma_i^{-1} = 1/\sigma_n \) by @thm-operator-norm-formulas (c).

(b) With \( \E = \0 \), \( (\ast) \) reduces to \( \x'(0) = \A^{+}\f \), so by (a)
\[
\frac{\norm{\x'(0)}}{\norm{\x}} \le \frac{\norm{\f}}{\sigma_n\norm{\x}}
= \kappa_2(\A)\,\varepsilon_{\b}\,\frac{\norm{\b}}{\sigma_1\norm{\x}}
\le \frac{\kappa_2(\A)\,\varepsilon_{\b}}{\cos\theta} ,
\]
a single factor of \( \kappa_2(\A) \) however large \( \norm{\r} \) is. (The residual enters only through \( 1/\cos\theta \), which is bounded as long as \( \theta \) is bounded away from \( \pi/2 \).)

(c) The residual sits in the term \( (\A^{*}\A)^{-1}\E^{*}\r \), and that is the only term with \( (\A^{*}\A)^{-1} \) *not* paired with an \( \A^{*} \) — which is exactly why it carries \( \sigma_n^{-2} \) rather than \( \sigma_n^{-1} \). It is proportional to \( \E \), so it vanishes when \( \E = \0 \). Perturbing \( \b \) tilts the target inside a fixed column space; perturbing \( \A \) tilts the column space itself, and the residual is the lever arm by which that tilt moves the answer.
:::

:::: {#exr-numerical-least-squares-c3}
[C3: A reflection applied to a matrix]

Let \( \H = \H_{\w} \) be a Householder reflection in \( \nR^m \) and let \( \A \in M_{m \times n}(\nR) \).

::: {.enumerate options="label=(\alph*)"}
1. Using @thm-householder-backward-stable (b) and \( \norm{\M} \le \norm{\M}_F \le \sqrt{n}\,\norm{\M} \) for \( \M \in M_{m \times n} \), show that the computed \( \widehat{\B} \) satisfies \( \norm{\widehat{\B} - \H\A} \le (10m+16)\sqrt n\,u\,\norm{\A} \).
2. Deduce that \( \sigma_i(\widehat{\B}) \) differs from \( \sigma_i(\A) \) by at most \( (10m+16)\sqrt n\,u\,\norm{\A} \) for every \( i \). *Hint: Chapter 19 §10 or Chapter 16 §09 bounds the perturbation of singular values by the norm of the perturbation.*
3. Explain why the corresponding statement is false for the classical Gram–Schmidt process, citing @exm-gram-schmidt-loses-orthogonality.
:::
::::

::: {.solution}
(a) By @thm-householder-backward-stable (b), \( \widehat{\B} - \H\A = \H\,\Delta\A \) with \( \norm{\Delta\A}_F \le (10m+16)u\norm{\A}_F \). Since \( \H \) is unitary (@prp-householder-properties (c)) it leaves the \( 2 \)-norm unchanged, so
\[
\norm{\widehat{\B} - \H\A} = \norm{\Delta\A} \le \norm{\Delta\A}_F \le (10m+16)u\norm{\A}_F \le (10m+16)\sqrt n\,u\,\norm{\A} .
\]

(b) \( \H\A \) has the same singular values as \( \A \): \( (\H\A)^{*}(\H\A) = \A^{*}\H^{*}\H\A = \A^{*}\A \), so @def-singular-values reads the same list off the same matrix. Weyl's inequality for singular values (@thm-weyl-singular-values with \( j = 1 \), or @cor-singular-value-perturbation directly) gives \( \lvert\sigma_i(\widehat{\B}) - \sigma_i(\H\A)\rvert \le \norm{\widehat{\B} - \H\A} \) for every \( i \), and the right-hand side is bounded in (a).

(c) The Gram–Schmidt recursion of @thm-gram-schmidt does not apply a unitary matrix to \( \A \); it *builds* a matrix \( \widehat{\Q} \) out of \( \A \) and hopes it is unitary. @exm-gram-schmidt-loses-orthogonality measures the damage: for \( \kappa_2(\A) = 3\cdot10^{6} \) the computed vectors have inner products of size \( 9\cdot10^{-5} \), so \( \widehat{\Q} \) is unitary only to five digits, and \( \norm{\widehat{\Q}\tp\widehat{\Q} - \I} \) exceeds \( u \) by eleven orders of magnitude on that one example. (That it does so at the rate \( u\kappa_2(\A)^2 \) in general is the classical estimate quoted above, which this book does not prove.) Any conclusion drawn from "unitary factors leave singular values alone" then inherits that error instead of none. The reflection route wins because the unitary matrix is never in question: it is exactly unitary by construction, and only its *input* is perturbed.
:::
