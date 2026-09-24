# The Complex Spectral Theorem

Two things are now on the table. Section 1 put every complex operator into upper triangular form in an **orthonormal** basis, and Section 3 identified the operators that commute with their adjoints. Put them together and the chapter's main theorem falls out in a few lines: a triangular matrix that is normal has nothing above the diagonal. This section proves that, reads off the consequences, and says exactly how much of the resulting picture is unique.

The field is \( \nC \) throughout this section, and every inner product space is finite-dimensional. The reason for insisting on \( \nC \) is Schur's theorem, and behind it the Fundamental Theorem of Algebra (@thm-fundamental-theorem-of-algebra): over \( \nR \) an operator can fail to have a single eigenvector, and Section 5 shows what has to change.

## Triangular plus normal forces diagonal

Start with the smallest case, where the mechanism is visible at a glance. Let
\[
\A = \begin{pmatrix} a & b \\ 0 & d \end{pmatrix} \in M_2(\nC)
\]
be upper triangular. The \( (1,1) \) entry of \( \A^{*}\A \) is the squared length of the first **column** of \( \A \), and the \( (1,1) \) entry of \( \A\A^{*} \) is the squared length of the first **row**:
\[
(\A^{*}\A)_{11} = \lvert a\rvert^2,
\qquad
(\A\A^{*})_{11} = \lvert a\rvert^2 + \lvert b\rvert^2 .
\]
If \( \A \) is normal these are equal, so \( \lvert b\rvert^2 = 0 \) and \( b = 0 \). One entry of one product did all the work. (This is @exr-normal-operators-b3, which you may already have done.)

The general case is the same comparison run down the diagonal, one row at a time. Nothing is clever; the only care needed is to use, at step \( j \), the zeros that steps \( 1, \dots, j-1 \) have already produced.

