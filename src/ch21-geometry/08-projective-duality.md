# Duality

Two facts about the projective plane sit side by side. Two distinct points lie on exactly one line; two distinct lines meet in exactly one point. Read either sentence aloud with "point" and "line" exchanged and you get the other. This is not a coincidence and it is not a philosophy: Chapter 4 already built the machine that produces it. A hyperplane of \( \nP(V) \) is the set of points killed by a linear functional, the functional is determined by the hyperplane up to a scalar, and so the hyperplanes of \( \nP(V) \) are themselves the points of a projective space, namely \( \nP(V^{*}) \). This section turns that observation into an inclusion-reversing dictionary between the projective subspaces of \( \nP(V) \) and those of \( \nP(V^{*}) \), gets the dimension bookkeeping right at both ends, and says exactly how much of the "duality principle" we are entitled to claim.

Throughout, \( F \) is an arbitrary field and \( V \) is a finite-dimensional vector space over \( F \) with \( \dim V = n + 1 \ge 1 \), so that \( \nP(V) \) has dimension \( n \) (@def-projective-space). No hypothesis on the characteristic is needed anywhere in this section, and no analysis is used. We keep the two extreme projective subspaces in play: \( \nP(\{\0\}) = \emptyset \), of dimension \( -1 \), and \( \nP(V) \) itself, of dimension \( n \). The correspondence below exchanges them, and it is precisely at those two ends that a duality argument is easiest to get wrong.

## Projective subspaces remember their subspaces

Everything rests on being able to move between a projective subspace \( \nP(U) \) and the subspace \( U \) it came from. That is the content of a short lemma, proved in Section 6 and recalled here because almost every proof below uses it.

