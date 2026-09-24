# Golden–Thompson

For numbers, \( e^{a+b} = e^{a}e^{b} \). For matrices this fails the moment \( \A \) and \( \B \) stop commuting, and Chapter 10 §09 was careful to say so: @thm-exponential-properties (d) buys the identity only at the price of \( \A\B = \B\A \). The question this section answers is what survives without that price. The answer is that the **trace** still knows the right inequality, in one direction, and that the direction is the useful one.

The section also closes the chapter, and Part V with it. After Golden–Thompson come two of its relatives — Klein's inequality and the non-negativity of the relative entropy — a counterexample showing that three matrices are one too many, and one theorem that is quoted rather than proved.

## Sums in the exponent, products in the answer

A product \( e^{\A}e^{\B} \) is not \( e^{\A+\B} \), but it is not far off either: to first order in \( \A \) and \( \B \) the two agree, since both are \( \I + \A + \B + \dots \), and the discrepancy is quadratic. So if the exponents are made small by a factor \( 1/k \) and the resulting error is repaired \( k \) times over, the discrepancy should vanish. It does, and this is the one tool that turns a sum in the exponent into a product.

::: {#lem-lie-product}
[Lie's Product Formula]

Let \( \A, \B \in M_n(\nC) \). Then
\[
e^{\A+\B} = \lim_{k \to \infty}\bigl(e^{\A/k}e^{\B/k}\bigr)^{k} ,
\]
the limit taken entrywise, and also in any norm on \( M_n(\nC) \).
:::

::: {.idea}
Write \( \S_k = e^{(\A+\B)/k} \) and \( \T_k = e^{\A/k}e^{\B/k} \). Then \( \S_k^{k} \) is exactly \( e^{\A+\B} \), so the whole task is to compare \( \S_k^{k} \) with \( \T_k^{k} \). Two estimates do it. Both \( \S_k \) and \( \T_k \) have norm at most \( e^{(\norm{\A}+\norm{\B})/k} \), so no power of either can be large; and \( \S_k - \T_k \) is of size \( 1/k^{2} \), because the two agree through the linear term. A telescoping identity turns a difference of \( k \)-th powers into \( k \) copies of \( \S_k - \T_k \), and \( k \cdot 1/k^2 \) tends to \( 0 \).
:::

::: {.proof}
Fix the spectral norm \( \norm{\cdot}_2 \), which is submultiplicative by @thm-operator-norm-properties (d). Put \( a = \norm{\A}_2 \), \( b = \norm{\B}_2 \) and \( c = a + b \), and let \( k \) be an integer with \( k \ge \max(1, c) \). Write
\[
\S_k = e^{(\A+\B)/k}, \qquad \T_k = e^{\A/k}e^{\B/k} .
\]

**Step 1. \( \S_k^{k} = e^{\A+\B} \).** The matrix \( (\A+\B)/k \) commutes with itself, so @thm-exponential-properties (d) gives \( e^{j(\A+\B)/k}e^{(\A+\B)/k} = e^{(j+1)(\A+\B)/k} \) for every \( j \ge 0 \). Induction on \( j \) yields \( \S_k^{j} = e^{j(\A+\B)/k} \), and \( j = k \) is the claim.

**Step 2. Norm bounds.** By @thm-exponential-norm-bound (a), \( \norm{\S_k}_2 \le e^{\norm{\A+\B}_2/k} \le e^{c/k} \), using \( \norm{\A+\B}_2 \le c \); and \( \norm{\T_k}_2 \le e^{a/k}e^{b/k} = e^{c/k} \) by submultiplicativity. Since \( k \ge c \), both are at most \( e \).

**Step 3. \( \S_k - \T_k \) is of size \( 1/k^{2} \).** For any \( \X \in M_n(\nC) \) put \( \R(\X) = e^{\X} - \I - \X \), so that @thm-exponential-norm-bound (c) gives
\[
\norm{\R(\X)}_2 \le \tfrac12\norm{\X}_2^{2}\,e^{\norm{\X}_2} .
\]
Multiplying out \( \T_k = \bigl(\I + \tfrac{\A}{k} + \R(\tfrac{\A}{k})\bigr)\bigl(\I + \tfrac{\B}{k} + \R(\tfrac{\B}{k})\bigr) \), and using \( e^{\B/k} = \I + \tfrac{\B}{k} + \R(\tfrac{\B}{k}) \) to collect the three terms that begin with \( \R(\tfrac{\A}{k}) \),
\[
\T_k = \I + \frac{\A+\B}{k} + \R\Bigl(\frac{\B}{k}\Bigr) + \frac{\A\B}{k^{2}} + \frac{\A}{k}\R\Bigl(\frac{\B}{k}\Bigr) + \R\Bigl(\frac{\A}{k}\Bigr)e^{\B/k} .
\]
Subtracting this from \( \S_k = \I + \tfrac{\A+\B}{k} + \R\bigl(\tfrac{\A+\B}{k}\bigr) \), the constant and linear terms cancel, and the triangle inequality with \( a/k, b/k, c/k \le 1 \) gives
\[
\begin{aligned}
\norm{\S_k - \T_k}_2
&\le \frac{c^{2}e}{2k^{2}} + \frac{b^{2}e}{2k^{2}} + \frac{ab}{k^{2}} +
     \frac{ab^{2}e}{2k^{3}} + \frac{a^{2}e^{2}}{2k^{2}} \\
&\le \frac{M}{k^{2}}, \qquad
M = \frac{(c^{2}+b^{2})e}{2} + ab + \frac{ab^{2}e}{2} + \frac{a^{2}e^{2}}{2} ,
\end{aligned}
\]
where the fourth term used \( 1/k^{3} \le 1/k^{2} \). The constant \( M \) depends only on \( \A \) and \( \B \).

**Step 4. Telescoping.** For any \( \M, \N \in M_n(\nC) \) and any \( k \ge 1 \),
\[
\M^{k} - \N^{k} = \sum_{j=0}^{k-1}\M^{j}(\M - \N)\N^{k-1-j} ,
\]
since the \( j \)-th summand is \( \M^{j+1}\N^{k-1-j} - \M^{j}\N^{k-j} \) and the sum telescopes. Applying this to \( \M = \S_k \), \( \N = \T_k \) and using Steps 1 and 2,
\[
\norm{e^{\A+\B} - \T_k^{k}}_2 \le \sum_{j=0}^{k-1}e^{jc/k}\,\norm{\S_k - \T_k}_2\,e^{(k-1-j)c/k} \le k\,e^{c}\,\frac{M}{k^{2}} = \frac{e^{c}M}{k} .
\]
The right side tends to \( 0 \), so \( \T_k^{k} \to e^{\A+\B} \) in the spectral norm, hence entrywise and in every norm by @cor-entrywise-convergence-is-the-convergence. This proves the formula.
:::

Nothing in the proof used that the matrices are Hermitian: the formula holds for all complex matrices. What it costs is a limit, and every consequence below is obtained by pushing an inequality through that limit.

## The trace of a product of two positive matrices

Golden–Thompson compares \( \tr e^{\A+\B} \) with \( \tr(e^{\A}e^{\B}) \). Before comparing them we should know that the second number is real, which is not obvious: the product of two Hermitian matrices is almost never Hermitian. One identity settles this, and it will be used again.

::: {#lem-trace-of-positive-product}
[Powers of a Product of Two Positive Matrices]

Let \( \X, \Y \in M_n(\nC) \) be positive semidefinite and let \( k \ge 1 \). Then
\[
\tr\bigl((\X\Y)^{k}\bigr) = \tr\bigl((\X^{1/2}\Y\X^{1/2})^{k}\bigr) ,
\]
and this number is real and \( \ge 0 \).
:::

::: {.proof}
Let \( \X^{1/2} \) be the positive square root of @thm-psd-square-root, and put \( \S = \X^{1/2}\Y\X^{1/2} \). We claim
\[
(\X\Y)^{k} = \X^{1/2}\,\S^{\,k-1}\,\X^{1/2}\Y \qquad (k \ge 1) .
\]
For \( k = 1 \) the right side is \( \X^{1/2}\X^{1/2}\Y = \X\Y \). Assuming it for \( k \), and using \( \X^{1/2}\Y\X\Y = \S\,\X^{1/2}\Y \),
\[
(\X\Y)^{k+1} = \X^{1/2}\S^{\,k-1}\bigl(\X^{1/2}\Y\X\Y\bigr) = \X^{1/2}\S^{\,k}\X^{1/2}\Y ,
\]
which is the claim for \( k+1 \). Taking traces and moving the leading \( \X^{1/2} \) to the back, which @thm-trace-properties (3) permits,
\[
\tr\bigl((\X\Y)^{k}\bigr) = \tr\bigl(\S^{\,k-1}\X^{1/2}\Y\X^{1/2}\bigr) = \tr(\S^{\,k}) .
\]
Now \( \S = (\X^{1/2})^{*}\Y\X^{1/2} \succeq 0 \) by @prp-congruence-positivity (a), since \( \X^{1/2} \) is Hermitian. So \( \S^{k} \) is Hermitian with eigenvalues the \( k \)-th powers of those of \( \S \), all \( \ge 0 \) by @thm-psd-characterizations (b). Its trace is the sum of its eigenvalues (@thm-trace-det-eigenvalues), hence real and \( \ge 0 \).
:::

::: {.check}
Why is \( \tr(e^{\A}e^{\B}) \) a real number for Hermitian \( \A \) and \( \B \), even though \( e^{\A}e^{\B} \) is not Hermitian?
:::

::: {.solution}
For Hermitian \( \A \) with spectral resolution \( \A = \sum_i\lambda_i\P_i \), @thm-unitary-exponential (a) gives \( e^{\A} = \sum_ie^{\lambda_i}\P_i \), which is Hermitian with positive eigenvalues, hence positive definite by @thm-psd-characterizations (b). The same holds for \( e^{\B} \). So @lem-trace-of-positive-product with \( k = 1 \) applies: \( \tr(e^{\A}e^{\B}) \) is real and \( \ge 0 \). The product itself is not Hermitian unless \( \A \) and \( \B \) commute, but its trace does not notice.
:::

The engine of Golden–Thompson is the next inequality. It says that in a trace, the powers may be moved off the product and onto the two factors — provided the exponent is a power of two. That restriction is not an accident of the proof technique here; it is what makes a repeated Cauchy–Schwarz argument close.

:::: {#lem-trace-power-inequality}
[The Trace Power Inequality]

Let \( r \ge 0 \) and \( m = 2^{r} \).

::: {.enumerate options="label=(\alph*)"}
1. \( \tr\bigl((\A^{*})^{m}\A^{m}\bigr) \le \tr\bigl((\A\A^{*})^{m}\bigr) \) for every \( \A \in M_n(\nC) \).
2. \( \tr\bigl((\X\Y)^{m}\bigr) \le \tr\bigl(\X^{m}\Y^{m}\bigr) \) for all positive semidefinite \( \X, \Y \in M_n(\nC) \).
:::
::::

::: {.idea}
Both halves are proved together by induction on \( r \), because each step of one needs the other at the previous stage. The only inequality used is Cauchy–Schwarz for the Frobenius inner product, in the form \( \lvert\tr(\M^{2})\rvert \le \tr(\M^{*}\M) \): a trace of a square is bounded by a trace of a product of a matrix with its adjoint. Everything else is cyclic rearrangement of words in \( \X \) and \( \Y \), or in \( \A \) and \( \A^{*} \). The role of (a) is to absorb the mismatch that Cauchy–Schwarz creates: it turns \( (\A^{*})^{m}\A^{m} \) — the wrong grouping — into \( (\A\A^{*})^{m} \), which is a word one can feed back into (b).
:::

::: {.proof}
Throughout, \( \inner{\M}{\N} = \tr(\N^{*}\M) \) is the Frobenius inner product of Chapter 11 §01, with induced norm \( \norm{\M}_F \).

**Claim 1.** *\( \lvert\tr(\M^{2})\rvert \le \tr(\M^{*}\M) \) for every \( \M \in M_n(\nC) \).* Since \( (\M^{*})^{*} = \M \), we have \( \tr(\M^{2}) = \tr\bigl((\M^{*})^{*}\M\bigr) = \inner{\M}{\M^{*}} \). By @thm-cauchy-schwarz, \( \lvert\inner{\M}{\M^{*}}\rvert \le \norm{\M}_F\norm{\M^{*}}_F \). Finally \( \norm{\M^{*}}_F^{2} = \tr(\M\M^{*}) = \tr(\M^{*}\M) = \norm{\M}_F^{2} \) by @thm-trace-properties (3), so the bound is \( \norm{\M}_F^{2} = \tr(\M^{*}\M) \).

**Claim 2.** *For positive semidefinite \( \X, \Y \) and \( q \ge 1 \), \( \tr\bigl((\X\Y^{2}\X)^{q}\bigr) = \tr\bigl((\X^{2}\Y^{2})^{q}\bigr) \); and for any \( \A \) and \( q \ge 1 \), \( \tr\bigl((\A^{2}(\A^{*})^{2})^{q}\bigr) = \tr\bigl((\P\Q)^{q}\bigr) \), where \( \P = \A\A^{*} \) and \( \Q = \A^{*}\A \).* Both are cyclic rearrangements, justified by @thm-trace-properties (3). Induction on \( q \) gives \( (\X\Y^{2}\X)^{q} = \X(\Y^{2}\X^{2})^{q-1}\Y^{2}\X \); moving the leading \( \X \) to the back turns its trace into \( \tr\bigl((\Y^{2}\X^{2})^{q}\bigr) \), which is \( \tr\bigl((\X^{2}\Y^{2})^{q}\bigr) \) by one more cyclic shift. For the second identity, \( \A^{2}(\A^{*})^{2} = \A\P\A^{*} \), and induction on \( q \) gives \( (\A\P\A^{*})^{q} = \A\,\P(\Q\P)^{q-1}\,\A^{*} \); moving the leading \( \A \) to the back turns its trace into \( \tr\bigl(\P(\Q\P)^{q-1}\Q\bigr) = \tr\bigl((\P\Q)^{q}\bigr) \).

We now induct on \( r \), proving (a) and (b) simultaneously.

**Base \( r = 0 \).** Part (a) reads \( \tr(\A^{*}\A) \le \tr(\A\A^{*}) \), an equality by @thm-trace-properties (3). Part (b) reads \( \tr(\X\Y) \le \tr(\X\Y) \).

**Step.** Assume (a) and (b) for \( r \), and write \( q = 2^{r} \).

*Part (b) for \( 2q \).* Put \( \A = \X\Y \), so \( \A^{*} = \Y\X \) because \( \X \) and \( \Y \) are Hermitian, and put \( \M = \A^{q} = (\X\Y)^{q} \). Then \( \M^{2} = (\X\Y)^{2q} \) and \( \M^{*}\M = (\A^{*})^{q}\A^{q} \). The number \( \tr(\M^{2}) = \tr\bigl((\X\Y)^{2q}\bigr) \) is real and \( \ge 0 \) by @lem-trace-of-positive-product, so it equals its own absolute value, and Claim 1 gives
\[
\tr\bigl((\X\Y)^{2q}\bigr) \le \bigl\lvert\tr(\M^{2})\bigr\rvert \le \tr\bigl((\A^{*})^{q}\A^{q}\bigr) .
\]
By the inductive hypothesis (a),
\[
\tr\bigl((\A^{*})^{q}\A^{q}\bigr) \le \tr\bigl((\A\A^{*})^{q}\bigr) = \tr\bigl((\X\Y^{2}\X)^{q}\bigr) = \tr\bigl((\X^{2}\Y^{2})^{q}\bigr) ,
\]
the last step by Claim 2. Now \( \X^{2} = \X^{*}\X \succeq 0 \) and \( \Y^{2} \succeq 0 \) by @thm-psd-characterizations (c), so the inductive hypothesis (b) applies to the pair \( \X^{2}, \Y^{2} \) and gives
\[
\tr\bigl((\X^{2}\Y^{2})^{q}\bigr) \le \tr\bigl(\X^{2q}\Y^{2q}\bigr) .
\]
Chaining the three displays proves (b) for \( 2q \).

*Part (a) for \( 2q \).* Put \( \B = \A^{2} \), so \( \B^{*} = (\A^{*})^{2} \), \( \A^{2q} = \B^{q} \) and \( (\A^{*})^{2q} = (\B^{*})^{q} \). The inductive hypothesis (a), applied to \( \B \), and then Claim 2 give
\[
\tr\bigl((\A^{*})^{2q}\A^{2q}\bigr) = \tr\bigl((\B^{*})^{q}\B^{q}\bigr) \le \tr\bigl((\B\B^{*})^{q}\bigr) = \tr\bigl((\P\Q)^{q}\bigr) ,
\]
with \( \P = \A\A^{*} \) and \( \Q = \A^{*}\A \), both positive semidefinite by @thm-psd-characterizations (c). The inductive hypothesis (b) applied to \( \P, \Q \) gives \( \tr\bigl((\P\Q)^{q}\bigr) \le \tr(\P^{q}\Q^{q}) \). Since \( \P^{q} \) and \( \Q^{q} \) are Hermitian, \( \tr(\P^{q}\Q^{q}) = \inner{\P^{q}}{\Q^{q}} \), and this number is real and \( \ge 0 \) by @lem-trace-of-positive-product, both matrices being positive semidefinite. So @thm-cauchy-schwarz gives
\[
\tr(\P^{q}\Q^{q}) = \inner{\P^{q}}{\Q^{q}} \le \norm{\P^{q}}_F\norm{\Q^{q}}_F = \tr(\P^{2q})^{1/2}\tr(\Q^{2q})^{1/2} .
\]
Write \( \A = \U\vSigma\V^{*} \) for a singular value decomposition (@thm-svd), with \( \vSigma = \diag(\sigma_1, \dots, \sigma_n) \). Then \( \P = \U\vSigma^{2}\U^{*} \) and \( \Q = \V\vSigma^{2}\V^{*} \), so \( \P \) and \( \Q \) are both unitarily similar to \( \vSigma^{2} \) and therefore have the same eigenvalues with multiplicity. Hence \( \tr(\P^{2q}) = \tr(\Q^{2q}) \), the displayed bound is \( \tr(\P^{2q}) \), and
\[
\tr\bigl((\A^{*})^{2q}\A^{2q}\bigr) \le \tr(\P^{2q}) = \tr\bigl((\A\A^{*})^{2q}\bigr) .
\]
This is (a) for \( 2q \), and the induction is complete.
:::

The restriction to \( m = 2^{r} \) is a restriction of this proof, not of the truth: (b) holds for every integer \( m \ge 1 \). It even holds for every real \( m \ge 1 \), once \( (\X\Y)^{m} \) is read as \( (\X^{1/2}\Y\X^{1/2})^{m} \), which @lem-trace-of-positive-product says is the same thing for integer exponents and which is the only reading available for the others, since \( \X\Y \) is neither Hermitian nor positive semidefinite. The general case is a theorem of Lieb and Thirring and is not proved here; nothing below needs it, because a limit along the powers of two is all Lie's formula asks for.

## The inequality of Golden and Thompson

Now the two halves fit together. Lie's formula writes \( e^{\A+\B} \) as a limit of \( m \)-th powers of \( e^{\A/m}e^{\B/m} \), and the trace power inequality moves the exponent \( m \) off the product and onto the two factors, where it reassembles \( e^{\A} \) and \( e^{\B} \).

::: {#thm-golden-thompson}
[The Golden–Thompson Inequality]

Let \( \A, \B \in M_n(\nC) \) be Hermitian. Then
\[
\tr e^{\A+\B} \ \le\ \tr\bigl(e^{\A}e^{\B}\bigr) .
\]
Both sides are real and positive, and equality holds if \( \A\B = \B\A \).
:::

::: {.idea}
Run the trace power inequality at the \( m \)-th root of each exponential and let \( m \) run through the powers of two. At each \( m \) the right-hand side is exactly \( \tr(e^{\A}e^{\B}) \), independent of \( m \), while the left-hand side converges to \( \tr e^{\A+\B} \) by Lie's formula. A non-strict inequality survives a limit.
:::

::: {.proof}
Fix \( r \ge 0 \) and put \( m = 2^{r} \), \( \X = e^{\A/m} \) and \( \Y = e^{\B/m} \). Since \( \A/m \) is Hermitian with spectral resolution \( \sum_i\mu_i\P_i \), @thm-unitary-exponential (a) gives \( \X = \sum_ie^{\mu_i}\P_i \), which is Hermitian with all eigenvalues \( e^{\mu_i} > 0 \); so \( \X \succ 0 \) by @thm-pd-characterizations (b), and likewise \( \Y \succ 0 \). As in Step 1 of the proof of @lem-lie-product, \( \X^{m} = e^{\A} \) and \( \Y^{m} = e^{\B} \).

By @lem-trace-power-inequality (b),
\[
\tr\Bigl(\bigl(e^{\A/m}e^{\B/m}\bigr)^{m}\Bigr) \le \tr\bigl(\X^{m}\Y^{m}\bigr) = \tr\bigl(e^{\A}e^{\B}\bigr) .
\]
The right side does not depend on \( r \). By @lem-lie-product the matrices \( \bigl(e^{\A/m}e^{\B/m}\bigr)^{m} \) converge entrywise to \( e^{\A+\B} \) as \( m = 2^{r} \to \infty \), so their traces, being sums of \( n \) entries, converge to \( \tr e^{\A+\B} \). A non-strict inequality survives a limit, so \( \tr e^{\A+\B} \le \tr(e^{\A}e^{\B}) \).

Both sides are real and \( \ge 0 \): the left because \( \A+\B \) is Hermitian, so \( e^{\A+\B} \succ 0 \) by the argument just given, and the right by @lem-trace-of-positive-product with \( k = 1 \). They are in fact positive, since a positive definite matrix has positive trace. If \( \A\B = \B\A \), then \( e^{\A}e^{\B} = e^{\A+\B} \) by @thm-exponential-properties (d), and the two sides are equal.
:::

A two-by-two family shows that the inequality is genuinely an inequality, and lets the reader see what the two sides look like.

::: {#exm-golden-thompson-two-by-two}
[The inequality on a two-by-two family]

For real \( a, b \) let
\[
\A = \begin{pmatrix} a & 0 \\ 0 & -a \end{pmatrix}, \qquad
\B = \begin{pmatrix} 0 & b \\ b & 0 \end{pmatrix} .
\]
Compute both sides of Golden–Thompson, and decide when the inequality is strict.
:::

::: {.solution}
Both matrices are real symmetric. Write \( \M = \begin{psmallmatrix} 0 & 1 \\ 1 & 0\end{psmallmatrix} \), so that \( \B = b\M \) and \( \M^{2} = \I \). Then \( \B^{2m} = b^{2m}\I \) and \( \B^{2m+1} = b^{2m+1}\M \), so splitting the exponential series into even and odd terms gives
\[
e^{\B} = \cosh(b)\,\I + \sinh(b)\,\M = \begin{pmatrix} \cosh b & \sinh b \\ \sinh b & \cosh b\end{pmatrix} ,
\]
for every real \( b \). Since \( e^{\A} = \diag(e^{a}, e^{-a}) \), the diagonal entries of \( e^{\A}e^{\B} \) are \( e^{a}\cosh b \) and \( e^{-a}\cosh b \), whence
\[
\tr\bigl(e^{\A}e^{\B}\bigr) = (e^{a} + e^{-a})\cosh b = 2\cosh a\,\cosh b .
\]

For the left side, \( \A+\B = \begin{psmallmatrix} a & b \\ b & -a\end{psmallmatrix} \) has trace \( 0 \) and determinant \( -(a^{2}+b^{2}) \), so its eigenvalues are \( \pm d \) with \( d = \sqrt{a^{2}+b^{2}} \). By @thm-unitary-exponential (a) the eigenvalues of \( e^{\A+\B} \) are \( e^{d} \) and \( e^{-d} \), so \( \tr e^{\A+\B} = 2\cosh d \) by @thm-trace-det-eigenvalues. The inequality therefore reads
\[
\cosh\sqrt{a^{2}+b^{2}} \ \le\ \cosh a\,\cosh b ,
\]
a statement about numbers, and it can be checked term by term. Expanding both sides as power series with non-negative terms, the coefficient of \( a^{2i}b^{2j} \) is \( \binom{i+j}{i}\big/(2i+2j)! \) on the left and \( 1\big/\bigl((2i)!(2j)!\bigr) \) on the right, so what is needed is \( \binom{i+j}{i} \le \binom{2i+2j}{2i} \). That holds because doubling each of \( i \) chosen items out of \( i+j \) produces \( 2i \) chosen items out of \( 2i+2j \), injectively; and it is strict as soon as \( i, j \ge 1 \), since then some \( 2i \)-subset splits a doubled pair and so is not in the image.

Equality therefore forces every term with \( i, j \ge 1 \) to vanish, that is \( a = 0 \) or \( b = 0 \) — exactly the cases where \( \A \) and \( \B \) commute. For \( a = b = 1 \) the two sides are \( 2\cosh\sqrt2 \approx 4.3564 \) and \( 2\cosh^{2}1 \approx 4.7622 \).
:::

::: {.warning}
**Golden–Thompson is a statement about traces and about nothing else.** It is tempting to guess the Loewner-order version \( e^{\A+\B} \preceq e^{\A/2}e^{\B}e^{\A/2} \), whose right side is Hermitian and positive semidefinite and has the same trace as \( e^{\A}e^{\B} \). It is false in general. Indeed both sides have the same determinant, namely \( e^{\tr\A + \tr\B} \) by @thm-exponential-properties (e) — and if \( \M \succeq \N \succ 0 \) with \( \det\M = \det\N \), then \( \Z = \N^{-1/2}\M\N^{-1/2} \succeq \I \) by @thm-loewner-basic (a), so all eigenvalues of \( \Z \) are \( \ge 1 \) while their product is \( \det\Z = \det\M/\det\N = 1 \); hence they are all \( 1 \), the Hermitian matrix \( \Z \) equals \( \I \), and \( \M = \N^{1/2}\Z\N^{1/2} = \N \). So the Loewner inequality would force \( e^{\A+\B} = e^{\A/2}e^{\B}e^{\A/2} \), and taking traces would force equality in Golden–Thompson, which @exm-golden-thompson-two-by-two refutes for \( a = b = 1 \).
:::

## Three matrices are one too many

Golden–Thompson looks as though it should iterate. It does not. The three-matrix statement
\[
\tr e^{\A+\B+\C} \ \le\ \tr\bigl(e^{\A}e^{\B}e^{\C}\bigr)
\]
is **false**, and the failure is not marginal: the right side can be negative while the left side, a trace of a positive definite matrix, is positive. A family of two-by-two real symmetric matrices shows it, exactly.

::: {#exm-three-matrices-fails}
[The three-matrix version fails]

Let \( t > 0 \) and let \( \P_1, \P_2, \P_3 \) be the orthogonal projections of \( \nR^{2} \) onto the three lines through the origin at angles \( 0 \), \( 2\pi/3 \) and \( 4\pi/3 \):
\[
\P_1 = \begin{pmatrix} 1 & 0 \\ 0 & 0\end{pmatrix}, \quad
\P_2 = \frac14\begin{pmatrix} 1 & -\sqrt3 \\ -\sqrt3 & 3\end{pmatrix}, \quad
\P_3 = \frac14\begin{pmatrix} 1 & \sqrt3 \\ \sqrt3 & 3\end{pmatrix} .
\]
Put \( \A = t\P_1 \), \( \B = t\P_2 \), \( \C = t\P_3 \), all symmetric. Compute both sides of the three-matrix inequality and show that it fails.
:::

::: {.solution}
Each \( \P_i \) is \( \u_i\u_i\tp \) for a unit vector \( \u_i \), with \( \u_1 = (1,0) \), \( \u_2 = (-\tfrac12, \tfrac{\sqrt3}{2}) \), \( \u_3 = (-\tfrac12, -\tfrac{\sqrt3}{2}) \); each is symmetric with \( \P_i^{2} = \P_i \). Adding the three matrices gives \( \P_1 + \P_2 + \P_3 = \tfrac32\I \), so \( \A+\B+\C = \tfrac{3t}{2}\I \) and
\[
\tr e^{\A+\B+\C} = 2e^{3t/2} .
\]

For the right side, \( \P_i^{2} = \P_i \) makes the exponential series collapse: \( e^{t\P} = \I + \alpha\P \) with \( \alpha = e^{t}-1 \), because \( \sum_{j \ge 1}t^{j}\P^{j}/j! = \bigl(\sum_{j\ge1}t^{j}/j!\bigr)\P \). Expanding the product of three such factors and using \( \tr\I = 2 \), \( \tr\P_i = 1 \), \( \tr(\P_i\P_j) = (\u_i\cdot\u_j)^{2} \) and \( \tr(\P_1\P_2\P_3) = (\u_1\cdot\u_2)(\u_2\cdot\u_3)(\u_3\cdot\u_1) \),
\[
\tr\bigl(e^{\A}e^{\B}e^{\C}\bigr) = 2 + 3\alpha + \tfrac34\alpha^{2} - \tfrac18\alpha^{3} ,
\]
since each pairwise dot product is \( -\tfrac12 \), so each \( \tr(\P_i\P_j) = \tfrac14 \) and the triple product is \( -\tfrac18 \). In terms of \( t \) this is
\[
\tr\bigl(e^{\A}e^{\B}e^{\C}\bigr) = \tfrac18\bigl(-e^{3t} + 9e^{2t} + 9e^{t} - 1\bigr) .
\]

The cubic term is negative, and for large \( t \) it wins. Precisely, if \( e^{t} \ge 10 \) then \( e^{2t} \ge 10e^{t} \) and \( e^{3t} \ge 10e^{2t} = 9e^{2t} + e^{2t} \ge 9e^{2t} + 10e^{t} \), so the bracket is negative and \( \tr(e^{\A}e^{\B}e^{\C}) < 0 \), while \( \tr e^{\A+\B+\C} = 2e^{3t/2} > 0 \). Taking \( t = 3 \), where \( e^{3} > 20 \), already does this: the two sides are \( 2e^{4.5} \approx 180.0 \) and \( \tfrac18(-e^{9}+9e^{6}+9e^{3}-1) \approx -536.6 \).

The failure is not confined to large \( t \). At \( t = 1 \) the two sides are \( 2e^{3/2} \approx 8.9634 \) and \( \tfrac18(-e^{3}+9e^{2}+9e-1) \approx 8.7351 \), and at \( t = 2 \) they are \( 2e^{3} \approx 40.171 \) and \( \tfrac18(-e^{6}+9e^{4}+9e^{2}-1) \approx 19.182 \).
:::

The numbers in the example are exact, and the two closed forms may be compared by hand; only their decimal expansions are approximations.

::: {.remark}
There is a second, more basic obstruction. For three Hermitian matrices the number \( \tr(e^{\A}e^{\B}e^{\C}) \) need not be **real**, so no inequality can even be written down. With
\[
\A = a\begin{pmatrix} 0 & 1 \\ 1 & 0\end{pmatrix}, \quad
\B = b\begin{pmatrix} 0 & -i \\ i & 0\end{pmatrix}, \quad
\C = c\begin{pmatrix} 1 & 0 \\ 0 & -1\end{pmatrix},
\]
each of the three squares is a multiple of \( \I \), so each exponential splits into a hyperbolic cosine times \( \I \) plus a hyperbolic sine times the matrix, and multiplying out gives
\[
\tr\bigl(e^{\A}e^{\B}e^{\C}\bigr) = 2\cosh a\cosh b\cosh c + 2i\sinh a\sinh b\sinh c ,
\]
because the product of the three matrices above is \( i\I \) while every shorter product among them has trace \( 0 \). The imaginary part is non-zero whenever \( a, b, c \) are all non-zero. With two matrices this cannot happen, by @lem-trace-of-positive-product.
:::

::: {.remark}
Two of the three matrices commuting is enough to restore the inequality, and exercise @exr-golden-thompson-c1 asks for the three cases. So the example above is as economical as it can be: no two of \( \P_1, \P_2, \P_3 \) commute.
:::

## Klein's inequality and relative entropy

Golden–Thompson is one of a family of trace inequalities whose proofs all end in the same place: a scalar convexity inequality summed against non-negative weights that add to one. The next theorem is the cleanest member of the family. It needs one fact about convex functions of a real variable, which Chapter 18 recorded only in an exercise, so we prove it here.

::: {#lem-convex-gradient-inequality}
[A Convex Function Lies Above Its Tangent]

Let \( I \subseteq \nR \) be an open interval and let \( f \colon I \to \nR \) be convex and differentiable. Then
\[
f(s) \ \ge\ f(t) + f'(t)(s - t) \qquad \text{for all } s, t \in I .
\]
:::

::: {.proof}
Fix \( s, t \in I \). If \( s = t \) both sides are \( f(t) \). Assume \( s \ne t \) and let \( 0 < \theta \le 1 \). The point \( t + \theta(s-t) = (1-\theta)t + \theta s \) lies in \( I \), and @def-convex-function gives
\[
f\bigl(t + \theta(s-t)\bigr) \le (1-\theta)f(t) + \theta f(s) ,
\]
that is, \( \bigl(f(t + \theta(s-t)) - f(t)\bigr)/\theta \le f(s) - f(t) \). Writing \( h = \theta(s-t) \), which is non-zero and tends to \( 0 \) as \( \theta \to 0^{+} \), the left side equals
\[
(s-t)\cdot\frac{f(t+h) - f(t)}{h} \ \longrightarrow\ (s-t)f'(t) ,
\]
by differentiability of \( f \) at \( t \). A non-strict inequality survives a limit, so \( (s-t)f'(t) \le f(s) - f(t) \), which is the claim.
:::

::: {#thm-klein}
[Klein's Inequality]

Let \( I \subseteq \nR \) be an open interval and let \( f \colon I \to \nR \) be convex and differentiable. Let \( \A, \B \in M_n(\nC) \) be Hermitian with \( \spec(\A) \subseteq I \) and \( \spec(\B) \subseteq I \). Then
\[
\tr\bigl(f(\A) - f(\B) - (\A - \B)f'(\B)\bigr) \ \ge\ 0 ,
\]
where \( f(\A) \), \( f(\B) \) and \( f'(\B) \) are the functional calculus of @def-function-of-normal-operator.
:::

::: {.idea}
Compute the trace in an orthonormal eigenbasis of \( \B \). Each diagonal entry then involves \( \B \) only through one eigenvalue \( \mu_j \), and involves \( \A \) only through the numbers \( c_{ij} = \lvert\inner{\v_j}{\u_i}\rvert^{2} \), the overlaps between the two eigenbases. Those numbers are non-negative and each column of the array sums to \( 1 \), which is exactly what is needed to write the whole trace as a weighted average of the scalar quantities \( f(\lambda_i) - f(\mu_j) - f'(\mu_j)(\lambda_i - \mu_j) \). Every one of those is \( \ge 0 \) by @lem-convex-gradient-inequality.
:::

::: {.proof}
By @cor-spectral-complex-matrix there are orthonormal bases \( (\u_1, \dots, \u_n) \) and \( (\v_1, \dots, \v_n) \) of \( \nC^{n} \) with \( \A\u_i = \lambda_i\u_i \) and \( \B\v_j = \mu_j\v_j \); all \( \lambda_i \) and \( \mu_j \) lie in \( I \). Put \( c_{ij} = \lvert\inner{\v_j}{\u_i}\rvert^{2} \ge 0 \). Expanding \( \v_j \) in the orthonormal basis \( (\u_i) \) gives \( \sum_i c_{ij} = \norm{\v_j}^{2} = 1 \) for each \( j \).

For any \( \M \in M_n(\nC) \) we have \( \tr\M = \sum_j\inner{\M\v_j}{\v_j} \): with \( \V \) the unitary matrix whose columns are the \( \v_j \), the sum is \( \tr(\V^{*}\M\V) = \tr(\M\V\V^{*}) = \tr\M \) by @thm-trace-properties (3). We evaluate the three terms at \( \v_j \).

By @def-function-of-normal-operator, \( f(\A)\u_i = f(\lambda_i)\u_i \), so expanding \( \v_j = \sum_i\inner{\v_j}{\u_i}\u_i \) and using orthonormality,
\[
\inner{f(\A)\v_j}{\v_j} = \sum_{i}f(\lambda_i)\,c_{ij}, \qquad
\inner{\A\v_j}{\v_j} = \sum_{i}\lambda_i\,c_{ij} .
\]
Also \( f(\B)\v_j = f(\mu_j)\v_j \) and \( f'(\B)\v_j = f'(\mu_j)\v_j \), so \( \inner{f(\B)\v_j}{\v_j} = f(\mu_j) \) and
\[
\inner{(\A-\B)f'(\B)\v_j}{\v_j} = f'(\mu_j)\Bigl(\sum_i\lambda_ic_{ij} - \mu_j\Bigr) .
\]
Summing over \( j \), and using \( \sum_ic_{ij} = 1 \) to write \( f(\mu_j) = \sum_ic_{ij}f(\mu_j) \) and \( \mu_j = \sum_ic_{ij}\mu_j \),
\[
\tr\bigl(f(\A) - f(\B) - (\A-\B)f'(\B)\bigr)
= \sum_{i,j}c_{ij}\,\bigl[\,f(\lambda_i) - f(\mu_j) - f'(\mu_j)(\lambda_i - \mu_j)\,\bigr] .
\]
Every bracket is \( \ge 0 \) by @lem-convex-gradient-inequality, and every \( c_{ij} \ge 0 \). This proves the inequality.
:::

The corollary that made Klein's inequality famous concerns density matrices, the positive semidefinite matrices of trace \( 1 \) that Chapter 18 §08 met as a convex body (@def-density-matrix). It needs the derivative of the logarithm, which the book has not yet computed.

::: {#lem-log-derivative}
[The Derivative of the Logarithm]

The function \( \log \colon (0,\infty) \to \nR \) of @lem-exp-log is differentiable with \( \log'(y) = 1/y \). Consequently \( g(t) = t\log t \) is differentiable on \( (0,\infty) \) with \( g'(t) = \log t + 1 \) and \( g''(t) = 1/t \), and \( g \) is strictly convex there.
:::

::: {.proof}
*Continuity.* By @lem-exp-log (a) and (b), \( \exp \colon \nR \to (0,\infty) \) is a strictly increasing bijection, so \( \log \) is strictly increasing. Fix \( y > 0 \), put \( s = \log y \) and let \( \varepsilon > 0 \). Then \( e^{s-\varepsilon} < y < e^{s+\varepsilon} \), and for \( y' \) in that open interval, applying the increasing \( \log \) gives \( s - \varepsilon < \log y' < s + \varepsilon \). So \( \log \) is continuous at \( y \).

*Differentiability.* Let \( h \ne 0 \) be small enough that \( y + h > 0 \), and put \( u = \log(y+h) - s \), so that \( y + h = e^{s+u} = ye^{u} \) and \( h = y(e^{u}-1) \). Since \( \log \) is injective, \( u \ne 0 \), and \( u \to 0 \) as \( h \to 0 \) by continuity. Hence
\[
\frac{\log(y+h) - \log y}{h} = \frac{u}{y(e^{u}-1)} \ \longrightarrow\ \frac1y ,
\]
because \( (e^{u}-1)/u \to 1 \): the exponential is its own derivative (@thm-exponential-properties (b) with \( n = 1 \)), and its value at \( 0 \) is \( 1 \).

*The function \( t\log t \).* For \( t > 0 \) and small \( h \ne 0 \),
\[
\frac{(t+h)\log(t+h) - t\log t}{h} = t\cdot\frac{\log(t+h) - \log t}{h} + \log(t+h) ,
\]
which tends to \( t \cdot (1/t) + \log t = 1 + \log t \), using continuity of \( \log \). Differentiating once more, \( g''(t) = 1/t > 0 \), so \( g \) is strictly convex by @lem-convex-one-variable.
:::

::: {#cor-relative-entropy}
[Non-negativity of the Relative Entropy]

Let \( \A, \B \in M_n(\nC) \) be positive definite with \( \tr\A = \tr\B = 1 \). Then
\[
\tr\bigl(\A(\log\A - \log\B)\bigr) \ \ge\ 0 .
\]
:::

::: {.proof}
Apply @thm-klein on \( I = (0,\infty) \) to \( f(t) = t\log t \), which is convex and differentiable with \( f'(t) = \log t + 1 \) by @lem-log-derivative. Both spectra lie in \( I \) by @thm-pd-characterizations (b). By @thm-functional-calculus-properties (b), \( f'(\B) = \log\B + \I \). So Klein's inequality reads
\[
\tr(\A\log\A) - \tr(\B\log\B) - \tr\bigl((\A-\B)(\log\B + \I)\bigr) \ \ge\ 0 .
\]
Expanding the last trace by linearity, it equals \( \tr(\A\log\B) - \tr(\B\log\B) + \tr\A - \tr\B \). Substituting and canceling \( \tr(\B\log\B) \),
\[
\tr(\A\log\A) - \tr(\A\log\B) - \tr\A + \tr\B \ \ge\ 0 ,
\]
and \( \tr\A = \tr\B = 1 \) removes the last two terms.
:::

The quantity \( \tr\bigl(\A(\log\A - \log\B)\bigr) \) is the **relative entropy** of \( \A \) with respect to \( \B \), and the corollary says it is a genuine measure of discrepancy: never negative, and zero when \( \A = \B \). For diagonal \( \A \) and \( \B \) it is the familiar sum \( \sum_i a_i(\log a_i - \log b_i) \) over two probability vectors, so the corollary contains the scalar statement as its commuting case.

::: {.remark}
Klein's inequality is the trace-level shadow of §02's @lem-peierls and @thm-trace-convex: all three say that a convex function applied to a Hermitian matrix behaves, after a trace, like a convex function applied to a weighted average of eigenvalues, the weights being the overlaps between two eigenbases. The array \( (c_{ij}) \) in the proof above is doubly stochastic (@def-doubly-stochastic), and Chapter 20 §05 used the same array for Hoffman–Wielandt. It is the same object doing the same job.
:::

## What is stated here and not proved

One theorem belongs in this section by subject and is beyond its means.

**Lieb's concavity theorem.** *Let \( \X \in M_n(\nC) \) be fixed and let \( p, q \ge 0 \) with \( p + q \le 1 \). Then the map*
\[
(\A, \B) \ \longmapsto\ \tr\bigl(\X^{*}\A^{p}\X\B^{q}\bigr)
\]
*is jointly concave on pairs of positive definite matrices.* This is a theorem of Lieb, and it is **not proved in this book**. What it needs is machinery this chapter does not build: either the theory of tensor products of positive maps, or a differentiation argument through the integral representations of §10 that would have to control two variables at once. It is recorded here because it is the natural strengthening of everything above — Golden–Thompson and the concavity of \( (\A,\B) \mapsto \tr e^{\log\A + \log\B} \) both follow from it — and because a reader who meets it elsewhere should know where it sits.

**Nothing in this book depends on it.** No statement in Chapters 0 to 21 is proved using Lieb's theorem, and no later chapter is promised a consequence of it.

## Summary and transfer

Five earlier chapters left inequalities unproved, each of them an inequality that was supposed to hold for **every** unitarily invariant norm, or for **every** convex function. This chapter proved them, and the reason they could all be proved at once is that they are all the same statement about vectors: a majorization.

- **Majorization is a doubly stochastic map.** §01 proved the theorem of Hardy, Littlewood and Pólya, @thm-hardy-littlewood-polya, that \( \x \prec \y \) exactly when \( \x = \D\y \) for a doubly stochastic \( \D \), and with Birkhoff's theorem from Chapter 19, exactly when \( \x \) lies in the convex hull of the permutations of \( \y \) (@cor-majorization-convex-hull).
- **Hence every convex function.** §02's @thm-karamata turned that into \( \sum_i\phi(x_i) \le \sum_i\phi(y_i) \), and @thm-trace-convex turned it into the convexity of \( \A \mapsto \tr f(\A) \).
- **Hence every unitarily invariant norm.** §03 identified the symmetric gauge functions and showed that they are monotone under weak majorization (@thm-gauge-monotone-under-majorization); §04's @thm-von-neumann-correspondence matched them one for one with the unitarily invariant norms of @def-unitarily-invariant-norm, through \( \uinorm{\A} = \Phi(\sigma(\A)) \); §05 proved von Neumann's trace inequality; and §06's @thm-ky-fan-dominance closed the circle, making \( \sigma(\A) \prec_w \sigma(\B) \) *equivalent* to \( \uinorm{\A} \le \uinorm{\B} \) for every such norm.
- **The applications.** §06 deduced Eckart–Young (@cor-eckart-young-ui) and the nearest-unitary theorem (@cor-polar-nearest-ui) in every unitarily invariant norm; §07 did the same for Lidskii (@thm-lidskii-ui) and Mirsky (@thm-mirsky-ui).
- **The order-theoretic half.** §08 studied operator convexity and proved the Hansen–Pedersen–Jensen inequality (@thm-jensen-operator); §09 proved that operator monotonicity of order \( n \) is exactly positivity of every \( n \times n \) Loewner matrix (@thm-loewner-matrix-criterion); §10 assembled Loewner's theorem (@thm-loewner), and with it @cor-power-operator-monotone and @cor-log-operator-monotone; §11 built the matrix geometric mean (@def-geometric-mean).
- **The exponential.** This section proved Lie's product formula, the trace power inequality, Golden–Thompson and Klein's inequality, and showed that three matrices break the pattern.

Six moves did the work of the chapter.

- **A majorization is a doubly stochastic map.** To prove something for all \( \x \prec \y \), write \( \x = \D\y \) and let convexity act one row at a time (§01, §02). *Transfer:* when a hypothesis is a family of inequalities between partial sums, look for the linear map that realizes it; the inequalities are usually the vertices of a polytope in disguise.
- **A symmetric gauge turns a weak majorization into a norm inequality.** A norm that cannot tell coordinates apart, and cannot see their signs, is monotone along \( \prec_w \) (§03, §04). *Transfer:* to prove one inequality for a whole family of norms, find the single combinatorial statement about the underlying numbers that all of them respect.
- **A Hermitian dilation turns singular values into eigenvalues.** Chapter 17 §09's \( \cH(\A) \) has eigenvalues \( \pm\sigma_i(\A) \), so every theorem about eigenvalues of Hermitian matrices has a singular-value twin (§04, §07). *Transfer:* when a result is known for Hermitian matrices and wanted for all matrices, look for the Hermitian matrix whose spectrum encodes the data.
- **The Schur product theorem turns a Loewner matrix into monotonicity.** The derivative of \( f \) at a diagonal matrix is a Hadamard product with the Loewner matrix, and Chapter 13 §07 says that a Hadamard product of positive semidefinite matrices is positive semidefinite (§09). *Transfer:* to show that a matrix-valued function is increasing, differentiate it and recognize the derivative as an entrywise product.
- **A limit of Riemann sums carries the Loewner order through an integral.** The positive semidefinite cone is closed, so an integral of positive semidefinite matrices is positive semidefinite (§10). *Transfer:* an order defined by a closed convex cone survives any limit, so it survives integration; the only work is building the integral.
- **Lie's product formula turns a sum in the exponent into a product.** @lem-lie-product replaces \( e^{\A+\B} \), which nothing can be said about directly, by a limit of products, each of which can be attacked with Cauchy–Schwarz (this section). *Transfer:* when two operations fail to commute, split one of them into \( k \) small steps, estimate the error of a single step as \( O(1/k^{2}) \), and let telescoping absorb the factor \( k \).

The chapter paid the following promises, in the words in which they were made.

| The promise | Made in | Paid by |
|---|---|---|
| Hardy–Littlewood–Pólya, "\( \x \prec \y \) exactly when \( \x = \D\y \) for a doubly stochastic \( \D \)" | Chapter 19 §09 | §01 |
| "the general consequences of a majorization \( \x \prec \y \), namely \( \sum_i\phi(x_i) \le \sum_i\phi(y_i) \) for every convex \( \phi \)" | Chapter 17 §07 | §02 and §07 |
| "for the whole class of functions that reverse majorization" (the product is Schur-concave) | Chapter 17 §08 | §02 |
| "\( \A \mapsto \tr f(\A) \) … is proved in Chapter 21" | Chapter 18 §10 | §02 |
| "It has not said which norms are invariant under unitary multiplication, which is Chapter 21" | Chapter 16 §08 | §04 |
| "The repair is to apply \( N_k \) to the singular values instead of the eigenvalues, which is what Chapter 21 does" | Chapter 17 §06 | §04 |
| Eckart–Young "in **every** unitarily invariant norm", by a route that "needs inequalities between the singular values of \( \A \) and of \( \A - \B \), not a projection argument" | Chapter 13 §10, Chapter 16 §08, Chapter 17 §09 | §06 |
| "\( \W \) also minimizes the distance in every unitarily invariant norm" | Chapter 13 §09 | §06 |
| "with \( \phi(t) = t^2 \) this is @cor-hoffman-wielandt-hermitian again" | Chapter 20 §05 | §07 |
| "one statement covering every unitarily invariant norm" (the index-by-index singular-value bound and Mirsky) | Chapter 20 §10 and §11 | §07 |
| "\( t \mapsto t^{s} \) is operator monotone on \( [0,\infty) \) exactly for \( 0 \le s \le 1 \)", with "the companion fact that \( t \mapsto \log t \) is operator monotone while \( t \mapsto e^{t} \) is not" | Chapter 13 §05 | §10, modulo (A7) |

Some things the chapter did not do. Loewner's theorem is proved here only up to one quoted fact, **(A7)**, the Nevanlinna–Pick characterization of Pick functions; §10 says precisely which implication rests on it, and §09's elementary half — that for a continuously differentiable \( f \), monotonicity of every order is exactly positivity of every Loewner matrix — is proved in full. The Lieb–Thirring inequality, which would remove the restriction to \( m = 2^{r} \) in @lem-trace-power-inequality, is not proved, and nothing here needs it. Lieb's concavity theorem is stated above and not proved, and nothing in the book depends on it. The equality cases of von Neumann's trace inequality and of Golden–Thompson were treated only in the directions that were needed.

**Part V ends here.** It began in Chapter 16 with a complaint: nine chapters had said "close" and "small" with nothing to measure by. A norm supplied the yardstick, and the five chapters since have been spent finding out what a yardstick is good for. Chapter 17 made the eigenvalues of a Hermitian matrix into the values of an optimization problem, so that they could be compared. Chapter 18 supplied the language of convexity in which such comparisons live. Chapter 19 studied the one class of non-Hermitian matrices — the non-negative ones — where a comparable theory exists, and produced Birkhoff's theorem, which this chapter used once. Chapter 20 asked how much the answers move when the data move. And Chapter 21 has collected the inequalities that all five chapters kept needing, and shown that they are one inequality seen from different sides. What none of these chapters has done is compute anything: every proof here is an existence or a comparison, and not one of them is an algorithm. That is the subject of Chapter 24.

## Exercises

### A. Check your understanding

:::: {#exr-golden-thompson-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the Golden–Thompson inequality, with its hypotheses.
2. State Lie's product formula, and say for which matrices it holds.
3. True or false: for Hermitian \( \A, \B \) the matrix \( e^{\A}e^{\B} \) is positive semidefinite. Justify your answer.
4. True or false: \( \tr e^{\A+\B} \le \tr(e^{\B}e^{\A}) \) for Hermitian \( \A, \B \). Justify your answer.
5. True or false: \( \tr e^{\A+\B+\C} \le \tr(e^{\A}e^{\B}e^{\C}) \) for Hermitian \( \A, \B, \C \). Justify your answer.
6. Where in the proof of @thm-golden-thompson is the hypothesis that \( \A \) and \( \B \) are Hermitian used?
:::
::::

::: {.solution}
(a) For Hermitian \( \A, \B \in M_n(\nC) \), \( \tr e^{\A+\B} \le \tr(e^{\A}e^{\B}) \) (@thm-golden-thompson). No commutativity is assumed; if \( \A\B = \B\A \) the two sides are equal.

(b) \( e^{\A+\B} = \lim_k (e^{\A/k}e^{\B/k})^{k} \) for **all** \( \A, \B \in M_n(\nC) \), Hermitian or not (@lem-lie-product).

(c) False, since positive semidefinite includes Hermitian (@def-positive-semidefinite (P1)) and \( (e^{\A}e^{\B})^{*} = e^{\B}e^{\A} \), which equals \( e^{\A}e^{\B} \) only when the two exponentials commute. In @exm-golden-thompson-two-by-two with \( a = b = 1 \),
\[
e^{\A}e^{\B} = \begin{pmatrix} e\cosh 1 & e\sinh 1 \\ e^{-1}\sinh 1 & e^{-1}\cosh 1\end{pmatrix} ,
\]
which is not symmetric because \( e\sinh 1 \ne e^{-1}\sinh 1 \).

(d) True. \( \tr(e^{\B}e^{\A}) = \tr(e^{\A}e^{\B}) \) by @thm-trace-properties (3), and \( \A + \B = \B + \A \), so this is @thm-golden-thompson with the roles exchanged.

(e) False; see @exm-three-matrices-fails, where the right side is negative and the left side positive. The right side need not even be real (the remark after that example).

(f) In two places. First, to know that \( e^{\A/m} \) and \( e^{\B/m} \) are positive semidefinite, which is the hypothesis of @lem-trace-power-inequality (b). Second, in @lem-trace-of-positive-product, which is what makes \( \tr(e^{\A}e^{\B}) \) real so that the inequality is a statement about real numbers.
:::

### B. Practice

:::: {#exr-golden-thompson-b1}
[B1: Both sides, exactly]

Let
\[
\A = \begin{pmatrix} 0 & 0 \\ 0 & -2\end{pmatrix}, \qquad
\B = \begin{pmatrix} 0 & 1 \\ 1 & 0\end{pmatrix} .
\]

::: {.enumerate options="label=(\alph*)"}
1. Compute \( e^{\A} \), \( e^{\B} \) and \( \tr(e^{\A}e^{\B}) \) exactly.
2. Compute \( \tr e^{\A+\B} \) exactly, and verify @thm-golden-thompson numerically to three decimal places.
:::
::::

::: {.solution}
(a) \( \A \) is diagonal, so \( e^{\A} = \diag(1, e^{-2}) \). Since \( \B^{2} = \I \), splitting the series into even and odd terms gives \( e^{\B} = \cosh(1)\I + \sinh(1)\B \), that is
\[
e^{\B} = \begin{pmatrix} \cosh 1 & \sinh 1 \\ \sinh 1 & \cosh 1\end{pmatrix} .
\]
Hence \( e^{\A}e^{\B} \) has diagonal entries \( \cosh 1 \) and \( e^{-2}\cosh 1 \), so
\[
\tr(e^{\A}e^{\B}) = (1 + e^{-2})\cosh 1 = \frac{(1+e^{-2})(e + e^{-1})}{2} .
\]
Numerically \( (1 + 0.135335)(1.543081) = 1.751914 \).

(b) \( \A + \B = \begin{psmallmatrix} 0 & 1 \\ 1 & -2\end{psmallmatrix} \) has trace \( -2 \) and determinant \( -1 \), so its characteristic polynomial is \( x^{2} + 2x - 1 \) and its eigenvalues are \( -1 \pm \sqrt2 \). A Hermitian matrix has \( \tr e^{\M} = \sum_i e^{\lambda_i} \) by @thm-unitary-exponential (a) and @thm-trace-det-eigenvalues, so
\[
\tr e^{\A+\B} = e^{-1+\sqrt2} + e^{-1-\sqrt2} = 2e^{-1}\cosh\sqrt2 .
\]
Numerically \( 2(0.367879)(2.178183) = 1.602618 \). Indeed \( 1.603 \le 1.752 \), and the inequality is strict because \( \A \) and \( \B \) do not commute: \( \A\B = \begin{psmallmatrix} 0 & 0 \\ -2 & 0\end{psmallmatrix} \) while \( \B\A = \begin{psmallmatrix} 0 & -2 \\ 0 & 0\end{psmallmatrix} \).
:::

:::: {#exr-golden-thompson-b2}
[B2: The trace power inequality on integers]

Let \( \X = \diag(2, 1) \) and \( \Y = \begin{psmallmatrix} 1 & 1 \\ 1 & 1\end{psmallmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Check that \( \X \) and \( \Y \) are positive semidefinite, and compute \( \tr\bigl((\X\Y)^{m}\bigr) \) and \( \tr(\X^{m}\Y^{m}) \) for \( m = 1, 2, 4 \).
2. Verify @lem-trace-power-inequality (b) in these three cases, and say for which of them it is strict.
:::
::::

::: {.solution}
(a) \( \X \) is diagonal, so its eigenvalues are \( 2 \) and \( 1 \); \( \Y \) is symmetric with trace \( 2 \) and determinant \( 0 \), so its eigenvalues are \( 2 \) and \( 0 \). Both lists are non-negative, so \( \X \succeq 0 \) and \( \Y \succeq 0 \) by @thm-psd-characterizations (b).

Now \( \X\Y = \begin{psmallmatrix} 2 & 2 \\ 1 & 1\end{psmallmatrix} \), which has trace \( 3 \) and determinant \( 0 \), so its eigenvalues are \( 3 \) and \( 0 \) and \( \tr\bigl((\X\Y)^{m}\bigr) = 3^{m} \): the values are \( 3, 9, 81 \). On the other side \( \Y^{m} = 2^{m-1}\Y \), since \( \Y^{2} = 2\Y \), and \( \X^{m} = \diag(2^{m}, 1) \), so
\[
\tr(\X^{m}\Y^{m}) = 2^{m-1}\tr\bigl(\diag(2^{m},1)\Y\bigr) = 2^{m-1}(2^{m}+1) ,
\]
giving \( 3, 10, 136 \) for \( m = 1, 2, 4 \).

(b) The inequality \( 3^{m} \le 2^{m-1}(2^{m}+1) \) holds in all three cases. It is an equality at \( m = 1 \), as the base case of the induction says it must be, and strict at \( m = 2 \) (\( 9 < 10 \)) and \( m = 4 \) (\( 81 < 136 \)).
:::

:::: {#exr-golden-thompson-b3}
[B3: Klein with the exponential]

Let \( \A, \B \in M_n(\nC) \) be Hermitian. Use @thm-klein with \( f(t) = e^{t} \) to prove
\[
\tr e^{\A} \ \ge\ \tr e^{\B} + \tr\bigl((\A - \B)e^{\B}\bigr) ,
\]
and check the inequality for \( \A = \diag(1, 0) \), \( \B = \0 \).
::::

::: {.solution}
The function \( f(t) = e^{t} \) is differentiable on \( I = \nR \) with \( f' = f \), and it is convex by @lem-exp-log (a). Both spectra are real, hence contained in \( I \). So @thm-klein gives
\[
\tr\bigl(e^{\A} - e^{\B} - (\A-\B)e^{\B}\bigr) \ \ge\ 0 ,
\]
and the trace is linear (@thm-trace-properties (1)), so this rearranges to the stated inequality.

For \( \A = \diag(1,0) \) and \( \B = \0 \): \( \tr e^{\A} = e + 1 \approx 3.71828 \), \( \tr e^{\B} = \tr\I = 2 \), and \( \tr(\A e^{\0}) = \tr\A = 1 \). So the inequality reads \( 3.71828 \ge 3 \), and it is strict.
:::

### C. Going deeper

:::: {#exr-golden-thompson-c1}
[C1: Two out of three is enough]

Let \( \A, \B, \C \in M_n(\nC) \) be Hermitian. Prove that
\[
\tr e^{\A+\B+\C} \ \le\ \tr\bigl(e^{\A}e^{\B}e^{\C}\bigr)
\]
holds whenever **some two** of the three matrices commute, treating the three cases separately. Explain why this does not contradict @exm-three-matrices-fails.

*Hint: @thm-exponential-properties (d), and the cyclic invariance of the trace.*
::::

::: {.solution}
*Case 1: \( \B\C = \C\B \).* Then \( e^{\B}e^{\C} = e^{\B+\C} \) by @thm-exponential-properties (d), so \( \tr(e^{\A}e^{\B}e^{\C}) = \tr(e^{\A}e^{\B+\C}) \). Since \( \B + \C \) is Hermitian, @thm-golden-thompson applied to the pair \( \A, \B+\C \) gives \( \tr e^{\A+\B+\C} \le \tr(e^{\A}e^{\B+\C}) \), as required.

*Case 2: \( \A\B = \B\A \).* Then \( e^{\A}e^{\B} = e^{\A+\B} \), so \( \tr(e^{\A}e^{\B}e^{\C}) = \tr(e^{\A+\B}e^{\C}) \), and @thm-golden-thompson applied to \( \A+\B \) and \( \C \) finishes.

*Case 3: \( \A\C = \C\A \).* By @thm-trace-properties (3), \( \tr(e^{\A}e^{\B}e^{\C}) = \tr(e^{\C}e^{\A}e^{\B}) = \tr(e^{\A+\C}e^{\B}) \), the last step because \( \A \) and \( \C \) commute. Now @thm-golden-thompson applied to \( \A+\C \) and \( \B \) gives \( \tr e^{\A+\B+\C} \le \tr(e^{\A+\C}e^{\B}) \).

There is no contradiction: in @exm-three-matrices-fails no two of \( \P_1, \P_2, \P_3 \) commute. Indeed, suppose two orthogonal projections \( \P, \Q \) onto distinct lines commute. Then \( \P\Q \) is Hermitian, since \( (\P\Q)^{*} = \Q\P = \P\Q \), and idempotent, since \( \P\Q\P\Q = \P^{2}\Q^{2} = \P\Q \); so it is an orthogonal projection, and its image lies in the image of \( \P \) and in that of \( \Q \), which meet only in \( \0 \). Hence \( \P\Q = \0 \), which for \( \P = \u\u\tp \) and \( \Q = \w\w\tp \) says \( \u\cdot\w = 0 \). But the three unit vectors above pair to \( -\tfrac12 \), never \( 0 \). For instance \( \P_1\P_2 = \tfrac14\begin{psmallmatrix} 1 & -\sqrt3 \\ 0 & 0\end{psmallmatrix} \ne \0 \).
:::

:::: {#exr-golden-thompson-c2}
[C2: The symmetric Lie formula]

Let \( \A, \B \in M_n(\nC) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( e^{\A+\B} = \lim_{k\to\infty}\bigl(e^{\A/2k}e^{\B/k}e^{\A/2k}\bigr)^{k} \).
2. Deduce that for Hermitian \( \A, \B \) one also has \( \tr e^{\A+\B} \le \tr\bigl(e^{\A/2}e^{\B}e^{\A/2}\bigr) \), and explain why this is not a new inequality.
:::

*Hint: for (a), rerun Steps 2–4 of the proof of @lem-lie-product with the new \( \T_k \); only the constant \( M \) changes.*
::::

::: {.solution}
(a) Keep \( \S_k = e^{(\A+\B)/k} \) and set \( \T_k = e^{\A/2k}e^{\B/k}e^{\A/2k} \). Step 1 of the proof of @lem-lie-product is unchanged: \( \S_k^{k} = e^{\A+\B} \). For Step 2, submultiplicativity and @thm-exponential-norm-bound (a) give \( \norm{\T_k}_2 \le e^{a/2k}e^{b/k}e^{a/2k} = e^{c/k} \), the same bound as before, with \( a = \norm{\A}_2 \), \( b = \norm{\B}_2 \), \( c = a+b \). For Step 3, write \( e^{\X} = \I + \X + \R(\X) \) as there and multiply out the three factors. Choosing the \( \I \) from all three gives \( \I \); choosing exactly one non-identity term gives \( \tfrac{\A}{2k} + \tfrac{\B}{k} + \tfrac{\A}{2k} = \tfrac{\A+\B}{k} \) together with the three remainders \( \R(\tfrac{\A}{2k}) \), \( \R(\tfrac{\B}{k}) \), \( \R(\tfrac{\A}{2k}) \). Every other term is a product of at least two non-identity factors. Once \( k \ge \max(1, c) \), each \( \R \) has norm at most \( c^{2}e/(2k^{2}) \) by @thm-exponential-norm-bound (c), so every non-identity factor has norm at most \( K/k \) with \( K = c + c^{2}e/2 \); a product of \( j \) of them therefore has norm at most \( K^{j}/k^{j} \), which for \( 2 \le j \le 3 \) and \( k \ge 1 \) is at most \( \max(K^{2}, K^{3})/k^{2} \). There are \( 27 \) terms in all. Subtracting from \( \S_k = \I + \tfrac{\A+\B}{k} + \R(\tfrac{\A+\B}{k}) \), the \( \I \) and the linear terms cancel and what is left is a sum of at most \( 27 \) terms, each of norm at most a constant over \( k^{2} \), so \( \norm{\S_k - \T_k}_2 \le M'/k^{2} \) for a constant \( M' \) depending only on \( \A \) and \( \B \). Step 4 is verbatim, and yields \( \norm{e^{\A+\B} - \T_k^{k}}_2 \le e^{c}M'/k \to 0 \).

(b) By @thm-trace-properties (3), \( \tr\bigl(e^{\A/2}e^{\B}e^{\A/2}\bigr) = \tr\bigl(e^{\A/2}e^{\A/2}e^{\B}\bigr) = \tr(e^{\A}e^{\B}) \), the last step by @thm-exponential-properties (d) since \( \A/2 \) commutes with itself. So the two right-hand sides are the same number and the inequality is @thm-golden-thompson restated. What is new is only the form: the middle expression is a positive semidefinite matrix, being \( (e^{\A/2})^{*}e^{\B}e^{\A/2} \) with \( e^{\A/2} \) Hermitian (@prp-congruence-positivity (a)), whereas \( e^{\A}e^{\B} \) is not Hermitian. The warning after @exm-golden-thompson-two-by-two shows that the Loewner-order strengthening of this form is nevertheless false.
:::

:::: {#exr-golden-thompson-c3}
[C3: When is the relative entropy zero?]

Let \( \A, \B \in M_n(\nC) \) be positive definite with \( \tr\A = \tr\B = 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Show that equality holds in @lem-convex-gradient-inequality for \( f(t) = t\log t \) only when \( s = t \).
2. Deduce that \( \tr\bigl(\A(\log\A - \log\B)\bigr) = 0 \) forces \( \A = \B \).
:::

*Hint: for (b), look at which coefficients \( c_{ij} \) in the proof of @thm-klein can be non-zero.*
::::

::: {.solution}
(a) By @lem-log-derivative, \( f(t) = t\log t \) is **strictly** convex on \( (0,\infty) \). Let \( s \ne t \) in \( (0,\infty) \) and let \( m = \tfrac12(s+t) \) be their midpoint, which also lies in \( (0,\infty) \). Strict convexity gives
\[
f(m) < \tfrac12 f(t) + \tfrac12 f(s) ,
\]
while @lem-convex-gradient-inequality applied at the point \( t \) with \( m \) in place of \( s \) gives
\[
f(m) \ \ge\ f(t) + f'(t)(m - t) = f(t) + \tfrac12 f'(t)(s-t) .
\]
Combining and multiplying by \( 2 \), \( 2f(t) + f'(t)(s-t) < f(t) + f(s) \), that is \( f(s) > f(t) + f'(t)(s-t) \). So the inequality is strict whenever \( s \ne t \).

(b) In the proof of @thm-klein with \( f(t) = t\log t \), the total is \( \sum_{i,j}c_{ij}\bigl[f(\lambda_i) - f(\mu_j) - f'(\mu_j)(\lambda_i-\mu_j)\bigr] \), with all \( c_{ij} \ge 0 \) and every bracket \( \ge 0 \). The computation in @cor-relative-entropy shows that this total equals \( \tr\bigl(\A(\log\A - \log\B)\bigr) \) when \( \tr\A = \tr\B \). If it is \( 0 \), then \( c_{ij} = 0 \) whenever the bracket is non-zero, that is, by (a), whenever \( \lambda_i \ne \mu_j \).

So \( \inner{\v_j}{\u_i} = 0 \) whenever \( \lambda_i \ne \mu_j \). Fix \( j \) and expand \( \v_j = \sum_i\inner{\v_j}{\u_i}\u_i \): only indices \( i \) with \( \lambda_i = \mu_j \) contribute, so \( \v_j \) lies in the eigenspace of \( \A \) for the eigenvalue \( \mu_j \), giving \( \A\v_j = \mu_j\v_j = \B\v_j \). This holds for every \( j \), and the \( \v_j \) form a basis, so \( \A = \B \).
:::
