# Definiteness and Second Derivatives

Chapter 12 studied positive definite matrices at length, and the previous section showed that the signature is what congruence remembers. Putting the two together costs almost nothing and buys two things: a vocabulary that covers the forms Chapter 12 had no name for, the indefinite and the semidefinite ones, and the classical application that made quadratic forms worth studying in the first place. Nothing from Chapter 12 is reproved here. The field is \( \nR \) throughout, since none of the five words below means anything without an order.

Throughout, \( V \) is a finite-dimensional real vector space, \( \beta \) is a **symmetric** bilinear form on \( V \) (@def-symmetric-form), \( q(\v) = \beta(\v,\v) \) is its quadratic form (@def-quadratic-form), and \( \A = \mtx{\beta}{\sB}{\sB} \) is its matrix in a basis \( \sB \) (@def-form-matrix), a real symmetric matrix.

## Five words for the sign of a form

Chapter 12 named two of the possible behaviors of \( q \): never negative, and always positive away from \( \0 \). There are three more, and the missing ones are not exotic. The form \( q(x_1, x_2) = x_1^2 - x_2^2 \) is positive at \( \e_1 \), negative at \( \e_2 \), and nothing in Chapter 12's vocabulary describes it.

*A form is definite when \( q \) has one strict sign, semidefinite when it has one sign but is allowed to vanish, and indefinite when it has both signs.*

