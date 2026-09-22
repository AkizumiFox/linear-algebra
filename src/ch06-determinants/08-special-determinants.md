# Special Determinants

A determinant of size \( n \) has \( n! \) terms, so a general formula for a large matrix is hopeless. Some matrices, though, have so much structure that their determinants collapse to a short product or a recurrence. This section computes the most useful of them: the Vandermonde determinant, which governs polynomial interpolation; tridiagonal determinants, which satisfy a three-term recurrence; block triangular determinants, which split into smaller ones; and the determinant of a rank-one update of the identity. The proofs share one idea: find the structure first (a polynomial with known roots, a row with two non-zero entries, a pattern of zeros) and let the defining properties of the determinant do the rest.

## The Vandermonde determinant

Chapter 2 proved that there is exactly one polynomial of degree at most \( n \) through \( n + 1 \) points with distinct first coordinates (@thm-interpolation-unique). Behind it sat a square matrix of powers of the nodes. Its determinant turns out to be a product of all the differences of the nodes, and that product explains at a glance why distinct nodes are exactly what is needed.

For \( x_1, \dots, x_n \in F \), the **Vandermonde matrix** is
\[
\V(x_1, \dots, x_n) \coloneqq \begin{pmatrix} 1 & x_1 & x_1^2 & \cdots & x_1^{n-1} \\ 1 & x_2 & x_2^2 & \cdots & x_2^{n-1} \\ \vdots & \vdots & \vdots & & \vdots \\ 1 & x_n & x_n^2 & \cdots & x_n^{n-1} \end{pmatrix} \in M_n(F),
\]
whose \( (i, j) \)-entry is \( x_i^{j-1} \). Row \( i \) lists the powers \( 1, x_i, \dots, x_i^{n-1} \) of the \( i \)-th node. For \( n = 1 \) it is the \( 1 \times 1 \) matrix \( (1) \), and for \( n = 2 \) its determinant is \( x_2 - x_1 \).

