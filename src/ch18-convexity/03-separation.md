# Separating Hyperplanes

Sections 01 and 02 looked at a convex set from the inside: which combinations of its points it contains, and how few points a combination needs. This section looks at it from the outside. A point that is not in a closed convex set can be cut off from it by a hyperplane, a set can be touched at its edge by a hyperplane that leaves the whole set on one side, and two disjoint convex sets can be pulled apart by one. All three facts come from a single construction, the point of the set nearest to a given point, and that construction is Chapter 11's orthogonal projection with the subspace replaced by a convex set.

**Throughout, \( V \) is a finite-dimensional real inner product space**, with inner product \( \inner{\cdot}{\cdot} \) (@def-inner-product), induced norm \( \norm{\cdot} \) (@def-induced-norm), and \( n = \dim V \). A sequence **converges**, \( \x_k \to \x \), when \( \norm{\x_k - \x} \to 0 \); **closed** means closed in the sense of @def-closed-set, so that a closed set contains the limit of every convergent sequence of its points. A set is **compact** if every sequence in it has a subsequence converging to a point of the set; this is the word of @cor-closed-bounded-compact, which says that every closed bounded subset of \( V \) is compact. The field is \( \nR \) because the whole section is about inequalities.

## The nearest point of a closed convex set

Chapter 11 answered a question about subspaces: given \( \v \) and a finite-dimensional subspace \( U \), which vector of \( U \) is closest to \( \v \)? @thm-best-approximation said there is exactly one, the orthogonal projection \( P_U\v \), and that \( \v - P_U\v \) is perpendicular to \( U \). Now replace \( U \) by a set with less structure, such as a disc, a box or a half-plane, and ask the same question. Two small experiments in \( \nR^2 \) show which hypotheses the answer needs.

- The **open** disc \( \{\y : \norm{\y} < 1\} \) and the point \( \x = (2, 0) \). The points \( (1 - 1/k, 0) \) of the disc come closer and closer to \( \x \), but the distance \( 1 \) is never reached, since the only candidate \( (1, 0) \) is missing. There is no nearest point. The set is convex but not closed.
- The **circle** \( \{\y : \norm{\y} = 1\} \) and the point \( \x = \0 \). Every point of the circle is at distance \( 1 \), so every point is a nearest point. The set is closed but not convex.

So we ask for both properties, and then everything works.

