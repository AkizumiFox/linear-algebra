# Contraction and the Trace

Chapter 3 defined the trace of an operator by choosing a basis, writing down the matrix, and adding the diagonal entries; it then proved that the answer does not depend on the choice (@def-trace-operator). That is a correct definition and an unsatisfying one. It says how to compute the number, not what the number is, and the independence of the basis arrives afterwards, as a theorem about similar matrices. Section 03 offers a way out. An operator on \( V \) is an element of \( V^{*} \otimes V \) (@thm-tensor-hom-iso), and on \( V^{*} \otimes V \) there is one obvious scalar-valued map that uses no basis at all: apply the functional to the vector. This section builds that map, proves that it is the trace, and extends it to tensors with many slots.

## Evaluation, made linear

The dual space was invented so that its elements could eat vectors. The eating is a function of two arguments,
\[
V^{*} \times V \to F, \qquad (\varphi, \v) \mapsto \varphi(\v),
\]
and it is bilinear: linear in \( \v \) because \( \varphi \) is a linear map, and linear in \( \varphi \) because that is how \( V^{*} \) is added and scaled (@def-dual-space). A bilinear map is exactly what the tensor product converts into a linear one, and by now this should be a reflex.

*Contraction is the evaluation pairing, turned into a single linear map by the tensor product.*

