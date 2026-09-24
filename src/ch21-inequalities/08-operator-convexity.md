# Operator Convex Functions

Chapter 17 §11 defined two notions side by side and then spent itself on one of them. Operator monotonicity got four families of examples, a warning and a classification to look forward to; operator convexity got one proposition — that \( t \mapsto t^2 \) is operator convex (@prp-square-operator-convex) — and then the chapter moved on. This section repays the debt. It collects the examples that are within reach, and it proves the one structural theorem the notion has: an inequality of Jensen's type that survives being squeezed by a contraction. That theorem is what makes operator convexity useful rather than merely curious.

**Throughout, \( F = \nR \) or \( F = \nC \)**, every matrix whose spectrum is named is Hermitian, and \( I \) denotes an **interval** of real numbers. The letter \( I \) is plain italic and is not the identity matrix \( \I \). For \( f \colon I \to \nR \) and Hermitian \( \A \) with \( \spec(\A) \subseteq I \), the matrix \( f(\A) \) is the one built by the functional calculus of Chapter 12 §08 (@def-function-of-normal-operator), and it is Hermitian because \( f \) is real-valued (@thm-functional-calculus-properties (c)).

## What operator convexity asks

Recall the definition. A function \( f \colon I \to \nR \) is **operator convex on \( I \)** if, for **every** size \( n \ge 1 \), all Hermitian \( \A, \B \in M_n(F) \) with spectra in \( I \), and every \( \theta \in [0, 1] \),
\[
f\bigl(\theta\A + (1-\theta)\B\bigr) \ \preceq\ \theta f(\A) + (1 - \theta)f(\B)
\]
in the Loewner order (@def-operator-monotone (b), @def-loewner-order). It is **operator concave** when \( -f \) is operator convex. Chapter 17 §11 checked that the left-hand side makes sense: the spectrum of a convex combination of two Hermitian matrices with spectra in \( I \) again lies in \( I \).

Taking \( n = 1 \) turns every matrix into a number and the Loewner order into \( \ge \), so an operator convex function is convex in the sense of @def-convex-function. As with monotonicity, the content lies in the sizes \( n \ge 2 \), and the clause "for every \( n \)" is what makes the class small.

Two facts from Chapter 17 §11 are the starting stock. Affine functions are operator convex and operator concave at once, with equality in the definition (@prp-affine-operator-monotone), and \( t \mapsto t^2 \) is operator convex on \( \nR \), because
\[
\theta\A^2 + (1-\theta)\B^2 - \bigl(\theta\A + (1-\theta)\B\bigr)^2 = \theta(1-\theta)(\A - \B)^2
\]
and the square of a Hermitian matrix is positive semidefinite (@prp-square-operator-convex).

Before adding to the stock we record three bookkeeping identities. Each says that a familiar operation on matrices passes through the functional calculus untouched, and each is used below without further comment.

