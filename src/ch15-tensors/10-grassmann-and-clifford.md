# The Exterior Algebra, and Clifford at Last

The exterior powers have so far been used one degree at a time, and the wedge of two of them has had nowhere to live: \( \Lambda^2V \) and \( \Lambda^3V \) are different spaces, and until now nothing said what \( (\u \wedge \w) \wedge \x \) means as an operation. Stacking them fixes that, exactly as stacking the tensor powers produced the tensor algebra (@def-tensor-algebra) and stacking the symmetric powers produced the symmetric algebra (@def-symmetric-algebra). The result is a \( 2^n \)-dimensional algebra, and it is the last object this chapter needs. With it we can finally pay the debt Chapter 14 recorded in writing: a Clifford algebra of \( (V, q) \) exists, and its dimension is \( 2^n \).

Throughout, \( F \) is a field and \( V \) is a vector space over \( F \) with \( \dim V = n \). From the subsection on decomposability on, \( \operatorname{char} F \ne 2 \), because @def-clifford-algebra assumes it. We use the exterior powers of @def-exterior-power with their universal property for alternating maps, their bases of increasing wedges (@thm-exterior-power-basis), the test @thm-wedge-nonzero-iff-independent, and the reordering rule @lem-alternating-map-properties (b) of the previous section.

## Stacking the exterior powers

The pieces are already in place; only the multiplication is missing. The pattern is the one @prp-symmetric-product-well-defined used for symmetric powers: a product of a \( k \)-fold wedge and an \( l \)-fold wedge ought to be the \( (k+l) \)-fold wedge of all the vectors, and the only thing to check is that this depends on the two factors and not on the way each was written.

