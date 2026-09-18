# Matrices

You have probably met matrices as tables of numbers that are multiplied by a strange rule. This section rebuilds them over an arbitrary field \( F \) and answers the questions a computational course leaves open. Why is the product defined the way it is? Which rules of school algebra survive, and which fail? What does it mean to divide by a matrix? Everything later in the book, from Gaussian elimination in Chapter 2 to the matrix of a linear map in Chapter 3, rests on the answers.

Throughout, \( F \) is a field (@def-field). Nothing here uses more about \( F \) than the field axioms, so every statement holds over \( \nQ \), \( \nR \), \( \nC \) and \( \nF_p \) alike.

## Matrices and their entries

::: {#def-matrix}
[Matrix]

Let \( F \) be a field and \( m, n \ge 1 \) integers. An **\( m \times n \) matrix over \( F \)** is a rectangular array
\[
  \A = \begin{pmatrix}
    a_{11} & a_{12} & \cdots & a_{1n} \\
    a_{21} & a_{22} & \cdots & a_{2n} \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{m1} & a_{m2} & \cdots & a_{mn}
  \end{pmatrix}
\]
with \( m \) rows and \( n \) columns, whose **entries** \( a_{ij} \) lie in \( F \). Formally, it is a function \( \{1, \dots, m\} \times \{1, \dots, n\} \to F \), \( (i, j) \mapsto a_{ij} \). The set of all such matrices is \( M_{m \times n}(F) \), and we write \( M_n(F) = M_{n \times n}(F) \) for the **square** matrices.
:::

The entry \( a_{ij} \) sits in row \( i \) and column \( j \): **row first, column second**. We write \( \A = (a_{ij}) \), and \( (\A)_{ij} \) for the \( (i, j) \)-entry when the matrix has no letter of its own. Two matrices are **equal** when they have the **same size** and the same entry in every position; this is equality of functions (@def-function).

Two sizes deserve their own names. A matrix in \( M_{n \times 1}(F) \) is a **column vector**, and we write
\[
  F^n = M_{n \times 1}(F), \qquad \x = \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} .
\]
In running text we write \( \x = (x_1, \dots, x_n) \) and still mean a column. Columns are printed in bold. A matrix in \( M_{1 \times n}(F) \) is a **row vector**. For \( j = 1, \dots, n \), the column \( \e_j \in F^n \) has \( 1 \) in position \( j \) and \( 0 \) elsewhere.

We will often cut a matrix into its columns. If \( \a_j = (a_{1j}, \dots, a_{mj}) \in F^m \) is the \( j \)-th column of \( \A \), we write
\[
  \A = \begin{pmatrix} \a_1 & \a_2 & \cdots & \a_n \end{pmatrix} .
\]
The \( i \)-th row of \( \A \) is the row vector \( \begin{pmatrix} a_{i1} & \cdots & a_{in} \end{pmatrix} \in M_{1 \times n}(F) \).

::: {#exm-matrices}
[Matrices over different fields]

Identify the size, the field and a few entries of each matrix:
\[
  \A = \begin{pmatrix} 1 & -2 & 0 \\ 3 & 1 & 4 \end{pmatrix}, \quad
  \B = \begin{pmatrix} i & 1 + i \\ 0 & 2 - i \end{pmatrix}, \quad
  \C = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}, \quad
  \D = \begin{pmatrix} 5 \end{pmatrix}.
\]
Here \( \C \) is meant over \( \nF_2 \). Also write out the \( 2 \times 2 \) real matrix \( \E \) with \( e_{ij} = i + 2j \).
:::

::: {.solution}
\( \A \in M_{2 \times 3}(\nR) \), with \( a_{12} = -2 \) and \( a_{23} = 4 \); its second column is \( \a_2 = (-2, 1) \). \( \B \in M_2(\nC) \), with \( b_{12} = 1 + i \) and \( b_{21} = 0 \). \( \C \in M_3(\nF_2) \); every entry is \( 0 \) or \( 1 \). \( \D \in M_1(\nR) \) is the degenerate case, a \( 1 \times 1 \) matrix. It behaves exactly like the number \( 5 \), and \( 1 \times 1 \) matrices are how numbers will appear inside matrix formulas. Finally \( e_{11} = 3 \), \( e_{12} = 5 \), \( e_{21} = 4 \), \( e_{22} = 6 \), so \( \E = \begin{pmatrix} 3 & 5 \\ 4 & 6 \end{pmatrix} \). Swapping the roles of \( i \) and \( j \) would give a different matrix, which is why the order "row, column" matters.
:::

## Special matrices

A few shapes of matrix occur so often that they have names. The **main diagonal** of a square matrix \( \A \in M_n(F) \) consists of the entries \( a_{11}, a_{22}, \dots, a_{nn} \).