::: {#lem-triangular-normal-diagonal}
[A Normal Triangular Matrix Is Diagonal]

Let \( \T = (t_{ij}) \in M_n(\nC) \) be upper triangular and normal. Then \( \T \) is diagonal.
:::

::: {.idea}
For any square matrix, the \( j \)-th diagonal entry of \( \T^{*}\T \) is the squared length of column \( j \), and the \( j \)-th diagonal entry of \( \T\T^{*} \) is the squared length of row \( j \). Normality says those two lengths agree for every \( j \). For an upper triangular matrix, column \( j \) reaches only down to the diagonal and row \( j \) only rightwards from it, so the equation compares "what sits above \( t_{jj} \)" with "what sits to the right of \( t_{jj} \)". Row \( 1 \) has nothing above it, so the right side must be empty too; that clears row \( 1 \), which empties the column sums one step further down, and the argument walks down the diagonal.
:::

::: {.proof}
For each \( j \), computing the \( (j, j) \) entries of the two products entry by entry,
\[
(\T^{*}\T)_{jj} = \sum_{i=1}^{n} \conj{t_{ij}}\,t_{ij} = \sum_{i=1}^{n} \lvert t_{ij}\rvert^2,
\qquad
(\T\T^{*})_{jj} = \sum_{k=1}^{n} \lvert t_{jk}\rvert^2 .
\]
Since \( \T \) is upper triangular, \( t_{ij} = 0 \) whenever \( i > j \), and \( t_{jk} = 0 \) whenever \( k < j \). So normality of \( \T \) says
\[
\sum_{i \le j} \lvert t_{ij}\rvert^2 = \sum_{k \ge j} \lvert t_{jk}\rvert^2
\qquad (j = 1, \dots, n).
\]{#eq-normal-row-column}

We prove by induction on \( j \) that \( t_{jk} = 0 \) for every \( k > j \).

**Base case \( j = 1 \).** The left-hand side of @eq-normal-row-column has the single term \( \lvert t_{11}\rvert^2 \), so
\[
\lvert t_{11}\rvert^2 = \lvert t_{11}\rvert^2 + \sum_{k > 1} \lvert t_{1k}\rvert^2 .
\]
Hence \( \sum_{k>1}\lvert t_{1k}\rvert^2 = 0 \), a sum of non-negative reals, so \( t_{1k} = 0 \) for every \( k > 1 \).

**Inductive step.** Let \( 1 < j \le n \) and suppose \( t_{mk} = 0 \) whenever \( m < j \) and \( k > m \). In the left-hand side of @eq-normal-row-column, every term with \( i < j \) is \( \lvert t_{ij}\rvert^2 \) with \( i < j \), hence with \( j > i \); by the inductive hypothesis, taking \( m = i \) and \( k = j \), each such \( t_{ij} \) is \( 0 \). So the left-hand side reduces to \( \lvert t_{jj}\rvert^2 \) and @eq-normal-row-column becomes
\[
\lvert t_{jj}\rvert^2 = \lvert t_{jj}\rvert^2 + \sum_{k > j} \lvert t_{jk}\rvert^2 ,
\]
whence \( t_{jk} = 0 \) for every \( k > j \), again because a sum of non-negative reals vanishes only when every term does.

By induction, every entry strictly above the diagonal is zero. Every entry strictly below it is zero because \( \T \) is upper triangular. So \( \T \) is diagonal, as claimed.
:::

Note what the proof did **not** need: no eigenvector was chosen, no dimension was inducted on, no subspace was split off. The whole argument is an identity between two lists of non-negative numbers. That is why it also survives, unchanged in spirit, into the block version used in Section 5 and the quantitative version in Section 11.

## The theorem

::: {#thm-spectral-complex}
[Complex Spectral Theorem]

Let \( V \) be a finite-dimensional inner product space over \( \nC \) and let \( T \in \cL(V) \). The following are equivalent.

::: {.enumerate options="label=(\alph*)"}
1. \( T \) is normal.
2. \( V \) has an orthonormal basis consisting of eigenvectors of \( T \).
:::
:::

::: {.idea}
\( (\Leftarrow) \) is a one-line check: in such a basis the matrix of \( T \) is diagonal, the matrix of \( T^{*} \) is its conjugate transpose, and two diagonal matrices commute. \( (\Rightarrow) \) is Schur plus the lemma: take an orthonormal basis making the matrix triangular, observe that normality of \( T \) is normality of that matrix because the basis is orthonormal, and apply @lem-triangular-normal-diagonal. A diagonal matrix in the basis \( \sB \) says precisely that each vector of \( \sB \) is an eigenvector.
:::

::: {.proof}
\( (\Leftarrow) \) Suppose \( \sB = (\e_1, \dots, \e_n) \) is an orthonormal basis with \( T\e_j = \lambda_j\e_j \) for each \( j \). Then \( \D \coloneqq \mtx{T}{\sB}{\sB} = \diag(\lambda_1, \dots, \lambda_n) \), and since \( \sB \) is orthonormal, \( \mtx{T^{*}}{\sB}{\sB} = \D^{*} = \diag(\conj{\lambda_1}, \dots, \conj{\lambda_n}) \) by @thm-matrix-of-adjoint. Both products are the same diagonal matrix:
\[
\D^{*}\D = \D\D^{*} = \diag\bigl(\lvert\lambda_1\rvert^2, \dots, \lvert\lambda_n\rvert^2\bigr) .
\]
Taking the matrix of an operator in a fixed basis turns composition into matrix multiplication and is injective (@thm-matrix-of-composition, @thm-linear-maps-isomorphic-to-matrices), so \( T^{*}T = TT^{*} \).

\( (\Rightarrow) \) Suppose \( T \) is normal. By Schur's theorem (@thm-schur-triangularization) there is an orthonormal basis \( \sB = (\e_1, \dots, \e_n) \) of \( V \) in which \( \T \coloneqq \mtx{T}{\sB}{\sB} \) is upper triangular. Because \( \sB \) is orthonormal, @thm-matrix-of-adjoint gives \( \mtx{T^{*}}{\sB}{\sB} = \T^{*} \), so the equation \( T^{*}T = TT^{*} \) reads \( \T^{*}\T = \T\T^{*} \): the matrix \( \T \) is normal. By @lem-triangular-normal-diagonal, \( \T \) is diagonal, say \( \T = \diag(\lambda_1, \dots, \lambda_n) \). Reading off the \( j \)-th column (@def-matrix-of-linear-map), \( T\e_j = \lambda_j\e_j \), and \( \e_j \neq \0 \) because \( \norm{\e_j} = 1 \). So \( \sB \) is an orthonormal basis of eigenvectors of \( T \). This proves the theorem.
:::

::: {#cor-spectral-complex-matrix}
[Unitary Diagonalization]

Let \( \A \in M_n(\nC) \). Then \( \A \) is normal if and only if there exist a unitary \( \U \in \Unit(n) \) and a diagonal \( \D \in M_n(\nC) \) with
\[
\A = \U\D\U^{*} .
\]
A matrix admitting such a factorization is called **unitarily diagonalizable**. The diagonal of \( \D \) is the list of eigenvalues of \( \A \) with multiplicity, in an order that may be prescribed in advance, and the columns of \( \U \) are a corresponding orthonormal basis of eigenvectors.
:::

::: {.proof}
Apply @thm-spectral-complex to the operator \( T_{\A} \) on \( \nC^n \) with its standard inner product, for which the standard basis is orthonormal.

\( (\Rightarrow) \) Let \( (\u_1, \dots, \u_n) \) be an orthonormal basis of eigenvectors, \( \A\u_j = \lambda_j\u_j \), and let \( \U \) be the matrix with these columns; it is unitary because its columns are orthonormal (@thm-isometry-characterizations (f)). Then \( \A\U \) has \( j \)-th column \( \lambda_j\u_j \), which is the \( j \)-th column of \( \U\D \) for \( \D = \diag(\lambda_1, \dots, \lambda_n) \). So \( \A\U = \U\D \) and \( \A = \U\D\U^{-1} = \U\D\U^{*} \).

\( (\Leftarrow) \) If \( \A = \U\D\U^{*} \) then \( \A^{*} = \U\D^{*}\U^{*} \), and
\[
\A^{*}\A = \U\D^{*}\D\U^{*} = \U\D\D^{*}\U^{*} = \A\A^{*},
\]
using \( \U^{*}\U = \I \) twice and the fact that diagonal matrices commute.

Finally, \( \A \) is similar to \( \D \), so they have the same characteristic polynomial (@thm-charpoly-similarity-invariant), and the roots of \( \det(x\I - \D) = \prod_j (x - \lambda_j) \) are the diagonal entries with multiplicity. Reordering the eigenvectors reorders the columns of \( \U \) and the diagonal of \( \D \) in the same way, so any order may be prescribed.
:::

::: {#exm-unitarily-diagonalize-hermitian}
[Unitarily diagonalizing a Hermitian matrix]

Find a unitary \( \U \) and a diagonal \( \D \) with \( \U^{*}\A\U = \D \), for
\[
\A = \begin{pmatrix} 2 & 1 - i \\ 1 + i & 3 \end{pmatrix} .
\]
:::

::: {.solution}
\( \A^{*} = \A \), so \( \A \) is Hermitian, hence normal, and @cor-spectral-complex-matrix applies. Its characteristic polynomial is
\[
\begin{aligned}
x^2 - (\tr \A)x + \det \A
&= x^2 - 5x + \bigl(6 - (1-i)(1+i)\bigr) \\
&= x^2 - 5x + 4,
\end{aligned}
\]
since \( (1-i)(1+i) = 1 - i^2 = 2 \). So the eigenvalues are \( 4 \) and \( 1 \), both real as @thm-self-adjoint-real-eigenvalues promises.

For \( \lambda = 4 \), the first row of \( \A - 4\I = \begin{pmatrix} -2 & 1-i \\ 1+i & -1 \end{pmatrix} \) gives \( -2z_1 + (1-i)z_2 = 0 \); taking \( z_2 = 2 \) gives \( \u = (1 - i,\, 2) \), with \( \norm{\u}^2 = 2 + 4 = 6 \).

For \( \lambda = 1 \), the first row of \( \A - \I = \begin{pmatrix} 1 & 1-i \\ 1+i & 2 \end{pmatrix} \) gives \( z_1 = -(1-i)z_2 \); taking \( z_2 = 1 \) gives \( \w = (-1 + i,\, 1) \), with \( \norm{\w}^2 = 2 + 1 = 3 \).

The two are orthogonal, as @cor-normal-orthogonal-eigenspaces predicts:
\[
\begin{aligned}
\inner{\u}{\w}
&= (1-i)\conj{(-1+i)} + 2 \cdot \conj{1} \\
&= (1-i)(-1-i) + 2 = -2 + 2 = 0 .
\end{aligned}
\]
Normalizing and using them as columns,
\[
\U = \begin{pmatrix} \tfrac{1-i}{\sqrt6} & \tfrac{-1+i}{\sqrt3} \\[2pt] \tfrac{2}{\sqrt6} & \tfrac{1}{\sqrt3} \end{pmatrix},
\qquad
\D = \begin{pmatrix} 4 & 0 \\ 0 & 1 \end{pmatrix},
\]
and \( \U^{*}\U = \I \), \( \U^{*}\A\U = \D \). As a check on the arithmetic, \( \tr \D = 5 = \tr \A \) and \( \det \D = 4 = \det \A \).
:::

## Reading the class off the spectrum

Once the eigenvalues sit on a diagonal, every question about \( T \) that is invariant under a unitary change of basis becomes a question about a list of complex numbers. Here are three answers.

::: {#cor-normal-spectral-corollaries}
[The Spectrum Decides]

Let \( T \in \cL(V) \) be normal on a finite-dimensional complex inner product space.

::: {.enumerate options="label=(\alph*)"}
1. \( T \) is self-adjoint if and only if every eigenvalue of \( T \) is real.
2. \( T \) is unitary if and only if every eigenvalue of \( T \) has modulus \( 1 \).
3. \( \inner{T\v}{\v} \) is a non-negative real number for every \( \v \in V \) if and only if every eigenvalue of \( T \) is a non-negative real.
:::
:::

::: {.idea}
By @thm-spectral-complex there is an orthonormal basis \( (\e_1, \dots, \e_n) \) with \( T\e_j = \lambda_j\e_j \), and then \( T^{*}\e_j = \conj{\lambda_j}\e_j \) by @thm-normal-eigenvector-shared. Two operators that agree on a basis are equal, so each of the three conditions can be tested one basis vector at a time, where it becomes a statement about the single number \( \lambda_j \).
:::

::: {.proof}
Fix an orthonormal basis \( (\e_1, \dots, \e_n) \) of eigenvectors, \( T\e_j = \lambda_j\e_j \) (@thm-spectral-complex), and recall \( T^{*}\e_j = \conj{\lambda_j}\e_j \) (@thm-normal-eigenvector-shared). Every eigenvalue of \( T \) occurs among \( \lambda_1, \dots, \lambda_n \), because \( \diag(\lambda_1, \dots, \lambda_n) \) is the matrix of \( T \) and its characteristic polynomial is \( \prod_j (x - \lambda_j) \).

(a) \( T = T^{*} \) holds if and only if \( T\e_j = T^{*}\e_j \) for every \( j \) (@thm-linear-transform-basis), that is \( \lambda_j\e_j = \conj{\lambda_j}\e_j \), that is \( \lambda_j = \conj{\lambda_j} \) since \( \e_j \neq \0 \). A complex number equals its conjugate exactly when it is real.

(b) \( T^{*}T\e_j = T^{*}(\lambda_j\e_j) = \lambda_j\conj{\lambda_j}\e_j = \lvert\lambda_j\rvert^2\e_j \), so \( T^{*}T = \id_V \) if and only if \( \lvert\lambda_j\rvert^2 = 1 \) for every \( j \). That is what it means for \( T \) to be unitary (@def-unitary-orthogonal): the equation \( T^{*}T = \id_V \) makes \( T \) injective, hence invertible on a finite-dimensional space (@thm-invertible-operator-tfae), with \( T^{-1} = T^{*} \) and therefore \( TT^{*} = \id_V \) as well.

(c) Write \( \v = \sum_j c_j\e_j \). Expanding both slots and using \( \inner{\e_j}{\e_i} = \delta_{ij} \),
\[
\inner{T\v}{\v} = \Bigl\langle \sum_j c_j\lambda_j\e_j, \sum_i c_i\e_i \Bigr\rangle = \sum_j \lambda_j\lvert c_j\rvert^2 .
\]
\( (\Leftarrow) \) If every \( \lambda_j \) is a non-negative real, this is a sum of non-negative reals. \( (\Rightarrow) \) Taking \( \v = \e_j \) gives \( \inner{T\e_j}{\e_j} = \lambda_j \), which is then a non-negative real by hypothesis.
:::

Part (c) names a class that Chapter 13 takes as its subject: the **positive** operators. Over \( \nC \) the hypothesis of normality is not really needed in (c), because \( \inner{T\v}{\v} \) real for every \( \v \) already forces \( T = T^{*} \): apply @thm-complex-zero-test to the operator \( T - T^{*} \), for which \( \inner{(T - T^{*})\v}{\v} = \inner{T\v}{\v} - \conj{\inner{T\v}{\v}} = 0 \). Over \( \nR \) that shortcut is unavailable, and Section 5 shows the quarter turn defeating it.

The next corollary is a small shock. The adjoint is defined through the inner product and has nothing to do with polynomials. For a normal operator it is one anyway.

::: {#cor-normal-commuting-poly}
[The Adjoint of a Normal Operator Is a Polynomial in It]

Let \( T \in \cL(V) \) be normal on a finite-dimensional complex inner product space, with distinct eigenvalues \( \lambda_1, \dots, \lambda_k \). Then there is a polynomial \( p \in \nC[x] \) of degree less than \( k \) with \( T^{*} = p(T) \).
:::

::: {.proof}
The scalars \( \lambda_1, \dots, \lambda_k \) are distinct, so by Lagrange interpolation (@thm-lagrange-interpolation) there is a polynomial \( p \in \nC[x] \) of degree less than \( k \) with
\[
p(\lambda_i) = \conj{\lambda_i} \qquad (i = 1, \dots, k) .
\]
Let \( (\e_1, \dots, \e_n) \) be an orthonormal basis of eigenvectors (@thm-spectral-complex), with \( T\e_j = \mu_j\e_j \) where each \( \mu_j \) is one of the \( \lambda_i \). Then \( p(T)\e_j = p(\mu_j)\e_j = \conj{\mu_j}\e_j = T^{*}\e_j \), the first equality because \( T^{i}\e_j = \mu_j^{i}\e_j \) for every \( i \ge 0 \), by induction from \( T\e_j = \mu_j\e_j \), and the last by @thm-normal-eigenvector-shared. The operators \( p(T) \) and \( T^{*} \) agree on a basis, hence are equal (@thm-linear-transform-basis).
:::

One consequence is worth stating on its own. Any operator \( S \) that commutes with \( T \) also commutes with every polynomial in \( T \), hence with \( T^{*} \). So for normal operators the apparently stronger requirement "commutes with \( T \) and with \( T^{*} \)" is no requirement at all, and Section 7 will use this to diagonalize whole commuting families at once. The polynomial depends on \( T \) and not only on its size: for \( T = \id_V \) one may take the constant \( p = 1 \), while for the matrix \( \diag(1, i) \) the conditions \( p(1) = 1 \) and \( p(i) = -i \) are met by
\[
p(x) = ix + (1 - i),
\]
as one checks by substituting \( x = 1 \) and \( x = i \).

## Exactly what is unique

The factorization \( \A = \U\D\U^{*} \) is not unique, and it is worth being precise about which parts of it are.

Unique: the **set** of eigenvalues \( \spec(T) \), and for each \( \lambda \in \spec(T) \) the eigenspace \( E_{\lambda}(T) \) with its dimension. These are defined from \( T \) alone, without any choice. Consequently the diagonal of \( \D \) is unique **as a list with multiplicities up to reordering**: each \( \lambda \) appears exactly \( \dim E_{\lambda}(T) \) times.

Not unique: the order of the diagonal, and the matrix \( \U \). Two freedoms create all the others. First, permuting the eigenvectors permutes the columns of \( \U \) and the diagonal of \( \D \) in step. Second, within a single eigenspace \( E_{\lambda}(T) \) of dimension \( m \), **any** orthonormal basis of that eigenspace will do, and there are many when \( m \ge 2 \): the choices are related by the unitary maps of \( E_{\lambda}(T) \). For \( \A = \I_n \), for instance, every unitary \( \U \) satisfies \( \U^{*}\A\U = \I_n \). What no freedom can change is that eigenvectors for distinct eigenvalues stay orthogonal (@cor-normal-orthogonal-eigenspaces), so the decomposition
\[
V = E_{\lambda_1}(T) \oplus \dots \oplus E_{\lambda_k}(T)
\]
into mutually orthogonal eigenspaces is itself unique. Section 8 turns that decomposition into the spectral resolution and shows it determines \( T \) completely.

::: {.check}
The matrix \( \A = \diag(1, 1, 2) \) is normal. Write down two different unitary matrices \( \U \) with \( \U^{*}\A\U = \A \), and explain why, for \( \diag(1, 2, 3) \) with the order of the diagonal fixed, the freedom shrinks to a single unit-modulus scalar on each column.
:::

::: {.solution}
Take \( \U_1 = \I_3 \) and \( \U_2 = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} \); more generally \( \R \oplus (1) \) works for **any** \( \R \in \Unit(2) \), because \( \A = \I_2 \oplus (2) \) and \( \R^{*}\I_2\R = \I_2 \). The freedom comes from the two-dimensional eigenspace \( E_1(\A) = \Span(\e_1, \e_2) \), inside which every orthonormal basis is as good as any other. For \( \diag(1,2,3) \) each eigenspace is a line, and a line has exactly two unit vectors over \( \nR \) and a circle of them over \( \nC \); the residual freedom is only the scalar factor of modulus \( 1 \) in each column, which changes \( \U \) but not the decomposition into eigenspaces.
:::

::: {.warning}
**"Diagonalizable" and "unitarily diagonalizable" are different conditions.** Every unitarily diagonalizable matrix is diagonalizable, because \( \U \) is in particular invertible. The converse fails, and it fails for matrices as small and as ordinary as \( \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix} \). Having \( n \) distinct eigenvalues guarantees diagonalizability (@cor-distinct-eigenvalues-diagonalizable) and guarantees nothing about orthogonality.
:::

::: {#exm-diagonalizable-not-normal}
[Diagonalizable, and no orthonormal eigenbasis]

For \( \A = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix} \in M_2(\nR) \), find an invertible \( \P \) with \( \P^{-1}\A\P \) diagonal, and show that no **orthogonal** \( \Q \) makes \( \Q\tp\A\Q \) diagonal.
:::

::: {.solution}
The matrix is upper triangular, so its eigenvalues are the diagonal entries \( 1 \) and \( 2 \) (@thm-det-triangular). For \( \lambda = 1 \), \( \A - \I = \begin{pmatrix} 0 & 1 \\ 0 & 1 \end{pmatrix} \) has kernel spanned by \( (1, 0) \). For \( \lambda = 2 \), \( \A - 2\I = \begin{pmatrix} -1 & 1 \\ 0 & 0 \end{pmatrix} \) has kernel spanned by \( (1, 1) \). Two distinct eigenvalues in dimension \( 2 \) give a basis of eigenvectors (@cor-distinct-eigenvalues-diagonalizable), so with
\[
\P = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}
\quad\text{we get}\quad
\P^{-1}\A\P = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}.
\]
Now suppose \( \Q\tp\A\Q = \D \) were diagonal with \( \Q \) orthogonal. Then \( \A = \Q\D\Q\tp \) would be normal by @cor-spectral-complex-matrix. But
\[
\A\tp\A = \begin{pmatrix} 1 & 1 \\ 1 & 5 \end{pmatrix}
\neq
\begin{pmatrix} 2 & 2 \\ 2 & 4 \end{pmatrix} = \A\A\tp ,
\]
so \( \A \) is not normal and no such \( \Q \) exists. The obstruction is visible without any theory: the eigenvectors are \( (1,0) \) and \( (1,1) \), the eigenspaces are lines and therefore the *only* candidates for eigenvector directions, and \( (1,0)\cdot(1,1) = 1 \neq 0 \). There simply is no orthogonal pair of eigenvectors to build \( \Q \) from.
:::

## Exercises

### A. Check your understanding

::: {#exr-spectral-theorem-complex-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the complex spectral theorem, including every hypothesis, and state its matrix form.
2. What goes wrong with the proof if the field is \( \nR \)? Name the exact step.
3. True or false: a matrix in \( M_n(\nC) \) with \( n \) distinct eigenvalues is unitarily diagonalizable. Justify your answer.
4. Let \( \A \in M_3(\nC) \) be normal with \( \spec(\A) = \{2, 2, -1\} \) as a list with multiplicity. Is the unitary \( \U \) in \( \A = \U\D\U^{*} \) determined by \( \A \) and the order of \( \D \)? What is determined?
5. A normal operator \( T \) satisfies \( T^{*} = T^{3} \). What can you say about its eigenvalues?
6. Explain why @lem-triangular-normal-diagonal cannot be weakened to "a normal matrix with some of its below-diagonal entries zero is diagonal".
:::
:::

::: {.solution}
(a) For a finite-dimensional inner product space \( V \) over \( \nC \) and \( T \in \cL(V) \): \( T \) is normal if and only if \( V \) has an orthonormal basis of eigenvectors of \( T \) (@thm-spectral-complex). Matrix form: \( \A \in M_n(\nC) \) is normal if and only if \( \A = \U\D\U^{*} \) with \( \U \) unitary and \( \D \) diagonal (@cor-spectral-complex-matrix).

(b) Schur's theorem. It needs an eigenvalue at every stage of its induction, which over \( \nC \) comes from @thm-fundamental-theorem-of-algebra; over \( \nR \) an operator may have none at all, and then there is no triangular form to start from.

(c) False. \( \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix} \) has the distinct eigenvalues \( 1 \) and \( 2 \) and is not normal, hence is not unitarily diagonalizable (@exm-diagonalizable-not-normal).

(d) No. The eigenspace \( E_2(\A) \) is two-dimensional, and replacing its orthonormal basis by any other one changes \( \U \) while leaving \( \D \) alone. What is determined: \( \spec(\A) = \{2, -1\} \), the eigenspaces \( E_2(\A) \) and \( E_{-1}(\A) \), their dimensions \( 2 \) and \( 1 \), and their mutual orthogonality.

(e) By @thm-normal-eigenvector-shared, \( T\v = \lambda\v \) gives \( T^{*}\v = \conj{\lambda}\v \), while \( T^{*} = T^3 \) gives \( T^{*}\v = \lambda^3\v \). Hence \( \conj{\lambda} = \lambda^3 \). Taking moduli, \( \lvert\lambda\rvert = \lvert\lambda\rvert^3 \), so \( \lvert\lambda\rvert \) is \( 0 \) or \( 1 \). If \( \lambda \neq 0 \), multiplying \( \conj{\lambda} = \lambda^3 \) by \( \lambda \) gives \( \lvert\lambda\rvert^2 = \lambda^4 \), that is \( \lambda^4 = 1 \). So every eigenvalue lies in \( \{0, 1, -1, i, -i\} \).

(f) The lemma uses triangularity at **every** index, not at a few places: the comparison of row and column lengths at step \( j \) is informative only because the whole of column \( j \) below the diagonal is already known to vanish. Zeros in some of those positions buy nothing. The circulant \( \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix} \) is normal and has zeros in positions \( (2,1) \) and \( (3,2) \), two of the three places below its diagonal, and it is not diagonal.
:::

### B. Practice

::: {#exr-spectral-theorem-complex-b1}
[B1: Unitarily diagonalize]

For each matrix, find a unitary \( \U \) and a diagonal \( \D \) with \( \U^{*}\A\U = \D \).

::: {.enumerate options="label=(\alph*)"}
1. \( \A = \begin{pmatrix} 3 & -i \\ i & 3 \end{pmatrix} \).
2. \( \A = \tfrac1{\sqrt2}\begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix} \).
:::
:::

::: {.solution}
(a) \( \A^{*} = \A \), so \( \A \) is Hermitian and normal. Its characteristic polynomial is \( x^2 - 6x + (9 - (-i)(i)) = x^2 - 6x + 8 \), with roots \( 4 \) and \( 2 \).

For \( \lambda = 4 \): \( \A - 4\I = \begin{pmatrix} -1 & -i \\ i & -1 \end{pmatrix} \), and the first row gives \( z_1 = -iz_2 \); take \( \u = (-i, 1) \), \( \norm{\u}^2 = 2 \). For \( \lambda = 2 \): \( \A - 2\I = \begin{pmatrix} 1 & -i \\ i & 1 \end{pmatrix} \), and the first row gives \( z_1 = iz_2 \); take \( \w = (i, 1) \), \( \norm{\w}^2 = 2 \). They are orthogonal: \( \inner{\u}{\w} = (-i)\conj{i} + 1 = (-i)(-i) + 1 = -1 + 1 = 0 \). Hence
\[
\U = \tfrac1{\sqrt2}\begin{pmatrix} -i & i \\ 1 & 1 \end{pmatrix},
\qquad
\D = \begin{pmatrix} 4 & 0 \\ 0 & 2 \end{pmatrix}.
\]

(b) \( \A \) is unitary (@exm-normal-catalog (c)), hence normal. Here \( \tr \A = \sqrt2 \) and \( \det \A = \tfrac12(1 - i^2) = 1 \), so the characteristic polynomial is \( x^2 - \sqrt2 x + 1 \), with roots
\[
x = \frac{\sqrt2 \pm \sqrt{2 - 4}}{2} = \frac{1 \pm i}{\sqrt2},
\]
both of modulus \( 1 \), as @cor-normal-spectral-corollaries (b) requires. For \( \lambda = (1+i)/\sqrt2 \), the equation \( \A\z = \lambda\z \) reads \( \tfrac1{\sqrt2}(z_1 + iz_2) = \tfrac{1+i}{\sqrt2}z_1 \), that is \( iz_2 = iz_1 \), so \( \u = (1, 1) \). For \( \lambda = (1-i)/\sqrt2 \) the same line gives \( iz_2 = -iz_1 \), so \( \w = (1, -1) \). These are orthogonal, so
\[
\U = \tfrac1{\sqrt2}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix},
\qquad
\D = \tfrac1{\sqrt2}\begin{pmatrix} 1 + i & 0 \\ 0 & 1 - i \end{pmatrix} .
\]
Here \( \U \) is real orthogonal even though \( \A \) is not real.
:::

::: {#exr-spectral-theorem-complex-b2}
[B2: A circulant, diagonalized]

Let \( \omega = e^{2\pi i/3} \), so \( \omega^3 = 1 \) and \( 1 + \omega + \omega^2 = 0 \), and let
\[
\C = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix} \in M_3(\nC) .
\]

::: {.enumerate options="label=(\alph*)"}
1. Verify that \( \C \) is normal.
2. Show that \( \f_j = \tfrac1{\sqrt3}(1, \omega^{j}, \omega^{2j}) \) is an eigenvector of \( \C \) for \( j = 0, 1, 2 \), and find the eigenvalue.
3. Deduce a unitary \( \F \) with \( \F^{*}\C\F \) diagonal, and write down the diagonal explicitly.
:::
:::

::: {.solution}
(a) Both products are the same matrix:
\[
\C^{*}\C = \C\C^{*} = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix} .
\]
(The entries are dot products of pairs of rows, respectively columns, of \( \C \); cyclic shifting makes the two lists agree.)

