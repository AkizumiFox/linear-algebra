# Infinite-Dimensional Spaces

Every theorem about bases so far has assumed a finite spanning list. Yet several of our running examples have none: \( F[x] \) is not finite-dimensional (@thm-polynomials-infinite-dimensional), and neither are the sequences or the functions \( \nR \to \nR \). Do such spaces have a basis at all? This section shows that they always do, using a principle from set theory called Zorn's Lemma, and then looks honestly at the price. The basis exists, but often nobody can write it down, and several finite-dimensional facts stop being true.

## Bases of infinite sets of vectors

An infinite-dimensional space cannot have a finite basis, so a basis now has to be an infinite collection of vectors. We recall the conventions for arbitrary subsets, set up with the span (@def-span) and with independence (@def-linear-independence). A linear combination always involves **finitely many** vectors, because the axioms only let us add two vectors at a time.

Let \( S \subseteq V \) be any subset, finite or infinite.

- \( \Span(S) \) is the set of all linear combinations \( a_1\v_1 + \dots + a_k\v_k \) with \( k \in \nN \), \( a_i \in F \) and \( \v_i \in S \).
- \( S \) is **linearly independent** if **every finite list of distinct vectors** of \( S \) is linearly independent in the sense of @def-linear-independence.
- \( S \) is a **basis** of \( V \) if \( S \) is linearly independent and \( \Span(S) = V \).

For a finite set \( S = \{\v_1, \dots, \v_k\} \) of distinct vectors, these agree with the notions for the list \( (\v_1, \dots, \v_k) \), since a sub-list of an independent list is independent. The empty set is independent: its only finite list of distinct vectors is the empty list. In the infinite case we lose the ordering of a basis, and we will not need it.

