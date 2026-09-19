# Birkhoff's Theorem

Chapter 17 §08 met the doubly stochastic matrices, the non-negative matrices whose rows and columns all add up to \( 1 \). It showed that every permutation matrix is an extreme point of the set \( \Omega_n \) they form, stated Birkhoff's theorem that there are no other extreme points, proved that this is equivalent to "every doubly stochastic matrix is an average of permutation matrices", and left the proof to this chapter. This section supplies it. The proof is a count: a corner of \( \Omega_n \) has so many zero entries that some row holds a single \( 1 \), and deleting that row and its column leaves a corner of \( \Omega_{n-1} \). We then bound how many permutation matrices an average needs, turn the theorem into a procedure for finding them, and use it to give the second proof of Schur's majorization theorem that Chapter 17 §08 sketched.

Throughout, the field is \( \nR \), and inequalities between matrices or vectors are entrywise, as in §01. Recall @def-doubly-stochastic: \( \M \in M_n(\nR) \) is **doubly stochastic** if \( m_{ij} \ge 0 \) for all \( i, j \), and every row and every column adds up to \( 1 \); in terms of the all-ones vector, \( \M\1 = \1 \) and \( \1\tp\M = \1\tp \). So \( \M \) is stochastic in the book's column sense (@def-stochastic-matrix), and so is \( \M\tp \).

## What is left to prove

Here is where Chapter 17 §08 stopped. The set \( \Omega_n \) is convex and compact. The \( n! \) permutation matrices \( \P_\sigma \), \( \sigma \in S_n \) (@def-permutation-matrix), lie in it, and each is an extreme point (@prp-permutation-matrices-extreme). The two forms of Birkhoff's theorem, "the extreme points are the permutation matrices" and "\( \Omega_n \) is the convex hull of the permutation matrices", were shown to be equivalent there, using Minkowski's theorem (@thm-minkowski-extreme) in one direction and @prp-extreme-points-of-hull in the other. For \( n = 2 \), the Quick check after the statement found \( \Omega_2 \) by hand: it is the segment from \( \I \) to the swap matrix.

So one implication is missing: **every extreme point of \( \Omega_n \) is a permutation matrix.** For \( n \ge 3 \) nothing as simple as the \( 2 \times 2 \) computation is available, since \( \Omega_3 \) already has four free parameters. What does the work instead is a result of Chapter 17 §09 that recognizes a corner of a polyhedron from its tight constraints.

## The doubly stochastic matrices form a polyhedron

Recall @def-polyhedron and @thm-vertices-basic-feasible. A polyhedron is a set \( \{\x \in \nR^N : \A\x \le \b\} \); its extreme points are called vertices; and a point \( \x \) of it is a vertex exactly when the rows \( \a_i\tp \) of the constraints that hold with equality at \( \x \), the **active** rows, include \( N \) linearly independent ones. An equation is allowed, as a pair of inequalities \( \a\tp\x \le \beta \) and \( -\a\tp\x \le -\beta \); both are active at every point of the polyhedron.

To put \( \Omega_n \) in this form, list the \( n^2 \) entries of a matrix \( \X \) as one column, the vectorization \( \vecop\X \in \nR^{n^2} \) of Chapter 7. A linear expression \( \sum_{i,j} b_{ij}x_{ij} \) in the entries is then the dot product of \( \vecop\X \) with \( \vecop\B \), and we may treat the coefficient matrix \( \B \in M_n(\nR) \) itself as the row of the constraint. Three families of coefficient matrices appear. With \( \E_{ij} \) the matrix unit (a \( 1 \) in position \( (i,j) \), zeros elsewhere), let
\[
\R_i = \e_i\1\tp , \qquad \C_j = \1\e_j\tp \qquad (1 \le i, j \le n) ,
\]
the matrices whose \( i \)-th row, respectively \( j \)-th column, consists of ones and whose other entries are zero. The letter \( \C_j \) is local to this section; elsewhere \( \C(p) \) is a companion matrix and \( \C_k(\lambda) \) a real Jordan block. Then \( \sum_{k,l}(\R_i)_{kl}x_{kl} \) is the \( i \)-th row sum of \( \X \), and \( \C_j \) gives the \( j \)-th column sum. So \( \Omega_n \subseteq M_n(\nR) \cong \nR^{n^2} \) is the polyhedron cut out by

::: {.enumerate options="label=(\roman*)"}
1. the \( n^2 \) inequalities \( -x_{ij} \le 0 \), with rows \( -\E_{ij} \);
2. the \( n \) row equations "row sum \( i \) equals \( 1 \)", with rows \( \pm\R_i \);
3. the \( n \) column equations "column sum \( j \) equals \( 1 \)", with rows \( \pm\C_j \).
:::

At a point \( \M \in \Omega_n \), every row \( \pm\R_i \) and \( \pm\C_j \) is active, and \( -\E_{ij} \) is active exactly when \( m_{ij} = 0 \). The whole argument turns on how much the \( 2n \) equations are worth. They are not independent: adding all row sums and adding all column sums both give the sum of all entries, that is,
\[
\R_1 + \dots + \R_n = \J = \C_1 + \dots + \C_n ,
\]
with \( \J \) the all-ones matrix. The next lemma says that this is the only relation.

