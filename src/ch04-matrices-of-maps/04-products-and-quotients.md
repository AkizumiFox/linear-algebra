# Products and Quotient Spaces

So far every new vector space in this book has been found **inside** an old one, as a subspace. This section builds new spaces in two other ways. The first glues spaces together side by side, making a product; it is the "external" direct sum promised in Chapter 1. The second, the quotient space \( V/U \), is subtler and more important: it collapses a subspace \( U \) to a single point and keeps only what \( V \) knows beyond \( U \). Quotients let us state precisely what a linear map remembers and what it forgets, in the three Isomorphism Theorems.

## Products of vector spaces

In Chapter 1 we wrote \( V = U \oplus W \) for subspaces \( U \) and \( W \) of one space \( V \) (@def-direct-sum). The two pieces already lived in a common space, and "direct" was a property of how they sat there. But often we want to combine two spaces that have nothing to do with each other, such as \( \nR^2 \) and \( \nR[x]_{\le 1} \), into one space in which each keeps its identity. There is no common space to add inside, so we build one.

The model is \( F^2 \). A vector of \( F^2 \) is a pair \( (a, b) \) of scalars, and we add and scale pairs entry by entry. Nothing in that recipe needs the entries to be scalars: the entries could be vectors, taken from any vector spaces over \( F \).

*The product of vector spaces is the space of lists with one entry from each space, added and scaled entry by entry.*

