# Commuting Families

Chapter 8 asked when several operators can be diagonalized in one basis and answered: exactly when they commute, provided each of them is diagonalizable on its own. With an inner product in hand the question sharpens in the same way the spectral theorem sharpened diagonalization. Can one **orthonormal** basis diagonalize all of them at once? For normal operators over \( \nC \) the answer is yes, and the proof is the chapter's signature move applied family-wide: cut the space into the eigenspaces of one member and recurse.

Throughout, \( V \) is a finite-dimensional inner product space over \( F = \nR \) or \( \nC \), and a family \( \cF \subseteq \cL(V) \) is called **commuting** if \( ST = TS \) for all \( S, T \in \cF \), as in Chapter 8.

## What Chapter 8 already gives, and what is missing

Three results from Chapter 8 do the bookkeeping, and it is worth being exact about what each one delivers.

- @thm-commuting-preserves-eigenspaces: if \( ST = TS \) then every eigenspace \( E_\lambda(T) \) is \( S \)-invariant. No hypothesis at all beyond commuting — not even finite dimension. This is what lets us look for common eigenvectors *inside* an eigenspace.
- @thm-commuting-common-eigenvector: a commuting family whose characteristic polynomials all split has a common eigenvector. Over \( \nC \) the splitting is automatic.
- @thm-simultaneous-diagonalization and @thm-simultaneous-diagonalization-family: a commuting family of **diagonalizable** operators is simultaneously diagonalizable (@def-simultaneously-diagonalizable), and conversely.

Two things are missing from that list. First, diagonalizability is a hypothesis there, and it has to be checked separately for each member. Second, and more to the point here, the common basis produced is just a basis: nothing says its vectors are orthogonal, and in general they are not.

Normality repairs both at once, over \( \nC \). It repairs the first because a normal operator is automatically diagonalizable, by @thm-spectral-complex. It repairs the second because that same theorem produces an *orthonormal* eigenbasis, so the pieces we cut the space into are mutually orthogonal.

One more ingredient is needed before the recursion can run: after cutting \( V \) into the eigenspaces of one member, the other members must still be normal on each piece. Section 3 supplies exactly this. An invariant subspace of a normal operator is automatically invariant under the adjoint as well, and the restriction to it is again normal: that is @prp-normal-invariant-reducing, proved there by a trace computation on the block form. Over \( \nR \) the self-adjoint version is @thm-self-adjoint-invariant-complement. (What fails, as the warning of Section 3 records, is the analogous statement for a subspace that is **not** invariant: a principal submatrix of a normal matrix need not be normal.) With that recalled, nothing stands in the way.

## One orthonormal basis for the whole family

