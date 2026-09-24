# Matrix Games and the Minimax Theorem

Chapter 17 was built on a min–max formula: the Courant–Fischer theorem describes each eigenvalue of a Hermitian matrix as a minimum of maxima over subspaces. This section proves a second min–max theorem that looks similar and works for a completely different reason. It concerns a game in which two players choose simultaneously, and it says that if the players are allowed to **randomize**, it does not matter which of them has to reveal a plan first. The theorem is due to von Neumann, and with linear programming duality in hand (§06) it takes a page to prove.

The two theorems are easy to confuse, and a reader who has just finished Chapter 17 will be tempted to. So the section also says precisely how they differ. Courant–Fischer is a statement about **subspaces**, and its equality comes from a **dimension count**. The minimax theorem is a statement about **simplices**, and its equality comes from **convexity**.

**Throughout, the field is \( \nR \)**, \( \1 \) is the all-ones vector of whatever length the context requires, and \( \J = \1\1\tp \) is the all-ones matrix. Inequalities between vectors are entrywise, as in §05.

## Matrix games

Two players, Row and Column, play a game described by a real matrix \( \A \in M_{m \times n}(\nR) \), the **payoff matrix**. Row secretly chooses a row \( i \), Column secretly chooses a column \( j \), both reveal their choices, and Column pays Row the amount \( a_{ij} \). A negative entry means that Row pays Column. Whatever one player wins, the other loses, so the game is called **zero-sum**. Row wants \( a_{ij} \) large and Column wants it small. A choice of a row, or of a column, is a **pure strategy**.

Suppose Row must announce a row in advance. Column will then answer with the smallest entry in that row, so the best Row can guarantee is
\[
\max_{i}\ \min_{j}\ a_{ij} .
\]
If instead Column must announce first, the best Column can guarantee is to pay at most \( \min_j \max_i a_{ij} \). Announcing first is never an advantage, and that holds for any payoff function whatsoever.

::: {#lem-max-min-le-min-max}
[Max–Min Never Exceeds Min–Max]

Let \( X \) and \( Y \) be sets and \( f \colon X \times Y \to \nR \) a function for which the extrema below exist. Then
\[
\max_{x \in X}\ \min_{y \in Y}\ f(x, y) \ \le\ \min_{y \in Y}\ \max_{x \in X}\ f(x, y) .
\]
:::

::: {.proof}
Let \( x_0 \in X \) and \( y_0 \in Y \). Then
\[
\min_{y \in Y} f(x_0, y) \ \le\ f(x_0, y_0) \ \le\ \max_{x \in X} f(x, y_0) .
\]
The left side does not depend on \( y_0 \) and the right side does not depend on \( x_0 \). Taking the maximum over \( x_0 \) on the left and then the minimum over \( y_0 \) on the right proves the lemma.
:::

The inequality can be strict. In the game with
\[
\A = \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix} ,
\]
Row wins when the two choices match and loses when they differ. Every row contains a \( -1 \), so \( \max_i\min_j a_{ij} = -1 \). Every column contains a \( 1 \), so \( \min_j\max_i a_{ij} = 1 \). Whoever announces first loses a unit, and there is a gap of \( 2 \) between what the players can guarantee.

Some games have no gap. In
\[
\A = \begin{pmatrix} 3 & 1 & 4 \\ 2 & 0 & 1 \end{pmatrix}
\]
the row minima are \( 1 \) and \( 0 \), whose maximum is \( 1 \), and the column maxima are \( 3, 1, 4 \), whose minimum is also \( 1 \). The entry \( a_{12} = 1 \) is the smallest in its row and the largest in its column. Such an entry is a **saddle point**. If Row plays row 1 and Column plays column 2, neither can gain by changing unilaterally, and the game is settled in pure strategies. The first game has no saddle point, and in that game the natural advice is: do not be predictable.

## Mixed strategies

The way to be unpredictable is to randomize. Row chooses row \( i \) with probability \( x_i \), and Column chooses column \( j \) with probability \( y_j \), independently. The probabilities of the \( m \) rows form a vector with non-negative entries summing to \( 1 \), that is, a point of the standard simplex of @def-standard-simplex,
\[
\Delta_m = \{ \x \in \nR^m : \x \ge \0 \text{ and } x_1 + \dots + x_m = 1 \} .
\]

*A mixed strategy is a probability distribution over the pure strategies, and the simplex is the set of all of them.*

