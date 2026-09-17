# Invertible Maps and Isomorphisms

In Chapter 1 we noticed that a basis of length \( n \) turns every vector of \( V \) into a column in \( F^n \), and that sums and multiples survive the translation. Then \( \nR[x]_{\le 2} \) and \( \nR^3 \) behave "the same", although they are different sets. This section makes "the same" precise. We define invertible linear maps and isomorphisms, prove that finite-dimensional spaces are classified by one number, their dimension, and collect everything we know about invertibility of an operator into one theorem.

## When are two spaces the same?

The naive notion of sameness is equality of sets, and it fails at once. The polynomial \( 3 - x + 2x^2 \) is not a column vector, so \( \nR[x]_{\le 2} \neq \nR^3 \). Yet every computation in one space has a twin in the other. Match \( a_0 + a_1x + a_2x^2 \) with \( (a_0, a_1, a_2) \):
\[
(1 + 2x) + (x - x^2) = 1 + 3x - x^2 \quad \longleftrightarrow \quad (1, 2, 0) + (0, 1, -1) = (1, 3, -1).
\]
A reader who only sees one side cannot tell which space the computation happened in. Three features make this work. The matching is **one-to-one** and **onto**, so nothing is lost or left over. It **respects sums and multiples** in the direction polynomial → column. And it respects them in the **reverse** direction too, so a conclusion drawn among columns can be carried back. In the language of this chapter: a linear map with a linear map going back.

*An isomorphism is a perfect dictionary between two vector spaces: every word has exactly one translation, and translating respects sums and scalar multiples in both directions.*