(b) Write \( \f = (1, \omega^{j}, \omega^{2j}) \) before normalizing. Then
\[
\C\f = \bigl(1 + \omega^{j},\ \omega^{j} + \omega^{2j},\ 1 + \omega^{2j}\bigr) .
\]
Using \( \omega^{3j} = 1 \), the second entry is \( \omega^{j}(1 + \omega^{j}) \) and the third is \( \omega^{2j}(\omega^{-2j} + 1) = \omega^{2j}(\omega^{j} + 1) \), since \( \omega^{-2j} = \omega^{j} \). So \( \C\f = (1 + \omega^{j})\f \), and the eigenvalue is \( 1 + \omega^{j} \).

(c) The three vectors \( \f_0, \f_1, \f_2 \) are orthonormal: each has norm \( \tfrac1{\sqrt3}\sqrt{3} = 1 \), and for \( j \neq l \),
\[
\inner{\f_j}{\f_l} = \tfrac13\sum_{m=0}^{2} \omega^{mj}\conj{\omega^{ml}} = \tfrac13\sum_{m=0}^{2} \bigl(\omega^{j-l}\bigr)^{m} = 0,
\]
because \( \omega^{j-l} \neq 1 \) is a cube root of unity and \( 1 + z + z^2 = 0 \) for such \( z \). Taking \( \F \) with columns \( \f_0, \f_1, \f_2 \),
\[
\begin{aligned}
\F^{*}\C\F &= \diag\bigl(2,\ 1 + \omega,\ 1 + \omega^2\bigr) \\
&= \diag\Bigl(2,\ \tfrac12 + \tfrac{\sqrt3}{2}i,\ \tfrac12 - \tfrac{\sqrt3}{2}i\Bigr),
\end{aligned}
\]
using \( \omega = -\tfrac12 + \tfrac{\sqrt3}{2}i \). Section 9 shows that this one matrix \( \F \) diagonalizes **every** \( 3 \times 3 \) circulant.
:::

