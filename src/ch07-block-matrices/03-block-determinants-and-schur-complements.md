# Schur Complements

Section 1 inverted block triangular matrices, and Section 2 cleared blocks without changing the rank. A general block matrix \( \begin{pmatrix} \A & \B \\ \C & \D \end{pmatrix} \) has no zero block to help, but when one diagonal block is invertible, a single step of block elimination creates one. What is left in the opposite corner is a new matrix, the Schur complement, and it carries everything that the invertible block does not: the determinant, the rank and the inverse of the whole matrix can all be read off from the block and its complement. This section introduces it, derives these formulas, uses the two complements of one matrix to prove the Sherman–Morrison–Woodbury formula, and ends with the determinant of a block matrix whose lower blocks commute, over every field.

## Eliminating a block

Suppose we must solve a linear system whose unknowns come in two groups, \( \x \in F^k \) and \( \y \in F^l \):
\[
\begin{pmatrix} \A & \B \\ \C & \D \end{pmatrix}\begin{pmatrix} \x \\ \y \end{pmatrix} = \begin{pmatrix} \f \\ \g \end{pmatrix}, \qquad\text{that is,}\qquad
\begin{aligned} \A\x + \B\y &= \f, \\ \C\x + \D\y &= \g, \end{aligned}
\]
with \( \A \in M_k(F) \) invertible. Do what we would do for two equations in two numbers: solve the first equation for \( \x \), and substitute. The first equation gives \( \x = \A^{-1}(\f - \B\y) \). Substituting into the second,
\[
\C \A^{-1}\f - \C \A^{-1}\B\y + \D\y = \g, \qquad\text{so}\qquad (\D - \C \A^{-1}\B)\,\y = \g - \C \A^{-1}\f .
\]
The unknown \( \x \) has disappeared, and \( \y \) solves a smaller system whose matrix is \( \D - \C \A^{-1}\B \). Once \( \y \) is known, \( \x = \A^{-1}(\f - \B\y) \). So the big system is solvable for every right-hand side exactly when the small matrix \( \D - \C \A^{-1}\B \) allows it, and this matrix will keep appearing.

For \( k = l = 1 \) we have met it before: \( d - cb/a = (ad - bc)/a \) is the determinant divided by the pivot \( a \), which is what Gaussian elimination leaves in the corner after clearing the entry \( c \).

*The Schur complement of an invertible block is what remains in the opposite corner after that block has been used to eliminate its row and column.*

::: {#def-schur-complement}
[Schur Complement]

Let \( \M = \begin{pmatrix} \A & \B \\ \C & \D \end{pmatrix} \in M_{(k+p) \times (k+l)}(F) \) be a block matrix with \( \A \in M_k(F) \), \( \B \in M_{k \times l}(F) \), \( \C \in M_{p \times k}(F) \) and \( \D \in M_{p \times l}(F) \), where \( k, p, l \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. If \( \A \) is **invertible**, the **Schur complement of \( \A \) in \( \M \)** is
\[
\M/\A \coloneqq \D - \C \A^{-1}\B \in M_{p \times l}(F) .
\]
2. Symmetrically, if \( \M = \begin{pmatrix} \A & \B \\ \C & \D \end{pmatrix} \) with \( \D \in M_l(F) \) **invertible**, \( \A \in M_{m \times k}(F) \), \( \B \in M_{m \times l}(F) \) and \( \C \in M_{l \times k}(F) \), the **Schur complement of \( \D \) in \( \M \)** is \( \M/\D \coloneqq \A - \B \D^{-1}\C \in M_{m \times k}(F) \).
:::
:::

In words, clause by clause. The block whose complement we take must be **square and invertible**, since its inverse appears in the formula; the other blocks may be rectangular. The complement has the size of the **opposite corner**: \( \M/\A \) has the shape of \( \D \), and \( \M/\D \) has the shape of \( \A \). In \( \C \A^{-1}\B \) the factors come in the only order the sizes allow: \( \C \) is \( p \times k \), \( \A^{-1} \) is \( k \times k \), \( \B \) is \( k \times l \). A way to remember it: go from the corner \( \D \) to \( \A \) along its row (\( \C \)), invert, and come back along its column (\( \B \)).

**Well-definedness.** \( \M/\A \) depends on \( \M \) and on the chosen partition, which says which corner is \( \A \). The inverse \( \A^{-1} \) is unique (@thm-inverse-matrix-properties), so there is no other choice to make.

**Examples.**

- **Scalars.** For \( \M = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \) with \( a \ne 0 \), \( \M/a = d - ca^{-1}b = (ad - bc)/a \). In particular \( a \cdot (\M/a) = \det \M \).
- **An identity corner.** If \( \A = \I_k \), then \( \M/\I_k = \D - \C \B \). No inversion is needed at all.
- **Block triangular.** If \( \C = 0 \), then \( \M/\A = \D \): nothing needs to be eliminated.
- **A \( 3 \times 3 \) example.** For \( \M = \left(\begin{array}{cc|c} 2 & 1 & 1 \\ 1 & 1 & 0 \\ \hline 3 & 1 & 4 \end{array}\right) \) over \( \nQ \), \( \A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \) has \( \A^{-1} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} \), and \( \C \A^{-1} = \begin{pmatrix} 3 & 1 \end{pmatrix}\A^{-1} = \begin{pmatrix} 2 & -1 \end{pmatrix} \), so \( \M/\A = 4 - \begin{pmatrix} 2 & -1 \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = (2) \). This \( 1 \times 1 \) complement is the last pivot of Gaussian elimination on \( \M \): subtracting \( \frac12 \) row \( 1 \) from row \( 2 \) and \( \frac32 \) row \( 1 \) from row \( 3 \) gives the rows \( (0, \frac12, -\frac12) \) and \( (0, -\frac12, \frac52) \), and adding the first of these to the second gives \( (0, 0, 2) \).

**Non-example by minimal change.** For \( \M = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} \), \( \M/(1) = 0 - 1 \cdot 1 \cdot 1 = (-1) \). Change the corner entry \( 1 \) to \( 0 \): \( \M' = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \). The blocks \( \B \), \( \C \), \( \D \) and the partition are unchanged, and \( \M' \) is still invertible, but \( \M'/(0) \) is **not defined**, because the clause "\( \A \) is invertible" fails. Here \( \M'/\D \) is not defined either, since \( \D = (0) \).

