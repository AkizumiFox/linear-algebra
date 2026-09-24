# Schur's Lemma

Section 3 cut a space into irreducible pieces. The next question is the one that always follows a decomposition: what are the maps between the pieces? The answer is startling in its poverty — there are almost none, and the ones that exist are invertible — and that poverty is exactly what makes the rest of the chapter work. A one-line lemma will replace an unknown operator by a scalar, over and over.

The lemma has two parts, and they do **not** have the same hypotheses. The first holds over every field. The second holds only when the field is algebraically closed, and the section ends by exhibiting the failure over \( \nR \) in full. Along the way we get the explanation of why commuting operators share eigenvectors, a fact Chapter 8 proved without explaining.

Recall that a field \( F \) is **algebraically closed** if every non-constant polynomial in \( F[x] \) has a root in \( F \). The Fundamental Theorem of Algebra (@thm-fundamental-theorem-of-algebra) says \( \nC \) is one; \( \nR \) and \( \nQ \) are not, as \( x^2 + 1 \) and \( x^2 - 2 \) show. Unless a statement says otherwise, \( F \) is an arbitrary field, \( A \) is an \( F \)-algebra, and \( A \)-spaces are finite-dimensional, as in @def-representation-of-an-algebra.

## Maps that respect the action

We have objects: \( A \)-spaces. We have subobjects: invariant subspaces. What is missing is the maps, and the requirement almost writes itself. Chapter 8 §09 got everything it had out of a single hypothesis, \( ST = TS \); read \( S \) as a map and \( T \) as the action, and that hypothesis is the one below.

*An \( A \)-map is a linear map for which acting and then mapping is the same as mapping and then acting.*