::: {#exr-spectral-theorem-complex-b3}
[B3: Decide unitary diagonalizability]

Determine which of the following matrices are unitarily diagonalizable over \( \nC \), and which are merely diagonalizable. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} \).
2. \( \begin{pmatrix} 2 & 3 \\ 0 & 2 \end{pmatrix} \).
3. \( \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix} \).
4. \( \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix} \).
:::
:::

::: {.solution}
(a) Unitarily diagonalizable: the matrix is skew-symmetric, hence skew-adjoint over \( \nC \) and normal, so @cor-spectral-complex-matrix applies. (Its eigenvalues are \( \pm i \).)

(b) Neither. Comparing \( (1,1) \) entries, \( (\A^{*}\A)_{11} = 4 \) and \( (\A\A^{*})_{11} = 4 + 9 = 13 \), so \( \A \) is not normal. It is not even diagonalizable: the only eigenvalue is \( 2 \) and \( \A - 2\I = 3\J_2(0) \neq \0 \) has rank \( 1 \), so \( \dim E_2(\A) = 1 < 2 \) (@thm-diagonalization).

(c) Diagonalizable but not unitarily: the eigenvalues \( 1 \) and \( 3 \) are distinct (@cor-distinct-eigenvalues-diagonalizable), while \( (\A^{*}\A)_{11} = 1 \neq 5 = (\A\A^{*})_{11} \), so \( \A \) is not normal.

