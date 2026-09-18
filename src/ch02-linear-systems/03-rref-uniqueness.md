# Uniqueness of the Reduced Form

Gauss–Jordan elimination involves choices: which non-zero entry to use as a pivot, and in what order to perform the operations. Different choices give different intermediate matrices, and different row echelon forms. The previous section claimed that they always end at the **same** reduced row echelon form. This matters more than it seems. Pivot columns, free variables, and later the rank of a matrix are all read off from the reduced form; if two people could reduce the same matrix to two different answers, none of these would be well defined. This section proves the claim.

## What row operations remember

Row operations change the columns of a matrix. What do they keep? Take
\[
\A = \begin{pmatrix} 1 & 2 & 1 & 3 \\ 2 & 4 & 0 & 2 \\ 3 & 6 & 2 & 7 \end{pmatrix}
\quad \text{and its RREF} \quad
\R = \begin{pmatrix} 1 & 2 & 0 & 1 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{pmatrix}
\]
over \( \nR \) (the computation is carried out in an example later in this section). The columns of \( \R \) look nothing like those of \( \A \). But look at how the columns depend on each other. In \( \R \), column 2 is twice column 1, and column 4 is column 1 plus twice column 3. In \( \A \), with columns \( \a_1, \dots, \a_4 \),
\[
\a_2 = (2, 4, 6) = 2\a_1, \qquad \a_4 = (3, 2, 7) = (1, 2, 3) + 2(1, 0, 2) = \a_1 + 2\a_3 .
\]
The same relations, with the same coefficients. This is no accident. A relation \( x_1\a_1 + \dots + x_n\a_n = \0 \) among the columns says \( \A\x = \0 \) (@thm-matrix-times-vector-columns), and row operations do not change the solutions of a homogeneous system.

