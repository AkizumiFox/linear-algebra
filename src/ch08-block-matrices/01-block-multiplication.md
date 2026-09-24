# Partitions and Block Multiplication

A large matrix often has structure that its individual entries hide: a corner of zeros, a copy of the identity, a smaller matrix repeated. Chapter 7 already met one such shape, the block triangular matrix, and computed its determinant from two smaller determinants. This section makes the idea systematic. We cut matrices into rectangular pieces, prove that products can be computed piece by piece, and use the pieces to read off structure: direct sums become block diagonal matrices, and a subspace that an operator maps into itself becomes a zero block in the corner.

## Cutting a matrix into blocks

Take two \( 4 \times 4 \) matrices over \( \nQ \) whose top-right \( 2 \times 2 \) corners are zero:
\[
\M = \left(\begin{array}{cc|cc} 1 & 2 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ \hline 1 & 0 & 2 & 1 \\ 2 & 1 & 1 & 1 \end{array}\right), \qquad
\N = \left(\begin{array}{cc|cc} 1 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ \hline 0 & 1 & 1 & 0 \\ 1 & 1 & 3 & 1 \end{array}\right).
\]
The lines cut each matrix into four \( 2 \times 2 \) pieces. Name them: \( \M = \begin{pmatrix} \A & 0 \\ \C & \D \end{pmatrix} \) and \( \N = \begin{pmatrix} \E & 0 \\ \G & \H \end{pmatrix} \), with \( \A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \), \( \C = \begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix} \), and so on. If we pretend that the pieces are numbers and multiply as for \( 2 \times 2 \) matrices, keeping the order of every product, we get
\[
\M \N \overset{?}{=} \begin{pmatrix} \A \E + 0\G & \A0 + 0\H \\ \C \E + \D \G & \C0 + \D \H \end{pmatrix} = \begin{pmatrix} \A \E & 0 \\ \C \E + \D \G & \D \H \end{pmatrix}.
\]
With \( \A \E = \begin{pmatrix} 3 & -1 \\ 1 & 0 \end{pmatrix} \), \( \C \E + \D \G = \begin{pmatrix} 2 & 2 \\ 4 & 0 \end{pmatrix} \) and \( \D \H = \begin{pmatrix} 5 & 1 \\ 4 & 1 \end{pmatrix} \), this predicts
\[
\M \N = \begin{pmatrix} 3 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 2 & 2 & 5 & 1 \\ 4 & 0 & 4 & 1 \end{pmatrix},
\]
and multiplying out the sixteen entries directly gives exactly this matrix. Two things happened. The zero corner of the product came for free, with no arithmetic. And the product of two \( 4 \times 4 \) matrices became four products of \( 2 \times 2 \) matrices, \( \A \E \), \( \C \E \), \( \D \G \) and \( \D \H \); the other four products in the block formula have a zero factor and cost nothing. To use this safely we need to say precisely what "cutting" means and prove that the pretend multiplication is always correct.

*Draw horizontal lines between rows and vertical lines between columns; the pieces are the blocks.*

