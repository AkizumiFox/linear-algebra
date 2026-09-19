# Tensor Products of Maps

Section 02 built the space \( V \otimes W \). A construction on spaces is worth little until it acts on maps as well: the philosophy of the whole book has been objects first, then the maps between them. So given \( S \colon V \to V' \) and \( T \colon W \to W' \), we want a single map \( V \otimes W \to V' \otimes W' \) built from the two. This section builds it, computes its matrix, and discovers that the matrix is the Kronecker product of Chapter 7 — which pays both of the debts that Chapter 7 §04 left open. It ends with the identification \( V^{*} \otimes W \cong \cL(V, W) \), which every later section of the chapter uses.

## A map on each factor gives a map on the product

The definition writes itself, and that is the danger. We want a map that sends \( \v \otimes \w \) to \( S\v \otimes T\w \), so the temptation is to write

> "Define \( (S \otimes T)(\v \otimes \w) \coloneqq S\v \otimes T\w \), and extend linearly."

Nothing in that sentence is a definition. Simple tensors span \( V \otimes W \) (@prp-simple-tensors-span), but they do not exhaust it, and worse, the expression of an element as a combination of them is wildly non-unique: \( \v \otimes \w = (2\v) \otimes (\tfrac12\w) \), and \( \v \otimes \w + \v \otimes \w' = \v \otimes (\w + \w') \). A formula prescribed on simple tensors may therefore assign two different values to one element, and then it defines nothing at all. Here is a formula that really does fail. Try to define \( g \colon V \otimes W \to V \) by \( g(\v \otimes \w) \coloneqq \v \). Taking \( \w = \0 \) gives \( \v \otimes \0 = \0 \) (@prp-simple-tensor-zero), so \( g \) would have to send \( \0 \) to every \( \v \) at once.

*To build a map out of \( V \otimes W \), never write a formula on simple tensors: write down a bilinear map and let the universal property produce the linear one.*

That is the discipline of this chapter, and applied here it costs three lines.

