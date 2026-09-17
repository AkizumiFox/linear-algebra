# Sets

Every object in linear algebra is a set with some extra structure. A vector space is a set on which we can add and scale, a subspace is a subset of it, and a linear map sends elements of one set to elements of another. Before the structure arrives, we need the plain language of sets: how to describe them, when two of them are equal, and how to combine them. The most important move in this section is proving that two sets are equal by proving two inclusions, a move we will use for subspaces, spans, kernels and images throughout the book.

## Sets, elements and set-builder notation

A **set** is a collection of objects, called its **elements**. We write \( x \in A \) for "\( x \) is an element of \( A \)" (also "\( x \) belongs to \( A \)", "\( x \) lies in \( A \)"), and \( x \notin A \) for its negation. A set is determined by its elements and nothing else: it has no order and no repetition. So \( \{1, 2\} \), \( \{2, 1\} \) and \( \{1, 1, 2\} \) all describe the same set, whose elements are \( 1 \) and \( 2 \). We make this precise below.

Small sets can be listed between braces. Infinite sets we meet constantly have fixed names.

::: {#def-common-number-sets}
[Common number sets]

We write

- \( \nN = \{0, 1, 2, 3, \dots\} \) for the **natural numbers**; in this book \( \nN \) **includes** \( 0 \);
- \( \nZ = \{\dots, -2, -1, 0, 1, 2, \dots\} \) for the **integers**;
- \( \nQ \) for the **rational numbers**, the numbers \( a/b \) with \( a, b \in \nZ \) and \( b \ne 0 \);
- \( \nR \) for the **real numbers**;
- \( \nC \) for the **complex numbers**, studied later in this chapter.
:::

Books disagree about whether \( 0 \in \nN \). With our convention, the Well-Ordering Principle (@thm-well-ordering) applies to collections that contain \( 0 \), and "\( n \in \nN \)" means \( n \ge 0 \). When we need positive integers only, we say "\( n \ge 1 \)". For real numbers \( a \le b \) we also use **intervals**: \( [a, b] \) is the set of real \( x \) with \( a \le x \le b \), \( (a, b) \) the set with \( a < x < b \), and \( [a, b) \), \( (a, b] \) are defined in the same way.

Listing elements fails for most sets we care about, such as "the real numbers whose square is less than \( 4 \)". Instead we describe a set by a property, and select from a set we already have.

::: {#def-set-builder}
[Set-builder notation]

Let \( S \) be a set and let \( P(x) \) be a predicate for \( x \in S \). The set
\[
\{ x \in S : P(x) \}
\]
is the set whose elements are **exactly** those \( x \in S \) for which \( P(x) \) is true.
:::

In words: an object \( y \) belongs to \( \{ x \in S : P(x) \} \) if and only if \( y \in S \) **and** \( P(y) \) is true. Both parts matter. The ambient set \( S \) says where we are looking, and the predicate says what we keep. The colon is read "such that"; some books use a vertical bar instead. When it is plain which sets the elements come from, as in the unions and intersections below, we sometimes leave the ambient set out and write \( \{ x : P(x) \} \).

A second form describes the elements by a formula: \( \{ 2k : k \in \nZ \} \) is the set of all numbers of the form \( 2k \) with \( k \) an integer. An object \( y \) belongs to it exactly when \( y = 2k \) for **some** \( k \in \nZ \). This form will describe sets such as "all combinations of given vectors" in Chapter 1.

::: {#exm-set-builder}
[Reading set-builder notation]

Describe each set more simply.

::: {.enumerate options="label=(\alph*)"}
1. \( \{ x \in \nR : x^2 < 4 \} \).
2. \( \{ x \in \nZ : x^2 < 4 \} \).
3. \( \{ n \in \nZ : n \text{ is even} \} \) and \( \{ 2k : k \in \nZ \} \).
4. \( \{ (x, y) : x, y \in \nR,\ x + y = 1 \} \), a set of ordered pairs (made precise under Cartesian products below).
:::
:::

::: {.solution}
(a) A real number satisfies \( x^2 < 4 \) exactly when \( -2 < x < 2 \), so the set is the interval \( (-2, 2) \).

(b) The same predicate, selected from \( \nZ \) instead, keeps only integers: the set is \( \{-1, 0, 1\} \). Changing the ambient set changes the set.

(c) Both are the set \( \{ \dots, -4, -2, 0, 2, 4, \dots \} \) of even integers. The first selects the integers with a property; the second produces each element by the formula \( 2k \). By the definition of "even" (@def-parity), an integer is even exactly when it equals \( 2k \) for some \( k \in \nZ \).

(d) The pairs of reals whose coordinates add to \( 1 \): the line in the plane through \( (1, 0) \) and \( (0, 1) \).
:::

What if no element of \( S \) satisfies the predicate? We still want a set, and it has no elements.

::: {#def-empty-set}
[Empty set]

The **empty set** \( \varnothing \) is the set with **no** elements: \( x \notin \varnothing \) for every object \( x \).
:::

For example, \( \{ x \in \nR : x^2 = -1 \} = \varnothing \), since \( x^2 \ge 0 \) for every real \( x \) (@exm-quantifiers). Also \( \{ n \in \nZ : 0 < n < 1 \} = \varnothing \). We will see shortly that there is only **one** empty set, so these two descriptions give the same set.

Statements about all elements of \( \varnothing \) are vacuously true: "every element of \( \varnothing \) is a prime number" has no element that could fail, just as in the degenerate case discussed after @exm-quantifiers.

::: {.warning}
**\( \varnothing \), \( \{\varnothing\} \) and \( \{0\} \) are three different sets.** The set \( \varnothing \) has no elements. The set \( \{\varnothing\} \) has exactly one element, namely the empty set. The set \( \{0\} \) has exactly one element, namely the number \( 0 \). A box containing an empty box is not an empty box. In Chapter 1 this matters: \( \{0\} \) will be a subspace, and \( \varnothing \) never is.
:::

## Subsets

Most sets in this book live inside a bigger set: the even integers inside \( \nZ \), a line inside the plane, and later a subspace inside a vector space. The first thing to check about a candidate subspace will be that it sits inside the space at all. We need a word for "sits inside".

*\( A \) is a subset of \( B \) when everything in \( A \) is also in \( B \).*

::: {#def-subset}
[Subset]

Let \( A \) and \( B \) be sets. We say \( A \) is a **subset** of \( B \), and write \( A \subseteq B \), if
\[
\forall x : \bigl( x \in A \Rightarrow x \in B \bigr).
\]
If \( A \subseteq B \) and \( A \ne B \), then \( A \) is a **proper** subset of \( B \), written \( A \subsetneq B \).
:::

In words: \( A \subseteq B \) says that **every** element of \( A \) is an element of \( B \). It says nothing about elements of \( B \); \( B \) may contain many more. The definition is an implication inside a "for every", so the proof template of the previous section applies: to show \( A \subseteq B \), **let** \( x \in A \) and show \( x \in B \).

By @def-negation-of-quantifiers and @thm-de-morgan-logic, the negation reads
\[
A \not\subseteq B \iff \exists x : x \in A \text{ and } x \notin B.
\]
So to show \( A \) is **not** a subset of \( B \), exhibit one element of \( A \) outside \( B \).

::: {#exm-subsets}
[Subsets]

Decide whether each inclusion holds.

::: {.enumerate options="label=(\alph*)"}
1. \( \nN \subseteq \nZ \subseteq \nQ \subseteq \nR \).
2. \( \{1, 2\} \subseteq \{1, 2, 3\} \) and \( \{1, 4\} \subseteq \{1, 2, 3\} \).
3. \( A \subseteq A \) and \( \varnothing \subseteq A \), for any set \( A \).
4. \( \{ x \in \nR : x^2 = 1 \} \subseteq \nZ \).
:::
:::

::: {.solution}
(a) All hold. Every natural number is an integer; every integer \( n \) equals \( n/1 \), so it is rational; every rational number is real.

(b) The first holds: each of \( 1, 2 \) is an element of \( \{1, 2, 3\} \). The second fails, although it differs from the first in only one element: \( 1 \) passes, but \( 4 \in \{1, 4\} \) and \( 4 \notin \{1, 2, 3\} \), so \( 4 \) is a witness for \( \{1, 4\} \not\subseteq \{1, 2, 3\} \).

(c) Both hold. For \( A \subseteq A \): let \( x \in A \); then \( x \in A \). For \( \varnothing \subseteq A \): the implication \( x \in \varnothing \Rightarrow x \in A \) has a false hypothesis for every \( x \) by @def-empty-set, so it is vacuously true (@def-implication-converse-contrapositive). The empty set is a subset of every set, including itself.

(d) Holds. Let \( x \in \nR \) with \( x^2 = 1 \). Then \( (x - 1)(x + 1) = 0 \), so \( x = 1 \) or \( x = -1 \), and both are integers.
:::

::: {.warning}
**\( \in \) and \( \subseteq \) are different relations.** \( x \in A \) says the object \( x \) is one of the elements of \( A \). \( A \subseteq B \) compares two sets, element by element. So \( 1 \in \{1, 2\} \) is true while \( 1 \subseteq \{1, 2\} \) makes no sense (\( 1 \) is not a set here); and \( \{1\} \subseteq \{1, 2\} \) is true while \( \{1\} \in \{1, 2\} \) is false.
:::

:::: {.check}
Let \( X = \{ \{1, 2\}, 3 \} \). Is \( \{1, 2\} \subseteq X \)? Is \( \{1, 2\} \in X \)?

::: {.solution}
The set \( X \) has exactly two elements: the set \( \{1, 2\} \) and the number \( 3 \). So \( \{1, 2\} \in X \) is **true**. But \( \{1, 2\} \subseteq X \) is **false**: \( 1 \in \{1, 2\} \), and \( 1 \) is neither the set \( \{1, 2\} \) nor the number \( 3 \), so \( 1 \notin X \).
:::
::::

## Equality of sets and double inclusion

We said a set is determined by its elements. Here is the precise version.

::: {#def-set-equality}
[Set equality]

Two sets \( A \) and \( B \) are **equal**, written \( A = B \), if they have exactly the same elements:
\[
\forall x : \bigl( x \in A \Leftrightarrow x \in B \bigr).
\]
:::

So \( \{1, 2\} = \{2, 1\} = \{1, 1, 2\} \): each object belongs to one of these sets exactly when it is \( 1 \) or \( 2 \). Order and repetition in a list are features of how we **write** a set, not of the set.

Proving a biconditional for every \( x \) at once is awkward. It is much easier to prove two implications separately, and that is exactly what the next result allows.

::: {#thm-double-inclusion}
[Double inclusion]

Let \( A \) and \( B \) be sets. Then \( A = B \) if and only if \( A \subseteq B \) and \( B \subseteq A \).
:::

::: {.proof}
By @def-set-equality, \( A = B \) means that for every \( x \), both \( x \in A \Rightarrow x \in B \) and \( x \in B \Rightarrow x \in A \) hold, since a biconditional is the conjunction of an implication and its converse. A statement of the form "for every \( x \), \( P(x) \) and \( Q(x) \)" holds exactly when "for every \( x \), \( P(x) \)" and "for every \( x \), \( Q(x) \)" both hold, by @def-quantifiers. Hence \( A = B \) holds exactly when \( \forall x \, (x \in A \Rightarrow x \in B) \) and \( \forall x \, (x \in B \Rightarrow x \in A) \) both hold. By @def-subset, these are \( A \subseteq B \) and \( B \subseteq A \). This proves the theorem.
:::

This is the move **"prove set equality by double inclusion"**. The proof is written in two labeled halves, \( (\subseteq) \) and \( (\supseteq) \), each starting "Let \( x \in \dots \)". Here is a first consequence.

::: {.remark}
There is only one empty set. If \( E \) and \( E' \) are sets with no elements, then \( E \subseteq E' \) and \( E' \subseteq E \) hold vacuously, as in @exm-subsets (c), so \( E = E' \) by @thm-double-inclusion. This is why we may say **the** empty set.
:::

::: {#exm-quadratic-solution-set}
[A solution set by double inclusion]

Prove that \( \{ x \in \nR : x^2 - 3x + 2 = 0 \} = \{1, 2\} \).
:::

::: {.solution}
Write \( S = \{ x \in \nR : x^2 - 3x + 2 = 0 \} \). By @thm-double-inclusion it suffices to prove \( S \subseteq \{1, 2\} \) and \( \{1, 2\} \subseteq S \).

\( (\subseteq) \) Let \( x \in S \). Then \( x \) is real and \( x^2 - 3x + 2 = 0 \). Factoring, \( (x - 1)(x - 2) = 0 \). A product of two real numbers is zero only if one factor is zero, so \( x = 1 \) or \( x = 2 \). Hence \( x \in \{1, 2\} \).

\( (\supseteq) \) Let \( x \in \{1, 2\} \), so \( x = 1 \) or \( x = 2 \). Both are real. If \( x = 1 \), then \( 1 - 3 + 2 = 0 \); if \( x = 2 \), then \( 4 - 6 + 2 = 0 \). In either case \( x \in S \).

This shows \( S = \{1, 2\} \).
:::

Solving an equation "at school" usually produces only the \( (\subseteq) \) half: "if \( x \) is a solution, then \( x \) is \( 1 \) or \( 2 \)". The \( (\supseteq) \) half, checking that the candidates really are solutions, is the part that gets forgotten. It matters whenever a step in the solving is not reversible, such as squaring both sides.

## Union, intersection and difference

Given two sets, there are three basic ways to form a new one: keep what is in either, keep what is in both, or keep what is in the first but not the second. Each is a set-builder description whose predicate uses a connective from the section on logic.

::: {#def-union}
[Union]

The **union** of sets \( A \) and \( B \) is
\[
A \cup B = \{ x : x \in A \text{ or } x \in B \}.
\]
:::

::: {#def-intersection}
[Intersection]

The **intersection** of sets \( A \) and \( B \) is
\[
A \cap B = \{ x : x \in A \text{ and } x \in B \}.
\]
We call \( A \) and \( B \) **disjoint** if \( A \cap B = \varnothing \).
:::

::: {#def-set-difference}
[Set difference and complement]

The **difference** of sets \( A \) and \( B \) is
\[
A \setminus B = \{ x \in A : x \notin B \}.
\]
When all sets under discussion are subsets of one fixed set \( U \), the **complement** of \( B \subseteq U \) is \( B^{c} = U \setminus B \).
:::

In words: the union keeps an element that lies in **at least one** of the sets (the "or" is inclusive, as always); the intersection keeps an element that lies in **both**; the difference \( A \setminus B \) keeps the elements of \( A \) that are **not** in \( B \). The complement depends on the choice of \( U \): the complement of \( \nN \) is the set of negative integers inside \( \nZ \), but a much bigger set inside \( \nR \).

::: {#exm-set-operations}
[Operations on finite sets]

Let \( A = \{1, 2, 3, 4\} \) and \( B = \{3, 4, 5, 6\} \). Compute \( A \cup B \), \( A \cap B \), \( A \setminus B \) and \( B \setminus A \).
:::

::: {.solution}
Checking each element against the definitions: \( A \cup B = \{1, 2, 3, 4, 5, 6\} \); \( A \cap B = \{3, 4\} \); \( A \setminus B = \{1, 2\} \); and \( B \setminus A = \{5, 6\} \). Since \( A \setminus B \ne B \setminus A \), the difference is not symmetric in its two arguments, unlike union and intersection.
:::

::: {#exm-set-operations-intervals}
[Operations on intervals]

Let \( A = [0, 2] \) and \( B = [1, 3] \). Compute \( A \cup B \), \( A \cap B \) and \( A \setminus B \).
:::

::: {.solution}
A real \( x \) lies in \( A \cup B \) when \( 0 \le x \le 2 \) or \( 1 \le x \le 3 \), which happens exactly when \( 0 \le x \le 3 \); so \( A \cup B = [0, 3] \). It lies in \( A \cap B \) when both hold, that is, when \( 1 \le x \le 2 \); so \( A \cap B = [1, 2] \). It lies in \( A \setminus B \) when \( 0 \le x \le 2 \) and not \( 1 \le x \le 3 \). Given \( x \le 2 \), "not \( 1 \le x \le 3 \)" means \( x < 1 \); so \( A \setminus B = [0, 1) \). The endpoint \( 1 \) is excluded because \( 1 \in B \).
:::

Unions, intersections and differences interact through laws that mirror those for "or", "and" and "not". The first pair is De Morgan's laws, the set version of @thm-de-morgan-logic.

::: {#thm-de-morgan-sets}
[De Morgan's laws for sets]

Let \( A \), \( B \) and \( C \) be sets. Then

::: {.enumerate options="label=(\alph*)"}
1. \( A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C) \);
2. \( A \setminus (B \cap C) = (A \setminus B) \cup (A \setminus C) \).
:::

In particular, if \( B, C \subseteq U \), then \( (B \cup C)^{c} = B^{c} \cap C^{c} \) and \( (B \cap C)^{c} = B^{c} \cup C^{c} \).
:::

::: {.idea}
Unwind membership into connectives. "\( x \notin B \cup C \)" is "not (\( x \in B \) or \( x \in C \))", and De Morgan for statements turns that into "\( x \notin B \) and \( x \notin C \)". So each law is its logical counterpart, applied one element at a time. We prove (a) by double inclusion; (b) is an exercise.
:::

::: {.proof}
We prove (a) using @thm-double-inclusion.

\( (\subseteq) \) Let \( x \in A \setminus (B \cup C) \). By @def-set-difference, \( x \in A \) and \( x \notin B \cup C \). By @def-union, the second says that "\( x \in B \) or \( x \in C \)" is false, so by @thm-de-morgan-logic, \( x \notin B \) and \( x \notin C \). Since \( x \in A \) and \( x \notin B \), we have \( x \in A \setminus B \); since \( x \in A \) and \( x \notin C \), we have \( x \in A \setminus C \). Hence \( x \in (A \setminus B) \cap (A \setminus C) \) by @def-intersection.

\( (\supseteq) \) Let \( x \in (A \setminus B) \cap (A \setminus C) \). By @def-intersection and @def-set-difference, \( x \in A \), \( x \notin B \) and \( x \notin C \). By @thm-de-morgan-logic, "\( x \in B \) or \( x \in C \)" is false, so \( x \notin B \cup C \). Together with \( x \in A \), this gives \( x \in A \setminus (B \cup C) \).

This proves (a). For the complement form, take \( A = U \) and use @def-set-difference: \( (B \cup C)^{c} = U \setminus (B \cup C) = (U \setminus B) \cap (U \setminus C) = B^{c} \cap C^{c} \), and similarly for (b).
:::

The second pair of laws says each of \( \cap \) and \( \cup \) distributes over the other, like multiplication over addition, except that here **both** directions hold.

::: {#thm-distributive-sets}
[Distributive laws for sets]

Let \( A \), \( B \) and \( C \) be sets. Then

::: {.enumerate options="label=(\alph*)"}
1. \( A \cap (B \cup C) = (A \cap B) \cup (A \cap C) \);
2. \( A \cup (B \cap C) = (A \cup B) \cap (A \cup C) \).
:::
:::

::: {.idea}
Double inclusion again, and in each half the "or" in a union forces a split into cases. For (b) \( (\supseteq) \), an element of both \( A \cup B \) and \( A \cup C \) is either in \( A \), and then done, or not in \( A \), and then it must be in \( B \) and in \( C \). We prove (b); (a) is an exercise.
:::

::: {.proof}
We prove (b) using @thm-double-inclusion.

\( (\subseteq) \) Let \( x \in A \cup (B \cap C) \). By @def-union, \( x \in A \) or \( x \in B \cap C \).

*Case 1: \( x \in A \).* Then \( x \in A \cup B \) and \( x \in A \cup C \) by @def-union.

*Case 2: \( x \in B \cap C \).* Then \( x \in B \) and \( x \in C \) by @def-intersection, so again \( x \in A \cup B \) and \( x \in A \cup C \).

In both cases \( x \in (A \cup B) \cap (A \cup C) \) by @def-intersection.

\( (\supseteq) \) Let \( x \in (A \cup B) \cap (A \cup C) \), so \( x \in A \cup B \) and \( x \in A \cup C \).

*Case 1: \( x \in A \).* Then \( x \in A \cup (B \cap C) \).

*Case 2: \( x \notin A \).* Since \( x \in A \cup B \) and \( x \notin A \), we get \( x \in B \). Since \( x \in A \cup C \) and \( x \notin A \), we get \( x \in C \). Hence \( x \in B \cap C \), so \( x \in A \cup (B \cap C) \).

In both cases \( x \in A \cup (B \cap C) \). This proves (b).
:::

::: {.remark}
In Chapter 1 we will see that the intersection of two subspaces is always a subspace, while their union usually is not: the two axes in the plane are subspaces, but \( (1, 0) + (0, 1) = (1, 1) \) lies on neither. The union is replaced there by a different construction, the sum of subspaces.
:::

## Indexed families of sets

Two sets are not always enough. In Chapter 1 we will need "the intersection of **all** subspaces that contain a given set", and there are usually infinitely many of them. So we need unions and intersections of any number of sets at once.

*An indexed family is a list of sets with one set for each label; its union keeps what lies in some member, its intersection what lies in every member.*

::: {#def-indexed-family}
[Unions and intersections of indexed families]

Let \( I \) be a set, and for each \( i \in I \) let \( A_i \) be a set. The collection \( (A_i)_{i \in I} \) is an **indexed family** of sets, with **index set** \( I \). Its **union** is
\[
\bigcup_{i \in I} A_i = \{ x : \exists i \in I : x \in A_i \},
\]
and, if \( I \) is **non-empty**, its **intersection** is
\[
\bigcap_{i \in I} A_i = \{ x : \forall i \in I : x \in A_i \}.
\]
:::

In words: \( x \) lies in the union when it lies in **at least one** \( A_i \), and in the intersection when it lies in **every** \( A_i \). When \( I = \{1, 2\} \), these are \( A_1 \cup A_2 \) and \( A_1 \cap A_2 \). When \( I = \{1, 2, 3, \dots\} \), we also write \( \bigcup_{n=1}^{\infty} A_n \) and \( \bigcap_{n=1}^{\infty} A_n \).

**Why \( I \) must be non-empty for the intersection.** If \( I = \varnothing \), the condition "\( \forall i \in I : x \in A_i \)" is vacuously true for **every** object \( x \), so the "intersection" would contain everything, which is not a set we want. (When all sets live inside a fixed \( U \), one sometimes defines the empty intersection to be \( U \).) The empty union causes no such trouble: "\( \exists i \in \varnothing \)" is always false, so \( \bigcup_{i \in \varnothing} A_i = \varnothing \).

::: {#exm-indexed-families}
[Indexed unions and intersections of intervals]

For each integer \( n \ge 1 \), let \( A_n = [1/n, 1] \) and \( B_n = (0, 1/n) \). Show that
\[
\bigcup_{n=1}^{\infty} A_n = (0, 1] \qquad \text{and} \qquad \bigcap_{n=1}^{\infty} B_n = \varnothing.
\]
You may use the fact that for every real \( x > 0 \) there is an integer \( n \ge 1 \) with \( 1/n < x \).
:::

::: {.solution}
*The union.* \( (\subseteq) \) Let \( x \in \bigcup_{n} A_n \). By @def-indexed-family, \( x \in A_n \) for some \( n \ge 1 \), so \( 0 < 1/n \le x \le 1 \). Hence \( x \in (0, 1] \). \( (\supseteq) \) Let \( x \in (0, 1] \). Since \( x > 0 \), there is an integer \( n \ge 1 \) with \( 1/n < x \). Then \( 1/n \le x \le 1 \), so \( x \in A_n \), and hence \( x \) lies in the union. By @thm-double-inclusion, the union is \( (0, 1] \).

*The intersection.* Suppose, for a contradiction, that some \( x \) lies in \( \bigcap_n B_n \). Then \( x \in B_1 = (0, 1) \), so \( x > 0 \). Choose an integer \( n \ge 1 \) with \( 1/n < x \). Then \( x \notin (0, 1/n) = B_n \), contradicting \( x \in B_n \) for every \( n \). Hence the intersection has no elements, so it equals \( \varnothing \).

Each \( B_n \) is non-empty (it contains \( 1/(2n) \)), and each is contained in the one before. Yet their intersection is empty. Infinite intersections can shrink to nothing even when no single step does.
:::

De Morgan's laws hold for indexed families with the same proofs: for a non-empty index set \( I \), \( A \setminus \bigcup_{i} B_i = \bigcap_{i} (A \setminus B_i) \) and \( A \setminus \bigcap_{i} B_i = \bigcup_{i} (A \setminus B_i) \). The "or" of the finite version becomes "there exists", and the "and" becomes "for every", exactly as in @def-negation-of-quantifiers.

## Cartesian products and \( n \)-tuples

A set forgets order: \( \{1, 2\} = \{2, 1\} \). But a point in the plane is not like that. The point \( (1, 2) \) is different from \( (2, 1) \). We need objects that remember order.

An **ordered pair** \( (a, b) \) has a first entry \( a \) and a second entry \( b \), and two ordered pairs are equal exactly when their entries agree in order:
\[
(a, b) = (a', b') \iff a = a' \text{ and } b = b'.
\]

::: {#def-cartesian-product}
[Cartesian product]

Let \( A \) and \( B \) be sets. The **Cartesian product** of \( A \) and \( B \) is the set of ordered pairs
\[
A \times B = \{ (a, b) : a \in A,\ b \in B \}.
\]
More generally, for sets \( A_1, \dots, A_n \), the product \( A_1 \times \cdots \times A_n \) is the set of all ordered lists \( (a_1, \dots, a_n) \) with \( a_i \in A_i \) for each \( i \).
:::

For example, \( \{1, 2\} \times \{x, y\} = \{ (1, x), (1, y), (2, x), (2, y) \} \). The order of the factors matters: \( (1, x) \in \{1, 2\} \times \{x, y\} \), but \( (1, x) \notin \{x, y\} \times \{1, 2\} \), whose pairs have a letter first. A degenerate case: \( A \times \varnothing = \varnothing \) for every set \( A \), since no pair can have a second entry from \( \varnothing \).

::: {#def-n-tuple}
[\( n \)-tuples]

Let \( A \) be a set and \( n \ge 1 \) an integer. An **\( n \)-tuple** of elements of \( A \) is an ordered list \( (a_1, \dots, a_n) \) with each \( a_i \in A \). The set of all of them is
\[
A^n = \underbrace{A \times A \times \cdots \times A}_{n \text{ factors}}.
\]
Two \( n \)-tuples are equal exactly when \( a_i = b_i \) for **every** \( i = 1, \dots, n \).
:::

::: {#exm-n-tuples}
[Sets of tuples]

Describe some elements of \( \nR^2 \), \( \nZ^3 \) and \( \{0, 1\}^3 \), and count the elements of \( \{0, 1\}^3 \).
:::

::: {.solution}
The set \( \nR^2 \) is the plane: it contains \( (0, 0) \), \( (1, -2) \) and \( (\sqrt{2}, \pi) \). The set \( \nZ^3 \) contains \( (1, 0, -4) \) but not \( (1, \tfrac12, 0) \), whose second entry is not an integer. The set \( \{0, 1\}^3 \) consists of the lists of three bits:
\[
\{0, 1\}^3 = \{ (0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1) \}.
\]
There are two choices for each of the three entries, giving \( 2 \cdot 2 \cdot 2 = 8 \) elements. In the same way, if \( A \) has \( k \) elements then \( A^n \) has \( k^n \) elements.
:::

In Chapter 1, \( \nR^n \) and more generally \( F^n \) become the first examples of vector spaces, with \( n \)-tuples added and scaled entry by entry.

## Power sets

Sets can themselves be elements of sets, as the warning about \( \{\varnothing\} \) showed. One such set collects every subset of a given set.

::: {#def-power-set}
[Power set]

The **power set** of a set \( S \) is the set of all subsets of \( S \):
\[
\powerset{S} = \{ X : X \subseteq S \}.
\]
:::

So \( X \in \powerset{S} \) means exactly \( X \subseteq S \). For example,
\[
\powerset{\{1, 2\}} = \{ \varnothing, \{1\}, \{2\}, \{1, 2\} \},
\]
which has \( 4 \) elements. The degenerate case is instructive: \( \powerset{\varnothing} = \{\varnothing\} \) has **one** element, because the empty set has exactly one subset, itself. For a set with \( n \) elements the power set has \( 2^n \) elements; the last exercise proves this by induction.

## Exercises

### A. Check your understanding

::: {#exr-sets-a1}
[A1]

Decide whether each statement is true or false. Give a one-line reason.

::: {.enumerate options="label=(\alph*)"}
1. \( 0 \in \nN \).
2. \( \varnothing \in \varnothing \).
3. \( \varnothing \subseteq \varnothing \).
4. \( \{0\} = \varnothing \).
5. \( \{1, 2\} = \{2, 1, 1\} \) and \( (1, 2) = (2, 1) \).
6. \( \{1\} \in \powerset{\{1, 2\}} \) and \( \{1\} \subseteq \powerset{\{1, 2\}} \).
:::
:::

::: {.solution}
(a) True. By @def-common-number-sets, \( \nN \) includes \( 0 \) in this book.

(b) False. By @def-empty-set, nothing is an element of \( \varnothing \), not even \( \varnothing \).

(c) True. The empty set is a subset of every set, vacuously, as in @exm-subsets.

(d) False. \( 0 \in \{0\} \) but \( 0 \notin \varnothing \), so the two sets do not have the same elements (@def-set-equality).

(e) The first is true: both sets have exactly the elements \( 1 \) and \( 2 \). The second is false: ordered pairs are equal only when their first entries agree, and \( 1 \ne 2 \).

(f) The first is true: \( \{1\} \subseteq \{1, 2\} \), so \( \{1\} \in \powerset{\{1, 2\}} \) by @def-power-set. The second is false: \( 1 \in \{1\} \), but \( 1 \) is a number, not a subset of \( \{1, 2\} \), so \( 1 \notin \powerset{\{1, 2\}} \).
:::

### B. Practice

::: {#exr-sets-b1}
[B1: The second De Morgan law]

Let \( A \), \( B \), \( C \) be sets. Prove that \( A \setminus (B \cap C) = (A \setminus B) \cup (A \setminus C) \), which is part (b) of @thm-de-morgan-sets.
:::

::: {.solution}
We use @thm-double-inclusion.

\( (\subseteq) \) Let \( x \in A \setminus (B \cap C) \). By @def-set-difference, \( x \in A \) and \( x \notin B \cap C \). By @def-intersection, "\( x \in B \) and \( x \in C \)" is false, so by @thm-de-morgan-logic, \( x \notin B \) or \( x \notin C \). If \( x \notin B \), then \( x \in A \setminus B \); if \( x \notin C \), then \( x \in A \setminus C \). In either case \( x \in (A \setminus B) \cup (A \setminus C) \) by @def-union.

\( (\supseteq) \) Let \( x \in (A \setminus B) \cup (A \setminus C) \). By @def-union, \( x \in A \setminus B \) or \( x \in A \setminus C \). In the first case \( x \in A \) and \( x \notin B \); in the second, \( x \in A \) and \( x \notin C \). In both cases \( x \in A \), and "\( x \notin B \) or \( x \notin C \)" is true, so by @thm-de-morgan-logic "\( x \in B \) and \( x \in C \)" is false, that is, \( x \notin B \cap C \). Hence \( x \in A \setminus (B \cap C) \).

This proves the equality.
:::

::: {#exr-sets-b2}
[B2: A distributive law]

Let \( A \), \( B \), \( C \) be sets. Prove that \( A \cap (B \cup C) = (A \cap B) \cup (A \cap C) \), which is part (a) of @thm-distributive-sets.
:::

::: {.solution}
We use @thm-double-inclusion.

\( (\subseteq) \) Let \( x \in A \cap (B \cup C) \). Then \( x \in A \) and \( x \in B \cup C \), so \( x \in B \) or \( x \in C \). If \( x \in B \), then \( x \in A \cap B \); if \( x \in C \), then \( x \in A \cap C \). In either case \( x \in (A \cap B) \cup (A \cap C) \).

\( (\supseteq) \) Let \( x \in (A \cap B) \cup (A \cap C) \). If \( x \in A \cap B \), then \( x \in A \) and \( x \in B \subseteq B \cup C \). If \( x \in A \cap C \), then \( x \in A \) and \( x \in C \subseteq B \cup C \). In either case \( x \in A \) and \( x \in B \cup C \), so \( x \in A \cap (B \cup C) \).

This proves the equality.
:::

::: {#exr-sets-b3}
[B3: An indexed intersection]

Prove that
\[
\bigcap_{n=1}^{\infty} \Bigl( -\frac1n, \frac1n \Bigr) = \{0\}.
\]
You may use the fact that for every real \( x > 0 \) there is an integer \( n \ge 1 \) with \( 1/n < x \).
:::

::: {.solution}
Write \( B_n = (-1/n, 1/n) \) and \( B = \bigcap_{n \ge 1} B_n \). We use @thm-double-inclusion.

\( (\supseteq) \) For every \( n \ge 1 \), \( -1/n < 0 < 1/n \), so \( 0 \in B_n \). By @def-indexed-family, \( 0 \in B \).

\( (\subseteq) \) Let \( x \in B \). Suppose, for a contradiction, that \( x \ne 0 \). Then \( \lvert x \rvert > 0 \), so there is an integer \( n \ge 1 \) with \( 1/n < \lvert x \rvert \). Then \( x \ge 1/n \) or \( x \le -1/n \), so \( x \notin B_n \). This contradicts \( x \in B \), which requires \( x \in B_n \) for **every** \( n \). Hence \( x = 0 \), that is, \( x \in \{0\} \).

This shows \( B = \{0\} \).
:::

### C. Going deeper

::: {#exr-sets-c1}
[C1: When union equals intersection]

Let \( A \) and \( B \) be sets. Prove that \( A \cup B = A \cap B \) if and only if \( A = B \).
:::

::: {.solution}
\( (\Leftarrow) \) Suppose \( A = B \). Then \( A \cup B = A \cup A \) and \( A \cap B = A \cap A \). By @def-union and @def-intersection, "\( x \in A \) or \( x \in A \)" and "\( x \in A \) and \( x \in A \)" are both equivalent to \( x \in A \), so \( A \cup A = A = A \cap A \). Hence \( A \cup B = A \cap B \).

\( (\Rightarrow) \) Suppose \( A \cup B = A \cap B \). We show \( A = B \) using @thm-double-inclusion.

\( (\subseteq) \) Let \( x \in A \). Then \( x \in A \cup B \) by @def-union. Since \( A \cup B = A \cap B \), we get \( x \in A \cap B \), and in particular \( x \in B \).

\( (\supseteq) \) Swapping the roles of \( A \) and \( B \) in the previous paragraph, which is allowed since \( A \cup B = B \cup A \) and \( A \cap B = B \cap A \), gives \( B \subseteq A \).

Hence \( A = B \). This proves the equivalence.
:::

::: {#exr-sets-c2}
[C2: Counting subsets]

For a finite set \( S \), write \( \lvert S \rvert \) for its number of elements. The aim is to prove that \( \lvert \powerset{S} \rvert = 2^{\lvert S \rvert} \) for every finite set \( S \).

::: {.enumerate options="label=(\alph*)"}
1. Check the claim when \( S = \varnothing \).
2. Let \( S \) have \( n + 1 \) elements, fix \( s \in S \), and let \( S' = S \setminus \{s\} \). Show that every subset \( X \) of \( S \) belongs to exactly one of the two collections: the subsets of \( S \) with \( s \notin X \), and the subsets of \( S \) with \( s \in X \).
3. Show that the subsets of \( S \) with \( s \notin X \) are exactly the subsets of \( S' \), and that \( X \mapsto X \setminus \{s\} \) and \( T \mapsto T \cup \{s\} \) pair off the subsets of \( S \) containing \( s \) with the subsets of \( S' \), each undoing the other.
4. Hence prove the claim by induction on \( n = \lvert S \rvert \).
:::

*Hint: in (c), use double inclusion to check that \( (X \setminus \{s\}) \cup \{s\} = X \) when \( s \in X \).*
:::

::: {.solution}
(a) The only subset of \( \varnothing \) is \( \varnothing \) itself, since any \( X \subseteq \varnothing \) has no elements and so equals \( \varnothing \) by @thm-double-inclusion. So \( \powerset{\varnothing} = \{\varnothing\} \) has \( 1 = 2^0 \) element.

(b) Let \( X \subseteq S \). The statement \( s \in X \) is either true or false, and not both. So \( X \) lies in exactly one of the two collections.

(c) *First collection.* If \( X \subseteq S \) and \( s \notin X \), then every \( x \in X \) lies in \( S \) and is not \( s \), so \( x \in S' \); hence \( X \subseteq S' \). Conversely, if \( T \subseteq S' \), then \( T \subseteq S \) and \( s \notin T \), since no element of \( S' \) equals \( s \). So the first collection is exactly \( \powerset{S'} \).

*Second collection.* If \( X \subseteq S \) with \( s \in X \), then \( X \setminus \{s\} \subseteq S' \). If \( T \subseteq S' \), then \( T \cup \{s\} \subseteq S \) contains \( s \). Now we check that the two operations undo each other. For \( X \) containing \( s \): an element lies in \( (X \setminus \{s\}) \cup \{s\} \) exactly when it is in \( X \) and not \( s \), or it is \( s \); since \( s \in X \), this is exactly when it is in \( X \). So \( (X \setminus \{s\}) \cup \{s\} = X \). For \( T \subseteq S' \): an element lies in \( (T \cup \{s\}) \setminus \{s\} \) exactly when it is in \( T \) or equal to \( s \), and not equal to \( s \); since \( s \notin T \), this is exactly when it is in \( T \). So \( (T \cup \{s\}) \setminus \{s\} = T \). Hence the two operations pair the subsets of \( S \) containing \( s \) one-to-one with the subsets of \( S' \), and the two collections have the same number of elements.

(d) Let \( P(n) \) be the statement "every set with \( n \) elements has exactly \( 2^n \) subsets". We use @thm-induction with \( n_0 = 0 \). The base case \( P(0) \) is (a), since the only set with no elements is \( \varnothing \). Let \( n \ge 0 \), suppose \( P(n) \), and let \( S \) have \( n + 1 \) elements. Fix \( s \in S \), which exists since \( n + 1 \ge 1 \), and let \( S' = S \setminus \{s\} \), a set with \( n \) elements. By (b), the number of subsets of \( S \) is the size of the first collection plus the size of the second. By (c) and the induction hypothesis, each of these sizes equals \( \lvert \powerset{S'} \rvert = 2^n \). Hence \( S \) has \( 2^n + 2^n = 2^{n+1} \) subsets, which is \( P(n + 1) \). By @thm-induction, \( P(n) \) holds for every \( n \in \nN \), as claimed.
:::
