# Bases and Coordinates

Spanning lists and independent lists each solve half of a problem. A spanning list reaches every vector of the space, but it may reach some vectors in more than one way. An independent list never wastes a vector, but it may not reach everything. This section puts the two halves together. The result, a basis, turns an abstract vector space into columns of numbers, and we prove that every space spanned by a finite list has one.

## What makes coordinates work

Start with the plane. Every vector of \( \nR^2 \) can be written as
\[
(x, y) = x\e_1 + y\e_2,
\]
and the pair \( (x, y) \) is its address. Two separate facts make this addressing system work. First, **every** vector has an address: the list \( (\e_1, \e_2) \) spans \( \nR^2 \). Second, every vector has **only one** address: if \( x\e_1 + y\e_2 = x'\e_1 + y'\e_2 \), then \( (x, y) = (x', y') \), so \( x = x' \) and \( y = y' \).

Nothing about this is special to \( \e_1 \) and \( \e_2 \). Take instead the list \( ((1, 1), (1, -1)) \). To find an address for \( (x, y) \) we solve
\[
a(1, 1) + b(1, -1) = (x, y), \qquad\text{that is,}\qquad a + b = x, \quad a - b = y.
\]
Adding and subtracting the two equations gives \( 2a = x + y \) and \( 2b = x - y \). So there is a solution, and it is the only one:
\[
a = \frac{x + y}{2}, \qquad b = \frac{x - y}{2}.
\]
For example \( (3, 1) = 2(1, 1) + 1(1, -1) \), and no other pair of scalars works. The grid is slanted, but every point still has exactly one address.

\begin{center}
\begin{tikzpicture}[scale=0.9]
  \draw[->, gray] (-0.5,0) -- (3.8,0) node[right] {$x$};
  \draw[->, gray] (0,-1.5) -- (0,2.6) node[above] {$y$};
  \draw[dashed, gray] (2,2) -- (3,1);
  \draw[dashed, gray] (1,-1) -- (3,1);
  \draw[->, thick] (0,0) -- (1,1) node[above left] {$(1,1)$};
  \draw[->, thick] (0,0) -- (1,-1) node[below] {$(1,-1)$};
  \draw[->, thick, dotted] (1,1) -- (2,2) node[above] {$2(1,1)$};
  \draw[->, very thick] (0,0) -- (3,1) node[right] {$(3,1)$};
  \fill (3,1) circle (1.5pt);
\end{tikzpicture}
\end{center}

Look at which property did which job. **Existence** of an address is spanning. **Uniqueness** of the address is independence: by @thm-independence-unique-combination, a list is independent exactly when every vector in its span has only one expression as a combination of it. A coordinate system is a list that does both jobs at once.

*A basis is a list with enough vectors to build everything and no vector to spare.*

## Bases

