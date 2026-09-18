# Inner Products and Norms

Nine chapters, and we have not measured anything. We can say that a list is independent, that a subspace has dimension four, that an operator is diagonalizable. We cannot yet say that a vector has length \( 3 \), or that two vectors meet at a right angle. Geometry has appeared only in pictures, never in the theory. This section puts it into the theory, by abstracting the one operation in \( \nR^n \) that already computes lengths and angles: the dot product.

## The field for this chapter

**Throughout Chapter 10 the field \( F \) is \( \nR \) or \( \nC \).** This is not laziness; two features of these fields are used on every page, and no other field has both.

The first is **positivity**. The point of the whole construction is that \( \inner{\v}{\v} \) should be the square of a length, so it must be a number we can compare with \( 0 \). Over \( \nF_p \) there is no ordering compatible with the arithmetic at all: in \( \nF_5 \), adding \( 1 \) to itself five times returns to \( 0 \), so no non-zero element can be called "positive" in any useful sense. Over \( \nQ \) there is an ordering, but lengths would not exist, since \( \sqrt{2} \notin \nQ \). Over \( \nR \) every sum of squares is \( \ge 0 \) and every non-negative number has a square root, and that is exactly what we need.

The second is **conjugation**. Over \( \nC \) the naive sum of squares fails immediately: \( 1^2 + i^2 = 0 \), so "\( z_1^2 + z_2^2 \)" is not a length for \( (1, i) \ne \0 \). The repair is to use \( z\conj{z} = \lvert z \rvert^2 \) instead of \( z^2 \) (@thm-conjugate-properties (c)), and this needs the complex conjugate. We write \( \conj{a} \) for the conjugate of \( a \in F \), with the convention that \( \conj{a} = a \) when \( F = \nR \); every formula below then reads correctly over both fields at once.

## From the dot product to the axioms

In \( \nR^n \) the dot product is
\[
\x \cdot \y = x_1y_1 + \dots + x_ny_n .
\]
It computes lengths, because \( \x \cdot \x = x_1^2 + \dots + x_n^2 \) is the square of the Euclidean length by Pythagoras. It computes angles too. For non-zero \( \x, \y \in \nR^2 \) at an angle \( \theta \), the law of cosines applied to the triangle with sides \( \x \), \( \y \) and \( \x - \y \) says
\[
\lVert \x - \y \rVert^2 = \lVert \x \rVert^2 + \lVert \y \rVert^2 - 2\lVert \x \rVert \lVert \y \rVert \cos\theta ,
\]
while expanding the left side entry by entry gives \( \lVert \x \rVert^2 + \lVert \y \rVert^2 - 2(\x \cdot \y) \). Comparing the two, \( \x \cdot \y = \lVert \x \rVert \lVert \y \rVert \cos\theta \). So one bilinear expression carries both length and angle, and perpendicularity is the single equation \( \x \cdot \y = 0 \).

Which properties of the dot product did that argument use? Only three: it is linear in each slot separately, it is symmetric, and \( \x \cdot \x > 0 \) for \( \x \ne \0 \). Those three we can demand of an abstract space. Over \( \nC \), as we saw, symmetry has to be weakened to conjugate symmetry, and the price is small: a conjugate bar in the second slot.

*An inner product is a way of multiplying two vectors into a scalar so that a vector paired with itself has positive "length squared".*

