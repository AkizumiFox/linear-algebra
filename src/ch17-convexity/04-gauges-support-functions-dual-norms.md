# Gauges, Support Functions and Dual Norms

Chapter 15 §01 observed that the closed unit ball of every norm is convex and symmetric, and left the converse alone: does every convex, symmetric set arise as the unit ball of some norm? This section answers yes, by reading a norm off a convex set from the inside, the **gauge**. It then reads a function off a convex set from the outside, the **support function**, which turns §03's description of a closed convex set by half-spaces into a formula. Applied to a unit ball, the support function is the **dual norm**, the measurement Chapter 15 never gave to a linear functional, and the last part of the section proves that taking the dual twice returns the norm we started with.

**Throughout, the field is \( \nR \), and we work in \( \nR^n \), \( n \ge 1 \), with the dot product** \( \inner{\x}{\y} = \x\tp\y \) and its norm \( \norm{\cdot}_2 \). So everything proved in §03 is available, with \( V = \nR^n \). A symbol \( \norm{\cdot} \) without a subscript is an **arbitrary** norm on \( \nR^n \) in the sense of @def-norm, and \( B \) is its closed unit ball (@def-unit-ball). Interior points are meant in the sense of @def-interior-point, which does not depend on the norm. For a set \( K \) and a real \( t \), we write \( tK = \{t\x : \x \in K\} \).

## Gauges

Every norm can be read off its unit ball. By (N2), for \( t > 0 \) we have \( \norm{\x} \le t \) exactly when \( \norm{\x/t} \le 1 \), that is, when \( \x \in tB \). Hence
\[
\norm{\x} = \inf\{t > 0 : \x \in tB\} ,
\]
the inflation factor by which \( B \) has to be blown up before it reaches \( \x \). The right-hand side makes sense for sets that are not unit balls, and this is the formula to study.

*The gauge of a convex set measures a vector by how far the set must be inflated to reach it.*

