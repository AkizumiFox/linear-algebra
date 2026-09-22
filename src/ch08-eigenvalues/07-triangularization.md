# Triangularization

Section 4 found two ways for diagonalization to fail. The field can be too small, as for a rotation of \( \nR^2 \). Or there can be too few eigenvectors, as for \( \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \), and no change of field helps. In the second case we should ask for less. The next simplest shape after a diagonal matrix is an upper triangular one, and triangular matrices are almost as good for computation: their eigenvalues, trace and determinant are visible on the diagonal. This section proves that an operator has a triangular matrix exactly when its characteristic polynomial splits, so every complex matrix is similar to a triangular one. The proof is the induction on dimension that Section 1 promised: take one eigenvector, pass to the quotient, and repeat.

## Triangular matrices and chains of invariant subspaces

As in Section 2, start with the wish and unwind it. Let \( \sB = (\v_1, \dots, \v_n) \) be a basis of \( V \) and \( T \in \cL(V) \). Column \( j \) of \( \mtx{T}{\sB}{\sB} \) holds the coordinates of \( T\v_j \) (@def-matrix-of-linear-map). The matrix is upper triangular when every entry below the diagonal is \( 0 \) (@def-upper-triangular), that is, when \( T\v_j \) is a combination of \( \v_1, \dots, \v_j \) only. So the first basis vector must be sent to a multiple of itself, the second into the plane of the first two, and so on. In the language of Section 1, each of the growing spans must be invariant. Chapter 3 proved this as an exercise (@exr-matrix-of-a-map-c1), where the word *invariant* was introduced just for that problem; here it is again, with one more piece of information about the diagonal.

::: {#thm-triangular-iff-flag}
[Triangular Matrices and Chains of Invariant Subspaces]

Let \( V \) be finite-dimensional with basis \( \sB = (\v_1, \dots, \v_n) \), let \( T \in \cL(V) \), and put \( U_0 = \{\0\} \) and \( U_k = \Span(\v_1, \dots, \v_k) \) for \( 1 \le k \le n \). The following are equivalent:

::: {.enumerate options="label=(\alph*)"}
1. \( \mtx{T}{\sB}{\sB} \) is upper triangular;
2. \( T\v_k \in U_k \) for every \( k = 1, \dots, n \);
3. each \( U_k \) is \( T \)-invariant.
:::

In that case, if \( d_1, \dots, d_n \) are the diagonal entries of \( \mtx{T}{\sB}{\sB} \), then \( (T - d_k\,\id_V)(U_k) \subseteq U_{k-1} \) for every \( k \).
:::

::: {.proof}
Write \( \mtx{T}{\sB}{\sB} = (a_{ij}) \), so that \( T\v_j = \sum_i a_{ij}\v_i \) with unique coefficients (@def-matrix-of-linear-map, @thm-unique-representation).

(a) \( \Leftrightarrow \) (b). If \( a_{ij} = 0 \) for \( i > j \), then \( T\v_j = \sum_{i \le j} a_{ij}\v_i \in U_j \). Conversely, if \( T\v_j \in U_j \), it has a representation using only \( \v_1, \dots, \v_j \); by uniqueness, \( a_{ij} = 0 \) for \( i > j \).

(b) \( \Rightarrow \) (c). For \( j \le k \), \( T\v_j \in U_j \subseteq U_k \), so \( U_k \) is invariant by @lem-invariance-on-spanning-list.

(c) \( \Rightarrow \) (b). \( \v_k \in U_k \), so \( T\v_k \in U_k \) by invariance.

Finally, suppose (a) holds and let \( \u = \sum_{j \le k} b_j\v_j \in U_k \). For \( j < k \), \( (T - d_k\,\id_V)\v_j = T\v_j - d_k\v_j \in U_j \subseteq U_{k-1} \). For \( j = k \), \( (T - d_k\,\id_V)\v_k = \sum_{i \le k} a_{ik}\v_i - a_{kk}\v_k = \sum_{i < k} a_{ik}\v_i \in U_{k-1} \), since \( d_k = a_{kk} \). By linearity, \( (T - d_k\,\id_V)\u \in U_{k-1} \).
:::

A chain \( U_1 \subset U_2 \subset \dots \subset U_n = V \) of subspaces with \( \dim U_k = k \) is often called a **flag**, after the picture of a point on a line in a plane in space. The theorem says: an upper triangular matrix is the same thing as a flag of invariant subspaces, together with a basis adapted to it. The last statement says what the diagonal entry \( d_k \) measures. Modulo the smaller space \( U_{k-1} \), the operator \( T \) acts on the new basis vector \( \v_k \) as multiplication by \( d_k \).

The operators for which such a basis exists deserve a name.

::: {#def-triangularizable}
[Triangularizable]

Let \( V \) be a finite-dimensional vector space over \( F \). An operator \( T \in \cL(V) \) is **triangularizable over \( F \)** if there **exists** a basis \( \sB \) of \( V \) such that \( \mtx{T}{\sB}{\sB} \) is upper triangular. A matrix \( \A \in M_n(F) \) is **triangularizable over \( F \)** if there **exist** an **invertible** \( \P \in M_n(F) \) and an upper triangular \( \U \in M_n(F) \) with \( \P^{-1}\A \P = \U \).
:::

As for diagonalizability, \( \A \) is triangularizable over \( F \) exactly when \( T_{\A} \) is, by @thm-similar-iff-same-operator.

**Examples.**

- **Diagonalizable operators** are triangularizable, since a diagonal matrix is upper triangular. So are all operators on a space of dimension \( 1 \), and the zero and identity operators.
- **Differentiation.** For \( D \) on \( \nR[x]_{\le n} \) in the basis \( (1, x, \dots, x^n) \), the matrix is upper triangular with zero diagonal: \( D(x^k) = kx^{k-1} \in \Span(1, \dots, x^k) \). The flag is \( \nR[x]_{\le 0} \subset \nR[x]_{\le 1} \subset \dots \subset \nR[x]_{\le n} \), a chain of invariant subspaces we met in Section 1. \( D \) is not diagonalizable (its only eigenvectors are the constants), but it is triangularizable.
- **Too few eigenvectors.** \( \J = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) is already triangular, with flag \( \Span(\e_1) \subset F^2 \).

**Non-example by minimal change.** Reverse the basis for \( D \) on \( \nR[x]_{\le 2} \): take \( (x^2, x, 1) \). The spans are \( \Span(x^2) \subset \Span(x^2, x) \subset \nR[x]_{\le 2} \), still a chain of subspaces of dimensions \( 1, 2, 3 \). What fails is invariance of the first one: \( D(x^2) = 2x \notin \Span(x^2) \). Accordingly, the matrix in this basis is
\[
\begin{pmatrix} 0 & 0 & 0 \\ 2 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix},
\]
which is lower triangular, not upper. Being triangularizable is a property of \( T \); being triangular is a property of \( T \) **and** a basis.

A triangularizable operator on \( V \ne \{\0\} \) must have an invariant line \( U_1 = \Span(\v_1) \), hence an eigenvector (@prp-one-dimensional-invariant). So the rotation \( R \) of \( \nR^2 \) by a right angle, which has no invariant line (@exm-rotation-invariant-subspaces), is **not** triangularizable over \( \nR \). An eigenvector to start the flag is exactly what is needed, and the next theorem shows that it is also enough, provided eigenvectors keep existing at every stage.

::: {.check}
Is \( \begin{pmatrix} 2 & 0 \\ 1 & 2 \end{pmatrix} \in M_2(\nR) \) triangularizable over \( \nR \)? If so, find a basis in which its matrix is upper triangular.
:::

::: {.solution}
Yes. We need a first basis vector that is an eigenvector. The matrix sends \( \e_2 \) to \( (0, 2) = 2\e_2 \), so start with \( \e_2 \), and complete with \( \e_1 \). In the basis \( (\e_2, \e_1) \), the image of \( \e_2 \) is \( 2\e_2 \) and the image of \( \e_1 \) is \( (2, 1) = \e_2 + 2\e_1 \), so the matrix is \( \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} \), which is upper triangular. (The standard basis gives a lower triangular matrix: \( \Span(\e_1) \) is not invariant.)
:::

