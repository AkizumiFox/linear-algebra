# Projective Space

The affine geometry of the first two sections has one flaw, and it is visible in the statement of @thm-flat-intersection-and-join: the formula for the dimension of a join has two cases, because two flats may fail to meet. This section builds a geometry in which that never happens. The construction is entirely linear — a projective space is the set of lines through the origin of a vector space — and the payoff is a dimension formula with no exceptional case at all. Everything here works over an arbitrary field \( F \), and neither analysis nor topology enters.

## Two lines that do not meet

In the affine plane \( \nA^2(\nR) \), take
\[
L_1 = \{(y_1,y_2) : y_2 - y_1 = 0\}, \qquad
L_2 = \{(y_1,y_2) : y_2 - y_1 = 1\} .
\]
A point in both would satisfy \( 0 = 1 \), so \( L_1 \cap L_2 = \emptyset \). Both are flats of dimension \( 1 \) with the same direction space \( \Span((1,1)) \), and their join is the whole plane. So @thm-flat-intersection-and-join (c) is in its second case: \( \dim(L_1 \vee L_2) = 1 + 1 - 1 + 1 = 2 \), with the extra \( +1 \) paid for by the failure to meet, and there is nothing to substitute for \( \dim(L_1 \cap L_2) \), because the empty set has no dimension.

The two lines do have something in common: a direction. They are going the same way, and the natural thing to say is that they meet "at infinity". The whole of this section is the work of turning that phrase into mathematics without losing linearity. The repair, in one sentence: *stop working with points of a vector space and start working with its lines through the origin.*

## The projective space of a vector space

Let \( V \) be a vector space over \( F \). On \( V \setminus \{\0\} \) define
\[
\x \sim \y \quad \text{if and only if} \quad \y = \lambda\x \text{ for some } \lambda \in F, \ \lambda \ne 0 .
\]
This is an equivalence relation (@def-equivalence-relation): it is reflexive with \( \lambda = 1 \); symmetric, because \( \y = \lambda\x \) with \( \lambda \ne 0 \) gives \( \x = \lambda^{-1}\y \); and transitive, because \( \y = \lambda\x \) and \( \z = \mu\y \) give \( \z = (\mu\lambda)\x \) with \( \mu\lambda \ne 0 \), a field having no zero divisors. Note that \( \0 \) had to be removed: it is equivalent only to itself, and keeping it would put a single extra point into every picture with no geometric job.

*A point of projective space is a line through the origin, with the origin itself thrown away.*

