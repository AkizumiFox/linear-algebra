# Projective Transformations

Section 06 built \( \nP(V) \) out of the lines through the origin of \( V \), and a construction is only as good as the maps that go with it. Here the maps are already in hand: an invertible linear operator sends lines through the origin to lines through the origin, so it permutes the points of \( \nP(V) \). This section shows that two operators give the same permutation exactly when they differ by a non-zero scalar, that such a map is pinned down by its values on \( n + 2 \) points in general position — and, over any field with more than two elements, **not** on \( n + 1 \) — and that the failure at \( n + 1 \) is precisely what makes the cross-ratio of four points on a line a genuine invariant.

Throughout, \( F \) is an arbitrary field and \( V \), \( W \) are finite-dimensional vector spaces over \( F \). Nothing in this section needs a characteristic assumption, an ordering or an inner product. In \( F^{n+1} \) we index coordinates from \( 0 \), writing \( \x = (x_0, x_1, \dots, x_n) \) and \( \e_0, \dots, \e_n \) for the standard basis, so that homogeneous coordinates read \( [x_0 : x_1 : \dots : x_n] \) as in @def-homogeneous-coordinates. We write \( F^{\times} = F \setminus \{0\} \) for the multiplicative group of \( F \) (@exm-groups), and \( \GL(V) \) for the set of invertible linear operators \( V \to V \); composition makes \( \GL(V) \) a group (@def-group), with identity \( \id_V \), exactly as it makes \( \GL_n(F) \) one.

## Maps induced by linear isomorphisms

We need maps \( \nP(V) \to \nP(W) \), and the only structure a projective space has is its supply of points, that is, of one-dimensional subspaces (@def-projective-space). So we want maps that carry one-dimensional subspaces to one-dimensional subspaces. A linear map \( T \) does this as soon as it kills nothing: \( T(\Span(\x)) = \Span(T\x) \), and the right-hand side is a line precisely when \( T\x \ne \0 \).

*A projective transformation is an invertible linear map, read on lines instead of on vectors.*

