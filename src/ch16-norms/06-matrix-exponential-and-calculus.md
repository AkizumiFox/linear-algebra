# Bounds for the Exponential, and Two Derivatives

Chapter 10 §09 built \( e^{\A} \) out of a series and closed with a promise: "Chapter 16 will return to \( e^{\A} \) with norms available, which give quantitative bounds instead of exact formulas." That is what this section does. It does not rebuild the exponential; @def-matrix-exponential and @thm-exponential-series-converges stand as they are, and the Jordan form is not touched. What is new is that the series now has a size, so its sum has a ceiling, its truncation has an error bound, and its behavior as \( t \to \infty \) has a rate.

The second half takes the other step Chapter 10 could not: it differentiates. The derivative of the determinant and the derivative of the inverse are both needed later in the book, and both require one fact from calculus that linear algebra does not supply. That fact is stated before it is used.

**Throughout, \( \norm{\cdot} \) is the operator norm on \( M_n(\nC) \) induced by a norm on \( \nC^{n} \)** (@def-operator-norm), so \( \norm{\I} = 1 \) and \( \norm{\X\Y} \le \norm{\X}\norm{\Y} \) (@thm-operator-norm-properties (c), (d)).

## How big is the exponential

Chapter 10 §10's criteria answered *whether*; the norm answers *how much*. The bound to aim at is the one the scalar case suggests: \( \lvert e^{z}\rvert \le e^{\lvert z\rvert} \), because the series has non-negative terms once every term is replaced by its modulus. The matrix proof is the same sentence with submultiplicativity in place of \( \lvert zw\rvert = \lvert z\rvert\lvert w\rvert \).

One scalar fact is needed and is not on the chapter's list of imports. We name it here rather than let it in quietly.

::: {.remark}
**A quoted fact.** For every real \( s \ge 0 \) the series \( \sum_{m \ge 0}s^{m}/m! \) converges, with sum \( e^{s} \). This is fact (A1) of Chapter 10 §09, quoted there and quoted again here; this book does not prove it. Because its terms are non-negative, its partial sums increase to \( e^{s} \), so every partial sum is at most \( e^{s} \) — that last step is **(A2), monotone convergence**, from the list in this chapter's introduction.
:::

