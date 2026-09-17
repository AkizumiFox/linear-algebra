# Rank and Block Matrices

Rank is the most robust number attached to a matrix, and Chapters 2 and 3 found several inequalities for it: the rank of a product is at most the rank of each factor, and Sylvester's inequality bounds it from below. Those proofs worked with subspaces. This section proves rank inequalities by a different and very mechanical method. We place the matrices we care about as blocks of one bigger matrix, and then change that matrix by block row and column operations, which never change the rank, until its rank can be read off. The method gives short proofs of the Frobenius inequality and of identities such as \( \rank(I_m - AB) + n = \rank(I_n - BA) + m \), which are awkward to reach with subspaces alone.

## Three basic inequalities

We start with what the shape of a block matrix alone says about its rank. Write \( \begin{pmatrix} A & B \end{pmatrix} \) for the matrix obtained by placing \( B \) to the right of \( A \) (same number of rows), and \( \begin{pmatrix} A \\ C \end{pmatrix} \) for \( C \) below \( A \) (same number of columns). In these results the blocks need **not** be square.

::: {#thm-block-rank-inequalities}
[Rank Inequalities for Block Matrices]

Let \( A \in M_{m \times k}(F) \), \( B \in M_{m \times l}(F) \), \( C \in M_{p \times k}(F) \) and \( D \in M_{p \times l}(F) \).

::: {.enumerate options="label=(\alph*)"}
1. \( \max(\rank A, \rank B) \le \rank\begin{pmatrix} A & B \end{pmatrix} \le \rank A + \rank B \), and likewise \( \max(\rank A, \rank C) \le \rank\begin{pmatrix} A \\ C \end{pmatrix} \le \rank A + \rank C \).
2. \( \rank\begin{pmatrix} A & 0 \\ 0 & D \end{pmatrix} = \rank A + \rank D \).
3. \( \rank\begin{pmatrix} A & B \\ 0 & D \end{pmatrix} \ge \rank A + \rank D \) and \( \rank\begin{pmatrix} A & 0 \\ C & D \end{pmatrix} \ge \rank A + \rank D \).
:::
:::

::: {.idea}
Rank is the dimension of the column space, so look at columns. In (a) the columns of \( \begin{pmatrix} A & B \end{pmatrix} \) are those of \( A \) together with those of \( B \), and dimensions of sums are at most sums of dimensions. In (b) the columns coming from \( A \) and from \( D \) live in two subspaces that meet only in \( \0 \). In (c) we cannot use the column space of \( B \), which is unknown, so instead we pick independent columns of \( A \) and of \( D \) and show that the columns of the big matrix standing above them are still independent: the zero block lets us peel off the \( D \)-part first.
:::

::: {.proof}
For \( \y \in F^m \) and \( \z \in F^p \), write \( \begin{pmatrix} \y \\ \z \end{pmatrix} \in F^{m+p} \) for the stacked vector.

(a) The columns of \( \begin{pmatrix} A & B \end{pmatrix} \) are the columns of \( A \) followed by the columns of \( B \), so its column space is \( \col(A) + \col(B) \) by @prp-sum-of-spans. It contains \( \col(A) \) and \( \col(B) \), which gives the lower bound by @thm-subspace-dimension, and by @thm-dimension-formula-subspace-dim
\[
\rank\begin{pmatrix} A & B \end{pmatrix} = \rank A + \rank B - \dim(\col A \cap \col B) \le \rank A + \rank B .
\]
For the stacked matrix, @prp-block-transpose gives \( \begin{pmatrix} A \\ C \end{pmatrix}\tp = \begin{pmatrix} A\tp & C\tp \end{pmatrix} \), and a matrix and its transpose have the same rank (@thm-row-rank-equals-column-rank). Apply the first part to \( A\tp \) and \( C\tp \).

(b) Let \( M = \begin{pmatrix} A & 0 \\ 0 & D \end{pmatrix} \). Its first \( k \) columns are \( \begin{pmatrix} \a_j \\ \0 \end{pmatrix} \) and its last \( l \) columns are \( \begin{pmatrix} \0 \\ \d_q \end{pmatrix} \), where \( \a_j \), \( \d_q \) are the columns of \( A \), \( D \). So \( \col(M) = Y + Z \) with \( Y = \{ \begin{pmatrix} \y \\ \0 \end{pmatrix} : \y \in \col A \} \) and \( Z = \{ \begin{pmatrix} \0 \\ \z \end{pmatrix} : \z \in \col D \} \). A vector in \( Y \cap Z \) has both parts zero, so \( Y \cap Z = \{\0\} \). The map \( \y \mapsto \begin{pmatrix} \y \\ \0 \end{pmatrix} \) is linear and injective from \( \col A \) onto \( Y \), so \( \dim Y = \rank A \) (@thm-isomorphic-iff-same-dimension); likewise \( \dim Z = \rank D \). By @thm-dimension-formula-subspace-dim, \( \rank M = \rank A + \rank D - 0 \).

(c) Let \( M = \begin{pmatrix} A & B \\ 0 & D \end{pmatrix} \), \( r = \rank A \) and \( s = \rank D \). By @thm-basis-column-space there are columns \( \a_{j_1}, \dots, \a_{j_r} \) of \( A \) that are linearly independent, and columns \( \d_{q_1}, \dots, \d_{q_s} \) of \( D \) that are linearly independent. The corresponding columns of \( M \) are \( \begin{pmatrix} \a_{j_i} \\ \0 \end{pmatrix} \) and \( \begin{pmatrix} \b_{q_i} \\ \d_{q_i} \end{pmatrix} \), where \( \b_q \) is column \( q \) of \( B \). Let
\[
\sum_{i=1}^{r} \alpha_i \begin{pmatrix} \a_{j_i} \\ \0 \end{pmatrix} + \sum_{i=1}^{s} \beta_i \begin{pmatrix} \b_{q_i} \\ \d_{q_i} \end{pmatrix} = \0 .
\]
The last \( p \) entries give \( \sum_i \beta_i\d_{q_i} = \0 \), so all \( \beta_i = 0 \). The first \( m \) entries then give \( \sum_i \alpha_i\a_{j_i} = \0 \), so all \( \alpha_i = 0 \). Hence \( \col(M) \) contains \( r + s \) linearly independent vectors, and \( \rank M \ge r + s \) by @thm-size-bounds. For the lower triangular shape, \( \begin{pmatrix} A & 0 \\ C & D \end{pmatrix}\tp = \begin{pmatrix} A\tp & C\tp \\ 0 & D\tp \end{pmatrix} \) by @prp-block-transpose; apply the first case and @thm-row-rank-equals-column-rank.
:::

All three inequalities, the two in (a) and the one in (c), can be strict, and small witnesses show it. For \( A = B = (1) \), \( \rank\begin{pmatrix} 1 & 1 \end{pmatrix} = 1 < 2 \): the two column spaces overlap. For \( A = \e_1 \) and \( B = \e_2 \) in \( F^2 \), \( \rank\begin{pmatrix} \e_1 & \e_2 \end{pmatrix} = \rank I_2 = 2 > \max(1, 1) \): each block adds something the other lacks. For \( A = D = (0) \) and \( B = (1) \), \( \rank\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = 1 > 0 + 0 \): the off-diagonal block contributes rank of its own. The proof of (a) says exactly when the upper bound is attained: \( \rank\begin{pmatrix} A & B \end{pmatrix} = \rank A + \rank B \) if and only if \( \col A \cap \col B = \{\0\} \).

::: {.warning}
**The ranks of the four blocks do not determine the rank of the whole.** Over \( \nQ \), \( \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \) and \( \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \) have all four \( 1 \times 1 \) blocks of rank \( 1 \), but ranks \( 1 \) and \( 2 \). Only special shapes, like the zero blocks in (b) and (c), turn block ranks into information about the whole matrix.
:::

::: {.check}
Without computing, find \( \rank\begin{pmatrix} 1 & 2 & 0 & 0 & 0 \\ 2 & 4 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 3 \\ 0 & 0 & 0 & 1 & 5 \end{pmatrix} \).
:::

::: {.solution}
With row partition \( 2, 2 \) and column partition \( 2, 3 \), the matrix is \( \begin{pmatrix} A & 0 \\ 0 & D \end{pmatrix} \) with \( A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} \) of rank \( 1 \) (the second row is twice the first) and \( D = \begin{pmatrix} 1 & 0 & 3 \\ 0 & 1 & 5 \end{pmatrix} \) of rank \( 2 \) (the first two columns are \( \e_1, \e_2 \)). By @thm-block-rank-inequalities (b), the rank is \( 1 + 2 = 3 \).
:::

