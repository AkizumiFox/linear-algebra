# Schur Triangularization

Chapter 8 proved that every operator on a non-zero complex vector space has an upper triangular matrix in **some** basis (@cor-complex-triangularizable). That basis was built by extending an eigenvector and passing to a quotient, and it came out as skewed as the operator happened to be. Now we have lengths and angles, so we can be fussier and ask for an **orthonormal** basis. The remarkable thing is that the answer is still yes, at no extra cost in hypotheses, and the proof is the same induction run inside an orthogonal complement rather than in a quotient. This section proves it, reads off the first consequences, and gives the real version, where a conjugate pair of eigenvalues costs one \( 2 \times 2 \) block.

Throughout, \( V \) is a finite-dimensional inner product space over \( F = \nR \) or \( F = \nC \), and every matrix statement uses the standard inner product on \( F^n \).

## Why the obvious route fails

Here is the natural first attempt, and it is worth watching it fail, because the repair is the whole idea of the proof.

We want an orthonormal basis \( \sB = (\v_1, \dots, \v_n) \) with \( \mtx{T}{\sB}{\sB} \) upper triangular, that is, with
\[
T\v_j \in \Span(\v_1, \dots, \v_j) \qquad \text{for every } j .
\]
For \( j = 1 \) this says \( \v_1 \) is an eigenvector of \( T \), and over \( \nC \) one exists (@thm-complex-operator-has-eigenvalue). Normalize it, set \( U = (\Span(\v_1))^{\perp} \), and try to finish by induction on \( U \). The attempt stops at once: to speak of \( T \) restricted to \( U \) we need \( U \) to be \( T \)-invariant, and it need not be.

::: {#exm-eigenline-complement-not-invariant}
[An Eigenline Whose Complement Is Not Invariant]

Let \( \A = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix} \) act on \( \nC^2 \). Check that \( \e_1 \) is an eigenvector and decide whether \( (\Span(\e_1))^{\perp} \) is invariant.
:::

::: {.solution}
\( \A\e_1 = (1, 0) = \e_1 \), so \( \e_1 \) is an eigenvector for the eigenvalue \( 1 \). The orthogonal complement of \( \Span(\e_1) \) is \( \Span(\e_2) \), and \( \A\e_2 = (1, 2) \), which is not a multiple of \( \e_2 \). So \( (\Span(\e_1))^{\perp} \) is **not** invariant, and the induction has nothing to run on.
:::

So the first basis vector is the wrong end to start from. Look at the target instead. Suppose \( \sB \) is orthonormal and \( \mtx{T}{\sB}{\sB} = \T \) is upper triangular. By @thm-matrix-of-adjoint the matrix of \( T^{*} \) in the same basis is \( \T^{*} \), which is **lower** triangular; and the last column of a lower triangular matrix has only its bottom entry. Reading that column off,
\[
T^{*}\v_n = \conj{t_{nn}}\,\v_n .
\]
*In the basis we are trying to build, the last vector is an eigenvector of \( T^{*} \) — not of \( T \).*

That is the vector to produce first, and it is exactly the one whose orthogonal complement behaves.