::: {#thm-exponential-norm-bound}
[Bounds for the Exponential]

Let \( \A \in M_n(\nC) \) and write \( a = \norm{\A} \). Then

::: {.enumerate options="label=(\alph*)"}
1. \( \norm{e^{\A}} \le e^{a} \);
2. \( \norm{e^{\A} - \I} \le e^{a} - 1 \);
3. \( \norm{e^{\A} - \I - \A} \le e^{a} - 1 - a \le \dfrac{a^{2}e^{a}}{2} \).
:::

In particular \( \norm{e^{t\A}} \le e^{\lvert t\rvert a} \) for every real \( t \).
:::

::: {.idea}
All three are the same computation stopped at a different place: bound the norm of a partial sum by the corresponding partial sum of \( \sum s^{m}/m! \), then let the partial sums converge. The only thing that needs care is the passage to the limit, and @lem-reverse-triangle-norm does it, exactly as in @thm-neumann-series. For the second inequality in (c), compare \( m! \) with \( 2\,(m-2)! \).
:::

::: {.proof}
Write \( \S_M = \sum_{m=0}^{M}\A^{m}/m! \). By @thm-exponential-series-converges the sequence \( (\S_M) \) converges entrywise to \( e^{\A} \), hence \( \norm{\S_M - e^{\A}} \to 0 \) by @cor-entrywise-convergence-is-the-convergence, hence \( \norm{\S_M} \to \norm{e^{\A}} \) by @lem-reverse-triangle-norm. The same three steps apply to \( \S_M - \I \) and to \( \S_M - \I - \A \). So in each part it suffices to bound the partial sums, uniformly in \( M \).

(a) Submultiplicativity gives \( \norm{\A^{m}} \le a^{m} \) for \( m \ge 1 \), by induction, and \( \norm{\A^{0}} = \norm{\I} = 1 \). By subadditivity and the quoted fact above,
\[
\norm{\S_M} \le \sum_{m=0}^{M}\frac{\norm{\A^{m}}}{m!} \le \sum_{m=0}^{M}\frac{a^{m}}{m!} \le e^{a} .
\]
Letting \( M \to \infty \) gives \( \norm{e^{\A}} \le e^{a} \).

(b) The same estimate with the term \( m = 0 \) removed:
\[
\norm{\S_M - \I} \le \sum_{m=1}^{M}\frac{a^{m}}{m!} \le e^{a} - 1 ,
\]
since the partial sums of \( \sum_{m \ge 1}a^{m}/m! \) increase to \( e^{a} - 1 \).

(c) Removing the terms \( m = 0 \) and \( m = 1 \) in the same way gives
\[
\norm{e^{\A} - \I - \A} \le \sum_{m \ge 2}\frac{a^{m}}{m!} = e^{a} - 1 - a .
\]
For the second inequality, note that \( m! = m(m-1)\,(m-2)! \ge 2\,(m-2)! \) for every \( m \ge 2 \), so \( a^{m}/m! \le \tfrac12 a^{2}\cdot a^{m-2}/(m-2)! \). Summing over \( m \ge 2 \) and substituting \( l = m - 2 \),
\[
\sum_{m \ge 2}\frac{a^{m}}{m!} \le \frac{a^{2}}{2}\sum_{l \ge 0}\frac{a^{l}}{l!} = \frac{a^{2}e^{a}}{2} .
\]

The final claim is (a) applied to \( t\A \), whose norm is \( \lvert t\rvert a \) by homogeneity. This proves the theorem.
:::

Part (c) is the statement that \( e^{\A} \) agrees with \( \I + \A \) to second order in \( \norm{\A} \), with an explicit constant. It is the bound one uses when \( \A \) is a small perturbation, and it is the counterpart, for the exponential, of @thm-neumann-series (c).

::: {#exm-exponential-bound-sharp-and-not}
[Where the bound is exact, and where it is useless]

Compare \( \norm{e^{\A}}_2 \) with \( e^{\norm{\A}_2} \) for

::: {.enumerate options="label=(\alph*)"}
1. \( \A = \diag(2, 1) \);
2. \( \A = \begin{pmatrix} 0 & 1 \\ -1 & 0\end{pmatrix} \), and more generally \( t\A \) for \( t > 0 \).
:::
:::

::: {.solution}
(a) \( \A \) is Hermitian, hence normal, so its singular values are the moduli of its eigenvalues and \( \norm{\A}_2 = 2 \) by @thm-operator-norm-formulas (c). By @def-matrix-function-jordan (or directly from the series, entry by entry) \( e^{\A} = \diag(e^{2}, e) \), again normal, so \( \norm{e^{\A}}_2 = e^{2} \). The bound \( e^{\norm{\A}_2} = e^{2} \) is attained exactly. The same happens for every \( \A = c\I \) with \( c > 0 \), so no constant smaller than \( 1 \) can be inserted in @thm-exponential-norm-bound (a).

(b) \( \A^{2} = -\I \), so \( \A^{3} = -\A \), \( \A^{4} = \I \), and grouping the series by parity gives, using fact (A1) of Chapter 10 §09 for the series of \( \cos \) and \( \sin \) and its (A3) to rearrange a convergent series into its even and odd parts,
\[
e^{t\A} = (\cos t)\I + (\sin t)\A = \begin{pmatrix} \cos t & \sin t \\ -\sin t & \cos t\end{pmatrix},
\]
a real orthogonal matrix. Hence \( \norm{e^{t\A}}_2 = 1 \) for every \( t \), while \( \norm{t\A}_2 = t \) and the bound reads \( e^{t} \). At \( t = 10 \) the bound is about \( 22026 \) and the truth is \( 1 \).
:::

::: {.warning}
**The bound sees only the size of \( \A \), never the direction of its spectrum.** Part (b) above is the extreme case: \( \norm{e^{t\A}} \) stays at \( 1 \) while \( e^{t\norm{\A}} \) runs away. The reason is that @thm-exponential-norm-bound throws away every cancellation in the series at the first step, when \( \norm{\A^{m}} \) is replaced by \( \norm{\A}^{m} \). Any statement about \( e^{t\A} \) for **large** \( t \) must come from the eigenvalues instead, which is the subject of the next subsection.
:::

::: {.check}
Why does @thm-exponential-norm-bound (a) fail for the Frobenius norm, and what is the correct statement for it?
:::

::: {.solution}
Because \( \norm{\I_n}_F = \sqrt n \), so already at \( \A = 0 \) the claim reads \( \sqrt n \le 1 \). Repeating the proof with the term \( m = 0 \) kept separate gives the correct version for any matrix norm: \( \norm{e^{\A}} \le \norm{\I} + e^{\norm{\A}} - 1 \). This is the same correction as in @exr-neumann-series-c3, and it comes from the same place: only an induced norm has \( \norm{\I} = 1 \).
:::

## Decay in the stable case

The warning above says the bound \( e^{t\norm{\A}} \) is the wrong instrument for large \( t \). The right one reads the eigenvalues, and the bridge to the discrete theory of §04 is the observation that the exponential turns the *real part* of an eigenvalue into a *modulus*.

::: {#lem-spectral-radius-of-exponential}
[The Spectrum of the Exponential]

Let \( \A \in M_n(\nC) \). Then \( \spec(e^{\A}) = \{e^{\lambda} : \lambda \in \spec(\A)\} \), and
\[
\rho(e^{\A}) = e^{\mu}, \qquad \mu = \max\{\operatorname{Re}\lambda : \lambda \in \spec(\A)\} .
\]
:::

::: {.idea}
The eigenvalues of \( e^{\A} \) are the numbers \( e^{\lambda} \) for \( \lambda \in \spec(\A) \), which the Jordan form makes visible. Taking moduli turns \( e^{\lambda} \) into \( e^{\operatorname{Re}\lambda} \), and the largest of finitely many such numbers is the one with the largest exponent.
:::

::: {.proof}
By @thm-jordan-canonical-form there are an invertible \( \P \) and a Jordan matrix \( \J \) with \( \A = \P\J\P^{-1} \), and the diagonal of \( \J \) lists the eigenvalues \( \lambda_1, \dots, \lambda_n \) of \( \A \) with multiplicity. By @thm-exponential-properties (a), \( e^{\J} = e^{\P^{-1}\A\P} = \P^{-1}e^{\A}\P \). By @thm-exponential-series-converges each block \( e^{\J_k(\lambda)} \) is upper triangular with \( e^{\lambda} \) on its diagonal, so \( e^{\J} \) is upper triangular with diagonal \( e^{\lambda_1}, \dots, e^{\lambda_n} \); hence \( \spec(e^{\J}) = \{e^{\lambda_i}\} \) by @thm-diagonal-of-triangular-form (b). Similar matrices have the same characteristic polynomial (@thm-charpoly-similarity-invariant), so \( \spec(e^{\A}) = \spec(e^{\J}) \), which is the first claim.

For the second, \( \lvert e^{\lambda}\rvert = e^{\operatorname{Re}\lambda} \) by fact (A1) of Chapter 10 §09, and \( s \mapsto e^{s} \) is non-decreasing on \( \nR \) — for \( h \ge 0 \), \( e^{s+h} = e^{s}e^{h} \ge e^{s} \) by fact (A1) of Chapter 10 §09 — so the largest of the finitely many numbers \( e^{\operatorname{Re}\lambda_i} \) is \( e^{\mu} \). This proves the lemma.
:::

Chapter 12 §10 called \( \A \) **stable** when every \( \lambda \in \spec(\A) \) has \( \operatorname{Re}\lambda < 0 \) (@def-lyapunov-equation). In the language of the lemma, \( \A \) is stable exactly when \( \rho(e^{\A}) < 1 \) — the continuous-time condition and Chapter 10 §10's discrete-time condition are the same condition, read through the exponential.

::: {#thm-exponential-decay}
[Exponential Decay of a Stable System]

Let \( \A \in M_n(\nC) \), let \( \mu = \max\{\operatorname{Re}\lambda : \lambda \in \spec(\A)\} \), and let \( \nu > \mu \) be real. Then there is a constant \( C \ge 1 \), depending on \( \A \), on \( \nu \) and on the norm, with
\[
\norm{e^{t\A}} \le C\,e^{\nu t} \qquad \text{for every } t \ge 0 .
\]
In particular, if \( \A \) is **stable** then \( \nu \) may be taken negative, and every solution of \( \x' = \A\x \) satisfies
\[
\norm{\x(t)} \le C e^{\nu t}\norm{\x(0)} \xrightarrow[t \to \infty]{} 0 .
\]
:::

::: {.idea}
Sample the flow at integer times and use §04. The matrix \( \M = e^{-\nu}e^{\A} \) has \( \rho(\M) = e^{\mu-\nu} < 1 \) by @lem-spectral-radius-of-exponential, so @cor-powers-converge-iff-rho-lt-one bounds all of its powers by one constant; unwinding the powers gives \( \norm{e^{k\A}} \le C_0e^{\nu k} \) at every integer \( k \). Between the integers, \( e^{t\A} = e^{(t-k)\A}e^{k\A} \) with \( 0 \le t - k < 1 \), and the crude bound @thm-exponential-norm-bound (a) is more than enough to cover a gap of length \( 1 \). The whole point is that the crude bound is applied only on a bounded interval, where crudeness costs a constant and not a rate.
:::

::: {.proof}
Put \( \M = e^{-\nu}e^{\A} \). Multiplying a matrix by a scalar \( c \) multiplies every eigenvalue by \( c \), so by @lem-spectral-radius-of-exponential,
\[
\rho(\M) = e^{-\nu}\rho(e^{\A}) = e^{-\nu}e^{\mu} = e^{\mu - \nu} < 1 ,
\]
using \( \mu - \nu < 0 \). Fix any \( q \) with \( \rho(\M) < q < 1 \). By @cor-powers-converge-iff-rho-lt-one (b) there is \( C_0 \ge 1 \) with \( \norm{\M^{k}} \le C_0q^{k} \le C_0 \) for every integer \( k \ge 0 \).

Since \( \A \) commutes with itself, @thm-exponential-properties (d) gives \( e^{(s+u)\A} = e^{s\A}e^{u\A} \) for all real \( s, u \); in particular \( (e^{\A})^{k} = e^{k\A} \) by induction on \( k \). Hence \( \M^{k} = e^{-\nu k}e^{k\A} \), and
\[
\norm{e^{k\A}} = e^{\nu k}\norm{\M^{k}} \le C_0\,e^{\nu k} \qquad (k = 0, 1, 2, \dots).
\]

Now let \( t \ge 0 \) and let \( k \) be the integer part of \( t \), so that \( k \ge 0 \) and \( 0 \le t - k < 1 \). Then \( e^{t\A} = e^{(t-k)\A}e^{k\A} \), so by submultiplicativity and @thm-exponential-norm-bound (a),
\[
\norm{e^{t\A}} \le \norm{e^{(t-k)\A}}\;\norm{e^{k\A}}
\le e^{(t-k)\norm{\A}}\,C_0e^{\nu k}
\le C_0\,e^{\norm{\A}}\,e^{\nu k} ,
\]
using \( 0 \le t - k < 1 \) in the last step. Finally \( e^{\nu k} = e^{\nu t}e^{-\nu(t-k)} \le e^{\nu t}e^{\lvert\nu\rvert} \), again because \( 0 \le t - k < 1 \). So the constant
\[
C = C_0\,e^{\norm{\A} + \lvert\nu\rvert} \ge 1
\]
works for every \( t \ge 0 \).

For the last statement, suppose \( \A \) is stable, so \( \mu < 0 \), and choose \( \nu \in (\mu, 0) \). By @thm-linear-ode-solution the unique solution with the given initial value is \( \x(t) = e^{t\A}\x(0) \), so \( \norm{\x(t)} \le \norm{e^{t\A}}\norm{\x(0)} \le Ce^{\nu t}\norm{\x(0)} \) by @thm-operator-norm-properties (a). Since \( \nu < 0 \), \( e^{\nu t} \to 0 \) as \( t \to \infty \) — this is fact (A5) of Chapter 10 §09 with \( j = 0 \), quoted there and quoted again here — so \( \norm{\x(t)} \to 0 \), and by @cor-entrywise-convergence-is-the-convergence the vectors \( \x(t) \) tend to \( \0 \). This proves the theorem.
:::

::: {#exm-decay-with-a-transient}
[Decay after a detour]

Let \( \A = \begin{pmatrix} -1 & 5 \\ 0 & -1 \end{pmatrix} \). Find \( \mu \), compute \( \norm{e^{t\A}}_{\infty} \) exactly, and find the smallest constant \( C \) that works in @thm-exponential-decay for \( \nu = -\tfrac12 \).
:::

::: {.solution}
*The eigenvalues.* \( \A \) is upper triangular with both diagonal entries \( -1 \), so \( \spec(\A) = \{-1\} \) (@thm-diagonal-of-triangular-form (b)) and \( \mu = -1 < 0 \): the matrix is stable.

*The exponential.* Write \( \A = -\I + 5\N \) with \( \N = \begin{psmallmatrix} 0&1\\0&0\end{psmallmatrix} \). The two summands commute and \( \N^{2} = 0 \), so @cor-exponential-of-jordan-block gives
\[
e^{t\A} = e^{-t}(\I + 5t\N) = e^{-t}\begin{pmatrix} 1 & 5t \\ 0 & 1\end{pmatrix} .
\]
The absolute row sums are \( e^{-t}(1 + 5t) \) and \( e^{-t} \), so \( \norm{e^{t\A}}_{\infty} = e^{-t}(1 + 5t) \) for \( t \ge 0 \) by @thm-operator-norm-formulas (b).

*The transient.* The function \( t \mapsto e^{-t}(1+5t) \) has derivative \( e^{-t}(4 - 5t) \), so it **rises** from \( 1 \) at \( t = 0 \) to \( 5e^{-4/5} \approx 2.247 \) at \( t = \tfrac45 \), and only then decays. A stable matrix does not decay from the start.

*The constant.* We need the smallest \( C \) with \( e^{-t}(1+5t) \le Ce^{-t/2} \) for all \( t \ge 0 \), that is, \( C = \max_{t \ge 0}(1+5t)e^{-t/2} \). The derivative of \( (1+5t)e^{-t/2} \) is \( e^{-t/2}\bigl(5 - \tfrac12(1+5t)\bigr) \), which is positive for \( t < \tfrac95 \) and negative for \( t > \tfrac95 \), so by fact (A6) of the chapter introduction the maximum is at \( t = \tfrac95 \) and
\[
C = 10\,e^{-9/10} \approx 4.066 .
\]
The rate \( e^{-t/2} \) is honest and the constant pays for the hump.
:::

::: {.remark}
**What this settles from Chapter 12 §10, and what it does not.** That section introduced the Lyapunov equation \( \A\X + \X\A^{*} = -\Q \) and the word *stable* (@def-lyapunov-equation). It then stated, without proof, that a stable \( \A \) and a positive definite \( \Q \) produce a positive definite solution \( \X \), and conversely; it assigned the positivity half to Chapter 13, and assigned to this chapter "the consequence for differential equations — that a stable \( \A \) makes every solution of \( \dot{\x} = \A\x \) decay, with \( \x^{*}\X\x \) as the quantity that measures the decay".

@thm-exponential-decay delivers the decay, with a rate, and does so without the Lyapunov equation at all. What it does not deliver is the existence of a positive definite \( \X \) for a stable \( \A \): that statement is not proved anywhere in this book, and nothing here depends on it. What can be said cheaply is the other half of the connection: **any** positive definite \( \X \) satisfying \( \A^{*}\X + \X\A = -\Q \) with \( \Q \succ 0 \) does measure the decay, in the sense that \( \x^{*}\X\x \) is strictly decreasing along every non-zero solution of \( \x' = \A\x \). That is @exr-matrix-exponential-and-calculus-c3, and it is three lines once the product rule below is available. Note the transpose: the equation the decay computation wants is @def-lyapunov-equation for the pair \( (\A^{*}, \Q) \), and \( \A \) is stable if and only if \( \A^{*} \) is, since the eigenvalues of \( \A^{*} \) are the conjugates of those of \( \A \).
:::

## Differentiating a matrix-valued function

A matrix whose entries vary — a family \( \A(t) \), a curve in \( M_n(F) \) — is differentiated entrywise, exactly as Chapter 10 §09 differentiated \( t \mapsto e^{t\A} \). The two derivatives this book needs later, of \( \det \) and of inversion, are algebraic facts with one analytic ingredient, and the ingredient is named first.

::: {#def-matrix-valued-derivative}
[Derivative of a Matrix-Valued Function]

Let \( I \subseteq \nR \) be an open interval and \( \A \colon I \to M_{m \times n}(\nC) \), written \( \A(t) = (a_{ij}(t)) \). Call \( \A \) **differentiable** at \( t_0 \in I \) if every entry function \( a_{ij} \colon I \to \nC \) is differentiable at \( t_0 \), and then set
\[
\A'(t_0) \coloneqq \bigl(a_{ij}'(t_0)\bigr) \in M_{m \times n}(\nC) .
\]
:::

The prime here always means the derivative in \( t \); no dual map (@def-dual-map) appears anywhere in this section, so the notation cannot collide. By @cor-entrywise-convergence-is-the-convergence the definition can be restated without coordinates: \( \A \) is differentiable at \( t_0 \) with derivative \( \B \) exactly when
\[
\norm{\frac{\A(t) - \A(t_0)}{t - t_0} - \B} \longrightarrow 0
\qquad (t \to t_0),
\]
in any norm at all. Both readings are used below, the entrywise one to import calculus and the norm one to take limits.

::: {.remark}
**The calculus this section quotes.** Let \( f, g \colon I \to \nC \) be differentiable at \( t_0 \).

::: {.enumerate options="label=(D\arabic*)"}
1. *(Linearity and the product rule.)* \( f + g \) and \( fg \) are differentiable at \( t_0 \), with \( (f+g)' = f' + g' \) and \( (fg)' = f'g + fg' \); a constant function has derivative \( 0 \).
2. *(Differentiable implies continuous.)* \( f \) is continuous at \( t_0 \).
:::

Neither is proved here. (D1) is Chapter 10 §09's fact (A3), read for complex-valued functions of a real variable; (D2) is one more standard fact of the same kind, quoted here for the first time in this book. Both are of a piece with Chapter 14 §06's Taylor assumption: standard one-variable calculus, quoted so that the theorems below have hypotheses to stand on. Everything that follows them is linear algebra.
:::

::: {#lem-matrix-product-rule}
[Product Rule for Matrices]

Let \( \A \colon I \to M_{m \times n}(\nC) \) and \( \B \colon I \to M_{n \times p}(\nC) \) be differentiable at \( t_0 \). Then so is \( t \mapsto \A(t)\B(t) \), with
\[
(\A\B)'(t_0) = \A'(t_0)\B(t_0) + \A(t_0)\B'(t_0) .
\]
:::

::: {.proof}
Fix a position \( (i, k) \). The entry function is \( t \mapsto \sum_{j=1}^{n}a_{ij}(t)b_{jk}(t) \), a finite sum of products of functions differentiable at \( t_0 \). By (D1) it is differentiable at \( t_0 \) with derivative
\[
\sum_{j=1}^{n}\bigl(a_{ij}'(t_0)b_{jk}(t_0) + a_{ij}(t_0)b_{jk}'(t_0)\bigr),
\]
which is the \( (i,k) \)-entry of \( \A'(t_0)\B(t_0) + \A(t_0)\B'(t_0) \). Since this holds at every position, @def-matrix-valued-derivative gives the claim. Note that the order of the factors is preserved throughout: matrices do not commute, and the product rule must not be written \( 2\A\A' \) even for \( \B = \A \). This proves the lemma.
:::

## The derivative of the inverse

Nothing so far says that \( t \mapsto \A(t)^{-1} \) is even defined near \( t_0 \), let alone differentiable. Both come from §05.

::: {#thm-derivative-of-inverse}
[Derivative of the Inverse]

Let \( \A \colon I \to M_n(\nC) \) be differentiable at \( t_0 \in I \), with \( \A(t_0) \) invertible. Then \( \A(t) \) is invertible for all \( t \) in some open interval around \( t_0 \), the function \( t \mapsto \A(t)^{-1} \) is differentiable at \( t_0 \), and
\[
\bigl(\A^{-1}\bigr)'(t_0) = -\,\A(t_0)^{-1}\,\A'(t_0)\,\A(t_0)^{-1} .
\]
:::

::: {.idea}
The formula is what one gets by differentiating \( \A\A^{-1} = \I \) with @lem-matrix-product-rule and solving — but that argument presupposes what has to be proved, namely that \( \A^{-1} \) is differentiable. So run it in the honest order. The difference of two inverses factors as \( \X^{-1} - \Y^{-1} = \X^{-1}(\Y - \X)\Y^{-1} \); divide by \( t - t_0 \) and the middle factor becomes a difference quotient, which converges by hypothesis, while the outer factor converges because inversion is continuous (@cor-invertible-matrices-open). The limit of the product is the product of the limits, and that is the formula.
:::

::: {.proof}
Write \( \A_0 = \A(t_0) \). By (D2) every entry of \( \A \) is continuous at \( t_0 \), so \( \A(t) \to \A_0 \) entrywise as \( t \to t_0 \), hence \( \norm{\A(t) - \A_0} \to 0 \) by @cor-entrywise-convergence-is-the-convergence. By @cor-invertible-matrices-open there is therefore an open interval \( J \ni t_0 \) on which \( \norm{\A(t) - \A_0} < 1/\norm{\A_0^{-1}} \), so that \( \A(t) \) is invertible for \( t \in J \), and on which \( \norm{\A(t)^{-1} - \A_0^{-1}} \to 0 \) as \( t \to t_0 \).

Let \( t \in J \) with \( t \ne t_0 \). Multiplying \( \A_0 - \A(t) \) on the left by \( \A(t)^{-1} \) and on the right by \( \A_0^{-1} \),
\[
\A(t)^{-1} - \A_0^{-1} = -\,\A(t)^{-1}\bigl(\A(t) - \A_0\bigr)\A_0^{-1} .
\]
Divide by \( t - t_0 \):
\[
\frac{\A(t)^{-1} - \A_0^{-1}}{t - t_0}
= -\,\A(t)^{-1}\,\frac{\A(t) - \A_0}{t - t_0}\,\A_0^{-1} .
\]
As \( t \to t_0 \) the middle factor tends to \( \A'(t_0) \), by @def-matrix-valued-derivative. The left factor tends to \( \A_0^{-1} \), by the first paragraph. Products of convergent matrix families converge to the product of the limits: if \( \norm{\X(t) - \X} \to 0 \) and \( \norm{\Y(t) - \Y} \to 0 \) then
\[
\norm{\X(t)\Y(t) - \X\Y}
\le \norm{\X(t) - \X}\norm{\Y(t)} + \norm{\X}\norm{\Y(t) - \Y} ,
\]
and \( \norm{\Y(t)} \) is bounded near \( t_0 \) because \( \norm{\Y(t)} \le \norm{\Y} + \norm{\Y(t) - \Y} \). Applying this twice, the right-hand side converges to \( -\A_0^{-1}\A'(t_0)\A_0^{-1} \). Hence the difference quotient on the left converges, which by @def-matrix-valued-derivative is exactly the differentiability of \( t \mapsto \A(t)^{-1} \) at \( t_0 \), with the stated derivative. This proves the theorem.
:::

::: {.warning}
**The two copies of \( \A^{-1} \) sit on either side and cannot be combined.** The scalar formula \( (1/a)' = -a'/a^{2} \) tempts one to write \( -\A^{-2}\A' \), and that is wrong unless \( \A'(t_0) \) commutes with \( \A(t_0) \). For \( \A(t) = \begin{psmallmatrix} 1 & t \\ 0 & 2\end{psmallmatrix} \) at \( t = 0 \): we have \( \A(0)^{-1} = \diag(1, \tfrac12) \) and \( \A'(0) = \begin{psmallmatrix} 0&1\\0&0\end{psmallmatrix} \), so the correct answer is \( -\diag(1,\tfrac12)\begin{psmallmatrix} 0&1\\0&0\end{psmallmatrix}\diag(1,\tfrac12) = \begin{psmallmatrix} 0 & -1/2 \\ 0 & 0\end{psmallmatrix} \), whereas \( -\A(0)^{-2}\A'(0) = -\begin{psmallmatrix} 1&0\\0&1/4\end{psmallmatrix}\begin{psmallmatrix} 0&1\\0&0\end{psmallmatrix} = \begin{psmallmatrix} 0 & -1 \\ 0 & 0\end{psmallmatrix} \).
:::

## Jacobi's formula

The determinant is a polynomial in the entries, so differentiating it needs no analysis beyond (D1); the work is in recognizing the answer.

::: {#thm-derivative-of-det}
[Jacobi's Formula]

Let \( \A \colon I \to M_n(\nC) \) be differentiable at \( t_0 \in I \). Then \( t \mapsto \det\A(t) \) is differentiable at \( t_0 \), with
\[
\frac{d}{dt}\Big|_{t_0}\det\A(t) = \tr\bigl(\adj\A(t_0)\,\A'(t_0)\bigr) .
\]
If moreover \( \A(t_0) \) is invertible, this equals \( \det\A(t_0)\,\tr\bigl(\A(t_0)^{-1}\A'(t_0)\bigr) \).
:::

::: {.idea}
Use the Leibniz formula, which writes \( \det \) as a sum of \( n! \) products of \( n \) entries, one from each column. The product rule differentiates each such product into \( n \) terms, the \( j \)-th of which has column \( j \) differentiated and the rest untouched. Collecting by \( j \) gives \( n \) determinants, the \( j \)-th being \( \A \) with its \( j \)-th column replaced by \( \a_j' \). Expanding that determinant along column \( j \) (@thm-laplace-expansion) produces \( \sum_i a_{ij}'C_{ij} \), and summing over \( j \) gives a double sum which is precisely a trace against the adjugate.
:::

::: {.proof}
For \( n = 1 \) the statement reads \( \frac{d}{dt}\big|_{t_0}a_{11}(t) = a_{11}'(t_0) \), since \( \adj\A = (1) \) by @def-adjugate, so assume \( n \ge 2 \); that is what lets us speak of cofactors. Write \( \A(t) = (a_{ij}(t)) \) with columns \( \a_1(t), \dots, \a_n(t) \), and write \( C_{ij} \) for the cofactors of \( \A(t_0) \) (@def-minor-cofactor). By @thm-leibniz-formula-alternating,
\[
\det\A(t) = \sum_{\sigma \in S_n}\sgn(\sigma)\,a_{\sigma(1)1}(t)\cdots a_{\sigma(n)n}(t) ,
\]
a finite sum of products of \( n \) functions each differentiable at \( t_0 \). By (D1), applied \( n - 1 \) times to each product and then to the sum, \( \det\A \) is differentiable at \( t_0 \) with
\[
\frac{d}{dt}\Big|_{t_0}\det\A
= \sum_{j=1}^{n}\ \sum_{\sigma \in S_n}\sgn(\sigma)\,a_{\sigma(j)j}'(t_0)\prod_{l \ne j}a_{\sigma(l)l}(t_0) ,
\]
where the outer sum collects, for each \( j \), the terms in which the \( j \)-th factor was the one differentiated. By @thm-leibniz-formula-alternating read backwards, the inner sum is the determinant of the matrix \( \A_j \) obtained from \( \A(t_0) \) by replacing its \( j \)-th column with \( \a_j'(t_0) \). Expanding \( \det\A_j \) along that column with @thm-laplace-expansion (a), and using that the cofactors of column \( j \) do not involve column \( j \) and are therefore the cofactors \( C_{ij} \) of \( \A(t_0) \) itself,
\[
\det \A_j = \sum_{i=1}^{n}a_{ij}'(t_0)\,C_{ij} .
\]
Summing over \( j \),
\[
\frac{d}{dt}\Big|_{t_0}\det\A = \sum_{j=1}^{n}\sum_{i=1}^{n}C_{ij}\,a_{ij}'(t_0) .
\]
It remains to recognize the right-hand side. By @def-adjugate, \( (\adj\A(t_0))_{ji} = C_{ij} \), so
\[
\tr\bigl(\adj\A(t_0)\,\A'(t_0)\bigr)
= \sum_{j=1}^{n}\sum_{i=1}^{n}(\adj\A(t_0))_{ji}\,a_{ij}'(t_0) ,
\]
which is the same double sum. For the last claim, if \( \A(t_0) \) is invertible then \( \adj\A(t_0) = \det\A(t_0)\,\A(t_0)^{-1} \) by @thm-adjugate-identity, and the trace is linear (@thm-trace-properties), so the scalar \( \det\A(t_0) \) comes out in front. This proves the theorem.
:::

::: {#cor-derivative-of-det-at-identity}
[The Determinant's Derivative at the Identity Is the Trace]

For every \( \B \in M_n(\nC) \),
\[
\frac{d}{dt}\Big|_{t=0}\det(\I + t\B) = \tr\B .
\]
:::

::: {.proof}
Apply @thm-derivative-of-det to \( \A(t) = \I + t\B \), which is differentiable with \( \A'(t) = \B \) and \( \A(0) = \I \). Since \( \I \) is invertible with \( \I^{-1} = \I \) and \( \det\I = 1 \), the second form of the formula gives \( \tr(\I\B) = \tr\B \).
:::

So the determinant, which is a product of \( n \) numbers, has the trace, a sum of \( n \) numbers, as its linearization at \( \I \). That is the honest source of the identity \( \det e^{\A} = e^{\tr\A} \) of @thm-exponential-properties (e), and @exr-matrix-exponential-and-calculus-c1 reproves that identity along these lines.

::: {#exm-jacobi-and-inverse-worked}
[Both derivatives on one family]

Let \( \A(t) = \begin{pmatrix} 1 + t & t^{2} \\ t & 1 \end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \frac{d}{dt}\det\A(t) \) directly and by @thm-derivative-of-det.
2. Compute \( (\A^{-1})'(0) \) by @thm-derivative-of-inverse, and check it against a direct expansion.
:::
:::

::: {.solution}
(a) *Directly.* \( \det\A(t) = (1+t)\cdot 1 - t^{2}\cdot t = 1 + t - t^{3} \), so the derivative is \( 1 - 3t^{2} \).

*By the formula.* \( \adj\A(t) = \begin{psmallmatrix} 1 & -t^{2} \\ -t & 1+t \end{psmallmatrix} \) (@def-adjugate) and \( \A'(t) = \begin{psmallmatrix} 1 & 2t \\ 1 & 0\end{psmallmatrix} \), so
\[
\adj\A(t)\,\A'(t) = \begin{pmatrix} 1 - t^{2} & 2t \\ 1 & -2t^{2} \end{pmatrix},
\]
whose trace is \( 1 - t^{2} - 2t^{2} = 1 - 3t^{2} \). The two agree.

(b) \( \A(0) = \I \) and \( \A'(0) = \begin{psmallmatrix} 1 & 0 \\ 1 & 0\end{psmallmatrix} \), so @thm-derivative-of-inverse gives
\[
(\A^{-1})'(0) = -\I\begin{pmatrix} 1 & 0 \\ 1 & 0\end{pmatrix}\I
= \begin{pmatrix} -1 & 0 \\ -1 & 0\end{pmatrix} .
\]

*Check.* \( \A(t)^{-1} = \dfrac{1}{1 + t - t^{3}}\begin{psmallmatrix} 1 & -t^{2} \\ -t & 1+t\end{psmallmatrix} \). Near \( t = 0 \) the scalar factor is \( 1 - t + (\text{terms in } t^{2}) \), so
\[
\A(t)^{-1} = \begin{pmatrix} 1 - t & 0 \\ -t & 1 \end{pmatrix} + (\text{terms in } t^{2}),
\]
whose derivative at \( 0 \) is \( \begin{psmallmatrix} -1 & 0 \\ -1 & 0\end{psmallmatrix} \), as predicted. The formula did the work that the quotient rule would otherwise have had to do four times.
:::

::: {.check}
@thm-derivative-of-det holds with no invertibility hypothesis, yet the second form of the formula has one. Where exactly is invertibility used, and what does the formula say at a \( t_0 \) where \( \det\A(t_0) = 0 \)?
:::

::: {.solution}
Only in the last line, where \( \adj\A(t_0) \) is rewritten as \( \det\A(t_0)\A(t_0)^{-1} \). The adjugate itself is defined for every square matrix (@def-adjugate), so the first form survives. At a \( t_0 \) with \( \det\A(t_0) = 0 \) it still gives a number: for \( \A(t) = \diag(t, t) \) at \( t_0 = 0 \) we get \( \adj\A(0) = 0 \), so the derivative of \( \det\A(t) = t^{2} \) is \( 0 \) there, which is correct. The second form would read "\( 0 \) times something undefined".
:::

## Exercises

### A. Check your understanding

:::: {#exr-matrix-exponential-and-calculus-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the three bounds of @thm-exponential-norm-bound, and say which property of the norm each one needs.
2. Determine whether the following statement is correct, and justify your answer: if \( \norm{\A}_2 \) is large then \( \norm{e^{\A}}_2 \) is large.
3. State @thm-exponential-decay, and say what the constant \( C \) is paying for.
4. State Jacobi's formula (@thm-derivative-of-det), and name the fact from calculus its proof quotes.
5. Write down the derivative of \( t \mapsto \A(t)^{-1} \) and explain in one sentence why it is not \( -\A^{-2}\A' \).
:::
::::

::: {.solution}
(a) \( \norm{e^{\A}} \le e^{\norm{\A}} \), \( \norm{e^{\A} - \I} \le e^{\norm{\A}} - 1 \), and \( \norm{e^{\A} - \I - \A} \le e^{\norm{\A}} - 1 - \norm{\A} \le \norm{\A}^{2}e^{\norm{\A}}/2 \). All three need subadditivity (to bound a sum term by term) and submultiplicativity (to get \( \norm{\A^{m}} \le \norm{\A}^{m} \)); the first also needs \( \norm{\I} = 1 \), which is what makes the \( m = 0 \) term equal \( 1 \).

(b) Incorrect. For \( \A = t\begin{psmallmatrix} 0 & 1 \\ -1 & 0\end{psmallmatrix} \) we have \( \norm{\A}_2 = t \), arbitrarily large, while \( e^{\A} \) is a rotation matrix and \( \norm{e^{\A}}_2 = 1 \) (@exm-exponential-bound-sharp-and-not).

(c) If \( \mu \) is the largest real part of an eigenvalue of \( \A \) and \( \nu > \mu \), there is \( C \ge 1 \) with \( \norm{e^{t\A}} \le Ce^{\nu t} \) for all \( t \ge 0 \). The constant pays for the transient: \( \norm{e^{t\A}} \) may first grow, as in @exm-decay-with-a-transient, and it also pays for the gap between \( \nu \) and \( \mu \).

(d) \( \frac{d}{dt}\det\A(t) = \tr(\adj\A(t)\,\A'(t)) \), for a matrix-valued \( \A \) differentiable at \( t \). The quoted fact is (D1): the linearity of differentiation and the product rule for complex-valued functions of a real variable.

(e) \( (\A^{-1})' = -\A^{-1}\A'\A^{-1} \). The two copies of \( \A^{-1} \) sit on opposite sides of \( \A' \), and matrices do not commute, so they may not be collected into \( \A^{-2} \) unless \( \A' \) commutes with \( \A \).
:::

### B. Practice

:::: {#exr-matrix-exponential-and-calculus-b1}
[B1: Bound against truth]

For each matrix, compute \( \norm{e^{\A}}_{\infty} \) exactly and compare with \( e^{\norm{\A}_{\infty}} \).

::: {.enumerate options="label=(\alph*)"}
1. \( \A = \begin{pmatrix} 0 & 3 \\ 0 & 0 \end{pmatrix} \).
2. \( \A = \diag(1, -4) \).
:::
::::

::: {.solution}
(a) \( \A^{2} = 0 \), so the series stops: \( e^{\A} = \I + \A = \begin{psmallmatrix} 1 & 3 \\ 0 & 1\end{psmallmatrix} \), with \( \norm{e^{\A}}_{\infty} = 4 \). Also \( \norm{\A}_{\infty} = 3 \), so the bound is \( e^{3} \approx 20.09 \). Correct, and loose by a factor of about \( 5 \).

(b) \( e^{\A} = \diag(e, e^{-4}) \), so \( \norm{e^{\A}}_{\infty} = e \approx 2.718 \). Here \( \norm{\A}_{\infty} = 4 \) and the bound is \( e^{4} \approx 54.6 \). The bound is governed by the entry of largest modulus, \( -4 \), while the exponential is governed by the largest **real part**, \( 1 \). This is the discrepancy @thm-exponential-decay exists to remove.
:::

:::: {#exr-matrix-exponential-and-calculus-b2}
[B2: A rate for a stable matrix]

Let \( \A = \begin{pmatrix} -2 & 4 \\ 0 & -2 \end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \mu \) and \( e^{t\A} \), and give \( \norm{e^{t\A}}_{\infty} \) for \( t \ge 0 \).
2. Find the largest value of \( \norm{e^{t\A}}_{\infty} \) on \( t \ge 0 \).
3. Find the smallest \( C \) that works in @thm-exponential-decay for \( \nu = -1 \).
:::
::::

::: {.solution}
(a) \( \A \) is upper triangular with diagonal \( -2, -2 \), so \( \spec(\A) = \{-2\} \) (@thm-diagonal-of-triangular-form (b)) and \( \mu = -2 \). Writing \( \A = -2\I + 4\N \) with \( \N = \begin{psmallmatrix} 0&1\\0&0\end{psmallmatrix} \), the summands commute and \( \N^2 = 0 \), so by @cor-exponential-of-jordan-block
\[
e^{t\A} = e^{-2t}\begin{pmatrix} 1 & 4t \\ 0 & 1 \end{pmatrix},
\qquad \norm{e^{t\A}}_{\infty} = e^{-2t}(1 + 4t) .
\]

(b) The derivative of \( e^{-2t}(1+4t) \) is \( e^{-2t}(4 - 2 - 8t) = e^{-2t}(2 - 8t) \), which is positive for \( t < \tfrac14 \) and negative after, so by fact (A6) the maximum is at \( t = \tfrac14 \). The value there is \( 2e^{-1/2} \approx 1.213 \).

(c) We need the smallest \( C \) with \( e^{-2t}(1+4t) \le Ce^{-t} \), that is, \( C = \max_{t \ge 0}(1+4t)e^{-t} \). Its derivative is \( e^{-t}(4 - 1 - 4t) = e^{-t}(3 - 4t) \), positive for \( t < \tfrac34 \) and negative after, so by fact (A6) the maximum is at \( t = \tfrac34 \) and \( C = 4e^{-3/4} \approx 1.890 \).
:::

:::: {#exr-matrix-exponential-and-calculus-b3}
[B3: Two derivatives]

Let \( \A(t) = \begin{pmatrix} \cos t & -\sin t \\ \sin t & \cos t \end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \frac{d}{dt}\det\A(t) \) by @thm-derivative-of-det and check it against the exact value of \( \det\A(t) \).
2. Compute \( (\A^{-1})'(t) \) by @thm-derivative-of-inverse and check it by differentiating \( \A(t)^{-1} \) directly.
:::
::::

::: {.solution}
(a) \( \det\A(t) = \cos^{2}t + \sin^{2}t = 1 \), so the derivative is \( 0 \). By the formula: \( \adj\A(t) = \begin{psmallmatrix} \cos t & \sin t \\ -\sin t & \cos t \end{psmallmatrix} \) and \( \A'(t) = \begin{psmallmatrix} -\sin t & -\cos t \\ \cos t & -\sin t\end{psmallmatrix} \), so
\[
\adj\A(t)\A'(t) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix},
\]
whose trace is \( 0 \). The two agree. (The diagonal entries are \( -\cos t\sin t + \sin t\cos t \) and \( \sin t\cos t - \cos t\sin t \), both zero.)

(b) Since \( \det\A(t) = 1 \), \( \A(t)^{-1} = \adj\A(t) = \begin{psmallmatrix} \cos t & \sin t \\ -\sin t & \cos t\end{psmallmatrix} \), whose entrywise derivative is \( \begin{psmallmatrix} -\sin t & \cos t \\ -\cos t & -\sin t\end{psmallmatrix} \). By the formula, using the product \( \adj\A(t)\A'(t) \) computed in (a),
\[
-\A^{-1}\A'\A^{-1}
= -\begin{pmatrix} 0 & -1 \\ 1 & 0\end{pmatrix}\begin{pmatrix} \cos t & \sin t \\ -\sin t & \cos t\end{pmatrix}
= \begin{pmatrix} -\sin t & \cos t \\ -\cos t & -\sin t \end{pmatrix} .
\]
The two agree.
:::

### C. Going deeper

:::: {#exr-matrix-exponential-and-calculus-c1}
[C1: The determinant of the exponential, again]

Let \( \A \in M_n(\nC) \) and put \( \varphi(t) = \det e^{t\A} \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \varphi \) is differentiable with \( \varphi'(t) = (\tr\A)\varphi(t) \).
2. Hence deduce \( \det e^{\A} = e^{\tr\A} \), recovering @thm-exponential-properties (e).
:::

*Hint for (b): consider \( \psi(t) = e^{-t\tr\A}\varphi(t) \).*
::::

::: {.solution}
(a) The function \( t \mapsto e^{t\A} \) is differentiable with derivative \( \A e^{t\A} \) (@thm-exponential-properties (b)), and \( e^{t\A} \) is invertible with inverse \( e^{-t\A} \) (@thm-exponential-properties (c)). So @thm-derivative-of-det applies in its second form:
\[
\varphi'(t) = \det(e^{t\A})\,\tr\bigl(e^{-t\A}\A e^{t\A}\bigr) .
\]
By @thm-trace-properties (3) with the two factors \( e^{-t\A} \) and \( \A e^{t\A} \), we get \( \tr(e^{-t\A}\A e^{t\A}) = \tr(\A e^{t\A}e^{-t\A}) = \tr\A \), giving \( \varphi'(t) = (\tr\A)\varphi(t) \).

(b) Put \( c = \tr\A \) and \( \psi(t) = e^{-ct}\varphi(t) \). By the product rule (D1) and (a),
\[
\psi'(t) = -c\,e^{-ct}\varphi(t) + e^{-ct}c\,\varphi(t) = 0
\]
for every \( t \), where \( \frac{d}{dt}e^{-ct} = -ce^{-ct} \) is @thm-exponential-properties (b) in the case \( n = 1 \). A differentiable function with vanishing derivative is constant — fact (A4) of Chapter 10 §09 — so \( \psi(t) = \psi(0) = \det(e^{0}) = \det\I = 1 \). Hence \( \varphi(t) = e^{ct} \), and \( t = 1 \) gives \( \det e^{\A} = e^{\tr\A} \).
:::

:::: {#exr-matrix-exponential-and-calculus-c2}
[C2: Comparing two exponentials]

Let \( \A, \B \in M_n(\nC) \) with \( \A\B = \B\A \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \norm{e^{\A} - e^{\B}} \le e^{\norm{\B}}\bigl(e^{\norm{\A - \B}} - 1\bigr) \).
2. Deduce that \( \M \mapsto e^{\M} \) is continuous at every \( \M \) that commutes with a neighborhood of itself, and identify those \( \M \): they are exactly the scalar matrices \( c\I \).
3. Say exactly where the commuting hypothesis is used, and why the argument cannot simply be dropped.
:::
::::

::: {.solution}
(a) Since \( \A \) and \( \B \) commute, so do \( \B \) and \( \A - \B \). By @thm-exponential-properties (d), \( e^{\A} = e^{\B + (\A - \B)} = e^{\B}e^{\A - \B} \). Hence
\[
e^{\A} - e^{\B} = e^{\B}\bigl(e^{\A-\B} - \I\bigr) ,
\]
and submultiplicativity with @thm-exponential-norm-bound (a) and (b) gives
\[
\norm{e^{\A} - e^{\B}} \le \norm{e^{\B}}\,\norm{e^{\A-\B} - \I}
\le e^{\norm{\B}}\bigl(e^{\norm{\A-\B}} - 1\bigr) .
\]

(b) Take \( \B = c\I \), which commutes with every matrix. For \( \A \) with \( \norm{\A - c\I} = \delta \), part (a) gives \( \norm{e^{\A} - e^{c}\I} \le e^{\lvert c\rvert}(e^{\delta} - 1) \), and \( e^{\delta} - 1 \to 0 \) as \( \delta \to 0 \), because \( t \mapsto e^{t} \) is differentiable by fact (A2) of Chapter 10 §09 and so continuous at \( 0 \). So \( e^{\A} \to e^{c\I} \) as \( \A \to c\I \).

(c) Only in the first line, where \( e^{\B + (\A-\B)} \) is split as \( e^{\B}e^{\A-\B} \); @thm-exponential-properties (d) has commutation as a hypothesis, and Chapter 10 §09 exhibits matrices with \( e^{\A+\B} \ne e^{\A}e^{\B} \). Without it there is no factorization to take norms of, and a different argument is needed. (The inequality itself is in fact true in general, but proving it needs an integral representation of \( e^{\A} - e^{\B} \), which this book does not have.)
:::

:::: {#exr-matrix-exponential-and-calculus-c3}
[C3: A quantity that measures the decay]

Let \( \A, \X, \Q \in M_n(\nC) \) with \( \X \) and \( \Q \) positive definite (@def-positive-semidefinite) and
\[
\A^{*}\X + \X\A = -\Q .
\]
Let \( \x \colon \nR \to \nC^{n} \) be differentiable with \( \x' = \A\x \), and put \( V(t) = \x(t)^{*}\X\x(t) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( V \) is real-valued and differentiable, with \( V'(t) = \x(t)^{*}(\A^{*}\X + \X\A)\x(t) \).
2. Deduce that if \( \x(0) \ne \0 \), then \( V \) is strictly decreasing.
3. Explain how this relates to the Lyapunov equation of @def-lyapunov-equation, whose unknown sits between \( \A \) and \( \A^{*} \) the other way round.
:::

*Hint for (a): \( \x^{*} \) is a \( 1 \times n \) matrix-valued function, and \( \conj{f}' = \conj{f'} \) for a differentiable \( f \colon \nR \to \nC \).*
::::

::: {.solution}
(a) \( V(t) \) is a \( 1 \times 1 \) matrix, and \( V(t)^{*} = \x^{*}\X^{*}\x = \x^{*}\X\x = V(t) \) since \( \X \) is Hermitian, so \( V(t) \) is real. Each entry of \( t \mapsto \x(t)^{*} \) is the conjugate of an entry of \( \x \), hence differentiable with \( (\x^{*})' = (\x')^{*} = (\A\x)^{*} = \x^{*}\A^{*} \). By @lem-matrix-product-rule, applied twice to the product \( \x^{*}\cdot\X\cdot\x \) and using \( \X' = 0 \),
\[
V'(t) = \x^{*}\A^{*}\X\x + \x^{*}\X\A\x = \x^{*}(\A^{*}\X + \X\A)\x .
\]

(b) By hypothesis \( V'(t) = -\x(t)^{*}\Q\x(t) \). If \( \x(t_1) = \0 \) for some \( t_1 \), then by @thm-linear-ode-solution \( \x(t) = e^{t\A}\x(0) \) for every \( t \), and \( e^{t_1\A} \) is invertible by @thm-exponential-properties (c), so \( \x(0) = \0 \), contradicting the hypothesis. So \( \x(t) \ne \0 \) for every \( t \), and \( \Q \succ 0 \) gives \( \x(t)^{*}\Q\x(t) > 0 \), hence \( V'(t) < 0 \) for every \( t \). A differentiable real function with everywhere negative derivative is strictly decreasing; that last step is the mean value theorem, one more fact of one-variable calculus quoted here and not proved.

(c) @def-lyapunov-equation writes the equation as \( \A\X + \X\A^{*} = -\Q \); the equation used here is that one for the pair \( (\A^{*}, \Q) \). The two are interchanged by replacing \( \A \) with \( \A^{*} \), which changes nothing about stability, since the eigenvalues of \( \A^{*} \) are the complex conjugates of those of \( \A \) and conjugation preserves real parts. So the decay of \( V \) is exactly the statement Chapter 12 §10 pointed forward to, for whichever of the two conventions one adopts — granted a positive definite solution \( \X \), whose existence is not proved in this book.
:::
