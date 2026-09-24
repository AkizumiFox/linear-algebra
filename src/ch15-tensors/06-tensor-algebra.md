# The Tensor Algebra

Sections 03 and 04 already iterated the tensor product: \( V^{\otimes k} \) is \( V \otimes \dots \otimes V \) with \( k \) factors, its brackets do not matter (@prp-tensor-associative), and \( k \)-linear maps out of \( V^k \) become linear maps on it (@lem-multilinear-universal). Two things are still missing, and Chapter 14 needs both. The first is a **basis** of \( V^{\otimes k} \), which the next three sections will cut down in two different ways. The second is a single algebra holding all the powers at once: Chapter 14 §12 described it as the algebra of "formal sums of strings of vectors, multiplied by concatenation", said no such algebra had been built, and deferred the Clifford algebra until it was. This section builds it, calls it \( \operatorname{T}(V) \), and proves the universal property that Sections 07, 08 and 10 will each quotient.

Throughout, \( F \) is a field and \( V \) is a finite-dimensional vector space over \( F \), with \( n = \dim V \). The letter \( k \) always denotes a non-negative integer.

## The \( k \)-th tensor power

Section 04 wrote \( V^{\otimes k} \) for the \( k \)-fold tensor product and \( V^{\otimes 0} = F \), and Section 03 proved what maps out of it look like. Before using that space three more times it is worth restating the property as a **characterization**, in the form the rest of the chapter will copy: *say what maps out of the object look like, and demand that the object be the most economical one with that property.* The definition below is @def-tensor-product with \( k \) slots in place of two, and nothing else changes.

*The \( k \)-th tensor power is the space in which \( k \)-linear maps become linear.*

