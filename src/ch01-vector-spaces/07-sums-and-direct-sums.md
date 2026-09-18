# Sums and Direct Sums

We can now measure a single subspace: take a basis and count. This section asks how two or more subspaces combine. The intersection of two subspaces is again a subspace, but the union usually is not, so we need a better way to join them. The answer is the sum \( U + W \). We then prove the dimension formula for sums and single out the best case, the direct sum, in which every vector splits into pieces in exactly one way.

## The sum of subspaces

Recall from @thm-intersection-subspaces that \( U \cap W \) is a subspace whenever \( U \) and \( W \) are. It is the largest subspace inside both. The natural companion would be the smallest subspace containing both, and the first guess is the union \( U \cup W \).

That guess fails. In \( \nR^2 \), let \( U \) be the \( x \)-axis and \( W \) the \( y \)-axis. Then \( (1, 0) \in U \) and \( (0, 1) \in W \), but their sum \( (1, 1) \) lies on neither axis, so \( U \cup W \) is not closed under addition (@exm-union-axes). In fact @prp-union-subspaces shows that \( U \cup W \) is a subspace only in the dull case \( U \subseteq W \) or \( W \subseteq U \).

The failure tells us what is missing. Any subspace containing \( U \) and \( W \) must contain \( \u + \w \) for every \( \u \in U \) and \( \w \in W \), because subspaces are closed under addition. So we put all these sums in from the start.

*The sum of two subspaces is everything you can reach by adding one vector from each.*

::: {#def-sum-of-subspaces}
[Sum of Subspaces]

Let \( V \) be a vector space over \( F \), and let \( U \) and \( W \) be subspaces of \( V \). The **sum** of \( U \) and \( W \) is the subset
\[
U + W \coloneqq \{ \u + \w : \u \in U \text{ and } \w \in W \}.
\]
More generally, for subspaces \( U_1, \dots, U_k \) of \( V \) (with \( k \ge 1 \)), their **sum** is
\[
U_1 + \dots + U_k \coloneqq \{ \u_1 + \dots + \u_k : \u_i \in U_i \text{ for each } i = 1, \dots, k \}.
\]
:::

In words: a vector \( \v \) lies in \( U + W \) when **there exist** some \( \u \in U \) and some \( \w \in W \) with \( \v = \u + \w \). The definition asks for one such pair. It does not say the pair is unique, and in general it is not. For \( k \) subspaces we pick **one** vector from **each** \( U_i \) and add them. We also write \( \sum_{i=1}^{k} U_i \), and for \( k = 1 \) the sum is just \( U_1 \).

Here are some first examples.

- **The two axes.** In \( \nR^2 \), with \( U \) the \( x \)-axis and \( W \) the \( y \)-axis, every \( (a, b) \) equals \( (a, 0) + (0, b) \), so \( U + W = \nR^2 \). The union is two lines; the sum is the whole plane.
- **Two planes in \( \nR^3 \).** Let \( P_{xy} = \{ (x, y, 0) \} \) and \( P_{yz} = \{ (0, y, z) \} \). Every \( (a, b, c) = (a, b, 0) + (0, 0, c) \) is a sum of a vector in \( P_{xy} \) and one in \( P_{yz} \), so \( P_{xy} + P_{yz} = \nR^3 \).
- **Polynomials.** In \( F[x]_{\le 2} \), let \( U \) be the constant polynomials and \( W = \{ bx + cx^2 : b, c \in F \} \). Then \( a + bx + cx^2 = a + (bx + cx^2) \), so \( U + W = F[x]_{\le 2} \).
- **Matrices.** In \( M_2(F) \), the upper triangular matrices plus the lower triangular matrices give everything:
  \[
  \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} a & b \\ 0 & d \end{pmatrix} + \begin{pmatrix} 0 & 0 \\ c & 0 \end{pmatrix}.
  \]
- **Degenerate cases.** For any subspace \( U \), we have \( U + \{\0\} = U \) and \( U + U = U \). In both, "\( \supseteq \)" holds because \( \u = \u + \0 \), and "\( \subseteq \)" holds because \( U \) is closed under addition. So adding a subspace to itself produces nothing new: a sum is not a count.

**Non-example by minimal change.** The definition makes sense for any two subsets \( S, T \subseteq V \), but the result need not be a subspace. Take \( S = \{ (1, 0) \} \) and \( T = \{ (0, 1) \} \) in \( \nR^2 \). Then \( S + T = \{ (1, 1) \} \), which does not contain \( \0 \). What changed is that \( S \) and \( T \) are not subspaces: the hypothesis "subspace" is exactly what makes the next theorem work.

::: {.warning}
The sum \( U + W \) is **not** the union \( U \cup W \). A vector of \( U + W \) need not lie in \( U \) or in \( W \): \( (1, 1) \) lies in the sum of the two axes but on neither axis. Conversely, \( U + W \) is usually far bigger than \( U \cup W \).
:::

The sum does what we built it to do.