**Why this definition.** The formula is read off from the elimination in the hook, so the question is only about the name and the hypotheses. "Complement" refers to position: \( \M/\A \) sits in the corner complementary to \( \A \). The quotient notation \( \M/\A \) is suggested by the first example, \( \det(\M/a) = \det \M / \det a \), and the determinant formula below shows that this holds for blocks of every size. Invertibility of \( \A \) cannot be dropped, since \( \A^{-1} \) is in the formula; the price is that some invertible matrices, like \( \M' \), have no Schur complement for a given partition.

::: {.warning}
**\( \M \) can be invertible while \( \A \) is not.** For \( \M' = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \), neither corner is invertible, so neither Schur complement exists for the partition \( 1, 1 \). Before using a formula below, check that the block you invert is invertible. If it is not, try the other corner (\( \M/\D \)), a different partition, or first permute rows: \( \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\M' = \I_2 \). The same issue appears in Gaussian elimination as a zero pivot.
:::

::: {.check}
Let \( \M = \left(\begin{array}{c|cc} 2 & 4 & 2 \\ \hline 1 & 3 & 5 \\ 3 & 1 & 0 \end{array}\right) \) with partition \( 1, 2 \). Compute \( \M/(2) \).
:::

::: {.solution}
Here \( \A = (2) \), \( \B = \begin{pmatrix} 4 & 2 \end{pmatrix} \), \( \C = \begin{pmatrix} 1 \\ 3 \end{pmatrix} \), \( \D = \begin{pmatrix} 3 & 5 \\ 1 & 0 \end{pmatrix} \). Then \( \C \A^{-1}\B = \frac12\begin{pmatrix} 4 & 2 \\ 12 & 6 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 6 & 3 \end{pmatrix} \), so \( \M/(2) = \begin{pmatrix} 1 & 4 \\ -5 & -3 \end{pmatrix} \). These are exactly the entries left in rows \( 2 \), \( 3 \) after clearing column \( 1 \) with the pivot \( 2 \).
:::

## The block LDU factorization

The elimination of the hook, written with matrices, factors \( \M \) into a lower block triangular matrix, a block diagonal matrix and an upper block triangular matrix. Everything else in this section follows from this factorization.

::: {#thm-block-ldu}
[Block LDU Factorization]

Let \( \M = \begin{pmatrix} \A & \B \\ \C & \D \end{pmatrix} \) be partitioned as in @def-schur-complement.

::: {.enumerate options="label=(\alph*)"}
1. If \( \A \in M_k(F) \) is invertible, then
\[
\M = \begin{pmatrix} \I_k & 0 \\ \C \A^{-1} & \I_p \end{pmatrix}\begin{pmatrix} \A & 0 \\ 0 & \M/\A \end{pmatrix}\begin{pmatrix} \I_k & \A^{-1}\B \\ 0 & \I_l \end{pmatrix}.
\]
2. If \( \D \in M_l(F) \) is invertible, then
\[
\M = \begin{pmatrix} \I_m & \B \D^{-1} \\ 0 & \I_l \end{pmatrix}\begin{pmatrix} \M/\D & 0 \\ 0 & \D \end{pmatrix}\begin{pmatrix} \I_k & 0 \\ \D^{-1}\C & \I_l \end{pmatrix}.
\]
:::
:::

::: {.idea}
The left factor in (a) records the row operation "subtract \( \C \A^{-1} \) times block row \( 1 \) from block row \( 2 \)", which turns \( \C \) into \( 0 \) and \( \D \) into \( \M/\A \). The right factor records the column operation "subtract block column \( 1 \) times \( \A^{-1}\B \) from block column \( 2 \)", which turns \( \B \) into \( 0 \). Undoing both operations gives the factorization. To prove it we need not retrace the elimination: multiplying out is enough.
:::

::: {.proof}
(a) Write \( \S = \M/\A = \D - \C \A^{-1}\B \). The sizes are conformable throughout. By @thm-block-multiplication,
\[
\begin{pmatrix} \A & 0 \\ 0 & \S \end{pmatrix}\begin{pmatrix} \I_k & \A^{-1}\B \\ 0 & \I_l \end{pmatrix} = \begin{pmatrix} \A & \A \A^{-1}\B \\ 0 & \S \end{pmatrix} = \begin{pmatrix} \A & \B \\ 0 & \S \end{pmatrix},
\]
and then
\[
\begin{pmatrix} \I_k & 0 \\ \C \A^{-1} & \I_p \end{pmatrix}\begin{pmatrix} \A & \B \\ 0 & \S \end{pmatrix} = \begin{pmatrix} \A & \B \\ \C \A^{-1}\A & \C \A^{-1}\B + \S \end{pmatrix} = \begin{pmatrix} \A & \B \\ \C & \D \end{pmatrix},
\]
since \( \C \A^{-1}\A = \C \) and \( \C \A^{-1}\B + (\D - \C \A^{-1}\B) = \D \). By associativity (@thm-matrix-multiplication-properties) the triple product equals \( \M \).

(b) Write \( \S' = \M/\D = \A - \B \D^{-1}\C \). By @thm-block-multiplication,
\[
\begin{aligned}
\begin{pmatrix} \S' & 0 \\ 0 & \D \end{pmatrix}\begin{pmatrix} \I_k & 0 \\ \D^{-1}\C & \I_l \end{pmatrix}
  &= \begin{pmatrix} \S' & 0 \\ \C & \D \end{pmatrix}, \\
\begin{pmatrix} \I_m & \B \D^{-1} \\ 0 & \I_l \end{pmatrix}\begin{pmatrix} \S' & 0 \\ \C & \D \end{pmatrix}
  &= \begin{pmatrix} \S' + \B \D^{-1}\C & \B \D^{-1}\D \\ \C & \D \end{pmatrix} = \M .
\end{aligned}
\]
:::

The outer factors are block triangular with identity blocks on the diagonal. They are invertible, with inverses obtained by changing the sign of the off-diagonal block (@thm-block-triangular-inverse), and they have determinant \( 1 \). So, up to these harmless factors, \( \M \) **is** the block diagonal matrix \( \A \oplus (\M/\A) \) when \( \A \) and \( \D \) are square. Determinant, rank and invertibility cannot tell the difference.

## Determinant and rank

The outer factors of @thm-block-ldu do not change the determinant or the rank, so both can be read off from the middle factor.

::: {#thm-schur-determinant}
[Schur Determinant Formula]

Let \( \M = \begin{pmatrix} \A & \B \\ \C & \D \end{pmatrix} \in M_{k+l}(F) \) with \( \A \in M_k(F) \), \( \D \in M_l(F) \) and \( k, l \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. If \( \A \) is invertible, then \( \det \M = \det \A \cdot \det(\M/\A) \).
2. If \( \D \) is invertible, then \( \det \M = \det \D \cdot \det(\M/\D) \).
:::
:::

::: {.proof}
(a) By @thm-block-ldu (a), \( \M = \L\,(\A \oplus (\M/\A))\,\U \) with \( \L = \begin{pmatrix} \I_k & 0 \\ \C \A^{-1} & \I_l \end{pmatrix} \) and \( \U = \begin{pmatrix} \I_k & \A^{-1}\B \\ 0 & \I_l \end{pmatrix} \). Here \( p = l \) because \( \M \) is square, so \( \M/\A \in M_l(F) \). By @thm-det-block-triangular, \( \det \L = \det \I_k\det \I_l = 1 \), \( \det \U = 1 \), and \( \det(\A \oplus (\M/\A)) = \det \A\det(\M/\A) \). By @thm-det-multiplicative,
\[
\det \M = \det \L \cdot \det \A\det(\M/\A) \cdot \det \U = \det \A\det(\M/\A) .
\]
(b) The same argument with @thm-block-ldu (b), where \( \M/\D \in M_k(F) \) because \( \M \) is square.
:::

This is the correct replacement for the false rule \( \det \M = \det(\A \D - \B \C) \) of Section 1: the determinant of \( \M \) is that of \( \A \) times that of the complement. For \( k = l = 1 \) it is \( a\big(d - ca^{-1}b\big) = ad - bc \). Chapter 6 promised this, and it relies on @thm-det-block-triangular in exactly the form proved there, with square diagonal blocks.

::: {#thm-schur-rank}
[Schur Rank Formula]

Let \( \M = \begin{pmatrix} \A & \B \\ \C & \D \end{pmatrix} \) be partitioned as in @def-schur-complement. If \( \A \in M_k(F) \) is invertible, then
\[
\rank \M = k + \rank(\M/\A) .
\]
Symmetrically, if \( \D \in M_l(F) \) is invertible, then \( \rank \M = l + \rank(\M/\D) \).
:::

::: {.proof}
By @thm-block-ldu (a), \( \M = \L\begin{pmatrix} \A & 0 \\ 0 & \M/\A \end{pmatrix}\U \), where \( \L \) and \( \U \) are invertible by @thm-block-elimination-rank (a). By @thm-rank-product-inequality, \( \rank \M \) equals the rank of the middle factor, which is \( \rank \A + \rank(\M/\A) = k + \rank(\M/\A) \) by @thm-block-rank-inequalities (b) and @thm-invertible-tfae. The second statement follows in the same way from @thm-block-ldu (b).
:::

In words: an invertible block of size \( k \) contributes exactly \( k \) to the rank, and all the remaining rank sits in its complement. For example, in @exm-rank-i-minus-ab the matrix \( \begin{pmatrix} \I_m & \A \\ \B & \I_n \end{pmatrix} \) has the two complements \( \I_n - \B \A \) and \( \I_m - \A \B \), and the theorem gives both expressions for its rank at once.

## Inverting a block matrix

Since \( \A \oplus (\M/\A) \) is invertible exactly when \( \M/\A \) is, the factorization also inverts \( \M \): invert the three factors and multiply them in the reverse order.

::: {#thm-block-inverse-formula}
[Block Inverse Formula]

Let \( \M = \begin{pmatrix} \A & \B \\ \C & \D \end{pmatrix} \in M_{k+l}(F) \) with \( \A \in M_k(F) \) and \( \D \in M_l(F) \).

::: {.enumerate options="label=(\alph*)"}
1. Suppose \( \A \) is invertible, and let \( \S = \M/\A \). Then \( \M \) is invertible if and only if \( \S \) is invertible, and in that case
\[
\M^{-1} = \begin{pmatrix} \A^{-1} + \A^{-1}\B \S^{-1}\C \A^{-1} & -\A^{-1}\B \S^{-1} \\ -\S^{-1}\C \A^{-1} & \S^{-1} \end{pmatrix}.
\]
In particular the lower-right \( l \times l \) block of \( \M^{-1} \) is \( (\M/\A)^{-1} \).
2. Suppose \( \D \) is invertible, and let \( \S' = \M/\D \). Then \( \M \) is invertible if and only if \( \S' \) is invertible, and in that case
\[
\M^{-1} = \begin{pmatrix} \S'^{-1} & -\S'^{-1}\B \D^{-1} \\ -\D^{-1}\C \S'^{-1} & \D^{-1} + \D^{-1}\C \S'^{-1}\B \D^{-1} \end{pmatrix}.
\]
In particular the upper-left \( k \times k \) block of \( \M^{-1} \) is \( (\M/\D)^{-1} \).
:::
:::

::: {.proof}
(a) By @thm-schur-rank, \( \rank \M = k + \rank \S \). So \( \rank \M = k + l \) if and only if \( \rank \S = l \), and by @thm-invertible-tfae this says that \( \M \) is invertible if and only if \( \S \) is.

Suppose \( \S \) is invertible. In @thm-block-ldu (a), \( \M = \L(\A \oplus \S)\U \), where \( \L^{-1} = \begin{pmatrix} \I_k & 0 \\ -\C \A^{-1} & \I_l \end{pmatrix} \) and \( \U^{-1} = \begin{pmatrix} \I_k & -\A^{-1}\B \\ 0 & \I_l \end{pmatrix} \) by @thm-block-triangular-inverse, and \( (\A \oplus \S)^{-1} = \A^{-1} \oplus \S^{-1} \) by @thm-block-diagonal-arithmetic (c). By @thm-inverse-matrix-properties (3), \( \M^{-1} = \U^{-1}(\A^{-1} \oplus \S^{-1})\L^{-1} \). By @thm-block-multiplication,
\[
\begin{aligned}
&\U^{-1}(\A^{-1} \oplus \S^{-1}) = \begin{pmatrix} \A^{-1} & -\A^{-1}\B \S^{-1} \\ 0 & \S^{-1} \end{pmatrix}, \\
&\begin{pmatrix} \A^{-1} & -\A^{-1}\B \S^{-1} \\ 0 & \S^{-1} \end{pmatrix}\begin{pmatrix} \I_k & 0 \\ -\C \A^{-1} & \I_l \end{pmatrix} \\
&\qquad = \begin{pmatrix} \A^{-1} + \A^{-1}\B \S^{-1}\C \A^{-1} & -\A^{-1}\B \S^{-1} \\ -\S^{-1}\C \A^{-1} & \S^{-1} \end{pmatrix}.
\end{aligned}
\]

(b) The equivalence follows from the second statement of @thm-schur-rank in the same way. By @thm-block-ldu (b), \( \M^{-1} = \begin{pmatrix} \I_k & 0 \\ -\D^{-1}\C & \I_l \end{pmatrix}(\S'^{-1} \oplus \D^{-1})\begin{pmatrix} \I_k & -\B \D^{-1} \\ 0 & \I_l \end{pmatrix} \), and
\[
\begin{pmatrix} \I_k & 0 \\ -\D^{-1}\C & \I_l \end{pmatrix}\begin{pmatrix} \S'^{-1} & 0 \\ 0 & \D^{-1} \end{pmatrix} = \begin{pmatrix} \S'^{-1} & 0 \\ -\D^{-1}\C \S'^{-1} & \D^{-1} \end{pmatrix},
\]
whose product with \( \begin{pmatrix} \I_k & -\B \D^{-1} \\ 0 & \I_l \end{pmatrix} \) is the displayed matrix by @thm-block-multiplication.
:::

Nobody should memorize these blocks. Remember instead that \( \M^{-1} \) is the product of three easy inverses in reverse order, and that the corner opposite \( \A \) in \( \M^{-1} \) is the inverse of the complement of \( \A \).

::: {#exm-block-inverse-4x4}
[A \( 4 \times 4 \) Inverse through a \( 2 \times 2 \) Schur Complement]

Invert
\[
\M = \left(\begin{array}{cc|cc} 1 & 1 & 0 & -1 \\ 1 & 2 & -1 & -1 \\ \hline -1 & -1 & 1 & 1 \\ 0 & 1 & 0 & -1 \end{array}\right) \in M_4(\nQ)
\]
using @thm-block-inverse-formula, and find \( \det \M \).
:::

::: {.solution}
The blocks are \( \A = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} \), \( \B = \begin{pmatrix} 0 & -1 \\ -1 & -1 \end{pmatrix} \), \( \C = \begin{pmatrix} -1 & -1 \\ 0 & 1 \end{pmatrix} \), \( \D = \begin{pmatrix} 1 & 1 \\ 0 & -1 \end{pmatrix} \).

*Step 1: invert \( \A \).* \( \det \A = 1 \), so \( \A^{-1} = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix} \) by @thm-two-by-two-inverse.

*Step 2: the two "half" products.*
\[
\C \A^{-1} = \begin{pmatrix} -1 & 0 \\ -1 & 1 \end{pmatrix}, \qquad \A^{-1}\B = \begin{pmatrix} 1 & -1 \\ -1 & 0 \end{pmatrix}, \qquad \C \A^{-1}\B = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}.
\]

*Step 3: the complement and its inverse.* \( \S = \M/\A = \D - \C \A^{-1}\B = \begin{pmatrix} 1 & 0 \\ 1 & -1 \end{pmatrix} \). Its determinant is \( -1 \ne 0 \), so \( \M \) is invertible by @thm-block-inverse-formula (a), and \( \S^{-1} = \begin{pmatrix} 1 & 0 \\ 1 & -1 \end{pmatrix} = \S \) by @thm-two-by-two-inverse. By @thm-schur-determinant, \( \det \M = \det \A\det \S = -1 \).

*Step 4: the blocks of \( \M^{-1} \).* Using Step 2,
\[
\begin{aligned}
-\A^{-1}\B \S^{-1} &= -\begin{pmatrix} 1 & -1 \\ -1 & 0 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 1 & -1 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \\
-\S^{-1}\C \A^{-1} &= -\begin{pmatrix} 1 & 0 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} -1 & 0 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix},
\end{aligned}
\]
and
\[
\begin{aligned}
\A^{-1} + \A^{-1}\B \S^{-1}\C \A^{-1}
  &= \A^{-1} + (\A^{-1}\B \S^{-1})(\C \A^{-1}) \\
  &= \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix} + \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}\begin{pmatrix} -1 & 0 \\ -1 & 1 \end{pmatrix} \\
  &= \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix} + \begin{pmatrix} -1 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} .
\end{aligned}
\]
Hence
\[
\M^{-1} = \left(\begin{array}{cc|cc} 1 & 0 & 0 & -1 \\ 0 & 1 & 1 & 0 \\ \hline 1 & 0 & 1 & 0 \\ 0 & 1 & 1 & -1 \end{array}\right).
\]
Check one row: row \( 1 \) of \( \M \) times column \( 1 \) of \( \M^{-1} \) is \( 1 + 0 + 0 + 0 = 1 \), and times column \( 3 \) is \( 0 + 1 + 0 - 1 = 0 \). All the work was with \( 2 \times 2 \) matrices, and only two of them had to be inverted.
:::

::: {.remark}
When \( \M \) is real symmetric, \( \M/\A \) is again symmetric, and Chapter 12 uses Schur complements to test whether \( \M \) is positive definite one block at a time. Chapter 23 reads Gaussian elimination itself as a sequence of Schur complements of \( 1 \times 1 \) pivots, which is the point of view behind block algorithms in numerical linear algebra.
:::

## The Sherman–Morrison–Woodbury formula

Chapter 6 proved the Matrix Determinant Lemma, \( \det(\I_n + \u\v\tp) = 1 + \v\tp\u \) (@thm-matrix-determinant-lemma), by bordering \( \I_n + \u\v\tp \) into a larger block matrix. There is a matching statement about inverses: if we already know \( \A^{-1} \) and change \( \A \) by a low-rank term \( \U \C \V \), the new inverse should cost only a small inversion. The trick is to find one block matrix that has \( \A \) in one corner and \( \A + \U \C \V \) as a Schur complement, and then to compute its inverse twice.

::: {#thm-woodbury}
[Sherman–Morrison–Woodbury Formula]

Let \( n, k \ge 1 \), let \( \A \in M_n(F) \) and \( \C \in M_k(F) \) be invertible, and let \( \U \in M_{n \times k}(F) \) and \( \V \in M_{k \times n}(F) \). Put \( \W = \C^{-1} + \V \A^{-1}\U \in M_k(F) \).

::: {.enumerate options="label=(\alph*)"}
1. \( \A + \U \C \V \) is invertible if and only if \( \W \) is invertible.
2. In that case
\[
\begin{aligned}
(\A + \U \C \V)^{-1}
  &= \A^{-1} - \A^{-1}\U\,\W^{-1}\,\V \A^{-1} \\
  &= \A^{-1} - \A^{-1}\U\big(\C^{-1} + \V \A^{-1}\U\big)^{-1}\V \A^{-1} .
\end{aligned}
\]
3. \( \det(\A + \U \C \V) = \det \A \cdot \det \C \cdot \det \W \).
:::
:::

::: {.idea}
Look for a block matrix whose two Schur complements are \( \A + \U \C \V \) and something involving \( \W \). The complement of the lower-right corner of \( \M = \begin{pmatrix} \A & \U \\ \V & \D \end{pmatrix} \) is \( \A - \U \D^{-1}\V \), which is \( \A + \U \C \V \) when \( \D^{-1} = -\C \), that is, \( \D = -\C^{-1} \). The complement of the upper-left corner is then \( -\C^{-1} - \V \A^{-1}\U = -\W \). Now @thm-block-inverse-formula computes the upper-left block of \( \M^{-1} \) in two ways: as \( (\M/\D)^{-1} = (\A + \U \C \V)^{-1} \), and from the formula in terms of \( \A \) and \( \M/\A \). Setting them equal is the Woodbury formula. The determinant formula of the previous subsection, used twice, gives (c).
:::

::: {.proof}
Let \( \D = -\C^{-1} \), which is invertible with \( \D^{-1} = -\C \) by @thm-inverse-matrix-properties (2) and (5), and let \( \M = \begin{pmatrix} \A & \U \\ \V & \D \end{pmatrix} \in M_{n+k}(F) \). By @def-schur-complement,
\[
\begin{aligned}
\M/\A &= \D - \V \A^{-1}\U = -\C^{-1} - \V \A^{-1}\U = -\W, \\
\M/\D &= \A - \U \D^{-1}\V = \A + \U \C \V .
\end{aligned}
\]

(a) By @thm-block-inverse-formula (a) and (b), \( \M \) is invertible if and only if \( -\W \) is, and if and only if \( \A + \U \C \V \) is. Since \( -\W \) is invertible exactly when \( \W \) is (@thm-inverse-matrix-properties (5)), this proves (a).

(b) Suppose \( \W \) is invertible, so \( \M \) is invertible, and \( (-\W)^{-1} = -\W^{-1} \). The upper-left \( n \times n \) block of \( \M^{-1} \) is \( (\M/\D)^{-1} = (\A + \U \C \V)^{-1} \) by @thm-block-inverse-formula (b). By @thm-block-inverse-formula (a), applied to \( \M \), whose blocks are \( \A, \U, \V, \D \), and with \( \S = \M/\A = -\W \), the same block is
\[
\A^{-1} + \A^{-1}\U(-\W)^{-1}\V \A^{-1} = \A^{-1} - \A^{-1}\U \W^{-1}\V \A^{-1} .
\]
The two expressions are the same block of the same matrix, so they are equal.

(c) By @thm-schur-determinant (a) and (b), \( \det \A\det(-\W) = \det \M = \det \D\det(\A + \U \C \V) \). Multiplying a \( k \times k \) matrix by \( -1 \) multiplies each of its \( k \) rows by \( -1 \), so by @thm-det-row-operations \( \det(-\W) = (-1)^k\det \W \) and \( \det \D = (-1)^k\det(\C^{-1}) = (-1)^k(\det \C)^{-1} \), using @cor-det-inverse. Hence \( \det \A\,(-1)^k\det \W = (-1)^k(\det \C)^{-1}\det(\A + \U \C \V) \). Multiplying both sides by \( (-1)^k\det \C \) gives (c).
:::

The formula is useful when \( k \) is much smaller than \( n \) and \( \A^{-1} \) is already known or easy (diagonal, say): the only new inversion is of the \( k \times k \) matrix \( \W \). The most common case is a rank-one update, \( k = 1 \) and \( \C = (1) \).

::: {#cor-sherman-morrison}
[Sherman–Morrison Formula]

Let \( \A \in M_n(F) \) be invertible and \( \u, \v \in F^n \). Then \( \A + \u\v\tp \) is invertible if and only if \( 1 + \v\tp \A^{-1}\u \ne 0 \), and in that case
\[
(\A + \u\v\tp)^{-1} = \A^{-1} - \frac{\A^{-1}\u\,\v\tp \A^{-1}}{1 + \v\tp \A^{-1}\u} .
\]
Moreover \( \det(\A + \u\v\tp) = \det \A\,(1 + \v\tp \A^{-1}\u) \).
:::

::: {.proof}
Apply @thm-woodbury with \( k = 1 \), \( \C = (1) \), \( \U = \u \) and \( \V = \v\tp \). Then \( \W = (1 + \v\tp \A^{-1}\u) \) is a \( 1 \times 1 \) matrix, invertible exactly when its entry is non-zero, with inverse the reciprocal. Multiplying by a \( 1 \times 1 \) matrix is multiplying by its entry, which gives the displayed formula; and \( \det \W \) is the entry itself.
:::

For example, over \( \nQ \) let \( \A = \diag(1, -1) \), so \( \A^{-1} = \A \), and \( \u = (1, 1) \). For \( \v = (2, 1) \), \( \A^{-1}\u = (1, -1) \), \( \v\tp \A^{-1} = \begin{pmatrix} 2 & -1 \end{pmatrix} \) and \( 1 + \v\tp \A^{-1}\u = 1 + (2 - 1) = 2 \ne 0 \). So \( \A + \u\v\tp = \begin{pmatrix} 3 & 1 \\ 2 & 0 \end{pmatrix} \) has determinant \( \det \A \cdot 2 = -2 \), and
\[
\begin{aligned}
(\A + \u\v\tp)^{-1}
  &= \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} - \frac12\begin{pmatrix} 1 \\ -1 \end{pmatrix}\begin{pmatrix} 2 & -1 \end{pmatrix} \\
  &= \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} - \begin{pmatrix} 1 & -\frac12 \\ -1 & \frac12 \end{pmatrix}
   = \begin{pmatrix} 0 & \frac12 \\ 1 & -\frac32 \end{pmatrix},
\end{aligned}
\]
which agrees with @thm-two-by-two-inverse. For \( \v = (1, 2) \) instead, \( 1 + \v\tp \A^{-1}\u = 1 + (1 - 2) = 0 \), and indeed \( \A + \u\v\tp = \begin{pmatrix} 2 & 2 \\ 1 & 1 \end{pmatrix} \) is not invertible.

With \( \A = \I_n \), the determinant statement is the Matrix Determinant Lemma of Chapter 6, now obtained as a special case of a formula about general low-rank updates, and it matches @exr-special-determinants-c3.

## Commuting blocks

Section 1 warned that \( \det\begin{pmatrix} \A & \B \\ \C & \D \end{pmatrix} \ne \det(\A \D - \B \C) \) in general. With the Schur complement we can see what goes wrong and what extra hypothesis repairs it. Take all four blocks in \( M_n(F) \) and suppose \( \D \) is invertible. By @thm-schur-determinant (b),
\[
\begin{aligned}
\det \M &= \det \D\,\det(\A - \B \D^{-1}\C) \\
  &= \det\big((\A - \B \D^{-1}\C)\D\big) = \det(\A \D - \B \D^{-1}\C \D),
\end{aligned}
\]
using @thm-det-multiplicative. If \( \C \) and \( \D \) commute, then \( \D^{-1}\C \D = \D^{-1}\D \C = \C \), and the right side is \( \det(\A \D - \B \C) \). So commuting is exactly what lets \( \D^{-1} \) cancel. The real question is how to remove the hypothesis that \( \D \) is invertible, which is not needed for the conclusion to make sense.

Over \( \nR \) one could perturb: \( \D + t\I_n \) is invertible for all but finitely many \( t \), both sides are polynomials in \( t \), and polynomials that agree at infinitely many points are equal. Over a finite field such as \( \nF_2 \) there may be no invertible perturbation at all. We use instead a perturbation by an **indeterminate**: replace \( \D \) by \( \D + x\I_n \), a matrix with entries in \( F[x] \). Its determinant is a monic polynomial, hence not the zero polynomial, and that is all the cancellation needs. First we record that evaluating polynomial entries commutes with matrix operations.

For \( \N = (n_{ij}) \) with entries in \( F[x] \) and \( c \in F \), write \( \N(c) = (n_{ij}(c)) \) for the matrix over \( F \) obtained by evaluating every entry at \( c \). A matrix over \( F \) is a matrix over \( F[x] \) with constant entries, and then \( \N(c) = \N \).

::: {#lem-evaluate-polynomial-matrix}
[Evaluating a Matrix of Polynomials]

Let \( c \in F \), and let \( \N, \N' \) be matrices with entries in \( F[x] \) of sizes for which the operations below are defined. Then \( (\N + \N')(c) = \N(c) + \N'(c) \), \( (\N \N')(c) = \N(c)\N'(c) \), and, for square \( \N \), \( (\det \N)(c) = \det\big(\N(c)\big) \).
:::

::: {.proof}
By @thm-evaluation-respects-operations, evaluation at \( c \) sends sums of polynomials to sums, products to products, and constants to themselves. The \( (i, j) \)-entry of \( \N + \N' \) is \( n_{ij} + n'_{ij} \) and that of \( \N \N' \) is \( \sum_l n_{il}n'_{lj} \), so evaluating gives the corresponding entries of \( \N(c) + \N'(c) \) and \( \N(c)\N'(c) \). The determinant \( \det \N \) is the Leibniz sum \( \sum_{\sigma} \sgn(\sigma)\prod_j n_{\sigma(j)j} \) of @def-determinant, computed in \( F[x] \), and evaluating it term by term gives the Leibniz sum for \( \N(c) \). This is the argument of @lem-charpoly-evaluation.
:::

::: {#thm-det-commuting-blocks}
[Determinant with Commuting Blocks]

Let \( n \ge 1 \) and \( \A, \B, \C, \D \in M_n(F) \) over **any** field \( F \). If \( \C \D = \D \C \), then
\[
\det\begin{pmatrix} \A & \B \\ \C & \D \end{pmatrix} = \det(\A \D - \B \C) .
\]
:::

::: {.idea}
① Work over the commutative ring \( F[x] \), replacing \( \D \) by \( \D_x = \D + x\I_n \), which still commutes with \( \C \). ② Multiply \( \M_x = \begin{pmatrix} \A & \B \\ \C & \D_x \end{pmatrix} \) on the right by \( \begin{pmatrix} \D_x & 0 \\ -\C & \I_n \end{pmatrix} \): the lower-left block becomes \( \C \D_x - \D_x\C = 0 \) and the upper-left block becomes \( \A \D_x - \B \C \). This is the Schur computation above with \( \D^{-1} \) cleared from the denominators. ③ Take determinants: \( \det \M_x\det \D_x = \det(\A \D_x - \B \C)\det \D_x \). ④ Cancel \( \det \D_x \), which is legal because it is a non-zero polynomial and \( F[x] \) has no zero divisors. ⑤ Set \( x = 0 \). Each step uses only determinant facts that Chapter 6 proved over commutative rings.
:::

::: {.proof}
Regard \( \A, \B, \C, \D \) as matrices over \( F[x] \) with constant entries, and let \( \D_x = \D + x\I_n \). The proofs of @thm-matrix-multiplication-properties use only the ring axioms, so they hold for matrices over \( F[x] \); in particular
\[
\C \D_x = \C \D + x\C = \D \C + x\C = \D_x\C,
\]
using the hypothesis \( \C \D = \D \C \). Let
\[
\M_x = \begin{pmatrix} \A & \B \\ \C & \D_x \end{pmatrix}, \qquad \R = \begin{pmatrix} \D_x & 0 \\ -\C & \I_n \end{pmatrix},
\]
both in \( M_{2n}(F[x]) \). By @thm-block-multiplication, which holds over \( F[x] \) by the remark following it,
\[
\M_x\R = \begin{pmatrix} \A \D_x - \B \C & \B \\ \C \D_x - \D_x\C & \D_x \end{pmatrix} = \begin{pmatrix} \A \D_x - \B \C & \B \\ 0 & \D_x \end{pmatrix}.
\]
By the remarks in Chapter 6 §5 and §8, @thm-det-multiplicative and @thm-det-block-triangular hold over the commutative ring \( F[x] \). Hence \( \det(\M_x\R) = \det \M_x\det \R \), with \( \det \R = \det \D_x\det \I_n = \det \D_x \), and \( \det(\M_x\R) = \det(\A \D_x - \B \C)\det \D_x \). So, in \( F[x] \),
\[
\det \M_x\cdot\det \D_x = \det(\A \D_x - \B \C)\cdot\det \D_x . \tag{$\ast$}
\]
Now \( \D_x = x\I_n - (-\D) \), so \( \det \D_x = p_{-\D}(x) \) is the characteristic polynomial of \( -\D \in M_n(F) \) (@def-characteristic-polynomial). By @thm-charpoly-coefficients it is monic of degree \( n \), so \( \det \D_x \ne 0 \) in \( F[x] \). By @cor-polynomial-no-zero-divisors (2), we may cancel it from \( (\ast) \):
\[
\det \M_x = \det(\A \D_x - \B \C) \quad\text{in } F[x] .
\]
Finally evaluate both sides at \( 0 \). By @lem-evaluate-polynomial-matrix, \( (\det \M_x)(0) = \det(\M_x(0)) = \det \M \), since \( \D_x(0) = \D \); and \( (\A \D_x - \B \C)(0) = \A \D - \B \C \), so \( (\det(\A \D_x - \B \C))(0) = \det(\A \D - \B \C) \). Hence \( \det \M = \det(\A \D - \B \C) \).
:::

The cancellation in \( F[x] \) is the heart of the argument, so it is worth being precise about why it is legal. Over \( F \) we cannot divide by \( \det \D \) when it is \( 0 \). Over \( F[x] \) we still cannot divide, since \( \det \D_x \) usually has no inverse, but we do not need to: cancellation only needs "\( pq = pr \) and \( p \ne 0 \) imply \( q = r \)", and this holds in \( F[x] \) because a product of non-zero polynomials is non-zero (@cor-polynomial-no-zero-divisors). The perturbation \( x\I_n \) makes \( \det \D_x \) non-zero **as a polynomial** even when every value \( \det(\D + c\I_n) \) with \( c \in F \) is zero. For example, over \( \nF_2 \), let \( \D = \E_{22} = \diag(0, 1) \). Then \( \det(\D + 0\I_2) = 0 \) and \( \det(\D + \I_2) = \det\diag(1, 0) = 0 \), because \( 1 + 1 = 0 \) in \( \nF_2 \); no scalar shift makes \( \D \) invertible. But \( \det(\D + x\I_2) = x(x + 1) = x^2 + x \) is not the zero polynomial.

For example, over \( \nQ \), let \( \A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \), \( \B = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} \), \( \D = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) and \( \C = 2\I_2 + \D = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} \), which commutes with \( \D \). Here \( \D \) is not invertible, so the Schur route is closed. The theorem gives \( \det \M = \det(\A \D - \B \C) = \det\begin{pmatrix} -2 & 0 \\ -2 & -3 \end{pmatrix} = 6 \).

