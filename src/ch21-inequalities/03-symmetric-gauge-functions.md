# Symmetric Gauge Functions

The last two sections turned a majorization into an inequality between sums of a convex function. This section turns it into an inequality between **norms**. The norms that work are the ones blind to exactly the information a majorization discards — the order of the entries and their signs — and Section 4 will show that these are precisely the norms a matrix inherits from its singular values.

**Throughout, the field is \( \nR \) and the space is \( \nR^n \) with the dot product** \( \inner{\x}{\y} = \x\tp\y \), \( n \ge 1 \). Majorization \( \prec \) and weak majorization \( \prec_w \) are Chapter 17 §08's (@def-majorization), and \( \x^{\downarrow} \) is the decreasing rearrangement. A **permutation matrix** \( \P_\sigma \) is @def-permutation-matrix; \( \P_\sigma\x \) rearranges the entries of \( \x \). We write \( \lvert\x\rvert = (\lvert x_1\rvert, \dots, \lvert x_n\rvert) \), and \( \x \le \y \) means \( x_i \le y_i \) for **every** \( i \) — the entrywise order of Chapter 18 §05, never the Loewner order. From §01 we use @cor-majorization-convex-hull, which rests on @thm-hardy-littlewood-polya; the exercises also use §02's @thm-karamata.

## What a norm must forget

Chapter 17 §06 measured a Hermitian matrix by its Ky Fan partial sum \( s_k(\A) = \lambda_1(\A) + \dots + \lambda_k(\A) \), and @exr-poincare-and-ky-fan-c2 asked whether \( s_k \) is a norm. On the positive semidefinite matrices it behaves like one; on all Hermitian matrices it fails, because \( s_1(\diag(0,-1)) = 0 \) with \( \diag(0,-1) \ne \0 \). The exercise ended by naming the repair: apply \( s_k \) to the **singular** values instead of the eigenvalues. Singular values are non-negative, so nothing can cancel, and the failure disappears.

That repair suggests the shape of the whole chapter's answer. A measurement of a matrix built from its singular values is a function of a list of \( n \) non-negative numbers. Two things about that list are accidents of bookkeeping. Its **order** is one: the singular values of a matrix form a multiset, and Chapter 13 chose to write them decreasingly. Its **signs** are the other: a formula that is to extend from non-negative lists to all of \( \nR^n \), and be a norm there, cannot notice which entries are negative, since \( \x \) and the vector obtained by flipping one sign have the same absolute values and must be measured alike.

*A symmetric gauge function is a norm that cannot tell the entries of a vector apart by where they sit or which way they point.*

