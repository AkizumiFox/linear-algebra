# Cofactor Expansion, the Adjugate and Cramer's Rule

We can now compute determinants by elimination and we know what they decide. This section adds a third view: a determinant of size \( n \) is a combination of determinants of size \( n - 1 \). This recursive formula, the Laplace expansion, is rarely the fastest way to compute, but it has two important consequences. It gives an explicit formula for the inverse of a matrix, through the adjugate, and an explicit formula for the solution of a square linear system, Cramer's rule. Both rest on one identity built from the entries alone, with no division, and that identity holds for matrices of polynomials too, which is what later chapters need.

## Minors and cofactors

Group the six terms of a \( 3 \times 3 \) determinant (from the examples after @def-determinant) by the entry they take from column \( 1 \):
\[
\det \A = a_{11}\,(a_{22}a_{33} - a_{32}a_{23}) - a_{21}\,(a_{12}a_{33} - a_{32}a_{13}) + a_{31}\,(a_{12}a_{23} - a_{22}a_{13}).
\]
Each bracket is a \( 2 \times 2 \) determinant. The bracket beside \( a_{11} \) is the determinant of what remains of \( \A \) after deleting row \( 1 \) and column \( 1 \); the bracket beside \( a_{21} \) is what remains after deleting row \( 2 \) and column \( 1 \); and similarly for \( a_{31} \). The signs alternate. These smaller determinants recur constantly, so they get names.

*A minor is the determinant of what is left after crossing out one row and one column; a cofactor is that minor with a checkerboard sign.*

