# Orthogonal Complements and Projections

Chapter 1 proved that every subspace of a finite-dimensional space has a complement, and then warned that it has many: the \( x \)-axis in \( \nR^2 \) is complemented by every other line through the origin. An inner product breaks the tie. Among all the complements of \( U \) there is now one built from \( U \) alone, the set of vectors perpendicular to everything in \( U \), and the projection onto \( U \) along it turns out to solve an approximation problem: it finds the vector of \( U \) closest to a given \( \v \). This section constructs that complement, that projection, and that answer.

Throughout, \( V \) is an inner product space over \( F = \nR \) or \( F = \nC \), with inner product \( \inner{\cdot}{\cdot} \) (@def-inner-product) and induced norm \( \norm{\cdot} \) (@def-induced-norm). We do **not** assume \( V \) is finite-dimensional; what we assume, each time, is that the subspace we project onto is.

## Orthogonal complements

In \( \nR^3 \), a plane \( U \) through the origin has a distinguished line attached to it: the normal line, the set of vectors perpendicular to the whole plane. Nothing about the plane had to be chosen to produce it. That construction is available in any inner product space, and it is available for any subset, not only for subspaces.

*The orthogonal complement of \( U \) collects every vector that is perpendicular to all of \( U \) at once.*

::: {#def-orthogonal-complement}
[Orthogonal complement]

Let \( V \) be an inner product space over \( F \) and let \( S \subseteq V \) be **any** subset. The **orthogonal complement** of \( S \) is
\[
S^{\perp} = \{\, \v \in V : \inner{\v}{\s} = 0 \text{ for every } \s \in S \,\},
\]
read "\( S \) perp".
:::

In words: \( \v \) belongs to \( S^{\perp} \) when \( \v \) is orthogonal (@def-orthogonal) to **every** single element of \( S \), not merely to some of them. The quantifier is what makes the definition useful, and it is also what makes \( S^{\perp} \) a subspace even when \( S \) is not. Note that the condition could equally be written \( \inner{\s}{\v} = 0 \) for every \( \s \in S \), since \( \inner{\s}{\v} = \conj{\inner{\v}{\s}} \) and a complex number vanishes exactly when its conjugate does. We will use whichever slot is convenient.

::: {#prp-orthogonal-complement-subspace}
[Perp is always a subspace]

For every subset \( S \) of an inner product space \( V \), the set \( S^{\perp} \) is a subspace of \( V \). Moreover \( S^{\perp} = \Span(S)^{\perp} \).
:::

::: {.proof}
We apply the Subspace Test (@thm-subspace-test). First, \( \inner{\0}{\s} = 0 \) for every \( \s \), because \( \inner{\cdot}{\s} \) is linear in the first slot and a linear map sends \( \0 \) to \( 0 \) (@thm-zero-maps-to-zero); so \( \0 \in S^{\perp} \). Next, let \( \v, \w \in S^{\perp} \) and \( a \in F \). For every \( \s \in S \),
\[
\inner{\v + \w}{\s} = \inner{\v}{\s} + \inner{\w}{\s} = 0, \qquad \inner{a\v}{\s} = a\inner{\v}{\s} = 0,
\]
both by linearity in the first slot. Hence \( \v + \w \in S^{\perp} \) and \( a\v \in S^{\perp} \).

For the second claim, \( S \subseteq \Span(S) \) gives \( \Span(S)^{\perp} \subseteq S^{\perp} \). Conversely let \( \v \in S^{\perp} \) and let \( \u = a_1\s_1 + \dots + a_k\s_k \) with \( \s_i \in S \). Then
\[
\inner{\u}{\v} = a_1\inner{\s_1}{\v} + \dots + a_k\inner{\s_k}{\v} = 0,
\]
since each \( \inner{\s_i}{\v} = \conj{\inner{\v}{\s_i}} = 0 \). So \( \inner{\v}{\u} = \conj{\inner{\u}{\v}} = 0 \), and \( \v \in \Span(S)^{\perp} \).
:::

The second half is what makes computation possible: to test membership in \( U^{\perp} \) it is enough to test against a spanning list of \( U \), not against all of \( U \).

**Examples.**

- **The extremes.** \( \{\0\}^{\perp} = V \), since \( \inner{\v}{\0} = 0 \) always. And \( V^{\perp} = \{\0\} \): if \( \v \in V^{\perp} \), then in particular \( \inner{\v}{\v} = 0 \), and positive definiteness forces \( \v = \0 \). This is the "pair it with itself" move, and it is the shape in which positivity almost always enters; it is the only place where positivity is used; we will use it again and again.
- **A plane in \( \nR^3 \).** Let \( U = \{ (x, y, z) : x + y + z = 0 \} \) with the dot product. The condition \( x + y + z = 0 \) says exactly \( \inner{(x, y, z)}{(1, 1, 1)} = 0 \), so \( U = \{(1,1,1)\}^{\perp} \). The Orthogonal Decomposition Theorem below will give the converse, \( U^{\perp} = \Span((1, 1, 1)) \).
- **A subset that is not a subspace.** In \( \nR^3 \), take \( S = \{ (1, 0, 0), (1, 1, 0) \} \), two vectors and nothing else. Then \( S^{\perp} = \{ (x, y, z) : x = 0,\ x + y = 0 \} = \Span((0, 0, 1)) \), a subspace, as @prp-orthogonal-complement-subspace promises. It equals \( \Span(S)^{\perp} \), the perp of the \( xy \)-plane.
- **Polynomials.** On \( \nR[x]_{\le 2} \) with \( \inner{p}{q} = \int_{-1}^{1} p(t)q(t)\,\dd t \), let \( U = \Span(1) \) be the constants. Then \( p \in U^{\perp} \) means \( \int_{-1}^{1} p(t)\,\dd t = 0 \): the polynomials of average value zero. For instance \( x \) and \( x^2 - \tfrac13 \) lie in \( U^{\perp} \), and they span it, since the Orthogonal Decomposition Theorem below gives \( \dim U^{\perp} = 3 - 1 = 2 \).

**Non-example by minimal change.** Weaken "for every \( \s \in S \)" to "for some \( \s \in S \)". With \( S = \{\e_1, \e_2\} \) in \( \nR^2 \), the weakened set is \( \{ \v : \inner{\v}{\e_1} = 0 \text{ or } \inner{\v}{\e_2} = 0 \} \), the union of the two axes. Closure under scalars still holds, and \( \0 \) still belongs; what fails is closure under addition, since \( (1, 0) + (0, 1) = (1, 1) \) lies on neither axis. This is the union of @exm-union-axes again, in new clothing. The universal quantifier is doing real work.

**Why this definition.** One could try to define "the" complement of \( U \) by choosing a basis of \( U \), extending it, and spanning the new vectors, which is what @thm-complement-exists does. That answer depends on every choice made along the way. The definition above depends only on \( U \) and on the inner product, and the next theorem shows that it really is a complement.

## The orthogonal decomposition

Here is the theorem that makes \( U^{\perp} \) more than a definition. Note the hypothesis: \( U \) must be finite-dimensional, but \( V \) need not be. The reason is that the proof needs an orthonormal basis of \( U \), and Gram–Schmidt supplies one only for a finite list.

:::: {#thm-orthogonal-decomposition}
[Orthogonal Decomposition Theorem]

Let \( V \) be an inner product space over \( F \) and let \( U \) be a **finite-dimensional** subspace of \( V \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( V = U \oplus U^{\perp} \);
2. \( (U^{\perp})^{\perp} = U \);
3. if in addition \( V \) is finite-dimensional, then \( \dim U^{\perp} = \dim V - \dim U \).
:::
::::

::: {.idea}
For (a) we must produce, from an arbitrary \( \v \), a piece inside \( U \) and a piece perpendicular to \( U \). Fix an orthonormal basis of \( U \). @thm-orthonormal-coordinates says that a vector **of \( U \)** is the sum of its coordinates against that basis; so for a \( \v \) that is not in \( U \), the same sum is the natural guess for the \( U \)-piece. Then we subtract and check. That is the move of Gram–Schmidt — project, then subtract — used once instead of repeatedly. Uniqueness of the splitting is the "pair with itself" move. For (b), one inclusion is free and the other is (a) applied twice.
:::

::: {.proof}
(a) Since \( U \) is finite-dimensional, it has an orthonormal basis \( (\e_1, \dots, \e_k) \) by @thm-gram-schmidt. Let \( \v \in V \) and put
\[
\u = \sum_{i=1}^{k} \inner{\v}{\e_i}\e_i \in U, \qquad \w = \v - \u .
\]
For each \( j \),
\[
\inner{\w}{\e_j} = \inner{\v}{\e_j} - \sum_{i=1}^{k} \inner{\v}{\e_i}\inner{\e_i}{\e_j} = \inner{\v}{\e_j} - \inner{\v}{\e_j} = 0,
\]
where the middle step uses \( \inner{\e_i}{\e_j} = \delta_{ij} \). So \( \w \) is orthogonal to each \( \e_j \), hence to \( \Span(\e_1, \dots, \e_k) = U \) by @prp-orthogonal-complement-subspace. Therefore \( \v = \u + \w \in U + U^{\perp} \).

The sum is direct: if \( \x \in U \cap U^{\perp} \), then \( \inner{\x}{\x} = 0 \) because \( \x \in U^{\perp} \) and \( \x \in U \), so \( \x = \0 \) by positive definiteness. By @thm-direct-sum-criteria, \( V = U \oplus U^{\perp} \).

(b) \( (\subseteq) \) Let \( \u \in U \). For every \( \w \in U^{\perp} \) we have \( \inner{\w}{\u} = 0 \), hence \( \inner{\u}{\w} = \conj{\inner{\w}{\u}} = 0 \). So \( \u \in (U^{\perp})^{\perp} \).

\( (\supseteq) \) Let \( \v \in (U^{\perp})^{\perp} \). By (a), write \( \v = \u + \w \) with \( \u \in U \) and \( \w \in U^{\perp} \). By the inclusion just proved, \( \u \in (U^{\perp})^{\perp} \), so \( \w = \v - \u \in (U^{\perp})^{\perp} \) as well. Thus \( \w \) lies in both \( U^{\perp} \) and \( (U^{\perp})^{\perp} \), giving \( \inner{\w}{\w} = 0 \) and \( \w = \0 \). Hence \( \v = \u \in U \).

(c) By (a), \( U^{\perp} \) is a complement of \( U \) in \( V \), so \( \dim U^{\perp} = \dim V - \dim U \) by @thm-complement-exists.
:::

Part (b) is worth pausing on. For a general subspace of a general vector space there is no operation "\( \perp \)" to apply twice, and even for the annihilator of Chapter 5 the analogous statement needed the double dual. Here it is a two-line consequence of (a). Part (c) says that \( \perp \) exchanges dimension \( k \) with dimension \( n - k \), just as the annihilator does (@thm-dimension-annihilator); Section 5 explains why the two facts are the same fact.

::: {.check}
Positive definiteness was used twice in the proof of @thm-orthogonal-decomposition, in the same way each time. Where? To see that it cannot be dropped, take \( \nR^2 \) with the indefinite form \( \beta(\x, \y) = x_1y_1 - x_2y_2 \), let \( U = \Span((1, 1)) \), and write \( U^{\perp} \) for the set of \( \v \) with \( \beta(\v, \u) = 0 \) for all \( \u \in U \). Compute \( U \cap U^{\perp} \).
:::

::: {.solution}
It was used to show \( U \cap U^{\perp} = \{\0\} \) in (a), and again for \( \w = \0 \) in (b); both times through "\( \inner{\x}{\x} = 0 \) forces \( \x = \0 \)".

With \( \beta \), the vector \( \u = (1, 1) \) satisfies \( \beta(\u, \u) = 1 - 1 = 0 \), so \( \u \) is "orthogonal to itself" and \( \u \in U^{\perp} \). Hence \( U \cap U^{\perp} = U \neq \{\0\} \), and the sum \( U + U^{\perp} \) is not direct. Indeed \( U^{\perp} = \{ (x_1, x_2) : x_1 - x_2 = 0 \} = U \) here, so \( U + U^{\perp} = U \) is not all of \( \nR^2 \). Both conclusions of the theorem fail.
:::

## Orthogonal projection

Once \( V = U \oplus U^{\perp} \), Chapter 2 hands us an operator: the projection onto \( U \) along \( U^{\perp} \) (@thm-projection-direct-sum). It deserves its own name and symbol, because the complement is no longer a choice.

::: {#def-orthogonal-projection}
[Orthogonal projection]

Let \( U \) be a finite-dimensional subspace of an inner product space \( V \). By @thm-orthogonal-decomposition (a), every \( \v \in V \) has a unique splitting \( \v = \u + \w \) with \( \u \in U \) and \( \w \in U^{\perp} \). The **orthogonal projection onto \( U \)** is the operator \( P_U \in \cL(V) \) defined by
\[
P_U\v = \u .
\]
:::

The definition makes sense because the splitting exists and is unique, and \( P_U \) is linear by @thm-projection-direct-sum (b), which also gives \( P_U^2 = P_U \), \( \im P_U = U \) and \( \ker P_U = U^{\perp} \). Nothing so far tells us how to compute \( P_U\v \). The proof of @thm-orthogonal-decomposition does, and that is the next theorem.

:::: {#thm-projection-formula}
[Projection formula]

Let \( U \) be a finite-dimensional subspace of an inner product space \( V \), with orthonormal basis \( (\e_1, \dots, \e_k) \). Then for every \( \v \in V \):

::: {.enumerate options="label=(\alph*)"}
1. \( \displaystyle P_U\v = \sum_{i=1}^{k} \inner{\v}{\e_i}\e_i \);
2. \( \inner{P_U\u}{\v} = \inner{\u}{P_U\v} \) for all \( \u, \v \in V \);
3. \( \norm{P_U\v} \le \norm{\v} \), with equality if and only if \( \v \in U \).
:::
::::

::: {.idea}
Part (a) is not a new computation: the vector \( \u \) built in the proof of @thm-orthogonal-decomposition (a) was exactly this sum, and by uniqueness of the splitting it must be \( P_U\v \). For (b), split **both** \( \u \) and \( \v \), and watch the cross terms die. For (c), split \( \v \) and use Pythagoras.
:::

::: {.proof}
(a) Put \( \u = \sum_i \inner{\v}{\e_i}\e_i \) and \( \w = \v - \u \). The proof of @thm-orthogonal-decomposition (a) showed \( \u \in U \) and \( \w \in U^{\perp} \). Since the splitting of \( \v \) in \( U \oplus U^{\perp} \) is unique (@def-direct-sum), \( P_U\v = \u \).

(b) Write \( \u = \u_1 + \u_2 \) and \( \v = \v_1 + \v_2 \) with \( \u_1, \v_1 \in U \) and \( \u_2, \v_2 \in U^{\perp} \). Then \( \inner{\u_1}{\v_2} = 0 \) because \( \v_2 \in U^{\perp} \) and \( \u_1 \in U \), and \( \inner{\u_2}{\v_1} = 0 \) for the same reason with the roles swapped. Hence
\[
\inner{P_U\u}{\v} = \inner{\u_1}{\v_1 + \v_2} = \inner{\u_1}{\v_1} = \inner{\u_1 + \u_2}{\v_1} = \inner{\u}{P_U\v}.
\]

(c) With \( \v = \v_1 + \v_2 \) as above, \( \v_1 \) and \( \v_2 \) are orthogonal, so \( \norm{\v}^2 = \norm{\v_1}^2 + \norm{\v_2}^2 \) by @thm-pythagoras. Since \( \norm{\v_2}^2 \ge 0 \), this gives \( \norm{P_U\v}^2 = \norm{\v_1}^2 \le \norm{\v}^2 \). Equality holds if and only if \( \norm{\v_2} = 0 \), that is \( \v_2 = \0 \), that is \( \v = \v_1 \in U \).
:::

Two comments. First, the right-hand side of (a) visibly depends on the orthonormal basis chosen, while the left-hand side does not; so the sum \( \sum_i \inner{\v}{\e_i}\e_i \) is the same for every orthonormal basis of \( U \). That is a genuine piece of information, obtained for free. Second, property (b) says that \( P_U \) can be moved from one slot of the inner product to the other at no cost. Section 6 will call such an operator **self-adjoint** and write the property as \( P_U^{*} = P_U \); we proved the property here so that nothing later depends on the order of the sections.

Orthonormal bases are convenient but not obligatory, and by hand it is usually faster to skip the square roots.

::: {#cor-projection-orthogonal-basis}
[Projecting with an orthogonal basis]

Let \( U \) be a finite-dimensional subspace of an inner product space \( V \), and let \( (\u_1, \dots, \u_k) \) be an **orthogonal** basis of \( U \), so that \( \inner{\u_i}{\u_j} = 0 \) for \( i \neq j \) and every \( \u_i \neq \0 \). Then
\[
P_U\v = \sum_{i=1}^{k} \frac{\inner{\v}{\u_i}}{\inner{\u_i}{\u_i}}\,\u_i \qquad \text{for every } \v \in V .
\]
:::

::: {.proof}
Each \( \u_i \) is non-zero, so \( \norm{\u_i} > 0 \) and \( \e_i = \u_i/\norm{\u_i} \) is defined. Each \( \e_i \) is a non-zero multiple of \( \u_i \), so \( (\e_1, \dots, \e_k) \) is again a basis of \( U \), and it is orthonormal: \( \inner{\e_i}{\e_j} = \inner{\u_i}{\u_j}/(\norm{\u_i}\norm{\u_j}) = \delta_{ij} \). By @thm-projection-formula (a),
\[
P_U\v = \sum_{i=1}^{k} \inner{\v}{\e_i}\,\e_i = \sum_{i=1}^{k} \frac{\inner{\v}{\u_i}}{\norm{\u_i}^2}\,\u_i ,
\]
where the two factors \( 1/\norm{\u_i} \) come out unchanged, the one in the second slot because \( \norm{\u_i} \) is real. Finally \( \norm{\u_i}^2 = \inner{\u_i}{\u_i} \) by @def-induced-norm.
:::

Each summand \( \inner{\v}{\u_i}\u_i/\inner{\u_i}{\u_i} \) is the projection of \( \v \) onto the line \( \Span(\u_i) \): the case \( k = 1 \) of the corollary.

## Best approximation and distance

Now the payoff. Of all the vectors of \( U \), which is nearest to a given \( \v \)? In \( \nR^3 \), dropping a perpendicular from a point to a plane is the familiar recipe, and the recipe is correct in every inner product space.

::: {#thm-best-approximation}
[Best Approximation Theorem]

Let \( U \) be a finite-dimensional subspace of an inner product space \( V \), and let \( \v \in V \). Then
\[
\norm{\v - P_U\v} \le \norm{\v - \u} \qquad \text{for every } \u \in U,
\]
and equality holds **only** for \( \u = P_U\v \).
:::

::: {.idea}
Insert \( P_U\v \) into the difference: \( \v - \u = (\v - P_U\v) + (P_U\v - \u) \). The first bracket is perpendicular to \( U \) and the second lies in \( U \), so the two are orthogonal, and Pythagoras turns the comparison into "a sum of two squares is at least one of them". The picture is a right triangle with hypotenuse \( \v - \u \).
:::

\begin{center}
\begin{tikzpicture}[scale=1.15]
  \draw[fill=black!6, draw=black!45] (-2.6, -0.75) -- (2.6, -0.75) -- (3.6, 0.75) -- (-1.6, 0.75) -- cycle;
  \node[black!70] at (-2.05, 0.45) {$U$};
  \coordinate (O) at (0, 0);
  \coordinate (P) at (0.55, 0.1);
  \coordinate (U) at (2.1, 0.45);
  \coordinate (V) at (0.55, 2.2);
  \fill (O) circle (1.6pt) node[below left] {$\0$};
  \fill (V) circle (1.8pt) node[above] {$\v$};
  \fill (P) circle (1.8pt) node[below left] {$P_U\v$};
  \fill (U) circle (1.6pt) node[below right] {$\u$};
  \draw[->, thick] (O) -- (V);
  \draw[->, thick] (O) -- (P);
  \draw[very thick] (V) -- (P);
  \draw[thick, dashed] (V) -- (U);
  \draw[thick, dashed] (P) -- (U);
  \draw (P) ++(0.0,0.16) -- ++(0.16,0.0) -- ++(0.0,-0.16);
  \node[right] at (0.62, 1.2) {$\v - P_U\v$};
  \node[above right] at (1.35, 1.35) {$\v - \u$};
\end{tikzpicture}
\end{center}

::: {.proof}
Let \( \u \in U \) and write
\[
\v - \u = (\v - P_U\v) + (P_U\v - \u).
\]
The first bracket lies in \( U^{\perp} \), since \( \v - P_U\v \) is the \( U^{\perp} \)-part of \( \v \) in @thm-orthogonal-decomposition (a). The second lies in \( U \), since \( P_U\v \in U \) and \( \u \in U \). Hence the two brackets are orthogonal, and @thm-pythagoras gives
\[
\norm{\v - \u}^2 = \norm{\v - P_U\v}^2 + \norm{P_U\v - \u}^2 \ge \norm{\v - P_U\v}^2 .
\]
Taking square roots proves the inequality, since the norm is non-negative. Equality forces \( \norm{P_U\v - \u}^2 = 0 \), hence \( P_U\v - \u = \0 \) by positive definiteness, that is \( \u = P_U\v \). This proves the theorem.
:::

So the minimum is attained, and attained at exactly one point. That lets us define a distance.

::: {#def-distance-to-subspace}
[Distance to a subspace]

Let \( U \) be a finite-dimensional subspace of an inner product space \( V \) and let \( \v \in V \). The **distance from \( \v \) to \( U \)** is
\[
d(\v, U) = \min_{\u \in U} \norm{\v - \u} = \norm{\v - P_U\v} .
\]
:::

The word **minimum** is justified, not sloppy: @thm-best-approximation says the values \( \norm{\v - \u} \) really do have a smallest one. Note also that \( d(\v, U) = 0 \) if and only if \( \v \in U \), and that, when \( V \) is finite-dimensional, \( d(\v, U) = \norm{P_{U^{\perp}}\v} \), since \( \v - P_U\v \) is the \( U^{\perp} \)-component of \( \v \). (The hypothesis is needed for \( P_{U^{\perp}} \) to be defined at all: @def-orthogonal-projection asks the subspace projected onto to be finite-dimensional, and \( U^{\perp} \) is not, in the infinite-dimensional setting this section is careful to allow.) When \( U^{\perp} \) is the smaller of the two, computing that component is the faster route.

:::: {#exm-distance-to-plane}
[Distance from a point to a plane]

In \( \nR^3 \) with the dot product, let \( U = \{ (x, y, z) : x + y + z = 0 \} \) and \( \v = (1, 2, 3) \). Find \( P_U\v \) and \( d(\v, U) \), twice: once through \( U^{\perp} \), and once through an orthonormal basis of \( U \).
::::

::: {.solution}
*Through \( U^{\perp} \).* Put \( \n = (1, 1, 1) \). Every \( (x, y, z) \in U \) satisfies \( \inner{(x,y,z)}{\n} = x + y + z = 0 \), so \( \n \in U^{\perp} \). Since \( U \) is the solution set of one non-trivial equation, \( \dim U = 2 \), so \( \dim U^{\perp} = 3 - 2 = 1 \) by @thm-orthogonal-decomposition (c), and therefore \( U^{\perp} = \Span(\n) \). By @cor-projection-orthogonal-basis with the one-element basis \( (\n) \),
\[
P_{U^{\perp}}\v = \frac{\inner{\v}{\n}}{\inner{\n}{\n}}\n = \frac{1 + 2 + 3}{3}(1, 1, 1) = (2, 2, 2),
\]
so \( P_U\v = \v - (2, 2, 2) = (-1, 0, 1) \) and \( d(\v, U) = \norm{(2, 2, 2)} = 2\sqrt{3} \).

*Through an orthonormal basis of \( U \).* The vectors \( (1, -1, 0) \) and \( (1, 1, -2) \) lie in \( U \) and are orthogonal to each other, so
\[
\e_1 = \tfrac{1}{\sqrt2}(1, -1, 0), \qquad \e_2 = \tfrac{1}{\sqrt6}(1, 1, -2)
\]
is an orthonormal basis of \( U \). Then \( \inner{\v}{\e_1} = (1 - 2)/\sqrt2 = -1/\sqrt2 \) and \( \inner{\v}{\e_2} = (1 + 2 - 6)/\sqrt6 = -3/\sqrt6 \), so @thm-projection-formula (a) gives
\[
P_U\v = -\tfrac{1}{\sqrt2}\e_1 - \tfrac{3}{\sqrt6}\e_2 = -\tfrac12(1, -1, 0) - \tfrac12(1, 1, -2) = (-1, 0, 1),
\]
the same answer. *Check:* \( (-1) + 0 + 1 = 0 \), so \( P_U\v \in U \); and \( \v - P_U\v = (2, 2, 2) \) is a multiple of \( \n \), so it lies in \( U^{\perp} \). The two conditions together identify the splitting, by uniqueness.
:::

The next example is the same theorem in a space of functions, where "closest" is no longer something one can see.

:::: {#exm-best-quadratic-approximation}
[The best quadratic approximation to a cubic]

On \( V = \nR[x]_{\le 3} \) with \( \inner{p}{q} = \int_{-1}^{1} p(t)q(t)\,\dd t \), let \( U = \nR[x]_{\le 2} \). Find the polynomial of \( U \) closest to \( x^3 \), and the distance.
::::

::: {.solution}
The list \( (1, x, x^2 - \tfrac13) \) is a basis of \( U \), being three independent polynomials of degrees \( 0, 1, 2 \) (@thm-distinct-degrees-independent) in a space of dimension \( 3 \). It is **orthogonal**: \( \inner{1}{x} = 0 \) and \( \inner{x}{x^2 - \tfrac13} = 0 \) because the integrands are odd, and
\[
\inner{1}{x^2 - \tfrac13} = \int_{-1}^{1}\Bigl(t^2 - \tfrac13\Bigr)\dd t = \tfrac23 - \tfrac23 = 0 .
\]
Now apply @cor-projection-orthogonal-basis to \( \v = x^3 \). Two of the three coefficients vanish because \( t^3 \) is odd: \( \inner{x^3}{1} = 0 \) and \( \inner{x^3}{x^2 - \tfrac13} = 0 \). The remaining one is
\[
\frac{\inner{x^3}{x}}{\inner{x}{x}} = \frac{\int_{-1}^{1} t^4\,\dd t}{\int_{-1}^{1} t^2\,\dd t} = \frac{2/5}{2/3} = \frac35 .
\]
Hence \( P_U(x^3) = \tfrac35 x \). The error is \( x^3 - \tfrac35 x \), with
\[
\begin{aligned}
\norm{x^3 - \tfrac35x}^2 &= \int_{-1}^{1}\Bigl(t^6 - \tfrac65 t^4 + \tfrac{9}{25}t^2\Bigr)\dd t \\
&= \tfrac27 - \tfrac65\cdot\tfrac25 + \tfrac{9}{25}\cdot\tfrac23 = \tfrac27 - \tfrac{6}{25} = \tfrac{8}{175},
\end{aligned}
\]
so \( d(x^3, U) = \sqrt{8/175} = \tfrac{2}{35}\sqrt{14} \approx 0.214 \).

*Check.* The error should be orthogonal to \( U \). Against \( 1 \) and \( x^2 - \tfrac13 \) this holds because \( t^3 - \tfrac35 t \) is odd; against \( x \) it reads \( \int_{-1}^{1}(t^4 - \tfrac35 t^2)\,\dd t = \tfrac25 - \tfrac35\cdot\tfrac23 = 0 \). Notice that the answer is **not** the Taylor polynomial of \( x^3 \) at \( 0 \), which is \( 0 \): Taylor approximates near one point, while \( P_U \) spreads the error over the whole interval.
:::

## Three traps

::: {.warning}
**\( U^{\perp} \) is not the annihilator \( U^{0} \).** Both objects consist of things that "kill" \( U \), but they live in different places: \( U^{\perp} \subseteq V \) is made of **vectors** (@def-orthogonal-complement), while \( U^{0} \subseteq V^{*} \) is made of **functionals** (@def-annihilator). The annihilator exists over every field and needs no extra structure; the orthogonal complement needs an inner product, so it needs \( F = \nR \) or \( F = \nC \). They do have the same dimension, \( \dim V - \dim U \) (@thm-dimension-annihilator, @thm-orthogonal-decomposition (c)), and that is not a coincidence: Section 5 produces an explicit bijection \( U^{\perp} \to U^{0} \). Until then, keep them apart.
:::

::: {.warning}
**"Orthogonal projection" is a special case of Chapter 2's projections, not a synonym.** An operator with \( P^2 = P \) is a projection onto \( \im P \) **along** \( \ker P \) (@def-projection-operator, @thm-projection-direct-sum), and Chapter 4, §05 stressed that the direction matters: on \( \nR^2 \), both \( \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \) and \( \begin{pmatrix} 1 & -1 \\ 0 & 0 \end{pmatrix} \) are projections onto the \( x \)-axis. Only the first is *orthogonal*, because only for the first is the kernel the perpendicular line; the second projects along \( \Span((1,1)) \) and is called **oblique**. So \( P_U \) carries more information than "\( P^2 = P \) and \( \im P = U \)": it also says which complement is used. @thm-projection-formula (b) is the extra property, and Exercise C3 below shows that it singles out the orthogonal projections among all projections.
:::

::: {.warning}
**\( U^{\perp} \) depends on the inner product, not only on \( U \).** In \( \nR^2 \) let \( U = \Span((1, 1)) \). With the dot product, \( U^{\perp} = \Span((1, -1)) \). With the weighted inner product \( \inner{\x}{\y} = 2x_1y_1 + x_2y_2 \), a vector \( (a, b) \) is orthogonal to \( (1, 1) \) when \( 2a + b = 0 \), so \( U^{\perp} = \Span((1, -2)) \). Same subspace, different perpendicular. The symbol \( \perp \) always hides a choice of \( \inner{\cdot}{\cdot} \), and when two inner products are in play the notation must say which.
:::

## Exercises

### A. Check your understanding

:::: {#exr-orthogonal-complements-and-projections-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the orthogonal complement \( S^{\perp} \) of a subset \( S \) of an inner product space.
2. True or false: \( S^{\perp} \) is a subspace only when \( S \) is a subspace. Justify your answer.
3. State the Orthogonal Decomposition Theorem, including every hypothesis.
4. Let \( U \) be a \( 3 \)-dimensional subspace of \( \nR^7 \). What is \( \dim U^{\perp} \), and what is \( \dim(U^{\perp})^{\perp} \)?
5. What quantity does \( P_U\v \) minimize, and over what set?
6. Name two differences between \( U^{\perp} \) and the annihilator \( U^{0} \).
:::
::::

::: {.solution}
(a) \( S^{\perp} = \{ \v \in V : \inner{\v}{\s} = 0 \text{ for every } \s \in S \} \) (@def-orthogonal-complement).

(b) False. \( S^{\perp} \) is a subspace for **every** subset \( S \), by @prp-orthogonal-complement-subspace, and it equals \( \Span(S)^{\perp} \). For instance \( \{(1,0,0), (1,1,0)\}^{\perp} = \Span((0,0,1)) \) in \( \nR^3 \).

(c) If \( V \) is an inner product space over \( \nR \) or \( \nC \) and \( U \) is a **finite-dimensional** subspace, then \( V = U \oplus U^{\perp} \) and \( (U^{\perp})^{\perp} = U \); if \( V \) is also finite-dimensional, then \( \dim U^{\perp} = \dim V - \dim U \) (@thm-orthogonal-decomposition). \( V \) itself need not be finite-dimensional.

(d) \( \dim U^{\perp} = 7 - 3 = 4 \) and \( \dim(U^{\perp})^{\perp} = \dim U = 3 \), by @thm-orthogonal-decomposition (c) and (b).

(e) It minimizes \( \norm{\v - \u} \) over \( \u \in U \), and it is the **only** minimizer (@thm-best-approximation).

(f) \( U^{\perp} \) consists of vectors of \( V \), \( U^{0} \) of functionals in \( V^{*} \); and \( U^{\perp} \) needs an inner product (so \( F = \nR \) or \( \nC \)), while \( U^{0} \) is defined over any field. A third difference: \( U^{\perp} \) is a complement of \( U \) inside \( V \), whereas \( U^{0} \) is not a subspace of \( V \) at all.
:::

### B. Practice

:::: {#exr-orthogonal-complements-and-projections-b1}
[B1: A complement and a projection in \( \nR^4 \)]

In \( \nR^4 \) with the dot product, let \( U = \Span\bigl((1, 1, 0, 0),\ (0, 0, 1, 1)\bigr) \).

::: {.enumerate options="label=(\alph*)"}
1. Find a basis of \( U^{\perp} \) and verify the dimension count.
2. Compute \( P_U\v \) and \( d(\v, U) \) for \( \v = (1, 2, 3, 4) \).
3. Verify directly that \( \v - P_U\v \in U^{\perp} \).
:::
::::

::: {.solution}
(a) By @prp-orthogonal-complement-subspace it is enough to be orthogonal to the two spanning vectors, so \( (a, b, c, d) \in U^{\perp} \) means \( a + b = 0 \) and \( c + d = 0 \). Hence
\[
U^{\perp} = \Span\bigl((1, -1, 0, 0),\ (0, 0, 1, -1)\bigr),
\]
these two being independent (look at the first and third entries). So \( \dim U^{\perp} = 2 = 4 - 2 \), as @thm-orthogonal-decomposition (c) requires.

(b) The spanning list of \( U \) is orthogonal, so @cor-projection-orthogonal-basis applies with \( \u_1 = (1,1,0,0) \), \( \u_2 = (0,0,1,1) \), both of squared norm \( 2 \):
\[
P_U\v = \frac{1 + 2}{2}\u_1 + \frac{3 + 4}{2}\u_2 = \Bigl(\tfrac32, \tfrac32, \tfrac72, \tfrac72\Bigr).
\]
Then \( \v - P_U\v = \bigl(-\tfrac12, \tfrac12, -\tfrac12, \tfrac12\bigr) \) and \( d(\v, U) = \sqrt{4 \cdot \tfrac14} = 1 \).

(c) The vector \( \bigl(-\tfrac12, \tfrac12, -\tfrac12, \tfrac12\bigr) \) satisfies \( a + b = 0 \) and \( c + d = 0 \), so it lies in \( U^{\perp} \) by (a).
:::

:::: {#exr-orthogonal-complements-and-projections-b2}
[B2: Distance from a point to a plane]

In \( \nR^3 \) with the dot product, let \( U = \{ (x, y, z) : 2x - y + 2z = 0 \} \) and \( \v = (1, 2, 3) \). Compute \( d(\v, U) \) and \( P_U\v \), and check that \( P_U\v \) lies in \( U \). Hence write down the general formula for the distance from \( \v \) to the plane \( \{ \x : \inner{\x}{\n} = 0 \} \), \( \n \neq \0 \).
::::

::: {.solution}
The plane is \( \{\n\}^{\perp} \) for \( \n = (2, -1, 2) \), and \( \n \in U^{\perp} \) with \( \dim U^{\perp} = 3 - 2 = 1 \) (@thm-orthogonal-decomposition (c)), so \( U^{\perp} = \Span(\n) \). Here \( \inner{\v}{\n} = 2 - 2 + 6 = 6 \) and \( \inner{\n}{\n} = 4 + 1 + 4 = 9 \), so
\[
P_{U^{\perp}}\v = \tfrac69\n = \Bigl(\tfrac43, -\tfrac23, \tfrac43\Bigr), \qquad P_U\v = \v - P_{U^{\perp}}\v = \Bigl(-\tfrac13, \tfrac83, \tfrac53\Bigr).
\]
*Check:* \( 2(-\tfrac13) - \tfrac83 + 2 \cdot \tfrac53 = \tfrac{-2 - 8 + 10}{3} = 0 \), so \( P_U\v \in U \). The distance is \( d(\v, U) = \norm{\tfrac69\n} = \tfrac69 \cdot 3 = 2 \).

In general \( d(\v, U) = \norm{P_{U^{\perp}}\v} = \bigl|\inner{\v}{\n}\bigr| \, \norm{\n} / \norm{\n}^2 = \bigl|\inner{\v}{\n}\bigr|/\norm{\n} \), which for \( \n = (2,-1,2) \) and \( \v = (1,2,3) \) gives \( 6/3 = 2 \).
:::

:::: {#exr-orthogonal-complements-and-projections-b3}
[B3: The best quadratic approximation to a quartic]

On \( \nR[x]_{\le 4} \) with \( \inner{p}{q} = \int_{-1}^{1}p(t)q(t)\,\dd t \), let \( U = \nR[x]_{\le 2} \). Find \( P_U(x^4) \) and \( d(x^4, U) \). *Hint: the orthogonal basis of @exm-best-quadratic-approximation still works.*
::::

::: {.solution}
Use the orthogonal basis \( (1, x, x^2 - \tfrac13) \) of \( U \) from @exm-best-quadratic-approximation, with \( \inner{1}{1} = 2 \) and
\[
\inner{x^2 - \tfrac13}{x^2 - \tfrac13} = \int_{-1}^{1}\Bigl(t^4 - \tfrac23 t^2 + \tfrac19\Bigr)\dd t = \tfrac25 - \tfrac49 + \tfrac29 = \tfrac{8}{45}.
\]
The coefficients against \( x^4 \) are \( \inner{x^4}{1} = \tfrac25 \), \( \inner{x^4}{x} = 0 \) (odd integrand) and
\[
\inner{x^4}{x^2 - \tfrac13} = \int_{-1}^{1}\Bigl(t^6 - \tfrac13 t^4\Bigr)\dd t = \tfrac27 - \tfrac13\cdot\tfrac25 = \tfrac{16}{105}.
\]
By @cor-projection-orthogonal-basis,
\[
P_U(x^4) = \frac{2/5}{2}\cdot 1 + \frac{16/105}{8/45}\Bigl(x^2 - \tfrac13\Bigr) = \tfrac15 + \tfrac67\Bigl(x^2 - \tfrac13\Bigr) = \tfrac67 x^2 - \tfrac{3}{35}.
\]
For the distance, @thm-pythagoras applied to \( x^4 = P_U(x^4) + (x^4 - P_U(x^4)) \) gives \( d^2 = \norm{x^4}^2 - \norm{P_U(x^4)}^2 \). Here \( \norm{x^4}^2 = \int_{-1}^1 t^8\,\dd t = \tfrac29 \) and, the basis being orthogonal,
\[
\norm{P_U(x^4)}^2 = \Bigl(\tfrac15\Bigr)^2 \cdot 2 + \Bigl(\tfrac67\Bigr)^2\cdot\tfrac{8}{45} = \tfrac{2}{25} + \tfrac{32}{245} = \tfrac{258}{1225}.
\]
Hence \( d^2 = \tfrac29 - \tfrac{258}{1225} = \tfrac{2450 - 2322}{11025} = \tfrac{128}{11025} \) and \( d(x^4, U) = \tfrac{8\sqrt2}{105} \approx 0.108 \).
:::

### C. Going deeper

:::: {#exr-orthogonal-complements-and-projections-c1}
[C1: Perp turns sums into intersections]

Let \( U \) and \( W \) be subspaces of an inner product space \( V \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( (U + W)^{\perp} = U^{\perp} \cap W^{\perp} \). (No finiteness is needed.)
2. Assume now that \( V \) is finite-dimensional. Deduce that \( (U \cap W)^{\perp} = U^{\perp} + W^{\perp} \).
:::
::::

::: {.solution}
(a) \( (\subseteq) \) Let \( \v \in (U + W)^{\perp} \). Since \( U \subseteq U + W \) (@thm-subspace-sum), \( \v \) is orthogonal to every element of \( U \), so \( \v \in U^{\perp} \); likewise \( \v \in W^{\perp} \).

\( (\supseteq) \) Let \( \v \in U^{\perp} \cap W^{\perp} \) and let \( \u + \w \in U + W \) with \( \u \in U \), \( \w \in W \). Then \( \inner{\v}{\u + \w} = \inner{\v}{\u} + \inner{\v}{\w} = 0 \), using additivity in the second slot. Hence \( \v \in (U + W)^{\perp} \).

(b) Apply (a) to the subspaces \( U^{\perp} \) and \( W^{\perp} \):
\[
\bigl(U^{\perp} + W^{\perp}\bigr)^{\perp} = (U^{\perp})^{\perp} \cap (W^{\perp})^{\perp} = U \cap W,
\]
where the second equality is @thm-orthogonal-decomposition (b), available because \( V \) is finite-dimensional, so all subspaces are (@thm-subspace-dimension). Now take \( \perp \) of both ends and use @thm-orthogonal-decomposition (b) once more, this time on the subspace \( U^{\perp} + W^{\perp} \):
\[
U^{\perp} + W^{\perp} = \Bigl(\bigl(U^{\perp} + W^{\perp}\bigr)^{\perp}\Bigr)^{\perp} = (U \cap W)^{\perp}.
\]
This proves the second identity.
:::

:::: {#exr-orthogonal-complements-and-projections-c2}
[C2: A subspace with no orthogonal complement]

Let \( V = \nR[x] \), with the **coefficient inner product**
\[
\inner{p}{q} = \sum_{k \ge 0} a_kb_k \quad \text{for } p = \sum_k a_kx^k,\ q = \sum_k b_kx^k,
\]
a finite sum, since a polynomial has only finitely many non-zero coefficients. Let \( U = \{\, p \in V : p(1) = 0 \,\} \).

::: {.enumerate options="label=(\alph*)"}
1. Verify that \( \inner{\cdot}{\cdot} \) is an inner product on \( V \) and that \( U \) is a subspace with \( U \neq V \).
2. Prove that \( U^{\perp} = \{0\} \). Conclude that \( U \oplus U^{\perp} \neq V \), so @thm-orthogonal-decomposition fails without the hypothesis that \( U \) is finite-dimensional.
3. Explain what goes wrong geometrically by exhibiting, for each \( m \ge 1 \), an element \( p_m \in U \) with \( \norm{p_m - 1} = 1/\sqrt{m} \).
:::
::::

::: {.solution}
(a) The form is symmetric and bilinear over \( \nR \) because each term \( a_kb_k \) is, and \( \inner{p}{p} = \sum_k a_k^2 > 0 \) whenever some \( a_k \neq 0 \), that is whenever \( p \neq 0 \). So it is an inner product. The map \( \varepsilon \colon p \mapsto p(1) \) is linear (@thm-evaluation-respects-operations), so \( U = \ker\varepsilon \) is a subspace (@thm-prop-kernel). It is proper, since the constant polynomial \( 1 \) has \( \varepsilon(1) = 1 \neq 0 \).

(b) Note first that \( x^i - x^j \in U \) for all \( i, j \ge 0 \), since \( 1 - 1 = 0 \). Let \( q = \sum_k b_kx^k \in U^{\perp} \). Pairing with \( x^i - x^j \) gives \( b_i - b_j = 0 \), so all the coefficients of \( q \) are equal, say to \( c \). But only finitely many of them are non-zero, and there are infinitely many indices, so \( c = 0 \) and \( q = 0 \). Hence \( U^{\perp} = \{0\} \) and \( U + U^{\perp} = U \neq V \).

(c) Take \( p_m = 1 - \tfrac1m(x + x^2 + \dots + x^m) \). Then \( p_m(1) = 1 - m \cdot \tfrac1m = 0 \), so \( p_m \in U \), while
\[
\norm{p_m - 1}^2 = \Bigl\|\tfrac1m(x + \dots + x^m)\Bigr\|^2 = m \cdot \frac{1}{m^2} = \frac1m .
\]
So the polynomial \( 1 \notin U \) has elements of \( U \) arbitrarily close to it: \( U \) leaves no room outside itself for a perpendicular direction, and the best approximation to \( 1 \) from \( U \) does not exist (the distances \( \norm{1 - p} \) get arbitrarily close to \( 0 \) without reaching it). The obstruction is not the dimension of \( V \) as such but the fact that \( U \) is not *closed*: filling in the missing limits is exactly what the theory of Hilbert spaces does, and there @thm-orthogonal-decomposition is recovered for closed subspaces. That is analysis, not linear algebra, and we do not pursue it.
:::

:::: {#exr-orthogonal-complements-and-projections-c3}
[C3: Which projections are orthogonal]

Let \( V \) be a finite-dimensional inner product space and let \( P \in \cL(V) \) satisfy \( P^2 = P \). Prove that the following are equivalent:

::: {.enumerate options="label=(\alph*)"}
1. \( P = P_U \) for some subspace \( U \);
2. \( \inner{P\u}{\v} = \inner{\u}{P\v} \) for all \( \u, \v \in V \);
3. \( \ker P = (\im P)^{\perp} \).
:::

*Hint: for (b) \( \Rightarrow \) (c), pair a vector of \( \ker P \) with \( P\v \).*
::::

::: {.solution}
(a) \( \Rightarrow \) (b) is @thm-projection-formula (b).

(b) \( \Rightarrow \) (c). \( (\subseteq) \) Let \( \x \in \ker P \) and let \( P\v \in \im P \) be arbitrary. Then
\[
\inner{\x}{P\v} = \conj{\inner{P\v}{\x}} = \conj{\inner{\v}{P\x}} = \conj{\inner{\v}{\0}} = 0,
\]
using (b) in the second equality. So \( \x \in (\im P)^{\perp} \).
\( (\supseteq) \) Let \( \x \in (\im P)^{\perp} \). Then
\[
\inner{P\x}{P\x} = \inner{\x}{P(P\x)} = \inner{\x}{P\x} = 0,
\]
the first equality by (b), the second by \( P^2 = P \), and the third because \( P\x \in \im P \) while \( \x \in (\im P)^{\perp} \). Positive definiteness gives \( P\x = \0 \), so \( \x \in \ker P \).

(c) \( \Rightarrow \) (a). Put \( U = \im P \). By @thm-projection-direct-sum (a), \( V = \im P \oplus \ker P = U \oplus U^{\perp} \), and \( P \) is the identity on \( U \) and zero on \( \ker P = U^{\perp} \). By the uniqueness clause of @thm-projection-direct-sum (b), \( P \) is the projection onto \( U \) along \( U^{\perp} \), which is \( P_U \) by @def-orthogonal-projection.
:::
