# The Adjoint

Chapter 4 attached to every linear map \( T \colon V \to W \) a dual map \( T' \colon W^{*} \to V^{*} \) running backwards between the dual spaces (@def-dual-map). An inner product puts a copy of the dual space back inside the space itself, by the Riesz correspondence of @thm-riesz-representation. Composing the two turns the backward map on functionals into a backward map on vectors, \( W \to V \). That map is the **adjoint** \( T^{*} \), and it is the single most useful construction in this chapter. This section builds it, computes its matrix, uses it to split both \( V \) and \( W \) into orthogonal pieces, and names the two classes of operators it singles out.

Throughout, \( F \) is \( \nR \) or \( \nC \), every inner product is linear in the first slot and conjugate-linear in the second, and every inner product space is finite-dimensional over \( F \) unless we say otherwise.

## Paying to cross the inner product

Here is the situation the adjoint answers. We have a linear map \( T \) and an inner product, and an expression like \( \inner{T\v}{\w} \) in which \( T \) sits in the first slot. Very often the argument needs \( T \) out of the way: we know something about \( \w \), or about the second slot, and the \( T \) is in the wrong place. Can we move it across?

For matrices the answer is already on the table. @lem-conjugate-transpose-pairing, proved in Section 4, says that for \( \A \in M_{m \times n}(F) \), \( \x \in F^n \) and \( \y \in F^m \),
\[
\inner{\A\x}{\y} = \inner{\x}{\A^{*}\y},
\]
with \( \A^{*} \) the conjugate transpose of @def-conjugate-transpose. The one-line reason is worth repeating, because it is the model for the whole section: writing \( \y^{*} \) for the row vector \( \conj{\y}\tp \), the standard inner product is the matrix product \( \inner{\x}{\y} = \y^{*}\x \), so \( \inner{\A\x}{\y} = (\y^{*}\A)\x = (\A^{*}\y)^{*}\x = \inner{\x}{\A^{*}\y} \). So a matrix does cross the inner product, and the price is a conjugate transpose. Over \( \nR \) the price is a transpose; over \( \nC \) a transpose and a conjugation.

*To move a map from the first slot to the second slot, you pay with a new map going the other way.*

That statement is about matrices and the standard inner product. The next theorem says the same map exists for every linear map between finite-dimensional inner product spaces, with no coordinates at all. Riesz does the work: the expression \( \inner{T\v}{\w} \), read as a function of \( \v \) with \( \w \) frozen, is a linear functional on \( V \), and @thm-riesz-representation says that every such functional is pairing against one fixed vector.

::: {#thm-adjoint-exists}
[Existence and Uniqueness of the Adjoint]

Let \( V \) and \( W \) be finite-dimensional inner product spaces over \( F \), and let \( T \in \cL(V, W) \). Then there is exactly one map \( T^{*} \colon W \to V \) such that
\[
\inner{T\v}{\w}_W = \inner{\v}{T^{*}\w}_V \qquad \text{for all } \v \in V,\ \w \in W,
\]
and this \( T^{*} \) is linear.
:::

::: {.idea}
Freeze \( \w \). Then \( \v \mapsto \inner{T\v}{\w} \) is a functional on \( V \), so Riesz hands us one vector that represents it; call it \( T^{*}\w \). That is the whole of existence, and it also gives uniqueness, since the Riesz vector is unique. Linearity is not part of the construction and has to be checked, and the way to check an identity between vectors is the signature move of this chapter: show the difference pairs to zero with everything, then pair it with itself.
:::

::: {.proof}
**Existence.** Fix \( \w \in W \) and define \( \varphi_{\w} \colon V \to F \) by \( \varphi_{\w}(\v) \coloneqq \inner{T\v}{\w} \). It is linear: for \( \v_1, \v_2 \in V \) and \( c \in F \),
\[
\varphi_{\w}(\v_1 + c\v_2) = \inner{T\v_1 + cT\v_2}{\w} = \inner{T\v_1}{\w} + c\inner{T\v_2}{\w},
\]
using the linearity of \( T \) and linearity in the **first** slot (@def-inner-product). Since \( V \) is finite-dimensional, @thm-riesz-representation gives a unique \( \u \in V \) with \( \varphi_{\w}(\v) = \inner{\v}{\u} \) for all \( \v \in V \). Define \( T^{*}\w \coloneqq \u \). By construction \( \inner{T\v}{\w} = \inner{\v}{T^{*}\w} \) for all \( \v \), which is the required identity.

**Uniqueness.** Suppose \( S \colon W \to V \) also satisfies \( \inner{T\v}{\w} = \inner{\v}{S\w} \) for all \( \v, \w \). Fix \( \w \). Then \( \inner{\v}{T^{*}\w - S\w} = 0 \) for every \( \v \in V \), by conjugate-additivity in the second slot. Taking \( \v = T^{*}\w - S\w \) gives \( \norm{T^{*}\w - S\w}^2 = 0 \), so \( T^{*}\w = S\w \) by positive definiteness (@def-inner-product). As \( \w \) was arbitrary, \( S = T^{*} \).

**Linearity.** Let \( \w_1, \w_2 \in W \) and \( c \in F \). For every \( \v \in V \),
\[
\begin{aligned}
\inner{\v}{T^{*}(\w_1 + c\w_2)} &= \inner{T\v}{\w_1 + c\w_2} = \inner{T\v}{\w_1} + \conj{c}\inner{T\v}{\w_2} \\
&= \inner{\v}{T^{*}\w_1} + \conj{c}\inner{\v}{T^{*}\w_2} = \inner{\v}{T^{*}\w_1 + cT^{*}\w_2},
\end{aligned}
\]
where the second and the last equalities use conjugate-linearity in the second slot. Hence \( \inner{\v}{T^{*}(\w_1 + c\w_2) - T^{*}\w_1 - cT^{*}\w_2} = 0 \) for every \( \v \), and pairing the right-hand vector with itself makes it \( \0 \). So \( T^{*} \) is linear. This proves the theorem.
:::

Notice where the two conjugations went. The scalar \( c \) came out of the second slot as \( \conj{c} \) and went back in as \( c \); the two conjugations cancel, which is exactly why \( T^{*} \) is linear and not conjugate-linear. Notice also that only \( V \) had to be finite-dimensional: the proof never uses a basis of \( W \). We keep both spaces finite-dimensional because the rest of the section does need it.

## The adjoint

The theorem produced an object attached to \( T \) and to the two inner products, and it is unique, so it deserves a name and a notation.

*The adjoint of \( T \) is the map you must apply on the other side of the inner product to leave the value unchanged.*

::: {#def-adjoint}
[Adjoint]

Let \( V \) and \( W \) be finite-dimensional inner product spaces over \( F \) and let \( T \in \cL(V, W) \). The **adjoint** of \( T \) is the unique linear map \( T^{*} \in \cL(W, V) \) satisfying
\[
\inner{T\v}{\w} = \inner{\v}{T^{*}\w} \qquad \text{for all } \v \in V \text{ and all } \w \in W .
\]
:::

In words, clause by clause:

- \( T^{*} \) goes **backwards**: its domain is the codomain of \( T \). If \( T \colon V \to W \) then \( T^{*} \colon W \to V \), like the dual map and unlike anything else we have attached to \( T \).
- The defining equation is an identity in **two** variables, and it must hold for **all** \( \v \) and **all** \( \w \). By linearity in the first slot and conjugate-linearity in the second, it is enough to check it when \( \v \) and \( \w \) range over bases of \( V \) and of \( W \), and that is usually how \( T^{*} \) gets computed.
- The left inner product lives in \( W \), the right one in \( V \). They are different inner products; only the notation hides it.
- The definition mentions no basis, but it does mention the two inner products. Change an inner product and \( T^{*} \) changes.

::: {#exm-adjoint-matrix-maps}
[Four Adjoints]

Compute the adjoint in each case. In (a) and (b) the spaces carry the standard inner product; in (c) and (d), \( V \) and \( W \) are arbitrary finite-dimensional inner product spaces.

::: {.enumerate options="label=(\alph*)"}
1. \( T_{\A} \colon \nC^3 \to \nC^2 \) for \( \A = \begin{pmatrix} 1 + i & 0 & 2 \\ i & 1 & -i \end{pmatrix} \).
2. The forward shift \( S \colon F^3 \to F^3 \), \( S(x_1, x_2, x_3) = (0, x_1, x_2) \).
3. \( \id_V \) and the zero map \( V \to W \).
4. The orthogonal projection \( P_U \colon V \to V \) onto a subspace \( U \subseteq V \).
:::
:::

::: {.solution}
(a) By @lem-conjugate-transpose-pairing, \( \inner{\A\x}{\y} = \inner{\x}{\A^{*}\y} \) for all \( \x, \y \), which is the defining identity of the adjoint; so \( (T_{\A})^{*} = T_{\A^{*}} \) for every matrix, by uniqueness in @thm-adjoint-exists. Here
\[
\A^{*} = \begin{pmatrix} 1 - i & -i \\ 0 & 1 \\ 2 & i \end{pmatrix},
\]
so \( T_{\A}^{*}(y_1, y_2) = \bigl((1 - i)y_1 - iy_2,\ y_2,\ 2y_1 + iy_2\bigr) \).

(b) Directly from the definition, for \( \x, \y \in F^3 \),
\[
\inner{S\x}{\y} = 0 \cdot \conj{y_1} + x_1\conj{y_2} + x_2\conj{y_3},
\qquad
\inner{\x}{(y_2, y_3, 0)} = x_1\conj{y_2} + x_2\conj{y_3} + x_3 \cdot 0 .
\]
The two agree for all \( \x \) and \( \y \).
So \( S^{*} \) is the **backward** shift \( S^{*}(y_1, y_2, y_3) = (y_2, y_3, 0) \). The forward shift pushes coordinates up; its adjoint pushes them down and drops the one that falls off the end.

(c) \( \inner{\id_V\v}{\w} = \inner{\v}{\w} = \inner{\v}{\id_V\w} \), so \( (\id_V)^{*} = \id_V \). For the zero map, \( \inner{0\v}{\w} = 0 = \inner{\v}{\0} \) for every \( \w \), so \( 0^{*} = 0 \), the zero map \( W \to V \). These are the degenerate cases, and they say the adjoint fixes what should be fixed.

(d) By @thm-projection-formula (b), \( \inner{P_U\u}{\v} = \inner{\u}{P_U\v} \) for all \( \u, \v \in V \). Since \( P_U \) is an operator on \( V \), this is exactly the defining identity for its own adjoint, so \( P_U^{*} = P_U \) by uniqueness in @thm-adjoint-exists.
:::

Part (d) is the first place where uniqueness earns its keep: we did not construct \( P_U^{*} \), we recognized an identity we already had and read the answer off it. That move recurs throughout the section.

::: {#exm-adjoint-differentiation}
[Differentiation on a Polynomial Space]

On \( V = \nR[x]_{\le 2} \) define \( \inner{p}{q} \coloneqq a_0b_0 + a_1b_1 + a_2b_2 \) for \( p = a_0 + a_1x + a_2x^2 \) and \( q = b_0 + b_1x + b_2x^2 \). (This is the standard inner product of \( \nR^3 \) transported by the coordinate map, so it is an inner product, and \( \sE = (1, x, x^2) \) is an orthonormal basis.) Find the adjoint of \( D \colon V \to V \), \( D(p) = p' \).
:::

::: {.solution}
For \( p, q \) as above, \( D(p) = a_1 + 2a_2x \), so
\[
\inner{Dp}{q} = a_1b_0 + 2a_2b_1 + 0 \cdot b_2 .
\]
We need \( D^{*}q = c_0 + c_1x + c_2x^2 \) with \( \inner{p}{D^{*}q} = a_0c_0 + a_1c_1 + a_2c_2 \) equal to the line above for **all** \( a_0, a_1, a_2 \). Comparing coefficients of \( a_0, a_1, a_2 \) gives \( c_0 = 0 \), \( c_1 = b_0 \), \( c_2 = 2b_1 \). Hence
\[
D^{*}(b_0 + b_1x + b_2x^2) = b_0x + 2b_1x^2 .
\]
So \( D^{*} \) raises degrees where \( D \) lowers them. It is not an antiderivative: the coefficient \( 2 \) and the discarded \( b_2 \) both say so.
:::

Here is a non-example by minimal change, and it explains the conjugate. On \( \nC^2 \), keep the standard inner product but try the plain transpose: is \( \inner{\A\x}{\y} = \inner{\x}{\A\tp\y} \)? Take \( \A = \begin{pmatrix} i & 0 \\ 0 & 0 \end{pmatrix} \), which is symmetric, so \( \A\tp = \A \), and take \( \x = \y = \e_1 \). Then \( \inner{\A\e_1}{\e_1} = \inner{(i, 0)}{(1, 0)} = i \), while \( \inner{\e_1}{\A\tp\e_1} = \inner{(1, 0)}{(i, 0)} = 1 \cdot \conj{i} = -i \). The two sides differ. Everything about the transpose still works — it is linear and it reverses products — but it fails the one clause that matters, the defining identity, and it fails it by a conjugation. Over \( \nR \) the conjugation is invisible and the transpose is correct.

**Why this definition.** We could have asked instead for a map \( R \) with \( \inner{R\w}{\v} = \inner{\w}{T\v} \). Conjugating @def-adjoint shows that \( R = T^{*} \) as well, so nothing new appears; the convention above is the one that reads left to right. The notation \( T^{*} \) matches the matrix notation \( \A^{*} \) of @exm-adjoint-matrix-maps (a), which is the point of the star. The word *adjoint* is unrelated to the *adjugate* of @def-adjugate; the collision of names is historical and the two objects have nothing to do with each other.

::: {.warning}
**The adjoint depends on the inner product, not on \( T \) alone.** On \( \nR^2 \) take \( T(x_1, x_2) = (x_2, 0) \). With the standard inner product, \( T^{*}(y_1, y_2) = (0, y_1) \). With the weighted inner product \( \inner{\x}{\y}_{w} \coloneqq x_1y_1 + 2x_2y_2 \), which is also an inner product, we need \( \inner{T\x}{\y}_{w} = x_2y_1 \) to equal \( \inner{\x}{S\y}_{w} = x_1(S\y)_1 + 2x_2(S\y)_2 \) for all \( \x \), which forces \( (S\y)_1 = 0 \) and \( (S\y)_2 = \tfrac12 y_1 \). So the adjoint is now \( \y \mapsto (0, \tfrac12 y_1) \), a different map. Writing \( T^{*} \) without saying which inner product is meant is as incomplete as writing a matrix of \( T \) without saying which basis.
:::

::: {.check}
Let \( T \in \cL(V, W) \) with \( T \neq 0 \). Can \( T^{*} = 0 \)?
:::

::: {.solution}
No. If \( T^{*} = 0 \) then \( \inner{T\v}{\w} = \inner{\v}{\0} = 0 \) for all \( \v, \w \). Taking \( \w = T\v \) gives \( \norm{T\v}^2 = 0 \), so \( T\v = \0 \) for every \( \v \), that is \( T = 0 \). This is the "pair it with itself" move again.
:::

Finally, the finite-dimensional hypothesis is not decoration.

::: {#exm-no-adjoint-infinite-dimensional}
[A Map With No Adjoint]

On \( V = \nR[x] \), all polynomials, define \( \inner{p}{q} \coloneqq \sum_{k \ge 0} a_kb_k \), a finite sum since the coefficients vanish eventually. Show that \( T \colon V \to V \), \( T(p) \coloneqq p(1) \cdot 1 \), has no adjoint.
:::

::: {.solution}
\( T \) is linear, being evaluation at \( 1 \) followed by multiplication by the constant polynomial \( 1 \). Suppose \( T^{*} \) existed. Apply the defining identity with \( p = x^k \) and with \( q = 1 \), the constant polynomial: since \( T(x^k) = 1 \),
\[
\inner{x^k}{T^{*}(1)} = \inner{T(x^k)}{1} = \inner{1}{1} = 1 \qquad \text{for every } k \ge 0 .
\]
But \( \inner{x^k}{T^{*}(1)} \) is the coefficient of \( x^k \) in \( T^{*}(1) \), so every coefficient of the polynomial \( T^{*}(1) \) equals \( 1 \). No polynomial has infinitely many non-zero coefficients, a contradiction. So \( T^{*} \) does not exist.

What failed is Riesz: the functional \( p \mapsto p(1) \) on \( \nR[x] \) is not pairing against any vector, precisely as in the infinite-dimensional discussion of Section 5.
:::

## Arithmetic of the adjoint

Starring behaves like transposing: it is additive, conjugate-homogeneous, order-reversing on products, and an involution.

::: {#thm-adjoint-properties}
[Properties of the Adjoint]

Let \( U, V, W \) be finite-dimensional inner product spaces over \( F \).

::: {.enumerate options="label=(\alph*)"}
1. For \( S, T \in \cL(V, W) \), \( (S + T)^{*} = S^{*} + T^{*} \).
2. For \( T \in \cL(V, W) \) and \( c \in F \), \( (cT)^{*} = \conj{c}\,T^{*} \).
3. For \( T \in \cL(U, V) \) and \( S \in \cL(V, W) \), \( (ST)^{*} = T^{*}S^{*} \).
4. \( T^{**} = T \) for every \( T \in \cL(V, W) \), and \( (\id_V)^{*} = \id_V \).
5. If \( T \in \cL(V, W) \) is invertible, then \( T^{*} \) is invertible and \( (T^{*})^{-1} = (T^{-1})^{*} \).
:::
:::

::: {.idea}
Each claim says that two maps \( W \to V \) agree. By the uniqueness in @thm-adjoint-exists, it is enough to check that the proposed right-hand side satisfies the defining identity of the left-hand side. So every proof is one chain of inner products, and nothing is ever solved for. Part (e) needs no chain at all: star the two equations \( T^{-1}T = \id_V \) and \( TT^{-1} = \id_W \) and use (c) and (d).
:::

::: {.proof}
Throughout, \( \v \) and \( \w \) denote arbitrary vectors of the relevant spaces, and each verification ends by invoking uniqueness in @thm-adjoint-exists.

(a) \( \inner{(S + T)\v}{\w} = \inner{S\v}{\w} + \inner{T\v}{\w} = \inner{\v}{S^{*}\w} + \inner{\v}{T^{*}\w} = \inner{\v}{(S^{*} + T^{*})\w} \), the last step by additivity in the second slot.

(b) \( \inner{(cT)\v}{\w} = c\inner{T\v}{\w} = c\inner{\v}{T^{*}\w} = \inner{\v}{\conj{c}\,T^{*}\w} \), where the last equality puts \( \conj{c} \) into the second slot, which conjugates it back to \( c \).

(c) For \( \u \in U \) and \( \w \in W \), using the defining identity for \( S \) and then for \( T \),
\[
\inner{(ST)\u}{\w} = \inner{S(T\u)}{\w} = \inner{T\u}{S^{*}\w} = \inner{\u}{T^{*}(S^{*}\w)} = \inner{\u}{(T^{*}S^{*})\w} .
\]

(d) The map \( T^{*} \in \cL(W, V) \) has its own adjoint \( T^{**} \in \cL(V, W) \), determined by \( \inner{T^{*}\w}{\v} = \inner{\w}{T^{**}\v} \). Conjugating the defining identity of \( T^{*} \) and using the conjugate symmetry of the inner product (@def-inner-product),
\[
\inner{T^{*}\w}{\v} = \conj{\inner{\v}{T^{*}\w}} = \conj{\inner{T\v}{\w}} = \inner{\w}{T\v} .
\]
So \( T \) satisfies the identity that defines \( T^{**} \), and \( T^{**} = T \). That \( (\id_V)^{*} = \id_V \) is @exm-adjoint-matrix-maps (c).

(e) Suppose \( T \) is invertible, with \( T^{-1} \in \cL(W, V) \). Applying (c) and (d) to \( T^{-1}T = \id_V \) and to \( TT^{-1} = \id_W \),
\[
T^{*}(T^{-1})^{*} = (T^{-1}T)^{*} = (\id_V)^{*} = \id_V, \qquad (T^{-1})^{*}T^{*} = (TT^{-1})^{*} = \id_W .
\]
Both composites are identities, so \( T^{*} \) is invertible with inverse \( (T^{-1})^{*} \) (@def-invertible-linear-map). This proves the theorem.
:::

Parts (a) and (b) say that \( T \mapsto T^{*} \) is **conjugate**-linear, not linear: over \( \nC \) it is the same half-twist that the Riesz map carries in @cor-riesz-isomorphism, and for the same reason. Part (c) is the order reversal familiar from transposes and from dual maps (@thm-dual-map-properties (b)). Part (d) says that starring is an involution, so no new maps appear by starring twice.

## The matrix of the adjoint

Now fix bases and compute. The conclusion is the one the opening computation suggests, **provided the bases are orthonormal**; the hypothesis is where all the content sits.

::: {#thm-matrix-of-adjoint}
[The Matrix of the Adjoint Is the Conjugate Transpose]

Let \( V \) and \( W \) be finite-dimensional inner product spaces over \( F \), let \( \sB = (\v_1, \dots, \v_n) \) be an **orthonormal** basis of \( V \) and \( \sC = (\w_1, \dots, \w_m) \) an **orthonormal** basis of \( W \), and let \( T \in \cL(V, W) \). Then
\[
\mtx{T^{*}}{\sC}{\sB} = \left(\mtx{T}{\sB}{\sC}\right)^{*} .
\]
:::

::: {.idea}
In an orthonormal basis a coordinate is an inner product (@thm-orthonormal-coordinates), so every matrix entry is an inner product, and the defining identity of \( T^{*} \) says precisely how those inner products are related. Write both entries out and compare.
:::

::: {.proof}
Write \( \A = \mtx{T}{\sB}{\sC} \) and \( \B = \mtx{T^{*}}{\sC}{\sB} \), of sizes \( m \times n \) and \( n \times m \). By @def-matrix-of-linear-map, the \( j \)-th column of \( \A \) holds the coordinates of \( T\v_j \) in \( \sC \), and by @thm-orthonormal-coordinates those coordinates are inner products:
\[
a_{ij} = \inner{T\v_j}{\w_i}, \qquad b_{ji} = \inner{T^{*}\w_i}{\v_j} .
\]
By conjugate symmetry and @def-adjoint,
\[
b_{ji} = \inner{T^{*}\w_i}{\v_j} = \conj{\inner{\v_j}{T^{*}\w_i}} = \conj{\inner{T\v_j}{\w_i}} = \conj{a_{ij}} .
\]
So \( \B \) is the matrix whose \( (j, i) \) entry is \( \conj{a_{ij}} \), which is \( \A^{*} \). This proves the theorem.
:::

Both hypotheses were used: orthonormality of \( \sC \) to read off \( a_{ij} \), orthonormality of \( \sB \) to read off \( b_{ji} \). Drop either one and the conclusion fails.

::: {.warning}
**The rule \( \mtx{T^{*}}{\sB}{\sB} = \bigl(\mtx{T}{\sB}{\sB}\bigr)^{*} \) is false in a basis that is not orthonormal.** The next example exhibits a two-dimensional counterexample with integer entries. The correct general statement involves the Gram matrix and is recorded in the remark after it.
:::

::: {#exm-adjoint-nonorthonormal-basis}
[The Transpose Rule Breaks]

Work in \( \nR^2 \) with the standard inner product and let \( T(x_1, x_2) = (x_2, 0) \). Let \( \sB = (\b_1, \b_2) \) with \( \b_1 = (1, 0) \) and \( \b_2 = (1, 1) \). Compute \( \mtx{T}{\sB}{\sB} \) and \( \mtx{T^{*}}{\sB}{\sB} \), and compare the second with the transpose of the first.
:::

::: {.solution}
First, \( \sB \) is a basis (two independent vectors in \( \nR^2 \)) but it is not orthonormal: \( \inner{\b_1}{\b_2} = 1 \neq 0 \) and \( \norm{\b_2} = \sqrt2 \).

By @exm-adjoint-matrix-maps (a) with \( \A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \), the adjoint is \( T^{*}(y_1, y_2) = (0, y_1) \).

*The matrix of \( T \).* \( T\b_1 = (0, 0) = 0\b_1 + 0\b_2 \) and \( T\b_2 = (1, 0) = 1\b_1 + 0\b_2 \), so
\[
\mtx{T}{\sB}{\sB} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \qquad \left(\mtx{T}{\sB}{\sB}\right)\tp = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} .
\]

*The matrix of \( T^{*} \).* \( T^{*}\b_1 = (0, 1) \) and \( T^{*}\b_2 = (0, 1) \). Solving \( (0, 1) = c_1(1, 0) + c_2(1, 1) \) gives \( c_2 = 1 \) and \( c_1 = -1 \), so both columns are \( (-1, 1) \):
\[
\mtx{T^{*}}{\sB}{\sB} = \begin{pmatrix} -1 & -1 \\ 1 & 1 \end{pmatrix} .
\]

The two displayed matrices are different: the transpose rule fails. A quick sanity check that nothing else went wrong: the traces are \( 0 \) and \( 0 \), and both matrices have rank \( 1 \), as they must, since \( \rank T = \rank T^{*} = 1 \).
:::

::: {.remark}
The correct rule. Let \( \G \) be the Gram matrix of \( \sB \), so \( g_{ij} = \inner{\b_j}{\b_i} \) (@def-gram-matrix), which is invertible because \( \sB \) is independent (@thm-gram-matrix-properties (c)). Then \( \mtx{T^{*}}{\sB}{\sB} = \G^{-1}\left(\mtx{T}{\sB}{\sB}\right)^{*}\G \). In the example, \( \G = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} \) and \( \G^{-1} = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix} \), and indeed
\[
\begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} = \begin{pmatrix} -1 & -1 \\ 1 & 1 \end{pmatrix} .
\]
When \( \sB \) is orthonormal, \( \G = \I \) and the rule collapses to @thm-matrix-of-adjoint. @exr-adjoints-c3 asks for the general rule.
:::

## The adjoint and the dual map

Two backward maps are now attached to \( T \): the dual map \( T' \colon W^{*} \to V^{*} \) of @def-dual-map, which needs no inner product and sends a functional \( f \) to \( f \circ T \), and the adjoint \( T^{*} \colon W \to V \), which does need one. The Riesz map converts one into the other. Nothing later in the book uses the comparison, so a reader who has not met Chapter 4 can take the square below on trust and move on to the next subsection.

Recall from @cor-riesz-isomorphism the Riesz map, the conjugate-linear bijection
\[
\Phi_V \colon V \to V^{*}, \qquad \Phi_V(\u) \coloneqq \inner{\cdot}{\u},
\]
and likewise \( \Phi_W \) for \( W \). The following square commutes: the two backward maps run horizontally, the two Riesz maps vertically, and the two routes from \( W \) to \( V^{*} \) agree, which is to say that
\[
\Phi_V \circ T^{*} = T' \circ \Phi_W .
\]
Both sides send a vector of \( W \) to a functional on \( V \), and evaluating each at a vector of \( V \) turns both into \( \inner{T\v}{\w} \); @exr-adjoints-c4 asks for those two lines.

\begin{center}
\begin{tikzpicture}[
    lab/.style={font=\small},
    arr/.style={->, thick, shorten >=3pt, shorten <=3pt}]
  \node (W)  at (0,2.1)   {$W$};
  \node (V)  at (4.4,2.1) {$V$};
  \node (Ws) at (0,0)     {$W^{*}$};
  \node (Vs) at (4.4,0)   {$V^{*}$};
  \draw[arr] (W)  -- (V)  node[midway, above, lab] {$T^{*}$};
  \draw[arr] (Ws) -- (Vs) node[midway, below, lab] {$T'$};
  \draw[arr] (W)  -- (Ws) node[midway, left,  lab] {$\Phi_W$};
  \draw[arr] (V)  -- (Vs) node[midway, right, lab] {$\Phi_V$};
  \node[lab, align=center] at (2.2,-1.15)
    {the vertical maps are the Riesz maps, one for each space};
\end{tikzpicture}
\end{center}

Read backwards, the identity says \( T^{*} = \Phi_V^{-1}T'\Phi_W \): transport a vector of \( W \) into \( W^{*} \), pull it back with the dual map, transport it back into \( V \). So the adjoint carries no information that \( T' \) does not already carry; what it carries is the inner product used to transport. The matrix statements match too. In dual bases the matrix of \( T' \) is the transpose of the matrix of \( T \) (@thm-matrix-of-dual-map); in orthonormal bases the matrix of \( T^{*} \) is the conjugate transpose (@thm-matrix-of-adjoint). The extra conjugation is the price of \( \Phi_V \) being conjugate-linear, and over \( \nR \) it disappears, which is why the two constructions are so easily confused there.

## The four fundamental subspaces

Chapter 2 attached four subspaces to a matrix: \( \col(\A) \) and \( \nul(\A) \) (@def-column-space, @def-null-space) together with \( \row(\A) \) (@def-row-space) and the null space of the transpose. Chapter 4 related two of them, with @thm-row-space-annihilates-null-space: the row space of \( \A \) **is** the annihilator of \( \nul(\A) \), so every linear equation satisfied by the solution set is a combination of the given ones. That statement lived in the dual space, and @def-annihilator carried a warning with it: over a general field the annihilator has no right to be pictured as a perpendicular. With an inner product, it does. The four subspaces become two orthogonal splittings, one in each of the two spaces.

::: {#thm-four-subspaces-orthogonal}
[The Four Fundamental Subspaces]

Let \( V, W \) be finite-dimensional inner product spaces over \( F \) and let \( T \in \cL(V, W) \). Then

::: {.enumerate options="label=(\alph*)"}
1. \( \ker T^{*} = (\im T)^{\perp} \);
2. \( \im T^{*} = (\ker T)^{\perp} \);
3. \( V = \ker T \oplus \im T^{*} \);
4. \( W = \im T \oplus \ker T^{*} \).
:::
:::

::: {.idea}
Only (a) needs an argument, and it is one chain of equivalences: \( T^{*}\w = \0 \) says a vector is zero, so pair it with everything, and the defining identity turns "everything" into "everything in the image of \( T \)". Then (b) is (a) applied to \( T^{*} \), using \( T^{**} = T \), and complemented with \( (U^{\perp})^{\perp} = U \). Parts (c) and (d) are then just the orthogonal decomposition theorem.
:::

::: {.proof}
(a) Let \( \w \in W \). Then
\[
\begin{aligned}
\w \in \ker T^{*} \iff T^{*}\w = \0 &\iff \inner{\v}{T^{*}\w} = 0 \text{ for all } \v \in V \\
&\iff \inner{T\v}{\w} = 0 \text{ for all } \v \in V \iff \w \in (\im T)^{\perp} .
\end{aligned}
\]
The second equivalence is non-degeneracy: forwards it is immediate, and backwards we take \( \v = T^{*}\w \) and get \( \norm{T^{*}\w}^2 = 0 \). The third is @def-adjoint. The fourth is @def-orthogonal-complement together with conjugate symmetry, since \( \inner{T\v}{\w} = 0 \) if and only if \( \inner{\w}{T\v} = 0 \), and the vectors \( T\v \) are exactly the elements of \( \im T \). Every step is reversible, so both inclusions come at once.

(b) Apply (a) to \( T^{*} \in \cL(W, V) \) in place of \( T \). Since \( T^{**} = T \) by @thm-adjoint-properties (d), this reads \( \ker T = (\im T^{*})^{\perp} \). Taking orthogonal complements and using \( (U^{\perp})^{\perp} = U \) for a subspace \( U \) of a finite-dimensional space (@thm-orthogonal-decomposition (b)),
\[
(\ker T)^{\perp} = \bigl((\im T^{*})^{\perp}\bigr)^{\perp} = \im T^{*} .
\]

(c) \( \ker T \) is a subspace of \( V \) (@thm-prop-kernel), so \( V = \ker T \oplus (\ker T)^{\perp} \) by @thm-orthogonal-decomposition (a), and \( (\ker T)^{\perp} = \im T^{*} \) by (b).

(d) Likewise \( W = \im T \oplus (\im T)^{\perp} \) by @thm-orthogonal-decomposition (a), and \( (\im T)^{\perp} = \ker T^{*} \) by (a). This proves the theorem.
:::

For a matrix \( \A \in M_{m \times n}(F) \) with the standard inner products, \( T_{\A}^{*} = T_{\A^{*}} \), so the theorem reads
\[
\nul(\A^{*}) = \col(\A)^{\perp}, \qquad \col(\A^{*}) = \nul(\A)^{\perp},
\]
with \( F^m = \col(\A) \oplus \nul(\A^{*}) \) and \( F^n = \nul(\A) \oplus \col(\A^{*}) \). Over \( \nR \) the columns of \( \A\tp \) are the rows of \( \A \) turned into vectors, so the second identity is the promised statement that **the row space and the null space are orthogonal complements of each other** in \( \nR^n \). This is @thm-row-space-annihilates-null-space with the annihilator replaced by the orthogonal complement, exactly as @cor-riesz-isomorphism licenses; and taking dimensions returns Rank–Nullity for matrices (@thm-rank-nullity-matrix) one more time. Section 4 proved the identity \( \nul(\A)^{\perp} = \col(\A^{*}) \) directly, because the minimum-norm solution needed it; the theorem above is that computation done once for all four subspaces and for maps rather than matrices.

::: {#exm-four-subspaces-matrix}
[All Four Subspaces of a 3 × 3 Matrix]

For \( \A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 2 & 1 \end{pmatrix} \) over \( \nR \), find bases of the four subspaces and verify the two orthogonality statements.
:::

::: {.solution}
Row three is the sum of rows one and two, and rows one and two are independent, so \( \rank \A = 2 \) and \( \row(\A) \) has the basis \( (1, 1, 0), (0, 1, 1) \) (written as vectors).

*Null space.* \( \A\x = \0 \) reduces to \( x_1 + x_2 = 0 \) and \( x_2 + x_3 = 0 \), so \( \nul(\A) = \Span\bigl((1, -1, 1)\bigr) \), of dimension \( 1 = 3 - 2 \), as @thm-rank-nullity-matrix requires.

*Orthogonality in the domain.* \( (1, 1, 0) \cdot (1, -1, 1) = 0 \) and \( (0, 1, 1) \cdot (1, -1, 1) = 0 \). So \( \row(\A) \perp \nul(\A) \), and since \( 2 + 1 = 3 \) the two are complementary: \( \nul(\A)^{\perp} = \row(\A) \).

*Column space.* Columns one and two are independent and column three is column two minus column one, so \( \col(\A) = \Span\bigl((1, 0, 1), (1, 1, 2)\bigr) \).

*Null space of the transpose.* \( \A\tp\y = \0 \) reads \( y_1 + y_3 = 0 \), \( y_1 + y_2 + 2y_3 = 0 \), \( y_2 + y_3 = 0 \), giving \( \nul(\A\tp) = \Span\bigl((-1, -1, 1)\bigr) \).

*Orthogonality in the codomain.* \( (1, 0, 1) \cdot (-1, -1, 1) = 0 \) and \( (1, 1, 2) \cdot (-1, -1, 1) = 0 \), and \( 2 + 1 = 3 \), so \( \col(\A)^{\perp} = \nul(\A\tp) \).
:::

::: {#cor-rank-adjoint}
[Rank of the Adjoint]

Let \( V, W \) be finite-dimensional inner product spaces over \( F \) and \( T \in \cL(V, W) \). Then

::: {.enumerate options="label=(\alph*)"}
1. \( \rank T^{*} = \rank T \);
2. \( \ker(T^{*}T) = \ker T \), and consequently \( \rank(T^{*}T) = \rank T \).
:::
:::

::: {.proof}
(a) By @thm-four-subspaces-orthogonal (b) and a dimension count,
\[
\rank T^{*} = \dim \im T^{*} = \dim (\ker T)^{\perp} = \dim V - \nullity T = \rank T,
\]
the middle equality by @thm-orthogonal-decomposition (c) and the last by the Rank–Nullity Theorem (@thm-rank-nullity).

(b) \( (\supseteq) \) If \( T\v = \0 \) then \( T^{*}T\v = T^{*}\0 = \0 \). \( (\subseteq) \) Suppose \( T^{*}T\v = \0 \). Then
\[
\norm{T\v}^2 = \inner{T\v}{T\v} = \inner{\v}{T^{*}T\v} = \inner{\v}{\0} = 0,
\]
so \( T\v = \0 \). Hence the kernels agree. Both \( T^{*}T \) and \( T \) are defined on \( V \), so Rank–Nullity gives \( \rank(T^{*}T) = \dim V - \nullity(T^{*}T) = \dim V - \nullity T = \rank T \).
:::

Part (a) is a fourth proof that row rank equals column rank, after the three of Chapters 2, 3 and 4: for a real matrix it says \( \rank \A\tp = \rank \A \). Part (b) is the engine of the normal equations: it is why \( \A^{*}\A \) is invertible exactly when \( \A \) has independent columns, which is the hypothesis in @cor-least-squares-unique.

::: {.check}
Let \( T \in \cL(V, W) \) with \( \dim V = 4 \), \( \dim W = 7 \) and \( \rank T = 3 \). What are \( \dim \ker T^{*} \) and \( \dim \im T^{*} \)?
:::

::: {.solution}
\( \rank T^{*} = 3 \) by @cor-rank-adjoint (a), so \( \dim \im T^{*} = 3 \); and \( T^{*} \colon W \to V \) with \( \dim W = 7 \), so \( \dim \ker T^{*} = 7 - 3 = 4 \). The same number comes from @thm-four-subspaces-orthogonal (a): \( \dim (\im T)^{\perp} = 7 - 3 = 4 \).
:::

## Self-adjoint and normal operators

For an operator \( T \in \cL(V) \), the adjoint lives in the same space \( \cL(V) \), so we may compare \( T \) with \( T^{*} \). Two comparisons matter, and everything in the next chapter rests on them.

*A self-adjoint operator is one that costs nothing to move across the inner product.*

::: {#def-self-adjoint}
[Self-adjoint Operator]

An operator \( T \in \cL(V) \) on a finite-dimensional inner product space is **self-adjoint** if \( T^{*} = T \), that is, if
\[
\inner{T\u}{\v} = \inner{\u}{T\v} \qquad \text{for all } \u, \v \in V .
\]
The matrix counterpart is the **Hermitian** matrix of @def-conjugate-transpose, \( \A^{*} = \A \); over \( \nR \) this says \( \A\tp = \A \), and the matrix is **symmetric**.
:::

In words: \( T^{*} \) is not a new map but \( T \) over again, so \( T \) must be an **operator**, with the same space and the same inner product on both sides; and the displayed identity is the defining identity of @def-adjoint with \( T^{*} \) rewritten as \( T \), still required for **all** \( \u \) and **all** \( \v \).

By @thm-matrix-of-adjoint, an operator on a finite-dimensional inner product space is self-adjoint exactly when its matrix in one (equivalently every) orthonormal basis is Hermitian. Three examples to keep in mind: the orthogonal projection \( P_U \) onto any subspace, self-adjoint by @exm-adjoint-matrix-maps (d), which is the geometric case; on \( \nR^2 \), the map of the symmetric \( \A = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} \), where conjugation does nothing and \( \A^{*} = \A\tp = \A \); and on \( \nC^2 \), the map of the Hermitian \( \A = \begin{pmatrix} 2 & 1 + i \\ 1 - i & 3 \end{pmatrix} \), where transposing swaps the two off-diagonal entries and conjugating swaps them back, while the diagonal is real and survives both.

Here is a non-example by minimal change: keep the shape and move the conjugate. The matrix \( \B = \begin{pmatrix} 2 & 1 + i \\ 1 + i & 3 \end{pmatrix} \) is **symmetric**, \( \B\tp = \B \), but \( \B^{*} = \begin{pmatrix} 2 & 1 - i \\ 1 - i & 3 \end{pmatrix} \neq \B \), so the clause \( T^{*} = T \) fails. It fails visibly at \( \u = \e_1 \) and \( \v = \e_2 \): \( \inner{\B\e_1}{\e_2} = 1 + i \), while \( \inner{\e_1}{\B\e_2} = \conj{1 + i} = 1 - i \). Over \( \nC \), self-adjointness means Hermitian, never merely symmetric.

Two more self-adjoint operators come for free: the combination \( D + D^{*} \) of @exm-adjoint-differentiation, and \( T^{*}T \) for any \( T \), since \( (T^{*}T)^{*} = T^{*}T^{**} = T^{*}T \) by @thm-adjoint-properties (c) and (d).

*An operator is normal when it and its adjoint may be applied in either order.*

::: {#def-normal-operator}
[Normal Operator]

An operator \( T \in \cL(V) \) on a finite-dimensional inner product space is **normal** if it commutes with its adjoint:
\[
T^{*}T = TT^{*} .
\]
:::

In words: normality is one equation between two operators on \( V \), with no vectors and no quantifiers in it. It does not ask that \( T \) and \( T^{*} \) be equal, only that their order may be swapped, so it is strictly weaker than self-adjointness.

Four examples, widening as they go. Every self-adjoint operator is normal, since then both sides are \( T^2 \). So is every invertible \( T \) with \( T^{-1} = T^{*} \) — Section 7 calls these unitary — since then both sides are \( \id_V \); the quarter-turn of \( \nR^2 \), with matrix \( \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \) in the standard basis, is one, and it is not self-adjoint. On \( \nC^2 \) the operator with matrix \( i\I \) satisfies \( (i\I)^{*} = -i\I \) by @thm-adjoint-properties (b), which commutes with \( i\I \) but is not equal to it: normal and not self-adjoint. Widest of all, every diagonal matrix \( \D = \diag(d_1, \dots, d_n) \) is normal, since \( \D^{*}\D = \D\D^{*} = \diag(\lvert d_1 \rvert^2, \dots, \lvert d_n \rvert^2) \).

A non-example by minimal change: take the diagonal matrix \( \diag(1, 0) \) and slide its non-zero entry off the diagonal. The Jordan block \( \J_2(0) = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) on \( \nC^2 \) has
\[
\J_2(0)^{*}\J_2(0) = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix},
\qquad
\J_2(0)\J_2(0)^{*} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix},
\]
and the two differ. The \( (1, 1) \) entries say what went wrong. Writing \( T \) for the map of \( \J_2(0) \), the \( (1, 1) \) entry of the first matrix is \( \inner{T^{*}T\e_1}{\e_1} = \norm{T\e_1}^2 = 0 \) and that of the second is \( \inner{TT^{*}\e_1}{\e_1} = \norm{T^{*}\e_1}^2 = 1 \), so \( \norm{T\e_1} \neq \norm{T^{*}\e_1} \): the operator kills \( \e_1 \) and its adjoint stretches it to a unit vector.

Over \( \nC \), normality is the weakest hypothesis under which the spectral theorem holds, and that is its reason for existing. Chapter 11 will show that the diagonal example is already the general one.

The facts available now, before any eigenvalue theory, are the ones that follow straight from the definition.

::: {#prp-self-adjoint-immediate}
[First Properties of Self-adjoint Operators]

Let \( T \in \cL(V) \) be self-adjoint on a finite-dimensional inner product space \( V \) over \( F \).

::: {.enumerate options="label=(\alph*)"}
1. \( \inner{T\v}{\v} \in \nR \) for every \( \v \in V \), even when \( F = \nC \).
2. If \( \sB \) is an orthonormal basis of \( V \), the diagonal entries of \( \mtx{T}{\sB}{\sB} \) are real.
3. \( T \) is normal.
:::
:::

::: {.proof}
(a) By conjugate symmetry (@def-inner-product) and self-adjointness,
\[
\conj{\inner{T\v}{\v}} = \inner{\v}{T\v} = \inner{T\v}{\v} .
\]
A complex number equal to its own conjugate is real.

(b) Let \( \sB = (\v_1, \dots, \v_n) \) be orthonormal. By @thm-orthonormal-coordinates the \( i \)-th coordinate of \( T\v_i \) is \( \inner{T\v_i}{\v_i} \), so the \( (i, i) \) entry of \( \mtx{T}{\sB}{\sB} \) is \( a_{ii} = \inner{T\v_i}{\v_i} \), which is real by (a).

(c) \( T^{*}T = TT = TT^{*} \).
:::

Part (a) is the first hint of the spectral theorem. If \( T\v = \lambda\v \) with \( \v \neq \0 \), then \( \inner{T\v}{\v} = \lambda\norm{\v}^2 \), and since the left side is real and \( \norm{\v}^2 \) is a positive real, \( \lambda \) must be real: a self-adjoint operator has no non-real eigenvalues. Chapter 11 turns this observation into the spectral theorems: a self-adjoint operator has an orthonormal basis of eigenvectors, with real eigenvalues; on a complex space the operators with an orthonormal basis of eigenvectors are exactly the normal ones, and on a real space exactly the self-adjoint ones. None of that is proved here, and none of it is used before then; but all of it is built from the adjoint and the orthogonal geometry of this chapter.

::: {.warning}
**"Self-adjoint" cannot be read off an arbitrary basis.** Being self-adjoint is a property of \( T \) together with the inner product, and the Hermitian test applies only in an **orthonormal** basis. The operator \( T(x_1, x_2) = (x_2, 0) \) of @exm-adjoint-nonorthonormal-basis is not self-adjoint, and its matrix in the standard orthonormal basis, \( \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \), is correctly non-symmetric. But the self-adjoint operator \( P(x_1, x_2) = (x_1, 0) \), the orthogonal projection onto the first axis, has the **non**-symmetric matrix \( \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix} \) in the basis \( \sB \) of that example, since \( P\b_1 = \b_1 \) and \( P\b_2 = (1, 0) = \b_1 \). A non-symmetric matrix is evidence of nothing until the basis is known to be orthonormal.
:::

## Exercises

### A. Check your understanding

::: {#exr-adjoints-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the defining property of the adjoint \( T^{*} \) of \( T \in \cL(V, W) \), including the domain and codomain of \( T^{*} \) and all quantifiers.
2. Which hypothesis of @thm-adjoint-exists is used to produce \( T^{*} \), and which theorem supplies it?
3. True or false: \( (cT)^{*} = cT^{*} \) for every scalar \( c \). Justify your answer.
4. State the hypothesis needed for \( \mtx{T^{*}}{\sC}{\sB} = \bigl(\mtx{T}{\sB}{\sC}\bigr)^{*} \), and say what goes wrong without it.
5. True or false: \( \ker T^{*} = (\ker T)^{\perp} \). Justify your answer.
6. Give an example of a normal operator that is not self-adjoint.
:::
:::

::: {.solution}
(a) For \( T \colon V \to W \), the adjoint is the unique \( T^{*} \colon W \to V \) with \( \inner{T\v}{\w} = \inner{\v}{T^{*}\w} \) for **all** \( \v \in V \) and **all** \( \w \in W \) (@def-adjoint).

(b) Finite-dimensionality of \( V \), which is what @thm-riesz-representation needs in order to represent the functional \( \v \mapsto \inner{T\v}{\w} \).

(c) False: \( (cT)^{*} = \conj{c}\,T^{*} \) (@thm-adjoint-properties (b)). Over \( \nR \) the two agree; over \( \nC \) take \( T = \id \) and \( c = i \), so that \( (i\,\id)^{*} = -i\,\id \neq i\,\id \).

(d) Both bases must be orthonormal (@thm-matrix-of-adjoint). Without it the rule fails: @exm-adjoint-nonorthonormal-basis has \( \bigl(\mtx{T}{\sB}{\sB}\bigr)\tp = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \) but \( \mtx{T^{*}}{\sB}{\sB} = \begin{pmatrix} -1 & -1 \\ 1 & 1 \end{pmatrix} \).

(e) False. The correct statements are \( \ker T^{*} = (\im T)^{\perp} \) and \( \im T^{*} = (\ker T)^{\perp} \) (@thm-four-subspaces-orthogonal). The two sides need not even live in the same space when \( V \neq W \).

(f) \( T = i\,\id \) on \( \nC^2 \): \( T^{*} = -i\,\id \) commutes with \( T \), but \( T^{*} \neq T \).
:::

### B. Practice

::: {#exr-adjoints-b1}
[B1: Adjoints of matrix maps]

Let \( \A = \begin{pmatrix} 1 + i & 0 & 2 \\ i & 1 & -i \end{pmatrix} \) and \( \B = \begin{pmatrix} 0 & 1 \\ i & 0 \end{pmatrix} \), acting between the complex spaces \( \nC^3 \xrightarrow{\ T_{\A}\ } \nC^2 \xrightarrow{\ T_{\B}\ } \nC^2 \) with the standard inner products.

::: {.enumerate options="label=(\alph*)"}
1. Write down \( T_{\A}^{*} \) and \( T_{\B}^{*} \) as matrix maps.
2. Compute the matrices of \( T_{\B}T_{\A} \) and of \( (T_{\B}T_{\A})^{*} \), and verify \( (T_{\B}T_{\A})^{*} = T_{\A}^{*}T_{\B}^{*} \) by direct computation.
3. Verify that \( T_{\B} \) is not self-adjoint, and determine whether it is normal.
:::
:::

::: {.solution}
(a) \( T_{\A}^{*} = T_{\A^{*}} \) and \( T_{\B}^{*} = T_{\B^{*}} \) (@exm-adjoint-matrix-maps (a)), with
\[
\A^{*} = \begin{pmatrix} 1 - i & -i \\ 0 & 1 \\ 2 & i \end{pmatrix}, \qquad \B^{*} = \begin{pmatrix} 0 & -i \\ 1 & 0 \end{pmatrix} .
\]

(b) \( \B\A = \begin{pmatrix} i & 1 & -i \\ i - 1 & 0 & 2i \end{pmatrix} \), so
\[
(\B\A)^{*} = \begin{pmatrix} -i & -i - 1 \\ 1 & 0 \\ i & -2i \end{pmatrix} .
\]
On the other side,
\[
\A^{*}\B^{*} = \begin{pmatrix} 1 - i & -i \\ 0 & 1 \\ 2 & i \end{pmatrix}\begin{pmatrix} 0 & -i \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} -i & -i(1 - i) \\ 1 & 0 \\ i & -2i \end{pmatrix},
\]
and \( -i(1 - i) = -i + i^2 = -1 - i \). The two matrices agree, as @thm-adjoint-properties (c) predicts.

(c) \( \B^{*} \neq \B \), since the \( (1, 2) \) entries are \( -i \) and \( 1 \). But
\[
\B^{*}\B = \begin{pmatrix} 0 & -i \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 0 & 1 \\ i & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ i & 0 \end{pmatrix}\begin{pmatrix} 0 & -i \\ 1 & 0 \end{pmatrix} = \B\B^{*},
\]
so \( T_{\B} \) is normal (@def-normal-operator) and not self-adjoint.
:::

::: {#exr-adjoints-b2}
[B2: Adjoints on a polynomial space]

Let \( V = \nR[x]_{\le 2} \) and \( W = \nR[x]_{\le 3} \), each with the coefficient inner product of @exm-adjoint-differentiation, so that \( \sE = (1, x, x^2) \) and \( \sF = (1, x, x^2, x^3) \) are orthonormal bases.

::: {.enumerate options="label=(\alph*)"}
1. Find the adjoint of \( M \colon V \to W \), \( M(p) = xp \).
2. Find the adjoint of \( E \colon V \to \nR \), \( E(p) = p(1) \), where \( \nR \) carries \( \inner{s}{t} = st \). (Compare @thm-riesz-representation.)
3. Verify \( \rank M^{*} = \rank M \) directly.
:::
:::

::: {.solution}
(a) \( M(1) = x \), \( M(x) = x^2 \), \( M(x^2) = x^3 \), so in the two orthonormal bases
\[
\mtx{M}{\sE}{\sF} = \begin{pmatrix} 0 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix},
\qquad
\mtx{M^{*}}{\sF}{\sE} = \bigl(\mtx{M}{\sE}{\sF}\bigr)\tp = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}
\]
by @thm-matrix-of-adjoint. Hence \( M^{*}(c_0 + c_1x + c_2x^2 + c_3x^3) = c_1 + c_2x + c_3x^2 \): delete the constant term and divide by \( x \).

(b) \( E \) is linear and \( E(a_0 + a_1x + a_2x^2) = a_0 + a_1 + a_2 \). For \( t \in \nR \) we need \( \inner{p}{E^{*}t} = \inner{E p}{t} = (a_0 + a_1 + a_2)t \) for all \( p \), so comparing coefficients of \( a_0, a_1, a_2 \) gives \( E^{*}(t) = t(1 + x + x^2) \). In particular \( E^{*}(1) = 1 + x + x^2 \) is the Riesz vector of the evaluation functional at \( 1 \).

(c) \( M \) is injective, since \( xp = 0 \) forces \( p = 0 \), so \( \rank M = \dim V = 3 \) by @thm-rank-nullity. And \( M^{*} \) is surjective: \( M^{*}(xq) = q \) for every \( q \in V \). So \( \rank M^{*} = 3 \) too, agreeing with @cor-rank-adjoint (a).
:::

::: {#exr-adjoints-b3}
[B3: Locating the kernel of the adjoint]

Let \( \A = \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 1 \end{pmatrix} \in M_{3 \times 2}(\nR) \), and let \( T = T_{\A} \colon \nR^2 \to \nR^3 \) with the standard inner products.

::: {.enumerate options="label=(\alph*)"}
1. Find a basis of \( \im T \) and a basis of \( \ker T^{*} \).
2. Verify directly that every vector of \( \ker T^{*} \) is orthogonal to every vector of \( \im T \), and that the dimensions add to \( 3 \).
3. Find \( \ker T \) and \( \im T^{*} \), and check @thm-four-subspaces-orthogonal (b) in this case.
:::
:::

::: {.solution}
(a) The two columns \( (1, 1, 0) \) and \( (0, 1, 1) \) are independent, so they are a basis of \( \im T = \col(\A) \) and \( \rank T = 2 \). Since \( T^{*} = T_{\A\tp} \), the kernel of \( T^{*} \) is \( \nul(\A\tp) \): the equations \( y_1 + y_2 = 0 \) and \( y_2 + y_3 = 0 \) give \( \ker T^{*} = \Span\bigl((1, -1, 1)\bigr) \).

(b) \( (1, 1, 0) \cdot (1, -1, 1) = 1 - 1 + 0 = 0 \) and \( (0, 1, 1) \cdot (1, -1, 1) = 0 - 1 + 1 = 0 \). Since these two vectors span \( \im T \), orthogonality extends to all of \( \im T \) by linearity. The dimensions are \( 2 + 1 = 3 = \dim \nR^3 \), as @thm-four-subspaces-orthogonal (d) requires.

(c) \( \A\x = \0 \) gives \( x_1 = 0 \) and \( x_2 = 0 \), so \( \ker T = \{\0\} \) and \( (\ker T)^{\perp} = \nR^2 \). On the other side, \( \rank T^{*} = \rank T = 2 \) by @cor-rank-adjoint (a), and \( \im T^{*} \subseteq \nR^2 \), so \( \im T^{*} = \nR^2 \). The two agree.
:::

### C. Going deeper

::: {#exr-adjoints-c1}
[C1: The adjoint of integration]

Let \( V = \nR[x]_{\le 1} \) and \( W = \nR[x]_{\le 2} \) with the coefficient inner products of @exr-adjoints-b2, and let
\[
J \colon V \to W, \qquad J(p)(x) \coloneqq \int_0^x p(t)\,\dd t .
\]

::: {.enumerate options="label=(\alph*)"}
1. Find \( J^{*} \).
2. Let \( D \colon W \to V \) be differentiation. Show that \( J^{*} \neq D \), although \( DJ = \id_V \).
3. Explain in one sentence why (b) does not contradict @thm-adjoint-properties (e).
:::
:::

::: {.solution}
(a) \( J(1) = x \) and \( J(x) = \tfrac12 x^2 \), so in the orthonormal bases \( \sD = (1, x) \) of \( V \) and \( \sE = (1, x, x^2) \) of \( W \),
\[
\mtx{J}{\sD}{\sE} = \begin{pmatrix} 0 & 0 \\ 1 & 0 \\ 0 & \tfrac12 \end{pmatrix},
\qquad
\mtx{J^{*}}{\sE}{\sD} = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & \tfrac12 \end{pmatrix}
\]
by @thm-matrix-of-adjoint. Hence \( J^{*}(c_0 + c_1x + c_2x^2) = c_1 + \tfrac12 c_2x \).

(b) \( D(c_0 + c_1x + c_2x^2) = c_1 + 2c_2x \), so \( J^{*} \) and \( D \) differ on \( x^2 \): \( J^{*}(x^2) = \tfrac12 x \) while \( D(x^2) = 2x \). Yet \( D(J(p)) = p \) for every \( p \in V \), by differentiating the integral, or by multiplying the two matrices: \( \mtx{D}{\sE}{\sD}\,\mtx{J}{\sD}{\sE} = \I_2 \).

(c) Part (e) of @thm-adjoint-properties applies to an **invertible** map, and \( J \) is not invertible: it is injective but not surjective, since \( \dim V = 2 < 3 = \dim W \). A one-sided inverse carries no information about the adjoint.
:::

::: {#exr-adjoints-c2}
[C2: Skew-adjoint operators]

Let \( V \) be a finite-dimensional inner product space over \( F \) and let \( T \in \cL(V) \) satisfy \( T^{*} = -T \) (such a \( T \) is called **skew-adjoint**).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \inner{T\v}{\v} \) is purely imaginary for every \( \v \in V \) when \( F = \nC \), and that \( \inner{T\v}{\v} = 0 \) for every \( \v \in V \) when \( F = \nR \).
2. Prove that every skew-adjoint \( T \) is normal.
3. Suppose \( F = \nC \). Prove that \( T \) is skew-adjoint if and only if \( iT \) is self-adjoint, and deduce that every \( S \in \cL(V) \) can be written \( S = A + iB \) with \( A, B \) self-adjoint.
:::
:::

::: {.solution}
(a) By conjugate symmetry and \( T^{*} = -T \),
\[
\conj{\inner{T\v}{\v}} = \inner{\v}{T\v} = \inner{T^{*}\v}{\v} = -\inner{T\v}{\v} .
\]
A complex number equal to minus its own conjugate has zero real part, so \( \inner{T\v}{\v} \) is purely imaginary. When \( F = \nR \) the inner product is real, so the same equation reads \( \inner{T\v}{\v} = -\inner{T\v}{\v} \), forcing \( \inner{T\v}{\v} = 0 \).

(b) \( T^{*}T = (-T)T = -T^2 \) and \( TT^{*} = T(-T) = -T^2 \), so the two agree.

(c) By @thm-adjoint-properties (b), \( (iT)^{*} = \conj{i}T^{*} = -iT^{*} \). If \( T^{*} = -T \) then \( (iT)^{*} = iT \), so \( iT \) is self-adjoint; conversely, if \( (iT)^{*} = iT \) then \( -iT^{*} = iT \), so \( T^{*} = -T \). For the decomposition put
\[
A \coloneqq \tfrac12(S + S^{*}), \qquad B \coloneqq \tfrac{1}{2i}(S - S^{*}) .
\]
Then \( A + iB = \tfrac12(S + S^{*}) + \tfrac12(S - S^{*}) = S \). Both are self-adjoint: \( A^{*} = \tfrac12(S^{*} + S) = A \) by @thm-adjoint-properties (a), (b) and (d), and \( \tfrac{1}{2i}(S - S^{*}) \) is \( -i \) times the skew-adjoint operator \( \tfrac12(S - S^{*}) \), hence self-adjoint by the first part of (c). This is the operator version of writing a complex number as \( a + bi \).
:::

::: {#exr-adjoints-c3}
[C3: The adjoint in an arbitrary basis]

Let \( V \) be a finite-dimensional inner product space, let \( \sB = (\b_1, \dots, \b_n) \) be **any** ordered basis of \( V \), let \( \G \) be its Gram matrix, \( g_{ij} = \inner{\b_j}{\b_i} \), and let \( T \in \cL(V) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \inner{\u}{\v} = \coord{\v}{\sB}^{*}\,\G\,\coord{\u}{\sB} \) for all \( \u, \v \in V \).
2. Deduce that \( \mtx{T^{*}}{\sB}{\sB} = \G^{-1}\left(\mtx{T}{\sB}{\sB}\right)^{*}\G \).
3. Check that (b) returns @thm-matrix-of-adjoint when \( \sB \) is orthonormal, and verify it on @exm-adjoint-nonorthonormal-basis.
:::

*Hint: for (b), write the defining identity of \( T^{*} \) in the coordinates of (a) and use that \( \x^{*}\M\y = \x^{*}\N\y \) for all \( \x, \y \) forces \( \M = \N \).*
:::

::: {.solution}
(a) Write \( \u = \sum_j x_j\b_j \) and \( \v = \sum_i y_i\b_i \), so \( \x = \coord{\u}{\sB} \) and \( \y = \coord{\v}{\sB} \). Expanding in the first slot and then in the second,
\[
\inner{\u}{\v} = \sum_{i, j} x_j\conj{y_i}\inner{\b_j}{\b_i} = \sum_{i, j} \conj{y_i}\,g_{ij}\,x_j = \y^{*}\G\x .
\]

(b) Put \( \A = \mtx{T}{\sB}{\sB} \) and \( \B = \mtx{T^{*}}{\sB}{\sB} \). By @thm-matrix-of-map-coordinates, \( \coord{T\u}{\sB} = \A\x \) and \( \coord{T^{*}\v}{\sB} = \B\y \). So (a) turns \( \inner{T\u}{\v} = \inner{\u}{T^{*}\v} \) into
\[
\y^{*}\G\A\x = (\B\y)^{*}\G\x = \y^{*}\B^{*}\G\x \qquad \text{for all } \x, \y \in F^n .
\]
Taking \( \x = \e_j \) and \( \y = \e_i \) reads off the \( (i, j) \) entries, so \( \G\A = \B^{*}\G \). The Gram matrix is invertible (@thm-gram-matrix-properties (c)), so \( \B^{*} = \G\A\G^{-1} \), and starring both sides gives \( \B = (\G^{-1})^{*}\A^{*}\G^{*} = \G^{-1}\A^{*}\G \), using \( \G^{*} = \G \) (@thm-gram-matrix-properties (a)) and hence \( (\G^{-1})^{*} = \G^{-1} \).

(c) If \( \sB \) is orthonormal then \( g_{ij} = \delta_{ij} \), so \( \G = \I \) and the formula reads \( \B = \A^{*} \), which is @thm-matrix-of-adjoint. In @exm-adjoint-nonorthonormal-basis the computation in the remark after it is exactly this formula, with \( \G = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} \).
:::

::: {#exr-adjoints-c4}
[C4: The adjoint is the dual map read through Riesz]

Let \( V, W \) be finite-dimensional inner product spaces over \( F \), let \( T \in \cL(V, W) \), let \( T' \colon W^{*} \to V^{*} \) be the dual map (@def-dual-map) and let \( \Phi_V, \Phi_W \) be the Riesz maps (@cor-riesz-isomorphism).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \Phi_V \circ T^{*} = T' \circ \Phi_W \), so that the square drawn in the section commutes.
2. Deduce that \( T^{*} = \Phi_V^{-1} \circ T' \circ \Phi_W \), and explain in one sentence why this says that the adjoint carries no information the dual map does not, beyond the choice of inner product.
:::

*Hint: for (a), both sides send a vector of \( W \) to a functional on \( V \), so evaluate them at an arbitrary vector of \( V \).*
:::

::: {.solution}
(a) Let \( \w \in W \) and \( \v \in V \). By @def-dual-map the dual map sends a functional \( f \in W^{*} \) to \( f \circ T \), and \( \Phi_W\w = \inner{\cdot}{\w} \), so
\[
\bigl(T'(\Phi_W\w)\bigr)(\v) = (\Phi_W\w)(T\v) = \inner{T\v}{\w} .
\]
On the other side \( \Phi_V(T^{*}\w) = \inner{\cdot}{T^{*}\w} \), so by @def-adjoint
\[
\bigl(\Phi_V(T^{*}\w)\bigr)(\v) = \inner{\v}{T^{*}\w} = \inner{T\v}{\w} .
\]
The two functionals agree at every \( \v \in V \), so they are equal, and this holds for every \( \w \in W \). Hence \( \Phi_V \circ T^{*} = T' \circ \Phi_W \).

(b) The Riesz maps are bijections (@cor-riesz-isomorphism), so \( \Phi_V \) may be inverted in (a), giving \( T^{*} = \Phi_V^{-1} \circ T' \circ \Phi_W \). Reading the right-hand side from right to left: transport a vector of \( W \) into \( W^{*} \), pull it back with \( T' \), transport it back into \( V \). Every step but the two transports is \( T' \), so the adjoint adds nothing to the dual map except the inner product used to identify a space with its dual.
:::