::: {#def-zero-matrix}
[Zero matrix]

The **zero matrix** \( 0 = 0_{m \times n} \in M_{m \times n}(F) \) is the matrix all of whose entries are \( 0 \).
:::

::: {#def-identity-matrix}
[Identity matrix]

The **identity matrix** \( \I_n \in M_n(F) \) has entries
\[
  (\I_n)_{ij} = \delta_{ij} = \begin{cases} 1 & \text{if } i = j, \\ 0 & \text{if } i \neq j. \end{cases}
\]
That is, \( 1 \) on the main diagonal and \( 0 \) elsewhere. We write \( \I \) when the size is clear. The symbol \( \delta_{ij} \) is the **Kronecker delta**.
:::

The columns of \( \I_n \) are exactly \( \e_1, \dots, \e_n \).

::: {#def-diagonal-matrix}
[Diagonal matrix]

A square matrix \( \A \in M_n(F) \) is **diagonal** if \( a_{ij} = 0 \) **whenever** \( i \neq j \). We write \( \diag(d_1, \dots, d_n) \) for the diagonal matrix with diagonal entries \( d_1, \dots, d_n \).
:::

::: {#def-upper-triangular}
[Upper triangular matrix]

A square matrix \( \A \in M_n(F) \) is **upper triangular** if \( a_{ij} = 0 \) **whenever** \( i > j \), that is, every entry **strictly below** the main diagonal is zero. It is **lower triangular** if \( a_{ij} = 0 \) whenever \( i < j \).
:::

::: {#exm-zero-identity}
[Zero and identity matrices]

Write out \( 0_{2 \times 3} \), \( \I_2 \) and \( \I_3 \). Which of them are diagonal?
:::

::: {.solution}
\[
  0_{2 \times 3} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}, \quad
  \I_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \quad
  \I_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}.
\]
\( \I_2 = \diag(1, 1) \) and \( \I_3 = \diag(1, 1, 1) \) are diagonal. The matrix \( 0_{2 \times 3} \) is **not** diagonal, because the definition only applies to square matrices; the square zero matrix \( 0_{n \times n} = \diag(0, \dots, 0) \) is diagonal.
:::

::: {#exm-special-matrices}
[Diagonal and triangular]

Classify each matrix as diagonal, upper triangular, lower triangular, or none of these:
\[
  \P = \begin{pmatrix} 3 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 0 \end{pmatrix}, \quad
  \Q = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{pmatrix}, \quad
  \R = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 7 & 6 \end{pmatrix}.
\]
:::

::: {.solution}
\( \P = \diag(3, -1, 0) \) is diagonal. A zero on the diagonal is allowed: the definition only constrains off-diagonal entries. \( \P \) is also both upper and lower triangular, and in general a matrix is diagonal exactly when it is both. \( \Q \) is upper triangular but not lower triangular, since \( q_{12} = 2 \neq 0 \). \( \R \) differs from \( \Q \) in one entry, \( r_{32} = 7 \). All other entries below the diagonal are still zero, but the clause "\( a_{ij} = 0 \) whenever \( i > j \)" fails at \( (i, j) = (3, 2) \), so \( \R \) is not upper triangular. It is not lower triangular either.
:::

## Addition and scalar multiplication

Matrices of the same size are added, and multiplied by scalars, one entry at a time.

::: {#def-matrix-addition}
[Matrix addition]

Let \( \A = (a_{ij}) \) and \( \B = (b_{ij}) \) be in \( M_{m \times n}(F) \), of the **same size**. Their **sum** is \( \A + \B \in M_{m \times n}(F) \) with \( (\A + \B)_{ij} = a_{ij} + b_{ij} \).
:::

::: {#def-scalar-multiplication}
[Scalar multiplication]

Let \( \A = (a_{ij}) \in M_{m \times n}(F) \) and \( c \in F \). The **scalar multiple** \( c\A \in M_{m \times n}(F) \) has entries \( (c\A)_{ij} = c\, a_{ij} \).
:::

::: {#def-additive-inverse}
[Additive inverse]

The **additive inverse** of \( \A \in M_{m \times n}(F) \) is \( -\A = (-1)\A \), with entries \( -a_{ij} \). We write \( \A - \B = \A + (-\B) \).
:::

Matrices of different sizes are never added: \( \begin{pmatrix} 1 & 2 \end{pmatrix} + \begin{pmatrix} 1 \\ 2 \end{pmatrix} \) is not defined.

::: {#exm-matrix-addition}
[Adding and scaling]

Let \( \A = \begin{pmatrix} 1 & -2 & 0 \\ 3 & 1 & 4 \end{pmatrix} \) and \( \B = \begin{pmatrix} 2 & 2 & -1 \\ 0 & -5 & 1 \end{pmatrix} \) in \( M_{2 \times 3}(\nR) \). Compute \( \A + \B \), \( 3\A \) and \( \A - 2\B \).
:::

::: {.solution}
Entry by entry,
\[
  \begin{aligned}
  \A + \B &= \begin{pmatrix} 3 & 0 & -1 \\ 3 & -4 & 5 \end{pmatrix}, \\
  3\A &= \begin{pmatrix} 3 & -6 & 0 \\ 9 & 3 & 12 \end{pmatrix}, \\
  \A - 2\B &= \begin{pmatrix} 1 - 4 & -2 - 4 & 0 + 2 \\ 3 - 0 & 1 + 10 & 4 - 2 \end{pmatrix} = \begin{pmatrix} -3 & -6 & 2 \\ 3 & 11 & 2 \end{pmatrix}.
  \end{aligned}
\]
:::

Because both operations work entry by entry, they inherit the rules of \( F \):

::: {#thm-matrix-addition-properties}
[Properties of addition and scalar multiplication]

Let \( \A, \B, \C \in M_{m \times n}(F) \) and \( c, d \in F \). Then:

1. \( \A + \B = \B + \A \);
2. \( (\A + \B) + \C = \A + (\B + \C) \);
3. \( \A + 0 = \A \);
4. \( \A + (-\A) = 0 \);
5. \( c(\A + \B) = c\A + c\B \) and \( (c + d)\A = c\A + d\A \);
6. \( (cd)\A = c(d\A) \) and \( 1\A = \A \).
:::

::: {.proof}
Two matrices of the same size are equal when their entries agree, so it suffices to compare \( (i, j) \)-entries. For 1, \( (\A + \B)_{ij} = a_{ij} + b_{ij} = b_{ij} + a_{ij} = (\B + \A)_{ij} \), where the middle equality is commutativity of addition in \( F \). For 5, \( (c(\A + \B))_{ij} = c(a_{ij} + b_{ij}) = c a_{ij} + c b_{ij} = (c\A + c\B)_{ij} \) by distributivity in \( F \). Each remaining identity reduces in the same way to the corresponding field axiom of @def-field in each entry. This proves the theorem.
:::

These eight rules will reappear in Chapter 1 as the axioms of a vector space: \( M_{m \times n}(F) \) is one of our standard examples.

## Matrix multiplication

Addition was entrywise. The obvious guess for multiplication is also entrywise, but that product is almost useless. The product that matters is the one that records **substitution**, and it looks very different.

Suppose new variables \( y_1, y_2 \) are given in terms of \( x_1, x_2 \), and \( z_1, z_2 \) in terms of \( y_1, y_2 \):
\[
  \begin{aligned} y_1 &= 2x_1 + x_2 \\ y_2 &= x_1 + 4x_2 \end{aligned}
  \qquad\qquad
  \begin{aligned} z_1 &= y_1 + 2y_2 \\ z_2 &= 3y_1 - y_2 \end{aligned}
\]
Record each substitution by its table of coefficients: \( \B = \begin{pmatrix} 2 & 1 \\ 1 & 4 \end{pmatrix} \) for \( \y \) in terms of \( \x \), and \( \A = \begin{pmatrix} 1 & 2 \\ 3 & -1 \end{pmatrix} \) for \( \z \) in terms of \( \y \). Substituting,
\[
  \begin{aligned}
  z_1 &= (2x_1 + x_2) + 2(x_1 + 4x_2) \\
  &= (1 \cdot 2 + 2 \cdot 1)x_1 + (1 \cdot 1 + 2 \cdot 4)x_2 = 4x_1 + 9x_2, \\
  z_2 &= 3(2x_1 + x_2) - (x_1 + 4x_2) \\
  &= (3 \cdot 2 + (-1) \cdot 1)x_1 + (3 \cdot 1 + (-1) \cdot 4)x_2 = 5x_1 - x_2 .
  \end{aligned}
\]
So \( \z \) in terms of \( \x \) has coefficient table \( \begin{pmatrix} 4 & 9 \\ 5 & -1 \end{pmatrix} \). Look at how each entry arose: the coefficient of \( x_k \) in \( z_i \) is \( a_{i1} b_{1k} + a_{i2} b_{2k} \), row \( i \) of \( \A \) against column \( k \) of \( \B \). The entrywise product \( \begin{pmatrix} 2 & 2 \\ 3 & -4 \end{pmatrix} \) has nothing to do with the substitution. This forces the definition.

*To multiply matrices, run each row of the first against each column of the second: the product of two matrices is the table of the combined substitution.*

::: {#def-matrix-multiplication}
[Matrix multiplication]

Let \( \A = (a_{ij}) \in M_{m \times n}(F) \) and \( \B = (b_{jk}) \in M_{n \times p}(F) \), so that **the number of columns of \( \A \) equals the number of rows of \( \B \)**. Their **product** is the matrix \( \A\B \in M_{m \times p}(F) \) with entries
\[
  (\A\B)_{ik} = \sum_{j=1}^{n} a_{ij} b_{jk} = a_{i1} b_{1k} + a_{i2} b_{2k} + \dots + a_{in} b_{nk}
\]
for \( 1 \le i \le m \) and \( 1 \le k \le p \). If the sizes do not match, \( \A\B \) is **not defined**.
:::

In words: to get the \( (i, k) \)-entry of \( \A\B \), walk along row \( i \) of \( \A \) and down column \( k \) of \( \B \) at the same time, multiply the entries you meet in pairs, and add. The size condition says that the row and the column have the same length \( n \), so the pairing makes sense. The product has as many rows as \( \A \) and as many columns as \( \B \):
\[
  \underset{m \times n}{\A} \; \underset{n \times p}{\B} = \underset{m \times p}{\A\B} .
\]

In particular, for \( \A \in M_{m \times n}(F) \) and a column \( \x \in F^n \), the product \( \A\x \in F^m \) is defined, with \( i \)-th entry \( a_{i1} x_1 + \dots + a_{in} x_n \). A system of \( m \) linear equations in \( n \) unknowns is therefore a single equation \( \A\x = \b \).

::: {#exm-matrix-multiplication}
[A product of square matrices]

Let \( \A = \begin{pmatrix} 2 & -1 \\ 0 & 3 \end{pmatrix} \) and \( \B = \begin{pmatrix} 1 & 4 \\ -2 & 1 \end{pmatrix} \) in \( M_2(\nR) \). Compute \( \A\B \) and \( \B\A \).
:::

::: {.solution}
Row \( i \) of \( \A \) against column \( k \) of \( \B \):
\[
  \begin{aligned}
  \A\B &= \begin{pmatrix} 2 \cdot 1 + (-1)(-2) & 2 \cdot 4 + (-1) \cdot 1 \\ 0 \cdot 1 + 3 \cdot (-2) & 0 \cdot 4 + 3 \cdot 1 \end{pmatrix} = \begin{pmatrix} 4 & 7 \\ -6 & 3 \end{pmatrix}, \\
  \B\A &= \begin{pmatrix} 1 \cdot 2 + 4 \cdot 0 & 1 \cdot (-1) + 4 \cdot 3 \\ -2 \cdot 2 + 1 \cdot 0 & (-2)(-1) + 1 \cdot 3 \end{pmatrix} = \begin{pmatrix} 2 & 11 \\ -4 & 5 \end{pmatrix}.
  \end{aligned}
\]
Both products are defined, and they are different.
:::

::: {#exm-matrix-multiplication-dimensions}
[Products of rectangular matrices]

Let \( \A = \begin{pmatrix} 1 & 0 & 2 \\ -1 & 3 & 1 \end{pmatrix} \in M_{2 \times 3}(\nR) \) and \( \B = \begin{pmatrix} 3 & 1 \\ 2 & 1 \\ 1 & 0 \end{pmatrix} \in M_{3 \times 2}(\nR) \). Determine the sizes of \( \A\B \) and \( \B\A \) and compute them. Then compute \( \begin{pmatrix} 1 & 2 \end{pmatrix} \begin{pmatrix} 3 \\ 4 \end{pmatrix} \) and \( \begin{pmatrix} 3 \\ 4 \end{pmatrix} \begin{pmatrix} 1 & 2 \end{pmatrix} \).
:::

::: {.solution}
\( \A\B \) is \( (2 \times 3)(3 \times 2) \), so it is \( 2 \times 2 \); \( \B\A \) is \( (3 \times 2)(2 \times 3) \), so it is \( 3 \times 3 \). Computing row against column,
\[
  \A\B = \begin{pmatrix} 3 + 0 + 2 & 1 + 0 + 0 \\ -3 + 6 + 1 & -1 + 3 + 0 \end{pmatrix} = \begin{pmatrix} 5 & 1 \\ 4 & 2 \end{pmatrix},
  \qquad
  \B\A = \begin{pmatrix} 2 & 3 & 7 \\ 1 & 3 & 5 \\ 1 & 0 & 2 \end{pmatrix}.
\]
For instance \( (\B\A)_{13} = 3 \cdot 2 + 1 \cdot 1 = 7 \). The last two products show the extreme cases: a row times a column is \( 1 \times 1 \), namely \( \begin{pmatrix} 1 \cdot 3 + 2 \cdot 4 \end{pmatrix} = \begin{pmatrix} 11 \end{pmatrix} \), while a column times a row is \( 2 \times 2 \), namely \( \begin{pmatrix} 3 & 6 \\ 4 & 8 \end{pmatrix} \).
:::

Here is a non-example by minimal change. Take the same six entries as \( \B \), but arrange them in two rows: \( \C = \begin{pmatrix} 3 & 2 & 1 \\ 1 & 1 & 0 \end{pmatrix} \in M_{2 \times 3}(\nR) \). The entries are still real numbers and \( \A \) is unchanged. But \( \A \) has \( 3 \) columns and \( \C \) has \( 2 \) rows, so forming \( \A\C \) would pair a row of length \( 3 \) with a column of length \( 2 \). The clause "**the number of columns of \( \A \) equals the number of rows of \( \B \)**" fails, and \( \A\C \) is **not defined**.

Why this definition, and not the entrywise one? Because it is the only rule under which "the table of a combined substitution is the product of the tables". In Chapter 3 the same fact becomes: the matrix of a composition of linear maps is the product of their matrices. Every property of matrix multiplication, good or bad, comes from this.

## Three views of a product

The entry formula is how one computes a product by hand, but it hides the structure. Two other descriptions, by columns and by rows, are what we will actually think with. It turns out that multiplying by \( \A \) on the left acts on each column of \( \B \) separately, and multiplying by \( \B \) on the right acts on each row of \( \A \) separately:

::: {#thm-three-views-of-product}
[Three views of a product]

Let \( \A \in M_{m \times n}(F) \) and \( \B \in M_{n \times p}(F) \), and write \( \B = \begin{pmatrix} \b_1 & \cdots & \b_p \end{pmatrix} \) with columns \( \b_k \in F^n \). Then:

1. **(Entries)** \( (\A\B)_{ik} = \sum_{j=1}^{n} a_{ij} b_{jk} \) for all \( i, k \);
2. **(Columns)** the \( k \)-th column of \( \A\B \) is \( \A\b_k \), that is,
\[
  \A\B = \begin{pmatrix} \A\b_1 & \A\b_2 & \cdots & \A\b_p \end{pmatrix};
\]
3. **(Rows)** the \( i \)-th row of \( \A\B \) is \( (\text{row } i \text{ of } \A)\, \B \).
:::

::: {.proof}
Part 1 is @def-matrix-multiplication. For part 2, fix \( k \). The column \( \b_k \) has entries \( b_{1k}, \dots, b_{nk} \), so by @def-matrix-multiplication the \( i \)-th entry of \( \A\b_k \in F^m \) is \( \sum_{j=1}^{n} a_{ij} b_{jk} \). By part 1 this is \( (\A\B)_{ik} \), the \( i \)-th entry of the \( k \)-th column of \( \A\B \). Hence the \( k \)-th column of \( \A\B \) is \( \A\b_k \).

For part 3, fix \( i \), and let \( \mathbf{r} = \begin{pmatrix} a_{i1} & \cdots & a_{in} \end{pmatrix} \) be row \( i \) of \( \A \). Then \( \mathbf{r} \B \) is a \( 1 \times p \) matrix whose \( k \)-th entry is \( \sum_{j=1}^{n} a_{ij} b_{jk} = (\A\B)_{ik} \), again by @def-matrix-multiplication. This is the \( k \)-th entry of row \( i \) of \( \A\B \). This proves the theorem.
:::

The column view reduces every matrix product to products \( \A\x \) of a matrix with a single column. So it pays to understand \( \A\x \) well, and here is the fact to understand:

::: {#thm-matrix-times-vector-columns}
[\( \A\x \) is a combination of the columns of \( \A \)]

Let \( \A = \begin{pmatrix} \a_1 & \cdots & \a_n \end{pmatrix} \in M_{m \times n}(F) \) with columns \( \a_j \in F^m \), and let \( \x = (x_1, \dots, x_n) \in F^n \). Then
\[
  \A\x = x_1 \a_1 + x_2 \a_2 + \dots + x_n \a_n .
\]
In particular \( \A\e_j = \a_j \) for each \( j \). Similarly, if \( \mathbf{r}_1, \dots, \mathbf{r}_m \) are the rows of \( \A \) and \( \y = \begin{pmatrix} y_1 & \cdots & y_m \end{pmatrix} \) is a row vector, then \( \y \A = y_1 \mathbf{r}_1 + \dots + y_m \mathbf{r}_m \).
:::

::: {.proof}
Both sides are in \( F^m \), so we compare \( i \)-th entries. By @def-matrix-multiplication, the \( i \)-th entry of \( \A\x \) is \( \sum_{j=1}^{n} a_{ij} x_j \). On the right, the \( i \)-th entry of \( x_j \a_j \) is \( x_j a_{ij} \) by @def-scalar-multiplication, so by @def-matrix-addition the \( i \)-th entry of \( \sum_j x_j \a_j \) is \( \sum_{j=1}^{n} x_j a_{ij} \). These agree because multiplication in \( F \) is commutative. Taking \( \x = \e_j \), whose only non-zero entry is \( x_j = 1 \), gives \( \A\e_j = \a_j \). The statement for rows follows in the same way, comparing the \( k \)-th entries \( \sum_{i} y_i a_{ik} \). This proves the theorem.
:::

Read the formula as a sentence: **the entries of \( \x \) are the weights, and the columns of \( \A \) are what gets weighted.** So \( \A\x = \b \) has a solution exactly when \( \b \) can be built from the columns of \( \A \). This single observation drives much of Chapters 2 and 3. Combined with @thm-three-views-of-product, it also says that **every column of \( \A\B \) is a combination of the columns of \( \A \)**, with weights taken from the corresponding column of \( \B \), and **every row of \( \A\B \) is a combination of the rows of \( \B \)**.

::: {#exm-three-views}
[One product, three ways]

Let
\[
  \A = \begin{pmatrix} 1 & 2 \\ 3 & -1 \\ 0 & 4 \end{pmatrix} \in M_{3 \times 2}(\nR), \qquad
  \B = \begin{pmatrix} 2 & 1 \\ -1 & 1 \end{pmatrix} \in M_2(\nR), \qquad
  \x = \begin{pmatrix} 2 \\ -1 \end{pmatrix}.
\]
Compute \( \A\x \) as a combination of the columns of \( \A \). Then compute \( \A\B \) by columns, check one row by the row view, and check one entry by the entry formula.
:::

::: {.solution}
The columns of \( \A \) are \( \a_1 = (1, 3, 0) \) and \( \a_2 = (2, -1, 4) \). By @thm-matrix-times-vector-columns,
\[
  \A\x = 2\a_1 - \a_2 = \begin{pmatrix} 2 \\ 6 \\ 0 \end{pmatrix} - \begin{pmatrix} 2 \\ -1 \\ 4 \end{pmatrix} = \begin{pmatrix} 0 \\ 7 \\ -4 \end{pmatrix}.
\]
**Columns.** The first column of \( \B \) is \( \b_1 = (2, -1) = \x \), so the first column of \( \A\B \) is \( \A\b_1 = (0, 7, -4) \), just computed. The second column is \( \b_2 = (1, 1) \), so \( \A\b_2 = \a_1 + \a_2 = (3, 2, 4) \). Hence
\[
  \A\B = \begin{pmatrix} 0 & 3 \\ 7 & 2 \\ -4 & 4 \end{pmatrix}.
\]
**Rows.** Row 2 of \( \A \) is \( \begin{pmatrix} 3 & -1 \end{pmatrix} \), and by @thm-matrix-times-vector-columns (rows version) \( \begin{pmatrix} 3 & -1 \end{pmatrix} \B = 3 \begin{pmatrix} 2 & 1 \end{pmatrix} - \begin{pmatrix} -1 & 1 \end{pmatrix} = \begin{pmatrix} 7 & 2 \end{pmatrix} \), which is row 2 of \( \A\B \).

**Entries.** \( (\A\B)_{32} = a_{31} b_{12} + a_{32} b_{22} = 0 \cdot 1 + 4 \cdot 1 = 4 \), as in the answer.

The column view needed nothing beyond scaling and adding columns of \( \A \). When the columns of \( \B \) are simple, it is usually the fastest route.
:::

::: {.check}
Without multiplying out, what is the second column of \( \begin{pmatrix} 5 & -1 & 7 \\ 2 & 0 & 3 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 0 \\ 4 & 1 \end{pmatrix} \)?
:::

::: {.solution}
The second column of the right factor is \( \e_3 = (0, 0, 1) \). By @thm-three-views-of-product and @thm-matrix-times-vector-columns, the second column of the product is \( \A\e_3 \), the third column of the left factor: \( (7, 3) \).
:::

## The rules of multiplication

Matrix multiplication keeps the most important rules of arithmetic: associativity, both distributive laws, and an identity.

::: {#thm-matrix-multiplication-properties}
[Properties of matrix multiplication]

Let \( c \in F \), and let \( \A, \A' \in M_{m \times n}(F) \), \( \B, \B' \in M_{n \times p}(F) \) and \( \C \in M_{p \times q}(F) \). Then:

1. **(Associativity)** \( (\A\B)\C = \A(\B\C) \);
2. **(Distributivity)** \( \A(\B + \B') = \A\B + \A\B' \) and \( (\A + \A')\B = \A\B + \A'\B \);
3. **(Identity)** \( \I_m \A = \A = \A \I_n \);
4. **(Scalars)** \( c(\A\B) = (c\A)\B = \A(c\B) \);
5. **(Zero)** \( 0_{\ell \times m} \A = 0_{\ell \times n} \) and \( \A\, 0_{n \times r} = 0_{m \times r} \) for all \( \ell, r \ge 1 \).
:::

::: {.idea}
Each identity is checked entry by entry. The only one with content is associativity. Both sides have \( (i, l) \)-entry equal to the double sum \( \sum_j \sum_k a_{ij} b_{jk} c_{kl} \), added up in two different orders, so the proof is "expand, swap the order of the finite sums, and fold back up". In the substitution picture it is no surprise: substituting in two stages gives the same result whichever pair of stages we combine first.
:::

::: {.proof}
For 1, both sides lie in \( M_{m \times q}(F) \). Fix \( i \) and \( l \). By @def-matrix-multiplication applied twice,
\[
  \bigl((\A\B)\C\bigr)_{il} = \sum_{k=1}^{p} (\A\B)_{ik}\, c_{kl} = \sum_{k=1}^{p} \Bigl( \sum_{j=1}^{n} a_{ij} b_{jk} \Bigr) c_{kl} = \sum_{k=1}^{p} \sum_{j=1}^{n} a_{ij} b_{jk} c_{kl},
\]
where the last step uses distributivity in \( F \). The same computation gives
\[
  \bigl(\A(\B\C)\bigr)_{il} = \sum_{j=1}^{n} a_{ij} (\B\C)_{jl} = \sum_{j=1}^{n} a_{ij} \Bigl( \sum_{k=1}^{p} b_{jk} c_{kl} \Bigr) = \sum_{j=1}^{n} \sum_{k=1}^{p} a_{ij} b_{jk} c_{kl} .
\]
The two double sums add the same \( np \) terms in different orders, so they are equal, by commutativity and associativity of addition in \( F \). Hence \( (\A\B)\C = \A(\B\C) \).

For 2, \( \bigl(\A(\B + \B')\bigr)_{ik} = \sum_j a_{ij}(b_{jk} + b'_{jk}) = \sum_j a_{ij} b_{jk} + \sum_j a_{ij} b'_{jk} = (\A\B + \A\B')_{ik} \) by distributivity in \( F \); the other law is the same with the roles of the factors swapped.

For 3, \( (\I_m \A)_{ik} = \sum_{j=1}^{m} \delta_{ij} a_{jk} = a_{ik} \), because by @def-identity-matrix only the term \( j = i \) survives. Likewise \( (\A \I_n)_{ik} = \sum_{j} a_{ij} \delta_{jk} = a_{ik} \).

For 4, \( (c(\A\B))_{ik} = c \sum_j a_{ij} b_{jk} = \sum_j (c a_{ij}) b_{jk} = ((c\A)\B)_{ik} \), and moving \( c \) next to \( b_{jk} \) instead, using commutativity in \( F \), gives \( (\A(c\B))_{ik} \). For 5, every term \( 0 \cdot a_{jk} \) or \( a_{ij} \cdot 0 \) is \( 0 \) by @thm-field-basic-properties. This proves the theorem.
:::

Associativity means we may write \( \A\B\C \) without brackets, and more generally a product of any number of matrices, as long as consecutive sizes match.

Just as important is what is **missing** from the list. There is no commutative law, and no cancellation law. Each of the following failures will cost you a wrong proof if you forget it.

::: {.warning}
**\( \A\B \neq \B\A \) in general.** Take \( \A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) and \( \B = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \). Then \( \A\B = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \) but \( \B\A = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} \). Before swapping two factors in a proof, you must know that they commute. (And if \( \A \) is \( 2 \times 3 \) and \( \B \) is \( 3 \times 2 \), then \( \A\B \) and \( \B\A \) do not even have the same size.)
:::

::: {.warning}
**A product can be zero with both factors non-zero.** In \( M_2(\nR) \),
\[
  \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}.
\]
So \( M_n(F) \) is not a field for \( n \ge 2 \), and "\( \A\B = 0 \) implies \( \A = 0 \) or \( \B = 0 \)" is false.
:::

::: {.warning}
**Cancellation fails: \( \A\C = \B\C \) does not imply \( \A = \B \).** With
\[
  \A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \quad \B = \begin{pmatrix} 1 & 2 \\ 3 & 9 \end{pmatrix}, \quad \C = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix},
\]
we get \( \A\C = \B\C = \begin{pmatrix} 1 & 1 \\ 3 & 3 \end{pmatrix} \) although \( \A \neq \B \). By the column view, both columns of \( \C \) are \( \e_1 \), so \( \A\C \) and \( \B\C \) only see the first columns of \( \A \) and \( \B \), which agree. Canceling \( \C \) is legal only when \( \C \) is invertible, as we will see below.
:::

::: {.check}
Find a non-zero \( \A \in M_2(\nR) \) with \( \A^2 = \A\A = 0 \).
:::

::: {.solution}
Take \( \A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \). By the column view, \( \A\e_1 = \0 \) and \( \A\e_2 = \e_1 \), so the columns of \( \A^2 \) are \( \A\0 = \0 \) and \( \A\e_1 = \0 \). Hence \( \A^2 = 0 \) although \( \A \neq 0 \). This small matrix is the source of a remarkable number of counterexamples in this book; it will reappear often.
:::

## The transpose

Rows and columns play symmetric roles in a matrix, and the transpose exchanges them.

::: {#def-transpose}
[Transpose]

Let \( \A = (a_{ij}) \in M_{m \times n}(F) \). The **transpose** of \( \A \) is the matrix \( \A\tp \in M_{n \times m}(F) \) with entries
\[
  (\A\tp)_{ij} = a_{ji} .
\]
:::

In words: row \( i \) of \( \A \) becomes column \( i \) of \( \A\tp \), and the size flips from \( m \times n \) to \( n \times m \). A square matrix is reflected in its main diagonal.

::: {#def-symmetric-matrix}
[Symmetric and skew-symmetric matrices]

A square matrix \( \A \in M_n(F) \) is **symmetric** if \( \A\tp = \A \), that is, \( a_{ij} = a_{ji} \) for all \( i, j \). It is **skew-symmetric** if \( \A\tp = -\A \), that is, \( a_{ij} = -a_{ji} \) for all \( i, j \).
:::

::: {#exm-transpose}
[Transposes, symmetric and skew-symmetric matrices]

Compute the transpose of \( \A = \begin{pmatrix} 1 & -2 & 0 \\ 3 & 1 & 4 \end{pmatrix} \). Decide whether
\[
  \S = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 5 \\ 3 & 5 & 6 \end{pmatrix}, \qquad
  \K = \begin{pmatrix} 0 & 2 & -1 \\ -2 & 0 & 3 \\ 1 & -3 & 0 \end{pmatrix}, \qquad
  \S' = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 5 \\ 3 & 6 & 6 \end{pmatrix}
\]
over \( \nR \) are symmetric or skew-symmetric.
:::

::: {.solution}
The rows of \( \A \) become columns: \( \A\tp = \begin{pmatrix} 1 & 3 \\ -2 & 1 \\ 0 & 4 \end{pmatrix} \in M_{3 \times 2}(\nR) \).

\( \S \) is symmetric: \( s_{12} = s_{21} = 2 \), \( s_{13} = s_{31} = 3 \), \( s_{23} = s_{32} = 5 \). \( \K \) is skew-symmetric: \( k_{12} = 2 = -k_{21} \), \( k_{13} = -1 = -k_{31} \), \( k_{23} = 3 = -k_{32} \), and each diagonal entry satisfies \( k_{ii} = -k_{ii} \), so it is \( 0 \). The matrix \( \S' \) differs from \( \S \) only in the entry \( (3, 2) \). Every other symmetric pair still matches, but \( s'_{23} = 5 \neq 6 = s'_{32} \), so \( \S' \) is **not** symmetric. A \( 1 \times 1 \) matrix is always symmetric, and the identity \( \I_n \) and every diagonal matrix are symmetric.
:::

Over \( \nR \), a skew-symmetric matrix has zero diagonal, since \( a_{ii} = -a_{ii} \) forces \( 2a_{ii} = 0 \). Over \( \nF_2 \), where \( -1 = 1 \), "skew-symmetric" and "symmetric" mean the same thing, and \( \I_2 \) is skew-symmetric. The characteristic of the field (@def-characteristic) matters.

The transpose is compatible with the operations, except that it **reverses** products:

::: {#thm-transpose-properties}
[Properties of the transpose]

Let \( c \in F \). For matrices of sizes for which each expression is defined:

1. \( (\A\tp)\tp = \A \);
2. \( (\A + \B)\tp = \A\tp + \B\tp \);
3. \( (c\A)\tp = c \A\tp \);
4. \( (\A\B)\tp = \B\tp \A\tp \) for \( \A \in M_{m \times n}(F) \) and \( \B \in M_{n \times p}(F) \).
:::

::: {.idea}
The order reverses for a size reason before any computation: \( (\A\B)\tp \) is \( p \times m \), and \( \B\tp \A\tp \) is \( (p \times n)(n \times m) = p \times m \), while \( \A\tp \B\tp \) is \( (n \times m)(p \times n) \), usually not even defined. Then compare entries.
:::

::: {.proof}
For 1, \( ((\A\tp)\tp)_{ij} = (\A\tp)_{ji} = a_{ij} \) by @def-transpose. For 2 and 3, \( ((\A + \B)\tp)_{ij} = a_{ji} + b_{ji} = (\A\tp + \B\tp)_{ij} \) and \( ((c\A)\tp)_{ij} = c a_{ji} = (c\A\tp)_{ij} \).

For 4, both sides lie in \( M_{p \times m}(F) \). Fix \( 1 \le i \le p \) and \( 1 \le k \le m \). By @def-transpose and @def-matrix-multiplication,
\[
  \begin{aligned}
  \bigl((\A\B)\tp\bigr)_{ik} &= (\A\B)_{ki} = \sum_{j=1}^{n} a_{kj} b_{ji}, \\
  (\B\tp \A\tp)_{ik} &= \sum_{j=1}^{n} (\B\tp)_{ij} (\A\tp)_{jk} = \sum_{j=1}^{n} b_{ji} a_{kj} .
  \end{aligned}
\]
The two sums agree term by term because multiplication in \( F \) is commutative. Hence \( (\A\B)\tp = \B\tp \A\tp \). This proves the theorem.
:::

For example, for every \( \A \in M_{m \times n}(F) \), the square matrix \( \A\tp \A \) is symmetric: by parts 4 and 1, \( (\A\tp \A)\tp = \A\tp (\A\tp)\tp = \A\tp \A \). Matrices of this form are central to least squares and the singular value decomposition much later on.

## The trace

The trace is the simplest number attached to a square matrix, and it has one surprising property.

::: {#def-trace}
[Trace]

The **trace** of a square matrix \( \A = (a_{ij}) \in M_n(F) \) is the sum of its diagonal entries:
\[
  \tr \A = \sum_{i=1}^{n} a_{ii} = a_{11} + a_{22} + \dots + a_{nn} \in F .
\]
:::

::: {#exm-trace}
[Computing traces]

Compute \( \tr \A \) for \( \A = \begin{pmatrix} 2 & 7 & -1 \\ 0 & -3 & 5 \\ 4 & 1 & 6 \end{pmatrix} \in M_3(\nR) \), and \( \tr \I_n \) over \( \nR \) and over \( \nF_2 \).
:::

::: {.solution}
\( \tr \A = 2 + (-3) + 6 = 5 \); the off-diagonal entries play no role. \( \tr \I_n = 1 + \dots + 1 = n \cdot 1 \). Over \( \nR \) this is \( n \). Over \( \nF_2 \) it is \( 0 \) when \( n \) is even and \( 1 \) when \( n \) is odd. The trace is **not** defined for a non-square matrix.
:::

::: {#thm-trace-properties}
[Properties of the trace]

Let \( \A, \B \in M_n(F) \) and \( c \in F \). Then:

1. \( \tr(\A + \B) = \tr \A + \tr \B \) and \( \tr(c\A) = c \tr \A \);
2. \( \tr(\A\tp) = \tr \A \);
3. \( \tr(\A\B) = \tr(\B\A) \). More generally, this holds for all \( \A \in M_{m \times n}(F) \) and \( \B \in M_{n \times m}(F) \), where \( \A\B \) is \( m \times m \) and \( \B\A \) is \( n \times n \).
:::

::: {.idea}
Part 3 is surprising because \( \A\B \neq \B\A \) in general. But the trace only sees the diagonal, and \( \tr(\A\B) = \sum_i \sum_j a_{ij} b_{ji} \) is a sum over all pairs \( (i, j) \) of the product of \( a_{ij} \) with the "mirror" entry \( b_{ji} \). That description does not care which matrix is written first.
:::

::: {.proof}
Parts 1 and 2 follow from the definitions: the diagonal entries of \( \A + \B \), \( c\A \) and \( \A\tp \) are \( a_{ii} + b_{ii} \), \( c a_{ii} \) and \( a_{ii} \).

For 3, let \( \A \in M_{m \times n}(F) \) and \( \B \in M_{n \times m}(F) \). By @def-trace and @def-matrix-multiplication,
\[
  \tr(\A\B) = \sum_{i=1}^{m} (\A\B)_{ii} = \sum_{i=1}^{m} \sum_{j=1}^{n} a_{ij} b_{ji}
  = \sum_{j=1}^{n} \sum_{i=1}^{m} b_{ji} a_{ij} = \sum_{j=1}^{n} (\B\A)_{jj} = \tr(\B\A),
\]
where the middle equality swaps the order of the finite double sum and uses commutativity of multiplication in \( F \). This proves the theorem.
:::

A first payoff: for all \( \A, \B \in M_n(F) \), the matrix \( \A\B - \B\A \) has trace \( \tr(\A\B) - \tr(\B\A) = 0 \). So over \( \nR \) it can never equal \( \I_n \), whose trace is \( n \) (@exr-matrices-c1). The trace will also turn out to be one of the quantities that does not change when we change coordinates.

It is tempting to conclude that the trace of a product ignores the order of **all** the factors. It does not.

::: {.warning}
**\( \tr(\A\B\C) \neq \tr(\B\A\C) \) in general.** Take \( \A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \), \( \B = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) and \( \C = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \). Then \( \A\B\C = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \) has trace \( 1 \), but \( \B\A = 0 \), so \( \B\A\C = 0 \) has trace \( 0 \). What **is** true is that a **cyclic** rotation preserves the trace: \( \tr(\A\B\C) = \tr\bigl((\A\B)\C\bigr) = \tr\bigl(\C(\A\B)\bigr) = \tr(\C\A\B) \) by part 3.
:::

## Inverse matrices

In a field we solve \( ax = b \) by multiplying by \( a^{-1} \), and this works exactly when \( a \neq 0 \). We would like to solve a system \( \A\x = \b \) the same way, by "dividing by \( \A \)". What should that mean, and for which \( \A \) is it possible?

The naive answer, "every non-zero matrix", fails. Let \( \N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \neq 0 \). For **any** \( \B \in M_2(F) \), the first column of \( \B\N \) is \( \B \) times the first column of \( \N \), that is \( \B\0 = \0 \), by @thm-three-views-of-product. The first column of \( \I_2 \) is \( \e_1 \neq \0 \), so \( \B\N \neq \I_2 \): no matrix undoes \( \N \) from the left. Dividing needs a genuine two-sided inverse, and not every non-zero matrix has one.

*An invertible matrix is a square matrix whose effect can be undone by multiplying, on either side.*

::: {#def-invertible-matrix}
[Invertible matrix]

A **square** matrix \( \A \in M_n(F) \) is **invertible** if there exists \( \B \in M_n(F) \) such that
\[
  \A\B = \I_n \quad \textbf{and} \quad \B\A = \I_n .
\]
Such a \( \B \) is called **an inverse** of \( \A \). A square matrix that is not invertible is called **singular**.
:::

In words: \( \A \) is invertible when some matrix \( \B \) of the same size cancels it **from the right** (\( \A\B = \I_n \)) **and** from the left (\( \B\A = \I_n \)). The definition asks for one \( \B \) doing both jobs, and it only speaks about square matrices.

Is "an inverse" really "the inverse"? Yes: an inverse, if it exists, is unique. This is part 1 of the next theorem, and it lets us write \( \A^{-1} \). The remaining parts are what inverses are for.

::: {#thm-inverse-matrix-properties}
[Properties of inverses]

Let \( \A, \B \in M_n(F) \).

1. **(Uniqueness)** If \( \B \) and \( \B' \) are both inverses of \( \A \), then \( \B = \B' \). We write \( \A^{-1} \) for **the** inverse of an invertible \( \A \).
2. If \( \A \) is invertible, then so is \( \A^{-1} \), and \( (\A^{-1})^{-1} = \A \).
3. If \( \A \) and \( \B \) are invertible, then so is \( \A\B \), and \( (\A\B)^{-1} = \B^{-1} \A^{-1} \).
4. If \( \A \) is invertible, then so is \( \A\tp \), and \( (\A\tp)^{-1} = (\A^{-1})\tp \).
5. If \( \A \) is invertible and \( c \in F \) is **non-zero**, then \( c\A \) is invertible, and \( (c\A)^{-1} = c^{-1} \A^{-1} \).
6. **(Cancellation)** If \( \A \) is invertible, then \( \A\X = \A\Y \) implies \( \X = \Y \) for all \( \X, \Y \in M_{n \times p}(F) \), and \( \X\A = \Y\A \) implies \( \X = \Y \) for all \( \X, \Y \in M_{p \times n}(F) \).
7. **(Solving)** If \( \A \) is invertible, then for every \( \b \in F^n \) the equation \( \A\x = \b \) has **exactly one** solution \( \x \in F^n \), namely \( \x = \A^{-1}\b \).
:::

::: {.idea}
Uniqueness is the standard trick for "prove unique by assuming two": sandwich \( \B' \) between \( \B \) and \( \A \), and use associativity to collapse the product both ways. For the other parts the candidate inverse is written in the statement, so we only multiply it out on **both** sides, as the definition demands. The order in part 3 is the "socks and shoes" rule: to undo "first \( \B \), then \( \A \)", undo \( \A \) first.
:::

::: {.proof}
For 1, suppose \( \A\B = \B\A = \I_n \) and \( \A\B' = \B'\A = \I_n \). By @thm-matrix-multiplication-properties (identity and associativity),
\[
  \B = \B \I_n = \B(\A\B') = (\B\A)\B' = \I_n \B' = \B' .
\]

For 2, the equations \( \A\A^{-1} = \I_n \) and \( \A^{-1}\A = \I_n \) say precisely that \( \A \) is an inverse of \( \A^{-1} \). By part 1 it is the inverse.

For 3, by associativity,
\[
  (\A\B)(\B^{-1}\A^{-1}) = \A(\B\B^{-1})\A^{-1} = \A \I_n \A^{-1} = \A\A^{-1} = \I_n ,
\]
and similarly \( (\B^{-1}\A^{-1})(\A\B) = \B^{-1}(\A^{-1}\A)\B = \B^{-1}\B = \I_n \). Hence \( \B^{-1}\A^{-1} \) is an inverse of \( \A\B \), and by part 1 it is \( (\A\B)^{-1} \).

For 4, by @thm-transpose-properties, \( \A\tp (\A^{-1})\tp = (\A^{-1}\A)\tp = \I_n\tp = \I_n \) and \( (\A^{-1})\tp \A\tp = (\A\A^{-1})\tp = \I_n \), where \( \I_n\tp = \I_n \) since \( \I_n \) is symmetric. Hence \( (\A^{-1})\tp \) is the inverse of \( \A\tp \).

For 5, since \( c \neq 0 \), the inverse \( c^{-1} \) exists in \( F \). By @thm-matrix-multiplication-properties (scalars), \( (c\A)(c^{-1}\A^{-1}) = (cc^{-1})(\A\A^{-1}) = \I_n \), and similarly in the other order.

For 6, suppose \( \A\X = \A\Y \). Multiplying on the left by \( \A^{-1} \) and using associativity, \( \X = \I_n \X = (\A^{-1}\A)\X = \A^{-1}(\A\X) = \A^{-1}(\A\Y) = (\A^{-1}\A)\Y = \Y \). The statement for \( \X\A = \Y\A \) follows by multiplying on the right by \( \A^{-1} \).

For 7, \( \x = \A^{-1}\b \) is a solution, since \( \A(\A^{-1}\b) = (\A\A^{-1})\b = \b \). If \( \x \) is any solution, then \( \A\x = \b = \A(\A^{-1}\b) \), and part 6 (with \( p = 1 \)) gives \( \x = \A^{-1}\b \). This proves the theorem.
:::

Part 6 is the repair of the failed cancellation law from the warnings above: **you may cancel an invertible matrix**, on the side where it stands, and nothing else.

::: {#exm-inverse-matrices}
[Some invertible matrices]

Show that each of the following is invertible and find its inverse: \( \I_n \); a diagonal matrix \( \D = \diag(d_1, \dots, d_n) \) with **all** \( d_i \neq 0 \); \( \A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix} \in M_2(\nR) \); and \( \U = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \in M_2(\nF_2) \).
:::

::: {.solution}
\( \I_n \I_n = \I_n \), so \( \I_n \) is its own inverse. This is the degenerate case: \( \I_n \) plays the role that \( 1 \) plays among numbers.

For \( \D \), let \( \E = \diag(d_1^{-1}, \dots, d_n^{-1}) \), which exists since every \( d_i \neq 0 \). Then \( (\D\E)_{ik} = \sum_j d_{ij} e_{jk} \), and only \( j = i = k \) can contribute, so \( \D\E = \diag(d_1 d_1^{-1}, \dots, d_n d_n^{-1}) = \I_n \); likewise \( \E\D = \I_n \). Hence \( \D^{-1} = \E \). For \( n = 1 \) this says the \( 1 \times 1 \) matrix \( (a) \) is invertible when \( a \neq 0 \), with inverse \( (a^{-1}) \), exactly as in the field.

For \( \A \), let \( \B = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix} \). Then
\[
  \A\B = \begin{pmatrix} 6 - 5 & -2 + 2 \\ 15 - 15 & -5 + 6 \end{pmatrix} = \I_2, \qquad
  \B\A = \begin{pmatrix} 6 - 5 & 3 - 3 \\ -10 + 10 & -5 + 6 \end{pmatrix} = \I_2 ,
\]
so \( \A^{-1} = \B \). (Where \( \B \) came from is explained by @thm-two-by-two-inverse below.)

For \( \U \) over \( \nF_2 \), \( \U^2 = \begin{pmatrix} 1 & 1 + 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \), since \( 1 + 1 = 0 \). So \( \U \) is its own inverse. Over \( \nR \) the same array would have inverse \( \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} \): the answer depends on the field.
:::

Now a non-example by minimal change. The matrix \( \diag(1, 2) \) is invertible, with inverse \( \diag(1, \frac12) \). Change the entry \( 2 \) to \( 0 \): \( \A = \diag(1, 0) \) is still diagonal and still non-zero. But for any \( \B \in M_2(F) \), the second column of \( \B\A \) is \( \B \) times the second column of \( \A \), which is \( \B\0 = \0 \), while the second column of \( \I_2 \) is \( \e_2 \). So \( \B\A \neq \I_2 \) for every \( \B \): the clause "**there exists** \( \B \) with ... \( \B\A = \I_n \)" fails, and \( \diag(1, 0) \) is singular. The same argument shows that any square matrix with a zero column is singular, and in particular so is every zero matrix \( 0_{n \times n} \).

Why does the definition insist on a **square** matrix and on **both** equations? For non-square matrices one-sided inverses can exist without the other side: with \( \C = \begin{pmatrix} 1 & 0 \end{pmatrix} \in M_{1 \times 2}(\nR) \) and \( \D = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \), we get \( \C\D = \begin{pmatrix} 1 \end{pmatrix} = \I_1 \) but \( \D\C = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \neq \I_2 \). Demanding both equations makes the inverse unique (part 1) and makes both cancellation laws (part 6) hold.

::: {.warning}
**For square matrices, \( \A\B = \I_n \) already implies \( \B\A = \I_n \). This is true, but it is not obvious, and we do not know it yet.** Nothing in this chapter proves it: the entries of \( \A\B \) and \( \B\A \) are different sums. It is proved in Chapter 2, using row reduction. Until then, to show that \( \B \) is the inverse of \( \A \), check **both** \( \A\B = \I_n \) and \( \B\A = \I_n \). (The non-square example above shows that some argument is needed.)
:::

For \( 2 \times 2 \) matrices, invertibility is decided by one number.

::: {#thm-two-by-two-inverse}
[Inverse of a \( 2 \times 2 \) matrix]

Let \( \A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in M_2(F) \). Then \( \A \) is invertible **if and only if** \( ad - bc \neq 0 \). In that case,
\[
  \A^{-1} = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}.
\]
:::

::: {.idea}
Where does the formula come from? Try to kill the off-diagonal entries of \( \A \) by multiplying with a matrix built from its own entries. Swapping \( a \) and \( d \) and negating \( b \) and \( c \) gives \( \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} = (ad - bc) \I_2 \). If \( ad - bc \neq 0 \), divide by it. If \( ad - bc = 0 \), the same computation shows that \( \A \) sends a non-zero column to \( \0 \), and an invertible matrix cannot do that, since its inverse would have to send \( \0 \) back to a non-zero column.
:::

::: {.proof}
Write \( \Delta = ad - bc \) and \( \tilde \A = \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} \). By @def-matrix-multiplication and commutativity of multiplication in \( F \),
\[
  \begin{aligned}
  \A \tilde \A &= \begin{pmatrix} ad - bc & -ab + ba \\ cd - dc & -cb + da \end{pmatrix} = \Delta \I_2, \\
  \tilde \A \A &= \begin{pmatrix} da - bc & db - bd \\ -ca + ac & -cb + ad \end{pmatrix} = \Delta \I_2 .
  \end{aligned}
\]

(\( \Leftarrow \)) Suppose \( \Delta \neq 0 \), so \( \Delta^{-1} \) exists in \( F \). By @thm-matrix-multiplication-properties (scalars), \( \A(\Delta^{-1}\tilde \A) = \Delta^{-1}(\A\tilde \A) = \Delta^{-1}\Delta \I_2 = \I_2 \), and likewise \( (\Delta^{-1}\tilde \A)\A = \I_2 \). Hence \( \A \) is invertible with \( \A^{-1} = \Delta^{-1}\tilde \A \), which is the stated formula.

(\( \Rightarrow \)) We prove the contrapositive. Suppose \( \Delta = 0 \). We first find \( \x \in F^2 \) with \( \x \neq \0 \) and \( \A\x = \0 \).

*Case 1.* \( \A = 0 \). Take \( \x = \e_1 \).

*Case 2.* \( c \neq 0 \) or \( d \neq 0 \). Take \( \x = (d, -c) \neq \0 \). Then \( \A\x = (ad - bc,\; cd - dc) = (\Delta, 0) = \0 \).

*Case 3.* \( c = d = 0 \) but \( a \neq 0 \) or \( b \neq 0 \). Take \( \x = (b, -a) \neq \0 \). Then \( \A\x = (ab - ba,\; cb - da) = (0, 0) = \0 \), since \( c = d = 0 \).

These cases cover every \( \A \). Now suppose, for a contradiction, that \( \A \) is invertible. Then by @thm-matrix-multiplication-properties,
\[
  \x = \I_2 \x = (\A^{-1}\A)\x = \A^{-1}(\A\x) = \A^{-1}\0 = \0 ,
\]
contradicting \( \x \neq \0 \). Hence \( \A \) is not invertible. This proves the theorem.
:::

The number \( ad - bc \) will return in Chapter 6 as the determinant of \( \A \). Here it arose from a single multiplication, and the proof used nothing beyond the field axioms, so the theorem holds over every field. For instance, \( \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix} \) has \( ad - bc = 6 - 5 = 1 \), which explains the inverse found in @exm-inverse-matrices; and \( \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} \) has \( ad - bc = 0 \), so it is singular, with \( \A(2, -1) = \0 \).

## Powers and polynomials of a matrix

A square matrix can be multiplied by itself, so we can form powers, and then plug the matrix into a polynomial (@def-polynomial). This is how polynomials act on matrices throughout the book.

::: {#def-polynomial-of-matrix}
[Powers and polynomials of a matrix]

Let \( \A \in M_n(F) \). The **powers** of \( \A \) are defined recursively by
\[
  \A^0 = \I_n, \qquad \A^{k+1} = \A^k \A \quad (k \in \nN).
\]
For a polynomial \( p = a_0 + a_1 x + \dots + a_N x^N \in F[x] \), the matrix **\( p(\A) \)** is
\[
  p(\A) = a_0 \I_n + a_1 \A + a_2 \A^2 + \dots + a_N \A^N \in M_n(F).
\]
:::

Two points in this definition deserve attention. The **constant term** \( a_0 \) becomes \( a_0 \I_n \), because \( a_0 \) alone is a number and cannot be added to matrices; this matches \( x^0 = 1 \) with \( \A^0 = \I_n \). And \( p(\A) \) is well defined, because enlarging \( N \) only adds terms \( 0 \cdot \A^k = 0 \), exactly as for evaluation at a number (@def-polynomial-evaluation).

The next theorem says that plugging in a matrix respects sums and products, just as plugging in a number does (@thm-evaluation-respects-operations).

::: {#thm-polynomial-of-matrix-properties}
[Polynomials in one matrix]

Let \( \A \in M_n(F) \) and \( p, q \in F[x] \). Then:

1. \( \A^j \A^k = \A^{j+k} \) for all \( j, k \in \nN \);
2. \( (p + q)(\A) = p(\A) + q(\A) \) and \( (pq)(\A) = p(\A)\, q(\A) \);
3. \( p(\A)\, q(\A) = q(\A)\, p(\A) \).
:::

::: {.idea}
In the proof of @thm-evaluation-respects-operations, the only delicate step moved \( c^i \) past a coefficient \( b_j \). Here the coefficients are scalars, and scalars can be moved freely through matrix products. The other step, \( c^i c^j = c^{i+j} \), becomes part 1, which is associativity plus induction. Part 3 is then free, because \( pq = qp \) in \( F[x] \).
:::

::: {.proof}
For 1, fix \( j \) and use induction on \( k \) (@thm-induction). For \( k = 0 \), \( \A^j \A^0 = \A^j \I_n = \A^j \). If \( \A^j \A^k = \A^{j+k} \), then by @def-polynomial-of-matrix and associativity (@thm-matrix-multiplication-properties),
\[
  \A^j \A^{k+1} = \A^j (\A^k \A) = (\A^j \A^k) \A = \A^{j+k} \A = \A^{j+k+1} .
\]

For 2, let \( p = \sum_{i=0}^{m} a_i x^i \) and \( q = \sum_{j=0}^{l} b_j x^j \). The statement for sums follows from @thm-matrix-addition-properties, since \( (a_i + b_i)\A^i = a_i \A^i + b_i \A^i \). For products, by @def-polynomial-ring the coefficient of \( x^k \) in \( pq \) is \( \sum_{i + j = k} a_i b_j \), so
\[
  \begin{aligned}
  (pq)(\A)
  &= \sum_{k} \Bigl( \sum_{i + j = k} a_i b_j \Bigr) \A^{k}
  = \sum_{i=0}^{m} \sum_{j=0}^{l} (a_i b_j) \A^{i} \A^{j} \\
  &= \Bigl( \sum_{i=0}^{m} a_i \A^i \Bigr) \Bigl( \sum_{j=0}^{l} b_j \A^j \Bigr) = p(\A)\,q(\A),
  \end{aligned}
\]
where the second equality uses part 1 and @thm-matrix-addition-properties, and the third uses distributivity and the scalar rule \( (a_i \A^i)(b_j \A^j) = (a_i b_j) \A^i \A^j \) from @thm-matrix-multiplication-properties.

For 3, \( pq = qp \) in \( F[x] \) by @thm-polynomial-ring-laws. Hence by part 2, \( p(\A)q(\A) = (pq)(\A) = (qp)(\A) = q(\A)p(\A) \). This proves the theorem.
:::

::: {#exm-polynomial-of-matrix}
[Plugging a matrix into a polynomial]

Let \( \A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix} \in M_2(\nR) \) and \( p = x^2 - 4x + 3 \). Compute \( p(\A) \) directly, and again using the factorization \( p = (x - 1)(x - 3) \).
:::

::: {.solution}
First \( \A^2 = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix} = \begin{pmatrix} 1 & 8 \\ 0 & 9 \end{pmatrix} \). Hence
\[
  p(\A) = \A^2 - 4\A + 3\I_2 = \begin{pmatrix} 1 & 8 \\ 0 & 9 \end{pmatrix} - \begin{pmatrix} 4 & 8 \\ 0 & 12 \end{pmatrix} + \begin{pmatrix} 3 & 0 \\ 0 & 3 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}.
\]
The constant term contributed \( 3\I_2 \), not "\( 3 \)". By @thm-polynomial-of-matrix-properties, \( p(\A) = (\A - \I_2)(\A - 3\I_2) \), and indeed
\[
  (\A - \I_2)(\A - 3\I_2) = \begin{pmatrix} 0 & 2 \\ 0 & 2 \end{pmatrix} \begin{pmatrix} -2 & 2 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}.
\]
Note that neither factor is zero; this is the second warning of the multiplication part in action. That the diagonal entries \( 1, 3 \) of \( \A \) are the roots of \( p \) is no accident, as we will see with eigenvalues.
:::

@thm-polynomial-of-matrix-properties is about polynomials in **one** matrix. Identities with **two** different matrices are another matter.

::: {.warning}
**School identities fail for matrices that do not commute.** Expanding with distributivity, \( (\A + \B)^2 = \A^2 + \A\B + \B\A + \B^2 \), and this equals \( \A^2 + 2\A\B + \B^2 \) only when \( \A\B = \B\A \). With \( \A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) and \( \B = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \): \( (\A + \B)^2 = \I_2 \), but \( \A^2 + 2\A\B + \B^2 = \begin{pmatrix} 2 & 0 \\ 0 & 0 \end{pmatrix} \). Before using a polynomial identity valid for numbers, check that all the matrices involved commute; polynomials in a single \( \A \) always do.
:::

## Two equivalence relations on matrices

We close with two relations on matrices that the rest of the book studies in depth. Both are equivalence relations (@def-equivalence-relation), and the proofs are short exercises in using @thm-inverse-matrix-properties.

::: {#exm-similarity}
[Similarity]

For \( \A, \B \in M_n(F) \), say \( \A \) is **similar** to \( \B \), written \( \A \sim \B \), if there is an **invertible** \( \P \in M_n(F) \) with \( \B = \P^{-1}\A\P \). Prove that similarity is an equivalence relation on \( M_n(F) \). Then check that \( \A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix} \) is similar to \( \diag(1, 3) \) using \( \P = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \), and show that \( \diag(1, 2) \) is **not** similar to \( \I_2 \) over \( \nR \).
:::

::: {.solution}
We check the three conditions of @def-equivalence-relation.

*Reflexive.* Let \( \A \in M_n(F) \). The identity \( \I_n \) is invertible with \( \I_n^{-1} = \I_n \) (@exm-inverse-matrices), and \( \I_n^{-1} \A \I_n = \A \). Hence \( \A \sim \A \).

*Symmetric.* Suppose \( \A \sim \B \), so \( \B = \P^{-1}\A\P \) with \( \P \) invertible. Multiplying on the left by \( \P \) and on the right by \( \P^{-1} \), and using associativity, \( \P\B\P^{-1} = (\P\P^{-1})\A(\P\P^{-1}) = \A \). By @thm-inverse-matrix-properties (part 2), \( \Q = \P^{-1} \) is invertible with \( \Q^{-1} = \P \), so \( \A = \Q^{-1}\B\Q \). Hence \( \B \sim \A \).

*Transitive.* Suppose \( \A \sim \B \) and \( \B \sim \C \), so \( \B = \P^{-1}\A\P \) and \( \C = \Q^{-1}\B\Q \) with \( \P, \Q \) invertible. Then
\[
  \C = \Q^{-1}(\P^{-1}\A\P)\Q = (\Q^{-1}\P^{-1})\A(\P\Q) = (\P\Q)^{-1}\A(\P\Q),
\]
where the last step is @thm-inverse-matrix-properties (part 3), which also says \( \P\Q \) is invertible. Hence \( \A \sim \C \). This shows that similarity is an equivalence relation.

For the numerical part, \( \P^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} \) by @thm-two-by-two-inverse (here \( ad - bc = 1 \)), and
\[
  \P^{-1}\A\P = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 3 \end{pmatrix}.
\]
Finally, if \( \P^{-1} \I_2 \P = \diag(1, 2) \) for some invertible \( \P \), then \( \diag(1, 2) = \P^{-1}\P = \I_2 \), which is false. (Alternatively: similar matrices have equal traces by @thm-trace-properties, and \( \tr \diag(1, 2) = 3 \neq 2 = \tr \I_2 \).) Hence \( \diag(1, 2) \not\sim \I_2 \).
:::

In Chapter 3 we will see that similar matrices describe the same linear map in two different coordinate systems. That is why a quantity like the trace, which similar matrices share, is really a property of the map and not of the matrix. Deciding when two matrices are similar is one of the main problems of this book.

::: {#exm-row-equivalence}
[Row equivalence]

For \( \A, \B \in M_{m \times n}(F) \), say \( \A \) is **row equivalent** to \( \B \) if there is an **invertible** \( \E \in M_m(F) \) with \( \B = \E\A \). Prove that row equivalence is an equivalence relation on \( M_{m \times n}(F) \). Then, with \( \E = \begin{pmatrix} 1 & 0 \\ -2 & 1 \end{pmatrix} \), compute \( \E\A \) for \( \A = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 5 & 0 \end{pmatrix} \) and describe what \( \E \) did to the rows of \( \A \).
:::

::: {.solution}
*Reflexive.* \( \A = \I_m \A \) and \( \I_m \) is invertible, so \( \A \) is row equivalent to itself.

*Symmetric.* Suppose \( \B = \E\A \) with \( \E \) invertible. Multiplying on the left by \( \E^{-1} \), \( \E^{-1}\B = (\E^{-1}\E)\A = \A \), and \( \E^{-1} \) is invertible by @thm-inverse-matrix-properties (part 2). So \( \B \) is row equivalent to \( \A \).

*Transitive.* Suppose \( \B = \E\A \) and \( \C = \E'\B \) with \( \E, \E' \) invertible. Then \( \C = \E'(\E\A) = (\E'\E)\A \) by associativity, and \( \E'\E \) is invertible by @thm-inverse-matrix-properties (part 3). So \( \A \) is row equivalent to \( \C \). This shows that row equivalence is an equivalence relation.

For the computation, \( \E \) is invertible, with inverse \( \begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix} \) (check both products, or use @thm-two-by-two-inverse with \( ad - bc = 1 \)). By the row view of @thm-three-views-of-product and @thm-matrix-times-vector-columns, row 1 of \( \E\A \) is \( 1 \cdot (\text{row } 1 \text{ of } \A) \) and row 2 is \( -2 \cdot (\text{row } 1) + 1 \cdot (\text{row } 2) \):
\[
  \E\A = \begin{pmatrix} 1 & 2 & 1 \\ 2 - 2 & 5 - 4 & 0 - 2 \end{pmatrix} = \begin{pmatrix} 1 & 2 & 1 \\ 0 & 1 & -2 \end{pmatrix}.
\]
So \( \E \) subtracted twice row 1 from row 2, which is the first step of Gaussian elimination on \( \A \).
:::

In Chapter 2 we will see that every elementary row operation is multiplication on the left by an invertible matrix, and that row equivalence is exactly "reachable by a sequence of row operations". This is why Gaussian elimination never changes the solutions of a linear system.

## Exercises

### A. Check your understanding

::: {#exr-matrices-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \A \in M_{2 \times 3}(F) \) and \( \B \in M_{3 \times 4}(F) \). Which of \( \A\B \), \( \B\A \), \( \A\tp \A \) and \( \B\tp \A\tp \) are defined? Give the size of each one that is.
2. Define what it means for \( \A \in M_n(F) \) to be invertible.
3. Determine whether the following statement is true: "if \( \A, \B \in M_n(F) \) and \( \A\B = 0 \), then \( \A = 0 \) or \( \B = 0 \)." Justify your answer.
4. Determine whether the following statement is true: "\( (\A + \B)(\A - \B) = \A^2 - \B^2 \) for all \( \A, \B \in M_2(\nR) \)." Justify your answer.
5. Let \( \A \in M_{3}(F) \) have columns \( \a_1, \a_2, \a_3 \). Express \( \A(2, 0, -1) \) and the second column of \( \A^2 \) in terms of the columns of \( \A \) and \( \A \) itself.
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. \( \A\B \) is \( (2 \times 3)(3 \times 4) \), defined, of size \( 2 \times 4 \). \( \B\A \) would pair rows of length \( 4 \) with columns of length \( 2 \), so it is not defined. \( \A\tp \A \) is \( (3 \times 2)(2 \times 3) \), defined, of size \( 3 \times 3 \). \( \B\tp \A\tp \) is \( (4 \times 3)(3 \times 2) \), defined, of size \( 4 \times 2 \); it equals \( (\A\B)\tp \) by @thm-transpose-properties.
2. \( \A \) is invertible if there exists \( \B \in M_n(F) \) with \( \A\B = \I_n \) **and** \( \B\A = \I_n \).
3. False. \( \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix} = 0 \) with both factors non-zero.
4. False. Expanding gives \( (\A + \B)(\A - \B) = \A^2 - \A\B + \B\A - \B^2 \), which differs from \( \A^2 - \B^2 \) unless \( \A\B = \B\A \). For \( \A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) and \( \B = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \), we have \( \A^2 = \B^2 = 0 \), but \( (\A + \B)(\A - \B) = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix} \neq 0 \).
5. By @thm-matrix-times-vector-columns, \( \A(2, 0, -1) = 2\a_1 - \a_3 \). By @thm-three-views-of-product, the second column of \( \A^2 = \A\A \) is \( \A\a_2 \).
:::
:::

### B. Practice

::: {#exr-matrices-b1}
[B1: Products and sizes]

Let
\[
  \A = \begin{pmatrix} 1 & -1 & 2 \\ 0 & 3 & 1 \end{pmatrix}, \quad
  \B = \begin{pmatrix} 2 & 1 \\ 1 & 0 \\ 0 & 4 \end{pmatrix}, \quad
  \C = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}
\]
over \( \nR \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \A\B \) and \( \B\A \).
2. Determine which of \( \A\C \) and \( \C\A \) is defined, and compute it.
3. Compute \( \A\x \) for \( \x = (2, 0, -1) \) as a combination of the columns of \( \A \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. \( \A\B \) is \( 2 \times 2 \) and \( \B\A \) is \( 3 \times 3 \). Row against column,
\[
  \A\B = \begin{pmatrix} 2 - 1 + 0 & 1 + 0 + 8 \\ 0 + 3 + 0 & 0 + 0 + 4 \end{pmatrix} = \begin{pmatrix} 1 & 9 \\ 3 & 4 \end{pmatrix},
  \qquad
  \B\A = \begin{pmatrix} 2 & 1 & 5 \\ 1 & -1 & 2 \\ 0 & 12 & 4 \end{pmatrix}.
\]
For instance \( (\B\A)_{12} = 2 \cdot (-1) + 1 \cdot 3 = 1 \) and \( (\B\A)_{32} = 0 \cdot (-1) + 4 \cdot 3 = 12 \).
2. \( \A\C \) would be \( (2 \times 3)(2 \times 2) \), and \( 3 \neq 2 \), so it is not defined. \( \C\A \) is \( (2 \times 2)(2 \times 3) \), of size \( 2 \times 3 \):
\[
  \C\A = \begin{pmatrix} 1 & -1 + 6 & 2 + 2 \\ 3 & -3 + 12 & 6 + 4 \end{pmatrix} = \begin{pmatrix} 1 & 5 & 4 \\ 3 & 9 & 10 \end{pmatrix}.
\]
3. By @thm-matrix-times-vector-columns, \( \A\x = 2\a_1 + 0\a_2 - \a_3 = 2(1, 0) - (2, 1) = (0, -1) \).
:::
:::

::: {#exr-matrices-b2}
[B2: Traces of products]

::: {.enumerate options="label=(\alph*)"}
1. With \( \A \) and \( \B \) as in @exr-matrices-b1, verify that \( \tr(\A\B) = \tr(\B\A) \), although \( \A\B \) and \( \B\A \) have different sizes.
2. Let \( \A = \diag(1, 2) \), \( \B = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) and \( \C = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \). Show that \( \tr(\A\B\C) \neq \tr(\B\A\C) \), and verify that \( \tr(\A\B\C) = \tr(\C\A\B) \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. From @exr-matrices-b1, \( \tr(\A\B) = 1 + 4 = 5 \) and \( \tr(\B\A) = 2 + (-1) + 4 = 5 \), as @thm-trace-properties predicts.
2. By the column view, \( \B\C \) has columns \( \B\e_2 = \e_1 \) and \( \B\0 = \0 \), so \( \B\C = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \), and \( \A\B\C = \A(\B\C) = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \), with trace \( 1 \). Next, \( \B\A = \begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix} \), so \( \B\A\C = \begin{pmatrix} 2 & 0 \\ 0 & 0 \end{pmatrix} \), with trace \( 2 \). Hence \( \tr(\A\B\C) = 1 \neq 2 = \tr(\B\A\C) \). Finally \( \A\B = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) and \( \C\A\B = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} \), with trace \( 1 = \tr(\A\B\C) \), as the cyclic rule predicts.
:::
:::

::: {#exr-matrices-b3}
[B3: Inverses of \( 2 \times 2 \) matrices]

::: {.enumerate options="label=(\alph*)"}
1. Find the inverse of \( \begin{pmatrix} 3 & 4 \\ 2 & 3 \end{pmatrix} \in M_2(\nR) \), and check both products.
2. Show that \( \A = \begin{pmatrix} 2 & 6 \\ 1 & 3 \end{pmatrix} \) is not invertible by finding a non-zero \( \x \) with \( \A\x = \0 \).
3. Find the inverse of \( \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \in M_2(\nF_5) \).
4. For which \( t \in \nR \) is \( \begin{pmatrix} t & 2 \\ 2 & t \end{pmatrix} \) invertible?
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Here \( ad - bc = 9 - 8 = 1 \neq 0 \), so by @thm-two-by-two-inverse the inverse is \( \B = \begin{pmatrix} 3 & -4 \\ -2 & 3 \end{pmatrix} \). Check: \( \begin{pmatrix} 3 & 4 \\ 2 & 3 \end{pmatrix} \B = \begin{pmatrix} 9 - 8 & -12 + 12 \\ 6 - 6 & -8 + 9 \end{pmatrix} = \I_2 \) and \( \B \begin{pmatrix} 3 & 4 \\ 2 & 3 \end{pmatrix} = \begin{pmatrix} 9 - 8 & 12 - 12 \\ -6 + 6 & -8 + 9 \end{pmatrix} = \I_2 \).
2. Here \( ad - bc = 6 - 6 = 0 \). Following the proof of @thm-two-by-two-inverse, take \( \x = (d, -c) = (3, -1) \neq \0 \). Then \( \A\x = (6 - 6, 3 - 3) = \0 \). If \( \A \) were invertible, then \( \x = \A^{-1}(\A\x) = \0 \), a contradiction. Hence \( \A \) is not invertible.
3. In \( \nF_5 \), \( ad - bc = 4 - 6 = -2 = 3 \neq 0 \), and \( 3^{-1} = 2 \) since \( 3 \cdot 2 = 6 = 1 \). By @thm-two-by-two-inverse the inverse is \( 2 \begin{pmatrix} 4 & -2 \\ -3 & 1 \end{pmatrix} = \begin{pmatrix} 8 & -4 \\ -6 & 2 \end{pmatrix} = \begin{pmatrix} 3 & 1 \\ 4 & 2 \end{pmatrix} \). Check: \( \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 3 & 1 \\ 4 & 2 \end{pmatrix} = \begin{pmatrix} 11 & 5 \\ 25 & 11 \end{pmatrix} = \I_2 \) and \( \begin{pmatrix} 3 & 1 \\ 4 & 2 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = \begin{pmatrix} 6 & 10 \\ 10 & 16 \end{pmatrix} = \I_2 \) in \( \nF_5 \).
4. By @thm-two-by-two-inverse, it is invertible if and only if \( t^2 - 4 \neq 0 \), that is, \( t \neq 2 \) and \( t \neq -2 \).
:::
:::

::: {#exr-matrices-b4}
[B4: Transposes of products]

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( (\A_1 \A_2 \cdots \A_k)\tp = \A_k\tp \cdots \A_2\tp \A_1\tp \) for all \( k \ge 1 \) and matrices \( \A_1, \dots, \A_k \) whose sizes allow the product.
2. Let \( \A \in M_n(F) \). Prove that \( \A + \A\tp \) is symmetric and \( \A - \A\tp \) is skew-symmetric.
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. We use induction on \( k \) (@thm-induction). For \( k = 1 \) there is nothing to prove. Suppose the formula holds for products of \( k \) matrices, and let \( \A_1, \dots, \A_{k+1} \) be given. By associativity, \( \A_1 \cdots \A_{k+1} = (\A_1 \cdots \A_k)\A_{k+1} \). By @thm-transpose-properties (part 4) and then the induction hypothesis,
\[
  (\A_1 \cdots \A_{k+1})\tp = \A_{k+1}\tp (\A_1 \cdots \A_k)\tp = \A_{k+1}\tp \A_k\tp \cdots \A_1\tp .
\]
This proves the formula for all \( k \ge 1 \).
2. By @thm-transpose-properties (parts 1–3), \( (\A + \A\tp)\tp = \A\tp + (\A\tp)\tp = \A\tp + \A = \A + \A\tp \), so \( \A + \A\tp \) is symmetric. Similarly \( (\A - \A\tp)\tp = \A\tp - \A = -(\A - \A\tp) \), so \( \A - \A\tp \) is skew-symmetric.
:::
:::

### C. Going deeper

::: {#exr-matrices-c1}
[C1: \( \A\B - \B\A = \I \) is impossible, or is it?]

::: {.enumerate options="label=(\alph*)"}
1. Prove that there are no \( \A, \B \in M_n(\nR) \), for any \( n \ge 1 \), with \( \A\B - \B\A = \I_n \).
2. Show that the argument of (a) breaks down in \( M_2(\nF_2) \), and that \( \A = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \), \( \B = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) satisfy \( \A\B - \B\A = \I_2 \) over \( \nF_2 \).
:::

*Hint: consider the trace of both sides.*
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Suppose, for a contradiction, that \( \A\B - \B\A = \I_n \). Taking traces and using @thm-trace-properties (parts 1 and 3),
\[
  n = \tr \I_n = \tr(\A\B - \B\A) = \tr(\A\B) - \tr(\B\A) = 0 .
\]
This contradicts \( n \ge 1 \). Hence no such \( \A, \B \) exist.
2. Over \( \nF_2 \) the same computation gives \( \tr \I_2 = 1 + 1 = 0 \), so taking traces yields \( 0 = 0 \) and no contradiction. For the given matrices, the column view gives \( \A\B = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} \) and \( \B\A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \), so \( \A\B - \B\A = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \I_2 \), because \( -1 = 1 \) in \( \nF_2 \).
:::
:::

::: {#exr-matrices-c2}
[C2: Triangular matrices with non-zero diagonal]

Let \( F \) be a field.

::: {.enumerate options="label=(\alph*)"}
1. Let \( \U = \begin{pmatrix} a & b \\ 0 & d \end{pmatrix} \) with \( a, d \neq 0 \). Show that \( \U \) is invertible and that \( \U^{-1} \) is upper triangular.
2. Let \( \U = \begin{pmatrix} a & b & c \\ 0 & d & e \\ 0 & 0 & f \end{pmatrix} \) with \( a, d, f \neq 0 \). Show that
\[
  \V = \begin{pmatrix} a^{-1} & -b(ad)^{-1} & (be - cd)(adf)^{-1} \\ 0 & d^{-1} & -e(df)^{-1} \\ 0 & 0 & f^{-1} \end{pmatrix}
\]
is the inverse of \( \U \).
3. Explain how the entries of \( \V \) can be found, column by column, by solving \( \U\v_k = \e_k \).
:::

*The general case, for all \( n \), follows from the methods of Chapter 2.*
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Here \( ad - b \cdot 0 = ad \neq 0 \), since a product of non-zero elements of a field is non-zero (@thm-field-basic-properties). By @thm-two-by-two-inverse, \( \U \) is invertible with \( \U^{-1} = (ad)^{-1} \begin{pmatrix} d & -b \\ 0 & a \end{pmatrix} = \begin{pmatrix} a^{-1} & -b(ad)^{-1} \\ 0 & d^{-1} \end{pmatrix} \), which is upper triangular.
2. The inverses \( a^{-1}, d^{-1}, f^{-1} \) exist, and \( ad, df, adf \neq 0 \) by @thm-field-basic-properties, so \( \V \) is defined. We check \( \U\V = \I_3 \) entry by entry. The diagonal entries are \( a \cdot a^{-1} = 1 \), \( d \cdot d^{-1} = 1 \), \( f \cdot f^{-1} = 1 \). Below the diagonal both matrices are zero, so \( (\U\V)_{21} = (\U\V)_{31} = (\U\V)_{32} = 0 \). Above the diagonal,
\[
  \begin{aligned}
  (\U\V)_{12} &= a \cdot \bigl(-b(ad)^{-1}\bigr) + b d^{-1} = -bd^{-1} + bd^{-1} = 0, \\
  (\U\V)_{23} &= d \cdot \bigl(-e(df)^{-1}\bigr) + e f^{-1} = -ef^{-1} + ef^{-1} = 0, \\
  (\U\V)_{13} &= a (be - cd)(adf)^{-1} + b\bigl(-e(df)^{-1}\bigr) + c f^{-1} \\
  &= (be - cd)(df)^{-1} - be(df)^{-1} + cd(df)^{-1} = 0 .
  \end{aligned}
\]
Hence \( \U\V = \I_3 \). For \( \V\U \), again the diagonal entries are \( 1 \) and the entries below the diagonal are \( 0 \), and
\[
  \begin{aligned}
  (\V\U)_{12} &= a^{-1} b - b(ad)^{-1} d = a^{-1}b - a^{-1}b = 0, \\
  (\V\U)_{23} &= d^{-1} e - e(df)^{-1} f = 0, \\
  (\V\U)_{13} &= a^{-1} c - b(ad)^{-1} e + (be - cd)(adf)^{-1} f \\
  &= a^{-1}c - be(ad)^{-1} + be(ad)^{-1} - cd(ad)^{-1} = 0,
  \end{aligned}
\]
using \( cd(ad)^{-1} = ca^{-1} \). Hence \( \V\U = \I_3 \), and \( \V = \U^{-1} \). Both products had to be checked, since we may not yet use that one implies the other.
3. By @thm-three-views-of-product, \( \U\V = \I_3 \) says exactly that the columns \( \v_1, \v_2, \v_3 \) of \( \V \) satisfy \( \U\v_k = \e_k \). Because \( \U \) is upper triangular, each system can be solved from the bottom row up. For example, \( \U\v_3 = \e_3 \) reads \( f x_3 = 1 \), \( d x_2 + e x_3 = 0 \), \( a x_1 + b x_2 + c x_3 = 0 \), giving \( x_3 = f^{-1} \), then \( x_2 = -e(df)^{-1} \), then \( x_1 = (be - cd)(adf)^{-1} \), which is the third column of \( \V \). (This only finds a candidate satisfying \( \U\V = \I_3 \); the check \( \V\U = \I_3 \) in (b) is still needed.)
:::
:::

::: {#exr-matrices-c3}
[C3: Matrices that commute]

Let \( \N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \in M_2(\nR) \).

::: {.enumerate options="label=(\alph*)"}
1. Find all \( \X \in M_2(\nR) \) with \( \X\N = \N\X \).
2. Deduce that the only matrices \( \X \in M_2(\nR) \) with \( \X\Y = \Y\X \) **for every** \( \Y \in M_2(\nR) \) are the scalar multiples \( c\I_2 \), \( c \in \nR \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Let \( \X = \begin{pmatrix} p & q \\ r & s \end{pmatrix} \). By the column view, \( \X\N = \begin{pmatrix} \X\0 & \X\e_1 \end{pmatrix} = \begin{pmatrix} 0 & p \\ 0 & r \end{pmatrix} \), and by the row view, \( \N\X \) has rows \( (\text{row } 2 \text{ of } \X) \) and \( \0 \): \( \N\X = \begin{pmatrix} r & s \\ 0 & 0 \end{pmatrix} \). Comparing entries, \( \X\N = \N\X \) if and only if \( r = 0 \) and \( p = s \), that is, \( \X = \begin{pmatrix} p & q \\ 0 & p \end{pmatrix} = p\I_2 + q\N \) with \( p, q \in \nR \) arbitrary.
2. Every \( c\I_2 \) commutes with every \( \Y \), by @thm-matrix-multiplication-properties: \( (c\I_2)\Y = c\Y = \Y(c\I_2) \). Conversely, suppose \( \X\Y = \Y\X \) for every \( \Y \). Taking \( \Y = \N \), part (a) gives \( \X = \begin{pmatrix} p & q \\ 0 & p \end{pmatrix} \). Taking \( \Y = \N\tp = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \), we compute \( \X\N\tp = \begin{pmatrix} q & 0 \\ p & 0 \end{pmatrix} \) and \( \N\tp \X = \begin{pmatrix} 0 & 0 \\ p & q \end{pmatrix} \). Equality forces \( q = 0 \). Hence \( \X = p\I_2 \), as claimed.
:::
:::
