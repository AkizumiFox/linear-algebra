# Commuting Operators

So far we have diagonalized or triangularized one operator at a time. Many problems hand us several at once: two matrices that describe the same system, or a matrix together with all its powers. Can a single basis make **all** of them diagonal, or all of them triangular? A necessary condition is easy to spot, because diagonal matrices commute. This section shows that commuting is also enough, as long as each operator can be handled on its own. The whole argument rests on one observation: an operator that commutes with \( T \) maps each eigenspace of \( T \) into itself, so we can search for common eigenvectors inside an eigenspace.

## When can two operators share a basis?

Let \( V \) be finite-dimensional and \( S, T \in \cL(V) \). Suppose one basis \( \sB \) makes both \( \mtx{S}{\sB}{\sB} \) and \( \mtx{T}{\sB}{\sB} \) diagonal. Diagonal matrices multiply entry by entry on the diagonal, so \( \mtx{S}{\sB}{\sB}\mtx{T}{\sB}{\sB} = \mtx{T}{\sB}{\sB}\mtx{S}{\sB}{\sB} \). By @cor-matrix-of-polynomial-of-operator this says \( \mtx{ST}{\sB}{\sB} = \mtx{TS}{\sB}{\sB} \), and since \( T \mapsto \mtx{T}{\sB}{\sB} \) is injective (@thm-linear-maps-isomorphic-to-matrices), \( ST = TS \). So **sharing a diagonalizing basis forces commuting**. The same is not true for triangular matrices: \( \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix} \) and \( \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix} \) are both upper triangular, and their products in the two orders are \( \begin{pmatrix} 1 & 2 \\ 0 & 4 \end{pmatrix} \) and \( \begin{pmatrix} 1 & 1 \\ 0 & 4 \end{pmatrix} \). We will see, though, that commuting is a convenient sufficient condition in the triangular case as well.

The question for this section is the converse: if \( ST = TS \), can we find a common basis? Here are the commuting pairs to keep in mind.

- **Polynomials in one operator.** For every \( p, q \in F[x] \), \( p(T)q(T) = q(T)p(T) \) (@thm-evaluation-homomorphism (c)). In particular \( T \) commutes with \( T^2 \), with \( T^{-1} \) when it exists (both products are \( \id_V \)), and with every scalar operator \( c\,\id_V \).
- **Diagonal matrices** commute with each other, and so do block diagonal matrices whose corresponding blocks commute (@thm-block-diagonal-arithmetic).
- **A non-commuting pair.** \( \E_{12} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) and \( \E_{21} = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \) give \( \E_{12}\E_{21} = \E_{11} \ne \E_{22} = \E_{21}\E_{12} \).

The last pair already shows that something must be assumed. Over any field, the eigenvectors of \( \E_{12} \) are the non-zero multiples of \( \e_1 \), and those of \( \E_{21} \) are the non-zero multiples of \( \e_2 \). They share no eigenvector at all, let alone a basis of them.

## Commuting operators preserve eigenspaces

How does the hypothesis \( ST = TS \) interact with eigenvectors? Take \( T\v = \lambda\v \) and ask what \( T \) does to \( S\v \). There is no \( S \) in the eigenvector equation yet, so we apply \( S \) to both sides.