::: {#lem-projective-subspaces-and-subspaces}
[Passing Between \( U \) and \( \nP(U) \)]

Let \( U, U_1, U_2 \) be subspaces of \( V \).

::: {.enumerate options="label=(\alph*)"}
1. \( \nP(U_1) \subseteq \nP(U_2) \) if and only if \( U_1 \subseteq U_2 \). In particular \( U \mapsto \nP(U) \) is injective, so a projective subspace determines its subspace.
2. \( \nP(U_1 \cap U_2) = \nP(U_1) \cap \nP(U_2) \).
3. \( \nP(U_1) \vee \nP(U_2) = \nP(U_1 + U_2) \), where \( \vee \) is the join, the smallest projective subspace containing both (@prp-join-and-meet).
:::
:::

::: {.proof}
Part (a) is @lem-projective-subspace-determines-subspace, and parts (b) and (c) are @prp-join-and-meet (a) and (b), the latter being where \( \vee \) was defined.
:::

One consequence will be used repeatedly: if \( S \subseteq T \) are projective subspaces of the same finite dimension, then \( S = T \). Indeed \( U_S \subseteq U_T \) by (a) and \( \dim U_S = \dim U_T \), so \( U_S = U_T \) by @thm-dim-impl-eq.

## The points of the dual space are the hyperplanes

A **hyperplane** of \( \nP(V) \) is a projective subspace of dimension \( n - 1 \), that is, \( \nP(H) \) for a hyperplane \( H \) of \( V \) in the sense of @def-hyperplane. In \( \nP^2 \) these are the lines; in \( \nP^3 \), the planes.

Now the hook. A hyperplane of \( V \) is the kernel of a non-zero functional (@thm-hyperplane-kernel-functional), and the functional is determined by its kernel up to a scalar, which is the injectivity half of the next proposition. "A non-zero vector of \( V^{*} \), up to a non-zero scalar" is exactly the description of a point of \( \nP(V^{*}) \). So the hyperplanes of \( \nP(V) \) are not merely a set: they are the points of a projective space of their own, of the same dimension.

*The dual projective space is the space whose points are the hyperplanes of the original.*

::: {#def-dual-projective-space}
[Dual Projective Space]

Let \( V \) be a finite-dimensional vector space over \( F \) with \( \dim V = n + 1 \ge 1 \). The **dual projective space** of \( \nP(V) \) is the projective space
\[
\nP(V^{*})
\]
of the dual space \( V^{*} \) (@def-dual-space). A point of \( \nP(V^{*}) \) is a class \( [\varphi] \) with \( \varphi \in V^{*} \) **non-zero**, and \( [\varphi] = [\psi] \) exactly when \( \psi = \lambda\varphi \) for some \( \lambda \in F \setminus \{0\} \).
:::

Its dimension is \( \dim V^{*} - 1 = n \), by @cor-dimension-dual-space: *the dual projective space has the same dimension as the original.* That is worth pausing on, because the correspondence we are about to build reverses dimensions inside a space of unchanged size.

**Non-example by minimal change.** Take \( \varphi = 0 \). It is a perfectly good element of \( V^{*} \), but \( [\,0\,] \) is not a point of \( \nP(V^{*} ) \) — the definition excludes the zero vector, as @def-projective-space does. And indeed \( \ker 0 = V \), which is not a hyperplane: it has codimension \( 0 \), not \( 1 \) (@def-hyperplane). The clause "non-zero" is exactly what keeps the following bijection honest.

::: {#prp-points-of-dual-are-hyperplanes}
[Points of the Dual Are Hyperplanes]

Let \( \dim V = n + 1 \ge 1 \). The map
\[
[\varphi] \longmapsto \nP(\ker\varphi)
\]
is a well-defined bijection from \( \nP(V^{*}) \) onto the set of hyperplanes of \( \nP(V) \).
:::

::: {.idea}
Three checks. Well defined: proportional functionals have the same kernel. Surjective: a hyperplane \( \nP(H) \) has \( \dim H^{0} = 1 \) by the annihilator count, so it is cut out by some non-zero functional. Injective: two functionals with the same kernel \( H \) both lie in the one-dimensional space \( H^{0} \), so they are proportional. The counting does all the work.
:::

::: {.proof}
*Well defined.* If \( \varphi \ne 0 \) then \( \ker\varphi \) is a hyperplane of \( V \) by @thm-hyperplane-kernel-functional, so \( \nP(\ker\varphi) \) is a projective subspace of dimension \( \dim\ker\varphi - 1 = n - 1 \), a hyperplane of \( \nP(V) \). If \( [\psi] = [\varphi] \), then \( \psi = \lambda\varphi \) with \( \lambda \ne 0 \), and \( \psi(\v) = 0 \) if and only if \( \varphi(\v) = 0 \), so \( \ker\psi = \ker\varphi \).

*Surjective.* Let \( \nP(H) \) be a hyperplane of \( \nP(V) \), so \( \dim H = n \). By @thm-dimension-annihilator, \( \dim H^{0} = (n+1) - n = 1 \), so there is a non-zero \( \varphi \in H^{0} \). Then \( H \subseteq \ker\varphi \) by @def-annihilator, and both have dimension \( n \) — the second by @thm-hyperplane-kernel-functional and @thm-dimension-quotient — so \( H = \ker\varphi \) by @thm-dim-impl-eq.

*Injective.* Suppose \( \ker\varphi = \ker\psi = H \) with \( \varphi, \psi \ne 0 \). Then \( \varphi, \psi \in H^{0} \), which has dimension \( 1 \) as above. Two non-zero vectors of a one-dimensional space are proportional, so \( \psi = \lambda\varphi \) with \( \lambda \ne 0 \), that is, \( [\psi] = [\varphi] \).
:::

In coordinates this is completely concrete. Take \( V = F^{n+1} \) with coordinates \( x_0, \dots, x_n \). By @thm-functionals-on-fn every functional is \( \varphi_{\a}(\x) = a_0x_0 + \dots + a_nx_n \) for a unique \( \a \in F^{n+1} \), and this identification is a linear isomorphism \( F^{n+1} \to (F^{n+1})^{*} \). So a point of the dual plane is a class \( [a_0 : \dots : a_n] \), and the hyperplane it names is
\[
\{\,[\x] \in \nP^n(F) \ :\ a_0x_0 + \dots + a_nx_n = 0\,\} .
\]
The equation is homogeneous, so it does not matter which representative \( \x \) we substitute; and scaling \( \a \) does not change the solution set. Both scalings are exactly the ones the projective spaces divide out.

::: {#exm-line-and-its-dual-point}
[A line and its point]

In \( \nP^2(\nQ) \), find the point of the dual plane naming the line through \( [1:1:0] \) and \( [0:1:1] \). Then find the point where the lines \( x_0 - x_1 + x_2 = 0 \) and \( x_0 + x_2 = 0 \) meet.
:::

::: {.solution}
*The line.* Its subspace is \( U = \Span\bigl((1,1,0), (0,1,1)\bigr) \), of dimension \( 2 \). By @thm-dimension-annihilator, \( \dim U^{0} = 3 - 2 = 1 \), so one non-zero functional does it. We need \( a_0 + a_1 = 0 \) and \( a_1 + a_2 = 0 \), whose solutions are the multiples of \( \a = (1, -1, 1) \). Check: \( 1 - 1 + 0 = 0 \) and \( 0 - 1 + 1 = 0 \). So the line is \( x_0 - x_1 + x_2 = 0 \), named by the dual point \( [1 : -1 : 1] \).

*The meet.* Dually, we need \( \x \) with \( x_0 - x_1 + x_2 = 0 \) and \( x_0 + x_2 = 0 \). Subtracting, \( x_1 = 0 \); then \( x_0 = -x_2 \). The solution space is spanned by \( (-1, 0, 1) \), so the two lines meet in the single point \( [-1:0:1] \). Check: \( -1 - 0 + 1 = 0 \) and \( -1 + 1 = 0 \).

The two computations are the same computation, run in \( V \) and in \( V^{*} \). That is the whole of duality in one example.
:::

::: {.warning}
**There is no canonical duality between \( \nP(V) \) and itself.** The rule "the point \( [a_0 : a_1 : a_2] \) names the line \( a_0x_0 + a_1x_1 + a_2x_2 = 0 \)" looks like a self-duality of \( \nP^2(F) \), but it depends on the coordinates. In \( \nP^2(\nQ) \) the rule assigns to \( [1:0:1] \) the line \( x_0 + x_2 = 0 \). Change coordinates by \( y_0 = x_0 \), \( y_1 = x_1 \), \( y_2 = 2x_2 \). The same point is \( [1:0:2] \) in the new coordinates, and the same rule now assigns to it the line \( y_0 + 2y_2 = 0 \), that is, \( x_0 + 4x_2 = 0 \). These are different lines: the point \( [1:0:-1] \) lies on the first, since \( 1 - 1 = 0 \), and not on the second, since \( 1 - 4 = -3 \ne 0 \). What is canonical is the correspondence between \( \nP(V) \) and \( \nP(V^{*}) \), not one between \( \nP(V) \) and itself. Identifying the two requires a choice — a basis, or a non-degenerate form, which is how the pole and polar of a conic will be built in Section 10 of this chapter.
:::

## The duality correspondence

We now extend \( [\varphi] \mapsto \nP(\ker\varphi) \) from hyperplanes to all projective subspaces. The right tool is the annihilator, and we keep Chapter 4's notation: for a subspace \( U \subseteq V \), \( U^{0} = \{\varphi \in V^{*} : \varphi(\u) = 0 \text{ for all } \u \in U\} \) (@def-annihilator).

For a projective subspace \( S = \nP(U) \) of \( \nP(V) \), define
\[
S^{0} \coloneqq \nP\bigl(U^{0}\bigr) \subseteq \nP(V^{*}) .
\]
This is well defined because \( S \) determines \( U \), by @lem-projective-subspaces-and-subspaces (a).

Before the theorem, the dimension bookkeeping, because it is the step where such a correspondence is usually stated wrongly. Projective dimension is one less than linear dimension. So from \( \dim U + \dim U^{0} = n+1 \) we get
\[
(\dim S + 1) + (\dim S^{0} + 1) = n + 1, \qquad\text{that is}\qquad \dim S^{0} = n - 1 - \dim S .
\]
Test it at both ends. If \( S = \emptyset \), so \( U = \{\0\} \) and \( \dim S = -1 \), the formula gives \( \dim S^{0} = n \), and indeed \( \{\0\}^{0} = V^{*} \), so \( S^{0} = \nP(V^{*}) \). If \( S = \nP(V) \), with \( \dim S = n \), the formula gives \( -1 \), and indeed \( V^{0} = \{0\} \), so \( S^{0} = \emptyset \). A point (\( \dim S = 0 \)) goes to a hyperplane (\( \dim S^{0} = n-1 \)), and a hyperplane goes to a point, agreeing with @prp-points-of-dual-are-hyperplanes. The formula is symmetric in the sense that \( d \mapsto n - 1 - d \) is its own inverse on \( \{-1, 0, \dots, n\} \).

::: {#thm-duality-correspondence}
[The Duality Correspondence]

Let \( \dim V = n + 1 \ge 1 \), and let \( S, T \) be projective subspaces of \( \nP(V) \), the empty set and \( \nP(V) \) included. Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \dim S^{0} = n - 1 - \dim S \);
2. \( S \subseteq T \) if and only if \( T^{0} \subseteq S^{0} \);
3. \( (S \vee T)^{0} = S^{0} \cap T^{0} \) and \( (S \cap T)^{0} = S^{0} \vee T^{0} \);
4. \( S \mapsto S^{0} \) is a bijection from the set of projective subspaces of \( \nP(V) \) onto the set of projective subspaces of \( \nP(V^{*}) \).
:::
:::

::: {.idea}
Every part is a Chapter 4 statement about annihilators, translated through @lem-projective-subspaces-and-subspaces, with the dimension shifted by one at each end. The only part that needs thought is the reverse implication in (b) and the surjectivity in (d): both go up a level to \( V^{**} \) and come back with @cor-annihilator-of-annihilator, which is available because \( V \) is finite-dimensional.
:::

::: {.proof}
Write \( S = \nP(U) \) and \( T = \nP(U') \), which is legitimate and unambiguous by @lem-projective-subspaces-and-subspaces (a).

(a) By @thm-dimension-annihilator, \( \dim U^{0} = (n+1) - \dim U \). Hence
\[
\dim S^{0} = \dim U^{0} - 1 = n - \dim U = n - (\dim S + 1) = n - 1 - \dim S .
\]

(b) \( (\Rightarrow) \) If \( S \subseteq T \), then \( U \subseteq U' \) by @lem-projective-subspaces-and-subspaces (a), so \( (U')^{0} \subseteq U^{0} \) by @thm-annihilator-properties (a), so \( T^{0} \subseteq S^{0} \) by the same lemma. \( (\Leftarrow) \) Suppose \( T^{0} \subseteq S^{0} \), so \( (U')^{0} \subseteq U^{0} \). Applying @thm-annihilator-properties (a) inside \( V^{*} \) gives \( U^{00} \subseteq (U')^{00} \). By @cor-annihilator-of-annihilator, \( U^{00} = \ev_V(U) \) and \( (U')^{00} = \ev_V(U') \), so \( \ev_V(U) \subseteq \ev_V(U') \). Since \( \ev_V \) is injective (@thm-double-dual-isomorphism), \( U \subseteq U' \), and \( S \subseteq T \).

(c) By @lem-projective-subspaces-and-subspaces (c), \( S \vee T = \nP(U + U') \), and \( (U + U')^{0} = U^{0} \cap (U')^{0} \) by @thm-annihilator-properties (c). Applying \( \nP(\cdot) \) and @lem-projective-subspaces-and-subspaces (b),
\[
(S \vee T)^{0} = \nP\bigl(U^{0} \cap (U')^{0}\bigr) = \nP(U^{0}) \cap \nP\bigl((U')^{0}\bigr) = S^{0} \cap T^{0} .
\]
For the second identity, \( S \cap T = \nP(U \cap U') \) by @lem-projective-subspaces-and-subspaces (b), and \( (U \cap U')^{0} = U^{0} + (U')^{0} \) by @thm-annihilator-properties (d), which needs \( V \) finite-dimensional. Applying \( \nP(\cdot) \) and part (c) of the same lemma gives \( (S \cap T)^{0} = S^{0} \vee T^{0} \).

(d) *Injective.* If \( S^{0} = T^{0} \) then \( U^{0} = (U')^{0} \) by @lem-projective-subspaces-and-subspaces (a), so \( U = U' \) by @cor-subspaces-determined-by-annihilator, so \( S = T \).

*Surjective.* Let \( R = \nP(W) \) be a projective subspace of \( \nP(V^{*} ) \), where \( W \) is a subspace of \( V^{*} \). Put
\[
U \coloneqq \ev_V^{-1}\bigl(W^{0}\bigr) = \{\v \in V : \varphi(\v) = 0 \text{ for every } \varphi \in W\},
\]
a subspace of \( V \): it is the intersection of the kernels \( \ker\varphi \) over \( \varphi \in W \), each a subspace by @thm-prop-kernel, and an intersection of subspaces is a subspace by @thm-intersection-subspaces. Since \( \ev_V \) is surjective (@thm-double-dual-isomorphism), \( \ev_V(U) = W^{0} \). By @cor-annihilator-of-annihilator, \( (U^{0})^{0} = U^{00} = \ev_V(U) = W^{0} \). Now \( U^{0} \) and \( W \) are subspaces of the finite-dimensional space \( V^{*} \) with the same annihilator, so \( U^{0} = W \) by @cor-subspaces-determined-by-annihilator applied in \( V^{*} \). Hence \( \nP(U)^{0} = \nP(W) = R \). This proves the theorem.
:::

::: {.check}
Let \( S \) be a line in \( \nP^3(F) \). What is \( \dim S^{0} \), and what kind of object is \( S^{0} \)? What if \( S \) is a point?
:::

::: {.solution}
Here \( n = 3 \) and \( \dim S = 1 \), so \( \dim S^{0} = 3 - 1 - 1 = 1 \) by @thm-duality-correspondence (a): \( S^{0} \) is again a line, this time in the dual space \( \nP((F^4)^{*}) \). Lines in \( \nP^3 \) are self-dual in dimension, which is one reason they are the interesting objects there. If instead \( S \) is a point, \( \dim S = 0 \) and \( \dim S^{0} = 3 - 1 - 0 = 2 \): a plane in the dual space. Concretely, it is the set of all planes of \( \nP^3 \) through that point.
:::

::: {.remark}
The last sentence of the solution is the general reading of the correspondence. Since \( S \subseteq P \) if and only if \( P^{0} \subseteq S^{0} \), the hyperplanes containing \( S \) are exactly the points of \( S^{0} \): *a projective subspace is named, on the dual side, by the family of hyperplanes that contain it.* For a point, that family is a hyperplane's worth of hyperplanes.
:::

\begin{center}
\begin{tikzpicture}[scale=1.05, lab/.style={font=\small}, pt/.style={circle, fill=black, inner sep=1.4pt}]
    % left panel: the pencil of lines through P
    \draw[black!70] (-1.5,0) -- (1.5,0);
    \draw[black!70] (-1.214,-0.881) -- (1.214,0.881);
    \draw[black!70] (-0.464,-1.427) -- (0.464,1.427);
    \draw[black!70] (0.464,-1.427) -- (-0.464,1.427);
    \draw[black!70] (1.214,-0.881) -- (-1.214,0.881);
    \node[pt] at (0,0) {};
    \node[lab] at (0.52,-0.72) {$P$};
    \node[lab] at (0,-2.05) {in $\nP(V)$};
    % arrow
    \draw[->, thick] (2.1,0) -- (4.1,0);
    \node[lab, above] at (3.1,0.1) {$L \mapsto L^{0}$};
    % right panel: the points of P^0 on a line
    \draw[black!70] (4.8,-0.98) -- (7.9,0.88);
    \node[pt] at (5.265,-0.701) {};
    \node[pt] at (5.73,-0.422) {};
    \node[pt] at (6.35,-0.05) {};
    \node[pt] at (6.97,0.322) {};
    \node[pt] at (7.435,0.601) {};
    \node[lab, below right] at (7.95,0.88) {$P^{0}$};
    \node[lab] at (6.35,-2.05) {in $\nP(V^{*})$};
    \node[lab, align=center] at (3.1,-2.85)
      {each line $L$ through $P$ is one point $L^{0}$ of the dual plane,\\ and those points fill the line $P^{0}$};
\end{tikzpicture}
\end{center}

## Dualizing twice

Applying the correspondence twice lands in \( \nP(V^{**}) \), not back in \( \nP(V) \). Chapter 4 already told us what to do: the evaluation map is a canonical isomorphism \( V \to V^{**} \), and it induces a projectivity.

::: {#thm-double-dual-projective}
[Dualizing Twice Returns the Original]

Let \( \dim V = n + 1 \ge 1 \). The evaluation map \( \ev_V \colon V \to V^{**} \) is an isomorphism (@thm-double-dual-isomorphism), so it induces a projectivity \( [\ev_V] \colon \nP(V) \to \nP(V^{**}) \) (@def-projective-transformation). For every projective subspace \( S \) of \( \nP(V) \),
\[
S^{00} = [\ev_V](S),
\]
so that under the identification \( \nP(V) = \nP(V^{**}) \) given by \( [\ev_V] \) we have \( S^{00} = S \). Moreover the inverse of the bijection of @thm-duality-correspondence (d) is \( R \mapsto [\ev_V]^{-1}\bigl(R^{0}\bigr) \).
:::

::: {.proof}
Write \( S = \nP(U) \). By the definition of the correspondence applied twice, \( S^{00} = \nP\bigl((U^{0})^{0}\bigr) = \nP\bigl(\ev_V(U)\bigr) \), using @cor-annihilator-of-annihilator. By @prp-projectivity-preserves-subspaces, \( \nP(\ev_V(U)) = [\ev_V](\nP(U)) = [\ev_V](S) \).

For the last statement, let \( R \) be a projective subspace of \( \nP(V^{*}) \) and put \( S \coloneqq [\ev_V]^{-1}(R^{0}) \), a projective subspace of \( \nP(V) \) by @prp-projectivity-preserves-subspaces applied to \( [\ev_V]^{-1} \). Then \( [\ev_V](S) = R^{0} \), so by the first part \( (S^{0})^{0} = S^{00} = R^{0} \). Both \( S^{0} \) and \( R \) are projective subspaces of \( \nP(V^{*}) \), and @thm-duality-correspondence (d) applied to the space \( V^{*} \) says that the correspondence there is injective, so \( S^{0} = R \).
:::

Duality is also compatible with the maps of Section 07, which is what makes it more than a coordinate trick.

::: {#prp-duality-and-projectivities}
[Duality and Projectivities]

Let \( T \colon V \to W \) be an isomorphism of \( (n+1) \)-dimensional spaces, with dual map \( T' \colon W^{*} \to V^{*} \) (@def-dual-map), which is an isomorphism by @thm-dual-map-properties (d). Then for every projective subspace \( S \) of \( \nP(V) \),
\[
\bigl([T](S)\bigr)^{0} = \bigl[(T')^{-1}\bigr]\bigl(S^{0}\bigr) .
\]
:::

::: {.proof}
Write \( S = \nP(U) \), so \( [T](S) = \nP(T(U)) \) by @prp-projectivity-preserves-subspaces. For \( \psi \in W^{*} \),
\[
\psi \in T(U)^{0} \iff \psi(T\u) = 0 \text{ for all } \u \in U \iff (T'\psi)(\u) = 0 \text{ for all } \u \in U,
\]
the second step by @def-dual-map, and the right-hand condition says \( T'\psi \in U^{0} \). Hence \( T(U)^{0} = (T')^{-1}(U^{0}) \). Applying \( \nP(\cdot) \) and @prp-projectivity-preserves-subspaces to the isomorphism \( (T')^{-1} \) gives the claim.
:::

## The duality principle

We can now state precisely what "every theorem has a dual" amounts to in this book.

::: {#thm-duality-principle}
[The Duality Principle]

Let \( \dim V = n + 1 \ge 1 \), and let \( S \mapsto S^{0} \) be the correspondence of @thm-duality-correspondence, from the projective subspaces of the \( n \)-dimensional space \( \nP(V) \) onto those of the \( n \)-dimensional space \( \nP(V^{*}) \). Let \( R, S, T \) be projective subspaces of \( \nP(V) \) and let \( d \) be an integer. Then:

::: {.enumerate options="label=(\alph*)"}
1. \( S \subseteq T \) if and only if \( T^{0} \subseteq S^{0} \); and \( S = T \) if and only if \( S^{0} = T^{0} \);
2. \( \dim S = d \) if and only if \( \dim S^{0} = n - 1 - d \);
3. \( R = S \vee T \) if and only if \( R^{0} = S^{0} \cap T^{0} \);
4. \( R = S \cap T \) if and only if \( R^{0} = S^{0} \vee T^{0} \);
5. as \( S \) runs over all projective subspaces of \( \nP(V) \), the subspace \( S^{0} \) runs exactly once over all projective subspaces of \( \nP(V^{*}) \).
:::
:::

::: {.proof}
(a) The first claim is @thm-duality-correspondence (b), and the second follows by applying it in both directions, or from injectivity in @thm-duality-correspondence (d).

(b) By @thm-duality-correspondence (a), \( \dim S^{0} = n - 1 - \dim S \). So \( \dim S = d \) gives \( \dim S^{0} = n-1-d \); conversely \( \dim S^{0} = n - 1 - d \) gives \( n - 1 - \dim S = n - 1 - d \), hence \( \dim S = d \).

(c) \( (\Rightarrow) \) is @thm-duality-correspondence (c). \( (\Leftarrow) \) If \( R^{0} = S^{0} \cap T^{0} = (S \vee T)^{0} \), then \( R = S \vee T \) by the equality clause of (a).

(d) The same argument with the second identity of @thm-duality-correspondence (c).

(e) This is @thm-duality-correspondence (d).
:::

**How the principle is used, and what we have not proved.** Every clause of @thm-duality-principle is an "if and only if", and by (e) the correspondence is a bijection between the two supplies of subspaces. So a proved statement about \( \nP(V) \) whose hypotheses and conclusion are built **only** from the relations \( \subseteq \) and \( = \), the operations \( \vee \) and \( \cap \), and the dimensions of the subspaces involved, can be translated clause by clause: reverse every inclusion, exchange \( \vee \) with \( \cap \), and replace every dimension \( d \) by \( n - 1 - d \). The translated statement then holds in \( \nP(V^{*}) \); and since every \( (n+1) \)-dimensional space \( W \) satisfies \( W \cong (W^{*})^{*} \) (@thm-double-dual-isomorphism), a statement true in \( \nP(V^{*}) \) for **every** \( V \) is true in \( \nP(W) \) for every \( W \), because projectivities preserve all of this structure (@prp-projectivity-preserves-subspaces).

This is a recipe, carried out below on the statements this chapter makes, and each carrying out is a proof. It is **not** a theorem here. To make "for every statement built only from …" itself a theorem, one has to define a formal language of incidence statements and induct on the way a statement is built, and this book has set up no such language. So we claim the principle only as a working method, and we prove each dual statement we use.

::: {#cor-dual-of-two-points-one-line}
[Two Points, Two Lines]

Let \( \dim V = 3 \), so that \( \nP(V) \) is a projective plane.

::: {.enumerate options="label=(\alph*)"}
1. Two distinct points of \( \nP(V) \) lie on exactly one line.
2. Two distinct lines of \( \nP(V) \) meet in exactly one point.
:::
:::

::: {.idea}
Prove (a) by hand: two distinct points have independent representatives, so their span is a plane in \( V \) and a line in \( \nP(V) \). Then get (b) from (a) by the dictionary, in \( \nP(V^{*}) \), which is a projective plane of its own. Section 06 already proved both statements directly from the dimension formula (@prp-two-points-determine-a-line, @cor-two-lines-meet). The point of doing (b) again this way is that duality delivers it with no geometry at all: every step is a clause of @thm-duality-principle with \( n = 2 \).
:::

::: {.proof}
(a) Let \( P = [\v] \ne Q = [\w] \). The list \( (\v, \w) \) is independent: otherwise \( \w \) would be a scalar multiple of \( \v \), giving \( P = Q \). So \( \Span(\v, \w) \) has dimension \( 2 \), and by @lem-projective-subspaces-and-subspaces (c), \( P \vee Q = \nP(\Span(\v, \w)) \), a projective subspace of dimension \( 1 \), that is, a line containing both points. If \( L \) is any line containing \( P \) and \( Q \), then \( P \vee Q \subseteq L \) because the join is the smallest such subspace, and both have dimension \( 1 \), so \( L = P \vee Q \) by the consequence noted after @lem-projective-subspaces-and-subspaces.

(b) Here \( n = 2 \). Let \( L_1 \ne L_2 \) be lines of \( \nP(V) \). By @thm-duality-principle (b), \( \dim L_i^{0} = 2 - 1 - 1 = 0 \), so \( L_1^{0} \) and \( L_2^{0} \) are points of \( \nP(V^{*}) \), and they are distinct by the equality clause of @thm-duality-principle (a). The space \( \nP(V^{*}) \) is a projective plane, since \( \dim V^{*} = 3 \) by @cor-dimension-dual-space, so part (a), applied in \( \nP(V^{*}) \), says that \( L_1^{0} \vee L_2^{0} \) is a line, of dimension \( 1 \).

By @thm-duality-principle (d), \( (L_1 \cap L_2)^{0} = L_1^{0} \vee L_2^{0} \). Hence \( \dim (L_1 \cap L_2)^{0} = 1 \), and @thm-duality-principle (b) read backwards gives \( \dim(L_1 \cap L_2) = 2 - 1 - 1 = 0 \). A projective subspace of dimension \( 0 \) is a single point. This proves that \( L_1 \) and \( L_2 \) meet in exactly one point.
:::

The same bookkeeping shows that the dimension formula of @thm-projective-dimension-formula is **self-dual**: replacing each of \( \dim(S \vee T) \), \( \dim(S \cap T) \), \( \dim S \), \( \dim T \) by \( n - 1 \) minus itself and exchanging \( \vee \) with \( \cap \) turns
\[
\dim(S \vee T) + \dim(S \cap T) = \dim S + \dim T
\]
into \( (n-1-\dim(S \cap T)) + (n-1-\dim(S \vee T)) = (n-1-\dim S) + (n-1-\dim T) \), which is the same equation after canceling \( 2(n-1) \). A self-dual theorem is one whose dual gives nothing new, and that is a useful thing to be able to detect.

::: {.warning}
**The dual of "point" is not "line"; it is "hyperplane", and which dimension that is depends on \( n \).** In the projective plane, \( n = 2 \), and \( 2 - 1 - 0 = 1 \): points dualize to lines, which is why @cor-dual-of-two-points-one-line looks like a swap of the two words. In \( \nP^3 \), \( n = 3 \), so points dualize to **planes** (\( 3 - 1 - 0 = 2 \)) and lines dualize to lines (\( 3 - 1 - 1 = 1 \)). The correct dual of "two distinct points lie on a unique line" in \( \nP^3 \) is "two distinct planes meet in a unique line", and that is true. The careless dual, "two distinct lines meet in a point", is **false** in \( \nP^3 \): the lines \( \nP(\Span(\e_0, \e_1)) \) and \( \nP(\Span(\e_2, \e_3)) \) have \( \Span(\e_0,\e_1) \cap \Span(\e_2,\e_3) = \{\0\} \), so they do not meet at all. Always compute \( n - 1 - d \); never translate by the words alone.
:::

Pole and polar — the correspondence a conic sets up between the points and the lines of a plane — is the one piece of duality that needs a quadratic form rather than only the annihilator. It is treated in Section 10 of this chapter, where conics are, and nothing in this section depends on it.

## Exercises

### A. Check your understanding

:::: {#exr-projective-duality-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the dual projective space of \( \nP(V) \), and say what its dimension is.
2. Let \( S \) be a plane in \( \nP^4(F) \). Compute \( \dim S^{0} \).
3. True or false, with a reason: the duality correspondence of @thm-duality-correspondence is a bijection from the points of \( \nP(V) \) to the points of \( \nP(V) \).
4. In \( \nP^2 \), what is the dual of the statement "three distinct points are collinear"?
5. What are \( \emptyset^{0} \) and \( \nP(V)^{0} \)?
:::
::::

::: {.solution}
(a) It is \( \nP(V^{*}) \), the projective space of the dual space (@def-dual-projective-space). If \( \dim \nP(V) = n \), then \( \dim\nP(V^{*}) = n \) as well, by @cor-dimension-dual-space.

(b) A plane has dimension \( 2 \) and \( n = 4 \), so \( \dim S^{0} = 4 - 1 - 2 = 1 \): a line in the dual space.

(c) False, twice over. It is a bijection between **all** projective subspaces of \( \nP(V) \) and all projective subspaces of \( \nP(V^{*}) \), and it sends points of \( \nP(V) \) to hyperplanes of \( \nP(V^{*}) \), not to points; and its target is \( \nP(V^{*}) \), not \( \nP(V) \) (see the warning after @exm-line-and-its-dual-point).

(d) With \( n = 2 \), points dualize to lines and a line dualizes to a point. "Three distinct points lie on one line" becomes "three distinct lines pass through one point", that is, the three lines are concurrent.

(e) \( \emptyset^{0} = \nP(\{\0\}^{0}) = \nP(V^{*}) \), of dimension \( n = n - 1 - (-1) \); and \( \nP(V)^{0} = \nP(V^{0}) = \nP(\{0\}) = \emptyset \), of dimension \( -1 = n - 1 - n \).
:::

### B. Practice

:::: {#exr-projective-duality-b1}
[B1: Lines and dual points]

Work in \( \nP^2(\nQ) \).

::: {.enumerate options="label=(\alph*)"}
1. Find the dual point of the line through \( [1:2:1] \) and \( [0:1:3] \).
2. Find the point where the lines \( x_0 + x_1 - x_2 = 0 \) and \( 2x_0 - x_1 = 0 \) meet.
:::
::::

::: {.solution}
(a) We need \( \a = (a_0, a_1, a_2) \) with \( a_0 + 2a_1 + a_2 = 0 \) and \( a_1 + 3a_2 = 0 \). From the second, \( a_1 = -3a_2 \); substituting, \( a_0 = -2a_1 - a_2 = 6a_2 - a_2 = 5a_2 \). Taking \( a_2 = 1 \) gives \( \a = (5, -3, 1) \), so the line is \( 5x_0 - 3x_1 + x_2 = 0 \) and the dual point is \( [5:-3:1] \). Check: \( 5 - 6 + 1 = 0 \) and \( 0 - 3 + 3 = 0 \). By @thm-dimension-annihilator the solution space is one-dimensional, so this is the only answer up to scaling.

(b) Solve \( x_0 + x_1 - x_2 = 0 \) and \( 2x_0 - x_1 = 0 \). The second gives \( x_1 = 2x_0 \), and then \( x_2 = x_0 + x_1 = 3x_0 \). Taking \( x_0 = 1 \), the meet is \( [1:2:3] \). Check: \( 1 + 2 - 3 = 0 \) and \( 2 - 2 = 0 \). The solution space is one-dimensional, consistent with @cor-dual-of-two-points-one-line (b).
:::

:::: {#exr-projective-duality-b2}
[B2: Dimension bookkeeping]

Let \( n = 5 \), so \( \nP(V) = \nP^5(F) \). For each of the following \( S \), give \( \dim S^{0} \), and say which of the two is larger.

::: {.enumerate options="label=(\alph*)"}
1. \( S \) a point.
2. \( S \) a line.
3. \( S \) of dimension \( 2 \).
4. \( S \) a hyperplane.
5. \( S = \emptyset \).
:::

Then determine whether there is any \( S \) with \( \dim S^{0} = \dim S \). Justify your answer.
::::

::: {.solution}
By @thm-duality-correspondence (a), \( \dim S^{0} = 5 - 1 - \dim S = 4 - \dim S \).

(a) \( \dim S = 0 \), \( \dim S^{0} = 4 \); the dual is larger. (b) \( 1 \) and \( 3 \); the dual is larger. (c) \( 2 \) and \( 2 \); equal. (d) \( 4 \) and \( 0 \); the original is larger. (e) \( -1 \) and \( 5 \); the dual is larger.

For the last part, \( \dim S^{0} = \dim S \) means \( 4 - \dim S = \dim S \), that is, \( \dim S = 2 \). So the self-dual dimension in \( \nP^5 \) is \( 2 \), and part (c) is an instance. In general \( \dim S^0 = \dim S \) forces \( 2\dim S = n - 1 \), which has a solution exactly when \( n \) is odd.
:::

:::: {#exr-projective-duality-b3}
[B3: Dualize a statement]

For each statement about \( \nP^3(F) \), write the dual statement, using @thm-duality-principle with \( n = 3 \), and say whether both are true.

::: {.enumerate options="label=(\alph*)"}
1. A point and a line not through it lie in exactly one plane.
2. Three planes with no common line meet in at most one point.
:::
::::

::: {.solution}
With \( n = 3 \), the dimension rule is \( d \mapsto 2 - d \): points (\( 0 \)) and planes (\( 2 \)) exchange, lines (\( 1 \)) stay lines, \( \emptyset \) (\( -1 \)) and the whole space (\( 3 \)) exchange. Joins become meets.

(a) Dual: *a plane and a line not contained in it meet in exactly one point.* Both are true. For the original: if \( P \not\subseteq L \) then \( P \cap L = \emptyset \), so by @thm-projective-dimension-formula \( \dim(P \vee L) = 0 + 1 - (-1) = 2 \), a plane, and it is unique because any plane containing both contains \( P \vee L \) and has the same dimension. Dualizing each clause by @thm-duality-principle gives the dual statement, which is therefore also true; directly, if the plane \( \Pi \) does not contain \( L \), then \( \Pi \vee L \) has dimension \( 3 \), so \( \dim(\Pi \cap L) = 2 + 1 - 3 = 0 \).

(b) Dualize clause by clause, as the warning after @cor-dual-of-two-points-one-line insists. The hypothesis "the three planes contain no common line" reads: there is no \( L \) with \( \dim L = 1 \) and \( L \subseteq \Pi_1 \cap \Pi_2 \cap \Pi_3 \). Writing \( P_i = \Pi_i^{0} \), which are points by @thm-duality-principle (b), and using (a) and (d) of that theorem, the hypothesis becomes: there is no \( L' \) with \( \dim L' = 1 \) and \( P_1 \vee P_2 \vee P_3 \subseteq L' \), that is, the three points are **not** collinear. The conclusion "\( \Pi_1 \cap \Pi_2 \cap \Pi_3 \) has dimension at most \( 0 \)" becomes "\( P_1 \vee P_2 \vee P_3 \) has dimension at least \( 2 \)". So the dual statement is: *three points not on a common line span a projective subspace of dimension at least \( 2 \)*, that is, they span a plane. Both are true: three non-collinear points \( [\v_1], [\v_2], [\v_3] \) have independent representatives, since a dependence would put all three in a subspace of dimension at most \( 2 \) and hence on a common line, so their join has dimension \( 2 \) by @lem-projective-subspaces-and-subspaces (c). The original then follows by dualizing back.
:::

### C. Going deeper

:::: {#exr-projective-duality-c1}
[C1: Counting in a finite projective plane]

Let \( q \) be a prime power and \( F = \nF_q \).

::: {.enumerate options="label=(\alph*)"}
1. Show that a projective space of dimension \( d \) over \( \nF_q \) has \( (q^{d+1} - 1)/(q - 1) \) points.
2. Deduce that \( \nP^2(\nF_q) \) has as many lines as points, and that every point lies on exactly \( q + 1 \) lines.
:::
::::

::: {.solution}
(a) Such a space is \( \nP(U) \) with \( \dim U = d + 1 \). The set \( U \setminus \{\0\} \) has \( q^{d+1} - 1 \) elements, and two non-zero vectors give the same point exactly when they differ by a scalar in \( \nF_q \setminus \{0\} \), a set of size \( q - 1 \). So each point has exactly \( q - 1 \) representatives, and the number of points is \( (q^{d+1}-1)/(q-1) \).

(b) By @prp-points-of-dual-are-hyperplanes the lines of \( \nP^2(\nF_q) \) are in bijection with the points of \( \nP((\nF_q^3)^{*}) \), which by @cor-dimension-dual-space is again a projective plane over \( \nF_q \). So by (a) with \( d = 2 \) both counts are \( N \coloneqq q^2 + q + 1 \).

For the last claim, fix a point \( P \). The lines of \( \nP^2(\nF_q) \) containing \( P \) are, by the remark after @thm-duality-correspondence, exactly the points of \( P^{0} \), and \( \dim P^{0} = 2 - 1 - 0 = 1 \) by @thm-duality-correspondence (a). So by (a) with \( d = 1 \) there are \( q + 1 \) of them. As a check, count the incident pairs \( (P, L) \) with \( P \in L \) in two ways: each line is a projective space of dimension \( 1 \) and so carries \( q+1 \) points, giving \( N(q+1) \) pairs, and the other count gives \( N(q+1) \) as well.
:::

:::: {#exr-projective-duality-c2}
[C2: A form makes a self-duality]

Let \( \beta \) be a non-degenerate symmetric bilinear form on \( V \), with \( \dim V = n+1 \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( R_{\beta} \colon V \to V^{*} \), \( \v \mapsto \beta(\cdot, \v) \), is an isomorphism, and deduce that it induces a projectivity \( [R_{\beta}] \colon \nP(V) \to \nP(V^{*}) \).
2. Hence define, for a projective subspace \( S \) of \( \nP(V) \), a projective subspace \( S^{\perp} \) of \( \nP(V) \) with \( \dim S^{\perp} = n - 1 - \dim S \), and show that the assignment \( S \mapsto S^{\perp} \) is an inclusion-reversing bijection of the set of projective subspaces of \( \nP(V) \) with itself.
3. Give an example over \( \nR \) with \( n = 2 \) in which \( S \subseteq S^{\perp} \) for some point \( S \), and explain why this cannot happen if \( \beta \) is positive definite.
:::
::::

::: {.solution}
(a) By @prp-nondegenerate-iff-invertible, \( \beta \) is non-degenerate exactly when \( R_{\beta} \) is an isomorphism \( V \to V^{*} \). A projectivity is induced by any isomorphism (@def-projective-transformation), so \( [R_{\beta}] \) is one.

(b) Define \( S^{\perp} \coloneqq [R_{\beta}]^{-1}\bigl(S^{0}\bigr) \). This is a projective subspace of \( \nP(V) \) by @prp-projectivity-preserves-subspaces, of the same dimension as \( S^{0} \), namely \( n - 1 - \dim S \) by @thm-duality-correspondence (a). Since \( [R_{\beta}]^{-1} \) is a bijection preserving inclusion (@prp-projectivity-preserves-subspaces) and \( S \mapsto S^{0} \) is an inclusion-reversing bijection onto the projective subspaces of \( \nP(V^{*}) \) (@thm-duality-correspondence (b), (d)), the composite is an inclusion-reversing bijection of the projective subspaces of \( \nP(V) \) with themselves.

(c) Take \( V = \nR^3 \) and \( \beta(\x, \y) = x_0y_0 + x_1y_1 - x_2y_2 \), which is non-degenerate since its matrix \( \diag(1,1,-1) \) is invertible. Let \( \v = (1, 0, 1) \), so \( \beta(\v, \v) = 1 + 0 - 1 = 0 \), and let \( S = \{[\v]\} \). Then \( R_{\beta}(\v) = \beta(\cdot, \v) \) kills \( \v \), so \( [\v] \in S^{\perp} \), that is, \( S \subseteq S^{\perp} \). If \( \beta \) were positive definite, then \( \beta(\v, \v) > 0 \) for every \( \v \ne \0 \), so no non-zero vector is annihilated by its own functional, and \( S \subseteq S^{\perp} \) is impossible for a point \( S \). The non-zero vectors with \( \beta(\v, \v) = 0 \) are the isotropic ones of @def-isotropic-vector, taken for the quadratic form \( q(\v) = \beta(\v, \v) \); they are exactly the points lying on their own duals.
:::

:::: {#exr-projective-duality-c3}
[C3: What the correspondence does to a chain]

Let \( \dim V = n + 1 \) and let
\[
\emptyset = S_{-1} \subsetneq S_0 \subsetneq S_1 \subsetneq \dots \subsetneq S_n = \nP(V)
\]
be projective subspaces with \( \dim S_d = d \) for each \( d \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( S_n^{0} \subsetneq S_{n-1}^{0} \subsetneq \dots \subsetneq S_{-1}^{0} \) is again such a chain, and identify \( \dim S_d^{0} \).
2. Deduce that \( S \mapsto S^{0} \) carries the chains of this shape in \( \nP(V) \) bijectively to those in \( \nP(V^{*}) \), and that it reverses their order.
:::
::::

::: {.solution}
(a) By @thm-duality-principle (a), \( S_{d} \subseteq S_{d+1} \) gives \( S_{d+1}^{0} \subseteq S_{d}^{0} \), and the inclusion is strict: if \( S_{d+1}^{0} = S_{d}^{0} \) then \( S_{d+1} = S_{d} \) by the equality clause, contradicting strictness. By @thm-duality-principle (b), \( \dim S_{d}^{0} = n - 1 - d \). As \( d \) runs from \( -1 \) to \( n \), the value \( n - 1 - d \) runs from \( n \) down to \( -1 \), taking each value once. So writing \( T_{e} \coloneqq S_{n-1-e}^{0} \) gives \( \dim T_e = e \) and \( T_{-1} \subsetneq T_0 \subsetneq \dots \subsetneq T_n \), a chain of the same shape in \( \nP(V^{*}) \).

(b) The assignment is injective because \( S \mapsto S^{0} \) is (@thm-duality-principle (e)), applied term by term. It is surjective: given a chain \( T_{-1} \subsetneq T_0 \subsetneq \dots \subsetneq T_n \) with \( \dim T_e = e \) in \( \nP(V^{*}) \), set \( S_d \coloneqq [\ev_V]^{-1}\bigl(T_{n-1-d}^{0}\bigr) \), which by @thm-double-dual-projective is the unique projective subspace of \( \nP(V) \) with \( S_d^{0} = T_{n-1-d} \). By @thm-duality-principle (b), \( \dim S_d = n - 1 - (n-1-d) = d \); and if \( d < d' \) then \( n-1-d > n-1-d' \), so \( T_{n-1-d} \supsetneq T_{n-1-d'} \), whence \( S_d \subsetneq S_{d'} \) by @thm-duality-principle (a). So \( (S_d) \) is a chain of the required shape whose image is the given one, and the order has been reversed.
:::
