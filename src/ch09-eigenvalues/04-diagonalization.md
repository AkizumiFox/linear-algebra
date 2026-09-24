# Diagonalization

We can now answer the question of Chapter 4 in the best case. An operator has a diagonal matrix in some basis exactly when there are enough eigenvectors to form a basis, and the previous two sections give precise ways to count "enough": by dimensions of eigenspaces, or by comparing geometric with algebraic multiplicities. This section proves that these tests agree, shows how to find the diagonalizing basis for a concrete matrix, and uses it to compute powers. The payoff is a closed formula for the Fibonacci numbers. We also meet the operators for which the method fails, and see that the field is part of the answer.

## Diagonalizable operators

Chapter 2 introduced similarity to compare the matrices of one operator in different bases (@thm-similar-iff-same-operator), and asked for the simplest representative. Section 2 unwound the wish "\( \mtx{T}{\sB}{\sB} \) is diagonal" and found that it says exactly that every vector of \( \sB \) is an eigenvector. Diagonal matrices are the matrices we can compute with most easily: they add, multiply, power and invert entry by entry. So the operators that admit such a basis deserve a name.

*An operator is diagonalizable when some basis consists of vectors that the operator only stretches.*

::: {#def-diagonalizable}
[Diagonalizable]

Let \( V \) be a finite-dimensional vector space over \( F \). An operator \( T \in \cL(V) \) is **diagonalizable** if there **exists** a basis \( \sB \) of \( V \) such that \( \mtx{T}{\sB}{\sB} \) is a diagonal matrix.

A matrix \( \A \in M_n(F) \) is **diagonalizable over \( F \)** if it is similar to a diagonal matrix: there **exist** an **invertible** \( \P \in M_n(F) \) and a diagonal \( \D \in M_n(F) \) with \( \P^{-1}\A \P = \D \), equivalently \( \A = \P \D \P^{-1} \).
:::

In words: for an operator, we are free to choose **any** basis, and we ask whether **one** of them makes the matrix diagonal; most bases will not. For a matrix, the change-of-basis matrix \( \P \) and the diagonal entries of \( \D \) must both have entries **in \( F \)**. The two notions match: \( \A \) is diagonalizable over \( F \) if and only if \( T_{\A} \in \cL(F^n) \) is diagonalizable, by @thm-similar-iff-same-operator (c), because the matrices of \( T_{\A} \) in the bases of \( F^n \) are exactly the matrices similar to \( \A \). Likewise, \( T \) is diagonalizable if and only if \( \mtx{T}{\sC}{\sC} \) is diagonalizable for one, equivalently every, basis \( \sC \) of \( V \), by @thm-similar-iff-same-operator (a) and (b).

**Examples.**

- **Diagonal matrices** are diagonalizable, with \( \P = \I \). So is every scalar operator \( c\,\id_V \), whose matrix is \( c\I \) in every basis.
- **The degenerate cases.** Every \( 1 \times 1 \) matrix is diagonal. On \( V = \{\0\} \), the empty basis gives the empty matrix, which counts as diagonal. These cases are harmless, but they remind us that diagonalizability is a question about repeated eigenvalues and missing eigenvectors, which need room to occur.
- **A \( 2 \times 2 \) matrix.** In @exm-eigenvalues-2x2, \( \A = \begin{pmatrix} 1 & 2 \\ 3 & 2 \end{pmatrix} \) has eigenvectors \( (2, 3) \) for \( 4 \) and \( (1, -1) \) for \( -1 \). They form a basis of \( \nR^2 \), so \( \A \) is diagonalizable, with \( \P = \begin{pmatrix} 2 & 1 \\ 3 & -1 \end{pmatrix} \) and \( \D = \diag(4, -1) \); we check this below.
- **Projections and involutions.** A projection \( P \) satisfies \( V = \im P \oplus \ker P \) with \( P \) the identity on \( \im P \) and zero on \( \ker P \) (@thm-projection-direct-sum). A basis of \( \im P \) followed by a basis of \( \ker P \) is a basis \( \sB \) with \( \mtx{P}{\sB}{\sB} = \diag(1, \dots, 1, 0, \dots, 0) \). In characteristic not \( 2 \), an involution splits \( V = E_{+} \oplus E_{-} \) (@thm-involution-decomposition), and gives \( \diag(1, \dots, 1, -1, \dots, -1) \) in the same way.

**Non-example by minimal change.** Change the \( (1, 2) \)-entry of \( \I_2 \) from \( 0 \) to \( 1 \), giving \( \J = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) over any field \( F \). It is still triangular with the single eigenvalue \( 1 \), and still invertible. What fails is the existence of a basis of eigenvectors: \( E_1(\J) = \ker\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = \Span(\e_1) \) is a line, so every eigenvector of \( \J \) is a multiple of \( \e_1 \), and no two eigenvectors are independent. By the unwinding in Section 2, no basis \( \sB \) makes \( \mtx{T_{\J}}{\sB}{\sB} \) diagonal. (Directly: if \( \P^{-1}\J \P = \D \) were diagonal, its diagonal entries would be eigenvalues of \( \J \), so \( \D = \I \), and then \( \J = \P \I \P^{-1} = \I \), which is false.)

**Why this definition.** We ask for similarity to a diagonal matrix, not equality, because the basis is ours to choose; a matrix like \( \begin{pmatrix} 1 & 2 \\ 3 & 2 \end{pmatrix} \) has nothing diagonal about it until the right basis is found. We insist that \( \P \) and \( \D \) have entries in \( F \), because otherwise the word would not depend on the field and would hide a real phenomenon: the rotation \( \R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \) has no real eigenvector, so it is not diagonalizable over \( \nR \), while over \( \nC \) it becomes \( \diag(i, -i) \) (Section 2). The name says what the definition promises: the operator can be **made** diagonal.

::: {.warning}
**Diagonalizability depends on the field, and even on its characteristic.** The rotation \( \R \) is diagonalizable over \( \nC \) but not over \( \nR \). A subtler case: \( \S = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) is diagonalizable over \( \nQ \), with eigenvectors \( (1, 1) \) for \( 1 \) and \( (1, -1) \) for \( -1 \). Over \( \nF_2 \) the same matrix has \( p_{\S} = x^2 - 1 = (x - 1)^2 \), since \( -1 = 1 \), and \( \S - \I = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \) has rank \( 1 \), so its only eigenvectors are the multiples of \( (1, 1) \), and \( \S \) is **not** diagonalizable over \( \nF_2 \). Always say over which field.
:::

## The Diagonalization Theorem

How do we decide whether a basis of eigenvectors exists without searching for one? Eigenvectors for different eigenvalues are automatically independent (@thm-distinct-eigenvalues-independent), so the only question is whether each eigenspace supplies enough of them. The theorem below lists five equivalent ways to say "enough".

::: {#thm-diagonalization}
[Diagonalization Theorem]

Let \( V \) be a finite-dimensional vector space over \( F \) with \( \dim V = n \ge 1 \), let \( T \in \cL(V) \), and let \( \lambda_1, \dots, \lambda_k \) be the distinct eigenvalues of \( T \) (possibly \( k = 0 \)). The following are equivalent:

::: {.enumerate options="label=(\alph*)"}
1. \( T \) is diagonalizable;
2. \( V \) has a basis consisting of eigenvectors of \( T \);
3. \( V = E_{\lambda_1}(T) \oplus \dots \oplus E_{\lambda_k}(T) \);
4. \( \dim E_{\lambda_1}(T) + \dots + \dim E_{\lambda_k}(T) = n \);
5. \( p_T \) splits over \( F \), and \( g_T(\lambda_i) = a_T(\lambda_i) \) for every \( i = 1, \dots, k \).
:::

In that case, if \( \sB \) is a basis of eigenvectors, then \( \mtx{T}{\sB}{\sB} \) is diagonal, its diagonal entries are the eigenvalues of the corresponding basis vectors, and each \( \lambda_i \) appears on the diagonal exactly \( a_T(\lambda_i) = g_T(\lambda_i) \) times.
:::

(For \( k = 0 \) the sum in (c) is \( \{\0\} \) and the sum in (d) is \( 0 \); all five conditions are then false, since \( n \ge 1 \).)

::: {.idea}
**Plan:** prove (a) \( \Rightarrow \) (b) \( \Rightarrow \) (c) \( \Rightarrow \) (d) \( \Rightarrow \) (e) \( \Rightarrow \) (b) \( \Rightarrow \) (a).

① (a) \( \Leftrightarrow \) (b) is the unwinding of columns from Section 2.
② From a basis of eigenvectors, the eigenspaces add up to \( V \), and @cor-eigenspaces-direct-sum makes the sum direct.
③ Dimensions add in a direct sum.
④ (d) \( \Rightarrow \) (e) is a sandwich: \( n = \sum g \le \sum a \le n \), so every inequality is an equality.
⑤ (e) \( \Rightarrow \) (b) runs the sandwich backwards and glues bases of the eigenspaces together.

The hard work was done in Sections 2 and 3; this proof only assembles it.
:::

::: {.proof}
(a) \( \Leftrightarrow \) (b). Let \( \sB = (\v_1, \dots, \v_n) \) be a basis of \( V \). By @def-matrix-of-linear-map, column \( j \) of \( \mtx{T}{\sB}{\sB} \) is \( \coord{T\v_j}{\sB} \), and this column is \( d_j\e_j \) if and only if \( T\v_j = d_j\v_j \). Hence \( \mtx{T}{\sB}{\sB} = \diag(d_1, \dots, d_n) \) if and only if \( T\v_j = d_j\v_j \) for every \( j \). Since basis vectors are non-zero, this says that every \( \v_j \) is an eigenvector of \( T \), for the eigenvalue \( d_j \). So a basis makes \( \mtx{T}{\sB}{\sB} \) diagonal exactly when it consists of eigenvectors, which also proves the final statement about the diagonal entries, apart from the count.

(b) \( \Rightarrow \) (c). Let \( \sB \) be a basis of eigenvectors. Each vector of \( \sB \) lies in \( E_{\lambda_i}(T) \) for some \( i \), so \( \sB \subseteq E_{\lambda_1}(T) + \dots + E_{\lambda_k}(T) \). This sum is a subspace (@thm-subspace-sum) containing a spanning list of \( V \), so it equals \( V \). By @cor-eigenspaces-direct-sum the sum is direct.

(c) \( \Rightarrow \) (d). By @thm-direct-sum-k-criteria ((a) \( \Rightarrow \) (e)), \( n = \dim V = \sum_i \dim E_{\lambda_i}(T) \).

(d) \( \Rightarrow \) (e). By @thm-geometric-le-algebraic, \( g_T(\lambda_i) \le a_T(\lambda_i) \) for each \( i \). The eigenvalues are exactly the roots of \( p_T \) in \( F \) (@thm-eigenvalue-characterizations), so by @thm-roots-with-multiplicity, \( \sum_i a_T(\lambda_i) \le \deg p_T = n \) (@thm-charpoly-coefficients). With (d),
\[
n = \sum_{i=1}^{k} g_T(\lambda_i) \le \sum_{i=1}^{k} a_T(\lambda_i) \le n .
\]
Hence both inequalities are equalities. The second equality, \( \sum_i a_T(\lambda_i) = \deg p_T \), means that \( p_T \) splits over \( F \) (@thm-roots-with-multiplicity). The first says \( \sum_i \big(a_T(\lambda_i) - g_T(\lambda_i)\big) = 0 \), a sum of non-negative integers, so every term is \( 0 \) and \( g_T(\lambda_i) = a_T(\lambda_i) \) for each \( i \).

(e) \( \Rightarrow \) (b). Since \( p_T \) splits, @thm-roots-with-multiplicity gives \( \sum_i a_T(\lambda_i) = n \), and so \( \sum_i g_T(\lambda_i) = n \) by (e). For each \( i \) let \( \sB_i \) be a basis of \( E_{\lambda_i}(T) \), of length \( g_T(\lambda_i) \), and let \( \sB \) be the list \( \sB_1, \dots, \sB_k \). The sum \( W = E_{\lambda_1}(T) + \dots + E_{\lambda_k}(T) \) is direct (@cor-eigenspaces-direct-sum), so by @thm-direct-sum-k-criteria ((a) \( \Rightarrow \) (d)), \( \sB \) is a basis of \( W \), and \( \dim W = n = \dim V \). By @thm-dim-impl-eq, \( W = V \). So \( \sB \) is a basis of \( V \), and its vectors are eigenvectors, being non-zero vectors of eigenspaces.

Finally, suppose \( \sB \) is a basis of eigenvectors, and let \( m_i \) be the number of its vectors with eigenvalue \( \lambda_i \). By (a) \( \Leftrightarrow \) (b), \( \mtx{T}{\sB}{\sB} \) is diagonal with \( \lambda_i \) appearing \( m_i \) times, so \( p_T = \prod_i (x - \lambda_i)^{m_i} \) (the triangular case after @def-characteristic-polynomial). Since the \( \lambda_i \) are distinct, \( (x - \lambda_i)^{m_i} \) divides \( p_T \) and the remaining factors do not vanish at \( \lambda_i \), so \( m_i = a_T(\lambda_i) \) by @lem-multiplicity-cofactor; and \( a_T(\lambda_i) = g_T(\lambda_i) \) by (e). This proves the theorem.
:::

This is the theorem promised in Chapter 1, §7: **an operator is diagonalizable exactly when its eigenspaces split \( V \) as a direct sum**, and then \( T \) acts on the \( i \)-th piece as the scalar \( \lambda_i \). In the language of @thm-direct-sum-invariant-block-diagonal, the pieces are invariant, the blocks are \( \lambda_i\I_{g(\lambda_i)} \), and the matrix is block diagonal with scalar blocks.

Condition (e) is the practical test. It separates two different ways to fail, and they have different remedies. If \( p_T \) does not split, the field is too small, and enlarging it (from \( \nR \) to \( \nC \)) may help. If \( p_T \) splits but some \( g(\lambda) < a(\lambda) \), there are genuinely too few eigenvectors, and no change of field helps; Chapter 10 explains what the best matrix is then.

The easiest case of (e) needs no rank computation at all.

::: {#cor-distinct-eigenvalues-diagonalizable}
[Distinct Eigenvalues Imply Diagonalizable]

Let \( V \) be a finite-dimensional vector space over \( F \) with \( \dim V = n \ge 1 \), and let \( T \in \cL(V) \) have \( n \) distinct eigenvalues. Then \( T \) is diagonalizable. The same holds for \( \A \in M_n(F) \) with \( n \) distinct eigenvalues in \( F \).
:::

::: {.proof}
Let \( \lambda_1, \dots, \lambda_n \) be the eigenvalues. Each \( \lambda_i \) is an eigenvalue, so \( E_{\lambda_i}(T) \ne \{\0\} \) (@def-eigenspace) and \( \dim E_{\lambda_i}(T) \ge 1 \), so \( \sum_i \dim E_{\lambda_i}(T) \ge n \), and by @cor-eigenspaces-direct-sum the sum is at most \( n \). Hence it equals \( n \), and \( T \) is diagonalizable by @thm-diagonalization ((d) \( \Rightarrow \) (a)).
:::

So a matrix whose characteristic polynomial has \( n \) distinct roots in \( F \) is diagonalizable over \( F \); for example \( \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix} \) is, because its eigenvalues \( 2 \) and \( 3 \) are distinct. This is the generic situation, but it is only a sufficient condition.

::: {.warning}
**The converse fails: diagonalizable matrices may have repeated eigenvalues.** \( \I_n \) is diagonal, and its only eigenvalue is \( 1 \). Less trivially, the matrix of @exm-diagonalize-3x3 below has eigenvalues \( 1, 1, 3 \) and is diagonalizable. A repeated eigenvalue is a reason to **check** \( g(\lambda) = a(\lambda) \), not a verdict.
:::

::: {.check}
Which of \( \begin{pmatrix} 3 & 1 \\ 0 & 5 \end{pmatrix} \), \( \begin{pmatrix} 3 & 1 \\ 0 & 3 \end{pmatrix} \), \( \begin{pmatrix} 3 & 0 \\ 0 & 3 \end{pmatrix} \) are diagonalizable over \( \nR \)?
:::

::: {.solution}
The first has distinct eigenvalues \( 3, 5 \), so it is diagonalizable by @cor-distinct-eigenvalues-diagonalizable. The second has \( a(3) = 2 \) but \( \rank\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = 1 \), so \( g(3) = 1 < a(3) \), and it is not diagonalizable by @thm-diagonalization (e). The third is already diagonal.
:::

## Computing \( \P \) and \( \D \)

For a matrix \( \A \in M_n(F) \), a basis of eigenvectors turns into the matrices \( \P \) and \( \D \) of @def-diagonalizable directly. Let \( (\v_1, \dots, \v_n) \) be a basis of \( F^n \) with \( \A\v_j = d_j\v_j \), let \( \P \) be the matrix with **columns** \( \v_1, \dots, \v_n \), and \( \D = \diag(d_1, \dots, d_n) \). By the column view of matrix multiplication (@thm-three-views-of-product), column \( j \) of \( \A \P \) is \( \A\v_j = d_j\v_j \), and column \( j \) of \( \P \D \) is \( \P(d_j\e_j) = d_j\v_j \). So
\[
\A \P = \P \D .
\]
The columns of \( \P \) form a basis, so \( \P \) is invertible (@thm-invertible-tfae), and multiplying on the left by \( \P^{-1} \) gives \( \P^{-1}\A \P = \D \). The **order** matters in one way only: the \( j \)-th column of \( \P \) must be an eigenvector for the \( j \)-th diagonal entry of \( \D \). Reordering the eigenvectors reorders the diagonal of \( \D \) in the same way, and any order works.

For \( \A = \begin{pmatrix} 1 & 2 \\ 3 & 2 \end{pmatrix} \), with \( \P = \begin{pmatrix} 2 & 1 \\ 3 & -1 \end{pmatrix} \) and \( \D = \diag(4, -1) \): \( \A \P = \begin{pmatrix} 8 & -1 \\ 12 & 1 \end{pmatrix} \) and \( \P \D = \begin{pmatrix} 8 & -1 \\ 12 & 1 \end{pmatrix} \). Checking \( \A \P = \P \D \) avoids computing \( \P^{-1} \), and together with \( \det \P = -5 \ne 0 \) it proves \( \P^{-1}\A \P = \D \).

The full procedure, then: compute \( p_{\A} \) and its roots; if it does not split over \( F \), stop (not diagonalizable over \( F \)); for each eigenvalue compute a basis of \( E_\lambda(\A) \); if some \( g(\lambda) < a(\lambda) \), stop; otherwise put the basis vectors as columns of \( \P \).

::: {#exm-diagonalize-3x3}
[Diagonalizing a \( 3 \times 3 \) Matrix with a Repeated Eigenvalue]

Let
\[
\A = \begin{pmatrix} 3 & 2 & -2 \\ -2 & -1 & 2 \\ -2 & -2 & 3 \end{pmatrix} \in M_3(\nR).
\]
Decide whether \( \A \) is diagonalizable over \( \nR \). If it is, find an invertible \( \P \) and a diagonal \( \D \) with \( \P^{-1}\A \P = \D \).
:::

::: {.solution}
*Characteristic polynomial.* Expanding along the first row (@thm-laplace-expansion over \( \nR[x] \)),
\[
\begin{aligned}
p_{\A}(x) &= \det\begin{pmatrix} x - 3 & -2 & 2 \\ 2 & x + 1 & -2 \\ 2 & 2 & x - 3 \end{pmatrix} \\
  &= (x - 3)\big[(x + 1)(x - 3) + 4\big] + 2\big[2(x - 3) + 4\big] \\
  &\qquad + 2\big[4 - 2(x + 1)\big].
\end{aligned}
\]
The brackets are \( x^2 - 2x + 1 = (x - 1)^2 \), \( 2(x - 1) \) and \( -2(x - 1) \), so the last two terms cancel and
\[
p_{\A}(x) = (x - 1)^2(x - 3).
\]
It splits over \( \nR \), with \( a(1) = 2 \) and \( a(3) = 1 \). As a check, \( \tr \A = 5 = 1 + 1 + 3 \) (@thm-trace-det-eigenvalues).

*Eigenspace for \( 1 \).*
\[
\A - \I = \begin{pmatrix} 2 & 2 & -2 \\ -2 & -2 & 2 \\ -2 & -2 & 2 \end{pmatrix}.
\]
Every row is a multiple of \( (1, 1, -1) \), so the rank is \( 1 \) and \( g(1) = 3 - 1 = 2 = a(1) \). The system reduces to \( x + y - z = 0 \); with the free variables \( y \) and \( z \), a basis of \( E_1(\A) \) is \( (-1, 1, 0) \), \( (1, 0, 1) \) (@thm-basis-null-space).

*Eigenspace for \( 3 \).* Here \( g(3) = 1 = a(3) \) by @thm-geometric-le-algebraic, so condition (e) of @thm-diagonalization holds and \( \A \) is diagonalizable. To find the eigenvector,
\[
\A - 3\I = \begin{pmatrix} 0 & 2 & -2 \\ -2 & -4 & 2 \\ -2 & -2 & 0 \end{pmatrix}.
\]
Row \( 1 \) gives \( y = z \), and row \( 3 \) gives \( x = -y \); row \( 2 \) then reads \( 2y - 4y + 2y = 0 \). So \( E_3(\A) = \Span((1, -1, -1)) \).

*The matrices.* Put the eigenvectors as columns, in the order of the eigenvalues we want on the diagonal:
\[
\P = \begin{pmatrix} -1 & 1 & 1 \\ 1 & 0 & -1 \\ 0 & 1 & -1 \end{pmatrix}, \qquad \D = \diag(1, 1, 3).
\]
*Check.* The columns of \( \A \P \) are \( \A(-1, 1, 0) = (-1, 1, 0) \), \( \A(1, 0, 1) = (1, 0, 1) \) and \( \A(1, -1, -1) = (3, -3, -3) \), which are the columns of \( \P \D \). Expanding along the first column, \( \det \P = -1 \cdot (0 + 1) - 1 \cdot (-1 - 1) = 1 \ne 0 \), so \( \P \) is invertible, and in fact
\[
\P^{-1} = \begin{pmatrix} 1 & 2 & -1 \\ 1 & 1 & 0 \\ 1 & 1 & -1 \end{pmatrix},
\]
as multiplying out \( \P \P^{-1} = \I \) confirms. Hence \( \P^{-1}\A \P = \D \).

Had we listed the eigenvectors in the order \( (1, -1, -1), (-1, 1, 0), (1, 0, 1) \), we would get \( \D = \diag(3, 1, 1) \) instead. Both are correct.
:::

## Powers and polynomials

Why diagonalize? Because powers of diagonal matrices are free: \( \diag(d_1, \dots, d_n)^k = \diag(d_1^k, \dots, d_n^k) \). Similarity carries this over.

::: {#thm-powers-diagonalizable}
[Powers and Polynomials of a Diagonalizable Matrix]

Let \( \A = \P \D \P^{-1} \) with \( \P \in M_n(F) \) invertible and \( \D = \diag(d_1, \dots, d_n) \). Then for every \( k \in \nN \) and every \( p \in F[x] \),
\[
\A^k = \P\,\diag(d_1^k, \dots, d_n^k)\,\P^{-1}, \qquad p(\A) = \P\,\diag\big(p(d_1), \dots, p(d_n)\big)\,\P^{-1}.
\]
If moreover every \( d_i \ne 0 \), then \( \A \) is invertible and \( \A^{-1} = \P\,\diag(d_1^{-1}, \dots, d_n^{-1})\,\P^{-1} \).
:::

::: {.proof}
Since \( \D = \P^{-1}\A \P \), @prp-similarity-invariants (c) gives \( p(\D) = \P^{-1}p(\A)\P \), so \( p(\A) = \P\,p(\D)\,\P^{-1} \). A diagonal matrix is the direct sum \( (d_1) \oplus \dots \oplus (d_n) \) of \( 1 \times 1 \) blocks, so by @thm-block-diagonal-arithmetic (b), extended to \( n \) blocks by induction on the number of blocks, \( p(\D) = (p(d_1)) \oplus \dots \oplus (p(d_n)) = \diag(p(d_1), \dots, p(d_n)) \). Taking \( p = x^k \) gives the formula for \( \A^k \). If every \( d_i \ne 0 \), put \( \B = \P\,\diag(d_1^{-1}, \dots, d_n^{-1})\,\P^{-1} \); then \( \A \B = \P \D \P^{-1}\P\,\diag(d_i^{-1})\,\P^{-1} = \P\,\diag(d_id_i^{-1})\,\P^{-1} = \P \P^{-1} = \I \), and \( \B = \A^{-1} \) by @thm-one-sided-inverse.
:::

In words: to apply a polynomial to a diagonalizable matrix, apply it to the eigenvalues and change basis back. The work is done once, when \( \P \) is found; every power after that costs a single product of three matrices. For @exm-diagonalize-3x3,
\[
\A^k = \P\,\diag(1, 1, 3^k)\,\P^{-1} = \begin{pmatrix} 3^k & 3^k - 1 & 1 - 3^k \\ 1 - 3^k & 2 - 3^k & 3^k - 1 \\ 1 - 3^k & 1 - 3^k & 3^k \end{pmatrix},
\]
which is \( \I \) for \( k = 0 \) and \( \A \) for \( k = 1 \), as it must be.

The most famous application is to a recurrence. A linear recurrence of order two becomes a first-order recurrence for vectors, whose solution is a matrix power.

::: {#exm-fibonacci-binet}
[A Closed Formula for the Fibonacci Numbers]

The Fibonacci numbers are defined by \( F_0 = 0 \), \( F_1 = 1 \) and \( F_{k+2} = F_{k+1} + F_k \) for \( k \ge 0 \). (Here \( F_k \) is a number, not a field; we work over \( \nR \).) Find a formula for \( F_k \) by diagonalizing a \( 2 \times 2 \) matrix.
:::

::: {.solution}
*A vector recurrence.* Put \( \x_k = (F_{k+1}, F_k) \in \nR^2 \). The recurrence says
\[
\x_{k+1} = \begin{pmatrix} F_{k+2} \\ F_{k+1} \end{pmatrix} = \begin{pmatrix} F_{k+1} + F_k \\ F_{k+1} \end{pmatrix} = \A\x_k, \qquad \A = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}.
\]
By induction on \( k \), \( \x_k = \A^k\x_0 \) with \( \x_0 = (1, 0) \).

*Eigenvalues.* \( \tr \A = 1 \) and \( \det \A = -1 \), so \( p_{\A}(x) = x^2 - x - 1 \), with the two real roots
\[
\varphi = \frac{1 + \sqrt5}{2}, \qquad \psi = \frac{1 - \sqrt5}{2}.
\]
They are distinct, so \( \A \) is diagonalizable over \( \nR \) (@cor-distinct-eigenvalues-diagonalizable). Each root satisfies \( \lambda^2 = \lambda + 1 \), and we will use \( \varphi + \psi = 1 \), \( \varphi\psi = -1 \) and \( \varphi - \psi = \sqrt5 \).

*Eigenvectors.* For a root \( \lambda \), the vector \( (\lambda, 1) \) is an eigenvector: \( \A(\lambda, 1) = (\lambda + 1, \lambda) = (\lambda^2, \lambda) = \lambda(\lambda, 1) \). So
\[
\P = \begin{pmatrix} \varphi & \psi \\ 1 & 1 \end{pmatrix}, \qquad \D = \diag(\varphi, \psi), \qquad \P^{-1} = \frac{1}{\sqrt5}\begin{pmatrix} 1 & -\psi \\ -1 & \varphi \end{pmatrix},
\]
where \( \det \P = \varphi - \psi = \sqrt5 \ne 0 \) and \( \P^{-1} \) comes from @thm-two-by-two-inverse.

*The power.* By @thm-powers-diagonalizable, \( \x_k = \P \D^k\P^{-1}\x_0 \). Working from the right:
\[
\begin{aligned}
\P^{-1}\x_0 &= \frac{1}{\sqrt5}\begin{pmatrix} 1 \\ -1 \end{pmatrix}, \\
\D^k\P^{-1}\x_0 &= \frac{1}{\sqrt5}\begin{pmatrix} \varphi^k \\ -\psi^k \end{pmatrix}, \\
\P \D^k\P^{-1}\x_0 &= \frac{1}{\sqrt5}\begin{pmatrix} \varphi^{k+1} - \psi^{k+1} \\ \varphi^k - \psi^k \end{pmatrix}.
\end{aligned}
\]
The second entry of \( \x_k \) is \( F_k \), so
\[
F_k = \frac{\varphi^k - \psi^k}{\sqrt5} = \frac{1}{\sqrt5}\left[\left(\frac{1 + \sqrt5}{2}\right)^{k} - \left(\frac{1 - \sqrt5}{2}\right)^{k}\right].
\]
*Check.* \( k = 0 \): \( 0 \). \( k = 1 \): \( (\varphi - \psi)/\sqrt5 = 1 \). \( k = 2 \): \( (\varphi^2 - \psi^2)/\sqrt5 = (\varphi - \psi)(\varphi + \psi)/\sqrt5 = 1 \). And the right side satisfies the recurrence, because \( \varphi^{k+2} = \varphi^{k+1} + \varphi^k \) (multiply \( \varphi^2 = \varphi + 1 \) by \( \varphi^k \)), and likewise for \( \psi \).

Since \( |\psi| < 1 \), the term \( \psi^k/\sqrt5 \) has absolute value less than \( 1/2 \), so \( F_k \) is the integer nearest to \( \varphi^k/\sqrt5 \); the Fibonacci numbers grow like powers of \( \varphi \approx 1.618 \), the larger eigenvalue.
:::

The irrational numbers in the formula are forced. Over \( \nQ \), the polynomial \( x^2 - x - 1 \) has no root (by @thm-rational-root, the only candidates are \( \pm 1 \), and neither works), so \( \A \) has no eigenvalue in \( \nQ \) and is **not** diagonalizable over \( \nQ \), although all its entries and powers are integers. Chapter 7 met the same numbers as determinants of tridiagonal matrices (@exm-tridiagonal-fibonacci); here the recurrence is solved rather than just recognized. Section 11 of this chapter treats general linear recurrences and Markov chains the same way.

## When diagonalization fails

Two examples collect the ways @thm-diagonalization (e) can fail.

**Too few eigenvectors.** \( \J = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) is not diagonalizable over **any** field, because \( p_{\J} = (x - 1)^2 \) splits but \( g(1) = 1 < 2 = a(1) \). Enlarging the field changes nothing: the rank of \( \J - \I \) is \( 1 \) over every field. Its powers are still easy, \( \J^k = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix} \) by induction, but they are not of the form \( \P\,\diag(1, 1)\,\P^{-1} = \I \); the entry \( k \), growing linearly rather than like a power, is the footprint of the missing eigenvector. Chapter 10 shows that such blocks are the only additional ingredient.

**Too small a field.** The rotation \( \R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \) has \( p_{\R} = x^2 + 1 \), which does not split over \( \nR \), so \( \R \) is not diagonalizable over \( \nR \). Over \( \nC \) it has the distinct eigenvalues \( \pm i \) with eigenvectors \( (1, -i) \) and \( (1, i) \), so with \( \P = \begin{pmatrix} 1 & 1 \\ -i & i \end{pmatrix} \),
\[
\P^{-1}\R \P = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix}.
\]
Then \( \R^k = \P\,\diag(i^k, (-i)^k)\,\P^{-1} \), and since \( i^4 = 1 \), \( \R^4 = \I \): four quarter-turns make a full turn, as they should.

When a matrix depends on a parameter, the same test decides diagonalizability for every value at once.

::: {#exm-diagonalizable-parameter}
[Diagonalizability with a Parameter]

For which \( t \in \nR \) is \( \A_t = \begin{pmatrix} 2 & t & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix} \) diagonalizable over \( \nR \)?
:::

::: {.solution}
The matrix is upper triangular, so \( p_{\A_t}(x) = (x - 2)^2(x - 3) \) for every \( t \), by @thm-det-triangular. This splits, with \( a(2) = 2 \) and \( a(3) = 1 \). Since \( 1 \le g(3) \le a(3) = 1 \) by @thm-geometric-le-algebraic, only \( \lambda = 2 \) needs checking. Here
\[
\A_t - 2\I = \begin{pmatrix} 0 & t & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix},
\]
whose rank is \( 1 \) if \( t = 0 \) and \( 2 \) if \( t \neq 0 \). By rank–nullity for matrices (@thm-rank-nullity-matrix), \( g(2) = 3 - \rank(\A_t - 2\I) \) is \( 2 \) when \( t = 0 \) and \( 1 \) when \( t \neq 0 \). By @thm-diagonalization (e), \( \A_t \) is diagonalizable exactly when \( t = 0 \).

Notice what did not change: the eigenvalues and their algebraic multiplicities are the same for every \( t \). Only the geometric multiplicity, a rank, detects the difference.
:::

## Exercises

### A. Check your understanding

:::: {#exr-diagonalization-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define what it means for \( \A \in M_n(F) \) to be diagonalizable over \( F \).
2. State the Diagonalization Theorem, with at least four equivalent conditions.
3. True or false: a diagonalizable \( n \times n \) matrix has \( n \) distinct eigenvalues. Justify your answer.
4. True or false: every invertible matrix is diagonalizable. Justify your answer.
5. True or false: every diagonalizable matrix is invertible. Justify your answer.
6. If \( \P^{-1}\A \P = \D \) is diagonal, what are the columns of \( \P \), and how are they matched with the diagonal of \( \D \)?
:::
::::

::: {.solution}
(a) There are an invertible \( \P \in M_n(F) \) and a diagonal \( \D \in M_n(F) \) with \( \P^{-1}\A \P = \D \) (@def-diagonalizable).

(b) See @thm-diagonalization: for \( T \in \cL(V) \), \( \dim V = n \ge 1 \), with distinct eigenvalues \( \lambda_1, \dots, \lambda_k \), the following are equivalent: \( T \) is diagonalizable; \( V \) has a basis of eigenvectors; \( V = \bigoplus_i E_{\lambda_i}(T) \); \( \sum_i \dim E_{\lambda_i}(T) = n \); \( p_T \) splits and \( g(\lambda_i) = a(\lambda_i) \) for all \( i \).

(c) False. \( \I_n \) is diagonal, with the single eigenvalue \( 1 \).

(d) False. \( \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) has determinant \( 1 \) but is not diagonalizable.

(e) False. The zero matrix is diagonal and not invertible.

(f) The columns of \( \P \) form a basis of eigenvectors of \( \A \), and column \( j \) is an eigenvector for the \( j \)-th diagonal entry of \( \D \), since \( \A \P = \P \D \).
:::

### B. Practice

:::: {#exr-diagonalization-b1}
[B1: Diagonalize or show impossible]

For each real matrix, either find an invertible \( \P \) and a diagonal \( \D \) with \( \P^{-1}\A \P = \D \), or show that none exist.

::: {.enumerate options="label=(\alph*)"}
1. \( \A_1 = \begin{pmatrix} 0 & 1 \\ -6 & 5 \end{pmatrix} \).
2. \( \A_2 = \begin{pmatrix} 1 & 1 & 1 \\ 2 & 0 & 1 \\ -3 & 3 & 2 \end{pmatrix} \).
3. \( \A_3 = \begin{pmatrix} -1 & 2 & -2 \\ -2 & 3 & -2 \\ 2 & -2 & 3 \end{pmatrix} \).
:::
::::

::: {.solution}
(a) \( \tr \A_1 = 5 \), \( \det \A_1 = 6 \), so \( p = x^2 - 5x + 6 = (x - 2)(x - 3) \). The eigenvalues are distinct, so \( \A_1 \) is diagonalizable (@cor-distinct-eigenvalues-diagonalizable). \( \A_1 - 2\I = \begin{pmatrix} -2 & 1 \\ -6 & 3 \end{pmatrix} \) gives \( y = 2x \), eigenvector \( (1, 2) \); \( \A_1 - 3\I = \begin{pmatrix} -3 & 1 \\ -6 & 2 \end{pmatrix} \) gives \( y = 3x \), eigenvector \( (1, 3) \). So
\[
\P = \begin{pmatrix} 1 & 1 \\ 2 & 3 \end{pmatrix}, \quad \D = \diag(2, 3), \quad \P^{-1} = \begin{pmatrix} 3 & -1 \\ -2 & 1 \end{pmatrix},
\]
and indeed \( \A_1\P = \begin{pmatrix} 2 & 3 \\ 4 & 9 \end{pmatrix} = \P \D \).

(b) Expanding along the first row,
\[
\begin{aligned}
p(x) &= \det\begin{pmatrix} x - 1 & -1 & -1 \\ -2 & x & -1 \\ 3 & -3 & x - 2 \end{pmatrix} \\
  &= (x - 1)\big[x(x - 2) - 3\big] + \big[-2(x - 2) + 3\big] - \big[6 - 3x\big].
\end{aligned}
\]
The first bracket is \( (x - 3)(x + 1) \), and the last two terms add up to \( -2x + 7 - 6 + 3x = x + 1 \). So \( p(x) = (x + 1)\big[(x - 1)(x - 3) + 1\big] = (x + 1)(x - 2)^2 \), and \( a(2) = 2 \). Now
\[
\A_2 - 2\I = \begin{pmatrix} -1 & 1 & 1 \\ 2 & -2 & 1 \\ -3 & 3 & 0 \end{pmatrix}.
\]
Row \( 3 \) equals row \( 1 \) minus row \( 2 \), and rows \( 1 \) and \( 2 \) are not proportional, so the rank is \( 2 \) and \( g(2) = 1 < 2 = a(2) \). By @thm-diagonalization (e), \( \A_2 \) is **not** diagonalizable, over \( \nR \) or over \( \nC \).

(c) Expanding along the first row,
\[
\begin{aligned}
p(x) &= \det\begin{pmatrix} x + 1 & -2 & 2 \\ 2 & x - 3 & 2 \\ -2 & 2 & x - 3 \end{pmatrix} \\
  &= (x + 1)\big[(x - 3)^2 - 4\big] + 2\big[2(x - 3) + 4\big] \\
  &\qquad + 2\big[4 + 2(x - 3)\big].
\end{aligned}
\]
The first bracket is \( (x - 5)(x - 1) \) and the other two are \( 2(x - 1) \) each, so \( p(x) = (x - 1)\big[(x + 1)(x - 5) + 8\big] = (x - 1)(x^2 - 4x + 3) = (x - 1)^2(x - 3) \). For \( \lambda = 1 \), \( \A_3 - \I = \begin{pmatrix} -2 & 2 & -2 \\ -2 & 2 & -2 \\ 2 & -2 & 2 \end{pmatrix} \) has rank \( 1 \), so \( g(1) = 2 = a(1) \), and \( E_1 \) is the plane \( x - y + z = 0 \), with basis \( (1, 1, 0), (-1, 0, 1) \). Also \( g(3) = 1 = a(3) \), so \( \A_3 \) is diagonalizable. From \( \A_3 - 3\I = \begin{pmatrix} -4 & 2 & -2 \\ -2 & 0 & -2 \\ 2 & -2 & 0 \end{pmatrix} \), row \( 3 \) gives \( y = x \) and row \( 2 \) gives \( z = -x \), so \( E_3 = \Span((1, 1, -1)) \). Hence
\[
\P = \begin{pmatrix} 1 & -1 & 1 \\ 1 & 0 & 1 \\ 0 & 1 & -1 \end{pmatrix}, \qquad \D = \diag(1, 1, 3).
\]
Check: \( \A_3(1, 1, 0) = (1, 1, 0) \), \( \A_3(-1, 0, 1) = (-1, 0, 1) \), \( \A_3(1, 1, -1) = (3, 3, -3) \), so \( \A_3\P = \P \D \); and \( \det \P = 1(0 - 1) + 1(-1 - 0) + 1(1 - 0) = -1 \ne 0 \).
:::

:::: {#exr-diagonalization-b2}
[B2: A tenth power]

Let \( \A = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix} \in M_2(\nR) \).

::: {.enumerate options="label=(\alph*)"}
1. Diagonalize \( \A \).
2. Hence find a formula for \( \A^k \), \( k \in \nN \), and compute \( \A^{10} \).
:::
::::

::: {.solution}
(a) \( \tr \A = 2 \), \( \det \A = -3 \), so \( p = x^2 - 2x - 3 = (x - 3)(x + 1) \). \( \A - 3\I = \begin{pmatrix} -2 & 2 \\ 2 & -2 \end{pmatrix} \) gives the eigenvector \( (1, 1) \), and \( \A + \I = \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix} \) gives \( (1, -1) \). So \( \P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \), \( \D = \diag(3, -1) \), and \( \P^{-1} = \frac12\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \) by @thm-two-by-two-inverse.

(b) By @thm-powers-diagonalizable,
\[
\A^k = \frac12\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} 3^k & 0 \\ 0 & (-1)^k \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = \frac12\begin{pmatrix} 3^k + (-1)^k & 3^k - (-1)^k \\ 3^k - (-1)^k & 3^k + (-1)^k \end{pmatrix}.
\]
For \( k = 1 \) this gives \( \frac12\begin{pmatrix} 2 & 4 \\ 4 & 2 \end{pmatrix} = \A \). With \( 3^{10} = 59049 \) and \( (-1)^{10} = 1 \),
\[
\A^{10} = \begin{pmatrix} 29525 & 29524 \\ 29524 & 29525 \end{pmatrix}.
\]
:::

:::: {#exr-diagonalization-b3}
[B3: A matrix with a parameter]

For \( t \in \nR \), let \( \A_t = \begin{pmatrix} 1 & 1 & 0 \\ 0 & t & 0 \\ 0 & 0 & 2 \end{pmatrix} \). Determine all \( t \) for which \( \A_t \) is diagonalizable over \( \nR \). Justify your answer.
::::

::: {.solution}
\( \A_t \) is upper triangular, so \( p(x) = (x - 1)(x - t)(x - 2) \), which splits over \( \nR \).

*Case \( t \notin \{1, 2\} \).* The eigenvalues \( 1, t, 2 \) are distinct, so \( \A_t \) is diagonalizable (@cor-distinct-eigenvalues-diagonalizable).

*Case \( t = 1 \).* Then \( a(1) = 2 \), and \( \A_1 - \I = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} \) has rank \( 2 \), so \( g(1) = 1 < 2 \). Not diagonalizable.

*Case \( t = 2 \).* Then \( a(2) = 2 \), and \( \A_2 - 2\I = \begin{pmatrix} -1 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} \) has rank \( 1 \), so \( g(2) = 2 = a(2) \); also \( g(1) = a(1) = 1 \). Diagonalizable, with eigenvectors \( \e_1 \) for \( 1 \) and \( (1, 1, 0), \e_3 \) for \( 2 \).