::: {#thm-commuting-preserves-eigenspaces}
[Commuting Operators Preserve Eigenspaces]

Let \( V \) be a vector space over \( F \), and let \( S, T \in \cL(V) \) with \( ST = TS \). Then for every \( \lambda \in F \), the eigenspace \( E_\lambda(T) \) is \( S \)-invariant.
:::

::: {.proof}
Let \( \v \in E_\lambda(T) \), so \( T\v = \lambda\v \). Since \( ST = TS \) and \( S \) is linear,
\[
T(S\v) = (TS)\v = (ST)\v = S(\lambda\v) = \lambda\,S\v .
\]
Hence \( S\v \in E_\lambda(T) \) by @def-eigenspace. This shows that \( S \) maps \( E_\lambda(T) \) into itself.
:::

No finite dimension is needed, and \( \lambda \) need not be an eigenvalue (then \( E_\lambda(T) = \{\0\} \) and there is nothing to prove). By symmetry, every eigenspace of \( S \) is \( T \)-invariant too.

In matrix language the theorem is a statement about block shapes. Take \( T = \diag(1, 1, 2) \) on \( F^3 \), with \( E_1(T) = \Span(\e_1, \e_2) \) and \( E_2(T) = \Span(\e_3) \), and let \( S \) be any matrix with \( ST = TS \). Both eigenspaces are \( S \)-invariant, and \( F^3 = E_1(T) \oplus E_2(T) \), so by @thm-direct-sum-invariant-block-diagonal the matrix \( S \) is block diagonal:
\[
S = \begin{pmatrix} s_{11} & s_{12} & 0 \\ s_{21} & s_{22} & 0 \\ 0 & 0 & s_{33} \end{pmatrix}.
\]
Conversely, every matrix of this shape commutes with \( T \), since \( T = \I_2 \oplus (2) \) and \( \I_2 \) commutes with every \( 2 \times 2 \) block (@thm-block-diagonal-arithmetic). Inside the repeated eigenspace \( S \) can be anything; this freedom is what the rest of the section has to deal with.

**Non-example.** Take \( T = \diag(1, 2) \) and the swap \( S = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \). Then \( S\e_1 = \e_2 \notin E_1(T) = \Span(\e_1) \), so \( E_1(T) \) is not \( S \)-invariant. The theorem is not contradicted: \( ST = \begin{pmatrix} 0 & 2 \\ 1 & 0 \end{pmatrix} \) and \( TS = \begin{pmatrix} 0 & 1 \\ 2 & 0 \end{pmatrix} \) differ.

::: {.check}
Let \( T = \I_2 \) and \( S = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) over \( \nR \). Do \( S \) and \( T \) commute? Is every eigenvector of \( T \) an eigenvector of \( S \)? Do \( S \) and \( T \) have a common eigenvector?
:::

::: {.solution}
Yes, \( \I_2 \) commutes with every \( 2 \times 2 \) matrix. No: every non-zero vector is an eigenvector of \( \I_2 \), but \( S\e_2 = (1, 1) \) is not a multiple of \( \e_2 \). Yes: \( \e_1 \) is an eigenvector of both, for the eigenvalues \( 1 \) and \( 1 \). The theorem says \( S \) maps \( E_1(T) = \nR^2 \) into itself, which is true but empty of information; the common eigenvector must be **searched for** inside that eigenspace, and here it is an eigenvector of \( S \).
:::

## A common eigenvector

Here is the plan for finding a common eigenvector of commuting \( S \) and \( T \). Pick an eigenvalue \( \lambda \) of \( T \) and put \( U = E_\lambda(T) \ne \{\0\} \). By @thm-commuting-preserves-eigenspaces, \( S \) restricts to an operator \( S|_U \) on \( U \). If \( S|_U \) has an eigenvector \( \u \), then \( S\u = \mu\u \) and, since \( \u \in U \), also \( T\u = \lambda\u \). So everything reduces to whether \( S|_U \) has an eigenvalue. Over \( \nC \) it does (@thm-complex-operator-has-eigenvalue). Over a general field we need to know that the characteristic polynomial of a restriction splits when that of \( S \) does. We record this, together with the same fact for the induced operator on the quotient, since triangularization will need both.

::: {#lem-invariant-charpoly-splits}
[Restrictions and Quotients Inherit Splitting]

Let \( V \) be a finite-dimensional vector space over \( F \), let \( T \in \cL(V) \), and let \( U \) be a \( T \)-invariant subspace with \( \{\0\} \ne U \ne V \). If \( p_T \) splits over \( F \), then \( p_{T|_U} \) and \( p_{\bar T} \) split over \( F \), where \( \bar T \) is the induced operator on \( V/U \).
:::

::: {.idea}
Section 1 factors \( p_T \) as \( p_{T|_U}\,p_{\bar T} \), so the two factors can only have roots that \( p_T \) has. A polynomial splits exactly when its root multiplicities add up to its degree (@thm-roots-with-multiplicity). Count: the multiplicities of the two factors add up to those of \( p_T \), which use up the whole degree; so neither factor can be short of its own degree.
:::

::: {.proof}
By @thm-invariant-subspace-matrix, \( p_T = f g \) with \( f = p_{T|_U} \) and \( g = p_{\bar T} \), both monic (@thm-charpoly-coefficients). Let \( c_1, \dots, c_k \) be the distinct roots of \( p_T \) in \( F \). Every root of \( f \) or of \( g \) in \( F \) is a root of \( p_T \) (@thm-evaluation-respects-operations), so it is among the \( c_i \), and a \( c_i \) that is not a root of \( f \) has \( \operatorname{mult}_{c_i}(f) = 0 \). Hence, by @thm-roots-with-multiplicity applied to \( f \) and to \( g \),
\[
\sum_{i=1}^{k} \operatorname{mult}_{c_i}(f) \le \deg f, \qquad \sum_{i=1}^{k} \operatorname{mult}_{c_i}(g) \le \deg g .
\]
Adding, and using @thm-multiplicity-of-product and then @thm-roots-with-multiplicity for the split polynomial \( p_T \),
\[
\begin{aligned}
\deg f + \deg g = \deg p_T
  &= \sum_{i=1}^{k} \operatorname{mult}_{c_i}(p_T) \\
  &= \sum_{i=1}^{k} \operatorname{mult}_{c_i}(f) + \sum_{i=1}^{k} \operatorname{mult}_{c_i}(g) \\
  &\le \deg f + \deg g .
\end{aligned}
\]
So both inequalities above are equalities, and \( f \) and \( g \) split over \( F \) by @thm-roots-with-multiplicity.
:::

Now the common eigenvector. We prove it for a whole family of commuting operators at once, possibly infinite, since the proof costs no more and the next theorems need it. A family \( \cF \subseteq \cL(V) \) is **commuting** if \( ST = TS \) for all \( S, T \in \cF \).

::: {#thm-commuting-common-eigenvector}
[Commuting Operators Have a Common Eigenvector]

Let \( V \ne \{\0\} \) be a finite-dimensional vector space over \( F \), and let \( \cF \subseteq \cL(V) \) be a non-empty commuting family such that \( p_T \) splits over \( F \) for every \( T \in \cF \). Then there is a non-zero \( \v \in V \) that is an eigenvector of **every** \( T \in \cF \). This applies to every commuting family when \( F = \nC \).
:::

::: {.idea}
For two operators, the plan above works: an eigenvector of \( S|_U \) with \( U = E_\lambda(T) \). For many operators we would like to repeat it, shrinking \( U \) each time, and a family may be infinite. So we jump straight to the end of the shrinking: take a non-zero subspace \( W \), invariant under the whole family, that is as small as possible. If some \( T \in \cF \) were not a scalar on \( W \), an eigenspace of \( T|_W \) would be a smaller such subspace. So every operator in the family is a scalar on \( W \), and any non-zero vector of \( W \) is a common eigenvector.
:::

::: {.proof}
Call a subspace **\( \cF \)-invariant** if it is \( T \)-invariant for every \( T \in \cF \). The space \( V \) is a non-zero \( \cF \)-invariant subspace, so among all non-zero \( \cF \)-invariant subspaces there is one, \( W \), of smallest dimension.

Let \( T \in \cF \). Then \( T|_W \) is an operator on \( W \ne \{\0\} \), and \( p_{T|_W} \) splits: if \( W = V \) this is the hypothesis, and otherwise it is @lem-invariant-charpoly-splits. Since \( p_{T|_W} \) is monic of degree \( \dim W \ge 1 \), it has a root \( \lambda \in F \), which is an eigenvalue of \( T|_W \) by @thm-eigenvalue-characterizations. Put
\[
W' = \{ \w \in W : T\w = \lambda\w \} = W \cap E_\lambda(T),
\]
which is non-zero because it contains an eigenvector of \( T|_W \). For every \( S \in \cF \), both \( W \) and \( E_\lambda(T) \) are \( S \)-invariant, the first by the choice of \( W \) and the second by @thm-commuting-preserves-eigenspaces; so \( W' \) is \( S \)-invariant by @prp-invariant-sum-intersection. Hence \( W' \) is a non-zero \( \cF \)-invariant subspace contained in \( W \), and by the minimality of \( \dim W \), \( \dim W' = \dim W \). By @thm-dim-impl-eq, \( W' = W \), that is, \( T\w = \lambda\w \) for every \( \w \in W \).

So every \( T \in \cF \) acts on \( W \) as multiplication by a scalar \( \lambda_T \). Any non-zero \( \v \in W \) then satisfies \( T\v = \lambda_T\v \) for every \( T \in \cF \), as claimed. Over \( \nC \) every characteristic polynomial splits (@cor-complex-polynomial-splits), so the hypothesis holds automatically.
:::

The proof never had to name the eigenvalues. It found a subspace on which every operator of the family is a scalar, and the scalars came for free.

::: {.warning}
**The splitting hypothesis cannot be dropped, and neither can commuting.** Over \( \nR \), the rotation \( \R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \) commutes with itself, yet the family \( \{\R\} \) has no real eigenvector at all, since \( p_{\R} = x^2 + 1 \) has no real root. Over \( \nC \), the non-commuting pair \( \E_{12}, \E_{21} \) has no common eigenvector, as we saw above.
:::

## Simultaneous triangularization

Section 7 triangularized one operator by splitting off an eigenvector and passing to the quotient. For a commuting family the same recursion works, because the eigenvector we split off can be chosen common to all.

::: {#thm-simultaneous-triangularization}
[Simultaneous Triangularization]

Let \( V \) be a finite-dimensional vector space over \( F \) with \( \dim V = n \ge 1 \), and let \( \cF \subseteq \cL(V) \) be a non-empty commuting family such that \( p_T \) splits over \( F \) for every \( T \in \cF \). Then there is **one** basis \( \sB \) of \( V \) such that \( \mtx{T}{\sB}{\sB} \) is upper triangular for **every** \( T \in \cF \).

In particular, if \( \A_1, \dots, \A_r \in M_n(\nC) \) commute pairwise, there is an invertible \( \P \in M_n(\nC) \) such that \( \P^{-1}\A_i\P \) is upper triangular for every \( i \).
:::

::: {.idea}
**Take one common eigenvector, extend, recurse.** ① @thm-commuting-common-eigenvector gives \( \v_1 \), an eigenvector of every \( T \in \cF \), so \( U = \Span(\v_1) \) is invariant under the family. ② On \( V/U \), the induced operators still commute, and their characteristic polynomials still split. ③ By induction on the dimension, one basis of \( V/U \) triangularizes all of them. ④ Lift it back and put \( \v_1 \) in front; the block triangular form of Section 1 does the rest.
:::

::: {.proof}
We use induction on \( n \). If \( n = 1 \), every \( 1 \times 1 \) matrix is upper triangular, so any basis works.

Let \( n \ge 2 \), and assume the theorem for spaces of dimension \( n - 1 \). By @thm-commuting-common-eigenvector there is \( \v_1 \ne \0 \) with \( T\v_1 = \lambda_T\v_1 \) for every \( T \in \cF \). Let \( U = \Span(\v_1) \); it is \( T \)-invariant for every \( T \in \cF \) (@prp-one-dimensional-invariant), and \( \{\0\} \ne U \ne V \) since \( \dim U = 1 < n \). For \( T \in \cF \) let \( \bar T \) be the induced operator on \( V/U \) (@def-restriction-operator), and put \( \bar\cF = \{ \bar T : T \in \cF \} \).

The family \( \bar\cF \) is commuting: for \( S, T \in \cF \) and \( \v \in V \),
\[
\bar S\bar T(\v + U) = \bar S(T\v + U) = ST\v + U = TS\v + U = \bar T\bar S(\v + U).
\]
Each \( p_{\bar T} \) splits by @lem-invariant-charpoly-splits, and \( \dim V/U = n - 1 \) by @thm-dimension-quotient. By the induction hypothesis there are \( \w_2, \dots, \w_n \in V \) such that \( \bar\sB = (\w_2 + U, \dots, \w_n + U) \) is a basis of \( V/U \) in which every \( \mtx{\bar T}{\bar\sB}{\bar\sB} \) is upper triangular.

Let \( \sB = (\v_1, \w_2, \dots, \w_n) \). It is linearly independent: if \( a_1\v_1 + a_2\w_2 + \dots + a_n\w_n = \0 \), then passing to \( V/U \), where \( \v_1 + U \) is the zero coset, gives \( a_2(\w_2 + U) + \dots + a_n(\w_n + U) = \0 \), so \( a_2 = \dots = a_n = 0 \) by the independence of \( \bar\sB \); then \( a_1\v_1 = \0 \) with \( \v_1 \ne \0 \) gives \( a_1 = 0 \). A linearly independent list of length \( n = \dim V \) is a basis (@thm-right-size-basis). Now \( \sB \) is a basis of \( U \) extended to a basis of \( V \), and \( \bar\sB \) is exactly the list of cosets in @thm-invariant-subspace-matrix. Hence for every \( T \in \cF \),
\[
\mtx{T}{\sB}{\sB} = \begin{pmatrix} \lambda_T & \ast \\ 0 & \mtx{\bar T}{\bar\sB}{\bar\sB} \end{pmatrix},
\]
with a \( 1 \times 1 \) upper-left block, a zero column below it, and an upper triangular lower-right block. Such a matrix is upper triangular. This completes the induction.

For the matrix statement, apply this to the family \( \{T_{\A_1}, \dots, T_{\A_r}\} \) on \( \nC^n \), whose characteristic polynomials split by @cor-complex-polynomial-splits, and let \( \P \) have the vectors of \( \sB \) as columns; then \( \P^{-1}\A_i\P = \mtx{T_{\A_i}}{\sB}{\sB} \) (@thm-change-of-basis-maps).
:::

A first use: if \( S \) and \( T \) commute and both characteristic polynomials split, the diagonal entries of \( \mtx{S + T}{\sB}{\sB} \) and \( \mtx{ST}{\sB}{\sB} \) are the sums and products of the diagonal entries of \( \mtx{S}{\sB}{\sB} \) and \( \mtx{T}{\sB}{\sB} \), position by position. For the sum this is entrywise; for the product, the \( (i, i) \)-entry of \( \X \Y \) is \( \sum_k x_{ik}y_{ki} \) (@def-matrix-multiplication), and when \( \X \) and \( \Y \) are upper triangular only \( k = i \) can contribute, since \( x_{ik} = 0 \) for \( k < i \) and \( y_{ki} = 0 \) for \( k > i \). By @thm-diagonal-of-triangular-form, those diagonal entries are the eigenvalues. So the eigenvalues of \( S + T \) are of the form \( \lambda + \mu \), with \( \lambda \) an eigenvalue of \( S \) and \( \mu \) one of \( T \), **paired by position in a common triangular form**. Section 2 warned that nothing like this holds without commuting.

## Simultaneous diagonalization

Diagonalization is the stronger wish, and it needs a stronger hypothesis: each operator must be diagonalizable on its own. The name for the goal:

::: {#def-simultaneously-diagonalizable}
[Simultaneously Diagonalizable]

Let \( V \) be finite-dimensional. A family \( \cF \subseteq \cL(V) \) is **simultaneously diagonalizable** if there is **one** basis \( \sB \) of \( V \) such that \( \mtx{T}{\sB}{\sB} \) is diagonal for **every** \( T \in \cF \). Matrices \( \A_1, \dots, \A_r \in M_n(F) \) are simultaneously diagonalizable over \( F \) if there is **one** invertible \( \P \in M_n(F) \) with every \( \P^{-1}\A_i\P \) diagonal.
:::

Equivalently, by the unwinding in Section 4, \( V \) has a basis whose vectors are eigenvectors of every \( T \in \cF \). The opening of this section showed that a simultaneously diagonalizable family is commuting. For diagonalizable operators the converse holds.

::: {#thm-simultaneous-diagonalization}
[Simultaneous Diagonalization]

Let \( V \) be a finite-dimensional vector space over \( F \) with \( \dim V \ge 1 \), and let \( S, T \in \cL(V) \) be diagonalizable. Then \( S \) and \( T \) are simultaneously diagonalizable if and only if \( ST = TS \).

For matrices: if \( \A, \B \in M_n(F) \) are diagonalizable over \( F \), there is an invertible \( \P \in M_n(F) \) with \( \P^{-1}\A \P \) and \( \P^{-1}\B \P \) both diagonal if and only if \( \A \B = \B \A \).
:::

::: {.idea}
Split \( V \) into the eigenspaces of \( T \). On each piece \( T \) is a scalar, so **any** basis of the piece consists of eigenvectors of \( T \); we are free to choose it to suit \( S \). The piece is \( S \)-invariant because \( S \) commutes with \( T \), and \( S \) restricted to it is diagonalizable because \( S \) is (Section 8). So each piece has a basis of eigenvectors of \( S \), and gluing these bases together gives the common basis.
:::

::: {.proof}
\( (\Rightarrow) \) Let \( \sB \) be a basis with \( \mtx{S}{\sB}{\sB} \) and \( \mtx{T}{\sB}{\sB} \) diagonal. Diagonal matrices commute, so by @cor-matrix-of-polynomial-of-operator, \( \mtx{ST}{\sB}{\sB} = \mtx{S}{\sB}{\sB}\mtx{T}{\sB}{\sB} = \mtx{T}{\sB}{\sB}\mtx{S}{\sB}{\sB} = \mtx{TS}{\sB}{\sB} \). The map \( \R \mapsto \mtx{\R}{\sB}{\sB} \) is injective (@thm-linear-maps-isomorphic-to-matrices), so \( ST = TS \).

\( (\Leftarrow) \) Suppose \( ST = TS \). Let \( \lambda_1, \dots, \lambda_k \) be the distinct eigenvalues of \( T \), and put \( U_i = E_{\lambda_i}(T) \). Since \( T \) is diagonalizable, @thm-diagonalization (c) gives
\[
V = U_1 \oplus \dots \oplus U_k .
\]
Each \( U_i \) is \( S \)-invariant (@thm-commuting-preserves-eigenspaces), and \( S \) is diagonalizable, so \( S|_{U_i} \) is diagonalizable by @cor-restriction-diagonalizable. Hence \( U_i \) has a basis \( \sB_i \) of eigenvectors of \( S|_{U_i} \) (@thm-diagonalization (b)), which are eigenvectors of \( S \). They are also eigenvectors of \( T \), being non-zero vectors of \( U_i = E_{\lambda_i}(T) \). Let \( \sB \) be the list \( \sB_1, \dots, \sB_k \). Since the sum is direct, \( \sB \) is a basis of \( V \) by @thm-direct-sum-k-criteria ((a) \( \Rightarrow \) (d)). Every vector of \( \sB \) is an eigenvector of both \( S \) and \( T \), so \( \mtx{S}{\sB}{\sB} \) and \( \mtx{T}{\sB}{\sB} \) are diagonal (@thm-diagonalization, (a) \( \Leftrightarrow \) (b)).

For matrices, apply this to \( T_{\A} \) and \( T_{\B} \) on \( F^n \), which are diagonalizable because \( \A \) and \( \B \) are (@def-diagonalizable), and commute because \( \A \B = \B \A \); let \( \P \) have the common eigenvectors as columns, as in Section 4.
:::

The proof is also an algorithm. Diagonalize \( \A \); in each eigenspace of \( \A \) of dimension at least \( 2 \), write down the matrix of \( \B \) restricted to it and diagonalize that small matrix; eigenspaces of dimension \( 1 \) need no work, since their basis vector is automatically an eigenvector of \( \B \).

::: {#exm-simultaneous-diagonalization}
[Diagonalizing Two Commuting Matrices Together]

Let
\[
\A = \begin{pmatrix} 1 & 0 & 0 \\ -2 & 1 & 2 \\ -2 & 0 & 3 \end{pmatrix}, \qquad \B = \begin{pmatrix} 1 & -2 & 2 \\ 0 & 1 & 0 \\ 0 & -2 & 3 \end{pmatrix} \in M_3(\nR).
\]
Check that \( \A \B = \B \A \), and find an invertible \( \P \) such that \( \P^{-1}\A \P \) and \( \P^{-1}\B \P \) are both diagonal.
:::

::: {.solution}
*They commute.* Multiplying out,
\[
\A \B = \begin{pmatrix} 1 & -2 & 2 \\ -2 & 1 & 2 \\ -2 & -2 & 5 \end{pmatrix} = \B \A .
\]

*Diagonalize \( \A \).* Expanding \( \det(x\I - \A) \) along the first row, whose only non-zero entry is \( x - 1 \),
\[
p_{\A}(x) = (x - 1)\det\begin{pmatrix} x - 1 & -2 \\ 0 & x - 3 \end{pmatrix} = (x - 1)^2(x - 3).
\]
For \( \lambda = 1 \), \( \A - \I = \begin{pmatrix} 0 & 0 & 0 \\ -2 & 0 & 2 \\ -2 & 0 & 2 \end{pmatrix} \) has rank \( 1 \) and reduces to \( x = z \), so \( E_1(\A) \) is the plane with basis \( \u_1 = (0, 1, 0) \), \( \u_2 = (1, 0, 1) \). For \( \lambda = 3 \), \( \A - 3\I = \begin{pmatrix} -2 & 0 & 0 \\ -2 & -2 & 2 \\ -2 & 0 & 0 \end{pmatrix} \) gives \( x = 0 \) and \( y = z \), so \( E_3(\A) = \Span((0, 1, 1)) \). Since \( g(1) = 2 = a(1) \) and \( g(3) = 1 = a(3) \), \( \A \) is diagonalizable. The same computation for \( \B \) gives \( p_{\B} = (x - 1)^2(x - 3) \), with \( \B - \I = \begin{pmatrix} 0 & -2 & 2 \\ 0 & 0 & 0 \\ 0 & -2 & 2 \end{pmatrix} \) of rank \( 1 \) and \( \B - 3\I \) of rank \( 2 \), so \( \B \) is diagonalizable as well.

A basis of eigenvectors of \( \A \) need not work for \( \B \): \( \B\u_1 = (-2, 1, -2) \) is not a multiple of \( \u_1 \). This is where the search inside the eigenspace comes in.

*The one-dimensional eigenspace.* \( E_3(\A) \) is \( \B \)-invariant (@thm-commuting-preserves-eigenspaces) and one-dimensional, so \( \v_3 = (0, 1, 1) \) is an eigenvector of \( \B \): indeed \( \B\v_3 = (0, 1, 1) = 1\cdot\v_3 \).

*The plane \( E_1(\A) \).* It is \( \B \)-invariant, and
\[
\B\u_1 = (-2, 1, -2) = \u_1 - 2\u_2, \qquad \B\u_2 = (3, 0, 3) = 3\u_2 .
\]
So the matrix of \( \B|_{E_1(\A)} \) in the basis \( (\u_1, \u_2) \) is \( \M = \begin{pmatrix} 1 & 0 \\ -2 & 3 \end{pmatrix} \), whose columns are the coordinates just found. It is lower triangular with eigenvalues \( 1 \) and \( 3 \). From \( \M - \I = \begin{pmatrix} 0 & 0 \\ -2 & 2 \end{pmatrix} \) the eigenvector is \( (1, 1) \), which stands for \( \u_1 + \u_2 = (1, 1, 1) \); from \( \M - 3\I = \begin{pmatrix} -2 & 0 \\ -2 & 0 \end{pmatrix} \) it is \( (0, 1) \), which stands for \( \u_2 = (1, 0, 1) \).

*The common basis.* Put \( \v_1 = (1, 0, 1) \), \( \v_2 = (1, 1, 1) \), \( \v_3 = (0, 1, 1) \) as columns:
\[
\P = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix}, \qquad \P^{-1}\A \P = \diag(1, 1, 3), \qquad \P^{-1}\B \P = \diag(3, 1, 1).
\]
*Check.* \( \A\v_1 = \v_1 \), \( \A\v_2 = \v_2 \), \( \A\v_3 = (0, 3, 3) = 3\v_3 \); \( \B\v_1 = (3, 0, 3) = 3\v_1 \), \( \B\v_2 = \v_2 \), \( \B\v_3 = \v_3 \). Expanding along the first row, \( \det \P = 1(1 - 1) - 1(0 - 1) + 0 = 1 \ne 0 \), so \( \P \) is invertible, with \( \P^{-1} = \begin{pmatrix} 0 & -1 & 1 \\ 1 & 1 & -1 \\ -1 & 0 & 1 \end{pmatrix} \).

Notice that neither matrix alone determines \( \P \): \( \A \) cannot tell \( \v_1 \) from \( \v_2 \), and \( \B \) cannot tell \( \v_2 \) from \( \v_3 \). Together they pin down all three lines.
:::

::: {.warning}
**Commuting does not make an operator diagonalizable.** The theorem assumes that both \( S \) and \( T \) are diagonalizable. \( \J = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) commutes with \( \I_2 \), and \( \I_2 \) is diagonal, but \( \J \) is not diagonalizable (Section 4), so no basis makes both diagonal. What survives is @thm-simultaneous-triangularization: \( \J \) and \( \I_2 \) are already upper triangular together.
:::

The theorem extends from two operators to any number, and even to infinitely many. An infinite family looks hopeless for an induction, but it lives inside the finite-dimensional space \( \cL(V) \), so finitely many of its members already span everything the family spans.

::: {#thm-simultaneous-diagonalization-family}
[Simultaneous Diagonalization of a Commuting Family]

Let \( V \) be a finite-dimensional vector space over \( F \) with \( \dim V \ge 1 \), and let \( \cF \subseteq \cL(V) \) be a family of diagonalizable operators. Then \( \cF \) is simultaneously diagonalizable if and only if it is commuting.
:::

::: {.idea}
① **Finite first.** For finitely many commuting diagonalizable \( T_1, \dots, T_r \), induct on \( r \): split \( V \) into eigenspaces of \( T_1 \), and on each piece apply the case \( r - 1 \) to the restrictions of \( T_2, \dots, T_r \). ② **Reduce to finite.** A longest linearly independent list \( T_1, \dots, T_r \) taken from \( \cF \) spans every member of \( \cF \), and has length at most \( \dim\cL(V) \). ③ A basis that diagonalizes \( T_1, \dots, T_r \) diagonalizes every linear combination of them.
:::

::: {.proof}
\( (\Rightarrow) \) If one basis makes every \( \mtx{T}{\sB}{\sB} \) diagonal, any two of these matrices commute, and the argument of @thm-simultaneous-diagonalization \( (\Rightarrow) \) gives \( ST = TS \) for all \( S, T \in \cF \).

\( (\Leftarrow) \) Suppose \( \cF \) is commuting. If \( \cF \) is empty, any basis works; assume not.

**Step 1: finitely many operators.** We prove by induction on \( r \ge 1 \): for every non-zero finite-dimensional space \( W \) and all pairwise commuting diagonalizable \( T_1, \dots, T_r \in \cL(W) \), some basis of \( W \) consists of eigenvectors of every \( T_i \). For \( r = 1 \) this is @thm-diagonalization. Let \( r \ge 2 \), and let \( \lambda_1, \dots, \lambda_k \) be the distinct eigenvalues of \( T_1 \), with \( U_j = E_{\lambda_j}(T_1) \ne \{\0\} \). By @thm-diagonalization (c), \( W = U_1 \oplus \dots \oplus U_k \). Each \( U_j \) is \( T_i \)-invariant for every \( i \) (@thm-commuting-preserves-eigenspaces), each \( T_i|_{U_j} \) is diagonalizable (@cor-restriction-diagonalizable), and the restrictions \( T_2|_{U_j}, \dots, T_r|_{U_j} \) commute pairwise, since they agree with \( T_2, \dots, T_r \) on \( U_j \). By the induction hypothesis, \( U_j \) has a basis \( \sB_j \) of common eigenvectors of \( T_2, \dots, T_r \); they are eigenvectors of \( T_1 \) too, as non-zero vectors of \( U_j \). The list \( \sB_1, \dots, \sB_k \) is a basis of \( W \) by @thm-direct-sum-k-criteria ((a) \( \Rightarrow \) (d)). This completes the induction.

**Step 2: a finite spanning subfamily.** Let \( N = \dim\cL(V) = (\dim V)^2 \) (@thm-linear-maps-isomorphic-to-matrices). Every linearly independent list in \( \cL(V) \) has length at most \( N \) (@thm-basis-extension), so among the linearly independent lists of members of \( \cF \) there is one of greatest length, say \( (T_1, \dots, T_r) \), with \( r \ge 1 \) because a single non-zero member is independent (if every member of \( \cF \) is \( 0 \), any basis works). For every \( T \in \cF \), the list \( (T_1, \dots, T_r, T) \) is longer, hence dependent, so \( T \in \Span(T_1, \dots, T_r) \) by @lem-append-independent.

**Step 3.** By Step 1 there is a basis \( \sB \) of \( V \) with every \( \mtx{T_i}{\sB}{\sB} \) diagonal. For \( T \in \cF \), write \( T = c_1T_1 + \dots + c_rT_r \); then \( \mtx{T}{\sB}{\sB} = c_1\mtx{T_1}{\sB}{\sB} + \dots + c_r\mtx{T_r}{\sB}{\sB} \) (@cor-matrix-of-polynomial-of-operator), a linear combination of diagonal matrices, hence diagonal. So \( \sB \) diagonalizes every member of \( \cF \).
:::

A typical infinite family is \( \{ p(T) : p \in F[x] \} \) for a diagonalizable \( T \). It is commuting, each \( p(T) \) is diagonalizable (Section 8), and here one basis works for the whole family without any of the theorem's machinery, namely an eigenbasis of \( T \): an eigenvector of \( T \) for \( \lambda \) is an eigenvector of \( p(T) \) for \( p(\lambda) \) (@exr-eigenvalues-and-eigenvectors-b3). The theorem says the same for families that are not generated by one operator in so visible a way.

## Exercises

### A. Check your understanding

:::: {#exr-commuting-operators-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the theorem relating commuting operators and eigenspaces.
2. True or false: if \( ST = TS \), then every eigenvector of \( T \) is an eigenvector of \( S \). Justify your answer.
3. True or false: any two commuting matrices in \( M_2(\nR) \) have a common eigenvector in \( \nR^2 \). Justify your answer.
4. True or false: if \( \A, \B \in M_n(F) \) are simultaneously diagonalizable, then \( \A \B = \B \A \). Justify your answer.
5. True or false: if \( \A \B = \B \A \) and \( \A \) is diagonalizable, then \( \B \) is diagonalizable. Justify your answer.
6. In the proof of @thm-simultaneous-diagonalization, which hypothesis makes each eigenspace of \( T \) invariant under \( S \), and which makes the restriction of \( S \) diagonalizable?
:::
::::

::: {.solution}
(a) If \( S, T \in \cL(V) \) and \( ST = TS \), then \( E_\lambda(T) \) is \( S \)-invariant for every \( \lambda \in F \) (@thm-commuting-preserves-eigenspaces).

(b) False. \( T = \I_2 \) commutes with \( S = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \); the vector \( \e_2 \) is an eigenvector of \( T \), but \( S\e_2 = (1, 1) \) is not a multiple of \( \e_2 \).

(c) False. The rotation \( \R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \) commutes with itself and has no real eigenvector, since \( p_{\R} = x^2 + 1 \) has no real root.

(d) True. If \( \P^{-1}\A \P = \D \) and \( \P^{-1}\B \P = \D' \) are diagonal, then \( \A \B = \P \D \P^{-1}\P \D'\P^{-1} = \P \D \D'\P^{-1} = \P \D'\D \P^{-1} = \B \A \), since diagonal matrices commute.

(e) False. \( \A = \I_2 \) is diagonalizable and commutes with \( \B = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \), which is not diagonalizable.

(f) The hypothesis \( ST = TS \) gives the invariance (@thm-commuting-preserves-eigenspaces). The hypothesis that \( S \) is diagonalizable gives, through @cor-restriction-diagonalizable, that \( S|_{E_\lambda(T)} \) is diagonalizable.
:::

### B. Practice

:::: {#exr-commuting-operators-b1}
[B1: Common eigenvectors]

Let
\[
\A = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & -1 & 2 \end{pmatrix}, \qquad \B = \begin{pmatrix} 2 & 1 & 0 \\ -1 & 4 & 0 \\ 2 & -2 & 5 \end{pmatrix} \in M_3(\nR).
\]

::: {.enumerate options="label=(\alph*)"}
1. Verify that \( \A \B = \B \A \).
2. Find every common eigenvector of \( \A \) and \( \B \).
3. Hence show that \( \A \) and \( \B \) are not simultaneously diagonalizable, and explain which hypothesis of @thm-simultaneous-diagonalization fails.
:::
::::

::: {.solution}
(a) Multiplying out,
\[
\A \B = \begin{pmatrix} 2 & 1 & 0 \\ -1 & 4 & 0 \\ 7 & -7 & 10 \end{pmatrix} = \B \A .
\]
For instance, the \( (3, 1) \)-entry of \( \A \B \) is row \( (1, -1, 2) \) of \( \A \) times column \( (2, -1, 2) \) of \( \B \), namely \( 2 + 1 + 4 = 7 \), and that of \( \B \A \) is row \( (2, -2, 5) \) of \( \B \) times column \( (1, 0, 1) \) of \( \A \), namely \( 2 + 0 + 5 = 7 \).

(b) \( \A \) is lower triangular, so \( p_{\A} = (x - 1)^2(x - 2) \). \( \A - \I = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 1 & -1 & 1 \end{pmatrix} \) has rank \( 1 \), so \( E_1(\A) = \{ (x, y, z) : x - y + z = 0 \} \) with basis \( \u_1 = (1, 1, 0) \), \( \u_2 = (-1, 0, 1) \). \( \A - 2\I = \begin{pmatrix} -1 & 0 & 0 \\ 0 & -1 & 0 \\ 1 & -1 & 0 \end{pmatrix} \) gives \( E_2(\A) = \Span(\e_3) \).

A common eigenvector is an eigenvector of \( \A \), so it lies in \( E_1(\A) \) or \( E_2(\A) \), and it must be an eigenvector of \( \B \) there. On the line \( E_2(\A) \): \( \B\e_3 = (0, 0, 5) = 5\e_3 \), so every non-zero multiple of \( \e_3 \) is a common eigenvector. On the plane \( E_1(\A) \), which is \( \B \)-invariant by @thm-commuting-preserves-eigenspaces:
\[
\B\u_1 = (3, 3, 0) = 3\u_1, \qquad \B\u_2 = (-2, 1, 3) = \u_1 + 3\u_2 .
\]
So in the basis \( \sB = (\u_1, \u_2) \), \( \mtx{\B|_{E_1(\A)}}{\sB}{\sB} = \begin{pmatrix} 3 & 1 \\ 0 & 3 \end{pmatrix} \). Its only eigenvalue is \( 3 \), and its eigenvectors are the non-zero multiples of \( (1, 0) \), that is, of \( \u_1 \). Hence the common eigenvectors are exactly the non-zero multiples of \( (1, 1, 0) \) and the non-zero multiples of \( (0, 0, 1) \).

(c) By (b), any list of common eigenvectors lies in \( \Span((1, 1, 0), \e_3) \), a plane, so no three of them form a basis of \( \nR^3 \). Hence no basis diagonalizes both. The failing hypothesis is that \( \B \) is diagonalizable: \( p_{\B} = (x - 3)^2(x - 5) \) (from the block computation, \( p_{\B} = p_{\B|_{E_1(\A)}}\,p_{\bar \B} \), or directly), and \( \B - 3\I = \begin{pmatrix} -1 & 1 & 0 \\ -1 & 1 & 0 \\ 2 & -2 & 2 \end{pmatrix} \) has rank \( 2 \), so \( g_{\B}(3) = 1 < 2 = a_{\B}(3) \).
:::

:::: {#exr-commuting-operators-b2}
[B2: Decide simultaneous diagonalizability]

For each pair of real matrices, determine whether they are simultaneously diagonalizable over \( \nR \). If they are, find a suitable \( \P \). Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \A = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix} \), \( \B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \).
2. \( \A = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix} \), \( \B = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix} \).
3. \( \A = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} \), \( \B = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} \).
:::
::::

::: {.solution}
(a) Yes. \( \A \B = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} = \B \A \). Both are diagonalizable: \( \A \) has \( p_{\A} = x^2 - 2x - 3 = (x - 3)(x + 1) \) and \( \B \) has \( p_{\B} = x^2 - 1 = (x - 1)(x + 1) \), each with distinct eigenvalues (@cor-distinct-eigenvalues-diagonalizable). By @thm-simultaneous-diagonalization a common \( \P \) exists. The eigenspaces of \( \A \) are lines, so their spanning vectors \( (1, 1) \) and \( (1, -1) \) work: \( \P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \), \( \P^{-1}\A \P = \diag(3, -1) \), \( \P^{-1}\B \P = \diag(1, -1) \), since \( \B(1, 1) = (1, 1) \) and \( \B(1, -1) = (-1, 1) \).

(b) No. Both are diagonalizable (distinct eigenvalues \( 1, 2 \)), but \( \A \B = \begin{pmatrix} 1 & 2 \\ 0 & 4 \end{pmatrix} \ne \begin{pmatrix} 1 & 1 \\ 0 & 4 \end{pmatrix} = \B \A \), so by @thm-simultaneous-diagonalization \( (\Rightarrow) \) no common \( \P \) exists.

(c) No. They commute, since \( \A = 2\I \). But \( \B \) is not diagonalizable: \( p_{\B} = (x - 2)^2 \) and \( \B - 2\I \) has rank \( 1 \), so \( g(2) = 1 < 2 \). If \( \P^{-1}\B \P \) were diagonal, \( \B \) would be diagonalizable (@def-diagonalizable).
:::

:::: {#exr-commuting-operators-b3}
[B3: Matrices commuting with a diagonal matrix]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \D = \diag(1, 2, 3) \in M_3(\nR) \). Prove that a matrix \( \B \in M_3(\nR) \) commutes with \( \D \) if and only if \( \B \) is diagonal.
2. Let \( \D' = \diag(1, 1, 2) \in M_3(\nR) \). Describe all \( \B \in M_3(\nR) \) with \( \B \D' = \D'\B \), and find one that is not diagonalizable.
:::
::::

::: {.solution}
(a) \( (\Leftarrow) \) Diagonal matrices commute. \( (\Rightarrow) \) Suppose \( \B \D = \D \B \). The eigenspaces of \( \D \) are \( E_1(\D) = \Span(\e_1) \), \( E_2(\D) = \Span(\e_2) \) and \( E_3(\D) = \Span(\e_3) \). By @thm-commuting-preserves-eigenspaces each is \( \B \)-invariant, so \( \B\e_j \in \Span(\e_j) \) for each \( j \). The \( j \)-th column of \( \B \) is \( \B\e_j \), so it has zeros off the diagonal, and \( \B \) is diagonal. (Directly: \( (\D \B)_{ij} = i\,b_{ij} \) and \( (\B \D)_{ij} = b_{ij}\,j \), so \( (i - j)b_{ij} = 0 \), and \( b_{ij} = 0 \) for \( i \ne j \).)

(b) As computed in the text for \( \diag(1, 1, 2) \), \( \B \D' = \D'\B \) exactly when \( \B = \begin{pmatrix} b_{11} & b_{12} & 0 \\ b_{21} & b_{22} & 0 \\ 0 & 0 & b_{33} \end{pmatrix} \) with arbitrary entries: \( E_1(\D') = \Span(\e_1, \e_2) \) and \( E_2(\D') = \Span(\e_3) \) are \( \B \)-invariant, which by @thm-direct-sum-invariant-block-diagonal forces this shape, and conversely \( \D' = \I_2 \oplus (2) \) commutes with every such block matrix (@thm-block-diagonal-arithmetic). For example \( \B = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix} \) commutes with \( \D' \), and it is not diagonalizable: \( p_{\B} = x(x - 1)^2 \) and \( \B - \I \) has rank \( 2 \), so \( g(1) = 1 < 2 = a(1) \).
:::

### C. Going deeper

:::: {#exr-commuting-operators-c1}
[C1: The commutant of a matrix with distinct eigenvalues]

Let \( \A \in M_n(F) \), \( n \ge 1 \), have \( n \) distinct eigenvalues \( \lambda_1, \dots, \lambda_n \in F \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( \A \B = \B \A \), then \( \B \) is diagonalizable and every eigenvector of \( \A \) is an eigenvector of \( \B \).
2. Prove that if \( \A \B = \B \A \), then \( \B = q(\A) \) for some \( q \in F[x] \) of degree at most \( n - 1 \).
3. Deduce that \( \{ \B \in M_n(F) : \A \B = \B \A \} \) is a subspace of \( M_n(F) \) of dimension \( n \), with basis \( (\I, \A, \dots, \A^{n-1}) \).
:::

*Hint: for (b), use Lagrange interpolation.*
::::

::: {.solution}
(a) By @cor-distinct-eigenvalues-diagonalizable, \( \A \) is diagonalizable, say \( \P^{-1}\A \P = \D \) with \( \D \) diagonal. A diagonal matrix is upper triangular, so its diagonal entries are the eigenvalues of \( \A \), each occurring as often as its algebraic multiplicity (@thm-diagonal-of-triangular-form (b)); here there are \( n \) distinct eigenvalues and \( n \) diagonal places, so each occurs once, and after permuting the columns of \( \P \) and the diagonal entries of \( \D \) together we may assume \( \D = \diag(\lambda_1, \dots, \lambda_n) \). Let \( \v_i \) be column \( i \) of \( \P \). Each \( E_{\lambda_i}(\A) \) has dimension at least \( 1 \), and the dimensions add up to at most \( n \) (@cor-eigenspaces-direct-sum), so each has dimension exactly \( 1 \) and \( E_{\lambda_i}(\A) = \Span(\v_i) \). Every eigenvector of \( \A \) for \( \lambda_i \) is a non-zero multiple of \( \v_i \). By @thm-commuting-preserves-eigenspaces, \( \B\v_i \in \Span(\v_i) \), so \( \B\v_i = \mu_i\v_i \) for some \( \mu_i \in F \), and \( \v_i \), with every non-zero multiple of it, is an eigenvector of \( \B \). The columns of \( \P \) form a basis of eigenvectors of \( \B \), so \( \P^{-1}\B \P = \diag(\mu_1, \dots, \mu_n) \) and \( \B \) is diagonalizable.

(b) The nodes \( \lambda_1, \dots, \lambda_n \) are distinct, so by @thm-lagrange-interpolation there is \( q \in F[x] \) with \( \deg q \le n - 1 \) and \( q(\lambda_i) = \mu_i \) for every \( i \). By @thm-powers-diagonalizable,
\[
q(\A) = \P\,\diag\big(q(\lambda_1), \dots, q(\lambda_n)\big)\,\P^{-1} = \P\,\diag(\mu_1, \dots, \mu_n)\,\P^{-1} = \B .
\]

(c) If \( \A \B = \B \A \) and \( \A \B' = \B'\A \), then \( \A(c\B + \B') = c\B \A + \B'\A = (c\B + \B')\A \), and \( \A0 = 0\A \); so the set \( \mathcal{C} \) is a subspace. Each \( \A^k \) commutes with \( \A \), so \( \Span(\I, \A, \dots, \A^{n-1}) \subseteq \mathcal{C} \), and (b) gives the reverse inclusion. For independence, let \( c_0\I + c_1\A + \dots + c_{n-1}\A^{n-1} = 0 \) and put \( q = \sum_k c_kx^k \). By @thm-powers-diagonalizable, \( 0 = q(\A) = \P\,\diag(q(\lambda_1), \dots, q(\lambda_n))\,\P^{-1} \), so \( q(\lambda_i) = 0 \) for all \( i \). A polynomial of degree at most \( n - 1 \) with \( n \) distinct roots is zero (@cor-root-bound-general), so every \( c_k = 0 \). Hence \( (\I, \A, \dots, \A^{n-1}) \) is a basis of \( \mathcal{C} \), and \( \dim\mathcal{C} = n \).
:::

:::: {#exr-commuting-operators-c2}
[C2: Commuting nilpotent matrices]

Recall that \( \N \in M_n(F) \) is **nilpotent** if \( \N^a = 0 \) for some \( a \ge 1 \) (@exr-eigenvalues-and-eigenvectors-c2). Let \( \N, \M \in M_n(F) \) with \( \N\M = \M \N \), \( \N^a = 0 \) and \( \M^b = 0 \) for some \( a, b \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \N\M \) is nilpotent.
2. Prove that \( (\N + \M)^{a + b - 1} = 0 \), so that \( \N + \M \) is nilpotent.
3. Show that both conclusions can fail without \( \N\M = \M \N \).
4. Now let \( F = \nC \). Give a second proof of (b) using @thm-simultaneous-triangularization.
:::

*Hint: for (b), expand the power as a sum of products of \( a + b - 1 \) factors, each equal to \( \N \) or \( \M \).*
::::

::: {.solution}
(a) Since \( \N\M = \M \N \), induction on \( k \) gives \( (\N\M)^k = \N^k\M^k \): if it holds for \( k \), then \( (\N\M)^{k+1} = \N^k\M^k\N\M = \N^k\N\M^k\M = \N^{k+1}\M^{k+1} \), where \( \M^k\N = \N\M^k \) follows from \( \M \N = \N\M \) by induction as well. With \( k = a \), \( (\N\M)^a = \N^a\M^a = 0 \cdot \M^a = 0 \).

(b) Let \( s = a + b - 1 \). By distributivity, \( (\N + \M)^s \) is the sum of all \( 2^s \) products \( \X_1\X_2\cdots \X_s \) with each \( \X_t \in \{\N, \M\} \). Since \( \N \) and \( \M \) commute, each such product can be rearranged, one adjacent swap at a time, into \( \N^i\M^{s-i} \), where \( i \) is the number of factors equal to \( \N \). If \( i \ge a \), then \( \N^i = \N^a\N^{i-a} = 0 \). If \( i \le a - 1 \), then \( s - i \ge s - a + 1 = b \), so \( \M^{s-i} = 0 \). Either way the product is \( 0 \), so \( (\N + \M)^s = 0 \).

(c) Let \( \N = \E_{12} \) and \( \M = \E_{21} \) in \( M_2(F) \). Both square to \( 0 \). But \( \N\M = \E_{11} \) satisfies \( \E_{11}^k = \E_{11} \ne 0 \) for all \( k \ge 1 \), and \( \N + \M = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) satisfies \( (\N + \M)^2 = \I \), so \( (\N + \M)^k \) is \( \I \) or \( \N + \M \), never \( 0 \). Neither is nilpotent, and indeed \( \N\M = \E_{11} \ne \E_{22} = \M \N \).

(d) By @thm-simultaneous-triangularization there is an invertible \( \P \in M_n(\nC) \) with \( \U = \P^{-1}\N\P \) and \( \U' = \P^{-1}\M \P \) upper triangular. Since \( \N \) is nilpotent, \( \spec(\N) = \{0\} \) (@exr-eigenvalues-and-eigenvectors-c2), so every diagonal entry of \( \U \) is \( 0 \) by @thm-diagonal-of-triangular-form; likewise for \( \U' \). So \( \U + \U' = \P^{-1}(\N + \M)\P \) is upper triangular with zero diagonal. A matrix \( \X \) of this kind is nilpotent: \( \X\e_1 = \0 \) and \( \X\e_j \in \Span(\e_1, \dots, \e_{j-1}) \), so by induction \( \X^j\e_j = \0 \) and \( \X^n = 0 \). Hence \( (\N + \M)^n = \P(\U + \U')^n\P^{-1} = 0 \).
:::