::: {#def-projective-transformation}
[Projective Transformation]

Let \( T \colon V \to W \) be an **isomorphism** of vector spaces over \( F \). The **projective transformation**, or **projectivity**, induced by \( T \) is the map
\[
[T] \colon \nP(V) \to \nP(W), \qquad [T]\bigl([\x]\bigr) \coloneqq [T\x] .
\]
A map \( \nP(V) \to \nP(W) \) is a projectivity if it equals \( [T] \) for **some** isomorphism \( T \).
:::

Two things must be checked before the formula means anything, and both use invertibility. First, \( [T\x] \) has to be a point at all: a point of \( \nP(W) \) is \( [\w] \) for a **non-zero** \( \w \), and if \( \x \ne \0 \) then \( T\x \ne \0 \), because \( T \) is injective (@thm-injective-iff-trivial-kernel). Second, the recipe must not depend on the representative: if \( [\x] = [\y] \), then \( \y = \lambda\x \) for some \( \lambda \in F^{\times} \) (@def-homogeneous-coordinates), so \( T\y = \lambda\, T\x \) and \( [T\y] = [T\x] \).

::: {#prp-projectivity-basic}
[Projectivities Compose and Invert]

Let \( T \colon V \to W \) and \( S \colon W \to X \) be isomorphisms of finite-dimensional vector spaces over \( F \). Then \( [S] \circ [T] = [ST] \), the map \( [T] \) is a bijection with inverse \( [T^{-1}] \), and \( [\id_V] = \id_{\nP(V)} \).
:::

::: {.proof}
For \( \x \in V \) with \( \x \ne \0 \), \( \bigl([S] \circ [T]\bigr)([\x]) = [S(T\x)] = [(ST)\x] = [ST]([\x]) \), and \( ST \) is an isomorphism as a composition of isomorphisms (@thm-isomorphic-equivalence-relation). Taking \( S = T^{-1} \) gives \( [T^{-1}] \circ [T] = [\id_V] \), and \( [\id_V]([\x]) = [\x] \), so \( [\id_V] = \id_{\nP(V)} \); taking the composition in the other order gives \( [T] \circ [T^{-1}] = \id_{\nP(W)} \). Hence \( [T] \) is a bijection with inverse \( [T^{-1}] \).
:::

**Examples.** Take \( V = W = F^{n+1} \), so that a projectivity of \( \nP^n(F) \) is \( [\x] \mapsto [\A\x] \) for an invertible \( \A \in \GL_{n+1}(F) \).

- \( \A = \I_{n+1} \) gives the identity, and so does \( \A = \lambda\I_{n+1} \) for any \( \lambda \ne 0 \), since \( [\lambda\x] = [\x] \). This degenerate case is the whole content of the next subsection.
- On \( \nP^1(F) \), the matrix \( \A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) sends \( [x_0 : x_1] \) to \( [x_1 : x_0] \). In the chart \( x_1 \ne 0 \), where \( [t : 1] \) is the scalar \( t \), this is \( t \mapsto 1/t \) for \( t \ne 0 \), and it exchanges \( [1 : 0] \) with \( [0 : 1] \). A projectivity repairs the one defect of \( t \mapsto 1/t \): on the projective line there is no missing value.
- On \( \nP^2(F) \), a permutation matrix permutes the three coordinate points \( [1:0:0] \), \( [0:1:0] \), \( [0:0:1] \).

**Non-example by minimal change.** Drop invertibility. On \( \nP^1(F) \) put \( \A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \). For \( [1 : 0] \) the recipe gives \( [1 : 0] \), which is fine; but \( \A(0, 1) = (0, 0) \), and \( [\0] \) is not a point of \( \nP^1(F) \). The formula fails on exactly the points of \( \nP(\ker \A) \), and injectivity is the clause that rules them out. The recipe does still make sense on the remaining points \( [1 : t] \), but it is no longer injective there: \( \A(1, t) = (1, 0) \) for every \( t \), so all of them go to the single point \( [1:0] \).

Projectivities respect everything \( \nP(V) \) is made of.

::: {#prp-projectivity-preserves-subspaces}
[Projectivities Preserve Subspaces, Joins and Meets]

Let \( T \colon V \to W \) be an isomorphism and let \( U \) be a subspace of \( V \). Then
\[
[T]\bigl(\nP(U)\bigr) = \nP(T(U)) ,
\]
a projective subspace of \( \nP(W) \) of the same dimension as \( \nP(U) \), and the restriction of \( [T] \) to \( \nP(U) \) is the projectivity induced by the isomorphism \( T|_U \colon U \to T(U) \). Consequently \( [T] \) preserves inclusion, intersections and joins of projective subspaces.
:::

::: {.proof}
By @def-projective-subspace, \( \nP(U) = \{[\u] : \u \in U,\ \u \ne \0\} \) and \( \dim \nP(U) = \dim U - 1 \). A point of \( [T](\nP(U)) \) is \( [T\u] \) with \( \0 \ne \u \in U \), and these are exactly the points \( [\w] \) with \( \0 \ne \w \in T(U) \), since \( T \) is a bijection from \( U \) onto \( T(U) \). Hence \( [T](\nP(U)) = \nP(T(U)) \). The restriction \( T|_U \) is linear and injective with image \( T(U) \), hence an isomorphism onto \( T(U) \), so \( \dim T(U) = \dim U \) (@thm-isomorphic-iff-same-dimension) and the two projective subspaces have equal dimension; and \( [T|_U] \) agrees with \( [T] \) on \( \nP(U) \) by the same formula.

For the last sentence, \( T \) preserves inclusion of subspaces and satisfies \( T(U_1 \cap U_2) = T(U_1) \cap T(U_2) \) and \( T(U_1 + U_2) = T(U_1) + T(U_2) \), the first because \( T \) is injective and the second because \( T \) is linear and surjective onto its image. Passing to projective subspaces, inclusion transfers in both directions by @lem-projective-subspace-determines-subspace, intersections by @prp-join-and-meet (a) and joins by @prp-join-and-meet (b), in each case applied on both sides of \( T \).
:::

## The projective linear group

Different matrices can induce the same projectivity: \( \I_2 \) and \( 2\I_2 \) both act as the identity on \( \nP^1(\nQ) \). The next theorem says that this is the only way it happens, and it is the reason the group of projectivities is smaller than \( \GL \).

::: {#thm-pgl}
[Projectivities and Scalars]

Let \( \dim V = \dim W \ge 1 \) and let \( S, T \colon V \to W \) be isomorphisms.

::: {.enumerate options="label=(\alph*)"}
1. \( [S] = [T] \) if and only if \( S = \lambda T \) for some \( \lambda \in F^{\times} \).
2. The set \( \operatorname{PGL}(V) \coloneqq \{[T] : T \in \GL(V)\} \) of projectivities of \( \nP(V) \) is a group under composition, the **projective linear group** of \( V \).
3. The map \( \Pi \colon \GL(V) \to \operatorname{PGL}(V) \), \( T \mapsto [T] \), is a surjective group homomorphism, and \( \ker \Pi = \{\lambda\,\id_V : \lambda \in F^{\times}\} \).
:::
:::

For \( V = F^{n+1} \) we write \( \operatorname{PGL}_{n+1}(F) \) for \( \operatorname{PGL}(F^{n+1}) \); part (a) then says that \( \A, \B \in \GL_{n+1}(F) \) induce the same projectivity of \( \nP^n(F) \) exactly when \( \B = \lambda\A \) for some \( \lambda \ne 0 \).

::: {.idea}
One direction is the computation \( [\lambda T\x] = [T\x] \). For the other, put \( R = T^{-1}S \), so that the hypothesis says \( [R\x] = [\x] \) for every \( \x \ne \0 \): **every non-zero vector is an eigenvector of \( R \)**. That is far stronger than it looks. Test it on \( \x \), \( \y \) and \( \x + \y \): if \( \x \) and \( \y \) are independent, comparing coefficients forces their eigenvalues to agree, and if they are dependent, the eigenvalue is forced directly. So \( R \) is a scalar. Parts (b) and (c) are then bookkeeping with @prp-projectivity-basic.
:::

::: {.proof}
(a) \( (\Leftarrow) \) If \( S = \lambda T \) with \( \lambda \ne 0 \), then for every \( \x \ne \0 \) we have \( S\x = \lambda(T\x) \), so \( [S\x] = [T\x] \) by @def-homogeneous-coordinates. Hence \( [S] = [T] \).

\( (\Rightarrow) \) Suppose \( [S] = [T] \). Put \( R = T^{-1}S \in \GL(V) \). For every \( \x \ne \0 \), \( [S\x] = [T\x] \) gives \( S\x = \mu\, T\x \) for some \( \mu \in F^{\times} \), hence \( R\x = T^{-1}S\x = \mu\x \). So for each \( \x \ne \0 \) there is a scalar \( \lambda_{\x} \in F^{\times} \) with \( R\x = \lambda_{\x}\x \).

We show \( \lambda_{\x} \) does not depend on \( \x \). Let \( \x, \y \ne \0 \).

*Case 1: \( (\x, \y) \) is dependent.* Take a dependence \( s\x + t\y = \0 \) with \( s, t \) not both zero. If \( t = 0 \) then \( s \ne 0 \) and \( \x = \0 \), which is false; so \( t \ne 0 \) and \( \y = c\x \) with \( c = -s/t \), and \( c \ne 0 \) because \( \y \ne \0 \). Then
\[
\lambda_{\y}\y = R\y = cR\x = c\lambda_{\x}\x = \lambda_{\x}\y ,
\]
and \( \y \ne \0 \) gives \( \lambda_{\y} = \lambda_{\x} \).

*Case 2: \( (\x, \y) \) is independent.* Then \( \x + \y \ne \0 \), and
\[
\lambda_{\x+\y}\x + \lambda_{\x+\y}\y = R(\x + \y) = R\x + R\y = \lambda_{\x}\x + \lambda_{\y}\y .
\]
Independence lets us compare coefficients, giving \( \lambda_{\x} = \lambda_{\x+\y} = \lambda_{\y} \).

So there is one scalar \( \lambda \in F^{\times} \) with \( R\x = \lambda\x \) for all \( \x \ne \0 \), and also for \( \x = \0 \). Hence \( R = \lambda\,\id_V \) and \( S = TR = \lambda T \).

(b) By @prp-projectivity-basic, \( \operatorname{PGL}(V) \) is closed under composition and under inverses and contains \( \id_{\nP(V)} = [\id_V] \); composition of maps is associative. So (G1)–(G3) of @def-group hold.

(c) Surjectivity is the definition of \( \operatorname{PGL}(V) \), and \( \Pi(ST) = [ST] = [S][T] = \Pi(S)\Pi(T) \) by @prp-projectivity-basic, so \( \Pi \) is a homomorphism (@def-group-homomorphism). Its kernel is \( \{T : [T] = [\id_V]\} \), which by (a) is \( \{\lambda\,\id_V : \lambda \in F^{\times}\} \). This proves the theorem.
:::

::: {.remark}
Part (c) is the sentence "\( \operatorname{PGL}(V) \) is \( \GL(V) \) modulo scalars", made precise without quotient groups, which this book has not built. By (a), the fiber of \( \Pi \) over \( [T] \) is \( \{\lambda T : \lambda \in F^{\times}\} \), and the fibers of any map partition its domain. The picture is the one Chapter 3 drew for the cosets \( \v + U \) of @def-coset, with multiplication in place of addition and @lem-coset-equality replaced by part (a) above.
:::

::: {.warning}
**A projectivity has no determinant, no trace and no eigenvalues.** Only a matrix has those, and a projectivity of \( \nP^n(F) \) is a matrix only up to a scalar. On \( \nP^2(\nQ) \), the matrices \( \I_3 \) and \( 2\I_3 \) induce the same projectivity but have determinants \( 1 \) and \( 8 \), and traces \( 3 \) and \( 6 \). In general \( \det(\lambda\A) = \lambda^{n+1}\det\A \), so the most one can hope to define is \( \det \A \) modulo \( (n+1) \)-th powers. What **is** well defined is a fixed point: \( [\A\x] = [\x] \) says \( \x \) is an eigenvector of \( \A \), and being an eigenvector does not depend on scaling \( \A \).
:::

## Frames, and how many points pin a projectivity down

A linear map is determined by its values on a basis. A projectivity of \( \nP^n(F) \) is induced by an \( (n+1) \times (n+1) \) matrix, which has \( n + 1 \) columns, so the first guess is that \( n + 1 \) points should determine it. Over any field with more than two elements the guess is wrong — the two-element field is a genuine exception, and we return to it below — and the reason is visible in @thm-pgl: knowing \( [\A\e_i] \) fixes each column of \( \A \) only up to its own scalar, which leaves \( n + 1 \) unknown scalars, while changing \( \A \) to \( \lambda\A \) costs only one. One extra point supplies the missing information.

First, the hypothesis under which the extra point helps.

::: {#def-general-position}
[General Position]

Let \( \dim V = n + 1 \). A list \( P_1, \dots, P_m \) of points of \( \nP(V) \) is **in general position** if for **every** subset \( I \subseteq \{1, \dots, m\} \) with \( \lvert I \rvert \le n + 1 \), and any choice of representatives \( \v_i \) with \( P_i = [\v_i] \), the list \( (\v_i)_{i \in I} \) is linearly independent.
:::

The clause "any choice of representatives" costs nothing: replacing \( \v_i \) by \( c_i\v_i \) with \( c_i \ne 0 \) does not change whether a list is independent, so the condition may be tested on one choice. For \( m = n + 2 \), which is the case we need, general position says exactly that **every \( n + 1 \) of the points have independent representatives**; no subset of size \( n + 2 \) can be independent in an \( (n+1) \)-dimensional space, which is why the bound \( \lvert I \rvert \le n + 1 \) is there.

**Examples.** In \( \nP^2(F) \), the four points \( [1:0:0] \), \( [0:1:0] \), \( [0:0:1] \), \( [1:1:1] \) are in general position: the first three representatives form a basis, and any three of the four are independent, since each of the other three triples has determinant \( \pm 1 \). In \( \nP^1(F) \), general position for three points means simply that they are pairwise distinct. The same holds in every dimension: the \( n + 2 \) points \( [\e_0], \dots, [\e_n] \), \( [1 : \dots : 1] \) of \( \nP^n(F) \) are in general position. Indeed \( n+1 \) of the representatives \( \e_0, \dots, \e_n, (1, \dots, 1) \) are either the \( \e_i \) themselves, with determinant \( 1 \), or all of them but one, say \( \e_j \), together with \( (1, \dots, 1) \); in that matrix row \( j \) is zero except for the entry \( 1 \) in the last column, and expanding along row \( j \) leaves the determinant of a permutation matrix, so the value is \( \pm 1 \). In \( \nP^n(F) \), a single point is always in general position, since one non-zero vector is independent.

**Non-example by minimal change.** Replace \( [1:1:1] \) by \( [1:1:0] \). The list \( [1:0:0] \), \( [0:1:0] \), \( [0:0:1] \), \( [1:1:0] \) fails: the subset \( \{1, 2, 4\} \) has representatives \( (1,0,0) \), \( (0,1,0) \), \( (1,1,0) \), and the third is the sum of the first two. Geometrically, three of the four points are collinear. No projectivity carries the first list to this one: a projectivity preserves joins and their dimensions (@prp-projectivity-preserves-subspaces), and here \( [1:0:0] \vee [0:1:0] \vee [1:1:0] \) is a line, while \( [1:0:0] \vee [0:1:0] \vee [1:1:1] \) is the whole plane.

The key step is that general position lets us choose representatives once and for all.

::: {#lem-projective-frame-normalization}
[Normalizing a Frame]

Let \( \dim V = n + 1 \ge 1 \) and let \( P_1, \dots, P_{n+2} \) be points of \( \nP(V) \) in general position. Then there are representatives \( \v_i \) with \( P_i = [\v_i] \) such that
\[
(\v_1, \dots, \v_{n+1}) \text{ is a basis of } V \qquad\text{and}\qquad \v_{n+2} = \v_1 + \dots + \v_{n+1} .
\]
Moreover such a list is unique up to one common scalar: if \( (\v'_1, \dots, \v'_{n+2}) \) is another, then \( \v'_i = a\v_i \) for all \( i \), with a single \( a \in F^{\times} \).
:::

::: {.idea}
Start from arbitrary representatives \( \u_i \). The first \( n+1 \) form a basis, so \( \u_{n+2} \) has coordinates \( c_1, \dots, c_{n+1} \) in it. General position is exactly the statement that **no coordinate is zero**: a vanishing \( c_j \) would put \( \u_{n+2} \) in the span of the other \( n \) basis vectors, making \( n+1 \) of our points dependent. Non-zero coordinates can be absorbed into the basis vectors, and then the last vector is the sum of the others. For uniqueness, write the second list as \( a_i\v_i \) and read off from the relation \( \sum \v_i = \v_{n+2} \) that all \( a_i \) coincide.
:::

::: {.proof}
Choose any representatives \( \u_i \) with \( P_i = [\u_i] \). By @def-general-position the list \( (\u_1, \dots, \u_{n+1}) \) is independent, and it has \( n + 1 = \dim V \) entries, so it is a basis of \( V \) (@thm-right-size-basis). Write
\[
\u_{n+2} = c_1\u_1 + \dots + c_{n+1}\u_{n+1}, \qquad c_i \in F .
\]
*Every \( c_j \) is non-zero.* Suppose \( c_j = 0 \) for some \( j \le n+1 \). Then
\[
1 \cdot \u_{n+2} - \sum_{i \ne j,\ i \le n+1} c_i\u_i = \0
\]
is a linear relation whose coefficient on \( \u_{n+2} \) is \( 1 \ne 0 \), so the list consisting of \( \u_{n+2} \) together with the \( n \) vectors \( \u_i \) (\( i \ne j \), \( i \le n+1 \)) is dependent (@def-linear-independence). It has \( n + 1 \) entries and its index set has \( n + 1 \) elements, contradicting @def-general-position.

Now set \( \v_i \coloneqq c_i\u_i \) for \( i \le n+1 \) and \( \v_{n+2} \coloneqq \u_{n+2} \). Each \( c_i \ne 0 \), so \( [\v_i] = [\u_i] = P_i \), and \( (\v_1, \dots, \v_{n+1}) \) is still a basis, being the old basis with each vector scaled by a non-zero scalar. By construction \( \v_{n+2} = \sum_{i=1}^{n+1} c_i\u_i = \sum_{i=1}^{n+1}\v_i \).

*Uniqueness.* Let \( (\v'_1, \dots, \v'_{n+2}) \) be another such list. Since \( [\v'_i] = P_i = [\v_i] \), there are \( a_i \in F^{\times} \) with \( \v'_i = a_i\v_i \). Applying the defining relation to both lists,
\[
a_{n+2}\sum_{i=1}^{n+1}\v_i = a_{n+2}\v_{n+2} = \v'_{n+2} = \sum_{i=1}^{n+1}\v'_i = \sum_{i=1}^{n+1} a_i\v_i .
\]
The list \( (\v_1, \dots, \v_{n+1}) \) is independent, so comparing coefficients gives \( a_i = a_{n+2} \) for every \( i \le n+1 \). Hence all \( a_i \) equal one scalar \( a \).
:::

The theorem is now three lines of linear algebra.

::: {#thm-fundamental-theorem-of-projective-geometry}
[Fundamental Theorem of Projective Geometry]

Let \( \dim V = \dim W = n + 1 \ge 1 \). Let \( P_1, \dots, P_{n+2} \) be points of \( \nP(V) \) in general position and \( Q_1, \dots, Q_{n+2} \) points of \( \nP(W) \) in general position. Then there is **exactly one** projectivity \( f \colon \nP(V) \to \nP(W) \) with
\[
f(P_i) = Q_i \qquad \text{for } i = 1, \dots, n+2 .
\]
:::

::: {.idea}
Normalize both lists by @lem-projective-frame-normalization. The first \( n+1 \) normalized vectors on each side are bases, so there is a unique linear map sending one basis to the other, and the normalization was arranged so that this map automatically takes the \( (n+2) \)-nd vector to the \( (n+2) \)-nd. For uniqueness, a second projectivity differs from the first by an operator that scales each of \( \v_1, \dots, \v_{n+1} \) and also their sum; the same coefficient comparison as in the lemma forces all the scalars to agree.
:::

::: {.proof}
By @lem-projective-frame-normalization choose representatives \( \v_1, \dots, \v_{n+2} \) of the \( P_i \) with \( (\v_1, \dots, \v_{n+1}) \) a basis of \( V \) and \( \v_{n+2} = \v_1 + \dots + \v_{n+1} \), and likewise \( \w_1, \dots, \w_{n+2} \) for the \( Q_i \).

*Existence.* By @thm-linear-transform-basis there is a unique linear \( T \colon V \to W \) with \( T\v_i = \w_i \) for \( i \le n+1 \). Its image is \( \Span(\w_1, \dots, \w_{n+1}) = W \) by @thm-image-spanned-by-basis-images, so \( T \) is surjective, and since \( \dim V = \dim W \) is finite, \( T \) is an isomorphism by @cor-rank-nullity-consequences (e). By linearity,
\[
T\v_{n+2} = T\Bigl(\sum_{i=1}^{n+1}\v_i\Bigr) = \sum_{i=1}^{n+1}\w_i = \w_{n+2} .
\]
Hence \( [T](P_i) = [T\v_i] = [\w_i] = Q_i \) for all \( i \le n+2 \).

*Uniqueness.* Let \( [S] \) be a projectivity with \( [S](P_i) = Q_i \) for all \( i \), where \( S \colon V \to W \) is an isomorphism. Then \( [S\v_i] = [\w_i] \), so there are \( \mu_i \in F^{\times} \) with \( S\v_i = \mu_i\w_i \). Put \( R = T^{-1}S \in \GL(V) \); then \( R\v_i = \mu_i\v_i \) for every \( i \le n+2 \). Applying \( R \) to \( \v_{n+2} = \sum_{i \le n+1}\v_i \),
\[
\mu_{n+2}\sum_{i=1}^{n+1}\v_i = R\v_{n+2} = \sum_{i=1}^{n+1} R\v_i = \sum_{i=1}^{n+1}\mu_i\v_i .
\]
By independence of \( (\v_1, \dots, \v_{n+1}) \), \( \mu_i = \mu_{n+2} \eqqcolon \mu \) for all \( i \le n+1 \). So \( R \) agrees with \( \mu\,\id_V \) on a basis, hence \( R = \mu\,\id_V \) (@thm-linear-transform-basis), and \( S = TR = \mu T \). By @thm-pgl (a), \( [S] = [T] \). This proves the theorem.
:::

Existence and uniqueness are both used constantly: existence says we may always **choose coordinates** so that \( n+2 \) prescribed points in general position become \( [\e_0], \dots, [\e_n] \) and \( [1 : \dots : 1] \); uniqueness says that having done so, nothing is left to choose.

::: {#exm-projectivity-from-four-points}
[Moving the standard frame]

Work in \( \nP^2(\nQ) \). Find the projectivity carrying
\[
[1:0:0],\quad [0:1:0],\quad [0:0:1],\quad [1:1:1]
\]
to
\[
Q_0 = [1:1:0],\quad Q_1 = [0:1:1],\quad Q_2 = [1:0:1],\quad Q_3 = [4:3:5],
\]
after checking that the second list is in general position.
:::

::: {.solution}
*General position.* Form the \( 3 \times 3 \) determinant of each triple of representatives, taken as columns. For the triples \( (Q_0, Q_1, Q_2) \), \( (Q_0, Q_1, Q_3) \), \( (Q_0, Q_2, Q_3) \), \( (Q_1, Q_2, Q_3) \) these determinants are \( 2 \), \( 6 \), \( -4 \), \( 2 \). All are non-zero in \( \nQ \), so every triple is independent (@thm-det-nonzero-iff-invertible together with the fact that the columns of an invertible matrix are independent), and the four points are in general position.

*Normalizing.* Following @lem-projective-frame-normalization, we need scalars \( \lambda_0, \lambda_1, \lambda_2 \) with
\[
\lambda_0(1,1,0) + \lambda_1(0,1,1) + \lambda_2(1,0,1) = (4,3,5),
\]
that is, \( \lambda_0 + \lambda_2 = 4 \), \( \lambda_0 + \lambda_1 = 3 \), \( \lambda_1 + \lambda_2 = 5 \). Adding all three gives \( \lambda_0 + \lambda_1 + \lambda_2 = 6 \), so \( \lambda_0 = 6 - 5 = 1 \), \( \lambda_1 = 6 - 4 = 2 \), \( \lambda_2 = 6 - 3 = 3 \). All are non-zero, as the lemma promised.

*The matrix.* The standard frame is already normalized, with \( \e_0 + \e_1 + \e_2 = (1,1,1) \). So the map sends \( \e_i \) to \( \lambda_i\q_i \), that is,
\[
\A = \begin{pmatrix} 1 & 0 & 3 \\ 1 & 2 & 0 \\ 0 & 2 & 3 \end{pmatrix},
\qquad \det \A = 12 \ne 0 .
\]
*Check.* The columns are \( (1,1,0) \), \( (0,2,2) \), \( (3,0,3) \), which represent \( Q_0 \), \( Q_1 \), \( Q_2 \); and \( \A(1,1,1) = (4,3,5) \), which represents \( Q_3 \). By @thm-fundamental-theorem-of-projective-geometry this \( [\A] \) is the only projectivity doing this, so every other matrix that works is a scalar multiple of \( \A \).
:::

Now the negative result promised above. It is not that the proof of @thm-fundamental-theorem-of-projective-geometry is wasteful; as long as \( F \) has more than two elements, \( n+1 \) points genuinely do not suffice.

::: {#prp-stabilizer-of-coordinate-points}
[What Fixes the Coordinate Points]

Let \( n \ge 1 \). A projectivity of \( \nP^n(F) \) fixes each of the \( n+1 \) points \( [\e_0], \dots, [\e_n] \) if and only if it is \( [\D] \) for an invertible **diagonal** matrix \( \D \). The group of such projectivities is trivial if and only if \( F = \nF_2 \).
:::

::: {.proof}
\( (\Leftarrow) \) If \( \D = \diag(d_0, \dots, d_n) \) with all \( d_i \ne 0 \), then \( \D\e_i = d_i\e_i \), so \( [\D][\e_i] = [\e_i] \).

\( (\Rightarrow) \) Let \( [\A] \) fix each \( [\e_i] \). Then \( \A\e_i = d_i\e_i \) for some \( d_i \in F^{\times} \). But \( \A\e_i \) is the \( i \)-th column of \( \A \) (@thm-three-views-of-product), so every column of \( \A \) has a single non-zero entry, on the diagonal: \( \A = \diag(d_0, \dots, d_n) \).

For the last sentence, by @thm-pgl (a) we have \( [\D] = [\I_{n+1}] \) if and only if \( \D = \lambda\I_{n+1} \), that is, if and only if \( d_0 = \dots = d_n \). So the group is trivial exactly when every tuple \( (d_0, \dots, d_n) \in (F^{\times})^{n+1} \) is constant, which, since \( n \ge 1 \), happens exactly when \( F^{\times} \) has one element, that is, when \( F = \nF_2 \).
:::

::: {.remark}
**\( n+1 \) points do not determine a projectivity.** Let \( F \) have an element \( c \ne 0, 1 \) — every field except \( \nF_2 \). In \( \nP^1(F) \) the two points \( [1:0] \) and \( [0:1] \) are in general position, and both \( [\I_2] \) and \( [\diag(1, c)] \) fix them, yet they are different maps: the second sends \( [1:1] \) to \( [1:c] \ne [1:1] \). The same works in \( \nP^n(F) \) with \( \D = \diag(1, \dots, 1, c) \) and the point \( [1 : \dots : 1] \). So the count of \( n+2 \) in @thm-fundamental-theorem-of-projective-geometry is exact.

Over \( \nF_2 \) this counterexample is unavailable, and @prp-stabilizer-of-coordinate-points already shows why: the group it describes is trivial there. So the negative result needs the hypothesis that \( F \) has at least three elements, and over the one excluded field the situation is genuinely different.
:::

::: {#prp-two-element-field-exception}
[Over the Two-Element Field, \( n+1 \) Points Suffice]

Let \( n \ge 1 \) and \( F = \nF_2 \). Given two lists \( P_0, \dots, P_n \) and \( Q_0, \dots, Q_n \) of \( n+1 \) points of \( \nP^n(\nF_2) \), each in general position, there is exactly one projectivity of \( \nP^n(\nF_2) \) carrying \( P_i \) to \( Q_i \) for every \( i \).
:::

::: {.proof}
Over \( \nF_2 \) the only non-zero scalar is \( 1 \), so each point has exactly one representative: write \( P_i = [\v_i] \) and \( Q_i = [\w_i] \). By @def-general-position the lists \( (\v_0, \dots, \v_n) \) and \( (\w_0, \dots, \w_n) \) are independent, and each has \( n+1 = \dim \nF_2^{n+1} \) entries, hence each is a basis (@thm-right-size-basis). By @thm-linear-transform-basis there is a unique linear \( T \) with \( T\v_i = \w_i \) for all \( i \); its image is \( \Span(\w_0, \dots, \w_n) = \nF_2^{n+1} \) (@thm-image-spanned-by-basis-images), so it is surjective and hence an isomorphism (@cor-rank-nullity-consequences (e)). Thus \( [T] \) carries \( P_i \) to \( Q_i \).

If \( [S] \) does too, then \( [S\v_i] = [\w_i] \), so \( S\v_i = \mu_i\w_i \) with \( \mu_i \in \nF_2 \setminus \{0\} = \{1\} \), that is, \( S\v_i = \w_i = T\v_i \) for every \( i \). Two linear maps agreeing on a basis are equal (@thm-linear-transform-basis), so \( S = T \) and \( [S] = [T] \).
:::

So the theorem to remember is @thm-fundamental-theorem-of-projective-geometry, with the count \( n+2 \) that works over every field; \( \nF_2 \) is the one field where a smaller count also works, for the accidental reason that it has no scalars to spare.

::: {.check}
Exhibit two different projectivities of \( \nP^2(\nQ) \) that agree on \( [1:0:0] \), \( [0:1:0] \) and \( [0:0:1] \), and name a point where they disagree.
:::

::: {.solution}
Take \( [\I_3] \) and \( [\D] \) with \( \D = \diag(1, 1, 2) \). Both fix the three coordinate points. They differ at \( [1:1:1] \), which \( [\D] \) sends to \( [1:1:2] \); and \( [1:1:2] \ne [1:1:1] \), since \( (1,1,2) \) is not a scalar multiple of \( (1,1,1) \). By @thm-pgl (a) the two projectivities are different, because \( \D \) is not a scalar multiple of \( \I_3 \).
:::

## The cross-ratio

Three distinct points on a projective line can be moved to any other three, by @thm-fundamental-theorem-of-projective-geometry with \( n = 1 \). A fourth point cannot: the theorem has used up all its freedom. What is left over is one invariant, and it is a point of \( \nP^1(F) \).

::: {#def-cross-ratio}
[Cross-Ratio]

Let \( L \) be a projective line, that is, a projective space of dimension \( 1 \) over \( F \), let \( A, B, C \in L \) be **pairwise distinct**, and let \( D \in L \) be arbitrary. Let \( f \colon L \to \nP^1(F) \) be the unique projectivity with
\[
f(A) = [1:0], \qquad f(B) = [0:1], \qquad f(C) = [1:1] .
\]
The **cross-ratio** of the ordered quadruple is the point
\[
(A, B; C, D) \coloneqq f(D) \in \nP^1(F) .
\]
:::

The projectivity \( f \) exists and is unique because three pairwise distinct points of a line are in general position (@def-general-position with \( n = 1 \)), on both sides. The cross-ratio is a **point of \( \nP^1(F) \)**, not a scalar; in the chart \( [\lambda : \mu] \mapsto \lambda/\mu \) it becomes a scalar whenever \( \mu \ne 0 \), and the one excluded value, \( [1:0] \), occurs exactly when \( D = A \), since \( f \) is injective. Likewise \( (A,B;C,D) = [0:1] \) exactly when \( D = B \), and \( [1:1] \) exactly when \( D = C \).

A formula makes this computable.

::: {#prp-cross-ratio-formula}
[Computing the Cross-Ratio]

In the situation of @def-cross-ratio, write \( L = \nP(U) \) with \( \dim U = 2 \), choose representatives \( A = [\a] \), \( B = [\b] \), and expand
\[
\c = c_1\a + c_2\b, \qquad \d = d_1\a + d_2\b
\]
for representatives \( \c \) of \( C \) and \( \d \) of \( D \). Then \( c_1 \ne 0 \), \( c_2 \ne 0 \), and
\[
(A, B; C, D) = [\, d_1c_2 : d_2c_1 \,] .
\]
If moreover \( L = \nP^1(F) \) and the four points lie in the chart \( \mu \ne 0 \), with scalars \( a, b, c, d \) given by \( [t : 1] \mapsto t \), then
\[
(A, B; C, D) = \Bigl[\, (c - a)(d - b) \,:\, (c - b)(d - a) \,\Bigr] .
\]
:::

::: {.idea}
Since \( A \ne B \), the pair \( (\a, \b) \) is a basis of \( U \), so the expansions exist. The projectivity of @def-cross-ratio is the one induced by the linear map sending \( c_1\a \mapsto \e_0 \) and \( c_2\b \mapsto \e_1 \), because that map sends \( \c \) to \( \e_0 + \e_1 \) — this is @lem-projective-frame-normalization for \( n = 1 \), done by hand. Then evaluate it at \( \d \). For the chart formula, take \( \a = (a, 1) \), \( \b = (b, 1) \) and solve two \( 2 \times 2 \) systems.
:::

::: {.proof}
The points \( A \ne B \) give independent representatives (@def-general-position), and \( \dim U = 2 \), so \( (\a, \b) \) is a basis of \( U \) (@thm-right-size-basis) and the expansions exist and are unique. If \( c_1 = 0 \) then \( \c = c_2\b \), so \( C = B \); if \( c_2 = 0 \) then \( C = A \). Both are excluded, so \( c_1c_2 \ne 0 \).

Let \( T \colon U \to F^2 \) be the linear map with \( T(c_1\a) = \e_0 \) and \( T(c_2\b) = \e_1 \) (@thm-linear-transform-basis; \( (c_1\a, c_2\b) \) is a basis since \( c_1c_2 \ne 0 \)). Its image is \( \Span(\e_0, \e_1) = F^2 \) (@thm-image-spanned-by-basis-images), so it is surjective, hence an isomorphism by @cor-rank-nullity-consequences (e). Then
\[
[T](A) = [T\a] = [c_1^{-1}\e_0] = [1:0], \qquad [T](B) = [0:1],
\]
and \( [T](C) = [T(c_1\a + c_2\b)] = [\e_0 + \e_1] = [1:1] \). By the uniqueness in @thm-fundamental-theorem-of-projective-geometry, \( [T] \) is the map \( f \) of @def-cross-ratio. Finally
\[
f(D) = [T(d_1\a + d_2\b)] = \bigl[\, d_1c_1^{-1}\e_0 + d_2c_2^{-1}\e_1 \,\bigr] = \bigl[\, d_1c_1^{-1} : d_2c_2^{-1} \,\bigr],
\]
and multiplying both entries by \( c_1c_2 \ne 0 \) gives \( [\,d_1c_2 : d_2c_1\,] \).

For the chart formula take \( \a = (a, 1) \), \( \b = (b, 1) \), \( \c = (c, 1) \), \( \d = (d, 1) \); these are representatives of the four points, and \( a \ne b \) because \( A \ne B \). Solving \( c_1a + c_2b = c \), \( c_1 + c_2 = 1 \) gives
\[
c_1 = \frac{c - b}{a - b}, \qquad c_2 = \frac{a - c}{a - b},
\]
and the same computation with \( d \) in place of \( c \) gives \( d_1 \), \( d_2 \). Hence
\[
\begin{aligned}
d_1c_2 &= \frac{(d - b)(a - c)}{(a - b)^2}, &
d_2c_1 &= \frac{(a - d)(c - b)}{(a - b)^2} ,
\end{aligned}
\]
and clearing the common factor \( (a-b)^{-2} \) and the common sign gives \( (A,B;C,D) = [\,(c-a)(d-b) : (c-b)(d-a)\,] \), as claimed.
:::

::: {.check}
@prp-cross-ratio-formula insists that \( A \), \( B \) and \( C \) be pairwise distinct, but puts no condition at all on \( D \). Where in the proof is each of these used, and why is \( [\,d_1c_2 : d_2c_1\,] \) a point of \( \nP^1(F) \) for every \( D \)?
:::

::: {.solution}
\( A \ne B \) makes \( (\a, \b) \) independent, hence a basis, which is what lets \( \c \) and \( \d \) be expanded at all. \( C \ne A \) and \( C \ne B \) are what force \( c_2 \ne 0 \) and \( c_1 \ne 0 \), which is what makes \( (c_1\a, c_2\b) \) a basis and lets us divide by \( c_1 \) and \( c_2 \). For \( D \) nothing is needed: \( \d \ne \0 \), so \( (d_1, d_2) \ne (0,0) \), and since \( c_1c_2 \ne 0 \) the pair \( (d_1c_2, d_2c_1) \) is again not \( (0,0) \). So it names a point of \( \nP^1(F) \), whichever point \( D \) is.
:::

::: {#thm-cross-ratio-invariant}
[Invariance and Completeness of the Cross-Ratio]

Let \( L \) and \( L' \) be projective lines over \( F \).

::: {.enumerate options="label=(\alph*)"}
1. **(Invariance)** If \( g \colon L \to L' \) is a projectivity and \( A, B, C \in L \) are pairwise distinct, then for every \( D \in L \), \( \bigl(g(A), g(B); g(C), g(D)\bigr) = (A, B; C, D) \).
2. **(Completeness)** Let \( A, B, C \in L \) be pairwise distinct and \( A', B', C' \in L' \) pairwise distinct, and let \( D \in L \), \( D' \in L' \). Then there is a projectivity \( L \to L' \) carrying \( A, B, C, D \) to \( A', B', C', D' \) if and only if \( (A,B;C,D) = (A',B';C',D') \).
:::
:::

::: {.idea}
Both halves come from the uniqueness in @thm-fundamental-theorem-of-projective-geometry, with no computation. For (a), \( f \circ g^{-1} \) normalizes the image triple, so it **is** the normalizing map of that triple; evaluate it at \( g(D) \). For (b), let \( h \) be the unique projectivity matching the triples; by (a) it preserves the cross-ratio, and the cross-ratio determines the fourth point because the normalizing map is injective.
:::

::: {.proof}
(a) Let \( f \colon L \to \nP^1(F) \) be the projectivity of @def-cross-ratio for \( (A, B, C) \). Since \( g \) is a bijection (@prp-projectivity-basic), \( g(A), g(B), g(C) \) are pairwise distinct, so the corresponding map \( f' \colon L' \to \nP^1(F) \) exists. The composition \( f \circ g^{-1} \colon L' \to \nP^1(F) \) is a projectivity (@prp-projectivity-basic) and sends \( g(A) \mapsto [1:0] \), \( g(B) \mapsto [0:1] \), \( g(C) \mapsto [1:1] \). By the uniqueness in @thm-fundamental-theorem-of-projective-geometry, \( f' = f \circ g^{-1} \). Hence
\[
\bigl(g(A), g(B); g(C), g(D)\bigr) = f'\bigl(g(D)\bigr) = f(D) = (A, B; C, D) .
\]

(b) \( (\Rightarrow) \) is (a). \( (\Leftarrow) \) Let \( h \colon L \to L' \) be the unique projectivity with \( h(A) = A' \), \( h(B) = B' \), \( h(C) = C' \) (@thm-fundamental-theorem-of-projective-geometry, \( n = 1 \)). Let \( f' \) be the normalizing map for \( (A', B', C') \). By (a),
\[
f'\bigl(h(D)\bigr) = (A', B'; C', h(D)) = (A, B; C, D) = (A', B'; C', D') = f'(D') .
\]
Since \( f' \) is injective, \( h(D) = D' \). This proves the theorem.
:::

So four points on a line carry exactly one piece of data that survives every projectivity, and two quadruples are projectively equivalent precisely when that datum agrees.

::: {#exm-cross-ratio-computation}
[A cross-ratio, before and after]

On \( \nP^1(\nQ) \), use the chart \( [t : 1] \mapsto t \) and take the points with parameters \( a = 0 \), \( b = 1 \), \( c = 3 \), \( d = 7 \). Compute \( (A, B; C, D) \). Then apply the projectivity \( [\A] \) with \( \A = \begin{pmatrix} 1 & 2 \\ 1 & 3 \end{pmatrix} \) and compute the cross-ratio of the images.
:::

::: {.solution}
By @prp-cross-ratio-formula,
\[
(A,B;C,D) = \bigl[\,(3-0)(7-1) : (3-1)(7-0)\,\bigr] = [18 : 14] = [9 : 7],
\]
which is the scalar \( 9/7 \) in the chart.

The matrix \( \A \) has \( \det \A = 3 - 2 = 1 \ne 0 \), so \( [\A] \) is a projectivity. It sends \( [t:1] \) to \( [t + 2 : t + 3] \), which lies in the chart when \( t \ne -3 \) and is then the scalar \( (t+2)/(t+3) \). The four parameters become
\[
0 \mapsto \tfrac23, \qquad 1 \mapsto \tfrac34, \qquad 3 \mapsto \tfrac56, \qquad 7 \mapsto \tfrac9{10} .
\]
The images are not equally spaced in any sense, and the gaps have changed from \( 1, 2, 4 \) to \( \tfrac1{12}, \tfrac1{12}, \tfrac1{15} \). The cross-ratio, however, is
\[
\Bigl[\bigl(\tfrac56 - \tfrac23\bigr)\bigl(\tfrac9{10} - \tfrac34\bigr) : \bigl(\tfrac56 - \tfrac34\bigr)\bigl(\tfrac9{10} - \tfrac23\bigr)\Bigr]
= \Bigl[\tfrac1{40} : \tfrac7{360}\Bigr] = [9 : 7],
\]
after multiplying both entries by \( 360 \). This is @thm-cross-ratio-invariant (a) in one instance.

As a second check, run @prp-cross-ratio-formula in its first form with \( \a = (0,1) \) and \( \b = (1,1) \): solving gives \( (c_1, c_2) = (-2, 3) \) and \( (d_1, d_2) = (-6, 7) \), so \( [\,d_1c_2 : d_2c_1\,] = [-18 : -14] = [9:7] \).
:::

::: {.warning}
**The cross-ratio depends on the order of the four points.** It is a function of an **ordered** quadruple. Swapping the first two points inverts it: with the notation of @prp-cross-ratio-formula, \( (B, A; C, D) = [\,d_2c_1 : d_1c_2\,] \), the two entries exchanged. With \( a, b, c, d = 0, 1, 3, 7 \) as above, \( (A,B;C,D) = [9:7] \) while \( (B,A;C,D) = [7:9] \), and \( 9/7 \ne 7/9 \). Writing "the cross-ratio of four points" without fixing an order names six different values in general.
:::

## Perspectivities

The classical source of projectivities is projection from a point, and it is worth seeing that the synthetic construction is the linear-algebraic one.

::: {#prp-perspectivity-is-projectivity}
[Projection From a Point Is a Projectivity]

Let \( \dim V = 3 \), let \( L = \nP(U) \) and \( L' = \nP(U') \) be lines in the projective plane \( \nP(V) \), and let \( O = [\o] \) be a point lying on neither. For \( P \in L \), let \( \pi(P) \) be the unique point in which the line \( O \vee P \) meets \( L' \). Then \( \pi \colon L \to L' \) is well defined, and it is the projectivity induced by the restriction to \( U \) of the projection of \( V \) onto \( U' \) along \( \Span(\o) \). In particular \( \pi \) preserves cross-ratio.
:::

::: {.idea}
Everything is forced by dimensions in a \( 3 \)-dimensional \( V \). Since \( \o \notin U' \) and \( \dim U' = 2 \), we have \( V = U' \oplus \Span(\o) \), so every vector splits uniquely as "a piece in \( U' \) plus a multiple of \( \o \)". Throwing away the multiple of \( \o \) is a linear map, and on \( U \) it is injective because \( \o \notin U \). That map is the projection, and the line \( O \vee P \) is exactly where the discarded multiple of \( \o \) lives.
:::

::: {.proof}
Since \( \o \ne \0 \) and \( \o \notin U' \), the sum \( U' + \Span(\o) \) properly contains \( U' \), so its dimension exceeds \( 2 \) and it equals \( V \). Since \( \dim U' + \dim\Span(\o) = 2 + 1 = 3 = \dim(U' + \Span(\o)) \), the sum is direct by @thm-direct-sum-criteria, so \( V = U' \oplus \Span(\o) \). Let \( \rho \colon V \to V \) be the projection onto \( U' \) along \( \Span(\o) \) (@thm-projection-direct-sum (b)), so that
\[
\x = \rho(\x) + t(\x)\,\o, \qquad \rho(\x) \in U',\ t(\x) \in F,
\]
is the unique such splitting, and \( \rho \) is linear.

*The restriction \( T \coloneqq \rho|_U \colon U \to U' \) is an isomorphism.* If \( \u \in U \) and \( \rho(\u) = \0 \), then \( \u = t(\u)\o \); since \( \o \notin U \), this forces \( t(\u) = 0 \) and \( \u = \0 \). So \( T \) is injective, and \( \dim U = \dim U' = 2 \) makes it an isomorphism (@cor-rank-nullity-consequences (e)).

*\( [T] = \pi \).* Let \( P = [\u] \) with \( \0 \ne \u \in U \). Since \( \o \notin U \), the vector \( \o \) is not a multiple of \( \u \), so \( \Span(\u, \o) \) has dimension \( 2 \). The projective subspace \( \nP(\Span(\u, \o)) \) contains \( O \) and \( P \), and any projective subspace \( \nP(W) \) containing both has \( \u, \o \in W \), hence \( \Span(\u, \o) \subseteq W \); so \( O \vee P = \nP(\Span(\u, \o)) \), a line. Now \( T\u = \u - t(\u)\o \in \Span(\u, \o) \cap U' \), and \( T\u \ne \0 \), so \( [T\u] \) lies on both \( O \vee P \) and \( L' \). These two lines are distinct, because \( O \) lies on the first and not on the second, so
\[
\dim\bigl(\Span(\u,\o) \cap U'\bigr) = 2 + 2 - \dim\bigl(\Span(\u,\o) + U'\bigr) = 4 - 3 = 1
\]
by @thm-dimension-formula-subspace-dim, the sum being all of \( V \) since it properly contains \( U' \). Hence the intersection point is unique and equals \( [T\u] \). So \( \pi \) is well defined and \( \pi = [T] \), a projectivity. Cross-ratio invariance is @thm-cross-ratio-invariant (a).
:::

\begin{center}
\begin{tikzpicture}[scale=1.15, lab/.style={font=\small}, pt/.style={circle, fill=black, inner sep=1.4pt}]
    \coordinate (O) at (0,3);
    % the two lines
    \draw[very thick] (-1.1,0) -- (3.9,0);
    \node[lab, right] at (3.95,0) {$L$};
    \draw[very thick] (-1.1,1.775) -- (3.4,0.65);
    \node[lab, right] at (3.45,0.6) {$L'$};
    % the four rays from the centre
    \draw[black!55] (O) -- (0,0);
    \draw[black!55] (O) -- (1,0);
    \draw[black!55] (O) -- (2,0);
    \draw[black!55] (O) -- (3,0);
    % centre
    \node[pt] at (O) {};
    \node[lab, above] at (0,3.1) {$O$};
    % the four points of L
    \node[pt] at (0,0) {}; \node[pt] at (1,0) {};
    \node[pt] at (2,0) {}; \node[pt] at (3,0) {};
    \node[lab, below] at (0,-0.12) {$P_1$};
    \node[lab, below] at (1,-0.12) {$P_2$};
    \node[lab, below] at (2,-0.12) {$P_3$};
    \node[lab, below] at (3,-0.12) {$P_4$};
    % their images on L'
    \node[pt] at (0,1.5) {};
    \node[pt] at (0.5455,1.3636) {};
    \node[pt] at (1.2,1.2) {};
    \node[pt] at (2,1) {};
    \node[lab, below left] at (-0.04,1.44) {$\pi(P_1)$};
    \node[lab, above right] at (2.02,1.02) {$\pi(P_4)$};
    \node[lab, align=center] at (1.4,-1.3)
      {projection from $O$ carries $L$ to $L'$:\\ the four points are equally spaced on $L$ and not on $L'$,\\ but both quadruples have cross-ratio $[4:3]$};
\end{tikzpicture}
\end{center}

The two lines need not be distinct. If \( L = L' \), then for \( P \in L \) the line \( O \vee P \) is not \( L \), because \( O \) lies on the first and not on the second, so the two meet in exactly one point (@cor-two-lines-meet) and that point is \( P \): the construction gives \( \pi = \id_L \). The classical statement takes the lines distinct, but the proof above never uses it.

Informally, this is what a photograph does. As a physical model rather than a theorem: a camera records, for each point of the scene, the point where the line from that point to the lens meets the film, and along any one line of the scene that is exactly the map \( \pi \). So a photograph of a straight railway track distorts the spacing of the sleepers but not their cross-ratio. Four equally spaced sleepers, with parameters \( 0, 1, 2, 3 \) along the track, have cross-ratio
\[
\bigl[\,(2-0)(3-1) : (2-1)(3-0)\,\bigr] = [4 : 3] ,
\]
and the four images on the film, bunched ever closer together toward the horizon, have cross-ratio \( [4:3] \) as well. Equal spacing is not a projective notion; \( [4:3] \) is.

## Affine maps inside the projective group

The chapter began with affine geometry, and we can now say exactly how it sits inside projective geometry. By @thm-affine-chart, \( \nP^n(F) \) is the disjoint union of the chart \( \{x_0 \ne 0\} \), identified with affine \( n \)-space by
\[
[x_0 : x_1 : \dots : x_n] \longmapsto \Bigl(\frac{x_1}{x_0}, \dots, \frac{x_n}{x_0}\Bigr),
\]
and the hyperplane at infinity \( H_{\infty} = \{[\x] : x_0 = 0\} = \nP(\Span(\e_1, \dots, \e_n)) \).

::: {#thm-projectivities-fixing-infinity}
[Affine Maps Are the Projectivities Fixing Infinity]

Let \( n \ge 1 \) and let \( g \) be a projectivity of \( \nP^n(F) \). Then \( g(H_{\infty}) = H_{\infty} \) if and only if \( g = [\A] \) for a matrix of the block form
\[
\A = \begin{pmatrix} 1 & \0\tp \\ \b & \M \end{pmatrix}, \qquad \b \in F^n, \quad \M \in \GL_n(F) .
\]
In that case \( g \) maps the chart \( \{x_0 \ne 0\} \) onto itself, and in the affine coordinates above it acts as
\[
\x \longmapsto \M\x + \b ,
\]
an invertible affine map with linear part \( \x \mapsto \M\x \) (@def-affine-map, @thm-affine-map-is-linear-plus-translation). Conversely every invertible affine map of \( F^n \) arises from exactly one such \( \A \).
:::

::: {.idea}
"\( g \) fixes \( H_{\infty} \) as a set" says that the matrix maps \( \Span(\e_1, \dots, \e_n) \) into itself, which is a statement about the top entry of \( n \) columns. Invertibility then forces the remaining corner entry to be non-zero, and since a projectivity only knows its matrix up to a scalar, we may divide by that entry. What is left is the block matrix that Section 01 already introduced for affine maps — the same matrix, with the extra coordinate moved from last place to first.
:::

::: {.proof}
Write \( H = \Span(\e_1, \dots, \e_n) = \{\x \in F^{n+1} : x_0 = 0\} \), so \( H_{\infty} = \nP(H) \), and let \( g = [\A] \) with \( \A \in \GL_{n+1}(F) \).

\( (\Rightarrow) \) Suppose \( g(H_{\infty}) = H_{\infty} \). By @prp-projectivity-preserves-subspaces, \( \nP(\A H) = \nP(H) \), and hence \( \A H = H \): a non-zero \( \h \in \A H \) has \( [\h] \in \nP(H) \), so \( \h \in H \), and conversely. Thus \( \A\e_j \in H \) for \( j = 1, \dots, n \), which says the columns \( 1, \dots, n \) of \( \A \) have zero entry in row \( 0 \). Writing column \( 0 \) as \( (a, \b) \) with \( a \in F \) and \( \b \in F^n \), and the lower right \( n \times n \) block as \( \M \),
\[
\A = \begin{pmatrix} a & \0\tp \\ \b & \M \end{pmatrix} .
\]
Here \( \M \) is invertible: \( \A \) restricts to an injective map \( H \to H \), which is therefore surjective (@cor-rank-nullity-consequences (e)), and that restriction is \( \M \) in the basis \( (\e_1, \dots, \e_n) \) of \( H \). And \( a \ne 0 \): if \( a = 0 \) then column \( 0 \) of \( \A \) lies in \( H = \A H \), so \( \A\e_0 = \A\h \) for some \( \h \in H \), and injectivity would give \( \e_0 \in H \), which is false. Replacing \( \A \) by \( a^{-1}\A \), which by @thm-pgl (a) induces the same projectivity, puts \( \A \) in the stated form with \( 1 \) in the corner.

\( (\Leftarrow) \) For \( \A \) of the stated form and \( \x \in H \), the first entry of \( \A\x \) is \( 1 \cdot 0 + \0\tp\x' = 0 \) where \( \x' \) collects the last \( n \) entries, so \( \A H \subseteq H \); and \( \A \) is invertible, since \( \A\x = \0 \) forces \( x_0 = 0 \) and then \( \M\x' = \0 \), so \( \x' = \0 \). By @cor-rank-nullity-consequences (e) again \( \A H = H \), and @prp-projectivity-preserves-subspaces gives \( g(H_{\infty}) = H_{\infty} \).

*The action on the chart.* Since \( g \) is a bijection of \( \nP^n(F) \) mapping \( H_{\infty} \) onto \( H_{\infty} \), it maps the complement \( \{x_0 \ne 0\} \) onto itself. A point of the chart is \( [1 : \x] \) with \( \x \in F^n \), and
\[
\A\begin{pmatrix} 1 \\ \x \end{pmatrix} = \begin{pmatrix} 1 \\ \M\x + \b \end{pmatrix},
\]
whose affine coordinates are \( \M\x + \b \). By @thm-affine-map-is-linear-plus-translation this is the affine map with linear part \( \x \mapsto \M\x \) and value \( \b \) at the origin, and it is invertible because \( \M \) is.

*Converse.* Given an invertible affine map \( \x \mapsto \M\x + \b \) of \( F^n \), the matrix displayed above induces a projectivity fixing \( H_{\infty} \) and restricting to it. If two such matrices \( \A \), \( \A' \) induce the same projectivity, then \( \A' = \lambda\A \) by @thm-pgl (a), and comparing the corner entries gives \( \lambda = 1 \), so \( \A' = \A \). This proves the theorem.
:::

So the affine group of \( F^n \) is the subgroup of \( \operatorname{PGL}_{n+1}(F) \) stabilizing one hyperplane. Projective geometry is affine geometry with the hyperplane at infinity forgotten, and every affine notion that a projectivity can destroy — parallelism, ratios of lengths along a line, midpoints — is a notion that mentions \( H_{\infty} \). The cross-ratio never does, which is why it survives.

## Exercises

### A. Check your understanding

:::: {#exr-projective-transformations-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State precisely when two isomorphisms \( S, T \colon V \to W \) induce the same projectivity.
2. How many points, and satisfying what condition, determine a projectivity of \( \nP^n(F) \) uniquely?
3. True or false, with a reason: a projectivity of \( \nP^2(\nQ) \) fixing four points in general position is the identity.
4. True or false, with a reason: \( \det \) is a well-defined function on \( \operatorname{PGL}_3(\nQ) \).
5. What is \( (A, B; C, B) \), and why?
:::
::::

::: {.solution}
(a) Exactly when \( S = \lambda T \) for some \( \lambda \in F^{\times} \) (@thm-pgl (a)).

(b) \( n + 2 \) points in general position, that is, \( n+2 \) points of which every \( n+1 \) have linearly independent representatives (@def-general-position, @thm-fundamental-theorem-of-projective-geometry).

(c) True. Here \( n = 2 \), so four points in general position are \( n + 2 \) points in general position. The identity is one projectivity fixing them, and by the uniqueness in @thm-fundamental-theorem-of-projective-geometry it is the only one.

(d) False. The matrices \( \I_3 \) and \( 2\I_3 \) induce the same projectivity but have determinants \( 1 \) and \( 8 \).

(e) \( (A, B; C, B) = [0:1] \). By @def-cross-ratio the cross-ratio is \( f(D) \) with \( D = B \), and \( f(B) = [0:1] \) by the definition of \( f \).
:::

### B. Practice

:::: {#exr-projective-transformations-b1}
[B1: A projectivity of the line]

Find a matrix inducing the projectivity of \( \nP^1(\nQ) \) that sends \( [1:0] \), \( [0:1] \), \( [1:1] \) to \( [1:1] \), \( [1:2] \), \( [2:3] \) respectively, and verify the three conditions.
::::

::: {.solution}
The source triple is already normalized in the sense of @lem-projective-frame-normalization: \( (\e_0, \e_1) \) is a basis and \( (1,1) = \e_0 + \e_1 \). Normalize the target: we need \( \lambda_1(1,1) + \lambda_2(1,2) = (2,3) \), that is, \( \lambda_1 + \lambda_2 = 2 \) and \( \lambda_1 + 2\lambda_2 = 3 \). Subtracting, \( \lambda_2 = 1 \), then \( \lambda_1 = 1 \). Both are non-zero, as @lem-projective-frame-normalization guarantees.

So the map sends \( \e_0 \mapsto (1,1) \) and \( \e_1 \mapsto (1,2) \), that is,
\[
\A = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}, \qquad \det \A = 1 \ne 0 .
\]
Check: \( \A\e_0 = (1,1) \), so \( [1:0] \mapsto [1:1] \); \( \A\e_1 = (1,2) \), so \( [0:1] \mapsto [1:2] \); \( \A(1,1) = (2,3) \), so \( [1:1] \mapsto [2:3] \). By @thm-fundamental-theorem-of-projective-geometry no other projectivity does this, so every other correct answer is \( \lambda\A \).
:::

:::: {#exr-projective-transformations-b2}
[B2: General position]

Determine which of the following lists of points of \( \nP^2(\nQ) \) are in general position. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( [1:0:0] \), \( [1:1:0] \), \( [1:1:1] \), \( [0:1:1] \).
2. \( [1:0:0] \), \( [0:1:0] \), \( [1:2:0] \), \( [0:0:1] \).
3. \( [1:1:1] \), \( [1:2:4] \), \( [1:3:9] \), \( [1:4:16] \).
:::
::::

::: {.solution}
Here \( n = 2 \), so general position for four points means every triple of representatives is independent, tested by a \( 3 \times 3 \) determinant.

(a) The four determinants, in the order of the triples \( (1,2,3) \), \( (1,2,4) \), \( (1,3,4) \), \( (2,3,4) \), are
\[
\begin{aligned}
\det\begin{pmatrix} 1&1&1\\0&1&1\\0&0&1\end{pmatrix} &= 1, &
\det\begin{pmatrix} 1&1&0\\0&1&1\\0&0&1\end{pmatrix} &= 1, \\
\det\begin{pmatrix} 1&1&0\\0&1&1\\0&1&1\end{pmatrix} &= 0, &
\det\begin{pmatrix} 1&1&0\\1&1&1\\0&1&1\end{pmatrix} &= -1 .
\end{aligned}
\]
The third is zero, so the list is **not** in general position: \( [1:0:0] \), \( [1:1:1] \), \( [0:1:1] \) are collinear, since \( (1,1,1) = (1,0,0) + (0,1,1) \).

(b) Not in general position: \( (1,2,0) = (1,0,0) + 2(0,1,0) \), so the first three points are collinear.

(c) In general position. The four representatives are \( (1, t, t^2) \) for \( t = 1, 2, 3, 4 \), so each triple gives a Vandermonde matrix, whose determinant is \( \prod_{i<j}(t_j - t_i) \) (@thm-vandermonde-determinant, and @cor-vandermonde-nonzero for the conclusion). Explicitly, \( t = 1,2,3 \) gives \( 1 \cdot 2 \cdot 1 = 2 \); \( t = 1,2,4 \) gives \( 1 \cdot 3 \cdot 2 = 6 \); \( t = 1,3,4 \) gives \( 2 \cdot 3 \cdot 1 = 6 \); \( t = 2,3,4 \) gives \( 1 \cdot 2 \cdot 1 = 2 \). All are non-zero, so every triple is independent.
:::

:::: {#exr-projective-transformations-b3}
[B3: Cross-ratio]

In \( \nP^1(\nQ) \) with the chart \( [t:1] \mapsto t \), let \( A, B, C, D \) have parameters \( 1, 2, 4, 8 \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( (A, B; C, D) \).
2. Compute the images of the four points under the projectivity induced by \( \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} \), and recompute the cross-ratio.
:::
::::

::: {.solution}
(a) By @prp-cross-ratio-formula,
\[
(A,B;C,D) = \bigl[\,(4-1)(8-2) : (4-2)(8-1)\,\bigr] = [18 : 14] = [9 : 7] .
\]

(b) The matrix has determinant \( 1 \), and sends \( [t : 1] \) to \( [t : t+1] \), which in the chart is \( t/(t+1) \). The four parameters become \( \tfrac12, \tfrac23, \tfrac45, \tfrac89 \). Then
\[
\begin{aligned}
\tfrac45 - \tfrac12 &= \tfrac3{10}, & \tfrac89 - \tfrac23 &= \tfrac29, \\
\tfrac45 - \tfrac23 &= \tfrac2{15}, & \tfrac89 - \tfrac12 &= \tfrac7{18},
\end{aligned}
\]
so the cross-ratio is \( \bigl[\tfrac3{10}\cdot\tfrac29 : \tfrac2{15}\cdot\tfrac7{18}\bigr] = \bigl[\tfrac1{15} : \tfrac7{135}\bigr] = [9 : 7] \), after multiplying both entries by \( 135 \). This agrees with (a), as @thm-cross-ratio-invariant (a) requires.
:::

### C. Going deeper

:::: {#exr-projective-transformations-c1}
[C1: Sharp triple transitivity, and a count]

::: {.enumerate options="label=(\alph*)"}
1. Prove that for any two triples of pairwise distinct points of \( \nP^1(F) \) there is exactly one projectivity carrying the first to the second.
2. Hence compute \( \lvert \operatorname{PGL}_2(\nF_q) \rvert \) for a finite field \( \nF_q \), and check your answer against \( q = 2 \) by listing the projectivities of \( \nP^1(\nF_2) \).
:::
::::

::: {.solution}
(a) On a line, \( n = 1 \), so \( n + 2 = 3 \) and general position for three points means pairwise distinct (@def-general-position). The statement is @thm-fundamental-theorem-of-projective-geometry.

(b) By (a), \( \operatorname{PGL}_2(\nF_q) \) acts on the set of ordered triples of pairwise distinct points of \( \nP^1(\nF_q) \) in such a way that exactly one group element carries any given triple to any other. Fixing one triple, the map \( g \mapsto (g(A), g(B), g(C)) \) is therefore a bijection from \( \operatorname{PGL}_2(\nF_q) \) onto the set of such triples. Now \( \nP^1(\nF_q) \) has \( q + 1 \) points: there are \( q^2 - 1 \) non-zero vectors in \( \nF_q^2 \), and each point has exactly \( q - 1 \) representatives, so the count is \( (q^2-1)/(q-1) = q+1 \). Hence
\[
\lvert \operatorname{PGL}_2(\nF_q) \rvert = (q+1)\,q\,(q-1) .
\]
For \( q = 2 \) this is \( 3 \cdot 2 \cdot 1 = 6 \). And indeed \( \nP^1(\nF_2) \) has the three points \( [1:0] \), \( [0:1] \), \( [1:1] \); by (a) every permutation of them is realized by exactly one projectivity, giving \( 3! = 6 \). (Consistently, \( \GL_2(\nF_2) \) has \( 6 \) elements and the scalars are only \( \I_2 \), so \( \Pi \) of @thm-pgl is injective here.)
:::

:::: {#exr-projective-transformations-c2}
[C2: Rearranging the four points]

Let \( A, B, C \) be pairwise distinct points of a projective line and \( D \) a fourth point.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( (B, A; C, D) \) is obtained from \( (A, B; C, D) = [\lambda : \mu] \) by exchanging the two entries.
2. Suppose all four points lie in a chart, with parameters \( a, b, c, d \), and that \( (A,B;C,D) \) is the scalar \( \chi \). Prove that \( (A, C; B, D) = 1 - \chi \).
:::
::::

::: {.solution}
(a) Use @prp-cross-ratio-formula with the representatives \( \a, \b \) and the expansions \( \c = c_1\a + c_2\b \), \( \d = d_1\a + d_2\b \). Computing \( (B, A; C, D) \) means expanding in the basis \( (\b, \a) \) instead, which exchanges the roles of the two coordinates: the coefficients of \( \c \) are now \( (c_2, c_1) \) and those of \( \d \) are \( (d_2, d_1) \). The formula gives \( [\,d_2c_1 : d_1c_2\,] \), the entries of \( [\,d_1c_2 : d_2c_1\,] \) exchanged.

(b) By @prp-cross-ratio-formula in the chart,
\[
\chi = \frac{(c-a)(d-b)}{(c-b)(d-a)}, \qquad (A,C;B,D) = \frac{(b-a)(d-c)}{(b-c)(d-a)} .
\]
Put both over the common denominator \( (c-b)(d-a) \), noting \( (b-c) = -(c-b) \):
\[
\chi + (A,C;B,D) = \frac{(c-a)(d-b) - (b-a)(d-c)}{(c-b)(d-a)} .
\]
Expand the numerator:
\[
\begin{aligned}
(c-a)(d-b) - (b-a)(d-c) &= cd - cb - ad + ab - bd + bc + ad - ac \\
&= cd + ab - bd - ac = (c-b)(d-a) .
\end{aligned}
\]
Hence \( \chi + (A,C;B,D) = 1 \), as claimed.
:::

:::: {#exr-projective-transformations-c3}
[C3: Cross-ratio characterizes projectivities of a line]

Let \( L \) and \( L' \) be projective lines over \( F \) and let \( g \colon L \to L' \) be an **injection** such that
\[
\bigl(g(A), g(B); g(C), g(D)\bigr) = (A, B; C, D)
\]
for all \( A, B, C, D \in L \) with \( A, B, C \) pairwise distinct. Prove that \( g \) is a projectivity.

*Hint: pin \( g \) down on three points first.*
::::

::: {.solution}
Write \( L = \nP(U) \) with \( \dim U = 2 \) and pick a basis \( (\u_1, \u_2) \) of \( U \); the three points \( [\u_1] \), \( [\u_2] \), \( [\u_1 + \u_2] \) are pairwise distinct, since no two of \( \u_1, \u_2, \u_1 + \u_2 \) are proportional. So we may choose pairwise distinct \( A, B, C \in L \). Since \( g \) is injective, \( g(A), g(B), g(C) \) are pairwise distinct. By @thm-fundamental-theorem-of-projective-geometry with \( n = 1 \) there is a unique projectivity \( h \colon L \to L' \) with \( h(A) = g(A) \), \( h(B) = g(B) \), \( h(C) = g(C) \).

Let \( D \in L \). By the hypothesis on \( g \) and by @thm-cross-ratio-invariant (a) applied to \( h \),
\[
\bigl(g(A), g(B); g(C), g(D)\bigr) = (A,B;C,D) = \bigl(h(A), h(B); h(C), h(D)\bigr).
\]
The two triples on the outside are the same, namely \( (g(A), g(B), g(C)) \). Writing \( f' \) for the normalizing projectivity of that triple (@def-cross-ratio), the displayed equality reads \( f'(g(D)) = f'(h(D)) \), and \( f' \) is injective, so \( g(D) = h(D) \). As \( D \) was arbitrary, \( g = h \), a projectivity.

Note where each hypothesis went: injectivity of \( g \) was needed only to know that \( g(A), g(B), g(C) \) are distinct, so that the cross-ratio hypothesis is applicable at all. Surjectivity was never assumed, and comes out at the end: \( g = h \) and \( h \) is a bijection (@prp-projectivity-basic).
:::
