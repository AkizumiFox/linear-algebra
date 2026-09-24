# The Structure Theorem

§05 settled the extreme case: over an algebraically closed field, an algebra of operators with no invariant subspace to hide in is the whole of \( \End(V) \). Most algebras are not like that. This section shows that, over an algebraically closed field and under one hypothesis — semisimplicity — that extreme case is nevertheless the only building block there is. Every such algebra is a product of full matrix algebras, and the sizes of the blocks are determined by the algebra. That is the structure theorem, and it is the last piece of general theory the chapter needs: from here on the work is to apply it to groups.

Throughout, \( F \) is a field and \( A \) is an associative algebra with identity, finite-dimensional over \( F \) and with \( A \ne \{0\} \).

## Products of matrix algebras

Before proving that something is a product of matrix algebras, we should say what the product is and look at a few.

*A product of algebras is a list of algebras run side by side, with nothing passing between the slots.*

::: {#def-product-of-algebras}
[Product of algebras]

Let \( A_1, \dots, A_k \) be \( F \)-algebras. Their **product** \( A_1 \times \dots \times A_k \) is the product vector space (@def-product-of-spaces) with multiplication defined **slot by slot**,
\[
(x_1, \dots, x_k)(y_1, \dots, y_k) = (x_1y_1, \dots, x_ky_k),
\]
and identity \( (1_{A_1}, \dots, 1_{A_k}) \).
:::

The axioms of @def-algebra-over-field hold slot by slot because they hold in each \( A_i \), and \( \dim(A_1 \times \dots \times A_k) = \sum_i \dim A_i \) by @thm-dimension-of-product. Two features of a product will be used constantly. First, the element \( e_i \) with \( 1_{A_i} \) in slot \( i \) and \( 0 \) elsewhere satisfies \( e_i^2 = e_i \), \( e_ie_j = 0 \) for \( i \ne j \), and \( e_1 + \dots + e_k = 1 \). Second, the product is almost never commutative, but its center always contains the \( k \)-dimensional span of \( e_1, \dots, e_k \).

::: {#exm-products-of-matrix-algebras}
[Three products, seen from two sides]

Identify each of the following with a product of matrix algebras over \( F \), and give its dimension: (i) the diagonal matrices in \( M_n(F) \); (ii) \( M_n(F) \) itself; (iii) the block diagonal matrices in \( M_5(F) \) with blocks of sizes \( 2, 2, 1 \), where the **two** \( 2 \times 2 \) blocks are allowed to differ.
:::

::: {.solution}
(i) The map \( \diag(c_1, \dots, c_n) \mapsto (c_1, \dots, c_n) \) is a bijection, is linear, sends \( \I_n \) to \( (1, \dots, 1) \), and is multiplicative because diagonal matrices multiply entry by entry. So the diagonal matrices form \( F \times \dots \times F = M_1(F)^{\,n} \), of dimension \( n = \sum_{i=1}^{n} 1^2 \).

(ii) \( M_n(F) \) is the product with one slot, \( k = 1 \) and \( n_1 = n \), of dimension \( n^2 \).

(iii) Writing a block diagonal matrix as the list of its blocks gives \( M_2(F) \times M_2(F) \times M_1(F) \), since block diagonal matrices multiply blockwise (@thm-block-diagonal-arithmetic, applied twice). Its dimension is \( 4 + 4 + 1 = 9 = 2^2 + 2^2 + 1^2 \).

In all three the dimension is \( \sum_i n_i^2 \). The theorem below says that this is not a coincidence of the examples.
:::

## The regular representation

An abstract algebra has no vectors to act on until we give it some, and the cheapest supply is the algebra itself.

::: {.remark}
The vocabulary is §03's and §04's. An **\( A \)-space** is a vector space \( V \) with an algebra homomorphism \( A \to \End(V) \), written \( a\v \) (@def-representation-of-an-algebra); **invariant** subspace and **irreducible** \( A \)-space are as in @def-simple-module; and a **homomorphism of \( A \)-spaces** \( f \colon V \to W \) is what §04 calls an \( A \)-map, a linear map with \( f(a\v) = af(\v) \) (@def-intertwining-map). A bijective one is an **isomorphism**, and we then write \( V \cong W \).
:::

The **regular representation** of \( A \), introduced in §03 (@def-representation-of-an-algebra), is \( A \) acting on itself by left multiplication: \( L \colon A \to \End(A) \), \( L_a(x) = ax \). It is injective because \( L_a(1_A) = a \); this is exactly @thm-cayley-for-algebras. Its invariant subspaces are the subspaces \( I \subseteq A \) with \( AI \subseteq I \), which is to say the **left ideals** of §02. So the irreducible invariant subspaces of the regular representation are the **minimal left ideals**: the non-zero left ideals containing no smaller non-zero left ideal.

We call \( A \) **semisimple** when the regular representation is semisimple in the sense of §03 (@def-semisimple-algebra): every left ideal of \( A \) has a complementary left ideal.

## The structure theorem

::: {#thm-wedderburn}
[Wedderburn's Structure Theorem, Algebraically Closed Case]

Let \( F \) be an **algebraically closed** field and let \( A \ne \{0\} \) be a **semisimple** finite-dimensional \( F \)-algebra: every left ideal of \( A \) has a complementary left ideal. Then there are an integer \( k \ge 1 \), integers \( n_1, \dots, n_k \ge 1 \) and an isomorphism of \( F \)-algebras
\[
A \;\cong\; M_{n_1}(F) \times \dots \times M_{n_k}(F).
\]
Moreover \( k \) and the multiset \( \{n_1, \dots, n_k\} \) depend only on \( A \): they are the number of isomorphism classes of irreducible \( A \)-spaces and their dimensions.
:::

::: {.idea}
**Step roadmap.** ① Break the regular representation into minimal left ideals. ② Keep one from each isomorphism class, say \( V_1, \dots, V_k \), and map \( A \) into \( \End(V_1) \times \dots \times \End(V_k) \) by letting it act on each. ③ The map is injective because an element acting as zero on every \( V_i \) acts as zero on all of \( A \), hence kills \( 1 \). ④ It is surjective: on \( W = V_1 \oplus \dots \oplus V_k \), Schur's lemma computes the commutant of the image to be the scalars-on-each-slot, and @thm-double-commutant turns that into the statement that the image is everything preserving the slots. ⑤ Uniqueness: read the \( n_i \) off as the dimensions of the irreducible \( A \)-spaces, which no choice in the proof can change.
:::

:::: {.proof}
**Step 1: split the regular representation.** Regard \( A \) as an \( A \)-space by left multiplication. Its invariant subspaces are the left ideals, and by hypothesis every one of them has an invariant complement. By @thm-semisimple-iff-sum-of-simples, (a) \( \Rightarrow \) (c), \( A \) is a **direct** sum of finitely many irreducible invariant subspaces:
\[
A = L_1 \oplus \dots \oplus L_m , \qquad L_j \text{ a minimal left ideal.}
\]
Since \( A \ne \{0\} \) we have \( m \ge 1 \).

**Step 2: one representative per class.** Being isomorphic is an equivalence relation on the list \( L_1, \dots, L_m \); pick one member from each class and call the chosen spaces \( V_1, \dots, V_k \). They are pairwise non-isomorphic, and every \( L_j \) is isomorphic to exactly one of them. Put \( n_i = \dim V_i \ge 1 \) and let \( \rho_i \colon A \to \End(V_i) \) be the homomorphism giving the action. Then \( k \ge 1 \).

**Step 3: the map, and its injectivity.** Let
\[
\Phi \colon A \to \End(V_1) \times \dots \times \End(V_k), \qquad
\Phi(a) = (\rho_1(a), \dots, \rho_k(a)).
\]
Each \( \rho_i \) is an algebra homomorphism and the product has slot-by-slot operations (@def-product-of-algebras), so \( \Phi \) is an algebra homomorphism, and \( \Phi(1_A) \) is the identity.

Suppose \( \Phi(a) = 0 \). Fix \( j \), let \( i \) be the index with \( L_j \cong V_i \), and let \( f \colon L_j \to V_i \) be an isomorphism of \( A \)-spaces. For \( x \in L_j \) we get \( f(ax) = \rho_i(a)f(x) = 0 \), and \( f \) is injective, so \( ax = 0 \). Thus \( aL_j = \{0\} \) for every \( j \), and since \( A = L_1 + \dots + L_m \) we get \( aA = \{0\} \). In particular \( a = a1_A = 0 \). So \( \Phi \) is injective.

**Step 4: surjectivity.** Let \( W = V_1 \oplus \dots \oplus V_k \) be the product space, with \( A \) acting slot by slot, and let \( B \subseteq \End(W) \) be the image of \( A \) under this action; \( B \) is a subalgebra containing \( \id_W \). Let \( D \subseteq \End(W) \) be the set of operators mapping each \( V_i \) into itself. Restricting to the slots identifies \( D \) with \( \End(V_1) \times \dots \times \End(V_k) \) as an algebra, and under that identification \( \Phi(A) \) corresponds to \( B \). So it suffices to prove \( B = D \).

*\( B \) acts semisimply on \( W \).* Each \( V_i \) is \( B \)-invariant, and a subspace of \( V_i \) is \( B \)-invariant exactly when it is \( A \)-invariant, so each \( V_i \) is an irreducible \( B \)-invariant subspace; and \( W = V_1 + \dots + V_k \). By @thm-semisimple-iff-sum-of-simples, \( B \) acts semisimply.

*The commutant of \( B \).* Let \( \iota_j \colon V_j \to W \) and \( \pi_i \colon W \to V_i \) be the slot inclusions and projections, and for \( s \in \End(W) \) put \( s_{ij} = \pi_i \circ s \circ \iota_j \colon V_j \to V_i \). Then \( s \) commutes with the action of every \( a \in A \) if and only if
\[
s_{ij}\,\rho_j(a) = \rho_i(a)\,s_{ij} \qquad \text{for all } i, j, a,
\]
that is, if and only if every \( s_{ij} \) is a homomorphism of \( A \)-spaces. For \( i \ne j \) the spaces \( V_i \) and \( V_j \) are irreducible and non-isomorphic, so @thm-schurs-lemma gives \( s_{ij} = 0 \). For \( i = j \) the field is algebraically closed and \( V_i \) is irreducible, so the second part of @thm-schurs-lemma gives \( s_{ii} = \lambda_i\,\id_{V_i} \) for some \( \lambda_i \in F \). Conversely every operator of that shape commutes with \( B \). Hence
\[
B' = \{\, \lambda_1\,\id_{V_1} \oplus \dots \oplus \lambda_k\,\id_{V_k} : \lambda_i \in F \,\}.
\]

*The double commutant of \( B \).* Let \( p_i \in \End(W) \) be the projection onto \( V_i \) along the other slots; it is the member of \( B' \) with \( \lambda_i = 1 \) and the other \( \lambda_j = 0 \). If \( t \in B'' \), then \( t \) commutes with \( p_i \), so
\[
t(V_i) = t(\im p_i) = \im(t p_i) = \im(p_i t) \subseteq \im p_i = V_i ,
\]
which says \( t \in D \). Conversely every \( t \in D \) commutes with each \( \lambda_1\id \oplus \dots \oplus \lambda_k\id \), so \( D \subseteq B'' \). Hence \( B'' = D \).

*Conclusion.* \( B \) is a subalgebra of \( \End(W) \) containing \( \id_W \) and acting semisimply, so @thm-double-commutant gives \( B = B'' = D \). Therefore \( \Phi \) is surjective, and with Step 3 it is an isomorphism of algebras onto \( \End(V_1) \times \dots \times \End(V_k) \).

**Step 5: matrices.** Choosing a basis \( \sB_i \) of \( V_i \) makes \( T \mapsto \mtx{T}{\sB_i}{\sB_i} \) a linear bijection \( \End(V_i) \to M_{n_i}(F) \) (@thm-linear-maps-isomorphic-to-matrices) which is multiplicative (@thm-matrix-of-composition) and sends \( \id_{V_i} \) to \( \I_{n_i} \), hence an isomorphism of algebras. Doing this in each slot gives
\[
A \cong M_{n_1}(F) \times \dots \times M_{n_k}(F).
\]

**Step 6: uniqueness.** We first identify all irreducible \( A \)-spaces.

::: {.claim}
If \( A = \sum_j L_j \) with each \( L_j \) an irreducible left ideal, then every irreducible \( A \)-space is isomorphic to some \( L_j \).
:::

::: {.proof}
Let \( U \) be an irreducible \( A \)-space and pick \( \u \in U \), \( \u \ne \0 \). The map \( f \colon A \to U \), \( f(a) = a\u \), is a homomorphism of \( A \)-spaces from the regular representation, since \( f(ba) = (ba)\u = b f(a) \). Its image is an invariant subspace containing \( f(1_A) = \u \ne \0 \), hence equals \( U \) by irreducibility. From \( A = \sum_j L_j \) we get \( U = \sum_j f(L_j) \), so \( f(L_{j_0}) \ne \{\0\} \) for some \( j_0 \). Then \( f|_{L_{j_0}} \colon L_{j_0} \to U \) is a non-zero homomorphism between irreducible \( A \)-spaces, hence an isomorphism by @thm-schurs-lemma.
:::

Now let \( B_0 = M_{p_1}(F) \times \dots \times M_{p_l}(F) \) be any product of matrix algebras, and let \( C_j = F^{p_j} \) carry the action of \( B_0 \) through the \( j \)-th slot. Each \( C_j \) is irreducible: given \( \v \ne \0 \) in \( F^{p_j} \) and any \( \w \), extend \( \v \) to a basis (@thm-basis-extension) and let \( \X \) be the matrix sending \( \v \mapsto \w \) and the other basis vectors to \( \0 \); then \( M_{p_j}(F)\v = F^{p_j} \), so no proper non-zero invariant subspace exists. They are pairwise non-isomorphic: the idempotent \( e_j \in B_0 \) acts as the identity on \( C_j \) and as \( 0 \) on \( C_i \) for \( i \ne j \), so an isomorphism \( f \colon C_j \to C_i \) would give \( f(\v) = f(e_j\v) = e_jf(\v) = \0 \) for every \( \v \), forcing \( f = 0 \). Finally, for each \( j \) and each column index \( c \) let \( C_{j,c} \subseteq B_0 \) consist of the elements whose slots other than \( j \) are \( \0 \) and whose \( j \)-th slot has all columns but the \( c \)-th equal to \( \0 \). Each \( C_{j,c} \) is a left ideal, the map \( x \mapsto x_j\e_c \) is an isomorphism of \( B_0 \)-spaces \( C_{j,c} \to C_j \), and \( B_0 \) is the direct sum of the \( C_{j,c} \). So by the Claim the irreducible \( B_0 \)-spaces are, up to isomorphism, exactly \( C_1, \dots, C_l \): there are \( l \) of them and their dimensions are \( p_1, \dots, p_l \).

An isomorphism of algebras \( A \to B_0 \) turns \( B_0 \)-spaces into \( A \)-spaces, preserving irreducibility and isomorphism. So if \( A \cong M_{n_1}(F) \times \dots \times M_{n_k}(F) \), then \( A \) has exactly \( k \) isomorphism classes of irreducible spaces and their dimensions are \( n_1, \dots, n_k \). Both quantities are determined by the isomorphism class of \( A \) alone, so they do not depend on the choices made in Steps 1 and 2. This proves the theorem.
::::

::: {.remark}
The case \( k = 1 \) says that a semisimple algebra with only one irreducible space, up to isomorphism, is a full matrix algebra. Burnside's theorem (@thm-burnside) is the concrete counterpart of that sentence: there the algebra arrives already written as operators on an irreducible space, its hypothesis is irreducibility rather than semisimplicity, and its conclusion is the sharper equality \( A = \End(V) \) in place of an isomorphism. The proof above does not use @thm-burnside; what it borrows from §05 is the double commutant theorem.
:::

Two hypotheses carried the proof, and it is worth saying again where. **Semisimplicity** was used twice: to split the regular representation in Step 1, and to apply the double commutant theorem in Step 4. **Algebraic closure** was used once, in the second half of Schur's lemma, to know that a homomorphism of an irreducible space to itself is a scalar. Drop algebraic closure and the diagonal slots become division algebras rather than \( F \); that is the general theorem, quoted below and not proved.

::: {#cor-dimension-count}
[Counting Dimensions in the Wedderburn Form]

In the situation of @thm-wedderburn,
\[
\dim_F A = n_1^2 + \dots + n_k^2 ,
\]
and the center \( Z(A) = \{ z \in A : za = az \text{ for all } a \in A \} \) has \( \dim_F Z(A) = k \).
:::

::: {.proof}
The dimension of a product is the sum of the dimensions (@thm-dimension-of-product) and \( \dim M_{n_i}(F) = n_i^2 \), which gives the first formula. An isomorphism of algebras carries the center onto the center, so we may compute in \( M_{n_1}(F) \times \dots \times M_{n_k}(F) \). Multiplication is slot by slot, so \( (z_1, \dots, z_k) \) is central exactly when each \( z_i \) is central in \( M_{n_i}(F) \), and by @prp-center-of-matrix-algebra, read through the identification of \( M_{n_i}(F) \) with \( \End(F^{n_i}) \), that means \( z_i = \lambda_i\I_{n_i} \). So \( Z(A) \) is isomorphic to \( F^{k} \) as a vector space, of dimension \( k \).
:::

The two numbers in the corollary are the whole invariant content of a semisimple algebra over an algebraically closed field: \( k \) is read from the center, and then the \( n_i \) are \( k \) positive integers with \( \sum n_i^2 = \dim A \). When \( A \) is the group algebra \( \nC[G] \) of a finite group, whose dimension is \( \lvert G\rvert \) by @def-group-algebra, this becomes the sum-of-squares formula \( \lvert G\rvert = \sum_i n_i^2 \) for the dimensions of the irreducible representations, and \( k \) turns out to be the number of conjugacy classes. Both statements are proved later in this chapter, once Maschke's theorem supplies the missing hypothesis that \( \nC[G] \) is semisimple.

::: {.check}
A semisimple algebra \( A \) over \( \nC \) has \( \dim A = 10 \) and \( \dim Z(A) = 4 \). What are the possible block sizes?
:::

::: {.solution}
By @cor-dimension-count we need \( k = 4 \) positive integers with \( n_1^2 + \dots + n_4^2 = 10 \). No \( n_i \) can be \( 3 \) or more: that block alone contributes at least \( 9 \), and the other three contribute at least \( 3 \), for a total of at least \( 12 \). So every \( n_i \) is \( 1 \) or \( 2 \); if \( t \) of them equal \( 2 \), the sum is \( 4t + (4 - t) = 10 \), so \( t = 2 \). Up to order the block sizes are \( 1, 1, 2, 2 \) and \( A \cong \nC \times \nC \times M_2(\nC) \times M_2(\nC) \).
:::

## What is quoted and not proved

The theorem above is the case this book can carry. The general statement is older and stronger, and we record it honestly.

::: {.remark}
**The Wedderburn–Artin theorem.** Over an arbitrary field \( F \), a finite-dimensional semisimple \( F \)-algebra is isomorphic to a product
\[
M_{n_1}(D_1) \times \dots \times M_{n_k}(D_k),
\]
where each \( D_i \) is a **division algebra** over \( F \) in the sense of §04 — an \( F \)-algebra, here finite-dimensional and not assumed commutative, in which every non-zero element has a multiplicative inverse. The result is due to Wedderburn, and Artin extended it beyond finite dimension. **We do not prove it.** The reason is not that the argument is long — it follows the same route, with Schur's lemma supplying \( \operatorname{End}_A(V_i) = D_i \) in place of \( F \) — but that this book has never built the theory of division rings. The only non-commutative division algebra it has met is the quaternions \( \nH \) over \( \nR \) (@def-quaternions), and one example is not a theory. Nothing in this chapter depends on the general statement.
:::

::: {.remark}
**Wedderburn's little theorem.** Every **finite** division ring is commutative, hence a field. This is a separate theorem of Wedderburn's, and we do not prove it either; the standard proofs use counting arguments in group theory or cyclotomic polynomials, neither of which this book has developed. Its effect on the theorem above is that over a finite field the division algebras \( D_i \) are all fields, so the blocks are matrix algebras over field extensions of \( F \).
:::

::: {.warning}
**Semisimplicity is not automatic, so the theorem does not apply to every algebra.** The upper triangular matrices in \( M_2(F) \) form a three-dimensional algebra which is **not** a product of matrix algebras: a product \( M_{n_1}(F) \times \dots \times M_{n_k}(F) \) of total dimension \( 3 \) would need \( \sum n_i^2 = 3 \), hence \( k = 3 \) and all \( n_i = 1 \), hence a commutative algebra; but \( \E_{11}\E_{12} = \E_{12} \) while \( \E_{12}\E_{11} = \0 \). What fails is semisimplicity: as §05 noted, \( \Span(\e_1) \) is an invariant subspace with no invariant complement. §03 identifies the obstruction as the radical of the algebra (@def-algebra-radical).
:::

## Two worked decompositions

::: {#exm-wedderburn-of-c4}
[The group algebra of a cyclic group of order four]

Let \( C_4 = \{1, g, g^2, g^3\} \) be a cyclic group of order \( 4 \), so \( g^4 = 1 \); it exists, for instance as the subgroup \( \{1, i, -1, -i\} \) of \( (\nC \setminus \{0\}, \cdot) \) with \( g = i \) (@thm-subgroup-test). Find the Wedderburn form of the group algebra \( \nC[C_4] \) (@def-group-algebra) explicitly, and exhibit the idempotents \( e_1, \dots, e_4 \) of the product.
:::

::: {.solution}
Let \( \omega_1 = 1 \), \( \omega_2 = i \), \( \omega_3 = -1 \), \( \omega_4 = -i \) be the four complex numbers with \( \omega^4 = 1 \). Define
\[
\Phi \colon \nC[C_4] \to \nC^4, \qquad
\Phi\Bigl(\sum_{t=0}^{3} a_t g^{t}\Bigr) = \Bigl(\sum_{t} a_t\omega_r^{\,t}\Bigr)_{r=1}^{4}.
\]
It is linear by construction. It is multiplicative: it is enough to check on the basis \( g^s, g^t \), where \( g^sg^t = g^{s+t} \) with the exponent read modulo \( 4 \), and \( \omega_r^{\,s+t} = \omega_r^{\,s}\omega_r^{\,t} \) with \( \omega_r^{4} = 1 \) making the reduction harmless. It sends \( 1 = g^0 \) to \( (1,1,1,1) \). Its matrix in the basis \( (1, g, g^2, g^3) \) of the source and the standard basis of \( \nC^4 \) is
\[
\begin{pmatrix}
1 & 1 & 1 & 1 \\
1 & i & -1 & -i \\
1 & -1 & 1 & -1 \\
1 & -i & -1 & i
\end{pmatrix},
\]
whose determinant is \( -16i \ne 0 \), so \( \Phi \) is bijective. Hence
\[
\nC[C_4] \cong \nC \times \nC \times \nC \times \nC = M_1(\nC)^{\,4},
\]
with \( k = 4 \) and \( n_1 = n_2 = n_3 = n_4 = 1 \); the dimension count \( \sum n_i^2 = 4 = \lvert C_4\rvert \) checks out, and \( Z(\nC[C_4]) \) is everything, of dimension \( 4 \), as it must be for a commutative algebra.

The idempotents pull back to
\[
e_r = \tfrac14\sum_{t=0}^{3}\conj{\omega_r^{\,t}}\,g^{t}, \qquad r = 1, \dots, 4,
\]
explicitly
\[
\begin{aligned}
e_1 &= \tfrac14(1 + g + g^2 + g^3), & e_2 &= \tfrac14(1 - ig - g^2 + ig^3), \\
e_3 &= \tfrac14(1 - g + g^2 - g^3), & e_4 &= \tfrac14(1 + ig - g^2 - ig^3).
\end{aligned}
\]
A direct expansion confirms \( e_r^2 = e_r \), \( e_re_s = 0 \) for \( r \ne s \), and \( e_1 + e_2 + e_3 + e_4 = 1 \). For instance
\[
\begin{aligned}
16\,e_2^2 &= (1 - ig - g^2 + ig^3)^2 \\
&= 4 - 4ig - 4g^2 + 4ig^3 = 16\,e_2 ,
\end{aligned}
\]
where the middle equality collects the sixteen products \( (\pm 1, \pm i)g^{s+t} \) with \( g^4 = 1 \).
:::

The matrix in that example is, up to the factor \( \tfrac12 \) that normalizes its columns, the Fourier matrix of size four (@exm-fourier-matrix-4, @thm-fourier-matrix-unitary). That is not a coincidence, and a later section of this chapter explains it: the characters of a finite abelian group assemble into a Fourier matrix, and the isomorphism above is the discrete Fourier transform.

::: {#exm-wedderburn-of-m2}
[An algebra already in Wedderburn form]

What is the Wedderburn form of \( M_2(\nC) \), and what are its irreducible spaces?
:::

::: {.solution}
It is \( M_2(\nC) \) itself: \( k = 1 \) and \( n_1 = 2 \), with \( \dim = 4 = 2^2 \) and \( \dim Z = 1 \), the scalars (@prp-center-of-matrix-algebra). To see that the theorem applies, note that \( M_2(\nC) = C_1 \oplus C_2 \) where \( C_c \) is the set of matrices whose only non-zero column is the \( c \)-th; each \( C_c \) is a left ideal isomorphic to \( \nC^2 \) as an \( M_2(\nC) \)-space, and \( \nC^2 \) is irreducible, so @thm-semisimple-iff-sum-of-simples makes the algebra semisimple. There is exactly one isomorphism class of irreducible space, namely \( \nC^2 \), of dimension \( 2 \) — which is Step 6's description of \( k \) and \( n_1 \). Note that \( M_2(\nC) \) is **not** a product of two smaller algebras: it is simple (@thm-matrix-algebra-is-simple), while a product with \( k \ge 2 \) has the proper non-zero two-sided ideal \( e_1A \).
:::

## Exercises

### A. Check your understanding

::: {#exr-wedderburn-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State @thm-wedderburn with all of its hypotheses, and say which hypothesis fails for the upper triangular matrices in \( M_2(\nC) \).
2. Where in the proof is algebraic closure used, and what replaces the conclusion when it is dropped?
3. A semisimple algebra over \( \nC \) has dimension \( 5 \). List all possibilities for its Wedderburn form.
4. True or false, with a reason: a commutative semisimple algebra over \( \nC \) of dimension \( n \) is isomorphic to \( \nC^{n} \).
:::
:::

::: {.solution}
(a) \( F \) algebraically closed, \( A \ne \{0\} \) finite-dimensional over \( F \), and \( A \) semisimple, that is, every left ideal has a complementary left ideal. For the upper triangular matrices semisimplicity fails: \( \Span(\e_1) \) is an invariant subspace of the natural action with no invariant complement, and correspondingly the left ideal of matrices with second row zero has no complementary left ideal.

(b) In Step 4, in the second half of @thm-schurs-lemma, to know that \( s_{ii} \) is a scalar. Without algebraic closure the slots become \( M_{n_i}(D_i) \) for division algebras \( D_i \), which is the Wedderburn–Artin theorem quoted above and not proved here.

(c) We need positive integers with \( \sum n_i^2 = 5 \): either \( 1+4 \), giving \( \nC \times M_2(\nC) \), or \( 1+1+1+1+1 \), giving \( \nC^5 \).

(d) True. By @thm-wedderburn, \( A \cong \prod_i M_{n_i}(\nC) \), and \( M_{n_i}(\nC) \) is commutative only for \( n_i = 1 \) (otherwise \( \E_{11}\E_{12} \ne \E_{12}\E_{11} \)). So every \( n_i = 1 \) and \( k = \sum n_i^2 = n \).
:::

### B. Practice

::: {#exr-wedderburn-b1}
[B1: Determine which are semisimple]

Determine which of the following algebras over \( \nC \) are semisimple, and give the Wedderburn form of those that are. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. The diagonal matrices in \( M_3(\nC) \).
2. \( \nC[x]/(x^2) \).
3. \( \nC[x]/(x^2 - 1) \).
:::
:::

::: {.solution}
(a) Semisimple, and equal to \( \nC \times \nC \times \nC \) by @exm-products-of-matrix-algebras (i). As a check on semisimplicity: the algebra is the direct sum of the three left ideals \( \nC\E_{ii} \), each of dimension \( 1 \) and hence irreducible, so @thm-semisimple-iff-sum-of-simples applies.

(b) Not semisimple. Both algebras here are quotients of the infinite-dimensional algebra \( \nC[x] \) by the ideal generated by one polynomial (@def-ideal-polynomials, @def-quotient-algebra), and each has dimension \( 2 \), a basis being the classes of \( 1 \) and \( x \). Write \( \varepsilon \) for the class of \( x \) in \( \nC[x]/(x^2) \), so the algebra is \( \{a + b\varepsilon\} \) with \( \varepsilon^2 = 0 \). The line \( \nC\varepsilon \) is a left ideal, and it is the **only** one-dimensional one: a left ideal spanned by \( a + b\varepsilon \) with \( a \ne 0 \) contains \( \varepsilon(a + b\varepsilon) = a\varepsilon \), hence \( \varepsilon \), hence is at least two-dimensional. So \( \nC\varepsilon \) has no complementary left ideal, which would have to be one-dimensional. Consistently, a product of matrix algebras of dimension \( 2 \) would be \( \nC \times \nC \), which has no non-zero element squaring to \( 0 \).

(c) Semisimple, with Wedderburn form \( \nC \times \nC \). The map \( p + (x^2-1) \mapsto (p(1), p(-1)) \) is linear, multiplicative and unital, and on the representatives \( a + bx \) it reads \( (a+b, a-b) \), which vanishes only for \( a = b = 0 \); an injective linear map between spaces of dimension \( 2 \) is bijective (@thm-rank-nullity). A product of copies of \( \nC \) is semisimple by the argument in (a).
:::

::: {#exr-wedderburn-b2}
[B2: A dimension count]

Let \( A \) be a semisimple algebra over \( \nC \) with \( \dim A = 8 \) and \( \dim Z(A) = 5 \). Determine the Wedderburn form of \( A \), and the dimensions of the irreducible \( A \)-spaces.
:::

::: {.solution}
By @cor-dimension-count, \( k = \dim Z(A) = 5 \) and \( n_1^2 + \dots + n_5^2 = 8 \) with every \( n_i \ge 1 \). Writing \( 8 = 5 + 3 \), we need \( \sum(n_i^2 - 1) = 3 \), and \( n^2 - 1 \) takes the values \( 0, 3, 8, \dots \) for \( n = 1, 2, 3, \dots \). So exactly one \( n_i \) equals \( 2 \) and the rest equal \( 1 \). Hence
\[
A \cong \nC \times \nC \times \nC \times \nC \times M_2(\nC),
\]
and the irreducible \( A \)-spaces have dimensions \( 1, 1, 1, 1, 2 \).
:::

::: {#exr-wedderburn-b3}
[B3: The group algebra of a group of order three]

Let \( C_3 = \{1, g, g^2\} \) with \( g^3 = 1 \). Imitating @exm-wedderburn-of-c4, produce an explicit algebra isomorphism \( \nC[C_3] \to \nC^3 \) and write down the three idempotents.
:::

::: {.solution}
Let \( \omega = e^{2\pi i/3} \), so \( 1, \omega, \omega^2 \) are the cube roots of \( 1 \) and \( 1 + \omega + \omega^2 = 0 \). Define
\[
\begin{aligned}
\Phi\Bigl(\sum_{t=0}^{2}a_tg^{t}\Bigr)
 &= \Bigl(\sum_t a_t,\ \sum_t a_t\omega^{t},\ \sum_t a_t\omega^{2t}\Bigr).
\end{aligned}
\]
As in the example, \( \Phi \) is linear, multiplicative (because \( \omega^{s+t} = \omega^s\omega^t \) and \( \omega^3 = 1 \)) and unital. Its matrix has rows \( (1,1,1) \), \( (1, \omega, \omega^2) \), \( (1, \omega^2, \omega) \); it is a Vandermonde matrix in the distinct nodes \( 1, \omega, \omega^2 \), hence invertible. So \( \nC[C_3] \cong \nC^3 \), and \( \sum n_i^2 = 3 = \lvert C_3 \rvert \). The idempotents are
\[
\begin{aligned}
e_1 &= \tfrac13(1 + g + g^2), \\
e_2 &= \tfrac13(1 + \omega^{2}g + \omega g^{2}), \\
e_3 &= \tfrac13(1 + \omega g + \omega^{2}g^{2}),
\end{aligned}
\]
the \( r \)-th being \( \tfrac13\sum_t \conj{\omega^{(r-1)t}}g^{t} \).
:::

### C. Going deeper

::: {#exr-wedderburn-c1}
[C1: Simple plus semisimple]

Let \( F \) be algebraically closed and let \( A \ne \{0\} \) be a finite-dimensional semisimple \( F \)-algebra.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( A \) is simple (has no two-sided ideal but \( \{0\} \) and \( A \)) if and only if \( k = 1 \), that is, \( A \cong M_n(F) \) for some \( n \).
2. Deduce that a finite-dimensional simple semisimple algebra over \( \nC \) has square dimension.
:::

*Hint for (a): in a product, the set of elements whose slots after the first are zero is a two-sided ideal.*
:::

::: {.solution}
(a) \( (\Leftarrow) \) If \( k = 1 \) then \( A \cong M_n(F) \), which is simple by @thm-matrix-algebra-is-simple, and simplicity is preserved by an algebra isomorphism.

\( (\Rightarrow) \) Suppose \( k \ge 2 \) and write \( A \cong M_{n_1}(F) \times \dots \times M_{n_k}(F) \). The set \( I \) of elements whose slots \( 2, \dots, k \) are \( 0 \) is closed under addition and under multiplication by any element on either side, because multiplication is slot by slot; so \( I \) is a two-sided ideal. It is non-zero, since \( e_1 \in I \), and it is not all of \( A \), since \( e_2 \notin I \). So \( A \) is not simple. Contrapositively, simple forces \( k = 1 \).

(b) By (a), \( A \cong M_n(F) \), so \( \dim A = n^2 \) by @cor-dimension-count with \( k = 1 \).
:::

::: {#exr-wedderburn-c2}
[C2: How often each irreducible appears]

Keep the notation of @thm-wedderburn and of its proof, so that \( A = L_1 \oplus \dots \oplus L_m \) with each \( L_j \) isomorphic to exactly one \( V_i \). Let \( m_i \) be the number of indices \( j \) with \( L_j \cong V_i \). For \( A \)-spaces \( V, W \) write \( \operatorname{Hom}_A(V, W) \) for the vector space of homomorphisms of \( A \)-spaces \( V \to W \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( f \mapsto f(1_A) \) is a linear bijection \( \operatorname{Hom}_A(A, V) \to V \) for every \( A \)-space \( V \), where \( A \) carries the regular representation.
2. Prove that \( \dim\operatorname{Hom}_A(L_j, V_i) \) is \( 1 \) if \( L_j \cong V_i \) and \( 0 \) otherwise.
3. Deduce that \( m_i = n_i \): each irreducible appears in the regular representation exactly as many times as its dimension. Check the result against @cor-dimension-count.
:::

*Hint for (b): @thm-schurs-lemma, both parts.*
:::

::: {.solution}
(a) The map is linear. It is injective: if \( f(1_A) = \0 \) then \( f(a) = f(a1_A) = af(1_A) = \0 \) for every \( a \). It is surjective: given \( \v \in V \), the map \( a \mapsto a\v \) is linear and satisfies \( (ba)\v = b(a\v) \), so it is a homomorphism of \( A \)-spaces sending \( 1_A \) to \( \v \).

(b) If \( L_j \not\cong V_i \), the first part of @thm-schurs-lemma says every homomorphism between these irreducible spaces is \( 0 \), so the dimension is \( 0 \). If \( L_j \cong V_i \), fix an isomorphism \( h \); then \( f \mapsto h^{-1}f \) is a linear bijection \( \operatorname{Hom}_A(L_j, V_i) \to \operatorname{Hom}_A(L_j, L_j) \), and by the second part of @thm-schurs-lemma, valid because \( F \) is algebraically closed, every self-homomorphism of the irreducible space \( L_j \) is a scalar. So the dimension is \( 1 \).

(c) A homomorphism out of a direct sum is the list of its restrictions to the summands, so \( \operatorname{Hom}_A(A, V_i) \) is linearly isomorphic to \( \bigoplus_j \operatorname{Hom}_A(L_j, V_i) \), of dimension \( m_i \) by (b). By (a) that dimension is \( \dim V_i = n_i \). Hence \( m_i = n_i \). As a check, \( \dim A = \sum_j \dim L_j = \sum_i m_in_i = \sum_i n_i^2 \), which is @cor-dimension-count.
:::

::: {#exr-wedderburn-c3}
[C3: Change the field]

Let \( A = \{ x\I_2 + y\Q : x, y \in \nR \} \subseteq M_2(\nR) \), where \( \Q = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( A \) is a semisimple \( \nR \)-algebra of dimension \( 2 \).
2. Show that \( A \) is **not** isomorphic to a product \( M_{n_1}(\nR) \times \dots \times M_{n_k}(\nR) \), and identify which hypothesis of @thm-wedderburn fails.
3. Prove that \( A \) is itself a division algebra over \( \nR \) and identify it.
:::
:::

::: {.solution}
(a) \( \Q^2 = -\I_2 \), so \( A \) is closed under multiplication and is a subalgebra containing \( \I_2 \), of dimension \( 2 \). Every non-zero element \( x\I_2 + y\Q \) has determinant \( x^2 + y^2 > 0 \), hence is invertible in \( M_2(\nR) \), and its inverse \( (x^2+y^2)^{-1}(x\I_2 - y\Q) \) lies in \( A \). So every non-zero left ideal contains an invertible element and hence equals \( A \); the only left ideals are \( \{0\} \) and \( A \), and each has a complementary left ideal (the other one). So \( A \) is semisimple.

(b) A product with \( \sum n_i^2 = 2 \) must be \( \nR \times \nR \), which contains the non-zero element \( (1, 0) \) with \( (1,0)(0,1) = (0,0) \); but in \( A \) the product of two non-zero elements is non-zero, since both are invertible. So no such isomorphism exists. The hypothesis that fails is algebraic closure: \( \nR \) is not algebraically closed.

(c) By (a) every non-zero element of \( A \) is invertible, and its inverse again lies in \( A \), so \( A \) is a division algebra over \( \nR \); it is a copy of \( \nC \), the map \( x\I_2 + y\Q \mapsto x + yi \) being a bijective algebra homomorphism. This is the \( D_1 \) that would appear in the quoted Wedderburn–Artin form of \( A \).
:::