:::: {#lem-functional-calculus-conjugation}
[Three Ways to Move the Functional Calculus]

Let \( I \subseteq \nR \) be an interval and \( f \colon I \to \nR \).

::: {.enumerate options="label=(\alph*)"}
1. **(Shift.)** Let \( s \in \nR \), let \( g(t) = f(t + s) \) on \( I - s \), and let \( \A \) be Hermitian with \( \spec(\A) \subseteq I - s \). Then \( g(\A) = f(\A + s\I) \).
2. **(Unitary conjugation.)** Let \( \A \) be Hermitian with \( \spec(\A) \subseteq I \) and let \( \U \) be unitary of the same size. Then \( \spec(\U^{*}\A\U) = \spec(\A) \) and
\[
f(\U^{*}\A\U) = \U^{*}f(\A)\U .
\]
3. **(Direct sums.)** Let \( \A, \B \) be Hermitian with spectra in \( I \). Then \( f(\A \oplus \B) = f(\A) \oplus f(\B) \).
:::
::::

::: {.proof}
Write the spectral resolution \( \A = \sum_j\mu_j\P_j \) with distinct \( \mu_j \) (@def-spectral-resolution, @thm-spectral-resolution).

(a) The numbers \( \mu_j + s \) are distinct, and \( \A + s\I = \sum_j(\mu_j + s)\P_j \) by @thm-spectral-resolution (c) and (d). The \( \P_j \) are non-zero self-adjoint idempotents, pairwise annihilating and summing to \( \I \) (@thm-spectral-resolution (b), (c)), so this is the spectral resolution of \( \A + s\I \) by @thm-spectral-resolution-unique. Hence \( f(\A + s\I) = \sum_jf(\mu_j + s)\P_j = \sum_jg(\mu_j)\P_j = g(\A) \), using @def-function-of-normal-operator twice.

(b) Put \( \Q_j = \U^{*}\P_j\U \). Each \( \Q_j \) is self-adjoint, \( \Q_j^2 = \U^{*}\P_j\U\U^{*}\P_j\U = \Q_j \), and \( \Q_i\Q_j = \0 \) for \( i \ne j \), all because \( \U\U^{*} = \I \); moreover \( \sum_j\Q_j = \U^{*}\I\U = \I \) and \( \Q_j \ne \0 \) since \( \U \) is invertible. Also \( \U^{*}\A\U = \sum_j\mu_j\Q_j \). So this is the spectral resolution of \( \U^{*}\A\U \) by @thm-spectral-resolution-unique, its distinct eigenvalues are the \( \mu_j \), and
\[
f(\U^{*}\A\U) = \sum_jf(\mu_j)\Q_j = \U^{*}\Bigl(\sum_jf(\mu_j)\P_j\Bigr)\U = \U^{*}f(\A)\U .
\]

(c) Let \( \nu_1, \dots, \nu_r \) be the distinct elements of \( \spec(\A) \cup \spec(\B) \). For each \( \nu \), let \( \P_{\nu}^{\A} \) be the orthogonal projection onto \( E_{\nu}(\A) \), understood as \( \0 \) when \( \nu \notin \spec(\A) \), and likewise \( \P_{\nu}^{\B} \). A vector \( (\x, \y) \) satisfies \( (\A \oplus \B)(\x, \y) = \nu(\x, \y) \) exactly when \( \A\x = \nu\x \) and \( \B\y = \nu\y \), so \( E_{\nu}(\A \oplus \B) = E_{\nu}(\A) \oplus E_{\nu}(\B) \), whose orthogonal projection is \( \P_{\nu}^{\A} \oplus \P_{\nu}^{\B} \). Hence \( \spec(\A \oplus \B) = \{\nu_1, \dots, \nu_r\} \subseteq I \) and, by @def-function-of-normal-operator,
\[
f(\A \oplus \B) = \sum_{\nu}f(\nu)\bigl(\P^{\A}_{\nu} \oplus \P^{\B}_{\nu}\bigr) = f(\A) \oplus f(\B) .
\]
:::

## The examples we can prove

Operator convex functions form a cone, exactly as the operator monotone ones do, and for the same reason.

:::: {#prp-operator-convex-cone}
[Combining Operator Convex Functions]

Let \( f \) and \( g \) be operator convex on \( I \).

::: {.enumerate options="label=(\alph*)"}
1. For all \( c \ge 0 \) and \( \alpha, \beta \in \nR \), the functions \( f + g \) and \( \alpha + \beta t + cf(t) \) are operator convex on \( I \).
2. For every \( s \in \nR \), the translate \( t \mapsto f(t + s) \) is operator convex on \( I - s \).
:::
::::

::: {.proof}
(a) Fix Hermitian \( \A, \B \) of the same size with spectra in \( I \), fix \( \theta \in [0, 1] \) and put \( \C = \theta\A + (1-\theta)\B \). By @thm-functional-calculus-properties (b), the defect
\[
D_h \coloneqq \theta h(\A) + (1-\theta)h(\B) - h(\C)
\]
satisfies \( D_{f + g} = D_f + D_g \) and \( D_{cf} = c\,D_f \). Both \( D_f \) and \( D_g \) are \( \succeq 0 \) by hypothesis, so for every \( \x \) the quadratic forms add and scale to something \( \ge 0 \), giving \( D_{f+g} \succeq 0 \) and \( D_{cf} \succeq 0 \). Adding an affine function changes nothing, since \( D_h = \0 \) for affine \( h \) by @prp-affine-operator-monotone.

(b) Let \( g(t) = f(t + s) \) and let \( \A, \B \) be Hermitian with spectra in \( I - s \). Then \( \A + s\I \) and \( \B + s\I \) have spectra in \( I \), and \( \theta(\A + s\I) + (1-\theta)(\B + s\I) = \C + s\I \). By @lem-functional-calculus-conjugation (a) applied three times,
\[
g(\C) = f(\C + s\I) \preceq \theta f(\A + s\I) + (1-\theta)f(\B + s\I) = \theta g(\A) + (1-\theta)g(\B) .
\]
:::

The new example is the reciprocal. Chapter 17 §11 left it as an exercise; part (d) of the theorem below rests on it, so it is proved here. The proof is the one the exercise's hint pointed at, and the whole content is that a positive definite matrix and its inverse sit in a single positive semidefinite block matrix.

:::: {#thm-operator-convex-examples}
[Four Operator Convex Functions]

::: {.enumerate options="label=(\alph*)"}
1. Every affine function \( t \mapsto \alpha + \beta t \) is operator convex and operator concave on \( \nR \).
2. \( t \mapsto t^2 \) is operator convex on \( \nR \), hence on every interval.
3. \( t \mapsto 1/t \) is operator convex on \( (0, \infty) \); equivalently, \( t \mapsto -1/t \) is operator concave there.
4. For every \( c > 0 \), the function \( t \mapsto 1/(t + c) \) is operator convex on \( (0, \infty) \), and \( t \mapsto t/(t + c) \) is operator **concave** there.
:::
::::

::: {.idea}
Only (c) is new. For numbers, \( 1/t \) is convex because \( 1/t \) is the smallest \( u \) with \( tu \ge 1 \), and "\( tu \ge 1 \)" is a condition that survives averaging. The matrix version of "\( tu \ge 1 \)" is that the block matrix \( \begin{psmallmatrix} \A & \I \\ \I & \U \end{psmallmatrix} \) is positive semidefinite, and Chapter 13 §06 reads that off a Schur complement. Averaging two such blocks averages the corners, and reading the Schur complement backwards turns the average back into an inequality between matrices.
:::

::: {.proof}
(a) is @prp-affine-operator-monotone and (b) is @prp-square-operator-convex. Restricting to a smaller interval only shrinks the supply of matrices, so both persist on every interval.

(c) **Claim.** For every \( \G \succ 0 \) in \( M_n(F) \), the Hermitian block matrix
\[
\M_{\G} = \begin{pmatrix} \G & \I_n \\ \I_n & \G^{-1} \end{pmatrix}
\]
is positive semidefinite.

::: {.proof}
The inverse of a Hermitian invertible matrix is Hermitian, since \( (\G^{-1})^{*} = (\G^{*})^{-1} = \G^{-1} \), so \( \M_{\G} \) is Hermitian. Its corner \( \G \) is \( \succ 0 \), and its Schur complement is \( \M_{\G}/\G = \G^{-1} - \I_n\G^{-1}\I_n = \0 \succeq 0 \). By @thm-block-psd-schur (b), \( \M_{\G} \succeq 0 \).
:::

Now let \( \A, \B \in M_n(F) \) be Hermitian with spectra in \( (0, \infty) \), so \( \A \succ 0 \) and \( \B \succ 0 \) by @thm-pd-characterizations (b), and let \( \theta \in [0, 1] \). Put \( \C = \theta\A + (1 - \theta)\B \). For \( \x \ne \0 \),
\[
\inner{\C\x}{\x} = \theta\inner{\A\x}{\x} + (1-\theta)\inner{\B\x}{\x} > 0 ,
\]
since both terms are \( \ge 0 \) and at least one coefficient is positive; hence \( \C \succ 0 \). By the Claim, \( \M_{\A} \succeq 0 \) and \( \M_{\B} \succeq 0 \), so their convex combination
\[
\theta\M_{\A} + (1-\theta)\M_{\B} = \begin{pmatrix} \C & \I_n \\ \I_n & \theta\A^{-1} + (1-\theta)\B^{-1} \end{pmatrix}
\]
has non-negative quadratic form at every vector and is therefore \( \succeq 0 \). Its corner \( \C \) is \( \succ 0 \), so @thm-block-psd-schur (b) applies in the other direction and gives
\[
\theta\A^{-1} + (1-\theta)\B^{-1} - \C^{-1} \ \succeq\ 0 .
\]
Since \( t \mapsto 1/t \) sends a positive definite matrix to its inverse (@def-function-of-normal-operator, as recalled in Chapter 17 §11), this is exactly the inequality required of \( f(t) = 1/t \). The size \( n \) was arbitrary.

(d) By (c) and @prp-operator-convex-cone (b), \( t \mapsto 1/(t + c) \) is operator convex on \( (0, \infty) - c = (-c, \infty) \), hence on the smaller interval \( (0, \infty) \). Finally \( t/(t + c) = 1 - c\cdot\frac{1}{t + c} \), which is an affine function minus a non-negative multiple of an operator convex function, so it is operator concave by @prp-operator-convex-cone (a) applied to \( -f \).
:::

::: {.remark}
Compare the list with Chapter 17 §11's list of operator monotone functions. The two overlap only in the affine ones: \( t^2 \) is operator convex and not operator monotone, \( -1/t \) is operator monotone and not even convex, and \( t/(t+c) \) is both operator monotone (@cor-shifted-inverse-operator-monotone) and operator concave. Two further examples, \( -\log t \) and \( t\log t \), are operator convex on \( (0, \infty) \); both proofs need an integral representation that §10 of this chapter supplies, so they are postponed to there.
:::

## Convex is not operator convex

The gap between convexity and operator convexity is as wide as the gap between increasing and operator monotone, and a single cube exposes it.

:::: {#exm-cube-not-operator-convex}
[The Cube Is Convex and Not Operator Convex]

Let
\[
\A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \qquad \B = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} .
\]
Show that \( \A \succeq 0 \) and \( \B \succ 0 \), and that with \( \theta = \tfrac12 \) the inequality required of \( f(t) = t^3 \) on \( [0, \infty) \) fails.
::::

::: {.solution}
\( \A \) is diagonal with non-negative entries, so \( \A \succeq 0 \) with spectrum \( \{0, 1\} \). \( \B \) is real symmetric with leading principal minors \( 2 \) and \( 2 - 1 = 1 \), both positive, so \( \B \succ 0 \) by Sylvester's criterion (@thm-pd-characterizations (d)). Both spectra lie in \( [0, \infty) \), and so does that of \( \tfrac12(\A + \B) \), a convex combination of two positive semidefinite matrices.

Now compute. \( \A^3 = \A \). From \( \B^2 = \begin{psmallmatrix} 5 & 3 \\ 3 & 2\end{psmallmatrix} \) we get \( \B^3 = \begin{psmallmatrix} 13 & 8 \\ 8 & 5\end{psmallmatrix} \). Also \( \A + \B = \begin{psmallmatrix} 3 & 1 \\ 1 & 1\end{psmallmatrix} \), whose square is \( \begin{psmallmatrix} 10 & 4 \\ 4 & 2\end{psmallmatrix} \) and whose cube is \( \begin{psmallmatrix} 34 & 14 \\ 14 & 6\end{psmallmatrix} \). Hence, clearing the denominator by a factor \( 8 \),
\[
8\Bigl(\tfrac12(\A^3 + \B^3) - \bigl(\tfrac12(\A + \B)\bigr)^3\Bigr)
= 4(\A^3 + \B^3) - (\A + \B)^3
= \begin{pmatrix} 22 & 18 \\ 18 & 14 \end{pmatrix} .
\]
Its determinant is \( 22 \cdot 14 - 18^2 = 308 - 324 = -16 < 0 \), so it is not positive semidefinite (@thm-psd-characterizations (e)). A witness needs no eigenvalues: with \( \x = (2, -3) \),
\[
\x\tp\begin{pmatrix} 22 & 18 \\ 18 & 14 \end{pmatrix}\x = 4 \cdot 22 - 12 \cdot 18 + 9 \cdot 14 = 88 - 216 + 126 = -2 < 0 .
\]
By @thm-functional-calculus-properties (a), \( t \mapsto t^3 \) sends a Hermitian matrix to its cube, so \( t^3 \) is not operator convex on \( [0, \infty) \). It is nevertheless convex there in the ordinary sense, since its second derivative \( 6t \) is \( \ge 0 \) (@thm-convex-second-derivative).
:::

::: {.warning}
**Convexity of \( f \) is not enough, already at size \( 2 \).** Every \( t^p \) with \( p \ge 1 \) is convex on \( [0, \infty) \), and the exponents \( 3 \) and \( 4 \) already fail to be operator convex. The trace does not notice the difference: §02's @thm-trace-convex makes \( \A \mapsto \tr f(\A) \) convex for **every** convex \( f \), and in @exm-cube-not-operator-convex the trace of the displayed matrix is \( 22 + 14 = 36 > 0 \), exactly as that theorem predicts, while the matrix itself is indefinite. A convex function controls the sum of the eigenvalues; an operator convex function controls the matrix.
:::

::: {.check}
Is \( t \mapsto t^4 \) operator convex on \( [0, \infty) \), because \( t^4 = (t^2)^2 \) is a composite of two operator convex functions?
:::

::: {.solution}
No. @prp-operator-convex-cone covers sums and non-negative multiples, never composites, and there is no reason it should: operator convexity of \( g \) constrains \( g \) on convex combinations of matrices, while \( (g \circ f)(\A) = g(f(\A)) \) asks about \( g \) at the matrix \( f(\A) \), which is a different question. The same pair as in @exm-cube-not-operator-convex settles it. From \( \A^4 = \A \), \( \B^4 = \begin{psmallmatrix} 34 & 21 \\ 21 & 13\end{psmallmatrix} \) and \( (\A+\B)^4 = \begin{psmallmatrix} 116 & 48 \\ 48 & 20\end{psmallmatrix} \),
\[
4\Bigl(\tfrac12(\A^4 + \B^4) - \bigl(\tfrac12(\A+\B)\bigr)^4\Bigr) = \begin{pmatrix} 41 & 30 \\ 30 & 21 \end{pmatrix} ,
\]
whose determinant is \( 861 - 900 = -39 < 0 \). A witness is \( \x = (3, -4) \), giving \( 9\cdot41 - 24\cdot30 + 16\cdot21 = -15 < 0 \).
:::

## Contractions and their dilations

The theorem this section is heading for compares \( f(\V^{*}\A\V) \) with \( \V^{*}f(\A)\V \). The matrices \( \V \) for which this can possibly work are the ones that do not stretch: otherwise \( \V^{*}\A\V \) can leave the interval where \( f \) lives.

*A contraction is a matrix that never lengthens a vector.*

::: {#def-matrix-contraction}
[Contraction]

Let \( \V \in M_{n \times m}(F) \). Then \( \V \) is a **contraction** if \( \V^{*}\V \preceq \I_m \), that is, if \( \norm{\V\x} \le \norm{\x} \) for every \( \x \in F^m \). It is an **isometry** if \( \V^{*}\V = \I_m \).
:::

The word is overloaded: Chapter 15 §04 uses **contraction** for the pairing \( V^{*} \otimes V \to F \) (@def-contraction), which is a different object entirely, and the two never appear together. The two phrasings above agree because \( \inner{(\I_m - \V^{*}\V)\x}{\x} = \norm{\x}^2 - \norm{\V\x}^2 \). Examples: every unitary matrix; every orthogonal projection \( \P \), since \( \P^{*}\P = \P^2 = \P \preceq \I \) (@def-loewner-order); the matrix \( \tfrac12\I \); and any matrix whose columns are an orthonormal list, which is an isometry. A non-example by minimal change: \( 2\I \) fails, since \( \I - (2\I)^{*}(2\I) = -3\I \) is not positive semidefinite.

The key structural fact is that a contraction is always the corner of a unitary matrix of twice the size. This is the **dilation**, and it is how a statement about contractions gets converted into a statement about unitary conjugation, which the functional calculus understands.

::: {#lem-block-dilation}
[Unitary Dilation of a Contraction]

Let \( \V \in M_{n \times m}(F) \) be a contraction, and set
\[
\D_1 = (\I_m - \V^{*}\V)^{1/2}, \qquad \D_2 = (\I_n - \V\V^{*})^{1/2} .
\]
Then \( \I_m - \V^{*}\V \succeq 0 \) and \( \I_n - \V\V^{*} \succeq 0 \), so both square roots exist, and the \( (n + m) \times (n + m) \) matrix
\[
\U = \begin{pmatrix} \V & \D_2 \\ \D_1 & -\V^{*} \end{pmatrix}
\]
is unitary.
:::

::: {.idea}
Only one of the four block identities needs an idea: \( \V^{*}\D_2 = \D_1\V^{*} \), which says that \( \V^{*} \) intertwines the two square roots. It holds for \( \V^{*}(\I - \V\V^{*}) = (\I - \V^{*}\V)\V^{*} \) by one line of algebra, hence for every polynomial in the two matrices, and the positive square root **is** a polynomial (@thm-psd-square-root (a)) — provided one polynomial can be chosen to serve both matrices at once, which Lagrange interpolation allows.
:::

::: {.proof}
Write \( \M = \I_m - \V^{*}\V \) and \( \N = \I_n - \V\V^{*} \). By hypothesis \( \M \succeq 0 \), which says \( \norm{\V\x} \le \norm{\x} \) for every \( \x \in F^m \). For \( \N \), fix \( \y \in F^n \) and put \( \z = \V^{*}\y \). Then, by Cauchy–Schwarz (@thm-cauchy-schwarz) and the contraction property applied to \( \z \),
\[
\norm{\z}^2 = \inner{\V\z}{\y} \ \le\ \norm{\V\z}\,\norm{\y} \ \le\ \norm{\z}\,\norm{\y} ,
\]
the first equality because \( \inner{\V\z}{\y} = \y^{*}\V\V^{*}\y = \norm{\V^{*}\y}^2 \). If \( \z \ne \0 \) we may divide by \( \norm{\z} > 0 \) to get \( \norm{\V^{*}\y} \le \norm{\y} \), and if \( \z = \0 \) that inequality is immediate. Hence \( \inner{\N\y}{\y} = \norm{\y}^2 - \norm{\V^{*}\y}^2 \ge 0 \) for every \( \y \), so \( \N \succeq 0 \). Both square roots now exist and are Hermitian, by @thm-psd-square-root.

**Claim.** \( \V^{*}\N^{1/2} = \M^{1/2}\V^{*} \).

::: {.proof}
First, \( \V^{*}\N = \V^{*} - \V^{*}\V\V^{*} = \M\V^{*} \). Hence \( \V^{*}\N^{k} = \M^{k}\V^{*} \) for every integer \( k \ge 0 \), by induction: the case \( k = 0 \) is trivial, and \( \V^{*}\N^{k+1} = (\V^{*}\N)\N^{k} = \M(\V^{*}\N^{k}) = \M^{k+1}\V^{*} \). Therefore \( \V^{*}q(\N) = q(\M)\V^{*} \) for every polynomial \( q \) with real coefficients.

The set \( \spec(\M) \cup \spec(\N) \) is finite and contained in \( [0, \infty) \), so by Lagrange interpolation (@thm-lagrange-interpolation) there is a real polynomial \( q \) with \( q(\nu) = \sqrt{\nu} \) for every \( \nu \) in it. By @thm-functional-calculus-properties (a) and @def-function-of-normal-operator, \( q(\M) = \sum_j q(\mu_j)\P_j = \sum_j\sqrt{\mu_j}\P_j = \M^{1/2} \), and likewise \( q(\N) = \N^{1/2} \). Substituting \( q \) into the displayed identity proves the claim.
:::

Taking adjoints in the claim, and using that \( \M^{1/2} \) and \( \N^{1/2} \) are Hermitian, gives \( \N^{1/2}\V = \V\M^{1/2} \). Now compute, in blocks (@thm-block-multiplication),
\[
\begin{aligned}
\U^{*}\U &= \begin{pmatrix} \V^{*} & \D_1 \\ \D_2 & -\V \end{pmatrix}\begin{pmatrix} \V & \D_2 \\ \D_1 & -\V^{*} \end{pmatrix} \\
&= \begin{pmatrix} \V^{*}\V + \D_1^2 & \V^{*}\D_2 - \D_1\V^{*} \\ \D_2\V - \V\D_1 & \D_2^2 + \V\V^{*}\end{pmatrix} .
\end{aligned}
\]
The top-left block is \( \V^{*}\V + \M = \I_m \) and the bottom-right is \( \N + \V\V^{*} = \I_n \), both by the definition of \( \M \) and \( \N \). The top-right block is \( \0 \) by the Claim, and the bottom-left is \( \0 \) by its adjoint form. So \( \U^{*}\U = \I_{m+n} \), and since \( \U \) is square this makes \( \U \) unitary (@thm-invertible-tfae).
:::

::: {.check}
Take \( m = n = 1 \) and \( \V = (c) \) with \( c \) real, \( \lvert c \rvert \le 1 \). What is the dilation?
:::

::: {.solution}
\( \D_1 = \D_2 = (\sqrt{1 - c^2}) \), so \( \U = \begin{psmallmatrix} c & \sqrt{1-c^2} \\ \sqrt{1-c^2} & -c \end{psmallmatrix} \). Writing \( c = \cos\varphi \) with \( \varphi \in [0, \pi] \), so that \( \sin\varphi \ge 0 \) and \( \sqrt{1 - c^2} = \sin\varphi \), this is the reflection matrix \( \begin{psmallmatrix} \cos\varphi & \sin\varphi \\ \sin\varphi & -\cos\varphi\end{psmallmatrix} \), which is orthogonal with determinant \( -1 \). So the lemma is the statement that every number in \( [-1, 1] \) is the corner of a \( 2 \times 2 \) reflection — the sentence "\( \cos^2\varphi + \sin^2\varphi = 1 \)", read as a matrix identity.
:::

## Jensen's inequality for operators

Here is the theorem. In words: **squeezing first and then applying \( f \) is at most applying \( f \) first and then squeezing**, provided \( f \) is operator convex and does not reward the squeezing at the origin.

::: {#thm-jensen-operator}
[Hansen–Pedersen–Jensen Inequality]

Let \( I \subseteq \nR \) be an interval with \( 0 \in I \), let \( f \colon I \to \nR \) be operator convex on \( I \), let \( \A \in M_n(F) \) be Hermitian with \( \spec(\A) \subseteq I \), and let \( \V \in M_{n \times m}(F) \) be a contraction. Then \( \spec(\V^{*}\A\V) \subseteq I \), and
\[
f(\V^{*}\A\V) \ \preceq\ \V^{*}f(\A)\V + f(0)\bigl(\I_m - \V^{*}\V\bigr) .
\]
In particular:

::: {.enumerate options="label=(\alph*)"}
1. if \( f(0) \le 0 \), then \( f(\V^{*}\A\V) \preceq \V^{*}f(\A)\V \);
2. if \( \V \) is an isometry, then \( f(\V^{*}\A\V) \preceq \V^{*}f(\A)\V \), with no condition on \( f(0) \).
:::
:::

::: {.idea}
Dilate. Once \( \V \) sits in the corner of a unitary \( \U \), the matrix \( \V^{*}\A\V \) sits in the corner of \( \U^{*}(\A \oplus \0)\U \), which is a unitary conjugate of \( \A \oplus \0 \) and therefore has the same spectrum. Conjugating a second time by the sign matrix \( \W = \I_m \oplus (-\I_n) \) flips the off-diagonal blocks, so **averaging the two conjugates deletes them**: the average is block diagonal, with \( \V^{*}\A\V \) in the corner. Operator convexity applied to that average, and then reading off the top-left block, is the whole proof. The term \( f(0)(\I - \V^{*}\V) \) is the residue of the zero block we padded with.
:::

::: {.proof}
**The spectrum.** Let \( \x \in F^m \) be a unit eigenvector of the Hermitian matrix \( \V^{*}\A\V \), with eigenvalue \( \mu \). If \( \V\x = \0 \), then \( \mu = \inner{\V^{*}\A\V\x}{\x} = 0 \in I \). Otherwise put \( \y = \V\x/\norm{\V\x} \) and \( \tau = \norm{\V\x}^2 \), so \( 0 < \tau \le 1 \) because \( \V \) is a contraction, and
\[
\mu = \inner{\A\V\x}{\V\x} = \tau\inner{\A\y}{\y} .
\]
By @lem-extreme-eigenvalues-quadratic-form, \( \inner{\A\y}{\y} \) lies between \( \lambda_n(\A) \) and \( \lambda_1(\A) \), hence in \( I \), since \( I \) is an interval containing the spectrum. Then \( \mu = \tau\inner{\A\y}{\y} + (1 - \tau)\cdot 0 \) is a convex combination of two points of \( I \), so \( \mu \in I \). The same argument applies to \( \D_2 = (\I_n - \V\V^{*})^{1/2} \): it is Hermitian with \( \D_2^{*}\D_2 = \I_n - \V\V^{*} \preceq \I_n \), because \( \V\V^{*} \succeq 0 \), so it is a contraction. Hence \( \spec(\D_2\A\D_2) \subseteq I \).

**The two conjugates.** Let \( \U \) be the dilation of @lem-block-dilation and put
\[
\M = \A \oplus \0_m, \qquad \W = \I_m \oplus (-\I_n) ,
\]
so that \( \W \) is unitary and Hermitian, and \( \spec(\M) = \spec(\A) \cup \{0\} \subseteq I \). Multiplying out in blocks,
\[
\U^{*}\M\U = \begin{pmatrix} \V^{*}\A\V & \V^{*}\A\D_2 \\ \D_2\A\V & \D_2\A\D_2 \end{pmatrix} ,
\]
and conjugating by \( \W \) negates the two off-diagonal blocks. Hence, with \( \X = \U^{*}\M\U \) and \( \Y = (\U\W)^{*}\M(\U\W) = \W^{*}\X\W \),
\[
\tfrac12(\X + \Y) = \bigl(\V^{*}\A\V\bigr) \oplus \bigl(\D_2\A\D_2\bigr) . \tag{$\ast$}
\]
Both \( \X \) and \( \Y \) are unitary conjugates of \( \M \), so both are Hermitian with spectrum \( \spec(\M) \subseteq I \) by @lem-functional-calculus-conjugation (b).

**Convexity.** Apply @def-operator-monotone (b) with \( \theta = \tfrac12 \) to \( \X \) and \( \Y \), then @lem-functional-calculus-conjugation (b) twice:
\[
f\bigl(\tfrac12(\X + \Y)\bigr) \preceq \tfrac12\bigl(\U^{*}f(\M)\U + \W^{*}\U^{*}f(\M)\U\W\bigr) .
\]
By @lem-functional-calculus-conjugation (c), \( f(\M) = f(\A) \oplus f(0)\I_m \). The same block computation as before, now with \( f(\A) \) in place of \( \A \) and \( f(0)\I_m \) in place of \( \0_m \), gives
\[
\U^{*}f(\M)\U = \begin{pmatrix} \V^{*}f(\A)\V + f(0)\D_1^2 & \ast \\ \ast & \ast \end{pmatrix} ,
\]
and averaging with its \( \W \)-conjugate again deletes the off-diagonal blocks. On the left, @lem-functional-calculus-conjugation (c) and \( (\ast) \) give \( f(\tfrac12(\X+\Y)) = f(\V^{*}\A\V) \oplus f(\D_2\A\D_2) \). So the inequality reads, between two block diagonal matrices,
\[
f(\V^{*}\A\V) \oplus f(\D_2\A\D_2) \ \preceq\ \bigl(\V^{*}f(\A)\V + f(0)\D_1^2\bigr) \oplus \Z
\]
for some Hermitian \( \Z \). The difference of the two sides is positive semidefinite, so its top-left \( m \times m \) block is too, by @thm-block-psd-schur (a). Since \( \D_1^2 = \I_m - \V^{*}\V \), that block inequality is the displayed statement of the theorem.

(a) If \( f(0) \le 0 \), then \( f(0)(\I_m - \V^{*}\V) \preceq 0 \), because \( \I_m - \V^{*}\V \succeq 0 \) and a non-positive multiple of a positive semidefinite matrix has non-positive quadratic form. Adding it can only decrease, so \( \V^{*}f(\A)\V + f(0)(\I_m - \V^{*}\V) \preceq \V^{*}f(\A)\V \), and transitivity of \( \preceq \) (@prp-loewner-partial-order) finishes.

(b) If \( \V^{*}\V = \I_m \) the extra term is \( \0 \).
:::

The special case worth remembering separately takes \( \V \) to be a projection. It says that **an operator convex function commutes with compression, up to the right inequality**.

::: {#cor-operator-convex-compression}
[Compression]

Let \( I \) be an interval with \( 0 \in I \), let \( f \colon I \to \nR \) be operator convex with \( f(0) \le 0 \), let \( \A \in M_n(F) \) be Hermitian with \( \spec(\A) \subseteq I \), and let \( \P \in M_n(F) \) be the matrix of an orthogonal projection. Then \( \spec(\P\A\P) \subseteq I \) and
\[
f(\P\A\P) \ \preceq\ \P f(\A)\P .
\]
:::

::: {.proof}
\( \P \) is Hermitian with \( \P^{*}\P = \P^2 = \P \preceq \I \), so \( \P \) is a contraction (@def-matrix-contraction). Apply @thm-jensen-operator (a) with \( \V = \P \), noting \( \P^{*}\A\P = \P\A\P \).
:::

::: {.warning}
**The condition \( f(0) \le 0 \) is not decoration.** Take \( f(t) = t^2 + 1 \), operator convex on \( \nR \) by @prp-operator-convex-cone (a), with \( f(0) = 1 > 0 \). Take \( \A = \0_n \) and \( \V = \0_{n \times m} \), a contraction. Then \( f(\V^{*}\A\V) = f(\0_m) = \I_m \) while \( \V^{*}f(\A)\V = \0 \), so the conclusion of @thm-jensen-operator (a) fails as badly as it can. The full inequality of the theorem survives: its right-hand side is \( \0 + 1 \cdot \I_m = \I_m \), with equality.
:::

::: {.check}
Why can the hypothesis "\( \V \) is a contraction" not be dropped in @cor-operator-convex-compression by rescaling — that is, why does the corollary for \( \P \) not give a version for \( c\P \) with \( c > 1 \)?
:::

::: {.solution}
Because both sides scale differently. For \( f(t) = t^2 \) and \( \V = c\I \) the claimed inequality would read \( c^4\A^2 \preceq c^2\A^2 \), which fails for every \( c > 1 \) and every \( \A \) with \( \A^2 \ne \0 \). The contraction hypothesis is what keeps the left-hand side from being inflated, and it enters the proof twice: it puts \( \spec(\V^{*}\A\V) \) back inside \( I \), which is what makes \( f(\V^{*}\A\V) \) defined at all, and it gives the square roots of @lem-block-dilation something to be square roots of.
:::

## Where this sits

Two convexity statements about matrices are now on the table, and they are of very different strengths.

- §02's @thm-trace-convex: for **every** convex \( f \), the function \( \A \mapsto \tr f(\A) \) is convex on the Hermitian matrices with spectrum in \( I \). This is a statement about one real number attached to the matrix.
- Operator convexity: for a much smaller class of \( f \), the matrices themselves are ordered. @exm-cube-not-operator-convex shows \( t^3 \) in the first class and not the second.

The Hansen–Pedersen–Jensen inequality is the reason the smaller class is worth isolating. A trace inequality cannot be compressed: knowing \( \tr f(\A) \) says nothing about \( \tr f(\P\A\P) \), since the compression changes the eigenvalues in ways the trace does not track. What @cor-operator-convex-compression compares is not the traces but the matrices, \( f(\P\A\P) \) with \( \P f(\A)\P \), and it is the step that later turns an operator convex function into an inequality between matrices of different sizes. Section 10 of this chapter adds \( -\log t \) and \( t\log t \) to the list of operator convex functions, and §11 uses the operator monotonicity of \( t^{1/2} \) to build the geometric mean of two positive definite matrices.

## Exercises

### A. Check your understanding

:::: {#exr-operator-convexity-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State what it means for \( f \colon I \to \nR \) to be operator convex, and say what the clause "for every \( n \)" ranges over.
2. Explain why an operator convex function is convex, and name a convex function that is not operator convex.
3. Decide whether the following is correct, and justify your answer: if \( f \) is operator convex on \( I \) and \( c < 0 \), then \( cf \) is operator convex on \( I \).
4. State the Hansen–Pedersen–Jensen inequality, and say which hypothesis fails for \( f(t) = t^2 + 1 \).
5. Is \( t \mapsto -1/t \) operator convex on \( (0, \infty) \)? Is it operator concave there?
:::
::::

::: {.solution}
(a) For every \( n \ge 1 \), all Hermitian \( \A, \B \in M_n(F) \) with spectra in \( I \) and every \( \theta \in [0,1] \), \( f(\theta\A + (1-\theta)\B) \preceq \theta f(\A) + (1-\theta)f(\B) \) (@def-operator-monotone (b)). The clause ranges over all matrix sizes at once.

(b) Taking \( n = 1 \) turns the matrices into numbers and \( \preceq \) into \( \le \), which is @def-convex-function. The function \( t \mapsto t^3 \) is convex on \( [0, \infty) \) and not operator convex there (@exm-cube-not-operator-convex).

(c) Incorrect: @prp-operator-convex-cone (a) requires \( c \ge 0 \). For \( c = -1 \) and \( f(t) = t^2 \), the claim would make \( -t^2 \) operator convex, that is \( t^2 \) operator concave; but @prp-square-operator-convex gives \( \theta\A^2 + (1-\theta)\B^2 - (\theta\A + (1-\theta)\B)^2 = \theta(1-\theta)(\A-\B)^2 \), which is non-zero for \( \A \ne \B \) and \( 0 < \theta < 1 \), so the reverse inequality fails.

(d) @thm-jensen-operator: for \( f \) operator convex on an interval containing \( 0 \), \( \A \) Hermitian with spectrum in that interval and \( \V \) a contraction, \( f(\V^{*}\A\V) \preceq \V^{*}f(\A)\V + f(0)(\I - \V^{*}\V) \). The last term vanishes when \( \V \) is an isometry, and when \( f(0) \le 0 \) it is \( \preceq \0 \) and may be discarded, which leaves \( f(\V^{*}\A\V) \preceq \V^{*}f(\A)\V \) in both cases. For \( f(t) = t^2 + 1 \) the failing hypothesis is \( f(0) \le 0 \).

(e) It is not operator convex: at \( n = 1 \) the scalar function \( -1/t \) is not convex, since at \( 1 \), \( 3 \) and their midpoint \( 2 \) the value \( -\tfrac12 \) exceeds the chord's \( -\tfrac23 \). It **is** operator concave, by @thm-operator-convex-examples (c).
:::

### B. Practice

:::: {#exr-operator-convexity-b1}
[B1: Which are operator convex?]

Determine which of the following functions are operator convex on the interval given. Justify your answer.

::: {.enumerate options="label=(\roman*)"}
1. \( f(t) = 7 - 3t \) on \( \nR \).
2. \( f(t) = 2t^2 + 5t - 1 \) on \( \nR \).
3. \( f(t) = \dfrac{4}{t + 3} \) on \( (0, \infty) \).
4. \( f(t) = \dfrac{t}{t + 3} \) on \( (0, \infty) \).
5. \( f(t) = t^3 \) on \( [0, \infty) \).
:::
::::

::: {.solution}
(i) Operator convex (and concave), by @thm-operator-convex-examples (a).

(ii) Operator convex: it is \( 2 \) times \( t^2 \) plus the affine function \( 5t - 1 \), so @prp-operator-convex-cone (a) applies with \( c = 2 \ge 0 \).

(iii) Operator convex, by @thm-operator-convex-examples (d) with \( c = 3 \) and @prp-operator-convex-cone (a) with the factor \( 4 \ge 0 \).

(iv) Not operator convex; it is operator **concave** by @thm-operator-convex-examples (d). Operator convexity would force ordinary convexity at \( n = 1 \), and \( t/(t+3) = 1 - 3/(t+3) \) has second derivative \( -6/(t+3)^3 < 0 \) on \( (0, \infty) \), so it is strictly concave there (@thm-convex-second-derivative).

(v) Not operator convex, by @exm-cube-not-operator-convex.
:::

:::: {#exr-operator-convexity-b2}
[B2: A dilation by hand]

Let \( \V = \begin{pmatrix} \tfrac12 & 0 \\ 0 & 0 \end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Verify that \( \V \) is a contraction and compute \( \D_1 = (\I_2 - \V^{*}\V)^{1/2} \) and \( \D_2 = (\I_2 - \V\V^{*})^{1/2} \).
2. Write down the \( 4 \times 4 \) matrix \( \U \) of @lem-block-dilation and verify directly that its first column is a unit vector orthogonal to its third column.
:::
::::

::: {.solution}
(a) \( \V^{*}\V = \V\V^{*} = \diag(\tfrac14, 0) \), so \( \I_2 - \V^{*}\V = \diag(\tfrac34, 1) \succeq 0 \), and \( \V \) is a contraction. Both \( \I_2 - \V^{*}\V \) and \( \I_2 - \V\V^{*} \) equal \( \diag(\tfrac34, 1) \), a diagonal matrix with non-negative entries, so
\[
\D_1 = \D_2 = \diag\bigl(\tfrac{\sqrt3}{2},\, 1\bigr) ,
\]
the unique positive semidefinite square root (@thm-psd-square-root).

(b) With the blocks in the order of the lemma,
\[
\U = \begin{pmatrix}
\tfrac12 & 0 & \tfrac{\sqrt3}{2} & 0 \\
0 & 0 & 0 & 1 \\
\tfrac{\sqrt3}{2} & 0 & -\tfrac12 & 0 \\
0 & 1 & 0 & 0
\end{pmatrix}.
\]
Its first column is \( (\tfrac12, 0, \tfrac{\sqrt3}{2}, 0) \), of squared length \( \tfrac14 + \tfrac34 = 1 \). Its third column is \( (\tfrac{\sqrt3}{2}, 0, -\tfrac12, 0) \), and the inner product of the two is \( \tfrac12\cdot\tfrac{\sqrt3}{2} + \tfrac{\sqrt3}{2}\cdot(-\tfrac12) = 0 \).
:::

:::: {#exr-operator-convexity-b3}
[B3: Compression of a square]

Let
\[
\A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}, \qquad \P = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} .
\]
Compute \( (\P\A\P)^2 \) and \( \P\A^2\P \), and verify the inequality of @cor-operator-convex-compression for \( f(t) = t^2 \). Hence state what the inequality says about the entry in position \( (1,1) \).
::::

::: {.solution}
\( \P \) is the orthogonal projection onto \( \Span(\e_1) \), and \( \P\A\P = \diag(2, 0) \), so \( (\P\A\P)^2 = \diag(4, 0) \). From \( \A^2 = \begin{psmallmatrix} 5 & 3 \\ 3 & 2\end{psmallmatrix} \) we get \( \P\A^2\P = \diag(5, 0) \). Hence
\[
\P\A^2\P - (\P\A\P)^2 = \diag(1, 0) \ \succeq\ 0 ,
\]
as @cor-operator-convex-compression predicts for \( f(t) = t^2 \), which is operator convex with \( f(0) = 0 \). In position \( (1,1) \) the inequality says \( (\A^2)_{11} \ge (a_{11})^2 \), that is \( 5 \ge 4 \): the \( (1,1) \) entry of \( \A^2 \) is \( \sum_j\lvert a_{1j}\rvert^2 \), which exceeds \( \lvert a_{11}\rvert^2 \) by the contribution of the off-diagonal entries.
:::

### C. Going deeper

:::: {#exr-operator-convexity-c1}
[C1: The square, without the dilation]

Let \( \A \in M_n(F) \) be Hermitian and let \( \V \in M_{n \times m}(F) \) be a contraction.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( (\V^{*}\A\V)^2 \preceq \V^{*}\A^2\V \) directly, without using @thm-jensen-operator.
2. Which hypothesis of @thm-jensen-operator does your proof use, and which does it not?
:::

*Hint for (a): insert \( \I - \V\V^{*} \).*
::::

::: {.solution}
(a) Compute the difference and factor it:
\[
\V^{*}\A^2\V - (\V^{*}\A\V)^2 = \V^{*}\A\A\V - \V^{*}\A\V\V^{*}\A\V = \V^{*}\A(\I_n - \V\V^{*})\A\V .
\]
As in the proof of @lem-block-dilation, \( \I_n - \V\V^{*} \succeq 0 \) because \( \V \) is a contraction. Writing \( \S = \A\V \), the right-hand side is \( \S^{*}(\I_n - \V\V^{*})\S \), which is \( \succeq 0 \) by @prp-congruence-positivity (a). Hence \( (\V^{*}\A\V)^2 \preceq \V^{*}\A^2\V \).

(b) It uses the contraction hypothesis, in the single step \( \I_n - \V\V^{*} \succeq 0 \). It does not use \( f(0) \le 0 \) — but it does not need to, since \( f(t) = t^2 \) has \( f(0) = 0 \).
:::

:::: {#exr-operator-convexity-c2}
[C2: Shrinking the matrix]

Let \( I \) be an interval with \( 0 \in I \), let \( f \) be operator convex on \( I \) with \( f(0) \le 0 \), and let \( \A \in M_n(F) \) be Hermitian with \( \spec(\A) \subseteq I \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( f(\theta\A) \preceq \theta f(\A) \) for every \( \theta \in [0, 1] \), assuming \( \spec(\theta\A) \subseteq I \).
2. Give an operator convex \( f \) with \( f(0) > 0 \) for which (a) fails, and say at which \( \theta \).
3. Let \( \V \in M_{n \times 1}(F) \) be a unit column vector and \( g(t) = t^2 + 1 \) on \( \nR \). Write out what @thm-jensen-operator (b) says here, and verify it for \( \A = \begin{psmallmatrix} 2 & 1 \\ 1 & 1\end{psmallmatrix} \) and \( \V = \e_1 \).
:::

*Hint for (a): a scalar multiple of the identity is a contraction when the scalar is small.*
::::

::: {.solution}
(a) Put \( \V = \sqrt{\theta}\,\I_n \), which is Hermitian with \( \V^{*}\V = \theta\I_n \preceq \I_n \), so \( \V \) is a contraction (@def-matrix-contraction). Then \( \V^{*}\A\V = \theta\A \) and \( \V^{*}f(\A)\V = \theta f(\A) \). By @thm-jensen-operator (a),
\[
f(\theta\A) = f(\V^{*}\A\V) \ \preceq\ \V^{*}f(\A)\V = \theta f(\A) .
\]

(b) Take \( f(t) = t^2 + 1 \), operator convex on \( \nR \) by @prp-operator-convex-cone (a), with \( f(0) = 1 > 0 \). At \( \theta = 0 \) the claim reads \( f(\0) \preceq \0 \), that is \( \I_n \preceq \0 \), which is false. In fact it fails at every \( \theta < 1 \): the claim is \( \theta^2\A^2 + \I \preceq \theta\A^2 + \theta\I \), which rearranges to \( (1 - \theta)\I \preceq (\theta - \theta^2)\A^2 \), and for \( \A = \0 \) the right-hand side is \( \0 \) while the left-hand side is \( \succ 0 \).

(c) A unit column \( \V \) satisfies \( \V^{*}\V = (1) = \I_1 \), so it is an isometry and (b) of the theorem applies with no condition on \( g(0) = 1 \). It says \( g(\V^{*}\A\V) \preceq \V^{*}g(\A)\V \), which for \( 1 \times 1 \) matrices is the number inequality \( (\V^{*}\A\V)^2 + 1 \le \V^{*}(\A^2 + \I)\V \). With \( \V = \e_1 \): \( \e_1^{*}\A\e_1 = 2 \), so the left side is \( 5 \); and \( \A^2 = \begin{psmallmatrix} 5 & 3 \\ 3 & 2\end{psmallmatrix} \), so the right side is \( 5 + 1 = 6 \). Indeed \( 5 \le 6 \).
:::

:::: {#exr-operator-convexity-c3}
[C3: What the trace does not see]

Let \( \A = \diag(1, 0) \) and \( \B = \begin{psmallmatrix} 2 & 1 \\ 1 & 1 \end{psmallmatrix} \) be the matrices of @exm-cube-not-operator-convex, and let \( f(t) = t^3 \) on \( [0, \infty) \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \tr\bigl(\tfrac12(\A^3 + \B^3)\bigr) - \tr\bigl((\tfrac12(\A+\B))^3\bigr) \), and say which theorem makes its sign predictable.
2. The same defect matrix is indefinite. Explain, in one sentence, why (a) and that fact are consistent.
3. Give a convex function \( g \) on \( [0, \infty) \) for which the defect matrix at this pair \( \A, \B \) is positive semidefinite, and name the reason.
:::
::::

::: {.solution}
(a) From @exm-cube-not-operator-convex the defect is \( \tfrac18\begin{psmallmatrix} 22 & 18 \\ 18 & 14\end{psmallmatrix} \), whose trace is \( \tfrac18(22 + 14) = \tfrac92 > 0 \). Its sign is predictable from @thm-trace-convex: \( t \mapsto t^3 \) is convex on \( [0, \infty) \), so \( \A \mapsto \tr(\A^3) \) is a convex function of the Hermitian matrix, and the defect of a convex function at a midpoint is \( \ge 0 \).

(b) A Hermitian \( 2 \times 2 \) matrix can have positive trace and a negative eigenvalue; the trace only sees the **sum** of the eigenvalues, and here they are approximately \( 4.55 \) and \( -0.055 \).

(c) Take \( g(t) = t^2 \). By @prp-square-operator-convex the defect equals \( \tfrac14(\A - \B)^2 \), a non-negative multiple of the square of a Hermitian matrix, hence \( \succeq 0 \). Explicitly \( \A - \B = \begin{psmallmatrix} -1 & -1 \\ -1 & -1\end{psmallmatrix} \), so the defect is \( \tfrac14\begin{psmallmatrix} 2 & 2 \\ 2 & 2\end{psmallmatrix} = \begin{psmallmatrix} 1/2 & 1/2 \\ 1/2 & 1/2\end{psmallmatrix} \succeq 0 \).
:::