## The Triangularization Theorem

If \( T \) has a triangular matrix, its characteristic polynomial is a product of linear factors, one for each diagonal entry. The converse is the real content: splitting of \( p_T \) is enough to build the flag.

::: {#thm-triangularization}
[Triangularization Theorem]

Let \( V \) be a finite-dimensional vector space over \( F \) with \( \dim V = n \ge 1 \), and let \( T \in \cL(V) \). Then \( T \) is triangularizable over \( F \) if and only if \( p_T \) splits over \( F \). The same holds for \( \A \in M_n(F) \) and \( p_{\A} \).
:::

::: {.idea}
Take one eigenvector, extend, recurse. Since \( p_T \) splits, it has a root in \( F \), so \( T \) has an eigenvector \( \v_1 \). Put \( U = \Span(\v_1) \) and extend \( \v_1 \) to a basis \( \sB \), with \( \bar\sB \) the basis it induces on \( V/U \). By @thm-invariant-subspace-matrix the matrix looks like
\[
\mtx{T}{\sB}{\sB} = \begin{pmatrix} \lambda & \ast \\ 0 & \mtx{\bar T}{\bar\sB}{\bar\sB} \end{pmatrix},
\]
where \( \bar T \) is the induced operator on the smaller space \( V/U \). The first column is already right. If \( \mtx{\bar T}{\bar\sB}{\bar\sB} \) could be made triangular, the whole matrix would be. Now \( \bar T \) lives on a space of dimension \( n - 1 \), and \( p_T = (x - \lambda)\,p_{\bar T} \), so \( p_{\bar T} \) splits too: this is the induction on dimension. The only technical point is that a basis of \( V/U \) lifts to vectors that, together with \( \v_1 \), form a basis of \( V \).
:::

::: {.proof}
\( (\Rightarrow) \) Let \( \mtx{T}{\sB}{\sB} \) be upper triangular with diagonal entries \( d_1, \dots, d_n \). The matrix \( x\I_n - \mtx{T}{\sB}{\sB} \) is upper triangular with diagonal entries \( x - d_i \), and @thm-det-triangular holds over \( F[x] \) (the remark at the end of Chapter 6, §4). So \( p_T = (x - d_1)\cdots(x - d_n) \) by @def-charpoly-operator, which splits (@def-polynomial-splits).

\( (\Leftarrow) \) We prove, by induction on \( n \ge 1 \), that every operator on an \( n \)-dimensional space whose characteristic polynomial splits is triangularizable. For \( n = 1 \), every \( 1 \times 1 \) matrix is upper triangular.

Let \( n \ge 2 \), and assume the statement for spaces of dimension \( n - 1 \). Since \( p_T \) is monic of degree \( n \) (@thm-charpoly-coefficients) and splits, \( p_T = (x - c_1)(x - c_2)\cdots(x - c_n) \) with \( c_i \in F \). As \( p_T(c_1) = 0 \), @thm-eigenvalue-characterizations gives an eigenvector \( \v_1 \) with \( T\v_1 = c_1\v_1 \). Let \( U = \Span(\v_1) \). It is \( T \)-invariant (@prp-one-dimensional-invariant), \( \dim U = 1 \), and \( U \ne V \) since \( n \ge 2 \). Let \( \bar T \) be the induced operator on \( V/U \) (@def-restriction-operator), a space of dimension \( n - 1 \ge 1 \) (@thm-dimension-quotient).

*\( p_{\bar T} \) splits.* The restriction \( T|_U \) is \( c_1\,\id_U \), whose matrix in the basis \( (\v_1) \) is \( (c_1) \), so \( p_{T|_U} = x - c_1 \). By @thm-invariant-subspace-matrix (b),
\[
(x - c_1)(x - c_2)\cdots(x - c_n) = p_T = (x - c_1)\,p_{\bar T} .
\]
Canceling the non-zero factor \( x - c_1 \) (@cor-polynomial-no-zero-divisors (2)) gives \( p_{\bar T} = (x - c_2)\cdots(x - c_n) \), which splits.

*Apply the induction hypothesis.* There is a basis \( \bar\sC = (\w_2 + U, \dots, \w_n + U) \) of \( V/U \) with \( \mtx{\bar T}{\bar\sC}{\bar\sC} \) upper triangular, for some \( \w_2, \dots, \w_n \in V \).

*Lift the basis.* Let \( \sB = (\v_1, \w_2, \dots, \w_n) \). Suppose \( a\v_1 + b_2\w_2 + \dots + b_n\w_n = \0 \). Passing to cosets, and using \( \v_1 \in U \), gives \( b_2(\w_2 + U) + \dots + b_n(\w_n + U) = \0 + U \) (@thm-quotient-space-operations-well-defined). Since \( \bar\sC \) is a basis, all \( b_i = 0 \). Then \( a\v_1 = \0 \) with \( \v_1 \ne \0 \), so \( a = 0 \) (@thm-zero-product). Thus \( \sB \) is a linearly independent list of \( n \) vectors in \( V \), hence a basis (@thm-right-size-basis).

*The matrix.* \( \sB \) extends the basis \( (\v_1) \) of \( U \), and the cosets of the added vectors form \( \bar\sC \). By @thm-invariant-subspace-matrix (b),
\[
\mtx{T}{\sB}{\sB} = \begin{pmatrix} c_1 & \ast \\ 0 & \mtx{\bar T}{\bar\sC}{\bar\sC} \end{pmatrix},
\]
where the \( 0 \) is a column of \( n - 1 \) zeros. The block \( \mtx{\bar T}{\bar\sC}{\bar\sC} \) is upper triangular, so \( \mtx{T}{\sB}{\sB} \) is upper triangular. This completes the induction.

For \( \A \in M_n(F) \), apply the result to \( T_{\A} \), using @thm-similar-iff-same-operator.
:::

The proof is an algorithm, and its output is a flag. The first invariant subspace is the eigenline \( U \); the \( k \)-th is spanned by \( \v_1 \) and the lifts \( \w_2, \dots, \w_k \) of the first \( k - 1 \) vectors of the flag for \( \bar T \). The eigenvalue found at each stage is the next diagonal entry.

Over the complex numbers the hypothesis is automatic.

::: {#cor-complex-triangularizable}
[Complex Operators Are Triangularizable]

Every operator on a finite-dimensional complex vector space \( V \ne \{\0\} \) is triangularizable over \( \nC \). Every \( \A \in M_n(\nC) \), \( n \ge 1 \), is similar to an upper triangular matrix in \( M_n(\nC) \).
:::

::: {.proof}
By @thm-charpoly-coefficients, \( p_T \) is non-zero, and by @cor-complex-polynomial-splits (a) it splits over \( \nC \). Apply @thm-triangularization.
:::

So over \( \nC \) the question of Chapter 3 always has at least this answer: a basis exists in which the matrix has zeros below the diagonal. A real matrix can always be triangularized as a complex matrix, but perhaps only with complex entries.

::: {.warning}
**Triangularizing may require leaving the field, and the triangular form is far from unique.** The rotation \( \R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \) has \( p_{\R} = x^2 + 1 \), which does not split over \( \nR \), so no **real** invertible \( \P \) makes \( \P^{-1}\R\P \) triangular; over \( \nC \) it becomes \( \diag(i, -i) \). And a triangularizable matrix has many triangular forms. \( \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix} \) and \( \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix} \) are both triangular forms of the same operator (the first has distinct eigenvalues \( 1, 2 \), so it is diagonalizable, and similar to the second). The off-diagonal entries change with the flag and the basis, and even the order of the diagonal entries is not fixed. Only the diagonal entries, as a list with repetitions, are determined, as the next theorem shows.
:::

