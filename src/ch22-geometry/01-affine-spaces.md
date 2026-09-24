# Affine Spaces and Affine Maps

Every space in this book so far has had a distinguished point: the zero vector. Geometry does not. A plane drawn on paper has no privileged spot, and none of the statements a geometer cares about — three points are collinear, two lines are parallel, this point is the midpoint of that segment — mentions one. This section builds the object that has all the structure of a vector space except the origin, and the maps between such objects. Everything in the rest of the chapter is written in this language.

## A set with no zero in it

Chapter 3 already produced such an object without naming it. Let \( \A \in M_{m \times n}(F) \) and \( \b \in F^m \), and suppose \( \A\x = \b \) is consistent. By @thm-general-solution-structure the solution set is \( \p + N \), where \( N = \nul(\A) \) and \( \p \) is any one solution. When \( \b \ne \0 \) this set is **not** a subspace: it misses \( \0 \), and the sum of two solutions is not a solution. Yet it is not shapeless either. The difference of two solutions is a vector of \( N \), and adding a vector of \( N \) to a solution gives a solution. So the solution set carries an action of \( N \), and \( N \) records exactly how any two solutions differ.

That is the whole structure, and it deserves a name. The only operation is: *subtract two points and get a vector; add a vector to a point and get a point.* Adding two points is meaningless, and so is multiplying a point by a scalar.

*An affine space is a set of points in which differences of points are vectors, and every vector moves every point to exactly one other.*