::: {#thm-subspace-sum}
[Sum of Subspaces Theorem]

Let \( U_1, \dots, U_k \) be subspaces of a vector space \( V \). Then \( U_1 + \dots + U_k \) is a subspace of \( V \) that contains each \( U_i \). Moreover, if \( X \) is any subspace of \( V \) containing every \( U_i \), then \( U_1 + \dots + U_k \subseteq X \). In other words, \( U_1 + \dots + U_k \) is the **smallest** subspace of \( V \) containing \( U_1, \dots, U_k \).
:::

::: {.proof}
Write \( S = U_1 + \dots + U_k \). We apply the Subspace Test (@thm-subspace-test).

(1) Each \( U_i \) contains \( \0 \), so \( \0 = \0 + \dots + \0 \in S \).

(2) Let \( \u_1 + \dots + \u_k \) and \( \u_1' + \dots + \u_k' \) be in \( S \), with \( \u_i, \u_i' \in U_i \). Regrouping with (VS1) and (VS2),
\[
(\u_1 + \dots + \u_k) + (\u_1' + \dots + \u_k') = (\u_1 + \u_1') + \dots + (\u_k + \u_k'),
\]
and \( \u_i + \u_i' \in U_i \) because \( U_i \) is closed under addition. Hence \( S \) is closed under addition.

(3) Let \( c \in F \). By the distributive axiom, \( c(\u_1 + \dots + \u_k) = c\u_1 + \dots + c\u_k \), and \( c\u_i \in U_i \) because \( U_i \) is closed under scaling. Hence \( S \) is closed under scalar multiplication.

Therefore \( S \) is a subspace. It contains \( U_j \): for \( \u \in U_j \), take \( \u_j = \u \) and \( \u_i = \0 \in U_i \) for \( i \ne j \). Finally, let \( X \) be a subspace containing every \( U_i \). An element \( \u_1 + \dots + \u_k \) of \( S \) is a sum of vectors \( \u_i \in U_i \subseteq X \), so it lies in \( X \) since \( X \) is closed under addition. This shows \( S \subseteq X \).
:::

So the sum plays the role that the union could not. It is the subspace analogue of \( \Span \), and the two notions fit together exactly. Recall from @thm-span-subspace that \( \Span(S) \) is the smallest subspace containing \( S \).

::: {#prp-sum-of-spans}
[Sum of Spans]

Let \( L_1, \dots, L_k \) be finite lists of vectors in \( V \), and let \( L \) be the list obtained by writing \( L_1, \dots, L_k \) one after another. Then
\[
\Span(L_1) + \dots + \Span(L_k) = \Span(L).
\]
:::

::: {.proof}
(\( \subseteq \)) The subspace \( \Span(L) \) contains every vector of each \( L_i \), so by @thm-span-subspace it contains each \( \Span(L_i) \). By @thm-subspace-sum it therefore contains \( \Span(L_1) + \dots + \Span(L_k) \).

(\( \supseteq \)) The sum \( \Span(L_1) + \dots + \Span(L_k) \) is a subspace by @thm-subspace-sum, and it contains each \( \Span(L_i) \), hence every vector of \( L \). By @thm-span-subspace it contains \( \Span(L) \).
:::

In practice this means: **to find a spanning list of a sum, concatenate spanning lists of the summands.** That list may be dependent, and the dimension formula below tells us by how much.

::: {.check}
In \( \nR^3 \), what is \( \Span((1, 0, 0)) + \Span((0, 1, 0)) \)? Is it equal to \( \Span((1, 0, 0)) \cup \Span((0, 1, 0)) \)?
:::

::: {.solution}
By @prp-sum-of-spans the sum is \( \Span((1, 0, 0), (0, 1, 0)) = \{ (a, b, 0) : a, b \in \nR \} \), the \( xy \)-plane. It is not the union: \( (1, 1, 0) \) lies in the plane but on neither axis.
:::

## The dimension formula

If \( U \) and \( W \) are finite-dimensional, how big is \( U + W \)? Concatenating a basis of \( U \) and a basis of \( W \) gives a spanning list of \( U + W \) of length \( \dim U + \dim W \) (@prp-sum-of-spans). That count is too large when \( U \) and \( W \) overlap. For the two planes \( P_{xy} \) and \( P_{yz} \) in \( \nR^3 \), it would give \( 2 + 2 = 4 \), but \( P_{xy} + P_{yz} = \nR^3 \) has dimension \( 3 \). The overlap is the \( y \)-axis, of dimension \( 1 \), and it has been counted twice. The theorem says this is the whole story.

::: {#thm-dimension-formula-subspace-dim}
[Dimension Formula for Sums]

Let \( U \) and \( W \) be finite-dimensional subspaces of a vector space \( V \). Then \( U + W \) is finite-dimensional, and
\[
\dim(U + W) = \dim U + \dim W - \dim(U \cap W).
\]
:::

The picture behind the proof is the inclusion diagram. The smallest space, \( U \cap W \), sits inside both \( U \) and \( W \), and both sit inside \( U + W \). We build bases from the bottom up.

\begin{center}
\begin{tikzpicture}[
    space/.style={draw, thick, rounded corners=2pt, inner sep=5pt, minimum height=2.2em},
    lab/.style={font=\small, align=center},
    inc/.style={->, thick, shorten >=3pt, shorten <=3pt}]
    \node[space] (cap) at (0, 0) {$U \cap W$};
    \node[space] (u) at (4, 1.6) {$U$};
    \node[space] (w) at (4, -1.6) {$W$};
    \node[space] (sum) at (8, 0) {$U + W$};
    \draw[inc] (cap) -- (u);
    \draw[inc] (cap) -- (w);
    \draw[inc] (u) -- (sum);
    \draw[inc] (w) -- (sum);
    \node[lab, below=4pt of cap] {basis\\$\v_1, \dots, \v_r$};
    \node[lab, above=4pt of u] {basis $\v_1, \dots, \v_r, \u_1, \dots, \u_s$};
    \node[lab, below=4pt of w] {basis $\v_1, \dots, \v_r, \w_1, \dots, \w_t$};
    \node[lab, below=4pt of sum] {Big Claim: basis\\$\v$'s, $\u$'s and $\w$'s};
    \node[font=\small] at (4, -3.1) {each arrow is an inclusion $\subseteq$};
\end{tikzpicture}
\end{center}

::: {.idea}
This is a dimension formula, so we start from the **smallest** space and extend outward.

① Take a basis \( (\v_1, \dots, \v_r) \) of \( U \cap W \).
② Extend it to a basis of \( U \) by adding \( \u_1, \dots, \u_s \), and separately to a basis of \( W \) by adding \( \w_1, \dots, \w_t \).
③ **Big Claim:** the combined list of all \( r + s + t \) vectors is a basis of \( U + W \). Spanning is easy. For independence, move the \( \w \)-part to the other side: the common vector lies in \( U \) and in \( W \), hence in \( U \cap W \), where the \( \v \)'s are a basis.
④ Count: \( r + s + t = (r + s) + (r + t) - r \).
:::

::: {.proof}
**Step 1: bases.** By @thm-intersection-subspaces, \( U \cap W \) is a subspace of \( V \); it lies inside \( U \) and uses the same operations, so it is also a subspace of \( U \). Since \( U \) is finite-dimensional, so is \( U \cap W \) (@thm-subspace-dimension), and it has a basis \( (\v_1, \dots, \v_r) \), where \( r = \dim(U \cap W) \) (@cor-basis-existence). This list is independent and lies in \( U \), so by the Basis Extension Theorem (@thm-basis-extension) there are vectors \( \u_1, \dots, \u_s \in U \) such that \( (\v_1, \dots, \v_r, \u_1, \dots, \u_s) \) is a basis of \( U \). In the same way, since the list also lies in \( W \), there are \( \w_1, \dots, \w_t \in W \) such that \( (\v_1, \dots, \v_r, \w_1, \dots, \w_t) \) is a basis of \( W \). Thus \( \dim U = r + s \) and \( \dim W = r + t \).

**Step 2: the Big Claim.**

::: {.claim}
The list \( \sB = (\v_1, \dots, \v_r, \u_1, \dots, \u_s, \w_1, \dots, \w_t) \) is a basis of \( U + W \).

::: {.proof}
*Spanning.* By @prp-sum-of-spans, \( U + W = \Span(\v_1, \dots, \v_r, \u_1, \dots, \u_s) + \Span(\v_1, \dots, \v_r, \w_1, \dots, \w_t) \) is the span of the concatenated list. That list contains each \( \v_i \) twice; removing the second copies does not change the span, since every removed vector already lies in the span of what remains (@thm-span-absorb). Hence \( \sB \) spans \( U + W \).

*Independence.* Let \( a_i, b_j, c_k \in F \) satisfy
\[
a_1\v_1 + \dots + a_r\v_r + b_1\u_1 + \dots + b_s\u_s + c_1\w_1 + \dots + c_t\w_t = \0.
\]
Move the \( \w \)-part across and name the common vector:
\[
\x \coloneqq a_1\v_1 + \dots + a_r\v_r + b_1\u_1 + \dots + b_s\u_s = -c_1\w_1 - \dots - c_t\w_t.
\]
The middle expression lies in \( U \), because all the \( \v_i \) and \( \u_j \) do. The right-hand expression lies in \( W \), because all the \( \w_k \) do. Hence \( \x \in U \cap W \). Since \( (\v_1, \dots, \v_r) \) spans \( U \cap W \), there are \( d_1, \dots, d_r \in F \) with \( \x = d_1\v_1 + \dots + d_r\v_r \). Comparing with the right-hand expression for \( \x \),
\[
d_1\v_1 + \dots + d_r\v_r + c_1\w_1 + \dots + c_t\w_t = \0.
\]
This is a combination of the basis \( (\v_1, \dots, \v_r, \w_1, \dots, \w_t) \) of \( W \), which is independent, so all \( d_i = 0 \) and all \( c_k = 0 \). Putting \( c_1 = \dots = c_t = 0 \) into the original equation leaves
\[
a_1\v_1 + \dots + a_r\v_r + b_1\u_1 + \dots + b_s\u_s = \0,
\]
a combination of the basis \( (\v_1, \dots, \v_r, \u_1, \dots, \u_s) \) of \( U \). By its independence, all \( a_i = 0 \) and all \( b_j = 0 \). Hence \( \sB \) is linearly independent (@def-linear-independence).
:::
:::

**Step 3: count.** By the claim, \( U + W \) has a finite basis of length \( r + s + t \), so it is finite-dimensional with \( \dim(U + W) = r + s + t \) (@def-dimension). Therefore
\[
\dim(U + W) = r + s + t = (r + s) + (r + t) - r = \dim U + \dim W - \dim(U \cap W),
\]
as claimed.
:::

The proof also works when some of \( r, s, t \) are \( 0 \): an empty list is independent and spans \( \{\0\} \), and every step reads correctly with empty sums. The move "basis of the smallest space, extend, Big Claim, count" is worth learning as a unit. It proves Rank–Nullity in Chapter 3 with the same four blocks.

The formula is often used to find one of the four numbers from the other three. Here are two uses, one by counting and one by computing.

::: {#exm-two-planes-r3}
[Two planes in \( \nR^3 \)]

Let \( U = \{ (x, y, z) \in \nR^3 : x + y + z = 0 \} \) and \( W = \{ (x, y, z) \in \nR^3 : x = z \} \). Show that \( U + W = \nR^3 \), and find a basis of \( \nR^3 \) of the shape used in the proof.
:::

::: {.solution}
Solving \( x + y + z = 0 \) for \( y \), every vector of \( U \) is \( (x, -x - z, z) = x(1, -1, 0) + z(0, -1, 1) \). The two vectors are independent (look at the first and third entries), so \( \dim U = 2 \). Similarly every vector of \( W \) is \( (x, y, x) = x(1, 0, 1) + y(0, 1, 0) \), and \( \dim W = 2 \).

A vector lies in \( U \cap W \) when \( x = z \) and \( x + y + z = 0 \), that is, \( y = -2x \). So \( U \cap W = \{ (x, -2x, x) \} = \Span((1, -2, 1)) \), which has dimension \( 1 \). By the dimension formula,
\[
\dim(U + W) = 2 + 2 - 1 = 3 = \dim \nR^3.
\]
Since \( U + W \subseteq \nR^3 \) and the dimensions agree, \( U + W = \nR^3 \) by @thm-dim-impl-eq.

Following the proof: \( (1, -2, 1) \) extends to a basis of \( U \) by \( (1, -1, 0) \in U \). Indeed \( (1, -1, 0) \) is not a multiple \( (c, -2c, c) \) of \( (1, -2, 1) \), since its first and third entries differ, so the list \( ((1, -2, 1), (1, -1, 0)) \) is independent by @lem-append-independent; it has length \( 2 = \dim U \), so it is a basis of \( U \) (@thm-right-size-basis). It extends to a basis of \( W \) by \( (0, 1, 0) \in W \), for the same reason: a multiple of \( (1, -2, 1) \) with first entry \( 0 \) is \( \0 \). The Big Claim says \( ((1, -2, 1), (1, -1, 0), (0, 1, 0)) \) is a basis of \( U + W = \nR^3 \).
:::

::: {#exm-two-planes-r4}
[Two planes in \( \nR^4 \) from spanning lists]

Let \( U = \Span((1, 1, 0, 0), (0, 0, 1, 1)) \) and \( W = \Span((1, 0, 1, 0), (0, 1, 0, 1)) \) in \( \nR^4 \). Find \( \dim(U \cap W) \) and \( \dim(U + W) \), and hence a basis of \( U + W \).
:::

::: {.solution}
Each spanning list is independent: in \( a(1, 1, 0, 0) + b(0, 0, 1, 1) = (a, a, b, b) = \0 \), both \( a \) and \( b \) are \( 0 \), and similarly \( c(1, 0, 1, 0) + d(0, 1, 0, 1) = (c, d, c, d) \). So \( \dim U = \dim W = 2 \).

A vector lies in \( U \cap W \) exactly when it can be written in both forms, \( (a, a, b, b) = (c, d, c, d) \). Comparing entries gives \( a = c \), \( a = d \), \( b = c \), \( b = d \), so \( a = b = c = d \). Hence \( U \cap W = \Span((1, 1, 1, 1)) \) and \( \dim(U \cap W) = 1 \). By the dimension formula, \( \dim(U + W) = 2 + 2 - 1 = 3 \).

For a basis, follow the proof. The vector \( (1, 1, 1, 1) \) together with \( (1, 1, 0, 0) \) is a list in \( U \), and it is independent by @lem-append-independent, because a multiple \( (c, c, c, c) \) of \( (1, 1, 1, 1) \) never equals \( (1, 1, 0, 0) \). It has length \( 2 = \dim U \), hence it is a basis of \( U \) (@thm-right-size-basis). Likewise \( ((1, 1, 1, 1), (1, 0, 1, 0)) \) is a basis of \( W \). By the Big Claim, \( ((1, 1, 1, 1), (1, 1, 0, 0), (1, 0, 1, 0)) \) is a basis of \( U + W \). In particular \( U + W \ne \nR^4 \).
:::

## Direct sums

In a basis, every vector has **exactly one** expression as a combination (@thm-unique-representation). Read that for \( F^n \) with the standard basis: \( F^n = \Span(\e_1) + \dots + \Span(\e_n) \), and each vector splits into pieces from these lines in exactly one way. We want the same property for subspaces that are not lines.

Sums do not always have it. In \( \nR^3 = P_{xy} + P_{yz} \),
\[
(1, 1, 1) = (1, 1, 0) + (0, 0, 1) = (1, 0, 0) + (0, 1, 1),
\]
two different splittings, because the planes share the \( y \)-axis and the \( y \)-component can be handed to either side. If we replace \( P_{yz} \) by the \( z \)-axis \( Z \), then \( (a, b, c) = (a, b, 0) + (0, 0, c) \) is the **only** splitting, since the \( Z \)-piece must have first two entries \( 0 \). We give this situation a name.

*A sum is direct when every vector in it breaks into one piece from each subspace in exactly one way.*

::: {#def-direct-sum}
[Direct Sum]

Let \( U_1, \dots, U_k \) be subspaces of a vector space \( V \) over \( F \). The sum \( U_1 + \dots + U_k \) is **direct** if **every** vector \( \v \in U_1 + \dots + U_k \) can be written in **exactly one** way as
\[
\v = \u_1 + \dots + \u_k \quad \text{with } \u_i \in U_i \text{ for each } i.
\]
In that case we write the sum as \( U_1 \oplus \dots \oplus U_k \). We write \( V = U_1 \oplus \dots \oplus U_k \) to mean that \( V = U_1 + \dots + U_k \) **and** the sum is direct.
:::

In words: existence of a splitting is automatic, since that is what membership in the sum means. The content of "direct" is **uniqueness**: if \( \u_1 + \dots + \u_k = \u_1' + \dots + \u_k' \) with \( \u_i, \u_i' \in U_i \), then \( \u_i = \u_i' \) for **every** \( i \). The symbol \( \oplus \) does not build a new space. It is the same subspace \( U_1 + \dots + U_k \), with a property recorded in the notation. (Chapter 3 builds an "external" direct sum out of spaces that do not sit inside a common \( V \).)

**Examples.**

- **Standard basis.** \( F^n = \Span(\e_1) \oplus \dots \oplus \Span(\e_n) \). More generally, if \( (\v_1, \dots, \v_n) \) is a basis of \( V \), then \( V = \Span(\v_1) \oplus \dots \oplus \Span(\v_n) \). A splitting \( \v = a_1\v_1 + \dots + a_n\v_n \) is a choice of coefficients, and @thm-unique-representation says there is exactly one.
- **Two splittings of the plane.** Let \( X \) be the \( x \)-axis, \( Y \) the \( y \)-axis and \( D = \{ (t, t) : t \in \nR \} \) the line \( y = x \). Then \( \nR^2 = X \oplus Y \), with \( (a, b) = (a, 0) + (0, b) \) the only splitting. Also \( \nR^2 = X \oplus D \): if \( (a, b) = (s, 0) + (t, t) \), the second entry forces \( t = b \), and then the first forces \( s = a - b \). So \( (a, b) = (a - b, 0) + (b, b) \), and there is no other choice.
- **Polynomials.** \( F[x]_{\le 2} = \Span(1) \oplus \Span(x, x^2) \). If \( a + bx + cx^2 = a' + (b'x + c'x^2) \), comparing coefficients gives \( a = a' \), \( b = b' \), \( c = c' \).
- **Degenerate.** \( U \oplus \{\0\} = U \) for every subspace \( U \): the only possible \( \{\0\} \)-piece is \( \0 \), so the \( U \)-piece of \( \v \) must be \( \v \).

**Non-example by minimal change.** Replace the \( z \)-axis in \( \nR^3 = P_{xy} \oplus Z \) by the plane \( P_{yz} \). The sum is still all of \( \nR^3 \), so existence still holds. What fails is uniqueness, as the two splittings of \( (1, 1, 1) \) above show. So \( \nR^3 = P_{xy} + P_{yz} \), but the sum is **not** direct. Likewise upper plus lower triangular \( 2 \times 2 \) matrices give \( M_2(F) \), but a diagonal matrix can be put in either summand, so that sum is not direct.

Checking uniqueness for **every** vector looks like a lot of work. For two subspaces it reduces to one condition you can check in a line.

::: {#thm-direct-sum-criteria}
[Direct Sum Criteria for Two Subspaces]

Let \( U \) and \( W \) be subspaces of a vector space \( V \). The following are equivalent:

::: {.enumerate options="label=(\alph*)"}
1. the sum \( U + W \) is direct;
2. \( U \cap W = \{\0\} \).
:::

If moreover \( U \) and \( W \) are finite-dimensional, they are also equivalent to

::: {.enumerate options="label=(\alph*)"}
3. \( \dim(U + W) = \dim U + \dim W \).
:::
:::

::: {.idea}
Uniqueness questions go through differences. If \( \u + \w = \u' + \w' \), then \( \u - \u' = \w' - \w \) is a single vector lying in both \( U \) and \( W \). So "no overlap" is exactly "no freedom in splitting". For (c), the dimension formula says the overcount \( \dim U + \dim W - \dim(U + W) \) is \( \dim(U \cap W) \), which is \( 0 \) exactly when \( U \cap W = \{\0\} \).
:::

::: {.proof}
(a) ⇒ (b). Suppose the sum is direct and let \( \v \in U \cap W \). Then \( \v = \v + \0 \) with \( \v \in U \), \( \0 \in W \), and \( \v = \0 + \v \) with \( \0 \in U \), \( \v \in W \). These are two splittings of \( \v \in U + W \), so by uniqueness their \( U \)-pieces agree: \( \v = \0 \). Hence \( U \cap W = \{\0\} \).

(b) ⇒ (a). Suppose \( U \cap W = \{\0\} \), and let \( \u + \w = \u' + \w' \) with \( \u, \u' \in U \) and \( \w, \w' \in W \). Then \( \u - \u' = \w' - \w \). The left side lies in \( U \) and the right side in \( W \), since both are subspaces. So this common vector lies in \( U \cap W = \{\0\} \), which gives \( \u = \u' \) and \( \w = \w' \). Hence every vector of \( U + W \) has only one splitting.

(b) ⇔ (c). Now let \( U \) and \( W \) be finite-dimensional. By the dimension formula (@thm-dimension-formula-subspace-dim), (c) holds if and only if \( \dim(U \cap W) = 0 \). A space has dimension \( 0 \) exactly when the empty list is a basis of it, that is, when it equals the span of the empty list, which is \( \{\0\} \). So (c) holds if and only if \( U \cap W = \{\0\} \).
:::

This is the everyday test: to show \( V = U \oplus W \), show \( V = U + W \) and \( U \cap W = \{\0\} \). In finite dimension there is a shortcut that avoids checking \( V = U + W \) at all: if \( U \cap W = \{\0\} \) and \( \dim U + \dim W = \dim V \), then \( \dim(U + W) = \dim V \) by (c), so \( U + W = V \) by @thm-dim-impl-eq. Count instead of check.

::: {#exm-plane-line-direct-sum}
[A plane and a line in \( \nR^3 \)]

Let \( U = \{ (x, y, z) \in \nR^3 : x + y + z = 0 \} \) and \( L = \Span((1, 1, 1)) \). Show that \( \nR^3 = U \oplus L \), and split \( (a, b, c) \) into its two pieces.
:::

::: {.solution}
From @exm-two-planes-r3, \( \dim U = 2 \), and \( \dim L = 1 \) since \( (1, 1, 1) \ne \0 \). If \( t(1, 1, 1) \in U \), then \( t + t + t = 3t = 0 \), so \( t = 0 \). Hence \( U \cap L = \{\0\} \). By @thm-direct-sum-criteria, \( \dim(U + L) = 2 + 1 = 3 \), so \( U + L = \nR^3 \) by @thm-dim-impl-eq. Therefore \( \nR^3 = U \oplus L \).

To split \( (a, b, c) \), look for \( t \) with \( (a, b, c) - t(1, 1, 1) \in U \), that is, \( (a - t) + (b - t) + (c - t) = 0 \). This gives \( t = \frac{a + b + c}{3} \), and
\[
(a, b, c) = \Big( a - \tfrac{a + b + c}{3},\ b - \tfrac{a + b + c}{3},\ c - \tfrac{a + b + c}{3} \Big) + \tfrac{a + b + c}{3}(1, 1, 1).
\]
The \( L \)-piece is the average of the entries times \( (1, 1, 1) \); the \( U \)-piece is what is left over.
:::

The same splitting trick, "average with a reflected copy", works for functions and matrices.

::: {#exm-even-odd-functions}
[Even and odd functions]

Let \( V = \nR^\nR \) be the space of all functions \( \nR \to \nR \), with \( E = \{ f : f(-x) = f(x) \text{ for all } x \} \) and \( O = \{ f : f(-x) = -f(x) \text{ for all } x \} \). Then \( V = E \oplus O \).
:::

::: {.solution}
Both are subspaces by the Subspace Test (@thm-subspace-test): the zero function is even and odd, and the defining equations are preserved by sums and scalar multiples. For instance, if \( f, g \in O \), then \( (f + g)(-x) = -f(x) - g(x) = -(f + g)(x) \).

*Sum.* For any \( f \in V \), put \( f_E(x) = \frac{f(x) + f(-x)}{2} \) and \( f_O(x) = \frac{f(x) - f(-x)}{2} \). Then \( f = f_E + f_O \), and \( f_E(-x) = \frac{f(-x) + f(x)}{2} = f_E(x) \), \( f_O(-x) = \frac{f(-x) - f(x)}{2} = -f_O(x) \). So \( V = E + O \).

*Intersection.* If \( f \in E \cap O \), then \( f(x) = f(-x) = -f(x) \) for every \( x \), so \( 2f(x) = 0 \) and \( f(x) = 0 \). Hence \( E \cap O = \{\0\} \), and \( V = E \oplus O \) by @thm-direct-sum-criteria.

For example, \( e^x = \cosh x + \sinh x \) is the splitting of the exponential function.
:::

::: {#exm-direct-sum-of-matrix}
[Symmetric and skew-symmetric matrices]

Let \( F \) be a field of characteristic not \( 2 \) (for instance \( \nR \) or \( \nC \)), and let \( n \ge 1 \). In \( M_n(F) \), let \( U_+ = \{ \A : \A\tp = \A \} \) be the symmetric matrices and \( U_- = \{ \A : \A\tp = -\A \} \) the skew-symmetric ones (@def-symmetric-matrix). Then \( M_n(F) = U_+ \oplus U_- \).
:::

::: {.solution}
Both are subspaces: \( 0\tp = 0 = -0 \), and by @thm-transpose-properties, \( (\A + \B)\tp = \A\tp + \B\tp \) and \( (c\A)\tp = c\A\tp \), so the equations \( \A\tp = \pm \A \) survive sums and scalar multiples.

Since the characteristic is not \( 2 \), we have \( 2 = 1 + 1 \ne 0 \) in \( F \), so \( \frac12 \) exists (@def-characteristic). For \( \A \in M_n(F) \),
\[
\A = \tfrac12 (\A + \A\tp) + \tfrac12 (\A - \A\tp).
\]
By @thm-transpose-properties, \( \big(\tfrac12(\A + \A\tp)\big)\tp = \tfrac12(\A\tp + \A) \) and \( \big(\tfrac12(\A - \A\tp)\big)\tp = \tfrac12(\A\tp - \A) = -\tfrac12(\A - \A\tp) \). So the first piece is in \( U_+ \), the second in \( U_- \), and \( M_n(F) = U_+ + U_- \).

If \( \A \in U_+ \cap U_- \), then \( \A = \A\tp = -\A \), so \( 2\A = 0 \). Multiplying by \( \frac12 \) gives \( \A = 0 \). Hence \( U_+ \cap U_- = \{0\} \), and \( M_n(F) = U_+ \oplus U_- \) by @thm-direct-sum-criteria. The pattern is the same as even plus odd: transpose plays the role of \( x \mapsto -x \).
:::

The hypothesis on the characteristic is used twice, both times to divide by \( 2 \). @exr-sums-and-direct-sums-c1 shows what goes wrong over \( \nF_2 \).

::: {.check}
Can two \( 2 \)-dimensional subspaces of \( \nR^3 \) form a direct sum?
:::

::: {.solution}
No. If the sum \( U + W \) were direct, @thm-direct-sum-criteria (c) would give \( \dim(U + W) = 2 + 2 = 4 \). But \( U + W \subseteq \nR^3 \), so \( \dim(U + W) \le 3 \) by @thm-subspace-dimension. So two planes through \( \0 \) in \( \nR^3 \) always share a non-zero vector.
:::

## Direct sums of several subspaces

For \( k \ge 3 \) subspaces, the tidy condition \( U \cap W = \{\0\} \) has no direct replacement by pairwise intersections; we will see why in a moment. What does carry over is the zero vector test, which looks just like linear independence, and a condition that compares each subspace with the sum of **all the others**.

::: {#thm-direct-sum-k-criteria}
[Direct Sum Criteria for Several Subspaces]

Let \( U_1, \dots, U_k \) be subspaces of a vector space \( V \), and write \( S = U_1 + \dots + U_k \). The following are equivalent:

::: {.enumerate options="label=(\alph*)"}
1. the sum \( S \) is direct;
2. the only way to write \( \0 = \u_1 + \dots + \u_k \) with \( \u_i \in U_i \) is \( \u_1 = \dots = \u_k = \0 \);
3. for **every** \( j = 1, \dots, k \),
   \[
   U_j \cap \sum_{i \ne j} U_i = \{\0\}.
   \]
:::

If moreover each \( U_i \) is finite-dimensional with a basis \( \sB_i \), and \( \sB \) is the list obtained by writing \( \sB_1, \dots, \sB_k \) one after another, then (a)–(c) are also equivalent to

::: {.enumerate options="label=(\alph*)"}
4. \( \sB \) is a basis of \( S \);
5. \( \dim S = \dim U_1 + \dots + \dim U_k \).
:::
:::

Here \( \sum_{i \ne j} U_i \) is the sum of the \( k - 1 \) subspaces other than \( U_j \) (and \( \{\0\} \) if \( k = 1 \)).

::: {.idea}
Condition (b) is uniqueness for the single vector \( \0 \), and just as for independence, uniqueness for \( \0 \) gives uniqueness everywhere by taking differences. For (b) ⇔ (c), a non-trivial way of writing \( \0 \) is the same thing as a non-zero vector \( \u_j \) that equals minus the sum of the other pieces. For (d), a combination of \( \sB \) groups into one piece per \( U_i \); independence of each \( \sB_i \) turns "piece is \( \0 \)" into "coefficients are \( 0 \)". Finally (d) ⇔ (e) is count instead of check: \( \sB \) always spans \( S \), so it is a basis exactly when its length is right.
:::

::: {.proof}
(a) ⇒ (b). The vector \( \0 \in S \) has the splitting \( \0 = \0 + \dots + \0 \). If the sum is direct, it has no other, which is (b).

(b) ⇒ (a). Assume (b), and let \( \u_1 + \dots + \u_k = \u_1' + \dots + \u_k' \) with \( \u_i, \u_i' \in U_i \). Subtracting and regrouping,
\[
(\u_1 - \u_1') + \dots + (\u_k - \u_k') = \0,
\]
where \( \u_i - \u_i' \in U_i \) because \( U_i \) is a subspace. By (b), \( \u_i - \u_i' = \0 \), that is, \( \u_i = \u_i' \), for every \( i \). Hence every vector of \( S \) has only one splitting.

(b) ⇒ (c). Assume (b), fix \( j \), and let \( \v \in U_j \cap \sum_{i \ne j} U_i \). Then \( \v = \sum_{i \ne j} \u_i \) for some \( \u_i \in U_i \), and so
\[
\u_1 + \dots + \u_{j-1} + (-\v) + \u_{j+1} + \dots + \u_k = \0,
\]
with \( -\v \in U_j \) in the \( j \)-th slot. By (b), every piece is \( \0 \); in particular \( -\v = \0 \), so \( \v = \0 \).

(c) ⇒ (b). Assume (c), and let \( \u_1 + \dots + \u_k = \0 \) with \( \u_i \in U_i \). Fix \( j \). Then
\[
\u_j = -\sum_{i \ne j} \u_i = \sum_{i \ne j} (-\u_i).
\]
The left side lies in \( U_j \), and the right side lies in \( \sum_{i \ne j} U_i \) since each \( -\u_i \in U_i \). By (c), \( \u_j = \0 \). As \( j \) was arbitrary, all pieces are \( \0 \).

For the rest, assume each \( U_i \) is finite-dimensional with basis \( \sB_i = (\b_{i1}, \dots, \b_{im_i}) \), where \( m_i = \dim U_i \). By @prp-sum-of-spans, \( \sB \) spans \( S = \Span(\sB_1) + \dots + \Span(\sB_k) \). In particular \( S \) is finite-dimensional.

(b) ⇒ (d). Since \( \sB \) spans \( S \), it remains to prove independence. Let \( \sum_{i=1}^{k} \sum_{r=1}^{m_i} a_{ir}\b_{ir} = \0 \), and group the terms by subspace: put \( \u_i = \sum_{r=1}^{m_i} a_{ir}\b_{ir} \in U_i \). Then \( \u_1 + \dots + \u_k = \0 \), so each \( \u_i = \0 \) by (b). Since \( \sB_i \) is independent, \( a_{i1} = \dots = a_{im_i} = 0 \) for each \( i \). Hence \( \sB \) is independent, and so a basis of \( S \).

(d) ⇒ (b). Assume (d), and let \( \u_1 + \dots + \u_k = \0 \) with \( \u_i \in U_i \). Since \( \sB_i \) spans \( U_i \), write \( \u_i = \sum_{r=1}^{m_i} a_{ir}\b_{ir} \). Then \( \sum_{i=1}^{k} \sum_{r=1}^{m_i} a_{ir}\b_{ir} = \0 \) is a combination of the independent list \( \sB \), so every \( a_{ir} = 0 \), and therefore every \( \u_i = \0 \).

(d) ⇒ (e). The list \( \sB \) has length \( m_1 + \dots + m_k \), so if it is a basis of \( S \), then \( \dim S = \dim U_1 + \dots + \dim U_k \) by @def-dimension.

(e) ⇒ (d). The list \( \sB \) spans \( S \) and has length \( m_1 + \dots + m_k \), which equals \( \dim S \) by (e). A spanning list whose length is the dimension is a basis (@thm-right-size-basis). This proves the theorem.
:::

For \( k = 2 \), condition (c) reads \( U_1 \cap U_2 = \{\0\} \) and \( U_2 \cap U_1 = \{\0\} \), so we recover @thm-direct-sum-criteria. The criteria (d) and (e) say that **bases of the pieces assemble into a basis of a direct sum, and dimensions add.**

For \( k \ge 3 \), the tempting shortcut is to check only the intersections of the subspaces two at a time. It does not work.

::: {.warning}
**Pairwise intersections \( \{\0\} \) do not make a sum direct.** In \( \nR^2 \), take the three lines \( X \) (the \( x \)-axis), \( Y \) (the \( y \)-axis) and \( D \) (the line \( y = x \)). Any two of them meet only in \( \0 \). But
\[
(1, 0) + (0, 1) + (-1, -1) = (0, 0)
\]
writes \( \0 \) with non-zero pieces from \( X \), \( Y \), \( D \), so (b) fails and \( X + Y + D \) is **not** direct. Condition (c) sees the problem: \( D \cap (X + Y) = D \cap \nR^2 = D \ne \{\0\} \).
:::

The same example breaks another tempting generalization. For finite sets, \( \lvert A \cup B \cup C \rvert \) is given by inclusion–exclusion, and the dimension formula looks like its two-set case. For three subspaces the analogous formula would be
\[
\dim(U_1 + U_2 + U_3) \overset{?}{=} \sum_i \dim U_i - \sum_{i < j} \dim(U_i \cap U_j) + \dim(U_1 \cap U_2 \cap U_3).
\]
For \( X, Y, D \) the left side is \( \dim \nR^2 = 2 \), and the right side is \( 1 + 1 + 1 - 0 - 0 - 0 + 0 = 3 \). So the formula is **false**. The reason is that \( U + W \) is not a union: the dimension of \( (U_1 + U_2) \cap U_3 \) is not determined by the pairwise intersections. @exr-sums-and-direct-sums-c3 gives the correct replacement and a second failure.

## Complements

Given a subspace \( U \) of \( V \), can we always find a subspace \( W \) with \( V = U \oplus W \)? Such a \( W \) is called a **complement** of \( U \) in \( V \). In \( \nR^3 \), the plane \( U \) of @exm-plane-line-direct-sum has the complement \( \Span((1, 1, 1)) \). In finite dimension, complements always exist, and the proof is again "basis of the smaller space, then extend".

::: {#thm-complement-exists}
[Existence of Complements]

Let \( V \) be a finite-dimensional vector space and \( U \) a subspace of \( V \). Then there is a subspace \( W \) of \( V \) with \( V = U \oplus W \). Every such \( W \) satisfies \( \dim W = \dim V - \dim U \).
:::

::: {.proof}
By @thm-subspace-dimension, \( U \) is finite-dimensional; let \( (\u_1, \dots, \u_m) \) be a basis of \( U \) (@cor-basis-existence). This list is independent in \( V \), so by the Basis Extension Theorem (@thm-basis-extension) there are \( \w_1, \dots, \w_r \in V \) such that \( (\u_1, \dots, \u_m, \w_1, \dots, \w_r) \) is a basis of \( V \). Put \( W = \Span(\w_1, \dots, \w_r) \), a subspace by @thm-span-subspace.

By @prp-sum-of-spans, \( U + W = \Span(\u_1, \dots, \u_m, \w_1, \dots, \w_r) = V \). The list \( (\w_1, \dots, \w_r) \) is independent, since a relation \( c_1\w_1 + \dots + c_r\w_r = \0 \) is also a relation \( 0\u_1 + \dots + 0\u_m + c_1\w_1 + \dots + c_r\w_r = \0 \) among the basis vectors of \( V \), forcing all \( c_k = 0 \). So \( (\w_1, \dots, \w_r) \) is a basis of \( W \). The concatenation of the bases of \( U \) and \( W \) is a basis of \( U + W = V \), so the sum is direct by @thm-direct-sum-k-criteria ((d) ⇒ (a)). Hence \( V = U \oplus W \).

Finally, if \( W \) is any subspace with \( V = U \oplus W \), then \( W \) is finite-dimensional (@thm-subspace-dimension), and @thm-direct-sum-criteria (c) gives \( \dim V = \dim U + \dim W \), as claimed.
:::

The proof made a choice: the vectors \( \w_1, \dots, \w_r \) that extend the basis. Different choices give different complements.

\begin{center}
\begin{tikzpicture}[scale=1.1]
    \draw[->, gray] (-2.6, 0) -- (2.8, 0) node[right] {$x$};
    \draw[->, gray] (0, -2.2) -- (0, 2.4) node[above] {$y$};
    \draw[very thick] (-2.4, 0) -- (2.4, 0);
    \node[below] at (2.2, 0) {$U$};
    \draw[thick, dashed] (0, -2.0) -- (0, 2.0);
    \node[right] at (0, 1.95) {$W$};
    \draw[thick, dotted] (-2.0, -2.0) -- (2.0, 2.0);
    \node[right] at (2.0, 2.0) {$W'$};
    \fill (1, 1) circle (1.5pt) node[left] {$(1,1)$};
\end{tikzpicture}
\end{center}

::: {.warning}
**A complement is not unique.** In \( \nR^2 \), the \( x \)-axis \( U \) (solid) has the complement \( W \), the \( y \)-axis (dashed), and also the complement \( W' \), the line \( y = x \) (dotted), as shown in the examples after @def-direct-sum. So "the complement of \( U \)" is meaningless, and \( U \oplus W = U \oplus W' \) does **not** allow us to cancel \( U \) and conclude \( W = W' \). What all complements share is their dimension. Also, a complement is not the set complement \( V \setminus U \), which does not even contain \( \0 \).
:::

Complements matter because a splitting \( V = U \oplus W \) lets us study \( V \) one piece at a time. In Chapter 3 each such splitting gives a projection of \( V \) onto \( U \) along \( W \), and the warning above becomes visible there: different complements give different projections. In Chapter 8 the eigenspaces of a diagonalizable operator split \( V \) as a direct sum, and that is what makes such operators easy to understand.

## Exercises

### A. Check your understanding

::: {#exr-sums-and-direct-sums-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the sum \( U_1 + \dots + U_k \) of subspaces of \( V \), and what it means for the sum to be direct.
2. State the dimension formula for \( \dim(U + W) \), with its hypotheses.
3. True or false: if \( V = U + W \) and \( U \cap W = \{\0\} \), then \( V = U \oplus W \). Justify your answer.
4. True or false: if \( U_1, U_2, U_3 \) are subspaces with \( U_i \cap U_j = \{\0\} \) for all \( i \ne j \), then the sum \( U_1 + U_2 + U_3 \) is direct. Justify your answer.
5. True or false: if \( U \) is a subspace of \( V \) with \( U \ne V \), then \( V \setminus U \) is a complement of \( U \). Justify your answer.
6. Name the method used to prove the dimension formula, in four steps.
:::
:::

::: {.solution}
(a) See @def-sum-of-subspaces: \( U_1 + \dots + U_k = \{ \u_1 + \dots + \u_k : \u_i \in U_i \} \). By @def-direct-sum, the sum is direct if every vector in it can be written as \( \u_1 + \dots + \u_k \) with \( \u_i \in U_i \) in exactly one way.

(b) If \( U \) and \( W \) are finite-dimensional subspaces of a vector space \( V \), then \( \dim(U + W) = \dim U + \dim W - \dim(U \cap W) \) (@thm-dimension-formula-subspace-dim).

(c) True. By @thm-direct-sum-criteria, \( U \cap W = \{\0\} \) means the sum \( U + W \) is direct, and it equals \( V \).

(d) False. The three lines \( X \), \( Y \), \( D \) in \( \nR^2 \) (the axes and the line \( y = x \)) meet pairwise only in \( \0 \), but \( (1, 0) + (0, 1) + (-1, -1) = \0 \) is a non-trivial way to write \( \0 \), so the sum is not direct by @thm-direct-sum-k-criteria.

(e) False. \( V \setminus U \) does not contain \( \0 \), because \( \0 \in U \). So it is not a subspace, and cannot be a complement.

(f) Take a basis of the smallest space \( U \cap W \); extend it to bases of \( U \) and of \( W \) (Basis Extension); prove the Big Claim that all the vectors together form a basis of \( U + W \) (spanning, then independence by moving one block across and noting the common vector lies in \( U \cap W \)); count.
:::

### B. Practice

::: {#exr-sums-and-direct-sums-b1}
[B1: Two Planes in \( \nR^4 \)]

Let \( U = \Span((1, 2, 0, 1), (0, 1, 1, 0)) \) and \( W = \Span((1, 3, 1, 1), (0, 0, 1, 1)) \) in \( \nR^4 \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \dim U = \dim W = 2 \).
2. Find \( U \cap W \) and its dimension.
3. Hence find \( \dim(U + W) \) and a basis of \( U + W \).
:::
:::

::: {.solution}
(a) If \( a(1, 2, 0, 1) + b(0, 1, 1, 0) = (a, 2a + b, b, a) = \0 \), then \( a = 0 \) and \( b = 0 \) from the first and third entries. So the spanning list of \( U \) is independent, hence a basis, and \( \dim U = 2 \). Similarly \( c(1, 3, 1, 1) + d(0, 0, 1, 1) = (c, 3c, c + d, c + d) = \0 \) forces \( c = 0 \), then \( d = 0 \), so \( \dim W = 2 \).

(b) A vector lies in \( U \cap W \) exactly when \( (a, 2a + b, b, a) = (c, 3c, c + d, c + d) \) for some \( a, b, c, d \in \nR \). The first entries give \( a = c \). The second gives \( 2a + b = 3a \), so \( b = a \). The third gives \( a = a + d \), so \( d = 0 \); the fourth, \( a = a + 0 \), then holds. So the common vectors are \( (a, 3a, a, a) = a(1, 3, 1, 1) \), and \( U \cap W = \Span((1, 3, 1, 1)) \), of dimension \( 1 \).

(c) By the dimension formula (@thm-dimension-formula-subspace-dim), \( \dim(U + W) = 2 + 2 - 1 = 3 \). Following its proof: \( ((1, 3, 1, 1), (0, 1, 1, 0)) \) is a list in \( U \) (by (b), \( (1, 3, 1, 1) \in U \cap W \)). It is independent by @lem-append-independent, since a multiple \( c(1, 3, 1, 1) \) with first entry \( 0 \) is \( \0 \ne (0, 1, 1, 0) \). It has length \( 2 = \dim U \), hence it is a basis of \( U \) by @thm-right-size-basis. Likewise \( ((1, 3, 1, 1), (0, 0, 1, 1)) \) is a basis of \( W \). By the Big Claim in the proof, \( ((1, 3, 1, 1), (0, 1, 1, 0), (0, 0, 1, 1)) \) is a basis of \( U + W \).
:::

::: {#exr-sums-and-direct-sums-b2}
[B2: A Plane and a Line]

Let \( U = \{ (x, y, z) \in \nR^3 : x - 2y + z = 0 \} \) and \( L = \Span((1, 0, 1)) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \nR^3 = U \oplus L \).
2. Write \( (2, 0, 4) \) as \( \u + \w \) with \( \u \in U \) and \( \w \in L \).
:::
:::

::: {.solution}
(a) Solving for \( x \), every vector of \( U \) is \( (2y - z, y, z) = y(2, 1, 0) + z(-1, 0, 1) \). These two vectors are independent (look at the second and third entries), so \( \dim U = 2 \). Since \( (1, 0, 1) \ne \0 \), \( \dim L = 1 \). If \( t(1, 0, 1) \in U \), then \( t - 0 + t = 2t = 0 \), so \( t = 0 \); hence \( U \cap L = \{\0\} \). By @thm-direct-sum-criteria, \( \dim(U + L) = 2 + 1 = 3 \), so \( U + L = \nR^3 \) by @thm-dim-impl-eq. Therefore \( \nR^3 = U \oplus L \).

(b) We need \( t \) with \( (2, 0, 4) - t(1, 0, 1) = (2 - t, 0, 4 - t) \in U \), that is, \( (2 - t) - 0 + (4 - t) = 0 \). This gives \( t = 3 \). So
\[
(2, 0, 4) = (-1, 0, 1) + 3(1, 0, 1),
\]
and indeed \( -1 - 0 + 1 = 0 \), so \( (-1, 0, 1) \in U \). By (a) this is the only such splitting.
:::

::: {#exr-sums-and-direct-sums-b3}
[B3: Direct or Not?]

Determine which of the following sums are direct. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \Span(1, x^2) + \Span(x, x^3) \) in \( \nR[x]_{\le 3} \).
2. \( T_{\mathrm{up}} + T_{\mathrm{low}} \) in \( M_2(\nR) \), where \( T_{\mathrm{up}} \) and \( T_{\mathrm{low}} \) are the upper and lower triangular matrices.
3. \( \Span((1, 0, 0)) + \Span((0, 1, 0)) + \Span((1, 1, 1)) \) in \( \nR^3 \).
4. \( \Span((1, 1, 0)) + \Span((0, 1, 1)) + \Span((1, 0, -1)) \) in \( \nR^3 \).
:::
:::

::: {.solution}
(a) Direct. If \( p \in \Span(1, x^2) \cap \Span(x, x^3) \), then \( p = a + bx^2 = cx + dx^3 \). Comparing coefficients of \( 1, x, x^2, x^3 \) gives \( a = c = b = d = 0 \), so \( p = 0 \). By @thm-direct-sum-criteria the sum is direct.

(b) Not direct. The identity matrix \( \I_2 \) is both upper and lower triangular, so \( \I_2 \in T_{\mathrm{up}} \cap T_{\mathrm{low}} \ne \{0\} \), and @thm-direct-sum-criteria applies.

(c) Direct. Each line has the basis given by its spanning vector, and we check that the concatenated list \( ((1, 0, 0), (0, 1, 0), (1, 1, 1)) \) is independent. If \( a(1, 0, 0) + b(0, 1, 0) + c(1, 1, 1) = (a + c, b + c, c) = \0 \), then \( c = 0 \), hence \( a = 0 \) and \( b = 0 \). The list spans the sum by @prp-sum-of-spans, so it is a basis of the sum, and the sum is direct by @thm-direct-sum-k-criteria ((d) ⇒ (a)).

(d) Not direct, although any two of the three lines meet only in \( \0 \) (no spanning vector is a multiple of another). Indeed
\[
(1, 1, 0) + (-1)(0, 1, 1) + (-1)(1, 0, -1) = (0, 0, 0)
\]
writes \( \0 \) as a sum of **non-zero** pieces from the three lines, so condition (b) of @thm-direct-sum-k-criteria fails.
:::

### C. Going deeper

::: {#exr-sums-and-direct-sums-c1}
[C1: Symmetric Plus Skew over \( \nF_2 \)]

Let \( U_+ \) and \( U_- \) be the symmetric and skew-symmetric matrices in \( M_2(\nF_2) \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( U_+ = U_- \).
2. Deduce that \( M_2(\nF_2) \ne U_+ \oplus U_- \). Which step of @exm-direct-sum-of-matrix fails, and why?
:::
:::

::: {.solution}
(a) In \( \nF_2 \) we have \( 1 + 1 = 0 \), so \( -a = a \) for every \( a \in \nF_2 \), and hence \( -\A = \A \) for every \( \A \in M_2(\nF_2) \). Therefore \( \A\tp = -\A \) holds if and only if \( \A\tp = \A \), which says \( U_- = U_+ \).

(b) By (a), \( U_+ \cap U_- = U_+ \), which contains \( \I_2 \ne 0 \). So the sum is not direct (@thm-direct-sum-criteria). It is not even all of \( M_2(\nF_2) \): \( U_+ + U_- = U_+ + U_+ = U_+ \), and \( \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) is not symmetric. In @exm-direct-sum-of-matrix both halves of the proof divide by \( 2 \): the splitting \( \A = \frac12(\A + \A\tp) + \frac12(\A - \A\tp) \) and the step from \( 2\A = 0 \) to \( \A = 0 \). In \( \nF_2 \), \( 2 = 1 + 1 = 0 \) has no inverse, so neither step is available. This is exactly the case of characteristic \( 2 \) excluded by the hypothesis.
:::

::: {#exr-sums-and-direct-sums-c2}
[C2: Subspaces That Must Meet]

::: {.enumerate options="label=(\alph*)"}
1. Let \( V \) be a vector space of dimension \( n \), and let \( U \), \( W \) be subspaces with \( \dim U + \dim W > n \). Prove that \( U \cap W \ne \{\0\} \).
2. Deduce that any two \( 3 \)-dimensional subspaces of \( \nR[x]_{\le 4} \) contain a common non-zero polynomial.
3. Give an example showing that (a) fails if "\( > \)" is replaced by "\( = \)".
:::
:::

::: {.solution}
(a) By @thm-subspace-dimension, \( U \), \( W \) and \( U + W \) are finite-dimensional, and \( \dim(U + W) \le \dim V = n \). By the dimension formula (@thm-dimension-formula-subspace-dim),
\[
\dim(U \cap W) = \dim U + \dim W - \dim(U + W) \ge \dim U + \dim W - n > 0.
\]
A subspace of positive dimension has a basis with at least one vector, which is non-zero because a list containing \( \0 \) is dependent. Hence \( U \cap W \ne \{\0\} \).

(b) \( \dim \nR[x]_{\le 4} = 5 \) and \( 3 + 3 = 6 > 5 \). By (a), the two subspaces meet in a non-zero polynomial.

(c) In \( \nR^2 \) (with \( n = 2 \)), the \( x \)-axis and the \( y \)-axis have \( 1 + 1 = 2 = n \), but their intersection is \( \{\0\} \).
:::

::: {#exr-sums-and-direct-sums-c3}
[C3: Three Subspaces]

::: {.enumerate options="label=(\alph*)"}
1. Let \( U_1, U_2, U_3 \) be subspaces of a vector space \( V \). Show that \( (U_1 + U_2) + U_3 = U_1 + U_2 + U_3 \).
2. Now let \( U_1, U_2, U_3 \) be finite-dimensional. Prove that
   \[
   \dim(U_1 + U_2 + U_3) = \dim U_1 + \dim U_2 + \dim U_3 - \dim(U_1 \cap U_2) - \dim\big((U_1 + U_2) \cap U_3\big).
   \]
3. In \( \nR^3 \), let \( U_1 = \{ z = 0 \} \), \( U_2 = \{ y = 0 \} \) and \( U_3 = \{ y = z \} \). Compute \( \dim(U_1 + U_2 + U_3) \), every \( \dim(U_i \cap U_j) \) and \( \dim(U_1 \cap U_2 \cap U_3) \). Show that the inclusion–exclusion formula fails, and compare with (b).
:::

*Hint: for (b), apply the dimension formula twice.*
:::

::: {.solution}
(a) Both sides are subspaces by @thm-subspace-sum. The right side contains \( U_1 \) and \( U_2 \), hence \( U_1 + U_2 \) (@thm-subspace-sum), and it contains \( U_3 \); so it contains \( (U_1 + U_2) + U_3 \) by @thm-subspace-sum. Conversely, an element \( \u_1 + \u_2 + \u_3 \) of the right side is the sum of \( \u_1 + \u_2 \in U_1 + U_2 \) and \( \u_3 \in U_3 \), so it lies in the left side.

(b) By @thm-dimension-formula-subspace-dim, \( U_1 + U_2 \) is finite-dimensional with \( \dim(U_1 + U_2) = \dim U_1 + \dim U_2 - \dim(U_1 \cap U_2) \). Applying the formula again to \( U_1 + U_2 \) and \( U_3 \), and using (a),
\[
\dim(U_1 + U_2 + U_3) = \dim(U_1 + U_2) + \dim U_3 - \dim\big((U_1 + U_2) \cap U_3\big).
\]
Substituting the first equation into the second gives the formula.

(c) Each \( U_i \) is a plane, so \( \dim U_i = 2 \): \( U_1 = \Span(\e_1, \e_2) \), \( U_2 = \Span(\e_1, \e_3) \), \( U_3 = \Span(\e_1, \e_2 + \e_3) \), each with an evidently independent spanning list. All three contain the \( x \)-axis \( \Span(\e_1) \).

- \( U_1 \cap U_2 = \{ y = z = 0 \} = \Span(\e_1) \).
- \( U_1 \cap U_3 = \{ z = 0, y = z \} = \{ y = z = 0 \} = \Span(\e_1) \).
- \( U_2 \cap U_3 = \{ y = 0, y = z \} = \Span(\e_1) \).
- \( U_1 \cap U_2 \cap U_3 = \Span(\e_1) \).

So each of these has dimension \( 1 \). Since \( U_1 + U_2 \) contains \( \e_1, \e_2, \e_3 \), it is \( \nR^3 \), and so \( U_1 + U_2 + U_3 = \nR^3 \) has dimension \( 3 \). The inclusion–exclusion formula would give
\[
2 + 2 + 2 - 1 - 1 - 1 + 1 = 4 \ne 3,
\]
so it fails. In (b), the last term is \( (U_1 + U_2) \cap U_3 = \nR^3 \cap U_3 = U_3 \), of dimension \( 2 \), and indeed \( 2 + 2 + 2 - 1 - 2 = 3 \). The inclusion–exclusion guess replaces this \( 2 \) by \( \dim(U_1 \cap U_3) + \dim(U_2 \cap U_3) - \dim(U_1 \cap U_2 \cap U_3) = 1 + 1 - 1 = 1 \), which is wrong because \( (U_1 + U_2) \cap U_3 \) is much bigger than \( (U_1 \cap U_3) + (U_2 \cap U_3) = \Span(\e_1) \).
:::
