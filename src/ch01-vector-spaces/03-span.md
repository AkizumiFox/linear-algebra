# Linear Combinations and Span

We now have vector spaces and, inside them, subspaces. So far every subspace has been handed to us by a condition, such as "\( x + 2y = 0 \)" or "\( \A\tp = \A \)". This section goes the other way. We start from a few vectors, build everything that can be built from them, and show that the result is always a subspace: the smallest one containing the vectors we started with. Along the way we meet the first way of measuring a space, by asking whether finitely many vectors are enough to build all of it.

## Linear combinations

Take two vectors in \( \nR^3 \), say \( \v_1 = (1, 0, 1) \) and \( \v_2 = (0, 1, 1) \). Which vectors can we build from them, using only the two operations a vector space gives us? Scaling gives \( a\v_1 \) and \( b\v_2 \), and adding gives
\[
a\v_1 + b\v_2 = (a, b, a + b).
\]
Adding or scaling again produces nothing new: for instance \( 2(a\v_1 + b\v_2) + (c\v_1 + d\v_2) = (2a + c)\v_1 + (2b + d)\v_2 \) has the same shape. So the vectors we can reach are exactly those of the form \( (a, b, a + b) \): the plane \( z = x + y \) through the origin. The expression \( a\v_1 + b\v_2 \) will appear in almost every argument from now on, so it deserves a name.

The vectors we combine come as a **list** \( (\v_1, \dots, \v_k) \): a finite sequence of vectors, in order, in which repeats are allowed. A list of length \( k = 0 \) is the **empty list** \( () \). Why lists rather than sets becomes important in the next section; for now it costs nothing.