::: {#def-affine-space}
[Affine Space]

Let \( V \) be a vector space over a field \( F \). An **affine space with direction space \( V \)** is a **non-empty** set \( \cA \), whose elements are called **points**, together with a map
\[
\cA \times \cA \to V, \qquad (P, Q) \mapsto \overrightarrow{PQ},
\]
such that:

::: {.enumerate options="label=(AS\arabic*)"}
1. (**Chasles's relation**) \( \overrightarrow{PQ} + \overrightarrow{QR} = \overrightarrow{PR} \) **for all** \( P, Q, R \in \cA \);
2. **for every** \( P \in \cA \), the map \( \cA \to V \), \( Q \mapsto \overrightarrow{PQ} \), is a **bijection**.
:::

The **dimension** of \( \cA \) is \( \dim \cA \coloneqq \dim V \). For \( P \in \cA \) and \( \v \in V \) we write \( P + \v \) for the unique point \( Q \) with \( \overrightarrow{PQ} = \v \), which exists and is unique by (AS2).
:::

Read the two clauses. (AS1) says that traveling from \( P \) to \( Q \) and then from \( Q \) to \( R \) is traveling from \( P \) to \( R \); it is the one law that makes the arrows behave like displacements. (AS2) says that from any fixed point \( P \), every vector of \( V \) is the displacement to exactly one point: **existence** makes \( \cA \) big enough (the action is *transitive*), **uniqueness** makes it no bigger (the action is *free*). The set \( \cA \) is not a vector space and has no zero; \( V \) is a vector space and has one.

\begin{center}
\begin{tikzpicture}[scale=0.9]
  \fill (0,0) circle (2pt) node[below left] {$P$};
  \fill (3,0.6) circle (2pt) node[below right] {$Q$};
  \fill (1.6,2.2) circle (2pt) node[above] {$R$};
  \draw[->, thick] (0,0) -- (2.85,0.57) node[midway, below] {$\overrightarrow{PQ}$};
  \draw[->, thick] (3,0.6) -- (1.68,2.12) node[midway, right] {$\overrightarrow{QR}$};
  \draw[->, thick, dashed] (0,0) -- (1.52,2.09) node[midway, above left] {$\overrightarrow{PR}$};
\end{tikzpicture}
\end{center}

Two consequences are immediate and will be used constantly.

::: {#lem-chasles-consequences}
[First consequences of Chasles]

Let \( \cA \) be an affine space with direction space \( V \). For all \( P, Q \in \cA \) and \( \u, \w \in V \):

::: {.enumerate options="label=(\alph*)"}
1. \( \overrightarrow{PP} = \0 \), and \( \overrightarrow{QP} = -\overrightarrow{PQ} \);
2. \( P + \0 = P \) and \( (P + \u) + \w = P + (\u + \w) \);
3. \( \overrightarrow{PQ} = \0 \) if and only if \( P = Q \).
:::
:::

::: {.proof}
(a) Taking \( P = Q = R \) in (AS1) gives \( \overrightarrow{PP} + \overrightarrow{PP} = \overrightarrow{PP} \), so \( \overrightarrow{PP} = \0 \) by cancellation in the group \( (V, +) \) (@thm-group-basic-properties). Taking \( R = P \) in (AS1) gives \( \overrightarrow{PQ} + \overrightarrow{QP} = \overrightarrow{PP} = \0 \).

(b) \( P + \0 = P \) restates \( \overrightarrow{PP} = \0 \). For the second identity, put \( Q = P + \u \) and \( R = Q + \w \), so that \( \overrightarrow{PQ} = \u \) and \( \overrightarrow{QR} = \w \). By (AS1), \( \overrightarrow{PR} = \u + \w \), which says \( R = P + (\u + \w) \).

(c) \( (\Leftarrow) \) is (a). \( (\Rightarrow) \) If \( \overrightarrow{PQ} = \0 = \overrightarrow{PP} \), then \( Q = P \) by the injectivity in (AS2).
:::

The clauses in part (b) are the axioms of an action of the additive group of \( V \) on \( \cA \), and the definition is often given that way instead. The two presentations carry the same information.

::: {#prp-affine-space-two-forms}
[The two forms of the definition agree]

Let \( V \) be a vector space over \( F \) and \( \cA \) a non-empty set. Giving a map \( \cA \times \cA \to V \) satisfying (AS1) and (AS2) is the same as giving a map \( \cA \times V \to \cA \), written \( (P, \v) \mapsto P + \v \), such that

::: {.enumerate options="label=(AC\arabic*)"}
1. \( P + \0 = P \) for every \( P \in \cA \);
2. \( (P + \u) + \w = P + (\u + \w) \) for all \( P \in \cA \) and \( \u, \w \in V \);
3. for all \( P, Q \in \cA \) there is **exactly one** \( \v \in V \) with \( P + \v = Q \).
:::

The two constructions are inverse to each other.
:::

::: {.idea}
There is nothing to find: in one direction the addition was already defined after @def-affine-space, in the other the vector \( \overrightarrow{PQ} \) is the one whose uniqueness (AC3) asserts. The work is checking the axioms, and each check is one line.
:::

::: {.proof}
Suppose first that \( (P, Q) \mapsto \overrightarrow{PQ} \) satisfies (AS1) and (AS2), and define \( P + \v \) as after @def-affine-space. Then (AC1) and (AC2) are @lem-chasles-consequences (b), and (AC3) is (AS2), since \( P + \v = Q \) says \( \overrightarrow{PQ} = \v \).

Conversely, suppose \( (P, \v) \mapsto P + \v \) satisfies (AC1)–(AC3), and let \( \overrightarrow{PQ} \) be the unique \( \v \) with \( P + \v = Q \). For (AS1), put \( \u = \overrightarrow{PQ} \) and \( \w = \overrightarrow{QR} \); then by (AC2),
\[
P + (\u + \w) = (P + \u) + \w = Q + \w = R ,
\]
so \( \overrightarrow{PR} = \u + \w \) by the uniqueness in (AC3). For (AS2), fix \( P \). The map \( Q \mapsto \overrightarrow{PQ} \) is surjective because \( \v \) is the image of \( P + \v \), and injective because \( \overrightarrow{PQ} = \overrightarrow{PQ'} = \v \) gives \( Q = P + \v = Q' \).

The two passages are inverse: starting from \( \overrightarrow{\ \cdot\ } \), the constructed addition has \( P + \v = Q \) exactly when \( \overrightarrow{PQ} = \v \), so the difference map it returns is the original one; and starting from an addition, the same equivalence returns it unchanged. This proves the proposition.
:::

::: {.remark}
The converse half used only (AC2) and (AC3), and it could not have used more: (AC1) follows from the other two. Indeed (AC3) with \( Q = P \) gives exactly one \( \v \) with \( P + \v = P \), and that \( \v \) has \( P + (\v + \v) = (P + \v) + \v = P + \v = P \) by (AC2), so \( \v + \v = \v \) by the same uniqueness and \( \v = \0 \). We list (AC1) anyway, because that is how the axioms of a group action are usually written.
:::

Now the examples. The first is the one every other example is modeled on.

::: {#exm-affine-space-basic}
[Four affine spaces]

Check each of the following against @def-affine-space, and say what its direction space and dimension are.

::: {.enumerate options="label=(\alph*)"}
1. A vector space \( V \) over \( F \), with \( \overrightarrow{\x\y} \coloneqq \y - \x \).
2. A coset \( \p + U \) of a subspace \( U \) of \( V \) (@def-coset), with the same difference map.
3. The solution set of a **consistent** system \( \A\x = \b \), \( \A \in M_{m \times n}(F) \).
4. The set \( \nF_2^2 \) of four points, with \( \overrightarrow{\x\y} = \y - \x \).
:::
:::

::: {.solution}
(a) Chasles reads \( (\y - \x) + (\z - \y) = \z - \x \), which is true in any vector space. For fixed \( \x \), the map \( \y \mapsto \y - \x \) is a bijection \( V \to V \) with inverse \( \v \mapsto \x + \v \). Direction space \( V \); dimension \( \dim V \). Here the point \( \x \) and the vector \( \x \) are the same object, and only the language distinguishes them.

(b) The set \( \p + U \) is non-empty (it contains \( \p \)) and the difference of two of its elements is \( (\p + \u) - (\p + \w) = \u - \w \in U \), so the map does land in \( U \). Chasles is again the identity in (a). For fixed \( \x \in \p + U \), the map \( \y \mapsto \y - \x \) is a bijection \( \p + U \to U \): it is injective, and \( \u \in U \) is the image of \( \x + \u \), which lies in \( \p + U \) because \( U \) is closed under addition. Direction space \( U \); dimension \( \dim U \). Over \( \nR \) these are exactly Chapter 18's affine subspaces of \( V \) (@def-affine-hull (b)), with the same dimension.

(c) By @thm-general-solution-structure the solution set is \( \p + \nul(\A) \) for any one solution \( \p \), so this is a special case of (b). Direction space \( \nul(\A) \); dimension \( \nullity(\A) = n - \rank\A \) by @thm-rank-nullity-matrix. Consistency is what makes the set non-empty, and @thm-rouche-capelli says when it holds.

(d) A special case of (a) with \( V = \nF_2^2 \): four points, direction space \( \nF_2^2 \), dimension \( 2 \). It is worth seeing because it is so small. Every pair of distinct points \( P \ne Q \) has \( \overrightarrow{PQ} = \overrightarrow{QP} \), since \( -1 = 1 \) in \( \nF_2 \); the next section will call a coset of a one-dimensional subspace a **line**, and here each such coset has exactly two points. So every one of the \( \binom{4}{2} = 6 \) pairs of distinct points is itself a line, and the six lines fall into three pairs with no point in common.
:::

**A non-example, by minimal change.** Delete one point from the plane: let \( \cA = \nR^2 \setminus \{\0\} \), with \( \overrightarrow{\x\y} = \y - \x \). Chasles still holds, because it is an identity about subtraction. But (AS2) fails: for \( P = (1, 0) \), no point \( Q \) of \( \cA \) has \( \overrightarrow{PQ} = (-1, 0) \), since the only candidate is \( \0 \), which we removed. The map \( Q \mapsto \overrightarrow{PQ} \) is injective but not surjective. It is exactly the transitivity of the action that fails: the set has a hole.

::: {.warning}
**A point is not a vector.** In an affine space there is no zero point; and over a field in which \( 2 \ne 0 \) and \( 3 \ne 0 \) there is no sum \( P + Q \) of two points and no multiple \( 3P \). The only legal expressions are \( \overrightarrow{PQ} \in V \), \( P + \v \in \cA \), and the affine combinations defined below. If you find yourself writing \( P + Q \), you have silently chosen an origin; the next subsection says what that costs.
:::

## Choosing an origin

An affine space looks like its direction space as soon as one point is nominated as the zero. This is the chapter's first named move, and it is used in almost every proof that follows: *to compute, pick an origin; to state a result, do not.*

::: {#prp-choice-of-origin}
[Choice of Origin]

Let \( \cA \) be an affine space with direction space \( V \), and let \( O \in \cA \). Then
\[
\theta_O \colon \cA \to V, \qquad \theta_O(P) = \overrightarrow{OP} ,
\]
is a bijection with \( \theta_O(O) = \0 \), and it carries the affine structure of \( \cA \) to that of \( V \) in @exm-affine-space-basic (a):
\[
\overrightarrow{PQ} = \theta_O(Q) - \theta_O(P) \qquad (P, Q \in \cA).
\]
If \( O' \in \cA \) is another point, then \( \theta_{O'}(P) = \theta_O(P) - \theta_O(O') \) for every \( P \): the two identifications differ by a translation of \( V \).
:::

::: {.proof}
\( \theta_O \) is a bijection by (AS2), and \( \theta_O(O) = \overrightarrow{OO} = \0 \) by @lem-chasles-consequences (a). By Chasles and the same lemma,
\[
\theta_O(Q) - \theta_O(P) = \overrightarrow{OQ} - \overrightarrow{OP} = \overrightarrow{OQ} + \overrightarrow{PO} = \overrightarrow{PQ} .
\]
For the last statement, apply this with \( P \) and \( O' \) in place of \( Q \) and \( P \): \( \theta_{O'}(P) = \overrightarrow{O'P} = \theta_O(P) - \theta_O(O') \).
:::

So an \( n \)-dimensional affine space over \( F \) is a copy of \( F^n \) with the labels rubbed off. Choosing \( O \) writes the labels back on, and any two choices differ by a translation. We write \( \nA^n(F) \) for \( F^n \) regarded as an affine space over itself, and \( \nA^n \) when \( F = \nR \); its points are written \( P = (p_1, \dots, p_n) \), in plain type, even though the same list of numbers written \( \p \) would be a vector.

::: {.warning}
**The identification is never canonical.** @prp-choice-of-origin does not say that \( \cA \) "is" \( V \); it says that each point of \( \cA \) gives one isomorphism, and there are as many as there are points. A statement proved after choosing \( O \) is a statement about \( \cA \) only if it does not depend on which \( O \) was chosen. Checking that independence is a real obligation, and the next subsection is nothing but that check, done once for all.
:::

## Affine combinations

Sums of points are forbidden, and yet the centroid \( \tfrac13(P_1 + P_2 + P_3) \) of a triangle is a genuine point of the plane, independent of any coordinate system. Something with weights adding up to \( 1 \) survives the loss of the origin. Here is the computation that says which expressions survive.

Fix \( O \in \cA \), points \( P_1, \dots, P_k \in \cA \) and scalars \( t_1, \dots, t_k \in F \) with \( s \coloneqq t_1 + \dots + t_k \). Let \( O' \in \cA \) and \( \w = \overrightarrow{OO'} \). Since \( \overrightarrow{O'P_i} = \overrightarrow{O'O} + \overrightarrow{OP_i} = \overrightarrow{OP_i} - \w \),
\[
\sum_{i=1}^{k} t_i \overrightarrow{O'P_i} = \sum_{i=1}^{k} t_i \overrightarrow{OP_i} - s\w ,
\]{#eq-affine-combination-shift}
and therefore, adding this vector to the point \( O' = O + \w \) and using @lem-chasles-consequences (b), we get the companion identity for points.

\[
O' + \sum_{i=1}^{k} t_i \overrightarrow{O'P_i} = \Bigl( O + \sum_{i=1}^{k} t_i \overrightarrow{OP_i} \Bigr) + (1 - s)\w .
\]{#eq-affine-combination-point-shift}
The vector on the left of @eq-affine-combination-shift does not depend on the origin exactly when \( s = 0 \); the point on the left of @eq-affine-combination-point-shift does not depend on it exactly when \( s = 1 \). Both cases are worth a name.

*Weights adding to one make a point; weights adding to zero make a vector; nothing else means anything.*

::: {#def-affine-combination}
[Affine Combination]

Let \( \cA \) be an affine space with direction space \( V \), let \( P_1, \dots, P_k \in \cA \) with \( k \ge 1 \), and let \( t_1, \dots, t_k \in F \).

::: {.enumerate options="label=(\alph*)"}
1. If \( t_1 + \dots + t_k = 1 \), the **affine combination** \( \sum_{i} t_iP_i \) is the **point** \( O + \sum_{i} t_i\overrightarrow{OP_i} \), for any \( O \in \cA \).
2. If \( t_1 + \dots + t_k = 0 \), the expression \( \sum_{i} t_iP_i \) denotes the **vector** \( \sum_{i} t_i\overrightarrow{OP_i} \in V \), for any \( O \in \cA \).
:::

For no other value of \( t_1 + \dots + t_k \) is \( \sum_i t_iP_i \) defined.
:::

In words: the same symbol means a point when the weights add up to \( 1 \) and a vector when they add up to \( 0 \), and the type of the answer is read off from the weights. The simplest instance of (b) is \( k = 2 \) with weights \( (-1, 1) \): the vector \( Q - P \) is \( \overrightarrow{PQ} \). The simplest instance of (a) is \( k = 1 \) with \( t_1 = 1 \), which is \( P_1 \).

::: {#prp-affine-combination-well-defined}
[Affine combinations are exactly the origin-free ones]

With the notation of @def-affine-combination, put \( s = t_1 + \dots + t_k \).

::: {.enumerate options="label=(\alph*)"}
1. If \( s = 1 \), the point \( O + \sum_i t_i\overrightarrow{OP_i} \) is the same for every \( O \in \cA \).
2. If \( s = 0 \), the vector \( \sum_i t_i\overrightarrow{OP_i} \) is the same for every \( O \in \cA \).
3. Suppose \( \dim \cA \ge 1 \). If \( s \ne 1 \), there are points \( P_1, \dots, P_k \) and origins \( O, O' \) for which \( O + \sum_i t_i\overrightarrow{OP_i} \) and \( O' + \sum_i t_i\overrightarrow{O'P_i} \) differ; and if \( s \ne 0 \), the same is true of the vectors \( \sum_i t_i\overrightarrow{OP_i} \).
:::
:::

::: {.proof}
(a) and (b) are @eq-affine-combination-point-shift and @eq-affine-combination-shift with \( 1 - s = 0 \) and \( s = 0 \) respectively, since \( O' \) was an arbitrary point of \( \cA \).

(c) Since \( \dim \cA \ge 1 \), the direction space \( V \) contains some \( \w \ne \0 \). Take any \( O \in \cA \), put \( O' = O + \w \), and take \( P_1 = \dots = P_k = O \), so that \( \overrightarrow{OP_i} = \0 \) for every \( i \). Then @eq-affine-combination-point-shift reads
\[
O' + \sum_i t_i\overrightarrow{O'P_i} = O + (1-s)\w ,
\]
which differs from \( O + \sum_i t_i \overrightarrow{OP_i} = O \) when \( (1-s)\w \ne \0 \), that is, when \( s \ne 1 \), by @lem-chasles-consequences (c). Likewise @eq-affine-combination-shift reads \( \sum_i t_i\overrightarrow{O'P_i} = -s\w \), which differs from \( \sum_i t_i\overrightarrow{OP_i} = \0 \) when \( s \ne 0 \).
:::

Taking \( \cA = V \) over \( \nR \) and \( O = \0 \), part (a) becomes the ordinary vector expression \( \sum_i t_i\x_i \) with \( \sum_i t_i = 1 \), which is Chapter 18's affine combination (@def-affine-hull (a)). So @def-affine-combination extends that notion from a real vector space to an affine space over any field, and adds the companion vector-valued case. Chapter 18's affine hull \( \operatorname{aff} S \) and its description as a coset (@prp-affine-hull-coset) are the real case of the flats of the next section.

::: {.check}
Let \( f \colon \nR \to \nR \) be \( f(x) = 2x + 3 \), which is not linear. Compute \( f(3 \cdot 1 - 2 \cdot 2) \) and \( 3f(1) - 2f(2) \); then compute \( f(1 + 2) \) and \( f(1) + f(2) \). What do the two pairs show?
:::

::: {.solution}
First pair: \( 3 \cdot 1 - 2 \cdot 2 = -1 \) and \( f(-1) = 1 \), while \( 3f(1) - 2f(2) = 3 \cdot 5 - 2 \cdot 7 = 1 \). They agree, and the weights \( 3 \) and \( -2 \) add up to \( 1 \). Second pair: \( f(3) = 9 \), while \( f(1) + f(2) = 5 + 7 = 12 \). They differ, and the weights \( 1 \) and \( 1 \) add up to \( 2 \). So \( f \) respects combinations whose weights add up to \( 1 \) and destroys the others: it is affine but not linear. That is the content of the next subsection.
:::

## Affine maps

Linear maps are the functions that respect the structure of a vector space. Affine maps should be the functions that respect the structure of an affine space, and by @def-affine-combination that structure is: which affine combinations equal which points. So there is only one reasonable definition.

*An affine map is one that can be applied inside an affine combination.*

::: {#def-affine-map}
[Affine Map]

Let \( \cA \) and \( \cB \) be affine spaces over the same field \( F \), with direction spaces \( V \) and \( W \). A map \( f \colon \cA \to \cB \) is **affine** if
\[
f\Bigl( \sum_{i=1}^{k} t_iP_i \Bigr) = \sum_{i=1}^{k} t_i f(P_i)
\]
**for every** \( k \ge 1 \), all \( P_1, \dots, P_k \in \cA \) and all \( t_1, \dots, t_k \in F \) with \( t_1 + \dots + t_k = 1 \).
:::

Both sides are points, by @def-affine-combination (a) applied in \( \cA \) and in \( \cB \). Nothing is asked about weights summing to anything else, and by the Quick check above nothing could be.

The definition quantifies over all \( k \), which is awkward to verify. The next theorem replaces it by a single linear map, and is the result the rest of the chapter uses.

::: {#thm-affine-map-is-linear-plus-translation}
[An Affine Map Is Linear Plus a Translation]

Let \( \cA, \cB \) be affine spaces over \( F \) with direction spaces \( V, W \), and let \( f \colon \cA \to \cB \). The following are equivalent.

::: {.enumerate options="label=(\alph*)"}
1. \( f \) is affine.
2. There is a linear map \( T \colon V \to W \) with \( \overrightarrow{f(P)f(Q)} = T(\overrightarrow{PQ}) \) for all \( P, Q \in \cA \).
3. For **some** \( O \in \cA \) there is a linear map \( T \colon V \to W \) with \( f(P) = f(O) + T(\overrightarrow{OP}) \) for all \( P \in \cA \).
:::

The map \( T \) in (b) and (c) is unique, is the same in both, and does not depend on \( O \). It is called the **linear part** of \( f \) and written \( \vec{f} \).
:::

::: {.idea}
The cycle is (a) \( \Rightarrow \) (c) \( \Rightarrow \) (b) \( \Rightarrow \) (a). For (a) \( \Rightarrow \) (c) we must manufacture a linear map out of a condition about weights, so we need the two vector-space axioms written as affine combinations. They are
\[
O + (\u + \w) = (O + \u) + (O + \w) - O, \qquad O + \lambda\u = \lambda(O + \u) + (1 - \lambda)O ,
\]
whose weights add up to \( 1 - 1 + 1 = 1 \) and \( \lambda + (1 - \lambda) = 1 \). Applying \( f \) to each is additivity and homogeneity of \( T \).
:::

::: {.proof}
(a) \( \Rightarrow \) (c). Fix \( O \in \cA \) and define \( T \colon V \to W \) by \( T(\v) = \overrightarrow{f(O)\, f(O + \v)} \); this is a map because \( O + \v \) is a well-defined point. Then \( f(O + \v) = f(O) + T(\v) \) by the definition of \( +\ \) in \( \cB \), so once \( T \) is shown to be linear, taking \( \v = \overrightarrow{OP} \) gives (c).

*Additivity.* Let \( \u, \w \in V \). The three points \( O + \u \), \( O + \w \), \( O \) with weights \( 1, 1, -1 \) have weight sum \( 1 \), and their affine combination, computed with origin \( O \), is \( O + (\u + \w - \0) = O + (\u + \w) \). Applying (a) and computing the right-hand side with origin \( f(O) \),
\[
\begin{aligned}
f(O + \u + \w) &= f(O + \u) + f(O + \w) - f(O) \\
&= f(O) + \bigl( T(\u) + T(\w) \bigr) ,
\end{aligned}
\]
so \( T(\u + \w) = T(\u) + T(\w) \).

*Homogeneity.* Let \( \lambda \in F \). The two points \( O + \u \) and \( O \) with weights \( \lambda \) and \( 1 - \lambda \) have weight sum \( 1 \), and their affine combination with origin \( O \) is \( O + \lambda\u \). Applying (a) and computing with origin \( f(O) \),
\[
f(O + \lambda\u) = \lambda f(O + \u) + (1 - \lambda)f(O) = f(O) + \lambda T(\u) ,
\]
so \( T(\lambda\u) = \lambda T(\u) \). Hence \( T \) is linear.

(c) \( \Rightarrow \) (b). Let \( O \) and \( T \) be as in (c) and let \( P, Q \in \cA \). Then \( f(P) = f(O) + T(\overrightarrow{OP}) \) and \( f(Q) = f(O) + T(\overrightarrow{OQ}) \), so by @prp-choice-of-origin applied in \( \cB \) with origin \( f(O) \), and then linearity of \( T \),
\[
\overrightarrow{f(P)f(Q)} = T(\overrightarrow{OQ}) - T(\overrightarrow{OP}) = T(\overrightarrow{OQ} - \overrightarrow{OP}) = T(\overrightarrow{PQ}) ,
\]
the last equality by @prp-choice-of-origin in \( \cA \).

(b) \( \Rightarrow \) (a). Let \( T \) be as in (b), let \( \sum_i t_i = 1 \), and put \( X = \sum_i t_iP_i \). Choose any \( O \in \cA \), so that \( \overrightarrow{OX} = \sum_i t_i\overrightarrow{OP_i} \) by @def-affine-combination. Applying (b) to the pairs \( (O, X) \) and \( (O, P_i) \), and then linearity,
\[
\overrightarrow{f(O)f(X)} = T(\overrightarrow{OX}) = \sum_i t_i\, T(\overrightarrow{OP_i}) = \sum_i t_i \overrightarrow{f(O)f(P_i)} .
\]
The right-hand side is, by @def-affine-combination computed in \( \cB \) with origin \( f(O) \), the displacement from \( f(O) \) to \( \sum_i t_if(P_i) \). Hence \( f(X) = \sum_i t_if(P_i) \), which is (a).

*Uniqueness.* Suppose \( T \) and \( T' \) both satisfy (b). Given \( \v \in V \), fix \( O \) and put \( Q = O + \v \); then \( T(\v) = \overrightarrow{f(O)f(Q)} = T'(\v) \). So \( T \) is determined by \( f \), independently of any origin; and a \( T \) satisfying (c) for one \( O \) satisfies (b) by the implication above, hence is this same map. This proves the theorem.
:::

So an affine map is *one linear map plus one displacement*, no more. In \( \nA^n(F) \to \nA^m(F) \) it is
\[
f(\x) = \A\x + \b , \qquad \A \in M_{m \times n}(F),\ \b \in F^m ,
\]
with \( \A \) the matrix of \( \vec{f} \) in the standard bases and \( \b = f(\0) \).

::: {.warning}
**Affine is weaker than linear, and the difference is exactly the origin.** An affine map \( f \colon V \to W \) between *vector spaces* is linear if and only if \( f(\0) = \0 \): if \( f(\x) = T(\x) + \b \) then \( f(\0) = \b \), and \( f \) is linear exactly when \( \b = \0 \). The translation \( \tau(\x) = \x + \b \) with \( \b \ne \0 \) is affine with linear part \( \id_V \) and is **not** linear — Chapter 2 recorded it as @exm-translation, the standard non-example of a linear map. Conversely \( x \mapsto x^2 \) on \( \nR \) fixes \( 0 \) and is not affine: it sends the affine combination \( 2 \cdot 1 + (-1) \cdot 0 = 1 \) to \( 1 \), while \( 2f(1) - f(0) = 2 \).
:::

An affine map is determined by very little, but not by too little. Here is the negative half; the positive half is the subject of the next section.

::: {#exm-affine-maps-agreeing-on-two-points}
[Two points are not enough in the plane]

Let \( f, g \colon \nA^2 \to \nA^2 \) be \( g(x, y) = (x, y) \) and \( f(x, y) = (x + y,\ y) \). Both are affine, being linear. They agree at the two distinct points \( (0, 0) \) and \( (1, 0) \) — indeed at every point of the line \( y = 0 \) — yet \( f(0, 1) = (1, 1) \ne (0, 1) = g(0, 1) \). So two points, even distinct ones, do not determine an affine map of the plane. The count to remember is \( n + 1 \): the next section proves that \( 3 \) suitably chosen points do determine an affine map of the plane, and that \( 2 \) never will.
:::

## The affine group, and the matrix that computes it

Affine maps compose, and the linear part is functorial. That single fact organizes every computation in the chapter.

::: {#thm-affine-group}
[Composition, Inverses, and the Affine Group]

Let \( \cA, \cB, \cC \) be affine spaces over \( F \), and write \( V \) and \( W \) for the direction spaces of \( \cA \) and \( \cB \).

::: {.enumerate options="label=(\alph*)"}
1. If \( f \colon \cA \to \cB \) and \( g \colon \cB \to \cC \) are affine, then \( g \circ f \) is affine and \( \overrightarrow{g \circ f} = \vec{g} \circ \vec{f} \).
2. An affine \( f \colon \cA \to \cB \) is bijective if and only if \( \vec{f} \) is bijective, and then \( f^{-1} \) is affine with \( \overrightarrow{f^{-1}} = (\vec{f})^{-1} \).
3. The bijective affine maps \( \cA \to \cA \) form a group \( \operatorname{Aff}(\cA) \) under composition, and \( f \mapsto \vec{f} \) is a surjective group homomorphism \( \operatorname{Aff}(\cA) \to \GL(V) \) whose kernel is the set of **translations** \( \tau_{\v} \colon P \mapsto P + \v \), \( \v \in V \).
:::
:::

::: {.idea}
Everything is read off from the identity \( \overrightarrow{f(P)f(Q)} = \vec{f}(\overrightarrow{PQ}) \) of @thm-affine-map-is-linear-plus-translation (b), which turns statements about points into statements about vectors. For (c), the kernel consists of the affine maps whose linear part is the identity, and such a map moves every point by the same vector.
:::

::: {.proof}
(a) For \( P, Q \in \cA \), applying @thm-affine-map-is-linear-plus-translation (b) twice,
\[
\overrightarrow{g(f(P))\,g(f(Q))} = \vec{g}\bigl( \overrightarrow{f(P)f(Q)} \bigr) = \vec{g}\bigl( \vec{f}(\overrightarrow{PQ}) \bigr) .
\]
Since \( \vec{g} \circ \vec{f} \) is linear (@thm-composition-linear), condition (b) of that theorem holds for \( g \circ f \) with this map, so \( g \circ f \) is affine and, by the uniqueness clause, \( \overrightarrow{g \circ f} = \vec{g} \circ \vec{f} \).

(b) \( (\Leftarrow) \) Suppose \( \vec{f} \) is bijective. If \( f(P) = f(Q) \) then \( \vec{f}(\overrightarrow{PQ}) = \overrightarrow{f(P)f(Q)} = \0 \), so \( \overrightarrow{PQ} = \0 \) and \( P = Q \) by @lem-chasles-consequences (c); thus \( f \) is injective. For surjectivity, fix \( O \in \cA \) and let \( R \in \cB \). As \( \vec{f} \) is onto, \( \overrightarrow{f(O)R} = \vec{f}(\v) \) for some \( \v \in V \), and then \( f(O + \v) = f(O) + \vec{f}(\v) = R \) by part (c) of @thm-affine-map-is-linear-plus-translation.

\( (\Rightarrow) \) Suppose \( f \) is bijective and fix \( O \in \cA \). If \( \vec{f}(\v) = \0 \), then \( f(O + \v) = f(O) + \0 = f(O) \), so \( O + \v = O \) and \( \v = \0 \); thus \( \vec{f} \) is injective. Given \( \w \in W \), the point \( f(O) + \w \) is \( f(P) \) for some \( P \), and then \( \w = \overrightarrow{f(O)f(P)} = \vec{f}(\overrightarrow{OP}) \); thus \( \vec{f} \) is onto.

For the inverse, let \( R, S \in \cB \) and put \( P = f^{-1}(R) \), \( Q = f^{-1}(S) \). Then \( \vec{f}(\overrightarrow{PQ}) = \overrightarrow{RS} \), so \( \overrightarrow{f^{-1}(R)f^{-1}(S)} = (\vec{f})^{-1}(\overrightarrow{RS}) \). Since \( (\vec{f})^{-1} \) is linear (@thm-inverse-is-linear), \( f^{-1} \) is affine with the stated linear part.

(c) By (a) and (b), \( \operatorname{Aff}(\cA) \) is closed under composition and inverses and contains \( \id_{\cA} \), whose linear part is \( \id_V \); composition of functions is associative, so it is a group (@def-group). By (a) the map \( f \mapsto \vec{f} \) preserves composition, and by (b) it lands in \( \GL(V) \); so it is a homomorphism (@def-group-homomorphism). It is onto: given \( T \in \GL(V) \), fix \( O \) and set \( f(P) = O + T(\overrightarrow{OP}) \), which is affine with \( \vec{f} = T \) by @thm-affine-map-is-linear-plus-translation (c) and bijective by (b).

Its kernel is \( \{ f : \vec{f} = \id_V \} \). Each translation \( \tau_{\v} \) lies there, since \( \overrightarrow{\tau_{\v}(P)\tau_{\v}(Q)} = \overrightarrow{PQ} \) by Chasles. Conversely suppose \( \vec{f} = \id_V \), fix \( O \) and put \( \v = \overrightarrow{O f(O)} \). For any \( P \), Chasles gives
\[
\overrightarrow{P f(P)} = \overrightarrow{PO} + \overrightarrow{O f(O)} + \overrightarrow{f(O) f(P)} = \overrightarrow{PO} + \v + \overrightarrow{OP} = \v ,
\]
so \( f(P) = P + \v = \tau_{\v}(P) \). This proves the theorem.
:::

In coordinates the homomorphism of (c) is visible in the shape of a matrix. Identify \( \x \in F^n \) with the column \( \binom{\x}{1} \in F^{n+1} \) — the points of \( \nA^n(F) \) become the vectors of \( F^{n+1} \) whose last coordinate is \( 1 \).

::: {#prp-affine-map-block-matrix}
[The Block Matrix of an Affine Map]

Let \( f \colon \nA^n(F) \to \nA^m(F) \) be affine, \( f(\x) = \A\x + \b \) with \( \A \in M_{m \times n}(F) \) the matrix of \( \vec f \) and \( \b = f(\0) \). Put
\[
\widehat{f} = \begin{pmatrix} \A & \b \\ \0\tp & 1 \end{pmatrix} \in M_{(m+1) \times (n+1)}(F) .
\]
Then \( \widehat{f}\binom{\x}{1} = \binom{f(\x)}{1} \) for every \( \x \in F^n \); and for affine \( f \colon \nA^n(F) \to \nA^m(F) \) and \( g \colon \nA^m(F) \to \nA^p(F) \) one has \( \widehat{g \circ f} = \widehat{g}\,\widehat{f} \). For \( m = n \), \( f \) is bijective if and only if \( \A \) is invertible, and then
\[
\widehat{f^{-1}} = (\widehat{f})^{-1} = \begin{pmatrix} \A^{-1} & -\A^{-1}\b \\ \0\tp & 1 \end{pmatrix} .
\]
:::

::: {.proof}
Block multiplication (@thm-block-multiplication) gives
\[
\begin{pmatrix} \A & \b \\ \0\tp & 1 \end{pmatrix}\begin{pmatrix} \x \\ 1 \end{pmatrix} = \begin{pmatrix} \A\x + \b \\ 1 \end{pmatrix} ,
\]
which is the first claim. Writing \( g(\y) = \C\y + \d \), the same rule gives
\[
\begin{pmatrix} \C & \d \\ \0\tp & 1 \end{pmatrix}\begin{pmatrix} \A & \b \\ \0\tp & 1 \end{pmatrix} = \begin{pmatrix} \C\A & \C\b + \d \\ \0\tp & 1 \end{pmatrix} ,
\]
and \( (g \circ f)(\x) = \C(\A\x + \b) + \d = (\C\A)\x + (\C\b + \d) \), so the two agree. For \( m = n \): \( f \) is bijective exactly when \( \vec f \) is, by @thm-affine-group (b), and \( \vec f \) is bijective exactly when its matrix \( \A \) is invertible, by @thm-rank-map-equals-rank-matrix (b). In that case \( \x \mapsto \A^{-1}\x - \A^{-1}\b \) is affine and is a two-sided inverse of \( f \), and its block matrix is the one displayed, which is therefore \( (\widehat{f})^{-1} \) by the composition rule.
:::

So composing affine maps is multiplying \( (n+1) \times (n+1) \) matrices, and \( \operatorname{Aff}(\nA^n(F)) \) is a group of such matrices. The last row \( (\0\tp \mid 1) \) is what records "these are points, not vectors"; the projective sections later in this chapter read that row again, as the equation of the hyperplane at infinity, after the extra coordinate is moved from last place to first.

::: {#exm-affine-composition-in-the-plane}
[Composing a shear and a quarter turn]

In \( \nA^2 \) let \( f(\x) = \A\x + \b \) and \( g(\y) = \C\y + \d \), where
\[
\A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}, \quad \b = \begin{pmatrix} 1 \\ -1 \end{pmatrix}, \quad \C = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \quad \d = \begin{pmatrix} 2 \\ 0 \end{pmatrix} .
\]
Compute \( g \circ f \) in block form, and find \( f^{-1} \).
:::

::: {.solution}
The block matrices multiply as
\[
\begin{pmatrix} 0 & -1 & 2 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 2 & 1 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -1 & 3 \\ 1 & 2 & 1 \\ 0 & 0 & 1 \end{pmatrix} ,
\]
so \( (g \circ f)(x, y) = (-y + 3,\ x + 2y + 1) \). **Check directly:** \( f(x,y) = (x + 2y + 1,\ y - 1) \), and applying \( g \) gives \( (-(y-1) + 2,\ x + 2y + 1) = (3 - y,\ x + 2y + 1) \), the same.

For the inverse, \( \A^{-1} = \begin{pmatrix} 1 & -2 \\ 0 & 1 \end{pmatrix} \) and \( -\A^{-1}\b = -\begin{pmatrix} 1 & -2 \\ 0 & 1\end{pmatrix}\begin{pmatrix}1 \\ -1\end{pmatrix} = \begin{pmatrix} -3 \\ 1 \end{pmatrix} \), so \( f^{-1}(x, y) = (x - 2y - 3,\ y + 1) \). **Check:** \( f^{-1}(f(x,y)) = \bigl( (x + 2y + 1) - 2(y - 1) - 3,\ (y-1) + 1 \bigr) = (x, y) \).
:::

Two things have been set up. Affine maps are linear maps that have forgotten where the origin is, and they are computed by one matrix of size one larger. The next section uses both to describe the subsets of an affine space that are themselves affine spaces.

## Exercises

### A. Check your understanding

::: {#exr-affine-spaces-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State Chasles's relation, and deduce \( \overrightarrow{QP} = -\overrightarrow{PQ} \) from it.
2. In an affine space over a field in which \( 2 \ne 0 \) and \( 3 \ne 0 \), which of \( P + Q \), \( 3P \), \( \overrightarrow{PQ} + \overrightarrow{RS} \), \( P + \overrightarrow{QR} \), \( \tfrac12 P + \tfrac12 Q \) are defined? For each defined one, say whether it is a point or a vector.
3. True or false, with a reason: a map \( f \colon \nR^2 \to \nR^2 \) with \( f(\0) = \0 \) is affine if and only if it is linear.
4. An affine map \( f \colon \nA^3 \to \nA^3 \) has \( \vec{f} \) of rank \( 2 \). Is \( f \) injective? Justify your answer.
:::
:::

::: {.solution}
(a) \( \overrightarrow{PQ} + \overrightarrow{QR} = \overrightarrow{PR} \) for all points \( P, Q, R \). Taking \( R = P \) gives \( \overrightarrow{PQ} + \overrightarrow{QP} = \overrightarrow{PP} \), and \( \overrightarrow{PP} = \0 \) by @lem-chasles-consequences (a); hence \( \overrightarrow{QP} = -\overrightarrow{PQ} \).

(b) \( P + Q \) and \( 3P \) are **not** defined: the weights add up to \( 2 \) and to \( 3 \), and under the hypotheses on \( F \) neither sum is \( 0 \) or \( 1 \), so @def-affine-combination gives these expressions no meaning; @prp-affine-combination-well-defined (c) says why nothing could, since for \( \dim\cA \ge 1 \) no such expression is origin-free. \( \overrightarrow{PQ} + \overrightarrow{RS} \) is a vector (a sum in \( V \)). \( P + \overrightarrow{QR} \) is a point. \( \tfrac12P + \tfrac12Q \) is a point, the midpoint, and \( \tfrac12 \) exists because \( 2 \ne 0 \). (The hypotheses on \( F \) are needed: over \( \nF_2 \) the weights of \( P + Q \) add up to \( 2 = 0 \), and @def-affine-combination (b) makes \( P + Q \) the vector \( \overrightarrow{OP} + \overrightarrow{OQ} = \overrightarrow{PQ} \).)

(c) True. An affine map is \( f(\x) = T(\x) + \b \) with \( T \) linear and \( \b = f(\0) \) (@thm-affine-map-is-linear-plus-translation), so \( f(\0) = \0 \) forces \( \b = \0 \) and \( f = T \). Conversely every linear map is affine, with \( \vec f = f \), and sends \( \0 \) to \( \0 \).

(d) No. By @thm-affine-group (b), \( f \) is bijective exactly when \( \vec f \) is, and for an operator on a finite-dimensional space injective, surjective and bijective agree (@thm-invertible-operator-tfae). Here \( \rank \vec f = 2 < 3 \), so \( \vec f \) is not injective; taking \( \v \ne \0 \) in \( \ker \vec f \) and any \( P \), the points \( P \) and \( P + \v \) have the same image, since \( \overrightarrow{f(P) f(P + \v)} = \vec f(\v) = \0 \).
:::

### B. Practice

::: {#exr-affine-spaces-b1}
[B1: Determine which are affine]

Determine which of the following maps are affine. Justify your answer; for each affine one give its linear part, and for each other one name a failing affine combination.

::: {.enumerate options="label=(\alph*)"}
1. \( f \colon \nA^2 \to \nA^2 \), \( f(x, y) = (2x - y + 1,\ 5) \).
2. \( f \colon \nA^2 \to \nA^1 \), \( f(x, y) = xy \).
3. \( f \colon \nA^1 \to \nA^2 \), \( f(t) = (1 - t,\ 2 + 3t) \).
4. \( f \colon \nA^2 \to \nA^2 \), \( f(x, y) = (x + 1,\ \lvert y \rvert) \).
:::
:::

::: {.solution}
(a) Affine: \( f(\x) = \A\x + \b \) with \( \A = \begin{pmatrix} 2 & -1 \\ 0 & 0\end{pmatrix} \) and \( \b = (1, 5) \). Its linear part is \( \x \mapsto \A\x \), of rank \( 1 \).

(b) Not affine. Take the affine combination \( 2(1,1) - 1 \cdot (0,0) = (2, 2) \), with weights \( 2 + (-1) = 1 \). Then \( f(2,2) = 4 \), while \( 2f(1,1) - f(0,0) = 2 \).

(c) Affine: \( f(t) = \A t + \b \) with \( \A = \begin{pmatrix} -1 \\ 3 \end{pmatrix} \) and \( \b = (1, 2) \). Linear part \( t \mapsto (-t, 3t) \), of rank \( 1 \).

(d) Not affine. Take the affine combination \( 2(0,1) - 1 \cdot (0,3) = (0,-1) \), with weights \( 2 + (-1) = 1 \). Then \( f(0,-1) = (1, 1) \), while \( 2f(0,1) - f(0,3) = 2(1,1) - (1,3) = (1, -1) \). The two differ, so \( f \) is not affine. (The first coordinate is affine in \( x \); it is \( \lvert y\rvert \) that fails.)
:::

::: {#exr-affine-spaces-b2}
[B2: Block matrices]

In \( \nA^2 \), let \( r \) be the affine map with \( \widehat{r} = \begin{pmatrix} 0 & -1 & 1 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} \) and let \( \tau \) be the translation by \( (2, 3) \).

::: {.enumerate options="label=(\alph*)"}
1. Write \( r \) and \( \tau \) in the form \( \x \mapsto \A\x + \b \).
2. Compute \( \widehat{\tau \circ r} \) and \( \widehat{r \circ \tau} \), and say whether the two maps are equal.
3. Find all fixed points of \( r \).
:::
:::

::: {.solution}
(a) \( r(x, y) = (-y + 1,\ x) \), that is, \( \A_r = \begin{pmatrix} 0 & -1 \\ 1 & 0\end{pmatrix} \), \( \b_r = (1, 0) \). And \( \tau(x, y) = (x + 2,\ y + 3) \), with \( \A_{\tau} = \I_2 \), \( \b_{\tau} = (2, 3) \).

(b) By @prp-affine-map-block-matrix, \( \widehat{\tau \circ r} = \widehat{\tau}\,\widehat{r} \) and \( \widehat{r \circ \tau} = \widehat{r}\,\widehat{\tau} \):
\[
\widehat{\tau}\,\widehat{r} = \begin{pmatrix} 0 & -1 & 3 \\ 1 & 0 & 3 \\ 0 & 0 & 1\end{pmatrix}, \qquad \widehat{r}\,\widehat{\tau} = \begin{pmatrix} 0 & -1 & -2 \\ 1 & 0 & 2 \\ 0 & 0 & 1\end{pmatrix} .
\]
They differ, so \( \tau \circ r \ne r \circ \tau \). (The linear parts agree; the translation vectors do not, because \( \vec{r} \) moves \( \b_{\tau} \).)

(c) \( r(x,y) = (x,y) \) reads \( -y + 1 = x \) and \( x = y \), so \( x = y = \tfrac12 \). The unique fixed point is \( (\tfrac12, \tfrac12) \). Equivalently, \( (\I - \A_r)\x = \b_r \) with \( \I - \A_r = \begin{pmatrix} 1 & 1 \\ -1 & 1\end{pmatrix} \) invertible.
:::

::: {#exr-affine-spaces-b3}
[B3: The four-point plane]

Let \( \cA = \nF_2^2 \) as in @exm-affine-space-basic (d), with points \( O = (0,0) \), \( P = (1,0) \), \( Q = (0,1) \), \( R = (1,1) \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \overrightarrow{PQ} \) and \( \overrightarrow{QP} \), and explain why they are equal.
2. How many affine combinations of the three points \( O, P, Q \) are there, and which points do they give? (A combination is counted by its list of weights.)
3. How many bijective affine maps \( \cA \to \cA \) are there?
:::
:::

::: {.solution}
(a) \( \overrightarrow{PQ} = Q - P = (0,1) - (1,0) = (1,1) \) and \( \overrightarrow{QP} = P - Q = (1,1) \). They are equal because \( \overrightarrow{QP} = -\overrightarrow{PQ} \) (@lem-chasles-consequences (a)) and \( -\v = \v \) for every \( \v \) over \( \nF_2 \).

(b) A weight list \( (t_0, t_1, t_2) \in \nF_2^3 \) with \( t_0 + t_1 + t_2 = 1 \) has an odd number of ones, so it is one of \( (1,0,0), (0,1,0), (0,0,1), (1,1,1) \): four lists. The first three give \( O, P, Q \), and \( (1,1,1) \) gives \( O + P + Q = (1,1) = R \). So the four affine combinations give the four points, each exactly once.

(c) By @thm-affine-group (c) an affine bijection is a translation composed with a linear one, and the number of pairs \( (T, \v) \in \GL(\nF_2^2) \times \nF_2^2 \) is \( \lvert \GL_2(\nF_2)\rvert \cdot 4 \). A matrix in \( \GL_2(\nF_2) \) has a non-zero first column (3 choices) and a second column outside the span of the first (\( 4 - 2 = 2 \) choices), so \( \lvert\GL_2(\nF_2)\rvert = 6 \) and there are \( 24 \) affine bijections. Since \( \lvert\cA\rvert = 4 \), these are **all** \( 4! = 24 \) permutations of the four points.
:::

### C. Going deeper

::: {#exr-affine-spaces-c1}
[C1: Fixed points]

Let \( f \colon \nA^n \to \nA^n \) be affine, \( f(\x) = \A\x + \b \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( f \) has a fixed point if and only if \( \b \in \col(\I - \A) \), and that the set of fixed points, when non-empty, is a coset of \( \nul(\I - \A) \).
2. Deduce that if \( 1 \) is not an eigenvalue of \( \A \), then \( f \) has exactly one fixed point.
3. Give an affine map of \( \nA^2 \) with no fixed point and linear part \( \ne \id \).
:::
:::

::: {.solution}
(a) \( f(\x) = \x \) says \( \A\x + \b = \x \), that is, \( (\I - \A)\x = \b \). This system is consistent exactly when \( \b \in \col(\I - \A) \) (@thm-consistent-iff-column-span), and then its solution set is \( \p + \nul(\I - \A) \) for any one solution \( \p \), by @thm-general-solution-structure.

(b) If \( 1 \) is not an eigenvalue of \( \A \), then \( \nul(\I - \A) = \{\0\} \), so \( \I - \A \) is invertible (@thm-invertible-tfae). Hence \( (\I - \A)\x = \b \) has the unique solution \( \x = (\I - \A)^{-1}\b \).

(c) Take \( \A = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix} \) and \( \b = (1, 0) \), so \( f(x,y) = (x + 1,\ 2y) \). Then \( \I - \A = \begin{pmatrix} 0 & 0 \\ 0 & -1\end{pmatrix} \) and \( \col(\I - \A) = \Span(\e_2) \), which does not contain \( \b = \e_1 \); so there is no fixed point, by (a). And \( \A \ne \I \).
:::

::: {#exr-affine-spaces-c2}
[C2: Affine maps on two points, over two fields]

Let \( f \colon \cA \to \cB \) be a map of affine spaces over \( F \) that preserves affine combinations of **two** points, that is, \( f((1-t)P + tQ) = (1-t)f(P) + tf(Q) \) for all \( P, Q \in \cA \) and \( t \in F \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( \operatorname{char} F \ne 2 \), then \( f \) is affine. *Hint: run the proof of @thm-affine-map-is-linear-plus-translation, replacing the three-point combination by two two-point ones.*
2. Show that over \( \nF_2 \) the hypothesis is empty, and give a non-affine map \( \nF_2^2 \to \nF_2 \) satisfying it.
:::
:::

::: {.solution}
(a) Fix \( O \in \cA \) and define \( T(\v) = \overrightarrow{f(O)f(O + \v)} \) as in @thm-affine-map-is-linear-plus-translation. Homogeneity is the hypothesis with \( P = O + \v \), \( Q = O \): \( O + \lambda\v = \lambda(O + \v) + (1-\lambda)O \), so \( f(O + \lambda\v) = \lambda f(O+\v) + (1-\lambda)f(O) = f(O) + \lambda T(\v) \), giving \( T(\lambda\v) = \lambda T(\v) \).

For additivity, let \( \u, \w \in V \) and let \( M = \tfrac12(O + \u) + \tfrac12(O + \w) \), which is legal since \( 2 \ne 0 \) in \( F \). With origin \( O \), \( M = O + \tfrac12(\u + \w) \). By the hypothesis, \( f(M) = \tfrac12 f(O + \u) + \tfrac12 f(O + \w) \), which with origin \( f(O) \) reads \( f(M) = f(O) + \tfrac12(T(\u) + T(\w)) \). So \( T\bigl(\tfrac12(\u + \w)\bigr) = \tfrac12\bigl(T(\u) + T(\w)\bigr) \). Applying homogeneity with \( \lambda = 2 \) to the left-hand side gives \( T(\u + \w) = T(\u) + T(\w) \). Hence \( T \) is linear, and \( f(P) = f(O) + T(\overrightarrow{OP}) \) by construction, so \( f \) is affine by @thm-affine-map-is-linear-plus-translation (c).

(b) Over \( \nF_2 \) the only scalars are \( t = 0 \) and \( t = 1 \), for which \( (1-t)P + tQ \) is \( P \) or \( Q \); the required identity then reads \( f(P) = f(P) \) or \( f(Q) = f(Q) \). So every map satisfies the hypothesis. Take \( f \colon \nF_2^2 \to \nF_2 \) with \( f(0,0) = f(1,0) = f(0,1) = 0 \) and \( f(1,1) = 1 \). It is not affine: by @exr-affine-spaces-b3 (b), \( (1,1) \) is the affine combination \( O + P + Q \) of the other three points with weights \( (1,1,1) \), so an affine \( f \) would have \( f(1,1) = f(O) + f(P) + f(Q) = 0 \).
:::

::: {#exr-affine-spaces-c3}
[C3: Conjugating a translation]

Let \( \cA \) be an affine space with direction space \( V \), let \( f \in \operatorname{Aff}(\cA) \) and let \( \v \in V \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( f \circ \tau_{\v} \circ f^{-1} = \tau_{\vec{f}(\v)} \).
2. Hence prove that the translations form a subgroup of \( \operatorname{Aff}(\cA) \) that is carried to itself by every conjugation, and that \( \v \mapsto \tau_{\v} \) is an isomorphism from \( (V, +) \) onto it.
3. Deduce that if \( \dim \cA \ge 2 \), then \( \operatorname{Aff}(\cA) \) is not abelian.
:::
:::

::: {.solution}
(a) Both sides are affine maps \( \cA \to \cA \). By @thm-affine-group (a) the linear part of the left-hand side is \( \vec f \circ \id_V \circ (\vec f)^{-1} = \id_V \), so by the kernel description in @thm-affine-group (c) it is a translation \( \tau_{\u} \) for some \( \u \). To identify \( \u \), fix \( O \in \cA \) and put \( P = f^{-1}(O) \). Then
\[
\u = \overrightarrow{O\,(f \circ \tau_{\v} \circ f^{-1})(O)} = \overrightarrow{f(P)\, f(P + \v)} = \vec{f}(\v) ,
\]
using @thm-affine-map-is-linear-plus-translation (b) and \( \overrightarrow{P(P+\v)} = \v \).

(b) The translations are the kernel of \( f \mapsto \vec f \) (@thm-affine-group (c)), hence a subgroup by @thm-homomorphism-basic-properties, and (a) says every conjugate of a translation is a translation. The map \( \v \mapsto \tau_{\v} \) satisfies \( \tau_{\u} \circ \tau_{\w} = \tau_{\u + \w} \) by @lem-chasles-consequences (b), so it is a homomorphism \( (V, +) \to \operatorname{Aff}(\cA) \); it is onto the translations by definition, and injective because \( \tau_{\v} = \id \) forces \( P + \v = P \), hence \( \v = \0 \).

(c) Since \( \dim V \ge 2 \), pick independent \( \v, \w \in V \) and \( T \in \GL(V) \) with \( T(\v) = \w \) (extend \( \{\v, \w\} \) to a basis of \( V \) by @thm-basis-extension-general, and map that basis to itself with \( \v \) and \( \w \) swapped, using @thm-linear-map-from-any-basis; this \( T \) is invertible because \( T \circ T \) fixes every basis vector and so is \( \id_V \), by the uniqueness in that theorem). By @thm-affine-group (c) there is \( f \in \operatorname{Aff}(\cA) \) with \( \vec f = T \). If \( \operatorname{Aff}(\cA) \) were abelian then \( f \circ \tau_{\v} \circ f^{-1} = \tau_{\v} \), while (a) gives \( \tau_{T(\v)} = \tau_{\w} \); by the injectivity in (b) that forces \( \v = \w \), contradicting independence.
:::
