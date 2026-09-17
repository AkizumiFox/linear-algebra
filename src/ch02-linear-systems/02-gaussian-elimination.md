# Gaussian Elimination

Every reader of this book has solved a system of equations by eliminating unknowns: subtract a multiple of one equation from another, and a variable disappears. Done by hand on small systems, this feels like common sense. Done on a system of 50 equations, or over \( \nF_2 \), or in a proof about all systems at once, it needs to be an algorithm, and we need to know that it never changes the answer. This section makes elimination precise, proves that it always reaches a standard shape, and shows how to read every solution from that shape.

## Three moves that do not change the answer

Here is a system over \( \nR \), solved the way one would solve it on paper:
\[
\begin{aligned}
x + 2y + z &= 4, \\
2x + 4y + 3z &= 9, \\
x + 3y + z &= 5 .
\end{aligned}
\]
Subtract twice the first equation from the second: \( z = 1 \). Subtract the first from the third: \( y = 1 \). Then the first equation gives \( x = 4 - 2 - 1 = 1 \).

Only three kinds of move were used, or could reasonably be used: **reorder** the equations, **multiply** an equation by a non-zero number, and **add a multiple** of one equation to another. None of them looks at the names \( x, y, z \). Each acts on the coefficients and the right-hand side of whole equations, that is, on the rows of the augmented matrix. The first step above, for instance, replaces row 2, \( (2, 4, 3 \mid 9) \), by row 2 minus twice row 1, \( (0, 0, 1 \mid 1) \).

Not every move that looks harmless is safe. Multiplying an equation by \( 0 \) turns it into \( 0 = 0 \), and a constraint silently disappears. So we list the allowed moves carefully.

*An elementary row operation is a reversible move on the rows of a matrix: swap two rows, rescale one row by a non-zero scalar, or add a multiple of one row to a different row.*

