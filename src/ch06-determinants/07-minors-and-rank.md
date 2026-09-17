# Minors, Rank and Cauchy–Binet

The determinant of a square matrix answers a yes-or-no question: is the matrix invertible? A rectangular matrix has no determinant, and a singular square matrix has determinant \( 0 \), which says nothing about *how* singular it is. Yet every matrix is full of square pieces, and each piece has a determinant. This section shows that these small determinants measure the rank exactly. It then answers a second question left open by multiplicativity: if \( A \) is \( m \times n \) and \( B \) is \( n \times m \), the product \( AB \) is square, so what is \( \det(AB) \)? The answer, the Cauchy–Binet formula, is proved by the same multilinear expansion that gave uniqueness of the determinant in @thm-alternating-form-uniqueness.

## Submatrices and minors

In @def-minor-cofactor we deleted one row and one column of a square matrix and took the determinant of what was left. That is a special case of a more flexible operation: keep **any** \( k \) rows and **any** \( k \) columns. The recurring object is the square block sitting at the crossings of the chosen rows and columns, and it deserves a name.

*A minor is the determinant of a square block cut out of a matrix by choosing some rows and the same number of columns.*

For a positive integer \( m \), write \( [m] = \{1, 2, \dots, m\} \).

::: {#def-submatrix-minor}
[Submatrix and Minor]

Let \( A = (a_{ij}) \in M_{m \times n}(F) \), and let \( 1 \le k \le \min(m, n) \). Let \( I = \{i_1 < i_2 < \dots < i_k\} \subseteq [m] \) and \( J = \{j_1 < j_2 < \dots < j_k\} \subseteq [n] \) be sets with **exactly \( k \)** elements each, listed in **increasing** order. The **submatrix** of \( A \) on rows \( I \) and columns \( J \) is
\[
A_{I,J} \coloneqq \big(a_{i_p j_q}\big)_{p, q = 1}^{k} \in M_k(F),
\]
the \( k \times k \) matrix whose \( (p, q) \)-entry is \( a_{i_p j_q} \). Its determinant \( \det A_{I,J} \) is a **\( k \times k \) minor** of \( A \).
:::

In words: cross out every row not in \( I \) and every column not in \( J \), and push the surviving entries together **without changing their order**. The chosen rows need not be adjacent, and neither need the columns. The sets \( I \) and \( J \) have the **same** size, so the block is square and has a determinant.

A \( 1 \times 1 \) minor is a single entry, \( \det A_{\{i\},\{j\}} = a_{ij} \). For a square \( A \in M_n(F) \) with \( n \ge 2 \), the minor \( M_{ij} \) of @def-minor-cofactor is the \( (n - 1) \times (n - 1) \) minor with \( I = [n] \setminus \{i\} \) and \( J = [n] \setminus \{j\} \). The only \( n \times n \) minor of a square matrix is \( \det A \) itself. An \( m \times n \) matrix has \( \binom{m}{k}\binom{n}{k} \) minors of size \( k \), one for each choice of \( I \) and \( J \).

**Example.** Let
\[
A = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 3 \end{pmatrix} \in M_{2 \times 3}(\nQ).
\]
Its \( 2 \times 2 \) minors all use \( I = \{1, 2\} \), and there are three choices of \( J \):
\[
\det A_{I,\{1,2\}} = \det\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} = 1, \quad
\det A_{I,\{1,3\}} = \det\begin{pmatrix} 1 & 0 \\ 0 & 3 \end{pmatrix} = 3, \quad
\det A_{I,\{2,3\}} = \det\begin{pmatrix} 2 & 0 \\ 1 & 3 \end{pmatrix} = 6.
\]
Its six \( 1 \times 1 \) minors are its entries. It has no \( 3 \times 3 \) minors, since it has only two rows.

**A degenerate example.** Every minor of the zero matrix \( 0_{m \times n} \) is \( 0 \): each block is a zero matrix, whose determinant is \( 0 \) by @thm-det-triangular. This case matters because it is exactly the matrix of rank \( 0 \), and the theorem below has to treat it separately.

**Non-example by minimal change.** Take the same rows and columns but list the columns of \( A \) above in the order \( 3, 1 \): the block \( \begin{pmatrix} 0 & 1 \\ 3 & 0 \end{pmatrix} \) has determinant \( -3 \), not \( 3 \). Every entry is still an entry of \( A \) from rows \( \{1, 2\} \) and columns \( \{1, 3\} \); what fails is the clause **listed in increasing order**. Reordering columns changes the determinant by a sign (@thm-alternating-properties), so the order convention is what makes "the" minor on \( (I, J) \) a single well-defined number.

**Why this definition.** Insisting on increasing order costs nothing and removes all sign ambiguity. Insisting on \( |I| = |J| \) is forced: only square blocks have determinants.

