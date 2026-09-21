# Associative Algebras

Since Chapter 8 the book has looked at one operator at a time, or at a family whose members commute. But operators rarely arrive alone. The polynomials in a fixed operator, the circulants of Chapter 11 §09, the matrices commuting with a given matrix, the linear symmetries of a figure: each of these is a whole set of operators, closed under addition, under scalars, and under composition. This section makes such a system a single object of study. It fixes the vocabulary — subalgebra, homomorphism, generated algebra, commutant — and builds the two examples the rest of the chapter runs on, the matrix algebra and the group algebra.

## What an algebra is, and what we assume about it

The definition is already in the book. Chapter 13 §12 introduced an **algebra over \( F \)** (@def-algebra-over-field) as a vector space \( A \) over \( F \) with a multiplication \( A \times A \to A \) that is bilinear (A1), associative (A2) and has an identity \( 1_A \) (A3). It also fixed the notion of a homomorphism of \( F \)-algebras. We build on that definition; the homomorphism clause is restated below only so that later sections have a label to cite.

Three standing conventions, stated once and used everywhere in this chapter.

- **Associative and unital.** Every algebra satisfies (A1), (A2) and (A3). Lie algebras and the cross product, which fail (A2) and (A3), are outside the chapter.
- **Finite-dimensional.** Unless a statement says otherwise, \( \dim_F A < \infty \). The one standing exception is \( F[x] \), which we keep as a source of counterexamples and always name as infinite-dimensional when we use it that way.
- **Not commutative, not invertible.** Nothing requires \( xy = yx \), and nothing requires a non-zero element to have an inverse. An algebra has an addition and a multiplication with all the usual laws except commutativity and division; it is not a group.

The examples are the ones Chapter 13 listed, and it is worth seeing why each satisfies the axioms. In \( M_n(F) \), matrix multiplication is bilinear and associative with identity \( \I_n \) (@thm-matrix-multiplication-properties), so \( M_n(F) \) is an \( F \)-algebra of dimension \( n^2 \). In \( \cL(V) \) for a vector space \( V \) over \( F \), composition is bilinear, associative and has the identity \( \id_V \) (@thm-composition-linear), so \( \cL(V) \) is an \( F \)-algebra; when \( \dim V = n \) it has dimension \( n^2 \) (@thm-linear-maps-isomorphic-to-matrices). The polynomial ring \( F[x] \) is an algebra of infinite dimension. The quaternions \( \nH \) form a real algebra of dimension \( 4 \) (@def-quaternions). The field \( F \) itself is an algebra of dimension \( 1 \), the degenerate case, and it matters: it is the smallest algebra that is not the zero space, and every non-zero algebra contains a copy of it.

::: {.remark}
Many books write \( \End(V) \), for the **endomorphisms** of \( V \), where this book writes \( \cL(V) \), and \( \Hom(V, W) \) where this book writes \( \cL(V, W) \). The names mean the same objects. This book writes \( \cL \) by default, and later sections of this chapter write \( \End(V) \) when the algebra structure is the point.
:::

## Subalgebras

After an object come its subobjects. We already know several sets of matrices that are closed under the three operations: the diagonal matrices, the upper triangular matrices, the circulants (@cor-circulants-algebra), the polynomials in a fixed matrix. In each case we checked closure by hand. The right move is to name the condition once.

*A subalgebra is a subspace that is closed under multiplication and contains the identity.*