::: {#thm-simultaneous-unitary-diagonalization}
[One Orthonormal Eigenbasis for a Commuting Family]

Let \( V \neq \{\0\} \) be a finite-dimensional **complex** inner product space and let \( \cF \subseteq \cL(V) \) be a non-empty commuting family of **normal** operators. Then \( V \) has an orthonormal basis \( \sB \) each of whose vectors is an eigenvector of every \( T \in \cF \); equivalently, \( [T]_{\sB} \) is diagonal for every \( T \in \cF \).

Conversely, if some orthonormal basis \( \sB \) makes every \( [T]_{\sB} \) diagonal, then \( \cF \) is commuting and every member of \( \cF \) is normal.
:::

::: {.idea}
Induction on \( \dim V \), with the two cases that every such induction has. If every member of the family is a scalar multiple of the identity, any orthonormal basis will do and there is nothing to arrange. Otherwise some \( T_0 \in \cF \) has at least two distinct eigenvalues, and @thm-spectral-complex splits \( V \) into the eigenspaces of \( T_0 \) — **orthogonally**, and into pieces strictly smaller than \( V \). Each piece is invariant under the whole family because the operators commute, and the restriction of a normal operator to an invariant subspace is normal, so each restricted family is again a commuting family of normal operators on a smaller space. Run the induction on each piece and glue.
:::

::: {.proof}
Induction on \( n = \dim V \ge 1 \).

If \( n = 1 \), any unit vector \( \v \) of \( V \) is a basis, and \( T\v \in V = \Span(\v) \) makes \( \v \) an eigenvector of every \( T \in \cL(V) \).

Let \( n \ge 2 \) and assume the theorem for all complex inner product spaces of dimension less than \( n \).

**Case 1: every \( T \in \cF \) is a scalar multiple of \( \id_V \).** Then every non-zero vector is an eigenvector of every \( T \in \cF \), and \( V \) has an orthonormal basis by @thm-gram-schmidt.

**Case 2: some \( T_0 \in \cF \) is not a scalar multiple of \( \id_V \).** Since \( T_0 \) is normal, @thm-spectral-complex gives an orthonormal basis \( \sC = (\c_1, \dots, \c_n) \) of \( V \) with \( T_0\c_j = \mu_j\c_j \). Let \( \lambda_1, \dots, \lambda_k \) be the distinct values among \( \mu_1, \dots, \mu_n \), and put
\[
V_i = \Span\{\c_j : \mu_j = \lambda_i\}, \qquad i = 1, \dots, k .
\]
The \( V_i \) are spanned by disjoint sub-lists of an orthonormal basis, so they are pairwise orthogonal, \( V = V_1 \oplus \cdots \oplus V_k \), and \( \dim V_1 + \cdots + \dim V_k = n \).

::: {.claim}
\( V_i = E_{\lambda_i}(T_0) \) for each \( i \).

::: {.proof}
The inclusion \( V_i \subseteq E_{\lambda_i}(T_0) \) holds because every spanning vector \( \c_j \) of \( V_i \) satisfies \( T_0\c_j = \lambda_i\c_j \). Conversely let \( \v \in E_{\lambda_i}(T_0) \) and write \( \v = \v_1 + \cdots + \v_k \) with \( \v_j \in V_j \). Applying \( T_0 \), which acts as \( \lambda_j \) on \( V_j \), gives \( \sum_j \lambda_j\v_j = T_0\v = \lambda_i\v = \sum_j \lambda_i\v_j \), so \( \sum_j (\lambda_j - \lambda_i)\v_j = \0 \). The sum being direct, each term vanishes, and \( \lambda_j \neq \lambda_i \) for \( j \neq i \) forces \( \v_j = \0 \). Hence \( \v = \v_i \in V_i \).
:::
:::

Because \( T_0 \) is not a scalar multiple of \( \id_V \), we have \( k \ge 2 \): if \( k = 1 \) then \( V = V_1 = E_{\lambda_1}(T_0) \) and \( T_0 = \lambda_1\id_V \). Hence \( \dim V_i < n \) for every \( i \).

Fix \( i \) and let \( S \in \cF \). By @thm-commuting-preserves-eigenspaces, \( V_i = E_{\lambda_i}(T_0) \) is \( S \)-invariant, and therefore \( S|_{V_i} \) is a normal operator on \( V_i \) by @prp-normal-invariant-reducing. Moreover the family
\[
\cF_i = \{\, S|_{V_i} : S \in \cF \,\}
\]
is commuting, since \( (S|_{V_i})(T|_{V_i}) = (ST)|_{V_i} = (TS)|_{V_i} = (T|_{V_i})(S|_{V_i}) \) for \( S, T \in \cF \), all four restrictions being defined because \( V_i \) is invariant.

By the inductive hypothesis applied to \( V_i \neq \{\0\} \) and \( \cF_i \), there is an orthonormal basis \( \sB_i \) of \( V_i \) whose vectors are eigenvectors of every \( S|_{V_i} \); such a vector \( \v \in V_i \) satisfies \( S\v = (S|_{V_i})\v = \mu\v \), so it is an eigenvector of \( S \) itself. Let \( \sB \) be the concatenation \( \sB_1, \dots, \sB_k \). It is orthonormal, because each \( \sB_i \) is and because \( V_i \perp V_j \) for \( i \neq j \), and it has \( \sum_i \dim V_i = n \) vectors, so it is an orthonormal basis of \( V \) (@thm-orthogonal-independent and @thm-right-size-basis). Every vector of \( \sB \) is an eigenvector of every \( T \in \cF \). This completes the induction.

For the converse, suppose every \( [T]_{\sB} \) is diagonal with \( \sB \) orthonormal. Diagonal matrices commute, so \( [ST]_{\sB} = [TS]_{\sB} \) and hence \( ST = TS \) (@thm-linear-maps-isomorphic-to-matrices). And \( [T^{*}]_{\sB} = ([T]_{\sB})^{*} \) by @thm-matrix-of-adjoint is diagonal as well, so \( [T^{*}T]_{\sB} \) and \( [TT^{*}]_{\sB} \) are products of diagonal matrices in the two orders, hence equal; so \( T \) is normal. This proves the theorem.
:::

Notice which hypothesis did which job. *Commuting* made the eigenspaces of \( T_0 \) invariant under the rest of the family; *normal* made those eigenspaces orthogonal and made the restrictions normal again; and *complex* is what makes \( T_0 \) have any eigenvalues at all. Drop any one of the three and the argument stops.

In matrix language:

::: {#cor-simultaneous-unitary-matrix}
[Commuting Normal Matrices]

Let \( \A_1, \dots, \A_r \in M_n(\nC) \) be normal and pairwise commuting. Then there is a unitary \( \U \in \Unit(n) \) such that \( \U^{*}\A_i\U \) is diagonal for every \( i \). The same holds for an arbitrary commuting family of normal matrices in \( M_n(\nC) \).
:::

::: {.proof}
Apply @thm-simultaneous-unitary-diagonalization to the family \( \{T_{\A_1}, \dots, T_{\A_r}\} \) on \( \nC^n \). Each \( T_{\A_i} \) is normal because \( T_{\A_i}^{*} = T_{\A_i^{*}} \) (@thm-matrix-of-adjoint, the standard basis being orthonormal) and \( \A_i^{*}\A_i = \A_i\A_i^{*} \); and the operators commute because the matrices do. Let \( \U \) have the resulting orthonormal basis \( \sB \) as its columns; then \( \U \in \Unit(n) \) by @thm-isometry-characterizations (f), and \( \U^{*}\A_i\U = \U^{-1}\A_i\U = [T_{\A_i}]_{\sB} \) is diagonal by @thm-change-of-basis-maps. Nothing in the argument used that the family is finite.
:::

::: {#cor-simultaneous-orthogonal-real}
[Commuting Symmetric Matrices]

Let \( V \) be a finite-dimensional **real** inner product space and let \( \cF \subseteq \cL(V) \) be a non-empty commuting family of self-adjoint operators. Then \( V \) has an orthonormal basis of common eigenvectors. Equivalently, if \( \A_1, \dots, \A_r \in M_n(\nR) \) are symmetric and pairwise commuting, there is \( \Q \in \Orth(n) \) with every \( \Q\tp\A_i\Q \) diagonal.
:::

::: {.proof}
Repeat the proof of @thm-simultaneous-unitary-diagonalization word for word, with two substitutions: use @thm-spectral-real in place of @thm-spectral-complex to split \( V \) into the eigenspaces of a member \( T_0 \) that is not a scalar multiple of \( \id_V \), and use @thm-self-adjoint-invariant-complement (b) in place of @prp-normal-invariant-reducing to see that each restriction \( S|_{V_i} \) is again self-adjoint. Every other step is unchanged, and the only property of \( \nC \) used in the original was the existence of an eigenvalue, which @thm-spectral-real supplies over \( \nR \) from self-adjointness. The matrix statement follows as in @cor-simultaneous-unitary-matrix, using @cor-spectral-real-matrix and \( \Q\tp = \Q^{-1} \).
:::

::: {#exm-simultaneous-orthogonal-3x3}
[Two Commuting Symmetric Matrices, Diagonalized Together]

Let
\[
\A = \begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix},
\qquad
\B = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 1 & 1 \end{pmatrix} \in M_3(\nR) .
\]
Check that \( \A\B = \B\A \) and find \( \Q \in \Orth(3) \) with \( \Q\tp\A\Q \) and \( \Q\tp\B\Q \) both diagonal.
:::

::: {.solution}
*They commute.* Multiplying out,
\[
\A\B = \begin{pmatrix} 0 & 2 & 2 \\ 2 & 1 & 1 \\ 2 & 1 & 1 \end{pmatrix} = \B\A .
\]
Both matrices are symmetric, so @cor-simultaneous-orthogonal-real applies.

*Diagonalize \( \A \).* Each row of \( \A \) sums to \( 2 \), so \( \A(1,1,1) = (2,2,2) \) and \( 2 \) is an eigenvalue with eigenvector \( (1,1,1) \). Also \( \A = \1\1\tp - \I_3 \), where \( \1 = (1,1,1) \); any \( \v \) with \( \1\tp\v = 0 \), that is with \( v_1 + v_2 + v_3 = 0 \), satisfies \( \A\v = -\v \). So \( E_2(\A) = \Span((1,1,1)) \) and \( E_{-1}(\A) \) is the plane \( v_1 + v_2 + v_3 = 0 \), and these account for all of \( \nR^3 \).

*The one-dimensional eigenspace.* By @thm-commuting-preserves-eigenspaces the line \( E_2(\A) \) is \( \B \)-invariant, so its spanning vector must already be an eigenvector of \( \B \). Indeed \( \B(1,1,1) = (2,2,2) \).

*The plane.* Inside \( E_{-1}(\A) \) we must search. The matrix \( \B \) has \( \B(0,1,-1) = (0,0,0) \) and \( \B(-2,1,1) = (-4,2,2) = 2(-2,1,1) \), and both \( (0,1,-1) \) and \( (-2,1,1) \) have coordinate sum \( 0 \), so they lie in \( E_{-1}(\A) \). They are orthogonal, and independent, so they are a basis of the plane.

*The common basis.* Normalizing the three vectors,
\[
\Q = \begin{pmatrix}
 1/\sqrt3 & -2/\sqrt6 & 0 \\
 1/\sqrt3 & 1/\sqrt6 & 1/\sqrt2 \\
 1/\sqrt3 & 1/\sqrt6 & -1/\sqrt2
\end{pmatrix},
\]
whose columns are orthonormal, so \( \Q \in \Orth(3) \) by @thm-isometry-characterizations (f). Then
\[
\Q\tp\A\Q = \diag(2, -1, -1), \qquad \Q\tp\B\Q = \diag(2, 2, 0),
\]
the diagonal entries being the eigenvalues found above, column by column. Neither matrix alone forces the choice: \( \A \) cannot tell the second column from the third, and \( \B \) cannot tell the first from the second. Together they pin down all three lines.
:::

::: {.warning}
**Neither hypothesis can be dropped.**

*Commuting is not enough.* The matrices \( \A = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix} \) and \( \B = \begin{pmatrix} 1 & 3 \\ 0 & 4 \end{pmatrix} \) satisfy \( \A\B = \begin{pmatrix} 1 & 7 \\ 0 & 8 \end{pmatrix} = \B\A \), and each is diagonalizable, having two distinct eigenvalues. They even share the eigenbasis \( \e_1, (1,1) \): \( \A(1,1) = 2(1,1) \) and \( \B(1,1) = 4(1,1) \). But that basis is not orthogonal, and no orthonormal one exists, because an orthonormal eigenbasis would make \( \A \) normal (@cor-spectral-complex-matrix), whereas
\[
\A^{*}\A = \begin{pmatrix} 1 & 1 \\ 1 & 5 \end{pmatrix} \neq \begin{pmatrix} 2 & 2 \\ 2 & 4 \end{pmatrix} = \A\A^{*} .
\]

*Normal is not enough.* The matrices \( \X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) and \( \Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \) are real symmetric, hence normal, and each is orthogonally diagonalizable on its own. They do not commute:
\[
\X\Z = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \neq \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = \Z\X .
\]
In fact they share no eigenvector at all: the eigenvectors of \( \Z \) are the multiples of \( \e_1 \) and of \( \e_2 \), and \( \X\e_1 = \e_2 \) is a multiple of neither.
:::

## Sums and products stay normal

Normality is not preserved by addition or multiplication. It is preserved by both as soon as the two operators commute, and the common eigenbasis makes this a one-line matter.

::: {#thm-commuting-normal-sum-normal}
[Sums and Products of Commuting Normal Operators]

Let \( V \) be a finite-dimensional complex inner product space and let \( S, T \in \cL(V) \) be normal with \( ST = TS \). Then \( S + T \) and \( ST \) are normal.
:::

::: {.proof}
If \( V = \{\0\} \) there is nothing to prove. Otherwise apply @thm-simultaneous-unitary-diagonalization to the family \( \{S, T\} \): there is an orthonormal basis \( \sB \) with \( [S]_{\sB} = \D \) and \( [T]_{\sB} = \D' \) both diagonal. Then \( [S+T]_{\sB} = \D + \D' \) and \( [ST]_{\sB} = \D\D' \) are diagonal, so every vector of \( \sB \) is an eigenvector of both operators, and both are normal by @thm-spectral-complex.
:::

::: {.remark}
Commutativity is essential, not a convenience. Take \( \M = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \), which is symmetric, and \( \N = \diag(1, 2i) \), which is diagonal; both are normal and they do not commute. Then
\[
\M + \N = \begin{pmatrix} 1 & 1 \\ 1 & 2i \end{pmatrix},
\qquad
\M\N = \begin{pmatrix} 0 & 2i \\ 1 & 0 \end{pmatrix},
\]
and neither is normal: for the sum, \( (\M+\N)(\M+\N)^{*} \) has \( (1,2) \) entry \( 1 - 2i \) while \( (\M+\N)^{*}(\M+\N) \) has \( 1 + 2i \) there; for the product, \( (\M\N)(\M\N)^{*} = \diag(4,1) \) while \( (\M\N)^{*}(\M\N) = \diag(1,4) \).
:::

::: {.check}
Let \( \A \in M_n(\nC) \) be normal and let \( p \in \nC[x] \). Explain, without using @thm-simultaneous-unitary-diagonalization, why \( \A \) and \( p(\A) \) are simultaneously unitarily diagonalizable.
:::

::: {.solution}
By @cor-spectral-complex-matrix, \( \A = \U\D\U^{*} \) with \( \U \) unitary and \( \D \) diagonal. Then \( \A^m = \U\D^m\U^{*} \) for every \( m \ge 0 \), since the inner factors \( \U^{*}\U \) cancel, so \( p(\A) = \U p(\D)\U^{*} \), and \( p(\D) = \diag(p(d_1), \dots, p(d_n)) \) is diagonal. The *same* \( \U \) diagonalizes both. This is consistent with the theorem, since \( \A \) and \( p(\A) \) commute and \( p(\A) \) is normal, being unitarily diagonalizable.
:::

## Without normality: simultaneous triangularization

If we ask only for triangular matrices, normality may be dropped entirely. Chapter 8 proved this with ordinary bases (@thm-simultaneous-triangularization); over \( \nC \) an inner product upgrades the basis to an orthonormal one, exactly as @thm-schur-triangularization upgraded @thm-triangularization.

::: {#thm-simultaneous-unitary-triangularization}
[Simultaneous Unitary Triangularization]

Let \( V \neq \{\0\} \) be a finite-dimensional complex inner product space and let \( \cF \subseteq \cL(V) \) be a non-empty commuting family. Then there is an orthonormal basis \( \sB \) of \( V \) such that \( [T]_{\sB} \) is upper triangular for **every** \( T \in \cF \). In particular, if \( \A_1, \dots, \A_r \in M_n(\nC) \) commute pairwise, there is \( \U \in \Unit(n) \) with every \( \U^{*}\A_i\U \) upper triangular.
:::

::: {.idea}
The same swap that proves Schur's theorem (@thm-schur-triangularization). A common eigenvector \( \v \) of \( \cF \) gives an invariant line, but \( \Span(\v)^{\perp} \) need not be invariant, so the recursion has nowhere to go. Take instead a common eigenvector \( \u \) of the **adjoints** \( T^{*} \): they commute too, and \( \Span(\u)^{\perp} \) *is* invariant under every \( T \in \cF \). Recurse there, and put \( \u \) at the **end** of the basis, where an upper triangular matrix allows an arbitrary column.
:::

::: {.proof}
Induction on \( n = \dim V \ge 1 \). For \( n = 1 \) every \( 1 \times 1 \) matrix is upper triangular, and a unit vector is an orthonormal basis.

Let \( n \ge 2 \) and assume the theorem in dimension \( n - 1 \). The family \( \cF^{*} = \{T^{*} : T \in \cF\} \) is commuting: for \( S, T \in \cF \), \( S^{*}T^{*} = (TS)^{*} = (ST)^{*} = T^{*}S^{*} \) by @thm-adjoint-properties. Since \( V \) is a complex space, @thm-commuting-common-eigenvector provides \( \u \neq \0 \) with \( T^{*}\u = \nu_T\u \) for every \( T \in \cF \); dividing by \( \norm{\u} \), take \( \norm{\u} = 1 \).

Put \( W = \Span(\u) \) and \( U = W^{\perp} \), of dimension \( n - 1 \) by @thm-orthogonal-decomposition (c). For each \( T \in \cF \) the line \( W \) is \( T^{*} \)-invariant, since \( T^{*}\u = \nu_T\u \), so \( U \) is \( T \)-invariant by @lem-adjoint-eigenline-complement. The family \( \{T|_U : T \in \cF\} \) is commuting, by the same computation on restrictions as in the proof of @thm-simultaneous-unitary-diagonalization. By the inductive hypothesis there is an orthonormal basis \( (\v_1, \dots, \v_{n-1}) \) of \( U \) in which every \( [T|_U] \) is upper triangular.

Let \( \sB = (\v_1, \dots, \v_{n-1}, \u) \). It is orthonormal, since \( \u \) is a unit vector orthogonal to \( U \), and it has \( n \) vectors, so it is an orthonormal basis of \( V \). Fix \( T \in \cF \). For \( j \le n-1 \), \( T\v_j = T|_U\v_j \in \Span(\v_1, \dots, \v_j) \), because the matrix of \( T|_U \) is upper triangular; so the \( j \)-th column of \( [T]_{\sB} \) has zeros below row \( j \). The last column is unconstrained, and an upper triangular matrix permits any entries there. Hence \( [T]_{\sB} \) is upper triangular, which completes the induction.

For the matrix statement, apply this to the operators \( T_{\A_i} \) on \( \nC^n \) and let \( \U \) have the vectors of \( \sB \) as columns, as in @cor-simultaneous-unitary-matrix.
:::

The order matters: the common eigenvector of the adjoints goes last, and the triangular shape is built from the bottom right corner upward. Running the same recursion with a common eigenvector of \( \cF \) itself and putting it first would work only if \( \Span(\v)^{\perp} \) were invariant, which is the extra fact that normality supplies and a bare commuting family does not.

## Exercises

### A. Check your understanding

::: {#exr-commuting-normal-families-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State @thm-simultaneous-unitary-diagonalization, naming every hypothesis.
2. Which result of Chapter 8 makes the eigenspaces of one member invariant under the others, and which hypothesis does it use?
3. Why is the restriction of a normal operator to an invariant subspace again normal, and which earlier result says so? Why does the same fail for a subspace that is not invariant?
4. True or false: two commuting diagonalizable matrices are simultaneously **unitarily** diagonalizable. Justify your answer.
5. True or false: if \( S \) and \( T \) are normal then \( S + T \) is normal. Justify your answer.
6. Which hypothesis of @thm-simultaneous-unitary-diagonalization is dropped in @thm-simultaneous-unitary-triangularization, and what is lost in the conclusion?
:::
:::

::: {.solution}
(a) Let \( V \neq \{\0\} \) be a finite-dimensional **complex** inner product space and \( \cF \subseteq \cL(V) \) a **non-empty** family of **normal** operators that **commute pairwise**. Then \( V \) has an orthonormal basis of common eigenvectors.

(b) @thm-commuting-preserves-eigenspaces: if \( ST = TS \), then \( E_\lambda(T) \) is \( S \)-invariant. The only hypothesis is that the two operators commute.

(c) @prp-normal-invariant-reducing: in an orthonormal basis adapted to \( U \) the matrix of a normal \( T \) is \( \A = \begin{pmatrix} \B & \C \\ \0 & \D \end{pmatrix} \), and comparing the traces of the \( (1,1) \) blocks of \( \A^{*}\A \) and \( \A\A^{*} \) forces \( \C = \0 \); the matrix is then block diagonal and its first block is normal. For a subspace that is not invariant the zero block below is absent and the argument collapses: the Section 3 warning compresses the \( 3 \times 3 \) cyclic shift to \( \Span(\e_1, \e_2) \) and gets a non-normal \( 2 \times 2 \) matrix.

(d) False. \( \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix} \) and \( \begin{pmatrix} 1 & 3 \\ 0 & 4 \end{pmatrix} \) commute and are diagonalizable, but the first is not normal, so it has no orthonormal eigenbasis at all (@cor-spectral-complex-matrix). Simultaneous diagonalization by an invertible matrix is all that Chapter 8 promises (@thm-simultaneous-diagonalization).

(e) False in general, true when they commute (@thm-commuting-normal-sum-normal). For a counterexample take \( \begin{pmatrix} 0&1\\1&0 \end{pmatrix} \) and \( \diag(1, 2i) \), as in the Remark after that theorem.

(f) Normality. What is lost is that the common matrices are only upper triangular, not diagonal.
:::

### B. Practice

::: {#exr-commuting-normal-families-b1}
[B1: Diagonalize two at once]

Let
\[
\A = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix},
\qquad
\B = \begin{pmatrix} 2 & 0 & -2 \\ 0 & 2 & -2 \\ -2 & -2 & 4 \end{pmatrix} \in M_3(\nR) .
\]

::: {.enumerate options="label=(\alph*)"}
1. Verify that \( \A\B = \B\A \) and that both are symmetric.
2. Find \( \Q \in \Orth(3) \) with \( \Q\tp\A\Q \) and \( \Q\tp\B\Q \) both diagonal, and write down the two diagonal matrices.
3. Explain why \( \A \) on its own does not determine \( \Q \) up to permuting and rescaling columns, but the pair does.
:::
:::

::: {.solution}
(a) Both are equal to their transposes by inspection. Each row of \( \B \) sums to \( 0 \) and each column too, so \( \1\1\tp\B = \0 = \B\1\1\tp \) where \( \1 = (1,1,1) \). Since \( \A = \1\1\tp + \I_3 \), we get \( \A\B = \B = \B\A \). (Direct multiplication confirms \( \A\B = \B \).)

(b) The eigenvectors of \( \A = \1\1\tp + \I_3 \) are \( \1 \), with \( \A\1 = 3\1 + \1 = 4\1 \), and every \( \v \) with \( v_1 + v_2 + v_3 = 0 \), with \( \A\v = \v \). Inside that plane we search with \( \B \):
\[
\begin{aligned}
\B(1,-1,0) &= (2,-2,0) = 2(1,-1,0), \\
\B(1,1,-2) &= (6,6,-12) = 6(1,1,-2),
\end{aligned}
\]
and both vectors have coordinate sum \( 0 \). Also \( \B\1 = \0 \). The three vectors \( \1 \), \( (1,-1,0) \), \( (1,1,-2) \) are pairwise orthogonal, as one checks from \( 1 - 1 + 0 = 0 \), \( 1 + 1 - 2 = 0 \) and \( 1 - 1 + 0 = 0 \). Normalizing,
\[
\Q = \begin{pmatrix}
 1/\sqrt3 & 1/\sqrt2 & 1/\sqrt6 \\
 1/\sqrt3 & -1/\sqrt2 & 1/\sqrt6 \\
 1/\sqrt3 & 0 & -2/\sqrt6
\end{pmatrix},
\]
and \( \Q\tp\A\Q = \diag(4, 1, 1) \), \( \Q\tp\B\Q = \diag(0, 2, 6) \).

(c) The eigenvalue \( 1 \) of \( \A \) has a two-dimensional eigenspace, so *every* orthonormal basis of that plane serves \( \A \) equally well, and there are infinitely many, not obtained from one another by permuting and rescaling columns. The matrix \( \B \) has three distinct eigenvalues, so its eigenlines are determined, and the pair therefore determines the three lines of \( \Q \) up to order and sign.
:::

::: {#exr-commuting-normal-families-b2}
[B2: Check the two warnings]

::: {.enumerate options="label=(\alph*)"}
1. For \( \A = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix} \) and \( \B = \begin{pmatrix} 1 & 3 \\ 0 & 4 \end{pmatrix} \), find an invertible \( \P \) with \( \P^{-1}\A\P \) and \( \P^{-1}\B\P \) diagonal, and show that no **unitary** \( \P \) does this.
2. For \( \X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) and \( \Z = \diag(1,-1) \), write down an orthogonal \( \Q_1 \) diagonalizing \( \X \) and an orthogonal \( \Q_2 \) diagonalizing \( \Z \), and prove that no single invertible matrix diagonalizes both.
:::
:::

::: {.solution}
(a) The common eigenvectors are \( \e_1 \) (eigenvalues \( 1 \) and \( 1 \)) and \( (1,1) \) (eigenvalues \( 2 \) and \( 4 \)): \( \A(1,1) = (2,2) \) and \( \B(1,1) = (4,4) \). So \( \P = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) works, with \( \P^{-1}\A\P = \diag(1,2) \) and \( \P^{-1}\B\P = \diag(1,4) \). If a unitary \( \P \) did the same, then \( \A = \P\D\P^{*} \) with \( \D \) diagonal would be normal by @cor-spectral-complex-matrix; but \( \A^{*}\A = \begin{pmatrix} 1&1\\1&5 \end{pmatrix} \) and \( \A\A^{*} = \begin{pmatrix} 2&2\\2&4 \end{pmatrix} \) differ in every entry.

(b) \( \X \) has eigenvectors \( (1,1) \) and \( (1,-1) \) for the eigenvalues \( 1 \) and \( -1 \), so \( \Q_1 = \tfrac1{\sqrt2}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \) gives \( \Q_1\tp\X\Q_1 = \diag(1,-1) \). \( \Z \) is already diagonal, so \( \Q_2 = \I_2 \). No single invertible \( \P \) diagonalizes both: if it did, then \( \P^{-1}\X\P \) and \( \P^{-1}\Z\P \) would be diagonal, hence commuting, and multiplying by \( \P \) and \( \P^{-1} \) would give \( \X\Z = \Z\X \). But \( \X\Z = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \) and \( \Z\X = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} \).
:::

::: {#exr-commuting-normal-families-b3}
[B3: Triangularize two at once]

Let \( \A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) and \( \B = \begin{pmatrix} 2 & 3 \\ 0 & 2 \end{pmatrix} \) in \( M_2(\nC) \).

::: {.enumerate options="label=(\alph*)"}
1. Verify that \( \A\B = \B\A \).
2. Determine whether \( \A \) and \( \B \) are simultaneously diagonalizable, and justify your answer.
3. Exhibit a unitary \( \U \) with \( \U^{*}\A\U \) and \( \U^{*}\B\U \) both upper triangular, as @thm-simultaneous-unitary-triangularization promises.
:::
:::

::: {.solution}
(a) \( \A\B = \begin{pmatrix} 2 & 5 \\ 0 & 2 \end{pmatrix} = \B\A \).

(b) No. If one basis made both diagonal, then \( \A \) alone would be diagonalizable; but \( p_{\A} = (x-1)^2 \) and \( \A - \I_2 = \begin{pmatrix} 0&1\\0&0 \end{pmatrix} \neq \0 \), so \( \A \) has the single eigenvalue \( 1 \) with a one-dimensional eigenspace, and is not diagonalizable. This is the hypothesis that @thm-simultaneous-diagonalization needs and that commuting does not supply.

(c) \( \U = \I_2 \): both matrices are already upper triangular in the standard basis, which is orthonormal. The content of the theorem is that such a basis always exists, not that it is hard to find in this example.
:::

### C. Going deeper

::: {#exr-commuting-normal-families-c1}
[C1: A special case of a theorem of Fuglede]

Let \( V \) be a finite-dimensional complex inner product space and let \( S, T \in \cL(V) \) be **both normal**, with \( ST = TS \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( ST^{*} = T^{*}S \) and \( S^{*}T = TS^{*} \).
2. Deduce that \( S + T^{*} \) and \( ST^{*} \) are normal.
3. Give an example of two commuting operators, **not** both normal, for which the conclusion of (a) fails as stated for the pair — that is, exhibit commuting \( S, T \) with \( ST^{*} \neq T^{*}S \).
:::

Note on the hypotheses: a theorem of Fuglede says that in (a) the operator \( S \) need not be assumed normal — it is enough that \( T \) be normal and that \( S \) commute with \( T \). That stronger statement is true and is not proved in this book; (a) is only the case in which both are normal, and its proof uses the normality of \( S \) in an essential way.
:::

::: {.solution}
(a) By @thm-simultaneous-unitary-diagonalization applied to the commuting family \( \{S, T\} \) of normal operators, there is an orthonormal basis \( \sB \) with \( [S]_{\sB} = \D \) and \( [T]_{\sB} = \D' \) diagonal. By @thm-matrix-of-adjoint, \( [T^{*}]_{\sB} = (\D')^{*} \), which is the diagonal matrix with the conjugated entries. Diagonal matrices commute, so
\[
[ST^{*}]_{\sB} = \D(\D')^{*} = (\D')^{*}\D = [T^{*}S]_{\sB},
\]
and \( ST^{*} = T^{*}S \) because a map is determined by its matrix (@thm-linear-maps-isomorphic-to-matrices). Exchanging the roles of \( S \) and \( T \) gives \( TS^{*} = S^{*}T \).

(b) \( T^{*} \) is normal, since \( (T^{*})^{*}T^{*} = TT^{*} = T^{*}T = T^{*}(T^{*})^{*} \). By (a), \( S \) and \( T^{*} \) commute, and both are normal, so @thm-commuting-normal-sum-normal applies to the pair \( (S, T^{*}) \) and gives that \( S + T^{*} \) and \( ST^{*} \) are normal.

(c) Take \( S = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) and \( T = \I_2 \). They commute, \( T \) is normal, and \( S \) is not. Here \( ST^{*} = S = T^{*}S \), so this pair does not refute anything — as the theorem of Fuglede predicts, since \( T \) is normal. Take instead \( T = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) and \( S = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \), which commute, since both are polynomials in \( T \). Then
\[
ST^{*} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix},
\qquad
T^{*}S = \begin{pmatrix} 0 & 0 \\ 1 & 1 \end{pmatrix},
\]
which differ. Here it is \( T \), not \( S \), that fails to be normal, and that is exactly the hypothesis the theorem of Fuglede keeps.
:::

::: {#exr-commuting-normal-families-c2}
[C2: A commuting family of orthogonal projections]

Let \( V \neq \{\0\} \) be a finite-dimensional inner product space over \( F = \nR \) or \( \nC \), and let \( P_1, \dots, P_r \in \cL(V) \) be the orthogonal projections onto subspaces \( U_1, \dots, U_r \), pairwise commuting.

::: {.enumerate options="label=(\alph*)"}
1. Prove that there is an orthonormal basis \( \sB \) of \( V \) such that every vector of \( \sB \) lies in \( U_i \) or in \( U_i^{\perp} \), for every \( i \).
2. Deduce that \( P_iP_j \) is the orthogonal projection onto \( U_i \cap U_j \).
3. Prove that \( P_i + P_j \) is an orthogonal projection if and only if \( U_i \perp U_j \), and identify the subspace in that case.
:::

*Hint for (a): the eigenvalues of an idempotent operator.*
:::

::: {.solution}
(a) Each \( P_i \) is self-adjoint, by @exm-adjoint-matrix-maps (d). Over \( \nR \), @cor-simultaneous-orthogonal-real applies directly to the commuting family \( \{P_1, \dots, P_r\} \); over \( \nC \) a self-adjoint operator is normal, since \( P^{*}P = P^2 = PP^{*} \), so @thm-simultaneous-unitary-diagonalization applies. Either way there is an orthonormal basis \( \sB \) of common eigenvectors. Let \( \v \in \sB \) and fix \( i \). If \( P_i\v = \mu\v \), then \( \mu^2\v = P_i^2\v = P_i\v = \mu\v \), so \( \mu \in \{0, 1\} \), since \( \v \neq \0 \). If \( \mu = 1 \) then \( \v = P_i\v \in \im P_i = U_i \); if \( \mu = 0 \) then \( \v \in \ker P_i = U_i^{\perp} \) (@def-orthogonal-projection).

(b) Write \( \sB = (\v_1, \dots, \v_n) \) and let \( W = U_i \cap U_j \). By (a) each \( \v_t \) satisfies \( P_i\v_t = a_t\v_t \) and \( P_j\v_t = b_t\v_t \) with \( a_t, b_t \in \{0,1\} \), so \( P_iP_j\v_t = a_tb_t\v_t \), which is \( \v_t \) when \( \v_t \in U_i \cap U_j \) and \( \0 \) otherwise. Let \( L = \Span\{\v_t : a_tb_t = 1\} \); then \( L \subseteq W \). Conversely, if \( \w \in W \), expand \( \w = \sum_t c_t\v_t \); applying \( P_i \) gives \( \w = \sum_t a_tc_t\v_t \), so \( c_t = a_tc_t \) and hence \( c_t = 0 \) whenever \( a_t = 0 \), and likewise for \( b_t \). So \( \w \in L \) and \( W = L \). Now \( P_iP_j \) fixes each \( \v_t \in L \) and kills the rest, and by @thm-projection-formula (a) with the orthonormal basis \( \{\v_t : a_tb_t = 1\} \) of \( W \), so does \( P_W \); two operators agreeing on a basis are equal, so \( P_iP_j = P_W \).

(c) Write \( Q = P_i + P_j \).

\( (\Rightarrow) \) Suppose \( Q \) is the orthogonal projection onto some subspace \( W \). Then \( Q^2 = Q \) (@def-orthogonal-projection), and expanding,
\[
P_i + P_j = Q^2 = P_i^2 + P_iP_j + P_jP_i + P_j^2 = P_i + P_j + 2P_iP_j ,
\]
using \( P_i^2 = P_i \), \( P_j^2 = P_j \) and \( P_jP_i = P_iP_j \). Hence \( 2P_iP_j = 0 \), so \( P_iP_j = 0 \). Now let \( \v \in U_j \); then \( P_i\v = P_i(P_j\v) = \0 \), so \( \v \in \ker P_i = U_i^{\perp} \). Therefore \( U_j \subseteq U_i^{\perp} \), which says \( U_i \perp U_j \).

\( (\Leftarrow) \) Suppose \( U_i \perp U_j \), so \( U_j \subseteq U_i^{\perp} = \ker P_i \) and \( U_i \subseteq \ker P_j \). For \( \v \in U_i \) we get \( Q\v = \v + \0 = \v \), and symmetrically \( Q\v = \v \) for \( \v \in U_j \), so \( Q \) is the identity on \( U_i \oplus U_j \). For \( \v \in (U_i \oplus U_j)^{\perp} = U_i^{\perp} \cap U_j^{\perp} \) we get \( Q\v = \0 + \0 = \0 \). Since \( V = (U_i \oplus U_j) \oplus (U_i \oplus U_j)^{\perp} \) by @thm-orthogonal-decomposition (a), \( Q \) agrees with \( P_{U_i \oplus U_j} \) on both summands, hence everywhere. So \( P_i + P_j = P_{U_i \oplus U_j} \).
:::