::: {#def-product-of-spaces}
[Product of vector spaces]

Let \( V_1, \dots, V_k \) be vector spaces over the **same** field \( F \). Their **product** (or **external direct sum**) is the Cartesian product (@def-cartesian-product)
\[
V_1 \times \dots \times V_k = \{ (\v_1, \dots, \v_k) : \v_i \in V_i \text{ for each } i \},
\]
with addition and scalar multiplication defined **entrywise**: for \( a \in F \),
\[
\begin{aligned}
(\v_1, \dots, \v_k) + (\w_1, \dots, \w_k) &\coloneqq (\v_1 + \w_1, \dots, \v_k + \w_k), \\
a(\v_1, \dots, \v_k) &\coloneqq (a\v_1, \dots, a\v_k).
\end{aligned}
\]
:::

In words: the \( i \)-th entry of a sum is the sum of the \( i \)-th entries, computed **in \( V_i \)**, and similarly for scalar multiples. Two elements are equal exactly when all their entries are equal. Every operation happens inside one \( V_i \) at a time, which is why all the \( V_i \) must share the field \( F \): the same scalar \( a \) has to act on every entry.

**It is a vector space.** Both operations land in \( V_1 \times \dots \times V_k \), since \( \v_i + \w_i \in V_i \) and \( a\v_i \in V_i \). Each axiom of @def-vector-space is an equation between lists, so it holds when it holds in each entry, and in each entry it is the same axiom in \( V_i \). For example, (VS6) reads
\[
\begin{aligned}
(a + b)(\v_1, \dots, \v_k)
  &= ((a + b)\v_1, \dots, (a + b)\v_k) \\
  &= (a\v_1 + b\v_1, \dots, a\v_k + b\v_k) \\
  &= a(\v_1, \dots, \v_k) + b(\v_1, \dots, \v_k),
\end{aligned}
\]
using (VS6) in each \( V_i \). The zero vector is \( (\0, \dots, \0) \), with the zero of \( V_i \) in the \( i \)-th entry, and the additive inverse of \( (\v_1, \dots, \v_k) \) is \( (-\v_1, \dots, -\v_k) \). The other axioms are checked in exactly the same way.

**Examples.**

- **The standard example.** \( F \times \dots \times F \) (\( n \) factors) is \( F^n \) with its usual operations.
- **Unrelated spaces.** An element of \( \nR^2 \times \nR[x]_{\le 1} \) is a pair \( ((a, b), c + dx) \), and \( ((1, 0), x) + ((2, 5), 3 - x) = ((3, 5), 3) \).
- **Augmented data.** A linear system \( \A\x = \b \) with \( m \) equations in \( n \) unknowns is a single element \( (\A, \b) \) of \( M_{m \times n}(F) \times F^m \).
- **Degenerate cases.** For \( k = 1 \) the product is \( V_1 \) itself, with entries written in parentheses. And \( V \times \{\0\} \) consists of the pairs \( (\v, \0) \); the map \( \v \mapsto (\v, \0) \) is a linear bijection \( V \to V \times \{\0\} \), so a zero factor adds nothing.

**Non-example by minimal change.** Take \( V_1 = \nC \) as a vector space over \( \nC \) and \( V_2 = \nR \) over \( \nR \). The set \( \nC \times \nR \) is fine, but the entrywise rule \( i \cdot (z, t) = (iz, it) \) fails: \( it \notin \nR \) for \( t \ne 0 \). The clause that fails is "over the **same** field". Restricting the scalars of \( \nC \) to \( \nR \) (@def-restriction-of-scalars) repairs it, and \( \nC \times \nR \) over \( \nR \) is a vector space of dimension \( 3 \).

Bases of the factors combine into a basis of the product. For \( \v \in V_i \), write \( \iota_i(\v) \) for the list with \( \v \) in the \( i \)-th entry and \( \0 \) in every other entry. The map \( \iota_i \colon V_i \to V_1 \times \dots \times V_k \) is linear, because the operations are entrywise.

::: {#thm-dimension-of-product}
[Dimension of a Product]

Let \( V_1, \dots, V_k \) be finite-dimensional vector spaces over \( F \), and let \( (\b_{i1}, \dots, \b_{in_i}) \) be a basis of \( V_i \) for each \( i \). Then the list of all vectors \( \iota_i(\b_{ij}) \), for \( i = 1, \dots, k \) and \( j = 1, \dots, n_i \), is a basis of \( V_1 \times \dots \times V_k \). In particular,
\[
\dim(V_1 \times \dots \times V_k) = \dim V_1 + \dots + \dim V_k .
\]
:::

::: {.proof}
*Spanning.* Let \( (\v_1, \dots, \v_k) \) be in the product. Since the operations are entrywise, \( (\v_1, \dots, \v_k) = \iota_1(\v_1) + \dots + \iota_k(\v_k) \). Each \( \v_i \) is a combination \( \sum_j c_{ij}\b_{ij} \), and \( \iota_i \) is linear, so \( \iota_i(\v_i) = \sum_j c_{ij}\,\iota_i(\b_{ij}) \) (@thm-linear-combination). Hence \( (\v_1, \dots, \v_k) \) is a combination of the vectors \( \iota_i(\b_{ij}) \).

*Independence.* Let \( \sum_{i=1}^{k}\sum_{j=1}^{n_i} c_{ij}\,\iota_i(\b_{ij}) = \0 \). The \( i \)-th entry of the left side is \( \sum_j c_{ij}\b_{ij} \), because every \( \iota_{i'}(\b_{i'j}) \) with \( i' \ne i \) has \( \0 \) there. So \( \sum_j c_{ij}\b_{ij} = \0 \) in \( V_i \) for each \( i \), and the independence of the basis of \( V_i \) gives \( c_{ij} = 0 \) for all \( j \).

The list has \( n_1 + \dots + n_k \) vectors, which gives the dimension (@def-dimension).
:::

For instance, \( \dim(\nR^2 \times \nR[x]_{\le 1}) = 2 + 2 = 4 \), so this product is isomorphic to \( \nR^4 \) by @thm-isomorphic-iff-same-dimension.

How does the external product relate to the internal direct sum of Chapter 1? If \( U_1, \dots, U_k \) are subspaces of \( V \), there is a natural linear map from the product to \( V \): add up the entries. The sum is direct exactly when this map loses no information.

::: {#thm-internal-external-direct-sum}
[Internal and External Direct Sums]

::: {.enumerate options="label=(\alph*)"}
1. Let \( U_1, \dots, U_k \) be subspaces of a vector space \( V \), and let
   \[
   S \colon U_1 \times \dots \times U_k \to V, \qquad S(\u_1, \dots, \u_k) = \u_1 + \dots + \u_k .
   \]
   Then \( S \) is linear with \( \im S = U_1 + \dots + U_k \). It is injective if and only if the sum \( U_1 + \dots + U_k \) is direct. In that case \( S \) is an isomorphism from \( U_1 \times \dots \times U_k \) onto \( U_1 \oplus \dots \oplus U_k \).
2. Conversely, let \( V_1, \dots, V_k \) be vector spaces over \( F \). Then the images \( \iota_i(V_i) \) are subspaces of \( V_1 \times \dots \times V_k \), each isomorphic to \( V_i \) via \( \iota_i \), and
   \[
   V_1 \times \dots \times V_k = \iota_1(V_1) \oplus \dots \oplus \iota_k(V_k).
   \]
:::
:::

::: {.proof}
(a) For lists \( (\u_i) \), \( (\u_i') \) and \( a \in F \), regrouping the finite sums gives \( S((\u_i) + (\u_i')) = \sum_i (\u_i + \u_i') = S((\u_i)) + S((\u_i')) \) and \( S(a(\u_i)) = \sum_i a\u_i = aS((\u_i)) \), so \( S \) is linear. Its image is \( \{ \u_1 + \dots + \u_k : \u_i \in U_i \} \), which is \( U_1 + \dots + U_k \) by @def-sum-of-subspaces. Its kernel consists of the lists with \( \u_1 + \dots + \u_k = \0 \). By @thm-injective-iff-trivial-kernel, \( S \) is injective if and only if the only such list is \( (\0, \dots, \0) \), which is condition (b) of @thm-direct-sum-k-criteria, equivalent to the sum being direct. In that case \( S \), viewed as a map onto its image, is a linear bijection, hence an isomorphism (@def-isomorphism).

(b) Each \( \iota_i \) is linear and injective (its kernel is \( \{\0\} \), since \( \iota_i(\v) \) has \( \v \) as its \( i \)-th entry), so \( \iota_i(V_i) \) is a subspace (@thm-prop-image) and \( \iota_i \) is a bijection onto it. Every list satisfies \( (\v_1, \dots, \v_k) = \iota_1(\v_1) + \dots + \iota_k(\v_k) \), so the product is the sum of the subspaces \( \iota_i(V_i) \). If \( \iota_1(\v_1) + \dots + \iota_k(\v_k) = \0 \), then \( (\v_1, \dots, \v_k) = (\0, \dots, \0) \), so every piece \( \iota_i(\v_i) \) is \( \0 \). By @thm-direct-sum-k-criteria ((b) \( \Rightarrow \) (a)) the sum is direct.
:::

So internal and external direct sums are the same thing seen from two sides. An internal direct sum is a product that happens to live inside \( V \); a product is an internal direct sum of copies of its factors. Many books write \( \oplus \) for both. This book keeps \( \times \) for the external construction, so that \( U \oplus W \) always refers to subspaces of one space.

::: {.check}
Use @thm-internal-external-direct-sum (a) and Rank–Nullity to explain why, for **finite-dimensional** subspaces \( U, W \) of \( V \), the sum \( U + W \) is direct if and only if \( \dim(U + W) = \dim U + \dim W \).
:::

::: {.solution}
The addition map \( S \colon U \times W \to V \) has image \( U + W \), and \( \dim(U \times W) = \dim U + \dim W \) by @thm-dimension-of-product. By @thm-rank-nullity, \( \dim U + \dim W = \dim(U + W) + \dim \ker S \). So \( \dim(U + W) = \dim U + \dim W \) exactly when \( \ker S = \{\0\} \), that is, when \( S \) is injective, which by the theorem means the sum is direct. This recovers @thm-direct-sum-criteria (a) \( \Leftrightarrow \) (c).
:::

## Cosets

The second construction starts from a picture you have already seen. In Chapter 1 we compared the line \( U = \{ x + 2y = 0 \} \) through the origin with the parallel line \( L = \{ x + 2y = 3 \} \), which is not a subspace. In Chapter 3 we found that the solutions of a consistent system \( \A\x = \b \) form a set \( \p + \nul(\A) \), a subspace shifted by one particular solution (@thm-general-solution-structure). Both are translates of a subspace. They deserve a name.

::: {#def-coset}
[Coset]

Let \( U \) be a subspace of a vector space \( V \), and let \( \v \in V \). The **coset** of \( U \) through \( \v \) is the subset
\[
\v + U \coloneqq \{ \v + \u : \u \in U \} \subseteq V .
\]
Any \( \w \in \v + U \) is called a **representative** of the coset.
:::

In \( \nR^2 \), with \( U = \{ x + 2y = 0 \} = \Span((2, -1)) \), the coset through \( (3, 0) \) is the line \( \{ x + 2y = 3 \} \): a point \( (3, 0) + t(2, -1) = (3 + 2t, -t) \) satisfies \( x + 2y = 3 \), and every solution of \( x + 2y = 3 \) is of this form with \( t = -y \). In general \( (a, b) + U = \{ x + 2y = a + 2b \} \), so the cosets of \( U \) are exactly the lines parallel to \( U \).

\begin{center}
\begin{tikzpicture}[scale=0.85]
  \draw[->, gray] (-3.8, 0) -- (4.6, 0) node[right] {$x$};
  \draw[->, gray] (0, -3.1) -- (0, 3.3) node[above] {$y$};
  \draw[very thick] (-3.5, 1.75) -- (4.2, -2.1);
  \node[right] at (4.2, -2.1) {$U = \{x + 2y = 0\}$};
  \draw[very thick, dashed] (-3.0, 3.0) -- (4.2, -0.6);
  \node[right] at (4.2, -0.6) {$\v + U = \{x + 2y = 3\}$};
  \draw[thick, dotted] (-3.5, 0.75) -- (3.2, -2.6);
  \node[left] at (-3.5, 0.75) {$\{x + 2y = -2\}$};
  \fill (0, 0) circle (1.6pt) node[below left] {$\mathbf{0}$};
  \fill (1, 1) circle (2pt) node[above right] {$\v = (1, 1)$};
  \fill (3, 0) circle (2pt) node[below left] {$\v' = (3, 0)$};
  \draw[->, thick] (1, 1) -- (2.9, 0.05);
  \node[font=\small, below left] at (2.0, 0.5) {$+\,(2, -1)$};
\end{tikzpicture}
\end{center}

The picture shows three cosets of \( U \): \( U \) itself (solid), the line through \( \v = (1, 1) \) (dashed), and another parallel line (dotted). The points \( \v = (1, 1) \) and \( \v' = (3, 0) \) lie on the same dashed line, because \( \v' - \v = (2, -1) \in U \); so they are two representatives of **one** coset. That observation is the whole theory of cosets.

::: {#lem-coset-equality}
[When two cosets are equal]

Let \( U \) be a subspace of \( V \). For \( \v, \w \in V \), write \( \v \sim \w \) if \( \v - \w \in U \).

::: {.enumerate options="label=(\alph*)"}
1. \( \sim \) is an equivalence relation on \( V \), and the equivalence class of \( \v \) is the coset \( \v + U \).
2. \( \v + U = \w + U \) if and only if \( \v - \w \in U \).
3. Two cosets of \( U \) are either equal or disjoint, and every vector of \( V \) lies in exactly one coset.
:::
:::

::: {.proof}
(a) We check @def-equivalence-relation. (E1) \( \v - \v = \0 \in U \). (E2) If \( \v - \w \in U \), then \( \w - \v = (-1)(\v - \w) \in U \) by @thm-negation-scalar and closure under scalar multiplication. (E3) If \( \v - \w \in U \) and \( \w - \x \in U \), then \( \v - \x = (\v - \w) + (\w - \x) \in U \) by closure under addition. For the class, \( \w \sim \v \) means \( \w - \v = \u \) for some \( \u \in U \), that is, \( \w = \v + \u \in \v + U \); so the class \( [\v] \) of @def-equivalence-class is \( \v + U \).

(b) By (a) and @lem-classes-equal-or-disjoint (a), \( \v + U = \w + U \) if and only if \( \v \sim \w \), that is, \( \v - \w \in U \).

(c) This is @lem-classes-equal-or-disjoint (b), together with \( \v \in \v + U \) (take \( \u = \0 \)).
:::

**More examples.**

- **Vertical lines.** In \( \nR^3 \), let \( U = \Span(\e_3) \), the \( z \)-axis. The coset \( (a, b, c) + U \) is the vertical line through \( (a, b, 0) \), and \( (a, b, c) + U = (a', b', c') + U \) exactly when \( a = a' \) and \( b = b' \). A coset is determined by the shadow of any of its points on the \( xy \)-plane.
- **Polynomials with a prescribed value.** In \( F[x]_{\le n} \), let \( U = \{ p : p(0) = 0 \} \), a subspace (the kernel of evaluation at \( 0 \)). Then \( p + U = q + U \) exactly when \( (p - q)(0) = 0 \), that is, \( p(0) = q(0) \). So \( p + U \) is the set of all polynomials with the same constant term as \( p \).
- **Degenerate cases.** If \( U = \{\0\} \), each coset \( \v + U = \{\v\} \) is a single vector. If \( U = V \), there is only one coset, \( \v + V = V \), because \( \v - \w \in V \) always.

**Non-example by minimal change.** Try to use the line \( L = \{ x + 2y = 3 \} \), which is not a subspace, in place of \( U \). The rule "\( \v \sim \w \) if \( \v - \w \in L \)" is not even reflexive: \( \v - \v = \0 \notin L \). What fails is the hypothesis that \( U \) is a subspace, which (E1), (E2) and (E3) each used.

::: {.warning}
**A coset has many names, and it is usually not a subspace.** In the example above, \( (1, 1) + U \) and \( (3, 0) + U \) are the **same** set, although \( (1, 1) \ne (3, 0) \). Never conclude \( \v = \w \) from \( \v + U = \w + U \); conclude only \( \v - \w \in U \). And \( \v + U \) is a subspace only when it contains \( \0 \), that is, when \( \v \in U \) and so \( \v + U = U \). The dashed line above is not a subspace.
:::

## The quotient space

Now we want to treat each coset as a single point. The motivation is a kind of deliberate forgetting. Suppose we only care about vectors of \( \nR^2 \) "up to" adding something from \( U \), for instance because we only ever measure the quantity \( x + 2y \). Then \( (1, 1) \) and \( (3, 0) \) carry the same information, and the space of all the information we keep is the set of lines parallel to \( U \). We would like this set to be a vector space, so that we can add and scale lines.

The recipe is the one used for \( \nZ/n\nZ \) in Chapter 0 (@exm-addition-mod-n-well-defined): define the operations through representatives, then check that the choice of representatives does not matter.

*The quotient space \( V/U \) is \( V \) with everything in \( U \) declared to be zero.*

::: {#def-quotient-space}
[Quotient space]

Let \( U \) be a subspace of a vector space \( V \) over \( F \). The **quotient space** \( V/U \) (read "\( V \) modulo \( U \)") is the set of all cosets of \( U \),
\[
V/U \coloneqq \{ \v + U : \v \in V \},
\]
with the operations
\[
\begin{aligned}
(\v + U) + (\w + U) &\coloneqq (\v + \w) + U, \\
a(\v + U) &\coloneqq a\v + U \qquad (\v, \w \in V,\ a \in F).
\end{aligned}
\]
The **quotient map** is \( \pi \colon V \to V/U \), \( \pi(\v) = \v + U \).
:::

In words: an element of \( V/U \) is a whole coset, a subset of \( V \). By @lem-coset-equality (a), \( V/U \) is the quotient set of \( V \) by the relation \( \v \sim \w \Leftrightarrow \v - \w \in U \) (@def-quotient-set), and \( \pi \) is its quotient map. To add two cosets, pick a representative of each, add them in \( V \), and take the coset of the result. To scale a coset, scale a representative. The operations are written with representatives, so before anything else we must check that they are **well defined**.

The danger is real. By @lem-coset-equality, \( (1, 1) + U \) and \( (3, 0) + U \) are one element of \( \nR^2/U \). If the sum \( ((1, 1) + U) + (\w + U) \) depended on which of the two names we used, the "definition" would assign two values to one pair of cosets, and it would not define a function at all (@def-function). The theorem below rules this out, and then shows that the operations make \( V/U \) a vector space.

::: {#thm-quotient-space-operations-well-defined}
[The Quotient Space Is a Vector Space]

Let \( U \) be a subspace of a vector space \( V \) over \( F \).

::: {.enumerate options="label=(\alph*)"}
1. The addition and scalar multiplication in @def-quotient-space are well defined: the right-hand sides depend only on the cosets \( \v + U \) and \( \w + U \), not on the representatives \( \v \) and \( \w \).
2. With these operations \( V/U \) is a vector space over \( F \). Its zero vector is \( \0 + U = U \), and the additive inverse of \( \v + U \) is \( (-\v) + U \).
3. The quotient map \( \pi \colon V \to V/U \) is linear and surjective, and \( \ker \pi = U \).
:::
:::

::: {.idea}
Chapter 0's @thm-well-defined-on-quotient turns a function on \( V \) that is constant on classes into a function on \( V/U \). It is stated for functions of one variable, so we use it one variable at a time. ① For scalar multiplication by a fixed \( a \): if \( \v - \v' \in U \), then \( a\v - a\v' = a(\v - \v') \in U \). ② For addition, first freeze the second summand \( \w \) and vary the first; then show that the resulting function on cosets does not change when \( \w \) is replaced by an equivalent \( \w' \). Each check is one line and uses exactly one closure property of \( U \). Once the operations exist, every axiom for cosets is the same axiom in \( V \), passed through \( \pi \).
:::

::: {.proof}
Throughout, \( \v \sim \v' \) means \( \v - \v' \in U \), and by @lem-coset-equality (b), \( \v \sim \v' \) exactly when \( \v + U = \v' + U \).

(a) *Scalar multiplication.* Fix \( a \in F \), and let \( g_a \colon V \to V/U \), \( g_a(\v) = a\v + U \). If \( \v \sim \v' \), then \( a\v - a\v' = a(\v - \v') \in U \) by (VS5) and closure of \( U \) under scalar multiplication, so \( g_a(\v) = g_a(\v') \). By @thm-well-defined-on-quotient (a), there is exactly one function \( \bar g_a \colon V/U \to V/U \) with \( \bar g_a(\v + U) = a\v + U \) for every \( \v \in V \). We define \( a(\v + U) \coloneqq \bar g_a(\v + U) \).

*Addition, first variable.* Fix \( \w \in V \), and let \( f_\w \colon V \to V/U \), \( f_\w(\v) = (\v + \w) + U \). If \( \v \sim \v' \), then \( (\v + \w) - (\v' + \w) = \v - \v' \in U \), so \( f_\w(\v) = f_\w(\v') \). By @thm-well-defined-on-quotient (a), there is exactly one function \( \bar f_\w \colon V/U \to V/U \) with \( \bar f_\w(\v + U) = (\v + \w) + U \) for every \( \v \).

*Addition, second variable.* Let \( \sF \) be the set of all functions \( V/U \to V/U \), and let \( h \colon V \to \sF \), \( h(\w) = \bar f_\w \). Suppose \( \w \sim \w' \). For every \( \v \in V \), \( (\v + \w) - (\v + \w') = \w - \w' \in U \), so
\[
\bar f_\w(\v + U) = (\v + \w) + U = (\v + \w') + U = \bar f_{\w'}(\v + U).
\]
Since every element of \( V/U \) has the form \( \v + U \), the functions \( \bar f_\w \) and \( \bar f_{\w'} \) are equal, that is, \( h(\w) = h(\w') \). By @thm-well-defined-on-quotient (a) again, there is exactly one function \( \bar h \colon V/U \to \sF \) with \( \bar h(\w + U) = \bar f_\w \). We define \( X + Y \coloneqq \bar h(Y)(X) \) for \( X, Y \in V/U \). Then
\[
(\v + U) + (\w + U) = \bar h(\w + U)(\v + U) = \bar f_\w(\v + U) = (\v + \w) + U,
\]
which is the formula of @def-quotient-space, and its value depends only on the two cosets.

(b) Every element of \( V/U \) is \( \pi(\v) = \v + U \) for some \( \v \), and by (a) we have \( \pi(\v) + \pi(\w) = \pi(\v + \w) \) and \( a\pi(\v) = \pi(a\v) \). Let \( X = \pi(\x) \), \( Y = \pi(\y) \), \( Z = \pi(\z) \) be in \( V/U \), and \( a, b \in F \). Each axiom follows by moving \( \pi \) outside, using the axiom in \( V \), and moving \( \pi \) back:

- (VS1) \( X + Y = \pi(\x + \y) = \pi(\y + \x) = Y + X \).
- (VS2) \( (X + Y) + Z = \pi((\x + \y) + \z) = \pi(\x + (\y + \z)) = X + (Y + Z) \).
- (VS3) \( X + \pi(\0) = \pi(\x + \0) = \pi(\x) = X \), so \( \pi(\0) = \0 + U = U \) is a zero vector.
- (VS4) \( X + \pi(-\x) = \pi(\x + (-\x)) = \pi(\0) \), so \( \pi(-\x) = (-\x) + U \) is an additive inverse of \( X \).
- (VS5) \( a(X + Y) = \pi(a(\x + \y)) = \pi(a\x + a\y) = aX + aY \).
- (VS6) \( (a + b)X = \pi((a + b)\x) = \pi(a\x + b\x) = aX + bX \).
- (VS7) \( a(bX) = \pi(a(b\x)) = \pi((ab)\x) = (ab)X \).
- (VS8) \( 1X = \pi(1\x) = \pi(\x) = X \).

Hence \( V/U \) is a vector space over \( F \).

(c) The identities \( \pi(\v + \w) = \pi(\v) + \pi(\w) \) and \( \pi(a\v) = a\pi(\v) \) from (b) say that \( \pi \) is linear. It is surjective by the definition of \( V/U \). Finally, \( \v \in \ker \pi \) means \( \v + U = \0 + U \), which by @lem-coset-equality (b) means \( \v = \v - \0 \in U \). So \( \ker \pi = U \).
:::

Part (c) has a pleasant reading: **every subspace is a kernel**. Given \( U \subseteq V \), the quotient map is a linear map whose kernel is exactly \( U \).

**Examples.**

- **Parallel lines.** In \( \nR^2/U \) with \( U = \{ x + 2y = 0 \} \), write \( \ell_c \) for the line \( \{ x + 2y = c \} \). Since \( (a, b) \in \ell_{a + 2b} \), the definition gives \( \ell_c + \ell_d = \ell_{c + d} \) and \( t\,\ell_c = \ell_{tc} \): to add two parallel lines, add their "heights" \( c \) and \( d \). The zero vector is \( \ell_0 = U \).
- **Constant terms.** In \( F[x]_{\le n}/U \) with \( U = \{ p : p(0) = 0 \} \), the coset \( p + U \) is determined by \( p(0) \), and \( (p + U) + (q + U) = (p + q) + U \) is determined by \( p(0) + q(0) \). All that survives of a polynomial is its constant term.
- **Degenerate cases.** \( V/\{\0\} \) has the cosets \( \{\v\} \), added exactly as in \( V \): nothing is forgotten. \( V/V \) has the single element \( V \), so it is the zero space: everything is forgotten.

**Non-example by minimal change.** Replace the line \( U \) by the union of the two axes, \( S = \Span(\e_1) \cup \Span(\e_2) \subseteq \nR^2 \). It still contains \( \0 \) and is still closed under scalar multiplication, but it is not closed under addition. Then "\( \v - \w \in S \)" is not transitive: \( (1, 1) - (0, 1) = (1, 0) \in S \) and \( (0, 1) - (0, 0) = (0, 1) \in S \), but \( (1, 1) - (0, 0) = (1, 1) \notin S \). Concretely, the "cosets" \( (1, 1) + S \) and \( (0, 0) + S = S \) both contain \( (0, 1) = (1, 1) + (-1, 0) \), yet they are different sets, since \( \0 \in S \) but \( (1, 1) + \s = \0 \) would need \( \s = (-1, -1) \notin S \). The sets \( \v + S \) do not split \( \nR^2 \) into disjoint pieces, so there is no set "\( \nR^2/S \)" of the kind the definition needs. The clause that fails is "\( U \) is a subspace", specifically closure under addition.

**Why this definition.** Each part of the hypothesis that \( U \) is a subspace has a job: \( \0 \in U \) makes \( \sim \) reflexive; closure under scalar multiplication makes \( \sim \) symmetric and scaling of cosets well defined; closure under addition makes \( \sim \) transitive and addition of cosets well defined. The non-example shows what goes wrong when one of them is missing. The notation \( V/U \) and the phrase "modulo \( U \)" come from \( \nZ/n\nZ \), where integers are identified when their difference lies in \( n\nZ \).

::: {.warning}
**\( V/U \) is not a subspace of \( V \).** Its elements are subsets of \( V \), not vectors of \( V \), and its addition is a new operation. For example, \( \nR^3/\Span(\e_3) \) is not the \( xy \)-plane: its elements are vertical lines. The \( xy \)-plane is a **complement** of the \( z \)-axis, one of many (Chapter 1), whereas \( V/U \) involves no choice at all. The two are isomorphic, as we show below, but they are different objects.
:::

In finite dimension the size of a quotient is exactly what one would guess from the picture: we lose \( \dim U \) dimensions.

::: {#thm-dimension-quotient}
[Dimension of a Quotient]

Let \( V \) be finite-dimensional and \( U \) a subspace of \( V \). Then \( V/U \) is finite-dimensional and
\[
\dim(V/U) = \dim V - \dim U .
\]
More precisely, if \( (\u_1, \dots, \u_m, \w_1, \dots, \w_s) \) is a basis of \( V \) such that \( (\u_1, \dots, \u_m) \) is a basis of \( U \), then \( (\w_1 + U, \dots, \w_s + U) \) is a basis of \( V/U \).
:::

::: {.proof}
By @thm-quotient-space-operations-well-defined (c), \( \pi \colon V \to V/U \) is linear, surjective and has kernel \( U \). By the Rank–Nullity Theorem (@thm-rank-nullity), \( \im \pi = V/U \) is finite-dimensional and \( \dim V = \dim U + \dim(V/U) \), which is the formula.

For the basis, let \( \v + U \in V/U \) and write \( \v = \sum_i a_i\u_i + \sum_j b_j\w_j \). Since \( \pi \) is linear and \( \pi(\u_i) = U \) is the zero vector, @thm-linear-combination gives \( \v + U = \sum_j b_j(\w_j + U) \). So the list \( (\w_1 + U, \dots, \w_s + U) \) spans \( V/U \). Its length is \( s = \dim V - \dim U = \dim(V/U) \), so it is a basis by @thm-right-size-basis (b).
:::

Such a basis always exists: take a basis of \( U \) and extend it (@thm-basis-extension). So to find a basis of a quotient, **extend a basis of \( U \) to one of \( V \) and keep the cosets of the new vectors.**

::: {#exm-quotient-basis}
[A basis of a quotient of \( \nR^3 \)]

Let \( U = \Span((1, 1, 1)) \subseteq \nR^3 \). Find a basis of \( \nR^3/U \), and write \( (2, 5, -1) + U \) in it.
:::

::: {.solution}
Extend \( (1, 1, 1) \) by \( \e_1 \) and \( \e_2 \). The list \( ((1, 1, 1), \e_1, \e_2) \) is independent: in \( a(1, 1, 1) + b\e_1 + c\e_2 = (a + b, a + c, a) = \0 \), the third entry gives \( a = 0 \), and then \( b = c = 0 \). It has length \( 3 \), so it is a basis of \( \nR^3 \) (@thm-right-size-basis). By @thm-dimension-quotient, \( (\e_1 + U, \e_2 + U) \) is a basis of \( \nR^3/U \), which has dimension \( 3 - 1 = 2 \).

To write \( (2, 5, -1) + U \), solve \( (2, 5, -1) = a(1, 1, 1) + b\e_1 + c\e_2 \): the third entry gives \( a = -1 \), then \( b = 3 \) and \( c = 6 \). Hence
\[
(2, 5, -1) + U = 3(\e_1 + U) + 6(\e_2 + U),
\]
and indeed \( (2, 5, -1) - (3, 6, 0) = (-1, -1, -1) \in U \). The coordinates \( (3, 6) \) are \( (x - z, y - z) \) evaluated at \( (2, 5, -1) \): they are exactly the quantities that do not change when a multiple of \( (1, 1, 1) \) is added.
:::

The warning above said that a quotient is not a complement. The next result says how they are related: any complement is a concrete model of the quotient.

::: {#prp-complement-isomorphic-to-quotient}
[A complement is a model of the quotient]

Let \( U \) be a subspace of \( V \), and let \( W \) be a subspace with \( V = U \oplus W \). Then the restriction of the quotient map, \( W \to V/U \), \( \w \mapsto \w + U \), is an isomorphism.
:::

::: {.proof}
The restriction of the linear map \( \pi \) to \( W \) is linear. *Injective:* if \( \w + U = U \) with \( \w \in W \), then \( \w \in U \) by @lem-coset-equality (b), so \( \w \in U \cap W = \{\0\} \) (@thm-direct-sum-criteria); by @thm-injective-iff-trivial-kernel the restriction is injective. *Surjective:* given \( \v + U \), write \( \v = \u + \w \) with \( \u \in U \), \( \w \in W \); then \( \v - \w = \u \in U \), so \( \v + U = \w + U \). A linear bijection is an isomorphism (@def-isomorphism).
:::

So every complement of \( U \) is isomorphic to \( V/U \), which gives a second proof that all complements have the same dimension. The quotient is the choice-free object that all the complements imitate.

::: {.check}
In \( \nR^2/U \) with \( U = \Span((1, 1)) \), is \( (2, 3) + U = (0, 1) + U \)? Is \( (1, 0) + U = (0, 1) + U \)? What is \( \dim(\nR^2/U) \)?
:::

::: {.solution}
By @lem-coset-equality (b): \( (2, 3) - (0, 1) = (2, 2) \in U \), so the first two cosets are equal. \( (1, 0) - (0, 1) = (1, -1) \notin U \), so the second pair are different cosets. By @thm-dimension-quotient, \( \dim(\nR^2/U) = 2 - 1 = 1 \).
:::

## The First Isomorphism Theorem

A linear map \( T \colon V \to W \) forgets exactly the information in its kernel: \( T\v = T\v' \) if and only if \( T(\v - \v') = \0 \), that is, \( \v - \v' \in \ker T \). In the language of this section, \( T \) takes the same value at two vectors exactly when they lie in the same coset of \( \ker T \). So \( T \) is really a function of the coset, and on cosets it forgets nothing.

::: {#thm-first-isomorphism}
[First Isomorphism Theorem]

Let \( T \colon V \to W \) be a linear map, and let \( K = \ker T \). Then the rule
\[
\bar T \colon V/K \to W, \qquad \bar T(\v + K) = T\v
\]
defines a linear map, which is injective with \( \im \bar T = \im T \), and satisfies \( \bar T \circ \pi = T \). Hence
\[
V/\ker T \cong \im T .
\]
:::

::: {.proof}
*Well defined.* \( K \) is a subspace by @thm-prop-kernel, so \( V/K \) is a vector space. If \( \v + K = \v' + K \), then \( \v - \v' \in K \) by @lem-coset-equality (b), so \( T\v - T\v' = T(\v - \v') = \0 \). Hence \( T \) is constant on each coset of \( K \), and by @thm-well-defined-on-quotient (a) there is exactly one function \( \bar T \colon V/K \to W \) with \( \bar T(\v + K) = T\v \), that is, \( \bar T \circ \pi = T \).

*Linear.* For \( \v, \w \in V \) and \( a \in F \), by @def-quotient-space and the linearity of \( T \),
\[
\begin{aligned}
\bar T\big((\v + K) + (\w + K)\big) &= \bar T\big((\v + \w) + K\big) = T(\v + \w) \\
&= T\v + T\w = \bar T(\v + K) + \bar T(\w + K),
\end{aligned}
\]
and similarly \( \bar T(a(\v + K)) = \bar T(a\v + K) = T(a\v) = a\bar T(\v + K) \).

*Injective.* If \( \bar T(\v + K) = \0 \), then \( T\v = \0 \), so \( \v \in K \) and \( \v + K = K \), the zero of \( V/K \). By @thm-injective-iff-trivial-kernel, \( \bar T \) is injective.

*Image.* The values of \( \bar T \) are the vectors \( T\v \), \( \v \in V \), so \( \im \bar T = \im T \). Regarded as a map \( V/K \to \im T \), \( \bar T \) is a linear bijection, hence an isomorphism (@def-isomorphism).
:::

So every linear map factors as "collapse the kernel, then embed": \( T = \bar T \circ \pi \), with \( \pi \) surjective and \( \bar T \) injective. When \( V \) is finite-dimensional, taking dimensions with @thm-dimension-quotient gives \( \dim V - \dim \ker T = \dim \im T \), which is Rank–Nullity again. The theorem is stronger than the count, because it names the isomorphism, and it holds in infinite dimension too.

The practical use runs the other way: to identify a quotient \( V/U \), find a surjective linear map out of \( V \) whose kernel is exactly \( U \).

::: {#exm-first-isomorphism}
[Identifying quotients]

Use the First Isomorphism Theorem to show:

::: {.enumerate options="label=(\alph*)"}
1. \( \nR^3/L \cong \nR^2 \), where \( L = \Span((1, 1, 1)) \);
2. \( \nR[x]_{\le n}/U \cong \nR \), where \( U = \{ p : p(0) = 0 \} \).
:::
:::

::: {.solution}
(a) Let \( T \colon \nR^3 \to \nR^2 \), \( T(x, y, z) = (x - z,\ y - z) \), which is linear because each entry is a linear expression. It is surjective, since \( T(a, b, 0) = (a, b) \). Its kernel is \( \{ x = z,\ y = z \} = \{ (t, t, t) \} = L \). By @thm-first-isomorphism, \( (x, y, z) + L \mapsto (x - z, y - z) \) is an isomorphism \( \nR^3/L \to \nR^2 \). This explains the coordinates found in @exm-quotient-basis. The check that it is well defined is visible: adding \( (t, t, t) \) to \( (x, y, z) \) does not change \( x - z \) or \( y - z \).

(b) Let \( \operatorname{ev}_0 \colon \nR[x]_{\le n} \to \nR \), \( p \mapsto p(0) \). It is linear by @thm-evaluation-respects-operations, surjective because the constant polynomial \( c \) maps to \( c \), and its kernel is \( U \) by definition. By @thm-first-isomorphism, \( p + U \mapsto p(0) \) is an isomorphism \( \nR[x]_{\le n}/U \to \nR \). In particular \( \dim(\nR[x]_{\le n}/U) = 1 \) by @thm-isomorphic-iff-same-dimension, so \( \dim U = (n + 1) - 1 = n \) by @thm-dimension-quotient.
:::

## The Second and Third Isomorphism Theorems

Two more identifications come from the same method: write down a surjective map, compute its kernel, and apply the First Isomorphism Theorem. The first compares a sum of subspaces with an intersection.

::: {#thm-second-isomorphism}
[Second Isomorphism Theorem]

Let \( U \) and \( W \) be subspaces of a vector space \( V \). Then \( U \cap W \) is a subspace of \( U \), \( W \) is a subspace of \( U + W \), and
\[
U/(U \cap W) \to (U + W)/W, \qquad \u + (U \cap W) \mapsto \u + W
\]
is a well-defined isomorphism. Hence \( (U + W)/W \cong U/(U \cap W) \).
:::

::: {.idea}
Picture two planes \( U \) and \( W \) in \( \nR^3 \) meeting in a line. Modulo \( W \), a vector of \( U + W \) is represented by its \( U \)-part alone, since the \( W \)-part is forgotten. The only vectors of \( U \) that become zero are those already in \( W \). So the map "\( \u \mapsto \u + W \)" from \( U \) is onto, with kernel \( U \cap W \).
:::

::: {.proof}
\( U \cap W \) is a subspace (@thm-intersection-subspaces) contained in \( U \), and \( W \) is a subspace contained in \( U + W \) (@thm-subspace-sum), so both quotients exist. Let \( \pi_W \colon U + W \to (U + W)/W \) be the quotient map, and let \( S \colon U \to (U + W)/W \), \( S\u = \u + W \), be its restriction to \( U \); \( S \) is linear because \( \pi_W \) is (@thm-quotient-space-operations-well-defined).

*\( S \) is surjective.* An element of \( (U + W)/W \) is \( (\u + \w) + W \) with \( \u \in U \), \( \w \in W \). Since \( (\u + \w) - \u = \w \in W \), @lem-coset-equality (b) gives \( (\u + \w) + W = \u + W = S\u \).

*\( \ker S = U \cap W \).* For \( \u \in U \), \( S\u = W \) means \( \u \in W \) (@lem-coset-equality (b)), that is, \( \u \in U \cap W \).

By @thm-first-isomorphism applied to \( S \), the rule \( \u + (U \cap W) \mapsto S\u = \u + W \) is a well-defined injective linear map with image \( \im S = (U + W)/W \), hence an isomorphism. (Directly: if \( \u - \u' \in U \cap W \), then \( \u - \u' \in W \), so \( \u + W = \u' + W \), and the value does not depend on the representative.)
:::

If \( U \) and \( W \) are finite-dimensional, then so is \( U + W \) (it is spanned by the union of bases, @prp-sum-of-spans), and @thm-dimension-quotient turns the theorem into \( \dim(U + W) - \dim W = \dim U - \dim(U \cap W) \). That is the dimension formula for sums (@thm-dimension-formula-subspace-dim), now as a consequence of an isomorphism rather than of a basis computation. An exercise below asks for the details.

The third theorem says that quotients can be taken in stages.

::: {#thm-third-isomorphism}
[Third Isomorphism Theorem]

Let \( U \subseteq W \subseteq V \) be subspaces. Then \( W/U = \{ \w + U : \w \in W \} \) is a subspace of \( V/U \), and
\[
(V/U)/(W/U) \to V/W, \qquad (\v + U) + W/U \mapsto \v + W
\]
is a well-defined isomorphism. Hence \( (V/U)/(W/U) \cong V/W \).
:::

::: {.proof}
Let \( S \colon V/U \to V/W \), \( S(\v + U) = \v + W \).

*Well defined.* If \( \v + U = \v' + U \), then \( \v - \v' \in U \subseteq W \), so \( \v + W = \v' + W \) by @lem-coset-equality (b). By @thm-well-defined-on-quotient (a), applied to \( V \to V/W \), \( \v \mapsto \v + W \), the rule defines a function on \( V/U \).

*Linear and surjective.*
\[
\begin{aligned}
S((\v + U) + (\w + U)) &= S((\v + \w) + U) = (\v + \w) + W \\
&= S(\v + U) + S(\w + U),
\end{aligned}
\]
and similarly for scalars, by @def-quotient-space in both quotients. Every \( \v + W \) equals \( S(\v + U) \).

*Kernel.* \( S(\v + U) = W \) means \( \v \in W \). If \( \v \in W \), then \( \v + U \in W/U \). Conversely, if \( \v + U = \w + U \) with \( \w \in W \), then \( \v - \w \in U \subseteq W \), so \( \v \in W \). Hence \( \ker S = W/U \). In particular \( W/U \) is a subspace of \( V/U \), by @thm-prop-kernel.

By @thm-first-isomorphism applied to \( S \), \( (V/U)/(W/U) \cong \im S = V/W \), via \( (\v + U) + W/U \mapsto S(\v + U) = \v + W \).
:::

The notation \( W/U \) is used with two meanings, and they agree: the quotient space of \( W \) by \( U \), and the set of cosets \( \w + U \) with \( \w \in W \), sitting inside \( V/U \). The coset \( \w + U \) is the same subset of \( V \) in both readings, and the operations agree because both are computed with representatives. For example, with \( V = \nR^3 \), \( U \) the \( z \)-axis and \( W \) the \( xz \)-plane, \( V/W \cong \nR \) through the \( y \)-coordinate, and the theorem says that first forgetting \( z \) and then forgetting \( x \) leaves the same thing as forgetting both at once.

## The universal property of the quotient

The proofs of the three theorems repeated one move: a linear map that vanishes on \( U \) passes to \( V/U \). We record that move once, in its general form. It is the standard way to **define** linear maps out of a quotient.

::: {#thm-quotient-universal-property}
[Universal Property of the Quotient]

Let \( U \) be a subspace of \( V \), \( \pi \colon V \to V/U \) the quotient map, and \( T \colon V \to W \) a linear map.

::: {.enumerate options="label=(\alph*)"}
1. If \( U \subseteq \ker T \), then there is **exactly one** linear map \( \bar T \colon V/U \to W \) with \( \bar T \circ \pi = T \), namely \( \bar T(\v + U) = T\v \). Its image is \( \im T \), and it is injective if and only if \( U = \ker T \).
2. Conversely, if some function \( \bar T \colon V/U \to W \) satisfies \( \bar T \circ \pi = T \), then \( U \subseteq \ker T \).
:::
:::

::: {.proof}
(a) If \( \v - \v' \in U \subseteq \ker T \), then \( T\v = T\v' \). By @thm-well-defined-on-quotient (a) there is exactly one function \( \bar T \) with \( \bar T(\v + U) = T\v \), and it is linear by the computation in the proof of @thm-first-isomorphism, which used only this formula. Any linear \( \bar T \) with \( \bar T \circ \pi = T \) satisfies this formula, so it is this one. The image is \( \{ T\v \} = \im T \). The kernel of \( \bar T \) is \( \{ \v + U : \v \in \ker T \} \); it is \( \{ U \} \), the zero subspace, exactly when every \( \v \in \ker T \) lies in \( U \), that is, when \( \ker T \subseteq U \), which together with \( U \subseteq \ker T \) means \( U = \ker T \). Apply @thm-injective-iff-trivial-kernel.

(b) Let \( \u \in U \). Then \( \pi(\u) = U = \pi(\0) \), so \( T\u = \bar T(\pi(\u)) = \bar T(\pi(\0)) = T(\0) = \0 \) by @thm-zero-maps-to-zero. Hence \( U \subseteq \ker T \).
:::

In words: **linear maps out of \( V/U \) are the same as linear maps out of \( V \) that kill \( U \).** The First Isomorphism Theorem is the case \( U = \ker T \). For example, the map \( T \colon \nR^3 \to \nR \), \( T(x, y, z) = x \), kills the \( z \)-axis \( U \), so it induces \( \bar T \colon \nR^3/U \to \nR \), \( (x, y, z) + U \mapsto x \). Since \( \ker T \) is the \( yz \)-plane, strictly larger than \( U \), this \( \bar T \) is not injective: it also kills the coset \( \e_2 + U \).

Quotients will return in Chapter 9, where an operator \( T \) with \( T(U) \subseteq U \) induces an operator on \( V/U \), and this is the engine of induction arguments on the dimension.

## Exercises

### A. Check your understanding

::: {#exr-products-and-quotients-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the quotient space \( V/U \) and its two operations.
2. State the condition, in terms of \( \v - \w \), for \( \v + U = \w + U \).
3. True or false: \( V/U \) is a subspace of \( V \). Justify your answer.
4. State the First Isomorphism Theorem.
5. If \( U \) is a \( 2 \)-dimensional subspace of \( \nR^5 \), what is \( \dim(\nR^5/U) \)? What is \( \dim(\nR^5 \times U) \)?
6. What must be checked before the formula \( (\v + U) + (\w + U) = (\v + \w) + U \) can be used as a definition, and which property of \( U \) makes the check work?
:::
:::

::: {.solution}
(a) For a subspace \( U \) of \( V \), \( V/U = \{ \v + U : \v \in V \} \), with \( (\v + U) + (\w + U) = (\v + \w) + U \) and \( a(\v + U) = a\v + U \) (@def-quotient-space).

(b) \( \v + U = \w + U \) if and only if \( \v - \w \in U \) (@lem-coset-equality).

(c) False. The elements of \( V/U \) are cosets, which are subsets of \( V \), not vectors of \( V \).

(d) If \( T \colon V \to W \) is linear, then \( \v + \ker T \mapsto T\v \) is a well-defined isomorphism \( V/\ker T \to \im T \) (@thm-first-isomorphism).

(e) \( 5 - 2 = 3 \) by @thm-dimension-quotient, and \( 5 + 2 = 7 \) by @thm-dimension-of-product.

(f) That the right-hand side does not depend on the representatives: if \( \v - \v' \in U \) and \( \w - \w' \in U \), then \( (\v + \w) + U = (\v' + \w') + U \). This works because \( (\v + \w) - (\v' + \w') = (\v - \v') + (\w - \w') \) and \( U \) is closed under addition.
:::

### B. Practice

::: {#exr-products-and-quotients-b1}
[B1: A basis of a quotient of \( \nR^4 \)]

Let \( U = \Span((1, 0, 1, 0), (0, 1, 0, 1)) \subseteq \nR^4 \).

::: {.enumerate options="label=(\alph*)"}
1. Find \( \dim(\nR^4/U) \) and a basis of \( \nR^4/U \).
2. Write \( (3, 1, 4, 1) + U \) in your basis.
3. Decide whether \( (1, 2, 3, 4) + U = (3, 4, 1, 2) + U \).
:::
:::

::: {.solution}
(a) The two spanning vectors are independent (look at the first two entries), so \( \dim U = 2 \) and \( \dim(\nR^4/U) = 4 - 2 = 2 \) by @thm-dimension-quotient. Extend by \( \e_1, \e_2 \). If \( a(1, 0, 1, 0) + b(0, 1, 0, 1) + c\e_1 + d\e_2 = (a + c, b + d, a, b) = \0 \), then \( a = b = 0 \) from the last two entries and \( c = d = 0 \) from the first two. So the four vectors are independent, hence a basis of \( \nR^4 \) (@thm-right-size-basis), and by @thm-dimension-quotient \( (\e_1 + U, \e_2 + U) \) is a basis of \( \nR^4/U \).

(b) Solve \( (3, 1, 4, 1) = (a + c, b + d, a, b) \): \( a = 4 \), \( b = 1 \), \( c = -1 \), \( d = 0 \). Since the \( U \)-part becomes zero in the quotient, \( (3, 1, 4, 1) + U = -1(\e_1 + U) + 0(\e_2 + U) \). Check: \( (3, 1, 4, 1) + \e_1 = (4, 1, 4, 1) = 4(1, 0, 1, 0) + (0, 1, 0, 1) \in U \).

(c) The difference is \( (1, 2, 3, 4) - (3, 4, 1, 2) = (-2, -2, 2, 2) \). A vector \( (a, b, a, b) \) of \( U \) has equal first and third entries, but \( -2 \ne 2 \). So the difference is not in \( U \), and the cosets are different by @lem-coset-equality.
:::

::: {#exr-products-and-quotients-b2}
[B2: A map that factors through a quotient]

Let \( T \colon \nR[x]_{\le 2} \to \nR^2 \), \( T(p) = (p(1), p'(1)) \), and \( U = \Span((x - 1)^2) \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( U \subseteq \ker T \), so that \( T \) induces a linear map \( \bar T \colon \nR[x]_{\le 2}/U \to \nR^2 \) with \( \bar T(p + U) = T(p) \).
2. Prove that \( \bar T \) is an isomorphism.
3. Compute \( \bar T(x^2 + U) \), and find the coset \( \bar T^{-1}(0, 1) \).
:::
:::

::: {.solution}
(a) \( T \) is linear, since evaluation and differentiation are. For \( q = (x - 1)^2 \), \( q(1) = 0 \) and \( q'(1) = 2(1 - 1) = 0 \), so \( T(q) = \0 \), and hence \( T(cq) = \0 \) for all \( c \). So \( U \subseteq \ker T \), and @thm-quotient-universal-property (a) gives the linear map \( \bar T \).

(b) \( T(1) = (1, 0) \) and \( T(x - 1) = (0, 1) \), so \( T \) is surjective and \( \rank T = 2 \). By @thm-rank-nullity, \( \dim \ker T = 3 - 2 = 1 = \dim U \), so \( \ker T = U \) by @thm-dim-impl-eq. By @thm-quotient-universal-property (a), \( \bar T \) is injective with image \( \im T = \nR^2 \). Hence \( \bar T \) is a linear bijection, an isomorphism.

(c) \( \bar T(x^2 + U) = T(x^2) = (1, 2) \). Since \( T(x - 1) = (0, 1) \), \( \bar T^{-1}(0, 1) = (x - 1) + U \), the set of all \( x - 1 + c(x - 1)^2 \).
:::

::: {#exr-products-and-quotients-b3}
[B3: Matrices modulo scalars]

Let \( n \ge 1 \) and \( S = \{ c\I_n : c \in F \} \subseteq M_n(F) \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( S \) is a subspace and find \( \dim(M_n(F)/S) \).
2. For \( n = 2 \), find a basis of \( M_2(F)/S \).
3. Show that \( \A + S = \B + S \) if and only if \( \A - \B \) is a scalar matrix, and decide whether \( \begin{pmatrix} 3 & 1 \\ 0 & 5 \end{pmatrix} + S = \begin{pmatrix} 1 & 1 \\ 0 & 3 \end{pmatrix} + S \).
:::
:::

::: {.solution}
(a) \( S = \Span(\I_n) \) is a subspace by @thm-span-subspace, of dimension \( 1 \) since \( \I_n \ne 0 \). By @thm-dimension-quotient, \( \dim(M_n(F)/S) = n^2 - 1 \).

(b) Extend \( (\I_2) \) by \( \E_{11}, \E_{12}, \E_{21} \). If \( a\I_2 + b\E_{11} + c\E_{12} + d\E_{21} = \begin{pmatrix} a + b & c \\ d & a \end{pmatrix} = 0 \), then \( a = c = d = 0 \) and then \( b = 0 \). So the four matrices are independent, hence a basis of \( M_2(F) \) (@thm-right-size-basis), and \( (\E_{11} + S, \E_{12} + S, \E_{21} + S) \) is a basis of \( M_2(F)/S \) by @thm-dimension-quotient.

(c) This is @lem-coset-equality (b) for the subspace \( S \). Here the difference is \( \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = 2\I_2 \in S \), so the two cosets are equal.
:::

### C. Going deeper

::: {#exr-products-and-quotients-c1}
[C1: The dimension formula from isomorphisms]

Let \( U \) and \( W \) be finite-dimensional subspaces of a vector space \( V \).

::: {.enumerate options="label=(\alph*)"}
1. Using @thm-second-isomorphism and @thm-dimension-quotient, prove that \( \dim(U + W) = \dim U + \dim W - \dim(U \cap W) \).
2. Give a second proof: apply Rank–Nullity to the addition map \( S \colon U \times W \to V \), \( S(\u, \w) = \u + \w \), after showing that \( \u \mapsto (\u, -\u) \) is an isomorphism from \( U \cap W \) onto \( \ker S \).
:::
:::

::: {.solution}
(a) \( U + W \) is finite-dimensional, being spanned by a basis of \( U \) followed by a basis of \( W \) (@prp-sum-of-spans), and \( U \cap W \subseteq U \) is finite-dimensional (@thm-subspace-dimension). By @thm-second-isomorphism, \( (U + W)/W \cong U/(U \cap W) \), and isomorphic finite-dimensional spaces have equal dimension (@thm-isomorphic-iff-same-dimension). Applying @thm-dimension-quotient to both sides,
\[
\dim(U + W) - \dim W = \dim U - \dim(U \cap W),
\]
which rearranges to the formula.

(b) The map \( S \) is linear with image \( U + W \) by @thm-internal-external-direct-sum (a). Let \( J \colon U \cap W \to U \times W \), \( J\u = (\u, -\u) \); it is well defined because \( \u \in U \) and \( -\u \in W \), and linear because the operations are entrywise. It is injective, since \( (\u, -\u) = (\0, \0) \) forces \( \u = \0 \). Its image lies in \( \ker S \), since \( \u + (-\u) = \0 \). Conversely, if \( (\u, \w) \in \ker S \), then \( \w = -\u \); so \( \u = -\w \in W \), hence \( \u \in U \cap W \) and \( (\u, \w) = J\u \). Thus \( J \) is an isomorphism onto \( \ker S \), and \( \dim \ker S = \dim(U \cap W) \). By @thm-dimension-of-product and @thm-rank-nullity,
\[
\dim U + \dim W = \dim(U \times W) = \dim(U + W) + \dim(U \cap W).
\]
:::

::: {#exr-products-and-quotients-c2}
[C2: The operator induced on a quotient]

Let \( V \) be finite-dimensional, \( T \in \cL(V) \), and \( U \) a subspace with \( T\u \in U \) for every \( \u \in U \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \bar T(\v + U) \coloneqq T\v + U \) is a well-defined linear operator on \( V/U \).
2. Let \( (\u_1, \dots, \u_m) \) be a basis of \( U \), extended to a basis \( \sB = (\u_1, \dots, \u_m, \w_1, \dots, \w_s) \) of \( V \). Show that
   \[
   \mtx{T}{\sB}{\sB} = \begin{pmatrix} \A & \B \\ 0 & D \end{pmatrix},
   \]
   where \( \A \in M_m(F) \) is the matrix of the restriction \( T|_U \colon U \to U \) in \( (\u_1, \dots, \u_m) \), \( D \in M_s(F) \) is the matrix of \( \bar T \) in \( (\w_1 + U, \dots, \w_s + U) \), and \( 0 \) is the \( s \times m \) zero matrix.
3. Check (b) when \( T \) is differentiation on \( \nR[x]_{\le 2} \), with \( U = \nR[x]_{\le 1} \) and \( \sB = (1, x, x^2) \).
:::

*Hint: for (a), apply @thm-quotient-universal-property to \( \pi \circ T \).*
:::

::: {.solution}
(a) The map \( \pi \circ T \colon V \to V/U \), \( \v \mapsto T\v + U \), is linear as a composition of linear maps (@thm-composition-linear). For \( \u \in U \), \( T\u \in U \), so \( (\pi \circ T)(\u) = U \), the zero of \( V/U \); thus \( U \subseteq \ker(\pi \circ T) \). By @thm-quotient-universal-property (a) there is exactly one linear map \( \bar T \colon V/U \to V/U \) with \( \bar T(\v + U) = T\v + U \).

(b) For \( j \le m \), \( T\u_j \in U \), so it is a combination of \( \u_1, \dots, \u_m \) only, and its \( \sB \)-coordinates are \( 0 \) in the last \( s \) places. These first \( m \) columns, restricted to their first \( m \) entries, are the columns of the matrix \( \A \) of \( T|_U \) (which maps \( U \) to \( U \) by hypothesis and is linear). For the remaining columns, write \( T\w_k = \sum_i b_{ik}\u_i + \sum_l d_{lk}\w_l \). Passing to \( V/U \), where \( \u_i + U = U \) is zero, gives \( \bar T(\w_k + U) = \sum_l d_{lk}(\w_l + U) \). So the \( s \times s \) matrix \( (d_{lk}) \) is the matrix \( D \) of \( \bar T \) in the basis \( (\w_1 + U, \dots, \w_s + U) \) of @thm-dimension-quotient, and the bottom-right block of \( \mtx{T}{\sB}{\sB} \) is \( D \).

(c) \( T(1) = 0 \), \( T(x) = 1 \), \( T(x^2) = 2x \), so \( \mtx{T}{\sB}{\sB} = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix} \). Differentiation maps \( U = \nR[x]_{\le 1} \) into itself. The block \( \A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) is the matrix of \( T \) on \( U \) in \( (1, x) \), the lower-left block is \( \begin{pmatrix} 0 & 0 \end{pmatrix} \), and the block \( D \) is the \( 1 \times 1 \) matrix \( (0) \): indeed \( \bar T(x^2 + U) = 2x + U = U \), the zero coset, since \( 2x \in U \).
:::

::: {#exr-products-and-quotients-c3}
[C3: Counting cosets over a finite field]

Let \( F = \nF_q \) be a finite field with \( q \) elements, \( V \) a vector space over \( F \) of dimension \( n \), and \( U \) a subspace of dimension \( m \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \lvert V \rvert = q^n \).
2. Show that every coset \( \v + U \) has exactly \( \lvert U \rvert \) elements, and deduce \( \lvert V/U \rvert = q^{n - m} \) by counting.
3. Check that (b) agrees with @thm-dimension-quotient.
:::
:::

::: {.solution}
(a) Choose a basis \( (\v_1, \dots, \v_n) \). By @thm-unique-representation, \( (a_1, \dots, a_n) \mapsto a_1\v_1 + \dots + a_n\v_n \) is a bijection \( F^n \to V \), and \( F^n \) has \( q^n \) elements.

(b) The map \( U \to \v + U \), \( \u \mapsto \v + \u \), is surjective by @def-coset and injective because \( \v + \u = \v + \u' \) implies \( \u = \u' \). So \( \lvert \v + U \rvert = \lvert U \rvert = q^m \) by (a) applied to \( U \). By @lem-coset-equality (c), the cosets partition \( V \) into \( \lvert V/U \rvert \) disjoint sets of size \( q^m \), so \( q^n = \lvert V/U \rvert \cdot q^m \), and \( \lvert V/U \rvert = q^{n - m} \).

(c) By @thm-dimension-quotient, \( V/U \) is a vector space over \( \nF_q \) of dimension \( n - m \), so by (a) it has \( q^{n - m} \) elements, in agreement with (b). For example, \( \nF_2^3 \) modulo a line has \( 8/2 = 4 \) cosets.
:::