::: {#prp-wedge-product-well-defined}
[The Wedge of Two Exterior Powers]

Let \( k, l \ge 1 \). There is a **unique** bilinear map
\[
\Lambda^{k}V \times \Lambda^{l}V \to \Lambda^{k+l}V,
\qquad (\omega, \eta) \mapsto \omega \wedge \eta ,
\]
such that for all \( \u_1, \dots, \u_k, \w_1, \dots, \w_l \in V \),
\[
(\u_1 \wedge \dots \wedge \u_k) \wedge (\w_1 \wedge \dots \wedge \w_l)
= \u_1 \wedge \dots \wedge \u_k \wedge \w_1 \wedge \dots \wedge \w_l .
\]
:::

::: {.idea}
Freeze the second factor's vectors and use the universal property once, in the first \( k \) slots; that turns the left-hand factor into an element of \( \Lambda^kV \). Then let the second factor's vectors vary: what we have built depends on them \( l \)-linearly, and vanishes as soon as two of them coincide, with values in a space of linear maps, so the universal property applies a second time.
:::

::: {.proof}
Fix \( \w_1, \dots, \w_l \in V \). The map \( V^k \to \Lambda^{k+l}V \) given by
\[
(\u_1, \dots, \u_k) \mapsto \u_1 \wedge \dots \wedge \u_k \wedge \w_1 \wedge \dots \wedge \w_l
\]
is \( k \)-linear, since the wedge of \( k + l \) vectors is linear in each slot and the last \( l \) are frozen, and alternating, since a repeat among the first \( k \) arguments is a repeat among all \( k+l \). By @def-exterior-power it induces a unique linear map
\[
R(\w_1, \dots, \w_l) \colon \Lambda^{k}V \to \Lambda^{k+l}V
\]
with \( R(\w_1, \dots, \w_l)(\u_1 \wedge \dots \wedge \u_k) \) equal to the displayed wedge.

Now let the \( \w \)'s vary. The assignment \( (\w_1, \dots, \w_l) \mapsto R(\w_1, \dots, \w_l) \), with values in the vector space \( \cL(\Lambda^kV, \Lambda^{k+l}V) \), is \( l \)-linear and alternating: two linear maps on \( \Lambda^kV \) are equal as soon as they agree on the wedges \( \u_1 \wedge \dots \wedge \u_k \), which span \( \Lambda^kV \) (@thm-exterior-power-basis), and on those the required identities are the linearity and the alternation of the wedge of \( k+l \) vectors in its last \( l \) slots. So @def-exterior-power applies again and gives a unique linear map
\[
\Lambda^{l}V \to \cL(\Lambda^{k}V, \Lambda^{k+l}V),
\qquad \w_1 \wedge \dots \wedge \w_l \mapsto R(\w_1, \dots, \w_l) .
\]
Reading a linear map into a space of linear maps as a bilinear map gives the required product, with the stated values. It is unique because the wedges span both factors and a bilinear map is determined on a pair of spanning sets. This proves the proposition.
:::

With the product in hand, the algebra assembles itself.

*The exterior algebra is all the exterior powers at once, multiplied by wedging.*

::: {#def-exterior-algebra}
[Exterior Algebra]

Let \( V \) be a vector space over \( F \), with \( \Lambda^{0}V = F \) and \( \Lambda^{1}V = V \) as in @def-exterior-power. The **exterior algebra**, or **Grassmann algebra**, of \( V \) is the vector space
\[
\Lambda V \coloneqq \bigoplus_{k \ge 0} \Lambda^{k}V,
\]
whose elements are the sequences \( x = (x_0, x_1, \dots) \) with \( x_k \in \Lambda^kV \) and only finitely many \( x_k \) non-zero, with componentwise operations, and whose multiplication is
\[
(x \wedge y)_m = \sum_{k + l = m} x_k \wedge y_l ,
\]
where \( \wedge \) on the right is @prp-wedge-product-well-defined for \( k, l \ge 1 \), and is scalar multiplication when \( k = 0 \) or \( l = 0 \). We identify each \( \Lambda^kV \) with the sequences supported in position \( k \), so that \( F \) and \( V \) are subspaces of \( \Lambda V \), and call an element of \( \Lambda^kV \subseteq \Lambda V \) **homogeneous of degree \( k \)**.
:::

In words: an element of \( \Lambda V \) is a finite sum \( x_0 + x_1 + \dots + x_N \) of pieces of different degrees, the scalars sit inside as the degree-\( 0 \) piece, and **the product adds degrees**. The finiteness clause is automatic here, since \( \Lambda^kV = \{\0\} \) once \( k > n \) (@thm-exterior-power-basis).

::: {#thm-exterior-algebra-structure}
[Structure of the Exterior Algebra]

Let \( \dim V = n \) with basis \( (\e_1, \dots, \e_n) \). For a subset \( S = \{i_1 < \dots < i_k\} \subseteq [n] \) write \( \e_S = \e_{i_1} \wedge \dots \wedge \e_{i_k} \), with \( \e_\emptyset = 1 \). Then

::: {.enumerate options="label=(\alph*)"}
1. \( \Lambda V \) is an associative unital \( F \)-algebra with identity \( 1 \in \Lambda^0V = F \), and \( \Lambda^kV \wedge \Lambda^lV \subseteq \Lambda^{k+l}V \).
2. The \( 2^n \) elements \( \e_S \), one for each subset \( S \subseteq [n] \), form a basis of \( \Lambda V \). In particular \( \dim_F \Lambda V = 2^n \).
3. \( \Lambda V \) is generated as an algebra by \( 1 \) and \( V \).
:::
:::

::: {.proof}
(a) Bilinearity of the product holds componentwise, by @prp-wedge-product-well-defined. For associativity, both \( (x \wedge y) \wedge z \) and \( x \wedge (y \wedge z) \) are trilinear in \( (x, y, z) \), so it is enough to compare them on homogeneous elements, and then on the wedges of vectors, which span each \( \Lambda^kV \) for \( k \ge 1 \) (@thm-exterior-power-basis) while \( \Lambda^0V \) is spanned by \( 1 \). On those both sides are the single wedge of all the listed vectors in order, by the defining identity of @prp-wedge-product-well-defined applied twice. The scalar \( 1 \) acts on each \( \Lambda^kV \) as multiplication by \( 1 \), hence as the identity. The grading statement is built into the definition of the product.

(b) By @thm-exterior-power-basis the \( \e_S \) with \( \lvert S \rvert = k \) form a basis of \( \Lambda^kV \), and \( \Lambda^kV = \{\0\} \) for \( k > n \). A basis of a direct sum is the union of bases of the summands, so the \( \e_S \) over all \( S \subseteq [n] \) form a basis of \( \Lambda V \). Their number is \( \sum_{k=0}^{n}\binom{n}{k} = 2^n \), by the binomial theorem applied to \( (1+1)^n \).

(c) Each \( \e_S \) is a product of elements of \( V \) by the defining identity of the product, and the \( \e_S \) span by (b).
:::

The one structural fact that is not inherited from the tensor algebra is how the order of a product matters.

::: {#thm-exterior-algebra-graded-commutative}
[Graded Commutativity]

Let \( \omega \in \Lambda^kV \) and \( \eta \in \Lambda^lV \). Then
\[
\omega \wedge \eta = (-1)^{kl}\, \eta \wedge \omega .
\]
In particular \( \omega \wedge \omega = \0 \) whenever \( k \) is **odd**, over every field.
:::

::: {.idea}
Count the swaps. To turn \( \w_1 \wedge \dots \wedge \w_l \wedge \u_1 \wedge \dots \wedge \u_k \) into \( \u_1 \wedge \dots \wedge \u_k \wedge \w_1 \wedge \dots \wedge \w_l \), each of the \( k \) vectors \( \u_i \) must cross each of the \( l \) vectors \( \w_j \), and every crossing costs a sign.
:::

::: {.proof}
Both sides are bilinear in \( (\omega, \eta) \), so by @thm-exterior-power-basis it suffices to take \( \omega = \u_1 \wedge \dots \wedge \u_k \) and \( \eta = \w_1 \wedge \dots \wedge \w_l \), and the cases \( k = 0 \) or \( l = 0 \) are scalar multiplication and are clear. The permutation of \( \{1, \dots, k+l\} \) carrying the list \( (\w_1, \dots, \w_l, \u_1, \dots, \u_k) \) to \( (\u_1, \dots, \u_k, \w_1, \dots, \w_l) \) has exactly \( kl \) inversions, one for each pair consisting of a \( \u \) and a \( \w \), so its sign is \( (-1)^{kl} \) (@def-sign-permutation). By @lem-alternating-map-properties (b) the two wedges differ by that factor, which is the claim.

For the last sentence let \( k \) be odd and \( \omega \in \Lambda^kV \). Write \( \omega = \sum_S c_S\,\e_S \) in the basis of @thm-exterior-algebra-structure, the sum over the \( S \) with \( \lvert S \rvert = k \). Then
\[
\omega \wedge \omega = \sum_{S}\sum_{T} c_Sc_T\,\e_S \wedge \e_T .
\]
A term with \( S = T \) has a repeated vector, so \( \e_S \wedge \e_S = \0 \). A pair \( S \ne T \) occurs twice, and the two occurrences are \( c_Sc_T\,\e_S \wedge \e_T \) and \( c_Tc_S\,\e_T \wedge \e_S = -c_Sc_T\,\e_S \wedge \e_T \), since \( (-1)^{kl} = (-1)^{k^2} = -1 \) for odd \( k \). So the two cancel, and nothing divides by \( 2 \) anywhere.
:::

::: {.warning}
**Graded commutative is not commutative.** In \( \Lambda F^2 \) we have \( \e_1 \wedge \e_2 = -\e_2 \wedge \e_1 \), and these are different elements unless \( \operatorname{char} F = 2 \). What is true in all degrees is only the signed rule. And the sign is \( +1 \) as soon as one of the degrees is even, so an element of \( \Lambda^2V \) commutes with everything, while two elements of \( \Lambda^1V = V \) anticommute.
:::

::: {.warning}
**\( \omega \wedge \omega \) need not be zero.** The identity \( \v \wedge \v = \0 \) is a statement about degree \( 1 \). For \( \omega = \e_1 \wedge \e_2 + \e_3 \wedge \e_4 \) in \( \Lambda F^4 \), a direct expansion gives \( \omega \wedge \omega = 2\,\e_1 \wedge \e_2 \wedge \e_3 \wedge \e_4 \), which is non-zero whenever \( \operatorname{char} F \ne 2 \). Squaring to zero is the privilege of odd degree.
:::

::: {#exm-exterior-algebra-of-f3}
[The exterior algebra of a three-dimensional space]

Describe \( \Lambda F^3 \) completely, and compute \( (\e_1 + \e_2 \wedge \e_3) \wedge (\e_2 + \e_1 \wedge \e_3) \).
:::

::: {.solution}
By @thm-exterior-algebra-structure it has dimension \( 2^3 = 8 \), with basis
\[
1; \quad \e_1, \e_2, \e_3; \quad \e_{12}, \e_{13}, \e_{23}; \quad \e_{123},
\]
writing \( \e_{ij} \) for \( \e_i \wedge \e_j \) and \( \e_{123} \) for \( \e_1 \wedge \e_2 \wedge \e_3 \). The degrees have dimensions \( 1, 3, 3, 1 \). Every product of two elements of degree \( \ge 2 \) lands in degree \( \ge 4 \), hence is \( \0 \).

For the computation, expand by bilinearity into four products:
\[
\begin{aligned}
\e_1 \wedge \e_2 &= \e_{12}, \\
\e_1 \wedge (\e_1 \wedge \e_3) &= \0 \quad (\text{repeated } \e_1), \\
(\e_2 \wedge \e_3) \wedge \e_2 &= \0 \quad (\text{repeated } \e_2), \\
(\e_2 \wedge \e_3) \wedge (\e_1 \wedge \e_3) &= \0 \quad (\text{degree } 4).
\end{aligned}
\]
So the product is \( \e_{12} \), while the reversed product is \( -\e_{12} \) plus the same three zeros.
:::

::: {.check}
In \( \Lambda F^4 \), what is \( (\e_1 \wedge \e_2) \wedge (\e_2 \wedge \e_3) \), and what is \( (\e_1 \wedge \e_2) \wedge (\e_3 \wedge \e_4) \)?
:::

::: {.solution}
The first is \( \e_1 \wedge \e_2 \wedge \e_2 \wedge \e_3 = \0 \), since \( \e_2 \) is repeated. The second is \( \e_1 \wedge \e_2 \wedge \e_3 \wedge \e_4 \), a basis vector of \( \Lambda^4F^4 \), so it is non-zero. Wedging two \( 2 \)-vectors gives zero exactly when the four vectors involved are dependent.
:::

## Decomposable elements

Section 2 warned that not every element of \( V \otimes W \) is a simple tensor \( \v \otimes \w \), and proved it with \( \e_1 \otimes \e_1 + \e_2 \otimes \e_2 \) (@exm-non-simple-tensor). The same thing happens one floor up, and for the same reason: the simple objects form a low-dimensional cone inside a large space, and a sum of two of them usually escapes it.

::: {#def-decomposable}
[Decomposable Element]

Let \( k \ge 1 \). An element \( \omega \in \Lambda^kV \) is **decomposable**, or a **\( k \)-blade**, if there exist \( \v_1, \dots, \v_k \in V \) with
\[
\omega = \v_1 \wedge \v_2 \wedge \dots \wedge \v_k .
\]
:::

**Examples.** Every element of \( \Lambda^1V = V \) is decomposable, with \( k = 1 \); so is \( \0 \), being \( \v \wedge \v \wedge \v_3 \wedge \dots \wedge \v_k \); and so is every element of the line \( \Lambda^nV \), since \( c\,\e_1 \wedge \dots \wedge \e_n = (c\e_1) \wedge \e_2 \wedge \dots \wedge \e_n \).

**Why the word.** A decomposable \( \omega \ne \0 \) carries a \( k \)-dimensional subspace: its factors are independent by @thm-wedge-nonzero-iff-independent, and they span one. Non-decomposable elements are exactly those that come from no single subspace, which is why the failure below is a phenomenon and not a notational accident.

::: {#thm-non-decomposable-two-vector}
[Not Every 2-Vector Is Decomposable]

Let \( \dim V = n \ge 4 \), let \( (\e_1, \dots, \e_n) \) be a basis of \( V \), and set
\[
\omega = \e_1 \wedge \e_2 + \e_3 \wedge \e_4 \in \Lambda^{2}V .
\]
Then \( \omega \) is **not** decomposable.
:::

::: {.idea}
A decomposable \( 2 \)-vector \( \u \wedge \w \) squares to zero, because the four-fold wedge \( \u \wedge \w \wedge \u \wedge \w \) repeats a vector. So compute \( \omega \wedge \omega \) and find it non-zero. That test needs \( \operatorname{char} F \ne 2 \); the proof below takes a second route that does not, by asking which vectors annihilate \( \omega \).
:::

::: {.proof}
Suppose \( \omega = \u \wedge \w \) for some \( \u, \w \in V \). Since \( \e_1 \wedge \e_2 \) and \( \e_3 \wedge \e_4 \) are distinct basis vectors of \( \Lambda^2V \) (@thm-exterior-power-basis), \( \omega \ne \0 \), so \( (\u, \w) \) is linearly independent by @thm-wedge-nonzero-iff-independent; in particular \( \u \ne \0 \).

Consider \( \u \wedge \omega = \u \wedge \u \wedge \w = \0 \), the wedge having a repeated argument. We show this is impossible. Let \( \v = \sum_{i=1}^{n} x_i\e_i \) be any vector and compute \( \v \wedge \omega \), using bilinearity and dropping every term with a repeated basis vector:
\[
\begin{aligned}
\v \wedge \omega
= {}& x_3\,\e_3 \wedge \e_1 \wedge \e_2 + x_4\,\e_4 \wedge \e_1 \wedge \e_2 \\
&+ x_1\,\e_1 \wedge \e_3 \wedge \e_4 + x_2\,\e_2 \wedge \e_3 \wedge \e_4 \\
&+ \sum_{i \ge 5} x_i\,(\e_i \wedge \e_1 \wedge \e_2 + \e_i \wedge \e_3 \wedge \e_4).
\end{aligned}
\]
Sorting each wedge by @lem-alternating-map-properties (b) turns this into a combination of the distinct basis vectors
\[
\e_{123},\ \e_{124},\ \e_{134},\ \e_{234},\
\e_{12i},\ \e_{34i} \ (i \ge 5)
\]
of \( \Lambda^3V \), with coefficients \( x_3, x_4, x_1, x_2 \) and \( x_i, x_i \) respectively, up to signs. Since these basis vectors are distinct and the \( \e_S \) are independent (@thm-exterior-power-basis), \( \v \wedge \omega = \0 \) forces \( x_1 = x_2 = \dots = x_n = 0 \), that is, \( \v = \0 \). This contradicts \( \u \ne \0 \) with \( \u \wedge \omega = \0 \). Hence \( \omega \) is not decomposable.
:::

::: {.remark}
When \( \operatorname{char} F \ne 2 \) there is a one-line version: \( \omega \wedge \omega = 2\,\e_1 \wedge \e_2 \wedge \e_3 \wedge \e_4 \ne \0 \), whereas \( (\u \wedge \w) \wedge (\u \wedge \w) = \0 \) always. The proof above was written to avoid that division, because the test fails over \( \nF_2 \) — see the warning next.
:::

::: {.warning}
**The square test is blind in characteristic \( 2 \).** Over \( \nF_2 \) every \( \omega \in \Lambda^2V \) satisfies \( \omega \wedge \omega = \0 \): in the expansion \( \sum_{S,T}c_Sc_T\,\e_S \wedge \e_T \) the diagonal terms vanish and each off-diagonal pair contributes \( 2c_Sc_T\,\e_S \wedge \e_T = \0 \). So over \( \nF_2 \) the vanishing of \( \omega \wedge \omega \) says nothing at all, while \( \e_1 \wedge \e_2 + \e_3 \wedge \e_4 \) is still not decomposable, by the proof above. A criterion and a phenomenon are different things.
:::

::: {.check}
Why does @thm-non-decomposable-two-vector need \( n \ge 4 \)? Show that every element of \( \Lambda^2V \) is decomposable when \( \dim V = 3 \).
:::

::: {.solution}
With \( n \le 3 \) there is no room to write \( \e_1 \wedge \e_2 + \e_3 \wedge \e_4 \) at all. For \( n = 3 \), take \( \omega = a\,\e_{12} + b\,\e_{13} + c\,\e_{23} \). If \( a = b = c = 0 \) then \( \omega = \0 \), which is decomposable. If \( a \ne 0 \), then
\[
\Bigl(\e_1 - \tfrac{c}{a}\e_3\Bigr) \wedge (a\e_2 + b\e_3)
= a\,\e_{12} + b\,\e_{13} + c\,\e_{23} = \omega ,
\]
using \( \e_3 \wedge \e_2 = -\e_{23} \). If \( a = 0 \), relabel the basis so that the surviving non-zero coefficient sits in the first slot and repeat. So the phenomenon starts exactly at \( n = 4 \).
:::

Together with @exm-non-simple-tensor this is the chapter's negative result, stated in its two forms: a general tensor is not a simple tensor, and a general \( k \)-vector is not a blade. The optimistic reading — that every element of a space built from \( V \) is built from finitely many vectors of \( V \) in the obvious way — is false in both places, and Section 11 will find the first form of it wearing a physical name.

## Algebras modulo relations

One tool is still missing. The Clifford algebra is to be built by imposing relations on \( \operatorname{T}(V) \), and imposing relations on an **algebra** means dividing by more than a subspace: the relations must stay relations after multiplication on either side. Chapter 6 met the commutative version of the idea for \( F[x] \) (@def-ideal-polynomials).

::: {#def-two-sided-ideal}
[Two-Sided Ideal, and the Ideal Generated by a Set]

Let \( A \) be an \( F \)-algebra (@def-algebra-over-field). A **two-sided ideal** of \( A \) is a subspace \( \cI \subseteq A \) such that \( yx \in \cI \) and \( xy \in \cI \) for **every** \( x \in \cI \) and **every** \( y \in A \). For a subset \( S \subseteq A \), the **ideal generated by \( S \)** is
\[
\langle S \rangle \coloneqq \Span\{\, y s z \;:\; y, z \in A,\ s \in S \,\} .
\]
:::

**Examples.** In \( F[x] \) the ideals are the sets \( \langle p \rangle \) of @def-ideal-polynomials; in any \( A \), both \( \{0\} \) and \( A \) are ideals. **Non-example by minimal change.** The diagonal matrices in \( M_2(F) \) form a subspace closed under multiplication, but not an ideal: it contains \( \E_{11} \), while \( \E_{21}\E_{11} = \E_{21} \) is not diagonal. Being closed among one's own elements is not the condition; absorbing products with the **whole** algebra is.

The span above is a subspace by construction, and it is a two-sided ideal because \( a(ysz) = (ay)sz \) and \( (ysz)a = ys(za) \) are again of the listed form. It contains \( S \), taking \( y = z = 1_A \), and every two-sided ideal containing \( S \) contains each \( ysz \); so \( \langle S \rangle \) is the smallest two-sided ideal containing \( S \), which is what "generated" means.

::: {#lem-quotient-algebra}
[Quotient of an Algebra by an Ideal]

Let \( A \) be an \( F \)-algebra and \( \cI \) a two-sided ideal of \( A \).

::: {.enumerate options="label=(\alph*)"}
1. The quotient space \( A/\cI \) carries exactly one multiplication making the quotient map \( \pi \colon A \to A/\cI \) an algebra homomorphism, namely \( (x + \cI)(y + \cI) = xy + \cI \); with it \( A/\cI \) is an \( F \)-algebra with identity \( 1_A + \cI \), and \( \ker \pi = \cI \).
2. If \( \varphi \colon A \to B \) is an algebra homomorphism with \( \cI \subseteq \ker\varphi \), then there is exactly one algebra homomorphism \( \bar\varphi \colon A/\cI \to B \) with \( \bar\varphi \circ \pi = \varphi \).
3. The kernel of any algebra homomorphism is a two-sided ideal.
:::
:::

::: {.proof}
(a) The rule is well defined: if \( x' = x + u \) and \( y' = y + w \) with \( u, w \in \cI \), then
\[
x'y' = xy + uy + xw + uw \in xy + \cI ,
\]
since \( \cI \) absorbs multiplication on both sides and is closed under addition. Bilinearity, associativity and the identity are then inherited from \( A \), because each is an identity among cosets that follows by applying \( \pi \) to the corresponding identity in \( A \). Any multiplication making \( \pi \) multiplicative must satisfy the displayed rule, and \( \pi \) is surjective, so the multiplication is unique. Finally \( \ker \pi = \cI \) by @lem-coset-equality.

(b) Since \( \varphi \) is linear with \( \cI \subseteq \ker\varphi \), @thm-quotient-universal-property (a) gives exactly one **linear** \( \bar\varphi \) with \( \bar\varphi\pi = \varphi \). It is multiplicative: every element of \( A/\cI \) is \( \pi(x) \) for some \( x \), and
\[
\bar\varphi(\pi(x)\pi(y)) = \bar\varphi(\pi(xy)) = \varphi(xy) = \varphi(x)\varphi(y),
\]
which is \( \bar\varphi(\pi(x))\,\bar\varphi(\pi(y)) \). Also \( \bar\varphi(\pi(1_A)) = \varphi(1_A) = 1_B \). Uniqueness is already contained in the uniqueness of the linear map.

(c) If \( \varphi(x) = 0 \) and \( y \in A \), then \( \varphi(xy) = \varphi(x)\varphi(y) = 0 \) and \( \varphi(yx) = 0 \); and \( \ker\varphi \) is a subspace because \( \varphi \) is linear.
:::

## The Clifford algebra, constructed

Chapter 14 §12 defined a Clifford algebra of \( (V, q) \) as a pair \( (C, \iota) \) with \( \iota \colon V \to C \) linear satisfying

- (C1) \( \iota(\v)^2 = q(\v)1_C \) for every \( \v \in V \), and
- (C2) the universal property: every linear \( f \colon V \to A \) into an \( F \)-algebra with \( f(\v)^2 = q(\v)1_A \) factors as \( f = \bar f \circ \iota \) for a unique algebra homomorphism \( \bar f \),

and then said in as many words that it could not produce one: "The definition says what a Clifford algebra would be; it does not produce one." What it needed was an algebra of formal strings of vectors, which is now @def-tensor-algebra, and a way to impose the relation \( \v \otimes \v = q(\v)1 \), which is now @lem-quotient-algebra.

::: {#thm-clifford-exists}
[Existence of the Clifford Algebra]

Let \( F \) be a field with \( \operatorname{char} F \ne 2 \), let \( V \) be a finite-dimensional \( F \)-vector space, let \( \beta \) be a symmetric bilinear form on \( V \) and \( q(\v) = \beta(\v,\v) \). Let
\[
\cI_q \coloneqq \bigl\langle\, \v \otimes \v - q(\v)1 \;:\; \v \in V \,\bigr\rangle
\subseteq \operatorname{T}(V)
\]
be the two-sided ideal generated by these elements, put \( \operatorname{Cl}(q) \coloneqq \operatorname{T}(V)/\cI_q \), and let \( \iota \colon V \to \operatorname{Cl}(q) \) be the restriction to \( V \subseteq \operatorname{T}(V) \) of the quotient map \( \pi \). Then \( (\operatorname{Cl}(q), \iota) \) is a Clifford algebra of \( (V, q) \) in the sense of @def-clifford-algebra.

In particular a Clifford algebra exists for every \( (V, q) \), and by @prp-clifford-uniqueness any two are isomorphic by a unique isomorphism compatible with the structure maps.
:::

::: {.idea}
The tensor algebra is the free associative algebra on \( V \): a linear map out of \( V \) extends uniquely to it (@thm-tensor-algebra-universal), with no relations in the way. Dividing by the smallest ideal containing \( \v \otimes \v - q(\v)1 \) imposes exactly the relation (C1) and nothing else, and "nothing else" is precisely what the universal property (C2) asserts.
:::

::: {.proof}
By @lem-quotient-algebra (a), \( \operatorname{Cl}(q) \) is an \( F \)-algebra and \( \pi \) is a surjective algebra homomorphism with \( \ker\pi = \cI_q \). The map \( \iota = \pi|_V \) is linear, being a restriction of a linear map.

**(C1).** Let \( \v \in V \). In \( \operatorname{T}(V) \) the product of \( \v \) with itself is \( \v \otimes \v \) (@def-tensor-algebra), and \( \v \otimes \v - q(\v)1 \) is a generator of \( \cI_q = \ker\pi \). Since \( \pi \) is multiplicative and linear,
\[
\iota(\v)^2 = \pi(\v)\pi(\v) = \pi(\v \otimes \v) = \pi\bigl(q(\v)1\bigr) = q(\v)1_{\operatorname{Cl}(q)} .
\]

**(C2).** Let \( A \) be an \( F \)-algebra and let \( f \colon V \to A \) be linear with \( f(\v)^2 = q(\v)1_A \) for every \( \v \in V \). By @thm-tensor-algebra-universal there is a unique algebra homomorphism \( \tilde f \colon \operatorname{T}(V) \to A \) with \( \tilde f|_V = f \). For every \( \v \in V \),
\[
\tilde f\bigl(\v \otimes \v - q(\v)1\bigr) = f(\v)f(\v) - q(\v)1_A = 0 ,
\]
so \( \ker\tilde f \) contains every generator of \( \cI_q \). By @lem-quotient-algebra (c), \( \ker\tilde f \) is a two-sided ideal, and \( \cI_q \) is the **smallest** one containing those generators (@def-two-sided-ideal), so \( \cI_q \subseteq \ker\tilde f \). By @lem-quotient-algebra (b) there is exactly one algebra homomorphism \( \bar f \colon \operatorname{Cl}(q) \to A \) with \( \bar f \circ \pi = \tilde f \), and restricting to \( V \) gives \( \bar f \circ \iota = \tilde f|_V = f \).

For the uniqueness clause of (C2), let \( g \colon \operatorname{Cl}(q) \to A \) be any algebra homomorphism with \( g \circ \iota = f \). Then \( g \circ \pi \) is an algebra homomorphism \( \operatorname{T}(V) \to A \) whose restriction to \( V \) is \( g\iota = f \), so \( g\pi = \tilde f \) by the uniqueness clause of @thm-tensor-algebra-universal. Hence \( g\pi = \bar f\pi \), and \( \pi \) is surjective, so \( g = \bar f \). This proves the theorem.
:::

::: {.remark}
Neither \( \operatorname{char} F \ne 2 \) nor finite dimension was used in this proof; the construction and both checks work for any \( V \) and any quadratic form. The hypotheses are carried because @def-clifford-algebra states them, and because the dimension count below needs an orthogonal basis.
:::

## The dimension, at last

Chapter 14 proved half of the count. Its @prp-clifford-spanning showed that for an orthogonal basis \( (\e_1, \dots, \e_n) \) of \( \beta \) the \( 2^n \) **sorted products**
\[
\iota(\e_{i_1})\iota(\e_{i_2})\cdots\iota(\e_{i_k}),
\qquad i_1 < i_2 < \dots < i_k ,
\]
span \( C \), so that \( \dim_F C \le 2^n \). The other half — their independence — is what this section owes. The idea is to make \( \Lambda V \), which has exactly the right dimension, into a place where the vectors of \( V \) act with square \( q(\v) \); the universal property then sends \( C \) into the operators on \( \Lambda V \), and evaluating at \( 1 \) turns the sorted products into distinct basis vectors.

Two families of operators on \( \Lambda V \) do the work: wedging a basis vector on, and deleting it again.

::: {#lem-clifford-operators}
[Creation and Deletion Operators]

Let \( (\e_1, \dots, \e_n) \) be a basis of \( V \), and for \( S \subseteq [n] \) let \( \e_S \) be as in @thm-exterior-algebra-structure. For \( i \in [n] \) write \( \sigma(i, S) = \lvert \{ j \in S : j < i \} \rvert \). Let \( E_i \in \cL(\Lambda V) \) be left multiplication by \( \e_i \), that is, \( E_i(\omega) = \e_i \wedge \omega \), and let \( D_i \in \cL(\Lambda V) \) be the unique linear map with
\[
D_i(\e_S) =
\begin{cases}
(-1)^{\sigma(i,S)}\,\e_{S \setminus \{i\}}, & i \in S, \\
\0, & i \notin S ,
\end{cases}
\]
which exists and is unique because the \( \e_S \) form a basis (@thm-exterior-algebra-structure). Then for all \( i, j \in [n] \),
\[
\begin{aligned}
E_iE_j + E_jE_i &= 0, \\
D_iD_j + D_jD_i &= 0, \\
D_iE_j + E_jD_i &= \delta_{ij}\,\id_{\Lambda V} .
\end{aligned}
\]
:::

::: {.idea}
\( E_i \) inserts the index \( i \) into the set \( S \) and \( D_i \) removes it, each at the cost of the sign needed to move \( \e_i \) past the smaller members of \( S \). All three identities are then a comparison of two signs, and in the third the two cases "\( i \in S \)" and "\( i \notin S \)" are exactly the two ways the identity can be satisfied: one term is zero and the other is \( \e_S \).
:::

::: {.proof}
First record what \( E_i \) does on the basis. If \( i \in S \) then \( \e_i \wedge \e_S \) repeats \( \e_i \) and is \( \0 \). If \( i \notin S \), then sorting \( \e_i \wedge \e_S \) moves \( \e_i \) past the \( \sigma(i,S) \) members of \( S \) smaller than \( i \), so by @lem-alternating-map-properties (b)
\[
E_i(\e_S) = (-1)^{\sigma(i,S)}\,\e_{S \cup \{i\}} .
\]

**First identity.** For every \( \omega \in \Lambda V \), \( E_iE_j(\omega) = \e_i \wedge \e_j \wedge \omega \) and \( E_jE_i(\omega) = \e_j \wedge \e_i \wedge \omega \), and \( \e_j \wedge \e_i = -\e_i \wedge \e_j \) by @thm-exterior-algebra-graded-commutative. Adding gives \( 0 \). (For \( i = j \) each term is separately \( 0 \).)

**Third identity, case \( i = j \).** If \( i \notin S \), then \( D_i(\e_S) = \0 \) and \( E_i(\e_S) = (-1)^{\sigma(i,S)}\e_{S \cup \{i\}} \); since \( \sigma(i, S \cup \{i\}) = \sigma(i,S) \), applying \( D_i \) returns \( (-1)^{2\sigma(i,S)}\e_S = \e_S \). If \( i \in S \), then \( E_i(\e_S) = \0 \) and \( D_i(\e_S) = (-1)^{\sigma(i,S)}\e_{S \setminus \{i\}} \); since \( \sigma(i, S \setminus \{i\}) = \sigma(i,S) \), applying \( E_i \) returns \( \e_S \). Either way the sum is \( \e_S \).

**Third identity, case \( i \ne j \).** If \( j \in S \) then \( E_j(\e_S) = \0 \), and \( D_i(\e_S) \) is either \( \0 \) or a multiple of \( \e_{S \setminus \{i\}} \), which still contains \( j \), so \( E_j \) kills it; both terms vanish. If \( j \notin S \) and \( i \notin S \) then \( D_i(\e_S) = \0 \) and \( D_i(\e_{S \cup \{j\}}) = \0 \) as well, since \( i \ne j \); again both terms vanish. So let \( j \notin S \) and \( i \in S \). Then
\[
\begin{aligned}
D_iE_j(\e_S) &= (-1)^{\sigma(j,S) + \sigma(i, S \cup \{j\})}\, \e_{(S \cup \{j\}) \setminus \{i\}}, \\
E_jD_i(\e_S) &= (-1)^{\sigma(i,S) + \sigma(j, S \setminus \{i\})}\, \e_{(S \setminus \{i\}) \cup \{j\}},
\end{aligned}
\]
and the two index sets agree. Now \( \sigma(i, S \cup \{j\}) = \sigma(i,S) + [\,j < i\,] \) and \( \sigma(j, S \setminus \{i\}) = \sigma(j,S) - [\,i < j\,] \), writing \( [\,P\,] \) for \( 1 \) if \( P \) holds and \( 0 \) otherwise. So the two exponents differ by \( [\,j<i\,] + [\,i<j\,] = 1 \), which is odd because \( i \ne j \). The two terms therefore cancel.

**Second identity.** Both \( D_iD_j(\e_S) \) and \( D_jD_i(\e_S) \) vanish unless \( i, j \in S \) and \( i \ne j \), and in that case they are \( (-1)^{\sigma(j,S)+\sigma(i, S \setminus \{j\})} \) and \( (-1)^{\sigma(i,S)+\sigma(j, S \setminus \{i\})} \) times the same \( \e_{S \setminus \{i,j\}} \). The same two identities for \( \sigma \) show the exponents differ by an odd number, so the terms cancel. For \( i = j \), \( D_i^2(\e_S) = \0 \) because \( i \notin S \setminus \{i\} \). This proves the lemma.
:::

::: {#thm-clifford-dimension-proved}
[Dimension of a Clifford Algebra]

Let \( F \) be a field with \( \operatorname{char} F \ne 2 \), let \( \dim V = n \), let \( \beta \) be a symmetric bilinear form on \( V \) with quadratic form \( q \), and let \( (C, \iota) \) be a Clifford algebra of \( (V, q) \). Let \( (\e_1, \dots, \e_n) \) be an orthogonal basis of \( V \) for \( \beta \). Then the \( 2^n \) sorted products of @prp-clifford-spanning form a **basis** of \( C \). Consequently
\[
\dim_F C = 2^n,
\]
the map \( \iota \) is injective, and \( C \) is isomorphic to \( \Lambda V \) **as a vector space**. This is @thm-clifford-dimension.
:::

::: {.idea}
Build a representation. ① Turn each basis vector \( \e_i \) into the operator \( c_i = E_i + d_iD_i \) on \( \Lambda V \), where \( d_i = q(\e_i) \); @lem-clifford-operators makes these anticommute and gives \( c_i^2 = d_i\,\id \), which is exactly (C1). ② The universal property then hands us an algebra homomorphism \( C \to \cL(\Lambda V) \). ③ Evaluate at the element \( 1 \in \Lambda^0V \): the sorted product for the index set \( S \) is sent to \( \e_S \), because at each step the new index is smaller than all the ones already there, so the deletion half contributes nothing. Distinct basis vectors come out, so the sorted products were independent.
:::

::: {.proof}
An orthogonal basis exists by @thm-symmetric-form-diagonalizable, since \( \operatorname{char} F \ne 2 \). Write \( d_i = q(\e_i) \) and \( c_i = E_i + d_iD_i \in \cL(\Lambda V) \), with \( E_i, D_i \) as in @lem-clifford-operators. By @prp-clifford-spanning the sorted products span \( C \) and \( \dim_F C \le 2^n \), so only independence is left.

**Step 1: the \( c_i \) satisfy the Clifford relations.** Expanding the product and collecting the four brackets,
\[
\begin{aligned}
c_ic_j + c_jc_i = {}& (E_iE_j + E_jE_i) + d_j(E_iD_j + D_jE_i) \\
&+ d_i(D_iE_j + E_jD_i) + d_id_j(D_iD_j + D_jD_i) .
\end{aligned}
\]
By @lem-clifford-operators the first and last brackets are \( 0 \) and each middle bracket is \( \delta_{ij}\id \). So \( c_ic_j = -c_jc_i \) for \( i \ne j \). Setting \( i = j \) in the display would give \( 2c_i^2 \), so expand \( c_i^2 \) directly instead; with \( E_i^2 = D_i^2 = 0 \), which were checked separately in the lemma,
\[
c_i^2 = E_i^2 + d_i(E_iD_i + D_iE_i) + d_i^2D_i^2 = d_i\,\id ,
\]
with no division by \( 2 \) anywhere.
Now \( \cL(\Lambda V) \) is an \( F \)-algebra under composition (@def-algebra-over-field). Let \( f \colon V \to \cL(\Lambda V) \) be the linear map with \( f(\e_i) = c_i \), which exists and is unique by @thm-linear-map-from-any-basis. For \( \v = \sum_i x_i\e_i \),
\[
f(\v)^2 = \sum_{i} x_i^2 c_i^2 + \sum_{i < j} x_ix_j(c_ic_j + c_jc_i)
= \Bigl(\sum_i d_ix_i^2\Bigr)\id ,
\]
the cross terms vanishing because \( i \ne j \) there. Since the basis is orthogonal, \( \beta(\e_i, \e_j) = 0 \) for \( i \ne j \), so \( q(\v) = \beta(\v,\v) = \sum_i d_ix_i^2 \). Hence \( f(\v)^2 = q(\v)\,\id \), which is (C1) for \( f \).

**Step 2: the induced homomorphism.** By the universal property (C2) of @def-clifford-algebra there is an algebra homomorphism \( \Psi \colon C \to \cL(\Lambda V) \) with \( \Psi\iota = f \). Define the linear map
\[
\Phi \colon C \to \Lambda V,
\qquad \Phi(x) = \Psi(x)(1),
\]
where \( 1 \in \Lambda^0V = F \subseteq \Lambda V \). It is linear because \( \Psi \) is linear and evaluation at a fixed element is linear.

**Step 3: \( \Phi \) sends sorted products to basis vectors.** Let \( S = \{i_1 < \dots < i_k\} \subseteq [n] \). Since \( \Psi \) is multiplicative and \( \Psi\iota = f \),
\[
\Psi\bigl(\iota(\e_{i_1})\cdots\iota(\e_{i_k})\bigr) = c_{i_1}c_{i_2}\cdots c_{i_k} .
\]
We claim \( c_{i_r}c_{i_{r+1}}\cdots c_{i_k}(1) = \e_{T_r} \) with \( T_r = \{i_r, \dots, i_k\} \), by downward induction on \( r \). For \( r = k+1 \) the product is empty and the value is \( 1 = \e_\emptyset \). Assume the claim for \( r+1 \). Because \( i_r < i_{r+1} \) and the indices increase, \( i_r \notin T_{r+1} \), so \( D_{i_r}(\e_{T_{r+1}}) = \0 \); and \( i_r \) is smaller than every element of \( T_{r+1} \), so \( \sigma(i_r, T_{r+1}) = 0 \) and \( E_{i_r}(\e_{T_{r+1}}) = \e_{T_r} \). Hence \( c_{i_r}(\e_{T_{r+1}}) = \e_{T_r} \), completing the induction. Taking \( r = 1 \),
\[
\Phi\bigl(\iota(\e_{i_1})\cdots\iota(\e_{i_k})\bigr) = \e_S ,
\]
and for \( S = \emptyset \), \( \Phi(1_C) = \id(1) = 1 = \e_\emptyset \).

**Step 4: conclusion.** Suppose a linear combination of the sorted products is \( 0 \). Applying \( \Phi \) gives the same combination of the \( \e_S \), which are linearly independent by @thm-exterior-algebra-structure (b); so all coefficients vanish. The sorted products are therefore linearly independent, and being also a spanning list they form a basis of \( C \), of size \( 2^n \). Thus \( \dim_F C = 2^n \).

Since \( 1_C \) and \( \iota(\e_1), \dots, \iota(\e_n) \) are among the basis elements just found, the list \( (\iota(\e_1), \dots, \iota(\e_n)) \) is independent, so \( \iota \) carries a basis of \( V \) to an independent list and is injective. Finally \( \Phi \) carries the basis of \( C \) bijectively onto the basis \( (\e_S) \) of \( \Lambda V \), so \( \Phi \) is a vector space isomorphism. This proves the theorem.
:::

**The debt, and how it was paid.** Chapter 14 §12 stated @thm-clifford-dimension and then wrote, under the heading "What is proved here, and what is not", that the inequality \( \dim_F C \le 2^n \) was proved in full, while "the reverse inequality — that the \( 2^n \) sorted products are linearly independent — is **not proved in this section**", and that the two halves would have to be established together by exhibiting one algebra of dimension exactly \( 2^n \) satisfying (C1) and (C2). Both halves are now supplied. The missing one was independence, and @thm-clifford-dimension-proved supplies it; the prior question, whether any Clifford algebra exists at all, is @thm-clifford-exists. Chapter 14 read the statement for \( n \ge 3 \) "as quoted from Chapter 15 and not as proved here"; it may now be read as proved.

The prediction was right in substance and slightly off in shape. The algebra of dimension \( 2^n \) that settled the matter is the exterior algebra, but it is not the Clifford algebra: it is only a space that \( \operatorname{Cl}(q) \) acts on, and independence came from the action rather than from an identification. Chapter 14 also guessed that "\( \operatorname{Cl}(q) \) is assembled from the exterior powers \( \Lambda^kV \), one for each \( k \)", and \( \Phi \) is that assembly, matching the sorted product on \( S \) with the wedge \( \e_S \).

::: {.warning}
**\( \operatorname{Cl}(q) \) and \( \Lambda V \) are the same size, not the same algebra.** The map \( \Phi \) above is an isomorphism of **vector spaces** only. It is not multiplicative, and no other map is either, unless \( q = 0 \): in \( \Lambda V \) the square of a vector is \( \0 \), while in \( \operatorname{Cl}(q) \) it is \( q(\v)1 \). Writing an element of \( \operatorname{Cl}(q) \) as a sum of wedges is a choice of coordinates, not a description of the multiplication.
:::

That warning deserves a proof rather than a slogan.

::: {#prp-clifford-versus-exterior}
[Comparing the Two Algebras]

Let \( \operatorname{char} F \ne 2 \) and \( \dim V = n \ge 1 \), and let \( q \) be the quadratic form of a symmetric bilinear form on \( V \).

::: {.enumerate options="label=(\alph*)"}
1. If \( q = 0 \), then \( \operatorname{Cl}(0) \) and \( \Lambda V \) are isomorphic as \( F \)-algebras.
2. If \( q \ne 0 \), they are **not** isomorphic as \( F \)-algebras, although they are isomorphic as vector spaces.
:::
:::

::: {.idea}
For (b), find a property of \( \Lambda V \) that \( \operatorname{Cl}(q) \) fails. In \( \Lambda V \) everything of positive degree is nilpotent, so an element whose square is a **non-zero scalar** can have no positive-degree part at all; but in \( \operatorname{Cl}(q) \) a vector \( \v \) with \( q(\v) \ne 0 \) squares to a non-zero scalar and is not a scalar itself.
:::

::: {.proof}
(a) Let \( q = 0 \) and let \( j \colon V \to \Lambda V \) be the inclusion \( V = \Lambda^1V \subseteq \Lambda V \). Then \( j(\v)^2 = \v \wedge \v = \0 = q(\v)1 \), so (C1) holds for \( j \). By the universal property (C2) of \( \operatorname{Cl}(0) \) there is an algebra homomorphism \( \psi \colon \operatorname{Cl}(0) \to \Lambda V \) with \( \psi\iota = j \). Its image is a subalgebra containing \( 1 \) and \( V \), hence all of \( \Lambda V \) by @thm-exterior-algebra-structure (c); so \( \psi \) is surjective. Both spaces have dimension \( 2^n \), by @thm-clifford-dimension-proved and @thm-exterior-algebra-structure (b), so \( \psi \) is bijective and is an algebra isomorphism.

(b) *Claim.* If \( x \in \Lambda V \) and \( x \wedge x = a\cdot 1 \) with \( a \in F \), \( a \ne 0 \), then \( x \in F\cdot 1 \).

*Proof of claim.* Throughout, \( y^t \) means the \( t \)-fold wedge product of \( y \) with itself. Write \( x = x_0 + m \) with \( x_0 \in \Lambda^0V = F \) and \( m \) the sum of the components of positive degree. Then
\[
x \wedge x = x_0^2 + 2x_0m + m \wedge m ,
\]
and the only degree-\( 0 \) term is \( x_0^2 \), so \( x_0^2 = a \ne 0 \) and hence \( x_0 \ne 0 \). Canceling that term leaves
\[
m \wedge (2x_0\cdot 1 + m) = \0 .
\]
Every product of \( n+1 \) elements of positive degree lies in \( \bigoplus_{k > n}\Lambda^kV = \{\0\} \), so \( m^{n+1} = \0 \). Put \( c = 2x_0 \), which is non-zero because \( \operatorname{char} F \ne 2 \) and \( x_0 \ne 0 \), and \( u = -c^{-1}m \), so that \( u^{n+1} = \0 \) and \( c\cdot 1 + m = c(1 - u) \). Then
\[
(1 - u) \wedge (1 + u + u^2 + \dots + u^{n}) = 1 - u^{n+1} = 1 ,
\]
and likewise in the other order, so \( c\cdot1 + m \) is invertible. Multiplying \( m \wedge (c\cdot 1 + m) = \0 \) by its inverse gives \( m = \0 \), so \( x = x_0 \in F\cdot 1 \), proving the claim.

Now suppose \( q \ne 0 \) and let \( \varphi \colon \operatorname{Cl}(q) \to \Lambda V \) be an algebra isomorphism. Choose \( \v \in V \) with \( q(\v) \ne 0 \) and put \( x = \varphi(\iota(\v)) \). Then
\[
x \wedge x = \varphi\bigl(\iota(\v)^2\bigr) = \varphi\bigl(q(\v)1\bigr) = q(\v)\cdot 1 ,
\]
a non-zero scalar, so \( x \in F\cdot 1 \) by the claim, say \( x = c\cdot 1 = \varphi(c\,1_{\operatorname{Cl}(q)}) \). Since \( \varphi \) is injective, \( \iota(\v) = c\,1_{\operatorname{Cl}(q)} \). But by @thm-clifford-dimension-proved the elements \( 1_{\operatorname{Cl}(q)}, \iota(\e_1), \dots, \iota(\e_n) \) are part of a basis of \( \operatorname{Cl}(q) \), and \( \iota(\v) \) is a combination of \( \iota(\e_1), \dots, \iota(\e_n) \) alone; comparing coordinates forces \( c = 0 \) and \( \iota(\v) = 0 \), contradicting \( \iota(\v)^2 = q(\v)1 \ne 0 \). So no such \( \varphi \) exists. The vector space isomorphism is @thm-clifford-dimension-proved.
:::

The dimension count also makes Clifford algebras easy to recognize, which is how one identifies them in practice.

::: {#cor-clifford-recognition}
[Recognizing a Clifford Algebra]

Let \( \operatorname{char} F \ne 2 \), \( \dim V = n \), and let \( q \) be as above. Let \( A \) be an \( F \)-algebra with \( \dim_F A = 2^n \), and let \( \iota_A \colon V \to A \) be linear with \( \iota_A(\v)^2 = q(\v)1_A \) for every \( \v \in V \). If \( A \) is generated as an algebra by \( 1_A \) and \( \iota_A(V) \), then \( (A, \iota_A) \) is a Clifford algebra of \( (V, q) \).
:::

::: {.proof}
Let \( (C, \iota) \) be the Clifford algebra of @thm-clifford-exists. By its universal property there is an algebra homomorphism \( \psi \colon C \to A \) with \( \psi\iota = \iota_A \). Its image is a subalgebra of \( A \) containing \( 1_A \) and \( \iota_A(V) \), hence is all of \( A \) by the generation hypothesis. So \( \psi \) is surjective, and \( \dim_F C = 2^n = \dim_F A \) by @thm-clifford-dimension-proved, so \( \psi \) is an isomorphism.

It remains to transport (C2). Let \( f \colon V \to B \) be linear with \( f(\v)^2 = q(\v)1_B \). Then \( \bar f\psi^{-1} \colon A \to B \) is an algebra homomorphism with \( \bar f\psi^{-1}\iota_A = \bar f\iota = f \), where \( \bar f \colon C \to B \) comes from (C2) for \( C \); and if \( g \colon A \to B \) is another one, then \( g\psi \colon C \to B \) satisfies \( g\psi\iota = g\iota_A = f \), so \( g\psi = \bar f \) by uniqueness for \( C \), whence \( g = \bar f\psi^{-1} \).
:::

::: {#exm-clifford-plane}
[The Clifford algebra of the Euclidean plane]

Let \( V = \nR^2 \) with \( q(\x) = x_1^2 + x_2^2 \), the form of signature \( (2,0) \). Show that \( \operatorname{Cl}_{2,0}(\nR) \cong M_2(\nR) \).
:::

::: {.solution}
Put
\[
\A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix},
\qquad
\B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
\]
in \( M_2(\nR) \), and let \( \iota(\x) = x_1\A + x_2\B \), a linear map \( \nR^2 \to M_2(\nR) \). Multiplying out, \( \A^2 = \B^2 = \I_2 \) and \( \A\B = -\B\A \), the products being \( \begin{psmallmatrix} 0 & 1 \\ -1 & 0\end{psmallmatrix} \) and its negative. Hence
\[
\iota(\x)^2 = x_1^2\A^2 + x_1x_2(\A\B + \B\A) + x_2^2\B^2
= q(\x)\I_2 ,
\]
which is (C1). Next, \( \dim_{\nR}M_2(\nR) = 4 = 2^2 \), and the four matrices \( \I_2, \A, \B, \A\B \) are linearly independent: the first two span the diagonal matrices and the last two span the off-diagonal ones, and the diagonal and off-diagonal matrices meet only in \( 0 \). So they are a basis, and \( M_2(\nR) \) is generated by \( \I_2 \) and \( \iota(\nR^2) \). By @cor-clifford-recognition, \( (M_2(\nR), \iota) \) is a Clifford algebra of \( (\nR^2, q) \), so \( \operatorname{Cl}_{2,0}(\nR) \cong M_2(\nR) \).

Compare Chapter 14's \( \operatorname{Cl}_{0,2}(\nR) = \nH \) (@exm-clifford-quaternions). All three of \( \nH \), \( M_2(\nR) \) and \( \Lambda\nR^2 \) have dimension \( 4 \), and no two are isomorphic: \( \nH \) has no zero divisors, \( M_2(\nR) \) has plenty, and \( \Lambda\nR^2 \) differs from both by @prp-clifford-versus-exterior (b). Changing a sign in \( q \) changes the algebra completely and never changes its size.
:::

::: {.check}
Where in the proof of @thm-clifford-dimension-proved is the hypothesis \( \operatorname{char} F \ne 2 \) used?
:::

::: {.solution}
Twice, both times through the orthogonal basis. It is needed to produce one at all: @thm-symmetric-form-diagonalizable assumes \( \operatorname{char} F \ne 2 \). And it is needed for Chapter 14's @prp-clifford-spanning, which supplies the spanning half, since that proof uses @lem-clifford-anticommutation, which comes from polarization. The operator identities of @lem-clifford-operators and the induction of Step 3 use no such hypothesis.
:::

With that, Chapter 14's last open statement is closed and the construction side of this chapter is complete. The final section spends the machinery on one application, where the failure of decomposability proved above reappears under another name.

## Exercises

### A. Check your understanding

:::: {#exr-grassmann-and-clifford-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the exterior algebra \( \Lambda V \) and state its dimension when \( \dim V = n \).
2. State the graded commutativity rule, and say what it gives when both degrees are odd.
3. Define what it means for \( \omega \in \Lambda^kV \) to be decomposable, and give one decomposable and one non-decomposable element of \( \Lambda^2F^4 \).
4. Which half of @thm-clifford-dimension was left unproved in Chapter 14, and which result of this section supplies it?
5. True or false: \( \operatorname{Cl}(q) \) and \( \Lambda V \) are isomorphic algebras. Justify your answer.
:::
::::

::: {.solution}
(a) \( \Lambda V = \bigoplus_{k \ge 0}\Lambda^kV \) with the product of @prp-wedge-product-well-defined extended by bilinearity (@def-exterior-algebra). Its dimension is \( \sum_k \binom{n}{k} = 2^n \) (@thm-exterior-algebra-structure).

(b) \( \omega \wedge \eta = (-1)^{kl}\eta \wedge \omega \) for \( \omega \in \Lambda^kV \), \( \eta \in \Lambda^lV \) (@thm-exterior-algebra-graded-commutative). Both odd gives \( \omega \wedge \eta = -\eta \wedge \omega \): odd-degree elements anticommute.

(c) \( \omega \) is decomposable if \( \omega = \v_1 \wedge \dots \wedge \v_k \) for some \( \v_i \in V \) (@def-decomposable). Decomposable: \( \e_1 \wedge \e_2 \). Non-decomposable: \( \e_1 \wedge \e_2 + \e_3 \wedge \e_4 \) (@thm-non-decomposable-two-vector).

(d) The independence of the \( 2^n \) sorted products, that is, the inequality \( \dim_F C \ge 2^n \). It is supplied by @thm-clifford-dimension-proved, which needs @thm-clifford-exists first so that the object exists.

(e) False in general. They are isomorphic as vector spaces, and as algebras exactly when \( q = 0 \) (@prp-clifford-versus-exterior).
:::

### B. Practice

:::: {#exr-grassmann-and-clifford-b1}
[B1: Multiplying in the exterior algebra]

In \( \Lambda F^4 \) with \( F = \nQ \), put \( x = \e_1 + \e_2 \wedge \e_3 \) and \( y = \e_2 + \e_1 \wedge \e_4 \). Compute the following, expressed in the basis of @thm-exterior-algebra-structure.

::: {.enumerate options="label=(\alph*)"}
1. \( x \wedge y \).
2. \( y \wedge x \).
3. \( x \wedge x \).
:::
::::

::: {.solution}
Write \( \e_{S} \) for the sorted wedge on \( S \).

(a) Expanding into four products:
\[
\begin{aligned}
\e_1 \wedge \e_2 &= \e_{12}, &
\e_1 \wedge (\e_1 \wedge \e_4) &= \0, \\
(\e_2 \wedge \e_3) \wedge \e_2 &= \0, &
(\e_2 \wedge \e_3) \wedge (\e_1 \wedge \e_4) &= \e_{1234} .
\end{aligned}
\]
The last one sorts as \( \e_2 \wedge \e_3 \wedge \e_1 \wedge \e_4 = \e_{1234} \), since moving \( \e_1 \) two places to the left costs \( (-1)^2 \). So \( x \wedge y = \e_{12} + \e_{1234} \).

(b) The surviving products are \( \e_2 \wedge \e_1 = -\e_{12} \) and \( (\e_1 \wedge \e_4) \wedge (\e_2 \wedge \e_3) = \e_{1234} \), the latter because \( \e_1 \wedge \e_4 \wedge \e_2 \wedge \e_3 \) sorts with two transpositions. So \( y \wedge x = -\e_{12} + \e_{1234} \). This agrees with @thm-exterior-algebra-graded-commutative applied degree by degree: the \( (1,1) \) part changes sign, the \( (1,2) \) and \( (2,2) \) parts do not.

(c) \( x \wedge x = \e_1 \wedge \e_1 + \e_1 \wedge \e_2 \wedge \e_3 + \e_2 \wedge \e_3 \wedge \e_1 + \0 = 2\,\e_{123} \), since \( \e_2 \wedge \e_3 \wedge \e_1 = \e_{123} \). An inhomogeneous element need not square to zero.
:::

::: {#exr-grassmann-and-clifford-b2}
[B2: Decomposable or not]

In \( \Lambda^2\nQ^4 \), writing \( \e_{ij} = \e_i \wedge \e_j \), determine whether each of the following is decomposable. Justify your answer.
\[
\omega_1 = \e_{12} + \e_{13} + 3\e_{14} - 2\e_{23} - \e_{24} + 5\e_{34},
\qquad
\omega_2 = \e_{12} + \e_{34} + \e_{14} .
\]
:::

::: {.solution}
For \( \omega = \sum_{i<j}c_{ij}\e_{ij} \) in \( \Lambda^2\nQ^4 \), expanding gives
\[
\omega \wedge \omega = 2(c_{12}c_{34} - c_{13}c_{24} + c_{14}c_{23})\,\e_{1234},
\]
since the only pairs of index sets with empty intersection are \( \{12\},\{34\} \) and \( \{13\},\{24\} \) and \( \{14\},\{23\} \), each occurring in two orders, and \( \e_{13} \wedge \e_{24} = -\e_{1234} \) while the other two products are \( +\e_{1234} \).

For \( \omega_1 \): \( 1 \cdot 5 - 1 \cdot (-1) + 3 \cdot (-2) = 5 + 1 - 6 = 0 \), so \( \omega_1 \wedge \omega_1 = \0 \) and the test is inconclusive. In fact \( \omega_1 \) **is** decomposable: it is \( \v_1 \wedge \v_2 \) for \( \v_1 = (1,0,2,1) \) and \( \v_2 = (0,1,1,3) \), by @exm-wedge-coordinates-f4.

For \( \omega_2 \): \( 1 \cdot 1 - 0 \cdot 0 + 1 \cdot 0 = 1 \), so \( \omega_2 \wedge \omega_2 = 2\,\e_{1234} \ne \0 \). A decomposable \( \u \wedge \w \) satisfies \( (\u \wedge \w) \wedge (\u \wedge \w) = \0 \), so \( \omega_2 \) is **not** decomposable.
:::

::: {#exr-grassmann-and-clifford-b3}
[B3: A Clifford algebra of a line]

Let \( V = \nR \) with \( q(x) = x^2 \), the form of signature \( (1,0) \). Let \( A = \nR \times \nR \) with componentwise operations, and \( \iota_A(x) = (x, -x) \). Prove that \( (A, \iota_A) \) is a Clifford algebra of \( (V, q) \), so that \( \operatorname{Cl}_{1,0}(\nR) \cong \nR \times \nR \). Contrast this with \( \operatorname{Cl}_{0,1}(\nR) \).
:::

::: {.solution}
\( A \) is an associative unital \( \nR \)-algebra with identity \( (1,1) \) and \( \dim_{\nR}A = 2 = 2^1 \). The map \( \iota_A \) is linear, and
\[
\iota_A(x)^2 = (x, -x)(x, -x) = (x^2, x^2) = q(x)(1,1) ,
\]
which is (C1). The subalgebra generated by \( (1,1) \) and \( \iota_A(\nR) = \Span\{(1,-1)\} \) contains the independent pair \( (1,1), (1,-1) \), hence is all of \( A \). By @cor-clifford-recognition, \( (A, \iota_A) \) is a Clifford algebra of \( (V, q) \).

The contrast: Chapter 14 showed \( \operatorname{Cl}_{0,1}(\nR) = \nC \) (@exm-clifford-complex-numbers), where \( q(x) = -x^2 \). Both algebras have dimension \( 2 \), but \( \nC \) is a field and \( \nR \times \nR \) has zero divisors, \( (1,0)(0,1) = (0,0) \). A single sign in \( q \) decides which.
:::

### C. Going deeper

:::: {#exr-grassmann-and-clifford-c1}
[C1: The Plücker relation]

Let \( \dim V = 4 \) with basis \( (\e_1, \dots, \e_4) \), let \( \operatorname{char} F \ne 2 \), and let \( \omega = \sum_{i<j}c_{ij}\e_{ij} \in \Lambda^2V \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \omega \wedge \omega = 2(c_{12}c_{34} - c_{13}c_{24} + c_{14}c_{23})\,\e_{1234} \).
2. Deduce that if \( c_{12}c_{34} - c_{13}c_{24} + c_{14}c_{23} \ne 0 \) then \( \omega \) is not decomposable.
3. Prove the converse: if the expression vanishes, then \( \omega \) is decomposable. *Hint: if \( \omega \ne \0 \), some \( c_{ij} \ne 0 \); after relabeling the basis assume \( c_{12} \ne 0 \) and look for \( \omega \) as a wedge of two vectors whose first two coordinates you may normalize.*
:::
::::

::: {.solution}
(a) By bilinearity, \( \omega \wedge \omega = \sum_{S,T}c_Sc_T\,\e_S \wedge \e_T \) over \( 2 \)-element sets \( S, T \). A term vanishes unless \( S \cap T = \emptyset \), so the surviving pairs are \( (\{1,2\},\{3,4\}) \), \( (\{1,3\},\{2,4\}) \), \( (\{1,4\},\{2,3\}) \) and their reverses. By @thm-exterior-algebra-graded-commutative with \( k = l = 2 \), reversing a pair does not change the product, so each contributes twice. Sorting, \( \e_{12} \wedge \e_{34} = \e_{1234} \); \( \e_{13} \wedge \e_{24} = \e_1 \wedge \e_3 \wedge \e_2 \wedge \e_4 = -\e_{1234} \), one transposition; and \( \e_{14} \wedge \e_{23} = \e_1 \wedge \e_4 \wedge \e_2 \wedge \e_3 = \e_{1234} \), two transpositions. Collecting gives the stated formula.

(b) If \( \omega = \u \wedge \w \) then \( \omega \wedge \omega = \u \wedge \w \wedge \u \wedge \w = \0 \), a wedge with a repeated vector. Since \( \operatorname{char} F \ne 2 \), (a) then forces the bracket to vanish. Contrapositively, a non-zero bracket rules out decomposability.

(c) If \( \omega = \0 \) it is decomposable. Otherwise relabel the basis so that \( c_{12} \ne 0 \); this is legitimate because a permutation of the basis permutes the six coefficients up to sign and changes the bracket by at most a sign, so both the hypothesis and the conclusion are preserved. Put
\[
\u = c_{12}\e_1 - c_{23}\e_3 - c_{24}\e_4,
\qquad
\w = \e_2 + \tfrac{c_{13}}{c_{12}}\e_3 + \tfrac{c_{14}}{c_{12}}\e_4 .
\]
Expanding and sorting each wedge,
\[
\begin{aligned}
\u \wedge \w = {}& c_{12}\e_{12} + c_{13}\e_{13} + c_{14}\e_{14} \\
& + c_{23}\e_{23} + c_{24}\e_{24} + \tfrac{1}{c_{12}}(c_{13}c_{24} - c_{14}c_{23})\,\e_{34} .
\end{aligned}
\]
Each of the first five coefficients is read off a single product: for instance the \( \e_{23} \) term comes from \( (-c_{23}\e_3) \wedge \e_2 = c_{23}\e_{23} \), and the \( \e_{13} \) term from \( c_{12}\e_1 \wedge \tfrac{c_{13}}{c_{12}}\e_3 \). The last comes from
\[
(-c_{23}\e_3 - c_{24}\e_4) \wedge \Bigl(\tfrac{c_{13}}{c_{12}}\e_3 + \tfrac{c_{14}}{c_{12}}\e_4\Bigr)
= \tfrac{c_{13}c_{24} - c_{14}c_{23}}{c_{12}}\,\e_{34} .
\]
By hypothesis \( c_{13}c_{24} - c_{14}c_{23} = c_{12}c_{34} \), so that coefficient is \( c_{34} \) and \( \u \wedge \w = \omega \). Hence \( \omega \) is decomposable.
:::

:::: {#exr-grassmann-and-clifford-c2}
[C2: Characteristic two]

Let \( F = \nF_2 \) and \( \dim V = 4 \) with basis \( (\e_1, \dots, \e_4) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \omega \wedge \omega = \0 \) for **every** \( \omega \in \Lambda^2V \).
2. Explain why (a) does not make every element of \( \Lambda^2V \) decomposable, and name the element and the argument that settle it.
3. Is the statement "\( \omega \wedge \omega = \0 \) for every \( \omega \) of odd degree" also special to characteristic \( 2 \)? Justify your answer.
:::
::::

::: {.solution}
(a) By the computation of @exr-grassmann-and-clifford-c1 (a), \( \omega \wedge \omega \) is \( 2 \) times an element of \( \Lambda^4V \), and \( 2 = 0 \) in \( \nF_2 \). (Equivalently: in \( \sum_{S,T}c_Sc_T\,\e_S \wedge \e_T \) the diagonal terms vanish and the off-diagonal ones pair up, each pair summing to \( 2c_Sc_T\,\e_S \wedge \e_T = \0 \).)

(b) Because \( \omega \wedge \omega = \0 \) is only a **necessary** condition for decomposability, and over \( \nF_2 \) everything satisfies it, so it carries no information at all. The element \( \omega = \e_1 \wedge \e_2 + \e_3 \wedge \e_4 \) is still not decomposable, by @thm-non-decomposable-two-vector, whose proof computes \( \v \wedge \omega \) for a general \( \v \) and never divides by \( 2 \).

(c) No, that one is characteristic-free: @thm-exterior-algebra-graded-commutative proves \( \omega \wedge \omega = \0 \) for odd degree over every field, by pairing off the terms with \( S \ne T \) rather than by dividing. Over \( \nF_2 \) the statement is true but vacuous as a test, for the same reason as in (a).
:::

::: {#exr-grassmann-and-clifford-c3}
[C3: The even part of a Clifford algebra]

Let \( \operatorname{char} F \ne 2 \), \( \dim V = n \ge 1 \), and let \( (C, \iota) \) be a Clifford algebra of \( (V, q) \), and let \( (\e_1, \dots, \e_n) \) be an orthogonal basis of \( V \) for \( \beta \). Let \( C^{+} \subseteq C \) be the span of the sorted products with \( k \) **even**, and \( C^{-} \) the span of those with \( k \) odd. Prove that \( C = C^{+} \oplus C^{-} \), that \( C^{+} \) is a subalgebra of \( C \), and that \( \dim_F C^{+} = \dim_F C^{-} = 2^{n-1} \). Is \( C^{-} \) a subalgebra?

*Hint: what does the sorting procedure of @prp-clifford-spanning do to the parity of the length of a product?*
:::

::: {.solution}
The sorted products form a basis of \( C \) by @thm-clifford-dimension-proved, and they are partitioned by the parity of \( \lvert S \rvert \), so \( C = C^{+} \oplus C^{-} \) and the two dimensions are \( \sum_{k \text{ even}}\binom{n}{k} \) and \( \sum_{k \text{ odd}}\binom{n}{k} \). These are equal and sum to \( 2^n \), since \( \sum_k (-1)^k\binom{n}{k} = (1-1)^n = 0 \) for \( n \ge 1 \); so each is \( 2^{n-1} \).

For the subalgebra claim, note that the two moves in the proof of @prp-clifford-spanning — swapping two neighboring distinct factors, and replacing \( \iota(\e_i)^2 \) by the scalar \( d_i \) — change the length of a product by \( 0 \) and by \( 2 \) respectively. Both preserve parity. So the product of two sorted products of lengths \( k \) and \( l \) is a combination of sorted products of length congruent to \( k + l \) modulo \( 2 \). Hence \( C^{+}C^{+} \subseteq C^{+} \), and since \( 1_C \in C^{+} \) (the empty product, of length \( 0 \)), \( C^{+} \) is a subalgebra.

\( C^{-} \) is not: \( 1_C \notin C^{-} \), and \( C^{-}C^{-} \subseteq C^{+} \) by the same parity count, so \( C^{-} \) fails to be closed as soon as it holds an element with non-zero square, such as \( \iota(\e_i) \) with \( q(\e_i) \ne 0 \).
:::
