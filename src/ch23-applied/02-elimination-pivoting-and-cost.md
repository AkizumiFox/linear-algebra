# Elimination, Pivoting and Cost

Chapter 2 solved \( \A\x = \b \) by elimination and packaged the work as \( \A = \L\U \) or \( \P\A = \L\U \). It said nothing about how much arithmetic that costs, and almost nothing about what rounding does to it — only a remark, about a two-by-two matrix with a tiny corner entry, ending: "Chapter 23 makes this precise." Chapter 7 left a second note: "Chapter 23 reads Gaussian elimination itself as a sequence of Schur complements of \( 1 \times 1 \) pivots." Chapter 12 left a third, that Cholesky "does about half the arithmetic of a general LU factorization" and needs no pivoting.

This section pays all three. Section 1 supplied the model and the word *backward stable*; here that word is applied to the oldest algorithm in the book. Throughout, matrices are **real**, since the representable numbers of @def-floating-point-model are real, and \( \lvert\M\rvert \) denotes the entrywise absolute value \( (\lvert m_{ij}\rvert) \), with \( \lvert\M\rvert \le \lvert\N\rvert \) read entrywise.

## Elimination is a sequence of Schur complements

Chapter 7 built a machine for one block elimination: if \( \M = \begin{psmallmatrix}\A & \B\\ \C & \D\end{psmallmatrix} \) with \( \A \) invertible, then subtracting \( \C\A^{-1} \) times the first block row from the second leaves \( \begin{psmallmatrix}\A & \B\\ \0 & \M/\A\end{psmallmatrix} \), where \( \M/\A = \D - \C\A^{-1}\B \) is the Schur complement (@def-schur-complement, @thm-block-ldu). Gaussian elimination is that machine run with a \( 1 \times 1 \) block, \( n - 1 \) times. Saying so exactly is the cleanest description of the algorithm there is, and it is what makes block versions of it possible.

