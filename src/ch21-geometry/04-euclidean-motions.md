# Euclidean Motions

Affine geometry knows about lines, parallels and ratios along a line, but not about length. Put the standard inner product back on \( \nR^n \) and a new question appears: which maps of space leave every distance unchanged? One might expect a large and unruly collection, since the condition says nothing about linearity, nothing about continuity, and nothing about where the origin goes. The first theorem of this section says otherwise. A map that preserves distances is forced to be affine, with an orthogonal linear part — and it is forced without assuming that it is onto, which most treatments quietly do. The rest of the section turns that structure theorem into a complete list of the motions of the plane and of space.

Throughout, the field is \( \nR \), the space is \( \nR^n \) with the standard inner product, and the **distance** between \( \x \) and \( \y \) is \( \norm{\x - \y} \). Matrices are bold, points of \( \nR^n \) are bold vectors as usual, and we write \( \R_{\theta} \) and the reflections of @thm-orthogonal-2x2 for the elements of \( \Orth(2) \).

## Distance alone

Chapter 10 studied the **linear** maps preserving distance: the isometries, which in \( \nR^n \) are the orthogonal matrices (@thm-isometry-characterizations). But a translation \( \x \mapsto \x + \b \) with \( \b \ne \0 \) also preserves every distance and is not linear, since it moves the origin. So the linear theory misses exactly what affine geometry was invented to supply, and the right notion drops linearity from the hypotheses altogether.

*A Euclidean motion is a map of space that changes no distance.*