::: {.warning}
**Rank is not read off principal minors.** A **principal** minor uses the same index set for rows and columns (\( I = J \)). It is tempting to test rank using only these, but they can all vanish for a non-zero matrix. For \( N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \), the principal minors are \( 0 \), \( 0 \) and \( \det N = 0 \), yet \( \rank N = 1 \). The non-zero minor is the off-diagonal entry \( \det N_{\{1\},\{2\}} = 1 \). The theorem below uses **all** minors.
:::

::: {.check}
How many \( 2 \times 2 \) minors does a \( 3 \times 4 \) matrix have? How many \( 3 \times 3 \) minors?
:::

::: {.solution}
A \( 2 \times 2 \) minor needs \( 2 \) of the \( 3 \) rows and \( 2 \) of the \( 4 \) columns: \( \binom{3}{2}\binom{4}{2} = 3 \cdot 6 = 18 \). A \( 3 \times 3 \) minor uses all three rows and \( 3 \) of the \( 4 \) columns: \( \binom{3}{3}\binom{4}{3} = 4 \).
:::

## Rank via minors

A non-zero determinant of a square block means the block is invertible, so its columns are independent. Independent columns inside a block come from independent columns of the whole matrix. So a large non-zero minor forces large rank. The converse, that large rank produces a large non-zero minor, needs us to find the right rows as well as the right columns. Both directions together give a description of rank using only determinants:

