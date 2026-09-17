# LU and PLU Factorizations

Gaussian elimination solves one system \( A\x = \b \). In practice the matrix often stays fixed while the right-hand side changes: the same network under different loads, the same model fed different data. The row operations depend only on \( A \), so repeating them for every \( \b \) wastes almost all of the work. This section stores the elimination as a factorization \( A = LU \), a lower triangular matrix that remembers the operations times an upper triangular matrix that is their result. We prove when it exists and when it is unique, and we repair its failures with row swaps.

Throughout, \( F \) is a field and all matrices are square, in \( M_n(F) \).

## Triangular systems are cheap

Some systems need no elimination at all. Take
\[
U = \begin{pmatrix} 2 & 1 & -1 \\ 0 & 3 & 1 \\ 0 & 0 & -2 \end{pmatrix}, \qquad
U\x = \begin{pmatrix} -1 \\ -1 \\ -4 \end{pmatrix}.
\]
The last equation mentions only \( x_3 \): \( -2x_3 = -4 \), so \( x_3 = 2 \). The second mentions \( x_2 \) and the known \( x_3 \): \( 3x_2 + 2 = -1 \), so \( x_2 = -1 \). The first then gives \( 2x_1 - 1 - 2 = -1 \), so \( x_1 = 1 \). This is **back substitution**: in an upper triangular system with non-zero diagonal entries, each equation introduces exactly one new unknown, read from the bottom up. A lower triangular system is solved the same way from the top down, by **forward substitution**.

Now suppose a matrix \( A \) factors as \( A = LU \) with \( L \) lower triangular and \( U \) upper triangular. Then \( A\x = \b \) reads \( L(U\x) = \b \). Naming the inner vector \( \y = U\x \) splits the problem in two:
\[
\text{first solve } L\y = \b \text{ for } \y, \qquad \text{then solve } U\x = \y \text{ for } \x .
\]
Both are triangular, so both are cheap. The expensive part, finding \( L \) and \( U \), is done once for all right-hand sides.

*An LU factorization is Gaussian elimination written down once, so that it never has to be done again.*

## LU factorizations