::: {#def-tensor-power}
[\( k \)-th Tensor Power]

Let \( V \) be a vector space over \( F \) and let \( k \ge 1 \). A **\( k \)-th tensor power of \( V \)** is a pair \( (P, \mu) \), where \( P \) is a vector space over \( F \) and \( \mu \colon V^k \to P \) is a \( k \)-linear map, such that

::: {.enumerate options="label=(T\arabic*)"}
1. (**universal property**) for **every** vector space \( W \) over \( F \) and **every** \( k \)-linear map \( f \colon V^k \to W \), there is a **unique** linear map \( \bar f \colon P \to W \) with \( \bar f \circ \mu = f \).
:::

We write \( V^{\otimes k} \) for \( P \) and
\[
\v_1 \otimes \v_2 \otimes \dots \otimes \v_k \coloneqq \mu(\v_1, \dots, \v_k)
\]
for the value of \( \mu \), and we call such an element a **simple tensor**. By convention \( V^{\otimes 0} = F \), with \( \mu \) the empty product \( 1 \in F \).
:::

Clause by clause. The pair is what is defined, not the space alone: without \( \mu \) there is nothing for \( f \) to factor through, and a bare vector space of the right dimension satisfies nothing. **Every** vector space \( W \) is allowed as a target, including \( W = F \) and including \( P \) itself; the property is a demand about all of them simultaneously. **Unique** is the clause that does the work later: existence of \( \bar f \) says \( P \) is big enough to record \( f \), and uniqueness says \( P \) is not bigger than that.

At \( k = 1 \) a \( 1 \)-linear map is a linear map, and the pair \( (V, \id_V) \) satisfies (T1) with \( \bar f = f \). So \( V^{\otimes 1} = V \), and the notation agrees with itself. At \( k = 2 \) the definition is @def-tensor-product with \( W \) replaced by \( V \), so \( V^{\otimes 2} = V \otimes V \). The convention \( V^{\otimes 0} = F \) is a convention in the same sense as \( \Span(\emptyset) = \{\0\} \) and \( 0! = 1 \): it is the choice that keeps the formulas below true at the boundary, as the dimension count \( \dim V^{\otimes k} = n^k \) and the multiplication rule will both confirm.

Uniqueness first, exactly as in Section 02.

::: {#thm-tensor-power-unique}
[Uniqueness of the Tensor Power]

Let \( (P, \mu) \) and \( (P', \mu') \) both be \( k \)-th tensor powers of \( V \). Then there is a **unique** linear isomorphism \( \varphi \colon P \to P' \) with \( \varphi \circ \mu = \mu' \).
:::

::: {.proof}
This is the proof of @thm-tensor-unique with \( k \) slots in place of two, and we run it once more so that the pattern is visible. Since \( \mu' \) is \( k \)-linear, (T1) for \( P \) gives a linear \( \varphi \colon P \to P' \) with \( \varphi\mu = \mu' \). Since \( \mu \) is \( k \)-linear, (T1) for \( P' \) gives a linear \( \psi \colon P' \to P \) with \( \psi\mu' = \mu \). Then \( \psi\varphi \colon P \to P \) is linear with \( \psi\varphi\mu = \psi\mu' = \mu \), and \( \id_P \) is another such map. By the uniqueness clause of (T1) for \( P \), applied to the \( k \)-linear map \( \mu \) itself, the two coincide: \( \psi\varphi = \id_P \). Swapping the roles of \( P \) and \( P' \) gives \( \varphi\psi = \id_{P'} \). Hence \( \varphi \) is an isomorphism, and (T1) delivered it uniquely. This proves the theorem.
:::

Four lines, and they used nothing but the property itself. That is the point of defining objects this way, and it is why the remaining uniqueness proofs in this chapter will be compressed to a citation of this one.

Now existence. Here the chapter can be lazy: a \( k \)-th tensor power does not need a new construction, because iterating the binary one already produces it.

::: {#thm-tensor-power-exists}
[Existence of the Tensor Power]

Let \( k \ge 1 \) and let \( V^{\otimes k} = V \otimes \dots \otimes V \) be the iterated tensor product of Section 03, with
\[
\mu_k(\v_1, \dots, \v_k) = \v_1 \otimes \dots \otimes \v_k .
\]
Then \( (V^{\otimes k}, \mu_k) \) is a \( k \)-th tensor power of \( V \), and it is spanned by its simple tensors.
:::

::: {.proof}
The map \( \mu_k \) is \( k \)-linear, being \( \otimes \) applied \( k - 1 \) times and \( \otimes \) bilinear in each use. Property (T1) and the spanning claim are exactly @lem-multilinear-universal, read with \( V_1 = \dots = V_k = V \). This proves the theorem.
:::

The proof is one sentence because Section 03 did the induction: freeze the last argument, apply the \( (k-1) \)-factor statement, let the last argument move again, and finish with the two-factor property. Two consequences are used in every argument below, so they are worth saying in words. **\( V^{\otimes k} \) is spanned by its simple tensors**, so two linear maps out of \( V^{\otimes k} \) are equal as soon as they agree on simple tensors; and **a \( k \)-linear recipe on \( V^k \) defines a linear map on \( V^{\otimes k} \)**, which is how every map out of a tensor power gets built, here and in Sections 07 and 08.

From now on \( V^{\otimes k} \) denotes this space, and by @thm-tensor-power-unique any other \( k \)-th tensor power is identified with it by a unique isomorphism respecting the simple tensors. So it is legitimate to speak of *the* \( k \)-th tensor power, and the model may be forgotten: every proof below argues from (T1).

## A basis, and the dimension

The count is the one Section 01 predicted. A \( k \)-linear map on an \( n \)-dimensional space may be prescribed freely on the \( n^k \) tuples of basis vectors and is determined by those values (@thm-multilinear-determined-by-basis); so \( V^{\otimes k} \) had better have dimension \( n^k \), and it does.

::: {#thm-tensor-power-basis}
[Basis of a Tensor Power]

Let \( \sB = (\v_1, \dots, \v_n) \) be a basis of \( V \) and let \( k \ge 1 \). Then the list of simple tensors
\[
\v_{i_1} \otimes \v_{i_2} \otimes \dots \otimes \v_{i_k},
\qquad (i_1, \dots, i_k) \in \{1, \dots, n\}^k ,
\]
is a basis of \( V^{\otimes k} \). In particular \( \dim V^{\otimes k} = n^k \).
:::

::: {.idea}
Spanning is multilinear expansion: write each argument in the basis and expand one slot at a time. Independence needs, for each tuple \( J \), a linear functional on \( V^{\otimes k} \) that is \( 1 \) on the tensor indexed by \( J \) and \( 0 \) on the others. Build it upstairs, as a product of dual basis functionals, and let the universal property carry it down.
:::

::: {.proof}
*Spanning.* By @thm-tensor-power-exists, \( V^{\otimes k} \) is spanned by its simple tensors, so it suffices to expand one of them in the basis \( \sB \). Write \( \u_t = \sum_{i=1}^{n} c_{ti}\v_i \) for \( t = 1, \dots, k \). Expanding \( \u_1 \otimes \dots \otimes \u_k \) in slot \( 1 \), then in slot \( 2 \), and so on, using \( k \)-linearity of \( \mu_k \) once per slot, gives
\[
\u_1 \otimes \dots \otimes \u_k
= \sum_{i_1, \dots, i_k} c_{1i_1}\cdots c_{ki_k}\;
\v_{i_1} \otimes \dots \otimes \v_{i_k},
\]
a linear combination of the listed tensors.

*Independence.* Let \( (\varphi_1, \dots, \varphi_n) \) be the dual basis of \( \sB \) (@thm-dual-basis), so \( \varphi_i(\v_j) = \delta_{ij} \). Fix a tuple \( J = (j_1, \dots, j_k) \) and define
\[
f_J(\u_1, \dots, \u_k) = \varphi_{j_1}(\u_1)\,\varphi_{j_2}(\u_2)\cdots\varphi_{j_k}(\u_k) .
\]
This is \( k \)-linear: in position \( t \) it is the functional \( \varphi_{j_t} \) times a fixed scalar. By (T1) it induces a linear \( \bar f_J \colon V^{\otimes k} \to F \) with
\[
\bar f_J(\v_{i_1} \otimes \dots \otimes \v_{i_k})
= \delta_{j_1 i_1}\cdots\delta_{j_k i_k},
\]
which is \( 1 \) if \( I = J \) and \( 0 \) otherwise. Now suppose \( \sum_I a_I \,\v_{i_1} \otimes \dots \otimes \v_{i_k} = \0 \), the sum over all \( n^k \) tuples \( I \). Applying \( \bar f_J \) to both sides leaves \( a_J = 0 \). Since \( J \) was arbitrary, every coefficient vanishes.

Hence the list is a basis. It has one member per tuple in \( \{1, \dots, n\}^k \), and there are \( n^k \) of those, so \( \dim V^{\otimes k} = n^k \). This proves the theorem.
:::

The count also confirms the convention \( V^{\otimes 0} = F \): the formula \( n^k \) at \( k = 0 \) reads \( n^0 = 1 = \dim F \), and the only \( 0 \)-tuple is the empty one.

::: {.check}
Let \( \dim V = 3 \). What is \( \dim V^{\otimes 4} \), and how many of its basis tensors have all four indices distinct?
:::

::: {.solution}
\( \dim V^{\otimes 4} = 3^4 = 81 \). None: an index tuple of length \( 4 \) drawn from \( \{1, 2, 3\} \) must repeat a value, by the pigeonhole principle. This is the first sign that the tensors with a repeated index are not a negligible part of \( V^{\otimes k} \) — Section 08 will divide by the span of the simple tensors \( \u_1 \otimes \dots \otimes \u_k \) that repeat a **vector**, a subspace containing every one of these.
:::

::: {#exm-tensor-cube-of-the-plane}
[A tensor cube, in coordinates]

Let \( V = F^2 \) with standard basis \( (\e_1, \e_2) \). Write out a basis of \( V^{\otimes 3} \), and expand \( (\e_1 + \e_2) \otimes (\e_1 - \e_2) \otimes \e_1 \) in it.
:::

::: {.solution}
By @thm-tensor-power-basis a basis is indexed by the \( 2^3 = 8 \) triples of indices from \( \{1, 2\} \):
\[
\begin{aligned}
&\e_1\otimes\e_1\otimes\e_1, \quad \e_1\otimes\e_1\otimes\e_2, \quad
\e_1\otimes\e_2\otimes\e_1, \quad \e_1\otimes\e_2\otimes\e_2, \\
&\e_2\otimes\e_1\otimes\e_1, \quad \e_2\otimes\e_1\otimes\e_2, \quad
\e_2\otimes\e_2\otimes\e_1, \quad \e_2\otimes\e_2\otimes\e_2 .
\end{aligned}
\]
Expanding slot by slot, first in slot \( 1 \) and then in slot \( 2 \), and noting that slot \( 3 \) is already a basis vector,
\[
\begin{aligned}
(\e_1 + \e_2)\otimes(\e_1 - \e_2)\otimes\e_1
={}& \e_1\otimes\e_1\otimes\e_1 - \e_1\otimes\e_2\otimes\e_1 \\
&+ \e_2\otimes\e_1\otimes\e_1 - \e_2\otimes\e_2\otimes\e_1 .
\end{aligned}
\]
Four of the eight coordinates are non-zero and the other four are \( 0 \). Note also that \( \e_1 \otimes \e_2 \otimes \e_1 \) and \( \e_2 \otimes \e_1 \otimes \e_1 \) are **different** basis vectors: the order of the slots is part of the data.
:::

## Stacking the powers: the tensor algebra

We now have one space for each \( k \). Chapter 14 wanted a single algebra containing all of them, in which \( \v_1 \otimes \v_2 \) and \( \v_3 \otimes \v_4 \otimes \v_5 \) could be multiplied to give \( \v_1 \otimes \v_2 \otimes \v_3 \otimes \v_4 \otimes \v_5 \). The multiplication is concatenation of strings; the only work is to define it without choosing a basis.

First the multiplication on a single pair of powers.

::: {#prp-tensor-concatenation}
[Concatenation of Tensors]

Let \( k, l \ge 1 \). There is a unique bilinear map
\[
V^{\otimes k} \times V^{\otimes l} \to V^{\otimes (k+l)},
\qquad (x, y) \mapsto x \cdot y ,
\]
such that for all \( \u_1, \dots, \u_k, \w_1, \dots, \w_l \in V \),
\[
(\u_1 \otimes \dots \otimes \u_k)\cdot(\w_1 \otimes \dots \otimes \w_l)
= \u_1 \otimes \dots \otimes \u_k \otimes \w_1 \otimes \dots \otimes \w_l .
\]
:::

::: {.idea}
The same peeling move as in @thm-tensor-power-exists, applied to the two blocks of slots in turn: first make the last \( l \) slots into a linear map, then make the first \( k \) slots into a linear map whose values are those linear maps.
:::

::: {.proof}
Fix \( \u_1, \dots, \u_k \in V \). The map \( V^l \to V^{\otimes(k+l)} \) sending \( (\w_1, \dots, \w_l) \) to \( \u_1 \otimes \dots \otimes \u_k \otimes \w_1 \otimes \dots \otimes \w_l \) is \( l \)-linear, since \( \mu_{k+l} \) is \( (k+l) \)-linear and the first \( k \) arguments are fixed. By (T1) for \( V^{\otimes l} \) it induces a unique linear map \( R(\u_1, \dots, \u_k) \colon V^{\otimes l} \to V^{\otimes (k+l)} \).

Next, \( (\u_1, \dots, \u_k) \mapsto R(\u_1, \dots, \u_k) \) is \( k \)-linear as a map into \( \cL(V^{\otimes l}, V^{\otimes (k+l)}) \). Indeed, two linear maps \( V^{\otimes l} \to V^{\otimes(k+l)} \) are equal as soon as they agree on simple tensors, and on a simple tensor both sides of each linearity identity reduce to linearity of \( \mu_{k+l} \) in one of its first \( k \) slots. By (T1) for \( V^{\otimes k} \) we get a linear map
\[
M \colon V^{\otimes k} \to \cL\bigl(V^{\otimes l},\, V^{\otimes(k+l)}\bigr),
\]
and we set \( x \cdot y = M(x)(y) \). This is linear in \( x \) because \( M \) is linear, and linear in \( y \) because each \( M(x) \) is linear, so it is bilinear, and on simple tensors it is the displayed concatenation.

Uniqueness: a bilinear map is determined by its values on pairs of spanning sets, and each factor is spanned by its simple tensors. This proves the proposition.
:::

With \( k = 0 \) or \( l = 0 \) we let \( \cdot \) be scalar multiplication, which is the only bilinear option on \( F \times V^{\otimes l} \) agreeing with "prepend nothing". Now stack.

::: {#def-tensor-algebra}
[Tensor Algebra]

Let \( V \) be a vector space over \( F \). The **tensor algebra** of \( V \) is the vector space
\[
\operatorname{T}(V) = \bigoplus_{k \ge 0} V^{\otimes k},
\]
whose elements are the sequences \( x = (x_0, x_1, x_2, \dots) \) with \( x_k \in V^{\otimes k} \) and \( x_k = \0 \) for **all but finitely many** \( k \), with componentwise addition and scalar multiplication, and whose multiplication is
\[
(xy)_m = \sum_{k + l = m} x_k \cdot y_l ,
\]
with \( \cdot \) as in @prp-tensor-concatenation. We identify \( V^{\otimes k} \) with the set of sequences supported in position \( k \), so that \( F = V^{\otimes 0} \) and \( V = V^{\otimes 1} \) are subspaces of \( \operatorname{T}(V) \). An element of \( V^{\otimes k} \subseteq \operatorname{T}(V) \) is called **homogeneous of degree \( k \)**.
:::

The "all but finitely many" clause is the same one that makes \( F[x] \) a space of polynomials rather than power series (@def-polynomial): an element of \( \operatorname{T}(V) \) is a **finite** sum \( x_0 + x_1 + \dots + x_N \), not a series. The formula for \( (xy)_m \) is then a finite sum, so the product is defined.

::: {#thm-tensor-algebra-is-an-algebra}
[The Tensor Algebra Is an Algebra]

\( \operatorname{T}(V) \) with the above operations is an associative unital \( F \)-algebra (@def-algebra-over-field), with identity \( 1 \in F = V^{\otimes 0} \). Moreover \( V^{\otimes k}\cdot V^{\otimes l} \subseteq V^{\otimes(k+l)} \) for all \( k, l \).
:::

::: {.proof}
Bilinearity of the multiplication is immediate from bilinearity of each \( \cdot \) in @prp-tensor-concatenation, since the components of \( xy \) are finite sums of bilinear expressions in the components of \( x \) and \( y \).

For associativity it suffices, by bilinearity in each of the three arguments and because the homogeneous components span, to check \( (xy)z = x(yz) \) for homogeneous \( x, y, z \), and then, because each power is spanned by its simple tensors, for simple tensors. Both sides are then the single simple tensor obtained by writing the three strings of vectors one after another, so they agree.

For the identity, \( 1 \in F = V^{\otimes 0} \) acts on each \( V^{\otimes k} \) as scalar multiplication by \( 1 \), hence as the identity. The grading statement is the target of @prp-tensor-concatenation. This proves the theorem.
:::

From here on we drop the dot and write \( xy \), and for simple tensors we write \( \u_1\otimes\dots\otimes\u_k \) for both the element and the product \( \u_1\u_2\cdots\u_k \) of \( k \) elements of \( V \) — they are the same thing, since concatenating \( k \) strings of length \( 1 \) gives the string of length \( k \).

::: {.warning}
**\( \operatorname{T}(V) \) is not commutative, and not finite-dimensional.** If \( \dim V \ge 2 \), pick basis vectors \( \v_1 \ne \v_2 \); then \( \v_1 \otimes \v_2 \) and \( \v_2 \otimes \v_1 \) are **distinct basis vectors** of \( V^{\otimes 2} \) by @thm-tensor-power-basis, so \( \v_1\v_2 \ne \v_2\v_1 \). And \( \dim \operatorname{T}(V) = \sum_k n^k \) is infinite as soon as \( n \ge 1 \), even though \( V \) is finite-dimensional. Every individual element still has only finitely many non-zero components.
:::

::: {#exm-tensor-algebra-of-a-line}
[The tensor algebra of a line]

Let \( \dim V = 1 \), say \( V = F\v \). Identify \( \operatorname{T}(V) \) with a familiar algebra.
:::

::: {.solution}
By @thm-tensor-power-basis, \( V^{\otimes k} \) has the single basis vector \( \v^{\otimes k} = \v \otimes \dots \otimes \v \), so \( \dim V^{\otimes k} = 1^k = 1 \). An element of \( \operatorname{T}(V) \) is therefore a finite sum \( a_0 + a_1\v + a_2\v^{\otimes 2} + \dots \) with \( a_k \in F \), and concatenation gives \( \v^{\otimes k}\v^{\otimes l} = \v^{\otimes(k+l)} \). Matching \( \v^{\otimes k} \) with \( x^k \) turns these into exactly the addition and multiplication rules of @def-polynomial-ring, so \( \operatorname{T}(V) \cong F[x] \) as \( F \)-algebras.

In particular \( \operatorname{T}(V) \) *is* commutative when \( \dim V = 1 \): there is only one letter, so no two letters can fail to commute. The warning above needed \( \dim V \ge 2 \), and it needed it for a reason.
:::

## The universal property of the tensor algebra

The tensor powers were characterized by what \( k \)-linear maps do. The algebra assembled from them has its own characterization, and it is the one Sections 07, 08 and 10 will use: **to define an algebra homomorphism out of \( \operatorname{T}(V) \), you only have to say what it does to the vectors.**

::: {#thm-tensor-algebra-universal}
[Universal Property of the Tensor Algebra]

Let \( V \) be a vector space over \( F \), let \( A \) be an associative unital \( F \)-algebra, and let \( f \colon V \to A \) be a **linear** map. Then there is a **unique** algebra homomorphism
\[
\bar f \colon \operatorname{T}(V) \to A
\qquad\text{with}\qquad
\bar f\bigl|_{V} = f .
\]
Explicitly, \( \bar f(\u_1 \otimes \dots \otimes \u_k) = f(\u_1)\cdots f(\u_k) \) and \( \bar f(a) = a1_A \) for \( a \in F \).
:::

::: {.idea}
Degree by degree. In degree \( k \), the recipe \( (\u_1, \dots, \u_k) \mapsto f(\u_1)\cdots f(\u_k) \) is \( k \)-linear because the product of \( A \) is bilinear and \( f \) is linear, so (T1) converts it into a linear map on \( V^{\otimes k} \). Assemble the pieces and check multiplicativity on simple tensors, which span.
:::

::: {.proof}
*Existence.* For \( k \ge 1 \) the map \( V^k \to A \) given by \( (\u_1, \dots, \u_k) \mapsto f(\u_1)f(\u_2)\cdots f(\u_k) \) is \( k \)-linear: with all arguments but the \( t \)-th fixed, it is \( f \) followed by multiplication on the left and on the right by fixed elements of \( A \), and all three of those maps are linear, the last two by bilinearity of the product (A1). By (T1) there is a unique linear \( \bar f_k \colon V^{\otimes k} \to A \) with \( \bar f_k(\u_1 \otimes \dots \otimes \u_k) = f(\u_1)\cdots f(\u_k) \). Put \( \bar f_0 \colon F \to A \), \( a \mapsto a1_A \), and define \( \bar f(x) = \sum_k \bar f_k(x_k) \), a finite sum. This is linear, and \( \bar f(1) = 1_A \).

Multiplicativity: the maps \( (x, y) \mapsto \bar f(xy) \) and \( (x, y) \mapsto \bar f(x)\bar f(y) \) are both bilinear, so it suffices to compare them on a spanning set of each argument, and the simple tensors of all degrees span \( \operatorname{T}(V) \). For two simple tensors,
\[
\begin{aligned}
\bar f\bigl((\u_1\otimes\dots\otimes\u_k)(\w_1\otimes\dots\otimes\w_l)\bigr)
&= f(\u_1)\cdots f(\u_k)f(\w_1)\cdots f(\w_l) \\
&= \bar f(\u_1\otimes\dots\otimes\u_k)\,\bar f(\w_1\otimes\dots\otimes\w_l),
\end{aligned}
\]
the first equality by @prp-tensor-concatenation and the definition of \( \bar f_{k+l} \), the second by the definition of \( \bar f_k \) and \( \bar f_l \) together with associativity in \( A \). The degree-\( 0 \) cases are the identity \( \bar f(ax) = a\bar f(x) \), which holds by linearity. Finally \( \bar f|_V = \bar f_1 = f \).

*Uniqueness.* Let \( \varphi \) be an algebra homomorphism with \( \varphi|_V = f \). Then \( \varphi(1) = 1_A \), so \( \varphi(a) = a1_A \) on \( V^{\otimes 0} \), and for a simple tensor, multiplicativity gives
\[
\varphi(\u_1\otimes\dots\otimes\u_k) = \varphi(\u_1)\cdots\varphi(\u_k) = f(\u_1)\cdots f(\u_k) .
\]
So \( \varphi \) agrees with \( \bar f \) on the simple tensors, which span \( \operatorname{T}(V) \), and both are linear. Hence \( \varphi = \bar f \). This proves the theorem.
:::

In words: **\( \operatorname{T}(V) \) is the free associative unital algebra on \( V \).** "Free" means that a linear map out of \( V \) extends to an algebra map in exactly one way, with no condition on \( f \) whatsoever — no multiplicativity is asked of \( f \), because \( V \) carries no multiplication to preserve. Compare the corresponding statement one level down, @thm-linear-map-from-any-basis: a *function* on a basis extends to a linear map in exactly one way. The tensor algebra plays the same role one level up.

::: {.remark}
The hypothesis on \( f \) is empty, and that is precisely what makes \( \operatorname{T}(V) \) too big to be useful on its own. Every interesting algebra built from \( V \) is a quotient of \( \operatorname{T}(V) \) by the relations one wants to impose, and @thm-tensor-algebra-universal is what shows that the quotient has the expected universal property. Section 07 imposes \( \u\w = \w\u \), Section 08 imposes \( \v\v = 0 \), and Section 10 imposes \( \v\v = q(\v)1 \), which is the construction Chapter 14 §12 said was unavailable.
:::

::: {.warning}
**Do not confuse the degree with the dimension.** \( V^{\otimes k} \) is the space of tensors of degree \( k \); its dimension is \( n^k \), not \( k \). A general element of \( V^{\otimes k} \) is a sum of simple tensors, and — exactly as in Section 02 — usually not a single one. A general element of \( \operatorname{T}(V) \) is not even homogeneous: \( 1 + \v_1 + \v_1\otimes\v_2 \) is a perfectly good element of degrees \( 0, 1, 2 \) at once.
:::

## Exercises

### A. Check your understanding

::: {#exr-tensor-algebra-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the universal property (T1) of the \( k \)-th tensor power, with every quantifier.
2. Let \( \dim V = 4 \). Compute \( \dim V^{\otimes 0} \), \( \dim V^{\otimes 1} \) and \( \dim V^{\otimes 3} \).
3. Give a spanning set of \( V^{\otimes k} \), and explain why it lets you check an identity between linear maps out of \( V^{\otimes k} \) on simple tensors only.
4. Determine whether \( \operatorname{T}(V) \) is commutative. Justify your answer, distinguishing the possible values of \( \dim V \).
5. State what data is needed to define an algebra homomorphism out of \( \operatorname{T}(V) \), and what must be checked about it.
:::
:::

::: {.solution}
(a) For every vector space \( W \) over \( F \) and every \( k \)-linear map \( f \colon V^k \to W \), there exists exactly one linear map \( \bar f \colon V^{\otimes k} \to W \) such that \( \bar f \circ \mu = f \), where \( \mu(\v_1, \dots, \v_k) = \v_1 \otimes \dots \otimes \v_k \).

(b) \( \dim V^{\otimes 0} = \dim F = 1 \); \( \dim V^{\otimes 1} = 4 \); \( \dim V^{\otimes 3} = 4^3 = 64 \), by @thm-tensor-power-basis.

(c) The simple tensors \( \u_1 \otimes \dots \otimes \u_k \) span \( V^{\otimes k} \) (@thm-tensor-power-exists); so does the smaller list of @thm-tensor-power-basis. Two linear maps that agree on a spanning set agree on every linear combination of it, hence everywhere.

(d) It is commutative if \( \dim V \le 1 \) and non-commutative if \( \dim V \ge 2 \). For \( \dim V = 0 \), \( \operatorname{T}(V) = F \); for \( \dim V = 1 \), \( \operatorname{T}(V) \cong F[x] \) by @exm-tensor-algebra-of-a-line. For \( \dim V \ge 2 \), \( \v_1 \otimes \v_2 \) and \( \v_2 \otimes \v_1 \) are distinct members of a basis by @thm-tensor-power-basis, so they are unequal.

(e) A **linear** map \( f \colon V \to A \) into an associative unital algebra \( A \), and nothing else: no condition on \( f \) needs checking, by @thm-tensor-algebra-universal. What must be checked is that \( A \) really is an associative unital algebra and that \( f \) really is linear.
:::

### B. Practice

::: {#exr-tensor-algebra-b1}
[B1: Expanding a simple tensor]

Let \( V = F^2 \). Expand each of the following in the basis of @thm-tensor-power-basis.

::: {.enumerate options="label=(\alph*)"}
1. \( (2\e_1 - \e_2) \otimes (\e_1 + 3\e_2) \) in \( V^{\otimes 2} \).
2. \( \e_1 \otimes (\e_1 - \e_2) \otimes (\e_1 + \e_2) \) in \( V^{\otimes 3} \).
:::
:::

::: {.solution}
(a) Expanding in slot \( 1 \), then slot \( 2 \),
\[
\begin{aligned}
(2\e_1 - \e_2)\otimes(\e_1 + 3\e_2)
={}& 2\,\e_1\otimes\e_1 + 6\,\e_1\otimes\e_2 \\
&- \e_2\otimes\e_1 - 3\,\e_2\otimes\e_2 .
\end{aligned}
\]

(b) Slot \( 1 \) is already a basis vector, so expand slots \( 2 \) and \( 3 \):
\[
\begin{aligned}
\e_1 \otimes (\e_1 - \e_2)\otimes(\e_1+\e_2)
={}& \e_1\otimes\e_1\otimes\e_1 + \e_1\otimes\e_1\otimes\e_2 \\
&- \e_1\otimes\e_2\otimes\e_1 - \e_1\otimes\e_2\otimes\e_2 .
\end{aligned}
\]
The four basis tensors beginning with \( \e_2 \) have coefficient \( 0 \), as they must: every term of the expansion carries \( \e_1 \) in slot \( 1 \).
:::

::: {#exr-tensor-algebra-b2}
[B2: A product in the tensor algebra]

Let \( V = F^2 \) and let \( x = 1 + \e_1 \) and \( y = \e_2 - \e_1\otimes\e_1 \) in \( \operatorname{T}(V) \). Compute \( xy \) and \( yx \), sort the answers by degree, and say whether \( x \) and \( y \) commute.
:::

::: {.solution}
Multiply out, using that \( 1 \) is the identity and that concatenation is @prp-tensor-concatenation:
\[
\begin{aligned}
xy &= \e_2 - \e_1\otimes\e_1 + \e_1\otimes\e_2 - \e_1\otimes\e_1\otimes\e_1 , \\
yx &= \e_2 - \e_1\otimes\e_1 + \e_2\otimes\e_1 - \e_1\otimes\e_1\otimes\e_1 .
\end{aligned}
\]
Both have degree-\( 1 \) part \( \e_2 \) and degree-\( 3 \) part \( -\e_1\otimes\e_1\otimes\e_1 \). Their degree-\( 2 \) parts differ: \( -\e_1\otimes\e_1 + \e_1\otimes\e_2 \) against \( -\e_1\otimes\e_1 + \e_2\otimes\e_1 \). Since \( \e_1\otimes\e_2 \ne \e_2\otimes\e_1 \) by @thm-tensor-power-basis, \( xy \ne yx \): they do not commute.
:::

::: {#exr-tensor-algebra-b3}
[B3: A homomorphism built from the universal property]

Let \( V = F^2 \) and let \( A = M_2(F) \). Define \( f \colon V \to A \) by
\[
f(x_1\e_1 + x_2\e_2) = \begin{pmatrix} 0 & x_1 \\ x_2 & 0 \end{pmatrix} .
\]
Prove that there is a unique algebra homomorphism \( \bar f \colon \operatorname{T}(V) \to M_2(F) \) with \( \bar f|_V = f \), and compute \( \bar f(\e_1 \otimes \e_2) \), \( \bar f(\e_2\otimes\e_1) \) and \( \bar f(\e_1\otimes\e_1) \).
:::

::: {.solution}
\( M_2(F) \) is an associative unital \( F \)-algebra (@def-algebra-over-field) and \( f \) is linear, since each entry of \( f(\x) \) is a linear function of \( \x \). By @thm-tensor-algebra-universal there is exactly one algebra homomorphism \( \bar f \) with \( \bar f|_V = f \).

On simple tensors \( \bar f \) is the product of the images, so with \( \A = f(\e_1) \) and \( \B = f(\e_2) \),
\[
\A = \begin{pmatrix} 0 & 1 \\ 0 & 0\end{pmatrix}, \quad
\B = \begin{pmatrix} 0 & 0 \\ 1 & 0\end{pmatrix},
\]
\[
\bar f(\e_1\otimes\e_2) = \A\B = \begin{pmatrix} 1 & 0 \\ 0 & 0\end{pmatrix},
\quad
\bar f(\e_2\otimes\e_1) = \B\A = \begin{pmatrix} 0 & 0 \\ 0 & 1\end{pmatrix},
\]
and \( \bar f(\e_1\otimes\e_1) = \A^2 = \0 \). The first two differ, which is another way to see that \( \e_1\otimes\e_2 \ne \e_2\otimes\e_1 \): a homomorphism cannot separate equal elements. The third shows \( \bar f \) is far from injective — as it must be, since \( \operatorname{T}(V) \) is infinite-dimensional and \( M_2(F) \) is not.
:::

### C. Going deeper

::: {#exr-tensor-algebra-c1}
[C1: The grading is a direct sum of subspaces]

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( x \in V^{\otimes k} \) and \( y \in V^{\otimes l} \) with \( k \ne l \) are both non-zero, then \( x + y \) lies in no single \( V^{\otimes m} \).
2. Deduce that an algebra homomorphism \( \varphi \colon \operatorname{T}(V) \to A \) is determined by its restrictions \( \varphi|_{V^{\otimes k}} \), and that these are in turn determined by \( \varphi|_V \).
:::
:::

::: {.solution}
(a) Under the identification of @def-tensor-algebra, \( x \) is the sequence with \( x \) in position \( k \) and \( \0 \) elsewhere, and similarly for \( y \). Their sum has non-zero entries in both positions \( k \) and \( l \). An element of \( V^{\otimes m} \) has at most one non-zero entry, in position \( m \). Since \( k \ne l \), the sum has two, so it is in no \( V^{\otimes m} \).

(b) Every element of \( \operatorname{T}(V) \) is the finite sum of its homogeneous components, so a linear map is determined by its restrictions to the \( V^{\otimes k} \). By multiplicativity, \( \varphi(\u_1\otimes\dots\otimes\u_k) = \varphi(\u_1)\cdots\varphi(\u_k) \), which depends only on \( \varphi|_V \); and \( V^{\otimes k} \) is spanned by its simple tensors, so \( \varphi|_{V^{\otimes k}} \) is determined by \( \varphi|_V \). (This is the uniqueness half of @thm-tensor-algebra-universal, isolated.)
:::

::: {#exr-tensor-algebra-c2}
[C2: Extending an operator to the algebra]

Let \( T \colon V \to V \) be linear.

::: {.enumerate options="label=(\alph*)"}
1. Prove that there is a unique algebra homomorphism \( \operatorname{T}(T) \colon \operatorname{T}(V) \to \operatorname{T}(V) \) with \( \operatorname{T}(T)|_V = T \), and that it maps \( V^{\otimes k} \) into \( V^{\otimes k} \).
2. Prove that \( \operatorname{T}(ST) = \operatorname{T}(S)\operatorname{T}(T) \) for linear \( S, T \colon V \to V \), and that \( \operatorname{T}(\id_V) = \id \).
3. Deduce that if \( T \) is invertible then so is \( \operatorname{T}(T) \).
:::
:::

::: {.solution}
(a) \( \operatorname{T}(V) \) is an associative unital algebra and the composite \( V \xrightarrow{T} V \hookrightarrow \operatorname{T}(V) \) is linear, so @thm-tensor-algebra-universal gives a unique algebra homomorphism \( \operatorname{T}(T) \) restricting to \( T \) on \( V \). On a simple tensor it is \( \u_1\otimes\dots\otimes\u_k \mapsto T\u_1 \otimes\dots\otimes T\u_k \), which lies in \( V^{\otimes k} \); those tensors span \( V^{\otimes k} \), so \( \operatorname{T}(T)(V^{\otimes k}) \subseteq V^{\otimes k} \).

(b) \( \operatorname{T}(S)\operatorname{T}(T) \) is a composite of algebra homomorphisms, hence an algebra homomorphism, and on \( V \) it is \( S T \). By the uniqueness clause of @thm-tensor-algebra-universal applied to the linear map \( ST \colon V \to \operatorname{T}(V) \), it equals \( \operatorname{T}(ST) \). Likewise \( \id_{\operatorname{T}(V)} \) is an algebra homomorphism restricting to \( \id_V \), so it equals \( \operatorname{T}(\id_V) \).

(c) By (b), \( \operatorname{T}(T)\operatorname{T}(T^{-1}) = \operatorname{T}(TT^{-1}) = \operatorname{T}(\id_V) = \id \), and the same with the factors swapped. Hence \( \operatorname{T}(T) \) is invertible with inverse \( \operatorname{T}(T^{-1}) \).
:::

::: {#exr-tensor-algebra-c3}
[C3: Why the empty degree is \( F \)]

Suppose we had instead set \( V^{\otimes 0} = \{\0\} \) and kept every other definition.

::: {.enumerate options="label=(\alph*)"}
1. Explain why @thm-tensor-power-basis would then fail at \( k = 0 \).
2. Explain why \( \operatorname{T}(V) \) would have no identity element, and hence would not be an algebra in the sense of @def-algebra-over-field.
3. Give one further formula in this section that the convention \( V^{\otimes 0} = F \) keeps true at \( k = 0 \).
:::
:::

::: {.solution}
(a) The theorem counts one basis vector per \( k \)-tuple of indices. There is exactly one \( 0 \)-tuple, the empty one, so the count gives \( n^0 = 1 \), the dimension of \( F \), not of \( \{\0\} \).

(b) The identity of \( \operatorname{T}(V) \) is \( 1 \in V^{\otimes 0} \). With \( V^{\otimes 0} = \{\0\} \) there is no candidate: a homogeneous element of degree \( m \ge 1 \) multiplies \( V^{\otimes k} \) into \( V^{\otimes(k+m)} \), so it cannot fix a non-zero element of \( V^{\otimes k} \), and neither can a sum of such elements, by @exr-tensor-algebra-c1 (a). Hypothesis (A3) of @def-algebra-over-field would fail.

(c) The universal property @thm-tensor-algebra-universal: its formula \( \bar f(a) = a1_A \) for \( a \in F \) is the degree-\( 0 \) case, and it is what makes \( \bar f \) unital. Equally acceptable: \( \dim \operatorname{T}(V) = \sum_{k \ge 0} n^k \), or the multiplication rule \( V^{\otimes 0}\cdot V^{\otimes l} \subseteq V^{\otimes l} \), which reads "multiplying by a scalar does not change the degree".
:::
