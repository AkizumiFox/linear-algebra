# Group Representations

Sections 01–06 studied an algebra of operators in the abstract. A group is not an algebra — its elements cannot be added — but a group can be made to *act* by operators, and then the operators it produces span an algebra. This section sets up that translation: a representation of a group \( G \) over \( F \) is the same thing as a representation of the group algebra \( F[G] \), so everything proved about algebras applies at once. The section's main theorem, Maschke's, says when the resulting algebra is semisimple, and its hypothesis on the field is not decoration: we exhibit a group and a field where the conclusion fails outright.

Throughout, \( G \) is a **finite** group, written multiplicatively, with its identity element written \( 1 \), and \( F \) is a field. All vector spaces are finite-dimensional over \( F \). Where a statement needs \( F \) to be \( \nC \), or needs a condition on \( \operatorname{char} F \), the statement says so.

## Letting a group act by operators

The book's groups so far have been groups *of* matrices or *of* permutations: \( \GL_n(F) \) (@exm-groups), the symmetric group \( S_n \), the classical groups of Chapter 13. Such a group arrives with its linear algebra attached. An abstract group does not. If all we know about \( G \) is its multiplication table, the only way to bring linear algebra to bear is to manufacture operators out of it.

The manufacture has one requirement. Group multiplication must become composition of operators, since composition is the only product on \( \cL(V) \), and every group element must become an **invertible** operator, since every group element can be undone. That is exactly the definition of a homomorphism into the group \( \GL(V) \) of invertible operators on \( V \), a group under composition by the same argument that makes \( \GL_n(F) \) one (@exm-groups).

*A representation is a way of realizing the elements of a group as invertible operators, so that multiplying in the group means composing the operators.*