::: {#def-basis}
[Basis]

Let \( V \) be a vector space over \( F \). A **basis** of \( V \) is a **list** \( (\v_1, \dots, \v_n) \) of vectors in \( V \) such that

::: {.enumerate options="label=(B\arabic*)"}
1. \( (\v_1, \dots, \v_n) \) is **linearly independent**, and
2. \( (\v_1, \dots, \v_n) \) **spans** \( V \), that is, \( \Span(\v_1, \dots, \v_n) = V \).
:::

We usually name a basis with a calligraphic letter, \( \sB = (\v_1, \dots, \v_n) \), and call \( n \) its **length**. The plural of basis is **bases**.
:::

In words: (B1) says that the only combination of the \( \v_i \) equal to \( \0 \) is the one with **all** coefficients zero, so no vector in the list is wasted. (B2) says that **every** vector of \( V \) is some combination of the \( \v_i \), so nothing is out of reach. The basis is a list, so its entries come in a definite order, and a basis is always a basis **of** a particular space: \( (\e_1, \e_2) \) is a basis of \( \nR^2 \), but not of \( \nR^3 \).

We start with the bases that come with the running examples.

::: {#exm-standard-bases}
[Standard Bases]

Show that each of the following lists is a basis. They are called the **standard bases**.

::: {.enumerate options="label=(\alph*)"}
1. \( (\e_1, \dots, \e_n) \) in \( F^n \), where \( \e_i \) has \( 1 \) in position \( i \) and \( 0 \) elsewhere.
2. \( (1, x, x^2, \dots, x^n) \) in \( F[x]_{\le n} \).
3. \( (\E_{11}, \E_{12}, \dots, \E_{1n}, \E_{21}, \dots, \E_{mn}) \) in \( M_{m \times n}(F) \), where the **matrix unit** \( \E_{ij} \) has \( 1 \) in entry \( (i, j) \) and \( 0 \) elsewhere, listed row by row.
:::
:::

::: {.solution}
(a) (B2): every \( (x_1, \dots, x_n) \in F^n \) equals \( x_1\e_1 + \dots + x_n\e_n \). (B1): let \( a_1\e_1 + \dots + a_n\e_n = \0 \). The left side is the column \( (a_1, \dots, a_n) \), so comparing entries gives \( a_1 = \dots = a_n = 0 \).

(b) (B2): by @def-polynomials-bounded-degree, every element of \( F[x]_{\le n} \) has the form \( a_0 + a_1x + \dots + a_nx^n \), which is a combination of \( 1, x, \dots, x^n \). (B1): let \( a_0 \cdot 1 + a_1x + \dots + a_nx^n = 0 \). Here \( 0 \) is the zero polynomial, all of whose coefficients are \( 0 \). Two polynomials are equal exactly when their coefficients agree (@def-polynomial), so \( a_0 = a_1 = \dots = a_n = 0 \).

(c) (B2): a matrix \( \A = (a_{ij}) \) equals \( \sum_{i, j} a_{ij}\E_{ij} \), since both sides have \( a_{ij} \) in entry \( (i, j) \). (B1): if \( \sum_{i, j} c_{ij}\E_{ij} \) is the zero matrix, then its \( (i, j) \) entry \( c_{ij} \) is \( 0 \) for every \( i, j \).
:::

The next examples show that a space has other bases, that the field matters, and what happens in the smallest space.

::: {#exm-more-bases}
[Three More Bases]

Show that each list is a basis.

::: {.enumerate options="label=(\alph*)"}
1. \( ((1, 1), (1, -1)) \) in \( \nR^2 \).
2. \( (1, i) \) in \( \nC \), regarded as a vector space **over \( \nR \)**.
3. The empty list \( () \) in the zero space \( \{\0\} \).
:::
:::

::: {.solution}
(a) We showed above that for every \( (x, y) \in \nR^2 \) the equation \( a(1, 1) + b(1, -1) = (x, y) \) has a solution, so (B2) holds. Taking \( (x, y) = (0, 0) \), the only solution is \( a = \frac{0 + 0}{2} = 0 \) and \( b = 0 \), so (B1) holds.

(b) The scalars are now real. (B2): every complex number is \( a + bi = a \cdot 1 + b \cdot i \) with \( a, b \in \nR \) (@def-complex-numbers). (B1): let \( a \cdot 1 + b \cdot i = 0 \) with \( a, b \in \nR \). A complex number is \( 0 \) exactly when its real and imaginary parts are \( 0 \), so \( a = b = 0 \).

(c) The empty list is linearly independent: there are no coefficients, so the condition "all coefficients are zero" holds vacuously. Its span is \( \{\0\} \) by the convention for the empty span. So both (B1) and (B2) hold.
:::

The degenerate case (c) matters more than it looks. Without it, the zero space would be the one space with no basis, and every theorem below would need an exception for it.

**Non-examples by minimal change.** Add one vector to the standard basis of \( \nR^2 \), making \( ((1, 0), (0, 1), (1, 1)) \). Spanning (B2) still holds, since the first two vectors already span. But (B1) fails:
\[
1 \cdot (1, 0) + 1 \cdot (0, 1) + (-1) \cdot (1, 1) = (0, 0),
\]
with coefficients **not all zero**. The effect is exactly the loss of unique addresses: \( (3, 1) = 3(1, 0) + 1(0, 1) + 0(1, 1) = 2(1, 0) + 0(0, 1) + 1(1, 1) \).

Now remove a vector instead. In \( \nR^3 \), the list \( ((1, 0, 0), (0, 1, 0)) \) is still independent, since \( a(1, 0, 0) + b(0, 1, 0) = (a, b, 0) = \0 \) forces \( a = b = 0 \). But (B2) fails: every combination \( (a, b, 0) \) has third entry \( 0 \), so \( (0, 0, 1) \) is out of reach.

::: {.check}
Is \( ((1, 2), (2, 1), (0, 0)) \) a basis of \( \nR^2 \)? If not, which of (B1) and (B2) fails?
:::

::: {.solution}
No. (B2) holds: \( (1, 2) \) and \( (2, 1) \) already span \( \nR^2 \), because solving \( a(1, 2) + b(2, 1) = (x, y) \) gives \( a = \frac{2y - x}{3} \) and \( b = \frac{2x - y}{3} \). But (B1) fails, because the list contains the zero vector: \( 0(1, 2) + 0(2, 1) + 1(0, 0) = (0, 0) \) with a non-zero coefficient.
:::

**Why this definition.** Drop (B1), and addresses stop being unique, as the list \( ((1, 0), (0, 1), (1, 1)) \) showed. Drop (B2), and some vectors have no address at all. Keeping both is exactly what an addressing system needs. The name comes from the everyday word: the basis is what everything else is built on.

::: {.remark}
Why a list and not a set? Two reasons. Coordinates, defined below, are a column of numbers, and a column needs to know which scalar comes first. And a set would hide repeats: the list \( ((1, 0), (1, 0), (0, 1)) \) is dependent, since \( 1(1, 0) - 1(1, 0) = \0 \), but as a set \( \{(1, 0), (1, 0), (0, 1)\} = \{(1, 0), (0, 1)\} \) it would look like the standard basis.
:::

::: {.warning}
Say **a** basis, not **the** basis. A space usually has many bases; a non-zero space over an infinite field such as \( \nR \) has infinitely many. For instance \( ((1, 0), (c, 1)) \) is a basis of \( \nR^2 \) for **every** real number \( c \), since \( (x, y) = (x - cy)(1, 0) + y(c, 1) \), and this is the only solution. The standard basis is a convenient choice, not a canonical one.
:::

## Unique representation and coordinates

We found the definition by asking for addresses that exist and are unique. The first result confirms that this is exactly what a basis delivers, and nothing more.

::: {#thm-unique-representation}
[Unique Representation]

Let \( V \) be a vector space over \( F \), and let \( \sB = (\v_1, \dots, \v_n) \) be a list in \( V \). Then \( \sB \) is a basis of \( V \) if and only if every \( \v \in V \) can be written as
\[
\v = a_1\v_1 + \dots + a_n\v_n \qquad (a_1, \dots, a_n \in F)
\]
in **exactly one** way.
:::

::: {.proof}
\( (\Rightarrow) \) Let \( \v \in V \). Since \( \sB \) spans \( V \), there are scalars with \( \v = a_1\v_1 + \dots + a_n\v_n \). Suppose also \( \v = b_1\v_1 + \dots + b_n\v_n \). Subtracting the two expressions and regrouping with the vector space axioms,
\[
(a_1 - b_1)\v_1 + \dots + (a_n - b_n)\v_n = \v - \v = \0.
\]
Since \( \sB \) is linearly independent, \( a_i - b_i = 0 \) for every \( i \). Hence the two expressions are the same.

\( (\Leftarrow) \) Every \( \v \in V \) is a combination of \( \sB \), so \( \sB \) spans \( V \). For independence, let \( a_1\v_1 + \dots + a_n\v_n = \0 \). We also have \( \0 = 0\v_1 + \dots + 0\v_n \). By uniqueness of the expression for the vector \( \0 \), all \( a_i = 0 \). Hence \( \sB \) is linearly independent, and \( \sB \) is a basis.
:::

This is @thm-independence-unique-combination in the special case where the span is the whole space. The theorem also gives a second way to check that a list is a basis: solve for the coefficients of a general vector, and see that there is always exactly one solution. We did exactly that for \( ((1, 1), (1, -1)) \).

Whenever something exists and is unique, it deserves a name.

::: {#def-coordinates}
[Coordinates]

Let \( \sB = (\v_1, \dots, \v_n) \) be a basis of a vector space \( V \) over \( F \), and let \( \v \in V \). The unique scalars \( a_1, \dots, a_n \) with \( \v = a_1\v_1 + \dots + a_n\v_n \) are the **coordinates** of \( \v \) **with respect to** \( \sB \). The column
\[
\coord{\v}{\sB} \coloneqq \begin{pmatrix} a_1 \\ \vdots \\ a_n \end{pmatrix} \in F^n
\]
is the **coordinate vector** of \( \v \) with respect to \( \sB \).
:::

In the standard basis of \( F^n \), the coordinate vector of \( (x_1, \dots, x_n) \) is the column \( (x_1, \dots, x_n) \) itself. That is why we rarely notice coordinates in \( F^n \). In other bases and other spaces they carry real information.

::: {#exm-polynomial-coordinates}
[Coordinates of a Polynomial]

Show that \( \sB = (1, 1 + x, 1 + x + x^2) \) is a basis of \( \nR[x]_{\le 2} \), and find \( \coord{p}{\sB} \) for \( p = 3 - x + 2x^2 \).
:::

::: {.solution}
We use @thm-unique-representation. Let \( q = q_0 + q_1x + q_2x^2 \in \nR[x]_{\le 2} \) be arbitrary. For scalars \( a, b, c \),
\[
a \cdot 1 + b(1 + x) + c(1 + x + x^2) = (a + b + c) + (b + c)x + cx^2.
\]
Two polynomials are equal exactly when their coefficients agree, so this equals \( q \) if and only if
\[
c = q_2, \qquad b + c = q_1, \qquad a + b + c = q_0.
\]
Solving from the top, \( c = q_2 \), then \( b = q_1 - q_2 \), then \( a = q_0 - q_1 \). So every \( q \) has exactly one expression, and \( \sB \) is a basis of \( \nR[x]_{\le 2} \).

For \( p = 3 - x + 2x^2 \) we have \( q_0 = 3 \), \( q_1 = -1 \), \( q_2 = 2 \). Hence \( c = 2 \), \( b = -1 - 2 = -3 \), and \( a = 3 - (-1) = 4 \):
\[
\coord{p}{\sB} = \begin{pmatrix} 4 \\ -3 \\ 2 \end{pmatrix}.
\]
Check: \( 4 - 3(1 + x) + 2(1 + x + x^2) = (4 - 3 + 2) + (-3 + 2)x + 2x^2 = 3 - x + 2x^2 \). In the standard basis \( (1, x, x^2) \), the same polynomial has coordinate vector \( (3, -1, 2) \).
:::

::: {.warning}
Coordinates depend on the basis **and on its order**. Take \( \v = (3, 1) \in \nR^2 \). With respect to the standard basis \( \sE = (\e_1, \e_2) \), \( \coord{\v}{\sE} = (3, 1) \). With respect to \( \sB = ((1, 1), (1, -1)) \), \( \coord{\v}{\sB} = (2, 1) \). With respect to \( \sB' = ((1, -1), (1, 1)) \), the same two vectors in the other order, \( \coord{\v}{\sB'} = (1, 2) \). A column of numbers means nothing until you say which ordered basis it refers to.
:::

The point of coordinates is that they turn computations in \( V \) into computations with columns. That works because they respect the two operations.

::: {#thm-coordinates-linear}
[Coordinates Respect the Operations]

Let \( \sB = (\v_1, \dots, \v_n) \) be a basis of a vector space \( V \) over \( F \). Then for all \( \u, \v \in V \) and \( c \in F \),
\[
\coord{\u + \v}{\sB} = \coord{\u}{\sB} + \coord{\v}{\sB}, \qquad \coord{c\v}{\sB} = c\,\coord{\v}{\sB}.
\]
Moreover, every column \( (a_1, \dots, a_n) \in F^n \) is the coordinate vector of exactly one vector of \( V \), namely \( a_1\v_1 + \dots + a_n\v_n \).
:::

::: {.proof}
Let \( \coord{\u}{\sB} = (a_1, \dots, a_n) \) and \( \coord{\v}{\sB} = (b_1, \dots, b_n) \). By the vector space axioms,
\[
\u + \v = \sum_{i=1}^n a_i\v_i + \sum_{i=1}^n b_i\v_i = \sum_{i=1}^n (a_i + b_i)\v_i, \qquad c\v = c\sum_{i=1}^n b_i\v_i = \sum_{i=1}^n (cb_i)\v_i.
\]
By @thm-unique-representation these are the only expressions of \( \u + \v \) and \( c\v \) in \( \sB \), so their coefficients are the coordinates: \( \coord{\u + \v}{\sB} = (a_i + b_i)_i \) and \( \coord{c\v}{\sB} = (cb_i)_i \), as claimed.

For the last statement, let \( (a_1, \dots, a_n) \in F^n \) and \( \w = a_1\v_1 + \dots + a_n\v_n \). By @def-coordinates, \( \coord{\w}{\sB} = (a_1, \dots, a_n) \). If also \( \coord{\w'}{\sB} = (a_1, \dots, a_n) \), then by definition \( \w' = a_1\v_1 + \dots + a_n\v_n = \w \).
:::

So a basis of length \( n \) sets up a one-to-one correspondence \( \v \mapsto \coord{\v}{\sB} \) between \( V \) and \( F^n \) that respects addition and scaling. Any question about sums and multiples in \( V \) can be answered in \( F^n \) instead. In Chapter 3 we will call such a correspondence an **isomorphism**.

## Every finite spanning list contains a basis

Where do bases come from? A finite-dimensional space is, by @def-finite-dimensional, a space spanned by some finite list. That list reaches everything but may contain waste, so the natural plan is to throw the waste away.

Care is needed about **what** to throw away. In \( ((1, 0), (0, 1), (1, 1)) \) each vector is a combination of the other two. Any single one can go, but not two of them. So redundancy is not a property of one vector alone: it depends on which other vectors stay. The fix is to decide one vector at a time, reading from left to right, and to compare each vector only with the vectors already kept.

First, a small lemma that tells us when a kept list stays independent.

::: {#lem-append-independent}
[Appending a Vector to an Independent List]

Let \( (\u_1, \dots, \u_k) \) be a linearly independent list in a vector space \( V \), and let \( \v \in V \). Then \( (\u_1, \dots, \u_k, \v) \) is linearly independent **if and only if** \( \v \notin \Span(\u_1, \dots, \u_k) \).
:::

::: {.proof}
\( (\Rightarrow) \) Suppose \( \v \in \Span(\u_1, \dots, \u_k) \), say \( \v = c_1\u_1 + \dots + c_k\u_k \). Then \( c_1\u_1 + \dots + c_k\u_k + (-1)\v = \0 \), with the coefficient \( -1 \ne 0 \). So the longer list is dependent. This proves \( (\Rightarrow) \) by contraposition.

\( (\Leftarrow) \) Suppose \( \v \notin \Span(\u_1, \dots, \u_k) \), and let \( a_1\u_1 + \dots + a_k\u_k + b\v = \0 \). If \( b \ne 0 \), then \( b^{-1} \) exists and
\[
\v = -b^{-1}a_1\u_1 - \dots - b^{-1}a_k\u_k \in \Span(\u_1, \dots, \u_k),
\]
a contradiction. Hence \( b = 0 \). Then \( a_1\u_1 + \dots + a_k\u_k = \0 \), and the independence of \( (\u_1, \dots, \u_k) \) gives \( a_1 = \dots = a_k = 0 \). So all coefficients are zero, and the longer list is independent.
:::

The direction \( (\Leftarrow) \) is @exr-independence-c2. When \( k = 0 \), the lemma says that the one-vector list \( (\v) \) is independent exactly when \( \v \notin \Span() = \{\0\} \), that is, when \( \v \ne \0 \), in agreement with @exm-independence-degenerate.

Now the procedure. Given a list \( (\v_1, \dots, \v_m) \) in \( V \), **sifting** it means the following.

::: {.algorithm}
Start with the empty list \( S_0 = () \). For \( r = 1, 2, \dots, m \) in turn:

- if \( \v_r \notin \Span(S_{r-1}) \), **keep** it: \( S_r = (S_{r-1}, \v_r) \);
- if \( \v_r \in \Span(S_{r-1}) \), **discard** it: \( S_r = S_{r-1} \).

The final list \( S_m \) is the **sifted list** of \( (\v_1, \dots, \v_m) \).
:::

Here \( (S_{r-1}, \v_r) \) means the list \( S_{r-1} \) with \( \v_r \) appended at the end. Each \( S_r \) is a **sub-list** of \( (\v_1, \dots, \v_m) \): it is obtained by deleting some entries and keeping the rest in their original order.

::: {#thm-sift}
[Sifting Theorem]

Let \( (\v_1, \dots, \v_m) \) be a list in a vector space \( V \), and let \( S_m \) be its sifted list. Then \( S_m \) is linearly independent and
\[
\Span(S_m) = \Span(\v_1, \dots, \v_m).
\]
In particular, every finite list that spans \( V \) contains a sub-list that is a basis of \( V \).
:::

::: {.idea}
Sifting protects two things at every step. A vector is kept only when it lies outside the span of what was kept before, so by @lem-append-independent the kept list stays independent. A vector is discarded only when it is already in that span, so by @thm-span-absorb discarding it loses nothing. We turn "at every step" into an induction on \( r \), the number of vectors read so far, with the invariant: \( S_r \) is independent and has the same span as \( \v_1, \dots, \v_r \).
:::

::: {.proof}
We prove by induction on \( r \in \{0, 1, \dots, m\} \) the statement

> \( P(r) \): the list \( S_r \) is linearly independent and \( \Span(S_r) = \Span(\v_1, \dots, \v_r) \).

*Base case.* \( S_0 \) is the empty list, which is linearly independent, and both sides of the span equation are the span of the empty list. So \( P(0) \) holds.

*Inductive step.* Let \( 1 \le r \le m \) and suppose \( P(r - 1) \) holds. Put \( W = \Span(S_{r-1}) \), so that \( W = \Span(\v_1, \dots, \v_{r-1}) \) by \( P(r - 1) \).

*Case 1: \( \v_r \in W \).* Then \( S_r = S_{r-1} \), which is independent. Since \( \v_r \in \Span(\v_1, \dots, \v_{r-1}) \), @thm-span-absorb gives \( \Span(\v_1, \dots, \v_r) = \Span(\v_1, \dots, \v_{r-1}) = W = \Span(S_r) \).

*Case 2: \( \v_r \notin W \).* Then \( S_r = (S_{r-1}, \v_r) \). Since \( S_{r-1} \) is independent and \( \v_r \notin \Span(S_{r-1}) \), @lem-append-independent shows that \( S_r \) is independent. For the spans, recall from @thm-span-subspace that the span of a list is a subspace, and is contained in every subspace containing the entries of the list. Every entry of \( S_r \) is one of \( \v_1, \dots, \v_r \), so \( \Span(S_r) \subseteq \Span(\v_1, \dots, \v_r) \). Conversely, \( \Span(S_r) \) is a subspace containing the entries of \( S_{r-1} \), so it contains \( W \), and with it \( \v_1, \dots, \v_{r-1} \); it also contains \( \v_r \). Hence \( \Span(\v_1, \dots, \v_r) \subseteq \Span(S_r) \).

In both cases \( P(r) \) holds. By induction \( P(m) \) holds, which is the first statement.

Finally, suppose \( (\v_1, \dots, \v_m) \) spans \( V \). Then \( S_m \) is a sub-list of it that is independent and satisfies \( \Span(S_m) = V \). So \( S_m \) is a basis of \( V \).
:::

Alternatively, one can delete instead of keep. As long as the list is dependent, the Linear Dependence Lemma (@thm-linear-dependence-lemma) locates an entry lying in the span of the entries before it, and deleting that entry does not change the span. Each deletion shortens the list, so the process stops after at most \( m \) steps. Sifting performs the same idea in a single left-to-right pass.

The decision "is \( \v_r \) in the span of the kept vectors?" is a small system of equations. For now we solve these systems by hand; Chapter 2 gives a systematic method.

::: {#exm-sifting}
[Sifting a List in \( \nR^3 \)]

Sift the list \( (\v_1, \dots, \v_6) \) in \( \nR^3 \), where
\[
\begin{aligned}
&\v_1 = (1, 1, 1), \quad \v_2 = (2, 2, 2), \quad \v_3 = (1, 0, 0), \\
&\v_4 = (3, 2, 2), \quad \v_5 = (1, 1, 0), \quad \v_6 = (0, 0, 1).
\end{aligned}
\]
Hence find a basis of \( \nR^3 \) inside the list.
:::

::: {.solution}
We go through the list once, comparing each vector with the vectors kept so far.

- \( \v_1 \): the kept list is empty, with span \( \{\0\} \). Since \( \v_1 \ne \0 \), **keep** \( \v_1 \).
- \( \v_2 \): \( \v_2 = 2\v_1 \in \Span(\v_1) \). **Discard.**
- \( \v_3 \): if \( (1, 0, 0) = a(1, 1, 1) = (a, a, a) \), the first entry gives \( a = 1 \) and the second gives \( a = 0 \), a contradiction. So \( \v_3 \notin \Span(\v_1) \). **Keep.**
- \( \v_4 \): \( 2\v_1 + \v_3 = (2, 2, 2) + (1, 0, 0) = (3, 2, 2) = \v_4 \), so \( \v_4 \in \Span(\v_1, \v_3) \). **Discard.**
- \( \v_5 \): suppose \( (1, 1, 0) = a(1, 1, 1) + b(1, 0, 0) = (a + b, a, a) \). The second entry gives \( a = 1 \) and the third gives \( a = 0 \), a contradiction. So \( \v_5 \notin \Span(\v_1, \v_3) \). **Keep.**
- \( \v_6 \): \( \v_1 - \v_5 = (1, 1, 1) - (1, 1, 0) = (0, 0, 1) = \v_6 \), so \( \v_6 \in \Span(\v_1, \v_3, \v_5) \). **Discard.**

The sifted list is \( (\v_1, \v_3, \v_5) = ((1, 1, 1), (1, 0, 0), (1, 1, 0)) \). By @thm-sift it is independent and has the same span as the original list. That span is all of \( \nR^3 \), since it contains \( \e_1 = \v_3 \), \( \e_2 = \v_5 - \v_3 \) and \( \e_3 = \v_6 \), and hence every combination of them. So \( (\v_1, \v_3, \v_5) \) is a basis of \( \nR^3 \).
:::

Sifting has no memory of the future, so its output depends on the order of the input.

::: {#exm-sifting-r2}
[The Order Matters]

Sift \( ((1, 0), (0, 1), (1, 1)) \) and \( ((1, 1), (1, 0), (0, 1)) \) in \( \nR^2 \).
:::

::: {.solution}
For the first list: \( (1, 0) \ne \0 \), so keep it. Every multiple of \( (1, 0) \) has second entry \( 0 \), so \( (0, 1) \notin \Span((1, 0)) \); keep it. Then \( (1, 1) = (1, 0) + (0, 1) \); discard it. The result is \( ((1, 0), (0, 1)) \).

For the second list: \( (1, 1) \ne \0 \), so keep it. If \( (1, 0) = a(1, 1) = (a, a) \), then \( a = 1 \) and \( a = 0 \), which is impossible; keep \( (1, 0) \). Then \( (0, 1) = (1, 1) - (1, 0) \); discard it. The result is \( ((1, 1), (1, 0)) \).

Both results are bases of \( \nR^2 \) (the lists span \( \nR^2 \) because they contain \( \e_1 \) and \( \e_2 \)), but they are different bases. A zero vector, by contrast, is discarded wherever it stands, because \( \0 \) lies in every span.
:::

::: {.check}
Sift the list \( (x, 2x, 1 + x, 1) \) in \( \nR[x]_{\le 1} \). Which vectors are kept?
:::

::: {.solution}
Keep \( x \), since \( x \ne 0 \). Discard \( 2x = 2 \cdot x \). Keep \( 1 + x \): every multiple \( ax \) has constant term \( 0 \), but \( 1 + x \) has constant term \( 1 \). Discard \( 1 = (1 + x) - x \). The sifted list is \( (x, 1 + x) \).
:::

The theorem answers the question we started with.

::: {#cor-basis-existence}
[Existence of Bases]

Every finite-dimensional vector space has a basis.
:::

::: {.proof}
Let \( V \) be finite-dimensional. By @def-finite-dimensional, \( V \) is spanned by some finite list. By @thm-sift, that list contains a sub-list that is a basis of \( V \).
:::

For \( V = \{\0\} \) the proof still works: \( \{\0\} \) is spanned by the empty list, and sifting it returns the empty list, which is the basis found in @exm-more-bases.

We now know that bases exist, and we can find one inside any finite spanning list. But a space has many bases. The next section proves the fact that makes them measurable: all bases of the same space have the same length.

## Exercises

### A. Check your understanding

::: {#exr-basis-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define what it means for a list \( (\v_1, \dots, \v_n) \) to be a basis of a vector space \( V \) over \( F \).
2. True or false: every list that spans \( \nR^2 \) is a basis of \( \nR^2 \). Justify your answer.
3. True or false: \( ((1, 0), (0, 1)) \) and \( ((0, 1), (1, 0)) \) are the same basis of \( \nR^2 \). Justify your answer.
4. What is a basis of the zero space \( \{\0\} \)?
5. When sifting a list, under what condition is the vector \( \v_r \) discarded?
6. True or false: if \( \sB \) is a basis of \( V \) and \( \coord{\u}{\sB} = \coord{\v}{\sB} \), then \( \u = \v \). Justify your answer.
:::
:::

::: {.solution}
(a) See @def-basis: the list is linearly independent and spans \( V \).

(b) False. \( ((1, 0), (0, 1), (1, 1)) \) spans \( \nR^2 \), but it is dependent, since \( (1, 0) + (0, 1) - (1, 1) = \0 \).

(c) False. A basis is a list, and the two lists have their entries in different orders. The difference is visible in coordinates: \( (3, 1) \) has coordinate vector \( (3, 1) \) in the first basis and \( (1, 3) \) in the second.

(d) The empty list \( () \), by @exm-more-bases (c).

(e) When \( \v_r \) lies in the span of the vectors kept before it, that is, \( \v_r \in \Span(S_{r-1}) \).

(f) True. If both coordinate vectors equal \( (a_1, \dots, a_n) \), then \( \u = a_1\v_1 + \dots + a_n\v_n = \v \) by @def-coordinates, where \( \sB = (\v_1, \dots, \v_n) \).
:::

### B. Practice

::: {#exr-basis-b1}
[B1: A Basis of \( \nR^3 \) and Coordinates]

Let \( \sB = ((1, 1, 0), (0, 1, 1), (1, 0, 1)) \). Show that \( \sB \) is a basis of \( \nR^3 \). Hence find \( \coord{\v}{\sB} \) for \( \v = (2, 3, 5) \).
:::

::: {.solution}
Let \( (p, q, r) \in \nR^3 \). For scalars \( a, b, c \),
\[
a(1, 1, 0) + b(0, 1, 1) + c(1, 0, 1) = (a + c, \; a + b, \; b + c),
\]
so this equals \( (p, q, r) \) if and only if \( a + c = p \), \( a + b = q \) and \( b + c = r \). Adding the three equations gives \( 2(a + b + c) = p + q + r \), so \( a + b + c = \frac{p + q + r}{2} \). Subtracting each equation from this one,
\[
b = \frac{-p + q + r}{2}, \qquad c = \frac{p - q + r}{2}, \qquad a = \frac{p + q - r}{2}.
\]
Conversely, these values satisfy the three equations: for instance \( a + c = \frac{2p}{2} = p \), and the other two are checked the same way. So every vector of \( \nR^3 \) has exactly one expression in \( \sB \), and \( \sB \) is a basis by @thm-unique-representation.

For \( (p, q, r) = (2, 3, 5) \): \( a = \frac{2 + 3 - 5}{2} = 0 \), \( b = \frac{-2 + 3 + 5}{2} = 3 \), \( c = \frac{2 - 3 + 5}{2} = 2 \). Check: \( 0(1, 1, 0) + 3(0, 1, 1) + 2(1, 0, 1) = (2, 3, 5) \). Hence \( \coord{\v}{\sB} = (0, 3, 2) \).
:::

::: {#exr-basis-b2}
[B2: Sifting Polynomials]

Sift the list \( (1 + x, \; 2 + 2x, \; x^2, \; 1 + x + x^2, \; x, \; 1) \) in \( \nR[x]_{\le 2} \), justifying each decision. Hence find a basis of \( \nR[x]_{\le 2} \) contained in the list.
:::

::: {.solution}
We read the list from left to right, comparing coefficients.

- \( 1 + x \ne 0 \): **keep**.
- \( 2 + 2x = 2(1 + x) \): **discard**.
- \( x^2 \): every multiple \( a(1 + x) \) has \( x^2 \)-coefficient \( 0 \), while \( x^2 \) has \( x^2 \)-coefficient \( 1 \). So \( x^2 \notin \Span(1 + x) \): **keep**.
- \( 1 + x + x^2 = (1 + x) + x^2 \): **discard**.
- \( x \): suppose \( x = a(1 + x) + bx^2 = a + ax + bx^2 \). The constant terms give \( a = 0 \) and the \( x \)-coefficients give \( a = 1 \), a contradiction. So \( x \notin \Span(1 + x, x^2) \): **keep**.
- \( 1 = (1 + x) - x \): **discard**.

The sifted list is \( (1 + x, x^2, x) \). The original list contains \( 1 \), \( x \) and \( x^2 \), so its span contains every combination of them, which is all of \( \nR[x]_{\le 2} \) by @exm-standard-bases. Hence the list spans \( \nR[x]_{\le 2} \), and by @thm-sift the sifted list \( (1 + x, x^2, x) \) is a basis of \( \nR[x]_{\le 2} \).
:::

::: {#exr-basis-b3}
[B3: Symmetric Matrices]

Let \( U = \{ \A \in M_2(\nR) : \A\tp = \A \} \). Show that \( (\E_{11}, \; \E_{12} + \E_{21}, \; \E_{22}) \) is a basis of \( U \), and find the coordinate vector of \( \begin{pmatrix} 2 & -1 \\ -1 & 5 \end{pmatrix} \) with respect to it.
:::

::: {.solution}
Each of the three matrices is symmetric, so the list lies in \( U \).

*Spanning.* Let \( \A \in U \). Writing \( \A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \), the condition \( \A\tp = \A \) says \( c = b \). Hence
\[
\A = \begin{pmatrix} a & b \\ b & d \end{pmatrix} = a\E_{11} + b(\E_{12} + \E_{21}) + d\E_{22}.
\]

*Independence.* Let \( a\E_{11} + b(\E_{12} + \E_{21}) + d\E_{22} = 0 \). The left side is \( \begin{pmatrix} a & b \\ b & d \end{pmatrix} \), so comparing entries with the zero matrix gives \( a = b = d = 0 \).

Hence the list is a basis of \( U \). Reading off \( a = 2 \), \( b = -1 \), \( d = 5 \), the coordinate vector is \( (2, -1, 5) \).
:::

### C. Going deeper

::: {#exr-basis-c1}
[C1: Polynomials Vanishing at 1]

Let \( F \) be a field, \( n \ge 1 \), and \( U = \{ p \in F[x]_{\le n} : p(1) = 0 \} \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( (x - 1, \; x^2 - 1, \; \dots, \; x^n - 1) \) is a basis of \( U \).
2. For \( n = 3 \), find the coordinate vector of \( x^3 - 2x + 1 \) with respect to this basis.
:::

*Hint: for \( p = a_0 + a_1x + \dots + a_nx^n \), what does \( p(1) = 0 \) say about \( a_0 \)?*
:::

::: {.solution}
(a) For \( p = a_0 + a_1x + \dots + a_nx^n \), evaluation gives \( p(1) = a_0 + a_1 + \dots + a_n \), since every power of \( 1 \) is \( 1 \). In particular each \( x^k - 1 \) lies in \( U \), because \( 1 - 1 = 0 \).

*Spanning.* Let \( p \in U \). Then \( a_0 = -(a_1 + \dots + a_n) \), so
\[
\begin{aligned}
p &= a_1x + \dots + a_nx^n - (a_1 + \dots + a_n) \\
&= a_1(x - 1) + a_2(x^2 - 1) + \dots + a_n(x^n - 1).
\end{aligned}
\]

*Independence.* Let \( c_1(x - 1) + \dots + c_n(x^n - 1) = 0 \). For \( 1 \le k \le n \), the coefficient of \( x^k \) on the left is \( c_k \), since \( x^k \) appears in no other term. The zero polynomial has all coefficients \( 0 \), so \( c_k = 0 \) for every \( k \).

Hence the list is a basis of \( U \).

(b) For \( p = x^3 - 2x + 1 \) we have \( p(1) = 0 \), and \( (a_1, a_2, a_3) = (-2, 0, 1) \). By the formula in (a), \( p = -2(x - 1) + 0(x^2 - 1) + 1(x^3 - 1) \). Check: \( -2x + 2 + x^3 - 1 = x^3 - 2x + 1 \). The coordinate vector is \( (-2, 0, 1) \).
:::

::: {#exr-basis-c2}
[C2: The Same List over a Different Field]

::: {.enumerate options="label=(\alph*)"}
1. Explain why \( ((1, 1), (1, -1)) \) is **not** a basis of \( \nF_2^2 \).
2. Let \( F \) be any field. Prove that \( ((1, 1), (1, -1)) \) is a basis of \( F^2 \) if and only if \( 1 + 1 \ne 0 \) in \( F \).
:::
:::

::: {.solution}
(a) In \( \nF_2 \) we have \( -1 = 1 \), so the list is \( ((1, 1), (1, 1)) \). It is dependent: \( 1 \cdot (1, 1) + 1 \cdot (1, 1) = (1 + 1, 1 + 1) = (0, 0) \) with non-zero coefficients. (It also fails to span: every combination is \( (c, c) \), so \( (1, 0) \) is out of reach.)

(b) Write \( 2 = 1 + 1 \in F \).

\( (\Leftarrow) \) Suppose \( 2 \ne 0 \), so \( 2^{-1} \) exists. Let \( (x, y) \in F^2 \). The equation \( a(1, 1) + b(1, -1) = (x, y) \) says \( a + b = x \) and \( a - b = y \). If it holds, adding and subtracting gives \( 2a = x + y \) and \( 2b = x - y \), so \( a = 2^{-1}(x + y) \) and \( b = 2^{-1}(x - y) \). Conversely these values satisfy \( a + b = 2^{-1} \cdot 2x = x \) and \( a - b = 2^{-1} \cdot 2y = y \). So every vector has exactly one expression, and the list is a basis by @thm-unique-representation.

\( (\Rightarrow) \) Suppose \( 2 = 0 \). Then \( 1 = -1 \), and the argument of (a) applies word for word: \( 1 \cdot (1, 1) + 1 \cdot (1, -1) = (2, 0) = (0, 0) \), so the list is dependent and is not a basis. This proves \( (\Rightarrow) \) by contraposition.
:::

::: {#exr-basis-c3}
[C3: Rescaling a Basis]

Let \( \sB = (\v_1, \dots, \v_n) \) be a basis of \( V \) over \( F \), and let \( c_1, \dots, c_n \in F \) be **non-zero**.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \sB' = (c_1\v_1, \dots, c_n\v_n) \) is a basis of \( V \).
2. Express \( \coord{\v}{\sB'} \) in terms of \( \coord{\v}{\sB} \).
3. Explain why the conclusion of (a) can fail if some \( c_i = 0 \).
:::
:::

::: {.solution}
(a) Let \( \v \in V \) and \( \coord{\v}{\sB} = (a_1, \dots, a_n) \). Since each \( c_i \ne 0 \), \( c_i^{-1} \) exists, and
\[
\v = \sum_{i=1}^n a_i\v_i = \sum_{i=1}^n (a_ic_i^{-1})(c_i\v_i).
\]
So \( \v \) has an expression in \( \sB' \). Suppose \( \v = \sum_i b_i(c_i\v_i) = \sum_i (b_ic_i)\v_i \). By uniqueness of the expression in \( \sB \) (@thm-unique-representation), \( b_ic_i = a_i \) for each \( i \), so \( b_i = a_ic_i^{-1} \). Hence the expression in \( \sB' \) is unique, and \( \sB' \) is a basis by @thm-unique-representation.

(b) By (a), \( \coord{\v}{\sB'} = (a_1c_1^{-1}, \dots, a_nc_n^{-1}) \): divide the \( i \)-th coordinate by \( c_i \).

(c) If \( c_1 = 0 \), then \( \sB' \) contains \( 0\v_1 = \0 \), and \( 1 \cdot \0 + 0 \cdot c_2\v_2 + \dots + 0 \cdot c_n\v_n = \0 \) is a combination with a non-zero coefficient. So \( \sB' \) is dependent and is not a basis.
:::
