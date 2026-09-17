# Changing the Field

Every vector space comes with its field, and we have already seen that the field matters: \( \dim_\nC \nC = 1 \) but \( \dim_\nR \nC = 2 \) (@exm-dimensions). This section explains the pattern behind that example. Shrinking the field multiplies the dimension by a fixed factor, the **tower law**. Going the other way, every real vector space can be enlarged to a complex one, its **complexification**, without changing the dimension. Both moves are used later, most of all when real matrices need complex eigenvalues.

## Restricting the scalars

Start with the standard example. The space \( \nC^2 \) over \( \nC \) has the basis \( (\e_1, \e_2) \), so its dimension is \( 2 \). But nothing stops us from multiplying vectors of \( \nC^2 \) only by **real** numbers. The addition is the same, and the axioms still hold, because they hold for all complex scalars. So \( \nC^2 \) is also a vector space over \( \nR \). What is its dimension now?

::: {#exm-c2-over-r}
[\( \nC^2 \) as a Real Vector Space]

Show that \( (\e_1, i\e_1, \e_2, i\e_2) \) is a basis of \( \nC^2 \) over \( \nR \), and write \( (1 + 2i, 3 - i) \) in it.
:::

::: {.solution}
*Spanning.* Let \( (z_1, z_2) \in \nC^2 \) and write \( z_k = a_k + b_ki \) with \( a_k, b_k \in \nR \). Then
\[
(z_1, z_2) = a_1\e_1 + b_1(i\e_1) + a_2\e_2 + b_2(i\e_2),
\]
a combination with **real** coefficients. For example, \( (1 + 2i, 3 - i) = 1\e_1 + 2(i\e_1) + 3\e_2 + (-1)(i\e_2) \).

*Independence.* Let \( a_1, b_1, a_2, b_2 \in \nR \) with \( a_1\e_1 + b_1(i\e_1) + a_2\e_2 + b_2(i\e_2) = \0 \). The left side is \( (a_1 + b_1i, \; a_2 + b_2i) \). Each entry is \( 0 \), and comparing real and imaginary parts (@def-complex-numbers) gives \( a_1 = b_1 = a_2 = b_2 = 0 \).

Hence \( \dim_\nR \nC^2 = 4 = 2 \dim_\nC \nC^2 \).
:::

The general setting has a big field \( L \), a smaller field \( K \) inside it, and a vector space over \( L \).

::: {#def-restriction-of-scalars}
[Subfield, Restriction of Scalars, Degree]

Let \( L \) be a field. A **subfield** of \( L \) is a subset \( K \subseteq L \) that contains \( 0 \) and \( 1 \) and is closed under addition, multiplication, negatives, and inverses of **non-zero** elements.

Let \( K \) be a subfield of \( L \), and let \( V \) be a vector space over \( L \). Keeping the addition of \( V \) and using scalar multiplication only for scalars in \( K \) makes \( V \) a vector space **over \( K \)**. We say \( V \) is obtained by **restriction of scalars**.

In particular \( L \) itself, a vector space over \( L \), is a vector space over \( K \). If it is finite-dimensional, its dimension is the **degree** \( [L : K] \coloneqq \dim_K L \).
:::

In words: a subfield is a field sitting inside \( L \) with the same operations. Restriction of scalars forgets how to multiply by elements of \( L \) outside \( K \).

There are two things to check. First, \( K \) with the operations of \( L \) is a field. Closure makes the operations land in \( K \), the elements \( 0, 1 \), negatives and inverses are in \( K \) by assumption, and the remaining axioms are identities that hold for all elements of \( L \), so in particular for those of \( K \). Second, \( V \) over \( K \) is a vector space. Scalar multiplication \( K \times V \to V \) lands in \( V \), and each axiom of @def-vector-space holds **for all** scalars in \( L \), so in particular for all scalars in \( K \).

We always write \( \dim_K V \) or \( \dim_L V \) when both fields are in play.

::: {#exm-field-degrees}
[Degrees of Some Fields]

Find \( [\nC : \nR] \), \( [\nQ(\sqrt2) : \nQ] \) and \( [K : K] \) for any field \( K \). Is \( [\nR : \nQ] \) defined?
:::

::: {.solution}
*\( [\nC : \nR] = 2 \).* Every \( z \in \nC \) is \( a \cdot 1 + b \cdot i \) with \( a, b \in \nR \), and \( a + bi = 0 \) forces \( a = b = 0 \) by @def-complex-numbers. So \( (1, i) \) is a basis of \( \nC \) over \( \nR \).

*\( [\nQ(\sqrt2) : \nQ] = 2 \).* The set \( \nQ(\sqrt2) = \{ a + b\sqrt2 : a, b \in \nQ \} \) is a subfield of \( \nR \) by @exm-q-sqrt2-field. The list \( (1, \sqrt2) \) spans it over \( \nQ \) by definition. For independence, let \( a + b\sqrt2 = 0 \) with \( a, b \in \nQ \). If \( b \ne 0 \), then \( \sqrt2 = -a/b \in \nQ \), contradicting @thm-sqrt2-irrational. So \( b = 0 \), and then \( a = 0 \).

*\( [K : K] = 1 \).* The list \( (1) \) is a basis of \( K \) over \( K \): every \( a \) equals \( a \cdot 1 \), and \( a \cdot 1 = 0 \) forces \( a = 0 \). This degenerate case says that restricting to the same field changes nothing.

*\( [\nR : \nQ] \)* is not defined, because \( \nR \) is not finite-dimensional over \( \nQ \) (@thm-reals-infinite-dimensional-over-rationals).
:::

Restriction only goes **down**. The set \( \nR \) with the operations of \( \nC \) is **not** a vector space over \( \nC \): everything about addition works, but scalar multiplication leaves the set, since \( i \cdot 1 = i \notin \nR \). Enlarging the field needs a construction, which is the second half of this section.

## The tower law

In @exm-c2-over-r we took a vector, wrote it in coordinates over \( \nC \), and then split each complex coordinate into real coordinates. The same two-stage process works for any fields.

::: {#thm-tower-law}
[Tower Law]

Let \( K \) be a subfield of \( L \), and let \( V \) be a vector space over \( L \). Suppose \( (a_1, \dots, a_m) \) is a basis of \( L \) over \( K \) and \( (\v_1, \dots, \v_n) \) is a basis of \( V \) over \( L \). Then the list of the \( mn \) vectors
\[
(a_1\v_1, \dots, a_m\v_1, \; a_1\v_2, \dots, a_m\v_2, \; \dots, \; a_1\v_n, \dots, a_m\v_n)
\]
is a basis of \( V \) over \( K \). In particular,
\[
\dim_K V = [L : K] \cdot \dim_L V.
\]
:::

::: {.idea}
Coordinates in two stages. A vector is an \( L \)-combination of the \( \v_j \); each \( L \)-coefficient is a \( K \)-combination of the \( a_i \). Substituting gives a double sum \( \sum_j \sum_i b_{ij}\,a_i\v_j \) with \( b_{ij} \in K \). For independence, run the same two stages backwards: regroup the double sum by \( j \), use independence over \( L \), then independence over \( K \).
:::

::: {.proof}
Throughout we use two axioms of @def-vector-space for scalars in \( L \): \( (c + c')\x = c\x + c'\x \) and \( c(c'\x) = (cc')\x \).

*Spanning.* Let \( \x \in V \). Since \( (\v_1, \dots, \v_n) \) spans \( V \) over \( L \), there are \( c_1, \dots, c_n \in L \) with \( \x = \sum_{j=1}^n c_j\v_j \). Since \( (a_1, \dots, a_m) \) spans \( L \) over \( K \), for each \( j \) there are \( b_{1j}, \dots, b_{mj} \in K \) with \( c_j = \sum_{i=1}^m b_{ij}a_i \). Therefore
\[
\x = \sum_{j=1}^n \Bigl( \sum_{i=1}^m b_{ij}a_i \Bigr)\v_j = \sum_{j=1}^n \sum_{i=1}^m (b_{ij}a_i)\v_j = \sum_{j=1}^n \sum_{i=1}^m b_{ij}(a_i\v_j),
\]
where the second equality uses \( (c + c')\x = c\x + c'\x \) and the third uses \( c(c'\x) = (cc')\x \). This is a \( K \)-linear combination of the vectors \( a_i\v_j \).

*Independence.* Let \( b_{ij} \in K \) with \( \sum_{j=1}^n \sum_{i=1}^m b_{ij}(a_i\v_j) = \0 \). Reading the display above from right to left,
\[
\sum_{j=1}^n \Bigl( \sum_{i=1}^m b_{ij}a_i \Bigr)\v_j = \0 .
\]
Each coefficient \( \sum_i b_{ij}a_i \) lies in \( L \), and \( (\v_1, \dots, \v_n) \) is independent over \( L \). Hence \( \sum_{i=1}^m b_{ij}a_i = 0 \) for every \( j \). For each fixed \( j \), this is a \( K \)-combination of \( (a_1, \dots, a_m) \) equal to \( 0 \), and that list is independent over \( K \). Hence \( b_{ij} = 0 \) for all \( i \) and \( j \).

So the \( mn \) vectors \( a_i\v_j \) form a basis of \( V \) over \( K \), and \( \dim_K V = mn = [L : K] \dim_L V \).
:::

The name comes from the picture of fields stacked in a tower, \( K \subseteq L \), with \( V \) on top: dimensions multiply as you go down. The most important case is \( \nR \subseteq \nC \).

::: {#thm-restriction-of-scalars-dimension}
[Complex Spaces as Real Spaces]

Let \( V \) be a vector space over \( \nC \) with basis \( (\v_1, \dots, \v_n) \). Then \( (\v_1, i\v_1, \dots, \v_n, i\v_n) \) is a basis of \( V \) over \( \nR \). In particular \( \dim_\nR V = 2\dim_\nC V \).
:::

::: {.proof}
By @exm-field-degrees, \( (1, i) \) is a basis of \( \nC \) over \( \nR \). By @thm-tower-law with \( a_1 = 1 \) and \( a_2 = i \), the list \( (1\v_1, i\v_1, \dots, 1\v_n, i\v_n) \) is a basis of \( V \) over \( \nR \), and \( 1\v_j = \v_j \) by @def-vector-space. The dimension is \( 2n \).
:::

This is the result of @exr-dimension-c2, now as a case of the tower law. For example, \( \dim_\nR \nC^n = 2n \), and \( \dim_\nR \nC[x]_{\le n} = 2(n + 1) \), with basis \( (1, i, x, ix, \dots, x^n, ix^n) \).

::: {.warning}
A subset of \( \nC^n \) can be a subspace over \( \nR \) without being a subspace over \( \nC \). The real vectors \( \nR^n \subseteq \nC^n \) contain \( \0 \) and are closed under addition and under multiplication by **real** scalars, so they form an \( \nR \)-subspace of dimension \( n \). But \( \e_1 \in \nR^n \) and \( i\e_1 \notin \nR^n \), so \( \nR^n \) is **not** a \( \nC \)-subspace. Always ask: a subspace over which field?
:::

::: {.check}
What is \( \dim_\nR M_{2 \times 3}(\nC) \)? What is \( \dim_\nQ \nQ(\sqrt2)^2 \)?
:::

::: {.solution}
\( M_{2 \times 3}(\nC) \) has dimension \( 6 \) over \( \nC \) (@exm-dimensions), so \( \dim_\nR = 2 \cdot 6 = 12 \) by @thm-restriction-of-scalars-dimension. The space \( \nQ(\sqrt2)^2 \) has dimension \( 2 \) over the field \( \nQ(\sqrt2) \), and \( [\nQ(\sqrt2) : \nQ] = 2 \) by @exm-field-degrees, so \( \dim_\nQ = 2 \cdot 2 = 4 \) by @thm-tower-law.
:::

## Complexification

Now go up. A real matrix such as the rotation \( \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \) moves every non-zero vector of \( \nR^2 \) off its own line. In \( \nC^2 \), however, it sends \( (1, -i) \) to \( (i, 1) = i(1, -i) \). To use such complex vectors for an arbitrary real space \( V \), not just \( \nR^n \), we need a complex space that contains \( V \) the way \( \nC^n \) contains \( \nR^n \).

The model is \( \nC^n \) itself. Every \( \z \in \nC^n \) splits as \( \z = \x + i\y \) with \( \x, \y \in \nR^n \), its real and imaginary parts, taken entry by entry. Multiplying by \( a + bi \) with \( a, b \in \nR \) gives
\[
(a + bi)(\x + i\y) = (a\x - b\y) + i(a\y + b\x).
\]
The right side only uses real scalars acting on real vectors. So we can copy it for any real space, exactly as \( \nC \) was built from pairs of real numbers in @def-complex-numbers.

*The complexification of \( V \) is the space of formal expressions \( \u + i\v \) with \( \u, \v \in V \), multiplied by complex numbers the way the rules of algebra dictate.*

::: {#def-complexification}
[Complexification]

Let \( V \) be a vector space over \( \nR \). The **complexification** of \( V \) is the set \( V_\nC \coloneqq V \times V \) with addition and scalar multiplication by \( \nC \) defined, **for all** \( (\u, \v), (\u', \v') \in V_\nC \) and \( a, b \in \nR \), by
\[
(\u, \v) + (\u', \v') \coloneqq (\u + \u', \; \v + \v'), \qquad (a + bi)(\u, \v) \coloneqq (a\u - b\v, \; a\v + b\u).
\]
We write \( \u + i\v \) for \( (\u, \v) \), and \( \u \) for \( (\u, \0) \).
:::

In words: addition is entry by entry. Multiplication by \( a + bi \) is the formula forced by \( i^2 = -1 \). The notation is honest: \( i(\v, \0) = (0\v - 1\0, \; 0\0 + 1\v) = (\0, \v) \), by @thm-zero-scalar-mult and @thm-scalar-zero-vector, so \( (\u, \0) + i(\v, \0) = (\u, \v) \). Also a **real** scalar acts entrywise: \( a(\u, \v) = (a\u, a\v) \). So \( V_\nC \), restricted to real scalars, is just two copies of \( V \).

**Why \( V_\nC \) is a vector space over \( \nC \).** The operations land in \( V \times V \). Addition is entrywise, so (commutativity, associativity, zero, negatives) follow from the same axioms in each entry of \( V \), with zero \( (\0, \0) \) and negative \( (-\u, -\v) \). We check the scalar axioms that involve the multiplication of \( \nC \); below, \( a\u - b\v \) means \( a\u + (-b)\v \), which is the same by @thm-negative-scalar-dist. Let \( \alpha = a + bi \) and \( \beta = c + di \) with \( a, b, c, d \in \nR \), and \( \z = (\u, \v) \).

- \( 1\z = \z \): we get \( (1\u - 0\v, \; 1\v + 0\u) = (\u, \v) \), since \( 0\v = \0 \) by @thm-zero-scalar-mult.
- \( \alpha(\beta\z) = (\alpha\beta)\z \): since \( \beta\z = (c\u - d\v, \; c\v + d\u) \), the axioms of \( V \) give
\[
\alpha(\beta\z) = \bigl( a(c\u - d\v) - b(c\v + d\u), \; a(c\v + d\u) + b(c\u - d\v) \bigr) = \bigl( (ac - bd)\u - (ad + bc)\v, \; (ac - bd)\v + (ad + bc)\u \bigr).
\]
Since \( \alpha\beta = (ac - bd) + (ad + bc)i \), this is \( (\alpha\beta)\z \).
- \( (\alpha + \beta)\z = \alpha\z + \beta\z \): with \( \alpha + \beta = (a + c) + (b + d)i \),
\[
(\alpha + \beta)\z = \bigl( (a + c)\u - (b + d)\v, \; (a + c)\v + (b + d)\u \bigr) = (a\u - b\v, \; a\v + b\u) + (c\u - d\v, \; c\v + d\u) = \alpha\z + \beta\z.
\]

The remaining axiom, \( \alpha(\z + \w) = \alpha\z + \alpha\w \), is @exr-changing-the-field-b3.

Here is the payoff: complexifying keeps the dimension, and even keeps the basis.

::: {#thm-complexification-basis}
[A Real Basis Is a Complex Basis of the Complexification]

Let \( V \) be a vector space over \( \nR \) with basis \( (\v_1, \dots, \v_n) \). Then \( (\v_1, \dots, \v_n) \), that is, \( ((\v_1, \0), \dots, (\v_n, \0)) \), is a basis of \( V_\nC \) over \( \nC \). In particular \( \dim_\nC V_\nC = \dim_\nR V \).
:::

::: {.idea}
A complex coefficient \( a_j + b_ji \) on \( \v_j \) puts \( a_j\v_j \) into the real part and \( b_j\v_j \) into the imaginary part. So one complex combination of the \( \v_j \) is the same as two real combinations, one for each part, and both questions (spanning, independence) split into two real questions about \( (\v_1, \dots, \v_n) \).
:::

::: {.proof}
For \( a, b \in \nR \) and \( \x \in V \), @def-complexification and @thm-scalar-zero-vector give
\[
(a + bi)(\x, \0) = (a\x - b\0, \; a\0 + b\x) = (a\x, \; b\x).
\]
Call this identity (∗).

*Spanning.* Let \( (\u, \v) \in V_\nC \). Since \( (\v_1, \dots, \v_n) \) spans \( V \), there are \( a_j, b_j \in \nR \) with \( \u = \sum_j a_j\v_j \) and \( \v = \sum_j b_j\v_j \). By (∗) and entrywise addition,
\[
\sum_{j=1}^n (a_j + b_ji)(\v_j, \0) = \sum_{j=1}^n (a_j\v_j, \; b_j\v_j) = \Bigl( \sum_{j=1}^n a_j\v_j, \; \sum_{j=1}^n b_j\v_j \Bigr) = (\u, \v).
\]

*Independence.* Let \( \alpha_1, \dots, \alpha_n \in \nC \) with \( \sum_j \alpha_j(\v_j, \0) = (\0, \0) \), and write \( \alpha_j = a_j + b_ji \) with \( a_j, b_j \in \nR \). By the same computation, \( \bigl( \sum_j a_j\v_j, \; \sum_j b_j\v_j \bigr) = (\0, \0) \). Since \( (\v_1, \dots, \v_n) \) is independent over \( \nR \), all \( a_j = 0 \) and all \( b_j = 0 \). Hence every \( \alpha_j = 0 \).

Therefore \( (\v_1, \dots, \v_n) \) is a basis of \( V_\nC \), and \( \dim_\nC V_\nC = n \).
:::

As a consistency check, restricting \( V_\nC \) back to \( \nR \) gives \( \dim_\nR V_\nC = 2n \) by @thm-restriction-of-scalars-dimension, which matches the fact that \( V_\nC \) over \( \nR \) is two copies of \( V \). The same proof works word for word for an infinite basis set, since every combination involves finitely many vectors.

::: {#exm-complexification-rn}
[The Complexification of \( \nR^n \) Is \( \nC^n \)]

Show that the map \( (\x, \y) \mapsto \x + i\y \), from \( (\nR^n)_\nC \) to \( \nC^n \), is a bijection that respects addition and multiplication by complex scalars.
:::

::: {.solution}
Here \( \x + i\y \) is computed in \( \nC^n \): its \( k \)-th entry is \( x_k + y_ki \). Every \( \z \in \nC^n \) has unique real and imaginary parts entry by entry (@def-complex-numbers), so exactly one pair \( (\x, \y) \) of real vectors maps to \( \z \). Hence the map is a bijection.

Addition is entrywise on both sides, so it is respected. For scaling, let \( a, b \in \nR \). In \( (\nR^n)_\nC \), \( (a + bi)(\x, \y) = (a\x - b\y, \; a\y + b\x) \), which maps to the vector with entries \( (ax_k - by_k) + (ay_k + bx_k)i \). In \( \nC^n \), the \( k \)-th entry of \( (a + bi)(\x + i\y) \) is
\[
(a + bi)(x_k + y_ki) = (ax_k - by_k) + (ay_k + bx_k)i.
\]
The two agree, so the map respects scalar multiplication. It sends the basis \( (\e_1, \dots, \e_n) \) of \( (\nR^n)_\nC \) from @thm-complexification-basis to the standard basis of \( \nC^n \).
:::

So \( (\nR^n)_\nC \) is \( \nC^n \) in disguise; in Chapter 3 such a bijection will be called an isomorphism. In the same way \( (M_n(\nR))_\nC \) is \( M_n(\nC) \), and \( (\nR[x]_{\le n})_\nC \) is \( \nC[x]_{\le n} \). The construction earns its keep in Chapter 8, where real matrices without real eigenvalues, like the rotation above, get complex ones, and in Chapter 11, in the spectral theory of real operators.

## Exercises

### A. Check your understanding

:::: {#exr-changing-the-field-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the degree \( [L : K] \) of a subfield \( K \subseteq L \).
2. State the Tower Law.
3. What is \( \dim_\nR \nC^3 \)? Give a basis.
4. True or false: every \( \nC \)-subspace of \( \nC^n \) is an \( \nR \)-subspace. Justify your answer.
5. What is \( \dim_\nC (M_2(\nR))_\nC \)?
:::
::::

::: {.solution}
(a) \( [L : K] = \dim_K L \), where \( L \) is regarded as a vector space over \( K \) by restriction of scalars (@def-restriction-of-scalars), when this dimension is finite.

(b) See @thm-tower-law: if \( (a_i) \) is a basis of \( L \) over \( K \) and \( (\v_j) \) is a basis of \( V \) over \( L \), then \( (a_i\v_j) \) is a basis of \( V \) over \( K \), so \( \dim_K V = [L : K]\dim_L V \).

(c) \( 6 \), with basis \( (\e_1, i\e_1, \e_2, i\e_2, \e_3, i\e_3) \), by @thm-restriction-of-scalars-dimension.

(d) True. A \( \nC \)-subspace contains \( \0 \), is closed under addition, and is closed under multiplication by every complex number, in particular by every real number.

(e) \( 4 \): \( \dim_\nR M_2(\nR) = 4 \) (@exm-dimensions), and @thm-complexification-basis keeps the dimension.
:::

### B. Practice

:::: {#exr-changing-the-field-b1}
[B1: A Tower over \( \nQ \)]

Find \( \dim_\nQ \nQ(\sqrt2)^3 \) and a basis of \( \nQ(\sqrt2)^3 \) over \( \nQ \).
::::

::: {.solution}
By @exm-q-sqrt2-field, \( \nQ(\sqrt2) \) is a field, so \( \nQ(\sqrt2)^3 \) is a vector space over it with basis \( (\e_1, \e_2, \e_3) \) and dimension \( 3 \) (@exm-dimensions). By @exm-field-degrees, \( (1, \sqrt2) \) is a basis of \( \nQ(\sqrt2) \) over the subfield \( \nQ \). By @thm-tower-law,
\[
(\e_1, \sqrt2\e_1, \e_2, \sqrt2\e_2, \e_3, \sqrt2\e_3)
\]
is a basis of \( \nQ(\sqrt2)^3 \) over \( \nQ \). Hence \( \dim_\nQ \nQ(\sqrt2)^3 = 2 \cdot 3 = 6 \).
:::

:::: {#exr-changing-the-field-b2}
[B2: Complex Matrices over \( \nR \)]

Let \( E_{11}, E_{12}, E_{21}, E_{22} \) be the matrix units of \( M_2(\nC) \). Find a basis of \( M_2(\nC) \) over \( \nR \), and write \( A = \begin{pmatrix} 1 + i & 2 \\ -i & 3i \end{pmatrix} \) in it.
::::

::: {.solution}
The matrix units form a basis of \( M_2(\nC) \) over \( \nC \) (@exm-standard-bases). By @thm-restriction-of-scalars-dimension,
\[
(E_{11}, iE_{11}, E_{12}, iE_{12}, E_{21}, iE_{21}, E_{22}, iE_{22})
\]
is a basis of \( M_2(\nC) \) over \( \nR \), so \( \dim_\nR M_2(\nC) = 8 \). Splitting each entry of \( A \) into real and imaginary parts,
\[
A = 1E_{11} + 1(iE_{11}) + 2E_{12} + 0(iE_{12}) + 0E_{21} + (-1)(iE_{21}) + 0E_{22} + 3(iE_{22}).
\]
:::

:::: {#exr-changing-the-field-b3}
[B3: Working in a Complexification]

Let \( V \) be a vector space over \( \nR \).

::: {.enumerate options="label=(\alph*)"}
1. Verify that \( \alpha(\z + \w) = \alpha\z + \alpha\w \) for all \( \alpha \in \nC \) and \( \z, \w \in V_\nC \).
2. In \( (\nR[x]_{\le 1})_\nC \), compute \( (2 - i)\bigl( (1 + x) + ix \bigr) \) from @def-complexification, and compare with the product \( (2 - i)(1 + x + ix) \) computed in \( \nC[x] \).
:::
::::

::: {.solution}
(a) Let \( \alpha = a + bi \) with \( a, b \in \nR \), \( \z = (\u, \v) \) and \( \w = (\u', \v') \). Then \( \z + \w = (\u + \u', \v + \v') \), and by the distributive law in \( V \) and @thm-negative-scalar-dist,
\[
\alpha(\z + \w) = \bigl( a(\u + \u') - b(\v + \v'), \; a(\v + \v') + b(\u + \u') \bigr) = \bigl( (a\u - b\v) + (a\u' - b\v'), \; (a\v + b\u) + (a\v' + b\u') \bigr),
\]
where we also rearranged the sums using commutativity and associativity of addition in \( V \). The right side is \( (a\u - b\v, \; a\v + b\u) + (a\u' - b\v', \; a\v' + b\u') = \alpha\z + \alpha\w \).

(b) Here \( a = 2 \), \( b = -1 \), \( \u = 1 + x \) and \( \v = x \). Then \( a\u - b\v = 2 + 2x + x = 2 + 3x \) and \( a\v + b\u = 2x - (1 + x) = -1 + x \). So the product is \( (2 + 3x) + i(-1 + x) \). In \( \nC[x] \), \( (2 - i)(1 + x + ix) = 2 + 2x + 2ix - i - ix - i^2x = (2 + 3x) + i(-1 + x) \), the same answer.
:::

### C. Going deeper

:::: {#exr-changing-the-field-c1}
[C1: When Is a Real Subspace Complex?]

Let \( W \subseteq \nC^n \) be a subspace over \( \nR \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( W \) is a subspace over \( \nC \) if and only if \( i\w \in W \) for every \( \w \in W \).
2. Deduce that if \( W \) is a subspace over \( \nC \), then \( \dim_\nR W \) is even.
3. Show that \( W_0 = \{ (z, \conj{z}) : z \in \nC \} \subseteq \nC^2 \) is a subspace over \( \nR \) of even real dimension that is **not** a subspace over \( \nC \). So the converse of (b) fails.
:::
::::

::: {.solution}
(a) (⇒) If \( W \) is a \( \nC \)-subspace, it is closed under multiplication by \( i \).

(⇐) Suppose \( i\w \in W \) for every \( \w \in W \). We use @thm-subspace-test over \( \nC \). Since \( W \) is an \( \nR \)-subspace, \( \0 \in W \) and \( W \) is closed under addition. Let \( \w \in W \) and \( a + bi \in \nC \) with \( a, b \in \nR \). Then \( a\w \in W \) and \( b(i\w) \in W \), because \( W \) is closed under real scalars, and \( (a + bi)\w = a\w + b(i\w) \) by the axioms of \( \nC^n \). This lies in \( W \) by closure under addition. Hence \( W \) is a \( \nC \)-subspace.

(b) \( W \) is a subspace of the finite-dimensional \( \nC \)-space \( \nC^n \), so by @thm-subspace-dimension it is finite-dimensional over \( \nC \), and by @cor-basis-existence it has a basis over \( \nC \), of some length \( k \). Restricting the scalars of \( W \) to \( \nR \) gives the same real space as before, so \( \dim_\nR W = 2k \) by @thm-restriction-of-scalars-dimension.

(c) Write \( z = a + bi \) with \( a, b \in \nR \). Then \( (z, \conj{z}) = (a + bi, a - bi) = a(1, 1) + b(i, -i) \), so \( W_0 \) is the \( \nR \)-span of \( ((1, 1), (i, -i)) \) and is an \( \nR \)-subspace by @thm-span-subspace. The list is independent over \( \nR \): \( a(1, 1) + b(i, -i) = \0 \) gives \( a + bi = 0 \), so \( a = b = 0 \). Hence \( \dim_\nR W_0 = 2 \). But \( (1, 1) \in W_0 \) while \( i(1, 1) = (i, i) \notin W_0 \), because \( \conj{i} = -i \ne i \). By (a), \( W_0 \) is not a \( \nC \)-subspace.
:::

:::: {#exr-changing-the-field-c2}
[C2: A Tower of Degree Four]

Let \( V = \{ x + y\sqrt3 : x, y \in \nQ(\sqrt2) \} \subseteq \nR \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \sqrt3 \notin \nQ(\sqrt2) \).
2. Regard \( \nR \) as a vector space over its subfield \( \nQ(\sqrt2) \). Prove that \( V \) is a subspace with basis \( (1, \sqrt3) \).
3. Deduce that \( \dim_\nQ V = 4 \), with basis \( (1, \sqrt2, \sqrt3, \sqrt6) \).
:::

*Hint for (a): square both sides, and argue with remainders on division by 3.*
::::

::: {.solution}
(a) First, there are no integers \( p, q \) with \( q \ne 0 \), not both divisible by \( 3 \), and \( cp^2 = 3q^2 \) for \( c \in \{1, 2\} \). Indeed, if \( 3 \nmid p \), then \( p = 3t \pm 1 \) and \( cp^2 = c(9t^2 \pm 6t + 1) \) leaves remainder \( c \in \{1, 2\} \) on division by \( 3 \), while \( 3q^2 \) leaves remainder \( 0 \). So \( 3 \mid p \), say \( p = 3s \). Then \( 9cs^2 = 3q^2 \), so \( q^2 = 3cs^2 \), and the same remainder argument (a square not divisible by \( 3 \) leaves remainder \( 1 \)) gives \( 3 \mid q \), a contradiction.

Now suppose \( \sqrt3 = a + b\sqrt2 \) with \( a, b \in \nQ \). Squaring, \( 3 = a^2 + 2b^2 + 2ab\sqrt2 \). If \( ab \ne 0 \), then \( \sqrt2 = (3 - a^2 - 2b^2)/(2ab) \in \nQ \), contradicting @thm-sqrt2-irrational. If \( b = 0 \), then \( a^2 = 3 \); writing \( a = p/q \) in lowest terms gives \( p^2 = 3q^2 \) with \( p, q \) not both divisible by \( 3 \), which is impossible. If \( a = 0 \), then \( 2b^2 = 3 \), and \( b = p/q \) in lowest terms gives \( 2p^2 = 3q^2 \), also impossible. Hence \( \sqrt3 \notin \nQ(\sqrt2) \).

(b) \( \nQ(\sqrt2) \) is a subfield of \( \nR \) by @exm-q-sqrt2-field, so \( \nR \) is a vector space over it by restriction of scalars. We use @thm-subspace-test. (1) \( 0 = 0 + 0\sqrt3 \in V \). (2) \( (x + y\sqrt3) + (x' + y'\sqrt3) = (x + x') + (y + y')\sqrt3 \in V \), since \( \nQ(\sqrt2) \) is closed under addition. (3) For \( c \in \nQ(\sqrt2) \), \( c(x + y\sqrt3) = cx + (cy)\sqrt3 \in V \), since \( \nQ(\sqrt2) \) is closed under multiplication. So \( V \) is a subspace.

The list \( (1, \sqrt3) \) spans \( V \) by the definition of \( V \). For independence, let \( x + y\sqrt3 = 0 \) with \( x, y \in \nQ(\sqrt2) \). If \( y \ne 0 \), then \( y^{-1} \in \nQ(\sqrt2) \) and \( \sqrt3 = -xy^{-1} \in \nQ(\sqrt2) \), contradicting (a). So \( y = 0 \), and then \( x = 0 \). Hence \( (1, \sqrt3) \) is a basis and \( \dim_{\nQ(\sqrt2)} V = 2 \).

(c) By @exm-field-degrees, \( (1, \sqrt2) \) is a basis of \( \nQ(\sqrt2) \) over \( \nQ \). By @thm-tower-law applied to \( \nQ \subseteq \nQ(\sqrt2) \) and the \( \nQ(\sqrt2) \)-space \( V \), the list \( (1 \cdot 1, \sqrt2 \cdot 1, 1 \cdot \sqrt3, \sqrt2 \cdot \sqrt3) = (1, \sqrt2, \sqrt3, \sqrt6) \) is a basis of \( V \) over \( \nQ \). Hence \( \dim_\nQ V = 2 \cdot 2 = 4 \).
:::