::: {#exm-basis-of-polynomials}
[A Basis of \( F[x] \)]

Show that \( \{ x^k : k \in \nN \} = \{1, x, x^2, \dots\} \) is a basis of \( F[x] \).
:::

::: {.solution}
*Spanning.* By @def-polynomial, every polynomial can be written as \( a_0 + a_1x + \dots + a_Nx^N \) for some \( N \in \nN \). This is a finite linear combination of \( 1, x, \dots, x^N \).

*Independence.* Let \( x^{k_1}, \dots, x^{k_m} \) be distinct monomials and suppose \( a_1x^{k_1} + \dots + a_mx^{k_m} = 0 \). The left side is the polynomial whose coefficient of \( x^{k_j} \) is \( a_j \), because the exponents \( k_j \) are distinct. The zero polynomial has every coefficient equal to \( 0 \), so by the definition of equality of polynomials, \( a_j = 0 \) for every \( j \).

Hence \( \{ x^k : k \in \nN \} \) is a basis of \( F[x] \).
:::

The sequence space behaves differently. Let \( F^{\nN} \) be the space of all sequences \( (a_0, a_1, a_2, \dots) \) with entries in \( F \), with entrywise addition and scaling. For \( i \in \nN \) let \( \e_i \) be the sequence with \( 1 \) in position \( i \) and \( 0 \) everywhere else.

::: {#exm-sequence-standard-vectors}
[The Vectors \( \e_i \) Do Not Span \( F^{\nN} \)]

Show that \( \{ \e_i : i \in \nN \} \) is linearly independent in \( F^{\nN} \), but is **not** a basis of \( F^{\nN} \).
:::

::: {.solution}
*Independence.* Let \( i_1, \dots, i_m \) be distinct and suppose \( a_1\e_{i_1} + \dots + a_m\e_{i_m} = \0 \). Position \( i_j \) of the left side is \( a_j \), since only \( \e_{i_j} \) has a non-zero entry there. Position \( i_j \) of the zero sequence is \( 0 \), so \( a_j = 0 \) for every \( j \).

*Not spanning.* A linear combination \( a_1\e_{i_1} + \dots + a_m\e_{i_m} \) has non-zero entries only in the \( m \) positions \( i_1, \dots, i_m \). So every vector in \( \Span\{\e_i : i \in \nN\} \) has only finitely many non-zero entries. The sequence \( (1, 1, 1, \dots) \) has infinitely many, so it is not in the span.
:::

The same example shows that \( F^{\nN} \) is infinite-dimensional. For each \( n \), the list \( (\e_0, \dots, \e_n) \) is independent of length \( n + 1 \). If a list of length \( m \) spanned \( F^{\nN} \), then \( n + 1 \le m \) for every \( n \) by @thm-steinitz, which is impossible.

::: {.warning}
It is tempting to write \( (1, 1, 1, \dots) = \e_0 + \e_1 + \e_2 + \cdots \). In a vector space this sum **means nothing**: the axioms define sums of two vectors, hence of finitely many, and an infinite sum would need a notion of limit. So "the \( \e_i \) span" is false, even though every sequence is "made of" its entries. Infinite sums return only in spaces with a notion of distance, much later.
:::

:::: {.check}
Let \( V \) be the space of formal power series \( a_0 + a_1x + a_2x^2 + \cdots \) over \( F \), that is, \( F^{\nN} \) with \( x^k \) standing for \( \e_k \). Is \( \{1, x, x^2, \dots\} \) a basis of \( V \)?

::: {.solution}
No. It is independent, by the argument of @exm-sequence-standard-vectors. But its span consists of the series with only finitely many non-zero coefficients, which are the polynomials. The series \( 1 + x + x^2 + \cdots \) is not among them, so the set does not span \( V \).
:::
::::

So does \( F^{\nN} \) have a basis? In finite dimension we built bases by sifting (@thm-sift) or by extending one vector at a time (@thm-basis-extension). Both constructions stop after finitely many steps. For \( F^{\nN} \) no step-by-step process can stop, and we need a different kind of existence argument.

## Zorn's Lemma

Look again at what a basis is in finite dimension: an independent list that cannot be enlarged (@thm-maximal-indep). "Cannot be enlarged" is a statement about the family of all independent sets, ordered by inclusion. Zorn's Lemma is a general principle that produces objects which cannot be enlarged. To state it we need words for orderings.

*A partial order is a way of comparing elements in which some pairs may be incomparable.*

:::: {#def-partial-order}
[Partial Order, Chain, Upper Bound, Maximal Element]

Let \( P \) be a set. A **partial order** on \( P \) is a relation \( \le \) on \( P \) (@def-relation) such that, **for all** \( p, q, r \in P \):

::: {.enumerate options="label=(P\arabic*)"}
1. \( p \le p \) (reflexive);
2. if \( p \le q \) and \( q \le p \), then \( p = q \) (antisymmetric);
3. if \( p \le q \) and \( q \le r \), then \( p \le r \) (transitive).
:::

Let \( (P, \le) \) be a partially ordered set.

- A **chain** in \( P \) is a subset \( C \subseteq P \) such that **for all** \( p, q \in C \), \( p \le q \) or \( q \le p \).
- An **upper bound** of a subset \( C \subseteq P \) is an element \( u \in P \) with \( c \le u \) **for every** \( c \in C \).
- A **maximal element** of \( P \) is an element \( m \in P \) such that **no** \( p \in P \) satisfies \( m \le p \) and \( p \ne m \).
::::

In words: a chain is a subset in which any two elements can be compared. An upper bound of \( C \) sits above everything in \( C \), but it only has to lie in \( P \), **not** in \( C \). A maximal element has nothing strictly above it. It is **not** required to lie above everything else.

::: {#exm-partial-orders}
[Inclusion as a Partial Order]

Let \( X \) be a set and \( P \) the power set of \( X \) (@def-power-set), ordered by \( \subseteq \). Check that this is a partial order, and describe chains, upper bounds and maximal elements when \( X = \{1, 2\} \). Then do the same for the subsets of \( \{1, 2\} \) with **at most one** element.
:::

::: {.solution}
Every set satisfies \( A \subseteq A \), which is (P1). If \( A \subseteq B \) and \( B \subseteq A \), then \( A = B \) by @thm-double-inclusion, which is (P2). Inclusion is transitive, which is (P3).

For \( X = \{1, 2\} \), the set \( C = \{ \varnothing, \{1\}, \{1, 2\} \} \) is a chain, while \( \{1\} \) and \( \{2\} \) are incomparable, so \( \{ \{1\}, \{2\} \} \) is not a chain. The set \( \{1, 2\} \) is an upper bound of every subset of \( P \), and it is the only maximal element.

Now let \( Q = \{ \varnothing, \{1\}, \{2\} \} \), still ordered by \( \subseteq \). Both \( \{1\} \) and \( \{2\} \) are maximal: nothing in \( Q \) strictly contains either. Neither is above the other. The subset \( \{ \{1\}, \{2\} \} \) has no upper bound in \( Q \).
:::

::: {#thm-zorn}
[Zorn's Lemma]

Let \( (P, \le) \) be a **non-empty** partially ordered set in which **every non-empty chain** has an upper bound in \( P \). Then \( P \) has a maximal element.
:::

We do not prove Zorn's Lemma, and no proof is possible from the other everyday rules of set theory. It is equivalent to the **axiom of choice**, the principle already used to build right inverses of surjections in @thm-right-inverse-iff-surjective: from any family of non-empty sets one may choose one element from each. Mathematicians accept it as an axiom, and we do too. In this section we point out each place where it is used.

::: {.warning}
"Maximal" is not "largest". The partially ordered set \( Q \) in @exm-partial-orders has two maximal elements and no largest one. For bases this is the familiar fact that a space has many bases: in \( \nR^2 \), both \( \{\e_1, \e_2\} \) and \( \{(1, 1), (1, -1)\} \) are maximal independent sets, and neither contains the other.
:::

## Every vector space has a basis

We prove the more general extension statement first, since the existence of a basis is the case \( S = \varnothing \).

::: {#thm-basis-extension-general}
[Basis Extension, General Form]

Let \( V \) be a vector space over \( F \), and let \( S \subseteq V \) be a linearly independent subset. Then there is a basis \( B \) of \( V \) with \( S \subseteq B \).
:::

::: {.idea}
① Let \( P \) be the family of independent sets containing \( S \), ordered by \( \subseteq \). ② A chain has the union as an upper bound, because an independence test uses only finitely many vectors, and finitely many members of a chain all fit inside one of them. ③ Zorn gives a maximal \( B \). ④ If some \( \v \) were outside \( \Span(B) \), then \( B \cup \{\v\} \) would be a bigger independent set, so \( B \) spans.
:::

:::: {.proof}
Let \( P \) be the set of all linearly independent subsets \( T \subseteq V \) with \( S \subseteq T \), partially ordered by \( \subseteq \) (see @exm-partial-orders). Since \( S \) is independent, \( S \in P \), so \( P \) is non-empty.

**Step 1: every non-empty chain has an upper bound.** Let \( C \subseteq P \) be a non-empty chain and let \( U = \bigcup_{T \in C} T \). Every \( T \in C \) contains \( S \) and \( C \) is non-empty, so \( S \subseteq U \), and \( T \subseteq U \) for every \( T \in C \).

::: {.claim}
If \( T_1, \dots, T_k \in C \) with \( k \ge 1 \), then one of them contains all the others.
:::

::: {.proof}
We use induction on \( k \). For \( k = 1 \) there is nothing to prove. Suppose the claim holds for \( k \), and let \( T_1, \dots, T_{k+1} \in C \). By the induction hypothesis some \( T_j \) contains \( T_1, \dots, T_k \). Since \( C \) is a chain, \( T_j \subseteq T_{k+1} \) or \( T_{k+1} \subseteq T_j \). In the first case \( T_{k+1} \) contains all of \( T_1, \dots, T_{k+1} \), and in the second case \( T_j \) does.
:::

Now let \( (\u_1, \dots, \u_k) \) be a list of distinct vectors of \( U \). If \( k = 0 \), the empty list is independent. Otherwise, each \( \u_i \) lies in some \( T_i \in C \), and by the Claim one of \( T_1, \dots, T_k \), say \( T_j \), contains all the \( \u_i \). Since \( T_j \) is independent, the list \( (\u_1, \dots, \u_k) \) is independent. Hence \( U \) is independent, so \( U \in P \), and \( U \) is an upper bound of \( C \).

**Step 2: a maximal element.** By Step 1 and @thm-zorn, \( P \) has a maximal element \( B \). Thus \( B \) is independent and \( S \subseteq B \).

**Step 3: \( B \) spans \( V \).** Suppose not, and let \( \v \in V \) with \( \v \notin \Span(B) \). Then \( \v \notin B \), since \( B \subseteq \Span(B) \). We show \( B \cup \{\v\} \) is independent. Take a list of distinct vectors of \( B \cup \{\v\} \). If \( \v \) is not in the list, the list lies in \( B \) and is independent. Otherwise, after reordering (which does not affect independence, as addition is commutative), the list is \( (\v, \w_1, \dots, \w_m) \) with distinct \( \w_i \in B \). Let
\[
a\v + b_1\w_1 + \dots + b_m\w_m = \0.
\]
If \( a \ne 0 \), then \( \v = -a^{-1}(b_1\w_1 + \dots + b_m\w_m) \in \Span(B) \), a contradiction. So \( a = 0 \), and then \( b_1 = \dots = b_m = 0 \) because \( B \) is independent. Hence \( B \cup \{\v\} \in P \), it contains \( B \), and it is not equal to \( B \). This contradicts the maximality of \( B \). Therefore \( \Span(B) = V \), and \( B \) is a basis of \( V \) containing \( S \).
::::

Notice where finiteness went. Steps 1 and 3 each look at only finitely many vectors at a time, which is all that linear algebra ever does. The one infinite step, "keep enlarging until you cannot", is handed to Zorn's Lemma.

::: {#thm-every-space-has-basis}
[Every Vector Space Has a Basis]

Every vector space \( V \) over a field \( F \) has a basis.
:::

::: {.proof}
The empty set is linearly independent. By @thm-basis-extension-general with \( S = \varnothing \), \( V \) has a basis. For \( V = \{\0\} \) that basis is \( \varnothing \), since \( \Span(\varnothing) = \{\0\} \).
:::

So \( F^{\nN} \) has a basis, and so do \( \nR^{\nR} \) and the continuous functions on \( [0, 1] \). The theorem does not tell us what these bases are.

## Existence without construction: \( \nR \) over \( \nQ \)

The real numbers form a vector space over \( \nQ \): add reals as usual, and multiply a real by a rational. By @thm-every-space-has-basis this space has a basis, often called a **Hamel basis**. Nobody has ever written one down, and nobody will. It is known that the existence of such a basis cannot be proved without some form of the axiom of choice. What we **can** prove is that this basis is infinite. The tool is counting.

*A countable set is one whose elements can be listed as a sequence, possibly with repeats.*

::: {#def-countable}
[Countable Set]

A set \( A \) is **countable** if \( A = \varnothing \) or there is a **surjective** function \( \nN \to A \). Otherwise \( A \) is **uncountable**.
:::

A surjection \( \sigma \colon \nN \to A \) lists \( A \) as \( \sigma(0), \sigma(1), \sigma(2), \dots \), and every element of \( A \) appears somewhere. Repeats are allowed, so every finite non-empty set is countable. The next lemma collects what we need.

:::: {#lem-countable-sets}
[Countable Sets]

::: {.enumerate options="label=(\alph*)"}
1. If \( A \) is countable and \( f \colon A \to A' \) is surjective, then \( A' \) is countable.
2. \( \nN \times \nN \) is countable.
3. If \( A \) and \( A' \) are countable, then \( A \times A' \) is countable.
4. \( \nQ \) is countable, and \( \nQ^n \) is countable for every \( n \ge 1 \).
:::
::::

::: {.proof}
(a) If \( A = \varnothing \), then \( A' = f(A) = \varnothing \). Otherwise take a surjection \( \sigma \colon \nN \to A \). Then \( f \circ \sigma \colon \nN \to A' \) is surjective by @thm-composition-preserves (a composite of surjections is surjective).

(b) For \( n \in \nN \), let \( 2^{a} \) be the largest power of \( 2 \) dividing \( n + 1 \); it exists because \( 2^a \le n + 1 \) bounds \( a \). Then \( (n + 1)/2^a \) is odd, so it equals \( 2b + 1 \) for a unique \( b \in \nN \). Put \( g(n) = (a, b) \). Given \( (a, b) \in \nN \times \nN \), let \( n = 2^a(2b + 1) - 1 \). The largest power of \( 2 \) dividing \( 2^a(2b+1) \) is \( 2^a \), because \( 2^{a+1} \mid 2^a(2b + 1) \) would force \( 2 \mid 2b + 1 \). Hence \( g(n) = (a, b) \), and \( g \) is surjective.

(c) If \( A \) or \( A' \) is empty, so is \( A \times A' \). Otherwise take surjections \( \sigma \colon \nN \to A \) and \( \tau \colon \nN \to A' \). The map \( \nN \times \nN \to A \times A' \), \( (m, n) \mapsto (\sigma(m), \tau(n)) \), is surjective. By (b) and (a), \( A \times A' \) is countable.

(d) The map \( \nN \to \nZ \) sending an even \( m \) to \( m/2 \) and an odd \( m \) to \( -(m + 1)/2 \) is surjective, so \( \nZ \) is countable. The map \( \nZ \times \nN \to \nQ \), \( (p, q) \mapsto p/(q + 1) \), is surjective, so \( \nQ \) is countable by (c) and (a). Finally \( \nQ^{n+1} \) is \( \nQ^n \times \nQ \) after identifying \( (q_1, \dots, q_{n+1}) \) with \( ((q_1, \dots, q_n), q_{n+1}) \), so induction on \( n \) with (c) shows that \( \nQ^n \) is countable for every \( n \ge 1 \).
:::

The real numbers are not countable. This is a fact about \( \nR \), not about linear algebra, and its proof needs one property of \( \nR \) that we take from analysis: the **nested interval property**. If \( I_0 \supseteq I_1 \supseteq I_2 \supseteq \cdots \) are closed bounded intervals \( [a_n, b_n] \) with \( a_n \le b_n \), then some real number lies in every \( I_n \).

::: {#lem-reals-uncountable}
[\( \nR \) Is Uncountable]

Assuming the nested interval property, there is no surjection \( \nN \to \nR \).
:::

::: {.proof}
Let \( r \colon \nN \to \nR \) be any function. We build closed intervals \( I_0 \supseteq I_1 \supseteq \cdots \) of positive length with \( r(n) \notin I_n \). Split \( [0, 1] \) into the thirds \( [0, \frac13] \) and \( [\frac23, 1] \). They are disjoint, so \( r(0) \) misses at least one of them; let \( I_0 \) be such a third. Given \( I_n = [a, b] \) with \( a < b \), the intervals \( [a, a + \frac{b - a}{3}] \) and \( [b - \frac{b - a}{3}, b] \) are disjoint and lie in \( I_n \), so \( r(n+1) \) misses one of them; let \( I_{n+1} \) be that one. By the nested interval property some \( x \) lies in every \( I_n \). For each \( n \), \( x \in I_n \) and \( r(n) \notin I_n \), so \( x \ne r(n) \). Hence \( x \) is not a value of \( r \), and \( r \) is not surjective.
:::

::: {#thm-reals-infinite-dimensional-over-rationals}
[\( \nR \) Is Infinite-Dimensional over \( \nQ \)]

The vector space \( \nR \) over \( \nQ \) is not finite-dimensional.
:::

::: {.proof}
Suppose a finite list spans \( \nR \) over \( \nQ \). Appending \( 1 \) keeps it spanning, so we may take a spanning list \( (b_1, \dots, b_n) \) with \( n \ge 1 \). Then the map
\[
\nQ^n \to \nR, \qquad (q_1, \dots, q_n) \mapsto q_1b_1 + \dots + q_nb_n
\]
is surjective, since every real number is a rational linear combination of \( b_1, \dots, b_n \). By @lem-countable-sets (d) and (a), \( \nR \) is countable. This contradicts @lem-reals-uncountable. Hence \( \nR \) is not finite-dimensional over \( \nQ \).
:::

The proof really shows more: **every** finite-dimensional vector space over \( \nQ \) is countable. It is honest about its inputs. Linear algebra supplied only "a spanning list gives a surjection from \( \nQ^n \)"; the rest is counting and one property of the real line.

:::: {.check}
Is \( \nC \) finite-dimensional as a vector space over \( \nQ \)?

::: {.solution}
No. If \( \nC \) were countable, then \( \nR \subseteq \nC \) would be countable too: pick any \( y_0 \in \nR \) and send \( z \in \nC \) to \( z \) if \( z \in \nR \) and to \( y_0 \) otherwise, a surjection \( \nC \to \nR \), and apply @lem-countable-sets (a). That contradicts @lem-reals-uncountable. So \( \nC \) is uncountable, and the proof of @thm-reals-infinite-dimensional-over-rationals, with \( \nC \) in place of \( \nR \), shows it is not finite-dimensional over \( \nQ \).
:::
::::

## What changes in infinite dimension

Several finite-dimensional theorems use a count, and counting is exactly what fails here.

::: {.warning}
**A proper subspace can be as big as the whole space.** In finite dimension, \( U \subseteq V \) with \( \dim U = \dim V \) forces \( U = V \) (@thm-dim-impl-eq). Now let \( U = \{ p \in F[x] : \text{the constant coefficient of } p \text{ is } 0 \} \). By the argument of @exm-basis-of-polynomials, \( U \) has the basis \( \{x, x^2, x^3, \dots\} \), and \( x^k \leftrightarrow x^{k+1} \) matches it one-to-one with the basis \( \{1, x, x^2, \dots\} \) of \( F[x] \). Yet \( 1 \notin U \), so \( U \ne F[x] \). The same happens in \( F^{\nN} \): the sequences with first entry \( 0 \) form a proper subspace, and deleting that first entry matches it one-to-one with all of \( F^{\nN} \), respecting addition and scaling. In Chapter 3 this becomes the shift map, which is injective but not surjective.
:::

::: {.remark}
In an infinite-dimensional space, "\( \dim V = \infty \)" hides real differences of size: \( F[x] \) has a countable basis, while every basis of \( \nR \) over \( \nQ \) is uncountable (@exr-infinite-dimensional-c2), and set theory shows that all bases of one space have the same cardinality, a fact we will not develop.
:::

**Scope.** From here on the book is mostly about finite-dimensional spaces, where bases are finite lists and counting works. Every theorem that needs finite dimension says so in its hypotheses. Infinite-dimensional spaces return with more structure, such as inner products and limits, where infinite sums can finally be given a meaning.

## Exercises

### A. Check your understanding

:::: {#exr-infinite-dimensional-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define what it means for an arbitrary subset \( S \) of a vector space \( V \) to be a basis of \( V \).
2. State Zorn's Lemma, including the meaning of "chain" and "upper bound".
3. True or false: \( \{ \e_i : i \in \nN \} \) is a basis of \( F^{\nN} \). Justify your answer.
4. True or false: every linearly independent subset of an infinite-dimensional space is infinite. Justify your answer.
5. True or false: in a partially ordered set, a maximal element \( m \) satisfies \( p \le m \) for every \( p \). Justify your answer.
:::
::::

::: {.solution}
(a) \( S \) is a basis if every finite list of distinct vectors of \( S \) is linearly independent, and every vector of \( V \) is a linear combination of finitely many vectors of \( S \).

(b) See @thm-zorn and @def-partial-order: a non-empty partially ordered set in which every non-empty chain (a subset whose elements are pairwise comparable) has an upper bound (an element of \( P \) above every element of the chain) has a maximal element.

(c) False. The set is independent, but \( (1, 1, 1, \dots) \) is not a finite linear combination of the \( \e_i \) (@exm-sequence-standard-vectors).

(d) False. The empty set and \( \{x\} \subseteq F[x] \) are finite independent subsets of the infinite-dimensional space \( F[x] \).

(e) False. In \( Q = \{ \varnothing, \{1\}, \{2\} \} \) ordered by \( \subseteq \), the element \( \{1\} \) is maximal, but \( \{2\} \not\subseteq \{1\} \) (@exm-partial-orders).
:::

### B. Practice

:::: {#exr-infinite-dimensional-b1}
[B1: Finitely Supported Sequences]

Let \( F^{(\nN)} \subseteq F^{\nN} \) be the set of sequences with only finitely many non-zero entries.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( F^{(\nN)} \) is a subspace of \( F^{\nN} \).
2. Prove that \( \{ \e_i : i \in \nN \} \) is a basis of \( F^{(\nN)} \).
:::
::::

::: {.solution}
(a) We use @thm-subspace-test. (1) The zero sequence has no non-zero entries, so \( \0 \in F^{(\nN)} \). (2) Let \( \x, \y \in F^{(\nN)} \), with non-zero entries only in finite sets of positions \( A \) and \( A' \). If \( i \notin A \cup A' \), then \( x_i + y_i = 0 + 0 = 0 \). So \( \x + \y \) has non-zero entries only in the finite set \( A \cup A' \), and \( \x + \y \in F^{(\nN)} \). (3) Let \( c \in F \). If \( i \notin A \), then \( cx_i = c \cdot 0 = 0 \), so \( c\x \in F^{(\nN)} \). Hence \( F^{(\nN)} \) is a subspace.

(b) Each \( \e_i \) lies in \( F^{(\nN)} \), and the set is independent by @exm-sequence-standard-vectors. For spanning, let \( \x \in F^{(\nN)} \) have non-zero entries only in positions \( i_1, \dots, i_m \). Then \( \x \) and \( x_{i_1}\e_{i_1} + \dots + x_{i_m}\e_{i_m} \) agree in positions \( i_1, \dots, i_m \) and are both \( 0 \) elsewhere, so they are equal. Hence \( \{ \e_i : i \in \nN \} \) is a basis of \( F^{(\nN)} \).
:::

:::: {#exr-infinite-dimensional-b2}
[B2: Exponentials Are Independent]

For \( k \in \nN \) let \( f_k \in \nR^{\nR} \) be \( f_k(x) = e^{kx} \). Prove that \( \{ f_k : k \in \nN \} \) is linearly independent. Hence deduce that \( \nR^{\nR} \) is infinite-dimensional.

*Hint: divide by the fastest-growing term.*
::::

::: {.solution}
Suppose not. Then there are distinct \( k_1 < k_2 < \dots < k_m \) and scalars \( a_1, \dots, a_m \), not all zero, with \( a_1e^{k_1x} + \dots + a_me^{k_mx} = 0 \) for every \( x \in \nR \). Discarding terms with zero coefficient, we may assume \( a_m \ne 0 \). Dividing by \( e^{k_mx} > 0 \) gives, for every \( x \in \nR \),
\[
a_m = -\sum_{j=1}^{m-1} a_j e^{(k_j - k_m)x}.
\]
Since \( k_j - k_m < 0 \) for \( j < m \), each \( e^{(k_j - k_m)x} \to 0 \) as \( x \to \infty \), so the right side tends to \( 0 \). The left side is the constant \( a_m \), so \( a_m = 0 \), a contradiction. Hence the set is independent.

For each \( n \), the list \( (f_0, \dots, f_n) \) is independent of length \( n + 1 \). If a list of length \( m \) spanned \( \nR^{\nR} \), @thm-steinitz would give \( n + 1 \le m \) for every \( n \), which is impossible. Hence \( \nR^{\nR} \) is infinite-dimensional.
:::

:::: {#exr-infinite-dimensional-b3}
[B3: Continuous Functions]

Let \( C[0, 1] \) be the space of continuous functions \( [0, 1] \to \nR \). Prove that \( C[0, 1] \) is infinite-dimensional.

*Hint: use "tent" functions supported on disjoint intervals, and choose good points.*
::::

::: {.solution}
For \( k \ge 1 \), let \( m_k = \frac12\left(\frac1{k+1} + \frac1k\right) \) and \( r_k = \frac12\left(\frac1k - \frac1{k+1}\right) > 0 \), the midpoint and half-length of \( J_k = [\frac1{k+1}, \frac1k] \). Define
\[
t_k(x) = \max\bigl(0, \; r_k - \lvert x - m_k \rvert\bigr).
\]
This is continuous, as built from continuous functions by \( \lvert \cdot \rvert \) and \( \max \). Also \( t_k(x) > 0 \) exactly when \( \lvert x - m_k \rvert < r_k \), that is, when \( x \) lies in the open interval \( (\frac1{k+1}, \frac1k) \). These open intervals are pairwise disjoint, and \( m_j \) lies in the \( j \)-th one. Hence \( t_k(m_j) = 0 \) for \( j \ne k \), while \( t_k(m_k) = r_k \).

Let \( a_1t_1 + \dots + a_nt_n = 0 \). Evaluating at \( m_j \) gives \( a_jr_j = 0 \), so \( a_j = 0 \) since \( r_j \ne 0 \). Hence \( (t_1, \dots, t_n) \) is independent for every \( n \). As in @exr-infinite-dimensional-b2, @thm-steinitz shows that no finite list spans \( C[0, 1] \).
:::

### C. Going deeper

:::: {#exr-infinite-dimensional-c1}
[C1: Complements in Any Dimension]

Let \( U \) be a subspace of a vector space \( V \), of any dimension. Prove that there is a subspace \( W \) of \( V \) with \( V = U \oplus W \), that is, every \( \v \in V \) can be written **uniquely** as \( \u + \w \) with \( \u \in U \), \( \w \in W \).

*Hint: @thm-basis-extension-general.*
::::

::: {.solution}
By @thm-every-space-has-basis, \( U \) has a basis \( B_U \). It is independent in \( V \), so by @thm-basis-extension-general there is a basis \( B \) of \( V \) with \( B_U \subseteq B \). Let \( W = \Span(B \setminus B_U) \), a subspace by @thm-span-subspace.

*Existence.* Let \( \v \in V \). Since \( B \) spans, \( \v = \sum_i a_i\u_i + \sum_j b_j\w_j \), a finite sum with \( \u_i \in B_U \) and \( \w_j \in B \setminus B_U \). The first sum lies in \( U \) and the second in \( W \).

*\( U \cap W = \{\0\} \).* Let \( \v \in U \cap W \). Since \( B_U \) spans \( U \) and \( B \setminus B_U \) spans \( W \), we have \( \v = \sum_i a_i\u_i = \sum_j b_j\w_j \) with distinct \( \u_i \in B_U \) and distinct \( \w_j \in B \setminus B_U \). Then \( \sum_i a_i\u_i - \sum_j b_j\w_j = \0 \) is a combination of a list of distinct vectors of \( B \), because \( B_U \) and \( B \setminus B_U \) are disjoint. Since \( B \) is independent, every \( a_i \) and \( b_j \) is \( 0 \), so \( \v = \0 \).

*Uniqueness.* If \( \u + \w = \u' + \w' \) with \( \u, \u' \in U \) and \( \w, \w' \in W \), then \( \u - \u' = \w' - \w \) lies in \( U \cap W = \{\0\} \). Hence \( \u = \u' \) and \( \w = \w' \). This proves \( V = U \oplus W \).
:::

:::: {#exr-infinite-dimensional-c2}
[C2: Bases of \( \nR \) over \( \nQ \) Are Uncountable]

::: {.enumerate options="label=(\alph*)"}
1. Let \( A_0, A_1, A_2, \dots \) be countable sets. Prove that \( \bigcup_{n \in \nN} A_n \) is countable. (You may use the axiom of choice.)
2. Let \( V \) be a vector space over \( \nQ \) with a countable basis. Prove that \( V \) is countable.
3. Deduce that every basis of \( \nR \) over \( \nQ \) is uncountable.
:::

*Hint: for (b), write \( V \) as a union of spans of finite lists.*
::::

::: {.solution}
(a) Let \( A = \bigcup_{n} A_n \). If \( A = \varnothing \) there is nothing to prove; otherwise fix \( a^* \in A \). For each \( n \) with \( A_n \ne \varnothing \), choose a surjection \( \sigma_n \colon \nN \to A_n \) (this is where choice is used). Define \( h \colon \nN \times \nN \to A \) by \( h(n, m) = \sigma_n(m) \) if \( A_n \ne \varnothing \), and \( h(n, m) = a^* \) otherwise. Every \( a \in A \) lies in some non-empty \( A_n \) and equals \( \sigma_n(m) \) for some \( m \), so \( h \) is surjective. By @lem-countable-sets (b) and (a), \( A \) is countable.

(b) If the basis is empty, \( V = \{\0\} \) is countable. Otherwise list the basis as \( \sigma(0), \sigma(1), \dots \) for a surjection \( \sigma \colon \nN \to B \). Every \( \v \in V \) is a combination of finitely many basis vectors, all among \( \sigma(0), \dots, \sigma(n) \) for some \( n \). Hence \( V = \bigcup_n V_n \) with \( V_n = \Span(\sigma(0), \dots, \sigma(n)) \). The map \( \nQ^{n+1} \to V_n \), \( (q_0, \dots, q_n) \mapsto \sum_i q_i\sigma(i) \), is surjective, so each \( V_n \) is countable by @lem-countable-sets (d) and (a). By (a), \( V \) is countable.

(c) By @thm-every-space-has-basis, \( \nR \) has a basis over \( \nQ \). If some basis were countable, then \( \nR \) would be countable by (b), contradicting @lem-reals-uncountable. Hence every basis is uncountable.
:::