::: {.warning}
**Which blocks commute decides which product appears.** The hypothesis \( \C \D = \D \C \) gives \( \det(\A \D - \B \C) \). If instead \( \A \) and \( \C \) commute, the correct formula is \( \det(\A \D - \C \B) \) (@exr-block-determinants-and-schur-complements-c3), with \( \C \) and \( \B \) in the other order. The two can differ: for the blocks \( \A = \I_2 \), \( \B = \E_{12} \), \( \C = \E_{21} \), \( \D = \E_{11} \) of the warning in Section 1, \( \A \) commutes with \( \C \) but \( \C \) does not commute with \( \D \); indeed \( \det \M = -1 = \det(\E_{11} - \E_{22}) = \det(\A \D - \C \B) \), while \( \det(\A \D - \B \C) = 0 \).
:::

## Exercises

### A. Check your understanding

:::: {#exr-block-determinants-and-schur-complements-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the Schur complement \( \M/\A \), including the hypothesis on \( \A \) and the size of \( \M/\A \).
2. State the block LDU factorization of \( \M \) in terms of \( \A \) and \( \M/\A \).
3. True or false: if \( \M = \begin{pmatrix} \A & \B \\ \C & \D \end{pmatrix} \) is invertible and \( \A \) is square, then \( \A \) is invertible. Justify your answer.
4. If \( \A \) is invertible and \( \M \) is invertible, which block of \( \M^{-1} \) is \( (\M/\A)^{-1} \)?
5. True or false: for all \( \A, \B, \C, \D \in M_n(F) \) with \( \C \D = \D \C \), \( \det\begin{pmatrix} \A & \B \\ \C & \D \end{pmatrix} = \det(\A \D - \B \C) \), even if \( \D \) is not invertible and \( F = \nF_2 \). Justify your answer.
:::
::::

::: {.solution}
(a) For \( \M = \begin{pmatrix} \A & \B \\ \C & \D \end{pmatrix} \) with \( \A \in M_k(F) \) **invertible**, \( \B \in M_{k \times l}(F) \), \( \C \in M_{p \times k}(F) \), \( \D \in M_{p \times l}(F) \): \( \M/\A = \D - \C \A^{-1}\B \in M_{p \times l}(F) \), the size of \( \D \) (@def-schur-complement).

(b) \( \M = \begin{pmatrix} \I_k & 0 \\ \C \A^{-1} & \I_p \end{pmatrix}\begin{pmatrix} \A & 0 \\ 0 & \M/\A \end{pmatrix}\begin{pmatrix} \I_k & \A^{-1}\B \\ 0 & \I_l \end{pmatrix} \) (@thm-block-ldu).

(c) False. \( \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) is invertible, but \( \A = (0) \) is not.

(d) The lower-right block, in the position of \( \D \) (@thm-block-inverse-formula (a)).

(e) True. @thm-det-commuting-blocks holds over every field and needs no invertibility; its proof cancels the non-zero polynomial \( \det(\D + x\I_n) \) in \( F[x] \).
:::

### B. Practice

:::: {#exr-block-determinants-and-schur-complements-b1}
[B1: A Schur complement, a determinant and a rank]

Let
\[
\M = \left(\begin{array}{cc|cc} 2 & 1 & 1 & 0 \\ 1 & 1 & 3 & 1 \\ \hline 1 & 2 & 9 & 5 \\ 0 & 1 & 6 & 4 \end{array}\right) \in M_4(\nQ).
\]
Compute \( \M/\A \) for the upper-left block \( \A \). Hence find \( \det \M \) and \( \rank \M \), and decide whether \( \M \) is invertible.
::::

::: {.solution}
\( \A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \) has \( \det \A = 1 \), so \( \A^{-1} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} \) (@thm-two-by-two-inverse). With \( \B = \begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix} \), \( \C = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \), \( \D = \begin{pmatrix} 9 & 5 \\ 6 & 4 \end{pmatrix} \):
\[
\C \A^{-1} = \begin{pmatrix} -1 & 3 \\ -1 & 2 \end{pmatrix}, \qquad \C \A^{-1}\B = \begin{pmatrix} 8 & 3 \\ 5 & 2 \end{pmatrix}, \qquad \M/\A = \begin{pmatrix} 1 & 2 \\ 1 & 2 \end{pmatrix}.
\]
By @thm-schur-determinant, \( \det \M = \det \A\det(\M/\A) = 1 \cdot 0 = 0 \). By @thm-schur-rank, \( \rank \M = 2 + \rank(\M/\A) = 2 + 1 = 3 \), since \( \M/\A \) is non-zero with equal rows. So \( \M \) is not invertible (@thm-invertible-tfae-det (d)).
:::

