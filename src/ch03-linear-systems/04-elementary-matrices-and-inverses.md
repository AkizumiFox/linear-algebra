# Elementary Matrices and Inverses

Gaussian elimination is a list of instructions: swap these rows, scale that one, add a multiple of one row to another. So far it lives outside algebra, as something we do to a matrix. This section turns every row operation into a matrix, so that "apply an operation" becomes "multiply on the left". With that one observation the algorithm becomes a tool for proofs. We use it to prove the main theorem about invertible matrices, to show that a one-sided inverse of a square matrix is automatically two-sided, which Chapter 0 stated after @def-invertible-matrix but could not prove, and to compute inverses.

Throughout, \( F \) is a field, and we use the three elementary row operations of @def-elementary-row-operations with their notation: the swap \( R_i \leftrightarrow R_j \) (\( i \neq j \)), the scaling \( R_i \to cR_i \) (\( c \) **non-zero**), and the replacement \( R_i \to R_i + cR_j \) (\( i \neq j \), any \( c \in F \)).

## Row operations are matrix multiplications

We have already seen one row operation disguised as a product. In @exm-row-equivalence of Chapter 0, multiplying \( \A = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 5 & 0 \end{pmatrix} \) on the left by \( \E = \begin{pmatrix} 1 & 0 \\ -2 & 1 \end{pmatrix} \) replaced row 2 by row 2 minus twice row 1, that is, it performed \( R_2 \to R_2 - 2R_1 \). Look at \( \E \) itself: it is what that same operation does to the identity matrix \( \I_2 \). This is no accident, and it deserves a name.

*An elementary matrix is the identity matrix after one row operation.*

::: {#def-elementary-matrix}
[Elementary matrix]

Let \( m \ge 1 \). A matrix \( \E \in M_m(F) \) is an **elementary matrix** if it is obtained from \( \I_m \) by performing **exactly one** elementary row operation. Writing \( \E_{ij} \) for the matrix unit (\( 1 \) in entry \( (i, j) \), \( 0 \) elsewhere; see @exm-standard-bases), the three kinds are:

1. \( \P_{ij} \), obtained by \( R_i \leftrightarrow R_j \) with \( i \neq j \): the identity with rows \( i \) and \( j \) swapped;
2. \( \D_i(c) = \diag(1, \dots, 1, c, 1, \dots, 1) \), with \( c \) in position \( i \), obtained by \( R_i \to cR_i \) with \( c \neq 0 \);
3. \( \I_m + c\E_{ij} \), obtained by \( R_i \to R_i + cR_j \) with \( i \neq j \) and \( c \in F \): the identity with an extra \( c \) in entry \( (i, j) \).
:::

In words: start from \( \I_m \), do **one** operation, and record the result. The size \( m \) is the number of **rows** of the matrices we plan to operate on. Type 3 puts \( c \) in row \( i \), column \( j \): the row that changes is \( i \), and the row that gets copied is \( j \).

**Examples.** In \( M_3(F) \),
\[
\P_{13} = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix}, \qquad
\D_2(5) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 5 & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad
\I_3 - 3\E_{31} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ -3 & 0 & 1 \end{pmatrix}
\]
come from \( R_1 \leftrightarrow R_3 \), \( R_2 \to 5R_2 \) (over a field where \( 5 \neq 0 \)), and \( R_3 \to R_3 - 3R_1 \). The degenerate case is worth a look: \( \D_1(1) = \I_m \) is elementary, since "multiply row 1 by \( 1 \)" is a legal operation, and so is \( \I_m + 0\E_{12} \). The identity is an elementary matrix. For \( m = 1 \) the elementary matrices are exactly the \( 1 \times 1 \) matrices \( (c) \) with \( c \neq 0 \), since there are no two distinct rows to swap or combine.

**Non-example by minimal change.** Change \( c = 5 \) in \( \D_2(5) \) to \( c = 0 \). The matrix \( \diag(1, 0, 1) \) is still diagonal and still differs from \( \I_3 \) in one entry, but "multiply row 2 by \( 0 \)" is not an elementary row operation: the clause \( c \neq 0 \) fails. Likewise \( \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} \) is a rearrangement of the rows of \( \I_3 \), but every one of its rows has moved, and a single swap moves only two rows. So it is not elementary. It is, however, the **product** \( \P_{12}\P_{23} \) of two elementary matrices, as Exercise A1 at the end of this section checks.

The whole point of the definition is the next theorem. To perform a row operation on **any** matrix, multiply on the left by what that operation does to the identity.

::: {#thm-row-op-is-left-multiplication}
[Row operations are left multiplications]

Let \( \rho \) be an elementary row operation on matrices with \( m \) rows, and let \( \E = \rho(\I_m) \) be the corresponding elementary matrix. Then for **every** \( n \ge 1 \) and every \( \A \in M_{m \times n}(F) \),
\[
\rho(\A) = \E\A .
\]
:::

::: {.idea}
Each operation builds every new row as a combination of the old rows, with coefficients that do not depend on the matrix: for \( R_i \to R_i + cR_j \), new row \( i \) is \( 1 \cdot (\text{row } i) + c \cdot (\text{row } j) \), and every other row is copied. Feed in \( \I_m \), whose rows are the standard row vectors, and the coefficients appear as the entries of \( \E \). Then the row view of a product says \( \E\A \) forms exactly those combinations of the rows of \( \A \).
:::

::: {.proof}
Let \( \r_1, \dots, \r_m \) be the rows of \( \A \), and write \( \e_l\tp \) for the \( l \)-th row of \( \I_m \). By @def-elementary-row-operations, for each \( k \) there are scalars \( c_{k1}, \dots, c_{km} \), depending on \( \rho \) but **not** on \( \A \), such that row \( k \) of \( \rho(\A) \) is \( c_{k1}\r_1 + \dots + c_{km}\r_m \). Explicitly, every row that the operation does not touch has \( c_{kk} = 1 \) and all other \( c_{kl} = 0 \), and the touched rows are:

- for \( R_i \leftrightarrow R_j \): row \( i \) is \( \r_j \) and row \( j \) is \( \r_i \);
- for \( R_i \to cR_i \): row \( i \) is \( c\r_i \);
- for \( R_i \to R_i + cR_j \): row \( i \) is \( \r_i + c\r_j \).

Applying \( \rho \) to \( \I_m \), row \( k \) of \( \E \) is \( c_{k1}\e_1\tp + \dots + c_{km}\e_m\tp = \begin{pmatrix} c_{k1} & \cdots & c_{km} \end{pmatrix} \). So the \( (k, l) \)-entry of \( \E \) is \( c_{kl} \). By @thm-three-views-of-product (rows), row \( k \) of \( \E\A \) is \( (\text{row } k \text{ of } \E)\, \A \), and by @thm-matrix-times-vector-columns (rows version) this equals \( c_{k1}\r_1 + \dots + c_{km}\r_m \), which is row \( k \) of \( \rho(\A) \). Since every row agrees, \( \rho(\A) = \E\A \). This proves the theorem.
:::

So a sequence of operations \( \rho_1, \rho_2, \dots, \rho_k \), performed in that order, turns \( \A \) into
\[
\rho_k(\cdots \rho_2(\rho_1(\A))\cdots) = \E_k \cdots \E_2 \E_1 \A, \qquad \E_i = \rho_i(\I_m),
\]
by applying the theorem \( k \) times and using associativity. The whole of Gaussian elimination is a single matrix \( \E_k \cdots \E_1 \) standing on the left.

::: {.warning}
The **first** operation stands **rightmost**. Doing \( R_1 \leftrightarrow R_2 \) and then \( R_1 \to R_1 + R_2 \) on \( \I_2 \) gives \( (\I_2 + \E_{12})\P_{12} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} \), while the product in the other order is \( \P_{12}(\I_2 + \E_{12}) = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix} \). Also, multiplying by \( \E \) on the **right** performs a **column** operation: \( \A(\I_2 + \E_{12}) \) adds column 1 to column 2, and column operations change solution sets.
:::

