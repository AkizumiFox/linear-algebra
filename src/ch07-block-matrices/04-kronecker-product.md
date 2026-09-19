# The Kronecker Product

So far the unknown in a matrix equation has been a vector: \( \A\x = \b \). Many natural questions have a matrix as the unknown instead. Which matrices commute with a given \( \A \)? Which \( \X \) solve \( \A \X + \X \B = \C \)? Such an equation is still linear in the entries of \( \X \), so in principle it is an ordinary linear system. The trouble is bookkeeping: we need to know what the coefficient matrix of that system is. This section builds it from \( \A \) and \( \B \) with one operation, the Kronecker product, and turns matrix equations into systems we already know how to solve.

## From a matrix equation to a linear system

Take \( \A, \B \in M_2(F) \) and an unknown \( \X = (x_{ij}) \in M_2(F) \), and look at the equation \( \A \X \B = \C \). By @def-matrix-multiplication, applied twice,
\[
(\A \X \B)_{rs} = \sum_{i=1}^{2}\sum_{j=1}^{2} a_{ri}\,x_{ij}\,b_{js} .
\]
So each entry of \( \A \X \B \) is a linear combination of the four unknowns \( x_{11}, x_{21}, x_{12}, x_{22} \), and the coefficient of \( x_{ij} \) in entry \( (r, s) \) is the product \( b_{js}a_{ri} \): **an entry of \( \B \) times an entry of \( \A \)**. Writing the four equations as a \( 4 \times 4 \) system, every coefficient is such a product. For instance, if we list the unknowns column by column as \( (x_{11}, x_{21}, x_{12}, x_{22}) \) and the equations in the same order, the first row of the coefficient matrix is
\[
\begin{pmatrix} b_{11}a_{11} & b_{11}a_{12} & b_{21}a_{11} & b_{21}a_{12} \end{pmatrix}.
\]
The left half of this row is \( b_{11} \) times row \( 1 \) of \( \A \), and the right half is \( b_{21} \) times row \( 1 \) of \( \A \).

That is a recurring pattern: a big matrix whose entries are all the products of the entries of two small matrices, arranged in blocks. It deserves a name.

## The Kronecker product

*The Kronecker product of \( \A \) and \( \B \) is the block matrix obtained by replacing each entry \( a_{ij} \) of \( \A \) by the block \( a_{ij}\B \).*

