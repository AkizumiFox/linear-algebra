# Row Space, Column Space, Null Space and Rank

We can now reduce any matrix and read off the solutions of any linear system. This section asks a coarser question: how much information does a matrix carry? Three subspaces come attached to every matrix \( \A \): the vectors \( \A\x \) it can produce, the combinations of its rows, and the vectors it sends to zero. Their dimensions are governed by a single number, the rank, which is the number of pivots. With it we settle when a system is solvable and how many solutions it has, and we turn the questions of Chapter 1 about vectors in \( F^m \) (independent? spanning? a basis of a sum or an intersection?) into a routine computation, which is the "systematic method" that Chapter 1 promised.

Throughout, \( F \) is a field and \( \A \in M_{m \times n}(F) \) has columns \( \a_1, \dots, \a_n \in F^m \).

## Three subspaces of a matrix

Here is the matrix we will follow through the section:
\[
\A = \begin{pmatrix} 1 & 2 & 0 & 0 & -1 \\ 2 & 4 & 1 & 0 & 0 \\ 1 & 2 & 1 & 1 & 2 \\ 0 & 0 & 1 & 1 & 3 \end{pmatrix} \in M_{4 \times 5}(\nR).
\]
Three questions about it have come up in this chapter, and each answer is a set. For which \( \b \in \nR^4 \) can we solve \( \A\x = \b \)? By @thm-consistent-iff-column-span, exactly for \( \b \) in the span of the columns. Which \( \x \in \nR^5 \) solve \( \A\x = \0 \)? By @thm-homogeneous-solutions-subspace, a subspace of \( \nR^5 \). And which new equations can we derive from the four by adding multiples of them? Their left-hand sides are exactly the combinations of the rows. These three sets recur so often that they get names.

*The column space is everything \( \A \) can produce, the null space is everything \( \A \) kills, and the row space is every left-hand side we can build from the equations of \( \A\x = \b \).*