::: {#def-mixed-strategy}
[Mixed Strategy]

In the game with payoff matrix \( \A \in M_{m \times n}(\nR) \), a **mixed strategy** for Row is a vector \( \x \in \Delta_m \), a mixed strategy for Column is a vector \( \y \in \Delta_n \), and the **expected payoff** is
\[
\x\tp\A\y = \sum_{i=1}^{m}\sum_{j=1}^{n} x_i\,a_{ij}\,y_j .
\]
:::

In words: a mixed strategy assigns to each pure strategy a weight that is **non-negative**, and the weights **sum to exactly** \( 1 \). The payoff \( a_{ij} \) occurs with probability \( x_iy_j \), since the two choices are independent, so \( \x\tp\A\y \) is the average payoff over many plays. The pure strategy "row \( i \)" is the mixed strategy \( \e_i \), a vertex of the simplex, and \( \e_i\tp\A\e_j = a_{ij} \). So mixed strategies extend pure ones, and the expected payoff extends the payoff.

**Examples.** \( \Delta_2 \) is the segment from \( (1, 0) \) to \( (0, 1) \) in the plane, whose points \( (p, 1 - p) \) with \( 0 \le p \le 1 \) mean "row 1 with probability \( p \)". \( \Delta_3 \) is the triangle with vertices \( \e_1, \e_2, \e_3 \) in \( \nR^3 \), and its center \( \tfrac13\1 \) is the uniform strategy. The degenerate case is \( \Delta_1 = \{1\} \): a player with only one pure strategy has no choice, and the game is a single row or a single column.

**Non-examples by minimal change.** \( \bigl(\tfrac12, \tfrac12, \tfrac12\bigr) \) has non-negative entries, but they sum to \( \tfrac32 \), so it is not a probability distribution. \( \bigl(\tfrac32, -\tfrac12\bigr) \) sums to \( 1 \), but it has a negative entry. It lies on the line through \( \Delta_2 \), outside the segment.

**Why this definition.** \( \Delta_n \) is exactly the set of convex combinations of \( \e_1, \dots, \e_n \), since \( \x = \sum x_j\e_j \). So it is the convex hull of the pure strategies, by @thm-convex-hull-combinations, and in particular it is a convex set (@def-convex-set). That convexity is what makes the theorem below true. The convention of @def-standard-simplex, \( n \) weights for \( n \) pure strategies, is the one a game needs. The payoff \( \x\tp\A\y \) is linear in \( \y \) for fixed \( \x \), and linear in \( \x \) for fixed \( \y \), so a mixture of strategies earns the same mixture of payoffs.

::: {.warning}
**A mixed strategy is not a compromise move.** Playing \( \bigl(\tfrac12, \tfrac12\bigr) \) in the matching game does not mean playing "half of row 1 and half of row 2" in a single round. Each round Row plays one actual row, chosen at random, and \( \x\tp\A\y \) is an average over rounds. In the matching game with \( \x = \y = \bigl(\tfrac12, \tfrac12\bigr) \), the expected payoff is \( 0 \), yet every single round pays \( +1 \) or \( -1 \), never \( 0 \).
:::

Against a fixed mixed strategy, the opponent never needs to randomize. That observation turns every "min over a simplex" into a min over finitely many numbers.

::: {#lem-pure-best-response}
[A Pure Best Response Exists]

Let \( \A \in M_{m \times n}(\nR) \). For every \( \x \in \Delta_m \),
\[
\min_{\y \in \Delta_n} \x\tp\A\y = \min_{1 \le j \le n} (\A\tp\x)_j ,
\]
and the minimum on the left is attained at \( \y = \e_j \) for any \( j \) attaining the minimum on the right. Likewise, for every \( \y \in \Delta_n \), \( \max_{\x \in \Delta_m}\x\tp\A\y = \max_{1 \le i \le m}(\A\y)_i \), attained at a vertex \( \e_i \).
:::

::: {.idea}
For fixed \( \x \), the payoff \( \x\tp\A\y \) is an average of the entries of \( \A\tp\x \) with weights \( y_j \), and an average is never below the smallest entry, which the vertex \( \e_j \) attains.
:::

::: {.proof}
Write \( \w = \A\tp\x \in \nR^n \) and \( \mu = \min_j w_j \), a minimum of finitely many numbers. For \( \y \in \Delta_n \),
\[
\x\tp\A\y = \w\tp\y = \sum_{j=1}^{n} y_jw_j \ \ge\ \sum_{j=1}^{n} y_j\mu = \mu ,
\]
because every \( y_j \ge 0 \) and \( \sum_j y_j = 1 \). If \( w_{j_0} = \mu \), then \( \e_{j_0} \in \Delta_n \) gives \( \x\tp\A\e_{j_0} = w_{j_0} = \mu \). So \( \mu \) is a value of \( \y \mapsto \x\tp\A\y \) on \( \Delta_n \) and a lower bound for all its values, hence its minimum. The second statement is the same argument applied to \( \A\y \) with the inequality reversed.
:::

So once Row fixes \( \x \), the amount Row can **guarantee** is
\[
g(\x) = \min_{\y \in \Delta_n}\x\tp\A\y = \min_j (\A\tp\x)_j ,
\]
the smallest entry of \( \A\tp\x \). Column, in the same way, guarantees by the second half of the lemma to pay at most \( h(\y) = \max_{\x \in \Delta_m}\x\tp\A\y = \max_i(\A\y)_i \). In the matching game, \( \x = \bigl(\tfrac12, \tfrac12\bigr) \) gives \( \A\tp\x = (0, 0) \) and \( g(\x) = 0 \), and the same holds for Column's \( h \). With mixing, both players can guarantee \( 0 \), and the gap of \( 2 \) has closed. The theorem says this always happens.

## The minimax theorem

::: {#thm-von-neumann-minimax}
[Von Neumann's Minimax Theorem]

Let \( \A \in M_{m \times n}(\nR) \). There are \( \x^{\star} \in \Delta_m \), \( \y^{\star} \in \Delta_n \) and \( v \in \nR \) such that
\[
\x\tp\A\y^{\star} \ \le\ v \ \le\ \x^{\star\top}\A\y \qquad \text{for all } \x \in \Delta_m,\ \y \in \Delta_n .
\]{#eq-minimax-saddle}
Consequently
\[
\max_{\x \in \Delta_m}\ \min_{\y \in \Delta_n}\ \x\tp\A\y
\ =\ v\ =\
\min_{\y \in \Delta_n}\ \max_{\x \in \Delta_m}\ \x\tp\A\y ,
\]
where the outer maximum is attained at \( \x^{\star} \) and the outer minimum at \( \y^{\star} \).
:::

::: {.idea}
Row wants the \( \x \in \Delta_m \) that maximizes the smallest entry of \( \A\tp\x \). If every entry of \( \A \) is positive, this can be rescaled into a linear program. Put \( \p = \x/v \), where \( v \) is the guaranteed amount. Then "\( \A\tp\x \ge v\1 \) with \( \1\tp\x = 1 \), \( v \) as large as possible" becomes "\( \A\tp\p \ge \1 \), \( \p \ge \0 \), \( \1\tp\p \) as small as possible". Column's problem becomes the dual of that program, by the same substitution. Strong duality (§06) says the two optimal values agree, and that common value is \( 1/v \). The plan:

① shift the entries by a constant to make them positive, which changes every payoff by the same constant;
② write down the two linear programs, check that both are feasible, and apply @thm-strong-duality;
③ rescale the optimal solutions into strategies and read off @eq-minimax-saddle.
:::

::: {.proof}
**Step 1. We may assume every \( a_{ij} > 0 \).** Choose \( c \in \nR \) with \( a_{ij} + c > 0 \) for all \( i, j \), and put \( \B = \A + c\J \). For \( \x \in \Delta_m \) and \( \y \in \Delta_n \),
\[
\x\tp\J\y = (\x\tp\1)(\1\tp\y) = 1 ,
\qquad\text{so}\qquad
\x\tp\B\y = \x\tp\A\y + c .
\]
Hence if \( \x^{\star}, \y^{\star}, w \) satisfy @eq-minimax-saddle for \( \B \), then \( \x^{\star}, \y^{\star}, w - c \) satisfy it for \( \A \). So it suffices to prove @eq-minimax-saddle when every entry of \( \A \) is positive, and we assume this from now on. Let \( \mu = \min_{i,j}a_{ij} > 0 \).

**Step 2. Two linear programs.** Consider
\[
\begin{aligned}
\text{(P)}\quad & \text{maximize } \1\tp\q \ \text{ subject to } \ \A\q \le \1,\ \q \ge \0 \quad (\q \in \nR^n), \\
\text{(D)}\quad & \text{minimize } \1\tp\p \ \text{ subject to } \ \A\tp\p \ge \1,\ \p \ge \0 \quad (\p \in \nR^m) .
\end{aligned}
\]
(P) is a linear program in the inequality form of @def-linear-program, with data \( (\A, \1, \1) \), and (D) is its dual (@def-dual-program). (P) is feasible, with \( \q = \0 \). (D) is feasible, with \( \p = \mu^{-1}\1 \): the \( j \)-th entry of \( \A\tp\p \) is \( \mu^{-1}\sum_i a_{ij} \ge \mu^{-1}a_{1j} \ge 1 \). By @thm-strong-duality (a), there are optimal \( \q^{\star} \) and \( \p^{\star} \) with equal values; call the common value \( \omega \), so that
\[
\1\tp\q^{\star} = \1\tp\p^{\star} = \omega .
\]
Moreover \( \omega > 0 \). Since \( \A\tp\p^{\star} \ge \1 \), we have \( \p^{\star} \ne \0 \), and a non-zero vector with non-negative entries has a positive entry sum.

**Step 3. Strategies from the programs.** Put
\[
\x^{\star} = \omega^{-1}\p^{\star}, \qquad \y^{\star} = \omega^{-1}\q^{\star}, \qquad v = \omega^{-1} .
\]
Then \( \x^{\star} \ge \0 \) with \( \1\tp\x^{\star} = \omega^{-1}\omega = 1 \), so \( \x^{\star} \in \Delta_m \), and likewise \( \y^{\star} \in \Delta_n \). The constraints of the two programs give
\[
\A\tp\x^{\star} = \omega^{-1}\A\tp\p^{\star} \ge v\1 ,
\qquad
\A\y^{\star} = \omega^{-1}\A\q^{\star} \le v\1 .
\]
For every \( \y \in \Delta_n \), therefore, \( \x^{\star\top}\A\y = \sum_j y_j(\A\tp\x^{\star})_j \ge v\sum_j y_j = v \). For every \( \x \in \Delta_m \), \( \x\tp\A\y^{\star} = \sum_i x_i(\A\y^{\star})_i \le v \). This is @eq-minimax-saddle.

**Step 4. The two extrema.** For \( \x \in \Delta_m \) let \( g(\x) = \min_{\y \in \Delta_n}\x\tp\A\y \), which exists by @lem-pure-best-response. By @eq-minimax-saddle, \( g(\x^{\star}) \ge v \), since every value of \( \y \mapsto \x^{\star\top}\A\y \) is at least \( v \). And \( g(\x) \le \x\tp\A\y^{\star} \le v \) for every \( \x \). So \( v \) is a value of \( g \) and an upper bound for all its values: \( \max_{\x}g(\x) \) exists, equals \( v \), and is attained at \( \x^{\star} \). In the same way \( h(\y) = \max_{\x}\x\tp\A\y \) satisfies \( h(\y^{\star}) \le v \le \x^{\star\top}\A\y \le h(\y) \) for every \( \y \), so \( \min_{\y}h(\y) = v \), attained at \( \y^{\star} \). This proves the theorem.
:::

::: {#def-value-of-game}
[Value and Optimal Strategies]

The number \( v \) of @thm-von-neumann-minimax is the **value** of the game with payoff matrix \( \A \), written \( v(\A) \). A strategy \( \x \in \Delta_m \) is **optimal for Row** if it guarantees the value, \( \min_{\y}\x\tp\A\y = v(\A) \), and \( \y \in \Delta_n \) is **optimal for Column** if \( \max_{\x}\x\tp\A\y = v(\A) \).
:::

The value is well defined: it equals the max–min, and that depends only on \( \A \). A strategy \( \x \) is optimal for Row exactly when every entry of \( \A\tp\x \) is at least \( v(\A) \), and \( \y \) is optimal for Column exactly when every entry of \( \A\y \) is at most \( v(\A) \); both statements are @lem-pure-best-response. These are linear conditions, so each player's set of optimal strategies is a convex subset of the simplex. Inequality @eq-minimax-saddle says that \( (\x^{\star}, \y^{\star}) \) is a **saddle point in mixed strategies**. If Row plays \( \x^{\star} \), Column cannot push the expected payment below \( v \). If Column plays \( \y^{\star} \), Row cannot push it above \( v \). Neither player gains by deviating alone, and announcing an optimal strategy in advance costs nothing.

Alternatively, the theorem can be proved with no linear programming, by separation. The key fact is an alternative in the style of Farkas: either some \( \y \in \Delta_n \) has \( \A\y \le \0 \), or some \( \x \in \Delta_m \) has \( \A\tp\x > \0 \). To prove it, separate the origin from the closed convex set \( \{ \A\y + \z : \y \in \Delta_n,\ \z \ge \0 \} \) using §03, and apply the result to \( \A - t\J \) for every real \( t \). That route shows most directly that the theorem is about convexity. It also needs the compactness of \( \Delta_n \), (A3) of Chapter 16's introduction, to know that the set being separated is closed. The route taken above hides all of the analysis inside Farkas's lemma.

## Two min–max theorems

@thm-von-neumann-minimax and the Courant–Fischer theorem of Chapter 17 (@thm-courant-fischer) both have "min" and "max" in them, and both are called min–max theorems. They are different theorems, with different proofs. Put side by side, for a Hermitian \( \A \in M_n(F) \) (\( F = \nR \) or \( \nC \)) and a real \( \B \in M_{m \times n}(\nR) \):
\[
\begin{aligned}
\lambda_k(\A) &= \min_{\dim W = n-k+1}\ \max_{\0 \ne \x \in W} R_{\A}(\x) \\
&= \max_{\dim W = k}\ \min_{\0 \ne \x \in W} R_{\A}(\x) , \\[4pt]
v(\B) &= \min_{\y \in \Delta_n}\ \max_{\x \in \Delta_m} \x\tp\B\y \\
&= \max_{\x \in \Delta_m}\ \min_{\y \in \Delta_n} \x\tp\B\y .
\end{aligned}
\]

**What is being chosen.** In Courant–Fischer the outer variable is a **subspace** \( W \), and the inner variable is a vector **inside that subspace**. The inner set depends on the outer choice, so the formula is a nested optimization, not a game between two independent players. In von Neumann's theorem the two variables range over **fixed** sets, \( \Delta_m \) and \( \Delta_n \), neither of which depends on the other.

**What the theorem asserts.** Von Neumann's theorem is an **exchange of order**: the same function, with the max and the min taken in both orders, gives the same number. Courant–Fischer exchanges nothing. Its two forms use different dimensions, \( n - k + 1 \) and \( k \), and swapping the order while keeping the dimension gives \( \lambda_{n+1-k}(\A) \), which differs from \( \lambda_k(\A) \) unless \( n = 2k - 1 \) or the two eigenvalues happen to be equal (the warning after @thm-courant-fischer). The sharpest contrast is in the inequality between the two forms. In von Neumann's theorem, "max–min \( \le \) min–max" is @lem-max-min-le-min-max, and it is free for every function. In Courant–Fischer the corresponding inequality
\[
\max_{\dim W = k}\ \min_{\0 \ne \x \in W} R_{\A}(\x)
\ \le\
\min_{\dim W' = n-k+1}\ \max_{\0 \ne \x \in W'} R_{\A}(\x)
\]
is **not** free: it is exactly the dimension count. Since \( k + (n - k + 1) > n \), any \( W \) of dimension \( k \) meets any \( W' \) of dimension \( n - k + 1 \) in a non-zero vector \( \x \) (@lem-subspace-intersection), and then \( \min_{W} R_{\A} \le R_{\A}(\x) \le \max_{W'} R_{\A} \).

**Where the equality comes from.** In Courant–Fischer it is a **dimension count**. Any subspace of dimension \( n - k + 1 \) must meet the span of the top \( k \) eigenvectors, by @lem-subspace-intersection, and on the shared vector the Rayleigh quotient is pinned. Convexity plays no role: the subspaces of dimension \( n - k + 1 \) do not form a convex set in any sense used here, and \( R_{\A} \) is not linear. In von Neumann's theorem it is **convexity**. The strategy sets are simplices, the payoff is linear in each variable separately, and the equality is linear programming duality, which is Farkas's lemma, which is a separating hyperplane. No dimension is counted anywhere.

**What they need.** Courant–Fischer needs a Hermitian matrix, since the spectral theorem supplies the eigenvectors that are its witnesses. Von Neumann's theorem holds for **every** real matrix, square or not.

**How each fails when its key ingredient is removed.** Replace the simplices by the finite sets of pure strategies, which are not convex, and von Neumann's equality fails, as in the matching game above. Replace the dimension \( n - k + 1 \) by \( n - k \), which is possible when \( k < n \), so that the dimension count no longer forces an intersection, and Courant–Fischer's formula returns \( \lambda_{k+1}(\A) \) instead of \( \lambda_k(\A) \).

## Solving a game

::: {#exm-game-two-by-three}
[A game with an unused column]

Find the value and optimal strategies for the game with payoff matrix
\[
\A = \begin{pmatrix} 3 & -1 & 2 \\ -2 & 4 & 0 \end{pmatrix} .
\]
:::

::: {.solution}
*No saddle point.* The row minima are \( -1 \) and \( -2 \), so \( \max_i\min_j a_{ij} = -1 \). The column maxima are \( 3, 4, 2 \), so \( \min_j\max_i a_{ij} = 2 \). The two differ, so both players must mix.

*Row's side.* Write \( \x = (p, 1 - p) \) with \( 0 \le p \le 1 \). Then
\[
\A\tp\x = \bigl(5p - 2,\ 4 - 5p,\ 2p\bigr) ,
\]
and by @lem-pure-best-response Row guarantees \( g(p) = \min\{5p - 2,\ 4 - 5p,\ 2p\} \). The graph of \( g \) is the lower envelope of three lines.

\begin{center}
\begin{tikzpicture}[xscale=5, yscale=0.7, lab/.style={font=\small}]
  \draw[->, gray] (0,0) -- (1.12,0) node[right, black, lab] {$p$};
  \draw[->, gray] (0,-2.3) -- (0,4.4);
  \foreach \t in {-2,-1,1,2,3,4} \draw[gray] (-0.015,\t) -- (0.015,\t) node[left=3pt, black, lab] {$\t$};
  \draw[gray] (1,-0.1) -- (1,0.1) node[above, black, lab] {$1$};
  \draw[thin] (0,-2) -- (1,3) node[right, lab] {col.~1: $5p-2$};
  \draw[thin] (0,4) -- (1,-1) node[right, lab] {col.~2: $4-5p$};
  \draw[thin, dashed] (0,0) -- (1,2) node[right, lab] {col.~3: $2p$};
  \draw[ultra thick] (0,-2) -- (0.6,1) -- (1,-1);
  \draw[dotted] (0.6,0) -- (0.6,1);
  \fill (0.6,1) ellipse (0.012 and 0.085);
  \draw[gray, thin] (0.6,1.12) -- (0.6,2.7) node[above, black, lab] {$(3/5,\ 1)$};
  \node[lab, below] at (0.6,0) {$3/5$};
  \node[lab, align=center] at (0.5,-3.5)
    {Row's guarantee $g(p)$ is the lower envelope (thick). It is highest at $p = 3/5$,\\
     where columns 1 and 2 cross at height $1$. The dashed line never touches it};
\end{tikzpicture}
\end{center}

For \( p \le \tfrac35 \) the first line is the lowest: \( 5p - 2 \le 4 - 5p \) exactly when \( p \le \tfrac35 \), and \( 5p - 2 \le 2p \) exactly when \( p \le \tfrac23 \). For \( p \ge \tfrac35 \) the second line is the lowest: \( 4 - 5p \le 2p \) exactly when \( p \ge \tfrac47 \), which holds since \( \tfrac35 > \tfrac47 \). So \( g(p) = 5p - 2 \) on \( [0, \tfrac35] \) and \( g(p) = 4 - 5p \) on \( [\tfrac35, 1] \). With slopes \( 5 \) and \( -5 \), \( g \) **strictly** increases on the first interval and **strictly** decreases on the second, so its maximum \( g\bigl(\tfrac35\bigr) = 1 \) is attained at \( p = \tfrac35 \) and nowhere else. The only optimal strategy for Row is \( \x^{\star} = \bigl(\tfrac35, \tfrac25\bigr) \), and \( \A\tp\x^{\star} = \bigl(1, 1, \tfrac65\bigr) \).

*Column's side.* Against \( \x^{\star} \), column 3 costs Column \( \tfrac65 \), which is more than the value, so we expect Column never to use it. Try \( \y = (q, 1 - q, 0) \): then \( \A\y = (4q - 1,\ 4 - 6q) \), and the two entries are equal when \( q = \tfrac12 \). So \( \y^{\star} = \bigl(\tfrac12, \tfrac12, 0\bigr) \), with \( \A\y^{\star} = (1, 1) \).

*Verification.* \( \A\tp\x^{\star} = \bigl(1, 1, \tfrac65\bigr) \ge 1\cdot\1 \) and \( \A\y^{\star} = (1, 1) \le 1\cdot\1 \). As in Step 3 of the proof, these two inequalities give @eq-minimax-saddle with \( v = 1 \). So the value is \( v(\A) = 1 \), Row's optimal strategy is \( \bigl(\tfrac35, \tfrac25\bigr) \), and \( \bigl(\tfrac12, \tfrac12, 0\bigr) \) is optimal for Column.

*Column's optimal strategy is unique too.* If \( \y \) is optimal for Column, then \( \A\y \le \1 \), so \( \x^{\star\top}\A\y \le 1 \). But \( \x^{\star\top}\A\y = y_1 + y_2 + \tfrac65y_3 = 1 + \tfrac15y_3 \), so \( y_3 = 0 \). With \( \y = (q, 1-q, 0) \), the conditions \( 4q - 1 \le 1 \) and \( 4 - 6q \le 1 \) give \( q \le \tfrac12 \) and \( q \ge \tfrac12 \). This is complementary slackness (@thm-complementary-slackness) in the language of games: a column whose payoff against an optimal \( \x \) exceeds the value is never used.
:::

::: {.check}
In the game of @exm-game-two-by-three, is \( \x = \bigl(\tfrac12, \tfrac12\bigr) \) an optimal strategy for Row? What does Column do against it?
:::

::: {.solution}
No. \( \A\tp\x = \bigl(\tfrac12, \tfrac32, 1\bigr) \), so \( g(\x) = \tfrac12 < 1 = v(\A) \). Column answers with column 1 and pays only \( \tfrac12 \) on average. The symmetric-looking strategy is not the safe one.
:::

::: {.warning}
**"Make the opponent indifferent between all columns" is not a method.** In @exm-game-two-by-three, no \( \x \in \Delta_2 \) makes all three entries of \( \A\tp\x \) equal: the first two are equal only at \( p = \tfrac35 \), where the third is \( \tfrac65 \), not \( 1 \). The optimal \( \x \) equalizes only the columns that Column actually uses. Deciding **which** columns those are is the real content of solving the game, and it is what the linear program decides. Equalizing the wrong set of columns produces a strategy that is not optimal, or a "solution" with negative probabilities.
:::

Finally, optimal strategies need not be unique, although in the example both were. @exr-minimax-b3 gives a game in which Row has a whole segment of optimal strategies, which is what the convexity of the optimal set allows.

## Exercises

### A. Check your understanding

:::: {#exr-minimax-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the standard simplex \( \Delta_n \), a mixed strategy, and the value of a matrix game.
2. State von Neumann's minimax theorem.
3. Determine whether the following is correct, and justify your answer: every matrix game has a saddle point in pure strategies.
4. Explain in two sentences why \( \max_{\x}\min_{\y} f(\x, \y) \le \min_{\y}\max_{\x} f(\x, \y) \) for every function \( f \) for which the extrema exist.
5. Name the mechanism that produces the equality in @thm-courant-fischer and the one that produces it in @thm-von-neumann-minimax.
:::
::::

::: {.solution}
(a) \( \Delta_n = \{ \x \in \nR^n : \x \ge \0,\ \sum_i x_i = 1 \} \). In a game with payoff matrix \( \A \in M_{m \times n}(\nR) \), a mixed strategy for Row is an \( \x \in \Delta_m \) and one for Column is a \( \y \in \Delta_n \). The value is \( v(\A) = \max_{\x \in \Delta_m}\min_{\y \in \Delta_n}\x\tp\A\y \).

(b) For every \( \A \in M_{m \times n}(\nR) \), \( \max_{\x \in \Delta_m}\min_{\y \in \Delta_n}\x\tp\A\y = \min_{\y \in \Delta_n}\max_{\x \in \Delta_m}\x\tp\A\y \), both extrema being attained. Equivalently, there are \( \x^{\star}, \y^{\star} \) and \( v \) with \( \x\tp\A\y^{\star} \le v \le \x^{\star\top}\A\y \) for all \( \x, \y \).

(c) Incorrect. In the matching game with \( \A = \begin{psmallmatrix} 1 & -1 \\ -1 & 1\end{psmallmatrix} \), \( \max_i\min_j a_{ij} = -1 < 1 = \min_j\max_i a_{ij} \). An entry that is smallest in its row and largest in its column would make these equal.

(d) For any \( \x_0, \y_0 \), \( \min_{\y} f(\x_0, \y) \le f(\x_0, \y_0) \le \max_{\x} f(\x, \y_0) \). The left side does not involve \( \y_0 \) and the right side does not involve \( \x_0 \), so we may maximize the left over \( \x_0 \) and minimize the right over \( \y_0 \).

(e) For Courant–Fischer, a dimension count: @lem-subspace-intersection forces every competing subspace to meet a span of eigenvectors. For von Neumann, convexity: the strategy sets are simplices and the payoff is linear in each variable, and the equality is linear programming duality, which rests on separation.
:::

### B. Practice

:::: {#exr-minimax-b1}
[B1: A two-by-two game]

Let \( \A = \begin{pmatrix} 2 & -3 \\ -1 & 1 \end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Show that the game has no saddle point in pure strategies.
2. Find the value and optimal strategies for both players, and verify the saddle inequality @eq-minimax-saddle.
:::
::::

::: {.solution}
(a) The row minima are \( -3 \) and \( -1 \), so \( \max_i\min_j a_{ij} = -1 \). The column maxima are \( 2 \) and \( 1 \), so \( \min_j\max_i a_{ij} = 1 \). These differ, so no entry is both smallest in its row and largest in its column.

(b) For \( \x = (p, 1 - p) \), \( \A\tp\x = (3p - 1,\ 1 - 4p) \). The first entry increases and the second decreases in \( p \), so their minimum is largest where they are equal: \( 3p - 1 = 1 - 4p \), that is, \( p = \tfrac27 \), with common value \( -\tfrac17 \). For \( \y = (q, 1 - q) \), \( \A\y = (5q - 3,\ 1 - 2q) \), and the entries are equal when \( q = \tfrac47 \), with common value \( -\tfrac17 \). So take \( \x^{\star} = \bigl(\tfrac27, \tfrac57\bigr) \), \( \y^{\star} = \bigl(\tfrac47, \tfrac37\bigr) \) and \( v = -\tfrac17 \). Then \( \A\tp\x^{\star} = -\tfrac17\1 \) and \( \A\y^{\star} = -\tfrac17\1 \). For every \( \y \in \Delta_2 \), \( \x^{\star\top}\A\y = -\tfrac17(y_1 + y_2) = -\tfrac17 \), and, since \( \A\y^{\star} = -\tfrac17\1 \), for every \( \x \in \Delta_2 \) we have \( \x\tp\A\y^{\star} = -\tfrac17(x_1 + x_2) = -\tfrac17 \). So @eq-minimax-saddle holds with equality throughout, and \( v(\A) = -\tfrac17 \). The game slightly favors Column.
:::

:::: {#exr-minimax-b2}
[B2: A saddle point]

Let \( \A = \begin{pmatrix} 3 & 1 & 4 \\ 2 & 0 & 1 \end{pmatrix} \), the second game of this section. Show that \( \x^{\star} = \e_1 \), \( \y^{\star} = \e_2 \) satisfy @eq-minimax-saddle with \( v = 1 \), and deduce the value of the game.
::::

::: {.solution}
For \( \x \in \Delta_2 \), \( \x\tp\A\e_2 = x_1\cdot 1 + x_2\cdot 0 = x_1 \le 1 \), since \( x_1 \le x_1 + x_2 = 1 \). For \( \y \in \Delta_3 \), \( \e_1\tp\A\y = 3y_1 + y_2 + 4y_3 \ge y_1 + y_2 + y_3 = 1 \). So \( \x\tp\A\e_2 \le 1 \le \e_1\tp\A\y \) for all \( \x, \y \), which is @eq-minimax-saddle with \( v = 1 \). By Step 4 of the proof of @thm-von-neumann-minimax (whose argument uses only @eq-minimax-saddle), the max–min and the min–max both equal \( 1 \), so \( v(\A) = 1 \). A pure saddle point is a special case of a mixed one.
:::

:::: {#exr-minimax-b3}
[B3: Many optimal strategies]

Let \( \A = \begin{pmatrix} 4 & 0 & 1 \\ -1 & 3 & 1 \end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( v(\A) = 1 \).
2. Find **all** optimal strategies for Row.
3. Show that Column has exactly one optimal strategy.
:::
::::

::: {.solution}
(a) Column can play \( \e_3 \), which gives \( \x\tp\A\e_3 = x_1 + x_2 = 1 \) for every \( \x \). Hence
\[
\min_{\y}\max_{\x}\x\tp\A\y \le \max_{\x}\x\tp\A\e_3 = 1 .
\] Row can play \( \x = \bigl(\tfrac12, \tfrac12\bigr) \), with \( \A\tp\x = \bigl(\tfrac32, \tfrac32, 1\bigr) \ge \1 \), so \( \max_{\x}\min_{\y}\x\tp\A\y \ge 1 \) by @lem-pure-best-response. By @thm-von-neumann-minimax both equal \( v(\A) \), which is therefore \( 1 \).

(b) By the remark after @def-value-of-game, \( \x = (p, 1 - p) \) is optimal exactly when \( \A\tp\x = (5p - 1,\ 3 - 3p,\ 1) \ge \1 \), that is, \( p \ge \tfrac25 \) and \( p \le \tfrac23 \). So the optimal strategies for Row are the whole segment \( \bigl\{ (p, 1 - p) : \tfrac25 \le p \le \tfrac23 \bigr\} \).

(c) \( \y = (a, b, c) \in \Delta_3 \) is optimal exactly when \( \A\y \le \1 \): \( 4a + c \le 1 \) and \( -a + 3b + c \le 1 \). Substituting \( c = 1 - a - b \), these become \( 3a \le b \) and \( 2b \le 2a \). Hence \( 3a \le b \le a \), so \( a \le 0 \), and with \( a \ge 0 \) we get \( a = 0 \) and then \( b = 0 \). So \( \y = \e_3 \) is the unique optimal strategy for Column.
:::

### C. Going deeper

:::: {#exr-minimax-c1}
[C1: Symmetric games]

Let \( \A \in M_n(\nR) \) be skew-symmetric, \( \A\tp = -\A \). Such a game is **symmetric**: the two players have the same options, and swapping their roles swaps the payoff's sign.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \x\tp\A\x = 0 \) for every \( \x \in \nR^n \), and deduce that \( v(\A) = 0 \).
2. Prove that \( \x \) is optimal for Row if and only if it is optimal for Column.
3. In rock–paper–scissors, with the pure strategies in that order and payoff \( 1 \) for a win, \( -1 \) for a loss and \( 0 \) for a tie,
\[
\A = \begin{pmatrix} 0 & -1 & 1 \\ 1 & 0 & -1 \\ -1 & 1 & 0 \end{pmatrix} .
\]
Prove that the uniform strategy \( \tfrac13\1 \) is the **only** optimal strategy.
:::
::::

::: {.solution}
(a) \( \x\tp\A\x \) is a \( 1 \times 1 \) matrix, so it equals its transpose: \( \x\tp\A\x = \x\tp\A\tp\x = -\x\tp\A\x \). Hence \( \x\tp\A\x = 0 \). Let \( \x^{\star}, \y^{\star}, v \) be as in @thm-von-neumann-minimax. Taking \( \y = \x^{\star} \) in the right half of @eq-minimax-saddle gives \( v \le \x^{\star\top}\A\x^{\star} = 0 \). Taking \( \x = \y^{\star} \) in the left half gives \( 0 = \y^{\star\top}\A\y^{\star} \le v \). So \( v(\A) = 0 \).

(b) By the remark after @def-value-of-game and (a), \( \x \) is optimal for Row exactly when \( \A\tp\x \ge \0 \), and optimal for Column exactly when \( \A\x \le \0 \). Since \( \A\tp\x = -\A\x \), the two conditions are the same.

(c) With \( \x = (x_1, x_2, x_3) \in \Delta_3 \), the condition \( \A\tp\x \ge \0 \) reads
\[
x_2 - x_3 \ge 0, \qquad x_3 - x_1 \ge 0, \qquad x_1 - x_2 \ge 0 .
\]
So \( x_2 \ge x_3 \ge x_1 \ge x_2 \), all three are equal, and since they sum to \( 1 \), each is \( \tfrac13 \). By (a) and (b), \( \tfrac13\1 \) is the unique optimal strategy for either player, and the value is \( 0 \).
:::

:::: {#exr-minimax-c2}
[C2: The value depends continuously on the payoffs]

For \( \A, \B \in M_{m \times n}(\nR) \), put \( \varepsilon = \max_{i,j}\lvert a_{ij} - b_{ij}\rvert \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \lvert v(\A) - v(\B)\rvert \le \varepsilon \).
2. Prove also that if \( a_{ij} \ge b_{ij} \) for all \( i, j \), then \( v(\A) \ge v(\B) \), and that \( v(\A + c\J) = v(\A) + c \) for every real \( c \).
:::
::::

::: {.solution}
(a) For \( \x \in \Delta_m \) and \( \y \in \Delta_n \),
\[
\lvert \x\tp\A\y - \x\tp\B\y \rvert \le \sum_{i,j} x_iy_j\lvert a_{ij} - b_{ij}\rvert \le \varepsilon\sum_{i,j}x_iy_j = \varepsilon ,
\]
since \( \sum_{i,j}x_iy_j = (\sum_i x_i)(\sum_j y_j) = 1 \). So \( \x\tp\A\y \le \x\tp\B\y + \varepsilon \) for all \( \x, \y \). Taking the minimum over \( \y \) preserves this inequality between two functions of \( \y \), and so does taking the maximum over \( \x \). By @thm-von-neumann-minimax the resulting max–mins are the values, so \( v(\A) \le v(\B) + \varepsilon \). Exchanging \( \A \) and \( \B \) gives \( v(\B) \le v(\A) + \varepsilon \).

(b) If \( a_{ij} \ge b_{ij} \), then \( \x\tp\A\y \ge \x\tp\B\y \) for all strategies, since every \( x_iy_j \ge 0 \), and the same two steps give \( v(\A) \ge v(\B) \). For the shift, \( \x\tp(\A + c\J)\y = \x\tp\A\y + c \) for all strategies, as in Step 1 of the proof of @thm-von-neumann-minimax, and adding a constant to a function adds it to every minimum and maximum. So \( v(\A + c\J) = v(\A) + c \).
:::
