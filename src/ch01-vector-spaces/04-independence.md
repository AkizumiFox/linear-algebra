# Linear Independence

A spanning list tells us that every vector of a space can be built. It says nothing about waste. The list \( ((1, 0), (0, 1), (1, 1)) \) spans \( \nR^2 \), but its third vector adds nothing that the first two did not already reach. To measure a space by the length of a list, we need lists with no such waste. This section makes "no vector is wasted" precise, proves the lemma that finds a wasted vector whenever there is one, and shows that lists without waste give every vector in their span a unique description.

## Redundant vectors

The previous section gave a way to shorten a list: if a vector lies in the span of the others, we may delete it without changing the span (@thm-span-absorb). Call such a vector **redundant**. We want a test for "this list has no redundant vector".

A first guess is that a vector is wasted when it repeats the direction of another one, so the test would be "no vector is a scalar multiple of another". This guess fails. In \( \nR^3 \), take
\[
\u = (1, 0, 1), \qquad \v = (0, 1, 1), \qquad \w = (1, 1, 2).
\]
No one of them is a multiple of another: a multiple of \( \u \) has second entry \( 0 \), a multiple of \( \v \) has first entry \( 0 \), a multiple \( (c, c, 2c) \) of \( \w \) has equal first and second entries, and in each case neither of the other two vectors has that shape. Yet \( \w = \u + \v \). All three lie in the plane \( z = x + y \), and by @thm-span-absorb, \( \Span(\u, \v, \w) = \Span(\u, \v) \). The vector \( \w \) is redundant even though it is not parallel to anything.

A second guess is correct but clumsy: "no vector is a linear combination of the others". For a list of length \( k \) this is \( k \) separate conditions, one for each vector. Here is a way to fold them into one. Move everything in \( \w = \u + \v \) to one side:
\[
1\u + 1\v + (-1)\w = \0 .
\]
This is a way to build \( \0 \) from the list with coefficients that are **not all zero**. Conversely, suppose \( a\u + b\v + c\w = \0 \) with, say, \( c \neq 0 \). Then \( \w = -\tfrac{a}{c}\u - \tfrac{b}{c}\v \), so \( \w \) is redundant. The same works whichever coefficient is non-zero. So a redundant vector exists exactly when \( \0 \) can be built in a non-trivial way. Building \( \0 \) trivially, with every coefficient \( 0 \), is always possible, so the condition we want is that this is the only way.

*A list is independent when the only way to build the zero vector from it is the trivial way.*

## Definition and examples