::: {#thm-rank-via-minors}
[Rank via Minors]

Let \( A \in M_{m \times n}(F) \) be **non-zero**.

::: {.enumerate options="label=(\alph*)"}
1. \( \rank A \) is the **largest** integer \( k \) such that \( A \) has a **non-zero** \( k \times k \) minor.
2. Equivalently, for each \( 1 \le k \le \min(m, n) \): \( \rank A \ge k \) if and only if some \( k \times k \) minor of \( A \) is non-zero; and \( \rank A < k \) if and only if **every** \( k \times k \) minor of \( A \) is zero.
:::
:::

::: {.idea}
Two inequalities. ① A non-zero \( k \times k \) minor on rows \( I \) and columns \( J \) makes \( A_{I,J} \) invertible; a dependence among the columns of \( A \) indexed by \( J \) would restrict to a dependence among the columns of \( A_{I,J} \). So \( \rank A \ge k \). ② If \( \rank A = r \), choose \( r \) independent columns (pivot columns). The \( m \times r \) matrix they form has rank \( r \), so by row rank = column rank it has \( r \) independent rows. Those rows cut out an \( r \times r \) block with independent rows, hence a non-zero determinant.
:::

::: {.proof}
**Step 1: a non-zero \( k \times k \) minor forces \( \rank A \ge k \).** Let \( I = \{i_1 < \dots < i_k\} \) and \( J = \{j_1 < \dots < j_k\} \) with \( \det A_{I,J} \ne 0 \). Write \( \a_1, \dots, \a_n \) for the columns of \( A \). Suppose \( c_1\a_{j_1} + \dots + c_k\a_{j_k} = \0 \) with \( c_1, \dots, c_k \in F \). Reading only the entries in rows \( i_1, \dots, i_k \) of this vector equation gives \( \sum_{q} c_q\, a_{i_p j_q} = 0 \) for \( p = 1, \dots, k \), that is, \( A_{I,J}\c = \0 \) with \( \c = (c_1, \dots, c_k) \). By @thm-det-nonzero-iff-invertible, \( A_{I,J} \) is invertible, so \( \c = \0 \) by @thm-invertible-tfae. Hence \( (\a_{j_1}, \dots, \a_{j_k}) \) is a linearly independent list in \( \col(A) \), and by @thm-size-bounds (a), \( k \le \dim\col(A) = \rank A \).

**Step 2: \( A \) has a non-zero \( r \times r \) minor, where \( r = \rank A \).** Since \( A \ne 0 \), some column is non-zero, so \( r \ge 1 \). By @thm-basis-column-space (a), the pivot columns \( \a_{j_1}, \dots, \a_{j_r} \) (\( j_1 < \dots < j_r \)) are linearly independent. Let \( J = \{j_1, \dots, j_r\} \) and let \( A' = A_{[m],J} \in M_{m \times r}(F) \) be the matrix with these columns. By @thm-independence-spanning-by-rank (a), \( \rank A' = r \), so by @thm-row-rank-equals-column-rank the row space of \( A' \) has dimension \( r \). The \( m \) rows of \( A' \) span its row space, so by @thm-sift some \( r \) of them, in rows \( i_1 < \dots < i_r \), form a basis of it; in particular they are linearly independent. These are exactly the rows of \( B = A_{I,J} \in M_r(F) \), where \( I = \{i_1, \dots, i_r\} \). Transposition is a linear bijection from \( 1 \times r \) rows to columns in \( F^r \), so the columns of \( B\tp \) are linearly independent. By @thm-invertible-tfae, \( B\tp \) is invertible, so \( \det B\tp \ne 0 \) by @thm-det-nonzero-iff-invertible, and \( \det B = \det B\tp \ne 0 \) by @thm-det-transpose.

**Conclusion.** By Step 2 there is a non-zero minor of size \( r \), and by Step 1 there is none of size larger than \( r \). This proves (a). For (b): if \( \rank A \ge k \), then Step 2 gives a non-zero \( r \times r \) minor with \( r \ge k \), and we still need one of size exactly \( k \). Expanding that \( r \times r \) determinant along any row (@thm-laplace-expansion) writes it as a combination of \( (r-1) \times (r-1) \) minors of the block, each of which is also an \( (r-1) \times (r-1) \) minor of \( A \); since the determinant is non-zero, one of these minors is non-zero. Repeating \( r - k \) times gives a non-zero \( k \times k \) minor. Conversely, a non-zero \( k \times k \) minor gives \( \rank A \ge k \) by Step 1. The second equivalence in (b) is the negation of the first.
:::

The theorem turns "rank at most \( k - 1 \)" into a finite list of polynomial equations in the entries: all \( k \times k \) minors vanish. That is why rank can only **drop** when the entries satisfy special equations, as the next example shows.

::: {#exm-rank-by-minors}
[Rank of a Family of Matrices]

For \( t \in \nQ \), let
\[
A(t) = \begin{pmatrix} 1 & 2 & 1 \\ 2 & t & 3 \\ 3 & 6 & t \end{pmatrix}.
\]
Find \( \rank A(t) \) for every \( t \).
:::

::: {.solution}
The only \( 3 \times 3 \) minor is \( \det A(t) \). By cofactor expansion along the first row (@thm-laplace-expansion),
\[
\det A(t) = 1\cdot(t^2 - 18) - 2\cdot(2t - 9) + 1\cdot(12 - 3t) = t^2 - 7t + 12 = (t - 3)(t - 4).
\]
So for \( t \ne 3, 4 \), \( A(t) \) has a non-zero \( 3 \times 3 \) minor and \( \rank A(t) = 3 \) by @thm-rank-via-minors.

For \( t \in \{3, 4\} \) every \( 3 \times 3 \) minor is zero, so \( \rank A(t) \le 2 \). Look for a \( 2 \times 2 \) minor that does not involve \( t \): rows \( \{1, 2\} \) and columns \( \{1, 3\} \) give
\[
\det\begin{pmatrix} 1 & 1 \\ 2 & 3 \end{pmatrix} = 1 \ne 0 .
\]
Hence \( \rank A(3) = \rank A(4) = 2 \). The same minor shows \( \rank A(t) \ge 2 \) for every \( t \), so rank \( 1 \) never occurs.
:::

::: {.remark}
To **compute** the rank of one given matrix, elimination is far cheaper: a \( 10 \times 10 \) matrix has \( \binom{10}{5}^2 = 63504 \) minors of size \( 5 \). Minors earn their keep in theory. They show that rank is unchanged by transposing (the minors of \( A\tp \) are the minors of \( A \), by @thm-det-transpose) and by enlarging the field (@exr-minors-and-rank-c2), and they describe the matrices of rank below \( k \) by polynomial equations.
:::

## The Cauchy–Binet formula

Multiplicativity, @thm-det-multiplicative, handles \( \det(AB) \) when both factors are square. Now let \( A \in M_{m \times n}(F) \) and \( B \in M_{n \times m}(F) \). The product \( AB \) is \( m \times m \), so it has a determinant, but \( \det A \) and \( \det B \) do not exist. The natural candidates to replace them are the largest minors: the \( m \times m \) minors of \( A \), which keep all rows and choose \( m \) columns \( S \), and the \( m \times m \) minors of \( B \), which keep all columns and choose the **same** \( m \) rows \( S \).

::: {#thm-cauchy-binet}
[Cauchy–Binet Formula]

Let \( A \in M_{m \times n}(F) \) and \( B \in M_{n \times m}(F) \). Then
\[
\det(AB) = \sum_{\substack{S \subseteq [n] \\ |S| = m}} \det A_{[m],S}\, \det B_{S,[m]} ,
\]
the sum running over all \( m \)-element subsets \( S \) of \( [n] \). In particular:

::: {.enumerate options="label=(\alph*)"}
1. if \( m > n \), the sum is empty and \( \det(AB) = 0 \);
2. if \( m = n \), the only subset is \( S = [n] \) and the formula is \( \det(AB) = \det A \det B \).
:::
:::

::: {.idea}
Treat \( \det \) as a function of the \( m \) columns of \( AB \). Column \( k \) of \( AB \) is \( A\b_k = \sum_j b_{jk}\a_j \), a combination of the columns of \( A \). Expand by multilinearity in all \( m \) columns at once, exactly as in the uniqueness proof: one term for each way of picking a column \( \a_{\varphi(k)} \) of \( A \) in slot \( k \). ① Terms that pick the same column twice vanish, because the determinant is alternating. ② The surviving picks use \( m \) **distinct** columns, forming a set \( S \), in some order; putting them in increasing order costs the sign of the reordering (@lem-alternating-permute-arguments). ③ Collecting all orders of the same \( S \) produces a Leibniz sum, which is \( \det B_{S,[m]} \).
:::

::: {.proof}
Write \( \a_1, \dots, \a_n \in F^m \) for the columns of \( A \) and \( b_{jk} \) for the entries of \( B \). For \( \x_1, \dots, \x_m \in F^m \), the function \( D(\x_1, \dots, \x_m) = \det(\x_1, \dots, \x_m) \) is an alternating \( m \)-linear form by @thm-leibniz-formula-alternating.

By @thm-three-views-of-product, column \( k \) of \( AB \) is \( A\b_k = \sum_{j=1}^{n} b_{jk}\a_j \). Expanding \( D \) by linearity in each of its \( m \) arguments in turn,
\[
\det(AB) = D\Big(\sum_{j=1}^{n} b_{j1}\a_j, \dots, \sum_{j=1}^{n} b_{jm}\a_j\Big) = \sum_{\varphi} \Big(\prod_{k=1}^{m} b_{\varphi(k)k}\Big)\, D(\a_{\varphi(1)}, \dots, \a_{\varphi(m)}),
\]
where \( \varphi \) runs over **all** functions \( [m] \to [n] \). If \( \varphi \) is not injective, two arguments of \( D \) are equal and the term is \( 0 \) because \( D \) is alternating (@def-alternating-form). So only injective \( \varphi \) contribute. In particular, if \( m > n \) there is no injective \( \varphi \), and \( \det(AB) = 0 \), which proves (a).

An injective \( \varphi \) has an image \( S = \{s_1 < \dots < s_m\} \subseteq [n] \) with \( m \) elements, and then \( \varphi(k) = s_{\pi(k)} \) for exactly one \( \pi \in S_m \). Conversely each pair \( (S, \pi) \) gives an injective \( \varphi \). By @lem-alternating-permute-arguments with \( \v_p = \a_{s_p} \),
\[
D(\a_{\varphi(1)}, \dots, \a_{\varphi(m)}) = \sgn(\pi)\, D(\a_{s_1}, \dots, \a_{s_m}) = \sgn(\pi)\, \det A_{[m],S},
\]
since \( A_{[m],S} \) has columns \( \a_{s_1}, \dots, \a_{s_m} \). Hence
\[
\det(AB) = \sum_{|S| = m} \det A_{[m],S} \sum_{\pi \in S_m} \sgn(\pi) \prod_{k=1}^{m} b_{s_{\pi(k)}k} .
\]
The matrix \( B_{S,[m]} \) has \( (p, k) \)-entry \( b_{s_p k} \), so its \( (\pi(k), k) \)-entry is \( b_{s_{\pi(k)}k} \), and the inner sum is \( \det B_{S,[m]} \) by @def-determinant. This proves the formula. For \( m = n \), the only \( S \) is \( [n] \), with \( A_{[n],[n]} = A \) and \( B_{[n],[n]} = B \), which gives (b).
:::

Part (b) is a second proof of multiplicativity, and part (a) matches what rank predicts: if \( m > n \), then \( \rank(AB) \le \rank A \le n < m \) by @thm-rank-product-inequality, so \( AB \) is not invertible. The formula also passes a sanity check at \( m = 1 \): a \( 1 \times n \) row times an \( n \times 1 \) column is the \( 1 \times 1 \) matrix \( \sum_j a_{1j}b_{j1} \), and the \( 1 \times 1 \) minors are single entries.

::: {.remark}
The proof uses only sums, differences and products of entries, together with @lem-alternating-permute-arguments, which is division-free by the remark in §4. So, like the results flagged in §4–§6, the Cauchy–Binet formula holds for matrices with entries in any commutative ring.
:::

::: {#exm-cauchy-binet}
[Cauchy–Binet for a \( 2 \times 3 \) times \( 3 \times 2 \) Product]

Let
\[
A = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 3 \end{pmatrix}, \qquad B = \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 2 & -1 \end{pmatrix}
\]
over \( \nQ \). Compute \( \det(AB) \) directly and by the Cauchy–Binet formula. Then compute \( \det(BA) \).
:::

::: {.solution}
*Directly.* \( AB = \begin{pmatrix} 1 + 2 + 0 & 0 + 2 + 0 \\ 0 + 1 + 6 & 0 + 1 - 3 \end{pmatrix} = \begin{pmatrix} 3 & 2 \\ 7 & -2 \end{pmatrix} \), so \( \det(AB) = -6 - 14 = -20 \).

*By Cauchy–Binet.* Here \( m = 2 \), \( n = 3 \), and there are three subsets \( S \). The minors of \( A \) were computed after @def-submatrix-minor. The minors of \( B \) keep both columns and rows \( S \):

| \( S \) | \( \det A_{[2],S} \) | \( \det B_{S,[2]} \) | product |
|---|---|---|---|
| \( \{1, 2\} \) | \( 1 \) | \( \det\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} = 1 \) | \( 1 \) |
| \( \{1, 3\} \) | \( 3 \) | \( \det\begin{pmatrix} 1 & 0 \\ 2 & -1 \end{pmatrix} = -1 \) | \( -3 \) |
| \( \{2, 3\} \) | \( 6 \) | \( \det\begin{pmatrix} 1 & 1 \\ 2 & -1 \end{pmatrix} = -3 \) | \( -18 \) |

The sum is \( 1 - 3 - 18 = -20 \), in agreement.

*The other product.* \( BA \) is \( 3 \times 3 \), and here the roles are \( m = 3 > n = 2 \), so \( \det(BA) = 0 \) by @thm-cauchy-binet (a). Indeed \( BA = \begin{pmatrix} 1 & 2 & 0 \\ 1 & 3 & 3 \\ 2 & 3 & -3 \end{pmatrix} \), whose third row is \( 3 \) times the first minus the second, so \( \det(BA) = 0 \).
:::

::: {.warning}
**For non-square factors, \( \det(AB) \) and \( \det(BA) \) differ.** For square matrices \( \det(AB) = \det A\det B = \det(BA) \). In the example above, \( \det(AB) = -20 \) while \( \det(BA) = 0 \). An even smaller case: \( A = \begin{pmatrix} 1 & 1 \end{pmatrix} \) and \( B = \begin{pmatrix} 1 \\ 1 \end{pmatrix} \) give \( AB = (2) \) and \( BA = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \), with determinants \( 2 \) and \( 0 \). Also, do not write "\( \det A \det B \)" for non-square \( A \), \( B \): those symbols are undefined, and the sum over \( S \) is what replaces them.
:::

::: {.check}
Let \( \u, \v \in F^n \) with \( n \ge 2 \). Without computing, what is \( \det(\u\v\tp) \)?
:::

::: {.solution}
\( \u\v\tp \) is the product of the \( n \times 1 \) matrix \( \u \) and the \( 1 \times n \) matrix \( \v\tp \). Here the product is \( n \times n \) and the middle size is \( 1 < n \), so \( \det(\u\v\tp) = 0 \) by @thm-cauchy-binet (a).
:::

## Sums of squares over the reals

Over \( \nR \), take \( B = A\tp \). The minors of \( A\tp \) are the minors of \( A \) with rows and columns exchanged, so Cauchy–Binet writes \( \det(AA\tp) \) as a sum of squares.

::: {#cor-gram-determinant-nonnegative}
[Gram Determinants Are Non-negative]

Let \( A \in M_{m \times n}(\nR) \). Then
\[
\det(AA\tp) = \sum_{\substack{S \subseteq [n] \\ |S| = m}} \big(\det A_{[m],S}\big)^2 \ \ge\ 0,
\]
with equality if and only if \( \rank A < m \).
:::

::: {.proof}
By @def-transpose, the \( (p, k) \)-entry of \( (A\tp)_{S,[m]} \) is the \( (k, s_p) \)-entry of \( A \), so \( (A\tp)_{S,[m]} = (A_{[m],S})\tp \). By @thm-det-transpose, \( \det (A\tp)_{S,[m]} = \det A_{[m],S} \). Substituting into @thm-cauchy-binet with \( B = A\tp \) gives the formula. A sum of squares of real numbers is \( \ge 0 \), and it is \( 0 \) if and only if every term is \( 0 \). Every \( m \times m \) minor of \( A \) has the form \( \det A_{[m],S} \), since an \( m \times m \) minor must use all \( m \) rows. If \( m > n \), the sum is empty and \( \rank A \le n < m \). Otherwise, by @thm-rank-via-minors (b) (or directly if \( A = 0 \)), all these minors vanish if and only if \( \rank A < m \).
:::

The matrix \( AA\tp \) collects the dot products of the rows of \( A \) with each other. Such matrices of pairwise inner products are **Gram matrices**; Chapters 10 and 12 study them, and there this corollary becomes the statement that a Gram matrix is positive semidefinite. For \( m = 2 \) the corollary is a classical identity about two vectors, @exr-minors-and-rank-b3. Over \( \nC \) or \( \nF_p \) the conclusion "\( \ge 0 \)" has no meaning, and the equality case can fail: over \( \nC \), \( A = \begin{pmatrix} 1 & i \end{pmatrix} \) has rank \( 1 \) but \( AA\tp = (1 + i^2) = (0) \).

## Exercises

### A. Check your understanding

:::: {#exr-minors-and-rank-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the \( k \times k \) minor of \( A \in M_{m \times n}(F) \) on rows \( I \) and columns \( J \).
2. True or false: if every principal minor of a square matrix is zero, the matrix is zero. Justify your answer.
3. True or false: if \( A \in M_{4 \times 5}(F) \) has a non-zero \( 3 \times 3 \) minor, then \( \rank A \ge 3 \). Justify your answer.
4. True or false: if \( A \in M_{3}(F) \) has a zero \( 2 \times 2 \) minor, then \( \rank A \le 1 \). Justify your answer.
5. State the Cauchy–Binet formula, and say what it gives when \( m > n \).
6. Let \( A \in M_{2 \times 3}(\nR) \). Why is \( \det(A\tp A) = 0 \)?
:::
::::

::: {.solution}
(a) For \( I = \{i_1 < \dots < i_k\} \subseteq [m] \) and \( J = \{j_1 < \dots < j_k\} \subseteq [n] \), it is \( \det A_{I,J} \), where \( A_{I,J} \in M_k(F) \) has \( (p, q) \)-entry \( a_{i_pj_q} \) (@def-submatrix-minor).

(b) False. \( N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) has principal minors \( 0, 0, 0 \) but \( N \ne 0 \).

(c) True, by Step 1 of the proof of @thm-rank-via-minors, or by part (b) of that theorem.

(d) False. The rank is decided by whether **some** minor is non-zero, not by one zero minor. \( I_3 \) has the zero \( 2 \times 2 \) minor on rows \( \{1, 2\} \) and columns \( \{2, 3\} \), namely \( \det\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} = 0 \), but \( \rank I_3 = 3 \).

(e) For \( A \in M_{m \times n}(F) \) and \( B \in M_{n \times m}(F) \), \( \det(AB) = \sum_{|S| = m} \det A_{[m],S}\det B_{S,[m]} \), summed over \( m \)-subsets \( S \subseteq [n] \). If \( m > n \) there are no such subsets and \( \det(AB) = 0 \).

(f) \( A\tp A \) is \( 3 \times 3 \), the product of a \( 3 \times 2 \) and a \( 2 \times 3 \) matrix. By @thm-cauchy-binet (a) with \( m = 3 > n = 2 \), \( \det(A\tp A) = 0 \).
:::

### B. Practice

:::: {#exr-minors-and-rank-b1}
[B1: Rank with a parameter]

For \( s \in \nQ \), let \( A(s) = \begin{pmatrix} 1 & s & 1 \\ s & 1 & 1 \\ 1 & 1 & s \end{pmatrix} \). Use minors to find \( \rank A(s) \) for every \( s \).
::::

::: {.solution}
By cofactor expansion along the first row (@thm-laplace-expansion),
\[
\det A(s) = 1\cdot(s - 1) - s\,(s^2 - 1) + 1\cdot(s - 1) = -s^3 + 3s - 2 = -(s - 1)^2(s + 2).
\]
If \( s \ne 1, -2 \), this \( 3 \times 3 \) minor is non-zero, so \( \rank A(s) = 3 \) by @thm-rank-via-minors.

If \( s = -2 \), then \( \det A(-2) = 0 \), so \( \rank A(-2) \le 2 \). The minor on rows \( \{1, 2\} \) and columns \( \{1, 2\} \) is \( \det\begin{pmatrix} 1 & -2 \\ -2 & 1 \end{pmatrix} = 1 - 4 = -3 \ne 0 \). Hence \( \rank A(-2) = 2 \).

If \( s = 1 \), every entry is \( 1 \). Every \( 2 \times 2 \) minor is \( \det\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} = 0 \), and the \( 1 \times 1 \) minors are non-zero. Hence \( \rank A(1) = 1 \).
:::

:::: {#exr-minors-and-rank-b2}
[B2: Checking Cauchy–Binet]

Let \( A = \begin{pmatrix} 1 & 0 & 2 \\ -1 & 1 & 1 \end{pmatrix} \) and \( B = \begin{pmatrix} 2 & 1 \\ 0 & 1 \\ 1 & -1 \end{pmatrix} \) over \( \nQ \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \det(AB) \) directly.
2. Compute \( \det(AB) \) by the Cauchy–Binet formula.
3. Hence, without multiplying, find \( \det(BA) \).
:::
::::

::: {.solution}
(a) \( AB = \begin{pmatrix} 2 + 0 + 2 & 1 + 0 - 2 \\ -2 + 0 + 1 & -1 + 1 - 1 \end{pmatrix} = \begin{pmatrix} 4 & -1 \\ -1 & -1 \end{pmatrix} \), so \( \det(AB) = -4 - 1 = -5 \).

(b) The three subsets of \( [3] \) of size \( 2 \) give
\[
\begin{aligned}
S = \{1, 2\}&: \ \det\begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix}\det\begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix} = 1 \cdot 2 = 2, \\
S = \{1, 3\}&: \ \det\begin{pmatrix} 1 & 2 \\ -1 & 1 \end{pmatrix}\det\begin{pmatrix} 2 & 1 \\ 1 & -1 \end{pmatrix} = 3 \cdot (-3) = -9, \\
S = \{2, 3\}&: \ \det\begin{pmatrix} 0 & 2 \\ 1 & 1 \end{pmatrix}\det\begin{pmatrix} 0 & 1 \\ 1 & -1 \end{pmatrix} = (-2)(-1) = 2 .
\end{aligned}
\]
The sum is \( 2 - 9 + 2 = -5 \), agreeing with (a).

(c) \( BA \in M_3(\nQ) \) is a product through \( F^2 \), so \( \det(BA) = 0 \) by @thm-cauchy-binet (a).
:::

:::: {#exr-minors-and-rank-b3}
[B3: The Lagrange identity]

Let \( \a = (a_1, \dots, a_n) \) and \( \b = (b_1, \dots, b_n) \) be vectors in \( \nR^n \), \( n \ge 2 \), and write \( \a \cdot \b = \sum_i a_ib_i \).

::: {.enumerate options="label=(\alph*)"}
1. Let \( M \in M_{2 \times n}(\nR) \) have rows \( \a\tp \) and \( \b\tp \). Compute \( MM\tp \).
2. Hence prove the **Lagrange identity**
\[
(\a \cdot \a)(\b \cdot \b) - (\a \cdot \b)^2 = \sum_{1 \le i < j \le n} (a_ib_j - a_jb_i)^2 .
\]
3. Check it for \( \a = (1, 2, 3) \) and \( \b = (4, 5, 6) \), and deduce \( (\a \cdot \b)^2 \le (\a \cdot \a)(\b \cdot \b) \) for all \( \a, \b \in \nR^n \).
:::
::::

::: {.solution}
(a) By @thm-three-views-of-product, the \( (p, q) \)-entry of \( MM\tp \) is row \( p \) of \( M \) times column \( q \) of \( M\tp \), which is row \( q \) of \( M \) transposed. Hence
\[
MM\tp = \begin{pmatrix} \a \cdot \a & \a \cdot \b \\ \b \cdot \a & \b \cdot \b \end{pmatrix}, \qquad \b \cdot \a = \a \cdot \b .
\]

(b) The left side of the identity is \( \det(MM\tp) \). By @cor-gram-determinant-nonnegative with \( m = 2 \), it equals the sum over \( S = \{i < j\} \) of \( (\det M_{[2],S})^2 \), and \( M_{[2],\{i,j\}} = \begin{pmatrix} a_i & a_j \\ b_i & b_j \end{pmatrix} \) has determinant \( a_ib_j - a_jb_i \). This proves the identity.

(c) Left side: \( \a \cdot \a = 14 \), \( \b \cdot \b = 77 \), \( \a \cdot \b = 32 \), so \( 14 \cdot 77 - 32^2 = 1078 - 1024 = 54 \). Right side: the pairs \( (1,2), (1,3), (2,3) \) give \( 5 - 8 = -3 \), \( 6 - 12 = -6 \), \( 12 - 15 = -3 \), and \( 9 + 36 + 9 = 54 \). In general the right side is a sum of squares of reals, hence \( \ge 0 \), so \( (\a \cdot \b)^2 \le (\a \cdot \a)(\b \cdot \b) \).
:::

### C. Going deeper

:::: {#exr-minors-and-rank-c1}
[C1: Counting spanning trees]

Consider the network with vertices \( 1, 2, 3, 4 \) and five edges, oriented as \( e_1 = 1 \to 2 \), \( e_2 = 2 \to 3 \), \( e_3 = 3 \to 4 \), \( e_4 = 4 \to 1 \), \( e_5 = 1 \to 3 \). A **spanning tree** is a set of \( 3 \) edges that connects all four vertices (ignoring orientation). Let \( N \in M_{4 \times 5}(\nR) \) be its incidence matrix (@def-incidence-matrix), let \( L = NN\tp \), and let \( N_0 \) and \( L_0 \) be \( N \) and \( L \) with the row (and, for \( L \), the column) of vertex \( 4 \) deleted.

::: {.enumerate options="label=(\alph*)"}
1. Compute \( L \) and \( \det L_0 \).
2. List the spanning trees and count them.
3. Show that \( L_0 = N_0N_0\tp \), and use @cor-gram-determinant-nonnegative to write \( \det L_0 \) as a sum over \( 3 \)-element sets of edges.
4. Compute the minor of \( N_0 \) for the tree \( \{e_1, e_2, e_3\} \) and for the non-tree \( \{e_1, e_2, e_5\} \). Explain, for these two sets, why the answers are \( \pm 1 \) and \( 0 \).
:::

The **matrix-tree theorem** says that for every connected network, \( \det L_0 \) equals the number of spanning trees; parts (c) and (d) are the heart of its proof, which Chapter 23 completes.

*Hint: for (d), a set of edges containing a cycle gives dependent columns.*
::::

::: {.solution}
(a) Column \( e \) of \( N \) has \( 1 \) at the tail and \( -1 \) at the head:
\[
N = \begin{pmatrix} 1 & 0 & 0 & -1 & 1 \\ -1 & 1 & 0 & 0 & 0 \\ 0 & -1 & 1 & 0 & -1 \\ 0 & 0 & -1 & 1 & 0 \end{pmatrix}, \qquad
L = NN\tp = \begin{pmatrix} 3 & -1 & -1 & -1 \\ -1 & 2 & -1 & 0 \\ -1 & -1 & 3 & -1 \\ -1 & 0 & -1 & 2 \end{pmatrix}.
\]
(Diagonal entries count the edges at a vertex; off-diagonal entries are \( -1 \) for each edge joining two vertices.) Expanding along the first row,
\[
\det L_0 = \det\begin{pmatrix} 3 & -1 & -1 \\ -1 & 2 & -1 \\ -1 & -1 & 3 \end{pmatrix} = 3(6 - 1) + 1\cdot(-3 - 1) - 1\cdot(1 + 2) = 15 - 4 - 3 = 8 .
\]

(b) There are \( \binom{5}{3} = 10 \) sets of three edges. Three edges on four vertices connect everything exactly when they contain no cycle, and the only \( 3 \)-edge cycles are the triangles \( \{e_1, e_2, e_5\} \) (vertices \( 1, 2, 3 \)) and \( \{e_3, e_4, e_5\} \) (vertices \( 1, 3, 4 \)). So there are \( 10 - 2 = 8 \) spanning trees, matching \( \det L_0 \).

(c) Deleting row \( 4 \) of \( N \) deletes row \( 4 \) of \( NN\tp \) (row view) and column \( 4 \) of \( NN\tp \) (column view of \( N\tp \)), by @thm-three-views-of-product. So \( L_0 = N_0N_0\tp \), with \( N_0 \in M_{3 \times 5}(\nR) \), and @cor-gram-determinant-nonnegative gives \( \det L_0 = \sum_{|S| = 3} (\det (N_0)_{[3],S})^2 \), one term for each set \( S \) of three edges.

(d) For \( S = \{e_1, e_2, e_3\} \), \( (N_0)_{[3],S} = \begin{pmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & -1 & 1 \end{pmatrix} \), which is lower triangular with determinant \( 1 \) (@thm-det-triangular). For \( S = \{e_1, e_2, e_5\} \), the columns are \( (1, -1, 0) \), \( (0, 1, -1) \), \( (1, 0, -1) \), and the third is the sum of the first two: going around the cycle \( 1 \to 2 \to 3 \) equals going directly \( 1 \to 3 \). So the columns are dependent and the minor is \( 0 \) by @thm-alternating-properties. Thus the non-tree contributes \( 0^2 \) and the tree contributes \( 1^2 \). (Sympy confirms that the ten minors are \( \pm 1 \) for the eight trees and \( 0 \) for the two triangles, so the sum is \( 8 \).)
:::

:::: {#exr-minors-and-rank-c2}
[C2: Rank does not depend on the field]

Let \( K \) be a subfield of a field \( L \) (@def-restriction-of-scalars), and let \( A \in M_{m \times n}(K) \). We may also regard \( A \) as a matrix in \( M_{m \times n}(L) \).

::: {.enumerate options="label=(\alph*)"}
1. Explain why each minor \( \det A_{I,J} \) is the same element whether computed in \( K \) or in \( L \).
2. Prove that the rank of \( A \) over \( K \) equals its rank over \( L \).
3. Deduce: if a system \( A\x = \0 \) with rational coefficients has a non-zero complex solution, it has a non-zero rational solution.
:::
::::

::: {.solution}
(a) By @def-determinant, \( \det A_{I,J} \) is a finite sum of \( \pm \) products of entries of \( A \). The entries lie in \( K \), and \( K \) has the same addition and multiplication as \( L \), so the sum is the same element of \( K \subseteq L \).

(b) If \( A = 0 \), both ranks are \( 0 \). Otherwise, by @thm-rank-via-minors (a) applied over \( K \) and over \( L \), each rank is the largest \( k \) for which some \( k \times k \) minor is non-zero. By (a) the list of minors, and which of them are non-zero, is the same in both cases. Hence the two ranks agree.

(c) Take \( K = \nQ \), \( L = \nC \). A non-zero complex solution means \( \nullity A \ge 1 \) over \( \nC \), so \( \rank_{\nC} A \le n - 1 \) by @thm-rank-nullity-matrix. By (b), \( \rank_{\nQ} A \le n - 1 \), so \( \nullity A \ge 1 \) over \( \nQ \), and a non-zero rational solution exists.
:::