::: {#lem-row-equivalent-same-null-space}
[Row equivalent matrices have the same homogeneous solutions]

Let \( \A, \B \in M_{m \times n}(F) \) be row equivalent. Then for every \( \x \in F^n \), \( \A\x = \0 \) if and only if \( \B\x = \0 \).
:::

::: {.proof}
Let a sequence of elementary row operations turn \( \A \) into \( \B \). By @lem-row-ops-act-on-columns, the same sequence turns \( [\, \A \mid \0 \,] \) into \( [\, \B \mid \0' \,] \), where \( \0' \) is obtained from the zero column by row operations and so is again the zero column. Hence \( [\, \A \mid \0 \,] \) and \( [\, \B \mid \0 \,] \) are row equivalent, and by @thm-row-ops-preserve-solutions (c) the systems \( \A\x = \0 \) and \( \B\x = \0 \) have the same solution set.
:::

Rewriting \( \A\x \) as a combination of columns turns the lemma into the statement we observed.

::: {#lem-row-ops-preserve-column-relations}
[Row operations preserve column relations]

Let \( \A, \B \in M_{m \times n}(F) \) have columns \( \a_1, \dots, \a_n \) and \( \b_1, \dots, \b_n \), and suppose that \( \A\x = \0 \Leftrightarrow \B\x = \0 \) for every \( \x \in F^n \). This holds, for instance, if \( \A \) and \( \B \) are row equivalent (@lem-row-equivalent-same-null-space). Then:

::: {.enumerate options="label=(\alph*)"}
1. for all \( x_1, \dots, x_n \in F \): \( x_1\a_1 + \dots + x_n\a_n = \0 \) if and only if \( x_1\b_1 + \dots + x_n\b_n = \0 \);
2. for every index \( l \) and all scalars \( d_1, \dots, d_{l-1} \): \( \a_l = d_1\a_1 + \dots + d_{l-1}\a_{l-1} \) if and only if \( \b_l = d_1\b_1 + \dots + d_{l-1}\b_{l-1} \);
3. for every index \( l \): \( \a_l \in \Span(\a_1, \dots, \a_{l-1}) \) if and only if \( \b_l \in \Span(\b_1, \dots, \b_{l-1}) \).
:::
:::

::: {.proof}
(a) By @thm-matrix-times-vector-columns, \( x_1\a_1 + \dots + x_n\a_n = \A\x \) and \( x_1\b_1 + \dots + x_n\b_n = \B\x \), where \( \x = (x_1, \dots, x_n) \). The hypothesis says \( \A\x = \0 \Leftrightarrow \B\x = \0 \).

(b) The equation \( \a_l = d_1\a_1 + \dots + d_{l-1}\a_{l-1} \) holds if and only if \( d_1\a_1 + \dots + d_{l-1}\a_{l-1} + (-1)\a_l + 0\a_{l+1} + \dots + 0\a_n = \0 \). By (a), with these coefficients, this holds if and only if the same combination of the \( \b_j \) is \( \0 \), that is, \( \b_l = d_1\b_1 + \dots + d_{l-1}\b_{l-1} \).

(c) By @def-span, \( \a_l \in \Span(\a_1, \dots, \a_{l-1}) \) means that the left side of (b) holds for **some** scalars \( d_1, \dots, d_{l-1} \). By (b) this happens if and only if the right side holds for some scalars, which means \( \b_l \in \Span(\b_1, \dots, \b_{l-1}) \).
:::

::: {.warning}
**Row operations preserve column relations, not columns or their span.** For \( \A = \begin{pmatrix} 1 & 2 \\ 1 & 2 \end{pmatrix} \) over \( \nR \), the operation \( R_2 \to R_2 - R_1 \) gives \( \begin{pmatrix} 1 & 2 \\ 0 & 0 \end{pmatrix} \). The relation "column 2 \( = 2 \cdot \) column 1" holds in both. But every column of \( \A \) lies on the line \( \Span((1, 1)) \), and every column of the new matrix lies on the different line \( \Span((1, 0)) \). So the span of the columns changed. To answer a question about the columns of \( \A \) themselves, find the relations from the reduced form, and then use them on the columns of \( \A \).
:::

## The columns of a reduced matrix

In a matrix in RREF, the column relations can be read off at a glance: pivot columns are standard basis vectors, and a non-pivot column **displays its own coefficients**. We record this precisely, together with a description of the pivot columns that does not mention pivots at all.

::: {#lem-rref-columns}
[Columns of a matrix in RREF]

Let \( \R \in M_{m \times n}(F) \) be in reduced row echelon form, with entries \( r_{il} \), columns \( \u_1, \dots, \u_n \), and pivot columns \( j_1 < \dots < j_r \).

::: {.enumerate options="label=(\alph*)"}
1. For each \( i = 1, \dots, r \), the pivot column \( \u_{j_i} \) is \( \e_i \).
2. If \( l \) is **not** a pivot column, then
\[
\u_l = \sum_{i \,:\, j_i < l} r_{il}\, \e_i = \sum_{i \,:\, j_i < l} r_{il}\, \u_{j_i} .
\]
3. Column \( l \) is a pivot column **if and only if** \( \u_l \notin \Span(\u_1, \dots, \u_{l-1}) \).
:::
:::

::: {.proof}
(a) By (E3) the entry of \( \u_{j_i} \) in row \( i \) is \( 1 \), and by (E4) its other entries are \( 0 \).

(b) Let \( l \) be a non-pivot column, and look at the entry \( r_{il} \) in each row \( i \). If \( i > r \), row \( i \) is zero by (E1), so \( r_{il} = 0 \). If \( i \le r \) and \( j_i > l \), then \( r_{il} \) lies strictly before the leading entry of row \( i \), so \( r_{il} = 0 \). The case \( j_i = l \) does not occur, since \( l \) is not a pivot column. So the only possibly non-zero entries of \( \u_l \) are the \( r_{il} \) with \( j_i < l \), which gives the first expression; the second follows from (a).

(c) If \( l \) is not a pivot column, (b) writes \( \u_l \) as a combination of the columns \( \u_{j_i} \) with \( j_i < l \), so \( \u_l \in \Span(\u_1, \dots, \u_{l-1}) \). Conversely, let \( l = j_i \) be a pivot column. For each \( l' < j_i \), the entry \( r_{il'} \) lies before the leading entry of row \( i \), so it is \( 0 \). Hence every vector of \( \Span(\u_1, \dots, \u_{l-1}) \), being a combination of vectors with \( i \)-th entry \( 0 \), has \( i \)-th entry \( 0 \). But \( \u_l = \e_i \) has \( i \)-th entry \( 1 \neq 0 \), so \( \u_l \notin \Span(\u_1, \dots, \u_{l-1}) \).
:::

Part (c) says: reading the columns from left to right, a column gets a pivot exactly when it is **new**, not a combination of the columns before it. That condition is about column relations only, and column relations survive row operations. This is the whole idea of the uniqueness proof.

## The uniqueness theorem

We can now prove that the reduced form depends only on the homogeneous solutions, and hence not on the operations used to reach it.

::: {#thm-rref-unique}
[Uniqueness of the reduced row echelon form]

Let \( \R, \R' \in M_{m \times n}(F) \) be in reduced row echelon form, and suppose that \( \R\x = \0 \Leftrightarrow \R'\x = \0 \) for every \( \x \in F^n \). Then \( \R = \R' \).

Consequently, every matrix \( \A \in M_{m \times n}(F) \) is row equivalent to **exactly one** matrix in reduced row echelon form, called **the RREF of \( \A \)**.
:::

::: {.idea}
A column dependence \( \sum_j x_j \u_j = \0 \) is exactly a null vector \( \x \), so \( \R \) and \( \R' \) have the same column relations. The pivot columns are exactly the columns that are not combinations of earlier columns (@lem-rref-columns (c)), so \( \R \) and \( \R' \) have the same pivot columns. A pivot column is a standard basis vector in both. A non-pivot column of an RREF matrix is determined by how it is built from the pivot columns before it (@lem-rref-columns (b)), and that recipe is a column relation, so it is the same in both. Hence every column agrees.
:::

::: {.proof}
Let \( \u_1, \dots, \u_n \) and \( \u'_1, \dots, \u'_n \) be the columns of \( \R \) and \( \R' \), and \( r_{il} \) the entries of \( \R \). By hypothesis, @lem-row-ops-preserve-column-relations applies to \( \R \) and \( \R' \).

*Same pivot columns.* For each \( l \), by @lem-row-ops-preserve-column-relations (c), \( \u_l \in \Span(\u_1, \dots, \u_{l-1}) \) if and only if \( \u'_l \in \Span(\u'_1, \dots, \u'_{l-1}) \). By @lem-rref-columns (c) applied to \( \R \) and to \( \R' \), column \( l \) is a pivot column of \( \R \) if and only if it is a pivot column of \( \R' \). So both matrices have the same pivot columns \( j_1 < \dots < j_r \).

*Pivot columns agree.* By @lem-rref-columns (a), \( \u_{j_i} = \e_i = \u'_{j_i} \) for \( i = 1, \dots, r \).

*Same non-pivot columns.* Let \( l \) be a non-pivot column. By @lem-rref-columns (b) for \( \R \),
\[
\u_l = \sum_{i \,:\, j_i < l} r_{il}\, \u_{j_i} .
\]
This is an equation of the form in @lem-row-ops-preserve-column-relations (b), with coefficient \( r_{il} \) on column \( j_i \) and \( 0 \) on the other earlier columns. By that lemma, the same equation holds for \( \R' \):
\[
\u'_l = \sum_{i \,:\, j_i < l} r_{il}\, \u'_{j_i} = \sum_{i \,:\, j_i < l} r_{il}\, \e_i = \u_l ,
\]
where the middle equality uses @lem-rref-columns (a) for \( \R' \), and the last uses @lem-rref-columns (b) for \( \R \).

Hence \( \u_l = \u'_l \) for every \( l \), and \( \R = \R' \).

For the consequence, let \( \A \in M_{m \times n}(F) \). By @thm-rref-exists, \( \A \) is row equivalent to at least one matrix in RREF. Suppose \( \A \) is row equivalent to \( \R \) and to \( \R' \), both in RREF. Row equivalence is an equivalence relation (@thm-row-ops-preserve-solutions (b)), so \( \R \) is row equivalent to \( \R' \). By @lem-row-equivalent-same-null-space, \( \R\x = \0 \Leftrightarrow \R'\x = \0 \) for every \( \x \), and by the first part \( \R = \R' \). This proves the theorem.
:::

Notice what the proof did **not** do: it never compared the two sequences of operations. A direct comparison of two runs of the algorithm would have to track every choice, and quickly becomes unmanageable. The proof instead found a description of the RREF, "pivots where a new column appears, and coefficients of the old columns elsewhere", that refers only to the null space, which the operations cannot change.

The theorem also gives a practical test: two matrices of the same size are row equivalent exactly when their RREFs are equal (you will write out the two-line proof in @exr-rref-uniqueness-b2). For example, over \( \nR \), \( \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} \) and \( \begin{pmatrix} 2 & 4 \\ 0 & 0 \end{pmatrix} \) both reduce to \( \begin{pmatrix} 1 & 2 \\ 0 & 0 \end{pmatrix} \), by \( R_2 \to R_2 - 2R_1 \) and by \( R_1 \to \tfrac12 R_1 \) respectively, so they are row equivalent. But \( \begin{pmatrix} 1 & 3 \\ 2 & 6 \end{pmatrix} \) reduces to \( \begin{pmatrix} 1 & 3 \\ 0 & 0 \end{pmatrix} \neq \begin{pmatrix} 1 & 2 \\ 0 & 0 \end{pmatrix} \), so it is row equivalent to neither, even though all three matrices have the same pivot columns.

::: {#exm-two-echelon-forms-same-rref}
[Two echelon forms, one reduced form]

Let \( \A = \begin{pmatrix} 1 & 2 & 1 & 3 \\ 2 & 4 & 0 & 2 \\ 3 & 6 & 2 & 7 \end{pmatrix} \) over \( \nR \).

::: {.enumerate options="label=(\alph*)"}
1. Reduce \( \A \) to a row echelon form in two ways: first using row 1 as the first pivot row, then starting with \( R_1 \leftrightarrow R_2 \).
2. Continue both to reduced row echelon form.
3. Read the column relations of \( \A \) off the RREF.
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. First route:
\[
\A \xrightarrow{R_2 \to R_2 - 2R_1}
\begin{pmatrix} 1 & 2 & 1 & 3 \\ 0 & 0 & -2 & -4 \\ 3 & 6 & 2 & 7 \end{pmatrix}
\xrightarrow{R_3 \to R_3 - 3R_1}
\begin{pmatrix} 1 & 2 & 1 & 3 \\ 0 & 0 & -2 & -4 \\ 0 & 0 & -1 & -2 \end{pmatrix}
\xrightarrow{R_3 \to R_3 - \frac12 R_2}
\begin{pmatrix} 1 & 2 & 1 & 3 \\ 0 & 0 & -2 & -4 \\ 0 & 0 & 0 & 0 \end{pmatrix} = \E_1 .
\]
Second route:
\[
\A \xrightarrow{R_1 \leftrightarrow R_2}
\begin{pmatrix} 2 & 4 & 0 & 2 \\ 1 & 2 & 1 & 3 \\ 3 & 6 & 2 & 7 \end{pmatrix}
\xrightarrow{R_2 \to R_2 - \frac12 R_1}
\begin{pmatrix} 2 & 4 & 0 & 2 \\ 0 & 0 & 1 & 2 \\ 3 & 6 & 2 & 7 \end{pmatrix}
\xrightarrow{R_3 \to R_3 - \frac32 R_1}
\begin{pmatrix} 2 & 4 & 0 & 2 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 2 & 4 \end{pmatrix}
\xrightarrow{R_3 \to R_3 - 2R_2}
\begin{pmatrix} 2 & 4 & 0 & 2 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{pmatrix} = \E_2 .
\]
Both \( \E_1 \) and \( \E_2 \) are in row echelon form, and \( \E_1 \neq \E_2 \). Both have pivot columns 1 and 3.
2. From \( \E_1 \):
\[
\E_1 \xrightarrow{R_2 \to -\frac12 R_2}
\begin{pmatrix} 1 & 2 & 1 & 3 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{pmatrix}
\xrightarrow{R_1 \to R_1 - R_2}
\begin{pmatrix} 1 & 2 & 0 & 1 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{pmatrix}.
\]
From \( \E_2 \):
\[
\E_2 \xrightarrow{R_1 \to \frac12 R_1}
\begin{pmatrix} 1 & 2 & 0 & 1 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{pmatrix}.
\]
The two routes end at the same matrix \( \R \), as @thm-rref-unique guarantees.
3. By @lem-rref-columns (b), the non-pivot columns of \( \R \) are \( \u_2 = 2\u_1 \) and \( \u_4 = 1 \cdot \u_1 + 2\u_3 \), reading the coefficients from the entries of each column. By @lem-row-ops-preserve-column-relations (b), the same relations hold for the columns of \( \A \): \( \a_2 = 2\a_1 \) and \( \a_4 = \a_1 + 2\a_3 \). Check: \( 2(1, 2, 3) = (2, 4, 6) \) and \( (1, 2, 3) + 2(1, 0, 2) = (3, 2, 7) \).
:::
:::

Both echelon forms in the example had the same pivot columns, although they were different matrices. That is also true in general, and it is the practical version of the theorem.

## Pivot columns are well defined

::: {#cor-pivot-columns-well-defined}
[Pivot columns are well defined]

Let \( \A \in M_{m \times n}(F) \) have columns \( \a_1, \dots, \a_n \). Define the **pivot columns of \( \A \)** to be the pivot columns of the RREF of \( \A \).

::: {.enumerate options="label=(\alph*)"}
1. Column \( l \) is a pivot column of \( \A \) **if and only if** \( \a_l \notin \Span(\a_1, \dots, \a_{l-1}) \).
2. If \( \E \) is **any** matrix in row echelon form that is row equivalent to \( \A \), then the pivot columns of \( \E \) are the pivot columns of \( \A \). In particular, every row echelon form of \( \A \) has the same number of non-zero rows.
:::
:::

::: {.idea}
Part (a) combines @lem-rref-columns (c) with the fact that column relations pass from the RREF back to \( \A \). For (b), finish the reduction of \( \E \): scale each pivot to \( 1 \) and clear the entries above the pivots. These operations never move a leading entry, so they produce a matrix in RREF with the same pivot columns as \( \E \), and by uniqueness it is the RREF of \( \A \).
:::

::: {.proof}
The RREF of \( \A \) is well defined by @thm-rref-unique; let \( \u_1, \dots, \u_n \) be its columns.

(a) \( \A \) and its RREF are row equivalent, so by @lem-row-ops-preserve-column-relations (c), \( \a_l \in \Span(\a_1, \dots, \a_{l-1}) \) if and only if \( \u_l \in \Span(\u_1, \dots, \u_{l-1}) \). By @lem-rref-columns (c), the latter fails exactly when \( l \) is a pivot column.

(b) Let \( \E \) have entries \( e_{hl} \) and pivot columns \( j_1 < \dots < j_s \). First perform \( R_i \to e_{i j_i}^{-1} R_i \) for \( i = 1, \dots, s \), which is legal since each pivot \( e_{i j_i} \) is non-zero. Scaling a row by a non-zero scalar does not change which of its entries are zero (@thm-field-basic-properties (d), (f)), so the result is still in row echelon form with the same pivot columns, and now every pivot is \( 1 \). Next, for \( i = 1, 2, \dots, s \) in turn, and for each \( h < i \), perform \( R_h \to R_h - cR_i \), where \( c \) is the current entry of row \( h \) in column \( j_i \). Row \( i \) is zero in all columns before \( j_i \), so this changes row \( h \) only in columns \( \ge j_i > j_h \). Hence the leading entry of row \( h \) is still a \( 1 \) in column \( j_h \), no zero row is touched, and the entries below every pivot stay \( 0 \). The operation makes the entry in position \( (h, j_i) \) equal to \( 0 \), and it does not spoil the entries \( (h, j_{i'}) \) with \( i' < i \) cleared earlier, because row \( i \) has a \( 0 \) in column \( j_{i'} < j_i \). At the end, every pivot column is a standard basis vector, so the matrix is in RREF, with pivot columns \( j_1, \dots, j_s \).

This matrix is row equivalent to \( \E \), hence to \( \A \) (@thm-row-ops-preserve-solutions (b)). By @thm-rref-unique it is the RREF of \( \A \). Therefore the pivot columns of \( \E \) are those of \( \A \). Since the non-zero rows of \( \E \) correspond one-to-one to its pivots, their number \( s \) is the number of pivot columns of \( \A \), whichever \( \E \) we chose.
:::

In practice, (b) means we may stop at any row echelon form to find the pivot columns, and (a) means we can sometimes find them with no elimination at all. Part (a) also says that the pivot columns of \( \A \) are exactly the columns kept when the list \( (\a_1, \dots, \a_n) \) is sifted as in @thm-sift: a column is kept exactly when it is not in the span of the columns before it. The number of pivot columns is the first candidate for a measure of "how much a matrix contains"; later in this chapter it becomes the rank.

::: {.check}
Without computing any row operations, find the pivot columns of \( \A = \begin{pmatrix} 1 & 2 & 0 & 1 \\ 2 & 4 & 1 & 3 \end{pmatrix} \) over \( \nR \).
:::

::: {.solution}
Use @cor-pivot-columns-well-defined (a) column by column. \( \a_1 = (1, 2) \neq \0 \), so it is not in \( \Span() = \{ \0 \} \): pivot. \( \a_2 = (2, 4) = 2\a_1 \): not a pivot. \( \a_3 = (0, 1) \) is not a multiple of \( (1, 2) \), and \( \Span(\a_1, \a_2) = \Span((1, 2)) \): pivot. \( \a_4 = (1, 3) = \a_1 + \a_3 \): not a pivot. The pivot columns are 1 and 3.
:::

::: {.warning}
**Uniqueness is a property of the reduced form only.** A matrix has many row echelon forms (@exm-two-echelon-forms-same-rref gave two), and it is only their pivot positions that agree. Also, two different matrices in RREF with the **same** pivot columns need not be row equivalent: \( \begin{pmatrix} 1 & 2 \end{pmatrix} \) and \( \begin{pmatrix} 1 & 3 \end{pmatrix} \) are both in RREF with pivot column 1, but they are different RREF matrices, so by @thm-rref-unique neither is row equivalent to the other.
:::

## Exercises

### A. Check your understanding

::: {#exr-rref-uniqueness-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the uniqueness theorem for the reduced row echelon form.
2. Determine whether the following statement is true: "if \( \A \) and \( \B \) are row equivalent, then the columns of \( \A \) and the columns of \( \B \) span the same subspace." Justify your answer.
3. Determine whether the following statement is true: "if \( \A \) and \( \B \) are row equivalent and \( \a_3 = \a_1 - \a_2 \) for the columns of \( \A \), then \( \b_3 = \b_1 - \b_2 \) for the columns of \( \B \)." Justify your answer.
4. Determine whether the following statement is true: "any two row echelon forms of the same matrix have the same number of zero rows." Justify your answer.
5. In the RREF of a matrix, what do the entries of a non-pivot column tell you about the original matrix?
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. If \( \R, \R' \in M_{m \times n}(F) \) are in RREF and \( \R\x = \0 \Leftrightarrow \R'\x = \0 \) for all \( \x \in F^n \), then \( \R = \R' \). Hence every matrix is row equivalent to exactly one matrix in RREF.
2. False. \( \begin{pmatrix} 1 & 2 \\ 1 & 2 \end{pmatrix} \) and \( \begin{pmatrix} 1 & 2 \\ 0 & 0 \end{pmatrix} \) are row equivalent, but their columns span \( \Span((1, 1)) \) and \( \Span((1, 0)) \), which are different lines in \( \nR^2 \).
3. True, by @lem-row-ops-preserve-column-relations (b) with \( l = 3 \), \( d_1 = 1 \), \( d_2 = -1 \).
4. True. By @cor-pivot-columns-well-defined (b), every row echelon form of an \( m \times n \) matrix \( \A \) has exactly as many non-zero rows as \( \A \) has pivot columns, so the number of zero rows is \( m \) minus that number.
5. If column \( l \) is not a pivot column, its entries \( r_{il} \) (for the pivot rows \( i \) with \( j_i < l \)) are the coefficients expressing column \( l \) of the original matrix as a combination of its pivot columns: \( \a_l = \sum_{j_i < l} r_{il}\, \a_{j_i} \).
:::
:::

### B. Practice

::: {#exr-rref-uniqueness-b1}
[B1: Column relations]

Let \( \A = \begin{pmatrix} 1 & -1 & 0 & 2 & 1 \\ 2 & -2 & 1 & 7 & 0 \\ 1 & -1 & 1 & 5 & 1 \end{pmatrix} \) over \( \nR \). Find the RREF of \( \A \), naming each operation. Hence find the pivot columns of \( \A \), and express each non-pivot column of \( \A \) as a linear combination of the pivot columns before it. Check your answer on the columns of \( \A \).
:::

::: {.solution}
\[
\A \xrightarrow{R_2 \to R_2 - 2R_1}
\begin{pmatrix} 1 & -1 & 0 & 2 & 1 \\ 0 & 0 & 1 & 3 & -2 \\ 1 & -1 & 1 & 5 & 1 \end{pmatrix}
\xrightarrow{R_3 \to R_3 - R_1}
\begin{pmatrix} 1 & -1 & 0 & 2 & 1 \\ 0 & 0 & 1 & 3 & -2 \\ 0 & 0 & 1 & 3 & 0 \end{pmatrix}
\xrightarrow{R_3 \to R_3 - R_2}
\begin{pmatrix} 1 & -1 & 0 & 2 & 1 \\ 0 & 0 & 1 & 3 & -2 \\ 0 & 0 & 0 & 0 & 2 \end{pmatrix}
\]
\[
\xrightarrow{R_3 \to \frac12 R_3}
\begin{pmatrix} 1 & -1 & 0 & 2 & 1 \\ 0 & 0 & 1 & 3 & -2 \\ 0 & 0 & 0 & 0 & 1 \end{pmatrix}
\xrightarrow{R_1 \to R_1 - R_3}
\begin{pmatrix} 1 & -1 & 0 & 2 & 0 \\ 0 & 0 & 1 & 3 & -2 \\ 0 & 0 & 0 & 0 & 1 \end{pmatrix}
\xrightarrow{R_2 \to R_2 + 2R_3}
\begin{pmatrix} 1 & -1 & 0 & 2 & 0 \\ 0 & 0 & 1 & 3 & 0 \\ 0 & 0 & 0 & 0 & 1 \end{pmatrix}.
\]
The pivot columns are 1, 3 and 5. By @lem-rref-columns (b), in the RREF column 2 is \( -1 \) times column 1, and column 4 is \( 2 \) times column 1 plus \( 3 \) times column 3. By @lem-row-ops-preserve-column-relations (b), the columns of \( \A \) satisfy
\[
\a_2 = -\a_1, \qquad \a_4 = 2\a_1 + 3\a_3 .
\]
Check: \( -(1, 2, 1) = (-1, -2, -1) = \a_2 \), and \( 2(1, 2, 1) + 3(0, 1, 1) = (2, 7, 5) = \a_4 \).
:::

::: {#exr-rref-uniqueness-b2}
[B2: Row equivalence via the RREF]

Prove that two matrices \( \A, \B \in M_{m \times n}(F) \) are row equivalent if and only if they have the same RREF.
:::

::: {.solution}
(⇒) Suppose \( \A \) and \( \B \) are row equivalent, and let \( \R \) be the RREF of \( \B \). Then \( \A \) is row equivalent to \( \B \), and \( \B \) to \( \R \), so \( \A \) is row equivalent to \( \R \) by transitivity (@thm-row-ops-preserve-solutions (b)). By the uniqueness in @thm-rref-unique, \( \R \) is the RREF of \( \A \).

(⇐) Suppose both have the RREF \( \R \). Then \( \A \) is row equivalent to \( \R \), and by symmetry \( \R \) is row equivalent to \( \B \) (@thm-row-ops-preserve-solutions (b)). By transitivity \( \A \) is row equivalent to \( \B \).
:::

::: {#exr-rref-uniqueness-b3}
[B3: Row equivalent or not?]

Determine whether the matrices in each pair are row equivalent over \( \nR \). Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \P = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 5 & 7 \end{pmatrix} \) and \( \Q = \begin{pmatrix} 1 & 1 & 2 \\ 3 & 4 & 7 \end{pmatrix} \).
2. \( \P = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \\ 0 & 1 & 2 \end{pmatrix} \) and \( \Q = \begin{pmatrix} 1 & 0 & -1 \\ 0 & 1 & 2 \\ 1 & 1 & 2 \end{pmatrix} \).
:::
:::

::: {.solution}
By @exr-rref-uniqueness-b2, two matrices of the same size are row equivalent exactly when their RREFs are equal. So we compute both RREFs.

::: {.enumerate options="label=(\alph*)"}
1. \( \P \xrightarrow{R_2 \to R_2 - 2R_1} \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \end{pmatrix} \xrightarrow{R_1 \to R_1 - 2R_2} \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \end{pmatrix} \), and \( \Q \xrightarrow{R_2 \to R_2 - 3R_1} \begin{pmatrix} 1 & 1 & 2 \\ 0 & 1 & 1 \end{pmatrix} \xrightarrow{R_1 \to R_1 - R_2} \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \end{pmatrix} \). The RREFs are equal, so \( \P \) and \( \Q \) are row equivalent.
2. \( \P \xrightarrow{R_2 \to R_2 - R_1} \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 0 & 1 & 2 \end{pmatrix} \xrightarrow{R_1 \to R_1 - R_2} \begin{pmatrix} 1 & 0 & -1 \\ 0 & 1 & 2 \\ 0 & 1 & 2 \end{pmatrix} \xrightarrow{R_3 \to R_3 - R_2} \begin{pmatrix} 1 & 0 & -1 \\ 0 & 1 & 2 \\ 0 & 0 & 0 \end{pmatrix} \).

   \( \Q \xrightarrow{R_3 \to R_3 - R_1} \begin{pmatrix} 1 & 0 & -1 \\ 0 & 1 & 2 \\ 0 & 1 & 3 \end{pmatrix} \xrightarrow{R_3 \to R_3 - R_2} \begin{pmatrix} 1 & 0 & -1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix} \xrightarrow{R_1 \to R_1 + R_3} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix} \xrightarrow{R_2 \to R_2 - 2R_3} \I_3 \).

   The RREFs differ (one has a zero row, the other is \( \I_3 \)), so \( \P \) and \( \Q \) are **not** row equivalent. Consistently with @cor-pivot-columns-well-defined, \( \P \) has pivot columns 1, 2 while \( \Q \) has 1, 2, 3.
:::
:::

### C. Going deeper

::: {#exr-rref-uniqueness-c1}
[C1: Counting reduced forms]

::: {.enumerate options="label=(\alph*)"}
1. List, by pivot columns, all \( 2 \times 3 \) matrices over \( \nF_2 \) in reduced row echelon form, and show that there are exactly \( 15 \) of them.
2. Deduce that \( M_{2 \times 3}(\nF_2) \), which has \( 64 \) elements, splits into exactly \( 15 \) classes of row equivalent matrices.
3. Show that over a field with \( q \) elements there are exactly \( 2q^2 + 2q + 3 \) such matrices.
:::
:::

::: {.solution}
We count over a field \( F \) with \( q \) elements, sorting by the list of pivot columns. In a matrix in RREF, a pivot column is forced (it is \( \e_i \)), an entry before a leading entry or in a zero row is forced to be \( 0 \), and every other entry, one lying in a non-pivot column to the right of its row's pivot, is free.

::: {.enumerate options="label=(\alph*)"}
1. With \( q = 2 \), writing \( * \) for a free entry:
   - no pivots: \( \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} \), \( 1 \) matrix;
   - pivot column 1 only: \( \begin{pmatrix} 1 & * & * \\ 0 & 0 & 0 \end{pmatrix} \), \( 4 \) matrices;
   - pivot column 2 only: \( \begin{pmatrix} 0 & 1 & * \\ 0 & 0 & 0 \end{pmatrix} \), \( 2 \) matrices;
   - pivot column 3 only: \( \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} \), \( 1 \) matrix;
   - pivot columns 1, 2: \( \begin{pmatrix} 1 & 0 & * \\ 0 & 1 & * \end{pmatrix} \), \( 4 \) matrices;
   - pivot columns 1, 3: \( \begin{pmatrix} 1 & * & 0 \\ 0 & 0 & 1 \end{pmatrix} \), \( 2 \) matrices;
   - pivot columns 2, 3: \( \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \), \( 1 \) matrix.

   A \( 2 \times 3 \) matrix has at most two pivots, so these are all the cases. The total is \( 1 + 4 + 2 + 1 + 4 + 2 + 1 = 15 \).
2. Row equivalence is an equivalence relation (@thm-row-ops-preserve-solutions (b)), so \( M_{2 \times 3}(\nF_2) \) is partitioned into equivalence classes (@thm-partition). By @thm-rref-unique, each class contains exactly one matrix in RREF: at least one by @thm-rref-exists, and at most one since two RREF matrices in the same class would be row equivalent, hence equal. So the classes correspond one-to-one to the \( 15 \) matrices of (a).
3. The same list, with each free entry taking \( q \) values, gives \( 1 + q^2 + q + 1 + q^2 + q + 1 = 2q^2 + 2q + 3 \). For \( q = 2 \) this is \( 8 + 4 + 3 = 15 \), as in (a).
:::
:::

::: {#exr-rref-uniqueness-c2}
[C2: Deleting a column]

Let \( \A \in M_{m \times n}(F) \) with \( n \ge 2 \), and let \( \R \) be its RREF.

::: {.enumerate options="label=(\alph*)"}
1. Let \( \A' \) and \( \R' \) be obtained from \( \A \) and \( \R \) by deleting the **last** column. Prove that \( \R' \) is the RREF of \( \A' \).
2. Show by an example that the corresponding statement for deleting the **first** column is false.
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Let a sequence of row operations turn \( \A \) into \( \R \). By @lem-row-ops-act-on-columns, the same sequence turns \( \A' \) into \( \R' \), so \( \A' \) is row equivalent to \( \R' \). By @thm-rref-unique it suffices to show that \( \R' \) is in RREF. Let \( j_1 < \dots < j_r \) be the pivot columns of \( \R \). If \( j_r < n \), then deleting column \( n \) does not change any leading entry or any pivot column, and the zero rows of \( \R \) stay zero, so (E1)–(E4) still hold. If \( j_r = n \), then row \( r \) of \( \R \) is zero except for its pivot in column \( n \), so in \( \R' \) rows \( r, \dots, m \) are zero and rows \( 1, \dots, r - 1 \) keep their leading entries in columns \( j_1 < \dots < j_{r-1} \) and their pivot columns. Again (E1)–(E4) hold, with \( r - 1 \) pivots. Hence \( \R' \) is in RREF, and it is the RREF of \( \A' \).
2. Let \( \A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) over \( \nR \). Then \( \A \xrightarrow{R_1 \to R_1 - R_2} \I_2 \), so its RREF is \( \I_2 \), and deleting the first column of \( \I_2 \) gives \( \begin{pmatrix} 0 \\ 1 \end{pmatrix} \). But deleting the first column of \( \A \) gives \( \begin{pmatrix} 1 \\ 1 \end{pmatrix} \), whose RREF is \( \begin{pmatrix} 1 \\ 0 \end{pmatrix} \), via \( R_2 \to R_2 - R_1 \). These differ. The pivot of a later column depends on the columns before it, so removing an early column can move pivots.
:::
:::