::: {#lem-adjoint-eigenline-complement}
[Eigenvectors of the Adjoint Cut Out Invariant Subspaces]

Let \( V \) be a finite-dimensional inner product space over \( F \), let \( T \in \cL(V) \), and let \( W \subseteq V \) be a \( T^{*} \)-invariant subspace. Then \( W^{\perp} \) is \( T \)-invariant.
:::

::: {.proof}
Let \( \u \in W^{\perp} \) and \( \w \in W \). Since \( W \) is \( T^{*} \)-invariant, \( T^{*}\w \in W \), so by @def-adjoint
\[
\inner{T\u}{\w} = \inner{\u}{T^{*}\w} = 0 .
\]
As \( \w \in W \) was arbitrary, \( T\u \in W^{\perp} \). Hence \( T(W^{\perp}) \subseteq W^{\perp} \).
:::

The special case we need is \( W = \Span(\v) \) with \( T^{*}\v = \mu\v \): one vector, one line, and an invariant complement of dimension \( n - 1 \) to recurse into. And over \( \nC \) such a \( \v \) always exists, because \( T^{*} \) is an operator on a non-zero complex space and the Fundamental Theorem of Algebra gives it an eigenvalue. That is where the field enters, and it is the only place it enters.

## The theorem

::: {#thm-schur-triangularization}
[Schur's Unitary Triangularization]

Let \( V \) be a finite-dimensional inner product space over \( \nC \) with \( \dim V = n \ge 1 \), and let \( T \in \cL(V) \).

::: {.enumerate options="label=(\alph*)"}
1. There is an **orthonormal** basis \( \sB \) of \( V \) such that \( \mtx{T}{\sB}{\sB} \) is upper triangular.
2. More precisely, let \( \lambda_1, \dots, \lambda_n \) be the eigenvalues of \( T \), each listed as often as its algebraic multiplicity, in **any** order we please. Then \( \sB \) can be chosen so that the \( i \)-th diagonal entry of \( \mtx{T}{\sB}{\sB} \) is \( \lambda_i \).
:::
:::

::: {.idea}
Induction on \( \dim V \), building the basis from its **last** vector backwards. ① Pick the eigenvalue \( \lambda_n \) we want in the bottom-right corner; the conjugate \( \conj{\lambda_n} \) is then an eigenvalue of \( T^{*} \), because starring turns a non-invertible operator into a non-invertible operator. ② Take a unit eigenvector \( \e \) of \( T^{*} \) for \( \conj{\lambda_n} \) and put \( U = (\Span(\e))^{\perp} \); by @lem-adjoint-eigenline-complement it is \( T \)-invariant, so \( T|_U \) exists and lives on a space of dimension \( n - 1 \). ③ Check that the characteristic polynomial of \( T|_U \) is \( p_T \) with the factor \( x - \lambda_n \) removed, so the inductive hypothesis may be applied with the shortened list. ④ Append \( \e \) to the basis it returns.
:::

::: {.proof}
We induct on \( n = \dim V \). Since \( \nC \) is algebraically closed, \( p_T \) splits (@cor-complex-polynomial-splits), so a list \( \lambda_1, \dots, \lambda_n \) as in (b) exists and \( p_T = (x - \lambda_1)\cdots(x - \lambda_n) \); proving (b) proves (a).

For \( n = 1 \), any unit vector \( \v_1 \) is a basis, every \( 1 \times 1 \) matrix is upper triangular, and its single entry is the single eigenvalue \( \lambda_1 \).

Let \( n \ge 2 \) and assume the statement for all inner product spaces of dimension \( n - 1 \). Fix a list \( \lambda_1, \dots, \lambda_n \) as in (b).

**\( \conj{\lambda_n} \) is an eigenvalue of \( T^{*} \).** Since \( \lambda_n \) is an eigenvalue of \( T \), the operator \( T - \lambda_n\,\id_V \) is not invertible (@thm-eigenvalue-characterizations). By @thm-adjoint-properties (a), (b) and (d), its adjoint is \( T^{*} - \conj{\lambda_n}\,\id_V \), and the adjoint of that is \( T - \lambda_n\,\id_V \) again. If \( T^{*} - \conj{\lambda_n}\,\id_V \) were invertible, then @thm-adjoint-properties (e) would make its adjoint \( T - \lambda_n\,\id_V \) invertible too. So \( T^{*} - \conj{\lambda_n}\,\id_V \) is not invertible, and \( \conj{\lambda_n} \in \spec(T^{*}) \).

Choose an eigenvector of \( T^{*} \) for \( \conj{\lambda_n} \); it is non-zero, so dividing by its norm gives a unit vector \( \e \) with \( T^{*}\e = \conj{\lambda_n}\e \). Put \( U = (\Span(\e))^{\perp} \). By @thm-orthogonal-decomposition (c), \( \dim U = n - 1 \ge 1 \), and \( U \) is \( T \)-invariant by @lem-adjoint-eigenline-complement. Write \( S = T|_U \in \cL(U) \), where \( U \) carries the inner product of \( V \).

**The bottom-right entry is \( \lambda_n \).** Using @def-adjoint and conjugate-linearity in the second slot,
\[
\inner{T\e}{\e} = \inner{\e}{T^{*}\e} = \inner{\e}{\conj{\lambda_n}\e} = \lambda_n\norm{\e}^2 = \lambda_n .
\]

**The shortened list belongs to \( S \).** Take any orthonormal basis \( (\f_1, \dots, \f_{n-1}) \) of \( U \) (@thm-gram-schmidt) and set \( \sC = (\f_1, \dots, \f_{n-1}, \e) \), an orthonormal list of \( n \) vectors, hence an orthonormal basis of \( V \) by @thm-orthogonal-independent and @thm-right-size-basis. Since \( U \) is \( T \)-invariant, @thm-invariant-subspace-matrix (b) applies with the basis \( \sC \) and gives \( p_T = p_S\,p_{\bar T} \), where \( \bar T \) is the induced operator on the one-dimensional quotient \( V/U \). Its matrix is the single bottom-right entry of \( \mtx{T}{\sC}{\sC} \), which is \( \inner{T\e}{\e} = \lambda_n \) by @thm-orthonormal-coordinates; so \( p_{\bar T} = x - \lambda_n \). Canceling that factor in \( \nC[x] \),
\[
p_S = (x - \lambda_1)\cdots(x - \lambda_{n-1}) .
\]
So \( \lambda_1, \dots, \lambda_{n-1} \) is a list of the eigenvalues of \( S \) with their algebraic multiplicities.

**Induct.** By the inductive hypothesis there is an orthonormal basis \( (\v_1, \dots, \v_{n-1}) \) of \( U \) in which the matrix of \( S \) is upper triangular with diagonal \( \lambda_1, \dots, \lambda_{n-1} \). Put \( \sB = (\v_1, \dots, \v_{n-1}, \e) \), again an orthonormal basis of \( V \) for the reason given above. For \( j \le n - 1 \) we have \( T\v_j = S\v_j \in \Span(\v_1, \dots, \v_j) \), so the \( j \)-th column of \( \mtx{T}{\sB}{\sB} \) vanishes below row \( j \) and has \( \lambda_j \) in row \( j \). The \( n \)-th column has nothing below row \( n \), and its entry there is \( \inner{T\e}{\e} = \lambda_n \). Hence \( \mtx{T}{\sB}{\sB} \) is upper triangular with diagonal \( \lambda_1, \dots, \lambda_n \). This proves the theorem.
:::

Two hypotheses did all the work, and it is worth naming which. **Complex** produced the eigenvalue of \( T^{*} \), through the Fundamental Theorem of Algebra; over \( \nR \) the theorem is false as stated, and the last part of this section says what survives. **Inner product** produced the invariant complement, through @lem-adjoint-eigenline-complement; without one we would be back in Chapter 8's quotient. Notice also what the theorem does **not** claim: nothing was assumed about \( T \), and nothing beyond triangularity is promised. Diagonal is a different and much stronger request, and Sections 4 and 5 say exactly which operators grant it.

## The matrix form

Translating through an orthonormal basis turns the theorem into a factorization. Recall that a square complex matrix is **unitary** when \( \U^{*}\U = \I \) (@def-unitary-orthogonal), and call two matrices **unitarily similar** when \( \B = \U^{*}\A\U \) for some unitary \( \U \); this is similarity by a matrix that is also an isometry, so it preserves the inner product as well as the operator.

::: {#cor-schur-matrix}
[Schur Factorization]

Let \( \A \in M_n(\nC) \) with \( n \ge 1 \), and let \( \lambda_1, \dots, \lambda_n \) be the eigenvalues of \( \A \), each listed as often as its algebraic multiplicity, in any prescribed order. Then there are a unitary \( \U \in M_n(\nC) \) and an upper triangular \( \T \in M_n(\nC) \) with
\[
\A = \U\T\U^{*}, \qquad t_{ii} = \lambda_i \quad (1 \le i \le n) .
\]
:::

::: {.proof}
Apply @thm-schur-triangularization to \( T_{\A} \) on \( \nC^n \) with the standard inner product and the given list: there is an orthonormal basis \( \sB = (\u_1, \dots, \u_n) \) of \( \nC^n \) with \( \T \coloneqq \mtx{T_{\A}}{\sB}{\sB} \) upper triangular and \( t_{ii} = \lambda_i \). Let \( \U \) be the matrix whose \( j \)-th column is \( \u_j \). Its columns are orthonormal, so \( \U \) is unitary (@thm-isometry-characterizations (f), @def-unitary-orthogonal), and \( \U = \mtx{\id}{\sB}{\sE} \) for the standard basis \( \sE \) (@def-change-of-coordinates-matrix). Since \( \mtx{T_{\A}}{\sE}{\sE} = \A \), @thm-change-of-basis-maps gives \( \T = \U^{-1}\A\U = \U^{*}\A\U \), the last step because \( \U^{-1} = \U^{*} \) for a unitary matrix. Rearranging gives \( \A = \U\T\U^{*} \).
:::

The order of the diagonal is free because at each step of the induction we chose which eigenvalue to send to the bottom-right corner, and any of them was available. That freedom is used constantly: it lets us put a distinguished eigenvalue first, or collect equal eigenvalues into a block.

::: {.remark}
**How to compute one.** The induction above runs from the bottom-right corner, because that is the corner where an operator on a subspace is available. For a **matrix** there is a second route, running from the top-left, and it is the one to use by hand. Let \( \q_1 \) be a unit eigenvector of \( \A \) for an eigenvalue \( \lambda \), extend it to an orthonormal basis of \( \nC^n \) (@cor-extend-orthonormal-basis) and let \( \Q \) be the unitary matrix with those columns. Then \( \Q^{*}\A\q_1 = \lambda\Q^{*}\q_1 = \lambda\e_1 \), so
\[
\Q^{*}\A\Q = \begin{pmatrix} \lambda & \b^{*} \\ \0 & \A_1 \end{pmatrix}
\]
for some \( \b \in \nC^{n-1} \) and \( \A_1 \in M_{n-1}(\nC) \). Triangularize \( \A_1 = \V\T_1\V^{*} \) and put \( \U = \Q(1 \oplus \V) \); the product is unitary and \( \U^{*}\A\U \) is upper triangular. This is legitimate for matrices precisely because we may replace \( \A \) by the compressed block \( \A_1 \), which is not the restriction of any operator: \( (\Span(\q_1))^{\perp} \) is not invariant, as @exm-eigenline-complement-not-invariant showed.
:::

::: {#exm-schur-2x2}
[A Two-by-Two Schur Factorization]

Find a unitary \( \U \) and an upper triangular \( \T \) with \( \U^{*}\A\U = \T \), as in @cor-schur-matrix, for
\[
\A = \begin{pmatrix} 2 & -1 \\ 1 & 4 \end{pmatrix} .
\]
:::

::: {.solution}
Here \( \tr\A = 6 \) and \( \det\A = 8 + 1 = 9 \), so \( p_{\A} = x^2 - 6x + 9 = (x - 3)^2 \) and the only eigenvalue is \( 3 \), with algebraic multiplicity \( 2 \).

Solving \( (\A - 3\I)\x = \0 \) with \( \A - 3\I = \begin{pmatrix} -1 & -1 \\ 1 & 1 \end{pmatrix} \) gives the single eigenline \( \Span\bigl((1, -1)\bigr) \). Take \( \q_1 = \tfrac1{\sqrt2}(1, -1) \) and complete with \( \q_2 = \tfrac1{\sqrt2}(1, 1) \), a unit vector orthogonal to \( \q_1 \). With \( \U \) the matrix of those columns,
\[
\U = \tfrac1{\sqrt2}\begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix},
\qquad
\U^{*}\A\U = \begin{pmatrix} 3 & -2 \\ 0 & 3 \end{pmatrix} .
\]
Both diagonal entries are \( 3 \), as they must be. The off-diagonal \( -2 \) cannot be removed: a matrix unitarily similar to \( \diag(3, 3) = 3\I \) would equal \( \U(3\I)\U^{*} = 3\I \), and \( \A \ne 3\I \).
:::

::: {#exm-schur-3x3}
[A Three-by-Three Schur Factorization]

Find a unitary \( \U \) and an upper triangular \( \T \) with \( \U^{*}\A\U = \T \), as in @cor-schur-matrix, for
\[
\A = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & -2 \\ 4 & -3 & -2 \end{pmatrix} .
\]
:::

::: {.solution}
*Step 1: peel off one eigenvector.* Expanding \( \det(x\I - \A) \) gives \( p_{\A} = (x - 1)(x - 3)(x + 4) \), so \( 1 \) is an eigenvalue. Solving \( (\A - \I)\x = \0 \) by row reduction gives the eigenline spanned by \( (3, 4, 0) \), of norm \( 5 \). Put
\[
\q_1 = \tfrac15(3, 4, 0), \quad \q_2 = \tfrac15(4, -3, 0), \quad \q_3 = (0, 0, 1),
\]
an orthonormal basis of \( \nC^3 \) (each has norm \( 1 \) and the three pairwise inner products are \( 0 \); the entries are real, so no conjugates intrude). With \( \Q = \begin{pmatrix} \q_1 & \q_2 & \q_3 \end{pmatrix} \),
\[
\Q^{*}\A\Q = \begin{pmatrix} 1 & 0 & -1 \\ 0 & 1 & 2 \\ 0 & 5 & -2 \end{pmatrix},
\qquad
\A_1 = \begin{pmatrix} 1 & 2 \\ 5 & -2 \end{pmatrix} .
\]

*Step 2: triangularize the block.* Here \( \tr\A_1 = -1 \) and \( \det\A_1 = -12 \), so \( p_{\A_1} = x^2 + x - 12 = (x - 3)(x + 4) \). For the eigenvalue \( 3 \), \( \A_1 - 3\I = \begin{pmatrix} -2 & 2 \\ 5 & -5 \end{pmatrix} \) gives the eigenvector \( (1, 1) \). Take \( \p_1 = \tfrac1{\sqrt2}(1, 1) \) and \( \p_2 = \tfrac1{\sqrt2}(1, -1) \), and let \( \V \) be the matrix of those columns. Then
\[
\V^{*}\A_1\V = \begin{pmatrix} 3 & 3 \\ 0 & -4 \end{pmatrix} .
\]

*Step 3: assemble.* Put \( \U = \Q(1 \oplus \V) \), whose columns are \( \q_1 \), \( (\q_2 + \q_3)/\sqrt2 \) and \( (\q_2 - \q_3)/\sqrt2 \):
\[
\U = \tfrac1{5\sqrt2}\begin{pmatrix} 3\sqrt2 & 4 & 4 \\ 4\sqrt2 & -3 & -3 \\ 0 & 5 & -5 \end{pmatrix},
\qquad
\U^{*}\A\U = \begin{pmatrix} 1 & -\tfrac1{\sqrt2} & \tfrac1{\sqrt2} \\ 0 & 3 & 3 \\ 0 & 0 & -4 \end{pmatrix} .
\]
The diagonal reads \( 1, 3, -4 \), and indeed \( p_{\A} = (x - 1)(x - 3)(x + 4) \), with trace \( 0 = 1 + 3 - 4 \) and determinant \( -12 = 1 \cdot 3 \cdot (-4) \).
:::

::: {.check}
Why does @thm-schur-triangularization not prove that every complex matrix is unitarily similar to a **diagonal** matrix?
:::

::: {.solution}
Because the proof controls only the entries below the diagonal. The entries above it are whatever they happen to be, and @exm-schur-2x2 shows they need not vanish: the matrix there has a \( -2 \) in the corner, and no unitary can remove it. A matrix unitarily similar to a diagonal one satisfies strong conditions — Section 4 identifies them exactly — and most matrices do not.
:::

## Reading the diagonal

A triangular form with an explicit factorization makes two Chapter 8 facts fall out in a line each.

::: {#cor-trace-sum-eigenvalues-again}
[Trace Is the Sum of the Eigenvalues]

Let \( \A \in M_n(\nC) \) have eigenvalues \( \lambda_1, \dots, \lambda_n \), listed with algebraic multiplicity. Then \( \tr\A = \lambda_1 + \dots + \lambda_n \).
:::

::: {.proof}
Write \( \A = \U\T\U^{*} \) as in @cor-schur-matrix. By @thm-trace-properties (3) applied to the pair \( \U \) and \( \T\U^{*} \),
\[
\tr\A = \tr\bigl(\U(\T\U^{*})\bigr) = \tr\bigl((\T\U^{*})\U\bigr) = \tr\T,
\]
since \( \U^{*}\U = \I \). The diagonal of \( \T \) is the list \( \lambda_1, \dots, \lambda_n \).
:::

::: {#cor-det-product-eigenvalues-again}
[Determinant Is the Product of the Eigenvalues]

Let \( \A \in M_n(\nC) \) have eigenvalues \( \lambda_1, \dots, \lambda_n \), listed with algebraic multiplicity. Then \( \det\A = \lambda_1\cdots\lambda_n \).
:::

::: {.proof}
With \( \A = \U\T\U^{*} \) as above, @thm-det-multiplicative gives \( \det\A = \det\U\,\det\T\,\det\U^{*} \), and \( \det\U\,\det\U^{*} = \det(\U\U^{*}) = \det\I = 1 \). So \( \det\A = \det\T \), which is the product of the diagonal entries by @thm-det-triangular.
:::

Both statements are @thm-trace-det-eigenvalues over \( \nC \), recovered from the diagonal of \( \T \) instead of from the coefficients of \( p_{\A} \). Nothing is new; what is new is how short the argument became once a triangular form was available in hand.

The next consequence is not a restatement of anything. It says that the matrices we know how to handle sit arbitrarily close to the ones we do not.

::: {#cor-schur-normal-matrix-nearby}
[Diagonalizable Matrices Are Everywhere]

Let \( \A \in M_n(\nC) \) and let \( \varepsilon > 0 \). Then there is a **diagonalizable** \( \A' \in M_n(\nC) \) with
\[
\lvert a_{ij} - a'_{ij} \rvert < \varepsilon \qquad \text{for all } i, j .
\]
In this sense every complex square matrix is a limit of diagonalizable ones.
:::

::: {.idea}
Diagonalizability is hard to arrange directly, but \( n \) distinct eigenvalues force it (@cor-distinct-eigenvalues-diagonalizable), and in a triangular form the eigenvalues are sitting on the diagonal where we can nudge them apart. The only thing to check is that a small nudge inside the triangular form is still a small nudge after conjugating back by \( \U \), and that is Cauchy–Schwarz on the rows of a unitary matrix.
:::

::: {.proof}
Write \( \A = \U\T\U^{*} \) as in @cor-schur-matrix. Choose \( \delta_1, \dots, \delta_n \in \nC \) with \( \lvert \delta_k \rvert < \varepsilon \) and with \( t_{11} + \delta_1, \dots, t_{nn} + \delta_n \) pairwise distinct. This is possible one index at a time: having chosen \( \delta_1, \dots, \delta_{k-1} \), the forbidden values of \( \delta_k \) are the \( k - 1 \) numbers \( t_{jj} + \delta_j - t_{kk} \), and the disc \( \{ \lvert z \rvert < \varepsilon \} \) has infinitely many points.

Put \( \D = \diag(\delta_1, \dots, \delta_n) \) and \( \A' = \U(\T + \D)\U^{*} \). The matrix \( \T + \D \) is upper triangular with \( n \) distinct diagonal entries, so by @thm-diagonal-of-triangular-form (b) it has \( n \) distinct eigenvalues; \( \A' \) is similar to it, hence has the same eigenvalues, and is diagonalizable by @cor-distinct-eigenvalues-diagonalizable.

For the entries, \( \A - \A' = -\U\D\U^{*} \), whose \( (i, j) \) entry is \( -\sum_{k} u_{ik}\delta_k\conj{u_{jk}} \). Hence
\[
\lvert a_{ij} - a'_{ij} \rvert \le \max_k \lvert \delta_k \rvert \sum_{k=1}^{n} \lvert u_{ik} \rvert\,\lvert u_{jk} \rvert \le \max_k \lvert \delta_k \rvert < \varepsilon,
\]
where the middle inequality is @thm-cauchy-schwarz applied to the vectors of moduli, together with the fact that the rows of \( \U \) are unit vectors, which is \( \U\U^{*} = \I \). This proves the corollary.
:::

This is the tool behind a standard strategy: *prove it for diagonalizable matrices, then take a limit*. Chapter 15, where matrices acquire norms and limits can be spoken of properly, runs arguments of exactly this shape; and @exr-schur-triangularization-c1 uses the triangular form directly, with no limits at all, to reprove the Cayley–Hamilton theorem over \( \nC \).

## The real version

Over \( \nR \) the theorem fails, and it fails for the reason it always does: a rotation has no real eigenvector, so no real basis makes its matrix triangular (@thm-triangularization). The most one can hope for is to let a conjugate pair occupy a \( 2 \times 2 \) block, and that much is true.

::: {#thm-real-schur}
[Real Schur Form]

Let \( \A \in M_n(\nR) \) with \( n \ge 1 \). Then there are an orthogonal \( \Q \in \Orth(n) \) and a matrix \( \T \in M_n(\nR) \) with
\[
\A = \Q\T\Q\tp,
\]
where \( \T \) is **block** upper triangular with diagonal blocks of size \( 1 \times 1 \) and \( 2 \times 2 \), and every \( 2 \times 2 \) diagonal block has a conjugate pair of non-real eigenvalues.
:::

::: {.idea}
The same induction, with one change. The eigenvector of \( T^{*} \) may fail to exist over \( \nR \), but an invariant subspace of dimension \( 1 \) or \( 2 \) always does — that is @exr-triangularization-c2, proved in Chapter 8 from a complex eigenvector \( \x + i\y \) by taking \( \Span(\x, \y) \). Apply it to \( T^{*} \), take the orthogonal complement, and induct. Dimension \( 1 \) occurs exactly when \( T^{*} \) has a real eigenvalue, and that is what keeps the \( 2 \times 2 \) blocks honest.
:::

::: {.proof}
Let \( T = T_{\A} \) on \( \nR^n \) with the standard inner product, so that \( T^{*} = T_{\A\tp} \) by @thm-matrix-of-adjoint. We induct on \( n \).

Choose a \( T^{*} \)-invariant subspace \( W \) as follows. If \( T^{*} \) has a real eigenvalue, let \( W \) be a corresponding eigenline, so \( d \coloneqq \dim W = 1 \). If it does not, take a complex eigenvalue \( \mu = a + bi \) of \( \A\tp \) with \( b \ne 0 \), which exists by @thm-complex-operator-has-eigenvalue applied to \( \A\tp \) over \( \nC \), and a complex eigenvector \( \x + i\y \) with \( \x, \y \in \nR^n \). Comparing real and imaginary parts of \( \A\tp(\x + i\y) = \mu(\x + i\y) \) gives \( \A\tp\x = a\x - b\y \) and \( \A\tp\y = b\x + a\y \), so \( W \coloneqq \Span(\x, \y) \) is \( T^{*} \)-invariant. It has dimension \( 2 \): were \( \x, \y \) dependent, \( W \) would be a \( T^{*} \)-invariant line and \( T^{*} \) would have a real eigenvalue, contrary to the case we are in. So \( d = 2 \). (@exr-triangularization-c2 runs the same argument in Chapter 8.)

Put \( U = W^{\perp} \), which is \( T \)-invariant by @lem-adjoint-eigenline-complement and has dimension \( n - d \) (@thm-orthogonal-decomposition (c)). Pick an orthonormal basis \( (\v_1, \dots, \v_{n-d}) \) of \( U \) and one \( (\v_{n-d+1}, \dots, \v_n) \) of \( W \) (@thm-gram-schmidt); together they form an orthonormal basis \( \sB \) of \( \nR^n \), since the two blocks are orthogonal to each other. Because \( T(U) \subseteq U \),
\[
\mtx{T}{\sB}{\sB} = \begin{pmatrix} \C & \ast \\ \0 & \B \end{pmatrix}
\]
with \( \C \in M_{n-d}(\nR) \) the matrix of \( T|_U \) and \( \B \in M_d(\nR) \). Writing \( \Q_{\sB} \) for the matrix whose columns are the vectors of \( \sB \), which is orthogonal because those columns are orthonormal, @thm-change-of-basis-maps gives \( \Q_{\sB}\tp\A\Q_{\sB} = \mtx{T}{\sB}{\sB} \).

*The block \( \B \) is of the allowed kind.* If \( d = 1 \) it is \( 1 \times 1 \). If \( d = 2 \), then by @thm-matrix-of-adjoint the matrix of \( T^{*} \) in \( \sB \) is the transpose of the display, whose bottom-right block is \( \B\tp \); as \( W \) is \( T^{*} \)-invariant, \( \B\tp \) is the matrix of \( T^{*}|_W \). A real eigenvalue of \( \B\tp \) would be a real eigenvalue of \( T^{*} \), which this case excludes. So \( p_{\B} = p_{\B\tp} \) has no real root, and its two complex roots form a conjugate pair by @thm-real-matrix-complex-eigenvalues.

*Close the induction.* If \( U = \{\0\} \) then \( n = d \le 2 \), the list \( \sB \) is a basis of \( W \), and \( \Q_{\sB}\tp\A\Q_{\sB} = \B \) is already a single allowed block; take \( \Q = \Q_{\sB} \). Otherwise \( 1 \le n - d < n \), and by the inductive hypothesis \( \C = \Q_1\T_1\Q_1\tp \) with \( \Q_1 \in \Orth(n - d) \) and \( \T_1 \) of the required shape. Put \( \Q = \Q_{\sB}(\Q_1 \oplus \I_d) \), a product of orthogonal matrices and so orthogonal (@prp-orthogonal-group-properties (a)). Then
\[
\Q\tp\A\Q = (\Q_1 \oplus \I_d)\tp\begin{pmatrix} \C & \ast \\ \0 & \B \end{pmatrix}(\Q_1 \oplus \I_d)
= \begin{pmatrix} \T_1 & \ast \\ \0 & \B \end{pmatrix},
\]
which is block upper triangular with diagonal blocks those of \( \T_1 \) followed by \( \B \). This proves the theorem.
:::

Two remarks on the shape. The \( 1 \times 1 \) blocks carry the real eigenvalues of \( \A \) and the \( 2 \times 2 \) blocks carry the non-real ones in conjugate pairs, so the block sizes are forced by the spectrum, even though the blocks themselves are not. And when all the eigenvalues of \( \A \) are real, every block is \( 1 \times 1 \) and the real Schur form is an honest orthogonal triangularization.

::: {.warning}
**Neither \( \T \) nor \( \U \) is unique; only the diagonal multiset is.** For \( \A = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix} \), taking \( \U = \I \) gives \( \T = \A \), with diagonal \( (1, 2) \). Taking instead \( \U = \tfrac1{\sqrt2}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \) gives
\[
\U^{*}\A\U = \begin{pmatrix} 2 & -1 \\ 0 & 1 \end{pmatrix},
\]
with diagonal \( (2, 1) \) and a different corner entry. So a Schur form is **not** a canonical form: it does not decide similarity, and two matrices can have the same triangular form without being equal. The canonical form for similarity is Jordan's (@thm-jordan-canonical-form), and Jordan's cannot in general be reached unitarily — @exm-schur-2x2 is already a Jordan block in disguise whose off-diagonal entry is \( -2 \), not \( 1 \). What the Schur form gives up in uniqueness it buys back in stability: the change of basis is an isometry.
:::

## Exercises

### A. Check your understanding

:::: {#exr-schur-triangularization-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State @thm-schur-triangularization, including the field and every hypothesis.
2. In the proof, an eigenvector of \( T^{*} \) is taken rather than one of \( T \). Say why, in one sentence, and name the property of \( (\Span(\v))^{\perp} \) that is wanted.
3. True or false: if \( \A \in M_n(\nC) \) is upper triangular in some orthonormal basis, then its eigenvalues are the diagonal entries of that triangular matrix. Justify your answer.
4. Which step of the proof of @thm-schur-triangularization fails over \( \nR \)?
5. Give a matrix in \( M_2(\nC) \) that is upper triangular in an orthonormal basis but is **not** diagonal in any.
:::
::::

::: {.solution}
(a) Let \( V \) be a finite-dimensional inner product space over \( \nC \) with \( \dim V \ge 1 \) and let \( T \in \cL(V) \). Then \( V \) has an orthonormal basis \( \sB \) with \( \mtx{T}{\sB}{\sB} \) upper triangular, and the diagonal may be made to read the eigenvalues of \( T \), with algebraic multiplicity, in any prescribed order.

(b) Because the induction needs \( (\Span(\v))^{\perp} \) to be **\( T \)-invariant**, and @lem-adjoint-eigenline-complement gives that exactly when \( \Span(\v) \) is \( T^{*} \)-invariant, that is, when \( \v \) is an eigenvector of \( T^{*} \).

(c) True. The matrix of \( T \) in **any** basis has the same characteristic polynomial (@thm-charpoly-similarity-invariant), and for a triangular matrix that polynomial is the product of \( x - t_{ii} \) (@thm-diagonal-of-triangular-form (a)). Orthonormality is irrelevant to this particular point.

(d) The Fundamental Theorem of Algebra, twice: once so that \( p_T \) splits into the list of \( n \) roots the statement speaks of (@cor-complex-polynomial-splits), and once for the existence of an eigenvalue of \( T^{*} \) at each stage of the induction. It came from @thm-complex-operator-has-eigenvalue, whose proof rests on the Fundamental Theorem of Algebra (@thm-fundamental-theorem-of-algebra); over \( \nR \) the rotation \( \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \) has no eigenvalue at all. Every other step is valid over \( \nR \).

(e) \( \A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \). It is already upper triangular in the standard orthonormal basis. It is not diagonal in any basis, orthonormal or not: its only eigenvalue is \( 0 \), so a diagonal form would be the zero matrix, and \( \A \ne 0 \).
:::

### B. Practice

:::: {#exr-schur-triangularization-b1}
[B1: A Schur form with complex entries]

Let \( \A = \begin{pmatrix} 1 & 2 \\ -1 & 3 \end{pmatrix} \), regarded as a complex matrix.

::: {.enumerate options="label=(\alph*)"}
1. Find the eigenvalues of \( \A \).
2. Find a unitary \( \U \in M_2(\nC) \) with \( \U^{*}\A\U \) upper triangular, and compute that triangular matrix.
3. Explain why no **real** orthogonal \( \Q \) makes \( \Q\tp\A\Q \) upper triangular.
:::
::::

::: {.solution}
(a) \( \tr\A = 4 \) and \( \det\A = 3 + 2 = 5 \), so \( p_{\A} = x^2 - 4x + 5 = (x - 2)^2 + 1 \), with roots \( 2 + i \) and \( 2 - i \).

(b) For \( \lambda = 2 + i \),
\[
\A - \lambda\I = \begin{pmatrix} -1 - i & 2 \\ -1 & 1 - i \end{pmatrix} .
\]
The second row gives \( -x + (1 - i)y = 0 \), so \( (1 - i, 1) \) is an eigenvector; its norm is \( \sqrt{2 + 1} = \sqrt3 \). Put \( \q_1 = \tfrac1{\sqrt3}(1 - i, 1) \). A unit vector orthogonal to it is \( \q_2 = \tfrac1{\sqrt3}(1, -1 - i) \), since
\[
\inner{\q_2}{\q_1} = \tfrac13\bigl(1 \cdot \conj{1 - i} + (-1 - i)\cdot\conj{1}\bigr) = \tfrac13\bigl((1 + i) - (1 + i)\bigr) = 0
\]
and \( \norm{\q_2}^2 = \tfrac13(1 + 2) = 1 \). With \( \U = \begin{pmatrix} \q_1 & \q_2 \end{pmatrix} \),
\[
\U^{*}\A\U = \begin{pmatrix} 2 + i & -1 - 2i \\ 0 & 2 - i \end{pmatrix} .
\]

(c) A real upper triangular matrix has its diagonal entries as eigenvalues (@thm-diagonal-of-triangular-form), and those entries are real. But \( \Q\tp\A\Q \) is similar to \( \A \), whose eigenvalues \( 2 \pm i \) are not real. So no such \( \Q \) exists. (This is @thm-real-schur doing the only thing it can: here \( \T \) is a single \( 2 \times 2 \) block, and \( \Q = \I \) already works.)
:::

:::: {#exr-schur-triangularization-b2}
[B2: A three-by-three Schur form]

Let \( \A = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 3 \\ 0 & 0 & 4 \end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Verify that \( (1, -1, 0) \) is an eigenvector and find the corresponding eigenvalue.
2. Extend it to an orthonormal basis of \( \nR^3 \) and compute \( \Q\tp\A\Q \) for the resulting \( \Q \).
3. Hence write down the eigenvalues of \( \A \) with their algebraic multiplicities.
:::
::::

::: {.solution}
(a) \( \A(1, -1, 0) = (2 - 1,\; 1 - 2,\; 0) = (1, -1, 0) \), so the eigenvalue is \( 1 \).

(b) Take \( \q_1 = \tfrac1{\sqrt2}(1, -1, 0) \), \( \q_2 = \tfrac1{\sqrt2}(1, 1, 0) \) and \( \q_3 = (0, 0, 1) \). These are pairwise orthogonal unit vectors, hence an orthonormal basis of \( \nR^3 \). With \( \Q = \begin{pmatrix} \q_1 & \q_2 & \q_3 \end{pmatrix} \),
\[
\Q\tp\A\Q = \begin{pmatrix} 1 & 0 & -\sqrt2 \\ 0 & 3 & 2\sqrt2 \\ 0 & 0 & 4 \end{pmatrix} .
\]
This is already upper triangular, so a single step sufficed and \( \U = \Q \). (In general the lower-right \( 2 \times 2 \) block would need a second step, as in @exm-schur-3x3.)

(c) The diagonal is \( 1, 3, 4 \), so by @thm-diagonal-of-triangular-form these are the eigenvalues, each of algebraic multiplicity \( 1 \). As a check, \( \tr\A = 8 = 1 + 3 + 4 \) and \( \det\A = 4(4 - 1) = 12 = 1 \cdot 3 \cdot 4 \).
:::

:::: {#exr-schur-triangularization-b3}
[B3: The field matters]

Let \( \A = \begin{pmatrix} a & -b \\ b & a \end{pmatrix} \in M_2(\nR) \) with \( b \ne 0 \).

::: {.enumerate options="label=(\alph*)"}
1. Find the eigenvalues of \( \A \) over \( \nC \) and show that \( \A \) is unitarily similar to a diagonal matrix in \( M_2(\nC) \).
2. Prove that there is no invertible \( \P \in M_2(\nR) \) at all, orthogonal or otherwise, with \( \P^{-1}\A\P \) upper triangular.
3. Say what @thm-real-schur produces for this \( \A \).
:::
::::

::: {.solution}
(a) \( \tr\A = 2a \) and \( \det\A = a^2 + b^2 \), so \( p_{\A} = x^2 - 2ax + a^2 + b^2 \) with roots \( a \pm bi \), distinct because \( b \ne 0 \). For \( \lambda = a + bi \), \( \A(1, -i) = (a + bi,\; b - ai) = (a + bi)(1, -i) \), so \( \q_1 = \tfrac1{\sqrt2}(1, -i) \) is a unit eigenvector; likewise \( \q_2 = \tfrac1{\sqrt2}(1, i) \) is a unit eigenvector for \( a - bi \), and
\[
\inner{\q_1}{\q_2} = \tfrac12\bigl(1 \cdot 1 + (-i)\conj{i}\bigr) = \tfrac12(1 - 1) = 0 .
\]
So \( \U = \begin{pmatrix} \q_1 & \q_2 \end{pmatrix} \) is unitary and \( \U^{*}\A\U = \diag(a + bi,\; a - bi) \).

(b) Suppose \( \P^{-1}\A\P = \T \) were upper triangular with \( \P \in M_2(\nR) \) invertible. Then \( \T \in M_2(\nR) \) is similar to \( \A \), so \( p_{\T} = p_{\A} \) (@thm-charpoly-similarity-invariant); but \( p_{\T} = (x - t_{11})(x - t_{22}) \) has the real roots \( t_{11}, t_{22} \), while \( p_{\A} \) has none. Contradiction.

(c) Since \( \A \) has no real eigenvalue, the real Schur form of \( \A \) is a single \( 2 \times 2 \) diagonal block; \( \Q = \I_2 \) and \( \T = \A \) already work. There is nothing to simplify: over \( \nR \) this matrix is as reduced as it gets.
:::

### C. Going deeper

:::: {#exr-schur-triangularization-c1}
[C1: Cayley–Hamilton from the triangular factors]

Let \( \T \in M_n(\nC) \) be upper triangular with diagonal entries \( \lambda_1, \dots, \lambda_n \), and set \( \N_k = (\T - \lambda_1\I)(\T - \lambda_2\I)\cdots(\T - \lambda_k\I) \) for \( 1 \le k \le n \).

::: {.enumerate options="label=(\alph*)"}
1. Prove by induction on \( k \) that the first \( k \) columns of \( \N_k \) are zero.
2. Deduce that \( p_{\T}(\T) = 0 \).
3. Deduce the Cayley–Hamilton Theorem (@thm-cayley-hamilton) for every \( \A \in M_n(\nC) \), using @cor-schur-matrix.
:::

*Hint for (a): the \( j \)-th column of \( \T - \lambda_j\I \) has its only possibly non-zero entries in rows \( 1, \dots, j - 1 \).*
::::

::: {.solution}
(a) For \( k = 1 \): the first column of \( \T - \lambda_1\I \) is \( (\lambda_1 - \lambda_1, 0, \dots, 0) = \0 \), since \( \T \) is upper triangular.

Assume the first \( k - 1 \) columns of \( \N_{k-1} \) are zero, where \( 2 \le k \le n \). Then \( \N_k = \N_{k-1}(\T - \lambda_k\I) \), so the \( j \)-th column of \( \N_k \) is \( \N_{k-1}\c_j \) with \( \c_j \) the \( j \)-th column of \( \T - \lambda_k\I \). For \( j \le k - 1 \) we get \( \N_k\e_j = \N_{k-1}(\T - \lambda_k\I)\e_j \), and since \( (\T - \lambda_k\I)\e_j \in \Span(\e_1, \dots, \e_j) \) by upper triangularity, this is a combination of the first \( j \le k - 1 \) columns of \( \N_{k-1} \), all zero. For \( j = k \) the column \( \c_k \) of \( \T - \lambda_k\I \) has its \( (k, k) \) entry equal to \( \lambda_k - \lambda_k = 0 \) and zeros below, so \( \c_k \in \Span(\e_1, \dots, \e_{k-1}) \), and \( \N_{k-1}\c_k \) is a combination of the first \( k - 1 \) columns of \( \N_{k-1} \), again zero. So all of the first \( k \) columns of \( \N_k \) vanish.

(b) By @thm-diagonal-of-triangular-form (a), \( p_{\T} = (x - \lambda_1)\cdots(x - \lambda_n) \), so \( p_{\T}(\T) = \N_n \). By (a) with \( k = n \), all \( n \) columns of \( \N_n \) are zero, that is \( p_{\T}(\T) = 0 \).

(c) Write \( \A = \U\T\U^{*} \) by @cor-schur-matrix. Similar matrices have the same characteristic polynomial (@thm-charpoly-similarity-invariant), so \( p_{\A} = p_{\T} \), and \( \A^k = \U\T^k\U^{*} \) for every \( k \ge 0 \) because the inner factors \( \U^{*}\U \) cancel. Hence
\[
p_{\A}(\A) = \U\,p_{\T}(\T)\,\U^{*} = \U\,0\,\U^{*} = 0 .
\]
Chapter 8 reached the same conclusion from the flag of invariant subspaces (@exr-triangularization-c1); here the whole argument happens inside one matrix product.
:::

:::: {#exr-schur-triangularization-c2}
[C2: The Frobenius norm is unitarily invariant]

Chapter 10 §07 introduced the Frobenius norm \( \norm{\A}_F = \bigl(\sum_{i, j} \lvert a_{ij} \rvert^2\bigr)^{1/2} \) and proved (a) and (b) below as @lem-frobenius-unitarily-invariant. Prove them again here without looking, since the argument is two lines and (c) is what this section is for.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \norm{\A}_F^2 = \tr(\A^{*}\A) \).
2. Prove that \( \norm{\U\A}_F = \norm{\A}_F = \norm{\A\V}_F \) whenever \( \U \in M_m(\nC) \) and \( \V \in M_n(\nC) \) are unitary.
3. Deduce that if \( \A = \U\T\U^{*} \) is a Schur factorization (@cor-schur-matrix), then \( \norm{\A}_F = \norm{\T}_F \).
:::
::::

::: {.solution}
(a) The \( (j, j) \) entry of \( \A^{*}\A \) is \( \sum_{i} \conj{a_{ij}}a_{ij} = \sum_i \lvert a_{ij} \rvert^2 \). Summing over \( j \) gives \( \tr(\A^{*}\A) = \sum_{i,j}\lvert a_{ij}\rvert^2 = \norm{\A}_F^2 \).

(b) By (a) and \( \U^{*}\U = \I_m \),
\[
\norm{\U\A}_F^2 = \tr\bigl((\U\A)^{*}(\U\A)\bigr) = \tr(\A^{*}\U^{*}\U\A) = \tr(\A^{*}\A) = \norm{\A}_F^2 .
\]
For the other side, use \( \tr(\B\C) = \tr(\C\B) \) (@thm-trace-properties (3)) and \( \V\V^{*} = \I_n \):
\[
\norm{\A\V}_F^2 = \tr(\V^{*}\A^{*}\A\V) = \tr(\A^{*}\A\V\V^{*}) = \tr(\A^{*}\A) = \norm{\A}_F^2 .
\]
Norms are non-negative, so the squares being equal gives the norms equal.

(c) Apply (b) twice: \( \norm{\A}_F = \norm{\U\T\U^{*}}_F = \norm{\T\U^{*}}_F = \norm{\T}_F \), using that \( \U^{*} \) is unitary as well. So a Schur factorization redistributes the size of \( \A \) between the diagonal and the strictly upper triangle without changing the total. Section 11 turns that observation into a measurement.
:::

:::: {#exr-schur-triangularization-c3}
[C3: Distinct eigenvalues are dense, but not over the reals]

::: {.enumerate options="label=(\alph*)"}
1. Sharpen @cor-schur-normal-matrix-nearby: prove that for every \( \A \in M_n(\nC) \) and every \( \varepsilon > 0 \) there is \( \A' \) with \( n \) **distinct** eigenvalues and \( \lvert a_{ij} - a'_{ij} \rvert < \varepsilon \) for all \( i, j \).
2. Show that the analogous statement fails over \( \nR \): for \( \R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \) there is an \( \varepsilon > 0 \) such that **no** real matrix within \( \varepsilon \) of \( \R \), entry by entry, has a real eigenvalue at all.
:::

*Hint for (b): a real \( 2 \times 2 \) matrix with entries \( a, b, c, d \) has real eigenvalues exactly when \( (a - d)^2 + 4bc \ge 0 \).*
::::

::: {.solution}
(a) This is exactly what the proof of @cor-schur-normal-matrix-nearby produced, before the conclusion was weakened. There the \( \delta_k \) were chosen so that the diagonal entries of \( \T + \D \) are pairwise distinct, and by @thm-diagonal-of-triangular-form (b) those \( n \) distinct numbers are the eigenvalues of \( \T + \D \), hence of the similar matrix \( \A' = \U(\T + \D)\U^{*} \). The entrywise estimate is unchanged.

(b) The characteristic polynomial of \( \begin{pmatrix} a & b \\ c & d \end{pmatrix} \) is \( x^2 - (a + d)x + (ad - bc) \), whose discriminant is
\[
(a + d)^2 - 4(ad - bc) = (a - d)^2 + 4bc,
\]
so the eigenvalues are real exactly when this is \( \ge 0 \). Take \( \varepsilon = \tfrac14 \) and let \( \A' \) have entries within \( \varepsilon \) of those of \( \R \), so \( \lvert a \rvert, \lvert d \rvert \le \tfrac14 \), \( b \in [-\tfrac54, -\tfrac34] \) and \( c \in [\tfrac34, \tfrac54] \). Then \( (a - d)^2 \le \tfrac14 \) and \( bc \le -\tfrac9{16} \), so
\[
(a - d)^2 + 4bc \le \tfrac14 - \tfrac94 = -2 < 0 .
\]
Hence \( \A' \) has no real eigenvalue, let alone two distinct ones. The reason is the one this section keeps meeting: over \( \nC \) the eigenvalues move continuously and can always be separated, while over \( \nR \) a conjugate pair cannot be pushed onto the real line by a small change.
:::