::: {#thm-nearest-point}
[Nearest Point Theorem]

Let \( C \) be a **non-empty, closed, convex** subset of \( V \), and let \( \x \in V \).

(a) There is **exactly one** point \( \p \in C \) with \( \norm{\x - \p} \le \norm{\x - \y} \) for every \( \y \in C \).

(b) A point \( \p \in C \) is this nearest point **if and only if**
\[
\inner{\x - \p}{\y - \p} \le 0 \qquad \text{for every } \y \in C .
\]{#eq-variational-inequality}
:::

The nearest point is written \( P_C(\x) \), and the map \( P_C \colon V \to C \) is the **projection onto \( C \)**. The number \( d(\x, C) = \norm{\x - P_C(\x)} \) is the **distance** from \( \x \) to \( C \).

::: {.idea}
Three jobs, three tools. ① Existence: a nearest point is a minimum of the continuous function \( \y \mapsto \norm{\x - \y} \), and a minimum exists on a compact set; \( C \) itself may be unbounded, so cut it down to the part of \( C \) within a fixed distance of \( \x \). ② The inequality @eq-variational-inequality is the first-order condition: slide from \( \p \) a little way towards another point \( \y \) of \( C \), which convexity allows, and ask that the distance not decrease. ③ Read backwards, the inequality says that the angle at \( \p \) between \( \x - \p \) and \( \y - \p \) is at least a right angle, and expanding \( \norm{\x - \y}^2 \) then gives \( \norm{\x - \y}^2 \ge \norm{\x - \p}^2 + \norm{\y - \p}^2 \). That inequality proves both that \( \p \) is nearest and that nothing else is.
:::

\begin{center}
\begin{tikzpicture}[scale=1.35]
  \fill[black!8] (-1.5,-1) -- (1.2,-1) -- (1.6,0.4) -- (0.4,1.3) -- (-1.4,0.6) -- cycle;
  \draw[thick] (-1.5,-1) -- (1.2,-1) -- (1.6,0.4) -- (0.4,1.3) -- (-1.4,0.6) -- cycle;
  \node at (-0.9,-0.55) {$C$};
  \coordinate (X) at (2.2,2.2);
  \coordinate (P) at (1.12,0.76);
  \coordinate (Y) at (-0.3,-0.2);
  \draw[dashed] (-0.88,2.26) -- (2.32,-0.14);
  \draw[->, very thick] (P) -- (X);
  \draw[->, thick] (P) -- (Y);
  \fill (X) circle (1.6pt) node[above right] {$\mathbf{x}$};
  \fill (P) circle (1.6pt);
  \node at (1.9,0.97) {$P_C(\mathbf{x})$};
  \fill (Y) circle (1.4pt) node[below left] {$\mathbf{y}$};
  \draw (P) ++(0.18,0.24) arc[start angle=53.1, end angle=214, radius=0.3];
  \node[align=center, font=\small] at (0.4,-1.75) {the angle at $P_C(\mathbf{x})$ between $\mathbf{x} - P_C(\mathbf{x})$ and $\mathbf{y} - P_C(\mathbf{x})$ is obtuse;\\ the dashed line through $P_C(\mathbf{x})$ is perpendicular to $\mathbf{x} - P_C(\mathbf{x})$};
\end{tikzpicture}
\end{center}

::: {.proof}
*Existence.* Since \( C \ne \emptyset \), pick \( \y_0 \in C \) and put \( R = \norm{\x - \y_0} \). Let
\[
K = \{\y \in C : \norm{\x - \y} \le R\} .
\]
Then \( \y_0 \in K \), and \( K \) is bounded, since \( \norm{\y} \le \norm{\x} + \norm{\y - \x} \le \norm{\x} + R \) for \( \y \in K \) by @cor-triangle-inequality. It is closed: if \( \y_k \in K \) and \( \y_k \to \y \), then \( \y \in C \) because \( C \) is closed, and
\[
\norm{\x - \y} \le \norm{\x - \y_k} + \norm{\y_k - \y} \le R + \norm{\y_k - \y}
\]
for every \( k \); the right-hand side tends to \( R \), and a non-strict inequality survives a limit, so \( \norm{\x - \y} \le R \). By @cor-closed-bounded-compact, the form in which Chapter 16 carried **the compactness of closed bounded sets, fact (A3) of Chapter 16's introduction**, over to every finite-dimensional space, \( K \) is compact. The function \( f(\y) = \norm{\x - \y} \) is continuous, since \( \lvert f(\y) - f(\y')\rvert \le \norm{\y - \y'} \) by @lem-reverse-triangle-norm. By **the extreme value theorem, fact (A4) of Chapter 16's introduction**, \( f \) attains a minimum on \( K \) at some \( \p \in K \). Every \( \y \in C \setminus K \) has \( f(\y) > R \ge f(\p) \). So \( \norm{\x - \p} \le \norm{\x - \y} \) for every \( \y \in C \).

*(b), \( (\Rightarrow) \).* Let \( \p \) be a nearest point and let \( \y \in C \). For \( 0 < t \le 1 \), the point \( \p + t(\y - \p) = (1 - t)\p + t\y \) lies in \( C \) by @def-convex-set. Hence, expanding with @thm-norm-properties (c) over \( \nR \),
\[
\norm{\x - \p}^2 \le \norm{(\x - \p) - t(\y - \p)}^2
= \norm{\x - \p}^2 - 2t\inner{\x - \p}{\y - \p} + t^2\norm{\y - \p}^2 .
\]
Cancel \( \norm{\x - \p}^2 \) and divide by \( 2t > 0 \): \( \inner{\x - \p}{\y - \p} \le \tfrac{t}{2}\norm{\y - \p}^2 \). This holds for every \( t = 1/k \), and letting \( k \to \infty \) gives @eq-variational-inequality.

*(b), \( (\Leftarrow) \), and uniqueness.* Let \( \p \in C \) satisfy @eq-variational-inequality, and let \( \y \in C \). The same expansion with \( t = 1 \) gives
\[
\begin{aligned}
\norm{\x - \y}^2 &= \norm{\x - \p}^2 - 2\inner{\x - \p}{\y - \p} + \norm{\y - \p}^2 \\
&\ge \norm{\x - \p}^2 + \norm{\y - \p}^2 .
\end{aligned} \tag{$\ast$}
\]
So \( \norm{\x - \y} \ge \norm{\x - \p} \), and \( \p \) is a nearest point. Finally, the nearest point \( \p \) found in the existence step satisfies @eq-variational-inequality by \( (\Rightarrow) \), so \( (\ast) \) applies to it; for \( \y \in C \) with \( \y \ne \p \) it gives \( \norm{\x - \y}^2 \ge \norm{\x - \p}^2 + \norm{\y - \p}^2 > \norm{\x - \p}^2 \), and \( \y \) is not a nearest point. This proves the theorem.
:::

The inequality \( (\ast) \) is Pythagoras with the equality relaxed to an inequality. That is exactly the relation with Chapter 11, and it deserves to be said precisely.

**This theorem generalizes @thm-best-approximation.** Let \( C = U \) be a subspace of \( V \). It is convex, and closed by @prp-closed-open-basics (c). For \( \p \in U \), the vector \( \y - \p \) runs over **all** of \( U \) as \( \y \) does, and with each \( \u \in U \) it also takes the value \( -\u \). So @eq-variational-inequality says \( \inner{\x - \p}{\u} \le 0 \) and \( -\inner{\x - \p}{\u} \le 0 \), that is,
\[
\inner{\x - \p}{\u} = 0 \qquad \text{for every } \u \in U .
\]
**For a subspace the variational inequality becomes an equality**, the statement \( \x - \p \in U^{\perp} \). Then \( \x = \p + (\x - \p) \) is the splitting of @thm-orthogonal-decomposition (a), so \( P_C(\x) = P_U\x \) by @def-orthogonal-projection, and \( (\ast) \) becomes the equation of @thm-pythagoras used in the proof of @thm-best-approximation. The projection onto a closed convex set is the orthogonal projection with "perpendicular" weakened to "at an obtuse angle".

::: {#exm-nearest-point-examples}
[Three projections]

Find \( P_C(\x) \) in each case, and check @eq-variational-inequality.

::: {.enumerate options="label=(\alph*)"}
1. \( C \) is the closed unit ball \( \{\y : \norm{\y} \le 1\} \) of \( V \), and \( \norm{\x} > 1 \).
2. \( C \) is the box \( [0,1]^3 = \{\y \in \nR^3 : 0 \le y_i \le 1 \text{ for each } i\} \) with the dot product, and \( \x = (3, -1, 2) \).
3. \( C \) is the half-space \( \{\y : \inner{\a}{\y} \le c\} \), where \( \a \ne \0 \), and \( \inner{\a}{\x} > c \).
:::
:::

::: {.solution}
(a) \( P_C(\x) = \x/\norm{\x} \). With \( \p = \x/\norm{\x} \) we have \( \norm{\p} = 1 \) and \( \x - \p = (\norm{\x} - 1)\p \), so for \( \y \in C \)
\[
\inner{\x - \p}{\y - \p} = (\norm{\x} - 1)\bigl(\inner{\p}{\y} - 1\bigr) \le 0 ,
\]
because \( \norm{\x} - 1 > 0 \) and \( \inner{\p}{\y} \le \norm{\p}\norm{\y} \le 1 \) by @thm-cauchy-schwarz. By @thm-nearest-point (b), \( \p \) is the nearest point, and \( d(\x, C) = \norm{\x} - 1 \).

(b) Clamp each coordinate into \( [0, 1] \): \( \p = (1, 0, 1) \). Then \( \x - \p = (2, -1, 1) \) and, for \( \y \in C \),
\[
\inner{\x - \p}{\y - \p} = 2(y_1 - 1) - y_2 + (y_3 - 1) \le 0 ,
\]
since \( y_1 \le 1 \), \( y_2 \ge 0 \) and \( y_3 \le 1 \). So \( P_C(\x) = (1, 0, 1) \) and \( d(\x, C) = \sqrt{4 + 1 + 1} = \sqrt6 \). The vector \( \a = \x - \p = (2, -1, 1) \) also cuts \( \x \) off: \( \inner{\a}{\x} = 9 \) and \( \norm{\a}^2 = 6 \), so \( c = \inner{\a}{\x} - \tfrac12\norm{\a}^2 = 6 \), and the plane \( 2y_1 - y_2 + y_3 = 6 \) strictly separates \( C \) from \( \x \), since its left side is at most \( 2 + 0 + 1 = 3 \) on \( C \) and equals \( 9 \) at \( \x \). @thm-separation-point below turns this recipe into a theorem.

(c) Put \( \lambda = (\inner{\a}{\x} - c)/\norm{\a}^2 \), which is positive, and \( \p = \x - \lambda\a \). Then \( \inner{\a}{\p} = \inner{\a}{\x} - \lambda\norm{\a}^2 = c \), so \( \p \in C \), and for \( \y \in C \)
\[
\inner{\x - \p}{\y - \p} = \lambda\bigl(\inner{\a}{\y} - c\bigr) \le 0 .
\]
So \( P_C(\x) = \x - \lambda\a \): drop the perpendicular to the boundary hyperplane, as Chapter 11 would have done. The distance is \( \lambda\norm{\a} = (\inner{\a}{\x} - c)/\norm{\a} \).
:::

Two degenerate cases fix the scale. If \( C = \{\c\} \) is a single point, then \( P_C(\x) = \c \) for every \( \x \), and @eq-variational-inequality holds because \( \y - \p = \0 \). If \( C = V \), then \( P_C \) is the identity. In every case \( P_C(\x) = \x \) exactly when \( \x \in C \).

::: {.check}
Where did the proof of @thm-nearest-point use that \( C \) is closed, and where that it is convex? Match each use with one of the two failing experiments before the theorem.
:::

::: {.solution}
Closedness was used in the existence step, to make \( K \) closed and hence compact; the open disc fails there, since the minimizing candidates converge to a point outside it. Convexity was used in \( (\Rightarrow) \), to know that \( (1 - t)\p + t\y \in C \), and uniqueness rests on that step. The circle fails there: with \( \x = \0 \), \( \p = \e_1 \) and \( \y = -\e_1 \), \( \inner{\x - \p}{\y - \p} = 2 > 0 \).
:::

::: {.warning}
**The proof needs an inner product, and uniqueness can fail without one.** In \( \nR^2 \) with \( \norm{\cdot}_\infty \), let \( C \) be the \( x_1 \)-axis, which is closed and convex, and \( \x = (0, 1) \). Then \( \norm{\x - (t, 0)}_\infty = \max(\lvert t\rvert, 1) = 1 \) for every \( t \in [-1, 1] \), so there is a whole segment of nearest points. Existence survives, since its proof used only (N3) and compactness. Uniqueness does not, because it came from the expansion of \( \norm{\x - \y}^2 \), which is available only for induced norms.
:::

## Hyperplanes and half-spaces

A hyperplane in the sense of Chapter 5 passes through \( \0 \): it is a subspace of codimension \( 1 \) (@def-hyperplane). To separate sets we need translates of hyperplanes, and Chapter 5 §06 called a coset \( \p + H \) of a hyperplane \( H \) (@def-coset) an **affine hyperplane**. In an inner product space these have a concrete form. By @thm-hyperplane-kernel-functional, \( H = \ker\varphi \) for a non-zero \( \varphi \in V^{*} \); by @thm-riesz-representation, \( \varphi = \inner{\cdot}{\a} \) for a non-zero \( \a \in V \). Hence
\[
\p + H = \{\y \in V : \inner{\a}{\y} = c\}, \qquad c = \inner{\a}{\p} ,
\]
and conversely every such set with \( \a \ne \0 \) is an affine hyperplane, with \( \a \) as a **normal vector**. It cuts \( V \) into the two **closed half-spaces** \( \{\inner{\a}{\cdot} \le c\} \) and \( \{\inner{\a}{\cdot} \ge c\} \). Both are convex, because \( \inner{\a}{\cdot} \) is linear, and closed by @prp-closed-open-basics (c).

::: {#def-separation}
[Separation by a Hyperplane]

Let \( A, B \subseteq V \) be non-empty. A **non-zero** vector \( \a \in V \) and a number \( c \in \nR \) **separate** \( A \) and \( B \) if
\[
\inner{\a}{\x} \le c \le \inner{\a}{\y} \qquad \text{for all } \x \in A \text{ and all } \y \in B .
\]
They **strictly separate** \( A \) and \( B \) if in addition there is a real \( \varepsilon > 0 \) with \( \inner{\a}{\x} \le c - \varepsilon \) and \( \inner{\a}{\y} \ge c + \varepsilon \) for all \( \x \in A \), \( \y \in B \).
:::

In words: \( A \) lies in one closed half-space of \( \{\inner{\a}{\cdot} = c\} \) and \( B \) in the other, and strict separation puts a slab of width \( 2\varepsilon/\norm{\a} \) between them. Replacing \( (\a, c) \) by \( (-\a, -c) \) swaps the roles of \( A \) and \( B \). With \( \a = \0 \) and \( c = 0 \) any two sets would be "separated".

## Cutting off a point

The first consequence of @thm-nearest-point is the one the chapter uses most. If \( \x \) is not in \( C \), the vector from \( P_C(\x) \) to \( \x \) is a normal vector for a hyperplane that cuts \( \x \) off.

::: {#thm-separation-point}
[Separating a Point from a Closed Convex Set]

Let \( C \subseteq V \) be non-empty, closed and convex, and let \( \x \notin C \). Put \( \a = \x - P_C(\x) \). Then \( \a \ne \0 \) and
\[
\inner{\a}{\y} \le \inner{\a}{\x} - \norm{\a}^2 \qquad \text{for every } \y \in C .
\]
In particular \( \a \) and \( c = \inner{\a}{\x} - \tfrac12\norm{\a}^2 \) strictly separate \( C \) and \( \{\x\} \).
:::

::: {.proof}
Write \( \p = P_C(\x) \). Since \( \p \in C \) and \( \x \notin C \), \( \a = \x - \p \ne \0 \). For \( \y \in C \), @eq-variational-inequality gives \( \inner{\a}{\y - \p} \le 0 \), hence
\[
\inner{\a}{\y} \le \inner{\a}{\p} = \inner{\a}{\x} - \inner{\a}{\x - \p} = \inner{\a}{\x} - \norm{\a}^2 .
\]
With \( \varepsilon = \tfrac12\norm{\a}^2 > 0 \) this reads \( \inner{\a}{\y} \le c - \varepsilon \), while \( \inner{\a}{\x} = c + \varepsilon \). This proves the theorem.
:::

In the picture after @thm-nearest-point, the hyperplane of the theorem is the line parallel to the dashed one, halfway between \( P_C(\x) \) and \( \x \).

The theorem turns into a description of a closed convex set from the outside. Sections 01 and 02 built convex sets up from points; this builds them down from half-spaces.

::: {#cor-closed-convex-halfspaces}
[A Closed Convex Set Is an Intersection of Half-Spaces]

Every non-empty closed convex subset \( C \) of \( V \) is the intersection of all the closed half-spaces \( \{\y : \inner{\a}{\y} \le c\} \), with \( \a \ne \0 \), that contain \( C \).
:::

::: {.proof}
Each of these half-spaces contains \( C \), so \( C \) lies in their intersection. Conversely, let \( \x \notin C \). By @thm-separation-point, with \( \a = \x - P_C(\x) \ne \0 \), the half-space \( \{\y : \inner{\a}{\y} \le \inner{\a}{\x} - \norm{\a}^2\} \) contains \( C \) but not \( \x \). So \( \x \) is not in the intersection. (If \( C = V \), the family of half-spaces is empty and its intersection is \( V \) by convention.)
:::

The corollary has a converse that is immediate: an intersection of closed half-spaces is closed and convex, because each half-space is and both properties pass to intersections. So the closed convex sets are **exactly** the intersections of closed half-spaces. §04 turns this into a formula, the support function, and §09 studies the case of finitely many half-spaces.

## Supporting hyperplanes

A point on the edge of \( C \) cannot be cut off, because it belongs to \( C \). The best one can hope for is a hyperplane through the point with all of \( C \) on one side, touching \( C \) without cutting it. To say "on the edge" we need two more words.

::: {#def-interior-point}
[Interior Point, Closure, Boundary Point]

Let \( S \subseteq V \). A point \( \x \in V \) is an **interior point** of \( S \) if there is a real \( r > 0 \) such that **every** \( \y \) with \( \norm{\y - \x} < r \) lies in \( S \); the set of interior points is written \( \interior{S} \). The **closure** \( \closure{S} \) of \( S \) is the set of limits of all convergent sequences of points of \( S \). A **boundary point** of \( S \) is a point of \( \closure{S} \) that is not an interior point of \( S \).
:::

Constant sequences show \( S \subseteq \closure{S} \), and by @def-closed-set, \( S \) is closed exactly when \( \closure{S} = S \). By @thm-norm-equivalence neither notion depends on the norm used: a ball of radius \( r \) for one norm contains a ball of positive radius for any other. For the closed unit disc of \( \nR^2 \), the interior points are those with \( \norm{\x} < 1 \), and the boundary points form the unit circle. A segment in \( \nR^2 \) has no interior points at all, so every one of its points is a boundary point; that is the case the next lemma isolates.

::: {#lem-convex-solid-or-flat}
[A Convex Set Is Solid or Flat]

Let \( V \ne \{\0\} \) and let \( C \subseteq V \) be non-empty and convex. Then **either** \( C \) has an interior point, **or** \( C \) lies in an affine hyperplane: there are \( \a \ne \0 \) and \( c \in \nR \) with \( \inner{\a}{\y} = c \) for every \( \y \in C \).
:::

::: {.idea}
Fix \( \c_0 \in C \) and look at the directions \( \y - \c_0 \) available inside \( C \). If they span a proper subspace, a normal vector to that subspace is the \( \a \) we want. If they span \( V \), then \( C \) contains \( n + 1 \) points in general position, hence the solid simplex they span, and the center of a solid simplex is an interior point because its barycentric coordinates change only a little when the point moves a little.
:::

::: {.proof}
Fix \( \c_0 \in C \) and let \( W = \Span\{\y - \c_0 : \y \in C\} \).

*Case 1: \( W \ne V \).* Then \( \dim W < n \), so \( \dim W^{\perp} = n - \dim W \ge 1 \) by @thm-orthogonal-decomposition (c), and there is \( \a \ne \0 \) in \( W^{\perp} \). For \( \y \in C \), \( \inner{\a}{\y - \c_0} = 0 \), that is, \( \inner{\a}{\y} = \inner{\a}{\c_0} \). Take \( c = \inner{\a}{\c_0} \).

*Case 2: \( W = V \).* Choose a linearly independent list \( (\y_1 - \c_0, \dots, \y_m - \c_0) \) with every \( \y_i \in C \) and \( m \) as large as possible; \( m \le n \) by @thm-size-bounds. Every vector \( \y - \c_0 \) with \( \y \in C \) lies in the span of this list, since otherwise @lem-append-independent would lengthen it. So the span contains every generator of \( W \), hence equals \( V \), and the list is a basis; thus \( m = n \). Let \( \varphi_i(\v) \) be the \( i \)-th coordinate of \( \v \) in this basis, a linear functional by @thm-coordinates-linear, and write \( \varphi_i = \inner{\cdot}{\w_i} \) by @thm-riesz-representation. Put \( \mu_i(\v) = \varphi_i(\v - \c_0) \). Then for every \( \v \in V \),
\[
\v = \Bigl(1 - \sum_{i=1}^{n}\mu_i(\v)\Bigr)\c_0 + \sum_{i=1}^{n}\mu_i(\v)\,\y_i ,
\]
and when \( \mu_i(\v) \ge 0 \) for every \( i \) and \( \sum_i\mu_i(\v) \le 1 \), this is a convex combination of points of \( C \), hence a point of \( C \): by @thm-convex-hull-combinations it lies in \( \conv C \), and \( \conv C = C \) by @def-convex-hull, since \( C \) is itself a convex set containing \( C \).

Let \( \z = \c_0 + \tfrac{1}{n+1}\sum_i(\y_i - \c_0) \), so that \( \mu_i(\z) = \tfrac{1}{n+1} \) for every \( i \). Each \( \w_i \ne \0 \), because \( \varphi_i(\y_i - \c_0) = 1 \); put \( L = \max_i\norm{\w_i} > 0 \) and \( r = 1/\bigl(n(n+1)L\bigr) \). If \( \norm{\v - \z} < r \), then by @thm-cauchy-schwarz
\[
\lvert\mu_i(\v) - \mu_i(\z)\rvert = \lvert\inner{\v - \z}{\w_i}\rvert \le L\norm{\v - \z} < \frac{1}{n(n+1)} ,
\]
so \( \mu_i(\v) > \tfrac{1}{n+1} - \tfrac{1}{n(n+1)} \ge 0 \) and \( \sum_i\mu_i(\v) < \tfrac{n}{n+1} + \tfrac{1}{n+1} = 1 \). Hence \( \v \in C \), and \( \z \) is an interior point of \( C \).
:::

The second ingredient says that from an interior point one can see the whole closure.

::: {#lem-closure-convex}
[Closure and Interior of a Convex Set]

Let \( C \subseteq V \) be convex.

::: {.enumerate options="label=(\alph*)"}
1. \( \closure{C} \) is closed and convex.
2. If \( \z \in \interior{C} \), \( \w \in \closure{C} \) and \( 0 < t \le 1 \), then \( (1 - t)\w + t\z \in \interior{C} \).
:::
:::

::: {.idea}
Part (a) pushes limits through: a limit of limits is a limit, and a convex combination of limits is the limit of convex combinations. For (b), picture a small ball around \( \z \) inside \( C \), and the cone from \( \w \) over it. The cone contains a smaller ball around \( (1 - t)\w + t\z \); since \( \w \) is only a limit, replace it by a nearby point \( \w' \) of \( C \), which shrinks the ball by half.
:::

::: {.proof}
(a) Let \( \x_k \in \closure{C} \) with \( \x_k \to \x \). Each \( \x_k \) is a limit of points of \( C \), so there is \( \c_k \in C \) with \( \norm{\c_k - \x_k} < 1/k \). Then \( \norm{\c_k - \x} \le 1/k + \norm{\x_k - \x} \to 0 \), so \( \x \in \closure{C} \). For convexity, let \( \x = \lim\c_k \) and \( \y = \lim\d_k \) with \( \c_k, \d_k \in C \), and \( 0 \le s \le 1 \). The points \( s\c_k + (1 - s)\d_k \) lie in \( C \) and converge to \( s\x + (1 - s)\y \), by @cor-triangle-inequality, so that point lies in \( \closure{C} \).

(b) Take \( \rho > 0 \) with every point within distance \( \rho \) of \( \z \) in \( C \), and put \( \p = (1 - t)\w + t\z \). If \( t = 1 \) then \( \p = \z \) and there is nothing to prove, so let \( t < 1 \). Choose \( \w' \in C \) with \( (1 - t)\norm{\w - \w'} < t\rho/2 \), possible because \( \w \) is a limit of points of \( C \). Let \( \norm{\q - \p} < t\rho/2 \), and put \( \z' = \bigl(\q - (1 - t)\w'\bigr)/t \), so that \( \q = (1 - t)\w' + t\z' \). Since \( \p = (1 - t)\w + t\z \),
\[
\z' - \z = \frac{(\q - \p) + (1 - t)(\w - \w')}{t} ,
\qquad \norm{\z' - \z} < \frac{t\rho/2 + t\rho/2}{t} = \rho .
\]
Hence \( \z' \in C \), and \( \q \in C \) by @def-convex-set. So every point within \( t\rho/2 \) of \( \p \) lies in \( C \), and \( \p \in \interior{C} \).
:::

Now the theorem. It asks only that \( \x_0 \) not be an interior point, which covers the boundary points of \( C \) and also the points outside \( \closure{C} \).

::: {#thm-supporting-hyperplane}
[Supporting Hyperplane Theorem]

Let \( V \ne \{\0\} \), let \( C \subseteq V \) be convex, and let \( \x_0 \in V \) be a point that is **not** an interior point of \( C \). Then there is a **non-zero** \( \a \in V \) with
\[
\inner{\a}{\y} \le \inner{\a}{\x_0} \qquad \text{for every } \y \in C .
\]
If moreover \( \x_0 \in C \), the affine hyperplane \( \{\y : \inner{\a}{\y} = \inner{\a}{\x_0}\} \) passes through \( \x_0 \) and has \( C \) in one of its closed half-spaces; it is called a **supporting hyperplane** of \( C \) at \( \x_0 \).
:::

::: {.idea}
Approach \( \x_0 \) from outside \( \closure{C} \) and cut off each approximating point with @thm-separation-point. The normal vectors, scaled to length \( 1 \), live on the compact unit sphere, so a subsequence converges, and in the limit the strict inequalities become the non-strict one we want. The only thing that could go wrong is that there are no points outside \( \closure{C} \) near \( \x_0 \). @lem-convex-solid-or-flat and @lem-closure-convex rule that out: if \( C \) is flat, its own hyperplane serves; if \( C \) is solid, pushing \( \x_0 \) directly away from an interior point leaves \( \closure{C} \) at once.
:::

::: {.proof}
If \( C = \emptyset \), any non-zero \( \a \) works, and one exists because \( V \ne \{\0\} \). So let \( C \ne \emptyset \).

*Case 1: \( C \) has no interior point.* By @lem-convex-solid-or-flat there are \( \a \ne \0 \) and \( c \) with \( \inner{\a}{\y} = c \) for all \( \y \in C \). If \( \inner{\a}{\x_0} \ge c \), then \( \a \) works. Otherwise \( -\a \) works, since \( \inner{-\a}{\y} = -c < -\inner{\a}{\x_0} \).

*Case 2: \( C \) has an interior point \( \z \).* For \( k \ge 1 \) let \( \x_k = \x_0 + \tfrac1k(\x_0 - \z) \). We claim \( \x_k \notin \closure{C} \). Indeed, with \( t = \tfrac{1}{k+1} \),
\[
(1 - t)\x_k + t\z = \tfrac{k}{k+1}\x_0 + \tfrac{1}{k+1}(\x_0 - \z) + \tfrac{1}{k+1}\z = \x_0 ,
\]
so if \( \x_k \) were in \( \closure{C} \), then \( \x_0 \) would be an interior point of \( C \) by @lem-closure-convex (b), contrary to the hypothesis. By @lem-closure-convex (a), \( \closure{C} \) is non-empty, closed and convex, so @thm-separation-point, applied to \( \closure{C} \) and \( \x_k \), gives \( \b_k \ne \0 \) with \( \inner{\b_k}{\y} \le \inner{\b_k}{\x_k} \) for all \( \y \in \closure{C} \), in particular for all \( \y \in C \). Put \( \a_k = \b_k/\norm{\b_k} \), a unit vector satisfying the same inequality.

The unit sphere of \( V \) is compact by @cor-closed-bounded-compact, which rests on **fact (A3) of Chapter 16's introduction**. So a subsequence \( (\a_{k_j}) \) converges to some \( \a \) with \( \norm{\a} = 1 \); in particular \( \a \ne \0 \). Fix \( \y \in C \). Then \( \inner{\a_{k_j}}{\y - \x_{k_j}} \le 0 \) for every \( j \), and \( \x_k \to \x_0 \) because \( \norm{\x_k - \x_0} = \norm{\x_0 - \z}/k \). By @thm-cauchy-schwarz,
\[
\begin{aligned}
\bigl\lvert\inner{\a_{k_j}}{\y - \x_{k_j}} - \inner{\a}{\y - \x_0}\bigr\rvert
&\le \bigl\lvert\inner{\a_{k_j} - \a}{\y - \x_{k_j}}\bigr\rvert + \bigl\lvert\inner{\a}{\x_0 - \x_{k_j}}\bigr\rvert \\
&\le \norm{\a_{k_j} - \a}\bigl(\norm{\y - \x_0} + \norm{\x_0 - \z}\bigr) + \norm{\x_0 - \x_{k_j}} ,
\end{aligned}
\]
which tends to \( 0 \). A non-strict inequality survives the limit, so \( \inner{\a}{\y - \x_0} \le 0 \). This proves the theorem.
:::

A supporting hyperplane need not be unique. At the corner \( (1, 1) \) of the square \( [-1, 1]^2 \), every \( \a = (a_1, a_2) \) with \( a_1, a_2 \ge 0 \), not both zero, works, since \( a_1y_1 + a_2y_2 \le a_1 + a_2 \) on the square. At a point of the unit circle, the boundary of the disc, only the positive multiples of the point itself work. Corners admit many supporting hyperplanes and smooth points one; §08 builds its induction on dimension on these hyperplanes, and §04 uses them to prove that a norm is recovered from its dual.

## Separating two convex sets

To separate two sets, separate one point from one set: the point \( \0 \) from the set of differences.

::: {#thm-separating-hyperplane}
[Separating Hyperplane Theorem]

Let \( C_1, C_2 \subseteq V \) be **non-empty, disjoint** and convex.

::: {.enumerate options="label=(\alph*)"}
1. If \( C_1 \) is **compact** and \( C_2 \) is **closed**, then \( C_1 \) and \( C_2 \) are strictly separated: there are \( \a \ne \0 \) and \( c \) with \( \inner{\a}{\x} < c < \inner{\a}{\y} \) for all \( \x \in C_1 \), \( \y \in C_2 \), and indeed with a margin \( \varepsilon > 0 \) as in @def-separation.
2. In general, \( C_1 \) and \( C_2 \) are separated: there are \( \a \ne \0 \) and \( c \) with \( \inner{\a}{\x} \le c \le \inner{\a}{\y} \) for all \( \x \in C_1 \), \( \y \in C_2 \).
:::
:::

::: {.idea}
The difference set \( D = \{\y - \x : \x \in C_1, \y \in C_2\} \) is convex and misses \( \0 \), and a normal \( \a \) with \( D \) on its positive side separates \( C_1 \) from \( C_2 \). For (a), compactness of \( C_1 \) makes \( D \) closed, and @thm-separation-point cuts \( \0 \) off; for (b), \( \0 \) is not an interior point of \( D \), and @thm-supporting-hyperplane applies.
:::

::: {.proof}
Let \( D = \{\y - \x : \x \in C_1, \y \in C_2\} \). It is convex: for \( 0 \le t \le 1 \),
\[
t(\y - \x) + (1 - t)(\y' - \x') = \bigl(t\y + (1 - t)\y'\bigr) - \bigl(t\x + (1 - t)\x'\bigr) ,
\]
a difference of a point of \( C_2 \) and a point of \( C_1 \). And \( \0 \notin D \), since \( C_1 \cap C_2 = \emptyset \).

(a) We show \( D \) is closed. Let \( \y_k - \x_k \to \d \) with \( \x_k \in C_1 \), \( \y_k \in C_2 \). Since \( C_1 \) is compact, a subsequence \( \x_{k_j} \) converges to some \( \x \in C_1 \). Then \( \y_{k_j} = (\y_{k_j} - \x_{k_j}) + \x_{k_j} \to \d + \x \), since a subsequence of a convergent sequence has the same limit, part of the elementary algebra of limits that Chapter 16's introduction imports; so \( \d + \x \in C_2 \) because \( C_2 \) is closed, and \( \d = (\d + \x) - \x \in D \). Now @thm-separation-point, applied to \( D \) and the point \( \0 \notin D \), gives \( \b \ne \0 \) with \( \inner{\b}{\d} \le -\norm{\b}^2 \) for all \( \d \in D \). With \( \a = -\b \) this says
\[
\inner{\a}{\x} + \norm{\a}^2 \le \inner{\a}{\y} \qquad \text{for all } \x \in C_1,\ \y \in C_2 .
\]
Fix \( \y \in C_2 \). The numbers \( \inner{\a}{\x} \), \( \x \in C_1 \), are bounded above by \( \inner{\a}{\y} - \norm{\a}^2 \), so by **the completeness of \( \nR \), fact (A1) of Chapter 16's introduction**, they have a least upper bound \( s \), and \( s + \norm{\a}^2 \le \inner{\a}{\y} \) for every \( \y \in C_2 \). Take \( \varepsilon = \tfrac12\norm{\a}^2 \) and \( c = s + \varepsilon \). Then \( \inner{\a}{\x} \le s = c - \varepsilon \) and \( \inner{\a}{\y} \ge c + \varepsilon \).

(b) If \( V = \{\0\} \), two non-empty subsets both contain \( \0 \) and cannot be disjoint, so \( V \ne \{\0\} \). The point \( \0 \) is not in \( D \), so it is not an interior point of \( D \). By @thm-supporting-hyperplane there is \( \b \ne \0 \) with \( \inner{\b}{\d} \le \inner{\b}{\0} = 0 \) for all \( \d \in D \). With \( \a = -\b \), this says \( \inner{\a}{\x} \le \inner{\a}{\y} \) for all \( \x \in C_1 \), \( \y \in C_2 \). As in (a), the least upper bound \( c \) of the numbers \( \inner{\a}{\x} \), \( \x \in C_1 \), exists by (A1) and satisfies \( \inner{\a}{\x} \le c \le \inner{\a}{\y} \). This proves the theorem.
:::

## Where strict separation fails

Part (a) asked one of the two sets to be compact. That hypothesis cannot be weakened to "closed", and the standard witness is a hyperbola and its asymptote.

::: {#exm-hyperbola-asymptote}
[A hyperbola and its asymptote]

In \( \nR^2 \) with the dot product, let
\[
A = \{\x : x_1 > 0,\ x_2 > 0,\ x_1x_2 \ge 1\} , \qquad B = \{\x : x_2 = 0\} .
\]
Show that \( A \) and \( B \) are non-empty, disjoint, closed and convex, that the \( x_1 \)-axis is the **only** hyperplane separating them, and that they are **not** strictly separated.
:::

\begin{center}
\begin{tikzpicture}[scale=0.9]
  \fill[black!8] plot[smooth] coordinates {(0.3,3.333) (0.4,2.5) (0.5,2) (0.7,1.4286) (1,1) (1.4,0.7143) (2,0.5) (2.8,0.3571) (4,0.25) (5,0.2)} -- (5,3.333) -- cycle;
  \draw[very thick] plot[smooth] coordinates {(0.3,3.333) (0.4,2.5) (0.5,2) (0.7,1.4286) (1,1) (1.4,0.7143) (2,0.5) (2.8,0.3571) (4,0.25) (5,0.2)};
  \draw[->, gray] (0,-0.6) -- (0,3.6) node[left, black] {$x_2$};
  \draw[very thick] (-1.2,0) -- (5.4,0) node[right] {$B$};
  \node at (2.6,2) {$A$};
  \node[font=\small, align=center] at (2.1,-1.2) {$A$ and $B$ are closed, convex and disjoint,\\ but the gap between them shrinks to zero};
\end{tikzpicture}
\end{center}

::: {.solution}
*Non-empty and disjoint.* \( (1, 1) \in A \) and \( \0 \in B \); every point of \( A \) has \( x_2 > 0 \), and every point of \( B \) has \( x_2 = 0 \).

*\( B \) is closed and convex.* It is a subspace, so it is convex, and closed by @prp-closed-open-basics (c).

*\( A \) is convex.* Let \( \x, \z \in A \) and \( 0 \le t \le 1 \), and let \( \w = t\x + (1 - t)\z \). Its coordinates are positive. Expanding,
\[
w_1w_2 = t^2x_1x_2 + (1 - t)^2z_1z_2 + t(1 - t)(x_1z_2 + x_2z_1) .
\]
By \( \bigl(\sqrt{x_1z_2} - \sqrt{x_2z_1}\bigr)^2 \ge 0 \), we get \( x_1z_2 + x_2z_1 \ge 2\sqrt{x_1x_2z_1z_2} \ge 2 \), using \( x_1x_2 \ge 1 \) and \( z_1z_2 \ge 1 \). Hence \( w_1w_2 \ge t^2 + (1 - t)^2 + 2t(1 - t) = 1 \), and \( \w \in A \).

*\( A \) is closed.* If \( \x_k \to \x \) with \( \x_k \in A \), then the coordinates converge, so \( x_1, x_2 \ge 0 \), and \( x_{k,1}x_{k,2} \to x_1x_2 \) by the algebra of limits, so \( x_1x_2 \ge 1 \). A product that is at least \( 1 \) has no zero factor, so \( x_1, x_2 > 0 \), and \( \x \in A \).

*The only separating hyperplane.* Let \( \a \ne \0 \) and \( c \) separate \( A \) and \( B \), in either order. On \( B \), \( \inner{\a}{(t, 0)} = a_1t \) for all real \( t \), and these values lie on one side of \( c \); that forces \( a_1 = 0 \). So \( a_2 \ne 0 \), and after replacing \( (\a, c) \) by \( (-\a, -c) \) we may take \( a_2 > 0 \). On \( B \) the value is \( 0 \). On \( A \) the values are \( a_2x_2 \), and since \( (1/s, s) \in A \) for every \( s > 0 \), they fill the interval \( (0, \infty) \). These are unbounded above, so \( A \) is on the side \( \ge c \) and \( B \) on the side \( \le c \): \( 0 \le c \le a_2s \) for every \( s > 0 \), which forces \( c = 0 \). The hyperplane \( \{a_2x_2 = 0\} \) is the \( x_1 \)-axis, and it separates, since \( a_2x_2 > 0 \) on \( A \) and \( = 0 \) on \( B \).

*No strict separation.* Strict separation would need the only separating hyperplane to miss both sets, and \( B \) **is** that hyperplane.
:::

The points \( (t, 1/t) \in A \) and \( (t, 0) \in B \) are \( 1/t \) apart, and @exr-separation-c2 shows that this vanishing distance is exactly what rules out strict separation.

::: {.warning}
**Disjoint closed convex sets need not be strictly separated.** The hyperbola region and its asymptote above are the example to remember: both closed, both convex, disjoint, and every hyperplane that separates them contains one of them. "Disjoint" gives only the weak separation of @thm-separating-hyperplane (b). Strict separation needs more, such as compactness of one set in (a).
:::

## Extending linear functionals

Separation has an analytic twin. Instead of a set and a point, take a linear functional defined on a subspace and bounded there by a convex function; can it be extended to the whole space without breaking the bound? The bounds allowed are the following.

::: {#def-sublinear-functional}
[Sublinear Functional]

Let \( V \) be a real vector space. A function \( p \colon V \to \nR \) is **sublinear** if, for **all** \( \x, \y \in V \) and **all** real \( t \ge 0 \),
\[
p(\x + \y) \le p(\x) + p(\y) \qquad\text{and}\qquad p(t\x) = t\,p(\x) .
\]
:::

Every norm is sublinear: (N3) is the first condition, and (N2) with \( t \ge 0 \) the second. Every linear functional is sublinear, with equality in the first condition. So is \( p(\x) = \max(x_1, x_2) \) on \( \nR^2 \), which is neither a norm nor linear: \( p(-\e_1) = 0 \). Taking \( t = 0 \) gives \( p(\0) = 0 \). A non-example by minimal change is \( p(\x) = \norm{\x}^2 \): the first condition fails at \( \x = \y \ne \0 \) (it would give \( 4\norm{\x}^2 \le 2\norm{\x}^2 \)), and so does the second, since \( p(t\x) = t^2p(\x) \).

It turns out that sublinearity is exactly what makes one-step extensions possible.

::: {#thm-hahn-banach-finite}
[Hahn–Banach Theorem, Finite-Dimensional]

Let \( V \) be a **finite-dimensional** real vector space, let \( p \) be a sublinear functional on \( V \), let \( U \) be a subspace of \( V \), and let \( f \in U^{*} \) satisfy \( f(\u) \le p(\u) \) for every \( \u \in U \). Then there is \( F \in V^{*} \) with
\[
F(\u) = f(\u) \text{ for every } \u \in U
\qquad\text{and}\qquad
F(\v) \le p(\v) \text{ for every } \v \in V .
\]
:::

::: {.idea}
Add one dimension at a time. On \( U + \Span(\v) \), a linear extension is fixed by one number \( c = F(\v) \). The requirement \( F \le p \) at the vectors \( \u + t\v \) with \( t > 0 \) gives upper bounds on \( c \), and at those with \( t < 0 \) it gives lower bounds. Sublinearity of \( p \), together with linearity of \( f \), is exactly what makes every lower bound at most every upper bound, so some \( c \) fits. Then induct on \( \dim V - \dim U \). No inner product is needed.
:::

::: {.proof}
We induct on \( k = \dim V - \dim U \). If \( k = 0 \), then \( U = V \) and \( F = f \) works.

Let \( k \ge 1 \) and assume the theorem whenever the difference of dimensions is \( k - 1 \). Pick \( \v \in V \setminus U \) and let \( W = U + \Span(\v) \). Each \( \w \in W \) can be written as \( \u + t\v \) with \( \u \in U \) and \( t \in \nR \), and only in one way: if \( \u + t\v = \u' + t'\v \) with \( t \ne t' \), then \( \v = (\u' - \u)/(t - t') \in U \), which is false; so \( t = t' \) and \( \u = \u' \). Appending \( \v \) to a basis of \( U \) gives a basis of \( W \) by @lem-append-independent, so \( \dim V - \dim W = k - 1 \). For \( c \in \nR \), the formula \( g(\u + t\v) = f(\u) + tc \) therefore defines a linear functional on \( W \) that extends \( f \).

For \( \u, \u' \in U \), linearity of \( f \), the hypothesis, and sublinearity of \( p \) give
\[
f(\u) + f(\u') = f(\u + \u') \le p(\u + \u') \le p(\u - \v) + p(\u' + \v) ,
\]
that is, \( f(\u) - p(\u - \v) \le p(\u' + \v) - f(\u') \). So every number in \( L = \{f(\u) - p(\u - \v) : \u \in U\} \) is at most every number in \( R = \{p(\u' + \v) - f(\u') : \u' \in U\} \). By **fact (A1) of Chapter 16's introduction**, the non-empty set \( L \), bounded above by any element of \( R \), has a least upper bound \( c \), and \( c \le r \) for every \( r \in R \). With this \( c \), we check \( g(\u + t\v) \le p(\u + t\v) \) in three cases.

- \( t = 0 \): this is the hypothesis \( f(\u) \le p(\u) \).
- \( t > 0 \): \( c \le p(\u/t + \v) - f(\u/t) \), the element of \( R \) at \( \u' = \u/t \). Multiply by \( t \) and use \( p(t\,\cdot) = t\,p(\cdot) \): \( tc \le p(\u + t\v) - f(\u) \).
- \( t = -s < 0 \): \( c \ge f(\u/s) - p(\u/s - \v) \), since this is an element of \( L \). Multiply by \( s \): \( sc \ge f(\u) - p(\u - s\v) \), that is, \( f(\u) - sc \le p(\u + t\v) \).

So \( g \le p \) on \( W \). By the induction hypothesis applied to \( W \) and \( g \), there is \( F \in V^{*} \) extending \( g \), hence \( f \), with \( F \le p \) on \( V \). This proves the theorem.
:::

**Beyond finite dimension.** The induction above stops after \( \dim V - \dim U \) steps. In an infinite-dimensional space there is no last step, and the one-step extension has to be combined with Zorn's lemma (@thm-zorn), exactly as Chapter 1 §08 combined "append one vector" with Zorn's lemma to prove @thm-every-space-has-basis. The resulting theorem, the Hahn–Banach theorem of functional analysis, is outside the scope of this book, and nothing here depends on it.

The special case that matters most is a norm.

::: {#cor-hahn-banach-norm}
[Norm-Preserving Extension]

Let \( V \) be a finite-dimensional real vector space with a norm \( \norm{\cdot} \), let \( U \) be a subspace, and let \( f \in U^{*} \) satisfy \( \lvert f(\u)\rvert \le \norm{\u} \) for every \( \u \in U \). Then there is \( F \in V^{*} \) extending \( f \) with \( \lvert F(\v)\rvert \le \norm{\v} \) for every \( \v \in V \).
:::

::: {.proof}
A norm is sublinear, so @thm-hahn-banach-finite with \( p = \norm{\cdot} \) gives \( F \) extending \( f \) with \( F(\v) \le \norm{\v} \) for all \( \v \). Applying this to \( -\v \) gives \( -F(\v) = F(-\v) \le \norm{-\v} = \norm{\v} \) by (N2). Hence \( \lvert F(\v)\rvert \le \norm{\v} \).
:::

In particular, for any \( \x \ne \0 \), taking \( U = \Span(\x) \) and \( f(t\x) = t\norm{\x} \) produces a functional \( F \) with \( F(\x) = \norm{\x} \) and \( \lvert F\rvert \le \norm{\cdot} \) everywhere: a linear functional that "sees" the full length of \( \x \) without ever exceeding the norm. §04 meets this functional again, as the vector at which a dual norm is attained.

::: {#exm-hahn-banach-interval}
[Many extensions]

On \( \nR^2 \) with \( \norm{\cdot}_\infty \), let \( U = \Span\bigl((1,1)\bigr) \) and \( f\bigl(s(1,1)\bigr) = s \). Find every \( F \) as in @cor-hahn-banach-norm, and compare with the interval produced by the proof of @thm-hahn-banach-finite for \( \v = \e_1 \).
:::

::: {.solution}
First, \( \lvert f(s(1,1))\rvert = \lvert s\rvert = \norm{s(1,1)}_\infty \), so the hypothesis holds. An extension has \( F(\e_1) = c \) for some \( c \), and then \( F(\e_2) = F\bigl((1,1)\bigr) - c = 1 - c \), so \( F(\x) = cx_1 + (1 - c)x_2 \).

If \( 0 \le c \le 1 \), then \( \lvert F(\x)\rvert \le c\lvert x_1\rvert + (1 - c)\lvert x_2\rvert \le \norm{\x}_\infty \). If \( c > 1 \), then \( \x = (1, -1) \) gives \( F(\x) = 2c - 1 > 1 = \norm{\x}_\infty \). If \( c < 0 \), then \( \x = (-1, 1) \) gives \( F(\x) = 1 - 2c > 1 \). So the extensions are exactly \( F(\x) = cx_1 + (1 - c)x_2 \) with \( c \in [0, 1] \): infinitely many.

In the proof, with \( p = \norm{\cdot}_\infty \), \( \u = s(1,1) \) and \( \v = \e_1 \), the elements of \( L \) are \( s - \max(\lvert s - 1\rvert, \lvert s\rvert) \), which is \( 0 \) for \( s \ge \tfrac12 \) and \( 2s - 1 < 0 \) for \( s < \tfrac12 \); so \( \sup L = 0 \). The elements of \( R \) are \( \max(\lvert s + 1\rvert, \lvert s\rvert) - s \), which is \( 1 \) for \( s \ge -\tfrac12 \) and \( -2s > 1 \) for \( s < -\tfrac12 \); so \( \inf R = 1 \). Every \( c \) between \( \sup L \) and \( \inf R \) works, and that is the interval \( [0, 1] \) found directly. The proof picked its left end.
:::

The corners of the square \( B_\infty \) are why the extension is not unique: \( U \) meets the unit sphere at the corner \( (1, 1) \), and every supporting line of the square at that corner gives an extension.

## Exercises

### A. Check your understanding

:::: {#exr-separation-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the characterization @eq-variational-inequality of the nearest point, and say what it becomes when \( C \) is a subspace.
2. Which two facts of Chapter 16's introduction does the existence of \( P_C(\x) \) use, and to which set are they applied?
3. Determine whether the following statement is correct, and justify your answer: every non-empty closed subset of \( \nR^2 \) has a unique point nearest to \( \0 \).
4. Determine whether the following statement is correct, and justify your answer: two disjoint non-empty closed convex subsets of \( \nR^2 \) can always be strictly separated.
:::
::::

::: {.solution}
(a) A point \( \p \in C \) is \( P_C(\x) \) exactly when \( \inner{\x - \p}{\y - \p} \le 0 \) for every \( \y \in C \) (@thm-nearest-point (b)). For a subspace \( U \) it becomes the equality \( \inner{\x - \p}{\u} = 0 \) for every \( \u \in U \), so \( P_C(\x) = P_U\x \) and @thm-best-approximation is recovered.

(b) The compactness of closed bounded sets (A3), through @cor-closed-bounded-compact, and the extreme value theorem (A4). They are applied to \( K = \{\y \in C : \norm{\x - \y} \le R\} \), the part of \( C \) within the distance \( R \) of \( \x \) attained at one chosen point of \( C \), and to the function \( \y \mapsto \norm{\x - \y} \).

(c) Incorrect. The unit circle is closed and non-empty, and every one of its points is at distance \( 1 \) from \( \0 \). Uniqueness needs convexity.

(d) Incorrect. The region \( A \) above the hyperbola \( x_1x_2 = 1 \) in the positive quadrant and its asymptote \( B \), the \( x_1 \)-axis, are disjoint, closed and convex, but the only hyperplane separating them is \( B \) itself (@exm-hyperbola-asymptote).
:::

### B. Practice

:::: {#exr-separation-b1}
[B1: Projection onto a half-plane]

In \( \nR^2 \) with the dot product, let \( C = \{\y : y_1 + y_2 \le 1\} \) and \( \x = (2, 3) \). Find \( P_C(\x) \) and \( d(\x, C) \), and verify @eq-variational-inequality.
::::

::: {.solution}
Here \( \a = (1, 1) \), \( c = 1 \), and \( \inner{\a}{\x} = 5 > 1 \). By @exm-nearest-point-examples (c), \( \lambda = (5 - 1)/2 = 2 \) and \( P_C(\x) = (2, 3) - 2(1, 1) = (0, 1) \). Check: \( 0 + 1 = 1 \), so \( \p = (0, 1) \in C \), and \( \x - \p = (2, 2) \), so \( \inner{\x - \p}{\y - \p} = 2y_1 + 2(y_2 - 1) = 2(y_1 + y_2 - 1) \le 0 \) for \( \y \in C \). By @thm-nearest-point (b) this is the nearest point, and \( d(\x, C) = \norm{(2, 2)} = 2\sqrt2 \).
:::

:::: {#exr-separation-b2}
[B2: Cutting off a point from a diamond]

Let \( C = B_1 = \{\y \in \nR^2 : \lvert y_1\rvert + \lvert y_2\rvert \le 1\} \), with the dot product, and \( \x = (2, 2) \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( P_C(\x) = (\tfrac12, \tfrac12) \).
2. Hence find the strictly separating hyperplane of @thm-separation-point, and check it directly.
3. Find every supporting hyperplane of \( C \) at \( (\tfrac12, \tfrac12) \).
:::
::::

::: {.solution}
(a) Let \( \p = (\tfrac12, \tfrac12) \), which lies in \( C \). Then \( \x - \p = (\tfrac32, \tfrac32) \) and, for \( \y \in C \),
\[
\inner{\x - \p}{\y - \p} = \tfrac32(y_1 + y_2 - 1) \le 0 ,
\]
because \( y_1 + y_2 \le \lvert y_1\rvert + \lvert y_2\rvert \le 1 \). By @thm-nearest-point (b), \( P_C(\x) = \p \).

(b) With \( \a = (\tfrac32, \tfrac32) \), we have \( \norm{\a}^2 = \tfrac92 \) and \( \inner{\a}{\x} = 6 \), so \( c = 6 - \tfrac94 = \tfrac{15}{4} \). The hyperplane \( \tfrac32(y_1 + y_2) = \tfrac{15}{4} \) is the line \( y_1 + y_2 = \tfrac52 \). Directly: on \( C \), \( y_1 + y_2 \le 1 < \tfrac52 \), while \( x_1 + x_2 = 4 > \tfrac52 \).

(c) Let \( \a \ne \0 \) satisfy \( \inner{\a}{\y} \le \inner{\a}{\p} = \tfrac12(a_1 + a_2) \) for all \( \y \in C \). Taking \( \y = \e_1 \) and \( \y = \e_2 \) gives \( a_1 \le \tfrac12(a_1 + a_2) \) and \( a_2 \le \tfrac12(a_1 + a_2) \), that is, \( a_1 \le a_2 \) and \( a_2 \le a_1 \); so \( a_1 = a_2 \). Taking \( \y = -\e_1 \) gives \( -a_1 \le a_1 \), so \( a_1 \ge 0 \), and \( a_1 \ne 0 \) since \( \a \ne \0 \). Conversely \( \a = (a, a) \) with \( a > 0 \) works, by the inequality in (a). So the only supporting hyperplane at \( \p \) is the line \( y_1 + y_2 = 1 \) through the edge containing \( \p \).
:::

:::: {#exr-separation-b3}
[B3: A unique extension]

On \( \nR^2 \) with \( \norm{\cdot}_1 \), let \( U = \Span\bigl((1, 2)\bigr) \) and \( f\bigl(t(1, 2)\bigr) = 3t \). Show that \( f \) satisfies the hypothesis of @cor-hahn-banach-norm, and find every extension \( F \) that the corollary allows.
::::

::: {.solution}
\( \lvert f(t(1,2))\rvert = 3\lvert t\rvert = \lvert t\rvert + 2\lvert t\rvert = \norm{t(1,2)}_1 \), so the hypothesis holds. Every \( F \in (\nR^2)^{*} \) is \( F(\x) = c_1x_1 + c_2x_2 \) (@thm-functionals-on-fn), and it extends \( f \) exactly when \( F\bigl((1,2)\bigr) = 3 \), that is, \( c_1 + 2c_2 = 3 \).

Next, \( \lvert F(\x)\rvert \le \norm{\x}_1 \) for all \( \x \) holds exactly when \( \lvert c_1\rvert \le 1 \) and \( \lvert c_2\rvert \le 1 \). Indeed, if both hold then \( \lvert c_1x_1 + c_2x_2\rvert \le \lvert x_1\rvert + \lvert x_2\rvert \); and if, say, \( \lvert c_1\rvert > 1 \), then \( \x = \e_1 \) gives \( \lvert F(\e_1)\rvert > 1 = \norm{\e_1}_1 \).

So we need \( c_1 = 3 - 2c_2 \) with \( \lvert 3 - 2c_2\rvert \le 1 \) and \( \lvert c_2\rvert \le 1 \). The first gives \( 1 \le c_2 \le 2 \), the second \( c_2 \le 1 \); hence \( c_2 = 1 \) and \( c_1 = 1 \). The only extension is \( F(\x) = x_1 + x_2 \).
:::

### C. Going deeper

:::: {#exr-separation-c1}
[C1: The projection does not stretch]

Let \( C \subseteq V \) be non-empty, closed and convex. Prove that \( \norm{P_C(\x) - P_C(\y)} \le \norm{\x - \y} \) for all \( \x, \y \in V \).

*Hint: write @eq-variational-inequality once at \( \x \), tested with the point \( P_C(\y) \), and once at \( \y \), tested with \( P_C(\x) \), and add.*
::::

::: {.solution}
Put \( \p = P_C(\x) \) and \( \q = P_C(\y) \). By @thm-nearest-point (b), applied at \( \x \) with the point \( \q \in C \) and at \( \y \) with the point \( \p \in C \),
\[
\inner{\x - \p}{\q - \p} \le 0 , \qquad \inner{\y - \q}{\p - \q} \le 0 .
\]
The second is \( \inner{\q - \y}{\q - \p} \le 0 \). Adding, \( \inner{(\x - \y) + (\q - \p)}{\q - \p} \le 0 \), that is,
\[
\norm{\q - \p}^2 \le \inner{\y - \x}{\q - \p} \le \norm{\y - \x}\,\norm{\q - \p}
\]
by @thm-cauchy-schwarz. If \( \q = \p \) there is nothing to prove; otherwise divide by \( \norm{\q - \p} > 0 \). This proves \( \norm{\p - \q} \le \norm{\x - \y} \).
:::

:::: {#exr-separation-c2}
[C2: Strict separation and distance]

Let \( C_1, C_2 \subseteq V \) be non-empty, closed and convex, and put \( \delta = \inf\{\norm{\y - \x} : \x \in C_1, \y \in C_2\} \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( C_1 \) and \( C_2 \) are strictly separated, then \( \delta > 0 \).
2. Prove that if \( \delta > 0 \), then \( C_1 \) and \( C_2 \) are strictly separated.
3. Hence deduce, without the computation of @exm-hyperbola-asymptote, that the sets \( A \) and \( B \) there are not strictly separated.
:::

*Hint for (b): replace the difference set \( D \) of @thm-separating-hyperplane by its closure.*
::::

::: {.solution}
(a) Let \( \a \ne \0 \), \( c \) and \( \varepsilon > 0 \) strictly separate the sets, with \( C_1 \) on the side \( \le c - \varepsilon \). For \( \x \in C_1 \) and \( \y \in C_2 \), @thm-cauchy-schwarz gives
\[
2\varepsilon \le \inner{\a}{\y} - \inner{\a}{\x} = \inner{\a}{\y - \x} \le \norm{\a}\,\norm{\y - \x} ,
\]
so \( \norm{\y - \x} \ge 2\varepsilon/\norm{\a} \). Hence \( \delta \ge 2\varepsilon/\norm{\a} > 0 \).

(b) Let \( D = \{\y - \x : \x \in C_1, \y \in C_2\} \), which is convex by the computation in the proof of @thm-separating-hyperplane. Every \( \d \in D \) has \( \norm{\d} \ge \delta \), and so does every point of \( \closure{D} \): if \( \d_k \to \d \) with \( \d_k \in D \), then \( \norm{\d} \ge \norm{\d_k} - \norm{\d_k - \d} \ge \delta - \norm{\d_k - \d} \) for every \( k \), and the right side tends to \( \delta \). So \( \0 \notin \closure{D} \), and \( \closure{D} \) is non-empty, closed and convex by @lem-closure-convex (a). By @thm-separation-point there is \( \b \ne \0 \) with \( \inner{\b}{\d} \le -\norm{\b}^2 \) on \( \closure{D} \supseteq D \). With \( \a = -\b \), this is \( \inner{\a}{\x} + \norm{\a}^2 \le \inner{\a}{\y} \) for all \( \x \in C_1 \), \( \y \in C_2 \), and the last paragraph of the proof of @thm-separating-hyperplane (a) turns it into strict separation with \( \varepsilon = \tfrac12\norm{\a}^2 \).

(c) The points \( (t, 1/t) \in A \) and \( (t, 0) \in B \) are at distance \( 1/t \), so \( \delta \le 1/t \) for every \( t > 0 \), and \( \delta = 0 \). By (a), \( A \) and \( B \) are not strictly separated.
:::