::: {#def-projective-space}
[Projective Space]

Let \( V \) be a finite-dimensional vector space over a field \( F \) with \( \dim V = n + 1 \). The **projective space** of \( V \) is the quotient set (@def-quotient-set)
\[
\nP(V) = (V \setminus \{\0\})/{\sim} ,
\]
whose elements are called **points**. The point determined by \( \x \ne \0 \) is written \( [\x] \). The **dimension** of \( \nP(V) \) is
\[
\dim\nP(V) = \dim V - 1 = n ,
\]
so that \( \nP(\{\0\}) = \emptyset \) has dimension \( -1 \). We write \( \nP^n(F) = \nP(F^{n+1}) \) for **projective \( n \)-space over \( F \)**. A projective space of dimension \( 1 \) is a **projective line**, and one of dimension \( 2 \) a **projective plane**.
:::

Two clauses need comment. The shift by one in the dimension is not a decoration: it is what makes a projective line behave like a line and a projective plane like a plane, as @thm-affine-chart is about to confirm. And the convention \( \dim\emptyset = -1 \) looks like a dodge, but it is forced by the same shift — the empty set is \( \nP(\{\0\}) \) and \( \dim\{\0\} = 0 \) — and it will do real work in @thm-projective-dimension-formula.

::: {#prp-projective-points-are-lines}
[Points Are Lines Through the Origin]

Let \( V \) be a finite-dimensional vector space over \( F \). The map \( [\x] \mapsto \Span(\x) \) is a bijection from \( \nP(V) \) onto the set of \( 1 \)-dimensional subspaces of \( V \).
:::

::: {.proof}
*Well defined.* If \( [\x] = [\y] \) then \( \y = \lambda\x \) with \( \lambda \ne 0 \), so \( \Span(\y) = \Span(\x) \) because each of \( \x, \y \) is a scalar multiple of the other. Also \( \x \ne \0 \), so \( \Span(\x) \) has dimension \( 1 \).

*Injective.* If \( \Span(\x) = \Span(\y) \) with \( \x, \y \ne \0 \), then \( \y = \lambda\x \) for some \( \lambda \in F \), and \( \lambda \ne 0 \) since \( \y \ne \0 \). Hence \( [\x] = [\y] \).

*Surjective.* A \( 1 \)-dimensional subspace has a basis \( (\x) \) with \( \x \ne \0 \), and then it is \( \Span(\x) \), the image of \( [\x] \). This proves the proposition.
:::

So a point of \( \nP^2(F) \) is a line through the origin of \( F^3 \), and a "line" of the projective plane will turn out to be a plane through the origin of \( F^3 \). Every statement below can be read twice: once about \( \nP(V) \) and once about subspaces of \( V \).

::: {#def-homogeneous-coordinates}
[Homogeneous Coordinates]

Let \( \x = (x_0, x_1, \dots, x_n) \in F^{n+1} \) be non-zero. The **homogeneous coordinates** of the point \( [\x] \in \nP^n(F) \) are written
\[
[\x] = [x_0 : x_1 : \dots : x_n] ,
\]
the colons recording that only the ratios are determined: for every \( \lambda \ne 0 \),
\[
[x_0 : x_1 : \dots : x_n] = [\lambda x_0 : \lambda x_1 : \dots : \lambda x_n] ,
\]
and not all of \( x_0, \dots, x_n \) are zero.
:::

**Coordinates run from \( 0 \).** In \( F^{n+1} \) we index the entries and the standard basis from \( 0 \), writing \( \x = (x_0, x_1, \dots, x_n) \) and \( \e_0, \dots, \e_n \), and every projective section of this chapter does the same. Subscripts start at \( 1 \) everywhere else in the book; the exception pays for itself here, because it keeps the \( n \) of \( \nP^n(F) \) equal to the dimension while the coordinates number \( n+1 \).

**Examples.**

- \( \nP^0(F) = \nP(F^1) \) has exactly one point, \( [1] \), since every non-zero scalar is a non-zero multiple of \( 1 \). Its dimension is \( 0 \), as a single point should have.
- \( \nP^1(F) \) consists of the points \( [1 : a] \) for \( a \in F \), all distinct, together with the single point \( [0 : 1] \). Indeed if \( x_0 \ne 0 \) then \( [x_0 : x_1] = [1 : x_1/x_0] \), and if \( x_0 = 0 \) then \( x_1 \ne 0 \) and \( [0 : x_1] = [0:1] \).
- \( \nP^1(\nF_2) = \{[1:0], [1:1], [0:1]\} \) has three points. The three lines through the origin of \( \nF_2^2 \) are \( \Span((1,0)) \), \( \Span((1,1)) \), \( \Span((0,1)) \), matching @prp-projective-points-are-lines.
- The degenerate case \( \nP(\{\0\}) = \emptyset \). It is worth keeping, because intersections produce it.

**Non-example by minimal change.** Over \( \nR \), replace the relation by \( \x \approx \y \) when \( \y = \lambda\x \) with \( \lambda > 0 \). This is still an equivalence relation, but the quotient is not \( \nP(V) \): every projective point \( [\x] \) splits into the two classes of \( \x \) and \( -\x \). The clause that fails is the one allowing **every** non-zero \( \lambda \), and what is lost is precisely the identification of a line with itself traversed backwards.

::: {.warning}
**A single homogeneous coordinate means nothing.** The expression "\( x_1 = 3 \)" is not a statement about a point of \( \nP^n(F) \), since \( [1:3:0] = [2:6:0] \) and the second coordinate changed. Only two kinds of statement survive scaling: a ratio such as \( x_1/x_0 \) where \( x_0 \ne 0 \), and the vanishing or non-vanishing of a **homogeneous** expression, such as \( x_1 = 0 \) or \( x_0x_2 - x_1^2 = 0 \). Whenever a formula below names a coordinate, check that it survives replacing \( \x \) by \( \lambda\x \).
:::

## The affine chart, and where the missing points live

Here is the theorem that makes the construction worth doing: projective space is an affine space plus a smaller projective space.

::: {#thm-affine-chart}
[The Standard Affine Chart]

Let \( n \ge 1 \) and let
\[
\begin{aligned}
U_0 &= \{[x_0 : \dots : x_n] \in \nP^n(F) : x_0 \ne 0\}, \\
H_{\infty} &= \{[x_0 : \dots : x_n] \in \nP^n(F) : x_0 = 0\} .
\end{aligned}
\]
Then:

::: {.enumerate options="label=(\alph*)"}
1. both conditions are independent of the representative, and \( \nP^n(F) = U_0 \sqcup H_{\infty} \), a disjoint union;
2. the map \( \iota \colon F^n \to U_0 \), \( \iota(a_1, \dots, a_n) = [1 : a_1 : \dots : a_n] \), is a bijection, with inverse \( [x_0 : \dots : x_n] \mapsto (x_1/x_0, \dots, x_n/x_0) \);
3. \( H_{\infty} = \nP(W) \) with \( W = \{\x \in F^{n+1} : x_0 = 0\} \), so \( H_{\infty} \) has dimension \( n-1 \), and \( [0 : x_1 : \dots : x_n] \mapsto [x_1 : \dots : x_n] \) is a bijection \( H_{\infty} \to \nP^{n-1}(F) \).
:::

\( U_0 \) is the **standard affine chart** and \( H_{\infty} \) the **hyperplane at infinity**.
:::

::: {.idea}
Scaling multiplies \( x_0 \) by a non-zero number, so it cannot create or destroy a zero there: that single observation makes both halves well defined. On the half where \( x_0 \ne 0 \) we may **normalize** \( x_0 \) to \( 1 \), and once \( x_0 = 1 \) the remaining coordinates are no longer ambiguous, which is why the affine points come back one for one. On the other half \( x_0 \) carries no information at all, so it may be deleted, and what is left is one dimension smaller.
:::

::: {.proof}
(a) If \( \y = \lambda\x \) with \( \lambda \ne 0 \) then \( y_0 = \lambda x_0 \), and a product of two elements of a field is zero only if one of them is, so \( y_0 = 0 \) exactly when \( x_0 = 0 \). Hence both defining conditions depend only on the point. Every point satisfies exactly one of them, so the union is disjoint and exhausts \( \nP^n(F) \).

(b) *Well defined:* \( (1, a_1, \dots, a_n) \ne \0 \), and its zeroth entry is \( 1 \ne 0 \), so \( \iota(\a) \in U_0 \).

*Injective:* if \( [1 : \a] = [1 : \a'] \) then \( (1, \a') = \lambda(1, \a) \) for some \( \lambda \ne 0 \); comparing zeroth entries gives \( \lambda = 1 \), hence \( \a' = \a \).

*Surjective:* let \( [\x] \in U_0 \), so \( x_0 \ne 0 \) and \( x_0^{-1} \) exists. Then \( x_0^{-1}\x = (1, x_1/x_0, \dots, x_n/x_0) \), so \( [\x] = \iota(x_1/x_0, \dots, x_n/x_0) \). The displayed formula for the inverse is exactly this computation, and it is independent of the representative because replacing \( \x \) by \( \lambda\x \) multiplies numerator and denominator of each ratio by \( \lambda \).

(c) \( W \) is a subspace of \( F^{n+1} \), being the kernel of the linear functional \( \x \mapsto x_0 \), and \( \dim W = n \) by the Rank-Nullity Theorem (@thm-rank-nullity), the functional being non-zero and hence surjective onto \( F \) (@prp-nonzero-functional-surjective). A non-zero \( \x \) has \( x_0 = 0 \) exactly when \( \x \in W \setminus \{\0\} \), so \( H_{\infty} = \nP(W) \) and \( \dim H_{\infty} = n - 1 \) by @def-projective-space. The stated map is well defined, because deleting the zeroth coordinate turns \( \lambda\x \) into \( \lambda \) times the deletion and cannot produce \( \0 \) from a non-zero \( \x \) with \( x_0 = 0 \); it is injective and surjective because inserting a zeroth coordinate \( 0 \) inverts it. This proves the theorem.
:::

For \( n = 2 \) the statement reads: **the projective plane is the affine plane together with a projective line.** Writing it out, every point of \( \nP^2(F) \) is exactly one of
\[
[1 : a : b] \ \ (a, b \in F), \qquad [0 : 1 : m] \ \ (m \in F), \qquad [0 : 0 : 1] ,
\]
the first family being the affine plane through \( \iota \), and the last two being the line at infinity \( H_\infty \cong \nP^1(F) \), which has \( \lvert F \rvert + 1 \) points when \( F \) is finite. The label \( m \) is chosen deliberately: the next proposition shows \( [0:1:m] \) is the point where all affine lines of slope \( m \) meet.

\begin{center}
\begin{tikzpicture}[scale=1.0, lab/.style={font=\small}]
    % the plane x_0 = 0, drawn first so everything else sits on top of it
    \fill[black!12] (-2.9,-2.35) -- (1.7,-3.15) -- (2.9,-1.45) -- (-1.7,-0.65) -- cycle;
    \draw[thick, black!55] (-2.9,-2.35) -- (1.7,-3.15) -- (2.9,-1.45) -- (-1.7,-0.65) -- cycle;
    \node[lab, black!60] at (3.55,-1.25) {$x_0 = 0$};
    \draw[very thick, black!80] (-1.97,-1.56) -- (1.97,-2.24);
    \draw[very thick, black!80] (-0.55,-2.68) -- (0.55,-1.12);
    % the plane x_0 = 1
    \fill[black!7] (-2.3,1.0) -- (2.3,0.2) -- (3.5,1.9) -- (-1.1,2.7) -- cycle;
    \draw[thick, black!55] (-2.3,1.0) -- (2.3,0.2) -- (3.5,1.9) -- (-1.1,2.7) -- cycle;
    \node[lab, black!60] at (3.1,2.5) {$x_0 = 1$};
    % three lines through the origin that meet the chart
    \draw[thick] (0,-1.9) -- (0.55,1.25); \fill (0.55,1.25) circle (1.6pt);
    \draw[thick, dashed] (0.55,1.25) -- (0.75,2.3);
    \draw[thick] (0,-1.9) -- (-1.2,1.55); \fill (-1.2,1.55) circle (1.6pt);
    \draw[thick, dashed] (-1.2,1.55) -- (-1.45,2.25);
    \draw[thick] (0,-1.9) -- (2.1,0.9); \fill (2.1,0.9) circle (1.6pt);
    \draw[thick, dashed] (2.1,0.9) -- (2.6,1.57);
    \fill (0,-1.9) circle (2pt);
    \node[lab, left] at (-0.12,-1.72) {$\0$};
    \node[lab, align=center] at (0.6,-4.2)
      {each line through $\0$ is one point of $\nP^2(F)$:\\ those meeting the plane $x_0=1$ give the affine chart,\\ those lying inside the plane $x_0 = 0$ give the line at infinity};
\end{tikzpicture}
\end{center}

::: {#prp-completing-an-affine-line}
[Completing an Affine Line]

Let \( a_1, a_2 \in F \) be not both zero, let \( b \in F \), and let
\[
L = \{(y_1, y_2) \in F^2 : a_1y_1 + a_2y_2 = b\} ,
\]
a flat of dimension \( 1 \) in \( \nA^2 \) by @thm-flat-is-solution-set, the single row \( (a_1, a_2) \) being non-zero, with direction space \( \Span((-a_2, a_1)) \). Let \( \varphi(x_0,x_1,x_2) = a_1x_1 + a_2x_2 - bx_0 \) and \( \bar L = \nP(\ker\varphi) \subseteq \nP^2(F) \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \bar L \) is a projective line;
2. \( \iota(L) = \bar L \cap U_0 \), so \( \bar L \) contains a faithful copy of \( L \);
3. \( \bar L \setminus U_0 \) is the single point \( [0 : -a_2 : a_1] \);
4. two such lines \( L, L' \) have the same direction space if and only if \( \bar L \) and \( \bar{L'} \) meet \( H_{\infty} \) in the same point.
:::
:::

::: {.proof}
(a) \( \varphi \) is linear and non-zero, since \( \varphi(0,1,0) = a_1 \) and \( \varphi(0,0,1) = a_2 \) are not both zero. So \( \varphi \) is surjective onto \( F \) (@prp-nonzero-functional-surjective) and \( \dim\ker\varphi = 3 - 1 = 2 \) by @thm-rank-nullity. Hence \( \bar L = \nP(\ker\varphi) \) has dimension \( 1 \).

(b) A point of \( U_0 \) is \( \iota(y_1,y_2) = [1 : y_1 : y_2] \) by @thm-affine-chart (b), and \( \varphi(1, y_1, y_2) = a_1y_1 + a_2y_2 - b \). This vanishes exactly when \( (y_1,y_2) \in L \). Since \( \varphi \) is homogeneous of degree \( 1 \), the vanishing does not depend on the representative.

(c) A point of \( \bar L \setminus U_0 \) has \( x_0 = 0 \) and \( a_1x_1 + a_2x_2 = 0 \) with \( (x_1,x_2) \ne (0,0) \). The solution set of that single non-trivial equation in \( F^2 \) is \( \Span((-a_2,a_1)) \), of dimension \( 1 \), so there is exactly one such projective point, namely \( [0 : -a_2 : a_1] \).

(d) By (c) the point in question is \( [0 : -a_2 : a_1] \), which by @prp-projective-points-are-lines determines and is determined by \( \Span((-a_2,a_1)) \), the direction space of \( L \). This proves the proposition.
:::

Now return to the hook. The lines \( L_1 : y_2 - y_1 = 0 \) and \( L_2 : y_2 - y_1 = 1 \) have \( (a_1, a_2) = (-1, 1) \) and \( b = 0 \) respectively \( b = 1 \), so
\[
\bar L_1 : x_2 - x_1 = 0, \qquad \bar L_2 : x_2 - x_1 - x_0 = 0 .
\]
Subtracting the two equations gives \( x_0 = 0 \), and then \( x_2 = x_1 \) with \( (x_1,x_2) \ne (0,0) \). So
\[
\bar L_1 \cap \bar L_2 = \{[0 : 1 : 1]\} ,
\]
exactly one point, and it lies on the line at infinity. By @prp-completing-an-affine-line (c) that point is \( [0 : -a_2 : a_1] = [0 : -1 : -1] = [0:1:1] \) for both lines, which is their common direction \( \Span((1,1)) \) read as a point. Two parallel lines meet at their shared direction, and nowhere else.

::: {.check}
In \( \nP^2(\nR) \), which point of the line at infinity do all the **vertical** affine lines \( y_1 = c \) pass through, and which point do all lines of slope \( m \) pass through?
:::

::: {.solution}
A vertical line \( y_1 = c \) has \( (a_1, a_2) = (1, 0) \), so by @prp-completing-an-affine-line (c) its point at infinity is \( [0 : -a_2 : a_1] = [0:0:1] \). A line \( y_2 = my_1 + k \), that is \( my_1 - y_2 = -k \), has \( (a_1,a_2) = (m,-1) \) and point at infinity \( [0 : 1 : m] \). So the points of \( H_{\infty} \) are \( [0:1:m] \) for each slope \( m \in \nR \), plus \( [0:0:1] \) for the vertical direction: one point per direction, and the vertical direction is no longer a special case.
:::

## Projective subspaces, and a dimension formula with one case

::: {#def-projective-subspace}
[Projective Subspace]

Let \( V \) be a finite-dimensional vector space over \( F \). A **projective subspace** of \( \nP(V) \) is a subset of the form
\[
\nP(U) = \{[\x] : \x \in U \setminus \{\0\}\}
\]
for a subspace \( U \) of \( V \). Its **dimension** is \( \dim U - 1 \). A projective subspace of dimension \( 0 \) is a **point**, of dimension \( 1 \) a **line**, of dimension \( 2 \) a **plane**, and of dimension \( \dim\nP(V) - 1 \) a **hyperplane**.
:::

The dimension is only well defined if \( U \) can be recovered from \( \nP(U) \). It can, and the reason is worth isolating.

::: {#lem-projective-subspace-determines-subspace}
[A Projective Subspace Remembers Its Subspace]

Let \( U \) and \( W \) be subspaces of \( V \). Then \( \nP(U) \subseteq \nP(W) \) if and only if \( U \subseteq W \); in particular \( \nP(U) = \nP(W) \) forces \( U = W \).
:::

::: {.proof}
\( (\Leftarrow) \) Immediate from the definition.

\( (\Rightarrow) \) Suppose \( \nP(U) \subseteq \nP(W) \) and let \( \x \in U \). If \( \x = \0 \) then \( \x \in W \). Otherwise \( [\x] \in \nP(U) \subseteq \nP(W) \), so \( [\x] = [\w] \) for some \( \w \in W \setminus \{\0\} \), that is \( \x = \lambda\w \) with \( \lambda \ne 0 \); hence \( \x \in W \), \( W \) being a subspace. So \( U \subseteq W \).

For the last claim, apply the equivalence in both directions and use that \( \subseteq \) is antisymmetric. This proves the lemma.
:::

::: {#prp-join-and-meet}
[Meet and Join]

Let \( S = \nP(U) \) and \( T = \nP(W) \) be projective subspaces of \( \nP(V) \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( S \cap T = \nP(U \cap W) \), so an intersection of projective subspaces is a projective subspace;
2. among all projective subspaces containing \( S \cup T \) there is a smallest one, namely \( \nP(U + W) \).
:::

We write \( S \vee T = \nP(U + W) \) and call it the **join** of \( S \) and \( T \).
:::

::: {.proof}
(a) Let \( \x \ne \0 \). By @lem-projective-subspace-determines-subspace applied to \( \Span(\x) \), we have \( [\x] \in \nP(U) \) exactly when \( \x \in U \). Hence \( [\x] \in S \cap T \) exactly when \( \x \in U \) and \( \x \in W \), that is \( \x \in (U \cap W) \setminus \{\0\} \), which says \( [\x] \in \nP(U \cap W) \).

(b) \( U \subseteq U + W \) and \( W \subseteq U + W \), so \( \nP(U+W) \) contains \( S \cup T \) by @lem-projective-subspace-determines-subspace. Conversely, if \( \nP(Y) \supseteq S \cup T \) for a subspace \( Y \), then the same lemma gives \( U \subseteq Y \) and \( W \subseteq Y \), hence \( U + W \subseteq Y \) because \( U + W \) is the smallest subspace containing both (@thm-subspace-sum), and so \( \nP(U+W) \subseteq \nP(Y) \). This proves the proposition.
:::

::: {#thm-projective-dimension-formula}
[Projective Dimension Formula]

Let \( S \) and \( T \) be projective subspaces of a finite-dimensional projective space. Then
\[
\dim(S \vee T) + \dim(S \cap T) = \dim S + \dim T .
\]{#eq-projective-dimension}
There is **no exceptional case**: the identity holds for all \( S \) and \( T \), including when \( S \cap T = \emptyset \), where \( \dim(S \cap T) = -1 \).
:::

::: {.idea}
There is nothing to invent. Write \( S \) and \( T \) as \( \nP(U) \) and \( \nP(W) \), apply Chapter 1's dimension formula to \( U \) and \( W \), and subtract \( 1 \) four times. The only thing that needs watching is the bookkeeping of those four \( -1 \)'s, and the reason the formula has no second case is that two of them cancel against the other two even when \( U \cap W = \{\0\} \) — which is precisely the situation the affine version could not handle.
:::

::: {.proof}
By @def-projective-subspace write \( S = \nP(U) \) and \( T = \nP(W) \); the subspaces \( U \) and \( W \) are uniquely determined by @lem-projective-subspace-determines-subspace. By @prp-join-and-meet, \( S \vee T = \nP(U+W) \) and \( S \cap T = \nP(U \cap W) \). Hence, using @def-projective-subspace four times and @thm-dimension-formula-subspace-dim once,
\[
\begin{aligned}
\dim(S \vee T) + \dim(S \cap T)
&= \bigl(\dim(U+W) - 1\bigr) + \bigl(\dim(U \cap W) - 1\bigr) \\
&= \bigl(\dim U + \dim W\bigr) - 2 \\
&= \bigl(\dim U - 1\bigr) + \bigl(\dim W - 1\bigr) \\
&= \dim S + \dim T .
\end{aligned}
\]
The middle step is @thm-dimension-formula-subspace-dim, which holds for **all** subspaces \( U, W \) with no hypothesis beyond finite dimension. In particular when \( U \cap W = \{\0\} \) the second term on the first line is \( 0 - 1 = -1 \), and the computation is unaffected. This proves the theorem.
:::

Compare the two formulas side by side. For flats \( A, B \) of an affine space, @thm-flat-intersection-and-join (c) gives
\[
\dim(A \vee B) =
\begin{cases}
\dim A + \dim B - \dim(A \cap B), & A \cap B \ne \emptyset, \\
\dim A + \dim B - \dim(\vec A \cap \vec B) + 1, & A \cap B = \emptyset,
\end{cases}
\]
where \( \vec A, \vec B \) are the direction spaces. Two cases, and in the second the intersection has dropped out of the formula entirely, replaced by an intersection of direction spaces and an apologetic \( +1 \). @eq-projective-dimension has one case and needs no directions. That is the whole reason for building projective space, and everything the rest of this chapter does with it rests on this one line.

::: {#cor-two-lines-meet}
[Two Lines in a Projective Plane Meet]

Let \( P \) be a projective plane, that is \( P = \nP(V) \) with \( \dim V = 3 \). Then any two distinct lines of \( P \) meet in exactly one point.
:::

::: {.proof}
Let \( S = \nP(U) \) and \( T = \nP(W) \) be distinct lines, so \( \dim U = \dim W = 2 \) and \( U \ne W \) by @lem-projective-subspace-determines-subspace. Then \( U + W \) contains \( U \) properly: otherwise \( W \subseteq U \), and two subspaces of the same dimension with one inside the other are equal (@thm-dim-impl-eq applied inside \( U \)), contradicting \( U \ne W \). So \( \dim(U + W) \ge 3 \), and \( \dim(U+W) \le \dim V = 3 \), whence \( \dim(U+W) = 3 \) and \( \dim(S \vee T) = 2 \).

By @thm-projective-dimension-formula,
\[
\dim(S \cap T) = \dim S + \dim T - \dim(S \vee T) = 1 + 1 - 2 = 0 ,
\]
and a projective subspace of dimension \( 0 \) is \( \nP(Y) \) with \( \dim Y = 1 \), which by @prp-projective-points-are-lines is a single point. This proves the corollary.
:::

::: {#prp-two-points-determine-a-line}
[Two Points Determine a Line]

Let \( \nP(V) \) be a projective space of dimension at least \( 1 \). Any two distinct points of \( \nP(V) \) lie on exactly one line.
:::

::: {.proof}
Let \( [\x] \ne [\y] \). Then \( \x \) and \( \y \) are linearly independent: a dependence relation with \( \x, \y \ne \0 \) would give \( \y = \lambda\x \) with \( \lambda \ne 0 \), hence \( [\x] = [\y] \). So \( U = \Span(\x, \y) \) has dimension \( 2 \) and \( \nP(U) \) is a line containing both points.

If \( \nP(Y) \) is any line containing both, then \( \x, \y \in Y \) by @lem-projective-subspace-determines-subspace, so \( U \subseteq Y \); and \( \dim Y = 2 = \dim U \), so \( U = Y \) by @thm-dim-impl-eq. This proves the proposition.
:::

The two statements just proved are each other's mirror images: "two distinct points lie on a unique line" and "two distinct lines meet in a unique point". Section 8 will show that this mirroring is not a coincidence.

::: {.remark}
The set \( \nP^2(\nR) \) is also a famous topological object, the real projective plane, and readers who have met it will be expecting words like "compact" and "non-orientable". This chapter does not use them. Nothing here is topological; every argument has been a statement about subspaces of a vector space, valid over any field, including finite ones where topology has nothing to say.
:::

## Counting points

Over a finite field the whole space can be counted, and the count is a useful check on the constructions above.

::: {#prp-projective-point-count}
[The Number of Points of a Finite Projective Space]

Let \( F \) be a finite field with \( q \) elements and let \( n \ge 0 \). Then
\[
\lvert \nP^n(F)\rvert = 1 + q + q^2 + \dots + q^n = \frac{q^{n+1} - 1}{q - 1} .
\]
More generally a projective subspace of dimension \( d \) has \( (q^{d+1}-1)/(q-1) \) points.
:::

::: {.idea}
Count the non-zero vectors and divide by the size of one equivalence class. Every class has the same size, \( q - 1 \), because scaling a fixed non-zero vector by distinct scalars gives distinct vectors. The alternative count, chart by chart, gives the geometric sum directly, and the two agreeing is a check on @thm-affine-chart.
:::

::: {.proof}
A vector of \( F^{n+1} \) is a list of \( n+1 \) entries, each chosen from \( F \) independently, so there are \( q^{n+1} \) of them and \( q^{n+1} - 1 \) non-zero ones.

Fix \( \x \ne \0 \). Its equivalence class is \( \{\lambda\x : \lambda \in F, \lambda \ne 0\} \), and the map \( \lambda \mapsto \lambda\x \) is injective there: if \( \lambda\x = \mu\x \) then \( (\lambda - \mu)\x = \0 \), and \( \x \ne \0 \) forces \( \lambda = \mu \). So every class has exactly \( q - 1 \) elements.

The classes partition \( F^{n+1} \setminus \{\0\} \) (@thm-partition), so the number of classes is \( (q^{n+1}-1)/(q-1) \). That this equals \( 1 + q + \dots + q^n \) follows from
\[
\begin{aligned}
(q-1)(1 + q + \dots + q^n)
&= (q + q^2 + \dots + q^{n+1}) - (1 + q + \dots + q^{n}) \\
&= q^{n+1} - 1 ,
\end{aligned}
\]
the middle terms canceling in pairs. For a projective subspace \( \nP(U) \) of dimension \( d \), the space \( U \) has dimension \( d+1 \), hence \( q^{d+1} \) elements, since a choice of basis puts it in bijection with \( F^{d+1} \) (@cor-coordinate-isomorphism); the same argument applies. This proves the proposition.
:::

The geometric sum is @thm-affine-chart in disguise: the chart contributes \( q^n \) points and the hyperplane at infinity contributes \( \lvert\nP^{n-1}(F)\rvert \), so \( \lvert\nP^n\rvert = q^n + \lvert\nP^{n-1}\rvert \), and unwinding that recursion from \( \lvert\nP^0\rvert = 1 \) gives \( 1 + q + \dots + q^n \).

::: {#exm-fano-plane}
[The Fano plane]

Describe \( \nP^2(\nF_2) \) completely: its points, its lines, how many points lie on each line and how many lines pass through each point. Verify @cor-two-lines-meet and @prp-two-points-determine-a-line by direct count.
:::

::: {.solution}
By @prp-projective-point-count there are \( 1 + 2 + 4 = 7 \) points. Since \( \nF_2^{\times} = \{1\} \), each point has a **unique** non-zero representative, so the points are simply the seven non-zero vectors of \( \nF_2^3 \). Number the point \( [x_0:x_1:x_2] \) by \( 4x_0 + 2x_1 + x_2 \):
\[
\begin{aligned}
1 &= [0{:}0{:}1], & 2 &= [0{:}1{:}0], & 3 &= [0{:}1{:}1], & 4 &= [1{:}0{:}0], \\
5 &= [1{:}0{:}1], & 6 &= [1{:}1{:}0], & 7 &= [1{:}1{:}1]. &&
\end{aligned}
\]
A line is \( \nP(U) \) with \( \dim U = 2 \), and by @prp-projective-point-count it has \( (2^2-1)/(2-1) = 3 \) points. Since \( U = \{\0, \u, \w, \u + \w\} \) for any two distinct non-zero \( \u, \w \in U \), the lines are exactly the triples \( \{\u, \w, \u+\w\} \) of non-zero vectors. There are seven:
\[
\begin{aligned}
&\{1,2,3\}: x_0 = 0, &\quad &\{1,4,5\}: x_1 = 0, \\
&\{2,4,6\}: x_2 = 0, &\quad &\{1,6,7\}: x_0 + x_1 = 0, \\
&\{2,5,7\}: x_0 + x_2 = 0, &\quad &\{3,4,7\}: x_1 + x_2 = 0, \\
&\{3,5,6\}: x_0+x_1+x_2 = 0. &&
\end{aligned}
\]
Each is the kernel of one of the seven non-zero linear functionals on \( \nF_2^3 \), and different functionals have different kernels here because a functional is determined up to a non-zero scalar by its kernel — if \( \ker\varphi = \ker\psi = U \) with \( \dim U = 2 \), then \( \varphi \) and \( \psi \) both vanish on \( U \) and so lie in the annihilator \( U^{0} \) (@def-annihilator), which has dimension \( 3 - 2 = 1 \) by @thm-dimension-annihilator — and the only non-zero scalar here is \( 1 \). So there are exactly seven lines.

*Incidences.* Each of the seven labels appears in exactly three of the seven displayed triples, so every point lies on exactly \( 3 \) lines. The total is consistent: counting incident pairs (point, line through it) by lines gives \( 7 \cdot 3 = 21 \), and counting them by points gives \( 7 \cdot 3 = 21 \) as well.

*The two theorems.* There are \( \binom{7}{2} = 21 \) pairs of points, and each of the \( 7 \) lines contains \( \binom{3}{2} = 3 \) pairs, for \( 21 \) pairs in total; since no pair can be covered twice without two lines sharing two points — which @prp-two-points-determine-a-line forbids — each pair is covered exactly once. Dually there are \( \binom{7}{2} = 21 \) pairs of lines, and each of the \( 7 \) points lies on \( 3 \) lines and so accounts for \( \binom{3}{2} = 3 \) of those pairs, again \( 21 \) in total; no pair of lines is accounted for twice, since two points on both lines would again contradict @prp-two-points-determine-a-line. So every pair of lines meets in exactly one point, as @cor-two-lines-meet says.
:::

\begin{center}
\begin{tikzpicture}[scale=1.1, lab/.style={font=\scriptsize}, pt/.style={circle, fill=black, inner sep=1.5pt}]
    \coordinate (P4) at (2,3.4641);
    \coordinate (P5) at (0,0);
    \coordinate (P6) at (4,0);
    \coordinate (P1) at (1,1.7321);
    \coordinate (P2) at (3,1.7321);
    \coordinate (P3) at (2,0);
    \coordinate (P7) at (2,1.1547);
    \draw[thick] (P4) -- (P5) -- (P6) -- cycle;
    \draw[thick] (P4) -- (P3);
    \draw[thick] (P5) -- (P2);
    \draw[thick] (P6) -- (P1);
    \draw[thick] (P7) circle (1.1547);
    \node[pt] at (P1) {}; \node[pt] at (P2) {}; \node[pt] at (P3) {};
    \node[pt] at (P4) {}; \node[pt] at (P5) {}; \node[pt] at (P6) {};
    \node[pt] at (P7) {};
    \node[lab, above] at ($(P4)+(0,0.12)$) {$4 = [1{:}0{:}0]$};
    \node[lab, left] at ($(P5)+(-0.1,-0.1)$) {$5 = [1{:}0{:}1]$};
    \node[lab, right] at ($(P6)+(0.1,-0.1)$) {$6 = [1{:}1{:}0]$};
    \node[lab, left] at ($(P1)+(-0.15,0.05)$) {$1 = [0{:}0{:}1]$};
    \node[lab, right] at ($(P2)+(0.15,0.05)$) {$2 = [0{:}1{:}0]$};
    \node[lab, below] at ($(P3)+(0,-0.12)$) {$3 = [0{:}1{:}1]$};
    \node[lab, right] at ($(P7)+(0.22,-0.26)$) {$7 = [1{:}1{:}1]$};
    \node[lab, align=center] at (2,-1.15)
      {the Fano plane $\nP^2(\nF_2)$: $7$ points, $7$ lines\\ (three sides, three medians, one circle), $3$ points on each line};
\end{tikzpicture}
\end{center}

In the picture the "midpoint" of two marked points really is their sum: \( 4 + 5 = [0{:}0{:}1] = 1 \), and likewise all round. The circle is the line \( x_0 = 0 \), which under @thm-affine-chart is the line at infinity, so the picture also shows \( \nP^2(\nF_2) \) as the four affine points \( 4, 5, 6, 7 \) of \( \nF_2^2 \) together with the three directions \( 1, 2, 3 \).

::: {.warning}
**A drawing of a finite projective plane is a mnemonic, not a picture.** The seven points of the Fano plane are not points of the Euclidean plane, and the "circle" is a line, not a curve. The only content of the drawing is the incidence data: which triples of the seven labels form a line. Any picture with the same seven triples is the same object, and no metric statement about the drawing means anything.
:::

## Exercises

### A. Check your understanding

::: {#exr-projective-space-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State @def-projective-space, and say why \( \0 \) is removed before taking the quotient.
2. What is \( \dim\nP(V) \) when \( \dim V = 5 \)? What is the dimension of a hyperplane of that projective space, and of what subspace of \( V \) is it the image?
3. Decide whether \( [2 : 4 : 6] = [1 : 2 : 3] \) in \( \nP^2(\nQ) \), and whether \( [0 : 1] = [0 : 2] \) in \( \nP^1(\nF_3) \). Justify your answers.
4. True or false: the condition \( x_1 + x_2 = 1 \) defines a subset of \( \nP^2(\nR) \). Justify your answer.
5. How many points does \( \nP^3(\nF_5) \) have?
:::
:::

::: {.solution}
(a) \( \nP(V) = (V \setminus\{\0\})/{\sim} \) with \( \x \sim \y \) when \( \y = \lambda\x \) for some non-zero \( \lambda \), and \( \dim\nP(V) = \dim V - 1 \). The vector \( \0 \) is removed because its class is \( \{\0\} \) alone, so it would contribute one point whose span \( \Span(\0) = \{\0\} \) is the zero subspace and not a line, and @prp-projective-points-are-lines would fail.

(b) \( \dim\nP(V) = 4 \). A hyperplane has dimension \( 3 \) and is \( \nP(U) \) for a subspace \( U \) of \( V \) with \( \dim U = 4 \).

(c) Yes: \( (2,4,6) = 2\,(1,2,3) \) and \( 2 \ne 0 \) in \( \nQ \). Yes again: \( (0,2) = 2\,(0,1) \) and \( 2 \ne 0 \) in \( \nF_3 \).

(d) False. The expression is not homogeneous: \( (1,1,0) \) satisfies it but \( (2,2,0) \), which represents the same point, does not. Only the vanishing of a homogeneous expression is a condition on points.

(e) \( (5^4 - 1)/(5-1) = 624/4 = 156 \), by @prp-projective-point-count.
:::

### B. Practice

::: {#exr-projective-space-b1}
[B1: Meeting at infinity]

In \( \nP^2(\nR) \), complete each pair of affine lines and find their intersection point, saying in each case whether it lies in the chart \( U_0 \) or at infinity.

::: {.enumerate options="label=(\alph*)"}
1. \( y_2 = 2y_1 + 1 \) and \( y_2 = 2y_1 - 3 \).
2. \( y_2 = 2y_1 + 1 \) and \( y_1 + y_2 = 4 \).
3. \( y_1 = 5 \) and \( y_1 = -2 \).
:::
:::

::: {.solution}
(a) Writing them as \( 2y_1 - y_2 = -1 \) and \( 2y_1 - y_2 = 3 \), @prp-completing-an-affine-line gives \( \bar L_1 : 2x_1 - x_2 + x_0 = 0 \) and \( \bar L_2 : 2x_1 - x_2 - 3x_0 = 0 \). Subtracting, \( 4x_0 = 0 \), so \( x_0 = 0 \) and \( x_2 = 2x_1 \): the point \( [0 : 1 : 2] \), at infinity. This agrees with part (c) of that proposition, since \( (a_1,a_2) = (2,-1) \) gives \( [0 : 1 : 2] \).

(b) Here \( \bar L_1 : 2x_1 - x_2 + x_0 = 0 \) and \( \bar L_2 : x_1 + x_2 - 4x_0 = 0 \). Adding, \( 3x_1 - 3x_0 = 0 \), so \( x_1 = x_0 \); then \( x_2 = 4x_0 - x_1 = 3x_0 \). Taking \( x_0 = 1 \) gives \( [1 : 1 : 3] \), which lies in \( U_0 \) and corresponds to the affine point \( (1,3) \). Check: \( 3 = 2\cdot1 + 1 \) and \( 1 + 3 = 4 \).

(c) \( \bar L_1 : x_1 - 5x_0 = 0 \) and \( \bar L_2 : x_1 + 2x_0 = 0 \). Subtracting, \( 7x_0 = 0 \), so \( x_0 = 0 \) and then \( x_1 = 0 \), forcing \( x_2 \ne 0 \): the point \( [0:0:1] \), at infinity, the vertical direction.
:::

::: {#exr-projective-space-b2}
[B2: Joins and meets]

In \( \nP^4(F) \), let \( S \) be a plane and \( T \) a plane.

::: {.enumerate options="label=(\alph*)"}
1. What are the possible values of \( \dim(S \cap T) \)? Justify each.
2. Show that two planes in \( \nP^4(F) \) always meet.
3. Give an example in \( \nP^5(F) \) of two planes that do not meet.
:::
:::

::: {.solution}
Throughout, \( S = \nP(U) \) and \( T = \nP(W) \) with \( \dim U = \dim W = 3 \) inside a space of dimension \( 5 \) (for \( \nP^4 \)).

(a) By @thm-projective-dimension-formula, \( \dim(S \cap T) = 4 - \dim(S \vee T) \). Now \( S \vee T \) contains \( S \), so \( \dim(S \vee T) \ge 2 \), and it is contained in \( \nP^4 \), so \( \dim(S\vee T) \le 4 \). Hence \( \dim(S \cap T) \in \{0, 1, 2\} \), and all three occur: \( 2 \) when \( S = T \); \( 1 \) when \( U \cap W \) has dimension \( 2 \), for instance \( U = \Span(\e_1,\e_2,\e_3) \), \( W = \Span(\e_1,\e_2,\e_4) \); and \( 0 \) for \( U = \Span(\e_1,\e_2,\e_3) \), \( W = \Span(\e_3,\e_4,\e_5) \).

(b) The computation in (a) shows \( \dim(S \cap T) \ge 4 - 4 = 0 > -1 \), so \( S \cap T \ne \emptyset \).

(c) In \( \nP^5(F) = \nP(F^6) \) take \( U = \Span(\e_1,\e_2,\e_3) \) and \( W = \Span(\e_4,\e_5,\e_6) \). Then \( U \cap W = \{\0\} \), so \( S \cap T = \nP(\{\0\}) = \emptyset \), and indeed @thm-projective-dimension-formula gives \( \dim(S \vee T) + (-1) = 2 + 2 \), that is \( \dim(S\vee T) = 5 \), the whole space.
:::

::: {#exr-projective-space-b3}
[B3: A projective plane over three elements]

Let \( F = \nF_3 \).

::: {.enumerate options="label=(\alph*)"}
1. How many points does \( \nP^2(\nF_3) \) have, and how many lines?
2. How many points lie on each line, and how many lines pass through each point?
3. List the four points of the line \( x_0 = 0 \).
:::
:::

::: {.solution}
(a) By @prp-projective-point-count, \( \lvert\nP^2(\nF_3)\rvert = 1 + 3 + 9 = 13 \). A line is \( \nP(U) \) with \( \dim U = 2 \), equivalently the kernel of a non-zero functional on \( \nF_3^3 \), and two non-zero functionals have the same kernel exactly when they are proportional (@cor-same-null-space-iff-same-row-space applied to the \( 1 \times 3 \) matrices, or directly: a kernel of dimension \( 2 \) determines the functional up to scale). So the lines correspond to the points of \( \nP((\nF_3^3)^{*}) \), of which there are again \( 13 \).

(b) Each line has \( (3^2-1)/(3-1) = 4 \) points. For the lines through a fixed point \( [\x] \): they are the \( \nP(U) \) with \( \Span(\x) \subseteq U \) and \( \dim U = 2 \), and every such \( U \) is \( \Span(\x, \y) \) for one of the \( 3^3 - 3 = 24 \) vectors \( \y \notin \Span(\x) \), while two choices \( \y, \y' \) give the same \( U \) exactly when \( \y' \in U \setminus \Span(\x) \), a set of \( 3^2 - 3 = 6 \) vectors. So each point lies on \( 24/6 = 4 \) lines. (Consistently, the incident pairs number \( 13\cdot4 = 52 \) counted by lines and \( 13\cdot4 = 52 \) counted by points.)

(c) The points with \( x_0 = 0 \) are \( [0:x_1:x_2] \) with \( (x_1,x_2) \ne (0,0) \), that is the points of \( \nP^1(\nF_3) \): \( [0:1:0] \), \( [0:1:1] \), \( [0:1:2] \) and \( [0:0:1] \). Four points, as (b) requires.
:::

### C. Going deeper

::: {#exr-projective-space-c1}
[C1: Other charts]

Work in \( \nP^n(F) \) and fix \( j \in \{0, 1, \dots, n\} \). Let \( U_j = \{[\x] : x_j \ne 0\} \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( U_j \) is well defined and in bijection with \( F^n \).
2. Prove that \( U_0 \cup U_1 \cup \dots \cup U_n = \nP^n(F) \).
3. For \( n = 1 \) and \( F = \nR \), describe the point of \( U_1 \) that is missing from \( U_0 \), and the point of \( U_0 \) missing from \( U_1 \). Conclude that the "point at infinity" is not a property of a point, but of a chart.
:::
:::

::: {.solution}
(a) Both parts repeat @thm-affine-chart with the index \( 0 \) replaced by \( j \). Scaling multiplies \( x_j \) by a non-zero scalar, so the condition \( x_j \ne 0 \) is independent of the representative. The bijection is
\[
(a_1, \dots, a_n) \mapsto [a_1 : \dots : a_j : 1 : a_{j+1} : \dots : a_n] ,
\]
with the \( 1 \) in position \( j \); it is injective because comparing the \( j \)-th entries of two proportional representatives forces the scalar to be \( 1 \), and surjective because \( [\x] = [x_j^{-1}\x] \) when \( x_j \ne 0 \).

(b) A point is \( [\x] \) with \( \x \ne \0 \), so some coordinate \( x_j \) is non-zero, and then \( [\x] \in U_j \).

(c) \( \nP^1(\nR) = \{[1:a] : a \in \nR\} \cup \{[0:1]\} \). The chart \( U_0 \) omits exactly \( [0:1] \), and the chart \( U_1 = \{[b:1] : b \in \nR\} \cup \{[1:0]\} \) omits exactly \( [1:0] \). Both omitted points are perfectly ordinary points of \( \nP^1(\nR) \); each is at infinity for one chart and in the affine part of the other. So "at infinity" describes a relation between a point and a chosen chart, not the point itself.
:::

::: {#exr-projective-space-c2}
[C2: Counting subspaces]

Let \( F \) be a finite field with \( q \) elements.

::: {.enumerate options="label=(\alph*)"}
1. Prove that the number of lines in \( \nP^2(F) \) equals the number of points, namely \( q^2 + q + 1 \). *Hint: a line is the kernel of a non-zero functional.*
2. Deduce that every point of \( \nP^2(F) \) lies on exactly \( q+1 \) lines.
3. How many points does a hyperplane of \( \nP^n(F) \) have, and how many points of \( \nP^n(F) \) lie outside it?
:::
:::

::: {.solution}
(a) A line of \( \nP^2(F) \) is \( \nP(U) \) with \( \dim U = 2 \), and by @lem-subspace-cut-out-by-annihilator such a \( U \) is the kernel of a non-zero functional \( \varphi \) on \( F^3 \), since \( \dim U^{0} = 3 - 2 = 1 \) (@thm-dimension-annihilator) and \( U \) is the common kernel of its annihilator. Two non-zero functionals have the same kernel exactly when they are proportional: if \( \ker\varphi = \ker\psi = U \), then \( \varphi \) and \( \psi \) both lie in the \( 1 \)-dimensional space \( U^{0} \), so one is a scalar multiple of the other, and the scalar is non-zero. So lines correspond to points of \( \nP((F^3)^{*}) \), and \( (F^3)^{*} \) has dimension \( 3 \) (@cor-dimension-dual-space); by @prp-projective-point-count there are \( q^2+q+1 \) of them.

(b) Count incident pairs (point, line through it) in two ways. Each line has \( q+1 \) points by @prp-projective-point-count, so the count is \( (q^2+q+1)(q+1) \). By symmetry among the \( q^2+q+1 \) points — or simply dividing — each point lies on \( (q^2+q+1)(q+1)/(q^2+q+1) = q+1 \) lines, provided every point lies on the same number. That last point needs an argument. The lines through a fixed \( [\x] \) are the \( \nP(U) \) with \( \Span(\x) \subseteq U \) and \( \dim U = 2 \), and every such \( U \) is \( \Span(\x, \y) \) for some \( \y \notin \Span(\x) \), of which there are \( q^3 - q \). Two choices \( \y, \y' \) give the same \( U \) exactly when \( \y' \in U \setminus \Span(\x) \), a set of \( q^2 - q \) vectors. So the number of such \( U \) is \( (q^3-q)/(q^2-q) = q+1 \), independently of \( [\x] \).

(c) A hyperplane is \( \nP(U) \) with \( \dim U = n \), so it has \( (q^n-1)/(q-1) = 1 + q + \dots + q^{n-1} \) points. Subtracting from \( 1 + q + \dots + q^n \) leaves \( q^n \) points outside, in agreement with @thm-affine-chart, whose chart \( U_0 \) is exactly the complement of a hyperplane and is in bijection with \( F^n \).
:::

::: {#exr-projective-space-c3}
[C3: Where the affine formula goes wrong]

Let \( A \) and \( B \) be flats of \( \nA^3(F) \).

::: {.enumerate options="label=(\alph*)"}
1. Give two lines in \( \nA^3(F) \) that do not meet and are not parallel, and compute \( \dim(A \vee B) \) from @thm-flat-intersection-and-join.
2. Complete both lines to projective lines in \( \nP^3(F) \) by the recipe of @thm-affine-chart, that is by adding the points with \( x_0 = 0 \) to the projective subspace each spans, and verify @eq-projective-dimension for the completed pair.
3. Explain in one sentence why the projective formula could not have an exceptional case, given @prp-join-and-meet.
:::
:::

::: {.solution}
(a) Take \( A = \{(t, 0, 0) : t \in F\} \) and \( B = \{(0, s, 1) : s \in F\} \). A common point would need third coordinate \( 0 \) and \( 1 \), so \( A \cap B = \emptyset \). Their direction spaces are \( \Span(\e_1) \) and \( \Span(\e_2) \), which are different, so they are not parallel and \( \vec A \cap \vec B = \{\0\} \). The second case of @thm-flat-intersection-and-join (c) gives \( \dim(A \vee B) = 1 + 1 - 0 + 1 = 3 \), the whole of \( \nA^3(F) \).

(b) Under \( \iota \) of @thm-affine-chart, \( A \) becomes \( \{[1:t:0:0]\} \), whose points together with \( [0:1:0:0] \) form \( \nP(U) \) with \( U = \Span\bigl((1,0,0,0), (0,1,0,0)\bigr) \); and \( B \) becomes \( \{[1:0:s:1]\} \), giving \( \nP(W) \) with \( W = \Span\bigl((1,0,0,1), (0,0,1,0)\bigr) \). Now \( U \cap W = \{\0\} \): a vector of \( U \) has third and fourth entries \( 0 \), while a vector \( a(1,0,0,1) + b(0,0,1,0) \) of \( W \) has third entry \( b \) and fourth entry \( a \), so both \( a \) and \( b \) vanish. Hence \( S \cap T = \emptyset \) of dimension \( -1 \), and \( U + W \) has dimension \( 2 + 2 - 0 = 4 \), so \( \dim(S \vee T) = 3 \). Then \( 3 + (-1) = 1 + 1 \), as @eq-projective-dimension requires. The two projective lines still do not meet, which is correct: @cor-two-lines-meet is about a projective **plane**, and these lines do not lie in one.

(c) Because by @prp-join-and-meet both the meet and the join of projective subspaces are again projective subspaces, coming from \( U \cap W \) and \( U + W \), and the vector-space formula @thm-dimension-formula-subspace-dim holds for those with no hypothesis whatever, the empty intersection being simply the case \( U \cap W = \{\0\} \).
:::
