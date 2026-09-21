# Flats, Independence and Coordinates

An affine space has no origin, so it has no subspaces in the sense of Chapter 1: a subspace must contain \( \0 \), and there is no \( \0 \). What it has instead are its **flats** — the lines, planes and hyperplanes that sit inside it. This section defines them, settles when two of them meet and how big the smallest flat containing both is, puts coordinates on an affine space using \( n + 1 \) points rather than \( n \) vectors, and shows that in \( \nA^n(F) \) the flats are exactly the solution sets of linear systems. The join formula has two cases, and the second one is where affine geometry parts company with linear algebra.

Throughout, \( \cA \) is an affine space over a field \( F \) with direction space \( V \) (@def-affine-space), and from the dimension formula onward \( \dim \cA = \dim V = n \) is finite, except where a statement says otherwise.

## Flats

A subset of \( \cA \) deserves to be called flat when it is an affine space in its own right, using the same difference map. By @def-affine-combination there is only one thing to require.

*A flat is a non-empty set of points closed under taking affine combinations.*

::: {#def-flat}
[Flat]

A subset \( A \subseteq \cA \) is a **flat**, or an **affine subspace** of \( \cA \), if it is **non-empty** and contains every affine combination of its own points: **whenever** \( k \ge 1 \), \( P_1, \dots, P_k \in A \) and \( t_1, \dots, t_k \in F \) satisfy \( t_1 + \dots + t_k = 1 \), the point \( \sum_{i=1}^{k}t_iP_i \) lies in \( A \).
:::

The requirement that \( A \) be non-empty is a convention, and it is the useful one: a flat is going to have a direction space and a dimension, and the empty set has neither. Intersections of flats may of course be empty, and we will say so each time.

::: {#prp-flat-is-coset}
[Flats Are the Cosets]

Let \( A \subseteq \cA \) be non-empty. Then \( A \) is a flat if and only if there are \( P \in \cA \) and a subspace \( U \) of \( V \) with \( A = P + U \coloneqq \{ P + \u : \u \in U \} \). In that case:

::: {.enumerate options="label=(\alph*)"}
1. \( U = \{ \overrightarrow{XY} : X, Y \in A \} \) is determined by \( A \) alone; it is written \( \vec{A} \) and called the **direction space** of \( A \).
2. \( A = Q + \vec{A} \) for **every** \( Q \in A \), and \( A \), with the difference map of \( \cA \) restricted to it, is an affine space with direction space \( \vec{A} \).
:::

The **dimension** of \( A \) is \( \dim A \coloneqq \dim \vec{A} \). A flat of dimension \( 0 \) is a single **point**, one of dimension \( 1 \) is a **line**, one of dimension \( 2 \) is a **plane**, and, when \( \dim\cA = n \) is finite, one of dimension \( n - 1 \) is a **hyperplane** of \( \cA \).
:::

::: {.idea}
One direction is a computation with origin \( P \). For the other, fix \( P \in A \) and let \( U \) be the set of displacements from \( P \) to points of \( A \); the three subspace axioms come from three affine combinations, with weight lists \( (1) \), \( (\lambda, 1 - \lambda) \) and \( (1, 1, -1) \).
:::

::: {.proof}
\( (\Leftarrow) \) Let \( A = P + U \) with \( U \) a subspace, and let \( P + \u_1, \dots, P + \u_k \in A \) with \( \sum_i t_i = 1 \). Computing the affine combination with origin \( P \) (@def-affine-combination),
\[
\sum_{i} t_i(P + \u_i) = P + \sum_i t_i\u_i \in P + U ,
\]
since \( U \) is closed under linear combinations. And \( A \ni P \) is non-empty.

\( (\Rightarrow) \) Let \( A \) be a flat, fix \( P \in A \) and put \( U = \{ \overrightarrow{PX} : X \in A \} \). Then \( \0 = \overrightarrow{PP} \in U \). If \( \u = \overrightarrow{PX} \in U \) and \( \lambda \in F \), the point \( \lambda X + (1 - \lambda)P \) lies in \( A \) and equals \( P + \lambda\u \) when computed with origin \( P \), so \( \lambda\u \in U \). If also \( \w = \overrightarrow{PY} \in U \), the point \( X + Y - P \) lies in \( A \) (weights \( 1 + 1 - 1 = 1 \)) and equals \( P + (\u + \w) \), so \( \u + \w \in U \). By @thm-subspace-test, \( U \) is a subspace, and \( A = P + U \) by construction.

(a) Let \( X, Y \in A \). Then \( \overrightarrow{XY} = \overrightarrow{XP} + \overrightarrow{PY} \in U \) by Chasles, since \( U \) is closed under negation and addition; so \( \{\overrightarrow{XY} : X, Y \in A\} \subseteq U \). Conversely each \( \u \in U \) is \( \overrightarrow{PX} \) for some \( X \in A \), and \( P \in A \). Hence the two sets are equal, and the right-hand side mentions only \( A \).

(b) Let \( Q \in A \). For \( X \in A \) we have \( \overrightarrow{QX} \in \vec{A} \) by (a), so \( A \subseteq Q + \vec{A} \); and for \( \u \in \vec{A} \), writing \( \u = \overrightarrow{XY} \) with \( X, Y \in A \), the point \( Q + \u \) is the affine combination \( Q + Y - X \) of points of \( A \), hence lies in \( A \). So \( A = Q + \vec{A} \). Finally the restricted difference map takes values in \( \vec{A} \) by (a), Chasles is inherited, and for fixed \( P \in A \) the map \( X \mapsto \overrightarrow{PX} \) is a bijection \( A \to \vec A \), being the restriction of the bijection of (AS2) to \( A = P + \vec A \). So (AS1) and (AS2) hold and \( A \) is an affine space with direction space \( \vec A \).
:::

Over \( \nR \), with \( \cA = V \), a flat is exactly Chapter 17's affine subspace of \( V \) (@def-affine-hull (b)), and the two dimensions agree: Chapter 17 also reads the subspace off the coset as the set of differences. Chapter 4's **affine hyperplane** \( \p + H \) (the paragraph before @prp-affine-subspace-intersection) is the case \( \dim A = n - 1 \) in \( \nA^n(F) \). A one-point set \( \{P\} = P + \{\0\} \) is a flat, and \( \cA = P + V \) is a flat: the two degenerate cases.

**A non-example, by minimal change.** A line is a flat; the union of two lines is not. Let \( X = \{ (x, y) \in \nA^2 : xy = 0 \} \), the union of the two coordinate axes. It is non-empty, and it contains every affine combination of points taken from one axis, each axis being a flat. But @def-flat asks for all of them: the points \( P = (1, 0) \) and \( Q = (0, 1) \) lie in \( X \), the weights of \( \tfrac12P + \tfrac12Q \) add up to \( 1 \), and \( \tfrac12P + \tfrac12Q = \bigl(\tfrac12, \tfrac12\bigr) \) has \( xy = \tfrac14 \ne 0 \). So the closure clause fails for one pair of points, and \( X \) is not a coset of a subspace, although it is a union of two of them.

::: {#prp-flat-intersection}
[Intersections of Flats]

Let \( (A_i)_{i \in I} \) be a non-empty family of flats of \( \cA \) and put \( A = \bigcap_{i \in I}A_i \). If \( A \ne \emptyset \), then \( A \) is a flat and \( \vec{A} = \bigcap_{i \in I}\vec{A_i} \).
:::

::: {.proof}
Suppose \( A \ne \emptyset \) and fix \( P \in A \). If \( P_1, \dots, P_k \in A \) and \( \sum_j t_j = 1 \), then the point \( \sum_j t_jP_j \) lies in each \( A_i \), because each \( A_i \) is a flat containing all the \( P_j \); so it lies in \( A \). Hence \( A \) is a flat. By @prp-flat-is-coset (b), \( A_i = P + \vec{A_i} \) for each \( i \) and \( A = P + \vec{A} \), so
\[
\vec{A} = \{ \overrightarrow{PX} : X \in A \} = \bigcap_{i \in I} \{ \overrightarrow{PX} : X \in A_i \} = \bigcap_{i \in I}\vec{A_i} ,
\]
where the middle equality holds because \( X \mapsto \overrightarrow{PX} \) is injective (AS2).
:::

Since \( \cA \) itself is a flat containing every subset, the following is well defined.

::: {#def-affine-join}
[Join of Flats]

Let \( A, B \) be flats of \( \cA \). Their **join** \( A \vee B \) is the intersection of all flats of \( \cA \) containing \( A \cup B \).
:::

The intersection contains \( A \), so it is non-empty, and it is a flat by @prp-flat-intersection: \( A \vee B \) is the **smallest** flat containing both. A single point \( P \) is a flat, and we write \( P \vee Q \), \( A \vee P \) for joins in which a one-point flat \( \{P\} \) appears. This is the affine analogue of \( U + W \), and Chapter 17's affine hull is the same construction over \( \nR \) (@prp-affine-hull-coset).

Parallelism is what an affine space has and a vector space does not notice.

::: {#def-parallel-flats}
[Parallel Flats]

Two flats \( A, B \) of \( \cA \) are **parallel**, written \( A \parallel B \), if \( \vec{A} = \vec{B} \).
:::

::: {#prp-parallel-equivalence}
[Parallelism]

Parallelism is an equivalence relation on the set of flats of \( \cA \). Two parallel flats are either equal or disjoint, and each equivalence class consists of the flats \( P + U \), \( P \in \cA \), for one fixed subspace \( U \).
:::

::: {.proof}
Equality of direction spaces is an equivalence relation, so \( \parallel \) is one. Let \( A \parallel B \) with common direction \( U \), and suppose \( X \in A \cap B \). Then \( A = X + U = B \) by @prp-flat-is-coset (b). So \( A \) and \( B \) are equal or disjoint. Finally, the flats with direction space \( U \) are exactly the sets \( P + U \) with \( P \in \cA \), again by @prp-flat-is-coset.
:::

Parallel flats have the same dimension. Some authors also call a line parallel to a plane containing its direction; we do not, and we say "\( \vec{A} \subseteq \vec{B} \)" when we mean that.

## When two flats meet, and how big their join is

Here is the central computation of the section. Two subspaces of a vector space always meet, in \( \0 \) at least. Two flats need not, and the dimension formula splits accordingly.

::: {#thm-flat-intersection-and-join}
[Intersection and Join of Two Flats]

Let \( A, B \) be flats of \( \cA \), and choose \( P \in A \) and \( Q \in B \). Parts (a) and (b) need no hypothesis on \( \dim\cA \).

::: {.enumerate options="label=(\alph*)"}
1. \( A \vee B = P + \bigl( \vec{A} + \vec{B} + \Span(\overrightarrow{PQ}) \bigr) \).
2. \( A \cap B \ne \emptyset \) if and only if \( \overrightarrow{PQ} \in \vec{A} + \vec{B} \); and then \( A \cap B \) is a flat whose direction space is \( \vec{A} \cap \vec{B} \).
3. Let \( \dim\cA = n \) be finite. If \( A \cap B \ne \emptyset \), then
\[
\dim(A \vee B) = \dim A + \dim B - \dim(A \cap B) .
\]
If \( A \cap B = \emptyset \), then
\[
\dim(A \vee B) = \dim A + \dim B - \dim(\vec{A} \cap \vec{B}) + 1 .
\]
4. Let \( \dim\cA = n \) be finite. If \( A \cap B = \emptyset \), there is a hyperplane \( H \) of \( V \) with \( A \subseteq P + H \) and \( B \subseteq Q + H \), and the two flats \( P + H \), \( Q + H \) are parallel, distinct and disjoint.
:::
:::

::: {.idea}
Everything is read off from one subspace, \( W = \vec{A} + \vec{B} + \Span(\overrightarrow{PQ}) \). The three summands are forced: the join must contain the directions of \( A \) and of \( B \), and it must contain a way of getting from \( A \) to \( B \). Whether the third summand is already inside the first two is exactly whether \( A \) and \( B \) meet — and that one extra dimension, present precisely when they miss each other, is the whole difference between (c)'s two cases.
:::

::: {.proof}
Put \( W = \vec{A} + \vec{B} + \Span(\overrightarrow{PQ}) \), a subspace of \( V \), and \( C = P + W \), a flat by @prp-flat-is-coset.

(a) First, \( A \cup B \subseteq C \). Indeed \( A = P + \vec{A} \subseteq P + W \). And each point of \( B \) is \( Q + \b \) with \( \b \in \vec{B} \), which equals \( P + (\overrightarrow{PQ} + \b) \) by @lem-chasles-consequences (b), and \( \overrightarrow{PQ} + \b \in W \). So \( C \) is one of the flats being intersected in @def-affine-join, whence \( A \vee B \subseteq C \).

Conversely, \( A \vee B \) is a flat containing \( P \), so \( A \vee B = P + U \) by @prp-flat-is-coset (b), where \( U \) is the direction space of \( A \vee B \). Since \( A \subseteq A \vee B \) and \( P \in A \), part (a) of that proposition gives \( \vec{A} \subseteq U \). Since \( Q \in A \vee B \), also \( \overrightarrow{PQ} \in U \). And for \( \b \in \vec{B} \) the point \( Q + \b \) lies in \( B \subseteq A \vee B \), so \( \overrightarrow{PQ} + \b = \overrightarrow{P\,(Q + \b)} \in U \), and therefore \( \b \in U \). Hence \( W \subseteq U \), that is, \( C \subseteq A \vee B \). The two inclusions give (a).

(b) \( (\Leftarrow) \) Suppose \( \overrightarrow{PQ} = \a + \b \) with \( \a \in \vec{A} \), \( \b \in \vec{B} \). Put \( X = P + \a \), a point of \( A \). Then
\[
\overrightarrow{QX} = \overrightarrow{QP} + \overrightarrow{PX} = -(\a + \b) + \a = -\b \in \vec{B} ,
\]
so \( X \in Q + \vec{B} = B \). Hence \( X \in A \cap B \).

\( (\Rightarrow) \) If \( X \in A \cap B \), then \( \overrightarrow{PX} \in \vec{A} \) and \( \overrightarrow{XQ} \in \vec{B} \) by @prp-flat-is-coset (a), so \( \overrightarrow{PQ} = \overrightarrow{PX} + \overrightarrow{XQ} \in \vec{A} + \vec{B} \). The last clause is @prp-flat-intersection applied to the two flats \( A \) and \( B \).

(c) *Case 1: \( A \cap B \ne \emptyset \).* By (b), \( \overrightarrow{PQ} \in \vec{A} + \vec{B} \), so \( W = \vec{A} + \vec{B} \). By (a) and @thm-dimension-formula-subspace-dim,
\[
\begin{aligned}
\dim(A \vee B) &= \dim(\vec{A} + \vec{B}) \\
&= \dim\vec{A} + \dim\vec{B} - \dim(\vec{A} \cap \vec{B}) ,
\end{aligned}
\]
and \( \dim(\vec A \cap \vec B) = \dim(A \cap B) \) by (b), which is the first formula.

*Case 2: \( A \cap B = \emptyset \).* By (b), \( \overrightarrow{PQ} \notin \vec{A} + \vec{B} \); in particular \( \overrightarrow{PQ} \ne \0 \). Then
\[
\Span(\overrightarrow{PQ}) \cap (\vec{A} + \vec{B}) = \{\0\} ,
\]
since a non-zero \( \lambda\overrightarrow{PQ} \) lying in \( \vec{A} + \vec{B} \) would give \( \overrightarrow{PQ} = \lambda^{-1}(\lambda\overrightarrow{PQ}) \in \vec{A} + \vec{B} \), \( \lambda \) being non-zero and hence invertible. So @thm-dimension-formula-subspace-dim applied to the two subspaces \( \vec A + \vec B \) and \( \Span(\overrightarrow{PQ}) \) gives \( \dim W = \dim(\vec{A} + \vec{B}) + 1 \), and one more application, as in Case 1, gives the second formula.

(d) Put \( U = \vec{A} + \vec{B} \) and \( r = \dim U \). By (b), \( \overrightarrow{PQ} \notin U \), so appending \( \overrightarrow{PQ} \) to a basis \( (\u_1, \dots, \u_r) \) of \( U \) leaves an independent list (@lem-append-independent). Extend it to a basis
\[
(\u_1, \dots, \u_r,\ \overrightarrow{PQ},\ \w_1, \dots, \w_{n - r - 1})
\]
of \( V \) by @thm-basis-extension, and let \( H = \Span(\u_1, \dots, \u_r, \w_1, \dots, \w_{n-r-1}) \). Then \( \dim H = n - 1 \), so \( \dim(V/H) = 1 \) by @thm-dimension-quotient and \( H \) is a hyperplane (@def-hyperplane). Now \( \vec{A} \subseteq U \subseteq H \) gives \( A = P + \vec{A} \subseteq P + H \), and likewise \( B \subseteq Q + H \). The flats \( P + H \) and \( Q + H \) are parallel by @def-parallel-flats. They are distinct: if they were equal, then \( Q \in P + H \) would give \( \overrightarrow{PQ} \in H \), contradicting the independence of the displayed basis. Being parallel and distinct, they are disjoint by @prp-parallel-equivalence. This proves the theorem.
:::

The two formulas in (c) are best read side by side. When the flats meet, the count is the subspace count of @thm-dimension-formula-subspace-dim, with \( A \cap B \) in the role of \( \vec A \cap \vec B \). When they miss, the correction term is taken among the **directions**, where the flats always do meet, and a \( +1 \) is paid for the displacement that carries one flat to the other.

Part (b) is what the two pictures below show. On the left the displacement \( \overrightarrow{PQ} \) splits as a step inside \( \vec{A} \) followed by a step inside \( \vec{B} \), and the flats meet; on the right it does not split, so it contributes a direction of its own to the join.

\begin{center}
\begin{tikzpicture}[scale=0.9]
  \draw[thick] (-0.5,0) -- (3.4,0) node[right] {$A$};
  \draw[thick] (0.1,-0.9) -- (2.7,1.7) node[above right] {$B$};
  \draw[->, thick] (0,0) -- (0.95,0) node[midway, below=7pt] {in $\vec{A}$};
  \draw[->, thick] (1,0) -- (1.95,0.95) node[midway, right=2pt] {in $\vec{B}$};
  \draw[->, dashed] (0.06,0.1) -- (1.94,1.04) node[midway, above left] {$\overrightarrow{PQ}$};
  \fill (0,0) circle (1.6pt) node[left=2pt] {$P$};
  \fill (2,1) circle (1.6pt) node[above right] {$Q$};
  \fill (1,0) circle (1.4pt) node[below right=0pt] {$X$};
  \node at (1.5,-1.7) {$A \cap B \ne \emptyset$};
  \begin{scope}[xshift=6cm]
    \draw[thick] (-0.5,0) -- (3.4,0) node[right] {$A$};
    \draw[thick] (-0.5,1.4) -- (3.4,1.4) node[right] {$B$};
    \draw[->, dashed] (0,0) -- (1.2,1.4) node[midway, left] {$\overrightarrow{PQ}$};
    \fill (0,0) circle (1.6pt) node[below left] {$P$};
    \fill (1.2,1.4) circle (1.6pt) node[above] {$Q$};
    \node at (1.5,-1.7) {$A \cap B = \emptyset$};
  \end{scope}
\end{tikzpicture}
\end{center}

::: {#exm-skew-lines-join}
[Two lines in space, twice]

In \( \nA^3 \) let
\[
\begin{aligned}
A &= (1, 0, 0) + \Span\bigl((1, 1, 0)\bigr) , \\
B &= (0, 0, 1) + \Span\bigl((1, -1, 0)\bigr) , \\
B' &= (0, 0, 1) + \Span\bigl((1, 1, 0)\bigr) .
\end{aligned}
\]
Decide in each case whether the lines meet, and compute \( \dim(A \vee B) \) and \( \dim(A \vee B') \).
:::

::: {.solution}
Here \( P = (1,0,0) \), \( Q = (0,0,1) \) and \( \overrightarrow{PQ} = (-1, 0, 1) \).

**\( A \) and \( B \).** The directions \( (1,1,0) \) and \( (1,-1,0) \) are independent, and \( \vec{A} + \vec{B} \) is the plane of vectors with third coordinate \( 0 \). Since \( \overrightarrow{PQ} = (-1,0,1) \) has third coordinate \( 1 \), it is not in \( \vec A + \vec B \), so \( A \cap B = \emptyset \) by @thm-flat-intersection-and-join (b): the lines are **skew**, that is, disjoint and not parallel. (Directly: \( (1 + s, s, 0) = (t, -t, 1) \) forces \( 0 = 1 \).) Also \( \vec A \cap \vec B = \{\0\} \), the two directions being independent. The second formula of (c) gives
\[
\dim(A \vee B) = 1 + 1 - 0 + 1 = 3 ,
\]
so \( A \vee B = \nA^3 \): two skew lines span the whole space.

**\( A \) and \( B' \).** Now \( \vec{A} = \vec{B'} \), so the lines are parallel, and they are distinct because \( \overrightarrow{PQ} = (-1,0,1) \notin \vec{A} \); hence they are disjoint (@prp-parallel-equivalence). Here \( \vec A \cap \vec{B'} = \vec A \) has dimension \( 1 \), so
\[
\dim(A \vee B') = 1 + 1 - 1 + 1 = 2 ,
\]
and \( A \vee B' \) is the plane \( (1,0,0) + \Span\bigl((1,1,0), (-1,0,1)\bigr) \), by part (a).
:::

::: {.warning}
**There is no convention for \( \dim\emptyset \) that makes one formula do both cases.** It is tempting to set \( \dim\emptyset = -1 \) and keep writing \( \dim(A \vee B) = \dim A + \dim B - \dim(A \cap B) \). For the skew lines of @exm-skew-lines-join that gives \( 1 + 1 - (-1) = 3 \), which is right; for the parallel lines \( A \) and \( B' \) it gives \( 3 \) as well, and the correct answer is \( 2 \). The two disjoint cases differ in \( \dim(\vec A \cap \vec B) \), which the empty intersection cannot record. Use the second formula of @thm-flat-intersection-and-join (c), and always check first whether the flats meet.
:::

::: {.check}
In \( \nA^4 \), let \( A \) and \( B \) be planes (flats of dimension \( 2 \)) with \( \vec{A} \cap \vec{B} = \{\0\} \). Must they meet?
:::

::: {.solution}
Yes. By @thm-dimension-formula-subspace-dim, \( \dim(\vec A + \vec B) = 2 + 2 - 0 = 4 = \dim V \), so \( \vec A + \vec B = V \) by @thm-dim-impl-eq. Hence \( \overrightarrow{PQ} \in \vec A + \vec B \) for any \( P \in A \), \( Q \in B \), and @thm-flat-intersection-and-join (b) gives \( A \cap B \ne \emptyset \). (The dimension formula agrees: the disjoint case would predict \( 2 + 2 - 0 + 1 = 5 > 4 \), which is impossible.) Their intersection is then a single point, since its direction space is \( \vec A \cap \vec B = \{\0\} \).
:::

## Affine frames and barycentric coordinates

To put coordinates on an \( n \)-dimensional vector space we choose \( n \) vectors. To put coordinates on an \( n \)-dimensional affine space we must also say where the origin is, so we choose \( n + 1 \) points — and if we refuse to single out one of them, the coordinates come out symmetric in all \( n + 1 \). That symmetry is what makes the centroid computation below one line.

Chapter 17 §02 defined a list \( (\x_0, \dots, \x_m) \) in a real vector space to be **affinely independent** when the only scalars with \( \sum_i\lambda_i = 0 \) and \( \sum_i \lambda_i\x_i = \0 \) are all zero (@def-affine-independence). By @def-affine-combination (b) the expression \( \sum_i\lambda_iP_i \) is a well-defined vector for points of an affine space whenever \( \sum_i\lambda_i = 0 \), so the same words apply here verbatim. The next lemma is @lem-affine-dependence (a) in that setting; its proof uses nothing about \( \nR \), so we give it again over an arbitrary field.

::: {#lem-affine-independence-differences}
[Affine Independence by Differences]

Let \( P_0, P_1, \dots, P_m \in \cA \). The following are equivalent.

::: {.enumerate options="label=(\alph*)"}
1. The only \( \lambda_0, \dots, \lambda_m \in F \) with \( \sum_{i=0}^m\lambda_i = 0 \) and \( \sum_{i=0}^m \lambda_iP_i = \0 \) are \( \lambda_0 = \dots = \lambda_m = 0 \).
2. The list \( (\overrightarrow{P_0P_1}, \dots, \overrightarrow{P_0P_m}) \) is linearly independent in \( V \).
:::

A list satisfying these is called **affinely independent**. Condition (a) does not mention \( P_0 \) specially, so (b) holds with any \( P_j \) in place of \( P_0 \) as soon as it holds for one.
:::

::: {.proof}
By @def-affine-combination (b) computed with origin \( P_0 \), and since \( \overrightarrow{P_0P_0} = \0 \),
\[
\sum_{i=0}^{m}\lambda_iP_i = \sum_{i=0}^{m}\lambda_i\overrightarrow{P_0P_i} = \sum_{i=1}^{m}\lambda_i\overrightarrow{P_0P_i} .
\]
Given \( \lambda_1, \dots, \lambda_m \), the condition \( \sum_{i=0}^m\lambda_i = 0 \) holds for exactly one \( \lambda_0 \), namely \( \lambda_0 = -\sum_{i \ge 1}\lambda_i \); and \( (\lambda_0, \dots, \lambda_m) \) is the zero list exactly when \( (\lambda_1, \dots, \lambda_m) \) is. So the relations forbidden by (a) correspond, one for one, to the non-trivial linear relations among \( \overrightarrow{P_0P_1}, \dots, \overrightarrow{P_0P_m} \), and (a) holds if and only if there are none, which is (b).
:::

Over \( \nR \) with \( \cA = V \) this is @lem-affine-dependence (a), and Chapter 17's warning applies unchanged: affine independence is **not** linear independence. The list \( (\0, \e_1, \e_2) \) in \( \nR^2 \) is linearly dependent and affinely independent, which is why the count below is \( n + 1 \) and not \( n \).

::: {#def-affine-frame}
[Affine Frame]

Let \( \dim \cA = n \). An **affine frame** of \( \cA \) is a list \( (P_0, P_1, \dots, P_n) \) of \( n + 1 \) affinely independent points of \( \cA \).
:::

By @lem-affine-independence-differences the list \( (\overrightarrow{P_0P_1}, \dots, \overrightarrow{P_0P_n}) \) is then independent with \( n = \dim V \) entries, hence a basis of \( V \) (@thm-right-size-basis); conversely, if it is a basis, the frame condition holds. So an affine frame is "a point together with a basis", written symmetrically. In \( \nA^n(F) \) the **standard frame** is \( (\0, \e_1, \dots, \e_n) \).

::: {#thm-barycentric-coordinates}
[Barycentric Coordinates]

Let \( \dim \cA = n \) and let \( (P_0, \dots, P_n) \) be an affine frame of \( \cA \). For every \( X \in \cA \) there are **unique** scalars \( t_0, \dots, t_n \in F \) with
\[
t_0 + t_1 + \dots + t_n = 1 \qquad\text{and}\qquad X = \sum_{i=0}^{n} t_iP_i .
\]
They are called the **barycentric coordinates** of \( X \) with respect to the frame.
:::

::: {.idea}
Existence is the basis expansion of \( \overrightarrow{P_0X} \), with \( t_0 \) invented to make the weights add up to \( 1 \). Uniqueness is affine independence: the difference of two weight lists is an affine dependence.
:::

::: {.proof}
*Existence.* The list \( (\overrightarrow{P_0P_1}, \dots, \overrightarrow{P_0P_n}) \) is a basis of \( V \), so there are unique \( t_1, \dots, t_n \in F \) with \( \overrightarrow{P_0X} = \sum_{i=1}^{n}t_i\overrightarrow{P_0P_i} \) (@thm-unique-representation). Put \( t_0 = 1 - (t_1 + \dots + t_n) \), so that \( \sum_{i=0}^n t_i = 1 \). Computing the affine combination with origin \( P_0 \),
\[
\sum_{i=0}^{n}t_iP_i = P_0 + \sum_{i=0}^{n}t_i\overrightarrow{P_0P_i} = P_0 + \overrightarrow{P_0X} = X .
\]

*Uniqueness.* Suppose \( \sum_i t_iP_i = X = \sum_i t_i'P_i \) with both weight lists summing to \( 1 \), and put \( \lambda_i = t_i - t_i' \). Then \( \sum_i\lambda_i = 0 \), so \( \sum_i\lambda_iP_i \) is the vector \( \sum_i \lambda_i\overrightarrow{P_0P_i} \) of @def-affine-combination (b), and computing both combinations with origin \( P_0 \) gives
\[
\sum_i \lambda_i\overrightarrow{P_0P_i} = \overrightarrow{P_0X} - \overrightarrow{P_0X} = \0 .
\]
By @lem-affine-independence-differences (a), every \( \lambda_i = 0 \). This proves the theorem.
:::

Barycentric coordinates come as a **list**, not as separate numbers: they are pinned down only by the requirement that they add up to \( 1 \), so no one of them means anything on its own. Their virtue is that the frame's points are treated alike: \( P_j \) has coordinates \( (0, \dots, 1, \dots, 0) \) with the \( 1 \) in slot \( j \), for every \( j \).

::: {#exm-barycentric-triangle}
[Reading a triangle]

In \( \nA^2 \) take the frame \( P_0 = (0,0) \), \( P_1 = (4, 0) \), \( P_2 = (0, 3) \).

::: {.enumerate options="label=(\alph*)"}
1. Check that it is a frame, and find the barycentric coordinates (@thm-barycentric-coordinates) of \( X = (1, 1) \).
2. Find the point with barycentric coordinates \( (\tfrac12, \tfrac14, \tfrac14) \).
3. Describe the line \( P_1 \vee P_2 \) in barycentric coordinates.
:::
:::

::: {.solution}
(a) \( \overrightarrow{P_0P_1} = (4, 0) \) and \( \overrightarrow{P_0P_2} = (0, 3) \) are independent, so by @lem-affine-independence-differences the list is affinely independent, and three points in a plane make a frame. For \( X = (1,1) \): from \( (1,1) = t_1(4,0) + t_2(0,3) \) we get \( t_1 = \tfrac14 \) and \( t_2 = \tfrac13 \), so \( t_0 = 1 - \tfrac14 - \tfrac13 = \tfrac{5}{12} \). The coordinates are \( \bigl(\tfrac{5}{12}, \tfrac14, \tfrac13\bigr) \). **Check:** \( \tfrac{5}{12}(0,0) + \tfrac14(4,0) + \tfrac13(0,3) = (1, 1) \), and \( \tfrac{5}{12} + \tfrac{3}{12} + \tfrac{4}{12} = 1 \).

(b) \( \tfrac12(0,0) + \tfrac14(4,0) + \tfrac14(0,3) = \bigl(1, \tfrac34\bigr) \).

(c) The join of the two distinct points \( P_1, P_2 \) is \( P_1 + \Span(\overrightarrow{P_1P_2}) \) by @thm-flat-intersection-and-join (a), a line. Its points are the affine combinations \( (1-t)P_1 + tP_2 \), whose barycentric coordinates are \( (0, 1-t, t) \); conversely a point with \( t_0 = 0 \) is such a combination. So \( P_1 \vee P_2 = \{ t_0 = 0 \} \). The point \( X \) of (a) has \( t_0 = \tfrac{5}{12} \ne 0 \) and so is not on it.
:::

The next result is the advertisement for the whole apparatus: a classical theorem of plane geometry, proved in one line of arithmetic with weights.

::: {#prp-medians-meet-at-centroid}
[The Medians Meet at the Centroid]

Let \( F \) be a field in which \( 2 \ne 0 \) and \( 3 \ne 0 \), let \( \cA \) be an affine space over \( F \), and let \( (P_1, P_2, P_3) \) be an affinely independent list in \( \cA \). Put
\[
M_1 = \tfrac12 P_2 + \tfrac12 P_3, \qquad M_2 = \tfrac12 P_1 + \tfrac12 P_3, \qquad M_3 = \tfrac12 P_1 + \tfrac12 P_2 ,
\]
the **midpoints** of the sides, and let \( m_i = P_i \vee M_i \) be the **medians**. Then \( m_1, m_2, m_3 \) are lines meeting in exactly one point, the **centroid**
\[
G = \tfrac13 P_1 + \tfrac13 P_2 + \tfrac13 P_3 ,
\]
and \( \overrightarrow{P_iG} = 2\,\overrightarrow{GM_i} \) for each \( i \).
:::

\begin{center}
\begin{tikzpicture}[scale=1.15]
  \coordinate (P1) at (0,0);
  \coordinate (P2) at (4,0);
  \coordinate (P3) at (1.2,2.6);
  \coordinate (M1) at (2.6,1.3);
  \coordinate (M2) at (0.6,1.3);
  \coordinate (M3) at (2,0);
  \coordinate (G)  at (1.7333,0.8667);
  \draw[thick] (P1) -- (P2) -- (P3) -- cycle;
  \draw[dashed] (P1) -- (M1);
  \draw[dashed] (P2) -- (M2);
  \draw[dashed] (P3) -- (M3);
  \fill (P1) circle (1.6pt) node[below left] {$P_1$};
  \fill (P2) circle (1.6pt) node[below right] {$P_2$};
  \fill (P3) circle (1.6pt) node[above] {$P_3$};
  \fill (M1) circle (1.4pt) node[right] {$M_1$};
  \fill (M2) circle (1.4pt) node[left] {$M_2$};
  \fill (M3) circle (1.4pt) node[below] {$M_3$};
  \fill (G) circle (1.8pt) node[above right] {$G$};
\end{tikzpicture}
\end{center}

::: {.idea}
Work in the plane \( \pi = (P_1 \vee P_2) \vee P_3 \), where \( (P_1, P_2, P_3) \) is an affine frame, and give every point its barycentric coordinates. A median is then the set of coordinate triples of one shape, and the three shapes have exactly one triple in common.
:::

::: {.proof}
The three points are affinely independent, so \( (\overrightarrow{P_1P_2}, \overrightarrow{P_1P_3}) \) is independent by @lem-affine-independence-differences and, by @thm-flat-intersection-and-join (a) applied twice, \( \pi \coloneqq (P_1 \vee P_2) \vee P_3 = P_1 + \Span(\overrightarrow{P_1P_2}, \overrightarrow{P_1P_3}) \) is a plane in which \( (P_1, P_2, P_3) \) is an affine frame. All the points named lie in \( \pi \), being affine combinations of \( P_1, P_2, P_3 \), so we may use the barycentric coordinates of @thm-barycentric-coordinates throughout; the weights \( \tfrac12 \) and \( \tfrac13 \) exist because \( 2 \) and \( 3 \) are non-zero, hence invertible, in \( F \).

*Each \( m_i \) is a line, and \( G \) lies on it.* Take \( i = 1 \). In coordinates \( P_1 = (1,0,0) \) and \( M_1 = (0, \tfrac12, \tfrac12) \), so \( P_1 \ne M_1 \) by the uniqueness in @thm-barycentric-coordinates, and \( m_1 = P_1 \vee M_1 = P_1 + \Span(\overrightarrow{P_1M_1}) \) by @thm-flat-intersection-and-join (a), a flat of dimension \( 1 \) because \( \overrightarrow{P_1M_1} \ne \0 \). Its points are the affine combinations \( (1-s)P_1 + sM_1 \), \( s \in F \), with coordinates
\[
\bigl( 1 - s,\ \tfrac{s}{2},\ \tfrac{s}{2} \bigr) .
\]
At \( s = \tfrac23 \) this is \( \bigl(\tfrac13, \tfrac13, \tfrac13\bigr) \), the coordinate triple of \( G \). So \( G \in m_1 \), and by the same computation with the indices permuted, \( G \in m_2 \) and \( G \in m_3 \).

*No other common point.* A point of \( m_1 \cap m_2 \) has coordinates \( (1 - s, \tfrac{s}{2}, \tfrac{s}{2}) \) and \( (\tfrac{s'}{2}, 1 - s', \tfrac{s'}{2}) \) for some \( s, s' \in F \). Uniqueness in @thm-barycentric-coordinates makes the two triples equal entry by entry. The third entries give \( s = s' \), and then the first two give \( 1 - s = \tfrac{s}{2} \), that is, \( \tfrac32 s = 1 \) and \( s = \tfrac23 \). So \( m_1 \cap m_2 = \{G\} \), and a fortiori \( m_1 \cap m_2 \cap m_3 = \{G\} \).

*The ratio.* With origin \( P_1 \) we have \( \overrightarrow{P_1M_1} = \tfrac12\overrightarrow{P_1P_2} + \tfrac12\overrightarrow{P_1P_3} \) and \( \overrightarrow{P_1G} = \tfrac13\overrightarrow{P_1P_2} + \tfrac13\overrightarrow{P_1P_3} \), so \( \overrightarrow{P_1G} = \tfrac23\overrightarrow{P_1M_1} \) and \( \overrightarrow{GM_1} = \overrightarrow{P_1M_1} - \overrightarrow{P_1G} = \tfrac13\overrightarrow{P_1M_1} \). Hence \( \overrightarrow{P_1G} = 2\overrightarrow{GM_1} \), and likewise for \( i = 2, 3 \). This proves the proposition.
:::

::: {.remark}
The hypotheses on the field are not decoration. Over \( \nF_2 \) there are no midpoints, because \( \tfrac12 \) does not exist; over \( \nF_3 \) there are midpoints but no centroid, because \( \tfrac13 \) does not exist — and indeed in \( \nA^2(\nF_3) \) the three medians of an affinely independent triple are parallel and pairwise disjoint, as Exercise C3 below computes.
:::

## An affine map is fixed by a frame

Barycentric coordinates make the next theorem immediate, and it is the affine counterpart of "a linear map is determined by its values on a basis".

::: {#thm-affine-map-determined-by-frame}
[An Affine Map Is Determined by a Frame]

Let \( \cA \) have dimension \( n \) with affine frame \( (P_0, \dots, P_n) \), let \( \cB \) be an affine space over the same field with direction space \( W \), and let \( Q_0, \dots, Q_n \in \cB \) be **any** points. Then there is exactly one affine map \( f \colon \cA \to \cB \) with \( f(P_i) = Q_i \) for \( i = 0, \dots, n \). Moreover \( f \) carries the barycentric coordinates of @thm-barycentric-coordinates across:
\[
f\Bigl( \sum_{i=0}^{n}t_iP_i \Bigr) = \sum_{i=0}^{n}t_iQ_i \qquad \Bigl( \sum_i t_i = 1 \Bigr) .
\]
:::

::: {.proof}
*Existence.* The list \( (\overrightarrow{P_0P_1}, \dots, \overrightarrow{P_0P_n}) \) is a basis of \( V \), so by @thm-linear-map-from-any-basis there is a linear \( T \colon V \to W \) with \( T(\overrightarrow{P_0P_i}) = \overrightarrow{Q_0Q_i} \) for \( i = 1, \dots, n \). Define \( f(X) = Q_0 + T(\overrightarrow{P_0X}) \); it is affine with \( \vec f = T \) by @thm-affine-map-is-linear-plus-translation (c). Then \( f(P_0) = Q_0 + T(\0) = Q_0 \), and \( f(P_i) = Q_0 + \overrightarrow{Q_0Q_i} = Q_i \).

*Uniqueness.* Let \( g \) be affine with \( g(P_i) = Q_i \) for all \( i \). By @thm-affine-map-is-linear-plus-translation (b),
\[
\vec{g}(\overrightarrow{P_0P_i}) = \overrightarrow{g(P_0)g(P_i)} = \overrightarrow{Q_0Q_i} = T(\overrightarrow{P_0P_i}) \qquad (i = 1, \dots, n),
\]
so \( \vec g \) and \( T \) agree on a basis and are equal (@thm-linear-transform-basis). Hence \( g(X) = g(P_0) + \vec g(\overrightarrow{P_0X}) = Q_0 + T(\overrightarrow{P_0X}) = f(X) \) for every \( X \).

The displayed identity is @def-affine-map applied to \( \sum_i t_iP_i \), using \( f(P_i) = Q_i \).
:::

So \( n + 1 \) points in the right position determine an affine map of an \( n \)-dimensional space, and prescribe it freely. Fewer points never do, and not because our proof is weak.

::: {#prp-fewer-points-insufficient}
[Points inside a proper flat do not determine an affine map]

Let \( \dim \cA = n \ge 1 \) and let \( S \subseteq \cA \) be contained in a flat \( A \) with \( \dim A < n \) — for instance, any set of at most \( n \) points. Then there are two **distinct** affine maps \( \cA \to \cA \) that agree at every point of \( S \).
:::

::: {.proof}
Let \( P \in A \) and let \( (\u_1, \dots, \u_d) \) be a basis of \( \vec{A} \), where \( d = \dim A < n \). Extend it to a basis \( (\u_1, \dots, \u_d, \w_1, \dots, \w_{n-d}) \) of \( V \) (@thm-basis-extension); since \( d < n \), the vector \( \w_1 \) exists. Let \( T \colon V \to V \) be the linear map fixing each \( \u_j \) and each \( \w_k \) with \( k \ge 2 \), and sending \( \w_1 \) to \( \0 \) (@thm-linear-map-from-any-basis), and put \( g(X) = P + T(\overrightarrow{PX}) \), an affine map by @thm-affine-map-is-linear-plus-translation (c).

For \( X \in A \) we have \( \overrightarrow{PX} \in \vec{A} = \Span(\u_1, \dots, \u_d) \), on which \( T \) is the identity, so \( g(X) = P + \overrightarrow{PX} = X \). Hence \( g \) agrees with \( \id_{\cA} \) on \( A \), and so on \( S \). But \( g \ne \id_{\cA} \), since \( g(P + \w_1) = P + T(\w_1) = P \ne P + \w_1 \) by @lem-chasles-consequences (c).

Finally, a non-empty set of at most \( n \) points does lie in such a flat. Put
\[
D = P_0 + \Span(\overrightarrow{P_0P_1}, \dots, \overrightarrow{P_0P_m}) .
\]
This is the smallest flat containing \( P_0, \dots, P_m \): it is a flat by @prp-flat-is-coset and contains every \( P_i \); and any flat containing all the \( P_i \) contains \( P_0 \), hence equals \( P_0 + U \) with each \( \overrightarrow{P_0P_i} \in U \), so it contains \( D \) by @thm-span-subspace. Thus \( \dim D \le m \), and \( m + 1 \le n \) gives \( \dim D \le n - 1 < n \). (An empty \( S \) lies in the flat \( \{P\} \) for any \( P \).)
:::

@exm-affine-maps-agreeing-on-two-points is an instance of this proposition, with \( n = 2 \) and \( S = \{(0,0), (1,0)\} \); it exhibits its own pair of maps rather than the pair the proof constructs. The moral is the count: \( n + 1 \), never \( n \). It is the same count that will govern projective transformations later in this chapter, where the answer turns out to be \( n + 2 \).

## A flat is a solution set

Chapter 2 produced flats as solution sets; Chapter 4 proved that every subspace of \( F^n \) is a null space. Putting the two together identifies the flats of \( \nA^n(F) \) completely.

::: {#thm-flat-is-solution-set}
[Flats Are Exactly the Solution Sets]

Let \( A \subseteq \nA^n(F) \) be non-empty and \( 0 \le k \le n \). The following are equivalent.

::: {.enumerate options="label=(\alph*)"}
1. \( A \) is a flat of dimension \( k \).
2. \( A = \{ \x \in F^n : \M\x = \c \} \) for some \( \M \in M_{(n-k) \times n}(F) \) with linearly independent rows and some \( \c \in F^{n-k} \).
:::

In that case no system with fewer than \( n - k \) equations has solution set \( A \), and for \( k < n \) the flat \( A \) is an intersection of exactly \( n - k \) affine hyperplanes.
:::

::: {.idea}
A flat is a coset \( \p + U \) by @prp-flat-is-coset, Chapter 4 turns \( U \) into a null space, and Chapter 2's "particular plus homogeneous" turns the coset into the solution set of the inhomogeneous system with the same matrix and right-hand side \( \M\p \).
:::

::: {.proof}
(a) \( \Rightarrow \) (b). By @prp-flat-is-coset, \( A = \p + U \) with \( U = \vec{A} \) and \( \dim U = k \). By @thm-subspace-is-solution-set (a) there is \( \M \in M_{(n-k)\times n}(F) \) with \( \nul(\M) = U \) whose rows \( \a_1\tp, \dots, \a_{n-k}\tp \) are the ones corresponding to a basis \( (\varphi_{\a_1}, \dots, \varphi_{\a_{n-k}}) \) of \( U^0 \) under the isomorphism \( \a \mapsto \varphi_{\a} \) of @thm-functionals-on-fn; an injective linear map preserves independence (@thm-injective-preserves-independence), so those rows are linearly independent. Put \( \c = \M\p \). Then \( \p \) solves \( \M\x = \c \), so by @thm-general-solution-structure the solution set is \( \p + \nul(\M) = \p + U = A \).

(b) \( \Rightarrow \) (a). The set \( A \) is non-empty, so it has an element \( \p \), and @thm-general-solution-structure gives \( A = \p + \nul(\M) \), a coset, hence a flat by @prp-flat-is-coset with \( \vec{A} = \nul(\M) \). The rows of \( \M \) are independent, so \( \rank\M = \dim\row(\M) = n - k \) by @thm-row-rank-equals-column-rank, and @thm-rank-nullity-matrix gives \( \dim A = \nullity(\M) = n - (n-k) = k \).

*Minimality.* Suppose \( \B \in M_{m \times n}(F) \) and \( \d \in F^m \) satisfy \( \{\x : \B\x = \d\} = A \). Fix \( \p \in A \). For any \( \x \), \( \B\x = \d \) holds if and only if \( \B(\x - \p) = \0 \), so \( \x \in A \) if and only if \( \x - \p \in \nul(\B) \); that is, \( A = \p + \nul(\B) \). Comparing with \( A = \p + \vec{A} \) and using @prp-flat-is-coset (a), \( \nul(\B) = \vec{A} = U \). By @thm-subspace-is-solution-set (b), \( m \ge n - k \).

*Hyperplanes.* Let \( k < n \) and write \( \a_1\tp, \dots, \a_{n-k}\tp \) for the rows of a matrix \( \M \) as in (b). Each \( \varphi_{\a_i} \) vanishes on \( U = \nul(\M) \), hence lies in \( U^0 \) (@def-annihilator), and the \( \varphi_{\a_i} \) are independent because the rows are and \( \a \mapsto \varphi_{\a} \) is an isomorphism (@thm-functionals-on-fn); as \( \dim U^0 = n - k \) by @thm-dimension-annihilator, they are a basis of \( U^0 \) (@thm-right-size-basis). So \( \M \) is a matrix as in @thm-subspace-is-solution-set (a), and @prp-affine-subspace-intersection applied to \( U \) and \( \p \) writes \( A = \p + U \) as the intersection of the \( n - k \) affine hyperplanes \( \{\x : \a_i\tp\x = \a_i\tp\p\} \).
:::

For \( k = n \) the system is empty and \( A = F^n \); for \( k = 0 \) it has \( n \) independent equations and \( A \) is a single point. In between, the count is the familiar one: **dimension counts parameters, codimension counts independent equations**, and now it holds for flats as it did for subspaces.

::: {#exm-flat-equations}
[Equations for a plane in four-space]

In @exm-implicit-equations the subspace \( U = \Span\bigl((1,1,0,1), (0,1,1,1)\bigr) \) of \( \nR^4 \) was found to be \( \{ \x : x_1 - x_2 + x_3 = 0,\ x_4 - x_2 = 0 \} \). Find equations for the flat \( A = \p + U \) with \( \p = (1, 0, 0, 0) \), and give two of its points.
:::

::: {.solution}
Take \( \M = \begin{pmatrix} 1 & -1 & 1 & 0 \\ 0 & -1 & 0 & 1 \end{pmatrix} \), whose null space is \( U \), and \( \c = \M\p = (1, 0) \). By @thm-flat-is-solution-set,
\[
A = \{ \x \in \nR^4 : x_1 - x_2 + x_3 = 1, \ \ x_4 - x_2 = 0 \} ,
\]
a flat of dimension \( 4 - 2 = 2 \). Two points: \( \p = (1,0,0,0) \), with \( 1 - 0 + 0 = 1 \) and \( 0 - 0 = 0 \); and \( \p + (1,1,0,1) = (2,1,0,1) \), with \( 2 - 1 + 0 = 1 \) and \( 1 - 1 = 0 \). By the minimality clause, no single equation cuts out \( A \), since \( n - k = 2 \).
:::

That closes the affine part of the chapter's foundations. Flats are cosets, they meet or they do not, their joins obey a two-case formula, they carry symmetric coordinates, and in \( \nA^n(F) \) they are the solution sets of linear systems. The one irritant is the second case of the join formula, and the reason two coplanar lines can fail to meet: in the affine plane, parallel lines have nowhere to intersect. The projective sections later in this chapter remove that exception by adding the missing points.

## Exercises

### A. Check your understanding

::: {#exr-affine-subspaces-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define a flat and its direction space, and say why the direction space does not depend on the point used to compute it.
2. State both cases of the dimension formula for \( \dim(A \vee B) \), and say which one applies to two distinct parallel planes in \( \nA^3 \).
3. True or false, with a reason: the intersection of two flats is a flat.
4. What are the barycentric coordinates of \( P_2 \) with respect to the frame \( (P_0, P_1, P_2, P_3) \) of a three-dimensional affine space?
:::
:::

::: {.solution}
(a) A flat is a non-empty subset closed under affine combinations (@def-flat); equivalently a coset \( P + U \) with \( U \) a subspace of \( V \) (@prp-flat-is-coset). Its direction space is \( \vec{A} = \{\overrightarrow{XY} : X, Y \in A\} \), a description that mentions only \( A \), so no choice of point enters.

(b) If \( A \cap B \ne \emptyset \), \( \dim(A \vee B) = \dim A + \dim B - \dim(A \cap B) \); if \( A \cap B = \emptyset \), \( \dim(A\vee B) = \dim A + \dim B - \dim(\vec A \cap \vec B) + 1 \). Two distinct parallel planes in \( \nA^3 \) are disjoint (@prp-parallel-equivalence), so the second applies: \( 2 + 2 - 2 + 1 = 3 \), and their join is \( \nA^3 \).

(c) False as stated, because the intersection may be empty, and the empty set is not a flat (@def-flat). It is true that a **non-empty** intersection of flats is a flat (@prp-flat-intersection). Two parallel lines in \( \nA^2 \) give the counterexample.

(d) \( (0, 0, 1, 0) \): the combination \( 0 \cdot P_0 + 0 \cdot P_1 + 1 \cdot P_2 + 0 \cdot P_3 \) has weights summing to \( 1 \) and equals \( P_2 \), and the coordinates are unique by @thm-barycentric-coordinates.
:::

### B. Practice

::: {#exr-affine-subspaces-b1}
[B1: Two flats in four-space]

In \( \nA^4 \) let \( A = (1,0,0,0) + \Span\bigl((1,1,0,0), (0,0,1,1)\bigr) \), and let
\[
B = (0,1,0,0) + \Span\bigl((1,0,1,0)\bigr), \qquad B' = (2,1,0,0) + \Span\bigl((1,0,1,0)\bigr) .
\]
For each of \( B \) and \( B' \), decide whether it meets \( A \), and compute \( \dim(A \vee \cdot) \). Justify your answers with @thm-flat-intersection-and-join.
:::

::: {.solution}
Write \( P = (1,0,0,0) \), \( \vec{A} = \Span\bigl((1,1,0,0),(0,0,1,1)\bigr) \) and \( \vec{B} = \vec{B'} = \Span\bigl((1,0,1,0)\bigr) \). The three spanning vectors are independent (the first two have disjoint supports, and \( a(1,1,0,0) + b(0,0,1,1) = (1,0,1,0) \) would need \( a = 1 \) and \( a = 0 \)), so \( \dim(\vec A + \vec B) = 3 \) and \( \vec{A} \cap \vec{B} = \{\0\} \).

**\( B \).** Here \( Q = (0,1,0,0) \) and \( \overrightarrow{PQ} = (-1,1,0,0) \). If \( \overrightarrow{PQ} = a(1,1,0,0) + b(0,0,1,1) + c(1,0,1,0) \), the second coordinate gives \( a = 1 \) and the first gives \( a + c = -1 \), so \( c = -2 \); the third then gives \( b + c = 0 \), so \( b = 2 \), and the fourth gives \( b = 0 \), a contradiction. So \( \overrightarrow{PQ} \notin \vec A + \vec B \) and \( A \cap B = \emptyset \) by part (b) of the theorem. Part (c) gives \( \dim(A \vee B) = 2 + 1 - 0 + 1 = 4 \), so \( A \vee B = \nA^4 \).

**\( B' \).** Here \( Q' = (2,1,0,0) \) and \( \overrightarrow{PQ'} = (1,1,0,0) \in \vec A \subseteq \vec A + \vec{B'} \), so \( A \cap B' \ne \emptyset \). Following the proof of part (b), the meeting point is \( P + (1,1,0,0) = (2,1,0,0) = Q' \), and indeed \( Q' \in A \cap B' \). By part (b) the direction space of \( A \cap B' \) is \( \vec A \cap \vec{B'} = \{\0\} \), so the intersection is the single point \( \{Q'\} \), of dimension \( 0 \), and \( \dim(A \vee B') = 2 + 1 - 0 = 3 \).
:::

::: {#exr-affine-subspaces-b2}
[B2: Barycentric arithmetic]

In \( \nA^2 \) take the frame \( P_0 = (1, 1) \), \( P_1 = (3, 1) \), \( P_2 = (1, 4) \).

::: {.enumerate options="label=(\alph*)"}
1. Verify that it is a frame.
2. Find the barycentric coordinates (@thm-barycentric-coordinates) of \( X = (2, 2) \).
3. Find the centroid of \( (P_0, P_1, P_2) \) in ordinary coordinates, and check its barycentric coordinates.
:::
:::

::: {.solution}
(a) \( \overrightarrow{P_0P_1} = (2, 0) \) and \( \overrightarrow{P_0P_2} = (0, 3) \) are independent, so the list is affinely independent by @lem-affine-independence-differences, and it has \( 3 = 2 + 1 \) entries.

(b) \( \overrightarrow{P_0X} = (1, 1) = t_1(2,0) + t_2(0,3) \) gives \( t_1 = \tfrac12 \), \( t_2 = \tfrac13 \), so \( t_0 = 1 - \tfrac12 - \tfrac13 = \tfrac16 \). The coordinates are \( \bigl(\tfrac16, \tfrac12, \tfrac13\bigr) \). **Check:** \( \tfrac16(1,1) + \tfrac12(3,1) + \tfrac13(1,4) = \bigl(\tfrac16 + \tfrac32 + \tfrac13,\ \tfrac16 + \tfrac12 + \tfrac43\bigr) = (2, 2) \).

(c) \( G = \tfrac13\bigl((1,1) + (3,1) + (1,4)\bigr) = \bigl(\tfrac53, 2\bigr) \). Its barycentric coordinates are \( \bigl(\tfrac13,\tfrac13,\tfrac13\bigr) \) by definition, and by uniqueness these are the only ones. **Check against (b)'s method:** \( \overrightarrow{P_0G} = \bigl(\tfrac23, 1\bigr) = \tfrac13(2,0) + \tfrac13(0,3) \), so \( t_1 = t_2 = \tfrac13 \) and \( t_0 = \tfrac13 \).
:::

::: {#exr-affine-subspaces-b3}
[B3: From parameters to equations and back]

::: {.enumerate options="label=(\alph*)"}
1. Find a system of equations whose solution set is the line \( A = (1, 2, 3) + \Span\bigl((1, 1, 1)\bigr) \) in \( \nA^3 \), using as few equations as possible.
2. The set \( B = \{ \x \in \nR^3 : x_1 + x_2 + x_3 = 6 \} \) is a flat. Find its dimension, a point of it, and its direction space.
3. Decide whether \( A \subseteq B \), and compute \( \dim(A \vee B) \).
:::
:::

::: {.solution}
(a) Here \( k = 1 \) and \( n = 3 \), so @thm-flat-is-solution-set calls for \( 3 - 1 = 2 \) equations, and no fewer will do. A functional \( \a\tp\x \) vanishes on \( \Span((1,1,1)) \) exactly when \( a_1 + a_2 + a_3 = 0 \); two independent such rows are \( (1,-1,0) \) and \( (0,1,-1) \). With \( \p = (1,2,3) \) the right-hand sides are \( 1 - 2 = -1 \) and \( 2 - 3 = -1 \), so
\[
A = \{ \x : x_1 - x_2 = -1, \ x_2 - x_3 = -1 \} .
\]
**Check:** \( \p \) satisfies both, and so does \( \p + (1,1,1) = (2,3,4) \).

(b) One equation with a non-zero row, so \( \dim B = 3 - 1 = 2 \) by @thm-flat-is-solution-set, a plane. The point \( (6,0,0) \) lies in it, and \( \vec{B} = \nul\begin{pmatrix} 1 & 1 & 1\end{pmatrix} = \{ \x : x_1 + x_2 + x_3 = 0 \} \).

(c) \( \p = (1,2,3) \) has \( 1 + 2 + 3 = 6 \), so \( \p \in B \); but \( (1,1,1) \notin \vec{B} \), since \( 1 + 1 + 1 = 3 \ne 0 \). So \( A \not\subseteq B \), while \( A \cap B \ne \emptyset \) (it contains \( \p \)). Since \( \vec A \cap \vec B = \{\0\} \), the intersection is the single point \( \{\p\} \) and \( \dim(A \vee B) = 1 + 2 - 0 = 3 \): the line and the plane together span \( \nA^3 \).
:::

### C. Going deeper

::: {#exr-affine-subspaces-c1}
[C1: Affine maps and flats]

Let \( f \colon \cA \to \cB \) be affine and let \( A \subseteq \cA \) be a flat.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( f(A) \) is a flat of \( \cB \) whose direction space is \( \vec{f}(\vec{A}) \), and deduce \( \dim f(A) \le \dim A \).
2. Prove that if \( B \subseteq \cB \) is a flat with \( f^{-1}(B) \ne \emptyset \), then \( f^{-1}(B) \) is a flat with direction space \( (\vec f)^{-1}(\vec B) \).
3. Hence prove that an **injective** affine map sends flats to flats of the same dimension, and lines to lines.
:::
:::

::: {.solution}
(a) \( f(A) \) is non-empty. Let \( P \in A \), so \( A = P + \vec A \) (@prp-flat-is-coset). For \( \u \in \vec A \), @thm-affine-map-is-linear-plus-translation (c) gives \( f(P + \u) = f(P) + \vec f(\u) \). Hence \( f(A) = f(P) + \vec f(\vec A) \), and \( \vec{f}(\vec{A}) \) is a subspace of \( W \), being the image of the linear map \( \vec f \) restricted to the subspace \( \vec{A} \) (@thm-prop-image applied to that restriction). So \( f(A) \) is a flat by @prp-flat-is-coset, with the stated direction space, and \( \dim f(A) = \dim\vec f(\vec A) \le \dim\vec A = \dim A \), because the images of a basis of \( \vec A \) span \( \vec f(\vec A) \) (@thm-image-spanned-by-basis-images) and a spanning list is at least as long as the dimension (@thm-size-bounds (b)).

(b) Let \( P \in f^{-1}(B) \), so \( f(P) \in B \). For \( \u \in V \), \( f(P + \u) = f(P) + \vec f(\u) \) lies in \( B = f(P) + \vec B \) exactly when \( \vec f(\u) \in \vec B \). So \( f^{-1}(B) = P + (\vec f)^{-1}(\vec B) \), and \( (\vec f)^{-1}(\vec B) \) is a subspace: it contains \( \0 \) and is closed under linear combinations by linearity of \( \vec f \) and the subspace test (@thm-subspace-test). By @prp-flat-is-coset, \( f^{-1}(B) \) is a flat with that direction space.

(c) If \( f \) is injective, then \( \vec f \) is injective: \( \vec f(\u) = \0 \) gives \( f(P + \u) = f(P) \), hence \( P + \u = P \) and \( \u = \0 \). An injective linear map carries a basis of \( \vec A \) to a linearly independent list (@thm-injective-preserves-independence) that spans \( \vec f(\vec A) \), hence to a basis of it; so \( \dim f(A) = \dim\vec f(\vec A) = \dim\vec A = \dim A \) by (a). A line has dimension \( 1 \), so its image is a flat of dimension \( 1 \), a line.
:::

::: {#exr-affine-subspaces-c2}
[C2: The midpoint quadrilateral]

Let \( F \) be a field with \( 2 \ne 0 \), let \( \cA \) be an affine space over \( F \), and let \( P_1, P_2, P_3, P_4 \in \cA \) be any four points. Put \( M_{12} = \tfrac12P_1 + \tfrac12P_2 \), and define \( M_{23}, M_{34}, M_{41} \) likewise.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \overrightarrow{M_{12}M_{23}} = \overrightarrow{M_{41}M_{34}} = \tfrac12\overrightarrow{P_1P_3} \).
2. Deduce that if \( M_{12}, M_{23}, M_{34}, M_{41} \) are distinct, then \( M_{12} \vee M_{23} \) and \( M_{41} \vee M_{34} \) are parallel lines, and likewise for the other pair of opposite sides: the four midpoints form a parallelogram.
3. What does the statement say when \( P_1, P_2, P_3, P_4 \) are **not** coplanar, for instance in \( \nA^3 \)?
:::
:::

::: {.solution}
(a) Fix any origin \( O \) and write \( \p_i = \overrightarrow{OP_i} \). By @def-affine-combination, \( \overrightarrow{O M_{12}} = \tfrac12(\p_1 + \p_2) \) and similarly for the others. Hence, by @prp-choice-of-origin,
\[
\overrightarrow{M_{12}M_{23}} = \tfrac12(\p_2 + \p_3) - \tfrac12(\p_1 + \p_2) = \tfrac12(\p_3 - \p_1) = \tfrac12\overrightarrow{P_1P_3} ,
\]
and
\[
\overrightarrow{M_{41}M_{34}} = \tfrac12(\p_3 + \p_4) - \tfrac12(\p_4 + \p_1) = \tfrac12(\p_3 - \p_1) .
\]
The answer does not depend on \( O \), as it must not.

(b) If \( M_{12} \ne M_{23} \), the join \( M_{12} \vee M_{23} \) is the line \( M_{12} + \Span(\overrightarrow{M_{12}M_{23}}) \) by @thm-flat-intersection-and-join (a). By (a) the two lines \( M_{12} \vee M_{23} \) and \( M_{41} \vee M_{34} \) have the same direction space \( \Span\bigl(\tfrac12\overrightarrow{P_1P_3}\bigr) \), so they are parallel (@def-parallel-flats). Running (a) with the indices shifted by one gives \( \overrightarrow{M_{23}M_{34}} = \overrightarrow{M_{12}M_{41}} = \tfrac12\overrightarrow{P_2P_4} \), so the other two sides are parallel too.

(c) Nothing in (a) used coplanarity, so the conclusion holds for a skew quadrilateral in \( \nA^3 \) as well: the four midpoints of a skew quadrilateral are coplanar and form a parallelogram. Four non-coplanar points are affinely independent: otherwise \( (\overrightarrow{P_1P_2}, \overrightarrow{P_1P_3}, \overrightarrow{P_1P_4}) \) would be dependent (@lem-affine-independence-differences) and span a subspace of dimension at most \( 2 \), putting all four points in a flat of dimension at most \( 2 \). The four midpoints are then distinct, since the difference of two of them is \( \sum_i\lambda_iP_i \) with \( \sum_i\lambda_i = 0 \) and the \( \lambda_i \) not all zero — for \( M_{12} \) and \( M_{23} \) the weights are \( \tfrac12 \) at \( P_1 \) and \( -\tfrac12 \) at \( P_3 \) — hence is a non-zero vector; so (b) applies. The two parallel lines \( M_{12} \vee M_{23} \) and \( M_{41} \vee M_{34} \) are also distinct: were they equal, their common direction space would contain \( \overrightarrow{M_{12}M_{41}} \), which is \( \tfrac12\overrightarrow{P_2P_4} \) by (b), so \( \tfrac12\overrightarrow{P_2P_4} = \mu \cdot \tfrac12\overrightarrow{P_1P_3} \) for some \( \mu \in F \) (@prp-flat-is-coset (a)) — a relation \( \sum_i\lambda_iP_i = \0 \) with weights summing to \( 0 \) and \( -\tfrac12 \ne 0 \) at \( P_2 \), again against affine independence. Their join is therefore a plane, of dimension \( 1 + 1 - 1 + 1 = 2 \) by @thm-flat-intersection-and-join (c), and it contains all four midpoints.
:::

::: {#exr-affine-subspaces-c3}
[C3: Medians over the field with three elements]

Work in \( \nA^2(\nF_3) \) with the affinely independent list \( P_1 = (0,0) \), \( P_2 = (1,0) \), \( P_3 = (0,1) \). (Nothing is lost by this choice: by @thm-affine-map-determined-by-frame any other affinely independent triple is carried to this one by an affine bijection, which preserves midpoints, being an affine combination, and carries lines to lines by @exr-affine-subspaces-c1.)

::: {.enumerate options="label=(\alph*)"}
1. Compute the three midpoints \( M_i \) and the three medians \( m_i = P_i \vee M_i \).
2. Prove that the three medians are pairwise parallel and pairwise disjoint, so that @prp-medians-meet-at-centroid fails over \( \nF_3 \).
3. Explain which step of the proof of @prp-medians-meet-at-centroid breaks, and why the hypothesis \( 3 \ne 0 \) cannot be dropped.
:::
:::

::: {.solution}
(a) In \( \nF_3 \) we have \( 2^{-1} = 2 \), since \( 2 \cdot 2 = 4 = 1 \). So
\[
\begin{aligned}
M_1 &= 2P_2 + 2P_3 = 2(1,0) + 2(0,1) = (2,2) , \\
M_2 &= 2P_1 + 2P_3 = (0,2) , \\
M_3 &= 2P_1 + 2P_2 = (2,0) .
\end{aligned}
\]
Then \( \overrightarrow{P_1M_1} = (2,2) \), \( \overrightarrow{P_2M_2} = (0,2) - (1,0) = (2,2) \) and \( \overrightarrow{P_3M_3} = (2,0) - (0,1) = (2,2) \). So
\[
\begin{aligned}
m_1 &= (0,0) + \Span\bigl((2,2)\bigr), \\
m_2 &= (1,0) + \Span\bigl((2,2)\bigr), \\
m_3 &= (0,1) + \Span\bigl((2,2)\bigr) .
\end{aligned}
\]

(b) All three have the same direction space \( \Span((2,2)) = \Span((1,1)) \), so they are parallel (@def-parallel-flats). They are distinct: \( \overrightarrow{P_1P_2} = (1,0) \notin \Span((1,1)) \), and likewise for the other two pairs, so no two of them share a point by @prp-flat-is-coset (b). Distinct parallel flats are disjoint (@prp-parallel-equivalence). Hence the three medians have no common point, and the conclusion of @prp-medians-meet-at-centroid is false here.

(c) The proof solved \( \tfrac32 s = 1 \) for \( s \), which needs \( 3 \) to be invertible. Over \( \nF_3 \) the point \( \tfrac13(P_1 + P_2 + P_3) \) does not exist, because \( 3 = 0 \) has no inverse; the weights \( (\tfrac13,\tfrac13,\tfrac13) \) cannot be written down at all. Concretely, the equation \( 1 - s = \tfrac{s}{2} \) becomes \( 1 - s = 2s \), that is, \( 1 = 3s = 0 \), which has no solution: the parametrizations of \( m_1 \) and \( m_2 \) never agree. So the hypothesis \( 3 \ne 0 \) is not an artifact of the proof; it is needed for the statement.
:::