::: {#def-invertible-linear-map}
[Invertible Linear Map]

Let \( V \) and \( W \) be vector spaces over \( F \), and let \( T \in \cL(V, W) \). Then \( T \) is **invertible** if there **exists a linear** map \( S \in \cL(W, V) \) such that
\[
ST = \id_V \qquad \textbf{and} \qquad TS = \id_W .
\]
:::

In words: \( S \) undoes \( T \) on \( V \) (first \( T \), then \( S \), and we are back where we started), \( T \) undoes \( S \) on \( W \), and the undoing map is itself linear. The definition asks for **one** map \( S \) doing **both** jobs.

**Well-definedness.** If \( S \) exists, it is an inverse **function** of \( T \) in the sense of @def-inverse-function, and inverse functions are unique by @thm-bijective-iff-invertible. So we may speak of **the** inverse and write \( T^{-1} \coloneqq S \). The same theorem says an invertible \( T \) is a bijection.

Is the word "linear" in the definition doing any work? One could imagine a linear bijection whose inverse function is not linear, which would then fail the definition. It turns out this never happens:

::: {#thm-inverse-is-linear}
[The Inverse of a Linear Bijection Is Linear]

Let \( T \in \cL(V, W) \) be bijective. Then its inverse function \( T^{-1} \colon W \to V \) is linear. Consequently, a linear map \( T \) is invertible if and only if it is bijective.
:::

::: {.idea}
To show \( T^{-1}(\w_1 + \w_2) = T^{-1}\w_1 + T^{-1}\w_2 \), we cannot compute \( T^{-1} \) directly. But we can apply \( T \), which we know is linear, to the right-hand side, and see that it lands on \( \w_1 + \w_2 \). Since \( T \) is injective, only one vector does that, namely \( T^{-1}(\w_1 + \w_2) \).
:::

::: {.proof}
Let \( \w_1, \w_2 \in W \) and \( c \in F \), and put \( \v_i \coloneqq T^{-1}\w_i \), so that \( T\v_i = \w_i \). Since \( T \) is linear,
\[
T(\v_1 + \v_2) = \w_1 + \w_2, \qquad T(c\v_1) = c\w_1 .
\]
Applying \( T^{-1} \) to both equations gives \( T^{-1}(\w_1 + \w_2) = \v_1 + \v_2 = T^{-1}\w_1 + T^{-1}\w_2 \) and \( T^{-1}(c\w_1) = c\v_1 = c\,T^{-1}\w_1 \). Hence \( T^{-1} \) is linear.

For the last statement: if \( T \) is invertible, it is bijective by @thm-bijective-iff-invertible. Conversely, if \( T \) is bijective, its inverse function \( S = T^{-1} \) satisfies \( ST = \id_V \) and \( TS = \id_W \) by @def-inverse-function, and \( S \) is linear by the first part. So \( T \) is invertible. This proves the theorem.
:::

So in practice we check invertibility by checking **bijectivity**, and never need to verify linearity of the inverse. Invertible linear maps are important enough to have a second name.

::: {#def-isomorphism}
[Isomorphism]

Let \( V \) and \( W \) be vector spaces over **the same field** \( F \). An **isomorphism** from \( V \) to \( W \) is an invertible linear map \( T \in \cL(V, W) \); equivalently, by @thm-inverse-is-linear, a **bijective** linear map.
:::

::: {#def-isomorphic}
[Isomorphic Spaces]

Vector spaces \( V \) and \( W \) over \( F \) are **isomorphic**, written \( V \cong W \), if there **exists an** isomorphism \( V \to W \).
:::

In words: \( V \cong W \) says that **some** perfect dictionary exists; it does not name one. The name comes from Greek *isos* (equal) and *morphe* (form): the two spaces have the same form, though not the same elements. An isomorphism \( V \to V \) is also called an **invertible operator**.

::: {#exm-standard-isomorphisms}
[The Standard Isomorphisms]

Show that each map is an isomorphism, and give its inverse.

::: {.enumerate options="label=(\alph*)"}
1. \( \Phi \colon \nR[x]_{\le n} \to \nR^{n+1} \), \( a_0 + a_1x + \dots + a_nx^n \mapsto (a_0, a_1, \dots, a_n) \).
2. \( \Psi \colon M_{m \times n}(F) \to F^{mn} \), which lists the entries row by row: \( (a_{ij}) \mapsto (a_{11}, \dots, a_{1n}, a_{21}, \dots, a_{mn}) \).
3. \( \Theta \colon \nC \to \nR^2 \), \( a + bi \mapsto (a, b) \), where \( \nC \) is a vector space **over \( \nR \)**.
4. \( T_A \colon F^n \to F^n \), \( \x \mapsto A\x \), for an invertible \( A \in M_n(F) \); and \( \id_V \) for any \( V \).
:::
:::

::: {.solution}
(a) *Linear.* Polynomials are added and scaled coefficient by coefficient, and so are columns, so \( \Phi(p + q) = \Phi(p) + \Phi(q) \) and \( \Phi(cp) = c\,\Phi(p) \). *Bijective.* The map \( (a_0, \dots, a_n) \mapsto a_0 + a_1x + \dots + a_nx^n \) is a two-sided inverse function, because two polynomials are equal exactly when all their coefficients agree (@def-polynomial). By @thm-inverse-is-linear, \( \Phi \) is an isomorphism, and \( \Phi^{-1} \) is that map. Hence \( \nR[x]_{\le n} \cong \nR^{n+1} \).

(b) Matrices are added and scaled entrywise, and so are vectors of \( F^{mn} \), so \( \Psi \) is linear. The map that writes the first \( n \) entries of a vector into row 1, the next \( n \) into row 2, and so on, undoes \( \Psi \) on both sides. Hence \( M_{m \times n}(F) \cong F^{mn} \).

(c) For \( a, b, a', b', c \in \nR \): \( (a + bi) + (a' + b'i) = (a + a') + (b + b')i \) and \( c(a + bi) = ca + cbi \), so \( \Theta \) is linear over \( \nR \). Every complex number has unique real and imaginary parts (@def-complex-numbers), so \( (a, b) \mapsto a + bi \) is a two-sided inverse. Hence \( \nC \cong \nR^2 \) **as real vector spaces**. In the same way @exm-complexification-rn showed that \( (\x, \y) \mapsto \x + i\y \) is a bijection \( (\nR^n)_\nC \to \nC^n \) respecting complex scalars; in our new language, \( (\nR^n)_\nC \cong \nC^n \) over \( \nC \).

(d) \( T_A \) is linear (@exm-matrix-transformation). Since \( A(A^{-1}\x) = (AA^{-1})\x = \x \) and \( A^{-1}(A\x) = \x \) by @thm-matrix-multiplication-properties, the linear map \( T_{A^{-1}} \) is a two-sided inverse: \( T_A^{-1} = T_{A^{-1}} \). The identity \( \id_V \) is its own inverse. This degenerate example matters: it shows \( V \cong V \), and even the zero space is isomorphic to itself, via the zero map \( \{\0\} \to \{\0\} \), which is \( \id_{\{\0\}} \).
:::

Here is a non-example by minimal change. Take (a) with \( n = 3 \), but keep only three coefficients: \( \Phi' \colon \nR[x]_{\le 3} \to \nR^3 \), \( a_0 + a_1x + a_2x^2 + a_3x^3 \mapsto (a_0, a_1, a_2) \). It is still linear, and still onto, since \( (a_0, a_1, a_2) = \Phi'(a_0 + a_1x + a_2x^2) \). But \( \Phi'(x^3) = \0 = \Phi'(0) \), so \( \Phi' \) is **not injective**. No \( S \) can satisfy \( S\Phi' = \id \), because \( S\Phi'(x^3) = S(\0) = 0 \neq x^3 \). The clause \( ST = \id_V \) is the one that fails.

**Why this definition.** Could we drop one of the two equations? The next example says no.

::: {#exm-differentiation-integration-one-sided}
[One Equation Is Not Enough]

On \( \nR[x] \), let \( D \) be differentiation and \( J(p) \coloneqq \int_0^x p(t)\,\dd t \), so that \( J(x^k) = \frac{x^{k+1}}{k+1} \) (@exm-differentiation, @exm-integration). On the sequence space \( F^{\nN} \), let \( L(a_0, a_1, a_2, \dots) \coloneqq (a_1, a_2, a_3, \dots) \) and \( R(a_0, a_1, a_2, \dots) \coloneqq (0, a_0, a_1, \dots) \) be the left and right shifts of @exm-shift. Show that \( DJ = \id \) and \( LR = \id \), but that none of \( D, J, L, R \) is invertible.
:::

::: {.solution}
All four maps are linear, by @exm-differentiation, @exm-integration and @exm-shift. For each \( k \in \nN \), \( DJ(x^k) = D\bigl(\tfrac{x^{k+1}}{k+1}\bigr) = x^k \), so \( DJ \) and \( \id \) agree on every \( x^k \). Every polynomial is a finite combination of the \( x^k \), so \( DJ = \id \) by @thm-linear-combination. Directly, \( LR(a_0, a_1, \dots) = L(0, a_0, a_1, \dots) = (a_0, a_1, \dots) \), so \( LR = \id \).

But \( JD(1) = J(0) = 0 \neq 1 \), and \( RL(1, 0, 0, \dots) = R(0, 0, \dots) = \0 \). In fact \( D(1) = 0 = D(0) \) and \( L(1, 0, 0, \dots) = \0 = L(\0) \), so \( D \) and \( L \) are not injective; and \( 1 \notin \im J \) (every \( J(p) \) has constant coefficient \( 0 \)) and \( (1, 0, 0, \dots) \notin \im R \), so \( J \) and \( R \) are not surjective. None of the four is bijective, so none is invertible (@thm-inverse-is-linear).
:::

So a one-sided inverse can exist without invertibility. The spaces here are infinite-dimensional, and that is not an accident: later in this section we prove that in finite dimension one equation does imply the other.

::: {.warning}
**Isomorphic is not equal, and an isomorphism is a choice.** \( \nR[x]_{\le 2} \cong \nR^3 \) does not make a polynomial a column. Worse, there are many isomorphisms, and none is singled out. The coefficient map of @exm-standard-isomorphisms sends \( x \) to \( (0, 1, 0) \). The coordinate map for the basis \( (1, 1 + x, 1 + x + x^2) \) of @exm-polynomial-coordinates is also an isomorphism (we prove this below), and it sends \( x = -1 \cdot 1 + 1 \cdot (1 + x) \) to \( (-1, 1, 0) \). A general \( n \)-dimensional space has no "standard" basis, so there is no natural isomorphism \( F^n \to V \); every one depends on a choice. Chapter 4 returns to this point with dual spaces.
:::

The first payoff of the definition is that an isomorphism carries all linear structure across, in both directions. We record the two facts we need.

::: {#thm-isomorphism-preserves-bases}
[Isomorphisms Carry Bases to Bases]

Let \( T \colon V \to W \) be an isomorphism, and let \( (\v_1, \dots, \v_n) \) be a basis of \( V \). Then \( (T\v_1, \dots, T\v_n) \) is a basis of \( W \).
:::

::: {.proof}
Since \( T \) is injective, the list \( (T\v_1, \dots, T\v_n) \) is linearly independent by @thm-injective-preserves-independence. By @thm-image-spanned-by-basis-images, it spans \( \im T \), and \( \im T = W \) because \( T \) is surjective. Hence it is a basis of \( W \).
:::

::: {#thm-isomorphic-equivalence-relation}
[Isomorphism Is an Equivalence Relation]

For vector spaces over \( F \): \( V \cong V \); if \( V \cong W \) then \( W \cong V \); and if \( U \cong V \) and \( V \cong W \) then \( U \cong W \).
:::

::: {.proof}
\( \id_V \) is an isomorphism (@exm-standard-isomorphisms (d)). If \( T \colon V \to W \) is an isomorphism, then \( T^{-1} \) is linear (@thm-inverse-is-linear) and has inverse \( T \), so it is an isomorphism \( W \to V \). If \( T \colon U \to V \) and \( S \colon V \to W \) are isomorphisms, then \( ST \) is linear by @thm-composition-linear and bijective by @thm-composition-preserves, hence an isomorphism by @thm-inverse-is-linear, with \( (ST)^{-1} = T^{-1}S^{-1} \) by @thm-inverse-of-composition. This proves the theorem.
:::

So \( \cong \) sorts vector spaces over \( F \) into classes (@def-equivalence-relation). The next question is which spaces land in the same class.

## Classification by dimension

By @thm-isomorphism-preserves-bases, isomorphic spaces have bases of the same length. Is that the **only** obstruction? Two spaces of dimension \( 6 \), say \( M_{2 \times 3}(\nR) \) and \( \nR[x]_{\le 5} \), look nothing alike. The following theorem says that this does not matter: for finite-dimensional spaces, dimension is a **complete invariant**.

::: {#thm-isomorphic-iff-same-dimension}
[Classification of Finite-Dimensional Spaces]

Let \( V \) and \( W \) be finite-dimensional vector spaces over the same field \( F \). Then
\[
V \cong W \quad \iff \quad \dim V = \dim W .
\]
:::

::: {.idea}
(⇒) is the payoff we just proved: an isomorphism moves a basis to a basis of the same length. For (⇐) we must **build** an isomorphism, and the only material we have is a basis on each side, \( (\v_1, \dots, \v_n) \) and \( (\w_1, \dots, \w_n) \). The obvious dictionary sends \( \v_i \) to \( \w_i \). Linear maps can be prescribed freely on a basis, so this defines \( T \), and the reverse prescription defines \( S \). To see \( ST = \id_V \) we do not compute: both sides are linear and agree on the basis, so they are equal. The hypothesis "same dimension" is exactly what makes the two bases the same length, so that "\( \v_i \mapsto \w_i \)" makes sense.
:::

::: {.proof}
(⇒) Suppose \( T \colon V \to W \) is an isomorphism, and let \( (\v_1, \dots, \v_n) \) be a basis of \( V \), with \( n = \dim V \) (@cor-basis-existence). By @thm-isomorphism-preserves-bases, \( (T\v_1, \dots, T\v_n) \) is a basis of \( W \), so \( \dim W = n = \dim V \).

(⇐) Suppose \( \dim V = \dim W = n \), and choose bases \( (\v_1, \dots, \v_n) \) of \( V \) and \( (\w_1, \dots, \w_n) \) of \( W \) (@cor-basis-existence). By @thm-linear-transform-basis there are linear maps \( T \in \cL(V, W) \) with \( T\v_i = \w_i \) and \( S \in \cL(W, V) \) with \( S\w_i = \v_i \), for \( i = 1, \dots, n \). Then \( ST \in \cL(V) \) is linear (@thm-composition-linear) and \( ST\v_i = S\w_i = \v_i = \id_V\v_i \) for every \( i \). Two linear maps that agree on a basis are equal, by the uniqueness part of @thm-linear-transform-basis, so \( ST = \id_V \). Swapping the roles of \( V \) and \( W \) gives \( TS = \id_W \). Hence \( T \) is invertible, and \( V \cong W \). This proves the theorem.
:::

The theorem needs both spaces to be over the **same** field; this is part of @def-isomorphic. \( \nC \) over \( \nC \) has dimension \( 1 \) and \( \nR \) over \( \nR \) has dimension \( 1 \), but the question "is \( \nC \cong \nR \)?" makes no sense, since a linear map must respect one common set of scalars.

Taking \( W = F^n \) with its standard basis, the proof builds a specific isomorphism \( V \to F^n \): the one sending \( \v_i \) to \( \e_i \). It is an old friend.

::: {#cor-coordinate-isomorphism}
[The Coordinate Isomorphism]

Let \( \sB = (\v_1, \dots, \v_n) \) be a basis of a vector space \( V \) over \( F \). Then the coordinate map
\[
V \to F^n, \qquad \v \mapsto \coord{\v}{\sB}
\]
is an isomorphism, with inverse \( (a_1, \dots, a_n) \mapsto a_1\v_1 + \dots + a_n\v_n \). In particular, every \( n \)-dimensional vector space over \( F \) is isomorphic to \( F^n \).
:::

::: {.proof}
By @thm-coordinates-linear, the coordinate map is linear, and every column \( (a_1, \dots, a_n) \in F^n \) is the coordinate vector of exactly one vector of \( V \), namely \( a_1\v_1 + \dots + a_n\v_n \). So the coordinate map is bijective, with the stated inverse function, and it is an isomorphism by @thm-inverse-is-linear.
:::

This is the promise of Chapter 1 kept: the correspondence \( \v \mapsto \coord{\v}{\sB} \) from @thm-coordinates-linear is an isomorphism. Its practical meaning is the slogan behind the rest of this chapter: **any computation with sums and multiples in an \( n \)-dimensional space can be done with columns in \( F^n \)**, at the price of choosing a basis.

::: {#exm-classify-by-dimension}
[Sorting Spaces by Dimension]

Which of the following real vector spaces are isomorphic to each other?

::: {.enumerate options="label=(\roman*)"}
1. \( \nR[x]_{\le 5} \);
2. \( M_{2 \times 3}(\nR) \);
3. the upper triangular matrices in \( M_3(\nR) \);
4. \( \nC^3 \), regarded as a vector space over \( \nR \);
5. \( U = \{ p \in \nR[x]_{\le 6} : p(1) = 0 \} \);
6. \( \nR^5 \).
:::
:::

::: {.solution}
By @thm-isomorphic-iff-same-dimension it suffices to compute dimensions over \( \nR \).

(i) The basis \( (1, x, \dots, x^5) \) gives dimension \( 6 \). (ii) \( \dim M_{2 \times 3}(\nR) = 2 \cdot 3 = 6 \) (@exm-dimensions). (iii) An upper triangular matrix is \( \sum_{i \le j} a_{ij}E_{ij} \), and this expression is unique because the coefficient of \( E_{ij} \) is the \( (i, j) \)-entry. By @thm-unique-representation the six matrix units \( E_{ij} \) with \( 1 \le i \le j \le 3 \) form a basis, so the dimension is \( 6 \). (iv) \( \dim_\nC \nC^3 = 3 \), so \( \dim_\nR \nC^3 = 6 \) by @thm-restriction-of-scalars-dimension.

(v) The evaluation map \( E \colon \nR[x]_{\le 6} \to \nR \), \( p \mapsto p(1) \), is linear, and surjective because \( E(c) = c \) for each constant \( c \). Its kernel is \( U \). By @thm-rank-nullity, \( \dim U = \dim \nR[x]_{\le 6} - \rank E = 7 - 1 = 6 \).

(vi) \( \dim \nR^5 = 5 \).

Hence the spaces (i)–(v) are all isomorphic to each other (and to \( \nR^6 \)), while \( \nR^5 \) is isomorphic to none of them. We never wrote down an isomorphism between, say, (iii) and (v); the theorem guarantees one.
:::

::: {.check}
Is \( M_2(\nR) \) isomorphic to \( \nR[x]_{\le 3} \)? Is it isomorphic to \( \nR[x]_{\le 4} \)?
:::

::: {.solution}
\( \dim M_2(\nR) = 4 = \dim \nR[x]_{\le 3} \), so \( M_2(\nR) \cong \nR[x]_{\le 3} \) by @thm-isomorphic-iff-same-dimension. But \( \dim \nR[x]_{\le 4} = 5 \neq 4 \) (not \( 4 \): count \( 1, x, x^2, x^3, x^4 \)), so \( M_2(\nR) \not\cong \nR[x]_{\le 4} \).
:::

## One-sided inverses

For square matrices, Chapter 2 proved that one equation is enough: if \( A, B \in M_n(F) \) and \( AB = I_n \), then \( BA = I_n \) (@thm-one-sided-inverse). @exm-differentiation-integration-one-sided shows that this fails for operators on infinite-dimensional spaces. And it fails between spaces of different dimension: for \( T \colon \nR^2 \to \nR^3 \), \( (x, y) \mapsto (x, y, 0) \), and \( S \colon \nR^3 \to \nR^2 \), \( (x, y, z) \mapsto (x, y) \), we have \( ST = \id_{\nR^2} \) but \( TS(0, 0, 1) = \0 \), so \( TS \neq \id_{\nR^3} \). What survives is exactly the case that looks like "square":

::: {#thm-one-sided-inverse-maps}
[One-Sided Inverses of Linear Maps]

Let \( V \) and \( W \) be finite-dimensional vector spaces over \( F \) with \( \dim V = \dim W \). Let \( T \in \cL(V, W) \) and \( S \in \cL(W, V) \). If \( ST = \id_V \), then \( TS = \id_W \). In that case \( T \) and \( S \) are both isomorphisms, \( S = T^{-1} \) and \( T = S^{-1} \).
:::

::: {.idea}
Without any dimension hypothesis, \( ST = \id_V \) already gives half of what we need: \( T \) must be injective, since \( S \) recovers \( \v \) from \( T\v \). The missing half, surjectivity, is exactly what the Rank–Nullity Theorem supplies for free when \( \dim V = \dim W \) is finite. Once \( T \) is known to be invertible, we cancel it: \( S = (ST)T^{-1} = T^{-1} \). So the one hypothesis the infinite-dimensional counterexamples violate, finite equal dimension, is spent on a single line: injective ⇒ surjective.
:::

::: {.proof}
Suppose \( ST = \id_V \), and let \( \v \in \ker T \). Then \( \v = \id_V\v = S(T\v) = S\0 = \0 \), since \( S \) is linear. So \( \ker T = \{\0\} \), and \( T \) is injective by @thm-injective-iff-trivial-kernel. Since \( V \) and \( W \) are finite-dimensional with \( \dim V = \dim W \), @cor-rank-nullity-consequences shows that \( T \) is also surjective. Hence \( T \) is bijective, and by @thm-inverse-is-linear it has a linear inverse \( T^{-1} \in \cL(W, V) \). By @thm-composition-linear (b) and (c),
\[
S = S\,\id_W = S(TT^{-1}) = (ST)T^{-1} = \id_V T^{-1} = T^{-1} .
\]
Therefore \( TS = TT^{-1} = \id_W \). Finally \( S = T^{-1} \) is an isomorphism with inverse \( T \) (@thm-isomorphic-equivalence-relation), so \( T = S^{-1} \). This proves the theorem.
:::

::: {.remark}
Compare the two proofs. For matrices (@thm-one-sided-inverse), the step "\( B\x = \0 \) has only the trivial solution, hence \( B \) is invertible" came from row reduction, through the Invertible Matrix Theorem. Here the same step, "injective, hence bijective", comes from Rank–Nullity, with no matrices at all. Once we can write maps as matrices (next section), the two theorems become the same theorem seen from two sides.
:::

In practice this means: **to verify that \( S \) is the inverse of \( T \) between spaces of the same finite dimension, one composition suffices.** By symmetry, \( TS = \id_W \) also implies \( ST = \id_V \): apply the theorem with the roles of \( T \) and \( S \) (and of \( V \) and \( W \)) swapped.

## The Invertible Operator Theorem

For an operator on a finite-dimensional space, invertibility can now be detected in many different ways. Chapter 2 collected the matrix versions in the Invertible Matrix Theorem (@thm-invertible-tfae), and said the list would grow. Here is its first growth, stated for operators.

::: {#thm-invertible-operator-tfae}
[Invertible Operator Theorem]

Let \( V \) be a **finite-dimensional** vector space over \( F \), and let \( T \in \cL(V) \). The following are equivalent.

::: {.enumerate options="label=(\alph*)"}
1. \( T \) is invertible.
2. \( T \) is injective.
3. \( \ker T = \{\0\} \), that is, \( \nullity T = 0 \).
4. \( T \) is surjective.
5. \( \rank T = \dim V \).
6. There is \( S \in \cL(V) \) with \( ST = \id_V \).
7. There is \( S \in \cL(V) \) with \( TS = \id_V \).
8. \( T \) maps **some** basis of \( V \) to a basis of \( V \).
9. \( T \) maps **every** basis of \( V \) to a basis of \( V \).
:::
:::

::: {.idea}
Nine conditions, but almost every arrow is a citation. The plan:

① the core, (a) ⇔ (b) ⇔ (c) ⇔ (d) ⇔ (e): kernel test for injectivity, Rank–Nullity for "injective ⇔ surjective", equal dimension for "image is everything";

② the one-sided inverses (f), (g): trivially implied by (a), and they imply (a) by @thm-one-sided-inverse-maps with \( W = V \);

③ the bases, (a) ⇒ (i) ⇒ (h) ⇒ (d): isomorphisms carry bases to bases, some basis exists, and an image containing a basis is everything.
:::

::: {.proof}
**(a) ⇒ (b).** An invertible map is bijective (@thm-inverse-is-linear).

**(b) ⇔ (c).** This is @thm-injective-iff-trivial-kernel, and \( \ker T = \{\0\} \) is the same as \( \dim \ker T = 0 \).

**(b) ⇔ (d).** Since \( T \) maps the finite-dimensional space \( V \) to a space of the same dimension, this is @cor-rank-nullity-consequences.

**(d) ⇔ (e).** If \( \im T = V \), then \( \rank T = \dim V \). Conversely, if \( \rank T = \dim V \), then \( \im T \) is a subspace of \( V \) of dimension \( \dim V \), so \( \im T = V \) by @thm-dim-impl-eq.

**(b) and (d) ⇒ (a).** If \( T \) is injective, it is also surjective by (b) ⇒ (d), hence bijective, hence invertible by @thm-inverse-is-linear. Together with the arrows above, (a)–(e) are equivalent.

**(a) ⇒ (f) and (a) ⇒ (g).** Take \( S = T^{-1} \).

**(f) ⇒ (a) and (g) ⇒ (a).** Apply @thm-one-sided-inverse-maps with \( W = V \): if \( ST = \id_V \), then \( T \) is invertible; if \( TS = \id_V \), the same theorem with the roles of \( S \) and \( T \) swapped shows that \( S \) is invertible with \( S^{-1} = T \), so \( T \) is invertible.

**(a) ⇒ (i).** This is @thm-isomorphism-preserves-bases.

**(i) ⇒ (h).** \( V \) has a basis by @cor-basis-existence, and by (i) its image is a basis.

**(h) ⇒ (d).** Let \( (\v_1, \dots, \v_n) \) be a basis whose image \( (T\v_1, \dots, T\v_n) \) is a basis of \( V \). Each \( T\v_i \) lies in the subspace \( \im T \), so \( V = \Span(T\v_1, \dots, T\v_n) \subseteq \im T \) by @thm-span-subspace. Hence \( \im T = V \).

All nine conditions are equivalent. This proves the theorem.
:::

As with the matrix theorem, the list is a menu. To prove that an operator **is** invertible, pick the cheapest item, usually (c): take \( \v \) with \( T\v = \0 \) and show \( \v = \0 \). To prove that it is **not**, exhibit one non-zero vector in the kernel.

::: {#exm-invertible-operator-by-kernel}
[Invertibility Without Solving Equations]

::: {.enumerate options="label=(\alph*)"}
1. Let \( T \in \cL(\nR[x]_{\le 2}) \), \( T(p) = p + xp' \). Show that \( T \) is invertible and find \( T^{-1} \).
2. Let \( V \) be **any** vector space and \( T \in \cL(V) \) with \( T^2 = T + \id_V \). Show that \( T \) is invertible, with \( T^{-1} = T - \id_V \).
:::
:::

::: {.solution}
(a) Let \( p = a + bx + cx^2 \). Then \( xp' = bx + 2cx^2 \), so
\[
T(a + bx + cx^2) = a + 2bx + 3cx^2 .
\]
If \( T(p) = 0 \), then \( a = 2b = 3c = 0 \), so \( a = b = c = 0 \) and \( p = 0 \). Hence \( \ker T = \{0\} \), and \( T \) is invertible by @thm-invertible-operator-tfae ((c) ⇒ (a)). We did not have to check surjectivity: the count did it for us. For the inverse, let \( S(a + bx + cx^2) \coloneqq a + \frac{b}{2}x + \frac{c}{3}x^2 \), which is linear. Then \( TS(a + bx + cx^2) = a + 2 \cdot \frac{b}{2}x + 3 \cdot \frac{c}{3}x^2 = a + bx + cx^2 \), so \( TS = \id \), and by @thm-one-sided-inverse-maps, \( S = T^{-1} \).

(b) The operators \( T \) and \( T - \id_V \) are polynomials in \( T \), so they commute (@thm-polynomial-of-operator-properties (c)). By @thm-composition-linear (d) and the hypothesis,
\[
T(T - \id_V) = T^2 - T = \id_V = (T - \id_V)T .
\]
So \( T - \id_V \) is a two-sided inverse, and \( T \) is invertible by @def-invertible-linear-map. Here \( V \) may be infinite-dimensional, since we verified **both** equations.
:::

::: {.warning}
**The Invertible Operator Theorem needs finite dimension, and it is about operators.** On \( \nR[x] \), differentiation \( D \) is surjective (every polynomial has an antiderivative \( J(p) \)) but not injective, and \( S(p) = xp \) is injective but not surjective (\( 1 \notin \im S \)). And for a map \( T \colon V \to W \) between **different** spaces, "injective" does not give "surjective" unless \( \dim V = \dim W \): the inclusion \( (x, y) \mapsto (x, y, 0) \) of \( \nR^2 \) into \( \nR^3 \) is injective and not surjective.
:::

::: {.check}
Is \( T \in \cL(M_2(\nR)) \), \( T(A) = A + A\tp \), invertible? Use the cheapest item of @thm-invertible-operator-tfae.
:::

::: {.solution}
No. Let \( A = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} \neq 0 \). Then \( A\tp = -A \), so \( T(A) = 0 \), and \( \ker T \neq \{0\} \). Item (c) fails, so \( T \) is not invertible.
:::

Isomorphisms let us move a whole space into \( F^n \). The next section moves **maps** as well: once bases are chosen, every linear map between finite-dimensional spaces becomes a matrix, and composition becomes matrix multiplication.

## Exercises

### A. Check your understanding

::: {#exr-isomorphisms-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define what it means for \( T \in \cL(V, W) \) to be an isomorphism, and what \( V \cong W \) means.
2. True or false: \( \nR[x]_{\le 3} \cong M_2(\nR) \). Justify your answer.
3. True or false: if \( \dim V = \dim W = 5 \) and \( T \in \cL(V, W) \) is injective, then \( T \) is an isomorphism. Justify your answer.
4. True or false: for every vector space \( V \) and all \( S, T \in \cL(V) \), \( ST = \id_V \) implies \( TS = \id_V \). Justify your answer.
5. True or false: if \( V \cong W \), then every linear map \( V \to W \) is an isomorphism. Justify your answer.
6. Which theorem would you use to show that a given operator on a finite-dimensional space is invertible by computing only its kernel?
:::
:::

::: {.solution}
(a) \( T \) is an isomorphism if it is invertible, that is, there is \( S \in \cL(W, V) \) with \( ST = \id_V \) and \( TS = \id_W \); equivalently, \( T \) is a bijective linear map (@thm-inverse-is-linear). \( V \cong W \) means that some isomorphism \( V \to W \) exists.

(b) True. Both have dimension \( 4 \), so they are isomorphic by @thm-isomorphic-iff-same-dimension.

(c) True. By @cor-rank-nullity-consequences an injective linear map between spaces of the same finite dimension is surjective, so \( T \) is bijective, hence an isomorphism.

(d) False. On \( F^{\nN} \), the shifts of @exm-differentiation-integration-one-sided satisfy \( LR = \id \) but \( RL \neq \id \). The statement is true when \( V \) is finite-dimensional (@thm-one-sided-inverse-maps).

(e) False. \( \nR^2 \cong \nR^2 \), but the zero map \( \nR^2 \to \nR^2 \) is not injective.

(f) The Invertible Operator Theorem, @thm-invertible-operator-tfae, (c) ⇒ (a).
:::

### B. Practice

::: {#exr-isomorphisms-b1}
[B1: An explicit isomorphism]

Let \( U = \{ A \in M_2(\nR) : A\tp = A \} \) be the space of symmetric \( 2 \times 2 \) real matrices. Find an explicit isomorphism \( U \to \nR[x]_{\le 2} \), and verify that it is one.
:::

::: {.solution}
Every \( A \in U \) has the form \( \begin{pmatrix} a & b \\ b & c \end{pmatrix} \) with \( a, b, c \in \nR \). Define
\[
T\begin{pmatrix} a & b \\ b & c \end{pmatrix} \coloneqq a + bx + cx^2, \qquad S(a + bx + cx^2) \coloneqq \begin{pmatrix} a & b \\ b & c \end{pmatrix}.
\]
*Linearity of \( T \).* Adding two symmetric matrices adds the entries \( a, b, c \), and adding polynomials adds coefficients, so \( T(A + A') = T(A) + T(A') \); similarly \( T(\lambda A) = \lambda T(A) \).

*Inverse.* \( S \) takes values in \( U \), and \( ST(A) = A \) for every \( A \in U \), since \( A \) is determined by its entries \( a, b, c \). Also \( TS(p) = p \) for every \( p \), since \( p \) is determined by its coefficients. So \( T \) has a two-sided inverse and is bijective, hence an isomorphism by @thm-inverse-is-linear. (Alternatively: both spaces have dimension \( 3 \) by @exm-dimensions, so by @thm-one-sided-inverse-maps the single equation \( ST = \id \) would already suffice.)
:::

::: {#exr-isomorphisms-b2}
[B2: Inverting \( \id + D \)]

Let \( n \ge 0 \), and let \( T \in \cL(\nR[x]_{\le n}) \), \( T(p) = p + p' \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( T \) is an isomorphism by computing its kernel.
2. Show that \( T^{-1} = \sum_{k=0}^{n} (-1)^kD^k \), where \( D \) is differentiation.
3. For \( n = 2 \), find the polynomial \( p \) with \( p + p' = x^2 \).
:::

*Hint: for (b), use the polynomial identity \( (1 + x)\sum_{k=0}^{n}(-x)^k = 1 + (-1)^nx^{n+1} \).*
:::

::: {.solution}
(a) Let \( p \in \ker T \), so \( p' = -p \). If \( p \neq 0 \), let \( d = \deg p \ge 0 \). Differentiation lowers the degree of a non-zero polynomial by at least one (it kills constants), so \( \deg p' < d = \deg(-p) \), contradicting \( p' = -p \). Hence \( p = 0 \) and \( \ker T = \{0\} \). By @thm-invertible-operator-tfae ((c) ⇒ (a)), \( T \) is an isomorphism.

(b) \( T = \id + D = q(D) \) with \( q = 1 + x \), and \( S \coloneqq \sum_{k=0}^n (-1)^kD^k = r(D) \) with \( r = \sum_{k=0}^n (-x)^k \). The identity in the hint is the telescoping sum \( \sum_{k=0}^{n}(-x)^k - \sum_{k=0}^{n}(-x)^{k+1} = 1 - (-x)^{n+1} \). By @thm-polynomial-of-operator-properties (b),
\[
TS = (qr)(D) = \id + (-1)^nD^{n+1} = \id,
\]
since \( D^{n+1} = 0 \) on \( \nR[x]_{\le n} \) (@exm-differentiation-nilpotent). By @thm-one-sided-inverse-maps, \( S = T^{-1} \).

(c) \( p = T^{-1}(x^2) = x^2 - D(x^2) + D^2(x^2) = x^2 - 2x + 2 \). Check: \( p + p' = (x^2 - 2x + 2) + (2x - 2) = x^2 \).
:::

::: {#exr-isomorphisms-b3}
[B3: Deciding isomorphism]

Determine which of the following pairs of real vector spaces are isomorphic. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \nR^4 \) and \( M_2(\nR) \).
2. \( \nR[x]_{\le 3} \) and \( \{ A \in M_3(\nR) : A\tp = -A \} \).
3. \( \{ p \in \nR[x]_{\le 4} : p(2) = 0 \} \) and \( \nR^4 \).
4. \( \nC^2 \) (over \( \nR \)) and \( \nR[x]_{\le 3} \).
5. The plane \( \{ (x, y, z) \in \nR^3 : x + y + z = 0 \} \) and \( \nC \) (over \( \nR \)).
:::
:::

::: {.solution}
By @thm-isomorphic-iff-same-dimension, in each case we compare dimensions over \( \nR \).

(a) Isomorphic: \( \dim \nR^4 = 4 = \dim M_2(\nR) \).

(b) Not isomorphic. \( \dim \nR[x]_{\le 3} = 4 \). If \( A\tp = -A \), then \( a_{ii} = -a_{ii} \), so \( 2a_{ii} = 0 \) and \( a_{ii} = 0 \), and \( a_{ji} = -a_{ij} \). Hence \( A = a_{12}(E_{12} - E_{21}) + a_{13}(E_{13} - E_{31}) + a_{23}(E_{23} - E_{32}) \), and the coefficients are entries of \( A \), so this expression is unique. By @thm-unique-representation these three matrices form a basis, and the dimension is \( 3 \neq 4 \).

(c) Isomorphic. The evaluation \( p \mapsto p(2) \), \( \nR[x]_{\le 4} \to \nR \), is linear and surjective (constants), with kernel the given space, so by @thm-rank-nullity its dimension is \( 5 - 1 = 4 \).

(d) Isomorphic: \( \dim_\nR \nC^2 = 2 \dim_\nC \nC^2 = 4 \) by @thm-restriction-of-scalars-dimension, and \( \dim \nR[x]_{\le 3} = 4 \).

(e) Isomorphic. The plane is the kernel of the surjective linear map \( (x, y, z) \mapsto x + y + z \) onto \( \nR \), so it has dimension \( 3 - 1 = 2 \) by @thm-rank-nullity; and \( \dim_\nR \nC = 2 \) (@exm-dimensions).
:::

### C. Going deeper

::: {#exr-isomorphisms-c1}
[C1: Invertible products]

::: {.enumerate options="label=(\alph*)"}
1. Let \( V \) be finite-dimensional and \( S, T \in \cL(V) \). Prove that if \( ST \) is invertible, then \( S \) and \( T \) are both invertible. Deduce that \( TS \) is then invertible too.
2. Show that (a) fails for \( V = F^{\nN} \): give \( S, T \in \cL(F^{\nN}) \) with \( ST \) invertible but neither \( S \) nor \( T \) invertible, and \( TS \) not invertible.
:::

*Hint: for (a), regroup \( (ST)(ST)^{-1} \) and \( (ST)^{-1}(ST) \).*
:::

::: {.solution}
(a) The inverse \( (ST)^{-1} \) lies in \( \cL(V) \) (@thm-inverse-is-linear), and \( (ST)(ST)^{-1} = \id_V = (ST)^{-1}(ST) \). By associativity (@thm-composition-linear (b)), \( S\bigl(T(ST)^{-1}\bigr) = \id_V \) and \( \bigl((ST)^{-1}S\bigr)T = \id_V \). By @thm-invertible-operator-tfae, (g) ⇒ (a) applied to \( S \) with right inverse \( T(ST)^{-1} \) shows that \( S \) is invertible, and (f) ⇒ (a) applied to \( T \) with left inverse \( (ST)^{-1}S \) shows that \( T \) is invertible. Then \( TS \) is a composition of isomorphisms, hence an isomorphism by @thm-isomorphic-equivalence-relation.

(b) Let \( S = L \) and \( T = R \) be the left and right shifts of @exm-differentiation-integration-one-sided. Then \( ST = LR = \id \), which is invertible. But \( L \) is not injective and \( R \) is not surjective, so neither is invertible, and \( TS = RL \) sends \( (1, 0, 0, \dots) \) to \( \0 \), so it is not injective and not invertible. The proof of (a) breaks at the appeal to @thm-invertible-operator-tfae, which needs finite dimension.
:::

::: {#exr-isomorphisms-c2}
[C2: A space isomorphic to a proper subspace]

::: {.enumerate options="label=(\alph*)"}
1. Let \( V \) be finite-dimensional and \( U \) a subspace of \( V \) with \( U \cong V \). Prove that \( U = V \).
2. Let \( U = \{ p \in F[x] : p(0) = 0 \} \), the polynomials with constant coefficient \( 0 \). Show that \( T \colon F[x] \to U \), \( T(p) = xp \), is an isomorphism. Hence (a) fails without finite dimension.
:::
:::

::: {.solution}
(a) \( U \) is finite-dimensional by @thm-subspace-dimension. Since \( U \cong V \), @thm-isomorphic-iff-same-dimension gives \( \dim U = \dim V \), and then \( U = V \) by @thm-dim-impl-eq.

(b) For \( p = \sum_k a_kx^k \), \( xp = \sum_k a_kx^{k+1} \) has constant coefficient \( 0 \), so \( T \) maps into \( U \), and \( T \) is linear because multiplication in \( F[x] \) distributes and commutes with scalars (@thm-polynomial-ring-laws). *Injective:* if \( xp = 0 \), then \( p = 0 \) by @cor-polynomial-no-zero-divisors, since \( x \neq 0 \). *Surjective:* if \( q = \sum_{k \ge 1} b_kx^k \in U \), then \( q = x\sum_{k \ge 1} b_kx^{k-1} = T\bigl(\sum_{k \ge 1} b_kx^{k-1}\bigr) \). So \( T \) is a bijective linear map, an isomorphism by @thm-inverse-is-linear, and \( U \cong F[x] \). But \( 1 \notin U \), so \( U \neq F[x] \). This is the phenomenon noted in Chapter 1, §8, now as an isomorphism.
:::
