# Burnside and the Double Commutant

Twice already the book has computed a commutant: Chapter 9 §04 found the matrices commuting with a basic Weyr matrix, and Chapter 11 §10 found the matrices commuting with a block diagonal matrix whose blocks have separated spectra. Both times the question was *given one operator, who commutes with it?* This section turns the question round. Given a whole algebra of operators, how much of the algebra can be read off from its commutant, and when is the algebra as large as it could possibly be? Two theorems answer this. Burnside's theorem says that over an algebraically closed field an algebra with no invariant subspace to hide in must be everything; the double commutant theorem says that a semisimple algebra is exactly the set of operators commuting with everything that commutes with it.

Throughout, \( V \) is a finite-dimensional vector space over a field \( F \), and \( \End(V) \) is the space \( \cL(V) \) of operators regarded as an algebra under composition. A **subalgebra** \( A \subseteq \End(V) \) contains \( \id_V \) by (SA3) of @def-subalgebra; this is not decoration, and the warning after @thm-double-commutant shows what goes wrong without it.

## Commutants, and when an operator is a scalar

For a subalgebra \( A \subseteq \End(V) \), @def-commutant sets
\[
A' = \{ t \in \End(V) : ta = at \text{ for all } a \in A \},
\]
and @prp-commutant-is-algebra says \( A' \) is again a subalgebra containing \( \id_V \).

Applying the prime twice gives the **double commutant** \( A'' \coloneqq (A')' \). One inclusion is free and worth recording at once: by @prp-commutant-is-algebra (c),
\[
A \subseteq A'' .
\]
The content of this section is that the reverse inclusion holds under a hypothesis we can name exactly.

Both theorems below end by proving that some operator is a scalar, and §01 has already supplied the fact that lets us conclude this. By @prp-center-of-matrix-algebra the center of \( M_n(F) \) consists of the scalar matrices or, in the operator form recorded there, for a finite-dimensional \( V \ne \{\0\} \) the operators commuting with every operator on \( V \) are exactly the scalar multiples of \( \id_V \):
\[
\End(V)' = \{\lambda\,\id_V : \lambda \in F\} .
\]
Nothing new is proved here; it is the operator form that the proofs below call on.

## Algebras that act irreducibly

Recall from §03 that \( V \) is **irreducible** as an \( A \)-space (§03 calls such a space simple, @def-simple-module) when \( V \ne \{\0\} \) and the only \( A \)-invariant subspaces of \( V \) are \( \{\0\} \) and \( V \). The following one-line consequence is used in every proof of this section, so we isolate it.

::: {#lem-orbit-of-a-vector}
[An Irreducible Algebra Moves One Vector Everywhere]

Let \( A \subseteq \End(V) \) be a subalgebra with \( \id_V \in A \), acting irreducibly on \( V \). Then \( A\v \coloneqq \{ a\v : a \in A \} = V \) for every \( \v \ne \0 \).
:::

::: {.proof}
The set \( A\v \) is the image of the linear map \( A \to V \), \( a \mapsto a\v \), hence a subspace. It is \( A \)-invariant: \( b(a\v) = (ba)\v \in A\v \) for \( b \in A \), since \( ba \in A \). It contains \( \id_V\v = \v \ne \0 \), so it is not \( \{\0\} \). Irreducibility leaves only \( A\v = V \).
:::

::: {.warning}
**The assumption \( \id_V \in A \) is doing real work here.** Take \( V = F \), a line, and \( A = \{0\} \), a subspace closed under composition but not a subalgebra, since it does not contain \( \id_V \). The only subspaces of \( V \) at all are \( \{\0\} \) and \( V \), so \( A \) satisfies the letter of irreducibility, yet \( A\v = \{\0\} \ne V \) and \( A \ne \End(V) = F \). Every statement below about an algebra acting irreducibly assumes the identity belongs to the algebra.
:::

## Burnside's theorem

Here is the question. An algebra \( A \subseteq \End(V) \) that acts irreducibly has nowhere to hide: no proper non-zero subspace survives it. Does that force \( A \) to be all of \( \End(V) \)? Over \( \nC \) the answer is yes. The proof is worth the trouble: the corollary below, which says that an irreducibly acting **set** of operators already spans \( \End(V) \), is what the representation theory later in this chapter uses to turn statements about a group into statements about all matrices.

::: {#thm-burnside}
[Burnside's Theorem]

Let \( F \) be an **algebraically closed** field, that is, one in which every non-constant polynomial in \( F[x] \) has a root. Let \( V \) be a vector space over \( F \) with \( 1 \le \dim V < \infty \), and let \( A \subseteq \End(V) \) be a subalgebra with \( \id_V \in A \). If \( V \) is irreducible as an \( A \)-space, then
\[
A = \End(V).
\]
:::

::: {.idea}
**Step roadmap.** ① Among the non-zero members of \( A \), let \( r \) be the smallest rank, attained at \( a \). ② Show \( r = 1 \). If \( r \ge 2 \), the image \( \im a \) has two independent vectors \( a\u_1, a\u_2 \), and irreducibility supplies \( b \in A \) carrying \( a\u_1 \) to \( \u_2 \). The operator \( ab \) maps \( \im a \) into itself; an eigenvalue \( \lambda \) of that restriction — this is the one place algebraic closure is spent — makes \( aba - \lambda a \) a member of \( A \) of strictly smaller rank, hence zero, and then \( a\u_2 = \lambda\,a\u_1 \) contradicts independence. ③ One rank-one operator \( \v_0\varphi_0 \) in \( A \) gives all of them: multiplying on the left moves \( \v_0 \) anywhere, and multiplying on the right moves \( \varphi_0 \) anywhere. ④ Rank-one operators span \( \End(V) \).
:::

:::: {.proof}
Write \( \v\varphi \) for the operator \( \x \mapsto \varphi(\x)\v \), where \( \v \in V \) and \( \varphi \in V^{*} \); it has rank \( 1 \) exactly when \( \v \ne \0 \) and \( \varphi \ne 0 \), and every operator of rank at most \( 1 \) has this form, since an operator with image \( \Span(\v) \), \( \v \ne \0 \), sends each \( \x \) to a unique multiple \( \varphi(\x)\v \), and \( \varphi \) so defined is linear.

**Step 1: a member of least rank.** Since \( \id_V \in A \) and \( \dim V \ge 1 \), the set \( \{ a \in A : a \ne 0 \} \) is non-empty. Let
\[
r = \min\{\rank a : a \in A,\ a \ne 0\} \ge 1 ,
\]
and fix \( a \in A \) with \( a \ne 0 \) and \( \rank a = r \).

**Step 2: \( r = 1 \).** Suppose \( r \ge 2 \). Then \( \dim \im a \ge 2 \), so there are \( \u_1, \u_2 \in V \) with \( a\u_1 \) and \( a\u_2 \) independent; in particular \( a\u_1 \ne \0 \). By @lem-orbit-of-a-vector there is \( b \in A \) with \( b(a\u_1) = \u_2 \).

Put \( W = \im a \), a subspace of dimension \( r \). Then \( ab(W) \subseteq \im a = W \), so \( s \coloneqq (ab)|_{W} \) is an operator on \( W \). Its characteristic polynomial \( p_s \) is monic of degree \( r \ge 1 \), hence non-constant, hence has a root \( \lambda \in F \) because \( F \) is algebraically closed; by @thm-eigenvalue-characterizations, \( \lambda \) is an eigenvalue of \( s \), so \( \ker(s - \lambda\,\id_W) \ne \{\0\} \).

Consider \( c \coloneqq aba - \lambda a \), which lies in \( A \) because \( A \) is closed under products and linear combinations. For every \( \x \in V \),
\[
c\,\x = (ab - \lambda\,\id_V)(a\x) = (s - \lambda\,\id_W)(a\x),
\]
the second equality because \( a\x \in W \). Hence \( \im c = (s - \lambda\,\id_W)(W) \), and @thm-rank-nullity applied to \( s - \lambda\,\id_W \) on \( W \) gives
\[
\rank c = r - \dim\ker(s - \lambda\,\id_W) \le r - 1 .
\]
By the minimality of \( r \), an element of \( A \) of rank less than \( r \) must be \( 0 \), so \( c = 0 \), that is, \( aba = \lambda a \). Applying both sides to \( \u_1 \) and using \( ba\u_1 = \u_2 \),
\[
a\u_2 = (aba)\u_1 = \lambda\,a\u_1 ,
\]
which contradicts the independence of \( a\u_1 \) and \( a\u_2 \). Therefore \( r = 1 \).

**Step 3: \( A \) contains every operator of rank at most one.** By Step 2 there is \( a_0 \in A \) with \( \rank a_0 = 1 \); write \( a_0 = \v_0\varphi_0 \) with \( \v_0 \ne \0 \) and \( \varphi_0 \ne 0 \).

*Left multiplication.* For \( b \in A \) and \( \x \in V \) we get \( b\,a_0\,\x = \varphi_0(\x)\,b\v_0 \), that is, \( b a_0 = (b\v_0)\varphi_0 \). By @lem-orbit-of-a-vector, \( A\v_0 = V \), so
\[
\v\varphi_0 \in A \qquad \text{for every } \v \in V .
\]

*Right multiplication.* For \( c \in A \) we get \( a_0 c = \v_0(\varphi_0 \circ c) \). Put
\[
S = \{\, \varphi_0 \circ c : c \in A \,\} \subseteq V^{*},
\]
the image of the linear map \( A \to V^{*} \), \( c \mapsto \varphi_0 \circ c \), and hence a subspace of \( V^{*} \).

::: {.claim}
\( S = V^{*} \).
:::

::: {.proof}
Let \( U = \{ \x \in V : \varphi(\x) = 0 \text{ for every } \varphi \in S \} \), a subspace of \( V \). It is \( A \)-invariant: if \( \x \in U \) and \( d \in A \), then for every \( c \in A \) we have \( cd \in A \) and so \( \varphi_0(c(d\x)) = \varphi_0((cd)\x) = 0 \), whence \( d\x \in U \). It is not all of \( V \): taking \( c = \id_V \) shows \( \varphi_0 \in S \), and \( \varphi_0 \ne 0 \) gives some \( \x \) with \( \varphi_0(\x) \ne 0 \). Irreducibility therefore forces \( U = \{\0\} \).

Let \( d = \dim S \) and pick a basis \( \varphi_1, \dots, \varphi_d \) of \( S \). The linear map \( \Theta \colon V \to F^{d} \), \( \Theta(\x) = (\varphi_1(\x), \dots, \varphi_d(\x)) \), has kernel exactly \( U = \{\0\} \), since a vector killed by a basis of \( S \) is killed by all of \( S \). So \( \Theta \) is injective and @thm-rank-nullity gives \( \dim V \le d \). On the other hand \( S \) is a subspace of \( V^{*} \), and \( \dim V^{*} = \dim V \) by @cor-dimension-dual-space, so \( d \le \dim V \). Hence \( d = \dim V^{*} \) and \( S = V^{*} \) by @thm-dim-impl-eq.
:::

Now let \( \v \in V \) and \( \varphi \in V^{*} \) be arbitrary. Choose \( c \in A \) with \( \varphi = \varphi_0 \circ c \), which the Claim allows, and \( b \in A \) with \( b\v_0 = \v \), which @lem-orbit-of-a-vector allows when \( \v \ne \0 \) (and for \( \v = \0 \) take \( b = 0 \)). Then for every \( \x \),
\[
(b\,a_0\,c)\x = b\bigl(\varphi_0(c\x)\,\v_0\bigr) = \varphi(\x)\,\v ,
\]
so \( \v\varphi = b a_0 c \in A \).

**Step 4: rank-one operators span.** Let \( t \in \End(V) \), let \( (\v_1, \dots, \v_n) \) be a basis of \( V \) and \( (\varphi_1, \dots, \varphi_n) \) its dual basis (@def-dual-basis). The operator \( \sum_{i=1}^{n} (t\v_i)\varphi_i \) sends \( \v_j \) to \( t\v_j \) for each \( j \), because \( \varphi_i(\v_j) = \delta_{ij} \); two operators agreeing on a basis are equal, so \( t = \sum_i (t\v_i)\varphi_i \). Each summand lies in \( A \) by Step 3, and \( A \) is a subspace, so \( t \in A \). This proves \( A = \End(V) \).
::::

The theorem is stronger than it may look. It says that irreducibility, a statement about *subspaces*, forces a statement about *dimension*: over an algebraically closed field, an irreducibly acting subalgebra of \( \End(V) \) has dimension exactly \( (\dim V)^2 \), the largest possible. There is no room between "acts irreducibly" and "is everything".

The version about sets rather than algebras is worth recording alongside it, since a group of invertible operators is a set closed under composition and not a subspace.

::: {#cor-irreducible-set-spans}
[An Irreducible Multiplicative Set Spans the Whole Algebra]

Let \( F \) be algebraically closed, \( V \) a vector space over \( F \) with \( 1 \le \dim V < \infty \), and let \( \cS \subseteq \End(V) \) be a set with \( \id_V \in \cS \) that is closed under composition. If the only subspaces \( U \subseteq V \) with \( s(U) \subseteq U \) for all \( s \in \cS \) are \( \{\0\} \) and \( V \), then \( \Span(\cS) = \End(V) \).
:::

::: {.proof}
Put \( A = \Span(\cS) \). It is a subspace containing \( \id_V \), and it is closed under multiplication: a product of two linear combinations of members of \( \cS \) expands, by bilinearity of composition, into a linear combination of products of members of \( \cS \), which lie in \( \cS \). So \( A \) is a subalgebra. A subspace \( U \) is \( A \)-invariant if and only if it is invariant under every member of \( \cS \), since invariance is preserved by linear combinations. So \( V \) is irreducible as an \( A \)-space, and @thm-burnside gives \( A = \End(V) \).
:::

::: {.warning}
**Burnside is false over a field that is not algebraically closed.** Let \( F = \nR \), \( V = \nR^2 \) and
\[
A = \left\{ \begin{pmatrix} x & -y \\ y & x \end{pmatrix} : x, y \in \nR \right\},
\]
the span of \( \I_2 \) and \( \Q = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \). Since \( \Q^2 = -\I_2 \), this is a subalgebra, and it acts irreducibly: an invariant line would be spanned by a real eigenvector of \( \Q \), and \( p_{\Q} = x^2 + 1 \) has no real root. Yet \( \dim A = 2 \), not \( 4 \), so \( A \ne M_2(\nR) \). This is the same witness §04 used against the second half of Schur's lemma (@thm-schurs-lemma), and the reason is the same: an operator on a real space need have no eigenvalue, and Step 2 of the proof needs one.
:::

::: {.check}
Let \( A \subseteq M_2(\nC) \) be the subalgebra generated by \( \X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) and \( \Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \). Without computing products, what must \( \dim A \) be, and why?
:::

::: {.solution}
It must be \( 4 \), so \( A = M_2(\nC) \). A one-dimensional invariant subspace would be a common eigenvector of \( \X \) and \( \Z \). The eigenvectors of \( \Z \) are the multiples of \( \e_1 \) and of \( \e_2 \), and \( \X\e_1 = \e_2 \) is not a multiple of \( \e_1 \), nor is \( \X\e_2 = \e_1 \) a multiple of \( \e_2 \). So \( A \) acts irreducibly on \( \nC^2 \), and @thm-burnside gives \( A = M_2(\nC) \). Directly: \( \I_2, \X, \Z \) and \( \X\Z = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \) are independent, which confirms it.
:::

## The double commutant theorem

Burnside handles the irreducible case. The general case is not "\( A \) is everything" — a diagonal algebra is not everything — but a statement about how faithfully \( A \) is recorded by its commutant. The right hypothesis is semisimplicity of the action, and it cannot be weakened to nothing, as the warning below shows.

The engine is a single step: an operator in \( A'' \) can be matched by a member of \( A \) on **one** given vector.

::: {#lem-one-vector-density}
[Matching on One Vector]

Let \( W \) be a finite-dimensional vector space over \( F \) and let \( B \subseteq \End(W) \) be a subalgebra with \( \id_W \in B \) which acts **semisimply** on \( W \): every \( B \)-invariant subspace of \( W \) has a \( B \)-invariant complement (@def-semisimple-algebra). Then for every \( t \in B'' \) and every \( \w \in W \) there is \( b \in B \) with \( b\w = t\w \).
:::

::: {.idea}
The subspace \( B\w \) is invariant, so it has an invariant complement, and the projection \( p \) onto \( B\w \) along that complement commutes with \( B \). Being in \( B'' \), the operator \( t \) commutes with \( p \), hence cannot move \( \w \) out of the image of \( p \), which is \( B\w \).
:::

::: {.proof}
Put \( U = B\w = \{b\w : b \in B\} \), a subspace of \( W \) (the image of \( b \mapsto b\w \)) which is \( B \)-invariant, since \( b_1(b\w) = (b_1b)\w \) for \( b_1 \in B \). By hypothesis there is a \( B \)-invariant subspace \( U_1 \) with \( W = U \oplus U_1 \). Let \( p \in \End(W) \) be the projection onto \( U \) along \( U_1 \) (@thm-projection-direct-sum (b)).

\( p \in B' \). Indeed, let \( b \in B \) and write \( \x = \u + \u_1 \) with \( \u \in U \), \( \u_1 \in U_1 \). Then \( b\u \in U \) and \( b\u_1 \in U_1 \) by invariance, so \( b\x = b\u + b\u_1 \) is the decomposition of \( b\x \), giving \( p(b\x) = b\u = b(p\x) \).

Since \( t \in B'' \) and \( p \in B' \), we have \( tp = pt \). Also \( \w = \id_W\w \in B\w = U \), so \( p\w = \w \). Therefore
\[
t\w = t(p\w) = p(t\w) \in \im p = U = B\w ,
\]
so \( t\w = b\w \) for some \( b \in B \).
:::

Matching on one vector is not yet matching everywhere. The trick that upgrades it is to run the lemma not on \( V \) but on \( n \) copies of \( V \) at once, where one cleverly chosen vector carries a whole basis.

::: {#thm-double-commutant}
[Double Commutant Theorem]

Let \( F \) be **any** field, let \( V \) be a finite-dimensional vector space over \( F \), and let \( A \subseteq \End(V) \) be a subalgebra with \( \id_V \in A \). Assume that \( A \) acts **semisimply** on \( V \): every \( A \)-invariant subspace of \( V \) has an \( A \)-invariant complement (@def-semisimple-algebra). Then
\[
A'' = A .
\]
:::

::: {.idea}
**Step roadmap.** ① @lem-one-vector-density matches \( t \in A'' \) with some \( a \in A \) on one vector. ② To match on a whole basis at once, let \( A \) act diagonally on \( V^{n} = V \oplus \dots \oplus V \) (\( n = \dim V \)) and apply the lemma there to the single vector whose \( n \) entries are the basis vectors. ③ For that we must check two things about the copied algebra \( \tilde A \): that it still acts semisimply, which @thm-semisimple-iff-sum-of-simples supplies, and that \( \tilde t \) lies in \( \tilde A'' \), which is a computation with the \( n \times n \) array of components of an operator on \( V^n \).
:::

::: {.proof}
The inclusion \( A \subseteq A'' \) was noted above, so only \( A'' \subseteq A \) needs proof. Let \( t \in A'' \), let \( n = \dim V \); if \( n = 0 \) there is nothing to prove, so let \( n \ge 1 \).

**Step 1: the copied algebra.** Let \( V^{n} = V \oplus \dots \oplus V \) be the product of \( n \) copies of \( V \) (@def-product-of-spaces), and for \( s \in \End(V) \) let \( \tilde s \in \End(V^{n}) \) be given by \( \tilde s(\x_1, \dots, \x_n) = (s\x_1, \dots, s\x_n) \). The map \( s \mapsto \tilde s \) is linear and satisfies \( \widetilde{s_1s_2} = \tilde s_1\tilde s_2 \) and \( \widetilde{\id_V} = \id_{V^{n}} \), so \( \tilde A = \{\tilde a : a \in A\} \) is a subalgebra of \( \End(V^{n}) \) containing the identity.

**Step 2: \( \tilde A \) acts semisimply on \( V^{n} \).** Since \( A \) acts semisimply on \( V \), @thm-semisimple-iff-sum-of-simples writes \( V = W_1 + \dots + W_q \) with each \( W_j \) an irreducible \( A \)-invariant subspace. For \( 1 \le k \le n \) let \( \iota_k \colon V \to V^{n} \) place a vector in the \( k \)-th slot and \( \0 \) elsewhere; it is injective and satisfies \( \iota_k(s\x) = \tilde s\,\iota_k(\x) \). Hence \( \iota_k(W_j) \) is \( \tilde A \)-invariant, and it is irreducible, because \( \iota_k \) carries the \( A \)-invariant subspaces of \( W_j \) bijectively onto the \( \tilde A \)-invariant subspaces of \( \iota_k(W_j) \). Every element of \( V^{n} \) is the sum of its \( n \) slots, so
\[
V^{n} = \sum_{k=1}^{n}\sum_{j=1}^{q} \iota_k(W_j) ,
\]
a sum of irreducible \( \tilde A \)-invariant subspaces. By the converse half of @thm-semisimple-iff-sum-of-simples, \( \tilde A \) acts semisimply on \( V^{n} \).

**Step 3: \( \tilde t \in \tilde A'' \).** Let \( \pi_k \colon V^{n} \to V \) be the \( k \)-th coordinate map. Every \( s \in \End(V^{n}) \) is determined by its components \( s_{kl} = \pi_k \circ s \circ \iota_l \in \End(V) \), through \( \pi_k(s\x) = \sum_{l} s_{kl}\x_l \). Comparing components in \( s\tilde a = \tilde a s \) gives
\[
(s\tilde a)_{kl} = s_{kl}\,a, \qquad (\tilde a s)_{kl} = a\,s_{kl},
\]
so \( s \in \tilde A' \) if and only if every \( s_{kl} \) lies in \( A' \). Now let \( s \in \tilde A' \). Then \( (\tilde t s)_{kl} = t\,s_{kl} \) and \( (s\tilde t)_{kl} = s_{kl}\,t \), and these agree because \( s_{kl} \in A' \) and \( t \in A'' \). Hence \( \tilde t \) commutes with every \( s \in \tilde A' \), that is, \( \tilde t \in \tilde A'' \).

**Step 4: conclude.** Let \( (\v_1, \dots, \v_n) \) be a basis of \( V \) and put \( \tilde\v = (\v_1, \dots, \v_n) \in V^{n} \). By Steps 1–3 the hypotheses of @lem-one-vector-density hold for \( B = \tilde A \) on \( W = V^{n} \), with \( \tilde t \in \tilde A'' \). So there is \( a \in A \) with \( \tilde a\,\tilde\v = \tilde t\,\tilde\v \), that is, \( a\v_i = t\v_i \) for every \( i \). Two operators agreeing on a basis are equal, so \( t = a \in A \). This proves \( A'' \subseteq A \), and with the reverse inclusion, \( A'' = A \).
:::

Notice which hypotheses were used where. Algebraic closure was **not** used: the double commutant theorem holds over every field, unlike Burnside. Finite dimension was used for the basis in Step 4 and inside @thm-semisimple-iff-sum-of-simples. Semisimplicity was used exactly once, to produce the invariant complement in @lem-one-vector-density.

::: {.warning}
**Neither hypothesis can simply be dropped.**

*Without the identity.* Take \( A = \{0\} \subseteq \End(F^2) \), a subspace closed under composition but with no identity element of \( \End(F^2) \) in it. Every subspace of \( F^2 \) is \( A \)-invariant and every subspace has a complement, so the condition on invariant complements holds; but \( A' = M_2(F) \) and \( A'' = \{\lambda\I_2\} \) by @prp-center-of-matrix-algebra, so \( A'' \ne A \).

*Without semisimplicity.* Let \( A \subseteq M_2(F) \) be the upper triangular matrices. The line \( \Span(\e_1) \) is \( A \)-invariant, and it is the **only** invariant line: if \( \v = (v_1, v_2) \) has \( v_2 \ne 0 \), then \( \E_{12}\v = v_2\e_1 \) is a non-zero multiple of \( \e_1 \) and does not lie in \( \Span(\v) \). A complement of \( \Span(\e_1) \) would be an invariant line other than \( \Span(\e_1) \), so there is none and \( A \) does not act semisimply. Here \( A' = \{\lambda\I_2\} \): a matrix commuting with \( \E_{11} \) and \( \E_{22} \) is diagonal, and commuting with \( \E_{12} \) then forces the two diagonal entries to agree. Hence \( A'' = \{\lambda\I_2\}' = M_2(F) \), which is strictly larger than \( A \).
:::

::: {.remark}
Semisimplicity is sufficient but not necessary. Let \( \N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) and \( A = \{ x\I_2 + y\N \} \). Solving \( \X\N = \N\X \) gives exactly the matrices \( x\I_2 + y\N \), so \( A' = A \) and therefore \( A'' = A \) — even though \( A \) does not act semisimply, the invariant line \( \Span(\e_1) = \ker\N \) again being the only one.
:::

::: {.remark}
The name has two sources. In finite dimensions the result above is due to Wedderburn, and the argument through \( n \) copies of \( V \) is the finite-dimensional shadow of Jacobson's density theorem, which we do not prove. For algebras of operators on a Hilbert space there is an analytic statement of the same shape, von Neumann's double commutant theorem, which is outside this book.
:::

## The commutant of one operator, revisited

The two earlier computations of the book now read as computations of \( A' \) for the smallest interesting algebra: the one generated by a single operator.

::: {#cor-weyr-commutant-revisited}
[The Commutant of a Single Operator]

Let \( V \) be a finite-dimensional vector space over \( F \), let \( T \in \cL(V) \), and let \( A = F[T] \subseteq \End(V) \) be the algebra of all polynomials in \( T \). Then
\[
A' = \{ S \in \cL(V) : ST = TS \}.
\]
Consequently the following two earlier results are computations of \( A' \).

::: {.enumerate options="label=(\alph*)"}
1. If \( F = \nC \) and the matrix of \( T \) in some basis is \( \A_1 \oplus \dots \oplus \A_r \) with the \( \A_p \) of pairwise disjoint spectra, then in that same basis every member of \( A' \) has a block **diagonal** matrix for the partition into those block sizes (@cor-commutant-block-diagonal).
2. If the matrix of \( T \) in some basis is a basic Weyr matrix of Weyr structure \( (w_1, \dots, w_s) \), then in that same basis every member of \( A' \) has a block **upper triangular** matrix for the partition \( w_1 + \dots + w_s \) (@prp-weyr-commutant).
:::

If moreover \( T \) is diagonalizable with distinct eigenvalues \( \lambda_1, \dots, \lambda_k \) and \( d_i = \dim E_{\lambda_i}(T) \), then \( A \) acts semisimply, \( \dim A = k \), \( \dim A' = \sum_{i=1}^{k} d_i^2 \), and \( A'' = A \).
:::

::: {.idea}
Nothing in (a) and (b) is new: whatever commutes with \( T \) commutes with every polynomial in it, so the two earlier computations were computations of \( A' \) all along. The diagonalizable case is where the second commutant enters. The Lagrange polynomials evaluated at \( T \) are the projections onto the eigenspaces, and they turn out to be a basis of \( A \); a commuting operator is exactly one that preserves each eigenspace and is otherwise unconstrained, which counts \( A' \); and the same projections assemble an invariant complement for any invariant subspace, which is the hypothesis @thm-double-commutant needs.
:::

::: {.proof}
An operator commutes with every polynomial in \( T \) as soon as it commutes with \( T \), and \( T \in A \); this gives the displayed description of \( A' \). Parts (a) and (b) are then the cited results verbatim, read for the matrix of \( T \) in the given basis.

For the last sentence, let \( T \) be diagonalizable, \( E_i = E_{\lambda_i}(T) \), so \( V = E_1 \oplus \dots \oplus E_k \) by @thm-diagonalization (c). Let \( \ell_i \in F[x] \) be the Lagrange polynomial with \( \ell_i(\lambda_j) = \delta_{ij} \) (@thm-lagrange-interpolation) and \( P_i = \ell_i(T) \). Evaluating on each \( E_j \), where \( T \) acts as \( \lambda_j \), shows \( P_i \) is the projection onto \( E_i \) along the other summands. Since \( T^{m} = \sum_i \lambda_i^{m}P_i \) for every \( m \ge 0 \), the algebra \( A \) is spanned by \( P_1, \dots, P_k \), which are independent because \( P_i P_j = \delta_{ij}P_i \) and each \( P_i \ne 0 \): applying \( \sum_i c_iP_i = 0 \) to a non-zero vector of \( E_j \) gives \( c_j = 0 \). So \( \dim A = k \).

By @thm-commuting-preserves-eigenspaces, every \( S \in A' \) maps each \( E_i \) into itself; conversely such an \( S \) commutes with \( T \), because both \( ST \) and \( TS \) act as \( \lambda_i S \) on \( E_i \). So \( A' \) is the set of operators preserving all the \( E_i \), and restricting gives a linear bijection \( A' \to \End(E_1) \times \dots \times \End(E_k) \); hence \( \dim A' = \sum_i d_i^2 \). Each \( P_i \) preserves every \( E_j \), so \( P_i \in A' \).

Finally, \( A \) acts semisimply. Let \( U \) be an \( A \)-invariant subspace. Then \( U \) is \( T \)-invariant, and \( T|_U \) is diagonalizable (@cor-restriction-diagonalizable), so \( U \) has a basis of eigenvectors of \( T \) (@thm-diagonalization, (a) \( \Leftrightarrow \) (b)) and therefore \( U = (U \cap E_1) \oplus \dots \oplus (U \cap E_k) \). Choose a complement \( C_i \) of \( U \cap E_i \) inside \( E_i \) for each \( i \) (@thm-complement-exists) and put \( C = C_1 \oplus \dots \oplus C_k \). Then \( V = U \oplus C \), and \( C \) is \( A \)-invariant because \( P_j(C) = C_j \subseteq C \) and the \( P_j \) span \( A \). So @thm-double-commutant applies and gives \( A'' = A \).
:::

So the diagonalizable case is an instance of @thm-double-commutant, reached here by hand; the Weyr case in (b) is **not**, since \( F[\W] \) does not act semisimply once \( s \ge 2 \). That is the honest shape of the relationship: the two earlier sections computed first commutants in cases where the second commutant theorem has nothing to say, and this section explains what extra hypothesis would make the computation reversible.

::: {#exm-commutants-of-two-extremes}
[The Two Extremes]

Inside \( M_n(F) \) with \( n \ge 2 \), compute \( A' \) and \( A'' \) for (i) \( A \) the diagonal matrices, and (ii) \( A \) the scalar matrices.
:::

::: {.solution}
(i) Let \( A = \{\diag(c_1, \dots, c_n)\} \). Then \( \X \) commutes with \( \E_{ii} \) for every \( i \) exactly when \( \X \) is diagonal, since \( (\X\E_{ii})_{kl} = x_{ki}\delta_{il} \) and \( (\E_{ii}\X)_{kl} = \delta_{ik}x_{il} \), and comparing at \( (k, i) \) with \( k \ne i \) gives \( x_{ki} = 0 \). So \( A' = A \), and applying the prime again, \( A'' = A' = A \). This agrees with @thm-double-commutant: the diagonal algebra acts semisimply, \( F^{n} \) being the direct sum of the \( n \) coordinate lines, each of which is invariant and one-dimensional, hence irreducible.

(ii) Let \( A = \{\lambda\I_n\} \). Every matrix commutes with a scalar matrix, so \( A' = M_n(F) \), and \( A'' = M_n(F)' = \{\lambda\I_n\} = A \) by @prp-center-of-matrix-algebra. Again \( A'' = A \), as it must be: the scalars act semisimply because every subspace is invariant and every subspace has a complement.

The two examples sit at opposite ends. In (i) the commutant is as small as the algebra; in (ii) the commutant is everything. In both, applying the prime a second time returns to the start, which is what the theorem promises whenever the action is semisimple.
:::

## Exercises

### A. Check your understanding

::: {#exr-double-commutant-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State Burnside's theorem, with every hypothesis.
2. Give the field hypothesis of @thm-double-commutant, and say why it differs from the one in (a).
3. True or false, with a reason: if \( A \subseteq \End(V) \) is a subalgebra containing \( \id_V \), then \( A''' = A' \).
4. Explain in one sentence why \( \{\0\} \) and \( V \) being the only \( A \)-invariant subspaces does **not** by itself imply \( A\v = V \) for \( \v \ne \0 \).
:::
:::

::: {.solution}
(a) \( F \) algebraically closed, \( V \) finite-dimensional over \( F \) with \( \dim V \ge 1 \), \( A \subseteq \End(V) \) a subalgebra containing \( \id_V \), and \( V \) irreducible as an \( A \)-space; the conclusion is \( A = \End(V) \).

(b) @thm-double-commutant has no field hypothesis at all: it holds over every field. Algebraic closure entered Burnside only to produce an eigenvalue of \( (ab)|_{\im a} \), and the double commutant proof never needs an eigenvalue — it needs an invariant complement, which semisimplicity hands over directly.

(c) True, and it holds for any subset: it is @prp-commutant-is-algebra (d). The two ingredients are (c) of that proposition, \( \cS \subseteq \cS'' \), and (b), that \( \cS \subseteq \cT \) implies \( \cT' \subseteq \cS' \). Applying the prime to \( A \subseteq A'' \) gives \( A''' \subseteq A' \), and applying the inclusion \( B \subseteq B'' \) to \( B = A' \) gives \( A' \subseteq A''' \).

(d) Because \( A\v \) could be \( \{\0\} \) if \( A \) contained no operator sending \( \v \) anywhere non-zero; the identity in \( A \) is what rules this out, as in the warning after @lem-orbit-of-a-vector.
:::

### B. Practice

::: {#exr-double-commutant-b1}
[B1: Determine which are irreducible]

For each subalgebra of \( M_2(\nC) \), determine whether it acts irreducibly on \( \nC^2 \), and hence whether it equals \( M_2(\nC) \). Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. The algebra generated by \( \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \).
2. The algebra generated by \( \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) and \( \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix} \).
3. The algebra of all matrices \( \begin{pmatrix} a & b \\ 0 & a \end{pmatrix} \).
:::
:::

::: {.solution}
(a) Not irreducible. With \( \N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) we have \( \N^2 = \0 \), so the algebra is \( \{x\I_2 + y\N\} \), and \( \Span(\e_1) = \im\N \) is invariant, proper and non-zero. It is not \( M_2(\nC) \); its dimension is \( 2 \).

(b) Irreducible, so it equals \( M_2(\nC) \) by @thm-burnside. The eigenvectors of \( \diag(1, i) \) are the multiples of \( \e_1 \) and of \( \e_2 \) (the diagonal entries are distinct), and the swap matrix maps each of those lines to the other, so no line is invariant under both.

(c) Not irreducible: this is the algebra of (a), written out. The invariant line is again \( \Span(\e_1) \).
:::

::: {#exr-double-commutant-b2}
[B2: A commutant and a double commutant]

Let \( \A = \diag(1, 1, 2) \in M_3(\nR) \) and let \( A = \nR[\A] \subseteq M_3(\nR) \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \dim A \).
2. Describe \( A' \) explicitly and compute \( \dim A' \).
3. Compute \( A'' \), and check the answer against @thm-double-commutant.
:::
:::

::: {.solution}
(a) The eigenvalues are \( 1 \) and \( 2 \), each with a non-zero eigenspace, so \( m_{\A} = (x-1)(x-2) \) and, by the count in @cor-weyr-commutant-revisited with \( k = 2 \), \( \dim A = 2 \): a basis is \( \I_3, \A \), equivalently \( \P_1 = \diag(1,1,0) \), \( \P_2 = \diag(0,0,1) \).

(b) \( E_1 = \Span(\e_1, \e_2) \) and \( E_2 = \Span(\e_3) \). Every matrix in \( A' \) preserves both (@thm-commuting-preserves-eigenspaces), and conversely a matrix preserving both commutes with \( \A \), since \( \A \) acts as a scalar on each; so a matrix lies in \( A' \) exactly when it has the shape
\[
\begin{pmatrix} p & q & 0 \\ u & v & 0 \\ 0 & 0 & w \end{pmatrix}.
\]
Its dimension is \( 2^2 + 1^2 = 5 \).

(c) A matrix commuting with all of these must commute in particular with \( \diag(1,1,0) \) and \( \diag(0,0,1) \), hence be of the same block shape, and its \( 2 \times 2 \) block must commute with all of \( M_2(\nR) \), hence be scalar (@prp-center-of-matrix-algebra). So \( A'' = \{\alpha\P_1 + \beta\P_2\} = A \), of dimension \( 2 \). Since \( \A \) is diagonalizable, \( A \) acts semisimply, and @thm-double-commutant predicts exactly \( A'' = A \).
:::

::: {#exr-double-commutant-b3}
[B3: One theorem, once]

Let \( F \) be algebraically closed, let \( V \) be finite-dimensional over \( F \) with \( \dim V \ge 2 \), and let \( A \subseteq \End(V) \) be a **commutative** subalgebra containing \( \id_V \). Prove that \( A \) does not act irreducibly on \( V \).
:::

::: {.solution}
Suppose it did. By @thm-burnside, \( A = \End(V) \). But \( \End(V) \) is not commutative when \( \dim V \ge 2 \): choosing a basis and the operators with matrices \( \E_{12} \) and \( \E_{21} \) gives \( \E_{12}\E_{21} = \E_{11} \ne \E_{22} = \E_{21}\E_{12} \). This contradicts commutativity of \( A \), so \( A \) is not irreducible.
:::

### C. Going deeper

::: {#exr-double-commutant-c1}
[C1: The rank-one step needs its hypothesis]

In Step 2 of the proof of @thm-burnside, the operator \( ab \) was restricted to \( W = \im a \) and an eigenvalue was extracted.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( ab(W) \subseteq W \), and give an example of \( a, b \in M_2(F) \) with \( ba(\im a) \not\subseteq \im a \), so that the order of the product matters.
2. Take \( F = \nR \), \( A = \{x\I_2 + y\Q\} \) with \( \Q = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \). Compute the minimal rank \( r \) of a non-zero member of \( A \) and confirm that the conclusion \( r = 1 \) fails.
3. Which sentence of Step 2 fails for this \( A \)? Say exactly where the hypothesis on \( F \) was used.
:::
:::

::: {.solution}
(a) \( ab(W) = a(b(W)) \subseteq \im a = W \), since \( a \) is applied last. For the other order take \( a = \E_{11} \) and \( b = \E_{21} \) in \( M_2(F) \). Then \( \im a = \Span(\e_1) \) and \( ba\,\e_1 = \E_{21}\e_1 = \e_2 \notin \Span(\e_1) \).

(b) A non-zero \( x\I_2 + y\Q \) has determinant \( x^2 + y^2 > 0 \) for real \( x, y \) not both zero, so it is invertible and has rank \( 2 \). Hence \( r = 2 \), and the conclusion \( r = 1 \) fails; consistently, \( A \) contains no rank-one matrix and is not all of \( M_2(\nR) \).

(c) The sentence "its characteristic polynomial has a root \( \lambda \in F \) because \( F \) is algebraically closed". With \( a = \I_2 \) and \( b = \Q \) we get \( W = \nR^2 \) and \( s = \Q \), whose characteristic polynomial \( x^2 + 1 \) has no real root. Everything before that sentence is valid over any field.
:::

::: {#exr-double-commutant-c2}
[C2: Commutants under a change of basis]

Let \( V \) be finite-dimensional over \( F \), let \( A \subseteq \End(V) \) be a subalgebra containing \( \id_V \), and let \( g \in \End(V) \) be invertible. Put \( gAg^{-1} = \{gag^{-1} : a \in A\} \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( gAg^{-1} \) is a subalgebra containing \( \id_V \) and that \( (gAg^{-1})' = gA'g^{-1} \).
2. Deduce that if \( A'' = A \) then \( (gAg^{-1})'' = gAg^{-1} \).
3. Hence show that the conclusion of @thm-double-commutant is a property of the algebra up to similarity, and use this to give, for each \( n \ge 2 \), a subalgebra of \( M_n(F) \) with \( A'' \ne A \).
:::
:::

::: {.solution}
(a) The map \( a \mapsto gag^{-1} \) is linear, sends \( \id_V \) to \( \id_V \), and satisfies \( (ga_1g^{-1})(ga_2g^{-1}) = g(a_1a_2)g^{-1} \), so the image is a subalgebra containing the identity. For the commutant: \( t \) commutes with every \( gag^{-1} \) if and only if \( g^{-1}tg \) commutes with every \( a \), that is, if and only if \( g^{-1}tg \in A' \), that is, \( t \in gA'g^{-1} \).

(b) Apply (a) twice: \( (gAg^{-1})'' = (gA'g^{-1})' = gA''g^{-1} = gAg^{-1} \).

(c) By (b), whether \( A'' = A \) holds is unchanged by replacing \( A \) with a similar copy, so it is a property of the similarity class. For a failure in \( M_n(F) \) take \( A_n \) = all upper triangular matrices. The same computation as in the warning after @thm-double-commutant, done with the matrix units \( \E_{ii} \) and \( \E_{i,i+1} \), gives \( A_n' = \{\lambda\I_n\} \), hence \( A_n'' = M_n(F) \ne A_n \); and by (b) every similar copy \( g A_n g^{-1} \) fails too.
:::

::: {#exr-double-commutant-c3}
[C3: Is this look-alike a theorem?]

Let \( V \) be finite-dimensional over an algebraically closed \( F \) and let \( A \subseteq \End(V) \) be a subalgebra with \( \id_V \in A \).

::: {.enumerate options="label=(\alph*)"}
1. Prove: if \( V \) is irreducible as an \( A \)-space then \( A' = \{\lambda\,\id_V\} \).
2. Is the converse true? That is, does \( A' = \{\lambda\,\id_V\} \) force \( V \) to be irreducible? Justify your answer.
:::

*Hint for (b): consider the upper triangular matrices in \( M_2(F) \).*
:::

::: {.solution}
(a) By @thm-burnside, \( A = \End(V) \), so \( A' = \End(V)' = \{\lambda\,\id_V\} \) by @prp-center-of-matrix-algebra. (This recovers the second half of Schur's lemma, @thm-schurs-lemma, in this special case.)

(b) No. Let \( A \) be the upper triangular matrices in \( M_2(F) \). The warning after @thm-double-commutant computes \( A' = \{\lambda\I_2\} \), yet \( \Span(\e_1) \) is a proper non-zero invariant subspace, so \( F^2 \) is not irreducible as an \( A \)-space — and indeed \( A \ne M_2(F) \). A trivial commutant is therefore strictly weaker than irreducibility; it is semisimplicity, not a small commutant, that makes the commutant remember the algebra.
:::