Hence \( \A_t \) is diagonalizable over \( \nR \) if and only if \( t \ne 1 \). In both exceptional cases a diagonal entry is repeated, but only for \( t = 1 \) is an eigenvector lost: the entry \( 1 \) in position \( (1, 2) \) couples \( \e_1 \) and \( \e_2 \), and it matters only when their diagonal entries agree.
:::

### C. Going deeper

:::: {#exr-diagonalization-c1}
[C1: Matrices with \( \A^k = \I \)]

Let \( \A \in M_n(\nC) \), \( n \ge 1 \), and \( k \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( \A^k = \I \), then every eigenvalue \( \lambda \) of \( \A \) satisfies \( \lambda^k = 1 \).
2. Prove that if \( \A \) is diagonalizable and every eigenvalue satisfies \( \lambda^k = 1 \), then \( \A^k = \I \).
3. Show that the hypothesis "diagonalizable" in (b) cannot be dropped.
:::
::::

::: {.solution}
(a) Let \( \A\v = \lambda\v \) with \( \v \ne \0 \). By @exr-eigenvalues-and-eigenvectors-b3 (a), \( \v = \I\v = \A^k\v = \lambda^k\v \), so \( (\lambda^k - 1)\v = \0 \) and \( \lambda^k = 1 \) by @thm-zero-product.

(b) Write \( \A = \P \D \P^{-1} \) with \( \D = \diag(d_1, \dots, d_n) \) (@def-diagonalizable). The \( d_i \) are eigenvalues of \( \A \): \( \D \) and \( \A \) are similar, so \( p_{\D} = p_{\A} \) (@thm-charpoly-similarity-invariant), and each \( d_i \) is a root of \( p_{\D} = \prod_j (x - d_j) \). So \( d_i^k = 1 \) for all \( i \), and by @thm-powers-diagonalizable, \( \A^k = \P\,\diag(d_1^k, \dots, d_n^k)\,\P^{-1} = \P \I \P^{-1} = \I \).

(c) Let \( \J = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \). Its only eigenvalue is \( 1 \), and \( 1^k = 1 \). But \( \J^k = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix} \) by induction (\( \J^{k+1} = \J^k\J \)), which is not \( \I \) since \( k \ne 0 \) in \( \nC \). (Section 8 proves the converse of (b) in a strong form: over \( \nC \), \( \A^k = \I \) forces \( \A \) to be diagonalizable.)
:::

:::: {#exr-diagonalization-c2}
[C2: Polynomials of diagonalizable matrices]

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( \A \in M_n(F) \) is diagonalizable over \( F \), then so is \( p(\A) \) for every \( p \in F[x] \), and that every eigenvalue of \( p(\A) \) has the form \( p(\lambda) \) with \( \lambda \in \spec(\A) \).
2. Show that the converse of the first statement fails: find a non-diagonalizable \( \A \) and a polynomial \( p \) with \( p(\A) \) diagonalizable.
:::
::::

::: {.solution}
(a) Let \( \A = \P \D \P^{-1} \), \( \D = \diag(d_1, \dots, d_n) \). By @thm-powers-diagonalizable, \( p(\A) = \P\,\diag(p(d_1), \dots, p(d_n))\,\P^{-1} \), so \( p(\A) \) is similar to a diagonal matrix, that is, diagonalizable. By @thm-charpoly-similarity-invariant, \( p_{p(\A)} = \prod_i (x - p(d_i)) \), so by @thm-eigenvalue-characterizations every eigenvalue of \( p(\A) \) is some \( p(d_i) \). As in @exr-diagonalization-c1 (b), each \( d_i \) is an eigenvalue of \( \A \).

(b) Let \( \A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) and \( p = x^2 \). Then \( \A \) is not diagonalizable: \( p_{\A} = x^2 \) gives \( a(0) = 2 \), while \( \rank \A = 1 \) gives \( g(0) = 1 \) (@thm-diagonalization (e)). But \( p(\A) = \A^2 = 0 \) is diagonal.
:::

:::: {#exr-diagonalization-c3}
[C3: The transpose map on \( M_n(F) \)]

Let \( n \ge 1 \) and \( \tau \colon M_n(F) \to M_n(F) \), \( \tau(\X) = \X\tp \).

::: {.enumerate options="label=(\alph*)"}
1. Suppose the characteristic of \( F \) is not \( 2 \). Prove that \( \tau \) is diagonalizable, and find \( \dim E_1(\tau) \) and \( \dim E_{-1}(\tau) \).
2. Under the same hypothesis, deduce \( p_\tau \), \( \tr\tau \) and \( \det\tau \).
3. Now let \( F = \nF_2 \) and \( n \ge 2 \). Prove that \( \tau \) is **not** diagonalizable.
:::

*Hint: for the dimensions, use the matrices \( \E_{ij} + \E_{ji} \) and \( \E_{ij} - \E_{ji} \).*
::::

::: {.solution}
(a) Since \( (\X\tp)\tp = \X \) (@thm-transpose-properties), \( \tau^2 = \id \). By @thm-involution-decomposition, \( M_n(F) = E_{+} \oplus E_{-} \), where \( E_{+} = E_1(\tau) \) is the space of symmetric matrices and \( E_{-} = E_{-1}(\tau) \) the space of skew-symmetric matrices.

A symmetric \( \X = (x_{ij}) \) is determined by its entries on and above the diagonal, and \( \X = \sum_i x_{ii}\E_{ii} + \sum_{i < j} x_{ij}(\E_{ij} + \E_{ji}) \). These \( n + \binom{n}{2} \) matrices are symmetric and independent, since their non-zero entries sit in disjoint positions. So \( \dim E_1(\tau) = n(n+1)/2 \). A skew-symmetric \( \X \) has \( x_{ii} = -x_{ii} \), so \( 2x_{ii} = 0 \) and \( x_{ii} = 0 \) (as \( 2 \ne 0 \)); and \( \X = \sum_{i < j} x_{ij}(\E_{ij} - \E_{ji}) \), with these \( \binom{n}{2} \) matrices independent for the same reason. So \( \dim E_{-1}(\tau) = n(n-1)/2 \).

The eigenvalues of \( \tau \) lie among \( \pm 1 \) (as in @exr-eigenvalues-and-eigenvectors-b2), and \( n(n+1)/2 + n(n-1)/2 = n^2 = \dim M_n(F) \). If \( n \ge 2 \), both eigenspaces are non-zero, and the dimensions of the eigenspaces add up to \( n^2 \); if \( n = 1 \), \( \tau = \id \) and \( E_1(\tau) \) is everything. Either way @thm-diagonalization ((d) \( \Rightarrow \) (a)) shows that \( \tau \) is diagonalizable.

(b) In a basis \( \sB \) of eigenvectors, \( \mtx{\tau}{\sB}{\sB} = \diag(1, \dots, 1, -1, \dots, -1) \) with \( n(n+1)/2 \) ones and \( n(n-1)/2 \) entries \( -1 \) (@thm-diagonalization). This matrix is triangular, so
\[
\begin{aligned}
p_\tau &= (x - 1)^{n(n+1)/2}(x + 1)^{n(n-1)/2}, \\
\tr\tau &= \frac{n(n+1)}{2} - \frac{n(n-1)}{2} = n, \\
\det\tau &= (-1)^{n(n-1)/2}.
\end{aligned}
\]
As a check on the trace: in the basis \( \sE = (\E_{ij}) \), \( \tau(\E_{ij}) = \E_{ji} \), so the diagonal entry of \( \mtx{\tau}{\sE}{\sE} \) at \( \E_{ij} \) is \( 1 \) if \( i = j \) and \( 0 \) otherwise, and the trace is \( n \).

(c) Over \( \nF_2 \), \( -1 = 1 \). If \( \tau(\X) = \lambda \X \) with \( \X \ne 0 \), then as in @exr-eigenvalues-and-eigenvectors-b2 (a), \( \lambda^2 = 1 \), so \( (\lambda - 1)^2 = \lambda^2 - 2\lambda + 1 = \lambda^2 + 1 = 0 \) and \( \lambda = 1 \). So \( \spec(\tau) = \{1\} \) and \( E_1(\tau) \) is the space of symmetric matrices. The spanning argument in (a) did not divide by \( 2 \), so \( \dim E_1(\tau) = n(n+1)/2 \). For \( n \ge 2 \), \( n(n+1)/2 < n^2 \), so condition (d) of @thm-diagonalization fails, and \( \tau \) is not diagonalizable. For instance, \( \E_{12} \) is not a sum of eigenvectors.
:::