::: {#def-inner-product}
[Inner Product]

Let \( F \) be \( \nR \) or \( \nC \), and let \( V \) be a vector space **over \( F \)**. An **inner product** on \( V \) is a map
\[
\inner{\cdot}{\cdot} \colon V \times V \to F
\]
such that for all \( \u, \v, \w \in V \) and all \( a, b \in F \):

::: {.enumerate options="label=(IP\arabic*)"}
1. \( \inner{a\u + b\v}{\w} = a\inner{\u}{\w} + b\inner{\v}{\w} \)  (**linear in the first slot**);
2. \( \inner{\v}{\u} = \conj{\inner{\u}{\v}} \)  (**conjugate symmetry**);
3. \( \inner{\v}{\v} > 0 \) for **every non-zero** \( \v \in V \)  (**positive definiteness**).
:::

A vector space equipped with an inner product is an **inner product space**. When \( F = \nR \) it is a **real** inner product space, when \( F = \nC \) a **complex** one.
:::

In words, clause by clause. (IP1) says that if we freeze the second slot, what is left is a linear functional on \( V \): the inner product distributes over sums and lets scalars out of the **first** argument untouched. (IP2) says that swapping the two arguments conjugates the answer; over \( \nR \) it is plain symmetry, \( \inner{\v}{\u} = \inner{\u}{\v} \). (IP3) says that a non-zero vector pairs with itself to give a **strictly** positive number. For the inequality in (IP3) to mean anything, \( \inner{\v}{\v} \) must be a **real** number; it is, and the reason is (IP2), as the next result shows. Note also what (IP3) does **not** say: it says nothing about \( \inner{\u}{\v} \) for \( \u \ne \v \), which may be negative, or not even real.

The first consequences are small, and we will use all of them constantly.

::: {#thm-inner-product-basic-properties}
[First Properties of an Inner Product]

Let \( V \) be an inner product space over \( F \). For all \( \u, \v, \w \in V \) and \( a, b \in F \):

::: {.enumerate options="label=(\alph*)"}
1. \( \inner{\v}{\v} \) is a **real** number, and \( \inner{\v}{\v} \ge 0 \) with equality if and only if \( \v = \0 \);
2. \( \inner{\u}{a\v + b\w} = \conj{a}\inner{\u}{\v} + \conj{b}\inner{\u}{\w} \)  (**conjugate-linear in the second slot**);
3. \( \inner{\0}{\v} = \inner{\v}{\0} = 0 \);
4. if \( \inner{\u}{\w} = \inner{\v}{\w} \) for **every** \( \w \in V \), then \( \u = \v \).
:::
:::

::: {.idea}
Each part is one application of an axiom. For (a), a number equal to its own conjugate is real. For (b), swap slots with (IP2), use (IP1), and swap back. For (d), the only vector orthogonal to everything is the zero vector, and we find that out by pairing the difference **with itself**: that is the move to remember.
:::

::: {.proof}
(a) By (IP2) with \( \u = \v \), \( \inner{\v}{\v} = \conj{\inner{\v}{\v}} \), and a complex number equal to its own conjugate has zero imaginary part, so \( \inner{\v}{\v} \in \nR \). If \( \v \ne \0 \), then \( \inner{\v}{\v} > 0 \) by (IP3). If \( \v = \0 \), then \( \inner{\0}{\0} = \inner{0 \cdot \0}{\0} = 0\inner{\0}{\0} = 0 \) by (IP1). Hence \( \inner{\v}{\v} \ge 0 \) always, with equality exactly when \( \v = \0 \).

(b) Using (IP2), then (IP1), then (IP2) again,
\[
\begin{aligned}
\inner{\u}{a\v + b\w}
&= \conj{\inner{a\v + b\w}{\u}} \\
&= \conj{a\inner{\v}{\u} + b\inner{\w}{\u}} \\
&= \conj{a}\,\conj{\inner{\v}{\u}} + \conj{b}\,\conj{\inner{\w}{\u}} \\
&= \conj{a}\inner{\u}{\v} + \conj{b}\inner{\u}{\w},
\end{aligned}
\]
where the third equality uses @thm-conjugate-properties (a) and (b).

(c) \( \inner{\0}{\v} = \inner{0 \cdot \0}{\v} = 0\inner{\0}{\v} = 0 \) by (IP1), and \( \inner{\v}{\0} = \conj{\inner{\0}{\v}} = 0 \) by (IP2).

(d) Put \( \z = \u - \v \). For every \( \w \), (IP1) gives \( \inner{\z}{\w} = \inner{\u}{\w} - \inner{\v}{\w} = 0 \). Take \( \w = \z \): then \( \inner{\z}{\z} = 0 \), so \( \z = \0 \) by (a), that is, \( \u = \v \).
:::

Part (d) is the first appearance of the move that runs through the whole chapter: **to show a vector is zero, pair it with itself.** There is exactly one vector of length zero, so an identity of the form \( \inner{\z}{\z} = 0 \) is a proof that \( \z = \0 \).

Part (b) is where the conjugate becomes visible in practice. An inner product over \( \nC \) is **not** bilinear: scalars leave the second slot wearing a bar. A map with properties (IP1) and (b) is called **sesquilinear**, from the Latin for "one and a half times linear".

## Examples

**The dot product on \( \nR^n \).** Define \( \inner{\x}{\y} = x_1y_1 + \dots + x_ny_n \). (IP1) holds because each term is linear in \( x_i \); (IP2) is the commutativity of multiplication in \( \nR \), and conjugation is the identity; (IP3) holds because \( \inner{\x}{\x} = x_1^2 + \dots + x_n^2 \) is a sum of squares of real numbers, which is \( 0 \) only when every \( x_i = 0 \). This is the **standard** inner product on \( \nR^n \), and it is the model for everything else.

**The standard inner product on \( \nC^n \).** Define
\[
\inner{\x}{\y} = x_1\conj{y_1} + \dots + x_n\conj{y_n} .
\]
(IP1) is clear. For (IP2), \( \conj{\inner{\x}{\y}} = \sum \conj{x_i}y_i = \inner{\y}{\x} \) by @thm-conjugate-properties (a), (b). For (IP3), \( \inner{\x}{\x} = \sum x_i\conj{x_i} = \sum \lvert x_i \rvert^2 \) by @thm-conjugate-properties (c), a sum of non-negative **real** numbers, zero only when every \( x_i = 0 \). The conjugates are doing exactly one job: making the diagonal values real and non-negative.

**Weighted inner products.** Fix real numbers \( w_1, \dots, w_n > 0 \) and put \( \inner{\x}{\y} = \sum_i w_i x_i\conj{y_i} \) on \( F^n \). The same three checks go through, with \( \inner{\x}{\x} = \sum w_i\lvert x_i \rvert^2 \); the weights must be **strictly** positive, or (IP3) fails for a standard basis vector. In the degenerate case \( n = 1 \) and \( w_1 = 1 \), this is \( \inner{x}{y} = x\conj{y} \) on \( F \) itself, the smallest non-zero inner product space there is. It matters because it is where the axioms are just the arithmetic of \( \lvert \cdot \rvert \).

**Continuous functions.** Let \( V = C[0, 1] \) be the space of continuous functions \( f \colon [0, 1] \to F \), and set
\[
\inner{f}{g} = \int_0^1 f(t)\conj{g(t)}\,\dd t .
\]
(IP1) is linearity of the integral, and (IP2) follows because conjugation commutes with integration. For (IP3), \( \inner{f}{f} = \int_0^1 \lvert f(t) \rvert^2 \,\dd t \ge 0 \), and we must rule out equality for \( f \ne 0 \). Here is the one fact from analysis we assume: if \( f \) is continuous and \( f(c) \ne 0 \) for some \( c \), then \( \lvert f \rvert \ge \lvert f(c) \rvert / 2 \) on some interval of positive length \( \delta \) around \( c \), so \( \int_0^1 \lvert f \rvert^2 \ge \delta \lvert f(c) \rvert^2 / 4 > 0 \). Continuity is not decoration; the non-example below shows what happens without it.

**Matrices: the Frobenius inner product.** First a piece of notation we will need all chapter.

::: {#def-conjugate-transpose}
[Conjugate Transpose]

For \( \A \in M_{m \times n}(F) \), the **conjugate transpose** \( \A^{*} \in M_{n \times m}(F) \) is the matrix with entries \( (\A^{*})_{ij} = \conj{a_{ji}} \). A square matrix with \( \A^{*} = \A \) is **Hermitian**.
:::

Over \( \nR \), \( \A^{*} = \A\tp \) and Hermitian means symmetric (@def-symmetric-matrix). Now on \( V = M_{m \times n}(F) \) define
\[
\inner{\A}{\B} = \tr(\B^{*}\A) .
\]
Writing out the trace, \( \tr(\B^{*}\A) = \sum_{j}\sum_{i} \conj{b_{ij}}a_{ij} \), so this is the standard inner product of \( F^{mn} \) after listing the entries in a column. In particular (IP1)–(IP3) hold, with \( \inner{\A}{\A} = \sum_{i,j}\lvert a_{ij} \rvert^2 \). This is the **Frobenius inner product**; for \( n = 1 \) it is the standard inner product on \( F^m \).

**Polynomials sampled at nodes.** Fix \( n + 1 \) **distinct** scalars \( c_0, \dots, c_n \in F \) and define, on \( V = F[x]_{\le n} \),
\[
\inner{p}{q} = \sum_{i=0}^{n} p(c_i)\conj{q(c_i)} .
\]
(IP1) and (IP2) hold because evaluation at \( c_i \) is linear (@thm-evaluation-respects-operations) and the standard inner product on \( F^{n+1} \) has them; indeed \( \inner{p}{q} \) is the standard inner product of the sample vectors \( (p(c_0), \dots, p(c_n)) \) and \( (q(c_0), \dots, q(c_n)) \). Positivity is the interesting clause. If \( \inner{p}{p} = \sum \lvert p(c_i) \rvert^2 = 0 \), then \( p \) vanishes at all \( n + 1 \) distinct nodes. A non-zero polynomial of degree at most \( n \) has at most \( n \) distinct roots (@cor-root-bound-general), so \( p = 0 \). The **number** of nodes is what makes this work, and the non-example below removes one.

## Non-examples, by minimal change

**Change a sign: the hyperbolic form on \( \nR^2 \).** Let \( \beta(\x, \y) = x_1y_1 - x_2y_2 \). Bilinearity survives, since each term is still linear in each slot, and so does symmetry. What fails is (IP3), and the witness is \( \e_2 \): \( \beta(\e_2, \e_2) = -1 < 0 \). The vector \( (1, 1) \) is worse still: it is non-zero, yet \( \beta((1,1),(1,1)) = 0 \), so it would be a non-zero vector of length \( 0 \). Forms like \( \beta \) are useful (they are the subject of the chapter on bilinear forms), but they are not inner products.

**Drop the conjugate on \( \nC^2 \).** Let \( \inner{\u}{\v} = \u\tp\v = u_1v_1 + u_2v_2 \) on \( \nC^2 \). This map is linear in **both** slots and symmetric, so it satisfies (IP1) and looks tidier than the standard product. Take \( \u = (1, i) \). Then
\[
\inner{\u}{\u} = 1^2 + i^2 = 1 - 1 = 0,
\]
with \( \u \ne \0 \). Clause (IP3) fails. This one example is the whole reason for the conjugate: over \( \nC \), sums of squares vanish on non-zero vectors, sums of squared **moduli** do not.

**Enlarge the space: drop continuity.** Keep the formula \( \inner{f}{g} = \int_0^1 fg \), but let \( V \) be all Riemann-integrable functions \( [0, 1] \to \nR \). Linearity and symmetry are untouched. Let \( f \) be \( 1 \) at \( t = \tfrac12 \) and \( 0 \) elsewhere. It is integrable, non-zero as a function, and \( \int_0^1 f^2 = 0 \). Positivity fails, so \( \inner{\cdot}{\cdot} \) is only **positive semidefinite** here. There are two standard repairs: restrict to continuous functions, as above, or regard two functions as equal when they differ on a negligible set. We take the first, and every function space in this chapter will be a space of continuous functions.

**Remove a node.** On \( \nR[x]_{\le 2} \), put \( \inner{p}{q} = p(0)q(0) + p(1)q(1) \): the node example with one node too few. Bilinearity and symmetry hold. But \( p = x^2 - x \) is a non-zero polynomial of degree \( 2 \) with \( p(0) = p(1) = 0 \), so \( \inner{p}{p} = 0 \). The clause that fails is (IP3), and it fails because two nodes cannot pin down a quadratic.

**Why this definition.** Each clause earns its place. Without (IP3) there can be non-zero vectors \( \v \) with \( \inner{\v}{\v} = 0 \), and the proof of @thm-inner-product-basic-properties (d) breaks down, because pairing a vector with itself no longer detects zero. (The form \( x_1y_1 - x_2y_2 \) below shows that the conclusion of (d) may survive anyway; what is lost is the argument for it, and with it every later proof that runs through \( \inner{\v}{\v} = 0 \Rightarrow \v = \0 \).) Without (IP2) the diagonal values need not be real, and "\( \inner{\v}{\v} > 0 \)" is meaningless. Linearity in the first slot rather than the second is a convention, but once chosen it must be kept: with (IP2) in place, linearity in one slot forces conjugate-linearity in the other, so a map cannot be linear in both unless \( F = \nR \).

::: {.warning}
**The conjugate goes in the second slot here, and books differ.** With our convention, \( \inner{a\u}{\v} = a\inner{\u}{\v} \) and \( \inner{\u}{a\v} = \conj{a}\inner{\u}{\v} \). Many books, especially in physics, put the conjugate in the first slot, so that their \( \inner{\u}{\v} \) is our \( \inner{\v}{\u} \). Every formula involving a lone conjugate then flips. When you read a formula elsewhere, check the convention first; when you write one, say which you use.
:::

::: {.check}
Is \( \inner{\x}{\y} = x_1y_1 + x_2y_2 + x_1y_2 \) an inner product on \( \nR^2 \)? If not, name the clause that fails and give a witness.
:::

::: {.solution}
No. It is bilinear, and \( \inner{\x}{\x} = x_1^2 + x_2^2 + x_1x_2 = (x_1 + \tfrac12 x_2)^2 + \tfrac34 x_2^2 > 0 \) for \( \x \ne \0 \), so (IP1) and (IP3) both hold. The clause that fails is (IP2): with \( \u = \e_1 \) and \( \v = \e_2 \) we get \( \inner{\u}{\v} = 1 \) but \( \inner{\v}{\u} = 0 \). Symmetrizing the cross term, to \( x_1y_1 + x_2y_2 + \tfrac12(x_1y_2 + x_2y_1) \), repairs it.
:::

## Norms

By @thm-inner-product-basic-properties (a), the number \( \inner{\v}{\v} \) is real and \( \ge 0 \), so it has a unique non-negative real square root. That square root is the length we were after.

::: {#def-induced-norm}
[Induced Norm]

Let \( V \) be an inner product space. The **norm** of \( \v \in V \) is
\[
\norm{\v} \coloneqq \sqrt{\inner{\v}{\v}} ,
\]
the **non-negative** real square root. A vector with \( \norm{\v} = 1 \) is a **unit vector**, and replacing a non-zero \( \v \) by \( \v / \norm{\v} \) is called **normalizing** it.
:::

On \( \nR^n \) with the dot product this is the Euclidean length \( \sqrt{x_1^2 + \dots + x_n^2} \), and on \( \nC^n \) it is \( \sqrt{\sum \lvert x_i \rvert^2} \). On \( C[0,1] \) it is \( \big(\int_0^1 \lvert f \rvert^2\big)^{1/2} \), and on matrices it is the **Frobenius norm** \( \big(\sum \lvert a_{ij} \rvert^2\big)^{1/2} \). By definition \( \norm{\v}^2 = \inner{\v}{\v} \) always, and this identity, read from right to left, is the most-used step in the chapter: **work with the norm squared, then expand.**

::: {#thm-norm-properties}
[Properties of the Induced Norm]

Let \( V \) be an inner product space over \( F \), \( \u, \v \in V \) and \( c \in F \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \norm{\v} \ge 0 \), with \( \norm{\v} = 0 \) if and only if \( \v = \0 \);
2. \( \norm{c\v} = \lvert c \rvert \norm{\v} \);
3. \( \norm{\u + \v}^2 = \norm{\u}^2 + 2\operatorname{Re}\inner{\u}{\v} + \norm{\v}^2 \).
:::
:::

::: {.proof}
(a) Immediate from @thm-inner-product-basic-properties (a) and the fact that a non-negative real number has square root \( 0 \) only when it is \( 0 \).

(b) By (IP1) and @thm-inner-product-basic-properties (b), \( \inner{c\v}{c\v} = c\conj{c}\inner{\v}{\v} = \lvert c \rvert^2\norm{\v}^2 \) using @thm-conjugate-properties (c). Taking non-negative square roots gives \( \norm{c\v} = \lvert c \rvert\norm{\v} \), since \( \lvert c \rvert \ge 0 \).

(c) Expand one slot at a time, by (IP1) and then @thm-inner-product-basic-properties (b):
\[
\begin{aligned}
\norm{\u + \v}^2
&= \inner{\u + \v}{\u + \v} \\
&= \inner{\u}{\u} + \inner{\u}{\v} + \inner{\v}{\u} + \inner{\v}{\v} .
\end{aligned}
\]
By (IP2), \( \inner{\v}{\u} = \conj{\inner{\u}{\v}} \), and \( z + \conj{z} = 2\operatorname{Re}z \) by @thm-conjugate-properties (c). This gives the stated identity.
:::

Part (c) is the workhorse. Over \( \nR \) the middle term is just \( 2\inner{\u}{\v} \), and the identity is the familiar \( (a + b)^2 = a^2 + 2ab + b^2 \) for vectors. Replacing \( \v \) by \( -\v \) gives \( \norm{\u - \v}^2 = \norm{\u}^2 - 2\operatorname{Re}\inner{\u}{\v} + \norm{\v}^2 \), and adding the two versions gives the **parallelogram law**
\[
\norm{\u + \v}^2 + \norm{\u - \v}^2 = 2\norm{\u}^2 + 2\norm{\v}^2 .
\tag{$\ast$}
\]
We return to \( (\ast) \) in the last warning of this section.

::: {.warning}
**A squared norm is real and non-negative, never complex.** If a computation in a complex space produces \( \norm{\v}^2 = 2i \), or a negative number, something has gone wrong — most often a missing conjugate. For \( \v = (1, i) \in \nC^2 \), the correct value is \( \norm{\v}^2 = \lvert 1 \rvert^2 + \lvert i \rvert^2 = 2 \), while the conjugate-free expression \( \v\tp\v \) gives \( 0 \). Use the answer as a check on the work.
:::

## Orthogonality and Pythagoras

With a norm in hand, the special relation \( \inner{\u}{\v} = 0 \) deserves its name.

::: {#def-orthogonal}
[Orthogonal Vectors]

Let \( V \) be an inner product space. Vectors \( \u, \v \in V \) are **orthogonal**, written \( \u \perp \v \), if \( \inner{\u}{\v} = 0 \). A list \( (\v_1, \dots, \v_k) \) is **orthogonal** if \( \v_i \perp \v_j \) whenever \( i \ne j \).
:::

The relation is symmetric: \( \inner{\u}{\v} = 0 \) if and only if \( \inner{\v}{\u} = \conj{\inner{\u}{\v}} = 0 \), so "\( \u \perp \v \)" needs no order. The zero vector is orthogonal to everything (@thm-inner-product-basic-properties (c)), and by part (a) of the same result it is the **only** vector orthogonal to itself. In \( \nR^n \) this is perpendicularity in the usual sense, by the law of cosines computation above: \( \cos\theta = 0 \) exactly when \( \x \cdot \y = 0 \). In \( \nC^2 \), the vectors \( (1, i) \) and \( (1, -i) \) are orthogonal, since \( 1\cdot\conj{1} + i\cdot\conj{(-i)} = 1 + i \cdot i = 0 \).

::: {#thm-pythagoras}
[Pythagorean Theorem]

Let \( (\v_1, \dots, \v_k) \) be an orthogonal list in an inner product space. Then
\[
\norm{\v_1 + \dots + \v_k}^2 = \norm{\v_1}^2 + \dots + \norm{\v_k}^2 .
\]
:::

::: {.proof}
Expand the left side by (IP1) and @thm-inner-product-basic-properties (b):
\[
\Big\langle \sum_{i} \v_i,\ \sum_{j} \v_j \Big\rangle = \sum_{i}\sum_{j} \inner{\v_i}{\v_j} .
\]
Every term with \( i \ne j \) is \( 0 \), because the list is orthogonal. What survives is \( \sum_i \inner{\v_i}{\v_i} = \sum_i \norm{\v_i}^2 \), as claimed.
:::

So orthogonality is exactly the condition under which squared lengths add. This is why the relation is worth naming, and why the rest of the chapter works so hard to produce orthogonal vectors.

::: {.warning}
**Over \( \nC \), the converse of Pythagoras fails.** By @thm-norm-properties (c), \( \norm{\u + \v}^2 = \norm{\u}^2 + \norm{\v}^2 \) says only that \( \operatorname{Re}\inner{\u}{\v} = 0 \), not that \( \inner{\u}{\v} = 0 \). In \( \nC \) with \( \inner{z}{w} = z\conj{w} \), take \( \u = 1 \) and \( \v = i \): then \( \inner{\u}{\v} = \conj{i} = -i \ne 0 \), yet \( \norm{1 + i}^2 = 2 = \norm{1}^2 + \norm{i}^2 \). Over \( \nR \) the converse does hold, since there \( \operatorname{Re} \) does nothing.
:::

::: {#thm-orthogonal-independent}
[Orthogonal Non-zero Vectors Are Independent]

Let \( (\v_1, \dots, \v_k) \) be an orthogonal list of **non-zero** vectors in an inner product space. Then the list is linearly independent.
:::

::: {.idea}
Start a dependence relation in the standard way, and then do the one thing an inner product allows: pair the relation with a single \( \v_j \). Orthogonality kills every term except the \( j \)-th, and what is left is \( a_j\norm{\v_j}^2 = 0 \) with \( \norm{\v_j} \ne 0 \).
:::

::: {.proof}
Let \( a_1\v_1 + \dots + a_k\v_k = \0 \) with \( a_1, \dots, a_k \in F \). Fix \( j \) and take the inner product of both sides with \( \v_j \). By (IP1) and @thm-inner-product-basic-properties (c),
\[
0 = \Big\langle \sum_{i} a_i\v_i,\ \v_j \Big\rangle = \sum_{i} a_i\inner{\v_i}{\v_j} = a_j\norm{\v_j}^2 ,
\]
where the last equality holds because \( \inner{\v_i}{\v_j} = 0 \) for \( i \ne j \). Since \( \v_j \ne \0 \), @thm-inner-product-basic-properties (a) gives \( \norm{\v_j}^2 > 0 \), so \( a_j = 0 \). As \( j \) was arbitrary, all the coefficients vanish, and the list is linearly independent by @def-linear-independence.
:::

The hypothesis "non-zero" cannot be dropped: the list \( (\e_1, \0) \) is orthogonal and dependent. With it, the result is a free supply of independent lists, and this is what makes the next section possible.

## The Cauchy–Schwarz inequality

Angles came from the formula \( \cos\theta = (\x \cdot \y)/(\norm{\x}\norm{\y}) \). To define an angle by that formula in an abstract space, we must know that the right-hand side lies in \( [-1, 1] \). That is exactly the following inequality, the most used inequality in the subject.

::: {#thm-cauchy-schwarz}
[Cauchy–Schwarz Inequality]

Let \( V \) be an inner product space and \( \u, \v \in V \). Then
\[
\lvert \inner{\u}{\v} \rvert \le \norm{\u}\,\norm{\v} ,
\]
with equality if and only if the list \( (\u, \v) \) is linearly dependent.
:::

::: {.idea}
Picture \( \u \) and \( \v \) in \( \nR^2 \). Drop a perpendicular from the tip of \( \u \) onto the line through \( \v \). The foot of the perpendicular is a multiple \( c\v \), and the two legs \( c\v \) and \( \u - c\v \) of the resulting right triangle have squared lengths adding to \( \norm{\u}^2 \). Since one leg has squared length \( \lvert\inner{\u}{\v}\rvert^2 / \norm{\v}^2 \), the inequality is just "a leg is no longer than the hypotenuse", and equality means the other leg is \( \0 \). The picture proves nothing in an abstract space, so we check algebraically that \( \u - c\v \perp \v \) for the right \( c \), and then let Pythagoras do the work.
:::

::: {.proof}
If \( \v = \0 \), both sides are \( 0 \) by @thm-inner-product-basic-properties (c), and \( (\u, \0) \) is dependent, so the statement holds. Suppose \( \v \ne \0 \), so \( \norm{\v} > 0 \), and put
\[
c = \frac{\inner{\u}{\v}}{\norm{\v}^2}, \qquad \z = \u - c\v .
\]
Then \( \z \perp \v \), since by (IP1)
\[
\inner{\z}{\v} = \inner{\u}{\v} - c\inner{\v}{\v} = \inner{\u}{\v} - \inner{\u}{\v} = 0 ,
\]
and hence also \( \z \perp c\v \). Now \( \u = \z + c\v \) is a sum of two orthogonal vectors, so @thm-pythagoras and @thm-norm-properties (b) give
\[
\norm{\u}^2 = \norm{\z}^2 + \lvert c \rvert^2\norm{\v}^2
= \norm{\z}^2 + \frac{\lvert \inner{\u}{\v} \rvert^2}{\norm{\v}^2} .
\tag{$\dagger$}
\]
Since \( \norm{\z}^2 \ge 0 \), dropping it gives \( \norm{\u}^2\norm{\v}^2 \ge \lvert \inner{\u}{\v} \rvert^2 \), and taking non-negative square roots proves the inequality.

Equality holds in \( (\dagger) \) exactly when \( \norm{\z} = 0 \), that is (@thm-norm-properties (a)) exactly when \( \u = c\v \). If \( \u = c\v \), the list \( (\u, \v) \) is dependent. Conversely, suppose \( (\u, \v) \) is dependent, say \( a\u + b\v = \0 \) with \( a, b \) not both \( 0 \). Here \( a \ne 0 \), since \( a = 0 \) would give \( b\v = \0 \) with \( b \ne 0 \) and hence \( \v = \0 \), which we have excluded. So \( \u = d\v \) with \( d = -b/a \), and then \( c = d\inner{\v}{\v}/\norm{\v}^2 = d \), so \( \z = \0 \). This proves the equality case.
:::

The proof is worth rereading for its shape: the vector \( \z \) was **found** from a picture and then **checked** from the axioms. That is the standard way to work in an abstract inner product space.

::: {#cor-triangle-inequality}
[Triangle Inequality]

Let \( V \) be an inner product space and \( \u, \v \in V \). Then
\[
\norm{\u + \v} \le \norm{\u} + \norm{\v} .
\]
:::

::: {.proof}
For any complex number \( z \) we have \( \operatorname{Re}z \le \lvert z \rvert \), as in the proof of @thm-complex-triangle-inequality. Hence, by @thm-norm-properties (c) and then @thm-cauchy-schwarz,
\[
\begin{aligned}
\norm{\u + \v}^2
&= \norm{\u}^2 + 2\operatorname{Re}\inner{\u}{\v} + \norm{\v}^2 \\
&\le \norm{\u}^2 + 2\lvert\inner{\u}{\v}\rvert + \norm{\v}^2 \\
&\le \norm{\u}^2 + 2\norm{\u}\norm{\v} + \norm{\v}^2 \\
&= \big(\norm{\u} + \norm{\v}\big)^2 .
\end{aligned}
\]
Both \( \norm{\u + \v} \) and \( \norm{\u} + \norm{\v} \) are \( \ge 0 \), so taking square roots preserves the inequality.
:::

Together, @thm-norm-properties (a), (b) and @cor-triangle-inequality say that \( \norm{\cdot} \) is a **norm** in the general sense studied in Chapter 15. Chapter 15 also shows that not every norm arises from an inner product; the last warning of this section explains how to tell.

::: {#def-angle}
[Angle Between Vectors]

Let \( V \) be a **real** inner product space and let \( \u, \v \in V \) be **non-zero**. The **angle** between \( \u \) and \( \v \) is the unique \( \theta \in [0, \pi] \) with
\[
\cos\theta = \frac{\inner{\u}{\v}}{\norm{\u}\,\norm{\v}} .
\]
:::

The definition needs @thm-cauchy-schwarz twice over. Cauchy–Schwarz says the quotient has absolute value at most \( 1 \), so it lies in \( [-1, 1] \); and \( \cos \) is a strictly decreasing bijection from \( [0, \pi] \) onto \( [-1, 1] \), so exactly one \( \theta \) qualifies. Without the inequality the formula could ask for the angle whose cosine is \( 7 \). Note also that \( \theta = \pi/2 \) if and only if \( \inner{\u}{\v} = 0 \), so the definition is consistent with @def-orthogonal.

Over \( \nC \) there is no angle, because \( \inner{\u}{\v} \) is not real. The quantity \( \lvert\inner{\u}{\v}\rvert / (\norm{\u}\norm{\v}) \in [0, 1] \) still makes sense, and it still measures how far the two vectors are from being orthogonal.

::: {#exm-angle-computations}
[Three Angles]

Compute the angle between \( \u = (1, 1, 0) \) and \( \v = (1, 0, 1) \) in \( \nR^3 \) with the dot product; between \( p = 1 \) and \( q = x \) in \( \nR[x]_{\le 1} \) with \( \inner{p}{q} = \int_0^1 pq \); and between \( \A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \) and \( \B = \begin{pmatrix} 1 & -1 \\ 1 & -1 \end{pmatrix} \) in \( M_2(\nR) \) with the Frobenius inner product.
:::

::: {.solution}
In \( \nR^3 \): \( \inner{\u}{\v} = 1 \), \( \norm{\u} = \norm{\v} = \sqrt2 \), so \( \cos\theta = 1/2 \) and \( \theta = \pi/3 \).

In \( \nR[x]_{\le 1} \): \( \inner{1}{x} = \int_0^1 t\,\dd t = \tfrac12 \), \( \norm{1}^2 = \int_0^1 1 = 1 \) and \( \norm{x}^2 = \int_0^1 t^2\,\dd t = \tfrac13 \). Hence
\[
\cos\theta = \frac{1/2}{1 \cdot 1/\sqrt3} = \frac{\sqrt3}{2},
\]
so \( \theta = \pi/6 \). The constant \( 1 \) and the function \( x \) are far from orthogonal on \( [0, 1] \), which is believable: both are positive there.

In \( M_2(\nR) \): \( \inner{\A}{\B} = 1 - 1 + 1 - 1 = 0 \), so \( \theta = \pi/2 \). The two matrices are orthogonal, with \( \norm{\A} = \norm{\B} = 2 \). As a check on Pythagoras, \( \A + \B = \begin{pmatrix} 2 & 0 \\ 2 & 0 \end{pmatrix} \) has \( \norm{\A + \B}^2 = 8 = 4 + 4 \).
:::

::: {.check}
In \( \nC^2 \) with the standard inner product, compute \( \inner{(1, i)}{(1, 1)} \) and \( \inner{(1, 1)}{(1, i)} \). Check the answers against (IP2), and against Cauchy–Schwarz.
:::

::: {.solution}
\( \inner{(1,i)}{(1,1)} = 1\cdot\conj1 + i\cdot\conj1 = 1 + i \), and \( \inner{(1,1)}{(1,i)} = 1\cdot\conj1 + 1\cdot\conj{i} = 1 - i \). They are conjugates, as (IP2) requires. For Cauchy–Schwarz, \( \lvert 1 + i \rvert = \sqrt2 \), while \( \norm{(1,i)} = \sqrt2 \) and \( \norm{(1,1)} = \sqrt2 \), so the inequality reads \( \sqrt2 \le 2 \). It is strict, which is right: \( (1, i) \) and \( (1, 1) \) are independent.
:::

::: {.warning}
**Not every norm comes from an inner product.** A function \( \norm{\cdot} \) can satisfy positivity, homogeneity and the inequality of @cor-triangle-inequality without being \( \sqrt{\inner{\v}{\v}} \) for any inner product. The test is the parallelogram law \( (\ast) \): every induced norm satisfies it, as we derived from @thm-norm-properties (c), so a norm that violates it is induced by nothing. Take \( \norm{\x}_\infty = \max(\lvert x_1 \rvert, \lvert x_2 \rvert) \) on \( \nR^2 \) with \( \u = \e_1 \), \( \v = \e_2 \). Then \( \norm{\u + \v}_\infty = \norm{\u - \v}_\infty = 1 \), so the left side of \( (\ast) \) is \( 2 \), while the right side is \( 4 \). Remarkably, the law is not only necessary but sufficient; @exr-inner-products-c1 proves the substance of that in \( \nR^2 \), and Chapter 15 takes up general norms.
:::

## Exercises

### A. Check your understanding

:::: {#exr-inner-products-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the three axioms of an inner product on a vector space over \( F = \nR \) or \( \nC \), and say in which slot the map is linear.
2. Why must the field be \( \nR \) or \( \nC \)? Name the two features used.
3. Explain why \( \inner{\v}{\v} \) is always a real number.
4. True or false: an inner product on a complex space is linear in the second slot. Justify your answer.
5. State the Cauchy–Schwarz inequality, its equality case, and one place where the equality case is used.
6. True or false: if \( \norm{\u + \v}^2 = \norm{\u}^2 + \norm{\v}^2 \) in a complex inner product space, then \( \u \perp \v \). Justify your answer.
:::
::::

::: {.solution}
(a) (IP1) \( \inner{a\u + b\v}{\w} = a\inner{\u}{\w} + b\inner{\v}{\w} \); (IP2) \( \inner{\v}{\u} = \conj{\inner{\u}{\v}} \); (IP3) \( \inner{\v}{\v} > 0 \) for \( \v \ne \0 \) (@def-inner-product). It is linear in the **first** slot.

(b) Positivity, so that \( \inner{\v}{\v} > 0 \) has meaning and square roots exist, and conjugation, so that \( \inner{\v}{\v} \) is real and non-negative over \( \nC \).

(c) By (IP2) with \( \u = \v \), the number equals its own conjugate, so its imaginary part is \( 0 \) (@thm-inner-product-basic-properties (a)).

(d) False. It is **conjugate**-linear in the second slot: \( \inner{\u}{a\v} = \conj{a}\inner{\u}{\v} \) (@thm-inner-product-basic-properties (b)). For example, in \( \nC \) with \( \inner{z}{w} = z\conj{w} \), \( \inner{1}{i} = -i \) while \( i\inner{1}{1} = i \).

(e) \( \lvert\inner{\u}{\v}\rvert \le \norm{\u}\norm{\v} \), with equality if and only if \( (\u, \v) \) is dependent (@thm-cauchy-schwarz). The inequality is what makes @def-angle well posed: it puts the quotient \( \inner{\u}{\v}/(\norm{\u}\norm{\v}) \) inside \( [-1, 1] \), where \( \arccos \) is defined. The equality case then says which vectors sit at the ends of that interval: \( \cos\theta = \pm 1 \) exactly for dependent pairs, that is, \( \theta = 0 \) or \( \theta = \pi \).

(f) False. It says only \( \operatorname{Re}\inner{\u}{\v} = 0 \). In \( \nC \) with \( \inner{z}{w} = z\conj{w} \), take \( \u = 1 \), \( \v = i \): then \( \inner{\u}{\v} = -i \ne 0 \) but \( \norm{1 + i}^2 = 2 = 1 + 1 \).
:::

### B. Practice

:::: {#exr-inner-products-b1}
[B1: Determine which are inner products]

Determine which of the following are inner products on the stated space. For those that are, verify the axioms; for those that are not, name the clause that fails and give an explicit witness.

::: {.enumerate options="label=(\alph*)"}
1. On \( \nR^2 \): \( \inner{\x}{\y} = x_1y_1 + 3x_2y_2 \).
2. On \( \nR^2 \): \( \inner{\x}{\y} = x_1y_1 + x_1y_2 + x_2y_1 + 2x_2y_2 \).
3. On \( \nC^2 \): \( \inner{\x}{\y} = x_1\conj{y_1} + x_2y_2 \).
4. On \( M_2(\nR) \): \( \inner{\A}{\B} = \tr(\A\B) \).
5. On \( \nR[x]_{\le 2} \): \( \inner{p}{q} = p(0)q(0) + p(1)q(1) + p(2)q(2) \).
:::
::::

::: {.solution}
(a) An inner product: it is the weighted product with weights \( 1, 3 > 0 \). Bilinearity and symmetry are clear, and \( \inner{\x}{\x} = x_1^2 + 3x_2^2 = 0 \) forces \( x_1 = x_2 = 0 \).

(b) An inner product. It is bilinear term by term, and symmetric because the two cross terms are interchanged by swapping \( \x \) and \( \y \). For positivity, complete the square:
\[
\inner{\x}{\x} = x_1^2 + 2x_1x_2 + 2x_2^2 = (x_1 + x_2)^2 + x_2^2 ,
\]
which is \( 0 \) only if \( x_2 = 0 \) and \( x_1 + x_2 = 0 \), that is \( \x = \0 \).

(c) Not an inner product. (IP2) fails: with \( \x = (0, 1) \) and \( \y = (0, i) \) we get \( \inner{\x}{\y} = i \) and \( \inner{\y}{\x} = i \), while (IP2) would require \( \inner{\y}{\x} = \conj{i} = -i \). Positivity fails too, at \( \x = (0, i) \): \( \inner{\x}{\x} = i^2 = -1 \).

(d) Not an inner product. It is bilinear, and symmetric by @thm-trace-properties (3). But (IP3) fails for \( \N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \ne 0 \), since \( \N^2 = 0 \) and so \( \inner{\N}{\N} = \tr(\N^2) = 0 \). Replacing \( \tr(\A\B) \) by \( \tr(\B\tp\A) \) repairs it: that is the Frobenius inner product.

(e) An inner product: the node example with the three distinct nodes \( 0, 1, 2 \) on \( \nR[x]_{\le 2} \). Bilinearity and symmetry come from linearity of evaluation. If \( \inner{p}{p} = p(0)^2 + p(1)^2 + p(2)^2 = 0 \), then \( p \) has three distinct roots and degree at most \( 2 \), so \( p = 0 \) by @cor-root-bound-general.
:::

:::: {#exr-inner-products-b2}
[B2: Norms and angles]

::: {.enumerate options="label=(\alph*)"}
1. In \( \nR^3 \) with the dot product, find \( \norm{\u} \), \( \norm{\v} \) and the cosine of the angle between \( \u = (1, 2, 2) \) and \( \v = (2, -1, 2) \).
2. In \( \nR[x]_{\le 2} \) with \( \inner{p}{q} = \int_{-1}^{1} pq \), compute \( \norm{1} \), \( \norm{x} \) and \( \inner{1}{x} \). What is the angle between \( 1 \) and \( x \)?
3. In \( M_2(\nC) \) with the Frobenius inner product, compute \( \norm{\A} \) for \( \A = \begin{pmatrix} 1 & i \\ 0 & 1 + i \end{pmatrix} \).
:::
::::

::: {.solution}
(a) \( \norm{\u} = \sqrt{1 + 4 + 4} = 3 \) and \( \norm{\v} = \sqrt{4 + 1 + 4} = 3 \). Also \( \inner{\u}{\v} = 2 - 2 + 4 = 4 \), so \( \cos\theta = 4/9 \). Cauchy–Schwarz reads \( 4 \le 9 \), and it is strict, as it must be for an independent pair.

(b) \( \norm{1}^2 = \int_{-1}^1 1\,\dd t = 2 \), so \( \norm{1} = \sqrt2 \); \( \norm{x}^2 = \int_{-1}^1 t^2\,\dd t = \tfrac23 \), so \( \norm{x} = \sqrt{2/3} \); and \( \inner{1}{x} = \int_{-1}^1 t\,\dd t = 0 \). The angle is \( \pi/2 \): on a symmetric interval, the constants are orthogonal to the odd functions. Compare this with @exm-angle-computations, where the interval \( [0, 1] \) gave the angle \( \pi/6 \) instead. **The geometry depends on the inner product, not only on the vectors.**

(c) \( \norm{\A}^2 = \lvert 1 \rvert^2 + \lvert i \rvert^2 + 0 + \lvert 1 + i \rvert^2 = 1 + 1 + 2 = 4 \), so \( \norm{\A} = 2 \).
:::

:::: {#exr-inner-products-b3}
[B3: Cauchy–Schwarz, concretely]

::: {.enumerate options="label=(\alph*)"}
1. Verify @thm-cauchy-schwarz for \( \a = (1, 2, 3) \) and \( \b = (3, 2, 1) \) in \( \nR^3 \) with the dot product, and say whether the inequality is strict.
2. Deduce from @thm-cauchy-schwarz the classical inequality
\[
\Big(\sum_{i=1}^{n} a_ib_i\Big)^2 \le \Big(\sum_{i=1}^{n} a_i^2\Big)\Big(\sum_{i=1}^{n} b_i^2\Big)
\]
for all real \( a_i, b_i \).
3. Hence show that \( (a_1 + \dots + a_n)^2 \le n(a_1^2 + \dots + a_n^2) \) for all real \( a_i \).
:::
::::

::: {.solution}
(a) \( \inner{\a}{\b} = 3 + 4 + 3 = 10 \), so \( \lvert\inner{\a}{\b}\rvert^2 = 100 \), while \( \norm{\a}^2\norm{\b}^2 = 14 \cdot 14 = 196 \). So \( 10 \le 14 \), strictly. It must be strict, since \( \a \) and \( \b \) are not multiples of each other.

(b) Apply @thm-cauchy-schwarz on \( \nR^n \) with the dot product to \( \a = (a_1, \dots, a_n) \) and \( \b = (b_1, \dots, b_n) \). Then \( \inner{\a}{\b} = \sum a_ib_i \), \( \norm{\a}^2 = \sum a_i^2 \) and \( \norm{\b}^2 = \sum b_i^2 \), and squaring the inequality \( \lvert\inner{\a}{\b}\rvert \le \norm{\a}\norm{\b} \) gives the claim.

(c) Take \( b_i = 1 \) for all \( i \) in (b). Then \( \sum a_ib_i = \sum a_i \) and \( \sum b_i^2 = n \), so \( (\sum a_i)^2 \le n\sum a_i^2 \). Equality holds exactly when \( \a \) is a multiple of \( (1, \dots, 1) \), that is, when all the \( a_i \) are equal.
:::

:::: {#exr-inner-products-b4}
[B4: A lower bound for a difference of norms]

Let \( V \) be an inner product space and \( \u, \v \in V \). Prove that
\[
\big\lvert \norm{\u} - \norm{\v} \big\rvert \le \norm{\u - \v} .
\]
::::

::: {.solution}
Write \( \u = (\u - \v) + \v \). By @cor-triangle-inequality,
\[
\norm{\u} \le \norm{\u - \v} + \norm{\v},
\]
so \( \norm{\u} - \norm{\v} \le \norm{\u - \v} \). Swapping the roles of \( \u \) and \( \v \) gives \( \norm{\v} - \norm{\u} \le \norm{\v - \u} \), and \( \norm{\v - \u} = \lvert -1 \rvert\norm{\u - \v} = \norm{\u - \v} \) by @thm-norm-properties (b). The quantity \( \lvert \norm{\u} - \norm{\v} \rvert \) is one of the two numbers just bounded, so it is at most \( \norm{\u - \v} \). This proves the inequality.
:::

### C. Going deeper

:::: {#exr-inner-products-c1}
[C1: The parallelogram law characterizes inner-product norms]

Let \( \norm{\cdot} \) be a norm on \( \nR^2 \), that is, a function \( \nR^2 \to \nR \) satisfying the three properties of @thm-norm-properties (a), (b) and @cor-triangle-inequality. Suppose it satisfies the parallelogram law
\[
\norm{\u + \v}^2 + \norm{\u - \v}^2 = 2\norm{\u}^2 + 2\norm{\v}^2
\]
for all \( \u, \v \), and define \( \beta(\u, \v) = \tfrac14\big(\norm{\u + \v}^2 - \norm{\u - \v}^2\big) \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \beta(\u, \u) = \norm{\u}^2 \), that \( \beta(\u, \v) = \beta(\v, \u) \), and that \( \beta(\u, \0) = 0 \).
2. Prove that \( \beta(\u, \v) + \beta(\u, \w) = 2\beta\big(\u, \tfrac12(\v + \w)\big) \) for all \( \u, \v, \w \).
3. Deduce that \( \beta(\u, \v) + \beta(\u, \w) = \beta(\u, \v + \w) \).
4. Granting that \( \beta(\u, t\v) = t\beta(\u, \v) \) for all \( t \in \nR \), conclude that \( \beta \) is an inner product on \( \nR^2 \) whose induced norm is \( \norm{\cdot} \).
:::

*Hint: for (b), apply the parallelogram law to the pair \( \u + \tfrac12(\v + \w) \), \( \tfrac12(\v - \w) \), and then to the pair \( \u - \tfrac12(\v + \w) \), \( \tfrac12(\w - \v) \).*
::::

::: {.solution}
(a) \( \beta(\u, \u) = \tfrac14(\norm{2\u}^2 - \norm{\0}^2) = \tfrac14 \cdot 4\norm{\u}^2 = \norm{\u}^2 \), using homogeneity. Symmetry holds because \( \norm{\v - \u} = \norm{\u - \v} \), again by homogeneity with \( c = -1 \). Finally \( \beta(\u, \0) = \tfrac14(\norm{\u}^2 - \norm{\u}^2) = 0 \).

(b) Put \( \m = \tfrac12(\v + \w) \) and \( \d = \tfrac12(\v - \w) \), so that \( \v = \m + \d \) and \( \w = \m - \d \). Apply the parallelogram law to \( \u + \m \) and \( \d \): since \( (\u + \m) + \d = \u + \v \) and \( (\u + \m) - \d = \u + \w \),
\[
\norm{\u + \v}^2 + \norm{\u + \w}^2 = 2\norm{\u + \m}^2 + 2\norm{\d}^2 .
\]
Apply it to \( \u - \m \) and \( \d \): since \( (\u - \m) - \d = \u - \v \) and \( (\u - \m) + \d = \u - \w \),
\[
\norm{\u - \v}^2 + \norm{\u - \w}^2 = 2\norm{\u - \m}^2 + 2\norm{\d}^2 .
\]
Subtracting the second from the first, the terms \( 2\norm{\d}^2 \) cancel, and dividing by \( 4 \) gives \( \beta(\u, \v) + \beta(\u, \w) = 2\beta(\u, \m) \), which is the claim.

(c) Take \( \w = \0 \) in (b). By (a), \( \beta(\u, \0) = 0 \), so \( \beta(\u, \v) = 2\beta(\u, \tfrac12\v) \) for all \( \v \). Applying this with \( \v + \w \) in place of \( \v \), we get \( 2\beta(\u, \tfrac12(\v + \w)) = \beta(\u, \v + \w) \), and the left side is \( \beta(\u, \v) + \beta(\u, \w) \) by (b).

(d) By (c) and the granted homogeneity, \( \beta \) is linear in its second slot, and by the symmetry in (a) it is then linear in the first as well, so (IP1) and (IP2) hold (conjugation is trivial over \( \nR \)). For (IP3), \( \beta(\u, \u) = \norm{\u}^2 > 0 \) for \( \u \ne \0 \), since a norm vanishes only at \( \0 \). So \( \beta \) is an inner product, and its induced norm is \( \sqrt{\beta(\u,\u)} = \norm{\u} \).

*Remark.* The granted step in (d) is where analysis enters: additivity from (c) gives \( \beta(\u, t\v) = t\beta(\u, \v) \) for every **rational** \( t \) by induction, and the extension to real \( t \) uses that \( t \mapsto \beta(\u, t\v) \) is continuous, which follows from continuity of the norm. Nothing else in the argument needs anything beyond the three norm properties.
:::

:::: {#exr-inner-products-c2}
[C2: Recovering the inner product from the norm]

Let \( V \) be an inner product space over \( F \).

::: {.enumerate options="label=(\alph*)"}
1. For \( F = \nR \), prove the polarization identity \( \inner{\u}{\v} = \tfrac14\big(\norm{\u + \v}^2 - \norm{\u - \v}^2\big) \).
2. For \( F = \nC \), prove that
\[
\inner{\u}{\v} = \frac14\sum_{k=0}^{3} i^{k}\,\norm{\u + i^{k}\v}^2 .
\]
3. Deduce that two inner products on \( V \) with the same induced norm are equal.
:::
::::

::: {.solution}
(a) By @thm-norm-properties (c) and its version with \( -\v \), and since \( \operatorname{Re} \) is the identity on \( \nR \),
\[
\norm{\u + \v}^2 - \norm{\u - \v}^2 = 4\inner{\u}{\v}.
\]
Dividing by \( 4 \) gives the identity.

(b) Write \( z = \inner{\u}{\v} \). By @thm-norm-properties (c) and @thm-inner-product-basic-properties (b),
\[
\norm{\u + i^k\v}^2 = \norm{\u}^2 + \norm{\v}^2 + 2\operatorname{Re}\big(\conj{i^{k}}z\big),
\]
where we used \( \norm{i^k\v} = \lvert i^k \rvert \norm{\v} = \norm{\v} \). Now \( \sum_{k=0}^3 i^k = 1 + i - 1 - i = 0 \), so the terms \( \norm{\u}^2 + \norm{\v}^2 \) contribute nothing. Writing \( z = a + bi \) with \( a, b \in \nR \), the four remaining terms \( 2 i^k \operatorname{Re}(\conj{i^k}z) \) are, for \( k = 0, 1, 2, 3 \),
\[
2a, \quad 2ib, \quad 2a, \quad 2ib,
\]
since \( \operatorname{Re}(z) = a \), \( \operatorname{Re}(-iz) = b \), \( \operatorname{Re}(-z) = -a \) and \( \operatorname{Re}(iz) = -b \). Their sum is \( 4a + 4bi = 4z \), and dividing by \( 4 \) gives the identity.

(c) Both (a) and (b) express \( \inner{\u}{\v} \) using only the norm. So if two inner products induce the same norm, the right-hand sides agree for all \( \u, \v \), hence so do the left-hand sides.
:::

:::: {#exr-inner-products-c3}
[C3: The equality cases]

Let \( V \) be an inner product space.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \norm{\u + \v} = \norm{\u} + \norm{\v} \) if and only if one of \( \u, \v \) is a **non-negative real** multiple of the other.
2. Deduce the equality condition in the classical inequality of @exr-inner-products-b3 (b): for real \( a_i, b_i \), equality holds if and only if one of the vectors \( (a_1, \dots, a_n) \), \( (b_1, \dots, b_n) \) is a multiple of the other.
3. Give real numbers \( a_i, b_i \), not all zero, with \( \sum a_ib_i < 0 \) and equality in the classical inequality, and explain why this does **not** contradict (a).
:::
::::

::: {.solution}
(a) \( (\Leftarrow) \) If \( \v = \0 \) both sides are \( \norm{\u} \). If \( \u = t\v \) with \( t \ge 0 \), then \( \norm{\u + \v} = (t + 1)\norm{\v} = t\norm{\v} + \norm{\v} = \norm{\u} + \norm{\v} \) by @thm-norm-properties (b).

\( (\Rightarrow) \) Suppose \( \norm{\u + \v} = \norm{\u} + \norm{\v} \). Squaring and using @thm-norm-properties (c),
\[
2\operatorname{Re}\inner{\u}{\v} = 2\norm{\u}\norm{\v} .
\]
The chain in the proof of @cor-triangle-inequality is therefore an equality throughout, so \( \operatorname{Re}\inner{\u}{\v} = \lvert\inner{\u}{\v}\rvert = \norm{\u}\norm{\v} \). The second equality and @thm-cauchy-schwarz make \( (\u, \v) \) dependent. Assume \( \v \ne \0 \) (otherwise \( \v = 0\u \) and we are done) and write \( \u = c\v \). Then \( \inner{\u}{\v} = c\norm{\v}^2 \), and the first equality says \( \operatorname{Re}(c)\norm{\v}^2 = \lvert c \rvert \norm{\v}^2 \), so \( \operatorname{Re}c = \lvert c \rvert \), which forces \( c \) to be real and \( \ge 0 \).

(b) Apply @thm-cauchy-schwarz on \( \nR^n \) as in @exr-inner-products-b3 (b). Squaring removes the sign, so equality in the squared inequality is equality in \( \lvert\inner{\a}{\b}\rvert = \norm{\a}\norm{\b} \), which by @thm-cauchy-schwarz holds exactly when \( (\a, \b) \) is dependent, that is, when one of the two vectors is a multiple of the other.

(c) Take \( n = 1 \), \( a_1 = 1 \), \( b_1 = -1 \): then \( \sum a_ib_i = -1 \) and both sides of the classical inequality equal \( 1 \). There is no contradiction with (a), because (a) is about equality in @cor-triangle-inequality, which needs a non-negative multiple, while the classical inequality is the **squared** Cauchy–Schwarz inequality, which is blind to the sign. Here \( \norm{\a + \b} = 0 \ne 2 = \norm{\a} + \norm{\b} \).
:::