::: {#lem-doubly-stochastic-sum-conditions}
[The Row and Column Sum Conditions]

Let \( n \ge 1 \), and let
\[
W_n = \{\X \in M_n(\nR) : \X\1 = \0,\ \1\tp\X = \0\tp\}
\]
be the space of real matrices whose rows and columns all add up to \( 0 \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \dim W_n = (n-1)^2 \);
2. the \( 2n \) matrices \( \R_1, \dots, \R_n, \C_1, \dots, \C_n \) span a subspace of \( M_n(\nR) \) of dimension \( 2n - 1 \).
:::
:::

::: {.idea}
A matrix in \( W_n \) is determined by its top-left \( (n-1) \times (n-1) \) block, which can be anything: the last column and the last row are then forced by the zero sums, and the corner comes out consistent. That gives (a). For (b), \( W_n \) is exactly the set of matrices killed by the \( 2n \) sum conditions, so rank–nullity converts one count into the other.
:::

::: {.proof}
(a) If \( n = 1 \), \( W_1 = \{\0\} \) and \( (n-1)^2 = 0 \). Let \( n \ge 2 \), and let \( \varphi \colon W_n \to M_{n-1}(\nR) \) delete the last row and the last column; it is linear. It is injective: if \( \X \in W_n \) has top-left block zero, then for \( i < n \) the \( i \)-th row sum is \( x_{in} = 0 \), for \( j < n \) the \( j \)-th column sum is \( x_{nj} = 0 \), and then the last row sum is \( x_{nn} = 0 \). So \( \X = \0 \). It is surjective: given \( \B \in M_{n-1}(\nR) \), with row sums \( r_i \), column sums \( c_j \) and total \( s = \sum_i r_i = \sum_j c_j \), let \( \X \) have top-left block \( \B \), last column \( (-r_1, \dots, -r_{n-1}, s) \) and last row \( (-c_1, \dots, -c_{n-1}, s) \). The \( i \)-th row sum for \( i < n \) is \( r_i - r_i = 0 \), the \( j \)-th column sum for \( j < n \) is \( c_j - c_j = 0 \), and the last row and last column both sum to \( -s + s = 0 \). So \( \X \in W_n \) and \( \varphi(\X) = \B \). Hence \( \varphi \) is an isomorphism and \( \dim W_n = \dim M_{n-1}(\nR) = (n-1)^2 \).

(b) Let \( \K \) be the \( 2n \times n^2 \) matrix whose rows are the transposed vectorizations \( (\vecop\R_i)\tp \) and \( (\vecop\C_j)\tp \), for \( 1 \le i, j \le n \). Then \( \K\,\vecop\X \) lists the row sums and the column sums of \( \X \), so the null space of \( \K \) is \( \vecop(W_n) \), of dimension \( (n-1)^2 \) by (a), as \( \vecop \) is an isomorphism. By @thm-rank-nullity-matrix, \( \rank\K = n^2 - (n-1)^2 = 2n - 1 \), and by @thm-row-rank-equals-column-rank this is the dimension of the span of the rows of \( \K \). Since \( \vecop \) is an isomorphism, the \( 2n \) matrices \( \R_i, \C_j \) span a subspace of dimension \( 2n - 1 \), as claimed.
:::

So of the \( n^2 + 4n \) constraints defining \( \Omega_n \), the \( 4n \) that come from equations contribute only \( 2n - 1 \) dimensions to the active rows, wherever we stand. The rest must come from zero entries.

::: {.check}
A vertex of \( \Omega_3 \) needs \( 9 \) linearly independent active rows. How many zero entries must it therefore have, at least? Does the identity matrix \( \I_3 \) meet this requirement?
:::

::: {.solution}
The row and column equations supply at most \( 2 \cdot 3 - 1 = 5 \) independent rows, by @lem-doubly-stochastic-sum-conditions (b). Each zero entry adds one row \( -\E_{ij} \), so at least \( 9 - 5 = 4 \) zero entries are needed; that is, at most \( 5 \) non-zero entries. The identity has \( 6 \) zero entries and \( 3 \) non-zero ones, so it meets the requirement with room to spare.
:::

## Birkhoff's theorem

Now the main theorem. We state both forms, since both are used, but prove only the missing implication.

::: {#thm-birkhoff}
[Birkhoff's Theorem]

Let \( n \ge 1 \). The extreme points of \( \Omega_n \) are exactly the \( n! \) permutation matrices of size \( n \). Equivalently, every doubly stochastic matrix is a convex combination of permutation matrices:
\[
\Omega_n = \conv\{\P_\sigma : \sigma \in S_n\} .
\]
:::

::: {.idea}
**Step roadmap.** Let \( \M \) be an extreme point of \( \Omega_n \) and induct on \( n \).

① **Count.** \( \M \) is a vertex of the polyhedron above, so it has \( n^2 \) independent active rows. At most \( 2n - 1 \) of them come from the equations, so at least \( n^2 - (2n-1) \) entries of \( \M \) are zero, and at most \( 2n - 1 \) are non-zero.

② **Pigeonhole.** Every row has a non-zero entry, since it adds up to \( 1 \). With \( n \) rows and fewer than \( 2n \) non-zero entries, some row has exactly one, and that entry is \( 1 \). Its column then has no room for anything else.

③ **Strip.** Delete that row and column. What is left is doubly stochastic of size \( n - 1 \), and, the key point, it is again **extreme**: any way of splitting it would split \( \M \).

④ **Induct.** The smaller matrix is a permutation matrix, and putting the \( 1 \) back gives one of size \( n \).
:::

::: {.proof}
By @prp-permutation-matrices-extreme, every permutation matrix is an extreme point of \( \Omega_n \). Distinct permutations give distinct matrices, since column \( j \) of \( \P_\sigma \) is \( \e_{\sigma(j)} \), so there are \( n! \) of them. The equivalence of the two forms was proved in Chapter 17 §08, from @thm-minkowski-extreme and @prp-extreme-points-of-hull. It remains to show that every extreme point of \( \Omega_n \) is a permutation matrix. We prove this by induction on \( n \ge 1 \).

For \( n = 1 \), \( \Omega_1 = \{(1)\} \), and \( (1) = \P_{\id} \).

Let \( n \ge 2 \), assume the statement for \( n - 1 \), and let \( \M \) be an extreme point of \( \Omega_n \).

**Step 1: at most \( 2n - 1 \) non-zero entries.** As shown above, \( \Omega_n \) is a polyhedron in \( M_n(\nR) \cong \nR^{n^2} \), and \( \M \) is one of its vertices (@def-polyhedron). By @thm-vertices-basic-feasible, the active rows at \( \M \) include \( n^2 \) linearly independent ones. Let \( z \) be the number of zero entries of \( \M \). The active rows are \( \pm\R_i \), \( \pm\C_j \), and \( -\E_{ij} \) for the \( z \) positions with \( m_{ij} = 0 \). All of them lie in the subspace
\[
\Span\{\R_1, \dots, \R_n, \C_1, \dots, \C_n\} + \Span\{\E_{ij} : m_{ij} = 0\} ,
\]
whose dimension is at most \( (2n - 1) + z \), by @lem-doubly-stochastic-sum-conditions (b) and the dimension formula for sums (@thm-dimension-formula-subspace-dim). A subspace containing \( n^2 \) linearly independent vectors has dimension at least \( n^2 \), by @thm-size-bounds (a) applied in that subspace. Hence \( n^2 \le 2n - 1 + z \), and the number of non-zero entries of \( \M \) is \( n^2 - z \le 2n - 1 \).

**Step 2: a row with a single \( 1 \).** Each row of \( \M \) adds up to \( 1 \), so it has at least one non-zero entry. If every row had at least two, \( \M \) would have at least \( 2n \) non-zero entries, contradicting Step 1. So some row \( i \) has exactly one non-zero entry, say \( m_{ij} \), and the row sum gives \( m_{ij} = 1 \). Column \( j \) consists of non-negative entries adding up to \( 1 \), one of which is \( m_{ij} = 1 \); so \( m_{kj} = 0 \) for every \( k \ne i \).

**Step 3: the reduced matrix is extreme.** Let \( \M' \in M_{n-1}(\nR) \) be \( \M \) with row \( i \) and column \( j \) deleted. Its entries are non-negative. Each of its rows is a row \( k \ne i \) of \( \M \) with the entry \( m_{kj} = 0 \) removed, so it still adds up to \( 1 \); likewise each of its columns is a column \( l \ne j \) of \( \M \) with \( m_{il} = 0 \) removed. So \( \M' \in \Omega_{n-1} \). For \( \Y \in M_{n-1}(\nR) \), let \( E(\Y) \in M_n(\nR) \) be the matrix obtained by inserting a new row at position \( i \) and a new column at position \( j \), with a \( 1 \) where they cross and zeros elsewhere along them. Then \( E(\M') = \M \); \( E(\Y) \in \Omega_n \) whenever \( \Y \in \Omega_{n-1} \), since the inserted row and column add up to \( 1 \) and add \( 0 \) to every old row and column; \( E(\Y) = E(\Z) \) only if \( \Y = \Z \); and \( E\bigl(\tfrac12(\Y + \Z)\bigr) = \tfrac12\bigl(E(\Y) + E(\Z)\bigr) \), because the inserted entries are the same for \( \Y \), \( \Z \) and their midpoint. Now suppose \( \M' = \tfrac12(\Y + \Z) \) with \( \Y, \Z \in \Omega_{n-1} \). Then \( \M = \tfrac12\bigl(E(\Y) + E(\Z)\bigr) \) with \( E(\Y), E(\Z) \in \Omega_n \), and since \( \M \) is extreme, \( E(\Y) = E(\Z) \), so \( \Y = \Z \). By the midpoint test (@lem-extreme-midpoint), \( \M' \) is an extreme point of \( \Omega_{n-1} \).

**Step 4: induction.** By the induction hypothesis, \( \M' \) is a permutation matrix: it has exactly one \( 1 \) in each row and each column and zeros elsewhere. Then so does \( \M = E(\M') \): row \( i \) and column \( j \) contain only the inserted \( 1 \), and every other row and column is one of \( \M' \) with a \( 0 \) inserted. By the remark after @def-permutation-matrix, \( \M \) is a permutation matrix. This completes the induction and proves the theorem.
:::

This pays Chapter 17 §08's promise. With Minkowski's theorem it describes \( \Omega_n \) completely: a compact convex set with exactly \( n! \) corners, each a permutation matrix.

Step 3 is not decoration. It is tempting to finish from Step 1 alone, by an induction on the number of non-zero entries, and that induction does not close.

::: {.warning}
**Few non-zero entries do not by themselves make a permutation matrix.** The matrix
\[
\N = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \tfrac12 & \tfrac12 \\ 0 & \tfrac12 & \tfrac12 \end{pmatrix} \in \Omega_3
\]
has \( 5 = 2 \cdot 3 - 1 \) non-zero entries, the most Step 1 allows, and it is not a permutation matrix; it is the midpoint of \( \I_3 \) and the permutation matrix that swaps the last two coordinates. Deleting its first row and column leaves \( \tfrac12\J_2 \), with \( 4 \) non-zero entries, more than the \( 2 \cdot 2 - 1 = 3 \) that a vertex of \( \Omega_2 \) may have. The count must be applied afresh at each size, and that needs the smaller matrix to be extreme, which is what Step 3 proves.
:::

## How many permutation matrices

Birkhoff's theorem writes every doubly stochastic matrix as an average of permutation matrices, but a priori with up to \( n! \) terms. Carathéodory's theorem (@thm-caratheodory) cuts this down to one more than the dimension, and the dimension is the one computed in @lem-doubly-stochastic-sum-conditions.

::: {#cor-birkhoff-convex-combination}
[Birkhoff's Theorem with a Count]

Let \( n \ge 1 \). Every \( \M \in \Omega_n \) is a convex combination of at most \( (n-1)^2 + 1 \) permutation matrices.
:::

::: {.idea}
All of \( \Omega_n \) lies in the coset of matrices with row and column sums \( 1 \), which is \( \tfrac1n\J + W_n \), of dimension \( (n-1)^2 \). Translate to \( W_n \) and apply Carathéodory's theorem there.
:::

::: {.proof}
Let \( \M \in \Omega_n \). By @thm-birkhoff and @thm-convex-hull-combinations, \( \M = \sum_{k=1}^{m} t_k\P_k \) for some permutation matrices \( \P_k \) and weights \( (t_1, \dots, t_m) \in \Delta_m \). Put \( \X_0 = \tfrac1n\J \in \Omega_n \). Every doubly stochastic matrix \( \X \) satisfies \( (\X - \X_0)\1 = \1 - \1 = \0 \) and \( \1\tp(\X - \X_0) = \0\tp \), so \( \X - \X_0 \in W_n \). As the weights add up to \( 1 \),
\[
\M - \X_0 = \sum_{k=1}^{m} t_k(\P_k - \X_0) ,
\]
so \( \M - \X_0 \) lies in the convex hull of \( S = \{\P_\sigma - \X_0 : \sigma \in S_n\} \), a subset of the real vector space \( W_n \), which has dimension \( (n-1)^2 \) by @lem-doubly-stochastic-sum-conditions (a). By @thm-caratheodory, \( \M - \X_0 = \sum_{k=1}^{r} s_k(\P'_k - \X_0) \) for some \( r \le (n-1)^2 + 1 \), permutation matrices \( \P'_k \) and weights \( (s_1, \dots, s_r) \in \Delta_r \). Adding \( \X_0 = \sum_k s_k\X_0 \) back gives \( \M = \sum_{k=1}^{r} s_k\P'_k \), as claimed.
:::

For \( n = 2 \) the bound is \( 2 \), and every point strictly inside the segment \( \Omega_2 \) needs both ends. For \( n = 3 \), Exercise C1 shows that \( 5 \) can be needed. That \( (n-1)^2 + 1 \) is best possible for every \( n \ge 2 \) is a known result which we state without proof. Compare the density matrices of Chapter 17 §08, where the spectral theorem did much better than Carathéodory's count. Here there is no such structure to exploit.

## Finding the permutations

The proof of Birkhoff's theorem says that the permutation matrices suffice. It does not say how to find them. One consequence of the theorem does, because it only concerns which entries are zero.

::: {#cor-doubly-stochastic-positive-diagonal}
[A Positive Diagonal]

Let \( \M \in \Omega_n \). Then there is a permutation \( \sigma \in S_n \) with \( m_{\sigma(j)j} > 0 \) for **every** \( j = 1, \dots, n \).
:::

::: {.proof}
By @thm-birkhoff, \( \M = \sum_{\tau \in S_n} t_\tau\P_\tau \) with every \( t_\tau \ge 0 \) and \( \sum_\tau t_\tau = 1 \), so some \( t_\sigma > 0 \). The \( (\sigma(j), j) \) entry of \( \P_\sigma \) is \( 1 \), and every term of the sum has non-negative entries. Hence \( m_{\sigma(j)j} \ge t_\sigma > 0 \) for every \( j \).
:::

In words, one can pick one positive entry in each column, all in different rows. This gives a procedure, often called **peeling**. Given \( \M \in \Omega_n \), choose \( \sigma \) as in the corollary and let \( t = \min_j m_{\sigma(j)j} \), so \( 0 < t \le 1 \).

- If \( t = 1 \), then each column \( j \) has its whole sum \( 1 \) at position \( \sigma(j) \), and \( \M = \P_\sigma \).
- If \( t < 1 \), then \( \M - t\P_\sigma \) has non-negative entries and all row and column sums \( 1 - t \), so \( \M_1 = (\M - t\P_\sigma)/(1 - t) \in \Omega_n \) and \( \M = t\P_\sigma + (1 - t)\M_1 \). Every zero of \( \M \) is a zero of \( \M_1 \), since \( \P_\sigma \) has its \( 1 \)'s at positive entries of \( \M \), and the entry where the minimum \( t \) was attained becomes a new zero.

Repeat with \( \M_1 \), producing \( \M_2, \M_3, \dots \), and write \( \M_0 = \M \). A doubly stochastic matrix has at least \( n \) non-zero entries, one per column, and each round removes at least one, so the procedure stops after at most \( n^2 - n + 1 \) rounds, with a permutation matrix. Unwinding the rounds writes \( \M \) as a convex combination of the permutation matrices found. In fact peeling never needs more than the \( (n-1)^2 + 1 \) of @cor-birkhoff-convex-combination. Let \( U_k \) be the subspace of those \( \X \in W_n \) with \( x_{ij} = 0 \) wherever \( \M_k \) has a zero; since zeros of \( \M_k \) stay zeros, \( U_{k+1} \subseteq U_k \), and \( \M_k - \M_{k+1} \) lies in \( U_k \) but not in \( U_{k+1} \), being positive at the new zero. So each round with \( t < 1 \) lowers \( \dim U_k \), which starts at most \( \dim W_n = (n-1)^2 \) by @lem-doubly-stochastic-sum-conditions (a) and never drops below \( 0 \); there are at most \( (n-1)^2 \) such rounds, and one final round. Still, peeling finds **a** decomposition, not necessarily the shortest one.

::: {#exm-birkhoff-peeling}
[Peeling a 4 × 4 matrix]

Write
\[
\M = \frac18\begin{pmatrix} 4 & 2 & 2 & 0 \\ 1 & 3 & 0 & 4 \\ 3 & 0 & 4 & 1 \\ 0 & 3 & 2 & 3 \end{pmatrix}
\]
as a convex combination of permutation matrices.
:::

::: {.solution}
The entries are non-negative, each row of \( 8\M \) adds up to \( 8 \), and so does each column: \( 4 + 1 + 3 + 0 \), \( 2 + 3 + 0 + 3 \), \( 2 + 0 + 4 + 2 \), \( 0 + 4 + 1 + 3 \). So \( \M \in \Omega_4 \). We peel \( \N = 8\M \), whose row and column sums start at \( 8 \); subtracting \( w \) times a permutation matrix lowers them all by \( w \). A permutation is recorded by the positions \( (\sigma(1), 1), \dots, (\sigma(4), 4) \) of its \( 1 \)'s, one per column.

*Round 1.* The diagonal of \( \N \) is \( 4, 3, 4, 3 \), all positive, so take \( \sigma_1 = \id \) with weight \( w_1 = 3 \). Subtracting \( 3\I \) leaves
\[
\begin{pmatrix} 1 & 2 & 2 & 0 \\ 1 & 0 & 0 & 4 \\ 3 & 0 & 1 & 1 \\ 0 & 3 & 2 & 0 \end{pmatrix} \quad (\text{sums } 5) .
\]

*Round 2.* Column \( 2 \) is now non-zero only in rows \( 1 \) and \( 4 \). Try row \( 4 \) there: the positions \( (1,1) \), \( (4,2) \), \( (3,3) \), \( (2,4) \) carry \( 1, 3, 1, 4 \), so take this \( \sigma_2 \) with weight \( w_2 = 1 \):
\[
\begin{pmatrix} 0 & 2 & 2 & 0 \\ 1 & 0 & 0 & 3 \\ 3 & 0 & 0 & 1 \\ 0 & 2 & 2 & 0 \end{pmatrix} \quad (\text{sums } 4) .
\]

*Round 3.* The positions \( (3,1), (1,2), (4,3), (2,4) \) carry \( 3, 2, 2, 3 \); weight \( w_3 = 2 \):
\[
\begin{pmatrix} 0 & 0 & 2 & 0 \\ 1 & 0 & 0 & 1 \\ 1 & 0 & 0 & 1 \\ 0 & 2 & 0 & 0 \end{pmatrix} \quad (\text{sums } 2) .
\]

*Round 4.* The positions \( (2,1), (4,2), (1,3), (3,4) \) carry \( 1, 2, 2, 1 \); weight \( w_4 = 1 \). What remains has a single \( 1 \) in positions \( (3,1), (4,2), (1,3), (2,4) \), a permutation matrix \( \P_{\sigma_5} \), with weight \( w_5 = 1 \).

The weights \( 3 + 1 + 2 + 1 + 1 = 8 \) account for the whole sum, and dividing by \( 8 \),
\[
\M = \tfrac38\,\P_{\sigma_1} + \tfrac18\,\P_{\sigma_2} + \tfrac28\,\P_{\sigma_3} + \tfrac18\,\P_{\sigma_4} + \tfrac18\,\P_{\sigma_5} ,
\]
where \( \sigma_1 = \id \), and \( \sigma_2, \sigma_3, \sigma_4, \sigma_5 \) send \( 1, 2, 3, 4 \) to \( 1, 4, 3, 2 \), to \( 3, 1, 4, 2 \), to \( 2, 4, 1, 3 \) and to \( 3, 4, 1, 2 \) respectively. Five terms, within the bound \( (4-1)^2 + 1 = 10 \). To check, add up any entry: position \( (1,3) \) is covered by \( \sigma_4 \) and \( \sigma_5 \), giving \( \tfrac18 + \tfrac18 = \tfrac28 \), which is \( m_{13} \).
:::

::: {.remark}
The route can be run the other way. @cor-doubly-stochastic-positive-diagonal is a statement about the zero pattern of \( \M \) alone, and it can be proved directly by combinatorics: by Hall's marriage theorem, or by the Frobenius–König theorem, which says that every \( n \times n \) matrix in which each choice of one entry per column, in distinct rows, meets a zero has an \( r \times s \) block of zeros with \( r + s = n + 1 \). With the corollary in hand first, peeling proves Birkhoff's theorem constructively. Both routes are standard; the one taken here uses only what Chapter 17 had already built.
:::

## Schur's theorem again

Chapter 16 §08 proved Schur's majorization theorem, @thm-schur-majorization: for a Hermitian \( \A \), the diagonal vector \( \d(\A) \) is majorized by the eigenvalue vector \( \vlambda(\A) \). The proof there went through Ky Fan's maximum principle. Chapter 17 §08 noted that Birkhoff's theorem would give a second proof, and sketched it. Here it is in full. The first ingredient says that the diagonal is a doubly stochastic image of the spectrum.

::: {#lem-diagonal-doubly-stochastic-image}
[The Diagonal Is a Doubly Stochastic Image of the Spectrum]

Let \( F = \nR \) or \( \nC \), let \( \A \in M_n(F) \) be Hermitian, and let \( \A = \U\D\U^{*} \) with \( \U \) unitary and \( \D = \diag(\lambda_1(\A), \dots, \lambda_n(\A)) \). Then the matrix \( \S = (\lvert u_{ij}\rvert^2) \) is doubly stochastic, and
\[
\d(\A) = \S\,\vlambda(\A) .
\]
Such a \( \U \) exists by @cor-spectral-complex-matrix, after reordering the columns of \( \U \), since a Hermitian matrix is normal: the diagonal entries of the \( \D \) it gives are the eigenvalues of \( \A \) with multiplicity, because similar matrices have the same characteristic polynomial \( p_{\A} \) (@thm-charpoly-similarity-invariant), and they are real (@thm-self-adjoint-real-eigenvalues), so they can be put in decreasing order.
:::

::: {.proof}
Write \( \lambda_j = \lambda_j(\A) \). By the definition of the matrix product, \( a_{ii} = \sum_{j}u_{ij}\lambda_j\conj{u_{ij}} = \sum_j \lvert u_{ij}\rvert^2\lambda_j \), which is the \( i \)-th entry of \( \S\vlambda(\A) \). The entries of \( \S \) are non-negative. Row \( i \) of \( \S \) adds up to \( \sum_j \lvert u_{ij}\rvert^2 = (\U\U^{*})_{ii} = 1 \), and column \( j \) adds up to \( \sum_i \lvert u_{ij}\rvert^2 = (\U^{*}\U)_{jj} = 1 \), since \( \U \) is unitary. So \( \S \in \Omega_n \).
:::

A doubly stochastic matrix of the form \( (\lvert u_{ij}\rvert^2) \) is called **unistochastic**. Not every doubly stochastic matrix is one (Exercise C3 asks for a witness), but the lemma needs only that \( \S \in \Omega_n \). The second ingredient is Birkhoff's theorem, which makes \( \S\vlambda \) an average of rearrangements of \( \vlambda \).

::: {#prp-doubly-stochastic-image-majorized}
[Doubly Stochastic Maps Even Out]

Let \( \S \in \Omega_n \) and \( \y \in \nR^n \). Then \( \S\y \prec \y \).
:::

::: {.idea}
A permutation matrix only rearranges \( \y \), and rearrangements are invisible to majorization. Birkhoff's theorem writes \( \S\y \) as an average of rearrangements, and the vectors majorized by \( \y \) form a convex set.
:::

::: {.proof}
By @thm-birkhoff, \( \S = \sum_{k=1}^{m} t_k\P_{\sigma_k} \) with \( (t_1, \dots, t_m) \in \Delta_m \), so \( \S\y = \sum_k t_k\P_{\sigma_k}\y \). Each \( \P_{\sigma}\y = \sum_j y_j\e_{\sigma(j)} \) has entry \( y_j \) in position \( \sigma(j) \), so it is a rearrangement of \( \y \). As observed after @def-majorization, majorization sees only which numbers occur and how often, so \( \y \prec \y \) (@prp-majorization-basic (a)) gives \( \P_\sigma\y \prec \y \). By @exm-majorization-set-convex the set \( \{\x : \x \prec \y\} \) is convex, and a convex set contains every convex combination of its points (@lem-convex-contains-combinations). Hence \( \S\y \prec \y \).
:::

*Second proof of @thm-schur-majorization.* Let \( \A \) be Hermitian. By @lem-diagonal-doubly-stochastic-image, \( \d(\A) = \S\vlambda(\A) \) with \( \S \in \Omega_n \), and by @prp-doubly-stochastic-image-majorized, \( \S\vlambda(\A) \prec \vlambda(\A) \). So \( \d(\A) \prec \vlambda(\A) \). \( \square \)

The first proof compared running totals using a variational principle; this one never compares running totals directly. It sees Schur's theorem as a statement about averaging: the diagonal entries are weighted averages of the eigenvalues, with weights that form a doubly stochastic matrix, and averaging can only even out a vector.

::: {#exm-schur-via-birkhoff}
[The averaging made visible]

For
\[
\A = \begin{pmatrix} 3 & 2 & 0 \\ 2 & 4 & 2 \\ 0 & 2 & 5 \end{pmatrix}
\]
of Chapter 16 §08, whose eigenvalues are \( \vlambda(\A) = (7, 4, 1) \) with unit eigenvectors \( \u_1 = \tfrac13(1, 2, 2) \), \( \u_2 = \tfrac13(-2, -1, 2) \), \( \u_3 = \tfrac13(2, -2, 1) \) (@exm-schur-three-by-three), compute \( \S \), check \( \d(\A) = \S\vlambda(\A) \), and write \( \d(\A) \) as an average of rearrangements of \( \vlambda(\A) \).
:::

::: {.solution}
Take \( \U \) with columns \( \u_1, \u_2, \u_3 \); it is orthogonal and \( \A = \U\D\U\tp \). Squaring its entries,
\[
\U = \frac13\begin{pmatrix} 1 & -2 & 2 \\ 2 & -1 & -2 \\ 2 & 2 & 1 \end{pmatrix} , \qquad
\S = \frac19\begin{pmatrix} 1 & 4 & 4 \\ 4 & 1 & 4 \\ 4 & 4 & 1 \end{pmatrix} .
\]
Every row and column of \( 9\S \) adds up to \( 9 \). Then
\[
\S\vlambda(\A) = \frac19\begin{pmatrix} 7 + 16 + 4 \\ 28 + 4 + 4 \\ 28 + 16 + 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 4 \\ 5 \end{pmatrix} = \d(\A) .
\]
To decompose \( \S \), let \( \P \) be the permutation matrix of \( \sigma = (1\ 2\ 3) \), \( \sigma(1) = 2 \), \( \sigma(2) = 3 \), \( \sigma(3) = 1 \). Then \( \P + \P^2 = \J - \I \), since \( \P \) and \( \P^2 \) have their \( 1 \)'s in the off-diagonal positions and never in the same place, so
\[
\S = \tfrac19\,\I + \tfrac49\,\P + \tfrac49\,\P^2 .
\]
With \( \P\vlambda = (1, 7, 4) \) and \( \P^2\vlambda = (4, 1, 7) \), the cyclic shifts of \( (7, 4, 1) \),
\[
\d(\A) = \tfrac19(7, 4, 1) + \tfrac49(1, 7, 4) + \tfrac49(4, 1, 7) = (3, 4, 5) .
\]
Each diagonal entry is an average of all three eigenvalues, with weight \( \tfrac19 \) on one of them and \( \tfrac49 \) on the other two. That is why the diagonal \( (3, 4, 5) \) is so much flatter than \( (7, 4, 1) \).
:::

Together with @thm-schur-horn, the lemma and the proposition already show that the diagonals of the Hermitian matrices with spectrum \( \vlambda \) are exactly the vectors \( \S\vlambda \) with \( \S \in \Omega_n \). The lemma puts every such diagonal among the \( \S\vlambda \); the proposition puts every \( \S\vlambda \) among the \( \x \prec \vlambda \); and Schur–Horn realizes every \( \x \prec \vlambda \) as a diagonal. So all three sets coincide, and in particular every \( \x \prec \vlambda \) is \( \S\vlambda \) for some \( \S \in \Omega_n \). This converse of the proposition is part of the theorem of Hardy, Littlewood and Pólya, which Chapter 20 takes up.

## Exercises

### A. Check your understanding

:::: {#exr-birkhoff-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State Birkhoff's theorem in both forms.
2. Name the results of Chapter 17 that the proof of @thm-birkhoff uses, and say what each contributes.
3. What upper bound does Step 1 of the proof give for the number of non-zero entries of a vertex of \( \Omega_4 \)? How many does a vertex actually have?
4. True or false: every matrix in \( \Omega_n \) with at most \( 2n - 1 \) non-zero entries is a permutation matrix. Justify your answer.
5. True or false: the product of two doubly stochastic matrices is doubly stochastic. Justify your answer.
6. True or false: every \( \M \in \Omega_3 \) is a convex combination of at most five permutation matrices. Justify your answer.
:::
::::

::: {.solution}
(a) The extreme points of \( \Omega_n \) are exactly the \( n! \) permutation matrices; equivalently, \( \Omega_n \) is the convex hull of the permutation matrices, that is, every doubly stochastic matrix is a convex combination of them.

(b) @thm-vertices-basic-feasible, which says that a vertex has \( n^2 \) independent active constraints and so forces many zero entries; @lem-extreme-midpoint, the midpoint test, used to show that the stripped matrix is again extreme; and @prp-permutation-matrices-extreme with the equivalence of the two forms, which rests on @thm-minkowski-extreme and @prp-extreme-points-of-hull.

(c) At most \( 2 \cdot 4 - 1 = 7 \). By @thm-birkhoff a vertex is a permutation matrix, with exactly \( 4 \) non-zero entries. The bound of Step 1 is far from sharp; it is only the first step of an induction.

(d) False. The matrix \( \N \) in the warning after @thm-birkhoff lies in \( \Omega_3 \) and has \( 5 = 2 \cdot 3 - 1 \) non-zero entries, but it is not a permutation matrix.

(e) True. If \( \A, \B \in \Omega_n \), the entries of \( \A\B \) are sums of products of non-negative numbers, and \( \A\B\1 = \A\1 = \1 \), \( \1\tp\A\B = \1\tp\B = \1\tp \).

(f) True, by @cor-birkhoff-convex-combination with \( n = 3 \): \( (3-1)^2 + 1 = 5 \).
:::

### B. Practice

:::: {#exr-birkhoff-b1}
[B1: Which are corners?]

For each matrix, determine whether it lies in \( \Omega_3 \) and, if so, whether it is an extreme point of \( \Omega_3 \). Justify your answers.
\[
\begin{aligned}
\M_1 &= \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} , &\quad
\M_2 &= \frac12\begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix} , \\
\M_3 &= \frac12\begin{pmatrix} 2 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix} , &\quad
\M_4 &= \begin{pmatrix} 1 & 1 & -1 \\ 0 & 0 & 1 \\ 0 & 0 & 1 \end{pmatrix} .
\end{aligned}
\]
::::

::: {.solution}
\( \M_1 \) has exactly one \( 1 \) in each row and each column and zeros elsewhere, so it is a permutation matrix, in \( \Omega_3 \) and extreme by @prp-permutation-matrices-extreme.

\( \M_2 \) has non-negative entries and every row and column of \( 2\M_2 \) adds up to \( 2 \), so \( \M_2 \in \Omega_3 \). It is not a permutation matrix, so by @thm-birkhoff it is not extreme. Explicitly, \( \M_2 = \tfrac12\I + \tfrac12\P \) with \( \P \) the permutation matrix with \( 1 \)'s at \( (1,2), (2,3), (3,1) \), and \( \I \ne \P \).

\( \M_3 \) is not in \( \Omega_3 \): its rows add up to \( 1, 1, \tfrac12 \).

\( \M_4 \) is not in \( \Omega_3 \): its rows and columns add up to \( 1 \) (rows \( 1, 1, 1 \); columns \( 1, 1, 1 \)), but the entry \( -1 \) is negative. It is in the coset \( \tfrac13\J + W_3 \) of the proof of @cor-birkhoff-convex-combination, which shows that the non-negativity conditions matter.
:::

:::: {#exr-birkhoff-b2}
[B2: Peeling a 3 × 3 matrix]

Let
\[
\M = \frac16\begin{pmatrix} 3 & 3 & 0 \\ 1 & 2 & 3 \\ 2 & 1 & 3 \end{pmatrix} .
\]
Check that \( \M \in \Omega_3 \), and write \( \M \) as a convex combination of permutation matrices by peeling. Hence confirm the bound of @cor-birkhoff-convex-combination for this \( \M \).
::::

::: {.solution}
The entries are non-negative; the rows of \( 6\M \) add up to \( 3 + 3 + 0 \), \( 1 + 2 + 3 \), \( 2 + 1 + 3 \), and the columns to \( 3 + 1 + 2 \), \( 3 + 2 + 1 \), \( 0 + 3 + 3 \), all \( 6 \). So \( \M \in \Omega_3 \). Peel \( \N = 6\M \).

*Round 1.* The diagonal \( 3, 2, 3 \) is positive; subtract \( 2\I \):
\[
\begin{pmatrix} 1 & 3 & 0 \\ 1 & 0 & 3 \\ 2 & 1 & 1 \end{pmatrix} \quad (\text{sums } 4) .
\]

*Round 2.* The positions \( (3,1), (1,2), (2,3) \) carry \( 2, 3, 3 \); subtract \( 2\P_1 \), where \( \P_1 \) has its \( 1 \)'s there:
\[
\begin{pmatrix} 1 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{pmatrix} \quad (\text{sums } 2) .
\]

*Round 3.* The positions \( (1,1), (3,2), (2,3) \) carry \( 1, 1, 1 \); subtract \( \P_2 \), with \( 1 \)'s there. What remains has \( 1 \)'s at \( (2,1), (1,2), (3,3) \): a permutation matrix \( \P_3 \), with weight \( 1 \).

So \( 6\M = 2\I + 2\P_1 + \P_2 + \P_3 \) and
\[
\M = \tfrac13\,\I + \tfrac13\,\P_1 + \tfrac16\,\P_2 + \tfrac16\,\P_3 ,
\]
with weights non-negative and adding up to \( 1 \). Hence \( \M \) uses four permutation matrices, within the bound \( (3-1)^2 + 1 = 5 \).
:::

:::: {#exr-birkhoff-b3}
[B3: Schur's theorem by averaging]

Let \( \A = \begin{pmatrix} 4 & 2 \\ 2 & 1 \end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Find \( \vlambda(\A) \) and an orthogonal \( \U \) with \( \A = \U\diag(\vlambda(\A))\U\tp \).
2. Compute \( \S = (u_{ij}^2) \) and check that \( \d(\A) = \S\vlambda(\A) \).
3. Write \( \S \) as a convex combination of permutation matrices, and hence \( \d(\A) \) as an average of rearrangements of \( \vlambda(\A) \). Confirm \( \d(\A) \prec \vlambda(\A) \) from @def-majorization.
:::
::::

::: {.solution}
(a) \( \A(2, 1) = (10, 5) = 5(2, 1) \) and \( \A(1, -2) = (0, 0) \), so \( \vlambda(\A) = (5, 0) \). With the unit eigenvectors \( \tfrac{1}{\sqrt5}(2, 1) \) and \( \tfrac{1}{\sqrt5}(1, -2) \) as columns,
\[
\U = \frac{1}{\sqrt5}\begin{pmatrix} 2 & 1 \\ 1 & -2 \end{pmatrix} ,
\]
which is orthogonal, and \( \A = \U\diag(5, 0)\U\tp \) by @cor-spectral-real-matrix.

(b) \( \S = \tfrac15\begin{pmatrix} 4 & 1 \\ 1 & 4 \end{pmatrix} \), and \( \S(5, 0) = (4, 1) = \d(\A) \).

(c) \( \S = \tfrac45\I + \tfrac15\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \), so \( \d(\A) = \tfrac45(5, 0) + \tfrac15(0, 5) = (4, 1) \). Directly: both vectors are decreasing, the totals are \( 5 = 5 \), and at \( k = 1 \), \( 4 \le 5 \). So \( \d(\A) \prec \vlambda(\A) \).
:::

### C. Going deeper

:::: {#exr-birkhoff-c1}
[C1: Five permutation matrices can be needed]

Let \( \P \) be the permutation matrix of the \( 3 \)-cycle \( 1 \mapsto 2 \mapsto 3 \mapsto 1 \), and let \( \T_{12}, \T_{13}, \T_{23} \) be those of the transpositions \( (1\ 2), (1\ 3), (2\ 3) \). The six permutation matrices of size \( 3 \) are \( \I, \P, \P^2 \) (the **even** ones) and \( \T_{12}, \T_{13}, \T_{23} \) (the **odd** ones).

::: {.enumerate options="label=(\alph*)"}
1. Show that each of the nine positions \( (i, j) \) holds a \( 1 \) in exactly one even and exactly one odd permutation matrix, and that each even and each odd permutation matrix share exactly one position of a \( 1 \).
2. Deduce that if \( \sum_\sigma c_\sigma\P_\sigma = \0 \) for real numbers \( c_\sigma \), then \( c_\sigma = c \) for the even \( \sigma \) and \( c_\sigma = -c \) for the odd \( \sigma \), for some \( c \in \nR \).
3. Let \( \M = \tfrac{1}{15}\bigl(\I + 2\P + 3\P^2 + 4\T_{12} + 5\T_{13}\bigr) \). Show that every way of writing \( \M \) as a convex combination of permutation matrices uses at least five of them with positive weight.
:::

*Hint: in (a), a permutation of \( \{1, 2, 3\} \) is determined by where it sends any two points.*
::::

::: {.solution}
(a) A permutation matrix \( \P_\sigma \) has a \( 1 \) in position \( (i, j) \) exactly when \( \sigma(j) = i \). The permutations of \( \{1, 2, 3\} \) with \( \sigma(j) = i \) are determined by where they send the other two points, which must go to the other two values in one of two ways, so there are exactly two. If \( \sigma \) is one of them, the other is \( \tau\sigma \), with \( \tau \) the transposition exchanging the two remaining values, so their signs are opposite (@def-sign-permutation, @thm-sign-multiplicative): one is even and one is odd. For the second claim, let \( \sigma \) be even and \( \tau \) odd. They cannot agree at all three points, since they differ; they cannot agree at exactly two, since two agreements force the third; and if they agreed nowhere, \( \tau^{-1}\sigma \) would fix no point and so be a \( 3 \)-cycle, which is even, while \( \tau^{-1}\sigma \) is odd. So they agree at exactly one point \( j \), that is, they share exactly one position \( (\sigma(j), j) \).

(b) Look at position \( (i, j) \): by (a) exactly one even \( \sigma \) and one odd \( \tau \) have a \( 1 \) there, so the equation gives \( c_\sigma + c_\tau = 0 \). By (a) again, every pair of an even \( \sigma \) and an odd \( \tau \) arises in this way at their shared position, so \( c_\sigma = -c_\tau \) for every such pair. Fixing one odd \( \tau \), all even \( c_\sigma \) equal \( c = -c_\tau \), and then every odd \( c_{\tau'} = -c \).

(c) The given weights are \( \tfrac{1}{15}(1, 2, 3) \) on \( \I, \P, \P^2 \) and \( \tfrac{1}{15}(4, 5, 0) \) on \( \T_{12}, \T_{13}, \T_{23} \); they are non-negative with sum \( 1 \). If \( \M = \sum_\sigma t_\sigma\P_\sigma \) is any other convex combination, the difference of the two weight lists satisfies (b), so the even weights are \( \tfrac{1}{15}(1, 2, 3) + s \) and the odd ones \( \tfrac{1}{15}(4, 5, 0) - s \) for some real \( s \). Non-negativity needs \( s \ge -\tfrac1{15} \) (from \( \I \)) and \( s \le 0 \) (from \( \T_{23} \)). For \( -\tfrac1{15} < s < 0 \), all six weights are positive. At \( s = 0 \) exactly one vanishes, that of \( \T_{23} \); at \( s = -\tfrac1{15} \) exactly one vanishes, that of \( \I \), the others being \( \tfrac{1}{15}(1, 2) \) and \( \tfrac{1}{15}(5, 6, 1) \). So every representation has at least five positive weights, and the bound \( (3 - 1)^2 + 1 = 5 \) of @cor-birkhoff-convex-combination is attained.
:::

:::: {#exr-birkhoff-c2}
[C2: Integer matrices with equal line sums]

Let \( k \ge 1 \), and let \( \N \in M_n(\nR) \) have non-negative **integer** entries, with every row and every column adding up to \( k \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \N \) is a sum of \( k \) permutation matrices, not necessarily distinct.
2. Carry this out for \( \N = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 1 & 2 \\ 1 & 1 & 1 \end{pmatrix} \).
:::

*Hint: apply @cor-doubly-stochastic-positive-diagonal to \( \tfrac1k\N \).*
::::

::: {.solution}
(a) By induction on \( k \). The matrix \( \tfrac1k\N \) is doubly stochastic, so by @cor-doubly-stochastic-positive-diagonal there is \( \sigma \) with \( n_{\sigma(j)j} > 0 \) for every \( j \). These are positive integers, so each is at least \( 1 \), and \( \N - \P_\sigma \) has non-negative integer entries with every row and column adding up to \( k - 1 \). If \( k = 1 \), then \( \N - \P_\sigma \) has line sums \( 0 \) and non-negative entries, so it is \( \0 \) and \( \N = \P_\sigma \). If \( k \ge 2 \), the induction hypothesis writes \( \N - \P_\sigma \) as a sum of \( k - 1 \) permutation matrices, and adding \( \P_\sigma \) gives \( k \).

(b) Every row and column adds up to \( 3 \). The diagonal \( 2, 1, 1 \) is positive; subtracting \( \I \) leaves
\[
\begin{pmatrix} 1 & 1 & 0 \\ 0 & 0 & 2 \\ 1 & 1 & 0 \end{pmatrix} .
\]
The positions \( (1,1), (3,2), (2,3) \) are positive; subtracting that permutation matrix leaves the permutation matrix with \( 1 \)'s at \( (3,1), (1,2), (2,3) \). So \( \N \) is \( \I \) plus these two permutation matrices.
:::

:::: {#exr-birkhoff-c3}
[C3: The dimension, and a matrix that is not unistochastic]

Let \( n \ge 2 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( \X \in W_n \) has every \( \lvert x_{ij}\rvert \le \tfrac1n \), then \( \tfrac1n\J + \X \in \Omega_n \). Deduce that \( \operatorname{aff}\Omega_n = \tfrac1n\J + W_n \) and \( \dim\Omega_n = (n-1)^2 \).
2. Show that \( \M = \tfrac12\begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix} \) is doubly stochastic but is not of the form \( (\lvert u_{ij}\rvert^2) \) for any unitary \( \U \in M_3(\nC) \).
:::

*Hint for (b): two columns of \( \U \) must be orthogonal; look at which rows both can be non-zero in.*
::::

::: {.solution}
(a) The entries of \( \tfrac1n\J + \X \) are \( \tfrac1n + x_{ij} \ge \tfrac1n - \tfrac1n = 0 \), and its rows and columns add up to \( 1 + 0 = 1 \), since \( \X \in W_n \). So it lies in \( \Omega_n \). The proof of @cor-birkhoff-convex-combination showed \( \Omega_n \subseteq \tfrac1n\J + W_n \), a coset, which is an affine set containing \( \Omega_n \), so \( \operatorname{aff}\Omega_n \subseteq \tfrac1n\J + W_n \). Conversely, let \( \X \in W_n \), \( \X \ne \0 \), and put \( c = n\max_{i,j}\lvert x_{ij}\rvert > 0 \). Then \( \tfrac1n\J \) and \( \tfrac1n\J + \tfrac1c\X \) lie in \( \Omega_n \), and the affine combination
\[
\tfrac1n\J + \X = (1 - c)\,\tfrac1n\J + c\,\bigl(\tfrac1n\J + \tfrac1c\X\bigr)
\]
lies in \( \operatorname{aff}\Omega_n \). So \( \operatorname{aff}\Omega_n = \tfrac1n\J + W_n \), and \( \dim\Omega_n = \dim W_n = (n-1)^2 \) by @lem-doubly-stochastic-sum-conditions (a).

(b) The entries are non-negative and every row and column adds up to \( 1 \). Suppose \( \M = (\lvert u_{ij}\rvert^2) \) with \( \U \) unitary. The zero entries \( m_{13} = m_{21} = m_{32} = 0 \) force \( u_{13} = u_{21} = u_{32} = 0 \). Columns \( 1 \) and \( 2 \) of \( \U \) are \( (u_{11}, 0, u_{31}) \) and \( (u_{12}, u_{22}, 0) \), and they are orthogonal because \( \U \) is unitary:
\[
0 = u_{11}\conj{u_{12}} + 0 \cdot \conj{u_{22}} + u_{31} \cdot 0 = u_{11}\conj{u_{12}} .
\]
But \( \lvert u_{11}\rvert^2 = \lvert u_{12}\rvert^2 = \tfrac12 \), so \( u_{11}\conj{u_{12}} \ne 0 \), a contradiction. Hence \( \M \) is not unistochastic.
:::