## Block elimination

Gaussian elimination changes a matrix by row operations, which are multiplications by invertible matrices on the left, and the rank never changes. The same is true when the "rows" are whole block rows and the multipliers are matrices. The matrices that do this are the block triangular matrices with identity blocks on the diagonal from @thm-block-triangular-inverse, together with block swaps.

Fix a partition of \( M = \begin{pmatrix} A & B \\ C & D \end{pmatrix} \in M_{(m+p) \times (k+l)}(F) \) with \( A \in M_{m \times k}(F) \). For matrices \( X \in M_{m \times p}(F) \) and \( Y \in M_{k \times l}(F) \), @thm-block-multiplication gives
\[
\begin{pmatrix} I_m & X \\ 0 & I_p \end{pmatrix}\begin{pmatrix} A & B \\ C & D \end{pmatrix} = \begin{pmatrix} A + XC & B + XD \\ C & D \end{pmatrix}, \qquad
\begin{pmatrix} A & B \\ C & D \end{pmatrix}\begin{pmatrix} I_k & Y \\ 0 & I_l \end{pmatrix} = \begin{pmatrix} A & AY + B \\ C & CY + D \end{pmatrix}.
\]
In words: multiplying on the **left** adds \( X \) times block row \( 2 \) to block row \( 1 \), with \( X \) on the left of the row; multiplying on the **right** adds block column \( 1 \) times \( Y \) to block column \( 2 \), with \( Y \) on the right of the column. The lower triangular multipliers \( \begin{pmatrix} I_m & 0 \\ X' & I_p \end{pmatrix} \) and \( \begin{pmatrix} I_k & 0 \\ Y' & I_l \end{pmatrix} \) act the same way in the other direction. Sides matter: the multiplier sits on the side of the product where the matrix operation happens.