::: {#def-linear-combination}
[Linear Combination]

Let \( V \) be a vector space over \( F \), and let \( (\v_1, \dots, \v_k) \) be a list of vectors in \( V \), where \( k \ge 0 \). A **linear combination** of \( (\v_1, \dots, \v_k) \) is a vector of the form
\[
a_1\v_1 + a_2\v_2 + \dots + a_k\v_k, \qquad \text{where } a_1, \dots, a_k \in F.
\]
The scalars \( a_i \) are the **coefficients** of the combination. A linear combination of the empty list is, by convention, the **empty sum** \( \0 \).
:::

In words: scale each vector of the list by a scalar from \( F \), then add up the results. Two small points hide in the notation. First, a sum of \( k \) vectors needs no brackets, because addition in \( V \) is associative (VS2); so the expression names a single vector. Second, the coefficients must lie in the field \( F \) we are working over. Changing the field can change what counts as a combination, as @exr-span-c2 shows.

The empty sum convention is the additive twin of \( 0! = 1 \) and \( x^0 = 1 \), where a product with no factors is the neutral element \( 1 \) for multiplication: a sum with no terms is the neutral element \( \0 \) for addition. It will make several statements true without exceptions.

::: {#exm-linear-combinations}
[Linear Combinations in Four Families]

Show that each vector is a linear combination of the given list.

::: {.enumerate options="label=(\alph*)"}
1. \( (3, -2, 1) \in \nR^3 \), of the list \( ((1, 0, 1), (0, 1, 1)) \).
2. \( x^2 - 1 \in \nR[x] \), of the list \( ((x + 1)^2, x + 1) \).
3. The function \( \sin^2 \) in \( \nR^\nR \), of the list \( (1, \cos 2x) \), where \( 1 \) is the constant function.
4. The zero vector of any vector space \( V \), of any list \( (\v_1, \dots, \v_k) \) in \( V \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. We need \( a(1, 0, 1) + b(0, 1, 1) = (a, b, a + b) \) to equal \( (3, -2, 1) \). The first two entries force \( a = 3 \) and \( b = -2 \), and then the third entry is \( a + b = 1 \), as required. Hence \( (3, -2, 1) = 3(1, 0, 1) - 2(0, 1, 1) \).
2. Expanding, \( (x + 1)^2 - 2(x + 1) = x^2 + 2x + 1 - 2x - 2 = x^2 - 1 \). So the coefficients are \( 1 \) and \( -2 \).
3. The double-angle formula \( \cos 2x = 1 - 2\sin^2 x \) holds for every real \( x \). Hence \( \sin^2 x = \tfrac12 \cdot 1 + \bigl(-\tfrac12\bigr) \cos 2x \) for every \( x \), which is an equality of functions by @def-function. The coefficients \( \tfrac12 \) and \( -\tfrac12 \) are real, as they must be.
4. Take every coefficient to be \( 0 \). By @thm-zero-scalar-mult, \( 0\v_i = \0 \) for each \( i \), so \( 0\v_1 + \dots + 0\v_k = \0 \). For the empty list, \( \0 \) is the empty sum. This degenerate case matters: it says the zero vector can always be built, from anything, even from nothing.
:::
:::

Notice that the question in (a) was a small system of equations in the unknown coefficients. That is typical: deciding whether a vector is a combination of a list means deciding whether a system of linear equations has a solution. Here we solve such systems by hand; Chapter 2 gives a systematic method.

## The span

*The span of some vectors is everything you can build from them by scaling and adding.*

We have two kinds of input to cover. Usually we start from a list, as above. But sometimes the natural input is a set, possibly infinite, such as all the powers \( 1, x, x^2, \dots \) in \( F[x] \). A linear combination only ever uses finitely many vectors, so for a set we allow every finite list drawn from it.

::: {#def-span}
[Span]

Let \( V \) be a vector space over \( F \).

- The **span** of a list \( (\v_1, \dots, \v_k) \) of vectors in \( V \) is the set of **all** its linear combinations:
\[
\Span(\v_1, \dots, \v_k) = \{ a_1\v_1 + \dots + a_k\v_k : a_1, \dots, a_k \in F \}.
\]
- The **span** of a subset \( S \subseteq V \), possibly infinite, is the set of all vectors that are linear combinations of **some finite** list of vectors in \( S \):
\[
\Span(S) = \{ a_1\s_1 + \dots + a_k\s_k : k \ge 0,\ \s_1, \dots, \s_k \in S,\ a_1, \dots, a_k \in F \}.
\]

In particular \( \Span() = \Span(\varnothing) = \{ \0 \} \). When the field matters we write \( \Span_F \).
:::

In words: for a list, the span collects every choice of coefficients. For a set, we may first pick any finite number of vectors from \( S \) (the same vector more than once is allowed), and then any coefficients. The value \( k = 0 \) is allowed, and it contributes the empty sum \( \0 \). So \( \0 \in \Span(S) \) for **every** \( S \), including \( S = \varnothing \).

**One thing to check.** A list \( (\v_1, \dots, \v_k) \) now has two spans: the span of the list, and the span of the set \( \{ \v_1, \dots, \v_k \} \) of its entries. They agree. A combination of the list is a combination of a finite list from the set, so the first is contained in the second. Conversely, take a combination \( b_1\w_1 + \dots + b_m\w_m \) where each \( \w_r \) is one of the \( \v_i \); for each \( r \), choose one index \( i(r) \) with \( \w_r = \v_{i(r)} \). Group the terms with the same index together, using (VS1), (VS2) and \( b\v + b'\v = (b + b')\v \) (VS6). The result is \( a_1\v_1 + \dots + a_k\v_k \), where \( a_i \) is the sum of the \( b_r \) with \( i(r) = i \) (and \( a_i = 0 \) if there are none, by @thm-zero-scalar-mult). So the second is contained in the first. In particular the span of a list does not change if we reorder the list or repeat an entry.

**Why \( \Span(\varnothing) = \{ \0 \} \)?** The definition forces it through the empty sum, but it is also the only sensible choice. We will prove that the span of \( S \) is the smallest subspace containing \( S \). The smallest subspace containing nothing in particular is \( \{ \0 \} \), since every subspace contains \( \0 \). Any other convention would make that theorem false for \( S = \varnothing \), and the empty list will turn out to be a basis of the zero space.

::: {#exm-spans}
[Computing Spans]

Describe each span.

::: {.enumerate options="label=(\alph*)"}
1. \( \Span((1, 0, 1), (0, 1, 1)) \) in \( \nR^3 \). Is \( (1, 2, 3) \) in it? Is \( (1, 2, 4) \)?
2. \( \Span(\v) \) for a single vector \( \v \) in a vector space \( V \).
3. \( \Span(1, x^2) \) in \( \nR[x] \).
4. \( \Span(\{ 1, x, x^2, x^3, \dots \}) \) in \( F[x] \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. As computed at the start of the section, the combinations are \( a(1, 0, 1) + b(0, 1, 1) = (a, b, a + b) \). So the span is \( \{ (x, y, z) \in \nR^3 : z = x + y \} \), a plane through the origin. For membership, a vector \( (x, y, z) \) is in the span exactly when the entries fit: the first two entries force \( a = x \) and \( b = y \), and then we need \( z = x + y \). Since \( 3 = 1 + 2 \), the vector \( (1, 2, 3) = 1(1, 0, 1) + 2(0, 1, 1) \) is in the span. Since \( 4 \neq 1 + 2 \), the vector \( (1, 2, 4) \) is not.
2. \( \Span(\v) = \{ a\v : a \in F \} \). If \( \v \neq \0 \) and \( V = \nR^2 \) or \( \nR^3 \), this is the line through the origin in the direction of \( \v \). If \( \v = \0 \), then \( a\0 = \0 \) for every \( a \) (@thm-scalar-zero-vector), so \( \Span(\0) = \{ \0 \} \). This degenerate case shows that a span can be as small as the zero space even when the list is not empty.
3. The combinations are \( a + bx^2 \) with \( a, b \in \nR \): the polynomials of degree at most \( 2 \) with no \( x \) term. For example \( x^2 + x \) is **not** in the span, because its coefficient of \( x \) is \( 1 \neq 0 \) and polynomials are equal only when all coefficients agree (@def-polynomial).
4. Every polynomial \( a_0 + a_1x + \dots + a_Nx^N \) is a combination of the finite list \( (1, x, \dots, x^N) \) of vectors in the set. Conversely every combination of finitely many powers of \( x \) is a polynomial. So the span is all of \( F[x] \). No single polynomial here is a combination of *infinitely* many powers: each one uses only the powers up to its degree.
:::
:::

::: {.check}
Is \( \Span((1, 2)) \) a subset of \( \Span((2, 4)) \) in \( \nR^2 \)? Are they equal?
:::

::: {.solution}
Yes to both. Since \( (2, 4) = 2(1, 2) \), every \( a(2, 4) = (2a)(1, 2) \) lies in \( \Span((1, 2)) \). Since \( (1, 2) = \tfrac12 (2, 4) \), every \( a(1, 2) = \tfrac{a}{2}(2, 4) \) lies in \( \Span((2, 4)) \). Both spans are the line \( y = 2x \). Different lists can have the same span.
:::

## The span is the smallest subspace

The plane in @exm-spans (a) was a subspace. That was no accident. Adding two combinations gives a combination, and so does scaling one. And any subspace that contains the vectors must contain all their combinations, because a subspace is closed under exactly the operations that build them. So the span is both a subspace and the smallest one available:

::: {#thm-span-subspace}
[Span Is the Smallest Subspace]

Let \( V \) be a vector space over \( F \) and let \( S \subseteq V \). Then:

::: {.enumerate options="label=(\arabic*)"}
1. \( \Span(S) \) is a subspace of \( V \);
2. \( S \subseteq \Span(S) \);
3. if \( U \) is a subspace of \( V \) with \( S \subseteq U \), then \( \Span(S) \subseteq U \).
:::

The same holds for the span of a list, which equals the span of the set of its entries.
:::

::: {.idea}
Part (1) is the three-check subspace test. Part (2) is the combination \( 1\s \). Part (3) is "a subspace is closed under the operations that build combinations"; since a combination has \( k \) terms for an arbitrary \( k \), we add one term at a time, by induction on \( k \).
:::

::: {.proof}
(1) We apply @thm-subspace-test.

- *Zero.* The empty list is a finite list of vectors in \( S \), and its only combination is \( \0 \). Hence \( \0 \in \Span(S) \).
- *Addition.* Let \( \x, \y \in \Span(S) \). Then \( \x = a_1\s_1 + \dots + a_k\s_k \) and \( \y = b_1\t_1 + \dots + b_m\t_m \) for some \( \s_i, \t_j \in S \) and scalars \( a_i, b_j \in F \). Therefore
\[
\x + \y = a_1\s_1 + \dots + a_k\s_k + b_1\t_1 + \dots + b_m\t_m ,
\]
which is a combination of the list \( (\s_1, \dots, \s_k, \t_1, \dots, \t_m) \) of vectors in \( S \). (If some \( \t_j \) equals some \( \s_i \), the list has a repeat, which lists allow.) Hence \( \x + \y \in \Span(S) \). This shows \( \Span(S) \) is closed under addition.
- *Scaling.* Let \( \x = a_1\s_1 + \dots + a_k\s_k \in \Span(S) \) and \( c \in F \). By (VS5), applied \( k - 1 \) times, and by (VS7) for each term,
\[
c\x = (ca_1)\s_1 + \dots + (ca_k)\s_k ,
\]
which is a combination of the same list. Hence \( c\x \in \Span(S) \). This shows \( \Span(S) \) is closed under scalar multiplication.

Therefore \( \Span(S) \) is a subspace of \( V \).

(2) Let \( \s \in S \). By (VS8), \( \s = 1\s \), which is a combination of the list \( (\s) \). Hence \( \s \in \Span(S) \).

(3) Let \( U \) be a subspace with \( S \subseteq U \). By @thm-subspace-test, \( U \) contains \( \0 \) and is closed under addition and scalar multiplication. We prove by induction on \( k \ge 0 \) (@thm-induction) that every combination \( a_1\s_1 + \dots + a_k\s_k \) with \( \s_i \in S \) lies in \( U \). For \( k = 0 \) the combination is \( \0 \in U \). Suppose the claim holds for \( k \), and consider \( a_1\s_1 + \dots + a_{k+1}\s_{k+1} \). By the induction hypothesis \( \x = a_1\s_1 + \dots + a_k\s_k \in U \). Since \( \s_{k+1} \in S \subseteq U \) and \( U \) is closed under scaling, \( a_{k+1}\s_{k+1} \in U \). Since \( U \) is closed under addition, \( \x + a_{k+1}\s_{k+1} \in U \). This completes the induction, and shows \( \Span(S) \subseteq U \).
:::

In one phrase: \( \Span(S) \) is a subspace containing \( S \), and it sits inside every other one. So "the smallest subspace containing \( S \)" makes sense, and it is \( \Span(S) \). This gives a second, top-down description of the span, which does not mention combinations at all.

::: {#cor-span-intersection}
[Span as an Intersection]

Let \( V \) be a vector space and \( S \subseteq V \). Let \( \sU \) be the set of all subspaces \( U \) of \( V \) with \( S \subseteq U \). Then
\[
\Span(S) = \bigcap_{U \in \sU} U .
\]
:::

::: {.proof}
The index set \( \sU \) is non-empty, because \( V \) is a subspace of itself containing \( S \); so the intersection is defined (@def-indexed-family).

(⊆) By @thm-span-subspace (3), \( \Span(S) \subseteq U \) for every \( U \in \sU \). Hence \( \Span(S) \) is contained in the intersection.

(⊇) By @thm-span-subspace (1) and (2), \( \Span(S) \) is itself a member of \( \sU \). An intersection is contained in each of its members, so the intersection is contained in \( \Span(S) \).

By @thm-double-inclusion, the two sets are equal.
:::

By @thm-intersection-subspaces, an intersection of subspaces is a subspace, so the right-hand side is a subspace for a reason that never mentions combinations. The two descriptions complement each other. The bottom-up one (combinations) tells us what the elements look like. The top-down one (intersection) is convenient for proving that the span lies inside something.

::: {.warning}
The span of \( S \) is **not** \( S \), and it is a subspace **even when \( S \) is not**. For example \( S = \{ (1, 0), (0, 1) \} \) is a two-element set, and not a subspace of \( \nR^2 \) (it does not contain \( (0, 0) \)). Its span is the whole plane \( \nR^2 \), since \( (x, y) = x(1, 0) + y(0, 1) \). By @thm-span-subspace, \( \Span(S) = S \) holds exactly when \( S \) is already a subspace. Also keep the two uses of the word apart: "the span of \( S \)" is a noun, a subspace; "\( S \) spans \( V \)" is a verb, defined next.
:::

## Spanning lists and finite-dimensional spaces

The most important case is when the span is everything. Then the list is a complete toolkit for the space: every vector can be built from it.

::: {#def-spanning-set}
[Spanning List, Spanning Set]

Let \( V \) be a vector space over \( F \). A list \( (\v_1, \dots, \v_k) \) in \( V \) **spans** \( V \), or is a **spanning list** of \( V \), if \( \Span(\v_1, \dots, \v_k) = V \). A subset \( S \subseteq V \) **spans** \( V \), or is a **spanning set** of \( V \), if \( \Span(S) = V \).
:::

Since every span is contained in \( V \), to show that a list spans \( V \) we must show one thing: **every** \( \v \in V \) can be written as \( a_1\v_1 + \dots + a_k\v_k \) for **some** scalars. The scalars may depend on \( \v \), and they need not be unique.

::: {#exm-spanning-set}
[Spanning Lists]

Show that each list spans the given space.

::: {.enumerate options="label=(\alph*)"}
1. \( (\e_1, \dots, \e_n) \) in \( F^n \), where \( \e_i \) has \( 1 \) in position \( i \) and \( 0 \) elsewhere.
2. \( (1, x, x^2) \) in \( F[x]_{\le 2} \).
3. \( ((1, 1), (1, -1)) \) in \( \nR^2 \).
4. \( (\E_{11}, \E_{12}, \E_{21}, \E_{22}) \) in \( M_2(F) \), where \( \E_{ij} \) has \( 1 \) in entry \( (i, j) \) and \( 0 \) elsewhere.
5. The empty list, in the zero space \( \{ \0 \} \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Let \( (x_1, \dots, x_n) \in F^n \). Adding entry by entry, \( x_1\e_1 + \dots + x_n\e_n = (x_1, \dots, x_n) \). So every vector is a combination, with its own entries as coefficients.
2. Every \( p \in F[x]_{\le 2} \) has the form \( a_0 + a_1x + a_2x^2 \) (@def-polynomials-bounded-degree), which is the combination \( a_0 \cdot 1 + a_1 \cdot x + a_2 \cdot x^2 \).
3. Let \( (p, q) \in \nR^2 \). We look for \( a, b \) with \( a(1, 1) + b(1, -1) = (p, q) \), that is,
\[
a + b = p, \qquad a - b = q.
\]
Adding the equations gives \( 2a = p + q \), and subtracting gives \( 2b = p - q \). So \( a = \tfrac{p + q}{2} \) and \( b = \tfrac{p - q}{2} \). Check: \( \tfrac{p + q}{2} + \tfrac{p - q}{2} = p \) and \( \tfrac{p + q}{2} - \tfrac{p - q}{2} = q \). Hence \( (p, q) = \tfrac{p + q}{2}(1, 1) + \tfrac{p - q}{2}(1, -1) \), and the list spans \( \nR^2 \). For instance \( (3, 5) = 4(1, 1) - (1, -1) \).
4. For any matrix, \( \begin{pmatrix} a & b \\ c & d \end{pmatrix} = a\E_{11} + b\E_{12} + c\E_{21} + d\E_{22} \), by adding entry by entry.
5. \( \Span() = \{ \0 \} \) by @def-span. So the empty list spans the zero space. (So does the list \( (\0) \).)
:::
:::

The solution of (3) divided by \( 2 \), which is fine in \( \nR \). Over \( \nF_2 \), where \( 2 = 0 \), the same list fails: there \( 1 = -1 \), so both vectors equal \( (1, 1) \), and their span is \( \{ (0, 0), (1, 1) \} \neq \nF_2^2 \). Whether a list spans depends on the field.

Now the non-example, by a minimal change of (3). Replace the list by \( ((1, 2), (2, 4)) \). It still has two vectors, and neither is zero. But every combination is
\[
a(1, 2) + b(2, 4) = (a + 2b)(1, 2),
\]
a vector whose second entry is twice its first. So \( (0, 1) \) is **not** reached, and the list does **not** span \( \nR^2 \). The clause that fails is "**every** \( \v \in V \) is a combination". The two vectors point along the same line, so their span is only the line \( y = 2x \).

Some spaces are spanned by a short list; others need infinitely many vectors. That distinction is the first coarse measurement of size in this book.

::: {#def-finite-dimensional}
[Finite-Dimensional]

A vector space \( V \) over \( F \) is **finite-dimensional** if **some** finite list of vectors in \( V \) spans \( V \). Otherwise \( V \) is **infinite-dimensional**.
:::

By @exm-spanning-set, \( F^n \), \( F[x]_{\le 2} \), \( M_2(F) \) and \( \{ \0 \} \) are finite-dimensional. The same argument as in (2) and (4) shows that \( F[x]_{\le n} \) and \( M_{m \times n}(F) \) are finite-dimensional too. The word "dimension" is used before we have defined a number called dimension; that number, and the fact that it is well defined, are the subject of section 6 of this chapter.

For the whole polynomial space no finite list is enough. The reason is degree: finitely many polynomials have a largest degree, and combining them never climbs above it.

::: {#thm-polynomials-infinite-dimensional}
[\( F\lbrack x\rbrack \) Is Infinite-Dimensional]

For every field \( F \), the vector space \( F[x] \) is infinite-dimensional.
:::

::: {.proof}
Let \( (p_1, \dots, p_k) \) be any finite list in \( F[x] \). We show it does not span \( F[x] \). Each \( \deg p_i \) is either a natural number or \( -\infty \), and there are finitely many, so we can choose \( N \in \nN \) with \( \deg p_i \le N \) for every \( i \).

Let \( a_1, \dots, a_k \in F \). The coefficients of \( a_ip_i \) are \( a_i \) times those of \( p_i \) (@exm-vector-spaces (c)). Every coefficient of \( x^m \) with \( m > N \) in \( p_i \) is \( 0 \), by @def-degree, and \( a_i \cdot 0 = 0 \) by (F6) and @thm-field-basic-properties (d); hence \( \deg(a_ip_i) \le N \). By @thm-degree-of-sum, \( \deg(p + q) \le \max(\deg p, \deg q) \), so a sum of two polynomials of degree at most \( N \) has degree at most \( N \). Applying this \( k - 1 \) times, \( \deg(a_1p_1 + \dots + a_kp_k) \le N \). (For \( k = 0 \) the combination is \( 0 \), of degree \( -\infty \le N \).)

Hence every element of \( \Span(p_1, \dots, p_k) \) has degree at most \( N \). But \( x^{N+1} \in F[x] \) has degree \( N + 1 > N \), so \( x^{N+1} \notin \Span(p_1, \dots, p_k) \). Since the list was arbitrary, no finite list spans \( F[x] \). This shows \( F[x] \) is infinite-dimensional.
:::

(In the proof we wrote polynomials in plain italic, \( p \), as in Chapter 0; they are vectors of \( F[x] \) all the same.) The proof is the move "find a quantity that combinations cannot increase". The space \( \nR^\nR \) of all functions is infinite-dimensional too, and so are the sequence spaces; we return to such spaces in section 8 of this chapter.

::: {.remark}
For an arbitrary subset \( S \subseteq V \), finite or infinite, "\( S \) spans \( V \)" means that **every** vector of \( V \) is a combination of **some finite** list of vectors in \( S \). Different vectors may use different finite lists, as in @exm-spans (d). We never form infinite sums: a vector space only lets us add two vectors at a time, so only finite sums have a meaning. The same "every finite list" reading will be used for independence of an arbitrary set in the next section.
:::

## Working with spans

Three facts make spans easy to manipulate. Each follows from @thm-span-subspace without writing a single combination.

::: {#prp-span-basic-properties}
[Basic Properties of Span]

Let \( V \) be a vector space and \( S, T \subseteq V \).

::: {.enumerate options="label=(\arabic*)"}
1. If \( T \subseteq \Span(S) \), then \( \Span(T) \subseteq \Span(S) \).
2. (Monotonicity) If \( T \subseteq S \), then \( \Span(T) \subseteq \Span(S) \).
3. \( \Span(\Span(S)) = \Span(S) \).
:::
:::

::: {.proof}
(1) By @thm-span-subspace (1), \( \Span(S) \) is a subspace, and by hypothesis it contains \( T \). By @thm-span-subspace (3) applied to \( T \), \( \Span(T) \subseteq \Span(S) \).

(2) By @thm-span-subspace (2), \( T \subseteq S \subseteq \Span(S) \). Now apply (1).

(3) Taking \( T = \Span(S) \) in (1) gives \( \Span(\Span(S)) \subseteq \Span(S) \). The reverse inclusion is @thm-span-subspace (2) applied to the set \( \Span(S) \).
:::

Part (1) is the workhorse. To show \( \Span(T) \subseteq \Span(S) \), it is enough to check that each vector **of \( T \)** is a combination of vectors of \( S \); we do not have to handle every combination of \( T \).

The next fact is the one later sections lean on most. If a vector can already be built from \( S \), then adding it to \( S \) builds nothing new.

::: {#thm-span-absorb}
[Absorbing a Vector into a Span]

Let \( V \) be a vector space, \( S \subseteq V \) and \( \v \in V \). If \( \v \in \Span(S) \), then
\[
\Span(S \cup \{ \v \}) = \Span(S).
\]
In particular, for a list: if \( \v \in \Span(\v_1, \dots, \v_k) \), then \( \Span(\v_1, \dots, \v_k, \v) = \Span(\v_1, \dots, \v_k) \), and the same holds with \( \v \) inserted at any position of the list.
:::

::: {.proof}
(⊇) Since \( S \subseteq S \cup \{ \v \} \), monotonicity (@prp-span-basic-properties (2)) gives \( \Span(S) \subseteq \Span(S \cup \{ \v \}) \).

(⊆) By @thm-span-subspace (2), \( S \subseteq \Span(S) \), and \( \v \in \Span(S) \) by hypothesis. Hence \( S \cup \{ \v \} \subseteq \Span(S) \), and @prp-span-basic-properties (1) gives \( \Span(S \cup \{ \v \}) \subseteq \Span(S) \).

For the list version, the span of a list equals the span of the set of its entries, whatever the order. The entries of \( (\v_1, \dots, \v_k, \v) \) form the set \( \{ \v_1, \dots, \v_k \} \cup \{ \v \} \), so the first part applies.
:::

Concretely, the proof substitutes. If \( \v = c_1\v_1 + \dots + c_k\v_k \), then any combination \( a_1\v_1 + \dots + a_k\v_k + b\v \) equals \( (a_1 + bc_1)\v_1 + \dots + (a_k + bc_k)\v_k \), which no longer uses \( \v \). Read backwards, the lemma says that a vector lying in the span of the others can be **deleted** from a list without shrinking its span. The next section turns this into the idea of a redundant vector, and section 6 of this chapter uses it at every step of the Exchange Theorem.

::: {#exm-same-span}
[Two Lists with the Same Span]

Show that \( \Span(1 + x, 1 - x) = \Span(1, x) \) in \( \nR[x] \).
:::

::: {.solution}
(⊆) Both \( 1 + x = 1 \cdot 1 + 1 \cdot x \) and \( 1 - x = 1 \cdot 1 + (-1) \cdot x \) lie in \( \Span(1, x) \). By @prp-span-basic-properties (1), \( \Span(1 + x, 1 - x) \subseteq \Span(1, x) \).

(⊇) Conversely,
\[
1 = \tfrac12 (1 + x) + \tfrac12 (1 - x), \qquad x = \tfrac12 (1 + x) - \tfrac12 (1 - x),
\]
so both \( 1 \) and \( x \) lie in \( \Span(1 + x, 1 - x) \). By @prp-span-basic-properties (1) again, \( \Span(1, x) \subseteq \Span(1 + x, 1 - x) \).

Hence the spans are equal; both are \( \nR[x]_{\le 1} \). Notice that we only checked four vectors, not all combinations. We also used \( \tfrac12 \), so the argument needs \( 2 \neq 0 \) in the field.
:::

::: {.check}
Is \( x^2 + 1 \in \Span(x^2 + x, x + 1) \) in \( \nR[x] \)?
:::

::: {.solution}
No. Suppose \( a(x^2 + x) + b(x + 1) = x^2 + 1 \). The left side is \( ax^2 + (a + b)x + b \). Comparing coefficients (@def-polynomial): \( a = 1 \) from \( x^2 \), \( b = 1 \) from the constant term, and \( a + b = 0 \) from \( x \). But then \( a + b = 2 \neq 0 \), a contradiction. So no such \( a, b \) exist.
:::

## Exercises

### A. Check your understanding

::: {#exr-span-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the span of a subset \( S \) of a vector space \( V \). What is \( \Span(\varnothing) \), and why?
2. Determine whether the following statement is true: "for a subset \( S \subseteq V \), \( \Span(S) = S \) if and only if \( S \) is a subspace of \( V \)." Justify your answer.
3. Determine whether the following statement is true: "if \( \Span(S) = \Span(T) \), then \( S = T \)." Justify your answer.
4. Is the zero vector in the span of every list? Is it in the span of the empty list?
5. State what it means for \( V \) to be finite-dimensional, and name the quantity used to show that \( F[x] \) is not.
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. \( \Span(S) \) is the set of all linear combinations \( a_1\s_1 + \dots + a_k\s_k \) with \( k \ge 0 \), \( \s_i \in S \) and \( a_i \in F \). \( \Span(\varnothing) = \{ \0 \} \): the only combination with no vectors is the empty sum \( \0 \). This is also the smallest subspace containing \( \varnothing \), as @thm-span-subspace requires.
2. True. If \( \Span(S) = S \), then \( S \) is a subspace by @thm-span-subspace (1). Conversely, if \( S \) is a subspace, then \( \Span(S) \subseteq S \) by @thm-span-subspace (3) with \( U = S \), and \( S \subseteq \Span(S) \) by (2).
3. False. In \( \nR^2 \), take \( S = \{ (1, 0), (0, 1) \} \) and \( T = \{ (1, 1), (1, -1) \} \). Both span \( \nR^2 \) (@exm-spanning-set), but \( S \neq T \).
4. Yes to both: take all coefficients \( 0 \), or, for the empty list, the empty sum. See @exm-linear-combinations (d).
5. \( V \) is finite-dimensional if some finite list of vectors in \( V \) spans \( V \). For \( F[x] \) the quantity is the degree: combinations of a finite list have degree at most the largest degree in the list (@thm-polynomials-infinite-dimensional).
:::
:::

### B. Practice

::: {#exr-span-b1}
[B1: Membership in a Span]

Determine whether each vector lies in the given span. If it does, write it as a linear combination. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( (2, -1, 5) \) and \( (3, 4, 1) \), in \( \Span((1, 1, 0), (0, 1, 1)) \subseteq \nR^3 \).
2. \( 2x^2 - 3x + 1 \) and \( x^2 + x + 1 \), in \( \Span(x^2 - x, x - 1) \subseteq \nR[x] \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. A combination is \( a(1, 1, 0) + b(0, 1, 1) = (a, a + b, b) \). For \( (2, -1, 5) \), the first and third entries force \( a = 2 \) and \( b = 5 \); then the middle entry would be \( 7 \neq -1 \). Hence \( (2, -1, 5) \) is **not** in the span. For \( (3, 4, 1) \), we get \( a = 3 \), \( b = 1 \), and the middle entry is \( 4 \), as required. Hence \( (3, 4, 1) = 3(1, 1, 0) + (0, 1, 1) \) is in the span.
2. A combination is \( a(x^2 - x) + b(x - 1) = ax^2 + (b - a)x - b \). Compare coefficients (@def-polynomial). For \( 2x^2 - 3x + 1 \): \( a = 2 \), \( -b = 1 \) so \( b = -1 \), and then \( b - a = -3 \), as required. Hence \( 2x^2 - 3x + 1 = 2(x^2 - x) - (x - 1) \) is in the span. For \( x^2 + x + 1 \): \( a = 1 \), \( b = -1 \), and then \( b - a = -2 \neq 1 \). Hence \( x^2 + x + 1 \) is **not** in the span. (Every element \( p \) of this span has \( p(1) = a - a + b - b = 0 \), and indeed \( x^2 + x + 1 \) has value \( 3 \) at \( 1 \).)
:::
:::

::: {#exr-span-b2}
[B2: Two Lists with the Same Span]

Prove that \( \Span((1, 1, 0), (0, 1, 1)) = \Span((1, 2, 1), (1, 0, -1)) \) in \( \nR^3 \).
:::

::: {.solution}
Write \( \u = (1, 1, 0) \), \( \w = (0, 1, 1) \).

(⊆) We have \( \u = \tfrac12 (1, 2, 1) + \tfrac12 (1, 0, -1) \) and \( \w = \tfrac12 (1, 2, 1) - \tfrac12 (1, 0, -1) \): indeed \( \tfrac12(2, 2, 0) = (1, 1, 0) \) and \( \tfrac12 (0, 2, 2) = (0, 1, 1) \). So \( \u, \w \in \Span((1, 2, 1), (1, 0, -1)) \), and @prp-span-basic-properties (1) gives the inclusion.

(⊇) We have \( (1, 2, 1) = \u + \w \) and \( (1, 0, -1) = \u - \w \). So both lie in \( \Span(\u, \w) \), and @prp-span-basic-properties (1) gives the reverse inclusion.

Hence the two spans are equal.
:::

::: {#exr-span-b3}
[B3: Spans in \( \nR^3 \), Geometrically]

Describe each span as the origin, a line through the origin, a plane through the origin (give an equation), or all of \( \nR^3 \). Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \Span((1, 2, 3)) \).
2. \( \Span((1, 0, 0), (0, 1, 0), (1, 1, 0)) \).
3. \( \Span((1, -1, 0), (0, 1, -1)) \).
4. \( \Span((0, 0, 0)) \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. The span is \( \{ (t, 2t, 3t) : t \in \nR \} \): the line through the origin and \( (1, 2, 3) \).
2. Since \( (1, 1, 0) = (1, 0, 0) + (0, 1, 0) \), @thm-span-absorb gives \( \Span((1, 0, 0), (0, 1, 0), (1, 1, 0)) = \Span((1, 0, 0), (0, 1, 0)) = \{ (a, b, 0) : a, b \in \nR \} \): the plane \( z = 0 \).
3. A combination is \( a(1, -1, 0) + b(0, 1, -1) = (a, b - a, -b) \), whose entries sum to \( 0 \). Conversely, if \( x + y + z = 0 \), take \( a = x \) and \( b = -z \); then \( b - a = -z - x = y \), so \( (x, y, z) = x(1, -1, 0) - z(0, 1, -1) \). Hence the span is the plane \( x + y + z = 0 \).
4. \( \Span((0, 0, 0)) = \{ \0 \} \), by @exm-spans (b): the origin alone.
:::
:::

### C. Going deeper

::: {#exr-span-c1}
[C1: Spans of Intersections and Unions]

Let \( S, T \) be subsets of a vector space \( V \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \Span(S \cap T) \subseteq \Span(S) \cap \Span(T) \).
2. Give an example in \( \nR^2 \) where the inclusion in (a) is strict.
3. Prove that \( \Span(S \cup T) = \{ \s + \t : \s \in \Span(S),\ \t \in \Span(T) \} \).
:::

*Hint for (c): in a combination of vectors of \( S \cup T \), sort the terms into two groups.*
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Since \( S \cap T \subseteq S \), monotonicity (@prp-span-basic-properties (2)) gives \( \Span(S \cap T) \subseteq \Span(S) \). By symmetry, \( \Span(S \cap T) \subseteq \Span(T) \). Hence \( \Span(S \cap T) \subseteq \Span(S) \cap \Span(T) \).
2. Take \( S = \{ (1, 0), (0, 1) \} \) and \( T = \{ (1, 1) \} \). Then \( S \cap T = \varnothing \), so \( \Span(S \cap T) = \{ \0 \} \). But \( \Span(S) = \nR^2 \) (@exm-spanning-set), so \( \Span(S) \cap \Span(T) = \Span(T) \), the line \( y = x \), which contains \( (1, 1) \neq \0 \). The inclusion is strict.
3. Write \( W = \{ \s + \t : \s \in \Span(S),\ \t \in \Span(T) \} \).

   (⊆) Let \( \v \in \Span(S \cup T) \), say \( \v = a_1\u_1 + \dots + a_k\u_k \) with each \( \u_i \in S \cup T \). Let \( \s \) be the sum of the terms \( a_i\u_i \) with \( \u_i \in S \), and \( \t \) the sum of the remaining terms, whose vectors lie in \( T \). Since addition is commutative and associative, \( \v = \s + \t \). Now \( \s \in \Span(S) \) and \( \t \in \Span(T) \); if a group is empty, its sum is \( \0 \), which lies in every span. Hence \( \v \in W \).

   (⊇) Let \( \s \in \Span(S) \) and \( \t \in \Span(T) \). By monotonicity, both lie in \( \Span(S \cup T) \), which is closed under addition by @thm-span-subspace (1). Hence \( \s + \t \in \Span(S \cup T) \).

   By @thm-double-inclusion, \( \Span(S \cup T) = W \). (So \( W \) is the set \( \Span(S) + \Span(T) \) of @exr-subspaces-c2, the **sum** of the two subspaces, studied in section 7 of this chapter.)
:::
:::

::: {#exr-span-c2}
[C2: The Span Depends on the Field]

The set \( \nC^2 \) is a vector space over \( \nC \). With the same addition, and scalar multiplication restricted to real scalars, it is also a vector space over \( \nR \), by @exr-vector-spaces-c3: every axiom holds for all complex scalars, so in particular for real ones.

::: {.enumerate options="label=(\alph*)"}
1. Show that \( ((1, 0), (0, 1)) \) spans \( \nC^2 \) over \( \nC \).
2. Explain why \( ((1, 0), (0, 1)) \) does **not** span \( \nC^2 \) over \( \nR \).
3. Find a finite list that spans \( \nC^2 \) over \( \nR \). Hence \( \nC^2 \) is finite-dimensional over \( \nR \) as well.
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. For \( (z, w) \in \nC^2 \), \( (z, w) = z(1, 0) + w(0, 1) \) with \( z, w \in \nC \).
2. Over \( \nR \) the coefficients must be real, and \( a(1, 0) + b(0, 1) = (a, b) \) with \( a, b \in \nR \) has real entries. So \( (i, 0) \) is not in \( \Span_\nR((1, 0), (0, 1)) \).
3. Take \( ((1, 0), (i, 0), (0, 1), (0, i)) \). Write \( z = a + bi \) and \( w = c + di \) with \( a, b, c, d \in \nR \) (@def-complex-numbers). Then
\[
(z, w) = a(1, 0) + b(i, 0) + c(0, 1) + d(0, i),
\]
a combination with real coefficients. So this list spans \( \nC^2 \) over \( \nR \), and \( \nC^2 \) is finite-dimensional over \( \nR \) by @def-finite-dimensional.
:::
:::