:::: {#def-symmetric-gauge}
[Symmetric Gauge Function]

A **symmetric gauge function** on \( \nR^n \) is a norm \( \Phi \colon \nR^n \to \nR \) (@def-norm) such that

::: {.enumerate options="label=(G\arabic*)"}
1. \( \Phi(\P_\sigma\x) = \Phi(\x) \) for **every** permutation matrix \( \P_\sigma \) and every \( \x \in \nR^n \)  (**permutation invariance**);
2. \( \Phi(\varepsilon_1x_1, \dots, \varepsilon_nx_n) = \Phi(\x) \) for **all** signs \( \varepsilon_i \in \{+1, -1\} \) and every \( \x \in \nR^n \)  (**sign invariance**).
:::
::::

In words: (G1) says that shuffling the entries does not change the measurement, and (G2) says that flipping any of their signs does not either. The word **every** does the work in both, and the two clauses are genuinely separate: below are a norm with (G1) and not (G2), and one with (G2) and not (G1). Together they say that \( \Phi(\x) \) depends only on the multiset \( \{\lvert x_1\rvert, \dots, \lvert x_n\rvert\} \), that is,
\[
\Phi(\x) = \Phi\bigl(\lvert\x\rvert^{\downarrow}\bigr) \qquad (\x \in \nR^n) ,
\]{#eq-gauge-depends-on-sorted-moduli}
since \( \lvert\x\rvert \) is obtained from \( \x \) by (G2) and \( \lvert\x\rvert^{\downarrow} \) from \( \lvert\x\rvert \) by (G1). Note also that (N2) of @def-norm already gives \( \Phi(-\x) = \Phi(\x) \); (G2) is much stronger, because it flips the signs **one entry at a time**.

::: {.warning}
**The word "gauge" is used here in a different sense from Chapter 18 §04.** There, @def-gauge attached to a convex set \( K \) the function \( p_K(\x) = \inf\{t > 0 : \x \in tK\} \), which measures a vector by inflating \( K \). That object is not this one. The name "symmetric gauge function" is standard and traditional for @def-symmetric-gauge, and the two never appear in the same argument in this book; where confusion is possible, this chapter writes \( \Phi \) and never \( p_K \).
:::

The first examples are the norms already at hand.

::: {#exm-symmetric-gauge-examples}
[The p-norms, the Ky Fan gauges, and size one]

Check each against @def-symmetric-gauge.

::: {.enumerate options="label=(\alph*)"}
1. \( \norm{\cdot}_p \) for \( 1 \le p \le \infty \).
2. For \( 1 \le k \le n \), the function \( \Phi_k(\x) = \sum_{i \le k}\lvert x\rvert^{\downarrow}_i \), the sum of the \( k \) largest absolute values.
3. On \( \nR^1 \), the function \( \Phi(x) = c\lvert x\rvert \) for a constant \( c > 0 \).
:::
:::

::: {.solution}
(a) These are norms: @exm-p-norms for \( p = 1, 2, \infty \), and @cor-minkowski-inequality supplies the triangle inequality for the rest. The formulas \( \bigl(\sum_i\lvert x_i\rvert^p\bigr)^{1/p} \) and \( \max_i\lvert x_i\rvert \) are built from the absolute values alone and are unchanged by reordering the sum or the maximum, so (G1) and (G2) hold.

(b) Rewrite the definition as a maximum:
\[
\Phi_k(\x) = \max\Bigl\{\sum_{i \in S}\lvert x_i\rvert \ :\ S \subseteq \{1, \dots, n\},\ \lvert S\rvert = k\Bigr\} ,
\]
since the largest such sum is the one over the indices of the \( k \) largest absolute values. Each function \( \x \mapsto \sum_{i \in S}\lvert x_i\rvert \) is non-negative, absolutely homogeneous and subadditive, so the maximum of finitely many of them is too, which gives (N2) and (N3). For (N1), every singleton is contained in some \( S \), so \( \Phi_k(\x) \ge \max_i\lvert x_i\rvert \), and \( \Phi_k(\x) = 0 \) forces \( \x = \0 \). Both (G1) and (G2) are visible in the displayed formula. At the two ends, \( \Phi_1 = \norm{\cdot}_\infty \) and \( \Phi_n = \norm{\cdot}_1 \).

(c) A norm on \( \nR^1 \) by inspection. There is only one permutation and \( \Phi(-x) = \Phi(x) \), so (G1) and (G2) are automatic: on \( \nR^1 \) **every** norm is a symmetric gauge function. The degenerate case is worth keeping in mind, because it shows that the two clauses carry no information until \( n \ge 2 \).
:::

The functions in (b) will be used constantly, so they get a name of their own.

::: {#def-ky-fan-gauge}
[Ky Fan Gauge]

For \( 1 \le k \le n \), the **\( k \)-th Ky Fan gauge** on \( \nR^n \) is
\[
\Phi_k(\x) = \sum_{i=1}^{k}\lvert x\rvert^{\downarrow}_i ,
\]
the sum of the \( k \) largest absolute values of the entries of \( \x \).
:::

**Non-examples by minimal change.** Each drops exactly one clause.

- *A norm with (G1) and not (G2).* On \( \nR^2 \) let
\[
\Phi(\x) = \max\bigl(\lvert x_1 + x_2\rvert,\ \lvert x_1\rvert,\ \lvert x_2\rvert\bigr) .
\]
Each of the three expressions is non-negative, absolutely homogeneous and subadditive, so their maximum is too; and \( \Phi(\x) = 0 \) forces \( x_1 = x_2 = 0 \), so \( \Phi \) is a norm. Swapping \( x_1 \) and \( x_2 \) permutes the three expressions, so (G1) holds. But \( \Phi(1,1) = 2 \) while \( \Phi(1,-1) = 1 \): (G2) fails.
- *A norm with (G2) and not (G1).* On \( \nR^2 \) let \( \Phi(\x) = \lvert x_1\rvert + 2\lvert x_2\rvert \). This is a norm, and it is built from absolute values, so (G2) holds. But \( \Phi(1, 0) = 1 \) and \( \Phi(0,1) = 2 \): (G1) fails.

**Why this definition.** The two clauses are exactly what a norm needs in order to be computable from an unordered list of non-negative numbers, and nothing more is demanded — in particular, no relation to any other norm, and no smoothness. Dropping (G1) allows a norm to prefer one coordinate to another, which no measurement of singular values can do, since relabeling the singular values of a matrix is not an operation on the matrix at all. Dropping (G2) allows a norm to see cancellation between coordinates, which is fatal: Section 7 needs \( \Phi \) evaluated at differences of eigenvalue lists and of singular value lists, whose entries have both signs (@thm-lidskii-ui and @thm-mirsky-ui).

::: {.check}
Is \( \Phi(\x) = \max_i x_i \) (no absolute values) a symmetric gauge function on \( \nR^n \) for \( n \ge 2 \)? Which clause fails first?
:::

::: {.solution}
It is not, and it fails before (G1) or (G2) are reached: it is not a norm. Absolute homogeneity (N2) fails at \( c = -1 \), since \( \max_i(-x_i) = -\min_i x_i \), which for \( \x = (1, 0) \) is \( 0 \) while \( \max_i x_i = 1 \). Positive definiteness (N1) fails too: \( \Phi(-1,-1) = -1 < 0 \). Restricted to vectors with non-negative entries the formula is perfectly reasonable, and it equals \( \norm{\x}_\infty \) there; the definition insists on a norm on all of \( \nR^n \) precisely so that this kind of one-sided formula is excluded.
:::

## A symmetric gauge is monotone

The first payoff is that a symmetric gauge respects the crudest comparison there is: if every entry of \( \x \) is smaller in absolute value than the matching entry of \( \y \), then \( \Phi(\x) \le \Phi(\y) \). This is not automatic for a norm. The function \( N(\x) = \lvert x_1 - x_2\rvert + \lvert x_1\rvert \) is a norm on \( \nR^2 \), and \( N(1, 0) = 2 \) is **larger** than \( N(1,1) = 1 \) although \( (1,0) \) is dominated entrywise by \( (1,1) \). Sign invariance is what rules this out.

::: {#prp-gauge-monotone}
[Symmetric Gauges Are Monotone]

Let \( \Phi \) be a symmetric gauge function on \( \nR^n \), and let \( \x, \y \in \nR^n \) satisfy \( \lvert x_i\rvert \le \lvert y_i\rvert \) for every \( i \). Then \( \Phi(\x) \le \Phi(\y) \).
:::

::: {.idea}
Change one coordinate at a time. Shrinking a single entry towards \( 0 \) is taking an average of two vectors: the vector itself and the one with that entry's sign flipped. Sign invariance says those two have the same \( \Phi \), and the triangle inequality says the average has no larger one.
:::

::: {.proof}
**Step 1: one coordinate.** Suppose \( \u, \v \in \nR^n \) agree in every coordinate except the \( j \)-th, where \( \lvert u_j\rvert \le \lvert v_j\rvert \). If \( v_j = 0 \) then \( u_j = 0 \) and \( \u = \v \). Otherwise put
\[
\theta = \frac12\Bigl(1 + \frac{u_j}{v_j}\Bigr) ,
\]
which lies in \( [0, 1] \) because \( \lvert u_j/v_j\rvert \le 1 \). Let \( \v' \) be \( \v \) with its \( j \)-th coordinate negated. Then \( \theta v_j + (1-\theta)(-v_j) = u_j \), while in every other coordinate \( \v \) and \( \v' \) agree with \( \u \), so
\[
\u = \theta\v + (1 - \theta)\v' .
\]
By (N3) and (N2) of @def-norm, \( \Phi(\u) \le \theta\Phi(\v) + (1-\theta)\Phi(\v') \), and \( \Phi(\v') = \Phi(\v) \) by (G2). Hence \( \Phi(\u) \le \Phi(\v) \).

**Step 2: all coordinates.** Put \( \z^{(0)} = \y \) and, for \( 1 \le j \le n \),
\[
\z^{(j)} = (x_1, \dots, x_j, y_{j+1}, \dots, y_n) ,
\]
so that \( \z^{(n)} = \x \). Consecutive vectors \( \z^{(j-1)} \) and \( \z^{(j)} \) agree except in coordinate \( j \), where \( \lvert x_j\rvert \le \lvert y_j\rvert \). By Step 1, \( \Phi(\z^{(j)}) \le \Phi(\z^{(j-1)}) \) for each \( j \). Chaining the \( n \) inequalities gives \( \Phi(\x) \le \Phi(\y) \), as claimed.
:::

Only (G2) was used. Permutation invariance is needed for the next step, and there it does all the work.

::: {.check}
Deduce from @prp-gauge-monotone that \( \Phi(\x) \ge \lvert x_j\rvert\,\Phi(\e_j) \) for every \( j \). What does the same proposition give as an upper bound, using \( \x = \sum_j x_j\e_j \)?
:::

::: {.solution}
The vector \( x_j\e_j \) has \( j \)-th entry \( x_j \) and all others \( 0 \), so its entries are dominated in absolute value by those of \( \x \); @prp-gauge-monotone gives \( \lvert x_j\rvert\Phi(\e_j) = \Phi(x_j\e_j) \le \Phi(\x) \). For the upper bound the triangle inequality suffices: \( \Phi(\x) \le \sum_j\lvert x_j\rvert\Phi(\e_j) \). By (G1) all the numbers \( \Phi(\e_j) \) are equal, to \( \Phi(\e_1) \) say, so
\[
\Phi(\e_1)\norm{\x}_\infty \ \le\ \Phi(\x) \ \le\ \Phi(\e_1)\norm{\x}_1 .
\]
Every symmetric gauge is trapped between multiples of \( \norm{\cdot}_\infty \) and \( \norm{\cdot}_1 \), with the same constant at both ends. Section 4 turns this into the statement that every **normalized** unitarily invariant norm lies between the spectral norm and the trace norm.
:::

Both bounds are cited later, so they are recorded here.

::: {#cor-gauge-between-infinity-and-one}
[A Symmetric Gauge Is Trapped Between Two Norms]

Let \( \Phi \) be a symmetric gauge function on \( \nR^n \). Then \( \Phi(\e_j) = \Phi(\e_1) \) for every \( j \), and
\[
\Phi(\e_1)\norm{\x}_\infty \ \le\ \Phi(\x) \ \le\ \Phi(\e_1)\norm{\x}_1 \qquad (\x \in \nR^n) .
\]
:::

::: {.proof}
Fix \( j \). Some permutation matrix carries \( \e_j \) to \( \e_1 \), so \( \Phi(\e_j) = \Phi(\e_1) \) by (G1). The entries of \( x_j\e_j \) are dominated in absolute value by those of \( \x \), so @prp-gauge-monotone gives
\[
\lvert x_j\rvert\,\Phi(\e_1) = \Phi(x_j\e_j) \le \Phi(\x) ,
\]
where the equality is (N2) of @def-norm; taking the largest \( \lvert x_j\rvert \) gives the left-hand inequality. For the right-hand one, \( \x = \sum_j x_j\e_j \), so (N3) and (N2) give \( \Phi(\x) \le \sum_j\lvert x_j\rvert\Phi(\e_j) = \Phi(\e_1)\norm{\x}_1 \). This proves the corollary.
:::

## From weak majorization to a dominating vector

Now for the bridge. A majorization \( \x \prec \y \) will be handled by @cor-majorization-convex-hull, which writes \( \x \) as an average of rearrangements of \( \y \); a norm cannot grow under an average. Weak majorization loses the equality of totals, so \( \x \) need not be such an average — \( (1, 0) \prec_w (2, 0) \), but \( (1,0) \) is no average of \( (2,0) \) and \( (0,2) \). What survives is that \( \x \) is dominated **entrywise** by something that is such an average, and that is exactly the hypothesis @prp-gauge-monotone wants.

::: {#lem-weak-majorization-dominated}
[Weak Majorization Is Domination plus Majorization]

Let \( \x, \y \in \nR^n \). Then \( \x \prec_w \y \) if and only if there is a vector \( \z \in \nR^n \) with
\[
\x \le \z \quad\text{entrywise}, \qquad \z \prec \y .
\]
If \( \x \) has **non-negative** entries, then \( \z \) may be taken with non-negative entries as well.
:::

::: {.idea}
\( (\Leftarrow) \) is two easy monotonicity steps. For \( (\Rightarrow) \), sort both vectors and think of the deficit \( \sum_i y_i - \sum_i x_i \) as water to be poured into \( \x \). Pouring it into the **top** entries would break the partial-sum inequalities immediately, so pour it into the bottom: raise every entry of \( \x \) that lies below a level \( c \) up to \( c \), and choose \( c \) so that the totals match. Choosing \( c \) needs no analysis: on each interval between consecutive entries of \( \x \) the total is an affine function of \( c \), so the right \( c \) can be written down.
:::

::: {.proof}
\( (\Leftarrow) \) Suppose \( \x \le \z \) entrywise and \( \z \prec \y \). Fix \( k \) and let \( I \) be a set of \( k \) indices carrying the \( k \) largest entries of \( \x \), so that \( \sum_{i \le k}x^{\downarrow}_i = \sum_{i \in I}x_i \). Then
\[
\sum_{i\le k}x^{\downarrow}_i = \sum_{i\in I}x_i \ \le\ \sum_{i\in I}z_i \ \le\ \sum_{i\le k}z^{\downarrow}_i ,
\]
the last step because the sum of **any** \( k \) entries of \( \z \) is at most the sum of its \( k \) largest. Hence \( \x \prec_w \z \), and \( \z \prec \y \) gives \( \sum_{i\le k}z^{\downarrow}_i \le \sum_{i\le k}y^{\downarrow}_i \) for \( k < n \) and equality of totals at \( k = n \); in both cases \( \sum_{i\le k}z^{\downarrow}_i \le \sum_{i\le k}y^{\downarrow}_i \). Combining, \( \x \prec_w \y \).

\( (\Rightarrow) \) Suppose \( \x \prec_w \y \). Majorization and weak majorization depend only on the decreasing rearrangements (@def-majorization and the remark after it), and the entrywise relation \( \x \le \z \) is preserved by applying one permutation to both sides. So it is enough to construct \( \z \) when \( \x = \x^{\downarrow} \) and \( \y = \y^{\downarrow} \): for general \( \x \), choose \( \P_\sigma \) with \( \P_\sigma\x = \x^{\downarrow} \), build \( \z' \) for the pair \( (\x^{\downarrow}, \y^{\downarrow}) \), and take \( \z = \P_\sigma^{-1}\z' \).

So let \( x_1 \ge \dots \ge x_n \) and \( y_1 \ge \dots \ge y_n \) with \( \sum_{i\le k}x_i \le \sum_{i\le k}y_i \) for every \( k \). Write \( S = \sum_{i=1}^{n}y_i \) and, for \( 0 \le k \le n-1 \),
\[
c_k = \frac{S - (x_1 + \dots + x_k)}{n - k} ,
\]
the level at which the last \( n - k \) entries would have to sit for the total to be \( S \). At \( k = n-1 \) we have \( c_{n-1} = S - \sum_{i \le n-1}x_i \ge \sum_{i\le n}x_i - \sum_{i\le n-1}x_i = x_n \), using \( \x \prec_w \y \) at \( k = n \). So the set of indices \( k \in \{0, \dots, n-1\} \) with \( c_k \ge x_{k+1} \) is non-empty; let \( j \) be its **smallest** element and put \( c = c_j \). Define
\[
\z = (x_1, \dots, x_j, \underbrace{c, \dots, c}_{n-j}) .
\]

*The vector \( \z \) dominates \( \x \).* For \( i \le j \) the entries agree. For \( i > j \), \( z_i = c \ge x_{j+1} \ge x_i \), since \( \x \) is decreasing and \( c \ge x_{j+1} \) by the choice of \( j \). If in addition \( \x \ge \0 \), then \( c \ge x_{j+1} \ge 0 \) and every entry of \( \z \) is non-negative, which is the last claim of the lemma.

*The vector \( \z \) is decreasing.* Only the step from \( x_j \) to \( c \) is in question, so assume \( j \ge 1 \). By the minimality of \( j \) we have \( c_{j-1} < x_j \). Multiplying out the two definitions,
\[
(n-j+1)c_{j-1} = S - \sum_{i\le j-1}x_i = (n-j)c_j + x_j ,
\]
so \( (n-j)c = (n-j+1)c_{j-1} - x_j < (n-j+1)x_j - x_j = (n-j)x_j \), and \( n - j \ge 1 \) gives \( c < x_j \). Hence \( \z = \z^{\downarrow} \).

*The vector \( \z \) is majorized by \( \y \).* Its total is \( \sum_{i\le j}x_i + (n-j)c = S \) by the definition of \( c_j \), which is (M2). For (M1) with \( k \le j \), the first \( k \) entries of \( \z \) are those of \( \x \), so \( \sum_{i\le k}z_i = \sum_{i\le k}x_i \le \sum_{i\le k}y_i \). For \( k > j \), subtract from the totals: since \( \sum_i z_i = \sum_i y_i = S \),
\[
\sum_{i\le k}z_i - \sum_{i\le k}y_i = \sum_{i>k}y_i - \sum_{i>k}z_i = \sum_{i>k}y_i - (n-k)c ,
\]
so it suffices to show \( \sum_{i>k}y_i \le (n-k)c \). First, at \( k = j \) this holds: from \( (n-j)c = S - \sum_{i\le j}x_i \) and \( \sum_{i\le j}x_i \le \sum_{i\le j}y_i \),
\[
(n-j)c \ \ge\ S - \sum_{i\le j}y_i = \sum_{i>j}y_i .
\]
So \( c \) is at least the average of the \( n - j \) smallest entries of \( \y \). Now let \( k > j \). Each of the entries \( y_{j+1}, \dots, y_k \) is at least each of \( y_{k+1}, \dots, y_n \), because \( \y \) is decreasing; hence each of them is at least the average \( A \) of \( y_{k+1}, \dots, y_n \), and therefore
\[
\sum_{i>j}y_i = \sum_{i=j+1}^{k}y_i + (n-k)A \ \ge\ (k - j)A + (n-k)A = (n-j)A .
\]
Combining, \( (n-j)c \ge \sum_{i>j}y_i \ge (n-j)A \), so \( c \ge A \) and \( (n-k)c \ge (n-k)A = \sum_{i>k}y_i \), as required. This proves \( \z \prec \y \) and the lemma.
:::

The construction is short enough to run by hand.

::: {#exm-dominating-vector}
[Filling from the bottom]

Let \( \x = (4, 1, 1) \) and \( \y = (5, 3, 2) \). Verify \( \x \prec_w \y \) and produce a \( \z \) with \( \x \le \z \) and \( \z \prec \y \).
:::

::: {.solution}
Both vectors are already decreasing. The running totals are \( 4, 5, 6 \) for \( \x \) and \( 5, 8, 10 \) for \( \y \), and \( 4 \le 5 \), \( 5 \le 8 \), \( 6 \le 10 \), so \( \x \prec_w \y \). The totals differ, so \( \x \not\prec \y \).

Here \( S = 10 \) and \( n = 3 \). The levels are \( c_0 = 10/3 \) and \( c_1 = (10-4)/2 = 3 \). Since \( c_0 = 10/3 < 4 = x_1 \), the index \( k = 0 \) fails; since \( c_1 = 3 \ge 1 = x_2 \), the smallest admissible index is \( j = 1 \), and \( c = 3 \). Hence
\[
\z = (4, 3, 3) .
\]
Check: \( (4,1,1) \le (4,3,3) \) entrywise; \( \z \) is decreasing; its running totals \( 4, 7, 10 \) satisfy \( 4 \le 5 \), \( 7 \le 8 \), \( 10 = 10 \), so \( \z \prec \y \). The deficit of \( 4 \) between the totals was poured entirely into the two bottom entries, which is what keeps the top partial sums under control.
:::

## The inequality

Everything is now in place.

::: {#thm-gauge-monotone-under-majorization}
[Symmetric Gauges Respect Majorization]

Let \( \Phi \) be a symmetric gauge function on \( \nR^n \).

::: {.enumerate options="label=(\alph*)"}
1. If \( \x, \y \in \nR^n \) and \( \x \prec \y \), then \( \Phi(\x) \le \Phi(\y) \).
2. If \( \x, \y \in \nR^n \) have **non-negative** entries and \( \x \prec_w \y \), then \( \Phi(\x) \le \Phi(\y) \).
:::
:::

::: {.idea}
For (a), §01 turns \( \x \prec \y \) into "\( \x \) is an average of rearrangements of \( \y \)", and a norm never exceeds an average of the values it takes on the points averaged — those values all being \( \Phi(\y) \), by permutation invariance. For (b), @lem-weak-majorization-dominated inserts a middle vector \( \z \): from \( \x \) to \( \z \) use monotonicity, from \( \z \) to \( \y \) use (a).
:::

::: {.proof}
(a) By @cor-majorization-convex-hull, \( \x \in \conv\{\P_\sigma\y : \sigma \in S_n\} \), so there are weights \( t_\sigma \ge 0 \) with \( \sum_\sigma t_\sigma = 1 \) and \( \x = \sum_\sigma t_\sigma\P_\sigma\y \). By the triangle inequality (N3) and absolute homogeneity (N2) of @def-norm, applied to this finite sum,
\[
\Phi(\x) \ \le\ \sum_{\sigma} t_\sigma\,\Phi(\P_\sigma\y) = \sum_\sigma t_\sigma\,\Phi(\y) = \Phi(\y) ,
\]
where the middle equality is (G1).

(b) By @lem-weak-majorization-dominated there is a \( \z \) **with non-negative entries** satisfying \( \x \le \z \) entrywise and \( \z \prec \y \). Since \( \x \) and \( \z \) have non-negative entries, \( \lvert x_i\rvert = x_i \le z_i = \lvert z_i\rvert \) for every \( i \), so @prp-gauge-monotone gives \( \Phi(\x) \le \Phi(\z) \). By part (a), \( \Phi(\z) \le \Phi(\y) \). This proves the theorem.
:::

Part (a) needs no sign condition, and part (b) cannot do without one.

::: {.warning}
**Part (b) is false for vectors with negative entries.** Take \( \x = (0, -10) \) and \( \y = (0, 0) \) in \( \nR^2 \). The decreasing rearrangements are \( (0, -10) \) and \( (0,0) \), and the running totals \( 0, -10 \) are at most \( 0, 0 \), so \( \x \prec_w \y \). But \( \Phi(\x) > 0 = \Phi(\y) \) for every norm \( \Phi \). The lemma is not at fault — \( \z = \0 \) does satisfy \( \x \le \z \) and \( \z \prec \y \). What fails is the step \( \Phi(\x) \le \Phi(\z) \), because @prp-gauge-monotone compares **absolute values**, and \( \lvert -10\rvert > \lvert 0\rvert \). Weak majorization lets a vector run far in the negative direction, and a norm measures that; only equality of totals, as in \( \prec \), or non-negativity of the entries rules it out. This is why Section 4 applies the theorem to singular values and never to eigenvalues.
:::

The converse of part (b) says that the family of symmetric gauges is strong enough to *detect* weak majorization, and it costs nothing: the Ky Fan gauges \( \Phi_k \) of @def-ky-fan-gauge are themselves symmetric gauges (@exm-symmetric-gauge-examples (b)), so the inequalities \( \Phi_k(\x) \le \Phi_k(\y) \) for every \( k \) are among those hypothesized, and for non-negative vectors they are the definition of \( \x \prec_w \y \). Exercise C1 below states the two directions together, and Section 6 turns them into a theorem about matrices.

## The dual gauge

Chapter 18 §04 gave every norm on \( \nR^n \) a dual, \( \norm{\y}_{*} = \max\{\inner{\x}{\y} : \norm{\x} \le 1\} \) (@def-dual-norm), and proved that taking the dual twice returns the norm (@thm-dual-dual-norm). Applied to a symmetric gauge, the construction stays inside the class.

::: {#def-dual-gauge}
[Dual Gauge]

Let \( \Phi \) be a symmetric gauge function on \( \nR^n \). Its **dual gauge** is the dual norm of @def-dual-norm,
\[
\Phi^{*}(\y) = \max\{\inner{\x}{\y} : \x \in \nR^n,\ \Phi(\x) \le 1\} .
\]
:::

::: {#thm-dual-gauge}
[The Dual of a Symmetric Gauge]

Let \( \Phi \) be a symmetric gauge function on \( \nR^n \). Then \( \Phi^{*} \) is a symmetric gauge function, and \( \Phi^{**} = \Phi \).
:::

::: {.idea}
Being a norm and being its own double dual are Chapter 18's, quoted. Only (G1) and (G2) need an argument, and each is the same one: the transformation can be moved off \( \y \) and onto \( \x \), where it permutes the constraint set \( \{\Phi \le 1\} \) onto itself.
:::

::: {.proof}
That \( \Phi^{*} \) is a norm is @prp-dual-norm-properties (a), and \( \Phi^{**} = \Phi \) is @thm-dual-dual-norm; both apply to any norm on \( \nR^n \).

(G1). Let \( \P = \P_\sigma \) be a permutation matrix. By @lem-permutation-matrices (b), \( \P\tp = \P^{-1} \), so \( \inner{\x}{\P\y} = \x\tp\P\y = (\P\tp\x)\tp\y = \inner{\P\tp\x}{\y} \). As \( \x \) runs over \( \{\Phi \le 1\} \), so does \( \x' = \P\tp\x \): indeed \( \Phi(\P\tp\x) = \Phi(\x) \) by (G1) for \( \Phi \), and \( \x \mapsto \P\tp\x \) is a bijection of \( \nR^n \). Hence the two maxima are over the same set of numbers, and \( \Phi^{*}(\P\y) = \Phi^{*}(\y) \).

(G2). Fix signs \( \varepsilon_i = \pm1 \) and write \( \y_\varepsilon = (\varepsilon_1y_1, \dots, \varepsilon_ny_n) \). Then \( \inner{\x}{\y_\varepsilon} = \sum_i x_i\varepsilon_iy_i = \inner{\x_\varepsilon}{\y} \), and \( \x \mapsto \x_\varepsilon \) is a bijection of \( \nR^n \) with \( \Phi(\x_\varepsilon) = \Phi(\x) \) by (G2) for \( \Phi \). So again the two maxima range over the same numbers, and \( \Phi^{*}(\y_\varepsilon) = \Phi^{*}(\y) \). This proves the theorem.
:::

So duality is an involution of the set of symmetric gauge functions on \( \nR^n \). The examples are Chapter 18's: by @prp-dual-of-one-two-infinity and @thm-dual-p-norm,
\[
(\norm{\cdot}_p)^{*} = \norm{\cdot}_q \qquad \Bigl(\tfrac1p + \tfrac1q = 1,\ 1 \le p \le \infty\Bigr) ,
\]
so \( \norm{\cdot}_1 \) and \( \norm{\cdot}_\infty \) are dual to each other and \( \norm{\cdot}_2 \) is self-dual. In the notation of @def-ky-fan-gauge that says \( \Phi_1^{*} = \Phi_n \) and \( \Phi_n^{*} = \Phi_1 \); exercise C2 below computes \( \Phi_k^{*} \) for the \( k \) in between. Section 5 will find the matrix meaning of all of this: the dual of a unitarily invariant norm, taken with respect to the trace pairing, is the norm attached to the dual gauge.

## Exercises

### A. Check your understanding

:::: {#exr-symmetric-gauge-functions-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State @def-symmetric-gauge, naming both invariance clauses and the space the function is defined on.
2. Explain why \( \Phi(\x) = \Phi(\lvert\x\rvert^{\downarrow}) \) for every symmetric gauge and every \( \x \).
3. True or false, with a reason: if \( \x \prec_w \y \) in \( \nR^n \), then \( \norm{\x}_2 \le \norm{\y}_2 \).
4. Name the hypothesis in @thm-gauge-monotone-under-majorization (b) that part (a) does without, and say where it is used in the proof.
:::
::::

::: {.solution}
(a) A symmetric gauge function on \( \nR^n \) is a norm \( \Phi \colon \nR^n \to \nR \) satisfying (G1) \( \Phi(\P_\sigma\x) = \Phi(\x) \) for every permutation matrix, and (G2) \( \Phi(\varepsilon_1x_1, \dots, \varepsilon_nx_n) = \Phi(\x) \) for all choices of signs \( \varepsilon_i = \pm1 \).

(b) This is @eq-gauge-depends-on-sorted-moduli. Replacing each \( x_i \) by \( \lvert x_i\rvert \) is a choice of signs, so (G2) gives \( \Phi(\x) = \Phi(\lvert\x\rvert) \); sorting \( \lvert\x\rvert \) decreasingly is applying a permutation matrix, so (G1) gives \( \Phi(\lvert\x\rvert) = \Phi(\lvert\x\rvert^{\downarrow}) \).

(c) False in general. Take \( \x = (0,-10) \) and \( \y = (0,0) \): then \( \x \prec_w \y \) but \( \norm{\x}_2 = 10 > 0 \). It is true when \( \x \) and \( \y \) have non-negative entries, by @thm-gauge-monotone-under-majorization (b) with \( \Phi = \norm{\cdot}_2 \).

(d) Non-negativity of the entries. It is used to pass from \( \x \le \z \) entrywise to \( \lvert x_i\rvert \le \lvert z_i\rvert \), which is what @prp-gauge-monotone requires; without it, \( x_i \le z_i \) says nothing about absolute values.
:::

### B. Practice

:::: {#exr-symmetric-gauge-functions-b1}
[B1: Which of these are symmetric gauges]

Determine which of the following are symmetric gauge functions on \( \nR^3 \). Justify your answer, naming the exact clause that fails when one does.

::: {.enumerate options="label=(\alph*)"}
1. \( \Phi(\x) = \lvert x_1\rvert + \lvert x_2\rvert + \lvert x_3\rvert \).
2. \( \Phi(\x) = \lvert x\rvert^{\downarrow}_1 + \lvert x\rvert^{\downarrow}_2 \).
3. \( \Phi(\x) = \bigl(\lvert x_1\rvert^{1/2} + \lvert x_2\rvert^{1/2} + \lvert x_3\rvert^{1/2}\bigr)^{2} \).
4. \( \Phi(\x) = \max(\lvert x_1\rvert, \lvert x_2\rvert) + \lvert x_3\rvert \).
5. \( \Phi(\x) = \lvert x_1 + x_2 + x_3\rvert + \lvert x_1 - x_2\rvert + \lvert x_2 - x_3\rvert \).
:::
::::

::: {.solution}
(a) Yes: this is \( \norm{\cdot}_1 = \Phi_3 \), @exm-symmetric-gauge-examples (a).

(b) Yes: this is the Ky Fan gauge \( \Phi_2 \) of @def-ky-fan-gauge, checked in @exm-symmetric-gauge-examples (b).

(c) No. It is non-negative, absolutely homogeneous, permutation invariant and sign invariant, but (N3) fails: with \( \x = (1,0,0) \) and \( \y = (0,1,0) \) we get \( \Phi(\x) = \Phi(\y) = 1 \) while \( \Phi(\x + \y) = (1+1)^2 = 4 > 2 \). It is not a norm, so it is not a symmetric gauge.

(d) No. It is a norm — a sum of two seminorms, positive definite because each coordinate appears — and it is sign invariant, so (G2) holds. But (G1) fails: \( \Phi(1,1,0) = 1 \) while \( \Phi(1,0,1) = 2 \).

(e) No. It is a norm: it is non-negative and absolutely homogeneous, subadditive as a sum of three seminorms, and \( \Phi(\x) = 0 \) forces \( x_1 = x_2 = x_3 \) and \( \lvert 3x_1\rvert = 0 \), hence \( \x = \0 \). Both invariance clauses fail. For (G1), \( \Phi(1,1,0) = 2 + 0 + 1 = 3 \) while \( \Phi(1,0,1) = 2 + 1 + 1 = 4 \). For (G2), \( \Phi(1,1,1) = 3 + 0 + 0 = 3 \) while \( \Phi(1,-1,1) = 1 + 2 + 2 = 5 \).
:::

:::: {#exr-symmetric-gauge-functions-b2}
[B2: Filling from the bottom]

Let \( \x = (6, 2, 2, 0) \) and \( \y = (7, 4, 3, 2) \) in \( \nR^4 \).

::: {.enumerate options="label=(\alph*)"}
1. Verify that \( \x \prec_w \y \) and that \( \x \not\prec \y \).
2. Carry out the construction in the proof of @lem-weak-majorization-dominated to produce \( \z \) with \( \x \le \z \) and \( \z \prec \y \).
3. Hence bound \( \norm{\x}_2 \) by \( \norm{\y}_2 \) without computing either, and then check the bound numerically.
:::
::::

::: {.solution}
(a) Both are decreasing. Running totals: \( 6, 8, 10, 10 \) for \( \x \) and \( 7, 11, 14, 16 \) for \( \y \). Each is at most the corresponding one, so \( \x \prec_w \y \); the totals \( 10 \) and \( 16 \) differ, so \( \x \not\prec \y \).

(b) Here \( S = 16 \) and \( n = 4 \), so \( c_0 = 16/4 = 4 \), \( c_1 = (16-6)/3 = 10/3 \), \( c_2 = (16-8)/2 = 4 \), \( c_3 = 16 - 10 = 6 \). Test \( c_k \ge x_{k+1} \): \( c_0 = 4 < 6 = x_1 \), so \( k = 0 \) fails; \( c_1 = 10/3 \ge 2 = x_2 \), so \( j = 1 \) and \( c = 10/3 \). Hence
\[
\z = \bigl(6, \tfrac{10}{3}, \tfrac{10}{3}, \tfrac{10}{3}\bigr) .
\]
Check: \( \x \le \z \) entrywise; \( \z \) is decreasing; running totals \( 6, \tfrac{28}{3}, \tfrac{38}{3}, 16 \), and \( 6 \le 7 \), \( \tfrac{28}{3} \approx 9.33 \le 11 \), \( \tfrac{38}{3} \approx 12.67 \le 14 \), \( 16 = 16 \). So \( \z \prec \y \).

(c) Both vectors have non-negative entries, so @thm-gauge-monotone-under-majorization (b) with \( \Phi = \norm{\cdot}_2 \) gives \( \norm{\x}_2 \le \norm{\y}_2 \). Numerically \( \norm{\x}_2 = \sqrt{36+4+4} = \sqrt{44} \) and \( \norm{\y}_2 = \sqrt{49+16+9+4} = \sqrt{78} \), and \( 44 \le 78 \). The intermediate vector satisfies \( \norm{\z}_2^2 = 36 + 3\cdot\tfrac{100}{9} = \tfrac{208}{3} \approx 69.3 \), between the two, as the proof predicts.
:::

:::: {#exr-symmetric-gauge-functions-b3}
[B3: Monotonicity used twice]

Let \( \Phi \) be a symmetric gauge function on \( \nR^3 \) with \( \Phi(\e_1) = 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( 1 \le \Phi(1,1,0) \le 2 \).
2. Prove that \( \Phi(2,1,1) \le \Phi(3,1,0) \).
3. Give a symmetric gauge for which the inequality in (b) is strict, and one for which it is an equality.
:::
::::

::: {.solution}
(a) The Quick check following @prp-gauge-monotone gives \( \Phi(\e_1)\norm{\x}_\infty \le \Phi(\x) \le \Phi(\e_1)\norm{\x}_1 \). With \( \x = (1,1,0) \) and \( \Phi(\e_1) = 1 \) this reads \( 1 \le \Phi(1,1,0) \le 2 \).

(b) Both vectors are decreasing with total \( 4 \), and the running totals \( 2, 3 \) of \( (2,1,1) \) are at most the running totals \( 3, 4 \) of \( (3,1,0) \), so \( (2,1,1) \prec (3,1,0) \). Now @thm-gauge-monotone-under-majorization (a) applies.

(c) Strict for \( \Phi = \norm{\cdot}_2 \): \( \sqrt6 < \sqrt{10} \). It is also strict for \( \Phi = \Phi_2 \), where the values are \( 3 \) and \( 4 \). Equality holds for \( \Phi = \norm{\cdot}_1 = \Phi_3 \), where both values are \( 4 \): any two non-negative vectors with the same total have the same \( 1 \)-norm, so a majorization can never be detected by \( \Phi_3 \) alone. This is the general shape of the equality case — the top gauge sees only the total, which a majorization preserves.
:::

### C. Going deeper

:::: {#exr-symmetric-gauge-functions-c1}
[C1: Symmetric gauges detect weak majorization]

Let \( \x, \y \in \nR^n \) have non-negative entries.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \x \prec_w \y \) if and only if \( \Phi(\x) \le \Phi(\y) \) for **every** symmetric gauge function \( \Phi \) on \( \nR^n \).
2. Prove that \( \x \prec \y \) if and only if \( \x \prec_w \y \) and \( \sum_ix_i = \sum_iy_i \).
3. Deduce that \( \x \prec \y \) if and only if \( \Phi(\x) \le \Phi(\y) \) for every symmetric gauge and \( \sum_ix_i = \sum_iy_i \).
:::

*Hint for (a): only finitely many gauges are needed.*
::::

::: {.solution}
(a) \( (\Rightarrow) \) is @thm-gauge-monotone-under-majorization (b). \( (\Leftarrow) \) Apply the hypothesis to the Ky Fan gauges \( \Phi_k \) of @def-ky-fan-gauge, \( k = 1, \dots, n \). Since \( \x \) and \( \y \) have non-negative entries, \( \lvert\x\rvert^{\downarrow} = \x^{\downarrow} \) and likewise for \( \y \), so \( \Phi_k(\x) = \sum_{i\le k}x^{\downarrow}_i \) and \( \Phi_k(\y) = \sum_{i\le k}y^{\downarrow}_i \). The inequalities \( \Phi_k(\x) \le \Phi_k(\y) \) for \( k = 1, \dots, n \) are exactly (M1) extended to \( k = n \), which is @def-majorization's \( \x \prec_w \y \).

(b) This is a restatement of @def-majorization: \( \x \prec \y \) means (M1) for \( k \le n-1 \) together with equality of totals, and \( \x \prec_w \y \) means (M1) for \( k \le n \). Given equality of totals, the case \( k = n \) of (M1) is automatic, so the two lists of conditions agree.

(c) Combine (a) and (b): \( \x \prec \y \) holds exactly when \( \x \prec_w \y \) and the totals are equal, and by (a) the first of these is equivalent to \( \Phi(\x) \le \Phi(\y) \) for every symmetric gauge.
:::

:::: {#exr-symmetric-gauge-functions-c2}
[C2: The dual of a Ky Fan gauge]

Fix \( 1 \le k \le n \) and let \( \Phi_k \) be the Ky Fan gauge of @def-ky-fan-gauge.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \Phi_k^{*}(\y) \ge \max\bigl(\norm{\y}_\infty,\ \tfrac1k\norm{\y}_1\bigr) \) by exhibiting two competitors.
2. Let \( \Phi_k(\x) \le 1 \) and let \( \y \) have non-negative, decreasing entries. Put \( t = \lvert x\rvert^{\downarrow}_k \) and split each \( \lvert x_i\rvert \) as \( (\lvert x_i\rvert - t)_{+} + \min(\lvert x_i\rvert, t) \). Prove that \( \sum_i(\lvert x_i\rvert - t)_{+} \le 1 - kt \) and that \( 0 \le t \le 1/k \).
3. Deduce \( \Phi_k^{*}(\y) = \max\bigl(\norm{\y}_\infty, \tfrac1k\norm{\y}_1\bigr) \), and check the cases \( k = 1 \) and \( k = n \) against @prp-dual-of-one-two-infinity.
:::
::::

::: {.solution}
(a) The vector \( \e_1 \) has \( \Phi_k(\e_1) = 1 \); replacing it by \( \pm\e_j \) with the sign of \( y_j \), for a \( j \) where \( \lvert y_j\rvert \) is largest, gives \( \inner{\x}{\y} = \norm{\y}_\infty \). The vector \( \x \) with \( x_i = \pm1/k \), the sign of \( y_i \), has \( \Phi_k(\x) = k\cdot\tfrac1k = 1 \) and \( \inner{\x}{\y} = \tfrac1k\norm{\y}_1 \). So \( \Phi_k^{*}(\y) \) is at least both numbers.

(b) Since \( \lvert x\rvert^{\downarrow} \) is decreasing, \( (\lvert x\rvert^{\downarrow}_i - t)_{+} = 0 \) for \( i > k \), so
\[
\sum_i(\lvert x_i\rvert - t)_{+} = \sum_{i\le k}\bigl(\lvert x\rvert^{\downarrow}_i - t\bigr) = \Phi_k(\x) - kt \le 1 - kt .
\]
Also \( kt \le \sum_{i\le k}\lvert x\rvert^{\downarrow}_i = \Phi_k(\x) \le 1 \), so \( 0 \le t \le 1/k \).

(c) By @thm-dual-gauge, \( \Phi_k^{*} \) is a symmetric gauge, so its value at \( \y \) depends only on \( \lvert\y\rvert^{\downarrow} \); and replacing \( \x \) by \( \lvert\x\rvert \) leaves \( \Phi_k(\x) \) unchanged and does not decrease \( \inner{\x}{\y} \) when \( \y \ge \0 \). So we may assume \( \y \) has non-negative decreasing entries and \( \x \ge \0 \). With \( t \) as in (b), and using \( y_i \le y_1 = \norm{\y}_\infty \) in the first sum and \( \min(x_i, t) \le t \) in the second,
\[
\inner{\x}{\y} \le \norm{\y}_\infty(1 - kt) + t\norm{\y}_1
= \norm{\y}_\infty + t\bigl(\norm{\y}_1 - k\norm{\y}_\infty\bigr) .
\]
If \( \norm{\y}_1 \le k\norm{\y}_\infty \), the bracket is at most \( 0 \) and \( t \ge 0 \), so the right side is at most \( \norm{\y}_\infty \). If \( \norm{\y}_1 > k\norm{\y}_\infty \), the right side increases with \( t \), and \( t \le 1/k \) gives the bound \( \norm{\y}_\infty + \tfrac1k\norm{\y}_1 - \norm{\y}_\infty = \tfrac1k\norm{\y}_1 \). In both cases \( \inner{\x}{\y} \le \max(\norm{\y}_\infty, \tfrac1k\norm{\y}_1) \), which with (a) gives equality.

For \( k = 1 \), \( \Phi_1 = \norm{\cdot}_\infty \) and the formula gives \( \max(\norm{\y}_\infty, \norm{\y}_1) = \norm{\y}_1 \), matching @prp-dual-of-one-two-infinity (b). For \( k = n \), \( \Phi_n = \norm{\cdot}_1 \) and the formula gives \( \max(\norm{\y}_\infty, \tfrac1n\norm{\y}_1) = \norm{\y}_\infty \), matching part (a) of the same proposition.
:::

:::: {#exr-symmetric-gauge-functions-c3}
[C3: Where each hypothesis is used]

::: {.enumerate options="label=(\alph*)"}
1. Determine whether there is a norm on \( \nR^2 \) that is permutation invariant and satisfies \( \Phi(\x) \le \Phi(\y) \) whenever \( \lvert x_i\rvert \le \lvert y_i\rvert \) for all \( i \), but is **not** a symmetric gauge function. Justify your answer.
2. @thm-gauge-monotone-under-majorization (b) needs non-negative entries, while @lem-weak-majorization-dominated does not. Locate the exact step of the proof of the theorem that uses the hypothesis, and explain why \( \x = (0,-10) \prec_w (0,0) = \y \) breaks it even though the lemma supplies a perfectly good \( \z \).
3. Let \( \x \prec_w \y \) with \( \x = \x^{\downarrow} \), and let \( \z \) be the vector built in the proof of @lem-weak-majorization-dominated. Prove that \( \z \prec \z' \) for **every** \( \z' \) with \( \x \le \z' \) and \( \sum_i z'_i = \sum_i y_i \), and deduce that \( \sum_i\phi(z_i) \le \sum_i\phi(z'_i) \) for every convex \( \phi \). *Hint: compare top partial sums; @thm-karamata does the last step.*
:::
::::

::: {.solution}
(a) There is none: monotonicity in the stated sense already forces (G2). If \( \lvert x_i\rvert \le \lvert y_i\rvert \) implies \( \Phi(\x) \le \Phi(\y) \), then for any signs the vectors \( \x \) and \( (\varepsilon_1x_1, \dots, \varepsilon_nx_n) \) dominate each other entrywise in absolute value, so their \( \Phi \)-values are equal, which is (G2). With permutation invariance this is @def-symmetric-gauge. So the conclusion of @prp-gauge-monotone is not merely implied by (G2): for any norm the two are equivalent.

(b) The step is \( \Phi(\x) \le \Phi(\z) \), which invokes @prp-gauge-monotone and therefore needs \( \lvert x_i\rvert \le \lvert z_i\rvert \), not \( x_i \le z_i \). For \( \x = (0,-10) \) and \( \y = (0,0) \) the lemma does supply a \( \z \), namely \( \z = \0 \): indeed \( \z \prec \y \) and \( \x \le \z \). But \( \lvert x_2\rvert = 10 > 0 = \lvert z_2\rvert \), so @prp-gauge-monotone does not apply, and it must not: \( \Phi(\x) > 0 = \Phi(\z) \) for every norm. When the entries are non-negative, \( x_i \le z_i \) and \( \lvert x_i\rvert \le \lvert z_i\rvert \) say the same thing, and the gap closes.

(c) Write \( S = \sum_iy_i \) and recall \( \z = (x_1, \dots, x_j, c, \dots, c) \), decreasing, with \( \sum_iz_i = S \). Let \( \z' \) satisfy \( \x \le \z' \) and \( \sum_iz'_i = S \), and write \( M_1 \ge \dots \ge M_n \) for its entries in decreasing order. Since the totals agree, (M2) holds, and it remains to check (M1) for \( 1 \le k \le n-1 \).

*Case \( k \le j \).* Then \( \sum_{i\le k}z_i = \sum_{i\le k}x_i \le \sum_{i\le k}z'_i \le \sum_{i\le k}M_i \), the first inequality from \( \x \le \z' \) and the second because no \( k \) entries of \( \z' \) add up to more than its \( k \) largest.

*Case \( k > j \).* Here \( \sum_{i\le k}z_i = S - (n-k)c \), so the claim is \( \sum_{i>k}M_i \le (n-k)c \). Suppose not. Then the average of \( M_{k+1}, \dots, M_n \) exceeds \( c \), and \( M_{k+1} \), being the largest of them, satisfies \( M_{k+1} > c \); hence \( M_i > c \) for every \( i \le k+1 \). Also \( \sum_{i\le j}M_i \ge \sum_{i\le j}x_i \), by the argument of the previous case. Therefore
\[
\begin{aligned}
S = \sum_{i}M_i &= \sum_{i\le j}M_i + \sum_{i=j+1}^{k}M_i + \sum_{i>k}M_i \\
&> \sum_{i\le j}x_i + (k-j)c + (n-k)c = S ,
\end{aligned}
\]
the last equality being \( \sum_{i\le j}x_i + (n-j)c = S \), which defined \( c \). This contradiction proves the case.

So \( \z \prec \z' \), and @thm-karamata gives \( \sum_i\phi(z_i) \le \sum_i\phi(z'_i) \) for every convex \( \phi \). In words: among all admissible ways of raising \( \x \) to the required total, the flat filling is the most even one.
:::