::: {#def-kronecker-product}
[Kronecker product]

Let \( \A = (a_{ij}) \in M_{m \times n}(F) \) and \( \B = (b_{kl}) \in M_{p \times q}(F) \), of **any** sizes. The **Kronecker product** of \( \A \) and \( \B \) is the \( mp \times nq \) block matrix
\[
\A \otimes \B \coloneqq \begin{pmatrix} a_{11}\B & a_{12}\B & \cdots & a_{1n}\B \\ a_{21}\B & a_{22}\B & \cdots & a_{2n}\B \\ \vdots & \vdots & & \vdots \\ a_{m1}\B & a_{m2}\B & \cdots & a_{mn}\B \end{pmatrix} \in M_{mp \times nq}(F),
\]
with \( m \) rows and \( n \) columns of blocks, each block of size \( p \times q \) (@def-block-partition).
:::

In words: the outer layout is the layout of \( \A \), and the inner pattern of every block is \( \B \). The sizes multiply, rows with rows and columns with columns. No condition on the sizes is needed, unlike for an ordinary product.

To work with single entries we need to know where each product \( a_{ij}b_{kl} \) sits. Block \( (i, j) \) occupies rows \( (i-1)p + 1, \dots, ip \) and columns \( (j-1)q + 1, \dots, jq \). Inside it, entry \( (k, l) \) is \( a_{ij}b_{kl} \). So
\[
\begin{aligned}
&(\A \otimes \B)_{(i-1)p+k,\ (j-1)q+l} = a_{ij}\,b_{kl} \\
&\qquad (1 \le i \le m,\ 1 \le j \le n,\ 1 \le k \le p,\ 1 \le l \le q).
\end{aligned} \tag{$\ast$}
\]
**Every entry is reached exactly once.** Division with remainder writes each row index \( r \in \{1, \dots, mp\} \) uniquely as \( r = (i-1)p + k \) with \( 1 \le i \le m \) and \( 1 \le k \le p \) (divide \( r - 1 \) by \( p \)), and likewise for columns. So \( (\ast) \) is a complete description of \( \A \otimes \B \), and it is the formula we use in proofs. In words, the rows of \( \A \otimes \B \) are labeled by pairs (row of \( \A \), row of \( \B \)) in dictionary order, and the columns by pairs (column of \( \A \), column of \( \B \)) in dictionary order.

**Examples.**

1. **A \( 2 \times 2 \) example.** With \( \A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \) and \( \B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \),
\[
\A \otimes \B = \begin{pmatrix} 1\B & 2\B \\ 3\B & 4\B \end{pmatrix} = \begin{pmatrix} 0 & 1 & 0 & 2 \\ 1 & 0 & 2 & 0 \\ 0 & 3 & 0 & 4 \\ 3 & 0 & 4 & 0 \end{pmatrix}.
\]
Check one entry against \( (\ast) \): row \( 3 = (2-1)\cdot 2 + 1 \) and column \( 2 = (1-1)\cdot 2 + 2 \) give \( a_{21}b_{12} = 3 \cdot 1 = 3 \), as displayed.
2. **Vectors.** For column vectors \( \u \in F^m \) and \( \v \in F^p \) (so \( n = q = 1 \)), \( \u \otimes \v \in F^{mp} \) lists all products \( u_iv_k \) in dictionary order. In particular, for standard basis vectors, \( \e_i \otimes \e_k = \e_{(i-1)p+k} \in F^{mp} \): the only non-zero product is \( 1 \cdot 1 \) in position \( (i-1)p + k \). For a column \( \u \in F^m \) and a row \( \v\tp \), \( \u \otimes \v\tp \) is the \( m \times p \) matrix with entries \( u_iv_k \), which is the outer product \( \u\v\tp \) of @cor-outer-product-expansion.
3. **Identity blocks.** \( \I_n \otimes \B \) has \( \B \) in each diagonal block and zero blocks elsewhere, so it is the block diagonal matrix \( \B \oplus \dots \oplus \B \) with \( n \) copies of \( \B \) (@def-block-diagonal). By contrast, \( \A \otimes \I_m \) replaces each entry \( a_{ij} \) by the \( m \times m \) block \( a_{ij}\I_m \). Taking both, \( \I_n \otimes \I_m = \I_{nm} \): by \( (\ast) \) its entries are \( \delta_{ij}\delta_{kl} \), which is \( 1 \) exactly when the row and column labels \( (i, k) \) and \( (j, l) \) agree.
4. **The degenerate case \( 1 \times 1 \).** If \( \A = (a) \) is \( 1 \times 1 \), then \( \A \otimes \B = a\B \); if \( \B = (b) \), then \( \A \otimes \B = b\A \). So a \( 1 \times 1 \) factor behaves like a scalar, and \( (1) \otimes \B = \B \). This case is worth keeping in mind: it shows that the Kronecker product extends scalar multiplication, which is why it is bilinear below.

**Non-example by minimal change.** Swap the two factors of Example 1:
\[
\B \otimes \A = \begin{pmatrix} 0\A & 1\A \\ 1\A & 0\A \end{pmatrix} = \begin{pmatrix} 0 & 0 & 1 & 2 \\ 0 & 0 & 3 & 4 \\ 1 & 2 & 0 & 0 \\ 3 & 4 & 0 & 0 \end{pmatrix}.
\]
It has the same size and the same multiset of entries, since both list all products \( a_{ij}b_{kl} \). What fails is the position formula \( (\ast) \): in \( \B \otimes \A \) the **outer** layout comes from \( \B \), so the products sit in different places. For instance, the \( (1, 2) \)-entry is \( a_{11}b_{12} = 1 \) in \( \A \otimes \B \) but \( b_{11}a_{12} = 0 \) in \( \B \otimes \A \).

**Why this definition.** The dictionary order in \( (\ast) \) is a convention, and the other order would simply give \( \B \otimes \A \). We fix it because it makes the block picture true: the Kronecker product is literally "\( \A \) with entries replaced by blocks", so block multiplication (@thm-block-multiplication) applies to it directly. The symbol \( \otimes \) anticipates the tensor product of Chapter 14, of which this is the matrix version.

::: {.warning}
**The Kronecker product is not commutative, and it is not the ordinary product.** The two matrices in Example 1 and the non-example differ, so \( \A \otimes \B \ne \B \otimes \A \) in general, even for square matrices of the same size. Also do not confuse \( \A \otimes \B \) with \( \A \B \): for \( \A, \B \in M_2(F) \), \( \A \B \) is \( 2 \times 2 \) while \( \A \otimes \B \) is \( 4 \times 4 \), and \( \A \otimes \B \) is defined for all sizes. We will see below that \( \A \otimes \B \) and \( \B \otimes \A \) are always **similar** when \( \A \) and \( \B \) are square, so they share rank, trace and determinant, but they are not equal.
:::

## Algebraic properties

The Kronecker product interacts well with every operation we have. The most useful rule is the one connecting it to ordinary multiplication: multiply the two left factors together and the two right factors together.

::: {#thm-kronecker-properties}
[Properties of the Kronecker Product]

Let \( c \in F \). Whenever the sizes make each side defined:

::: {.enumerate options="label=(\alph*)"}
1. **(Bilinearity)** \( (\A + \A') \otimes \B = \A \otimes \B + \A' \otimes \B \), \( \A \otimes (\B + \B') = \A \otimes \B + \A \otimes \B' \), and \( (c\A) \otimes \B = c(\A \otimes \B) = \A \otimes (c\B) \).
2. **(Associativity)** \( (\A \otimes \B) \otimes \C = \A \otimes (\B \otimes \C) \) for all \( \A \in M_{m \times n}(F) \), \( \B \in M_{p \times q}(F) \), \( \C \in M_{r \times s}(F) \).
3. **(Mixed product rule)** For \( \A \in M_{m \times n}(F) \), \( \C \in M_{n \times t}(F) \), \( \B \in M_{p \times q}(F) \) and \( \D \in M_{q \times u}(F) \),
\[
(\A \otimes \B)(\C \otimes \D) = (\A \C) \otimes (\B \D) .
\]
4. **(Transpose)** \( (\A \otimes \B)\tp = \A\tp \otimes \B\tp \).
5. **(Inverse)** If \( \A \in M_n(F) \) and \( \B \in M_m(F) \) are invertible, then \( \A \otimes \B \) is invertible and \( (\A \otimes \B)^{-1} = \A^{-1} \otimes \B^{-1} \).
:::
:::

::: {.idea}
Parts (a), (b) and (d) are entry checks with \( (\ast) \). For (c), both factors on the left are block matrices, and the columns of blocks of \( \A \otimes \B \) (\( n \) of them, each \( q \) wide) match the rows of blocks of \( \C \otimes \D \) (\( n \) of them, each \( q \) tall). So we may multiply blockwise, and each block of the product is a sum \( \sum_j (a_{ij}\B)(c_{jk}\D) \) in which the scalars come out. Part (e) is (c) with \( \C = \A^{-1} \), \( \D = \B^{-1} \).
:::

::: {.proof}
(a) By \( (\ast) \), the entry of \( (\A + \A') \otimes \B \) in position \( ((i-1)p + k, (j-1)q + l) \) is \( (a_{ij} + a'_{ij})b_{kl} = a_{ij}b_{kl} + a'_{ij}b_{kl} \), which is the entry of \( \A \otimes \B + \A' \otimes \B \) in the same position. The other identities are checked the same way, using \( (ca_{ij})b_{kl} = c(a_{ij}b_{kl}) = a_{ij}(cb_{kl}) \).

(b) Both sides are \( mpr \times nqs \). Let \( 1 \le i \le m \), \( 1 \le k \le p \), \( 1 \le t \le r \), and similarly \( j, l, u \) for columns. Applying \( (\ast) \) twice, the entry of \( (\A \otimes \B) \otimes \C \) in row \( \big((i-1)p + k - 1\big)r + t \) and column \( \big((j-1)q + l - 1\big)s + u \) is \( (\A \otimes \B)_{(i-1)p+k,\,(j-1)q+l}\;c_{tu} = a_{ij}b_{kl}c_{tu} \). Likewise the entry of \( \A \otimes (\B \otimes \C) \) in row \( (i-1)pr + (k-1)r + t \) and column \( (j-1)qs + (l-1)s + u \) is \( a_{ij}(\B \otimes \C)_{(k-1)r+t,\,(l-1)s+u} = a_{ij}b_{kl}c_{tu} \). Since \( \big((i-1)p + k - 1\big)r + t = (i-1)pr + (k-1)r + t \), and similarly for columns, the two matrices have the same entry in every position; every position arises from exactly one choice of indices, by division with remainder. Hence they are equal.

(c) Partition \( \A \otimes \B \) into \( m \) rows and \( n \) columns of blocks as in @def-kronecker-product, each block \( p \times q \), and \( \C \otimes \D \) into \( n \) rows and \( t \) columns of blocks, each \( q \times u \). The column partition of the first matrix (\( n \) parts of size \( q \)) equals the row partition of the second, so the partitions are conformable, and by @thm-block-multiplication the \( (i, k) \) block of the product is
\[
\sum_{j=1}^{n} (a_{ij}\B)(c_{jk}\D) = \sum_{j=1}^{n} a_{ij}c_{jk}\,\B \D = (\A \C)_{ik}\,\B \D,
\]
where the first equality uses @thm-matrix-multiplication-properties (4) and the second uses @def-matrix-multiplication. This is the \( (i, k) \) block of \( (\A \C) \otimes (\B \D) \), a matrix partitioned into \( m \) rows and \( t \) columns of \( p \times u \) blocks. So the two matrices agree block by block, hence entry by entry.

(d) \( (\A \otimes \B)\tp \) is \( nq \times mp \). By @def-transpose and \( (\ast) \), its entry in row \( (j-1)q + l \) and column \( (i-1)p + k \) is \( (\A \otimes \B)_{(i-1)p+k,\,(j-1)q+l} = a_{ij}b_{kl} = (\A\tp)_{ji}(\B\tp)_{lk} \), which by \( (\ast) \) is the entry of \( \A\tp \otimes \B\tp \) in the same position.

(e) By (c) and Example 3, \( (\A \otimes \B)(\A^{-1} \otimes \B^{-1}) = (\A \A^{-1}) \otimes (\B \B^{-1}) = \I_n \otimes \I_m = \I_{nm} \), and similarly \( (\A^{-1} \otimes \B^{-1})(\A \otimes \B) = \I_{nm} \). By @def-invertible-matrix, \( \A \otimes \B \) is invertible with inverse \( \A^{-1} \otimes \B^{-1} \).
:::

The mixed product rule is the engine of everything that follows. One immediate consequence splits a Kronecker product of square matrices into two simpler factors: for \( \A \in M_n(F) \) and \( \B \in M_m(F) \),
\[
\A \otimes \B = (\A \I_n) \otimes (\I_m\B) = (\A \otimes \I_m)(\I_n \otimes \B), \tag{$\ast\ast$}
\]
and in the same way \( \A \otimes \B = (\I_n \otimes \B)(\A \otimes \I_m) \). So \( \A \otimes \I_m \) and \( \I_n \otimes \B \) commute, even though \( \A \) and \( \B \) have nothing to do with each other.

For example, with \( \A = \begin{pmatrix} 1 & -1 \\ 0 & 2 \end{pmatrix} \), \( \B = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \), \( \C = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} \) and \( \D = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \), multiplying two \( 4 \times 4 \) matrices directly gives
\[
(\A \otimes \B)(\C \otimes \D) = \begin{pmatrix} 2 & 1 & -2 & -1 \\ 1 & 1 & -1 & -1 \\ 0 & 0 & 4 & 2 \\ 0 & 0 & 2 & 2 \end{pmatrix}\begin{pmatrix} 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 1 \\ 1 & 0 & 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 & -1 & -2 \\ 0 & 0 & -1 & -1 \\ 2 & 4 & 2 & 4 \\ 2 & 2 & 2 & 2 \end{pmatrix},
\]
while the rule needs only two \( 2 \times 2 \) products, \( \A \C = \begin{pmatrix} 0 & -1 \\ 2 & 2 \end{pmatrix} \) and \( \B \D = \begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix} \), whose Kronecker product is the same matrix.

## Swapping the factors

The warning said that \( \A \otimes \B \) and \( \B \otimes \A \) differ. They differ only in the order in which rows and columns are labeled: \( \A \otimes \B \) uses (index of \( \A \), index of \( \B \)) in dictionary order, \( \B \otimes \A \) the reverse order. Relabeling rows and columns by the same permutation is conjugation by a permutation matrix, and that is what the next result makes precise.

First, a fact about permutation matrices. Recall that for \( \sigma \in S_N \), the permutation matrix \( \P_\sigma \) has \( j \)-th column \( \e_{\sigma(j)} \), and \( \P_\sigma^{-1} = \P_\sigma\tp \) (@def-permutation-matrix, @lem-permutation-matrices). For every \( \M \in M_N(F) \),
\[
\big(\P_\sigma\tp \M \P_\sigma\big)_{rs} = \M_{\sigma(r)\,\sigma(s)} \qquad (1 \le r, s \le N). \tag{$\dagger$}
\]
Indeed, by @thm-three-views-of-product column \( s \) of \( \M \P_\sigma \) is \( \M\e_{\sigma(s)} \), which is column \( \sigma(s) \) of \( \M \). Row \( r \) of \( \P_\sigma\tp \) is \( \e_{\sigma(r)}\tp \), so by the same theorem row \( r \) of \( \P_\sigma\tp \L \) is row \( \sigma(r) \) of \( \L \), for any \( \L \in M_N(F) \). Combining the two gives \( (\dagger) \).

::: {#prp-kronecker-swap-similar}
[Swapping the Factors Is a Permutation Similarity]

Let \( n, m \ge 1 \). There is a permutation matrix \( \P \in M_{nm}(F) \), depending only on \( n \) and \( m \), such that
\[
\B \otimes \A = \P^{-1}(\A \otimes \B)\P \qquad \text{for all } \A \in M_n(F),\ \B \in M_m(F).
\]
In particular \( \A \otimes \B \sim \B \otimes \A \), and \( \I_m \otimes \A = \P^{-1}(\A \otimes \I_m)\P \).
:::

::: {.proof}
Every \( r \in \{1, \dots, nm\} \) can be written uniquely as \( r = (k-1)n + i \) with \( 1 \le k \le m \) and \( 1 \le i \le n \). Define \( \sigma(r) \coloneqq (i-1)m + k \). As \( (k, i) \) runs over all pairs, so does \( (i, k) \), and each value \( (i-1)m + k \) is taken by exactly one pair; hence \( \sigma \) is a bijection of \( \{1, \dots, nm\} \), that is, \( \sigma \in S_{nm} \). Put \( \P = \P_\sigma \).

Let \( r = (k-1)n + i \) and \( s = (l-1)n + j \). By \( (\ast) \) applied to \( \B \otimes \A \), \( (\B \otimes \A)_{rs} = b_{kl}a_{ij} \). By \( (\ast) \) applied to \( \A \otimes \B \),
\[
(\A \otimes \B)_{\sigma(r)\,\sigma(s)} = (\A \otimes \B)_{(i-1)m+k,\ (j-1)m+l} = a_{ij}b_{kl} .
\]
So by \( (\dagger) \), \( \P_\sigma\tp(\A \otimes \B)\P_\sigma \) and \( \B \otimes \A \) agree in every entry, and \( \P_\sigma\tp = \P_\sigma^{-1} \) by @lem-permutation-matrices (b). The last claim is the case \( \B = \I_m \).
:::

For example, when \( n = m = 2 \), \( \sigma \) fixes \( 1 \) and \( 4 \) and swaps \( 2 \) and \( 3 \), so \( \P \) is the elementary matrix \( \P_{23} \): conjugating by it swaps rows \( 2, 3 \) and columns \( 2, 3 \). Doing this to \( \A \otimes \B \) in Example 1 does give \( \B \otimes \A \), as a direct check shows. For rectangular \( \A \in M_{m \times n}(F) \) and \( \B \in M_{p \times q}(F) \), the same argument gives \( \B \otimes \A = \P_\sigma\tp(\A \otimes \B)\P_\tau \) with one permutation for the rows and another for the columns.

## Rank, trace and determinant

Each of the three basic numbers attached to a matrix behaves multiplicatively. The formulas for trace and rank are what one would guess. The determinant is subtler, because the sizes enter as exponents.

::: {#thm-kronecker-rank-trace-det}
[Rank, Trace and Determinant of a Kronecker Product]

::: {.enumerate options="label=(\alph*)"}
1. For \( \A \in M_{m \times n}(F) \) and \( \B \in M_{p \times q}(F) \), \( \rank(\A \otimes \B) = \rank \A \cdot \rank \B \).
2. For \( \A \in M_n(F) \) and \( \B \in M_m(F) \), \( \tr(\A \otimes \B) = \tr \A \cdot \tr \B \).
3. For \( \A \in M_n(F) \) and \( \B \in M_m(F) \), \( \det(\A \otimes \B) = (\det \A)^{m}\,(\det \B)^{n} \).
:::
:::

::: {.idea}
For rank, bring both factors to rank normal form, \( \A = \Q \N_r\P \) and \( \B = \Q'\N_s\P' \). The mixed product rule moves the invertible factors outside, where they do not change rank, and \( \N_r \otimes \N_s \) visibly has rank \( rs \). Trace is a sum over diagonal entries, and the diagonal entries of \( \A \otimes \B \) are the products \( a_{ii}b_{kk} \). For the determinant, split \( \A \otimes \B = (\A \otimes \I_m)(\I_n \otimes \B) \) by \( (\ast\ast) \). The second factor is block diagonal with \( n \) copies of \( \B \). The first is not, but by @prp-kronecker-swap-similar it is similar to \( \I_m \otimes \A \), which is block diagonal with \( m \) copies of \( \A \).
:::

::: {.proof}
(a) Let \( r = \rank \A \) and \( s = \rank \B \). By @thm-rank-normal-form (b) and @def-equivalent-matrices, there are invertible \( \Q_1, \P_1, \Q_2, \P_2 \) with \( \N_r = \Q_1\A \P_1 \) and \( \N_s = \Q_2\B \P_2 \), where \( \N_r \in M_{m \times n}(F) \) and \( \N_s \in M_{p \times q}(F) \) have \( \I_r \), \( \I_s \) in the top left corner and zeros elsewhere. Hence \( \A = \Q_1^{-1}\N_r\P_1^{-1} \) and \( \B = \Q_2^{-1}\N_s\P_2^{-1} \), and by @thm-kronecker-properties (c), used twice,
\[
\A \otimes \B = (\Q_1^{-1} \otimes \Q_2^{-1})(\N_r \otimes \N_s)(\P_1^{-1} \otimes \P_2^{-1}) .
\]
The outer factors are invertible by @thm-kronecker-properties (e), so \( \rank(\A \otimes \B) = \rank(\N_r \otimes \N_s) \) by @thm-rank-product-inequality.

By \( (\ast) \), the entry of \( \N_r \otimes \N_s \) in position \( ((i-1)p + k, (j-1)q + l) \) is \( 1 \) if \( i = j \le r \) and \( k = l \le s \), and \( 0 \) otherwise. So for each of the \( rs \) pairs \( (i, k) \) with \( i \le r \), \( k \le s \), column \( (i-1)q + k \) equals \( \e_{(i-1)p+k} \), and every other column is zero. Distinct pairs give distinct standard basis vectors, so these \( rs \) columns are linearly independent and span the column space. Hence \( \rank(\N_r \otimes \N_s) = rs \) by @def-rank-matrix, which proves (a). (If \( r = 0 \) or \( s = 0 \), the matrix is zero and both sides are \( 0 \).)

(b) By \( (\ast) \) with \( p = q = m \), the diagonal entries of \( \A \otimes \B \) are those with \( (i-1)m + k = (j-1)m + l \), that is \( i = j \) and \( k = l \) by uniqueness of division with remainder, and they equal \( a_{ii}b_{kk} \). By @def-trace,
\[
\tr(\A \otimes \B) = \sum_{i=1}^{n}\sum_{k=1}^{m} a_{ii}b_{kk} = \Big(\sum_{i=1}^{n} a_{ii}\Big)\Big(\sum_{k=1}^{m} b_{kk}\Big) = \tr \A \cdot \tr \B .
\]

(c) First, a block diagonal matrix \( \M_1 \oplus \dots \oplus \M_t \) with square blocks \( \M_1, \dots, \M_t \) has determinant \( \det \M_1 \cdots \det \M_t \). For \( t = 1 \) there is nothing to prove, and for \( t \ge 2 \) the matrix is \( \M_1 \oplus (\M_2 \oplus \dots \oplus \M_t) \), so @thm-block-diagonal-arithmetic (d) (or @thm-det-block-triangular) and induction on \( t \) give the claim.

By Example 3, \( \I_n \otimes \B = \B \oplus \dots \oplus \B \) with \( n \) blocks, so \( \det(\I_n \otimes \B) = (\det \B)^n \). Likewise \( \I_m \otimes \A = \A \oplus \dots \oplus \A \) with \( m \) blocks, so \( \det(\I_m \otimes \A) = (\det \A)^m \). By @prp-kronecker-swap-similar, \( \A \otimes \I_m \) is similar to \( \I_m \otimes \A \), so \( \det(\A \otimes \I_m) = (\det \A)^m \) by @cor-det-similarity-invariant. Finally, by \( (\ast\ast) \) and @thm-det-multiplicative,
\[
\det(\A \otimes \B) = \det(\A \otimes \I_m)\det(\I_n \otimes \B) = (\det \A)^m(\det \B)^n .
\]
:::

The exponents are easy to get backwards, and a size count fixes them. In \( \A \otimes \B \) with \( \A \in M_n(F) \), \( \B \in M_m(F) \), the matrix \( \A \) is "used" \( m \) times (once for each index of \( \B \)), so \( \det \A \) appears to the power \( m \), the size of the **other** factor. For \( \A = c\I_n \) and \( \B = \I_m \), \( \A \otimes \B = c\I_{nm} \) has determinant \( c^{nm} = (c^n)^m = (\det \A)^m \), which confirms the exponent.

For the matrices of the example after @thm-kronecker-properties, \( \det \A = 2 \), \( \det \B = 1 \), \( \tr \A = 3 \) and \( \tr \B = 3 \), so \( \det(\A \otimes \B) = 2^2 \cdot 1^2 = 4 \), \( \tr(\A \otimes \B) = 9 \), and \( \rank(\A \otimes \B) = 2 \cdot 2 = 4 \). Directly, the diagonal of \( \A \otimes \B \) is \( 2, 1, 4, 2 \), with sum \( 9 \).

::: {.check}
Let \( \A \in M_2(\nR) \) have \( \tr \A = 4 \), \( \det \A = 3 \), and let \( \B \in M_3(\nR) \) have \( \tr \B = 2 \), \( \det \B = -1 \). Find \( \tr(\A \otimes \B) \), \( \det(\A \otimes \B) \) and \( \det(\B \otimes \A) \).
:::

::: {.solution}
By @thm-kronecker-rank-trace-det, \( \tr(\A \otimes \B) = 4 \cdot 2 = 8 \) and \( \det(\A \otimes \B) = (\det \A)^3(\det \B)^2 = 27 \cdot 1 = 27 \). With the roles swapped, \( \det(\B \otimes \A) = (\det \B)^2(\det \A)^3 = 27 \), as it must be since \( \B \otimes \A \sim \A \otimes \B \) (@prp-kronecker-swap-similar). The common wrong answer \( (\det \A)^2(\det \B)^3 = -9 \) puts each matrix's own size in its exponent.
:::

## Vectorization

We return to the question of the opening: turning a matrix equation into a linear system. For that we need to flatten the unknown matrix into a column, in an order that matches \( (\ast) \).

*To vectorize a matrix is to stack its columns into one long column.*

::: {#def-vec-operator}
[Vectorization]

Let \( \X = (x_{ij}) \in M_{m \times n}(F) \) have columns \( \x_1, \dots, \x_n \in F^m \). Its **vectorization** is the column vector
\[
\vecop \X \coloneqq \begin{pmatrix} \x_1 \\ \x_2 \\ \vdots \\ \x_n \end{pmatrix} \in F^{mn},
\]
whose entry in position \( (j-1)m + i \) is \( x_{ij} \), for \( 1 \le i \le m \), \( 1 \le j \le n \).
:::

For example, \( \vecop\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = (1, 3, 2, 4) \), read down the first column and then down the second. For a column \( \x \in F^m \) (the case \( n = 1 \)), \( \vecop \x = \x \). The map \( \vecop \colon M_{m \times n}(F) \to F^{mn} \) is linear, since each entry of \( \vecop \X \) is an entry of \( \X \), and bijective, since it only rearranges entries; so it is an isomorphism. It sends the matrix unit \( \E_{ij} \) to \( \e_{(j-1)m+i} = \e_j \otimes \e_i \) (Example 2, with the index of the column first). More generally, \( \vecop(\u\v\tp) = \v \otimes \u \) for \( \u \in F^m \) and \( \v \in F^n \): column \( j \) of \( \u\v\tp \) is \( v_j\u \).

Two conventions are in use, and they differ. Some books stack the **rows** instead, which exchanges the roles of the two factors in the next theorem. We always stack columns.

::: {#thm-vec-identity}
[The vec Identity]

Let \( \A \in M_{k \times m}(F) \), \( \X \in M_{m \times n}(F) \) and \( \B \in M_{n \times l}(F) \). Then
\[
\vecop(\A \X \B) = (\B\tp \otimes \A)\,\vecop \X .
\]
:::

::: {.idea}
Both sides are columns in \( F^{kl} \). We compare one entry, using the formula for a triple product on the left and \( (\ast) \) on the right. The factor \( \A \) acts on the row index of \( \X \), which is the inner index in \( \vecop \); the factor \( \B \) acts on the column index, which is the outer index. That is why \( \B \) comes first, and it enters transposed because it multiplies \( \X \) from the right.
:::

::: {.proof}
Both sides lie in \( F^{kl} \): \( \A \X \B \in M_{k \times l}(F) \), and \( \B\tp \otimes \A \in M_{lk \times nm}(F) \) acts on \( \vecop \X \in F^{mn} \). Fix \( 1 \le r \le k \) and \( 1 \le s \le l \), and consider position \( (s-1)k + r \). By @def-vec-operator and @def-matrix-multiplication applied twice, the left side has entry
\[
(\A \X \B)_{rs} = \sum_{i=1}^{m}\sum_{j=1}^{n} a_{ri}\,x_{ij}\,b_{js} .
\]
On the right, write the column index \( c \in \{1, \dots, nm\} \) of \( \B\tp \otimes \A \) uniquely as \( c = (j-1)m + i \) with \( 1 \le j \le n \), \( 1 \le i \le m \). By \( (\ast) \), \( (\B\tp \otimes \A)_{(s-1)k+r,\ (j-1)m+i} = (\B\tp)_{sj}\,a_{ri} = b_{js}\,a_{ri} \), and by @def-vec-operator the \( c \)-th entry of \( \vecop \X \) is \( x_{ij} \). Hence the entry of the right side in position \( (s-1)k + r \) is
\[
\sum_{c=1}^{nm} (\B\tp \otimes \A)_{(s-1)k+r,\ c}\,(\vecop \X)_c = \sum_{j=1}^{n}\sum_{i=1}^{m} b_{js}\,a_{ri}\,x_{ij},
\]
which equals the left side. As \( (r, s) \) ranges over all pairs, \( (s-1)k + r \) ranges over all positions, so the two vectors are equal.
:::

Taking \( \B = \I_n \) or \( \A = \I_m \) gives the two one-sided forms, which are used most often:
\[
\vecop(\A \X) = (\I_n \otimes \A)\,\vecop \X, \qquad \vecop(\X \B) = (\B\tp \otimes \I_m)\,\vecop \X .
\]
The first says that multiplying \( \X \) by \( \A \) on the left multiplies each column of \( \X \) by \( \A \): \( \I_n \otimes \A = \A \oplus \dots \oplus \A \) acts on the stacked columns one at a time.

Now every linear matrix equation built from products becomes a linear system. The most important one is the **Sylvester equation**
\[
\A \X + \X \B = \C, \qquad \A \in M_m(F),\ \B \in M_n(F),\ \C \in M_{m \times n}(F),
\]
for an unknown \( \X \in M_{m \times n}(F) \). Applying \( \vecop \), which is linear, and the two one-sided forms,
\[
\big(\I_n \otimes \A + \B\tp \otimes \I_m\big)\,\vecop \X = \vecop \C .
\]
So the Sylvester equation has **exactly one** solution for every \( \C \) if and only if the \( mn \times mn \) matrix \( \I_n \otimes \A + \B\tp \otimes \I_m \) is invertible (@thm-invertible-tfae, transported through the isomorphism \( \vecop \)). The equation \( \A \X = \X \A \) of the opening, which describes the matrices commuting with \( \A \), is the case \( \B = -\A \), \( \C = 0 \): its solutions form the null space of \( \I_m \otimes \A - \A\tp \otimes \I_m \).

::: {#exm-sylvester-equation-vec}
[A Sylvester Equation as a Linear System]

Solve \( \A \X + \X \B = \C \) over \( \nQ \), where
\[
\A = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}, \qquad \B = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}, \qquad \C = \begin{pmatrix} 1 & -1 \\ 1 & 3 \end{pmatrix}.
\]
:::

::: {.solution}
Here \( m = n = 2 \). Compute the two Kronecker products from @def-kronecker-product:
\[
\I_2 \otimes \A = \begin{pmatrix} 1 & 1 & 0 & 0 \\ 0 & 2 & 0 & 0 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 2 \end{pmatrix}, \qquad \B\tp \otimes \I_2 = \begin{pmatrix} 1\I_2 & 1\I_2 \\ 0\I_2 & 1\I_2 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}.
\]
With \( \vecop \X = (x_{11}, x_{21}, x_{12}, x_{22}) \) and \( \vecop \C = (1, 1, -1, 3) \), the system \( (\I_2 \otimes \A + \B\tp \otimes \I_2)\vecop \X = \vecop \C \) is
\[
\begin{pmatrix} 2 & 1 & 1 & 0 \\ 0 & 3 & 0 & 1 \\ 0 & 0 & 2 & 1 \\ 0 & 0 & 0 & 3 \end{pmatrix}\begin{pmatrix} x_{11} \\ x_{21} \\ x_{12} \\ x_{22} \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ -1 \\ 3 \end{pmatrix}.
\]
The coefficient matrix is upper triangular with non-zero diagonal entries \( 2, 3, 2, 3 \), so its determinant is \( 36 \ne 0 \) (@thm-det-triangular) and the solution is unique. Back substitution gives \( x_{22} = 1 \); then \( 2x_{12} + 1 = -1 \), so \( x_{12} = -1 \); then \( 3x_{21} + 1 = 1 \), so \( x_{21} = 0 \); then \( 2x_{11} + 0 - 1 = 1 \), so \( x_{11} = 1 \). Hence
\[
\X = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}.
\]
*Check:* \( \A \X = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix} \) and \( \X \B = \begin{pmatrix} 0 & -1 \\ 1 & 1 \end{pmatrix} \), whose sum is \( \C \). As a check on the bookkeeping, row \( 1 \) of the system is the \( (1, 1) \) entry of \( \A \X + \X \B \), namely \( (x_{11} + x_{21}) + (x_{11} + x_{12}) \).
:::

In this example the coefficient matrix came out triangular, with diagonal entries \( a_{ii} + b_{jj} \). That is no accident when \( \A \) is upper triangular and \( \B \) lower triangular, as @exr-kronecker-product-c2 below shows. In general, whether \( \I_n \otimes \A + \B\tp \otimes \I_m \) is invertible depends on the eigenvalues of \( \A \) and \( \B \): over \( \nC \), the equation \( \A \X - \X \B = \C \) is uniquely solvable for every \( \C \) exactly when \( \A \) and \( \B \) have no common eigenvalue. That criterion needs eigenvalues and is proved in Chapter 11, and its quantitative form appears in Chapter 19.

::: {.warning}
**Keep the order and the transpose in \( \vecop(\A \X \B) = (\B\tp \otimes \A)\vecop \X \).** Both \( \A \otimes \B\tp \) and \( \B \otimes \A \) look plausible, and both are wrong. With \( \X = \E_{11} \in M_2(F) \), \( \A = \I_2 \) and \( \B = \E_{21} \), we get \( \A \X \B = \E_{11}\E_{21} = 0 \), and indeed \( (\B\tp \otimes \I_2)\,\e_1 = (\E_{12} \otimes \I_2)\e_1 = \0 \), because the first column of \( \E_{12} \otimes \I_2 \) is zero. But \( (\B \otimes \I_2)\,\e_1 = (\E_{21} \otimes \I_2)\e_1 = \e_3 \ne \0 \). So \( \B \otimes \A \) fails. A similar test with \( \A = \E_{12} \), \( \X = \E_{21} \), \( \B = \I_2 \) refutes \( \A \otimes \B\tp \). If a formula is in doubt, test it on matrix units.
:::

The Kronecker product is the coordinate shadow of a basis-free construction: the tensor product of linear maps, in Chapter 14, whose matrix in suitable bases is exactly \( \A \otimes \B \). The dictionary order in \( (\ast) \) will reappear there as an ordering of a basis \( \v_i \otimes \w_k \).

## Exercises

### A. Check your understanding

:::: {#exr-kronecker-product-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define \( \A \otimes \B \) for \( \A \in M_{m \times n}(F) \) and \( \B \in M_{p \times q}(F) \), and state its size.
2. True or false: for all \( \A, \B \in M_2(F) \), \( \A \otimes \B = \B \otimes \A \). Justify your answer.
3. State the mixed product rule, including the conditions on the sizes.
4. True or false: \( \det(\A \otimes \B) = \det \A \det \B \) for all \( \A, \B \in M_2(\nR) \). Justify your answer.
5. State the vec identity, and name the matrix \( \M \) with \( \vecop(\X \B) = \M\vecop \X \) for \( \X \in M_{m \times n}(F) \), \( \B \in M_n(F) \).
:::
::::

::: {.solution}
(a) \( \A \otimes \B \) is the \( mp \times nq \) block matrix with \( (i, j) \) block \( a_{ij}\B \) (@def-kronecker-product); equivalently, its entry in position \( ((i-1)p + k, (j-1)q + l) \) is \( a_{ij}b_{kl} \).

(b) False. For \( \A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \) and \( \B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \), the \( (1, 2) \) entry of \( \A \otimes \B \) is \( a_{11}b_{12} = 1 \) and that of \( \B \otimes \A \) is \( b_{11}a_{12} = 0 \). The two are similar (@prp-kronecker-swap-similar), not equal.

(c) If \( \A \in M_{m \times n}(F) \), \( \C \in M_{n \times t}(F) \), \( \B \in M_{p \times q}(F) \) and \( \D \in M_{q \times u}(F) \), then \( (\A \otimes \B)(\C \otimes \D) = (\A \C) \otimes (\B \D) \) (@thm-kronecker-properties (c)). The conditions are exactly that \( \A \C \) and \( \B \D \) are defined.

(d) False. By @thm-kronecker-rank-trace-det, \( \det(\A \otimes \B) = (\det \A)^2(\det \B)^2 \). For \( \A = \B = 2\I_2 \), \( \A \otimes \B = 4\I_4 \) has determinant \( 256 \), while \( \det \A\det \B = 16 \).

(e) \( \vecop(\A \X \B) = (\B\tp \otimes \A)\vecop \X \) (@thm-vec-identity). With \( \A = \I_m \), \( \M = \B\tp \otimes \I_m \).
:::

### B. Practice

:::: {#exr-kronecker-product-b1}
[B1: Computing with Kronecker products]

Let \( \A = \begin{pmatrix} 2 & 0 \\ 1 & -1 \end{pmatrix} \) and \( \B = \begin{pmatrix} 1 & 1 \\ 0 & 3 \end{pmatrix} \) over \( \nQ \).

::: {.enumerate options="label=(\alph*)"}
1. Write out \( \A \otimes \B \) and \( \B \otimes \A \).
2. Compute \( \tr \), \( \det \) and \( \rank \) of \( \A \otimes \B \) from @thm-kronecker-rank-trace-det, and check the trace directly.
3. Compute \( \A^2 \otimes \B^2 \) and use it to write down \( (\A \otimes \B)^2 \) without multiplying \( 4 \times 4 \) matrices. Justify the step.
4. Hence find \( (\A \otimes \B)^{-1} \).
:::
::::

::: {.solution}
(a) By @def-kronecker-product,
\[
\begin{aligned}
\A \otimes \B &= \begin{pmatrix} 2\B & 0\B \\ 1\B & -1\B \end{pmatrix} = \begin{pmatrix} 2 & 2 & 0 & 0 \\ 0 & 6 & 0 & 0 \\ 1 & 1 & -1 & -1 \\ 0 & 3 & 0 & -3 \end{pmatrix}, \\
\B \otimes \A &= \begin{pmatrix} 1\A & 1\A \\ 0\A & 3\A \end{pmatrix} = \begin{pmatrix} 2 & 0 & 2 & 0 \\ 1 & -1 & 1 & -1 \\ 0 & 0 & 6 & 0 \\ 0 & 0 & 3 & -3 \end{pmatrix}.
\end{aligned}
\]

(b) \( \tr \A = 1 \), \( \tr \B = 4 \), \( \det \A = -2 \), \( \det \B = 3 \), and both have rank \( 2 \). By @thm-kronecker-rank-trace-det, \( \tr(\A \otimes \B) = 4 \), \( \det(\A \otimes \B) = (-2)^2 \cdot 3^2 = 36 \) and \( \rank(\A \otimes \B) = 4 \). Directly, the diagonal of \( \A \otimes \B \) is \( 2, 6, -1, -3 \), with sum \( 4 \).

(c) By the mixed product rule (@thm-kronecker-properties (c)) with \( \C = \A \) and \( \D = \B \), \( (\A \otimes \B)^2 = \A^2 \otimes \B^2 \). Here \( \A^2 = \begin{pmatrix} 4 & 0 \\ 1 & 1 \end{pmatrix} \) and \( \B^2 = \begin{pmatrix} 1 & 4 \\ 0 & 9 \end{pmatrix} \), so
\[
(\A \otimes \B)^2 = \begin{pmatrix} 4\B^2 & 0 \\ \B^2 & \B^2 \end{pmatrix} = \begin{pmatrix} 4 & 16 & 0 & 0 \\ 0 & 36 & 0 & 0 \\ 1 & 4 & 1 & 4 \\ 0 & 9 & 0 & 9 \end{pmatrix}.
\]

(d) \( \A^{-1} = \frac{1}{-2}\begin{pmatrix} -1 & 0 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} \frac12 & 0 \\ \frac12 & -1 \end{pmatrix} \) and \( \B^{-1} = \frac13\begin{pmatrix} 3 & -1 \\ 0 & 1 \end{pmatrix} \) by @thm-two-by-two-inverse. By @thm-kronecker-properties (e),
\[
(\A \otimes \B)^{-1} = \A^{-1} \otimes \B^{-1} = \begin{pmatrix} \frac12\B^{-1} & 0 \\ \frac12\B^{-1} & -\B^{-1} \end{pmatrix} = \begin{pmatrix} \frac12 & -\frac16 & 0 & 0 \\ 0 & \frac16 & 0 & 0 \\ \frac12 & -\frac16 & -1 & \frac13 \\ 0 & \frac16 & 0 & -\frac13 \end{pmatrix}.
\]
Multiplying by \( \A \otimes \B \) gives \( \I_4 \).
:::

:::: {#exr-kronecker-product-b2}
[B2: One-sided equations]

Let \( \A \in M_m(F) \) and \( \C \in M_{m \times n}(F) \), and consider \( \A \X = \C \) for \( \X \in M_{m \times n}(F) \).

::: {.enumerate options="label=(\alph*)"}
1. Write the equation in the form \( \M\vecop \X = \vecop \C \), and describe \( \M \) as a block matrix.
2. Explain why the system splits into \( n \) separate systems, one for each column of \( \X \).
3. Hence show that \( \A \X = \C \) has exactly one solution for every \( \C \) if and only if \( \A \) is invertible.
4. Solve \( \X \A = \C \) over \( \nQ \) by the same method, where \( \A = \begin{pmatrix} 1 & 2 \\ 1 & 3 \end{pmatrix} \) and \( \C = \begin{pmatrix} 3 & 7 \\ 0 & 1 \end{pmatrix} \).
:::
::::

::: {.solution}
(a) By @thm-vec-identity with \( \B = \I_n \), \( \vecop(\A \X) = (\I_n \otimes \A)\vecop \X \), so \( \M = \I_n \otimes \A = \A \oplus \dots \oplus \A \), with \( n \) blocks.

(b) Write \( \vecop \X \) and \( \vecop \C \) as stacks of the columns \( \x_j \) and \( \c_j \). By @thm-block-multiplication, \( (\A \oplus \dots \oplus \A)\vecop \X \) is the stack of the \( \A\x_j \). So the system says \( \A\x_j = \c_j \) for \( j = 1, \dots, n \), and the unknowns of different columns never meet.

(c) \( (\Leftarrow) \) If \( \A \) is invertible, then \( \A \X = \C \) forces \( \X = \A^{-1}\C \), and this \( \X \) is a solution. \( (\Rightarrow) \) Suppose \( \A \X = \C \) is solvable for every \( \C \). Given \( \c \in F^m \), take \( \C \) with every column equal to \( \c \); by (b), a solution gives \( \x \) with \( \A\x = \c \). So \( \A\x = \c \) is solvable for every \( \c \), and \( \A \) is invertible by @thm-invertible-tfae ((e) \( \Rightarrow \) (a)).

(d) By @thm-vec-identity with the left factor \( \I_2 \), \( \vecop(\X \A) = (\A\tp \otimes \I_2)\vecop \X \). With \( \A\tp = \begin{pmatrix} 1 & 1 \\ 2 & 3 \end{pmatrix} \), \( \vecop \X = (x_{11}, x_{21}, x_{12}, x_{22}) \) and \( \vecop \C = (3, 0, 7, 1) \), the system is
\[
\begin{pmatrix} 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \\ 2 & 0 & 3 & 0 \\ 0 & 2 & 0 & 3 \end{pmatrix}\begin{pmatrix} x_{11} \\ x_{21} \\ x_{12} \\ x_{22} \end{pmatrix} = \begin{pmatrix} 3 \\ 0 \\ 7 \\ 1 \end{pmatrix}.
\]
This time the system splits by the **rows** of \( \X \): equations \( 1, 3 \) involve only \( x_{11}, x_{12} \), and equations \( 2, 4 \) only \( x_{21}, x_{22} \). From \( x_{11} + x_{12} = 3 \) and \( 2x_{11} + 3x_{12} = 7 \) we get \( x_{12} = 1 \), \( x_{11} = 2 \). From \( x_{21} + x_{22} = 0 \) and \( 2x_{21} + 3x_{22} = 1 \) we get \( x_{22} = 1 \), \( x_{21} = -1 \). Hence
\[
\X = \begin{pmatrix} 2 & 1 \\ -1 & 1 \end{pmatrix}.
\]
*Check:* \( \X \A = \begin{pmatrix} 2 + 1 & 4 + 3 \\ -1 + 1 & -2 + 3 \end{pmatrix} = \begin{pmatrix} 3 & 7 \\ 0 & 1 \end{pmatrix} = \C \).
:::

:::: {#exr-kronecker-product-b3}
[B3: Which identities hold?]

Determine which of the following statements hold for **all** \( \A, \B, \C \in M_2(\nR) \). Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( (\A \otimes \B)(\A \otimes \B) = \A^2 \otimes \B^2 \).
2. \( (\A + \B) \otimes \C = \A \otimes \C + \B \otimes \C \).
3. \( (\A \otimes \B)\tp = \B\tp \otimes \A\tp \).
4. \( \A \otimes \B = 0 \) implies \( \A = 0 \) or \( \B = 0 \).
5. \( \tr(\A \otimes \B) = \tr(\B \otimes \A) \).
6. \( \A \otimes \B + \B \otimes \A = 2(\A \otimes \B) \).
:::
::::

::: {.solution}
(a) Holds, by the mixed product rule (@thm-kronecker-properties (c)).

(b) Holds, by bilinearity (@thm-kronecker-properties (a)).

(c) Fails. By @thm-kronecker-properties (d), \( (\A \otimes \B)\tp = \A\tp \otimes \B\tp \), and this differs from \( \B\tp \otimes \A\tp \) in general. Take \( \A = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix} \) and \( \B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \B\tp \). By \( (\ast) \), the \( (1, 2) \) entry of \( \A\tp \otimes \B\tp \) is \( (\A\tp)_{11}b_{12} = 1 \), while that of \( \B\tp \otimes \A\tp \) is \( b_{11}(\A\tp)_{12} = 0 \). Unlike \( (\A \B)\tp = \B\tp \A\tp \), the order of the factors does not reverse.

(d) Holds. If \( \A \ne 0 \) and \( \B \ne 0 \), then \( \rank \A \ge 1 \) and \( \rank \B \ge 1 \), so \( \rank(\A \otimes \B) \ge 1 \) by @thm-kronecker-rank-trace-det (a), and \( \A \otimes \B \ne 0 \). (Directly: if \( a_{ij} \ne 0 \) and \( b_{kl} \ne 0 \), the entry \( a_{ij}b_{kl} \) of \( \A \otimes \B \) is non-zero.)

(e) Holds: both equal \( \tr \A\tr \B \) by @thm-kronecker-rank-trace-det (b).

(f) Fails, since it is equivalent to \( \B \otimes \A = \A \otimes \B \), which is false for the matrices of Example 1 after @def-kronecker-product (see the non-example there).
:::

### C. Going deeper

:::: {#exr-kronecker-product-c1}
[C1: When is a Kronecker product invertible?]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \A \in M_n(F) \) and \( \B \in M_m(F) \). Prove that \( \A \otimes \B \) is invertible if and only if both \( \A \) and \( \B \) are invertible.
2. Let \( \A \in M_{m \times n}(F) \) and \( \B \in M_{p \times q}(F) \) with \( mp = nq \), so that \( \A \otimes \B \) is square. Prove that if \( m \ne n \), then \( \A \otimes \B \) is **not** invertible.
3. Give an example of a \( 2 \times 1 \) matrix \( \A \) and a \( 1 \times 2 \) matrix \( \B \) for which \( \A \otimes \B \) is a non-zero \( 2 \times 2 \) matrix, and compute its rank.
:::
::::

::: {.solution}
(a) By @thm-kronecker-rank-trace-det (c), \( \det(\A \otimes \B) = (\det \A)^m(\det \B)^n \). In a field a product is non-zero if and only if each factor is, so this is non-zero if and only if \( \det \A \ne 0 \) and \( \det \B \ne 0 \) (here \( n, m \ge 1 \)). By @thm-det-nonzero-iff-invertible, applied to all three matrices, \( \A \otimes \B \) is invertible if and only if \( \A \) and \( \B \) are.

(b) Suppose \( m < n \). Since \( mp = nq \) and \( m < n \), we get \( p > q \). By @thm-kronecker-rank-trace-det (a) and the bound \( \rank \M \le \) (number of rows) and \( \le \) (number of columns),
\[
\rank(\A \otimes \B) = \rank \A\rank \B \le m \cdot q < n \cdot q = nq,
\]
so the \( nq \times nq \) matrix \( \A \otimes \B \) is not invertible (@thm-invertible-tfae). If \( m > n \), then \( p < q \), and \( \rank \A\rank \B \le n \cdot p < m \cdot p = mp = nq \) in the same way.

(c) Take \( \A = \begin{pmatrix} 1 \\ 2 \end{pmatrix} \) and \( \B = \begin{pmatrix} 3 & 1 \end{pmatrix} \). Then \( \A \otimes \B = \begin{pmatrix} 1\B \\ 2\B \end{pmatrix} = \begin{pmatrix} 3 & 1 \\ 6 & 2 \end{pmatrix} \), the outer product \( \A \B \), of rank \( 1 \cdot 1 = 1 \): its second row is twice its first. So it is square and non-zero but singular, as (b) predicts.
:::

:::: {#exr-kronecker-product-c2}
[C2: Kronecker sums]

Let \( \A \in M_n(F) \) and \( \B \in M_m(F) \), and put \( \K \coloneqq \A \otimes \I_m + \I_n \otimes \B \in M_{nm}(F) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( (\A \otimes \I_m)(\I_n \otimes \B) = (\I_n \otimes \B)(\A \otimes \I_m) \), and deduce that \( \K^2 = \A^2 \otimes \I_m + 2(\A \otimes \B) + \I_n \otimes \B^2 \).
2. Show that for \( \X \in M_{m \times n}(F) \), \( \vecop(\B \X + \X \A\tp) = \K\vecop \X \).
3. Suppose \( \A \) and \( \B \) are upper triangular. Prove that \( \K \) is upper triangular with diagonal entries \( a_{ii} + b_{kk} \), and deduce that \( \B \X + \X \A\tp = \C \) has exactly one solution for every \( \C \in M_{m \times n}(F) \) if and only if \( a_{ii} + b_{kk} \ne 0 \) for all \( i, k \).
4. For \( \A = \begin{pmatrix} 1 & 2 \\ 0 & -1 \end{pmatrix} \) and \( \B = \begin{pmatrix} 1 & 0 \\ 0 & 3 \end{pmatrix} \) over \( \nQ \), decide whether \( \B \X + \X \A\tp = \C \) is solvable for every \( \C \). If not, find a \( \C \) with no solution.
:::
::::

::: {.solution}
(a) By the mixed product rule, both products equal \( (\A \I_n) \otimes (\I_m\B) = (\I_n\A) \otimes (\B \I_m) = \A \otimes \B \), as in \( (\ast\ast) \). Expanding \( \K^2 \) by distributivity (@thm-matrix-multiplication-properties) gives \( (\A \otimes \I_m)^2 + (\A \otimes \I_m)(\I_n \otimes \B) + (\I_n \otimes \B)(\A \otimes \I_m) + (\I_n \otimes \B)^2 \). The middle terms are both \( \A \otimes \B \), and the outer ones are \( \A^2 \otimes \I_m \) and \( \I_n \otimes \B^2 \) by the mixed product rule.

(b) By @thm-vec-identity, \( \vecop(\B \X \I_n) = (\I_n \otimes \B)\vecop \X \) and \( \vecop(\I_m\X \A\tp) = ((\A\tp)\tp \otimes \I_m)\vecop \X = (\A \otimes \I_m)\vecop \X \). Add, using linearity of \( \vecop \).

(c) By \( (\ast) \), the entry of \( \A \otimes \I_m \) in position \( ((i-1)m + k, (j-1)m + l) \) is \( a_{ij}\delta_{kl} \), which is zero unless \( i \le j \) and \( k = l \); in that case \( (i-1)m + k \le (j-1)m + l \). The entry of \( \I_n \otimes \B \) there is \( \delta_{ij}b_{kl} \), zero unless \( i = j \) and \( k \le l \), and again the row index is at most the column index. So both are upper triangular, hence so is \( \K \). On the diagonal, \( i = j \) and \( k = l \), and the entry is \( a_{ii} + b_{kk} \). By @thm-det-triangular, \( \det \K = \prod_{i,k}(a_{ii} + b_{kk}) \). By (b), the equation is \( \K\vecop \X = \vecop \C \), and since \( \vecop \) is an isomorphism, it has exactly one solution for every \( \C \) if and only if \( \K \) is invertible (@thm-invertible-tfae), that is \( \det \K \ne 0 \) (@thm-det-nonzero-iff-invertible), that is every \( a_{ii} + b_{kk} \ne 0 \).

(d) The diagonal entries \( a_{ii} + b_{kk} \) are \( 1 + 1 = 2 \), \( 1 + 3 = 4 \), \( -1 + 1 = 0 \), \( -1 + 3 = 2 \), so by (c) the equation is not solvable for every \( \C \). Explicitly,
\[
\K = \begin{pmatrix} 1\I_2 & 2\I_2 \\ 0\I_2 & -1\I_2 \end{pmatrix} + \begin{pmatrix} \B & 0 \\ 0 & \B \end{pmatrix} = \begin{pmatrix} 2 & 0 & 2 & 0 \\ 0 & 4 & 0 & 2 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 2 \end{pmatrix},
\]
whose third row is zero. So \( \K\vecop \X \) always has third entry \( 0 \), and any \( \C \) with \( (\vecop \C)_3 = c_{12} \ne 0 \) has no solution, for example \( \C = \E_{12} \). (Directly: the \( (1, 2) \) entry of \( \B \X + \X \A\tp \) is \( x_{12} + (x_{11}a_{21} + x_{12}a_{22}) = x_{12} - x_{12} = 0 \).)
:::