::: {#def-definiteness-of-a-form}
[Definiteness of a Real Symmetric Form]

Let \( \beta \) be a symmetric bilinear form on a real vector space \( V \), with quadratic form \( q \). Then \( \beta \) is:

::: {.enumerate options="label=(\alph*)"}
1. **positive definite** if \( q(\v) > 0 \) for **every non-zero** \( \v \in V \);
2. **positive semidefinite** if \( q(\v) \ge 0 \) for every \( \v \in V \);
3. **negative definite** if \( q(\v) < 0 \) for every non-zero \( \v \in V \);
4. **negative semidefinite** if \( q(\v) \le 0 \) for every \( \v \in V \);
5. **indefinite** if there exist \( \u, \w \in V \) with \( q(\u) > 0 \) and \( q(\w) < 0 \).
:::

The same five words apply to a real symmetric matrix \( \A \), through the form \( \beta(\x,\y) = \x\tp\A\y \) on \( \nR^n \).
:::

The small words carry the weight. In (a) and (c) the inequality is **strict** and the vector must be **non-zero**; in (b) and (d) it is weak and \( \v = \0 \) is allowed, where \( q(\0) = 0 \) makes the condition automatic. Definite implies semidefinite of the same sign. Clause (e) is not the negation of (b): \( q(x_1,x_2) = -x_1^2 \) is neither positive semidefinite nor indefinite. For matrices, (a) and (b) are @def-positive-semidefinite restricted to \( F = \nR \), so \( \A \succ 0 \) and \( \A \succeq 0 \) keep their meanings, and the negative versions are the positive ones for \( -\A \).

Four examples on \( \nR^2 \), all diagonal so that \( q \) can be read off @eq-diagonal-quadratic-form: \( x_1^2 + x_2^2 \) is positive definite; \( x_1^2 \) is positive semidefinite but not definite, since it vanishes at \( \e_2 \ne \0 \); \( -x_1^2 - x_2^2 \) is negative definite; \( x_1^2 - x_2^2 \) is indefinite. The zero form is the degenerate case, satisfying (b) and (d) and nothing else — which is why the five classes overlap rather than partition. Changing one sign in the third gives the non-example \( -x_1^2 + x_2^2 \): it is no longer negative semidefinite, and the clause that fails is (d) at \( \v = \e_2 \), where \( q = 1 > 0 \).

Now the reading through the signature, which makes all five conditions into statements about three integers.

::: {#thm-definiteness-by-signature}
[Definiteness Is the Signature]

Let \( \beta \) be a symmetric bilinear form on a real vector space \( V \) of dimension \( n \), with inertia \( (n_+, n_-, n_0) \) (@def-signature). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \beta \) is positive definite \( \iff \) \( (n_+, n_-, n_0) = (n, 0, 0) \);
2. \( \beta \) is positive semidefinite \( \iff \) \( n_- = 0 \);
3. \( \beta \) is negative definite \( \iff \) \( (n_+, n_-, n_0) = (0, n, 0) \);
4. \( \beta \) is negative semidefinite \( \iff \) \( n_+ = 0 \);
5. \( \beta \) is indefinite \( \iff \) \( n_+ > 0 \) and \( n_- > 0 \).
:::
:::

::: {.idea}
Fix an orthogonal basis. Then \( q \) is \( \sum_i d_i c_i^2 \) with no cross terms, and each of the five conditions becomes a visible condition on the signs of the \( d_i \): plugging in a basis vector reads off one \( d_i \), and a general \( \v \) mixes the \( d_i \) with non-negative weights. Sylvester's law is what lets us fix one basis and still be talking about \( \beta \).
:::

::: {.proof}
By @thm-symmetric-form-diagonalizable there is an orthogonal basis \( \sB = (\v_1, \dots, \v_n) \) for \( \beta \); put \( d_i = q(\v_i) \). By @thm-sylvester-inertia the numbers of positive, negative and zero \( d_i \) are \( n_+ \), \( n_- \) and \( n_0 \), whichever orthogonal basis is used. For \( \v = \sum_i c_i\v_i \), @eq-diagonal-quadratic-form gives
\[
q(\v) = \sum_{i=1}^{n} d_i c_i^2 .
\]

(b) \( (\Rightarrow) \) If some \( d_j < 0 \) then \( q(\v_j) = d_j < 0 \), so \( \beta \) is not positive semidefinite. \( (\Leftarrow) \) If no \( d_i \) is negative then every term \( d_ic_i^2 \) is \( \ge 0 \), so \( q(\v) \ge 0 \).

(a) \( (\Rightarrow) \) A positive definite \( \beta \) is positive semidefinite, so \( n_- = 0 \) by (b); and if some \( d_j = 0 \) then \( q(\v_j) = 0 \) with \( \v_j \ne \0 \), a contradiction. Hence \( n_0 = 0 \) and \( n_+ = n \). \( (\Leftarrow) \) If every \( d_i > 0 \) and \( \v \ne \0 \), some \( c_j \ne 0 \), so \( q(\v) \ge d_jc_j^2 > 0 \), the other terms being \( \ge 0 \).

(c) and (d) follow by applying (a) and (b) to \( -\beta \), whose diagonal entries are \( -d_i \) and whose inertia is therefore \( (n_-, n_+, n_0) \).

(e) \( (\Rightarrow) \) Suppose \( q(\u) > 0 \) and \( q(\w) < 0 \). Then \( \beta \) is neither positive semidefinite nor negative semidefinite, so \( n_- > 0 \) by (b) and \( n_+ > 0 \) by (d). \( (\Leftarrow) \) If \( n_+ > 0 \) and \( n_- > 0 \), some \( d_i > 0 \) and some \( d_j < 0 \), and the basis vectors \( \v_i, \v_j \) are the required \( \u, \w \). This proves the theorem.
:::

So the five words sort the \( \tfrac12(n+1)(n+2) \) congruence classes of @cor-real-symmetric-classification into named families, and every one of them is decided by counting signs. Two of these five verdicts were already settled in Chapter 12 by other means, and it is worth putting the tests side by side.

::: {#prp-definiteness-tests-for-forms}
[Chapter 12's Tests, in the Language of Forms]

Let \( \beta \) be a symmetric bilinear form on an \( n \)-dimensional real vector space, \( \A = \mtx{\beta}{\sB}{\sB} \) its matrix in any basis, and \( \A_k \) the top-left \( k \times k \) corner of \( \A \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \beta \) is positive definite \( \iff \) every eigenvalue of \( \A \) is positive \( \iff \) \( \det \A_k > 0 \) for \( k = 1, \dots, n \);
2. \( \beta \) is negative definite \( \iff \) every eigenvalue of \( \A \) is negative \( \iff \) \( (-1)^k\det \A_k > 0 \) for \( k = 1, \dots, n \).
:::
:::

::: {.proof}
(a) By @def-form-matrix and @thm-form-matrix-determines, \( q(\v) = \x\tp\A\x \) where \( \x = \coord{\v}{\sB} \), and \( \v \ne \0 \) exactly when \( \x \ne \0 \). So \( \beta \) is positive definite exactly when \( \A \succ 0 \), and the two stated tests are @thm-pd-characterizations (b) and (d), the second being Sylvester's criterion.

(b) Apply (a) to \( -\beta \), whose matrix is \( -\A \). The eigenvalues of \( -\A \) are the negatives of those of \( \A \), and \( (-\A)_k = -\A_k \) has \( \det(-\A_k) = (-1)^k\det\A_k \), since scaling each of the \( k \) rows by \( -1 \) multiplies the determinant by \( -1 \) once per row (@thm-det-row-operations (b)). This proves the proposition.
:::

The eigenvalue test is the one to think with, the minor test the one to compute with; cheapest of all is the symmetric elimination of Section 4, which returns the whole signature rather than a verdict. Nothing is said about the semidefinite cases on purpose: Sylvester's criterion has no weak version, as Chapter 12 showed with \( \diag(0,-1) \), whose leading minors are both \( 0 \).

::: {.check}
A real symmetric \( \A \in M_3(\nR) \) has \( \det \A_1 = -2 \), \( \det \A_2 = 5 \), \( \det \A_3 = -1 \). What is its definiteness?
:::

::: {.solution}
Negative definite. The signs alternate starting with a negative one, so \( (-1)^k\det\A_k > 0 \) for \( k = 1, 2, 3 \): indeed \( (-1)(-2) = 2 > 0 \), \( (+1)(5) = 5 > 0 \), \( (-1)(-1) = 1 > 0 \). By @prp-definiteness-tests-for-forms (b) the form is negative definite, and by @thm-definiteness-by-signature (c) its inertia is \( (0, 3, 0) \). Note that \( \det \A_3 = \det\A < 0 \) on its own would have been no evidence at all.
:::

## The second-derivative test

Here is the use. A differentiable function \( f \colon \nR^n \to \nR \) is constant to first order at a critical point, so whether the point is a minimum, a maximum or neither is decided — usually — by the second-order behavior. That behavior is a quadratic form, and @thm-definiteness-by-signature decides it. The linear algebra is the whole content; what has to be imported is one theorem of analysis, and we state it rather than hide it.

::: {#def-hessian}
[Hessian]

Let \( f \) be a real-valued function on an open set \( U \subseteq \nR^n \), twice continuously differentiable on \( U \), and let \( \a \in U \). The **Hessian** of \( f \) at \( \a \) is the matrix
\[
\H_f(\a) \in M_n(\nR), \qquad
\bigl(\H_f(\a)\bigr)_{ij} = \frac{\partial^2 f}{\partial x_i\,\partial x_j}(\a) .
\]
A point \( \a \in U \) with \( \nabla f(\a) = \0 \) is a **critical point** of \( f \).
:::

Two facts about \( \H_f(\a) \) are needed, and neither is linear algebra. They are exactly the analysis this book imports, so we set them out as assumptions rather than let them pass unnoticed. Let \( f \) be twice continuously differentiable on an open \( U \subseteq \nR^n \) and let \( \a \in U \).

::: {.enumerate options="label=(A\arabic*)"}
1. *(Symmetry of the second derivatives.)* The mixed partial derivatives satisfy \( \partial^2f/\partial x_i\partial x_j = \partial^2f/\partial x_j\partial x_i \) on \( U \), so \( \H_f(\a) \) is a **symmetric** matrix.
2. *(Taylor's theorem with a second-order remainder.)* For every \( \h \) small enough that \( \a + \h \in U \),
\[
f(\a + \h) = f(\a) + \nabla f(\a)\cdot\h + \tfrac12\,\h\tp\H_f(\a)\h + r(\h),
\]
where the remainder satisfies \( r(\h)/\norm{\h}^2 \to 0 \) as \( \h \to \0 \).
:::

These are two standard theorems of multivariable calculus. This book proves neither. They are quoted so that the theorem below has hypotheses to stand on, and Chapter 17 quotes them again for its second-derivative test of convexity, exactly as the theorem of Abel and Ruffini was quoted in Chapter 10. Everything after them is linear algebra.

By (A1) the Hessian is a real symmetric matrix, so it has an inertia, and by @thm-definiteness-by-signature that inertia decides the definiteness of the quadratic form \( \h \mapsto \h\tp\H_f(\a)\h \). One small lemma converts definiteness into a quantitative bound, and it is the only place where a real number is needed rather than a sign.

::: {#lem-definite-form-bounded-below}
[A Positive Definite Form Is Bounded Below by a Multiple of the Norm Squared]

Let \( \A \in M_n(\nR) \) be symmetric and positive definite, and let \( \lambda \) be its smallest eigenvalue. Then \( \lambda > 0 \) and
\[
\x\tp\A\x \ \ge\ \lambda\norm{\x}^2 \qquad \text{for every } \x \in \nR^n .
\]
:::

::: {.proof}
By @cor-spectral-real-matrix there are an orthogonal \( \Q \in \Orth(n) \) and a diagonal \( \D = \diag(\lambda_1, \dots, \lambda_n) \) listing the eigenvalues of \( \A \) with \( \A = \Q\D\Q\tp \). By @thm-pd-characterizations (b) every \( \lambda_i > 0 \), so \( \lambda = \min_i \lambda_i > 0 \). Put \( \y = \Q\tp\x \). Then
\[
\x\tp\A\x = \y\tp\D\y = \sum_{i=1}^n \lambda_i y_i^2 \ \ge\ \lambda\sum_{i=1}^n y_i^2 = \lambda\norm{\y}^2 ,
\]
using \( \lambda_i \ge \lambda \) and \( y_i^2 \ge 0 \) termwise. Finally \( \Q\Q\tp = \I \), so \( \norm{\y}^2 = \x\tp\Q\Q\tp\x = \norm{\x}^2 \). This proves the lemma.
:::

::: {#thm-second-derivative-test}
[The Second-Derivative Test]

Let \( f \) be a real-valued function, twice continuously differentiable on an open set \( U \subseteq \nR^n \), let \( \a \in U \) be a critical point of \( f \), and let \( (n_+, n_-, n_0) \) be the inertia of \( \H_f(\a) \). Then:

::: {.enumerate options="label=(\alph*)"}
1. if \( \H_f(\a) \) is positive definite, that is \( (n_+, n_-, n_0) = (n, 0, 0) \), then \( \a \) is a strict local minimum of \( f \);
2. if \( \H_f(\a) \) is negative definite, that is \( (n_+, n_-, n_0) = (0, n, 0) \), then \( \a \) is a strict local maximum of \( f \);
3. if \( \H_f(\a) \) is indefinite, that is \( n_+ > 0 \) and \( n_- > 0 \), then \( \a \) is neither a local minimum nor a local maximum: every neighborhood of \( \a \) contains points where \( f > f(\a) \) and points where \( f < f(\a) \). Such an \( \a \) is a **saddle point**.
:::

If \( n_0 > 0 \) and \( \a \) is not covered by (a)–(c), the test gives no information.
:::

::: {.idea}
Taylor says \( f(\a+\h) - f(\a) \) is \( \tfrac12 q(\h) \) plus a remainder that is smaller than \( \norm{\h}^2 \) near \( \0 \), where \( q(\h) = \h\tp\H_f(\a)\h \). For (a) the quadratic term is at least \( \tfrac12\lambda\norm{\h}^2 \) by @lem-definite-form-bounded-below, which beats a remainder eventually smaller than \( \tfrac14\lambda\norm{\h}^2 \); so the difference is positive. For (c) there is no bound in every direction, and none is needed: walk along a single line \( \h = t\u \) where \( q(\u) > 0 \), and the whole thing is \( t^2 \) times something tending to \( \tfrac12q(\u) > 0 \). One direction up, one direction down, and no extremum.
:::

::: {.proof}
Write \( \H = \H_f(\a) \) and \( q(\h) = \h\tp\H\h \). Since \( \a \) is critical, \( \nabla f(\a) = \0 \), so (A2) reads
\[
f(\a+\h) - f(\a) = \tfrac12 q(\h) + r(\h),
\qquad \frac{r(\h)}{\norm{\h}^2} \to 0 .
\tag{$\ast$}
\]

(a) Let \( \lambda > 0 \) be the smallest eigenvalue of \( \H \), so that \( q(\h) \ge \lambda\norm{\h}^2 \) by @lem-definite-form-bounded-below. Since \( r(\h)/\norm{\h}^2 \to 0 \), there is \( \delta > 0 \) with \( \a + \h \in U \) and \( \lvert r(\h)\rvert \le \tfrac14\lambda\norm{\h}^2 \) whenever \( 0 < \norm{\h} < \delta \). For such \( \h \), by \( (\ast) \),
\[
f(\a+\h) - f(\a) \ \ge\ \tfrac12\lambda\norm{\h}^2 - \tfrac14\lambda\norm{\h}^2
= \tfrac14\lambda\norm{\h}^2 > 0 .
\]
So \( f(\a + \h) > f(\a) \) for every \( \h \ne \0 \) with \( \norm{\h} < \delta \), which is what "strict local minimum" says.

(b) The Hessian of \( -f \) at \( \a \) is \( -\H \), whose inertia is \( (n, 0, 0) \) because that of \( \H \) is \( (0, n, 0) \); so \( -\H \) is positive definite by @thm-definiteness-by-signature (a). Part (a) applied to \( -f \) makes \( \a \) a strict local minimum of \( -f \), that is a strict local maximum of \( f \).

(c) By @thm-definiteness-by-signature (e) there are \( \u, \w \in \nR^n \) with \( q(\u) > 0 \) and \( q(\w) < 0 \); both are non-zero, since \( q(\0) = 0 \). Fix \( t \ne 0 \) small and put \( \h = t\u \). Then \( q(t\u) = t^2q(\u) \), so \( (\ast) \) gives
\[
\frac{f(\a + t\u) - f(\a)}{t^2}
= \tfrac12 q(\u) + \frac{r(t\u)}{t^2} .
\]
Now \( r(t\u)/t^2 = \norm{\u}^2\cdot r(t\u)/\norm{t\u}^2 \to 0 \) as \( t \to 0 \), because \( \norm{t\u} \to 0 \) and \( \norm{\u}^2 \) is a constant. So for all small enough \( t \ne 0 \) the right-hand side is at least \( \tfrac14q(\u) > 0 \), and hence \( f(\a + t\u) > f(\a) \). The same computation with \( \w \) in place of \( \u \) gives \( f(\a + t\w) < f(\a) \) for all small enough \( t \ne 0 \). Every neighborhood of \( \a \) contains points of both kinds, so \( \a \) is neither a local minimum nor a local maximum. This proves the theorem.
:::

Cases (a)–(c) exhaust the non-degenerate ones: if \( n_0 = 0 \) then \( n_+ + n_- = n \), so either \( n_+ = n \), or \( n_- = n \), or both are positive. What is left undecided is exactly \( n_0 > 0 \), and there the test is silent because it has to be.

::: {#exm-classify-critical-points}
[Two critical points of a cubic surface]

Find the critical points of \( f(x,y) = x^3 - 3xy + y^3 \) on \( \nR^2 \) and classify each one.
:::

::: {.solution}
The partial derivatives are \( f_x = 3x^2 - 3y \) and \( f_y = -3x + 3y^2 \). Setting both to zero gives \( y = x^2 \) and \( x = y^2 \), hence \( x = x^4 \), so \( x(x^3 - 1) = 0 \) and \( x \in \{0, 1\} \). The real critical points are \( (0,0) \) and \( (1,1) \).

Differentiating again,
\[
\H_f(x,y) = \begin{pmatrix} 6x & -3 \\ -3 & 6y\end{pmatrix} .
\]

At \( (0,0) \) the Hessian is \( \begin{psmallmatrix} 0 & -3 \\ -3 & 0\end{psmallmatrix} \), with \( \det = -9 < 0 \). A \( 2 \times 2 \) symmetric matrix with negative determinant has eigenvalue product \( -9 \), hence one eigenvalue of each sign, so its inertia is \( (1,1,0) \) by @thm-inertia-from-eigenvalues and the form is indefinite. By @thm-second-derivative-test (c), \( (0,0) \) is a saddle point. Concretely \( f(t,t) = 2t^3 - 3t^2 < 0 \) and \( f(t,-t) = 3t^2 > 0 \) for small \( t > 0 \).

At \( (1,1) \) the Hessian is \( \begin{psmallmatrix} 6 & -3 \\ -3 & 6\end{psmallmatrix} \), whose leading principal minors are \( 6 > 0 \) and \( 36 - 9 = 27 > 0 \). By @prp-definiteness-tests-for-forms (a) it is positive definite, so \( (1,1) \) is a strict local minimum, with value \( f(1,1) = -1 \).
:::

::: {#exm-degenerate-hessian}
[One Hessian, three answers]

The three functions
\[
g_1 = x^2 + y^4, \qquad g_2 = x^2 - y^4, \qquad g_3 = x^2
\]
all have \( \nabla g_i(0,0) = \0 \) and the same Hessian at the origin. What is that Hessian, and what happens at the origin in each case?
:::

::: {.solution}
Every second derivative of \( y^4 \) vanishes at \( y = 0 \), so all three have
\[
\H_{g_i}(0,0) = \begin{pmatrix} 2 & 0 \\ 0 & 0\end{pmatrix},
\]
with inertia \( (1, 0, 1) \): positive semidefinite, not definite, not indefinite. The test is silent, and it must be, because the three answers differ. For \( g_1 \) the origin is a strict local minimum, since \( x^2 + y^4 > 0 \) away from \( \0 \). For \( g_2 \) it is a saddle: \( g_2(t,0) = t^2 > 0 \) and \( g_2(0,t) = -t^4 < 0 \) for \( t \ne 0 \). For \( g_3 \) it is a minimum but not a strict one, since \( g_3 \) vanishes along the whole \( y \)-axis. The quadratic term decided nothing here; the quartic term decided everything.
:::

::: {.warning}
**The test reads the signature, not the determinant.** In two variables the familiar rule is "\( \det \H > 0 \) and \( f_{xx} > 0 \) means a minimum", and the second half is not decoration: \( \diag(-1,-1) \) has \( \det = 1 > 0 \), and \( -x^2-y^2 \) has a strict local **maximum** at the origin. All \( \det\H > 0 \) says in two variables is that \( n_0 = 0 \) and \( n_- \) is even — definite, of a sign the determinant cannot see. In three variables it says even less: \( \diag(1,-1,-1) \) has \( \det = 1 > 0 \) and is indefinite.
:::

## Exercises

### A. Check your understanding

::: {#exr-definiteness-and-second-derivatives-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define what it means for a symmetric bilinear form on a real vector space to be **indefinite**.
2. State the signature condition equivalent to negative semidefiniteness, and the one equivalent to positive definiteness.
3. Determine whether the following statement is correct, and justify your answer: a symmetric form that is not positive semidefinite is indefinite.
4. Name the two results of analysis that @thm-second-derivative-test assumes, and say which part of its proof uses each.
5. A critical point has \( n_0 = 2 \) and \( n_- = 0 \). What does @thm-second-derivative-test conclude?
:::
:::

::: {.solution}
(a) \( \beta \) is indefinite if there exist \( \u \) and \( \w \) in \( V \) with \( q(\u) > 0 \) and \( q(\w) < 0 \), where \( q(\v) = \beta(\v,\v) \).

(b) Negative semidefinite \( \iff n_+ = 0 \); positive definite \( \iff (n_+, n_-, n_0) = (n, 0, 0) \), equivalently \( n_+ = n \). Both are @thm-definiteness-by-signature.

(c) Incorrect. The form \( q(x_1,x_2) = -x_1^2 \) has inertia \( (0,1,1) \); it is not positive semidefinite, since \( q(\e_1) = -1 \), and not indefinite, since \( q \) is never positive. Failing (b) of @def-definiteness-of-a-form means only \( n_- > 0 \); being indefinite needs \( n_+ > 0 \) as well.

(d) Symmetry of the mixed second partial derivatives, which makes the Hessian symmetric so that it has an inertia at all; and Taylor's theorem with a second-order remainder, which is the identity \( (\ast) \) that every part of the proof manipulates.

(e) Nothing. Here \( n_+ = n - 2 \) and \( n_- = 0 \), so the Hessian is positive semidefinite but not definite and not indefinite, and none of (a), (b), (c) applies. @exm-degenerate-hessian shows that all of "strict minimum", "non-strict minimum" and "saddle" really do occur in this situation.
:::

### B. Practice

::: {#exr-definiteness-and-second-derivatives-b1}
[B1: Classify by the signature]

Determine the definiteness of each of the following real symmetric matrices, and give the inertia of each. Justify your answers.
\[
\A_1 = \begin{pmatrix} 2 & 1 \\ 1 & 2\end{pmatrix},\quad
\A_2 = \begin{pmatrix} -1 & 2 \\ 2 & -5\end{pmatrix},\quad
\A_3 = \begin{pmatrix} 1 & 2 \\ 2 & 1\end{pmatrix}.
\]
:::

::: {.solution}
For \( \A_1 \): \( \det(\A_1)_1 = 2 > 0 \) and \( \det \A_1 = 4 - 1 = 3 > 0 \), so \( \A_1 \) is positive definite by @prp-definiteness-tests-for-forms (a), with inertia \( (2,0,0) \).

For \( \A_2 \): \( (-1)^1\det(\A_2)_1 = 1 > 0 \) and \( (-1)^2\det\A_2 = 5 - 4 = 1 > 0 \), so \( \A_2 \) is negative definite by @prp-definiteness-tests-for-forms (b), with inertia \( (0,2,0) \).

For \( \A_3 \): \( \det\A_3 = 1 - 4 = -3 < 0 \), so the two eigenvalues have product \( -3 \) and hence opposite signs. The inertia is \( (1,1,0) \) by @thm-inertia-from-eigenvalues, and \( \A_3 \) is indefinite by @thm-definiteness-by-signature (e). Explicitly \( q(1,1) = 6 > 0 \) and \( q(1,-1) = -2 < 0 \).
:::

::: {#exr-definiteness-and-second-derivatives-b2}
[B2: Critical points of a quartic]

Find all critical points of \( f(x,y) = x^4 + y^4 - 4xy \) and classify each with @thm-second-derivative-test.
:::

::: {.solution}
\( f_x = 4x^3 - 4y \) and \( f_y = 4y^3 - 4x \), so \( y = x^3 \) and \( x = y^3 = x^9 \). Then \( x(x^8 - 1) = 0 \), so \( x \in \{0, 1, -1\} \) and the critical points are \( (0,0) \), \( (1,1) \), \( (-1,-1) \). The Hessian is
\[
\H_f(x,y) = \begin{pmatrix} 12x^2 & -4 \\ -4 & 12y^2\end{pmatrix}.
\]
At \( (0,0) \) it is \( \begin{psmallmatrix} 0 & -4 \\ -4 & 0\end{psmallmatrix} \), with determinant \( -16 < 0 \), hence inertia \( (1,1,0) \) and a saddle point. At \( (\pm1,\pm1) \) it is \( \begin{psmallmatrix} 12 & -4 \\ -4 & 12\end{psmallmatrix} \), with leading minors \( 12 > 0 \) and \( 144 - 16 = 128 > 0 \), hence positive definite: both are strict local minima, each of value \( f = 1 + 1 - 4 = -2 \).
:::

### C. Going deeper

::: {#exr-definiteness-and-second-derivatives-c1}
[C1: The signature measures positive subspaces]

Let \( \beta \) be a symmetric bilinear form on a real vector space \( V \) of dimension \( n \), with inertia \( (n_+, n_-, n_0) \). Call a subspace \( U \subseteq V \) **positive** if \( q(\v) > 0 \) for every non-zero \( \v \in U \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( V \) has a positive subspace of dimension \( n_+ \).
2. Prove that every positive subspace has dimension at most \( n_+ \). *Hint: consider a subspace on which \( q \le 0 \) of the largest available dimension.*
3. Hence deduce that \( n_+ \) equals the largest dimension of a positive subspace, and that this gives a second proof that \( n_+ \) does not depend on the orthogonal basis.
:::
:::

::: {.solution}
Fix an orthogonal basis \( \sB = (\v_1, \dots, \v_n) \) for \( \beta \), ordered so that \( d_i = q(\v_i) > 0 \) for \( i \le n_+ \), then negative, then zero.

(a) Put \( U = \Span(\v_1, \dots, \v_{n_+}) \). For a non-zero \( \v = \sum_{i \le n_+} c_i\v_i \), @eq-diagonal-quadratic-form gives \( q(\v) = \sum_{i\le n_+} d_ic_i^2 > 0 \), since every \( d_i > 0 \) and some \( c_i \ne 0 \). So \( U \) is positive of dimension \( n_+ \).

(b) Put \( U' = \Span(\v_{n_++1}, \dots, \v_n) \), of dimension \( n - n_+ \). For \( \v \in U' \), @eq-diagonal-quadratic-form gives \( q(\v) = \sum_{i > n_+} d_ic_i^2 \le 0 \), every \( d_i \) there being \( \le 0 \). Let \( W \) be any positive subspace. Then \( W \cap U' = \{\0\} \), since a non-zero vector in the intersection would have \( q > 0 \) and \( q \le 0 \). By the dimension formula (@thm-dimension-formula-subspace-dim),
\[
\dim W + (n - n_+) = \dim(W + U') \le n ,
\]
so \( \dim W \le n_+ \).

(c) By (a) and (b) the largest dimension of a positive subspace is exactly \( n_+ \). That description mentions only \( \beta \) and \( V \), no basis, so \( n_+ \) is an invariant of \( \beta \). Together with the invariance of \( \rank\beta = n_+ + n_- \) under congruence (@thm-congruence-preserves-rank) this recovers @thm-sylvester-inertia.
:::

::: {#exr-definiteness-and-second-derivatives-c2}
[C2: A saddle the determinant hides]

Let \( f(x,y,z) = x^2 - y^2 - z^2 + xyz \).

::: {.enumerate options="label=(\alph*)"}
1. Verify that the origin is a critical point and compute \( \H_f(\0) \) and its determinant.
2. Classify the origin, and explain why the sign of \( \det \H_f(\0) \) alone would have been useless.
3. Prove that no twice continuously differentiable \( g \colon \nR^3 \to \nR \) has a strict local maximum at a critical point \( \0 \) with \( \det\H_g(\0) > 0 \), and give a \( g \colon \nR^2 \to \nR \) that does. Which feature of the dimension is responsible?
:::
:::

::: {.solution}
(a) \( f_x = 2x + yz \), \( f_y = -2y + xz \), \( f_z = -2z + xy \), all zero at \( \0 \). The second derivatives at \( \0 \) are \( f_{xx} = 2 \), \( f_{yy} = f_{zz} = -2 \), and \( f_{xy} = z \), \( f_{xz} = y \), \( f_{yz} = x \), all zero at \( \0 \). So \( \H_f(\0) = \diag(2,-2,-2) \), with \( \det = 8 > 0 \).

(b) The inertia is \( (1,2,0) \), so the Hessian is indefinite and \( \0 \) is a saddle point by @thm-second-derivative-test (c). The determinant is the product of the eigenvalues (@cor-det-product-eigenvalues-again) and therefore records only the parity of \( n_- \); here \( \det > 0 \) says \( n_- \) is even, which is equally true of the negative definite \( \diag(-2,-2,-2) \) and of the positive definite \( \I_3 \). It cannot distinguish them.

(c) Suppose \( \0 \) is a local maximum of \( g \) and write \( q(\h) = \h\tp\H_g(\0)\h \). If \( q(\u) > 0 \) for some \( \u \), the computation in the proof of @thm-second-derivative-test (c) gives \( g(t\u) > g(\0) \) for all small \( t \ne 0 \), contradicting the maximum. So \( q(\u) \le 0 \) for every \( \u \), that is \( \H_g(\0) \) is negative semidefinite and \( n_+ = 0 \) by @thm-definiteness-by-signature (d). If moreover \( \det \H_g(\0) > 0 \) then \( 0 \) is not an eigenvalue, so \( n_0 = 0 \) and the inertia is \( (0,3,0) \). But then \( \det\H_g(\0) = \lambda_1\lambda_2\lambda_3 \) is a product of three negative numbers, hence negative — a contradiction. On \( \nR^2 \) there is no obstruction: \( g(x,y) = -x^2 - y^2 \) has \( \H_g(\0) = -2\I_2 \), determinant \( 4 > 0 \), and a strict local maximum at \( \0 \). The responsible feature is the parity of the dimension: the determinant is the product of \( n \) eigenvalues, so a negative definite Hessian has \( \det \) of sign \( (-1)^n \).
:::
