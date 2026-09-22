# Extreme Points

Everything so far has gone from points to convex sets: a set of points has a convex hull, and Carathéodory's theorem says how few points each element of the hull needs. This section asks the reverse question: given a convex set, which of its points cannot be manufactured from the others? A triangle is the hull of its three corners, and no smaller set will do. The corners are the **extreme points**, and the main theorem, due to Minkowski, says that a compact convex set is always the hull of its extreme points. We then find the extreme points of three unit balls and of the density matrices, show that the permutation matrices are extreme among the doubly stochastic matrices, and end with a compact convex set whose extreme points do not form a closed set.

Throughout, the field is \( \nR \), and \( V \) is a finite-dimensional real inner product space: \( \nR^n \) with the dot product, or \( M_n(\nR) \) with the Frobenius inner product \( \inner{\A}{\B} = \tr(\B\tp\A) \) of Chapter 10 §01. **Compact** is meant as in §03, and closed bounded sets are compact by @cor-closed-bounded-compact. Conversely a compact set is closed, as a subsequence has the limit of the whole sequence, and bounded, as a sequence with \( \norm{\x_k} > k \) has no convergent subsequence, convergent sequences being bounded; both facts belong to the elementary algebra of limits that Chapter 15's introduction imports.

## Points that are not in between

A convex set contains the segment between any two of its points (@def-convex-set). In a filled triangle, a point in the middle of an edge sits between the two ends of that edge, and an interior point sits between many pairs. A corner sits between no pair: any segment of the triangle through a corner has the corner as an end. So the corners are the points you cannot do without: delete one from the list of points whose hull you take, and the hull shrinks.

*An extreme point of a convex set is a point that is not strictly between two other points of the set.*