::: {#def-column-space}
[Column space]

The **column space** of \( \A \in M_{m \times n}(F) \) is the span of its columns,
\[
\col(\A) \coloneqq \Span(\a_1, \dots, \a_n) = \{ \A\x : \x \in F^n \} \subseteq F^m .
\]
:::

::: {#def-row-space}
[Row space]

The **row space** of \( \A \in M_{m \times n}(F) \) is the span of its rows,
\[
\row(\A) \coloneqq \Span(\text{row } 1, \dots, \text{row } m) \subseteq M_{1 \times n}(F) .
\]
:::

::: {#def-null-space}
[Null space]

The **null space** of \( \A \in M_{m \times n}(F) \) is the solution set of the homogeneous system,
\[
\nul(\A) \coloneqq \{ \x \in F^n : \A\x = \0 \} \subseteq F^n .
\]
:::

In words: \( \col(\A) \) lives among the **outputs**, in \( F^m \) (one entry per row); \( \nul(\A) \) lives among the **inputs**, in \( F^n \) (one entry per column); and \( \row(\A) \) consists of row vectors of length \( n \). The two descriptions of \( \col(\A) \) agree by @thm-matrix-times-vector-columns: \( \A\x = x_1\a_1 + \dots + x_n\a_n \), and as \( \x \) runs over \( F^n \) these are all the combinations of the columns.

**Well-definedness.** All three are subspaces. \( \col(\A) \) and \( \row(\A) \) are spans, hence subspaces by @thm-span-subspace, of \( F^m \) and of \( M_{1 \times n}(F) \) respectively. \( \nul(\A) \) is a subspace of \( F^n \) by @thm-homogeneous-solutions-subspace. The row vectors \( M_{1 \times n}(F) \) form an \( n \)-dimensional space, with the standard basis \( \e_1\tp, \dots, \e_n\tp \) (@exm-dimensions). Transposing turns row vectors into columns and respects sums and scalar multiples (@thm-transpose-properties), so it sends a combination of rows to the same combination of their transposes, and only the zero row transposes to \( \0 \). The transposes of the rows of \( \A \) are the columns of \( \A\tp \). Hence transposing sends \( \row(\A) \) onto \( \col(\A\tp) \), a list of rows is independent exactly when the list of their transposes is, and transposing a basis of \( \row(\A) \) gives a basis of \( \col(\A\tp) \). Therefore
\[
\dim \row(\A) = \dim \col(\A\tp). \tag{$\ast$}
\]

**Examples.**

- **The identity.** \( \col(\I_n) = F^n \), since the columns \( \e_1, \dots, \e_n \) span; \( \row(\I_n) = M_{1 \times n}(F) \); and \( \nul(\I_n) = \{\0\} \), since \( \I_n\x = \x \).
- **The zero matrix** is the degenerate case. For \( 0 = 0_{m \times n} \), \( \col(0) = \Span(\0, \dots, \0) = \{\0\} \), \( \row(0) = \{0\} \), and \( \nul(0) = F^n \), since every \( \x \) is killed. It carries no information, and its column space is as small as possible while its null space is as large as possible. We will see that this trade-off is exact.
- **A single row.** For \( \A = \begin{pmatrix} 1 & 1 & -1 \end{pmatrix} \in M_{1 \times 3}(\nR) \), the columns are the scalars \( 1, 1, -1 \in \nR^1 \), so \( \col(\A) = \nR^1 \), \( \row(\A) = \Span\bigl(\begin{pmatrix} 1 & 1 & -1 \end{pmatrix}\bigr) \) is a line of row vectors, and \( \nul(\A) \) is the plane \( x + y - z = 0 \) in \( \nR^3 \).

**Non-example by minimal change.** Replace \( \0 \) by a non-zero right-hand side: the solution set \( \{ \x \in F^n : \A\x = \b \} \) with \( \b \neq \0 \). It is described by the same equations, and it is still of the form \( \p + \nul(\A) \) when non-empty (@thm-general-solution-structure). But it does not contain \( \0 \), since \( \A\0 = \0 \neq \b \), so it fails the first condition of @thm-subspace-test.

::: {.warning}
The three spaces live in **different places**. For \( \A \in M_{4 \times 5}(\nR) \) above, \( \col(\A) \subseteq \nR^4 \) but \( \nul(\A) \subseteq \nR^5 \), so a statement such as "\( \nul(\A) \subseteq \col(\A) \)" does not even make sense. Keep track by size: \( \A\x \) needs \( \x \) with \( n \) entries and returns a vector with \( m \) entries.
:::

## Rank and nullity

The column space measures how much \( \A \) can reach, and the null space how much it collapses. We measure each by its dimension. Both are subspaces of finite-dimensional spaces, so both have a dimension by @thm-subspace-dimension.

*The rank counts the independent directions that \( \A \) can produce.*

::: {#def-rank-matrix}
[Rank of a matrix]

The **rank** of \( \A \in M_{m \times n}(F) \) is \( \rank \A \coloneqq \dim \col(\A) \).
:::

::: {#def-nullity-matrix}
[Nullity of a matrix]

The **nullity** of \( \A \in M_{m \times n}(F) \) is \( \nullity \A \coloneqq \dim \nul(\A) \).
:::

From the examples above: \( \rank \I_n = n \) and \( \nullity \I_n = 0 \); \( \rank 0_{m \times n} = 0 \) and \( \nullity 0_{m \times n} = n \); and \( \rank \begin{pmatrix} 1 & 1 & -1 \end{pmatrix} = 1 \), with nullity \( 2 \). In each case rank plus nullity equals the number of columns. Two simple bounds hold at once: \( \rank \A \le m \), because \( \col(\A) \subseteq F^m \), and \( \rank \A \le n \), because \( \col(\A) \) is spanned by \( n \) vectors (@thm-size-bounds). Why define rank through columns and not rows? We could have, and one of the main theorems of this section says the answer would be the same.

## What row operations preserve

To compute these spaces we will row reduce. So we first ask what a row operation does to each of them. Recall from @thm-row-equivalent-iff-invertible-multiple that \( \A \) is row equivalent to \( \B \) exactly when \( \B = \E\A \) with \( \E \in M_m(F) \) invertible; since row equivalence is symmetric (@thm-row-ops-preserve-solutions (b)), we may simply say that \( \A \) and \( \B \) are row equivalent.

::: {#thm-row-ops-row-space}
[Row operations and the three spaces]

Let \( \A, \B \in M_{m \times n}(F) \) be row equivalent. Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \row(\B) = \row(\A) \);
2. \( \nul(\B) = \nul(\A) \). Equivalently, writing \( \b_1, \dots, \b_n \) for the columns of \( \B \): for all \( c_1, \dots, c_n \in F \), the columns of \( \A \) satisfy \( c_1\a_1 + \dots + c_n\a_n = \0 \) if and only if the columns of \( \B \) satisfy \( c_1\b_1 + \dots + c_n\b_n = \0 \);
3. but \( \col(\B) \) and \( \col(\A) \) **need not** be equal.
:::
:::

::: {.proof}
(a) Write \( \B = \E\A \) with \( \E \) invertible, by @thm-row-equivalent-iff-invertible-multiple. By @thm-three-views-of-product, row \( i \) of \( \E\A \) is \( (\text{row } i \text{ of } \E)\A \), which by @thm-matrix-times-vector-columns (rows version) is a combination of the rows of \( \A \). So every row of \( \B \) lies in \( \row(\A) \), and \( \row(\B) \subseteq \row(\A) \) by @prp-span-basic-properties (1). Since \( \A = \E^{-1}\B \) with \( \E^{-1} \) invertible, the same argument gives \( \row(\A) \subseteq \row(\B) \).

(b) The equality \( \nul(\B) = \nul(\A) \) is @lem-row-equivalent-same-null-space. By @thm-matrix-times-vector-columns, \( c_1\a_1 + \dots + c_n\a_n = \A\c \) and \( c_1\b_1 + \dots + c_n\b_n = \B\c \) with \( \c = (c_1, \dots, c_n) \), so the second statement is the first one written out (this is @lem-row-ops-preserve-column-relations).

(c) Let \( \A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \in M_2(\nR) \) and \( \B = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix} \), obtained by \( R_2 \to R_2 - R_1 \). Then \( \col(\A) = \Span((1, 1)) \) and \( \col(\B) = \Span((1, 0)) \). These lines differ, since \( (1, 0) \) is not a multiple of \( (1, 1) \).
:::

So row reduction keeps the row space and the **relations among the columns**, but it moves the columns themselves.

::: {.warning}
**Do not read \( \col(\A) \) off the reduced form.** In (c) above, the RREF of \( \A \) is \( \B \), whose column space is the \( x \)-axis, while \( \col(\A) \) is the line \( y = x \). What survives row reduction is the *pattern* of dependence: in both matrices column 2 equals column 1. So we use the RREF to decide **which** columns to take, and then take those columns **from \( \A \)**.
:::

## Bases from the reduced form

Fix the notation for the rest of the section. Let \( \R = (r_{kj}) \) be the reduced row echelon form of \( \A \) (@thm-rref-exists, @thm-rref-unique), with columns \( \r_1, \dots, \r_n \in F^m \). Let \( \R \) have \( r \) non-zero rows, and let the pivot of row \( k \) lie in column \( j_k \), so that \( j_1 < j_2 < \dots < j_r \). These are the **pivot columns** of \( \A \), well defined by @cor-pivot-columns-well-defined. The remaining columns are the **free columns**. We use three facts from @def-reduced-row-echelon-form:

- rows \( r + 1, \dots, m \) of \( \R \) are zero;
- column \( j_k \) of \( \R \) is \( \e_k \) (the pivot is \( 1 \) and the only non-zero entry of its column);
- in row \( k \), every entry to the left of the pivot is \( 0 \).

From the last two, if column \( j \) of \( \R \) has exactly \( t \) pivot columns to its left, then **every entry of \( \r_j \) in rows \( t + 1, \dots, m \) is zero, except the pivot entry of row \( t + 1 \) when \( j = j_{t+1} \)**. Indeed, for \( k \ge t + 1 \), row \( k \) is either zero or has its pivot in column \( j_k \ge j \), and entries to the left of a pivot vanish. In the running example,
\[
\R = \begin{pmatrix} 1 & 2 & 0 & 0 & -1 \\ 0 & 0 & 1 & 0 & 2 \\ 0 & 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix},
\]
with \( r = 3 \), pivot columns \( 1, 3, 4 \) and free columns \( 2, 5 \) (the reduction is carried out in @exm-bases-of-three-subspaces below).

The column space comes first. In \( \R \) the answer is visible: the pivot columns are \( \e_1, \dots, \e_r \), and every column has zeros below row \( r \). Row reduction does not preserve columns, but by @thm-row-ops-row-space (b) it preserves every linear relation among them, and "is a basis" and "equals this combination" are statements about relations.

::: {#thm-basis-column-space}
[Pivot columns form a basis of the column space]

Let \( \A \in M_{m \times n}(F) \) have pivot columns \( j_1 < \dots < j_r \), and let \( \R = (r_{kj}) \) be its RREF. Then:

::: {.enumerate options="label=(\alph*)"}
1. the pivot columns **of \( \A \)**, \( (\a_{j_1}, \dots, \a_{j_r}) \), form a basis of \( \col(\A) \);
2. if column \( j \) is free and \( t \) pivot columns lie to its left, then \( \a_j = r_{1j}\a_{j_1} + \dots + r_{tj}\a_{j_t} \);
3. the pivot columns of \( \A \) are exactly the vectors kept when \( (\a_1, \dots, \a_n) \) is sifted as in @thm-sift.
:::
:::

::: {.idea}
Both claims are statements about linear relations among columns, so by @thm-row-ops-row-space (b) it suffices to prove them for \( \R \), where they can be seen by inspection. The pivot columns of \( \R \) are \( \e_1, \dots, \e_r \), which are independent. A free column of \( \R \) is \( \sum_k r_{kj}\e_k \), a combination of the pivot columns to its left with its own entries as coefficients. So we transfer two relations back to \( \A \): "\( \sum c_k \a_{j_k} = \0 \) forces \( c_1 = \dots = c_r = 0 \)" and "\( \a_j - \sum_k r_{kj}\a_{j_k} = \0 \)". Part (c) is a rereading of @cor-pivot-columns-well-defined.
:::

::: {.proof}
Throughout, we use @thm-row-ops-row-space (b) in the form: for scalars \( c_1, \dots, c_n \),
\[
c_1\a_1 + \dots + c_n\a_n = \0 \iff c_1\r_1 + \dots + c_n\r_n = \0 . \tag{$\dagger$}
\]

(b) Let column \( j \) be free, with \( t \) pivot columns \( j_1, \dots, j_t \) to its left. By the fact in bold before the theorem, the entries of \( \r_j \) in rows \( t + 1, \dots, m \) are zero, so \( \r_j = r_{1j}\e_1 + \dots + r_{tj}\e_t = r_{1j}\r_{j_1} + \dots + r_{tj}\r_{j_t} \), since \( \r_{j_k} = \e_k \). This is a linear relation among the columns of \( \R \) with coefficient \( 1 \) on \( \r_j \), \( -r_{kj} \) on \( \r_{j_k} \), and \( 0 \) elsewhere. By \( (\dagger) \), the columns of \( \A \) satisfy the same relation, which is (b).

(a) *Spanning.* Each pivot column \( \a_{j_k} \) lies in \( \Span(\a_{j_1}, \dots, \a_{j_r}) \), and each free column does by (b). Hence \( \col(\A) = \Span(\a_1, \dots, \a_n) \subseteq \Span(\a_{j_1}, \dots, \a_{j_r}) \) by @prp-span-basic-properties (1). The reverse inclusion holds by @prp-span-basic-properties (2), since the pivot columns are among the columns.

*Independence.* Let \( c_1\a_{j_1} + \dots + c_r\a_{j_r} = \0 \). This is a relation among all the columns of \( \A \) with coefficient \( 0 \) on the free columns. By \( (\dagger) \), \( c_1\r_{j_1} + \dots + c_r\r_{j_r} = c_1\e_1 + \dots + c_r\e_r = \0 \). The \( k \)-th entry of the left side is \( c_k \), so \( c_1 = \dots = c_r = 0 \). Hence the pivot columns of \( \A \) are linearly independent, and with spanning they form a basis of \( \col(\A) \) by @def-basis.

(c) By @cor-pivot-columns-well-defined (a), column \( j \) is a pivot column if and only if \( \a_j \notin \Span(\a_1, \dots, \a_{j-1}) \). Sifting keeps \( \a_j \) exactly when \( \a_j \) is not in the span of the vectors kept before it, and by @thm-sift (applied to \( (\a_1, \dots, \a_{j-1}) \)) that span is \( \Span(\a_1, \dots, \a_{j-1}) \). Hence the kept vectors are exactly the pivot columns. This proves the theorem.
:::

This is sifting (@thm-sift) done by elimination. In Chapter 1, each step "is \( \v_j \) in the span of the vectors kept so far?" was a separate small system. One row reduction answers all of them at once, and part (b) even gives the coefficients.

The row space and the null space are read off \( \R \) directly.

::: {#thm-basis-row-space}
[Basis of the row space]

The non-zero rows of the RREF \( \R \) of \( \A \) form a basis of \( \row(\A) \).
:::

::: {.proof}
By @thm-row-ops-row-space (a), \( \row(\A) = \row(\R) \). The zero rows of \( \R \) contribute nothing to a combination, so the \( r \) non-zero rows span \( \row(\R) \). For independence, let \( c_1(\text{row } 1) + \dots + c_r(\text{row } r) = 0 \). Look at the entry in column \( j_k \): since column \( j_k \) of \( \R \) is \( \e_k \), only row \( k \) has a non-zero entry there, equal to \( 1 \). So that entry of the combination is \( c_k \), and \( c_k = 0 \) for each \( k \). Hence the non-zero rows are a basis of \( \row(\A) \).
:::

For the null space, each free variable gets one basis vector: set that free variable to \( 1 \), the other free variables to \( 0 \), and solve for the pivot variables.

::: {#thm-basis-null-space}
[Basis of the null space]

Let \( \A \in M_{m \times n}(F) \) have RREF \( \R = (r_{kj}) \) with pivot columns \( j_1 < \dots < j_r \). For each free column \( f \), define \( \s_f \in F^n \) by
\[
\begin{aligned}
(\s_f)_f &= 1, \\
(\s_f)_{f'} &= 0 \text{ for every other free } f', \\
(\s_f)_{j_k} &= -r_{kf} \text{ for } k = 1, \dots, r .
\end{aligned}
\]
Then the vectors \( \s_f \), one for each free column \( f \), form a basis of \( \nul(\A) \). In particular \( \nullity \A = n - r \), the number of free columns.
:::

::: {.proof}
By @thm-row-ops-row-space (b), \( \nul(\A) = \nul(\R) \). For \( k \le r \), row \( k \) of \( \R \) has entry \( 1 \) in column \( j_k \), entry \( 0 \) in every other pivot column (since column \( j_{k'} \) is \( \e_{k'} \)), and entries \( r_{kf} \) in the free columns. Rows \( k > r \) are zero. Hence \( \R\x = \0 \) is equivalent to the \( r \) equations
\[
x_{j_k} = -\sum_{f \text{ free}} r_{kf}\, x_f \qquad (k = 1, \dots, r). \tag{$\ddagger$}
\]
*Spanning.* Let \( \x \in \nul(\A) \), and put \( \y = \sum_{f \text{ free}} x_f \s_f \). For a free column \( f \), the \( f \)-th entry of \( \y \) is \( x_f \), since \( \s_f \) has a \( 1 \) there and the other \( \s_{f'} \) have \( 0 \). For a pivot column, the \( j_k \)-th entry of \( \y \) is \( \sum_f x_f(-r_{kf}) \), which equals \( x_{j_k} \) by \( (\ddagger) \). So \( \x = \y \) lies in the span of the \( \s_f \). Each \( \s_f \) itself satisfies \( (\ddagger) \), so it lies in \( \nul(\A) \).

*Independence.* If \( \sum_f c_f\s_f = \0 \), then the \( f \)-th entry of the left side is \( c_f \), so every \( c_f = 0 \).

Hence the \( \s_f \) form a basis of \( \nul(\A) \), and there are \( n - r \) of them.
:::

::: {#exm-bases-of-three-subspaces}
[Bases for the running example]

Find bases of \( \col(\A) \), \( \row(\A) \) and \( \nul(\A) \), and the rank and nullity, for
\[
\A = \begin{pmatrix} 1 & 2 & 0 & 0 & -1 \\ 2 & 4 & 1 & 0 & 0 \\ 1 & 2 & 1 & 1 & 2 \\ 0 & 0 & 1 & 1 & 3 \end{pmatrix} \in M_{4 \times 5}(\nR).
\]
:::

::: {.solution}
Row reduce:
\[
\begin{aligned}
\A \xrightarrow[R_3 \to R_3 - R_1]{R_2 \to R_2 - 2R_1}
\begin{pmatrix} 1 & 2 & 0 & 0 & -1 \\ 0 & 0 & 1 & 0 & 2 \\ 0 & 0 & 1 & 1 & 3 \\ 0 & 0 & 1 & 1 & 3 \end{pmatrix}
&\xrightarrow[R_4 \to R_4 - R_2]{R_3 \to R_3 - R_2}
\begin{pmatrix} 1 & 2 & 0 & 0 & -1 \\ 0 & 0 & 1 & 0 & 2 \\ 0 & 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 1 & 1 \end{pmatrix} \\
&\xrightarrow{R_4 \to R_4 - R_3}
\R = \begin{pmatrix} 1 & 2 & 0 & 0 & -1 \\ 0 & 0 & 1 & 0 & 2 \\ 0 & 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}.
\end{aligned}
\]
The pivot columns are \( 1, 3, 4 \), and the free columns are \( 2, 5 \).

**Column space.** By @thm-basis-column-space (a), the pivot columns **of \( \A \)**,
\[
\a_1 = (1, 2, 1, 0), \qquad \a_3 = (0, 1, 1, 1), \qquad \a_4 = (0, 0, 1, 1),
\]
form a basis of \( \col(\A) \), so \( \rank \A = 3 \). By part (b), the free columns are \( \a_2 = 2\a_1 \) (from column 2 of \( \R \)) and \( \a_5 = -\a_1 + 2\a_3 + \a_4 \) (from column 5). Check: \( -(1, 2, 1, 0) + 2(0, 1, 1, 1) + (0, 0, 1, 1) = (-1, 0, 2, 3) = \a_5 \). Note that \( \col(\A) \neq \col(\R) \): every column of \( \R \) has last entry \( 0 \), but \( \a_3 \) does not.

**Row space.** By @thm-basis-row-space, a basis is
\[
\begin{pmatrix} 1 & 2 & 0 & 0 & -1 \end{pmatrix}, \quad \begin{pmatrix} 0 & 0 & 1 & 0 & 2 \end{pmatrix}, \quad \begin{pmatrix} 0 & 0 & 0 & 1 & 1 \end{pmatrix},
\]
so \( \dim \row(\A) = 3 \).

**Null space.** The equations \( (\ddagger) \) read \( x_1 = -2x_2 + x_5 \), \( x_3 = -2x_5 \), \( x_4 = -x_5 \). By @thm-basis-null-space, a basis is
\[
\s_2 = (-2, 1, 0, 0, 0), \qquad \s_5 = (1, 0, -2, -1, 1),
\]
so \( \nullity \A = 2 \). Check: \( \A\s_2 = -2\a_1 + \a_2 = \0 \) and \( \A\s_5 = \a_1 - 2\a_3 - \a_4 + \a_5 = \0 \), which are the two relations found above.

So \( \rank \A = \dim \row(\A) = 3 \) and \( \rank \A + \nullity \A = 5 \), the number of columns.
:::

::: {.check}
Without computing anything, what is the largest possible rank of a \( 3 \times 5 \) matrix, and the smallest possible nullity?
:::

::: {.solution}
\( \rank \A = \dim \col(\A) \le 3 \), since \( \col(\A) \subseteq F^3 \). By @thm-basis-null-space, the nullity is the number of free columns, \( 5 - r \), where \( r \le 3 \) is the number of pivots (one per non-zero row). So the nullity is at least \( 2 \). For example \( \begin{pmatrix} \I_3 & 0_{3 \times 2} \end{pmatrix} \) attains rank \( 3 \) and nullity \( 2 \).
:::

## Row rank equals column rank

The example came out with \( \dim \row(\A) = \dim \col(\A) \). This is not luck, and it is surprising: the row space and the column space live in different spaces, and the rows and columns of a \( 4 \times 5 \) matrix have nothing obvious in common. Counting pivots explains it.

::: {#thm-row-rank-equals-column-rank}
[Row rank equals column rank]

Let \( \A \in M_{m \times n}(F) \), and let \( r \) be the number of pivots of its RREF. Then
\[
\dim \row(\A) = \dim \col(\A) = r .
\]
Consequently \( \rank \A = \rank \A\tp \).
:::

::: {.proof}
By @thm-basis-column-space (a), \( \col(\A) \) has a basis consisting of the \( r \) pivot columns, so \( \dim \col(\A) = r \). By @thm-basis-row-space, \( \row(\A) \) has a basis consisting of the non-zero rows of the RREF. Each non-zero row contains exactly one pivot and each pivot lies in a non-zero row, so there are \( r \) of them, and \( \dim \row(\A) = r \). Finally, by \( (\ast) \) at the start of this section, \( \rank \A\tp = \dim \col(\A\tp) = \dim \row(\A) = r = \rank \A \).
:::

The theorem makes the rank independent of **which** echelon form we compute. Gaussian elimination without the final clearing-up phase produces an echelon form that is not reduced, and different sequences of operations produce different echelon forms. They all give the same count.

::: {#cor-rank-from-any-echelon-form}
[Rank from any echelon form]

Let \( \A \in M_{m \times n}(F) \), and let \( \G \) be a matrix in row echelon form that is row equivalent to \( \A \). Then the number of non-zero rows of \( \G \) is \( \rank \A \), and the columns of \( \G \) containing its pivots are exactly the pivot columns of \( \A \).
:::

::: {.proof}
By @cor-pivot-columns-well-defined (b), the pivot columns of \( \G \) are the pivot columns of \( \A \). Each non-zero row of \( \G \) has exactly one pivot, in a different column (@def-row-echelon-form), so the number of non-zero rows of \( \G \) equals the number of pivot columns of \( \A \), which is \( \rank \A \) by @thm-row-rank-equals-column-rank.
:::

::: {.warning}
Rank is a property of \( \A \), not of a computation, but it must be counted from a row echelon form. The number of non-zero rows of \( \A \) itself is not the rank: \( \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} \) has two non-zero rows and rank \( 1 \). Count non-zero rows only after reaching an echelon form. And the rank depends on the field when the entries are read in different fields: \( \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \) has rank \( 2 \) over \( \nR \), but over \( \nF_2 \), where \( -1 = 1 \), both rows are \( \begin{pmatrix} 1 & 1 \end{pmatrix} \) and the rank is \( 1 \).
:::

## Rank–nullity and the Rouché–Capelli theorem

The trade-off between the zero matrix and the identity was exact, and now we can say why.

::: {#thm-rank-nullity-matrix}
[Rank–Nullity for Matrices]

For every \( \A \in M_{m \times n}(F) \),
\[
\rank \A + \nullity \A = n,
\]
the number of **columns** of \( \A \).
:::

::: {.proof}
Let \( r \) be the number of pivot columns of \( \A \). By @thm-row-rank-equals-column-rank, \( \rank \A = r \). By @thm-basis-null-space, \( \nullity \A = n - r \). Adding gives \( n \).
:::

Each column of \( \A \) is either a pivot column, contributing a direction to \( \col(\A) \), or a free column, contributing a direction to \( \nul(\A) \). Nothing is lost and nothing is counted twice. In Chapter 3 the same equation becomes the Rank–Nullity Theorem for linear maps, with a proof that uses no matrices at all.

Now the question this chapter started with. When does \( \A\x = \b \) have a solution, and how many solutions are there? The first answer was \( \b \in \col(\A) \) (@thm-consistent-iff-column-span); here is a version that is a pure count.

::: {#thm-rouche-capelli}
[Rouché–Capelli Theorem]

Let \( \A \in M_{m \times n}(F) \), \( \b \in F^m \), and let \( [\A \mid \b] \in M_{m \times (n+1)}(F) \) be the augmented matrix.

::: {.enumerate options="label=(\alph*)"}
1. The system \( \A\x = \b \) is consistent if and only if \( \rank \A = \rank\,[\A \mid \b] \).
2. Suppose it is consistent, let \( \p \) be one solution, let \( r = \rank \A \), and let \( \s_1, \dots, \s_{n-r} \) be a basis of \( \nul(\A) \). Then every solution can be written as
\[
\x = \p + t_1\s_1 + \dots + t_{n-r}\s_{n-r}
\]
for **exactly one** choice of \( (t_1, \dots, t_{n-r}) \in F^{n-r} \). In words: the solutions form an \( (n - r) \)-parameter family.
3. If moreover \( F \) is a finite field with \( q \) elements (for instance \( \nF_p \), with \( q = p \)), a consistent system has exactly \( q^{\,n - \rank \A} \) solutions.
:::
:::

::: {.idea}
For (a), adding the column \( \b \) can only enlarge the column space, and the dimension goes up exactly when \( \b \) is new, that is, when \( \b \notin \col(\A) \). For (b), the structure theorem says solutions are \( \p \) plus null vectors, and null vectors have unique coordinates in a basis. For (c), unique coordinates mean the solutions are in bijection with \( F^{n-r} \), which has \( q^{n-r} \) elements.
:::

::: {.proof}
(a) By @def-column-space, \( \col([\A \mid \b]) = \Span(\a_1, \dots, \a_n, \b) \), which contains \( \col(\A) \) by @prp-span-basic-properties (2).

\( (\Rightarrow) \) Suppose the system is consistent. By @thm-consistent-iff-column-span, \( \b \in \Span(\a_1, \dots, \a_n) \), so by @thm-span-absorb \( \col([\A \mid \b]) = \col(\A) \), and the ranks are equal.

\( (\Leftarrow) \) Suppose \( \rank \A = \rank\,[\A \mid \b] \). Then \( \col(\A) \) is a subspace of \( \col([\A \mid \b]) \) of the same dimension, so \( \col(\A) = \col([\A \mid \b]) \) by @thm-dim-impl-eq. In particular \( \b \in \col(\A) \), and the system is consistent by @thm-consistent-iff-column-span.

(b) By @thm-rank-nullity-matrix, \( \nullity \A = n - r \), so a basis \( \s_1, \dots, \s_{n-r} \) of \( \nul(\A) \) exists (@thm-basis-null-space). By @thm-general-solution-structure, \( \x \) is a solution if and only if \( \x - \p \in \nul(\A) \). By @thm-unique-representation, applied in the vector space \( \nul(\A) \) with this basis, each \( \x - \p \in \nul(\A) \) equals \( t_1\s_1 + \dots + t_{n-r}\s_{n-r} \) for exactly one \( (t_1, \dots, t_{n-r}) \). Conversely every such expression is in \( \nul(\A) \), so \( \p \) plus it is a solution. This proves (b).

(c) By (b), the rule \( (t_1, \dots, t_{n-r}) \mapsto \p + t_1\s_1 + \dots + t_{n-r}\s_{n-r} \) is a bijection from \( F^{n-r} \) onto the solution set: every solution is hit, and by exactly one tuple. A tuple in \( F^{n-r} \) is a choice of \( n - r \) entries, each one of \( q \) elements, so \( F^{n-r} \) has \( q^{n-r} \) elements. (When \( r = n \) there is exactly one tuple, the empty one, and the basis of \( \nul(\A) \) is empty, so \( \p \) is the only solution and \( q^0 = 1 \).) Hence the solution set has \( q^{n-r} \) elements.
:::

Over an infinite field such as \( \nQ \), \( \nR \) or \( \nC \), part (b) gives the familiar trichotomy: no solution, exactly one solution (when \( \rank \A = n \)), or infinitely many (when \( \rank \A < n \), since distinct values of \( t_1 \) give distinct solutions). Over a finite field "infinitely many" is replaced by an exact power of \( q \). For example, over \( \nF_2 \) a system can never have exactly \( 3 \) or \( 6 \) solutions.

::: {#exm-counting-solutions-f3}
[Counting solutions over \( \nF_3 \)]

Over \( \nF_3 \), consider
\[
\A = \begin{pmatrix} 1 & 1 & 0 & 2 \\ 1 & 2 & 1 & 0 \\ 2 & 0 & 1 & 2 \end{pmatrix}, \qquad \b = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}, \qquad \b' = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}.
\]
Decide whether \( \A\x = \b \) and \( \A\x = \b' \) are consistent, and count their solutions.
:::

::: {.solution}
We reduce both augmented matrices at once, carrying two right-hand columns; arithmetic is modulo \( 3 \), so \( -1 = 2 \) and \( -2 = 1 \).
\[
\begin{aligned}
\left[\begin{array}{cccc|c|c} 1 & 1 & 0 & 2 & 1 & 1 \\ 1 & 2 & 1 & 0 & 0 & 0 \\ 2 & 0 & 1 & 2 & 1 & 0 \end{array}\right]
&\xrightarrow[R_3 \to R_3 - 2R_1]{R_2 \to R_2 - R_1}
\left[\begin{array}{cccc|c|c} 1 & 1 & 0 & 2 & 1 & 1 \\ 0 & 1 & 1 & 1 & 2 & 2 \\ 0 & 1 & 1 & 1 & 2 & 1 \end{array}\right] \\
&\xrightarrow[R_1 \to R_1 - R_2]{R_3 \to R_3 - R_2}
\left[\begin{array}{cccc|c|c} 1 & 0 & 2 & 1 & 2 & 2 \\ 0 & 1 & 1 & 1 & 2 & 2 \\ 0 & 0 & 0 & 0 & 0 & 2 \end{array}\right].
\end{aligned}
\]
Row operations act on each column separately, so deleting either right-hand column gives a reduction of the corresponding augmented matrix. For instance, in row 2, \( (1, 2, 1, 0) - (1, 1, 0, 2) = (0, 1, 1, -2) = (0, 1, 1, 1) \), and in row 3, \( (2, 0, 1, 2) - 2(1, 1, 0, 2) = (0, -2, 1, -2) = (0, 1, 1, 1) \).

The left block is an echelon form of \( \A \) with two non-zero rows, so \( \rank \A = 2 \) by @cor-rank-from-any-echelon-form. With \( \b \), the augmented matrix \( [\A \mid \b] \) has the same two non-zero rows (the last is zero), so \( \rank\,[\A \mid \b] = 2 = \rank \A \), and by @thm-rouche-capelli (a) the system is consistent. By part (c) it has exactly \( 3^{4 - 2} = 9 \) solutions. Explicitly, the reduced system is \( x_1 = 2 - 2x_3 - x_4 = 2 + x_3 + 2x_4 \) and \( x_2 = 2 - x_3 - x_4 = 2 + 2x_3 + 2x_4 \), with \( x_3, x_4 \in \nF_3 \) free: nine choices.

With \( \b' \), the last row \( (0, 0, 0, 0 \mid 2) \) is a non-zero row with its pivot in the last column, so \( [\A \mid \b'] \) has three non-zero rows in echelon form and \( \rank\,[\A \mid \b'] = 3 \neq 2 \). By @thm-rouche-capelli (a), \( \A\x = \b' \) has no solution. Indeed, row 3 of \( \A \) is the sum of rows 1 and 2, so any solution would need \( b'_3 = b'_1 + b'_2 = 1 \), but \( b'_3 = 0 \).
:::

## Rank of a product

Multiplying matrices cannot create information: every column of \( \A\B \) is a combination of the columns of \( \A \), and every row is a combination of the rows of \( \B \). The rank records this.

::: {#thm-rank-product-inequality}
[Rank of a product]

Let \( \A \in M_{m \times n}(F) \) and \( \B \in M_{n \times p}(F) \). Then
\[
\rank(\A\B) \le \min(\rank \A, \rank \B).
\]
Moreover, if \( \P \in M_m(F) \) and \( \Q \in M_n(F) \) are invertible, then \( \rank(\P\A) = \rank \A = \rank(\A\Q) \).
:::

::: {.proof}
Let \( \b_1, \dots, \b_p \in F^n \) be the columns of \( \B \). By @thm-three-views-of-product, the columns of \( \A\B \) are \( \A\b_1, \dots, \A\b_p \), which lie in \( \col(\A) \) by @def-column-space. By @prp-span-basic-properties (1), \( \col(\A\B) \subseteq \col(\A) \), so \( \rank(\A\B) \le \rank \A \) by @thm-subspace-dimension. Similarly, row \( i \) of \( \A\B \) is \( (\text{row } i \text{ of } \A)\B \), a combination of the rows of \( \B \) by @thm-matrix-times-vector-columns (rows version), so \( \row(\A\B) \subseteq \row(\B) \). By @thm-row-rank-equals-column-rank, \( \rank(\A\B) = \dim \row(\A\B) \le \dim \row(\B) = \rank \B \).

For the second statement, apply the inequality twice: \( \rank \A = \rank(\P^{-1}(\P\A)) \le \rank(\P\A) \le \rank \A \), so equality holds throughout. The same sandwich with \( \A = (\A\Q)\Q^{-1} \) gives \( \rank(\A\Q) = \rank \A \).
:::

The equality case recovers something we already knew in a new form: row operations (left multiplication by an invertible \( \P \)) do not change the rank. The inequality is often strict. For \( \A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \), both factors of \( \A \cdot \A \) have rank \( 1 \), but \( \A^2 = 0 \) has rank \( 0 \).

## A toolkit for questions from Chapter 1

In Chapter 1 we asked, again and again, whether some vectors in \( F^m \) are independent, whether they span, how to extend them to a basis, and what the sum and intersection of two subspaces are. Each was answered by solving a small system by hand. Everything now reduces to one move: **put the vectors as columns of a matrix, row reduce, and read off pivots**.

::: {#thm-independence-spanning-by-rank}
[Independence and spanning by rank]

Let \( \v_1, \dots, \v_k \in F^m \), and let \( \A = \begin{pmatrix} \v_1 & \cdots & \v_k \end{pmatrix} \in M_{m \times k}(F) \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( (\v_1, \dots, \v_k) \) is linearly independent if and only if \( \rank \A = k \), that is, every column is a pivot column;
2. \( (\v_1, \dots, \v_k) \) spans \( F^m \) if and only if \( \rank \A = m \), that is, every row of the RREF has a pivot;
3. \( (\v_1, \dots, \v_k) \) is a basis of \( F^m \) if and only if \( k = m = \rank \A \).
:::
:::

::: {.proof}
(a) By @thm-matrix-times-vector-columns, \( c_1\v_1 + \dots + c_k\v_k = \A\c \) with \( \c = (c_1, \dots, c_k) \), so the list is independent if and only if \( \nul(\A) = \{\0\} \), that is, \( \nullity \A = 0 \). By @thm-rank-nullity-matrix this means \( \rank \A = k \).

(b) The list spans \( F^m \) if and only if \( \col(\A) = F^m \). Since \( \col(\A) \subseteq F^m \) and \( \dim F^m = m \), this holds if and only if \( \rank \A = m \), by @thm-dim-impl-eq for one direction and because equal spaces have equal dimension for the other. The number of pivots is \( \rank \A \) by @thm-row-rank-equals-column-rank, and the RREF has \( m \) rows, each with at most one pivot.

(c) Combine (a) and (b) with @def-basis.
:::

::: {#exm-independence-by-rank}
[Testing independence]

Decide whether \( \v_1 = (1, 2, 0, 1) \), \( \v_2 = (2, 4, 1, 1) \), \( \v_3 = (0, 0, 1, -1) \) are linearly independent in \( \nR^4 \). If not, find a linear relation.
:::

::: {.solution}
Row reduce the matrix with these columns:
\[
\begin{aligned}
\begin{pmatrix} 1 & 2 & 0 \\ 2 & 4 & 0 \\ 0 & 1 & 1 \\ 1 & 1 & -1 \end{pmatrix}
&\xrightarrow[R_4 \to R_4 - R_1]{R_2 \to R_2 - 2R_1}
\begin{pmatrix} 1 & 2 & 0 \\ 0 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & -1 & -1 \end{pmatrix} \\
&\xrightarrow{R_2 \leftrightarrow R_3}
\begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \\ 0 & -1 & -1 \end{pmatrix} \\
&\xrightarrow[R_1 \to R_1 - 2R_2]{R_4 \to R_4 + R_2}
\begin{pmatrix} 1 & 0 & -2 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}.
\end{aligned}
\]
Only columns 1 and 2 are pivot columns, so the rank is \( 2 < 3 \), and the vectors are **dependent** by @thm-independence-spanning-by-rank (a). Column 3 of the RREF gives the relation, by @thm-basis-column-space (b): \( \v_3 = -2\v_1 + \v_2 \). Check: \( -2(1, 2, 0, 1) + (2, 4, 1, 1) = (0, 0, 1, -1) \). Moreover \( (\v_1, \v_2) \) is a basis of \( \Span(\v_1, \v_2, \v_3) \) by @thm-basis-column-space (a).
:::

To **extend** an independent list to a basis of \( F^m \), append the standard basis and keep the pivot columns. The appended vectors guarantee that the columns span \( F^m \). The original vectors all survive, because by @thm-basis-column-space (c) a column is discarded only if it lies in the span of the columns before it, and an independent list has no such vector (@lem-append-independent).

::: {#exm-extend-basis-by-elimination}
[Extending to a basis by elimination]

Extend the independent list \( (\v_1, \v_2) = ((1, 2, 0, 1), (2, 4, 1, 1)) \) from @exm-independence-by-rank to a basis of \( \nR^4 \).
:::

::: {.solution}
Form \( \M = \begin{pmatrix} \v_1 & \v_2 & \e_1 & \e_2 & \e_3 & \e_4 \end{pmatrix} \) and row reduce:
\[
\begin{aligned}
\begin{pmatrix} 1 & 2 & 1 & 0 & 0 & 0 \\ 2 & 4 & 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ 1 & 1 & 0 & 0 & 0 & 1 \end{pmatrix}
&\xrightarrow[R_4 \to R_4 - R_1]{R_2 \to R_2 - 2R_1}
\begin{pmatrix} 1 & 2 & 1 & 0 & 0 & 0 \\ 0 & 0 & -2 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ 0 & -1 & -1 & 0 & 0 & 1 \end{pmatrix} \\
&\xrightarrow[\text{then } R_4 \to R_4 + R_2]{R_2 \leftrightarrow R_3}
\begin{pmatrix} 1 & 2 & 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ 0 & 0 & -2 & 1 & 0 & 0 \\ 0 & 0 & -1 & 0 & 1 & 1 \end{pmatrix}
\end{aligned}
\]
\[
\xrightarrow[\text{then } R_3 \to -R_3]{R_3 \leftrightarrow R_4}
\begin{pmatrix} 1 & 2 & 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & 0 & -1 & -1 \\ 0 & 0 & -2 & 1 & 0 & 0 \end{pmatrix}
\xrightarrow{R_4 \to R_4 + 2R_3}
\begin{pmatrix} 1 & 2 & 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & 0 & -1 & -1 \\ 0 & 0 & 0 & 1 & -2 & -2 \end{pmatrix}.
\]
This is an echelon form with pivots in columns \( 1, 2, 3, 4 \). By @cor-rank-from-any-echelon-form these are the pivot columns of \( \M \), so by @thm-basis-column-space (a) the corresponding columns of \( \M \) form a basis of \( \col(\M) = \nR^4 \):
\[
(\v_1, \v_2, \e_1, \e_2).
\]
(Clearing above the pivots gives the RREF, whose column 5 says \( \e_3 = -\v_1 + \v_2 - \e_1 - 2\e_2 \); check: \( -(1, 2, 0, 1) + (2, 4, 1, 1) - (1, 0, 0, 0) - 2(0, 1, 0, 0) = (0, 0, 1, 0) \).)
:::

For sums and intersections, one reduction does both jobs.

::: {#prp-sum-intersection-by-elimination}
[Sum and intersection by elimination]

Let \( U, W \subseteq F^m \) be subspaces with bases \( (\u_1, \dots, \u_k) \) and \( (\w_1, \dots, \w_l) \), and let \( \M = \begin{pmatrix} \u_1 & \cdots & \u_k & \w_1 & \cdots & \w_l \end{pmatrix} \in M_{m \times (k+l)}(F) \). Then:

::: {.enumerate options="label=(\alph*)"}
1. the pivot columns of \( \M \) form a basis of \( U + W \);
2. for \( \x = (x_1, \dots, x_{k+l}) \in F^{k+l} \) write \( \u_{\x} \coloneqq x_1\u_1 + \dots + x_k\u_k \), the combination of the \( \u \)'s with the first \( k \) entries of \( \x \) as coefficients. If \( (\n_1, \dots, \n_d) \) is a basis of \( \nul(\M) \), then \( (\u_{\n_1}, \dots, \u_{\n_d}) \) is a basis of \( U \cap W \).
:::

In particular \( \dim(U + W) = \rank \M \) and \( \dim(U \cap W) = \nullity \M \).
:::

::: {.proof}
(a) By @prp-sum-of-spans, \( U + W = \Span(\u_1, \dots, \u_k, \w_1, \dots, \w_l) = \col(\M) \), and @thm-basis-column-space (a) applies.

(b) By @thm-matrix-times-vector-columns, \( \x \in \nul(\M) \) means \( x_1\u_1 + \dots + x_k\u_k = -(x_{k+1}\w_1 + \dots + x_{k+l}\w_l) \), so \( \u_{\x} \) lies in \( U \) and in \( W \). Also \( \u_{\x + \y} = \u_{\x} + \u_{\y} \) and \( \u_{c\x} = c\,\u_{\x} \), by the vector space axioms in \( F^m \).

*Spanning.* Let \( \v \in U \cap W \). Since the \( \u \)'s span \( U \) and the \( \w \)'s span \( W \), \( \v = a_1\u_1 + \dots + a_k\u_k = b_1\w_1 + \dots + b_l\w_l \). Then \( \x = (a_1, \dots, a_k, -b_1, \dots, -b_l) \in \nul(\M) \) and \( \u_{\x} = \v \). Writing \( \x = \sum_i t_i\n_i \) gives \( \v = \sum_i t_i\u_{\n_i} \).

*Independence.* Let \( \sum_i t_i\u_{\n_i} = \0 \), and put \( \x = \sum_i t_i\n_i \in \nul(\M) \). Then \( \u_{\x} = x_1\u_1 + \dots + x_k\u_k = \0 \), so \( x_1 = \dots = x_k = 0 \) because the \( \u \)'s are independent. Since \( \M\x = \0 \), also \( x_{k+1}\w_1 + \dots + x_{k+l}\w_l = \0 \), so the remaining entries vanish because the \( \w \)'s are independent. Hence \( \x = \0 \), and \( t_1 = \dots = t_d = 0 \) because the \( \n_i \) are independent.

The dimension statements follow by counting the two bases, using @thm-row-rank-equals-column-rank for \( \rank \M \).
:::

Adding the two counts and using @thm-rank-nullity-matrix gives \( \dim(U + W) + \dim(U \cap W) = \rank \M + \nullity \M = k + l = \dim U + \dim W \). This is the Dimension Formula for Sums (@thm-dimension-formula-subspace-dim) again, now with a second, computational proof for subspaces of \( F^m \). (Some texts use the matrix with columns \( \u_1, \dots, \u_k, -\w_1, \dots, -\w_l \) instead of \( \M \), so that a null vector gives equal combinations \( \sum a_i\u_i = \sum b_j\w_j \) with no sign change. The two null spaces differ only by the signs of the last \( l \) entries.)

::: {#exm-sum-by-elimination}
[A basis of a sum]

Let \( U = \Span(\u_1, \u_2) \) and \( W = \Span(\w_1, \w_2) \) in \( \nR^4 \), where
\[
\u_1 = (1, 0, 1, 2), \quad \u_2 = (0, 1, 1, 1), \quad \w_1 = (1, 1, 0, 1), \quad \w_2 = (1, 3, 0, 1).
\]
Find a basis and the dimension of \( U + W \).
:::

::: {.solution}
Each pair is independent, since neither vector is a multiple of the other (compare the first two entries), so \( \dim U = \dim W = 2 \). Row reduce \( \M = \begin{pmatrix} \u_1 & \u_2 & \w_1 & \w_2 \end{pmatrix} \):
\[
\begin{pmatrix} 1 & 0 & 1 & 1 \\ 0 & 1 & 1 & 3 \\ 1 & 1 & 0 & 0 \\ 2 & 1 & 1 & 1 \end{pmatrix}
\xrightarrow[R_4 \to R_4 - 2R_1]{R_3 \to R_3 - R_1}
\begin{pmatrix} 1 & 0 & 1 & 1 \\ 0 & 1 & 1 & 3 \\ 0 & 1 & -1 & -1 \\ 0 & 1 & -1 & -1 \end{pmatrix}
\xrightarrow[R_4 \to R_4 - R_2]{R_3 \to R_3 - R_2}
\begin{pmatrix} 1 & 0 & 1 & 1 \\ 0 & 1 & 1 & 3 \\ 0 & 0 & -2 & -4 \\ 0 & 0 & -2 & -4 \end{pmatrix}
\]
\[
\xrightarrow[\text{then } R_3 \to -\frac12 R_3]{R_4 \to R_4 - R_3}
\begin{pmatrix} 1 & 0 & 1 & 1 \\ 0 & 1 & 1 & 3 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{pmatrix}
\xrightarrow[R_2 \to R_2 - R_3]{R_1 \to R_1 - R_3}
\R = \begin{pmatrix} 1 & 0 & 0 & -1 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{pmatrix}.
\]
The pivot columns are \( 1, 2, 3 \). By @prp-sum-intersection-by-elimination (a), \( (\u_1, \u_2, \w_1) \) is a basis of \( U + W \), and \( \dim(U + W) = 3 \). Column 4 of \( \R \) says \( \w_2 = -\u_1 + \u_2 + 2\w_1 \); check: \( -(1, 0, 1, 2) + (0, 1, 1, 1) + 2(1, 1, 0, 1) = (1, 3, 0, 1) \).
:::

::: {#exm-intersection-by-elimination}
[A basis of an intersection]

For \( U \) and \( W \) as in @exm-sum-by-elimination, find a basis of \( U \cap W \), and check the Dimension Formula for Sums.
:::

::: {.solution}
We reuse the RREF \( \R \) of \( \M \). Its only free column is column 4, so by @thm-basis-null-space \( \nul(\M) \) has the basis \( \n = (1, -1, -2, 1) \) (set \( x_4 = 1 \); then \( x_1 = 1 \), \( x_2 = -1 \), \( x_3 = -2 \)). The relation \( \M\n = \0 \) reads \( \u_1 - \u_2 - 2\w_1 + \w_2 = \0 \), that is,
\[
\u_1 - \u_2 = 2\w_1 - \w_2 .
\]
By @prp-sum-intersection-by-elimination (b), \( \u_{\n} = \u_1 - \u_2 = (1, -1, 0, 1) \) is a basis of \( U \cap W \). Check that it lies in \( W \): \( 2(1, 1, 0, 1) - (1, 3, 0, 1) = (1, -1, 0, 1) \). So \( \dim(U \cap W) = 1 \), and
\[
\dim U + \dim W - \dim(U \cap W) = 2 + 2 - 1 = 3 = \dim(U + W),
\]
in agreement with @thm-dimension-formula-subspace-dim.
:::

## Exercises

### A. Check your understanding

::: {#exr-rank-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define \( \col(\A) \), \( \row(\A) \), \( \nul(\A) \) and \( \rank \A \) for \( \A \in M_{m \times n}(F) \), and say which space each subspace lives in.
2. State the Rank–Nullity Theorem for matrices and the Rouché–Capelli Theorem.
3. True or false: if \( \R \) is the RREF of \( \A \), then \( \col(\R) = \col(\A) \). Justify your answer.
4. True or false: there is a \( 4 \times 6 \) real matrix with nullity \( 1 \). Justify your answer.
5. True or false: for every \( \A \in M_{m \times n}(F) \), \( \rank \A = \rank \A\tp \). Justify your answer.
6. Describe how to find a basis of \( U \cap W \) for subspaces \( U, W \subseteq F^m \) given by bases.
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. \( \col(\A) \) is the span of the columns, a subspace of \( F^m \); \( \row(\A) \) is the span of the rows, a subspace of \( M_{1 \times n}(F) \); \( \nul(\A) = \{ \x \in F^n : \A\x = \0 \} \), a subspace of \( F^n \); and \( \rank \A = \dim \col(\A) \) (@def-column-space, @def-row-space, @def-null-space, @def-rank-matrix).
2. For \( \A \in M_{m \times n}(F) \), \( \rank \A + \nullity \A = n \) (@thm-rank-nullity-matrix). For \( \b \in F^m \), \( \A\x = \b \) is consistent if and only if \( \rank \A = \rank\,[\A \mid \b] \); then the solutions are \( \p + \nul(\A) \), an \( (n - \rank \A) \)-parameter family, with exactly \( q^{\,n - \rank \A} \) solutions over a field with \( q \) elements (@thm-rouche-capelli).
3. False. For \( \A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \), \( \R = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix} \), and \( (1, 1) \in \col(\A) \) but \( (1, 1) \notin \col(\R) = \Span((1, 0)) \). Row operations preserve the row space and the column relations, not the column space (@thm-row-ops-row-space).
4. False. Its rank is at most \( 4 \), since the column space lies in \( \nR^4 \), so by @thm-rank-nullity-matrix its nullity is \( 6 - \rank \A \ge 2 \).
5. True. This is @thm-row-rank-equals-column-rank.
6. Put the basis vectors of \( U \) and then of \( W \) as the columns of \( \M \), find a basis of \( \nul(\M) \) from the RREF, and for each basis vector \( \n \) take the combination of the \( \u \)'s with the first \( k \) entries of \( \n \) as coefficients (@prp-sum-intersection-by-elimination).
:::
:::

### B. Practice

::: {#exr-rank-b1}
[B1: The three subspaces of a \( 3 \times 5 \) matrix]

Let
\[
\A = \begin{pmatrix} 1 & -1 & 2 & 0 & 3 \\ 2 & -2 & 5 & 1 & 4 \\ -1 & 1 & -1 & 1 & -5 \end{pmatrix} \in M_{3 \times 5}(\nR).
\]
Find bases of \( \col(\A) \), \( \row(\A) \) and \( \nul(\A) \). Hence verify \( \rank \A + \nullity \A = 5 \).
:::

::: {.solution}
Row reduce:
\[
\A \xrightarrow[R_3 \to R_3 + R_1]{R_2 \to R_2 - 2R_1}
\begin{pmatrix} 1 & -1 & 2 & 0 & 3 \\ 0 & 0 & 1 & 1 & -2 \\ 0 & 0 & 1 & 1 & -2 \end{pmatrix}
\xrightarrow[R_1 \to R_1 - 2R_2]{R_3 \to R_3 - R_2}
\R = \begin{pmatrix} 1 & -1 & 0 & -2 & 7 \\ 0 & 0 & 1 & 1 & -2 \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}.
\]
The pivot columns are \( 1 \) and \( 3 \); the free columns are \( 2, 4, 5 \).

By @thm-basis-column-space, the pivot columns of \( \A \), \( (1, 2, -1) \) and \( (2, 5, -1) \), form a basis of \( \col(\A) \). By @thm-basis-row-space, \( \begin{pmatrix} 1 & -1 & 0 & -2 & 7 \end{pmatrix} \) and \( \begin{pmatrix} 0 & 0 & 1 & 1 & -2 \end{pmatrix} \) form a basis of \( \row(\A) \). The reduced equations are \( x_1 = x_2 + 2x_4 - 7x_5 \) and \( x_3 = -x_4 + 2x_5 \), so by @thm-basis-null-space a basis of \( \nul(\A) \) is
\[
\s_2 = (1, 1, 0, 0, 0), \qquad \s_4 = (2, 0, -1, 1, 0), \qquad \s_5 = (-7, 0, 2, 0, 1).
\]
For example \( \A\s_4 = 2\a_1 - \a_3 + \a_4 = (2, 4, -2) - (2, 5, -1) + (0, 1, 1) = \0 \). Hence \( \rank \A = 2 \) and \( \nullity \A = 3 \), and \( 2 + 3 = 5 \), as @thm-rank-nullity-matrix requires.
:::

::: {#exr-rank-b2}
[B2: Independence and extension in \( \nR^4 \)]

Let \( \v_1 = (1, 0, 2, 1) \), \( \v_2 = (2, 1, 3, 1) \), \( \v_3 = (0, 1, -1, -1) \) in \( \nR^4 \).

::: {.enumerate options="label=(\alph*)"}
1. Determine whether \( (\v_1, \v_2, \v_3) \) is linearly independent. Justify your answer.
2. Find a basis of \( \Span(\v_1, \v_2, \v_3) \), and extend it to a basis of \( \nR^4 \) using standard basis vectors.
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Row reduce the matrix with columns \( \v_1, \v_2, \v_3 \):
\[
\begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \\ 2 & 3 & -1 \\ 1 & 1 & -1 \end{pmatrix}
\xrightarrow[R_4 \to R_4 - R_1]{R_3 \to R_3 - 2R_1}
\begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \\ 0 & -1 & -1 \\ 0 & -1 & -1 \end{pmatrix}
\xrightarrow[R_4 \to R_4 + R_2,\ R_1 \to R_1 - 2R_2]{R_3 \to R_3 + R_2}
\begin{pmatrix} 1 & 0 & -2 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}.
\]
The rank is \( 2 < 3 \), so the list is dependent by @thm-independence-spanning-by-rank (a). Column 3 gives \( \v_3 = -2\v_1 + \v_2 \) (@thm-basis-column-space (b)); check: \( (-2, 0, -4, -2) + (2, 1, 3, 1) = (0, 1, -1, -1) \).
2. By @thm-basis-column-space (a), \( (\v_1, \v_2) \) is a basis of \( \Span(\v_1, \v_2, \v_3) \). To extend it, row reduce \( \begin{pmatrix} \v_1 & \v_2 & \e_1 & \e_2 & \e_3 & \e_4 \end{pmatrix} \):
\[
\begin{aligned}
\begin{pmatrix} 1 & 2 & 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 1 & 0 & 0 \\ 2 & 3 & 0 & 0 & 1 & 0 \\ 1 & 1 & 0 & 0 & 0 & 1 \end{pmatrix}
&\xrightarrow[R_4 \to R_4 - R_1]{R_3 \to R_3 - 2R_1}
\begin{pmatrix} 1 & 2 & 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 1 & 0 & 0 \\ 0 & -1 & -2 & 0 & 1 & 0 \\ 0 & -1 & -1 & 0 & 0 & 1 \end{pmatrix} \\
&\xrightarrow[R_4 \to R_4 + R_2]{R_3 \to R_3 + R_2}
\begin{pmatrix} 1 & 2 & 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 1 & 0 & 0 \\ 0 & 0 & -2 & 1 & 1 & 0 \\ 0 & 0 & -1 & 1 & 0 & 1 \end{pmatrix}
\end{aligned}
\]
\[
\xrightarrow[\text{then } R_3 \to -R_3]{R_3 \leftrightarrow R_4}
\begin{pmatrix} 1 & 2 & 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & -1 & 0 & -1 \\ 0 & 0 & -2 & 1 & 1 & 0 \end{pmatrix}
\xrightarrow{R_4 \to R_4 + 2R_3}
\begin{pmatrix} 1 & 2 & 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & -1 & 0 & -1 \\ 0 & 0 & 0 & -1 & 1 & -2 \end{pmatrix}.
\]
This echelon form has pivots in columns \( 1, 2, 3, 4 \), which are the pivot columns by @cor-rank-from-any-echelon-form. By @thm-basis-column-space (a) the corresponding columns form a basis of the column space, which is \( \nR^4 \) since it contains \( \e_1, \dots, \e_4 \). Hence \( (\v_1, \v_2, \e_1, \e_2) \) is a basis of \( \nR^4 \) extending \( (\v_1, \v_2) \).
:::
:::

::: {#exr-rank-b3}
[B3: Sum and intersection in \( \nR^5 \)]

Let \( U = \Span(\u_1, \u_2, \u_3) \) and \( W = \Span(\w_1, \w_2) \) in \( \nR^5 \), where
\[
\begin{aligned}
&\u_1 = (1, 1, 0, 0, 1), \quad \u_2 = (0, 1, 1, 0, 0), \quad \u_3 = (1, 0, 0, 1, 0), \\
&\w_1 = (1, 2, 2, 1, 2), \quad \w_2 = (0, 0, 1, 1, 1).
\end{aligned}
\]
Find \( \dim U \), \( \dim W \), a basis of \( U + W \) and a basis of \( U \cap W \). Hence verify @thm-dimension-formula-subspace-dim.
:::

::: {.solution}
Row reduce \( \M = \begin{pmatrix} \u_1 & \u_2 & \u_3 & \w_1 & \w_2 \end{pmatrix} \):
\[
\begin{aligned}
\begin{pmatrix} 1 & 0 & 1 & 1 & 0 \\ 1 & 1 & 0 & 2 & 0 \\ 0 & 1 & 0 & 2 & 1 \\ 0 & 0 & 1 & 1 & 1 \\ 1 & 0 & 0 & 2 & 1 \end{pmatrix}
&\xrightarrow[R_5 \to R_5 - R_1]{R_2 \to R_2 - R_1}
\begin{pmatrix} 1 & 0 & 1 & 1 & 0 \\ 0 & 1 & -1 & 1 & 0 \\ 0 & 1 & 0 & 2 & 1 \\ 0 & 0 & 1 & 1 & 1 \\ 0 & 0 & -1 & 1 & 1 \end{pmatrix} \\
&\xrightarrow{R_3 \to R_3 - R_2}
\begin{pmatrix} 1 & 0 & 1 & 1 & 0 \\ 0 & 1 & -1 & 1 & 0 \\ 0 & 0 & 1 & 1 & 1 \\ 0 & 0 & 1 & 1 & 1 \\ 0 & 0 & -1 & 1 & 1 \end{pmatrix}
\end{aligned}
\]
\[
\xrightarrow[R_5 \to R_5 + R_3]{R_4 \to R_4 - R_3}
\begin{pmatrix} 1 & 0 & 1 & 1 & 0 \\ 0 & 1 & -1 & 1 & 0 \\ 0 & 0 & 1 & 1 & 1 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 2 & 2 \end{pmatrix}
\xrightarrow[\text{then } R_4 \to \frac12 R_4]{R_4 \leftrightarrow R_5}
\begin{pmatrix} 1 & 0 & 1 & 1 & 0 \\ 0 & 1 & -1 & 1 & 0 \\ 0 & 0 & 1 & 1 & 1 \\ 0 & 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}.
\]
Clearing above the pivots (\( R_3 \to R_3 - R_4 \), \( R_2 \to R_2 - R_4 \), \( R_1 \to R_1 - R_4 \), then \( R_2 \to R_2 + R_3 \), \( R_1 \to R_1 - R_3 \)) gives
\[
\R = \begin{pmatrix} 1 & 0 & 0 & 0 & -1 \\ 0 & 1 & 0 & 0 & -1 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}.
\]
The pivot columns are \( 1, 2, 3, 4 \), so \( (\u_1, \u_2, \u_3, \w_1) \) is independent by @thm-basis-column-space (a), and so are its sub-lists \( (\u_1, \u_2, \u_3) \) and \( (\w_1) \); also \( \w_2 \) is not a multiple of \( \w_1 \) (compare first entries). Hence \( \dim U = 3 \) and \( \dim W = 2 \), with the given spanning lists as bases. By @prp-sum-intersection-by-elimination (a), \( (\u_1, \u_2, \u_3, \w_1) \) is a basis of \( U + W \), so \( \dim(U + W) = 4 \).

The only free column is column 5. Setting \( x_5 = 1 \) gives \( \n = (1, 1, 0, -1, 1) \), a basis of \( \nul(\M) \) by @thm-basis-null-space. So \( \u_1 + \u_2 - \w_1 + \w_2 = \0 \), and by @prp-sum-intersection-by-elimination (b), \( \u_1 + \u_2 = (1, 2, 1, 0, 1) \) is a basis of \( U \cap W \). Check: \( \w_1 - \w_2 = (1, 2, 1, 0, 1) \). Hence \( \dim(U \cap W) = 1 \), and
\[
\dim U + \dim W - \dim(U \cap W) = 3 + 2 - 1 = 4 = \dim(U + W).
\]
:::

### C. Going deeper

::: {#exr-rank-c1}
[C1: Rank of a sum]

Let \( \A, \B \in M_{m \times n}(F) \). Prove that \( \rank(\A + \B) \le \rank \A + \rank \B \). Give an example where the inequality is strict.
:::

::: {.solution}
The \( j \)-th column of \( \A + \B \) is \( \a_j + \b_j \), which lies in \( \col(\A) + \col(\B) \) (@def-sum-of-subspaces). This sum is a subspace (@thm-subspace-sum), so by @thm-span-subspace, \( \col(\A + \B) \subseteq \col(\A) + \col(\B) \). By @thm-subspace-dimension and @thm-dimension-formula-subspace-dim,
\[
\begin{aligned}
\rank(\A + \B)
&\le \dim(\col(\A) + \col(\B)) \\
&= \rank \A + \rank \B - \dim(\col(\A) \cap \col(\B)) \\
&\le \rank \A + \rank \B .
\end{aligned}
\]
For strictness, take \( \A = \I_2 \) and \( \B = -\I_2 \) over \( \nR \): \( \rank(\A + \B) = \rank 0 = 0 < 2 + 2 \).
:::

::: {#exr-rank-c2}
[C2: Matrices of rank one]

Let \( \A \in M_{m \times n}(F) \). Prove that \( \rank \A = 1 \) if and only if \( \A = \x\y\tp \) for some **non-zero** \( \x \in F^m \) and \( \y \in F^n \).
:::

::: {.solution}
\( (\Leftarrow) \) Suppose \( \A = \x\y\tp \) with \( \x, \y \neq \0 \), and write \( \y = (y_1, \dots, y_n) \). By @thm-three-views-of-product, the \( j \)-th column of \( \x\y\tp \) is \( \x \) times the \( j \)-th column of \( \y\tp \), the \( 1 \times 1 \) matrix \( (y_j) \); that is, \( y_j\x \). So every column lies in \( \Span(\x) \), and \( \col(\A) \subseteq \Span(\x) \). Since \( \y \neq \0 \), some \( y_j \neq 0 \), and then \( y_j\x \neq \0 \) because \( \x \neq \0 \) (@thm-zero-product). The list \( (\x) \) is independent, since \( a\x = \0 \) forces \( a = 0 \) (@thm-zero-product), so \( \Span(\x) \) has dimension \( 1 \), and \( \rank \A \le 1 \) by @thm-subspace-dimension. On the other hand \( \rank \A \neq 0 \): a space of dimension \( 0 \) has the empty list as a basis, so it equals \( \Span() = \{\0\} \), but \( \col(\A) \) contains the non-zero vector \( y_j\x \). Hence \( \rank \A = 1 \).

\( (\Rightarrow) \) Suppose \( \rank \A = 1 \), and let \( (\x) \) be a basis of \( \col(\A) \); then \( \x \neq \0 \). Each column \( \a_j \in \col(\A) \) equals \( y_j\x \) for some \( y_j \in F \). Put \( \y = (y_1, \dots, y_n) \). By the computation in \( (\Leftarrow) \), the \( j \)-th column of \( \x\y\tp \) is \( y_j\x = \a_j \), so \( \A = \x\y\tp \). If \( \y = \0 \), then \( \A = 0 \) would have rank \( 0 \), so \( \y \neq \0 \). This proves the claim.
:::

::: {#exr-rank-c3}
[C3: The matrix \( i + j \)]

For \( n \ge 1 \), let \( \A_n \in M_n(\nR) \) have entries \( a_{ij} = i + j \). Prove that \( \rank \A_1 = 1 \) and \( \rank \A_n = 2 \) for every \( n \ge 2 \). Hence find \( \nullity \A_n \).

*Hint: write each row as a combination of two fixed row vectors.*
:::

::: {.solution}
For \( n = 1 \), \( \A_1 = (2) \neq 0 \), so \( \rank \A_1 = 1 \). Let \( n \ge 2 \), and put \( \mathbf{1} = \begin{pmatrix} 1 & 1 & \cdots & 1 \end{pmatrix} \) and \( \mathbf{d} = \begin{pmatrix} 1 & 2 & \cdots & n \end{pmatrix} \) in \( M_{1 \times n}(\nR) \). Row \( i \) of \( \A_n \) is \( \begin{pmatrix} i + 1 & \cdots & i + n \end{pmatrix} = i\mathbf{1} + \mathbf{d} \). So \( \row(\A_n) \subseteq \Span(\mathbf{1}, \mathbf{d}) \), and \( \dim \row(\A_n) \le 2 \) by @thm-size-bounds.

Rows 1 and 2 are \( \begin{pmatrix} 2 & 3 & \cdots \end{pmatrix} \) and \( \begin{pmatrix} 3 & 4 & \cdots \end{pmatrix} \). If \( c_1(\text{row } 1) + c_2(\text{row } 2) = 0 \), the first two entries give \( 2c_1 + 3c_2 = 0 \) and \( 3c_1 + 4c_2 = 0 \). Subtracting the first from the second gives \( c_1 + c_2 = 0 \), so \( c_1 = -c_2 \), and then \( -2c_2 + 3c_2 = c_2 = 0 \), so \( c_1 = 0 \). Hence \( \row(\A_n) \) contains two independent vectors, and \( \dim \row(\A_n) \ge 2 \) by @thm-size-bounds.

So \( \dim \row(\A_n) = 2 \), and \( \rank \A_n = 2 \) by @thm-row-rank-equals-column-rank. By @thm-rank-nullity-matrix, \( \nullity \A_n = n - 2 \) for \( n \ge 2 \), and \( \nullity \A_1 = 0 \).
:::

::: {#exr-rank-c4}
[C4: Counting right-hand sides over a finite field]

Let \( F \) be a finite field with \( q \) elements, and let \( \A \in M_{m \times n}(F) \) have rank \( r \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that exactly \( q^{r} \) vectors \( \b \in F^m \) make \( \A\x = \b \) consistent.
2. By counting the pairs \( (\x, \b) \in F^n \times F^m \) with \( \A\x = \b \) in two ways, and using @thm-general-solution-structure but **not** @thm-rank-nullity-matrix, prove that \( \nul(\A) \) has exactly \( q^{\,n - r} \) elements. Deduce \( \nullity \A = n - r \): a counting proof of Rank–Nullity over a finite field.
3. Over \( \nF_2 \), let \( \A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix} \). How many \( \b \in \nF_2^3 \) give a consistent system, and how many solutions does each such system have?
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. By @thm-consistent-iff-column-span, \( \A\x = \b \) is consistent exactly when \( \b \in \col(\A) \). Let \( (\c_1, \dots, \c_r) \) be a basis of \( \col(\A) \). By @thm-unique-representation, \( (t_1, \dots, t_r) \mapsto t_1\c_1 + \dots + t_r\c_r \) is a bijection \( F^r \to \col(\A) \): every vector of \( \col(\A) \) is hit by exactly one tuple. Since \( F^r \) has \( q^r \) elements, so does \( \col(\A) \).
2. Let \( N = \lvert \nul(\A) \rvert \). Each \( \x \in F^n \) determines exactly one \( \b = \A\x \), so there are \( q^n \) pairs. Now group the pairs by \( \b \). If \( \b \notin \col(\A) \), there are none, by @thm-consistent-iff-column-span. If \( \b \in \col(\A) \), pick one solution \( \p \); by @thm-general-solution-structure the solutions are \( \p + \nul(\A) \), and \( \h \mapsto \p + \h \) is a bijection from \( \nul(\A) \) onto this set (it is onto by definition, and \( \p + \h = \p + \h' \) gives \( \h = \h' \)). So each of the \( q^r \) vectors \( \b \) of (a) accounts for exactly \( N \) pairs, and there are \( q^r N \) pairs in total. Hence \( q^r N = q^n \), and \( N = q^{\,n-r} \).

   Let \( d = \nullity \A \). The argument of (a), applied to a basis of \( \nul(\A) \) of length \( d \), gives \( N = q^{d} \). So \( q^{d} = q^{\,n-r} \). Since \( q \ge 2 \), distinct exponents give distinct powers of \( q \), so \( d = n - r \). This is @thm-rank-nullity-matrix, proved here by counting alone.
3. Over \( \nF_2 \), \( R_3 \to R_3 + R_1 \) gives row 3 equal to \( (0, 1, 1) \), and then \( R_3 \to R_3 + R_2 \) makes it zero. So an echelon form is \( \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{pmatrix} \), and \( \rank \A = 2 \) by @cor-rank-from-any-echelon-form. By (a), exactly \( 2^2 = 4 \) of the \( 8 \) vectors \( \b \) give a consistent system, and by @thm-rouche-capelli (c) each has \( 2^{3-2} = 2 \) solutions. (The consistent \( \b \) are those with \( b_1 + b_2 + b_3 = 0 \). The rows of \( \A \) add up to zero, so every consistent \( \b \) satisfies this equation; exactly \( 4 \) vectors of \( \nF_2^3 \) satisfy it, and \( 4 \) are consistent, so the two sets coincide.)
:::
:::
