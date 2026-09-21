# Lax Pairs and the Toda Flow

The QR algorithm of Section 5 is a sequence \( \A^{(1)}, \A^{(2)}, \A^{(3)}, \dots \) of matrices, each similar to the last, drifting towards triangular form. Nothing in it looks like a differential equation. This section shows that it is one: there is a curve \( \L(t) \) of matrices, all with the same eigenvalues, that passes through the QR iterates at the integer times. The bridge is a class of matrix differential equations whose solutions cannot change their spectrum, and the proof that they cannot is a page of pure algebra. It is the one place in the chapter where nothing is computed and nothing is rounded.

Throughout, \( I \subseteq \nR \) is an open interval and matrix-valued functions of \( t \in I \) are differentiated entrywise, as in @def-matrix-valued-derivative. **In this section the letter \( \L \) names the matrix being flowed**, following the universal notation for it; the graph Laplacian of Section 11 carries the same symbol and never appears here.

## Which matrix differential equations preserve the spectrum?

Start from the answer we want and read the equation off it. Suppose \( \L(t) \) is a curve of matrices, all similar to \( \L(0) \) by a similarity that also moves with \( t \):
\[
\L(t) = \S(t)\,\L(0)\,\S(t)^{-1},
\]
with \( \S \colon I \to M_n(\nC) \) differentiable and everywhere invertible. Differentiate. By the product rule (@lem-matrix-product-rule) and the derivative of the inverse (@thm-derivative-of-inverse),
\[
\begin{aligned}
\L' &= \S'\L(0)\S^{-1} - \S\L(0)\S^{-1}\S'\S^{-1}\\
&= (\S'\S^{-1})\L - \L(\S'\S^{-1}) ,
\end{aligned}
\]
where the second line inserts \( \S^{-1}\S = \I \) in the first term and recognizes \( \S\L(0)\S^{-1} = \L \) in both. So with \( \B = \S'\S^{-1} \) the curve satisfies \( \L' = \B\L - \L\B \). The commutator is not a clever choice: it is what a moving similarity is *forced* to satisfy.

*A Lax pair is a matrix that moves, together with the infinitesimal similarity that moves it.*