(d) Unitarily diagonalizable: the matrix is a permutation matrix, so its columns are orthonormal and it is unitary, hence normal. (Its eigenvalues are the cube roots of unity.)
:::

### C. Going deeper

::: {#exr-spectral-theorem-complex-c1}
[C1: Operators of finite order]

Let \( T \in \cL(V) \) be normal on a finite-dimensional complex inner product space, and suppose \( T^{k} = \id_V \) for some integer \( k \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that every eigenvalue of \( T \) is a \( k \)-th root of unity.
2. Deduce that \( T \) is unitary and unitarily diagonalizable.
3. Show that the hypothesis "normal" cannot be dropped from (b) by exhibiting a \( T \) with \( T^{2} = \id_V \) that is not unitary.
:::
:::

::: {.solution}
(a) If \( T\v = \lambda\v \) with \( \v \neq \0 \), then \( T^{k}\v = \lambda^{k}\v \) (@exr-eigenvalues-and-eigenvectors-b3 (a)) and \( T^{k}\v = \v \), so \( (\lambda^{k} - 1)\v = \0 \) and \( \lambda^{k} = 1 \).

(b) Every \( k \)-th root of unity has modulus \( 1 \), so \( T \) is unitary by @cor-normal-spectral-corollaries (b), and it is unitarily diagonalizable by @thm-spectral-complex because it is normal.

(c) On \( \nC^2 \) take \( \A = \begin{pmatrix} 1 & 1 \\ 0 & -1 \end{pmatrix} \). Then \( \A^2 = \I \), so \( T_{\A} \) has order \( 2 \); but its second column \( (1, -1) \) has norm \( \sqrt2 \neq 1 \), so \( \A \) is not unitary (@thm-isometry-characterizations (f)). It is still diagonalizable, with eigenvalues \( 1 \) and \( -1 \); what fails is only the orthogonality of the eigenvectors.
:::

::: {#exr-spectral-theorem-complex-c2}
[C2: Same spectrum, same multiplicities]

Let \( \A, \B \in M_n(\nC) \) be normal, and suppose they have the same eigenvalues with the same multiplicities, that is, the same characteristic polynomial.

::: {.enumerate options="label=(\alph*)"}
1. Prove that there is a unitary \( \W \) with \( \B = \W\A\W^{*} \) (one says \( \A \) and \( \B \) are **unitarily similar**).
2. Give two matrices in \( M_2(\nC) \) with the same characteristic polynomial that are not unitarily similar, and say which hypothesis of (a) they violate.
3. Deduce that two normal matrices are unitarily similar if and only if they are similar.
:::
:::

::: {.solution}
(a) By @cor-spectral-complex-matrix write \( \A = \U\D\U^{*} \) and \( \B = \V\D'\V^{*} \) with \( \U, \V \) unitary and \( \D, \D' \) diagonal. The diagonals of \( \D \) and \( \D' \) are the eigenvalue lists of \( \A \) and \( \B \) with multiplicity, which agree as multisets; and the order on the diagonal may be prescribed, so we may choose the eigenvector orderings to make \( \D' = \D \). Then
\[
\B = \V\D\V^{*} = \V\U^{*}\A\U\V^{*} = \W\A\W^{*}
\quad\text{with}\quad \W = \V\U^{*},
\]
and \( \W \) is unitary because \( \Unit(n) \) is closed under products and inverses (@prp-orthogonal-group-properties).

(b) \( \A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) and \( \B = \0 \) both have characteristic polynomial \( x^2 \); they are not even similar, since similar matrices have equal rank. A pair that is similar but not unitarily similar: \( \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix} \) and \( \diag(1, 2) \). In both cases the violated hypothesis is normality of one of the two matrices.

(c) \( (\Rightarrow) \) A unitary similarity is a similarity. \( (\Leftarrow) \) Similar matrices have the same characteristic polynomial (@thm-charpoly-similarity-invariant), so if both are normal, (a) upgrades the similarity to a unitary one.
:::

::: {#exr-spectral-theorem-complex-c3}
[C3: Normality cannot be dropped]

@cor-normal-spectral-corollaries reads the class of a **normal** operator off its spectrum. This exercise shows that each part fails without that hypothesis.

::: {.enumerate options="label=(\alph*)"}
1. Give \( \A \in M_2(\nC) \) with both eigenvalues real that is not Hermitian.
2. Give \( \A \in M_2(\nC) \) with both eigenvalues of modulus \( 1 \) that is not unitary.
3. Over \( \nR \), give \( \A \in M_2(\nR) \) with \( \inner{\A\x}{\x} \ge 0 \) for every \( \x \in \nR^2 \) whose eigenvalues are not non-negative reals. Why does no such example exist over \( \nC \)?
:::
:::

::: {.solution}
(a) \( \A = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix} \) has eigenvalues \( 1 \) and \( 2 \) and is not Hermitian, since \( \A^{*} = \begin{pmatrix} 1 & 0 \\ 1 & 2 \end{pmatrix} \neq \A \). It is not normal (@exm-diagonalizable-not-normal).

(b) \( \A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) has \( 1 \) as its only eigenvalue, of modulus \( 1 \), and is not unitary: its second column has norm \( \sqrt2 \). Again it is not normal, the \( (1,1) \) entries of \( \A^{*}\A \) and \( \A\A^{*} \) being \( 1 \) and \( 2 \).

(c) Take the quarter turn \( \A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \). For every \( \x = (x_1, x_2) \in \nR^2 \),
\[
\inner{\A\x}{\x} = -x_2x_1 + x_1x_2 = 0 \ge 0,
\]
yet \( \A \) has no real eigenvalue at all; over \( \nC \) its eigenvalues are \( \pm i \), which are not non-negative reals. Over \( \nC \) no such example exists: if \( \inner{T\v}{\v} = 0 \) for every \( \v \) then \( T = 0 \) by @thm-complex-zero-test, and more generally \( \inner{T\v}{\v} \) real for every \( \v \) forces \( T \) to be self-adjoint, hence normal, by applying @thm-complex-zero-test to \( T - T^{*} \). Real scalars are not enough to detect an operator over \( \nR \), and they are over \( \nC \).
:::