::: {#thm-block-elimination-rank}
[Block Elimination Preserves Rank]

Let \( M = \begin{pmatrix} A & B \\ C & D \end{pmatrix} \) be as above.

::: {.enumerate options="label=(\alph*)"}
1. For all \( X \in M_{m \times p}(F) \), \( X' \in M_{p \times m}(F) \), \( Y \in M_{k \times l}(F) \) and \( Y' \in M_{l \times k}(F) \), the matrices
\[
\begin{pmatrix} I_m & X \\ 0 & I_p \end{pmatrix}, \quad \begin{pmatrix} I_m & 0 \\ X' & I_p \end{pmatrix}, \quad \begin{pmatrix} I_k & Y \\ 0 & I_l \end{pmatrix}, \quad \begin{pmatrix} I_k & 0 \\ Y' & I_l \end{pmatrix}
\]
are invertible, and so are the block swaps \( \begin{pmatrix} 0 & I_p \\ I_m & 0 \end{pmatrix} \in M_{m+p}(F) \) and \( \begin{pmatrix} 0 & I_k \\ I_l & 0 \end{pmatrix} \in M_{k+l}(F) \). Hence multiplying \( M \) on the left or right by any product of such matrices does not change its rank. The swaps give \( \begin{pmatrix} 0 & I_p \\ I_m & 0 \end{pmatrix}M = \begin{pmatrix} C & D \\ A & B \end{pmatrix} \) and \( M\begin{pmatrix} 0 & I_k \\ I_l & 0 \end{pmatrix} = \begin{pmatrix} B & A \\ D & C \end{pmatrix} \).
2. If \( \col(B) \subseteq \col(A) \), or if \( \row(B) \subseteq \row(D) \), then \( \rank\begin{pmatrix} A & B \\ 0 & D \end{pmatrix} = \rank A + \rank D \).
:::
:::

::: {.proof}
(a) By @thm-block-triangular-inverse (c), with identity blocks on the diagonal, \( \begin{pmatrix} I_m & X \\ 0 & I_p \end{pmatrix} \) has inverse \( \begin{pmatrix} I_m & -X \\ 0 & I_p \end{pmatrix} \); the lower triangular case follows by transposing (@prp-block-transpose, @thm-inverse-matrix-properties). In the swap \( S = \begin{pmatrix} 0 & I_p \\ I_m & 0 \end{pmatrix} \) the row partition is \( p, m \) and the column partition is \( m, p \). Let \( S' = \begin{pmatrix} 0 & I_m \\ I_p & 0 \end{pmatrix} \), with row partition \( m, p \) and column partition \( p, m \). These are conformable, and @thm-block-multiplication gives \( S'S = \begin{pmatrix} I_m & 0 \\ 0 & I_p \end{pmatrix} = I_{m+p} \), so \( S \) is invertible by @thm-one-sided-inverse; the other swap is the same with \( k, l \) in place of \( m, p \). The two displayed products are @thm-block-multiplication. Rank is unchanged by invertible factors on either side (@thm-rank-product-inequality).

(b) Suppose \( \col(B) \subseteq \col(A) \). Each column \( \b_q \) of \( B \) is then \( A\y_q \) for some \( \y_q \in F^k \) (@def-column-space, @thm-matrix-times-vector-columns). Let \( Y \in M_{k \times l}(F) \) have columns \( \y_q \), so that \( AY = B \) by @thm-three-views-of-product. By the computation before the theorem,
\[
\begin{pmatrix} A & B \\ 0 & D \end{pmatrix}\begin{pmatrix} I_k & -Y \\ 0 & I_l \end{pmatrix} = \begin{pmatrix} A & -AY + B \\ 0 & D \end{pmatrix} = \begin{pmatrix} A & 0 \\ 0 & D \end{pmatrix},
\]
and (a) together with @thm-block-rank-inequalities (b) gives the claim. If \( \row(B) \subseteq \row(D) \), the same argument applied to rows gives \( B = XD \) for some \( X \in M_{m \times p}(F) \), and \( \begin{pmatrix} I_m & -X \\ 0 & I_p \end{pmatrix}\begin{pmatrix} A & B \\ 0 & D \end{pmatrix} = \begin{pmatrix} A & 0 \\ 0 & D \end{pmatrix} \).
:::

Part (b) is the typical use of (a): a block that is a multiple of a neighboring block can be cleared, exactly as an entry below a pivot is cleared in Gaussian elimination. The zero block of @thm-block-rank-inequalities (c) is what lets the cleared matrix fall apart into a direct sum.

## Frobenius's inequality by blocks

Recall Sylvester's rank inequality (@thm-sylvester-rank-inequality): for \( A \in M_{m \times n}(F) \) and \( B \in M_{n \times p}(F) \), \( \rank(AB) \ge \rank A + \rank B - n \). In @exr-rank-factorization-c1 we met a stronger statement, Frobenius's inequality, and proved it by comparing intersections of subspaces with a null space. Here is a proof in which nothing is chosen: we write down one block matrix whose rank we know, and eliminate.

::: {#thm-frobenius-rank-block-proof}
[Frobenius's Rank Inequality]

Let \( A \in M_{m \times n}(F) \), \( B \in M_{n \times p}(F) \) and \( C \in M_{p \times q}(F) \). Then
\[
\rank(ABC) + \rank B \ge \rank(AB) + \rank(BC) .
\]
:::

::: {.idea}
The left side is the rank of \( \begin{pmatrix} ABC & 0 \\ 0 & B \end{pmatrix} \), by @thm-block-rank-inequalities (b). The right side is a lower bound for any block triangular matrix with diagonal blocks \( AB \) and \( BC \), by part (c). So we want to turn the first matrix into the second by block elimination. Found backwards: \( A \) times the second block row puts \( AB \) into the top-right corner; then the second block column times \( C \) cancels \( ABC \) and puts \( BC \) into the bottom-left corner. A swap of the two block columns finishes the job.
:::

::: {.proof}
Let \( P = \begin{pmatrix} ABC & 0 \\ 0 & B \end{pmatrix} \), with row partition \( m, n \) and column partition \( q, p \). By @thm-block-rank-inequalities (b), \( \rank P = \rank(ABC) + \rank B \). By @thm-block-multiplication,
\[
\begin{pmatrix} I_m & A \\ 0 & I_n \end{pmatrix} P = \begin{pmatrix} ABC & AB \\ 0 & B \end{pmatrix}, \qquad
\begin{pmatrix} ABC & AB \\ 0 & B \end{pmatrix}\begin{pmatrix} I_q & 0 \\ -C & I_p \end{pmatrix} = \begin{pmatrix} ABC - ABC & AB \\ -BC & B \end{pmatrix} = \begin{pmatrix} 0 & AB \\ -BC & B \end{pmatrix}.
\]
Multiplying on the right by the block swap \( \begin{pmatrix} 0 & I_q \\ I_p & 0 \end{pmatrix} \) exchanges the two block columns and gives \( Q = \begin{pmatrix} AB & 0 \\ B & -BC \end{pmatrix} \). By @thm-block-elimination-rank (a), \( \rank Q = \rank P \). By @thm-block-rank-inequalities (c), \( \rank Q \ge \rank(AB) + \rank(-BC) = \rank(AB) + \rank(BC) \), where \( \rank(-BC) = \rank(BC) \) because \( -BC \) and \( BC \) have the same column space. Hence \( \rank(ABC) + \rank B \ge \rank(AB) + \rank(BC) \).
:::

Taking \( B = I_n \) gives \( \rank(AC) + n \ge \rank A + \rank C \) for \( A \in M_{m \times n}(F) \) and \( C \in M_{n \times q}(F) \), which is Sylvester's inequality again. Taking \( A = I_n \) or \( C = I_p \) gives an equality and no information, as it should. The inequality says that multiplying by \( A \) on the left loses at least as much rank from \( BC \) as from \( B \): the rank lost is \( \rank(BC) - \rank(ABC) \le \rank B - \rank(AB) \). A smaller column space has less to lose.

## A worked example: \( I - AB \) and \( I - BA \)

Products in the two orders, \( AB \) and \( BA \), are different matrices of possibly different sizes, and Chapter 3 showed that even their ranks can differ. Yet \( I - AB \) and \( I - BA \) are tightly linked. The block matrix that links them contains \( I_m \), \( A \), \( B \) and \( I_n \), and each identity block can be used as a pivot to clear its neighbors.

::: {#exm-rank-i-minus-ab}
[Rank of \( I - AB \) versus \( I - BA \)]

Let \( A \in M_{m \times n}(F) \) and \( B \in M_{n \times m}(F) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \rank(I_m - AB) + n = \rank(I_n - BA) + m \).
2. Deduce that for \( m = n \), \( \rank(I_n - AB) = \rank(I_n - BA) \), and \( I_n - AB \) is invertible if and only if \( I_n - BA \) is.
3. Check (a) for \( A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix} \) and \( B = \begin{pmatrix} 1 & 0 \\ 0 & 0 \\ 0 & 1 \end{pmatrix} \) over \( \nQ \).
:::
:::

::: {.solution}
(a) Let \( M = \begin{pmatrix} I_m & A \\ B & I_n \end{pmatrix} \in M_{m+n}(F) \), with partition \( m, n \) for rows and columns. We eliminate in two different ways.

*Using \( I_m \) as the pivot.* Subtract \( B \) times block row \( 1 \) from block row \( 2 \), then subtract block column \( 1 \) times \( A \) from block column \( 2 \). By @thm-block-multiplication,
\[
\begin{pmatrix} I_m & 0 \\ -B & I_n \end{pmatrix} M = \begin{pmatrix} I_m & A \\ 0 & I_n - BA \end{pmatrix}, \qquad
\begin{pmatrix} I_m & A \\ 0 & I_n - BA \end{pmatrix}\begin{pmatrix} I_m & -A \\ 0 & I_n \end{pmatrix} = \begin{pmatrix} I_m & 0 \\ 0 & I_n - BA \end{pmatrix}.
\]
By @thm-block-elimination-rank (a) and @thm-block-rank-inequalities (b), \( \rank M = m + \rank(I_n - BA) \).

*Using \( I_n \) as the pivot.* Subtract \( A \) times block row \( 2 \) from block row \( 1 \), then subtract block column \( 2 \) times \( B \) from block column \( 1 \):
\[
\begin{pmatrix} I_m & -A \\ 0 & I_n \end{pmatrix} M = \begin{pmatrix} I_m - AB & 0 \\ B & I_n \end{pmatrix}, \qquad
\begin{pmatrix} I_m - AB & 0 \\ B & I_n \end{pmatrix}\begin{pmatrix} I_m & 0 \\ -B & I_n \end{pmatrix} = \begin{pmatrix} I_m - AB & 0 \\ 0 & I_n \end{pmatrix}.
\]
So \( \rank M = \rank(I_m - AB) + n \) in the same way. Comparing the two expressions for \( \rank M \) proves (a).

(b) For \( m = n \) the two added terms are equal and cancel. A square matrix is invertible exactly when its rank is \( n \) (@thm-invertible-tfae), so \( I_n - AB \) is invertible if and only if \( I_n - BA \) is.

(c) Here \( AB = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_2 \), so \( \rank(I_2 - AB) = 0 \), and
\[
BA = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 1 & 1 \end{pmatrix}, \qquad I_3 - BA = \begin{pmatrix} 0 & -1 & 0 \\ 0 & 1 & 0 \\ 0 & -1 & 0 \end{pmatrix},
\]
which has rank \( 1 \). Indeed \( 0 + 3 = 1 + 2 \). So \( AB = I_2 \) while \( BA \ne I_3 \), and the identity accounts for the difference exactly: \( I_3 - BA \) has rank \( 3 - 2 = 1 \).
:::

The trick is worth naming. **To compare two expressions, find one block matrix from which both can be obtained by elimination, and compute its rank twice.** Section 3 does the same with determinants and inverses, and the pair \( I - AB \), \( I - BA \) returns there as Sylvester's determinant identity.

## Exercises

### A. Check your understanding

:::: {#exr-rank-of-block-matrices-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the three inequalities of @thm-block-rank-inequalities.
2. True or false: \( \rank\begin{pmatrix} A & B \\ 0 & D \end{pmatrix} = \rank A + \rank D \) for all blocks of compatible sizes. Justify your answer.
3. Which matrix do you multiply \( \begin{pmatrix} A & B \\ C & D \end{pmatrix} \) by, and on which side, to replace \( C \) by \( C - XA \)?
4. True or false: \( \rank\begin{pmatrix} A & B \end{pmatrix} = \rank A + \rank B \) whenever \( A \) and \( B \) have the same number of rows. Justify your answer.
5. State Frobenius's inequality, and explain how Sylvester's inequality follows from it.
:::
::::

::: {.solution}
(a) \( \max(\rank A, \rank B) \le \rank\begin{pmatrix} A & B \end{pmatrix} \le \rank A + \rank B \) (and the same for stacked blocks); \( \rank\begin{pmatrix} A & 0 \\ 0 & D \end{pmatrix} = \rank A + \rank D \); and both block triangular shapes have rank at least \( \rank A + \rank D \).

(b) False. \( \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) with \( 1 \times 1 \) blocks has rank \( 1 \), but \( \rank(0) + \rank(0) = 0 \). Only \( \ge \) holds in general.

(c) Multiply on the left by \( \begin{pmatrix} I & 0 \\ -X & I \end{pmatrix} \): block row \( 2 \) becomes \( \begin{pmatrix} C - XA & D - XB \end{pmatrix} \) by @thm-block-multiplication. The rank does not change (@thm-block-elimination-rank).

(d) False. \( \begin{pmatrix} 1 & 1 \end{pmatrix} \) has rank \( 1 \), not \( 1 + 1 \). Equality holds exactly when \( \col A \cap \col B = \{\0\} \).

(e) \( \rank(ABC) + \rank B \ge \rank(AB) + \rank(BC) \) for matrices of compatible sizes. With \( B = I_n \) it reads \( \rank(AC) + n \ge \rank A + \rank C \), which is Sylvester's inequality.
:::

### B. Practice

:::: {#exr-rank-of-block-matrices-b1}
[B1: Ranks of block matrices]

Let \( A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} \) and \( D = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) in \( M_2(\nQ) \). Find the rank of each \( 4 \times 4 \) matrix, citing the result you use. In which case is the lower bound of @thm-block-rank-inequalities (c) strict?

::: {.enumerate options="label=(\alph*)"}
1. \( M_1 = \begin{pmatrix} A & 0 \\ 0 & D \end{pmatrix} \).
2. \( M_2 = \begin{pmatrix} A & B \\ 0 & D \end{pmatrix} \) with \( B = \begin{pmatrix} 1 & 3 \\ 2 & 6 \end{pmatrix} \).
3. \( M_3 = \begin{pmatrix} A & I_2 \\ 0 & 0 \end{pmatrix} \).
:::
::::

::: {.solution}
\( \rank A = 1 \), since the second row is twice the first and \( A \ne 0 \); \( \rank D = 2 \), since \( \det D = 1 \ne 0 \).

(a) By @thm-block-rank-inequalities (b), \( \rank M_1 = 1 + 2 = 3 \).

(b) The columns of \( B \) are \( (1, 2) \) and \( (3, 6) = 3(1, 2) \), and \( (1, 2) \) is the first column of \( A \). So \( \col B \subseteq \col A \), and by @thm-block-elimination-rank (b), \( \rank M_2 = 1 + 2 = 3 \). (Explicitly \( B = AY \) with \( Y = \begin{pmatrix} 1 & 3 \\ 0 & 0 \end{pmatrix} \).)

(c) The lower bound is \( \rank A + \rank 0 = 1 \). But the last two columns of \( M_3 \) are \( \e_1, \e_2 \), and every column lies in \( \Span(\e_1, \e_2) \), so \( \rank M_3 = 2 \). This is the strict case: the block \( I_2 \) is not a multiple of \( A \) or of the zero block.
:::

:::: {#exr-rank-of-block-matrices-b2}
[B2: Shifted products]

Let \( A \in M_{m \times n}(F) \), \( B \in M_{n \times m}(F) \) and \( c \in F \) with \( c \ne 0 \).

::: {.enumerate options="label=(\alph*)"}
1. By adapting @exm-rank-i-minus-ab, prove that \( \rank(cI_m - AB) + n = \rank(cI_n - BA) + m \).
2. Check (a) over \( \nQ \) for \( c = 2 \), \( A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \\ 1 & 0 \end{pmatrix} \) and \( B = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix} \).
3. Show by an example with \( m = 1 \), \( n = 2 \) that (a) can fail for \( c = 0 \).
:::
::::

::: {.solution}
(a) Since \( c \ne 0 \), put \( A' = c^{-1}A \). Then \( cI_m - AB = c(I_m - A'B) \) and \( cI_n - BA = c(I_n - BA') \). Multiplying a matrix by the non-zero scalar \( c \) does not change its column space, hence not its rank. By @exm-rank-i-minus-ab (a) applied to \( A' \) and \( B \),
\[
\rank(cI_m - AB) + n = \rank(I_m - A'B) + n = \rank(I_n - BA') + m = \rank(cI_n - BA) + m .
\]

(b) Here \( m = 3 \), \( n = 2 \), and
\[
2I_3 - AB = \begin{pmatrix} 1 & -1 & -1 \\ 0 & 1 & 0 \\ -1 & 0 & 1 \end{pmatrix}, \qquad 2I_2 - BA = \begin{pmatrix} 0 & -1 \\ 0 & 1 \end{pmatrix},
\]
since \( AB = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix} \) and \( BA = \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix} \). In the first matrix, row \( 1 \) equals \( -(\text{row } 2) - (\text{row } 3) \), and rows \( 2 \) and \( 3 \) are not multiples of each other, so its rank is \( 2 \) (@thm-row-rank-equals-column-rank). The second has rank \( 1 \). Indeed \( 2 + 2 = 1 + 3 \).

(c) For \( c = 0 \) the identity would say \( \rank(AB) + n = \rank(BA) + m \). Take \( A = \begin{pmatrix} 1 & 0 \end{pmatrix} \) and \( B = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \): \( AB = (1) \) has rank \( 1 \), and \( BA = E_{11} \in M_2(F) \) has rank \( 1 \), but \( 1 + 2 \ne 1 + 1 \).
:::

:::: {#exr-rank-of-block-matrices-b3}
[B3: Idempotents by blocks]

Let \( A \in M_n(F) \).

::: {.enumerate options="label=(\alph*)"}
1. Starting from \( \begin{pmatrix} A & 0 \\ 0 & I_n - A \end{pmatrix} \), use block elimination to prove
\[
\rank A + \rank(I_n - A) = n + \rank(A - A^2) .
\]
2. Deduce that \( A^2 = A \) if and only if \( \rank A + \rank(I_n - A) = n \).
3. Compare (b) with what Chapter 3 says about projections.
:::

*Hint: first add block row 1 to block row 2, then add block column 2 to block column 1.*
::::

::: {.solution}
(a) Write \( I = I_n \). By @thm-block-multiplication, each step being multiplication by one of the matrices of @thm-block-elimination-rank (a):
\[
\begin{pmatrix} A & 0 \\ 0 & I - A \end{pmatrix}
\xrightarrow{\ \text{row}_2 + \text{row}_1\ }
\begin{pmatrix} A & 0 \\ A & I - A \end{pmatrix}
\xrightarrow{\ \text{col}_1 + \text{col}_2\ }
\begin{pmatrix} A & 0 \\ I & I - A \end{pmatrix}
\xrightarrow{\ \text{row}_1 - A\,\text{row}_2\ }
\begin{pmatrix} 0 & A^2 - A \\ I & I - A \end{pmatrix}
\xrightarrow{\ \text{col}_2 - \text{col}_1(I - A)\ }
\begin{pmatrix} 0 & A^2 - A \\ I & 0 \end{pmatrix}.
\]
The multipliers are, in order, \( \begin{pmatrix} I & 0 \\ I & I \end{pmatrix} \) on the left, \( \begin{pmatrix} I & 0 \\ I & I \end{pmatrix} \) on the right, \( \begin{pmatrix} I & -A \\ 0 & I \end{pmatrix} \) on the left and \( \begin{pmatrix} I & -(I - A) \\ 0 & I \end{pmatrix} \) on the right. In the third step the top row becomes \( \begin{pmatrix} A - AI & 0 - A(I - A) \end{pmatrix} = \begin{pmatrix} 0 & A^2 - A \end{pmatrix} \), and in the fourth the bottom-right block becomes \( (I - A) - I(I - A) = 0 \). Swapping the block columns (@thm-block-elimination-rank (a)) gives \( \begin{pmatrix} A^2 - A & 0 \\ 0 & I \end{pmatrix} \), of rank \( \rank(A^2 - A) + n \) by @thm-block-rank-inequalities (b). The first matrix has rank \( \rank A + \rank(I - A) \), and rank is unchanged throughout. Since \( A^2 - A = -(A - A^2) \) has the same rank as \( A - A^2 \), (a) follows.

(b) By (a), \( \rank A + \rank(I - A) = n \) if and only if \( \rank(A - A^2) = 0 \), that is, \( A - A^2 = 0 \).

(c) If \( A^2 = A \), then \( T_A \) is a projection (@def-projection-operator), so \( F^n = \im T_A \oplus \ker T_A \) by @thm-projection-direct-sum, with \( \ker T_A = \col(I - A) \) (a vector \( \v \) with \( A\v = \0 \) equals \( (I - A)\v \), and conversely \( A(I - A) = A - A^2 = 0 \)). So \( \rank A + \rank(I - A) = \dim\im T_A + \dim\ker T_A = n \), which is the forward direction of (b). The block argument also gives the converse, and it never mentions subspaces.
:::

### C. Going deeper

:::: {#exr-rank-of-block-matrices-c1}
[C1: The rank of \( A - ABA \)]

Let \( A \in M_{m \times n}(F) \) and \( B \in M_{n \times m}(F) \).

::: {.enumerate options="label=(\alph*)"}
1. Verify, by block multiplication, the following chain, in which each arrow is multiplication by an invertible block triangular matrix:
\[
\begin{pmatrix} A & 0 \\ 0 & I_n - BA \end{pmatrix} \to \begin{pmatrix} A & A \\ 0 & I_n - BA \end{pmatrix} \to \begin{pmatrix} A & A \\ BA & I_n \end{pmatrix} \to \begin{pmatrix} A - ABA & A \\ 0 & I_n \end{pmatrix} \to \begin{pmatrix} A - ABA & 0 \\ 0 & I_n \end{pmatrix}.
\]
Name each multiplier and the side it acts on.
2. Deduce that \( \rank(A - ABA) = \rank A + \rank(I_n - BA) - n \).
3. Suppose \( ABA = A \). Show that \( BA \) is idempotent and that \( \rank(BA) = \rank A \).
:::

*Hint for (c): use (b), then @exr-rank-of-block-matrices-b3.*
::::

::: {.solution}
(a) The partitions are \( m, n \) for rows and \( n, n \) for columns. By @thm-block-multiplication:

1. Right multiplication by \( \begin{pmatrix} I_n & I_n \\ 0 & I_n \end{pmatrix} \) adds block column \( 1 \) to block column \( 2 \): \( \begin{pmatrix} A & A + 0 \\ 0 & 0 + (I_n - BA) \end{pmatrix} \).
2. Left multiplication by \( \begin{pmatrix} I_m & 0 \\ B & I_n \end{pmatrix} \) adds \( B \) times block row \( 1 \) to block row \( 2 \): the new row is \( \begin{pmatrix} BA & BA + I_n - BA \end{pmatrix} = \begin{pmatrix} BA & I_n \end{pmatrix} \).
3. Right multiplication by \( \begin{pmatrix} I_n & 0 \\ -BA & I_n \end{pmatrix} \) subtracts block column \( 2 \) times \( BA \) from block column \( 1 \): the new column is \( \begin{pmatrix} A - ABA \\ BA - I_nBA \end{pmatrix} = \begin{pmatrix} A - ABA \\ 0 \end{pmatrix} \).
4. Left multiplication by \( \begin{pmatrix} I_m & -A \\ 0 & I_n \end{pmatrix} \) subtracts \( A \) times block row \( 2 \) from block row \( 1 \): the new row is \( \begin{pmatrix} A - ABA - A\cdot 0 & A - AI_n \end{pmatrix} = \begin{pmatrix} A - ABA & 0 \end{pmatrix} \).

All four multipliers are invertible by @thm-block-elimination-rank (a).

(b) By @thm-block-elimination-rank (a) the first and last matrices have the same rank, and by @thm-block-rank-inequalities (b) these ranks are \( \rank A + \rank(I_n - BA) \) and \( \rank(A - ABA) + n \). Rearranging gives the formula.

(c) \( (BA)^2 = B(ABA) = BA \), so \( BA \) is idempotent. By (b), \( 0 = \rank(A - ABA) = \rank A + \rank(I_n - BA) - n \), so \( \rank(I_n - BA) = n - \rank A \). By @exr-rank-of-block-matrices-b3 (b) applied to the idempotent \( BA \), \( \rank(BA) = n - \rank(I_n - BA) = \rank A \).
:::

:::: {#exr-rank-of-block-matrices-c2}
[C2: Involutions and the field]

Let \( A \in M_n(F) \).

::: {.enumerate options="label=(\alph*)"}
1. Suppose the characteristic of \( F \) is not \( 2 \). Starting from \( \begin{pmatrix} A - I_n & 0 \\ 0 & A + I_n \end{pmatrix} \), prove that
\[
\rank(A - I_n) + \rank(A + I_n) = n + \rank(A^2 - I_n) .
\]
2. Deduce that if \( A^2 = I_n \) (and \( \operatorname{char} F \ne 2 \)), then \( \rank(A - I_n) + \rank(A + I_n) = n \).
3. Show that (b) fails over \( \nF_2 \), and point to the step of (a) that breaks.
:::

*Hint for (a): add block column 2 to block column 1, and subtract block row 2 from block row 1; then \( -2I_n \) is an invertible pivot.*
::::

::: {.solution}
(a) Write \( I = I_n \) and \( P = A + I \). Since \( \operatorname{char} F \ne 2 \), \( 2 \ne 0 \) in \( F \), so \( \frac12 \) exists and \( -2I \) is invertible. By @thm-block-multiplication, with each multiplier from @thm-block-elimination-rank (a):
\[
\begin{pmatrix} A - I & 0 \\ 0 & P \end{pmatrix}
\xrightarrow{\ \text{col}_1 + \text{col}_2\ }
\begin{pmatrix} A - I & 0 \\ P & P \end{pmatrix}
\xrightarrow{\ \text{row}_1 - \text{row}_2\ }
\begin{pmatrix} -2I & -P \\ P & P \end{pmatrix}
\xrightarrow{\ \text{col}_2 - \text{col}_1 \cdot \frac12 P\ }
\begin{pmatrix} -2I & 0 \\ P & P - \frac12 P^2 \end{pmatrix}
\xrightarrow{\ \text{row}_2 + \frac12 P\,\text{row}_1\ }
\begin{pmatrix} -2I & 0 \\ 0 & P - \frac12 P^2 \end{pmatrix}.
\]
In the second step \( (A - I) - P = -2I \); in the third, \( -P - (-2I)\tfrac12 P = 0 \) and \( P - P\cdot\frac12 P = P - \frac12P^2 \); in the fourth, \( P + \frac12P(-2I) = 0 \). Finally
\[
P - \tfrac12P^2 = \tfrac12 P(2I - P) = \tfrac12(A + I)(I - A) = \tfrac12(I - A^2),
\]
where the product \( (A + I)(I - A) = I - A + A - A^2 \) expands by distributivity. The first matrix has rank \( \rank(A - I) + \rank(A + I) \) and the last has rank \( n + \rank(\tfrac12(I - A^2)) = n + \rank(A^2 - I) \) by @thm-block-rank-inequalities (b), non-zero scalar multiples having the same column space. Rank is unchanged throughout.

(b) If \( A^2 = I_n \), then \( \rank(A^2 - I_n) = 0 \).

(c) Over \( \nF_2 \), take \( A = I_n \). Then \( A^2 = I_n \), but \( A - I_n = 0 \) and \( A + I_n = 2I_n = 0 \), so the left side is \( 0 \ne n \). The step that breaks is the pivot: \( -2I_n = 0 \) is not invertible, and \( \frac12 \) does not exist. (Chapter 3's decomposition of an involution into \( \pm 1 \) parts, @thm-involution-decomposition, needs the same hypothesis.)
:::