::: {#def-subalgebra}
[Subalgebra]

Let \( A \) be an algebra over \( F \). A subset \( B \subseteq A \) is a **subalgebra** of \( A \) if

::: {.enumerate options="label=(SA\arabic*)"}
1. \( B \) is a **subspace** of \( A \);
2. \( xy \in B \) **for all** \( x, y \in B \);
3. \( 1_A \in B \).
:::
:::

Clause by clause. (SA1) is the linear condition: \( B \) is closed under addition and under scalars, so it is a vector space in its own right. (SA2) says the multiplication of \( A \) restricts to a map \( B \times B \to B \). (SA3) asks for **the** identity of \( A \), not merely for some element of \( B \) that acts as an identity on \( B \); the difference is real, and the warning below shows a set that satisfies (SA1) and (SA2), has its own identity, and is not a subalgebra.

**Well-definedness.** A subalgebra is an algebra. Bilinearity, associativity and the identity law are equations among elements of \( B \), and they hold there because they hold in \( A \). So nothing needs to be re-checked once (SA1)–(SA3) are known — which is exactly the labor that naming the condition saves.

Throughout, \( \E_{ij} \) denotes the **matrix unit** with a \( 1 \) in position \( (i, j) \) and zeros elsewhere; the \( n^2 \) of them are a basis of \( M_n(F) \) (@exm-standard-bases).

::: {#exm-first-subalgebras}
[Six subalgebras]

Decide which of the following are subalgebras, and of which algebra.

::: {.enumerate options="label=(\alph*)"}
1. The scalars \( F1_A = \{c1_A : c \in F\} \) inside any algebra \( A \).
2. The diagonal matrices and the upper triangular matrices inside \( M_n(F) \). We write \( \cT_n \) for the second of these, since it returns below and in the next section.
3. The circulants \( \cC_n \) inside \( M_n(\nC) \) (Chapter 11 §09).
4. The quaternions \( \nH \) inside \( M_2(\nC) \), as an algebra over \( \nR \).
5. The **strictly** upper triangular matrices inside \( M_n(F) \).
6. The matrices of trace \( 0 \) inside \( M_2(F) \).
:::
:::

::: {.solution}
(a) A subalgebra. It is the image of the linear map \( c \mapsto c1_A \), hence a subspace; \( (c1_A)(d1_A) = (cd)1_A \) by bilinearity; and \( 1_A = 1\cdot 1_A \). Its dimension is \( 1 \) unless \( A = \{0\} \): if \( 1_A = 0 \), then \( x = 1_Ax = 0 \) for every \( x \). This is the degenerate example, and every subalgebra contains it.

(b) Both are subalgebras. Sums and scalar multiples of diagonal (respectively upper triangular) matrices are again such, the product of two upper triangular matrices is upper triangular because \( (\A\B)_{ij} = \sum_k a_{ik}b_{kj} \) vanishes when \( i > j \) — every term has \( k < i \) or \( k > j \) — and \( \I_n \) is diagonal. The diagonal matrices have dimension \( n \), with basis the \( \E_{ii} \), and \( \cT_n \) has dimension \( n(n+1)/2 \), with basis the \( \E_{ij} \) for \( i \le j \).

(c) A subalgebra, of dimension \( n \): this is exactly @cor-circulants-algebra (a), (b), together with the fact that \( \I \) is the circulant whose first row is \( (1, 0, \dots, 0) \).

(d) A subalgebra of \( M_2(\nC) \) **over \( \nR \)**, of real dimension \( 4 \), as @def-quaternions records: the real span of \( \I_2, \i, \j, \k \) is closed under multiplication by the quaternion relations, and it contains \( \I_2 \). It is **not** a subalgebra over \( \nC \), since it is not closed under multiplication by \( i \): \( i\I_2 \) has both diagonal entries equal to \( i \), while every element of \( \nH \) has diagonal entries \( a + bi \) and \( a - bi \), forcing \( a = 0 \) and \( b = 1 \) and \( b = -1 \) at once.

(e) **Not** a subalgebra. It is a subspace and it is closed under products, by the computation in (b) with strict inequalities. But \( \I_n \) is not strictly upper triangular for \( n \ge 1 \), so (SA3) fails. This is the non-example by minimal change: drop the diagonal from (b) and exactly one clause breaks.

(f) **Not** a subalgebra. \( \E_{12}\E_{21} = \E_{11} \) has trace \( 1 \ne 0 \), so (SA2) fails. Clause (SA3) fails too, except in characteristic \( 2 \), where \( \tr\I_2 = 2 = 0 \).
:::

::: {.warning}
(SA3) is not a formality. In \( M_2(F) \), the set \( B = \{a\E_{11} : a \in F\} \) is a subspace, is closed under products, and even has an identity of its own, namely \( \E_{11} \), since \( \E_{11}(a\E_{11}) = a\E_{11} \). It is still not a subalgebra of \( M_2(F) \), because \( \I_2 \notin B \). Subspaces that are closed under multiplication but miss the identity are the shape of the *ideals* of the next section — though this particular one is not an ideal either, as Section 2 checks. They are a different kind of object, and no theorem about subalgebras applies to them.
:::

::: {.check}
In \( M_2(\nF_2) \), is the set of matrices of trace \( 0 \) closed under multiplication? Does it contain the identity?
:::

::: {.solution}
It contains \( \I_2 \), because \( \tr\I_2 = 1 + 1 = 0 \) in \( \nF_2 \), so (SA3) holds here. But it is still not a subalgebra: \( \E_{12} \) and \( \E_{21} \) have trace \( 0 \) and \( \E_{12}\E_{21} = \E_{11} \) has trace \( 1 \ne 0 \), so (SA2) fails. One clause can hold over one field and fail over another; the other clause fails over every field.
:::

## Homomorphisms, isomorphisms, and the algebra generated by a set

@def-algebra-over-field already says what a homomorphism of \( F \)-algebras is: an \( F \)-linear map \( \varphi \colon A \to B \) with \( \varphi(xy) = \varphi(x)\varphi(y) \) and \( \varphi(1_A) = 1_B \). We name it, so that later sections can cite it, and add the two subsets it produces.

::: {#def-algebra-homomorphism}
[Algebra Homomorphism, Kernel and Image]

Let \( A \) and \( B \) be algebras over \( F \). An **algebra homomorphism** \( \varphi \colon A \to B \) is an \( F \)-linear map with
\[
\varphi(xy) = \varphi(x)\varphi(y) \quad \text{for all } x, y \in A,
\qquad \varphi(1_A) = 1_B ,
\]
as in @def-algebra-over-field. Its **kernel** is \( \ker\varphi = \{x \in A : \varphi(x) = 0\} \) and its **image** is \( \im\varphi = \{\varphi(x) : x \in A\} \), the kernel and image of \( \varphi \) as a linear map.
:::

The unital clause \( \varphi(1_A) = 1_B \) does not follow from the other two. The zero map \( M_2(F) \to M_2(F) \) is linear and multiplicative and sends \( \I_2 \) to \( 0 \ne \I_2 \), so it is **not** an algebra homomorphism. We will never call it one.

::: {#def-algebra-isomorphism}
[Isomorphic Algebras]

An **algebra isomorphism** is a bijective algebra homomorphism. Algebras \( A \) and \( B \) are **isomorphic**, written \( A \cong B \), if there is an algebra isomorphism \( A \to B \).
:::

The inverse of an algebra isomorphism \( \varphi \) is again one: it is linear (@thm-inverse-is-linear), it satisfies \( \varphi^{-1}(uv) = \varphi^{-1}(u)\varphi^{-1}(v) \) — apply the injective map \( \varphi \) to both sides — and \( \varphi^{-1}(1_B) = 1_A \). So \( \cong \) is symmetric, and it is reflexive and transitive for the same reasons as in @thm-isomorphic-equivalence-relation.

Two homomorphisms to keep in mind. First, taking matrices: for a finite-dimensional \( V \) with ordered basis \( \sB \), the map \( T \mapsto \mtx{T}{\sB}{\sB} \) is an algebra isomorphism \( \cL(V) \to M_n(F) \), being a linear bijection (@thm-linear-maps-isomorphic-to-matrices) that turns composition into matrix multiplication (@thm-matrix-of-composition) and sends \( \id_V \) to \( \I_n \). Second, a non-example: transposition \( \A \mapsto \A\tp \) on \( M_n(F) \) is a linear bijection fixing \( \I_n \), but \( (\A\B)\tp = \B\tp\A\tp \), so it reverses products. For \( n \ge 2 \) it is not a homomorphism, since \( (\E_{12}\E_{21})\tp = \E_{11} \) while \( \E_{12}\tp\E_{21}\tp = \E_{21}\E_{12} = \E_{22} \).

Now the construction we need constantly: the smallest subalgebra containing a given set of operators.

::: {#def-generated-subalgebra}
[The Subalgebra Generated by a Set]

Let \( A \) be an algebra over \( F \) and \( S \subseteq A \). The **subalgebra generated by \( S \)**, written \( F\langle S\rangle \), is the intersection of all subalgebras of \( A \) containing \( S \).
:::

The letter \( F \) in \( F\langle S\rangle \) records that scalars are allowed; the next section writes \( \langle S\rangle \), without the \( F \), for the **ideal** generated by \( S \), which is a different and usually larger set. The intersection of any collection of subalgebras is a subalgebra — each clause of @def-subalgebra is preserved by intersections — and \( A \) itself is one of them, so \( F\langle S\rangle \) is a subalgebra containing \( S \), and it is contained in every other one. That is what "generated" means. It also has a concrete description.

::: {#prp-generated-is-span-of-words}
[What the Generated Subalgebra Contains]

Let \( A \) be an algebra over \( F \) and \( S \subseteq A \). Then \( F\langle S\rangle \) is the span of \( 1_A \) together with all finite products \( s_1s_2\cdots s_k \) with \( k \ge 1 \) and \( s_1, \dots, s_k \in S \).
:::

::: {.proof}
Let \( P \) be that span. Every subalgebra containing \( S \) contains each product \( s_1\cdots s_k \) by (SA2) and induction on \( k \), contains \( 1_A \) by (SA3), and is a subspace by (SA1); hence it contains \( P \). In particular \( P \subseteq F\langle S\rangle \).

Conversely \( P \) is itself a subalgebra: it is a span, hence a subspace; it contains \( 1_A \); and a product of two spanning elements is either \( 1_A \), or a product \( s_1\cdots s_k \), or a concatenation \( (s_1\cdots s_k)(t_1\cdots t_l) \), which is again such a product by associativity. By bilinearity, a product of two elements of \( P \) is a combination of such products, so it lies in \( P \). Since \( S \subseteq P \), minimality gives \( F\langle S\rangle \subseteq P \). This proves the proposition.
:::

For a single operator the products are just the powers, and the minimal polynomial says how many of them are independent.

::: {#prp-polynomial-algebra-dimension}
[The Algebra Generated by One Operator]

Let \( V \ne \{\0\} \) be finite-dimensional over \( F \) and let \( T \in \cL(V) \) have minimal polynomial \( m_T \), of degree \( d \). Then
\[
F[T] \coloneqq \{p(T) : p \in F[x]\}
\]
is a **commutative** subalgebra of \( \cL(V) \), it equals \( F\langle\{T\}\rangle \), and \( (\id_V, T, T^2, \dots, T^{d-1}) \) is a basis of it. In particular \( \dim F[T] = \deg m_T \).
:::

::: {.idea}
Division with remainder cuts every power of \( T \) down to degree less than \( d \), which gives spanning; and a shorter relation among the powers would be an annihilating polynomial of degree less than \( d \), which is what minimality forbids.
:::

::: {.proof}
By @thm-evaluation-homomorphism the map \( p \mapsto p(T) \) is linear and multiplicative, so \( F[T] \) is a subspace closed under products, and it contains \( \id_V = 1(T) \); it is therefore a subalgebra. Any two of its elements commute, since \( p(T)q(T) = (pq)(T) = (qp)(T) = q(T)p(T) \). By @prp-generated-is-span-of-words, \( F\langle\{T\}\rangle \) is the span of \( \id_V \) and the powers \( T^k \) with \( k \ge 1 \), which is \( F[T] \).

Since \( V \) is finite-dimensional, \( m_T \) exists (@thm-annihilator-ideal (b), (c)); and \( d \ge 1 \), because the only monic polynomial of degree \( 0 \) is \( 1 \), whose value at \( T \) is \( \id_V \ne 0 \) since \( V \ne \{\0\} \).

*Spanning.* Let \( p \in F[x] \). Dividing by \( m_T \) (@thm-polynomial-division) gives \( p = qm_T + r \) with \( \deg r < d \), and \( p(T) = q(T)m_T(T) + r(T) = r(T) \), a combination of \( \id_V, T, \dots, T^{d-1} \).

*Independence.* Suppose \( c_0\id_V + c_1T + \dots + c_{d-1}T^{d-1} = 0 \) with the \( c_i \) not all zero. Then \( r = c_0 + c_1x + \dots + c_{d-1}x^{d-1} \) is a non-zero polynomial with \( r(T) = 0 \) and \( \deg r < d \), contradicting the fact that \( m_T \) has least degree among the non-zero annihilating polynomials (@thm-annihilator-ideal (b)).

So the \( d \) listed operators are a basis, and \( \dim F[T] = d \). This proves the proposition.
:::

::: {#exm-two-polynomial-algebras}
[Two polynomial algebras]

Compute \( \dim F[\A] \) for \( \A = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} \) and for \( \B = \diag(1, 2, 3) \) over \( \nQ \).
:::

::: {.solution}
For \( \A \): \( \A^2 = 0 \) and \( \A \ne 0 \), so \( x^2 \) annihilates \( \A \) and no polynomial of degree \( 1 \) does (if \( a\I + b\A = 0 \), reading the \( (1,1) \) and \( (1,2) \) entries gives \( a = b = 0 \)). Hence \( m_{\A} = x^2 \) and \( \dim\nQ[\A] = 2 \), with basis \( (\I, \A) \). Note that \( \dim\nQ[\A] = 2 \) is much smaller than \( \dim M_3(\nQ) = 9 \).

For \( \B \): \( (x-1)(x-2)(x-3) \) annihilates \( \B \), since the product of the three diagonal matrices \( \B - k\I \) is \( 0 \). No polynomial \( r \) of degree at most \( 2 \) does, unless \( r = 0 \): \( r(\B) = \diag(r(1), r(2), r(3)) = 0 \) would give \( r \) three distinct roots. So \( m_{\B} \) has degree \( 3 \) and \( \dim\nQ[\B] = 3 \), with basis \( (\I, \B, \B^2) \).
:::

## The group algebra

Here is the object that turns a group of symmetries into linear algebra. Suppose a finite group \( G \) acts on a space by invertible operators \( \rho(g) \). Then every \( F \)-combination \( \sum_g a_g\rho(g) \) is again an operator, and the products of such combinations are governed entirely by the multiplication table of \( G \). It is worth building, once and for all, the algebra in which those formal combinations live.

*The group algebra is the set of formal \( F \)-combinations of group elements, multiplied by the group law.*

::: {#def-group-algebra}
[Group Algebra]

Let \( G \) be a **finite** group with identity \( e \), and let \( F \) be a field. The **group algebra** \( F[G] \) is the free vector space \( F^{(G)} \) on the set \( G \) (@def-free-vector-space), with basis \( \{\delta_g : g \in G\} \), equipped with the unique bilinear multiplication satisfying
\[
\delta_g\,\delta_h = \delta_{gh} \qquad \text{for all } g, h \in G .
\]
We write \( g \) for \( \delta_g \) and \( 1 \) for \( \delta_e \), so that a general element is a formal sum \( \sum_{g \in G} a_g\,g \) with all \( a_g \in F \), two such sums are equal exactly when all their coefficients agree, and
\[
\Bigl(\sum_{g} a_g\,g\Bigr)\Bigl(\sum_{h} b_h\,h\Bigr)
= \sum_{k \in G}\Bigl(\sum_{g \in G} a_g\,b_{g^{-1}k}\Bigr)k .
\]
:::

**Well-definedness.** Choose an ordering \( g_1, \dots, g_N \) of \( G \), so that \( (\delta_{g_1}, \dots, \delta_{g_N}) \) is an ordered basis of \( F^{(G)} \) (@lem-free-vector-space (a)). By @thm-multilinear-determined-by-basis with \( k = 2 \), there is **exactly one** bilinear map \( F[G] \times F[G] \to F[G] \) taking the prescribed values \( \delta_{g_ig_j} \) on basis pairs. The displayed formula for the product is that bilinear map written out: expanding \( \sum_{g,h}a_gb_h\,gh \) and collecting the terms with \( gh = k \), which means \( h = g^{-1}k \), gives the stated coefficient of \( k \).

The axioms hold. Bilinearity is (A1) by construction. For associativity (A2), both \( (xy)z \) and \( x(yz) \) are trilinear in \( (x, y, z) \), so by @thm-multilinear-determined-by-basis it is enough to compare them on basis triples, where \( (\delta_g\delta_h)\delta_k = \delta_{(gh)k} = \delta_{g(hk)} = \delta_g(\delta_h\delta_k) \) by the associativity axiom (G1) of @def-group. For (A3), \( \delta_e\delta_g = \delta_{eg} = \delta_g = \delta_g\delta_e \) on basis elements, hence everywhere by bilinearity. So \( F[G] \) is an \( F \)-algebra, of dimension \( \lvert G\rvert \).

In words: an element of \( F[G] \) is a bookkeeping device, a list of \( \lvert G\rvert \) scalars indexed by the group, and multiplying two of them convolves the lists along the group law. The group sits inside \( F[G] \): the map \( g \mapsto \delta_g \) is injective (distinct basis vectors) and multiplicative, and each \( \delta_g \) is invertible with inverse \( \delta_{g^{-1}} \).

::: {#exm-group-algebras}
[Three group algebras]

::: {.enumerate options="label=(\alph*)"}
1. \( G = \{e\} \).
2. \( G = \nZ/n\nZ \), written multiplicatively as \( \{1, g, \dots, g^{n-1}\} \) with \( g^n = 1 \).
3. \( G = S_3 \).
:::

In each case give the dimension and decide whether \( F[G] \) is commutative.
:::

::: {.solution}
(a) \( F[\{e\}] = F\delta_e \cong F \), of dimension \( 1 \), and commutative. This is the degenerate case.

(b) \( \dim F[G] = n \), and \( F[G] \) is commutative because \( g^ig^j = g^{i+j} = g^jg^i \) on basis elements and multiplication is bilinear. Moreover the map \( \varepsilon \colon F[x] \to F[G] \) sending \( p = \sum_i c_ix^i \) to \( \sum_i c_ig^i \) is an algebra homomorphism: it is linear by construction, it sends \( 1 \) to \( g^0 = 1 \), and for \( p = \sum_i c_ix^i \) and \( q = \sum_j d_jx^j \),
\[
\varepsilon(pq) = \sum_k \Bigl(\sum_{i+j=k} c_id_j\Bigr)g^k = \Bigl(\sum_i c_ig^i\Bigr)\Bigl(\sum_j d_jg^j\Bigr) = \varepsilon(p)\varepsilon(q),
\]
where the middle equality is bilinearity together with \( g^ig^j = g^{i+j} \). It is surjective because the powers \( 1, g, \dots, g^{n-1} \) are a basis. Its kernel is exactly \( \langle x^n - 1\rangle \): dividing \( p \) by \( x^n - 1 \) (@thm-polynomial-division) gives \( p = q(x^n-1) + r \) with \( \deg r < n \), and since \( \varepsilon(x^n - 1) = g^n - 1 = 0 \) we get \( \varepsilon(p) = \varepsilon(r) \), which vanishes only when all coefficients of \( r \) vanish, the \( g^i \) being a basis. The next section turns this into an isomorphism \( F[\nZ/n\nZ] \cong F[x]/\langle x^n - 1\rangle \).

(c) \( \dim F[S_3] = 6 \), and \( F[S_3] \) is **not** commutative: with \( \sigma = (1\ 2) \) and \( \tau = (1\ 2\ 3) \) we have \( \sigma\tau \ne \tau\sigma \) in \( S_3 \), so \( \delta_{\sigma}\delta_{\tau} \ne \delta_{\tau}\delta_{\sigma} \) are distinct basis vectors. In general \( F[G] \) is commutative if and only if \( G \) is abelian: the displayed argument gives one direction, and if \( F[G] \) is commutative then \( \delta_{gh} = \delta_g\delta_h = \delta_h\delta_g = \delta_{hg} \), and distinct group elements give distinct basis vectors, so \( gh = hg \).
:::

::: {.warning}
The elements of \( F[G] \) are formal sums, not group elements, and most of them are **not** invertible. In \( \nQ[\nZ/2\nZ] \) with \( \nZ/2\nZ = \{1, g\} \), the element \( 1 + g \) satisfies \( (1+g)^2 = 1 + 2g + g^2 = 2(1+g) \), so \( \tfrac12(1+g) \) is a non-zero element equal to its own square and different from \( 1 \). Multiplying it by \( 1 - g \) gives \( 0 \), so neither factor has an inverse. Passing from \( G \) to \( F[G] \) buys linearity at the price of invertibility.
:::

## Every finite-dimensional algebra is an algebra of matrices

Matrices look like a special case of an algebra. They are not: every finite-dimensional algebra is one, and the embedding is the most economical thing imaginable — let the algebra act on itself.

::: {#thm-cayley-for-algebras}
[Left Multiplication Embeds an Algebra in Its Own Operators]

Let \( A \) be an algebra over \( F \). For \( a \in A \) define \( L_a \colon A \to A \) by \( L_a(x) = ax \). Then
\[
L \colon A \to \cL(A), \qquad a \mapsto L_a ,
\]
is an **injective** algebra homomorphism. If \( \dim_F A = n < \infty \), then \( A \) is isomorphic to a subalgebra of \( M_n(F) \).
:::

::: {.idea}
Each axiom of an algebra says one thing about \( L \): bilinearity in the second slot makes \( L_a \) linear, bilinearity in the first makes \( a \mapsto L_a \) linear, associativity makes \( L \) multiplicative, and the identity makes \( L \) unital and — this is the point — injective, because an operator that kills everything in particular kills \( 1_A \), and \( L_a(1_A) = a \).
:::

::: {.proof}
Each \( L_a \) is linear, because multiplication is linear in its second argument (A1). The map \( L \) is linear, because multiplication is linear in its first argument: \( L_{a + ca'}(x) = (a + ca')x = ax + c(a'x) \) for all \( x \).

\( L \) is multiplicative: for \( a, b, x \in A \), associativity (A2) gives
\[
L_{ab}(x) = (ab)x = a(bx) = L_a\bigl(L_b(x)\bigr) = (L_aL_b)(x) ,
\]
so \( L_{ab} = L_aL_b \). It is unital: \( L_{1_A}(x) = 1_Ax = x \), so \( L_{1_A} = \id_A \).

\( L \) is injective: if \( L_a = 0 \) then, evaluating at \( 1_A \), \( a = a1_A = L_a(1_A) = 0 \). So \( \ker L = \{0\} \) and \( L \) is injective (@thm-injective-iff-trivial-kernel).

Suppose now \( \dim_F A = n < \infty \). Then \( \im L \) is a subalgebra of \( \cL(A) \): it is a subspace, it is closed under products since \( L_aL_b = L_{ab} \), and it contains \( \id_A = L_{1_A} \). The map \( L \colon A \to \im L \) is a bijective algebra homomorphism, hence an algebra isomorphism. Fixing an ordered basis of \( A \) and taking matrices is an algebra isomorphism \( \cL(A) \to M_n(F) \), as recorded after @def-algebra-isomorphism, and it carries \( \im L \) to a subalgebra of \( M_n(F) \) isomorphic to \( A \). This proves the theorem.
:::

The theorem is the reason the rest of the chapter may think in matrices without loss. It is also a genuine computation: to see an abstract algebra concretely, write down the matrices of left multiplication in a basis.

::: {#exm-cayley-upper-triangular}
[Left multiplication for the upper triangular algebra]

Let \( A = \cT_2 \), the upper triangular matrices in \( M_2(F) \), with ordered basis \( \sB = (\E_{11}, \E_{12}, \E_{22}) \). Compute the matrix of \( L_{\U} \) for \( \U = \begin{pmatrix} a & b \\ 0 & c\end{pmatrix} \), and read off what the embedding of @thm-cayley-for-algebras does.
:::

::: {.solution}
Multiply each basis element on the left by \( \U \):
\[
\U\E_{11} = a\E_{11}, \qquad
\U\E_{12} = a\E_{12}, \qquad
\U\E_{22} = b\E_{12} + c\E_{22} .
\]
Putting the coordinate vectors in as columns,
\[
\mtx{L_{\U}}{\sB}{\sB} =
\begin{pmatrix} a & 0 & 0 \\ 0 & a & b \\ 0 & 0 & c \end{pmatrix} .
\]
So \( \cT_2 \), an algebra of \( 2 \times 2 \) matrices of dimension \( 3 \), is isomorphic to the algebra of \( 3 \times 3 \) matrices of this shape. The embedding is faithful but wasteful: \( \U \mapsto \U \) already embeds \( \cT_2 \) in \( M_2(F) \). Left multiplication is the embedding that always exists, not the smallest one.
:::

## Commutants

The last construction of the section is the one that will carry Schur's lemma later. Given a set of operators, ask which operators commute with all of them. Chapter 8 §09 asked this about a pair, Chapter 9 §04 about a Weyr matrix, Chapter 11 §07 about a normal family. It is the same question each time.

*The commutant of a set is everything that commutes with all of it.*

::: {#def-commutant}
[Commutant and Center]

Let \( A \) be an algebra over \( F \) and let \( S \subseteq A \) be **any subset**. The **commutant** of \( S \) in \( A \) is
\[
S' \coloneqq \{ a \in A : as = sa \text{ for every } s \in S \} .
\]
The **center** of \( A \) is \( Z(A) \coloneqq A' \), the set of elements commuting with **every** element of \( A \). We write \( S'' \) for \( (S')' \).
:::

In words: to belong to \( S' \), an element must commute with each member of \( S \) — one failure disqualifies it. The members of \( S \) need not commute with each other, and \( S \) need not be a subspace or a subalgebra; the definition asks nothing of \( S \).

::: {#prp-commutant-is-algebra}
[Properties of the Commutant]

Let \( A \) be an algebra over \( F \) and \( S, T \subseteq A \).

::: {.enumerate options="label=(\alph*)"}
1. \( S' \) is a subalgebra of \( A \); in particular \( Z(A) \) is a commutative subalgebra.
2. If \( S \subseteq T \), then \( T' \subseteq S' \).
3. \( S \subseteq S'' \).
4. \( S' = S''' \).
:::
:::

::: {.proof}
(a) Fix \( s \in S \). The set \( \{a : as = sa\} \) is the kernel of the linear map \( a \mapsto as - sa \), hence a subspace (@thm-prop-kernel); \( S' \) is the intersection of these subspaces over \( s \in S \), hence a subspace. If \( a, b \in S' \) then \( (ab)s = a(bs) = a(sb) = (as)b = (sa)b = s(ab) \), using associativity at each step, so \( ab \in S' \). And \( 1_As = s = s1_A \), so \( 1_A \in S' \). Thus \( S' \) is a subalgebra. For the center, every element of \( Z(A) \) commutes with every element of \( A \), so in particular any two of them commute.

(b) If \( a \) commutes with every element of \( T \) and \( S \subseteq T \), then \( a \) commutes with every element of \( S \).

(c) Let \( s \in S \). Every \( a \in S' \) satisfies \( as = sa \), which is the condition for \( s \) to lie in \( (S')' \).

(d) Applying (c) to \( S' \) gives \( S' \subseteq S''' \). Applying (b) to the inclusion \( S \subseteq S'' \) of (c) gives \( (S'')' \subseteq S' \), that is, \( S''' \subseteq S' \).
:::

Three commutants, computed. Each is a short exercise in comparing entries, and the pattern they show is the one Schur's lemma will explain.

::: {#exm-three-commutants}
[Commutants of three matrices]

Compute the commutant \( S' \) inside the stated algebra for

::: {.enumerate options="label=(\alph*)"}
1. \( S = \{\D\} \) inside \( M_3(F) \), where \( \D = \diag(d_1, d_2, d_3) \) has \( d_1, d_2, d_3 \) **distinct**;
2. \( S = \{\N\} \) inside \( M_3(F) \), where \( \N = \J_3(0) \) is the nilpotent Jordan block;
3. \( S = M_3(\nQ) \) inside \( M_3(\nQ) \).
:::
:::

::: {.solution}
(a) *Distinct diagonal.* Comparing the \( (i,j) \) entries, \( (\D\X)_{ij} = d_ix_{ij} \) and \( (\X\D)_{ij} = x_{ij}d_j \), so \( \D\X = \X\D \) says \( (d_i - d_j)x_{ij} = 0 \) for all \( i, j \). Since the \( d_i \) are distinct, \( x_{ij} = 0 \) whenever \( i \ne j \). So \( \{\D\}' \) is the algebra of diagonal matrices in \( M_3(F) \), of dimension \( 3 \). Here \( m_{\D} \) has degree \( 3 \), since \( (x - d_1)(x - d_2)(x - d_3) \) annihilates \( \D \) while no non-zero polynomial of degree at most \( 2 \) does, such a polynomial having the three distinct roots \( d_1, d_2, d_3 \); so by @prp-polynomial-algebra-dimension \( \dim F[\D] = 3 \) as well. Every polynomial in \( \D \) commutes with \( \D \), so \( F[\D] \subseteq \{\D\}' \), and equal dimensions give \( \{\D\}' = F[\D] \).

(b) *Jordan block.* Write \( \N = \E_{12} + \E_{23} \). Then \( (\N\X)_{ij} = x_{i+1,j} \) (read as \( 0 \) when \( i + 1 > 3 \)) and \( (\X\N)_{ij} = x_{i,j-1} \) (read as \( 0 \) when \( j - 1 < 1 \)). Setting these equal for all \( i, j \): the entries with \( j = 1 \) give \( x_{21} = x_{31} = 0 \), the entries with \( i = 3 \) give \( x_{31} = x_{32} = 0 \), and the four remaining equations give \( x_{22} = x_{11} \), \( x_{23} = x_{12} \), \( x_{32} = x_{21} \) and \( x_{33} = x_{22} \). So
\[
\{\N\}' = \left\{ \begin{pmatrix} a & b & c \\ 0 & a & b \\ 0 & 0 & a\end{pmatrix} : a, b, c \in F \right\}
= F[\N] ,
\]
of dimension \( 3 \), since \( \I, \N, \N^2 \) are exactly the three matrices of this shape with one of \( a, b, c \) equal to \( 1 \) and the others \( 0 \). Again \( \deg m_{\N} = 3 \), so this is \( F[\N] \) by @prp-polynomial-algebra-dimension.

(c) *The whole algebra.* Let \( \X \in M_3(\nQ)' \). Commuting with \( \D = \diag(1,2,3) \) forces \( \X \) diagonal by the first computation, say \( \X = \diag(x_1, x_2, x_3) \); and then \( \X\E_{12} = x_1\E_{12} \) while \( \E_{12}\X = x_2\E_{12} \), so \( x_1 = x_2 \), and similarly \( x_2 = x_3 \). Hence \( \X \) is a scalar matrix. Conversely scalar matrices commute with everything. So \( Z(M_3(\nQ)) = \nQ\I_3 \), of dimension \( 1 \). The argument used that \( 1, 2, 3 \) are distinct scalars; over a field of characteristic \( 2 \) or \( 3 \) they are not, which is why the general statement below is proved with matrix units instead.
:::

The last computation deserves a clean statement over every field, because later sections use it.

::: {#prp-center-of-matrix-algebra}
[The Center of the Matrix Algebra Is the Scalars]

Let \( F \) be **any** field and \( n \ge 1 \). Then \( Z(M_n(F)) = F\I_n \). Equivalently, for a finite-dimensional \( V \ne \{\0\} \), the operators commuting with every operator on \( V \) are exactly the scalar multiples of \( \id_V \).
:::

::: {.proof}
\( (\supseteq) \) A scalar matrix \( c\I_n \) satisfies \( (c\I_n)\X = c\X = \X(c\I_n) \) by @thm-matrix-multiplication-properties (4).

\( (\subseteq) \) For \( n = 1 \) the claim reads \( F = F\I_1 \), which is true, so assume \( n \ge 2 \). Let \( \X = (x_{pq}) \in Z(M_n(F)) \). Writing \( (\E_{ij})_{pq} = \delta_{pi}\delta_{qj} \) and expanding both products with @thm-three-views-of-product (1),
\[
(\E_{ij}\X)_{pq} = \delta_{pi}\,x_{jq},
\qquad
(\X\E_{ij})_{pq} = x_{pi}\,\delta_{qj} .
\]
Now fix \( j \) and choose any \( i \ne j \), which is possible because \( n \ge 2 \). Reading \( \E_{ij}\X = \X\E_{ij} \) at \( (p, q) = (i, q) \) with \( q \ne j \) gives \( x_{jq} = x_{ii}\delta_{qj} = 0 \), so every off-diagonal entry in row \( j \) of \( \X \) vanishes; and reading it at \( (p, q) = (i, j) \) gives \( x_{jj} = x_{ii} \). Letting \( j \) run over all indices makes \( \X \) diagonal, and applying the second conclusion to every pair \( i \ne j \) makes all its diagonal entries equal. So \( \X = x_{11}\I_n \).

The statement for operators follows by choosing a basis and applying the algebra isomorphism \( \cL(V) \to M_n(F) \) recorded after @def-algebra-isomorphism, which carries \( \id_V \) to \( \I_n \), and under which an element of the center corresponds to an element of the center. This proves the proposition.
:::

::: {.check}
In \( M_2(F) \), what is \( \{\I_2\}' \), and what is \( \{\I_2\}'' \)? Does \( S'' = S \) hold for \( S = \{\I_2\} \)?
:::

::: {.solution}
Everything commutes with \( \I_2 \), so \( \{\I_2\}' = M_2(F) \). Then \( \{\I_2\}'' = Z(M_2(F)) = F\I_2 \) by @prp-center-of-matrix-algebra. So \( S \subsetneq S'' \) here: \( S'' \) is the one-dimensional space of scalar matrices, while \( S \) is a single matrix. The inclusion of @prp-commutant-is-algebra (c) is genuinely an inclusion, and \( S'' \) should be read as "the smallest thing \( S \) cannot be distinguished from by commutation".
:::

::: {.remark}
Both commutants in @exm-three-commutants (a), (b) came out equal to the algebra generated by the matrix. That is not automatic. For \( \A = \I_n \) with \( n \ge 2 \), the algebra \( F[\A] \) is the one-dimensional space of scalar matrices, while \( \{\A\}' = M_n(F) \) has dimension \( n^2 \). The exact condition is that the minimal and characteristic polynomials of \( \A \) agree, which is Chapter 9 §05's condition for a cyclic vector to exist; **that equivalence is quoted here and not proved**, and nothing in this chapter depends on it.
:::

::: {.warning}
An algebra is not a group, and the theory of this chapter never assumes an inverse. In \( F[x] \) the only elements with a multiplicative inverse are the non-zero constants, since \( \deg(pq) = \deg p + \deg q \); in \( M_n(F) \) the invertible elements are the non-singular matrices, a proper subset; in \( F[G] \) the warning above produced two non-zero elements with product \( 0 \). Every argument below that wants to divide must first produce an inverse, and most of them cannot.
:::

## Exercises

### A. Check your understanding

::: {#exr-associative-algebras-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the three clauses in the definition of a subalgebra, and say which one the strictly upper triangular matrices fail.
2. Give the definition of the commutant \( S' \) of a subset \( S \) of an algebra \( A \), and say why \( S \) itself need not be a subalgebra.
3. True or false, with a reason: a linear bijection \( \varphi \colon A \to B \) with \( \varphi(xy) = \varphi(x)\varphi(y) \) for all \( x, y \) is an algebra isomorphism.
4. What is \( \dim F[G] \), and what is \( \dim F[T] \) for an operator \( T \) on a finite-dimensional space?
:::
:::

::: {.solution}
(a) (SA1) a subspace, (SA2) closed under products, (SA3) contains \( 1_A \). The strictly upper triangular matrices fail (SA3), since \( \I_n \) has non-zero diagonal.

(b) \( S' = \{a \in A : as = sa \text{ for every } s \in S\} \) (@def-commutant). The definition quantifies over the elements of \( S \) one at a time and asks nothing of \( S \) as a set, so \( S \) may be a single element, a finite list, or any subset at all.

(c) True — but note that \( \varphi(1_A) = 1_B \) is a separate requirement in general, which here follows from bijectivity: for every \( u \in B \), writing \( u = \varphi(x) \), we get \( \varphi(1_A)u = \varphi(1_Ax) = u \) and likewise on the other side, so \( \varphi(1_A) \) is an identity of \( B \) and equals \( 1_B \) by uniqueness of identities. The statement is true for bijective \( \varphi \); it is false without bijectivity, as the zero map shows.

(d) \( \dim F[G] = \lvert G\rvert \) (@def-group-algebra) and \( \dim F[T] = \deg m_T \) (@prp-polynomial-algebra-dimension).
:::

### B. Practice

::: {#exr-associative-algebras-b1}
[B1: Determine which are subalgebras]

Determine which of the following are subalgebras of the stated algebra. Justify your answer, naming the exact clause that fails when one does.

::: {.enumerate options="label=(\alph*)"}
1. \( \{\A \in M_2(F) : a_{21} = 0\} \) inside \( M_2(F) \).
2. \( \{\A \in M_2(F) : a_{12} = a_{21}\} \) inside \( M_2(F) \).
3. \( \{p \in F[x] : p(0) = p(1)\} \) inside \( F[x] \).
4. \( \{c\,\id_V + N : c \in F,\ N^2 = 0\} \) inside \( \cL(V) \), for \( \dim V = 3 \).
:::
:::

::: {.solution}
(a) A subalgebra: this is \( \cT_2 \), handled in @exm-first-subalgebras (b).

(b) **Not** a subalgebra. The set is the symmetric matrices, a subspace containing \( \I_2 \), so (SA1) and (SA3) hold. But (SA2) fails: \( \begin{psmallmatrix} 0&1\\1&0\end{psmallmatrix}\begin{psmallmatrix} 1&0\\0&0\end{psmallmatrix} = \begin{psmallmatrix} 0&0\\1&0\end{psmallmatrix} \), which is not symmetric.

(c) A subalgebra. It is the kernel of the linear functional \( p \mapsto p(0) - p(1) \), hence a subspace; it contains \( 1 \); and if \( p(0) = p(1) \) and \( q(0) = q(1) \) then \( (pq)(0) = p(0)q(0) = p(1)q(1) = (pq)(1) \) by @thm-evaluation-respects-operations.

(d) **Not** a subalgebra, because it is not even a subspace: (SA1) fails. Take \( N_1 = \E_{12} \) and \( N_2 = \E_{23} \), both squaring to \( 0 \). Their sum \( N = \E_{12} + \E_{23} \) has \( N^2 = \E_{13} \ne 0 \) and \( N^3 = 0 \), so \( N \) is not of the listed form: if \( N = c\,\id_V + M \) with \( M^2 = 0 \), then \( M = N - c\,\id_V \) and \( 0 = M^2 = N^2 - 2cN + c^2\id_V \), whose diagonal entries in the standard basis are all \( c^2 \); so \( c = 0 \), and then \( M = N \) with \( N^2 \ne 0 \).
:::

::: {#exr-associative-algebras-b2}
[B2: A commutant]

Let \( \D = \diag(1, 1, 2) \in M_3(\nQ) \). Compute \( \{\D\}' \) and its dimension, and compare it with \( \dim\nQ[\D] \). Hence show that \( \{\D\}' \ne \nQ[\D] \).
:::

::: {.solution}
As in @exm-three-commutants, \( \D\X = \X\D \) says \( (d_i - d_j)x_{ij} = 0 \) with \( (d_1, d_2, d_3) = (1,1,2) \). The coefficient vanishes exactly for \( (i,j) \in \{(1,1),(1,2),(2,1),(2,2),(3,3)\} \), so
\[
\{\D\}' = \left\{\begin{pmatrix} p & q & 0 \\ r & s & 0 \\ 0 & 0 & t\end{pmatrix}\right\} ,
\]
of dimension \( 5 \).

For \( \nQ[\D] \): the polynomial \( (x-1)(x-2) \) annihilates \( \D \), and no polynomial of degree \( 1 \) does, since \( a\I + b\D = 0 \) would give \( a + b = 0 \) and \( a + 2b = 0 \), hence \( a = b = 0 \). So \( m_{\D} = (x-1)(x-2) \) and \( \dim\nQ[\D] = 2 \) by @prp-polynomial-algebra-dimension. Since \( 5 \ne 2 \), the two algebras differ; concretely \( \E_{12} \in \{\D\}' \) is not a polynomial in \( \D \), because every such polynomial is diagonal.
:::

::: {#exr-associative-algebras-b3}
[B3: Cayley for the quaternions]

Let \( \nH \) be the quaternions with ordered basis \( \sB = (1, \i, \j, \k) \) over \( \nR \), where \( 1 \) denotes \( \I_2 \). Compute the matrices of \( L_{\i} \) and \( L_{\j} \) in \( \sB \), and verify that they satisfy \( L_{\i}^2 = -\I_4 \) and \( L_{\i}L_{\j} = L_{\k} \).
:::

::: {.solution}
By @def-quaternions, \( \i\cdot 1 = \i \), \( \i\i = -1 \), \( \i\j = \k \) and \( \i\k = -\j \). Writing the coordinate vectors of these four images as columns,
\[
\mtx{L_{\i}}{\sB}{\sB} =
\begin{pmatrix}
0 & -1 & 0 & 0 \\
1 & 0 & 0 & 0 \\
0 & 0 & 0 & -1 \\
0 & 0 & 1 & 0
\end{pmatrix} .
\]
Likewise \( \j\cdot 1 = \j \), \( \j\i = -\k \), \( \j\j = -1 \), \( \j\k = \i \), so
\[
\mtx{L_{\j}}{\sB}{\sB} =
\begin{pmatrix}
0 & 0 & -1 & 0 \\
0 & 0 & 0 & 1 \\
1 & 0 & 0 & 0 \\
0 & -1 & 0 & 0
\end{pmatrix} .
\]
Squaring the first gives \( -\I_4 \), and multiplying the two in this order gives the matrix with columns \( (0,0,0,1), (0,0,1,0), (0,-1,0,0), (-1,0,0,0) \), which is the matrix of \( L_{\k} \) computed the same way from \( \k\cdot 1 = \k \), \( \k\i = \j \), \( \k\j = -\i \), \( \k\k = -1 \). Both checks also follow from @thm-cayley-for-algebras without computing: \( L \) is multiplicative, so \( L_{\i}L_{\i} = L_{\i\i} = L_{-1} = -\I_4 \) and \( L_{\i}L_{\j} = L_{\i\j} = L_{\k} \). This exhibits \( \nH \) as a subalgebra of \( M_4(\nR) \).
:::

### C. Going deeper

::: {#exr-associative-algebras-c1}
[C1: The center of a group algebra]

Let \( G \) be a finite group and \( F \) a field. For \( g \in G \), the **conjugacy class** of \( g \) is \( K_g = \{hgh^{-1} : h \in G\} \), and the **class sum** is \( z_g = \sum_{k \in K_g} k \in F[G] \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( x = \sum_g a_g\,g \) lies in \( Z(F[G]) \) if and only if \( a_{hgh^{-1}} = a_g \) for all \( g, h \in G \).
2. Deduce that the distinct class sums form a basis of \( Z(F[G]) \), so that \( \dim Z(F[G]) \) is the number of conjugacy classes of \( G \).
3. Compute \( \dim Z(F[S_3]) \).
:::

*Hint for (a): by bilinearity it is enough to test commutation against the basis elements \( h \in G \).*
:::

::: {.solution}
(a) By bilinearity, \( x \) is central if and only if \( xh = hx \) for every \( h \in G \), equivalently \( h^{-1}xh = x \) for every \( h \) (multiply by \( h^{-1} \), which exists in \( G \)). Now
\[
h^{-1}xh = \sum_{g} a_g\,h^{-1}gh = \sum_{u} a_{huh^{-1}}\,u ,
\]
where the second equality substitutes \( u = h^{-1}gh \), that is, \( g = huh^{-1} \); this is a bijection of \( G \), so it merely relabels the sum. Comparing coefficients with \( x = \sum_u a_u u \), which is legitimate because the \( u \) are a basis, gives \( h^{-1}xh = x \) for all \( h \) exactly when \( a_{huh^{-1}} = a_u \) for all \( u, h \).

(b) Being conjugate is an equivalence relation on \( G \): \( g = ege^{-1} \); if \( g' = hgh^{-1} \) then \( g = h^{-1}g'(h^{-1})^{-1} \); and conjugating twice is conjugating by the product. So \( G \) is the disjoint union of its distinct classes \( K_1, \dots, K_r \). By (a), a central element has a constant coefficient on each class, so \( Z(F[G]) \) is exactly the span of the class sums \( z_1, \dots, z_r \); and these are independent, because they are sums over **disjoint** non-empty sets of basis vectors. Hence \( \dim Z(F[G]) = r \).

(c) Conjugate elements satisfy the same equations \( g^k = e \): expanding and canceling the inner pairs \( h^{-1}h \) gives \( (hgh^{-1})^k = hg^kh^{-1} \), which equals \( e \) exactly when \( g^k = e \). Now \( S_3 \) splits into three sets by this test: \( \{e\} \); the three transpositions, which are the elements with \( g^2 = e \ne g \); and the two \( 3 \)-cycles, which are the elements with \( g^3 = e \ne g \). No conjugacy class can meet two of these sets. Each of them is a single class: \( (1\ 3)(1\ 2)(1\ 3)^{-1} = (2\ 3) \) and \( (2\ 3)(1\ 2)(2\ 3)^{-1} = (1\ 3) \) make the three transpositions conjugate, and \( (1\ 2)(1\ 2\ 3)(1\ 2)^{-1} = (1\ 3\ 2) \) makes the two \( 3 \)-cycles conjugate. So \( r = 3 \) and \( \dim Z(F[S_3]) = 3 \).
:::

::: {#exr-associative-algebras-c2}
[C2: Generated by two matrix units]

Work in \( M_2(F) \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( F\langle\{\E_{12}\}\rangle \) and its dimension.
2. Compute \( F\langle\{\E_{12}, \E_{21}\}\rangle \) and its dimension.
3. Deduce that adding one generator can change the commutant from an algebra of dimension \( 2 \) to the scalars, and compute both commutants.
:::
:::

::: {.solution}
(a) \( \E_{12}^2 = 0 \), so by @prp-generated-is-span-of-words the generated algebra is \( \Span(\I_2, \E_{12}) \), of dimension \( 2 \). It is \( F[\E_{12}] \), which matches @prp-polynomial-algebra-dimension since \( m_{\E_{12}} = x^2 \).

(b) The words include \( \E_{12}\E_{21} = \E_{11} \) and \( \E_{21}\E_{12} = \E_{22} \), so the generated algebra contains all four matrix units and is \( M_2(F) \), of dimension \( 4 \).

(c) \( \{\E_{12}\}' \): writing \( \X = (x_{ij}) \), \( \E_{12}\X \) has first row \( (x_{21}, x_{22}) \) and second row zero, while \( \X\E_{12} \) has second column \( (x_{11}, x_{21}) \) and first column zero. Equality forces \( x_{21} = 0 \) and \( x_{22} = x_{11} \), so \( \{\E_{12}\}' = \Span(\I_2, \E_{12}) \), of dimension \( 2 \). By @prp-commutant-is-algebra (b), \( \{\E_{12}, \E_{21}\}' \subseteq \{\E_{12}\}' \), and it equals \( Z(M_2(F)) = F\I_2 \) by part (b) and @prp-center-of-matrix-algebra. One extra generator cuts the commutant from dimension \( 2 \) to dimension \( 1 \).
:::

::: {#exr-associative-algebras-c3}
[C3: Is the group algebra ever a field?]

Let \( G \) be a finite group with \( \lvert G\rvert \ge 2 \) and let \( F \) be any field.

::: {.enumerate options="label=(\alph*)"}
1. Pick \( g \ne e \) in \( G \) of order \( m \ge 2 \), meaning \( g^m = e \) and \( g^i \ne e \) for \( 1 \le i < m \). (Such an \( m \) exists: the powers \( g, g^2, \dots \) cannot all be distinct in a finite group, and canceling gives \( g^i = e \) for some \( i \ge 1 \).) Show that \( x = 1 - g \) and \( y = 1 + g + \dots + g^{m-1} \) satisfy \( xy = 0 \) with \( x \ne 0 \) and \( y \ne 0 \).
2. Deduce that \( F[G] \) is never a field, and never isomorphic to a subalgebra of a field.
3. Is \( F[G] \) ever commutative for \( \lvert G\rvert \ge 2 \)? Give an example or a proof that it is not.
:::
:::

::: {.solution}
(a) The powers \( 1, g, \dots, g^{m-1} \) are distinct elements of \( G \): if \( g^i = g^j \) with \( 0 \le i < j \le m-1 \) then \( g^{j-i} = e \) with \( 1 \le j - i < m \), contradicting minimality of \( m \) (cancellation is @thm-group-basic-properties (4)). So \( x \ne 0 \) and \( y \ne 0 \), both being non-zero combinations of distinct basis vectors. Expanding,
\[
xy = \sum_{i=0}^{m-1} g^i - \sum_{i=0}^{m-1} g^{i+1} = 1 - g^m = 1 - 1 = 0 .
\]

(b) In a field, and more generally in any subalgebra of a field, a product of two non-zero elements is non-zero: if \( xy = 0 \) and \( x \ne 0 \) then \( y = x^{-1}(xy) = 0 \). Part (a) produces a violation, so \( F[G] \) is not a field and embeds in none. (An algebra with such a pair \( x, y \) is said to have *zero divisors*.)

(c) Yes, whenever \( G \) is abelian: then \( g_ig_j = g_jg_i \) on basis elements, and bilinearity extends the identity to all of \( F[G] \). For example \( F[\nZ/2\nZ] \) is commutative of dimension \( 2 \). Part (b) says it is still not a field, which is consistent: \( \nQ[\nZ/2\nZ] \cong \nQ \times \nQ \), a commutative algebra with zero divisors.
:::