::: {#def-representation}
[Representation of a group]

Let \( G \) be a group, \( F \) a field and \( V \) a finite-dimensional vector space over \( F \). A **representation** of \( G \) on \( V \) over \( F \) is a group homomorphism
\[
  \rho \colon G \to \GL(V),
\]
that is, a map assigning to each \( g \in G \) an invertible operator \( \rho(g) \) on \( V \) such that \( \rho(gh) = \rho(g)\rho(h) \) **for all** \( g, h \in G \).
The space \( V \) is the **representation space**, and \( \dim V \) is the **degree** of \( \rho \). The representation is **faithful** if \( \rho \) is injective. When \( V = F^n \) we speak of a **matrix representation** and write \( \rho(g) \in \GL_n(F) \).
:::

In words: to give a representation is to attach to each \( g \in G \) an invertible operator \( \rho(g) \) on one fixed space \( V \), in such a way that the operator attached to a product is the composition of the operators attached to the factors. Two conditions that look like extra demands are already implied by @thm-homomorphism-basic-properties: \( \rho(1) = \id_V \), and \( \rho(g^{-1}) = \rho(g)^{-1} \) for every \( g \). So we never have to check them.

Note what is **not** required. Nothing says \( \rho \) is injective, and nothing says the operators \( \rho(g) \) are distinct. The constant map \( g \mapsto \id_V \) is a perfectly good representation; it simply carries no information about \( G \).

**Examples.** Fix a finite group \( G \) and a field \( F \).

- **The trivial representation.** \( V = F \) and \( \rho(g) = \id_F \) for every \( g \). It is a representation because \( \id_F \cdot \id_F = \id_F \), matching \( \rho(gh) = \rho(g)\rho(h) \). Its degree is \( 1 \). This is the degenerate case, and it is not a curiosity: it is one of the basic building blocks, and in Section 08 it is the piece that detects averages.
- **The sign representation of \( S_n \).** \( V = F \) and \( \rho(\sigma) = \sgn(\sigma)\,\id_F \), where \( \sgn \) is the sign of a permutation (@def-sign-permutation). It is a homomorphism because \( \sgn(\sigma\tau) = \sgn(\sigma)\sgn(\tau) \) (@thm-sign-multiplicative). Over a field of characteristic \( 2 \) we have \( -1 = 1 \), so the sign representation coincides with the trivial one; over \( \nC \) it does not. It is faithful on \( S_2 \), whose two elements have signs \( 1 \) and \( -1 \), but not on \( S_n \) for \( n \ge 3 \), where \( \sgn((1\ 2\ 3)) = 1 = \sgn(\id) \) while \( (1\ 2\ 3) \ne \id \).
- **The permutation representation of \( S_n \).** \( V = F^n \) and \( \rho(\sigma)\e_i = \e_{\sigma(i)} \), extended linearly (@thm-linear-map-from-any-basis). Then \( \rho(\sigma)\rho(\tau)\e_i = \rho(\sigma)\e_{\tau(i)} = \e_{\sigma(\tau(i))} = \rho(\sigma\tau)\e_i \), where the last step uses that \( \sigma\tau \) means "first \( \tau \), then \( \sigma \)". So \( \rho \) is a homomorphism, and each \( \rho(\sigma) \) is invertible with inverse \( \rho(\sigma^{-1}) \). The matrix of \( \rho(\sigma) \) in the standard basis is the permutation matrix \( \P_\sigma \) of @def-permutation-matrix. The same recipe works for any subgroup of \( S_n \).
- **The rotation representation of \( \nZ/n\nZ \) over \( \nR \).** \( V = \nR^2 \) and \( \rho([k]) \) is rotation by \( 2\pi k/n \), with matrix \( \begin{pmatrix} \cos(2\pi k/n) & -\sin(2\pi k/n) \\ \sin(2\pi k/n) & \cos(2\pi k/n)\end{pmatrix} \). Composing rotations adds angles, so \( \rho([k])\rho([l]) = \rho([k+l]) \); and rotating by \( 2\pi n/n = 2\pi \) is the identity, so the recipe does not depend on the representative \( k \). For \( n \ge 3 \) this representation has no invariant line. A line invariant under \( \rho([1]) \) would give that matrix a real eigenvalue (@prp-one-dimensional-invariant), but with \( c = \cos(2\pi/n) \) and \( s = \sin(2\pi/n) \) its characteristic polynomial is \( x^2 - 2cx + 1 \), of discriminant \( 4c^2 - 4 = -4s^2 \), which is negative because \( 0 < 2\pi/n < \pi \) forces \( s \ne 0 \) when \( n \ge 3 \). (The quarter-turn case is @exm-rotation-invariant-subspaces.) Section 04 turned this into the standard warning about Schur's lemma over \( \nR \).
- **The regular representation.** \( V = F[G] \), the group algebra of @def-group-algebra: the free vector space on the set \( G \) (@def-free-vector-space), with basis \( \{\delta_g : g \in G\} \) and multiplication determined by \( \delta_g\delta_h = \delta_{gh} \). Its dimension is \( \lvert G\rvert \). Put \( \rho_{\mathrm{reg}}(g)\delta_h = \delta_{gh} \), extended linearly. Then \( \rho_{\mathrm{reg}}(g)\rho_{\mathrm{reg}}(g')\delta_h = \delta_{gg'h} = \rho_{\mathrm{reg}}(gg')\delta_h \), so \( \rho_{\mathrm{reg}} \) is a homomorphism, and \( \rho_{\mathrm{reg}}(g) \) is invertible with inverse \( \rho_{\mathrm{reg}}(g^{-1}) \). It is faithful: if \( \rho_{\mathrm{reg}}(g) = \id \) then \( \delta_g = \rho_{\mathrm{reg}}(g)\delta_1 = \delta_1 \), so \( g = 1 \) because the \( \delta_h \) are distinct basis vectors. Its degree is \( \lvert G\rvert \).

**Non-example by minimal change.** Keep \( V = F^2 \) and \( G = \nZ/4\nZ \), and try \( \rho([k]) = \begin{pmatrix} 1 & k \\ 0 & 1\end{pmatrix} \) over \( \nQ \). Each matrix is invertible, and \( \rho([k])\rho([l]) = \begin{pmatrix} 1 & k+l \\ 0 & 1\end{pmatrix} \), so multiplicativity holds on representatives. But the recipe is not **well defined** on \( \nZ/4\nZ \): the class \( [0] \) is also \( [4] \), and \( \begin{pmatrix} 1 & 4 \\ 0 & 1\end{pmatrix} \ne \I_2 \). The clause that fails is that \( \rho \) must be a function on \( G \). Over \( \nF_2 \) the same recipe on \( \nZ/2\nZ \) *is* well defined, because \( \begin{pmatrix} 1 & 2 \\ 0 & 1\end{pmatrix} = \I_2 \) there; we return to that example when Maschke's theorem breaks.

::: {.warning}
**A representation need not remember the group.** The trivial representation of any group is a representation, and it forgets everything. Conversely, a non-injective \( \rho \) can still be useful: the sign representation of \( S_n \) has a huge kernel yet separates even from odd permutations. When a statement needs \( \rho \) to see all of \( G \), it must say **faithful**; none of the theorems below does.
:::

::: {.check}
Is \( \rho \colon \nZ/3\nZ \to \GL_1(\nR) = \nR \setminus \{0\} \), \( \rho([k]) = (-1)^k \), a representation?
:::

::: {.solution}
No: it is not well defined. We have \( [0] = [3] \) in \( \nZ/3\nZ \), but \( (-1)^0 = 1 \) while \( (-1)^3 = -1 \). Equivalently, a representation of degree \( 1 \) is a homomorphism \( \nZ/3\nZ \to \nR\setminus\{0\} \), and \( \rho([1])^3 = \rho([0]) = 1 \) forces \( \rho([1]) = 1 \), since \( 1 \) is the only real cube root of \( 1 \). So the only degree-\( 1 \) real representation of \( \nZ/3\nZ \) is the trivial one.
:::

## Subrepresentations, equivalence, and irreducibility

Having made operators, we ask the question this book always asks of a family of operators: can the space be broken into smaller pieces that the family preserves? Chapter 8 called such a piece an invariant subspace (@def-invariant-subspace). Here the family is \( \{\rho(g) : g \in G\} \).

::: {#def-subrepresentation}
[Subrepresentation]

Let \( \rho \) be a representation of \( G \) on \( V \). A subspace \( U \subseteq V \) is **\( G \)-invariant** if \( \rho(g)\u \in U \) **for every** \( g \in G \) and every \( \u \in U \). In that case the restrictions \( \rho(g)|_U \) define a representation \( \rho|_U \) of \( G \) on \( U \), the **subrepresentation** of \( \rho \) on \( U \).
:::

Two checks make this legitimate. First, \( \rho(g)|_U \) really is an operator **on** \( U \), by invariance. Second, it is invertible on \( U \): applying invariance to \( g^{-1} \) gives \( \rho(g)^{-1}U = \rho(g^{-1})U \subseteq U \), so \( \rho(g)|_U \) has a two-sided inverse on \( U \), namely \( \rho(g^{-1})|_U \). Multiplicativity is inherited. The subspaces \( \{\0\} \) and \( V \) are always \( G \)-invariant; we call them the **trivial** invariant subspaces.

::: {#def-equivalent-representations}
[Equivalence of representations]

Let \( \rho \) and \( \rho' \) be representations of \( G \) on \( V \) and \( V' \), over the same field. A linear map \( S \colon V \to V' \) **intertwines** \( \rho \) and \( \rho' \) if
\[
  S\,\rho(g) = \rho'(g)\,S \qquad \text{for every } g \in G .
\]
The representations are **equivalent**, written \( \rho \cong \rho' \), if some intertwining \( S \) is an isomorphism; equivalently, if \( \rho'(g) = S\rho(g)S^{-1} \) for all \( g \).
:::

Equivalence is what "the same representation written in another basis" means. Indeed, if \( V = V' = F^n \) and \( S \) is an invertible matrix, then \( \rho'(g) = S\rho(g)S^{-1} \) is simultaneous similarity of the whole family \( \{\rho(g)\} \) by one matrix. It is an equivalence relation: \( \id_V \) intertwines \( \rho \) with itself; if \( S \) intertwines \( \rho \) with \( \rho' \) and is invertible then \( S^{-1} \) intertwines \( \rho' \) with \( \rho \), since \( S\rho(g) = \rho'(g)S \) gives \( \rho(g)S^{-1} = S^{-1}\rho'(g) \); and a composition of intertwining isomorphisms intertwines.

::: {#def-irreducible-representation}
[Irreducible representation]

A representation \( \rho \) of \( G \) on \( V \) is **irreducible** if \( V \ne \{\0\} \) and the only \( G \)-invariant subspaces of \( V \) are \( \{\0\} \) and \( V \). A representation with \( V \ne \{\0\} \) that is not irreducible is **reducible**.
:::

Read the two clauses separately. The zero space is excluded by decree, exactly as \( 1 \) is excluded from the primes: keeping it would break every statement of the form "every representation is built from irreducible ones". The second clause is the real content.

**Examples and a non-example.**

- Every representation of degree \( 1 \) is irreducible: a one-dimensional space has no subspaces but \( \{\0\} \) and itself.
- The permutation representation of \( S_3 \) on \( F^3 \) is **reducible** for every \( F \). The line \( L = \Span(\e_1 + \e_2 + \e_3) \) is \( S_3 \)-invariant, since \( \rho(\sigma)(\e_1+\e_2+\e_3) = \e_{\sigma(1)}+\e_{\sigma(2)}+\e_{\sigma(3)} = \e_1+\e_2+\e_3 \), the same three basis vectors in another order. And \( L \ne \{\0\} \), \( L \ne F^3 \).
- So is the **sum-zero** subspace \( W = \{\x \in F^3 : x_1 + x_2 + x_3 = 0\} \), of dimension \( 2 \): permuting the coordinates of \( \x \) does not change their sum. We will see below that over \( \nC \) the subrepresentation on \( W \) is irreducible; this is the **standard representation** of \( S_3 \).
- **Non-example by minimal change.** Replace \( S_3 \) by the subgroup \( H = \{\id, (1\ 2)\} \subseteq S_3 \) and keep \( V = F^3 \). Then \( \Span(\e_3) \) is \( H \)-invariant, though it is not \( S_3 \)-invariant. Invariance depends on the whole group, not on one element of it.

Finally, the operation that puts representations together. If \( \rho_1, \rho_2 \) are representations of \( G \) on \( V_1, V_2 \), their **direct sum** is the representation \( \rho_1 \oplus \rho_2 \) on \( V_1 \oplus V_2 \) given by \( (\rho_1\oplus\rho_2)(g)(\v_1, \v_2) = (\rho_1(g)\v_1, \rho_2(g)\v_2) \). In a basis adapted to the decomposition its matrix is block diagonal, \( \rho_1(g) \oplus \rho_2(g) \). Conversely, if \( V = U \oplus W \) with both summands \( G \)-invariant, then the map \( U \oplus W \to V \), \( (\u, \w) \mapsto \u + \w \), is an isomorphism intertwining \( \rho|_U \oplus \rho|_W \) with \( \rho \), so \( \rho \cong \rho|_U \oplus \rho|_W \). So "decomposing a representation" and "finding an invariant complement" are the same task.

## Representations of \( G \) and representations of \( F[G] \)

Here is the bridge that puts Sections 01–06 to work. The group algebra \( F[G] \) was built in @def-group-algebra precisely so that the next theorem is true.

::: {#thm-representations-are-modules-over-the-group-algebra}
[Representations of \( G \) are representations of \( F[G] \)]

Let \( G \) be a finite group, \( F \) a field and \( V \) a finite-dimensional vector space over \( F \). The assignment
\[
  \rho \ \longmapsto \ \widetilde\rho, \qquad
  \widetilde\rho\Bigl(\sum_{g \in G} a_g \delta_g\Bigr) \coloneqq \sum_{g \in G} a_g\,\rho(g),
\]
is a bijection from the set of representations \( \rho \colon G \to \GL(V) \) onto the set of algebra homomorphisms \( F[G] \to \End(V) \) (@def-algebra-homomorphism) — that is, onto the ways of making \( V \) an \( F[G] \)-space in the sense of @def-representation-of-an-algebra. Moreover a subspace \( U \subseteq V \) is \( G \)-invariant for \( \rho \) if and only if \( \widetilde\rho(a)U \subseteq U \) for every \( a \in F[G] \).
:::

::: {.idea}
An element of \( F[G] \) is a formal linear combination of group elements, so a linear map out of \( F[G] \) is determined by, and may be prescribed freely on, the basis \( \{\delta_g\} \). The only thing to check is that "multiplicative on the basis" upgrades to "multiplicative everywhere", and that is bilinearity of both products. The inverse map recovers \( \rho \) by restricting to the basis; the one point needing care is why \( \widetilde\rho(\delta_g) \) is automatically **invertible**, which is where \( \delta_g\delta_{g^{-1}} = \delta_1 \) earns its keep.
:::

::: {.proof}
Let \( \rho \colon G \to \GL(V) \) be a representation. The formula defines a linear map \( \widetilde\rho \colon F[G] \to \End(V) \), because \( \{\delta_g\} \) is a basis of \( F[G] \) and a linear map may be prescribed on a basis (@thm-linear-map-from-any-basis). It sends \( \delta_1 \) to \( \rho(1) = \id_V \) (@thm-homomorphism-basic-properties). For multiplicativity, take \( a = \sum_g a_g\delta_g \) and \( b = \sum_h b_h\delta_h \). Multiplication in \( F[G] \) and composition in \( \End(V) \) are both bilinear, so
\[
\begin{aligned}
  \widetilde\rho(ab) &= \widetilde\rho\Bigl(\sum_{g, h} a_g b_h\, \delta_{gh}\Bigr)
   = \sum_{g, h} a_g b_h\, \rho(gh) \\
   &= \sum_{g, h} a_g b_h\, \rho(g)\rho(h)
   = \Bigl(\sum_g a_g \rho(g)\Bigr)\Bigl(\sum_h b_h \rho(h)\Bigr) = \widetilde\rho(a)\widetilde\rho(b),
\end{aligned}
\]
where the third equality is the homomorphism property of \( \rho \). Hence \( \widetilde\rho \) is an algebra homomorphism.

Conversely, let \( \varphi \colon F[G] \to \End(V) \) be an algebra homomorphism, and set \( \rho(g) \coloneqq \varphi(\delta_g) \). Since \( \delta_1 \) is the identity of \( F[G] \) (@def-group-algebra) and \( \id_V \) is the identity of \( \End(V) \), the unital clause of @def-algebra-homomorphism gives \( \varphi(\delta_1) = \id_V \). Then \( \rho(g)\rho(h) = \varphi(\delta_g\delta_h) = \varphi(\delta_{gh}) = \rho(gh) \). In particular \( \rho(g)\rho(g^{-1}) = \varphi(\delta_1) = \id_V \) and likewise in the other order, so each \( \rho(g) \) is invertible and \( \rho \) maps into \( \GL(V) \). Thus \( \rho \) is a representation, and \( \widetilde\rho = \varphi \) because the two agree on the basis \( \{\delta_g\} \) and both are linear. Since also \( \widetilde\rho(\delta_g) = \rho(g) \), the two constructions are mutually inverse, and the assignment is a bijection.

For the last sentence, suppose \( U \) is \( G \)-invariant. For \( a = \sum_g a_g\delta_g \) and \( \u \in U \), each \( \rho(g)\u \) lies in \( U \), and \( U \) is a subspace, so \( \widetilde\rho(a)\u = \sum_g a_g \rho(g)\u \in U \). Conversely, if \( \widetilde\rho(a)U \subseteq U \) for all \( a \), take \( a = \delta_g \). This proves the theorem.
:::

So the two languages are interchangeable, and we use whichever is shorter. A \( G \)-invariant subspace is an \( F[G] \)-invariant subspace; an irreducible representation of \( G \) on \( V \) is exactly a simple \( F[G] \)-space in the sense of @def-simple-module; and a map intertwining two representations of \( G \) is exactly an \( F[G] \)-map in the sense of @def-intertwining-map, since the condition \( S\rho(g) = \rho'(g)S \) for all \( g \) extends by linearity to all of \( F[G] \). In particular Schur's lemma (@thm-schurs-lemma) applies verbatim to irreducible representations of groups, and we use it that way in Section 08.

::: {.remark}
Working with \( F[G] \) rather than with \( G \) buys one thing that matters: the ability to **add** group elements. Every averaging argument below lives in \( F[G] \), not in \( G \). Chapter 9 §07 made the same move for a single operator, replacing \( T \) by the algebra \( F[T] \) and the space by an \( F[x] \)-module.
:::

## Maschke's theorem

We now know that a reducible representation has a proper non-zero invariant subspace \( U \). To break \( V \) into pieces we need more: an invariant **complement**, a \( G \)-invariant \( W \) with \( V = U \oplus W \). An ordinary complement always exists (@thm-complement-exists), but it has no reason to be invariant.

The idea for repairing it is the one move this chapter uses over and over. Start with an object that is not invariant, and average its \( G \)-translates. The average is invariant because translating it permutes the terms of the sum. Averaging divides by \( \lvert G\rvert \), and that is the whole hypothesis.

::: {#lem-group-order-invertible}
[When the group order is invertible]

Let \( F \) be a field and \( m \) a positive integer. Then \( m \cdot 1_F \ne 0 \) in \( F \) if and only if \( \operatorname{char} F \) does not divide \( m \).
:::

::: {.proof}
If \( \operatorname{char} F = 0 \), then \( m \cdot 1_F \ne 0 \) for every positive integer \( m \) (@def-characteristic), and \( 0 \) divides no positive integer, so both sides of the equivalence hold. Assume from now on that \( p \coloneqq \operatorname{char} F > 0 \), so \( p \) is the **smallest** positive integer with \( p\cdot 1_F = 0 \).

(\( \Rightarrow \)) We prove the contrapositive: if \( p \mid m \), then \( m\cdot 1_F = 0 \). Write \( m = qp \) with \( q \ge 1 \). By @lem-integer-multiples, \( m\cdot 1_F = (qp)\cdot 1_F = (q\cdot 1_F)(p\cdot 1_F) = (q\cdot 1_F)\cdot 0 = 0 \).

(\( \Leftarrow \)) Suppose, for a contradiction, that some positive integer \( m \) has \( m\cdot 1_F = 0 \) and \( p \nmid m \). Choose such an \( m \) as small as possible. Now \( m \ne p \), since \( p \mid p \), and \( m > p \), since \( p \) is the smallest positive integer killing \( 1_F \). So \( m - p \) is a positive integer, and by @lem-integer-multiples
\[
  (m - p)\cdot 1_F + p \cdot 1_F = m \cdot 1_F = 0 ,
\]
whence \( (m-p)\cdot 1_F = 0 \). Also \( p \nmid m - p \), for otherwise \( p \) would divide \( (m-p) + p = m \). This contradicts the minimality of \( m \). This proves the lemma.
:::

::: {#thm-maschke}
[Maschke's Theorem]

Let \( G \) be a **finite** group and \( F \) a field whose characteristic does **not** divide \( \lvert G\rvert \). Let \( \rho \) be a representation of \( G \) on a finite-dimensional space \( V \) over \( F \), and let \( U \subseteq V \) be a \( G \)-invariant subspace. Then there is a \( G \)-invariant subspace \( W \subseteq V \) with
\[
  V = U \oplus W .
\]
:::

::: {.idea}
Pick **any** projection \( P \) of \( V \) onto \( U \); its kernel is a complement, but the wrong one, because \( P \) need not commute with the \( \rho(g) \). Repair it by averaging the conjugates \( \rho(g)P\rho(g)^{-1} \) over \( g \in G \). ① Each conjugate is again a projection onto \( U \), because \( U \) is invariant. ② Their average \( P_0 \) is therefore again a projection onto \( U \) — here we divide by \( \lvert G\rvert \). ③ Conjugating \( P_0 \) by \( \rho(h) \) only permutes the terms of the sum, so \( P_0 \) commutes with every \( \rho(h) \), and then its kernel is invariant.
:::

::: {.proof}
Write \( n = \lvert G\rvert \). By hypothesis and @lem-group-order-invertible, \( n \cdot 1_F \ne 0 \), so the scalar \( \tfrac{1}{n} \coloneqq (n\cdot 1_F)^{-1} \) exists in \( F \). By @thm-complement-exists there is a subspace \( W_0 \) with \( V = U \oplus W_0 \); let \( P \in \cL(V) \) be the projection onto \( U \) along \( W_0 \) (@thm-projection-direct-sum (b)), so \( \im P = U \) and \( P\u = \u \) for all \( \u \in U \). Define
\[
  P_0 \coloneqq \frac{1}{n}\sum_{g \in G} \rho(g)\, P\, \rho(g)^{-1} \ \in \cL(V).
\]

**Step 1: \( \im P_0 \subseteq U \).** Let \( \v \in V \) and \( g \in G \). Then \( P\rho(g)^{-1}\v \in \im P = U \), and \( U \) is \( G \)-invariant, so \( \rho(g)P\rho(g)^{-1}\v \in U \). A subspace is closed under sums and scalar multiples, so \( P_0\v \in U \).

**Step 2: \( P_0\u = \u \) for \( \u \in U \).** Let \( \u \in U \) and \( g \in G \). Since \( U \) is \( G \)-invariant and \( \rho(g)^{-1} = \rho(g^{-1}) \), we have \( \rho(g)^{-1}\u \in U \), so \( P\rho(g)^{-1}\u = \rho(g)^{-1}\u \) and hence \( \rho(g)P\rho(g)^{-1}\u = \u \). Summing over the \( n \) elements of \( G \) gives \( \sum_g \rho(g)P\rho(g)^{-1}\u = (n\cdot 1_F)\u \), and multiplying by \( \tfrac1n \) gives \( P_0\u = \u \).

By Steps 1 and 2, \( P_0\v \in U \) for every \( \v \), and \( P_0 \) fixes \( U \) pointwise; therefore \( P_0^2\v = P_0(P_0\v) = P_0\v \), so \( P_0 \) is a projection (@def-projection-operator) with \( \im P_0 = U \).

**Step 3: \( P_0 \) commutes with every \( \rho(h) \).** Fix \( h \in G \). Then
\[
  \rho(h)P_0\rho(h)^{-1} = \frac1n \sum_{g \in G} \rho(hg)\,P\,\rho(hg)^{-1},
\]
using \( \rho(h)\rho(g) = \rho(hg) \) and \( \rho(g)^{-1}\rho(h)^{-1} = (\rho(h)\rho(g))^{-1} = \rho(hg)^{-1} \). The map \( g \mapsto hg \) is a bijection \( G \to G \), with inverse \( g \mapsto h^{-1}g \) by @thm-group-basic-properties, so as \( g \) runs over \( G \) so does \( hg \), and the sum is unchanged: \( \rho(h)P_0\rho(h)^{-1} = P_0 \). Multiplying on the right by \( \rho(h) \) gives \( \rho(h)P_0 = P_0\rho(h) \).

**Step 4: conclusion.** Put \( W \coloneqq \ker P_0 \). By @thm-projection-direct-sum (a), \( V = \im P_0 \oplus \ker P_0 = U \oplus W \). And \( W \) is \( G \)-invariant: if \( P_0\w = \0 \) and \( h \in G \), then by Step 3, \( P_0\rho(h)\w = \rho(h)P_0\w = \0 \), so \( \rho(h)\w \in W \). This proves the theorem.
:::

Two hypotheses did real work, and it is worth naming where. **Finiteness** of \( G \) is what makes the sum \( \sum_{g} \) a finite sum, hence an operator at all. The condition on the **characteristic** is what makes \( \tfrac1n \) exist, and Step 2 is where it is spent: without the division, the computation in Step 2 gives \( \sum_g \rho(g)P\rho(g)^{-1}\u = (n\cdot 1_F)\u \), which is \( \0 \) for every \( \u \in U \) when \( \operatorname{char} F \) divides \( n \). The unnormalized sum then **annihilates** \( U \) instead of fixing it, and there is nothing to rescue. Both failures are real, not artifacts of the proof.

::: {#exm-maschke-fails-char-p}
[Maschke fails when the characteristic divides the order]

Let \( p \) be a prime, \( F = \nF_p \), \( G = \nZ/p\nZ \) and \( V = \nF_p^2 \). Define
\[
  \rho([k]) \coloneqq \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix} \in \GL_2(\nF_p).
\]
Show that \( \rho \) is a well-defined representation, that \( U = \Span(\e_1) \) is \( G \)-invariant, and that \( U \) has **no** \( G \)-invariant complement.
:::

::: {.solution}
*Well defined.* The entry \( k \) is read in \( \nF_p \), so the matrix depends only on \( k \) modulo \( p \); and \( \begin{psmallmatrix}1&k\\0&1\end{psmallmatrix}\begin{psmallmatrix}1&l\\0&1\end{psmallmatrix} = \begin{psmallmatrix}1&k+l\\0&1\end{psmallmatrix} \), so \( \rho([k])\rho([l]) = \rho([k]+[l]) \). Each matrix is invertible, with inverse \( \rho([-k]) \). So \( \rho \) is a representation of the additive group \( \nZ/p\nZ \). Here \( \lvert G\rvert = p = \operatorname{char}\nF_p \), so the characteristic **does** divide the order and the hypothesis of @thm-maschke fails.

*The invariant line.* \( \rho([k])\e_1 = \e_1 \) for every \( k \), so \( U = \Span(\e_1) \) is \( G \)-invariant, and \( U \ne \{\0\}, V \).

*No invariant complement.* If \( V = U \oplus W \), then \( \dim W = 2 - 1 = 1 \) by @thm-dimension-formula-subspace-dim, so \( W = \Span(\v) \) for some \( \v = (a, b) \ne \0 \); and \( b \ne 0 \), since \( b = 0 \) would force \( a \ne 0 \) and \( W = \Span(\e_1) = U \), which is not a complement of itself. Suppose \( W \) is \( G \)-invariant. Then \( \rho([1])\v = (a + b,\, b) \) must be a scalar multiple \( \lambda\v = (\lambda a, \lambda b) \). Comparing second coordinates and dividing by \( b \ne 0 \) gives \( \lambda = 1 \); comparing first coordinates then gives \( a + b = a \), so \( b = 0 \), a contradiction. Hence \( U \) has no \( G \)-invariant complement. In fact \( U \) is the **only** non-trivial invariant subspace, so \( V \) is neither irreducible nor a direct sum of irreducibles.
:::

::: {.warning}
**Do not drop finiteness either.** Let \( G = \nZ \) (infinite) act on \( \nQ^2 \) by \( \rho(k) = \begin{psmallmatrix}1&k\\0&1\end{psmallmatrix} \) — now well defined, since \( \nZ \) has no relations to respect. The computation just made, with \( b \ne 0 \) in \( \nQ \), again shows \( \Span(\e_1) \) is invariant with no invariant complement, and here the characteristic is \( 0 \). Averaging over \( \nZ \) is not an option: the sum has infinitely many terms.
:::

Once one invariant complement can always be found, the full decomposition follows by induction.

::: {#cor-complete-reducibility}
[Complete Reducibility of Group Representations]

Let \( G \) be a finite group and \( F \) a field with \( \operatorname{char} F \nmid \lvert G\rvert \) — for instance \( F = \nC \). Then every representation \( \rho \) of \( G \) on a non-zero finite-dimensional space \( V \) over \( F \) decomposes as
\[
  V = V_1 \oplus V_2 \oplus \dots \oplus V_r
\]
with each \( V_i \) a \( G \)-invariant subspace on which the subrepresentation is irreducible.
:::

::: {.proof}
We argue by strong induction on \( \dim V \ge 1 \) (@thm-strong-induction). If \( \rho \) is irreducible, take \( r = 1 \) and \( V_1 = V \). Otherwise \( V \) has a \( G \)-invariant subspace \( U \) with \( U \ne \{\0\} \) and \( U \ne V \). By @thm-maschke there is a \( G \)-invariant \( W \) with \( V = U \oplus W \), and \( W \ne \{\0\} \) since \( U \ne V \). Both \( \dim U \) and \( \dim W \) are at least \( 1 \), and since \( U \cap W = \{\0\} \) (@thm-direct-sum-criteria) the dimension formula @thm-dimension-formula-subspace-dim gives \( \dim U + \dim W = \dim V \); hence both are smaller than \( \dim V \). The induction hypothesis decomposes \( U \) and \( W \) into irreducible invariant subspaces, and concatenating the two lists decomposes \( V \), because a subspace of \( U \) invariant under \( \rho|_U \) is invariant under \( \rho \). This proves the corollary.
:::

In the language of Section 03, the corollary says that \( F[G] \) acts semisimply on every representation (@def-semisimple-algebra, @thm-semisimple-iff-sum-of-simples); applied to the regular representation, it says \( F[G] \) is a semisimple algebra. Section 06's structure theorem then applies to \( \nC[G] \), and Section 08 cashes that in.

::: {.check}
Where exactly does the proof of @cor-complete-reducibility use that \( V \ne \{\0\} \)?
:::

::: {.solution}
In the base of the induction and in the meaning of the conclusion. If \( V = \{\0\} \) it is not irreducible (@def-irreducible-representation excludes the zero space) and it has no non-zero invariant subspace to split off, so neither branch of the argument applies. The usual convention is that \( \{\0\} \) is the empty direct sum, \( r = 0 \); the corollary is stated with \( V \ne \{\0\} \) so that \( r \ge 1 \).
:::

## Two families worked out

We close with the two examples Section 08 will compute characters for. Both are over \( \nC \), where @cor-complete-reducibility applies to every finite group.

::: {#exm-cyclic-irreducibles}
[The irreducible complex representations of a cyclic group]

Let \( G = \nZ/n\nZ \) and \( F = \nC \). Determine all irreducible representations of \( G \) up to equivalence.
:::

::: {.solution}
*Every irreducible is one-dimensional.* Let \( \rho \) be a representation of \( G \) on \( V \ne \{\0\} \) over \( \nC \), and set \( A = \rho([1]) \). By @thm-complex-operator-has-eigenvalue, \( A \) has an eigenvector \( \v \ne \0 \), say \( A\v = \lambda\v \). The line \( L = \Span(\v) \) is invariant under \( A \), hence under every power \( A^k = \rho([k]) \), so \( L \) is \( G \)-invariant. If \( \rho \) is irreducible then \( L = V \), so \( \dim V = 1 \). (For abelian \( G \) the algebra \( \nC[G] \) is commutative, since \( \delta_g\delta_h = \delta_{gh} = \delta_{hg} = \delta_h\delta_g \) and multiplication is bilinear; so this is also @cor-abelian-irreducibles-are-lines read through @thm-representations-are-modules-over-the-group-algebra.)

*Listing them.* A one-dimensional representation is a homomorphism \( \chi \colon \nZ/n\nZ \to \nC\setminus\{0\} \), determined by \( z = \chi([1]) \), which must satisfy \( z^n = \chi([n]) = \chi([0]) = 1 \). So \( z \) is an \( n \)-th root of unity, \( z = \omega^k \) with \( \omega = e^{2\pi i/n} \) and \( 0 \le k \le n-1 \) (@exm-roots-of-unity). Conversely each such \( z \) does define a homomorphism \( \chi_k([j]) = \omega^{jk} \): the recipe respects representatives because \( \omega^{n} = 1 \), and \( \omega^{(j+l)k} = \omega^{jk}\omega^{lk} \).

*They are pairwise inequivalent.* Two one-dimensional representations are equivalent exactly when they are equal, since on a one-dimensional space every operator is \( \lambda\,\id \) for a scalar \( \lambda \), and \( S(\lambda\,\id)S^{-1} = \lambda\,\id \) for every isomorphism \( S \). And \( \chi_k \ne \chi_l \) for \( 0 \le k < l \le n-1 \), because \( \chi_k([1]) = \omega^k \ne \omega^l = \chi_l([1]) \), the \( n \)-th roots of unity being distinct.

So \( \nZ/n\nZ \) has exactly \( n \) irreducible complex representations, all of degree \( 1 \), namely \( \chi_0, \dots, \chi_{n-1} \). Their degrees satisfy \( \sum_k 1^2 = n = \lvert G\rvert \), the count @cor-dimension-count gives for the semisimple algebra \( \nC[G] \).
:::

::: {#exm-s3-irreducibles}
[The irreducible complex representations of the symmetric group on three letters]

Write down three pairwise inequivalent irreducible complex representations of \( S_3 \), with explicit matrices for the two-dimensional one.
:::

::: {.solution}
*Trivial and sign.* \( \rho_{\mathrm{triv}}(\sigma) = 1 \) and \( \rho_{\mathrm{sgn}}(\sigma) = \sgn(\sigma) \), both on \( \nC \), both irreducible because their degree is \( 1 \). They are inequivalent: \( \rho_{\mathrm{triv}}((1\ 2)) = 1 \ne -1 = \rho_{\mathrm{sgn}}((1\ 2)) \).

*The standard representation.* Take the permutation representation on \( \nC^3 \) and restrict it to the invariant plane \( W = \{\x : x_1 + x_2 + x_3 = 0\} \). A basis of \( W \) is \( \sB = (\f_1, \f_2) \) with \( \f_1 = \e_1 - \e_2 \) and \( \f_2 = \e_2 - \e_3 \): they lie in \( W \), they are independent, and \( \dim W = 2 \) because \( W \) is the kernel of the surjective functional \( \x \mapsto x_1+x_2+x_3 \) on \( \nC^3 \) (@thm-rank-nullity). Since \( S_3 \) is generated by \( (1\ 2) \) and \( (1\ 2\ 3) \) — every element of \( S_3 \) is a product of transpositions (@thm-transpositions-generate), and \( (1\ 3) = (1\ 2\ 3)(1\ 2) \), \( (2\ 3) = (1\ 2)(1\ 2\ 3) \) — it is enough to record two matrices. With \( \rho(\sigma)\e_i = \e_{\sigma(i)} \):
\[
\begin{aligned}
  \rho((1\ 2))\f_1 &= \e_2 - \e_1 = -\f_1, \\
  \rho((1\ 2))\f_2 &= \e_1 - \e_3 = \f_1 + \f_2, \\
  \rho((1\ 2\ 3))\f_1 &= \e_2 - \e_3 = \f_2, \\
  \rho((1\ 2\ 3))\f_2 &= \e_3 - \e_1 = -\f_1 - \f_2 .
\end{aligned}
\]
Writing \( R_\sigma \coloneqq \rho(\sigma)|_W \), the two matrices in the basis \( \sB \) are
\[
  \mtx{R_{(1\ 2)}}{\sB}{\sB} = \begin{pmatrix} -1 & 1 \\ 0 & 1 \end{pmatrix},
  \qquad
  \mtx{R_{(1\ 2\ 3)}}{\sB}{\sB} = \begin{pmatrix} 0 & -1 \\ 1 & -1 \end{pmatrix}.
\]
The remaining four matrices follow by multiplying: \( \I_2 \) for \( \id \), \( \begin{psmallmatrix}0&-1\\-1&0\end{psmallmatrix} \) for \( (1\ 3) \), \( \begin{psmallmatrix}1&0\\1&-1\end{psmallmatrix} \) for \( (2\ 3) \) and \( \begin{psmallmatrix}-1&1\\-1&0\end{psmallmatrix} \) for \( (1\ 3\ 2) \).

*Irreducibility.* A proper non-zero invariant subspace of the plane \( W \) would be a line \( \Span(\v) \), and \( \v \) would be an eigenvector of **both** displayed matrices. The first has eigenvalues \( -1 \) and \( 1 \), with eigenvectors spanned by \( (1, 0) \) and \( (1, 2) \) respectively. The second has characteristic polynomial \( x^2 + x + 1 \), whose roots are the two primitive cube roots of unity; neither \( (1,0) \) nor \( (1,2) \) is an eigenvector of it, since \( \begin{psmallmatrix}0&-1\\1&-1\end{psmallmatrix}(1,0) = (0,1) \) and \( \begin{psmallmatrix}0&-1\\1&-1\end{psmallmatrix}(1,2) = (-2,-1) \) are not multiples of \( (1,0) \), \( (1,2) \). So there is no common eigenvector, and the standard representation is irreducible.

*Inequivalent.* It has degree \( 2 \), the others degree \( 1 \), and equivalent representations act on spaces of the same dimension.

The degrees satisfy \( 1^2 + 1^2 + 2^2 = 6 = \lvert S_3\rvert \), which is the count @cor-dimension-count gives for the semisimple algebra \( \nC[S_3] \). That count runs over **all** isomorphism classes of irreducible \( \nC[S_3] \)-spaces (@thm-wedderburn), and a further class would add at least \( 1 \) to a total already equal to \( 6 \); so these three are all of the irreducible complex representations of \( S_3 \). Section 08 reaches the same conclusion by counting conjugacy classes, which does not require the list to be found first.
:::

## Exercises

### A. Check your understanding

::: {#exr-group-representations-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the definition of a representation of a group \( G \) on a vector space \( V \), and say which two properties of \( \rho \) come for free.
2. State Maschke's theorem with all of its hypotheses.
3. Determine whether the following is true: "every representation of degree \( 1 \) is irreducible." Justify your answer.
4. Give an example of a reducible representation of \( S_3 \) over \( \nC \), and name an invariant subspace.
5. Explain why \( \rho \colon \nZ/2\nZ \to \GL_1(\nQ) \), \( \rho([k]) = 2^k \), is **not** a representation.
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. A representation is a group homomorphism \( \rho \colon G \to \GL(V) \) with \( V \) finite-dimensional over \( F \), that is, \( \rho(gh) = \rho(g)\rho(h) \) for all \( g, h \in G \) with each \( \rho(g) \) invertible (@def-representation). Free: \( \rho(1) = \id_V \) and \( \rho(g^{-1}) = \rho(g)^{-1} \), by @thm-homomorphism-basic-properties.
2. If \( G \) is finite, \( F \) is a field with \( \operatorname{char} F \nmid \lvert G\rvert \), \( V \) is finite-dimensional over \( F \) and \( U \subseteq V \) is \( G \)-invariant, then \( U \) has a \( G \)-invariant complement \( W \), so \( V = U \oplus W \) (@thm-maschke).
3. True. If \( \dim V = 1 \) then \( V \ne \{\0\} \) and the only subspaces of \( V \) are \( \{\0\} \) and \( V \), so in particular the only invariant ones are the trivial ones.
4. The permutation representation of \( S_3 \) on \( \nC^3 \); the line \( \Span(\e_1+\e_2+\e_3) \) is invariant, as is the sum-zero plane.
5. It is not well defined: \( [0] = [2] \) in \( \nZ/2\nZ \), but \( 2^0 = 1 \ne 4 = 2^2 \). (Equivalently, a degree-\( 1 \) representation of \( \nZ/2\nZ \) needs \( \rho([1])^2 = 1 \), and the only rational solutions of \( z^2 = 1 \) are \( z = \pm 1 \).)
:::
:::

### B. Practice

::: {#exr-group-representations-b1}
[B1: Which of these are representations?]

Determine which of the following are representations. Justify your answer in each case.

::: {.enumerate options="label=(\alph*)"}
1. \( G = \nZ/6\nZ \), \( F = \nC \), \( \rho([k]) = \begin{pmatrix} \omega^k & 0 \\ 0 & \omega^{-k}\end{pmatrix} \) with \( \omega = e^{\pi i/3} \).
2. \( G = S_3 \), \( F = \nR \), \( \rho(\sigma) = \sgn(\sigma)\,\P_\sigma \), where \( \P_\sigma \) is the permutation matrix with \( \P_\sigma\e_i = \e_{\sigma(i)} \) (@def-permutation-matrix).
3. \( G = S_3 \), \( F = \nR \), \( \rho(\sigma) = \P_\sigma\tp \) with \( \P_\sigma \) as in (b).
4. \( G = \nZ/4\nZ \), \( F = \nR \), \( \rho([k]) = \begin{pmatrix} 1 & 0 \\ 0 & k+1 \end{pmatrix} \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Yes. Here \( \omega^6 = e^{2\pi i} = 1 \), so the matrix depends only on \( k \) modulo \( 6 \) and the map is well defined; it is diagonal, hence invertible since \( \omega^{\pm k} \ne 0 \); and \( \rho([k])\rho([l]) = \diag(\omega^{k+l}, \omega^{-k-l}) = \rho([k]+[l]) \).
2. Yes. Both factors are multiplicative: \( \sgn(\sigma\tau) = \sgn(\sigma)\sgn(\tau) \) (@thm-sign-multiplicative) and \( \P_\sigma\P_\tau = \P_{\sigma\tau} \) (@lem-permutation-matrices (a)). Scalars commute with matrices, so \( \rho(\sigma)\rho(\tau) = \sgn(\sigma\tau)\P_{\sigma\tau} = \rho(\sigma\tau) \), and \( \rho(\sigma) \) is invertible because \( \P_\sigma \) is and \( \sgn(\sigma) \ne 0 \).
3. No. Taking transposes reverses products: \( \rho(\sigma)\rho(\tau) = \P_\sigma\tp\P_\tau\tp = (\P_\tau\P_\sigma)\tp = \P_{\tau\sigma}\tp = \rho(\tau\sigma) \). Since \( S_3 \) is not abelian this differs from \( \rho(\sigma\tau) \): with \( \sigma = (1\ 2) \), \( \tau = (1\ 3) \) we get \( \tau\sigma = (1\ 2\ 3) \ne (1\ 3\ 2) = \sigma\tau \) (@exm-cycle-notation), and distinct permutations have distinct permutation matrices. (The repair is \( \sigma \mapsto \P_{\sigma^{-1}}\tp \), or equivalently \( \P_{\sigma} \) itself.)
4. No, on two counts. It is not well defined: \( [0] = [4] \) but \( \diag(1,1) \ne \diag(1,5) \). And it is not multiplicative even on representatives: \( \rho([1])\rho([1]) = \diag(1,4) \) while \( \rho([2]) = \diag(1,3) \).
:::
:::

::: {#exr-group-representations-b2}
[B2: Averaging an inner product]

Let \( G \) be a finite group and \( \rho \) a representation of \( G \) on a complex space \( V \) carrying an inner product \( \inner{\cdot}{\cdot} \) (@def-inner-product). Define
\[
  \inner{\u}{\v}_G \coloneqq \frac{1}{\lvert G\rvert}\sum_{g \in G} \inner{\rho(g)\u}{\rho(g)\v} .
\]
Prove that \( \inner{\cdot}{\cdot}_G \) is an inner product on \( V \) and that every \( \rho(g) \) is an isometry for it. Hence give a second proof of @thm-maschke over \( \nC \).
:::

::: {.solution}
*(IP1).* For fixed \( \v \), the map \( \u \mapsto \inner{\rho(g)\u}{\rho(g)\v} \) is linear in \( \u \), being a composition of the linear map \( \rho(g) \) with a slot that is linear by (IP1) for \( \inner{\cdot}{\cdot} \). A sum of linear maps times a scalar is linear.

*(IP2).* \( \inner{\v}{\u}_G = \tfrac1{\lvert G\rvert}\sum_g \inner{\rho(g)\v}{\rho(g)\u} = \tfrac1{\lvert G\rvert}\sum_g \conj{\inner{\rho(g)\u}{\rho(g)\v}} = \conj{\inner{\u}{\v}_G} \), since conjugation is additive.

*(IP3).* For \( \v \ne \0 \), each \( \rho(g)\v \ne \0 \) because \( \rho(g) \) is invertible, so each term \( \inner{\rho(g)\v}{\rho(g)\v} \) is \( > 0 \), and \( \lvert G\rvert > 0 \) is a positive real. Hence \( \inner{\v}{\v}_G > 0 \).

*Isometry.* For \( h \in G \), \( \inner{\rho(h)\u}{\rho(h)\v}_G = \tfrac1{\lvert G\rvert}\sum_g \inner{\rho(gh)\u}{\rho(gh)\v} = \inner{\u}{\v}_G \), because \( g \mapsto gh \) is a bijection of \( G \) (@thm-group-basic-properties).

*Second proof of Maschke over \( \nC \).* Let \( U \) be \( G \)-invariant and let \( W = U^{\perp} \) be its orthogonal complement for \( \inner{\cdot}{\cdot}_G \). Then \( V = U \oplus W \) by @thm-orthogonal-decomposition. If \( \w \in W \), \( \u \in U \) and \( h \in G \), then, writing \( \u = \rho(h)\bigl(\rho(h)^{-1}\u\bigr) \) and using that \( \rho(h) \) preserves \( \inner{\cdot}{\cdot}_G \),
\[
  \inner{\rho(h)\w}{\u}_G = \inner{\rho(h)\w}{\rho(h)\rho(h)^{-1}\u}_G = \inner{\w}{\rho(h)^{-1}\u}_G = 0,
\]
the last step because \( \rho(h)^{-1}\u = \rho(h^{-1})\u \in U \) and \( \w \in U^{\perp} \). So \( \rho(h)\w \in W \), and \( W \) is \( G \)-invariant. Note that this route needs \( F = \nR \) or \( \nC \), where inner products live, whereas @thm-maschke needs only a condition on the characteristic.
:::

::: {#exr-group-representations-b3}
[B3: Decomposing a permutation representation]

Number the coordinates of \( \nC^3 \) as \( 0, 1, 2 \), as in Chapter 11 §09, and let \( G = \nZ/3\nZ \) act by \( \rho([k]) = \S^k \), where \( \S \) is the cyclic shift, \( \S\x = (x_1, x_2, x_0) \). Check that \( \rho \) is a representation, decompose \( \nC^3 \) into one-dimensional invariant subspaces, and identify each with one of the \( \chi_k \) of @exm-cyclic-irreducibles.
:::

::: {.solution}
*A representation.* Shifting three times restores every entry, so \( \S^3 = \I \), and therefore \( \S^k \) depends only on \( k \) modulo \( 3 \): the recipe is well defined on \( \nZ/3\nZ \). It is multiplicative because \( \S^k\S^l = \S^{k+l} \), and each \( \S^k \) is invertible with inverse \( \S^{3-k} \).

*Decomposition.* Let \( \omega = e^{2\pi i/3} \). By @thm-shift-eigenvectors the vectors \( \f_j = \tfrac{1}{\sqrt3}(1, \omega^{j}, \omega^{2j}) \), \( j = 0, 1, 2 \), satisfy \( \S\f_j = \omega^{j}\f_j \). The three eigenvalues \( 1, \omega, \omega^2 \) are distinct, so the \( \f_j \) are independent (@thm-distinct-eigenvalues-independent), and three independent vectors in \( \nC^3 \) form a basis (@thm-right-size-basis). Hence
\[
  \nC^3 = \Span(\f_0)\oplus\Span(\f_1)\oplus\Span(\f_2),
\]
and each line is invariant under \( \S \), hence under every \( \rho([k]) = \S^k \).

*Identification.* On \( \Span(\f_j) \) the element \( [k] \) acts by the scalar \( \omega^{jk} \), which is exactly \( \chi_j([k]) \) in the notation of @exm-cyclic-irreducibles. So the three summands realize \( \chi_0, \chi_1, \chi_2 \): every irreducible representation of \( \nZ/3\nZ \) occurs exactly once.
:::

### C. Going deeper

::: {#exr-group-representations-c1}
[C1: One-dimensional representations and the commutator]

Let \( G \) be a finite group and \( F \) a field.

::: {.enumerate options="label=(\alph*)"}
1. Prove that every representation of degree \( 1 \) satisfies \( \rho(ghg^{-1}h^{-1}) = 1 \) for all \( g, h \in G \).
2. Deduce that the only degree-\( 1 \) complex representation of \( G = S_3 \) other than the trivial one is the sign representation. *Hint: write the \( 3 \)-cycle \( (1\ 2\ 3) \) in the form \( ghg^{-1}h^{-1} \) with \( g \) and \( h \) transpositions.*
:::
:::

::: {.solution}
(a) A degree-\( 1 \) representation takes values in \( F\setminus\{0\} \), which is abelian under multiplication. So \( \rho(ghg^{-1}h^{-1}) = \rho(g)\rho(h)\rho(g)^{-1}\rho(h)^{-1} = \rho(g)\rho(g)^{-1}\rho(h)\rho(h)^{-1} = 1 \), using @thm-homomorphism-basic-properties for the inverses.

(b) Let \( \rho \) have degree \( 1 \) over \( \nC \). Transpositions are their own inverses, so \( (1\ 2)(1\ 3)(1\ 2)^{-1}(1\ 3)^{-1} = (1\ 2)(1\ 3)(1\ 2)(1\ 3) \). Applying this product to each point, rightmost factor first: \( 1 \mapsto 3 \mapsto 3 \mapsto 1 \mapsto 2 \), \( 2 \mapsto 2 \mapsto 1 \mapsto 3 \mapsto 3 \) and \( 3 \mapsto 1 \mapsto 2 \mapsto 2 \mapsto 1 \). So the product is \( (1\ 2\ 3) \). By (a), \( \rho((1\ 2\ 3)) = 1 \), and then \( \rho((1\ 3\ 2)) = \rho((1\ 2\ 3))^{2} = 1 \). Let \( c = \rho((1\ 2)) \). Since \( (1\ 2)^2 = \id \), \( c^2 = 1 \), so \( c = \pm 1 \). Finally \( (1\ 3) = (1\ 2\ 3)(1\ 2) \) and \( (2\ 3) = (1\ 2)(1\ 2\ 3) \), so \( \rho((1\ 3)) = \rho((2\ 3)) = c \) as well. Thus \( \rho \) is determined by \( c \): for \( c = 1 \) it is trivial, and for \( c = -1 \) it agrees with \( \sgn \) on every element. Both values do occur, so there are exactly two.
:::

::: {#exr-group-representations-c2}
[C2: Maschke over a field of the right characteristic]

Let \( G = \nZ/2\nZ \) and \( V = F^2 \), with \( \rho([1]) = \begin{pmatrix} 0 & 1 \\ 1 & 0\end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. For \( F = \nQ \), find two \( G \)-invariant lines whose direct sum is \( V \).
2. For \( F = \nF_2 \), prove that \( V \) has exactly one non-trivial \( G \)-invariant subspace, and conclude that @thm-maschke fails here. Which hypothesis is violated?
3. For \( F = \nF_3 \), decompose \( V \) into irreducible subrepresentations.
:::
:::

::: {.solution}
(a) \( \rho([1]) \) swaps the coordinates, so \( \u = (1,1) \) and \( \w = (1,-1) \) satisfy \( \rho([1])\u = \u \) and \( \rho([1])\w = -\w \). Both lines are invariant, since \( \rho([0]) = \I_2 \) as well. The two vectors are independent, because the matrix with columns \( \u, \w \) has determinant \( -2 \ne 0 \) in \( \nQ \); hence \( \Span(\u)\cap\Span(\w) = \{\0\} \) and the sum is direct (@thm-direct-sum-criteria). Its dimension is \( 2 = \dim V \), so \( V = \Span(\u)\oplus\Span(\w) \).

(b) Over \( \nF_2 \) we have \( -1 = 1 \), so \( \w = \u = (1,1) \) and the two lines coincide. A non-trivial invariant subspace is a line \( \Span((a,b)) \) with \( (a,b) \ne (0,0) \), and invariance requires \( (b,a) = \lambda(a,b) \). Over \( \nF_2 \) the only non-zero scalar is \( \lambda = 1 \), forcing \( a = b \), so \( (a,b) = (1,1) \) and the only non-trivial invariant subspace is \( \Span((1,1)) \). A complement of a line in the plane \( V \) is again a line, and the only invariant line is \( \Span((1,1)) \) itself, which is not a complement of itself. So this invariant subspace has no invariant complement, and \( V \) is not a direct sum of irreducibles. The violated hypothesis is on the characteristic: \( \operatorname{char}\nF_2 = 2 = \lvert G\rvert \).

(c) Over \( \nF_3 \), \( -1 = 2 \ne 1 \), so \( \u = (1,1) \) and \( \w = (1,2) \) are again independent, with \( \rho([1])\u = \u \) and \( \rho([1])\w = 2\w = -\w \). Hence \( V = \Span(\u)\oplus\Span(\w) \), each summand of dimension \( 1 \) and so irreducible. Here \( \operatorname{char}\nF_3 = 3 \nmid 2 = \lvert G\rvert \), and @thm-maschke applies.
:::

::: {#exr-group-representations-c3}
[C3: The contragredient representation]

Let \( G \) be a finite group and \( \rho \) a representation of \( G \) on \( V \) over \( F \). For \( g \in G \) define \( \tau(g) \coloneqq \bigl(\rho(g)^{-1}\bigr)' \in \cL(V^{*}) \), where \( T' \) denotes the dual map (@def-dual-map).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \tau \) is a representation of \( G \) on \( V^{*} \), the **contragredient** of \( \rho \).
2. Prove that if \( U \subseteq V \) is \( G \)-invariant for \( \rho \), then its annihilator \( U^{0} \subseteq V^{*} \) (@def-annihilator) is \( G \)-invariant for \( \tau \).
3. Hence deduce that if \( \tau \) is irreducible, so is \( \rho \).
:::
:::

::: {.solution}
(a) Each \( \rho(g)^{-1} \) is invertible, so \( \tau(g) \) is invertible by @thm-dual-map-properties (d). For multiplicativity, put \( S = \rho(h)^{-1} \) and \( T = \rho(g)^{-1} \). By @thm-dual-map-properties (b),
\[
\begin{aligned}
  \tau(g)\tau(h) &= T'S' = (ST)' = \bigl(\rho(h)^{-1}\rho(g)^{-1}\bigr)' \\
  &= \bigl((\rho(g)\rho(h))^{-1}\bigr)' = \bigl(\rho(gh)^{-1}\bigr)' = \tau(gh),
\end{aligned}
\]
where the fourth equality is @thm-group-basic-properties (3) applied in \( \GL(V) \). So \( \tau \) is a homomorphism into \( \GL(V^{*}) \).

(b) Let \( \varphi \in U^{0} \), \( g \in G \) and \( \u \in U \). By @def-dual-map, \( \bigl(\tau(g)\varphi\bigr)(\u) = \varphi\bigl(\rho(g)^{-1}\u\bigr) \). Since \( \rho(g)^{-1} = \rho(g^{-1}) \) and \( U \) is \( G \)-invariant, \( \rho(g)^{-1}\u \in U \), so the value is \( 0 \). Hence \( \tau(g)\varphi \) annihilates \( U \), that is, \( \tau(g)\varphi \in U^{0} \).

(c) Suppose \( \tau \) is irreducible. Then \( V^{*} \ne \{\0\} \), so \( V \ne \{\0\} \) by @cor-dimension-dual-space. Let \( U \) be a \( G \)-invariant subspace of \( V \) with \( U \ne \{\0\} \) and \( U \ne V \). By (b), \( U^{0} \) is \( G \)-invariant, and by @thm-dimension-annihilator, \( \dim U^{0} = \dim V - \dim U \). From \( 0 < \dim U < \dim V \) we get \( 0 < \dim U^{0} < \dim V = \dim V^{*} \), so \( U^{0} \) is a non-trivial invariant subspace of \( V^{*} \), contradicting irreducibility. Hence \( \rho \) has no such \( U \), and \( \rho \) is irreducible.
:::