::: {#def-minor-cofactor}
[Minor and cofactor]

Let \( n \ge 2 \), \( \A \in M_n(F) \) and \( i, j \in \{1, \dots, n\} \). The **\( (i, j) \)-minor** of \( \A \) is
\[
\begin{aligned}
M_{ij} \coloneqq \det(&\text{the } (n-1) \times (n-1) \text{ matrix obtained from } \A \\
&\text{by deleting row } i \text{ and column } j).
\end{aligned}
\]
The **\( (i, j) \)-cofactor** of \( \A \) is \( C_{ij} \coloneqq (-1)^{i+j} M_{ij} \).
:::

The rows and columns that remain keep their original order. The sign \( (-1)^{i+j} \) depends only on the position, and follows a checkerboard starting with \( + \) in the top-left corner:
\[
\begin{pmatrix} + & - & + & \cdots \\ - & + & - & \cdots \\ + & - & + & \cdots \\ \vdots & \vdots & \vdots & \ddots \end{pmatrix}.
\]
When the matrix matters we write \( M_{ij}(\A) \) and \( C_{ij}(\A) \).

**Examples.** For \( \A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \), the minors are \( 1 \times 1 \) determinants: \( M_{11} = d \), \( M_{12} = c \), \( M_{21} = b \), \( M_{22} = a \), and the cofactors are \( C_{11} = d \), \( C_{12} = -c \), \( C_{21} = -b \), \( C_{22} = a \). For the matrix \( \A = \begin{pmatrix} 2 & 1 & 3 \\ 0 & 4 & 1 \\ 5 & 2 & 1 \end{pmatrix} \) of the previous sections, the cofactors along column \( 1 \) are
\[
\begin{aligned}
C_{11} &= +\det \begin{pmatrix} 4 & 1 \\ 2 & 1 \end{pmatrix} = 2, \\
C_{21} &= -\det \begin{pmatrix} 1 & 3 \\ 2 & 1 \end{pmatrix} = 5, \\
C_{31} &= +\det \begin{pmatrix} 1 & 3 \\ 4 & 1 \end{pmatrix} = -11,
\end{aligned}
\]
and \( a_{11}C_{11} + a_{21}C_{21} + a_{31}C_{31} = 4 + 0 - 55 = -51 \), which is \( \det \A \) as computed before. For the identity \( \I_n \), \( C_{ii} = \det \I_{n-1} = 1 \), and \( C_{ij} = 0 \) for \( i \ne j \), because deleting row \( i \) and a different column \( j \) leaves a matrix with a zero column.

**Non-example by minimal change.** A minor and a cofactor differ only by a sign, and forgetting the sign is the commonest slip. For the \( 2 \times 2 \) matrix above, \( M_{12} = c \) but \( C_{12} = -c \); using minors throughout would turn \( a_{11}C_{11} + a_{21}C_{21} = ad - cb \) into \( ad + cb \), which is the permanent, not the determinant.

## The Laplace expansion

The \( 3 \times 3 \) grouping above is a special case of a general identity, valid along **every** row and **every** column.

::: {#thm-laplace-expansion}
[Laplace Expansion]

Let \( n \ge 2 \) and \( \A \in M_n(F) \), with cofactors \( C_{ij} \).

::: {.enumerate options="label=(\alph*)"}
1. **(Along column \( j \))** For each \( j \in \{1, \dots, n\} \),
   \[
   \det \A = a_{1j}C_{1j} + a_{2j}C_{2j} + \dots + a_{nj}C_{nj} = \sum_{i=1}^{n} a_{ij}C_{ij} .
   \]
2. **(Along row \( i \))** For each \( i \in \{1, \dots, n\} \),
   \[
   \det \A = a_{i1}C_{i1} + a_{i2}C_{i2} + \dots + a_{in}C_{in} = \sum_{j=1}^{n} a_{ij}C_{ij} .
   \]
:::
:::

::: {.idea}
The plan for (a):

① Write column \( j \) as \( \sum_i a_{ij}\e_i \) and use linearity in column \( j \). This leaves \( n \) determinants, the \( i \)-th with column \( j \) replaced by \( \e_i \).

② In such a determinant, move the lone \( 1 \) to the top-left corner. To keep the other rows and columns in their original order, use **adjacent** swaps: \( j - 1 \) column swaps and \( i - 1 \) row swaps, costing \( (-1)^{(i-1)+(j-1)} = (-1)^{i+j} \).

③ A matrix whose first column is \( \e_1 \) has the same determinant as its lower-right \( (n-1) \times (n-1) \) block: only permutations fixing \( 1 \) contribute to the Leibniz formula. After ②, that block is exactly the matrix defining \( M_{ij} \).

Part (b) is part (a) for the transpose.
:::

::: {.proof}
(a) Fix \( j \). For \( i \in \{1, \dots, n\} \), let \( \B^{(i)} \) be the matrix obtained from \( \A \) by replacing column \( j \) with \( \e_i \).

::: {.claim}
\( \det \B^{(i)} = C_{ij} \).

::: {.proof}
Write \( \B = \B^{(i)} \), with columns \( \b_1, \dots, \b_n \), so \( \b_j = \e_i \) and \( \b_k \) is the \( k \)-th column of \( \A \) for \( k \ne j \).

*Moving the column.* Swap columns \( j - 1 \) and \( j \), then columns \( j - 2 \) and \( j - 1 \), and so on, ending with columns \( 1 \) and \( 2 \). After these \( j - 1 \) adjacent swaps the columns are \( \b_j, \b_1, \dots, \b_{j-1}, \b_{j+1}, \dots, \b_n \): the column \( \b_j \) is first and the others are in their original order. Call this matrix \( \B_1 \). By @thm-det-row-operations (d), each swap multiplies the determinant by \( -1 \), so \( \det \B_1 = (-1)^{j-1} \det \B \).

*Moving the row.* In the same way, move row \( i \) of \( \B_1 \) to the top by \( i - 1 \) adjacent row swaps, keeping the other rows in their original order. Call the result \( \B_2 \). By @thm-det-row-operations (a), \( \det \B_2 = (-1)^{i-1} \det \B_1 \).

*The shape of \( \B_2 \).* The first column of \( \B_1 \) is \( \e_i \), and moving row \( i \) to the top turns it into \( \e_1 \). For \( p, q \ge 2 \), the \( (p, q) \)-entry of \( \B_2 \) comes from the rows of \( \A \) other than \( i \) and the columns of \( \A \) other than \( j \), both in their original order. So the lower-right \( (n-1) \times (n-1) \) block of \( \B_2 \) is the matrix \( \A' \) obtained from \( \A \) by deleting row \( i \) and column \( j \). Writing \( b'_{pq} \) for the entries of \( \B_2 \), we have \( b'_{11} = 1 \), \( b'_{p1} = 0 \) for \( p \ge 2 \), and \( b'_{pq} = a'_{p-1, q-1} \) for \( p, q \ge 2 \).

*The block determinant.* In the Leibniz formula for \( \det \B_2 \), the factor \( b'_{\sigma(1)1} \) is \( 0 \) unless \( \sigma(1) = 1 \). Let \( G = \{\sigma \in S_n : \sigma(1) = 1\} \). For \( \sigma \in G \), define \( \rho \in S_{n-1} \) by \( \rho(k) = \sigma(k+1) - 1 \); this is a bijection of \( \{1, \dots, n-1\} \), because \( \sigma \) maps \( \{2, \dots, n\} \) bijectively onto itself. The map \( \sigma \mapsto \rho \) is a bijection \( G \to S_{n-1} \), with inverse \( \rho \mapsto \sigma \), \( \sigma(1) = 1 \), \( \sigma(k+1) = \rho(k) + 1 \). An inversion of \( \sigma \) (@def-inversion) is a pair \( p < q \) with \( \sigma(p) > \sigma(q) \); it never has \( p = 1 \), since \( \sigma(1) = 1 \) is smallest, and for \( p, q \ge 2 \) it is exactly an inversion \( (p - 1, q - 1) \) of \( \rho \). So \( \sgn(\sigma) = \sgn(\rho) \) by @def-sign-permutation. Therefore
\[
\det \B_2 = \sum_{\sigma \in G} \sgn(\sigma) \cdot 1 \cdot \prod_{q=2}^{n} b'_{\sigma(q)q} = \sum_{\rho \in S_{n-1}} \sgn(\rho) \prod_{k=1}^{n-1} a'_{\rho(k)k} = \det \A' = M_{ij} .
\]

Combining, \( \det \B = (-1)^{j-1}(-1)^{i-1} \det \B_2 = (-1)^{i+j} M_{ij} = C_{ij} \).
:::
:::

Now the \( j \)-th column of \( \A \) is \( \sum_{i=1}^{n} a_{ij}\e_i \), and the other columns of \( \A \) and of each \( \B^{(i)} \) agree. By linearity of \( \det \) in column \( j \) (@thm-leibniz-formula-alternating) and the claim,
\[
\det \A = \sum_{i=1}^{n} a_{ij} \det \B^{(i)} = \sum_{i=1}^{n} a_{ij} C_{ij} .
\]

(b) Fix \( i \). The \( (k, i) \)-entry of \( \A\tp \) is \( a_{ik} \). Deleting row \( k \) and column \( i \) from \( \A\tp \) gives the transpose of the matrix obtained from \( \A \) by deleting row \( i \) and column \( k \), so \( M_{ki}(\A\tp) = M_{ik}(\A) \) by @thm-det-transpose, and hence \( C_{ki}(\A\tp) = C_{ik}(\A) \). Applying (a) to \( \A\tp \) along column \( i \), and @thm-det-transpose again,
\[
\det \A = \det \A\tp = \sum_{k=1}^{n} a_{ik}\, C_{ki}(\A\tp) = \sum_{k=1}^{n} a_{ik}\, C_{ik}(\A).
\]
This proves the theorem.
:::

::: {.check}
In step ② of the Idea, why not move column \( j \) to the front with the single swap of columns \( 1 \) and \( j \)?
:::

::: {.solution}
A single swap costs only one factor \( -1 \), but it puts the old first column in position \( j \), so the lower-right block is no longer the matrix defining \( M_{ij} \): its columns are out of order. For \( j \ge 3 \), putting that column back in place within the block takes \( j - 2 \) further adjacent swaps, and the total sign is again \( (-1)^{1 + (j-2)} = (-1)^{j-1} \). Adjacent swaps keep the count honest from the start.
:::

::: {.remark}
**Over a commutative ring.** The proof uses multilinearity and the swap rule for columns and rows, the Leibniz formula, and @thm-det-transpose. All of these are division-free (see the remarks at the ends of the previous two sections). So the Laplace expansion holds for matrices with entries in any commutative ring \( R \), for instance \( F[x] \).
:::

The expansion is most useful along a row or column with many zeros, since each zero entry kills its term without computing the minor.

::: {#exm-laplace-4x4}
[A \( 4 \times 4 \) Expansion]

Compute \( \det \A \) for
\[
\A = \begin{pmatrix} 3 & 1 & 0 & 2 \\ 1 & 0 & 2 & 0 \\ 2 & 4 & 1 & 3 \\ 0 & 1 & 5 & 2 \end{pmatrix} \in M_4(\nR)
\]
by expanding along a suitable row.
:::

::: {.solution}
Row \( 2 \) has two zeros. Its signs in the checkerboard are \( -, +, -, + \). By @thm-laplace-expansion (b) along row \( 2 \),
\[
\det \A = 1 \cdot C_{21} + 0 \cdot C_{22} + 2 \cdot C_{23} + 0 \cdot C_{24} = -M_{21} - 2M_{23} .
\]
Deleting row \( 2 \) and column \( 1 \), and then row \( 2 \) and column \( 3 \),
\[
M_{21} = \det \begin{pmatrix} 1 & 0 & 2 \\ 4 & 1 & 3 \\ 1 & 5 & 2 \end{pmatrix}, \qquad M_{23} = \det \begin{pmatrix} 3 & 1 & 2 \\ 2 & 4 & 3 \\ 0 & 1 & 2 \end{pmatrix}.
\]
Expand \( M_{21} \) along its first row, which has a zero:
\[
M_{21} = 1 \cdot \det \begin{pmatrix} 1 & 3 \\ 5 & 2 \end{pmatrix} - 0 + 2 \cdot \det \begin{pmatrix} 4 & 1 \\ 1 & 5 \end{pmatrix} = (2 - 15) + 2(20 - 1) = 25 .
\]
Expand \( M_{23} \) along its third row \( (0, 1, 2) \), with signs \( +, -, + \):
\[
M_{23} = -1 \cdot \det \begin{pmatrix} 3 & 2 \\ 2 & 3 \end{pmatrix} + 2 \cdot \det \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix} = -(9 - 4) + 2(12 - 2) = 15 .
\]
Hence \( \det \A = -25 - 2 \cdot 15 = -55 \).
:::

::: {.warning}
**The sign belongs to the position, not to the place in the row.** Along row \( 2 \) the signs start with \( - \). Using the first-row pattern \( +, -, +, - \) in the example above would give \( 1 \cdot 25 + 2 \cdot 15 = 55 \), the wrong sign. Always read the sign as \( (-1)^{i+j} \).
:::

Expansion alone is slow: expanding fully down to \( 1 \times 1 \) determinants reproduces all \( n! \) Leibniz terms. In practice one first creates zeros with replacements, which do not change the determinant, and then expands along the line of zeros.

## The adjugate

In Chapter 0 we inverted a \( 2 \times 2 \) matrix by multiplying it by \( \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} \) (@thm-two-by-two-inverse). Compare with the cofactors listed after @def-minor-cofactor: \( C_{11} = d \), \( C_{12} = -c \), \( C_{21} = -b \), \( C_{22} = a \). The matrix of Chapter 0 is the matrix of cofactors, **transposed**. That recurring matrix deserves a name in every size.

*The adjugate is the transposed matrix of cofactors.*

::: {#def-adjugate}
[Adjugate]

Let \( n \ge 2 \) and \( \A \in M_n(F) \). The **adjugate** of \( \A \) is the matrix \( \adj \A \in M_n(F) \) with entries
\[
(\adj \A)_{ij} \coloneqq C_{ji} ,
\]
that is, the **transpose** of the matrix \( (C_{ij}) \) of cofactors. For \( n = 1 \) we set \( \adj \A \coloneqq (1) \).
:::

In words: the entry in row \( i \), column \( j \) of \( \adj \A \) is the cofactor from row \( j \), column \( i \) of \( \A \). The adjugate is defined for **every** square matrix, invertible or not.

**Examples.** For \( n = 2 \), \( \adj \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} \). For \( \I_n \), the cofactors computed above give \( \adj \I_n = \I_n \). For
\[
\B = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 3 \end{pmatrix},
\]
the nine cofactors, row by row, are \( C_{11} = 3 \), \( C_{12} = 1 \), \( C_{13} = -1 \); \( C_{21} = -6 \), \( C_{22} = 3 \), \( C_{23} = 2 \); \( C_{31} = 2 \), \( C_{32} = -1 \), \( C_{33} = 1 \). Transposing,
\[
\adj \B = \begin{pmatrix} 3 & -6 & 2 \\ 1 & 3 & -1 \\ -1 & 2 & 1 \end{pmatrix}, \qquad \B \adj \B = \begin{pmatrix} 5 & 0 & 0 \\ 0 & 5 & 0 \\ 0 & 0 & 5 \end{pmatrix},
\]
and \( \det \B = 1 \cdot 3 + 2 \cdot 1 + 0 \cdot (-1) = 5 \), by expansion along row \( 1 \).

**Non-example by minimal change.** Skip the transpose. The cofactor matrix \( \begin{pmatrix} 3 & 1 & -1 \\ -6 & 3 & 2 \\ 2 & -1 & 1 \end{pmatrix} \) has the same entries in other places, and \( \B \) times it is \( \begin{pmatrix} -9 & 7 & 3 \\ -4 & 2 & 3 \\ 9 & -2 & 2 \end{pmatrix} \), which is not a multiple of \( \I_3 \). The transpose is what lines up row \( i \) of \( \B \) with the cofactors **of row \( i \)**.

The product \( \B \adj \B = (\det \B) \I_3 \) is no accident. Its diagonal entries are row expansions of \( \det \B \). Its off-diagonal entries are expansions too, of a matrix that looks like \( \B \) but has a repeated row.

::: {#thm-adjugate-identity}
[The Adjugate Identity]

For every \( \A \in M_n(F) \),
\[
\A \adj \A = \adj \A \, \A = (\det \A)\, \I_n .
\]
:::

::: {.idea}
The \( (i, k) \)-entry of \( \A \adj \A \) is \( \sum_j a_{ij} C_{kj} \): the entries of row \( i \) against the cofactors of row \( k \). If \( i = k \), this is the expansion of \( \det \A \) along row \( i \). If \( i \ne k \), build a look-alike matrix \( \tilde \A \): copy \( \A \), but overwrite row \( k \) with row \( i \). The cofactors along row \( k \) never see row \( k \), because computing them deletes it, so \( \tilde \A \) has the same cofactors along row \( k \) as \( \A \). Expanding \( \det \tilde \A \) along row \( k \) gives exactly \( \sum_j a_{ij} C_{kj} \), and \( \det \tilde \A = 0 \) because two rows are equal.
:::

::: {.proof}
For \( n = 1 \), \( \A = (a) \), \( \adj \A = (1) \), and both products are \( (a) = (\det \A) \I_1 \). Let \( n \ge 2 \).

*The product \( \A \adj \A \).* By @thm-three-views-of-product and @def-adjugate, its \( (i, k) \)-entry is
\[
\sum_{j=1}^{n} a_{ij}\, (\adj \A)_{jk} = \sum_{j=1}^{n} a_{ij}\, C_{kj} .
\]
If \( i = k \), this is \( \det \A \) by @thm-laplace-expansion (b) along row \( i \). Suppose \( i \ne k \), and let \( \tilde \A \) be the matrix obtained from \( \A \) by replacing row \( k \) with a copy of row \( i \). Rows \( i \) and \( k \) of \( \tilde \A \) are equal, so \( \det \tilde \A = 0 \) by @thm-det-transpose. Expanding along row \( k \) by @thm-laplace-expansion (b),
\[
0 = \det \tilde \A = \sum_{j=1}^{n} \tilde a_{kj}\, C_{kj}(\tilde \A) .
\]
Here \( \tilde a_{kj} = a_{ij} \). The minor \( M_{kj}(\tilde \A) \) is computed from \( \tilde \A \) with row \( k \) deleted, and outside row \( k \) the matrices \( \tilde \A \) and \( \A \) agree; so \( C_{kj}(\tilde \A) = C_{kj}(\A) \). Hence \( \sum_j a_{ij} C_{kj} = 0 \). Therefore \( \A \adj \A = (\det \A) \I_n \).

*The product \( \adj \A \, \A \).* Its \( (i, k) \)-entry is \( \sum_{j} C_{ji}\, a_{jk} \). If \( i = k \), this is \( \det \A \) by @thm-laplace-expansion (a) along column \( i \). If \( i \ne k \), let \( \hat \A \) be \( \A \) with column \( i \) replaced by a copy of column \( k \). It has two equal columns, so \( \det \hat \A = 0 \) by @thm-leibniz-formula-alternating. Expanding along column \( i \), \( 0 = \sum_j \hat a_{ji}\, C_{ji}(\hat \A) = \sum_j a_{jk}\, C_{ji}(\A) \), since deleting column \( i \) removes the only column where \( \hat \A \) and \( \A \) differ. Therefore \( \adj \A \, \A = (\det \A) \I_n \). This proves the theorem.
:::

::: {.remark}
**Over a commutative ring.** This proof uses only @thm-laplace-expansion and the alternating property, so the adjugate identity holds for \( \A \in M_n(R) \) over any commutative ring \( R \). For \( R = F[x] \), the matrix \( \adj(x\I - \A) \) has polynomial entries and \( (x\I - \A) \adj(x\I - \A) = \det(x\I - \A)\, \I \). This identity reappears in Chapter 9. Over \( R \) the identity also shows that \( \A \) has an inverse in \( M_n(R) \) as soon as \( \det \A \) has an inverse in \( R \), namely \( (\det \A)^{-1} \adj \A \).
:::

Dividing by the determinant, when we may, gives the inverse.

::: {#cor-inverse-formula}
[Inverse via the Adjugate]

Let \( \A \in M_n(F) \) with \( \det \A \ne 0 \). Then \( \A \) is invertible and
\[
\A^{-1} = \frac{1}{\det \A} \adj \A .
\]
:::

::: {.proof}
By @thm-adjugate-identity, \( \A \big( (\det \A)^{-1} \adj \A \big) = (\det \A)^{-1} (\det \A) \I_n = \I_n \), using that scalars commute with matrices (@thm-matrix-multiplication-properties). By @thm-one-sided-inverse, \( \A \) is invertible with inverse \( (\det \A)^{-1} \adj \A \).
:::

For \( n = 2 \) this is @thm-two-by-two-inverse again. For the matrix \( \B \) above, \( \B^{-1} = \frac15 \begin{pmatrix} 3 & -6 & 2 \\ 1 & 3 & -1 \\ -1 & 2 & 1 \end{pmatrix} \).

::: {.warning}
**The adjugate exists for singular matrices too.** Nothing in @def-adjugate needs \( \det \A \ne 0 \). For \( S = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 1 & 0 & 1 \end{pmatrix} \), with \( \det S = 0 \), one computes \( \adj S = \begin{pmatrix} 4 & -2 & 0 \\ 4 & -2 & 0 \\ -4 & 2 & 0 \end{pmatrix} \ne 0 \), and \( S \adj S = 0 \), as @thm-adjugate-identity predicts. So "\( \adj \A \) exists" says nothing about invertibility, and the formula \( \A^{-1} = \adj \A / \det \A \) must never be used before checking \( \det \A \ne 0 \).
:::

::: {.check}
What are \( \adj(c\I_n) \) for \( c \in F \) and \( n \ge 2 \), and \( \adj 0 \) for the zero matrix in \( M_n(F) \), \( n \ge 2 \)? What is \( \adj 0 \) for \( n = 1 \)?
:::

::: {.solution}
Deleting row \( i \) and column \( i \) from \( c\I_n \) leaves \( c\I_{n-1} \), of determinant \( c^{n-1} \); deleting row \( i \) and a different column leaves a zero column, of determinant \( 0 \). So \( \adj(c\I_n) = c^{n-1} \I_n \); in particular \( \adj 0 = 0 \) for \( n \ge 2 \), since \( 0^{n-1} = 0 \). For \( n = 1 \), \( \adj(0) = (1) \) by definition, and indeed \( (0)(1) = (0) = (\det 0) \I_1 \).
:::

## Cramer's rule

For an invertible \( \A \), the system \( \A\x = \b \) has exactly one solution. The adjugate expresses it in closed form, and the closed form has a direct proof by linearity that shows where it comes from. For \( k \in \{1, \dots, n\} \), write \( \A_k(\b) \) for the matrix obtained from \( \A \) by replacing column \( k \) with \( \b \).

::: {#thm-cramers-rule}
[Cramer's Rule]

Let \( \A \in M_n(F) \) be invertible and \( \b \in F^n \). The unique solution \( \x \) of \( \A\x = \b \) is given by
\[
x_k = \frac{\det \A_k(\b)}{\det \A}, \qquad k = 1, \dots, n .
\]
:::

::: {.idea}
If \( \A\x = \b \), then \( \b = x_1\a_1 + \dots + x_n\a_n \). Put this combination into column \( k \) and expand by linearity. Every term except the \( k \)-th has the column \( \a_j \) twice, so it vanishes, and what remains is \( x_k \det \A \).
:::

::: {.proof}
By @thm-inverse-matrix-properties (7), \( \A\x = \b \) has exactly one solution \( \x \). By @thm-matrix-times-vector-columns, \( \b = \sum_{j=1}^{n} x_j \a_j \), where \( \a_j \) is the \( j \)-th column of \( \A \). Since \( \det \) is linear in column \( k \) (@thm-leibniz-formula-alternating),
\[
\det \A_k(\b) = \sum_{j=1}^{n} x_j \det \A_k(\a_j) .
\]
For \( j \ne k \), the matrix \( \A_k(\a_j) \) has the column \( \a_j \) in positions \( j \) and \( k \), so its determinant is \( 0 \). For \( j = k \), \( \A_k(\a_k) = \A \). Hence \( \det \A_k(\b) = x_k \det \A \). Since \( \A \) is invertible, \( \det \A \ne 0 \) by @thm-det-nonzero-iff-invertible, and dividing gives the formula.
:::

Alternatively, \( \x = \A^{-1}\b = (\det \A)^{-1} \adj \A\, \b \) by @cor-inverse-formula, and the \( k \)-th entry of \( \adj \A\, \b \) is \( \sum_j C_{jk} b_j \), which is the expansion of \( \det \A_k(\b) \) along column \( k \) (@thm-laplace-expansion (a)); the cofactors along column \( k \) of \( \A_k(\b) \) and of \( \A \) agree, because computing them deletes column \( k \).

For example, the system \( 2x + y = 5 \), \( 7x + 4y = 18 \) has coefficient matrix of determinant \( 8 - 7 = 1 \), so
\[
x = \det \begin{pmatrix} 5 & 1 \\ 18 & 4 \end{pmatrix} = 2, \qquad y = \det \begin{pmatrix} 2 & 5 \\ 7 & 18 \end{pmatrix} = 1,
\]
and indeed \( 2 \cdot 2 + 1 = 5 \) and \( 7 \cdot 2 + 4 = 18 \).

::: {.warning}
**Cramer's rule is a theoretical tool, not an algorithm.** It needs \( n + 1 \) determinants of size \( n \). Evaluated by the Leibniz formula this is about \( (n+1)! \) products; even with each determinant computed by elimination it costs about \( n^4/3 \) operations, while Gaussian elimination solves the system once in about \( n^3/3 \). For \( n = 20 \), term-by-term Leibniz evaluation at \( 10^9 \) multiplications per second would take tens of thousands of years. Use Cramer's rule to understand **how** the solution depends on \( \A \) and \( \b \), and elimination to find it.
:::

## Integer matrices

The adjugate formula shows that each entry of \( \A^{-1} \) is a polynomial in the entries of \( \A \) divided by the single polynomial \( \det \A \). In particular, the entries of \( \A^{-1} \) change continuously with those of \( \A \) over \( \nR \), as long as \( \det \A \ne 0 \). Here is an arithmetic consequence. A matrix with integer entries lies in \( M_n(\nQ) \), and we may ask when its inverse again has integer entries.

::: {#cor-integer-inverse}
[Integer Matrices with Integer Inverses]

Let \( \A \in M_n(\nQ) \) have all entries in \( \nZ \).

::: {.enumerate options="label=(\alph*)"}
1. \( \det \A \in \nZ \), and \( \adj \A \) has all entries in \( \nZ \).
2. \( \A \) is invertible and \( \A^{-1} \) has all entries in \( \nZ \) if and only if \( \det \A = 1 \) or \( \det \A = -1 \).
:::
:::

::: {.proof}
(a) The Leibniz formula (@def-determinant) is a sum of products of entries with signs \( \pm 1 \), so the determinant of a matrix with integer entries is an integer. Each cofactor is \( \pm \) such a determinant, so \( \adj \A \) has integer entries (for \( n = 1 \), \( \adj \A = (1) \)).

(b) \( (\Leftarrow) \) If \( \det \A = \pm 1 \), then \( \A \) is invertible and \( \A^{-1} = \pm \adj \A \) by @cor-inverse-formula, which has integer entries by (a). \( (\Rightarrow) \) Suppose \( \A^{-1} \) has integer entries. By @thm-det-multiplicative, \( \det \A \det(\A^{-1}) = \det \I_n = 1 \), and both factors are integers by (a). The only integers whose product is \( 1 \) are \( 1 \cdot 1 \) and \( (-1)(-1) \), so \( \det \A = \pm 1 \).
:::

For example, \( \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix} \) has determinant \( 1 \) and inverse \( \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix} \), while \( \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix} \) has determinant \( 2 \) and inverse \( \begin{pmatrix} 1/2 & -1/2 \\ 0 & 1 \end{pmatrix} \). In the language of the remark after @thm-adjugate-identity, part (b) says that a matrix over the ring \( \nZ \) is invertible over \( \nZ \) exactly when its determinant is invertible in \( \nZ \).

## Exercises

### A. Check your understanding

::: {#exr-cofactor-expansion-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the \( (i, j) \)-minor, the \( (i, j) \)-cofactor and the adjugate of \( \A \in M_n(F) \), \( n \ge 2 \).
2. What are the signs \( (-1)^{i+j} \) of the cofactors in positions \( (2, 3) \) and \( (4, 4) \)?
3. True or false: \( \adj \A \) is defined only when \( \A \) is invertible. Justify your answer.
4. True or false: Cramer's rule (@thm-cramers-rule) gives the solutions of every square linear system \( \A\x = \b \). Justify your answer.
5. In the proof of @thm-adjugate-identity, which matrix is expanded to show that \( \sum_j a_{ij}C_{kj} = 0 \) for \( i \ne k \), and why is its determinant \( 0 \)?
6. True or false: if \( \A \) has integer entries and \( \det \A = 2 \), then \( \A^{-1} \) has integer entries. Justify your answer.
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. \( M_{ij} \) is the determinant of the \( (n-1) \times (n-1) \) matrix obtained by deleting row \( i \) and column \( j \); \( C_{ij} = (-1)^{i+j}M_{ij} \); \( \adj \A \) is the matrix with \( (i, j) \)-entry \( C_{ji} \) (@def-minor-cofactor, @def-adjugate).
2. \( (-1)^{5} = -1 \) and \( (-1)^{8} = 1 \).
3. False. It is defined for every square matrix; for instance \( \adj \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix} \), although the matrix is singular.
4. False. It requires \( \det \A \ne 0 \). For \( \A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \) and \( \b = (1, 1) \), the system has infinitely many solutions, and the formula would divide by \( 0 \).
5. The matrix \( \tilde \A \) obtained from \( \A \) by replacing row \( k \) with row \( i \), expanded along row \( k \). It has two equal rows, \( i \) and \( k \), so its determinant is \( 0 \).
6. False. By @cor-integer-inverse, an integer inverse forces \( \det \A = \pm 1 \). For instance \( \diag(2, 1) \) has inverse \( \diag(\frac12, 1) \).
:::
:::

### B. Practice

::: {#exr-cofactor-expansion-b1}
[B1: Adjugate and inverse]

Let \( \A = \begin{pmatrix} 1 & 2 & -1 \\ 0 & 1 & 3 \\ 2 & 1 & 1 \end{pmatrix} \in M_3(\nR) \). Compute all nine cofactors, \( \adj \A \) and \( \det \A \). Verify that \( \A \adj \A = (\det \A) \I_3 \), and hence write down \( \A^{-1} \).
:::

::: {.solution}
The cofactors are
\[
\begin{aligned}
C_{11} &= +(1 \cdot 1 - 3 \cdot 1) = -2, & C_{12} &= -(0 \cdot 1 - 3 \cdot 2) = 6, \\
C_{13} &= +(0 \cdot 1 - 1 \cdot 2) = -2, & C_{21} &= -(2 \cdot 1 - (-1) \cdot 1) = -3, \\
C_{22} &= +(1 \cdot 1 - (-1) \cdot 2) = 3, & C_{23} &= -(1 \cdot 1 - 2 \cdot 2) = 3, \\
C_{31} &= +(2 \cdot 3 - (-1) \cdot 1) = 7, & C_{32} &= -(1 \cdot 3 - (-1) \cdot 0) = -3, \\
C_{33} &= +(1 \cdot 1 - 2 \cdot 0) = 1 .
\end{aligned}
\]
Transposing the cofactor matrix (@def-adjugate),
\[
\adj \A = \begin{pmatrix} -2 & -3 & 7 \\ 6 & 3 & -3 \\ -2 & 3 & 1 \end{pmatrix}.
\]
Expanding along row \( 1 \) (@thm-laplace-expansion), \( \det \A = 1 \cdot (-2) + 2 \cdot 6 + (-1)(-2) = 12 \). Row \( 1 \) of \( \A \) against the columns of \( \adj \A \) gives \( -2 + 12 + 2 = 12 \), \( -3 + 6 - 3 = 0 \), \( 7 - 6 - 1 = 0 \); row \( 2 \) gives \( 0 + 6 - 6 = 0 \), \( 0 + 3 + 9 = 12 \), \( 0 - 3 + 3 = 0 \); row \( 3 \) gives \( -4 + 6 - 2 = 0 \), \( -6 + 3 + 3 = 0 \), \( 14 - 3 + 1 = 12 \). So \( \A \adj \A = 12 \I_3 \). By @cor-inverse-formula,
\[
\A^{-1} = \frac{1}{12} \begin{pmatrix} -2 & -3 & 7 \\ 6 & 3 & -3 \\ -2 & 3 & 1 \end{pmatrix}.
\]
:::

::: {#exr-cofactor-expansion-b2}
[B2: Cramer's rule]

Use Cramer's rule to solve
\[
x_1 + 2x_2 - x_3 = -3, \qquad x_2 + 3x_3 = 5, \qquad 2x_1 + x_2 + x_3 = 3
\]
over \( \nR \). Check your answer by substitution.
:::

::: {.solution}
The coefficient matrix is the matrix \( \A \) of @exr-cofactor-expansion-b1, with \( \det \A = 12 \ne 0 \), and \( \b = (-3, 5, 3) \). Expanding each \( \A_k(\b) \) along its first row,
\[
\begin{aligned}
\det \A_1(\b) &= \det \begin{pmatrix} -3 & 2 & -1 \\ 5 & 1 & 3 \\ 3 & 1 & 1 \end{pmatrix} \\
&= -3(1 - 3) - 2(5 - 9) - 1(5 - 3) = 6 + 8 - 2 = 12, \\
\det \A_2(\b) &= \det \begin{pmatrix} 1 & -3 & -1 \\ 0 & 5 & 3 \\ 2 & 3 & 1 \end{pmatrix} \\
&= 1(5 - 9) + 3(0 - 6) - 1(0 - 10) = -4 - 18 + 10 = -12, \\
\det \A_3(\b) &= \det \begin{pmatrix} 1 & 2 & -3 \\ 0 & 1 & 5 \\ 2 & 1 & 3 \end{pmatrix} \\
&= 1(3 - 5) - 2(0 - 10) - 3(0 - 2) = -2 + 20 + 6 = 24 .
\end{aligned}
\]
By @thm-cramers-rule, \( x_1 = 12/12 = 1 \), \( x_2 = -12/12 = -1 \), \( x_3 = 24/12 = 2 \). Check: \( 1 - 2 - 2 = -3 \), \( -1 + 6 = 5 \), \( 2 - 1 + 2 = 3 \).
:::

::: {#exr-cofactor-expansion-b3}
[B3: Choosing the best line]

Compute \( \det \N \) for
\[
\N = \begin{pmatrix} 2 & 0 & 0 & 3 \\ 1 & 4 & 0 & -1 \\ 0 & 5 & 0 & 2 \\ 3 & 1 & 2 & 0 \end{pmatrix} \in M_4(\nR),
\]
expanding along the row or column that needs the least work.
:::

::: {.solution}
Column \( 3 \) has a single non-zero entry, \( a_{43} = 2 \), whose sign is \( (-1)^{4+3} = -1 \). By @thm-laplace-expansion (a) along column \( 3 \), \( \det \N = -2 M_{43} \), where
\[
\begin{aligned}
M_{43} &= \det \begin{pmatrix} 2 & 0 & 3 \\ 1 & 4 & -1 \\ 0 & 5 & 2 \end{pmatrix} \\
&= 2\big(4 \cdot 2 - (-1) \cdot 5\big) - 0 + 3\big(1 \cdot 5 - 4 \cdot 0\big) = 26 + 15 = 41,
\end{aligned}
\]
expanding along the first row. Hence \( \det \N = -82 \).
:::

### C. Going deeper

::: {#exr-cofactor-expansion-c1}
[C1: The determinant of the adjugate]

Let \( n \ge 2 \) and \( \A \in M_n(F) \). Prove that \( \det(\adj \A) = (\det \A)^{n-1} \).

*Hint: treat \( \det \A \ne 0 \) and \( \det \A = 0 \) separately; in the second case, ask whether \( \adj \A \) can be invertible.*
:::

::: {.solution}
*Case 1: \( \det \A \ne 0 \).* By @thm-adjugate-identity and @thm-det-multiplicative, \( \det \A \det(\adj \A) = \det\big((\det \A) \I_n\big) = (\det \A)^n \), where the last step is @thm-det-triangular. Dividing by \( \det \A \ne 0 \) gives \( \det(\adj \A) = (\det \A)^{n-1} \).

*Case 2: \( \det \A = 0 \).* Then \( \A \adj \A = 0 \) by @thm-adjugate-identity. Suppose, for a contradiction, that \( \adj \A \) is invertible. Then \( \A = (\A \adj \A)(\adj \A)^{-1} = 0 \). But every minor of the zero matrix is the determinant of a zero matrix of size \( n - 1 \ge 1 \), which is \( 0 \), so \( \adj 0 = 0 \), which is not invertible. This contradiction shows that \( \adj \A \) is not invertible, so \( \det(\adj \A) = 0 = (\det \A)^{n-1} \) by @thm-det-nonzero-iff-invertible, since \( n - 1 \ge 1 \).
:::

::: {#exr-cofactor-expansion-c2}
[C2: The rank of the adjugate]

Let \( n \ge 2 \) and \( \A \in M_n(F) \). Prove that
\[
\rank(\adj \A) = \begin{cases} n & \text{if } \rank \A = n, \\ 1 & \text{if } \rank \A = n - 1, \\ 0 & \text{if } \rank \A \le n - 2. \end{cases}
\]

::: {.enumerate options="label=(\alph*)"}
1. Prove the case \( \rank \A = n \).
2. Suppose \( \rank \A \le n - 2 \). Prove that every minor \( M_{ij} \) is \( 0 \).
3. Suppose \( \rank \A = n - 1 \). Prove that every column of \( \adj \A \) lies in \( \nul(\A) \), and deduce \( \rank(\adj \A) \le 1 \).
4. Suppose \( \rank \A = n - 1 \). Prove that some minor \( M_{ij} \) is non-zero, and conclude.
:::

*Hint for (d): choose \( n - 1 \) independent columns of \( \A \), then \( n - 1 \) independent rows of the resulting \( n \times (n-1) \) matrix.*
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. If \( \rank \A = n \), then \( \A \) is invertible by @thm-invertible-tfae-det, so \( \det \A \ne 0 \) and \( \adj \A = (\det \A) \A^{-1} \) by @cor-inverse-formula. This is invertible, since \( \A^{-1} \) is and \( \det \A \ne 0 \) (@thm-inverse-matrix-properties), so \( \rank(\adj \A) = n \).
2. Fix \( i, j \), and let \( \A' \) be \( \A \) with row \( i \) and column \( j \) deleted. The \( n - 1 \) columns of \( \A \) other than column \( j \) lie in \( \col(\A) \), of dimension \( \rank \A \le n - 2 \), so they are linearly dependent by @thm-size-bounds: \( \sum_{k \ne j} c_k \a_k = \0 \) with the \( c_k \) not all zero. Deleting the \( i \)-th entry of every vector preserves this relation, so the columns of \( \A' \) are dependent. By @thm-invertible-tfae, \( \A' \) is not invertible, and \( M_{ij} = \det \A' = 0 \) by @thm-det-nonzero-iff-invertible. Hence \( \adj \A = 0 \) and \( \rank(\adj \A) = 0 \).
3. Since \( \rank \A < n \), \( \det \A = 0 \) by @thm-invertible-tfae-det, so \( \A \adj \A = 0 \) by @thm-adjugate-identity. By @thm-three-views-of-product, \( \A \) kills each column of \( \adj \A \), so \( \col(\adj \A) \subseteq \nul(\A) \). By @thm-rank-nullity-matrix, \( \dim \nul(\A) = n - (n - 1) = 1 \). Hence \( \rank(\adj \A) \le 1 \).
4. By @thm-basis-column-space, the pivot columns of \( \A \) form a basis of \( \col(\A) \); there are \( n - 1 \) of them, so exactly one column index \( j \) is not a pivot column. Let \( \A_0 \in M_{n \times (n-1)}(F) \) consist of the other \( n - 1 \) columns. They are independent, so \( \rank \A_0 = n - 1 \), and \( \dim \row(\A_0) = n - 1 \) by @thm-row-rank-equals-column-rank. The \( n \) rows of \( \A_0 \) span \( \row(\A_0) \), so by @thm-sift some \( n - 1 \) of them are independent; since \( n - 1 \) independent vectors in a space of dimension \( n - 1 \) form a basis, sifting leaves out exactly one row, say row \( i \). Deleting row \( i \) from \( \A_0 \) gives an \( (n-1) \times (n-1) \) matrix \( \A' \) with independent rows, so \( \det \A' \ne 0 \) by @thm-invertible-tfae-det. But \( \A' \) is \( \A \) with row \( i \) and column \( j \) deleted, so \( M_{ij} \ne 0 \), hence \( C_{ij} \ne 0 \) and \( \adj \A \ne 0 \). With (c), \( \rank(\adj \A) = 1 \).
:::
:::

::: {#exr-cofactor-expansion-c3}
[C3: An adjugate over \( F[x] \)]

Work in \( M_2(\nR[x]) \), using the remarks after @thm-laplace-expansion and @thm-adjugate-identity.

::: {.enumerate options="label=(\alph*)"}
1. For \( \A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \), compute \( \det(x\I - \A) \) and \( \adj(x\I - \A) \), and verify \( (x\I - \A)\adj(x\I - \A) = \det(x\I - \A)\, \I \) by multiplying out.
2. For a general \( \A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in M_2(\nR) \), show that \( \adj(x\I - \A) = x\I - \adj \A \) and \( \A + \adj \A = (\tr \A) \I \).
3. Deduce from (b), without using @thm-adjugate-identity over \( \nR[x] \), that \( (x\I - \A)\adj(x\I - \A) = \big(x^2 - (\tr \A)x + \det \A\big) \I \), and check that \( x^2 - (\tr \A)x + \det \A = \det(x\I - \A) \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. \( x\I - \A = \begin{pmatrix} x - 1 & -2 \\ -3 & x - 4 \end{pmatrix} \), so \( \det(x\I - \A) = (x - 1)(x - 4) - 6 = x^2 - 5x - 2 \), and by @def-adjugate, \( \adj(x\I - \A) = \begin{pmatrix} x - 4 & 2 \\ 3 & x - 1 \end{pmatrix} \). The product has entries \( (x - 1)(x - 4) - 6 = x^2 - 5x - 2 \), \( 2(x - 1) - 2(x - 1) = 0 \), \( -3(x - 4) + 3(x - 4) = 0 \) and \( -6 + (x - 4)(x - 1) = x^2 - 5x - 2 \), so it is \( (x^2 - 5x - 2) \I \).
2. \( x\I - \A = \begin{pmatrix} x - a & -b \\ -c & x - d \end{pmatrix} \), so \( \adj(x\I - \A) = \begin{pmatrix} x - d & b \\ c & x - a \end{pmatrix} = x\I - \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} = x\I - \adj \A \). Also \( \A + \adj \A = \begin{pmatrix} a + d & 0 \\ 0 & a + d \end{pmatrix} = (\tr \A) \I \).
3. Since \( x\I \) commutes with every matrix, expanding with (b) gives
   \[
   \begin{aligned}
   (x\I - \A)(x\I - \adj \A) &= x^2 \I - x(\A + \adj \A) + \A \adj \A \\
   &= x^2 \I - (\tr \A)x \I + (ad - bc) \I,
   \end{aligned}
   \]
   where \( \A \adj \A = (ad - bc) \I \) is the computation of @thm-two-by-two-inverse over \( \nR \). Finally \( \det(x\I - \A) = (x - a)(x - d) - bc = x^2 - (a + d)x + (ad - bc) \), which is \( x^2 - (\tr \A)x + \det \A \).
:::
:::
