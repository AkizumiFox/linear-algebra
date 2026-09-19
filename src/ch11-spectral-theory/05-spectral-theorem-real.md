# The Real Spectral Theorem

Over \( \nC \) the answer was clean: an orthonormal basis of eigenvectors exists exactly for the normal operators. Over \( \nR \) the same question has a different answer, and a smaller one. The class shrinks from normal to self-adjoint, and the reason is a single example that we have met since Chapter 8 and can finally name as the obstruction: a rotation of the plane is as normal as an operator can be and has no eigenvector at all. This section proves the real theorem, examines that obstruction, and then rescues what can be rescued for real normal operators. It ends with the application that made the theorem famous outside linear algebra: the axes of a conic.

Throughout, \( V \) is a finite-dimensional inner product space over \( \nR \) unless stated otherwise, and "symmetric" means \( \A\tp = \A \).

## One eigenvector, then its orthogonal complement

The proof is the signature move of the chapter, run as an induction. Section 2 did all the work: it produced an eigenvector, and it showed that the orthogonal complement of an invariant subspace is again invariant with a self-adjoint restriction. Those two facts fit together into an induction on dimension with nothing left over.

::: {#thm-spectral-real}
[Real Spectral Theorem]

Let \( V \) be a finite-dimensional inner product space over \( \nR \) and let \( T \in \cL(V) \). The following are equivalent.

::: {.enumerate options="label=(\alph*)"}
1. \( T \) is self-adjoint.
2. \( V \) has an orthonormal basis consisting of eigenvectors of \( T \).
:::
:::

::: {.idea}
\( (\Leftarrow) \) In such a basis the matrix is diagonal, and a real diagonal matrix is its own transpose. \( (\Rightarrow) \) Induct on \( \dim V \). Peel off one unit eigenvector \( \e_1 \), which exists by @thm-self-adjoint-has-eigenvalue; the line \( U = \Span(\e_1) \) is invariant, so @thm-self-adjoint-invariant-complement makes \( U^{\perp} \) invariant with a self-adjoint restriction. That restriction lives on a space of dimension \( \dim V - 1 \), so the inductive hypothesis applies to it, and the basis it returns is already orthogonal to \( \e_1 \).
:::

::: {.proof}
\( (\Leftarrow) \) Let \( \sB \) be an orthonormal basis of eigenvectors, so \( \D \coloneqq \mtx{T}{\sB}{\sB} \) is diagonal with real entries. Since \( \sB \) is orthonormal, \( \mtx{T^{*}}{\sB}{\sB} = \D^{*} = \D\tp = \D \) by @thm-matrix-of-adjoint, the last equality because a diagonal matrix equals its transpose. Two operators with the same matrix in one basis are equal (@thm-linear-maps-isomorphic-to-matrices), so \( T^{*} = T \).

\( (\Rightarrow) \) Induct on \( n = \dim V \). If \( n = 0 \) the empty list is an orthonormal basis and there is nothing to prove. Let \( n \ge 1 \) and suppose the statement holds for every real inner product space of dimension \( n - 1 \).

Since \( V \neq \{\0\} \) and \( T \) is self-adjoint, \( T \) has an eigenvalue \( \lambda \in \nR \) by @thm-self-adjoint-has-eigenvalue, say \( T\v = \lambda\v \) with \( \v \neq \0 \). Put \( \e_1 = \v/\norm{\v} \), a unit eigenvector, and \( U = \Span(\e_1) \). Then \( U \) is \( T \)-invariant, because \( T(c\e_1) = c\lambda\e_1 \in U \).

By @thm-self-adjoint-invariant-complement, \( U^{\perp} \) is \( T \)-invariant and the restriction \( T|_{U^{\perp}} \) is a self-adjoint operator on \( U^{\perp} \), which is an inner product space in its own right under the restricted inner product. Its dimension is \( n - 1 \) by @thm-orthogonal-decomposition (c). By the inductive hypothesis, \( U^{\perp} \) has an orthonormal basis \( (\e_2, \dots, \e_n) \) of eigenvectors of \( T|_{U^{\perp}} \); each \( \e_j \) satisfies \( T\e_j = \mu_j\e_j \) in \( V \) as well, since the restriction is the same map.

Finally \( (\e_1, \dots, \e_n) \) is orthonormal: the last \( n-1 \) vectors are orthonormal among themselves and each lies in \( U^{\perp} \), hence is orthogonal to \( \e_1 \), which has norm \( 1 \). An orthonormal list is linearly independent (@thm-orthogonal-independent), and it has \( n = \dim V \) members, so it is a basis (@thm-right-size-basis). Every member is an eigenvector of \( T \). This proves the theorem.
:::

::: {.remark}
No complexification appears anywhere in that induction, which is worth noticing: the argument is entirely real. The one place where complex numbers were needed is inside @thm-self-adjoint-has-eigenvalue, whose proof complexifies once to borrow an eigenvalue from the Fundamental Theorem of Algebra (@thm-fundamental-theorem-of-algebra) and then observes that the eigenvalue is real. So \( \nC \) is used exactly once, to start the machine, and never again.
:::

::: {#cor-spectral-real-matrix}
[Orthogonal Diagonalization]

Let \( \A \in M_n(\nR) \). Then \( \A \) is symmetric if and only if there are an orthogonal \( \Q \in \Orth(n) \) and a **real** diagonal \( \D \) with
\[
\A = \Q\D\Q\tp .
\]
The diagonal of \( \D \) is the eigenvalue list of \( \A \) with multiplicity, in any prescribed order, and the columns of \( \Q \) are a corresponding orthonormal basis of eigenvectors.
:::

::: {.proof}
Apply @thm-spectral-real to \( T_{\A} \) on \( \nR^n \) with the standard inner product, for which the standard basis is orthonormal, so that \( \A\tp = \A \) is exactly self-adjointness (@thm-matrix-of-adjoint).

\( (\Rightarrow) \) Let \( (\q_1, \dots, \q_n) \) be an orthonormal basis with \( \A\q_j = \lambda_j\q_j \), and let \( \Q \) have these columns; it is orthogonal by @thm-isometry-characterizations (f). Column \( j \) of \( \A\Q \) is \( \lambda_j\q_j \), which is column \( j \) of \( \Q\D \) for \( \D = \diag(\lambda_1, \dots, \lambda_n) \). So \( \A\Q = \Q\D \) and \( \A = \Q\D\Q^{-1} = \Q\D\Q\tp \). The eigenvalues are real because \( \A \) is self-adjoint (@thm-self-adjoint-real-eigenvalues), so \( \D \) is a real matrix.

\( (\Leftarrow) \) If \( \A = \Q\D\Q\tp \) with \( \D \) real diagonal, then
\[
\A\tp = (\Q\D\Q\tp)\tp = \Q\D\tp\Q\tp = \Q\D\Q\tp = \A .
\]
The claims about the order and the columns are as in @cor-spectral-complex-matrix.
:::

## The negative result: normal is not enough over the reals

Over \( \nC \) the class with an orthonormal eigenbasis was the normal operators. Over \( \nR \) @thm-spectral-real says it is the self-adjoint ones, which is a strictly smaller class: every self-adjoint operator is normal, and the converse now fails. It is worth seeing exactly how it fails, because the failure is not a technicality about multiplicities or about a badly chosen basis. It is the complete absence of an eigenvector.

::: {#exm-rotation-normal-no-real-eigenvector}
[A normal real operator with no eigenvector]

Let \( T \in \cL(\nR^2) \) be the quarter turn, with matrix
\[
\R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}
\]
in the standard basis. Show that \( T \) is normal, and that \( T \) has no eigenvalue and no eigenvector in \( \nR^2 \).
:::

::: {.solution}
Normality: \( \R\tp\R = \R\R\tp = \I \), so \( T \) is even orthogonal, hence normal. (One may also read it off the shape: \( \R = \vLambda(i) \) is the rotation-scaling block of @def-real-jordan-block.)

No eigenvalue: \( p_{\R}(x) = x^2 + 1 \), which has no root in \( \nR \). So \( \R - \lambda\I \) is invertible for every real \( \lambda \), and \( \ker(T - \lambda\,\id) = \{\0\} \) (@thm-eigenvalue-characterizations). Geometrically, \( T \) turns every non-zero vector by a right angle, so \( T\v \) is never a real multiple of \( \v \); the operator maps no line to itself.
:::

That example rules out every possible improvement of @thm-spectral-real to normal operators over \( \nR \), and not by a narrow margin. An orthonormal basis of eigenvectors needs \( n \) eigenvectors; the quarter turn supplies none. So the two spectral theorems are not two versions of one statement with a technical difference: the real one has a genuinely smaller hypothesis, and the only reason it is not smaller still is @thm-self-adjoint-has-eigenvalue, which manufactures the eigenvector that the rotation lacks.

Two further remarks keep the picture honest. First, the quarter turn is not exceptional. Over \( \nR \), *every* normal operator that is not self-adjoint fails to have an orthonormal eigenbasis, because @thm-spectral-real is an equivalence: having such a basis and being self-adjoint are the same condition. Second, nothing is wrong with the operator; what is missing is the field. Regard \( \R \) as a complex matrix and it is unitarily diagonalizable, with eigenvalues \( \pm i \) and eigenvectors \( (1, \mp i) \) in \( \nC^2 \) (the sign of the eigenvalue and of the entry being opposite). The complex spectral theorem never fails; it simply answers a question about \( \nC^n \).

::: {.check}
Is \( \R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \) orthogonally diagonalizable over \( \nR \)? Is it unitarily diagonalizable over \( \nC \)? Are the two answers consistent?
:::

::: {.solution}
Not over \( \nR \): an orthogonal diagonalization \( \R = \Q\D\Q\tp \) would make \( \R \) symmetric by @cor-spectral-real-matrix, and \( \R\tp = -\R \neq \R \). Over \( \nC \) it is unitarily diagonalizable, because it is normal (@cor-spectral-complex-matrix); explicitly \( \U^{*}\R\U = \diag(i, -i) \) for \( \U = \tfrac1{\sqrt2}\begin{pmatrix} 1 & 1 \\ -i & i \end{pmatrix} \). There is no conflict: the two statements concern different spaces, \( \nR^2 \) and \( \nC^2 \), and the diagonalizing basis of the second one is not real.
:::

## What a real normal operator does look like

The rotation is not a defect to be apologized for; it is a building block. Chapter 9 already promoted it to one when it built the real Jordan form, and the same \( 2 \times 2 \) block returns here as the only thing that can obstruct a real diagonalization of a normal operator.

::: {#thm-real-normal-form}
[Real Normal Form of a Normal Operator]

Let \( V \) be a finite-dimensional inner product space over \( \nR \) and let \( T \in \cL(V) \) be normal. Then \( V \) has an orthonormal basis in which the matrix of \( T \) is block diagonal,
\[ (c_1) \oplus \dots \oplus (c_p) \oplus \vLambda(\lambda_1) \oplus \dots \oplus \vLambda(\lambda_q),
\]
with \( c_1, \dots, c_p \in \nR \) and, for each \( j \), \( \lambda_j = a_j + b_ji \) with \( b_j > 0 \) and
\[
\vLambda(\lambda_j) = \begin{pmatrix} a_j & -b_j \\ b_j & a_j \end{pmatrix}
\]
the rotation-scaling block of @def-real-jordan-block. In matrix form: \( \A \in M_n(\nR) \) is normal if and only if \( \A = \Q\B\Q\tp \) with \( \Q \in \Orth(n) \) and \( \B \) of the displayed shape.
:::

::: {.idea}
The real Schur form of Section 1 gets us to a **block** triangular matrix with \( 1 \times 1 \) and \( 2 \times 2 \) diagonal blocks, and the corner blocks above the diagonal are the only obstruction left. The argument that killed them in the complex case, comparing a diagonal entry of \( \T\tp\T \) with the same entry of \( \T\T\tp \), works verbatim on blocks once "entry" is replaced by "trace of a block": the identity \( \tr(\X\X\tp) = \sum_{i,j} x_{ij}^2 \) turns the comparison into a sum of squares that has to vanish. What remains is to see what a \( 2 \times 2 \) real normal matrix can be, and there are exactly two answers: symmetric, which splits further, or a rotation-scaling block.
:::

::: {.proof}
Fix an orthonormal basis of \( V \) and let \( \A \in M_n(\nR) \) be the matrix of \( T \) in it; then \( \A\tp \) is the matrix of \( T^{*} \) (@thm-matrix-of-adjoint), and \( T \) normal means \( \A\tp\A = \A\A\tp \). Every orthogonal change of orthonormal basis replaces \( \A \) by \( \Q\tp\A\Q \), which is again normal:
\[
(\Q\tp\A\Q)\tp(\Q\tp\A\Q) = \Q\tp\A\tp\A\Q = \Q\tp\A\A\tp\Q,
\]
and the same computation in the other order gives \( (\Q\tp\A\Q)(\Q\tp\A\Q)\tp \). So we may replace \( \A \) by any orthogonally similar matrix at will.

**Step 1: a block triangular form.** By the real Schur form (@thm-real-schur) there is \( \Q_1 \in \Orth(n) \) with \( \T = \Q_1\tp\A\Q_1 \) block upper triangular, its diagonal blocks of size \( 1 \times 1 \) and \( 2 \times 2 \). Write the block partition as \( \T = (\T_{kl})_{1 \le k, l \le m} \) with \( \T_{kl} = \0 \) for \( k > l \). By the previous paragraph \( \T \) is normal.

**Step 2: the corners vanish.**

::: {.claim}
A normal, block upper triangular real matrix is block diagonal.
:::

::: {.proof}
Induct on the number \( m \) of diagonal blocks; \( m = 1 \) is trivial. Comparing the \( (1,1) \) blocks of the two products (@thm-block-multiplication) and using \( \T_{k1} = \0 \) for \( k > 1 \),
\[
\begin{aligned}
(\T\tp\T)_{11} &= \T_{11}\tp\T_{11}, \\
(\T\T\tp)_{11} &= \T_{11}\T_{11}\tp + \sum_{l > 1} \T_{1l}\T_{1l}\tp .
\end{aligned}
\]
Take traces. Since \( \tr(\X\Y) = \tr(\Y\X) \) (@thm-trace-properties), the two terms \( \tr(\T_{11}\tp\T_{11}) \) and \( \tr(\T_{11}\T_{11}\tp) \) are equal and cancel, leaving
\[
\sum_{l > 1} \tr\bigl(\T_{1l}\T_{1l}\tp\bigr) = 0 .
\]
For a real matrix \( \X \), \( \tr(\X\X\tp) = \sum_{i,j} x_{ij}^2 \ge 0 \), with equality only for \( \X = \0 \). So \( \T_{1l} = \0 \) for every \( l > 1 \): the first block row is clear, and \( \T = \T_{11} \oplus \T' \) where \( \T' \) is the trailing block upper triangular matrix with \( m - 1 \) diagonal blocks. Then
\[
\T\tp\T = \T_{11}\tp\T_{11} \oplus {\T'}\tp\T',
\qquad
\T\T\tp = \T_{11}\T_{11}\tp \oplus \T'{\T'}\tp,
\]
so normality of \( \T \) gives normality of \( \T' \), and the inductive hypothesis applies.
:::

So after Step 2 the matrix is \( \D_1 \oplus \dots \oplus \D_m \) with each \( \D_k \) of size \( 1 \) or \( 2 \). Both products are now computed blockwise, so normality of the whole reads \( \D_k\tp\D_k = \D_k\D_k\tp \) for each \( k \): every diagonal block is normal.

**Step 3: the shape of a \( 2 \times 2 \) real normal block.** Let \( \D = \begin{pmatrix} p & q \\ r & s \end{pmatrix} \) be real and normal. Expanding both products,
\[
\D\D\tp - \D\tp\D
= \begin{pmatrix} q^2 - r^2 & (r - q)(p - s) \\ (r - q)(p - s) & r^2 - q^2 \end{pmatrix},
\]
so normality says \( q^2 = r^2 \) and \( (r - q)(p - s) = 0 \). The first equation gives \( q = r \) or \( q = -r \), and when \( q = -r = 0 \) both hold, so the following two cases are exhaustive.

*Case 1: \( q = r \).* Then \( \D \) is symmetric, and @cor-spectral-real-matrix supplies an orthogonal \( 2 \times 2 \) matrix turning it into a real diagonal matrix, which is two \( 1 \times 1 \) blocks.

*Case 2: \( q = -r \) and \( q \neq 0 \).* Then \( r - q = -2q \neq 0 \), so \( p = s \) and
\[
\D = \begin{pmatrix} p & q \\ -q & p \end{pmatrix} .
\]
If \( q < 0 \), this is \( \vLambda(p - qi) \) with \( -q > 0 \), as required. If \( q > 0 \), conjugate by the orthogonal matrix \( \diag(1, -1) \):
\[
\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
\begin{pmatrix} p & q \\ -q & p \end{pmatrix}
\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
= \begin{pmatrix} p & -q \\ q & p \end{pmatrix},
\]
which is \( \vLambda(p + qi) \) with \( q > 0 \).

**Step 4: assembling.** Apply Step 3 inside each diagonal block, using the direct sum \( \Q_2 \) of the resulting \( 1 \times 1 \) and \( 2 \times 2 \) orthogonal matrices, which is orthogonal because its columns are orthonormal. Then \( \Q = \Q_1\Q_2 \) is orthogonal and \( \Q\tp\A\Q \) has the stated shape; reordering the blocks by a permutation matrix, itself orthogonal, puts the \( 1 \times 1 \) blocks first. The columns of \( \Q \) are the required orthonormal basis.

For the converse, a block diagonal matrix \( \B \) of the displayed shape is normal, since \( \B\tp\B \) and \( \B\B\tp \) are computed blockwise and every block is normal: \( (c)\tp(c) = (c^2) = (c)(c)\tp \), and \( \vLambda(\lambda)\tp\vLambda(\lambda) = \lvert\lambda\rvert^2\I_2 = \vLambda(\lambda)\vLambda(\lambda)\tp \). Then \( \A = \Q\B\Q\tp \) is normal by the first paragraph. This proves the theorem.
:::

The two theorems now fit together. A real normal operator is self-adjoint exactly when no \( \vLambda \) block occurs, and then @thm-real-normal-form is @thm-spectral-real. The eigenvalues of \( \A \) are the numbers \( c_i \) together with the conjugate pairs \( \lambda_j, \conj{\lambda_j} \), so the \( \vLambda \) blocks are precisely the non-real part of the spectrum, packaged two real dimensions at a time. Section 6 specializes this to orthogonal operators, where \( \lvert\lambda\rvert = 1 \) forces every \( 2 \times 2 \) block to be a plane rotation.

## A symmetric matrix as a sum of projections

Writing \( \A = \Q\D\Q\tp \) and expanding the product column by column turns the diagonalization into a sum of very simple matrices.

::: {#cor-symmetric-rank-one-sum}
[Spectral Decomposition of a Symmetric Matrix]

Let \( \A \in M_n(\nR) \) be symmetric, and let \( (\q_1, \dots, \q_n) \) be an orthonormal basis of \( \nR^n \) with \( \A\q_i = \lambda_i\q_i \). Then
\[
\A = \sum_{i=1}^{n} \lambda_i\,\q_i\q_i\tp ,
\]
and each \( \q_i\q_i\tp \) is the matrix of the orthogonal projection of \( \nR^n \) onto the line \( \Span(\q_i) \).
:::

::: {.proof}
Let \( \Q \) have columns \( \q_1, \dots, \q_n \) and \( \D = \diag(\lambda_1, \dots, \lambda_n) \), so \( \A = \Q\D\Q\tp \) by @cor-spectral-real-matrix. The columns of \( \Q\D \) are \( \lambda_i\q_i \), and the rows of \( \Q\tp \) are \( \q_i\tp \), so the column-times-row expansion of the product (@cor-outer-product-expansion) gives \( \A = \sum_i (\lambda_i\q_i)\q_i\tp \), which is the stated sum.

For the second claim, \( \q_i \) is a unit vector, so the orthogonal projection onto \( \Span(\q_i) \) is \( \x \mapsto \inner{\x}{\q_i}\q_i \) by @thm-projection-formula. Since \( \inner{\x}{\q_i} = \q_i\tp\x \) is a scalar, \( \inner{\x}{\q_i}\q_i = \q_i(\q_i\tp\x) = (\q_i\q_i\tp)\x \).
:::

::: {#exm-symmetric-3x3-spectral}
[Orthogonally diagonalizing a 3 by 3 matrix]

Orthogonally diagonalize
\[
\A = \begin{pmatrix} 3 & 1 & 1 \\ 1 & 3 & 1 \\ 1 & 1 & 3 \end{pmatrix},
\]
and write it as a sum of rank-one orthogonal projections.
:::

::: {.solution}
The rows all sum to \( 5 \), so \( \A(1,1,1) = 5(1,1,1) \) and \( 5 \) is an eigenvalue. Also \( \A = 2\I + \J \) where \( \J \) is the all-ones matrix, and \( \J\x = \0 \) exactly when \( x_1 + x_2 + x_3 = 0 \); on that plane \( \A\x = 2\x \). So
\[
E_5(\A) = \Span\bigl((1,1,1)\bigr),
\qquad
E_2(\A) = \{\x : x_1 + x_2 + x_3 = 0\},
\]
of dimensions \( 1 \) and \( 2 \), which already account for all of \( \nR^3 \). The two eigenspaces are orthogonal, as @thm-self-adjoint-orthogonal-eigenspaces requires.

Inside \( E_2(\A) \) any orthonormal basis will do. Start from the independent pair \( (1,-1,0) \) and \( (1,0,-1) \), both in the plane, and run one step of Gram–Schmidt (@thm-gram-schmidt): the second vector minus its component along the first is \( (1,0,-1) - \tfrac12(1,-1,0) = \tfrac12(1,1,-2) \), a multiple of \( (1,1,-2) \). Normalizing all three,
\[
\q_1 = \tfrac{1}{\sqrt3}(1,1,1),
\quad
\q_2 = \tfrac{1}{\sqrt2}(1,-1,0),
\quad
\q_3 = \tfrac{1}{\sqrt6}(1,1,-2).
\]
With \( \Q = (\q_1 \mid \q_2 \mid \q_3) \) we get \( \Q\tp\Q = \I \) and \( \Q\tp\A\Q = \diag(5, 2, 2) \). By @cor-symmetric-rank-one-sum,
\[
\A = 5\,\q_1\q_1\tp + 2\,\q_2\q_2\tp + 2\,\q_3\q_3\tp .
\]
As a check, \( \q_2\q_2\tp + \q_3\q_3\tp = \I - \q_1\q_1\tp \) because the three projections sum to the identity, so the right-hand side is \( 2\I + 3\,\q_1\q_1\tp = 2\I + \J \), which is \( \A \). Notice that \( \q_2 \) and \( \q_3 \) were not forced on us, while the two projections \( \q_1\q_1\tp \) and \( \q_2\q_2\tp + \q_3\q_3\tp \) were: they are the projections onto the two eigenspaces. Section 8 makes that observation into a theorem.
:::

## The principal axis theorem

Here is the application. A **quadratic form** on \( \nR^n \) is a function
\[
q(\x) = \x\tp\A\x = \sum_{i,j} a_{ij}x_ix_j
\]
for some \( \A \in M_n(\nR) \). Only the symmetric part of \( \A \) matters, since \( \x\tp\A\x = \x\tp\A\tp\x \) for a \( 1 \times 1 \) matrix, so we always take \( \A \) symmetric; then \( \A \) is determined by \( q \), with \( a_{ii} \) the coefficient of \( x_i^2 \) and \( a_{ij} \) **half** the coefficient of \( x_ix_j \) for \( i \neq j \). Chapter 13 studies such forms in their own right.

::: {#thm-principal-axes}
[Principal Axis Theorem]

Let \( \A \in M_n(\nR) \) be symmetric, let \( q(\x) = \x\tp\A\x \), and let \( \Q \in \Orth(n) \) with \( \Q\tp\A\Q = \D = \diag(\lambda_1, \dots, \lambda_n) \), the columns \( \q_1, \dots, \q_n \) of \( \Q \) being an orthonormal basis of eigenvectors. Substituting \( \x = \Q\y \), that is, taking \( y_i = \inner{\x}{\q_i} \) to be the coordinates of \( \x \) in that basis,
\[
q(\x) = \sum_{i=1}^{n} \lambda_i y_i^2 .
\]
In particular, for \( n = 2 \) with \( \lambda_1, \lambda_2 > 0 \), the level set \( \{q = 1\} \) is an ellipse whose axes lie along \( \q_1 \) and \( \q_2 \), with half-lengths \( 1/\sqrt{\lambda_1} \) and \( 1/\sqrt{\lambda_2} \).
:::

::: {.proof}
Since \( \Q \) is invertible, \( \x = \Q\y \) sets up a bijection between \( \x \) and \( \y = \Q^{-1}\x = \Q\tp\x \), whose \( i \)-th entry is \( \q_i\tp\x = \inner{\x}{\q_i} \). Substituting,
\[
q(\Q\y) = (\Q\y)\tp\A(\Q\y) = \y\tp(\Q\tp\A\Q)\y = \y\tp\D\y = \sum_i \lambda_iy_i^2 ,
\]
using \( (\Q\y)\tp = \y\tp\Q\tp \) (@thm-transpose-properties).

For \( n = 2 \) with both \( \lambda_i > 0 \), the condition \( q(\x) = 1 \) becomes \( \lambda_1y_1^2 + \lambda_2y_2^2 = 1 \), the standard equation of an ellipse in the \( \y \) coordinates, meeting the \( y_1 \)-axis where \( y_1 = \pm 1/\sqrt{\lambda_1} \) and the \( y_2 \)-axis where \( y_2 = \pm 1/\sqrt{\lambda_2} \). Those axes are the lines \( \Span(\q_1) \) and \( \Span(\q_2) \) of the original picture, because \( \y = \e_1 \) corresponds to \( \x = \Q\e_1 = \q_1 \). Since \( \Q \) is orthogonal, it preserves lengths (@thm-isometry-characterizations), so the half-lengths are unchanged by the substitution.
:::

::: {#exm-principal-axes-ellipse}
[Finding the axes of a conic]

Identify the curve \( 3x^2 - 2xy + 3y^2 = 1 \) in \( \nR^2 \), and find its axes and their half-lengths.
:::

::: {.solution}
The symmetric matrix of the form is
\[
\A = \begin{pmatrix} 3 & -1 \\ -1 & 3 \end{pmatrix},
\]
the off-diagonal entries being half of \( -2 \). Its characteristic polynomial is \( x^2 - 6x + 8 \), so the eigenvalues are \( 2 \) and \( 4 \). For \( \lambda = 2 \), \( \A - 2\I = \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix} \) gives \( x = y \) and the unit eigenvector \( \q_1 = \tfrac1{\sqrt2}(1,1) \). For \( \lambda = 4 \), \( \A - 4\I = \begin{pmatrix} -1 & -1 \\ -1 & -1 \end{pmatrix} \) gives \( x = -y \) and \( \q_2 = \tfrac1{\sqrt2}(1,-1) \).

In the coordinates \( y_1 = \inner{\x}{\q_1} \), \( y_2 = \inner{\x}{\q_2} \), the equation is \( 2y_1^2 + 4y_2^2 = 1 \). Both eigenvalues are positive, so the curve is an **ellipse**. Its major axis lies along \( \q_1 \), the line \( y = x \), with half-length \( 1/\sqrt2 \); its minor axis lies along \( \q_2 \), the line \( y = -x \), with half-length \( 1/2 \). The check is that \( \tfrac1{\sqrt2}(1,1) \) scaled to length \( 1/\sqrt2 \) is the point \( (\tfrac12, \tfrac12) \), and \( 3\cdot\tfrac14 - 2\cdot\tfrac14 + 3\cdot\tfrac14 = 1 \).
:::

\begin{center}
\begin{tikzpicture}[scale=3, lab/.style={font=\small}]
    \draw[->, gray] (-1.0,0) -- (1.05,0) node[below, black, lab] {$x$};
    \draw[->, gray] (0,-1.0) -- (0,1.05) node[left, black, lab] {$y$};
    \draw[dashed, black!45] (-0.72,-0.72) -- (0.72,0.72);
    \draw[dashed, black!45] (0.62,-0.62) -- (-0.62,0.62);
    \draw[very thick, rotate=45] (0,0) ellipse (0.7071 and 0.5);
    \draw[->, very thick] (0,0) -- (0.5,0.5);
    \draw[->, very thick] (0,0) -- (0.3536,-0.3536);
    \node[lab, right] at (0.50,0.42) {$\tfrac{1}{\sqrt2}\q_1$};
    \node[lab, right] at (0.36,-0.40) {$\tfrac12\q_2$};
    \node[lab] at (0.86,0.74) {$\lambda_1 = 2$};
    \node[lab] at (-0.80,0.72) {$\lambda_2 = 4$};
    \node[lab, align=center] at (0,-1.22)
      {$3x^2-2xy+3y^2=1$: the axes lie along the\\ eigenvectors, with half-lengths $1/\sqrt{\lambda_i}$};
\end{tikzpicture}
\end{center}

Two features of the picture are worth naming. The axes are **orthogonal** because the eigenvectors are, and that is the whole content of the theorem; a non-symmetric matrix in the same role would produce a pair of distinguished directions that need not be perpendicular. And the bigger eigenvalue gives the **shorter** axis, since the half-length is \( 1/\sqrt{\lambda} \): a large \( \lambda \) makes \( q \) reach the value \( 1 \) sooner.

::: {.remark}
Chapter 13 will diagonalize quadratic forms again, but by **congruence**: replacing \( \A \) by \( \P\tp\A\P \) for an arbitrary invertible \( \P \), not necessarily orthogonal. That is a weaker relation, and it destroys the eigenvalues while preserving only their signs, which is Sylvester's law of inertia. What makes the present theorem special is that \( \Q\tp = \Q^{-1} \), so \( \Q\tp\A\Q = \Q^{-1}\A\Q \) and the two relations coincide: an orthogonal change of variables is a similarity *and* a congruence, so it keeps the eigenvalues and the geometry at once.
:::

::: {.warning}
**The theorem needs \( \nR \), and symmetry is not the same as having real eigenvalues.** The matrix \( \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} \) is symmetric with rational entries, but its eigenvalues are \( (1 \pm \sqrt5)/2 \), which are irrational; over \( \nQ \) there is no eigenvector at all, and no version of @thm-spectral-real survives. Conversely \( \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix} \) has the real eigenvalues \( 1 \) and \( 2 \) and is not symmetric; real eigenvalues alone buy nothing, since they do not make the eigenvectors orthogonal.
:::

## Exercises

### A. Check your understanding

::: {#exr-spectral-theorem-real-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the real spectral theorem and its matrix form, with every hypothesis.
2. Which two results from Section 2 does the induction use, and what does each one supply?
3. True or false: a normal operator on a real inner product space has an orthonormal basis of eigenvectors. Justify your answer.
4. What are the possible diagonal blocks in the real normal form of a normal operator, and what does the condition \( b > 0 \) rule out?
5. Given a symmetric \( \A \) with orthonormal eigenvectors \( \q_1, \q_2 \) and eigenvalues \( 9 \) and \( 1 \), describe the curve \( \x\tp\A\x = 1 \).
6. True or false: a real matrix with real eigenvalues is symmetric. Justify your answer.
:::
:::

::: {.solution}
(a) For a finite-dimensional real inner product space \( V \) and \( T \in \cL(V) \): \( T \) is self-adjoint if and only if \( V \) has an orthonormal basis of eigenvectors (@thm-spectral-real). Matrix form: \( \A \in M_n(\nR) \) is symmetric if and only if \( \A = \Q\D\Q\tp \) with \( \Q \) orthogonal and \( \D \) real diagonal (@cor-spectral-real-matrix).

(b) @thm-self-adjoint-has-eigenvalue supplies one eigenvector to peel off, and @thm-self-adjoint-invariant-complement supplies the smaller object to induct on, namely the self-adjoint restriction to the orthogonal complement.

(c) False. The quarter turn of \( \nR^2 \) is normal and has no eigenvector at all (@exm-rotation-normal-no-real-eigenvector).

(d) Blocks \( (c) \) with \( c \in \nR \), and \( 2 \times 2 \) blocks \( \vLambda(\lambda) = \begin{pmatrix} a & -b \\ b & a \end{pmatrix} \) with \( b > 0 \) (@thm-real-normal-form). The condition \( b > 0 \) rules out the transposed block \( \vLambda(\conj\lambda) \), which is orthogonally similar to it via \( \diag(1, -1) \); fixing the sign is what makes the list of blocks well defined.

(e) An ellipse with axes along \( \q_1 \) and \( \q_2 \), of half-lengths \( 1/3 \) and \( 1 \) (@thm-principal-axes). The longer axis is along \( \q_2 \), the eigenvector for the **smaller** eigenvalue.

(f) False. \( \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix} \) has eigenvalues \( 1, 2 \) and is not symmetric. The correct statement is the converse: a symmetric real matrix has real eigenvalues.
:::

### B. Practice

::: {#exr-spectral-theorem-real-b1}
[B1: Orthogonally diagonalize]

For each symmetric matrix, find an orthogonal \( \Q \) and a diagonal \( \D \) with \( \Q\tp\A\Q = \D \).

::: {.enumerate options="label=(\alph*)"}
1. \( \A = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix} \).
2. \( \A = \begin{pmatrix} 4 & 0 & 1 \\ 0 & 2 & 0 \\ 1 & 0 & 4 \end{pmatrix} \).
:::
:::

::: {.solution}
(a) \( p_{\A}(x) = x^2 - 2x - 3 = (x-3)(x+1) \), so the eigenvalues are \( 3 \) and \( -1 \). For \( \lambda = 3 \), \( \A - 3\I = \begin{pmatrix} -2 & 2 \\ 2 & -2 \end{pmatrix} \) gives \( x_1 = x_2 \) and \( \q_1 = \tfrac1{\sqrt2}(1,1) \); for \( \lambda = -1 \), \( \q_2 = \tfrac1{\sqrt2}(1,-1) \). Hence
\[
\Q = \tfrac1{\sqrt2}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix},
\qquad
\D = \begin{pmatrix} 3 & 0 \\ 0 & -1 \end{pmatrix} .
\]

(b) The second coordinate is untouched: \( \A\e_2 = 2\e_2 \). On \( \Span(\e_1, \e_3) \) the matrix acts as \( \begin{pmatrix} 4 & 1 \\ 1 & 4 \end{pmatrix} \), with eigenvalues \( 5 \) and \( 3 \) and eigenvectors \( (1,1) \) and \( (1,-1) \) there. Lifting back,
\[
\q_1 = \tfrac1{\sqrt2}(1,0,1),
\quad
\q_2 = \tfrac1{\sqrt2}(-1,0,1),
\quad
\q_3 = (0,1,0),
\]
with eigenvalues \( 5, 3, 2 \). These are orthonormal, so \( \Q = (\q_1 \mid \q_2 \mid \q_3) \) is orthogonal and \( \Q\tp\A\Q = \diag(5, 3, 2) \). As a check, \( 5 + 3 + 2 = 10 = \tr \A \).
:::

::: {#exr-spectral-theorem-real-b2}
[B2: Identify the conic]

Identify the curve \( 5x^2 + 4xy + 5y^2 = 1 \): say what kind of conic it is, find its axes, and find their half-lengths.
:::

::: {.solution}
The symmetric matrix of the form is \( \A = \begin{pmatrix} 5 & 2 \\ 2 & 5 \end{pmatrix} \), the off-diagonal entries being half of \( 4 \). Its characteristic polynomial is \( x^2 - 10x + 21 = (x-7)(x-3) \), so the eigenvalues are \( 7 \) and \( 3 \). For \( \lambda = 7 \), \( \A - 7\I = \begin{pmatrix} -2 & 2 \\ 2 & -2 \end{pmatrix} \) gives \( \q_1 = \tfrac1{\sqrt2}(1,1) \); for \( \lambda = 3 \), \( \q_2 = \tfrac1{\sqrt2}(1,-1) \).

By @thm-principal-axes the equation becomes \( 7y_1^2 + 3y_2^2 = 1 \). Both eigenvalues are positive, so the curve is an ellipse. Its axes are the lines \( y = x \) and \( y = -x \), with half-lengths \( 1/\sqrt7 \) along \( \q_1 \) and \( 1/\sqrt3 \) along \( \q_2 \); the major axis is the second one. Check: the point \( \tfrac1{\sqrt3}\q_2 = \tfrac1{\sqrt6}(1,-1) \) gives \( \tfrac56 - \tfrac46 + \tfrac56 = 1 \).
:::

::: {#exr-spectral-theorem-real-b3}
[B3: A sum of rank-one projections]

Using your answer to @exr-spectral-theorem-real-b1 (b), write
\[
\A = \begin{pmatrix} 4 & 0 & 1 \\ 0 & 2 & 0 \\ 1 & 0 & 4 \end{pmatrix}
\]
as \( \sum_i \lambda_i\q_i\q_i\tp \), with the three matrices \( \q_i\q_i\tp \) written out, and verify the identity by adding them.
:::

::: {.solution}
With \( \q_1 = \tfrac1{\sqrt2}(1,0,1) \), \( \q_2 = \tfrac1{\sqrt2}(-1,0,1) \), \( \q_3 = (0,1,0) \) and \( \lambda = 5, 3, 2 \),
\[
\q_1\q_1\tp = \tfrac12\begin{pmatrix} 1 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 1 \end{pmatrix},
\qquad
\q_2\q_2\tp = \tfrac12\begin{pmatrix} 1 & 0 & -1 \\ 0 & 0 & 0 \\ -1 & 0 & 1 \end{pmatrix},
\]
and \( \q_3\q_3\tp \) is the matrix with a single \( 1 \) in position \( (2,2) \). Then
\[
5\,\q_1\q_1\tp + 3\,\q_2\q_2\tp
= \begin{pmatrix} 4 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 4 \end{pmatrix},
\]
since \( \tfrac12(5+3) = 4 \) on the diagonal and \( \tfrac12(5-3) = 1 \) off it. Adding \( 2\,\q_3\q_3\tp \) inserts the \( 2 \) in position \( (2,2) \) and gives \( \A \), as @cor-symmetric-rank-one-sum requires.
:::

### C. Going deeper

::: {#exr-spectral-theorem-real-c1}
[C1: One eigenvalue only]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \A \in M_n(\nR) \) be symmetric with every eigenvalue equal to \( \lambda \). Prove that \( \A = \lambda\I \).
2. Show that (a) fails without symmetry, by exhibiting a matrix in \( M_2(\nR) \) whose only eigenvalue is \( 0 \) and which is not \( \0 \).
3. Deduce that a symmetric \( \A \) with \( \A^2 = \A \) is the matrix of an orthogonal projection.
:::
:::

::: {.solution}
(a) By @cor-spectral-real-matrix, \( \A = \Q\D\Q\tp \) with \( \D \) diagonal carrying the eigenvalues, so \( \D = \lambda\I \). Hence \( \A = \Q(\lambda\I)\Q\tp = \lambda\Q\Q\tp = \lambda\I \).

(b) \( \J_2(0) = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) has characteristic polynomial \( x^2 \), so \( 0 \) is its only eigenvalue, and it is not the zero matrix. It is of course not symmetric.

(c) If \( \A^2 = \A \) and \( \A\x = \lambda\x \) with \( \x \neq \0 \), then \( \lambda^2\x = \A^2\x = \A\x = \lambda\x \), so \( \lambda^2 = \lambda \) and \( \lambda \in \{0, 1\} \). By @cor-spectral-real-matrix, \( \A = \Q\D\Q\tp \) with \( \D \) diagonal of zeros and ones, so \( \A = \sum_{i \in S}\q_i\q_i\tp \) where \( S \) indexes the eigenvalue \( 1 \) (@cor-symmetric-rank-one-sum). That is the sum of the projections onto an orthonormal basis of \( U = E_1(\A) \), which is the orthogonal projection \( P_U \) by @thm-projection-formula.
:::

::: {#exr-spectral-theorem-real-c2}
[C2: Diagonalizing two matrices at once]

Let \( \A, \B \in M_n(\nR) \) be symmetric with \( \A\B = \B\A \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that each eigenspace \( E_{\lambda}(\A) \) is \( \B \)-invariant, and that the restriction of \( T_{\B} \) to it is self-adjoint.
2. Prove that there is a single \( \Q \in \Orth(n) \) with \( \Q\tp\A\Q \) and \( \Q\tp\B\Q \) both diagonal.
3. Show that the conclusion fails without commutativity, using \( \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \) and \( \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \).
:::

*Hint for (b): apply @thm-spectral-real inside each eigenspace of \( \A \).*
:::

::: {.solution}
(a) Invariance is @thm-commuting-preserves-eigenspaces: if \( \A\x = \lambda\x \) then \( \A(\B\x) = \B(\A\x) = \lambda\B\x \). For self-adjointness of the restriction, take \( \u, \v \in E_{\lambda}(\A) \); then \( \inner{\B\u}{\v} = \inner{\u}{\B\v} \) because \( \B \) is symmetric on all of \( \nR^n \), and both \( \B\u \) and \( \B\v \) lie in \( E_{\lambda}(\A) \) by the first part, so the identity holds inside the subspace with its restricted inner product.

(b) Let \( \lambda_1, \dots, \lambda_k \) be the distinct eigenvalues of \( \A \). By @thm-spectral-real, \( \nR^n \) is the direct sum of the eigenspaces \( E_{\lambda_i}(\A) \), and these are mutually orthogonal (@thm-self-adjoint-orthogonal-eigenspaces). By (a) and @thm-spectral-real applied to the self-adjoint operator \( T_{\B}|_{E_{\lambda_i}(\A)} \), each \( E_{\lambda_i}(\A) \) has an orthonormal basis of eigenvectors of \( \B \). Every vector of \( E_{\lambda_i}(\A) \) is an eigenvector of \( \A \), so these basis vectors are common eigenvectors. Stringing the \( k \) bases together gives an orthonormal basis of \( \nR^n \), orthonormal across the blocks because distinct eigenspaces of \( \A \) are orthogonal. Let \( \Q \) have those vectors as columns; then \( \Q \in \Orth(n) \) and both \( \Q\tp\A\Q \) and \( \Q\tp\B\Q \) are diagonal.

(c) These two do not commute: \( \A\B = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) while \( \B\A = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \). And no common eigenbasis exists: the eigenvectors of \( \A \) are the multiples of \( \e_1 \) and of \( \e_2 \), while \( \B\e_1 = \e_2 \) is not a multiple of \( \e_1 \). Commutativity is necessary as well as sufficient, since two simultaneously diagonalized matrices commute.
:::

::: {#exr-spectral-theorem-real-c3}
[C3: A rotation-scaling in normal form]

Let \( \A = \begin{pmatrix} 3 & 4 \\ -4 & 3 \end{pmatrix} \in M_2(\nR) \).

::: {.enumerate options="label=(\alph*)"}
1. Verify that \( \A \) is normal and not symmetric, and find its complex eigenvalues.
2. Find an orthogonal \( \Q \) with \( \Q\tp\A\Q = \vLambda(\lambda) \) for the eigenvalue \( \lambda \) with positive imaginary part.
3. Explain why no orthogonal \( \Q \) makes \( \Q\tp\A\Q \) diagonal, and why this does not contradict @thm-spectral-complex.
:::
:::

::: {.solution}
(a) \( \A\tp\A = \A\A\tp = 25\I \), so \( \A \) is normal; \( \A\tp \neq \A \) since \( 4 \neq -4 \). Its characteristic polynomial is \( x^2 - 6x + 25 = (x-3)^2 + 16 \), with roots \( 3 \pm 4i \).

(b) The eigenvalue with positive imaginary part is \( \lambda = 3 + 4i \), so \( \vLambda(\lambda) = \begin{pmatrix} 3 & -4 \\ 4 & 3 \end{pmatrix} \). Take \( \Q = \diag(1, -1) \), which is orthogonal. Then
\[
\Q\tp\A\Q = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
\begin{pmatrix} 3 & 4 \\ -4 & 3 \end{pmatrix}
\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
= \begin{pmatrix} 3 & -4 \\ 4 & 3 \end{pmatrix},
\]
which is \( \vLambda(3 + 4i) \). This is Case 2 of the proof of @thm-real-normal-form with \( p = 3 \) and \( q = 4 \).

(c) If \( \Q\tp\A\Q \) were diagonal for some \( \Q \in \Orth(2) \), then \( \A = \Q\D\Q\tp \) would be symmetric by @cor-spectral-real-matrix, and it is not. There is no contradiction with @thm-spectral-complex, which concerns a **complex** inner product space: over \( \nC^2 \) the matrix \( \A \) is indeed unitarily diagonalizable, to \( \diag(3+4i, 3-4i) \), but the diagonalizing basis \( \tfrac1{\sqrt2}(1, \pm i) \) is not real, so it is unavailable inside \( \nR^2 \).
:::