::: {#def-euclidean-motion}
[Euclidean Motion]

A **Euclidean motion** of \( \nR^n \), or simply a **motion**, is a map \( f \colon \nR^n \to \nR^n \) such that
\[
\norm{f(\x) - f(\y)} = \norm{\x - \y} \qquad \text{for all } \x, \y \in \nR^n .
\]
No linearity, continuity or surjectivity is assumed.
:::

In words: the only requirement is that the distance between any two points equals the distance between their images. The quantifier is **for all** pairs, not for pairs at some special distance, and that turns out to be exactly the right amount of information.

**Examples.**

1. **Translations.** \( t_{\b}(\x) = \x + \b \) satisfies \( t_{\b}(\x) - t_{\b}(\y) = \x - \y \), so it is a motion for every \( \b \). It is linear only when \( \b = \0 \).
2. **Orthogonal maps.** For \( \Q \in \Orth(n) \), the map \( \x \mapsto \Q\x \) is a motion: \( \norm{\Q\x - \Q\y} = \norm{\Q(\x - \y)} = \norm{\x - \y} \), the last equality by @thm-isometry-characterizations (a) applied to \( T_{\Q} \), which is an isometry by part (f) of that theorem.
3. **Compositions.** If \( f \) and \( g \) are motions then so is \( g \circ f \), since \( \norm{g(f(\x)) - g(f(\y))} = \norm{f(\x) - f(\y)} = \norm{\x - \y} \). In particular \( \x \mapsto \Q\x + \b \) is a motion for every \( \Q \in \Orth(n) \) and \( \b \in \nR^n \).
4. **The degenerate case \( n = 0 \)** is the one-point space and its only motion is the identity; for \( n = 1 \) the motions are \( x \mapsto \pm x + b \), as the theorem below will confirm.

**A non-example by minimal change.** Take \( f(\x) = 2\x \). It is linear, continuous and bijective, and it multiplies every distance by the same factor \( 2 \). The one clause of @def-euclidean-motion it fails is the only one there is: \( \norm{f(\x) - f(\y)} = 2\norm{\x - \y} \ne \norm{\x - \y} \) as soon as \( \x \ne \y \). A map that rescales all distances equally is a **similarity**, not a motion, and this book does not pursue them.

**Why this definition, and why it is enough.** Nothing in it mentions the vector space structure of \( \nR^n \); it is a statement about \( \nR^n \) as a set with a distance. The content of the next theorem is that the vector space structure is recoverable anyway. That is worth pausing on: distances alone remember which points are midpoints, hence which maps are affine, hence all of the linear algebra.

::: {#thm-motion-is-affine}
[Every Motion Is Affine]

Let \( f \colon \nR^n \to \nR^n \) be a Euclidean motion. Then there are a unique \( \Q \in \Orth(n) \) and a unique \( \b \in \nR^n \) with
\[
f(\x) = \Q\x + \b \qquad \text{for every } \x \in \nR^n .
\]
In particular \( f \) is an affine map (@def-affine-map) whose linear part \( \vec f \) (@thm-affine-map-is-linear-plus-translation) is the isometry \( T_{\Q} \).
:::

::: {.idea}
Three steps. ① Move the origin out of the way: \( g(\x) = f(\x) - f(\0) \) is a motion fixing \( \0 \), so it preserves norms as well as distances. ② A map preserving both norms and distances preserves inner products, because the inner product is built from those two by polarization: \( 2\inner{\x}{\y} = \norm{\x}^2 + \norm{\y}^2 - \norm{\x - \y}^2 \). ③ A map preserving inner products is linear, and the way to see it is the reflex for showing a vector is zero: pair the vector \( g(\x + \y) - g(\x) - g(\y) \) with itself. Expanding the square turns it into a combination of inner products, each of which \( g \) has just been shown to preserve, and the combination is the square of \( (\x + \y) - \x - \y = \0 \).
:::

::: {.proof}
**Step 1: reduce to a motion fixing the origin.** Put \( \b = f(\0) \) and \( g(\x) = f(\x) - \b \). For all \( \x, \y \),
\[
\norm{g(\x) - g(\y)} = \norm{f(\x) - f(\y)} = \norm{\x - \y} ,
\]
so \( g \) is a motion, and \( g(\0) = \0 \). Taking \( \y = \0 \) gives
\[
\norm{g(\x)} = \norm{g(\x) - g(\0)} = \norm{\x - \0} = \norm{\x}
\]
for every \( \x \): \( g \) preserves norms.

**Step 2: \( g \) preserves inner products.** By @thm-norm-properties (c), for real vectors \( \u, \v \),
\[
\begin{aligned}
\norm{\u - \v}^2 &= \norm{\u}^2 - 2\inner{\u}{\v} + \norm{\v}^2 , \\
\text{so}\qquad 2\inner{\u}{\v} &= \norm{\u}^2 + \norm{\v}^2 - \norm{\u - \v}^2 .
\end{aligned}
\]
This is the polarization identity of @lem-polarization-identities in the form that uses the distance: the inner product is determined by norms and distances alone. Applying it to \( g(\x), g(\y) \) and then to \( \x, \y \), and using Step 1 three times,
\[
\begin{aligned}
2\inner{g(\x)}{g(\y)}
&= \norm{g(\x)}^2 + \norm{g(\y)}^2 - \norm{g(\x) - g(\y)}^2 \\
&= \norm{\x}^2 + \norm{\y}^2 - \norm{\x - \y}^2 = 2\inner{\x}{\y} .
\end{aligned}
\]
So \( \inner{g(\x)}{g(\y)} = \inner{\x}{\y} \) for all \( \x, \y \).

**Step 3: \( g \) is linear.** Fix \( \x, \y \in \nR^n \) and expand the squared norm of \( \d = g(\x + \y) - g(\x) - g(\y) \). For any three vectors \( \r, \s, \z \), repeated use of @thm-norm-properties (c) gives
\[
\begin{aligned}
\norm{\r - \s - \z}^2 = \ &\norm{\r}^2 + \norm{\s}^2 + \norm{\z}^2 \\
&- 2\inner{\r}{\s} - 2\inner{\r}{\z} + 2\inner{\s}{\z} .
\end{aligned}
\]
Apply this with \( \r = g(\x+\y) \), \( \s = g(\x) \), \( \z = g(\y) \). Every term on the right is a norm or an inner product of values of \( g \), and Steps 1 and 2 replace each by the corresponding quantity for \( \x + \y \), \( \x \), \( \y \). The result is the same expression with \( \r = \x + \y \), \( \s = \x \), \( \z = \y \), that is, \( \norm{(\x + \y) - \x - \y}^2 = 0 \). Hence \( \norm{\d}^2 = 0 \) and \( \d = \0 \) by @thm-norm-properties (a), so
\[
g(\x + \y) = g(\x) + g(\y) .
\]
For scalars, let \( \lambda \in \nR \) and expand in the same way:
\[
\begin{aligned}
\norm{g(\lambda\x) - \lambda g(\x)}^2
&= \norm{g(\lambda\x)}^2 - 2\lambda\inner{g(\lambda\x)}{g(\x)} + \lambda^2\norm{g(\x)}^2 \\
&= \norm{\lambda\x}^2 - 2\lambda\inner{\lambda\x}{\x} + \lambda^2\norm{\x}^2 \\
&= \lambda^2\norm{\x}^2 - 2\lambda^2\norm{\x}^2 + \lambda^2\norm{\x}^2 = 0 ,
\end{aligned}
\]
so \( g(\lambda\x) = \lambda g(\x) \). Therefore \( g \) is linear.

**Step 4: the matrix.** Let \( \Q \) be the matrix of \( g \) in the standard basis, so \( g(\x) = \Q\x \). By Step 2, \( g \) preserves inner products, so \( \Q \in \Orth(n) \) by @thm-isometry-characterizations (b) and (f), the standard basis being orthonormal. Then \( f(\x) = g(\x) + \b = \Q\x + \b \).

**Uniqueness.** If \( \Q\x + \b = \Q'\x + \b' \) for every \( \x \), then \( \x = \0 \) gives \( \b = \b' \), and then \( (\Q - \Q')\x = \0 \) for every \( \x \) gives \( \Q = \Q' \). This proves the theorem.
:::

::: {.remark}
**Surjectivity was never used.** The definition of a motion asks only that distances be preserved, and the proof never produces a preimage of anything. Most treatments define a motion to be a distance-preserving **bijection**, and then the bijectivity is an unused hypothesis — as the next corollary shows, it comes for free.
:::

::: {#cor-motion-bijective}
[Motions Are Bijections]

Every Euclidean motion \( f \) of \( \nR^n \) is a bijection, and \( f^{-1} \) is again a motion. The linear part of \( f^{-1} \) is \( \Q\tp \), where \( \Q \) is the linear part of \( f \).
:::

::: {.proof}
Write \( f(\x) = \Q\x + \b \) by @thm-motion-is-affine. Since \( \Q \in \Orth(n) \), \( \Q \) is invertible with \( \Q^{-1} = \Q\tp \) (@thm-isometry-characterizations (g1)), so the map \( h(\y) = \Q\tp(\y - \b) = \Q\tp\y - \Q\tp\b \) satisfies \( h(f(\x)) = \x \) and \( f(h(\y)) = \y \). Hence \( f \) is a bijection with inverse \( h \), which is a motion by examples 2 and 3 after @def-euclidean-motion, with linear part \( \Q\tp \).
:::

::: {.warning}
**The Euclidean norm is doing real work.** Step 2 is the only place where the special shape of \( \norm{\cdot} \) is used, and for other norms the phenomenon fails. Here is a distance-preserving map that is not affine, for a norm of Chapter 15 and between spaces of different dimensions. Give \( \nR^2 \) the norm \( \norm{(y_1,y_2)}_{\infty} = \max(\lvert y_1\rvert, \lvert y_2\rvert) \) of Chapter 15 and consider \( \varphi \colon \nR \to \nR^2 \), \( \varphi(t) = (t, \lvert t\rvert) \). For \( s, t \in \nR \), @lem-reverse-triangle-norm applied to the absolute value as a norm on \( \nR \) gives \( \bigl\lvert\lvert s\rvert - \lvert t\rvert\bigr\rvert \le \lvert s - t\rvert \), so
\[
\norm{\varphi(s) - \varphi(t)}_{\infty} = \max\bigl(\lvert s - t\rvert,\ \bigl\lvert\lvert s\rvert - \lvert t\rvert\bigr\rvert\bigr) = \lvert s - t\rvert .
\]
So \( \varphi \) preserves distances exactly, and it is visibly not affine: \( \varphi(-1) = (-1,1) \), \( \varphi(0) = (0,0) \) and \( \varphi(1) = (1,1) \), yet \( \varphi(0) \) is not the midpoint of \( \varphi(-1) \) and \( \varphi(1) \), which is \( (0,1) \). Replacing \( \lvert t\rvert \) by any function \( \nR \to \nR \) that never changes by more than its input does gives another one. What makes @thm-motion-is-affine true is polarization, an identity special to the norms that come from an inner product, and not any property shared by all norms.
:::

The determinant of the linear part now splits the motions into two halves, exactly as it splits \( \Orth(n) \).

::: {#def-direct-and-opposite}
[Direct and Opposite Motions]

Let \( f(\x) = \Q\x + \b \) be a motion of \( \nR^n \). It is **direct**, or orientation-preserving, if \( \det\Q = 1 \), and **opposite**, or orientation-reversing, if \( \det\Q = -1 \). These are the only possibilities: \( \Q\tp\Q = \I_n \), and \( \det\Q\tp = \det\Q \) (@thm-det-transpose), so \( (\det\Q)^2 = \det(\Q\tp\Q) = 1 \) by @thm-det-multiplicative.
:::

::: {.check}
For which \( n \) is the map \( f(\x) = -\x + \b \) a direct motion of \( \nR^n \)? Describe it for \( n = 2 \) and \( n = 3 \).
:::

::: {.solution}
It is a motion with linear part \( -\I_n \), and \( \det(-\I_n) = (-1)^n \), so it is direct exactly when \( n \) is even. For \( n = 2 \) it is direct: \( -\I_2 = \R_{\pi} \), and \( f \) is the half-turn about the point \( \tfrac12\b \), which is its unique fixed point, since \( -\x + \b = \x \) forces \( \x = \tfrac12\b \). For \( n = 3 \) it is opposite: it is the point reflection \( \x \mapsto 2(\tfrac12\b) - \x \) in the point \( \tfrac12\b \), which sends each point to the point diametrically opposite it through that center.
:::

## The group of motions

Write \( \operatorname{E}(n) \) for the set of Euclidean motions of \( \nR^n \) and \( \operatorname{Trans}(n) = \{t_{\b} : \b \in \nR^n\} \) for the translations. One proposition records how these fit together, and every part of it is a line of computation.

::: {#prp-motion-group}
[The Euclidean Group]

::: {.enumerate options="label=(\alph*)"}
1. \( \operatorname{E}(n) \) is a group under composition.
2. The map \( \lambda \colon \operatorname{E}(n) \to \Orth(n) \) sending a motion to its linear part is a surjective group homomorphism.
3. \( \ker\lambda = \operatorname{Trans}(n) \), and \( \b \mapsto t_{\b} \) is a group isomorphism \( (\nR^n, +) \to \operatorname{Trans}(n) \).
4. For every motion \( f \) with linear part \( \Q \) and every \( \b \in \nR^n \),
 \[
 f \circ t_{\b} \circ f^{-1} = t_{\Q\b} .
 \]
 In particular a conjugate of a translation is a translation.
:::
:::

::: {.idea}
Write everything in the form \( \x \mapsto \Q\x + \b \). Composing two such maps multiplies the matrices and moves the translation vectors through, so the matrix is exactly the part that composes without interference — which is what a homomorphism is. Part (d) is one substitution, and it explains where the translations sit: they are the motions that every other motion pushes around among themselves.
:::

::: {.proof}
By @thm-motion-is-affine every motion is \( \x \mapsto \Q\x + \b \) with \( \Q \in \Orth(n) \), and conversely every such map is a motion (examples 2 and 3 after @def-euclidean-motion). Write \( f_{\Q,\b} \) for it. A direct computation gives the composition rule:
\[
f_{\R,\c}\bigl(f_{\Q,\b}(\x)\bigr) = \R(\Q\x + \b) + \c = (\R\Q)\x + (\R\b + \c) ,
\]
so
\[
f_{\R,\c} \circ f_{\Q,\b} = f_{\R\Q,\ \R\b + \c} . \tag{$\ast$}
\]

(a) By @cor-motion-bijective every motion is a bijection of \( \nR^n \), so \( \operatorname{E}(n) \) is a subset of the group of all bijections \( \nR^n \to \nR^n \) under composition, which is a group by the argument of @exm-groups for \( S_n \): composition of functions is associative by @thm-composition-associative, the identity map is a two-sided identity, and a bijection has a two-sided inverse (@thm-bijective-iff-invertible), none of which used finiteness. It contains \( \id = f_{\I,\0} \), it is closed under composition by \( (\ast) \) and because \( \R\Q \in \Orth(n) \) (@prp-orthogonal-group-properties), and it is closed under inverses by @cor-motion-bijective. By @def-subgroup it is a subgroup, hence a group.

(b) With \( \lambda(f_{\Q,\b}) = \Q \), well defined by the uniqueness in @thm-motion-is-affine, \( (\ast) \) reads \( \lambda(g \circ f) = \lambda(g)\lambda(f) \), so \( \lambda \) is a homomorphism (@def-group-homomorphism). It is surjective because \( \lambda(f_{\Q,\0}) = \Q \) for every \( \Q \in \Orth(n) \).

(c) \( \lambda(f_{\Q,\b}) = \I \) if and only if \( \Q = \I \), that is, \( f = t_{\b} \); so \( \ker\lambda = \operatorname{Trans}(n) \). By \( (\ast) \) with \( \R = \Q = \I \), \( t_{\c} \circ t_{\b} = t_{\b + \c} \), so \( \b \mapsto t_{\b} \) is a homomorphism from \( (\nR^n, +) \); it is injective because \( t_{\b} = \id \) forces \( \b = t_{\b}(\0) = \0 \), and its image is \( \operatorname{Trans}(n) \) by definition.

(d) By @cor-motion-bijective, \( f^{-1}(\x) = \Q\tp(\x - \c) \) where \( f = f_{\Q,\c} \). Then
\[
f\bigl(t_{\b}(f^{-1}(\x))\bigr) = \Q\bigl(\Q\tp(\x - \c) + \b\bigr) + \c = (\x - \c) + \Q\b + \c = \x + \Q\b ,
\]
which is \( t_{\Q\b}(\x) \). This proves the proposition.
:::

::: {.remark}
In the vocabulary of group theory, (c) and (d) say that \( \operatorname{Trans}(n) \) is a **normal** subgroup of \( \operatorname{E}(n) \) and that the quotient group \( \operatorname{E}(n)/\operatorname{Trans}(n) \) is isomorphic to \( \Orth(n) \). This book has not built quotient groups — Chapter 3 §09's quotients are quotients of **vector spaces**, and \( \operatorname{E}(n) \) is not one — so the proposition records instead the exact content such a quotient would package: a surjective homomorphism onto \( \Orth(n) \) whose kernel is exactly the translations. Concretely, the motions with a given linear part \( \Q \) are exactly the maps \( t_{\b} \circ f_{\Q,\0} \), one for each \( \b \), which is the statement that the fibers of \( \lambda \) are the translates of its kernel.
:::

::: {.warning}
**\( \operatorname{E}(n) \) is not the direct product of \( \Orth(n) \) and \( \operatorname{Trans}(n) \).** Part (d) shows why: conjugating \( t_{\b} \) by a rotation gives \( t_{\Q\b} \), not \( t_{\b} \), so the two subgroups do **not** commute with one another. Concretely in \( \nR^2 \), with \( \Q = \R_{\pi/2} \) and \( \b = \e_1 \), the composite \( f_{\Q,\0} \circ t_{\e_1} \) sends \( \0 \) to \( \Q\e_1 = \e_2 \), while \( t_{\e_1} \circ f_{\Q,\0} \) sends \( \0 \) to \( \e_1 \). A rotation followed by a translation is not the same motion as the translation followed by the rotation.
:::

## Motions of the plane

Now the classification. Four kinds of map appear, and each is built from a linear one by moving the origin to a chosen point.

::: {#def-motion-types-plane}
[Translation, Rotation, Reflection, Glide Reflection]

Let \( \p \in \nR^2 \).

::: {.enumerate options="label=(\alph*)"}
1. The **translation** by \( \b \) is \( t_{\b}(\x) = \x + \b \).
2. The **rotation about \( \p \) by \( \theta \)** is \( \x \mapsto \R_{\theta}(\x - \p) + \p \).
3. Let \( L = \p + \Span(\u) \) be a line, \( \u \ne \0 \), and let \( \Q_L \in \Orth(2) \) be the linear reflection fixing \( \Span(\u) \) and negating \( \Span(\u)^{\perp} \). The **reflection in \( L \)** is \( s_L(\x) = \Q_L(\x - \p) + \p \).
4. Let \( \v \ne \0 \) be parallel to \( L \), that is, \( \v \in \Span(\u) \). The **glide reflection** with axis \( L \) and vector \( \v \) is \( t_{\v} \circ s_L \).
:::
:::

The reflection \( s_L \) does not depend on which point \( \p \in L \) is used: replacing \( \p \) by \( \p + c\u \) changes \( \Q_L(\x - \p) + \p \) by \( -c\Q_L\u + c\u = \0 \), since \( \Q_L\u = \u \). All four maps are motions, being composites of translations and orthogonal maps. Their linear parts are \( \I \), \( \R_{\theta} \), \( \Q_L \) and \( \Q_L \), so the first two are direct and the last two are opposite.

::: {#thm-plane-motions}
[Classification of the Motions of the Plane]

Let \( f(\x) = \Q\x + \b \) be a motion of \( \nR^2 \). Then **exactly one** of the following holds.

::: {.enumerate options="label=(\alph*)"}
1. \( f = \id \).
2. \( f = t_{\b} \) is a translation with \( \b \ne \0 \); the vector \( \b \) is unique.
3. \( f \) is a rotation about a point \( \p \) by an angle \( \theta \in (0, 2\pi) \); the point \( \p \) and the angle \( \theta \) are unique.
4. \( f \) is a reflection \( s_L \) in a line \( L \); the line \( L \) is unique.
5. \( f \) is a glide reflection with axis \( L \) and vector \( \v \ne \0 \); the pair \( (L, \v) \) is unique.
:::

The five cases are told apart by the determinant of \( \Q \) and the fixed-point set \( \operatorname{Fix}(f) = \{\x : f(\x) = \x\} \):
\[
\begin{array}{c|c|c|c|c|c}
& \text{(a)} & \text{(b)} & \text{(c)} & \text{(d)} & \text{(e)} \\ \hline
\det\Q & 1 & 1 & 1 & -1 & -1 \\
\operatorname{Fix}(f) & \nR^2 & \emptyset & \text{a point} & \text{a line} & \emptyset
\end{array}
\]
:::

::: {.idea}
Split on \( \det\Q \), which @thm-orthogonal-2x2 turns into "\( \Q \) is a rotation \( \R_{\theta} \)" or "\( \Q \) is a linear reflection".

For \( \det\Q = 1 \) with \( \Q \ne \I \), the matrix \( \I - \Q \) is invertible, and solving \( (\I - \Q)\p = \b \) is exactly finding a fixed point; once there is one, moving the origin to it makes \( f \) linear.

For \( \det\Q = -1 \) there may be no fixed point, so instead split \( \b \) into its components along the mirror and across it. The **across** part is absorbed by sliding the mirror halfway; the **along** part is what is left over, and it is the glide.
:::

::: {.proof}
*Case \( \det\Q = 1 \).* By @thm-orthogonal-2x2 (a), \( \Q = \R_{\theta} \) for a unique \( \theta \in [0, 2\pi) \).

If \( \theta = 0 \) then \( \Q = \I \) and \( f = t_{\b} \), which is case (a) when \( \b = \0 \) and case (b) otherwise; the vector is \( \b = f(\0) \), hence unique. Its fixed-point set is \( \nR^2 \) or \( \emptyset \).

If \( \theta \ne 0 \), then
\[
\det(\I - \R_{\theta}) = (1 - \cos\theta)^2 + \sin^2\theta = 2 - 2\cos\theta .
\]
Were this \( 0 \) we would have \( \cos\theta = 1 \), hence \( \sin^2\theta = 1 - \cos^2\theta = 0 \) and \( \R_{\theta} = \I = \R_0 \), so \( \theta = 0 \) by the uniqueness in @thm-orthogonal-2x2 (a), a contradiction. So \( \I - \Q \) is invertible and there is a unique \( \p \) with \( (\I - \Q)\p = \b \), that is, with \( f(\p) = \Q\p + \b = \p \). For every \( \x \),
\[
f(\x) - \p = \Q\x + \b - \p = \Q\x - \Q\p = \Q(\x - \p) ,
\]
so \( f \) is the rotation about \( \p \) by \( \theta \): case (c). Its fixed points satisfy \( (\I - \Q)(\x - \p) = \0 \), hence \( \x = \p \), so \( \operatorname{Fix}(f) = \{\p\} \) and \( \p \) is determined by \( f \); \( \theta \) is determined because \( \Q \) is.

*Case \( \det\Q = -1 \).* By @thm-orthogonal-2x2 (b), \( \Q \) fixes a line \( \Span(\u) \) pointwise and negates \( \Span(\u)^{\perp} = \Span(\w) \), where \( (\u, \w) \) is an orthonormal basis of \( \nR^2 \). By @thm-orthogonal-decomposition write
\[
\b = \b_{\parallel} + \b_{\perp} , \qquad \b_{\parallel} = \inner{\b}{\u}\u , \quad \b_{\perp} = \inner{\b}{\w}\w .
\]
Put \( \c = \tfrac12\b_{\perp} \) and \( L = \c + \Span(\u) \). The reflection in \( L \) is \( s_L(\x) = \Q(\x - \c) + \c = \Q\x + (\I - \Q)\c \), and \( \Q\c = -\c \) because \( \c \in \Span(\w) \), so \( (\I - \Q)\c = 2\c = \b_{\perp} \) and
\[
s_L(\x) = \Q\x + \b_{\perp} , \qquad f(\x) = \Q\x + \b_{\perp} + \b_{\parallel} = \bigl(t_{\b_{\parallel}} \circ s_L\bigr)(\x) .
\]

If \( \b_{\parallel} = \0 \), then \( f = s_L \): case (d). Its fixed set is \( L \), since \( \Q(\x - \c) = \x - \c \) holds exactly when \( \x - \c \in \Span(\u) \); so \( L \) is determined by \( f \).

If \( \b_{\parallel} \ne \0 \), then \( f \) is the glide reflection with axis \( L \) and vector \( \b_{\parallel} \), which is parallel to \( L \): case (e). For its fixed set, compute the square of \( f \):
\[
f(f(\x)) = \Q(\Q\x + \b) + \b = \x + (\Q\b + \b) = \x + 2\b_{\parallel} ,
\]
using \( \Q^2 = \I \) and \( \Q\b = \b_{\parallel} - \b_{\perp} \). So \( f \circ f = t_{2\b_{\parallel}} \ne \id \), and a fixed point of \( f \) would be a fixed point of \( f \circ f \); hence \( \operatorname{Fix}(f) = \emptyset \).

*Uniqueness in case (e).* Suppose also \( f = t_{\v} \circ s_{L'} \) with \( \v \ne \0 \) parallel to \( L' \). Picking \( \p' \in L' \) gives \( f(\x) = \Q_{L'}\x + (\I - \Q_{L'})\p' + \v \), so comparing linear parts (unique by @thm-motion-is-affine) gives \( \Q_{L'} = \Q \), and hence \( L' \) has direction \( \Span(\u) \) and \( \v \in \Span(\u) \). Now \( \I - \Q \) sends \( \u \) to \( \0 \) and \( \w \) to \( 2\w \), so \( (\I - \Q)\p' \in \Span(\w) \), and
\[
\b = (\I - \Q)\p' + \v , \qquad (\I - \Q)\p' \in \Span(\w),\ \ \v \in \Span(\u) .
\]
Comparing with \( \b = \b_{\parallel} + \b_{\perp} \) and using the uniqueness of the decomposition in @thm-orthogonal-decomposition, \( \v = \b_{\parallel} \). Finally \( s_{L'} = t_{-\v} \circ f = s_L \), and a reflection determines its axis as its fixed set, so \( L' = L \).

*Exactly one case holds.* The table follows from what was computed in each case, and it separates the five: within \( \det\Q = 1 \) the fixed sets \( \nR^2 \), \( \emptyset \), a single point are distinct, and within \( \det\Q = -1 \) a line and \( \emptyset \) are distinct. This proves the theorem.
:::

So there are only four shapes of plane motion, and the surprise is the fourth. A student asked to list them usually produces translations, rotations and reflections, and stops; the glide reflection is the one that has no fixed point and no visible center, and it is forced on us by the two-line computation \( f \circ f = t_{2\b_{\parallel}} \).

::: {#exm-classify-plane-motion}
[Naming a plane motion]

Classify the motion \( f(\x) = \Q\x + \b \) of \( \nR^2 \) with
\[
\Q = \tfrac15\begin{pmatrix} -3 & 4 \\ 4 & 3 \end{pmatrix} , \qquad \b = (5, 0) .
\]
:::

::: {.solution}
*The linear part.* The columns \( \tfrac15(-3,4) \) and \( \tfrac15(4,3) \) have norm \( \tfrac15\sqrt{9 + 16} = 1 \) and inner product \( \tfrac1{25}(-12 + 12) = 0 \), so \( \Q \in \Orth(2) \) by @thm-isometry-characterizations (f), and \( \det\Q = \tfrac1{25}(-9 - 16) = -1 \). So \( f \) is opposite, and we are in case (d) or (e) of @thm-plane-motions.

*The mirror direction.* Solve \( \Q\x = \x \): the first row gives \( -3x_1 + 4x_2 = 5x_1 \), that is \( x_2 = 2x_1 \), and the second row gives \( 4x_1 + 3x_2 = 5x_2 \), the same condition. So \( \Q \) fixes \( \Span(\u') \) with \( \u' = (1,2) \), and negates \( \Span(\w') \) with \( \w' = (2,-1) \): indeed \( \Q(2,-1) = \tfrac15(-6 - 4,\ 8 - 3) = (-2, 1) \).

*Splitting \( \b \).* Since \( \norm{\u'}^2 = 5 \),
\[
\b_{\parallel} = \frac{\inner{\b}{\u'}}{5}\u' = \frac{5}{5}(1,2) = (1,2) , \qquad
\b_{\perp} = \b - \b_{\parallel} = (4, -2) = 2\,\w' .
\]
As \( \b_{\parallel} \ne \0 \), \( f \) is a **glide reflection**. Its axis is \( L = \c + \Span((1,2)) \) with \( \c = \tfrac12\b_{\perp} = (2,-1) \), and its vector is \( (1, 2) \).

*Checks.* The point \( (2,-1) \) should go to \( (2,-1) + (1,2) = (3,1) \), and indeed \( f(2,-1) = \tfrac15(-6 - 4,\ 8 - 3) + (5,0) = (-2,1) + (5,0) = (3,1) \), which lies on \( L \). And \( f \circ f \) should be the translation by \( 2\b_{\parallel} = (2,4) \): \( f(f(\x)) = \x + \Q\b + \b \), with \( \Q\b = \tfrac15(-15, 20) = (-3, 4) \), so \( \Q\b + \b = (2, 4) \).
:::

The next example is the one that explains where reflections sit in the group: they generate everything, and two of them make a direct motion.

::: {#exm-two-reflections}
[Two mirrors]

::: {.enumerate options="label=(\alph*)"}
1. Reflect in the line \( L_1 = \Span((1,0)) \) and then in \( L_2 = \Span((1,1)) \). Identify the composite.
2. Reflect in \( M_1 = \{x_2 = 0\} \) and then in \( M_2 = \{x_2 = 1\} \). Identify the composite.
3. Prove the general statements: two reflections in lines through a common point \( \p \) meeting at angle \( \alpha \) compose to the rotation about \( \p \) by \( 2\alpha \); two reflections in parallel lines compose to a translation by twice the perpendicular vector between them.
:::
:::

::: {.solution}
(a) The reflection in the first coordinate axis is \( \Q_1 = \diag(1, -1) \), and the reflection in the line \( x_2 = x_1 \) swaps the coordinates, \( \Q_2 = \begin{psmallmatrix} 0 & 1 \\ 1 & 0\end{psmallmatrix} \) (each fixes its line pointwise and negates the orthogonal complement, which is the description in @thm-orthogonal-2x2 (b)). Then
\[
\Q_2\Q_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \R_{\pi/2} .
\]
The two lines meet at angle \( \pi/4 \), and the composite is the rotation by \( 2\cdot\pi/4 = \pi/2 \) about their common point \( \0 \).

(b) \( s_{M_1}(x_1, x_2) = (x_1, -x_2) \), and \( s_{M_2}(x_1,x_2) = (x_1, 2 - x_2) \), since reflecting in the line \( x_2 = 1 \) fixes the first coordinate and sends \( x_2 \) to \( 2 - x_2 \). Composing, \( s_{M_2}(s_{M_1}(\x)) = (x_1, 2 + x_2) \), the translation by \( (0,2) \) — twice the perpendicular vector \( (0,1) \) from \( M_1 \) to \( M_2 \).

(c) Let \( L_i = \p + \Span(\u_i) \) with \( \u_i \) unit vectors, meeting at \( \p \). Moving the origin to \( \p \) (that is, conjugating by \( t_{-\p} \)) we may assume \( \p = \0 \), because \( s_{L_i} = t_{\p} \circ \Q_{L_i} \circ t_{-\p} \) and the two translations cancel in the middle of the composite. By @thm-orthogonal-2x2 (b) the linear reflection in the line through \( \0 \) at angle \( \varphi \) is \( \M_{2\varphi} \), the matrix with rows \( (\cos 2\varphi, \sin 2\varphi) \) and \( (\sin 2\varphi, -\cos 2\varphi) \). Writing \( \D = \diag(1,-1) \), one checks \( \M_{\psi} = \R_{\psi}\D \) and \( \D\R_{\psi}\D = \R_{-\psi} \), the second because \( \D \) changes the sign of \( \sin\psi \) in both off-diagonal entries. Hence, for lines at angles \( \varphi_1 \) and \( \varphi_2 \) with \( \alpha = \varphi_2 - \varphi_1 \),
\[
\M_{2\varphi_2}\M_{2\varphi_1} = \R_{2\varphi_2}\D\R_{2\varphi_1}\D = \R_{2\varphi_2}\R_{-2\varphi_1} = \R_{2\alpha} ,
\]
a rotation about \( \0 \) by \( 2\alpha \); conjugating back gives the rotation about \( \p \).

For parallel lines \( L_i = \c_i + \Span(\u) \) the linear part is the same reflection \( \Q \) for both, and \( s_{L_i}(\x) = \Q\x + (\I - \Q)\c_i \). Therefore
\[
\begin{aligned}
s_{L_2}\bigl(s_{L_1}(\x)\bigr)
&= \Q\bigl(\Q\x + (\I - \Q)\c_1\bigr) + (\I - \Q)\c_2 \\
&= \x + (\Q - \I)\c_1 + (\I - \Q)\c_2 = \x + (\I - \Q)(\c_2 - \c_1) ,
\end{aligned}
\]
using \( \Q^2 = \I \). Since \( \I - \Q \) kills \( \Span(\u) \) and doubles \( \Span(\u)^{\perp} \), the vector \( (\I - \Q)(\c_2 - \c_1) \) is twice the component of \( \c_2 - \c_1 \) perpendicular to the lines. In (b), \( \c_2 - \c_1 = (0,1) \) and the translation was by \( (0,2) \).
:::

\begin{center}
\begin{tikzpicture}[scale=1.15, lab/.style={font=\small}]
  \draw[->, gray] (-2.6,0) -- (2.7,0);
  \draw[->, gray] (0,-1.6) -- (0,2.7);
  \draw[very thick] (-2.4,0) -- (2.4,0);
  \node[lab, below] at (2.3,-0.08) {$L_1$};
  \draw[very thick] (-1.7,-1.7) -- (1.7,1.7);
  \node[lab, above right] at (1.6,1.6) {$L_2$};
  \fill (1.8,0.6) circle (0.055); \node[lab, right] at (1.88,0.6) {$\mathbf{x}$};
  \fill (1.8,-0.6) circle (0.055); \node[lab, right] at (1.88,-0.62) {$s_{L_1}(\mathbf{x})$};
  \fill (-0.6,1.8) circle (0.055); \node[lab, right] at (-0.5,2.05) {$s_{L_2}(s_{L_1}(\mathbf{x}))$};
  \draw[dashed, gray] (1.8,0.6) -- (1.8,-0.6);
  \draw[dashed, gray] (1.8,-0.6) -- (-0.6,1.8);
  \draw[->, thick] (1.62,0.54) arc (18.4:108.4:1.71);
  \node[lab] at (0.70,1.05) {$2\alpha$};
  \node[lab] at (1.05,0.26) {$\alpha$};
  \node[lab, align=center] at (0,-2.5)
    {Two mirrors meeting at angle $\alpha$ compose to the rotation\\
     through $2\alpha$ about their common point};
\end{tikzpicture}
\end{center}

## Motions of space

In \( \nR^3 \) the same method works, with @cor-so3-is-rotation supplying the normal form of the linear part. Two new names are needed.

::: {#def-space-motion-types}
[Screw Motion, Rotatory Reflection]

Let \( L = \p + \Span(\u) \) be a line in \( \nR^3 \) with \( \norm{\u} = 1 \), and let \( \Pi = \p + W \) be a plane.

::: {.enumerate options="label=(\alph*)"}
1. A **rotation about the axis \( L \)** is a motion \( \x \mapsto \Q(\x - \p) + \p \) with \( \Q \in \SO(3) \), \( \Q \ne \I \) and \( \Q\u = \u \). It fixes \( L \) pointwise, and by @cor-so3-is-rotation it turns the plane \( \Span(\u)^{\perp} \) by a single angle \( \theta \in (0, \pi] \), the **angle** of the rotation. The requirement \( \Q \ne \I \) keeps the identity out: it is a translation, and a translation should not also count as a rotation about every line at once.
2. A **screw motion** is \( t_{\v} \circ r \), where \( r \) is a rotation about \( L \) — so its angle is again non-zero — and \( \v \ne \0 \) is parallel to \( L \).
3. The **reflection in the plane \( \Pi \)** is \( \x \mapsto \Q_{\Pi}(\x - \p) + \p \), with \( \Q_{\Pi} \) the linear map fixing \( W \) pointwise and negating \( W^{\perp} \); a **glide reflection** is \( t_{\v} \circ s_{\Pi} \) with \( \v \ne \0 \) lying in \( W \).
4. A **rotatory reflection about the point \( \p \)** is the composite of a rotation about an axis \( L = \p + \Span(\u) \) by an angle \( \theta \in (0, \pi] \) with the reflection in the plane \( \p + \Span(\u)^{\perp} \) perpendicular to that axis. The two commute, and the composite is \( \x \mapsto \Q(\x - \p) + \p \) where \( \Q \) is \( [-1] \oplus \R_{\theta} \) in an orthonormal basis beginning with \( \u \); in particular \( \det\Q = -1 \). The case \( \theta = \pi \) gives \( \Q = -\I_3 \) and the **point reflection** \( \x \mapsto 2\p - \x \).
:::
:::

::: {#thm-space-motions}
[Classification of the Motions of Space]

Let \( f(\x) = \Q\x + \b \) be a motion of \( \nR^3 \).

::: {.enumerate options="label=(\alph*)"}
1. If \( f \) is direct, then \( f \) is a translation (possibly the identity), a rotation about an axis, or a screw motion, according as \( \Q = \I \), or \( \Q \ne \I \) and \( \b \) is orthogonal to the line fixed by \( \Q \), or \( \Q \ne \I \) and it is not.
2. If \( f \) is opposite, then \( f \) is a reflection in a plane, a glide reflection, or a rotatory reflection about a point.
:::
In both parts the three cases are mutually exclusive, and are told apart by \( \operatorname{Fix}(f) \) together with whether \( \Q = \I \):
\[
\begin{array}{c|c|c|c}
\det\Q = 1 & \text{translation} & \text{rotation} & \text{screw} \\ \hline
\operatorname{Fix}(f) & \nR^3 \text{ or } \emptyset & \text{a line} & \emptyset \\
\Q & \I & \ne \I & \ne \I
\end{array}
\]
\[
\begin{array}{c|c|c|c}
\det\Q = -1 & \text{reflection} & \text{glide} & \text{rotatory} \\ \hline
\operatorname{Fix}(f) & \text{a plane} & \emptyset & \text{a point}
\end{array}
\]
:::

::: {.idea}
@cor-so3-is-rotation gives an orthonormal basis \( (\u, \w_1, \w_2) \) in which \( \Q \) is \( [1] \oplus \R_{\theta} \) or \( [-1] \oplus \R_{\theta} \) with \( \theta \in [0, \pi] \). In every case, split \( \b \) into its component along \( \u \) and its component in \( W = \Span(\u)^{\perp} \), and ask whether \( \I - \Q \) can absorb each piece.

For a direct motion with \( \theta \ne 0 \), \( \I - \Q \) kills \( \u \) but is invertible on \( W \); so the \( W \)-part of \( \b \) is absorbed by moving the axis, and the \( \u \)-part survives as the glide along the axis. That is Chasles's screw.

For an opposite motion the roles swap. When \( \theta = 0 \), \( \Q \) is a plane reflection: \( \I - \Q \) is invertible on \( \Span(\u) \) and kills \( W \), so the \( \u \)-part of \( \b \) is absorbed by sliding the mirror plane and the \( W \)-part survives as the glide. When \( \theta \ne 0 \), \( \I - \Q \) is invertible outright, so **all** of \( \b \) is absorbed and \( f \) has a fixed point.
:::

::: {.proof}
By @cor-so3-is-rotation there are an orthonormal basis \( (\u, \w_1, \w_2) \) of \( \nR^3 \) and \( \theta \in [0, \pi] \) such that, in that basis, \( \Q \) is \( [1] \oplus \R_{\theta} \) when \( \det\Q = 1 \) and \( [-1] \oplus \R_{\theta} \) when \( \det\Q = -1 \). Put \( W = \Span(\u)^{\perp} = \Span(\w_1, \w_2) \), a \( \Q \)-invariant subspace on which \( \Q \) acts as \( \R_{\theta} \) in the basis \( (\w_1, \w_2) \), and write, by @thm-orthogonal-decomposition,
\[
\b = \b_{\parallel} + \b_{\perp} , \qquad \b_{\parallel} = \inner{\b}{\u}\u , \quad \b_{\perp} \in W .
\]
As in the proof of @thm-plane-motions, \( \det(\I_2 - \R_{\theta}) = 2 - 2\cos\theta \), which is non-zero exactly when \( \R_{\theta} \ne \I_2 \), that is, when \( \theta \ne 0 \).

**(a) Direct motions.** Here \( \Q\u = \u \).

*If \( \theta = 0 \)*, then \( \Q = \I \) and \( f = t_{\b} \), the identity when \( \b = \0 \). Its fixed set is \( \nR^3 \) or \( \emptyset \).

*If \( \theta \ne 0 \)*, then \( \Q \ne \I \) and the restriction of \( \I - \Q \) to \( W \) has matrix \( \I_2 - \R_{\theta} \), which is invertible. Since \( \b_{\perp} \in W \), there is a unique \( \c \in W \) with \( (\I - \Q)\c = \b_{\perp} \). Put \( L = \c + \Span(\u) \) and \( r(\x) = \Q(\x - \c) + \c = \Q\x + (\I - \Q)\c = \Q\x + \b_{\perp} \). Then \( r \) fixes \( L \) pointwise, because \( r(\c + s\u) = \Q(s\u) + \c = s\u + \c \), so \( r \) is the rotation about the axis \( L \). And
\[
f(\x) = \Q\x + \b_{\perp} + \b_{\parallel} = \bigl(t_{\b_{\parallel}} \circ r\bigr)(\x) ,
\]
with \( \b_{\parallel} \) parallel to \( L \). So \( f = r \) is a rotation about \( L \) when \( \b_{\parallel} = \0 \), and a screw motion otherwise.

For the fixed sets, note that \( (\I - \Q)\x \in W \) for every \( \x \), because \( (\I - \Q)\u = \0 \) and \( \I - \Q \) maps \( W \) into \( W \). Hence the \( \u \)-component of \( f(\x) - \x = \b - (\I - \Q)\x \) is \( \b_{\parallel} \). If \( \b_{\parallel} \ne \0 \) there is no fixed point; if \( \b_{\parallel} = \0 \) the fixed points are the \( \x \) with \( (\I - \Q)\x = \b_{\perp} \), whose \( W \)-component is the unique \( \c \) above and whose \( \u \)-component is free, that is, the line \( L \).

**(b) Opposite motions.** Here \( \Q\u = -\u \).

*If \( \theta = 0 \)*, then \( \Q \) fixes \( W \) pointwise and negates \( \Span(\u) \): it is the linear reflection in the plane \( W \). Put \( \c = \tfrac12\b_{\parallel} \in \Span(\u) \) and \( \Pi = \c + W \). Since \( \Q\c = -\c \) we get \( (\I - \Q)\c = 2\c = \b_{\parallel} \), so the reflection in \( \Pi \) is
\[
s_{\Pi}(\x) = \Q(\x - \c) + \c = \Q\x + \b_{\parallel} ,
\qquad
f(\x) = \bigl(t_{\b_{\perp}} \circ s_{\Pi}\bigr)(\x) ,
\]
with \( \b_{\perp} \in W \) parallel to \( \Pi \). So \( f \) is the reflection in \( \Pi \) when \( \b_{\perp} = \0 \), and a glide reflection otherwise. For the fixed sets: \( (\I - \Q)\x \in \Span(\u) \) for every \( \x \), since \( \I - \Q \) kills \( W \), so the \( W \)-component of \( f(\x) - \x \) is \( \b_{\perp} \). If \( \b_{\perp} \ne \0 \) there is no fixed point; if \( \b_{\perp} = \0 \) the fixed points are the \( \x \) with \( (\I - \Q)\x = \b_{\parallel} \), that is, with \( \u \)-component \( \c \), which is the plane \( \Pi \).

*If \( \theta \ne 0 \)*, then in the basis \( (\u, \w_1, \w_2) \) the matrix \( \I_3 - \Q \) is \( [2] \oplus (\I_2 - \R_{\theta}) \), whose determinant is \( 2(2 - 2\cos\theta) \ne 0 \). So \( \I - \Q \) is invertible and there is a unique \( \p \) with \( (\I - \Q)\p = \b \), that is, \( f(\p) = \p \). Then \( f(\x) - \p = \Q(\x - \p) \) for every \( \x \), as in the plane case, and \( f \) is a rotatory reflection about \( \p \): in the basis \( (\u, \w_1, \w_2) \) its linear part is \( [-1] \oplus \R_{\theta} \), the rotation by \( \theta \) about \( \Span(\u) \) followed by the reflection in \( W \), and these two commute. The fixed set is \( \{\p\} \), since \( \I - \Q \) is injective. When \( \theta = \pi \), \( \R_{\pi} = -\I_2 \) and \( \Q = -\I_3 \), giving the point reflection \( \x \mapsto 2\p - \x \).

Finally, exactly one case holds in each part. Among the direct motions a translation has \( \Q = \I \) while a rotation and a screw do not, and those two differ by having a line of fixed points or none; among the opposite motions the three fixed sets, a plane, the empty set and a single point, are pairwise different. This proves the theorem.
:::

::: {.remark}
Part (a) is **Chasles's theorem**: every direct motion of space is a screw, provided the two degenerate cases barred by @def-space-motion-types are allowed back in — angle \( \theta = 0 \), which is a pure translation, and \( \v = \0 \), which is a pure rotation. The corresponding statement in the plane, @thm-plane-motions, has no screw because a rotation of \( \nR^2 \) leaves no axis to glide along.
:::

::: {.warning}
**From \( \nR^4 \) on, the list breaks down.** The proof rested entirely on @cor-so3-is-rotation, which in turn rested on the arithmetic \( p + q + 2m = 3 \) of @thm-orthogonal-canonical-form. In \( \nR^4 \) the matrix \( \R_{\pi/2} \oplus \R_{\pi/3} \) has determinant \( 1 \) and fixes no non-zero vector, so a direct motion of \( \nR^4 \) need not have an axis and need not be a screw. The right general statement replaces "one axis and one angle" by the full canonical form: a **direct** motion of \( \nR^n \) decomposes the space into a flat, along which it translates, and a list of mutually orthogonal planes, each turned by its own angle. The word **direct** is needed there: that description hides the \( -\I_q \) block of @thm-orthogonal-canonical-form, which splits into rotations by \( \pi \) only when \( q \) is even, and an opposite motion keeps one leftover direction and negates it. The glide reflection of @thm-space-motions (b) is the smallest witness, with \( p = 2 \), \( q = 1 \), \( m = 0 \): it has no rotation plane, yet it is not a pure translation. This book proves the classification only for \( n \le 3 \).
:::

::: {#exm-classify-space-motion}
[Naming a space motion]

Classify the motion \( f(\x) = \Q\x + \b \) of \( \nR^3 \) with
\[
\Q = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} ,
\qquad \b = (4, 1, -2) .
\]
:::

::: {.solution}
*The linear part.* The columns of \( \Q \) are \( \e_2, \e_3, \e_1 \), an orthonormal list, so \( \Q \in \Orth(3) \) by @thm-isometry-characterizations (f). Expanding along the first row, \( \det\Q = 0 - 0 + 1\cdot(1\cdot 1 - 0\cdot 0) = 1 \), so \( f \) is direct. By @thm-rodrigues (c), \( \Q = \R_{\n,\theta} \) for some unit \( \n \) and \( \theta \in [0,\pi] \). Its trace is \( 0 \), so by @thm-rotation-angle-trace (a) the angle is given by \( \cos\theta = \tfrac12(0 - 1) = -\tfrac12 \), that is \( \theta = 2\pi/3 \), and in particular \( \Q \ne \I \). The axis direction is fixed by \( \Q \): reading \( \Q\x = (x_3, x_1, x_2) \), the equation \( \Q\x = \x \) says \( x_1 = x_2 = x_3 \), so the axis direction is \( \u' = (1,1,1) \).

*Splitting \( \b \).* With \( \norm{\u'}^2 = 3 \) and \( \inner{\b}{\u'} = 4 + 1 - 2 = 3 \),
\[
\b_{\parallel} = \tfrac33(1,1,1) = (1,1,1) , \qquad \b_{\perp} = \b - \b_{\parallel} = (3, 0, -3) .
\]
Since \( \b_{\parallel} \ne \0 \), @thm-space-motions (a) says \( f \) is a **screw motion** with glide vector \( (1,1,1) \).

*The axis.* We need \( \c \) perpendicular to \( \u' \) with \( (\I - \Q)\c = \b_{\perp} \). Writing \( (\I - \Q)\c = (c_1 - c_3,\ c_2 - c_1,\ c_3 - c_2) \), the equations are \( c_1 - c_3 = 3 \), \( c_2 - c_1 = 0 \), \( c_3 - c_2 = -3 \), together with \( c_1 + c_2 + c_3 = 0 \). From the second, \( c_2 = c_1 \); from the first, \( c_3 = c_1 - 3 \); the sum gives \( 3c_1 - 3 = 0 \), so \( \c = (1, 1, -2) \). The axis is \( L = (1,1,-2) + \Span((1,1,1)) \).

*Checks.* The rotation part \( r(\x) = \Q\x + (3,0,-3) \) should fix \( \c \): \( \Q(1,1,-2) = (-2, 1, 1) \), and \( (-2,1,1) + (3,0,-3) = (1,1,-2) \). And \( f \) applied three times should be the translation by \( 3\b_{\parallel} = (3,3,3) \), since \( \Q^3 = \I \):
\[
f^3(\x) = \Q^3\x + \Q^2\b + \Q\b + \b = \x + (\I + \Q + \Q^2)\b .
\]
Here \( \I + \Q + \Q^2 \) is the all-ones matrix \( \J \), so \( (\I + \Q + \Q^2)\b = (4 + 1 - 2)\1 = (3,3,3) \), as predicted.
:::

## Exercises

### A. Check your understanding

:::: {#exr-euclidean-motions-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State @def-euclidean-motion, and say which of linearity, continuity and surjectivity it assumes.
2. True or false: every motion of \( \nR^n \) with a fixed point is linear. Justify your answer.
3. Name the four kinds of motion of \( \nR^2 \) and give the fixed-point set of each.
4. True or false: the composite of two opposite motions of \( \nR^3 \) is opposite. Justify your answer.
5. A motion of \( \nR^3 \) has exactly one fixed point. What kind is it?
:::
::::

::: {.solution}
(a) A motion is a map \( f \colon \nR^n \to \nR^n \) with \( \norm{f(\x) - f(\y)} = \norm{\x - \y} \) for all \( \x, \y \). It assumes none of the three: @thm-motion-is-affine shows that a motion is automatically affine, and @cor-motion-bijective that it is automatically a bijection.

(b) False as stated, but only just: by @thm-motion-is-affine, \( f(\x) = \Q\x + \b \), and \( f(\p) = \p \) gives \( \b = \p - \Q\p \), so \( f(\x) = \Q(\x - \p) + \p \), which is linear precisely when \( \p \) can be taken to be \( \0 \). For example the half-turn of \( \nR^2 \) about \( (1,0) \), \( \x \mapsto -\x + (2,0) \), has a fixed point but sends \( \0 \) to \( (2,0) \ne \0 \), so it is not linear. What is true is that a motion fixing \( \0 \) is linear, which is Steps 1 to 3 of @thm-motion-is-affine.

(c) Translations (fixed set \( \nR^2 \) if the identity, otherwise \( \emptyset \)); rotations about a point (one point); reflections in a line (that line); glide reflections (\( \emptyset \)). This is @thm-plane-motions.

(d) False. By @prp-motion-group (b) the linear part of a composite is the product of the linear parts, and \( \det \) is multiplicative (@thm-det-multiplicative), so the composite has \( \det = (-1)(-1) = 1 \) and is **direct**. What composes is the parity, not the word "opposite": @exm-two-reflections is the two-dimensional instance, where two reflections make a rotation.

(e) A rotatory reflection about that point, by @thm-space-motions: it is the only kind whose fixed set is a single point. In particular it is opposite.
:::

### B. Practice

:::: {#exr-euclidean-motions-b1}
[B1: Classify three plane motions]

Classify each motion \( f(\x) = \Q\x + \b \) of \( \nR^2 \), giving the center and angle, the axis, or the axis and glide vector, as appropriate.

::: {.enumerate options="label=(\alph*)"}
1. \( \Q = \begin{psmallmatrix} 0 & -1 \\ 1 & 0 \end{psmallmatrix} \), \( \b = (2, 4) \).
2. \( \Q = \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix} \), \( \b = (3, 3) \).
3. \( \Q = \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix} \), \( \b = (1, -1) \).
:::
::::

::: {.solution}
(a) \( \det\Q = 1 \) and \( \Q = \R_{\pi/2} \), so \( f \) is a rotation by \( \pi/2 \). Its center solves \( (\I - \Q)\p = \b \), that is \( p_1 + p_2 = 2 \) and \( -p_1 + p_2 = 4 \); adding gives \( 2p_2 = 6 \), so \( \p = (-1, 3) \). Check: \( f(-1,3) = (-3, -1) + (2,4) = (-1, 3) \). So \( f \) is the rotation about \( (-1,3) \) by \( \pi/2 \).

(b) \( \det\Q = -1 \), and \( \Q \) swaps the coordinates: it is the reflection in \( \Span((1,1)) \), negating \( \Span((1,-1)) \). With \( \u' = (1,1) \), \( \inner{\b}{\u'} = 6 \) and \( \norm{\u'}^2 = 2 \), so \( \b_{\parallel} = 3(1,1) = (3,3) = \b \) and \( \b_{\perp} = \0 \). Since \( \b_{\parallel} \ne \0 \), \( f \) is a glide reflection with axis \( \c + \Span((1,1)) \), where \( \c = \tfrac12\b_{\perp} = \0 \): the axis is the line \( x_2 = x_1 \) and the glide vector is \( (3,3) \). Check: \( f(0,0) = (3,3) \), which is on the axis.

(c) Same \( \Q \). Now \( \inner{\b}{\u'} = 0 \), so \( \b_{\parallel} = \0 \) and \( \b_{\perp} = (1,-1) \). Hence \( f \) is a **reflection**, in the line \( L = \c + \Span((1,1)) \) with \( \c = \tfrac12(1,-1) \). Check: \( f(\tfrac12, -\tfrac12) = (-\tfrac12, \tfrac12) + (1,-1) = (\tfrac12, -\tfrac12) \), a fixed point, and \( f(\tfrac32, \tfrac12) = (\tfrac12, \tfrac32) + (1,-1) = (\tfrac32, \tfrac12) \), another one; the two lie on \( L \).
:::

:::: {#exr-euclidean-motions-b2}
[B2: A space motion]

Classify the motion \( f(\x) = \Q\x + \b \) of \( \nR^3 \) with
\[
\Q = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix} ,
\qquad \b = (0, 2, 0) ,
\]
giving the axis and the glide vector if there is one.
::::

::: {.solution}
The columns are \( \e_1, \e_3, -\e_2 \), orthonormal, so \( \Q \in \Orth(3) \); expanding along the first row, \( \det\Q = 1\cdot(0 + 1) = 1 \), so \( f \) is direct. The fixed vectors of \( \Q \) satisfy \( x_1 \) free, \( -x_3 = x_2 \), \( x_2 = x_3 \), hence \( x_2 = x_3 = 0 \): the axis direction is \( \u = \e_1 \), and \( \Q \) is the quarter turn about it.

Now \( \b_{\parallel} = \inner{\b}{\e_1}\e_1 = \0 \) and \( \b_{\perp} = (0,2,0) \). Since \( \b_{\parallel} = \0 \), @thm-space-motions (a) says \( f \) is a **pure rotation** about an axis, with no glide. The axis is \( \c + \Span(\e_1) \) where \( \c \in \Span(\e_2, \e_3) \) solves \( (\I - \Q)\c = \b_{\perp} \):
\[
(\I - \Q)(0, c_2, c_3) = (0,\ c_2 + c_3,\ -c_2 + c_3) = (0, 2, 0)
\]
gives \( c_2 + c_3 = 2 \) and \( c_3 = c_2 \), so \( \c = (0,1,1) \). The axis is \( \{(t, 1, 1) : t \in \nR\} \). Check: \( f(0,1,1) = (0, -1, 1) + (0,2,0) = (0,1,1) \), and \( f(5,1,1) = (5,-1,1) + (0,2,0) = (5,1,1) \).
:::

:::: {#exr-euclidean-motions-b3}
[B3: A motion is determined by few points]

Let \( f \) and \( g \) be motions of \( \nR^n \) that agree on \( \0, \e_1, \dots, \e_n \). Prove that \( f = g \).

*Hint: consider \( h = g^{-1} \circ f \) and use @thm-motion-is-affine.*
::::

::: {.solution}
By @cor-motion-bijective, \( g^{-1} \) is a motion, so \( h = g^{-1} \circ f \) is a motion (example 3 after @def-euclidean-motion). It fixes \( \0 \) and each \( \e_i \), since \( f \) and \( g \) agree there. By @thm-motion-is-affine, \( h(\x) = \Q\x + \b \) with \( \Q \in \Orth(n) \); from \( h(\0) = \0 \) we get \( \b = \0 \), and then \( \Q\e_i = h(\e_i) = \e_i \) for each \( i \), so \( \Q \) agrees with \( \I \) on a basis and \( \Q = \I \). Hence \( h = \id \), and composing with \( g \) gives \( f = g \).

(The \( n + 1 \) points \( \0, \e_1, \dots, \e_n \) are affinely independent, and the same argument works for any affinely independent list of \( n+1 \) points, which is the affine statement of §02.)
:::

### C. Going deeper

:::: {#exr-euclidean-motions-c1}
[C1: Reflections generate the motions]

::: {.enumerate options="label=(\alph*)"}
1. Prove that every motion of \( \nR^n \) is a composite of at most \( n + 1 \) reflections in affine hyperplanes, where the reflection in the hyperplane \( \p + \Span(\w)^{\perp} \) is \( \x \mapsto \H_{\w}(\x - \p) + \p \) with \( \H_{\w} \) the Householder reflection of @def-householder-reflection.
2. Deduce that a translation of \( \nR^n \) by \( \b \ne \0 \) is a composite of exactly two such reflections, and identify them.
:::

*Hint: for (a), first make the motion fix a point, then quote @thm-cartan-dieudonne-small.*
::::

::: {.solution}
(a) Write \( f(\x) = \Q\x + \b \) by @thm-motion-is-affine. If \( \b = \0 \), then \( \Q \) is a product of at most \( n \) Householder reflections by @thm-cartan-dieudonne-small, and each of those is the reflection in the hyperplane \( \0 + \Span(\w)^{\perp} \) in the above sense, so \( f \) is a composite of at most \( n \le n+1 \) reflections.

If \( \b \ne \0 \), let \( \sigma \) be the reflection in the hyperplane \( \tfrac12\b + \Span(\b)^{\perp} \), that is, \( \sigma(\x) = \H_{\b}(\x - \tfrac12\b) + \tfrac12\b \). Since \( \H_{\b}\b = -\b \) (@prp-householder-properties (d)), this simplifies to \( \sigma(\x) = \H_{\b}\x + \b \), and then, using \( \H_{\b}^2 = \I \) (@prp-householder-properties (b)),
\[
\sigma\bigl(\sigma(\x)\bigr) = \H_{\b}\bigl(\H_{\b}\x + \b\bigr) + \b = \x - \b + \b = \x ,
\]
so \( \sigma^{-1} = \sigma \). Therefore
\[
(\sigma \circ f)(\x) = \H_{\b}(\Q\x + \b) + \b = \H_{\b}\Q\x - \b + \b = \H_{\b}\Q\x ,
\]
a linear orthogonal map, which by @thm-cartan-dieudonne-small is a product of at most \( n \) Householder reflections. Hence \( f = \sigma \circ (\sigma \circ f) \) is a composite of at most \( n + 1 \) reflections.

(b) Let \( f = t_{\b} \) with \( \b \ne \0 \). It is not a single reflection, since a reflection has a fixed point and \( t_{\b} \) has none. Let \( \sigma_0 \) be the reflection in \( \Span(\b)^{\perp} \) and \( \sigma_1 \) the reflection in \( \tfrac12\b + \Span(\b)^{\perp} \). By the computation in (a), \( \sigma_0(\x) = \H_{\b}\x \) and \( \sigma_1(\x) = \H_{\b}\x + \b \), so
\[
(\sigma_1\circ\sigma_0)(\x) = \H_{\b}\bigl(\H_{\b}\x\bigr) + \b = \x + \b = t_{\b}(\x) .
\]
So exactly two reflections suffice, in two parallel hyperplanes perpendicular to \( \b \) and at distance \( \tfrac12\norm{\b} \) apart — the \( n \)-dimensional form of @exm-two-reflections (b).
:::

:::: {#exr-euclidean-motions-c2}
[C2: Matching two congruent frames]

Let \( \p_0, \dots, \p_n \) and \( \q_0, \dots, \q_n \) be points of \( \nR^n \) with \( \norm{\p_i - \p_j} = \norm{\q_i - \q_j} \) for all \( i, j \), and suppose \( \p_1 - \p_0, \dots, \p_n - \p_0 \) is a basis of \( \nR^n \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that there is a motion \( f \) of \( \nR^n \) with \( f(\p_i) = \q_i \) for every \( i \).
2. Prove that \( f \) is unique, and give an example with fewer points where it is not.
:::

*Hint: for (a), translate both lists so that \( \p_0 = \q_0 = \0 \), then compare the inner products of the two lists.*
::::

::: {.solution}
(a) Replacing \( \p_i \) by \( \p_i - \p_0 \) and \( \q_i \) by \( \q_i - \q_0 \) changes no distance, and undoing the two translations at the end changes a motion into a motion; so assume \( \p_0 = \q_0 = \0 \). Put \( \v_i = \p_i \) and \( \w_i = \q_i \) for \( i \ge 1 \). Taking \( j = 0 \) in the hypothesis gives \( \norm{\v_i} = \norm{\w_i} \), and then for \( i, j \ge 1 \), by @thm-norm-properties (c),
\[
\begin{aligned}
2\inner{\v_i}{\v_j} &= \norm{\v_i}^2 + \norm{\v_j}^2 - \norm{\v_i - \v_j}^2 \\
&= \norm{\w_i}^2 + \norm{\w_j}^2 - \norm{\w_i - \w_j}^2 = 2\inner{\w_i}{\w_j} .
\end{aligned}
\]
So the two lists have the same inner products. Since \( (\v_1, \dots, \v_n) \) is a basis, @thm-linear-transform-basis gives a unique linear \( T \) with \( T\v_i = \w_i \), and for \( \x = \sum_i x_i\v_i \),
\[
\norm{T\x}^2 = \sum_{i,j} x_ix_j\inner{\w_i}{\w_j} = \sum_{i,j}x_ix_j\inner{\v_i}{\v_j} = \norm{\x}^2 ,
\]
where both ends use @thm-norm-properties (c) repeatedly to expand a squared norm of a sum. So \( T \) is an isometry, and \( f(\x) = T\x \) is a motion with \( f(\p_i) = \q_i \) for \( i \ge 1 \) and \( f(\0) = \0 \).

(b) If \( f \) and \( g \) are motions with \( f(\p_i) = g(\p_i) = \q_i \) for all \( i \), then \( h = g^{-1}\circ f \) is a motion (@cor-motion-bijective) fixing every \( \p_i \). Write \( h(\x) = \Q\x + \b \) by @thm-motion-is-affine. Subtracting \( h(\p_0) = \p_0 \) from \( h(\p_i) = \p_i \) gives \( \Q(\p_i - \p_0) = \p_i - \p_0 \) for \( i \ge 1 \), so \( \Q \) fixes a basis and \( \Q = \I \); then \( \b = \p_0 - \p_0 = \0 \) and \( h = \id \), so \( f = g \).

With fewer points the spanning hypothesis fails and uniqueness goes with it. In \( \nR^2 \), take the single pair \( \p_0 = \q_0 = (0,0) \) and \( \p_1 = \q_1 = (1,0) \). Both the identity and the reflection in the first coordinate axis are motions carrying \( \p_i \) to \( \q_i \), and they differ at \( (0,1) \). Here \( \p_1 - \p_0 = \e_1 \) spans only a line.
:::

:::: {#exr-euclidean-motions-c3}
[C3: Motions of a finite set]

Let \( S \subseteq \nR^n \) be a finite non-empty set and let \( G = \{f \in \operatorname{E}(n) : f(S) = S\} \) be its symmetry group.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( G \) is a subgroup of \( \operatorname{E}(n) \), and that every \( f \in G \) fixes the **centroid** \( \c = \tfrac{1}{\lvert S\rvert}\sum_{\p \in S}\p \).
2. Deduce that \( G \) is isomorphic to a subgroup of \( \Orth(n) \), and that \( G \) contains no translation other than the identity.
:::
::::

::: {.solution}
(a) The identity lies in \( G \). If \( f, g \in G \) then \( (g\circ f)(S) = g(S) = S \), and \( f(S) = S \) with \( f \) a bijection (@cor-motion-bijective) gives \( f^{-1}(S) = S \); so \( G \) is a subgroup by @def-subgroup, using @prp-motion-group (a).

Let \( f \in G \), with \( f(\x) = \Q\x + \b \). Since \( f \) restricts to a bijection of the finite set \( S \),
\[
\sum_{\p \in S} f(\p) = \sum_{\q \in S}\q = \lvert S\rvert\,\c ,
\]
while on the other hand \( \sum_{\p\in S}f(\p) = \Q\bigl(\sum_{\p\in S}\p\bigr) + \lvert S\rvert\b = \lvert S\rvert(\Q\c + \b) = \lvert S\rvert f(\c) \). Dividing by \( \lvert S\rvert \ne 0 \) gives \( f(\c) = \c \).

(b) Conjugating by the translation \( t_{-\c} \) gives an injective homomorphism \( G \to \operatorname{E}(n) \), \( f \mapsto t_{-\c}\circ f\circ t_{\c} \), whose image consists of motions fixing \( \0 \), hence of linear ones by @thm-motion-is-affine; those are the orthogonal maps. So \( G \) is isomorphic to a subgroup of \( \Orth(n) \), namely \( \{\lambda(f) : f \in G\} \) in the notation of @prp-motion-group. If \( t_{\b} \in G \) then \( t_{\b}(\c) = \c \) by (a), so \( \b = \0 \). Geometrically: a finite figure cannot be carried onto itself by a non-trivial translation, because a translation would move its centroid.
:::