::: {#def-elementary-row-operations}
[Elementary row operations]

Let \( F \) be a field and let \( M \in M_{m \times k}(F) \) have rows \( \r_1, \dots, \r_m \). An **elementary row operation** on \( M \) is one of the following.

::: {.enumerate options="label=(\arabic*)"}
1. **Swap** two rows: for \( i \neq j \), exchange \( \r_i \) and \( \r_j \). Notation: \( R_i \leftrightarrow R_j \).
2. **Scale** a row: for an index \( i \) and a scalar \( c \in F \) with \( c \neq 0 \), replace \( \r_i \) by \( c\r_i \). Notation: \( R_i \to cR_i \).
3. **Replace** a row by adding a multiple of **another** row: for indices \( i \neq j \) and any \( c \in F \), replace \( \r_i \) by \( \r_i + c\r_j \). Notation: \( R_i \to R_i + cR_j \).
:::

In each case the rows not mentioned are left unchanged.
:::

In words: (1) reorders, (2) rescales one row by a **non-zero** scalar, and (3) changes **one** row, row \( i \), using a **different** row \( j \), which itself stays as it was. We write \( R_i \to R_i - cR_j \) for \( R_i \to R_i + (-c)R_j \). The notation \( R_i \) refers to the current row \( i \) at the moment the operation is performed.

Take \( M = \begin{pmatrix} 1 & 2 & 0 \\ 3 & 1 & 1 \end{pmatrix} \) over \( \nR \). Then \( R_1 \leftrightarrow R_2 \) gives \( \begin{pmatrix} 3 & 1 & 1 \\ 1 & 2 & 0 \end{pmatrix} \), \( R_1 \to -2R_1 \) gives \( \begin{pmatrix} -2 & -4 & 0 \\ 3 & 1 & 1 \end{pmatrix} \), and \( R_2 \to R_2 - 3R_1 \) gives \( \begin{pmatrix} 1 & 2 & 0 \\ 0 & -5 & 1 \end{pmatrix} \). The degenerate case \( m = 1 \) is worth a glance: a one-row matrix admits no swap and no replacement, since both need two different rows, so its only elementary row operations are the scalings.

The minimal change that breaks the definition is to drop "\( c \neq 0 \)". The move \( R_2 \to 0R_2 \) still replaces one row by a multiple of itself, but it sends \( \begin{pmatrix} 1 & 2 & 0 \\ 3 & 1 & 1 \end{pmatrix} \) to \( \begin{pmatrix} 1 & 2 & 0 \\ 0 & 0 & 0 \end{pmatrix} \), and no move of any kind can recover the lost row \( (3, 1, 1) \) from that matrix. The failing clause is \( c \neq 0 \), and the damage is exactly irreversibility.

::: {.warning}
**Perform operations one at a time.** It is tempting to write "\( R_1 \to R_1 - R_2 \) and \( R_2 \to R_2 - R_1 \)" as one step, using the old rows in both. That is not a sequence of elementary row operations, and it can destroy information. On the system \( x = 1 \), \( x = 1 \) it produces \( 0 = 0 \), \( 0 = 0 \), whose solution set is all of \( F \), not \( \{ 1 \} \). Done in order, the second operation uses the **new** row 1, \( (0 \mid 0) \), and leaves row 2 unchanged, so no information is lost.
:::

Why these three and no others? They are exactly the moves of hand elimination, and each can be undone by a move of the same kind, which is what the theorem below needs. The condition \( i \neq j \) in (3) is not fussiness: "add \( c \) times row \( i \) to row \( i \)" would be scaling by \( 1 + c \), which is illegal when \( c = -1 \) (Exercise C1).

An elementary row operation acts on the rows, but it treats each column separately: the new entry in position \( (i, l) \) is computed only from entries of column \( l \). We record this, because it will be used again and again.

::: {#lem-row-ops-act-on-columns}
[Row operations act column by column]

Let \( M = [\, M_1 \mid M_2 \,] \in M_{m \times k}(F) \) be split into its first \( k_1 \) columns \( M_1 \) and its remaining columns \( M_2 \). If an elementary row operation turns \( M \) into \( M' = [\, M'_1 \mid M'_2 \,] \) (split in the same place), then the same operation turns \( M_1 \) into \( M'_1 \) and \( M_2 \) into \( M'_2 \). In particular, an elementary row operation turns a zero column into a zero column.
:::

::: {.proof}
Let \( m_{hl} \) be the entries of \( M \) and \( m'_{hl} \) those of \( M' \). For a swap \( R_i \leftrightarrow R_j \): \( m'_{il} = m_{jl} \), \( m'_{jl} = m_{il} \), and \( m'_{hl} = m_{hl} \) for \( h \neq i, j \). For a scaling \( R_i \to cR_i \): \( m'_{il} = c\,m_{il} \), and other rows are unchanged. For a replacement \( R_i \to R_i + cR_j \): \( m'_{il} = m_{il} + c\,m_{jl} \), and other rows are unchanged. In each case, every entry of column \( l \) of \( M' \) is computed from column \( l \) of \( M \) alone, by the same rule for every \( l \). Hence applying the operation to \( M_1 \) or to \( M_2 \) separately gives \( M'_1 \) and \( M'_2 \). If column \( l \) of \( M \) is zero, each formula gives \( 0 \), since \( c \cdot 0 = 0 \) and \( 0 + c \cdot 0 = 0 \) (@thm-field-basic-properties).
:::

For an augmented matrix, the lemma says: operating on \( [\, A \mid \b \,] \) is the same as operating on \( A \) and on \( \b \) with the same moves. Now we name what sequences of moves produce.

::: {#def-row-equivalent}
[Row equivalence]

Let \( A, B \in M_{m \times k}(F) \). We say \( A \) is **row equivalent** to \( B \) if \( B \) can be obtained from \( A \) by a **finite** sequence of elementary row operations. The empty sequence is allowed, so every matrix is row equivalent to itself.
:::

In @exm-row-equivalence of Chapter 0 we met a definition that looks different: \( B = EA \) for an **invertible** matrix \( E \). In section 4 of this chapter we prove that the two definitions agree (@thm-row-equivalent-iff-invertible-multiple), by writing each elementary row operation as multiplication by an invertible matrix. Until then, "row equivalent" means the definition above.

## Row operations preserve solutions

Here is the promise from the start of the section, now as a theorem.

::: {#thm-row-ops-preserve-solutions}
[Row operations preserve solutions]

Let \( F \) be a field.

::: {.enumerate options="label=(\alph*)"}
1. **(Reversibility)** If an elementary row operation turns \( M \) into \( M' \), then an elementary row operation **of the same type** turns \( M' \) back into \( M \).
2. Row equivalence is an equivalence relation on \( M_{m \times k}(F) \).
3. If \( [\, A \mid \b \,] \) and \( [\, A' \mid \b' \,] \) in \( M_{m \times (n + 1)}(F) \) are row equivalent, then the systems \( A\x = \b \) and \( A'\x = \b' \) have the **same** solution set.
:::
:::

::: {.idea}
Reversibility is checked type by type, and the check for scaling is the only place where \( c \neq 0 \) is used. For (c), every equation of the new system is a combination of equations of the old one, so an old solution satisfies the new system. That gives one inclusion. Instead of repeating the argument backwards, reversibility gives the other inclusion for free.
:::

::: {.proof}
(a) A swap \( R_i \leftrightarrow R_j \) is undone by the same swap. A scaling \( R_i \to cR_i \) is undone by \( R_i \to c^{-1}R_i \), which is a legal scaling because \( c \neq 0 \) has an inverse \( c^{-1} \neq 0 \) in \( F \) (@def-field): the row becomes \( c^{-1}(c\r_i) = \r_i \). A replacement \( R_i \to R_i + cR_j \) is undone by \( R_i \to R_i - cR_j \). Here we use \( i \neq j \): row \( j \) was not changed by the first operation, so the second one gives \( (\r_i + c\r_j) - c\r_j = \r_i \).

(b) Reflexivity holds via the empty sequence. For symmetry, suppose operations \( O_1, \dots, O_s \), in this order, turn \( A \) into \( B \). By (a), each \( O_t \) has an undoing operation \( O'_t \). Then \( O'_s, O'_{s-1}, \dots, O'_1 \), in this order, turn \( B \) back into \( A \). For transitivity, if a sequence turns \( A \) into \( B \) and another turns \( B \) into \( C \), performing the first and then the second turns \( A \) into \( C \), and this is still a finite sequence.

(c) First suppose a **single** operation turns \( [\, A \mid \b \,] \) into \( [\, A' \mid \b' \,] \). Let \( S \) and \( S' \) be the two solution sets. Write \( \r_h \) for row \( h \) of \( A \), so that equation \( h \) says \( \r_h\x = b_h \), where \( \r_h\x \) is a \( 1 \times 1 \) product. Let \( \s \in S \), so \( \r_h\s = b_h \) for every \( h \). Each equation of the new system holds at \( \s \):

- after \( R_i \leftrightarrow R_j \), the new equations are the old ones in another order;
- after \( R_i \to cR_i \), the new equation \( i \) is \( (c\r_i)\x = cb_i \), and \( (c\r_i)\s = c(\r_i\s) = cb_i \);
- after \( R_i \to R_i + cR_j \), the new equation \( i \) is \( (\r_i + c\r_j)\x = b_i + cb_j \), and \( (\r_i + c\r_j)\s = \r_i\s + c(\r_j\s) = b_i + cb_j \), by @thm-matrix-multiplication-properties.

The other equations are unchanged. Hence \( \s \in S' \), and \( S \subseteq S' \). By (a), a single operation turns \( [\, A' \mid \b' \,] \) back into \( [\, A \mid \b \,] \), so the same argument gives \( S' \subseteq S \). Therefore \( S = S' \).

For a sequence of \( s \) operations, the intermediate augmented matrices all have the same solution set, by the single-operation case applied \( s \) times (formally, by induction on \( s \)). This proves (c).
:::

This theorem is the license for everything that follows: we may transform a system as much as we like by row operations, and the solutions of the final system are the solutions of the original one. What it does **not** license is just as important.

::: {.warning}
**Scaling by \( 0 \) is not a row operation, and it changes the solution set.** Over \( \nR \), the system \( x + y = 2 \), \( x - y = 0 \) has exactly one solution, \( (1, 1) \). Applying the illegal move \( R_2 \to 0R_2 \) gives \( x + y = 2 \), \( 0 = 0 \), whose solutions \( (2 - t, t) \) form a whole line. The inclusion \( S \subseteq S' \) in the proof above still holds; what fails is reversibility, and with it \( S' \subseteq S \).
:::

::: {.warning}
**Column operations are not allowed.** Operations on the columns of \( [\, A \mid \b \,] \) mix up the unknowns. The system \( x + y = 3 \), \( x - y = 1 \) has the unique solution \( (2, 1) \). Adding column 1 to column 2 of its augmented matrix gives \( \left[ \begin{array}{cc|c} 1 & 2 & 3 \\ 1 & 0 & 1 \end{array} \right] \), the system \( x + 2y = 3 \), \( x = 1 \), whose only solution is \( (1, 1) \). Even swapping two columns of \( A \) swaps the corresponding entries of every solution.
:::

## Echelon forms

Row operations can change a system a great deal. We now choose a target: a shape of matrix from which the solutions can be read off with no further work. Look at the finished computation from the start of the section. After eliminating, the augmented matrix could be brought to
\[
\left[ \begin{array}{ccc|c} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 1 \end{array} \right],
\]
which says \( x = 1 \), \( y = 1 \), \( z = 1 \) outright. Not every system can be brought to this shape, since not every system has exactly one solution. The general target is a staircase.

For a non-zero row of a matrix, its **leading entry** is its first non-zero entry, reading from the left.

*A matrix is in row echelon form when its non-zero rows come first and their leading entries step strictly to the right as we go down.*

::: {#def-row-echelon-form}
[Row echelon form]

A matrix \( R \in M_{m \times k}(F) \) is in **row echelon form** if:

::: {.enumerate options="label=(E\arabic*)"}
1. there is an integer \( r \) with \( 0 \le r \le m \) such that rows \( 1, \dots, r \) are non-zero and rows \( r + 1, \dots, m \) are zero; and
2. if the leading entry of row \( i \) lies in column \( j_i \), for \( i = 1, \dots, r \), then \( j_1 < j_2 < \dots < j_r \), **strictly**.
:::

The leading entries of rows \( 1, \dots, r \) are the **pivots** of \( R \), and the columns \( j_1, \dots, j_r \) are its **pivot columns**.
:::

In words: (E1) says zero rows sit at the bottom, and (E2) says each pivot lies strictly to the right of the pivot above it. Two consequences are used constantly. Each row contains at most one pivot, so there are at most \( m \) pivots. And **every entry below a pivot is zero**: if \( h > i \), then row \( h \) is zero or has its leading entry in column \( j_h > j_i \), so its entry in column \( j_i \) is \( 0 \).

::: {#def-reduced-row-echelon-form}
[Reduced row echelon form]

A matrix \( R \in M_{m \times k}(F) \) is in **reduced row echelon form** (**RREF**) if it is in row echelon form, with pivot columns \( j_1 < \dots < j_r \), and moreover:

::: {.enumerate options="label=(E\arabic*)"}
3. every pivot equals \( 1 \): \( r_{i j_i} = 1 \) for \( i = 1, \dots, r \); and
4. every pivot is the **only** non-zero entry in its column: \( r_{h j_i} = 0 \) for all \( h \neq i \).
:::
:::

In words: (E3) normalizes the pivots, and (E4) clears the entries **above** each pivot as well as below. Together they say that the pivot column \( j_i \) is the standard basis vector \( \e_i \in F^m \).

::: {#exm-echelon-forms}
[Echelon or not?]

Decide which of the following real matrices are in row echelon form, and which are in reduced row echelon form. Give the pivot columns where they exist.
\[
P = \begin{pmatrix} 2 & 1 & 3 \\ 0 & 0 & -1 \\ 0 & 0 & 0 \end{pmatrix}, \quad
Q = \begin{pmatrix} 1 & 5 & 0 & 2 \\ 0 & 0 & 1 & 3 \end{pmatrix}, \quad
T = \begin{pmatrix} 1 & 0 & 2 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}, \quad
Z = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}.
\]
:::

::: {.solution}
\( P \) is in row echelon form: rows 1 and 2 are non-zero, row 3 is zero, and the leading entries lie in columns \( 1 < 3 \). The pivot columns are 1 and 3. It is **not** reduced: the pivot \( 2 \) is not \( 1 \), failing (E3), and column 3 has the non-zero entry \( 3 \) above the pivot \( -1 \), failing (E4).

\( Q \) is in reduced row echelon form, with pivot columns 1 and 3. Both pivots are \( 1 \), and columns 1 and 3 are \( \e_1 \) and \( \e_2 \). The entries \( 5, 2, 3 \) in the non-pivot columns 2 and 4 are allowed to be anything.

\( T \) is **not** in row echelon form. Its leading entries lie in columns \( 1, 3, 2 \), and \( 3 < 2 \) fails, so (E2) fails. Swapping rows 2 and 3 would repair it.

\( Z \) is in reduced row echelon form, with \( r = 0 \): there are no pivots, and (E2)–(E4) hold vacuously. This degenerate case matters, because the zero matrix must have an RREF too, and it is itself.
:::

For \( Q \), a minimal change gives a non-example: replacing the \( 0 \) in position \( (1, 3) \) by \( 4 \) keeps (E1)–(E3), but column 3 now has the non-zero entry \( 4 \) above its pivot, so (E4) fails.

Why insist on the reduced form, when row echelon form already allows back substitution? Because a system in reduced form needs **no** substitution: each pivot variable appears in exactly one equation. More importantly, the reduced form turns out to be **unique**: a matrix is row equivalent to exactly one matrix in RREF, however the operations are chosen. That is proved in the next section, and it is what makes later definitions, such as the rank, independent of choices. Row echelon form is not unique, as the warning after the worked example shows.

::: {.check}
Is \( \begin{pmatrix} 1 & 2 & 0 & -1 \\ 0 & 0 & 1 & 3 \\ 0 & 0 & 0 & 0 \end{pmatrix} \) in reduced row echelon form? If it is the coefficient matrix of a homogeneous system in \( x_1, x_2, x_3, x_4 \), which unknowns correspond to pivot columns?
:::

::: {.solution}
Yes. Row 3 is the only zero row and it is last; the leading entries lie in columns \( 1 < 3 \); both are \( 1 \); and columns 1 and 3 are \( \e_1 \) and \( \e_2 \). The pivot columns are 1 and 3, so the unknowns \( x_1 \) and \( x_3 \) correspond to pivots, and \( x_2, x_4 \) do not.
:::

## Gauss–Jordan elimination

We now show that every matrix can be brought to reduced row echelon form. The procedure works through the columns from left to right, keeping a count \( r \) of the pivots found so far.

::: {.algorithm}
**Gauss–Jordan elimination.** Input: \( M \in M_{m \times k}(F) \). Set \( r = 0 \). For \( l = 1, 2, \dots, k \) in turn:

1. Look for a row \( h \) with \( h > r \) whose entry in column \( l \) is non-zero. If there is none, column \( l \) gets no pivot; go on to the next \( l \).
2. Otherwise choose such an \( h \). If \( h \neq r + 1 \), perform \( R_{r+1} \leftrightarrow R_h \).
3. Let \( a \neq 0 \) be the entry now in position \( (r + 1, l) \). Perform \( R_{r+1} \to a^{-1}R_{r+1} \), so that this entry becomes \( 1 \).
4. For every row \( g \neq r + 1 \) whose entry \( c \) in column \( l \) is non-zero, perform \( R_g \to R_g - cR_{r+1} \).
5. Increase \( r \) by \( 1 \).

Output: the final matrix, which is in reduced row echelon form, with \( r \) pivots.
:::

Step 2 involves a choice: any non-zero entry will do. By hand, we choose one that avoids fractions. If we skip the scaling in step 3 and clear only the entries **below** the pivot \( a \), by \( R_g \to R_g - ca^{-1}R_{r+1} \) for the rows \( g > r + 1 \), the output is a row echelon form instead; this cheaper variant is **Gaussian elimination**, and it is followed by back substitution.

::: {#thm-rref-exists}
[Existence of the reduced row echelon form]

Let \( F \) be a field. Every matrix \( M \in M_{m \times k}(F) \) is row equivalent to a matrix in reduced row echelon form.
:::

::: {.idea}
We prove that the algorithm works, by induction on the number \( l \) of columns processed. The invariant is: the first \( l \) columns of the current matrix form a matrix in RREF. When a new column is processed, all the operations involve only rows below the pivots found so far, or add multiples of the new pivot row, which is zero in the first \( l \) columns. So the part already built is never disturbed. After all \( k \) columns, the whole matrix is in RREF.
:::

::: {.proof}
For \( 0 \le l \le k \), let \( P(l) \) be the statement: there is a matrix \( M_l \) row equivalent to \( M \) and an integer \( r \ge 0 \) such that the \( m \times l \) matrix \( L \) formed by the first \( l \) columns of \( M_l \) is in reduced row echelon form with exactly \( r \) non-zero rows. We prove \( P(l) \) for all \( l \) by induction (@thm-induction). For \( l = 0 \) take \( M_0 = M \) and \( r = 0 \); there are no columns, so there is nothing to check.

Suppose \( P(l) \) holds for some \( l < k \), with \( M_l \), \( L \) and \( r \) as described, and let \( j_1 < \dots < j_r \le l \) be the pivot columns of \( L \). By (E1) for \( L \), rows \( r + 1, \dots, m \) of \( M_l \) are zero in columns \( 1, \dots, l \). Let \( L' \) denote the first \( l + 1 \) columns of the matrix we are about to construct.

*Case 1: every entry of column \( l + 1 \) of \( M_l \) in rows \( h > r \) is zero* (this includes the case \( r = m \)). Put \( M_{l+1} = M_l \). Rows \( r + 1, \dots, m \) of \( L' \) are zero, and rows \( 1, \dots, r \) are non-zero with the same leading entries as in \( L \), which lie in columns \( \le l \). So (E1)–(E3) hold for \( L' \) with the same \( r \) and pivot columns, and so does (E4), since the pivot columns of \( L' \) are those of \( L \) and are unchanged. Hence \( L' \) is in RREF and \( P(l + 1) \) holds.

*Case 2: some row \( h > r \) has a non-zero entry in column \( l + 1 \).* Then \( r + 1 \le h \le m \). Perform steps 2, 3 and 4 of the algorithm with this \( h \) and with column \( l + 1 \); call the result \( M_{l+1} \). It is row equivalent to \( M_l \), hence to \( M \), by @thm-row-ops-preserve-solutions (b).

These operations do not change columns \( 1, \dots, l \). Indeed, the swap in step 2 and the scaling in step 3 only move or rescale rows \( h \) and \( r + 1 \), which are both zero in those columns. Each replacement \( R_g \to R_g - cR_{r+1} \) in step 4 adds a multiple of row \( r + 1 \), which is still zero in columns \( 1, \dots, l \). So the first \( l \) columns of \( M_{l+1} \) form the matrix \( L \). In column \( l + 1 \), step 3 makes the entry in row \( r + 1 \) equal to \( 1 \), and each replacement in step 4 makes the entry of row \( g \) equal to \( c - c \cdot 1 = 0 \) without changing any other row. So column \( l + 1 \) of \( M_{l+1} \) is \( \e_{r+1} \).

We check that \( L' \) is in RREF with \( r + 1 \) non-zero rows. Rows \( 1, \dots, r \) of \( L' \) have the same leading entries as in \( L \), in columns \( j_1 < \dots < j_r \le l \). Row \( r + 1 \) is zero in columns \( 1, \dots, l \) and has a \( 1 \) in column \( l + 1 \), so its leading entry is in column \( j_{r+1} \coloneqq l + 1 > j_r \). Rows \( r + 2, \dots, m \) are zero in columns \( 1, \dots, l \) and in column \( l + 1 \), so they are zero. This gives (E1) and (E2). The pivots are \( 1 \), by (E3) for \( L \) and the construction, so (E3) holds. For (E4), the columns \( j_1, \dots, j_r \) are unchanged from \( L \), and column \( l + 1 \) is \( \e_{r+1} \). Hence \( P(l + 1) \) holds.

By induction \( P(k) \) holds: \( M_k \) is row equivalent to \( M \), and its first \( k \) columns, which are all of \( M_k \), form a matrix in reduced row echelon form. This proves the theorem.
:::

The proof is also the correctness proof of the algorithm: the matrix \( M_l \) is the state of the computation after column \( l \). Note where the field axioms were used. Step 3 divides by \( a \neq 0 \), which needs (F8), and nothing else in the argument depends on which field we work over.

::: {#exm-gauss-jordan-3x4}
[Gauss–Jordan on a \( 3 \times 4 \) system]

Solve the following system over \( \nR \) by Gauss–Jordan elimination, naming each operation:
\[
\begin{aligned}
2x_2 - 2x_3 + x_4 &= 3, \\
x_1 + x_2 + x_3 \phantom{{} + x_4} &= 3, \\
2x_1 + x_2 + 3x_3 + x_4 &= 3 .
\end{aligned}
\]
:::

::: {.solution}
We work on the augmented matrix. **Column 1.** Row 1 has a \( 0 \) there, so we bring up row 2, whose entry is already \( 1 \). Then we clear the rest of column 1.
\[
\left[ \begin{array}{cccc|c} 0 & 2 & -2 & 1 & 3 \\ 1 & 1 & 1 & 0 & 3 \\ 2 & 1 & 3 & 1 & 3 \end{array} \right]
\xrightarrow{R_1 \leftrightarrow R_2}
\left[ \begin{array}{cccc|c} 1 & 1 & 1 & 0 & 3 \\ 0 & 2 & -2 & 1 & 3 \\ 2 & 1 & 3 & 1 & 3 \end{array} \right]
\xrightarrow{R_3 \to R_3 - 2R_1}
\left[ \begin{array}{cccc|c} 1 & 1 & 1 & 0 & 3 \\ 0 & 2 & -2 & 1 & 3 \\ 0 & -1 & 1 & 1 & -3 \end{array} \right]
\]
**Column 2.** The candidates below row 1 are \( 2 \) and \( -1 \). Choosing \( -1 \) avoids fractions, so we swap it up and scale.
\[
\xrightarrow{R_2 \leftrightarrow R_3}
\left[ \begin{array}{cccc|c} 1 & 1 & 1 & 0 & 3 \\ 0 & -1 & 1 & 1 & -3 \\ 0 & 2 & -2 & 1 & 3 \end{array} \right]
\xrightarrow{R_2 \to -R_2}
\left[ \begin{array}{cccc|c} 1 & 1 & 1 & 0 & 3 \\ 0 & 1 & -1 & -1 & 3 \\ 0 & 2 & -2 & 1 & 3 \end{array} \right]
\]
Now clear column 2 above and below the pivot.
\[
\xrightarrow{R_1 \to R_1 - R_2}
\left[ \begin{array}{cccc|c} 1 & 0 & 2 & 1 & 0 \\ 0 & 1 & -1 & -1 & 3 \\ 0 & 2 & -2 & 1 & 3 \end{array} \right]
\xrightarrow{R_3 \to R_3 - 2R_2}
\left[ \begin{array}{cccc|c} 1 & 0 & 2 & 1 & 0 \\ 0 & 1 & -1 & -1 & 3 \\ 0 & 0 & 0 & 3 & -3 \end{array} \right]
\]
**Column 3.** The only entry below row 2 is \( 0 \), so column 3 gets no pivot. **Column 4.** The entry \( 3 \) in row 3 becomes the pivot.
\[
\xrightarrow{R_3 \to \frac13 R_3}
\left[ \begin{array}{cccc|c} 1 & 0 & 2 & 1 & 0 \\ 0 & 1 & -1 & -1 & 3 \\ 0 & 0 & 0 & 1 & -1 \end{array} \right]
\xrightarrow{R_1 \to R_1 - R_3}
\left[ \begin{array}{cccc|c} 1 & 0 & 2 & 0 & 1 \\ 0 & 1 & -1 & -1 & 3 \\ 0 & 0 & 0 & 1 & -1 \end{array} \right]
\xrightarrow{R_2 \to R_2 + R_3}
\left[ \begin{array}{cccc|c} 1 & 0 & 2 & 0 & 1 \\ 0 & 1 & -1 & 0 & 2 \\ 0 & 0 & 0 & 1 & -1 \end{array} \right]
\]
**Column 5.** No rows remain below row 3, so we stop. The final matrix is in RREF, with pivot columns 1, 2 and 4. It is the system
\[
x_1 + 2x_3 = 1, \qquad x_2 - x_3 = 2, \qquad x_4 = -1,
\]
which by @thm-row-ops-preserve-solutions has the same solutions as the original. The unknown \( x_3 \) is unconstrained; writing \( x_3 = t \), the solutions are
\[
(1 - 2t,\ 2 + t,\ t,\ -1) = (1, 2, 0, -1) + t(-2, 1, 1, 0), \qquad t \in \nR .
\]
Check: \( (1, 2, 0, -1) \) gives \( 4 + 0 - 1 = 3 \), \( 1 + 2 + 0 = 3 \) and \( 2 + 2 + 0 - 1 = 3 \); and \( (-2, 1, 1, 0) \) gives \( 2 - 2 + 0 = 0 \), \( -2 + 1 + 1 = 0 \) and \( -4 + 1 + 3 + 0 = 0 \). This is the "particular plus homogeneous" form of @thm-general-solution-structure.
:::

A computer algebra system does the same computation exactly. In the online version the cell below can be edited and run, which is a good way to check a hand computation.

```{.python .run #cell-gauss-jordan-check}
from sympy import Matrix

M = Matrix([
    [0, 2, -2, 1, 3],
    [1, 1,  1, 0, 3],
    [2, 1,  3, 1, 3],
])
R, pivots = M.rref()   # the RREF and the (0-based) pivot columns
print(R)
print("pivot columns:", [j + 1 for j in pivots])
```

::: {.warning}
**Echelon forms are not unique; only the reduced form is.** Different choices in step 2 give different intermediate matrices. For \( \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \) over \( \nR \), the operation \( R_2 \to R_2 - 3R_1 \) gives the row echelon form \( \begin{pmatrix} 1 & 2 \\ 0 & -2 \end{pmatrix} \). Starting instead with \( R_1 \leftrightarrow R_2 \) and then \( R_2 \to R_2 - \frac13 R_1 \) gives the row echelon form \( \begin{pmatrix} 3 & 4 \\ 0 & \frac23 \end{pmatrix} \). Both continue to the same RREF, \( I_2 \). That this always happens is the theorem of the next section; until it is proved, "the" RREF of a matrix is not yet justified.
:::

## Reading off the solutions

Once \( [\, A \mid \b \,] \) is in reduced row echelon form, the example shows what to do: a pivot in the last column signals a contradiction, and otherwise the unknowns without pivots can be chosen freely. We name the two kinds of unknowns.

Suppose \( [\, A \mid \b \,] \), with \( A \in M_{m \times n}(F) \), is row equivalent to a matrix \( [\, R \mid \c \,] \) in reduced row echelon form, where \( R \) is \( m \times n \). For \( l \le n \), the unknown \( x_l \) is a **pivot variable** if \( l \) is a pivot column of \( [\, R \mid \c \,] \), and a **free variable** otherwise. (By the uniqueness theorem of the next section, this does not depend on which sequence of operations was used.)

::: {#thm-reading-rref}
[Reading solutions from the RREF]

Let \( A \in M_{m \times n}(F) \) and \( \b \in F^m \), and suppose \( [\, A \mid \b \,] \) is row equivalent to a matrix \( [\, R \mid \c \,] \) in reduced row echelon form. Let \( r_{il} \) be the entries of \( R \) and \( \c = (c_1, \dots, c_m) \).

::: {.enumerate options="label=(\alph*)"}
1. \( A\x = \b \) is inconsistent **if and only if** the last column, column \( n + 1 \), is a pivot column of \( [\, R \mid \c \,] \), that is, some row of \( [\, R \mid \c \,] \) is \( (0 \ \cdots \ 0 \mid 1) \).
2. Suppose there is no pivot in the last column. Let \( j_1 < \dots < j_r \) be the pivot columns. Then for **every** choice of scalars \( t_l \in F \), one for each free variable \( x_l \), there is **exactly one** solution with \( x_l = t_l \) for all free \( l \), namely the one with
\[
x_{j_i} = c_i - \sum_{l \text{ free}} r_{il}\, t_l \qquad (i = 1, \dots, r).
\]
In particular, setting every free variable to \( 0 \) gives the solution \( \p \) with \( p_{j_i} = c_i \) and all other entries \( 0 \).
3. A consistent system \( A\x = \b \) has exactly one solution **if and only if** it has no free variables, that is, each of the columns \( 1, \dots, n \) is a pivot column.
:::
:::

::: {.proof}
By @thm-row-ops-preserve-solutions (c), \( A\x = \b \) has the same solution set as \( R\x = \c \), so we work with the latter.

(a, ⇐) If row \( i \) of \( [\, R \mid \c \,] \) has its pivot in column \( n + 1 \), then its first \( n \) entries are \( 0 \) and \( c_i = 1 \) by (E3). Equation \( i \) reads \( 0 = 1 \), which is false in any field (@def-field). So there is no solution.

(b) Suppose no pivot lies in column \( n + 1 \). Then all pivots of \( [\, R \mid \c \,] \) lie in columns \( j_1, \dots, j_r \le n \). By (E1), rows \( r + 1, \dots, m \) of \( [\, R \mid \c \,] \) are zero, so the corresponding equations read \( 0 = 0 \) and hold for every \( \x \). For \( i \le r \), row \( i \) of \( R \) has \( r_{i j_i} = 1 \) by (E3) and \( r_{i j_h} = 0 \) for \( h \neq i \) by (E4). So equation \( i \) reads
\[
x_{j_i} + \sum_{l \text{ free}} r_{il}\, x_l = c_i .
\]
Hence \( \x \) is a solution if and only if \( x_{j_i} = c_i - \sum_{l \text{ free}} r_{il} x_l \) for \( i = 1, \dots, r \). Each unknown is either a pivot variable or a free variable, not both. So once the free variables are given the values \( t_l \), these equations determine every pivot variable uniquely, and the resulting vector is a solution. This proves (b).

(a, ⇒) This is the contrapositive of what (b) just showed: if there is no pivot in the last column, then choosing all \( t_l = 0 \) produces a solution, so the system is consistent.

(c) By (a), a consistent system has no pivot in the last column, so (b) applies. If there are no free variables, (b) gives exactly one solution. If \( x_l \) is free, the choices \( t_l = 0 \) and \( t_l = 1 \), with all other free variables \( 0 \), give two solutions whose \( l \)-th entries differ, since \( 0 \neq 1 \). This proves (c).
:::

In @exm-gauss-jordan-3x4 the pivot columns were 1, 2, 4, the free variable was \( x_3 \), and (b) gave \( x_1 = 1 - 2t \), \( x_2 = 2 + t \), \( x_4 = -1 \), with \( \p = (1, 2, 0, -1) \). The same recipe works over any field, and over a finite field the free variables can take only finitely many values.

::: {#exm-elimination-f2}
[Elimination over \( \nF_2 \)]

Solve the following system over \( \nF_2 \):
\[
x_1 + x_2 + x_4 = 1, \qquad x_2 + x_3 + x_4 = 0, \qquad x_1 + x_3 + x_4 = 1 .
\]
How many solutions are there? What changes if the same equations are read over \( \nR \)?
:::

::: {.solution}
In \( \nF_2 \), \( -1 = 1 \), so \( R_i \to R_i - R_j \) is the same operation as \( R_i \to R_i + R_j \), and every non-zero pivot is already \( 1 \). **Column 1** has its pivot in row 1; clear row 3. **Column 2** has its pivot in row 2; clear rows 3 and 1.
\[
\left[ \begin{array}{cccc|c} 1 & 1 & 0 & 1 & 1 \\ 0 & 1 & 1 & 1 & 0 \\ 1 & 0 & 1 & 1 & 1 \end{array} \right]
\xrightarrow{R_3 \to R_3 + R_1}
\left[ \begin{array}{cccc|c} 1 & 1 & 0 & 1 & 1 \\ 0 & 1 & 1 & 1 & 0 \\ 0 & 1 & 1 & 0 & 0 \end{array} \right]
\xrightarrow{R_3 \to R_3 + R_2}
\left[ \begin{array}{cccc|c} 1 & 1 & 0 & 1 & 1 \\ 0 & 1 & 1 & 1 & 0 \\ 0 & 0 & 0 & 1 & 0 \end{array} \right]
\]
\[
\xrightarrow{R_1 \to R_1 + R_2}
\left[ \begin{array}{cccc|c} 1 & 0 & 1 & 0 & 1 \\ 0 & 1 & 1 & 1 & 0 \\ 0 & 0 & 0 & 1 & 0 \end{array} \right]
\]
In the row \( R_3 + R_1 \), the entries \( 1 + 1 \) became \( 0 \), and in \( R_3 + R_2 \) the entry in column 3 is \( 1 + 1 = 0 \). **Column 3** has only a \( 0 \) below row 2, so no pivot. **Column 4** has its pivot in row 3; row 1 already has a \( 0 \) there, so only row 2 needs clearing.
\[
\xrightarrow{R_2 \to R_2 + R_3}
\left[ \begin{array}{cccc|c} 1 & 0 & 1 & 0 & 1 \\ 0 & 1 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 \end{array} \right]
\]
This is in RREF, with pivot columns 1, 2, 4 and no pivot in the last column, so the system is consistent by @thm-reading-rref (a). The free variable is \( x_3 = t \), and part (b) gives \( x_1 = 1 - t = 1 + t \), \( x_2 = -t = t \), \( x_4 = 0 \). Since \( t \in \nF_2 = \{ 0, 1 \} \), there are exactly two solutions:
\[
(1, 0, 0, 0) \quad \text{and} \quad (0, 1, 1, 0).
\]
Check the second: \( 0 + 1 + 0 = 1 \), \( 1 + 1 + 0 = 0 \), \( 0 + 1 + 0 = 1 \) in \( \nF_2 \).

Over \( \nR \) the first step is \( R_3 \to R_3 - R_1 \), giving row 3 \( = (0, -1, 1, 0 \mid 0) \), and adding row 2 then gives \( (0, 0, 2, 1 \mid 0) \). The entry \( 2 \) is non-zero in \( \nR \), so column 3 now gets a pivot. Completing the reduction gives pivot columns 1, 2, 3, free variable \( x_4 \), and infinitely many real solutions. The same equations lead to different pivot patterns over different fields, because \( 1 + 1 = 0 \) in one and not in the other.
:::

When a coefficient depends on a parameter, whether a column gets a pivot can depend on the parameter too. Then the reduction splits into cases, one for each answer to "is this entry zero?".

::: {#exm-system-with-parameter}
[A system with a parameter]

For which \( k \in \nR \) does the system \( x + ky = 1 \), \( kx + y = 1 \) have no solution, exactly one solution, or infinitely many? Find the solutions when they exist.
:::

::: {.solution}
The entry in position \( (1, 1) \) is \( 1 \) for every \( k \), so it is a pivot with no case distinction:
\[
\left[ \begin{array}{cc|c} 1 & k & 1 \\ k & 1 & 1 \end{array} \right]
\xrightarrow{R_2 \to R_2 - kR_1}
\left[ \begin{array}{cc|c} 1 & k & 1 \\ 0 & 1 - k^2 & 1 - k \end{array} \right].
\]
(For \( k = 0 \) this operation changes nothing, which is allowed.) Column 2 gets a pivot in row 2 exactly when \( 1 - k^2 = (1 - k)(1 + k) \) is non-zero, and only then may we scale by its inverse. So we split into cases.

*Case \( k \neq \pm 1 \).* Then \( 1 - k^2 \neq 0 \), and \( R_2 \to (1 - k^2)^{-1}R_2 \) turns row 2 into \( (0, 1 \mid \tfrac{1}{1 + k}) \), since \( \tfrac{1 - k}{(1 - k)(1 + k)} = \tfrac{1}{1 + k} \). Then \( R_1 \to R_1 - kR_2 \) turns row 1 into \( (1, 0 \mid 1 - \tfrac{k}{1 + k}) = (1, 0 \mid \tfrac{1}{1 + k}) \). The RREF is \( [\, I_2 \mid \c \,] \) with \( \c = (\tfrac{1}{1 + k}, \tfrac{1}{1 + k}) \), and by @thm-reading-rref (c) this is the only solution. Check: \( \tfrac{1}{1 + k} + \tfrac{k}{1 + k} = 1 \) for both equations.

*Case \( k = 1 \).* Row 2 is \( (0, 0 \mid 0) \), and \( \left[ \begin{array}{cc|c} 1 & 1 & 1 \\ 0 & 0 & 0 \end{array} \right] \) is in RREF with pivot column 1. The free variable is \( y = t \), and @thm-reading-rref (b) gives the solutions \( (1 - t, t) \), \( t \in \nR \): infinitely many.

*Case \( k = -1 \).* Row 2 is \( (0, 0 \mid 2) \), and \( R_2 \to \tfrac12 R_2 \) makes it \( (0, 0 \mid 1) \). The last column is a pivot column, so the system is inconsistent by @thm-reading-rref (a). Directly: \( x - y = 1 \) and \( -x + y = 1 \) add up to \( 0 = 2 \).

Hence there is no solution for \( k = -1 \), there are infinitely many for \( k = 1 \), and there is exactly one otherwise. The trap is to scale by \( (1 - k^2)^{-1} \) before asking whether \( 1 - k^2 \) is zero: that step silently assumes \( k \neq \pm 1 \), and loses exactly the two interesting cases.
:::

## More unknowns than equations

Counting pivots gives a first general theorem. A matrix with \( m \) rows has at most \( m \) pivots, one per non-zero row. If there are more unknowns than that, some unknown must be free.

::: {#cor-more-unknowns-than-equations}
[More unknowns than equations]

Let \( A \in M_{m \times n}(F) \) with \( n > m \).

::: {.enumerate options="label=(\alph*)"}
1. The homogeneous system \( A\x = \0 \) has a **non-trivial** solution.
2. Consequently, every list of \( n \) vectors in \( F^m \) with \( n > m \) is linearly dependent.
:::
:::

::: {.proof}
(a) By @thm-rref-exists, \( [\, A \mid \0 \,] \) is row equivalent to a matrix \( [\, R \mid \c \,] \) in RREF. By @lem-row-ops-act-on-columns, each operation keeps the last column zero, so \( \c = \0 \), and the last column is not a pivot column. Each pivot is the leading entry of a different row, so there are at most \( m \) pivots, hence at most \( m < n \) pivot columns among the first \( n \) columns. So some \( x_l \) is a free variable. By @thm-reading-rref (b), with \( t_l = 1 \) and every other free variable \( 0 \), there is a solution whose \( l \)-th entry is \( 1 \neq 0 \). This solution is non-trivial.

(b) Let \( \v_1, \dots, \v_n \in F^m \) and let \( A \in M_{m \times n}(F) \) have these columns. By (a) there is \( \x \neq \0 \) with \( A\x = \0 \), and by @thm-matrix-times-vector-columns this says \( x_1\v_1 + \dots + x_n\v_n = \0 \) with \( x_1, \dots, x_n \) not all zero. So the list is linearly dependent.
:::

Part (b) is not new: since \( \dim F^m = m \), it is also a case of @thm-size-bounds, which rests on the Steinitz Exchange Theorem (@thm-steinitz). The proof here is independent of that one. It uses nothing from Chapter 1 beyond the definition of independence, only elimination and a count of pivots. Two proofs by different routes give some confidence that the dimension theory of Chapter 1 and the computations of this chapter will fit together, and the rest of the chapter makes that fit exact.

## Exercises

### A. Check your understanding

::: {#exr-gaussian-elimination-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. List the three types of elementary row operation, including the conditions on the scalar and on the indices.
2. Determine whether the following statement is true: "every matrix in row echelon form is in reduced row echelon form." Justify your answer.
3. Determine whether the following statement is true: "if the RREF of \( [\, A \mid \b \,] \) has a zero row, then \( A\x = \b \) is inconsistent." Justify your answer.
4. Determine whether the following statement is true: "a homogeneous system of 3 equations in 5 unknowns over \( \nR \) has infinitely many solutions." Justify your answer.
5. Explain why swapping two columns of \( A \) in \( [\, A \mid \b \,] \) is **not** a safe step when solving \( A\x = \b \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. \( R_i \leftrightarrow R_j \) with \( i \neq j \); \( R_i \to cR_i \) with \( c \neq 0 \); \( R_i \to R_i + cR_j \) with \( i \neq j \) and any \( c \in F \).
2. False. \( \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix} \) is in row echelon form, but its first pivot is \( 2 \neq 1 \), so (E3) fails; its second column also has a non-zero entry above the pivot, so (E4) fails.
3. False. A zero row is the equation \( 0 = 0 \), which every vector satisfies. Inconsistency means a row \( (0 \ \cdots \ 0 \mid 1) \) (@thm-reading-rref (a)). For example \( \left[ \begin{array}{c|c} 1 & 1 \\ 0 & 0 \end{array} \right] \) is the consistent system \( x = 1 \), \( 0 = 0 \).
4. True. By @cor-more-unknowns-than-equations (\( 5 > 3 \)) there is a non-trivial solution \( \h \), and since \( \nR \) is infinite, the multiples \( c\h \) (\( c \in \nR \)) are infinitely many distinct solutions, as in @exr-linear-systems-c1.
5. It swaps the roles of two unknowns: \( \s \) solves the new system exactly when the vector obtained from \( \s \) by swapping those two entries solves the old one. So the solution set changes, unless the swap happens to fix it. For instance \( x = 1 \), \( y = 2 \) becomes \( y = 1 \), \( x = 2 \).
:::
:::

### B. Practice

::: {#exr-gaussian-elimination-b1}
[B1: Reduce and solve]

Reduce the augmented matrix of each system over \( \nR \) to reduced row echelon form, naming each operation. Hence decide whether the system is consistent, and if so, describe all solutions.

::: {.enumerate options="label=(\alph*)"}
1. \( x_1 + 2x_2 - x_3 = 1 \), \( 2x_1 + 5x_2 + x_3 = 4 \), \( x_1 + 3x_2 + 2x_3 = 4 \).
2. \( x_1 + x_2 + 2x_3 = 3 \), \( 2x_1 + 3x_2 + 5x_3 = 7 \), \( x_1 + 2x_2 + 4x_3 = 5 \).
3. \( x_1 - x_2 + 2x_3 + x_4 = 2 \), \( 2x_1 - 2x_2 + 5x_3 + 4x_4 = 5 \), \( -x_1 + x_2 - x_3 + x_4 = -1 \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. \[
\left[ \begin{array}{ccc|c} 1 & 2 & -1 & 1 \\ 2 & 5 & 1 & 4 \\ 1 & 3 & 2 & 4 \end{array} \right]
\xrightarrow{R_2 \to R_2 - 2R_1}
\left[ \begin{array}{ccc|c} 1 & 2 & -1 & 1 \\ 0 & 1 & 3 & 2 \\ 1 & 3 & 2 & 4 \end{array} \right]
\xrightarrow{R_3 \to R_3 - R_1}
\left[ \begin{array}{ccc|c} 1 & 2 & -1 & 1 \\ 0 & 1 & 3 & 2 \\ 0 & 1 & 3 & 3 \end{array} \right]
\]
\[
\xrightarrow{R_1 \to R_1 - 2R_2}
\left[ \begin{array}{ccc|c} 1 & 0 & -7 & -3 \\ 0 & 1 & 3 & 2 \\ 0 & 1 & 3 & 3 \end{array} \right]
\xrightarrow{R_3 \to R_3 - R_2}
\left[ \begin{array}{ccc|c} 1 & 0 & -7 & -3 \\ 0 & 1 & 3 & 2 \\ 0 & 0 & 0 & 1 \end{array} \right]
\]
Column 3 gets no pivot. Column 4 has its pivot in row 3:
\[
\xrightarrow{R_1 \to R_1 + 3R_3}
\left[ \begin{array}{ccc|c} 1 & 0 & -7 & 0 \\ 0 & 1 & 3 & 2 \\ 0 & 0 & 0 & 1 \end{array} \right]
\xrightarrow{R_2 \to R_2 - 2R_3}
\left[ \begin{array}{ccc|c} 1 & 0 & -7 & 0 \\ 0 & 1 & 3 & 0 \\ 0 & 0 & 0 & 1 \end{array} \right].
\]
The last column is a pivot column, so by @thm-reading-rref (a) the system is inconsistent. (Row 3 already said \( 0 = 1 \) before the last two operations.)
2. \[
\left[ \begin{array}{ccc|c} 1 & 1 & 2 & 3 \\ 2 & 3 & 5 & 7 \\ 1 & 2 & 4 & 5 \end{array} \right]
\xrightarrow{R_2 \to R_2 - 2R_1}
\left[ \begin{array}{ccc|c} 1 & 1 & 2 & 3 \\ 0 & 1 & 1 & 1 \\ 1 & 2 & 4 & 5 \end{array} \right]
\xrightarrow{R_3 \to R_3 - R_1}
\left[ \begin{array}{ccc|c} 1 & 1 & 2 & 3 \\ 0 & 1 & 1 & 1 \\ 0 & 1 & 2 & 2 \end{array} \right]
\]
\[
\xrightarrow{R_1 \to R_1 - R_2}
\left[ \begin{array}{ccc|c} 1 & 0 & 1 & 2 \\ 0 & 1 & 1 & 1 \\ 0 & 1 & 2 & 2 \end{array} \right]
\xrightarrow{R_3 \to R_3 - R_2}
\left[ \begin{array}{ccc|c} 1 & 0 & 1 & 2 \\ 0 & 1 & 1 & 1 \\ 0 & 0 & 1 & 1 \end{array} \right]
\xrightarrow{R_1 \to R_1 - R_3}
\left[ \begin{array}{ccc|c} 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 1 \\ 0 & 0 & 1 & 1 \end{array} \right]
\xrightarrow{R_2 \to R_2 - R_3}
\left[ \begin{array}{ccc|c} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 \end{array} \right].
\]
Columns 1, 2, 3 are pivot columns and the last column is not, so by @thm-reading-rref (c) there is exactly one solution, \( (1, 0, 1) \). Check: \( 1 + 0 + 2 = 3 \), \( 2 + 0 + 5 = 7 \), \( 1 + 0 + 4 = 5 \).
3. \[
\left[ \begin{array}{cccc|c} 1 & -1 & 2 & 1 & 2 \\ 2 & -2 & 5 & 4 & 5 \\ -1 & 1 & -1 & 1 & -1 \end{array} \right]
\xrightarrow{R_2 \to R_2 - 2R_1}
\left[ \begin{array}{cccc|c} 1 & -1 & 2 & 1 & 2 \\ 0 & 0 & 1 & 2 & 1 \\ -1 & 1 & -1 & 1 & -1 \end{array} \right]
\xrightarrow{R_3 \to R_3 + R_1}
\left[ \begin{array}{cccc|c} 1 & -1 & 2 & 1 & 2 \\ 0 & 0 & 1 & 2 & 1 \\ 0 & 0 & 1 & 2 & 1 \end{array} \right]
\]
Column 2 has only zeros below row 1, so no pivot. Column 3 has its pivot in row 2:
\[
\xrightarrow{R_1 \to R_1 - 2R_2}
\left[ \begin{array}{cccc|c} 1 & -1 & 0 & -3 & 0 \\ 0 & 0 & 1 & 2 & 1 \\ 0 & 0 & 1 & 2 & 1 \end{array} \right]
\xrightarrow{R_3 \to R_3 - R_2}
\left[ \begin{array}{cccc|c} 1 & -1 & 0 & -3 & 0 \\ 0 & 0 & 1 & 2 & 1 \\ 0 & 0 & 0 & 0 & 0 \end{array} \right].
\]
Columns 4 and 5 have only a \( 0 \) in row 3, so this is the RREF. The pivot columns are 1 and 3; the free variables are \( x_2 = s \) and \( x_4 = t \). By @thm-reading-rref (b), \( x_1 = s + 3t \) and \( x_3 = 1 - 2t \). Hence the solution set is
\[
\{ (0, 0, 1, 0) + s(1, 1, 0, 0) + t(3, 0, -2, 1) : s, t \in \nR \}.
\]
:::
:::

::: {#exr-gaussian-elimination-b2}
[B2: A parameter]

For which \( k \in \nR \) is the system
\[
x + y - z = 2, \qquad x + 2y + z = 3, \qquad x + y + (k^2 - 5)z = k
\]
inconsistent, which give exactly one solution, and which give infinitely many? Justify your answer, and find the solutions when they exist.
:::

::: {.solution}
\[
\left[ \begin{array}{ccc|c} 1 & 1 & -1 & 2 \\ 1 & 2 & 1 & 3 \\ 1 & 1 & k^2 - 5 & k \end{array} \right]
\xrightarrow{R_2 \to R_2 - R_1}
\left[ \begin{array}{ccc|c} 1 & 1 & -1 & 2 \\ 0 & 1 & 2 & 1 \\ 1 & 1 & k^2 - 5 & k \end{array} \right]
\xrightarrow{R_3 \to R_3 - R_1}
\left[ \begin{array}{ccc|c} 1 & 1 & -1 & 2 \\ 0 & 1 & 2 & 1 \\ 0 & 0 & k^2 - 4 & k - 2 \end{array} \right]
\xrightarrow{R_1 \to R_1 - R_2}
\left[ \begin{array}{ccc|c} 1 & 0 & -3 & 1 \\ 0 & 1 & 2 & 1 \\ 0 & 0 & k^2 - 4 & k - 2 \end{array} \right].
\]
Whether column 3 gets a pivot depends on whether \( k^2 - 4 = (k - 2)(k + 2) \) is zero.

*Case \( k \neq \pm 2 \).* Then \( k^2 - 4 \neq 0 \), and \( R_3 \to (k^2 - 4)^{-1}R_3 \) turns row 3 into \( (0, 0, 1 \mid \tfrac{1}{k + 2}) \), since \( \tfrac{k - 2}{(k - 2)(k + 2)} = \tfrac{1}{k + 2} \). Then \( R_1 \to R_1 + 3R_3 \) and \( R_2 \to R_2 - 2R_3 \) give the RREF \( [\, I_3 \mid \c \,] \) with
\[
\c = \left( \frac{k + 5}{k + 2},\ \frac{k}{k + 2},\ \frac{1}{k + 2} \right),
\]
using \( 1 + \tfrac{3}{k + 2} = \tfrac{k + 5}{k + 2} \) and \( 1 - \tfrac{2}{k + 2} = \tfrac{k}{k + 2} \). By @thm-reading-rref (c) there is exactly one solution, \( \c \).

*Case \( k = 2 \).* Row 3 is zero, and the matrix is in RREF with pivot columns 1, 2 and free variable \( z = t \). The solutions are \( (1 + 3t, 1 - 2t, t) \), \( t \in \nR \): infinitely many.

*Case \( k = -2 \).* Row 3 is \( (0, 0, 0 \mid -4) \), and \( R_3 \to -\tfrac14 R_3 \) makes it \( (0, 0, 0 \mid 1) \). The last column is a pivot column, so the system is inconsistent.

Hence: inconsistent for \( k = -2 \), infinitely many solutions for \( k = 2 \), and exactly one solution otherwise.
:::

::: {#exr-gaussian-elimination-b3}
[B3: Over \( \nF_3 \)]

Solve each system over \( \nF_3 \) by reducing to RREF, naming each operation, and list all solutions.

::: {.enumerate options="label=(\alph*)"}
1. \( x + 2y + z = 1 \), \( 2x + y + z = 0 \), \( x + z = 2 \).
2. \( x + y + 2z = 1 \), \( 2x + z = 2 \).
:::
:::

::: {.solution}
In \( \nF_3 \) the inverses are \( 1^{-1} = 1 \) and \( 2^{-1} = 2 \), since \( 2 \cdot 2 = 4 = 1 \), and \( -1 = 2 \), \( -2 = 1 \).

::: {.enumerate options="label=(\alph*)"}
1. \[
\left[ \begin{array}{ccc|c} 1 & 2 & 1 & 1 \\ 2 & 1 & 1 & 0 \\ 1 & 0 & 1 & 2 \end{array} \right]
\xrightarrow{R_2 \to R_2 - 2R_1}
\left[ \begin{array}{ccc|c} 1 & 2 & 1 & 1 \\ 0 & 0 & 2 & 1 \\ 1 & 0 & 1 & 2 \end{array} \right]
\xrightarrow{R_3 \to R_3 - R_1}
\left[ \begin{array}{ccc|c} 1 & 2 & 1 & 1 \\ 0 & 0 & 2 & 1 \\ 0 & 1 & 0 & 1 \end{array} \right]
\]
Here \( 1 - 4 = -3 = 0 \), \( 1 - 2 = -1 = 2 \), \( 0 - 2 = 1 \), and \( 0 - 2 = 1 \), \( 2 - 1 = 1 \). Column 2 has entries \( 0, 1 \) below row 1, so we swap:
\[
\xrightarrow{R_2 \leftrightarrow R_3}
\left[ \begin{array}{ccc|c} 1 & 2 & 1 & 1 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 2 & 1 \end{array} \right]
\xrightarrow{R_1 \to R_1 - 2R_2}
\left[ \begin{array}{ccc|c} 1 & 0 & 1 & 2 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 2 & 1 \end{array} \right]
\xrightarrow{R_3 \to 2R_3}
\left[ \begin{array}{ccc|c} 1 & 0 & 1 & 2 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 2 \end{array} \right]
\xrightarrow{R_1 \to R_1 - R_3}
\left[ \begin{array}{ccc|c} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 2 \end{array} \right].
\]
There are no free variables, so the unique solution is \( (0, 1, 2) \). Check: \( 0 + 2 + 2 = 4 = 1 \), \( 0 + 1 + 2 = 3 = 0 \), \( 0 + 2 = 2 \).
2. \[
\left[ \begin{array}{ccc|c} 1 & 1 & 2 & 1 \\ 2 & 0 & 1 & 2 \end{array} \right]
\xrightarrow{R_2 \to R_2 - 2R_1}
\left[ \begin{array}{ccc|c} 1 & 1 & 2 & 1 \\ 0 & 1 & 0 & 0 \end{array} \right]
\xrightarrow{R_1 \to R_1 - R_2}
\left[ \begin{array}{ccc|c} 1 & 0 & 2 & 1 \\ 0 & 1 & 0 & 0 \end{array} \right],
\]
using \( 0 - 2 = 1 \), \( 1 - 4 = 0 \), \( 2 - 2 = 0 \). The free variable is \( z = t \), and \( x = 1 - 2t = 1 + t \), \( y = 0 \). As \( t \) runs through \( 0, 1, 2 \), the solutions are \( (1, 0, 0) \), \( (2, 0, 1) \), \( (0, 0, 2) \): exactly three.
:::
:::

### C. Going deeper

::: {#exr-gaussian-elimination-c1}
[C1: Why \( i \neq j \)?]

Consider the move "\( R_i \to R_i + cR_i \)", which the definition does **not** allow.

::: {.enumerate options="label=(\alph*)"}
1. Show that for \( c = -1 \) this move is not reversible: give a matrix on which its effect cannot be undone by any sequence of elementary row operations and moves of this kind, and a system whose solution set it changes.
2. Show that for \( c \neq -1 \) the move is an elementary row operation of another type. Explain why the condition \( i \neq j \) in type (3) therefore loses nothing.
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. The move replaces \( \r_i \) by \( \r_i + (-1)\r_i = \0 \). Apply it to the \( 1 \times 2 \) augmented matrix \( [\, 1 \mid 1 \,] \) of the equation \( x = 1 \) over any field \( F \): the result is \( [\, 0 \mid 0 \,] \), the equation \( 0 = 0 \). The solution set changes from \( \{ 1 \} \) to all of \( F \). No sequence of moves can return to \( [\, 1 \mid 1 \,] \): every elementary row operation, and every move "\( R_i \to R_i + cR_i \)", sends a zero matrix to a zero matrix, by the formulas in the proof of @lem-row-ops-act-on-columns and \( c \cdot 0 = 0 \).
2. The move replaces \( \r_i \) by \( (1 + c)\r_i \). If \( c \neq -1 \), then \( 1 + c \neq 0 \), and this is the scaling \( R_i \to (1 + c)R_i \), an operation of type (2). So allowing \( i = j \) in type (3) would add only moves that are already available (when \( c \neq -1 \)) and one move that destroys information (\( c = -1 \)). Requiring \( i \neq j \) excludes exactly the bad case.
:::
:::

::: {#exr-gaussian-elimination-c2}
[C2: The cost of elimination]

Let \( A \in M_n(F) \) and \( \b \in F^n \), and suppose that Gauss–Jordan elimination on \( [\, A \mid \b \,] \) finds, for each \( l = 1, \dots, n \), a non-zero entry in position \( (l, l) \) and so never swaps. Count as one **operation** each multiplication or division of two scalars, under these conventions: scaling row \( l \) costs one division for each entry in columns \( l + 1, \dots, n + 1 \) (the pivot is simply set to \( 1 \)), and each replacement \( R_g \to R_g - cR_l \) costs one multiplication for each entry in columns \( l + 1, \dots, n + 1 \) (the entry in column \( l \) is simply set to \( 0 \)).

::: {.enumerate options="label=(\alph*)"}
1. Show that processing column \( l \) costs at most \( n(n + 1 - l) \) operations.
2. Hence show that the whole elimination costs at most \( \tfrac12 (n^3 + n^2) \) operations.
3. Roughly how many times more work is a system of \( 2n \) equations than one of \( n \) equations, for large \( n \)?
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Scaling row \( l \) costs \( n + 1 - l \) divisions. At most \( n - 1 \) other rows need a replacement, each costing \( n + 1 - l \) multiplications. The total is at most \( (n + 1 - l) + (n - 1)(n + 1 - l) = n(n + 1 - l) \).
2. Summing (a) over \( l = 1, \dots, n \), and substituting \( q = n + 1 - l \), which runs through \( 1, \dots, n \),
\[
\sum_{l=1}^{n} n(n + 1 - l) = n \sum_{q=1}^{n} q = n \cdot \frac{n(n + 1)}{2} = \frac{n^3 + n^2}{2},
\]
using the formula for \( 1 + \dots + n \) (@prp-sum-first-n).
3. The bound is dominated by \( \tfrac12 n^3 \) for large \( n \), since \( \tfrac12 n^2 \) is small compared with it. Replacing \( n \) by \( 2n \) multiplies \( n^3 \) by \( 8 \), so doubling the size of the system costs roughly eight times as much.
:::
:::

::: {#exr-gaussian-elimination-c3}
[C3: Solvable for every right-hand side]

Let \( A \in M_{m \times n}(F) \), and suppose that \( A\x = \b \) is consistent for **every** \( \b \in F^m \). Prove that \( m \le n \).

*Hint: suppose \( m > n \), reduce \( A \) to its RREF \( R \), and run the operations backwards on \( [\, R \mid \e_m \,] \).*
:::

::: {.solution}
Suppose, for a contradiction, that \( m > n \). By @thm-rref-exists, some sequence of operations \( O_1, \dots, O_s \) turns \( A \) into a matrix \( R \) in RREF. By (E2), \( R \) has at most \( n \) pivots, one in each pivot column, so at most \( n < m \) non-zero rows, and by (E1) its last row is zero. Therefore the last row of \( [\, R \mid \e_m \,] \) is \( (0 \ \cdots \ 0 \mid 1) \), so the system \( R\x = \e_m \) has no solution.

By @thm-row-ops-preserve-solutions (a), each \( O_t \) is undone by an operation \( O'_t \), and \( O'_s, \dots, O'_1 \) turn \( R \) back into \( A \). Apply them to \( [\, R \mid \e_m \,] \). By @lem-row-ops-act-on-columns they act on the two blocks separately, so the result is \( [\, A \mid \b \,] \) for some \( \b \in F^m \). By @thm-row-ops-preserve-solutions (c), \( A\x = \b \) has the same solutions as \( R\x = \e_m \), namely none. This contradicts the hypothesis, so \( m \le n \).
:::
