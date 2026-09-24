# Convex Polyhedra, Geometrically

Chapter 18 built the theory of convex sets and proved its main theorems: that a compact convex set is the hull of its extreme points, that a bounded polyhedron and a polytope are the same thing, and that a feasible, bounded linear program and its dual have the same optimal value. **This section proves none of that again.** It reads those theorems as statements about the geometry of a solid with flat sides: what its faces are, how they fit together, and what a linear program looks like when the objective is a family of parallel hyperplanes sliding across it. Everything here is a corollary of Chapter 18 or a short argument on top of it, and every citation points back there.

Throughout, the field is \( \nR \) and the space is \( \nR^n \) with the dot product, as in Chapter 18. A polyhedron is a set \( P = \{\x \in \nR^n : \A\x \le \b\} \) (@def-polyhedron), with \( \A \in M_{m \times n}(\nR) \) whose rows we write \( \a_1\tp, \dots, \a_m\tp \), so that \( \A\x \le \b \) is the list of inequalities \( \a_i\tp\x \le b_i \). A **vertex** of \( P \) is an extreme point of it (@def-extreme-point), and \( \operatorname{ext} P \) is the set of them. We use Chapters 16 and 18's topological words — closed, bounded, compact — only inside the results we cite; nothing here develops them further.

## Faces, cut by a supporting hyperplane

A cube has six square sides, twelve edges and eight corners, and each of them is the part of the cube touched by a plane that has the whole cube on one side. That is the picture to formalize. The tool is Chapter 18's supporting hyperplane (@thm-supporting-hyperplane): a hyperplane through a point of a convex set with the set in one of its closed half-spaces.

*A face of a polyhedron is the part of it touched by a hyperplane that does not cut into it.*