::: {#def-lu-factorization}
[LU factorization]

A matrix \( L \in M_n(F) \) is **unit lower triangular** if it is lower triangular and **every** diagonal entry equals \( 1 \). Let \( A \in M_n(F) \). An **LU factorization** of \( A \) is a pair \( (L, U) \) of matrices in \( M_n(F) \) such that
\[
A = LU, \qquad L \text{ is **unit** lower triangular}, \qquad U \text{ is upper triangular}.
\]
:::

In words: \( L \) has \( 1 \)'s on the diagonal and zeros above it, and the entries below the diagonal are unrestricted. \( U \) has zeros strictly below the diagonal, and its diagonal entries are unrestricted; some of them may be \( 0 \). The definition says **an** factorization: whether there is only one is a theorem, and it needs a hypothesis.

::: {#exm-lu-by-elimination}
[An LU factorization from elimination]

Let
\[
A = \begin{pmatrix} 2 & 1 & -1 \\ 4 & 5 & -1 \\ -2 & 8 & 2 \end{pmatrix} \in M_3(\nQ).
\]
Reduce \( A \) to upper triangular form using only operations "subtract a multiple of a higher row from a lower row", and record each multiplier. Compare the result with the matrix \( U \) of the previous subsection.
:::

::: {.solution}
The first pivot is \( 2 \). To clear column 1 below it we subtract \( \ell_{21} = 4/2 = 2 \) times row 1 from row 2, and \( \ell_{31} = -2/2 = -1 \) times row 1 from row 3:
\[
\begin{pmatrix} 2 & 1 & -1 \\ 4 & 5 & -1 \\ -2 & 8 & 2 \end{pmatrix}
\xrightarrow[R_3 \to R_3 - (-1)R_1]{R_2 \to R_2 - 2R_1}
\begin{pmatrix} 2 & 1 & -1 \\ 0 & 3 & 1 \\ 0 & 9 & 1 \end{pmatrix}.
\]
The second pivot is \( 3 \). We subtract \( \ell_{32} = 9/3 = 3 \) times row 2 from row 3:
\[
\begin{pmatrix} 2 & 1 & -1 \\ 0 & 3 & 1 \\ 0 & 9 & 1 \end{pmatrix}
\xrightarrow{R_3 \to R_3 - 3R_2}
\begin{pmatrix} 2 & 1 & -1 \\ 0 & 3 & 1 \\ 0 & 0 & -2 \end{pmatrix} = U.
\]
Put the multipliers below the diagonal of a unit lower triangular matrix, each in the position of the entry it cleared:
\[
L = \begin{pmatrix} 1 & 0 & 0 \\ \ell_{21} & 1 & 0 \\ \ell_{31} & \ell_{32} & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ -1 & 3 & 1 \end{pmatrix}.
\]
Multiplying out, row by row,
\[
LU = \begin{pmatrix} 2 & 1 & -1 \\ 2 \cdot 2 & 2 \cdot 1 + 3 & 2 \cdot (-1) + 1 \\ -2 & -1 + 9 & 1 + 3 - 2 \end{pmatrix} = \begin{pmatrix} 2 & 1 & -1 \\ 4 & 5 & -1 \\ -2 & 8 & 2 \end{pmatrix} = A .
\]
So \( (L, U) \) is an LU factorization of \( A \), and \( U \) is exactly the triangular matrix of the back substitution above.
:::

The example suggests the general statement: elimination produces \( U \), and the multipliers, **with their signs as subtracted**, fill in \( L \). We prove this below. First, the smallest cases.

- **Upper triangular \( A \).** \( A = I \cdot A \), and \( I \) is unit lower triangular. So every upper triangular matrix, including \( 0 \) and \( I \), has the LU factorization \( (I, A) \).
- **\( 1 \times 1 \).** Every \( (a) \in M_1(F) \) is upper triangular, so \( (a) = (1)(a) \). Nothing can go wrong here, and that is exactly why the \( 2 \times 2 \) failure below is instructive.

**Non-example by minimal change.** The matrix \( \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} \) has the LU factorization
\[
\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & -1 \end{pmatrix}.
\]
Change the top-left entry from \( 1 \) to \( 0 \), and everything collapses.

::: {#exm-no-lu-factorization}
[An invertible matrix with no LU factorization]

Show that \( A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \in M_2(F) \) has **no** LU factorization, over any field \( F \), although \( A \) is invertible.
:::

::: {.solution}
\( A \) is invertible, since \( AA = I_2 \). Suppose, for a contradiction, that \( A = LU \) with
\[
L = \begin{pmatrix} 1 & 0 \\ \ell & 1 \end{pmatrix}, \qquad U = \begin{pmatrix} u & v \\ 0 & w \end{pmatrix}.
\]
Then
\[
LU = \begin{pmatrix} u & v \\ \ell u & \ell v + w \end{pmatrix}.
\]
Comparing \( (1, 1) \)-entries with \( A \) gives \( u = 0 \). Comparing \( (2, 1) \)-entries gives \( \ell u = 1 \). But \( \ell u = \ell \cdot 0 = 0 \) by @thm-field-basic-properties, and \( 0 \neq 1 \) in a field. This contradiction shows that no LU factorization exists.
:::

What failed is visible: the \( (1, 1) \)-entry of any product \( LU \) is \( u_{11} \) alone, so a zero there forces the whole first column of \( LU \) to vanish. In elimination terms, the first pivot is \( 0 \) while the entry below it is not, and the only cure is to **swap** rows, which "subtract a multiple of a higher row from a lower row" cannot do. We return to this with permutation matrices.

**Why "unit".** Without the \( 1 \)'s on the diagonal of \( L \), uniqueness would fail even for invertible matrices. If \( A = LU \) and \( D \) is any invertible diagonal matrix, then also \( A = (LD)(D^{-1}U) \), where \( LD \) is still lower triangular and \( D^{-1}U \) still upper triangular. When \( L \) is invertible and \( D \neq I \), this is a different pair, and over any field with more than two elements such a \( D \) exists. For instance \( \begin{pmatrix} 2 \end{pmatrix} = \begin{pmatrix} 1 \end{pmatrix}\begin{pmatrix} 2 \end{pmatrix} = \begin{pmatrix} 2 \end{pmatrix}\begin{pmatrix} 1 \end{pmatrix} = \begin{pmatrix} 4 \end{pmatrix}\begin{pmatrix} 1/2 \end{pmatrix} \) over \( \nQ \). Fixing the diagonal of \( L \) removes this freedom and matches what elimination does: it never rescales a row.

::: {.warning}
**Invertible does not mean "has an LU factorization".** The matrix of @exm-no-lu-factorization is invertible and has none. Conversely, a singular matrix can have one: \( 0 = I \cdot 0 \). Existence of an LU factorization is a property of the **order of the rows**, not of invertibility.
:::

## Unit lower triangular matrices

Elimination builds \( L \) out of elementary matrices, and the uniqueness proof below divides one factorization by another. Both need the same facts: products and inverses of unit lower triangular matrices stay unit lower triangular. We also need to know exactly when a triangular matrix is invertible.

The key observation is a statement about where the non-zero entries of a product can sit.

::: {#lem-unit-lower-triangular-closed}
[Unit lower triangular matrices are closed]

Let \( L, L' \in M_n(F) \) be unit lower triangular. Then:

::: {.enumerate options="label=(\alph*)"}
1. \( LL' \) is unit lower triangular;
2. \( L \) is invertible, and \( L^{-1} \) is unit lower triangular.
:::
:::

::: {.idea}
Write \( L = I + N \), where \( N \) has non-zero entries only strictly below the diagonal. Multiplying two such matrices pushes the non-zero entries **further** below the diagonal, so \( N^n = 0 \). Then the geometric series \( 1/(1 + t) = 1 - t + t^2 - \cdots \) stops after \( n \) terms and gives the inverse exactly.
:::

::: {.proof}
Say that \( X \in M_n(F) \) is **\( p \)-low** if \( x_{ij} = 0 \) whenever \( i < j + p \). So \( 0 \)-low means lower triangular, and \( 1 \)-low means zero on and above the diagonal.

::: {.claim}
If \( X \) is \( p \)-low and \( Y \) is \( q \)-low, then \( XY \) is \( (p + q) \)-low. A matrix that is \( n \)-low is the zero matrix.
:::

::: {.proof}
By @def-matrix-multiplication, \( (XY)_{ij} = \sum_{l=1}^{n} x_{il} y_{lj} \). A term can be non-zero only if \( i \ge l + p \) and \( l \ge j + q \), which together give \( i \ge j + p + q \). So if \( i < j + p + q \), every term is \( 0 \) and \( (XY)_{ij} = 0 \). For the second statement, every pair of indices satisfies \( i \le n < 1 + n \le j + n \), so every entry of an \( n \)-low matrix is \( 0 \).
:::

Write \( L = I + N \) and \( L' = I + N' \). Since \( L \) and \( L' \) are unit lower triangular, \( N \) and \( N' \) are \( 1 \)-low.

For (a), \( LL' = I + N + N' + NN' \) by @thm-matrix-multiplication-properties. Here \( N + N' \) is \( 1 \)-low, since a sum of entries that are both \( 0 \) is \( 0 \), and \( NN' \) is \( 2 \)-low, hence \( 1 \)-low, by the Claim. So \( LL' - I \) is \( 1 \)-low, which says that \( LL' \) is unit lower triangular.

For (b), let \( K = I - N + N^2 - \dots + (-1)^{n-1} N^{n-1} \). Multiplying out, the sum telescopes:
\[
(I + N)K = I + (-1)^{n-1} N^{n} = I,
\]
where \( N^n = 0 \) because \( N^n \) is \( n \)-low by the Claim applied \( n - 1 \) times. The same computation gives \( K(I + N) = I \), since \( N \) commutes with its own powers. Hence \( L \) is invertible with \( L^{-1} = K \). Finally \( K - I = \sum_{p=1}^{n-1} (-1)^p N^p \) is a sum of \( 1 \)-low matrices, by the Claim, so \( K \) is unit lower triangular. This proves the lemma.
:::

Transposing everything, the same statements hold for **unit upper triangular** matrices (upper triangular with \( 1 \)'s on the diagonal).

The next lemma decides invertibility of a triangular matrix from its diagonal, without any computation beyond back substitution.

::: {#lem-triangular-invertible}
[Invertibility of a triangular matrix]

An upper triangular matrix \( U \in M_n(F) \) is invertible if and only if **every** diagonal entry \( u_{11}, \dots, u_{nn} \) is non-zero.
:::

::: {.proof}
(⇐) Suppose every \( u_{kk} \neq 0 \), and let \( U\x = \0 \). We show \( x_k = 0 \) for \( k = n, n-1, \dots, 1 \) in turn. Suppose \( x_{k+1} = \dots = x_n = 0 \) (nothing is assumed when \( k = n \)). Row \( k \) of \( U\x = \0 \) reads \( u_{kk} x_k + \sum_{j > k} u_{kj} x_j = 0 \), because \( u_{kj} = 0 \) for \( j < k \). The sum vanishes, so \( u_{kk} x_k = 0 \), and \( x_k = 0 \) since \( u_{kk} \neq 0 \). Hence \( \x = \0 \) is the only solution of \( U\x = \0 \), and \( U \) is invertible by @thm-invertible-tfae.

(⇒) We prove the contrapositive. Suppose \( u_{kk} = 0 \) for some \( k \). For each \( j \le k \), the entries of column \( j \) in rows \( i \ge k \) are zero: if \( i > j \) this is upper triangularity, and the only remaining case \( i = j = k \) is \( u_{kk} = 0 \). So the first \( k \) columns of \( U \) lie in \( W = \Span(\e_1, \dots, \e_{k-1}) \). The list \( (\e_1, \dots, \e_{k-1}) \) is independent and spans \( W \), so \( \dim W = k - 1 \) (for \( k = 1 \), \( W = \{\0\} \) has dimension \( 0 \)). By @thm-size-bounds (a), these \( k \) columns are linearly dependent, so the columns of \( U \) are dependent, and \( U \) is not invertible by @thm-invertible-tfae. This proves the lemma.
:::

## Elimination without row swaps

To prove that elimination always produces an LU factorization, we first need to say exactly which elimination we mean. It is Gaussian elimination restricted to one kind of operation: subtracting a multiple of a row from a row **below** it.

::: {.algorithm}
**Elimination without row swaps.** Input: \( A \in M_n(F) \). Put \( A^{(0)} = A \). For \( k = 1, 2, \dots, n - 1 \), write \( A^{(k-1)} = (a_{ij}) \) and do the following.

- If \( a_{kk} \neq 0 \), set \( \ell_{ik} = a_{ik} / a_{kk} \) for \( i = k+1, \dots, n \).
- If \( a_{kk} = 0 \) and \( a_{ik} = 0 \) for **every** \( i > k \), set \( \ell_{ik} = 0 \) for \( i = k+1, \dots, n \).
- If \( a_{kk} = 0 \) but \( a_{ik} \neq 0 \) for **some** \( i > k \), **stop**: a row swap is needed.

If we did not stop, obtain \( A^{(k)} \) from \( A^{(k-1)} \) by replacing row \( i \) with (row \( i \)) \( - \ell_{ik} \cdot \) (row \( k \)), for each \( i = k+1, \dots, n \).

If the loop finishes without stopping, we say **elimination without row swaps succeeds** on \( A \). The numbers \( \ell_{ik} \) (\( i > k \)) are its **multipliers**, and \( U = A^{(n-1)} \) is its **result**.
:::

In both non-stopping cases the new \( (i, k) \)-entry is \( a_{ik} - \ell_{ik} a_{kk} = 0 \): in the first case by the choice of \( \ell_{ik} \), in the second because both terms are already \( 0 \). The multipliers are well defined: row \( k \) is not changed during step \( k \), so it does not matter in which order the rows \( i > k \) are updated.

The proof will write each step as a matrix. By @def-elementary-matrix, the elementary matrix of the operation \( R_i \to R_i + cR_k \) (\( i \neq k \)) is \( I + cE_{ik} \), where \( E_{ik} \) is the matrix unit with \( 1 \) in entry \( (i, k) \). We will write the matrix unit as a product of a column and a row,
\[
E_{ik} = \e_i \e_k\tp ,
\]
which holds because \( \e_i \e_k\tp \) has \( (p, q) \)-entry \( (\e_i)_p (\e_k)_q \), equal to \( 1 \) if \( p = i \) and \( q = k \), and \( 0 \) otherwise.
We will use one more rule constantly: for a vector \( \v \in F^n \), the \( 1 \times 1 \) matrix \( \e_k\tp \v \) is the \( k \)-th entry \( v_k \), which we treat as a scalar. In particular \( \e_k\tp \e_j = 0 \) for \( j \neq k \).

For \( 1 \le k \le n \) and a vector \( \v \in F^n \) whose first \( k \) entries are zero, put
\[
G_k(\v) = I + \v\, \e_k\tp .
\]
Its only non-identity entries are \( v_i \) in position \( (i, k) \), for \( i > k \): it is the identity with the column vector \( \v \) written into column \( k \) below the diagonal. So \( G_k(\v) \) is unit lower triangular.

::: {#lem-elimination-matrices}
[Multiplier matrices]

Let \( 1 \le k \le n \), and let \( \v, \v_1, \dots, \v_m \in F^n \) be vectors such that the first \( k \) entries of \( \v \) are zero and, for each \( j \), the first \( j \) entries of \( \v_j \) are zero (\( m \le n \)). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( G_k(\v) \) is the product, in any order, of the elementary matrices \( I + v_i E_{ik} \) for \( i = k+1, \dots, n \);
2. \( G_k(\v) G_k(-\v) = G_k(-\v) G_k(\v) = I \);
3. \( G_1(\v_1) G_2(\v_2) \cdots G_m(\v_m) = I + \v_1 \e_1\tp + \v_2 \e_2\tp + \dots + \v_m \e_m\tp \).
:::
:::

::: {.proof}
For (a), let \( i, j > k \). By @thm-matrix-multiplication-properties,
\[
(I + a\, \e_i \e_k\tp)(I + b\, \e_j \e_k\tp) = I + a\, \e_i \e_k\tp + b\, \e_j \e_k\tp + ab\, \e_i (\e_k\tp \e_j) \e_k\tp ,
\]
and the last term is zero because \( \e_k\tp \e_j = 0 \) for \( j \neq k \). Repeating this, one factor at a time, the product of the \( I + v_iE_{ik} = I + v_i \e_i \e_k\tp \) in any order is \( I + \sum_{i > k} v_i \e_i \e_k\tp = I + \v\, \e_k\tp \), since \( \v = \sum_{i > k} v_i \e_i \).

For (b), \( (I + \v\, \e_k\tp)(I - \v\, \e_k\tp) = I - \v (\e_k\tp \v) \e_k\tp = I \), because \( \e_k\tp \v = v_k = 0 \). Swapping the signs gives the other order.

For (c), we use induction on \( m \); the case \( m = 1 \) is the definition. Suppose the formula holds for \( m - 1 \). Then
\[
\Bigl(I + \sum_{j < m} \v_j \e_j\tp\Bigr)(I + \v_m \e_m\tp) = I + \sum_{j < m} \v_j \e_j\tp + \v_m \e_m\tp + \sum_{j < m} \v_j (\e_j\tp \v_m) \e_m\tp .
\]
For \( j < m \), \( \e_j\tp \v_m \) is entry \( j \) of \( \v_m \), which is zero because the first \( m \) entries of \( \v_m \) are zero. So the last sum vanishes, and the formula holds for \( m \). This proves the lemma.
:::

Part (c) is the heart of the matter: when the factors come in the order \( G_1, G_2, \dots \), they **do not interfere**, and each vector \( \v_j \) lands untouched in column \( j \).

::: {#thm-lu-exists-without-swaps}
[LU from elimination]

Let \( A \in M_n(F) \), and suppose elimination without row swaps succeeds on \( A \), with multipliers \( \ell_{ik} \) and result \( U \). Let \( L \) be the unit lower triangular matrix whose \( (i, k) \)-entry is \( \ell_{ik} \) for every \( i > k \). Then \( U \) is upper triangular and
\[
A = LU .
\]
In particular \( A \) has an LU factorization.
:::

::: {.idea}
Each step of elimination is left multiplication by a product of elementary matrices, which collapses to one matrix \( G_k(-\boldsymbol{\ell}_k) \). So \( U = G_{n-1}(-\boldsymbol{\ell}_{n-1}) \cdots G_1(-\boldsymbol{\ell}_1) A \). To get \( A \) back, undo the steps in reverse order. Their inverses \( G_k(\boldsymbol{\ell}_k) \) then appear in the order \( G_1, G_2, \dots \), which is exactly the order in which, by @lem-elimination-matrices (c), the multipliers drop into place.
:::

::: {.proof}
Let \( A^{(0)}, \dots, A^{(n-1)} = U \) be the matrices produced by the algorithm. For each \( k \), let \( \boldsymbol{\ell}_k = \sum_{i > k} \ell_{ik} \e_i \in F^n \), a vector whose first \( k \) entries are zero.

**Step 1: \( U \) is upper triangular.** We show by induction on \( k \) that in \( A^{(k)} \) every entry below the diagonal in columns \( 1, \dots, k \) is zero. For \( k = 0 \) there is nothing to prove. Suppose it holds for \( A^{(k-1)} \). Step \( k \) changes only rows \( i > k \), replacing row \( i \) by row \( i \) minus a multiple of row \( k \). In columns \( j < k \), the entry of row \( k \) lies below the diagonal (\( k > j \)), so it is \( 0 \) by the induction hypothesis, and the entries of row \( i \) in these columns stay \( 0 \). In column \( k \), the new entries below the diagonal are \( 0 \), as noted after the algorithm. This completes the induction, and for \( k = n - 1 \) it says that \( U \) is upper triangular.

**Step 2: each step is a matrix.** Step \( k \) performs the operations "add \( -\ell_{ik} \) times row \( k \) to row \( i \)" for \( i = k+1, \dots, n \). By @thm-row-op-is-left-multiplication, applying them one after another multiplies \( A^{(k-1)} \) on the left by the corresponding elementary matrices \( I - \ell_{ik}E_{ik} \). By @lem-elimination-matrices (a), their product is \( G_k(-\boldsymbol{\ell}_k) \). Hence \( A^{(k)} = G_k(-\boldsymbol{\ell}_k) A^{(k-1)} \), and therefore
\[
U = G_{n-1}(-\boldsymbol{\ell}_{n-1}) \cdots G_2(-\boldsymbol{\ell}_2)\, G_1(-\boldsymbol{\ell}_1)\, A .
\]

**Step 3: undo the steps.** Multiply both sides on the left by \( G_{n-1}(\boldsymbol{\ell}_{n-1}) \), then by \( G_{n-2}(\boldsymbol{\ell}_{n-2}) \), and so on down to \( G_1(\boldsymbol{\ell}_1) \). By @lem-elimination-matrices (b), each one cancels the factor next to it, and we get
\[
G_1(\boldsymbol{\ell}_1)\, G_2(\boldsymbol{\ell}_2) \cdots G_{n-1}(\boldsymbol{\ell}_{n-1})\, U = A .
\]
By @lem-elimination-matrices (c), the product on the left of \( U \) is \( I + \sum_{k=1}^{n-1} \boldsymbol{\ell}_k \e_k\tp \). Its \( (i, k) \)-entry for \( i > k \) is \( \ell_{ik} \); its diagonal entries are \( 1 \); its entries above the diagonal are \( 0 \). That is, it is \( L \). Hence \( A = LU \) with \( L \) unit lower triangular and \( U \) upper triangular, as claimed.
:::

So the multipliers are not something to be remembered separately: they **are** the lower triangular factor. When a computer performs elimination it stores each \( \ell_{ik} \) in the slot \( (i, k) \) that it has just cleared, and at the end the one array holds \( L \) below the diagonal and \( U \) on and above it.

::: {.warning}
**The matrix that performs elimination, \( L^{-1} \), is not \( L \) with its multipliers negated.** In @exm-lu-by-elimination the operations multiply \( A \) on the left by
\[
G_2(-\boldsymbol{\ell}_2)\, G_1(-\boldsymbol{\ell}_1) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & -3 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ 7 & -3 & 1 \end{pmatrix},
\]
and the entry \( 7 = 1 + (-3)(-2) \) mixes two multipliers. This matrix is \( L^{-1} \), by Step 3 of the proof. It is \( L \), whose factors come in the order \( G_1, G_2 \), that has the multipliers cleanly in place.
:::

::: {.check}
Find the LU factorization of \( A = \begin{pmatrix} 2 & 4 \\ 6 & 5 \end{pmatrix} \) over \( \nQ \) by elimination, and check it by multiplying.

::: {.solution}
The pivot is \( 2 \) and the multiplier is \( \ell_{21} = 6/2 = 3 \). Subtracting \( 3 \) times row 1 from row 2 gives \( U = \begin{pmatrix} 2 & 4 \\ 0 & 5 - 12 \end{pmatrix} = \begin{pmatrix} 2 & 4 \\ 0 & -7 \end{pmatrix} \), and \( L = \begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix} \). Check: \( LU = \begin{pmatrix} 2 & 4 \\ 6 & 12 - 7 \end{pmatrix} = A \).
:::
:::

## Solving with an LU factorization

Once \( A = LU \) is known, each system \( A\x = \b \) costs two substitutions.

::: {#exm-lu-solve}
[Two right-hand sides, one factorization]

Let \( A = \begin{pmatrix} 2 & 1 & -1 \\ 4 & 5 & -1 \\ -2 & 8 & 2 \end{pmatrix} \) with the factorization \( A = LU \) of @exm-lu-by-elimination. Solve \( A\x = \b \) for
\[
\b = \begin{pmatrix} -1 \\ -3 \\ -6 \end{pmatrix} \quad\text{and}\quad \b' = \begin{pmatrix} 3 \\ 7 \\ -2 \end{pmatrix}.
\]
:::

::: {.solution}
*First right-hand side.* Forward substitution in \( L\y = \b \):
\[
y_1 = -1, \qquad 2y_1 + y_2 = -3 \Rightarrow y_2 = -1, \qquad -y_1 + 3y_2 + y_3 = -6 \Rightarrow y_3 = -6 - 1 + 3 = -4 .
\]
Back substitution in \( U\x = \y \):
\[
-2x_3 = -4 \Rightarrow x_3 = 2, \qquad 3x_2 + x_3 = -1 \Rightarrow x_2 = -1, \qquad 2x_1 + x_2 - x_3 = -1 \Rightarrow x_1 = 1 .
\]
So \( \x = (1, -1, 2) \). Check: \( A\x = (2 - 1 - 2, \; 4 - 5 - 2, \; -2 - 8 + 4) = (-1, -3, -6) = \b \).

*Second right-hand side.* \( L\y = \b' \): \( y_1 = 3 \), \( y_2 = 7 - 2 \cdot 3 = 1 \), \( y_3 = -2 + y_1 - 3y_2 = -2 + 3 - 3 = -2 \). Then \( U\x = \y \): \( -2x_3 = -2 \), so \( x_3 = 1 \); \( 3x_2 + 1 = 1 \), so \( x_2 = 0 \); \( 2x_1 + 0 - 1 = 3 \), so \( x_1 = 2 \). So \( \x' = (2, 0, 1) \), and indeed \( A\x' = (4 + 0 - 1, \; 8 + 0 - 1, \; -4 + 0 + 2) = (3, 7, -2) \).

Since the diagonal of \( U \) is \( 2, 3, -2 \), all non-zero, \( U \) is invertible by @lem-triangular-invertible, \( L \) is invertible by @lem-unit-lower-triangular-closed, and so \( A = LU \) is invertible. Each solution found is therefore the only one.
:::

How much is saved? Count the arithmetic operations (\( +, -, \times, \div \)) for an \( n \times n \) matrix. At step \( k \) of elimination there are \( n - k \) rows below the pivot. Each needs one division for its multiplier, then \( n - k \) multiplications and \( n - k \) subtractions in the columns to the right of column \( k \). With \( j = n - k \), the total is
\[
\sum_{j=1}^{n-1} j(2j + 1) = \frac{n(n-1)(4n+1)}{6} \approx \frac{2}{3} n^3 .
\]
Forward substitution with a unit lower triangular \( L \) uses \( n(n-1) \) operations, and back substitution \( n^2 \), so a pair of triangular solves costs \( 2n^2 - n \). For \( n = 1000 \) that is about \( 6.7 \times 10^8 \) operations for the factorization, done once, against about \( 2 \times 10^6 \) for each new right-hand side.

## Uniqueness

The factorization of @exm-lu-by-elimination came from one particular procedure. Could another procedure give a different pair \( (L, U) \)? For invertible matrices, no.

::: {#thm-lu-unique}
[Uniqueness of the LU factorization]

Let \( A \in M_n(F) \) be **invertible**. If \( A = L_1U_1 \) and \( A = L_2U_2 \) are LU factorizations, then \( L_1 = L_2 \) and \( U_1 = U_2 \).
:::

::: {.idea}
Take the difference in multiplicative form: from \( L_1U_1 = L_2U_2 \) we get \( (L_2^{-1}L_1)U_1 = U_2 \). The matrix \( M = L_2^{-1}L_1 \) is unit lower triangular, and multiplying \( U_1 \) by it must leave an upper triangular matrix. Clearing below the diagonal column by column, the non-zero pivots of \( U_1 \) force \( M \) to have nothing below its diagonal. Invertibility of \( A \) is what provides those non-zero pivots.
:::

::: {.proof}
By @lem-unit-lower-triangular-closed (b), \( L_1 \) and \( L_2 \) are invertible. Hence \( U_1 = L_1^{-1}A \) is a product of invertible matrices, so it is invertible by @thm-inverse-matrix-properties, and by @lem-triangular-invertible its diagonal entries \( u_{11}, \dots, u_{nn} \) are all non-zero.

Let \( M = L_2^{-1}L_1 \). By @lem-unit-lower-triangular-closed, \( M = (m_{ij}) \) is unit lower triangular. Multiplying \( L_1U_1 = L_2U_2 \) on the left by \( L_2^{-1} \) gives \( MU_1 = U_2 \), so \( MU_1 \) is upper triangular. We show \( m_{ij} = 0 \) for all \( i > j \), by induction on the column \( j \).

Fix \( j \), and suppose \( m_{ik} = 0 \) whenever \( k < j \) and \( i > k \). Let \( i > j \). Since \( MU_1 \) is upper triangular and \( i > j \),
\[
0 = (MU_1)_{ij} = \sum_{k=1}^{n} m_{ik} u_{kj} = \sum_{k \le j} m_{ik} u_{kj} = m_{ij} u_{jj},
\]
where the third equality uses \( u_{kj} = 0 \) for \( k > j \), and the last uses \( m_{ik} = 0 \) for \( k < j \) (here \( i > j > k \)). Since \( u_{jj} \neq 0 \), we get \( m_{ij} = 0 \). This completes the induction, so \( M \) is lower triangular with \( 1 \)'s on the diagonal and nothing below it: \( M = I \).

Hence \( L_2^{-1}L_1 = I \), and multiplying by \( L_2 \) gives \( L_1 = L_2 \). Then \( U_1 = L_1^{-1}A = L_2^{-1}A = U_2 \). This proves the theorem.
:::

Two consequences are worth saying. The LU factorization of an invertible matrix does not depend on how it was found, so it is legitimate to speak of **the** factors \( L \) and \( U \). And if elimination without row swaps succeeds on an invertible \( A \), then every pivot is non-zero: row \( k \) is not changed after step \( k \), so the pivot of step \( k \) is \( u_{kk} \), which is non-zero by the first paragraph of the proof. So the second case of the algorithm (a zero pivot over a zero column) never occurs.

::: {.remark}
The hypothesis "invertible" cannot be dropped. For every \( c \in F \),
\[
\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ c & 1 \end{pmatrix} \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix},
\]
since the first column of the right factor is zero. Taking \( c = 0 \) and \( c = 1 \) gives two different LU factorizations. The proof breaks exactly at "\( u_{jj} \neq 0 \)", here for \( j = 1 \).
:::

## Row swaps and the PLU factorization

@exm-no-lu-factorization showed that some matrices, even invertible ones, have no LU factorization, because elimination meets a zero pivot with a non-zero entry below it. The cure in Gaussian elimination is to swap rows. We now show that the swaps can all be collected in front, as a single matrix that rearranges the rows of \( A \) **before** elimination starts. After that rearrangement, no swaps are needed.

Matrices that rearrange rows have a name.

::: {#def-permutation-matrix}
[Permutation matrix]

Let \( \sigma \in S_n \) be a permutation of \( \{1, \dots, n\} \). The **permutation matrix** of \( \sigma \) is
\[
P_\sigma = \begin{pmatrix} \e_{\sigma(1)} & \e_{\sigma(2)} & \cdots & \e_{\sigma(n)} \end{pmatrix} \in M_n(F),
\]
the matrix whose \( j \)-th column is \( \e_{\sigma(j)} \). A matrix is a **permutation matrix** if it equals \( P_\sigma \) for some \( \sigma \in S_n \).
:::

Equivalently, a permutation matrix has exactly one \( 1 \) in each row and in each column, and zeros elsewhere. The identity is \( P_{\id} \). The matrix \( \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) of @exm-no-lu-factorization is \( P_\tau \) for the transposition \( \tau = (1\ 2) \). By contrast \( \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) is **not** a permutation matrix: each column is still non-zero, but its first row contains two \( 1 \)'s, and its second column \( (1, 1) \) is not a standard basis vector.

::: {#lem-permutation-matrices}
[Permutation matrices]

Let \( \sigma, \tau \in S_n \).

::: {.enumerate options="label=(\alph*)"}
1. \( P_\sigma P_\tau = P_{\sigma \circ \tau} \). In particular a product of permutation matrices is a permutation matrix.
2. \( P_\sigma \) is invertible and \( P_\sigma^{-1} = P_\sigma\tp \).
3. If \( \tau = (r\ s) \) is a transposition, then \( P_\tau \) is the elementary matrix \( P_{rs} \) that swaps rows \( r \) and \( s \), and \( P_\tau^2 = I \).
4. Let \( 1 \le k < r < s \le n \), let \( \tau = (r\ s) \), and let \( \v \in F^n \) have its first \( k \) entries zero. Then \( P_\tau \v \) has its first \( k \) entries zero, and
\[
P_\tau\, G_k(\v)\, P_\tau = G_k(P_\tau \v).
\]
:::
:::

::: {.proof}
(a) By @thm-matrix-times-vector-columns, \( P_\tau \e_j = \e_{\tau(j)} \) and so \( P_\sigma P_\tau \e_j = P_\sigma \e_{\tau(j)} = \e_{\sigma(\tau(j))} \). So the \( j \)-th column of \( P_\sigma P_\tau \) is \( \e_{(\sigma \circ \tau)(j)} \), for every \( j \), which is the claim.

(b) By @thm-three-views-of-product, \( (P_\sigma\tp P_\sigma)_{ij} = \e_{\sigma(i)}\tp \e_{\sigma(j)} \), which is \( 1 \) if \( \sigma(i) = \sigma(j) \) and \( 0 \) otherwise. Since \( \sigma \) is injective, \( \sigma(i) = \sigma(j) \) exactly when \( i = j \). Hence \( P_\sigma\tp P_\sigma = I \), and by @thm-one-sided-inverse, \( P_\sigma \) is invertible with inverse \( P_\sigma\tp \).

(c) Swapping rows \( r \) and \( s \) of \( I \) produces a matrix whose column \( r \) is \( \e_s \), whose column \( s \) is \( \e_r \), and whose other columns \( j \) are \( \e_j \). These are the columns \( \e_{\tau(j)} \), so the swap matrix is \( P_\tau \). Since \( \tau \circ \tau = \id \), part (a) gives \( P_\tau^2 = P_{\id} = I \).

(d) Write \( P = P_\tau \). Its effect on a vector is to exchange entries \( r \) and \( s \), which are both beyond position \( k \), so \( P\v \) still has its first \( k \) entries zero. Since \( k \neq r, s \), we have \( P\e_k = \e_{\tau(k)} = \e_k \). By (b) and (c), \( P\tp = P^{-1} = P \), so \( \e_k\tp P = \e_k\tp P\tp = (P\e_k)\tp = \e_k\tp \) by @thm-transpose-properties. Therefore
\[
P(I + \v\,\e_k\tp)P = P^2 + (P\v)(\e_k\tp P) = I + (P\v)\,\e_k\tp = G_k(P\v),
\]
using \( P^2 = I \) from (c). This proves the lemma.
:::

By (c) and @thm-row-op-is-left-multiplication, \( P_\tau A \) is \( A \) with rows \( r \) and \( s \) swapped, and by (a) every permutation matrix is a product of such swaps applied in turn, since for \( n \ge 2 \) every permutation is a product of transpositions (@thm-transpositions-generate). So \( PA \) is always \( A \) with its rows rearranged.

::: {#def-plu-factorization}
[PLU factorization]

Let \( A \in M_n(F) \). A **PLU factorization** of \( A \) is a triple \( (P, L, U) \) of matrices in \( M_n(F) \) such that
\[
PA = LU, \qquad P \text{ is a permutation matrix}, \qquad L \text{ is unit lower triangular}, \qquad U \text{ is upper triangular}.
\]
:::

In words: after rearranging the rows of \( A \) by \( P \), the matrix has an LU factorization. By @lem-permutation-matrices (b) this can also be written \( A = P\tp LU \), which is why some books write the factorization as \( A = PLU \) with their \( P \) our \( P\tp \). For example, \( A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) has the PLU factorization \( (A, I, I) \), since \( AA = I = I \cdot I \). An LU factorization is the special case \( P = I \).

To produce \( P \), run elimination and allow a swap whenever a zero pivot has a non-zero entry below it.

::: {.algorithm}
**Elimination with row swaps.** Input: \( A \in M_n(F) \). Put \( A^{(0)} = A \). For \( k = 1, 2, \dots, n - 1 \), with \( A^{(k-1)} = (a_{ij}) \):

- If \( a_{ik} = 0 \) for **every** \( i \ge k \), set \( P_k = I \) and all \( \ell_{ik} = 0 \), and let \( A^{(k)} = A^{(k-1)} \).
- Otherwise choose some \( r_k \ge k \) with \( a_{r_k k} \neq 0 \). Let \( P_k \) be the matrix swapping rows \( k \) and \( r_k \) (so \( P_k = I \) if \( r_k = k \)), and let \( B = P_k A^{(k-1)} \). Set \( \ell_{ik} = b_{ik}/b_{kk} \) for \( i > k \), and obtain \( A^{(k)} \) from \( B \) by replacing row \( i \) with (row \( i \)) \( - \ell_{ik} \cdot \) (row \( k \)) for each \( i > k \).
:::

This version never stops. Here is the result it delivers.

::: {#thm-plu-exists}
[Existence of a PLU factorization]

**Every** \( A \in M_n(F) \) has a PLU factorization.
:::

::: {.idea}
**Step roadmap.** ① As before, each step is a matrix: \( A^{(k)} = G_k(-\boldsymbol{\ell}_k) P_k A^{(k-1)} \), and the final matrix \( U \) is upper triangular. ② The swaps are tangled with the multiplier matrices. A swap of two rows below row \( k \) can be pushed to the right past \( G_k \) at the price of swapping the entries of the multiplier vector: this is @lem-permutation-matrices (d). ③ Once all swaps sit next to \( A \), the rest is the LU proof word for word. In practice, ② says: when you swap two rows, also swap the multipliers already stored in those rows.
:::

::: {.proof}
Run elimination with row swaps on \( A \), producing \( A^{(0)}, \dots, A^{(n-1)} = U \), swap matrices \( P_1, \dots, P_{n-1} \) and multipliers \( \ell_{ik} \). Let \( \boldsymbol{\ell}_k = \sum_{i > k} \ell_{ik} \e_i \), whose first \( k \) entries are zero.

**Step 1.** Exactly as in Step 1 of the proof of @thm-lu-exists-without-swaps, every entry of \( A^{(k)} \) below the diagonal in columns \( 1, \dots, k \) is zero. The only new point is the swap in step \( k \): it exchanges rows \( k \) and \( r_k \ge k \), whose entries in columns \( j < k \) are below the diagonal and hence zero, so the swap does not disturb these columns. After the swap the pivot \( b_{kk} \) is non-zero, and the new entries below it are \( b_{ik} - \ell_{ik}b_{kk} = 0 \). Hence \( U \) is upper triangular. By @lem-permutation-matrices (c), @thm-row-op-is-left-multiplication and @lem-elimination-matrices (a), as in Step 2 of that proof,
\[
A^{(k)} = G_k(-\boldsymbol{\ell}_k)\, P_k\, A^{(k-1)} \qquad (k = 1, \dots, n-1).
\]
This also holds in the first case of the algorithm, where \( P_k = I \) and \( G_k(\0) = I \).

**Step 2.** For \( 1 \le k \le m \le n-1 \) put \( \boldsymbol{\ell}_k^{(m)} = P_m P_{m-1} \cdots P_{k+1} \boldsymbol{\ell}_k \), with \( \boldsymbol{\ell}_m^{(m)} = \boldsymbol{\ell}_m \). We claim that the first \( k \) entries of \( \boldsymbol{\ell}_k^{(m)} \) are zero and that
\[
G_m(-\boldsymbol{\ell}_m) P_m \cdots G_1(-\boldsymbol{\ell}_1) P_1 = G_m(-\boldsymbol{\ell}_m^{(m)}) \cdots G_1(-\boldsymbol{\ell}_1^{(m)})\; P_m \cdots P_1 .
\]
For \( m = 1 \) both sides are \( G_1(-\boldsymbol{\ell}_1) P_1 \). Suppose the claim holds for \( m \), and multiply it on the left by \( G_{m+1}(-\boldsymbol{\ell}_{m+1}) P_{m+1} \). The matrix \( P_{m+1} \) is \( I \) or swaps rows \( m+1 \) and \( r_{m+1} > m + 1 \), both beyond every \( k \le m \). So by @lem-permutation-matrices (c) and (d), for each \( k \le m \) and each vector \( \v \) with its first \( k \) entries zero,
\[
P_{m+1}\, G_k(\v) = P_{m+1}\, G_k(\v)\, P_{m+1} P_{m+1} = G_k(P_{m+1}\v)\, P_{m+1},
\]
and \( P_{m+1}\v \) again has its first \( k \) entries zero. Applying this for \( k = m, m-1, \dots, 1 \) moves \( P_{m+1} \) to the right past every factor \( G_k \), replacing \( \boldsymbol{\ell}_k^{(m)} \) by \( P_{m+1}\boldsymbol{\ell}_k^{(m)} = \boldsymbol{\ell}_k^{(m+1)} \) (note \( P_{m+1}(-\v) = -P_{m+1}\v \)). This is the claim for \( m + 1 \).

**Step 3.** By Step 1, \( U = G_{n-1}(-\boldsymbol{\ell}_{n-1}) P_{n-1} \cdots G_1(-\boldsymbol{\ell}_1) P_1 A \). Write \( \boldsymbol{\ell}'_k = \boldsymbol{\ell}_k^{(n-1)} \) and \( P = P_{n-1} \cdots P_1 \). By Step 2,
\[
U = G_{n-1}(-\boldsymbol{\ell}'_{n-1}) \cdots G_1(-\boldsymbol{\ell}'_1)\, PA .
\]
\( P \) is a permutation matrix by @lem-permutation-matrices (a) and (c). Multiplying on the left by \( G_{n-1}(\boldsymbol{\ell}'_{n-1}) \), then \( G_{n-2}(\boldsymbol{\ell}'_{n-2}) \), and so on, and using @lem-elimination-matrices (b) and (c) as in Step 3 of the proof of @thm-lu-exists-without-swaps,
\[
PA = LU, \qquad L = I + \sum_{k=1}^{n-1} \boldsymbol{\ell}'_k \e_k\tp ,
\]
where \( L \) is unit lower triangular because the first \( k \) entries of each \( \boldsymbol{\ell}'_k \) are zero. So \( (P, L, U) \) is a PLU factorization of \( A \). This proves the theorem.
:::

::: {#exm-plu}
[A swap in the middle]

Find a PLU factorization of
\[
A = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 4 & 3 \\ 3 & 7 & 2 \end{pmatrix} \in M_3(\nQ).
\]
:::

::: {.solution}
*Step 1.* The pivot \( 1 \) is non-zero, so no swap. The multipliers are \( \ell_{21} = 2 \) and \( \ell_{31} = 3 \):
\[
A \xrightarrow[R_3 \to R_3 - 3R_1]{R_2 \to R_2 - 2R_1} \begin{pmatrix} 1 & 2 & 1 \\ 0 & 0 & 1 \\ 0 & 1 & -1 \end{pmatrix}, \qquad \boldsymbol{\ell}_1 = \begin{pmatrix} 0 \\ 2 \\ 3 \end{pmatrix}.
\]
*Step 2.* The pivot position \( (2, 2) \) holds \( 0 \), but the entry below it is \( 1 \). Elimination without row swaps would stop here. We swap rows 2 and 3, so \( P_2 = P_{23} \):
\[
\xrightarrow{R_2 \leftrightarrow R_3} \begin{pmatrix} 1 & 2 & 1 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{pmatrix} = U .
\]
The entry below the new pivot is already \( 0 \), so \( \ell_{32} = 0 \), and \( U \) is upper triangular.

By Step 2 of the proof, the stored multipliers of step 1 are swapped too: \( \boldsymbol{\ell}'_1 = P_2 \boldsymbol{\ell}_1 = (0, 3, 2) \). Hence
\[
P = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}, \qquad
L = \begin{pmatrix} 1 & 0 & 0 \\ 3 & 1 & 0 \\ 2 & 0 & 1 \end{pmatrix}.
\]
Check: \( PA \) is \( A \) with rows 2 and 3 swapped, and
\[
LU = \begin{pmatrix} 1 & 2 & 1 \\ 3 & 6 + 1 & 3 - 1 \\ 2 & 4 & 2 + 1 \end{pmatrix} = \begin{pmatrix} 1 & 2 & 1 \\ 3 & 7 & 2 \\ 2 & 4 & 3 \end{pmatrix} = PA .
\]
Notice where the multipliers ended up: \( 3 \) in row 2 and \( 2 \) in row 3, traveling with the rows they belong to. To solve \( A\x = \b \), multiply by \( P \) and solve \( LU\x = P\b \) by two substitutions; since \( P \) is invertible, this changes no solutions. For \( \b = (2, 3, 8) \), \( P\b = (2, 8, 3) \). Forward substitution in \( L\y = P\b \) gives \( y_1 = 2 \), \( y_2 = 8 - 3 \cdot 2 = 2 \), \( y_3 = 3 - 2 \cdot 2 = -1 \). Back substitution in \( U\x = \y \) gives \( x_3 = -1 \), \( x_2 = 2 + x_3 = 1 \), \( x_1 = 2 - 2x_2 - x_3 = 1 \). Check: \( A(1, 1, -1) = (1 + 2 - 1, \; 2 + 4 - 3, \; 3 + 7 - 2) = (2, 3, 8) \).
:::

::: {.remark}
Over \( \nR \), computers do not choose just any non-zero pivot. They choose the entry of **largest absolute value** in the column, which is called **partial pivoting**. The reason is rounding. For \( A = \begin{pmatrix} \varepsilon & 1 \\ 1 & 1 \end{pmatrix} \) with \( \varepsilon = 10^{-20} \), elimination without swaps gives the multiplier \( 10^{20} \) and \( u_{22} = 1 - 10^{20} \), which in standard double-precision arithmetic is stored as \( -10^{20} \). Multiplying back, the computed \( LU \) has \( (2, 2) \)-entry \( 10^{20} - 10^{20} = 0 \) instead of \( 1 \). Swapping the rows first gives the harmless multiplier \( \varepsilon \). Chapter 23 makes this precise.
:::

## Symmetric matrices: the LDLᵀ factorization

When \( A \) is symmetric, the two factors of \( A = LU \) are secretly related: up to a diagonal matrix, \( U \) is the transpose of \( L \). In @exm-lu-by-elimination the factors look unrelated, but that matrix is not symmetric. Try a symmetric one:
\[
\begin{pmatrix} 1 & 3 & -2 \\ 3 & 7 & -8 \\ -2 & -8 & 5 \end{pmatrix} \xrightarrow[R_3 \to R_3 + 2R_1]{R_2 \to R_2 - 3R_1} \begin{pmatrix} 1 & 3 & -2 \\ 0 & -2 & -2 \\ 0 & -2 & 1 \end{pmatrix} \xrightarrow{R_3 \to R_3 - R_2} \begin{pmatrix} 1 & 3 & -2 \\ 0 & -2 & -2 \\ 0 & 0 & 3 \end{pmatrix} = U ,
\]
with multipliers \( \ell_{21} = 3 \), \( \ell_{31} = -2 \), \( \ell_{32} = 1 \). Divide each row of \( U \) by its diagonal entry: the rows become \( (1, 3, -2) \), \( (0, 1, 1) \), \( (0, 0, 1) \). These are the columns of \( L = \begin{pmatrix} 1 & 0 & 0 \\ 3 & 1 & 0 \\ -2 & 1 & 1 \end{pmatrix} \), read as rows. So \( U = DL\tp \) with \( D = \diag(1, -2, 3) \), and \( A = LDL\tp \).

::: {#thm-ldlt}
[LDLᵀ factorization]

Let \( A \in M_n(F) \) be **symmetric** and **invertible**, and suppose \( A = LU \) is an LU factorization. Then the diagonal entries \( u_{11}, \dots, u_{nn} \) of \( U \) are non-zero, and with \( D = \diag(u_{11}, \dots, u_{nn}) \),
\[
U = DL\tp \qquad\text{and}\qquad A = LDL\tp .
\]
:::

::: {.idea}
Pull the diagonal out of \( U \), writing \( U = DV \) with \( V \) unit upper triangular, so \( A = LDV \). Transposing, \( A = A\tp = V\tp (DL\tp) \), which is a second LU factorization of the same invertible matrix. Uniqueness forces the two to agree, so \( L = V\tp \).
:::

::: {.proof}
As in the proof of @thm-lu-unique, \( U = L^{-1}A \) is invertible, so its diagonal entries are non-zero by @lem-triangular-invertible. Hence \( D \) is invertible, with \( D^{-1} = \diag(u_{11}^{-1}, \dots, u_{nn}^{-1}) \). Let \( V = D^{-1}U \). Row \( i \) of \( V \) is \( u_{ii}^{-1} \) times row \( i \) of \( U \), so \( V \) is upper triangular with \( v_{ii} = u_{ii}^{-1}u_{ii} = 1 \), and \( A = LDV \).

Since \( A \) is symmetric and \( D\tp = D \), @thm-transpose-properties gives
\[
A = A\tp = (LDV)\tp = V\tp D L\tp = V\tp (DL\tp).
\]
Here \( V\tp \) is unit lower triangular, because \( V \) is unit upper triangular. And \( DL\tp \) is upper triangular: its \( (i, j) \)-entry is \( u_{ii} \ell_{ji} \), and \( \ell_{ji} = 0 \) when \( j < i \), since \( L \) is lower triangular. So \( (V\tp, DL\tp) \) is an LU factorization of the invertible matrix \( A \). By @thm-lu-unique, \( V\tp = L \) and \( DL\tp = U \). Therefore \( A = LU = LDL\tp \), as claimed.
:::

The factorization stores about half as much: \( L \) and the diagonal \( D \) determine everything. Over \( \nR \), when every entry of \( D \) is positive, one can split \( D = D^{1/2}D^{1/2} \) and write \( A = (LD^{1/2})(LD^{1/2})\tp \); this is the **Cholesky factorization**, which Chapter 12 connects with positive definite matrices.

::: {.remark}
Symmetry alone does not give an LU factorization: \( \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) is symmetric and invertible, and has none by @exm-no-lu-factorization. The theorem assumes the factorization exists and then improves it.
:::

## Exercises

### A. Check your understanding

::: {#exr-lu-factorization-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define an LU factorization of a matrix \( A \in M_n(F) \), and a PLU factorization.
2. True or false: every invertible matrix has an LU factorization. Justify your answer.
3. Suppose \( A = LU \). In which order are the two triangular systems solved to find a solution of \( A\x = \b \), and what is each one?
4. True or false: the product of two unit lower triangular \( n \times n \) matrices is unit lower triangular. Justify your answer.
5. True or false: the zero matrix in \( M_2(F) \) has more than one LU factorization. Justify your answer.
6. What is the inverse of a permutation matrix \( P \)?
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. See @def-lu-factorization: \( A = LU \) with \( L \) unit lower triangular and \( U \) upper triangular. See @def-plu-factorization: \( PA = LU \) with \( P \) a permutation matrix, \( L \) unit lower triangular and \( U \) upper triangular.
2. False. \( \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) is invertible but has no LU factorization, by @exm-no-lu-factorization.
3. First \( L\y = \b \), by forward substitution; then \( U\x = \y \), by back substitution. Then \( A\x = L(U\x) = L\y = \b \).
4. True, by @lem-unit-lower-triangular-closed (a).
5. True. For every \( c \in F \), \( \begin{pmatrix} 1 & 0 \\ c & 1 \end{pmatrix} 0 = 0 \), so \( \left(\begin{pmatrix} 1 & 0 \\ c & 1 \end{pmatrix}, 0\right) \) is an LU factorization; \( c = 0 \) and \( c = 1 \) give two different ones. This does not contradict @thm-lu-unique, because \( 0 \) is not invertible.
6. \( P^{-1} = P\tp \), by @lem-permutation-matrices (b).
:::
:::

### B. Practice

::: {#exr-lu-factorization-b1}
[B1: An LU factorization]

Find the LU factorization of
\[
A = \begin{pmatrix} 1 & 2 & 0 \\ -3 & -7 & 4 \\ 2 & 6 & -3 \end{pmatrix} \in M_3(\nQ)
\]
by elimination without row swaps. Hence show that \( A \) is invertible.
:::

::: {.solution}
*Step 1.* The pivot is \( 1 \), with multipliers \( \ell_{21} = -3 \) and \( \ell_{31} = 2 \):
\[
A \xrightarrow[R_3 \to R_3 - 2R_1]{R_2 \to R_2 - (-3)R_1} \begin{pmatrix} 1 & 2 & 0 \\ 0 & -1 & 4 \\ 0 & 2 & -3 \end{pmatrix}.
\]
*Step 2.* The pivot is \( -1 \), with multiplier \( \ell_{32} = 2/(-1) = -2 \):
\[
\xrightarrow{R_3 \to R_3 - (-2)R_2} \begin{pmatrix} 1 & 2 & 0 \\ 0 & -1 & 4 \\ 0 & 0 & 5 \end{pmatrix} = U .
\]
By @thm-lu-exists-without-swaps,
\[
L = \begin{pmatrix} 1 & 0 & 0 \\ -3 & 1 & 0 \\ 2 & -2 & 1 \end{pmatrix}, \qquad A = LU .
\]
Check: \( LU = \begin{pmatrix} 1 & 2 & 0 \\ -3 & -6 - 1 & 4 \\ 2 & 4 + 2 & -8 + 5 \end{pmatrix} = A \).

The diagonal entries \( 1, -1, 5 \) of \( U \) are non-zero, so \( U \) is invertible by @lem-triangular-invertible, and \( L \) is invertible by @lem-unit-lower-triangular-closed. Hence \( A = LU \) is invertible by @thm-inverse-matrix-properties.
:::

::: {#exr-lu-factorization-b2}
[B2: Two systems, one factorization]

With \( A = LU \) as in @exr-lu-factorization-b1, solve \( A\x = \b \) for \( \b = (3, -6, 5) \) and for \( \b = (0, 1, -2) \), using only forward and back substitution.
:::

::: {.solution}
*For \( \b = (3, -6, 5) \).* \( L\y = \b \): \( y_1 = 3 \); \( -3y_1 + y_2 = -6 \), so \( y_2 = 3 \); \( 2y_1 - 2y_2 + y_3 = 5 \), so \( y_3 = 5 - 6 + 6 = 5 \). Then \( U\x = \y \): \( 5x_3 = 5 \), so \( x_3 = 1 \); \( -x_2 + 4x_3 = 3 \), so \( x_2 = 1 \); \( x_1 + 2x_2 = 3 \), so \( x_1 = 1 \). Hence \( \x = (1, 1, 1) \). Check: \( A\x = (1 + 2, \; -3 - 7 + 4, \; 2 + 6 - 3) = (3, -6, 5) \).

*For \( \b = (0, 1, -2) \).* \( L\y = \b \): \( y_1 = 0 \); \( y_2 = 1 + 3y_1 = 1 \); \( y_3 = -2 - 2y_1 + 2y_2 = 0 \). Then \( U\x = \y \): \( 5x_3 = 0 \), so \( x_3 = 0 \); \( -x_2 + 0 = 1 \), so \( x_2 = -1 \); \( x_1 + 2(-1) = 0 \), so \( x_1 = 2 \). Hence \( \x = (2, -1, 0) \). Check: \( A\x = (2 - 2, \; -6 + 7, \; 4 - 6) = (0, 1, -2) \).

Since \( A \) is invertible (@exr-lu-factorization-b1), each solution is the only one, by @thm-inverse-matrix-properties.
:::

::: {#exr-lu-factorization-b3}
[B3: A PLU factorization]

Let \( A = \begin{pmatrix} 0 & 1 & 2 \\ 1 & 1 & 1 \\ 2 & 3 & 1 \end{pmatrix} \in M_3(\nQ) \).

::: {.enumerate options="label=(\alph*)"}
1. Explain why \( A \) has no LU factorization.
2. Find a PLU factorization of \( A \).
3. Hence solve \( A\x = (0, 2, 7) \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. If \( A = LU \), then the \( (1, 1) \)-entry gives \( u_{11} = a_{11} = 0 \), and the \( (2, 1) \)-entry gives \( a_{21} = \ell_{21}u_{11} = 0 \). But \( a_{21} = 1 \neq 0 \), a contradiction, exactly as in @exm-no-lu-factorization.
2. The first pivot position holds \( 0 \) and the entry below is \( 1 \), so swap rows 1 and 2, \( P_1 = P_{12} \):
\[
A \xrightarrow{R_1 \leftrightarrow R_2} \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 2 & 3 & 1 \end{pmatrix} \xrightarrow[R_3 \to R_3 - 2R_1]{R_2 \to R_2 - 0R_1} \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 0 & 1 & -1 \end{pmatrix} \xrightarrow{R_3 \to R_3 - 1R_2} \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & -3 \end{pmatrix} = U .
\]
The multipliers are \( \ell_{21} = 0 \), \( \ell_{31} = 2 \), \( \ell_{32} = 1 \), and no swap happens after step 1, so they need no rearranging. Hence
\[
P = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad L = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 2 & 1 & 1 \end{pmatrix}.
\]
Check: \( PA = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 2 & 3 & 1 \end{pmatrix} \), and \( LU = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 2 & 2 + 1 & 2 + 2 - 3 \end{pmatrix} = PA \).
3. \( A\x = \b \) holds if and only if \( PA\x = P\b \), since \( P \) is invertible (@lem-permutation-matrices (b)). Swapping the first two entries of \( \b = (0, 2, 7) \), we solve \( LU\x = P\b = (2, 0, 7) \). \( L\y = (2, 0, 7) \): \( y_1 = 2 \), \( y_2 = 0 \), \( y_3 = 7 - 2 \cdot 2 - 0 = 3 \). \( U\x = \y \): \( -3x_3 = 3 \), so \( x_3 = -1 \); \( x_2 + 2x_3 = 0 \), so \( x_2 = 2 \); \( x_1 + x_2 + x_3 = 2 \), so \( x_1 = 1 \). Hence \( \x = (1, 2, -1) \). Check: \( A\x = (0 + 2 - 2, \; 1 + 2 - 1, \; 2 + 6 - 1) = (0, 2, 7) \).
:::
:::

### C. Going deeper

::: {#exr-lu-factorization-c1}
[C1: Leading principal submatrices]

For \( A \in M_n(F) \) and \( 1 \le k \le n \), the **leading principal submatrix** \( A_k \in M_k(F) \) is the top-left \( k \times k \) corner of \( A \), with entries \( a_{ij} \) for \( i, j \le k \).

::: {.enumerate options="label=(\alph*)"}
1. Let \( L \) be lower triangular and \( U \) upper triangular in \( M_n(F) \). Show that \( (LU)_k = L_k U_k \) for every \( k \).
2. Deduce that if \( A \) has an LU factorization \( A = LU \) with \( U \) invertible, then every leading principal submatrix \( A_1, \dots, A_n \) is invertible.
3. Prove the converse: if \( A_1, \dots, A_n \) are all invertible, then \( A \) has an LU factorization with \( U \) invertible.
:::

*Hint for (c): induction on \( n \). Write \( A \) with \( A_{n-1} \) in its top-left corner, a column \( \b \), a row \( \c\tp \) and a corner entry \( d \), and look for \( L \) and \( U \) of the same shape.*
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Let \( i, j \le k \). By @def-matrix-multiplication, \( (LU)_{ij} = \sum_{l=1}^{n} \ell_{il} u_{lj} \). If \( l > k \), then \( l > i \), so \( \ell_{il} = 0 \) because \( L \) is lower triangular. Hence \( (LU)_{ij} = \sum_{l=1}^{k} \ell_{il}u_{lj} = (L_kU_k)_{ij} \), as claimed.
2. Suppose \( A = LU \) with \( U \) invertible. By (a), \( A_k = L_kU_k \). The matrix \( L_k \) is unit lower triangular, so it is invertible by @lem-unit-lower-triangular-closed. By @lem-triangular-invertible, \( u_{11}, \dots, u_{nn} \) are non-zero; \( U_k \) is upper triangular with diagonal \( u_{11}, \dots, u_{kk} \), so \( U_k \) is invertible by the same lemma. Hence \( A_k \) is invertible by @thm-inverse-matrix-properties.
3. We prove by induction on \( n \) that every \( A \in M_n(F) \) whose leading principal submatrices are all invertible has an LU factorization with \( U \) invertible. For \( n = 1 \), \( A = (a_{11}) \) with \( a_{11} \neq 0 \), and \( A = (1)(a_{11}) \) works.

   Let \( n \ge 2 \) and suppose the statement holds for \( n - 1 \). Write
   \[
   A = \begin{pmatrix} A_{n-1} & \b \\ \c\tp & d \end{pmatrix}, \qquad \b, \c \in F^{n-1},\ d \in F .
   \]
   The leading principal submatrices of \( A_{n-1} \) are \( A_1, \dots, A_{n-1} \), all invertible, so by the induction hypothesis \( A_{n-1} = L'U' \) with \( L' \) unit lower triangular and \( U' \) upper triangular and invertible. Put \( \y = L'^{-1}\b \), \( \x\tp = \c\tp U'^{-1} \) and \( z = d - \x\tp\y \), and let
   \[
   L = \begin{pmatrix} L' & \0 \\ \x\tp & 1 \end{pmatrix}, \qquad U = \begin{pmatrix} U' & \y \\ \0\tp & z \end{pmatrix}.
   \]
   Then \( L \) is unit lower triangular and \( U \) is upper triangular. Computing \( LU \) entry by entry, splitting each sum \( \sum_{l=1}^{n} \) into \( l \le n - 1 \) and \( l = n \): the top-left block is \( L'U' + \0\,\0\tp = A_{n-1} \); the top-right column is \( L'\y + \0 z = \b \); the bottom-left row is \( \x\tp U' + 1 \cdot \0\tp = \c\tp \); the corner is \( \x\tp\y + z = d \). Hence \( A = LU \).

   Finally \( A = A_n \) is invertible by hypothesis, and \( L \) is invertible by @lem-unit-lower-triangular-closed, so \( U = L^{-1}A \) is invertible by @thm-inverse-matrix-properties. This completes the induction.
:::

In the language of elimination: \( z \) is the \( n \)-th pivot, and (c) shows that invertible leading corners are exactly what keeps every pivot non-zero.
:::

::: {#exr-lu-factorization-c2}
[C2: An LDLᵀ factorization]

Let \( A = \begin{pmatrix} 4 & -4 & 8 \\ -4 & 5 & -11 \\ 8 & -11 & 27 \end{pmatrix} \in M_3(\nR) \).

::: {.enumerate options="label=(\alph*)"}
1. Find the LU factorization of \( A \), show that \( A \) is invertible, and write \( A = LDL\tp \).
2. Deduce that \( \x\tp A\x > 0 \) for every non-zero \( \x \in \nR^3 \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Step 1: pivot \( 4 \), multipliers \( \ell_{21} = -1 \), \( \ell_{31} = 2 \). Row 2 becomes \( (-4, 5, -11) + (4, -4, 8) = (0, 1, -3) \), row 3 becomes \( (8, -11, 27) - 2(4, -4, 8) = (0, -3, 11) \). Step 2: pivot \( 1 \), multiplier \( \ell_{32} = -3 \); row 3 becomes \( (0, -3, 11) + 3(0, 1, -3) = (0, 0, 2) \). Hence
\[
L = \begin{pmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 2 & -3 & 1 \end{pmatrix}, \qquad U = \begin{pmatrix} 4 & -4 & 8 \\ 0 & 1 & -3 \\ 0 & 0 & 2 \end{pmatrix},
\]
and \( A = LU \) by @thm-lu-exists-without-swaps. The diagonal \( 4, 1, 2 \) of \( U \) is non-zero, so \( U \) is invertible (@lem-triangular-invertible), \( L \) is invertible (@lem-unit-lower-triangular-closed), and \( A = LU \) is invertible. \( A \) is symmetric, so by @thm-ldlt, with \( D = \diag(4, 1, 2) \),
\[
A = LDL\tp, \qquad DL\tp = \begin{pmatrix} 4 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix}\begin{pmatrix} 1 & -1 & 2 \\ 0 & 1 & -3 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 4 & -4 & 8 \\ 0 & 1 & -3 \\ 0 & 0 & 2 \end{pmatrix} = U,
\]
which confirms the theorem directly.
2. Let \( \x \neq \0 \) and put \( \y = L\tp\x \). By @lem-unit-lower-triangular-closed, \( L \) is invertible, so \( L\tp \) is invertible by @thm-inverse-matrix-properties (4), so \( \y \neq \0 \) (otherwise \( \x = (L\tp)^{-1}\y = \0 \)). By @thm-transpose-properties, \( \y\tp = \x\tp L \), so
\[
\x\tp A \x = \x\tp L D L\tp \x = \y\tp D \y = 4y_1^2 + y_2^2 + 2y_3^2 ,
\]
reading the \( 1 \times 1 \) matrix as a real number. Each term is \( \ge 0 \), and at least one \( y_i \neq 0 \), which makes its term strictly positive. Hence \( \x\tp A\x > 0 \).
:::
:::

::: {#exr-lu-factorization-c3}
[C3: Counting matrices without an LU factorization]

::: {.enumerate options="label=(\alph*)"}
1. Let \( A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in M_2(F) \). Prove that \( A \) has an LU factorization if and only if \( a \neq 0 \) or \( c = 0 \).
2. Let \( q \) be a prime. How many matrices in \( M_2(\nF_q) \) have **no** LU factorization? List them for \( q = 2 \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. (⇒) Suppose \( A = LU \) with \( L = \begin{pmatrix} 1 & 0 \\ \ell & 1 \end{pmatrix} \) and \( U = \begin{pmatrix} u & v \\ 0 & w \end{pmatrix} \). As in @exm-no-lu-factorization, \( LU = \begin{pmatrix} u & v \\ \ell u & \ell v + w \end{pmatrix} \), so \( a = u \) and \( c = \ell u = \ell a \). If \( a = 0 \), then \( c = 0 \). Hence \( a \neq 0 \) or \( c = 0 \).

   (⇐) If \( a \neq 0 \), elimination without row swaps succeeds with multiplier \( \ell = c/a \), and indeed
   \[
   \begin{pmatrix} 1 & 0 \\ c/a & 1 \end{pmatrix}\begin{pmatrix} a & b \\ 0 & d - cb/a \end{pmatrix} = \begin{pmatrix} a & b \\ c & cb/a + d - cb/a \end{pmatrix} = A .
   \]
   If \( c = 0 \), then \( A \) is upper triangular and \( A = IA \).
2. By (a), \( A \) has no LU factorization exactly when \( a = 0 \) and \( c \neq 0 \). There are \( q - 1 \) choices of \( c \), and \( q \) choices each of \( b \) and \( d \), so there are \( (q - 1)q^2 \) such matrices. For \( q = 2 \) this gives \( 4 \) of the \( 16 \) matrices: \( a = 0 \), \( c = 1 \), and \( b, d \in \{0, 1\} \), that is,
\[
\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}, \quad \begin{pmatrix} 0 & 0 \\ 1 & 1 \end{pmatrix}, \quad \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}.
\]
:::
:::