::: {#def-contraction}
[Contraction]

Let \( V \) be a vector space over \( F \). The **contraction** of \( V \) is the unique linear map
\[
C \colon V^{*} \otimes V \to F, \qquad C(\varphi \otimes \v) = \varphi(\v)
\quad (\varphi \in V^{*},\ \v \in V).
\]
:::

**Well-definedness.** The pairing \( (\varphi, \v) \mapsto \varphi(\v) \) is bilinear, so @def-tensor-product supplies exactly one linear map on \( V^{*} \otimes V \) taking those values. Nothing else is chosen: no basis, no finite dimension, no extra structure on \( V \).

**Examples.**

1. **In coordinates.** Let \( \dim V = n \), let \( \sB = (\v_1, \dots, \v_n) \) be a basis and \( \sB^{*} = (\varphi^1, \dots, \varphi^n) \) its dual basis (@def-dual-basis), so \( \varphi^j(\v_i) = \delta^j_i \). A general \( \xi \in V^{*} \otimes V \) is \( \xi = \sum_{i,j} a_{ij}\,\varphi^j \otimes \v_i \) by @thm-tensor-basis, and
\[
C(\xi) = \sum_{i,j} a_{ij}\,\varphi^j(\v_i) = \sum_{i=1}^{n} a_{ii} .
\]
The contraction sums the coefficients whose two indices agree. That is a diagonal sum, which is the first hint of what is coming.
2. **The smallest case.** If \( \dim V = 1 \), pick \( \v \ne \0 \) and let \( \varphi \) be dual to it. Every element of \( V^{*} \otimes V \) is \( a\,\varphi \otimes \v \), and \( C(a\,\varphi \otimes \v) = a \). So \( C \) is the isomorphism \( V^{*} \otimes V \cong F \). Degenerate, and worth seeing: the contraction is the only thing that can happen here.
3. **A functional times a vector, in \( F^n \).** With \( V = F^n \), \( \varphi = \y\tp \) and \( \v = \x \), \( C(\varphi \otimes \v) = \y\tp\x \), the dot product. Chapter 10's inner product on \( \nR^n \) is this contraction composed with the identification of \( \nR^n \) with its dual — which is extra structure, and is why the dot product is not a contraction of \( V \otimes V \).

**Non-example by minimal change.** Replace \( \varphi(\v) \) by \( \varphi(\v)^2 \). The assignment \( (\varphi, \v) \mapsto \varphi(\v)^2 \) is not bilinear — doubling \( \v \) multiplies it by \( 4 \) — so no linear map on \( V^{*} \otimes V \) agrees with it, and @def-tensor-product does not apply. The exact clause that fails is linearity in each slot.

**Why one upper slot and one lower slot.** Contraction needs a functional *and* a vector: the functional supplies the mouth. There is no analogous map \( V \otimes V \to F \).

::: {.warning}
**There is no canonical contraction of two vectors.** A linear map \( V \otimes V \to F \) is the same thing as a bilinear form on \( V \) (@def-tensor-product with \( Z = F \)), and Chapter 13 spent a chapter on the fact that a vector space carries *many* bilinear forms and prefers none of them. Each basis of \( V \) supplies one, \( (\v, \w) \mapsto \sum_i \varphi^i(\v)\varphi^i(\w) \), and different bases supply different ones: on \( \nR^2 \) the standard basis gives the dot product, while \( ((1,0), (1,1)) \) gives a form under which \( (1,0) \) and \( (0,1) \) are not orthogonal. Only the pairing between \( V^{*} \) and \( V \) is free of charge.
:::

## Contraction is the trace

We can now say what the trace is.

::: {#thm-trace-is-contraction}
[The Trace Is a Contraction]

Let \( V \) be a finite-dimensional vector space over \( F \), and let
\[
\Theta \colon V^{*} \otimes V \to \cL(V)
\]
be the isomorphism of @thm-tensor-hom-iso. Then
\[
\tr\big(\Theta(\xi)\big) = C(\xi) \qquad \text{for every } \xi \in V^{*} \otimes V ,
\]
that is, \( \tr = C \circ \Theta^{-1} \) as maps \( \cL(V) \to F \).
:::

::: {.idea}
Both sides are linear in \( \xi \), so by @lem-determined-by-simple-tensors it is enough to check simple tensors. And \( \Theta(\varphi \otimes \v) \) is the rank-at-most-one map \( \u \mapsto \varphi(\u)\v \), whose trace can be read off from a single well-chosen basis: put \( \v \) first.
:::

::: {.proof}
Both \( \xi \mapsto \tr(\Theta(\xi)) \) and \( \xi \mapsto C(\xi) \) are linear, being composites of linear maps (@thm-trace-operator-properties for the first). By @lem-determined-by-simple-tensors it suffices to prove \( \tr(\Theta(\varphi \otimes \v)) = \varphi(\v) \) for all \( \varphi \in V^{*} \), \( \v \in V \).

Write \( R \coloneqq \Theta(\varphi \otimes \v) \), so \( R\u = \varphi(\u)\v \) for every \( \u \). If \( \v = \0 \), then \( R = 0 \) and \( \varphi(\v) = 0 \), so both sides vanish. Otherwise \( (\v) \) is a linearly independent list, so by @thm-basis-extension-general it extends to a basis \( \sB = (\u_1, \dots, \u_n) \) of \( V \) with \( \u_1 = \v \). For each \( j \),
\[
R\u_j = \varphi(\u_j)\,\v = \varphi(\u_j)\,\u_1 ,
\]
so column \( j \) of \( \mtx{R}{\sB}{\sB} \) has \( \varphi(\u_j) \) in row \( 1 \) and zeros below it (@def-matrix-of-linear-map). Hence the only non-zero diagonal entry is the one in position \( (1,1) \), equal to \( \varphi(\u_1) = \varphi(\v) \). By @def-trace-operator, \( \tr R = \varphi(\v) \), as required.
:::

**What has changed.** Chapter 3's definition named a basis and then had to prove that the answer survived a change of basis, using @thm-trace-similarity-invariant. Here nothing was named. The map \( C \) was manufactured by the universal property out of the evaluation pairing, which exists before any basis does, and \( \Theta \) was manufactured the same way. So basis-independence is not a theorem about \( C \circ \Theta^{-1} \); there is no basis in the construction to be independent of. Chapter 3's theorem is still true, and it is what makes the two descriptions agree — but it is now an observation about a *computation* of the trace, not part of its definition. The single basis used in the proof above was a convenience for reading off one number, not a choice the answer could depend on.

Two consequences come free. First, the trace of a rank-one map.

::: {#cor-trace-of-rank-one}
[Trace of a Rank-One Map]

Let \( V \) be finite-dimensional, \( \varphi \in V^{*} \) and \( \v \in V \), and let \( R \in \cL(V) \) be \( R\u = \varphi(\u)\v \). Then \( \tr R = \varphi(\v) \). In particular, with a basis \( \sB \) and its dual basis, \( \id_V = \Theta\big(\sum_i \varphi^i \otimes \v_i\big) \) and \( \tr \id_V = \sum_i \varphi^i(\v_i) = n \cdot 1 \).
:::

::: {.proof}
The first claim was proved inside @thm-trace-is-contraction. For the second, \( \Theta(\sum_i \varphi^i \otimes \v_i) \) sends \( \v_j \) to \( \sum_i \varphi^i(\v_j)\v_i = \v_j \), so it is \( \id_V \) (@thm-linear-transform-basis); applying \( C \) gives \( \sum_i \varphi^i(\v_i) = \sum_i 1 = n \cdot 1 \).
:::

Second, the promise made in §03: the trace of a tensor product of maps multiplies, and now we can see why. The key is that a functional on \( V \otimes W \) is built from one on each factor.

::: {#prp-dual-of-tensor}
[The Dual of a Tensor Product]

Let \( V \) and \( W \) be finite-dimensional over \( F \). There is a unique linear map
\[
\kappa \colon V^{*} \otimes W^{*} \to (V \otimes W)^{*},
\qquad
\kappa(\varphi \otimes \psi)(\v \otimes \w) = \varphi(\v)\,\psi(\w),
\]
and it is an isomorphism.
:::

::: {.proof}
For fixed \( \varphi, \psi \), the map \( (\v, \w) \mapsto \varphi(\v)\psi(\w) \) is bilinear, so @def-tensor-product produces a unique functional \( \varphi \cdot \psi \in (V \otimes W)^{*} \) with the stated values. The assignment \( (\varphi, \psi) \mapsto \varphi \cdot \psi \) is itself bilinear, since two functionals agreeing on all simple tensors are equal (@lem-determined-by-simple-tensors), so @def-tensor-product gives the unique linear \( \kappa \).

Let \( \sB = (\v_1, \dots, \v_n) \) and \( \sC = (\w_1, \dots, \w_m) \) be bases with dual bases \( (\varphi^i) \) and \( (\psi^j) \). Then \( \kappa(\varphi^i \otimes \psi^j)(\v_k \otimes \w_l) = \delta^i_k\delta^j_l \), so \( \kappa \) carries the basis \( (\varphi^i \otimes \psi^j) \) of \( V^{*} \otimes W^{*} \) (@thm-tensor-basis) to the dual basis of \( \sB \otimes \sC \) (@thm-dual-basis (a), which characterizes it by these values). A linear map carrying a basis to a basis is an isomorphism, by @thm-image-spanned-by-basis-images and @thm-rank-nullity.
:::

::: {#cor-trace-of-tensor-product}
[Why the Trace Multiplies]

Let \( V, W \) be finite-dimensional over \( F \), \( S \in \cL(V) \) and \( T \in \cL(W) \). Then \( \tr(S \otimes T) = \tr S \cdot \tr T \).
:::

::: {.proof}
Both \( (S, T) \mapsto \tr(S \otimes T) \) and \( (S, T) \mapsto \tr S \cdot \tr T \) are bilinear on \( \cL(V) \times \cL(W) \), by @prp-tensor-of-maps-algebra (a), (b) and @thm-trace-operator-properties. The maps of rank at most one span \( \cL(V) \), since \( \Theta \) is onto and simple tensors span \( V^{*} \otimes V \) (@prp-simple-tensors-span); likewise for \( \cL(W) \). So it suffices to check the identity when \( S = \Theta(\varphi \otimes \v) \) and \( T = \Theta(\psi \otimes \w) \).

For such \( S \) and \( T \) and any \( \a \otimes \b \in V \otimes W \),
\[
(S \otimes T)(\a \otimes \b) = \varphi(\a)\v \otimes \psi(\b)\w
= \kappa(\varphi \otimes \psi)(\a \otimes \b)\,(\v \otimes \w),
\]
so \( S \otimes T = \Theta\big(\kappa(\varphi \otimes \psi) \otimes (\v \otimes \w)\big) \) by @lem-determined-by-simple-tensors. By @thm-trace-is-contraction and @prp-dual-of-tensor,
\[
\tr(S \otimes T) = \kappa(\varphi \otimes \psi)(\v \otimes \w) = \varphi(\v)\psi(\w),
\]
which is \( \tr S \cdot \tr T \) by @cor-trace-of-rank-one.
:::

So the trace multiplies because *evaluation* multiplies: a functional on a tensor product is a product of functionals, and contraction is evaluation. Chapter 7 proved this by summing \( a_{ii}b_{kk} \) over all pairs (@thm-kronecker-rank-trace-det (b)), which is the same fact with the sum written out.

## Tensors with many slots

Contraction is not confined to one upper and one lower slot; it can be applied to a chosen pair inside a tensor with any number of them. First we name those tensors. Write
\[
V^{\otimes p} \coloneqq \underbrace{V \otimes \dots \otimes V}_{p}, \qquad V^{\otimes 0} \coloneqq F,
\]
which is unambiguous by @prp-tensor-associative.

::: {#def-tensor-type}
[Tensor of type \( (p, q) \)]

Let \( V \) be a vector space over \( F \) and \( p, q \ge 0 \). A **tensor of type \( (p, q) \)** on \( V \) is an element of
\[
T^{p}_{q}(V) \coloneqq V^{\otimes p} \otimes (V^{*})^{\otimes q} .
\]
The \( p \) copies of \( V \) are the **contravariant** slots and the \( q \) copies of \( V^{*} \) the **covariant** slots. The number \( p + q \) is the **rank** or **order** of the tensor.
:::

If \( \dim V = n \), then \( \dim T^p_q(V) = n^{p+q} \) by @thm-tensor-basis and @cor-dimension-dual-space. The small cases are all things we have met:

- \( T^0_0(V) = F \): scalars.
- \( T^1_0(V) = V \) and \( T^0_1(V) = V^{*} \): vectors and functionals.
- \( T^1_1(V) = V \otimes V^{*} \cong \cL(V) \): operators, by @thm-tensor-hom-iso together with the swap of @exr-tensor-products-of-maps-c3, which sends \( \v \otimes \varphi \) to \( \varphi \otimes \v \).
- \( T^0_2(V) \cong (V \otimes V)^{*} \) by @prp-dual-of-tensor, and a functional on \( V \otimes V \) is a bilinear form on \( V \) by @def-tensor-product. So a type \( (0, 2) \) tensor is exactly a bilinear form — the whole subject matter of Chapter 13.

::: {.warning}
**The word "rank" is overloaded here.** The rank of a tensor in the sense of @def-tensor-type is the number of slots, \( p + q \); it has nothing to do with \( \rank T \) for a linear map, nor with the smallest number of simple tensors needed to write an element. A type \( (1,1) \) tensor always has rank \( 2 \) in this sense, whatever the rank of the corresponding operator. Where confusion is possible we say **order**.
:::

Now the general contraction. Contracting slot \( a \) against slot \( b \) means feeding the \( b \)-th functional the \( a \)-th vector and keeping everything else.

::: {#def-contraction-slots}
[Contraction on a pair of slots]

Let \( V \) be a vector space over \( F \), let \( p, q \ge 1 \), and fix \( 1 \le a \le p \) and \( 1 \le b \le q \). The **contraction on slots \( a \) and \( b \)** is the unique linear map
\[
C^{a}_{b} \colon T^{p}_{q}(V) \to T^{p-1}_{q-1}(V)
\]
with, for all \( \v_1, \dots, \v_p \in V \) and \( \varphi^1, \dots, \varphi^q \in V^{*} \),
\[
\begin{aligned}
&C^{a}_{b}\big(\v_1 \otimes \dots \otimes \v_p \otimes \varphi^1 \otimes \dots \otimes \varphi^q\big) \\
&\qquad = \varphi^b(\v_a)\;\v_1 \otimes \dots \widehat{\v_a} \dots \otimes \v_p
\otimes \varphi^1 \otimes \dots \widehat{\varphi^b} \dots \otimes \varphi^q ,
\end{aligned}
\]
where a hat means that the factor is omitted.
:::

**Well-definedness.** The right-hand side is multilinear in the \( p + q \) arguments: each argument appears exactly once, either inside the scalar \( \varphi^b(\v_a) \) or as one factor of a tensor product, and both are linear in it. By @lem-multilinear-universal there is exactly one linear map on \( T^p_q(V) \) with these values. For \( p = q = 1 \) it lands in \( T^0_0(V) = F \) and sends \( \v \otimes \varphi \) to \( \varphi(\v) \): it is @def-contraction read on \( V \otimes V^{*} \) instead of \( V^{*} \otimes V \), that is, \( C \) composed with the swap of @exr-tensor-products-of-maps-c3. We use that identification silently from here on, and @thm-trace-is-contraction applies to either reading.

::: {.warning}
**Which slots you contract matters.** Let \( \dim V = 2 \) with basis \( (\v_1, \v_2) \) and dual basis \( (\varphi^1, \varphi^2) \), and take the type \( (2, 2) \) tensor
\[
t = \v_1 \otimes \v_2 \otimes \varphi^1 \otimes \varphi^2 .
\]
Then \( C^1_1(t) = \varphi^1(\v_1)\,\v_2 \otimes \varphi^2 = \v_2 \otimes \varphi^2 \), while \( C^1_2(t) = \varphi^2(\v_1)\,\v_2 \otimes \varphi^1 = 0 \). The two contractions of the same tensor differ, one of them being zero. There is no "the" contraction of a tensor of order \( \ge 3 \): the slots must be named.
:::

::: {.check}
Let \( \dim V = 3 \) with basis \( (\v_1, \v_2, \v_3) \) and dual basis \( (\varphi^1, \varphi^2, \varphi^3) \), and let
\[
t = \v_1 \otimes \varphi^1 + 2\,\v_2 \otimes \varphi^2 - \v_1 \otimes \varphi^3 \in T^1_1(V).
\]
Compute \( C^1_1(t) \), and say which operator \( t \) corresponds to.
:::

::: {.solution}
\( C^1_1(t) = \varphi^1(\v_1) + 2\varphi^2(\v_2) - \varphi^3(\v_1) = 1 + 2 - 0 = 3 \). The corresponding operator sends \( \v_1 \mapsto \v_1 \), \( \v_2 \mapsto 2\v_2 \), \( \v_3 \mapsto -\v_1 \), so its matrix in \( (\v_1, \v_2, \v_3) \) is \( \begin{pmatrix} 1 & 0 & -1 \\ 0 & 2 & 0 \\ 0 & 0 & 0 \end{pmatrix} \), of trace \( 3 \), in agreement with @thm-trace-is-contraction.
:::

Index notation, in the next section, makes contraction visibly what it looks like in physics: set an upper index equal to a lower one and sum.

## Exercises

### A. Check your understanding

:::: {#exr-contraction-and-trace-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the contraction \( C \colon V^{*} \otimes V \to F \), and say what makes it well defined.
2. State the relation between the trace and the contraction, with its hypothesis.
3. Explain why there is no canonical linear map \( V \otimes V \to F \).
4. For \( \dim V = 4 \), what is \( \dim T^2_3(V) \)?
5. True or false: for \( t \in T^2_2(V) \), the four contractions \( C^a_b(t) \) all agree. Justify your answer.
:::
::::

::: {.solution}
(a) \( C \) is the unique linear map with \( C(\varphi \otimes \v) = \varphi(\v) \) (@def-contraction). It is well defined because \( (\varphi, \v) \mapsto \varphi(\v) \) is bilinear, so @def-tensor-product produces exactly one such linear map.

(b) If \( V \) is **finite-dimensional**, then \( \tr(\Theta(\xi)) = C(\xi) \) for all \( \xi \in V^{*} \otimes V \), where \( \Theta \) is the isomorphism of @thm-tensor-hom-iso (@thm-trace-is-contraction).

(c) Such a map is the same thing as a bilinear form on \( V \), and a vector space has many bilinear forms with none distinguished; each basis produces a different one. Contraction works only because \( V^{*} \) comes with the evaluation pairing built in.

(d) \( 4^{2+3} = 4^5 = 1024 \).

(e) False. @def-contraction-slots's warning gives \( t = \v_1 \otimes \v_2 \otimes \varphi^1 \otimes \varphi^2 \) with \( C^1_1(t) = \v_2 \otimes \varphi^2 \ne 0 \) and \( C^1_2(t) = 0 \).
:::

### B. Practice

:::: {#exr-contraction-and-trace-b1}
[B1: Contracting a mixed tensor]

Let \( \dim V = 3 \) with basis \( \sB = (\v_1, \v_2, \v_3) \) and dual basis \( (\varphi^1, \varphi^2, \varphi^3) \). Let
\[
t = 2\,\v_1 \otimes \varphi^1 - \v_1 \otimes \varphi^2 + 3\,\v_2 \otimes \varphi^2 + \v_3 \otimes \varphi^1 - 4\,\v_3 \otimes \varphi^3 .
\]

::: {.enumerate options="label=(\alph*)"}
1. Write the matrix of the operator \( S \) corresponding to \( t \), in the basis \( \sB \).
2. Compute \( C^1_1(t) \) from @def-contraction-slots, and check it against \( \tr S \).
3. Compute \( \tr(S \otimes S) \) without writing down a \( 9 \times 9 \) matrix.
:::
::::

::: {.solution}
(a) The tensor \( \v_i \otimes \varphi^j \) corresponds to the operator \( \u \mapsto \varphi^j(\u)\v_i \), whose matrix is the matrix unit \( \E_{ij} \) (@thm-tensor-hom-iso). Adding up,
\[
\mtx{S}{\sB}{\sB} = \begin{pmatrix} 2 & -1 & 0 \\ 0 & 3 & 0 \\ 1 & 0 & -4 \end{pmatrix}.
\]

(b) \( C^1_1(t) = 2\varphi^1(\v_1) - \varphi^2(\v_1) + 3\varphi^2(\v_2) + \varphi^1(\v_3) - 4\varphi^3(\v_3) = 2 - 0 + 3 + 0 - 4 = 1 \), and the diagonal of the matrix in (a) sums to \( 2 + 3 - 4 = 1 \).

(c) By @cor-trace-of-tensor-product, \( \tr(S \otimes S) = (\tr S)^2 = 1 \).
:::

:::: {#exr-contraction-and-trace-b2}
[B2: Two contractions of one tensor]

Let \( \dim V = 2 \) with basis \( (\v_1, \v_2) \) and dual basis \( (\varphi^1, \varphi^2) \), and let
\[
t = \v_1 \otimes \varphi^1 \otimes \varphi^2 + \v_2 \otimes \varphi^2 \otimes \varphi^2 \in T^1_2(V).
\]
Compute \( C^1_1(t) \) and \( C^1_2(t) \), and state which space each lies in.
::::

::: {.solution}
Both lie in \( T^0_1(V) = V^{*} \). Contracting the single upper slot against the **first** lower slot,
\[
C^1_1(t) = \varphi^1(\v_1)\,\varphi^2 + \varphi^2(\v_2)\,\varphi^2 = \varphi^2 + \varphi^2 = 2\varphi^2 .
\]
Against the **second** lower slot, the remaining factor is the first functional:
\[
C^1_2(t) = \varphi^2(\v_1)\,\varphi^1 + \varphi^2(\v_2)\,\varphi^2 = 0 + \varphi^2 = \varphi^2 .
\]
So \( C^1_1(t) = 2\varphi^2 \ne \varphi^2 = C^1_2(t) \).
:::

:::: {#exr-contraction-and-trace-b3}
[B3: Which statements hold?]

Let \( V, W \) be finite-dimensional over \( F \). Determine which of the following hold. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( C(\xi) = 0 \) implies \( \xi = 0 \).
2. \( \tr(\Theta(\varphi \otimes \v)) = \varphi(\v) \) for all \( \varphi \in V^{*} \), \( \v \in V \).
3. Every element of \( T^0_2(V) \) is a bilinear form on \( V \), and conversely.
4. \( \tr(S \otimes T) = \tr(T \otimes S) \) for \( S \in \cL(V) \), \( T \in \cL(W) \).
5. \( C \colon V^{*} \otimes V \to F \) is surjective whenever \( V \ne \{\0\} \).
:::
::::

::: {.solution}
(a) Fails for \( \dim V \ge 2 \). With a basis and its dual, \( \xi = \varphi^1 \otimes \v_2 \ne 0 \) (@prp-simple-tensor-zero) but \( C(\xi) = \varphi^1(\v_2) = 0 \). Contraction is a functional, not an injection; its kernel has dimension \( n^2 - 1 \).

(b) Holds: @cor-trace-of-rank-one.

(c) Holds. By @prp-dual-of-tensor, \( T^0_2(V) = V^{*} \otimes V^{*} \cong (V \otimes V)^{*} \), and by @def-tensor-product the linear maps \( V \otimes V \to F \) correspond exactly to the bilinear maps \( V \times V \to F \), which are the bilinear forms of @def-bilinear-form.

(d) Holds: both equal \( \tr S \cdot \tr T \) by @cor-trace-of-tensor-product, the two products of scalars being equal.

(e) Holds. Take \( \v \ne \0 \); by @thm-functionals-separate-points there is \( \varphi \) with \( \varphi(\v) = 1 \), so \( C(c\,\varphi \otimes \v) = c \) for every \( c \in F \).
:::

### C. Going deeper

:::: {#exr-contraction-and-trace-c1}
[C1: Composition, in tensor language]

Let \( V \) be finite-dimensional over \( F \) and \( \Theta \colon V^{*} \otimes V \to \cL(V) \) the isomorphism of @thm-tensor-hom-iso.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \Theta(\varphi \otimes \v)\,\Theta(\psi \otimes \w) = \varphi(\w)\,\Theta(\psi \otimes \v) \) for all \( \varphi, \psi \in V^{*} \) and \( \v, \w \in V \). Recall that \( ST \) means first \( T \), then \( S \).
2. Hence compute \( \tr\big(\Theta(\varphi \otimes \v)\,\Theta(\psi \otimes \w)\big) \), and observe that the answer is unchanged when \( (\varphi, \v) \) and \( (\psi, \w) \) are exchanged.
3. Deduce that \( \tr(ST) = \tr(TS) \) for all \( S, T \in \cL(V) \).
:::
::::

::: {.solution}
(a) Both sides are operators on \( V \), so evaluate at an arbitrary \( \u \in V \). Applying \( \Theta(\psi \otimes \w) \) first gives \( \psi(\u)\w \), and then
\[
\Theta(\varphi \otimes \v)\big(\psi(\u)\w\big) = \psi(\u)\,\varphi(\w)\,\v ,
\]
using linearity of \( \Theta(\varphi \otimes \v) \). The right side gives \( \varphi(\w)\,\psi(\u)\,\v \), the same scalar times the same vector. Hence the two operators agree at every \( \u \).

(b) By (a) and @cor-trace-of-rank-one,
\[
\tr\big(\Theta(\varphi \otimes \v)\,\Theta(\psi \otimes \w)\big) = \varphi(\w)\,\psi(\v) .
\]
Exchanging \( (\varphi, \v) \) with \( (\psi, \w) \) turns this into \( \psi(\v)\,\varphi(\w) \), which is the same product of scalars.

(c) The maps \( (S, T) \mapsto \tr(ST) \) and \( (S, T) \mapsto \tr(TS) \) are bilinear on \( \cL(V) \times \cL(V) \), and the rank-one maps \( \Theta(\varphi \otimes \v) \) span \( \cL(V) \) (as \( \Theta \) is onto and simple tensors span, by @prp-simple-tensors-span). By (b) the two maps agree on such pairs, hence everywhere.
:::

:::: {#exr-contraction-and-trace-c2}
[C2: The contraction of the identity, over any field]

Let \( V \) be finite-dimensional over \( F \), \( n = \dim V \ge 1 \), and let \( \iota \in V^{*} \otimes V \) be the tensor with \( \Theta(\iota) = \id_V \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \iota = \sum_{i=1}^{n} \varphi^i \otimes \v_i \) for **every** basis \( \sB \) of \( V \) with dual basis \( \sB^{*} \). (This tensor is basis-free, though each expression for it is not.)
2. Prove that \( C(\iota) = n \cdot 1 \) in \( F \).
3. Over \( \nF_2 \) with \( n = 2 \), find a tensor \( \xi \ne \iota \) in \( V^{*} \otimes V \) with \( C(\xi) = C(\iota) \), and relate this to Chapter 3's observation that the trace does not determine the rank of a projection over \( \nF_2 \).
:::
::::

::: {.solution}
(a) By @cor-trace-of-rank-one, \( \Theta(\sum_i \varphi^i \otimes \v_i) = \id_V \) for any basis and its dual basis. Since \( \Theta \) is injective (@thm-tensor-hom-iso), all these tensors are equal, and each equals \( \iota \).

(b) \( C(\iota) = \sum_i \varphi^i(\v_i) = \sum_i 1 = n \cdot 1 \) by @def-dual-basis.

(c) Take \( \xi = 0 \). Then \( C(\xi) = 0 = 2 \cdot 1 = C(\iota) \) in \( \nF_2 \), while \( \xi \ne \iota \) because \( \Theta(\iota) = \id \ne 0 \). Under \( \Theta \) these are the identity and the zero operator, both projections, of ranks \( 2 \) and \( 0 \); this is exactly @thm-rank-equals-trace-projection's warning that over a field of characteristic \( 2 \) the integer \( \rank P \) cannot be recovered from \( \tr P \). The contraction is faithful to the tensor, but the field can be too small for the resulting scalar to distinguish them.
:::
