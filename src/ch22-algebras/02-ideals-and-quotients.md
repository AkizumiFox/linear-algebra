# Ideals and Quotients

Subalgebras are the parts of an algebra one can multiply inside. Ideals are the parts one can divide by. Chapter 14 §10 introduced two-sided ideals for one purpose, to cut the Clifford algebra out of the tensor algebra; here they become the tool for taking an algebra apart. Two things are new. First, in a non-commutative algebra there are **three** kinds of ideal, and the difference decides every statement below. Second, the main theorem of the section says that the matrix algebra has no two-sided ideals at all — which is why matrix algebras are the atoms out of which the rest of the chapter builds everything.

## Three kinds of ideal

Section 1 left a set unexplained. In \( M_2(F) \) the matrices \( a\E_{11} \) form a subspace closed under products, but not a subalgebra: the identity is missing. What kind of object is it? Look instead at the slightly bigger set
\[
C_1 = \{ \X \in M_2(F) : \text{column } 2 \text{ of } \X \text{ is } \0 \} = \Span(\E_{11}, \E_{21}) .
\]
Multiplying on the **left** by anything keeps a matrix in \( C_1 \), because \( \A\X \) has \( k \)-th column \( \A\x_k \) (@thm-three-views-of-product), so a zero column stays zero. Multiplying on the **right** does not: \( \E_{11}\E_{12} = \E_{12} \notin C_1 \). Absorption on one side is a genuine phenomenon, and it needs its own name.

*An ideal is a subspace that absorbs multiplication: a left ideal from the left, a right ideal from the right, a two-sided ideal from both.*

