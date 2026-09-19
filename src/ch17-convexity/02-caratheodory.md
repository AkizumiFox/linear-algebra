# Carathéodory's Theorem

By @thm-convex-hull-combinations, the convex hull of a set \( S \) consists of the convex combinations of points of \( S \), with any number of points allowed. For a hundred points in the plane, that description permits a single point of the hull to be an average of all hundred at once. A picture says that this is wasteful: the hundred points spread out into a polygon, the polygon can be cut into triangles with corners among the points, and every point of the polygon lies in one of those triangles, so three points always suffice. This section proves the general statement. In a space of dimension \( n \), every point of a convex hull is a convex combination of at most \( n + 1 \) points of the set, and the bound cannot be lowered. Two consequences follow. The hull of a compact set is compact, which §08 uses. And from the same counting argument come Radon's theorem and Helly's theorem, which describe how convex sets in \( \nR^n \) can intersect.

As in §01, all spaces are real. Carathéodory's theorem needs a **finite dimension** and nothing else; the compactness corollary needs, in addition, a norm, and any norm will do.

## When there are too many points

The proof we want has a simple plan. If a point is written as a convex combination of **too many** points, find a way to shift the weights so that the point stays where it is while one weight falls to zero. That point can then be dropped. Two things are needed: a precise meaning of "too many", and a way to shift the weights without moving the point.

Both come from one observation. If \( \sum_i \lambda_i\x_i = \0 \) and \( \sum_i \lambda_i = 0 \), then for every real \( s \),
\[
\sum_i (t_i - s\lambda_i)\x_i = \sum_i t_i\x_i \quad\text{and}\quad \sum_i (t_i - s\lambda_i) = \sum_i t_i .
\]
So the weights \( t_i - s\lambda_i \) describe the same point, and they still add up to \( 1 \). A relation of this shape is what we need a word for.

*A list of points is affinely dependent when some combination with coefficients adding to zero, not all of them zero, cancels out.*

