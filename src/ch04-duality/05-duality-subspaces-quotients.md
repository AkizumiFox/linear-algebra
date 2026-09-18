# Duality for Subspaces and Quotients

A subspace \( U \) of \( V \) gives two new vector spaces: \( U \) itself, and the quotient \( V/U \) of Chapter 3. Each has a dual space, and so far \( U^{*} \) and \( (V/U)^{*} \) have nothing to do with \( V^{*} \). This section connects them. The answer is a swap: the dual of the quotient is a **subspace** of \( V^{*} \), namely the annihilator \( U^{0} \), and the dual of the subspace is a **quotient** of \( V^{*} \), namely \( V^{*}/U^{0} \). Both identifications come from the First Isomorphism Theorem, and neither needs a basis. At the end we use them to describe hyperplanes, the subspaces cut out by a single equation, in any dimension.

## Restricting functionals to a subspace

Let \( U \) be a subspace of \( V \). A functional \( \varphi \in V^{*} \) measures every vector of \( V \), so in particular it measures the vectors of \( U \). Forgetting the rest gives the **restriction** \( \varphi|_U \colon U \to F \), \( \u \mapsto \varphi(\u) \), which is a functional on \( U \). This defines the restriction map
\[
\rho \colon V^{*} \to U^{*}, \qquad \rho(\varphi) = \varphi|_U .
\]
It is not a new kind of map. Let \( \iota \colon U \to V \), \( \iota(\u) = \u \), be the inclusion. Its dual map (@def-dual-map) sends \( \varphi \) to \( \varphi \circ \iota \), and \( (\varphi \circ \iota)(\u) = \varphi(\u) \). So \( \rho = \iota' \), and in particular \( \rho \) is linear.

Two questions decide what \( \rho \) does. Which functionals restrict to zero? By @def-annihilator, exactly those in \( U^{0} \). And does every functional on \( U \) come from one on \( V \)? That is an extension problem, and it has a positive answer in every dimension.

::: {#thm-dual-of-subspace}
[Dual of a Subspace]

Let \( V \) be a vector space over \( F \), of any dimension, and let \( U \) be a subspace of \( V \). The restriction map \( \rho \colon V^{*} \to U^{*} \), \( \rho(\varphi) = \varphi|_U \), is linear and surjective, and \( \ker \rho = U^{0} \). Hence
\[
V^{*}/U^{0} \to U^{*}, \qquad \varphi + U^{0} \mapsto \varphi|_U
\]
is a well-defined isomorphism, and \( U^{*} \cong V^{*}/U^{0} \).
:::

::: {.idea}
The kernel is the definition of \( U^{0} \) read aloud. The real content is surjectivity: given \( \psi \) on \( U \), we must extend it to all of \( V \). A basis tells us how. Extend a basis of \( U \) to a basis of \( V \); a linear map may be prescribed freely on a basis, so declare the extension to agree with \( \psi \) on the basis of \( U \) and to be \( 0 \) on the new basis vectors. Then the First Isomorphism Theorem turns "surjective with kernel \( U^{0} \)" into the isomorphism.
:::

::: {.proof}
We saw above that \( \rho = \iota' \) is linear. For \( \varphi \in V^{*} \), \( \rho(\varphi) = 0 \) means \( \varphi(\u) = 0 \) for every \( \u \in U \), which is \( \varphi \in U^{0} \) by @def-annihilator. So \( \ker \rho = U^{0} \).

*Surjective.* Let \( \psi \in U^{*} \). By @thm-every-space-has-basis, \( U \) has a basis \( B_U \). It is a linearly independent subset of \( V \), so by @thm-basis-extension-general there is a basis \( B \) of \( V \) with \( B_U \subseteq B \). By @thm-linear-map-from-any-basis there is a linear map \( \varphi \colon V \to F \) with
\[
\varphi(\b) = \psi(\b) \quad \text{for } \b \in B_U, \qquad \varphi(\b) = 0 \quad \text{for } \b \in B \setminus B_U .
\]
Then \( \varphi|_U \) and \( \psi \) are linear maps \( U \to F \) that agree on the basis \( B_U \) of \( U \), so \( \varphi|_U = \psi \) by the uniqueness part of @thm-linear-map-from-any-basis. Thus \( \rho(\varphi) = \psi \), and \( \rho \) is surjective. (If \( V \) is finite-dimensional, the finite versions @cor-basis-existence, @thm-basis-extension and @thm-linear-transform-basis suffice, and no choice principle is needed.)

By the First Isomorphism Theorem (@thm-first-isomorphism), \( \varphi + \ker\rho \mapsto \rho(\varphi) \) is a well-defined isomorphism \( V^{*}/\ker \rho \to \im \rho \). Since \( \ker \rho = U^{0} \) and \( \im \rho = U^{*} \), this is the claimed isomorphism.
:::

In words: **a functional on \( U \) is a functional on \( V \), up to adding something that vanishes on \( U \).** Two extensions of the same \( \psi \) differ by an element of \( U^{0} \), and every element of \( U^{0} \) can be added.

When \( V \) is finite-dimensional, taking dimensions recovers the count of this chapter. By @cor-dimension-dual-space, \( \dim U^{*} = \dim U \) and \( \dim V^{*} = \dim V \), and by @thm-dimension-quotient, \( \dim(V^{*}/U^{0}) = \dim V - \dim U^{0} \). So the isomorphism says \( \dim U = \dim V - \dim U^{0} \), which is @thm-dimension-annihilator again.

## Functionals on a quotient

Now the other space. A functional \( \psi \) on \( V/U \) measures cosets. Composing with the quotient map \( \pi \colon V \to V/U \), \( \pi(\v) = \v + U \), turns it into a measurement of vectors, \( \v \mapsto \psi(\v + U) \). This functional on \( V \) cannot tell apart two vectors in the same coset, so in particular it is zero on \( U \). The theorem says that nothing is lost and nothing else appears: the functionals on \( V/U \) are **exactly** the functionals on \( V \) that vanish on \( U \).

::: {#thm-dual-of-quotient}
[Dual of a Quotient]

Let \( V \) be a vector space over \( F \), of any dimension, let \( U \) be a subspace, and let \( \pi \colon V \to V/U \) be the quotient map. Then the dual map
\[
\pi' \colon (V/U)^{*} \to V^{*}, \qquad \pi'(\psi) = \psi \circ \pi ,
\]
is injective, and its image is \( U^{0} \). Hence \( \pi' \) is an isomorphism from \( (V/U)^{*} \) onto \( U^{0} \), and \( (V/U)^{*} \cong U^{0} \).
:::

::: {.idea}
Injectivity uses only that \( \pi \) is surjective: if \( \psi \circ \pi \) is zero, then \( \psi \) is zero on every coset. For the image, one inclusion is "\( \pi \) kills \( U \)". The other inclusion asks us to build a functional on \( V/U \) from a functional on \( V \) that vanishes on \( U \), and that is exactly what the universal property of the quotient does.
:::

::: {.proof}
The map \( \pi' \) is linear by @def-dual-map.

*Injective.* Suppose \( \pi'(\psi) = \psi \circ \pi = 0 \). Every element of \( V/U \) is \( \pi(\v) \) for some \( \v \in V \), because \( \pi \) is surjective (@thm-quotient-space-operations-well-defined (c)). Then \( \psi(\pi(\v)) = 0 \) for every \( \v \), so \( \psi = 0 \). By @thm-injective-iff-trivial-kernel, \( \pi' \) is injective.

*\( \im \pi' \subseteq U^{0} \).* For \( \u \in U \), \( \pi(\u) = U \) is the zero vector of \( V/U \), so \( (\psi \circ \pi)(\u) = \psi(\0) = 0 \). Hence \( \psi \circ \pi \in U^{0} \).

*\( U^{0} \subseteq \im \pi' \).* Let \( \varphi \in U^{0} \). Then \( U \subseteq \ker \varphi \), so by @thm-quotient-universal-property (a) there is a linear map \( \psi \colon V/U \to F \) with \( \psi \circ \pi = \varphi \). This \( \psi \) lies in \( (V/U)^{*} \), and \( \pi'(\psi) = \varphi \).

So \( \pi' \) is an injective linear map with image \( U^{0} \); regarded as a map onto \( U^{0} \) it is a linear bijection, hence an isomorphism.
:::

Concretely, the inverse isomorphism \( U^{0} \to (V/U)^{*} \) is \( \varphi \mapsto \bar\varphi \), where \( \bar\varphi(\v + U) = \varphi(\v) \). The formula is well defined precisely because \( \varphi \) vanishes on \( U \): if \( \v - \v' \in U \), then \( \varphi(\v) - \varphi(\v') = \varphi(\v - \v') = 0 \).

The two theorems fit together as a mirror:

| | subspace \( U \subseteq V \) | quotient \( V/U \) |
|---|---|---|
| its dual is | a **quotient** of \( V^{*} \): \( U^{*} \cong V^{*}/U^{0} \) | a **subspace** of \( V^{*} \): \( (V/U)^{*} \cong U^{0} \) |
| the map | \( \iota' \): restrict | \( \pi' \): compose with \( \pi \) |
| the map is | surjective | injective |

The last row is no accident: \( \iota \) is injective and \( \pi \) is surjective, and dualizing swaps the two properties.

**Alternatively,** in finite dimension both theorems follow from @thm-kernel-image-dual-map, which says \( \ker T' = (\im T)^{0} \) and \( \im T' = (\ker T)^{0} \). For \( T = \pi \): \( \im \pi = V/U \), whose annihilator is \( \{0\} \), and \( \ker \pi = U \), so \( \pi' \) is injective with image \( U^{0} \). For \( T = \iota \): \( \im \iota = U \), so \( \ker \iota' = U^{0} \), and \( \ker \iota = \{\0\} \), whose annihilator is all of \( U^{*} \), so \( \iota' \) is surjective. The proofs above avoid dimension counts, which is why they work in every dimension.

::: {.check}
Let \( V \) be a vector space of dimension \( 6 \) and \( U \) a subspace of dimension \( 2 \). Find \( \dim U^{0} \), \( \dim (V/U)^{*} \), \( \dim U^{*} \) and \( \dim(V^{*}/U^{0}) \), and check that the two theorems are consistent with these numbers.
:::

::: {.solution}
By @thm-dimension-annihilator, \( \dim U^{0} = 6 - 2 = 4 \). By @thm-dimension-quotient and @cor-dimension-dual-space, \( \dim(V/U)^{*} = \dim(V/U) = 4 \), matching \( (V/U)^{*} \cong U^{0} \). Next, \( \dim U^{*} = \dim U = 2 \), and \( \dim(V^{*}/U^{0}) = 6 - 4 = 2 \), matching \( U^{*} \cong V^{*}/U^{0} \).
:::

## A line in \( \nR^3 \), in coordinates

The theorems name their isomorphisms without choosing anything. To see them act, we now choose bases and compute. Recall that a functional on \( \nR^3 \) is determined by its values on \( \e_1, \e_2, \e_3 \) (@thm-functionals-on-fn). So every \( \varphi \in (\nR^3)^{*} \) has the form \( \varphi(x, y, z) = ax + by + cz \), with \( (a, b, c) = (\varphi(\e_1), \varphi(\e_2), \varphi(\e_3)) \). We write such a functional simply as \( ax + by + cz \).

::: {#exm-dual-of-line-quotient}
[Both isomorphisms for a line]

Let \( \u = (1, 2, -1) \) and \( U = \Span(\u) \subseteq \nR^3 \).

::: {.enumerate options="label=(\alph*)"}
1. Find a basis of \( U^{0} \).
2. Find a basis of \( \nR^3/U \), its dual basis \( (\psi_1, \psi_2) \) of \( (\nR^3/U)^{*} \), and the images \( \pi'(\psi_1), \pi'(\psi_2) \).
3. Describe the restriction map \( \rho \colon (\nR^3)^{*} \to U^{*} \) and the isomorphism \( (\nR^3)^{*}/U^{0} \to U^{*} \).
:::
:::

::: {.solution}
(a) By @thm-annihilator-properties (b), \( U^{0} = \{\u\}^{0} \), so \( ax + by + cz \in U^{0} \) exactly when \( a + 2b - c = 0 \), that is, \( c = a + 2b \). Taking \( (a, b) = (1, 0) \) and \( (0, 1) \) gives
\[
\varphi_1 = x + z, \qquad \varphi_2 = y + 2z .
\]
They are independent (look at the coefficients of \( x \) and \( y \)), and \( \dim U^{0} = 3 - 1 = 2 \) by @thm-dimension-annihilator, so \( (\varphi_1, \varphi_2) \) is a basis of \( U^{0} \) (@thm-right-size-basis).

(b) The list \( (\u, \e_1, \e_2) \) is independent: in \( a\u + b\e_1 + c\e_2 = (a + b, 2a + c, -a) = \0 \), the third entry gives \( a = 0 \), and then \( b = c = 0 \). It has length 3, so it is a basis of \( \nR^3 \), and by @thm-dimension-quotient \( (\e_1 + U, \e_2 + U) \) is a basis of \( \nR^3/U \). Its dual basis consists of the \( \psi_i \) with \( \psi_i(\e_j + U) = \delta_{ij} \) (@thm-dual-basis).

The functional \( \pi'(\psi_1) = \psi_1 \circ \pi \) on \( \nR^3 \) takes the values \( \psi_1(\e_1 + U) = 1 \) at \( \e_1 \), \( \psi_1(\e_2 + U) = 0 \) at \( \e_2 \), and \( \psi_1(U) = 0 \) at \( \u \). Writing it as \( ax + by + cz \), this says \( a = 1 \), \( b = 0 \) and \( a + 2b - c = 0 \), so \( c = 1 \). Similarly \( \pi'(\psi_2) \) has \( a = 0 \), \( b = 1 \), \( c = 2 \). Hence
\[
\pi'(\psi_1) = x + z = \varphi_1, \qquad \pi'(\psi_2) = y + 2z = \varphi_2 .
\]
So \( \pi' \) carries the dual basis of \( (\nR^3/U)^{*} \) onto the basis of \( U^{0} \) found in (a), as @thm-dual-of-quotient predicts. Read backwards: \( \psi_1((x, y, z) + U) = x + z \) and \( \psi_2((x, y, z) + U) = y + 2z \). These are well defined, since adding \( t\u = (t, 2t, -t) \) changes \( x + z \) by \( t - t = 0 \) and \( y + 2z \) by \( 2t - 2t = 0 \).

(c) The space \( U^{*} \) is one-dimensional, with basis the functional \( \xi \) determined by \( \xi(\u) = 1 \) (the dual basis of \( (\u) \)). A functional \( \varphi = ax + by + cz \) restricts to \( \varphi|_U = \varphi(\u)\,\xi = (a + 2b - c)\,\xi \), since both sides take the value \( a + 2b - c \) at \( \u \). So \( \rho \) is "evaluate at \( \u \)". Its kernel is \( \{ a + 2b - c = 0 \} = U^{0} \), and it is surjective, since \( \rho(x) = \xi \). The isomorphism of @thm-dual-of-subspace is
\[
(ax + by + cz) + U^{0} \ \mapsto\ (a + 2b - c)\,\xi .
\]
For instance \( x + U^{0} = -z + U^{0} \), because \( x - (-z) = \varphi_1 \in U^{0} \); both restrict to \( \xi \).
:::

## Why "natural" matters here

In the example, bases entered only when we wanted numbers. The maps \( \rho \) and \( \pi' \) were defined before any basis was chosen: restrict a functional, or compose it with \( \pi \). That is what makes the two isomorphisms **natural**, in the sense of the discussion of the double dual. They are part of the structure of \( V \) and \( U \), not of a coordinate system.

There is a tempting shortcut that is **not** natural. Since \( U^{*} \) is a quotient of \( V^{*} \), one might try to find a copy of \( U^{*} \) **inside** \( V^{*} \), as a subspace. This can be done, but only by making a choice. Pick a complement \( W \) of \( U \), so \( V = U \oplus W \). A functional that vanishes on \( W \) is determined by its values on \( U \), so the restriction \( \rho \) maps \( W^{0} \) isomorphically onto \( U^{*} \) (@exr-duality-subspaces-quotients-c2). But different complements give different subspaces \( W^{0} \).

::: {.warning}
**\( U^{*} \) is not a subspace of \( V^{*} \).** Its elements are functionals on \( U \), which cannot be evaluated at vectors outside \( U \). To place \( U^{*} \) inside \( V^{*} \) one must extend each functional, and extensions are not unique. In the example above, the complement \( W_1 = \Span(\e_1, \e_2) \) of \( U \) gives \( W_1^{0} = \Span(z) \), while \( W_2 = \Span(\e_1, \e_3) \) gives \( W_2^{0} = \Span(y) \). These are different lines in \( (\nR^3)^{*} \), and both restrict isomorphically onto \( U^{*} \): \( z|_U = -\xi \) and \( y|_U = 2\xi \). The choice-free statement is \( U^{*} \cong V^{*}/U^{0} \), a quotient.
:::

The same caution applies on the other side, in reverse. \( (V/U)^{*} \) **is** naturally a subspace of \( V^{*} \), namely \( U^{0} \), but \( V/U \) itself is not a subspace of \( V \). Duality turns the quotient, which has no natural home inside \( V \), into a subspace, which does.

## Codimension and hyperplanes

The quotient measures how far a subspace is from filling the whole space. In \( \nR^3 \) a plane through the origin misses "one direction" and a line misses "two directions". For finite-dimensional \( V \) the number of missing directions is \( \dim V - \dim U \). But this formula is useless in \( F[x] \), where \( \dim V \) and \( \dim U \) may both be infinite, although \( U = \{ p : p(0) = 0 \} \) misses only one direction: every polynomial is a constant plus an element of \( U \). The quotient gives the right number in every case.

*The codimension of \( U \) counts the directions in \( V \) that \( U \) is missing.*

::: {#def-codimension}
[Codimension]

Let \( U \) be a subspace of a vector space \( V \) over \( F \). If \( V/U \) is finite-dimensional, the **codimension** of \( U \) in \( V \) is
\[
\codim U \coloneqq \dim(V/U) .
\]
If \( V/U \) is infinite-dimensional, we say that \( U \) has **infinite codimension**.
:::

In words: we do not compare the sizes of \( U \) and \( V \). We collapse \( U \) to zero and measure what is left. The codimension depends on the ambient space, so when that is unclear we write "codimension of \( U \) **in** \( V \)".

::: {#def-hyperplane}
[Hyperplane]

A **hyperplane** in \( V \) is a subspace \( H \) of \( V \) of codimension **exactly** \( 1 \), that is, with \( \dim(V/H) = 1 \).
:::

**Examples.**

- **Finite dimension.** If \( V \) is finite-dimensional, then \( \codim U = \dim V - \dim U \) by @thm-dimension-quotient. The hyperplanes of \( F^n \) are its subspaces of dimension \( n - 1 \): the lines through \( \0 \) in \( F^2 \) and the planes through \( \0 \) in \( F^3 \).
- **Trace.** In \( M_n(F) \) with \( n \ge 1 \), the trace-zero matrices are the kernel of \( \tr \colon M_n(F) \to F \). This map is linear and onto, since \( \tr(c\E_{11}) = c \), so \( M_n(F)/\ker\tr \cong F \) by @thm-first-isomorphism, and the trace-zero matrices form a hyperplane.
- **Polynomials.** In \( F[x] \), let \( U = \{ p : p(0) = 0 \} \). Evaluation at \( 0 \) is a linear map \( F[x] \to F \) with kernel \( U \), and it is surjective because the constant \( c \) maps to \( c \). By @thm-first-isomorphism, \( F[x]/U \cong F \), so \( U \) is a hyperplane in the infinite-dimensional space \( F[x] \). In the same way \( \{ p : p(0) = p(1) = 0 \} \) has codimension 2 (@exr-duality-subspaces-quotients-b3).
- **Degenerate cases.** \( \codim V = 0 \), since \( V/V \) is the zero space, and \( \codim\{\0\} = \dim V \) when \( V \) is finite-dimensional. In particular \( V \) itself is **not** a hyperplane, and the only hyperplane of a one-dimensional space is \( \{\0\} \). The zero space \( \{\0\} \) has no hyperplanes at all.

**Non-example by minimal change.** In \( \nR^3 \), the plane \( \{ x + y + z = 0 \} \) is a hyperplane. Replace it by the line \( \{ x + y + z = 0,\ x - y = 0 \} = \Span((1, 1, -2)) \). It is still a subspace, but its codimension is \( 3 - 1 = 2 \), so the clause "codimension **exactly** 1" fails. Replace it instead by \( \{ x + y + z = 1 \} \): now it is not a subspace at all, so it has no codimension. It is a coset of a hyperplane, an object we return to in the next section.

**Why this definition.** Codimension is the dual notion of dimension, and the duality theorems make this precise. If \( U \) has finite codimension, then by @thm-dual-of-quotient, @cor-dimension-dual-space and @thm-isomorphic-iff-same-dimension,
\[
\codim U = \dim(V/U) = \dim (V/U)^{*} = \dim U^{0},
\]
and this holds even when \( V \) is infinite-dimensional. So **dimension counts vectors, and codimension counts independent equations**. For finite-dimensional \( V \) this is @thm-dimension-annihilator again: \( \dim U^{0} = \dim V - \dim U \).

::: {.warning}
**In infinite dimension a hyperplane need not be "smaller" than the whole space.** In \( F[x] \), the hyperplane \( U = \{ p : p(0) = 0 \} = \{ xq : q \in F[x] \} \) is isomorphic to \( F[x] \) itself, via \( q \mapsto xq \): this map is linear, injective (if \( xq = 0 \) then \( q = 0 \)) and onto \( U \). So you cannot detect codimension by comparing \( U \) with \( V \) up to isomorphism, and the formula \( \codim U = \dim V - \dim U \) must never be used outside finite dimension. Always compute \( \dim(V/U) \), or count equations.
:::

Hyperplanes are exactly the subspaces cut out by **one** non-trivial linear equation. In \( F^n \) this is familiar: \( a_1x_1 + \dots + a_nx_n = 0 \) with the \( a_i \) not all zero defines a subspace of dimension \( n - 1 \). The quotient makes the statement true in every dimension.

::: {#thm-hyperplane-kernel-functional}
[Hyperplanes Are Kernels of Functionals]

Let \( V \) be a vector space over \( F \), of any dimension, and let \( H \) be a subspace of \( V \). Then \( H \) is a hyperplane if and only if \( H = \ker \varphi \) for some **non-zero** \( \varphi \in V^{*} \).
:::

::: {.idea}
A non-zero functional maps onto the one-dimensional space \( F \), so the First Isomorphism Theorem makes \( V/\ker\varphi \) one-dimensional. Conversely, if \( V/H \) is one-dimensional, it "is" \( F \) after choosing an isomorphism, and composing that isomorphism with \( \pi \) gives a functional whose kernel is \( H \).
:::

::: {.proof}
(⇐) Suppose \( \varphi \in V^{*} \) is non-zero. Then \( \im \varphi \) is a subspace of \( F \) (@thm-prop-image) containing a non-zero scalar, so \( \dim \im\varphi = 1 = \dim F \), and \( \im \varphi = F \) by @thm-dim-impl-eq. By @thm-first-isomorphism, \( V/\ker\varphi \cong F \), so \( \dim(V/\ker\varphi) = 1 \), and \( \ker\varphi \) is a hyperplane.

(⇒) Suppose \( \dim(V/H) = 1 \). By @thm-isomorphic-iff-same-dimension there is an isomorphism \( \theta \colon V/H \to F \). Let \( \varphi = \theta \circ \pi \), where \( \pi \colon V \to V/H \) is the quotient map. It is linear as a composition of linear maps (@thm-composition-linear), so \( \varphi \in V^{*} \). For \( \v \in V \), \( \varphi(\v) = 0 \) means \( \theta(\v + H) = 0 \), which holds exactly when \( \v + H \) is the zero coset, since \( \theta \) is injective; and \( \v + H = H \) means \( \v \in H \) by @lem-coset-equality (b). So \( \ker\varphi = H \). Finally \( \varphi \ne 0 \): since \( V/H \ne \{\0\} \), we have \( H \ne V \), so some \( \v \notin H = \ker\varphi \).
:::

The functional is not unique, but almost: two functionals with the same kernel are scalar multiples of each other (@exr-linear-functionals-c1; @exr-duality-subspaces-quotients-b2 gives a second proof). So hyperplanes of \( V \) correspond to non-zero functionals **up to a non-zero scalar**, just as the plane \( x + y + z = 0 \) is also \( 2x + 2y + 2z = 0 \).

A hyperplane together with any one vector outside it fills the space.

::: {.remark}
Let \( H = \ker\varphi \) be a hyperplane and \( \v_0 \notin H \). Then \( V = H \oplus \Span(\v_0) \). Indeed \( \varphi(\v_0) \ne 0 \), and every \( \v \in V \) splits as
\[
\v = \Big( \v - \tfrac{\varphi(\v)}{\varphi(\v_0)}\,\v_0 \Big) + \tfrac{\varphi(\v)}{\varphi(\v_0)}\,\v_0 ,
\]
where the first bracket lies in \( \ker\varphi \) because \( \varphi \) of it is \( \varphi(\v) - \varphi(\v) = 0 \). And \( H \cap \Span(\v_0) = \{\0\} \), since \( \varphi(c\v_0) = c\varphi(\v_0) = 0 \) forces \( c = 0 \).
:::

::: {.check}
Decide which of the following are hyperplanes, and for each hyperplane give a non-zero functional with that kernel.

::: {.enumerate options="label=(\alph*)"}
1. The symmetric matrices in \( M_2(F) \).
2. The symmetric matrices in \( M_3(F) \).
3. \( \{ p \in F[x] : p(1) = 0 \} \) in \( F[x] \).
:::
:::

::: {.solution}
(a) Yes. \( \A \) is symmetric exactly when \( a_{12} - a_{21} = 0 \), so the symmetric matrices are the kernel of \( \A \mapsto a_{12} - a_{21} \), which is linear and non-zero (it takes the value \( 1 \) at \( \E_{12} \)). By @thm-hyperplane-kernel-functional this is a hyperplane.

(b) No. The symmetric \( 3 \times 3 \) matrices form a subspace of dimension \( 6 \) (choose the entries on and above the diagonal freely), so the codimension is \( 9 - 6 = 3 \ne 1 \).

(c) Yes. It is the kernel of \( p \mapsto p(1) \), which is linear (@thm-evaluation-respects-operations) and non-zero (it sends the constant \( 1 \) to \( 1 \)).
:::

## Exercises

### A. Check your understanding

::: {#exr-duality-subspaces-quotients-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the theorem identifying \( (V/U)^{*} \) with a subspace of \( V^{*} \), including the map.
2. Define the codimension of a subspace, and define a hyperplane.
3. True or false: \( U^{*} \) is a subspace of \( V^{*} \). Justify your answer.
4. Let \( U \) be a subspace of dimension \( 2 \) in \( F^5 \). Find \( \dim (F^5/U)^{*} \) and \( \codim U \).
5. Is \( \{ (x_1, x_2, x_3, x_4) \in \nR^4 : x_1 = x_2 = 0 \} \) a hyperplane in \( \nR^4 \)? Justify your answer.
6. True or false: every non-zero linear functional \( \varphi \colon V \to F \) is surjective. Justify your answer.
:::
:::

::: {.solution}
(a) For a subspace \( U \) of \( V \) with quotient map \( \pi \), the dual map \( \pi' \colon (V/U)^{*} \to V^{*} \), \( \psi \mapsto \psi \circ \pi \), is injective with image \( U^{0} \); so \( (V/U)^{*} \cong U^{0} \) (@thm-dual-of-quotient).

(b) If \( V/U \) is finite-dimensional, \( \codim U = \dim(V/U) \); otherwise \( U \) has infinite codimension. A hyperplane is a subspace of codimension exactly \( 1 \).

(c) False. Elements of \( U^{*} \) are defined only on \( U \), so they are not elements of \( V^{*} \). What is true is \( U^{*} \cong V^{*}/U^{0} \), a quotient (@thm-dual-of-subspace).

(d) \( \dim(F^5/U)^{*} = \dim(F^5/U) = 5 - 2 = 3 \), by @cor-dimension-dual-space and @thm-dimension-quotient. So \( \codim U = 3 \).

(e) No. The subspace is \( \Span(\e_3, \e_4) \), of dimension 2, so its codimension is \( 4 - 2 = 2 \).

(f) True, in any dimension. This is @prp-nonzero-functional-surjective: \( \im\varphi \) is a subspace of the one-dimensional space \( F \) containing a non-zero element, so it is \( F \).
:::

### B. Practice

::: {#exr-duality-subspaces-quotients-b1}
[B1: The dual of a quotient of \( \nR^4 \)]

Let \( U = \Span((1, -1, 0, 2), (0, 1, 1, -1)) \subseteq \nR^4 \), and write functionals on \( \nR^4 \) as \( a_1x_1 + a_2x_2 + a_3x_3 + a_4x_4 \).

::: {.enumerate options="label=(\alph*)"}
1. Find a basis \( (\varphi_1, \varphi_2) \) of \( U^{0} \).
2. Let \( \psi_1, \psi_2 \in (\nR^4/U)^{*} \) be the functionals with \( \pi'(\psi_i) = \varphi_i \). Compute \( \psi_1 \) and \( \psi_2 \) at the coset \( (2, 0, 1, 3) + U \).
3. Find a basis of \( \nR^4/U \) whose dual basis is \( (\psi_1, \psi_2) \).
:::
:::

::: {.solution}
(a) A functional lies in \( U^{0} \) exactly when it vanishes at both spanning vectors (@thm-annihilator-properties (b)), that is,
\[
a_1 - a_2 + 2a_4 = 0, \qquad a_2 + a_3 - a_4 = 0 .
\]
The second gives \( a_3 = a_4 - a_2 \), and the first gives \( a_1 = a_2 - 2a_4 \). Taking \( (a_2, a_4) = (1, 0) \) and \( (-1, -1) \) gives \( (1, 1, -1, 0) \) and \( (1, -1, 0, -1) \), that is,
\[
\varphi_1 = x_1 + x_2 - x_3, \qquad \varphi_2 = x_1 - x_2 - x_4 .
\]
Check: \( \varphi_1(1, -1, 0, 2) = 0 \), \( \varphi_1(0, 1, 1, -1) = 0 \), \( \varphi_2(1, -1, 0, 2) = 1 + 1 - 2 = 0 \), \( \varphi_2(0, 1, 1, -1) = -1 + 1 = 0 \). They are independent (compare the coefficients of \( x_3 \) and \( x_4 \)). The spanning vectors of \( U \) are independent (compare first entries, then second), so \( \dim U^{0} = 4 - 2 = 2 \) by @thm-dimension-annihilator, and \( (\varphi_1, \varphi_2) \) is a basis by @thm-right-size-basis.

(b) By @thm-dual-of-quotient, \( \psi_i(\v + U) = \varphi_i(\v) \). So \( \psi_1((2, 0, 1, 3) + U) = 2 + 0 - 1 = 1 \) and \( \psi_2((2, 0, 1, 3) + U) = 2 - 0 - 3 = -1 \).

(c) We need cosets \( \c_1, \c_2 \) with \( \psi_i(\c_j) = \delta_{ij} \). The vector \( -\e_3 \) has \( \varphi_1(-\e_3) = 1 \) and \( \varphi_2(-\e_3) = 0 \), and \( -\e_4 \) has \( \varphi_1(-\e_4) = 0 \), \( \varphi_2(-\e_4) = 1 \). Put \( \c_1 = -\e_3 + U \) and \( \c_2 = -\e_4 + U \). If \( a\c_1 + b\c_2 = \0 \), applying \( \psi_1 \) and \( \psi_2 \) gives \( a = 0 \) and \( b = 0 \); so \( (\c_1, \c_2) \) is independent, and since \( \dim(\nR^4/U) = 2 \) it is a basis (@thm-right-size-basis). By construction \( \psi_i(\c_j) = \delta_{ij} \), so \( (\psi_1, \psi_2) \) is its dual basis (@thm-dual-basis).
:::

::: {#exr-duality-subspaces-quotients-b2}
[B2: Functionals with the same kernel]

Let \( V \) be a vector space over \( F \), of any dimension, and let \( \varphi, \psi \in V^{*} \) be non-zero. Prove that \( \ker\varphi = \ker\psi \) if and only if \( \psi = c\varphi \) for some non-zero \( c \in F \). (@exr-linear-functionals-c1 proved (⇒) by a different route; here use the hyperplane decomposition.)

*Hint: the remark after @thm-hyperplane-kernel-functional.*
:::

::: {.solution}
(⇐) If \( \psi = c\varphi \) with \( c \ne 0 \), then \( \psi(\v) = 0 \) if and only if \( c\varphi(\v) = 0 \), if and only if \( \varphi(\v) = 0 \), since \( c \) is invertible. So \( \ker\psi = \ker\varphi \).

(⇒) Suppose \( \ker\varphi = \ker\psi = H \). Since \( \varphi \ne 0 \), choose \( \v_0 \) with \( \varphi(\v_0) \ne 0 \); then \( \v_0 \notin H \), so also \( \psi(\v_0) \ne 0 \). Put \( c = \psi(\v_0)/\varphi(\v_0) \), which is non-zero, and \( \chi = \psi - c\varphi \in V^{*} \). Then \( \chi \) vanishes on \( H \), because both \( \psi \) and \( \varphi \) do, and \( \chi(\v_0) = \psi(\v_0) - c\varphi(\v_0) = 0 \). By @thm-hyperplane-kernel-functional \( H \) is a hyperplane, and by the remark after it \( V = H \oplus \Span(\v_0) \). A linear map vanishing on \( H \) and on \( \v_0 \) vanishes on every \( \h + a\v_0 \), hence on \( V \). So \( \chi = 0 \), that is, \( \psi = c\varphi \).
:::

::: {#exr-duality-subspaces-quotients-b3}
[B3: Dimension computations]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \dim V = 7 \) and \( \dim U = 3 \). Find \( \dim U^{*} \), \( \dim(V^{*}/U^{0}) \), \( \dim(V/U)^{*} \) and \( \codim U \).
2. In \( V = F[x]_{\le 3} \), let \( U = \{ p : p(0) = p(1) = 0 \} \). Using the map \( T \colon V \to F^2 \), \( T(p) = (p(0), p(1)) \), find \( \codim U \) and \( \dim U \), and write \( U \) as an intersection of two hyperplanes.
3. Hence find a basis of \( U^{0} \) consisting of evaluation functionals.
:::
:::

::: {.solution}
(a) \( \dim U^{*} = 3 \) by @cor-dimension-dual-space. \( \dim U^{0} = 7 - 3 = 4 \) by @thm-dimension-annihilator, so \( \dim(V^{*}/U^{0}) = 7 - 4 = 3 \) (@thm-dimension-quotient), consistent with @thm-dual-of-subspace. \( \dim(V/U)^{*} = \dim(V/U) = 4 \), consistent with @thm-dual-of-quotient, and \( \codim U = 4 \).

(b) \( T \) is linear because evaluation is (@thm-evaluation-respects-operations), and \( \ker T = U \). It is surjective: \( T(1) = (1, 1) \) and \( T(x) = (0, 1) \) span \( F^2 \). By @thm-first-isomorphism, \( V/U \cong F^2 \), so \( \codim U = 2 \), and \( \dim U = 4 - 2 = 2 \) by @thm-dimension-quotient. Writing \( \varepsilon_0(p) = p(0) \) and \( \varepsilon_1(p) = p(1) \), we have \( U = \ker\varepsilon_0 \cap \ker\varepsilon_1 \), and both kernels are hyperplanes by @thm-hyperplane-kernel-functional, since both functionals send \( 1 \) to \( 1 \).

(c) Both \( \varepsilon_0 \) and \( \varepsilon_1 \) lie in \( U^{0} \). They are independent: if \( a\varepsilon_0 + b\varepsilon_1 = 0 \), evaluating at \( x \) gives \( b = 0 \), and then evaluating at \( 1 \) gives \( a = 0 \). Since \( \dim U^{0} = 4 - 2 = 2 \), \( (\varepsilon_0, \varepsilon_1) \) is a basis of \( U^{0} \) (@thm-right-size-basis).
:::

### C. Going deeper

::: {#exr-duality-subspaces-quotients-c1}
[C1: Subspaces of finite codimension are intersections of hyperplanes]

Let \( V \) be a vector space over \( F \), of any dimension, and let \( U \) be a subspace of finite codimension \( k \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that there are non-zero \( \varphi_1, \dots, \varphi_k \in U^{0} \) with \( U = \ker\varphi_1 \cap \dots \cap \ker\varphi_k \). Deduce that \( U \) is an intersection of \( k \) hyperplanes.
2. Prove that \( U \) is not an intersection of fewer than \( k \) hyperplanes.
:::

*Hint: for (a), take a dual basis of \( (V/U)^{*} \); for (b), consider the map \( V \to F^m \), \( \v \mapsto (\varphi_1(\v), \dots, \varphi_m(\v)) \).*
:::

::: {.solution}
(a) Let \( \pi \colon V \to V/U \) be the quotient map. Since \( \dim(V/U) = k \), choose a basis \( (\c_1, \dots, \c_k) \) of \( V/U \) and let \( (\psi_1, \dots, \psi_k) \) be its dual basis (@thm-dual-basis). Put \( \varphi_i = \psi_i \circ \pi \). By @thm-dual-of-quotient, \( \varphi_i \in U^{0} \), and \( \varphi_i \ne 0 \) because \( \pi' \) is injective and \( \psi_i \ne 0 \).

Since each \( \varphi_i \) lies in \( U^{0} \), \( U \subseteq \ker\varphi_i \) for each \( i \). Conversely, let \( \v \in \ker\varphi_1 \cap \dots \cap \ker\varphi_k \), and write \( \v + U = \sum_j a_j\c_j \). Applying \( \psi_i \) gives \( a_i = \psi_i(\v + U) = \varphi_i(\v) = 0 \) for every \( i \). So \( \v + U \) is the zero coset, and \( \v \in U \) by @lem-coset-equality (b). This proves \( U = \bigcap_i \ker\varphi_i \). Each \( \ker\varphi_i \) is a hyperplane by @thm-hyperplane-kernel-functional.

(b) Suppose \( U = H_1 \cap \dots \cap H_m \) with hyperplanes \( H_i \). By @thm-hyperplane-kernel-functional, \( H_i = \ker\varphi_i \) for non-zero \( \varphi_i \in V^{*} \). The map \( S \colon V \to F^m \), \( S(\v) = (\varphi_1(\v), \dots, \varphi_m(\v)) \), is linear, since each entry is, and \( \ker S = \bigcap_i \ker\varphi_i = U \). By @thm-first-isomorphism, \( V/U \cong \im S \), a subspace of \( F^m \). Hence \( k = \dim(V/U) = \dim \im S \le m \) by @thm-subspace-dimension. So at least \( k \) hyperplanes are needed.
:::

::: {#exr-duality-subspaces-quotients-c2}
[C2: Complements and a choice of copy of \( U^{*} \)]

Let \( V \) be finite-dimensional, and let \( U, W \) be subspaces with \( V = U \oplus W \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( V^{*} = U^{0} \oplus W^{0} \) without using @thm-annihilator-properties (d). (This is @exr-annihilators-c3 (a), which used it.)
2. Deduce that the restriction map \( \rho \colon V^{*} \to U^{*} \) restricts to an isomorphism \( W^{0} \to U^{*} \).
3. In \( \nR^2 \), let \( U = \Span(\e_1) \), \( W_1 = \Span(\e_2) \) and \( W_2 = \Span((1, 1)) \). Find \( W_1^{0} \) and \( W_2^{0} \), and find the element of each that restricts to the functional \( \xi \in U^{*} \) with \( \xi(\e_1) = 1 \). Conclude that the copy of \( U^{*} \) inside \( V^{*} \) depends on the complement.
:::
:::

::: {.solution}
(a) Let \( n = \dim V \). If \( \varphi \in U^{0} \cap W^{0} \), then \( \varphi \) vanishes on \( U \) and on \( W \), hence on every \( \u + \w \), that is, on \( U + W = V \); so \( \varphi = 0 \). By @thm-dimension-annihilator, \( \dim U^{0} + \dim W^{0} = (n - \dim U) + (n - \dim W) = 2n - n = n \), using \( \dim U + \dim W = n \) for a direct sum (@thm-direct-sum-criteria). By @thm-dimension-formula-subspace-dim, \( \dim(U^{0} + W^{0}) = n - 0 = n = \dim V^{*} \), so \( U^{0} + W^{0} = V^{*} \) (@thm-dim-impl-eq), and the sum is direct because the intersection is \( \{0\} \).

(b) The restriction of \( \rho \) to \( W^{0} \) is linear. Its kernel is \( W^{0} \cap \ker\rho = W^{0} \cap U^{0} = \{0\} \) by @thm-dual-of-subspace and (a), so it is injective. Its domain has dimension \( n - \dim W = \dim U = \dim U^{*} \). An injective linear map between spaces of the same finite dimension is an isomorphism (@cor-rank-nullity-consequences (e)).

(c) Write functionals on \( \nR^2 \) as \( ax + by \). \( W_1^{0} \) consists of those with \( b = 0 \), so \( W_1^{0} = \Span(x) \). \( W_2^{0} \) consists of those with \( a + b = 0 \), so \( W_2^{0} = \Span(x - y) \). Restricting to \( U \): \( x|_U \) and \( (x - y)|_U \) both take the value \( 1 \) at \( \e_1 \), so both equal \( \xi \). The elements \( x \) and \( x - y \) are different, so the subspaces \( W_1^{0} \ne W_2^{0} \) of \( V^{*} \) are two different copies of \( U^{*} \), one for each complement.
:::