:::: {#exr-block-determinants-and-schur-complements-b2}
[B2: A rank-one update]

Let \( \A = \diag(1, 2, 4) \in M_3(\nQ) \), \( \u = (1, 1, 1) \) and \( \v = (1, -1, 2) \). Use @cor-sherman-morrison to find \( \det(\A + \u\v\tp) \) and \( (\A + \u\v\tp)^{-1} \), and check one entry.
::::

::: {.solution}
\( \A^{-1} = \diag(1, \frac12, \frac14) \), so \( \A^{-1}\u = (1, \frac12, \frac14) \) and \( \v\tp \A^{-1} = \begin{pmatrix} 1 & -\frac12 & \frac12 \end{pmatrix} \). Then \( \v\tp \A^{-1}\u = 1 - \frac12 + \frac12 = 1 \), so \( 1 + \v\tp \A^{-1}\u = 2 \ne 0 \). By @cor-sherman-morrison, \( \A + \u\v\tp \) is invertible, \( \det(\A + \u\v\tp) = 8 \cdot 2 = 16 \), and
\[
\begin{aligned}
(\A + \u\v\tp)^{-1}
  &= \diag\big(1, \tfrac12, \tfrac14\big) - \frac12\begin{pmatrix} 1 \\ \frac12 \\ \frac14 \end{pmatrix}\begin{pmatrix} 1 & -\frac12 & \frac12 \end{pmatrix} \\
  &= \begin{pmatrix} 1 & 0 & 0 \\ 0 & \frac12 & 0 \\ 0 & 0 & \frac14 \end{pmatrix} - \begin{pmatrix} \frac12 & -\frac14 & \frac14 \\ \frac14 & -\frac18 & \frac18 \\ \frac18 & -\frac1{16} & \frac1{16} \end{pmatrix} \\
  &= \begin{pmatrix} \frac12 & \frac14 & -\frac14 \\ -\frac14 & \frac58 & -\frac18 \\ -\frac18 & \frac1{16} & \frac3{16} \end{pmatrix}.
\end{aligned}
\]
Check: \( \A + \u\v\tp = \begin{pmatrix} 2 & -1 & 2 \\ 1 & 1 & 2 \\ 1 & -1 & 6 \end{pmatrix} \), and its row \( 1 \) times column \( 1 \) of the answer is \( 1 + \frac14 - \frac14 = 1 \), times column \( 2 \) is \( \frac12 - \frac58 + \frac18 = 0 \).
:::

:::: {#exr-block-determinants-and-schur-complements-b3}
[B3: Identity corners]

Let \( \B \in M_{k \times l}(F) \), \( \C \in M_{l \times k}(F) \) and \( \M = \begin{pmatrix} \I_k & \B \\ \C & \I_l \end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \M \) is invertible if and only if \( \S = \I_l - \C \B \) is, and write down \( \M^{-1} \) in terms of \( \S^{-1} \).
2. Deduce the inverse of \( \begin{pmatrix} \I_k & \B \\ 0 & \I_l \end{pmatrix} \).
3. For \( \B = \begin{pmatrix} 1 \\ 2 \end{pmatrix} \) and \( \C = \begin{pmatrix} 1 & 1 \end{pmatrix} \) over \( \nQ \), compute \( \M^{-1} \).
:::
::::

::: {.solution}
(a) The block \( \I_k \) is invertible and \( \M/\I_k = \I_l - \C \I_k^{-1}\B = \I_l - \C \B \). By @thm-block-inverse-formula (a), \( \M \) is invertible if and only if \( \I_l - \C \B \) is, and then, with \( \A^{-1} = \I_k \),
\[
\M^{-1} = \begin{pmatrix} \I_k + \B \S^{-1}\C & -\B \S^{-1} \\ -\S^{-1}\C & \S^{-1} \end{pmatrix}.
\]

(b) With \( \C = 0 \), \( \S = \I_l - \C \B = \I_l \) and \( \S^{-1} = \I_l \), so the inverse is \( \begin{pmatrix} \I_k & -\B \\ 0 & \I_l \end{pmatrix} \), in agreement with @thm-block-triangular-inverse.

(c) \( \C \B = (3) \), so \( \S = \I_1 - \C \B = (-2) \) and \( \S^{-1} = (-\frac12) \). Then \( \B \S^{-1}\C = -\frac12\begin{pmatrix} 1 & 1 \\ 2 & 2 \end{pmatrix} \), \( -\B \S^{-1} = \begin{pmatrix} \frac12 \\ 1 \end{pmatrix} \) and \( -\S^{-1}\C = \begin{pmatrix} \frac12 & \frac12 \end{pmatrix} \), so
\[
\M^{-1} = \begin{pmatrix} \frac12 & -\frac12 & \frac12 \\ -1 & 0 & 1 \\ \frac12 & \frac12 & -\frac12 \end{pmatrix}, \qquad \M = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 2 \\ 1 & 1 & 1 \end{pmatrix}.
\]
Check: row \( 3 \) of \( \M \) times column \( 3 \) of \( \M^{-1} \) is \( \frac12 + 1 - \frac12 = 1 \), and times column \( 1 \) is \( \frac12 - 1 + \frac12 = 0 \).
:::

### C. Going deeper

:::: {#exr-block-determinants-and-schur-complements-c1}
[C1: Sylvester's determinant identity]

Let \( \A \in M_{m \times n}(F) \) and \( \B \in M_{n \times m}(F) \) with \( m, n \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Compute both Schur complements of the identity blocks in \( \M = \begin{pmatrix} \I_m & -\A \\ \B & \I_n \end{pmatrix} \), and deduce
\[
\det(\I_m + \A \B) = \det(\I_n + \B \A) .
\]
2. Deduce that for every non-zero \( c \in F \), \( \det(c\I_m - \A \B) = c^{m-n}\det(c\I_n - \B \A) \).
3. Deduce @thm-matrix-determinant-lemma from (a).
:::
::::

::: {.solution}
(a) Both identity blocks are invertible. By @def-schur-complement,
\[
\begin{aligned}
\M/\I_m &= \I_n - \B \I_m^{-1}(-\A) = \I_n + \B \A, \\
\M/\I_n &= \I_m - (-\A)\I_n^{-1}\B = \I_m + \A \B .
\end{aligned}
\]
By @thm-schur-determinant (a) and (b), \( \det \M = \det \I_m\det(\I_n + \B \A) \) and \( \det \M = \det \I_n\det(\I_m + \A \B) \). Hence \( \det(\I_m + \A \B) = \det(\I_n + \B \A) \).

(b) Let \( \A' = -c^{-1}\A \). Then \( c\I_m - \A \B = c(\I_m + \A'\B) \) and \( c\I_n - \B \A = c(\I_n + \B \A') \). Multiplying an \( m \times m \) matrix by \( c \) multiplies each of its \( m \) rows by \( c \), so it multiplies the determinant by \( c^m \) (@thm-det-row-operations). By (a) applied to \( \A' \) and \( \B \),
\[
\begin{aligned}
\det(c\I_m - \A \B)
  &= c^m\det(\I_m + \A'\B) = c^m\det(\I_n + \B \A') \\
  &= c^m c^{-n}\det(c\I_n - \B \A) = c^{m-n}\det(c\I_n - \B \A) .
\end{aligned}
\]

(c) Let \( \u, \v \in F^n \), and apply (a) with the sizes \( m, n \) there replaced by \( n, 1 \): \( \A = \u \in M_{n \times 1}(F) \) and \( \B = \v\tp \in M_{1 \times n}(F) \). Then \( \det(\I_n + \u\v\tp) = \det(\I_1 + \v\tp\u) = 1 + \v\tp\u \), because the determinant of a \( 1 \times 1 \) matrix is its entry.
:::

:::: {#exr-block-determinants-and-schur-complements-c2}
[C2: Pivots as Schur complements]

Let \( \A \in M_n(F) \), and for \( 1 \le k \le n \) let \( \A_k \) be its leading principal submatrix (the top-left \( k \times k \) corner), as in @exr-lu-factorization-c1.

::: {.enumerate options="label=(\alph*)"}
1. Suppose \( \A_{k-1} \) is invertible, where \( 2 \le k \le n \), and write \( \A_k = \begin{pmatrix} \A_{k-1} & \b \\ \c\tp & d \end{pmatrix} \). Show that \( s_k \coloneqq \A_k/\A_{k-1} \) is the scalar \( d - \c\tp \A_{k-1}^{-1}\b \), and that \( \det \A_k = \det \A_{k-1}\cdot s_k \).
2. Suppose \( \A_1, \dots, \A_n \) are all invertible, and put \( s_1 = a_{11} \). Prove that \( \det \A_k = s_1s_2\cdots s_k \) for every \( k \), and that every \( s_k \) is non-zero.
3. Keep the hypothesis of (b). In the proof of @exr-lu-factorization-c1 (c), the last pivot is \( z = d - \x\tp\y \) with \( \y = \L'^{-1}\b \) and \( \x\tp = \c\tp \U'^{-1} \). Show that \( z = \A_n/\A_{n-1} \). Deduce that the diagonal entries of \( \U \) in the LU factorization are \( u_{kk} = \det \A_k / \det \A_{k-1} \), with \( \det \A_0 \coloneqq 1 \).
4. Check (c) for \( \A = \begin{pmatrix} 2 & 1 & 1 \\ 4 & 3 & 3 \\ 8 & 7 & 9 \end{pmatrix} \) over \( \nQ \).
:::
::::

::: {.solution}
(a) With the partition \( k - 1, 1 \), @def-schur-complement gives the \( 1 \times 1 \) matrix \( \A_k/\A_{k-1} = d - \c\tp \A_{k-1}^{-1}\b \), which we identify with its entry. By @thm-schur-determinant (a), \( \det \A_k = \det \A_{k-1}\det(s_k) = \det \A_{k-1}\cdot s_k \).

(b) By induction on \( k \). For \( k = 1 \), \( \det \A_1 = a_{11} = s_1 \). If \( \det \A_{k-1} = s_1\cdots s_{k-1} \), then by (a), which applies since \( \A_{k-1} \) is invertible, \( \det \A_k = s_1\cdots s_{k-1}s_k \). Since \( \A_k \) is invertible, \( \det \A_k \ne 0 \) (@thm-det-nonzero-iff-invertible), so no factor \( s_k \) is zero (@thm-field-basic-properties (d)).

(c) \( \A_{n-1} = \L'\U' \) with both factors invertible, so \( \A_{n-1}^{-1} = \U'^{-1}\L'^{-1} \) (@thm-inverse-matrix-properties (3)) and \( \x\tp\y = \c\tp \U'^{-1}\L'^{-1}\b = \c\tp \A_{n-1}^{-1}\b \). Hence \( z = d - \c\tp \A_{n-1}^{-1}\b = \A_n/\A_{n-1} = s_n \) by (a). The same construction applied to \( \A_k \) (whose LU factors are the top-left corners \( \L_k, \U_k \) of \( \L, \U \), by @exr-lu-factorization-c1 (a) and @thm-lu-unique) shows \( u_{kk} = s_k \) for every \( k \). By (a) and (b), \( s_k = \det \A_k/\det \A_{k-1} \), with \( s_1 = \det \A_1/1 \).

(d) \( \det \A_1 = 2 \), \( \det \A_2 = 6 - 4 = 2 \), and expanding, \( \det \A_3 = 2(27 - 21) - 1(36 - 24) + 1(28 - 24) = 12 - 12 + 4 = 4 \). The predicted pivots are \( 2 \), \( 2/2 = 1 \), \( 4/2 = 2 \). Elimination gives \( \L = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 4 & 3 & 1 \end{pmatrix} \) and \( \U = \begin{pmatrix} 2 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 2 \end{pmatrix} \): subtract \( 2 \) and \( 4 \) times row \( 1 \) to get rows \( (0, 1, 1) \) and \( (0, 3, 5) \), then \( 3 \) times the new row \( 2 \) to get \( (0, 0, 2) \). The diagonal of \( \U \) is \( 2, 1, 2 \), as predicted.
:::

:::: {#exr-block-determinants-and-schur-complements-c3}
[C3: When \( \A \) and \( \C \) commute]

Let \( n \ge 1 \) and \( \A, \B, \C, \D \in M_n(F) \) with \( \A \C = \C \A \), and \( \M = \begin{pmatrix} \A & \B \\ \C & \D \end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Assume \( \A \) is invertible. Use @thm-schur-determinant to prove \( \det \M = \det(\A \D - \C \B) \).
2. Remove the assumption that \( \A \) is invertible, over any field, by adapting the proof of @thm-det-commuting-blocks with \( \A_x = \A + x\I_n \).
3. For \( \A = \I_2 \), \( \B = \E_{12} \), \( \C = \E_{21} \), \( \D = \E_{11} \) in \( M_2(\nQ) \), check that \( \A \C = \C \A \), and compare \( \det \M \), \( \det(\A \D - \C \B) \) and \( \det(\A \D - \B \C) \).
:::

*Hint for (b): multiply \( \M_x \) on the left by a block matrix that clears the lower-left block.*
::::

::: {.solution}
(a) By @thm-schur-determinant (a) and @thm-det-multiplicative,
\[
\begin{aligned}
\det \M &= \det \A\det(\D - \C \A^{-1}\B) \\
  &= \det\big(\A(\D - \C \A^{-1}\B)\big) = \det(\A \D - \A \C \A^{-1}\B) .
\end{aligned}
\]
Since \( \A \C = \C \A \), \( \A \C \A^{-1} = \C \A \A^{-1} = \C \), so \( \det \M = \det(\A \D - \C \B) \).

(b) Let \( \A_x = \A + x\I_n \) over \( F[x] \). Then \( \A_x\C = \A \C + x\C = \C \A + x\C = \C \A_x \). Let \( \M_x = \begin{pmatrix} \A_x & \B \\ \C & \D \end{pmatrix} \) and \( \L = \begin{pmatrix} \I_n & 0 \\ -\C & \A_x \end{pmatrix} \). By @thm-block-multiplication over \( F[x] \),
\[
\L \M_x = \begin{pmatrix} \A_x & \B \\ -\C \A_x + \A_x\C & -\C \B + \A_x\D \end{pmatrix} = \begin{pmatrix} \A_x & \B \\ 0 & \A_x\D - \C \B \end{pmatrix}.
\]
By @thm-det-multiplicative and @thm-det-block-triangular over \( F[x] \) (Chapter 6 §5 and §8), \( \det \A_x\det \M_x = \det \A_x\det(\A_x\D - \C \B) \), using \( \det \L = \det \I_n\det \A_x \). As in the proof of @thm-det-commuting-blocks, \( \det \A_x = p_{-\A}(x) \) is monic, hence non-zero, and @cor-polynomial-no-zero-divisors (2) gives \( \det \M_x = \det(\A_x\D - \C \B) \). Evaluating at \( x = 0 \) with @lem-evaluate-polynomial-matrix gives \( \det \M = \det(\A \D - \C \B) \).

(c) \( \A \C = \C = \C \A \), since \( \A = \I_2 \). As computed in Section 1, \( \det \M = -1 \). Also \( \A \D - \C \B = \E_{11} - \E_{21}\E_{12} = \E_{11} - \E_{22} = \diag(1, -1) \), with determinant \( -1 \), in agreement with (b). But \( \A \D - \B \C = \E_{11} - \E_{12}\E_{21} = \E_{11} - \E_{11} = 0 \), with determinant \( 0 \). So with \( \A \C = \C \A \) the product must be taken as \( \C \B \), not \( \B \C \); here \( \C \D = \E_{21} \ne 0 = \D \C \), so @thm-det-commuting-blocks does not apply.
:::
