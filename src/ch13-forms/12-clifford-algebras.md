# A First Look at Clifford Algebras

The chapter ends with a construction rather than a classification. Everything so far has taken a quadratic form apart; this section asks instead for an algebra in which the form becomes a *square*, so that \( q(\v) \) is literally \( \v \) times \( \v \) for a multiplication we invent. The answer is a Clifford algebra, and two of the most familiar algebras in mathematics are its first two examples. This is an introduction only: we define the object, prove what the definition alone gives, work three cases out completely, and stop.

## Making a form into a square

Take \( V = \nR^2 \) with the negative definite form \( q(\x) = -(x_1^2 + x_2^2) \), and suppose we had an associative multiplication on some larger space containing \( V \), with an identity \( 1 \), in which every vector satisfies \( \v^2 = q(\v)\cdot 1 \). Write \( \epsilon_1, \epsilon_2 \) for the two standard basis vectors sitting inside that algebra. Expanding \( \v = x_1\epsilon_1 + x_2\epsilon_2 \) and using only bilinearity of the product,
\[
\v^2 = x_1^2\epsilon_1^2 + x_1x_2(\epsilon_1\epsilon_2 + \epsilon_2\epsilon_1) + x_2^2\epsilon_2^2 .
\]
We want this to equal \( -(x_1^2 + x_2^2)\cdot 1 \) for **every** \( x_1, x_2 \). Taking \( x_2 = 0 \) forces \( \epsilon_1^2 = -1 \), and taking \( x_1 = 0 \) forces \( \epsilon_2^2 = -1 \). What is left is \( x_1x_2(\epsilon_1\epsilon_2 + \epsilon_2\epsilon_1) = 0 \) for all \( x_1, x_2 \), which forces
\[
\epsilon_1\epsilon_2 = -\epsilon_2\epsilon_1 .
\]
So the two basis vectors must square to \( -1 \) and must **anticommute**. That last relation hands us a third square root of \( -1 \) we did not ask for, since \( (\epsilon_1\epsilon_2)^2 = \epsilon_1\epsilon_2\epsilon_1\epsilon_2 = -\epsilon_1^2\epsilon_2^2 = -1 \). Three anticommuting square roots of \( -1 \): those are Hamilton's quaternions. Run the same argument on a one-dimensional \( V \) with \( q(x) = -x^2 \) and the single relation \( \epsilon_1^2 = -1 \) produces \( \nC \).

*A Clifford algebra is the smallest place where the vectors of \( V \) can be multiplied and each one squares to its own \( q \)-value.*

## Algebras

The objects above are algebras, a word the book has used informally and now needs precisely.