::: {#def-left-ideal}
[Left and Right Ideals]

Let \( A \) be an algebra over \( F \) and let \( I \subseteq A \) be a **subspace**. Then \( I \) is

::: {.enumerate options="label=(\alph*)"}
1. a **left ideal** of \( A \) if \( ax \in I \) **for every** \( a \in A \) and **every** \( x \in I \);
2. a **right ideal** of \( A \) if \( xa \in I \) **for every** \( a \in A \) and **every** \( x \in I \).
:::

A **two-sided ideal** is a subspace that is both, which is @def-two-sided-ideal. When \( A \) is commutative the three notions coincide, and we say **ideal**.
:::

Read the quantifiers. The multiplier \( a \) runs over the **whole** algebra, not over \( I \); being closed among one's own elements, which is clause (SA2) of a subalgebra, is a different and much weaker condition. And the definition is not symmetric: in \( C_1 \) above, "every \( a \)" works on the left and fails on the right.

::: {#exm-first-ideals}
[Ideals in five algebras]

::: {.enumerate options="label=(\alph*)"}
1. In any algebra \( A \): \( \{0\} \) and \( A \).
2. In \( F[x] \): the sets \( \langle p\rangle \) of @def-ideal-polynomials.
3. In \( M_n(F) \): the column ideal \( C_j \) of matrices whose columns other than the \( j \)-th are zero.
4. In \( M_n(F) \): the set \( R_U = \{\X : \col(\X) \subseteq U\} \) for a subspace \( U \subseteq F^n \).
5. In any algebra \( A \): the kernel of an algebra homomorphism \( \varphi \colon A \to B \).
:::

Say in each case which of the three kinds of ideal is meant.
:::

::: {.solution}
(a) Two-sided, and these are the degenerate cases: \( \{0\} \) absorbs everything because \( a0 = 0 \), and \( A \) absorbs everything because there is nowhere else to go.

(b) Two-sided, because \( F[x] \) is commutative. Chapter 5's (I1)–(I3) are exactly @def-left-ideal read in a commutative algebra, with (I1) and (I2) replaced by the stronger requirement that \( I \) be a subspace — which is no change, since \( cf = (c1)f \in I \) for a scalar \( c \) by (I3).

(c) A **left** ideal, by the computation above, of dimension \( n \). Not a right ideal for \( n \ge 2 \): \( \E_{jj}\E_{jk} = \E_{jk} \notin C_j \) for \( k \ne j \).

(d) A **right** ideal: \( \col(\X\A) \subseteq \col(\X) \subseteq U \), because each column of \( \X\A \) is a combination of the columns of \( \X \) (@thm-three-views-of-product). Not a left ideal in general: for \( U = \Span(\e_1) \subseteq F^2 \), \( \E_{11} \in R_U \) but \( \E_{21}\E_{11} = \E_{21} \) has column space \( \Span(\e_2) \not\subseteq U \).

(e) Two-sided: this is @lem-quotient-algebra (c).
:::

The non-example is the one Chapter 14 already gave, and it is worth repeating because it is the mistake to avoid. The diagonal matrices in \( M_2(F) \) form a subspace closed under products — a subalgebra, in fact — and are **not** an ideal of any kind: \( \E_{11} \) is diagonal, while \( \E_{21}\E_{11} = \E_{21} \) and \( \E_{11}\E_{12} = \E_{12} \) are not. Closure under one's own products is not absorption.

Why insist on absorbing products with the whole algebra? Because that is exactly the condition under which the quotient vector space \( A/I \) inherits a multiplication, as @lem-quotient-algebra (a) shows: the computation \( x'y' = xy + uy + xw + uw \) needs \( uy \) and \( xw \) to lie in \( I \) when \( u, w \) do, with \( x, y \) arbitrary. The condition is necessary as well: taking \( u = 0 \) leaves \( xw \), which must lie in \( I \) for every \( x \in A \) and \( w \in I \), and taking \( w = 0 \) leaves \( uy \), which must lie in \( I \) for every \( u \in I \) and \( y \in A \). A one-sided ideal gives only half of that, and half is not enough.

::: {.warning}
A two-sided ideal is almost never a subalgebra, and a subalgebra is almost never an ideal. If a left ideal \( I \) contains an invertible element \( u \), then for every \( a \in A \) we have \( a = (au^{-1})u \in I \), so \( I = A \). In particular a **proper** ideal of any kind contains no invertible element, hence does not contain \( 1_A \), hence fails (SA3). The only ideal that is a subalgebra is \( A \) itself.
:::

::: {.check}
In \( M_2(F) \), is \( \Span(\E_{11}) \) a left ideal? A right ideal?
:::

::: {.solution}
Neither. It is a subspace, but \( \E_{21}\E_{11} = \E_{21} \notin \Span(\E_{11}) \), so it is not a left ideal, and \( \E_{11}\E_{12} = \E_{12} \notin \Span(\E_{11}) \), so it is not a right ideal. It is closed under its own products, which is why it looked like something in the warning of Section 1; it is neither a subalgebra nor an ideal. The smallest left ideal containing it is \( C_1 \), and the smallest two-sided ideal containing it is all of \( M_2(F) \), by the theorem below.
:::

## Matrix units multiply in one line

Everything about ideals of \( M_n(F) \) follows from a single product rule. Recall that the **matrix unit** \( \E_{ij} \) has a \( 1 \) in position \( (i,j) \) and zeros elsewhere, and that the \( n^2 \) matrix units are a basis of \( M_n(F) \) (@exm-standard-bases).

::: {#lem-matrix-units}
[The Matrix Unit Product Rule]

Let \( F \) be a field, \( n \ge 1 \), and \( 1 \le i, j, k, l \le n \). Then, in \( M_n(F) \),
\[
\E_{ij}\E_{kl} = \delta_{jk}\,\E_{il},
\qquad\text{and}\qquad
\E_{ij}\,\X\,\E_{kl} = x_{jk}\,\E_{il} \ \text{ for every } \X = (x_{pq}) .
\]
Moreover \( \E_{11} + \E_{22} + \dots + \E_{nn} = \I_n \).
:::

::: {.proof}
Write \( (\E_{ij})_{pq} = \delta_{pi}\delta_{qj} \), which is the definition of the matrix unit. By @thm-three-views-of-product (1),
\[
(\E_{ij}\E_{kl})_{pq} = \sum_{r} \delta_{pi}\delta_{rj}\,\delta_{rk}\delta_{ql}
= \delta_{pi}\delta_{ql}\sum_{r}\delta_{rj}\delta_{rk}
= \delta_{jk}\,\delta_{pi}\delta_{ql} ,
\]
since the only surviving term of the last sum is \( r = j \), which contributes \( 1 \) when \( k = j \) and \( 0 \) otherwise. The right-hand side is the \( (p,q) \) entry of \( \delta_{jk}\E_{il} \).

For the second identity, expand \( \X = \sum_{r,s} x_{rs}\E_{rs} \) in the basis of matrix units and use bilinearity together with the first identity twice:
\[
\E_{ij}\X\E_{kl} = \sum_{r,s} x_{rs}\,\E_{ij}\E_{rs}\E_{kl}
= \sum_{r,s} x_{rs}\,\delta_{jr}\delta_{sk}\,\E_{il}
= x_{jk}\,\E_{il} .
\]
The last statement is the observation that \( \sum_i\E_{ii} \) has \( (p,q) \) entry \( \sum_i \delta_{pi}\delta_{qi} = \delta_{pq} \). This proves the lemma.
:::

The second identity is the one to remember: *sandwiching a matrix between two matrix units extracts one entry and moves it to a chosen place.* Choosing \( i \) and \( l \) freely, a single non-zero entry of \( \X \) can be moved anywhere.

## The matrix algebra is simple

An algebra whose only two-sided ideals are \( \{0\} \) and itself is called **simple**; Section 3 makes this a definition, adding the clause that the algebra be non-zero. The theorem says that matrix algebras are simple over every field.

::: {#thm-matrix-algebra-is-simple}
[The Matrix Algebra Has No Proper Two-Sided Ideals]

Let \( F \) be **any** field and \( n \ge 1 \). The only two-sided ideals of \( M_n(F) \) are \( \{0\} \) and \( M_n(F) \). Consequently, for a finite-dimensional vector space \( V \ne \{\0\} \) over \( F \), the only two-sided ideals of \( \cL(V) \) are \( \{0\} \) and \( \cL(V) \).
:::

::: {.idea}
An ideal that contains anything non-zero contains a matrix with some entry \( x_{jk} \ne 0 \). Sandwich it: @lem-matrix-units turns that one entry into an arbitrary matrix unit, up to the non-zero scalar \( x_{jk} \), which we may divide out. Once the ideal has all \( n^2 \) matrix units, it has their span, and it also has their sum, which is \( \I_n \).
:::

::: {.proof}
Both \( \{0\} \) and \( M_n(F) \) are two-sided ideals. Let \( \cI \) be a two-sided ideal with \( \cI \ne \{0\} \), and choose \( \X \in \cI \) with \( \X \ne 0 \). Then some entry \( x_{jk} \) is non-zero; fix such a pair \( (j, k) \).

Let \( i \) and \( l \) be arbitrary. Since \( \cI \) absorbs multiplication on both sides, \( \E_{ij}\X\E_{kl} \in \cI \), and by @lem-matrix-units this element is \( x_{jk}\E_{il} \). As \( x_{jk} \ne 0 \) it is invertible in \( F \), and \( \cI \) is a subspace, so
\[
\E_{il} = x_{jk}^{-1}\bigl(x_{jk}\E_{il}\bigr) \in \cI .
\]
Hence \( \cI \) contains every matrix unit. The matrix units span \( M_n(F) \) (@exm-standard-bases) and \( \cI \) is a subspace, so \( \cI = M_n(F) \).

For \( \cL(V) \), fix an ordered basis of \( V \) and use the algebra isomorphism \( \cL(V) \to M_n(F) \) recorded after @def-algebra-isomorphism. An algebra isomorphism carries two-sided ideals to two-sided ideals, since it is a linear bijection and \( \varphi(ax) = \varphi(a)\varphi(x) \) in both directions. This proves the theorem.
:::

Nothing in the proof used anything about \( F \) beyond the existence of \( x_{jk}^{-1} \), which is the field axiom. The theorem holds over \( \nQ \), over \( \nC \), and over \( \nF_2 \) alike, and it is the reason matrix algebras will turn out to be the building blocks in this chapter's structure theorem: they cannot be broken.

One consequence is worth recording; §03 proves it again for every simple algebra.

::: {#cor-matrix-homomorphism-injective}
[Homomorphisms out of a Matrix Algebra Are Injective]

Let \( F \) be a field, \( n \ge 1 \), and let \( \varphi \colon M_n(F) \to B \) be an algebra homomorphism into any \( F \)-algebra \( B \ne \{0\} \). Then \( \varphi \) is injective.
:::

::: {.proof}
By @lem-quotient-algebra (c), \( \ker\varphi \) is a two-sided ideal of \( M_n(F) \), so by @thm-matrix-algebra-is-simple it is \( \{0\} \) or \( M_n(F) \). If \( \ker\varphi = M_n(F) \), then \( 1_B = \varphi(\I_n) = 0 \), and then \( b = 1_Bb = 0 \) for every \( b \in B \), contradicting \( B \ne \{0\} \). So \( \ker\varphi = \{0\} \) and \( \varphi \) is injective (@thm-injective-iff-trivial-kernel).
:::

::: {.warning}
"Simple" says nothing about one-sided ideals. \( M_n(F) \) has no two-sided ideals other than the two obvious ones, and for \( n \ge 2 \) it has a whole lattice of left ideals, as the next result shows. Whenever a statement in this chapter says "ideal", check which kind is meant before using it.
:::

## The left ideals of the matrix algebra

The left ideals are not trivial, and they are worth knowing exactly: they are indexed by subspaces of row vectors, and the smallest of them are the column ideals.

::: {#prp-left-ideals-of-matrix-algebra}
[The Left Ideals of \( M_n(F) \)]

Let \( F \) be a field and \( n \ge 1 \). For a subspace \( W \subseteq M_{1\times n}(F) \) of row vectors, put
\[
L_W \coloneqq \{ \X \in M_n(F) : \row(\X) \subseteq W \} .
\]

::: {.enumerate options="label=(\alph*)"}
1. \( L_W \) is a left ideal of \( M_n(F) \), and \( \dim L_W = n\dim W \).
2. Every left ideal \( L \) of \( M_n(F) \) equals \( L_W \) for exactly one \( W \), namely the span of the union of the row spaces of the elements of \( L \):
   \[
   W = \Span\Bigl(\bigcup_{\X \in L}\row(\X)\Bigr) .
   \]
3. \( W \mapsto L_W \) is an inclusion-preserving bijection from subspaces of \( M_{1\times n}(F) \) onto left ideals of \( M_n(F) \). The minimal non-zero left ideals are the \( L_W \) with \( \dim W = 1 \).
4. Taking \( W = \Span(\e_j\tp) \) gives the column ideal \( C_j \) of @exm-first-ideals (c), of dimension \( n \), and \( M_n(F) = C_1 \oplus \dots \oplus C_n \) as a direct sum of left ideals.
:::
:::

::: {.idea}
Two facts drive everything. First, left multiplication can only shrink the row space: row \( i \) of \( \A\X \) is a combination of the rows of \( \X \). Second, left multiplication can produce **every** matrix whose rows lie in the row space of \( \X \), because the rows of \( \A\X \) are arbitrary combinations of the rows of \( \X \), one combination per row and chosen independently. So a left ideal is determined by the row vectors it can reach, and it contains every matrix built from them.
:::

::: {.proof}
Throughout we use two consequences of @thm-three-views-of-product (3): row \( i \) of \( \A\X \) is (row \( i \) of \( \A \)) \( \X \); and for a row vector \( \a\tp \in M_{1\times n}(F) \), the product \( \a\tp\X \) is the combination of the rows of \( \X \) with weights \( a_1, \dots, a_n \), so that
\[
\row(\X) = \{\,\a\tp\X \;:\; \a\tp \in M_{1\times n}(F)\,\} . \tag{$\ast$}
\]

(a) \( L_W \) is a subspace: every row of \( \X + c\Y \) is the corresponding row of \( \X \) plus \( c \) times that of \( \Y \), hence lies in \( W \) when both do. It is a left ideal: each row of \( \A\X \) lies in \( \row(\X) \subseteq W \) by the first consequence. For the dimension, the map \( M_n(F) \to \bigl(M_{1\times n}(F)\bigr)^n \) sending \( \X \) to its list of rows is a linear bijection, and it carries \( L_W \) onto \( W \times \dots \times W \) — the rows may be chosen from \( W \) independently of one another. So \( \dim L_W = n\dim W \) by @thm-dimension-of-product.

(b) Let \( L \) be a left ideal and put \( W \coloneqq \Span\bigl(\bigcup_{\X \in L}\row(\X)\bigr) \), a subspace of \( M_{1\times n}(F) \) by @thm-span-subspace; then \( L \subseteq L_W \) by construction.

For the reverse inclusion, choose \( \X_1, \dots, \X_m \in L \) with \( W = \row(\X_1) + \dots + \row(\X_m) \). Such a choice exists: \( W \) is a subspace of the \( n \)-dimensional space \( M_{1\times n}(F) \), so it has a finite basis; each basis vector is by @def-span a finite combination of row vectors drawn from the spaces \( \row(\X) \) with \( \X \in L \), and each such space is a subspace, so that basis vector lies in the sum of the finitely many \( \row(\X) \) involved. Collecting the \( \X \) used across the whole basis gives \( \X_1, \dots, \X_m \in L \) with \( W \subseteq \row(\X_1) + \dots + \row(\X_m) \), and the reverse containment holds because each \( \row(\X_t) \subseteq W \). Let \( \Y \in L_W \) and let \( \y_1\tp, \dots, \y_n\tp \) be its rows, all in \( W \). Each \( \y_p\tp \) lies in \( W = \row(\X_1) + \dots + \row(\X_m) \), hence is a sum of elements of the \( \row(\X_t) \), so by \( (\ast) \) there are row vectors \( \a_{pt}\tp \) with
\[
\y_p\tp = \sum_{t=1}^{m} \a_{pt}\tp\,\X_t \qquad (1 \le p \le n) .
\]
Let \( \A_t \in M_n(F) \) be the matrix whose \( p \)-th row is \( \a_{pt}\tp \). Then row \( p \) of \( \sum_t \A_t\X_t \) is \( \sum_t \a_{pt}\tp\X_t = \y_p\tp \), so \( \Y = \sum_t\A_t\X_t \). Each \( \A_t\X_t \) lies in \( L \) because \( L \) is a left ideal, and \( L \) is a subspace, so \( \Y \in L \). Hence \( L = L_W \).

Uniqueness: \( L_W \) determines \( W \), because \( W = \Span\bigl(\bigcup_{\X \in L_W}\row(\X)\bigr) \). Indeed that span is contained in \( W \) by definition, and it contains every \( \a\tp \in W \), since the matrix \( \e_1\a\tp \), whose first row is \( \a\tp \) and whose other rows are zero, lies in \( L_W \).

(c) If \( W \subseteq W' \) then \( L_W \subseteq L_{W'} \); conversely \( L_W \subseteq L_{W'} \) forces \( W \subseteq W' \), by the description of \( W \) just given. With (b), the map is a bijection, and it preserves and reflects inclusion, so it matches minimal non-zero left ideals with minimal non-zero subspaces, which are the lines.

(d) A matrix has all its rows in \( \Span(\e_j\tp) \) exactly when every entry outside column \( j \) is zero, which is the description of \( C_j \); its dimension is \( n\cdot 1 = n \) by (a). Every \( \X \) is the sum of its columns placed in the corresponding \( C_j \), and a matrix lying in \( C_j \) and in the sum of the others is zero, so the sum is direct. This proves the proposition.
:::

::: {.remark}
Everything transposes. Since \( (\X\A)\tp = \A\tp\X\tp \), the linear bijection \( \X \mapsto \X\tp \) carries left ideals onto right ideals and back. Applying it to the proposition, and writing \( U = \{\a \in F^n : \a\tp \in W\} \), the right ideals of \( M_n(F) \) are exactly the sets \( R_U = \{\X : \col(\X) \subseteq U\} \) of @exm-first-ideals (d), for subspaces \( U \subseteq F^n \), with \( \dim R_U = n\dim U \). It is worth keeping the two statements apart: column spaces classify **right** ideals, row spaces classify **left** ideals.
:::

## Quotients, and the first isomorphism theorem

Chapter 14 §10 did the work. @lem-quotient-algebra says that the quotient **space** \( A/\cI \) of Chapter 3 (@def-quotient-space) carries exactly one multiplication making \( \pi \colon A \to A/\cI \) multiplicative, namely \( (x + \cI)(y + \cI) = xy + \cI \), and that with it \( A/\cI \) is an algebra with identity \( 1_A + \cI \). We give the object its name.

::: {#def-quotient-algebra}
[Quotient Algebra]

Let \( A \) be an algebra over \( F \) and \( \cI \) a **two-sided** ideal of \( A \). The **quotient algebra** \( A/\cI \) is the quotient vector space \( A/\cI \) with the multiplication \( (x + \cI)(y + \cI) = xy + \cI \) of @lem-quotient-algebra, and \( \pi \colon A \to A/\cI \), \( \pi(x) = x + \cI \), is the **quotient homomorphism**.
:::

Two facts come for free. The ideal must be two-sided: a *merely* one-sided ideal gives a quotient vector space, but the product of cosets is not well defined on it. And when \( A \) is finite-dimensional, \( \dim(A/\cI) = \dim A - \dim\cI \) by @thm-dimension-quotient.

::: {#thm-algebra-first-isomorphism}
[First Isomorphism Theorem for Algebras]

Let \( \varphi \colon A \to B \) be a homomorphism of \( F \)-algebras. Then \( \ker\varphi \) is a two-sided ideal of \( A \), \( \im\varphi \) is a subalgebra of \( B \), and the rule
\[
\bar\varphi \colon A/\ker\varphi \to B, \qquad \bar\varphi(x + \ker\varphi) = \varphi(x),
\]
defines an injective algebra homomorphism with image \( \im\varphi \). Hence
\[
A/\ker\varphi \cong \im\varphi
\]
as \( F \)-algebras.
:::

::: {.idea}
Chapter 3 already produced the linear isomorphism; all that is left is to see that it respects products, and that is one line, because the product on the quotient was **defined** so that \( \pi \) is multiplicative.
:::

::: {.proof}
\( \ker\varphi \) is a two-sided ideal by @lem-quotient-algebra (c). \( \im\varphi \) is a subalgebra of \( B \): it is a subspace (@thm-prop-image), it is closed under products since \( \varphi(x)\varphi(y) = \varphi(xy) \), and it contains \( 1_B = \varphi(1_A) \).

Write \( K = \ker\varphi \). By @thm-first-isomorphism, \( \bar\varphi \) is a well-defined **linear** map, it is injective, its image is \( \im\varphi \), and \( \bar\varphi\circ\pi = \varphi \).

It is multiplicative. Every element of \( A/K \) is \( \pi(x) \) for some \( x \in A \), and by @def-quotient-algebra and the multiplicativity of \( \varphi \),
\[
\bar\varphi\bigl(\pi(x)\pi(y)\bigr) = \bar\varphi\bigl(\pi(xy)\bigr) = \varphi(xy) = \varphi(x)\varphi(y)
= \bar\varphi(\pi(x))\,\bar\varphi(\pi(y)) .
\]
It is unital: \( \bar\varphi(1_{A/K}) = \bar\varphi(\pi(1_A)) = \varphi(1_A) = 1_B \). So \( \bar\varphi \) is an injective algebra homomorphism onto \( \im\varphi \), hence an algebra isomorphism \( A/K \to \im\varphi \). This proves the theorem.
:::

The theorem turns every surjective homomorphism into a quotient, and that is how quotient algebras are recognized in practice: build a homomorphism, compute its kernel, and read off the answer. Here are two instances.

::: {#exm-cyclic-group-algebra-quotient}
[The group algebra of a cyclic group]

Let \( F \) be a field, \( n \ge 1 \), and \( G = \nZ/n\nZ \) written multiplicatively as \( \{1, g, \dots, g^{n-1}\} \) with \( g^n = 1 \). Show that
\[
F[G] \cong F[x]/\langle x^n - 1\rangle .
\]
:::

::: {.solution}
@exm-group-algebras (b) produced an algebra homomorphism \( \varepsilon \colon F[x] \to F[G] \) with \( \varepsilon(p) = \sum_i c_ig^i \) for \( p = \sum_i c_ix^i \), showed that it is surjective, and identified \( \ker\varepsilon = \langle x^n - 1\rangle \). Note that \( \langle x^n-1\rangle \) is a two-sided ideal of \( F[x] \), since \( F[x] \) is commutative. By @thm-algebra-first-isomorphism,
\[
F[x]/\langle x^n - 1\rangle \cong \im\varepsilon = F[G] .
\]
Both sides have dimension \( n \): the left by @thm-dimension-polynomial-quotient, the right by @def-group-algebra. This pays off the promise made in Section 1, and it says something the group alone does not: the group algebra of a cyclic group is a ring of polynomials with one relation.
:::

The second instance needs a two-element algebra built from \( F \). For \( F \)-algebras \( A \) and \( B \), the **product algebra** \( A \times B \) is the product vector space (@def-product-of-spaces) with componentwise multiplication \( (a, b)(a', b') = (aa', bb') \). Bilinearity, associativity and the identity \( (1_A, 1_B) \) are inherited componentwise, so \( A \times B \) is an algebra, of dimension \( \dim A + \dim B \) (@thm-dimension-of-product). We need only \( F \times F \), of dimension \( 2 \).

::: {#exm-triangular-quotient}
[Upper triangular matrices modulo their strictly upper part]

Let \( \cT_2 \) be the upper triangular matrices in \( M_2(F) \) and let
\( \cN = \Span(\E_{12}) \) be the strictly upper triangular ones.

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \cN \) is a two-sided ideal of \( \cT_2 \).
2. Identify \( \cT_2/\cN \).
:::
:::

::: {.solution}
Write a general element of \( \cT_2 \) as \( \U = \begin{psmallmatrix} a & b \\ 0 & c\end{psmallmatrix} \) and note
\[
\begin{pmatrix} a & b \\ 0 & c\end{pmatrix}\begin{pmatrix} p & q \\ 0 & r\end{pmatrix}
= \begin{pmatrix} ap & aq + br \\ 0 & cr \end{pmatrix} . \tag{$\dagger$}
\]

(a) \( \cN \) is the set of elements of \( \cT_2 \) with \( a = c = 0 \), a subspace. Putting \( a = c = 0 \) in \( (\dagger) \) gives a product with both diagonal entries \( 0 \), and putting \( p = r = 0 \) does the same; so \( \cN \) absorbs multiplication on both sides.

(b) Define \( \varphi \colon \cT_2 \to F \times F \) by \( \varphi(\U) = (a, c) \). It is linear, it sends \( \I_2 \) to \( (1,1) \), and by \( (\dagger) \) it is multiplicative, since the diagonal of a product of upper triangular matrices is the product of the diagonals. It is surjective, since \( \varphi(\diag(a,c)) = (a,c) \), and its kernel is exactly \( \cN \). By @thm-algebra-first-isomorphism,
\[
\cT_2/\cN \cong F \times F .
\]
A dimension check: \( \dim\cT_2 = 3 \), \( \dim\cN = 1 \), \( \dim(F\times F) = 2 = 3 - 1 \), as @thm-dimension-quotient requires.
:::

So \( \cT_2 \) is **not** simple: it has a proper non-zero two-sided ideal, and dividing by it leaves the most transparent algebra there is, a product of copies of \( F \). @thm-matrix-algebra-is-simple says \( M_2(F) \) admits no such surgery. That contrast — an algebra with an ideal to divide out, against one with none — is the division the rest of the chapter runs on.

## Exercises

### A. Check your understanding

::: {#exr-ideals-and-quotients-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define left ideal, right ideal and two-sided ideal, and say which of the three is needed to form a quotient algebra.
2. State the product rule for matrix units, and say which step of the proof of @thm-matrix-algebra-is-simple uses that \( F \) is a field.
3. True or false, with a reason: a two-sided ideal of an algebra \( A \) is a subalgebra of \( A \).
4. Give a left ideal of \( M_3(F) \) of dimension \( 6 \), and say which subspace of row vectors it corresponds to.
:::
:::

::: {.solution}
(a) See @def-left-ideal: a subspace absorbing multiplication from the left, from the right, or from both. Forming a quotient algebra needs a **two-sided** ideal, because the product of cosets is otherwise not well defined (@lem-quotient-algebra (a)).

(b) \( \E_{ij}\E_{kl} = \delta_{jk}\E_{il} \), and \( \E_{ij}\X\E_{kl} = x_{jk}\E_{il} \) (@lem-matrix-units). The field is used when dividing by the non-zero scalar \( x_{jk} \) to extract \( \E_{il} \) from \( x_{jk}\E_{il} \).

(c) False, unless \( \cI = A \). A proper ideal contains no invertible element, in particular not \( 1_A \), so (SA3) fails; see the warning after @exm-first-ideals.

(d) \( L_W \) with \( W = \Span(\e_1\tp, \e_2\tp) \), the matrices whose third column is zero; \( \dim L_W = 3\cdot 2 = 6 \) by @prp-left-ideals-of-matrix-algebra (a).
:::

### B. Practice

::: {#exr-ideals-and-quotients-b1}
[B1: Determine which are ideals]

Determine, for each of the following subspaces, whether it is a left ideal, a right ideal, a two-sided ideal, or none. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \{\X \in M_2(F) : x_{11} + x_{22} = 0\} \).
2. \( \{\X \in M_2(F) : \text{row } 2 \text{ of } \X \text{ is } \0\} \).
3. \( \{\X \in M_3(F) : \X\e_1 = \0\} \).
4. \( \{p \in F[x] : p(0) = 0\} \) inside \( F[x] \).
:::
:::

::: {.solution}
(a) None. It is a subspace, but \( \E_{12} \) lies in it while \( \E_{21}\E_{12} = \E_{22} \) does not, so it is not a left ideal; and \( \E_{12}\E_{21} = \E_{11} \) is not in it, so it is not a right ideal. (One may also argue from @thm-matrix-algebra-is-simple: a two-sided ideal of dimension \( 3 \) is impossible.)

(b) A **right** ideal, not a left ideal. The set is a subspace, and right multiplication keeps the condition: by @thm-three-views-of-product (3), row \( 2 \) of \( \X\A \) is (row \( 2 \) of \( \X \)) \( \A = \0 \). Left multiplication does not: \( \E_{11} \) has second row \( \0 \), while \( \E_{21}\E_{11} = \E_{21} \) does not.

(c) A **left** ideal, not a right ideal. It is \( L_W \) for \( W = \Span(\e_2\tp, \e_3\tp) \): a matrix kills \( \e_1 \) exactly when its first column is zero, that is, when every row lies in \( W \). Left multiplication keeps the condition since \( (\A\X)\e_1 = \A(\X\e_1) = \0 \). Right multiplication does not: \( \E_{12}\e_1 = \0 \), while \( (\E_{12}\E_{21})\e_1 = \E_{11}\e_1 = \e_1 \ne \0 \).

(d) A two-sided ideal, since \( F[x] \) is commutative: it is \( \langle x\rangle \) by @thm-remainder-theorem, and \( (hp)(0) = h(0)p(0) = 0 \).
:::

::: {#exr-ideals-and-quotients-b2}
[B2: A quotient computed]

Let \( A = F[x]/\langle x^2\rangle \).

::: {.enumerate options="label=(\alph*)"}
1. Write down a basis of \( A \) and its multiplication table.
2. Show that \( \cI = \Span(x + \langle x^2\rangle) \) is a two-sided ideal of \( A \) and identify \( A/\cI \).
3. Show that \( A \) is not isomorphic to \( F \times F \).
:::
:::

::: {.solution}
(a) By @thm-dimension-polynomial-quotient, \( \dim A = 2 \), with basis \( (1 + \langle x^2\rangle,\ x + \langle x^2\rangle) \). Write \( 1 \) and \( t \) for these. The table is \( 1\cdot 1 = 1 \), \( 1\cdot t = t\cdot 1 = t \), and \( t^2 = x^2 + \langle x^2\rangle = 0 \).

(b) \( \cI = \Span(t) \) is a subspace, and \( (a + bt)t = at \in \cI \), \( t(a + bt) = at \in \cI \), so it absorbs on both sides. The map \( \varphi \colon A \to F \), \( a + bt \mapsto a \), is linear, sends \( 1 \) to \( 1 \), and is multiplicative because \( (a + bt)(a' + b't) = aa' + (ab' + a'b)t \). Its kernel is \( \cI \), so \( A/\cI \cong F \) by @thm-algebra-first-isomorphism.

(c) In \( F \times F \) the equation \( y^2 = 0 \) forces \( y = 0 \), since a product of scalars vanishes only when a factor does. In \( A \) the non-zero element \( t \) satisfies \( t^2 = 0 \). An algebra isomorphism preserves squares and sends \( 0 \) to \( 0 \), so no isomorphism exists.
:::

::: {#exr-ideals-and-quotients-b3}
[B3: An ideal generated]

Inside \( M_3(F) \), let \( \cI = \langle \E_{23}\rangle \) be the two-sided ideal generated by \( \E_{23} \) in the sense of @def-two-sided-ideal. Compute \( \cI \), and do the same for the **left** ideal generated by \( \E_{23} \), that is, \( \Span\{\A\E_{23} : \A \in M_3(F)\} \).
:::

::: {.solution}
By @def-two-sided-ideal, \( \cI \) is spanned by the elements \( \A\E_{23}\B \). Taking \( \A = \E_{i2} \) and \( \B = \E_{3l} \) gives \( \E_{i2}\E_{23}\E_{3l} = \E_{il} \) by @lem-matrix-units, for all \( i \) and \( l \). So \( \cI \) contains every matrix unit and \( \cI = M_3(F) \), of dimension \( 9 \). This is @thm-matrix-algebra-is-simple in a single instance.

The left ideal is different. By \( (\ast) \) in the proof of @prp-left-ideals-of-matrix-algebra, \( \row(\E_{23}) = \Span(\e_3\tp) \), so \( \{\A\E_{23}\} \) is exactly the set of matrices all of whose rows are multiples of \( \e_3\tp \), that is, the column ideal \( C_3 \), of dimension \( 3 \). Generating on one side and on two sides give a three-dimensional and a nine-dimensional answer.
:::

### C. Going deeper

::: {#exr-ideals-and-quotients-c1}
[C1: All the ideals of the upper triangular algebra]

Let \( \cT_2 \) be the upper triangular matrices in \( M_2(F) \), with basis \( (\E_{11}, \E_{12}, \E_{22}) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \cJ_1 = \Span(\E_{11}, \E_{12}) \) and \( \cJ_2 = \Span(\E_{12}, \E_{22}) \) are two-sided ideals.
2. Prove that \( \{0\} \), \( \Span(\E_{12}) \), \( \cJ_1 \), \( \cJ_2 \) and \( \cT_2 \) are the **only** two-sided ideals of \( \cT_2 \).
3. Identify \( \cT_2/\cJ_1 \) and \( \cT_2/\cJ_2 \).
:::

*Hint for (b): if an ideal contains an element with \( a \ne 0 \), multiply it by \( \E_{11} \) on both sides.*
:::

::: {.solution}
Throughout write \( \U = \begin{psmallmatrix} a & b \\ 0 & c\end{psmallmatrix} \) and use \( (\dagger) \) of @exm-triangular-quotient.

(a) \( \cJ_1 \) is the set of \( \U \) with \( c = 0 \). Putting \( c = 0 \) in \( (\dagger) \) gives a product with lower right entry \( cr = 0 \); putting \( r = 0 \) does the same. So \( \cJ_1 \) absorbs on both sides. Symmetrically, \( \cJ_2 \) is the set with \( a = 0 \), and \( (\dagger) \) gives upper left entry \( ap \), which vanishes if \( a = 0 \) or \( p = 0 \).

(b) Let \( \cI \) be a two-sided ideal and take \( \U \in \cI \). By \( (\dagger) \), \( \E_{11}\U\E_{11} = a\E_{11} \) and \( \E_{22}\U\E_{22} = c\E_{22} \), both in \( \cI \). Also \( \E_{11}\U\E_{22} = b\E_{12} \in \cI \).

*Case 1: some element of \( \cI \) has \( a \ne 0 \).* Then \( \E_{11} \in \cI \), hence \( \E_{12} = \E_{11}\E_{12} \in \cI \), so \( \cJ_1 \subseteq \cI \). If in addition some element has \( c \ne 0 \), then \( \E_{22} \in \cI \) and \( \cI = \cT_2 \); otherwise every element has \( c = 0 \) and \( \cI = \cJ_1 \).

*Case 2: every element of \( \cI \) has \( a = 0 \).* If some element has \( c \ne 0 \), then \( \E_{22} \in \cI \), hence \( \E_{12} = \E_{12}\E_{22} \in \cI \), so \( \cJ_2 \subseteq \cI \subseteq \cJ_2 \) and \( \cI = \cJ_2 \). Otherwise every element has \( a = c = 0 \), so \( \cI \subseteq \Span(\E_{12}) \), and \( \cI \) is \( \{0\} \) or \( \Span(\E_{12}) \).

These five exhaust the possibilities.

(c) \( \U \mapsto c \) is a surjective algebra homomorphism \( \cT_2 \to F \) by \( (\dagger) \), with kernel \( \cJ_1 \); so \( \cT_2/\cJ_1 \cong F \) by @thm-algebra-first-isomorphism. Symmetrically \( \U \mapsto a \) gives \( \cT_2/\cJ_2 \cong F \).
:::

::: {#exr-ideals-and-quotients-c2}
[C2: Simplicity over a small field, and a failure]

::: {.enumerate options="label=(\alph*)"}
1. Verify @thm-matrix-algebra-is-simple by hand for \( M_2(\nF_2) \), starting from the ideal generated by \( \E_{12} + \E_{21} \).
2. Let \( A = F \times F \). Show that \( A \) has exactly four two-sided ideals, and conclude that a commutative algebra of dimension \( 2 \) can fail to be simple.
3. Deduce that \( M_2(F) \) and \( F^4 = F \times F \times F \times F \) are not isomorphic as \( F \)-algebras, although they have the same dimension.
:::
:::

::: {.solution}
(a) Let \( \X = \E_{12} + \E_{21} \) and let \( \cI \) be the two-sided ideal it generates. Its \( (1,2) \) entry is \( 1 \ne 0 \), so by @lem-matrix-units, \( \E_{i1}\X\E_{2l} = x_{12}\E_{il} = \E_{il} \) for all \( i, l \in \{1,2\} \). Hence \( \cI \) contains \( \E_{11}, \E_{12}, \E_{21}, \E_{22} \) and so all of \( M_2(\nF_2) \). Over \( \nF_2 \) no division was needed, because the non-zero entry was already \( 1 \).

(b) Let \( \cI \subseteq F \times F \) be an ideal and put \( e_1 = (1,0) \), \( e_2 = (0,1) \). For \( (u, v) \in \cI \) we get \( (u,0) = e_1(u,v) \in \cI \) and \( (0,v) \in \cI \). So \( \cI \) is determined by whether it contains a pair with \( u \ne 0 \) and whether it contains a pair with \( v \ne 0 \), giving \( \{0\} \), \( F\times\{0\} \), \( \{0\}\times F \) and \( F \times F \). Each of these four is indeed an ideal, by componentwise multiplication. The two middle ones are proper and non-zero, so \( F \times F \) is not simple.

(c) \( M_2(F) \) has exactly two two-sided ideals (@thm-matrix-algebra-is-simple), while \( F^4 \) has more: the same argument as in (b) shows that \( F\times\{0\}\times\{0\}\times\{0\} \) is a proper non-zero ideal. An algebra isomorphism carries two-sided ideals bijectively to two-sided ideals, so no isomorphism can exist. Both algebras have dimension \( 4 \), so dimension alone classifies nothing.
:::

::: {#exr-ideals-and-quotients-c3}
[C3: Left ideals and null spaces]

Let \( F \) be a field and \( n \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. For a subspace \( U \subseteq F^n \), prove that \( N_U = \{\X \in M_n(F) : \X\u = \0 \text{ for every } \u \in U\} \) is a left ideal of \( M_n(F) \).
2. Prove that \( \dim N_U = n(n - \dim U) \).
3. Prove that \( U \mapsto N_U \) is an **inclusion-reversing** bijection from subspaces of \( F^n \) onto left ideals of \( M_n(F) \), and describe \( N_U \) in the language of @prp-left-ideals-of-matrix-algebra.
:::

*Hint for (b): a matrix kills every vector of \( U \) exactly when each of its rows annihilates \( U \).*
:::

::: {.solution}
(a) \( N_U \) is the intersection over \( \u \in U \) of the null spaces of the linear maps \( \X \mapsto \X\u \), hence a subspace. If \( \X \in N_U \) and \( \A \in M_n(F) \), then \( (\A\X)\u = \A(\X\u) = \0 \), so \( \A\X \in N_U \).

(b) Let \( \a\tp \) be a row of \( \X \). The entries of \( \X\u \) are the numbers \( \a\tp\u \) as \( \a\tp \) runs over the rows, so \( \X\u = \0 \) for every \( \u \in U \) exactly when every row of \( \X \) annihilates \( U \), that is, when \( \row(\X) \subseteq W_U \), where \( W_U \) is the space of row vectors annihilating \( U \). Identifying a row vector \( \a\tp \) with the functional \( \u \mapsto \a\tp\u \), which is a linear bijection \( M_{1\times n}(F) \to (F^n)^{*} \) by @thm-functionals-on-fn, the space \( W_U \) corresponds to \( U^{0} \), so \( \dim W_U = n - \dim U \) by @thm-dimension-annihilator. Hence \( N_U = L_{W_U} \), and @prp-left-ideals-of-matrix-algebra (a) gives \( \dim N_U = n(n - \dim U) \).

(c) It is enough to show that \( U \mapsto W_U \), which under the identification of (b) is \( U \mapsto U^{0} \), is an inclusion-reversing bijection from subspaces of \( F^n \) onto subspaces of \( M_{1\times n}(F) \); composing with the inclusion-preserving bijection \( W \mapsto L_W \) of @prp-left-ideals-of-matrix-algebra (c) then gives the claim, since \( N_U = L_{W_U} \) by (b).

It reverses inclusions by @thm-annihilator-properties (a), and it is injective by @cor-subspaces-determined-by-annihilator. For surjectivity, let \( W \) be a subspace of \( (F^n)^{*} \) of dimension \( k \), with basis \( \varphi_1, \dots, \varphi_k \), and put \( U = \ker\varphi_1 \cap \dots \cap \ker\varphi_k \). By @thm-independent-functionals-surjective, \( U \) has codimension \( k \), so \( \dim U = n - k \) and \( \dim U^{0} = k \) by @thm-dimension-annihilator. Every \( \varphi_i \) vanishes on \( U \), so \( W \subseteq U^{0} \); equal dimensions give \( W = U^{0} \).
:::