::: {#def-intertwining-map}
[\( A \)-Map, and Isomorphism of \( A \)-spaces]

Let \( A \) be an \( F \)-algebra and let \( V \) and \( W \) be \( A \)-spaces. A linear map \( \varphi \colon V \to W \) is an **\( A \)-map** if
\[
\varphi(a\v) = a\,\varphi(\v) \qquad \text{for every } a \in A \text{ and every } \v \in V .
\]
We write \( \End_A(V) \) for the set of \( A \)-maps from \( V \) to itself. A **bijective** \( A \)-map is an **isomorphism of \( A \)-spaces**, and \( V \) and \( W \) are **isomorphic** if one exists.
:::

In words: the two actions, on the source and on the target, are tied together by \( \varphi \). Note that the letter \( a \) on the left acts on \( V \) and the one on the right acts on \( W \); the condition is a statement about two different operators. The subscript in \( \End_A(V) \) is part of the symbol and is never dropped: the book writes \( \cL(V) \) for **all** linear maps \( V \to V \), and \( \End_A(V) \subseteq \cL(V) \) is the subset of those that respect the action.

Three routine facts, each one line. **\( \End_A(V) \) is a subalgebra of \( \cL(V) \) containing \( \id_V \):** the defining condition is linear in \( \varphi \), the identity satisfies it, and if \( \varphi, \psi \) satisfy it then \( (\varphi\psi)(a\v) = \varphi(a\psi(\v)) = a(\varphi\psi)(\v) \). **The inverse of a bijective \( A \)-map is an \( A \)-map:** given \( \w \in W \) write \( \w = \varphi(\v) \); then \( \varphi^{-1}(a\w) = \varphi^{-1}(\varphi(a\v)) = a\v = a\varphi^{-1}(\w) \). **A composite of \( A \)-maps is an \( A \)-map**, by the same computation as the first.

**Examples.**

- **Scalars.** \( \lambda\,\id_V \in \End_A(V) \) for every \( \lambda \in F \), since the action is linear. These are the \( A \)-maps we get for free, and Schur's lemma will say that over an algebraically closed field they are all of them.
- **The commutant, again.** If \( A \subseteq \cL(V) \) is a subalgebra containing \( \id_V \), acting tautologically, then \( \varphi \) is an \( A \)-map exactly when \( \varphi T = T\varphi \) for every \( T \in A \). So \( \End_A(V) = A' \), the commutant of Section 1 (@def-commutant, @prp-commutant-is-algebra). The two notions are the same notion.
- **A projection onto a summand.** If \( V = U \oplus W \) with both summands \( A \)-invariant, the projection of \( V \) onto \( U \) along \( W \) is an \( A \)-map: write \( \v = \u + \w \), and \( a\v = a\u + a\w \) is the corresponding splitting of \( a\v \), so the projection of \( a\v \) is \( a\u \).

**Non-example by minimal change.** Take \( A = F[\N] \subseteq \cL(F^2) \) with \( \N = \J_2(0) \), and \( \varphi = \E_{21} \). Then \( \varphi(\N\e_2) = \varphi(\e_1) = \e_2 \) while \( \N\varphi(\e_2) = \N\0 = \0 \). Linear, but not an \( A \)-map: the clause that fails is the displayed one, at \( a = \N \) and \( \v = \e_2 \).

## The lemma

Everything now follows from one observation: an \( A \)-map has an \( A \)-invariant kernel and an \( A \)-invariant image, and an irreducible \( A \)-space (@def-simple-module) has almost none of either.

:::: {#thm-schurs-lemma}
[Schur's Lemma]

Let \( A \) be an \( F \)-algebra.

::: {.enumerate options="label=(\alph*)"}
1. Let \( V \) and \( W \) be **irreducible** \( A \)-spaces and let \( \varphi \colon V \to W \) be an \( A \)-map. Then either \( \varphi = 0 \) or \( \varphi \) is an isomorphism of \( A \)-spaces. **No hypothesis on \( F \) is needed.**
2. Suppose in addition that \( F \) is **algebraically closed**, and let \( V \) be an irreducible \( A \)-space. Then every \( A \)-map \( \varphi \colon V \to V \) is a scalar: \( \varphi = \lambda\,\id_V \) for some \( \lambda \in F \). Equivalently, \( \End_A(V) = \{\lambda\,\id_V : \lambda \in F\} \).
:::
::::

::: {.idea}
For (a): the kernel and the image are invariant, so each is one of the two extremes, and a single word — "\( \varphi \ne 0 \)" — rules out the wrong extreme on both sides. For (b): we want to compare \( \varphi \) with a scalar, so we need a scalar to compare it with, and the only source of one is an eigenvalue. That is the whole role of algebraic closure. Once \( \lambda \) is in hand, \( \varphi - \lambda\,\id_V \) is an \( A \)-map that is **not** injective, and part (a) says a non-zero one would have to be.
:::

::: {.proof}
(a) The kernel is \( A \)-invariant: if \( \varphi(\v) = \0 \) then \( \varphi(a\v) = a\varphi(\v) = \0 \). The image is \( A \)-invariant: \( a\varphi(\v) = \varphi(a\v) \in \operatorname{im}\varphi \).

Suppose \( \varphi \ne 0 \). Then \( \ker\varphi \ne V \), and since \( V \) is irreducible its only other invariant subspace is \( \{\0\} \), so \( \ker\varphi = \{\0\} \) and \( \varphi \) is injective (@thm-injective-iff-trivial-kernel). Also \( \operatorname{im}\varphi \ne \{\0\} \), and since \( W \) is irreducible, \( \operatorname{im}\varphi = W \), so \( \varphi \) is surjective. Hence \( \varphi \) is bijective, and its inverse is an \( A \)-map by the remark above; so \( \varphi \) is an isomorphism of \( A \)-spaces.

(b) Since \( V \) is irreducible, \( V \ne \{\0\} \), so \( n = \dim V \ge 1 \) and the characteristic polynomial \( p_{\varphi} \) is monic of degree \( n \), hence non-constant. As \( F \) is algebraically closed, \( p_{\varphi} \) has a root \( \lambda \in F \), and \( \lambda \) is then an eigenvalue of \( \varphi \) (@thm-eigenvalue-characterizations).

Put \( \psi = \varphi - \lambda\,\id_V \). It is an \( A \)-map, because \( \End_A(V) \) is a subspace containing \( \id_V \). Its kernel is \( E_{\lambda}(\varphi) \ne \{\0\} \), so \( \psi \) is not injective and therefore not an isomorphism. By (a), applied with \( W = V \), the only remaining possibility is \( \psi = 0 \), that is, \( \varphi = \lambda\,\id_V \). Conversely every scalar multiple of \( \id_V \) is an \( A \)-map, so \( \End_A(V) \) consists exactly of these. This proves the lemma.
:::

Part (a) says something worth naming even when the field is small: for an irreducible \( V \), every non-zero element of \( \End_A(V) \) is invertible. An algebra with that property is called a **division algebra**, and part (a) is the statement that the commutant of an irreducible action is one. Part (b) says that over an algebraically closed field the only division algebra that can occur is \( F \) itself. That is a genuine restriction on the field, not a formality.

::: {.warning}
**Only the second part needs algebraic closure.** Part (a) was proved over an arbitrary field and will be used over arbitrary fields. Part (b) used exactly one thing that (a) did not: the existence of an eigenvalue of \( \varphi \). Quoting "Schur's lemma says the commutant is the scalars" without the hypothesis is the standard error, and the next example is the standard witness.
:::

## What goes wrong over the reals

::: {#exm-rotation-commutant-is-complex}
[A Real Irreducible Representation with Commutant \( \nC \)]

Let \( n \ge 3 \), put \( \theta = 2\pi/n \), \( c = \cos\theta \), \( s = \sin\theta \), and let
\[
\R = \begin{pmatrix} c & -s \\ s & c \end{pmatrix} \in M_2(\nR) .
\]
Since \( \R^n = \I_2 \), the powers of \( \R \) repeat with period dividing \( n \); Section 7 will read \( k \mapsto \R^k \) as a representation of a cyclic group, and that is what we will then call the **rotation representation**. Let \( A = \nR[\R] \subseteq M_2(\nR) \) be the algebra of polynomials in \( \R \), so that the \( A \)-invariant subspaces of \( \nR^2 \) are exactly the \( \R \)-invariant ones. Show that \( \nR^2 \) is an irreducible \( A \)-space and compute \( \End_A(\nR^2) \).
:::

::: {.solution}
**Irreducible.** A proper non-zero invariant subspace of \( \nR^2 \) would be a line \( \nR\v \) with \( \R\v \in \nR\v \), that is, a real eigenvector of \( \R \). Now
\[
p_{\R}(x) = x^2 - 2cx + 1 ,
\]
whose discriminant is \( 4c^2 - 4 = -4s^2 \). For \( n \ge 3 \) we have \( 0 < \theta \le 2\pi/3 < \pi \), so \( s = \sin\theta > 0 \) and the discriminant is negative: \( p_{\R} \) has no real root, hence \( \R \) has no real eigenvalue (@thm-eigenvalue-characterizations), hence no invariant line. So the only invariant subspaces are \( \{\0\} \) and \( \nR^2 \), and \( \nR^2 \ne \{\0\} \).

**The commutant.** Since \( A \) acts tautologically, \( \End_A(\nR^2) \) is the commutant \( A' \) (@def-commutant): the set of \( \X \in M_2(\nR) \) commuting with every element of \( A \); since \( A \) consists of polynomials in \( \R \), this is the set of \( \X \) with \( \X\R = \R\X \). Write \( \X = \begin{psmallmatrix} p & q \\ r & t\end{psmallmatrix} \). Multiplying out,
\[
\begin{aligned}
\X\R &= \begin{pmatrix} pc + qs & -ps + qc \\ rc + ts & -rs + tc \end{pmatrix}, \\
\R\X &= \begin{pmatrix} cp - sr & cq - st \\ sp + cr & sq + ct \end{pmatrix},
\end{aligned}
\]
so that
\[
\X\R - \R\X = s\begin{pmatrix} q + r & t - p \\ t - p & -(q+r) \end{pmatrix} .
\]
Since \( s \ne 0 \), the equation \( \X\R = \R\X \) says exactly \( r = -q \) and \( t = p \). Writing \( \Q = \begin{psmallmatrix} 0 & -1 \\ 1 & 0\end{psmallmatrix} \) for the quarter turn, we get
\[
\End_A(\nR^2) = \{\, p\I_2 + r\Q : p, r \in \nR \,\} ,
\]
a two-dimensional real algebra. It is a copy of \( \nC \): the map \( p + ri \mapsto p\I_2 + r\Q \) is linear and bijective (it carries the basis \( 1, i \) to the independent \( \I_2, \Q \)), it sends \( 1 \) to \( \I_2 \), and since \( \Q^2 = -\I_2 \),
\[
(p\I_2 + r\Q)(p'\I_2 + r'\Q) = (pp' - rr')\I_2 + (pr' + rp')\Q ,
\]
which matches \( (p + ri)(p' + r'i) = (pp' - rr') + (pr' + rp')i \). So it is an isomorphism of \( \nR \)-algebras.

**What this shows.** Part (b) of @thm-schurs-lemma fails over \( \nR \): here \( \End_A(\nR^2) \) has dimension \( 2 \), not \( 1 \). Part (a) does not fail, and we can see it directly: \( \det(p\I_2 + r\Q) = p^2 + r^2 \), which is non-zero unless \( p = r = 0 \), so every non-zero element of the commutant is invertible, exactly as (a) predicts. The commutant is a division algebra; it is just not \( \nR \).
:::

::: {.remark}
The same computation with \( n = 4 \) gives \( \R = \Q \), and the commutant \( \nR[\Q] \) is then the algebra generated by \( \R \) itself. Over \( \nC \) the picture collapses: \( \R \) has eigenvalues \( e^{\pm i\theta} \) there, so the two eigenlines are invariant and \( \nC^2 \) is **not** an irreducible \( \nC[\R] \)-space. Irreducibility, like semisimplicity, is a statement about a space **and** a field.
:::

## Families of operators

The corollaries below are about a family of operators — a set of matrices, the image of a group — rather than about an algebra given in advance. The translation costs one lemma, and Section 1's generated subalgebra is what it produces.

:::: {#lem-family-and-generated-algebra}
[A Family and the Algebra It Generates]

Let \( V \) be a finite-dimensional vector space over \( F \) and let \( \cF \subseteq \cL(V) \) be any set of operators. Write \( A(\cF) \coloneqq F\langle\cF\rangle \) for the subalgebra of \( \cL(V) \) generated by \( \cF \) (@def-generated-subalgebra). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( A(\cF) \) contains \( \cF \) and \( \id_V \), and is the span of \( \id_V \) together with all products \( S_1S_2\cdots S_m \) with \( m \ge 1 \) and \( S_1, \dots, S_m \in \cF \);
2. a subspace \( U \subseteq V \) is invariant under every member of \( \cF \) if and only if it is \( A(\cF) \)-invariant;
3. an operator \( S \in \cL(V) \) commutes with every member of \( \cF \) if and only if it commutes with every element of \( A(\cF) \);
4. if the members of \( \cF \) commute with one another, then \( A(\cF) \) is commutative.
:::
::::

::: {.proof}
(a) A generated subalgebra contains its generators, and every subalgebra contains the identity (@def-subalgebra), which in \( \cL(V) \) is \( \id_V \). The span description is @prp-generated-is-span-of-words applied to the set \( \cF \) inside the algebra \( \cL(V) \).

(b) \( (\Leftarrow) \) holds because \( \cF \subseteq A(\cF) \). \( (\Rightarrow) \) If \( SU \subseteq U \) for every \( S \in \cF \), then applying the members one at a time gives \( S_1\cdots S_mU \subseteq U \) for every word, and \( \id_VU \subseteq U \); a subspace is closed under linear combinations, so \( A(\cF)U \subseteq U \).

(c) \( (\Leftarrow) \) again holds because \( \cF \subseteq A(\cF) \). \( (\Rightarrow) \) If \( S \) commutes with each \( S_i \) then it commutes with \( S_1\cdots S_m \), by moving \( S \) across one factor at a time; it commutes with \( \id_V \); and the set of operators commuting with \( S \) is a subspace, so it contains the span.

(d) Let \( S \in \cF \). By hypothesis \( S \) commutes with every member of \( \cF \), so by (c) it commutes with every element of \( A(\cF) \). Now fix \( a \in A(\cF) \). What we have just shown says that every member of \( \cF \) commutes with \( a \); applying (c) to \( a \) in place of \( S \), the element \( a \) commutes with every element of \( A(\cF) \). As \( a \) was arbitrary, \( A(\cF) \) is commutative.
:::

Say that a family \( \cF \subseteq \cL(V) \) **acts irreducibly** if \( V \ne \{\0\} \) and the only subspaces invariant under every member of \( \cF \) are \( \{\0\} \) and \( V \). By (a) and (b), this says exactly that \( V \) is an irreducible \( A(\cF) \)-space.

::: {#cor-commuting-with-irreducible}
[An Operator Commuting with an Irreducible Family Is a Scalar]

Let \( F \) be **algebraically closed**, let \( V \) be a finite-dimensional vector space over \( F \), and let \( \cF \subseteq \cL(V) \) act irreducibly. If \( S \in \cL(V) \) commutes with every member of \( \cF \), then \( S = \lambda\,\id_V \) for some \( \lambda \in F \).
:::

::: {.proof}
Put \( A = A(\cF) \), a subalgebra of \( \cL(V) \) containing \( \id_V \) by @lem-family-and-generated-algebra (a), so \( V \) is an \( A \)-space under the tautological representation, and by (b) it is irreducible. By (c), \( S \) commutes with every element of \( A \), that is, \( S \in \End_A(V) \). Since \( F \) is algebraically closed, @thm-schurs-lemma (b) gives \( S = \lambda\,\id_V \).
:::

::: {#cor-abelian-irreducibles-are-lines}
[Over an Algebraically Closed Field, Commutative Means One-Dimensional]

Let \( F \) be **algebraically closed**, let \( A \) be a **commutative** \( F \)-algebra, and let \( V \) be an irreducible \( A \)-space. Then \( \dim V = 1 \).
:::

::: {.idea}
Commutativity makes every operator of the action an \( A \)-map, so Schur turns all of them into scalars at once. But an algebra of scalars leaves every subspace invariant, and only a line can survive that.
:::

::: {.proof}
Let \( a \in A \). For every \( b \in A \) we have \( \rho(a)\rho(b) = \rho(ab) = \rho(ba) = \rho(b)\rho(a) \), so \( \rho(a) \) is an \( A \)-map from \( V \) to itself. By @thm-schurs-lemma (b) there is \( \lambda(a) \in F \) with \( \rho(a) = \lambda(a)\,\id_V \).

Hence \( a\v = \lambda(a)\v \) for every \( a \in A \) and \( \v \in V \), so **every** subspace of \( V \) is \( A \)-invariant. Since \( V \) is irreducible, \( V \ne \{\0\} \); pick \( \v \ne \0 \). Then \( F\v \) is a non-zero \( A \)-invariant subspace, so \( F\v = V \) and \( \dim V = 1 \).
:::

Both hypotheses are doing work. Commutativity is needed: \( \nC^2 \) is an irreducible \( M_2(\nC) \)-space of dimension \( 2 \). Algebraic closure is needed: in @exm-rotation-commutant-is-complex the algebra \( A = \nR[\R] \) is commutative, being generated by one operator, and \( \nR^2 \) is an irreducible \( A \)-space of dimension \( 2 \).

::: {.check}
The algebra \( A = \nR[\R] \) of @exm-rotation-commutant-is-complex is commutative and \( \nR^2 \) is an irreducible \( A \)-space of dimension \( 2 \). Which hypothesis of @cor-abelian-irreducibles-are-lines fails, and where exactly does the proof break?
:::

::: {.solution}
Algebraic closure fails: \( \nR \) is not algebraically closed. The proof breaks at its first move, the appeal to @thm-schurs-lemma (b): the operator \( \rho(\R) = \R \) is indeed an \( A \)-map, but it is not a scalar, because its characteristic polynomial \( x^2 - 2cx + 1 \) has no root in \( \nR \) and so \( \R \) has no eigenvalue to be a scalar multiple of. Everything before that point — commutativity, irreducibility, the fact that each \( \rho(a) \) is an \( A \)-map — is still true.
:::

Section 9 will use @cor-abelian-irreducibles-are-lines in exactly the form stated: over \( \nC \), every irreducible representation of a commutative algebra, and hence of an abelian group, is one-dimensional, so its "matrix" is a single complex number.

## Looking back at commuting operators

Chapter 8 §09 proved that a commuting family of operators, each with a splitting characteristic polynomial, has a common eigenvector (@thm-commuting-common-eigenvector), and built simultaneous diagonalization on it. At the time the proof looked like a clever trick: take a minimal invariant subspace and show every operator is a scalar on it. We can now say what the trick was.

::: {#cor-schur-common-eigenvector}
[Commuting Operators Have a Common Eigenvector]

Let \( F \) be **algebraically closed**, let \( V \ne \{\0\} \) be finite-dimensional over \( F \), and let \( \cF \subseteq \cL(V) \) be a family whose members commute with one another. Then there is \( \v \ne \0 \) that is an eigenvector of every \( T \in \cF \).
:::

::: {.proof}
Among the non-zero subspaces of \( V \) invariant under every member of \( \cF \) — there is one, namely \( V \) — choose \( W \) of smallest dimension. Put \( A = A(\cF) \), which is a commutative subalgebra of \( \cL(V) \) containing \( \id_V \) by @lem-family-and-generated-algebra (a), (d), and note that \( W \) is \( A \)-invariant by part (b) of the same lemma. So \( a \mapsto a|_W \) is a representation of \( A \) on \( W \).

\( W \) is an irreducible \( A \)-space: it is non-zero, and a non-zero \( A \)-invariant subspace \( U \subseteq W \) is, by @lem-family-and-generated-algebra (b), invariant under every member of \( \cF \), hence has \( \dim U \ge \dim W \) by the choice of \( W \), hence equals \( W \) (@thm-dim-impl-eq).

By @cor-abelian-irreducibles-are-lines, \( \dim W = 1 \). Write \( W = F\v \) with \( \v \ne \0 \). For every \( T \in \cF \) we have \( T\v \in W = F\v \), so \( \v \) is an eigenvector of \( T \). This proves the corollary.
:::

That is Chapter 8's argument, with its steps given their names: "minimal non-zero invariant subspace" is "irreducible", and "every operator is a scalar on it" is Schur's lemma. The version proved there is the stronger one — it asks only that each \( p_T \) split over \( F \), not that \( F \) be algebraically closed — and getting that extra generality is exactly what its @lem-invariant-charpoly-splits was for. What this section adds is not strength but explanation: the scalars appeared because a commutative algebra acting irreducibly over an algebraically closed field has nowhere to act except on a line.

The other half of Chapter 8 §09, simultaneous diagonalization, needs one more ingredient: that the whole space splits into such lines, not just that one of them exists. Section 3's language names that ingredient — the algebra must act semisimply — and in the presence of an inner product it comes for free.

:::: {#prp-adjoint-closed-acts-semisimply .optional}
[Closed Under Adjoints Implies Semisimple]

Let \( V \) be a finite-dimensional inner product space over \( F = \nR \) or \( F = \nC \), and let \( A \subseteq \cL(V) \) be a subalgebra containing \( \id_V \) and closed under adjoints: \( T \in A \) implies \( T^{*} \in A \) (@def-adjoint). Then:

::: {.enumerate options="label=(\alph*)"}
1. for every \( A \)-invariant subspace \( U \), the orthogonal complement \( U^{\perp} \) is \( A \)-invariant, and \( V = U \oplus U^{\perp} \); in particular \( A \) acts semisimply on \( V \);
2. \( V \) is a direct sum of **pairwise orthogonal** irreducible \( A \)-invariant subspaces.
:::
::::

::: {.proof}
(a) Let \( U \) be \( A \)-invariant, let \( T \in A \) and \( \w \in U^{\perp} \). For every \( \u \in U \),
\[
\inner{T\w}{\u} = \inner{\w}{T^{*}\u} = 0 ,
\]
because \( T^{*} \in A \) gives \( T^{*}\u \in U \), while \( \w \in U^{\perp} \). So \( T\w \in U^{\perp} \), and \( U^{\perp} \) is \( A \)-invariant. The splitting \( V = U \oplus U^{\perp} \) is @thm-orthogonal-decomposition (a). Hence every \( A \)-invariant subspace has an \( A \)-invariant complement (@def-semisimple-algebra).

(b) Induction on \( \dim V \). If \( V = \{\0\} \) it is the empty direct sum. Otherwise choose, among the non-zero \( A \)-invariant subspaces, one of smallest dimension, \( W \); as in the proof of @thm-semisimple-iff-sum-of-simples it is irreducible. By (a), \( V = W \oplus W^{\perp} \) with \( W^{\perp} \) invariant and \( \dim W^{\perp} < \dim V \).

The restricted algebra \( A|_{W^{\perp}} = \{T|_{W^{\perp}} : T \in A\} \subseteq \cL(W^{\perp}) \) satisfies the same hypotheses on the inner product space \( W^{\perp} \): it is a subalgebra containing \( \id_{W^{\perp}} \), and for \( \w, \w' \in W^{\perp} \),
\[
\inner{T|_{W^{\perp}}\w}{\w'} = \inner{T\w}{\w'} = \inner{\w}{T^{*}\w'} = \inner{\w}{T^{*}|_{W^{\perp}}\w'} ,
\]
so \( (T|_{W^{\perp}})^{*} = T^{*}|_{W^{\perp}} \in A|_{W^{\perp}} \) by uniqueness of the adjoint (@thm-adjoint-exists). By the inductive hypothesis \( W^{\perp} = W_1 \oplus \dots \oplus W_r \) with the \( W_i \) pairwise orthogonal and irreducible, and each \( W_i \subseteq W^{\perp} \) is orthogonal to \( W \). Hence \( V = W \oplus W_1 \oplus \dots \oplus W_r \) as required.
:::

Now take a commuting family \( \cF \) of **self-adjoint** operators on a finite-dimensional complex inner product space \( V \ne \{\0\} \), and put \( A = A(\cF) \). It is commutative by @lem-family-and-generated-algebra (d). It is closed under adjoints, because \( (S_1\cdots S_m)^{*} = S_m^{*}\cdots S_1^{*} = S_m\cdots S_1 = S_1\cdots S_m \), the last step by commutativity, and because \( \varphi \mapsto \varphi^{*} \) is conjugate-linear, so the span of a set of self-adjoint operators is closed under it. By @prp-adjoint-closed-acts-semisimply, \( V \) is an orthogonal direct sum of irreducible \( A \)-subspaces; by @cor-abelian-irreducibles-are-lines those subspaces are lines; and a line invariant under every member of \( \cF \) is spanned by a common eigenvector. Normalizing gives an orthonormal basis of common eigenvectors — Chapter 11 §07's conclusion (@thm-simultaneous-unitary-diagonalization) for a commuting self-adjoint family, obtained here by putting two general facts together rather than by an induction tailored to the situation. Chapter 11 proves more, for commuting **normal** families, and pays for it with a longer argument.

::: {.warning}
**The converse of @cor-commuting-with-irreducible is false.** A family whose commutant is only the scalars need not act irreducibly, and the witness is short. Take \( F = \nC \) and let \( \cF \) be the algebra of upper triangular matrices in \( M_2(\nC) \), acting on \( \nC^2 \). A matrix commuting with \( \E_{11} \) must be diagonal, and one commuting with \( \E_{12} \) as well must have equal diagonal entries, so the commutant is \( \{p\I_2 : p \in \nC\} \), the scalars; exercise C2 does the two computations. Yet \( \nC\e_1 \) is invariant under every upper triangular matrix, so \( \cF \) does not act irreducibly. Thus "the commutant is the scalars" is a consequence of irreducibility, never a test for it. The genuine converse statement, that an irreducible subalgebra is **all** of \( \cL(V) \), is Burnside's theorem in Section 5, and it needs more than the commutant.
:::

## Exercises

### A. Check your understanding

:::: {#exr-schurs-lemma-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State both parts of Schur's lemma and say precisely which one needs \( F \) to be algebraically closed, and what that hypothesis is used for.
2. True or false: if \( V \) and \( W \) are irreducible \( A \)-spaces with \( \dim V \ne \dim W \), then the only \( A \)-map \( V \to W \) is \( 0 \). Justify your answer.
3. Explain why, for an irreducible \( A \)-space \( V \), no element of \( \End_A(V) \) can be non-zero and non-invertible.
4. Give \( \End_A(\nR^2) \) for the rotation representation of @exm-rotation-commutant-is-complex, and say which part of Schur's lemma it illustrates and which it refutes.
:::
::::

::: {.solution}
(a) Part (a): an \( A \)-map between irreducible \( A \)-spaces is \( 0 \) or an isomorphism; no hypothesis on \( F \). Part (b): over an algebraically closed \( F \), every \( A \)-map from an irreducible \( V \) to itself is a scalar. Algebraic closure is used once, to produce a root of the characteristic polynomial of \( \varphi \), that is, an eigenvalue.

(b) True. A non-zero \( A \)-map would be an isomorphism by @thm-schurs-lemma (a), and an isomorphism of vector spaces preserves dimension (@thm-isomorphic-iff-same-dimension), contradicting \( \dim V \ne \dim W \).

(c) By @thm-schurs-lemma (a) with \( W = V \): a non-zero \( A \)-map \( V \to V \) is an isomorphism, hence invertible.

(d) \( \End_A(\nR^2) = \{p\I_2 + r\Q\} \cong \nC \). It illustrates part (a) — every non-zero element has determinant \( p^2 + r^2 \ne 0 \), so the commutant is a division algebra — and refutes part (b) read without its hypothesis, since the commutant is two-dimensional over \( \nR \).
:::

### B. Practice

:::: {#exr-schurs-lemma-b1}
[B1: An irreducibility test]

Let \( \D = \diag(i, -i) \in M_2(\nC) \), which satisfies \( \D^4 = \I_2 \), and let \( A = \nC[\D] \) be the algebra of polynomials in \( \D \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \End_A(\nC^2) \).
2. Deduce from @thm-schurs-lemma (b) that \( \nC^2 \) is not an irreducible \( A \)-space, and confirm this by exhibiting a proper non-zero invariant subspace.
:::
::::

::: {.solution}
(a) An operator is an \( A \)-map exactly when it commutes with \( \D \), since the elements of \( A \) are the polynomials in \( \D \). Writing \( \X = \begin{psmallmatrix} p & q \\ r & t\end{psmallmatrix} \),
\[
\X\D - \D\X = \begin{pmatrix} 0 & -2iq \\ 2ir & 0 \end{pmatrix},
\]
which vanishes exactly when \( q = r = 0 \). So \( \End_A(\nC^2) \) is the algebra of diagonal matrices, of dimension \( 2 \).

(b) If \( \nC^2 \) were irreducible then, \( \nC \) being algebraically closed, @thm-schurs-lemma (b) would force \( \End_A(\nC^2) \) to have dimension \( 1 \). It has dimension \( 2 \), so \( \nC^2 \) is not irreducible. Indeed \( \nC\e_1 \) is invariant, since \( \D\e_1 = i\e_1 \).
:::

:::: {#exr-schurs-lemma-b2}
[B2: The quarter turn, over two fields]

Let \( \Q = \begin{psmallmatrix} 0 & -1 \\ 1 & 0 \end{psmallmatrix} \), the rotation by a quarter turn, and let \( A_F = F[\Q] \) for \( F = \nR \) and for \( F = \nC \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \nR^2 \) is an irreducible \( A_{\nR} \)-space and that \( \End_{A_{\nR}}(\nR^2) \cong \nC \).
2. Show that \( \nC^2 \) is **not** an irreducible \( A_{\nC} \)-space, and find two invariant lines.
3. Explain why (a) and (b) together are consistent with Schur's lemma.
:::
::::

::: {.solution}
(a) This is @exm-rotation-commutant-is-complex with \( n = 4 \), so \( \theta = \pi/2 \), \( c = 0 \), \( s = 1 \): the characteristic polynomial \( x^2 + 1 \) has no real root, so there is no invariant line and \( \nR^2 \) is irreducible; and the commutant is \( \{p\I_2 + r\Q\} \cong \nC \).

(b) Over \( \nC \) the polynomial \( x^2 + 1 \) has the roots \( \pm i \), so \( \Q \) has eigenvalues \( i \) and \( -i \), with eigenvectors \( (1, -i) \) and \( (1, i) \) respectively: from \( \Q(1, -i) = (i, 1) = i(1, -i) \) and \( \Q(1, i) = (-i, 1) = -i(1, i) \). Each of \( \nC(1, i) \) and \( \nC(1, -i) \) is a proper non-zero invariant line.

(c) Part (b) of Schur's lemma applies only over an algebraically closed field. Over \( \nC \) it does apply, and it is not contradicted: the space is reducible there, so the lemma says nothing about it. Over \( \nR \) the space is irreducible but the field is not algebraically closed, so only part (a) applies — and part (a) holds, since every non-zero element of \( \{p\I_2 + r\Q\} \) is invertible.
:::

:::: {#exr-schurs-lemma-b3}
[B3: A common eigenvector]

Let
\[
\A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}, \qquad
\B = \begin{pmatrix} 3 & 5 \\ 0 & 3 \end{pmatrix} \in M_2(\nC) .
\]

::: {.enumerate options="label=(\alph*)"}
1. Verify that \( \A\B = \B\A \).
2. Find a common eigenvector, and check that it spans the unique minimal non-zero invariant subspace, as in the proof of @cor-schur-common-eigenvector.
:::
::::

::: {.solution}
(a) The diagonal entries of both products are \( 2 \cdot 3 = 6 \), the lower left entry of both is \( 0 \), and the upper right entries are \( (\A\B)_{12} = 2 \cdot 5 + 1 \cdot 3 = 13 \) and \( (\B\A)_{12} = 3 \cdot 1 + 5 \cdot 2 = 13 \). So
\[
\A\B = \B\A = \begin{pmatrix} 6 & 13 \\ 0 & 6 \end{pmatrix}.
\]

(b) \( \A\e_1 = 2\e_1 \) and \( \B\e_1 = 3\e_1 \), so \( \e_1 \) is a common eigenvector and \( \nC\e_1 \) is invariant. It is the only invariant line: if \( \v = (x, y) \) with \( y \ne 0 \) spanned an invariant line, then \( \A\v = (2x + y, 2y) \) would be a multiple \( c\v \), forcing \( c = 2 \) from the second coordinate and then \( y = 0 \) from the first. So \( \nC\e_1 \) is the minimal non-zero invariant subspace the proof of @cor-schur-common-eigenvector produces, and it is a line, as @cor-abelian-irreducibles-are-lines requires.
:::

### C. Going deeper

:::: {#exr-schurs-lemma-c1}
[C1: A commutant that is a field]

Let \( \A = \begin{psmallmatrix} 0 & 2 \\ 1 & 0 \end{psmallmatrix} \in M_2(\nQ) \), the companion matrix of \( x^2 - 2 \), and let \( A = \nQ[\A] \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \nQ^2 \) is an irreducible \( A \)-space.
2. Compute \( \End_A(\nQ^2) \) and prove that it is a field in which \( 2 \) has a square root.
3. Explain why this does not contradict @thm-schurs-lemma.
:::
::::

::: {.solution}
(a) \( p_{\A} = x^2 - 2 \) by @thm-companion-char-min, and \( x^2 - 2 \) has no rational root, since \( \sqrt2 \) is irrational (@thm-sqrt2-irrational). So \( \A \) has no eigenvalue in \( \nQ \) (@thm-eigenvalue-characterizations), hence no invariant line, and the only invariant subspaces of \( \nQ^2 \) are \( \{\0\} \) and \( \nQ^2 \).

(b) An \( A \)-map is an \( \X = \begin{psmallmatrix} p & q \\ r & t\end{psmallmatrix} \) commuting with \( \A \). Computing,
\[
\X\A - \A\X = \begin{pmatrix} q - 2r & 2p - 2t \\ t - p & 2r - q \end{pmatrix},
\]
which vanishes exactly when \( t = p \) and \( q = 2r \). So
\[
\End_A(\nQ^2) = \{\, p\I_2 + r\A : p, r \in \nQ \,\} ,
\]
using \( \A = \begin{psmallmatrix} 0 & 2 \\ 1 & 0\end{psmallmatrix} \). Since \( \A^2 = 2\I_2 \), this is a commutative algebra in which \( \A \) is a square root of \( 2\I_2 \); and every non-zero element is invertible, because \( \det(p\I_2 + r\A) = p^2 - 2r^2 \), which vanishes for rational \( p, r \) only when \( p = r = 0 \): if \( r = 0 \) then \( p^2 = 0 \), and if \( r \ne 0 \) then \( (p/r)^2 = 2 \) with \( p/r \in \nQ \), contradicting @thm-sqrt2-irrational. A commutative algebra in which every non-zero element is invertible is a field.

(c) Part (a) of @thm-schurs-lemma predicts exactly this: the commutant of an irreducible action is a division algebra. Part (b) does not apply, because \( \nQ \) is not algebraically closed.
:::

:::: {#exr-schurs-lemma-c2}
[C2: Scalar commutant without irreducibility]

Let \( F \) be **algebraically closed** — say \( F = \nC \), so that @cor-commuting-with-irreducible really applies — and let \( A \subseteq M_2(F) \) be the algebra of upper triangular matrices.

::: {.enumerate options="label=(\alph*)"}
1. Compute the set of \( \X \in M_2(F) \) commuting with every element of \( A \). (The computation uses nothing about \( F \).)
2. Deduce that the converse of @cor-commuting-with-irreducible fails: a family with commutant the scalars need not act irreducibly.
:::
::::

::: {.solution}
(a) It suffices to commute with the basis \( \E_{11}, \E_{12}, \E_{22} \). Write \( \X = \begin{psmallmatrix} p & q \\ r & t\end{psmallmatrix} \). From
\[
\X\E_{11} - \E_{11}\X = \begin{pmatrix} 0 & -q \\ r & 0 \end{pmatrix}
\]
we get \( q = r = 0 \), and then
\[
\X\E_{12} - \E_{12}\X = \begin{pmatrix} 0 & p - t \\ 0 & 0 \end{pmatrix}
\]
gives \( p = t \). Conversely a scalar matrix commutes with everything. So the commutant is \( \{p\I_2 : p \in F\} \), the scalars.

(b) The family \( \cF = A \) has commutant the scalars by (a), yet it does not act irreducibly on \( F^2 \): the line \( F\e_1 \) is invariant, as computed in @exm-triangular-not-semisimple. So the implication in @cor-commuting-with-irreducible cannot be reversed. (The hypothesis is not vacuous either: over an algebraically closed field the corollary does apply whenever the family is irreducible.)
:::