::: {#def-lax-pair}
[Lax Pair]

Let \( I \subseteq \nR \) be an open interval. A **Lax pair** on \( I \) is a pair of functions \( \L, \B \colon I \to M_n(\nC) \), with \( \L \) differentiable, such that
\[
\L'(t) = [\B(t), \L(t)] \coloneqq \B(t)\L(t) - \L(t)\B(t)
\qquad \text{for every } t \in I .
\]
The equation itself is called a **Lax equation**, and \( \L \) is said to **flow** under it.
:::

Clause by clause. The two matrices are **square of the same size \( n \)**, or the bracket is not defined. Only \( \L \) is required to be **differentiable**; \( \B \) may be any function of \( t \) whatsoever, and in the interesting cases it is built out of \( \L(t) \) itself, which makes the equation non-linear. The bracket \( [\B, \L] \) is the commutator of the notation list, and the **order matters**: \( [\L, \B] = -[\B, \L] \), so swapping the two letters runs the flow backwards.

**Examples.**

1. **\( \B = 0 \).** Then \( \L' = 0 \), so \( \L \) is constant. The degenerate case, and it matters: it is the sanity check that the definition does not force motion.
2. **Constant \( \B \).** Put \( \L(t) = e^{t\B}\L_0e^{-t\B} \) for a fixed \( \L_0 \). By @thm-exponential-properties (b) and @lem-matrix-product-rule,
\[
\L'(t) = \B e^{t\B}\L_0e^{-t\B} + e^{t\B}\L_0(-\B e^{-t\B}) = \B\L - \L\B ,
\]
the last step because \( \B \) commutes with \( e^{\pm t\B} \), again by @thm-exponential-properties (b). So \( (\L, \B) \) is a Lax pair on all of \( \nR \). @cor-lax-constant-coefficient below says these are the only solutions when \( \B \) is constant.

A third example is worth a block of its own, because it is the one to hold in mind.

::: {#exm-lax-nilpotent-curve}
[A curve of matrices with a frozen spectrum]

Take \( \B = \begin{psmallmatrix} 0 & 1 \\ 0 & 0\end{psmallmatrix} \) and \( \L_0 = \begin{psmallmatrix} 0 & 0 \\ 1 & 0\end{psmallmatrix} \). Since \( \B^2 = 0 \), @def-matrix-exponential gives \( e^{t\B} = \I + t\B \), and the recipe of the previous example produces
\[
\L(t) = \begin{pmatrix} 1 & t \\ 0 & 1\end{pmatrix}\begin{pmatrix} 0 & 0 \\ 1 & 0\end{pmatrix}\begin{pmatrix} 1 & -t \\ 0 & 1\end{pmatrix}
= \begin{pmatrix} t & -t^2 \\ 1 & -t\end{pmatrix} .
\]
Three of the four entries move — only the corner \( \ell_{21} = 1 \) stands still — and yet \( \tr\L(t) = 0 \) and \( \det\L(t) = -t^2 + t^2 = 0 \), so \( p_{\L(t)}(x) = x^2 \) for every \( t \). The curve stays inside one similarity class the whole time.
:::

**A non-example, by dropping the second term.** Replace the Lax equation by \( \L' = \B\L \) with \( \B = \I \). The unique solution with \( \L(0) = \L_0 \) is \( \L(t) = e^{t}\L_0 \) (@thm-linear-ode-solution, applied to each column). Its eigenvalues are \( e^{t}\lambda_i \), which move. What was lost is precisely the second term: \( \B\L \) alone is not a commutator, and a commutator is what the differentiation of a similarity produced.

::: {.warning}
**Isospectral does not mean constant.** In @exm-lax-nilpotent-curve the matrix \( \L(t) \) changes at every instant; what stays put is its list of eigenvalues. The eigen*vectors* move, and they must, since they are the columns of \( \S(t) \) up to scale. A flow that fixed the eigenvectors as well would fix \( \L \). The whole use of a Lax pair — in Section 5's language, in this section's, and in the theory of integrable systems generally — is that something moves while something else does not.
:::

## The isospectral theorem

The derivation above suggests the proof: manufacture \( \S(t) \) and conclude by similarity. That route runs into an obstacle the book cannot clear. The natural \( \S \) is the solution of \( \S' = \B\S \), \( \S(t_0) = \I \), and for a **constant** \( \B \) that is \( e^{(t-t_0)\B} \) by Chapter 9 §09. For a \( \B \) that depends on \( t \) — the only case of interest here — the existence of such an \( \S \) is a theorem about linear differential equations with variable coefficients, and this book does not prove it. So we take a different route, which needs no flow at all.

::: {#thm-lax-isospectral}
[Lax Pairs Are Isospectral]

Let \( (\L, \B) \) be a Lax pair on an open interval \( I \). Then the characteristic polynomial of \( \L(t) \) does not depend on \( t \):
\[
p_{\L(t)} = p_{\L(s)} \qquad \text{for all } s, t \in I .
\]
In particular \( \L(t) \) has the same eigenvalues as \( \L(s) \), with the same algebraic multiplicities, and \( \tr\L(t) \) and \( \det\L(t) \) are constant.
:::

::: {.idea}
Freeze \( x \in \nC \) and watch the single number \( f(t) = \det(x\I - \L(t)) \). Jacobi's formula turns its derivative into a trace against the adjugate, and the adjugate is the one matrix that turns \( \M \) into the scalar \( \det\M \) from either side. Writing the bracket in terms of \( \M = x\I - \L \) rather than \( \L \) — which is legitimate, because \( x\I \) commutes with everything — makes the two halves of the trace cancel, because a trace is unchanged by a cyclic shift. So \( f' \equiv 0 \), and a polynomial identity valid for every \( x \) is an identity of polynomials.
:::

::: {.proof}
Fix \( x \in \nC \) and put \( \M(t) = x\I - \L(t) \), which is differentiable with \( \M'(t) = -\L'(t) \) (@def-matrix-valued-derivative). Let
\[
f(t) = \det\M(t) = p_{\L(t)}(x) .
\]
By Jacobi's formula (@thm-derivative-of-det), \( f \) is differentiable on \( I \) with
\[
f'(t) = \tr\bigl(\adj\M(t)\,\M'(t)\bigr).
\]

Rewrite the bracket in terms of \( \M \). Since \( \L = x\I - \M \) and \( x\I \) commutes with \( \B \),
\[
[\B, \L] = \B(x\I - \M) - (x\I - \M)\B = \M\B - \B\M ,
\]
so \( \M' = -\L' = -[\B, \L] = \B\M - \M\B \). Writing \( \M = \M(t) \) and using the linearity of the trace (@thm-trace-properties (a)),
\[
f'(t) = \tr\bigl(\adj\M\,\B\M\bigr) - \tr\bigl(\adj\M\,\M\B\bigr).
\]
A cyclic shift (@thm-trace-properties (c)) moves \( \M \) to the front of the first trace, so
\[
f'(t) = \tr\bigl(\M\,\adj\M\,\B\bigr) - \tr\bigl(\adj\M\,\M\,\B\bigr).
\]
By @thm-adjugate-identity, \( \M\adj\M = \adj\M\,\M = (\det\M)\I \), so the two traces are the same number and \( f'(t) = 0 \) for every \( t \in I \).

A differentiable function on an interval with vanishing derivative is constant — the mean value theorem, fact (A6) of Chapter 15's introduction, applied to the real and imaginary parts of \( f \). (Chapter 9 §09's fact (A4) says this for functions defined on all of \( \nR \), which is not the hypothesis here.) So \( p_{\L(t)}(x) = p_{\L(s)}(x) \) for all \( s, t \in I \).

Finally, \( x \in \nC \) was arbitrary, so the two polynomials \( p_{\L(t)} \) and \( p_{\L(s)} \) define the same function \( \nC \to \nC \); since \( \nC \) is infinite, @thm-polynomial-function-determines-polynomial (b) gives \( p_{\L(t)} = p_{\L(s)} \) as polynomials. The eigenvalues are their roots and the multiplicities the multiplicities of those roots, and \( \tr \) and \( \det \) are two of the coefficients up to sign (@thm-charpoly-coefficients). This proves the theorem.
:::

::: {.remark}
**What the proof did not need.** It never produced the similarity \( \S(t) \), never solved a differential equation, and never used any property of \( \B \) — not continuity, and not differentiability. The only analytic ingredients are two: (D1), the differentiation package Chapter 15 §06 quoted, which is what Jacobi's formula rests on, and the mean value theorem (A6) of Chapter 15's introduction, in the form "zero derivative on an interval implies constant". Everything else is the adjugate identity and the invariance of the trace under a cyclic shift.
:::

When \( \B \) *is* constant, the similarity is available and the theorem can be sharpened: the flow is completely determined.

::: {#cor-lax-constant-coefficient}
[Constant \( \B \): the flow is conjugation by the exponential]

Let \( \B \in M_n(\nC) \) be a fixed matrix and let \( \L \colon \nR \to M_n(\nC) \) be differentiable with \( \L' = [\B, \L] \). Then
\[
\L(t) = e^{t\B}\,\L(0)\,e^{-t\B} \qquad (t \in \nR),
\]
so \( \L(t) \) is similar to \( \L(0) \) for every \( t \).
:::

::: {.proof}
Put \( \M(t) = e^{-t\B}\L(t)e^{t\B} \), a product of three differentiable matrix functions. By @lem-matrix-product-rule and @thm-exponential-properties (b), which also gives \( \B e^{\pm t\B} = e^{\pm t\B}\B \),
\[
\begin{aligned}
\M'(t) &= -\B e^{-t\B}\L e^{t\B} + e^{-t\B}\L' e^{t\B} + e^{-t\B}\L\B e^{t\B}\\
&= e^{-t\B}\bigl(-\B\L + (\B\L - \L\B) + \L\B\bigr)e^{t\B} = 0 .
\end{aligned}
\]
By fact (A4) of Chapter 9 §09, every entry of \( \M \) is constant, so \( \M(t) = \M(0) = \L(0) \). Multiplying on the left by \( e^{t\B} \) and on the right by \( e^{-t\B} \), and using \( (e^{t\B})^{-1} = e^{-t\B} \) from @thm-exponential-properties (c), gives the formula. This proves the corollary.
:::

::: {.check}
Prove directly from the Lax equation, without @thm-lax-isospectral, that \( \tr\L(t) \) is constant.
:::

::: {.solution}
The trace of a matrix is a linear function of its entries, so \( (\tr\L)'(t) = \tr(\L'(t)) \) by (D1) and @thm-trace-properties (a). Then
\[
\tr\L'(t) = \tr(\B\L) - \tr(\L\B) = 0
\]
by @thm-trace-properties (c). So \( \tr\L \) has zero derivative on \( I \) and is constant by fact (A6) of Chapter 15's introduction. The same argument applied to \( \L^m \) gives \( \tr(\L^m)' = 0 \) for every \( m \ge 1 \) (@exr-lax-pairs-and-the-toda-flow-c1).
:::

## The Toda flow

Now for the flow that matters. Take \( \L \) real symmetric and tridiagonal, and take \( \B \) to be the skew-symmetric matrix built from the off-diagonal entries of \( \L \). There are two sign conventions, differing by \( \B \mapsto -\B \) and so running the flow in opposite directions; we fix the one that drives the largest eigenvalue towards the top-left corner, as @exm-toda-two-by-two will confirm.

::: {#def-toda-flow}
[The Toda Flow]

For \( \M \in M_n(\nR) \) write \( \M_{+} \) for its **strictly upper triangular part** and \( \M_{-} \) for its **strictly lower triangular part**, so that \( \M \) is the sum of \( \M_{-} \), its diagonal part and \( \M_{+} \), and set
\[
\B(\M) \coloneqq \M_{+} - \M_{-} .
\]
The **Toda flow** is the Lax equation
\[
\L'(t) = \bigl[\B(\L(t)),\ \L(t)\bigr]
\]
for a differentiable \( \L \colon I \to M_n(\nR) \) taking symmetric tridiagonal values.
:::

Two clauses need checking. First, \( \B(\M) \) is **skew-symmetric** when \( \M \) is symmetric: transposing turns the strictly upper part into the strictly lower part of \( \M\tp = \M \), so \( \B(\M)\tp = \M_{-} - \M_{+} = -\B(\M) \). Second, the equation is **non-linear**: \( \B \) depends on \( \L \), and the right-hand side is quadratic in the entries of \( \L \). That is what makes it a genuine dynamical system rather than a rewriting of @cor-lax-constant-coefficient.

Writing the equation out shows what it does.

::: {#prp-toda-equations}
[The Toda Flow in Coordinates]

Let \( \L \in M_n(\nR) \) be symmetric and tridiagonal, with diagonal entries \( d_1, \dots, d_n \) and off-diagonal entries \( e_1, \dots, e_{n-1} \), so \( \ell_{i,i+1} = \ell_{i+1,i} = e_i \). Put \( e_0 = e_n = 0 \). Then \( [\B(\L), \L] \) is again symmetric and tridiagonal, with
\[
\bigl[\B(\L), \L\bigr]_{ii} = 2\bigl(e_i^2 - e_{i-1}^2\bigr),
\qquad
\bigl[\B(\L), \L\bigr]_{i,i+1} = e_i\,(d_{i+1} - d_i) .
\]
Consequently the Toda flow is the system
\[
d_i' = 2\bigl(e_i^2 - e_{i-1}^2\bigr) \ \ (1 \le i \le n),
\qquad
e_i' = e_i\,(d_{i+1} - d_i) \ \ (1 \le i \le n-1) .
\]{#eq-toda-coordinates}
:::

::: {.proof}
Write \( \B = \B(\L) \), so that \( b_{i,i+1} = e_i \), \( b_{i+1,i} = -e_i \), and every other entry of \( \B \) is \( 0 \). Then for all \( i, j \),
\[
(\B\L)_{ij} = e_i\,\ell_{i+1,j} - e_{i-1}\,\ell_{i-1,j},
\qquad
(\L\B)_{ij} = e_{j-1}\,\ell_{i,j-1} - e_{j}\,\ell_{i,j+1},
\]
with the convention that a term with an index outside \( 1, \dots, n \) is \( 0 \); this is just the two non-zero entries in row \( i \) of \( \B \), respectively in column \( j \) of \( \B \). Write \( \C = \B\L - \L\B \), so
\[
c_{ij} = e_i\ell_{i+1,j} - e_{i-1}\ell_{i-1,j} - e_{j-1}\ell_{i,j-1} + e_{j}\ell_{i,j+1} .
\tag{$\ast$}
\]

\( \C \) is symmetric: since \( \B\tp = -\B \) and \( \L\tp = \L \),
\[
\C\tp = \L\tp\B\tp - \B\tp\L\tp = -\L\B + \B\L = \C ,
\]
so it is enough to compute \( c_{ij} \) for \( j \ge i \).

*Case \( j = i \).* Every \( \ell \) appearing in \( (\ast) \) is then an off-diagonal neighbor: \( \ell_{i+1,i} = e_i \), \( \ell_{i-1,i} = e_{i-1} \), \( \ell_{i,i-1} = e_{i-1} \), \( \ell_{i,i+1} = e_i \). So
\[
c_{ii} = e_i^2 - e_{i-1}^2 - e_{i-1}^2 + e_i^2 = 2(e_i^2 - e_{i-1}^2).
\]

*Case \( j = i+1 \).* Now \( \ell_{i+1,i+1} = d_{i+1} \) and \( \ell_{i,i} = d_i \), while \( \ell_{i-1,i+1} = 0 \) and \( \ell_{i,i+2} = 0 \) because \( \L \) is tridiagonal. So \( c_{i,i+1} = e_i d_{i+1} - e_i d_i \).

*Case \( j = i+2 \).* Here \( \ell_{i+1,i+2} = e_{i+1} \) and \( \ell_{i,i+1} = e_i \), while \( \ell_{i-1,i+2} = \ell_{i,i+3} = 0 \). So
\[
c_{i,i+2} = e_ie_{i+1} - 0 - e_{i+1}e_i + 0 = 0 .
\]

*Case \( j \ge i+3 \).* Each of the four entries \( \ell_{i+1,j} \), \( \ell_{i-1,j} \), \( \ell_{i,j-1} \), \( \ell_{i,j+1} \) has its two indices differing by at least \( 2 \), so all four are \( 0 \) and \( c_{ij} = 0 \).

Hence \( \C \) is symmetric tridiagonal with the stated entries, and equating \( \L' \) with \( \C \) entry by entry gives @eq-toda-coordinates. This proves the proposition.
:::

Read @eq-toda-coordinates for what it is. The off-diagonal entries feed the diagonal — mass \( e_i^2 \) flows from \( d_{i+1} \) up to \( d_i \) — and the diagonal drives the off-diagonal, each \( e_i \) growing or shrinking according to the sign of \( d_{i+1} - d_i \). Summing the first family gives \( \sum_i d_i' = 0 \), the constancy of the trace, with the terms canceling in pairs. And an \( e_i \) that vanishes at some time has \( e_i' = 0 \) at that same time. It is tempting to read off that such an \( e_i \) stays \( 0 \) for ever — that the flow never re-couples two blocks which have already separated, the continuous shadow of deflation in Section 5 — but that is a statement about the *solutions* of the system, and getting it from the instantaneous one needs a uniqueness theorem for differential equations of the sort this section declined to assume above. Only the instantaneous statement is claimed here.

::: {#exm-toda-two-by-two}
[The \( 2 \times 2 \) flow, twice]

Let \( n = 2 \), so \( \L = \begin{psmallmatrix} d_1 & e_1 \\ e_1 & d_2\end{psmallmatrix} \) and @eq-toda-coordinates reads
\[
d_1' = 2e_1^2, \qquad d_2' = -2e_1^2, \qquad e_1' = e_1(d_2 - d_1) .
\]

::: {.enumerate options="label=(\alph*)"}
1. Verify by hand that \( \tr\L \) and \( \det\L \) are constant along the flow.
2. Solve the flow explicitly for \( \L(0) = \begin{psmallmatrix} 0 & 1 \\ 1 & 0\end{psmallmatrix} \).
:::
:::

::: {.solution}
(a) \( (\tr\L)' = d_1' + d_2' = 2e_1^2 - 2e_1^2 = 0 \). For the determinant,
\[
(\det\L)' = (d_1d_2 - e_1^2)' = d_1'd_2 + d_1d_2' - 2e_1e_1' ,
\]
by (D1) of Chapter 15 §06. Substituting,
\[
2e_1^2d_2 - 2d_1e_1^2 - 2e_1^2(d_2 - d_1) = 0 .
\]
So both coefficients of \( p_{\L(t)}(x) = x^2 - (\tr\L)x + \det\L \) are constant, which is @thm-lax-isospectral for \( n = 2 \), got by hand.

(b) Put \( u = e^{4t} \) and
\[
d_1(t) = \frac{u - 1}{u + 1}, \qquad d_2(t) = -d_1(t), \qquad e_1(t) = \frac{2e^{2t}}{u + 1} .
\]
At \( t = 0 \), \( u = 1 \) gives \( d_1 = 0 \) and \( e_1 = 1 \), which is \( \L(0) \). Differentiating, with \( u' = 4u \),
\[
d_1' = \frac{4u(u+1) - (u-1)4u}{(u+1)^2} = \frac{8u}{(u+1)^2},
\qquad
2e_1^2 = \frac{8e^{4t}}{(u+1)^2} = \frac{8u}{(u+1)^2},
\]
so the first equation holds; the second then holds because \( d_2 = -d_1 \). For the third,
\[
e_1' = \frac{4e^{2t}(u+1) - 2e^{2t}\cdot 4u}{(u+1)^2} = \frac{4e^{2t}(1 - u)}{(u+1)^2},
\]
while \( e_1(d_2 - d_1) = -2d_1e_1 = -2\cdot\frac{u-1}{u+1}\cdot\frac{2e^{2t}}{u+1} \), which is the same. Two checks: \( d_1^2 + e_1^2 = \bigl((u-1)^2 + 4u\bigr)/(u+1)^2 = 1 \), so \( \det\L(t) = -1 \) for every \( t \), matching \( \det\L(0) = -1 \); and as \( t \to \infty \), \( d_1 \to 1 \) and \( e_1 \to 0 \), so \( \L(t) \to \diag(1, -1) \). The flow sorts the eigenvalues \( \pm 1 \) onto the diagonal, largest first.
:::

The last sentence of that example is the whole point of the section. Sorting the eigenvalues onto the diagonal in decreasing order, with the off-diagonal entries dying away, is exactly what the QR algorithm does. The next theorem says the resemblance is an identity.

## The QR algorithm is the Toda flow at integer times

One piece of algebra first. The skew-symmetric matrices and the upper triangular matrices fill \( M_n(\nR) \) between them, without overlap.

::: {#lem-skew-upper-splitting}
[Skew plus upper triangular, uniquely]

Every \( \M \in M_n(\nR) \) is \( \M = \K + \U \) for exactly one skew-symmetric \( \K \) and one upper triangular \( \U \). If \( \M \) is symmetric then \( \K = \M_{-} - \M_{+} = -\B(\M) \).
:::

::: {.proof}
*Uniqueness.* It suffices to show that a matrix \( \X \) that is both skew-symmetric and upper triangular is \( 0 \). Its transpose \( \X\tp = -\X \) is lower triangular and upper triangular at once, hence diagonal; so \( \X \) is diagonal with \( x_{ii} = -x_{ii} \), giving \( \X = 0 \). If \( \K_1 + \U_1 = \K_2 + \U_2 \) then \( \K_1 - \K_2 = \U_2 - \U_1 \) is such an \( \X \).

*Existence for symmetric \( \M \)*, which is the only case we use. Put \( \K = \M_{-} - \M_{+} \), skew-symmetric by the computation after @def-toda-flow, and \( \U = \M - \K \), whose strictly lower part is \( \M_{-} - \M_{-} = 0 \), so it is upper triangular. For a general \( \M \), take \( \K = \M_{-} - (\M_{-})\tp \) and \( \U = \M - \K \); the entries of \( \U \) below the diagonal are \( m_{ij} - m_{ij} = 0 \) for \( i > j \). This proves the lemma.
:::

::: {#thm-toda-qr-connection}
[One QR Step Is One Unit of Toda Time]

Let \( \L_0 \in M_n(\nR) \) be symmetric and let \( \A^{(1)}, \A^{(2)}, \A^{(3)}, \dots \) be the unshifted QR iterates of @def-qr-iteration started at \( \A^{(1)} = e^{\L_0} \), with the factorizations
\[
\A^{(k)} = \Q^{(k)}\R^{(k)}, \qquad \A^{(k+1)} = \R^{(k)}\Q^{(k)} \qquad (k \ge 1)
\]
normalized so that each \( \R^{(k)} \) has positive diagonal entries, and write \( \W_k = \Q^{(1)}\Q^{(2)}\cdots\Q^{(k)} \), with \( \W_0 = \I \). Then for every \( k \ge 0 \):

::: {.enumerate options="label=(\alph*)"}
1. the factorizations exist and are unique, and \( \A^{(k+1)} = \W_k\tp\,\A^{(1)}\,\W_k \);
2. \( \W_k \) is the orthogonal factor in the QR factorization of \( e^{k\L_0} \);
3. \( \A^{(k+1)} = e^{\L_k} \), where \( \L_k = \W_k\tp\,\L_0\,\W_k \) is symmetric and has the same eigenvalues as \( \L_0 \).
:::
:::

::: {.idea}
Each QR step is a similarity by the orthogonal factor, so after \( k \) steps the matrix has been conjugated by the accumulated product \( \W_k \). Conjugating an exponential is exponentiating the conjugate, which turns the statement about \( \A \) into a statement about \( \L \). The only thing left to identify is \( \W_k \), and Section 5 has already done the work: @thm-qr-is-orthogonal-iteration supplies the telescoping identity \( (\A^{(1)})^k = \W_k\R^{(k)}\cdots\R^{(1)} \). A product of orthogonal matrices is orthogonal, a product of upper triangular matrices with positive diagonal is again one, so uniqueness of the QR factorization names \( \W_k \) for us.
:::

::: {.proof}
**Step 1: the factorizations exist and are unique.** By @thm-exponential-properties (c), \( \A^{(1)} = e^{\L_0} \) is invertible, so its columns are independent and @thm-qr-factorization applies, giving a unique \( \Q^{(1)} \) with orthonormal columns — here square, hence orthogonal — and a unique upper triangular \( \R^{(1)} \) with positive diagonal. Every \( \A^{(k)} \) is similar to \( \A^{(1)} \) by @prp-qr-iteration-similar, hence invertible, so the same argument runs at every step. This positive-diagonal normalization is the choice @def-qr-iteration deliberately left open, and it is the only ingredient here that Section 5 does not already supply.

**Step 2: (a), and the telescoping identity.** Every matrix here is real and each \( \Q^{(k)} \) is orthogonal, so the conjugate transpose in @thm-qr-is-orthogonal-iteration is a transpose. With \( \S_k \coloneqq \R^{(k)}\R^{(k-1)}\cdots\R^{(1)} \) and \( \S_0 = \I \), that theorem — whose \( \U_k \) and \( \T_k \) are our \( \W_k \) and \( \S_k \) — gives, for every \( k \ge 1 \),
\[
\A^{(k+1)} = \W_k\tp\,\A^{(1)}\,\W_k
\qquad\text{and}\qquad
(\A^{(1)})^{k} = \W_k\S_k ,
\]
and for \( k = 0 \) the two read \( \A^{(1)} = \A^{(1)} \) and \( \I = \I \), since \( \W_0 = \S_0 = \I \). The first is (a).

**Step 3: (b).** Since \( \L_0 \) commutes with itself, @thm-exponential-properties (d) gives \( (e^{\L_0})^{k} = e^{k\L_0} \), so \( e^{k\L_0} = \W_k\S_k \). Each \( \Q^{(j)} \) is orthogonal, so \( \W_k \) is orthogonal. Each \( \R^{(j)} \) is upper triangular with positive diagonal, and a product of such matrices is upper triangular with diagonal entries the products of the diagonal entries, hence positive; so \( \S_k \) is upper triangular with positive diagonal. By the uniqueness in @thm-qr-factorization, \( \W_k\S_k \) **is** the QR factorization of \( e^{k\L_0} \).

**Step 4: (c).** \( \W_k \) is orthogonal, so \( \W_k\tp = \W_k^{-1} \), and @thm-exponential-properties (a) gives
\[
\A^{(k+1)} = \W_k^{-1}e^{\L_0}\W_k = e^{\W_k^{-1}\L_0\W_k} = e^{\L_k} .
\]
Finally \( \L_k\tp = \W_k\tp\L_0\tp\W_k = \L_k \), and \( \L_k \) is similar to \( \L_0 \), so the two have the same characteristic polynomial (@thm-charpoly-similarity-invariant) and hence the same eigenvalues. This proves the theorem.
:::

So the QR algorithm, applied to the exponential of a symmetric matrix, is a sequence of orthogonal conjugations of \( \L_0 \) whose \( k \)-th term is read off the QR factorization of \( e^{k\L_0} \). That last description makes sense for every real \( t \), not only for integers, and it is the missing curve.

::: {.remark}
**The continuous statement, and the one thing in it we do not prove.** For \( t \in \nR \) let \( e^{t\L_0} = \Q(t)\R(t) \) be the QR factorization with \( \R(t) \) of positive diagonal, and put \( \L(t) = \Q(t)\tp\L_0\Q(t) \). By @thm-toda-qr-connection (b) and (c), \( \Q(k) = \W_k \) and \( \L(k) = \L_k \), so this curve passes through the QR iterates at the integer times. **Granting that \( t \mapsto \Q(t) \) is differentiable** — it is, because the Gram--Schmidt formulas express its entries through arithmetic and square roots of positive quantities, but that is a fact of analysis this book has not set up — the curve satisfies the Lax equation \( \L' = [\B(\L), \L] \). Here is the derivation. Differentiating \( e^{t\L_0} = \Q\R \) with @thm-exponential-properties (b) and @lem-matrix-product-rule gives \( \L_0\Q\R = \Q'\R + \Q\R' \); multiplying by \( \R^{-1} \) on the right and \( \Q\tp \) on the left,
\[
\L(t) = \Q\tp\L_0\Q = \Q\tp\Q' + \R'\R^{-1} .
\]
Now \( \Q\tp\Q = \I \) differentiates to \( (\Q')\tp\Q + \Q\tp\Q' = 0 \), so \( \Q\tp\Q' \) is skew-symmetric, while \( \R'\R^{-1} \) is upper triangular. By @lem-skew-upper-splitting the splitting is unique, so \( \Q\tp\Q' = -\B(\L(t)) \). Differentiating \( \L = \Q\tp\L_0\Q \), inserting \( \Q\Q\tp = \I \) in each term and using \( (\Q')\tp\Q = -\Q\tp\Q' \),
\[
\L' = (\Q')\tp\L_0\Q + \Q\tp\L_0\Q' = -(\Q\tp\Q')\L + \L(\Q\tp\Q') = [\B(\L), \L] .
\]
That is a Lax equation, and \( \L_0 \) was only assumed symmetric. It is the *Toda* flow of @def-toda-flow when \( \L(t) \) is in addition symmetric **tridiagonal**, which the definition demands, and it is so whenever \( \L_0 \) is. Here is why. Since \( \R(t) \) is upper triangular and invertible, the span of the first \( j \) columns of \( \Q(t) \) is the span of the first \( j \) columns of \( e^{t\L_0} \), namely \( e^{t\L_0}\Span(\e_1, \dots, \e_j) \). A tridiagonal \( \L_0 \) carries \( \Span(\e_1, \dots, \e_j) \) into \( \Span(\e_1, \dots, \e_{j+1}) \), and it commutes with \( e^{t\L_0} \) (@thm-exponential-properties (b)), so it carries the span of the first \( j \) columns of \( \Q(t) \) into the span of the first \( j+1 \). The \( i \)-th column of \( \Q(t) \) is orthogonal to that span for \( i > j+1 \), so the \( (i,j) \) entry of \( \L(t) = \Q\tp\L_0\Q \) vanishes there: nothing below the subdiagonal, and symmetric, hence tridiagonal. For such an \( \L_0 \) the curve is the Toda flow, @prp-toda-equations puts it in the coordinates @eq-toda-coordinates, and, modulo that one differentiability, **the QR algorithm is the time-one map of the Toda flow**. The discrete half of the statement, @thm-toda-qr-connection, rests on nothing unproved; the continuous half is flagged here and nothing later depends on it.
:::

::: {.warning}
**The interpolation is of \( \L \), not of \( \A \), and it needs the starting matrix to be an exponential.** @thm-toda-qr-connection starts from \( \A^{(1)} = e^{\L_0} \), so it says nothing directly about the QR algorithm run on an arbitrary matrix. The matrices it does cover are exactly the symmetric positive definite ones. On the one hand \( e^{\L_0} = \Q e^{\D}\Q\tp \) is symmetric with positive eigenvalues \( e^{\lambda_i} \), writing \( \L_0 = \Q\D\Q\tp \) by @cor-spectral-real-matrix and using @thm-exponential-properties (a) together with @cor-exponential-of-jordan-block; on the other, a symmetric \( \A \succ 0 \) with eigenvalues \( \mu_i > 0 \) is \( e^{\L_0} \) for the symmetric \( \L_0 = \Q\diag(\log\mu_1, \dots, \log\mu_n)\Q\tp \), the logarithm being the one built in Chapter 17 §11 (@lem-exp-log). A symmetric matrix with a negative eigenvalue is therefore out of reach. The right reading is not "QR is Toda" but "QR on \( e^{\L_0} \) is Toda on \( \L_0 \)".
:::

## What this buys

Nothing in this section makes a computation faster. What it does is change what the QR algorithm *is*. As an algorithm it is a rule: factor, multiply back, repeat, and hope the subdiagonal shrinks. As a flow it is a curve in a bounded set — every entry of a symmetric matrix is at most its largest eigenvalue in absolute value, and the spectrum is frozen — and the questions one asks about it change accordingly. Why does the largest eigenvalue surface at the top left? Because \( d_1' = 2e_1^2 \ge 0 \) at all times. Why do the off-diagonal entries die away geometrically once the diagonal has almost settled? Because \( e_i' = e_i(d_{i+1} - d_i) \), which near a diagonal limit is decay at the rate of the gap \( d_i - d_{i+1} \) — the same eigenvalue gap that governs the QR algorithm's rate in Section 5. Neither reading is a proof, and neither is visible at all in the discrete language.

That is the general lesson, and it is worth naming as one of this chapter's moves: an algorithm and a differential equation can be the same object at two resolutions, and which resolution to use is a choice. Similar correspondences are known for other iterations, including the shifted QR algorithm; none of them is proved here. The subject they belong to is the theory of integrable systems, and it is the one place where this computational chapter touches pure mathematics.

## Exercises

### A. Check your understanding

:::: {#exr-lax-pairs-and-the-toda-flow-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define a Lax pair, and say which of the two functions is required to be differentiable.
2. State @thm-lax-isospectral, and name the two results from earlier chapters its proof uses.
3. Determine whether the following statement is correct, and justify your answer: if \( \L' = [\B, \L] \) then \( \L(t) = \L(0) \) for all \( t \).
4. Explain in one sentence why the proof of @thm-lax-isospectral does not construct the conjugating matrix \( \S(t) \).
5. Write down the Toda equations @eq-toda-coordinates for \( n = 3 \), and check that the sum of the three diagonal equations is \( 0 \).
:::
::::

::: {.solution}
(a) A pair \( \L, \B \colon I \to M_n(\nC) \) with \( \L \) differentiable and \( \L'(t) = \B(t)\L(t) - \L(t)\B(t) \) for all \( t \in I \). Only \( \L \) must be differentiable.

(b) The characteristic polynomial of \( \L(t) \) is independent of \( t \). The proof uses Jacobi's formula (@thm-derivative-of-det) and the adjugate identity (@thm-adjugate-identity), together with \( \tr(\X\Y) = \tr(\Y\X) \) (@thm-trace-properties (c)).

(c) Incorrect. @exm-lax-nilpotent-curve has \( \L(t) = \begin{psmallmatrix} t & -t^2 \\ 1 & -t\end{psmallmatrix} \), which is non-constant while its characteristic polynomial \( x^2 \) is constant. Isospectral is much weaker than constant.

(d) Because for a \( \B \) depending on \( t \) that matrix is the solution of a linear differential equation with variable coefficients, whose existence this book does not prove; differentiating the determinant avoids needing it at all.

(e) With \( e_0 = e_3 = 0 \):
\[
d_1' = 2e_1^2, \quad d_2' = 2(e_2^2 - e_1^2), \quad d_3' = -2e_2^2,
\]
\[
e_1' = e_1(d_2 - d_1), \quad e_2' = e_2(d_3 - d_2).
\]
The three diagonal right-hand sides sum to \( 2e_1^2 + 2e_2^2 - 2e_1^2 - 2e_2^2 = 0 \), which is the constancy of the trace.
:::

### B. Practice

:::: {#exr-lax-pairs-and-the-toda-flow-b1}
[B1: A Lax pair verified]

Let \( \B = \begin{pmatrix} 0 & 1 \\ 0 & 0\end{pmatrix} \) and \( \L(t) = \begin{pmatrix} t & -t^2 \\ 1 & -t \end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Verify directly that \( \L'(t) = [\B, \L(t)] \).
2. Compute \( p_{\L(t)} \) and confirm @thm-lax-isospectral in this case.
3. Determine whether \( \L(t) \) and \( \L(0) \) are similar for every \( t \), and exhibit the similarity.
:::
::::

::: {.solution}
(a) \( \L'(t) = \begin{psmallmatrix} 1 & -2t \\ 0 & -1\end{psmallmatrix} \). On the other side,
\[
\B\L = \begin{pmatrix} 1 & -t \\ 0 & 0\end{pmatrix},
\qquad
\L\B = \begin{pmatrix} 0 & t \\ 0 & 1\end{pmatrix},
\]
so \( [\B, \L] = \begin{psmallmatrix} 1 & -2t \\ 0 & -1\end{psmallmatrix} = \L'(t) \).

(b) \( \tr\L(t) = t - t = 0 \) and \( \det\L(t) = -t^2 - (-t^2) = 0 \), so \( p_{\L(t)}(x) = x^2 \) for every \( t \). The spectrum is \( \{0\} \) at all times.

(c) Yes. Since \( \B \) is constant, @cor-lax-constant-coefficient applies, and \( e^{t\B} = \I + t\B \) because \( \B^2 = 0 \). So
\[
\L(t) = \begin{pmatrix} 1 & t \\ 0 & 1\end{pmatrix}\L(0)\begin{pmatrix} 1 & -t \\ 0 & 1\end{pmatrix},
\qquad \L(0) = \begin{pmatrix} 0 & 0 \\ 1 & 0\end{pmatrix},
\]
which one checks by multiplying out. (Similarity is also forced by (b) alone here: both matrices are non-zero and nilpotent of size \( 2 \), hence both similar to \( \J_2(0) \).)
:::

:::: {#exr-lax-pairs-and-the-toda-flow-b2}
[B2: The bracket by hand]

Let
\[
\L = \begin{pmatrix} 1 & 2 & 0 \\ 2 & 3 & 1 \\ 0 & 1 & -1\end{pmatrix}.
\]
Compute \( \B(\L) \) and \( [\B(\L), \L] \) directly, and check the answer against @prp-toda-equations.
::::

::: {.solution}
Here \( d = (1, 3, -1) \) and \( e = (2, 1) \). The strictly upper and lower parts give
\[
\B(\L) = \begin{pmatrix} 0 & 2 & 0 \\ -2 & 0 & 1 \\ 0 & -1 & 0\end{pmatrix}.
\]
Multiplying,
\[
\B(\L)\L = \begin{pmatrix} 4 & 6 & 2 \\ -2 & -3 & -1 \\ -2 & -3 & -1\end{pmatrix},
\qquad
\L\B(\L) = \begin{pmatrix} -4 & 2 & 2 \\ -6 & 3 & 3 \\ -2 & 1 & 1\end{pmatrix},
\]
so
\[
[\B(\L), \L] = \begin{pmatrix} 8 & 4 & 0 \\ 4 & -6 & -4 \\ 0 & -4 & -2\end{pmatrix}.
\]
Against @prp-toda-equations: \( 2(e_1^2 - e_0^2) = 2\cdot4 = 8 \); \( 2(e_2^2 - e_1^2) = 2(1 - 4) = -6 \); \( 2(e_3^2 - e_2^2) = -2 \); \( e_1(d_2 - d_1) = 2(3-1) = 4 \); \( e_2(d_3 - d_2) = 1(-1-3) = -4 \). All five agree, the matrix is symmetric tridiagonal, and its trace is \( 8 - 6 - 2 = 0 \), as it must be.
:::

:::: {#exr-lax-pairs-and-the-toda-flow-b3}
[B3: One QR step on an exponential]

Let \( \L_0 = \begin{psmallmatrix} 0 & 1 \\ 1 & 0\end{psmallmatrix} \) and \( \A^{(1)} = e^{\L_0} \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( e^{t\L_0} = \begin{psmallmatrix} c(t) & s(t) \\ s(t) & c(t)\end{psmallmatrix} \) with \( c(t) = \tfrac12(e^{t} + e^{-t}) \) and \( s(t) = \tfrac12(e^{t} - e^{-t}) \).
2. Find the QR factorization of \( e^{t\L_0} \) with positive diagonal, and hence \( \L(t) = \Q(t)\tp\L_0\Q(t) \).
3. Compare your \( \L(1) \) with @exm-toda-two-by-two (b).
:::
::::

::: {.solution}
(a) \( \L_0^2 = \I \), so \( \L_0^{2m} = \I \) and \( \L_0^{2m+1} = \L_0 \). Splitting @def-matrix-exponential into even and odd terms,
\[
e^{t\L_0} = \Bigl(\sum_{m \ge 0}\frac{t^{2m}}{(2m)!}\Bigr)\I + \Bigl(\sum_{m\ge0}\frac{t^{2m+1}}{(2m+1)!}\Bigr)\L_0 ,
\]
and the two scalar series are the even and odd halves of \( e^{t} = \sum_j t^j/j! \), namely \( c(t) \) and \( s(t) \) by fact (A1) of Chapter 9 §09.

(b) Write \( \rho = (c^2 + s^2)^{1/2} > 0 \). Gram--Schmidt on the columns, as in @thm-qr-factorization: the first column \( (c, s) \) normalizes to \( \q_1 = \rho^{-1}(c,s) \); the second column \( (s,c) \) has \( \inner{(s,c)}{\q_1} = 2cs/\rho \), and
\[
(s,c) - \frac{2cs}{\rho^2}(c,s) = \frac{c^2 - s^2}{\rho^2}(-s, c) = \frac{1}{\rho^2}(-s,c),
\]
because \( c^2 - s^2 = 1 \). That vector has length \( 1/\rho \), so \( \q_2 = \rho^{-1}(-s, c) \). Hence \( \Q(t) = \rho^{-1}\begin{psmallmatrix} c & -s \\ s & c\end{psmallmatrix} \), whose determinant is \( 1 \), and \( \R(t) = \Q(t)\tp e^{t\L_0} \) has positive diagonal. Then
\[
\L(t) = \Q\tp\L_0\Q = \frac{1}{\rho^2}\begin{pmatrix} 2cs & 1 \\ 1 & -2cs\end{pmatrix}.
\]
Since \( \rho^2 = c^2 + s^2 = \tfrac12(e^{2t} + e^{-2t}) \) and \( 2cs = \tfrac12(e^{2t} - e^{-2t}) \), multiplying numerator and denominator by \( 2e^{2t} \) gives
\[
\L(t) = \begin{pmatrix} \dfrac{e^{4t} - 1}{e^{4t}+1} & \dfrac{2e^{2t}}{e^{4t}+1} \\[6pt] \dfrac{2e^{2t}}{e^{4t}+1} & -\dfrac{e^{4t}-1}{e^{4t}+1}\end{pmatrix}.
\]

(c) This is exactly the solution written down in @exm-toda-two-by-two (b). At \( t = 1 \) it is \( d_1 = (e^4-1)/(e^4+1) \approx 0.9640 \) and \( e_1 = 2e^2/(e^4+1) \approx 0.2658 \). One QR step on \( e^{\L_0} \) has moved \( \L \) one unit of Toda time, and the off-diagonal entry has already fallen from \( 1 \) to about \( 0.27 \).
:::

### C. Going deeper

:::: {#exr-lax-pairs-and-the-toda-flow-c1}
[C1: The power sums are constants of the motion]

Let \( (\L, \B) \) be a Lax pair on \( I \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( t \mapsto \tr\bigl(\L(t)^{m}\bigr) \) is constant for every integer \( m \ge 1 \). *Hint: the product rule, then @thm-trace-properties (c).*
2. Deduce, for \( n = 2 \), that the characteristic polynomial of \( \L(t) \) is constant, without using @thm-lax-isospectral.
:::
::::

::: {.solution}
(a) By @lem-matrix-product-rule and induction, \( t \mapsto \L(t)^m \) is differentiable with
\[
(\L^m)' = \sum_{j=0}^{m-1}\L^{j}\,\L'\,\L^{m-1-j} .
\]
The trace is linear (@thm-trace-properties (a)) and unchanged by a cyclic shift (@thm-trace-properties (c)), so each summand contributes \( \tr(\L^{m-1}\L') \), and
\[
\bigl(\tr\L^m\bigr)' = m\,\tr\bigl(\L^{m-1}\L'\bigr) = m\,\tr\bigl(\L^{m-1}(\B\L - \L\B)\bigr).
\]
Now \( \tr(\L^{m-1}\B\L) = \tr(\L\L^{m-1}\B) = \tr(\L^{m}\B) \) by a cyclic shift, and \( \tr(\L^{m-1}\L\B) = \tr(\L^m\B) \) as well, so the bracket contributes \( 0 \). By fact (A6) of Chapter 15's introduction the function is constant on \( I \).

(b) For \( n = 2 \), \( p_{\L(t)}(x) = x^2 - \tau x + \delta \) with \( \tau = \tr\L(t) \) and \( \delta = \det\L(t) \). By Cayley--Hamilton (@thm-cayley-hamilton), \( \L^2 - \tau\L + \delta\I = 0 \); taking traces gives \( \tr(\L^2) - \tau^2 + 2\delta = 0 \), that is
\[
\delta = \tfrac12\bigl(\tau^2 - \tr(\L^2)\bigr).
\]
Part (a) with \( m = 1 \) makes \( \tau \) constant and with \( m = 2 \) makes \( \tr(\L^2) \) constant, so \( \delta \) is constant too. Hence \( p_{\L(t)} \) is constant.
:::

:::: {#exr-lax-pairs-and-the-toda-flow-c2}
[C2: How far \( \B \) is from being determined]

Let \( (\L, \B) \) be a Lax pair on \( I \) and let \( \C \colon I \to M_n(\nC) \) satisfy \( [\C(t), \L(t)] = 0 \) for every \( t \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( (\L, \B + \C) \) is also a Lax pair.
2. Give an example with \( \C \ne 0 \), and conclude that a Lax equation does not determine \( \B \).
3. Prove, using @lem-skew-upper-splitting, that there is nevertheless **exactly one** skew-symmetric \( \B \) for which \( \B + \) (upper triangular) equals a given symmetric \( \L \) — that is, the \( \B(\L) \) of @def-toda-flow is the only natural candidate once "skew-symmetric" and "upper triangular" are the two slots.
:::
::::

::: {.solution}
(a) \( [\B + \C, \L] = [\B, \L] + [\C, \L] = [\B, \L] + 0 = \L' \).

(b) Take \( \C(t) = c\,\I \) for any scalar \( c \ne 0 \), or \( \C(t) = q(\L(t)) \) for any polynomial \( q \), since a polynomial in \( \L \) commutes with \( \L \). So \( \B \) can always be altered by a multiple of \( \I \) without changing the flow, and the Lax equation determines \( \B \) at most up to the commutant of \( \L \).

(c) @lem-skew-upper-splitting says \( \L = \K + \U \) for exactly one skew-symmetric \( \K \) and one upper triangular \( \U \), and computes \( \K = \L_{-} - \L_{+} = -\B(\L) \) for symmetric \( \L \). So the pair of slots (skew, upper triangular) picks out \( \B(\L) \) uniquely, up to the sign convention, and the remaining freedom found in (a) and (b) is freedom in a *different* decomposition, not in this one.
:::

:::: {#exr-lax-pairs-and-the-toda-flow-c3}
[C3: Symmetry constrains \( \B \)]

Let \( (\L, \B) \) be a Lax pair of real matrices on \( I \) with \( \L(t) \) symmetric for every \( t \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( [\B(t) + \B(t)\tp,\ \L(t)] = 0 \) for every \( t \).
2. Deduce that \( \bigl(\L, \tfrac12(\B - \B\tp)\bigr) \) is also a Lax pair, so that \( \B \) may always be taken skew-symmetric.
3. Determine whether the Toda \( \B(\L) \) of @def-toda-flow satisfies the hypothesis of (a). Justify your answer.
:::
::::

::: {.solution}
(a) Transposing \( \L' = \B\L - \L\B \) and using \( \L\tp = \L \) — so that \( (\L')\tp = (\L\tp)' = \L' \), differentiation being entrywise — gives
\[
\L' = (\L')\tp = \L\tp\B\tp - \B\tp\L\tp = \L\B\tp - \B\tp\L = -[\B\tp, \L].
\]
Adding this to \( \L' = [\B, \L] \) gives \( 2\L' = [\B, \L] - [\B\tp, \L] \), while subtracting gives \( 0 = [\B, \L] + [\B\tp, \L] = [\B + \B\tp, \L] \).

(b) Put \( \C = -\tfrac12(\B + \B\tp) \). By (a), \( [\B + \B\tp, \L] = 0 \), so \( [\C, \L] = 0 \), and @exr-lax-pairs-and-the-toda-flow-c2 (a) says \( (\L, \B + \C) \) is a Lax pair. But \( \B + \C = \B - \tfrac12(\B + \B\tp) = \tfrac12(\B - \B\tp) \), which is skew-symmetric. So the skew part of \( \B \) already drives the flow, and the symmetric part is inert.

(c) Yes, and trivially: \( \B(\L) \) is skew-symmetric for symmetric \( \L \), so \( \B(\L) + \B(\L)\tp = 0 \), which commutes with everything. Part (b) says that this is not a lucky feature of the Toda choice but the normal form of any Lax pair with symmetric \( \L \).
:::
