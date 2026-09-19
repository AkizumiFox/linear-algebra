# Cones and Farkas's Lemma

Chapter 2 answered one question about a linear system completely: \( \A\x = \b \) has a solution exactly when \( \b \) lies in the column space of \( \A \) (@thm-consistent-iff-column-span). Its applications section then hit a wall. Traffic flows cannot be negative, and once the unknowns are required to satisfy \( \x \ge \0 \), the column space is the wrong set to look in. This section finds the right set, which is a **cone**, and answers the new question with the separation theorems of §03: either \( \A\x = \b \) has a non-negative solution, or a single vector \( \y \) certifies that it has none. That is Farkas's lemma, and the next two sections run on it.

One step is harder than it looks. Separation needs a **closed** set, and nothing proved so far says that the relevant cone is closed. Most of the work goes into that step, and the last part of the section shows, with an explicit cone, that it can really fail.

**Throughout, the field is \( \nR \).** Vectors in \( \nR^n \) are columns, \( \inner{\x}{\y} = \y\tp\x \) is the standard inner product, and \( \norm{\cdot} \) is the Euclidean norm it induces, the norm that @thm-nearest-point uses. Convergence \( \y_k \to \y \) means \( \norm{\y_k - \y} \to 0 \), and "closed" is meant in the sequential sense of @def-closed-set: a set \( S \) is closed when every limit of a convergent sequence of points of \( S \) again lies in \( S \). Convergence in this norm is entrywise convergence, by the elementary bound
\[
\lvert y_i\rvert \ \le\ \norm{\y} \ \le\ \lvert y_1\rvert + \dots + \lvert y_n\rvert \qquad \text{for } \y \in \nR^n \text{ and } 1 \le i \le n .
\]{#eq-euclidean-entry-bound}
The left inequality holds because \( y_i^2 \le y_1^2 + \dots + y_n^2 \), and the right one is the triangle inequality for \( \y = y_1\e_1 + \dots + y_n\e_n \). Applied to \( \y_k - \y \), with the algebra of limits of Chapter 15's introduction on the right, it shows that \( \norm{\y_k - \y} \to 0 \) exactly when every entry of \( \y_k - \y \) tends to \( 0 \).

## Convex cones

For a vector with real entries we write \( \x \ge \0 \) when **every entry** of \( \x \) is \( \ge 0 \), and \( \x > \0 \) when every entry is \( > 0 \). The set
\[
\nR^m_{\ge 0} = \{ \x \in \nR^m : \x \ge \0 \}
\]
is the **non-negative orthant**. The relation \( \x \ge \0 \) is an entrywise statement about a vector, and it has nothing to do with the Loewner order \( \A \succeq 0 \) of Chapter 12, which is a statement about a matrix.

Here is the question. Let \( \A \in M_{m \times n}(\nR) \) have columns \( \a_1, \dots, \a_n \). By @thm-matrix-times-vector-columns, \( \A\x = x_1\a_1 + \dots + x_n\a_n \), so
\[
\{ \b \in \nR^m : \A\x = \b \text{ for some } \x \ge \0 \}
= \{ x_1\a_1 + \dots + x_n\a_n : \text{every } x_j \ge 0 \} .
\]
Without the sign condition this set would be the span of the columns, a subspace. With it, the set is closed under addition and under multiplication by **non-negative** scalars, but not under multiplication by \( -1 \). Such sets turn up whenever quantities cannot be negative, so they get a name.

*A cone is a set you may stretch and add in, but never reflect.*

::: {#def-convex-cone}
[Convex Cone]

Let \( V \) be a vector space over \( \nR \). A subset \( K \subseteq V \) is a **convex cone** if \( K \) is **non-empty** and
\[
a\u + b\v \in K \qquad \text{for all } \u, \v \in K \text{ and all real } a, b \ge 0 .
\]
:::

In words: a convex cone contains every **non-negative** combination of two of its members, and hence, by induction on the number of terms, every non-negative combination of finitely many of its members. Three special cases unpack the single condition. Taking \( a = b = 0 \) shows \( \0 \in K \), so every convex cone contains the origin. Taking \( b = 0 \) shows that \( K \) is closed under multiplication by non-negative scalars. Taking \( a = b = 1 \) shows that it is closed under addition, and conversely a non-empty set with these two closure properties is a convex cone.

A convex cone is a convex set in the sense of @def-convex-set: take \( a = 1 - t \) and \( b = t \) with \( 0 \le t \le 1 \). The converse fails, and the next examples show how.

**Examples.** Each is checked against the one condition of the definition.

- **The orthant.** If \( \u, \v \ge \0 \) and \( a, b \ge 0 \), then every entry of \( a\u + b\v \) is a sum of products of non-negative numbers, so \( a\u + b\v \ge \0 \). Hence \( \nR^m_{\ge 0} \) is a convex cone.
- **A half-space through the origin.** Fix \( \a \in \nR^n \) and let \( H = \{ \x : \inner{\x}{\a} \ge 0 \} \). If \( \u, \v \in H \) and \( a, b \ge 0 \), then \( \inner{a\u + b\v}{\a} = a\inner{\u}{\a} + b\inner{\v}{\a} \ge 0 \). So \( H \) is a convex cone. When \( \a \ne \0 \) it is one of the two closed half-spaces bounded by the hyperplane \( \a^{\perp} \).
- **The ice-cream cone.** In \( \nR^{n+1} \), write vectors as \( (\x, t) \) with \( \x \in \nR^n \) and \( t \in \nR \), and let \( L = \{ (\x, t) : \norm{\x}_2 \le t \} \). If \( (\x, t), (\y, s) \in L \) and \( a, b \ge 0 \), the triangle inequality and homogeneity of the norm (@def-norm) give \( \norm{a\x + b\y}_2 \le a\norm{\x}_2 + b\norm{\y}_2 \le at + bs \). So \( L \) is a convex cone. In \( \nR^3 \) it is the round solid cone that gives the family its name.
- **Positive semidefinite matrices.** In the real vector space of real symmetric \( n \times n \) matrices, the set of \( \A \succeq 0 \) is a convex cone. This is part (a) of @exr-positive-definite-matrices-c2. Chapter 12 used the phrase there, and this is the definition it was using.
- **Degenerate cases.** \( \{\0\} \) and \( V \) are convex cones. More generally, **every subspace is a convex cone**, since it is closed under all linear combinations and in particular the non-negative ones. A subspace is the extreme case of a cone that happens to be closed under reflection as well.

**Non-examples by minimal change.** In \( \nR^2 \), take the union of two opposite quadrants, \( Q = \{ \x : x_1x_2 \ge 0 \} \). It is closed under non-negative scaling, since \( (ax_1)(ax_2) = a^2x_1x_2 \). The clause that fails is addition: \( (1, 0) \) and \( (0, -1) \) lie in \( Q \), but their sum \( (1, -1) \) does not. Or keep convexity and lose the scaling: the closed unit disc is convex, but \( 2\e_1 \) is not in it. Or translate the orthant to \( \1 + \nR^2_{\ge 0} \): it is convex and closed under addition, but it does not contain \( \0 \).

**Why this definition.** The scalars must be non-negative. With all real scalars allowed, the definition becomes the definition of a subspace, and the sign information that started this section would be lost. The requirement \( \0 \in K \) is a convention that some authors drop: they call \( \{ \x : \x > \0 \} \) a cone as well. Including the origin costs nothing here and keeps the statements below free of exceptions.

::: {.warning}
**A convex cone need not be closed.** In \( \nR^2 \) let
\[
C = \{ (x, y) : x > 0 \} \cup \{ (0, 0) \} .
\]
It is a convex cone. Let \( \u, \v \in C \) and \( a, b \ge 0 \). The first entry of \( a\u + b\v \) is \( au_1 + bv_1 \ge 0 \). If it is positive, the vector lies in \( C \). If it is zero, then \( au_1 = 0 \) and \( bv_1 = 0 \); since the only member of \( C \) with first entry \( 0 \) is \( \0 \), this forces \( a\u = \0 \) and \( b\v = \0 \), and the sum is \( \0 \in C \). But \( (1/k, 1) \in C \) for every \( k \ge 1 \), while the limit \( (0, 1) \) is not in \( C \). Separating a point from a cone needs the cone to be closed, so closedness must be proved. This particular cone comes back at the end of the section as the image of a closed cone.
:::

The cones in the question at the start of this section are the simplest kind.

::: {#def-finitely-generated-cone}
[Finitely Generated Cone]

Let \( \a_1, \dots, \a_m \) be vectors in a real vector space \( V \). The **cone generated by** them is
\[
\operatorname{cone}(\a_1, \dots, \a_m) = \Bigl\{ \textstyle\sum_{i=1}^{m} x_i\a_i : x_1, \dots, x_m \ge 0 \Bigr\} .
\]
A cone of this form is **finitely generated**. For the empty list we set \( \operatorname{cone}() = \{\0\} \), the value of the empty sum. When \( V = \nR^n \) and \( \A \) is the matrix with columns \( \a_1, \dots, \a_m \), this is \( \{ \A\x : \x \in \nR^m_{\ge 0} \} \), and we also write it \( \operatorname{cone}(\A) \).
:::

It is a convex cone: a non-negative combination of two non-negative combinations of the \( \a_i \) is again one, with coefficients \( ax_i + bx'_i \ge 0 \). It is also the **smallest** convex cone containing \( \a_1, \dots, \a_m \), since any convex cone containing the \( \a_i \) contains all their non-negative combinations, by the remark after @def-convex-cone. The orthant is \( \operatorname{cone}(\e_1, \dots, \e_m) \). A subspace with basis \( \v_1, \dots, \v_k \) is \( \operatorname{cone}(\v_1, -\v_1, \dots, \v_k, -\v_k) \), since \( c\v_i \) is \( c\v_i \) or \( \lvert c\rvert(-\v_i) \) according to the sign of \( c \). The ice-cream cone is **not** finitely generated, a fact we shall neither need nor prove.

::: {.check}
Is \( \operatorname{cone}\bigl((1, 0), (1, 1), (0, 1)\bigr) \) in \( \nR^2 \) the same as \( \operatorname{cone}\bigl((1, 0), (0, 1)\bigr) \)? Is \( \operatorname{cone}\bigl((1, 0), (-1, 0)\bigr) \) a line or a half-line?
:::

::: {.solution}
Both cones are the quadrant \( \nR^2_{\ge 0} \). The second list's cone is the quadrant because \( x_1\e_1 + x_2\e_2 = (x_1, x_2) \). The first contains the second, and every generator of the first lies in the quadrant, which is a convex cone, so the first is contained in the quadrant too. A redundant generator changes nothing. The cone of \( (1, 0) \) and \( (-1, 0) \) is the whole \( x \)-axis \( \{ (t, 0) : t \in \nR \} \), a line: for \( t \ge 0 \) use \( t(1, 0) \), and for \( t < 0 \) use \( \lvert t\rvert(-1, 0) \).
:::

## The dual cone

A certificate that \( \A\x = \b \) has no non-negative solution will be a vector \( \y \) that makes a non-negative inner product with every column of \( \A \) but a negative one with \( \b \). Every non-negative combination of the columns then also has a non-negative inner product with \( \y \), so \( \b \) cannot be such a combination. The set of vectors \( \y \) that pass the first test deserves a name.

*The dual cone of \( K \) is the set of directions that make an angle of at most \( 90^\circ \) with everything in \( K \).*

::: {#def-dual-cone}
[Dual Cone]

Let \( V \) be a finite-dimensional real inner product space and let \( S \subseteq V \) be **any** subset. The **dual cone** of \( S \) is
\[
S^{*} = \{ \y \in V : \inner{\x}{\y} \ge 0 \text{ for every } \x \in S \} .
\]
We write \( S^{**} \) for \( (S^{*})^{*} \).
:::

In words: \( \y \in S^{*} \) when the linear functional \( \inner{\cdot}{\y} \) is non-negative on the whole of \( S \), that is, when \( S \) lies in the closed half-space \( \{ \x : \inner{\x}{\y} \ge 0 \} \). The inner product is what places \( S^{*} \) inside \( V \) rather than in the dual space of Chapter 4 (@thm-functionals-on-fn is the case \( V = \nR^n \)).

::: {.warning}
**\( S^{*} \) is not the dual space.** The star here produces a subset of \( V \) itself, not a space of functionals, and it is defined for any subset, not only for a subspace. For a subspace \( U \) the dual cone is the orthogonal complement: if \( \inner{\u}{\y} \ge 0 \) for every \( \u \in U \), then applying this to \( -\u \in U \) gives \( \inner{\u}{\y} \le 0 \) as well, so \( \inner{\u}{\y} = 0 \), and the converse is immediate. So for a subspace we always write \( U^{\perp} \), never \( U^{*} \).
:::

The basic properties take one line each, and they explain why every dual cone is a good set to separate from.

::: {#prp-dual-cone-basic}
[Basic Properties of the Dual Cone]

Let \( V \) be a finite-dimensional real inner product space and let \( S, T \subseteq V \).

::: {.enumerate options="label=(\alph*)"}
1. \( S^{*} \) is a closed convex cone.
2. If \( S \subseteq T \), then \( T^{*} \subseteq S^{*} \).
3. \( S \subseteq S^{**} \).
4. \( \operatorname{cone}(\a_1, \dots, \a_m)^{*} = \{ \y : \inner{\a_i}{\y} \ge 0 \text{ for } i = 1, \dots, m \} \). In \( \nR^n \), with \( \A \) the matrix of columns \( \a_i \), this is \( \{ \y : \A\tp\y \ge \0 \} \).
:::
:::

::: {.idea}
\( S^{*} \) is the intersection of the sets \( \{ \y : \inner{\x}{\y} \ge 0 \} \), one for each \( \x \in S \). Parts (a), (b) and (d) read off this description (more members of \( S \) mean more conditions, and for a cone the generators suffice), and (c) is the symmetry of the inner product.
:::

::: {.proof}
(a) \( \0 \in S^{*} \), so \( S^{*} \) is non-empty. If \( \y, \z \in S^{*} \) and \( a, b \ge 0 \), then \( \inner{\x}{a\y + b\z} = a\inner{\x}{\y} + b\inner{\x}{\z} \ge 0 \) for every \( \x \in S \), using linearity in the second slot, which holds because the field is \( \nR \). Finally \( S^{*} = \bigcap_{\x \in S}\{ \y : \inner{\x}{\y} \ge 0 \} \) is an intersection of closed half-spaces (all of \( V \) when \( \x = \0 \)), closed by @prp-closed-open-basics (c) and (b), since \( \inner{\x}{\cdot} \) is a linear functional; if \( S = \emptyset \), then \( S^{*} = V \), which is closed.

(b) A vector that is non-negative against every member of \( T \) is in particular non-negative against every member of \( S \).

(c) If \( \x \in S \), then \( \inner{\x}{\y} \ge 0 \) for every \( \y \in S^{*} \), by the definition of \( S^{*} \). Since the inner product is symmetric over \( \nR \), this says \( \inner{\y}{\x} \ge 0 \) for every \( \y \in S^{*} \), which is \( \x \in S^{**} \).

(d) The generators lie in the cone, so (b) gives \( \subseteq \). Conversely, if \( \inner{\a_i}{\y} \ge 0 \) for every \( i \), then \( \inner{\sum x_i\a_i}{\y} = \sum x_i\inner{\a_i}{\y} \ge 0 \) whenever every \( x_i \ge 0 \). The matrix form follows because the \( i \)-th entry of \( \A\tp\y \) is \( \a_i\tp\y = \inner{\a_i}{\y} \).
:::

Part (a) holds for **every** set \( S \), including one that is neither convex nor closed. Part (c) is only an inclusion, and the question of when it is an equality is really the question of this section.

**Examples.**

- **The orthant is its own dual.** By (d), \( (\nR^m_{\ge 0})^{*} = \operatorname{cone}(\e_1, \dots, \e_m)^{*} = \{ \y : \inner{\e_i}{\y} = y_i \ge 0 \text{ for all } i \} = \nR^m_{\ge 0} \).
- **A single generator.** \( \operatorname{cone}(\a)^{*} = \{ \y : \inner{\a}{\y} \ge 0 \} \), a closed half-space when \( \a \ne \0 \). A thin cone has a fat dual.
- **The degenerate cases.** The dual cone of \( \{\0\} \) is all of \( V \), and the dual cone of \( V \) is \( \{\0\} \), because a \( \y \) in it must satisfy \( \inner{-\y}{\y} \ge 0 \), that is \( \norm{\y}^2 \le 0 \). As subspaces, by the warning, we write these as \( \{\0\}^{\perp} = V \) and \( V^{\perp} = \{\0\} \).
- **A wedge in the plane.** For \( K = \operatorname{cone}\bigl((1, 0), (1, 1)\bigr) \), part (d) gives \( K^{*} = \{ \y : y_1 \ge 0,\ y_1 + y_2 \ge 0 \} \). This is the wedge between the directions \( (0, 1) \) and \( (1, -1) \), each of which is perpendicular to one edge of \( K \). @exr-cones-and-farkas-b3 finishes this computation.

## Finitely generated cones are closed

Now the key step. We want to separate a point \( \b \) from \( \operatorname{cone}(\A) \), and §03 separates points only from **closed** convex sets. So we must show that \( \operatorname{cone}(\A) \) is closed.

Here is why that is not obvious. Suppose \( \A\x_k \to \b \) with every \( \x_k \ge \0 \). The obvious move is to take a limit of the \( \x_k \), but they need not converge, or even be bounded. If the columns of \( \A \) are dependent, then \( \A\x_k \) can stay put while \( \x_k \) runs off along the null space. The cure has two parts. First, throw away the dependence, generator by generator, which is the "count, then drop a point" move of @thm-caratheodory adapted to cones. Second, once the columns are independent, prove that \( \x_k \) is recovered from \( \A\x_k \) by a fixed linear map, so that the \( \x_k \) cannot escape.

::: {#thm-conic-caratheodory}
[Carathéodory's Theorem for Cones]

Let \( V \) be a real vector space and let \( \a_1, \dots, \a_m \in V \). Every \( \b \in \operatorname{cone}(\a_1, \dots, \a_m) \) lies in \( \operatorname{cone}(\a_i : i \in S) \) for some set of indices \( S \subseteq \{1, \dots, m\} \) such that the list \( (\a_i)_{i \in S} \) is **linearly independent**. In particular, if \( \dim V = n \), then \( \b \) is a non-negative combination of at most \( n \) of the \( \a_i \).
:::

::: {.idea}
Take a representation of \( \b \) that uses as few generators as possible. If those generators were dependent, a dependence relation could be added to the representation, with a scalar multiple chosen so that one coefficient reaches zero and none goes negative. That removes a generator, which contradicts minimality. It is the move of @thm-caratheodory with a *linear* dependence in place of an affine one, and that difference is why the bound is \( n \) rather than \( n + 1 \).
:::

::: {.proof}
By @def-finitely-generated-cone, \( \b = \sum_{i=1}^{m} x_i\a_i \) with every \( x_i \ge 0 \). Discarding the terms with \( x_i = 0 \), we can write \( \b = \sum_{i \in S} x_i\a_i \) with \( x_i > 0 \) for every \( i \in S \), for some \( S \subseteq \{1, \dots, m\} \). The empty set is allowed, when \( \b = \0 \). Among all such representations choose one with \( \lvert S\rvert \) as small as possible. We claim that \( (\a_i)_{i \in S} \) is linearly independent.

Suppose not. Then there are reals \( c_i \), for \( i \in S \), not all zero, with \( \sum_{i \in S} c_i\a_i = \0 \). Replacing every \( c_i \) by \( -c_i \) if necessary, we may assume that \( c_i > 0 \) for at least one \( i \). Put
\[
t = \min\Bigl\{ \frac{x_i}{c_i} : i \in S,\ c_i > 0 \Bigr\} ,
\]
a minimum over a non-empty finite set, so it exists. It is \( > 0 \), and it is attained at some \( i_0 \in S \). Then
\[
\b = \sum_{i \in S} x_i\a_i - t\sum_{i \in S} c_i\a_i = \sum_{i \in S} (x_i - tc_i)\,\a_i .
\]
Every new coefficient is \( \ge 0 \). If \( c_i \le 0 \), then \( x_i - tc_i \ge x_i > 0 \). If \( c_i > 0 \), then \( t \le x_i/c_i \), so \( x_i - tc_i \ge 0 \). Also \( x_{i_0} - tc_{i_0} = 0 \). Discarding the zero coefficients leaves a representation of \( \b \) with positive coefficients on a subset of \( S \setminus \{i_0\} \), which contradicts the minimality of \( \lvert S \rvert \). Hence \( (\a_i)_{i \in S} \) is linearly independent, and \( \b \in \operatorname{cone}(\a_i : i \in S) \).

If \( \dim V = n \), a linearly independent list in \( V \) has length at most \( n \) by @thm-size-bounds (a), so \( \lvert S\rvert \le n \). This proves the theorem.
:::

The second part is a statement about one cone with independent generators.

::: {#lem-orthant-image-closed}
[Injective Images of the Orthant Are Closed]

Let \( \B \in M_{n \times k}(\nR) \) have **linearly independent columns**. Then \( \operatorname{cone}(\B) = \{ \B\x : \x \in \nR^k_{\ge 0} \} \) is a closed subset of \( \nR^n \).
:::

::: {.idea}
Independent columns make \( \x \mapsto \B\x \) injective, and an injective matrix has a left inverse \( \L \) with \( \L\B = \I_k \). So if \( \B\x_j \) converges, then \( \x_j = \L(\B\x_j) \) converges too, because \( \L \) is a fixed matrix. The limit is still \( \ge \0 \), and it maps to the limit of the \( \B\x_j \). The left inverse is what keeps the \( \x_j \) from running away, and injectivity is exactly what provides it.
:::

::: {.proof}
If \( k = 0 \), the cone is \( \{\0\} \), which is closed. Let \( k \ge 1 \). Since the columns of \( \B \) are linearly independent, @cor-least-squares-unique ((b) \( \Rightarrow \) (c), with \( F = \nR \), where \( \B^{*} = \B\tp \)) shows that \( \B\tp\B \in M_k(\nR) \) is invertible. Put \( \L = (\B\tp\B)^{-1}\B\tp \in M_{k \times n}(\nR) \), so that \( \L\B = \I_k \).

Let \( \y_j \in \operatorname{cone}(\B) \) with \( \y_j \to \y \). Write \( \y_j = \B\x_j \) with \( \x_j \ge \0 \). Then \( \x_j = \L\B\x_j = \L\y_j \). By @eq-euclidean-entry-bound, \( \y_j \to \y \) entrywise. Each entry of \( \L\y_j \) is a fixed linear combination of the entries of \( \y_j \), so by the algebra of limits \( \x_j = \L\y_j \to \L\y \) entrywise. Put \( \x = \L\y \).

Each entry of \( \x_j \) is \( \ge 0 \), and a non-strict inequality survives a limit, so \( \x \ge \0 \). By the same reasoning with the fixed matrix \( \B \), we have \( \y_j = \B\x_j \to \B\x \) entrywise. A convergent sequence of real numbers has only one limit, so \( \B\x = \y \). Hence \( \y = \B\x \) with \( \x \ge \0 \), that is, \( \y \in \operatorname{cone}(\B) \). This proves that the cone is closed.
:::

The two pieces now fit together.

::: {#thm-finitely-generated-cone-closed}
[Finitely Generated Cones Are Closed]

Let \( \a_1, \dots, \a_m \in \nR^n \). Then \( \operatorname{cone}(\a_1, \dots, \a_m) \) is a closed convex cone.
:::

::: {.idea}
By @thm-conic-caratheodory the cone is the union of the cones of its independent sublists. There are finitely many of them, and each is closed by @lem-orthant-image-closed. A finite union of closed sets is closed, by @prp-closed-open-basics (b).
:::

::: {.proof}
Write \( K = \operatorname{cone}(\a_1, \dots, \a_m) \), a convex cone by the remark after @def-finitely-generated-cone. Let \( \cS \) be the set of those \( S \subseteq \{1, \dots, m\} \) for which \( (\a_i)_{i \in S} \) is linearly independent, and for \( S \in \cS \) put \( K_S = \operatorname{cone}(\a_i : i \in S) \). The empty set is in \( \cS \), and \( \cS \) is finite, with at most \( 2^m \) members.

First, \( K = \bigcup_{S \in \cS} K_S \). Each \( K_S \subseteq K \), because a non-negative combination of some of the \( \a_i \) is a non-negative combination of all of them with the remaining coefficients zero. And \( K \subseteq \bigcup_{S} K_S \) is @thm-conic-caratheodory.

Next, each \( K_S \) is closed. If \( S = \emptyset \), then \( K_S = \{\0\} \). Otherwise \( K_S = \operatorname{cone}(\B_S) \), where \( \B_S \) is the matrix whose columns are the \( \a_i \) with \( i \in S \). Those columns are linearly independent, so @lem-orthant-image-closed applies.

Hence \( K \) is a finite union of closed sets, closed by @prp-closed-open-basics (b).
:::

The proof uses no analysis beyond the algebra of limits of Chapter 15's introduction, through @eq-euclidean-entry-bound and the subsequence argument of @prp-closed-open-basics (b). In particular it never uses compactness, fact (A3) (the only compactness in the background would be the equivalence of norms, which fixing the Euclidean norm avoids); a finitely generated cone other than \( \{\0\} \) is unbounded, so compactness had nothing to offer anyway. What the proof uses is **finite generation**, twice: for finitely many pieces, and for writing each piece as the image of an orthant under a matrix with a left inverse. The last part of the section shows that without it the conclusion can fail. In Farkas's lemma below, compactness enters only through the existence half of @thm-nearest-point.

## Farkas's lemma

We can now separate. @thm-separation-point would give some hyperplane between \( \b \) and the cone, but for a cone we want one **through the origin**, with a normal vector whose sign on the cone we control. Both come most cleanly from the nearest point of @thm-nearest-point.

::: {#lem-cone-separation}
[Separating a Point from a Closed Cone]

Let \( V \) be a finite-dimensional real inner product space, let \( K \subseteq V \) be a **closed** convex cone, and let \( \b \in V \) with \( \b \notin K \). Then there is \( \y \in K^{*} \) with \( \inner{\b}{\y} < 0 \).
:::

::: {.idea}
Let \( \p \) be the point of \( K \) nearest to \( \b \), and use \( \y = \p - \b \), the vector from \( \b \) back to the cone. The inequality of @thm-nearest-point says that every point of \( K \) is seen from \( \p \) at an angle of at least \( 90^\circ \) from \( \b \). Because \( K \) is a cone, we may test it against \( \0 \) and \( 2\p \), which shows that the separating hyperplane passes through the origin.
:::

::: {.proof}
\( K \) is non-empty, closed and convex, so by @thm-nearest-point (a) there is a point \( \p \in K \) nearest to \( \b \), and by part (b) of the same theorem
\[
\inner{\b - \p}{\z - \p} \le 0 \qquad \text{for every } \z \in K .
\]{#eq-cone-variational}
Put \( \y = \p - \b \), which is non-zero since \( \p \in K \) and \( \b \notin K \). The points \( \z = \0 \) and \( \z = 2\p \) lie in \( K \), since \( K \) is a cone. Substituting them into @eq-cone-variational gives \( \inner{\b - \p}{\p} \ge 0 \) and \( \inner{\b - \p}{\p} \le 0 \), so \( \inner{\y}{\p} = 0 \). Now @eq-cone-variational reads \( \inner{\b - \p}{\z} \le 0 \), that is \( \inner{\z}{\y} \ge 0 \), for every \( \z \in K \). So \( \y \in K^{*} \). Finally,
\[
\inner{\b}{\y} = \inner{\p - \y}{\y} = \inner{\p}{\y} - \inner{\y}{\y} = -\norm{\y}^2 < 0 ,
\]
since \( \y \ne \0 \). This proves the lemma.
:::

With \( K = \operatorname{cone}(\A) \), the lemma becomes the theorem this section is named after. It is stated for a matrix, since that is how it will be used.

::: {#thm-farkas}
[Farkas's Lemma]

Let \( \A \in M_{m \times n}(\nR) \) and \( \b \in \nR^m \). **Exactly one** of the following has a solution:

::: {.enumerate options="label=(F\arabic*)"}
1. \( \A\x = \b \) with \( \x \in \nR^n \), \( \x \ge \0 \);
2. \( \A\tp\y \ge \0 \) and \( \b\tp\y < 0 \), with \( \y \in \nR^m \).
:::
:::

::: {.idea}
The two systems cannot both be solvable, which is one line of algebra: pair \( \A\x = \b \) with \( \y \). That at least one is solvable is geometry. If (F1) fails, then \( \b \) lies outside the cone of the columns, the cone is closed by @thm-finitely-generated-cone-closed, and @lem-cone-separation produces \( \y \).
:::

::: {.proof}
*Not both.* Suppose \( \A\x = \b \) with \( \x \ge \0 \), and \( \A\tp\y \ge \0 \). Then
\[
\b\tp\y = (\A\x)\tp\y = \x\tp(\A\tp\y) \ge 0 ,
\]
since it is a sum of products of the non-negative entries of \( \x \) and \( \A\tp\y \). So \( \b\tp\y < 0 \) is impossible.

*At least one.* Suppose (F1) has no solution. Let \( K = \operatorname{cone}(\A) \). By @def-finitely-generated-cone, (F1) says exactly that \( \b \in K \), so \( \b \notin K \). By @thm-finitely-generated-cone-closed, \( K \) is a closed convex cone, so @lem-cone-separation gives \( \y \in K^{*} \) with \( \inner{\b}{\y} = \b\tp\y < 0 \). By @prp-dual-cone-basic (d), \( \y \in K^{*} \) means \( \A\tp\y \ge \0 \). So \( \y \) solves (F2). This proves the theorem.
:::

**The geometric reading.** Either \( \b \) lies in the cone spanned by the columns of \( \A \), or there is a hyperplane through the origin, \( \{ \z : \inner{\z}{\y} = 0 \} \), with every column on one side (\( \inner{\a_j}{\y} \ge 0 \)) and \( \b \) strictly on the other (\( \inner{\b}{\y} < 0 \)). The vector \( \y \) is a **certificate of infeasibility**: anyone can check (F2) by multiplying out, and the "not both" computation then proves that (F1) has no solution.

\begin{center}
\begin{tikzpicture}[scale=1.25, lab/.style={font=\small}]
  \fill[black!10] (0,0) -- (3.2,0.64) -- (1.33,3.0) -- cycle;
  \draw[->, gray] (-1.9,0) -- (3.4,0);
  \draw[->, gray] (0,-0.9) -- (0,3.2);
  \draw[->, very thick] (0,0) -- (2,0.4) node[below right, lab] {$\mathbf{a}_1$};
  \draw[->, very thick] (0,0) -- (0.8,1.8) node[right, lab] {$\mathbf{a}_2$};
  \draw[thick, dashed] (-0.4,-0.9) -- (1.42,3.2);
  \fill (-1,1.5) circle (0.05) node[left, lab] {$\mathbf{b}$};
  \fill (0.39,0.88) circle (0.04) node[right, lab] {$\mathbf{p}$};
  \draw[dotted, thick] (-1,1.5) -- (0.39,0.88);
  \draw[->, thick] (0,0) -- (0.9,-0.4) node[below, lab] {$\mathbf{y}$};
  \node[lab] at (2.1,1.5) {$K$};
  \node[lab, align=center] at (0.8,-1.8)
    {$\mathbf{b}$ lies outside $K = \operatorname{cone}(\mathbf{a}_1, \mathbf{a}_2)$, and $\mathbf{p}$ is the point\\
     of $K$ nearest to it. The vector $\mathbf{y}$ points along $\mathbf{p} - \mathbf{b}$. The dashed\\
     line $\langle \mathbf{z}, \mathbf{y}\rangle = 0$ passes through $\mathbf{0}$, with $K$ on the side\\
     $\langle \mathbf{z}, \mathbf{y} \rangle \ge 0$ and $\mathbf{b}$ strictly on the other};
\end{tikzpicture}
\end{center}

::: {#exm-farkas-certificate}
[Deciding a system both ways]

Let
\[
\A = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \end{pmatrix} ,
\qquad
\b = \begin{pmatrix} 3 \\ 2 \end{pmatrix},
\qquad
\b' = \begin{pmatrix} -1 \\ 1 \end{pmatrix} .
\]
Decide, for \( \b \) and for \( \b' \), which alternative of @thm-farkas holds, and exhibit the solution.
:::

::: {.solution}
The columns are \( \a_1 = \e_1 \), \( \a_2 = (2, 1) \) and \( \a_3 = \e_2 \), all in the closed first quadrant. So \( \operatorname{cone}(\A) \subseteq \nR^2_{\ge 0} \), and in fact the two are equal, since \( \e_1 \) and \( \e_2 \) are among the generators.

For \( \b = (3, 2) \) we expect (F1). The system \( x_1 + 2x_2 = 3 \), \( x_2 + x_3 = 2 \) has, for example, the solution \( \x = (3, 0, 2) \ge \0 \), and also \( \x = (1, 1, 1) \). Non-negative solutions need not be unique.

For \( \b' = (-1, 1) \) we expect (F2), since \( \b' \) has a negative first entry. Try \( \y = \e_1 \): then \( \A\tp\y = (1, 2, 0) \ge \0 \) and \( \b'^{\top}\y = -1 < 0 \). So \( \y = \e_1 \) is a certificate, and by the "not both" half of @thm-farkas the system \( \A\x = \b' \), \( \x \ge \0 \) has no solution. The certificate encodes a one-line argument: the first equation reads \( x_1 + 2x_2 = -1 \), and its left side is \( \ge 0 \) whenever \( \x \ge \0 \).
:::

Linear programming, in the next section, meets systems of **inequalities**, \( \A\x \le \b \) with \( \x \ge \0 \). Farkas's lemma handles them after one standard move: add a **slack** variable to turn each inequality into an equation.

::: {#cor-farkas-inequality}
[Farkas's Lemma for Inequalities]

Let \( \M \in M_{m \times n}(\nR) \) and \( \d \in \nR^m \). Exactly one of the following has a solution:

::: {.enumerate options="label=(\roman*)"}
1. \( \M\z \le \d \) with \( \z \in \nR^n \), \( \z \ge \0 \);
2. \( \w \ge \0 \), \( \M\tp\w \ge \0 \) and \( \d\tp\w < 0 \), with \( \w \in \nR^m \).
:::
:::

::: {.idea}
A slack vector \( \s = \d - \M\z \ge \0 \) turns the inequalities into equations with matrix \( \begin{pmatrix} \M & \I_m \end{pmatrix} \), and in @thm-farkas the identity block becomes the extra condition \( \w \ge \0 \).
:::

::: {.proof}
Here \( \M\z \le \d \) means \( \d - \M\z \ge \0 \). So (i) has a solution if and only if there are \( \z \ge \0 \) and \( \s \ge \0 \) in \( \nR^m \) with \( \M\z + \s = \d \): given \( \z \), take \( \s = \d - \M\z \), and given \( \z \) and \( \s \), drop \( \s \). In block form this reads
\[
\begin{pmatrix} \M & \I_m \end{pmatrix}\begin{pmatrix} \z \\ \s \end{pmatrix} = \d ,
\qquad
\begin{pmatrix} \z \\ \s \end{pmatrix} \ge \0 .
\]
Apply @thm-farkas to the \( m \times (n+m) \) matrix \( \begin{pmatrix} \M & \I_m \end{pmatrix} \) and to \( \d \). Exactly one of the system above and the following is solvable: \( \begin{pmatrix} \M & \I_m\end{pmatrix}\tp\w \ge \0 \) and \( \d\tp\w < 0 \). The transpose has the blocks \( \M\tp \) and \( \I_m \) stacked, so the first condition says \( \M\tp\w \ge \0 \) and \( \w \ge \0 \). That is (ii).
:::

## The dual of the dual

Farkas's lemma has a coordinate-free form, which says that nothing is lost by passing to the dual cone twice, provided the cone is closed.

::: {#thm-dual-cone-of-dual-cone}
[The Bidual of a Closed Cone]

Let \( V \) be a finite-dimensional real inner product space and let \( K \subseteq V \) be a **closed** convex cone. Then \( K^{**} = K \).
:::

::: {.proof}
\( K \subseteq K^{**} \) is @prp-dual-cone-basic (c). Conversely, let \( \b \notin K \). By @lem-cone-separation there is \( \y \in K^{*} \) with \( \inner{\b}{\y} < 0 \). That single \( \y \) shows \( \b \notin K^{**} \). Hence \( K^{**} \subseteq K \), and the two are equal.
:::

For \( K = \operatorname{cone}(\A) \), which is closed by @thm-finitely-generated-cone-closed, the theorem **is** Farkas's lemma. By @prp-dual-cone-basic (d), \( K^{*} = \{ \y : \A\tp\y \ge \0 \} \), so "\( \b \in K^{**} \)" says that every \( \y \) with \( \A\tp\y \ge \0 \) has \( \b\tp\y \ge 0 \), that is, (F2) has no solution. And "\( \b \in K \)" is (F1). This is the "dualize" move in its purest form: a question about a cone (is \( \b \) in it?) is traded for one about its dual (does every member of the dual approve of \( \b \)?), and the trade is exact when the cone is closed.

::: {.remark}
For the wedge \( K = \operatorname{cone}\bigl((1, 0), (1, 1)\bigr) \), whose dual is \( \operatorname{cone}\bigl((0, 1), (1, -1)\bigr) \) by @exr-cones-and-farkas-b3, the theorem and @prp-dual-cone-basic (d) say that \( K = \{ \x : \inner{\x}{(0, 1)} \ge 0,\ \inner{\x}{(1, -1)} \ge 0 \} \), one inequality for each generator of \( K^{*} \). In general the theorem describes a closed convex cone from outside, as an intersection of half-spaces through the origin; for a finitely generated cone finitely many suffice, which is one half of the Minkowski–Weyl theorem of Section 9.
:::

## When the cone is not finitely generated

The system "\( \A\x = \b \), \( \x \ge \0 \)" asks whether \( \b \) lies in the image of the orthant under \( \x \mapsto \A\x \). Replace the orthant by a closed convex cone \( K \subseteq \nR^k \) and \( \A \) by a matrix \( \P \in M_{m \times k}(\nR) \), and ask whether \( \b \in \P(K) \). The "not both" half of the proof of @thm-farkas survives unchanged. The "at least one" half needs \( \P(K) \) to be closed, and the next example shows that this can fail.

::: {#exm-image-of-closed-cone-not-closed}
[A closed cone with a non-closed shadow]

In \( \nR^3 \), with coordinates \( (x, y, z) \), let
\[
K = \{ (x, y, z) : x s^2 + 2y\,st + z t^2 \ge 0 \text{ for all } s, t \in \nR \} ,
\]
the set of triples for which the symmetric matrix \( \begin{psmallmatrix} x & y \\ y & z \end{psmallmatrix} \) is positive semidefinite (@def-positive-semidefinite). Let \( \P = \begin{psmallmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{psmallmatrix} \), so that \( \P(x, y, z) = (x, y) \) is the projection onto the first two coordinates, and write \( \P(K) = \{ \P\k : \k \in K \} \). Show that \( K \) is a closed convex cone, but that
\[
\P(K) = \{ (x, y) : x > 0 \} \cup \{ (0, 0) \} ,
\]
the cone of the earlier warning, which is not closed. Then show that for \( \b = (0, 1) \) **neither** of the two alternatives holds:

::: {.enumerate options="label=(\roman*)"}
1. \( \P\k = \b \) for some \( \k \in K \);
2. \( \inner{\P\k}{\y} \ge 0 \) for every \( \k \in K \), and \( \inner{\b}{\y} < 0 \), for some \( \y \in \nR^2 \).
:::
:::

::: {.solution}
*\( K \) is a closed convex cone.* Write \( q_{\k}(s, t) = xs^2 + 2yst + zt^2 \) for \( \k = (x, y, z) \). It is linear in \( \k \): \( q_{a\k + b\k'} = aq_{\k} + bq_{\k'} \). So if \( \k, \k' \in K \) and \( a, b \ge 0 \), then \( q_{a\k + b\k'}(s, t) \ge 0 \) for all \( s, t \), and \( K \) is a convex cone that contains \( \0 \). If \( \k_j \to \k \) with \( \k_j \in K \), then for fixed \( s, t \) the number \( q_{\k_j}(s, t) \) is a fixed linear combination of the entries of \( \k_j \). So it converges to \( q_{\k}(s, t) \), and \( q_{\k}(s, t) \ge 0 \) because a non-strict inequality survives a limit. Hence \( K \) is closed.

*Membership.* By @thm-psd-characterizations (a) \( \Leftrightarrow \) (e), \( (x, y, z) \in K \) exactly when the principal minors \( x \), \( z \) and \( xz - y^2 \) are all \( \ge 0 \).

*The image.* \( (0, 0) = \P(\0) \in \P(K) \). If \( x > 0 \) and \( y \) is arbitrary, put \( z = y^2/x \). Then \( x \ge 0 \), \( z \ge 0 \) and \( xz - y^2 = 0 \), so \( (x, y, z) \in K \) and \( (x, y) \in \P(K) \). Conversely, if \( (x, y, z) \in K \), then \( x \ge 0 \), and if \( x = 0 \) then \( 0 = xz \ge y^2 \) forces \( y = 0 \). So \( \P(K) \) is exactly the displayed set. It is not closed: \( (1/k, 1) \in \P(K) \) converges to \( (0, 1) \notin \P(K) \).

*Neither alternative holds for \( \b = (0, 1) \).* Alternative (i) fails because \( \b \notin \P(K) \). For (ii), suppose \( \y = (y_1, y_2) \) has \( \inner{\P\k}{\y} \ge 0 \) for every \( \k \in K \). Since \( (1, t) \in \P(K) \) for every real \( t \), we get \( y_1 + ty_2 \ge 0 \) for all \( t \). A non-constant affine function of \( t \) takes negative values, so \( y_2 = 0 \). But then \( \inner{\b}{\y} = y_2 = 0 \), which is not \( < 0 \). So (ii) fails too.
:::

It is worth seeing exactly where the proof of @thm-farkas breaks. The vectors \( \k_j = (1/j, 1, j) \) lie in \( K \), their images \( (1/j, 1) \) converge to \( \b \), and the \( \k_j \) themselves run off to infinity in the third coordinate. This is the escape that the left inverse in @lem-orthant-image-closed prevented. There is no nearest point of \( \P(K) \) to \( \b \): the distance is \( 0 \), but \( \b \) is not in the set, so @lem-cone-separation has nothing to start from. What fails is **closedness**, which is why the finitely generated case needed its own theorem.

The dual cone cannot see the difference either: \( \P(K)^{**} \) is the closed half-plane \( \{ x \ge 0 \} \), strictly larger than \( \P(K) \), as @exr-cones-and-farkas-c3 shows.

## Exercises

### A. Check your understanding

:::: {#exr-cones-and-farkas-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define a convex cone and the dual cone of a subset \( S \) of \( \nR^n \).
2. State Farkas's lemma, and say in one sentence what the vector \( \y \) in the second alternative certifies.
3. Determine whether the following is correct, and justify your answer: every convex cone in \( \nR^2 \) is closed.
4. Determine whether the following is correct, and justify your answer: the union of two convex cones in \( \nR^2 \) is a convex cone.
5. In @thm-conic-caratheodory the bound is \( n \) generators, while @thm-caratheodory allows \( n + 1 \) points. Which feature of the proof accounts for the difference?
:::
::::

::: {.solution}
(a) A convex cone is a non-empty \( K \subseteq \nR^n \) with \( a\u + b\v \in K \) for all \( \u, \v \in K \) and all real \( a, b \ge 0 \). The dual cone of \( S \) is \( S^{*} = \{ \y : \inner{\x}{\y} \ge 0 \text{ for every } \x \in S \} \).

(b) For \( \A \in M_{m \times n}(\nR) \) and \( \b \in \nR^m \), exactly one of the following is solvable: \( \A\x = \b \) with \( \x \ge \0 \), or \( \A\tp\y \ge \0 \) with \( \b\tp\y < 0 \). Such a \( \y \) certifies that the first system has no solution, since any solution \( \x \) would give \( 0 > \b\tp\y = \x\tp\A\tp\y \ge 0 \).

(c) Incorrect. The cone \( \{ (x, y) : x > 0 \} \cup \{\0\} \) of the warning in this section is a convex cone, but \( (1/k, 1) \to (0, 1) \) leaves it.

(d) Incorrect. The two quadrants \( \nR^2_{\ge 0} \) and \( -\nR^2_{\ge 0} \) are convex cones, and their union contains \( (1, 0) \) and \( (0, -1) \) but not their sum \( (1, -1) \).

(e) For cones the dependence to be removed is a **linear** dependence \( \sum c_i\a_i = \0 \), and a linearly independent list in an \( n \)-dimensional space has at most \( n \) members. For convex hulls it is an **affine** dependence (coefficients also summing to \( 0 \)), and an affinely independent list can have \( n + 1 \) members.
:::

### B. Practice

:::: {#exr-cones-and-farkas-b1}
[B1: Recognizing cones]

Determine which of the following subsets of \( \nR^2 \) or \( \nR^3 \) are convex cones. Justify your answers.

::: {.enumerate options="label=(\alph*)"}
1. \( \{ \x \in \nR^2 : x_1 \ge \lvert x_2\rvert \} \).
2. \( \{ \x \in \nR^3 : x_1 + x_2 + x_3 = 0 \} \).
3. \( \{ \x \in \nR^2 : x_1 \ge 1 \} \).
4. \( \{ \x \in \nR^2 : x_2 \ge x_1^2 \} \).
5. \( \{ \x \in \nR^3 : x_1 \ge 0,\ x_2 \ge 0,\ x_3 \le x_1 + x_2 \} \).
:::
::::

::: {.solution}
(a) A convex cone. It is non-empty, containing \( \0 \). If \( x_1 \ge \lvert x_2\rvert \), \( y_1 \ge \lvert y_2\rvert \) and \( a, b \ge 0 \), then by the triangle inequality for real numbers
\[
\lvert ax_2 + by_2\rvert \le a\lvert x_2\rvert + b\lvert y_2\rvert \le ax_1 + by_1 .
\]
It is \( \operatorname{cone}\bigl((1, 1), (1, -1)\bigr) \), a quarter-plane turned by \( 45^\circ \).

(b) A convex cone. It is a subspace, being the null space of \( \begin{pmatrix} 1 & 1 & 1\end{pmatrix} \), and every subspace is a convex cone.

(c) Not a convex cone: it does not contain \( \0 \), which taking \( a = b = 0 \) in the definition would force into it. It is convex and closed under addition; what fails is scaling by \( 0 \le a < 1 \), for instance \( \tfrac12(1, 0) = (\tfrac12, 0) \) is not in it.

(d) Not a convex cone. It is convex, but it is not closed under non-negative scaling: \( (1, 1) \) is in it, and \( 2(1, 1) = (2, 2) \) is not, since \( 2 < 4 \).

(e) A convex cone. Each of the three conditions is a homogeneous linear inequality \( \inner{\x}{\a} \ge 0 \), with \( \a = \e_1 \), \( \e_2 \) and \( (1, 1, -1) \), so the set is an intersection of three half-spaces through the origin. Each is a convex cone by the examples of this section, and an intersection of convex cones is a convex cone: it contains \( \0 \), and each member cone contains every non-negative combination of points of the intersection.
:::

:::: {#exr-cones-and-farkas-b2}
[B2: A certificate either way]

Let \( \A = \begin{pmatrix} 1 & 1 & -1 \\ 0 & 1 & 2 \end{pmatrix} \). For each of \( \b = (0, 3) \) and \( \b = (-1, 1) \), decide which alternative of @thm-farkas holds, and exhibit a solution of that alternative.
::::

::: {.solution}
The columns are \( \a_1 = (1, 0) \), \( \a_2 = (1, 1) \) and \( \a_3 = (-1, 2) \).

For \( \b = (0, 3) \), try \( \x = (0, x_2, x_3) \): the equations \( x_2 - x_3 = 0 \) and \( x_2 + 2x_3 = 3 \) give \( x_2 = x_3 = 1 \). So \( \x = (0, 1, 1) \ge \0 \) solves \( \A\x = \b \), and (F1) holds.

For \( \b = (-1, 1) \), look for \( \y \) perpendicular to the "outermost" generator \( \a_3 \) and non-negative on the others. The vector \( \y = (2, 1) \) gives \( \A\tp\y = (2, 3, 0) \ge \0 \) and \( \b\tp\y = -2 + 1 = -1 < 0 \). So (F2) holds, and by @thm-farkas the system \( \A\x = (-1, 1) \), \( \x \ge \0 \) has no solution. As a direct check, adding twice the first equation to the second gives \( 2x_1 + 3x_2 = -1 \), whose left side is \( \ge 0 \) for \( \x \ge \0 \).
:::

:::: {#exr-cones-and-farkas-b3}
[B3: A dual cone and its dual]

Let \( K = \operatorname{cone}\bigl((1, 0), (1, 1)\bigr) \subseteq \nR^2 \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( K^{*} = \operatorname{cone}\bigl((0, 1), (1, -1)\bigr) \).
2. Compute \( K^{**} \) and check that it equals \( K \), as @thm-dual-cone-of-dual-cone predicts.
:::
::::

::: {.solution}
(a) By @prp-dual-cone-basic (d), \( K^{*} = \{ \y : y_1 \ge 0,\ y_1 + y_2 \ge 0 \} \). Given such a \( \y \), write \( \y = (y_1 + y_2)(0, 1) + y_1(1, -1) \): indeed the right side is \( (y_1, y_1 + y_2 - y_1) = (y_1, y_2) \), and both coefficients are \( \ge 0 \). So \( \y \in \operatorname{cone}\bigl((0,1),(1,-1)\bigr) \). Conversely, both generators satisfy the two inequalities, and the set defined by the inequalities is a convex cone, so it contains the cone they generate.

(b) Applying @prp-dual-cone-basic (d) to the generators found in (a), \( K^{**} = \{ \x : x_2 \ge 0,\ x_1 - x_2 \ge 0 \} \). The same decomposition argument, now with \( \x = (x_1 - x_2)(1, 0) + x_2(1, 1) \), shows this set is \( \operatorname{cone}\bigl((1, 0), (1, 1)\bigr) = K \).
:::

### C. Going deeper

:::: {#exr-cones-and-farkas-c1}
[C1: Gordan's alternative]

Let \( \A \in M_{m \times n}(\nR) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that exactly one of the following has a solution: \( \A\x = \0 \) with \( \x \ge \0 \) and \( \x \ne \0 \); or \( \A\tp\y > \0 \) with \( \y \in \nR^m \).
2. Deduce that if the columns of \( \A \) are \( (1, 0) \), \( (0, 1) \) and \( (-1, -1) \), then some non-trivial non-negative combination of them is \( \0 \), and find one.
:::

*Hint for (a): scale \( \x \) so that its entries sum to \( 1 \), and apply @thm-farkas to \( \A \) with an extra row of ones.*
::::

::: {.solution}
(a) *Not both.* If \( \A\x = \0 \) with \( \x \ge \0 \), \( \x \ne \0 \), and \( \A\tp\y > \0 \), then \( 0 = \y\tp\A\x = \sum_j x_j(\A\tp\y)_j \). Every term is \( \ge 0 \), and the term for an index with \( x_j > 0 \) is \( > 0 \). That is a contradiction.

*At least one.* Suppose the first system has no solution. If \( \A\x = \0 \), \( \x \ge \0 \) and \( \1\tp\x = 1 \), then \( \x \ne \0 \) would solve it. So the system
\[
\begin{pmatrix} \A \\ \1\tp \end{pmatrix}\x = \begin{pmatrix} \0 \\ 1 \end{pmatrix} ,
\qquad \x \ge \0 ,
\]
has no solution. By @thm-farkas there is \( (\y, s) \in \nR^m \times \nR \) with \( \A\tp\y + s\1 \ge \0 \) and \( \0\tp\y + 1\cdot s < 0 \), that is, \( s < 0 \). Then \( \A\tp\y \ge -s\1 > \0 \), so \( \y \) solves the second system.

(b) Here \( \A = \begin{psmallmatrix} 1 & 0 & -1 \\ 0 & 1 & -1\end{psmallmatrix} \). The second system is impossible: \( \A\tp\y = (y_1, y_2, -y_1 - y_2) \), and its entries sum to \( 0 \), so they cannot all be positive. By (a) the first system is solvable. Indeed \( \x = (1, 1, 1) \) gives \( \A\x = (1 - 1, 1 - 1) = \0 \).
:::

:::: {#exr-cones-and-farkas-c2}
[C2: The ice-cream cone is its own dual]

Let \( L = \{ (\x, t) \in \nR^{n} \times \nR : \norm{\x}_2 \le t \} \), with the inner product \( \inner{(\x, t)}{(\y, s)} = \y\tp\x + ts \) on \( \nR^{n+1} \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( L \subseteq L^{*} \).
2. Prove that \( L^{*} \subseteq L \).
3. Deduce that \( L \) is closed.
:::

*Hint for (b): test \( (\y, s) \in L^{*} \) against the member \( (-\y, \norm{\y}_2) \) of \( L \).*
::::

::: {.solution}
(a) Let \( (\x, t), (\y, s) \in L \). By @thm-cauchy-schwarz, \( \lvert\y\tp\x\rvert \le \norm{\x}_2\norm{\y}_2 \le ts \), where the last step multiplies the inequalities \( 0 \le \norm{\x}_2 \le t \) and \( 0 \le \norm{\y}_2 \le s \). Hence \( \y\tp\x + ts \ge ts - \lvert\y\tp\x\rvert \ge 0 \). Fix \( (\y, s) \in L \): we have shown that its inner product with every \( (\x, t) \in L \) is \( \ge 0 \), so \( (\y, s) \in L^{*} \). Hence \( L \subseteq L^{*} \).

(b) Let \( (\y, s) \in L^{*} \). The point \( (-\y, \norm{\y}_2) \) lies in \( L \), so
\[
0 \le \inner{(-\y, \norm{\y}_2)}{(\y, s)} = -\norm{\y}_2^2 + s\norm{\y}_2 = \norm{\y}_2\bigl(s - \norm{\y}_2\bigr) .
\]
If \( \y \ne \0 \), dividing by \( \norm{\y}_2 > 0 \) gives \( s \ge \norm{\y}_2 \). If \( \y = \0 \), test against \( (\0, 1) \in L \) instead: \( s \ge 0 = \norm{\y}_2 \). Either way \( (\y, s) \in L \).

(c) By (a) and (b), \( L = L^{*} \), and every dual cone is closed by @prp-dual-cone-basic (a).
:::

:::: {#exr-cones-and-farkas-c3}
[C3: The bidual sees only the closure]

Let \( C = \{ (x, y) : x > 0 \} \cup \{(0, 0)\} \subseteq \nR^2 \), the image cone of @exm-image-of-closed-cone-not-closed.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( C^{*} = \{ (y_1, 0) : y_1 \ge 0 \} \).
2. Prove that \( C^{**} = \{ (x, y) : x \ge 0 \} \).
3. Explain why this does not contradict @thm-dual-cone-of-dual-cone, and show that \( C^{**} \) is the set of all limits of convergent sequences of points of \( C \).
:::
::::

::: {.solution}
(a) If \( (y_1, y_2) \in C^{*} \), then testing against \( (1, t) \in C \) gives \( y_1 + ty_2 \ge 0 \) for every real \( t \). This forces \( y_2 = 0 \), as in the example, and then \( t = 0 \) gives \( y_1 \ge 0 \). Conversely, if \( y_2 = 0 \) and \( y_1 \ge 0 \), then \( \inner{(x, y)}{(y_1, 0)} = xy_1 \ge 0 \) for every \( (x, y) \in C \), since \( x \ge 0 \) on \( C \).

(b) By (a), \( C^{*} = \operatorname{cone}\bigl((1, 0)\bigr) \), so by @prp-dual-cone-basic (d),
\[
C^{**} = \{ (x, y) : \inner{(x, y)}{(1, 0)} \ge 0 \} = \{ (x, y) : x \ge 0 \} .
\]

(c) @thm-dual-cone-of-dual-cone assumes the cone is closed, and \( C \) is not. Every point of \( C^{**} \) is such a limit: if \( x > 0 \) or \( (x, y) = \0 \), use the constant sequence; if \( x = 0 \), use \( (1/k, y) \in C \), which tends to \( (0, y) \). Conversely, a limit of points of \( C \subseteq C^{**} \) lies in \( C^{**} \), because \( C^{**} \) is closed by @prp-dual-cone-basic (a). So \( C^{**} \) is exactly the set of limits of sequences in \( C \).
:::