::: {#def-polyhedron-face}
[Face of a Polyhedron]

Let \( P \subseteq \nR^n \) be a polyhedron. A **face** of \( P \) is a set of the form
\[
F = \{\x \in P : \c\tp\x = \beta\}
\]
for some \( \c \in \nR^n \) and \( \beta \in \nR \) such that \( \c\tp\x \le \beta \) **for every** \( \x \in P \). A face other than \( P \) itself is called **proper**.
:::

Clause by clause. The pair \( (\c, \beta) \) must be a **valid inequality** for \( P \): the whole polyhedron lies in the closed half-space \( \{\c\tp\x \le \beta\} \). The face is then what the boundary hyperplane \( \{\c\tp\x = \beta\} \) actually touches. Note that \( \c \) is allowed to be \( \0 \).

Two faces come free. Taking \( \c = \0 \) and \( \beta = 0 \) makes the inequality \( 0 \le 0 \), valid everywhere, and \( F = P \): **the whole polyhedron is a face of itself**. Taking \( \c = \0 \) and \( \beta = 1 \) makes the inequality \( 0 \le 1 \), again valid, and \( F = \emptyset \): **the empty set is a face**. These two are the degenerate cases, and they are kept because the theorems below are cleaner with them than without.

Chapter 18 §08 already has a notion of face for an arbitrary convex set, @def-face: a convex subset \( F \subseteq C \) that swallows every segment of \( C \) passing through it at an inner point. The two agree here in one direction at once.

::: {.remark}
Every face in the sense of @def-polyhedron-face is a face in the sense of @def-face. That is exactly @prp-exposed-face (a), applied with \( \w = \c \) and \( \alpha = \beta \), since on \( \nR^n \) the inner product \( \inner{\c}{\x} \) is \( \c\tp\x \). So everything Chapter 18 proves about faces applies to ours; in particular @lem-extreme-points-of-face gives \( \operatorname{ext} F = F \cap \operatorname{ext} P \). The converse — that every face of a **polyhedron** in Chapter 18's sense is cut out by a supporting hyperplane — is also true, and @exr-polyhedra-and-linear-programming-c2 proves it. It uses flatness: the same exercise ends with a round convex set having a one-point face in the sense of @def-face that no supporting hyperplane isolates, so the converse fails for general convex sets.
:::

**Examples**, in \( \nR^2 \), with \( P \) the triangle \( \{x_1 \ge 0,\ x_2 \ge 0,\ x_1 + x_2 \le 3\} \) of Chapter 18 §09.

1. \( \c = (1,1) \), \( \beta = 3 \). The inequality is valid by the third row, and the face is the slanted edge from \( (3,0) \) to \( (0,3) \).
2. \( \c = (1,0) \), \( \beta = 3 \). Valid, since \( x_1 \le x_1 + x_2 \le 3 \) on \( P \). The face is the single point \( (3, 0) \): the hyperplane \( x_1 = 3 \) touches the triangle at one corner.
3. \( \c = (-1, 0) \), \( \beta = 0 \). Valid by the first row, and the face is the vertical edge \( \{0\} \times [0,3] \).
4. \( \c = (1, 1) \), \( \beta = 4 \). Valid, but never attained: the face is \( \emptyset \).

**A non-example by minimal change.** In example 1 replace \( \beta = 3 \) by \( \beta = 2 \). The set \( \{\x \in P : x_1 + x_2 = 2\} \) is still a segment inside \( P \), still convex, and still a slice by a hyperplane. What fails is the one clause the definition insists on: \( x_1 + x_2 \le 2 \) is **not** valid for \( P \), since \( (3,0) \in P \) violates it. The hyperplane cuts through the triangle instead of resting against it, and the slice is not a face. It also fails @def-face: the segment from \( (0,0) \) to \( (3,0) \) passes through \( (2,0) \) at an inner point but is not contained in the slice.

The reason faces are useful is that there are only finitely many of them, and each is again a polyhedron described by the **same** rows, some of them turned into equations.

::: {#prp-face-is-polyhedron}
[Faces Are Polyhedra, and There Are Finitely Many]

Let \( P = \{\x \in \nR^n : \A\x \le \b\} \) with \( m \) rows. For \( J \subseteq \{1, \dots, m\} \) put
\[
P_J = \{\x \in P : \a_i\tp\x = b_i \text{ for every } i \in J\} .
\]
Then:

::: {.enumerate options="label=(\alph*)"}
1. every \( P_J \) is a face of \( P \), and it is a polyhedron;
2. every **non-empty** face of \( P \) equals \( P_J \) for some \( J \);
3. consequently \( P \) has at most \( 2^m \) non-empty faces, and every face of \( P \) is a polyhedron.
:::
:::

::: {.idea}
For (a), add up the rows indexed by \( J \): the sum \( \sum_{i \in J}\a_i\tp\x \) is at most \( \sum_{i \in J}b_i \) on \( P \), and a sum of numbers each at most its bound hits the total bound only if every one of them does. So one valid inequality encodes all of \( J \) at once.

For (b), let \( F \) be a non-empty face and let \( J \) collect the rows that are tight at **every** point of \( F \). Certainly \( F \subseteq P_J \). For the other inclusion we need a point \( \x^{*} \) of \( F \) at which every row outside \( J \) is **slack**; averaging finitely many points of \( F \), one per slack row, produces it. Then, given \( \y \in P_J \) with \( \c\tp\y < \beta \), step from \( \x^{*} \) **away** from \( \y \). The rows in \( J \) are equations satisfied by both points, so they survive the step exactly; the rows outside \( J \) have room at \( \x^{*} \), so they survive a short step. But the step raises \( \c\tp\x \) above \( \beta \), which no point of \( P \) may do.
:::

::: {.proof}
(a) Put \( \c = \sum_{i \in J}\a_i \) and \( \beta = \sum_{i \in J}b_i \), with the empty sums \( \0 \) and \( 0 \). For \( \x \in P \),
\[
\c\tp\x = \sum_{i \in J}\a_i\tp\x \le \sum_{i \in J}b_i = \beta ,
\]
so the inequality is valid. If \( \x \in P \) and \( \c\tp\x = \beta \), then \( \sum_{i \in J}(b_i - \a_i\tp\x) = 0 \) is a sum of non-negative numbers, so each is zero and \( \x \in P_J \); conversely every \( \x \in P_J \) has \( \c\tp\x = \beta \). Hence \( P_J = \{\x \in P : \c\tp\x = \beta\} \) is a face. It is a polyhedron because each equation \( \a_i\tp\x = b_i \) is the pair of inequalities \( \a_i\tp\x \le b_i \) and \( -\a_i\tp\x \le -b_i \), so \( P_J \) is cut out by \( m + \lvert J\rvert \) inequalities.

(b) Let \( F = \{\x \in P : \c\tp\x = \beta\} \) be non-empty, with \( \c\tp\x \le \beta \) on \( P \). Put
\[
J = \{i : \a_i\tp\x = b_i \text{ for every } \x \in F\} .
\]
Then \( F \subseteq P_J \) by the definition of \( J \), and it remains to prove \( P_J \subseteq F \).

First note that \( F \) is convex: it is the intersection of the convex set \( P \) (@prp-polyhedron-closed-convex) with the solution set of a linear equation, which is convex as the preimage of a point under \( \x \mapsto \c\tp\x \) (@prp-convexity-operations (b)); an intersection of convex sets is convex by @prp-convexity-operations (a).

**Step 1: a point of \( F \) with every row outside \( J \) slack.** For each \( i \notin J \) choose, by the definition of \( J \), a point \( \x_i \in F \) with \( \a_i\tp\x_i < b_i \). If \( J = \{1, \dots, m\} \) let \( \x^{*} \) be any point of \( F \). Otherwise let \( k \ge 1 \) be the number of indices outside \( J \) and let \( \x^{*} = \frac1k\sum_{i \notin J}\x_i \), which lies in \( F \) by convexity. For each \( i \notin J \), every term of \( \a_i\tp\x^{*} = \frac1k\sum_{j \notin J}\a_i\tp\x_j \) is at most \( b_i \) and the term \( j = i \) is strictly less, so \( \a_i\tp\x^{*} < b_i \).

**Step 2: the step away from \( \y \).** Let \( \y \in P_J \) and suppose, for a contradiction, that \( \c\tp\y < \beta \). For \( t > 0 \) put \( \z_t = \x^{*} + t(\x^{*} - \y) \). For \( i \in J \) we have \( \a_i\tp\x^{*} = b_i \), because \( \x^{*} \in F \subseteq P_J \), and \( \a_i\tp\y = b_i \), because \( \y \in P_J \); hence
\[
\a_i\tp\z_t = b_i + t(b_i - b_i) = b_i \le b_i .
\]
For \( i \notin J \) put \( \delta = \min_{i \notin J}(b_i - \a_i\tp\x^{*}) > 0 \) and \( M = \max_{i \notin J}\lvert\a_i\tp\x^{*} - \a_i\tp\y\rvert \); both are minima and maxima of finitely many numbers. Choose \( t > 0 \) with \( tM < \delta \), which is possible (any \( t \) will do if \( M = 0 \)). Then for \( i \notin J \),
\[
\a_i\tp\z_t = \a_i\tp\x^{*} + t\bigl(\a_i\tp\x^{*} - \a_i\tp\y\bigr) \le \a_i\tp\x^{*} + tM < \a_i\tp\x^{*} + \delta \le b_i .
\]
So \( \z_t \in P \). But
\[
\c\tp\z_t = \c\tp\x^{*} + t(\c\tp\x^{*} - \c\tp\y) = \beta + t(\beta - \c\tp\y) > \beta ,
\]
since \( t > 0 \) and \( \beta - \c\tp\y > 0 \). This contradicts the validity of \( \c\tp\x \le \beta \) on \( P \). Hence \( \c\tp\y = \beta \) and \( \y \in F \), so \( P_J \subseteq F \) and \( F = P_J \).

(c) There are \( 2^m \) subsets \( J \), so by (b) at most that many non-empty faces. Each of them is a polyhedron by (a), and the empty face is the polyhedron \( \{\x : 0 \le -1\} \). This proves the proposition.
:::

The map \( J \mapsto P_J \) is onto the non-empty faces but is very far from injective: adding to \( J \) a row that is already tight everywhere on \( P_J \) changes nothing, and adding two incompatible rows gives \( \emptyset \).

::: {.warning}
**A row of the system need not be a side of the solid.** In \( P = \{\x \in \nR^2 : x_1 \le 1,\ x_2 \le 1,\ x_1 + x_2 \le 3\} \) the third row is implied by the first two, since \( x_1 + x_2 \le 2 \) on \( P \). It defines no face except the empty one: \( P_{\{3\}} = \{\x \in P : x_1 + x_2 = 3\} = \emptyset \). So a polyhedron with \( m \) rows can have far fewer than \( m \) sides, and counting rows is not counting geometry. Conversely, @def-polyhedron-face never mentions the rows at all, which is why @prp-face-is-polyhedron has to prove that the faces can be read off them.
:::

## Vertices, edges, facets

A non-empty face \( F \) is a non-empty convex set, so it has a dimension: \( \dim F = \dim \operatorname{aff} F \), as in Chapter 18 §01, and \( \operatorname{aff} F \) is the flat \( \p + U \) of @prp-affine-hull-coset — a flat in the sense of @def-flat. The graded vocabulary follows.

::: {#def-edge-and-facet}
[Edge, Facet]

Let \( P \subseteq \nR^n \) be a non-empty polyhedron. A face of \( P \) of dimension \( 1 \) is an **edge**; a face of dimension \( \dim P - 1 \) is a **facet**. A face of dimension \( 0 \) is a single point, and the next proposition shows that these are exactly the vertices.
:::

::: {#prp-vertex-iff-point-face}
[Three Descriptions of a Corner]

Let \( P = \{\x \in \nR^n : \A\x \le \b\} \) and \( \v \in P \). The following are equivalent.

::: {.enumerate options="label=(\alph*)"}
1. \( \v \) is a vertex of \( P \), that is, an extreme point.
2. \( \{\v\} \) is a face of \( P \).
3. Among the rows active at \( \v \) there are \( n \) linearly independent ones, that is, \( \v \) is a basic feasible point.
:::
:::

::: {.idea}
(a) and (c) are @thm-vertices-basic-feasible, already proved. A one-point face is an extreme point by @prp-exposed-face (b). For the remaining implication, take \( J \) to be the active set: if the active rows have rank \( n \), the system \( \A_J\x = \b_J \) has \( \v \) as its only solution, so \( P_J = \{\v\} \), and @prp-face-is-polyhedron makes that a face.
:::

::: {.proof}
(a) \( \Leftrightarrow \) (c) is @thm-vertices-basic-feasible.

(b) \( \Rightarrow \) (a). Write \( \{\v\} = \{\x \in P : \c\tp\x = \beta\} \) with \( \c\tp\x \le \beta \) on \( P \). By @prp-exposed-face (b), applied with \( \w = \c \) and \( \alpha = \beta \), \( \v \in \operatorname{ext} P \).

(c) \( \Rightarrow \) (b). Let \( I = I(\v) \) be the active set and \( \A_I \) the matrix of active rows, of rank \( n \) by hypothesis. Its null space is \( \{\0\} \) by @thm-rank-nullity-matrix, so \( \A_I\x = \b_I \) has at most one solution; since \( \v \) is one, it is the only one. Hence
\[
P_I = \{\x \in P : \A_I\x = \b_I\} = \{\v\} ,
\]
and \( P_I \) is a face by @prp-face-is-polyhedron (a). This proves the equivalence.
:::

So a corner of a polyhedron can be recognized three ways: by convexity (it is not an average), by geometry (a hyperplane touches \( P \) there and nowhere else), or by algebra (enough constraints are tight). The three are used interchangeably from here on.

Bounded polyhedra are the ones with enough corners to rebuild them. This is the bounded half of the Minkowski–Weyl theorem, and it is the sentence this whole section is arranged around.

::: {#thm-polytope-is-hull-of-vertices}
[A Bounded Polyhedron Is the Hull of Its Vertices]

Let \( P \subseteq \nR^n \) be a bounded polyhedron. Then \( \operatorname{ext} P \) is finite and
\[
P = \conv(\operatorname{ext} P) .
\]
Conversely, every polytope is a bounded polyhedron.
:::

::: {.proof}
If \( P = \emptyset \), both sides are \( \emptyset \) and \( \operatorname{ext}P = \emptyset \). Otherwise \( P \) is closed and convex by @prp-polyhedron-closed-convex, and bounded by hypothesis, so it is compact by @cor-closed-bounded-compact. By @thm-minkowski-extreme, \( P = \conv(\operatorname{ext} P) \), and \( \operatorname{ext} P \) is finite by @cor-finitely-many-vertices. The converse is @thm-minkowski-weyl (a).
:::

The same theorem applied to a face is what makes an edge a segment between two corners — the statement that lets one speak of walking along the edges of a solid.

::: {#prp-edge-is-segment}
[An Edge Joins Two Vertices]

Let \( P \subseteq \nR^n \) be a bounded polyhedron and \( F \) an edge of \( P \). Then \( F = [\v, \w] \) for two distinct vertices \( \v, \w \) of \( P \).
:::

::: {.idea}
An edge is itself a bounded polyhedron, so it is the hull of its own vertices; those are vertices of \( P \) because a face passes extremeness upwards. Being \( 1 \)-dimensional, it sits on a line, and the hull of finitely many points of a line is the segment between the outermost two.
:::

::: {.proof}
By @prp-face-is-polyhedron, \( F \) is a polyhedron, and it is bounded because \( F \subseteq P \). By @thm-polytope-is-hull-of-vertices, \( F = \conv(\operatorname{ext} F) \) with \( \operatorname{ext} F \) finite, and \( F \ne \emptyset \) since it has a dimension. By the remark after @def-polyhedron-face, \( F \) is a face of \( P \) in the sense of @def-face, so @lem-extreme-points-of-face gives \( \operatorname{ext} F = F \cap \operatorname{ext} P \): every vertex of \( F \) is a vertex of \( P \).

Fix \( \p \in F \). By @prp-affine-hull-coset, \( \operatorname{aff} F = \p + U \) with \( U = \Span\{\x - \p : \x \in F\} \), and \( \dim U = \dim F = 1 \), so \( U = \Span(\u) \) for some \( \u \ne \0 \). Every point of \( F \) lies in \( \operatorname{aff}F \), hence is \( \p + t\u \) for exactly one \( t \in \nR \), the map \( t \mapsto \p + t\u \) being injective because \( \u \ne \0 \). Let \( t_1 \le \dots \le t_k \) be the parameters of the points of \( \operatorname{ext} F \), a non-empty finite list. A convex combination \( \sum_j s_j(\p + t_j\u) \) equals \( \p + (\sum_j s_jt_j)\u \), and \( \sum_j s_jt_j \) lies in \( [t_1, t_k] \); conversely each \( t \in [t_1, t_k] \) is \( (1-\lambda)t_1 + \lambda t_k \) for some \( \lambda \in [0,1] \). Hence, writing \( [\v, \w] \) for the segment of Chapter 18 §01,
\[
F = \{\p + t\u : t_1 \le t \le t_k\} = [\v, \w], \qquad \v = \p + t_1\u,\ \ \w = \p + t_k\u .
\]
If \( t_1 = t_k \) then \( F \) is a single point and \( \dim F = 0 \), contrary to hypothesis; so \( \v \ne \w \), and both are vertices of \( P \). This proves the proposition.
:::

## Two face lattices, computed

Faces are ordered by inclusion, and the resulting picture — which face lies in which — is the **face lattice** of the polyhedron. It is the combinatorial skeleton of the solid. Here it is in full for the two standard examples.

::: {#exm-cube-face-lattice}
[The faces of a cube]

Let \( B_\infty = [-1, 1]^n \), described by the \( 2n \) rows \( \e_i\tp\x \le 1 \) and \( -\e_i\tp\x \le 1 \). Find all faces of \( B_\infty \) and their dimensions.
:::

::: {.solution}
By @prp-face-is-polyhedron (b) every non-empty face is some \( P_J \). A set \( J \) of rows says, for each coordinate \( i \), either nothing, or \( x_i = 1 \), or \( x_i = -1 \), or both; the last makes \( P_J = \emptyset \). So the non-empty faces are indexed by **sign vectors** \( \s \in \{-1, 0, 1\}^n \):
\[
F_{\s} = \{\x \in B_\infty : x_i = s_i \text{ for every } i \text{ with } s_i \ne 0\} .
\]
Each \( F_{\s} \) is non-empty: the point with \( x_i = s_i \) where \( s_i \ne 0 \) and \( x_i = 0 \) elsewhere lies in it. Distinct sign vectors give distinct faces, because \( s_i = \pm 1 \) exactly when the coordinate \( x_i \) is constantly \( \pm 1 \) on \( F_{\s} \). So \( B_\infty \) has exactly \( 3^n \) non-empty faces, one for each sign vector, together with \( \emptyset \).

Let \( Z = \{i : s_i = 0\} \) and \( z = \lvert Z\rvert \). Then \( \operatorname{aff} F_{\s} \) is the flat \( \{\x : x_i = s_i \text{ for } i \notin Z\} \), a coset of \( \Span\{\e_i : i \in Z\} \): it contains \( F_{\s} \), and conversely \( F_{\s} \) contains the point \( \p \) with \( p_i = s_i \) for \( i \notin Z \) and \( p_i = 0 \) for \( i \in Z \), together with \( \p + \e_i \) for every \( i \in Z \), whose differences from \( \p \) span \( \Span\{\e_i : i \in Z\} \). By @prp-affine-hull-coset, \( \dim F_{\s} = z \).

So the faces of dimension \( k \) are the sign vectors with exactly \( k \) zeros, and there are \( \binom{n}{k}2^{n-k} \) of them. For \( n = 3 \): \( 8 \) vertices (\( k = 0 \)), \( 12 \) edges (\( k = 1 \)), \( 6 \) facets (\( k = 2 \)) and the cube itself, and \( 8 + 12 + 6 + 1 = 27 = 3^3 \). Every vertex is a sign vector \( \pm 1 \) in each coordinate, matching what @exm-cube-cross-polytope found by the rank test.
:::

Here is the resulting lattice for the square \( B_\infty \subseteq \nR^2 \), with \( \emptyset \) at the bottom and the square at the top, and a line drawn when the lower face is contained in the upper one.

\begin{center}
\begin{tikzpicture}[scale=1.0, every node/.style={font=\footnotesize}]
  \node (E) at (0,0) {$\emptyset$};
  \node (v1) at (-3,1.4) {$(-1,-1)$};
  \node (v2) at (-1,1.4) {$(1,-1)$};
  \node (v3) at (1,1.4) {$(-1,1)$};
  \node (v4) at (3,1.4) {$(1,1)$};
  \node (e1) at (-3,2.8) {$x_2 = -1$};
  \node (e2) at (-1,2.8) {$x_1 = -1$};
  \node (e3) at (1,2.8) {$x_1 = 1$};
  \node (e4) at (3,2.8) {$x_2 = 1$};
  \node (T) at (0,4.2) {$B_\infty$};
  \foreach \nd in {v1,v2,v3,v4} \draw[gray] (E) -- (\nd);
  \draw (v1) -- (e1); \draw (v1) -- (e2);
  \draw (v2) -- (e1); \draw (v2) -- (e3);
  \draw (v3) -- (e2); \draw (v3) -- (e4);
  \draw (v4) -- (e3); \draw (v4) -- (e4);
  \foreach \nd in {e1,e2,e3,e4} \draw[gray] (\nd) -- (T);
  \node[align=center] at (0,-1.1)
    {The face lattice of the square: one empty face, four vertices,\\
     four edges, and the square itself. Nine non-empty faces, $3^2$};
\end{tikzpicture}
\end{center}

::: {#exm-simplex-face-lattice}
[The faces of a simplex]

Let \( \Delta_n = \{\t \in \nR^n : t_i \ge 0,\ \sum_i t_i = 1\} \) be the standard simplex (@def-standard-simplex), described by the \( n \) rows \( -t_i \le 0 \) together with \( \1\tp\t \le 1 \) and \( -\1\tp\t \le -1 \). Find all faces of \( \Delta_n \).
:::

::: {.solution}
The last two rows are tight at every point of \( \Delta_n \), so including them in \( J \) changes nothing. A face is therefore \( P_J \) for \( J \) determined by a set \( S \subseteq \{1, \dots, n\} \) of coordinates forced to zero:
\[
F_S = \{\t \in \Delta_n : t_i = 0 \text{ for every } i \in S\} .
\]
Write \( T = \{1, \dots, n\} \setminus S \). If \( T = \emptyset \) the conditions \( \t = \0 \) and \( \sum_i t_i = 1 \) clash, so \( F_S = \emptyset \). If \( T \ne \emptyset \), then \( F_S \) consists of the vectors \( \t \ge \0 \) supported in \( T \) with \( \sum_{i \in T}t_i = 1 \), which by @thm-convex-hull-combinations is exactly \( \conv\{\e_i : i \in T\} \), a copy of \( \Delta_{\lvert T\rvert} \). Its dimension is \( \lvert T\rvert - 1 \), by the computation of \( \dim\Delta_k \) after @prp-affine-hull-coset. Distinct non-empty \( T \) give distinct faces, since \( \e_i \in F_S \) exactly for \( i \in T \).

So the non-empty faces of \( \Delta_n \) are indexed by the **non-empty subsets** \( T \subseteq \{1, \dots, n\} \), and there are \( 2^n - 1 \) of them: \( n \) vertices, \( \binom n2 \) edges, and so on up to \( \Delta_n \) itself. For \( n = 4 \), the tetrahedron \( \Delta_4 \subseteq \nR^4 \) of dimension \( 3 \) has \( 4 + 6 + 4 + 1 = 15 = 2^4 - 1 \) non-empty faces.
:::

The contrast is the point. The cube's lattice is the set of sign vectors; that of the simplex is the set of non-empty subsets. A cube in dimension \( n \) has \( 2^n \) vertices and \( 2n \) facets; a simplex has \( n \) vertices and \( n \) facets. The cube's corners grow exponentially with \( n \), those of the simplex only linearly.

::: {.check}
How many faces does a triangle in \( \nR^2 \) have, counting the empty face and the triangle itself?
:::

::: {.solution}
Eight: \( \emptyset \), three vertices, three edges, and the triangle. Count directly from @prp-face-is-polyhedron (b), writing the triangle as the polyhedron cut out by its three sides: \( P_{\emptyset} \) is the triangle, each single row gives one side, each pair of rows gives the corner where those two sides meet, and all three rows together give \( \emptyset \). That is \( 1 + 3 + 3 \) non-empty faces, plus \( \emptyset \). The count matches @exm-simplex-face-lattice with \( n = 3 \), whose \( 2^3 - 1 = 7 \) non-empty faces are indexed by the non-empty subsets of the three corners.
:::

## A linear program, seen

Fix \( \c \in \nR^n \) with \( \c \ne \0 \). The level sets \( \{\x : \c\tp\x = \gamma\} \) of the objective are parallel affine hyperplanes, one for each \( \gamma \), and they sweep across \( \nR^n \) as \( \gamma \) grows, moving in the direction \( \c \). Maximizing \( \c\tp\x \) over a polyhedron \( P \) means pushing the sweeping hyperplane as far as it will go while still touching \( P \). Two things can happen: it escapes to infinity, and the program is unbounded; or there is a last hyperplane that touches, and what it touches is a face.

::: {#prp-optimal-set-is-a-face}
[The Optimal Set Is a Face]

Let \( P \subseteq \nR^n \) be a polyhedron, \( \c \in \nR^n \), and suppose \( \c\tp\x \) attains a maximum \( \gamma^{\star} \) on \( P \). Then the set \( F^{\star} \) of maximizers is a non-empty face of \( P \). If \( P \) is bounded, \( F^{\star} \) contains a vertex of \( P \).
:::

::: {.proof}
By the definition of a maximum, \( \c\tp\x \le \gamma^{\star} \) for every \( \x \in P \), and \( F^{\star} = \{\x \in P : \c\tp\x = \gamma^{\star}\} \) is non-empty. That is @def-polyhedron-face verbatim, so \( F^{\star} \) is a face.

Suppose \( P \) is bounded. Then \( F^{\star} \subseteq P \) is a bounded polyhedron by @prp-face-is-polyhedron, and non-empty, so \( \operatorname{ext} F^{\star} \ne \emptyset \) by @thm-polytope-is-hull-of-vertices (a non-empty set is not the hull of the empty set). By the remark after @def-polyhedron-face and @lem-extreme-points-of-face, \( \operatorname{ext} F^{\star} = F^{\star} \cap \operatorname{ext} P \), so any point of \( \operatorname{ext} F^{\star} \) is a vertex of \( P \) lying in \( F^{\star} \).
:::

The last sentence is @cor-linear-max-at-extreme read geometrically, and it says a little more than that corollary: not only is *some* maximizer a vertex, but the *whole* set of maximizers is a face — a single vertex when the optimum is unique, and otherwise an edge or a larger face, up to all of \( P \) when \( \c = \0 \). A linear program with a non-unique optimum has a positive-dimensional optimal face, and every point of it is optimal.

An algorithm now suggests itself: start at a vertex, and as long as some edge leaving it increases the objective, walk along that edge to the vertex at its other end (@prp-edge-is-segment guarantees there is one, when \( P \) is bounded). That is the idea of the **simplex method**, sketched in Chapter 18 §09 after @cor-finitely-many-vertices. **No algorithm is developed here or anywhere in this book:** Chapter 24 is where this book's algorithms live, and it treats the numerical linear algebra of elimination, least squares and eigenvalues, not linear programming. What this section supplies is the geometry an algorithm would exploit.

::: {#exm-lp-geometry}
[A linear program and its picture]

Maximize \( 3x_1 + 2x_2 \) over
\[
P = \{\x \in \nR^2 : x_1 \ge 0,\ x_2 \ge 0,\ x_1 + x_2 \le 5,\ 2x_1 + x_2 \le 8\} .
\]
Find the vertices, the optimum, the optimal face, and the dual optimal solution.
:::

::: {.solution}
Number the rows (1) \( -x_1 \le 0 \), (2) \( -x_2 \le 0 \), (3) \( x_1 + x_2 \le 5 \), (4) \( 2x_1 + x_2 \le 8 \). No two rows are multiples of each other, so each of the \( \binom42 = 6 \) pairs gives one basic point, which we test against the other two rows:
\[
\begin{array}{c|c|l}
\text{pair} & \text{basic point} & \text{verdict} \\ \hline
(1),(2) & (0, 0) & \text{feasible} \\
(1),(3) & (0, 5) & (4)\colon 5 \le 8 \text{: feasible} \\
(1),(4) & (0, 8) & (3)\colon 8 \le 5 \text{ fails} \\
(2),(3) & (5, 0) & (4)\colon 10 \le 8 \text{ fails} \\
(2),(4) & (4, 0) & (3)\colon 4 \le 5 \text{: feasible} \\
(3),(4) & (3, 2) & \text{feasible}
\end{array}
\]
For the last pair, subtracting (3) from (4) gives \( x_1 = 3 \), hence \( x_2 = 2 \). By @prp-vertex-iff-point-face the vertices are \( (0,0) \), \( (0,5) \), \( (4,0) \) and \( (3,2) \). \( P \) is bounded, since \( 0 \le x_1, x_2 \le 5 \) on it, so by @thm-polytope-is-hull-of-vertices it is the quadrilateral \( \conv\{(0,0), (4,0), (3,2), (0,5)\} \).

The objective takes the value \( 0 \) at \( (0,0) \), \( 10 \) at \( (0,5) \), \( 12 \) at \( (4,0) \) and \( 13 \) at \( (3,2) \), so by @prp-optimal-set-is-a-face the maximum is \( 13 \), at \( \x^{\star} = (3,2) \), and the optimal face is \( \{\x \in P : 3x_1 + 2x_2 = 13\} \). Since only one vertex achieves \( 13 \) and the face is the hull of its vertices, the optimal face is the single point \( \{(3,2)\} \): the optimum is unique.

The rows active at \( \x^{\star} \) are (3) and (4), with outer normals \( \a_3 = (1,1) \) and \( \a_4 = (2,1) \). And
\[
\c = (3, 2) = 1\cdot(1,1) + 1\cdot(2,1) = 1\cdot\a_3 + 1\cdot\a_4 ,
\]
so \( \y = (1, 1) \) is a candidate for the dual. In the notation of @def-dual-program, with \( \A \) the rows \( (1,1) \) and \( (2,1) \) and \( \b = (5, 8) \), the dual asks to minimize \( 5y_1 + 8y_2 \) subject to \( y_1 + 2y_2 \ge 3 \), \( y_1 + y_2 \ge 2 \), \( \y \ge \0 \). At \( \y = (1,1) \) both constraints are equalities and the value is \( 5 + 8 = 13 \), which matches. By @cor-duality-certificate (a), \( \x^{\star} \) and \( \y \) are both optimal, and no further checking is needed.
:::

\begin{center}
\begin{tikzpicture}[scale=0.85, lab/.style={font=\small}]
  \fill[black!10] (0,0) -- (4,0) -- (3,2) -- (0,5) -- cycle;
  \draw[->, gray] (-0.5,0) -- (6.4,0) node[above, black, lab] {$x_1$};
  \draw[->, gray] (0,-0.5) -- (0,8.2) node[left, black, lab] {$x_2$};
  \draw[thick] (-0.3,5.3) -- (5.4,-0.4);
  \node[lab, below right] at (5.35,-0.35) {$x_1 + x_2 = 5$};
  \draw[thick] (0.1,7.8) -- (4.45,-0.9);
  \node[lab, right] at (0.15,7.7) {$2x_1 + x_2 = 8$};
  \draw[thick, dashed] (0.334,6.0) -- (4.8,-0.7);
  \node[lab, below left] at (4.55,-0.85) {$3x_1 + 2x_2 = 13$};
  \fill (3,2) circle (0.07);
  \node[lab, below left] at (2.95,1.95) {$\mathbf{x}^{\star}$};
  \draw[->] (3,2) -- (4.4,2.7) node[below right, lab] {$\mathbf{a}_4$};
  \draw[->, very thick] (3,2) -- (4.5,3.0) node[right, lab] {$\mathbf{c}$};
  \draw[->] (3,2) -- (4.1,3.1) node[above, lab] {$\mathbf{a}_3$};
  \node[lab, align=center] at (2.6,-2.4)
    {The feasible quadrilateral, the level line of the objective through\\
     the optimum, and the two active outer normals whose non-negative\\
     combination is $\mathbf{c} = \mathbf{a}_3 + \mathbf{a}_4$};
\end{tikzpicture}
\end{center}

## What the dual variables are, geometrically

The example ended with an identity worth isolating: the objective vector was a **non-negative** combination of the outer normals of the constraints active at the optimum, and the coefficients were the dual optimal solution. That is the geometric content of duality, and Chapter 18 has already done all the work.

Recall Chapter 18 §06's pair of programs, with \( \A \in M_{m\times n}(\nR) \), \( \b \in \nR^m \), \( \c \in \nR^n \):
\[
\begin{aligned}
\text{(P)}\quad &\text{maximize } \c\tp\x \ \text{ subject to } \A\x \le \b,\ \x \ge \0 ; \\
\text{(D)}\quad &\text{minimize } \b\tp\y \ \text{ subject to } \A\tp\y \ge \c,\ \y \ge \0 .
\end{aligned}
\]
The feasible region of (P) is the polyhedron with the \( m \) rows \( \a_i\tp\x \le b_i \) and the \( n \) rows \( (-\e_j)\tp\x \le 0 \). The **outer normal** of a row is the vector on its left-hand side: \( \a_i \) for the \( i \)-th constraint and \( -\e_j \) for the sign constraint on \( x_j \).

::: {#prp-dual-normal-cone}
[Dual Variables Are the Weights of the Active Normals]

Let \( \x^{\star} \) be an optimal solution of (P). Then there are \( \y \in \nR^m \) and \( \s \in \nR^n \) with \( \y \ge \0 \) and \( \s \ge \0 \) such that
\[
\c = \sum_{i=1}^{m} y_i\a_i + \sum_{j=1}^{n} s_j(-\e_j) ,
\]
where \( y_i = 0 \) whenever \( \a_i\tp\x^{\star} < b_i \), and \( s_j = 0 \) whenever \( x^{\star}_j > 0 \). That is, \( \c \) is a non-negative combination of the outer normals of the constraints **active at \( \x^{\star} \)**, and the weights are an optimal solution of (D).
:::

::: {.idea}
Strong duality hands over an optimal \( \y \) for (D); the slack \( \s = \A\tp\y - \c \) is non-negative because \( \y \) is dual feasible, and rearranging is the displayed identity. Complementary slackness is exactly the statement that the weights vanish on the inactive constraints.
:::

::: {.proof}
Since \( \x^{\star} \) is feasible, (P) is feasible, and \( \c\tp\x \le \c\tp\x^{\star} \) for every feasible \( \x \), so (P) is not unbounded. By @thm-strong-duality (b), (D) is therefore feasible, and by @thm-strong-duality (a) both programs have optimal solutions with equal optimal values; let \( \y \) be an optimal solution of (D). Then \( \y \ge \0 \) and \( \A\tp\y \ge \c \), so \( \s \coloneqq \A\tp\y - \c \ge \0 \). Reading the \( j \)-th coordinate of \( \A\tp\y \) as \( \sum_i y_ia_{ij} \), we get \( \A\tp\y = \sum_i y_i\a_i \), and hence
\[
\c = \A\tp\y - \s = \sum_{i=1}^{m}y_i\a_i + \sum_{j=1}^{n}s_j(-\e_j) .
\]
Both \( \x^{\star} \) and \( \y \) are optimal, so @thm-complementary-slackness applies: its condition (i) says \( y_i > 0 \) forces \( (\A\x^{\star})_i = b_i \), which is the contrapositive of "\( \a_i\tp\x^{\star} < b_i \) forces \( y_i = 0 \)"; its condition (ii) says \( x^{\star}_j > 0 \) forces \( (\A\tp\y)_j = c_j \), that is \( s_j = 0 \). This proves the proposition.
:::

So a dual optimal solution is a **certificate written in normals**. The hyperplane \( \{\x : \c\tp\x = \b\tp\y\} \) supports the feasible region at \( \x^{\star} \), by @thm-weak-duality and equality of the optimal values, and @prp-dual-normal-cone says how its normal \( \c \) is assembled from the normals of the facets meeting at \( \x^{\star} \). Increasing \( b_i \) loosens the \( i \)-th constraint, and \( y_i \) **bounds** the gain: the dual feasible region \( \{\y \ge \0 : \A\tp\y \ge \c\} \) does not mention \( \b \) at all, so \( \y \) stays dual feasible when \( b_i \) is raised to \( b_i + \varepsilon \), and @thm-weak-duality then caps the objective of every point feasible for the loosened program at \( \b\tp\y + \varepsilon y_i \), the old optimal value plus \( \varepsilon y_i \). That \( y_i \) is also the **exact** rate of gain, its *shadow price* in the economists' phrase, says more, and this book does not prove it; nothing here uses it, and it can fail. Take \( n = 1 \), \( m = 2 \), \( \A = \begin{psmallmatrix} 1 \\ 1\end{psmallmatrix} \), \( \b = (1,1) \) and \( \c = 1 \), so that (P) maximizes \( x \) subject to \( x \le 1 \) written twice and \( x \ge 0 \). Its optimum is \( 1 \), and \( \y = (1,0) \) is dual feasible with \( \b\tp\y = 1 \), hence dual optimal by @cor-duality-certificate (a); but raising \( b_1 \) leaves the second copy binding and the optimum at \( 1 \), a gain of \( 0 \) against \( y_1 = 1 \). The same pair shows which half of complementary slackness is available: @thm-complementary-slackness (i) says \( y_i > 0 \) forces row \( i \) tight, so a constraint **slack** at the optimum has \( y_i = 0 \), and that is what @prp-dual-normal-cone records. The converse is the trap — here \( y_2 = 0 \) while row \( 2 \) is tight.

## Polyhedra without corners

Boundedness is doing real work in @thm-polytope-is-hull-of-vertices, and the failures are worth seeing.

::: {#exm-slab-no-vertex}
[A slab, and a quadrant]

::: {.enumerate options="label=(\alph*)"}
1. Find the faces of the slab \( S = \{\x \in \nR^3 : 0 \le x_3 \le 1\} \), and its vertices.
2. Show that \( \max\{x_1 + x_2 : \x \in Q\} \) does not exist for the quadrant \( Q = \{\x \in \nR^2 : x_1 \ge 0,\ x_2 \ge 0\} \), although \( Q \) has a vertex.
:::
:::

::: {.solution}
(a) \( S \) has the two rows \( -x_3 \le 0 \) and \( x_3 \le 1 \). By @prp-face-is-polyhedron the non-empty faces are among \( P_\emptyset = S \), \( P_{\{1\}} = \{x_3 = 0\} \), \( P_{\{2\}} = \{x_3 = 1\} \) and \( P_{\{1,2\}} = \emptyset \). So there are three non-empty faces: \( S \) and two parallel planes, of dimensions \( 3 \), \( 2 \), \( 2 \). There is no face of dimension \( 0 \) or \( 1 \). In particular \( S \) has **no vertices**: at any \( \x \in S \) the active rows are among \( \pm\e_3 \), of rank at most \( 1 < 3 \), so @thm-vertices-basic-feasible denies a vertex. Hence \( \conv(\operatorname{ext}S) = \conv\emptyset = \emptyset \ne S \), and @thm-minkowski-extreme indeed needs compactness. Note also that \( \max\{-x_3 : \x \in S\} = 0 \) **is** attained, on the whole face \( \{x_3 = 0\} \), which contains no vertex: the last sentence of @prp-optimal-set-is-a-face needs boundedness too.

(b) The point \( (0,0) \) is a vertex of \( Q \): the two active rows \( -\e_1, -\e_2 \) are independent, so @thm-vertices-basic-feasible applies. It is the only one, since at any other point of \( Q \) at most one row is active. But \( (t, t) \in Q \) for every \( t \ge 0 \) and \( x_1 + x_2 = 2t \) there, so the objective is unbounded above and no maximum exists. A polyhedron can have corners and still have no optimum.
:::

::: {.warning}
**"Vertex" and "corner of the picture" can both be empty words for an unbounded polyhedron.** The slab above is a perfectly ordinary convex solid, closed, with a genuine boundary, and it has no vertices, no edges, and no bounded face. Nothing in this section rebuilds it from finitely many points, and nothing should: by @thm-minkowski-weyl (a) a polyhedron is a polytope exactly when it is bounded. The general finite description of an unbounded polyhedron needs directions as well as points — every non-empty polyhedron is a polytope plus a finitely generated cone — which Chapter 18 derives from @thm-minkowski-weyl (b) in @exr-polytopes-c1, and which is not pursued here.
:::

## Exercises

### A. Check your understanding

:::: {#exr-polyhedra-and-linear-programming-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State @def-polyhedron-face, and say which pair \( (\c, \beta) \) exhibits \( P \) itself as a face and which exhibits \( \emptyset \).
2. True or false: a polyhedron given by \( m \) inequalities in \( \nR^n \) has exactly \( 2^m \) non-empty faces. Justify your answer.
3. Give the three equivalent descriptions of a vertex from @prp-vertex-iff-point-face.
4. True or false: if a linear program over a bounded non-empty polyhedron has two distinct optimal solutions, it has infinitely many. Justify your answer.
5. How many faces of dimension \( 2 \) does the cube \( [-1,1]^4 \) have?
:::
::::

::: {.solution}
(a) A face of a polyhedron \( P \) is a set \( \{\x \in P : \c\tp\x = \beta\} \) for some \( \c, \beta \) with \( \c\tp\x \le \beta \) valid on all of \( P \). The pair \( (\0, 0) \) gives \( F = P \); the pair \( (\0, 1) \) gives \( F = \emptyset \).

(b) False; \( 2^m \) is only an upper bound (@prp-face-is-polyhedron (c)). The map \( J \mapsto P_J \) need not be injective, and some \( P_J \) may be empty. The warning after that proposition has \( m = 3 \) rows in \( \nR^2 \) and only four non-empty faces: the polyhedron, two edges and one vertex.

(c) \( \v \in P \) is a vertex when: it is an extreme point of \( P \); or \( \{\v\} \) is a face of \( P \); or among the rows active at \( \v \) there are \( n \) linearly independent ones.

(d) True. The optimal set is a face (@prp-optimal-set-is-a-face), hence convex, so it contains the whole segment joining the two optimal points, and a segment with distinct ends has infinitely many points.

(e) By @exm-cube-face-lattice with \( n = 4 \), \( k = 2 \): \( \binom42 2^{4-2} = 6\cdot 4 = 24 \).
:::

### B. Practice

:::: {#exr-polyhedra-and-linear-programming-b1}
[B1: Vertices and faces of a region]

Let
\[
P = \{\x \in \nR^2 : x_1 \ge 0,\ x_2 \ge 0,\ x_1 + 2x_2 \le 8,\ 2x_1 + x_2 \le 10\} .
\]
Find all vertices of \( P \), list all of its faces, and maximize \( x_1 + 3x_2 \) over \( P \).
::::

::: {.solution}
Number the rows (1) \( -x_1 \le 0 \), (2) \( -x_2 \le 0 \), (3) \( x_1 + 2x_2 \le 8 \), (4) \( 2x_1 + x_2 \le 10 \). No two are multiples, so each of the six pairs gives a basic point:
\[
\begin{array}{c|c|l}
\text{pair} & \text{point} & \text{verdict} \\ \hline
(1),(2) & (0,0) & \text{feasible} \\
(1),(3) & (0,4) & (4)\colon 4 \le 10 \text{: feasible} \\
(1),(4) & (0,10) & (3)\colon 20 \le 8 \text{ fails} \\
(2),(3) & (8,0) & (4)\colon 16 \le 10 \text{ fails} \\
(2),(4) & (5,0) & (3)\colon 5 \le 8 \text{: feasible} \\
(3),(4) & (4,2) & \text{feasible}
\end{array}
\]
For the last pair, twice (3) minus (4) gives \( 3x_2 = 6 \), so \( x_2 = 2 \) and \( x_1 = 8 - 4 = 4 \). By @prp-vertex-iff-point-face the vertices are \( (0,0) \), \( (0,4) \), \( (5,0) \) and \( (4,2) \), so \( P \) is a quadrilateral, not a pentagon; two of the six basic points are infeasible. \( P \) is bounded (\( 0 \le x_1 \le 5 \), \( 0 \le x_2 \le 4 \) on it), so \( P = \conv\{(0,0), (5,0), (4,2), (0,4)\} \) by @thm-polytope-is-hull-of-vertices.

By @prp-face-is-polyhedron (b) every non-empty face is some \( P_J \). The four singletons give the four edges, computed directly: \( P_{\{1\}} = \{x_1 = 0,\ 0 \le x_2 \le 4\} \); \( P_{\{2\}} = \{x_2 = 0,\ 0 \le x_1 \le 5\} \); \( P_{\{3\}} = \{x_1 + 2x_2 = 8\} \cap P \), where \( x_1 = 8 - 2x_2 \ge 0 \) gives \( x_2 \le 4 \) and \( 2x_1 + x_2 = 16 - 3x_2 \le 10 \) gives \( x_2 \ge 2 \), a segment from \( (4,2) \) to \( (0,4) \); and \( P_{\{4\}} = \{2x_1 + x_2 = 10\} \cap P \), which in the same way is the segment from \( (4,2) \) to \( (5,0) \). The six pairs give \( P_{\{1,2\}} = \{(0,0)\} \), \( P_{\{1,3\}} = \{(0,4)\} \), \( P_{\{2,4\}} = \{(5,0)\} \), \( P_{\{3,4\}} = \{(4,2)\} \), and \( P_{\{1,4\}} = P_{\{2,3\}} = \emptyset \), the two infeasible basic points; every \( J \) with three or more rows gives \( \emptyset \), since no point of \( P \) has three rows active. So \( P \) has ten faces in all: \( \emptyset \), four vertices, four edges and \( P \) itself.

The objective \( x_1 + 3x_2 \) takes the values \( 0 \), \( 5 \), \( 10 \), \( 12 \) at \( (0,0) \), \( (5,0) \), \( (4,2) \), \( (0,4) \). By @prp-optimal-set-is-a-face the maximum is \( 12 \), attained at \( (0,4) \) alone.
:::

:::: {#exr-polyhedra-and-linear-programming-b2}
[B2: Reading the dual off the normals]

For the program of @exr-polyhedra-and-linear-programming-b1 with objective \( x_1 + 3x_2 \), use @prp-dual-normal-cone to write \( \c = (1,3) \) as a non-negative combination of the outer normals of the constraints active at the optimum, and check the resulting dual solution against @cor-duality-certificate.
::::

::: {.solution}
The optimum is \( \x^{\star} = (0,4) \). The active rows there are (1), with outer normal \( -\e_1 = (-1, 0) \), and (3), with outer normal \( \a_3 = (1,2) \). In the notation of @def-dual-program the rows of \( \A \) are (3) and (4) in that order, so the weight on \( \a_3 \) is \( y_1 \). Writing \( \c = y_1\a_3 + s_1(-\e_1) \) with \( \a_3 = (1,2) \):
\[
(1,3) = y_1(1,2) + s_1(-1, 0)
\]
gives \( 2y_1 = 3 \), so \( y_1 = \tfrac32 \), and \( 1 = \tfrac32 - s_1 \), so \( s_1 = \tfrac12 \). Both are non-negative, as @prp-dual-normal-cone requires. Row (4) is inactive at \( \x^{\star} \), so its weight is \( y_2 = 0 \); and \( x^{\star}_2 = 4 > 0 \), so the slack on the second sign constraint is \( s_2 = 0 \).

So \( \A \) has rows \( (1,2) \) and \( (2,1) \), with \( \b = (8, 10) \) and \( \c = (1,3) \). The dual solution read off is \( \y = (\tfrac32, 0) \), which satisfies \( \y \ge \0 \) and
\[
\A\tp\y = \tfrac32(1,2) = \bigl(\tfrac32, 3\bigr) \ge (1,3) = \c ,
\]
so it is dual feasible, with value \( \b\tp\y = 8\cdot\tfrac32 = 12 \). Since the primal value at \( (0,4) \) is also \( 12 \), @cor-duality-certificate (a) confirms that both are optimal.
:::

:::: {#exr-polyhedra-and-linear-programming-b3}
[B3: Faces of the cross-polytope]

Let \( B_1 = \{\x \in \nR^n : \s\tp\x \le 1 \text{ for every sign vector } \s \in \{-1,1\}^n\} \), the cross-polytope of @exm-cube-cross-polytope. Determine the face \( P_J \) for \( J \) a single sign vector \( \s \), and its dimension. How many facets does \( B_1 \) have?
::::

::: {.solution}
For a single sign vector \( \s \), \( P_{\{\s\}} = \{\x \in B_1 : \s\tp\x = 1\} \). Now \( \s\tp\x = \sum_i s_ix_i \le \sum_i\lvert x_i\rvert = \norm{\x}_1 \), term by term, so equality holds exactly when \( s_ix_i = \lvert x_i\rvert \) for every \( i \); and \( \norm{\x}_1 = \max_{\s}\s\tp\x \le 1 \) on \( B_1 \), as @exm-cube-cross-polytope records. So \( \s\tp\x = 1 \) forces \( \norm{\x}_1 = 1 \) and \( s_ix_i = \lvert x_i\rvert \ge 0 \) for every \( i \); conversely those conditions give \( \s\tp\x = \norm{\x}_1 = 1 \). Writing \( \x = \sum_i x_i\e_i \) with \( x_i = s_i\lvert x_i\rvert \), we get
\[
P_{\{\s\}} = \Bigl\{\sum_i t_i(s_i\e_i) : t_i \ge 0,\ \sum_i t_i = 1\Bigr\} = \conv\{s_1\e_1, \dots, s_n\e_n\} ,
\]
using @thm-convex-hull-combinations. This is a copy of \( \Delta_n \), of dimension \( n - 1 \) by the computation after @prp-affine-hull-coset. Since \( \dim B_1 = n \) — it contains \( \0 \) and every \( \pm\e_i \), and the differences \( \e_i - \0 \) span \( \nR^n \), so @prp-affine-hull-coset gives \( \operatorname{aff}B_1 = \nR^n \) — each \( P_{\{\s\}} \) is a facet. Distinct \( \s \) give distinct facets, since \( \s \) is recovered from \( P_{\{\s\}} \) by the signs of the vertices \( s_i\e_i \).

There are no others. Every non-empty face is \( P_J \) for a set \( J \) of sign vectors, by @prp-face-is-polyhedron (b), and if \( \s \ne \s' \) both lie in \( J \) then \( P_J \subseteq P_{\{\s\}} \cap P_{\{\s'\}} \). A point of that intersection has \( x_i = s_i\lvert x_i\rvert = s'_i\lvert x_i\rvert \), so \( x_i = 0 \) whenever \( s_i \ne s'_i \); hence the intersection is \( \conv\{s_i\e_i : s_i = s'_i\} \), of dimension at most \( n - 2 \), since at least one index is missing. So \( B_1 \) has exactly \( 2^n \) facets: in \( \nR^n \) it has \( 2n \) vertices and \( 2^n \) facets, exactly the reverse of the cube.
:::

### C. Going deeper

:::: {#exr-polyhedra-and-linear-programming-c1}
[C1: A face of a face]

Let \( P \) be a polyhedron and \( F \) a face of \( P \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that every face of \( F \) is a face of \( P \).
2. Deduce that the faces of \( P \) contained in a fixed face \( F \) are exactly the faces of \( F \).
:::

*Hint: for (a), use @prp-face-is-polyhedron to write both \( F \) and the face of \( F \) in the form \( P_J \).*
::::

::: {.solution}
(a) We may assume the face \( G \) of \( F \) is non-empty, since \( \emptyset \) is a face of \( P \). Fix a system \( \A\x \le \b \) with \( P = \{\x : \A\x \le \b\} \) and rows \( \a_i\tp\x \le b_i \), \( i = 1, \dots, m \). By @prp-face-is-polyhedron (b), \( F = P_J \) for some \( J \). By part (a) of the same proposition, \( F \) is cut out by the \( m \) original rows together with the rows \( -\a_i\tp\x \le -b_i \) for \( i \in J \). By (b) applied to \( F \) with **this** system, \( G = F_K \) for some set \( K \) of those rows; since the rows \( -\a_i\tp\x \le -b_i \) with \( i \in J \) are tight everywhere on \( F \), including them in \( K \) changes nothing, so we may take \( K \subseteq \{1, \dots, m\} \). Then
\[
G = \{\x \in F : \a_i\tp\x = b_i \text{ for } i \in K\} = \{\x \in P : \a_i\tp\x = b_i \text{ for } i \in J \cup K\} = P_{J \cup K} ,
\]
which is a face of \( P \) by @prp-face-is-polyhedron (a).

(b) By (a), every face of \( F \) is a face of \( P \), and it is contained in \( F \). Conversely let \( G \) be a face of \( P \) with \( G \subseteq F \), say \( G = \{\x \in P : \c\tp\x = \beta\} \) with \( \c\tp\x \le \beta \) on \( P \). Then \( \c\tp\x \le \beta \) holds in particular on \( F \subseteq P \), and
\[
\{\x \in F : \c\tp\x = \beta\} = \{\x \in P : \c\tp\x = \beta\} \cap F = G \cap F = G ,
\]
so \( G \) is a face of \( F \).
:::

:::: {#exr-polyhedra-and-linear-programming-c2}
[C2: The two notions of face agree for a polyhedron]

Let \( P = \{\x \in \nR^n : \A\x \le \b\} \) and let \( F \subseteq P \) be a non-empty face in the sense of @def-face: \( F \) is convex, and whenever \( t\y + (1-t)\z \in F \) with \( \y, \z \in P \) and \( 0 < t < 1 \), both \( \y \) and \( \z \) lie in \( F \).

::: {.enumerate options="label=(\alph*)"}
1. Let \( J = \{i : \a_i\tp\x = b_i \text{ for every } \x \in F\} \). Prove that \( F = P_J \).
2. Deduce that \( F \) is a face in the sense of @def-polyhedron-face, so the two notions agree for polyhedra.
:::

*Hint: for (a), Step 1 of the proof of @prp-face-is-polyhedron produces a point of \( F \) at which every row outside \( J \) is slack; use it as the midpoint of a short segment.*
::::

::: {.solution}
(a) \( F \subseteq P_J \) by the definition of \( J \). For the reverse inclusion, note first that \( F \) is convex, so Step 1 of the proof of @prp-face-is-polyhedron applies verbatim and yields \( \x^{*} \in F \) with \( \a_i\tp\x^{*} < b_i \) for every \( i \notin J \).

Let \( \y \in P_J \). If \( \y = \x^{*} \) we are done, so assume \( \y \ne \x^{*} \) and put \( \z_t = \x^{*} + t(\x^{*} - \y) \) for \( t > 0 \). Exactly as in Step 2 of that proof, \( \a_i\tp\z_t = b_i \) for \( i \in J \) and, for small enough \( t > 0 \), \( \a_i\tp\z_t < b_i \) for \( i \notin J \); so \( \z_t \in P \). Fix such a \( t \). Then
\[
\x^{*} = \frac{t}{1+t}\,\y + \frac{1}{1+t}\,\z_t ,
\]
a combination with positive coefficients adding to \( 1 \): indeed the right side is \( \frac{t\y + \x^{*} + t\x^{*} - t\y}{1+t} = \x^{*} \). Both \( \y \) and \( \z_t \) lie in \( P \) and \( \x^{*} \in F \), so the face property of @def-face forces \( \y \in F \). Hence \( P_J \subseteq F \) and \( F = P_J \).

(b) By @prp-face-is-polyhedron (a), \( P_J \) is a face in the sense of @def-polyhedron-face. Together with the remark after @def-polyhedron-face, which gives the other direction for every face, the two notions coincide on polyhedra.

They do not coincide for general convex sets, and one round set shows it. Let \( D = \{\x \in \nR^2 : \norm{\x} \le 1\} \), let \( \q = (2,0) \), let \( C = \conv(D \cup \{\q\}) \), and put \( \p = \bigl(\tfrac12, \tfrac{\sqrt3}{2}\bigr) \), so that \( \norm{\p} = 1 \) and \( \inner{\p}{\q} = 1 \). Since \( D \) is convex, @thm-convex-hull-combinations writes every point of \( C \) as \( (1-s)\d + s\q \) with \( \d \in D \) and \( s \in [0,1] \), whence
\[
\inner{\p}{(1-s)\d + s\q} = (1-s)\inner{\p}{\d} + s \le (1-s)\norm{\d} + s \le 1 ,
\]
the first inequality by @thm-cauchy-schwarz. Equality with \( s < 1 \) forces \( \inner{\p}{\d} = \norm{\d} = 1 \), hence \( (\p, \d) \) dependent and \( \d = \p \); so \( \{\x \in C : \inner{\p}{\x} = 1\} = [\p, \q] \). Now \( \{\p\} \) **is** a face of \( C \) in the sense of @def-face: if \( \p = t\y + (1-t)\z \) with \( \y, \z \in C \) and \( 0 < t < 1 \), then \( 1 = t\inner{\p}{\y} + (1-t)\inner{\p}{\z} \), and both inner products are at most \( 1 \), so both equal \( 1 \) and \( \y = \p + a(\q - \p) \), \( \z = \p + b(\q - \p) \) with \( a, b \in [0,1] \); then \( ta + (1-t)b = 0 \) forces \( a = b = 0 \). But no supporting hyperplane isolates \( \p \). If \( \inner{\c}{\x} \le \beta \) on \( C \) with \( \inner{\c}{\p} = \beta \), then \( \c \ne \0 \), since \( \c = \0 \) gives the face \( C \) or \( \emptyset \); testing the inequality at the point \( \c/\norm{\c} \) of \( D \) gives \( \norm{\c} \le \beta = \inner{\c}{\p} \le \norm{\c} \), so equality holds in @thm-cauchy-schwarz and \( \c = \norm{\c}\p \), \( \beta = \norm{\c} \). Then \( \inner{\c}{\q} = \norm{\c}\inner{\p}{\q} = \beta \), so \( \q \) lies in the face too, and the face is not \( \{\p\} \).
:::

:::: {#exr-polyhedra-and-linear-programming-c3}
[C3: The optimal face has no better vertex outside it]

Let \( P \subseteq \nR^n \) be a non-empty bounded polyhedron, \( \c \in \nR^n \), and let \( F^{\star} \) be the optimal face of @prp-optimal-set-is-a-face.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( F^{\star} = \conv(F^{\star} \cap \operatorname{ext} P) \).
2. Deduce that the optimal value of the program equals \( \max\{\c\tp\v : \v \in \operatorname{ext}P\} \), a maximum over a finite set, and that this finite maximum is attained exactly at the vertices lying in \( F^{\star} \).
:::
::::

::: {.solution}
(a) \( F^{\star} \) is a non-empty bounded polyhedron by @prp-face-is-polyhedron, so @thm-polytope-is-hull-of-vertices gives \( F^{\star} = \conv(\operatorname{ext}F^{\star}) \). By the remark after @def-polyhedron-face, \( F^{\star} \) is a face of \( P \) in the sense of @def-face, so @lem-extreme-points-of-face gives \( \operatorname{ext}F^{\star} = F^{\star} \cap \operatorname{ext}P \). Substituting proves (a).

(b) By @cor-finitely-many-vertices, \( \operatorname{ext}P \) is finite, and it is non-empty by @thm-polytope-is-hull-of-vertices since \( P \ne \emptyset \). Write \( \gamma^{\star} \) for the optimal value. Every vertex lies in \( P \), so \( \c\tp\v \le \gamma^{\star} \) for \( \v \in \operatorname{ext}P \); and by (a) \( F^{\star} \) contains a vertex, at which \( \c\tp\v = \gamma^{\star} \). So the finite maximum equals \( \gamma^{\star} \). A vertex \( \v \) attains it exactly when \( \c\tp\v = \gamma^{\star} \), which is exactly the condition \( \v \in F^{\star} \) defining the optimal face.
:::