::: {#def-extreme-point}
[Extreme Point]

Let \( C \subseteq V \) be a convex set. A point \( \x \in C \) is an **extreme point** of \( C \) if, **whenever** \( \x = t\y + (1 - t)\z \) with \( \y, \z \in C \) and \( 0 < t < 1 \) **strictly**, then \( \y = \z = \x \). The set of extreme points of \( C \) is written \( \operatorname{ext} C \).
:::

In words: the only way to put \( \x \) strictly inside a segment of \( C \) is the useless way, with both ends equal to \( \x \). The word **strictly** matters. With \( t = 1 \) allowed, every point would be \( 1 \cdot \x + 0 \cdot \z \) for any \( \z \in C \), and no point of a set with two elements or more would be extreme.

To test the definition, midpoints are enough.

::: {#lem-extreme-midpoint}
[The Midpoint Test]

Let \( C \subseteq V \) be convex and \( \x \in C \). Then \( \x \) is an extreme point of \( C \) if and only if, whenever \( \x = \frac12(\y + \z) \) with \( \y, \z \in C \), we have \( \y = \z \).
:::

::: {.idea}
If \( \x \) sits at parameter \( t \le \frac12 \) on a segment \( [\z, \y] \), shorten the segment to \( [\z, \y'] \) with \( \y' \) at parameter \( 2t \); then \( \x \) is its midpoint.
:::

::: {.proof}
\( (\Rightarrow) \) Take \( t = \frac12 \) in @def-extreme-point.

\( (\Leftarrow) \) Let \( \x = t\y + (1 - t)\z \) with \( \y, \z \in C \) and \( 0 < t < 1 \). Swapping the names of \( \y \) and \( \z \) if necessary, we may assume \( t \le \frac12 \). Put \( \y' = 2t\y + (1 - 2t)\z \). Since \( 0 < 2t \le 1 \), \( \y' \) lies on the segment from \( \z \) to \( \y \), so \( \y' \in C \) by convexity. Moreover
\[
\tfrac12(\y' + \z) = t\y + (1 - t)\z = \x ,
\]
so the hypothesis gives \( \y' = \z \), that is, \( 2t(\y - \z) = \0 \). As \( t \ne 0 \), \( \y = \z \), and then \( \x = t\y + (1 - t)\y = \y \). So \( \y = \z = \x \), as claimed.
:::

Now some examples, simplest first.

1. **A single point.** \( C = \{\x\} \) is convex, and \( \x \) is extreme: any \( \y, \z \in C \) equal \( \x \).
2. **A closed segment** \( C = \{t\a + (1 - t)\b : 0 \le t \le 1\} \) with \( \a \ne \b \) has exactly two extreme points, \( \a \) and \( \b \). A point \( \x \) with parameter \( 0 < s < 1 \) is not extreme, since \( \x = s\a + (1 - s)\b \) with \( \a \ne \b \). The end \( \a \) is extreme: if \( \a = \frac12(\y + \z) \) with \( \y, \z \) at parameters \( r, r' \in [0, 1] \), then comparing coefficients along the line gives \( \frac12(r + r') = 1 \), which forces \( r = r' = 1 \) and \( \y = \z = \a \). (The coefficient comparison is legitimate because \( t \mapsto t\a + (1-t)\b = \b + t(\a - \b) \) is injective, as \( \a - \b \ne \0 \).)
3. **The closed half-plane** \( H = \{(x_1, x_2) \in \nR^2 : x_2 \ge 0\} \) has **no** extreme points. Every \( \x \in H \) is the midpoint of \( \x + \e_1 \) and \( \x - \e_1 \), both in \( H \), and they differ.
4. **The empty set** is convex and compact with no extreme points. It satisfies the main theorem below only because \( \conv\emptyset = \emptyset \), which is why the theorem's last sentence says "non-empty".

The closed disk \( B_2 \subseteq \nR^2 \) is a richer example: its extreme points are the whole unit circle. The section on unit balls below proves this for every \( n \).

**A non-example by minimal change.** Take the closed triangle \( T = \conv\{(0,0), (2,0), (0,2)\} \) and slide from the corner \( (2, 0) \) along the edge to its midpoint \( (1, 1) \). The point \( (1,1) \) is still in \( T \), still on its boundary, and still on a line with all of \( T \) on one side (\( x_1 + x_2 \le 2 \) on \( T \)). What fails is the one clause of @def-extreme-point: \( (1,1) = \frac12\bigl((2,0) + (0,2)\bigr) \) with \( (2,0) \ne (0,2) \).

::: {.warning}
**Extreme is not the same as "on the boundary".** The point \( (1, 1) \) just used lies on the boundary of the triangle \( T \), and every open disk around it contains points outside \( T \); yet it is not extreme. The other direction does hold, for every convex set: an extreme point is never an interior point, since an interior point \( \x \) is the midpoint of \( \x \pm \varepsilon\e_1 \) for small \( \varepsilon > 0 \).
:::

::: {.check}
Let \( S = \{(0,0), (2,0), (0,2), (1,1), (1,0)\} \). Which points of \( S \) are extreme points of \( \conv S \)?
:::

::: {.solution}
Only \( (0,0) \), \( (2,0) \) and \( (0,2) \). The hull is the triangle \( T = \{x_1 \ge 0,\ x_2 \ge 0,\ x_1 + x_2 \le 2\} \) above, because \( (1,1) \) and \( (1,0) = \frac12\bigl((0,0) + (2,0)\bigr) \) already lie in \( T \). Each of those two points is the midpoint of two distinct points of \( T \), so neither is extreme. The corners are extreme. For \( (2, 0) \): if \( (2,0) = \frac12(\y + \z) \) with \( \y, \z \in T \), then \( y_1, z_1 \le 2 \) and \( \frac12(y_1 + z_1) = 2 \) force \( y_1 = z_1 = 2 \), and the only point of \( T \) with first coordinate \( 2 \) is \( (2,0) \), because \( x_2 \ge 0 \) and \( x_1 + x_2 \le 2 \). The other two corners are handled the same way, with \( x_2 \) and with \( -x_1 - x_2 \) in place of \( x_1 \).
:::

**Why this definition.** It does not ask \( \x \) to be far from the rest of \( C \), or on a corner; on the disk, extreme points have extreme neighbors arbitrarily close. It asks only that \( \x \) not be an average of other points of \( C \), which is what "cannot be manufactured from the others" means for a convex hull. Exercise C1 shows that \( \x \) is extreme exactly when \( C \setminus \{\x\} \) is still convex.

The first result makes the indispensability precise: if a convex set is the hull of \( S \), then \( S \) contains every extreme point.

::: {#prp-extreme-points-of-hull}
[Extreme Points of a Hull Come From the Generators]

Let \( S \subseteq V \) be any set. Then \( \operatorname{ext}(\conv S) \subseteq S \).
:::

::: {.idea}
Split off one generator from a convex combination: what remains is again a point of the hull, and \( \x \) lies strictly between the two.
:::

::: {.proof}
Let \( \x \) be an extreme point of \( \conv S \). By @thm-convex-hull-combinations, \( \x = \sum_{i=1}^{k} t_i\s_i \) with \( \s_i \in S \), every \( t_i > 0 \) (drop the zero terms) and \( \sum_i t_i = 1 \). If \( k = 1 \) then \( \x = \s_1 \in S \). If \( k \ge 2 \), then \( 0 < t_1 < 1 \), and
\[
\x = t_1\s_1 + (1 - t_1)\r , \qquad \r = \sum_{i=2}^{k} \frac{t_i}{1 - t_1}\,\s_i .
\]
The coefficients of \( \r \) are positive and add up to \( 1 \), so \( \r \in \conv S \) by @thm-convex-hull-combinations. Since \( \x \) is extreme, \( \s_1 = \r = \x \). In either case \( \x \in S \).
:::

In particular a **polytope**, the hull of finitely many points, has finitely many extreme points, all among the points one started from. Section 9 is built on this.

## Faces

A single extreme point is too small an object for an induction on dimension. The right object is a piece of the set that behaves like an extreme point as a whole.

::: {#def-face}
[Face]

Let \( C \subseteq V \) be convex. A **face** of \( C \) is a convex subset \( F \subseteq C \) such that, **whenever** \( t\y + (1 - t)\z \in F \) with \( \y, \z \in C \) and \( 0 < t < 1 \), both \( \y \) and \( \z \) lie in \( F \).
:::

So a face swallows every segment of \( C \) that passes through it at an inner point. The empty set and \( C \) itself are faces, and a one-point set \( \{\x\} \) is a face exactly when \( \x \) is an extreme point: that is @def-extreme-point word for word. The edges of a triangle are faces. The segment joining the midpoints of two edges is convex but is not a face: if the triangle has corners \( \a, \b, \c \) and the segment joins \( \frac12(\a + \b) \) to \( \frac12(\a + \c) \), its midpoint is \( \frac12\a + \frac12\cdot\frac12(\b + \c) \), an inner point of a segment of the triangle whose ends \( \a \) and \( \frac12(\b + \c) \) do not lie on it.

What makes faces useful for an induction is that they pass extremeness upwards.

::: {#lem-extreme-points-of-face}
[Extreme Points of a Face]

Let \( C \subseteq V \) be convex and \( F \) a face of \( C \). Then \( \operatorname{ext} F = F \cap \operatorname{ext} C \). In particular an extreme point of a face is an extreme point of \( C \).
:::

::: {.proof}
Let \( \x \in \operatorname{ext} F \), and let \( \x = t\y + (1 - t)\z \) with \( \y, \z \in C \) and \( 0 < t < 1 \). Since \( F \) is a face, \( \y, \z \in F \), and since \( \x \) is extreme in \( F \), \( \y = \z = \x \). So \( \x \in \operatorname{ext} C \). Conversely a point of \( F \) that is extreme in \( C \) is extreme in the smaller set \( F \), because the definition then quantifies over fewer pairs \( \y, \z \).
:::

The faces we can actually produce are the ones cut off by a hyperplane that has the whole set on one side. This is the situation of @thm-supporting-hyperplane.

::: {#prp-exposed-face}
[Supporting Slices Are Faces]

Let \( C \subseteq V \) be convex, let \( \w \in V \) and \( \alpha \in \nR \), and suppose \( \inner{\w}{\x} \le \alpha \) for every \( \x \in C \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( F = \{\x \in C : \inner{\w}{\x} = \alpha\} \) is a face of \( C \);
2. if \( F \) is a single point \( \{\c\} \), then \( \c \) is an extreme point of \( C \).
:::
:::

::: {.idea}
A weighted average of numbers that are all at most \( \alpha \) equals \( \alpha \) only if each of them does.
:::

::: {.proof}
(a) \( F \) is convex, since if \( \inner{\w}{\y} = \inner{\w}{\z} = \alpha \), the same holds for \( t\y + (1-t)\z \) by linearity of the inner product in its second slot. Let \( \y, \z \in C \), \( 0 < t < 1 \), and \( t\y + (1 - t)\z \in F \). Then
\[
\alpha = t\inner{\w}{\y} + (1 - t)\inner{\w}{\z} ,
\]
with \( \inner{\w}{\y} \le \alpha \) and \( \inner{\w}{\z} \le \alpha \). If either inequality were strict, the right side would be strictly less than \( t\alpha + (1-t)\alpha = \alpha \), because \( t \) and \( 1 - t \) are positive. So both are equalities, and \( \y, \z \in F \).

(b) By (a), \( \{\c\} \) is a face, and its only point is extreme in it. By @lem-extreme-points-of-face, \( \c \in \operatorname{ext} C \).
:::

A point \( \c \) as in (b), the **unique** maximizer over \( C \) of some linear function \( \x \mapsto \inner{\w}{\x} \), is called an **exposed point**. Part (b) says that exposed points are extreme; it is the most convenient test for extremeness.

## Minkowski's theorem

The main theorem is proved by induction on dimension. Recall from §01 that a non-empty convex set \( C \) has dimension \( \dim C = \dim \operatorname{aff} C \); by @prp-affine-hull-coset, \( \operatorname{aff} C = \x_0 + W_C \) with \( W_C = \Span\{\y - \x_0 : \y \in C\} \), independent of \( \x_0 \in C \). So \( \dim C = \dim W_C \) (@def-affine-hull (b)). A convex set has dimension \( 0 \) exactly when it is a single point, and for every \( \y \in C \) the difference set \( C - \y = \{\x - \y : \x \in C\} \) lies in \( W_C \).

::: {#thm-minkowski-extreme}
[Minkowski's Theorem]

Let \( V \) be a finite-dimensional real inner product space and let \( K \subseteq V \) be a compact convex set. Then
\[
K = \conv(\operatorname{ext} K) .
\]
In particular, a non-empty compact convex set has at least one extreme point.
:::

::: {.idea}
The inclusion \( \supseteq \) is free, since \( K \) is convex and contains its extreme points. For \( \subseteq \), induct on \( \dim K \). Take \( \x \in K \) and a line through \( \x \) in a direction of \( W_K \). Compactness cuts the line down to a segment \( [\y, \z] \) of \( K \) with \( \x \) on it. An end \( \y \) is not an interior point, and @thm-supporting-hyperplane, applied **inside** \( W_K \) to the translate \( K - \y \), gives a hyperplane through \( \y \) with \( K \) on one side. The slice of \( K \) on that hyperplane is a face of smaller dimension, so by induction \( \y \) is a convex combination of its extreme points, and those are extreme in \( K \) by @lem-extreme-points-of-face. The same goes for \( \z \), and \( \x \) lies between \( \y \) and \( \z \). The space matters: in all of \( V \), a hyperplane containing all of \( K \) would qualify, and would give nothing.
:::

::: {.proof}
\( (\supseteq) \) \( K \) is convex and contains \( \operatorname{ext} K \), so it contains \( \conv(\operatorname{ext} K) \), the smallest convex set containing \( \operatorname{ext} K \) (@def-convex-hull).

\( (\subseteq) \) If \( K = \emptyset \) there is nothing to prove. For non-empty \( K \) we prove, by induction on \( d \ge 0 \), the statement: *every non-empty compact convex set of dimension \( d \), in any finite-dimensional real inner product space, is contained in the convex hull of its extreme points.*

If \( d = 0 \), then \( K = \{\x_0\} \), and \( \x_0 \) is extreme, so \( K = \conv(\operatorname{ext} K) \).

Let \( d \ge 1 \), assume the statement for all dimensions less than \( d \), and let \( \dim K = d \) and \( \x \in K \). Write \( W = W_K \), and choose \( \u \in W \) with \( \u \ne \0 \), which is possible because \( \dim W = d \ge 1 \).

**Step 1: a segment through \( \x \).** Let \( T = \{t \in \nR : \x + t\u \in K\} \), which contains \( 0 \). It is bounded: if \( \norm{\k} \le R \) for every \( \k \in K \), then for \( t \in T \), \( \lvert t \rvert\norm{\u} = \norm{(\x + t\u) - \x} \le 2R \). It is closed: if \( t_j \in T \) and \( t_j \to t \), then \( \x + t_j\u \to \x + t\u \), which lies in \( K \) because \( K \) is closed. So \( T \) is a non-empty closed bounded subset of \( \nR \), which is compact by fact (A3) of Chapter 15's introduction. The function \( t \mapsto t \) is continuous, so by fact (A4) (the extreme value theorem) it attains a minimum \( a \) and a maximum \( b \) on \( T \), and \( a \le 0 \le b \). Put \( \y = \x + a\u \) and \( \z = \x + b\u \), both in \( K \). If \( a < b \) then
\[
\x = \frac{b}{b - a}\,\y + \frac{-a}{b - a}\,\z ,
\]
a convex combination, since both coefficients are \( \ge 0 \) and they add up to \( 1 \); if \( a = b \) then \( a = b = 0 \) and \( \x = \y = \z \). Either way \( \x \in \conv\{\y, \z\} \).

**Step 2: a supporting hyperplane at \( \y \), inside \( W \).** With the inner product of \( V \) restricted to it, \( W \ne \{\0\} \) is a finite-dimensional real inner product space. The set \( K - \y \) lies in \( W \), is convex by @prp-convexity-operations (c), and contains \( \0 \). But \( \0 \) is not an interior point of \( K - \y \) in \( W \) (@def-interior-point): for every \( \varepsilon > 0 \), the vector \( -\varepsilon\u \in W \), of norm \( \varepsilon\norm{\u} \), is **not** in \( K - \y \), because \( \y - \varepsilon\u = \x + (a - \varepsilon)\u \notin K \) by the choice of \( a \). By @thm-supporting-hyperplane, applied in \( W \) to \( K - \y \) and \( \0 \), there is a non-zero \( \w \in W \) with
\[
\inner{\w}{\k - \y} \le \inner{\w}{\0} = 0 \qquad \text{for every } \k \in K .
\]

**Step 3: the face through \( \y \) has smaller dimension.** So \( \inner{\w}{\k} \le \alpha \coloneqq \inner{\w}{\y} \) on \( K \), and by @prp-exposed-face (a), \( F = \{\k \in K : \inner{\w}{\k} = \alpha\} \) is a face of \( K \). It is non-empty, as \( \y \in F \), and convex. It is bounded, being inside \( K \), and closed: if \( \k_j \in F \) and \( \k_j \to \k \), then \( \k \in K \), and \( \lvert\inner{\w}{\k_j} - \inner{\w}{\k}\rvert \le \norm{\w}\norm{\k_j - \k} \to 0 \) by @thm-cauchy-schwarz, so \( \inner{\w}{\k} = \alpha \). So \( F \) is compact. Using \( \y \in F \) as base point, \( W_F \) is spanned by vectors \( \k - \y \) with \( \k \in F \), each of which lies in
\[
W' = \{\v \in W : \inner{\w}{\v} = 0\} ,
\]
the kernel of the linear functional \( \v \mapsto \inner{\w}{\v} \) on \( W \). That functional is non-zero, since it sends \( \w \) to \( \norm{\w}^2 > 0 \), so its image is \( \nR \) and @thm-rank-nullity gives \( \dim W' = d - 1 \). Hence \( \dim F = \dim W_F \le d - 1 \) by @thm-subspace-dimension.

**Step 4: induction.** By the induction hypothesis, \( \y \in \conv(\operatorname{ext} F) \), and \( \operatorname{ext} F \subseteq \operatorname{ext} K \) by @lem-extreme-points-of-face. So \( \y \in \conv(\operatorname{ext} K) \). Running Steps 2 to 4 with \( -\u \) in place of \( \u \), which exchanges the roles of \( a \) and \( b \), gives \( \z \in \conv(\operatorname{ext} K) \). Since \( \conv(\operatorname{ext} K) \) is convex and contains \( \y \) and \( \z \), Step 1 gives \( \x \in \conv(\operatorname{ext} K) \). As \( \x \in K \) was arbitrary, this proves the inclusion and the theorem. The last sentence of the statement follows, since \( \conv \emptyset = \emptyset \).
:::

::: {.warning}
**Compactness cannot be dropped.** The quarter-plane \( Q = \{x_1 \ge 0,\ x_2 \ge 0\} \) is closed and convex with exactly one extreme point, the origin, and \( \conv\{\0\} = \{\0\} \ne Q \). The open disk, bounded but not closed, has no extreme points at all, since each of its points \( \x \) is the midpoint of \( \x \pm \varepsilon\e_1 \) for small \( \varepsilon > 0 \).
:::

Combined with Carathéodory's theorem (@thm-caratheodory), Minkowski's theorem says more: every point of a compact convex \( K \) of dimension \( d \) is a convex combination of at most \( d + 1 \) extreme points. To see this, pick \( \x_0 \in K \) and apply @thm-caratheodory to the translate \( \operatorname{ext} K - \x_0 \), which lies in the \( d \)-dimensional space \( W_K \); translating back preserves convex combinations, because their coefficients add up to \( 1 \).

The consequence used most often concerns linear functions. By the Riesz representation theorem (@thm-riesz-representation), every linear functional on \( V \) is \( \x \mapsto \inner{\x}{\a} \) for some \( \a \in V \), and it is continuous by @thm-cauchy-schwarz, since \( \lvert\inner{\x}{\a} - \inner{\x'}{\a}\rvert \le \norm{\a}\norm{\x - \x'} \).

::: {#cor-linear-max-at-extreme}
[Linear Functions Peak at Extreme Points]

Let \( K \subseteq V \) be a non-empty compact convex set and \( \a \in V \). Then the maximum of \( \x \mapsto \inner{\x}{\a} \) over \( K \) exists and is attained at an extreme point of \( K \). The same holds for the minimum.
:::

::: {.idea}
Minkowski's theorem writes a maximizer as an average of extreme points, and an average of values at most \( M \) equals \( M \) only if every value does.
:::

::: {.proof}
By fact (A4) of Chapter 15's introduction, the continuous function \( \x \mapsto \inner{\x}{\a} \) attains a maximum \( M \) on \( K \), at some \( \x^\ast \in K \). By @thm-minkowski-extreme and @thm-convex-hull-combinations, \( \x^\ast = \sum_{i=1}^{k} t_i\v_i \) with \( \v_i \in \operatorname{ext} K \), \( t_i > 0 \) and \( \sum_i t_i = 1 \). Then
\[
M = \inner{\x^\ast}{\a} = \sum_{i=1}^{k} t_i\inner{\v_i}{\a} ,
\]
while each \( \inner{\v_i}{\a} \le M \). If some \( \inner{\v_i}{\a} < M \), the weighted average would be strictly less than \( M \), because every \( t_i > 0 \). So \( \inner{\v_i}{\a} = M \) for every \( i \), and \( \v_1 \) is an extreme point at which the maximum is attained. For the minimum, apply this to \( -\a \).
:::

This is why linear programs are solved at corners: when one of Section 6's feasible regions is bounded and non-empty, the corollary puts an optimum at an extreme point, and Section 9 shows that there are finitely many. The same corollary gives a new view of Chapter 16's variational formulas, as we will see after the density matrices.

## Three unit balls

The unit balls of the three norms of Chapter 15 (@def-unit-ball, @exm-p-norms) are compact and convex. They are convex by the remark after @def-unit-ball. They are bounded, and closed, because \( \norm{\x_k} \le 1 \) and \( \x_k \to \x \) give \( \norm{\x} \le \norm{\x_k} + \norm{\x - \x_k} \le 1 + \norm{\x - \x_k} \) for every \( k \), hence \( \norm{\x} \le 1 \); so they are compact by @cor-closed-bounded-compact.

::: {#exm-extreme-points-unit-balls}
[The diamond, the cube and the sphere]

In \( \nR^n \) with \( n \ge 1 \), show that:

::: {.enumerate options="label=(\alph*)"}
1. \( \operatorname{ext} B_1 = \{\pm\e_1, \dots, \pm\e_n\} \), \( 2n \) points;
2. \( \operatorname{ext} B_\infty = \{\s : \text{every } s_i = \pm 1\} \), the \( 2^n \) sign vectors;
3. \( \operatorname{ext} B_2 = \{\x : \norm{\x}_2 = 1\} \), the whole unit sphere.
:::
:::

::: {.solution}
In each case we show that the listed points are extreme and that no other point is. The second half uses the same device each time: a point \( \x \) of the ball is not extreme as soon as we find \( \v \ne \0 \) with \( \x \pm \v \) both in the ball, because \( \x \) is their midpoint.

(a) *The points \( \pm\e_i \) are extreme.* Let \( \e_i = \frac12(\y + \z) \) with \( \norm{\y}_1, \norm{\z}_1 \le 1 \). Then
\[
1 = \tfrac12(y_i + z_i) \le \tfrac12(\lvert y_i\rvert + \lvert z_i\rvert) \le \tfrac12(\norm{\y}_1 + \norm{\z}_1) \le 1 ,
\]
so every inequality is an equality. The first forces \( y_i = \lvert y_i\rvert \) and \( z_i = \lvert z_i \rvert \). The second, since \( \lvert y_i\rvert \le \norm{\y}_1 \) and \( \lvert z_i\rvert \le \norm{\z}_1 \) separately, forces \( \lvert y_i\rvert = \norm{\y}_1 \), so all other entries of \( \y \) vanish, and the third forces \( \norm{\y}_1 = 1 \). Hence \( \y = \e_i \), and likewise \( \z = \e_i \). By @lem-extreme-midpoint, \( \e_i \) is extreme; for \( -\e_i \) apply this to \( -\y, -\z \).

*No other point is extreme.* Let \( \x \in B_1 \). If \( \norm{\x}_1 < 1 \), put \( \varepsilon = 1 - \norm{\x}_1 > 0 \) and \( \v = \varepsilon\e_1 \); then \( \norm{\x \pm \v}_1 \le \norm{\x}_1 + \varepsilon = 1 \). If \( \norm{\x}_1 = 1 \) and \( \x \) is not some \( \pm\e_i \), then \( \x \) has two non-zero entries \( x_i, x_j \) with \( i \ne j \). Let \( \sigma_i, \sigma_j \in \{\pm 1\} \) be their signs, \( \varepsilon = \min(\lvert x_i\rvert, \lvert x_j\rvert) > 0 \), and \( \v = \varepsilon(\sigma_i\e_i - \sigma_j\e_j) \). Adding \( \v \) moves \( \lvert x_i \rvert \) up by \( \varepsilon \) and \( \lvert x_j \rvert \) down by \( \varepsilon \), and subtracting \( \v \) does the opposite; neither entry changes sign, because \( \varepsilon \le \lvert x_i \rvert, \lvert x_j \rvert \). So \( \norm{\x \pm \v}_1 = \norm{\x}_1 = 1 \).

(b) *Sign vectors are extreme.* Let \( \s = \frac12(\y + \z) \) with \( \norm{\y}_\infty, \norm{\z}_\infty \le 1 \). For each \( i \), \( s_i = \pm 1 \) is the average of \( y_i \) and \( z_i \), both in \( [-1, 1] \). If \( s_i = 1 \), then \( y_i + z_i = 2 \) with \( y_i, z_i \le 1 \) forces \( y_i = z_i = 1 \); if \( s_i = -1 \), then \( y_i + z_i = -2 \) with \( y_i, z_i \ge -1 \) forces \( y_i = z_i = -1 \). So \( \y = \z = \s \).

*No other point is extreme.* If \( \x \in B_\infty \) is not a sign vector, some \( \lvert x_i \rvert < 1 \). Put \( \v = (1 - \lvert x_i\rvert)\e_i \ne \0 \). Then the \( i \)-th entries of \( \x \pm \v \) are \( x_i \pm (1 - \lvert x_i \rvert) \), both in \( [-1, 1] \), and the other entries are unchanged.

(c) *Unit vectors are extreme.* Let \( \norm{\x}_2 = 1 \) and \( \x = \frac12(\y + \z) \) with \( \norm{\y}_2, \norm{\z}_2 \le 1 \). The parallelogram law of Chapter 10 §01, which comes from expanding with @thm-norm-properties (c), gives
\[
\norm{\y - \z}_2^2 = 2\norm{\y}_2^2 + 2\norm{\z}_2^2 - \norm{\y + \z}_2^2 \le 2 + 2 - \norm{2\x}_2^2 = 0 ,
\]
so \( \y = \z \).

*No other point is extreme.* If \( \norm{\x}_2 < 1 \), put \( \v = (1 - \norm{\x}_2)\e_1 \); then \( \norm{\x \pm \v}_2 \le \norm{\x}_2 + (1 - \norm{\x}_2) = 1 \).

In (a) and (b), Minkowski's theorem (@thm-minkowski-extreme) now makes \( B_1 \) the hull of the \( 2n \) points \( \pm\e_i \), and \( B_\infty \) the hull of the \( 2^n \) sign vectors. In (c) it says only that the ball is the hull of the sphere, and the infinitely many extreme points are why \( B_2 \) is not a polytope.
:::

## Density matrices

Sums and non-negative multiples of positive semidefinite matrices are positive semidefinite, because \( \x\tp(s\A + t\B)\x = s\,\x\tp\A\x + t\,\x\tp\B\x \); Chapter 12 §01 recorded this in @exr-positive-definite-matrices-c2 (a). Cutting that cone with a single linear condition gives a compact convex set whose extreme points we can find exactly.

::: {#def-density-matrix}
[Density Matrix]

A **density matrix** of size \( n \) is a real symmetric matrix \( \X \in M_n(\nR) \) with \( \X \succeq 0 \) and \( \tr\X = 1 \). We write \( \cD_n \) for the set of them.
:::

The name comes from quantum mechanics, which uses the complex Hermitian version; the proofs below carry over, with \( \x^{*} \) for \( \x\tp \), \( \lvert\x^{*}\y\rvert^2 \) for \( (\x\tp\y)^2 \), and @cor-spectral-complex-matrix for @cor-spectral-real-matrix. The set \( \cD_n \) is convex: if \( \X, \Y \in \cD_n \) and \( 0 \le t \le 1 \), then \( t\X + (1-t)\Y \) is symmetric, \( \x\tp(t\X + (1-t)\Y)\x = t\,\x\tp\X\x + (1-t)\,\x\tp\Y\x \ge 0 \), and the trace is \( t + (1 - t) = 1 \). It is compact in \( M_n(\nR) \): the three conditions are preserved by entrywise limits, since symmetry and trace are linear and each inequality \( \x\tp\X_j\x \ge 0 \) survives the limit; and it is bounded, since by @cor-spectral-real-matrix
\[
\norm{\X}_F^2 = \tr(\X^2) = \sum_{i=1}^{n}\lambda_i(\X)^2 \le \Bigl(\sum_{i=1}^{n}\lambda_i(\X)\Bigr)^2 = 1 ,
\]
where the inequality uses \( \lambda_i(\X) \ge 0 \) (@thm-psd-characterizations).

For a unit vector \( \x \in \nR^n \), the matrix \( \x\x\tp \) is in \( \cD_n \): it is symmetric, \( \y\tp\x\x\tp\y = (\x\tp\y)^2 \ge 0 \), and \( \tr(\x\x\tp) = \x\tp\x = 1 \). It is the orthogonal projection onto the line \( \Span\{\x\} \). One more fact about positive semidefinite matrices is needed: a zero value of the quadratic form pins down a null vector.

::: {#lem-psd-form-zero}
[A Zero of the Form Is a Null Vector]

Let \( \B \in M_n(\nR) \) be symmetric with \( \B \succeq 0 \), and let \( \y \in \nR^n \) satisfy \( \y\tp\B\y = 0 \). Then \( \B\y = \0 \).
:::

::: {.proof}
By @cor-spectral-real-matrix, \( \B = \sum_{i=1}^{n} \mu_i\q_i\q_i\tp \) for an orthonormal basis \( (\q_1, \dots, \q_n) \) of eigenvectors, with eigenvalues \( \mu_i \ge 0 \) by @thm-psd-characterizations. Then \( 0 = \y\tp\B\y = \sum_i \mu_i(\q_i\tp\y)^2 \), a sum of non-negative terms, so \( \mu_i(\q_i\tp\y)^2 = 0 \) for every \( i \). Hence \( \mu_i(\q_i\tp\y) = 0 \) for every \( i \), and \( \B\y = \sum_i \mu_i(\q_i\tp\y)\q_i = \0 \).
:::

::: {#thm-extreme-density-matrices}
[Extreme Points of the Density Matrices]

For \( n \ge 1 \),
\[
\operatorname{ext}\cD_n = \{\x\x\tp : \x \in \nR^n,\ \norm{\x} = 1\} ,
\]
the orthogonal projections of rank one. Every \( \X \in \cD_n \) is a convex combination of at most \( n \) of them.
:::

::: {.idea}
The spectral theorem writes \( \X \) as \( \sum_i \lambda_i\q_i\q_i\tp \), with weights \( \lambda_i \ge 0 \) adding up to \( \tr\X = 1 \). That is already a convex combination of rank-one projections, which gives the last sentence and shows at once that a matrix with two positive eigenvalues is not extreme. For the converse, suppose \( \x\x\tp \) is an average of two density matrices. On every vector orthogonal to \( \x \), the form of \( \x\x\tp \) is zero, so the forms of both pieces are zero there too, and @lem-psd-form-zero turns that into "both pieces kill \( \x^{\perp} \)". A symmetric matrix that kills \( \x^\perp \) is a multiple of \( \x\x\tp \), and the trace fixes the multiple.
:::

::: {.proof}
Let \( \X \in \cD_n \). By @cor-spectral-real-matrix, \( \X = \sum_{i=1}^{n}\lambda_i\q_i\q_i\tp \) with \( (\q_1, \dots, \q_n) \) orthonormal and \( \lambda_i = \lambda_i(\X) \). Each \( \lambda_i \ge 0 \) by @thm-psd-characterizations, and \( \sum_i\lambda_i = \tr\X = 1 \), the trace being the sum of the eigenvalues. Dropping the zero terms, this writes \( \X \) as a convex combination of at most \( n \) matrices \( \q_i\q_i\tp \), which proves the last sentence.

**Only rank-one projections are extreme.** At least one eigenvalue of \( \X \) is positive, since the trace is \( 1 \). Suppose first that \( \X \) has at least two positive eigenvalues. As they are listed decreasingly, \( \lambda_1 \ge \lambda_2 > 0 \), and then \( 0 < \lambda_1 < 1 \), because the total is \( 1 \) and \( \lambda_2 \) is part of it. Put
\[
\Y = \frac{1}{1 - \lambda_1}\sum_{i=2}^{n}\lambda_i\q_i\q_i\tp .
\]
Its coefficients are non-negative and add up to \( 1 \), so \( \Y \in \cD_n \) by the convexity of \( \cD_n \), and \( \X = \lambda_1\q_1\q_1\tp + (1 - \lambda_1)\Y \). The two ends differ, since \( \q_1\q_1\tp\q_1 = \q_1 \) while \( \Y\q_1 = \0 \) by orthonormality. So \( \X \) is not extreme. If instead \( \X \) has exactly one positive eigenvalue, that eigenvalue is the whole trace, \( 1 \), and \( \X = \q_1\q_1\tp \). So every extreme point has the form \( \x\x\tp \) with \( \norm{\x} = 1 \).

**Every rank-one projection is extreme.** Let \( \norm{\x} = 1 \) and \( \x\x\tp = \frac12(\B + \C) \) with \( \B, \C \in \cD_n \). For every \( \y \) with \( \x\tp\y = 0 \),
\[
0 = (\x\tp\y)^2 = \y\tp\x\x\tp\y = \tfrac12\,\y\tp\B\y + \tfrac12\,\y\tp\C\y ,
\]
a sum of two non-negative numbers, so \( \y\tp\B\y = 0 \), and \( \B\y = \0 \) by @lem-psd-form-zero. Now let \( \v \in \nR^n \) be arbitrary, and write \( \v = (\x\tp\v)\x + \y \) with \( \y = \v - (\x\tp\v)\x \), so that \( \x\tp\y = \x\tp\v - \x\tp\v = 0 \) because \( \x\tp\x = 1 \). Then \( \B\v = (\x\tp\v)\B\x \) for every \( \v \), that is, \( \B = (\B\x)\x\tp \). Since \( \B \) is symmetric, also \( \B = \B\tp = \x(\B\x)\tp \), and applying both expressions to \( \x \) gives \( \B\x = (\x\tp\B\x)\,\x \). Hence \( \B = c\,\x\x\tp \) with \( c = \x\tp\B\x \), and \( 1 = \tr\B = c\,\tr(\x\x\tp) = c \). So \( \B = \x\x\tp \), and by symmetry of the argument \( \C = \x\x\tp \). By @lem-extreme-midpoint, \( \x\x\tp \) is extreme. This proves the theorem.
:::

For instance, \( \X = \frac{1}{15}\begin{pmatrix} 9 & 2 \\ 2 & 6 \end{pmatrix} \) is symmetric with trace \( 1 \), and \( \X(2, 1) = \frac23(2, 1) \), \( \X(1, -2) = \frac13(1, -2) \). With \( \q_1 = \frac{1}{\sqrt5}(2, 1) \) and \( \q_2 = \frac{1}{\sqrt5}(1, -2) \), the proof's splitting is
\[
\begin{aligned}
\X &= \frac23\,\q_1\q_1\tp + \frac13\,\q_2\q_2\tp \\
&= \frac23\cdot\frac15\begin{pmatrix} 4 & 2 \\ 2 & 1 \end{pmatrix} + \frac13\cdot\frac15\begin{pmatrix} 1 & -2 \\ -2 & 4 \end{pmatrix} ,
\end{aligned}
\]
and the entries check: \( \frac{8 + 1}{15} = \frac{9}{15} \), \( \frac{4 - 2}{15} = \frac{2}{15} \), \( \frac{2 + 4}{15} = \frac{6}{15} \).

Here the spectral theorem handed us the decomposition promised by Minkowski's theorem, with at most \( n \) terms. Carathéodory's theorem, in the coset of symmetric matrices of trace \( 1 \), of dimension \( n(n+1)/2 - 1 \), would only have promised \( n(n+1)/2 \). Structure beats counting.

Now the promised instance of @cor-linear-max-at-extreme. For a real symmetric \( \A \), the function \( \X \mapsto \tr(\A\X) = \inner{\X}{\A} \) is linear on \( M_n(\nR) \), with \( \inner{\cdot}{\cdot} \) the Frobenius inner product.

::: {#exm-top-eigenvalue-over-density-matrices}
[The largest eigenvalue as a linear maximum]

Let \( \A \in M_n(\nR) \) be symmetric. Show that \( \lambda_1(\A) = \max\{\tr(\A\X) : \X \in \cD_n\} \), and find the maximum for \( \A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \).
:::

::: {.solution}
The set \( \cD_n \) is non-empty, compact and convex, so by @cor-linear-max-at-extreme the maximum exists and is attained at an extreme point, which by @thm-extreme-density-matrices is \( \x\x\tp \) with \( \norm{\x} = 1 \). There,
\[
\tr(\A\x\x\tp) = \tr(\x\tp\A\x) = \x\tp\A\x \le \lambda_1(\A)
\]
by the cyclic property of the trace and @lem-extreme-eigenvalues-quadratic-form. The bound is attained when \( \x \) is a unit eigenvector for \( \lambda_1(\A) \), by the same lemma, so the maximum is \( \lambda_1(\A) \).

For the given \( \A \), \( \A(1, 1) = (3, 3) \) and \( \A(1, -1) = (1, -1) \), so \( \lambda_1(\A) = 3 \), and the maximizer is \( \x\x\tp \) with \( \x = \frac{1}{\sqrt2}(1, 1) \):
\[
\X = \frac12\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}, \qquad
\A\X = \frac12\begin{pmatrix} 3 & 3 \\ 3 & 3 \end{pmatrix}, \qquad \tr(\A\X) = 3 .
\]
:::

This is the case \( k = 1 \) of Ky Fan's maximum principle (@thm-ky-fan); for \( k > 1 \), \( \tr(\Q\tp\A\Q) = \tr(\A\Q\Q\tp) \) is again linear in the projection \( \Q\Q\tp \), but this section does not show that the rank-\( k \) projections are the extreme points of any convex set.

## Doubly stochastic matrices

Chapter 8 met **stochastic** matrices, whose entries are non-negative and whose columns add up to \( 1 \) (@def-stochastic-matrix). Asking the rows to add up to \( 1 \) as well gives a set with remarkable corners.

::: {#def-doubly-stochastic}
[Doubly Stochastic Matrix]

A matrix \( \M \in M_n(\nR) \) is **doubly stochastic** if all its entries are non-negative and **every** row and **every** column adds up to \( 1 \). We write \( \Omega_n \) for the set of doubly stochastic \( n \times n \) matrices.
:::

Every permutation matrix \( \P_\sigma \) is doubly stochastic, since it has exactly one \( 1 \) in each row and each column and zeros elsewhere (the remark after @def-permutation-matrix). So is \( \frac1n\J \), the matrix with every entry \( \frac1n \). The set \( \Omega_n \) is convex, since non-negativity and the \( 2n \) linear conditions on sums survive convex combinations. It is compact in \( M_n(\nR) \): its entries lie in \( [0, 1] \), so it is bounded, and each defining condition, being a non-strict inequality or a linear equation in the entries, survives limits. By Minkowski's theorem, \( \Omega_n \) is the hull of its extreme points, and the natural candidates are the permutation matrices.

::: {#prp-permutation-matrices-extreme}
[Permutation Matrices Are Extreme]

Every permutation matrix is an extreme point of \( \Omega_n \).
:::

::: {.idea}
Non-negative entries cannot cancel, so a zero of \( \P \) forces zeros in both pieces, and the row sums then leave no freedom.
:::

::: {.proof}
Let \( \P = \P_\sigma \) and \( \P = t\A + (1 - t)\B \) with \( \A, \B \in \Omega_n \) and \( 0 < t < 1 \). Wherever \( \P \) has a zero entry, \( 0 = t\,a_{ij} + (1 - t)\,b_{ij} \) with both terms non-negative, so \( a_{ij} = b_{ij} = 0 \). Each row of \( \A \) therefore has at most one non-zero entry, in the position where \( \P \) has its \( 1 \), and since the row adds up to \( 1 \), that entry is \( 1 \). So \( \A = \P \), and likewise \( \B = \P \).
:::

The proof never used the column sums. The converse is much deeper.

**Birkhoff's theorem.** *The extreme points of \( \Omega_n \) are exactly the \( n! \) permutation matrices. Equivalently, every doubly stochastic matrix is a convex combination of permutation matrices.*

The two forms are equivalent by what we have. If the permutation matrices are all the extreme points, Minkowski's theorem (@thm-minkowski-extreme) makes \( \Omega_n \) their hull. Conversely, if \( \Omega_n \) is the hull of the permutation matrices, @prp-extreme-points-of-hull puts every extreme point among them, and @prp-permutation-matrices-extreme shows that each of them is one. We do not prove Birkhoff's theorem here; Chapter 18 does. For \( n = 2 \) it can be checked by hand, as the next Quick check shows.

::: {.check}
Show that every \( \M \in \Omega_2 \) has the form \( \begin{pmatrix} t & 1 - t \\ 1 - t & t \end{pmatrix} \) with \( 0 \le t \le 1 \), and deduce Birkhoff's theorem for \( n = 2 \).
:::

::: {.solution}
Let \( t = m_{11} \). The first row sum gives \( m_{12} = 1 - t \), the first column sum gives \( m_{21} = 1 - t \), and the second row sum gives \( m_{22} = 1 - (1 - t) = t \). Non-negativity gives \( 0 \le t \le 1 \). So
\[
\M = t\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} + (1 - t)\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} ,
\]
a convex combination of the two \( 2 \times 2 \) permutation matrices. Hence \( \Omega_2 \) is the segment between them, and its extreme points are its two ends.
:::

Birkhoff's theorem would also give a second route to Schur's theorem, @thm-schur-majorization, which Chapter 16 §08 proved without it. If \( \A = \Q\D\Q\tp \) with \( \Q \) orthogonal and \( \D = \diag(\lambda_1(\A), \dots, \lambda_n(\A)) \) (@cor-spectral-real-matrix, after reordering), then \( \d(\A) = \S\vlambda(\A) \) with \( \S = (q_{ij}^2) \), doubly stochastic because the rows and columns of \( \Q \) are unit vectors, so \( \d(\A) \) would be an average of rearrangements of \( \vlambda(\A) \), each majorized by \( \vlambda(\A) \), hence majorized by \( \vlambda(\A) \) itself by @exm-majorization-set-convex.

## When the extreme points are not closed

In every example so far, the extreme points have formed a closed set: finitely many points, a sphere, or the rank-one projections. That is not always so.

::: {#exm-extreme-points-not-closed}
[A double cone over a circle]

In \( \nR^3 \), let \( \Gamma = \{(1, 0, 0) + (\u, 0) : \u \in \nR^2,\ \norm{\u} = 1\} \) be the circle of radius \( 1 \) centered at \( (1, 0, 0) \) in the plane \( x_3 = 0 \), where \( (\u, 0) = (u_1, u_2, 0) \); it passes through the origin, at \( \u = (-1, 0) \). Let \( \p = (0, 0, 1) \), \( \q = (0, 0, -1) \), \( S = \Gamma \cup \{\p, \q\} \) and \( K = \conv S \). Show that \( K \) is compact and convex, that
\[
\operatorname{ext} K = (\Gamma \setminus \{\0\}) \cup \{\p, \q\} ,
\]
and that this set is not closed.
:::

::: {.solution}
*Compact and convex.* \( K \) is convex as a convex hull. The set \( S \) is bounded and closed: a limit of points of \( \Gamma \) satisfies the closed conditions \( (x_1 - 1)^2 + x_2^2 = 1 \) and \( x_3 = 0 \), which describe \( \Gamma \), and adding two points keeps it closed. So \( S \) is compact, and \( K \) is compact by @cor-hull-of-compact-is-compact.

*The candidates.* By @prp-extreme-points-of-hull, \( \operatorname{ext} K \subseteq S \).

*The origin is not extreme.* \( \0 \in \Gamma \subseteq K \), and \( \0 = \frac12(\p + \q) \) with \( \p \ne \q \).

*The points \( \p \) and \( \q \) are extreme.* Let \( \varphi(\x) = x_3 \). On \( S \), \( \varphi(\p) = 1 \), \( \varphi(\q) = -1 \) and \( \varphi = 0 \) on \( \Gamma \). A point \( \x = \sum_i t_i\s_i \) of \( K \), written as a convex combination with every \( t_i > 0 \) (@thm-convex-hull-combinations), has \( \varphi(\x) = \sum_i t_i\varphi(\s_i) \le 1 \), with equality only if every \( \s_i = \p \), that is, only if \( \x = \p \). So \( \varphi \le 1 \) on \( K \) with equality exactly at \( \p \), and \( \p \) is extreme by @prp-exposed-face (b). The same argument with \( -\varphi \) handles \( \q \).

*The other points of \( \Gamma \) are extreme.* Fix \( \c = (1, 0, 0) + (\u, 0) \) with \( \c \ne \0 \), that is, \( \u \ne (-1, 0) \); then \( u_1 > -1 \), because a unit vector with \( u_1 = -1 \) is \( (-1, 0) \). Let \( \varphi(\x) = \inner{\u}{(x_1, x_2)} = u_1x_1 + u_2x_2 \), so that \( \varphi(\c) = u_1 + \norm{\u}^2 = u_1 + 1 \). For a point \( \s = (1, 0, 0) + (\u', 0) \) of \( \Gamma \),
\[
\varphi(\s) = u_1 + \inner{\u}{\u'} \le u_1 + \norm{\u}\norm{\u'} = u_1 + 1
\]
by @thm-cauchy-schwarz. Equality forces \( (\u, \u') \) to be linearly dependent, so \( \u' = \pm\u \), and \( \u' = -\u \) would give \( \inner{\u}{\u'} = -1 \); so equality holds only at \( \u' = \u \), that is, at \( \s = \c \). Also \( \varphi(\p) = \varphi(\q) = 0 < 1 + u_1 = \varphi(\c) \). So \( \varphi(\s) < \varphi(\c) \) for every \( \s \in S \) other than \( \c \). As before, a convex combination \( \x = \sum_i t_i\s_i \) with all \( t_i > 0 \) has \( \varphi(\x) \le \varphi(\c) \), with equality only if every \( \s_i = \c \). By @prp-exposed-face (b), \( \c \) is extreme.

*Not closed.* For \( k \ge 1 \) let \( \c_k = \bigl(1 - \sqrt{1 - 1/k^2},\ 1/k,\ 0\bigr) \). It is \( (1, 0, 0) + (\u_k, 0) \) with \( \u_k = \bigl(-\sqrt{1 - 1/k^2}, 1/k\bigr) \), a unit vector, so \( \c_k \in \Gamma \); and \( \c_k \ne \0 \), as its second entry is \( 1/k \). So every \( \c_k \) is extreme. For \( 0 \le h \le 1 \) we have \( (1 - h)^2 \le 1 - h \), hence \( 1 - h \le \sqrt{1 - h} \le 1 \) and \( 0 \le 1 - \sqrt{1 - h} \le h \). With \( h = 1/k^2 \), the first entry of \( \c_k \) lies in \( [0, 1/k^2] \), so \( \c_k \to \0 \), which is not extreme. So \( \operatorname{ext} K \) contains a sequence converging to a point outside it, and it is not closed (@def-closed-set).
:::

Geometrically, \( K \) is a double cone over the disk bounded by \( \Gamma \), with apexes \( \p \) and \( \q \). The segment from \( \p \) to \( \q \) touches the rim of the disk at the origin, which robs the origin of its extremeness while leaving its neighbors on the circle intact. So the set of extreme points of a compact convex set need not be closed, and hence need not be compact.

## Exercises

### A. Check your understanding

:::: {#exr-extreme-points-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the definition of an extreme point of a convex set \( C \subseteq V \).
2. True or false: every boundary point of a compact convex set in \( \nR^2 \) is an extreme point. Justify your answer.
3. True or false: there is a non-empty closed convex subset of \( \nR^2 \) with no extreme points. Justify your answer.
4. State @thm-minkowski-extreme, and name the two facts from Chapter 15's introduction that its proof uses.
5. True or false: if \( K = \conv S \) with \( S \) finite, then every point of \( S \) is an extreme point of \( K \). Justify your answer.
:::
::::

::: {.solution}
(a) A point \( \x \in C \) is extreme if \( \x = t\y + (1 - t)\z \) with \( \y, \z \in C \) and \( 0 < t < 1 \) forces \( \y = \z = \x \).

(b) False. In the square \( [-1, 1]^2 \), the point \( (1, 0) \) is on the boundary, since \( (1 + \varepsilon, 0) \) lies outside for every \( \varepsilon > 0 \), but it is the midpoint of \( (1, 1) \) and \( (1, -1) \), both in the square.

(c) True. The closed half-plane \( \{x_2 \ge 0\} \) is one: each of its points \( \x \) is the midpoint of \( \x \pm \e_1 \), which lie in it. A line is another.

(d) A compact convex subset \( K \) of a finite-dimensional real inner product space is the convex hull of its extreme points. The proof uses (A3), to see that the set of \( t \) with \( \x + t\u \in K \) is compact, and (A4), the extreme value theorem, to find its smallest and largest elements.

(e) False. Take \( S = \{0, 1, 2\} \subseteq \nR \). Then \( K = [0, 2] \), whose extreme points are \( 0 \) and \( 2 \); the point \( 1 = \frac12(0 + 2) \) of \( S \) is not extreme. What is true is the reverse inclusion \( \operatorname{ext} K \subseteq S \) (@prp-extreme-points-of-hull).
:::

### B. Practice

:::: {#exr-extreme-points-b1}
[B1: Finding extreme points]

Determine the extreme points of each of the following convex subsets of \( \nR^2 \). Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \conv\{(0,0), (4,0), (0,2), (2,1), (1,1)\} \).
2. \( P = \{(x, y) : x^2 \le y \le 1\} \).
3. The strip \( \{(x, y) : 0 \le y \le 1\} \).
:::

*Hint: for (b), use @prp-exposed-face (b) with a tangent line.*
::::

::: {.solution}
(a) By @prp-extreme-points-of-hull, every extreme point is one of the five listed points. The point \( (2, 1) = \frac12\bigl((4,0) + (0,2)\bigr) \) is not extreme. Neither is \( (1, 1) = \frac12\bigl((2, 1) + (0, 1)\bigr) \), since \( (0, 1) = \frac12\bigl((0,0) + (0,2)\bigr) \) lies in the hull, and \( (2,1) \ne (0,1) \). The three corners are extreme: each is the unique maximizer over the five points of a linear function, namely \( -x - y \), \( x \) and \( y \) respectively, hence the unique maximizer over the hull by the convex-combination argument of @exm-extreme-points-not-closed, and @prp-exposed-face (b) applies. So the extreme points are \( (0,0) \), \( (4,0) \) and \( (0,2) \).

(b) *Points \( (a, a^2) \) with \( -1 \le a \le 1 \) are extreme.* Let \( \varphi(x, y) = 2ax - y \). For \( (x, y) \in P \),
\[
\varphi(x, y) \le 2ax - x^2 = a^2 - (x - a)^2 \le a^2 ,
\]
with equality only if \( x = a \) and \( y = x^2 = a^2 \). So \( (a, a^2) \) is the unique maximizer of \( \varphi \) over \( P \), and it lies in \( P \) because \( a^2 \le 1 \). By @prp-exposed-face (b) it is extreme.

*No other point is extreme.* Let \( (x, y) \in P \) with \( y \ne x^2 \), so \( x^2 < y \le 1 \). If \( y < 1 \), let \( \varepsilon = \min(y - x^2, 1 - y) > 0 \); then \( (x, y \pm \varepsilon) \in P \) and \( (x, y) \) is their midpoint. If \( y = 1 \), then \( \lvert x \rvert < 1 \); let \( \varepsilon = 1 - \lvert x \rvert > 0 \); then \( (x \pm \varepsilon)^2 \le (\lvert x\rvert + \varepsilon)^2 = 1 \), so \( (x \pm \varepsilon, 1) \in P \), and \( (x, 1) \) is their midpoint. So \( \operatorname{ext} P = \{(a, a^2) : -1 \le a \le 1\} \).

(c) None: every point \( \x \) of the strip is the midpoint of \( \x \pm \e_1 \), which lie in the strip. The strip is closed and convex but not bounded, so Minkowski's theorem (@thm-minkowski-extreme) does not apply.
:::

:::: {#exr-extreme-points-b2}
[B2: A density matrix split into pure pieces]

Let
\[
\X = \begin{pmatrix} 1/2 & 1/4 \\ 1/4 & 1/2 \end{pmatrix}, \qquad
\Y = \frac12\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}, \qquad
\Z = \begin{pmatrix} 1/2 & 1 \\ 1 & 1/2 \end{pmatrix} .
\]

::: {.enumerate options="label=(\alph*)"}
1. For each of the three matrices, decide whether it lies in \( \cD_2 \), and if so whether it is an extreme point.
2. Write \( \X \) as a convex combination of two extreme points of \( \cD_2 \).
:::
::::

::: {.solution}
(a) All three are symmetric with trace \( 1 \). For \( \X \): \( \X(1, 1) = \frac34(1, 1) \) and \( \X(1, -1) = \frac14(1, -1) \), so its eigenvalues are \( \frac34 \) and \( \frac14 \), both non-negative. Hence \( \X \in \cD_2 \) (@thm-psd-characterizations), and it has two positive eigenvalues, so it is **not** extreme by @thm-extreme-density-matrices. For \( \Y \): \( \Y = \x\x\tp \) with \( \x = \frac{1}{\sqrt2}(1, 1) \), a unit vector, so \( \Y \in \cD_2 \) and it **is** extreme. For \( \Z \): \( \det\Z = \frac14 - 1 = -\frac34 < 0 \), so the product of its eigenvalues is negative and one of them is negative. Hence \( \Z \) is not positive semidefinite, and \( \Z \notin \cD_2 \).

(b) With the unit eigenvectors \( \q_1 = \frac{1}{\sqrt2}(1, 1) \) and \( \q_2 = \frac{1}{\sqrt2}(1, -1) \),
\[
\begin{aligned}
\X &= \frac34\,\q_1\q_1\tp + \frac14\,\q_2\q_2\tp \\
&= \frac34\cdot\frac12\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} + \frac14\cdot\frac12\begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix} .
\end{aligned}
\]
The entries check: the diagonal is \( \frac38 + \frac18 = \frac12 \) and the off-diagonal is \( \frac38 - \frac18 = \frac14 \). The weights \( \frac34, \frac14 \) are non-negative and add up to \( 1 \), and both matrices are extreme points by @thm-extreme-density-matrices.
:::

:::: {#exr-extreme-points-b3}
[B3: A doubly stochastic matrix from permutations]

Let
\[
\M = \frac16\begin{pmatrix} 3 & 2 & 1 \\ 1 & 3 & 2 \\ 2 & 1 & 3 \end{pmatrix} .
\]

::: {.enumerate options="label=(\alph*)"}
1. Check that \( \M \in \Omega_3 \).
2. Write \( \M \) as a convex combination of three permutation matrices. Hence explain why \( \M \) is not an extreme point of \( \Omega_3 \).
:::
::::

::: {.solution}
(a) The entries are non-negative. Each row of \( 6\M \) is a rearrangement of \( 3, 2, 1 \), and so is each column (the columns are \( (3,1,2) \), \( (2,3,1) \), \( (1,2,3) \)), so every row and column of \( \M \) adds up to \( 6/6 = 1 \).

(b) The entries equal to \( 3 \) sit on the diagonal, the entries equal to \( 2 \) in positions \( (1,2), (2,3), (3,1) \), and the entries equal to \( 1 \) in positions \( (1,3), (2,1), (3,2) \). Each of these three patterns has exactly one position in each row and each column, so each is a permutation matrix:
\[
\P = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix} , \qquad
\P^2 = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} ,
\]
and \( \I \). Hence
\[
\M = \frac12\,\I + \frac13\,\P + \frac16\,\P^2 ,
\]
with weights non-negative and adding up to \( 1 \). Since \( \M = \frac12\I + \frac12\bigl(\frac23\P + \frac13\P^2\bigr) \), with \( \frac23\P + \frac13\P^2 \in \Omega_3 \) by convexity and different from \( \I \) (its diagonal is zero), \( \M \) is the midpoint of two distinct points of \( \Omega_3 \) and is not extreme.
:::

### C. Going deeper

:::: {#exr-extreme-points-c1}
[C1: Deleting an extreme point]

Let \( C \subseteq V \) be convex and \( \x \in C \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \x \) is an extreme point of \( C \) if and only if \( C \setminus \{\x\} \) is convex.
2. Deduce that \( \x \) is an extreme point of \( C \) if and only if \( \x \notin \conv(C \setminus \{\x\}) \).
:::
::::

::: {.solution}
(a) \( (\Rightarrow) \) Let \( \y, \z \in C \setminus \{\x\} \) and \( 0 \le t \le 1 \). The point \( \w = t\y + (1 - t)\z \) lies in \( C \) by convexity. If \( t = 0 \) or \( t = 1 \), \( \w \) is \( \z \) or \( \y \), which is not \( \x \). If \( 0 < t < 1 \) and \( \w = \x \), extremality would give \( \y = \x \), which is false. So \( \w \ne \x \), and \( \w \in C \setminus \{\x\} \).

\( (\Leftarrow) \) Suppose \( \x = t\y + (1 - t)\z \) with \( \y, \z \in C \), \( 0 < t < 1 \), and not both equal to \( \x \). If exactly one of them, say \( \z \), equals \( \x \), then \( \x = t\y + (1 - t)\x \), so \( t(\y - \x) = \0 \) and \( \y = \x \), a contradiction. So neither equals \( \x \), both lie in \( C \setminus \{\x\} \), and their combination \( \x \) does not: \( C \setminus \{\x\} \) is not convex.

(b) If \( \x \) is extreme, \( C \setminus \{\x\} \) is convex by (a), so it is its own hull (@def-convex-hull), which does not contain \( \x \). If \( \x \) is not extreme, (a) gives \( \y, \z \in C \setminus \{\x\} \) and \( t \in [0, 1] \) with \( t\y + (1 - t)\z \notin C \setminus \{\x\} \); this point lies in \( C \), so it is \( \x \), and \( \x \in \conv(C \setminus \{\x\}) \).
:::

:::: {#exr-extreme-points-c2}
[C2: Every contraction is an average of orthogonal matrices]

Let \( \cB = \{\A \in M_n(\nR) : \norm{\A}_2 \le 1\} \), the unit ball of the operator \( 2 \)-norm (@def-operator-norm), so that \( \A \in \cB \) exactly when \( \norm{\A\x} \le \norm{\x} \) for every \( \x \in \nR^n \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that every orthogonal matrix is an extreme point of \( \cB \).
2. Prove that every \( \A \in \cB \) that is not orthogonal is **not** an extreme point of \( \cB \).
3. Deduce that every \( \A \in \cB \) is a convex combination of orthogonal matrices.
:::

*Hint for (b): use the singular value decomposition (@thm-svd) and change only the smallest singular value.*
::::

::: {.solution}
(a) Let \( \Q \) be orthogonal and \( \Q = \frac12(\B + \C) \) with \( \B, \C \in \cB \). Let \( \x \) be a unit vector. Then \( \Q\x \) is a unit vector, \( \B\x \) and \( \C\x \) lie in the Euclidean unit ball \( B_2 \), and \( \Q\x = \frac12(\B\x + \C\x) \). By @exm-extreme-points-unit-balls (c), \( \Q\x \) is an extreme point of \( B_2 \), so \( \B\x = \C\x \) by @lem-extreme-midpoint. This holds for every unit \( \x \), hence for every \( \x \) by scaling, so \( \B = \C \). By @lem-extreme-midpoint again, \( \Q \) is extreme.

(b) By @thm-svd, \( \A = \U\vSigma\V\tp \) with \( \U, \V \) orthogonal and \( \vSigma = \diag(\sigma_1, \dots, \sigma_n) \), \( \sigma_1 \ge \dots \ge \sigma_n \ge 0 \), and \( \sigma_1 = \norm{\A}_2 \le 1 \) by @thm-operator-norm-formulas (c). If \( \sigma_n = 1 \), then every \( \sigma_i = 1 \) and \( \A = \U\V\tp \) is orthogonal. So \( \sigma_n < 1 \). Put \( \varepsilon = 1 - \sigma_n > 0 \), let \( \u_n, \v_n \) be the last columns of \( \U, \V \), and \( \A_{\pm} = \A \pm \varepsilon\,\u_n\v_n\tp = \U\D_{\pm}\V\tp \) with \( \D_{\pm} = \diag(\sigma_1, \dots, \sigma_{n-1}, \sigma_n \pm \varepsilon) \). The last diagonal entries are \( 1 \) and \( 2\sigma_n - 1 \in [-1, 1) \), so every diagonal entry \( d_i \) of \( \D_\pm \) has \( \lvert d_i\rvert \le 1 \). Since \( \U \) and \( \V\tp \) preserve Euclidean length,
\[
\norm{\A_{\pm}\x} = \norm{\D_{\pm}\V\tp\x} \le \norm{\V\tp\x} = \norm{\x} ,
\]
the inequality because \( \D_\pm \) multiplies each coordinate by a number of absolute value at most \( 1 \). So \( \A_{\pm} \in \cB \), \( \A = \frac12(\A_+ + \A_-) \), and \( \A_+ \ne \A_- \) because \( \u_n\v_n\tp \ne \0 \). Hence \( \A \) is not extreme.

(c) \( \cB \) is convex, being the unit ball of a norm (the remark after @def-unit-ball). It is closed and bounded for \( \norm{\cdot}_2 \): if \( \norm{\A_j - \A}_2 \to 0 \) with \( \norm{\A_j}_2 \le 1 \), then \( \norm{\A}_2 \le \norm{\A_j}_2 + \norm{\A - \A_j}_2 \le 1 + \norm{\A - \A_j}_2 \) for every \( j \), and letting \( j \to \infty \) gives \( \norm{\A}_2 \le 1 \). By @cor-closed-bounded-compact it is compact for the Frobenius norm as well. By (a) and (b), \( \operatorname{ext}\cB \) is the set of orthogonal matrices, and @thm-minkowski-extreme gives \( \cB = \conv(\Orth(n)) \).
:::

:::: {#exr-extreme-points-c3}
[C3: The corners of the Loewner interval]

Let \( \cE = \{\X \in M_n(\nR) : \X\tp = \X,\ 0 \preceq \X \preceq \I\} \), where \( \X \preceq \I \) means \( \I - \X \succeq 0 \) (@def-loewner-order).

::: {.enumerate options="label=(\alph*)"}
1. Prove that every symmetric \( \P \) with \( \P^2 = \P \), that is, every orthogonal projection, is an extreme point of \( \cE \).
2. Prove that no other point of \( \cE \) is extreme.
3. Deduce that every \( \X \in \cE \) is a convex combination of orthogonal projections, and give such a combination for \( \X = \diag(\frac12, \frac14) \).
:::

*Hint for (a): use @lem-psd-form-zero twice, once on \( \ker\P \) and once on \( \im\P \).*
::::

::: {.solution}
(a) First, \( \P \in \cE \): its eigenvalues satisfy \( \lambda^2 = \lambda \), so each is \( 0 \) or \( 1 \), and \( \P \) and \( \I - \P \) have eigenvalues in \( \{0, 1\} \), hence are positive semidefinite (@thm-psd-characterizations). Let \( \P = \frac12(\A + \B) \) with \( \A, \B \in \cE \). If \( \P\x = \0 \), then \( 0 = \x\tp\P\x = \frac12\x\tp\A\x + \frac12\x\tp\B\x \) with both terms \( \ge 0 \), so \( \x\tp\A\x = 0 \) and \( \A\x = \0 \) by @lem-psd-form-zero. If \( \P\x = \x \), then \( 0 = \x\tp(\I - \P)\x = \frac12\x\tp(\I - \A)\x + \frac12\x\tp(\I - \B)\x \), so \( \x\tp(\I - \A)\x = 0 \) and, since \( \I - \A \succeq 0 \), \( (\I - \A)\x = \0 \), that is, \( \A\x = \x \). Every \( \v \in \nR^n \) is \( (\v - \P\v) + \P\v \), where \( \P(\v - \P\v) = \0 \) and \( \P(\P\v) = \P\v \). So \( \A\v = \0 + \P\v = \P\v \) for every \( \v \), and \( \A = \P \); then \( \B = 2\P - \A = \P \). By @lem-extreme-midpoint, \( \P \) is extreme.

(b) Let \( \X \in \cE \) not be idempotent. By @cor-spectral-real-matrix, \( \X = \sum_i\lambda_i\q_i\q_i\tp \) with \( \q_i \) orthonormal, and every \( \lambda_i \in [0, 1] \) because \( \X \succeq 0 \) and \( \I - \X \succeq 0 \) have eigenvalues \( \lambda_i \) and \( 1 - \lambda_i \). If every \( \lambda_i \) were \( 0 \) or \( 1 \), \( \X^2 = \sum_i\lambda_i^2\q_i\q_i\tp = \X \); so some \( \lambda_1 \), say, lies strictly between \( 0 \) and \( 1 \). Put \( \varepsilon = \min(\lambda_1, 1 - \lambda_1) > 0 \) and \( \X_\pm = \X \pm \varepsilon\q_1\q_1\tp \). These have the same eigenvectors, with \( \lambda_1 \) replaced by \( \lambda_1 \pm \varepsilon \in [0, 1] \), so \( \X_\pm \in \cE \); they differ, and \( \X \) is their midpoint.

(c) \( \cE \) is convex (both conditions survive convex combinations, as for \( \cD_n \)), closed (each condition survives limits), and bounded (its eigenvalues lie in \( [0, 1] \), so \( \norm{\X}_F^2 = \sum_i\lambda_i^2 \le n \)). By (a), (b) and @thm-minkowski-extreme, \( \cE \) is the convex hull of the orthogonal projections. For \( \X = \diag(\frac12, \frac14) \), reading off the eigenvalues in layers,
\[
\X = \frac14\,\I + \frac14\diag(1, 0) + \frac12\,\0 ,
\]
a convex combination of the projections \( \I \), \( \diag(1, 0) \) and \( \0 \) with weights \( \frac14, \frac14, \frac12 \). The diagonal entries check: \( \frac14 + \frac14 = \frac12 \) and \( \frac14 \).
:::