::: {#def-block-partition}
[Block Partition]

Let \( \A = (a_{ij}) \in M_{m \times n}(F) \). A **row partition** of \( \A \) is a list of **positive** integers \( m_1, \dots, m_a \) with \( m_1 + \dots + m_a = m \), and a **column partition** is a list of positive integers \( n_1, \dots, n_b \) with \( n_1 + \dots + n_b = n \). Put \( \mu_r = m_1 + \dots + m_r \) and \( \nu_s = n_1 + \dots + n_s \), with \( \mu_0 = \nu_0 = 0 \). For \( 1 \le r \le a \) and \( 1 \le s \le b \), the **\( (r, s) \) block** of \( \A \) is the matrix \( \A_{rs} \in M_{m_r \times n_s}(F) \) with entries
\[
(\A_{rs})_{ij} = a_{\mu_{r-1} + i,\ \nu_{s-1} + j} \qquad (1 \le i \le m_r,\ 1 \le j \le n_s).
\]
We then write \( \A = (\A_{rs}) \), displayed as an \( a \times b \) array of blocks, and call \( \A \) a **block matrix**.

Let \( \B \in M_{n \times p}(F) \). Partitions of \( \A \) and \( \B \) are **conformable** if the column partition of \( \A \) and the row partition of \( \B \) are **the same list** \( n_1, \dots, n_b \), in the same order.
:::

In words: the row partition says where the horizontal lines go. Block row \( r \) consists of the rows with indices in \( I_r = \{ \mu_{r-1} + 1, \dots, \mu_r \} \), a run of \( m_r \) consecutive rows, and similarly block column \( s \) consists of the columns in \( J_s = \{ \nu_{s-1} + 1, \dots, \nu_s \} \). The block \( \A_{rs} \) is what survives when we keep only the rows in \( I_r \) and the columns in \( J_s \), renumbered from \( 1 \). Conformability says that the vertical lines through \( \A \) sit at the same places as the horizontal lines through \( \B \). That is exactly what will make each product "block of \( \A \) times block of \( \B \)" defined.

**Well-definedness.** The runs \( I_1, \dots, I_a \) are disjoint and cover \( \{1, \dots, m\} \), and the same holds for \( J_1, \dots, J_b \). So every entry of \( \A \) lies in exactly one block. Conversely, if we are given matrices \( \A_{rs} \in M_{m_r \times n_s}(F) \), there is exactly one \( \A \in M_{m \times n}(F) \) with these blocks. Block sizes must fit: all blocks in block row \( r \) have \( m_r \) rows, and all blocks in block column \( s \) have \( n_s \) columns. We allow only positive parts, so no block is empty.

**Examples.**

- **Every entry a block.** With \( m_r = 1 \) and \( n_s = 1 \) for all \( r, s \), the block \( \A_{rs} \) is the \( 1 \times 1 \) matrix \( (a_{rs}) \). A matrix is its own finest block matrix.
- **One block.** With \( a = b = 1 \), the single block is \( \A \) itself. This degenerate partition matters because a statement about block matrices then says something about ordinary matrices, and the statement must not break.
- **Columns as blocks.** Row partition \( m \), column partition \( 1, 1, \dots, 1 \). The blocks are the \( n \) columns of \( \A \): \( \A = \begin{pmatrix} \a_1 & \cdots & \a_n \end{pmatrix} \), as in Chapter 0.
- **The hook.** For \( \M \) and \( \N \) above, both partitions are \( 2, 2 \), so the column partition of \( \M \) equals the row partition of \( \N \): they are conformable.

**Non-example by minimal change.** Keep \( \M \) with column partition \( 2, 2 \), but cut \( \N \) with row partition \( 1, 3 \). The product \( \M \N \) is still defined, and both partitions are legitimate. What fails is conformability: the first block column of \( \M \) has \( 2 \) columns, while the first block row of \( \N \) has \( 1 \) row, so the "product" \( \A \cdot \N_{11} \) of a \( 2 \times 2 \) matrix with a \( 1 \times 2 \) matrix is undefined.

::: {.check}
Let \( \A \in M_{3 \times 5}(F) \) have row partition \( 1, 2 \) and column partition \( 3, 2 \), and let \( \B \in M_{5 \times 4}(F) \) have row partition \( 2, 3 \). Are the partitions conformable? What are the sizes of the blocks \( \A_{21} \) and \( \B_{2t} \)?
:::

::: {.solution}
No. The column partition of \( \A \) is \( 3, 2 \) and the row partition of \( \B \) is \( 2, 3 \). Both lists sum to \( 5 \), but they differ in order, and conformability asks for the same list. The block \( \A_{21} \) is \( 2 \times 3 \) (block row \( 2 \) has \( 2 \) rows, block column \( 1 \) has \( 3 \) columns), and every \( \B_{2t} \) has \( 3 \) rows.
:::

## Block multiplication

Here is the theorem that justifies the computation in the hook. The proof is nothing but the entry formula for a product, with the sum over the middle index cut into the runs \( J_1, \dots, J_b \).

::: {#thm-block-multiplication}
[Block Multiplication]

Let \( \A \in M_{m \times n}(F) \) and \( \B \in M_{n \times p}(F) \) be conformably partitioned: \( \A \) with row partition \( m_1, \dots, m_a \) and column partition \( n_1, \dots, n_b \), and \( \B \) with row partition \( n_1, \dots, n_b \) and column partition \( p_1, \dots, p_c \). Partition \( \A \B \in M_{m \times p}(F) \) with row partition \( m_1, \dots, m_a \) and column partition \( p_1, \dots, p_c \). Then for all \( 1 \le r \le a \) and \( 1 \le t \le c \),
\[
(\A \B)_{rt} = \sum_{s=1}^{b} \A_{rs}\B_{st} = \A_{r1}\B_{1t} + \A_{r2}\B_{2t} + \dots + \A_{rb}\B_{bt} .
\]
Each product \( \A_{rs}\B_{st} \) is defined and lies in \( M_{m_r \times p_t}(F) \).
:::

::: {.idea}
Look at one entry of \( \A \B \), in row \( i^* \) and column \( k^* \). It is a sum over the middle index \( j = 1, \dots, n \). Cut that sum into the runs \( J_1, \dots, J_b \) given by the common partition. The part over \( J_s \) pairs row \( i^* \) of \( \A \), restricted to the columns of block column \( s \), with column \( k^* \) of \( \B \), restricted to the rows of block row \( s \). That is one entry of \( \A_{rs}\B_{st} \). The only real work is translating indices between the big matrix and the blocks.
:::

::: {.proof}
Let \( \mu_r, \nu_s, \rho_t \) be the partial sums of the three partitions, as in @def-block-partition, and \( J_s = \{ \nu_{s-1} + 1, \dots, \nu_s \} \). The block \( \A_{rs} \) is \( m_r \times n_s \) and \( \B_{st} \) is \( n_s \times p_t \), so their product is defined and is \( m_r \times p_t \), as is the block \( (\A \B)_{rt} \).

Fix \( r, t \), and let \( 1 \le i \le m_r \) and \( 1 \le k \le p_t \). Put \( i^* = \mu_{r-1} + i \) and \( k^* = \rho_{t-1} + k \). By @def-block-partition and @def-matrix-multiplication,
\[
\big((\A \B)_{rt}\big)_{ik} = (\A \B)_{i^*k^*} = \sum_{j=1}^{n} a_{i^*j}\,b_{jk^*} .
\]
The sets \( J_1, \dots, J_b \) are disjoint with union \( \{1, \dots, n\} \), so the finite sum may be grouped according to them. In the group for \( J_s \), substitute \( j = \nu_{s-1} + l \); as \( l \) runs through \( 1, \dots, n_s \), \( j \) runs through \( J_s \) exactly once. Hence
\[
\begin{aligned}
\big((\A \B)_{rt}\big)_{ik}
  &= \sum_{s=1}^{b} \sum_{j \in J_s} a_{i^*j}\,b_{jk^*} \\
  &= \sum_{s=1}^{b} \sum_{l=1}^{n_s} a_{\mu_{r-1}+i,\ \nu_{s-1}+l}\ b_{\nu_{s-1}+l,\ \rho_{t-1}+k} \\
  &= \sum_{s=1}^{b} \sum_{l=1}^{n_s} (\A_{rs})_{il}\,(\B_{st})_{lk},
\end{aligned}
\]
where the last step is the definition of the blocks \( \A_{rs} \) and \( \B_{st} \). By @def-matrix-multiplication the inner sum is \( (\A_{rs}\B_{st})_{ik} \), and by @def-matrix-addition the outer sum is the \( (i, k) \)-entry of \( \sum_s \A_{rs}\B_{st} \). Since \( i \) and \( k \) were arbitrary, \( (\A \B)_{rt} = \sum_s \A_{rs}\B_{st} \). This proves the theorem.
:::

So conformably partitioned matrices multiply like matrices whose entries are matrices. The commonest case is a \( 2 \times 2 \) block matrix:
\[
\begin{pmatrix} \A & \B \\ \C & \D \end{pmatrix}\begin{pmatrix} \A' & \B' \\ \C' & \D' \end{pmatrix} = \begin{pmatrix} \A \A' + \B \C' & \A \B' + \B \D' \\ \C \A' + \D \C' & \C \B' + \D \D' \end{pmatrix},
\]
whenever the partitions are conformable. Sums and scalar multiples of matrices with the same partition are also computed blockwise, straight from @def-matrix-addition and @def-scalar-multiplication, since each entry lies in exactly one block.

**Over a commutative ring.** The proof uses only sums and products of entries and the regrouping of a finite sum. So block multiplication holds verbatim for matrices with entries in any commutative ring \( R \) in the sense of Chapter 7 §4, for instance \( R = F[x] \). Section 3 uses this.

::: {.warning}
**Keep the order inside every block product.** The top-left block of the product above is \( \A \A' + \B \C' \), not \( \A'\A + \C'\B \): blocks are matrices, and matrices do not commute. In the hook, \( \C \E + \D \G = \begin{pmatrix} 2 & 2 \\ 4 & 0 \end{pmatrix} \), while \( \E \C + \G \D = \begin{pmatrix} 0 & 0 \\ 4 & 2 \end{pmatrix} \). For the same reason, the formula \( ad - bc \) for a \( 2 \times 2 \) determinant does **not** survive with blocks: in general \( \det\begin{pmatrix} \A & \B \\ \C & \D \end{pmatrix} \ne \det(\A \D - \B \C) \). Take \( \A = \I_2 \), \( \B = \E_{12} \), \( \C = \E_{21} \), \( \D = \E_{11} \) in \( M_2(\nQ) \). Then \( \A \D - \B \C = \E_{11} - \E_{12}\E_{21} = \E_{11} - \E_{11} = 0 \), with determinant \( 0 \). But
\[
\M = \begin{pmatrix} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix},
\]
and subtracting row \( 4 \) from row \( 1 \), which does not change the determinant (@thm-det-row-operations), gives the permutation matrix that swaps \( \e_1 \) and \( \e_4 \), whose determinant is \( -1 \). So \( \det \M = -1 \ne 0 \). Section 3 shows that the formula does hold when \( \C \) and \( \D \) commute; here \( \C \D = \E_{21} \ne 0 = \D \C \).
:::

Transposing a block matrix transposes each block and reflects the array of blocks.

::: {#prp-block-transpose}
[Transpose of a Block Matrix]

Let \( \A \in M_{m \times n}(F) \) have row partition \( m_1, \dots, m_a \), column partition \( n_1, \dots, n_b \) and blocks \( \A_{rs} \). Give \( \A\tp \) the row partition \( n_1, \dots, n_b \) and the column partition \( m_1, \dots, m_a \). Then \( (\A\tp)_{sr} = (\A_{rs})\tp \). In particular \( \begin{pmatrix} \A & \B \\ \C & \D \end{pmatrix}\tp = \begin{pmatrix} \A\tp & \C\tp \\ \B\tp & \D\tp \end{pmatrix} \).
:::

::: {.proof}
For \( 1 \le j \le n_s \) and \( 1 \le i \le m_r \), by @def-block-partition and @def-transpose, \( \big((\A\tp)_{sr}\big)_{ji} = (\A\tp)_{\nu_{s-1}+j,\ \mu_{r-1}+i} = a_{\mu_{r-1}+i,\ \nu_{s-1}+j} = (\A_{rs})_{ij} = \big((\A_{rs})\tp\big)_{ji} \).
:::

## Rows, columns and outer products

The finest and coarsest partitions turn @thm-block-multiplication into facts we already know, and one mixed choice gives something new.

Partition \( \A \in M_{m \times n}(F) \) trivially (one block) and \( \B \in M_{n \times p}(F) \) into columns (row partition \( n \), column partition \( 1, \dots, 1 \)). These are conformable, and the theorem says that the \( k \)-th block of \( \A \B \), its \( k \)-th column, is \( \A\b_k \). That is the column view of @thm-three-views-of-product. Partitioning \( \A \) into rows and \( \B \) trivially gives the row view in the same way.

Now cut \( \A \) into columns and \( \B \) into rows. Both middle partitions are \( 1, 1, \dots, 1 \) (with \( n \) ones), so they are conformable, and the product has a single block.

::: {#cor-outer-product-expansion}
[Outer Product Expansion]

Let \( \A \in M_{m \times n}(F) \) have columns \( \a_1, \dots, \a_n \in F^m \), and let \( \B \in M_{n \times p}(F) \) have rows \( \r_1, \dots, \r_n \in M_{1 \times p}(F) \). Then
\[
\A \B = \a_1\r_1 + \a_2\r_2 + \dots + \a_n\r_n = \sum_{k=1}^{n} \a_k\r_k ,
\]
where each \( \a_k\r_k \in M_{m \times p}(F) \) is column \( k \) of \( \A \) times row \( k \) of \( \B \).
:::

::: {.proof}
Give \( \A \) the row partition \( m \) and the column partition \( 1, \dots, 1 \), so that its blocks are \( \A_{1k} = \a_k \); give \( \B \) the row partition \( 1, \dots, 1 \) and the column partition \( p \), so that \( \B_{k1} = \r_k \). The partitions are conformable, and by @thm-block-multiplication the single block of \( \A \B \) is \( \sum_{k} \A_{1k}\B_{k1} = \sum_k \a_k\r_k \).
:::

Each term \( \a_k\r_k \) is a column times a row, an **outer product**, and it has rank at most \( 1 \): its columns are the multiples \( r_{kj}\a_k \) of the single vector \( \a_k \). So the corollary writes every product of an \( m \times n \) and an \( n \times p \) matrix as a sum of \( n \) matrices of rank at most one, in the spirit of @exr-rank-factorization-b3, which writes a matrix of rank \( r \) as a sum of \( r \) rank-one matrices. For example,
\[
\begin{aligned}
&\begin{pmatrix} 1 & 2 \\ 3 & 4 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 & 2 \\ -1 & 1 & 1 \end{pmatrix} \\
&\qquad = \begin{pmatrix} 1 \\ 3 \\ 0 \end{pmatrix}\begin{pmatrix} 1 & 0 & 2 \end{pmatrix} + \begin{pmatrix} 2 \\ 4 \\ 1 \end{pmatrix}\begin{pmatrix} -1 & 1 & 1 \end{pmatrix} \\
&\qquad = \begin{pmatrix} 1 & 0 & 2 \\ 3 & 0 & 6 \\ 0 & 0 & 0 \end{pmatrix} + \begin{pmatrix} -2 & 2 & 2 \\ -4 & 4 & 4 \\ -1 & 1 & 1 \end{pmatrix} \\
&\qquad = \begin{pmatrix} -1 & 2 & 4 \\ -1 & 4 & 10 \\ -1 & 1 & 1 \end{pmatrix},
\end{aligned}
\]
which is the product computed entry by entry.

## Block diagonal matrices

Diagonal matrices are the easiest matrices to compute with: they multiply, power and invert entry by entry along the diagonal. Replace the diagonal entries by square blocks and all of this survives, one block at a time.

*A block diagonal matrix is several square matrices placed corner to corner along the diagonal, with zeros everywhere else.*

::: {#def-block-diagonal}
[Block Diagonal Matrix]

Let \( k_1, \dots, k_r \) be positive integers and \( \A_i \in M_{k_i}(F) \) **square** for each \( i \). Their **direct sum** \( \A_1 \oplus \dots \oplus \A_r \) is the matrix in \( M_{k_1 + \dots + k_r}(F) \) which, with row partition and column partition both equal to \( k_1, \dots, k_r \), has \( (i, i) \) block \( \A_i \) and \( (i, j) \) block \( 0 \) for \( i \ne j \). A square matrix is **block diagonal with respect to** the partition \( k_1, \dots, k_r \) if it has this form. For two blocks,
\[
\A \oplus \B = \begin{pmatrix} \A & 0 \\ 0 & \B \end{pmatrix}.
\]
:::

In words: the same partition is used for rows and columns, so the diagonal blocks are square; the blocks on the diagonal may be anything; every block off the diagonal is zero. Whether a matrix is block diagonal depends on the partition, which is part of the statement.

**Examples.**

- **Diagonal matrices.** \( \diag(d_1, \dots, d_n) = (d_1) \oplus \dots \oplus (d_n) \), with all \( k_i = 1 \).
- **The identity.** \( \I_k \oplus \I_l = \I_{k+l} \), and more generally \( \I_k \oplus 0_l \) is the matrix of a projection (@cor-projection-matrix).
- **A genuine block.** \( \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \oplus (2) = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix} \), with partition \( 2, 1 \).
- **One block.** With \( r = 1 \), \( \A_1 \) itself. Every square matrix is block diagonal with respect to the trivial partition, which is why the partition must always be named.

**Non-example by minimal change.** Change the \( (1, 3) \)-entry of the third example from \( 0 \) to \( 1 \). The partition \( 2, 1 \) still has square diagonal blocks \( \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) and \( (2) \), and the \( (2, 1) \) block \( \begin{pmatrix} 0 & 0 \end{pmatrix} \) is still zero. What fails is the clause that the \( (1, 2) \) block is zero: it is now \( \begin{pmatrix} 1 \\ 0 \end{pmatrix} \). The matrix is block upper triangular, which is treated below, but not block diagonal for this partition.

**Why the symbol \( \oplus \).** The matrix \( \A \oplus \B \) acts on \( F^{k+l} = \Span(\e_1, \dots, \e_k) \oplus \Span(\e_{k+1}, \dots, \e_{k+l}) \) by sending each of the two summands into itself, acting as \( \A \) on the first and as \( \B \) on the second. The theorem on adapted bases below makes this precise for any operator and any direct sum, and it is the reason the same symbol is used.

::: {.warning}
**\( \A \oplus \B \) is a matrix, not a subspace, and the order matters.** For subspaces, \( U \oplus W \) and \( W \oplus U \) are the same set. For matrices, \( (1) \oplus (2) = \diag(1, 2) \) and \( (2) \oplus (1) = \diag(2, 1) \) are different matrices. They are similar (swap the two basis vectors), but they are not equal.
:::

::: {#thm-block-diagonal-arithmetic}
[Arithmetic of Block Diagonal Matrices]

Let \( \A, \A' \in M_k(F) \), \( \B, \B' \in M_l(F) \) and \( c \in F \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( (\A \oplus \B) + (\A' \oplus \B') = (\A + \A') \oplus (\B + \B') \), \( c(\A \oplus \B) = c\A \oplus c\B \), and \( (\A \oplus \B)(\A' \oplus \B') = \A \A' \oplus \B \B' \);
2. \( (\A \oplus \B)^j = \A^j \oplus \B^j \) for every \( j \in \nN \), and \( p(\A \oplus \B) = p(\A) \oplus p(\B) \) for every \( p \in F[x] \);
3. \( \A \oplus \B \) is invertible if and only if \( \A \) and \( \B \) are both invertible, and then \( (\A \oplus \B)^{-1} = \A^{-1} \oplus \B^{-1} \);
4. \( \det(\A \oplus \B) = \det \A \det \B \) and \( \tr(\A \oplus \B) = \tr \A + \tr \B \).
:::
:::

::: {.proof}
(a) Sums and scalar multiples are computed blockwise, and by @thm-block-multiplication the product has blocks \( \A \A' + 0 \cdot 0 = \A \A' \), \( \A0 + 0\B' = 0 \), \( 0\A' + \B0 = 0 \) and \( 0 \cdot 0 + \B \B' = \B \B' \).

(b) By induction on \( j \). For \( j = 0 \), \( (\A \oplus \B)^0 = \I_{k+l} = \I_k \oplus \I_l \) by @def-polynomial-of-matrix. If \( (\A \oplus \B)^j = \A^j \oplus \B^j \), then \( (\A \oplus \B)^{j+1} = (\A^j \oplus \B^j)(\A \oplus \B) = \A^{j+1} \oplus \B^{j+1} \) by (a). For \( p = \sum_j c_jx^j \), (a) gives \( p(\A \oplus \B) = \sum_j c_j(\A^j \oplus \B^j) = \big(\sum_j c_j\A^j\big) \oplus \big(\sum_j c_j\B^j\big) = p(\A) \oplus p(\B) \).

(d) The matrix \( \A \oplus \B \) is block upper triangular with square diagonal blocks, so \( \det(\A \oplus \B) = \det \A \det \B \) by @thm-det-block-triangular. Its diagonal entries are those of \( \A \) followed by those of \( \B \), so the traces add (@def-trace).

(c) \( (\Leftarrow) \) By (a), \( (\A \oplus \B)(\A^{-1} \oplus \B^{-1}) = \I_k \oplus \I_l = \I_{k+l} \), so by @thm-one-sided-inverse \( \A \oplus \B \) is invertible with inverse \( \A^{-1} \oplus \B^{-1} \). \( (\Rightarrow) \) If \( \A \oplus \B \) is invertible, then \( \det \A \det \B \ne 0 \) by (d) and @thm-det-nonzero-iff-invertible. A product in a field is non-zero only if both factors are (@thm-field-basic-properties (d)), so \( \det \A \ne 0 \ne \det \B \), and both are invertible by @thm-det-nonzero-iff-invertible.
:::

By induction on the number of blocks, the same rules hold for \( \A_1 \oplus \dots \oplus \A_r \): everything is done block by block. For instance \( \big(\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \oplus (2)\big)^{5} = \begin{pmatrix} 1 & 5 \\ 0 & 1 \end{pmatrix} \oplus (32) \), since \( \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}^{j} = \begin{pmatrix} 1 & j \\ 0 & 1 \end{pmatrix} \) by induction.

## Block triangular matrices

Allow one more non-zero block: \( \M = \begin{pmatrix} \A & \B \\ 0 & \D \end{pmatrix} \) with \( \A \in M_k(F) \), \( \D \in M_l(F) \) square and \( \B \in M_{k \times l}(F) \). Such a matrix is **block upper triangular**; with the zero block above the diagonal instead, **block lower triangular**. Chapter 7 computed \( \det \M = \det \A\det \D \) (@thm-det-block-triangular). Products and inverses keep the shape.

::: {#thm-block-triangular-inverse}
[Block Triangular Products and Inverses]

Let \( k, l \ge 1 \), and let \( \M = \begin{pmatrix} \A & \B \\ 0 & \D \end{pmatrix} \) and \( \M' = \begin{pmatrix} \A' & \B' \\ 0 & \D' \end{pmatrix} \), with \( \A, \A' \in M_k(F) \), \( \D, \D' \in M_l(F) \) and \( \B, \B' \in M_{k \times l}(F) \).

::: {.enumerate options="label=(\alph*)"}
1. \( \M \M' = \begin{pmatrix} \A \A' & \A \B' + \B \D' \\ 0 & \D \D' \end{pmatrix} \); in particular it is block upper triangular.
2. \( \M \) is invertible if and only if \( \A \) and \( \D \) are both invertible.
3. In that case
\[
\M^{-1} = \begin{pmatrix} \A^{-1} & -\A^{-1}\B \D^{-1} \\ 0 & \D^{-1} \end{pmatrix}.
\]
:::
:::

::: {.idea}
Where does the formula come from? Solve \( \M\begin{pmatrix} \x \\ \y \end{pmatrix} = \begin{pmatrix} \f \\ \g \end{pmatrix} \) by back substitution with blocks. The second block row says \( \D\y = \g \), so \( \y = \D^{-1}\g \). The first says \( \A\x + \B\y = \f \), so \( \x = \A^{-1}\f - \A^{-1}\B \D^{-1}\g \). Reading off the coefficients of \( \f \) and \( \g \) gives the four blocks of \( \M^{-1} \). The proof only has to check the answer.
:::

::: {.proof}
(a) By @thm-block-multiplication, the blocks of \( \M \M' \) are \( \A \A' + \B0 = \A \A' \), \( \A \B' + \B \D' \), \( 0\A' + \D0 = 0 \) and \( 0\B' + \D \D' = \D \D' \).

(b) By @thm-det-block-triangular, \( \det \M = \det \A\det \D \). By @thm-det-nonzero-iff-invertible, \( \M \) is invertible if and only if \( \det \A\det \D \ne 0 \), which in a field happens exactly when \( \det \A \ne 0 \) and \( \det \D \ne 0 \) (@thm-field-basic-properties (f) and (d)), that is, when \( \A \) and \( \D \) are both invertible.

(c) Let \( \X \) be the displayed matrix. By (a) with \( \A' = \A^{-1} \), \( \B' = -\A^{-1}\B \D^{-1} \) and \( \D' = \D^{-1} \),
\[
\M \X = \begin{pmatrix} \A \A^{-1} & -\A \A^{-1}\B \D^{-1} + \B \D^{-1} \\ 0 & \D \D^{-1} \end{pmatrix} = \begin{pmatrix} \I_k & 0 \\ 0 & \I_l \end{pmatrix} = \I_{k+l} .
\]
By @thm-one-sided-inverse, \( \X = \M^{-1} \).
:::

Transposing with @prp-block-transpose turns this into the lower triangular version: if \( \A \) and \( \D \) are invertible, then \( \begin{pmatrix} \A & 0 \\ \C & \D \end{pmatrix}^{-1} = \begin{pmatrix} \A^{-1} & 0 \\ -\D^{-1}\C \A^{-1} & \D^{-1} \end{pmatrix} \). A special case is used constantly: \( \begin{pmatrix} \I_k & \X \\ 0 & \I_l \end{pmatrix}^{-1} = \begin{pmatrix} \I_k & -\X \\ 0 & \I_l \end{pmatrix} \) for every \( \X \in M_{k \times l}(F) \). Adding \( \X \) times the second block of coordinates to the first is undone by subtracting it.

::: {.check}
The matrix \( \M = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix} \), with row partition \( 2, 1 \) and column partition \( 1, 2 \), has a zero lower-left block and is invertible. Does this contradict @thm-block-triangular-inverse?
:::

::: {.solution}
No. The theorem needs the diagonal blocks square, which means equal row and column partitions. Here the top-left block \( \begin{pmatrix} 1 \\ 0 \end{pmatrix} \) is \( 2 \times 1 \) and the bottom-right block \( \begin{pmatrix} 1 & 0 \end{pmatrix} \) is \( 1 \times 2 \), so "\( \A \) is invertible" does not even make sense. (The lower-left block is the \( 1 \times 1 \) entry in position \( (3, 1) \), which is \( 0 \).)
:::

## Matrices of operators in adapted bases

Now the shapes pay off. For an operator \( T \in \cL(V) \) and a subspace \( U \subseteq V \), we say that **\( T \) maps \( U \) into \( U \)** if \( T\u \in U \) for every \( \u \in U \). Then the **restriction** \( T|_U \colon U \to U \), \( \u \mapsto T\u \), is an operator on \( U \), linear because its values are those of \( T \). Such subspaces are the subject of Chapter 9; here we only ask what they do to the matrix of \( T \).

When \( V = U \oplus W \) and a basis of \( U \) is followed by a basis of \( W \), the combined list is a basis of \( V \) (@thm-direct-sum-k-criteria), which we call **adapted** to the decomposition. If \( T \) maps both pieces into themselves, the matrix splits.

::: {#thm-direct-sum-block-diagonal}
[Direct Sums Give Block Diagonal Matrices]

Let \( V = U \oplus W \) be finite-dimensional with \( U \ne \{\0\} \ne W \), let \( \sB_U = (\u_1, \dots, \u_k) \) and \( \sB_W = (\w_1, \dots, \w_l) \) be bases of \( U \) and \( W \), and let \( \sB = (\u_1, \dots, \u_k, \w_1, \dots, \w_l) \). For \( T \in \cL(V) \), the following are equivalent:

::: {.enumerate options="label=(\alph*)"}
1. \( T \) maps \( U \) into \( U \) and \( W \) into \( W \);
2. \( \mtx{T}{\sB}{\sB} \) is block diagonal with respect to the partition \( k, l \).
:::

In that case \( \mtx{T}{\sB}{\sB} = \mtx{T|_U}{\sB_U}{\sB_U} \oplus \mtx{T|_W}{\sB_W}{\sB_W} \).
:::

::: {.proof}
By @thm-direct-sum-k-criteria, \( \sB \) is a basis of \( V \). By @def-matrix-of-linear-map, column \( j \le k \) of \( \mtx{T}{\sB}{\sB} \) holds the coordinates of \( T\u_j \), and column \( k + q \) those of \( T\w_q \).

(a) \( \Rightarrow \) (b). Since \( T\u_j \in U = \Span(\sB_U) \), write \( T\u_j = \sum_{i} a_{ij}\u_i \). By uniqueness of coordinates (@thm-unique-representation), the last \( l \) entries of column \( j \) are \( 0 \) and the first \( k \) are \( a_{1j}, \dots, a_{kj} \), which is column \( j \) of \( \mtx{T|_U}{\sB_U}{\sB_U} \). In the same way \( T\w_q = \sum_p d_{pq}\w_p \), so column \( k + q \) is \( 0 \) in its first \( k \) entries and equals column \( q \) of \( \mtx{T|_W}{\sB_W}{\sB_W} \) in its last \( l \). This shows \( \mtx{T}{\sB}{\sB} = \mtx{T|_U}{\sB_U}{\sB_U} \oplus \mtx{T|_W}{\sB_W}{\sB_W} \).

(b) \( \Rightarrow \) (a). If the \( (2, 1) \) block is zero, then the coordinates of each \( T\u_j \) vanish in the last \( l \) places, so \( T\u_j \in \Span(\sB_U) = U \). For \( \u = \sum_j c_j\u_j \in U \), linearity gives \( T\u = \sum_j c_jT\u_j \in U \), since \( U \) is a subspace. The \( (1, 2) \) block being zero gives \( T\w_q \in W \) in the same way, and hence \( T \) maps \( W \) into \( W \).
:::

For example, let \( T = \frac{d^2}{dx^2} \) on \( \nR[x]_{\le 3} = U \oplus W \) with \( U = \Span(1, x^2) \) (even polynomials) and \( W = \Span(x, x^3) \) (odd polynomials). Since \( T(1) = 0 \), \( T(x^2) = 2 \), \( T(x) = 0 \) and \( T(x^3) = 6x \), \( T \) maps each piece into itself, and in the basis \( \sB = (1, x^2, x, x^3) \)
\[
\mtx{T}{\sB}{\sB} = \begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix} \oplus \begin{pmatrix} 0 & 6 \\ 0 & 0 \end{pmatrix}.
\]
In the standard order \( (1, x, x^2, x^3) \) the same operator has the matrix with \( 2 \) in position \( (1, 3) \) and \( 6 \) in position \( (2, 4) \), which is not block diagonal for the partition \( 2, 2 \). **Ordering the basis to match the decomposition is part of the method.**

If \( T \) maps only one subspace \( U \) into itself, we can still take a basis of \( U \) first, but the remaining basis vectors need not be sent anywhere special. What survives is a zero block in the lower left, and the lower-right block turns out to describe the operator that \( T \) induces on the quotient \( V/U \). This was @exr-products-and-quotients-c2 in Chapter 2; we now record it as a theorem, with its converse.

::: {#thm-invariant-subspace-block-triangular}
[Subspaces Mapped into Themselves Give Block Triangular Matrices]

Let \( V \) be finite-dimensional, \( T \in \cL(V) \), and \( U \) a subspace with \( \{\0\} \ne U \ne V \). Let \( \sB_U = (\u_1, \dots, \u_k) \) be a basis of \( U \), extended to a basis \( \sB = (\u_1, \dots, \u_k, \w_1, \dots, \w_l) \) of \( V \).

::: {.enumerate options="label=(\alph*)"}
1. \( T \) maps \( U \) into \( U \) if and only if the lower-left \( l \times k \) block of \( \mtx{T}{\sB}{\sB} \) is zero.
2. In that case the rule \( \bar T(\v + U) = T\v + U \) defines an operator \( \bar T \) on \( V/U \), and
\[
\mtx{T}{\sB}{\sB} = \begin{pmatrix} \mtx{T|_U}{\sB_U}{\sB_U} & \B \\ 0 & \mtx{\bar T}{\bar\sB}{\bar\sB} \end{pmatrix}
\]
for some \( \B \in M_{k \times l}(F) \), where \( \bar\sB = (\w_1 + U, \dots, \w_l + U) \) is a basis of \( V/U \).
:::
:::

::: {.idea}
Read the matrix one column at a time. The first \( k \) columns describe \( T\u_j \), which lie in \( U \) exactly when their \( \w \)-coordinates vanish. The last \( l \) columns describe \( T\w_q \), which may have any \( \u \)-part; passing to \( V/U \) erases that part and leaves precisely the \( \w \)-coordinates, which are the lower-right block.
:::

::: {.proof}
(a) Column \( j \le k \) of \( \mtx{T}{\sB}{\sB} \) is the coordinate vector of \( T\u_j \) (@def-matrix-of-linear-map), and by @thm-unique-representation its last \( l \) entries vanish if and only if \( T\u_j \in \Span(\u_1, \dots, \u_k) = U \). If \( T \) maps \( U \) into \( U \), this holds for every \( j \). Conversely, if it holds for every \( j \), then for \( \u = \sum_j c_j\u_j \in U \) we get \( T\u = \sum_j c_jT\u_j \in U \), because \( U \) is a subspace.

(b) Let \( \pi \colon V \to V/U \) be the quotient map, linear with kernel \( U \) (@thm-quotient-space-operations-well-defined). The composite \( \pi T \) is linear (@thm-composition-linear), and for \( \u \in U \), \( \pi(T\u) = \0 \) because \( T\u \in U \). So \( U \subseteq \ker(\pi T) \), and by @thm-quotient-universal-property (a) there is exactly one linear \( \bar T \colon V/U \to V/U \) with \( \bar T(\v + U) = T\v + U \). By @thm-dimension-quotient, \( \bar\sB \) is a basis of \( V/U \).

By (a), the lower-left block is zero, and as in the proof of @thm-direct-sum-block-diagonal, the upper-left block is \( \mtx{T|_U}{\sB_U}{\sB_U} \). For \( 1 \le q \le l \), write \( T\w_q = \sum_{i=1}^{k} b_{iq}\u_i + \sum_{p=1}^{l} d_{pq}\w_p \), so that column \( k + q \) of \( \mtx{T}{\sB}{\sB} \) is \( (b_{1q}, \dots, b_{kq}, d_{1q}, \dots, d_{lq}) \). Applying the linear map \( \pi \), and using \( \pi(\u_i) = \0 \),
\[
\bar T(\w_q + U) = \pi(T\w_q) = \sum_{p=1}^{l} d_{pq}\,(\w_p + U) .
\]
By @def-matrix-of-linear-map, column \( q \) of \( \mtx{\bar T}{\bar\sB}{\bar\sB} \) is \( (d_{1q}, \dots, d_{lq}) \), which is the lower-right part of column \( k + q \) of \( \mtx{T}{\sB}{\sB} \). This proves (b), with \( \B = (b_{iq}) \).
:::

The upper-left block depends only on the basis \( \sB_U \), and the lower-right block only on the cosets \( \w_1 + U, \dots, \w_l + U \). So replacing each \( \w_q \) by \( \w_q + \u'_q \) with \( \u'_q \in U \) can change the top-right block \( \B \), but leaves both diagonal blocks unchanged. The theorem splits \( T \) into two smaller operators, and every quantity that sees only diagonal blocks splits with it. By @thm-det-block-triangular, \( \det T = \det(T|_U)\det\bar T \). Applied over \( F[x] \) (Chapter 7 §8 notes that the block triangular determinant holds over any commutative ring), \( x\I - \mtx{T}{\sB}{\sB} = \begin{pmatrix} x\I_k - \mtx{T|_U}{\sB_U}{\sB_U} & -\B \\ 0 & x\I_l - \mtx{\bar T}{\bar\sB}{\bar\sB} \end{pmatrix} \) gives \( p_T = p_{T|_U}\,p_{\bar T} \). Chapter 9 builds on exactly this factorization.

::: {#exm-cyclic-shift-block-triangular}
[A Plane Mapped into Itself]

Let \( T \colon \nR^3 \to \nR^3 \), \( T(x, y, z) = (y, z, x) \), and \( U = \{ (x, y, z) : x + y + z = 0 \} \). Show that \( T \) maps \( U \) into \( U \), find \( \mtx{T}{\sB}{\sB} \) for the basis \( \sB = (\u_1, \u_2, \e_3) \) with \( \u_1 = (1, -1, 0) \), \( \u_2 = (0, 1, -1) \), and interpret the lower-right block.
:::

::: {.solution}
If \( x + y + z = 0 \), then the entries of \( T(x, y, z) = (y, z, x) \) also sum to \( 0 \), so \( T \) maps \( U \) into \( U \). The vectors \( \u_1, \u_2 \) lie in \( U \) and are independent (look at the first entries, then the last), and \( \dim U = 2 \) since \( U \) is the kernel of the non-zero functional \( (x, y, z) \mapsto x + y + z \) (@thm-rank-nullity). So \( (\u_1, \u_2) \) is a basis of \( U \) (@thm-right-size-basis), and \( \sB \) is a basis of \( \nR^3 \): in a relation \( a\u_1 + b\u_2 + c\e_3 = \0 \), the entries sum to \( c = 0 \), and then \( a = b = 0 \), so \( \sB \) is an independent list of \( 3 \) vectors (@thm-right-size-basis). Now
\[
\begin{aligned}
T\u_1 &= (-1, 0, 1) = -\u_1 - \u_2, \\
T\u_2 &= (1, -1, 0) = \u_1, \\
T\e_3 &= (0, 1, 0) = \u_2 + \e_3,
\end{aligned}
\]
so
\[
\mtx{T}{\sB}{\sB} = \left(\begin{array}{cc|c} -1 & 1 & 0 \\ -1 & 0 & 1 \\ \hline 0 & 0 & 1 \end{array}\right).
\]
The lower-left block is zero, as @thm-invariant-subspace-block-triangular predicts. The lower-right block \( (1) \) says \( \bar T(\e_3 + U) = \e_3 + U \), so \( \bar T \) is the identity on the line \( \nR^3/U \). Indeed \( T\v - \v = (y - x, z - y, x - z) \) has entries summing to \( 0 \), so \( T\v + U = \v + U \) for every \( \v \): \( T \) moves vectors, but never changes the sum of their coordinates, and that sum is all that \( \nR^3/U \) remembers.
:::

## Exercises

### A. Check your understanding

:::: {#exr-block-multiplication-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define what it means for partitions of \( \A \in M_{m \times n}(F) \) and \( \B \in M_{n \times p}(F) \) to be conformable.
2. State the block multiplication formula for \( \begin{pmatrix} \A & \B \\ \C & \D \end{pmatrix}\begin{pmatrix} \A' & \B' \\ \C' & \D' \end{pmatrix} \).
3. True or false: the top-left block of that product is \( \A'\A + \C'\B \). Justify your answer.
4. True or false: if \( \A \in M_k(F) \) and \( \B \in M_l(F) \), then \( \A \oplus \B = \B \oplus \A \). Justify your answer.
5. True or false: if \( \M = \begin{pmatrix} \A & \B \\ 0 & \D \end{pmatrix} \) with \( \A \), \( \D \) square is invertible, then \( \M^{-1} \) is block upper triangular. Justify your answer.
6. In a basis whose first \( k \) vectors form a basis of \( U \), what does a zero lower-left block of \( \mtx{T}{\sB}{\sB} \) say about \( T \)?
:::
::::

::: {.solution}
(a) The column partition of \( \A \) and the row partition of \( \B \) are the same list \( n_1, \dots, n_b \), in the same order (@def-block-partition).

(b) It is \( \begin{pmatrix} \A \A' + \B \C' & \A \B' + \B \D' \\ \C \A' + \D \C' & \C \B' + \D \D' \end{pmatrix} \), provided the partitions are conformable (@thm-block-multiplication).

(c) False in general. The block is \( \A \A' + \B \C' \), with each block of the left factor on the left. For \( 4 \times 4 \) matrices with partition \( 2, 2 \), take \( \A = \E_{12} \), \( \A' = \E_{21} \) in \( M_2(F) \) and all other blocks zero. Then the top-left block of the product is \( \A \A' = \E_{11} \), while \( \A'\A + \C'\B = \E_{22} \).

(d) False. For \( k = l = 1 \), \( (1) \oplus (2) = \diag(1, 2) \ne \diag(2, 1) = (2) \oplus (1) \).

(e) True. By @thm-block-triangular-inverse (b), \( \A \) and \( \D \) are invertible, and (c) gives \( \M^{-1} \) with lower-left block \( 0 \).

(f) That \( T \) maps \( U \) into \( U \) (@thm-invariant-subspace-block-triangular (a)).
:::

### B. Practice

:::: {#exr-block-multiplication-b1}
[B1: Multiplying block matrices]

Let
\[
\M = \left(\begin{array}{cc|c} 1 & 2 & 1 \\ 0 & 1 & -1 \\ \hline 2 & 0 & 3 \end{array}\right), \qquad \N = \left(\begin{array}{cc|c} 1 & 0 & 0 \\ 1 & 1 & 2 \\ \hline 1 & -1 & 1 \end{array}\right) \in M_3(\nQ),
\]
both with row and column partition \( 2, 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \M \N \) blockwise, and check one block against the entry formula.
2. Explain why the partitions would **not** be conformable if \( \N \) were given the row partition \( 1, 2 \) instead.
:::
::::

::: {.solution}
(a) Write \( \M = \begin{pmatrix} \A & \b \\ \c & d \end{pmatrix} \) and \( \N = \begin{pmatrix} \E & \f \\ \g & h \end{pmatrix} \) with \( \A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \), \( \b = \begin{pmatrix} 1 \\ -1 \end{pmatrix} \), \( \c = \begin{pmatrix} 2 & 0 \end{pmatrix} \), \( d = (3) \), \( \E = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} \), \( \f = \begin{pmatrix} 0 \\ 2 \end{pmatrix} \), \( \g = \begin{pmatrix} 1 & -1 \end{pmatrix} \), \( h = (1) \). The partitions are conformable (both middle partitions are \( 2, 1 \)), so by @thm-block-multiplication
\[
\begin{aligned}
\A \E + \b\g &= \begin{pmatrix} 3 & 2 \\ 1 & 1 \end{pmatrix} + \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 4 & 1 \\ 0 & 2 \end{pmatrix}, \\
\A\f + \b h &= \begin{pmatrix} 4 \\ 2 \end{pmatrix} + \begin{pmatrix} 1 \\ -1 \end{pmatrix} = \begin{pmatrix} 5 \\ 1 \end{pmatrix},
\end{aligned}
\]
\[
\c \E + d\g = \begin{pmatrix} 2 & 0 \end{pmatrix} + \begin{pmatrix} 3 & -3 \end{pmatrix} = \begin{pmatrix} 5 & -3 \end{pmatrix}, \qquad \c\f + dh = (0) + (3) = (3).
\]
Hence
\[
\M \N = \begin{pmatrix} 4 & 1 & 5 \\ 0 & 2 & 1 \\ 5 & -3 & 3 \end{pmatrix}.
\]
Check the \( (3, 3) \)-entry directly: row \( 3 \) of \( \M \) is \( (2, 0, 3) \) and column \( 3 \) of \( \N \) is \( (0, 2, 1) \), giving \( 0 + 0 + 3 = 3 \).

(b) The column partition of \( \M \) is \( 2, 1 \), and the row partition \( 1, 2 \) is a different list. Concretely, the top-left block \( \A \) of \( \M \) is \( 2 \times 2 \), while the top-left block of \( \N \) would be \( 1 \times 2 \), and a \( 2 \times 2 \) matrix cannot multiply a \( 1 \times 2 \) matrix.
:::

:::: {#exr-block-multiplication-b2}
[B2: Inverting a block triangular matrix]

Use @thm-block-triangular-inverse to find the inverse of
\[
\M = \begin{pmatrix} 2 & 1 & 1 & 0 \\ 1 & 1 & 2 & 1 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 1 \end{pmatrix} \in M_4(\nQ),
\]
and check one block of \( \M \M^{-1} \).
::::

::: {.solution}
With the partition \( 2, 2 \), \( \M = \begin{pmatrix} \A & \B \\ 0 & \D \end{pmatrix} \) with \( \A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \), \( \B = \begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix} \), \( \D = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \). Both \( \det \A = 1 \) and \( \det \D = 1 \) are non-zero, so by @thm-two-by-two-inverse
\[
\A^{-1} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}, \qquad \D^{-1} = \begin{pmatrix} 1 & -2 \\ 0 & 1 \end{pmatrix}.
\]
Then \( \A^{-1}\B = \begin{pmatrix} -1 & -1 \\ 3 & 2 \end{pmatrix} \) and \( -\A^{-1}\B \D^{-1} = -\begin{pmatrix} -1 & 1 \\ 3 & -4 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ -3 & 4 \end{pmatrix} \). By @thm-block-triangular-inverse (c),
\[
\M^{-1} = \begin{pmatrix} 1 & -1 & 1 & -1 \\ -1 & 2 & -3 & 4 \\ 0 & 0 & 1 & -2 \\ 0 & 0 & 0 & 1 \end{pmatrix}.
\]
Check the top-right block of \( \M \M^{-1} \):
\[
\begin{aligned}
\A(-\A^{-1}\B \D^{-1}) + \B \D^{-1}
  &= \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 1 & -1 \\ -3 & 4 \end{pmatrix} + \begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix}\begin{pmatrix} 1 & -2 \\ 0 & 1 \end{pmatrix} \\
  &= \begin{pmatrix} -1 & 2 \\ -2 & 3 \end{pmatrix} + \begin{pmatrix} 1 & -2 \\ 2 & -3 \end{pmatrix} = 0 ,
\end{aligned}
\]
as it must be.
:::

:::: {#exr-block-multiplication-b3}
[B3: A projection in an adapted basis]

Let \( \P = \begin{pmatrix} 0 & 1 & -1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \in M_3(\nR) \), \( U = \Span((1, 1, 0), (0, 1, 1)) \) and \( W = \Span(\e_1) \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \P^2 = \P \), that \( \P\u = \u \) for \( \u \in U \) and \( \P\e_1 = \0 \), and that \( \nR^3 = U \oplus W \).
2. Let \( \sB = ((1, 1, 0), (0, 1, 1), \e_1) \). Use @thm-direct-sum-block-diagonal to write down \( \mtx{T_{\P}}{\sB}{\sB} \) without computing, and confirm it as \( \S^{-1}\P \S \), where \( \S \) has the vectors of \( \sB \) as columns.
3. Hence find \( \P^{100} \) and \( \tr \P \).
:::
::::

::: {.solution}
(a) Multiplying, \( \P^2 \) has rows \( (0, 1, -1) \), \( (0, 1, 0) \), \( (0, 0, 1) \), so \( \P^2 = \P \). Also \( \P(1, 1, 0) = (1, 1, 0) \), \( \P(0, 1, 1) = (0, 1, 1) \) and \( \P\e_1 = \0 \) (the first column is zero), so \( \P \) fixes every vector of \( U \) by linearity. The three vectors of \( \sB \) are the columns of \( \S = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 0 \end{pmatrix} \), and expanding along the last column, \( \det \S = 1 \cdot (1 - 0) = 1 \ne 0 \). So \( \S \) is invertible (@thm-det-nonzero-iff-invertible), its columns form a basis of \( \nR^3 \) (@thm-invertible-tfae), and \( \nR^3 = U \oplus W \) by @thm-direct-sum-k-criteria.

(b) \( T_{\P} \) maps \( U \) into \( U \) (as the identity) and \( W \) into \( W \) (as zero). By @thm-direct-sum-block-diagonal, \( \mtx{T_{\P}}{\sB}{\sB} = \I_2 \oplus (0) = \diag(1, 1, 0) \). By @thm-change-of-basis-maps, \( \mtx{T_{\P}}{\sB}{\sB} = \S^{-1}\P \S \). Here \( \S^{-1} = \begin{pmatrix} 0 & 1 & -1 \\ 0 & 0 & 1 \\ 1 & -1 & 1 \end{pmatrix} \) (check \( \S \S^{-1} = \I_3 \)), and \( \P \S \) has columns \( \P(1, 1, 0) = (1, 1, 0) \), \( \P(0, 1, 1) = (0, 1, 1) \), \( \P\e_1 = \0 \), so \( \S^{-1}\P \S = \S^{-1}\begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 1 & 0 \end{pmatrix} = \diag(1, 1, 0) \).

(c) \( \P = \S\diag(1, 1, 0)\S^{-1} \), so \( \P^{100} = \S\diag(1, 1, 0)^{100}\S^{-1} = \S\diag(1, 1, 0)\S^{-1} = \P \) by @thm-block-diagonal-arithmetic (b) (or directly from \( \P^2 = \P \)). By @thm-trace-similarity-invariant, \( \tr \P = \tr\diag(1, 1, 0) = 2 \), which matches \( 0 + 1 + 1 \).
:::

### C. Going deeper

:::: {#exr-block-multiplication-c1}
[C1: Square-zero matrices of half rank]

Let \( n \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. For \( \X \in M_n(F) \), let \( \N_{\X} = \begin{pmatrix} 0 & \X \\ 0 & 0 \end{pmatrix} \in M_{2n}(F) \). Show that \( \N_{\X}^2 = 0 \) and that \( \rank \N_{\X} = \rank \X \).
2. Let \( V \) have dimension \( 2n \), and let \( T \in \cL(V) \) satisfy \( T^2 = 0 \) and \( \rank T = n \). Show that \( \im T = \ker T \). Choose \( \w_1, \dots, \w_n \) with \( (T\w_1, \dots, T\w_n) \) a basis of \( \im T \), and put \( \u_i = T\w_i \). Prove that \( \sB = (\u_1, \dots, \u_n, \w_1, \dots, \w_n) \) is a basis of \( V \) and that \( \mtx{T}{\sB}{\sB} = \N_{\I_n} \).
3. Deduce that for every invertible \( \X \in M_n(F) \), the matrix \( \N_{\X} \) is similar to \( \N_{\I_n} \).
:::

*Hint: for the independence in (b), apply \( T \).*
::::

::: {.solution}
(a) By @thm-block-multiplication, \( \N_{\X}^2 = \begin{pmatrix} 0 \cdot 0 + \X \cdot 0 & 0 \cdot \X + \X \cdot 0 \\ 0 & 0 \end{pmatrix} = 0 \). The first \( n \) columns of \( \N_{\X} \) are zero, and column \( n + j \) is \( \begin{pmatrix} \x_j \\ \0 \end{pmatrix} \), where \( \x_j \) is column \( j \) of \( \X \). A combination \( \sum_j c_j\begin{pmatrix} \x_j \\ \0 \end{pmatrix} \) is zero exactly when \( \sum_j c_j\x_j = \0 \), so a list of these columns is independent exactly when the corresponding columns of \( \X \) are. Hence \( \dim\col(\N_{\X}) = \dim\col(\X) \), that is, \( \rank \N_{\X} = \rank \X \).

(b) If \( \v = T\x \in \im T \), then \( T\v = T^2\x = \0 \), so \( \im T \subseteq \ker T \). By @thm-rank-nullity, \( \dim\ker T = 2n - n = n = \dim\im T \), so \( \im T = \ker T \) by @thm-dim-impl-eq. The vectors \( \w_i \) exist because \( (T\w_1, \dots, T\w_n) \) can be any basis of \( \im T \), each of whose vectors is \( T \) of something.

Let \( \sum_i a_i\u_i + \sum_i b_i\w_i = \0 \). Applying \( T \), and using \( T\u_i = T^2\w_i = \0 \), gives \( \sum_i b_i\u_i = \0 \). The \( \u_i \) form a basis of \( \im T \), so all \( b_i = 0 \), and then \( \sum_i a_i\u_i = \0 \) gives all \( a_i = 0 \). So \( \sB \) is a linearly independent list of \( 2n = \dim V \) vectors, hence a basis (@thm-right-size-basis). Since \( T\u_i = \0 \) and \( T\w_i = \u_i \), column \( i \le n \) of \( \mtx{T}{\sB}{\sB} \) is zero and column \( n + i \) is \( \e_i \). So \( \mtx{T}{\sB}{\sB} = \begin{pmatrix} 0 & \I_n \\ 0 & 0 \end{pmatrix} = \N_{\I_n} \).

(c) If \( \X \) is invertible, then by (a) the operator \( T = T_{\N_{\X}} \) on \( F^{2n} \) satisfies \( T^2 = 0 \) and \( \rank T = \rank \N_{\X} = \rank \X = n \) (@thm-rank-map-equals-rank-matrix, and @thm-invertible-tfae for \( \rank \X = n \)). By (b) there is a basis \( \sB \) with \( \mtx{T}{\sB}{\sB} = \N_{\I_n} \). The matrix of \( T \) in the standard basis is \( \N_{\X} \), so \( \N_{\X} \) and \( \N_{\I_n} \) are similar by @thm-similar-iff-same-operator.
:::

:::: {#exr-block-multiplication-c2}
[C2: Powers of block triangular matrices]

Let \( \A \in M_k(F) \), \( \D \in M_l(F) \) and \( \B \in M_{k \times l}(F) \), and let \( \M = \begin{pmatrix} \A & \B \\ 0 & \D \end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that for every \( j \ge 1 \),
\[
\M^j = \begin{pmatrix} \A^j & \S_j \\ 0 & \D^j \end{pmatrix}, \qquad \S_j = \sum_{i=0}^{j-1} \A^{i}\B \D^{\,j-1-i} .
\]
2. Deduce that if \( \D = 0 \), then \( \M^j = \begin{pmatrix} \A^j & \A^{j-1}\B \\ 0 & 0 \end{pmatrix} \) for \( j \ge 1 \), and that if moreover \( \A^r = 0 \), then \( \M^{r+1} = 0 \).
3. For \( \A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \), \( \B = \begin{pmatrix} 1 \\ 1 \end{pmatrix} \) and \( \D = (0) \), find the least \( j \) with \( \M^j = 0 \).
:::
::::

::: {.solution}
(a) By induction on \( j \). For \( j = 1 \), \( \S_1 = \A^0\B \D^0 = \B \). Suppose the formula holds for \( j \). By @thm-block-triangular-inverse (a),
\[
\M^{j+1} = \M^j\M = \begin{pmatrix} \A^j\A & \A^j\B + \S_j\D \\ 0 & \D^j\D \end{pmatrix},
\]
and \( \A^j\B + \S_j\D = \A^j\B \D^0 + \sum_{i=0}^{j-1} \A^i\B \D^{\,j-i} = \sum_{i=0}^{j} \A^i\B \D^{\,j-i} = \S_{j+1} \). This completes the induction.

(b) If \( \D = 0 \), every term of \( \S_j \) with \( j - 1 - i \ge 1 \) contains a factor \( \D = 0 \), and only \( i = j - 1 \) survives, with \( \D^0 = \I_l \). So \( \S_j = \A^{j-1}\B \) and \( \D^j = 0 \). If also \( \A^r = 0 \), then \( \M^{r+1} \) has blocks \( \A^{r+1} = 0 \) and \( \A^r\B = 0 \), so \( \M^{r+1} = 0 \).

(c) Here \( \A^2 = 0 \), so \( \M^3 = 0 \) by (b). But \( \M^2 = \begin{pmatrix} \A^2 & \A \B \\ 0 & 0 \end{pmatrix} \) with \( \A \B = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \ne \0 \), so \( \M^2 \ne 0 \); and \( \M \ne 0 \). The least such \( j \) is \( 3 \). Explicitly, \( \M = \begin{pmatrix} 0 & 1 & 1 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} \) and \( \M^2 = \E_{13} \).
:::
