# Complex Numbers

The equation \( x^2 + 1 = 0 \) has no real solution, because the square of a real number is never negative. For most of school mathematics this gap is harmless. In linear algebra it is not: later in the book we meet real matrices, such as a rotation of the plane, whose most useful data cannot be found among the real numbers. This section builds the complex numbers, the number system that closes the gap, and collects the facts about them that the rest of the book uses.

## The complex numbers as pairs of reals

The quick way to introduce complex numbers is to say "invent a symbol \( i \) with \( i^2 = -1 \) and compute as usual". That raises a fair worry. How do we know that such a symbol does not lead to a contradiction, the way "invent a number \( z \) with \( 0 \cdot z = 1 \)" does? The answer is to build the new numbers out of objects we already trust: pairs of real numbers.

Here is the recurring expression that suggests the definition. If we pretend \( i^2 = -1 \) and expand, we get
\[
(a + bi)(c + di) = ac + adi + bci + bd\, i^2 = (ac - bd) + (ad + bc)i.
\]
So a "number \( a + bi \)" is really the pair \( (a, b) \), and the product should be the pair \( (ac - bd, ad + bc) \). We take this formula as the definition, so nothing is pretended.

*A complex number is a pair of real numbers, multiplied as if \( i^2 = -1 \).*

::: {#def-complex-numbers}
[Complex Numbers]

The set of **complex numbers** is \( \nC \coloneqq \nR^2 = \{ (a, b) : a, b \in \nR \} \), with addition and multiplication defined **for every** \( (a, b), (c, d) \in \nC \) by
\[
(a, b) + (c, d) \coloneqq (a + c, \; b + d), \qquad (a, b)(c, d) \coloneqq (ac - bd, \; ad + bc).
\]
We write \( a \) for \( (a, 0) \) and \( i \) for \( (0, 1) \), so that \( (a, b) = a + bi \). For \( z = a + bi \) with \( a, b \in \nR \), the **real part** of \( z \) is \( \operatorname{Re} z \coloneqq a \) and the **imaginary part** of \( z \) is \( \operatorname{Im} z \coloneqq b \).
:::

In words: addition is coordinate by coordinate, as for points of the plane. Multiplication is the formula found by expanding. The last sentence is a naming convention: the real number \( a \) is identified with the point \( (a, 0) \) on the horizontal axis, and \( i \) is the point one unit up. Note that the imaginary part \( b \) is a **real** number; it is not \( bi \).

Two things need checking before this convention is safe.

- **The notation \( a + bi \) is honest.** By the definitions, \( a + bi = (a, 0) + (b, 0)(0, 1) = (a, 0) + (0, b) = (a, b) \). Two complex numbers are equal exactly when they are equal as pairs, so \( a + bi = c + di \) with \( a, b, c, d \in \nR \) means \( a = c \) **and** \( b = d \). This is how we "compare real and imaginary parts".
- **Identifying \( a \) with \( (a, 0) \) does not change real arithmetic.** We have \( (a, 0) + (c, 0) = (a + c, 0) \) and \( (a, 0)(c, 0) = (ac - 0, 0 + 0) = (ac, 0) \). So adding or multiplying two real numbers inside \( \nC \) gives the same answer as in \( \nR \).

With these in place, the equation that motivated everything is now a computation: \( i^2 = (0, 1)(0, 1) = (0 \cdot 0 - 1 \cdot 1, \; 0 \cdot 1 + 1 \cdot 0) = (-1, 0) = -1 \).

::: {#exm-complex-arithmetic}
[First Computations in \( \nC \)]

Compute \( (2 + 3i)(1 - i) \), the powers \( i^0, i^1, \dots, i^7 \), and the product \( (a + bi)(a - bi) \) for real \( a, b \).
:::

::: {.solution}
By the multiplication rule with \( a = 2 \), \( b = 3 \), \( c = 1 \), \( d = -1 \),
\[
(2 + 3i)(1 - i) = \big(2 \cdot 1 - 3 \cdot (-1)\big) + \big(2 \cdot (-1) + 3 \cdot 1\big) i = 5 + i.
\]
For the powers, \( i^0 = 1 \), \( i^1 = i \), \( i^2 = -1 \), \( i^3 = i^2 \cdot i = -i \) and \( i^4 = (-i) i = -i^2 = 1 \). From then on the pattern repeats with period 4: \( i^5 = i \), \( i^6 = -1 \), \( i^7 = -i \).

Finally, \( (a + bi)(a - bi) = \big(a^2 - b(-b)\big) + \big(a(-b) + ba\big)i = a^2 + b^2 \). This product is a real number, and it is **non-negative**. We will meet it again as \( \lvert z \rvert^2 \).
:::

The degenerate case deserves a look too. A real number \( a = a + 0i \) is a complex number whose imaginary part is zero, and the number \( 0 = 0 + 0i \) is the only complex number with both parts zero. Every computation with real numbers is also a computation in \( \nC \), by the second check above.

**A non-example by minimal change.** Change one sign in the multiplication rule: define \( (a, b) * (c, d) \coloneqq (ac + bd, \; ad + bc) \), which is what expanding gives if we pretend \( j^2 = +1 \) instead. Addition is unchanged, and this product is still commutative and has \( (1, 0) \) as a unit. But
\[
(1, 1) * (1, -1) = \big(1 - 1, \; -1 + 1\big) = (0, 0),
\]
so two non-zero elements multiply to zero. Division also breaks down: \( (1, 1) * (c, d) = (c + d, \; c + d) \) can never equal the unit \( (1, 0) \), because that would need \( c + d = 1 \) and \( c + d = 0 \) at once. So the non-zero element \( (1, 1) \) has no inverse. The single sign in \( ac - bd \) is what makes the complex numbers a number system in which we can divide, as we are about to see.

::: {.check}
Using the definition, compute \( i^{10} \) and \( (1 + i)^2 \). Is \( \operatorname{Im}(3 - 4i) \) equal to \( -4i \)?
:::

::: {.solution}
Since the powers of \( i \) repeat with period 4 and \( 10 = 8 + 2 \), we get \( i^{10} = i^2 = -1 \). Next, \( (1 + i)^2 = (1 - 1) + (1 + 1)i = 2i \). No: the imaginary part is the real number \( -4 \), not \( -4i \).
:::

**The usual rules of arithmetic hold.** Before computing freely, we should confirm that rearranging, regrouping and expanding brackets are legal in \( \nC \). The definition does not promise this; it has to be checked.

::: {#prp-complex-arithmetic-laws}
[Arithmetic Laws in \( \nC \)]

For all \( z, w, u \in \nC \):

::: {.enumerate options="label=(\alph*)"}
1. \( z + w = w + z \) and \( zw = wz \);
2. \( (z + w) + u = z + (w + u) \) and \( (zw)u = z(wu) \);
3. \( z(w + u) = zw + zu \);
4. \( z + 0 = z \), \( z \cdot 1 = z \), and \( z + (-z) = 0 \), where \( -(a + bi) \coloneqq (-a) + (-b)i \).
:::
:::

::: {.idea}
Every law reduces to the corresponding law for real numbers once both sides are written as pairs. Addition is coordinate by coordinate, so its laws are immediate. For multiplication the only real work is associativity: expand both sides and see that they produce the same four terms in each coordinate.
:::

::: {.proof}
Let \( z = a + bi \), \( w = c + di \) and \( u = e + fi \) with \( a, b, c, d, e, f \in \nR \). Since addition acts coordinate by coordinate, the laws for addition in (a), (b) and (d) follow from the same laws in \( \nR \), applied to each coordinate.

(a) By definition \( zw = (ac - bd) + (ad + bc)i \) and \( wz = (ca - db) + (cb + da)i \). These are equal because real multiplication and addition are commutative.

(b) Expanding with the definition twice gives
\[
(zw)u = \big((ac - bd)e - (ad + bc)f\big) + \big((ac - bd)f + (ad + bc)e\big)i
\]
and
\[
z(wu) = \big(a(ce - df) - b(cf + de)\big) + \big(a(cf + de) + b(ce - df)\big)i.
\]
Multiplying out, both real parts equal \( ace - adf - bcf - bde \) and both imaginary parts equal \( acf + ade + bce - bdf \). Hence \( (zw)u = z(wu) \).

(c) We have \( w + u = (c + e) + (d + f)i \), so
\[
\begin{aligned}
z(w + u)
&= \big(a(c + e) - b(d + f)\big) + \big(a(d + f) + b(c + e)\big)i \\
&= \big((ac - bd) + (ae - bf)\big) + \big((ad + bc) + (af + be)\big)i,
\end{aligned}
\]
which is \( zw + zu \) by the definitions of the product and the sum.

(d) With \( 1 = 1 + 0i \), we get \( z \cdot 1 = (a \cdot 1 - b \cdot 0) + (a \cdot 0 + b \cdot 1)i = a + bi = z \). Also \( z + (-z) = (a - a) + (b - b)i = 0 \). This proves the proposition.
:::

From now on we compute in \( \nC \) exactly as in \( \nR \): expand brackets, collect terms, and replace \( i^2 \) by \( -1 \). The proposition is what makes that habit legitimate.

## Conjugate and modulus

Division is still missing. To divide by \( 3 + 4i \) we want some number to multiply by that lands in the real numbers, where division is familiar. The computation \( (a + bi)(a - bi) = a^2 + b^2 \) in @exm-complex-arithmetic shows exactly which number does the job. Both ingredients get names.

*Conjugating reflects a point in the real axis; the modulus is its distance from the origin.*

::: {#def-conjugate-modulus}
[Conjugate and Modulus]

Let \( z = a + bi \in \nC \) with \( a, b \in \nR \). The **complex conjugate** of \( z \) is \( \conj{z} \coloneqq a - bi \). The **modulus** (or absolute value) of \( z \) is the real number \( \lvert z \rvert \coloneqq \sqrt{a^2 + b^2} \ge 0 \), the non-negative square root.
:::

In words: the conjugate keeps the real part and flips the sign of the imaginary part. The modulus is the length of the segment from \( 0 \) to the point \( (a, b) \), by Pythagoras. For a real number \( a = a + 0i \), we get \( \conj{a} = a \) and \( \lvert a \rvert = \sqrt{a^2} \), the usual absolute value, so the notation does not clash with its real meaning. For example, \( \conj{3 + 4i} = 3 - 4i \), \( \lvert 3 + 4i \rvert = 5 \), \( \conj{i} = -i \) and \( \lvert i \rvert = 1 \).

The following rules are used constantly, in this section and much later for complex inner products.

::: {#thm-conjugate-properties}
[Properties of Conjugation and Modulus]

For all \( z, w \in \nC \):

::: {.enumerate options="label=(\alph*)"}
1. \( \conj{z + w} = \conj{z} + \conj{w} \) and \( \conj{\conj{z}} = z \);
2. \( \conj{zw} = \conj{z} \, \conj{w} \);
3. \( z \conj{z} = \lvert z \rvert^2 \) and \( z + \conj{z} = 2 \operatorname{Re} z \);
4. \( \lvert zw \rvert = \lvert z \rvert \, \lvert w \rvert \) and \( \lvert \conj{z} \rvert = \lvert z \rvert \).
:::
:::

::: {.idea}
Parts (a)–(c) are direct computations with real and imaginary parts. For (d), expanding \( \lvert zw \rvert \) directly is legitimate but messy. It is cleaner to square: by (c) a squared modulus is a product with a conjugate, and (b) lets the conjugate split across the product.
:::

::: {.proof}
Let \( z = a + bi \) and \( w = c + di \) with \( a, b, c, d \in \nR \).

(a) We have \( \conj{z + w} = (a + c) - (b + d)i = (a - bi) + (c - di) = \conj{z} + \conj{w} \), and \( \conj{\conj{z}} = \conj{a - bi} = a + bi = z \).

(b) Since \( zw = (ac - bd) + (ad + bc)i \), we get \( \conj{zw} = (ac - bd) - (ad + bc)i \). On the other hand,
\[
\begin{aligned}
\conj{z} \, \conj{w}
&= (a - bi)(c - di) \\
&= \big(ac - (-b)(-d)\big) + \big(a(-d) + (-b)c\big)i \\
&= (ac - bd) - (ad + bc)i.
\end{aligned}
\]

(c) By the computation in @exm-complex-arithmetic, \( z \conj{z} = a^2 + b^2 = \lvert z \rvert^2 \). Also \( z + \conj{z} = 2a = 2 \operatorname{Re} z \).

(d) By (c), then (b), then @prp-complex-arithmetic-laws to reorder the four factors,
\[
\lvert zw \rvert^2 = (zw)\conj{zw} = z w \conj{z} \, \conj{w} = (z \conj{z})(w \conj{w}) = \lvert z \rvert^2 \lvert w \rvert^2.
\]
Both \( \lvert zw \rvert \) and \( \lvert z \rvert \lvert w \rvert \) are non-negative real numbers with the same square, so they are equal. Finally \( \lvert \conj{z} \rvert = \sqrt{a^2 + (-b)^2} = \lvert z \rvert \). This proves the theorem.
:::

The first payoff is division. If \( z \ne 0 \), then \( \lvert z \rvert^2 = a^2 + b^2 \) is a **strictly** positive real number, so we may divide by it.

::: {#prp-complex-inverse}
[Inverse of a Complex Number]

Let \( z \in \nC \) with \( z \ne 0 \). Then \( w \coloneqq \dfrac{1}{\lvert z \rvert^2} \, \conj{z} \) satisfies \( zw = 1 \). We write \( z^{-1} \) or \( \dfrac{1}{z} \) for this \( w \).
:::

::: {.proof}
Write \( z = a + bi \). Since \( z \ne 0 \), at least one of \( a, b \) is non-zero, so \( \lvert z \rvert^2 = a^2 + b^2 > 0 \). By @prp-complex-arithmetic-laws and @thm-conjugate-properties (c),
\[
zw = \frac{1}{\lvert z \rvert^2} \, (z \conj{z}) = \frac{1}{\lvert z \rvert^2} \, \lvert z \rvert^2 = 1,
\]
as claimed.
:::

In practice, "multiply top and bottom by the conjugate". For instance
\[
\begin{aligned}
\frac{1}{3 + 4i} &= \frac{3 - 4i}{(3 + 4i)(3 - 4i)} = \frac{3 - 4i}{25}, \\
\frac{5 + i}{1 - i} &= \frac{(5 + i)(1 + i)}{(1 - i)(1 + i)} = \frac{4 + 6i}{2} = 2 + 3i,
\end{aligned}
\]
which agrees with \( (2 + 3i)(1 - i) = 5 + i \) from @exm-complex-arithmetic. Only one inverse exists; this is a special case of a general fact about fields proved in the next section.

**The triangle inequality.** The modulus measures distance: \( \lvert z - w \rvert \) is the distance between the points \( z \) and \( w \) of the plane. The side of a triangle is never longer than the other two sides together, and this is the algebraic form of that fact.

::: {#thm-complex-triangle-inequality}
[Triangle Inequality]

For all \( z, w \in \nC \),
\[
\lvert z + w \rvert \le \lvert z \rvert + \lvert w \rvert.
\]
:::

::: {.idea}
Moduli are square roots, which are awkward to add. Both sides are non-negative, so it suffices to compare their squares. Expand \( \lvert z + w \rvert^2 \) using \( \lvert u \rvert^2 = u \conj{u} \): the cross terms combine into \( 2 \operatorname{Re}(z \conj{w}) \). A real part is never bigger than the modulus, and that single estimate finishes the proof.
:::

::: {.proof}
First, for any \( u = x + yi \) with \( x, y \in \nR \), we have \( \operatorname{Re} u = x \le \lvert x \rvert = \sqrt{x^2} \le \sqrt{x^2 + y^2} = \lvert u \rvert \), since the square root is increasing.

Now let \( z, w \in \nC \). By @thm-conjugate-properties (c), (a) and @prp-complex-arithmetic-laws,
\[
\lvert z + w \rvert^2 = (z + w)(\conj{z} + \conj{w}) = z \conj{z} + z \conj{w} + w \conj{z} + w \conj{w} = \lvert z \rvert^2 + \big(z \conj{w} + \conj{z \conj{w}}\big) + \lvert w \rvert^2,
\]
where we used \( w \conj{z} = \conj{z \conj{w}} \), which follows from @thm-conjugate-properties (b) and (a). By @thm-conjugate-properties (c) the bracket equals \( 2 \operatorname{Re}(z \conj{w}) \). Therefore, using \( \operatorname{Re} u \le \lvert u \rvert \) and then @thm-conjugate-properties (d),
\[
\lvert z + w \rvert^2 \le \lvert z \rvert^2 + 2 \lvert z \conj{w} \rvert + \lvert w \rvert^2 = \lvert z \rvert^2 + 2 \lvert z \rvert \lvert w \rvert + \lvert w \rvert^2 = \big(\lvert z \rvert + \lvert w \rvert\big)^2.
\]
Both \( \lvert z + w \rvert \) and \( \lvert z \rvert + \lvert w \rvert \) are non-negative, so taking square roots preserves the inequality. This proves the triangle inequality.
:::

The route "square, expand, bound the cross term" is worth remembering: it is exactly the route we will take for norms in inner product spaces. The inequality is often strict. For \( z = 1 \) and \( w = -1 \), the left side is \( 0 \) and the right side is \( 2 \).

## Two things that do not carry over from the reals

Complex numbers obey the rules of arithmetic, but not every habit from the real line survives.

The first loss is order. On \( \nR \) we use two facts about positivity: for every \( x \), exactly one of \( x > 0 \), \( x = 0 \), \( -x > 0 \) holds, and sums and products of positive numbers are positive. Suppose some relation \( > \) on \( \nC \) had both properties. Since \( i \ne 0 \), either \( i > 0 \) or \( -i > 0 \), and in both cases the product rule gives \( i^2 = (-i)^2 = -1 > 0 \). The same argument applied to \( 1 \ne 0 \) gives \( 1 = 1^2 = (-1)^2 > 0 \). Then both \( 1 \) and \( -1 \) are positive, so their sum \( 0 \) is positive, which contradicts "exactly one".

::: {.warning}
There is no ordering on \( \nC \) compatible with addition and multiplication, so an inequality such as \( z < w \) between complex numbers means nothing. Inequalities in this book compare **real** numbers: moduli \( \lvert z \rvert \), real parts, or quantities known to be real. Writing \( i > 0 \) leads, as shown above, to \( 0 > 0 \).
:::

The second loss is the square-root rule \( \sqrt{x}\sqrt{y} = \sqrt{xy} \), which on \( \nR \) is only claimed for \( x, y \ge 0 \).

::: {.warning}
Every non-zero complex number has **two** square roots, and no choice of "the" square root makes \( \sqrt{z}\sqrt{w} = \sqrt{zw} \) true for all \( z, w \). With \( \sqrt{-1} = i \): \( \sqrt{-1} \cdot \sqrt{-1} = i^2 = -1 \), but \( \sqrt{(-1)(-1)} = \sqrt{1} = 1 \). Avoid the symbol \( \sqrt{z} \) for non-real \( z \); say "a square root of \( z \)" and solve \( w^2 = z \) instead.
:::

Solving \( w^2 = z \) is a finite computation, done by comparing real and imaginary parts.

::: {#exm-complex-square-root}
[Square Roots of \( 5 - 12i \)]

Find all \( w \in \nC \) with \( w^2 = 5 - 12i \).
:::

::: {.solution}
Write \( w = x + yi \) with \( x, y \in \nR \). Then \( w^2 = (x^2 - y^2) + 2xyi \), so comparing real and imaginary parts, \( w^2 = 5 - 12i \) holds exactly when
\[
x^2 - y^2 = 5 \quad \text{and} \quad xy = -6.
\]
Taking moduli in \( w^2 = 5 - 12i \) and using @thm-conjugate-properties (d) gives \( \lvert w \rvert^2 = \lvert 5 - 12i \rvert = \sqrt{25 + 144} = 13 \), that is \( x^2 + y^2 = 13 \). Adding and subtracting this and the first equation gives \( x^2 = 9 \) and \( y^2 = 4 \), so \( x = \pm 3 \) and \( y = \pm 2 \). The condition \( xy = -6 < 0 \) says \( x \) and \( y \) have opposite signs. Hence \( w = 3 - 2i \) or \( w = -3 + 2i \). Both work: \( (3 - 2i)^2 = 9 - 12i + 4i^2 = 5 - 12i \), and \( (-3 + 2i)^2 = (3 - 2i)^2 \).
:::

## Polar form: multiplication rotates and scales

Addition in \( \nC \) is the familiar addition of arrows in the plane. Multiplication has a geometric meaning too, and it only becomes visible when we describe a point by its distance from \( 0 \) and its angle, instead of by its coordinates.

Let \( z \ne 0 \) and put \( r = \lvert z \rvert > 0 \). The number \( z / r \) has modulus \( 1 \) by @thm-conjugate-properties (d), so it lies on the unit circle. From trigonometry, every point \( (x, y) \) with \( x^2 + y^2 = 1 \) is \( (\cos\theta, \sin\theta) \) for some real \( \theta \). We abbreviate
\[
e^{i\theta} \coloneqq \cos\theta + i\sin\theta \qquad (\theta \in \nR),
\]
and then every non-zero complex number can be written as
\[
z = r e^{i\theta}, \qquad r = \lvert z \rvert > 0, \quad \theta \in \nR.
\]
This is the **polar form** of \( z \), and \( \theta \) is **an** argument of \( z \). The word "an" matters: \( \theta \) and \( \theta + 2\pi k \) give the same point for every integer \( k \). Conversely, if \( r e^{i\theta} = s e^{i\varphi} \) with \( r, s > 0 \), then taking moduli gives \( r = s \) (as \( \lvert e^{i\theta} \rvert = \sqrt{\cos^2\theta + \sin^2\theta} = 1 \)). Comparing real and imaginary parts then gives \( \cos\theta = \cos\varphi \) and \( \sin\theta = \sin\varphi \), which from trigonometry means \( \theta - \varphi \) is an integer multiple of \( 2\pi \).

For now \( e^{i\theta} \) is only a name for \( \cos\theta + i\sin\theta \). The next result is the reason the name is a good one: these numbers multiply the way exponentials do.

::: {#thm-polar-multiplication}
[Multiplication in Polar Form]

For all \( \theta, \varphi \in \nR \),
\[
e^{i\theta} e^{i\varphi} = e^{i(\theta + \varphi)}.
\]
Consequently, if \( z = r e^{i\theta} \) and \( w = s e^{i\varphi} \) with \( r, s > 0 \), then \( zw = rs \, e^{i(\theta + \varphi)} \).
:::

::: {.proof}
By the multiplication rule,
\[
\begin{aligned}
e^{i\theta} e^{i\varphi}
&= (\cos\theta\cos\varphi - \sin\theta\sin\varphi) + (\cos\theta\sin\varphi + \sin\theta\cos\varphi)i \\
&= \cos(\theta + \varphi) + i \sin(\theta + \varphi),
\end{aligned}
\]
where the last equality uses the addition formulas for cosine and sine. This is \( e^{i(\theta + \varphi)} \). For the second statement, \( zw = (rs)(e^{i\theta} e^{i\varphi}) \) by @prp-complex-arithmetic-laws, and the first statement finishes the proof.
:::

In words: **to multiply two complex numbers, multiply their moduli and add their arguments**. Multiplying by a fixed \( w = s e^{i\varphi} \) is therefore a rotation of the plane about \( 0 \) by the angle \( \varphi \), combined with a stretch by the factor \( s \). The picture shows \( z \), \( w \) and \( zw \) for \( \lvert z \rvert = 1.5 \), \( \lvert w \rvert = 1.2 \) and arguments \( 20^\circ \) and \( 50^\circ \).

\begin{center}
\begin{tikzpicture}[scale=2]
    \draw[->] (-0.3,0) -- (2.2,0) node[right] {$\operatorname{Re}$};
    \draw[->] (0,-0.3) -- (0,2.1) node[above] {$\operatorname{Im}$};
    \draw[dashed] (1,0) arc (0:90:1);
    \draw[thick,->] (0,0) -- (20:1.5) node[right] {$z$};
    \draw[thick,->] (0,0) -- (50:1.2) node[below right] {$w$};
    \draw[very thick,->] (0,0) -- (70:1.8) node[above] {$zw$};
    \draw (0.55,0) arc (0:20:0.55);
    \node at (10:0.8) {\small $20^\circ$};
    \draw (20:1.3) arc (20:70:1.3);
    \node at (45:1.5) {\small $50^\circ$};
    \node[below] at (1,0) {\small $1$};
\end{tikzpicture}
\end{center}

The arrow for \( zw \) has length \( 1.5 \times 1.2 = 1.8 \) and makes the angle \( 20^\circ + 50^\circ = 70^\circ \) with the positive real axis: it is the arrow for \( z \), turned by \( w \)'s angle and stretched by \( w \)'s length. The small arc marks the argument of \( z \), the large arc marks the extra turn by the argument of \( w \), and the dashed arc is the unit circle, where the numbers \( e^{i\theta} \) live.

Two special cases are worth isolating. Multiplying by \( i = e^{i\pi/2} \) is a quarter turn counterclockwise, which explains \( i^2 = -1 \): two quarter turns send \( 1 \) to \( -1 \). And \( e^{i\theta} e^{-i\theta} = e^{0} = 1 \), so \( (e^{i\theta})^{-1} = e^{-i\theta} = \conj{e^{i\theta}} \).

Repeating @thm-polar-multiplication gives powers.

::: {#thm-de-moivre}
[De Moivre's Formula]

For every \( \theta \in \nR \) and every \( n \in \nN \),
\[
\big(e^{i\theta}\big)^n = e^{in\theta}, \quad \text{that is,} \quad (\cos\theta + i\sin\theta)^n = \cos n\theta + i \sin n\theta.
\]
Consequently \( (r e^{i\theta})^n = r^n e^{in\theta} \) for every real \( r > 0 \).
:::

::: {.proof}
We use induction on \( n \) (@thm-induction). For \( n = 0 \), both sides equal \( 1 \), since \( e^{i \cdot 0} = \cos 0 + i \sin 0 = 1 \). Suppose \( (e^{i\theta})^n = e^{in\theta} \) for some \( n \in \nN \). Then \( (e^{i\theta})^{n+1} = (e^{i\theta})^n e^{i\theta} = e^{in\theta} e^{i\theta} = e^{i(n+1)\theta} \) by the induction hypothesis and @thm-polar-multiplication. The consequence follows by the same induction, since \( (r e^{i\theta})^{n+1} = (r^n e^{in\theta})(r e^{i\theta}) = r^{n+1} e^{i(n+1)\theta} \) by @thm-polar-multiplication.
:::

Powers that are painful to expand become one line in polar form.

::: {#exm-polar-power}
[A Power via Polar Form]

Compute \( (\sqrt{3} + i)^6 \).
:::

::: {.solution}
The modulus is \( \lvert \sqrt{3} + i \rvert = \sqrt{3 + 1} = 2 \), and \( \sqrt{3} + i = 2\big(\tfrac{\sqrt{3}}{2} + \tfrac12 i\big) = 2\big(\cos\tfrac{\pi}{6} + i\sin\tfrac{\pi}{6}\big) = 2e^{i\pi/6} \). By @thm-de-moivre,
\[
(\sqrt{3} + i)^6 = 2^6 e^{i \cdot 6\pi/6} = 64 (\cos\pi + i \sin\pi) = -64.
\]
Expanding \( (\sqrt{3} + i)^6 \) with the binomial theorem gives the same answer after seven terms and some cancellation.
:::

::: {.check}
Use polar form to compute \( (1 + i)^8 \).
:::

::: {.solution}
We have \( \lvert 1 + i \rvert = \sqrt{2} \) and \( 1 + i = \sqrt{2}\big(\tfrac{1}{\sqrt 2} + \tfrac{1}{\sqrt 2} i\big) = \sqrt{2} \, e^{i\pi/4} \). By @thm-de-moivre, \( (1 + i)^8 = (\sqrt{2})^8 e^{i \cdot 8\pi/4} = 16 e^{2\pi i} = 16 \). As a cross-check, \( (1 + i)^2 = 2i \), so \( (1 + i)^8 = (2i)^4 = 16 i^4 = 16 \).
:::

## Roots of unity

Polar form also turns the equation \( z^n = c \) into a question about angles. The most important case is \( c = 1 \).

::: {#exm-roots-of-unity}
[Roots of Unity]

Let \( n \ge 1 \) be an integer. Find all \( z \in \nC \) with \( z^n = 1 \), and draw them for \( n = 6 \).
:::

::: {.solution}
Since \( 0^n = 0 \ne 1 \), every solution is non-zero, so we may write \( z = r e^{i\theta} \) with \( r > 0 \). By @thm-de-moivre, \( z^n = r^n e^{in\theta} \), and \( 1 = 1 \cdot e^{i0} \). By uniqueness of the polar form up to multiples of \( 2\pi \), \( z^n = 1 \) holds exactly when \( r^n = 1 \) and \( n\theta = 2\pi k \) for some integer \( k \). Since \( r > 0 \) is real, \( r^n = 1 \) forces \( r = 1 \). Hence the solutions are
\[
e^{2\pi i k / n}, \qquad k \in \nZ.
\]
Put \( \omega \coloneqq e^{2\pi i/n} \). By @thm-de-moivre, \( e^{2\pi i k/n} = \omega^k \) for \( k \ge 0 \). Two integers \( k, l \) give the same number exactly when \( 2\pi(k - l)/n \) is a multiple of \( 2\pi \), that is, when \( n \) divides \( k - l \). So there are exactly \( n \) distinct solutions,
\[
1, \; \omega, \; \omega^2, \; \dots, \; \omega^{n-1},
\]
the **\( n \)-th roots of unity**. They sit on the unit circle at equally spaced angles. For \( n \ge 3 \) they are the corners of a regular polygon with \( n \) corners, one of them at \( 1 \); for \( n = 2 \) they are \( \pm 1 \).

For \( n = 6 \), the angles are multiples of \( 60^\circ \), and the roots are
\[
1, \quad \tfrac12 + \tfrac{\sqrt3}{2}i, \quad -\tfrac12 + \tfrac{\sqrt3}{2}i, \quad -1, \quad -\tfrac12 - \tfrac{\sqrt3}{2}i, \quad \tfrac12 - \tfrac{\sqrt3}{2}i.
\]

\begin{center}
\begin{tikzpicture}[scale=1.6]
    \draw[->] (-1.5,0) -- (1.6,0) node[right] {$\operatorname{Re}$};
    \draw[->] (0,-1.4) -- (0,1.5) node[above] {$\operatorname{Im}$};
    \draw[dashed] (0,0) circle (1);
    \draw[thick] (0:1) -- (60:1) -- (120:1) -- (180:1) -- (240:1) -- (300:1) -- cycle;
    \foreach \k in {0,...,5} { \fill (\k*60:1) circle (1.2pt); }
    \node[below right] at (0:1) {$1$};
    \node[above right] at (60:1) {$\omega$};
    \node[above left] at (120:1) {$\omega^2$};
    \node[below left] at (180:1) {$\omega^3 = -1$};
    \node[below left] at (240:1) {$\omega^4$};
    \node[below right] at (300:1) {$\omega^5$};
\end{tikzpicture}
\end{center}

The six roots sum to \( 0 \): since \( \omega^3 = e^{i\pi} = -1 \), we have \( \omega^{k+3} = -\omega^k \), so the roots cancel in the opposite pairs \( \{1, \omega^3\} \), \( \{\omega, \omega^4\} \), \( \{\omega^2, \omega^5\} \). In the picture, the hexagon is symmetric about its center \( 0 \). The sum of the \( n \)-th roots of unity is \( 0 \) for every \( n \ge 2 \); see @exr-complex-numbers-c2.
:::

## The Fundamental Theorem of Algebra

We built \( \nC \) so that one polynomial equation, \( z^2 + 1 = 0 \), has a solution. It turns out that nothing more ever needs to be added: every polynomial equation already has a solution in \( \nC \). Here a **complex polynomial of degree \( n \)** means an expression \( a_n z^n + \dots + a_1 z + a_0 \) with \( a_0, \dots, a_n \in \nC \) and \( a_n \ne 0 \); polynomials are studied properly in a later section of this chapter.

::: {#thm-fta-statement}
[Fundamental Theorem of Algebra, Statement]

Let \( n \ge 1 \) and let \( a_0, a_1, \dots, a_n \in \nC \) with \( a_n \ne 0 \). Then there exists \( z \in \nC \) with
\[
a_n z^n + a_{n-1} z^{n-1} + \dots + a_1 z + a_0 = 0.
\]
:::

We do not prove this theorem here. Its proof needs tools we have not built, and it is proved in Chapter 5. Nothing in Chapters 0–4 depends on it.

::: {.remark}
Combined with division of polynomials (also in Chapter 5), the theorem gives the form in which it is usually applied: every complex polynomial of degree \( n \ge 1 \) **splits into linear factors**, \( a_n z^n + \dots + a_0 = a_n (z - z_1)(z - z_2) \cdots (z - z_n) \) for some \( z_1, \dots, z_n \in \nC \), not necessarily distinct. For linear algebra this is the fact that every complex square matrix has an eigenvalue, the starting point of the theory of canonical forms.
:::

One companion fact needs no heavy machinery. If the coefficients \( a_0, \dots, a_n \) are **real** and \( p(z) = a_n z^n + \dots + a_0 \) has \( p(z_0) = 0 \), then applying @thm-conjugate-properties (a) and (b) term by term, and \( \conj{a_k} = a_k \), gives \( p(\conj{z_0}) = \conj{p(z_0)} = \conj{0} = 0 \). So the non-real roots of a real polynomial come in conjugate pairs. For example, \( z^2 - 2z + 5 \) has the roots \( 1 + 2i \) and \( 1 - 2i \): indeed \( (1 + 2i)^2 - 2(1 + 2i) + 5 = (-3 + 4i) - (2 + 4i) + 5 = 0 \).

## Exercises

### A. Check your understanding

::: {#exr-complex-numbers-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the complex conjugate \( \conj{z} \) and the modulus \( \lvert z \rvert \) of \( z = a + bi \), where \( a, b \in \nR \).
2. State the triangle inequality for complex numbers.
3. True or false: \( \lvert z + w \rvert = \lvert z \rvert + \lvert w \rvert \) for all \( z, w \in \nC \). Justify your answer.
4. True or false: \( z \conj{z} \) is a non-negative real number for every \( z \in \nC \). Justify your answer.
5. True or false: if \( z, w \in \nC \) and \( z^2 = w^2 \), then \( z = w \). Justify your answer.
6. State the Fundamental Theorem of Algebra.
:::
:::

::: {.solution}
(a) See @def-conjugate-modulus: \( \conj{z} = a - bi \) and \( \lvert z \rvert = \sqrt{a^2 + b^2} \ge 0 \).

(b) See @thm-complex-triangle-inequality: \( \lvert z + w \rvert \le \lvert z \rvert + \lvert w \rvert \) for all \( z, w \in \nC \).

(c) False. For \( z = 1 \) and \( w = -1 \), \( \lvert z + w \rvert = 0 \) but \( \lvert z \rvert + \lvert w \rvert = 2 \).

(d) True. By @thm-conjugate-properties (c), \( z \conj{z} = \lvert z \rvert^2 = a^2 + b^2 \), which is real and non-negative.

(e) False. For \( z = 1 \) and \( w = -1 \), \( z^2 = w^2 = 1 \) but \( z \ne w \). (What is true is that \( z^2 = w^2 \) implies \( z = w \) or \( z = -w \).)

(f) See @thm-fta-statement: every complex polynomial \( a_n z^n + \dots + a_0 \) with \( n \ge 1 \) and \( a_n \ne 0 \) has a root in \( \nC \).
:::

### B. Practice

::: {#exr-complex-numbers-b1}
[B1: Arithmetic]

Write each of the following in the form \( a + bi \) with \( a, b \in \nR \), or as a real number where indicated.

::: {.enumerate options="label=(\alph*)"}
1. \( (3 - 2i)(4 + i) \).
2. \( \dfrac{1 + 2i}{2 - i} \).
3. \( \lvert (3 + 4i)(5 - 12i) \rvert \), without expanding the product.
4. \( \operatorname{Re}\dfrac{1}{1 + i} \) and \( \operatorname{Im}\dfrac{1}{1 + i} \).
:::
:::

::: {.solution}
(a) Expanding and using \( i^2 = -1 \): \( (3 - 2i)(4 + i) = 12 + 3i - 8i - 2i^2 = 14 - 5i \).

(b) Multiplying top and bottom by \( \conj{2 - i} = 2 + i \) (@prp-complex-inverse),
\[
\frac{1 + 2i}{2 - i} = \frac{(1 + 2i)(2 + i)}{(2 - i)(2 + i)} = \frac{2 + i + 4i + 2i^2}{4 + 1} = \frac{5i}{5} = i.
\]

(c) By @thm-conjugate-properties (d), \( \lvert (3 + 4i)(5 - 12i) \rvert = \lvert 3 + 4i \rvert \, \lvert 5 - 12i \rvert = \sqrt{25} \cdot \sqrt{169} = 5 \cdot 13 = 65 \).

(d) By @prp-complex-inverse, \( \dfrac{1}{1 + i} = \dfrac{1 - i}{\lvert 1 + i \rvert^2} = \dfrac{1 - i}{2} = \dfrac12 - \dfrac12 i \). Hence the real part is \( \tfrac12 \) and the imaginary part is \( -\tfrac12 \).
:::

::: {#exr-complex-numbers-b2}
[B2: A Square Root]

::: {.enumerate options="label=(\alph*)"}
1. Find all \( w \in \nC \) with \( w^2 = -3 + 4i \).
2. Hence solve \( z^2 + 2z + 4 - 4i = 0 \).
:::

*Hint: for (b), complete the square.*
:::

::: {.solution}
(a) Write \( w = x + yi \) with \( x, y \in \nR \). Comparing real and imaginary parts in \( (x^2 - y^2) + 2xyi = -3 + 4i \) gives \( x^2 - y^2 = -3 \) and \( xy = 2 \). Taking moduli, by @thm-conjugate-properties (d), \( x^2 + y^2 = \lvert w \rvert^2 = \lvert -3 + 4i \rvert = 5 \). Adding and subtracting, \( x^2 = 1 \) and \( y^2 = 4 \). Since \( xy = 2 > 0 \), \( x \) and \( y \) have the same sign. Therefore \( w = 1 + 2i \) or \( w = -1 - 2i \). Check: \( (1 + 2i)^2 = 1 + 4i - 4 = -3 + 4i \), and \( (-1 - 2i)^2 = (1 + 2i)^2 \).

(b) Completing the square, \( z^2 + 2z + 4 - 4i = (z + 1)^2 - 1 + 4 - 4i = (z + 1)^2 - (-3 + 4i) \). So the equation holds exactly when \( (z + 1)^2 = -3 + 4i \). By (a), this means \( z + 1 = 1 + 2i \) or \( z + 1 = -1 - 2i \). Hence the solutions are \( z = 2i \) and \( z = -2 - 2i \).
:::

::: {#exr-complex-numbers-b3}
[B3]

Let \( z \in \nC \) with \( z \ne 0 \). Prove that \( \dfrac{1}{z} = \conj{z} \) if and only if \( \lvert z \rvert = 1 \).
:::

::: {.solution}
By @prp-complex-inverse, \( \dfrac{1}{z} = \dfrac{1}{\lvert z \rvert^2} \conj{z} \).

\( (\Leftarrow) \) Suppose \( \lvert z \rvert = 1 \). Then \( \dfrac{1}{z} = \dfrac{1}{1} \conj{z} = \conj{z} \).

\( (\Rightarrow) \) Suppose \( \dfrac{1}{z} = \conj{z} \). Then \( \dfrac{1}{\lvert z \rvert^2} \conj{z} = \conj{z} \). Since \( z \ne 0 \), also \( \conj{z} \ne 0 \), so multiplying both sides by \( (\conj{z})^{-1} \) gives \( \dfrac{1}{\lvert z \rvert^2} = 1 \), that is, \( \lvert z \rvert^2 = 1 \). As \( \lvert z \rvert \ge 0 \), this forces \( \lvert z \rvert = 1 \). This proves the equivalence.
:::

::: {#exr-complex-numbers-b4}
[B4: Polar Form]

::: {.enumerate options="label=(\alph*)"}
1. Compute \( (1 - \sqrt{3}\, i)^6 \).
2. Find all \( z \in \nC \) with \( z^3 = -8i \), in the form \( a + bi \).
:::
:::

::: {.solution}
(a) We have \( \lvert 1 - \sqrt3 i \rvert = \sqrt{1 + 3} = 2 \) and \( 1 - \sqrt3 i = 2\big(\cos(-\tfrac{\pi}{3}) + i \sin(-\tfrac{\pi}{3})\big) = 2e^{-i\pi/3} \). By @thm-de-moivre, \( (1 - \sqrt3 i)^6 = 64 e^{-2\pi i} = 64(\cos 2\pi - i \sin 2\pi) = 64 \).

(b) Since \( 0^3 \ne -8i \), write \( z = r e^{i\theta} \) with \( r > 0 \). Also \( -8i = 8 e^{-i\pi/2} \). By @thm-de-moivre, \( z^3 = r^3 e^{3i\theta} \). By uniqueness of polar form up to multiples of \( 2\pi \), \( z^3 = -8i \) holds exactly when \( r^3 = 8 \) and \( 3\theta = -\tfrac{\pi}{2} + 2\pi k \) for some integer \( k \). Therefore \( r = 2 \) and \( \theta = -\tfrac{\pi}{6} + \tfrac{2\pi k}{3} \). The values \( k = 0, 1, 2 \) give \( \theta = -\tfrac{\pi}{6}, \tfrac{\pi}{2}, \tfrac{7\pi}{6} \), and every other \( k \) differs from one of these by a multiple of \( 3 \), which changes \( \theta \) by a multiple of \( 2\pi \). Hence the solutions are
\[
2e^{-i\pi/6} = \sqrt3 - i, \qquad 2e^{i\pi/2} = 2i, \qquad 2e^{7i\pi/6} = -\sqrt3 - i.
\]
Check: \( (2i)^3 = 8i^3 = -8i \).
:::

### C. Going deeper

::: {#exr-complex-numbers-c1}
[C1: Reverse Triangle Inequality]

Prove that \( \big\lvert \lvert z \rvert - \lvert w \rvert \big\rvert \le \lvert z - w \rvert \) for all \( z, w \in \nC \).

*Hint: write \( z = (z - w) + w \).*
:::

::: {.solution}
Let \( z, w \in \nC \). Since \( z = (z - w) + w \), the triangle inequality (@thm-complex-triangle-inequality) gives \( \lvert z \rvert \le \lvert z - w \rvert + \lvert w \rvert \), so \( \lvert z \rvert - \lvert w \rvert \le \lvert z - w \rvert \). Swapping the roles of \( z \) and \( w \) gives \( \lvert w \rvert - \lvert z \rvert \le \lvert w - z \rvert \). Moreover \( \lvert w - z \rvert = \lvert (-1)(z - w) \rvert = \lvert -1 \rvert \, \lvert z - w \rvert = \lvert z - w \rvert \) by @thm-conjugate-properties (d). The real number \( \big\lvert \lvert z \rvert - \lvert w \rvert \big\rvert \) equals one of \( \lvert z \rvert - \lvert w \rvert \) and \( \lvert w \rvert - \lvert z \rvert \), and both are at most \( \lvert z - w \rvert \). This proves the inequality.
:::

::: {#exr-complex-numbers-c2}
[C2: Roots of Unity Sum to Zero]

Let \( n \ge 2 \) and \( \omega = e^{2\pi i/n} \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( 1 + \omega + \omega^2 + \dots + \omega^{n-1} = 0 \).
2. Deduce that \( \displaystyle\sum_{k=0}^{n-1} \cos\frac{2\pi k}{n} = 0 \) and \( \displaystyle\sum_{k=0}^{n-1} \sin\frac{2\pi k}{n} = 0 \).
:::

*Hint: compare \( S \) with \( \omega S \), where \( S \) is the sum in (a).*
:::

::: {.solution}
(a) Let \( S = 1 + \omega + \dots + \omega^{n-1} \). By @thm-de-moivre, \( \omega^n = e^{2\pi i} = 1 \). Therefore
\[
\omega S = \omega + \omega^2 + \dots + \omega^{n-1} + \omega^n = \omega + \omega^2 + \dots + \omega^{n-1} + 1 = S,
\]
so \( (\omega - 1)S = 0 \). Since \( n \ge 2 \), we have \( 0 < 2\pi/n \le \pi \), so \( \operatorname{Re}\omega = \cos(2\pi/n) < 1 \) and \( \omega \ne 1 \). Hence \( \omega - 1 \ne 0 \), and multiplying \( (\omega - 1)S = 0 \) by \( (\omega - 1)^{-1} \) (@prp-complex-inverse) gives \( S = 0 \).

(b) By @thm-de-moivre, \( \omega^k = \cos\frac{2\pi k}{n} + i \sin\frac{2\pi k}{n} \) for each \( k \). Since addition in \( \nC \) is coordinate by coordinate, the real part of \( S \) is \( \sum_{k=0}^{n-1} \cos\frac{2\pi k}{n} \) and the imaginary part is \( \sum_{k=0}^{n-1} \sin\frac{2\pi k}{n} \). By (a), \( S = 0 \), so both sums are \( 0 \).
:::

::: {#exr-complex-numbers-c3}
[C3: Symmetries of \( \nC \) Fixing \( \nR \)]

Let \( \sigma \colon \nC \to \nC \) be a function with \( \sigma(z + w) = \sigma(z) + \sigma(w) \) and \( \sigma(zw) = \sigma(z)\sigma(w) \) for all \( z, w \in \nC \), and \( \sigma(a) = a \) for every \( a \in \nR \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \sigma(i)^2 = -1 \).
2. Prove that the only complex numbers \( u \) with \( u^2 = -1 \) are \( i \) and \( -i \).
3. Deduce that either \( \sigma(z) = z \) for every \( z \in \nC \), or \( \sigma(z) = \conj{z} \) for every \( z \in \nC \).
4. Show that \( z \mapsto \conj{z} \) does satisfy all three conditions on \( \sigma \).
:::

*Hint: for (b), write \( u = x + yi \) and compare real and imaginary parts.*
:::

::: {.solution}
(a) Since \( \sigma \) respects products and fixes the real number \( -1 \), we get \( \sigma(i)^2 = \sigma(i \cdot i) = \sigma(-1) = -1 \).

(b) Let \( u = x + yi \) with \( x, y \in \nR \) and \( u^2 = -1 \). Comparing real and imaginary parts in \( (x^2 - y^2) + 2xyi = -1 \) gives \( x^2 - y^2 = -1 \) and \( xy = 0 \). If \( y = 0 \), then \( x^2 = -1 \), which is impossible for real \( x \). Hence \( x = 0 \), so \( y^2 = 1 \) and \( y = \pm 1 \). Therefore \( u = i \) or \( u = -i \), and both satisfy \( u^2 = -1 \).

(c) By (a) and (b), \( \sigma(i) = i \) or \( \sigma(i) = -i \). Let \( z = a + bi \) with \( a, b \in \nR \). Since \( \sigma \) respects sums and products and fixes \( a \) and \( b \),
\[
\sigma(z) = \sigma(a) + \sigma(b)\sigma(i) = a + b\,\sigma(i).
\]
If \( \sigma(i) = i \), this gives \( \sigma(z) = z \) for every \( z \). If \( \sigma(i) = -i \), it gives \( \sigma(z) = a - bi = \conj{z} \) for every \( z \).

(d) By @thm-conjugate-properties (a) and (b), conjugation respects sums and products. For \( a \in \nR \), \( \conj{a} = \conj{a + 0i} = a - 0i = a \). So conjugation satisfies all three conditions.
:::