## What the diagonal records

A diagonalization displays the eigenvalues. A triangularization does too, with their algebraic multiplicities.

::: {#thm-diagonal-of-triangular-form}
[The Diagonal of a Triangular Form]

Let \( V \) be finite-dimensional with \( \dim V = n \ge 1 \), \( T \in \cL(V) \), and let \( \sB \) be a basis with \( \mtx{T}{\sB}{\sB} \) upper triangular, with diagonal entries \( d_1, \dots, d_n \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( p_T = (x - d_1)(x - d_2)\cdots(x - d_n) \);
2. \( \spec(T) = \{d_1, \dots, d_n\} \), and each eigenvalue \( \lambda \) occurs among \( d_1, \dots, d_n \) exactly \( a_T(\lambda) \) times;
3. \( \tr T = d_1 + \dots + d_n \) and \( \det T = d_1\cdots d_n \).
:::

In particular, any two triangular forms of \( T \) have the same diagonal entries, up to order.
:::

::: {.proof}
(a) was shown in the proof of @thm-triangularization, \( (\Rightarrow) \).

(b) By @thm-eigenvalue-characterizations, the eigenvalues are the roots of \( p_T \) in \( F \), and \( \lambda \) is a root of \( \prod_i (x - d_i) \) exactly when \( \prod_i (\lambda - d_i) = 0 \), that is, when \( \lambda = d_i \) for some \( i \) (@thm-field-basic-properties). By @thm-multiplicity-of-product, \( a_T(\lambda) = \operatorname{mult}_\lambda(p_T) = \sum_i \operatorname{mult}_\lambda(x - d_i) \). Each term is \( 1 \) if \( d_i = \lambda \) and \( 0 \) otherwise, by @thm-remainder-theorem (b), since \( x - d_i \) is not divisible by \( (x - \lambda)^2 \) for degree reasons. So the sum counts the indices with \( d_i = \lambda \).

(c) By @def-trace-operator, \( \tr T = \tr\mtx{T}{\sB}{\sB} = \sum_i d_i \). By @def-det-operator and @thm-det-triangular, \( \det T = \det\mtx{T}{\sB}{\sB} = \prod_i d_i \).

The final statement follows from (b): the number of times \( \lambda \) occurs on the diagonal is \( a_T(\lambda) \), which does not depend on the basis.
:::

Part (c) recovers @thm-trace-det-eigenvalues. In Section 3 it came from comparing coefficients of \( p_T \); here it is read off a matrix. For instance, a complex \( 3 \times 3 \) matrix with \( p_{\A} = (x - 1)^2(x + 4) \) is similar to a triangular matrix with diagonal \( 1, 1, -4 \) in some order, so \( \tr \A = -2 \) and \( \det \A = -4 \), however complicated \( \A \) looks.

The theorem does **not** say that a triangular form with **distinct** diagonal entries is itself diagonal: \( \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix} \) is a counterexample. What does follow is that \( T \) is then diagonalizable (@cor-distinct-eigenvalues-diagonalizable), so some **other** basis makes its matrix diagonal. And an operator with repeated diagonal entries may or may not be diagonalizable: compare \( \I_2 \) with \( \J \).

## Triangularizing a matrix in practice

For a matrix \( \A \in M_n(F) \) whose characteristic polynomial splits, the proof of @thm-triangularization becomes a procedure.

1. Find an eigenvalue \( \lambda_1 \) and an eigenvector \( \v_1 \).
2. Extend \( \v_1 \) to a basis \( (\v_1, \w_2, \dots, \w_n) \) of \( F^n \), choosing the \( \w_i \) as simple as possible, for example standard basis vectors.
3. Compute the matrix of the induced operator on \( F^n/\Span(\v_1) \) in the basis \( (\w_2 + U, \dots, \w_n + U) \). Its entries are the coordinates of \( \A\w_j \) along \( \w_2, \dots, \w_n \), ignoring the \( \v_1 \)-coordinate.
4. Triangularize this \( (n - 1) \times (n - 1) \) matrix in the same way, and lift each coset back to its representative.

::: {#exm-triangularize-3x3}
[Triangularizing a Matrix with a Single Eigenvector Line]

Let
\[
\A = \begin{pmatrix} 2 & 0 & 1 \\ 0 & 2 & 1 \\ 1 & -1 & 2 \end{pmatrix} \in M_3(\nR).
\]
Show that \( \A \) is not diagonalizable but is triangularizable over \( \nR \), and find an invertible \( \P \) with \( \P^{-1}\A \P \) upper triangular.
:::

::: {.solution}
*The characteristic polynomial.* Expanding along the first row (@thm-laplace-expansion over \( \nR[x] \)),
\[
\begin{aligned}
p_{\A} &= \det\begin{pmatrix} x - 2 & 0 & -1 \\ 0 & x - 2 & -1 \\ -1 & 1 & x - 2 \end{pmatrix} \\
  &= (x - 2)\big[(x - 2)^2 + 1\big] + (-1)\det\begin{pmatrix} 0 & x - 2 \\ -1 & 1 \end{pmatrix}.
\end{aligned}
\]
The last determinant is \( 0 \cdot 1 - (x - 2)(-1) = x - 2 \), so \( p_{\A} = (x - 2)\big[(x - 2)^2 + 1 - 1\big] = (x - 2)^3 \). It splits, so \( \A \) is triangularizable by @thm-triangularization.

*Eigenvectors.* \( \A - 2\I = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 1 \\ 1 & -1 & 0 \end{pmatrix} \) has rank \( 2 \), so \( g(2) = 1 < 3 = a(2) \), and \( \A \) is not diagonalizable (@thm-diagonalization (e)). The system gives \( z = 0 \) and \( x = y \), so \( E_2(\A) = \Span(\v_1) \) with \( \v_1 = (1, 1, 0) \): all eigenvectors lie on one line.

*Step 1.* Let \( U = \Span(\v_1) \), and extend to the basis \( (\v_1, \e_2, \e_3) \) of \( \nR^3 \) (the matrix with these columns has determinant \( 1 \)).

*Step 2: the induced operator.* Express the images of \( \e_2 \) and \( \e_3 \) in the basis:
\[
\A\e_2 = (0, 2, -1) = 0\,\v_1 + 2\e_2 - \e_3, \qquad \A\e_3 = (1, 1, 2) = 1\,\v_1 + 0\,\e_2 + 2\e_3 .
\]
Dropping the \( \v_1 \)-coordinates, the induced operator \( \bar \A \) on \( \nR^3/U \) has, in the basis \( \bar\sB = (\e_2 + U, \e_3 + U) \), the matrix
\[
\mtx{\bar \A}{\bar\sB}{\bar\sB} = \begin{pmatrix} 2 & 0 \\ -1 & 2 \end{pmatrix},
\]
with \( p_{\bar \A} = (x - 2)^2 \), as the proof predicts.

*Step 3: triangularize \( \bar \A \).* Its second column says \( \bar \A(\e_3 + U) = 2(\e_3 + U) \), so \( \e_3 + U \) is an eigenvector. In the basis \( (\e_3 + U, \e_2 + U) \), \( \bar \A(\e_2 + U) = -(\e_3 + U) + 2(\e_2 + U) \), and the matrix becomes \( \begin{pmatrix} 2 & -1 \\ 0 & 2 \end{pmatrix} \).

*Step 4: lift.* The basis \( \sB = (\v_1, \e_3, \e_2) \) of \( \nR^3 \) gives
\[
\P = \begin{pmatrix} 1 & 0 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}, \qquad \P^{-1}\A \P = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & -1 \\ 0 & 0 & 2 \end{pmatrix}.
\]
*Check.* \( \A\v_1 = (2, 2, 0) = 2\v_1 \); \( \A\e_3 = (1, 1, 2) = \v_1 + 2\e_3 \); \( \A\e_2 = (0, 2, -1) = -\e_3 + 2\e_2 \). These are the columns \( (2, 0, 0) \), \( (1, 2, 0) \), \( (0, -1, 2) \) of the triangular matrix, read in the basis \( \sB \). Also \( \det \P = -1 \ne 0 \).

The flag is \( \Span((1, 1, 0)) \subset \{ (a, a, b) : a, b \in \nR \} \subset \nR^3 \). One can check the plane directly: \( \A(a, a, b) = (2a + b,\ 2a + b,\ 2b) \) lies in it again. The diagonal is \( 2, 2, 2 \), as @thm-diagonal-of-triangular-form requires.
:::

Different choices in Step 2 give different triangular matrices, with the same diagonal. Chapter 9 shows how to choose the basis so that the entries above the diagonal are as simple as possible (the Jordan form). Chapter 11 shows that over \( \nC \) with an inner product, the basis can even be chosen orthonormal (Schur's theorem).

## Exercises

### A. Check your understanding

:::: {#exr-triangularization-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define what it means for \( \A \in M_n(F) \) to be triangularizable over \( F \).
2. State the Triangularization Theorem.
3. For a basis \( (\v_1, \dots, \v_n) \), which subspaces must be invariant for \( \mtx{T}{\sB}{\sB} \) to be upper triangular?
4. True or false: every \( \A \in M_n(\nR) \) is triangularizable over \( \nR \). Justify your answer.
5. True or false: every triangularizable matrix is diagonalizable. Justify your answer.
6. Let \( \A \in M_4(\nC) \) have \( p_{\A} = (x - 3)^3(x + 1) \). What are the diagonal entries of any upper triangular matrix similar to \( \A \), and what are \( \tr \A \) and \( \det \A \)?
:::
::::

::: {.solution}
(a) There are an invertible \( \P \in M_n(F) \) and an upper triangular \( \U \in M_n(F) \) with \( \P^{-1}\A \P = \U \) (@def-triangularizable).

(b) An operator on a space of dimension \( n \ge 1 \) over \( F \) is triangularizable over \( F \) if and only if its characteristic polynomial splits over \( F \) (@thm-triangularization).

(c) All the spans \( \Span(\v_1, \dots, \v_k) \), \( 1 \le k \le n \) (@thm-triangular-iff-flag).

(d) False. The rotation \( \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \) has \( p = x^2 + 1 \), which does not split over \( \nR \).

(e) False. \( \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) is triangular but not diagonalizable.

(f) By @thm-diagonal-of-triangular-form, the diagonal is \( 3, 3, 3, -1 \) in some order, so \( \tr \A = 8 \) and \( \det \A = -27 \).
:::

### B. Practice

:::: {#exr-triangularization-b1}
[B1: Triangularizing matrices]

For each real matrix, find an invertible \( \P \) such that \( \P^{-1}\A \P \) is upper triangular, and write down \( \P^{-1}\A \P \).

::: {.enumerate options="label=(\alph*)"}
1. \( \A = \begin{pmatrix} 3 & 1 \\ -1 & 1 \end{pmatrix} \).
2. \( \A = \begin{pmatrix} 2 & 0 & 1 \\ 1 & 3 & 1 \\ 1 & 0 & 2 \end{pmatrix} \), with \( p_{\A} = (x - 1)(x - 3)^2 \) (@exm-charpoly-small).
:::
::::

::: {.solution}
(a) \( \tr \A = 4 \), \( \det \A = 4 \), so \( p_{\A} = (x - 2)^2 \), which splits. \( \A - 2\I = \begin{pmatrix} 1 & 1 \\ -1 & -1 \end{pmatrix} \) gives the eigenvector \( \v_1 = (1, -1) \). Extend with \( \e_2 \): \( \A\e_2 = (1, 1) = \v_1 + 2\e_2 \). So with
\[
\P = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix}, \qquad \P^{-1}\A \P = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} .
\]
(In size \( 2 \), one eigenvector already fixes the flag.)

(b) \( \A\e_2 = (0, 3, 0) = 3\e_2 \), so \( \v_1 = \e_2 \) is an eigenvector for \( 3 \). Let \( U = \Span(\e_2) \) and extend to \( (\e_2, \e_1, \e_3) \). Then \( \A\e_1 = (2, 1, 1) = \e_2 + 2\e_1 + \e_3 \) and \( \A\e_3 = (1, 1, 2) = \e_2 + \e_1 + 2\e_3 \), so the induced operator has matrix \( \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \) in the basis \( (\e_1 + U, \e_3 + U) \). Its characteristic polynomial is \( x^2 - 4x + 3 = (x - 3)(x - 1) \), with eigenvectors \( (1, 1) \) for \( 3 \) and \( (1, -1) \) for \( 1 \), that is, \( \e_1 + \e_3 + U \) and \( \e_1 - \e_3 + U \). Lifting gives the basis \( (\e_2,\ \e_1 + \e_3,\ \e_1 - \e_3) \). Now
\[
\begin{aligned}
\A(\e_1 + \e_3) &= (3, 2, 3) = 2\e_2 + 3(\e_1 + \e_3), \\
\A(\e_1 - \e_3) &= (1, 0, -1) = \e_1 - \e_3,
\end{aligned}
\]
so
\[
\P = \begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & -1 \end{pmatrix}, \qquad \P^{-1}\A \P = \begin{pmatrix} 3 & 2 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{pmatrix},
\]
with \( \det \P = 2 \ne 0 \) (expand along the second row). The diagonal \( 3, 3, 1 \) agrees with \( p_{\A} \).
:::

:::: {#exr-triangularization-b2}
[B2: Nilpotent matrices are strictly triangular]

Let \( \A \in M_n(\nC) \), \( n \ge 1 \), with \( \A^k = 0 \) for some \( k \ge 1 \). Prove that \( \A \) is similar to a **strictly** upper triangular matrix, that is, an upper triangular matrix with zero diagonal.
::::

::: {.solution}
By @cor-complex-triangularizable, \( \P^{-1}\A \P = \U \) is upper triangular for some invertible \( \P \). By @thm-diagonal-of-triangular-form (b), each diagonal entry of \( \U \) is an eigenvalue of \( \A \). By @exr-eigenvalues-and-eigenvectors-c2 (a), the only eigenvalue of a nilpotent operator on a non-zero space is \( 0 \). So every diagonal entry of \( \U \) is \( 0 \), and \( \U \) is strictly upper triangular. (The statement holds over every field, with a different proof: use the chain \( \ker \A \subseteq \ker \A^2 \subseteq \dots \subseteq \ker \A^k = F^n \) to build the basis.)
:::

:::: {#exr-triangularization-b3}
[B3: Eigenvalues of powers from a triangular form]

Let \( \A \in M_n(\nC) \), \( n \ge 1 \), and let \( \P^{-1}\A \P = \U \) be upper triangular with diagonal entries \( d_1, \dots, d_n \).

::: {.enumerate options="label=(\alph*)"}
1. Show that the product of two upper triangular matrices is upper triangular, with diagonal entries the products of the corresponding diagonal entries.
2. Deduce that \( p_{\A^k} = (x - d_1^k)\cdots(x - d_n^k) \) and \( \tr(\A^k) = d_1^k + \dots + d_n^k \) for every \( k \ge 1 \).
3. Suppose \( p_{\A} = (x - 1)(x + 1)(x - 2) \). Find \( p_{\A^2} \), \( \tr \A^2 \) and \( \det \A^2 \).
:::
::::

::: {.solution}
(a) Let \( \U, \U' \) be upper triangular. The \( (i, j) \)-entry of \( \U \U' \) is \( \sum_l u_{il}u'_{lj} \). A term can be non-zero only if \( u_{il} \ne 0 \) and \( u'_{lj} \ne 0 \), which forces \( i \le l \le j \). So the entry is \( 0 \) when \( i > j \), and for \( i = j \) only \( l = i \) survives, giving \( u_{ii}u'_{ii} \).

(b) \( \P^{-1}\A^k\P = (\P^{-1}\A \P)^k = \U^k \), by induction on \( k \). By (a) and induction, \( \U^k \) is upper triangular with diagonal entries \( d_i^k \). By @thm-diagonal-of-triangular-form (a) and (c), applied to \( T_{\A^k} \) in the basis given by the columns of \( \P \), \( p_{\A^k} = \prod_i (x - d_i^k) \) and \( \tr \A^k = \sum_i d_i^k \).

(c) By @thm-diagonal-of-triangular-form, the diagonal of \( \U \) is \( 1, -1, 2 \) in some order. By (b), \( p_{\A^2} = (x - 1)(x - 1)(x - 4) = (x - 1)^2(x - 4) \), \( \tr \A^2 = 1 + 1 + 4 = 6 \), and \( \det \A^2 = 1 \cdot 1 \cdot 4 = 4 \). The last agrees with \( \det \A^2 = (\det \A)^2 = (-2)^2 \).
:::

### C. Going deeper

:::: {#exr-triangularization-c1}
[C1: A second proof of Cayley–Hamilton]

Let \( V \) be finite-dimensional with \( \dim V = n \ge 1 \), and let \( T \in \cL(V) \) have a basis \( \sB = (\v_1, \dots, \v_n) \) with \( \mtx{T}{\sB}{\sB} \) upper triangular, with diagonal entries \( d_1, \dots, d_n \). Let \( U_0 = \{\0\} \) and \( U_k = \Span(\v_1, \dots, \v_k) \).

::: {.enumerate options="label=(\alph*)"}
1. Let \( S_k = (T - d_1\,\id_V)(T - d_2\,\id_V)\cdots(T - d_k\,\id_V) \). Prove by induction on \( k \) that \( S_k(U_k) = \{\0\} \) for \( 1 \le k \le n \).
2. Deduce that \( p_T(T) = 0 \), without using the adjugate.
3. Deduce the Cayley–Hamilton Theorem for every \( \A \in M_n(\nC) \), and then for every \( \A \in M_n(\nR) \).
4. Why does this argument, on its own, not prove the theorem for \( \A \in M_2(\nF_2) \) with \( p_{\A} = x^2 + x + 1 \)?
:::

*Hint: for (a), use the last statement of @thm-triangular-iff-flag.*
::::

::: {.solution}
(a) By @thm-triangular-iff-flag, each \( U_k \) is invariant and \( (T - d_k\,\id_V)(U_k) \subseteq U_{k-1} \). For \( k = 1 \), \( S_1(U_1) = (T - d_1\,\id_V)(U_1) \subseteq U_0 = \{\0\} \). Suppose \( S_{k-1}(U_{k-1}) = \{\0\} \) for some \( k \ge 2 \). Since \( S_k = S_{k-1}(T - d_k\,\id_V) \), for \( \u \in U_k \) we get \( S_k\u = S_{k-1}\big((T - d_k\,\id_V)\u\big) \in S_{k-1}(U_{k-1}) = \{\0\} \).

(b) By @thm-diagonal-of-triangular-form (a), \( p_T = \prod_{i=1}^{n}(x - d_i) \), so \( p_T(T) = S_n \) by @thm-evaluation-homomorphism (b). By (a), \( S_n \) kills \( U_n = V \), so \( p_T(T) = 0 \).

(c) Let \( \A \in M_n(\nC) \). By @cor-complex-triangularizable, \( T_{\A} \) has a basis in which its matrix is upper triangular, and (b) gives \( p_{\A}(T_{\A}) = 0 \), so \( p_{\A}(\A) = 0 \) by @cor-matrix-of-polynomial-of-operator. For \( \A \in M_n(\nR) \), regard \( \A \) as an element of \( M_n(\nC) \). The Leibniz formula gives the same polynomial \( p_{\A} \) with real coefficients, and \( p_{\A}(\A) \) is computed from the same entries by the same sums and products; it is \( 0 \) by the complex case.

(d) Over \( \nF_2 \), \( x^2 + x + 1 \) has no root (its values at \( 0 \) and \( 1 \) are both \( 1 \)), so it does not split, and the matrix is not triangularizable over \( \nF_2 \) by @thm-triangularization. To run the argument we would need a larger field containing \( \nF_2 \) in which the polynomial splits, and we have not constructed one. The adjugate proof of @thm-cayley-hamilton needs no such field. (For instance \( \A = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix} \) has this characteristic polynomial, and indeed \( \A^2 + \A + \I = 0 \) over \( \nF_2 \).)
:::

:::: {#exr-triangularization-c2}
[C2: Real operators have small invariant subspaces]

Let \( \A \in M_n(\nR) \), \( n \ge 1 \), regarded also as a complex matrix.

::: {.enumerate options="label=(\alph*)"}
1. Let \( \lambda = a + bi \) (\( a, b \in \nR \)) be a complex eigenvalue of \( \A \) with eigenvector \( \z = \x + i\y \), where \( \x, \y \in \nR^n \). Show that \( \A\x = a\x - b\y \) and \( \A\y = b\x + a\y \).
2. Deduce that \( \Span(\x, \y) \subseteq \nR^n \) is \( \A \)-invariant, and has dimension \( 1 \) or \( 2 \).
3. Deduce that every operator on a real vector space \( V \) with \( 1 \le \dim V < \infty \) has an invariant subspace of dimension \( 1 \) or \( 2 \).
4. For \( \C = \begin{pmatrix} 0 & 0 & 2 \\ 1 & 0 & -1 \\ 0 & 1 & 2 \end{pmatrix} \), check that \( \z = (0, -2, 1) + i(-2, 1, 0) \) is an eigenvector for \( i \), and find the invariant plane of (b).
:::
::::

::: {.solution}
(a) The eigenvalue exists by @thm-complex-operator-has-eigenvalue. Since \( \A \) has real entries, \( \A\z = \A\x + i\A\y \) with \( \A\x, \A\y \in \nR^n \). On the other hand, \( \lambda\z = (a + bi)(\x + i\y) = (a\x - b\y) + i(b\x + a\y) \). A vector of \( \nC^n \) determines its real and imaginary parts entry by entry, so \( \A\x = a\x - b\y \) and \( \A\y = b\x + a\y \).

(b) By (a), \( \A\x \) and \( \A\y \) lie in \( W = \Span(\x, \y) \), so \( W \) is invariant by @lem-invariance-on-spanning-list. Since \( \z \ne \0 \), at least one of \( \x, \y \) is non-zero, so \( \dim W \ge 1 \), and \( \dim W \le 2 \) since \( W \) is spanned by two vectors.

(c) Choose a basis \( \sB \) of \( V \), let \( \A = \mtx{T}{\sB}{\sB} \in M_n(\nR) \), and let \( W \) be as in (b). Let \( \Phi \colon V \to \nR^n \) be the coordinate isomorphism \( \v \mapsto \coord{\v}{\sB} \) (@cor-coordinate-isomorphism). Then \( \Phi^{-1}(W) \) is a subspace of the same dimension as \( W \), and for \( \v \in \Phi^{-1}(W) \), \( \Phi(T\v) = \A\Phi(\v) \in W \) (@thm-matrix-of-map-coordinates), so \( T\v \in \Phi^{-1}(W) \).

(d) With \( \x = (0, -2, 1) \) and \( \y = (-2, 1, 0) \): \( \C\x = (2, -1, 0) = -\y \) and \( \C\y = (0, -2, 1) = \x \). So \( \C\z = \C\x + i\C\y = -\y + i\x = i(\x + i\y) = i\z \), and \( \z \) is an eigenvector for \( i \) (here \( a = 0 \), \( b = 1 \), matching (a)). The invariant plane is \( \Span((0, -2, 1), (-2, 1, 0)) \), which is the plane \( x + 2y + 4z = 0 \). Over \( \nR \), \( \C \) also has the eigenvalue \( 2 \) with eigenvector \( (1, 0, 1) \), an invariant line.
:::

:::: {#exr-triangularization-c3}
[C3: Traces of powers detect nilpotency]

Let \( \C \in M_n(\nC) \), \( n \ge 1 \), with \( \tr(\C^k) = 0 \) for \( k = 1, \dots, n \). The goal is to prove that \( \C^n = 0 \).

::: {.enumerate options="label=(\alph*)"}
1. Let \( d_1, \dots, d_n \) be the diagonal entries of a triangular form of \( \C \). Show that \( d_1^k + \dots + d_n^k = 0 \) for \( k = 1, \dots, n \).
2. Suppose some \( d_i \ne 0 \). Let \( \mu_1, \dots, \mu_r \) (\( r \ge 1 \)) be the distinct non-zero values among the \( d_i \), and let \( m_j \ge 1 \) be the number of indices \( i \) with \( d_i = \mu_j \). Show that \( \sum_{j=1}^{r} m_j\mu_j^k = 0 \) for \( k = 1, \dots, r \).
3. Show that the \( r \times r \) matrix with \( (k, j) \)-entry \( \mu_j^k \) is invertible, and derive a contradiction from (b).
4. Conclude that every \( d_i = 0 \), that \( p_{\C} = x^n \), and that \( \C^n = 0 \).
5. Show that the statement fails over \( \nF_2 \).
:::

*Hint: for (c), factor the matrix as a transposed Vandermonde matrix times a diagonal matrix.*
::::

::: {.solution}
(a) By @cor-complex-triangularizable a triangular form exists, and by @exr-triangularization-b3 (b), \( \tr \C^k = \sum_i d_i^k \), which is \( 0 \) by hypothesis.

(b) Indices with \( d_i = 0 \) contribute nothing to \( \sum_i d_i^k \) for \( k \ge 1 \). Grouping the other indices by their value, \( \sum_i d_i^k = \sum_j m_j\mu_j^k \). Since \( r \le n \), (a) applies for \( k = 1, \dots, r \).

(c) Let \( \M \) be the matrix with \( (k, j) \)-entry \( \mu_j^k \). The Vandermonde matrix \( \V = \V(\mu_1, \dots, \mu_r) \) has \( (j, k) \)-entry \( \mu_j^{k-1} \), so \( \V\tp \) has \( (k, j) \)-entry \( \mu_j^{k-1} \), and multiplying column \( j \) by \( \mu_j \) gives \( \M = \V\tp\diag(\mu_1, \dots, \mu_r) \). Since the \( \mu_j \) are distinct, \( \V \) is invertible (@cor-vandermonde-nonzero), hence so is \( \V\tp \) (@thm-det-transpose); since the \( \mu_j \) are non-zero, the diagonal matrix is invertible. So \( \M \) is invertible. By (b), \( \M(m_1, \dots, m_r) = \0 \), so \( (m_1, \dots, m_r) = \0 \) in \( \nC^r \). But each \( m_j \) is a positive integer, which is non-zero in \( \nC \). This contradiction shows that no \( d_i \) is non-zero.

(d) By (c), all \( d_i = 0 \), so \( p_{\C} = x^n \) by @thm-diagonal-of-triangular-form (a). By @thm-cayley-hamilton, \( \C^n = p_{\C}(\C) = 0 \).

(e) Over \( \nF_2 \), \( \C = \I_2 \) has \( \tr \C^k = \tr \I_2 = 1 + 1 = 0 \) for every \( k \), but \( \C^k = \I_2 \ne 0 \). The step that fails is (c): the positive integer \( m_1 = 2 \) is \( 0 \) in \( \nF_2 \). Compare @exr-commutators-and-shoda-c2, where in characteristic \( 0 \) the same conclusion was reached for a commutator by a route that avoids eigenvalues.
:::