::: {#def-affine-independence}
[Affine Independence]

Let \( V \) be a real vector space and let \( (\x_0, \x_1, \dots, \x_m) \) be a list in \( V \), \( m \ge 0 \). The list is **affinely independent** if, **for all** real \( \lambda_0, \dots, \lambda_m \),
\[
\sum_{i=0}^{m} \lambda_i\x_i = \0 \ \text{ and } \ \sum_{i=0}^{m} \lambda_i = 0 \quad\Longrightarrow\quad \lambda_0 = \lambda_1 = \dots = \lambda_m = 0 .
\]
It is **affinely dependent** otherwise. A relation \( \sum_i \lambda_i\x_i = \0 \) with \( \sum_i\lambda_i = 0 \) and the \( \lambda_i \) **not all zero** is an **affine dependence**.
:::

In words: this is linear independence (@def-linear-independence) with one extra hypothesis, that the coefficients add up to zero. The extra hypothesis makes the condition easier to satisfy, and it makes the notion blind to the choice of origin. Translating every point by \( \p \) changes \( \sum_i\lambda_i\x_i \) by \( \bigl(\sum_i\lambda_i\bigr)\p = \0 \), so a translated list is affinely dependent exactly when the original is.

Some small cases:

- A single point \( (\x_0) \) is always affinely independent: \( \lambda_0 = 0 \) is forced by the sum condition alone.
- Two points \( (\x_0, \x_1) \) are affinely dependent exactly when they are equal: the condition forces \( \lambda_1 = -\lambda_0 \), and then \( \lambda_0(\x_0 - \x_1) = \0 \) has a solution \( \lambda_0 \ne 0 \) if and only if \( \x_0 = \x_1 \).
- Three collinear points are affinely dependent: \( (0, 0), (1, 1), (2, 2) \) satisfy \( 1 \cdot (0, 0) - 2 \cdot (1, 1) + 1 \cdot (2, 2) = \0 \), with \( 1 - 2 + 1 = 0 \).

**A non-example by minimal change.** The list \( (\0, \e_1, \e_2) \) in \( \nR^2 \) is affinely independent: the \( \e_1 \)- and \( \e_2 \)-coordinates of \( \lambda_0\0 + \lambda_1\e_1 + \lambda_2\e_2 = \0 \) give \( \lambda_1 = \lambda_2 = 0 \), and then the sum condition gives \( \lambda_0 = 0 \). Move the third point to \( 2\e_1 \). The list \( (\0, \e_1, 2\e_1) \) still spans the same line as \( (\0, \e_1) \), but now \( 1\cdot\0 - 2\e_1 + 1 \cdot (2\e_1) = \0 \) with \( 1 - 2 + 1 = 0 \): the three points have fallen onto one line, and the implication in the definition fails.

::: {.warning}
**Affine independence is not linear independence.** The list \( (\0, \e_1, \e_2) \) in \( \nR^2 \) is linearly dependent, since it contains \( \0 \), yet it was just shown to be affinely independent. A triangle is an affinely independent list of three points in a two-dimensional space, which linear independence would never allow. That is why the bound in this section is \( n + 1 \), and not \( n \). The implication does run one way: a linearly independent list is affinely independent, since an affine dependence is in particular a linear relation with coefficients not all zero.
:::

The next lemma converts affine dependence into linear dependence of differences, which is what allows a dimension count.

::: {#lem-affine-dependence}
[Affine Dependence by Differences]

Let \( V \) be a real vector space and \( \x_0, \dots, \x_m \in V \).

::: {.enumerate options="label=(\alph*)"}
1. The list \( (\x_0, \dots, \x_m) \) is affinely independent **if and only if** the list \( (\x_1 - \x_0, \dots, \x_m - \x_0) \) is linearly independent.
2. If \( \dim V = n \), every affinely independent list in \( V \) has at most \( n + 1 \) entries. Equivalently, every list of \( n + 2 \) or more points of \( V \) is affinely dependent.
:::
:::

::: {.idea}
The sum condition determines \( \lambda_0 \) from the other coefficients, and eliminating it turns an affine relation among the points into a linear relation among the differences, and back.
:::

::: {.proof}
(a) Suppose \( \sum_{i=0}^{m}\lambda_i\x_i = \0 \) and \( \sum_{i=0}^{m}\lambda_i = 0 \). Then \( \lambda_0 = -\sum_{i \ge 1}\lambda_i \), and substituting,
\[
\sum_{i=1}^{m} \lambda_i(\x_i - \x_0) = \sum_{i=0}^{m}\lambda_i\x_i = \0 .
\]
Conversely, if \( \sum_{i=1}^{m} \lambda_i(\x_i - \x_0) = \0 \), then setting \( \lambda_0 = -\sum_{i \ge 1}\lambda_i \) gives an affine relation \( \sum_{i=0}^{m}\lambda_i\x_i = \0 \) with \( \sum_{i=0}^{m}\lambda_i = 0 \). These two passages are inverse to each other, and \( (\lambda_0, \dots, \lambda_m) \) is not all zero exactly when \( (\lambda_1, \dots, \lambda_m) \) is not all zero, because \( \lambda_0 \) is determined by the others. So affine dependences of the points correspond to linear relations, not all zero, among the differences, and one exists exactly when the other does.

(b) If \( (\x_0, \dots, \x_m) \) is affinely independent, then by (a) the \( m \) differences \( \x_i - \x_0 \) are linearly independent, so \( m \le n \) by @thm-size-bounds (a). The list has \( m + 1 \le n + 1 \) entries.
:::

## The theorem

Now the plan can be carried out. The statement is sharper than the count: the points can be taken affinely independent, and the count is a consequence.

::: {#thm-caratheodory}
[Carathéodory's Theorem]

Let \( V \) be a real vector space with \( \dim V = n \), and let \( S \subseteq V \). Every point of \( \conv S \) is a convex combination of an **affinely independent** list of points of \( S \). In particular, every point of \( \conv S \) is a convex combination of **at most \( n + 1 \)** points of \( S \).
:::

::: {.idea}
**Count, then drop a point.** Write \( \x \) with as few points as possible, so that every weight is positive. If the points were affinely dependent, the weights \( t_i - s\lambda_i \) would describe the same \( \x \) for every \( s \). Start at \( s = 0 \) and increase \( s \). The weights with \( \lambda_i > 0 \) decrease, and there is at least one of these, because the \( \lambda_i \) add up to zero without all being zero. Stop at the first moment a weight reaches \( 0 \): all the weights are still \( \ge 0 \), and one point has become unnecessary. That contradicts minimality.
:::

::: {.proof}
Let \( \x \in \conv S \). By @thm-convex-hull-combinations, \( \x \) is a convex combination of finitely many points of \( S \). Among all ways of writing it so, choose one,
\[
\x = \sum_{i=0}^{m} t_i\x_i , \qquad \x_i \in S,\ \ (t_0, \dots, t_m) \in \Delta_{m+1} ,
\]
with the number \( m + 1 \) of points as small as possible. Then every \( t_i > 0 \): a zero weight could be deleted, and the remaining weights would still be non-negative and add up to \( 1 \), giving a shorter expression.

Suppose, for a contradiction, that \( (\x_0, \dots, \x_m) \) is affinely dependent, and let \( \sum_i\lambda_i\x_i = \0 \), \( \sum_i\lambda_i = 0 \) be an affine dependence. The \( \lambda_i \) are not all zero and add up to \( 0 \), so at least one of them is positive. Put
\[
s = \min\Bigl\{ \frac{t_i}{\lambda_i} : \lambda_i > 0 \Bigr\} ,
\]
a minimum over a non-empty finite set, and let \( j \) be an index where it is attained; \( s > 0 \) since each \( t_i > 0 \). Define \( t_i' = t_i - s\lambda_i \). Then:

- \( t_i' \ge 0 \) for every \( i \). If \( \lambda_i \le 0 \), then \( t_i' \ge t_i > 0 \), since \( s > 0 \). If \( \lambda_i > 0 \), then \( s \le t_i/\lambda_i \) by the choice of \( s \), so \( s\lambda_i \le t_i \).
- \( t_j' = t_j - (t_j/\lambda_j)\lambda_j = 0 \).
- \( \sum_i t_i' = \sum_i t_i - s\sum_i\lambda_i = 1 \) and \( \sum_i t_i'\x_i = \sum_i t_i\x_i - s\sum_i\lambda_i\x_i = \x \).

So \( \x \) is a convex combination of the \( m \) points \( \x_i \), \( i \ne j \), contradicting the minimality of \( m + 1 \). Hence \( (\x_0, \dots, \x_m) \) is affinely independent. By @lem-affine-dependence (b) it has at most \( n + 1 \) entries. This proves the theorem.
:::

In the plane, then, every point of the hull of any set \( S \) lies in a triangle whose corners are points of \( S \), possibly a degenerate one (a segment or a single point). In \( \nR^3 \) it lies in a tetrahedron with corners in \( S \). The proof is constructive: given any convex combination, it says how to shorten it, one point at a time.

::: {#exm-caratheodory-reduction}
[Dropping a point in the plane]

In \( \nR^2 \) let \( \x_0 = (0, 0) \), \( \x_1 = (3, 0) \), \( \x_2 = (0, 3) \), \( \x_3 = (2, 2) \), and let \( \x = \tfrac14(\x_0 + \x_1 + \x_2 + \x_3) = (\tfrac54, \tfrac54) \). Write \( \x \) as a convex combination of three of these points by the method of the proof.
:::

::: {.solution}
Four points in \( \nR^2 \) are affinely dependent by @lem-affine-dependence (b). To find a dependence, solve \( \sum_i \lambda_i\x_i = \0 \) and \( \sum_i\lambda_i = 0 \): the two coordinate equations read \( 3\lambda_1 + 2\lambda_3 = 0 \) and \( 3\lambda_2 + 2\lambda_3 = 0 \). Taking \( \lambda_3 = 3 \) gives \( \lambda_1 = \lambda_2 = -2 \), and then \( \lambda_0 = -(\lambda_1 + \lambda_2 + \lambda_3) = 1 \). Check: \( 1\cdot(0,0) - 2(3,0) - 2(0,3) + 3(2,2) = (-6 + 6, -6 + 6) = \0 \), and \( 1 - 2 - 2 + 3 = 0 \).

The positive coefficients are \( \lambda_0 = 1 \) and \( \lambda_3 = 3 \), with ratios \( t_0/\lambda_0 = \tfrac14 \) and \( t_3/\lambda_3 = \tfrac1{12} \). So \( s = \tfrac1{12} \), attained at \( j = 3 \), and the new weights are
\[
\t' = \bigl(\tfrac14 - \tfrac1{12},\ \tfrac14 + \tfrac2{12},\ \tfrac14 + \tfrac2{12},\ \tfrac14 - \tfrac3{12}\bigr) = \bigl(\tfrac16,\ \tfrac5{12},\ \tfrac5{12},\ 0\bigr) .
\]
Check: \( \tfrac5{12}(3, 0) + \tfrac5{12}(0, 3) = (\tfrac54, \tfrac54) = \x \), and \( \tfrac2{12} + \tfrac5{12} + \tfrac5{12} = 1 \). So \( \x = \tfrac16\x_0 + \tfrac5{12}\x_1 + \tfrac5{12}\x_2 \) lies in the triangle with corners \( \x_0, \x_1, \x_2 \), and \( \x_3 \) has been dropped.

The minimum matters. Using the other positive coefficient, \( s = \tfrac14 \), would make the weight of \( \x_3 \) equal to \( \tfrac14 - \tfrac34 = -\tfrac12 < 0 \): the point would still be described correctly, but not as a convex combination.
:::

\begin{center}
\begin{tikzpicture}[scale=1.05, lab/.style={font=\small}]
  \fill[black!10] (0,0) -- (3,0) -- (0,3) -- cycle;
  \draw[->, gray] (-0.4,0) -- (3.6,0);
  \draw[->, gray] (0,-0.4) -- (0,3.5);
  \draw[thick] (0,0) -- (3,0) -- (0,3) -- cycle;
  \draw[dashed] (3,0) -- (2,2) -- (0,3);
  \fill (0,0) circle (0.05);
  \fill (3,0) circle (0.05);
  \fill (0,3) circle (0.05);
  \draw[thick, fill=white] (2,2) circle (0.06);
  \fill (1.25,1.25) circle (0.05);
  \node[lab, below left] at (0,0) {$\mathbf{x}_0$};
  \node[lab, below] at (3,0) {$\mathbf{x}_1$};
  \node[lab, left] at (0,3) {$\mathbf{x}_2$};
  \node[lab, above right] at (2,2) {$\mathbf{x}_3$ (dropped)};
  \node[lab, right] at (1.3,1.2) {$\mathbf{x}$};
  \node[lab, align=center] at (1.6,-0.95) {$\mathbf{x}$ is an average of all four points,\\ and already lies in the shaded triangle of three};
\end{tikzpicture}
\end{center}

The bound \( n + 1 \) cannot be improved, and the standard simplex shows it.

::: {#exm-caratheodory-sharp}
[The bound is attained]

In \( \nR^n \), let \( S = \{\0, \e_1, \dots, \e_n\} \) and let \( \c = \tfrac{1}{n+1}(\0 + \e_1 + \dots + \e_n) = \tfrac1{n+1}\1 \). Show that \( \c \in \conv S \) is not a convex combination of any \( n \) points of \( S \).
:::

::: {.solution}
The point \( \c \) is a convex combination of the \( n + 1 \) points of \( S \), each with weight \( \tfrac1{n+1} \). A convex combination of \( n \) of the points leaves one out. If it leaves out \( \e_j \), the combination is \( t_0\0 + \sum_{i \ne j} t_i\e_i \), whose \( j \)-th coordinate is \( 0 \), while \( c_j = \tfrac1{n+1} \ne 0 \). If it leaves out \( \0 \), the combination is \( \sum_i t_i\e_i = (t_1, \dots, t_n) \), whose coordinates add up to \( 1 \), while those of \( \c \) add up to \( \tfrac{n}{n+1} \ne 1 \). Either way it is not \( \c \).
:::

The bound can be far from attained for a particular set, however, and it is worth seeing one.

::: {#exm-hull-of-circle}
[Two points suffice for a circle]

Let \( S = \{\x \in \nR^2 : \norm{\x}_2 = 1\} \) be the unit circle. Show that \( \conv S \) is the closed unit disc \( B_2 \), and that every point of \( B_2 \) is a convex combination of **two** points of \( S \).
:::

::: {.solution}
\( B_2 \) is convex (@exm-convex-first-examples (d)) and contains \( S \), so \( \conv S \subseteq B_2 \) by @def-convex-hull. Conversely, let \( (a, b) \in B_2 \), so \( a^2 + b^2 \le 1 \), and put \( c = \sqrt{1 - a^2} \), which is real since \( \lvert a\rvert \le 1 \). The points \( (a, c) \) and \( (a, -c) \) lie on \( S \), and \( \lvert b\rvert \le c \) because \( b^2 \le 1 - a^2 \). With \( t = \tfrac{c + b}{2c} \) when \( c > 0 \),
\[
t(a, c) + (1-t)(a, -c) = \bigl(a,\ (2t - 1)c\bigr) = (a, b) ,
\]
and \( 0 \le t \le 1 \) because \( -c \le b \le c \). When \( c = 0 \), we have \( a = \pm1 \) and \( b = 0 \), and \( (a, b) \) is itself a point of \( S \). So every point of the disc lies on a vertical chord of the circle, and \( B_2 \subseteq \conv S \) by @thm-convex-hull-combinations.
:::

::: {.check}
A point of \( \nR^3 \) is given as a convex combination of seven points of a set \( S \). What is the smallest number of points of \( S \) that @thm-caratheodory guarantees will suffice? Can one always manage with three?
:::

::: {.solution}
Four, since \( n + 1 = 4 \) for \( n = 3 \). Three do not always suffice: by @exm-caratheodory-sharp with \( n = 3 \), the point \( \tfrac14(1, 1, 1) \) is a convex combination of \( \0, \e_1, \e_2, \e_3 \) and of no three of them.
:::

::: {.remark}
The only place the proof used \( \dim V = n \) was the final count, through @lem-affine-dependence (b), and all that count needs is a space containing the differences of the points. If \( S \) lies in an affine subspace of dimension \( d \), then \( n + 1 \) can be replaced by \( d + 1 \); @exr-caratheodory-c1 carries this out. A set of points on a line in \( \nR^{100} \) needs only two at a time.
:::

## The hull of a compact set

The first use of the theorem is a statement about limits. Recall from @cor-closed-bounded-compact that a subset \( K \) of a finite-dimensional real space with a norm is **compact** if every sequence in \( K \) has a subsequence converging to a point **of \( K \)**. Compactness is what lets later sections take a maximum, or a nearest point, over a hull, and it is not obvious that a hull keeps it. A convex combination may use arbitrarily many points, so a sequence of combinations could use more and more of them, and there would be no single compact set of parameters from which to extract a convergent subsequence. Carathéodory's bound removes that possibility: every point of the hull is described by exactly \( n + 1 \) points of \( K \) and \( n + 1 \) weights.

::: {#cor-hull-of-compact-is-compact}
[The Hull of a Compact Set Is Compact]

Let \( V \) be a finite-dimensional real vector space with a norm, and let \( K \subseteq V \) be compact.

::: {.enumerate options="label=(\alph*)"}
1. \( \conv K \) is compact.
2. If \( K \) is non-empty, then every linear functional \( \varphi \) on \( V \) attains a maximum on \( \conv K \), and
\[
\max_{\x \in \conv K} \varphi(\x) = \max_{\x \in K} \varphi(\x) .
\]
:::
:::

::: {.idea}
For (a), write each term of a sequence in \( \conv K \) as a combination of exactly \( n + 1 \) points of \( K \), using @thm-caratheodory and padding with zero weights. That turns one sequence into \( n + 2 \) sequences: one of weight vectors in \( \Delta_{n+1} \), and \( n + 1 \) of points of \( K \). Extract a convergent subsequence from each in turn, a subsequence of the previous one each time, and pass to the limit in the combination. For (b), a linear functional cannot do better on an average than on the best of the points averaged.
:::

::: {.proof}
Let \( n = \dim V \).

(a) If \( K = \emptyset \), then \( \conv K = \emptyset \), which is compact vacuously. Otherwise let \( (\y_k) \) be a sequence in \( \conv K \). By @thm-caratheodory, each \( \y_k \) is a convex combination of at most \( n + 1 \) points of \( K \); repeating one of those points with weight \( 0 \) if necessary, we may write
\[
\y_k = \sum_{i=0}^{n} t_{k,i}\,\x_{k,i} , \qquad \x_{k,i} \in K,\ \ \t_k = (t_{k,0}, \dots, t_{k,n}) \in \Delta_{n+1} .
\]

*Step 1: the weights.* \( \Delta_{n+1} \) is closed in \( \nR^{n+1} \) by @prp-closed-open-basics (b), (c), and bounded, since each coordinate of a point of it lies in \( [0, 1] \). By **the compactness of closed bounded sets in \( \nR^{n+1} \), fact (A3) of Chapter 15's introduction**, some subsequence of \( (\t_k) \) converges to a point \( \t = (t_0, \dots, t_n) \in \Delta_{n+1} \). In particular \( t_{k,i} \to t_i \) along it for each \( i \), since \( \lvert t_{k,i} - t_i\rvert \le \norm{\t_k - \t}_2 \).

*Step 2: the points.* Along that subsequence, the sequence \( (\x_{k,0}) \) lies in \( K \), so by compactness of \( K \) a further subsequence has \( \x_{k,0} \to \x_0 \in K \). Along it, a further subsequence has \( \x_{k,1} \to \x_1 \in K \), and so on through \( i = n \). A subsequence of a convergent sequence converges to the same limit, so along the final subsequence, which we index by \( k \) again, \( \t_k \to \t \) and \( \x_{k,i} \to \x_i \) for every \( i \).

*Step 3: the limit.* Put \( \y = \sum_{i=0}^{n} t_i\x_i \), which lies in \( \conv K \) by @thm-convex-hull-combinations. By (N3) and (N2) of @def-norm, along the final subsequence,
\[
\begin{aligned}
\norm{\y_k - \y}
&\le \sum_{i=0}^{n} \norm{t_{k,i}\x_{k,i} - t_i\x_i} \\
&\le \sum_{i=0}^{n} \Bigl(\lvert t_{k,i} - t_i\rvert\,\norm{\x_{k,i}} + t_i\norm{\x_{k,i} - \x_i}\Bigr) ,
\end{aligned}
\]
where the second line writes \( t_{k,i}\x_{k,i} - t_i\x_i = (t_{k,i} - t_i)\x_{k,i} + t_i(\x_{k,i} - \x_i) \). Each \( \norm{\x_{k,i}} \le \norm{\x_i} + \norm{\x_{k,i} - \x_i} \) is bounded, since the last term tends to \( 0 \). So every term on the right tends to \( 0 \), and \( \y_k \to \y \in \conv K \) along the subsequence. Hence \( \conv K \) is compact.

(b) By @lem-linear-map-lipschitz, \( \varphi \) is continuous. By **the extreme value theorem, fact (A4) of Chapter 15's introduction**, applied to \( \varphi \) on the non-empty compact set \( K \), there is \( \x^{\ast} \in K \) with \( \varphi(\x) \le M = \varphi(\x^{\ast}) \) for every \( \x \in K \). Now let \( \y = \sum_i t_i\x_i \) be any point of \( \conv K \), with \( \x_i \in K \) and \( \t \in \Delta_m \) (@thm-convex-hull-combinations). By linearity, and since every \( t_i \ge 0 \),
\[
\varphi(\y) = \sum_i t_i\varphi(\x_i) \le \sum_i t_iM = M .
\]
So \( M \) bounds \( \varphi \) on \( \conv K \), and it is attained there, at \( \x^{\ast} \in K \subseteq \conv K \). This proves the corollary.
:::

For instance, \( \varphi(x, y) = x + 2y \) takes the values \( 0, 3, 6 \) at the corners \( (0, 0), (3, 0), (0, 3) \) of the triangle in @exm-caratheodory-reduction; as in the proof of (b), at a point \( \sum_i t_i\x_i \) of the triangle it takes the average \( 3t_1 + 6t_2 \le 6 \) of these values, so its maximum over the triangle is \( 6 \), attained at \( (0, 3) \). At the interior point \( \x = (\tfrac54, \tfrac54) \) it takes \( \tfrac{15}4 = \tfrac16 \cdot 0 + \tfrac5{12} \cdot 3 + \tfrac5{12} \cdot 6 \), an average of the corner values and so no larger than the largest.

To maximize a linear functional over the hull of finitely many points it is enough to evaluate it at those points (@exr-caratheodory-b3). §08 extends this to every compact convex set, and §09 shows that a bounded feasible region of §06 is such a hull.

::: {.warning}
**The hull of a closed set need not be closed.** In \( \nR^2 \), let \( S = \{(0, 1)\} \cup \{(x, 0) : x \in \nR\} \), a point together with a line. \( S \) is closed, by @prp-closed-open-basics (b), (c). Its hull is
\[
\conv S = \{(x, y) : 0 \le y < 1\} \cup \{(0, 1)\} .
\]
Indeed a convex combination of points of \( S \) with total weight \( y \) on \( (0, 1) \) has second coordinate \( y \), and when \( y < 1 \) any first coordinate \( x \) is reached, as \( y(0,1) + (1-y)\bigl(x/(1-y), 0\bigr) = (x, y) \); when \( y = 1 \) all the weight is on \( (0, 1) \). The points \( (1, 1 - 1/k) \) lie in \( \conv S \) and converge to \( (1, 1) \), which does not. So compactness in @cor-hull-of-compact-is-compact cannot be weakened to closedness: here \( S \) is closed but unbounded, and the hull loses the line \( y = 1 \), except for the one point that belongs to \( S \).
:::

## Radon's theorem and Helly's theorem

The dimension count behind Carathéodory's theorem says something about intersections of convex sets as well. Its first form is a statement about \( n + 2 \) points.

::: {#thm-radon}
[Radon's Theorem]

Let \( V \) be a real vector space with \( \dim V = n \), and let \( \x_1, \dots, \x_m \in V \) with \( m \ge n + 2 \). Then the index set \( \{1, \dots, m\} \) can be split into two **disjoint** non-empty sets \( I \) and \( J \) with
\[
\conv\{\x_i : i \in I\} \cap \conv\{\x_j : j \in J\} \ne \emptyset .
\]
:::

::: {.idea}
Take an affine dependence and separate its positive coefficients from the rest. Moving the negative terms across the equation gives an equation between a positive combination of some points and a positive combination of the others, with the **same total weight** on each side, because the coefficients add up to zero. Divide by that total, and each side becomes a convex combination.
:::

::: {.proof}
By @lem-affine-dependence (b), the list \( (\x_1, \dots, \x_m) \) is affinely dependent: there are \( \lambda_1, \dots, \lambda_m \), not all zero, with \( \sum_i\lambda_i\x_i = \0 \) and \( \sum_i\lambda_i = 0 \). Let \( I = \{i : \lambda_i > 0\} \) and \( J = \{j : \lambda_j \le 0\} \), which are disjoint with union \( \{1, \dots, m\} \). Since the \( \lambda_i \) add up to \( 0 \) and are not all zero, some \( \lambda_i \) is positive and some is negative, so neither \( I \) nor \( J \) is empty. Put \( \sigma = \sum_{i \in I}\lambda_i > 0 \); then \( \sum_{j \in J}(-\lambda_j) = \sigma \) as well, since the total is \( 0 \). Moving the terms indexed by \( J \) across and dividing by \( \sigma \),
\[
\y \coloneqq \sum_{i \in I} \frac{\lambda_i}{\sigma}\,\x_i = \sum_{j \in J} \frac{-\lambda_j}{\sigma}\,\x_j .
\]
On the left the coefficients are positive and add up to \( 1 \); on the right they are \( \ge 0 \) and add up to \( 1 \). So \( \y \) lies in both hulls, by @thm-convex-hull-combinations. This proves the theorem.
:::

A partition as in the theorem is a **Radon partition**. In the plane, four points in general position (no three on a line) either have one inside the triangle of the other three, or they form a quadrilateral whose two diagonals cross; @exr-caratheodory-b2 finds the partition in each case. The count \( n + 2 \) cannot be lowered: the \( n + 1 \) points \( \0, \e_1, \dots, \e_n \) have no Radon partition (@exr-caratheodory-c3).

Helly's theorem turns the counting around. Instead of asking how many points a hull needs, it asks how many sets of a family must be checked to know that all of them have a common point. Checking pairs is not enough, since three lines in the plane can meet pairwise in three different points; checking triples in the plane is.

::: {#thm-helly}
[Helly's Theorem]

Let \( V \) be a real vector space with \( \dim V = n \), and let \( C_1, \dots, C_m \) be convex subsets of \( V \), with \( m \ge n + 1 \). If **every** \( n + 1 \) of the sets have a point in common, then all \( m \) of them have a point in common.
:::

::: {.idea}
Induction on the number of sets. Given \( m \ge n + 2 \) sets, the inductive hypothesis provides, for each \( i \), a point \( \x_i \) lying in every set **except possibly** \( C_i \). That is \( m \ge n + 2 \) points, so Radon's theorem splits them into two groups whose hulls meet at some \( \y \). Any one set \( C_k \) misses at most one point, \( \x_k \), and that point lies in only one of the two groups; the other group lies entirely in \( C_k \), and so does its hull, which contains \( \y \).
:::

::: {.proof}
We use induction on \( m \). For \( m = n + 1 \), the hypothesis applied to all \( m \) sets is the conclusion. Let \( m \ge n + 2 \), and suppose the theorem holds for families of \( m - 1 \) convex sets. For each \( i = 1, \dots, m \), the family \( \{C_k : k \ne i\} \) has \( m - 1 \ge n + 1 \) members, and every \( n + 1 \) of them have a common point by hypothesis. By the inductive hypothesis, there is a point \( \x_i \) with
\[
\x_i \in C_k \quad\text{for every } k \ne i .
\]
Since \( m \ge n + 2 \), @thm-radon splits \( \{1, \dots, m\} \) into disjoint non-empty sets \( I \), \( J \) and gives a point \( \y \in \conv\{\x_i : i \in I\} \cap \conv\{\x_j : j \in J\} \).

Fix \( k \in \{1, \dots, m\} \). If \( k \in I \), then \( k \notin J \), so every \( \x_j \) with \( j \in J \) lies in \( C_k \). Since \( C_k \) is convex, @lem-convex-contains-combinations puts every convex combination of these points in \( C_k \), so \( \conv\{\x_j : j \in J\} \subseteq C_k \) by @thm-convex-hull-combinations, and in particular \( \y \in C_k \). If \( k \in J \), the same argument with \( I \) in place of \( J \) gives \( \y \in C_k \). Hence \( \y \) lies in every \( C_k \). This completes the induction.
:::

::: {#exm-helly-four-half-planes}
[Helly's proof run on four half-planes]

In \( \nR^2 \), let
\[
\begin{aligned}
C_1 &= \{y \ge 0\}, & C_2 &= \{x \ge 0\}, \\
C_3 &= \{x + y \le 2\}, & C_4 &= \{x - y \le 1\}.
\end{aligned}
\]
Find points \( \x_i \) in all the sets except \( C_i \), and follow the proof of @thm-helly to a common point of all four.
:::

::: {.solution}
Here \( n = 2 \) and \( m = 4 = n + 2 \), so the proof applies Radon's theorem (@thm-radon) to four points. The following points lie in every set except their own, as substitution into the four inequalities shows:
\[
\x_1 = (0, -1), \quad \x_2 = (-1, 0), \quad \x_3 = (2, 2), \quad \x_4 = (2, 0) .
\]
For instance, \( \x_1 \) has \( x = 0 \ge 0 \), \( x + y = -1 \le 2 \), \( x - y = 1 \le 1 \), and \( y = -1 < 0 \) violates \( C_1 \). And \( \x_4 \) has \( y = 0 \), \( x = 2 \), \( x + y = 2 \), and \( x - y = 2 > 1 \) violates \( C_4 \).

An affine dependence: the equations \( \sum_i\lambda_i\x_i = \0 \), \( \sum_i\lambda_i = 0 \) are satisfied by \( \vlambda = (-6, 4, -3, 5) \). Check: the first coordinates give \( -4 - 6 + 10 = 0 \), the second \( 6 - 6 + 0 = 0 \), and \( -6 + 4 - 3 + 5 = 0 \). The positive coefficients are at \( I = \{2, 4\} \), with \( \sigma = 9 \), so
\[
\y = \tfrac49\x_2 + \tfrac59\x_4 = \bigl(\tfrac{-4 + 10}{9}, 0\bigr) = \bigl(\tfrac23, 0\bigr) ,
\]
and from the other side \( \tfrac69\x_1 + \tfrac39\x_3 = \bigl(\tfrac69, \tfrac{-6 + 6}{9}\bigr) = (\tfrac23, 0) \), as it must be. Finally \( \y = (\tfrac23, 0) \) satisfies \( y = 0 \ge 0 \), \( x = \tfrac23 \ge 0 \), \( x + y = \tfrac23 \le 2 \) and \( x - y = \tfrac23 \le 1 \): it lies in all four half-planes. The proof explains why, without any checking: \( C_2 \) and \( C_4 \) contain \( \x_1 \) and \( \x_3 \), hence the segment between them, which contains \( \y \); and \( C_1 \) and \( C_3 \) contain \( \x_2 \) and \( \x_4 \), hence the other segment through \( \y \).
:::

::: {.remark}
Helly's theorem is about **finite** families, and the finiteness cannot simply be dropped. The closed half-lines \( [k, \infty) \subseteq \nR \), for \( k = 1, 2, 3, \dots \), are convex, and any finitely many of them meet (at their largest \( k \)), but no real number lies in all of them. For compact convex sets the infinite version does hold; @exr-caratheodory-c2 proves it for a sequence of sets.
:::

With these results the chapter has its combinatorial foundation. §03 turns to geometry: a point outside a closed convex set can be separated from it by a hyperplane.

## Exercises

### A. Check your understanding

:::: {#exr-caratheodory-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State @thm-caratheodory.
2. True or false: every point in the convex hull of ten points of \( \nR^2 \) is a convex combination of three of them. Justify your answer.
3. True or false: the convex hull of a closed subset of \( \nR^2 \) is closed. Justify your answer.
4. True or false: any four points of \( \nR^3 \) have a Radon partition. Justify your answer.
5. Is the list \( (\e_1, \e_2, \e_3) \) in \( \nR^3 \) affinely independent? Is \( (\e_1, \e_2, \e_1 + \e_2 - \e_3, \e_3) \)?
6. Which facts from Chapter 15's list of imported analysis does @cor-hull-of-compact-is-compact use, and where?
:::
::::

::: {.solution}
(a) If \( \dim V = n \) and \( S \subseteq V \), every point of \( \conv S \) is a convex combination of an affinely independent list of points of \( S \), and so of at most \( n + 1 \) points of \( S \).

(b) True, by @thm-caratheodory with \( n = 2 \): at most three are needed, and if fewer are used, a point can be added with weight \( 0 \).

(c) False. The warning in this section gives \( S = \{(0, 1)\} \cup \{(x, 0) : x \in \nR\} \), closed, with \( (1, 1) \) a limit of points of \( \conv S \) not in \( \conv S \).

(d) False. Radon's theorem (@thm-radon) needs \( n + 2 = 5 \) points in \( \nR^3 \), and four can fail. The points \( \0, \e_1, \e_2, \e_3 \) are affinely independent, since \( \e_1, \e_2, \e_3 \) are linearly independent (@lem-affine-dependence (a)). A point common to the hulls of two disjoint groups of them would give two convex combinations with equal value, and subtracting them gives a relation with coefficients adding up to \( 0 \) and not all zero, which is an affine dependence. So there is no Radon partition; @exr-caratheodory-c3 carries this out for \( n + 1 \) affinely independent points in general.

(e) Yes: it is linearly independent, and a linearly independent list is affinely independent. The second list is affinely dependent: \( \e_1 + \e_2 - (\e_1 + \e_2 - \e_3) - \e_3 = \0 \) with coefficients \( 1, 1, -1, -1 \), which add up to \( 0 \).

(f) (A3), the compactness of closed bounded sets, for the weights in part (a); and (A4), the extreme value theorem, for the maximum over \( K \) in part (b). Part (a) also uses the hypothesis that \( K \) is compact, once for each of the \( n + 1 \) points.
:::

### B. Practice

:::: {#exr-caratheodory-b1}
[B1: Shortening a combination]

In \( \nR^2 \), let \( \x_1 = (0, 0) \), \( \x_2 = (4, 0) \), \( \x_3 = (4, 4) \), \( \x_4 = (0, 4) \), and
\[
\x = \tfrac1{10}\x_1 + \tfrac2{10}\x_2 + \tfrac3{10}\x_3 + \tfrac4{10}\x_4 .
\]

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \x \), and find an affine dependence among \( \x_1, \dots, \x_4 \).
2. Use the method of @thm-caratheodory to write \( \x \) as a convex combination of three of the points.
3. Apply the method with the dependence multiplied by \( -1 \). Which point is dropped now? Hence \( \x \) lies in two different triangles with corners among the \( \x_i \).
:::
::::

::: {.solution}
(a) \( \x = \tfrac2{10}(4, 0) + \tfrac3{10}(4, 4) + \tfrac4{10}(0, 4) = (\tfrac{8 + 12}{10}, \tfrac{12 + 16}{10}) = (2, \tfrac{14}5) \). The corners of a square satisfy \( \x_1 - \x_2 + \x_3 - \x_4 = (0 - 4 + 4 - 0, 0 - 0 + 4 - 4) = \0 \), with \( 1 - 1 + 1 - 1 = 0 \). So \( \vlambda = (1, -1, 1, -1) \).

(b) The positive coefficients are at \( \x_1 \) and \( \x_3 \), with ratios \( \tfrac{1/10}{1} = \tfrac1{10} \) and \( \tfrac{3/10}{1} = \tfrac3{10} \). So \( s = \tfrac1{10} \), attained at \( \x_1 \), and the new weights are \( \t - s\vlambda = (0, \tfrac3{10}, \tfrac2{10}, \tfrac5{10}) \). Check: \( \tfrac3{10}(4, 0) + \tfrac2{10}(4, 4) + \tfrac5{10}(0, 4) = (\tfrac{12 + 8}{10}, \tfrac{8 + 20}{10}) = (2, \tfrac{14}5) \), and the weights add up to \( 1 \). So \( \x \in \conv\{\x_2, \x_3, \x_4\} \).

(c) With \( -\vlambda = (-1, 1, -1, 1) \), the positive coefficients are at \( \x_2 \) and \( \x_4 \), with ratios \( \tfrac2{10} \) and \( \tfrac4{10} \). So \( s = \tfrac2{10} \), attained at \( \x_2 \), and the weights become \( \t + s\vlambda = (\tfrac3{10}, 0, \tfrac5{10}, \tfrac2{10}) \). Check: \( \tfrac5{10}(4, 4) + \tfrac2{10}(0, 4) = (2, \tfrac{20 + 8}{10}) = (2, \tfrac{14}5) \). Now \( \x_2 \) is dropped, and \( \x \in \conv\{\x_1, \x_3, \x_4\} \). The two answers are consistent: the triangle with corners \( \x_2, \x_3, \x_4 \) is the part of the square where \( x + y \ge 4 \), the triangle with corners \( \x_1, \x_3, \x_4 \) is the part where \( y \ge x \), and \( (2, \tfrac{14}5) \) satisfies both. The shorter combination produced by Carathéodory's theorem is not unique; it depends on the dependence used and on its sign.
:::

:::: {#exr-caratheodory-b2}
[B2: Radon partitions in the plane]

Find a Radon partition, and a point common to the two hulls, for each list of four points in \( \nR^2 \). Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( (0, 0), (4, 0), (0, 4), (1, 1) \).
2. \( (0, 0), (3, 1), (1, 3), (4, 4) \).
:::
::::

::: {.solution}
Label the points \( \x_1, \dots, \x_4 \) in the order given, and follow the proof of @thm-radon.

(a) The equations \( \sum_i\lambda_i\x_i = \0 \), \( \sum_i\lambda_i = 0 \) read \( 4\lambda_2 + \lambda_4 = 0 \), \( 4\lambda_3 + \lambda_4 = 0 \), \( \lambda_1 + \lambda_2 + \lambda_3 + \lambda_4 = 0 \). Taking \( \lambda_4 = 4 \) gives \( \lambda_2 = \lambda_3 = -1 \) and \( \lambda_1 = -2 \). So \( I = \{4\} \), \( J = \{1, 2, 3\} \), \( \sigma = 4 \), and
\[
\y = \x_4 = (1, 1) = \tfrac24(0, 0) + \tfrac14(4, 0) + \tfrac14(0, 4) .
\]
The fourth point lies inside the triangle of the other three.

(b) The equations read \( 3\lambda_2 + \lambda_3 + 4\lambda_4 = 0 \), \( \lambda_2 + 3\lambda_3 + 4\lambda_4 = 0 \), and \( \sum_i \lambda_i = 0 \). Subtracting the first two gives \( \lambda_2 = \lambda_3 \), and then \( 4\lambda_2 + 4\lambda_4 = 0 \), so \( \lambda_4 = -\lambda_2 \) and \( \lambda_1 = -\lambda_2 - \lambda_3 - \lambda_4 = -\lambda_2 \). Taking \( \lambda_2 = -1 \) gives \( \vlambda = (1, -1, -1, 1) \). So \( I = \{1, 4\} \), \( J = \{2, 3\} \), \( \sigma = 2 \), and
\[
\y = \tfrac12(0, 0) + \tfrac12(4, 4) = (2, 2) = \tfrac12(3, 1) + \tfrac12(1, 3) .
\]
The two diagonals of the quadrilateral cross at \( (2, 2) \).
:::

:::: {#exr-caratheodory-b3}
[B3: Linear functionals on a polygon]

Let \( V \) be a finite-dimensional real vector space with a norm, and \( \x_1, \dots, \x_m \in V \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \{\x_1, \dots, \x_m\} \) is compact, and deduce that \( P = \conv\{\x_1, \dots, \x_m\} \) is compact.
2. Prove that every linear functional \( \varphi \) on \( V \) attains its maximum over \( P \) at one of the points \( \x_i \).
3. Find the maximum and the minimum of \( \varphi(x, y) = 2x - y \) over the triangle \( \conv\{(1, 0), (3, 1), (0, 2)\} \) of @exm-hull-membership.
:::
::::

::: {.solution}
(a) Let \( (\y_k) \) be a sequence in the finite set. Some \( \x_i \) occurs as \( \y_k \) for infinitely many \( k \), since there are only \( m \) candidates, and those terms form a constant subsequence, which converges to \( \x_i \), a point of the set. So the set is compact, and \( P \) is compact by @cor-hull-of-compact-is-compact (a).

(b) By @cor-hull-of-compact-is-compact (b), the maximum of \( \varphi \) over \( P \) equals its maximum over \( \{\x_1, \dots, \x_m\} \), which is \( \max_i\varphi(\x_i) \), attained at an \( \x_i \) with the largest value.

(c) The values at the corners are \( \varphi(1, 0) = 2 \), \( \varphi(3, 1) = 5 \), \( \varphi(0, 2) = -2 \). By (b), the maximum over the triangle is \( 5 \), at \( (3, 1) \). Applying (b) to \( -\varphi \), the minimum is \( -2 \), at \( (0, 2) \).
:::

### C. Going deeper

:::: {#exr-caratheodory-c1}
[C1: Carathéodory in the affine hull]

Let \( V \) be a real vector space, \( S \subseteq V \) non-empty, and suppose \( \operatorname{aff} S \) has dimension \( d \) (@def-affine-hull).

::: {.enumerate options="label=(\alph*)"}
1. Prove that every affinely independent list of points of \( S \) has at most \( d + 1 \) entries.
2. Hence prove that every point of \( \conv S \) is a convex combination of at most \( d + 1 \) points of \( S \).
3. Let \( S = \{(t, t, t) : 0 \le t \le 1\} \cup \{(2, 2, 2)\} \subseteq \nR^3 \). What bound does @thm-caratheodory give, and what bound does (b) give?
:::
::::

::: {.solution}
(a) By @prp-affine-hull-coset, \( \operatorname{aff} S = \x_0 + U \) with \( \dim U = d \). If \( (\y_0, \dots, \y_m) \) is an affinely independent list in \( S \), then each \( \y_i \) lies in \( \x_0 + U \), so each difference \( \y_i - \y_0 = (\y_i - \x_0) - (\y_0 - \x_0) \) lies in \( U \). By @lem-affine-dependence (a) the \( m \) differences are linearly independent, and they lie in the \( d \)-dimensional space \( U \), so \( m \le d \) by @thm-size-bounds (a).

(b) By @thm-caratheodory, each point of \( \conv S \) is a convex combination of an affinely independent list of points of \( S \), which has at most \( d + 1 \) entries by (a).

(c) Here \( n = 3 \), so @thm-caratheodory gives \( 4 \). All of \( S \) lies on the line \( \Span(\1) \), and \( S \) contains two distinct points, so \( \operatorname{aff} S \) is that line and \( d = 1 \); (b) gives \( 2 \). Indeed \( \conv S \) is the segment from \( \0 \) to \( (2, 2, 2) \), and each of its points is a convex combination of the two endpoints.
:::

:::: {#exr-caratheodory-c2}
[C2: Helly's theorem for a sequence of compact sets]

Let \( V \) be a real vector space of dimension \( n \) with a norm, and let \( C_1, C_2, C_3, \dots \) be a sequence of **compact** convex subsets of \( V \) such that every \( n + 1 \) of them have a common point.

::: {.enumerate options="label=(\alph*)"}
1. Prove that a compact set \( K \) is closed.
2. Prove that for each \( m \ge 1 \) there is a point \( \y_m \in C_1 \cap \dots \cap C_m \).
3. Prove that \( \bigcap_{k \ge 1} C_k \ne \emptyset \).
4. Explain where the argument fails for the closed half-lines \( [k, \infty) \) of the remark after @thm-helly.
:::

*Hint for (c): all the \( \y_m \) lie in \( C_1 \).*
::::

::: {.solution}
(a) Let \( \x_k \to \x \) with \( \x_k \in K \). By compactness, a subsequence converges to some \( \x' \in K \). It also converges to \( \x \), as a subsequence of a convergent sequence, and a limit is unique: \( \norm{\x - \x'} \le \norm{\x - \x_{k_j}} + \norm{\x_{k_j} - \x'} \to 0 \), so \( \x = \x' \) by (N1). Hence \( \x \in K \).

(b) For \( m \le n \), the sets \( C_1, \dots, C_m \), together with \( C_{m+1}, \dots, C_{n+1} \), are \( n + 1 \) of the sets, and a common point of all of them lies in \( C_1 \cap \dots \cap C_m \). For \( m \ge n + 1 \), @thm-helly applies to the convex sets \( C_1, \dots, C_m \).

(c) Every \( \y_m \) lies in the compact set \( C_1 \), so a subsequence \( \y_{m_j} \) converges to some \( \y \). Fix \( k \). For \( m_j \ge k \), \( \y_{m_j} \in C_k \), and \( C_k \) is closed by (a); the terms with \( m_j \ge k \) form a sequence in \( C_k \) converging to \( \y \), so \( \y \in C_k \). As \( k \) was arbitrary, \( \y \in \bigcap_k C_k \).

(d) Steps (a) and (b) survive for \( C_k = [k, \infty) \) with \( n = 1 \): the sets are closed, and \( \y_m = m \) lies in the first \( m \) of them. Step (c) fails, because \( C_1 = [1, \infty) \) is not compact: the sequence \( \y_m = m \) has no convergent subsequence, and the points escape to infinity instead of accumulating at a common point.
:::

:::: {#exr-caratheodory-c3}
[C3: The counts are sharp]

Let \( V \) be a real vector space of dimension \( n \), and let \( (\x_0, \dots, \x_n) \) be affinely independent.

::: {.enumerate options="label=(\alph*)"}
1. Prove that each point of \( \conv\{\x_0, \dots, \x_n\} \) has **exactly one** expression \( \sum_i t_i\x_i \) with \( \t \in \Delta_{n+1} \).
2. Deduce that \( \frac1{n+1}\sum_i \x_i \) is not a convex combination of any \( n \) of the points. (This recovers @exm-caratheodory-sharp.)
3. Prove that \( \x_0, \dots, \x_n \) have **no** Radon partition, so that \( n + 2 \) in @thm-radon cannot be lowered.
:::
::::

::: {.solution}
(a) If \( \sum_i t_i\x_i = \sum_i t_i'\x_i \) with \( \t, \t' \in \Delta_{n+1} \), then \( \sum_i (t_i - t_i')\x_i = \0 \) and \( \sum_i (t_i - t_i') = 1 - 1 = 0 \). By affine independence every \( t_i - t_i' = 0 \).

(b) The point has the expression with all weights \( \tfrac1{n+1} \). A convex combination of \( n \) of the points is an expression of the form in (a) with the omitted point given weight \( 0 \). By the uniqueness in (a), it would have to coincide with the all-\( \tfrac1{n+1} \) expression, which has no zero weight.

(c) Suppose \( I, J \) are disjoint, non-empty, and \( \sum_{i \in I} a_i\x_i = \sum_{j \in J} b_j\x_j \) with non-negative weights, each family adding up to \( 1 \). Then \( \sum_{i \in I} a_i\x_i - \sum_{j \in J} b_j\x_j = \0 \) is a relation among the \( \x_i \) whose coefficients add up to \( 1 - 1 = 0 \); an index lying in neither set gets coefficient \( 0 \), and no index lies in both, since \( I \cap J = \emptyset \). By affine independence, all these coefficients are \( 0 \), so every \( a_i = 0 \), contradicting \( \sum_{i \in I} a_i = 1 \). Hence no Radon partition exists.
:::