::: {#def-linear-independence}
[Linear Independence]

Let \( V \) be a vector space over \( F \) and let \( (\v_1, \dots, \v_k) \) be a list of vectors in \( V \), where \( k \ge 0 \). The list is **linearly independent** (over \( F \)) if, **for all** \( a_1, \dots, a_k \in F \),
\[
a_1\v_1 + a_2\v_2 + \dots + a_k\v_k = \0 \quad \Longrightarrow \quad a_1 = a_2 = \dots = a_k = 0 .
\]
The list is **linearly dependent** if it is not linearly independent: that is, if there exist \( a_1, \dots, a_k \in F \), **not all zero**, with \( a_1\v_1 + \dots + a_k\v_k = \0 \). Such an equation is a **linear relation** among the vectors. The empty list is linearly independent.
:::

In words: the hypothesis is an arbitrary linear combination that happens to equal \( \0 \). The conclusion says that **every** coefficient in it is \( 0 \). Dependence is the negation, obtained by the rules of @def-negation-of-quantifiers: "for all \( a \), (combination \( = \0 \) \( \Rightarrow \) all \( a_i = 0 \))" becomes "there exist \( a \) with combination \( = \0 \) and **not** all \( a_i = 0 \)". This is exactly the negation worked out in @exm-negation-not-all-zero. The empty list is independent because the condition is vacuous: there are no coefficients, so "all of them are \( 0 \)" holds automatically.

The definition also dictates how every independence proof starts. It is a "for all" statement about coefficients, so we take arbitrary coefficients and assume the hypothesis:

**Let \( a_1\v_1 + \dots + a_k\v_k = \0 \).** Then … hence all \( a_i = 0 \).

Between "Let" and "hence", the work is to turn one vector equation into scalar equations. How we do that depends on what \( \0 \) means in the space: in \( F^n \) we compare entries, in \( F[x] \) we compare coefficients, in a function space we evaluate at points, and in \( M_{m \times n}(F) \) we compare entries.

::: {#exm-linear-independence}
[Independent Lists in Four Families]

Show that each list is linearly independent.

::: {.enumerate options="label=(\alph*)"}
1. \( (\e_1, \dots, \e_n) \) in \( F^n \).
2. \( (1, x, x^2) \) in \( F[x] \).
3. \( ((1, 1), (1, -1)) \) in \( \nR^2 \).
4. \( (\sin, \cos) \) in the space \( \nR^\nR \) of all functions \( \nR \to \nR \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Let \( a_1\e_1 + \dots + a_n\e_n = \0 \). The left side is the vector \( (a_1, \dots, a_n) \), and \( \0 = (0, \dots, 0) \). Comparing entries, \( a_1 = \dots = a_n = 0 \). Hence the list is independent.
2. Let \( a + bx + cx^2 = 0 \), where \( 0 \) is the **zero polynomial**, the polynomial with every coefficient \( 0 \). Two polynomials are equal exactly when all their coefficients agree (@def-polynomial). Comparing the coefficients of \( 1, x, x^2 \) gives \( a = b = c = 0 \). Hence the list is independent.
3. Let \( a(1, 1) + b(1, -1) = (0, 0) \). Comparing entries, \( a + b = 0 \) and \( a - b = 0 \). Adding the two equations gives \( 2a = 0 \), so \( a = 0 \) since \( 2 \neq 0 \) in \( \nR \); then \( b = -a = 0 \). Hence the list is independent.
4. Let \( a\sin + b\cos = 0 \), where \( 0 \) is the **zero function**. Equality of functions means equality at every point (@def-function), so \( a\sin t + b\cos t = 0 \) for **every** \( t \in \nR \). We may choose convenient points. At \( t = 0 \): \( a \cdot 0 + b \cdot 1 = 0 \), so \( b = 0 \). At \( t = \pi/2 \): \( a \cdot 1 + b \cdot 0 = 0 \), so \( a = 0 \). Hence the list is independent.
:::
:::

In (d) we did not need the equation at every point, only at two well-chosen ones. That is the general move for functions: **choose good points**, where most terms vanish. Note the logic. Evaluating at a point can only prove independence; if the equations at our chosen points had allowed non-zero solutions, we would have learned nothing, and would have to try other points or another method.

The degenerate cases are worth settling once, because they come up inside every later argument.

::: {#exm-independence-degenerate}
[Degenerate Lists]

Let \( V \) be a vector space over \( F \). Decide whether each list is independent.

::: {.enumerate options="label=(\alph*)"}
1. A list \( (\v_1, \dots, \v_k) \) with some \( \v_j = \0 \).
2. A list \( (\v) \) of length one.
3. A list \( (\v_1, \dots, \v_k) \) with a repeat: \( \v_i = \v_j \) for some \( i \neq j \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Dependent. Take \( a_j = 1 \) and every other coefficient \( 0 \). By @thm-zero-scalar-mult and @thm-scalar-zero-vector, every term is \( \0 \), so the combination is \( \0 \), and the coefficient \( a_j = 1 \) is not zero.
2. Independent if and only if \( \v \neq \0 \). If \( \v = \0 \), use (a). If \( \v \neq \0 \), let \( a\v = \0 \); by @thm-zero-product, \( a = 0 \) or \( \v = \0 \), and the second is false, so \( a = 0 \).
3. Dependent. Take \( a_i = 1 \), \( a_j = -1 \), and every other coefficient \( 0 \). The combination is \( \v_i + (-1)\v_j = \v_i - \v_j = \0 \) by @thm-negation-scalar, since \( \v_i = \v_j \), and \( a_i = 1 \neq 0 \).
:::
:::

Now the non-example, by a minimal change. Add one vector to the independent list \( ((1, 0), (0, 1)) \) of @exm-linear-independence (a), to get \( ((1, 0), (0, 1), (1, 1)) \). Each vector is still non-zero, and any two of the three still form an independent list. But
\[
1(1, 0) + 1(0, 1) + (-1)(1, 1) = (0, 0)
\]
with coefficients not all zero, so the clause "\( \Longrightarrow a_1 = \dots = a_k = 0 \)" fails, and the list is **dependent**. The polynomial version behaves the same way: \( (1, x) \) is independent, but \( (1, x, 1 + x) \) is dependent, because \( 1 \cdot 1 + 1 \cdot x + (-1)(1 + x) = 0 \).

::: {.check}
Is the list \( ((1, 2, 0), (0, 1, 1), (1, 0, -2)) \) in \( \nR^3 \) linearly independent?
:::

::: {.solution}
No. Let \( a(1, 2, 0) + b(0, 1, 1) + c(1, 0, -2) = \0 \). Comparing entries: \( a + c = 0 \), \( 2a + b = 0 \), \( b - 2c = 0 \). The first two give \( c = -a \) and \( b = -2a \), and then the third reads \( -2a + 2a = 0 \), which holds for every \( a \). Taking \( a = 1 \) gives the relation \( (1, 2, 0) - 2(0, 1, 1) - (1, 0, -2) = \0 \), with coefficients not all zero.
:::

Two more kinds of question come up constantly: lists that depend on a parameter, and lists of matrices. The method does not change.

::: {#exm-independence-parameter-and-matrices}
[A Parameter and a List of Matrices]

::: {.enumerate options="label=(\alph*)"}
1. For which \( k \in \nR \) is the list \( ((1, 1, 0), (1, 0, 1), (0, 1, k)) \) in \( \nR^3 \) linearly independent?
2. Is the list \( \left( \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \right) \) in \( M_2(\nR) \) linearly independent?
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Let \( a(1, 1, 0) + b(1, 0, 1) + c(0, 1, k) = \0 \). Comparing entries gives \( a + b = 0 \), \( a + c = 0 \) and \( b + kc = 0 \). The first two give \( b = -a \) and \( c = -a \); substituting into the third, \( -a - ka = -(1 + k)a = 0 \).

    If \( k \neq -1 \), then \( 1 + k \neq 0 \), so \( a = 0 \) by @thm-field-basic-properties, and then \( b = c = 0 \). The list is independent.

    If \( k = -1 \), the equations hold for every \( a \); taking \( a = 1 \) gives \( (1, 1, 0) - (1, 0, 1) - (0, 1, -1) = \0 \) with coefficients not all zero. The list is dependent.

    So the list is independent exactly when \( k \neq -1 \). Notice the shape of the argument: the parameter ends up as a factor multiplying one unknown, and the only question is when that factor can be zero.
2. Let \( a\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} + b\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} + c\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} \). The left side is \( \begin{pmatrix} a & b + c \\ b & a \end{pmatrix} \). Two matrices are equal when their entries agree (@def-matrix), so \( a = 0 \), \( b + c = 0 \) and \( b = 0 \); hence \( c = 0 \) too. The list is independent.

    For matrices, "compare entries" turns one matrix equation into four scalar equations, one per entry.
:::
:::

## Why lists, and why this definition

::: {.remark}
**Why lists, not sets.** In a set, repeats disappear: \( \{ \v, \v \} = \{ \v \} \). If independence were defined for sets, the "list" \( (\v, \v) \), which has the obvious relation \( \v - \v = \0 \), would silently become the independent set \( \{ \v \} \) when \( \v \neq \0 \). The repeat can also be hidden: \( x + 1 \) and \( 1 + x \) look different on the page but are the same vector. A list keeps both entries and so records the dependence. The second reason is order. Coordinates with respect to a basis (next section) are read off in order, so \( (\e_1, \e_2) \) and \( (\e_2, \e_1) \) must be different objects. The Linear Dependence Lemma below also refers to "the vectors before \( \v_j \)", which needs an order. Reordering a list does not change whether it is independent, since a relation can be rearranged term by term.
:::

For an arbitrary subset \( S \subseteq V \), finite or infinite, we say \( S \) is **linearly independent** if **every** finite list of **distinct** vectors of \( S \) is linearly independent. The word "distinct" is essential: without it, the list \( (\s, \s) \) would make every non-empty set dependent. For a finite set \( S = \{ \v_1, \dots, \v_k \} \) with the \( \v_i \) distinct, this agrees with independence of the list \( (\v_1, \dots, \v_k) \): every list of distinct vectors of \( S \) is a reordered sub-list, and a sub-list of an independent list is independent (@exr-independence-b3). Together with "\( S \) spans \( V \)" from the previous section, this is the language section 8 of this chapter uses for spaces with no finite spanning list.

**Why "all \( a_i = 0 \)", and why is the empty list independent?** Suppose we only asked that **some** \( a_i \) be \( 0 \). The list \( ((1, 0), (0, 1), (0, 2)) \) has the redundant vector \( (0, 2) = 2(0, 1) \). But in any relation \( a(1, 0) + b(0, 1) + c(0, 2) = \0 \), comparing first entries forces \( a = 0 \), so every relation has a zero coefficient, and the list would pass the weaker test. Only "**all** \( a_i = 0 \)" rules out every non-trivial relation. The empty list is independent because it wastes nothing, and this convention makes the empty list a basis of the zero space in the next section, just as \( \Span() = \{ \0 \} \) makes it a spanning list.

::: {.warning}
**"Not all zero" is not "all non-zero".** A dependence relation needs **one** non-zero coefficient, not every coefficient non-zero. The list \( ((1, 0), (0, 1), (0, 2)) \) is dependent, by \( 0(1, 0) + 2(0, 1) - (0, 2) = \0 \). But no relation has all three coefficients non-zero: comparing first entries in \( a(1, 0) + b(0, 1) + c(0, 2) = \0 \) forces \( a = 0 \). Hunting for a relation with no zero coefficient would wrongly conclude that the list is independent.
:::

::: {.warning}
**Pairwise independence is not independence.** Checking pairs is not enough. In the list \( ((1, 0, 1), (0, 1, 1), (1, 1, 2)) \) from the start of the section, every two of the three vectors form an independent list, but the three together are dependent, since \( (1, 0, 1) + (0, 1, 1) - (1, 1, 2) = \0 \). For three or more vectors, independence is a condition on all of them at once.
:::

## The Linear Dependence Lemma

The definition says that a dependent list has a relation. It does not say which vector is redundant, and the discussion at the start of the section only found a redundant vector where the coefficient was non-zero. The next lemma makes a definite choice, and chooses it so that the redundant vector depends only on vectors **before** it in the list. This one-directional form is what later proofs need, because they build lists from left to right.

::: {#thm-linear-dependence-lemma}
[Linear Dependence Lemma]

Let \( V \) be a vector space over \( F \), and let \( (\v_1, \dots, \v_k) \) be a linearly dependent list in \( V \). Then:

::: {.enumerate options="label=(\arabic*)"}
1. there is an index \( j \in \{ 1, \dots, k \} \) with \( \v_j \in \Span(\v_1, \dots, \v_{j-1}) \). For \( j = 1 \) this means \( \v_1 = \0 \), so if \( \v_1 \neq \0 \), then \( j \ge 2 \);
2. for any such \( j \), removing \( \v_j \) does not change the span:
\[
\Span(\v_1, \dots, \v_{j-1}, \v_{j+1}, \dots, \v_k) = \Span(\v_1, \dots, \v_k).
\]
:::
:::

::: {.idea}
Take a relation with coefficients not all zero. We want to solve for one vector in terms of the vectors before it, so we need a vector whose coefficient is non-zero and which comes **after** every other vector with a non-zero coefficient. That is the **largest** index \( j \) with \( a_j \neq 0 \). Everything after it has coefficient zero and drops out, and we divide by \( a_j \). Part (2) is then @thm-span-absorb read backwards.
:::

::: {.proof}
(1) Since the list is dependent, there are \( a_1, \dots, a_k \in F \), not all zero, with \( a_1\v_1 + \dots + a_k\v_k = \0 \). The set \( \{ i : a_i \neq 0 \} \) is non-empty and finite, so it has a largest element; call it \( j \). Then \( a_j \neq 0 \), and \( a_i = 0 \) for every \( i > j \). By @thm-zero-scalar-mult the terms with \( i > j \) are \( \0 \), so
\[
a_1\v_1 + \dots + a_{j-1}\v_{j-1} + a_j\v_j = \0 .
\]
Adding the negative of \( a_1\v_1 + \dots + a_{j-1}\v_{j-1} \) to both sides gives \( a_j\v_j = -(a_1\v_1 + \dots + a_{j-1}\v_{j-1}) \). Since \( a_j \neq 0 \) and \( F \) is a field, \( a_j \) has an inverse \( a_j^{-1} \in F \) (@def-field). Multiplying both sides by \( a_j^{-1} \), and using \( a_j^{-1}(a_j\v_j) = (a_j^{-1}a_j)\v_j = 1\v_j = \v_j \) on the left, and \( -\x = (-1)\x \) (@thm-negation-scalar) with the distributive laws on the right, we get
\[
\v_j = (-a_j^{-1}a_1)\v_1 + \dots + (-a_j^{-1}a_{j-1})\v_{j-1} .
\]
Hence \( \v_j \in \Span(\v_1, \dots, \v_{j-1}) \). When \( j = 1 \) the right side is the empty sum, so \( \v_1 = \0 \); therefore if \( \v_1 \neq \0 \), then \( j \ge 2 \).

(2) Let \( j \) be any index with \( \v_j \in \Span(\v_1, \dots, \v_{j-1}) \), and let \( L = (\v_1, \dots, \v_{j-1}, \v_{j+1}, \dots, \v_k) \). Each of \( \v_1, \dots, \v_{j-1} \) is an entry of \( L \), so by monotonicity (@prp-span-basic-properties (2)) \( \Span(\v_1, \dots, \v_{j-1}) \subseteq \Span(L) \), and hence \( \v_j \in \Span(L) \). By @thm-span-absorb, inserting \( \v_j \) back into \( L \) at position \( j \) does not change the span. That is, \( \Span(\v_1, \dots, \v_k) = \Span(L) \), as claimed.
:::

The index \( j \) need not be unique, and the lemma does **not** say that every vector depends on earlier ones. A small example shows both.

::: {#exm-dependence-lemma}
[The Lemma on a Concrete List]

In \( \nR^2 \), let \( \v_1 = (1, 1) \), \( \v_2 = (1, -1) \), \( \v_3 = (2, 0) \), \( \v_4 = (0, 1) \). Find two different linear relations, and the index \( j \) that the proof of @thm-linear-dependence-lemma extracts from each. Which indices \( j \) satisfy \( \v_j \in \Span(\v_1, \dots, \v_{j-1}) \)?
:::

::: {.solution}
First relation: \( \v_1 + \v_2 - \v_3 = (1 + 1 - 2, 1 - 1 - 0) = (0, 0) \). The largest index with a non-zero coefficient is \( j = 3 \), and solving gives \( \v_3 = \v_1 + \v_2 \in \Span(\v_1, \v_2) \).

Second relation: \( \v_1 - \v_2 - 2\v_4 = (1 - 1 - 0, 1 + 1 - 2) = (0, 0) \). Here the largest index is \( j = 4 \), and \( \v_4 = \tfrac12 \v_1 - \tfrac12 \v_2 \in \Span(\v_1, \v_2, \v_3) \).

So \( j = 3 \) and \( j = 4 \) both qualify, and by part (2) of the lemma either \( \v_3 \) or \( \v_4 \) can be removed without changing the span. On the other hand, \( j = 2 \) does not qualify: \( \v_2 = (1, -1) \) is not a multiple of \( \v_1 = (1, 1) \), because a multiple \( (c, c) \) has equal entries. And \( j = 1 \) does not occur since \( \v_1 \neq \0 \). Removing \( \v_3 \) and then (by the lemma applied to \( (\v_1, \v_2, \v_4) \), which is still dependent by the second relation) \( \v_4 \) leaves \( (\v_1, \v_2) \), whose span is \( \nR^2 \) by @exm-spanning-set.

The lemma only locates vectors that depend on **earlier** ones. Here \( \v_1 \) and \( \v_2 \) could also be removed without changing the span, since \( \v_1 = \v_3 - \v_2 \) and \( \v_2 = \v_3 - \v_1 \), but the lemma never points at them.
:::

Read the other way round, part (1) is a test for independence that works left to right.

::: {.remark}
**Independence, one vector at a time.** A list \( (\v_1, \dots, \v_k) \) is linearly independent **if and only if** no \( \v_j \) lies in \( \Span(\v_1, \dots, \v_{j-1}) \). The "if" direction is the contrapositive of part (1). For "only if", suppose \( \v_j = c_1\v_1 + \dots + c_{j-1}\v_{j-1} \). Then \( c_1\v_1 + \dots + c_{j-1}\v_{j-1} + (-1)\v_j = \0 \), with zero coefficients on \( \v_{j+1}, \dots, \v_k \), is a relation whose coefficient \( -1 \) is non-zero. So the list is dependent. In words: a list is independent exactly when each vector reaches something new beyond the vectors before it. For instance \( (1, x, x^2) \) passes: \( 1 \neq 0 \), \( x \) is not a constant, and \( x^2 \) has degree too high to be in \( \Span(1, x) \).
:::

Combining the two parts of the lemma gives a clean statement about spans alone: a list is dependent exactly when it contains a vector that can be thrown away for free.

::: {#thm-span-preservation}
[Span Preservation]

Let \( V \) be a vector space and \( (\v_1, \dots, \v_k) \) a list in \( V \) with \( k \ge 1 \). Then the list is linearly dependent **if and only if** there is an index \( j \) such that
\[
\Span(\v_1, \dots, \v_{j-1}, \v_{j+1}, \dots, \v_k) = \Span(\v_1, \dots, \v_k).
\]
:::

::: {.proof}
\( (\Rightarrow) \) By @thm-linear-dependence-lemma (1) there is an index \( j \) with \( \v_j \in \Span(\v_1, \dots, \v_{j-1}) \), and by part (2) removing that \( \v_j \) does not change the span.

\( (\Leftarrow) \) Let \( L \) be the list with \( \v_j \) removed, and suppose \( \Span(L) = \Span(\v_1, \dots, \v_k) \). By @thm-span-subspace (2), \( \v_j \in \Span(\v_1, \dots, \v_k) = \Span(L) \). So \( \v_j = \sum_{i \neq j} c_i\v_i \) for some scalars \( c_i \), and therefore \( \sum_{i \neq j} c_i\v_i + (-1)\v_j = \0 \). The coefficient of \( \v_j \) is \( -1 \neq 0 \), so the list is dependent.
:::

So a spanning list that is dependent can always be shortened and still span. Repeating this until the list becomes independent is the idea behind the next section's proof that every finite spanning list contains a basis.

## Unique representations

Independence was introduced to rule out waste. Its most useful consequence is about uniqueness. If a vector could be built from a list in two different ways, subtracting the two recipes would give a non-trivial way to build \( \0 \). So for an independent list, every vector in the span has exactly one recipe.

::: {#thm-independence-unique-combination}
[Independence and Uniqueness of Coefficients]

Let \( V \) be a vector space over \( F \) and \( (\v_1, \dots, \v_k) \) a list in \( V \). The following are equivalent:

::: {.enumerate options="label=(\alph*)"}
1. \( (\v_1, \dots, \v_k) \) is linearly independent;
2. every \( \v \in \Span(\v_1, \dots, \v_k) \) has **exactly one** representation as a linear combination: if \( a_1\v_1 + \dots + a_k\v_k = b_1\v_1 + \dots + b_k\v_k \), then \( a_i = b_i \) for every \( i \).
:::
:::

::: {.proof}
(a \( \Rightarrow \) b) Suppose the list is independent, and let \( a_1\v_1 + \dots + a_k\v_k = b_1\v_1 + \dots + b_k\v_k \). Subtracting the right side from both sides and using \( a\v - b\v = (a - b)\v \) (@thm-negative-scalar-dist and @def-vector-space) gives
\[
(a_1 - b_1)\v_1 + \dots + (a_k - b_k)\v_k = \0 .
\]
By independence, \( a_i - b_i = 0 \) for every \( i \), that is, \( a_i = b_i \).

(b \( \Rightarrow \) a) Suppose (b) holds, and let \( a_1\v_1 + \dots + a_k\v_k = \0 \). By @thm-zero-scalar-mult, also \( 0\v_1 + \dots + 0\v_k = \0 \). These are two representations of \( \0 \in \Span(\v_1, \dots, \v_k) \), so by (b), \( a_i = 0 \) for every \( i \). Hence the list is independent.
:::

Every vector of a span has **at least** one representation, by definition of the span; independence is what makes it **at most** one. For a dependent list uniqueness fails: with the list \( ((1, 0), (0, 1), (1, 1)) \),
\[
(1, 1) = 1(1, 0) + 1(0, 1) + 0(1, 1) = 0(1, 0) + 0(0, 1) + 1(1, 1).
\]
In the next section, a list that is independent **and** spans is called a basis. By this theorem every vector then has a unique list of coefficients, its coordinates.

## Polynomials of distinct degrees

For polynomials there is a test that needs no equations at all. The list \( (x^2 + x, x - 3, 5) \) is independent, and the reason is visible: the degrees are \( 2 \), \( 1 \) and \( 0 \), and combining lower-degree polynomials can never produce a higher degree.

::: {#thm-distinct-degrees-independent}
[Polynomials of Distinct Degrees Are Independent]

Let \( F \) be a field and let \( p_1, \dots, p_k \in F[x] \) be **non-zero** polynomials whose degrees are **pairwise distinct**. Then the list \( (p_1, \dots, p_k) \) is linearly independent.
:::

::: {.idea}
Put the polynomials in order of increasing degree. If the list were dependent, the Linear Dependence Lemma would give a polynomial lying in the span of the ones before it. Those all have smaller degree, so their span consists of polynomials of smaller degree, and cannot contain it.
:::

::: {.proof}
A linear relation among the \( p_i \) can be rearranged term by term, so reordering the list does not affect independence. Hence we may assume \( \deg p_1 < \deg p_2 < \dots < \deg p_k \).

Suppose, for a contradiction, that the list is dependent. Since \( p_1 \neq 0 \), @thm-linear-dependence-lemma gives an index \( j \ge 2 \) with \( p_j \in \Span(p_1, \dots, p_{j-1}) \). Let \( n = \deg p_{j-1} \), a natural number since \( p_{j-1} \neq 0 \). For every \( i \le j - 1 \) we have \( \deg p_i \le n \), so \( p_1, \dots, p_{j-1} \) lie in \( F[x]_{\le n} \), which is a subspace of \( F[x] \) by @exm-poly-degree-bound. By @thm-span-subspace (3), \( \Span(p_1, \dots, p_{j-1}) \subseteq F[x]_{\le n} \). Hence \( \deg p_j \le n = \deg p_{j-1} \), contradicting \( \deg p_{j-1} < \deg p_j \). Therefore the list is linearly independent.
:::

Both hypotheses matter. The zero polynomial must be excluded, because a list containing \( 0 \) is dependent (@exm-independence-degenerate). And the converse fails: distinct degrees are sufficient, not necessary. The list \( (x, x + 1) \) has equal degrees but is independent, since \( ax + b(x + 1) = (a + b)x + b = 0 \) forces \( b = 0 \) and then \( a = 0 \).

## Independence depends on the field

The same set can be a vector space over two fields, and the answer to "independent?" can change with the field, because the field decides which coefficients are allowed.

::: {.warning}
**Always ask: independent over which field?** In \( \nC^2 \), let \( \v_1 = (1, i) \) and \( \v_2 = (i, -1) \). Over \( \nC \) the list \( (\v_1, \v_2) \) is **dependent**: \( i\v_1 = (i, i^2) = (i, -1) = \v_2 \), so \( i\v_1 + (-1)\v_2 = \0 \) with coefficient \( i \neq 0 \). Over \( \nR \) (the same addition, but only real scalars, as in @exr-span-c2) the list is **independent**: if \( a\v_1 + b\v_2 = (a + bi, ai - b) = (0, 0) \) with \( a, b \in \nR \), then the first entry \( a + bi = 0 \) forces \( a = b = 0 \), since a complex number is zero only when its real and imaginary parts are. The relation over \( \nC \) used the coefficient \( i \), which is not available over \( \nR \).
:::

A second example of the same phenomenon: \( ((1, 1), (1, -1)) \) is independent in \( \nR^2 \) (@exm-linear-independence (c)), but in \( \nF_2^2 \), where \( -1 = 1 \), it is the list \( ((1, 1), (1, 1)) \) with a repeat, hence dependent. The proof over \( \nR \) divided by \( 2 \), which is \( 0 \) in \( \nF_2 \).

## Exercises

### A. Check your understanding

::: {#exr-independence-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define what it means for a list \( (\v_1, \dots, \v_k) \) in a vector space over \( F \) to be linearly independent, and what it means for it to be linearly dependent.
2. Determine whether the following statement is true: "a list of vectors is linearly dependent if and only if one of its vectors is a scalar multiple of another." Justify your answer.
3. Is the empty list linearly independent? Is the list \( (\0) \)?
4. Determine whether the following statement is true: "if \( (\v_1, \v_2, \v_3) \) is linearly dependent, then \( \v_3 \in \Span(\v_1, \v_2) \)." Justify your answer.
5. To prove that a list of functions \( \nR \to \nR \) is independent, what does "\( = 0 \)" mean, and what is a standard way to extract scalar equations?
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. It is independent if for all \( a_1, \dots, a_k \in F \), \( a_1\v_1 + \dots + a_k\v_k = \0 \) implies \( a_1 = \dots = a_k = 0 \). It is dependent if there are \( a_1, \dots, a_k \in F \), not all zero, with \( a_1\v_1 + \dots + a_k\v_k = \0 \).
2. False. The list \( ((1, 0, 1), (0, 1, 1), (1, 1, 2)) \) in \( \nR^3 \) is dependent, since the third vector is the sum of the first two, but no vector is a multiple of another. (The "if" direction is true: \( \v_i = c\v_j \) with \( i \neq j \) gives the relation \( \v_i - c\v_j = \0 \) with coefficient \( 1 \neq 0 \).)
3. The empty list is independent: there are no coefficients, so the condition holds vacuously. The list \( (\0) \) is dependent: \( 1 \cdot \0 = \0 \) with coefficient \( 1 \neq 0 \) (@exm-independence-degenerate).
4. False. Take \( \v_1 = (1, 0) \), \( \v_2 = (2, 0) \), \( \v_3 = (0, 1) \) in \( \nR^2 \). The list is dependent, since \( 2\v_1 - \v_2 = \0 \). But every combination of \( \v_1, \v_2 \) has second entry \( 0 \), so \( \v_3 \notin \Span(\v_1, \v_2) \). @thm-linear-dependence-lemma only promises **some** \( j \); here \( j = 2 \).
5. It means the zero function: the combination takes the value \( 0 \) at **every** point. Evaluating at well-chosen points turns it into scalar equations for the coefficients.
:::
:::

### B. Practice

::: {#exr-independence-b1}
[B1: Independent or Not?]

Determine which of the following lists are linearly independent. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( ((1, 0, 2), (0, 1, 1), (1, 1, 3)) \) in \( \nR^3 \).
2. \( ((1, 1, 0), (0, 1, 1), (1, 0, 1)) \) in \( \nR^3 \).
3. \( (x^2 + 1, x^2 - 1, x) \) in \( \nR[x] \).
4. \( \left( \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \right) \) in \( M_2(\nR) \).
5. \( (f, g) \) in \( \nR^\nR \), where \( f(t) = e^t \) and \( g(t) = e^{2t} \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Dependent. Since \( (1, 0, 2) + (0, 1, 1) = (1, 1, 3) \), we have \( (1, 0, 2) + (0, 1, 1) - (1, 1, 3) = \0 \), with coefficients not all zero.
2. Independent. Let \( a(1, 1, 0) + b(0, 1, 1) + c(1, 0, 1) = \0 \). Comparing entries: \( a + c = 0 \), \( a + b = 0 \), \( b + c = 0 \). The first two give \( c = -a \) and \( b = -a \); then the third gives \( -2a = 0 \), so \( a = 0 \), and hence \( b = c = 0 \).
3. Independent. Let \( a(x^2 + 1) + b(x^2 - 1) + cx = 0 \). The left side is \( (a + b)x^2 + cx + (a - b) \). Comparing coefficients (@def-polynomial): \( a + b = 0 \), \( c = 0 \), \( a - b = 0 \). Adding the first and third gives \( 2a = 0 \), so \( a = 0 \), and then \( b = 0 \).
4. Dependent. The first two matrices add up to the third, so \( 1 \cdot \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} + 1 \cdot \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} + (-1) \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \) is the zero matrix.
5. Independent. Let \( af + bg = 0 \), the zero function. Then \( ae^t + be^{2t} = 0 \) for every \( t \in \nR \). At \( t = 0 \): \( a + b = 0 \). At \( t = \ln 2 \): \( 2a + 4b = 0 \), so \( a + 2b = 0 \). Subtracting the first equation gives \( b = 0 \), and then \( a = 0 \).
:::
:::

::: {#exr-independence-b2}
[B2: A Parameter]

For which \( t \in \nR \) is the list \( ((1, t), (t, 1)) \) in \( \nR^2 \) linearly independent? Justify your answer.
:::

::: {.solution}
Let \( a(1, t) + b(t, 1) = (0, 0) \), that is, \( a + tb = 0 \) and \( ta + b = 0 \). The first equation gives \( a = -tb \). Substituting into the second, \( -t^2b + b = (1 - t^2)b = 0 \).

If \( t \neq \pm 1 \), then \( 1 - t^2 \neq 0 \), so \( b = 0 \) by @thm-field-basic-properties, and then \( a = -tb = 0 \). The list is independent.

If \( t = 1 \), the list is \( ((1, 1), (1, 1)) \), which has a repeat and is dependent. If \( t = -1 \), the list is \( ((1, -1), (-1, 1)) \), and \( 1 \cdot (1, -1) + 1 \cdot (-1, 1) = (0, 0) \), so it is dependent.

Hence the list is linearly independent exactly when \( t \neq 1 \) and \( t \neq -1 \).
:::

::: {#exr-independence-b3}
[B3: Sub-Lists]

A **sub-list** of \( (\v_1, \dots, \v_k) \) is a list \( (\v_{i_1}, \dots, \v_{i_m}) \) with \( 1 \le i_1 < i_2 < \dots < i_m \le k \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that every sub-list of a linearly independent list is linearly independent.
2. Deduce that if some sub-list of a list is linearly dependent, then the whole list is linearly dependent.
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Let \( (\v_1, \dots, \v_k) \) be independent, and let \( b_1\v_{i_1} + \dots + b_m\v_{i_m} = \0 \). Define \( a_i = b_r \) if \( i = i_r \) for some \( r \) (the indices \( i_r \) are distinct, so this is well defined), and \( a_i = 0 \) otherwise. By @thm-zero-scalar-mult the extra terms are \( \0 \), so \( a_1\v_1 + \dots + a_k\v_k = b_1\v_{i_1} + \dots + b_m\v_{i_m} = \0 \). By independence, every \( a_i = 0 \); in particular every \( b_r = a_{i_r} = 0 \). Hence the sub-list is independent.
2. This is the contrapositive of (a): if the whole list were independent, every sub-list would be independent by (a).
:::
:::

### C. Going deeper

::: {#exr-independence-c1}
[C1: Sums of Pairs, and the Field \( \nF_2 \)]

Let \( V \) be a vector space over \( F \) and \( (\u, \v, \w) \) a linearly independent list in \( V \).

::: {.enumerate options="label=(\alph*)"}
1. Suppose \( F = \nR \). Prove that \( (\u + \v, \v + \w, \w + \u) \) is linearly independent.
2. Suppose \( F = \nF_2 \). Prove that \( (\u + \v, \v + \w, \w + \u) \) is linearly dependent, and give an example of an independent list \( (\u, \v, \w) \) over \( \nF_2 \), so that the statement is not vacuous.
3. Which property of \( \nR \) did (a) use that \( \nF_2 \) lacks? Deduce that (a) holds over every field in which \( 1 + 1 \neq 0 \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Let \( a(\u + \v) + b(\v + \w) + c(\w + \u) = \0 \). Expanding and regrouping with the axioms of @def-vector-space gives \( (a + c)\u + (a + b)\v + (b + c)\w = \0 \). By independence of \( (\u, \v, \w) \), \( a + c = 0 \), \( a + b = 0 \) and \( b + c = 0 \). The first two give \( c = -a \) and \( b = -a \), and then the third gives \( -2a = 0 \). Since \( 2 \neq 0 \) in \( \nR \), \( a = 0 \), and hence \( b = c = 0 \). This proves independence.
2. Over \( \nF_2 \),
\[
1(\u + \v) + 1(\v + \w) + 1(\w + \u) = (1 + 1)\u + (1 + 1)\v + (1 + 1)\w = 0\u + 0\v + 0\w = \0 ,
\]
using \( 1 + 1 = 0 \) in \( \nF_2 \) and @thm-zero-scalar-mult. The coefficients are \( 1 \neq 0 \), so the list is dependent. For an example, \( (\e_1, \e_2, \e_3) \) in \( \nF_2^3 \) is independent by the argument of @exm-linear-independence (a), which works over any field.
3. Part (a) divided by \( 2 = 1 + 1 \), that is, used \( 2 \neq 0 \), to pass from \( -2a = 0 \) to \( a = 0 \). In \( \nF_2 \), \( 2 = 0 \). In any field with \( 1 + 1 \neq 0 \), the element \( 2 \) has an inverse, and the proof of (a) goes through word for word.
:::
:::

::: {#exr-independence-c2}
[C2: Adding a Vector outside the Span]

Let \( (\v_1, \dots, \v_k) \) be a linearly independent list in \( V \), and let \( \v \in V \) with \( \v \notin \Span(\v_1, \dots, \v_k) \). Prove that \( (\v_1, \dots, \v_k, \v) \) is linearly independent. Give an example showing that the hypothesis \( \v \notin \Span(\v_1, \dots, \v_k) \) cannot be dropped.
:::

::: {.solution}
Let \( a_1\v_1 + \dots + a_k\v_k + a\v = \0 \). Suppose \( a \neq 0 \). Then, as in the proof of @thm-linear-dependence-lemma, \( \v = (-a^{-1}a_1)\v_1 + \dots + (-a^{-1}a_k)\v_k \in \Span(\v_1, \dots, \v_k) \), contradicting the hypothesis. Hence \( a = 0 \), and the relation becomes \( a_1\v_1 + \dots + a_k\v_k = \0 \). By independence of \( (\v_1, \dots, \v_k) \), \( a_1 = \dots = a_k = 0 \). So all coefficients are zero, and the longer list is independent.

For the example, take \( (\e_1) \) in \( \nR^2 \) and \( \v = 2\e_1 \in \Span(\e_1) \). The list \( (\e_1) \) is independent, but \( (\e_1, 2\e_1) \) is dependent, by \( 2\e_1 - 2\e_1 = \0 \).
:::

::: {#exr-independence-c3}
[C3: \( 1, \sqrt 2, \sqrt 3 \) over \( \nQ \)]

Regard \( \nR \) as a vector space over \( \nQ \). Prove that the list \( (1, \sqrt 2, \sqrt 3) \) is linearly independent over \( \nQ \). Is it linearly independent over \( \nR \)?

*Hint: you may use without proof that \( \sqrt 3 \) and \( \sqrt 6 \) are irrational (the proof of @thm-sqrt2-irrational adapts). Isolate one square root and square.*
:::

::: {.solution}
Let \( a + b\sqrt 2 + c\sqrt 3 = 0 \) with \( a, b, c \in \nQ \). Then \( a + b\sqrt 2 = -c\sqrt 3 \), and squaring both sides gives \( a^2 + 2b^2 + 2ab\sqrt 2 = 3c^2 \).

If \( ab \neq 0 \), then \( \sqrt 2 = \dfrac{3c^2 - a^2 - 2b^2}{2ab} \in \nQ \), contradicting @thm-sqrt2-irrational. Hence \( ab = 0 \), so \( a = 0 \) or \( b = 0 \).

*Case 1: \( b = 0 \).* Then \( a + c\sqrt 3 = 0 \). If \( c \neq 0 \), then \( \sqrt 3 = -a/c \in \nQ \), a contradiction. So \( c = 0 \), and then \( a = 0 \).

*Case 2: \( a = 0 \).* Then \( b\sqrt 2 + c\sqrt 3 = 0 \). Multiplying by \( \sqrt 2 \) gives \( 2b + c\sqrt 6 = 0 \). If \( c \neq 0 \), then \( \sqrt 6 = -2b/c \in \nQ \), a contradiction. So \( c = 0 \), then \( b\sqrt 2 = 0 \), and \( b = 0 \) since \( \sqrt 2 \neq 0 \).

In both cases \( a = b = c = 0 \), so the list is linearly independent over \( \nQ \).

Over \( \nR \) it is dependent: \( \sqrt 2 \cdot 1 + (-1) \cdot \sqrt 2 + 0 \cdot \sqrt 3 = 0 \), and the coefficient \( \sqrt 2 \) is a non-zero real number. Over \( \nR \) any two non-zero real numbers form a dependent list.
:::