::: {#thm-elimination-is-schur-complements}
[Elimination Produces Schur Complements]

Let \( \A \in M_n(F) \) and \( 1 \le k \le n - 1 \), and suppose the first \( k \) steps of elimination without row swaps (Chapter 2 §06) are carried out with **non-zero pivots**, producing \( \A^{(k)} \). Partition
\[
\A = \begin{pmatrix} \A_k & \B \\ \C & \D\end{pmatrix},
\qquad
\A^{(k)} = \begin{pmatrix} \V & \B' \\ \0 & \S\end{pmatrix},
\]
with \( \A_k, \V \in M_k(F) \), the zero block being what the first \( k \) steps created. Then \( \A_k \) is invertible and
\[
\S = \A/\A_k = \D - \C\,\A_k^{-1}\B .
\]
In particular, for \( k = 1 \) and \( a_{11} \ne 0 \), one step of elimination replaces the trailing \( (n-1) \times (n-1) \) block by the Schur complement of the \( 1 \times 1 \) pivot block.
:::

::: {.idea}
The first \( k \) steps multiply \( \A \) on the left by a unit lower triangular matrix whose columns \( k+1, \dots, n \) are those of the identity — that is exactly what @lem-elimination-matrices (c) says, and it is the whole point. Such a matrix has block form \( \begin{psmallmatrix}\L_{11} & \0\\ \L_{21} & \I\end{psmallmatrix} \). Multiply that by the partitioned \( \A^{(k)} \), match the four blocks against \( \A \), and the \( \L_{11} \) cancels out of the bottom-right block, leaving the Schur complement.
:::

::: {.proof}
Write \( \boldsymbol{\ell}_j \) for the \( j \)-th multiplier vector, whose first \( j \) entries are zero, and recall from Chapter 2 §06 that step \( j \) multiplies on the left by \( \G_j(-\boldsymbol{\ell}_j) \), with inverse \( \G_j(\boldsymbol{\ell}_j) \) by @lem-elimination-matrices (b). Hence \( \A = \L_k\A^{(k)} \) where, by @lem-elimination-matrices (c),
\[
\L_k = \G_1(\boldsymbol{\ell}_1)\cdots\G_k(\boldsymbol{\ell}_k) = \I + \sum_{j=1}^{k}\boldsymbol{\ell}_j\e_j\tp .
\]
Only columns \( 1, \dots, k \) of \( \L_k \) differ from those of \( \I \), so partitioning \( \L_k \) as \( \A \) is partitioned gives
\[
\L_k = \begin{pmatrix} \L_{11} & \0 \\ \L_{21} & \I_{n-k}\end{pmatrix},
\]
with \( \L_{11} \in M_k(F) \) unit lower triangular, hence invertible by @lem-unit-lower-triangular-closed (b).

By @thm-block-multiplication,
\[
\begin{pmatrix} \A_k & \B \\ \C & \D\end{pmatrix}
= \begin{pmatrix} \L_{11} & \0 \\ \L_{21} & \I\end{pmatrix}
  \begin{pmatrix} \V & \B' \\ \0 & \S\end{pmatrix}
= \begin{pmatrix} \L_{11}\V & \L_{11}\B' \\ \L_{21}\V & \L_{21}\B' + \S\end{pmatrix} .
\]
Comparing blocks: \( \A_k = \L_{11}\V \), \( \B = \L_{11}\B' \), \( \C = \L_{21}\V \) and \( \D = \L_{21}\B' + \S \).

Now \( \V \) is upper triangular with the first \( k \) pivots on its diagonal, and those are non-zero by hypothesis, so \( \V \) is invertible by @lem-triangular-invertible. Therefore \( \A_k = \L_{11}\V \) is invertible, and \( \A_k^{-1} = \V^{-1}\L_{11}^{-1} \). Hence
\[
\C\,\A_k^{-1}\B = (\L_{21}\V)(\V^{-1}\L_{11}^{-1})(\L_{11}\B') = \L_{21}\B' ,
\]
and so \( \S = \D - \L_{21}\B' = \D - \C\A_k^{-1}\B = \A/\A_k \). This proves the theorem.
:::

::: {#exm-schur-complement-by-elimination}
[Two steps, two Schur complements]

Let
\[
\A = \begin{pmatrix} 1 & 2 & 3\\ 2 & 7 & 5\\ -1 & 4 & 8\end{pmatrix} .
\]
Carry out two steps of elimination without row swaps, then compute \( \A/\A_1 \) and \( \A/\A_2 \) directly from @def-schur-complement, and check @thm-elimination-is-schur-complements in both cases.
:::

::: {.solution}
*The elimination.* The first multipliers are \( \ell_{21} = 2/1 = 2 \) and \( \ell_{31} = -1/1 = -1 \); subtracting \( \ell_{i1} \) times row \( 1 \) from row \( i \) gives \( \A^{(1)} \). The second multiplier is \( \ell_{32} = 6/3 = 2 \), and row \( 3 \) becomes \( (0, 0, 11 - 2(-1)) = (0,0,13) \):
\[
\A^{(1)} = \begin{pmatrix} 1 & 2 & 3\\ 0 & 3 & -1\\ 0 & 6 & 11\end{pmatrix},
\qquad
\A^{(2)} = \begin{pmatrix} 1 & 2 & 3\\ 0 & 3 & -1\\ 0 & 0 & 13\end{pmatrix} .
\]

*The Schur complement of the \( 1 \times 1 \) block.* Here \( \A_1 = (1) \), \( \B = \begin{pmatrix}2 & 3\end{pmatrix} \), \( \C = \begin{pmatrix}2 & -1\end{pmatrix}\tp \) and \( \D = \begin{psmallmatrix}7&5\\4&8\end{psmallmatrix} \), so
\[
\begin{aligned}
\A/\A_1
&= \D - \C\A_1^{-1}\B
= \begin{pmatrix}7&5\\4&8\end{pmatrix} - \begin{pmatrix}2\\-1\end{pmatrix}\begin{pmatrix}2&3\end{pmatrix}\\
&= \begin{pmatrix}7&5\\4&8\end{pmatrix} - \begin{pmatrix}4&6\\-2&-3\end{pmatrix}
= \begin{pmatrix}3&-1\\6&11\end{pmatrix} ,
\end{aligned}
\]
which is exactly the trailing block of \( \A^{(1)} \).

*The Schur complement of the \( 2 \times 2 \) block.* Now \( \A_2 = \begin{psmallmatrix}1&2\\2&7\end{psmallmatrix} \), with \( \det\A_2 = 3 \) and \( \A_2^{-1} = \tfrac13\begin{psmallmatrix}7&-2\\-2&1\end{psmallmatrix} \), while \( \C = \begin{pmatrix}-1 & 4\end{pmatrix} \) and \( \B = \begin{pmatrix}3 & 5\end{pmatrix}\tp \). Then
\[
\begin{aligned}
\C\A_2^{-1} &= \tfrac13\begin{pmatrix}-15 & 6\end{pmatrix} = \begin{pmatrix}-5 & 2\end{pmatrix},\\
\A/\A_2 &= 8 - \begin{pmatrix}-5 & 2\end{pmatrix}\begin{pmatrix}3\\5\end{pmatrix} = 8 - (-5) = 13 ,
\end{aligned}
\]
the trailing \( 1 \times 1 \) block of \( \A^{(2)} \). Both readings agree with @thm-elimination-is-schur-complements, and as an arithmetic check the pivots \( 1, 3, 13 \) multiply to \( 39 \), which is \( \det\A \) — the corollary below says why that is no coincidence.
:::

Two consequences come out for free. The first identifies the pivots with ratios of minors, which is how Chapter 12 §01 wrote them in Sylvester's criterion.

::: {#cor-pivots-and-minors}
[Pivots Are Ratios of Leading Minors]

Let \( \A \in M_n(F) \), let \( 1 \le k \le n-1 \), and write \( \A_j \) for the leading principal \( j \times j \) submatrix of \( \A \), with \( \det\A_0 \coloneqq 1 \).

::: {.enumerate options="label=(\alph*)"}
1. If the first \( k \) pivots of elimination without row swaps are non-zero, then \( \A_1, \dots, \A_k \) are invertible and the \( j \)-th pivot equals \( \det\A_j/\det\A_{j-1} \) for \( j \le k \).
2. Conversely, if \( \A_1, \dots, \A_{n-1} \) are invertible then elimination without row swaps succeeds on \( \A \) with non-zero pivots, and \( \A = \L\U \) by @thm-lu-exists-without-swaps.
:::
:::

::: {.proof}
(a) Invertibility of \( \A_1, \dots, \A_k \) is @thm-elimination-is-schur-complements applied with \( 1, \dots, k \) in place of \( k \). For \( j = 1 \) the pivot is \( a_{11} = \det\A_1/\det\A_0 \), as claimed. For \( 2 \le j \le k \), the \( j \)-th pivot is the \( (j,j) \) entry of \( \A^{(j-1)} \), which by the theorem (with \( j - 1 \) in place of \( k \)) is the \( (1,1) \) entry of \( \A/\A_{j-1} \). That entry is \( a_{jj} \) minus row \( j \) of \( \C \) times \( \A_{j-1}^{-1} \) times column \( j \) of \( \B \), so it involves only rows and columns \( 1, \dots, j \) of \( \A \): it equals the \( 1 \times 1 \) matrix \( \A_j/\A_{j-1} \). By @thm-schur-determinant (a), \( \det\A_j = \det\A_{j-1}\cdot\det(\A_j/\A_{j-1}) \), which is the claim.

(b) We show by induction on \( j \) that the \( j \)-th pivot is non-zero, for \( j = 1, \dots, n-1 \). For \( j = 1 \) the pivot is \( a_{11} = \det\A_1 \ne 0 \). Let \( 2 \le j \le n-1 \) and suppose the first \( j-1 \) pivots are non-zero. Then @thm-elimination-is-schur-complements applies with \( j - 1 \) in place of \( k \), and the calculation in (a) identifies the \( j \)-th pivot as \( \det\A_j/\det\A_{j-1} \), which is non-zero because \( \A_j \) and \( \A_{j-1} \) are invertible (@thm-det-nonzero-iff-invertible). So elimination never stops, and @thm-lu-exists-without-swaps gives \( \A = \L\U \).
:::

::: {.check}
The matrix \( \begin{psmallmatrix}0 & 1\\ 1 & 0\end{psmallmatrix} \) has no LU factorization (@exm-no-lu-factorization). Which hypothesis of @cor-pivots-and-minors (b) fails, and what does @thm-elimination-is-schur-complements say about it?
:::

::: {.solution}
\( \A_1 = (0) \) is not invertible, so (b) does not apply. @thm-elimination-is-schur-complements does not apply either: it assumes the first pivot is non-zero, and here it is \( 0 \), so the Schur complement \( \A/\A_1 \) is not even defined — @def-schur-complement requires the pivot block to be invertible. This is the whole content of Chapter 2's "elimination stops": there is no Schur complement to form.
:::

## What elimination costs

A **flop** is one arithmetic operation: one addition, subtraction, multiplication or division, or one square root. Counting flops is crude — it ignores which operations are slow and how data moves — but it captures how the work grows with \( n \). We quote leading terms, writing \( \tfrac23 n^3 + O(n^2) \) and meaning it. **The constant matters and the exponent matters more**: halving the constant is worth having, but a smaller exponent overtakes it at some size and stays ahead forever.

::: {#prp-lu-cost}
[The Cost of Elimination]

Counting each of the five operations as one flop, and counting only arithmetic on matrix and vector entries:

::: {.enumerate options="label=(\alph*)"}
1. Elimination without row swaps on \( \A \in M_n(\nR) \) costs
   \[
   \frac{n(n-1)(4n+1)}{6} = \tfrac23 n^3 - \tfrac12 n^2 - \tfrac16 n
   \]
   flops, that is \( \tfrac23 n^3 + O(n^2) \).
2. Forward substitution with a unit lower triangular \( \L \) costs \( n^2 - n \) flops and back substitution with an upper triangular \( \U \) costs \( n^2 \), so solving \( \A\x = \b \) from a factorization costs \( 2n^2 - n \) flops.
3. The Cholesky recursion of Chapter 12 §02 on a positive definite \( \A \in M_n(\nR) \) costs
   \[
   \frac{n(n+1)(2n+1)}{6} = \tfrac13 n^3 + \tfrac12 n^2 + \tfrac16 n
   \]
   flops, that is \( \tfrac13 n^3 + O(n^2) \), of which \( n \) are square roots.
:::
:::

::: {.proof}
(a) At step \( k \) the algorithm computes \( n - k \) multipliers, one division each, and then replaces each of the \( (n-k)^2 \) entries of the trailing block by \( a_{ij} - \ell_{ik}a_{kj} \), two flops each. The entries below the pivot are set to zero without arithmetic. So the cost is
\[
\sum_{k=1}^{n-1}\Bigl[(n-k) + 2(n-k)^2\Bigr]
= \sum_{j=1}^{n-1}\bigl(j + 2j^2\bigr)
= \frac{(n-1)n}{2} + \frac{(n-1)n(2n-1)}{3} ,
\]
using \( \sum_{j\le m} j = m(m+1)/2 \) and \( \sum_{j \le m}j^2 = m(m+1)(2m+1)/6 \) with \( m = n-1 \). Putting the two terms over \( 6 \) gives \( n(n-1)\bigl(3 + 2(2n-1)\bigr)/6 = n(n-1)(4n+1)/6 \).

(b) Forward substitution computes \( x_i = b_i - \sum_{j<i}\ell_{ij}x_j \) with no division, since \( \ell_{ii} = 1 \): that is \( 2(i-1) \) flops, and \( \sum_{i\le n}2(i-1) = n(n-1) \). Back substitution computes \( x_i = \bigl(b_i - \sum_{j>i}u_{ij}x_j\bigr)/u_{ii} \), which is \( 2(n-i) + 1 \) flops, and \( \sum_{i \le n}\bigl(2(n-i)+1\bigr) = n(n-1) + n = n^2 \).

(c) Column \( j \) of the recursion computes \( \ell_{jj} = \bigl(a_{jj} - \sum_{k<j}\ell_{jk}^2\bigr)^{1/2} \), costing \( 2(j-1) \) flops for the sum and one square root, and then \( \ell_{ij} = \bigl(a_{ij} - \sum_{k<j}\ell_{ik}\ell_{jk}\bigr)/\ell_{jj} \) for each of the \( n - j \) rows below, costing \( 2(j-1) + 1 \) flops each. The total is
\[
\begin{aligned}
\sum_{j=1}^{n}(n - j + 1)\bigl(2j - 1\bigr)
&= \sum_{i=1}^{n} i\,(2n - 2i + 1)\\
&= (2n+1)\frac{n(n+1)}{2} - 2\cdot\frac{n(n+1)(2n+1)}{6} ,
\end{aligned}
\]
substituting \( i = n - j + 1 \); the two terms combine to \( n(n+1)(2n+1)\bigl(\tfrac12 - \tfrac13\bigr) = n(n+1)(2n+1)/6 \).
:::

Comparing (a) and (c): \( \tfrac13 n^3 \) against \( \tfrac23 n^3 \). This is Chapter 12 §02's "Cholesky does about half the arithmetic of a general LU factorization", now a count rather than a claim, for the reason that section gave — the recursion produces one triangular factor instead of two. Part (b) says the factorization is the expensive part: solving \( m \) systems with the same \( \A \) costs \( \tfrac23n^3 + 2mn^2 \), not \( m \) times \( \tfrac23 n^3 \).

## One row at a time

Every algorithm below computes its entries the same way: accumulate a sum of products into a running total, then possibly divide. Analyzing that pattern once saves doing it three times.

::: {#lem-substitution-row}
[One Row of Substitution]

Let \( m \ge 0 \), let \( t_1, \dots, t_m \), \( y_1, \dots, y_m \), \( c \) and \( d \ne 0 \) be representable, and suppose
\[
s_0 = c,
\qquad
s_p = \fl\bigl(s_{p-1} - \fl(t_py_p)\bigr) \quad (p = 1, \dots, m),
\qquad
z = \fl(s_m/d)
\]
are computed in the model of @def-floating-point-model, with \( (m+1)u < 1 \). Then there are \( \theta_0, \dots, \theta_m \) with
\[
c = d\,z\,(1 + \theta_0) + \sum_{p=1}^{m} t_py_p(1 + \theta_p),
\qquad
\lvert\theta_p\rvert \le \gamma_{m+1} \ \text{ for all } p .
\]
If the final division is omitted, so that \( z = s_m \), the same identity holds with \( d = 1 \) and \( \lvert\theta_p\rvert \le \gamma_m \).
:::

::: {.idea}
Unroll the recursion, then divide the whole identity by the product of the accumulation factors. Dividing is the trick: it moves those factors onto \( c \)'s neighbors as **inverse** factors, which is exactly what @lem-gamma-bound was stated to allow.
:::

::: {.proof}
By (FP2) there are \( \delta_p, \varepsilon_p, \eta \), all of modulus at most \( u \), with \( \fl(t_py_p) = t_py_p(1+\delta_p) \), \( s_p = \bigl(s_{p-1} - t_py_p(1+\delta_p)\bigr)(1+\varepsilon_p) \), and \( z = (s_m/d)(1+\eta) \). Induction on \( m \) gives
\[
s_m = c\prod_{p=1}^{m}(1+\varepsilon_p) - \sum_{p=1}^{m}t_py_p(1+\delta_p)\prod_{q=p}^{m}(1+\varepsilon_q) ,
\]
the case \( m = 0 \) being \( s_0 = c \), and the step from \( m-1 \) to \( m \) multiplying everything by \( 1 + \varepsilon_m \) and subtracting the new term.

Each \( 1 + \varepsilon_p \) is non-zero, since \( \lvert\varepsilon_p\rvert \le u < 1 \), so we may divide the identity by \( \prod_{p \le m}(1+\varepsilon_p) \) and rearrange:
\[
c = s_m\prod_{p=1}^{m}(1+\varepsilon_p)^{-1} + \sum_{p=1}^{m}t_py_p(1+\delta_p)\prod_{q=1}^{p-1}(1+\varepsilon_q)^{-1} .
\]
From \( z = (s_m/d)(1+\eta) \) we get \( s_m = d\,z\,(1+\eta)^{-1} \). So the first term is \( d\,z \) times a product of \( m + 1 \) factors of the form \( (1+\delta)^{\pm1} \) with \( \lvert\delta\rvert \le u \), which by @lem-gamma-bound is \( 1 + \theta_0 \) with \( \lvert\theta_0\rvert \le \gamma_{m+1} \). The \( p \)-th term of the sum carries \( 1 + (p-1) = p \le m \) such factors, so it is \( t_py_p(1+\theta_p) \) with \( \lvert\theta_p\rvert \le \gamma_p \le \gamma_{m+1} \).

If the division is omitted, the first term carries only the \( m \) inverse factors, so \( \lvert\theta_0\rvert \le \gamma_m \), and the rest of the argument is unchanged. This proves the lemma.
:::

## Solving a triangular system

Here is the cleanest backward error analysis in the subject, and the model for every other one in this chapter. Note in advance what it does **not** assume: nothing about the size of the diagonal entries of \( \T \), nothing about its conditioning, and no pivoting of any kind.

::: {#thm-triangular-solve-backward-error}
[Backward Error of a Triangular Solve]

Let \( \T \in M_n(\nR) \) be lower triangular with representable entries and non-zero diagonal, let \( \b \in \nR^n \) be representable, and let \( nu < 1 \). Let \( \widehat\x \) be computed by forward substitution in the model: for each \( i \), the products \( t_{ij}\widehat x_j \) are subtracted from \( b_i \) one at a time in increasing order of \( j \), and the result is divided by \( t_{ii} \) — that is, exactly the computation of @lem-substitution-row with \( m = i-1 \). Then there is a lower triangular \( \Delta\T \) with
\[
(\T + \Delta\T)\widehat\x = \b
\qquad\text{and}\qquad
\lvert\Delta t_{ij}\rvert \le \gamma_i\,\lvert t_{ij}\rvert \le \gamma_n\,\lvert t_{ij}\rvert
\quad (j \le i) .
\]
The same statement, with \( \gamma_{n+1-i} \) in place of \( \gamma_i \), holds for back substitution with an upper triangular \( \T \).
:::

::: {.idea}
Row \( i \) *is* the pattern of @lem-substitution-row, with \( c = b_i \), the \( m = i-1 \) products \( t_{ij}\widehat x_j \), and the final division by \( t_{ii} \). The lemma hands back an identity in which every coefficient of \( \widehat x_j \) is \( t_{ij} \) times something within \( \gamma_i \) of \( 1 \); that "something minus one", times \( t_{ij} \), is \( \Delta t_{ij} \).
:::

::: {.proof}
Fix \( i \). The quantities \( \widehat x_1, \dots, \widehat x_{i-1} \) are already computed, hence representable, so @lem-substitution-row applies with \( m = i - 1 \), \( c = b_i \), \( t_p = t_{ip} \), \( y_p = \widehat x_p \), \( d = t_{ii} \) and \( z = \widehat x_i \). Since \( m + 1 = i \le n \) and \( nu < 1 \), it gives \( \theta_0, \dots, \theta_{i-1} \) of modulus at most \( \gamma_i \) with
\[
b_i = t_{ii}\widehat x_i(1+\theta_0) + \sum_{j<i} t_{ij}\widehat x_j(1+\theta_j) .
\]
Define \( \Delta t_{ii} = t_{ii}\theta_0 \), \( \Delta t_{ij} = t_{ij}\theta_j \) for \( j < i \), and \( \Delta t_{ij} = 0 \) for \( j > i \). Then \( \Delta\T \) is lower triangular, \( \lvert\Delta t_{ij}\rvert \le \gamma_i\lvert t_{ij}\rvert \le \gamma_n\lvert t_{ij}\rvert \) since \( \gamma_i \le \gamma_n \), and the display says precisely that row \( i \) of \( (\T + \Delta\T)\widehat\x \) equals \( b_i \). As \( i \) was arbitrary, \( (\T+\Delta\T)\widehat\x = \b \).

For back substitution, row \( i \) has \( n - i \) products instead of \( i - 1 \), so the lemma applies with \( m = n - i \) and the bound is \( \gamma_{n+1-i} \). This proves the theorem.
:::

This is as strong as a backward error statement gets. The perturbation is bounded **entrywise**, and entrywise *relative to the entries of \( \T \) itself*: a zero entry of \( \T \) is not perturbed at all, and a tiny entry is perturbed only in its own last digits. So a triangular solve is backward stable in the sense of @def-backward-stable — with the constant \( c = 1.02\,n \) in any model with \( nu \le 0.01 \), since \( \gamma_n \le 1.02\,nu \) there — whatever \( \kappa(\T) \) may be.

::: {.warning}
**Backward stable is not accurate, and this theorem is where the point bites hardest.** @thm-triangular-solve-backward-error holds for every non-singular triangular \( \T \). It does not say \( \widehat\x \) is near \( \x \). By @thm-forward-from-backward the forward error can be about \( \kappa(\T)\gamma_n \), and triangular matrices can be spectacularly ill-conditioned. Take the \( n \times n \) matrix \( \T \) with \( 1 \) on the diagonal and \( -1 \) everywhere above it. Its row sums of moduli are \( n, n-1, \dots, 1 \), so \( \norm{\T}_{\infty} = n \). Its inverse has \( 1 \) on the diagonal and \( 2^{j-i-1} \) in position \( (i,j) \) for \( j > i \): back substitution on \( \T\x = \e_j \) gives \( x_j = 1 \) and \( x_i = \sum_{p > i} x_p \) for \( i < j \), and each partial sum of \( 1, 1, 2, 4, \dots \) is the next term. Hence \( \norm{\T^{-1}}_{\infty} = 1 + (1 + 2 + \dots + 2^{n-2}) = 2^{n-1} \) and \( \kappa_{\infty}(\T) = n2^{n-1} \), so for \( n = 60 \) a backward stable solve can still return nonsense. Stability is a promise about the *data*, and a promise about the data is worth only what the conditioning of the problem makes it worth.
:::

## The factorization itself

For the factorization we analyze the ordering that computes each entry of \( \L \) and \( \U \) by one accumulation. In exact arithmetic it produces the same factors as Chapter 2's row operations — for invertible \( \A \) this is @thm-lu-unique — but it groups the arithmetic differently, and rounding notices the difference.

::: {.algorithm}
**Elimination, one entry at a time.** Input: \( \A \in M_n(\nR) \). Set \( \ell_{ii} = 1 \). For \( i = 1, 2, \dots, n \):

- for \( j = i, \dots, n \), put \( u_{ij} = a_{ij} - \sum_{k<i}\ell_{ik}u_{kj} \);
- if \( u_{ii} = 0 \), stop; otherwise for \( r = i+1, \dots, n \), put \( \ell_{ri} = \bigl(a_{ri} - \sum_{k<i}\ell_{rk}u_{ki}\bigr)/u_{ii} \).
:::

::: {#thm-lu-backward-error}
[Backward Error of a Factorization]

Let \( \A \in M_n(\nR) \) have representable entries, let \( nu < 1 \), and suppose the algorithm above runs to completion in the model of @def-floating-point-model, producing \( \widehat\L \) and \( \widehat\U \). Then
\[
\widehat\L\widehat\U = \A + \Delta\A
\qquad\text{with}\qquad
\lvert\Delta\A\rvert \le \gamma_n\,\lvert\widehat\L\rvert\,\lvert\widehat\U\rvert
\]
entrywise.
:::

::: {.idea}
Each entry is one application of @lem-substitution-row: the entries of \( \U \) with no division, the entries of \( \L \) with one. In both cases the lemma returns \( a_{ij} \) as a sum of the products \( \widehat\ell_{ip}\widehat u_{pj} \), each with its own factor \( 1 + \theta_p \). Collecting the terms is exactly forming the \( (i,j) \) entry of \( \widehat\L\widehat\U \), and the \( \theta_p \) are what is left over.
:::

::: {.proof}
*Case \( i \le j \).* The computation of \( \widehat u_{ij} \) is @lem-substitution-row with \( m = i - 1 \), \( c = a_{ij} \), \( t_p = \widehat\ell_{ip} \), \( y_p = \widehat u_{pj} \), no division and \( z = \widehat u_{ij} \). Writing \( \theta_i \) for the \( \theta_0 \) of the lemma, and using \( \widehat\ell_{ii} = 1 \),
\[
a_{ij} = \sum_{p=1}^{i}\widehat\ell_{ip}\widehat u_{pj}(1 + \theta_p),
\qquad
\lvert\theta_p\rvert \le \gamma_{i-1} .
\]
(For \( i = 1 \) the sum has one term and \( \theta_1 = 0 \).) Since \( \widehat\ell_{ip} = 0 \) for \( p > i \), the sum without the \( \theta_p \) is \( (\widehat\L\widehat\U)_{ij} \). Hence
\[
\bigl\lvert a_{ij} - (\widehat\L\widehat\U)_{ij}\bigr\rvert
= \Bigl\lvert\sum_{p\le i}\widehat\ell_{ip}\widehat u_{pj}\theta_p\Bigr\rvert
\le \gamma_{i-1}\sum_{p\le i}\lvert\widehat\ell_{ip}\rvert\lvert\widehat u_{pj}\rvert
= \gamma_{i-1}\bigl(\lvert\widehat\L\rvert\lvert\widehat\U\rvert\bigr)_{ij} ,
\]
the last equality again because \( \widehat\ell_{ip} = 0 \) for \( p > i \).

*Case \( i > j \).* The computation of \( \widehat\ell_{ij} \) is @lem-substitution-row with \( m = j-1 \), \( c = a_{ij} \), \( t_p = \widehat\ell_{ip} \), \( y_p = \widehat u_{pj} \), \( d = \widehat u_{jj} \) and \( z = \widehat\ell_{ij} \). Writing \( \theta_j \) for \( \theta_0 \),
\[
a_{ij} = \sum_{p=1}^{j}\widehat\ell_{ip}\widehat u_{pj}(1 + \theta_p),
\qquad
\lvert\theta_p\rvert \le \gamma_{j} .
\]
Since \( \widehat u_{pj} = 0 \) for \( p > j \), the sum without the \( \theta_p \) is again \( (\widehat\L\widehat\U)_{ij} \), and the same estimate gives \( \lvert a_{ij} - (\widehat\L\widehat\U)_{ij}\rvert \le \gamma_j(\lvert\widehat\L\rvert\lvert\widehat\U\rvert)_{ij} \).

In both cases the constant is at most \( \gamma_n \). This proves the theorem.
:::

::: {.remark}
**What is proved and what is not.** The theorem is about the ordering displayed above. Chapter 2's ordering, which updates the whole trailing block at each step, satisfies the same bound \( \lvert\Delta\A\rvert \le \gamma_n\lvert\widehat\L\rvert\lvert\widehat\U\rvert \); the proof is a different induction of comparable length, and **we do not give it here**. Nothing later in this chapter uses it. Also, the theorem assumes the algorithm completes, which in the model means every computed \( \widehat u_{ii} \) is non-zero; it says nothing about what happens when one of them is zero, or about the case where a pivot is non-zero only by a rounding accident. One more seam will appear below: the growth bound for partial pivoting, proved in the next subsection, concerns the **exact** elimination in Chapter 2's ordering, whereas the bound just proved concerns the factors this ordering computes in the model. In exact arithmetic, and for invertible \( \A \), the two orderings produce the same \( \L \) and \( \U \), by @thm-lu-unique; in the model they agree only to within rounding, and we do not quantify that here. Nothing below is allowed to cross that seam quietly. @eq-lu-growth-bound, proved next, measures growth in the **computed** factors, which is a quantity one can read off after the fact; the a priori bound \( 2^{n-1} \) of @thm-growth-partial-pivoting is a statement about exact elimination. The three places that put the two together — the warning after @exm-growth-attained and the solutions to A1 and B3 — say that they are doing so, and each of them uses the combination only to show that even its most favorable reading proves nothing.
:::

The bound is useless until we know how big \( \lvert\widehat\L\rvert\lvert\widehat\U\rvert \) is, and *that* is not controlled by \( \A \). It is controlled by what the algorithm does to \( \A \), which is why elimination needs a pivoting rule at all. The quantity to watch has a name.

::: {#def-growth-factor}
[Growth factor]

Let elimination — with whatever pivoting rule is in force — be run on \( \A \in M_n(\nR) \), producing an upper factor \( \U \). The **growth factor** of that run is
\[
g_n \coloneqq
\frac{\max_{i,j}\lvert u_{ij}\rvert}{\max_{i,j}\lvert a_{ij}\rvert} ,
\]
the largest entry in modulus the algorithm produces, relative to the largest entry in modulus it was given. For a run in the model, \( \U \) means the computed \( \widehat\U \).
:::

::: {.remark}
The classical definition takes the maximum over **every** intermediate matrix \( \A^{(0)} = \A, \A^{(1)}, \dots, \A^{(n-1)} = \U \) of the row-operation ordering, not only over \( \U \). That quantity is at least \( g_n \), so any upper bound proved for it bounds \( g_n \) too, and it is what the growth theorem of the next subsection actually estimates. The ratio above is the form the backward error bound needs.
:::

Suppose a pivoting rule keeps every multiplier at most \( 1 \) in modulus — the next subsection exhibits one, for the algorithm above as well as for Chapter 2's ordering. Then \( \lvert\widehat\ell_{ip}\rvert \le 1 \), so for all \( i, j \)
\[
\bigl(\lvert\widehat\L\rvert\lvert\widehat\U\rvert\bigr)_{ij}
\le \sum_{p}\lvert\widehat u_{pj}\rvert
\le n\max_{p,q}\lvert\widehat u_{pq}\rvert
= n\,g_n\max_{p,q}\lvert a_{pq}\rvert ,
\]
and @thm-lu-backward-error becomes
\[
\max_{i,j}\lvert\Delta a_{ij}\rvert \;\le\; n\,\gamma_n\,g_n\,\max_{i,j}\lvert a_{ij}\rvert .
\]{#eq-lu-growth-bound}
Since \( \gamma_n \) is about \( nu \), the relative backward error is about \( n^2g_nu \). The dimensional factor \( n^2 \) is pessimistic and nobody minds it. **Everything therefore depends on \( g_n \)** — and on nothing else.

## Pivoting

::: {#prp-partial-pivoting-bounds-multipliers}
[Partial Pivoting Bounds the Multipliers]

Run elimination with **partial pivoting**: at step \( k \), before eliminating, exchange row \( k \) with a row \( r \ge k \) for which \( \lvert a^{(k-1)}_{rk}\rvert \) is largest. Then every multiplier satisfies \( \lvert\ell_{ik}\rvert \le 1 \), in exact arithmetic; and in the model \( \lvert\widehat\ell_{ik}\rvert \le 1 \) as well.
:::

::: {.proof}
After the exchange, the pivot \( a^{(k-1)}_{kk} \) has the largest modulus in its column among rows \( k, \dots, n \). If it is zero then the whole column is zero, every multiplier is set to \( 0 \), and there is nothing to prove. Otherwise \( \lvert a^{(k-1)}_{ik}\rvert \le \lvert a^{(k-1)}_{kk}\rvert \) for \( i > k \), so \( \lvert\ell_{ik}\rvert = \lvert a^{(k-1)}_{ik}/a^{(k-1)}_{kk}\rvert \le 1 \).

In the model, \( \widehat\ell_{ik} = \fl(x) \) for a real \( x \) with \( \lvert x\rvert \le 1 \). Both \( 1 \) and \( -1 \) lie in \( \cR \), by @def-floating-point-model, and the one with the sign of \( x \) is at distance \( 1 - \lvert x\rvert \) from \( x \); since \( \fl(x) \) is a **nearest** element of \( \cR \), also \( \lvert\fl(x) - x\rvert \le 1 - \lvert x\rvert \). If \( \lvert\fl(x)\rvert \) were greater than \( 1 \) we would get \( \lvert\fl(x) - x\rvert \ge \lvert\fl(x)\rvert - \lvert x\rvert > 1 - \lvert x\rvert \), a contradiction. So \( \lvert\widehat\ell_{ik}\rvert \le 1 \).
:::

::: {.remark}
**The same rule, one entry at a time.** The proposition is stated for Chapter 2's ordering, which has the column entries \( a^{(k-1)}_{rk} \) in hand at step \( k \). In the entry-at-a-time algorithm those entries appear as the candidate numerators \( a_{ri} - \sum_{k<i}\widehat\ell_{rk}\widehat u_{ki} \) with \( r \ge i \), and partial pivoting there means: form all of them, exchange rows \( i \) and \( r \) so that the largest of them in modulus becomes \( \widehat u_{ii} \), and only **then** divide. The proof above applies word for word, with the candidate numerator in place of \( a^{(k-1)}_{rk} \) — it uses nothing about those numbers except that the divisor is the largest of them in modulus — so every multiplier of that ordering satisfies \( \lvert\widehat\ell_{ri}\rvert \le 1 \) too. That is what licenses the hypothesis under which @eq-lu-growth-bound was derived for the computed factors of @thm-lu-backward-error.
:::

::: {#thm-growth-partial-pivoting}
[Growth Under Partial Pivoting]

In exact arithmetic, elimination with partial pivoting on any \( \A \in M_n(\nR) \) has growth factor \( g_n \le 2^{n-1} \).
:::

::: {.idea}
One step replaces an entry by itself minus a multiple, of modulus at most \( 1 \), of another entry. Two numbers of modulus at most \( M \) cannot make more than \( 2M \). Repeat \( n-1 \) times.
:::

::: {.proof}
Write \( M_k = \max_{i,j}\lvert a^{(k)}_{ij}\rvert \), and let \( \B = (b_{ij}) \) be \( \A^{(k-1)} \) after the row exchange of step \( k \); an exchange only permutes entries, so \( \max_{i,j}\lvert b_{ij}\rvert = M_{k-1} \). Every entry of \( \A^{(k)} \) is either an entry of \( \B \) (the rows \( 1, \dots, k \) are left alone, and the entries below the pivot are set to \( 0 \)) or of the form
\[
a^{(k)}_{ij} = b_{ij} - \ell_{ik}b_{kj},
\qquad
\bigl\lvert a^{(k)}_{ij}\bigr\rvert \le \lvert b_{ij}\rvert + \lvert\ell_{ik}\rvert\lvert b_{kj}\rvert \le 2M_{k-1} ,
\]
using \( \lvert\ell_{ik}\rvert \le 1 \) from @prp-partial-pivoting-bounds-multipliers. Hence \( M_k \le 2M_{k-1} \) for every \( k \), and by induction \( M_k \le 2^kM_0 \). The intermediate matrices are \( \A^{(0)}, \dots, \A^{(n-1)} \), so
\[
\max_{i,j,k}\bigl\lvert a^{(k)}_{ij}\bigr\rvert = \max_{0 \le k \le n-1} M_k \le 2^{n-1}M_0 ,
\]
which is \( g_n \le 2^{n-1} \). This proves the theorem.
:::

::: {.remark}
One expects the same argument in the model to give \( M_k \le 2(1+u)^2M_{k-1} \), the subtraction and the multiplication each contributing a factor \( 1 + \delta \), and hence \( g_n \le \bigl(2(1+u)^2\bigr)^{n-1} \), which for any \( u \) worth using is \( 2^{n-1} \) in all but the last digits. **We have not written that induction out**, and nothing in this section cites it: @thm-growth-partial-pivoting, the exact-arithmetic statement, is the only growth bound we have, and the passages that carry it over to a computed factorization say that they are doing so.
:::

::: {.check}
Run elimination on \( \begin{psmallmatrix}1 & 2\\ 3 & 4\end{psmallmatrix} \) without row swaps, and again with partial pivoting, and compute \( g_2 \) each time. Does partial pivoting make the growth factor smaller?
:::

::: {.solution}
Without a swap the multiplier is \( 3 \) and \( u_{22} = 4 - 3\cdot2 = -2 \), so \( \U = \begin{psmallmatrix}1&2\\0&-2\end{psmallmatrix} \) and \( g_2 = 2/4 = \tfrac12 \). With partial pivoting the rows are exchanged, the multiplier is \( \tfrac13 \) and \( u_{22} = 2 - \tfrac13\cdot4 = \tfrac23 \), so \( \U = \begin{psmallmatrix}3&4\\0&2/3\end{psmallmatrix} \) and \( g_2 = 4/4 = 1 \). Pivoting made the growth factor *larger*, and \( g_n < 1 \) is perfectly possible. Partial pivoting does not minimize growth; it bounds the multipliers, and @thm-growth-partial-pivoting turns that into a worst-case bound — here \( 2^{1} = 2 \), which both runs respect.
:::

The bound \( 2^{n-1} \) is dreadful, and it is attained.

::: {#exm-growth-attained}
[A matrix that really grows]

Let \( \Y_n \in M_n(\nR) \) have \( 1 \) on the diagonal, \( -1 \) strictly below it, \( 0 \) strictly above it except in the last column, and \( 1 \) throughout the last column. For \( n = 4 \),
\[
\Y_4 = \begin{pmatrix}
1 & 0 & 0 & 1\\
-1 & 1 & 0 & 1\\
-1 & -1 & 1 & 1\\
-1 & -1 & -1 & 1
\end{pmatrix} .
\]
Run elimination with partial pivoting on \( \Y_4 \) and on \( \Y_5 \), and compute the growth factor of each.
:::

::: {.solution}
The runs below are in exact arithmetic, so the factors are \( \L \) and \( \U \), with no hats. Every entry of \( \Y_n \) has modulus \( 1 \), so \( g_n \) is simply the largest modulus of an entry of the resulting \( \U \).

*Step 1 on \( \Y_4 \).* Column \( 1 \) is \( (1, -1, -1, -1) \); all four entries have modulus \( 1 \), so the largest is already in place and no exchange is made. The multipliers are \( -1 \), so each lower row has row \( 1 \) **added** to it. Rows \( 2, 3, 4 \) become \( (0, 1, 0, 2) \), \( (0, -1, 1, 2) \), \( (0, -1, -1, 2) \): the last column has doubled.

*Step 2.* Column \( 2 \) below the diagonal is \( (-1, -1) \) against the pivot \( 1 \); again no exchange, multipliers \( -1 \). Rows \( 3, 4 \) become \( (0, 0, 1, 4) \) and \( (0, 0, -1, 4) \).

*Step 3.* Multiplier \( -1 \) again; row \( 4 \) becomes \( (0, 0, 0, 8) \). So
\[
\U = \begin{pmatrix}
1 & 0 & 0 & 1\\ 0 & 1 & 0 & 2\\ 0 & 0 & 1 & 4\\ 0 & 0 & 0 & 8
\end{pmatrix},
\qquad
g_4 = \frac{8}{1} = 8 = 2^{3} .
\]

*For \( n = 5 \)* the same three observations repeat once more: no exchange is ever made, every multiplier is \( -1 \), and the last column runs \( 1, 2, 4, 8, 16 \) down the diagonal of \( \U \), giving \( g_5 = 16 = 2^{4} \).

Every entry of \( \Y_n \) is \( \pm1 \), and partial pivoting does exactly what it is told; for these two sizes the bound of @thm-growth-partial-pivoting is attained, not approached. The same three observations run by induction for every \( n \), and @exr-elimination-pivoting-and-cost-c2 carries that induction out.
:::

::: {.warning}
**Partial pivoting is not proved stable by anything in this chapter.** @eq-lu-growth-bound bounds the backward error by \( n\gamma_ng_n\max_{i,j}\lvert a_{ij}\rvert \), where \( g_n \) is the growth in the **computed** factors, and the only bound we have on growth is @thm-growth-partial-pivoting's \( 2^{n-1} \), for the **exact** elimination; the remark after @thm-lu-backward-error records that gap and we have not closed it. Grant it anyway, and the resulting backward error bound is about \( n^22^{n-1}u \), which for \( n = 60 \) exceeds \( 1 \) and says nothing at all — so even the optimistic reading proves nothing. What is true in practice is that \( g_n \) is almost always a small multiple of \( 1 \) — but "almost always" is a statement about the matrices people meet, not a theorem, and @exm-growth-attained, with @exr-elimination-pivoting-and-cost-c2 for general \( n \), shows there is no theorem to be had. Partial pivoting is used because it is cheap and because its failures are rare and constructed, not because it is backward stable in the sense of @def-backward-stable. That is an honest summary of the state of the subject, and the reader should not accept a tidier one.
:::

## The example Chapter 2 promised

Chapter 2 §06 ended its discussion of pivoting with a two-by-two matrix and a promise: after describing how \( \begin{psmallmatrix}\varepsilon & 1\\ 1 & 1\end{psmallmatrix} \) makes elimination produce a computed \( \L\U \) whose \( (2,2) \) entry is \( 0 \) instead of \( 1 \), it wrote "Swapping the rows first gives the harmless multiplier \( \varepsilon \). Chapter 23 makes this precise." Here it is, made precise.

::: {#exm-epsilon-pivot}
[The tiny pivot, in the model]

Work in the six-digit decimal model of @exm-six-digit-model, where \( u = 5\times10^{-6} \), and take
\[
\A = \begin{pmatrix}\varepsilon & 1\\ 1 & 1\end{pmatrix},
\qquad
\b = \begin{pmatrix}1\\2\end{pmatrix},
\qquad
\varepsilon = 10^{-8} .
\]
Factor and solve without an exchange, then with one. In each case compute \( \widehat\L\widehat\U \) exactly and report the backward error.
:::

::: {.solution}
*The exact answer.* Subtracting the first equation's \( \varepsilon \)-multiple, \( (1-\varepsilon)x_1 = 1 \), so
\[
\x = \Bigl(\frac{1}{1-\varepsilon},\; \frac{1-2\varepsilon}{1-\varepsilon}\Bigr)
= (1.00000001\ldots,\; 0.99999999\ldots) .
\]
Also \( \kappa_{\infty}(\A) = 4/(1-\varepsilon) < 5 \), exactly as in Chapter 15 §08: the problem is well conditioned.

*Without the exchange.* The multiplier is \( \fl(1/\varepsilon) = 10^{8} \), and
\[
\widehat u_{22} = \fl\bigl(1 - \fl(10^{8}\cdot 1)\bigr) = \fl(1 - 10^{8}) = \fl(-99999999) = -10^{8} ,
\]
the last step by rounding to six digits. Forward substitution gives \( \widehat y_1 = 1 \) and \( \widehat y_2 = \fl(2 - 10^{8}) = -10^{8} \); back substitution gives \( \widehat x_2 = \fl(-10^8/-10^8) = 1 \) and then
\[
\widehat x_1 = \fl\bigl((1 - 1)/\varepsilon\bigr) = 0 .
\]
The computed answer is \( (0, 1) \) — Chapter 15 §08's \( (0,1) \), reproduced here in a model rather than by hand-waving about digits. Multiplying the computed factors *exactly*,
\[
\begin{aligned}
\widehat\L\widehat\U
&= \begin{pmatrix}1 & 0\\ 10^{8} & 1\end{pmatrix}\begin{pmatrix}10^{-8} & 1\\ 0 & -10^{8}\end{pmatrix}\\
&= \begin{pmatrix}10^{-8} & 1\\ 1 & 0\end{pmatrix}
= \A + \Delta\A,
\qquad
\Delta\A = \begin{pmatrix}0&0\\0&-1\end{pmatrix} .
\end{aligned}
\]
So \( \norm{\Delta\A}_{\infty}/\norm{\A}_{\infty} = \tfrac12 \). The backward error is not \( O(u) \); it is \( O(1) \). This factorization is **not** backward stable, and it is not even close.

*With the exchange.* Partial pivoting compares \( \lvert\varepsilon\rvert \) with \( 1 \) and swaps, so we factor \( \P\A = \begin{psmallmatrix}1&1\\ \varepsilon&1\end{psmallmatrix} \) with \( \P\b = (2,1) \). The multiplier is \( \fl(\varepsilon/1) = \varepsilon \), and \( \widehat u_{22} = \fl(1 - \fl(\varepsilon\cdot1)) = \fl(1 - 10^{-8}) = 1 \), since \( 1 - 10^{-8} \) lies between the representable neighbors \( 0.999999 \) and \( 1 \) and is far nearer the second. Forward substitution gives \( \widehat y_1 = 2 \) and \( \widehat y_2 = \fl(1 - \fl(2\varepsilon)) = \fl(1 - 2\times10^{-8}) = 1 \); back substitution gives \( \widehat x_2 = 1 \) and \( \widehat x_1 = \fl((2-1)/1) = 1 \). The computed answer is \( (1, 1) \), whose relative error against the exact \( \x \) is about \( 10^{-8} \), far *better* than \( u \). Multiplying the computed factors exactly,
\[
\begin{aligned}
\widehat\L\widehat\U
&= \begin{pmatrix}1&0\\ 10^{-8}&1\end{pmatrix}\begin{pmatrix}1&1\\0&1\end{pmatrix}\\
&= \begin{pmatrix}1&1\\ 10^{-8}& 1 + 10^{-8}\end{pmatrix}
= \P\A + \Delta\A,
\qquad
\Delta\A = \begin{pmatrix}0&0\\0&10^{-8}\end{pmatrix} ,
\end{aligned}
\]
so \( \norm{\Delta\A}_{\infty}/\norm{\A}_{\infty} = 5\times10^{-9} \), comfortably below \( u \). This factorization is backward stable.

*What the exchange achieved.* Exactly what @eq-lu-growth-bound predicts. Without it the growth factor is \( g_2 = 10^{8} \): an entry of modulus \( 10^{8} \) is created out of a matrix whose largest entry is \( 1 \), and creating it destroys the information in \( a_{22} = 1 \), which lies beneath its last digit. With the exchange, @prp-partial-pivoting-bounds-multipliers keeps the multiplier at \( \varepsilon \le 1 \), \( g_2 = 1 \), and nothing large is ever made. Note what was **not** the problem: \( \kappa_{\infty}(\A) < 5 \) throughout. Chapter 15 §08 said so: "Conditioning bounds what *any* method can promise; whether a given method keeps that promise is stability."
:::

## Cholesky needs no pivoting

For a positive definite matrix the whole difficulty disappears, and the reason is a one-line inequality about the entries of the factor. Chapter 12 §02 asserted it — "it needs no pivoting: the recursion above never divides by something that positive definiteness allows to be zero" — and left the arithmetic half here.

::: {#thm-cholesky-stability}
[Cholesky Does Not Grow]

Let \( \A \in M_n(\nR) \) be symmetric positive definite with representable entries, and let \( \L \) be its Cholesky factor, \( \A = \L\L\tp \) with \( \ell_{ii} > 0 \) (@thm-cholesky).

::: {.enumerate options="label=(\alph*)"}
1. \( \lvert\ell_{ij}\rvert \le \sqrt{a_{ii}} \) for all \( j \le i \), and
   \[
   \bigl(\lvert\L\rvert\lvert\L\tp\rvert\bigr)_{ik} \le \sqrt{a_{ii}a_{kk}} \le \max_{p,q}\lvert a_{pq}\rvert
   \qquad\text{for all } i, k .
   \]
2. Suppose \( (n+1)u < 1 \) and the recursion of Chapter 12 §02 runs to completion in the model, producing \( \widehat\L \). Then
   \[
   \widehat\L\widehat\L\tp = \A + \Delta\A,
   \qquad
   \lvert\Delta\A\rvert \le \gamma_{n+1}\,\lvert\widehat\L\rvert\,\lvert\widehat\L\tp\rvert .
   \]
3. If moreover \( \gamma_{n+1} < 1 \), then
   \[
   \max_{i,j}\lvert\Delta a_{ij}\rvert \le \frac{\gamma_{n+1}}{1 - \gamma_{n+1}}\,\max_{i,j}\lvert a_{ij}\rvert .
   \]
:::
:::

::: {.idea}
For (a): the rows of \( \L \) have known lengths, because \( (\L\L\tp)_{ii} = a_{ii} \) *is* the squared length of row \( i \). An entry is no longer than its row, and Cauchy–Schwarz compares two rows. For (b): each off-diagonal entry is @lem-substitution-row again, and the diagonal entry is the same lemma followed by a square root, which contributes two more factors. For (c): part (b) bounds the row lengths of \( \widehat\L \) in terms of \( \A \), and then (a)'s argument runs again on \( \widehat\L \).
:::

::: {.proof}
(a) Row \( i \) of \( \L \) has \( \sum_{p}\ell_{ip}^2 = (\L\L\tp)_{ii} = a_{ii} \), so every single term satisfies \( \ell_{ij}^2 \le a_{ii} \). By the Cauchy–Schwarz inequality (@thm-cauchy-schwarz) applied to the rows \( i \) and \( k \) of \( \lvert\L\rvert \),
\[
\bigl(\lvert\L\rvert\lvert\L\tp\rvert\bigr)_{ik}
= \sum_{p}\lvert\ell_{ip}\rvert\lvert\ell_{kp}\rvert
\le \Bigl(\sum_p \ell_{ip}^2\Bigr)^{1/2}\Bigl(\sum_p \ell_{kp}^2\Bigr)^{1/2}
= \sqrt{a_{ii}a_{kk}} .
\]
Finally \( \sqrt{a_{ii}a_{kk}} \le \max_p a_{pp} \), and \( \max_p a_{pp} = \max_{p,q}\lvert a_{pq}\rvert \): the diagonal entries are positive (take \( \x = \e_p \) in @def-positive-semidefinite), and \( \lvert a_{pq}\rvert = \lvert(\L\L\tp)_{pq}\rvert \le (\lvert\L\rvert\lvert\L\tp\rvert)_{pq} \le \sqrt{a_{pp}a_{qq}} \le \max_p a_{pp} \), the middle step by the display just proved.

(b) Fix \( i > j \). The computation \( \widehat\ell_{ij} = \fl\bigl((a_{ij} - \sum_{k<j}\widehat\ell_{ik}\widehat\ell_{jk})/\widehat\ell_{jj}\bigr) \) is @lem-substitution-row with \( m = j-1 \) and \( d = \widehat\ell_{jj} \), so, writing \( \theta_j \) for \( \theta_0 \),
\[
a_{ij} = \sum_{p=1}^{j}\widehat\ell_{ip}\widehat\ell_{jp}(1+\theta_p),
\qquad
\lvert\theta_p\rvert \le \gamma_j \le \gamma_{n+1} .
\]
Since \( \widehat\ell_{jp} = 0 \) for \( p > j \), the sum without the \( \theta_p \) is \( (\widehat\L\widehat\L\tp)_{ij} \), so
\[
\bigl\lvert a_{ij} - (\widehat\L\widehat\L\tp)_{ij}\bigr\rvert
\le \gamma_{n+1}\sum_{p \le j}\lvert\widehat\ell_{ip}\rvert\lvert\widehat\ell_{jp}\rvert
= \gamma_{n+1}\bigl(\lvert\widehat\L\rvert\lvert\widehat\L\tp\rvert\bigr)_{ij} .
\]

For \( i = j \), let \( \widehat s \) be the value accumulated before the square root, so \( \widehat\ell_{jj} = \fl(\sqrt{\widehat s}) = \sqrt{\widehat s}(1+\eta) \) with \( \lvert\eta\rvert \le u \), and \( \widehat s = \widehat\ell_{jj}^{\,2}(1+\eta)^{-2} \). By the **proof** of @lem-substitution-row with \( m = j - 1 \) and no division — we need not just the size of \( \theta_0' \) but its shape, and the proof produces \( 1 + \theta_0' \) as the product of the \( j-1 \) factors \( (1+\varepsilon_p)^{-1} \) —
\[
a_{jj} = \widehat s\,(1 + \theta_0') + \sum_{p<j}\widehat\ell_{jp}^{\,2}(1+\theta_p),
\qquad
\lvert\theta_0'\rvert, \lvert\theta_p\rvert \le \gamma_{j-1} .
\]
Substituting \( \widehat s \), the first term is \( \widehat\ell_{jj}^{\,2} \) times a product of \( (j-1) + 2 \le n+1 \) factors of the form \( (1+\delta)^{\pm1} \), which by @lem-gamma-bound is \( 1 + \theta_j \) with \( \lvert\theta_j\rvert \le \gamma_{n+1} \). So again \( a_{jj} = \sum_{p \le j}\widehat\ell_{jp}\widehat\ell_{jp}(1+\theta_p) \) with all \( \lvert\theta_p\rvert \le \gamma_{n+1} \), and the displayed estimate follows as before. Since \( \widehat\L \) is lower triangular, the entries with \( i < j \) are the transposes of these, and \( \Delta\A \) is symmetric.

(c) The diagonal case of (b) reads \( \lvert a_{ii} - (\widehat\L\widehat\L\tp)_{ii}\rvert \le \gamma_{n+1}(\widehat\L\widehat\L\tp)_{ii} \), because \( (\lvert\widehat\L\rvert\lvert\widehat\L\tp\rvert)_{ii} = \sum_p\widehat\ell_{ip}^{\,2} = (\widehat\L\widehat\L\tp)_{ii} \). Hence \( (\widehat\L\widehat\L\tp)_{ii}(1 - \gamma_{n+1}) \le a_{ii} \), that is
\[
\sum_p \widehat\ell_{ip}^{\,2} \le \frac{a_{ii}}{1 - \gamma_{n+1}} .
\]
Cauchy–Schwarz as in (a), now for \( \widehat\L \), gives \( (\lvert\widehat\L\rvert\lvert\widehat\L\tp\rvert)_{ik} \le \sqrt{a_{ii}a_{kk}}/(1-\gamma_{n+1}) \le \max_{p,q}\lvert a_{pq}\rvert/(1-\gamma_{n+1}) \). Substituting into (b) gives (c). This proves the theorem.
:::

Compare (c) with @eq-lu-growth-bound. For a general matrix the backward error carried the factor \( g_n \), which partial pivoting bounds only by \( 2^{n-1} \), sharply. Here the same quantity is bounded by the largest entry of \( \A \) itself, with **no growth factor and no pivoting**: the Cholesky recursion is unconditionally backward stable. The reason sits entirely in part (a) — the rows of the factor cannot be longer than the diagonal of \( \A \) allows — and that is a fact about positive definiteness, not about arithmetic. Chapter 12 §02 called positive definiteness "the one structural hypothesis under which elimination is unconditionally safe"; this is the proof.

::: {.warning}
**Part (a) bounds \( \lvert\ell_{ij}\rvert \) by \( \sqrt{a_{ii}} \), the diagonal entry of its own row, not of its column.** The column version is false. For
\[
\A = \begin{pmatrix} 0.01 & 0.09 \\ 0.09 & 100\end{pmatrix},
\]
which is positive definite since \( 0.01 > 0 \) and \( \det\A = 1 - 0.0081 > 0 \) (@thm-pd-characterizations (d)), the factor is \( \ell_{11} = 0.1 \), \( \ell_{21} = 0.9 \), and \( \lvert\ell_{21}\rvert = 0.9 \) is nine times \( \sqrt{a_{11}} = 0.1 \). It is at most \( \sqrt{a_{22}} = 10 \), as (a) requires. An entry of \( \L \) can be far larger than the pivot it was divided by; what it cannot exceed is the size of its own row.
:::

## Exercises

### A. Check your understanding

:::: {#exr-elimination-pivoting-and-cost-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define a flop and the growth factor \( g_n \).
2. State the partial pivoting rule, and say what @prp-partial-pivoting-bounds-multipliers gets from it.
3. State the leading term of the flop count for an LU factorization, for two triangular solves and for Cholesky.
4. Decide whether each statement is correct, with a reason: (i) "a triangular solve needs pivoting when the diagonal entries are small"; (ii) "elimination with partial pivoting is backward stable"; (iii) "a backward stable factorization gives an accurate solution".
5. In one sentence, what does @thm-elimination-is-schur-complements say about the trailing block after \( k \) steps?
:::
::::

::: {.solution}
(a) A flop is one arithmetic operation — an addition, subtraction, multiplication, division or square root. The growth factor is \( g_n = \max_{i,j}\lvert u_{ij}\rvert/\max_{i,j}\lvert a_{ij}\rvert \), the largest entry in modulus the elimination produces relative to the largest in modulus it was given (@def-growth-factor); the classical version maximizes over every intermediate matrix as well, and is at least as large.

(b) At step \( k \), exchange row \( k \) with the row \( r \ge k \) maximizing \( \lvert a^{(k-1)}_{rk}\rvert \). The consequence is \( \lvert\ell_{ik}\rvert \le 1 \) for every multiplier, in exact arithmetic and in the model.

(c) \( \tfrac23 n^3 \), \( 2n^2 \) and \( \tfrac13 n^3 \) respectively (@prp-lu-cost); the third is half the first.

(d) (i) Incorrect. @thm-triangular-solve-backward-error holds for every non-singular triangular matrix, with no hypothesis on the diagonal and no pivoting. (ii) Incorrect as stated. The only growth bound available is @thm-growth-partial-pivoting's \( g_n \le 2^{n-1} \), proved for the exact elimination, and @exm-growth-attained shows it is attained; even granting its transfer to the computed factors — the gap recorded in the remark after @thm-lu-backward-error — the resulting backward error bound \( n^2 2^{n-1}u \) is vacuous for moderate \( n \). (iii) Incorrect. It gives an accurate solution only when the problem is well conditioned; @thm-forward-from-backward supplies the missing factor \( \kappa(\A) \).

(e) It is the Schur complement \( \A/\A_k \) of the leading \( k \times k \) block — so elimination is the repeated formation of Schur complements of \( 1 \times 1 \) pivots.
:::

### B. Practice

:::: {#exr-elimination-pivoting-and-cost-b1}
[B1: A Schur complement by two routes]

Let
\[
\A = \begin{pmatrix} 2 & 1 & -1 \\ 4 & 5 & -1 \\ -2 & 8 & 2\end{pmatrix} .
\]

::: {.enumerate options="label=(\alph*)"}
1. Carry out one step of elimination without row swaps and read off the trailing \( 2 \times 2 \) block.
2. Compute \( \A/\A_1 = \D - \C a_{11}^{-1}\B \) directly from @def-schur-complement and check that the two agree.
3. Carry out the second step and verify @cor-pivots-and-minors (a) by computing \( \det\A_1 \), \( \det\A_2 \) and \( \det\A_3 \).
:::
::::

::: {.solution}
(a) The multipliers are \( \ell_{21} = 4/2 = 2 \) and \( \ell_{31} = -2/2 = -1 \). Subtracting gives rows \( (0, 3, 1) \) and \( (0, 9, 1) \), so the trailing block is \( \begin{psmallmatrix}3&1\\9&1\end{psmallmatrix} \).

(b) Here \( \A_1 = (2) \), \( \B = (1, -1) \), \( \C = (4, -2)\tp \), \( \D = \begin{psmallmatrix}5&-1\\8&2\end{psmallmatrix} \), so
\[
\C a_{11}^{-1}\B = \tfrac12\begin{pmatrix}4\\-2\end{pmatrix}\begin{pmatrix}1&-1\end{pmatrix} = \begin{pmatrix}2&-2\\-1&1\end{pmatrix},
\qquad
\A/\A_1 = \begin{pmatrix}3&1\\9&1\end{pmatrix} ,
\]
which agrees with (a), as @thm-elimination-is-schur-complements says it must.

(c) The second multiplier is \( 9/3 = 3 \), and the second step turns \( (0,9,1) \) into \( (0, 0, 1 - 3) = (0,0,-2) \). So the pivots are \( 2, 3, -2 \). Now \( \det\A_1 = 2 \), \( \det\A_2 = 10 - 4 = 6 \), and \( \det\A = 2(10+8) - 1(8-2) + (-1)(32+10) = 36 - 6 - 42 = -12 \). The ratios are \( 2/1 = 2 \), \( 6/2 = 3 \) and \( -12/6 = -2 \): the pivots, as claimed.
:::

:::: {#exr-elimination-pivoting-and-cost-b2}
[B2: Growth, with and without a swap]

Let \( \A = \begin{pmatrix} 10^{-4} & 1 \\ 1 & 1\end{pmatrix} \), and work in the six-digit decimal model.

::: {.enumerate options="label=(\alph*)"}
1. Factor \( \A \) without an exchange, compute \( g_2 \), and compute \( \widehat\L\widehat\U \) exactly.
2. Do the same after exchanging the rows.
3. Compare the two backward errors with the bound of @eq-lu-growth-bound.
:::
::::

::: {.solution}
(a) The multiplier is \( \fl(1/10^{-4}) = 10^{4} \), and \( \widehat u_{22} = \fl(1 - 10^{4}) = -9999.00 \), which is exactly representable. So
\[
\widehat\L\widehat\U = \begin{pmatrix}1&0\\10^4&1\end{pmatrix}\begin{pmatrix}10^{-4}&1\\0&-9999\end{pmatrix} = \begin{pmatrix}10^{-4}&1\\1&1\end{pmatrix} = \A ,
\]
so here \( \Delta\A = \0 \): with six digits, \( 1 - 10^4 \) is *not* rounded, and nothing is lost. The growth factor is \( g_2 = 9999/1 = 9999 \).

(b) After the exchange the multiplier is \( 10^{-4} \) and \( \widehat u_{22} = \fl(1 - 10^{-4}) = 0.999900 \), again exact, so \( \widehat\L\widehat\U = \P\A \) exactly and \( g_2 = 1 \).

(c) Both backward errors are zero, so both satisfy the bound. For \( n = 2 \) the entry-at-a-time algorithm and Chapter 2's row operations perform the very same three operations, so @eq-lu-growth-bound applies to these runs as it stands, with \( g_2 \) read off the computed factors. The point is the *bound*, not the outcome: in (a) it is \( 2\gamma_2 g_2 \approx 4 \times 9999\,u \approx 0.2 \), which permits a catastrophe, while in (b) it is about \( 4u \), which does not. Large growth does not force a large backward error; it removes the guarantee that there is none, and @exm-epsilon-pivot shows what happens when the permission is taken up.
:::

:::: {#exr-elimination-pivoting-and-cost-b3}
[B3: The Cholesky entry bound]

Let \( \A = \begin{pmatrix} 4 & -2 & 6 \\ -2 & 5 & -1 \\ 6 & -1 & 26\end{pmatrix} \), whose Cholesky factor was computed in @exm-cholesky-by-hand to be \( \L \) with rows \( (2,0,0) \), \( (-1,2,0) \), \( (3,1,4) \).

::: {.enumerate options="label=(\alph*)"}
1. Check @thm-cholesky-stability (a) entry by entry.
2. Compute \( \lvert\L\rvert\lvert\L\tp\rvert \) and check that every entry is at most \( \max_{p,q}\lvert a_{pq}\rvert \).
3. What would the bound of @eq-lu-growth-bound require if \( \A \) were factored by general elimination with partial pivoting instead?
:::
::::

::: {.solution}
(a) The bound is \( \lvert\ell_{ij}\rvert \le \sqrt{a_{ii}} \). Row \( 1 \): \( 2 \le \sqrt4 = 2 \), with equality. Row \( 2 \): \( 1, 2 \le \sqrt5 \approx 2.236 \). Row \( 3 \): \( 3, 1, 4 \le \sqrt{26} \approx 5.099 \). All hold, and the row sums of squares are \( 4, 5, 26 \), which are \( a_{11}, a_{22}, a_{33} \) exactly.

(b) \( \lvert\L\rvert \) has rows \( (2,0,0) \), \( (1,2,0) \), \( (3,1,4) \), so
\[
\lvert\L\rvert\lvert\L\tp\rvert = \begin{pmatrix} 4 & 2 & 6\\ 2 & 5 & 5\\ 6 & 5 & 26\end{pmatrix} .
\]
The largest entry of \( \A \) in modulus is \( 26 \), and every entry above is at most \( 26 \) — indeed the \( (i,k) \) entry is at most \( \sqrt{a_{ii}a_{kk}} \): for instance \( 5 \le \sqrt{5 \cdot 26} \approx 11.4 \).

(c) It would require knowing \( g_3 \) for the computed factors, and the only bound available is @thm-growth-partial-pivoting's exact-arithmetic \( 2^{2} = 4 \); granting the transfer between the two (the remark after @thm-lu-backward-error), @eq-lu-growth-bound permits \( \max\lvert\Delta a_{ij}\rvert \le 3\gamma_3\cdot4\cdot26 = 12\gamma_3\cdot 26 \). @thm-cholesky-stability (c) permits \( \bigl(\gamma_4/(1-\gamma_4)\bigr)\cdot 26 \) instead: the factor \( 3g_3 = 12 \) disappears entirely, and the price is the step from \( \gamma_3 \) to \( \gamma_4/(1-\gamma_4) \), which is about \( \tfrac43\gamma_3 \). No pivoting is needed to get it.
:::

### C. Going deeper

:::: {#exr-elimination-pivoting-and-cost-c1}
[C1: Column diagonal dominance needs no pivoting]

Call \( \A \in M_n(\nR) \) **strictly column diagonally dominant** if \( \lvert a_{jj}\rvert > \sum_{i \ne j}\lvert a_{ij}\rvert \) for every \( j \).

::: {.enumerate options="label=(\alph*)"}
1. Show that partial pivoting makes no exchange at the first step.
2. Show that \( \A/\A_1 \) is again strictly column diagonally dominant, and that each of its column sums \( \sum_{i\ge2}\lvert a'_{ij}\rvert \) is at most the corresponding column sum \( \sum_{i\ge1}\lvert a_{ij}\rvert \) of \( \A \).
3. Deduce that elimination without any exchanges succeeds and that \( g_n < 2 \).
:::
*Hint: for (c), bound every entry of every \( \A^{(k)} \) by a column sum of \( \A \).*
::::

::: {.solution}
(a) Column \( 1 \) satisfies \( \lvert a_{11}\rvert > \sum_{i \ge 2}\lvert a_{i1}\rvert \ge \lvert a_{i1}\rvert \) for each \( i \ge 2 \), so the entry of largest modulus in column \( 1 \) is already \( a_{11} \), and it is non-zero.

(b) Write \( a'_{ij} = a_{ij} - (a_{i1}/a_{11})a_{1j} \) for \( i, j \ge 2 \). For the column sums, the triangle inequality gives
\[
\sum_{i\ge2}\lvert a'_{ij}\rvert
\le \sum_{i\ge2}\lvert a_{ij}\rvert + \frac{\lvert a_{1j}\rvert}{\lvert a_{11}\rvert}\sum_{i\ge2}\lvert a_{i1}\rvert
\le \sum_{i\ge2}\lvert a_{ij}\rvert + \lvert a_{1j}\rvert
= \sum_{i\ge1}\lvert a_{ij}\rvert ,
\]
using \( \sum_{i\ge2}\lvert a_{i1}\rvert < \lvert a_{11}\rvert \). For dominance, fix \( j \ge 2 \). Then
\[
\sum_{\substack{i\ge2\\ i\ne j}}\lvert a'_{ij}\rvert
\le \sum_{\substack{i\ge2\\ i\ne j}}\lvert a_{ij}\rvert + \frac{\lvert a_{1j}\rvert}{\lvert a_{11}\rvert}\sum_{\substack{i\ge2\\ i\ne j}}\lvert a_{i1}\rvert
< \bigl(\lvert a_{jj}\rvert - \lvert a_{1j}\rvert\bigr) + \frac{\lvert a_{1j}\rvert}{\lvert a_{11}\rvert}\bigl(\lvert a_{11}\rvert - \lvert a_{j1}\rvert\bigr) ,
\]
where the two strict bounds are column-\( j \) and column-\( 1 \) dominance. The right side equals \( \lvert a_{jj}\rvert - \lvert a_{1j}\rvert\lvert a_{j1}\rvert/\lvert a_{11}\rvert \), which is at most \( \lvert a_{jj} - a_{j1}a_{1j}/a_{11}\rvert = \lvert a'_{jj}\rvert \) by the reverse triangle inequality. So \( \sum_{i \ge 2, i\ne j}\lvert a'_{ij}\rvert < \lvert a'_{jj}\rvert \).

(c) By (a) and (b) and induction, every Schur complement \( \A^{(k)} \) restricted to its active block is strictly column diagonally dominant, so no exchange is ever made and no pivot is zero. By (b) and induction, the column sums of the active blocks never increase, so every entry of every \( \A^{(k)} \) is bounded by \( \max_j\sum_i\lvert a_{ij}\rvert \) — and the rows that have been frozen into \( \U \) were bounded the same way when they were created. Finally, dominance gives \( \sum_i\lvert a_{ij}\rvert < 2\lvert a_{jj}\rvert \le 2\max_{p,q}\lvert a_{pq}\rvert \), so \( g_n < 2 \). Hence such matrices need no pivoting at all.
:::

:::: {#exr-elimination-pivoting-and-cost-c2}
[C2: The growth bound is attained for every \( n \)]

Let \( \Y_n \) be the matrix of @exm-growth-attained: \( y_{ii} = 1 \), \( y_{ij} = -1 \) for \( i > j \), \( y_{in} = 1 \) for all \( i \), and \( y_{ij} = 0 \) for \( j > i \) with \( j < n \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that partial pivoting makes no exchange at any step, and that every multiplier equals \( -1 \).
2. Prove by induction on \( k \) that after \( k \) steps the active trailing block is again of the form \( \Y_{n-k} \), except that its last column is \( 2^{k} \) times the all-ones vector.
3. Deduce \( g_n = 2^{n-1} \), and explain why this does not contradict the practical success of partial pivoting.
:::
::::

::: {.solution}
(a) and (b) together, by induction. At step \( k = 1 \), column \( 1 \) is \( (1, -1, \dots, -1) \), every entry of modulus \( 1 \), so the pivot \( y_{11} = 1 \) is already of largest modulus and no exchange is made; the multipliers are \( -1/1 = -1 \). Subtracting \( -1 \) times row \( 1 \) from row \( i \) adds row \( 1 \) to row \( i \). Row \( 1 \) is \( (1, 0, \dots, 0, 1) \), so for \( i \ge 2 \) the entries in columns \( 2, \dots, n-1 \) are unchanged, the entry in column \( 1 \) becomes \( 0 \), and the entry in column \( n \) becomes \( 1 + 1 = 2 \). The trailing \( (n-1)\times(n-1) \) block therefore has \( 1 \) on its diagonal, \( -1 \) below, \( 0 \) above except in the last column, and \( 2 \) throughout its last column: it is \( \Y_{n-1} \) with the last column doubled. Since doubling one column changes neither which entry of a column has largest modulus nor the ratios within the other columns, the same applies at every subsequent step, and after \( k \) steps the active block is \( \Y_{n-k} \) with last column \( 2^{k} \) times the all-ones vector.

(c) Every entry of \( \Y_n \) has modulus \( 1 \), so \( M_0 = 1 \). By (b) the largest entry ever created is the \( (n,n) \) entry after step \( n-1 \), namely \( 2^{n-1} \). So \( g_n = 2^{n-1} \), meeting @thm-growth-partial-pivoting exactly.

This does not contradict anything practical: \( \Y_n \) is a constructed matrix, and the theorem only says the *worst case* is \( 2^{n-1} \). What the example does destroy is the hope of a theorem: no bound better than \( 2^{n-1} \) can be proved for partial pivoting, so any claim that partial pivoting is backward stable is a claim about the matrices one meets, not about all matrices. That is why @thm-cholesky-stability matters — it is a genuine theorem, for a class of matrices identified in advance.
:::