::: {#def-algebra-over-field}
[Algebra over a Field]

An **algebra over \( F \)**, or an **\( F \)-algebra**, is a vector space \( A \) over \( F \) together with a map \( A \times A \to A \), written \( (x, y) \mapsto xy \), which is

::: {.enumerate options="label=(A\arabic*)"}
1. **bilinear**: linear in each argument with the other fixed;
2. **associative**: \( (xy)z = x(yz) \) for all \( x, y, z \in A \);
3. **unital**: there is an element \( 1_A \in A \) with \( 1_Ax = x1_A = x \) for every \( x \in A \).
:::

A **homomorphism of \( F \)-algebras** is an \( F \)-linear map \( \varphi \colon A \to B \) with \( \varphi(xy) = \varphi(x)\varphi(y) \) for all \( x, y \) and \( \varphi(1_A) = 1_B \). An **isomorphism** is a bijective homomorphism.
:::

Every algebra here is associative and unital, and we stop saying so. The examples are old friends: \( F \) itself; \( M_n(F) \); \( F[x] \); \( \cL(V) \) under composition; and \( \nC \) over \( \nR \), of dimension \( 2 \). A non-example by minimal change: \( \nR^3 \) with the cross product is bilinear but fails (A2) and (A3), since \( (\e_1 \times \e_1) \times \e_2 = \0 \) while \( \e_1 \times (\e_1 \times \e_2) = -\e_2 \), and no vector acts as an identity.

One consequence of (A1) is used constantly below: a bilinear map is determined by its values on a basis, so two products agree, and a linear map is multiplicative, as soon as this is checked on basis elements.

## The definition

::: {#def-clifford-algebra}
[Clifford Algebra]

Let \( F \) be a field with \( \operatorname{char} F \ne 2 \), let \( V \) be a finite-dimensional \( F \)-vector space, let \( \beta \) be a symmetric bilinear form on \( V \) and let \( q(\v) = \beta(\v, \v) \) be its quadratic form (@def-quadratic-form). A **Clifford algebra** of \( (V, q) \) is a pair \( (C, \iota) \), where \( C \) is an \( F \)-algebra and \( \iota \colon V \to C \) is a linear map, such that

::: {.enumerate options="label=(C\arabic*)"}
1. \( \iota(\v)^2 = q(\v)1_C \) for **every** \( \v \in V \);
2. (**universal property**) for every \( F \)-algebra \( A \) and every linear map \( f \colon V \to A \) with \( f(\v)^2 = q(\v)1_A \) for every \( \v \in V \), there is a **unique** algebra homomorphism \( \bar f \colon C \to A \) with \( \bar f \circ \iota = f \).
:::

We write \( \operatorname{Cl}(q) \), or \( \operatorname{Cl}(V, q) \), for a Clifford algebra of \( (V, q) \), and \( \operatorname{Cl}_{p,m}(\nR) \) when \( V \) is the space \( \nR^{p,m} \) of @def-minkowski-space, that is, \( \nR^{p+m} \) with the real form of signature \( (p, m) \).
:::

Clause by clause. (C1) is the demand we started from: inside \( C \) every vector has a square, and that square is a *number* times the identity, not a vector. (C2) says \( C \) is the most economical algebra with that property. Any other algebra where the vectors square correctly receives a map from \( C \), so \( C \) has no relations beyond those (C1) forces; and the map is unique, so \( C \) has no room to spare either. What is defined is the pair \( (C, \iota) \), not \( C \) alone.

::: {.remark}
The subscripts in \( \operatorname{Cl}_{p,m}(\nR) \) are usually written \( p, q \), but \( q \) already names the quadratic form here, so the second index is \( m \).
:::

**Existence is deferred.** The definition says what a Clifford algebra would be; it does not produce one. The standard construction is not available yet: one takes the **tensor algebra** of \( V \) — the infinite-dimensional algebra whose elements are formal sums of strings of vectors, multiplied by concatenation — and divides out by the relations \( \v \otimes \v - q(\v)1 \). Chapter 14 builds tensor algebras and carries this out, for every \( V \) and \( q \) at once. So everything below is of one of two kinds: a consequence of the definition, valid whenever a Clifford algebra exists, or an explicit algebra written down by hand, which proves existence in that case. We say which each time.

The first consequence is that "the" Clifford algebra is legitimate language.

::: {#prp-clifford-uniqueness}
[Uniqueness of the Clifford Algebra]

Let \( (C, \iota) \) and \( (C', \iota') \) both be Clifford algebras of \( (V, q) \). Then there is a unique algebra isomorphism \( \varphi \colon C \to C' \) with \( \varphi \circ \iota = \iota' \).
:::

::: {.idea}
Each one's universal property produces a map to the other. The two composites are self-maps that do nothing to \( \iota \), and the uniqueness clause says the only such self-map is the identity.
:::

::: {.proof}
Since \( (C', \iota') \) satisfies (C1), the universal property (C2) of \( C \), applied with \( A = C' \) and \( f = \iota' \), gives an algebra homomorphism \( \varphi \colon C \to C' \) with \( \varphi\iota = \iota' \). Symmetrically, (C2) for \( C' \) gives \( \psi \colon C' \to C \) with \( \psi\iota' = \iota \). Then \( \psi\varphi \colon C \to C \) is an algebra homomorphism with \( \psi\varphi\iota = \psi\iota' = \iota \). The identity \( \id_C \) is another one. By the uniqueness clause of (C2) for \( C \), applied with \( A = C \) and \( f = \iota \), the two coincide: \( \psi\varphi = \id_C \). Swapping the roles of \( C \) and \( C' \) gives \( \varphi\psi = \id_{C'} \). Hence \( \varphi \) is an isomorphism, and it is unique because (C2) already delivers it uniquely. This proves the proposition.
:::

Next, the identity that does all the computing.

::: {#lem-clifford-anticommutation}
[The Anticommutation Relation]

Let \( (C, \iota) \) be a Clifford algebra of \( (V, q) \). Then for all \( \u, \v \in V \),
\[
\iota(\u)\iota(\v) + \iota(\v)\iota(\u) = 2\beta(\u, \v)1_C .
\]
In particular \( \iota(\u) \) and \( \iota(\v) \) anticommute whenever \( \beta(\u, \v) = 0 \).
:::

::: {.proof}
By (C1) applied to \( \u + \v \), and then bilinearity of the product together with linearity of \( \iota \),
\[
q(\u + \v)1_C = \iota(\u + \v)^2
= \iota(\u)^2 + \iota(\u)\iota(\v) + \iota(\v)\iota(\u) + \iota(\v)^2 .
\]
By @thm-polarization-forms, \( q(\u+\v) = q(\u) + 2\beta(\u,\v) + q(\v) \), and by (C1) again \( \iota(\u)^2 = q(\u)1_C \) and \( \iota(\v)^2 = q(\v)1_C \). Canceling those two terms from both sides leaves the stated identity. The last sentence is the case \( \beta(\u,\v) = 0 \).
:::

So an **orthogonal** basis for \( \beta \) becomes a list of pairwise anticommuting elements of \( C \), each with a scalar square. That is the whole computational content of a Clifford algebra, and @thm-symmetric-form-diagonalizable guarantees such a basis exists whenever \( \operatorname{char} F \ne 2 \) — which is where the characteristic hypothesis in @def-clifford-algebra earns its place, since @thm-polarization-forms needs it too.

## Three algebras, worked out

::: {#exm-clifford-of-zero-space}
[The zero space]

Let \( V = \{\0\} \), so \( q = 0 \) and \( n = 0 \). Show that \( (F, \iota) \) with \( \iota = 0 \) is a Clifford algebra of \( (V, q) \), so that \( \operatorname{Cl}(0) = F \).
:::

::: {.solution}
(C1): the only vector is \( \0 \), and \( \iota(\0)^2 = 0 = q(\0)1_F \).

(C2): let \( A \) be an \( F \)-algebra and \( f \colon V \to A \) linear, necessarily \( f = 0 \), so the condition on \( f \) reads \( 0 = 0 \). Define \( \bar f \colon F \to A \) by \( \bar f(a) = a1_A \): it is linear, sends \( 1 \) to \( 1_A \), and is multiplicative because \( \bar f(ab) = (ab)1_A = (a1_A)(b1_A) \) by bilinearity of the product and \( 1_A1_A = 1_A \); and \( \bar f\iota = 0 = f \). It is unique, since any algebra homomorphism \( \varphi \colon F \to A \) is linear with \( \varphi(1) = 1_A \), hence \( \varphi(a) = a1_A \).

So \( \operatorname{Cl}(0) = F \), of dimension \( 1 = 2^0 \): the construction adds nothing when there is nothing to add.
:::

::: {#exm-clifford-complex-numbers}
[The complex numbers]

Let \( V = \nR \) with \( q(x) = -x^2 \), the form of signature \( (0,1) \). Show that \( \nC \), with \( \iota \colon \nR \to \nC \) given by \( \iota(x) = xi \), is a Clifford algebra of \( (V, q) \), so that \( \operatorname{Cl}_{0,1}(\nR) = \nC \).
:::

::: {.solution}
Here \( \nC \) is an algebra over \( \nR \) of dimension \( 2 \), with basis \( (1, i) \).

(C1): \( \iota(x)^2 = (xi)^2 = x^2i^2 = -x^2 = q(x)\cdot 1 \).

(C2): let \( A \) be a real algebra and \( f \colon \nR \to A \) linear with \( f(x)^2 = -x^2 1_A \). Put \( u = f(1) \), so \( f(x) = xu \) by linearity and \( u^2 = -1_A \). Define \( \bar f \colon \nC \to A \) by \( \bar f(a + bi) = a1_A + bu \), which is \( \nR \)-linear and sends \( 1 \) to \( 1_A \). To see it is multiplicative, note that \( (z, w) \mapsto \bar f(zw) \) and \( (z, w) \mapsto \bar f(z)\bar f(w) \) are both \( \nR \)-bilinear, so it suffices to compare them on the basis \( (1, i) \): the pairs involving \( 1 \) are immediate, and \( \bar f(i\cdot i) = \bar f(-1) = -1_A = u^2 = \bar f(i)\bar f(i) \). Finally \( \bar f\iota(x) = \bar f(xi) = xu = f(x) \). For uniqueness, an algebra homomorphism \( \varphi \) with \( \varphi\iota = f \) has \( \varphi(1) = 1_A \) and \( \varphi(i) = \varphi(\iota(1)) = f(1) = u \), and \( (1, i) \) spans \( \nC \), so \( \varphi = \bar f \).

So \( \operatorname{Cl}_{0,1}(\nR) = \nC \), of dimension \( 2 = 2^1 \). Read this backwards: \( \nC \) is not primarily "\( \nR \) with a square root of \( -1 \) attached", it is the smallest algebra in which the number \( x \) squares to \( -x^2 \).
:::

For the two-dimensional case we need the quaternions, and we need them to be associative. The cheapest way to get associativity is to find them inside a matrix algebra, where it is free.

::: {#def-quaternions}
[The Quaternions]

Inside \( M_2(\nC) \), regarded as an algebra over \( \nR \), put
\[
\i = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix}, \quad
\j = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}, \quad
\k = \begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix} .
\]
The **quaternions** \( \nH \) are the real span of \( \I_2, \i, \j, \k \) in \( M_2(\nC) \).
:::

The three matrices carry Hamilton's names and are written bold lowercase, as basis vectors of \( \nH \); the plain \( i \) in their entries is the complex unit, which is a different object from the matrix \( \i \). Multiplying them out gives
\[
\i^2 = \j^2 = \k^2 = -\I_2 , \qquad
\i\j = \k = -\j\i ,
\]
and then \( \j\k = \i = -\k\j \) and \( \k\i = \j = -\i\k \). A real combination \( a\I_2 + b\i + c\j + d\k \) is the matrix with rows \( (a + bi,\ c + di) \) and \( (-c + di,\ a - bi) \), which vanishes only when \( a = b = c = d = 0 \); so \( \dim_{\nR}\nH = 4 \). The relations show the span is closed under multiplication, so \( \nH \) is a real subalgebra of \( M_2(\nC) \) — and it is associative for free, because matrix multiplication is.

::: {#exm-clifford-quaternions}
[The quaternions]

Let \( V = \nR^2 \) with \( q(\x) = -(x_1^2 + x_2^2) \), the form of signature \( (0,2) \). Show that \( \nH \), with \( \iota(\x) = x_1\i + x_2\j \), is a Clifford algebra of \( (V, q) \), so that \( \operatorname{Cl}_{0,2}(\nR) = \nH \).
:::

::: {.solution}
(C1): using \( \i\j + \j\i = \0 \) and \( \i^2 = \j^2 = -\I_2 \),
\[
\iota(\x)^2 = x_1^2\i^2 + x_1x_2(\i\j + \j\i) + x_2^2\j^2
= -(x_1^2 + x_2^2)\I_2 ,
\]
which is \( q(\x)1_{\nH} \).

(C2): let \( A \) be a real algebra and \( f \colon \nR^2 \to A \) linear with \( f(\x)^2 = q(\x)1_A \). Put \( u = f(\e_1) \) and \( w = f(\e_2) \), so \( u^2 = w^2 = -1_A \), and by @lem-clifford-anticommutation — or directly, by expanding \( f(\e_1 + \e_2)^2 = -2\cdot 1_A \) — we get \( uw + wu = 0 \), that is, \( wu = -uw \). Define the linear map
\[
\bar f(a\I_2 + b\i + c\j + d\k) = a1_A + bu + cw + d\,uw ,
\]
which is well defined because \( (\I_2, \i, \j, \k) \) is a basis of \( \nH \), and sends \( 1_{\nH} = \I_2 \) to \( 1_A \). Both \( (z,z') \mapsto \bar f(zz') \) and \( (z,z') \mapsto \bar f(z)\bar f(z') \) are \( \nR \)-bilinear, so multiplicativity need only be checked on the basis. The pairs involving \( \I_2 \) are immediate, and the remaining nine are
\[
\begin{aligned}
\i\i &= -\I_2 \;\mapsto\; -1_A = u^2, &
\j\j &= -\I_2 \;\mapsto\; -1_A = w^2, \\
\i\j &= \k \;\mapsto\; uw, &
\j\i &= -\k \;\mapsto\; -uw = wu, \\
\i\k &= -\j \;\mapsto\; -w = u(uw), &
\k\i &= \j \;\mapsto\; w = (uw)u, \\
\j\k &= \i \;\mapsto\; u = w(uw), &
\k\j &= -\i \;\mapsto\; -u = (uw)w, \\
\k\k &= -\I_2 \;\mapsto\; -1_A = (uw)^2 .
\end{aligned}
\]
Each right-hand claim is one line of algebra in \( A \), using associativity, \( wu = -uw \) and \( u^2 = w^2 = -1_A \). For instance \( (uw)u = u(wu) = -u(uw) = -u^2w = w \), and \( (uw)^2 = u(wu)w = -u^2w^2 = -1_A \).

Finally \( \bar f\iota(\x) = x_1u + x_2w = f(\x) \). For uniqueness, an algebra homomorphism \( \varphi \) with \( \varphi\iota = f \) is forced on \( \I_2 \), on \( \i = \iota(\e_1) \) and on \( \j = \iota(\e_2) \), hence on \( \k = \i\j \), and these four span \( \nH \).

So \( \operatorname{Cl}_{0,2}(\nR) = \nH \), of dimension \( 4 = 2^2 \).
:::

::: {.warning}
**A Clifford algebra is not commutative, and a product of two vectors is not a vector.** In \( \operatorname{Cl}_{0,2}(\nR) = \nH \) the image \( \iota(\nR^2) = \Span(\i, \j) \) is a plane, and \( \i\j = \k \) lies outside it; worse, \( \i\j = -\j\i \), so the order matters. Two habits have to go: that multiplying two elements of \( V \) keeps you in \( V \), and that \( xy = yx \). Beyond the scalars \( F\cdot 1_C \), nothing may be assumed to commute.
:::

## How big is it

The three examples all came out with \( \dim = 2^n \). Half of that is a theorem we can prove.

::: {#prp-clifford-spanning}
[The Clifford Algebra Is Spanned by Sorted Products]

Let \( (C, \iota) \) be a Clifford algebra of \( (V, q) \), where \( \dim V = n \) and \( \operatorname{char} F \ne 2 \), and let \( (\e_1, \dots, \e_n) \) be an orthogonal basis of \( V \) for \( \beta \). Then \( C \) is spanned over \( F \) by the \( 2^n \) products
\[
\iota(\e_{i_1})\iota(\e_{i_2})\cdots\iota(\e_{i_k}),
\qquad 1 \le i_1 < i_2 < \dots < i_k \le n ,
\]
one for each subset \( \{i_1, \dots, i_k\} \) of \( \{1, \dots, n\} \), the empty product being \( 1_C \). In particular \( \dim_F C \le 2^n \).
:::

::: {.idea}
Two steps. ① Show that \( C \) is generated as an algebra by \( 1_C \) and \( \iota(V) \) — this is not automatic, and it is where the *uniqueness* half of the universal property does its work. ② Sort: any product of basis vectors can be put in increasing order by swapping neighbors at the cost of a sign (@lem-clifford-anticommutation), and a repeated neighbor collapses to a scalar (C1).
:::

::: {.proof}
An orthogonal basis exists by @thm-symmetric-form-diagonalizable, since \( \operatorname{char} F \ne 2 \). Write \( d_i = q(\e_i) \).

**Step 1: \( C \) is generated by \( 1_C \) and \( \iota(V) \).** Let \( C' \subseteq C \) be the set of all \( F \)-linear combinations of \( 1_C \) and of finite products \( \iota(\v_1)\cdots\iota(\v_m) \) with \( \v_1, \dots, \v_m \in V \). It is a subspace closed under multiplication and contains \( 1_C \), hence is itself an \( F \)-algebra, and \( \iota \) followed by the change of codomain gives a linear map \( \iota' \colon V \to C' \) satisfying (C1). By the universal property of \( C \), applied with \( A = C' \) and \( f = \iota' \), there is an algebra homomorphism \( g \colon C \to C' \) with \( g\iota = \iota' \). Let \( j \colon C' \to C \) be the inclusion, an algebra homomorphism. Then \( jg \colon C \to C \) is an algebra homomorphism with \( jg\iota = \iota \), and so is \( \id_C \); by the uniqueness clause of (C2), applied with \( A = C \) and \( f = \iota \), we get \( jg = \id_C \). Hence \( j \) is surjective, so \( C' = C \).

**Step 2: sorting.** By Step 1 and linearity of \( \iota \), \( C \) is spanned by \( 1_C \) together with the products \( \iota(\e_{j_1})\cdots\iota(\e_{j_m}) \) over all finite index strings \( (j_1, \dots, j_m) \). Fix such a product and induct on the pair \( \bigl(m, \operatorname{inv}(j_1, \dots, j_m)\bigr) \), ordered lexicographically, where \( \operatorname{inv} \) counts the pairs \( r < s \) with \( j_r > j_s \). If the string is strictly increasing, the product is on the list and we are done. Otherwise some neighboring pair has \( j_r \ge j_{r+1} \). If \( j_r = j_{r+1} \), then (C1) replaces \( \iota(\e_{j_r})^2 \) by the scalar \( d_{j_r} \), producing a scalar multiple of a product of length \( m - 2 \). If \( j_r > j_{r+1} \), then @lem-clifford-anticommutation with \( \beta(\e_{j_r}, \e_{j_{r+1}}) = 0 \) lets us swap the two factors at the cost of a sign, producing a product of the same length with one fewer inversion. Either way the induction applies, and the product is a scalar multiple of a listed one.

There are \( 2^n \) subsets of \( \{1, \dots, n\} \), so the spanning list has \( 2^n \) members and \( \dim_F C \le 2^n \). This proves the proposition.
:::

::: {.check}
Where exactly does @prp-clifford-spanning use the word **unique** in (C2), and what would go wrong without it?
:::

::: {.solution}
In Step 1, at the sentence "by the uniqueness clause of (C2) … we get \( jg = \id_C \)". Existence alone gives an algebra homomorphism \( jg \colon C \to C \) fixing \( \iota \), but nothing then makes it the identity, and the argument cannot conclude that \( j \) is surjective. The conclusion really would be false. Take \( V = \nR \) with \( q(x) = -x^2 \), let \( A = \nC \times \nC \) with componentwise multiplication, and set \( \iota(x) = (xi, xi) \). Then \( \iota(x)^2 = q(x)1_A \), so (C1) holds, and so does the existence half of (C2): the first projection, followed by the homomorphism \( \nC \to B \) built in @exm-clifford-complex-numbers, does the job for every target \( B \). But \( A \) is **not** spanned by \( 1_A \) and products of vectors, since every such product lies in the diagonal \( \{(z,z)\} \), of dimension \( 2 \). What fails is uniqueness — the second projection is a second map — and that is the clause the proof needs.
:::

The other half of the count is a different matter.

::: {#thm-clifford-dimension}
[Dimension of a Clifford Algebra]

Let \( \operatorname{char} F \ne 2 \), let \( \dim V = n \), and let \( (C, \iota) \) be a Clifford algebra of \( (V, q) \). Then the \( 2^n \) sorted products of @prp-clifford-spanning form a **basis** of \( C \), so \( \dim_F C = 2^n \). In particular \( \iota \) is injective.
:::

**What is proved here, and what is not.** The inequality \( \dim_F C \le 2^n \) is @prp-clifford-spanning, proved in full. The reverse inequality — that the \( 2^n \) sorted products are linearly independent — is **not proved in this section**, and it cannot be, because the definition alone does not even produce an algebra: independence and existence have to be established together, by constructing one algebra of dimension exactly \( 2^n \) that satisfies (C1) and (C2). Chapter 14 does that, from the tensor algebra. What this section does establish is the theorem in the three cases above: \( n = 0 \) with \( \dim = 1 \), \( n = 1 \) with \( \dim = 2 \), and the case \( q = -x_1^2 - x_2^2 \) of \( n = 2 \) with \( \dim = 4 \), each by writing the algebra down and checking (C1) and (C2) by hand. For \( n \ge 3 \), read the statement above as quoted from Chapter 14 and not as proved here.

Granting the theorem, the subsets of \( \{1, \dots, n\} \) indexing the basis are the first sign that \( \operatorname{Cl}(q) \) is assembled from the exterior powers \( \Lambda^kV \), one for each \( k \). Chapter 14 constructs both and makes that precise.

## What Clifford algebras are for

One computation shows where the subject goes. Recall from Section 10 that the isometries of \( q \) form a group (@def-isometry-group-of-form). Inside \( \operatorname{Cl}(q) \), some of them are conjugations.

::: {#prp-clifford-reflection}
[Reflections Are Conjugations]

Let \( (C, \iota) \) be a Clifford algebra of \( (V, q) \) and let \( \u \in V \) with \( q(\u) \ne 0 \). Then \( \iota(\u) \) is invertible in \( C \), with inverse \( q(\u)^{-1}\iota(\u) \), and for every \( \v \in V \),
\[
-\iota(\u)\iota(\v)\iota(\u)^{-1} = \iota\bigl(s_{\u}(\v)\bigr),
\qquad
s_{\u}(\v) \coloneqq \v - \frac{2\beta(\u,\v)}{q(\u)}\,\u .
\]
The map \( s_{\u} \) fixes \( \{\v : \beta(\u,\v) = 0\} \) pointwise, sends \( \u \) to \( -\u \), and satisfies \( q(s_{\u}(\v)) = q(\v) \).
:::

::: {.proof}
By (C1), \( \iota(\u)^2 = q(\u)1_C \) with \( q(\u) \ne 0 \), so \( \iota(\u)\bigl(q(\u)^{-1}\iota(\u)\bigr) = 1_C \) and likewise on the other side. By @lem-clifford-anticommutation, \( \iota(\u)\iota(\v) = 2\beta(\u,\v)1_C - \iota(\v)\iota(\u) \), so multiplying on the right by \( \iota(\u) \),
\[
\iota(\u)\iota(\v)\iota(\u) = 2\beta(\u,\v)\iota(\u) - q(\u)\iota(\v) .
\]
Dividing by \( q(\u) \) and negating gives \( -\iota(\u)\iota(\v)\iota(\u)^{-1} = \iota(\v) - \frac{2\beta(\u,\v)}{q(\u)}\iota(\u) \), which is \( \iota(s_{\u}(\v)) \) by linearity of \( \iota \). If \( \beta(\u,\v) = 0 \) then \( s_{\u}(\v) = \v \); and \( s_{\u}(\u) = \u - 2\u = -\u \). Finally, writing \( c = 2\beta(\u,\v)/q(\u) \),
\[
q(\v - c\u) = q(\v) - 2c\beta(\u,\v) + c^2q(\u) = q(\v),
\]
since \( c^2q(\u) = c\cdot 2\beta(\u,\v) \). This proves the proposition.
:::

So the reflection in a hyperplane, the basic isometry of a quadratic form, is carried out inside \( \operatorname{Cl}(q) \) by conjugating with a single vector. Composing such conjugations reaches more isometries, and the invertible elements of \( \operatorname{Cl}(q) \) acting on \( V \) this way form a group mapping onto the isometry group of \( q \) — two-to-one, since \( \iota(\u) \) and \( -\iota(\u) \) conjugate alike. That double covering is where **spinors** live: objects the covering group acts on and the isometry group does not, because going once around a rotation returns them with a sign. This book will not build them. What it will do is Chapter 14: construct tensor algebras, construct \( \operatorname{Cl}(q) \) from one, and prove @thm-clifford-dimension. Nothing later depends on this section, and the chapter ends here.

## Exercises

### A. Check your understanding

::: {#exr-clifford-algebras-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the definition of an \( F \)-algebra, and give one example of dimension \( 1 \) and one of dimension \( 4 \).
2. State the universal property (C2), with every quantifier.
3. What is \( \operatorname{Cl}(0) \) when \( V = \{\0\} \), and what is its dimension?
4. True or false: \( \operatorname{Cl}_{0,2}(\nR) \) is commutative. Justify your answer.
5. What does this book prove about \( \dim\operatorname{Cl}(q) \) when \( \dim V = 3 \), and what does it only quote?
:::
:::

::: {.solution}
(a) A vector space over \( F \) with a bilinear, associative, unital multiplication (@def-algebra-over-field). Dimension \( 1 \): \( F \) itself. Dimension \( 4 \): \( M_2(F) \), or \( \nH \) over \( \nR \).

(b) For every \( F \)-algebra \( A \) and every linear \( f \colon V \to A \) such that \( f(\v)^2 = q(\v)1_A \) for every \( \v \in V \), there exists a unique algebra homomorphism \( \bar f \colon C \to A \) such that \( \bar f \circ \iota = f \).

(c) \( \operatorname{Cl}(0) = F \), of dimension \( 1 = 2^0 \) (@exm-clifford-of-zero-space).

(d) False. It is \( \nH \) by @exm-clifford-quaternions, and \( \i\j = \k \ne -\k = \j\i \).

(e) It proves \( \dim\operatorname{Cl}(q) \le 2^3 = 8 \), by @prp-clifford-spanning. The equality \( \dim\operatorname{Cl}(q) = 8 \), and indeed the existence of \( \operatorname{Cl}(q) \) at all, is quoted from Chapter 14.
:::

### B. Practice

::: {#exr-clifford-algebras-b1}
[B1: The split case]

Let \( V = \nR \) with \( q(x) = x^2 \), the form of signature \( (1,0) \). Let \( A = \nR \times \nR \) with componentwise addition and multiplication, and \( \iota \colon \nR \to A \), \( \iota(x) = (x, -x) \). Prove that \( (A, \iota) \) is a Clifford algebra of \( (V, q) \), and state its dimension.
:::

::: {.solution}
\( A \) is a real algebra of dimension \( 2 \) with identity \( 1_A = (1,1) \), and \( \bigl(1_A, \iota(1)\bigr) = \bigl((1,1), (1,-1)\bigr) \) is a basis, since \( a(1,1) + b(1,-1) = (a+b, a-b) \) vanishes only for \( a = b = 0 \).

(C1): \( \iota(x)^2 = (x^2, x^2) = q(x)1_A \).

(C2): let \( B \) be a real algebra and \( f \colon \nR \to B \) linear with \( f(x)^2 = x^21_B \). Put \( u = f(1) \), so \( f(x) = xu \) and \( u^2 = 1_B \). Define \( \bar f(a, b) = \tfrac{a+b}{2}1_B + \tfrac{a-b}{2}u \), which is linear and sends \( 1_A \) to \( 1_B \) and \( \iota(1) \) to \( u \). By bilinearity, multiplicativity need only be checked on that basis: the pairs involving \( 1_A \) are immediate, and \( \iota(1)^2 = 1_A \mapsto 1_B = u^2 \). Also \( \bar f\iota(x) = xu = f(x) \), and any such homomorphism is forced on \( 1_A \) and \( \iota(1) \), which span \( A \).

So \( \operatorname{Cl}_{1,0}(\nR) = \nR \times \nR \), of dimension \( 2 = 2^1 \). Comparing with @exm-clifford-complex-numbers: the same one-dimensional \( V \) with the opposite sign of \( q \) gives \( \nC \) instead, so the Clifford algebra sees the sign of the form, not just its rank.
:::

::: {#exr-clifford-algebras-b2}
[B2]

Work in \( \operatorname{Cl}_{0,2}(\nR) = \nH \), with \( \iota(\x) = x_1\i + x_2\j \). Let \( \u = (1,2) \) and \( \v = (3,-1) \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \iota(\u)\iota(\v) \) and \( \iota(\v)\iota(\u) \), and verify @lem-clifford-anticommutation on this pair.
2. Compute \( q(\u) \), verify \( \iota(\u)^2 = q(\u)1_{\nH} \), and write down \( \iota(\u)^{-1} \).
:::
:::

::: {.solution}
(a) Using \( \i^2 = \j^2 = -1 \) and \( \i\j = \k = -\j\i \), and writing \( 1 \) for \( \I_2 \),
\[
\begin{aligned}
\iota(\u)\iota(\v) &= (\i + 2\j)(3\i - \j) = -3 - \k - 6\k + 2 = -1 - 7\k , \\
\iota(\v)\iota(\u) &= (3\i - \j)(\i + 2\j) = -3 + 6\k + \k + 2 = -1 + 7\k .
\end{aligned}
\]
Their sum is \( -2 \). On the other side, \( \beta(\u,\v) = -(1\cdot 3 + 2\cdot(-1)) = -1 \), so \( 2\beta(\u,\v)1_{\nH} = -2 \). The two agree.

(b) \( q(\u) = -(1 + 4) = -5 \). And \( \iota(\u)^2 = (\i + 2\j)^2 = -1 + 2\k - 2\k - 4 = -5 \), as required. Hence \( \iota(\u)^{-1} = q(\u)^{-1}\iota(\u) = -\tfrac15(\i + 2\j) \) by @prp-clifford-reflection.
:::

::: {#exr-clifford-algebras-b3}
[B3]

In \( \nR^{0,2} \) let \( \u = \e_1 \) and \( \v = \e_1 + \e_2 \). Compute the reflection \( s_{\u}(\v) \) directly from the formula in @prp-clifford-reflection, then compute \( -\iota(\u)\iota(\v)\iota(\u)^{-1} \) inside \( \nH \), and check that the two agree.
:::

::: {.solution}
Here \( \beta(\x,\y) = -(x_1y_1 + x_2y_2) \), so \( \beta(\u,\v) = -1 \) and \( q(\u) = -1 \). The formula gives
\[
s_{\u}(\v) = \v - \frac{2(-1)}{-1}\u = \v - 2\u = -\e_1 + \e_2 .
\]
In \( \nH \): \( \iota(\u) = \i \), \( \iota(\v) = \i + \j \), and \( \iota(\u)^{-1} = q(\u)^{-1}\i = -\i \). Hence
\[
-\i(\i + \j)(-\i) = \i(\i + \j)\i = (-1 + \k)\i = -\i + \k\i = -\i + \j ,
\]
using \( \k\i = \j \). That is \( \iota(-\e_1 + \e_2) \), which agrees with \( \iota(s_{\u}(\v)) \). Geometrically \( s_{\u} \) negates the \( \e_1 \) coordinate and fixes the \( \e_2 \) one, which is what the answer shows.
:::

### C. Going deeper

::: {#exr-clifford-algebras-c1}
[C1: A Clifford algebra of matrices]

In \( M_2(\nR) \) put \( \E_1 = \begin{psmallmatrix} 1 & 0 \\ 0 & -1\end{psmallmatrix} \) and \( \E_2 = \begin{psmallmatrix} 0 & 1 \\ -1 & 0 \end{psmallmatrix} \), and let \( V = \nR^2 \) carry the form \( q(\x) = x_1^2 - x_2^2 \) of signature \( (1,1) \), with \( f(\x) = x_1\E_1 + x_2\E_2 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( f(\x)^2 = q(\x)\I_2 \) for every \( \x \), and that \( (\I_2, \E_1, \E_2, \E_1\E_2) \) is a basis of \( M_2(\nR) \).
2. Assume a Clifford algebra \( (C, \iota) \) of \( (V, q) \) exists. Deduce that \( C \cong M_2(\nR) \), and hence that \( \dim C = 4 \).
:::

*Hint for (b): the homomorphism the universal property hands you has a surjective image; then count.*
:::

::: {.solution}
(a) A direct multiplication gives \( \E_1^2 = \I_2 \), \( \E_2^2 = -\I_2 \) and
\[
\E_1\E_2 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = -\E_2\E_1 ,
\]
so \( \E_1\E_2 + \E_2\E_1 = \0 \) and
\[
f(\x)^2 = x_1^2\E_1^2 + x_1x_2(\E_1\E_2 + \E_2\E_1) + x_2^2\E_2^2 = (x_1^2 - x_2^2)\I_2 .
\]
For the basis: \( a\I_2 + b\E_1 + c\E_2 + d\E_1\E_2 \) is the matrix with rows \( (a+b,\ c+d) \) and \( (-c+d,\ a-b) \), and setting all four entries to zero forces \( a = b = c = d = 0 \). Four independent vectors in the \( 4 \)-dimensional space \( M_2(\nR) \) form a basis.

(b) By (a) and the universal property (C2) with \( A = M_2(\nR) \), there is an algebra homomorphism \( \bar f \colon C \to M_2(\nR) \) with \( \bar f\iota = f \). Its image is a subalgebra containing \( \I_2 \), \( \E_1 = f(\e_1) \) and \( \E_2 = f(\e_2) \), hence also \( \E_1\E_2 \); by (a) those four span \( M_2(\nR) \), so \( \bar f \) is surjective and \( \dim C \ge 4 \). On the other hand \( \dim C \le 2^2 = 4 \) by @prp-clifford-spanning. Therefore \( \dim C = 4 \) and \( \bar f \) is a surjective linear map between spaces of equal finite dimension, hence bijective, hence an algebra isomorphism. So \( \operatorname{Cl}_{1,1}(\nR) \cong M_2(\nR) \).
:::

::: {#exr-clifford-algebras-c2}
[C2: Why characteristic 2 is excluded]

Explain why @def-clifford-algebra assumes \( \operatorname{char} F \ne 2 \), by naming the first statement of this section that fails without it and saying what replaces the missing input.
:::

::: {.solution}
The first casualty is @lem-clifford-anticommutation, whose proof cites @thm-polarization-forms for \( q(\u+\v) = q(\u) + 2\beta(\u,\v) + q(\v) \) — and that identity is how \( \beta \) is recovered from \( q \), by a division by \( 2 \) that is unavailable in characteristic \( 2 \). Without it, the relation \( \iota(\u)\iota(\v) + \iota(\v)\iota(\u) = 2\beta(\u,\v)1_C \) collapses to \( \iota(\u)\iota(\v) + \iota(\v)\iota(\u) = 0 \) and carries no information about the form at all. @prp-clifford-spanning then loses its sorting step in the form given, and @thm-symmetric-form-diagonalizable, which supplied the orthogonal basis, has the same hypothesis.

What is missing is a definition. In characteristic \( 2 \) a quadratic form is not the same data as a symmetric bilinear form — Section 3 warned exactly this — so a quadratic form must be defined in its own right, as a function \( q \colon V \to F \) with \( q(a\v) = a^2q(\v) \) whose associated \( \beta(\u,\v) = q(\u+\v) - q(\u) - q(\v) \) is bilinear. Clifford algebras are defined in that setting too, by the same (C1) and (C2), but this book does not define quadratic forms there and so does not go on.
:::