::: {#def-gauge}
[Gauge]

Let \( K \subseteq \nR^n \) be convex, with \( \0 \) an **interior point** of \( K \). The **gauge** (or **Minkowski functional**) of \( K \) is the function \( p_K \colon \nR^n \to \nR \) given by
\[
p_K(\x) = \inf\{t > 0 : \x \in tK\} .
\]
:::

The infimum exists. Choose \( r > 0 \) with every \( \y \) satisfying \( \norm{\y}_2 < r \) in \( K \). If \( t > \norm{\x}_2/r \), then \( \norm{\x/t}_2 < r \), so \( \x/t \in K \) and \( \x \in tK \). So the set of admissible \( t \) is non-empty, and it is bounded below by \( 0 \); by **the completeness of \( \nR \), fact (A1) of Chapter 15's introduction**, it has a greatest lower bound, and
\[
0 \le p_K(\x) \le \norm{\x}_2/r \qquad \text{for every } \x \in \nR^n .
\]
The interior point is what makes \( p_K \) finite. For the segment \( [-\e_1, \e_1] \subseteq \nR^2 \), which has no interior points, the vector \( \e_2 \) lies in no multiple \( tK \), and the formula would give the infimum of the empty set.

::: {#prp-gauge-properties}
[Properties of the Gauge]

Let \( K \subseteq \nR^n \) be convex with \( \0 \) an interior point, and let \( \x \in \nR^n \).

::: {.enumerate options="label=(\alph*)"}
1. \( \x \in tK \) for **every** \( t > p_K(\x) \).
2. \( p_K \) is sublinear (@def-sublinear-functional).
3. \( \{\x : p_K(\x) < 1\} \subseteq K \subseteq \{\x : p_K(\x) \le 1\} \).
4. If \( K \) is closed, then \( K = \{\x : p_K(\x) \le 1\} \).
:::
:::

::: {.idea}
Everything comes from one observation, (a): since \( \0 \in K \) and \( K \) is convex, shrinking a point of \( K \) towards \( \0 \) keeps it in \( K \), so the admissible \( t \) form a whole half-line. Subadditivity is then convexity applied to \( \x/s \) and \( \y/t \) with weights proportional to \( s \) and \( t \).
:::

::: {.proof}
(a) Let \( t > p_K(\x) \). By the definition of an infimum there is \( s \) with \( p_K(\x) \le s < t \) and \( \x \in sK \), so \( \x/s \in K \). Since \( \0 \in K \) and \( K \) is convex,
\[
\frac{\x}{t} = \frac{s}{t}\cdot\frac{\x}{s} + \Bigl(1 - \frac{s}{t}\Bigr)\0 \in K ,
\]
that is, \( \x \in tK \).

(b) Let \( \lambda > 0 \). Since \( \lambda\x \in tK \) exactly when \( \x \in (t/\lambda)K \), the admissible \( t \) for \( \lambda\x \) are \( \lambda \) times those for \( \x \), and \( p_K(\lambda\x) = \lambda p_K(\x) \). For \( \lambda = 0 \), \( \0 \in tK \) for every \( t > 0 \), so \( p_K(\0) = 0 \). For subadditivity, let \( \varepsilon > 0 \), \( s = p_K(\x) + \varepsilon \) and \( t = p_K(\y) + \varepsilon \). By (a), \( \x/s \) and \( \y/t \) lie in \( K \), so by convexity
\[
\frac{\x + \y}{s + t} = \frac{s}{s + t}\cdot\frac{\x}{s} + \frac{t}{s + t}\cdot\frac{\y}{t} \in K .
\]
Hence \( p_K(\x + \y) \le s + t = p_K(\x) + p_K(\y) + 2\varepsilon \), for every \( \varepsilon > 0 \), and so \( p_K(\x + \y) \le p_K(\x) + p_K(\y) \).

(c) If \( p_K(\x) < 1 \), then \( \x \in 1\cdot K \) by (a). If \( \x \in K \), then \( t = 1 \) is admissible, so \( p_K(\x) \le 1 \).

(d) Let \( p_K(\x) \le 1 \). By (a), \( \x \in (1 + 1/k)K \) for every \( k \ge 1 \), so the points \( \x/(1 + 1/k) \) lie in \( K \). They converge to \( \x \), and \( K \) is closed, so \( \x \in K \). With (c) this gives \( K = \{p_K \le 1\} \).
:::

The gauge of a unit ball is its norm, by the computation that opened this section. A second example: for the rectangle \( K = [-2, 2] \times [-1, 1] \subseteq \nR^2 \), a vector lies in \( tK \) exactly when \( \lvert x_1\rvert \le 2t \) and \( \lvert x_2\rvert \le t \), so
\[
p_K(\x) = \max\bigl(\tfrac12\lvert x_1\rvert,\ \lvert x_2\rvert\bigr) ,
\]
a weighted \( \infty \)-norm of the kind in @exm-induced-and-weighted-norms (b). At the degenerate extreme, \( K = \nR^n \) lies in every \( tK \), and \( p_K \) is identically \( 0 \): sublinear, but no norm.

The next theorem says exactly when a gauge is a norm. Its part (b) records the facts about unit balls that make the match perfect.

::: {#thm-gauge-is-norm}
[Convex Bodies and Norms]

::: {.enumerate options="label=(\alph*)"}
1. Let \( K \subseteq \nR^n \) be **closed, bounded, convex** and **symmetric** (\( -K = K \)), with \( \0 \) an interior point. Then \( p_K \) is a norm on \( \nR^n \), and its closed unit ball is \( K \).
2. Conversely, the closed unit ball \( B \) of any norm \( \norm{\cdot} \) on \( \nR^n \) is closed, bounded, convex and symmetric, with \( \0 \) an interior point, and \( p_B = \norm{\cdot} \).
:::

So the norms on \( \nR^n \) correspond one to one with the sets described in (a).
:::

::: {.idea}
Sublinearity is two thirds of a norm, and @prp-gauge-properties already has it. The missing third is absolute homogeneity for a scalar \( c < 0 \), which is what symmetry buys, and positive definiteness, which is what boundedness buys: a non-zero vector cannot fit inside every shrunken copy \( tK \) of a bounded set. Closedness makes the unit ball of \( p_K \) equal to \( K \) rather than squeezed between the two sets of @prp-gauge-properties (c).
:::

::: {.proof}
(a) By @prp-gauge-properties (b), \( p_K \) is sublinear, which gives (N3) and (N2) for \( c \ge 0 \). For \( c < 0 \), symmetry gives \( \x \in tK \) if and only if \( -\x \in t(-K) = tK \), so \( p_K(-\x) = p_K(\x) \) and \( p_K(c\x) = \lvert c\rvert p_K(-\x) = \lvert c\rvert p_K(\x) \). For (N1), \( p_K \ge 0 \) by definition. Let \( R \) be such that \( \norm{\y}_2 \le R \) for all \( \y \in K \). If \( p_K(\x) = 0 \), then \( \x \in tK \) for every \( t > 0 \) by @prp-gauge-properties (a), so \( \norm{\x}_2 \le tR \) for every \( t > 0 \), and \( \x = \0 \). So \( p_K \) is a norm, and its closed unit ball \( \{p_K \le 1\} \) is \( K \) by @prp-gauge-properties (d).

(b) Chapter 15 §01 showed, right after @def-unit-ball, that \( B \) is convex and symmetric. By @thm-norm-equivalence there are constants \( 0 < m \le M \) with \( m\norm{\x}_2 \le \norm{\x} \le M\norm{\x}_2 \). If \( \norm{\x} \le 1 \), then \( \norm{\x}_2 \le 1/m \), so \( B \) is bounded. If \( \norm{\x}_2 < 1/M \), then \( \norm{\x} < 1 \), so \( \0 \) is an interior point. If \( \x_k \in B \) and \( \x_k \to \x \), then \( \lvert\norm{\x_k} - \norm{\x}\rvert \le \norm{\x_k - \x} \le M\norm{\x_k - \x}_2 \to 0 \) by @lem-reverse-triangle-norm, and \( \norm{\x} \le 1 \) because a non-strict inequality survives the limit; so \( B \) is closed. Finally, \( \x \in tB \) exactly when \( t \ge \norm{\x} \), for \( t > 0 \), so \( p_B(\x) = \norm{\x} \) (for \( \x = \0 \), the infimum of all \( t > 0 \) is \( 0 \)). This proves the theorem.
:::

**This is the converse of Chapter 15's "every unit ball is convex".** There, a norm produced a convex symmetric set, the ball of @def-unit-ball, and convexity was what the triangle inequality bought. Here a convex symmetric set produces a norm, and the triangle inequality is what convexity buys: the subadditivity step in @prp-gauge-properties (b) is the convexity of \( K \), used once. Norms and closed bounded symmetric convex sets with \( \0 \) inside are the same objects seen two ways, one analytic, one geometric.

Each hypothesis in (a) carries one clause of @def-norm, and dropping one breaks exactly that clause.

- **Drop symmetry.** The triangle \( T = \{\x : x_1 \ge -1,\ x_2 \ge -1,\ x_1 + x_2 \le 1\} \), with vertices \( (-1,-1) \), \( (2,-1) \), \( (-1,2) \), is closed, bounded and convex, and contains the disc of radius \( \tfrac12 \) about \( \0 \). A vector lies in \( tT \) exactly when \( -x_1 \le t \), \( -x_2 \le t \) and \( x_1 + x_2 \le t \), so
\[
p_T(\x) = \max\bigl(-x_1,\ -x_2,\ x_1 + x_2\bigr) ,
\]
which is never negative, since the three numbers add up to \( 0 \). This is sublinear and satisfies (N1), but \( p_T\bigl((1,1)\bigr) = 2 \) while \( p_T\bigl((-1,-1)\bigr) = 1 \), so (N2) fails at \( c = -1 \).
- **Drop boundedness.** The strip \( S = \{\x \in \nR^2 : \lvert x_2\rvert \le 1\} \) is closed, convex and symmetric, and \( p_S(\x) = \lvert x_2\rvert \). Now (N2) and (N3) hold but (N1) fails: \( p_S(\e_1) = 0 \). This is the seminorm of @exm-norm-non-example (b).

::: {.check}
Let \( K \) be the open unit disc \( \{\x \in \nR^2 : \norm{\x}_2 < 1\} \), which is bounded, symmetric and convex (if \( \norm{\x}_2, \norm{\y}_2 < 1 \) and \( 0 \le t \le 1 \), then \( \norm{(1 - t)\x + t\y}_2 \le (1 - t)\norm{\x}_2 + t\norm{\y}_2 < 1 \)) but not closed. What is \( p_K \), and what is its closed unit ball?
:::

::: {.solution}
For \( t > 0 \), \( \x \in tK \) exactly when \( \norm{\x}_2 < t \), so the admissible \( t \) form the interval \( (\norm{\x}_2, \infty) \) and \( p_K(\x) = \norm{\x}_2 \). So \( p_K \) is a norm after all, but its closed unit ball is the closed disc, not \( K \). Closedness is used only for the last claim of @thm-gauge-is-norm (a), through @prp-gauge-properties (d).
:::

## Support functions

§03 described a closed convex set from the outside: by @cor-closed-convex-halfspaces it is the intersection of the closed half-spaces containing it. For a fixed normal vector \( \y \), the half-spaces \( \{\x : \inner{\x}{\y} \le c\} \) containing \( K \) are those with \( c \ge \inner{\x}{\y} \) for every \( \x \in K \), and the tightest of them has \( c = \sup_{\x \in K}\inner{\x}{\y} \). That number, as a function of the direction \( \y \), deserves a name.

*The support function of a set records, for each direction, how far the set reaches in that direction.*

::: {#def-support-function}
[Support Function]

Let \( K \subseteq \nR^n \) be **non-empty**. The **support function** of \( K \) is
\[
h_K(\y) = \sup_{\x \in K}\inner{\x}{\y} , \qquad \y \in \nR^n ,
\]
with the value \( +\infty \) when the numbers \( \inner{\x}{\y} \), \( \x \in K \), are unbounded above.
:::

When the numbers are bounded above, the supremum exists by (A1). If \( K \) is **bounded**, say \( \norm{\x}_2 \le R \) on \( K \), then \( \inner{\x}{\y} \le R\norm{\y}_2 \) by @thm-cauchy-schwarz, so \( h_K \) is real-valued. If \( K \) is **compact**, the supremum is a maximum by **the extreme value theorem, fact (A4) of Chapter 15's introduction**, since \( \x \mapsto \inner{\x}{\y} \) is continuous: \( \lvert\inner{\x}{\y} - \inner{\x'}{\y}\rvert \le \norm{\x - \x'}_2\norm{\y}_2 \). For a unit vector \( \y \), the hyperplane \( \{\inner{\cdot}{\y} = h_K(\y)\} \) is the one with normal \( \y \) that touches \( K \) from outside, and \( h_K(\y) \) is its signed distance from \( \0 \).

Some examples, each computed from the definition.

- **A point.** \( h_{\{\x_0\}}(\y) = \inner{\x_0}{\y} \), a linear function.
- **The Euclidean ball.** \( h_{B_2}(\y) = \norm{\y}_2 \): at most that by @thm-cauchy-schwarz, and attained at \( \x = \y/\norm{\y}_2 \) when \( \y \ne \0 \).
- **The standard simplex** \( \conv\{\e_1, \dots, \e_n\} \). By @thm-convex-hull-combinations its points are \( \sum_i t_i\e_i \) with \( t_i \ge 0 \) and \( \sum_i t_i = 1 \), and \( \sum_i t_iy_i \le \max_i y_i \), with equality at a vertex \( \e_k \) where \( y_k \) is largest. So \( h(\y) = \max_i y_i \).
- **A segment.** \( h_{[-\e_1, \e_1]}(\y) = \lvert y_1\rvert \) in \( \nR^2 \).
- **An unbounded set.** For the half-line \( \{t\e_1 : t \ge 0\} \), \( h(\y) = 0 \) if \( y_1 \le 0 \) and \( h(\y) = +\infty \) if \( y_1 > 0 \).

::: {#prp-support-function-properties}
[Properties of the Support Function]

Let \( K, L \subseteq \nR^n \) be non-empty and bounded.

::: {.enumerate options="label=(\alph*)"}
1. \( h_K \) is sublinear.
2. If \( K \subseteq L \), then \( h_K \le h_L \).
3. \( h_{\conv K} = h_K \).
:::
:::

::: {.idea}
A supremum of linear functions of \( \y \) inherits whatever inequalities each of them satisfies, which gives (a) and (b). For (c), a linear function takes on a convex combination a weighted average of its values, and an average never exceeds the largest value.
:::

::: {.proof}
(a) For \( \x \in K \), \( \inner{\x}{\y + \z} = \inner{\x}{\y} + \inner{\x}{\z} \le h_K(\y) + h_K(\z) \), and taking the supremum over \( \x \) gives \( h_K(\y + \z) \le h_K(\y) + h_K(\z) \). For \( t > 0 \), \( \inner{\x}{t\y} = t\inner{\x}{\y} \), and a positive factor comes out of a supremum; for \( t = 0 \) both sides are \( 0 \), as \( K \ne \emptyset \).

(b) A supremum over a larger set is at least as large.

(c) Since \( K \subseteq \conv K \), (b) gives \( h_K \le h_{\conv K} \), once we know \( \conv K \) is bounded: it lies in the ball \( \{\norm{\x}_2 \le R\} \), which is convex and contains \( K \) (@def-convex-hull). Conversely, by @thm-convex-hull-combinations a point of \( \conv K \) is \( \x = \sum_i t_i\x_i \) with \( \x_i \in K \), \( t_i \ge 0 \), \( \sum_i t_i = 1 \), and then
\[
\inner{\x}{\y} = \sum_i t_i\inner{\x_i}{\y} \le \sum_i t_i\,h_K(\y) = h_K(\y) .
\]
So \( h_{\conv K} \le h_K \).
:::

::: {.warning}
**A support function cannot see gaps.** The two-point set \( \{\e_1, -\e_1\} \) and the segment \( [-\e_1, \e_1] \) in \( \nR^2 \) have the same support function \( \lvert y_1\rvert \), by @prp-support-function-properties (c). So \( h_K \) does not determine \( K \) in general; it determines only the convex hull, and the next theorem shows that among closed convex sets it determines the set.
:::

Here is the promised formula. It is @cor-closed-convex-halfspaces with the family of half-spaces indexed by their normals.

::: {#thm-support-function-determines}
[The Support Function Determines a Closed Convex Set]

Let \( K, L \subseteq \nR^n \) be non-empty, closed and convex. Then

::: {.enumerate options="label=(\alph*)"}
1. \( K = \{\x \in \nR^n : \inner{\x}{\y} \le h_K(\y) \text{ for every } \y \in \nR^n\} \);
2. \( K \subseteq L \) if and only if \( h_K(\y) \le h_L(\y) \) for every \( \y \); in particular \( K = L \) if and only if \( h_K = h_L \).
:::

Here \( h_K \) and \( h_L \) may take the value \( +\infty \), with \( a \le +\infty \) for every \( a \).
:::

::: {.idea}
Part (a) is @cor-closed-convex-halfspaces, with the half-space for the normal \( \y \) chosen as tight as possible, at level \( h_K(\y) \). Part (b) then compares the two families of half-spaces normal by normal.
:::

::: {.proof}
(a) Every \( \x \in K \) satisfies \( \inner{\x}{\y} \le h_K(\y) \) by definition. Conversely let \( \x \notin K \). By @thm-separation-point there is \( \a \ne \0 \) with \( \inner{\a}{\z} \le \inner{\a}{\x} - \norm{\a}_2^2 \) for all \( \z \in K \). Hence \( h_K(\a) \le \inner{\a}{\x} - \norm{\a}_2^2 < \inner{\x}{\a} \), and \( \x \) violates the condition at \( \y = \a \).

(b) If \( K \subseteq L \), then \( h_K \le h_L \) because a supremum over a larger set is at least as large. Conversely, suppose \( h_K \le h_L \) and let \( \x \in K \). For every \( \y \), \( \inner{\x}{\y} \le h_K(\y) \le h_L(\y) \), so \( \x \in L \) by (a) applied to \( L \). The last statement follows by applying this in both directions.
:::

## Polar sets

The condition \( h_K(\y) \le 1 \) cuts out a set of directions, and that set turns out to be a mirror image of \( K \).

::: {#def-polar-set}
[Polar Set]

The **polar** of a set \( K \subseteq \nR^n \) is
\[
K^{\circ} = \{\y \in \nR^n : \inner{\x}{\y} \le 1 \text{ for every } \x \in K\} .
\]
:::

For non-empty \( K \), \( K^{\circ} = \{\y : h_K(\y) \le 1\} \). The polar is always closed, convex and contains \( \0 \), being an intersection of closed half-spaces \( \{\y : \inner{\x}{\y} \le 1\} \), one for each \( \x \in K \). Two examples:

- \( (B_2)^{\circ} = B_2 \), because \( h_{B_2}(\y) = \norm{\y}_2 \).
- For the single point \( K = \{\e_1\} \) in \( \nR^2 \), \( K^{\circ} = \{\y : y_1 \le 1\} \), a half-plane. Its polar consists of the \( \x \) with \( x_1y_1 + x_2y_2 \le 1 \) whenever \( y_1 \le 1 \). Letting \( y_2 \) run over \( \nR \) forces \( x_2 = 0 \), letting \( y_1 \to -\infty \) forces \( x_1 \ge 0 \), and \( y_1 = 1 \) forces \( x_1 \le 1 \). So \( K^{\circ\circ} \) is the segment \( [\0, \e_1] \), which is not \( K \).

The second example shows what the theorem must assume.

::: {#thm-bipolar}
[Bipolar Theorem]

Let \( K \subseteq \nR^n \) be closed and convex with \( \0 \in K \). Then \( K^{\circ\circ} = K \).
:::

::: {.idea}
One inclusion is the definition read twice. For the other, cut a point \( \x \notin K \) off with @thm-separation-point, and rescale the normal so that \( K \) lies in \( \{\inner{\cdot}{\b} \le 1\} \) while \( \x \) does not. That rescaled normal lies in \( K^{\circ} \) and witnesses \( \x \notin K^{\circ\circ} \); the rescaling needs \( \0 \in K \).
:::

::: {.proof}
\( (\supseteq) \) Let \( \x \in K \). For every \( \y \in K^{\circ} \), \( \inner{\x}{\y} \le 1 \) by the definition of \( K^{\circ} \). Hence \( \x \in K^{\circ\circ} \).

\( (\subseteq) \) Let \( \x \notin K \). By @thm-separation-point there is \( \a \ne \0 \) with \( \inner{\a}{\z} \le \inner{\a}{\x} - \norm{\a}_2^2 \) for all \( \z \in K \). Put \( s = \sup_{\z \in K}\inner{\a}{\z} \), which exists by (A1); since \( \0 \in K \), \( s \ge 0 \), and \( s < \inner{\a}{\x} \). If \( s > 0 \), let \( \b = \a/s \). Then \( \inner{\z}{\b} \le 1 \) for all \( \z \in K \), so \( \b \in K^{\circ} \), while \( \inner{\x}{\b} > 1 \). If \( s = 0 \), then \( \inner{\a}{\x} > 0 \); let \( \b = 2\a/\inner{\a}{\x} \). Then \( \inner{\z}{\b} \le 0 \le 1 \) on \( K \), so \( \b \in K^{\circ} \), while \( \inner{\x}{\b} = 2 > 1 \). In both cases \( \x \notin K^{\circ\circ} \).
:::

The hypothesis \( \0 \in K \) was used to make \( s \ge 0 \), so that dividing by \( s \) keeps the direction of the inequality; the counterexample \( \{\e_1\} \) above is exactly a closed convex set without it.

## Dual norms

Chapter 15 measured vectors (@def-norm) and matrices (@def-operator-norm). A third kind of object sits between them and was never measured: a linear functional on \( \nR^n \), which by @thm-functionals-on-fn is \( \x \mapsto \y\tp\x = \inner{\x}{\y} \) for exactly one \( \y \). How big is it?

When \( \x \) is measured by \( \norm{\cdot}_2 \), @thm-cauchy-schwarz answers: \( \lvert\inner{\x}{\y}\rvert \le \norm{\x}_2\norm{\y}_2 \), and the constant \( \norm{\y}_2 \) is the best possible. When \( \x \) is measured by another norm, the question is the same — what is the smallest \( c \) with \( \lvert\inner{\x}{\y}\rvert \le c\norm{\x} \) for every \( \x \)? — and the answer is the largest value of \( \inner{\x}{\y} \) over the unit ball. That is the support function of \( B \), and it is also the operator norm of the \( 1 \times n \) matrix \( \y\tp \). An expression that turns up three ways deserves a name.

*The dual norm of \( \y \) is the most that the functional \( \inner{\cdot}{\y} \) can extract from a vector of norm at most one.*

::: {#def-dual-norm}
[Dual Norm]

Let \( \norm{\cdot} \) be a norm on \( \nR^n \), with closed unit ball \( B \). The **dual norm** of \( \norm{\cdot} \) is the function \( \norm{\cdot}_{*} \colon \nR^n \to \nR \) given by
\[
\norm{\y}_{*} = \max\{\inner{\x}{\y} : \x \in \nR^n,\ \norm{\x} \le 1\} = h_B(\y) .
\]
:::

The maximum exists. By @thm-gauge-is-norm (b), \( B \) is non-empty, closed and bounded, hence compact by @cor-closed-bounded-compact, which rests on **fact (A3) of Chapter 15's introduction**; and \( \x \mapsto \inner{\x}{\y} \) is continuous, so by **the extreme value theorem, fact (A4)**, it attains its maximum on \( B \).

In words: fix \( \y \), let \( \x \) range over the vectors that the **given** norm calls short, and record the largest value of \( \inner{\x}{\y} \). The inner product is part of the definition, and so is the norm; changing either changes \( \norm{\cdot}_{*} \). No absolute value is needed in the maximum: \( B \) is symmetric, so replacing \( \x \) by \( -\x \) shows that the largest value of \( \inner{\x}{\y} \) on \( B \) is also the largest value of \( \lvert\inner{\x}{\y}\rvert \).

::: {#prp-dual-norm-properties}
[Properties of the Dual Norm]

Let \( \norm{\cdot} \) be a norm on \( \nR^n \), with closed unit ball \( B \).

::: {.enumerate options="label=(\alph*)"}
1. \( \norm{\cdot}_{*} \) is a norm on \( \nR^n \).
2. \( \lvert\inner{\x}{\y}\rvert \le \norm{\x}\,\norm{\y}_{*} \) for all \( \x, \y \), and \( \norm{\y}_{*} \) is the smallest constant \( c \) with \( \lvert\inner{\x}{\y}\rvert \le c\norm{\x} \) for every \( \x \).
3. \( \norm{\y}_{*} \) is the operator norm (@def-operator-norm) of the \( 1 \times n \) matrix \( \y\tp \), with \( \norm{\cdot} \) on \( \nR^n \) and \( \lvert\cdot\rvert \) on \( \nR \).
4. The closed unit ball of \( \norm{\cdot}_{*} \) is the polar \( B^{\circ} \).
:::
:::

::: {.idea}
Each norm axiom for \( \norm{\cdot}_{*} \) is checked one \( \x \in B \) at a time and then survives the maximum; (N1) needs a good test vector, \( \y \) itself rescaled into \( B \). For (b), rescale any \( \x \ne \0 \) into \( B \). Parts (c) and (d) only compare definitions.
:::

::: {.proof}
(a) (N1): \( \x = \0 \in B \) gives \( \norm{\y}_{*} \ge 0 \). If \( \y \ne \0 \), then \( \x = \y/\norm{\y} \in B \) gives \( \norm{\y}_{*} \ge \norm{\y}_2^2/\norm{\y} > 0 \). (N2): for \( c \ge 0 \), \( \max_B\inner{\x}{c\y} = c\max_B\inner{\x}{\y} \); for \( c < 0 \), \( \inner{\x}{c\y} = \lvert c\rvert\inner{-\x}{\y} \), and \( -\x \) runs over \( B \) as \( \x \) does, by (N2) for \( \norm{\cdot} \). (N3): for \( \x \in B \), \( \inner{\x}{\y + \z} = \inner{\x}{\y} + \inner{\x}{\z} \le \norm{\y}_{*} + \norm{\z}_{*} \); take the maximum over \( \x \).

(b) For \( \x = \0 \) there is nothing to prove. For \( \x \ne \0 \), \( \x/\norm{\x} \in B \), so \( \pm\inner{\x}{\y}/\norm{\x} = \inner{\pm\x/\norm{\x}}{\y} \le \norm{\y}_{*} \), using that \( B \) is symmetric. If \( c \) is any constant with \( \lvert\inner{\x}{\y}\rvert \le c\norm{\x} \) for all \( \x \), then \( \inner{\x}{\y} \le c \) on \( B \), so \( \norm{\y}_{*} \le c \).

(c) By @def-operator-norm and the equivalent descriptions that follow it in Chapter 15 §03, the operator norm of \( \y\tp \) is \( \max\{\lvert\y\tp\x\rvert : \norm{\x} \le 1\} \), which is \( \norm{\y}_{*} \) by the remark after @def-dual-norm.

(d) \( \norm{\y}_{*} \le 1 \) exactly when \( \inner{\x}{\y} \le 1 \) for every \( \x \in B \), which is the definition of \( \y \in B^{\circ} \) (@def-polar-set).
:::

Part (b) is Cauchy–Schwarz for an arbitrary norm, with the price that the two factors are measured differently. Now the three norms of Chapter 15.

::: {#prp-dual-of-one-two-infinity}
[Duals of the 1-, 2- and Infinity-Norms]

On \( \nR^n \) with the dot product,

::: {.enumerate options="label=(\alph*)"}
1. the dual of \( \norm{\cdot}_1 \) is \( \norm{\cdot}_\infty \);
2. the dual of \( \norm{\cdot}_\infty \) is \( \norm{\cdot}_1 \);
3. the dual of \( \norm{\cdot}_2 \) is \( \norm{\cdot}_2 \).
:::
:::

::: {.idea}
Each part is an upper bound and a witness, the same pattern as @thm-operator-norm-formulas. For the \( 1 \)-norm, all of the budget \( \norm{\x}_1 \le 1 \) goes on the coordinate where \( \lvert y_k\rvert \) is largest. For the \( \infty \)-norm, every coordinate can be spent at once, each with the sign of \( y_i \), so nothing cancels. For the \( 2 \)-norm, the witness is \( \y \) itself, rescaled.
:::

::: {.proof}
(a) For \( \norm{\x}_1 \le 1 \), \( \inner{\x}{\y} \le \sum_i\lvert x_i\rvert\lvert y_i\rvert \le \norm{\y}_\infty\sum_i\lvert x_i\rvert \le \norm{\y}_\infty \). Choose \( k \) with \( \lvert y_k\rvert = \norm{\y}_\infty \), and let \( \x = \pm\e_k \) with the sign of \( y_k \) (either sign if \( y_k = 0 \)). Then \( \norm{\x}_1 = 1 \) and \( \inner{\x}{\y} = \lvert y_k\rvert = \norm{\y}_\infty \).

(b) For \( \norm{\x}_\infty \le 1 \), \( \inner{\x}{\y} \le \sum_i\lvert x_i\rvert\lvert y_i\rvert \le \sum_i\lvert y_i\rvert = \norm{\y}_1 \). Let \( x_i = 1 \) if \( y_i \ge 0 \) and \( x_i = -1 \) if \( y_i < 0 \). Then \( \norm{\x}_\infty = 1 \) and \( \inner{\x}{\y} = \sum_i\lvert y_i\rvert = \norm{\y}_1 \).

(c) For \( \norm{\x}_2 \le 1 \), \( \inner{\x}{\y} \le \norm{\x}_2\norm{\y}_2 \le \norm{\y}_2 \) by @thm-cauchy-schwarz. For \( \y \ne \0 \), \( \x = \y/\norm{\y}_2 \) gives equality; for \( \y = \0 \) both sides are \( 0 \).
:::

So the \( 1 \)- and \( \infty \)-norms are each other's duals, and the Euclidean norm is its own. In the language of polars, (a) and (b) say \( (B_1)^{\circ} = B_\infty \) and \( (B_\infty)^{\circ} = B_1 \): the diamond and the square of Chapter 15's picture are polar to each other, and the disc is polar to itself. Part (b) of @prp-dual-norm-properties now reads \( \lvert\inner{\x}{\y}\rvert \le \norm{\x}_1\norm{\y}_\infty \), the simplest of a family of inequalities. The general member pairs \( \norm{\cdot}_p \) with \( \norm{\cdot}_q \), \( \tfrac1p + \tfrac1q = 1 \); it is **Hölder's inequality**, and §11 of this chapter proves it and deduces that the dual of \( \norm{\cdot}_p \) is \( \norm{\cdot}_q \) for every \( 1 < p < \infty \). The degenerate case \( n = 1 \) is worth one line: every norm on \( \nR \) is \( \norm{x} = a\lvert x\rvert \) with \( a > 0 \), its ball is \( [-1/a, 1/a] \), and \( \norm{y}_{*} = \lvert y\rvert/a \).

**A non-example by minimal change.** Keep the formula \( \max_K\inner{\x}{\y} \), and replace the symmetric ball by the triangle \( K = \conv\{(-1,-1), (2,-1), (-1,2)\} \), which is compact and convex and has \( \0 \) inside. By @prp-support-function-properties (c), \( h_K(\y) \) is the largest of \( -y_1 - y_2 \), \( 2y_1 - y_2 \) and \( -y_1 + 2y_2 \). It is sublinear by @prp-support-function-properties (a), and positive at every \( \y \ne \0 \), since the three numbers add up to \( 0 \) and are not all zero. But \( h_K(\e_1) = 2 \) and \( h_K(-\e_1) = 1 \), so (N2) fails at \( c = -1 \). Symmetry of the ball is exactly what makes a dual norm a norm.

Why this definition, and not another? The measurement of a functional must be compatible with the measurement of its inputs, in the sense that \( \lvert\inner{\x}{\y}\rvert \le c\norm{\x} \) for every \( \x \), and @prp-dual-norm-properties (b) says that \( \norm{\y}_{*} \) is the **smallest** compatible \( c \). Any larger choice would be a bound, not a measurement. Abstractly, the dual norm lives on the dual space: for \( \varphi \in (\nR^n)^{*} \) one would put \( \norm{\varphi} = \max_{\norm{\x} \le 1}\varphi(\x) \), and the dot product is used only to name \( \varphi \) by a vector, through @thm-functionals-on-fn. That is why a different inner product on \( \nR^n \) gives a different formula for "the same" dual norm. The name is standard: the dual space carries the dual norm.

::: {.warning}
**A larger norm has a smaller dual.** If \( \norm{\x}_a \le \norm{\x}_b \) for all \( \x \), then the ball of \( \norm{\cdot}_b \) lies inside the ball of \( \norm{\cdot}_a \), and a maximum over a smaller set is smaller: \( \norm{\y}_{b*} \le \norm{\y}_{a*} \). For instance \( N(\x) = 2\norm{\x}_2 \) has ball of radius \( \tfrac12 \) and dual \( N_{*}(\y) = \tfrac12\norm{\y}_2 \), not \( 2\norm{\y}_2 \). Scaling a norm up scales its dual down.
:::

Chapter 15 measured vectors and matrices but never a linear functional; @def-dual-norm fills that gap, and @prp-dual-norm-properties (c) shows it is exactly an operator norm of Chapter 15, the one for \( 1 \times n \) matrices. The one question it leaves open is whether the construction loses information.

## The dual of the dual

Apply the construction twice. Since \( \norm{\cdot}_{*} \) is a norm, it has a dual \( \norm{\cdot}_{**} \), and the natural guess is that we are back where we started. For the three norms of @prp-dual-of-one-two-infinity this is visible: \( 1 \to \infty \to 1 \) and \( 2 \to 2 \to 2 \). In general it is a theorem, and its proof is a supporting hyperplane.

::: {#thm-dual-dual-norm}
[The Dual of the Dual Norm]

For every norm \( \norm{\cdot} \) on \( \nR^n \), \( \norm{\cdot}_{**} = \norm{\cdot} \).
:::

::: {.idea}
One inequality is Cauchy–Schwarz for dual norms. For the other, take \( \x \) on the unit sphere of \( \norm{\cdot} \). It is on the edge of the ball \( B \), so §03 provides a supporting hyperplane of \( B \) at \( \x \). Its normal \( \a \) is a direction in which \( B \) reaches no further than \( \x \) does, so the maximum defining \( \norm{\a}_{*} \) is attained **at** \( \x \); rescaling \( \a \) produces a functional of dual norm \( 1 \) that takes the value \( 1 \) at \( \x \).
:::

::: {.proof}
Let \( \x \in \nR^n \). For every \( \y \) with \( \norm{\y}_{*} \le 1 \), @prp-dual-norm-properties (b) gives \( \inner{\x}{\y} \le \norm{\x}\norm{\y}_{*} \le \norm{\x} \). By @def-dual-norm applied to \( \norm{\cdot}_{*} \), whose unit ball is \( \{\y : \norm{\y}_{*} \le 1\} \), this says \( \norm{\x}_{**} \le \norm{\x} \).

For the reverse inequality, both sides vanish at \( \x = \0 \), and both are absolutely homogeneous, so it suffices to take \( \norm{\x} = 1 \). Then \( \x \in B \), but \( \x \) is not an interior point of \( B \): the vectors \( (1 + 1/k)\x \) have norm \( 1 + 1/k > 1 \) and \( \norm{(1 + 1/k)\x - \x}_2 = \norm{\x}_2/k \to 0 \). By @thm-supporting-hyperplane, applied to the convex set \( B \) and the point \( \x \), there is \( \a \ne \0 \) with \( \inner{\z}{\a} \le \inner{\x}{\a} \) for every \( \z \in B \). Since \( \x \in B \), the maximum in @def-dual-norm is attained at \( \x \):
\[
\norm{\a}_{*} = \max_{\z \in B}\inner{\z}{\a} = \inner{\x}{\a} .
\]
By @prp-dual-norm-properties (a), \( \norm{\a}_{*} > 0 \). Let \( \y = \a/\norm{\a}_{*} \). Then \( \norm{\y}_{*} = 1 \) and \( \inner{\x}{\y} = 1 \). Hence \( \norm{\x}_{**} \ge 1 = \norm{\x} \). This proves the theorem.
:::

Alternatively, the vector \( \y \) can be obtained from Hahn–Banach. @cor-hahn-banach-norm, applied to \( U = \Span(\x) \) and \( f(t\x) = t\norm{\x} \), gives a functional \( F \) with \( F(\x) = \norm{\x} \) and \( \lvert F\rvert \le \norm{\cdot} \); writing \( F = \inner{\cdot}{\y} \) by @thm-functionals-on-fn, the second property says \( \norm{\y}_{*} \le 1 \) by @prp-dual-norm-properties (b), so \( \norm{\x}_{**} \ge \inner{\x}{\y} = \norm{\x} \). So the analytic and the geometric forms of §03 each prove the theorem, which is one more sign that they are the same fact.

Read with the definition of \( \norm{\cdot}_{**} \) unwound, the theorem is a formula for the original norm.

::: {#cor-norm-as-max}
[A Norm Is a Maximum of Linear Functions]

For every norm \( \norm{\cdot} \) on \( \nR^n \) and every \( \x \in \nR^n \),
\[
\norm{\x} = \max\{\inner{\x}{\y} : \norm{\y}_{*} \le 1\} ,
\]
and when \( \x \ne \0 \) the maximum is attained at some \( \y \) with \( \norm{\y}_{*} = 1 \).
:::

::: {.proof}
The right-hand side is \( \norm{\x}_{**} \) by @def-dual-norm applied to \( \norm{\cdot}_{*} \), and it equals \( \norm{\x} \) by @thm-dual-dual-norm. For \( \x \ne \0 \), the proof of @thm-dual-dual-norm, applied to \( \x/\norm{\x} \), produced \( \y \) with \( \norm{\y}_{*} = 1 \) and \( \inner{\x/\norm{\x}}{\y} = 1 \), so \( \inner{\x}{\y} = \norm{\x} \).
:::

So every norm is the support function of the unit ball of its dual, \( \norm{\cdot} = h_{\{\y : \norm{\y}_{*} \le 1\}} \): a maximum of the linear functions \( \x \mapsto \inner{\x}{\y} \), one for each \( \y \) in a compact set. §10 of this chapter shows that a pointwise maximum of linear functions is always convex, and norms (their convexity was already the triangle inequality) are among its first examples.

::: {.check}
For \( \x = (3, -4) \), find a \( \y \) with \( \norm{\y}_\infty = 1 \) and \( \inner{\x}{\y} = \norm{\x}_1 \), and a \( \y \) with \( \norm{\y}_1 = 1 \) and \( \inner{\x}{\y} = \norm{\x}_\infty \).
:::

::: {.solution}
The dual of \( \norm{\cdot}_1 \) is \( \norm{\cdot}_\infty \) (@prp-dual-of-one-two-infinity (a)), so the first \( \y \) is a sign vector: \( \y = (1, -1) \) gives \( 3 + 4 = 7 = \norm{\x}_1 \). The dual of \( \norm{\cdot}_\infty \) is \( \norm{\cdot}_1 \), so the second \( \y \) puts all its weight on the largest coordinate: \( \y = (0, -1) \) gives \( 4 = \norm{\x}_\infty \). Each is the witness from the proof of @prp-dual-of-one-two-infinity, with the roles of \( \x \) and \( \y \) exchanged.
:::

## Operator norms as maxima of bilinear values

The corollary also rewrites Chapter 15's operator norm. Fix a norm \( \norm{\cdot}_\alpha \) on \( \nR^n \) and a norm \( \norm{\cdot}_\beta \) on \( \nR^m \), and write \( \norm{\A}_{\alpha\to\beta} \) for the operator norm of \( \A \in M_{m\times n}(\nR) \) that they induce (@def-operator-norm). By the equivalent descriptions after that definition, \( \norm{\A}_{\alpha\to\beta} = \max\{\norm{\A\x}_\beta : \norm{\x}_\alpha \le 1\} \).

::: {#prp-operator-norm-bilinear}
[Operator Norms through Dual Norms]

Let \( \A \in M_{m \times n}(\nR) \), and let \( \norm{\cdot}_\alpha \), \( \norm{\cdot}_\beta \) be norms on \( \nR^n \) and \( \nR^m \), with duals \( \norm{\cdot}_{\alpha*} \) and \( \norm{\cdot}_{\beta*} \). Then

::: {.enumerate options="label=(\alph*)"}
1. \( \norm{\A}_{\alpha\to\beta} = \max\{\y\tp\A\x : \norm{\x}_\alpha \le 1,\ \norm{\y}_{\beta*} \le 1\} \);
2. \( \norm{\A\tp}_{\beta*\to\alpha*} = \norm{\A}_{\alpha\to\beta} \).
:::
:::

::: {.idea}
Write the outer norm \( \norm{\A\x}_\beta \) as a maximum over its dual ball by @cor-norm-as-max, and the operator norm becomes one maximum over pairs \( (\x, \y) \). Since \( \y\tp\A\x = \x\tp\A\tp\y \), the same double maximum, taken with \( \x \) innermost, is the operator norm of \( \A\tp \), which gives (b).
:::

::: {.proof}
(a) For \( \norm{\x}_\alpha \le 1 \), @cor-norm-as-max in \( \nR^m \) gives \( \norm{\A\x}_\beta = \max\{\y\tp\A\x : \norm{\y}_{\beta*} \le 1\} \). So every value \( \y\tp\A\x \) in the set is at most \( \norm{\A\x}_\beta \le \norm{\A}_{\alpha\to\beta} \). Conversely, choose \( \x_0 \) with \( \norm{\x_0}_\alpha \le 1 \) and \( \norm{\A\x_0}_\beta = \norm{\A}_{\alpha\to\beta} \), which exists by @lem-operator-norm-attained, and then \( \y_0 \) attaining the maximum for \( \norm{\A\x_0}_\beta \). The value \( \y_0\tp\A\x_0 \) equals \( \norm{\A}_{\alpha\to\beta} \), so the maximum exists and has this value.

(b) By the equivalent descriptions after @def-operator-norm, and then @def-dual-norm for \( \norm{\cdot}_{\alpha*} \),
\[
\norm{\A\tp}_{\beta*\to\alpha*}
= \max_{\norm{\y}_{\beta*} \le 1}\norm{\A\tp\y}_{\alpha*}
= \max_{\norm{\y}_{\beta*} \le 1}\ \max_{\norm{\x}_\alpha \le 1}\inner{\x}{\A\tp\y} .
\]
Since \( \inner{\x}{\A\tp\y} = \x\tp\A\tp\y = \y\tp\A\x \), this is the maximum in (a).
:::

With \( \alpha = \beta = \infty \), part (b) and @prp-dual-of-one-two-infinity say \( \norm{\A\tp}_1 = \norm{\A}_\infty \): the largest column sum of \( \A\tp \) is the largest row sum of \( \A \), which is also what @thm-operator-norm-formulas gives directly. With \( \alpha = \beta = 2 \) it says \( \norm{\A\tp}_2 = \norm{\A}_2 \), that is, \( \sigma_1(\A\tp) = \sigma_1(\A) \). For the matrix \( \A = \begin{psmallmatrix} 3 & 0 \\ 4 & 5\end{psmallmatrix} \) of @exm-three-norms-of-a-matrix, \( \norm{\A}_1 = 7 \) and \( \norm{\A}_\infty = 9 \). Its transpose \( \begin{psmallmatrix} 3 & 4 \\ 0 & 5\end{psmallmatrix} \) has column sums \( 3 \) and \( 9 \) and row sums \( 7 \) and \( 5 \), so \( \norm{\A\tp}_1 = 9 = \norm{\A}_\infty \) and \( \norm{\A\tp}_\infty = 7 = \norm{\A}_1 \), as (b) predicts.

## Exercises

### A. Check your understanding

:::: {#exr-gauges-support-functions-dual-norms-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the gauge \( p_K \), the support function \( h_K \) and the dual norm \( \norm{\cdot}_{*} \), stating what each needs of the set or norm involved.
2. Determine whether the following statement is correct, and justify your answer: the support function of every non-empty bounded subset of \( \nR^2 \) is a norm.
3. What is the dual of \( \norm{\cdot}_\infty \) on \( \nR^n \)? What is the dual of that?
4. Which result of §03 does the proof of @thm-dual-dual-norm use, and at which point?
5. Determine whether the following statement is correct, and justify your answer: \( K^{\circ\circ} = K \) for every non-empty closed convex \( K \subseteq \nR^n \).
:::
::::

::: {.solution}
(a) For \( K \) convex with \( \0 \) an interior point, \( p_K(\x) = \inf\{t > 0 : \x \in tK\} \) (@def-gauge). For \( K \) non-empty, \( h_K(\y) = \sup_{\x \in K}\inner{\x}{\y} \), possibly \( +\infty \) (@def-support-function). For a norm \( \norm{\cdot} \) with ball \( B \), \( \norm{\y}_{*} = \max_{\x \in B}\inner{\x}{\y} = h_B(\y) \) (@def-dual-norm).

(b) Incorrect. For \( K = \{\0\} \), \( h_K = 0 \), which violates (N1). For the segment \( [-\e_1, \e_1] \), \( h_K(\y) = \lvert y_1\rvert \) vanishes at \( \e_2 \). Support functions are sublinear (@prp-support-function-properties (a)) but need not be norms.

(c) \( \norm{\cdot}_1 \), by @prp-dual-of-one-two-infinity (b); and the dual of \( \norm{\cdot}_1 \) is \( \norm{\cdot}_\infty \) again, by (a) of the same proposition, as @thm-dual-dual-norm requires.

(d) @thm-supporting-hyperplane, applied to the unit ball \( B \) at a point \( \x \) with \( \norm{\x} = 1 \), to produce a normal \( \a \) at which the maximum defining \( \norm{\a}_{*} \) is attained at \( \x \).

(e) Incorrect. For \( K = \{\e_1\} \) in \( \nR^2 \), \( K^{\circ\circ} \) is the segment \( [\0, \e_1] \). @thm-bipolar needs \( \0 \in K \).
:::

### B. Practice

:::: {#exr-gauges-support-functions-dual-norms-b1}
[B1: A weighted norm and its dual]

On \( \nR^2 \) let \( N(\x) = \max\bigl(\lvert x_1\rvert, 2\lvert x_2\rvert\bigr) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( N_{*}(\y) = \lvert y_1\rvert + \tfrac12\lvert y_2\rvert \).
2. Verify @thm-dual-dual-norm for \( N \) by computing \( N_{**} \) directly.
:::
::::

::: {.solution}
(a) The ball of \( N \) is the rectangle \( \lvert x_1\rvert \le 1 \), \( \lvert x_2\rvert \le \tfrac12 \). On it, \( \inner{\x}{\y} \le \lvert x_1\rvert\lvert y_1\rvert + \lvert x_2\rvert\lvert y_2\rvert \le \lvert y_1\rvert + \tfrac12\lvert y_2\rvert \). The point \( \x = (s_1, \tfrac12 s_2) \), where \( s_i = 1 \) if \( y_i \ge 0 \) and \( s_i = -1 \) otherwise, lies in the ball and gives equality. So \( N_{*}(\y) = \lvert y_1\rvert + \tfrac12\lvert y_2\rvert \).

(b) The ball of \( N_{*} \) is \( \{\lvert y_1\rvert + \tfrac12\lvert y_2\rvert \le 1\} \). On it,
\[
\inner{\x}{\y} \le \lvert x_1\rvert\lvert y_1\rvert + 2\lvert x_2\rvert\cdot\tfrac12\lvert y_2\rvert
\le N(\x)\bigl(\lvert y_1\rvert + \tfrac12\lvert y_2\rvert\bigr) \le N(\x) .
\]
If \( N(\x) = \lvert x_1\rvert \), the point \( \y = \pm\e_1 \) (sign of \( x_1 \)) lies in the ball and gives \( \inner{\x}{\y} = \lvert x_1\rvert \). If \( N(\x) = 2\lvert x_2\rvert \), the point \( \y = \pm2\e_2 \) (sign of \( x_2 \)) lies in the ball, since \( \tfrac12\cdot 2 = 1 \), and gives \( \inner{\x}{\y} = 2\lvert x_2\rvert \). So \( N_{**} = N \).
:::

:::: {#exr-gauges-support-functions-dual-norms-b2}
[B2: A hexagonal norm]

Let \( K = \{\x \in \nR^2 : \lvert x_1\rvert \le 1,\ \lvert x_2\rvert \le 1,\ \lvert x_1 - x_2\rvert \le 1\} \).

::: {.enumerate options="label=(\alph*)"}
1. Check that \( K \) satisfies the hypotheses of @thm-gauge-is-norm (a).
2. Show that \( p_K(\x) = \max\bigl(\lvert x_1\rvert, \lvert x_2\rvert, \lvert x_1 - x_2\rvert\bigr) \), and compute \( p_K\bigl((2, -1)\bigr) \).
3. Determine whether \( p_K \) is induced by an inner product. Justify your answer.
:::
::::

::: {.solution}
(a) \( K \) is the intersection of six closed half-planes, such as \( \{x_1 \le 1\} \) and \( \{x_1 - x_2 \ge -1\} \), each closed and convex (§03, before @def-separation); so \( K \) is closed and convex. It is bounded, since \( \norm{\x}_2 \le \sqrt2 \) when \( \lvert x_1\rvert, \lvert x_2\rvert \le 1 \). It is symmetric, since each condition is unchanged by \( \x \mapsto -\x \). And if \( \norm{\x}_2 < \tfrac12 \), then \( \lvert x_1\rvert, \lvert x_2\rvert < \tfrac12 \) and \( \lvert x_1 - x_2\rvert < 1 \), so \( \x \in K \) and \( \0 \) is an interior point.

(b) For \( t > 0 \), \( \x \in tK \) exactly when \( \x/t \in K \), that is, when \( \lvert x_1\rvert \le t \), \( \lvert x_2\rvert \le t \) and \( \lvert x_1 - x_2\rvert \le t \). The infimum of such \( t \) is \( M = \max(\lvert x_1\rvert, \lvert x_2\rvert, \lvert x_1 - x_2\rvert) \) when \( \x \ne \0 \), and \( 0 = M \) when \( \x = \0 \). So \( p_K\bigl((2,-1)\bigr) = \max(2, 1, 3) = 3 \).

(c) No. With \( \u = \e_1 \) and \( \v = \e_2 \), \( p_K(\u + \v) = \max(1, 1, 0) = 1 \) and \( p_K(\u - \v) = \max(1, 1, 2) = 2 \), so the left side of the parallelogram law is \( 1 + 4 = 5 \), while the right side is \( 2\cdot 1 + 2\cdot 1 = 4 \). By @thm-parallelogram-characterization, no inner product induces \( p_K \).
:::

:::: {#exr-gauges-support-functions-dual-norms-b3}
[B3: The polar of a triangle]

Let \( K = \conv\{(-1,-1), (2,-1), (-1,2)\} \subseteq \nR^2 \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( h_K(\e_1) \), \( h_K(-\e_1) \) and \( h_K\bigl((1,1)\bigr) \).
2. Describe \( K^{\circ} \) by three linear inequalities.
3. Show that \( (-1, 0) \), \( (0, -1) \) and \( (1, 1) \) lie in \( K^{\circ} \), and that \( (1, 0) \) does not.
:::
::::

::: {.solution}
(a) By @prp-support-function-properties (c), \( h_K(\y) \) is the largest of \( \inner{\v}{\y} \) over the three vertices \( \v \), that is, of \( -y_1 - y_2 \), \( 2y_1 - y_2 \), \( -y_1 + 2y_2 \). So \( h_K(\e_1) = \max(-1, 2, -1) = 2 \), \( h_K(-\e_1) = \max(1, -2, 1) = 1 \), and \( h_K\bigl((1,1)\bigr) = \max(-2, 1, 1) = 1 \).

(b) \( \y \in K^{\circ} \) exactly when \( h_K(\y) \le 1 \), that is,
\[
-y_1 - y_2 \le 1, \qquad 2y_1 - y_2 \le 1, \qquad -y_1 + 2y_2 \le 1 .
\]

(c) At \( (-1, 0) \) the three left sides are \( 1, -2, 1 \); at \( (0, -1) \) they are \( 1, 1, -2 \); at \( (1, 1) \) they are \( -2, 1, 1 \). All are \( \le 1 \). At \( (1, 0) \) the second is \( 2 > 1 \), so \( (1, 0) \notin K^{\circ} \), in agreement with \( h_K(\e_1) = 2 \).
:::

### C. Going deeper

:::: {#exr-gauges-support-functions-dual-norms-c1}
[C1: The norm from 1 to infinity]

Let \( \A \in M_{m \times n}(\nR) \), and let \( \norm{\A}_{1\to\infty} \) be the operator norm with \( \norm{\cdot}_1 \) on \( \nR^n \) and \( \norm{\cdot}_\infty \) on \( \nR^m \).

::: {.enumerate options="label=(\alph*)"}
1. Using @prp-operator-norm-bilinear (a), prove that \( \norm{\A}_{1\to\infty} = \max_{i,j}\lvert a_{ij}\rvert \).
2. Deduce from @prp-operator-norm-bilinear (b) that the operator norm of \( \A\tp \) with \( \norm{\cdot}_1 \) on \( \nR^m \) and \( \norm{\cdot}_\infty \) on \( \nR^n \) is the same number.
3. Explain why this does not contradict the warning of Chapter 15 §03 that the entrywise maximum is not a matrix norm.
:::
::::

::: {.solution}
(a) By @prp-dual-of-one-two-infinity (b), the dual of \( \norm{\cdot}_\infty \) is \( \norm{\cdot}_1 \), so @prp-operator-norm-bilinear (a) gives \( \norm{\A}_{1\to\infty} = \max\{\y\tp\A\x : \norm{\x}_1 \le 1,\ \norm{\y}_1 \le 1\} \). Write \( M = \max_{i,j}\lvert a_{ij}\rvert \). For such \( \x, \y \),
\[
\y\tp\A\x = \sum_{i,j}y_ia_{ij}x_j \le M\sum_i\lvert y_i\rvert\sum_j\lvert x_j\rvert \le M .
\]
If \( \lvert a_{kl}\rvert = M \), then \( \x = \e_l \) and \( \y = \pm\e_k \), with the sign of \( a_{kl} \), give \( \y\tp\A\x = M \). So \( \norm{\A}_{1\to\infty} = M \).

(b) By @prp-operator-norm-bilinear (b) with \( \alpha = 1 \) and \( \beta = \infty \), \( \norm{\A\tp}_{\beta*\to\alpha*} = \norm{\A\tp}_{1\to\infty} \) equals \( \norm{\A}_{1\to\infty} \), using \( \beta* = 1 \) and \( \alpha* = \infty \) from @prp-dual-of-one-two-infinity. This is consistent with (a), since \( \A \) and \( \A\tp \) have the same entries.

(c) \( \norm{\cdot}_{1\to\infty} \) uses **different** norms on the source and the target, so the product \( \A\B \) of two square matrices is measured by a norm that does not compose: submultiplicativity in @thm-operator-norm-properties (d) needs the target norm of \( \B \) to be the source norm of \( \A \). With one norm on \( M_n(\nR) \) the entrywise maximum is not submultiplicative (@exm-entrywise-max-not-submultiplicative), and nothing here says otherwise.
:::

:::: {#exr-gauges-support-functions-dual-norms-c2}
[C2: Equivalence constants dualize]

Let \( N_1, N_2 \) be norms on \( \nR^n \) and \( 0 < m \le M \) constants with \( mN_1(\x) \le N_2(\x) \le MN_1(\x) \) for every \( \x \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \tfrac1M N_{1*}(\y) \le N_{2*}(\y) \le \tfrac1m N_{1*}(\y) \) for every \( \y \).
2. Apply (a) to \( \norm{\x}_2 \le \norm{\x}_1 \le \sqrt n\,\norm{\x}_2 \) from @prp-p-norm-inequalities, and compare the result with that proposition.
:::
::::

::: {.solution}
(a) If \( N_2(\x) \le 1 \), then \( N_1(\x) \le 1/m \), so \( \x = \tfrac1m\x' \) with \( N_1(\x') \le 1 \), and \( \inner{\x}{\y} = \tfrac1m\inner{\x'}{\y} \le \tfrac1m N_{1*}(\y) \). Taking the maximum over the ball of \( N_2 \) gives \( N_{2*}(\y) \le \tfrac1m N_{1*}(\y) \). If \( N_1(\x) \le 1 \), then \( N_2(\x) \le M \), and @prp-dual-norm-properties (b) gives \( \inner{\x}{\y} \le N_2(\x)N_{2*}(\y) \le MN_{2*}(\y) \); so \( N_{1*}(\y) \le MN_{2*}(\y) \).

(b) Take \( N_1 = \norm{\cdot}_2 \), \( N_2 = \norm{\cdot}_1 \), \( m = 1 \), \( M = \sqrt n \). The duals are \( \norm{\cdot}_2 \) and \( \norm{\cdot}_\infty \) (@prp-dual-of-one-two-infinity), so (a) gives \( \tfrac{1}{\sqrt n}\norm{\y}_2 \le \norm{\y}_\infty \le \norm{\y}_2 \). These are exactly the other two inequalities \( \norm{\y}_\infty \le \norm{\y}_2 \le \sqrt n\,\norm{\y}_\infty \) of @prp-p-norm-inequalities: that proposition is closed under duality, with the constants carried over unchanged.
:::

:::: {#exr-gauges-support-functions-dual-norms-c3}
[C3: The gauge is the support function of the polar]

Let \( K \subseteq \nR^n \) be closed and convex, with \( \0 \) an interior point.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( p_K(\x) = h_{K^{\circ}}(\x) \) for every \( \x \). *Hint: for \( t > 0 \), rewrite "\( \x \in tK \)" using @thm-bipolar.*
2. Deduce @thm-dual-dual-norm again from (a), @thm-gauge-is-norm (b) and @prp-dual-norm-properties (d).
:::
::::

::: {.solution}
(a) The polar \( K^{\circ} \) contains \( \0 \), so \( h_{K^{\circ}}(\x) \ge \inner{\x}{\0} = 0 \). Let \( t > 0 \). By @thm-bipolar, \( K = K^{\circ\circ} \), so
\[
\x \in tK \iff \x/t \in K^{\circ\circ} \iff \inner{\x}{\y} \le t \text{ for every } \y \in K^{\circ} \iff h_{K^{\circ}}(\x) \le t .
\]
So the admissible \( t \) in @def-gauge are the \( t > 0 \) with \( t \ge h_{K^{\circ}}(\x) \), and their infimum is \( h_{K^{\circ}}(\x) \) (if \( h_{K^{\circ}}(\x) = 0 \), the admissible \( t \) are all \( t > 0 \), with infimum \( 0 \)). In particular \( h_{K^{\circ}}(\x) \) is finite.

(b) Let \( B \) be the ball of \( \norm{\cdot} \). By @thm-gauge-is-norm (b), \( B \) is closed and convex with \( \0 \) interior, and \( \norm{\cdot} = p_B \). By (a), \( p_B = h_{B^{\circ}} \), and \( B^{\circ} \) is the ball of \( \norm{\cdot}_{*} \) by @prp-dual-norm-properties (d). So \( \norm{\x} = \max\{\inner{\x}{\y} : \norm{\y}_{*} \le 1\} = \norm{\x}_{**} \), the maximum existing by @def-dual-norm applied to \( \norm{\cdot}_{*} \).
:::