::: {#exm-elementary-matrices}
[Three operations, three products]

Let \( \A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \\ 3 & 4 \end{pmatrix} \in M_{3 \times 2}(\nR) \). Compute \( \P_{13}\A \), \( \D_2(5)\A \) and \( (\I_3 - 3\E_{31})\A \), and check that each is the result of the corresponding row operation.
:::

::: {.solution}
By the row view, row \( k \) of \( \E\A \) is the combination of the rows of \( \A \) whose weights are row \( k \) of \( \E \).

- Rows of \( \P_{13} \) are \( \e_3\tp, \e_2\tp, \e_1\tp \), so \( \P_{13}\A = \begin{pmatrix} 3 & 4 \\ 0 & 1 \\ 1 & 2 \end{pmatrix} \): rows 1 and 3 are swapped.
- Row 2 of \( \D_2(5) \) is \( 5\e_2\tp \), so \( \D_2(5)\A = \begin{pmatrix} 1 & 2 \\ 0 & 5 \\ 3 & 4 \end{pmatrix} \): row 2 is multiplied by 5.
- Row 3 of \( \I_3 - 3\E_{31} \) is \( \begin{pmatrix} -3 & 0 & 1 \end{pmatrix} \), so row 3 of the product is \( -3(1, 2) + (3, 4) = (0, -2) \), and \( (\I_3 - 3\E_{31})\A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \\ 0 & -2 \end{pmatrix} \): this is \( R_3 \to R_3 - 3R_1 \).

In each case the product agrees with the operation, as @thm-row-op-is-left-multiplication predicts.
:::

::: {.check}
Which \( 3 \times 3 \) elementary matrix performs \( R_2 \to R_2 + 4R_3 \)? Which operation undoes it, and what is its matrix?
:::

::: {.solution}
Apply the operation to \( \I_3 \): row 2 becomes \( \e_2\tp + 4\e_3\tp \), so the matrix is \( \I_3 + 4\E_{23} \), with \( 4 \) in entry \( (2, 3) \). The operation \( R_2 \to R_2 - 4R_3 \) undoes it, since row 3 is unchanged by both; its matrix is \( \I_3 - 4\E_{23} \).
:::

Every row operation can be undone by another row operation, and the matching statement for matrices is:

::: {#thm-elementary-invertible}
[Elementary matrices are invertible]

Every elementary matrix is invertible, and its inverse is an elementary matrix of the same kind:
\[
\P_{ij}^{-1} = \P_{ij}, \qquad \D_i(c)^{-1} = \D_i(c^{-1}), \qquad (\I_m + c\E_{ij})^{-1} = \I_m - c\E_{ij} \quad (i \neq j).
\]
:::

::: {.proof}
Let \( \E = \rho(\I_m) \), and let \( \rho' \) be the operation on the same line of the display: \( \rho' = \rho \) for a swap, \( R_i \to c^{-1}R_i \) for \( R_i \to cR_i \) (legal, since \( c \neq 0 \) gives \( c^{-1} \neq 0 \)), and \( R_i \to R_i - cR_j \) for \( R_i \to R_i + cR_j \). In each case \( \rho'(\rho(\A)) = \A \) and \( \rho(\rho'(\A)) = \A \) for every \( \A \), as in @thm-row-ops-preserve-solutions (a): swapping twice restores the order; scaling by \( c \) and \( c^{-1} \) multiplies row \( i \) by \( cc^{-1} = 1 \); and adding \( c\r_j \) and then \( -c\r_j \) to row \( i \) restores row \( i \), because \( i \neq j \) means row \( j \) is not changed in between. Let \( \E' = \rho'(\I_m) \). By @thm-row-op-is-left-multiplication,
\[
\E'\E = \rho'(\E) = \rho'(\rho(\I_m)) = \I_m \quad \text{and} \quad \E\E' = \rho(\E') = \rho(\rho'(\I_m)) = \I_m .
\]
Hence \( \E \) is invertible with \( \E^{-1} = \E' \), which is the matrix in the display. This proves the theorem.
:::

The hypothesis \( i \neq j \) did real work: "add \( c \) times row \( i \) to row \( i \)" is scaling by \( 1 + c \), which destroys row \( i \) when \( c = -1 \) and cannot be undone. That is why @def-elementary-row-operations excludes it.

## The invertible matrix theorem

Chapter 0 defined an invertible matrix by the existence of a two-sided inverse, and gave only one practical test, \( ad - bc \neq 0 \), for \( 2 \times 2 \) matrices (@thm-two-by-two-inverse). For larger matrices, searching for \( \B \) with \( \A\B = \B\A = \I_n \) directly is hopeless. What we want is a list of conditions, each of which we can check by a method we already have, that are all equivalent to invertibility. Then we may test whichever is cheapest.

We need one small fact about square matrices in reduced form.

::: {#lem-square-rref-identity-or-zero-row}
[Square reduced matrices]

Let \( \R \in M_n(F) \) be in reduced row echelon form. Then either \( \R = \I_n \), or the last row of \( \R \) is zero.
:::

::: {.proof}
Suppose the last row of \( \R \) is not zero. Since zero rows of a matrix in echelon form come after all non-zero rows (@def-row-echelon-form), no row of \( \R \) is zero, so each of the \( n \) rows has a pivot. Let the pivot of row \( k \) be in column \( c_k \). Pivots move strictly to the right as we go down, so \( 1 \le c_1 < c_2 < \dots < c_n \le n \). A strictly increasing list of \( n \) integers in \( \{1, \dots, n\} \) must be \( 1, 2, \dots, n \), so \( c_k = k \). By @def-reduced-row-echelon-form, each pivot equals \( 1 \) and is the only non-zero entry of its column, so column \( k \) of \( \R \) is \( \e_k \) for every \( k \). Hence \( \R = \I_n \).
:::

Here is the theorem. It collects, for a square matrix, facts about solving systems, about row reduction, and about the columns as vectors in the sense of Chapter 1.

::: {#thm-invertible-tfae}
[Invertible Matrix Theorem]

Let \( \A \in M_n(F) \), with columns \( \a_1, \dots, \a_n \in F^n \). The following are equivalent.

::: {.enumerate options="label=(\alph*)"}
1. \( \A \) is invertible.
2. The homogeneous system \( \A\x = \0 \) has only the trivial solution \( \x = \0 \).
3. The reduced row echelon form of \( \A \) is \( \I_n \).
4. \( \A \) is a product of elementary matrices.
5. For **every** \( \b \in F^n \), the system \( \A\x = \b \) has a solution.
6. The columns \( (\a_1, \dots, \a_n) \) are linearly independent.
7. The columns \( (\a_1, \dots, \a_n) \) span \( F^n \).
8. The columns \( (\a_1, \dots, \a_n) \) form a basis of \( F^n \).
:::
:::

::: {.idea}
Eight conditions would need 56 implications if proved pairwise; a cycle through them needs far fewer. The plan:

① the core cycle (a) \( \Rightarrow \) (b) \( \Rightarrow \) (c) \( \Rightarrow \) (d) \( \Rightarrow \) (a), where each arrow uses one earlier tool (cancel by \( \A^{-1} \); row reduction; elementary matrices; products of invertible matrices);

② (b) \( \Leftrightarrow \) (f), which is the column view \( \A\x = x_1\a_1 + \dots + x_n\a_n \);

③ (f) \( \Leftrightarrow \) (h) \( \Leftrightarrow \) (g), which is "count instead of check" in the \( n \)-dimensional space \( F^n \);

④ (g) \( \Leftrightarrow \) (e), which is "consistent means \( \b \) is in the column span".

The only arrow that needs a new argument is (b) \( \Rightarrow \) (c); the others quote a result we already have. An RREF that is not \( \I_n \) has a zero row, so it really has fewer equations than unknowns, and such a homogeneous system has a non-trivial solution.
:::

::: {.proof}
**(a) \( \Rightarrow \) (b).** Suppose \( \A \) is invertible and \( \A\x = \0 \). Multiplying on the left by \( \A^{-1} \) and using @thm-matrix-multiplication-properties, \( \x = (\A^{-1}\A)\x = \A^{-1}(\A\x) = \A^{-1}\0 = \0 \).

**(b) \( \Rightarrow \) (c).** Suppose (b) holds. By @thm-rref-exists, \( \A \) is row equivalent to a matrix \( \R \) in reduced row echelon form, and \( \R \) is the RREF of \( \A \) by @thm-rref-unique. By @lem-row-equivalent-same-null-space, \( \R\x = \0 \) has the same solutions as \( \A\x = \0 \), so it too has only the trivial solution. Suppose, for a contradiction, that \( \R \neq \I_n \). By @lem-square-rref-identity-or-zero-row, the last row of \( \R \) is zero. If \( n = 1 \), then \( \R = (0) \) and \( \x = (1) \) is a non-trivial solution. If \( n \ge 2 \), the last equation of \( \R\x = \0 \) reads \( 0 = 0 \), so \( \R\x = \0 \) has the same solutions as the homogeneous system \( \R'\x = \0 \) formed by the first \( n - 1 \) rows. That system has \( n - 1 \) equations in \( n > n - 1 \) unknowns, so by @cor-more-unknowns-than-equations it has a non-trivial solution. Either way we contradict (b). Hence \( \R = \I_n \).

**(c) \( \Rightarrow \) (d).** Suppose the RREF of \( \A \) is \( \I_n \). By @def-row-equivalent there are row operations \( \rho_1, \dots, \rho_k \) taking \( \A \) to \( \I_n \). If \( k = 0 \), then \( \A = \I_n = \D_1(1) \) is elementary. Otherwise, with \( \E_i = \rho_i(\I_n) \), @thm-row-op-is-left-multiplication gives \( \E_k \cdots \E_1 \A = \I_n \). Each \( \E_i \) is invertible by @thm-elementary-invertible, so multiplying on the left by \( \E_k^{-1} \), then \( \E_{k-1}^{-1} \), and so on, gives
\[
\A = \E_1^{-1} \E_2^{-1} \cdots \E_k^{-1},
\]
and each \( \E_i^{-1} \) is elementary by @thm-elementary-invertible.

**(d) \( \Rightarrow \) (a).** Suppose \( \A = \E_1 \cdots \E_k \) with each \( \E_i \) elementary and \( k \ge 1 \). Each \( \E_i \) is invertible by @thm-elementary-invertible, and a product of two invertible matrices is invertible by @thm-inverse-matrix-properties (part 3). By induction on \( k \), \( \A \) is invertible.

So far (a), (b), (c), (d) are equivalent.

**(b) \( \Leftrightarrow \) (f).** By @thm-matrix-times-vector-columns, \( \A\x = x_1\a_1 + \dots + x_n\a_n \). So "\( \A\x = \0 \) only for \( \x = \0 \)" says exactly that \( x_1\a_1 + \dots + x_n\a_n = \0 \) forces \( x_1 = \dots = x_n = 0 \), which is @def-linear-independence for the columns.

**(f) \( \Leftrightarrow \) (h) \( \Leftrightarrow \) (g).** The columns form a list of exactly \( n \) vectors in \( F^n \), and \( \dim F^n = n \) (@exm-dimensions). By @thm-right-size-basis, such a list is a basis if it is linearly independent, and also if it spans. Conversely a basis is independent and spanning by @def-basis. Hence (f) \( \Rightarrow \) (h) \( \Rightarrow \) (g) \( \Rightarrow \) (h) \( \Rightarrow \) (f).

**(g) \( \Leftrightarrow \) (e).** By @thm-consistent-iff-column-span, \( \A\x = \b \) has a solution if and only if \( \b \in \Span(\a_1, \dots, \a_n) \). So (e) says every \( \b \in F^n \) lies in this span, that is, \( F^n \subseteq \Span(\a_1, \dots, \a_n) \). The reverse inclusion always holds, so (e) is equivalent to (g).

Combining the four parts, all eight conditions are equivalent. This proves the theorem.
:::

In practice the theorem is a menu. To show a matrix **is** invertible, pick the most convenient item, very often (b): take a solution of \( \A\x = \0 \) and show it is \( \0 \). To show a matrix is **not** invertible, exhibit one non-zero solution of \( \A\x = \0 \), or one linear relation among the columns. The list grows in both directions. Chapter 2 has already given the operator form of it, in terms of kernels and images (@thm-invertible-operator-tfae), and later chapters add determinants in Chapter 7, eigenvalues in Chapter 9, and positive definiteness and singular values in Chapter 13.

::: {.check}
Is \( \A = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 1 & 3 & 4 \end{pmatrix} \in M_3(\nR) \) invertible? Use whichever item of @thm-invertible-tfae is quickest.
:::

::: {.solution}
No. The third column is the sum of the first two: \( (1, 0, 1) + (2, 1, 3) = (3, 1, 4) \). So \( \a_1 + \a_2 - \a_3 = \0 \) is a linear relation with coefficients not all zero, item (f) fails, and hence (a) fails. Equivalently, \( \x = (1, 1, -1) \) is a non-trivial solution of \( \A\x = \0 \).
:::

::: {.warning}
The theorem is about **square** matrices. For \( \A = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \end{pmatrix} \in M_{2 \times 3}(\nR) \), the columns span \( \nR^2 \) (the first two are \( \e_1, \e_2 \)), so (g) holds, but \( \x = (1, 1, -1) \) solves \( \A\x = \0 \), so (b) fails. The proof of (f) \( \Leftrightarrow \) (g) used that the number of columns equals \( \dim F^n \), and that is exactly what breaks.
:::

## One-sided inverses are two-sided

Chapter 0 left a gap on purpose. The definition of invertibility (@def-invertible-matrix) asks for **both** \( \A\B = \I_n \) and \( \B\A = \I_n \). Chapter 0 then stated that, for square matrices, the first equation already implies the second, but that nothing there could prove it: the entries of \( \A\B \) and \( \B\A \) are different sums. Now we can prove it, and the proof uses the menu above instead of entries.

::: {#thm-one-sided-inverse}
[One-sided inverses of square matrices]

Let \( \A, \B \in M_n(F) \). If \( \A\B = \I_n \), then \( \B\A = \I_n \). Hence \( \A \) and \( \B \) are both invertible, \( \B = \A^{-1} \) and \( \A = \B^{-1} \).
:::

::: {.idea}
We cannot touch \( \B\A \) directly, so we aim at invertibility of one factor instead. Which one? From \( \A\B = \I_n \), a vector killed by \( \B \) is killed by \( \A\B = \I_n \), so it is \( \0 \). That is item (b) for \( \B \). Once \( \B^{-1} \) exists, we may cancel it: \( \A = (\A\B)\B^{-1} = \B^{-1} \).
:::

::: {.proof}
Suppose \( \A\B = \I_n \), and let \( \x \in F^n \) with \( \B\x = \0 \). Then, by @thm-matrix-multiplication-properties,
\[
\x = \I_n\x = (\A\B)\x = \A(\B\x) = \A\0 = \0 .
\]
So \( \B\x = \0 \) has only the trivial solution, and \( \B \) is invertible by @thm-invertible-tfae ((b) \( \Rightarrow \) (a)). Multiplying \( \A\B = \I_n \) on the right by \( \B^{-1} \) and using associativity,
\[
\A = \A(\B\B^{-1}) = (\A\B)\B^{-1} = \I_n \B^{-1} = \B^{-1} .
\]
Therefore \( \B\A = \B\B^{-1} = \I_n \). Since \( \A = \B^{-1} \) is invertible with inverse \( \B \) by @thm-inverse-matrix-properties (part 2), we get \( \A^{-1} = \B \). This proves the theorem.
:::

By symmetry, \( \B\A = \I_n \) also implies \( \A\B = \I_n \): apply the theorem with the roles of \( \A \) and \( \B \) swapped. So from now on, **to verify that \( \B \) is the inverse of a square matrix \( \A \), one product suffices**. We also get a useful consequence of the same kind: if \( \A, \B \in M_n(F) \) and \( \A\B \) is invertible, then \( \A \) and \( \B \) are invertible (Exercise B3 at the end of this section).

::: {.warning}
For **non-square** matrices a one-sided inverse need not be two-sided. Let
\[
\A = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}, \qquad \B = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{pmatrix}.
\]
Then \( \A\B = \I_2 \), but \( \B\A = \diag(1, 1, 0) \neq \I_3 \). In fact no \( \C \in M_{3 \times 2}(F) \) has \( \C\A = \I_3 \): \( \A\e_3 = \0 \), so \( \C\A\e_3 = \0 \neq \e_3 = \I_3\e_3 \). The proof above breaks because \( \B\x = \0 \Rightarrow \x = \0 \) no longer gives invertibility: \( \B \) is not square, so @thm-invertible-tfae does not apply.
:::

## Computing the inverse

@thm-invertible-tfae (c) says \( \A \) is invertible exactly when it row reduces to \( \I_n \). The proof of (c) \( \Rightarrow \) (d) even produced a matrix: if \( \E_k \cdots \E_1 \A = \I_n \), then \( \E_k \cdots \E_1 \) is a left inverse, hence **the** inverse by @thm-one-sided-inverse. We do not want to multiply out the \( \E_i \) by hand. The trick is to let the operations act on \( \I_n \) at the same time as on \( \A \): since \( \E_k \cdots \E_1 \I_n = \E_k \cdots \E_1 \), the operations that turn \( \A \) into \( \I_n \) turn \( \I_n \) into \( \A^{-1} \). We write \( [\A \mid \I_n] \) for the \( n \times 2n \) matrix whose first \( n \) columns are those of \( \A \) and whose last \( n \) columns are those of \( \I_n \).

::: {.algorithm}
**Input:** \( \A \in M_n(F) \).

1. Form the \( n \times 2n \) matrix \( [\A \mid \I_n] \).
2. Row reduce it to reduced row echelon form \( [\R \mid \C] \), with \( \R, \C \in M_n(F) \).
3. If \( \R = \I_n \), output \( \A^{-1} = \C \). Otherwise, output "\( \A \) is not invertible".

In practice, stop as soon as a zero row appears in the left half: \( \A \) is then not invertible (see the remark after the theorem).
:::

::: {#thm-inverse-by-row-reduction}
[Inverse by row reduction]

Let \( \A \in M_n(F) \), and let \( [\R \mid \C] \) be the reduced row echelon form of \( [\A \mid \I_n] \), with \( \R, \C \in M_n(F) \). Then \( \R \) is the reduced row echelon form of \( \A \). Consequently, \( \A \) is invertible if and only if \( \R = \I_n \), and in that case \( \A^{-1} = \C \).
:::

::: {.idea}
Two things need checking. First, the operations act on the two halves independently, so the left half is transformed exactly as \( \A \) alone would be. Second, the left half of a reduced matrix is itself reduced, so it really is the RREF of \( \A \). The first is the column view of a product; the second is a small check on the staircase shape. After that, \( \R = \E\A \) and \( \C = \E\I_n = \E \), and @thm-one-sided-inverse finishes.
:::

::: {.proof}
Let \( \rho_1, \dots, \rho_k \) be row operations taking \( [\A \mid \I_n] \) to \( [\R \mid \C] \), and put \( \E = \E_k \cdots \E_1 \) with \( \E_i = \rho_i(\I_n) \) (and \( \E = \I_n \) if \( k = 0 \)). By @thm-row-op-is-left-multiplication, \( [\R \mid \C] = \E\,[\A \mid \I_n] \). By @thm-three-views-of-product (columns), each column of \( \E\,[\A \mid \I_n] \) is \( \E \) times the corresponding column, so
\[
\R = \E\A \qquad \text{and} \qquad \C = \E\I_n = \E .
\]

::: {.claim}
\( \R \) is in reduced row echelon form.
:::

::: {.proof}
If row \( k \) of \( \R \) is non-zero, its first non-zero entry is also the first non-zero entry of row \( k \) of \( [\R \mid \C] \), so the pivots of the non-zero rows of \( \R \) are pivots of \( [\R \mid \C] \), in the same positions. Suppose row \( k \) of \( \R \) is zero but some later row \( l > k \) of \( \R \) is non-zero. Row \( k \) of \( [\R \mid \C] \) cannot be zero, since zero rows of \( [\R \mid \C] \) come after its non-zero rows and row \( l \) is non-zero. So its pivot lies in a column \( > n \), while the pivot of row \( l \) lies in a column \( \le n \), to the left: this contradicts the staircase condition of @def-row-echelon-form. Hence the zero rows of \( \R \) come last, the pivots of \( \R \) move strictly right, and each pivot of \( \R \) is \( 1 \) and the only non-zero entry in its column, because this holds in \( [\R \mid \C] \). So \( \R \) satisfies @def-reduced-row-echelon-form.
:::

Now \( \R = \E_k \cdots \E_1 \A \) is obtained from \( \A \) by the operations \( \rho_1, \dots, \rho_k \) (@thm-row-op-is-left-multiplication), so \( \A \) is row equivalent to \( \R \), and \( \R \) is in reduced form. By @thm-rref-unique, \( \R \) is the RREF of \( \A \). By @thm-invertible-tfae ((a) \( \Leftrightarrow \) (c)), \( \A \) is invertible if and only if \( \R = \I_n \). If \( \R = \I_n \), then \( \E\A = \I_n \), and @thm-one-sided-inverse gives \( \A^{-1} = \E = \C \). This proves the theorem.
:::

::: {.remark}
The early stop is justified the same way. If, after some operations, \( [\A \mid \I_n] \) has become \( [\A' \mid \E'] \) with a zero row in \( \A' \), then, exactly as in the proof, \( \E' \) is the product of the elementary matrices of the operations used so far and \( \A' = \E'\A \). So \( \E' \) is invertible by @thm-elementary-invertible and @thm-inverse-matrix-properties (part 3). A matrix with a zero row \( k \) is not invertible, since row \( k \) of \( \A'\X \) is zero for every \( \X \), so \( \A'\X \neq \I_n \). If \( \A \) were invertible, \( \A' = \E'\A \) would be invertible by @thm-inverse-matrix-properties (part 3). Hence \( \A \) is not invertible.
:::

::: {#exm-inverse-3x3}
[A \( 3 \times 3 \) inverse]

Find the inverse of \( \A = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 5 & 3 \\ 1 & 3 & 3 \end{pmatrix} \in M_3(\nR) \), or show that it does not exist.
:::

::: {.solution}
Row reduce \( [\A \mid \I_3] \), naming each operation.
\[
\begin{aligned}
\left[\begin{array}{ccc|ccc} 1 & 2 & 1 & 1 & 0 & 0 \\ 2 & 5 & 3 & 0 & 1 & 0 \\ 1 & 3 & 3 & 0 & 0 & 1 \end{array}\right]
&\xrightarrow[R_3 \to R_3 - R_1]{R_2 \to R_2 - 2R_1}
\left[\begin{array}{ccc|ccc} 1 & 2 & 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & -2 & 1 & 0 \\ 0 & 1 & 2 & -1 & 0 & 1 \end{array}\right] \\
&\xrightarrow{R_3 \to R_3 - R_2}
\left[\begin{array}{ccc|ccc} 1 & 2 & 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & -2 & 1 & 0 \\ 0 & 0 & 1 & 1 & -1 & 1 \end{array}\right]
\end{aligned}
\]
The left half now has three pivots, so no zero row will appear. Clear above the pivots, from the bottom up:
\[
\xrightarrow[R_1 \to R_1 - R_3]{R_2 \to R_2 - R_3}
\left[\begin{array}{ccc|ccc} 1 & 2 & 0 & 0 & 1 & -1 \\ 0 & 1 & 0 & -3 & 2 & -1 \\ 0 & 0 & 1 & 1 & -1 & 1 \end{array}\right]
\xrightarrow{R_1 \to R_1 - 2R_2}
\left[\begin{array}{ccc|ccc} 1 & 0 & 0 & 6 & -3 & 1 \\ 0 & 1 & 0 & -3 & 2 & -1 \\ 0 & 0 & 1 & 1 & -1 & 1 \end{array}\right].
\]
The left half is \( \I_3 \), so by @thm-inverse-by-row-reduction \( \A \) is invertible and
\[
\A^{-1} = \begin{pmatrix} 6 & -3 & 1 \\ -3 & 2 & -1 \\ 1 & -1 & 1 \end{pmatrix}.
\]
Check one product: row 1 of \( \A \) times the columns of \( \A^{-1} \) gives \( 6 - 6 + 1 = 1 \), \( -3 + 4 - 1 = 0 \), \( 1 - 2 + 1 = 0 \); rows 2 and 3 give \( (0, 1, 0) \) and \( (0, 0, 1) \) in the same way. So \( \A\A^{-1} = \I_3 \), and by @thm-one-sided-inverse this single product is enough.
:::

::: {#exm-inverse-fails-zero-row}
[When the algorithm stops]

Decide whether \( \A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 5 & 7 \\ 1 & 3 & 4 \end{pmatrix} \in M_3(\nR) \) is invertible.
:::

::: {.solution}
Row reduce \( [\A \mid \I_3] \):
\[
\begin{aligned}
\left[\begin{array}{ccc|ccc} 1 & 2 & 3 & 1 & 0 & 0 \\ 2 & 5 & 7 & 0 & 1 & 0 \\ 1 & 3 & 4 & 0 & 0 & 1 \end{array}\right]
&\xrightarrow[R_3 \to R_3 - R_1]{R_2 \to R_2 - 2R_1}
\left[\begin{array}{ccc|ccc} 1 & 2 & 3 & 1 & 0 & 0 \\ 0 & 1 & 1 & -2 & 1 & 0 \\ 0 & 1 & 1 & -1 & 0 & 1 \end{array}\right] \\
&\xrightarrow{R_3 \to R_3 - R_2}
\left[\begin{array}{ccc|ccc} 1 & 2 & 3 & 1 & 0 & 0 \\ 0 & 1 & 1 & -2 & 1 & 0 \\ 0 & 0 & 0 & 1 & -1 & 1 \end{array}\right].
\end{aligned}
\]
A zero row has appeared in the left half, so by the remark after @thm-inverse-by-row-reduction, \( \A \) is not invertible. The right half of that row is not wasted: it records the combination of rows that produced zero. Row 3 of the left half is \( 1 \cdot (\text{row } 1) - 1 \cdot (\text{row } 2) + 1 \cdot (\text{row } 3) \) of \( \A \), and indeed \( (1, 2, 3) - (2, 5, 7) + (1, 3, 4) = (0, 0, 0) \).
:::

Finally, the method writes an invertible matrix as a product of elementary matrices, as in @thm-invertible-tfae (d).

::: {#exm-product-of-elementary-matrices}
[Factoring into elementary matrices]

Write \( \A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix} \in M_2(\nR) \) as a product of elementary matrices, and read off \( \A^{-1} \).
:::

::: {.solution}
Reduce \( \A \) to \( \I_2 \), keeping integers:
\[
\begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}
\xrightarrow{R_2 \to R_2 - 2R_1}
\begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}
\xrightarrow{R_1 \to R_1 - R_2}
\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}
\xrightarrow{R_2 \to R_2 - R_1}
\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}.
\]
The elementary matrices of these operations are \( \E_1 = \I_2 - 2\E_{21} \), \( \E_2 = \I_2 - \E_{12} \), \( \E_3 = \I_2 - \E_{21} \), and by @thm-row-op-is-left-multiplication, \( \E_3\E_2\E_1\A = \I_2 \). Multiplying on the left by \( \E_3^{-1} \), then \( \E_2^{-1} \), then \( \E_1^{-1} \), and using @thm-elementary-invertible,
\[
\A = \E_1^{-1}\E_2^{-1}\E_3^{-1} = \begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}.
\]
Multiplying out confirms it: the last two factors give \( \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \), and then the first factor adds twice row 1 to row 2, giving \( \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix} \). Also \( \E_3\E_2\E_1 \) is a left inverse of \( \A \), hence \( \A^{-1} \) by @thm-one-sided-inverse:
\[
\A^{-1} = \E_3\E_2\E_1 = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix},
\]
which agrees with @thm-two-by-two-inverse, since \( ad - bc = 1 \). The factorization is not unique: a different sequence of operations gives different factors.
:::

## Permutation matrices

A row swap is one elementary matrix. Doing several of them in a row is not, but the product is still a matrix of a single recognizable kind, and it is worth naming here because it turns up far beyond this chapter: it is how a relabeling of coordinates becomes a matrix.

::: {#def-permutation-matrix}
[Permutation matrix]

Let \( \sigma \in S_n \) be a permutation of \( \{1, \dots, n\} \). The **permutation matrix** of \( \sigma \) is
\[
\P_\sigma = \begin{pmatrix} \e_{\sigma(1)} & \e_{\sigma(2)} & \cdots & \e_{\sigma(n)} \end{pmatrix} \in M_n(F),
\]
the matrix whose \( j \)-th column is \( \e_{\sigma(j)} \). A matrix is a **permutation matrix** if it equals \( \P_\sigma \) for some \( \sigma \in S_n \).
:::

Equivalently, a permutation matrix has exactly one \( 1 \) in each row and in each column, and zeros elsewhere. The identity is \( \P_{\id} \), and \( \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) is \( \P_\tau \) for the transposition \( \tau = (1\ 2) \), which is also the elementary matrix \( \P_{12} \). By contrast \( \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) is **not** a permutation matrix: each column is still non-zero, but its first row contains two \( 1 \)'s, and its second column \( (1, 1) \) is not a standard basis vector.

::: {#lem-permutation-matrices}
[Permutation matrices]

Let \( \sigma, \tau \in S_n \).

::: {.enumerate options="label=(\alph*)"}
1. \( \P_\sigma \P_\tau = \P_{\sigma \circ \tau} \). In particular a product of permutation matrices is a permutation matrix.
2. \( \P_\sigma \) is invertible and \( \P_\sigma^{-1} = \P_\sigma\tp \).
3. If \( \tau = (r\ s) \) is a transposition, then \( \P_\tau \) is the elementary matrix \( \P_{rs} \) that swaps rows \( r \) and \( s \), and \( \P_\tau^2 = \I \).
:::
:::

::: {.proof}
(a) By @thm-matrix-times-vector-columns, \( \P_\tau \e_j = \e_{\tau(j)} \) and so \( \P_\sigma \P_\tau \e_j = \P_\sigma \e_{\tau(j)} = \e_{\sigma(\tau(j))} \). So the \( j \)-th column of \( \P_\sigma \P_\tau \) is \( \e_{(\sigma \circ \tau)(j)} \), for every \( j \), which is the claim.

(b) By @thm-three-views-of-product, \( (\P_\sigma\tp \P_\sigma)_{ij} = \e_{\sigma(i)}\tp \e_{\sigma(j)} \), which is \( 1 \) if \( \sigma(i) = \sigma(j) \) and \( 0 \) otherwise. Since \( \sigma \) is injective, \( \sigma(i) = \sigma(j) \) exactly when \( i = j \). Hence \( \P_\sigma\tp \P_\sigma = \I \), and by @thm-one-sided-inverse, \( \P_\sigma \) is invertible with inverse \( \P_\sigma\tp \).

(c) Swapping rows \( r \) and \( s \) of \( \I \) produces a matrix whose column \( r \) is \( \e_s \), whose column \( s \) is \( \e_r \), and whose other columns \( j \) are \( \e_j \). These are the columns \( \e_{\tau(j)} \), so the swap matrix is \( \P_\tau \). Since \( \tau \circ \tau = \id \), part (a) gives \( \P_\tau^2 = \P_{\id} = \I \). This proves the lemma.
:::

By (c) and @thm-row-op-is-left-multiplication, \( \P_\tau \A \) is \( \A \) with rows \( r \) and \( s \) swapped, and by (a) every permutation matrix is a product of such swaps applied in turn, since for \( n \ge 2 \) every permutation is a product of transpositions (@thm-transpositions-generate). So \( \P_\sigma\A \) is always \( \A \) with its rows rearranged.

## Row equivalence, revisited

Two descriptions of "row equivalent" are now on the table. @exm-row-equivalence of Chapter 0 said \( \B = \E\A \) for some invertible \( \E \). @def-row-equivalent says \( \B \) is reachable from \( \A \) by finitely many row operations. Chapter 0 promised that they agree, and now it is one line each way.

::: {#thm-row-equivalent-iff-invertible-multiple}
[Row equivalence is left multiplication by an invertible matrix]

Let \( \A, \B \in M_{m \times n}(F) \). Then \( \A \) is row equivalent to \( \B \) (that is, \( \B \) can be reached from \( \A \) by row operations) if and only if \( \B = \E\A \) for some invertible \( \E \in M_m(F) \).
:::

::: {.proof}
\( (\Rightarrow) \) Suppose row operations \( \rho_1, \dots, \rho_k \) take \( \A \) to \( \B \). By @thm-row-op-is-left-multiplication, \( \B = \E_k \cdots \E_1 \A \) with \( \E_i = \rho_i(\I_m) \), and \( \E = \E_k \cdots \E_1 \) is invertible by @thm-elementary-invertible and @thm-inverse-matrix-properties (part 3). (If \( k = 0 \), take \( \E = \I_m \).)

\( (\Leftarrow) \) Suppose \( \B = \E\A \) with \( \E \) invertible. By @thm-invertible-tfae ((a) \( \Rightarrow \) (d)), \( \E = \E_k \cdots \E_1 \) for some elementary matrices \( \E_i \). Let \( \rho_i \) be the operation with \( \rho_i(\I_m) = \E_i \). By @thm-row-op-is-left-multiplication, performing \( \rho_1 \), then \( \rho_2 \), …, then \( \rho_k \) on \( \A \) produces \( \E_k \cdots \E_1 \A = \B \). Hence \( \A \) is row equivalent to \( \B \).
:::

So the equivalence relation of @exm-row-equivalence is the one Gaussian elimination moves along, and "two matrices have the same RREF" is the same as "each is an invertible matrix times the other". In the next section this form, \( \B = \E\A \), is what makes row spaces and ranks easy to compare.

## Exercises

### A. Check your understanding

::: {#exr-elementary-matrices-and-inverses-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define an elementary matrix, and write down the \( 3 \times 3 \) elementary matrix that performs \( R_3 \to R_3 + 7R_1 \).
2. State four of the conditions in @thm-invertible-tfae.
3. True or false: the product of two elementary matrices is always an elementary matrix. Justify your answer.
4. True or false: if \( \A \in M_{2 \times 3}(F) \), \( \B \in M_{3 \times 2}(F) \) and \( \A\B = \I_2 \), then \( \B\A = \I_3 \). Justify your answer.
5. True or false: if \( \A \in M_n(F) \) and \( \A\x = \e_j \) has a solution for each \( j = 1, \dots, n \), then \( \A \) is invertible. Justify your answer.
6. Describe the method for computing the inverse of a square matrix, and how it detects a matrix that is not invertible.
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. An elementary matrix in \( M_m(F) \) is one obtained from \( \I_m \) by exactly one elementary row operation (@def-elementary-matrix). Applying \( R_3 \to R_3 + 7R_1 \) to \( \I_3 \) gives \( \I_3 + 7\E_{31} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 7 & 0 & 1 \end{pmatrix} \).
2. For \( \A \in M_n(F) \), each of the following is equivalent to \( \A \) being invertible: \( \A\x = \0 \) has only the trivial solution; the RREF of \( \A \) is \( \I_n \); \( \A \) is a product of elementary matrices; the columns of \( \A \) form a basis of \( F^n \).
3. False. A single row operation changes at most two rows of \( \I_3 \) (a swap changes two, a scaling or an addition changes one), so every elementary \( 3 \times 3 \) matrix has at least one row equal to the corresponding row of \( \I_3 \). But \( \P_{12}\P_{23} = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} \) (by the row view, its rows are rows 2, 1, 3 of \( \P_{23} \)) differs from \( \I_3 \) in every row. Hence it is a product of two elementary matrices that is not elementary.
4. False. With \( \A = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} \) and \( \B = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{pmatrix} \), \( \A\B = \I_2 \) but \( \B\A = \diag(1, 1, 0) \neq \I_3 \). @thm-one-sided-inverse needs square matrices.
5. True. Let \( \x_j \) solve \( \A\x_j = \e_j \), and let \( \B \) have columns \( \x_1, \dots, \x_n \). By @thm-three-views-of-product, \( \A\B \) has columns \( \e_1, \dots, \e_n \), so \( \A\B = \I_n \), and \( \A \) is invertible by @thm-one-sided-inverse.
6. Row reduce \( [\A \mid \I_n] \) to reduced form \( [\R \mid \C] \). If \( \R = \I_n \), then \( \A^{-1} = \C \); if \( \R \neq \I_n \), in particular if a zero row appears in the left half at any stage, \( \A \) is not invertible (@thm-inverse-by-row-reduction).
:::
:::

### B. Practice

::: {#exr-elementary-matrices-and-inverses-b1}
[B1: Inverses by row reduction]

For each matrix, find the inverse or show that it is not invertible.

::: {.enumerate options="label=(\alph*)"}
1. \( \A = \begin{pmatrix} 1 & 0 & 2 \\ 2 & 1 & 3 \\ 4 & 1 & 8 \end{pmatrix} \in M_3(\nR) \).
2. \( \B = \begin{pmatrix} 1 & 2 & -1 \\ 0 & 1 & 1 \\ 2 & 5 & -1 \end{pmatrix} \in M_3(\nR) \).
3. \( \C = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix} \in M_3(\nF_2) \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Row reduce \( [\A \mid \I_3] \):
\[
\begin{aligned}
\left[\begin{array}{ccc|ccc} 1 & 0 & 2 & 1 & 0 & 0 \\ 2 & 1 & 3 & 0 & 1 & 0 \\ 4 & 1 & 8 & 0 & 0 & 1 \end{array}\right]
&\xrightarrow[R_3 \to R_3 - 4R_1]{R_2 \to R_2 - 2R_1}
\left[\begin{array}{ccc|ccc} 1 & 0 & 2 & 1 & 0 & 0 \\ 0 & 1 & -1 & -2 & 1 & 0 \\ 0 & 1 & 0 & -4 & 0 & 1 \end{array}\right] \\
&\xrightarrow{R_3 \to R_3 - R_2}
\left[\begin{array}{ccc|ccc} 1 & 0 & 2 & 1 & 0 & 0 \\ 0 & 1 & -1 & -2 & 1 & 0 \\ 0 & 0 & 1 & -2 & -1 & 1 \end{array}\right]
\end{aligned}
\]
\[
\xrightarrow[R_1 \to R_1 - 2R_3]{R_2 \to R_2 + R_3}
\left[\begin{array}{ccc|ccc} 1 & 0 & 0 & 5 & 2 & -2 \\ 0 & 1 & 0 & -4 & 0 & 1 \\ 0 & 0 & 1 & -2 & -1 & 1 \end{array}\right].
\]
The left half is \( \I_3 \), so by @thm-inverse-by-row-reduction, \( \A^{-1} = \begin{pmatrix} 5 & 2 & -2 \\ -4 & 0 & 1 \\ -2 & -1 & 1 \end{pmatrix} \). Check: row 1 of \( \A \) against the columns of \( \A^{-1} \) gives \( 5 - 4 = 1 \), \( 2 - 2 = 0 \), \( -2 + 2 = 0 \), and rows 2 and 3 give \( (0, 1, 0) \) and \( (0, 0, 1) \), so \( \A\A^{-1} = \I_3 \), which suffices by @thm-one-sided-inverse.
2. Row reduce \( [\B \mid \I_3] \):
\[
\begin{aligned}
\left[\begin{array}{ccc|ccc} 1 & 2 & -1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 2 & 5 & -1 & 0 & 0 & 1 \end{array}\right]
&\xrightarrow{R_3 \to R_3 - 2R_1}
\left[\begin{array}{ccc|ccc} 1 & 2 & -1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 0 & 1 & 1 & -2 & 0 & 1 \end{array}\right] \\
&\xrightarrow{R_3 \to R_3 - R_2}
\left[\begin{array}{ccc|ccc} 1 & 2 & -1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 0 & 0 & 0 & -2 & -1 & 1 \end{array}\right].
\end{aligned}
\]
A zero row appears in the left half, so \( \B \) is not invertible (remark after @thm-inverse-by-row-reduction). The right half of that row says \( -2(\text{row } 1) - (\text{row } 2) + (\text{row } 3) = \0 \), that is, row 3 of \( \B \) is \( 2(\text{row } 1) + (\text{row } 2) \).
3. Over \( \nF_2 \) we have \( -1 = 1 \), so subtracting a row is adding it. Row reduce \( [\C \mid \I_3] \):
\[
\begin{aligned}
\left[\begin{array}{ccc|ccc} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 1 & 1 & 1 & 0 & 0 & 1 \end{array}\right]
&\xrightarrow{R_3 \to R_3 + R_1}
\left[\begin{array}{ccc|ccc} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 0 & 0 & 1 & 1 & 0 & 1 \end{array}\right] \\
&\xrightarrow{R_2 \to R_2 + R_3}
\left[\begin{array}{ccc|ccc} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 1 & 1 & 1 \\ 0 & 0 & 1 & 1 & 0 & 1 \end{array}\right] \\
&\xrightarrow{R_1 \to R_1 + R_2}
\left[\begin{array}{ccc|ccc} 1 & 0 & 0 & 0 & 1 & 1 \\ 0 & 1 & 0 & 1 & 1 & 1 \\ 0 & 0 & 1 & 1 & 0 & 1 \end{array}\right].
\end{aligned}
\]
Hence \( \C^{-1} = \begin{pmatrix} 0 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix} \). Check in \( \nF_2 \): row 1 of \( \C \) is \( (1, 1, 0) \), and against the columns of \( \C^{-1} \) it gives \( 0 + 1 = 1 \), \( 1 + 1 = 0 \), \( 1 + 1 = 0 \); rows 2 and 3 give \( (0, 1, 0) \) and \( (0, 0, 1) \) similarly.
:::
:::

::: {#exr-elementary-matrices-and-inverses-b2}
[B2: A product of elementary matrices]

Let \( \A = \begin{pmatrix} 1 & 3 \\ 2 & 5 \end{pmatrix} \in M_2(\nR) \).

::: {.enumerate options="label=(\alph*)"}
1. Write \( \A \) as a product of elementary matrices.
2. Hence write \( \A^{-1} \) as a product of elementary matrices, and compute it.
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Reduce \( \A \) to \( \I_2 \):
\[
\begin{pmatrix} 1 & 3 \\ 2 & 5 \end{pmatrix}
\xrightarrow{R_2 \to R_2 - 2R_1}
\begin{pmatrix} 1 & 3 \\ 0 & -1 \end{pmatrix}
\xrightarrow{R_2 \to -R_2}
\begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}
\xrightarrow{R_1 \to R_1 - 3R_2}
\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}.
\]
With \( \E_1 = \I_2 - 2\E_{21} \), \( \E_2 = \D_2(-1) \), \( \E_3 = \I_2 - 3\E_{12} \), @thm-row-op-is-left-multiplication gives \( \E_3\E_2\E_1\A = \I_2 \). Multiplying on the left by \( \E_3^{-1}, \E_2^{-1}, \E_1^{-1} \) in turn and using @thm-elementary-invertible,
\[
\A = \E_1^{-1}\E_2^{-1}\E_3^{-1} = \begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}.
\]
Check: the last two factors give \( \begin{pmatrix} 1 & 3 \\ 0 & -1 \end{pmatrix} \), and adding twice row 1 to row 2 gives \( \begin{pmatrix} 1 & 3 \\ 2 & 5 \end{pmatrix} \).
2. Since \( \E_3\E_2\E_1\A = \I_2 \), @thm-one-sided-inverse gives
\[
\A^{-1} = \E_3\E_2\E_1 = \begin{pmatrix} 1 & -3 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ -2 & 1 \end{pmatrix} = \begin{pmatrix} -5 & 3 \\ 2 & -1 \end{pmatrix}.
\]
(The last two factors give \( \begin{pmatrix} 1 & 0 \\ 2 & -1 \end{pmatrix} \), and \( R_1 \to R_1 - 3R_2 \) then gives the answer.) This agrees with @thm-two-by-two-inverse, since \( ad - bc = -1 \).
:::
:::

::: {#exr-elementary-matrices-and-inverses-b3}
[B3: Invertible products]

Let \( \A, \B \in M_n(F) \), and suppose \( \A\B \) is invertible. Prove that \( \A \) and \( \B \) are both invertible.
:::

::: {.solution}
Let \( \C = (\A\B)^{-1} \). Then \( \A(\B\C) = (\A\B)\C = \I_n \) by associativity, so \( \A \) has the right inverse \( \B\C \), and by @thm-one-sided-inverse \( \A \) is invertible. Similarly \( (\C\A)\B = \C(\A\B) = \I_n \), so \( \B \) has the left inverse \( \C\A \). By @thm-one-sided-inverse with the roles of the two matrices swapped (\( \C\A \) times \( \B \) is \( \I_n \)), \( \B \) is invertible. This proves the claim.
:::

### C. Going deeper

::: {#exr-elementary-matrices-and-inverses-c1}
[C1: Triangular matrices]

Let \( \U = (u_{ij}) \in M_n(F) \) be upper triangular (@def-upper-triangular).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \U \) is invertible if and only if \( u_{ii} \neq 0 \) for every \( i \).
2. Prove that if \( \U \) is invertible, then \( \U^{-1} \) is upper triangular.
:::

*Hint: for (a), use item (b) or item (f) of @thm-invertible-tfae; for (b), consider the systems \( \U\x = \e_k \).*
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. \( (\Leftarrow) \) Suppose every \( u_{ii} \neq 0 \), and let \( \U\x = \0 \). Row \( i \) of this system reads \( u_{ii}x_i + u_{i,i+1}x_{i+1} + \dots + u_{in}x_n = 0 \), since \( u_{ij} = 0 \) for \( j < i \). We show \( x_n = x_{n-1} = \dots = x_1 = 0 \) by downward induction. Row \( n \) is \( u_{nn}x_n = 0 \), and \( u_{nn} \neq 0 \), so \( x_n = 0 \). If \( x_{i+1} = \dots = x_n = 0 \), row \( i \) becomes \( u_{ii}x_i = 0 \), so \( x_i = 0 \) since \( u_{ii} \neq 0 \). Hence \( \x = \0 \), and \( \U \) is invertible by @thm-invertible-tfae ((b) \( \Rightarrow \) (a)).

   \( (\Rightarrow) \) Suppose \( u_{kk} = 0 \) for some \( k \). Every column \( j \le k \) of \( \U \) has zero entries in rows \( k, k+1, \dots, n \): below the diagonal by triangularity, and in row \( k \) of column \( k \) by assumption. So the \( k \) columns \( \u_1, \dots, \u_k \) all lie in \( \Span(\e_1, \dots, \e_{k-1}) \), a subspace of dimension \( k - 1 \) (its spanning list is a sub-list of the standard basis, hence independent). By @thm-size-bounds (a), a list of \( k > k - 1 \) vectors there is linearly dependent. A non-trivial relation among \( \u_1, \dots, \u_k \), extended by zero coefficients on \( \u_{k+1}, \dots, \u_n \), is a non-trivial relation among all the columns. So the columns of \( \U \) are dependent, and \( \U \) is not invertible by @thm-invertible-tfae ((a) \( \Rightarrow \) (f)). (For \( k = 1 \), the span is \( \{\0\} \) and \( \u_1 = \0 \), so the same conclusion holds.)
2. Suppose \( \U \) is invertible, so every \( u_{ii} \neq 0 \) by (a). Fix \( k \), and let \( \x \) be the \( k \)-th column of \( \U^{-1} \). By @thm-three-views-of-product, \( \U\x \) is the \( k \)-th column of \( \U\U^{-1} = \I_n \), so \( \U\x = \e_k \). For \( i > k \), row \( i \) of this system reads \( u_{ii}x_i + \dots + u_{in}x_n = 0 \). By the same downward induction as in (a), running only over \( i = n, n-1, \dots, k+1 \), we get \( x_n = \dots = x_{k+1} = 0 \). So the \( k \)-th column of \( \U^{-1} \) has zeros below position \( k \). As \( k \) was arbitrary, \( \U^{-1} \) is upper triangular.
:::
:::

::: {#exr-elementary-matrices-and-inverses-c2}
[C2: All right inverses]

Let \( \A = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \end{pmatrix} \in M_{2 \times 3}(\nR) \).

::: {.enumerate options="label=(\alph*)"}
1. Find all \( \B \in M_{3 \times 2}(\nR) \) with \( \A\B = \I_2 \).
2. Show that there is no \( \C \in M_{3 \times 2}(\nR) \) with \( \C\A = \I_3 \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. By @thm-three-views-of-product, \( \A\B = \I_2 \) means that the columns \( \b_1, \b_2 \) of \( \B \) satisfy \( \A\b_1 = \e_1 \) and \( \A\b_2 = \e_2 \). The matrix \( \A \) is already in reduced form with pivots in columns 1 and 2 and \( x_3 \) free, so \( \A\x = \0 \) means \( x_1 = -x_3 \), \( x_2 = -x_3 \), and its solutions are the multiples of \( (-1, -1, 1) \). One solution of \( \A\x = \e_1 \) is \( (1, 0, 0) \), and one solution of \( \A\x = \e_2 \) is \( (0, 1, 0) \). By @thm-general-solution-structure,
\[
\b_1 = (1, 0, 0) + s(-1, -1, 1), \qquad \b_2 = (0, 1, 0) + t(-1, -1, 1) \qquad (s, t \in \nR).
\]
Hence the right inverses of \( \A \) are exactly
\[
\B = \begin{pmatrix} 1 - s & -t \\ -s & 1 - t \\ s & t \end{pmatrix}, \qquad s, t \in \nR,
\]
infinitely many of them.
2. Suppose \( \C\A = \I_3 \), and let \( \x = (-1, -1, 1) \), so \( \A\x = \0 \). Then \( \x = \I_3\x = \C(\A\x) = \C\0 = \0 \), a contradiction since \( \x \neq \0 \). Hence \( \A \) has no left inverse.
:::
:::

::: {#exr-elementary-matrices-and-inverses-c3}
[C3: Nilpotent perturbations of the identity]

Let \( \A \in M_n(F) \) and suppose \( \A^k = 0 \) for some integer \( k \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \I_n + \A \) is invertible, by using item (b) of @thm-invertible-tfae.
2. Verify that \( (\I_n + \A)(\I_n - \A + \A^2 - \dots + (-1)^{k-1}\A^{k-1}) = \I_n \), and deduce a formula for \( (\I_n + \A)^{-1} \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Let \( \x \in F^n \) with \( (\I_n + \A)\x = \0 \). Then \( \A\x = -\x \). Multiplying on the left by \( \A \) and using this again, \( \A^2\x = \A(-\x) = -\A\x = (-1)^2\x \), and inductively \( \A^j\x = (-1)^j\x \) for every \( j \ge 1 \). Taking \( j = k \), \( \0 = \A^k\x = (-1)^k\x \), so \( \x = \0 \) (multiply by \( (-1)^k \)). By @thm-invertible-tfae ((b) \( \Rightarrow \) (a)), \( \I_n + \A \) is invertible.
2. Expanding with @thm-matrix-multiplication-properties,
\[
(\I_n + \A)\sum_{j=0}^{k-1} (-1)^j \A^j = \sum_{j=0}^{k-1} (-1)^j \A^j + \sum_{j=0}^{k-1} (-1)^j \A^{j+1} = \I_n + (-1)^{k-1}\A^k = \I_n,
\]
since the terms \( (-1)^j\A^j \) for \( 1 \le j \le k-1 \) in the first sum cancel against the terms \( (-1)^{j-1}\A^j \) of the second, and \( \A^k = 0 \). By @thm-one-sided-inverse, \( (\I_n + \A)^{-1} = \I_n - \A + \A^2 - \dots + (-1)^{k-1}\A^{k-1} \).
:::
:::
