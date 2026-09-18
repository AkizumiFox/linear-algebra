# Products Entry by Entry

Matrix multiplication is not the only way to multiply two matrices of the same size. There is a much simpler product — multiply the entries in matching positions — which is useless for composing linear maps and extremely useful everywhere else. This section introduces it and proves the one theorem that makes it interesting: it preserves positivity. A determinant inequality follows, and it contains Hadamard's inequality of Section 6 as a special case.

Throughout, \( F = \nR \) or \( F = \nC \).

## The entrywise product

Two matrices of the same shape can be multiplied the way two lists of numbers are: position by position. The operation has no interpretation in terms of linear maps, which is one reason it looks like a curiosity at first sight, and it is written with a small circle to keep it away from ordinary multiplication.

*The Hadamard product multiplies matrices the way a spreadsheet would.*

::: {#def-hadamard-product}
[Hadamard Product]

Let \( \A, \B \in M_{m \times n}(F) \). Their **Hadamard product**, or **entrywise product**, is the matrix \( \A \circ \B \in M_{m \times n}(F) \) with

\[
(\A \circ \B)_{ij} = a_{ij}b_{ij} \qquad\text{for all } i, j .
\]
:::

Both factors must have **the same shape**, and the result has that shape too; there is no rule like "columns of the first match rows of the second". The operation is commutative and associative, and it is bilinear — \( (\A + \A') \circ \B = \A \circ \B + \A' \circ \B \) and \( (c\A) \circ \B = c(\A \circ \B) \) — because each of these is a statement about numbers, checked one entry at a time. Its identity element is the all-ones matrix \( \J \), not \( \I \).

**Examples.**

- \( \begin{pmatrix} 1 & 2 \\ 3 & 4\end{pmatrix} \circ \begin{pmatrix} 5 & 0 \\ -1 & 2\end{pmatrix} = \begin{pmatrix} 5 & 0 \\ -3 & 8\end{pmatrix} \).
- \( \A \circ \I = \diag(a_{11}, \dots, a_{nn}) \): multiplying entrywise by the identity **erases** everything off the diagonal, where ordinary multiplication by \( \I \) changes nothing.
- \( \A \circ \J = \A \), so \( \J \) is the identity for \( \circ \).
- For two diagonal matrices, \( \D \circ \D' = \D\D' \): both products are \( \diag(d_1d_1', \dots, d_nd_n') \). For matrices in general the two have nothing to do with each other, though they can coincide by accident: \( \begin{psmallmatrix}1&1\\0&0\end{psmallmatrix} \) and \( \begin{psmallmatrix}1&0\\0&0\end{psmallmatrix} \) have equal Hadamard and matrix products without either being diagonal.
- For column vectors \( \u, \w \in F^n \), regarded as \( n \times 1 \) matrices, \( \u \circ \w = (u_1w_1, \dots, u_nw_n) \).

**Non-example by minimal change.** Take \( \A = \begin{psmallmatrix} 0 & 1 \\ 1 & 0\end{psmallmatrix} \) and \( \B = \A \). Then \( \A\B = \I \), but \( \A \circ \B = \begin{psmallmatrix} 0 & 1 \\ 1 & 0\end{psmallmatrix} \circ \begin{psmallmatrix} 0 & 1 \\ 1 & 0\end{psmallmatrix} = \begin{psmallmatrix} 0 & 1 \\ 1 & 0\end{psmallmatrix} \). The two products differ, and they differ in the most basic way: \( \A \) is its own inverse and its own Hadamard square.

::: {.warning}
**\( \A \circ \B \) is not \( \A\B \), and almost nothing carries over.** Two invertible matrices can have a singular entrywise product:

\[
\begin{pmatrix} 1 & 2 \\ 2 & 1\end{pmatrix} \circ \begin{pmatrix} 2 & 1 \\ 1 & 2\end{pmatrix} = \begin{pmatrix} 2 & 2 \\ 2 & 2\end{pmatrix} ,
\]

where the two factors have determinants \( -3 \) and \( 3 \) and the product has determinant \( 0 \). There is no formula for \( \det(\A \circ \B) \) in terms of \( \det \A \) and \( \det \B \), no relation between the eigenvalues, and no rule \( (\A \circ \B)^{-1} = \A^{-1} \circ \B^{-1} \). The one structural property that does survive is the subject of this section, and it is a genuine surprise.
:::

The name is the same one that Section 6 attached to a determinant inequality. That is a coincidence of a busy mathematician, not of the mathematics: Hadamard's inequality and the Hadamard product are unrelated statements, and this section will nonetheless prove one from the other.

## The Schur product theorem

Positivity is a statement about the quadratic form \( \x^{*}\A\x \), and the quadratic form of \( \A \circ \B \) has no visible relation to those of \( \A \) and \( \B \). So the following theorem cannot be proved by staring at the form. What works is to break both matrices into the simplest positive pieces there are — rank-one matrices \( \u\u^{*} \) — and to notice that the entrywise product of two such pieces is again one.

::: {#lem-hadamard-rank-one}
[Entrywise product of two rank-one positive matrices]

Let \( \u, \w \in F^n \). Then

\[
(\u\u^{*}) \circ (\w\w^{*}) = (\u \circ \w)(\u \circ \w)^{*} .
\]
:::

::: {.proof}
Compare the \( (i, j) \) entries. The \( (i, j) \) entry of \( \u\u^{*} \) is \( u_i\conj{u_j} \) and that of \( \w\w^{*} \) is \( w_i\conj{w_j} \), so the left-hand side has \( (i, j) \) entry

\[
u_i\conj{u_j}\,w_i\conj{w_j} = (u_iw_i)\,\conj{(u_jw_j)} ,
\]

the rearrangement using commutativity of \( F \) and \( \conj{u_j}\,\conj{w_j} = \conj{u_jw_j} \). The vector \( \u \circ \w \) has \( i \)-th entry \( u_iw_i \), so the right-hand side has \( (i, j) \) entry \( (u_iw_i)\conj{(u_jw_j)} \) as well. The two matrices agree entry by entry.
:::

That one line is the whole theorem; everything else is bookkeeping over the spectral decompositions.

::: {#thm-schur-product}
[Schur Product Theorem]

Let \( \A, \B \in M_n(F) \).

::: {.enumerate options="label=(\alph*)"}
1. If \( \A \succeq 0 \) and \( \B \succeq 0 \), then \( \A \circ \B \succeq 0 \).
2. If \( \A \succ 0 \) and \( \B \succ 0 \), then \( \A \circ \B \succ 0 \).
:::
:::

::: {.idea}
For (a): the spectral theorem writes \( \A = \sum_i\lambda_i\u_i\u_i^{*} \) and \( \B = \sum_j\mu_j\w_j\w_j^{*} \) with all \( \lambda_i, \mu_j \ge 0 \). Expand \( \A \circ \B \) by bilinearity into \( n^2 \) terms; by @lem-hadamard-rank-one each term is a non-negative multiple of a matrix \( \z\z^{*} \), and those are positive semidefinite. A sum of positive semidefinite matrices is positive semidefinite, so we are done.

For (b), do not redo the argument with strict inequalities: the vectors \( \u_i \circ \w_j \) need not span, and the bookkeeping becomes unpleasant. Instead peel a multiple of the identity off \( \B \). If \( \varepsilon > 0 \) is the smallest eigenvalue of \( \B \), then \( \B = (\B - \varepsilon\I) + \varepsilon\I \) with \( \B - \varepsilon\I \succeq 0 \), so
\[
\A \circ \B = \A \circ (\B - \varepsilon\I) + \varepsilon\,(\A \circ \I) ,
\]
and \( \A \circ \I \) is the diagonal matrix of the \( a_{ii} \), which are strictly positive. Part (a) handles the first term, and a positive definite matrix plus a positive semidefinite one is positive definite.
:::

::: {.proof}
(a) Both \( \A \) and \( \B \) are Hermitian, so each has an orthonormal basis of eigenvectors. Let \( (\u_1, \dots, \u_n) \) be one for \( \A \), with \( \A\u_i = \lambda_i\u_i \), and let \( \U \) be the unitary matrix with these columns, so that \( \A = \U\D\U^{*} \) with \( \D = \diag(\lambda_1, \dots, \lambda_n) \) by @cor-spectral-complex-matrix over \( \nC \) and @cor-spectral-real-matrix over \( \nR \). The columns of \( \U\D \) are \( \lambda_i\u_i \) and the rows of \( \U^{*} \) are \( \u_i^{*} \), so @cor-outer-product-expansion gives

\[
\A = \sum_{i=1}^{n}\lambda_i\,\u_i\u_i^{*} ,
\]

which over \( \nR \) is @cor-symmetric-rank-one-sum. In the same way \( \B = \sum_{j}\mu_j\w_j\w_j^{*} \). Every \( \lambda_i \ge 0 \) and every \( \mu_j \ge 0 \), by @thm-psd-characterizations (b).

The Hadamard product is bilinear, so expanding both sums,

\[
\A \circ \B = \sum_{i=1}^{n}\sum_{j=1}^{n} \lambda_i\mu_j\,\bigl[(\u_i\u_i^{*}) \circ (\w_j\w_j^{*})\bigr]
= \sum_{i,j} \lambda_i\mu_j\,\z_{ij}\z_{ij}^{*} ,
\]

where \( \z_{ij} = \u_i \circ \w_j \) and the second equality is @lem-hadamard-rank-one. Each \( \z_{ij}\z_{ij}^{*} \) is positive semidefinite by @exm-psd-first-examples (b), and each coefficient \( \lambda_i\mu_j \) is a non-negative real number. A non-negative combination of positive semidefinite matrices is positive semidefinite (@exr-positive-definite-matrices-c2 (a)), so \( \A \circ \B \succeq 0 \).

(b) Let \( \varepsilon > 0 \) be the smallest eigenvalue of \( \B \), which is positive by @thm-pd-characterizations (b). The matrix \( \B - \varepsilon\I \) is Hermitian with eigenvalues \( \mu_j - \varepsilon \ge 0 \), so \( \B - \varepsilon\I \succeq 0 \) by @thm-psd-characterizations (b). Since \( \circ \) is bilinear and \( \A \circ \I = \diag(a_{11}, \dots, a_{nn}) \),

\[
\A \circ \B = \A \circ (\B - \varepsilon\I) \;+\; \varepsilon\,\diag(a_{11}, \dots, a_{nn}) .
\]

The first term is positive semidefinite by (a). In the second, \( a_{ii} = \inner{\A\e_i}{\e_i} > 0 \) because \( \A \succ 0 \) and \( \e_i \ne \0 \), so \( \varepsilon\diag(a_{11}, \dots, a_{nn}) \succ 0 \) by @exm-psd-first-examples (a). For \( \x \ne \0 \), the quadratic form of the sum is \( \ge 0 \) plus \( > 0 \), hence \( > 0 \). So \( \A \circ \B \succ 0 \), and the theorem is proved.
:::

The theorem is a genuine addition to the list of operations that preserve positivity. Sums and non-negative multiples were easy (@exr-positive-definite-matrices-c2), congruence was easy (@prp-congruence-positivity), and the ordinary product is not on the list at all, since \( \A\B \) need not even be Hermitian. The entrywise product is on the list, and nothing in the definition of positivity suggests it should be.

::: {#exm-schur-product-three}
[A \( 3 \times 3 \) Entrywise Product]

Let

\[
\A = \begin{pmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2 \end{pmatrix},
\qquad
\B = \begin{pmatrix} 1 & -1 & 1 \\ -1 & 2 & -1 \\ 1 & -1 & 3 \end{pmatrix} .
\]

Check that \( \A \succ 0 \) and \( \B \succ 0 \), compute \( \A \circ \B \), and verify directly that it is positive definite.
:::

::: {.solution}
The leading principal minors of \( \A \) are \( 2 \), \( 4 - 1 = 3 \) and, expanding along the first row, \( 2(4-1) - 1(2-0) = 4 \). All are positive, so \( \A \succ 0 \) by Sylvester's criterion (@thm-pd-characterizations (d)).

Those of \( \B \) are \( 1 \), \( 2 - 1 = 1 \) and \( 1(6-1) + 1(-3+1) + 1(1-2) = 5 - 2 - 1 = 2 \). All positive, so \( \B \succ 0 \).

Entry by entry,

\[
\A \circ \B = \begin{pmatrix} 2 & -1 & 0 \\ -1 & 4 & -1 \\ 0 & -1 & 6 \end{pmatrix} ,
\]

whose leading principal minors are \( 2 \), \( 8 - 1 = 7 \) and \( 2(24 - 1) + 1(-6 - 0) = 46 - 6 = 40 \). All positive, so \( \A \circ \B \succ 0 \), as @thm-schur-product (b) promised. Note that the eigenvalues of \( \A \circ \B \) have nothing to do with those of \( \A \) and \( \B \), and that \( \det(\A \circ \B) = 40 \) is much larger than \( \det \A\det \B = 4 \cdot 2 = 8 \). The next theorem explains part of that: it forces \( \det(\A \circ \B) \ge \det\A \prod_i b_{ii} = 24 \). Getting down to the product \( \det\A\det\B \) needs Hadamard's inequality as well, which is @exr-schur-product-theorem-c2.
:::

::: {.check}
Let \( \A = \begin{psmallmatrix} 1 & 1 \\ 1 & 1\end{psmallmatrix} \) and \( \B = \begin{psmallmatrix} 2 & -1 \\ -1 & 2\end{psmallmatrix} \). Compute \( \A \circ \B \) and decide whether it is positive definite. Does this contradict @thm-schur-product (b)?
:::

::: {.solution}
\( \A \circ \B = \begin{psmallmatrix} 2 & -1 \\ -1 & 2\end{psmallmatrix} \), with leading principal minors \( 2 \) and \( 3 \), so it is positive definite. There is no contradiction: @thm-schur-product (b) is an implication, not an equivalence. Here \( \A \) is only positive semidefinite (\( \A = \1\1\tp \), so \( \det \A = 0 \)), and the theorem's hypothesis fails — but the conclusion happens to hold anyway. Part (a) is what applies, and it correctly predicts \( \A \circ \B \succeq 0 \).
:::

## Oppenheim's inequality

Hadamard's inequality of Section 6 compared \( \det \A \) with the product of the diagonal entries of \( \A \). Oppenheim's inequality does the same for a Hadamard product, and it contains Hadamard's as the special case \( \B = \I \).

::: {#thm-oppenheim}
[Oppenheim's Inequality]

Let \( \A, \B \in M_n(F) \) with \( \A \succeq 0 \) and \( \B \succeq 0 \). Then

\[
\det(\A \circ \B) \ \ge \ \det \A \cdot b_{11}b_{22}\cdots b_{nn} .
\]
:::

::: {.idea}
Induct on \( n \), taking both matrices positive definite first. Split off the \( (1,1) \) entry of each: the Schur complements \( \A/\alpha \) and \( \B/\beta \) are positive definite of size \( n - 1 \), and a short computation, whose only real step is @lem-hadamard-rank-one again, shows that the Schur complement of the corner in \( \A \circ \B \) is

\[
(\A \circ \B)/(\alpha\beta) = (\A/\alpha) \circ \B' + \tfrac1\alpha\,(\a\a^{*}) \circ (\B/\beta) ,
\]

a positive definite matrix plus a positive semidefinite one. So its determinant is at least that of the first term, by @lem-det-psd-increment, and the inductive hypothesis handles that. The semidefinite case follows by replacing \( \A \) and \( \B \) with \( \A + t\I \) and \( \B + t\I \) and letting \( t \) shrink to \( 0 \).
:::

::: {.proof}
*Case 1: \( \A \succ 0 \) and \( \B \succ 0 \).* Induct on \( n \). For \( n = 1 \) both sides are \( a_{11}b_{11} \).

Let \( n \ge 2 \), and split both matrices with a \( 1 \times (n-1) \) partition:

\[
\A = \begin{pmatrix} \alpha & \a^{*} \\ \a & \A' \end{pmatrix},
\qquad
\B = \begin{pmatrix} \beta & \b^{*} \\ \b & \B' \end{pmatrix},
\]

with \( \alpha = a_{11} > 0 \), \( \beta = b_{11} > 0 \) and \( \a, \b \in F^{n-1} \). The Schur complements are

\[
\A/\alpha = \A' - \tfrac1\alpha\,\a\a^{*}, \qquad \B/\beta = \B' - \tfrac1\beta\,\b\b^{*} ,
\]

and both are positive definite by @thm-block-psd-schur (b). Since conjugation acts entrywise, \( \a^{*} \circ \b^{*} = (\a \circ \b)^{*} \), so

\[
\A \circ \B = \begin{pmatrix} \alpha\beta & (\a \circ \b)^{*} \\ \a \circ \b & \A' \circ \B' \end{pmatrix} ,
\]

and \( \alpha\beta > 0 \), so this matrix too has a Schur complement at its corner:

\[
(\A \circ \B)/(\alpha\beta) = \A' \circ \B' - \tfrac1{\alpha\beta}\,(\a \circ \b)(\a \circ \b)^{*} .
\]

By @lem-hadamard-rank-one the subtracted term is \( \tfrac1{\alpha\beta}(\a\a^{*}) \circ (\b\b^{*}) \). Substituting \( \A' = \A/\alpha + \tfrac1\alpha\a\a^{*} \) and expanding by bilinearity,

\[
\begin{aligned}
\A' \circ \B' &= (\A/\alpha) \circ \B' + \tfrac1\alpha\,(\a\a^{*}) \circ \B' \\
 &= (\A/\alpha) \circ \B' + \tfrac1\alpha\,(\a\a^{*}) \circ \Bigl(\B/\beta + \tfrac1\beta\b\b^{*}\Bigr) ,
\end{aligned}
\]

and the last term of this is exactly \( \tfrac1{\alpha\beta}(\a\a^{*}) \circ (\b\b^{*}) \). It therefore cancels, leaving

\[
(\A \circ \B)/(\alpha\beta) = \underbrace{(\A/\alpha) \circ \B'}_{\textstyle \succ 0} \;+\; \underbrace{\tfrac1\alpha\,(\a\a^{*}) \circ (\B/\beta)}_{\textstyle \succeq 0} . \tag{$\ast$}
\]

The first term is positive definite by @thm-schur-product (b), since \( \A/\alpha \succ 0 \) and \( \B' \succ 0 \) (the latter by @thm-block-psd-schur (a) applied to \( \B \)). The second is positive semidefinite by @thm-schur-product (a), since \( \a\a^{*} \succeq 0 \) by @exm-psd-first-examples (b) and \( \B/\beta \succ 0 \), and \( 1/\alpha > 0 \).

Now compute. By @thm-schur-determinant applied to \( \A \circ \B \), then \( (\ast) \) with @lem-det-psd-increment, then the inductive hypothesis applied to the pair \( \A/\alpha \) and \( \B' \):

\[
\begin{aligned}
\det(\A \circ \B) &= \alpha\beta\cdot\det\bigl[(\A \circ \B)/(\alpha\beta)\bigr] \\
 &\ge \alpha\beta\cdot\det\bigl[(\A/\alpha) \circ \B'\bigr] \\
 &\ge \alpha\beta\cdot\det(\A/\alpha)\cdot b_{22}\cdots b_{nn} .
\end{aligned}
\]

By @thm-schur-determinant again, now for \( \A \), we have \( \det(\A/\alpha) = \det \A/\alpha \). Substituting and canceling \( \alpha \),

\[
\det(\A \circ \B) \ \ge \ \beta\,\det \A\cdot b_{22}\cdots b_{nn} = \det \A\cdot b_{11}b_{22}\cdots b_{nn} ,
\]

which completes the induction.

*Case 2: \( \A \succeq 0 \) and \( \B \succeq 0 \).* For real \( t > 0 \), the matrices \( \A + t\I \) and \( \B + t\I \) are positive definite, as in the proof of @cor-fischer-inequality. Case 1 gives

\[
\det\bigl[(\A + t\I) \circ (\B + t\I)\bigr] \ \ge \ \det(\A + t\I)\cdot\prod_{i=1}^{n}(b_{ii} + t) .
\]

Every entry of \( (\A + t\I) \circ (\B + t\I) \) is a polynomial in \( t \), so both sides are polynomial, hence continuous, functions of \( t \) (@thm-leibniz-formula-alternating). Letting \( t \) decrease to \( 0 \) preserves the inequality and gives the statement. This proves the theorem.
:::

::: {.remark}
Taking \( \B = \I \) recovers Hadamard's inequality. Indeed \( \A \circ \I = \diag(a_{11}, \dots, a_{nn}) \) and \( \prod_i b_{ii} = 1 \), so the conclusion reads \( a_{11}\cdots a_{nn} \ge \det \A \), which is @thm-hadamard-inequality (a). Swapping the roles of \( \A \) and \( \B \) gives the companion bound \( \det(\A \circ \B) \ge \det \B\cdot\prod_i a_{ii} \), and combining either one with Hadamard's inequality gives \( \det(\A \circ \B) \ge \det \A\det \B \); that last consequence is @exr-schur-product-theorem-c2.
:::

## Where this gets used

The natural home of the Hadamard product is data. A covariance matrix is a Gram matrix (@thm-gram-matrix-properties), hence positive semidefinite, and rescaling each variable to unit variance turns it into a **correlation matrix**: positive semidefinite with every diagonal entry equal to \( 1 \). The Schur product theorem says that the entrywise product of two correlation matrices is another one — the diagonal entries stay \( 1 \cdot 1 = 1 \) — so one can damp the correlations of one model by those of another and still have a legitimate covariance structure. Nothing in the definition of "positive semidefinite" makes that obvious, and it is the reason the theorem is quoted far outside linear algebra.

::: {.warning}
**Entrywise products preserve positivity; entrywise inverses do not.** Let \( \A = \begin{psmallmatrix} 2 & 1 \\ 1 & 2\end{psmallmatrix} \), which is positive definite, with leading principal minors \( 2 \) and \( 3 \). Replacing each entry by its reciprocal gives \( \begin{psmallmatrix} 1/2 & 1 \\ 1 & 1/2\end{psmallmatrix} \), whose determinant is \( \tfrac14 - 1 = -\tfrac34 < 0 \): not positive semidefinite. The entrywise reciprocal is not the Hadamard inverse of anything useful, and the matrix inverse \( \A^{-1} \), which **is** positive definite (@exr-positive-definite-matrices-b3), has nothing to do with it.
:::

## Exercises

### A. Check your understanding

:::: {#exr-schur-product-theorem-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define \( \A \circ \B \), and say what shapes the two factors must have.
2. What is \( \A \circ \I \)? What is \( \A \circ \J \)?
3. State the Schur product theorem.
4. True or false: if \( \A \succ 0 \), then the matrix with entries \( 1/a_{ij} \) (assuming no entry is \( 0 \)) is positive definite. Justify your answer.
5. What does Oppenheim's inequality say when \( \B = \I \)?
:::
::::

::: {.solution}
(a) For \( \A, \B \in M_{m\times n}(F) \) of the **same** shape, \( (\A \circ \B)_{ij} = a_{ij}b_{ij} \), and \( \A \circ \B \) has that same shape (@def-hadamard-product).

(b) \( \A \circ \I = \diag(a_{11}, \dots, a_{nn}) \), and \( \A \circ \J = \A \), since \( \J \) has every entry \( 1 \).

(c) If \( \A \succeq 0 \) and \( \B \succeq 0 \), then \( \A \circ \B \succeq 0 \); if both are positive definite, so is \( \A \circ \B \) (@thm-schur-product).

(d) False. For \( \A = \begin{psmallmatrix} 2 & 1 \\ 1 & 2\end{psmallmatrix} \succ 0 \), the entrywise reciprocal is \( \begin{psmallmatrix} 1/2 & 1 \\ 1 & 1/2\end{psmallmatrix} \), with determinant \( -3/4 < 0 \).

(e) By @thm-oppenheim it says \( \det(\A \circ \I) \ge \det \A \cdot 1 \), that is \( a_{11}\cdots a_{nn} \ge \det \A \): Hadamard's inequality, @thm-hadamard-inequality (a).
:::

### B. Practice

:::: {#exr-schur-product-theorem-b1}
[B1: Compute and decide]

For each pair below, compute \( \A \circ \B \) and determine whether it is positive definite, positive semidefinite but not definite, or neither. Say in each case whether @thm-schur-product applies.

::: {.enumerate options="label=(\alph*)"}
1. \( \A = \begin{psmallmatrix} 1 & 1 \\ 1 & 1\end{psmallmatrix} \), \( \B = \begin{psmallmatrix} 1 & 1 \\ 1 & 1\end{psmallmatrix} \).
2. \( \A = \begin{psmallmatrix} 1 & 1 \\ 1 & 1\end{psmallmatrix} \), \( \B = \begin{psmallmatrix} 1 & 2 \\ 2 & 1\end{psmallmatrix} \).
3. \( \A = \begin{psmallmatrix} 2 & 1 \\ 1 & 2\end{psmallmatrix} \), \( \B = \begin{psmallmatrix} 3 & -1 \\ -1 & 1\end{psmallmatrix} \).
:::
::::

::: {.solution}
(a) \( \A \circ \B = \begin{psmallmatrix} 1 & 1 \\ 1 & 1\end{psmallmatrix} \). Both factors are \( \1\1\tp \succeq 0 \) (@exm-psd-first-examples (b)), so @thm-schur-product (a) applies and predicts \( \succeq 0 \). The product has determinant \( 0 \), so it is positive semidefinite but not definite.

(b) \( \A \circ \B = \begin{psmallmatrix} 1 & 2 \\ 2 & 1\end{psmallmatrix} \), whose determinant is \( 1 - 4 = -3 < 0 \): neither. The theorem does not apply, since \( \B \) is not positive semidefinite (its determinant is \( -3 \)). This is what the hypothesis is for.

(c) \( \A \succ 0 \) (minors \( 2 \), \( 3 \)) and \( \B \succ 0 \) (minors \( 3 \), \( 2 \)), so @thm-schur-product (b) applies. Indeed \( \A \circ \B = \begin{psmallmatrix} 6 & -1 \\ -1 & 2\end{psmallmatrix} \), with minors \( 6 \) and \( 11 \), is positive definite. @thm-oppenheim also checks out: \( 11 \ge \det \A\cdot b_{11}b_{22} = 3 \cdot 3 = 9 \).
:::

:::: {#exr-schur-product-theorem-b2}
[B2: Entrywise squares]

Let \( \A = \begin{psmallmatrix} 1 & 1 & 1 \\ 1 & 2 & 2 \\ 1 & 2 & 3\end{psmallmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \A \succ 0 \).
2. Compute \( \A \circ \A \), the matrix of squared entries, and verify that it is positive definite.
3. Explain why (b) needed no computation.
:::
::::

::: {.solution}
(a) The leading principal minors are \( 1 \), \( 2 - 1 = 1 \) and, expanding along the first row, \( 1(6-4) - 1(3-2) + 1(2-2) = 1 \). All positive, so \( \A \succ 0 \) by @thm-pd-characterizations (d).

(b) \( \A \circ \A = \begin{psmallmatrix} 1 & 1 & 1 \\ 1 & 4 & 4 \\ 1 & 4 & 9\end{psmallmatrix} \), with leading principal minors \( 1 \), \( 4 - 1 = 3 \) and \( 1(36 - 16) - 1(9 - 4) + 1(4 - 4) = 20 - 5 = 15 \). All positive, so it is positive definite.

(c) @thm-schur-product (b) with \( \B = \A \) gives \( \A \circ \A \succ 0 \) immediately.
:::

### C. Going deeper

:::: {#exr-schur-product-theorem-c1}
[C1: Polynomials applied entrywise]

Let \( \A \in M_n(F) \) with \( \A \succeq 0 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that the entrywise power \( \A^{\circ m} \), with \( (i, j) \) entry \( a_{ij}^{\,m} \), is positive semidefinite for every integer \( m \ge 1 \).
2. Let \( p(x) = c_0 + c_1x + \dots + c_dx^d \) have **non-negative real** coefficients. Prove that the matrix \( p^{\circ}(\A) \) with \( (i, j) \) entry \( p(a_{ij}) \) is positive semidefinite.
3. Give an example of \( \A \succeq 0 \) and a polynomial \( p \) with a negative coefficient for which \( p^{\circ}(\A) \) is not positive semidefinite.
:::
::::

::: {.solution}
(a) Induct on \( m \). For \( m = 1 \) the claim is the hypothesis. If \( \A^{\circ m} \succeq 0 \), then \( \A^{\circ(m+1)} = \A^{\circ m} \circ \A \succeq 0 \) by @thm-schur-product (a).

(b) By definition of the entries, \( p^{\circ}(\A) = c_0\J + c_1\A + c_2\A^{\circ 2} + \dots + c_d\A^{\circ d} \), since each side has \( (i, j) \) entry \( \sum_k c_ka_{ij}^{\,k} \) (with \( a_{ij}^0 = 1 \), which is the \( (i,j) \) entry of \( \J \)). Now \( \J = \1\1\tp \succeq 0 \) by @exm-psd-first-examples (b), each \( \A^{\circ k} \succeq 0 \) by (a), and each \( c_k \ge 0 \). A non-negative combination of positive semidefinite matrices is positive semidefinite (@exr-positive-definite-matrices-c2 (a)).

(c) Take \( \A = \J \in M_2(\nR) \), which is positive semidefinite, and \( p(x) = x - 2 \). Then \( p^{\circ}(\A) \) has every entry \( -1 \), that is \( p^{\circ}(\A) = -\J \), and \( \inner{-\J\e_1}{\e_1} = -1 < 0 \). So the hypothesis on the coefficients cannot be dropped.
:::

:::: {#exr-schur-product-theorem-c2}
[C2: The product of the determinants]

Let \( \A, \B \in M_n(F) \) with \( \A \succeq 0 \) and \( \B \succeq 0 \). Prove that

\[
\det(\A \circ \B) \ \ge \ \det \A \cdot \det \B .
\]

Is the inequality ever an equality with both matrices positive definite?
::::

::: {.solution}
By @thm-oppenheim, \( \det(\A \circ \B) \ge \det \A\cdot\prod_i b_{ii} \). By @thm-hadamard-inequality (a) applied to \( \B \succeq 0 \), \( \prod_i b_{ii} \ge \det \B \). Both \( \det \A \ge 0 \) and \( \prod_i b_{ii} \ge 0 \) (the diagonal entries of a positive semidefinite matrix are \( \ge 0 \) by @exr-positive-definite-matrices-c1 (a)), so multiplying the second inequality by \( \det \A \ge 0 \) and chaining,

\[
\det(\A \circ \B) \ \ge\ \det \A\prod_i b_{ii} \ \ge\ \det \A\det \B .
\]

Yes, equality can occur: take \( \A = \B = \I_n \), so that \( \A \circ \B = \I_n \) and all three quantities are \( 1 \). More generally, take \( \A \succ 0 \) diagonal and \( \B = \I_n \).
:::

:::: {#exr-schur-product-theorem-c3}
[C3: The rank of an entrywise product]

Let \( \A, \B \in M_n(F) \) with \( \A \succeq 0 \) and \( \B \succeq 0 \), of ranks \( r \) and \( s \). Prove that

\[
\rank(\A \circ \B) \le rs .
\]

*Hint: how many terms in the proof of @thm-schur-product (a) are actually non-zero?*
::::

::: {.solution}
Write \( \A = \sum_i\lambda_i\u_i\u_i^{*} \) and \( \B = \sum_j\mu_j\w_j\w_j^{*} \) as in the proof of @thm-schur-product (a). The number of non-zero eigenvalues of \( \A \) is \( \rank \A = r \): diagonalizing, \( \A = \U\D\U^{*} \) with \( \U \) invertible, so \( \rank \A = \rank \D \) by @thm-rank-product-inequality, and \( \rank \D \) counts the non-zero \( \lambda_i \). Likewise exactly \( s \) of the \( \mu_j \) are non-zero. Dropping the vanishing terms,

\[
\A \circ \B = \sum_{\lambda_i \ne 0}\ \sum_{\mu_j \ne 0} \lambda_i\mu_j\,\z_{ij}\z_{ij}^{*}, \qquad \z_{ij} = \u_i \circ \w_j ,
\]

a sum of \( rs \) matrices, each of rank at most \( 1 \), since every column of \( \z_{ij}\z_{ij}^{*} \) lies in \( \Span(\z_{ij}) \). The rank of a sum of two matrices is at most the sum of their ranks (@exr-rank-c1); applying that repeatedly to the \( rs \) summands gives \( \rank(\A \circ \B) \le rs \).
:::