::: {#thm-vandermonde-determinant}
[Vandermonde Determinant]

Let \( n \ge 1 \) and \( x_1, \dots, x_n \in F \). Then
\[
\det \V(x_1, \dots, x_n) = \prod_{1 \le i < j \le n} (x_j - x_i),
\]
where the empty product (for \( n = 1 \)) is \( 1 \).
:::

::: {.idea}
Induction on \( n \). Replace the last node \( x_n \) by a variable \( t \). Expanding along the last row shows the determinant is a polynomial \( f(t) \) of degree at most \( n - 1 \), with leading coefficient the smaller Vandermonde determinant. Setting \( t = x_i \) for \( i < n \) makes two rows equal, so \( x_1, \dots, x_{n-1} \) are roots of \( f \). A polynomial of degree at most \( n - 1 \) with these \( n - 1 \) roots is its leading coefficient times \( \prod_{i<n}(t - x_i) \). Now put \( t = x_n \) back. The roots argument needs the \( x_i \) distinct; if they are not, both sides are \( 0 \) anyway.
:::

::: {.proof}
We use induction on \( n \) (@thm-induction). For \( n = 1 \), \( \det(1) = 1 \), the empty product.

Let \( n \ge 2 \), assume the formula for \( n - 1 \) nodes, and write \( \V = \V(x_1, \dots, x_n) \). Let \( C_{n1}, \dots, C_{nn} \) be the cofactors of \( \V \) along row \( n \) (@def-minor-cofactor). Each \( C_{nj} \) is computed after deleting row \( n \), so it does not involve \( x_n \). Define
\[
f(t) \coloneqq \sum_{j=1}^{n} C_{nj}\, t^{j-1} \in F[t] .
\]
For \( c \in F \), let \( \V_c \) be \( \V \) with row \( n \) replaced by \( (1, c, \dots, c^{n-1}) \). Then \( \V_c \) has the same cofactors along row \( n \) as \( \V \), so by @thm-laplace-expansion along row \( n \),
\[
\det \V_c = \sum_{j=1}^{n} c^{j-1} C_{nj} = f(c) . \tag{$\ast$}
\]
In particular \( \det \V = f(x_n) \). The coefficient of \( t^{n-1} \) in \( f \) is \( C_{nn} = (-1)^{2n}\det \V(x_1, \dots, x_{n-1}) \), since deleting row \( n \) and column \( n \) of \( \V \) leaves the Vandermonde matrix of the first \( n - 1 \) nodes.

*Case 1: two of \( x_1, \dots, x_{n-1} \) are equal,* say \( x_p = x_q \) with \( p < q < n \). Then rows \( p \) and \( q \) of \( \V \) are equal. By @thm-det-transpose, \( \det \V = \det \V\tp \), and \( \V\tp \) has two equal columns, so \( \det \V = 0 \) because the determinant is alternating (@def-alternating-form). The product also vanishes, since it contains the factor \( x_q - x_p = 0 \).

*Case 2: \( x_1, \dots, x_{n-1} \) are distinct.* For \( i < n \), the matrix \( \V_{x_i} \) has rows \( i \) and \( n \) equal, so \( f(x_i) = \det \V_{x_i} = 0 \) by \( (\ast) \) and the argument of Case 1. Hence \( x_1, \dots, x_{n-1} \) are \( n - 1 \) distinct roots of \( f \), and by @cor-root-bound-general,
\[
g(t) \coloneqq (t - x_1)(t - x_2)\cdots(t - x_{n-1}) \ \text{ divides } \ f .
\]
Write \( f = hg \) with \( h \in F[t] \). If \( h \ne 0 \), then \( \deg h = \deg f - (n - 1) \le 0 \) by @thm-degree-of-product, since \( \deg f \le n - 1 \); so in every case \( h \) is a constant \( h \in F \). As \( g \) is monic of degree \( n - 1 \), the coefficient of \( t^{n-1} \) in \( hg \) is \( h \), so \( h = C_{nn} = \det \V(x_1, \dots, x_{n-1}) \). Evaluating at \( x_n \) (@thm-evaluation-respects-operations) and using the induction hypothesis,
\[
\begin{aligned}
\det \V &= f(x_n) = \det \V(x_1, \dots, x_{n-1}) \prod_{i=1}^{n-1}(x_n - x_i) \\
&= \prod_{1 \le i < j \le n-1}(x_j - x_i) \prod_{i=1}^{n-1}(x_n - x_i) .
\end{aligned}
\]
The two products together run over all pairs \( i < j \le n \), the second one collecting exactly the pairs with \( j = n \). This proves the formula for \( n \), and the theorem follows by induction.
:::

::: {#exm-vandermonde-three}
[A \( 3 \times 3 \) Vandermonde Determinant]

Compute \( \det \V(1, 2, 4) \) from the formula and by cofactor expansion.
:::

::: {.solution}
The formula gives \( (2 - 1)(4 - 1)(4 - 2) = 1 \cdot 3 \cdot 2 = 6 \). Directly, expanding
\[
\V(1, 2, 4) = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 4 \\ 1 & 4 & 16 \end{pmatrix}
\]
along the first row gives \( 1\cdot(32 - 16) - 1\cdot(16 - 4) + 1\cdot(4 - 2) = 16 - 12 + 2 = 6 \).
:::

The product vanishes exactly when a factor does, because a field has no zero divisors. So:

::: {#cor-vandermonde-nonzero}
[Distinct Nodes Give an Invertible Vandermonde Matrix]

\( \V(x_1, \dots, x_n) \) is invertible if and only if \( x_1, \dots, x_n \) are **distinct**.
:::

::: {.proof}
In a field, a product is non-zero if and only if every factor is non-zero (@thm-field-basic-properties (f), applied repeatedly). So by @thm-vandermonde-determinant, \( \det \V(x_1, \dots, x_n) \ne 0 \) if and only if \( x_j \ne x_i \) for all \( i < j \). By @thm-det-nonzero-iff-invertible, this is equivalent to invertibility.
:::

Now the promised two-line proof of @thm-interpolation-unique. Given distinct \( x_0, \dots, x_n \) and values \( y_0, \dots, y_n \), a polynomial \( p = c_0 + c_1x + \dots + c_nx^n \) satisfies \( p(x_i) = y_i \) for all \( i \) if and only if \( \V(x_0, \dots, x_n)\,\c = \y \), since row \( i \) of this system reads \( c_0 + c_1x_i + \dots + c_nx_i^n = y_i \). By @cor-vandermonde-nonzero the matrix is invertible, so the system has exactly one solution \( \c = \V(x_0, \dots, x_n)^{-1}\y \) (@thm-invertible-tfae), and the interpolating polynomial exists and is unique.

::: {.remark}
This is not a proof from nothing. The root bound of Chapter 5 (@cor-root-bound-general) did the real work inside @thm-vandermonde-determinant, exactly as the root bound did in Chapter 2 (@lem-root-bound). What the determinant adds is an explicit number: it says how close to singular the interpolation problem is, since nodes that nearly coincide make the product small.
:::

::: {.warning}
**Watch the shape and the order.** The formula is for rows \( (1, x_i, \dots, x_i^{n-1}) \) starting at the power \( 0 \), and for the factors \( x_j - x_i \) with \( i < j \), "later node minus earlier node". Dropping the column of ones changes the answer: \( \det\begin{pmatrix} x_1 & x_1^2 \\ x_2 & x_2^2 \end{pmatrix} = x_1x_2(x_2 - x_1) \), not \( x_2 - x_1 \). Writing the factors as \( x_i - x_j \) instead flips the sign of each of the \( \binom{n}{2} \) factors, so it multiplies the answer by \( (-1)^{\binom{n}{2}} \): already for \( n = 2 \) and \( n = 3 \) this is \( -1 \), a wrong sign.
:::

::: {.check}
Without expanding, find \( \det \V(1, 2, 3, 5) \).
:::

::: {.solution}
The pairs \( i < j \) give \( (2 - 1)(3 - 1)(5 - 1)(3 - 2)(5 - 2)(5 - 3) = 1 \cdot 2 \cdot 4 \cdot 1 \cdot 3 \cdot 2 = 48 \).
:::

## Tridiagonal determinants

Many matrices in applications have non-zero entries only on the diagonal and next to it: discretized differential equations, chains of springs, the recurrences of orthogonal polynomials. Such a matrix is **tridiagonal**. Its determinant is not a closed formula in general, but it obeys a recurrence in the size, because the last row has only two non-zero entries.

Let \( \T_n \in M_n(F) \) have diagonal entries \( a_1, \dots, a_n \), entries \( b_1, \dots, b_{n-1} \) just above the diagonal (\( (i, i+1) \)-entry \( b_i \)), entries \( c_1, \dots, c_{n-1} \) just below it (\( (i+1, i) \)-entry \( c_i \)), and zeros elsewhere:
\[
\T_n = \begin{pmatrix} a_1 & b_1 & & & \\ c_1 & a_2 & b_2 & & \\ & c_2 & \ddots & \ddots & \\ & & \ddots & a_{n-1} & b_{n-1} \\ & & & c_{n-1} & a_n \end{pmatrix}.
\]
For \( 1 \le k \le n \), the top-left \( k \times k \) block of \( \T_n \) is the tridiagonal matrix \( \T_k \) built from \( a_1, \dots, a_k \), \( b_1, \dots, b_{k-1} \), \( c_1, \dots, c_{k-1} \). Write \( D_k = \det \T_k \), and set \( D_0 = 1 \).

::: {#thm-tridiagonal-recurrence}
[Tridiagonal Recurrence]

With this notation, \( D_1 = a_1 \), and for \( 2 \le k \le n \),
\[
D_k = a_k\,D_{k-1} - b_{k-1}c_{k-1}\,D_{k-2} .
\]
:::

::: {.proof}
\( D_1 = \det(a_1) = a_1 \). For \( k = 2 \), \( D_2 = a_1a_2 - b_1c_1 = a_2D_1 - b_1c_1D_0 \). Let \( k \ge 3 \). Row \( k \) of \( \T_k \) has only two possibly non-zero entries, \( c_{k-1} \) in column \( k - 1 \) and \( a_k \) in column \( k \). By @thm-laplace-expansion along row \( k \),
\[
D_k = c_{k-1}(-1)^{2k-1}M_{k,k-1} + a_k(-1)^{2k}M_{kk} = a_kM_{kk} - c_{k-1}M_{k,k-1},
\]
where \( M_{kk} = \det \T_{k-1} = D_{k-1} \). The minor \( M_{k,k-1} \) is the determinant of the \( (k - 1) \times (k - 1) \) matrix obtained by deleting row \( k \) and column \( k - 1 \). Its last column consists of rows \( 1, \dots, k - 1 \) of column \( k \) of \( \T_k \), which is \( b_{k-1} \) in the last position and \( 0 \) elsewhere. Expanding along this last column (@thm-laplace-expansion), with sign \( (-1)^{(k-1)+(k-1)} = 1 \), gives \( M_{k,k-1} = b_{k-1}\det \T_{k-2} = b_{k-1}D_{k-2} \), because deleting the last row and column leaves rows and columns \( 1, \dots, k - 2 \) of \( \T_k \). Substituting proves the recurrence.
:::

::: {#exm-tridiagonal-fibonacci}
[Fibonacci Numbers as Determinants]

Let \( \T_n \) have \( 1 \) on the diagonal, \( 1 \) above it and \( -1 \) below it. Find \( D_n = \det \T_n \).
:::

::: {.solution}
Here \( a_k = 1 \) and \( b_{k-1}c_{k-1} = 1 \cdot (-1) = -1 \), so @thm-tridiagonal-recurrence gives \( D_k = D_{k-1} + D_{k-2} \) for \( k \ge 2 \), with \( D_0 = 1 \) and \( D_1 = 1 \). Hence
\[
D_1, D_2, D_3, \dots = 1, 2, 3, 5, 8, 13, 21, 34, \dots,
\]
the Fibonacci numbers: \( D_n = F_{n+1} \), where \( F_1 = F_2 = 1 \) and \( F_{k} = F_{k-1} + F_{k-2} \). For instance
\[
D_3 = \det\begin{pmatrix} 1 & 1 & 0 \\ -1 & 1 & 1 \\ 0 & -1 & 1 \end{pmatrix} = 1\cdot(1 + 1) - 1\cdot(-1 - 0) + 0 = 3 .
\]
:::

Only the products \( b_{k-1}c_{k-1} \) enter the recurrence, never \( b_{k-1} \) and \( c_{k-1} \) separately. For example, for a real number \( t \), putting \( 2t \) on the diagonal and \( 1 \) on both neighboring lines gives \( D_k = 2t\,D_{k-1} - D_{k-2} \), so \( D_1 = 2t \), \( D_2 = 4t^2 - 1 \), \( D_3 = 8t^3 - 4t \). These are the Chebyshev polynomials of the second kind.

## Block triangular matrices

A matrix can be cut into blocks by a horizontal and a vertical line. When the block in the lower left is zero, the determinant should see only the two square blocks on the diagonal, just as a triangular determinant sees only diagonal entries. This result is used constantly, for instance in Chapter 7 for Schur complements.

::: {#thm-det-block-triangular}
[Block Triangular Determinant]

Let \( \A \in M_k(F) \), \( \D \in M_l(F) \) and \( \B \in M_{k \times l}(F) \), with \( k, l \ge 1 \). Then
\[
\det\begin{pmatrix} \A & \B \\ 0 & \D \end{pmatrix} = \det \A \cdot \det \D ,
\]
where \( 0 \) is the \( l \times k \) zero matrix. The same holds for \( \begin{pmatrix} \A & 0 \\ \C & \D \end{pmatrix} \) with \( \C \in M_{l \times k}(F) \).
:::

::: {.idea}
In the Leibniz formula for the whole matrix, a term picks one entry from each column. The first \( k \) columns have zeros below row \( k \), so a non-zero term must pick rows \( 1, \dots, k \) for the first \( k \) columns, and is then forced to pick rows \( k+1, \dots, n \) for the last \( l \) columns. Such a permutation is a permutation of each block, its inversions are the inversions inside the blocks, and the Leibniz sum factors into two Leibniz sums.
:::

::: {.proof}
Let \( n = k + l \) and \( \M = \begin{pmatrix} \A & \B \\ 0 & \D \end{pmatrix} = (m_{ij}) \). By @def-determinant, \( \det \M = \sum_{\sigma \in S_n} \sgn(\sigma) \prod_{j=1}^{n} m_{\sigma(j)j} \). Since \( m_{ij} = 0 \) for \( i > k \ge j \), the term of \( \sigma \) is \( 0 \) unless \( \sigma(j) \le k \) for every \( j \le k \). For such \( \sigma \), the injective map \( \sigma \) sends \( \{1, \dots, k\} \) into itself, hence onto itself (a finite set), and so it sends \( \{k+1, \dots, n\} \) onto itself. Therefore \( \sigma \) determines \( \alpha \in S_k \) and \( \beta \in S_l \) by
\[
\alpha(j) = \sigma(j) \quad (j \le k), \qquad \beta(q) = \sigma(k + q) - k \quad (q \le l),
\]
and every pair \( (\alpha, \beta) \) arises from exactly one such \( \sigma \).

We compare signs through inversions (@def-inversion). A pair \( i < j \) with \( i, j \le k \) is an inversion of \( \sigma \) exactly when it is one of \( \alpha \); a pair \( k + p < k + q \) is an inversion of \( \sigma \) exactly when \( p < q \) is one of \( \beta \); and a pair \( i \le k < j \) is never an inversion, since \( \sigma(i) \le k < \sigma(j) \). By @def-sign-permutation, \( \sgn(\sigma) = \sgn(\alpha)\sgn(\beta) \). Also \( m_{\sigma(j)j} = a_{\alpha(j)j} \) for \( j \le k \) and \( m_{\sigma(k+q),k+q} = d_{\beta(q)q} \). Hence
\[
\det \M = \sum_{\alpha \in S_k}\sum_{\beta \in S_l} \sgn(\alpha)\sgn(\beta) \prod_{j=1}^{k} a_{\alpha(j)j} \prod_{q=1}^{l} d_{\beta(q)q} = \det \A \cdot \det \D,
\]
using @def-determinant twice. For the lower block triangular case, the transpose of \( \begin{pmatrix} \A & 0 \\ \C & \D \end{pmatrix} \) is \( \begin{pmatrix} \A\tp & \C\tp \\ 0 & \D\tp \end{pmatrix} \), so by @thm-det-transpose and the first case its determinant is \( \det \A\tp \det \D\tp = \det \A \det \D \).
:::

The proof uses only sums and products of entries, so, like the results flagged in §4–§6, it holds for matrices over any commutative ring; §10 uses this over \( F[x] \). By induction on the number of blocks, a matrix with square blocks \( \A_1, \dots, \A_r \) on the diagonal and zeros below them has determinant \( \det \A_1 \cdots \det \A_r \); @thm-det-triangular is the case where every block is \( 1 \times 1 \).

For example,
\[
\det\begin{pmatrix} 2 & 1 & 5 & -3 \\ 1 & 1 & 0 & 7 \\ 0 & 0 & 3 & 1 \\ 0 & 0 & 4 & 2 \end{pmatrix} = \det\begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}\det\begin{pmatrix} 3 & 1 \\ 4 & 2 \end{pmatrix} = 1 \cdot 2 = 2,
\]
and the entries \( 5, -3, 0, 7 \) of the upper right block play no role.

::: {.warning}
**There is no "block \( ad - bc \)" rule.** For a general block matrix, \( \det\begin{pmatrix} \A & \B \\ \C & \D \end{pmatrix} \ne \det \A\det \D - \det \B\det \C \). Take \( \A = \D = 0 \) and \( \B = \C = \I_2 \): the \( 4 \times 4 \) matrix \( \begin{pmatrix} 0 & \I_2 \\ \I_2 & 0 \end{pmatrix} \) is the permutation matrix of \( (1\ 3)(2\ 4) \), a product of two transpositions, so its determinant is \( +1 \); the rule would give \( 0 \cdot 0 - 1 \cdot 1 = -1 \). The zero block in the corner is what the theorem needs. The correct formulas for general blocks use Schur complements, in Chapter 7.
:::

::: {.check}
Is \( \det\begin{pmatrix} \A & \B \\ 0 & \D \end{pmatrix} = \det \A \det \D \) meaningful when \( \A \) is \( 2 \times 3 \) and \( \D \) is \( 3 \times 2 \) (so the whole matrix is \( 5 \times 5 \))?
:::

::: {.solution}
No. The theorem requires \( \A \) and \( \D \) square; here \( \det \A \) and \( \det \D \) are undefined. In fact the whole determinant is \( 0 \) whatever the entries: the first \( 3 \) columns have their non-zero entries only in the first \( 2 \) rows, so they are linearly dependent in a \( 2 \)-dimensional space, and a determinant with dependent columns is \( 0 \) (@thm-alternating-properties).
:::

## Rank-one updates

Changing a matrix by a rank-one matrix \( \u\v\tp \) is the smallest possible change in the sense of rank, and it happens often: updating one observation in statistics, modifying one row of a system, or adding the same number to every entry. The determinant of the updated identity turns out to be a single dot product.

::: {#thm-matrix-determinant-lemma}
[Matrix Determinant Lemma]

Let \( \u, \v \in F^n \). Then
\[
\det(\I_n + \u\v\tp) = 1 + \v\tp\u .
\]
:::

::: {.idea}
Border \( \I_n + \u\v\tp \) by an extra column \( \u \) and an extra row \( (\0\tp, 1) \), giving a block triangular matrix \( \M \) with the same determinant. Then clear the update by elimination with blocks. Rows: add \( \v\tp \) times the top \( n \) rows to the new bottom row (multiply by \( \L \) on the left). Columns: subtract the last column times \( \v\tp \) from the first \( n \) columns (multiply by \( \L' \) on the right). The factors \( \L \), \( \L' \) have determinant \( 1 \), and the result is block triangular with \( \I_n \) and the \( 1 \times 1 \) block \( 1 + \v\tp\u \) on the diagonal.
:::

::: {.proof}
Consider the \( (n+1) \times (n+1) \) block matrices
\[
\L = \begin{pmatrix} \I_n & \0 \\ \v\tp & 1 \end{pmatrix}, \qquad \M = \begin{pmatrix} \I_n + \u\v\tp & \u \\ \0\tp & 1 \end{pmatrix}, \qquad \L' = \begin{pmatrix} \I_n & \0 \\ -\v\tp & 1 \end{pmatrix}.
\]
Splitting the sum \( \sum_{j} \) in @thm-three-views-of-product (1) into the indices \( j \le n \) and \( j = n + 1 \) shows that matrices partitioned in this way multiply block by block, like \( 2 \times 2 \) matrices whose entries are blocks. Hence
\[
\L\M = \begin{pmatrix} \I_n + \u\v\tp & \u \\ \v\tp + (\v\tp\u)\v\tp & \v\tp\u + 1 \end{pmatrix},
\]
where we used \( \v\tp(\u\v\tp) = (\v\tp\u)\v\tp \) by associativity, \( \v\tp\u \) being a \( 1 \times 1 \) matrix, that is, a scalar. Multiplying on the right by \( \L' \),
\[
\L\M\L' = \begin{pmatrix} \I_n + \u\v\tp - \u\v\tp & \u \\ \v\tp + (\v\tp\u)\v\tp - (1 + \v\tp\u)\v\tp & 1 + \v\tp\u \end{pmatrix} = \begin{pmatrix} \I_n & \u \\ \0\tp & 1 + \v\tp\u \end{pmatrix}.
\]
By @thm-det-block-triangular, \( \det \L = \det \I_n \cdot 1 = 1 \), \( \det \L' = 1 \), \( \det \M = \det(\I_n + \u\v\tp) \cdot 1 \), and \( \det(\L\M\L') = \det \I_n\,(1 + \v\tp\u) = 1 + \v\tp\u \). By @thm-det-multiplicative, \( \det(\L\M\L') = \det \L\det \M\det \L' = \det(\I_n + \u\v\tp) \). This proves the lemma.
:::

::: {#exm-all-ones-perturbed}
[\( a \) on the Diagonal, \( 1 \) Elsewhere]

Let \( a \in \nR \) and \( n \ge 1 \), and let \( \A_n \in M_n(\nR) \) have every diagonal entry \( a \) and every other entry \( 1 \). Find \( \det \A_n \).
:::

::: {.solution}
Let \( \mathbf{1} = (1, \dots, 1) \in \nR^n \). Every entry of \( \mathbf{1}\mathbf{1}\tp \) is \( 1 \), so \( \A_n = (a - 1)\I_n + \mathbf{1}\mathbf{1}\tp \).

*Case \( a \ne 1 \).* Then \( \A_n = (a - 1)\big(\I_n + \u\mathbf{1}\tp\big) \) with \( \u = \frac{1}{a-1}\mathbf{1} \). Scaling an \( n \times n \) matrix by \( c \) multiplies its determinant by \( c^n \) (multilinearity in each of the \( n \) columns), so by @thm-matrix-determinant-lemma
\[
\det \A_n = (a - 1)^n\Big(1 + \frac{n}{a - 1}\Big) = (a - 1)^{n-1}(a - 1 + n),
\]
since \( \mathbf{1}\tp\u = \frac{n}{a-1} \).

*Case \( a = 1 \).* For \( n \ge 2 \), all columns are equal, so \( \det \A_n = 0 \), which the formula also gives. For \( n = 1 \), \( \det \A_1 = 1 \), and the formula gives \( (a - 1)^0 \cdot 1 = 1 \).

So \( \det \A_n = (a - 1)^{n-1}(a + n - 1) \) for every \( a \). For \( n = 3 \) this is \( (a - 1)^2(a + 2) \); with \( a = 3 \) it gives \( 4 \cdot 5 = 20 \).
:::

::: {.warning}
**The lemma is about \( \I_n + \u\v\tp \), not \( \u\v\tp \) or \( \u\tp\v \).** The rank-one matrix \( \u\v\tp \) is \( n \times n \) and, for \( n \ge 2 \), has determinant \( 0 \); the scalar \( \v\tp\u \) is its trace. Do not confuse \( \det(\I_n + \u\v\tp) = 1 + \v\tp\u \) with \( \det(\I_n) + \det(\u\v\tp) = 1 \) (for \( n \ge 2 \)), which is false whenever \( \v\tp\u \ne 0 \): for \( \u = \v = \e_1 \), \( \I_n + \e_1\e_1\tp = \diag(2, 1, \dots, 1) \) has determinant \( 2 \).
:::

## Exercises

### A. Check your understanding

:::: {#exr-special-determinants-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the Vandermonde determinant formula, including the order of the factors.
2. True or false: \( \V(x_1, \dots, x_n) \) is invertible whenever \( x_1, \dots, x_n \) are non-zero. Justify your answer.
3. Write down the recurrence for the determinant of a tridiagonal matrix, and say which row the proof expands along.
4. True or false: \( \det\begin{pmatrix} \A & \B \\ \C & \D \end{pmatrix} = \det \A\det \D \) whenever \( \A \) and \( \D \) are square and \( \B = 0 \). Justify your answer.
5. True or false: \( \det(\I_n + \u\v\tp) = \det(\I_n + \v\u\tp) \) for all \( \u, \v \in F^n \). Justify your answer.
:::
::::

::: {.solution}
(a) \( \det \V(x_1, \dots, x_n) = \prod_{1 \le i < j \le n}(x_j - x_i) \), where \( \V \) has \( (i, j) \)-entry \( x_i^{j-1} \) (@thm-vandermonde-determinant).

(b) False. \( \V(1, 1) = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \) has non-zero nodes and determinant \( 0 \). The condition is that the nodes are **distinct** (@cor-vandermonde-nonzero); \( 0 \) is allowed as a node.

(c) \( D_k = a_kD_{k-1} - b_{k-1}c_{k-1}D_{k-2} \), with \( D_0 = 1 \), \( D_1 = a_1 \) (@thm-tridiagonal-recurrence). The proof expands along the last row, which has only two non-zero entries.

(d) True. With \( \B = 0 \) the matrix is lower block triangular, and @thm-det-block-triangular applies.

(e) True. Both equal \( 1 + \v\tp\u = 1 + \u\tp\v \) by @thm-matrix-determinant-lemma, since \( \v\tp\u = \sum_i v_iu_i = \u\tp\v \).
:::

### B. Practice

:::: {#exr-special-determinants-b1}
[B1: A \( 4 \times 4 \) Vandermonde determinant]

Compute \( \det\begin{pmatrix} 1 & -1 & 1 & -1 \\ 1 & 0 & 0 & 0 \\ 1 & 1 & 1 & 1 \\ 1 & 2 & 4 & 8 \end{pmatrix} \). Hence decide whether there is exactly one polynomial \( p \in \nR[x]_{\le 3} \) with \( p(-1) = 3 \), \( p(0) = 1 \), \( p(1) = 0 \), \( p(2) = 5 \).
::::

::: {.solution}
Row \( i \) is \( (1, x_i, x_i^2, x_i^3) \) with nodes \( -1, 0, 1, 2 \), so this is \( \V(-1, 0, 1, 2) \). By @thm-vandermonde-determinant its determinant is
\[
(0 - (-1))(1 - (-1))(2 - (-1))(1 - 0)(2 - 0)(2 - 1) = 1 \cdot 2 \cdot 3 \cdot 1 \cdot 2 \cdot 1 = 12 .
\]
(Check by expanding along row \( 2 \), which is \( (1, 0, 0, 0) \): the determinant is \( (-1)^{2+1}\det\begin{pmatrix} -1 & 1 & -1 \\ 1 & 1 & 1 \\ 2 & 4 & 8 \end{pmatrix} = -\big({-1}(8 - 4) - 1(8 - 2) - 1(4 - 2)\big) = -(-4 - 6 - 2) = 12 \).) Hence the coefficient matrix of the interpolation system is invertible, and there is exactly one \( p \in \nR[x]_{\le 3} \) with the given values.
:::

:::: {#exr-special-determinants-b2}
[B2: The second-difference matrix]

Let \( \K_n \in M_n(\nR) \) have \( 2 \) on the diagonal, \( -1 \) directly above and below it, and \( 0 \) elsewhere. Prove that \( \det \K_n = n + 1 \). Hence show that \( \K_n \) is invertible for every \( n \).
::::

::: {.solution}
Here \( a_k = 2 \) and \( b_{k-1}c_{k-1} = (-1)(-1) = 1 \). By @thm-tridiagonal-recurrence, \( D_k = 2D_{k-1} - D_{k-2} \) for \( k \ge 2 \), with \( D_0 = 1 \), \( D_1 = 2 \). We show \( D_k = k + 1 \) by strong induction on \( k \) (@thm-strong-induction). It holds for \( k = 0, 1 \). If it holds for \( k - 1 \) and \( k - 2 \), then \( D_k = 2k - (k - 1) = k + 1 \). Hence \( \det \K_n = D_n = n + 1 \ne 0 \), and \( \K_n \) is invertible by @thm-det-nonzero-iff-invertible.
:::

:::: {#exr-special-determinants-b3}
[B3: A rank-one update]

Let \( \u = (1, 2, 3) \) and \( \v = (1, -1, 2) \) in \( \nQ^3 \).

::: {.enumerate options="label=(\alph*)"}
1. Use @thm-matrix-determinant-lemma to find \( \det(\I_3 + \u\v\tp) \).
2. Write out \( \I_3 + \u\v\tp \) and check your answer by elimination.
3. Find all \( t \in \nQ \) for which \( \I_3 + t\,\u\v\tp \) is **not** invertible.
:::
::::

::: {.solution}
(a) \( \v\tp\u = 1 - 2 + 6 = 5 \), so \( \det(\I_3 + \u\v\tp) = 6 \).

(b) \( \u\v\tp = \begin{pmatrix} 1 & -1 & 2 \\ 2 & -2 & 4 \\ 3 & -3 & 6 \end{pmatrix} \), so \( \I_3 + \u\v\tp = \begin{pmatrix} 2 & -1 & 2 \\ 2 & -1 & 4 \\ 3 & -3 & 7 \end{pmatrix} \). Subtract row \( 1 \) from row \( 2 \), which does not change the determinant (@thm-det-row-operations), to get row \( 2 \) equal to \( (0, 0, 2) \). Expanding along that row,
\[
\det = 2 \cdot (-1)^{2+3}\det\begin{pmatrix} 2 & -1 \\ 3 & -3 \end{pmatrix} = -2(-6 + 3) = 6 .
\]

(c) \( \I_3 + t\,\u\v\tp = \I_3 + (t\u)\v\tp \), whose determinant is \( 1 + t\,\v\tp\u = 1 + 5t \). It is zero exactly for \( t = -\frac15 \), and by @thm-det-nonzero-iff-invertible that is the only \( t \) for which the matrix is not invertible.
:::

### C. Going deeper

:::: {#exr-special-determinants-c1}
[C1: The Cauchy determinant]

Let \( x_1, \dots, x_n, y_1, \dots, y_n \in F \) with \( x_i + y_j \ne 0 \) for all \( i, j \), and let \( \Q_n \in M_n(F) \) have \( (i, j) \)-entry \( \dfrac{1}{x_i + y_j} \). The goal is
\[
\det \Q_n = \frac{\prod_{1 \le i < j \le n}(x_j - x_i)(y_j - y_i)}{\prod_{i=1}^{n}\prod_{j=1}^{n}(x_i + y_j)} .
\]

::: {.enumerate options="label=(\alph*)"}
1. For \( i < n \), subtract row \( n \) from row \( i \). Show that the new \( (i, j) \)-entry is \( \dfrac{x_n - x_i}{(x_i + y_j)(x_n + y_j)} \), and deduce that \( \det \Q_n = \dfrac{\prod_{i<n}(x_n - x_i)}{\prod_{j}(x_n + y_j)}\det \Q' \), where \( \Q' \) agrees with \( \Q_n \) in rows \( 1, \dots, n-1 \) and has last row \( (1, \dots, 1) \).
2. In \( \Q' \), for \( j < n \), subtract column \( n \) from column \( j \). Deduce that \( \det \Q' = \dfrac{\prod_{j<n}(y_n - y_j)}{\prod_{i<n}(x_i + y_n)}\det \Q_{n-1} \), where \( \Q_{n-1} \) is built from \( x_1, \dots, x_{n-1} \) and \( y_1, \dots, y_{n-1} \).
3. Prove the formula by induction on \( n \).
4. The **Hilbert matrix** \( \H_n \) has \( (i, j) \)-entry \( \frac{1}{i + j - 1} \). Show that it is a Cauchy matrix, and use (c) to compute \( \det \H_3 \).
:::

*Hint: in (a) and (b), factor scalars out of whole rows and columns using multilinearity.*
::::

::: {.solution}
(a) For \( i < n \), \( \frac{1}{x_i + y_j} - \frac{1}{x_n + y_j} = \frac{(x_n + y_j) - (x_i + y_j)}{(x_i + y_j)(x_n + y_j)} = \frac{x_n - x_i}{(x_i + y_j)(x_n + y_j)} \). These row operations do not change the determinant (@thm-det-row-operations). In the new matrix, row \( i < n \) has the factor \( x_n - x_i \) in every entry, and column \( j \) has the factor \( \frac{1}{x_n + y_j} \) in every entry (in row \( n \), \( \frac{1}{x_n + y_j} = \frac{1}{x_n + y_j} \cdot 1 \)). Pulling these scalars out of each row and column by multilinearity (@thm-det-row-operations, in its row and column forms) leaves the matrix \( \Q' \) with entries \( \frac{1}{x_i + y_j} \) in rows \( i < n \) and \( 1 \) in row \( n \). This gives the stated formula.

(b) For \( j < n \), subtracting column \( n \) from column \( j \) leaves the determinant unchanged, makes the last row \( (0, \dots, 0, 1) \), and for \( i < n \) gives \( \frac{1}{x_i + y_j} - \frac{1}{x_i + y_n} = \frac{y_n - y_j}{(x_i + y_j)(x_i + y_n)} \). Pull \( y_n - y_j \) out of column \( j \) (\( j < n \)) and \( \frac{1}{x_i + y_n} \) out of row \( i \) (\( i < n \)); the last row \( (0, \dots, 0, 1) \) is unaffected by the column factors because its first \( n - 1 \) entries are \( 0 \), and row factors do not touch row \( n \). What remains has \( \frac{1}{x_i + y_j} \) in positions \( i, j < n \), entries \( (x_i + y_n)\cdot\frac{1}{x_i + y_n} = 1 \) in column \( n \) above the corner, and last row \( (0, \dots, 0, 1) \). Expanding along the last row (@thm-laplace-expansion) gives \( \det \Q_{n-1} \), with sign \( (-1)^{2n} = 1 \).

(c) For \( n = 1 \), \( \det \Q_1 = \frac{1}{x_1 + y_1} \), which is the formula with empty products upstairs. For \( n \ge 2 \), combining (a) and (b),
\[
\det \Q_n = \frac{\prod_{i<n}(x_n - x_i)(y_n - y_i)}{\prod_{j \le n}(x_n + y_j)\prod_{i<n}(x_i + y_n)}\det \Q_{n-1} .
\]
The numerator supplies exactly the factors of \( \prod_{i<j}(x_j - x_i)(y_j - y_i) \) with \( j = n \), and the denominator supplies exactly the factors \( x_i + y_j \) with \( \max(i, j) = n \), each once. By the induction hypothesis, \( \det \Q_{n-1} \) supplies all the remaining factors. This proves the formula.

(d) With \( x_i = i \) and \( y_j = j - 1 \), \( x_i + y_j = i + j - 1 \ge 1 \), so \( \H_n \) is a Cauchy matrix over \( \nQ \). For \( n = 3 \), the numerator is \( \big((2-1)(3-1)(3-2)\big)^2 = 4 \), since \( y_j - y_i = j - i = x_j - x_i \). The denominator is the product of all \( i + j - 1 \): the rows give \( 1 \cdot 2 \cdot 3 = 6 \), \( 2 \cdot 3 \cdot 4 = 24 \), \( 3 \cdot 4 \cdot 5 = 60 \), in total \( 8640 \). Hence \( \det \H_3 = \frac{4}{8640} = \frac{1}{2160} \). (In general \( \det \H_n = c_n^4 / c_{2n} \) with \( c_n = \prod_{k=1}^{n-1} k! \); we state this without proof. These determinants shrink extremely fast, which is why Hilbert matrices are a standard test of numerical methods.)
:::

:::: {#exr-special-determinants-c2}
[C2: A circulant determinant over \( \nC \)]

Let \( a, b, c \in \nC \), let \( \omega = e^{2\pi i/3} \), and let
\[
\Z = \begin{pmatrix} a & b & c \\ c & a & b \\ b & c & a \end{pmatrix}.
\]

::: {.enumerate options="label=(\alph*)"}
1. For \( k = 0, 1, 2 \), let \( \w_k = (1, \omega^k, \omega^{2k}) \) and \( \lambda_k = a + b\omega^k + c\omega^{2k} \). Show that \( \Z\w_k = \lambda_k\w_k \).
2. Let \( \W \) be the matrix with columns \( \w_0, \w_1, \w_2 \). Show that \( \Z\W = \W\diag(\lambda_0, \lambda_1, \lambda_2) \) and that \( \det \W \ne 0 \). Deduce \( \det \Z = \lambda_0\lambda_1\lambda_2 \).
3. Using \( \omega^3 = 1 \) and \( 1 + \omega + \omega^2 = 0 \), deduce \( \det \Z = a^3 + b^3 + c^3 - 3abc \), and check this against the Leibniz formula.
:::

Circulant matrices of every size are treated in Chapter 11.
::::

::: {.solution}
(a) By @exm-roots-of-unity, \( \omega^3 = 1 \), so \( \omega^{-k} = \omega^{2k} \) and \( \omega^{-2k} = \omega^{k} \). Row \( 1 \) of \( \Z\w_k \) is \( a + b\omega^k + c\omega^{2k} = \lambda_k \). Row \( 2 \) is \( c + a\omega^k + b\omega^{2k} = \omega^k(c\omega^{-k} + a + b\omega^k) = \omega^k(a + b\omega^k + c\omega^{2k}) = \omega^k\lambda_k \). Row \( 3 \) is \( b + c\omega^k + a\omega^{2k} = \omega^{2k}(b\omega^{-2k} + c\omega^{-k} + a) = \omega^{2k}\lambda_k \). Hence \( \Z\w_k = \lambda_k\w_k \).

(b) By @thm-three-views-of-product, column \( k \) of \( \Z\W \) is \( \Z\w_k = \lambda_k\w_k \), which is column \( k \) of \( \W\diag(\lambda_0, \lambda_1, \lambda_2) \). The \( (i, k) \)-entry of \( \W \) is \( (\omega^k)^{i-1} \), so \( \W = \V(1, \omega, \omega^2)\tp \). The nodes \( 1, \omega, \omega^2 \) are distinct (they are \( e^{2\pi ik/3} \) for \( k = 0, 1, 2 \)), so \( \det \W = \det \V(1, \omega, \omega^2) \ne 0 \) by @thm-det-transpose and @cor-vandermonde-nonzero. By @thm-det-multiplicative and @thm-det-triangular, \( \det \Z\det \W = \det \W\,\lambda_0\lambda_1\lambda_2 \), and canceling \( \det \W \ne 0 \) gives \( \det \Z = \lambda_0\lambda_1\lambda_2 \).

(c) Multiply out \( \lambda_1\lambda_2 = (a + b\omega + c\omega^2)(a + b\omega^2 + c\omega) \). The nine terms are \( a^2 \), \( ab\omega^2 + ab\omega \), \( ac\omega + ac\omega^2 \), \( b^2\omega^3 \), \( bc\omega^2 \), \( bc\omega^4 = bc\omega \), \( c^2\omega^3 \). Using \( \omega^3 = 1 \) and \( \omega + \omega^2 = -1 \),
\[
\lambda_1\lambda_2 = a^2 + b^2 + c^2 - ab - ac - bc .
\]
Then \( \det \Z = (a + b + c)(a^2 + b^2 + c^2 - ab - ac - bc) = a^3 + b^3 + c^3 - 3abc \), expanding and canceling. The Leibniz formula for \( \Z \) gives the three even terms \( a \cdot a \cdot a \), \( c \cdot c \cdot c \) (from \( \sigma = (1\ 2\ 3) \)) and \( b \cdot b \cdot b \), and the three odd terms, each equal to \( abc \) with sign \( - \): the same answer.
:::

:::: {#exr-special-determinants-c3}
[C3: Rank-one updates of an invertible matrix]

Let \( \A \in M_n(F) \) be invertible and \( \u, \v \in F^n \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \det(\A + \u\v\tp) = \det \A\,\big(1 + \v\tp \A^{-1}\u\big) \).
2. Deduce that \( \A + \u\v\tp \) is invertible if and only if \( \v\tp \A^{-1}\u \ne -1 \).
3. Give an example over \( \nQ \) with \( n = 2 \) where \( \A \) is invertible, \( \u\v\tp \ne 0 \), and \( \A + \u\v\tp \) is **not** invertible.
:::
::::

::: {.solution}
(a) Since \( \A \) is invertible, \( \A + \u\v\tp = \A(\I_n + \A^{-1}\u\v\tp) = \A\big(\I_n + (\A^{-1}\u)\v\tp\big) \) by @thm-matrix-multiplication-properties. By @thm-det-multiplicative and @thm-matrix-determinant-lemma applied to the vectors \( \A^{-1}\u \) and \( \v \), \( \det(\A + \u\v\tp) = \det \A\,(1 + \v\tp \A^{-1}\u) \).

(b) \( \det \A \ne 0 \) by @thm-det-nonzero-iff-invertible, so \( \det(\A + \u\v\tp) \ne 0 \) exactly when \( 1 + \v\tp \A^{-1}\u \ne 0 \). Apply @thm-det-nonzero-iff-invertible again.

(c) Take \( \A = \I_2 \), \( \u = (-1, 0) \), \( \v = (1, 0) \). Then \( \v\tp\u = -1 \), and indeed \( \A + \u\v\tp = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} \) is not invertible.
:::