::: {#thm-tensor-of-maps-well-defined}
[Tensor Product of Two Linear Maps]

Let \( V, V', W, W' \) be vector spaces over \( F \), and let \( S \in \cL(V, V') \) and \( T \in \cL(W, W') \). Then there is **exactly one** linear map
\[
f \colon V \otimes W \to V' \otimes W'
\]
with \( f(\v \otimes \w) = S\v \otimes T\w \) for **all** \( \v \in V \) and \( \w \in W \).
:::

::: {.idea}
The assignment \( (\v, \w) \mapsto S\v \otimes T\w \) is bilinear, because \( S \) and \( T \) are linear and \( \otimes \) is bilinear in its two slots. A bilinear map out of \( V \times W \) is exactly what the universal property consumes, and what it returns is a unique linear map out of \( V \otimes W \). There is nothing else to check.
:::

::: {.proof}
Define \( \beta \colon V \times W \to V' \otimes W' \) by \( \beta(\v, \w) \coloneqq S\v \otimes T\w \). Fix \( \w \in W \). The map \( \v \mapsto S\v \otimes T\w \) is the composite of \( S \), which is linear, with the map \( \u \mapsto \u \otimes T\w \), which is linear because the map \( \otimes \colon V' \times W' \to V' \otimes W' \) of @def-tensor-product is bilinear, hence linear in its first slot with the second slot held fixed. A composite of linear maps is linear (@thm-composition-linear), so \( \beta \) is linear in its first argument. Fixing \( \v \) instead and swapping the roles of the two slots gives linearity in the second. Hence \( \beta \) is bilinear.

By the universal property in @def-tensor-product there is a unique linear \( f \colon V \otimes W \to V' \otimes W' \) with \( f(\v \otimes \w) = \beta(\v, \w) = S\v \otimes T\w \) for all \( \v, \w \). This proves both existence and uniqueness.
:::

Uniqueness is what licenses a name.

::: {#def-tensor-of-maps}
[Tensor product of linear maps]

Let \( S \in \cL(V, V') \) and \( T \in \cL(W, W') \). The **tensor product** of \( S \) and \( T \) is the unique linear map
\[
S \otimes T \colon V \otimes W \to V' \otimes W'
\]
of @thm-tensor-of-maps-well-defined, characterized by
\[
(S \otimes T)(\v \otimes \w) = S\v \otimes T\w
\quad (\v \in V,\ \w \in W).
\]
:::

The symbol \( \otimes \) now has three jobs — a space, a vector, a map — and they agree: \( S \otimes T \) applied to \( \v \otimes \w \) is \( S\v \otimes T\w \), which is the only thing the notation could mean.

**Examples.**

1. **The identity.** \( \id_V \otimes \id_W \) sends \( \v \otimes \w \) to \( \v \otimes \w \), and so does \( \id_{V \otimes W} \). Both are linear and both are the factorization of the same bilinear map, so \( \id_V \otimes \id_W = \id_{V \otimes W} \) by the uniqueness clause. Degenerate, and used in almost every proof below.
2. **Acting on one slot.** \( S \otimes \id_W \) sends \( \v \otimes \w \) to \( S\v \otimes \w \): it does \( S \) in the first slot and leaves the second alone. If \( V = W = F[x] \) and \( S = D \) is differentiation, \( D \otimes \id \) is "differentiate the first factor".
3. **Scalars.** For \( c, d \in F \), \( (c\,\id_V) \otimes (d\,\id_W) \) sends \( \v \otimes \w \) to \( c\v \otimes d\w = cd\,(\v \otimes \w) \), so it is \( cd\,\id_{V \otimes W} \). In particular a scalar may be moved from one slot to the other, which is the map-level shadow of \( c\v \otimes \w = \v \otimes c\w \).
4. **Zero.** If \( S = 0 \), then \( (S \otimes T)(\v \otimes \w) = \0 \otimes T\w = \0 \), so \( S \otimes T = 0 \). The converse also holds; see @exr-tensor-products-of-maps-c1.

**Non-example by minimal change.** Keep \( S \) and \( T \) linear, but try to send \( \v \otimes \w \) to \( S\v \otimes T\w + \v \otimes \w \). This one *is* legitimate: the assignment \( (\v, \w) \mapsto S\v \otimes T\w + \v \otimes \w \) is a sum of two bilinear maps, hence bilinear, and the universal property applies. What is not legitimate is \( (\v, \w) \mapsto S\v \otimes T\w + \u_0 \) for a fixed non-zero \( \u_0 \in V' \otimes W' \): the added constant destroys linearity in each slot, so no linear map on \( V \otimes W \) does this, and indeed the prescription contradicts itself at \( \w = \0 \). The exact clause that fails is bilinearity, and it fails for the same reason as in the map \( g \) above.

We will lean repeatedly on the following consequence of the uniqueness clause. It replaces the phrase "and extend linearly", which we are not allowed to use.

::: {#lem-determined-by-simple-tensors}
[Simple Tensors Determine a Map]

Let \( Z \) be a vector space over \( F \) and let \( f, g \colon V \otimes W \to Z \) be linear. If \( f(\v \otimes \w) = g(\v \otimes \w) \) for all \( \v \in V \) and \( \w \in W \), then \( f = g \).
:::

::: {.proof}
Put \( \beta(\v, \w) \coloneqq f(\v \otimes \w) \). Since \( \otimes \) is bilinear and \( f \) is linear, \( \beta \) is bilinear. By hypothesis \( \beta(\v, \w) = g(\v \otimes \w) \) as well, so \( f \) and \( g \) are both linear maps factoring \( \beta \) through \( \otimes \). The universal property of @def-tensor-product says there is only one such map. Hence \( f = g \).
:::

No finite-dimensionality is needed, and no basis is chosen. With it, the algebra of \( \otimes \) on maps is a formality.

:::: {#prp-tensor-of-maps-algebra}
[Algebra of Tensor Products of Maps]

Let \( S, S_1, S_2 \in \cL(V, V') \), \( T, T_1, T_2 \in \cL(W, W') \) and \( c \in F \). Let also \( R \in \cL(V', V'') \) and \( U \in \cL(W', W'') \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( (S_1 + S_2) \otimes T = S_1 \otimes T + S_2 \otimes T \) and \( S \otimes (T_1 + T_2) = S \otimes T_1 + S \otimes T_2 \);
2. \( (cS) \otimes T = c(S \otimes T) = S \otimes (cT) \);
3. \( (R \otimes U)(S \otimes T) = RS \otimes UT \);
4. \( \id_V \otimes \id_W = \id_{V \otimes W} \).
:::
::::

::: {.proof}
In each part both sides are linear maps out of \( V \otimes W \), so by @lem-determined-by-simple-tensors it suffices to compare their values at a simple tensor \( \v \otimes \w \).

(a) The left side gives \( (S_1 + S_2)\v \otimes T\w = (S_1\v + S_2\v) \otimes T\w \), which equals \( S_1\v \otimes T\w + S_2\v \otimes T\w \) because \( \otimes \) is additive in its first slot. That is the value of the right side. The second identity is the same argument in the other slot.

(b) \( (cS)\v \otimes T\w = (c\,S\v) \otimes T\w = c(S\v \otimes T\w) = S\v \otimes (c\,T\w) \), where both outer equalities use bilinearity of \( \otimes \).

(c) \( (R \otimes U)\big((S \otimes T)(\v \otimes \w)\big) = (R \otimes U)(S\v \otimes T\w) = RS\v \otimes UT\w \), which is the value of \( RS \otimes UT \).

(d) Done in Example 1.
:::

Part (c) is the statement that \( \otimes \) respects composition: it is *functoriality*, and we will see in a moment that it is the mixed product rule of @thm-kronecker-properties in disguise.

Two more structural facts are needed before §04 can speak of tensors with several slots. The first extends the universal property from two factors to any number, and the second says that the brackets do not matter.

For \( k \ge 2 \) define the iterated tensor product by
\[
V_1 \otimes \dots \otimes V_k \coloneqq (V_1 \otimes \dots \otimes V_{k-1}) \otimes V_k ,
\]
starting from \( V_1 \) itself when \( k = 1 \), and write \( \v_1 \otimes \dots \otimes \v_k \) for \( (\v_1 \otimes \dots \otimes \v_{k-1}) \otimes \v_k \). Multilinear maps of \( k \) arguments were defined in @def-multilinear-map.

::: {#lem-multilinear-universal}
[Universal Property for \( k \) Factors]

Let \( V_1, \dots, V_k \) and \( Z \) be vector spaces over \( F \), and let \( \beta \colon V_1 \times \dots \times V_k \to Z \) be multilinear. Then there is **exactly one** linear map
\[
\bar\beta \colon V_1 \otimes \dots \otimes V_k \to Z
\]
with \( \bar\beta(\v_1 \otimes \dots \otimes \v_k) = \beta(\v_1, \dots, \v_k) \) for all \( \v_1, \dots, \v_k \). Moreover the tensors \( \v_1 \otimes \dots \otimes \v_k \) span \( V_1 \otimes \dots \otimes V_k \).
:::

::: {.idea}
Induction on \( k \), freezing the last argument. With \( \v_k \) held fixed, \( \beta \) is multilinear in the first \( k-1 \) arguments, so the inductive hypothesis converts it into a linear map on \( X = V_1 \otimes \dots \otimes V_{k-1} \). Letting \( \v_k \) move again gives a bilinear map on \( X \times V_k \), and (T1) finishes. The spanning claim is the same induction.
:::

::: {.proof}
For \( k = 1 \) take \( \bar\beta = \beta \), which is linear, and the claim is trivial; for \( k = 2 \) the statement is @def-tensor-product together with @prp-simple-tensors-span. Let \( k \ge 3 \) and assume the lemma for \( k - 1 \). Put \( X \coloneqq V_1 \otimes \dots \otimes V_{k-1} \).

Fix \( \v_k \in V_k \). The map \( (\v_1, \dots, \v_{k-1}) \mapsto \beta(\v_1, \dots, \v_k) \) is multilinear, so the inductive hypothesis gives a unique linear \( g_{\v_k} \colon X \to Z \) with \( g_{\v_k}(\v_1 \otimes \dots \otimes \v_{k-1}) = \beta(\v_1, \dots, \v_k) \).

The map \( X \times V_k \to Z \), \( (x, \v_k) \mapsto g_{\v_k}(x) \), is bilinear. It is linear in \( x \) because each \( g_{\v_k} \) is. For linearity in \( \v_k \), fix \( \v_k, \v'_k \in V_k \) and \( c \in F \): the linear maps \( g_{\v_k + c\v'_k} \) and \( g_{\v_k} + c\,g_{\v'_k} \) agree at every \( \v_1 \otimes \dots \otimes \v_{k-1} \), because \( \beta \) is linear in its last argument, and those tensors span \( X \) by the inductive hypothesis; so the two maps are equal.

By @def-tensor-product there is a unique linear \( \bar\beta \) on \( X \otimes V_k = V_1 \otimes \dots \otimes V_k \) with \( \bar\beta(x \otimes \v_k) = g_{\v_k}(x) \); taking \( x = \v_1 \otimes \dots \otimes \v_{k-1} \) gives \( \bar\beta(\v_1 \otimes \dots \otimes \v_k) = \beta(\v_1, \dots, \v_k) \).

Finally, \( X \otimes V_k \) is spanned by the simple tensors \( x \otimes \v_k \) (@prp-simple-tensors-span), each \( x \) is a combination of \( \v_1 \otimes \dots \otimes \v_{k-1} \) by the inductive hypothesis, and \( \otimes \) is linear in its first slot; so the \( k \)-fold tensors span. A linear map is determined by its values on a spanning set, which gives uniqueness of \( \bar\beta \).
:::

::: {#prp-tensor-associative}
[Associativity of the Tensor Product]

Let \( U, V, W \) be vector spaces over \( F \). There is a unique isomorphism
\[
\alpha \colon (U \otimes V) \otimes W \to U \otimes (V \otimes W)
\]
with \( \alpha\big((\u \otimes \v) \otimes \w\big) = \u \otimes (\v \otimes \w) \) for all \( \u, \v, \w \).
:::

::: {.proof}
The map \( (\u, \v, \w) \mapsto \u \otimes (\v \otimes \w) \) is trilinear, since \( \otimes \) is bilinear in each of its two uses. By @lem-multilinear-universal with \( k = 3 \) there is a unique linear \( \alpha \) on \( (U \otimes V) \otimes W \) with the stated values. Symmetrically, freezing the *first* argument instead and running the two-factor property twice produces a linear \( \alpha' \colon U \otimes (V \otimes W) \to (U \otimes V) \otimes W \) with \( \alpha'(\u \otimes (\v \otimes \w)) = (\u \otimes \v) \otimes \w \). The composite \( \alpha'\alpha \) fixes every \( (\u \otimes \v) \otimes \w \), and those span by @lem-multilinear-universal, so \( \alpha'\alpha = \id \); symmetrically \( \alpha\alpha' = \id \). Hence \( \alpha \) is an isomorphism.
:::

From now on we drop the brackets and write \( U \otimes V \otimes W \), with \( \u \otimes \v \otimes \w \) for the element that both ways of bracketing name, and likewise for any number of factors.

## The matrix of a tensor product of maps

Now we compute. A matrix needs **ordered** bases, and \( V \otimes W \) has a basis indexed by *pairs* \( (i, k) \), so the whole content of the computation is which order we put the pairs in.

*Order the basis \( \v_i \otimes \w_k \) by dictionary order on the pair \( (i, k) \): the index of the first factor changes slowly, the index of the second factor runs fastest.*

::: {#def-tensor-basis-ordering}
[The product basis, ordered]

Let \( \sB = (\v_1, \dots, \v_n) \) be an ordered basis of \( V \) and \( \sC = (\w_1, \dots, \w_q) \) an ordered basis of \( W \). Write \( \sB \otimes \sC \) for the basis \( (\v_i \otimes \w_k) \) of \( V \otimes W \) given by @thm-tensor-basis, **ordered** so that \( \v_i \otimes \w_k \) occupies position
\[
(i - 1)q + k \qquad (1 \le i \le n,\ 1 \le k \le q),
\]
that is, in the order
\[
\v_1 \otimes \w_1,\ \dots,\ \v_1 \otimes \w_q,\ \v_2 \otimes \w_1,\ \dots,\ \v_n \otimes \w_q .
\]
:::

Division with remainder writes every position \( 1, \dots, nq \) as \( (i-1)q + k \) for exactly one pair, so this really is an ordering of the whole basis. It is the dictionary order on pairs, and it is the same rule that Chapter 7 used to label the rows and columns of a Kronecker product in the formula \( (\ast) \) after @def-kronecker-product. That is not a coincidence, and the next theorem says why.

::: {#thm-kronecker-is-tensor}
[The Kronecker Product Is the Matrix of a Tensor Product of Maps]

Let \( V, V', W, W' \) be finite-dimensional vector spaces over \( F \) with ordered bases
\[
\begin{aligned}
\sB &= (\v_1, \dots, \v_n) \text{ of } V, &\quad \sB' &= (\v'_1, \dots, \v'_m) \text{ of } V', \\
\sC &= (\w_1, \dots, \w_q) \text{ of } W, &\quad \sC' &= (\w'_1, \dots, \w'_p) \text{ of } W' .
\end{aligned}
\]
Let \( S \in \cL(V, V') \) and \( T \in \cL(W, W') \). Then, with the orderings of @def-tensor-basis-ordering on both sides,
\[
\mtx{S \otimes T}{\sB \otimes \sC}{\sB' \otimes \sC'}
= \mtx{S}{\sB}{\sB'} \otimes \mtx{T}{\sC}{\sC'} ,
\]
the Kronecker product of @def-kronecker-product.
:::

::: {.idea}
A matrix is read off column by column, and column \( (j, l) \) of the left side holds the coordinates of \( (S \otimes T)(\v_j \otimes \w_l) = S\v_j \otimes T\w_l \). Expanding \( S\v_j \) and \( T\w_l \) in their bases and multiplying out by bilinearity produces the coefficient \( a_{ij}b_{kl} \) on \( \v'_i \otimes \w'_k \) — a product of one entry of each matrix. The entry formula \( (\ast) \) of Chapter 7 says the Kronecker product puts exactly that number in exactly that place, provided the pairs are read in dictionary order. So the theorem is the entry formula and bilinearity, nothing more.
:::

::: {.proof}
Write \( \A = (a_{ij}) = \mtx{S}{\sB}{\sB'} \in M_{m \times n}(F) \) and \( \B = (b_{kl}) = \mtx{T}{\sC}{\sC'} \in M_{p \times q}(F) \), so that by @def-matrix-of-linear-map
\[
S\v_j = \sum_{i=1}^{m} a_{ij}\v'_i, \qquad
T\w_l = \sum_{k=1}^{p} b_{kl}\w'_k .
\]
Fix \( j \) and \( l \). Using @def-tensor-of-maps and then bilinearity of \( \otimes \) in each slot,
\[
\begin{aligned}
(S \otimes T)(\v_j \otimes \w_l)
&= S\v_j \otimes T\w_l \\
&= \Big(\sum_{i} a_{ij}\v'_i\Big) \otimes \Big(\sum_{k} b_{kl}\w'_k\Big) \\
&= \sum_{i=1}^{m}\sum_{k=1}^{p} a_{ij}b_{kl}\,(\v'_i \otimes \w'_k) .
\end{aligned}
\]
By @def-tensor-basis-ordering, \( \v_j \otimes \w_l \) is the basis vector in position \( (j-1)q + l \) of \( \sB \otimes \sC \), and \( \v'_i \otimes \w'_k \) is the basis vector in position \( (i-1)p + k \) of \( \sB' \otimes \sC' \). So the displayed expansion says that the entry of \( \mtx{S \otimes T}{\sB \otimes \sC}{\sB' \otimes \sC'} \) in row \( (i-1)p + k \) and column \( (j-1)q + l \) is \( a_{ij}b_{kl} \).

By the entry formula \( (\ast) \) accompanying @def-kronecker-product, that is exactly the entry of \( \A \otimes \B \) in the same position. Every row index of an \( mp \times nq \) matrix is \( (i-1)p + k \) for exactly one pair \( (i, k) \), and every column index is \( (j-1)q + l \) for exactly one pair \( (j, l) \), so the two matrices agree in every position. This proves the theorem.
:::

**The ordering is the whole content, so it is worth being exact about it.** Suppose we had ordered the product basis the other way, putting \( \v_i \otimes \w_k \) in position \( (k-1)n + i \), so that the *second* index changes slowly. Running the proof again, the entry in row \( (k-1)m + i \) and column \( (l-1)n + j \) is still \( a_{ij}b_{kl} \), which by \( (\ast) \) is the entry of \( \B \otimes \A \) in that position. So the other ordering gives
\[
\mtx{T}{\sC}{\sC'} \otimes \mtx{S}{\sB}{\sB'} ,
\]
the Kronecker product with the factors **swapped** — not the transpose, and not the same matrix. For square factors the two answers are related exactly as @prp-kronecker-swap-similar says, by conjugating with the permutation matrix that relabels dictionary order into its reverse — which is precisely the change-of-coordinates matrix between the two orderings of the product basis. In the rectangular setting of @thm-kronecker-is-tensor the relation is not a conjugation at all: the row and column relabelings are different permutations, so \( \B \otimes \A = \P_\sigma\tp(\A \otimes \B)\P_\tau \) with two matrices, as Chapter 7 notes just after that proposition's proof.

::: {.warning}
**Do not reverse the two factors of the basis ordering.** The theorem needs the index of the **first** tensor factor to be the slow one, matching Chapter 7's dictionary order in \( (\ast) \). With the fast and slow indices exchanged the matrix of \( S \otimes T \) is \( [T] \otimes [S] \). For \( \A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \) and \( \B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) these two differ in the \( (1,2) \) entry, which is \( a_{11}b_{12} = 1 \) in the first and \( b_{11}a_{12} = 0 \) in the second (the non-example after @def-kronecker-product).
:::

**Chapter 7's two promises, paid.** At @def-kronecker-product, Chapter 7 wrote that the symbol \( \otimes \) "anticipates the tensor product of Chapter 14, of which this is the matrix version". @thm-kronecker-is-tensor is that statement, made precise and proved: the Kronecker product of two matrices is the matrix of the tensor product of the two maps they represent, taken in the product bases. At the end of the same section, Chapter 7 wrote that the Kronecker product is "the coordinate shadow of a basis-free construction: the tensor product of linear maps, in Chapter 14, whose matrix in suitable bases is exactly \( \A \otimes \B \)", and promised that "the dictionary order in \( (\ast) \) will reappear there as an ordering of a basis \( \v_i \otimes \w_k \)". The suitable bases are \( \sB \otimes \sC \) and \( \sB' \otimes \sC' \); the dictionary order has reappeared, as @def-tensor-basis-ordering; and the shadow is cast by \( S \otimes T \). The second promise gets a sharper payment at the end of this section, where the vec identity turns out to be this same theorem applied to a space of matrices.

::: {#exm-tensor-of-maps-matrix}
[Computing with a tensor product of maps]

Let \( S \colon F^2 \to F^2 \) and \( T \colon F^3 \to F^2 \) have matrices, in the standard bases,
\[
\A = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}, \qquad
\B = \begin{pmatrix} 1 & 0 & -1 \\ 2 & 1 & 0 \end{pmatrix}.
\]
Compute \( (S \otimes T)(\e_1 \otimes \f_2 + \e_2 \otimes \f_3) \) directly from @def-tensor-of-maps, and again from the matrix of @thm-kronecker-is-tensor. Here \( (\e_1, \e_2) \) is the standard basis of \( F^2 \) and \( (\f_1, \f_2, \f_3) \) that of \( F^3 \).
:::

::: {.solution}
**Directly.** Columns of \( \A \) and \( \B \) give \( S\e_1 = 2\e_1 \), \( S\e_2 = \e_1 + 3\e_2 \), \( T\f_2 = \e_2 \) and \( T\f_3 = -\e_1 \). Hence
\[
\begin{aligned}
(S \otimes T)(\e_1 \otimes \f_2 + \e_2 \otimes \f_3)
&= 2\e_1 \otimes \e_2 + (\e_1 + 3\e_2) \otimes (-\e_1) \\
&= -\,\e_1 \otimes \e_1 + 2\,\e_1 \otimes \e_2 - 3\,\e_2 \otimes \e_1 ,
\end{aligned}
\]
using bilinearity of \( \otimes \) in both slots.

**By matrix.** The domain basis, ordered as in @def-tensor-basis-ordering, is \( (\e_1 \otimes \f_1, \e_1 \otimes \f_2, \e_1 \otimes \f_3, \e_2 \otimes \f_1, \e_2 \otimes \f_2, \e_2 \otimes \f_3) \), so the input has coordinate column \( (0, 1, 0, 0, 0, 1) \). By @thm-kronecker-is-tensor the matrix of \( S \otimes T \) is
\[
\A \otimes \B = \begin{pmatrix}
2 & 0 & -2 & 1 & 0 & -1 \\
4 & 2 & 0 & 2 & 1 & 0 \\
0 & 0 & 0 & 3 & 0 & -3 \\
0 & 0 & 0 & 6 & 3 & 0
\end{pmatrix},
\]
and multiplying it by that column gives \( (-1, 2, -3, 0) \). In the codomain basis \( (\e_1 \otimes \e_1, \e_1 \otimes \e_2, \e_2 \otimes \e_1, \e_2 \otimes \e_2) \) this is the same element as before.
:::

## What Chapter 7 was computing

Every property of the Kronecker product proved by entry-chasing in Chapter 7 is now a property of maps, and several of them become one-liners. We record the three that the rest of the chapter uses.

The mixed product rule comes first, because it is the one Chapter 7 called "the engine of everything that follows".

::: {#cor-mixed-product-is-composition}
[The Mixed Product Rule Is Functoriality]

Let \( \A \in M_{m \times n}(F) \), \( \C \in M_{n \times t}(F) \), \( \B \in M_{p \times q}(F) \) and \( \D \in M_{q \times u}(F) \). Then
\[
(\A \otimes \B)(\C \otimes \D) = (\A \C) \otimes (\B \D) .
\]
:::

::: {.proof}
Let \( S, R, T, U \) be the linear maps with matrices \( \A, \C, \B, \D \) in the standard bases of the relevant spaces \( F^k \). By @thm-kronecker-is-tensor, with all product bases ordered as in @def-tensor-basis-ordering, \( \A \otimes \B \) and \( \C \otimes \D \) are the matrices of \( S \otimes T \) and \( R \otimes U \). By @thm-matrix-of-composition the product of the matrices is the matrix of the composite \( (S \otimes T)(R \otimes U) \), which is \( SR \otimes TU \) by @prp-tensor-of-maps-algebra (c). Applying @thm-kronecker-is-tensor once more, and @thm-matrix-of-composition again to each factor, the matrix of \( SR \otimes TU \) is \( (\A \C) \otimes (\B \D) \).
:::

This is @thm-kronecker-properties (c), which Chapter 7 proved by partitioning both matrices into conformable blocks and multiplying blockwise. The proof above says what the identity *means*: doing two things one after the other in each slot separately is the same as doing them one after the other in both slots at once. In the same way, the bilinearity of @thm-kronecker-properties (a) is parts (a) and (b) of @prp-tensor-of-maps-algebra, its associativity (b) is @prp-tensor-associative, and its inverse rule (e) is parts (c) and (d) together with invertibility of a composite.

Next, the numerical invariants.

::: {#cor-tensor-map-invariants}
[Rank, Determinant and Trace of a Tensor Product of Maps]

Let \( V, V', W, W' \) be finite-dimensional over \( F \), \( S \in \cL(V, V') \), \( T \in \cL(W, W') \). Then
\[
\rank(S \otimes T) = \rank S \cdot \rank T .
\]
If moreover \( V = V' \) and \( W = W' \), with \( n = \dim V \ge 1 \) and \( m = \dim W \ge 1 \), then
\[
\det(S \otimes T) = (\det S)^{m}(\det T)^{n},
\qquad
\tr(S \otimes T) = \tr S \cdot \tr T .
\]
:::

::: {.idea}
For the rank, choose bases adapted to the two kernels: then \( S \otimes T \) kills most product basis vectors and sends the remaining \( \rank S \cdot \rank T \) of them to independent vectors. For the determinant, split \( S \otimes T = (S \otimes \id)(\id \otimes T) \). The factor \( \id_V \otimes T \) preserves each of the \( n \) subspaces \( \v_i \otimes W \) and acts on each as \( T \); the factor \( S \otimes \id_W \) preserves each of the \( m \) subspaces \( V \otimes \w_k \) and acts as \( S \). So each factor is block diagonal with repeated blocks, and the exponents count the *other* space's dimension, which is where the exponents come from. The trace we take from the matrix.
:::

::: {.proof}
**Rank.** Let \( r = \rank S \) and \( s = \rank T \). Choose a basis \( (\v_1, \dots, \v_n) \) of \( V \) whose last \( n - r \) vectors form a basis of \( \ker S \); this is possible by @thm-basis-extension-general applied to a basis of \( \ker S \), after reordering. Then \( S\v_1, \dots, S\v_r \) span \( \im S \) by @thm-image-spanned-by-basis-images, and being \( r = \rank S \) spanning vectors of an \( r \)-dimensional space they form a basis of \( \im S \) (@thm-right-size-basis). Choose a basis \( (\w_1, \dots, \w_m) \) of \( W \) the same way, so that \( T\w_1, \dots, T\w_s \) is a basis of \( \im T \) and \( T\w_l = \0 \) for \( l > s \).

By @thm-image-spanned-by-basis-images, \( \im(S \otimes T) \) is spanned by the vectors \( S\v_j \otimes T\w_l \), and those with \( j > r \) or \( l > s \) are \( \0 \). Extend \( (S\v_1, \dots, S\v_r) \) to a basis of \( V' \) and \( (T\w_1, \dots, T\w_s) \) to a basis of \( W' \) (@thm-basis-extension-general). By @thm-tensor-basis the products of these basis vectors form a basis of \( V' \otimes W' \); in particular the \( rs \) vectors \( S\v_j \otimes T\w_l \) with \( j \le r \), \( l \le s \) are linearly independent. They therefore form a basis of \( \im(S \otimes T) \), and \( \rank(S \otimes T) = rs \).

**Determinant.** By @prp-tensor-of-maps-algebra (c) and (d),
\[
S \otimes T = (S \otimes \id_W)(\id_V \otimes T),
\]
so \( \det(S \otimes T) = \det(S \otimes \id_W)\det(\id_V \otimes T) \) by @thm-det-operator-properties. Fix bases \( \sB \) of \( V \) and \( \sC \) of \( W \) and use the ordering of @def-tensor-basis-ordering. For each \( i \), the subspace \( \v_i \otimes W \coloneqq \Span(\v_i \otimes \w_1, \dots, \v_i \otimes \w_m) \) is carried into itself by \( \id_V \otimes T \), which acts on it as \( T \) does on \( W \); and \( V \otimes W \) is the direct sum of these \( n \) subspaces, because their bases together form the basis \( \sB \otimes \sC \). Consecutive blocks of the ordering are exactly these subspaces, so
\[
\mtx{\id_V \otimes T}{\sB \otimes \sC}{\sB \otimes \sC} = \underbrace{\mtx{T}{\sC}{\sC} \oplus \dots \oplus \mtx{T}{\sC}{\sC}}_{n \text{ blocks}},
\]
whose determinant is \( (\det T)^{n} \) by @thm-block-diagonal-arithmetic (d) and induction on the number of blocks. The same argument for \( S \otimes \id_W \), using instead the \( m \) subspaces \( V \otimes \w_k \), gives \( \det(S \otimes \id_W) = (\det S)^{m} \). (This time the relevant basis vectors are not consecutive in the ordering of @def-tensor-basis-ordering, so reorder the basis to make them so; matrices of one operator in two bases are similar, by @thm-change-of-basis-maps, hence have the same determinant, by @cor-det-similarity-invariant.) Multiplying the two gives the formula.

**Trace.** By @thm-kronecker-is-tensor the matrix of \( S \otimes T \) in \( \sB \otimes \sC \) is \( \mtx{S}{\sB}{\sB} \otimes \mtx{T}{\sC}{\sC} \), so by @def-trace-operator and @thm-kronecker-rank-trace-det (b), \( \tr(S \otimes T) = \tr S \cdot \tr T \).
:::

These are parts (a), (c) and (b) of @thm-kronecker-rank-trace-det, transported to operators. Two remarks on what has changed. First, the exponents in the determinant formula are no longer something to memorize: \( \det S \) appears to the power \( \dim W \) because \( S \otimes \id_W \) runs \( S \) once on each of the \( \dim W \) copies of \( V \) inside \( V \otimes W \). Second, the proof of the trace formula above is still a computation in a basis. There is a genuinely basis-free reason, and §04 gives it. The determinant, too, has a basis-free explanation, which has to wait for the top exterior power in §09.

::: {.warning}
**Most operators on \( V \otimes W \) are not of the form \( S \otimes T \).** The operators that are of this form are heavily constrained: by @cor-tensor-map-invariants their rank is a product \( rs \) with \( r \le \dim V \) and \( s \le \dim W \). Take \( V = W = F^2 \), so \( \dim(V \otimes W) = 4 \), and let \( P \) be any operator on \( V \otimes W \) of rank \( 3 \), for instance the projection onto the span of the first three basis vectors of @def-tensor-basis-ordering. Then \( 3 = rs \) with \( r, s \in \{0, 1, 2\} \) is impossible, so \( P \ne S \otimes T \) for every \( S \) and \( T \). The maps \( S \otimes T \) do **span** \( \cL(V \otimes W) \), which is a different and weaker statement; this is the same distinction as between simple tensors and general tensors in §02.
:::

::: {.check}
Let \( S \in \cL(V) \) and \( T \in \cL(W) \) with \( \dim V = 3 \) and \( \dim W = 2 \), and suppose \( \det S = 2 \) and \( \det T = -1 \). What are \( \det(S \otimes T) \) and \( \det(T \otimes S) \), where the second is an operator on \( W \otimes V \)?
:::

::: {.solution}
By @cor-tensor-map-invariants, \( \det(S \otimes T) = (\det S)^{\dim W}(\det T)^{\dim V} = 2^{2}(-1)^{3} = -4 \). For \( T \otimes S \) the roles swap, giving \( (\det T)^{\dim V}(\det S)^{\dim W} = (-1)^{3}2^{2} = -4 \) as well. The two agree, as they must: a determinant is a product of scalars, and the exponent always belongs to the *other* factor's dimension. The tempting wrong answer, \( (\det S)^{3}(\det T)^{2} = 8 \), puts each map's own dimension in its exponent.
:::

## Maps as tensors

We come to the identification that the rest of the chapter runs on. A functional \( \varphi \in V^{*} \) and a vector \( \w \in W \) together determine a linear map \( V \to W \): measure with \( \varphi \), then scale \( \w \) by the answer. That recipe is bilinear in \( (\varphi, \w) \), which is now a reflex: it must come from a linear map on \( V^{*} \otimes W \).

::: {#thm-tensor-hom-iso}
[Tensors Are Maps]

Let \( V \) and \( W \) be **finite-dimensional** vector spaces over \( F \). There is a unique linear map
\[
\Theta \colon V^{*} \otimes W \to \cL(V, W),
\qquad
\Theta(\varphi \otimes \w)(\v) = \varphi(\v)\,\w ,
\]
and it is an isomorphism. Moreover, for \( R \in \cL(V_0, V) \) and \( U \in \cL(W, W_0) \) with \( V_0, W_0 \) finite-dimensional,
\[
\Theta\big((R' \otimes U)(\xi)\big) = U\,\Theta(\xi)\,R
\qquad (\xi \in V^{*} \otimes W),
\]
where \( R' \colon V^{*} \to V_0^{*} \) is the dual map of @def-dual-map and the \( \Theta \) on the left is the one for the pair \( (V_0, W_0) \).
:::

::: {.idea}
Existence is the universal property again. For bijectivity, count: both sides have dimension \( \dim V \cdot \dim W \), so it is enough to see that \( \Theta \) carries a basis onto a basis. It carries \( \varphi_j \otimes \w_i \) to the map whose matrix is the matrix unit \( \E_{ij} \), and the matrix units are a basis. The last formula is the statement that \( \Theta \) turns the tensor product of maps into composition on the two sides; it is checked on simple tensors.
:::

::: {.proof}
**Existence and uniqueness.** For fixed \( \varphi \) and \( \w \), the assignment \( \v \mapsto \varphi(\v)\w \) is linear, so it is an element \( \varphi \cdot \w \) of \( \cL(V, W) \). The map \( (\varphi, \w) \mapsto \varphi \cdot \w \) is bilinear: for every \( \v \),
\[
\begin{aligned}
(\varphi + \psi)(\v)\w &= \varphi(\v)\w + \psi(\v)\w, \\
\varphi(\v)(\w + \w') &= \varphi(\v)\w + \varphi(\v)\w', \\
(c\varphi)(\v)\w &= c\,\varphi(\v)\w = \varphi(\v)(c\w),
\end{aligned}
\]
and two maps agreeing at every \( \v \) are equal. By @def-tensor-product there is a unique linear \( \Theta \) with \( \Theta(\varphi \otimes \w) = \varphi \cdot \w \).

**Bijectivity.** Let \( \sB = (\v_1, \dots, \v_n) \) be a basis of \( V \) with dual basis \( \sB^{*} = (\varphi_1, \dots, \varphi_n) \) (@def-dual-basis), and \( \sC = (\w_1, \dots, \w_m) \) a basis of \( W \). By @thm-tensor-basis the products \( \varphi_j \otimes \w_i \) form a basis of \( V^{*} \otimes W \), of size \( nm \). Now \( \Theta(\varphi_j \otimes \w_i) \) sends \( \v_k \) to \( \varphi_j(\v_k)\w_i = \delta_{jk}\w_i \), so it sends \( \v_j \) to \( \w_i \) and every other basis vector to \( \0 \). By @def-matrix-of-linear-map its matrix is the matrix unit \( \E_{ij} \). The matrix units form a basis of \( M_{m \times n}(F) \) (@exm-standard-bases) and \( T \mapsto \mtx{T}{\sB}{\sC} \) is an isomorphism (@thm-linear-maps-isomorphic-to-matrices), so the \( nm \) maps \( \Theta(\varphi_j \otimes \w_i) \) form a basis of \( \cL(V, W) \).

Hence \( \im \Theta \) contains a basis of \( \cL(V, W) \), so \( \Theta \) is surjective (@thm-image-spanned-by-basis-images). Since \( \dim(V^{*} \otimes W) = nm = \dim \cL(V, W) \), @thm-rank-nullity gives \( \nullity \Theta = 0 \), so \( \Theta \) is injective (@thm-injective-iff-trivial-kernel). Therefore \( \Theta \) is an isomorphism.

**Naturality.** Both \( \xi \mapsto \Theta((R' \otimes U)\xi) \) and \( \xi \mapsto U\,\Theta(\xi)\,R \) are linear in \( \xi \), so by @lem-determined-by-simple-tensors it suffices to check them at \( \xi = \varphi \otimes \w \). On the left, \( (R' \otimes U)(\varphi \otimes \w) = R'\varphi \otimes U\w \), and for \( \v \in V_0 \),
\[
\Theta(R'\varphi \otimes U\w)(\v) = (R'\varphi)(\v)\,U\w = \varphi(R\v)\,U\w ,
\]
using @def-dual-map. On the right, \( \big(U\,\Theta(\varphi \otimes \w)\,R\big)(\v) = U\big(\varphi(R\v)\w\big) = \varphi(R\v)\,U\w \) by linearity of \( U \). The two agree.
:::

::: {.warning}
**Finite dimension is a hypothesis, not decoration.** The map \( \Theta \) is defined and injective for any \( V \) and \( W \), but it is surjective only onto the maps of finite rank: \( \Theta(\sum_{t=1}^{N} \varphi_t \otimes \w_t) \) has image inside \( \Span(\w_1, \dots, \w_N) \), so its rank is at most \( N \). On \( V = W = F[x] \), the identity map has infinite rank and is therefore not \( \Theta(\xi) \) for any \( \xi \in V^{*} \otimes V \). Everything below uses the finite-dimensional statement.
:::

The letter \( \Theta \) is deliberate: taking \( V = F^n \) and \( W = F^m \) and using the dual basis to identify \( (F^n)^{*} \) with \( F^n \), this \( \Theta \) is the isomorphism \( F^m \otimes F^n \cong M_{m \times n}(F) \) of @thm-tensor-fn-matrices, with the two factors written in the order that makes the source a space of *maps* rather than of matrices. Section 02's model was the special case; this is the general statement.

Two uses of the theorem, immediately. First, it names the matrix units: under \( \Theta \), the map with matrix \( \E_{ij} \) *is* the tensor \( \varphi_j \otimes \w_i \), so a matrix is a sum \( \sum_{i,j} a_{ij}\,\varphi_j \otimes \w_i \). Note the index order — the functional carries the column index, the vector the row index — and compare it with Chapter 7's vectorization, which stacks columns.

Second, the naturality formula is the vec identity.

::: {#exm-vec-identity-as-tensor}
[The vec identity, read as a tensor product of maps]

Let \( \A \in M_{k \times m}(F) \) and \( \B \in M_{n \times l}(F) \), and let
\[
\Psi \colon M_{m \times n}(F) \to M_{k \times l}(F), \qquad \X \mapsto \A\X\B ,
\]
which is linear. Identify \( M_{m \times n}(F) \) with \( \cL(F^n, F^m) \) and \( M_{k \times l}(F) \) with \( \cL(F^l, F^k) \). Explain why @thm-vec-identity, \( \vecop(\A\X\B) = (\B\tp \otimes \A)\vecop\X \), is @thm-kronecker-is-tensor applied to \( \Psi \).
:::

::: {.solution}
Let \( R \colon F^l \to F^n \) and \( U \colon F^m \to F^k \) be the maps with matrices \( \B \) and \( \A \) in the standard bases. Under the identification, \( \Psi \) becomes the map \( \cL(F^n, F^m) \to \cL(F^l, F^k) \) sending \( T \) to \( UTR \), so by the naturality clause of @thm-tensor-hom-iso it corresponds, through \( \Theta \), to
\[
R' \otimes U \colon (F^n)^{*} \otimes F^m \to (F^l)^{*} \otimes F^k .
\]
Order the basis of \( (F^n)^{*} \otimes F^m \) as in @def-tensor-basis-ordering, using the dual standard basis \( (\varphi_1, \dots, \varphi_n) \) first and the standard basis \( (\e_1, \dots, \e_m) \) second. Then \( \varphi_j \otimes \e_i \) sits in position \( (j-1)m + i \), and \( \Theta(\varphi_j \otimes \e_i) = \E_{ij} \). By @def-vec-operator, \( \vecop \E_{ij} = \e_{(j-1)m+i} \). So \( \vecop \) **is** the coordinate map of this ordered basis: the dictionary order with the *column* index slow is exactly the order in which vectorization stacks the columns.

Now apply @thm-kronecker-is-tensor. The matrix of \( R' \) in the dual standard bases is \( \B\tp \), because the matrix of a dual map is the transpose (@thm-matrix-of-dual-map), and the matrix of \( U \) is \( \A \). Hence the matrix of \( R' \otimes U \) in the product bases above is \( \B\tp \otimes \A \). Reading that equality of matrices through the coordinate map \( \vecop \) gives \( \vecop(\A\X\B) = (\B\tp \otimes \A)\vecop\X \), which is @thm-vec-identity.

For a numerical check, take \( \A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \) and \( \B = \begin{pmatrix} 3 & 0 \\ 1 & -1 \end{pmatrix} \). Writing the four images \( \A\E_{ij}\B \) in the order \( \E_{11}, \E_{21}, \E_{12}, \E_{22} \) and stacking the four columns \( \vecop(\A\E_{ij}\B) \) side by side gives
\[
\begin{pmatrix}
3 & 6 & 1 & 2 \\
0 & 3 & 0 & 1 \\
0 & 0 & -1 & -2 \\
0 & 0 & 0 & -1
\end{pmatrix},
\]
which is \( \B\tp \otimes \A \) written out.
:::

So the transpose in the vec identity, which Chapter 7 had to warn readers not to get wrong, is not a bookkeeping accident: it is there because \( \Psi \) multiplies \( \X \) on the right by \( \B \), and right multiplication is *precomposition*, which reverses arrows. The dual map is what reverses them, and the matrix of a dual map is a transpose. That is the sharper form of Chapter 7's second promise, and it is why the wrong guesses \( \A \otimes \B\tp \) and \( \B \otimes \A \) are wrong.

## Exercises

### A. Check your understanding

:::: {#exr-tensor-products-of-maps-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the defining property of \( S \otimes T \), and say why writing "\( (S \otimes T)(\v \otimes \w) = S\v \otimes T\w \), extended linearly" is not by itself a definition.
2. Let \( \dim V = 3 \), \( \dim W = 4 \), \( \dim V' = 2 \), \( \dim W' = 5 \). What are the sizes of \( \mtx{S}{\sB}{\sB'} \), \( \mtx{T}{\sC}{\sC'} \) and \( \mtx{S \otimes T}{\sB \otimes \sC}{\sB' \otimes \sC'} \)?
3. In the ordering of @def-tensor-basis-ordering with \( \dim V = 3 \) and \( \dim W = 4 \), which basis vector of \( V \otimes W \) sits in position \( 7 \)?
4. True or false: every operator on \( V \otimes W \) is of the form \( S \otimes T \). Justify your answer.
5. State @thm-tensor-hom-iso, including its hypothesis, and say what \( \Theta(\varphi \otimes \w) \) does to a vector \( \v \).
:::
::::

::: {.solution}
(a) \( S \otimes T \) is the **unique** linear map \( V \otimes W \to V' \otimes W' \) with \( (S \otimes T)(\v \otimes \w) = S\v \otimes T\w \) for all \( \v, \w \) (@def-tensor-of-maps). The quoted phrase is not a definition because a general element of \( V \otimes W \) is a sum of simple tensors in many different ways, so a prescription on simple tensors may be inconsistent; \( \v \otimes \0 = \0 \) already forces consistency conditions. What makes it work is that \( (\v, \w) \mapsto S\v \otimes T\w \) is bilinear, so @def-tensor-product supplies the map.

(b) \( 2 \times 3 \), \( 5 \times 4 \), and \( 10 \times 12 \) (@thm-kronecker-is-tensor: an \( m \times n \) and a \( p \times q \) matrix give an \( mp \times nq \) one).

(c) With \( q = 4 \), position \( 7 = (i-1)\cdot 4 + k \) forces \( i = 2 \), \( k = 3 \). So it is \( \v_2 \otimes \w_3 \).

(d) False. By @cor-tensor-map-invariants, \( \rank(S \otimes T) = \rank S \cdot \rank T \). With \( \dim V = \dim W = 2 \), an operator of rank \( 3 \) on the \( 4 \)-dimensional space \( V \otimes W \) cannot have its rank factored as a product of two integers each at most \( 2 \).

(e) For \( V, W \) **finite-dimensional**, there is a unique linear \( \Theta \colon V^{*} \otimes W \to \cL(V, W) \) with \( \Theta(\varphi \otimes \w)(\v) = \varphi(\v)\w \), and it is an isomorphism. So \( \Theta(\varphi \otimes \w) \) measures \( \v \) with \( \varphi \) and scales \( \w \) by the result.
:::

### B. Practice

:::: {#exr-tensor-products-of-maps-b1}
[B1: A tensor product of maps, two ways]

Let \( S \colon \nQ^2 \to \nQ^2 \) and \( T \colon \nQ^2 \to \nQ^3 \) have matrices, in the standard bases,
\[
\A = \begin{pmatrix} 1 & -1 \\ 2 & 0 \end{pmatrix}, \qquad
\B = \begin{pmatrix} 1 & 0 \\ 0 & 2 \\ -1 & 1 \end{pmatrix}.
\]

::: {.enumerate options="label=(\alph*)"}
1. Write down \( \mtx{S \otimes T}{\sB \otimes \sC}{\sB' \otimes \sC'} \) for the standard bases, ordered as in @def-tensor-basis-ordering.
2. Compute \( (S \otimes T)(\e_1 \otimes \e_2 - \e_2 \otimes \e_1) \) directly from @def-tensor-of-maps.
3. Check (b) against (a) by multiplying the matrix by the coordinate column of the input.
:::
::::

::: {.solution}
(a) By @thm-kronecker-is-tensor the matrix is \( \A \otimes \B \), of size \( 6 \times 4 \):
\[
\A \otimes \B =
\begin{pmatrix}
1 & 0 & -1 & 0 \\
0 & 2 & 0 & -2 \\
-1 & 1 & 1 & -1 \\
2 & 0 & 0 & 0 \\
0 & 4 & 0 & 0 \\
-2 & 2 & 0 & 0
\end{pmatrix}.
\]

(b) The columns of \( \A \) give \( S\e_1 = \e_1 + 2\e_2 \) and \( S\e_2 = -\e_1 \); the columns of \( \B \) give \( T\e_1 = \f_1 - \f_3 \) and \( T\e_2 = 2\f_2 + \f_3 \), where \( (\f_1, \f_2, \f_3) \) is the standard basis of \( \nQ^3 \). Hence
\[
\begin{aligned}
&(S \otimes T)(\e_1 \otimes \e_2 - \e_2 \otimes \e_1) \\
&\quad = (\e_1 + 2\e_2) \otimes (2\f_2 + \f_3) - (-\e_1) \otimes (\f_1 - \f_3) \\
&\quad = \e_1 \otimes \f_1 + 2\,\e_1 \otimes \f_2 + 4\,\e_2 \otimes \f_2 + 2\,\e_2 \otimes \f_3 ,
\end{aligned}
\]
where the \( \e_1 \otimes \f_3 \) terms cancel: \( +1 \) from the first product and \( -1 \) from the second.

(c) The input has coordinates \( (0, 1, -1, 0) \) in the basis \( (\e_1 \otimes \e_1, \e_1 \otimes \e_2, \e_2 \otimes \e_1, \e_2 \otimes \e_2) \). Multiplying gives \( (1, 2, 0, 0, 4, 2) \), which in the basis \( (\e_1 \otimes \f_1, \e_1 \otimes \f_2, \e_1 \otimes \f_3, \e_2 \otimes \f_1, \e_2 \otimes \f_2, \e_2 \otimes \f_3) \) is exactly the answer to (b).
:::

:::: {#exr-tensor-products-of-maps-b2}
[B2: Invariants without multiplying matrices]

Let \( S \in \cL(V) \) and \( T \in \cL(W) \) over \( \nR \), with \( \dim V = 4 \), \( \dim W = 3 \), \( \rank S = 2 \), \( \rank T = 3 \), \( \tr S = 5 \), \( \tr T = -2 \), \( \det T = 6 \).

::: {.enumerate options="label=(\alph*)"}
1. Find \( \rank(S \otimes T) \) and \( \nullity(S \otimes T) \).
2. Find \( \tr(S \otimes T) \).
3. Find \( \det(S \otimes T) \). Justify the value from the ranks alone.
4. Find \( \tr(S \otimes \id_W) \) and \( \tr(\id_V \otimes T) \), and check that their product is **not** \( \tr(S \otimes T) \) in general by comparing with (b).
:::
::::

::: {.solution}
(a) By @cor-tensor-map-invariants, \( \rank(S \otimes T) = 2 \cdot 3 = 6 \). Since \( \dim(V \otimes W) = 12 \) by @thm-tensor-basis, @thm-rank-nullity gives \( \nullity(S \otimes T) = 12 - 6 = 6 \).

(b) \( \tr(S \otimes T) = 5 \cdot (-2) = -10 \).

(c) \( \rank S = 2 < 4 = \dim V \), so \( S \) is not invertible and \( \det S = 0 \) by @thm-invertible-tfae and @def-det-operator. Hence \( \det(S \otimes T) = 0^{3} \cdot 6^{4} = 0 \). Directly: \( \rank(S \otimes T) = 6 < 12 \), so \( S \otimes T \) is not invertible.

(d) \( \tr(S \otimes \id_W) = \tr S \cdot \tr \id_W = 5 \cdot 3 = 15 \) and \( \tr(\id_V \otimes T) = 4 \cdot (-2) = -8 \), using \( \tr \id = (\dim) \cdot 1 \) from @thm-trace-operator-properties. Their product is \( -120 \ne -10 \). There is no contradiction: \( S \otimes T \) is the *composite* of the two, and the trace of a composite is not the product of the traces.
:::

:::: {#exr-tensor-products-of-maps-b3}
[B3: Which statements hold?]

Let \( V, W \) be finite-dimensional over \( F \). Determine which of the following hold for **all** \( S, S_1, S_2 \in \cL(V) \) and \( T \in \cL(W) \). Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( (S_1S_2) \otimes T = (S_1 \otimes T)(S_2 \otimes T) \).
2. \( (S_1S_2) \otimes T^2 = (S_1 \otimes T)(S_2 \otimes T) \).
3. \( S \otimes T = 0 \) implies \( S = 0 \) or \( T = 0 \).
4. \( S \otimes \id_W \) and \( \id_V \otimes T \) commute.
5. If \( S \) and \( T \) are invertible, so is \( S \otimes T \), with inverse \( S^{-1} \otimes T^{-1} \).
:::
::::

::: {.solution}
(a) Fails. By @prp-tensor-of-maps-algebra (c) the right side is \( S_1S_2 \otimes T^2 \), and with \( S_1 = S_2 = \id_V \) and \( T = 2\,\id_W \) over \( \nQ \) the two sides are \( 2\,\id \) and \( 4\,\id \) on \( V \otimes W \), by Example 3 after @def-tensor-of-maps.

(b) Holds: it is exactly @prp-tensor-of-maps-algebra (c).

(c) Holds. If \( S \ne 0 \) and \( T \ne 0 \), then \( \rank S \ge 1 \) and \( \rank T \ge 1 \), so \( \rank(S \otimes T) \ge 1 \) by @cor-tensor-map-invariants, and \( S \otimes T \ne 0 \).

(d) Holds. By @prp-tensor-of-maps-algebra (c) and (d), both composites equal \( S \otimes T \).

(e) Holds. By @prp-tensor-of-maps-algebra (c) and (d), \( (S \otimes T)(S^{-1} \otimes T^{-1}) = \id_V \otimes \id_W = \id_{V \otimes W} \), and likewise in the other order.
:::

### C. Going deeper

:::: {#exr-tensor-products-of-maps-c1}
[C1: When a tensor product of maps vanishes]

Let \( V, V', W, W' \) be finite-dimensional over \( F \), \( S \in \cL(V, V') \) and \( T \in \cL(W, W') \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( S \otimes T = 0 \) if and only if \( S = 0 \) or \( T = 0 \).
2. Prove that \( \ker(S \otimes \id_W) = \ker S \otimes W \), meaning the span of all \( \v \otimes \w \) with \( \v \in \ker S \).
3. Deduce \( \nullity(S \otimes \id_W) = \nullity S \cdot \dim W \), and check it against @cor-tensor-map-invariants.
:::
::::

::: {.solution}
(a) \( (\Leftarrow) \) If \( S = 0 \), then \( (S \otimes T)(\v \otimes \w) = \0 \otimes T\w = \0 \) for all \( \v, \w \), so \( S \otimes T = 0 \) by @lem-determined-by-simple-tensors. Likewise if \( T = 0 \). \( (\Rightarrow) \) Suppose \( S \ne 0 \) and \( T \ne 0 \). Then \( \rank S \ge 1 \) and \( \rank T \ge 1 \), so \( \rank(S \otimes T) = \rank S \cdot \rank T \ge 1 \) by @cor-tensor-map-invariants, and \( S \otimes T \ne 0 \).

(b) \( (\supseteq) \) For \( \v \in \ker S \) and \( \w \in W \), \( (S \otimes \id_W)(\v \otimes \w) = \0 \otimes \w = \0 \); a kernel is a subspace (@thm-prop-kernel), so it contains the span of these elements. \( (\subseteq) \) Choose a basis \( (\v_1, \dots, \v_n) \) of \( V \) whose last \( n - r \) vectors span \( \ker S \), where \( r = \rank S \), and such that \( S\v_1, \dots, S\v_r \) are independent (as in the proof of @cor-tensor-map-invariants). Let \( (\w_1, \dots, \w_q) \) be a basis of \( W \) and let \( z = \sum_{j,l} c_{jl}\,\v_j \otimes \w_l \) lie in the kernel. Then
\[
\0 = (S \otimes \id_W)(z) = \sum_{j \le r}\sum_{l} c_{jl}\,S\v_j \otimes \w_l ,
\]
and the vectors \( S\v_j \otimes \w_l \) with \( j \le r \) are linearly independent by @thm-tensor-basis, after extending \( (S\v_1, \dots, S\v_r) \) to a basis of \( V' \). Hence \( c_{jl} = 0 \) for all \( j \le r \), so \( z \) is a combination of the \( \v_j \otimes \w_l \) with \( j > r \), all of which lie in \( \ker S \otimes W \).

(c) By (b) and @thm-tensor-basis applied to \( \ker S \) and \( W \), \( \nullity(S \otimes \id_W) = \dim \ker S \cdot \dim W = \nullity S \cdot \dim W \). Consistency: @cor-tensor-map-invariants gives \( \rank(S \otimes \id_W) = \rank S \cdot \dim W \), and adding the two gives \( (\rank S + \nullity S)\dim W = \dim V \cdot \dim W = \dim(V \otimes W) \), as @thm-rank-nullity requires.
:::

:::: {#exr-tensor-products-of-maps-c2}
[C2: Rank-one maps and simple tensors]

Let \( V, W \) be finite-dimensional over \( F \) and let \( \Theta \) be the isomorphism of @thm-tensor-hom-iso.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \Theta(\xi) \) has rank at most \( 1 \) if and only if \( \xi \) is a simple tensor \( \varphi \otimes \w \).
2. Deduce that "not every tensor is simple" (§02) says exactly that not every linear map has rank at most \( 1 \), and identify the tensor corresponding to \( \id_V \) in a basis.
3. Let \( \dim V = \dim W = 2 \). Exhibit \( \xi \in V^{*} \otimes W \) that is not simple, by exhibiting a map of rank \( 2 \).
:::
::::

::: {.solution}
(a) \( (\Leftarrow) \) \( \Theta(\varphi \otimes \w) \) sends every \( \v \) into \( \Span(\w) \), so its image has dimension at most \( 1 \). \( (\Rightarrow) \) Suppose \( R \coloneqq \Theta(\xi) \) has rank at most \( 1 \). If \( R = 0 \), then \( \xi = 0 = 0 \otimes \0 \) since \( \Theta \) is injective. Otherwise \( \im R = \Span(\w) \) for some \( \w \ne \0 \), so for each \( \v \) there is a unique scalar \( \varphi(\v) \) with \( R\v = \varphi(\v)\w \); uniqueness and linearity of \( R \) make \( \varphi \) linear, so \( \varphi \in V^{*} \). Then \( R = \Theta(\varphi \otimes \w) \), and \( \xi = \varphi \otimes \w \) because \( \Theta \) is injective.

(b) By (a) and bijectivity of \( \Theta \), the non-simple tensors in \( V^{*} \otimes W \) correspond exactly to the maps of rank at least \( 2 \). Taking \( W = V \) with basis \( \sB = (\v_1, \dots, \v_n) \) and dual basis \( (\varphi_1, \dots, \varphi_n) \), the matrix of \( \id_V \) is \( \I_n = \sum_i \E_{ii} \), so \( \id_V = \Theta\big(\sum_{i=1}^{n} \varphi_i \otimes \v_i\big) \). For \( n \ge 2 \) this has rank \( n \ge 2 \), hence is not simple. For \( n = 2 \) it is the witness \( \varphi_1 \otimes \v_1 + \varphi_2 \otimes \v_2 \), which is @exm-non-simple-tensor read through \( \Theta \).

(c) Take \( \xi = \varphi_1 \otimes \w_1 + \varphi_2 \otimes \w_2 \) for bases \( (\v_1, \v_2) \) of \( V \) and \( (\w_1, \w_2) \) of \( W \). Then \( \Theta(\xi) \) sends \( \v_1 \mapsto \w_1 \) and \( \v_2 \mapsto \w_2 \), so it has rank \( 2 \), and by (a) \( \xi \) is not simple.
:::

:::: {#exr-tensor-products-of-maps-c3}
[C3: Reproving the swap]

Let \( V \) and \( W \) be finite-dimensional over \( F \) with ordered bases \( \sB \) and \( \sC \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that there is a unique isomorphism \( \tau \colon V \otimes W \to W \otimes V \) with \( \tau(\v \otimes \w) = \w \otimes \v \).
2. Prove that \( \tau(S \otimes T) = (T \otimes S)\tau \) for all \( S \in \cL(V) \), \( T \in \cL(W) \).
3. Deduce @prp-kronecker-swap-similar: for \( \A \in M_n(F) \) and \( \B \in M_m(F) \) there is a permutation matrix \( \P \) with \( \B \otimes \A = \P^{-1}(\A \otimes \B)\P \), and identify \( \P \).
:::

*Hint for (c): think of \( \tau \) as renaming basis vectors rather than as moving them.*
::::

::: {.solution}
(a) The map \( (\v, \w) \mapsto \w \otimes \v \) is bilinear, so @def-tensor-product gives a unique linear \( \tau \) with \( \tau(\v \otimes \w) = \w \otimes \v \). The same construction with the roles swapped gives \( \sigma \colon W \otimes V \to V \otimes W \) with \( \sigma(\w \otimes \v) = \v \otimes \w \). Then \( \sigma\tau \) fixes every simple tensor, so \( \sigma\tau = \id \) by @lem-determined-by-simple-tensors, and likewise \( \tau\sigma = \id \). Hence \( \tau \) is an isomorphism.

(b) Both sides are linear maps out of \( V \otimes W \), so by @lem-determined-by-simple-tensors compare at \( \v \otimes \w \): the left gives \( \tau(S\v \otimes T\w) = T\w \otimes S\v \), and the right gives \( (T \otimes S)(\w \otimes \v) = T\w \otimes S\v \).

(c) Let \( S, T \) be the operators on \( F^n, F^m \) with matrices \( \A, \B \). Both \( \sB \otimes \sC \) and \( \tau^{-1}(\sC \otimes \sB) \) are orderings of the same basis of \( F^n \otimes F^m \), differing by the permutation \( \sigma \) that sends position \( (k-1)n + i \) to position \( (i-1)m + k \) — the direction matters, since \( \sigma \) is not an involution unless \( n = m \) — and let \( \P \) be its matrix, which is exactly the \( \P_\sigma \) built in the proof of @prp-kronecker-swap-similar.
:::
