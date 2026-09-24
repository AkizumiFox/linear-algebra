# The Tensor Product

The previous section ended with a wish: a space through which every bilinear map out of \( V \times W \) becomes a **linear** map. This section grants it. The object is called the tensor product, and building it is the main technical work of the chapter — but the way we go about it matters more than the object itself, because the same three moves recur four more times, for the tensor algebra, the symmetric powers, the exterior powers and the Clifford algebra.

The three moves are: **state what the object must do**, in the form of a property of the maps out of it; **prove that any two objects doing it are isomorphic by a unique isomorphism**, using nothing but that property; and only then **construct one**, to know that the definition is not empty. The middle move is what licenses the word "the". @thm-tensor-unique below is written out at full length and is the template for the rest of the chapter, so it is worth reading twice.

Throughout, \( F \) is a field and all vector spaces are over \( F \). No finite-dimensionality is assumed until we reach bases, where it is stated.

## What the object has to do

Here is the goal, stated before its terms are defined. We want a space \( X \) and a bilinear map \( \tau \colon V \times W \to X \) such that *every bilinear map \( \beta \) out of \( V \times W \) can be pushed through \( \tau \), and what comes out the other side is linear.* Two demands hide in that sentence. There must be **at least one** way to push \( \beta \) through, or the property is useless; and **at most one**, or we cannot recover \( \beta \) from its linear shadow. So we ask for existence and uniqueness together.

*A tensor product is the most efficient bilinear map out of \( V \times W \): every other one is it, followed by a single linear map.*

::: {#def-tensor-product}
[Tensor Product]

Let \( V \) and \( W \) be vector spaces over \( F \). A **tensor product of \( V \) and \( W \)** is a pair \( (X, \tau) \), where \( X \) is a vector space over \( F \) and \( \tau \colon V \times W \to X \) is a bilinear map, satisfying:

::: {.enumerate options="label=(T\arabic*)"}
1. (**universal property**) **For every** vector space \( Z \) over \( F \) and **every** bilinear map \( \beta \colon V \times W \to Z \), there is a **unique** linear map \( \bar\beta \colon X \to Z \) with \( \bar\beta \circ \tau = \beta \).
:::
:::

In words, clause by clause. **For every \( Z \):** the property is a demand about *all* targets at once, not about one favorite target. **Every bilinear \( \beta \):** the arbitrary bilinear map is the input; nothing is assumed about it beyond @def-multilinear-map with \( k = 2 \). **There is a unique linear \( \bar\beta \):** exactly one, so both existence and uniqueness are being asserted. **With \( \bar\beta \circ \tau = \beta \):** this is an equality of functions on \( V \times W \), namely \( \bar\beta(\tau(\v, \w)) = \beta(\v, \w) \) for all \( \v, \w \). We say \( \beta \) **factors through** \( \tau \), and picture it as a triangle: the two routes from \( V \times W \) to \( Z \), one direct and one through \( X \), give the same answer.

Notice what the definition does **not** say. It says nothing about the elements of \( X \), nothing about a formula, and nothing about a basis: it is a statement purely about maps. That is deliberate, since a definition naming elements would depend on a construction, and there are several.

::: {.warning}
**The definition does not say that every element of \( X \) has the form \( \tau(\v, \w) \).** It says that the values \( \tau(\v, \w) \) are enough to *determine* a linear map on \( X \) — which, as we prove below, means they span \( X \), not that they exhaust it. Sums of them are generally not of that form. This is the single most common misreading of the tensor product, and we return to it with a proof at the end of the section.
:::

## Any two tensor products are the same

Before building anything, we settle the word "the". If two pairs both satisfy (T1), each one's property produces a map to the other, and the composites have no choice but to be identities. This is the argument Chapter 14 used for the Clifford algebra (@prp-clifford-uniqueness), and it is the argument we will use in four more sections.

::: {#thm-tensor-unique}
[Uniqueness of the Tensor Product]

Let \( V \) and \( W \) be vector spaces over \( F \), and let \( (X, \tau) \) and \( (X', \tau') \) both be tensor products of \( V \) and \( W \). Then there is a **unique** isomorphism \( \varphi \colon X \to X' \) with \( \varphi \circ \tau = \tau' \).
:::

::: {.idea}
Three steps. ① Each pair's universal property, applied with the *other* pair's bilinear map as input, produces a linear map; so we get \( \varphi \colon X \to X' \) and \( \psi \colon X' \to X \) at once, for free. ② Compose them. The composite \( \psi\varphi \) is a linear self-map of \( X \) that does nothing to \( \tau \) — and so is the identity. ③ The uniqueness half of (T1), applied with \( Z = X \) and \( \beta = \tau \), says there is only **one** linear self-map doing nothing to \( \tau \). So the two coincide. The uniqueness half is the engine; without it the argument produces two maps and no reason for them to be inverse.
:::

::: {.proof}
**Step 1.** The map \( \tau' \colon V \times W \to X' \) is bilinear. Apply (T1) for \( (X, \tau) \) with \( Z = X' \) and \( \beta = \tau' \): there is a unique linear \( \varphi \colon X \to X' \) with \( \varphi \circ \tau = \tau' \). Symmetrically, applying (T1) for \( (X', \tau') \) with \( Z = X \) and \( \beta = \tau \) gives a unique linear \( \psi \colon X' \to X \) with \( \psi \circ \tau' = \tau \).

**Step 2.** The composite \( \psi\varphi \colon X \to X \) is linear (@thm-composition-linear (a)), and
\[
(\psi\varphi) \circ \tau = \psi \circ (\varphi \circ \tau) = \psi \circ \tau' = \tau .
\]
The identity \( \id_X \) is also linear and satisfies \( \id_X \circ \tau = \tau \).

**Step 3.** Apply (T1) for \( (X, \tau) \) with \( Z = X \) and \( \beta = \tau \), which is bilinear by hypothesis. It says there is **exactly one** linear map \( X \to X \) whose composite with \( \tau \) is \( \tau \). Both \( \psi\varphi \) and \( \id_X \) are such maps. Hence \( \psi\varphi = \id_X \). Swapping the roles of \( (X, \tau) \) and \( (X', \tau') \) gives \( \varphi\psi = \id_{X'} \).

So \( \varphi \) has a two-sided inverse and is a bijection, hence an isomorphism (@thm-inverse-is-linear). It is the unique isomorphism with \( \varphi \circ \tau = \tau' \), because (T1) already produced it as the unique **linear** map with that property, and an isomorphism is in particular linear. This proves the theorem.
:::

**Aftermath, and the template.** Read the proof again with the names removed. It says: *an object defined by a universal property is determined up to a unique isomorphism compatible with its structure map, because each object's property hands you a comparison map, and the uniqueness clause forces the composites to be identities.* Nothing in it used bilinearity, or vector spaces, or two factors. Sections 06, 07, 08 and 10 define the tensor algebra, the symmetric power, the exterior power and the Clifford algebra by universal properties of exactly this shape, and each time the uniqueness proof is these three steps with different letters. When you meet them, do not reread the argument; recognize it.

Because of @thm-tensor-unique we may now speak of **the** tensor product and fix notation.

::: {#def-tensor-notation}
[Notation for Tensors]

When a tensor product of \( V \) and \( W \) exists, we write it \( V \otimes W \), write \( \v \otimes \w \) for \( \tau(\v, \w) \), and call an element of the form \( \v \otimes \w \) a **simple tensor** (also called a *pure* or *decomposable* tensor). The defining property then reads: every bilinear \( \beta \colon V \times W \to Z \) has a unique linear \( \bar\beta \colon V \otimes W \to Z \) with \( \bar\beta(\v \otimes \w) = \beta(\v, \w) \).
:::

Bilinearity of \( \tau \), rewritten in this notation, gives the rules we compute with:
\[
\begin{aligned}
(\v + \v') \otimes \w &= \v \otimes \w + \v' \otimes \w, \\
\v \otimes (\w + \w') &= \v \otimes \w + \v \otimes \w', \\
(c\v) \otimes \w = c(\v \otimes \w) &= \v \otimes (c\w) .
\end{aligned}
\]
The third line is the one to remember: **a scalar moves freely across the \( \otimes \) sign.** That is the whole reason \( \v \otimes \w \) does not determine \( \v \) and \( \w \).

## Building one: a free space modulo relations

Uniqueness is worthless if nothing satisfies (T1), so we construct a tensor product. The strategy is the one named in the chapter introduction: *take a space in which the symbols \( \v \otimes \w \) are completely unrelated, then divide out exactly the relations bilinearity demands.* Both halves need a tool.

The first tool is a space with a basis indexed by an arbitrary set. It is the space of finitely supported functions, which Chapter 1 met for \( S = \nN \) (@exr-infinite-dimensional-b1).

::: {#def-free-vector-space}
[Free Vector Space on a Set]

Let \( S \) be a set and \( F \) a field. The **free vector space on \( S \) over \( F \)** is
\[
F^{(S)} \coloneqq \{\, f \colon S \to F \ :\ f(s) = 0 \text{ for all but finitely many } s \,\},
\]
a subset of the space \( F^{S} \) of all functions \( S \to F \) (@exm-vector-spaces (d)), with the pointwise operations. For \( s \in S \), let \( \delta_s \in F^{(S)} \) be the function with \( \delta_s(s) = 1 \) and \( \delta_s(t) = 0 \) for \( t \ne s \).
:::

::: {#lem-free-vector-space}
[Universal Property of the Free Vector Space]

Let \( S \) be a set and \( F \) a field.

::: {.enumerate options="label=(\alph*)"}
1. \( F^{(S)} \) is a subspace of \( F^{S} \), and \( \{\delta_s : s \in S\} \) is a basis of it.
2. For **every** vector space \( Z \) over \( F \) and **every** function \( g \colon S \to Z \) — no structure on \( g \) is assumed, since \( S \) is only a set — there is **exactly one** linear map \( \bar g \colon F^{(S)} \to Z \) with \( \bar g(\delta_s) = g(s) \) for all \( s \in S \).
:::
:::

::: {.proof}
(a) We use @thm-subspace-test. The zero function vanishes everywhere, so it lies in \( F^{(S)} \). If \( f, h \in F^{(S)} \) vanish outside the finite sets \( A \) and \( B \), then \( f + h \) vanishes outside \( A \cup B \), which is finite, and \( cf \) vanishes outside \( A \). So \( F^{(S)} \) is a subspace.

Each \( \delta_s \) lies in \( F^{(S)} \). *Spanning:* if \( f \in F^{(S)} \) is non-zero exactly on the finite set \( \{s_1, \dots, s_r\} \), then \( f \) and \( \sum_{i} f(s_i)\delta_{s_i} \) take the same value at every point of \( S \), hence are equal. *Independence:* if \( \sum_{i} a_i\delta_{s_i} = 0 \) for distinct \( s_1, \dots, s_r \), evaluate at \( s_j \) to get \( a_j = 0 \). By @def-basis, \( \{\delta_s\} \) is a basis, possibly infinite in the sense of @thm-basis-extension-general.

(b) Immediate from (a) and @thm-linear-map-from-any-basis, which prescribes a linear map arbitrarily on a basis, in one and only one way.
:::

In words: **a function on a set becomes a linear map on the free space, for free.** That is the point of the construction, and the whole of it: \( F^{(S)} \) imposes no relations among the \( \delta_s \), so nothing can obstruct a prescription.

The second tool is the quotient. Chapter 2 recorded exactly the statement we need: a linear map that kills a subspace \( U \) passes, in exactly one way, to a linear map on \( V/U \) (@thm-quotient-universal-property (a)). We use it in the form "to define a map out of a quotient, define it upstairs and check it kills the relations".

::: {#thm-tensor-exists}
[Existence of the Tensor Product]

For every pair of vector spaces \( V, W \) over \( F \), a tensor product \( (X, \tau) \) of \( V \) and \( W \) exists.
:::

::: {.idea}
Write down the symbols \( \v \otimes \w \) as a basis of a huge space \( P \), one basis vector for each **pair** of vectors — so at this stage \( \v \otimes \w \) has no properties at all. The four bilinearity rules are then four families of elements of \( P \) that we want to be zero, so divide by the subspace they span. A bilinear \( \beta \) becomes a linear map on \( P \) by @lem-free-vector-space, kills each relation because it is bilinear, and therefore passes to the quotient by @thm-quotient-universal-property. Uniqueness of the induced map is spanning: the cosets of the basis vectors span the quotient.
:::

::: {.proof}
Let \( S = V \times W \), regarded as a **set**, and let \( P = F^{(S)} \) be the free vector space on it (@def-free-vector-space), with basis \( \{\delta_{(\v, \w)}\} \). Let \( R \subseteq P \) be the span of all elements of the four forms
\[
\begin{aligned}
&\delta_{(\v + \v',\, \w)} - \delta_{(\v, \w)} - \delta_{(\v', \w)}, \qquad
\delta_{(\v,\, \w + \w')} - \delta_{(\v, \w)} - \delta_{(\v, \w')}, \\
&\delta_{(c\v,\, \w)} - c\,\delta_{(\v, \w)}, \qquad\qquad\qquad\ \
\delta_{(\v,\, c\w)} - c\,\delta_{(\v, \w)},
\end{aligned}
\]
taken over all \( \v, \v' \in V \), all \( \w, \w' \in W \) and all \( c \in F \). A span is a subspace, so \( R \) is one. Put
\[
X \coloneqq P/R, \qquad \tau(\v, \w) \coloneqq \pi\bigl(\delta_{(\v, \w)}\bigr),
\]
where \( \pi \colon P \to P/R \) is the quotient map, which is linear with kernel \( R \) (@thm-quotient-space-operations-well-defined).

*\( \tau \) is bilinear.* The element \( \delta_{(\v + \v', \w)} - \delta_{(\v, \w)} - \delta_{(\v', \w)} \) lies in \( R = \ker \pi \), so applying \( \pi \) and using its linearity gives \( \tau(\v + \v', \w) - \tau(\v, \w) - \tau(\v', \w) = \0 \). The other three families give, in the same way, additivity in the second slot and the two scalar rules. These are the clauses of @def-multilinear-map for \( k = 2 \).

*(T1), existence.* Let \( Z \) be a vector space and \( \beta \colon V \times W \to Z \) bilinear. Regarding \( \beta \) as a **function** on the set \( S \), @lem-free-vector-space (b) gives a unique linear \( b \colon P \to Z \) with \( b(\delta_{(\v, \w)}) = \beta(\v, \w) \). It kills every generator of \( R \): for instance
\[
b\bigl(\delta_{(\v + \v', \w)} - \delta_{(\v, \w)} - \delta_{(\v', \w)}\bigr)
= \beta(\v + \v', \w) - \beta(\v, \w) - \beta(\v', \w) = \0
\]
because \( \beta \) is linear in its first slot, and the other three families vanish by the other three clauses of bilinearity. Since \( b \) is linear and vanishes on a spanning set of \( R \), it vanishes on \( R \) (@thm-linear-combination); that is, \( R \subseteq \ker b \). By @thm-quotient-universal-property (a) there is exactly one linear \( \bar\beta \colon X \to Z \) with \( \bar\beta \circ \pi = b \), and then
\[
\bar\beta(\tau(\v, \w)) = \bar\beta\bigl(\pi(\delta_{(\v, \w)})\bigr) = b\bigl(\delta_{(\v, \w)}\bigr) = \beta(\v, \w),
\]
so \( \bar\beta \circ \tau = \beta \).

*(T1), uniqueness.* Suppose \( L \colon X \to Z \) is linear with \( L \circ \tau = \beta \). Since \( \pi \) is surjective and the \( \delta_{(\v, \w)} \) span \( P \), the elements \( \tau(\v, \w) = \pi(\delta_{(\v,\w)}) \) span \( X \). On each of them, \( L \) and \( \bar\beta \) agree, both giving \( \beta(\v, \w) \). Two linear maps that agree on a spanning set agree everywhere, by @thm-linear-combination. Hence \( L = \bar\beta \).

So \( (X, \tau) \) satisfies (T1), which proves the theorem.
:::

**Aftermath.** The construction is ugly and the object is not. That is normal for a universal property: the model is a scaffolding, and after this proof we never open it again. Every later fact about \( V \otimes W \) in this book is derived from (T1), never from cosets of formal sums — which is also why the identification \( F^m \otimes F^n \cong M_{m \times n}(F) \) below is legitimate as an alternative model, and much more pleasant to compute in.

One property is worth extracting at once, because we will use it constantly and because it is the second appearance of the self-map trick.

::: {#prp-simple-tensors-span}
[Simple Tensors Span]

Let \( (V \otimes W, \tau) \) be a tensor product. Then \( V \otimes W = \Span\{\, \v \otimes \w : \v \in V, \ \w \in W \,\} \).
:::

::: {.proof}
Let \( Y = \Span\{\v \otimes \w\} \), a subspace of \( V \otimes W \), and let \( j \colon Y \to V \otimes W \) be the inclusion, which is linear. Restricting the codomain of \( \tau \) gives a bilinear map \( \tau_Y \colon V \times W \to Y \), \( (\v, \w) \mapsto \v \otimes \w \); it is bilinear because \( \tau \) is and because \( Y \) is a subspace, so the identities hold already in \( Y \). By (T1) with \( Z = Y \) there is a linear \( L \colon V \otimes W \to Y \) with \( L \circ \tau = \tau_Y \). Then \( jL \) is a linear self-map of \( V \otimes W \) with \( jL\tau = j\tau_Y = \tau \), and so is \( \id \). By the uniqueness clause of (T1) with \( Z = V \otimes W \) and \( \beta = \tau \), we get \( jL = \id \). Hence \( j \) is surjective, so \( Y = V \otimes W \).
:::

::: {.remark}
That proof used no basis, no construction and no finite dimension — only (T1). It is the same three lines as Step 1 of @prp-clifford-spanning's proof in Chapter 14, where the generated subalgebra was shown to be everything. Once you see "a subobject that receives the structure map must be the whole thing", you can reuse it verbatim.
:::

## A basis and a dimension

Now we can count. The prediction at the end of the previous section was \( \dim(V \otimes W) = (\dim V)(\dim W) \), and here it is, with a basis attached.

::: {#thm-tensor-basis}
[Basis of a Tensor Product]

Let \( V \) and \( W \) be finite-dimensional, with bases \( (\v_1, \dots, \v_n) \) of \( V \) and \( (\w_1, \dots, \w_m) \) of \( W \). Then the \( nm \) simple tensors
\[
\v_i \otimes \w_j, \qquad 1 \le i \le n, \quad 1 \le j \le m,
\]
form a basis of \( V \otimes W \). In particular \( \dim(V \otimes W) = (\dim V)(\dim W) \).
:::

::: {.idea}
Spanning is bilinearity: expand both slots of a simple tensor and use @prp-simple-tensors-span. Independence needs linear functionals on \( V \otimes W \) that pick out one coefficient — and (T1) manufactures functionals out of bilinear forms, while @thm-dual-basis supplies all the bilinear forms we could want, namely \( (\x, \y) \mapsto \varphi_p(\x)\psi_q(\y) \).
:::

::: {.proof}
*Spanning.* By @prp-simple-tensors-span it suffices to write each simple tensor in terms of the listed ones. Let \( \v = \sum_i a_i\v_i \) and \( \w = \sum_j b_j\w_j \). Expanding one slot at a time by the rules following @def-tensor-notation,
\[
\v \otimes \w = \Bigl(\sum_i a_i \v_i\Bigr) \otimes \Bigl(\sum_j b_j\w_j\Bigr) = \sum_{i,j} a_ib_j\,(\v_i \otimes \w_j).
\]

*Independence.* Let \( (\varphi_1, \dots, \varphi_n) \) and \( (\psi_1, \dots, \psi_m) \) be the bases of \( V^{*} \) and \( W^{*} \) dual to the given ones, so \( \varphi_p(\v_i) = \delta_{pi} \) and \( \psi_q(\w_j) = \delta_{qj} \) (@thm-dual-basis). Fix \( p \) and \( q \). The function
\[
\beta_{pq} \colon V \times W \to F, \qquad \beta_{pq}(\x, \y) = \varphi_p(\x)\,\psi_q(\y),
\]
is bilinear: freezing \( \y \) leaves \( \psi_q(\y)\varphi_p \), a scalar multiple of a linear functional, and symmetrically. By (T1) there is a linear \( f_{pq} \colon V \otimes W \to F \) with \( f_{pq}(\x \otimes \y) = \varphi_p(\x)\psi_q(\y) \); in particular \( f_{pq}(\v_i \otimes \w_j) = \delta_{pi}\delta_{qj} \).

Now suppose \( \sum_{i,j} c_{ij}\,(\v_i \otimes \w_j) = \0 \). Apply \( f_{pq} \). By linearity the left side becomes \( \sum_{i,j} c_{ij}\delta_{pi}\delta_{qj} = c_{pq} \), and the right side is \( 0 \). Hence \( c_{pq} = 0 \). Since \( p \) and \( q \) were arbitrary, all coefficients vanish.

So the \( nm \) listed tensors form a basis, and \( \dim(V \otimes W) = nm \). This proves the theorem.
:::

**Aftermath: the count agrees.** In @thm-multilinear-maps-dimension we found \( \dim \cM(V, W; Z) = (\dim Z)(\dim V)(\dim W) \), and we argued that a universal object \( X \) would have to satisfy \( \dim \cL(X, Z) = \dim \cM(V, W; Z) \), forcing \( \dim X = (\dim V)(\dim W) \). @thm-tensor-basis delivers exactly that number, and the agreement is not a coincidence — it is the universal property, counted. Here is the statement behind it.

::: {#cor-bilinear-maps-linearized}
[Bilinear Maps Are Linear Maps on the Tensor Product]

Let \( V, W, Z \) be vector spaces over \( F \). The map
\[
\Xi \colon \cL(V \otimes W, Z) \to \cM(V, W; Z), \qquad L \mapsto L \circ \tau,
\]
is an isomorphism of vector spaces. When \( V \), \( W \) and \( Z \) are finite-dimensional, both sides have dimension \( (\dim Z)(\dim V)(\dim W) \).
:::

::: {.proof}
\( \Xi \) lands where claimed: \( L \circ \tau \) is bilinear, since freezing one slot of \( \tau \) gives a linear map and composing with the linear \( L \) keeps it linear (@thm-composition-linear (a)). It is linear in \( L \) by @thm-composition-linear (d), which gives \( (L_1 + L_2) \circ \tau = L_1\tau + L_2\tau \) and \( (cL)\circ\tau = c(L\tau) \). It is surjective by the existence half of (T1) and injective by the uniqueness half: if \( L\tau = 0 \), then both \( L \) and the zero map are linear maps composing with \( \tau \) to give the zero bilinear map, so \( L = 0 \), and @thm-injective-iff-trivial-kernel applies. The dimension count is @thm-multilinear-maps-dimension on one side and @thm-linear-maps-isomorphic-to-matrices together with @thm-tensor-basis on the other.
:::

::: {.check}
What is \( V \otimes W \) when \( W = F \), viewed as a one-dimensional space over itself? What is it when \( W = \{\0\} \)?
:::

::: {.solution}
For \( W = F \): \( \dim(V \otimes F) = (\dim V) \cdot 1 = \dim V \) by @thm-tensor-basis, and indeed \( \v \mapsto \v \otimes 1 \) is an isomorphism \( V \to V \otimes F \), since it carries a basis \( (\v_i) \) to the basis \( (\v_i \otimes 1) \). For \( W = \{\0\} \): the dimension is \( 0 \), so \( V \otimes \{\0\} = \{\0\} \). Both are the degenerate cases one should be able to predict from the product formula, and both come out right.
:::

## Coordinates: the tensor product of coordinate spaces

An abstract object is easier to trust once it has a concrete model. For coordinate spaces there is a very good one: \( F^m \otimes F^n \) is the space of \( m \times n \) matrices, with the simple tensor \( \x \otimes \y \) corresponding to the outer product \( \x\y\tp \).

::: {#thm-tensor-fn-matrices}
[\( F^m \otimes F^n \cong M_{m \times n}(F) \)]

Let \( m, n \ge 1 \). There is a unique linear map
\[
\Theta \colon F^m \otimes F^n \to M_{m \times n}(F), \qquad \Theta(\x \otimes \y) = \x\y\tp,
\]
and it is an isomorphism, carrying \( \e_i \otimes \f_j \) to the matrix unit \( \E_{ij} \). Under \( \Theta \), the simple tensors correspond exactly to the matrices of rank at most \( 1 \).
:::

::: {.proof}
The map \( (\x, \y) \mapsto \x\y\tp \) is bilinear: its \( (i, j) \) entry is \( x_iy_j \), and with \( \y \) frozen, \( (\x + \x')\y\tp = \x\y\tp + \x'\y\tp \) and \( (c\x)\y\tp = c(\x\y\tp) \) by @thm-matrix-multiplication-properties (2) and (4); freezing \( \x \) is the same computation (@exr-multilinear-maps-b1 (c)). By (T1) there is a unique linear \( \Theta \) with \( \Theta(\x \otimes \y) = \x\y\tp \). On standard basis vectors, \( \e_i\f_j\tp \) has a single \( 1 \) in position \( (i, j) \), so \( \Theta(\e_i \otimes \f_j) = \E_{ij} \).

By @thm-tensor-basis the \( mn \) tensors \( \e_i \otimes \f_j \) form a basis of \( F^m \otimes F^n \), and the \( mn \) matrix units form a basis of \( M_{m \times n}(F) \) (@exm-standard-bases (c)). By @thm-linear-transform-basis there is a linear \( \Psi \colon M_{m \times n}(F) \to F^m \otimes F^n \) with \( \Psi(\E_{ij}) = \e_i \otimes \f_j \). Then \( \Psi\Theta \) and \( \Theta\Psi \) are linear maps fixing a basis, hence are the identities by the uniqueness half of @thm-linear-transform-basis. So \( \Theta \) is an isomorphism.

For the last claim, a non-zero \( \x\y\tp \) is a product of an \( m \times 1 \) and a \( 1 \times n \) matrix, so it has rank \( 1 \) by @prp-rank-minimal-factorization; and \( \x\y\tp = \0 \) when \( \x = \0 \) or \( \y = \0 \), of rank \( 0 \). Conversely, a matrix \( \A \) of rank \( 1 \) factors as \( \A = \x\y\tp \) with \( \x \in F^m \) and \( \y\tp \in M_{1 \times n}(F) \), again by @prp-rank-minimal-factorization, and the zero matrix is \( \0 \otimes \0 \). This proves the theorem.
:::

::: {#exm-tensor-coordinates}
[Computing in \( F^2 \otimes F^3 \)]

Work in \( F^2 \otimes F^3 \) with standard bases \( (\e_1, \e_2) \) and \( (\f_1, \f_2, \f_3) \).

::: {.enumerate options="label=(\alph*)"}
1. Expand \( (\e_1 + 2\e_2) \otimes (3\f_1 - \f_2) \) in the basis of @thm-tensor-basis, and write the corresponding matrix.
2. Decide whether \( t = \e_1 \otimes \f_1 + 2\,\e_1 \otimes \f_2 + 3\,\e_2 \otimes \f_1 + 6\,\e_2 \otimes \f_2 \) is a simple tensor, and if so write it as one.
3. Decide whether \( u = \e_1 \otimes \f_1 + \e_2 \otimes \f_2 \) is a simple tensor.
:::
:::

::: {.solution}
(a) Expanding one slot at a time,
\[
(\e_1 + 2\e_2) \otimes (3\f_1 - \f_2) = 3\,\e_1 \otimes \f_1 - \e_1 \otimes \f_2 + 6\,\e_2 \otimes \f_1 - 2\,\e_2 \otimes \f_2 .
\]
The coefficient of \( \e_i \otimes \f_j \) is the \( (i, j) \) entry of the matrix, so \( \Theta \) sends it to
\[
\begin{pmatrix} 3 & -1 & 0 \\ 6 & -2 & 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 2\end{pmatrix}\begin{pmatrix} 3 & -1 & 0 \end{pmatrix},
\]
which is the outer product predicted by @thm-tensor-fn-matrices.

(b) The coefficients give \( \Theta(t) = \begin{psmallmatrix} 1 & 2 & 0 \\ 3 & 6 & 0 \end{psmallmatrix} \). Its second row is \( 3 \) times its first, so every \( 2 \times 2 \) minor vanishes and the rank is \( 1 \) (@thm-rank-via-minors). By @thm-tensor-fn-matrices, \( t \) is simple. Factoring, \( \Theta(t) = (1, 3)\tp(1, 2, 0) \), so
\[
t = (\e_1 + 3\e_2) \otimes (\f_1 + 2\f_2),
\]
which expands back to \( t \).

(c) Here \( \Theta(u) = \begin{psmallmatrix} 1 & 0 & 0 \\ 0 & 1 & 0\end{psmallmatrix} \), whose first two columns are independent, so its rank is \( 2 \). By @thm-tensor-fn-matrices, \( u \) is **not** simple. No amount of rewriting will turn it into a single \( \v \otimes \w \).
:::

## Three things a tensor is not

Part (c) above is not a curiosity; it is the central negative fact about tensor products, and the first of three misreadings worth naming before they happen.

### Not every tensor is simple

::: {#exm-non-simple-tensor}
[A tensor that is not simple]

In \( F^2 \otimes F^2 \), the element \( u = \e_1 \otimes \e_1 + \e_2 \otimes \e_2 \) is not a simple tensor, for any field \( F \).
:::

::: {.idea}
Two routes, and both are worth having. The quick one: \( \Theta(u) = \I_2 \), of rank \( 2 \), while simple tensors have rank at most \( 1 \). The portable one: suppose \( u = \v \otimes \w \), hit it with the four coordinate functionals \( f_{pq} \) built in the proof of @thm-tensor-basis, and read off four scalar equations that cannot all hold.
:::

::: {.proof}
Suppose \( u = \v \otimes \w \) for some \( \v, \w \in F^2 \). Let \( (\varphi_1, \varphi_2) \) be the basis of \( (F^2)^{*} \) dual to \( (\e_1, \e_2) \), and for \( p, q \in \{1, 2\} \) let \( f_{pq} \colon F^2 \otimes F^2 \to F \) be the linear map with \( f_{pq}(\x \otimes \y) = \varphi_p(\x)\varphi_q(\y) \), supplied by (T1) as in the proof of @thm-tensor-basis. Applying \( f_{pq} \) to both sides of \( u = \v \otimes \w \) gives
\[
v_pw_q = f_{pq}(u) = \delta_{p1}\delta_{q1} + \delta_{p2}\delta_{q2},
\]
that is, \( v_1w_1 = 1 \), \( v_2w_2 = 1 \), \( v_1w_2 = 0 \) and \( v_2w_1 = 0 \). From \( v_1w_1 = 1 \) we get \( v_1 \ne 0 \), so \( v_1w_2 = 0 \) forces \( w_2 = 0 \) — and then \( v_2w_2 = 0 \ne 1 \). This contradiction shows that no such \( \v, \w \) exist, so \( u \) is not simple.
:::

::: {.warning}
**A general element of \( V \otimes W \) is a *sum* of simple tensors, not a simple tensor.** @prp-simple-tensors-span says the simple tensors span; @exm-non-simple-tensor says they do not exhaust. A statement proved only for simple tensors is therefore proved for nothing until you extend it by linearity — which is legitimate precisely when the statement is about a linear map, and illegitimate when it is about, say, ranks or products. Whenever you want to define something on \( V \otimes W \), do not write "define it on \( \v \otimes \w \) and extend": use (T1), which is that move done correctly.
:::

The smallest number of simple tensors needed to write a given tensor is a genuine invariant, and for coordinate spaces @thm-tensor-fn-matrices identifies it: it is the rank of the corresponding matrix. So "not simple" means "rank at least \( 2 \)". A later section meets the same failure for elements of \( \Lambda^2 V \) that are not wedges of two vectors, and the closing section meets it again under the name *entanglement*.

### A simple tensor vanishes only for an obvious reason

::: {#prp-simple-tensor-zero}
[When a Simple Tensor Is Zero]

Let \( V \) and \( W \) be finite-dimensional, \( \v \in V \) and \( \w \in W \). Then \( \v \otimes \w = \0 \) if and only if \( \v = \0 \) or \( \w = \0 \).
:::

::: {.proof}
\( (\Leftarrow) \) If \( \v = \0 \), then \( \v \otimes \w = (0 \cdot \0) \otimes \w = 0(\0 \otimes \w) = \0 \), using that a scalar passes across \( \otimes \). The case \( \w = \0 \) is the same with the slots swapped.

\( (\Rightarrow) \) Suppose \( \v \ne \0 \) and \( \w \ne \0 \). By @thm-functionals-separate-points (a) there are \( \varphi \in V^{*} \) and \( \psi \in W^{*} \) with \( \varphi(\v) = 1 \) and \( \psi(\w) = 1 \). The map \( (\x, \y) \mapsto \varphi(\x)\psi(\y) \) is bilinear, so (T1) gives a linear \( f \colon V \otimes W \to F \) with \( f(\x \otimes \y) = \varphi(\x)\psi(\y) \). Then \( f(\v \otimes \w) = 1 \ne 0 \), while \( f(\0) = 0 \). Hence \( \v \otimes \w \ne \0 \). This proves the proposition.
:::

::: {.warning}
**A product of non-zero things can be zero in many algebraic settings, but not here.** It is tempting to expect \( V \otimes W \) to behave like a ring with zero divisors, so that some \( \v \otimes \w \) vanishes accidentally. It does not: @prp-simple-tensor-zero says the only way to get \( \0 \) is to feed in \( \0 \). The zero divisors appear one level later — in the algebras of the following sections, where products of non-zero *sums* of simple tensors can vanish.
:::

### A simple tensor does not remember its factors

::: {#prp-simple-tensor-equality}
[When Two Simple Tensors Agree]

Let \( V \) and \( W \) be finite-dimensional, and let \( \v, \v' \in V \) and \( \w, \w' \in W \) with \( \v \otimes \w \ne \0 \). Then
\[
\v \otimes \w = \v' \otimes \w'
\]
if and only if there is a scalar \( c \ne 0 \) with \( \v' = c\v \) and \( \w' = c^{-1}\w \).
:::

::: {.idea}
The "if" half is the scalar rule. For "only if", the danger is that \( \v' \) points somewhere new. Suppose it does; then \( (\v, \v') \) is independent, so there is a functional killing \( \v \) and not \( \v' \), and the corresponding \( f \) on \( V \otimes W \) separates the two sides.
:::

::: {.proof}
\( (\Leftarrow) \) If \( \v' = c\v \) and \( \w' = c^{-1}\w \), then \( \v' \otimes \w' = (c\v) \otimes (c^{-1}\w) = c c^{-1}(\v \otimes \w) = \v \otimes \w \), moving each scalar across \( \otimes \).

\( (\Rightarrow) \) Suppose \( \v \otimes \w = \v' \otimes \w' \ne \0 \). By @prp-simple-tensor-zero all four vectors are non-zero. Suppose, for a contradiction, that \( \v' \notin \Span(\v) \). Then \( (\v, \v') \) is linearly independent, so it extends to a basis of \( V \) (@thm-basis-extension), and the dual basis (@thm-dual-basis) provides \( \varphi \in V^{*} \) with \( \varphi(\v) = 0 \) and \( \varphi(\v') = 1 \). Since \( \w' \ne \0 \), @thm-functionals-separate-points (a) provides \( \psi \in W^{*} \) with \( \psi(\w') = 1 \). By (T1) there is a linear \( f \colon V \otimes W \to F \) with \( f(\x \otimes \y) = \varphi(\x)\psi(\y) \). Evaluating both sides of \( \v \otimes \w = \v' \otimes \w' \),
\[
0 = \varphi(\v)\psi(\w) = f(\v \otimes \w) = f(\v' \otimes \w') = \varphi(\v')\psi(\w') = 1,
\]
which is absurd. Hence \( \v' = c\v \) for some \( c \in F \), and \( c \ne 0 \) because \( \v' \ne \0 \).

Then \( \v \otimes \w = (c\v) \otimes \w' = \v \otimes (c\w') \), so \( \v \otimes (\w - c\w') = \0 \) by bilinearity. Since \( \v \ne \0 \), @prp-simple-tensor-zero forces \( \w - c\w' = \0 \), that is, \( \w' = c^{-1}\w \). This proves the proposition.
:::

::: {.warning}
**\( \v \otimes \w = \v' \otimes \w' \) does not mean \( \v = \v' \) and \( \w = \w' \).** Already \( 2\v \otimes \w = \v \otimes 2\w \), with different factors on the two sides. So "the first factor of a simple tensor" is **not** a well-defined function: writing \( t = \v \otimes \w \) and then speaking of "the \( \v \) of \( t \)" is an error. What @prp-simple-tensor-equality salvages is that the *lines* \( \Span(\v) \) and \( \Span(\w) \) are determined, which is exactly the information carried by a rank-one matrix: its column space and its row space.
:::

::: {.check}
In \( \nR^2 \otimes \nR^2 \), is \( \e_1 \otimes \e_2 + \e_2 \otimes \e_1 \) a simple tensor?
:::

::: {.solution}
No. Its matrix under \( \Theta \) is \( \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix} \), of determinant \( -1 \ne 0 \), hence of rank \( 2 \) (@thm-det-nonzero-iff-invertible). By @thm-tensor-fn-matrices a simple tensor would have rank at most \( 1 \). Note how little the symmetry of the expression helps: being a sum of two simple tensors is the generic situation, not a special one.
:::

## Exercises

### A. Check your understanding

::: {#exr-tensor-product-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the universal property (T1) of the tensor product, with every quantifier.
2. What does @thm-tensor-unique assert, and which clause of (T1) makes the composites identities?
3. Give \( \dim(V \otimes W) \) in terms of \( \dim V \) and \( \dim W \), and a basis.
4. True or false: every element of \( V \otimes W \) is of the form \( \v \otimes \w \). Justify your answer.
5. True or false: if \( \v \otimes \w = \0 \) then \( \v = \0 \). Justify your answer.
6. Explain in one sentence why the tensor product is **not** defined by a formula for its elements.
:::
:::

::: {.solution}
(a) A pair \( (X, \tau) \) with \( \tau \colon V \times W \to X \) bilinear such that for **every** vector space \( Z \) and **every** bilinear \( \beta \colon V \times W \to Z \) there is a **unique** linear \( \bar\beta \colon X \to Z \) with \( \bar\beta \circ \tau = \beta \) (@def-tensor-product).

(b) That any two tensor products of \( V \) and \( W \) are isomorphic by a unique isomorphism commuting with the two structure maps. The **uniqueness** clause: it says there is only one linear self-map \( X \to X \) composing with \( \tau \) to give \( \tau \), and since both \( \psi\varphi \) and \( \id_X \) are such maps, they are equal.

(c) \( (\dim V)(\dim W) \), with basis \( (\v_i \otimes \w_j) \) for bases \( (\v_i) \) of \( V \) and \( (\w_j) \) of \( W \) (@thm-tensor-basis).

(d) False. In \( F^2 \otimes F^2 \), \( \e_1 \otimes \e_1 + \e_2 \otimes \e_2 \) is not simple (@exm-non-simple-tensor).

(e) False as stated: it says \( \v = \0 \) **or** \( \w = \0 \) (@prp-simple-tensor-zero). For instance \( \v \otimes \0 = \0 \) for every \( \v \).

(f) Because a formula would require choosing a construction, and the object is characterized by what maps out of it do, not by what its elements look like; different constructions give different-looking elements and the same space up to a unique isomorphism.
:::

### B. Practice

::: {#exr-tensor-product-b1}
[B1: Simple or not]

For each element of \( F^3 \otimes F^3 \) below, determine whether it is a simple tensor. If it is, write it as \( \v \otimes \w \); if it is not, justify your answer. Use the standard basis \( (\e_1, \e_2, \e_3) \) in both factors.

::: {.enumerate options="label=(\alph*)"}
1. \( t_1 = \e_1 \otimes \e_2 - 2\,\e_1 \otimes \e_3 + 3\,\e_3 \otimes \e_2 - 6\,\e_3 \otimes \e_3 \).
2. \( t_2 = \e_1 \otimes \e_1 + \e_2 \otimes \e_2 + \e_3 \otimes \e_3 \).
3. \( t_3 = \e_1 \otimes \e_2 + \e_2 \otimes \e_1 \).
4. \( t_4 = \0 \).
:::
:::

::: {.solution}
Throughout we use @thm-tensor-fn-matrices: \( t \) is simple exactly when the matrix \( \Theta(t) \), whose \( (i, j) \) entry is the coefficient of \( \e_i \otimes \e_j \), has rank at most \( 1 \).

(a) \( \Theta(t_1) = \begin{psmallmatrix} 0 & 1 & -2 \\ 0 & 0 & 0 \\ 0 & 3 & -6\end{psmallmatrix} \). Row \( 3 \) is \( 3 \) times row \( 1 \) and row \( 2 \) is zero, so the rank is \( 1 \). Factoring, \( \Theta(t_1) = (1, 0, 3)\tp(0, 1, -2) \), so
\[
t_1 = (\e_1 + 3\e_3) \otimes (\e_2 - 2\e_3),
\]
which expands to the four given terms.

(b) \( \Theta(t_2) = \I_3 \), of rank \( 3 \). Not simple. This is @exm-non-simple-tensor one size larger.

(c) \( \Theta(t_3) \) has \( 1 \) in positions \( (1,2) \) and \( (2,1) \) and zeros elsewhere. Its top-left \( 2 \times 2 \) minor is \( 0 \cdot 0 - 1 \cdot 1 = -1 \ne 0 \), so its rank is \( 2 \) (@thm-rank-via-minors). Not simple.

(d) \( \Theta(t_4) = \0 \), of rank \( 0 \le 1 \). So \( t_4 \) is simple, and indeed \( \0 = \0 \otimes \0 \). The degenerate case is simple for a boring reason, and it is worth keeping in the statement of @thm-tensor-fn-matrices.
:::

::: {#exr-tensor-product-b2}
[B2: Inducing maps from bilinear maps]

In each case, a bilinear map is given. Use (T1) to produce the induced linear map on the tensor product, and compute the requested value.

::: {.enumerate options="label=(\alph*)"}
1. \( \beta \colon F^2 \times F^2 \to F \), \( \beta(\x, \y) = x_1y_1 + x_2y_2 \). Compute \( \bar\beta(\e_1 \otimes \e_1 + \e_2 \otimes \e_2) \).
2. \( \beta \colon F^n \times F^n \to M_n(F) \), \( \beta(\x, \y) = \x\y\tp - \y\x\tp \). Compute \( \bar\beta(\v \otimes \v) \) for any \( \v \).
3. \( \beta \colon V^{*} \times V \to F \), \( \beta(\varphi, \v) = \varphi(\v) \), for \( V \) finite-dimensional. Compute \( \bar\beta(\varphi_1 \otimes \v_1 + \varphi_2 \otimes \v_2) \) for a basis \( (\v_i) \) with dual basis \( (\varphi_i) \), assuming \( \dim V \ge 2 \).
:::
:::

::: {.solution}
(a) \( \beta \) is the dot product, bilinear by @exm-bilinear-forms-first (a). By (T1) there is a unique linear \( \bar\beta \) with \( \bar\beta(\x \otimes \y) = x_1y_1 + x_2y_2 \). By linearity,
\[
\bar\beta(\e_1 \otimes \e_1 + \e_2 \otimes \e_2) = \bar\beta(\e_1 \otimes \e_1) + \bar\beta(\e_2 \otimes \e_2) = 1 + 1 = 2 .
\]

(b) Each entry of \( \x\y\tp - \y\x\tp \) is \( x_iy_j - y_ix_j \), linear in each slot, so \( \beta \) is bilinear and (T1) applies. Then \( \bar\beta(\v \otimes \v) = \v\v\tp - \v\v\tp = \0 \) for every \( \v \), so the induced map kills every "diagonal" simple tensor without being zero: \( \bar\beta(\e_1 \otimes \e_2) = \E_{12} - \E_{21} \ne \0 \) for \( n \ge 2 \).

(c) The evaluation pairing is bilinear by @exm-multilinear-maps-first (f), so \( \bar\beta \colon V^{*} \otimes V \to F \) exists with \( \bar\beta(\varphi \otimes \v) = \varphi(\v) \). Hence
\[
\bar\beta(\varphi_1 \otimes \v_1 + \varphi_2 \otimes \v_2) = \varphi_1(\v_1) + \varphi_2(\v_2) = 1 + 1 = 2 .
\]
This map is the contraction, and the answer \( 2 \) is a first glimpse of a later section: it is the trace of a rank-two projection.
:::

::: {#exr-tensor-product-b3}
[B3: Dimensions and bases]

Let \( V \), \( W \) and \( U \) be finite-dimensional over \( F \), with \( \dim V = 3 \), \( \dim W = 4 \) and \( \dim U = 2 \).

::: {.enumerate options="label=(\alph*)"}
1. Find \( \dim(V \otimes W) \) and \( \dim\bigl((V \otimes W) \otimes U\bigr) \).
2. Find \( \dim \cL(V \otimes W, U) \) and \( \dim \cM(V, W; U) \), and explain why they agree.
3. Let \( V = F^3 \) with basis \( (\e_1, \e_2, \e_3) \) and \( W = F^4 \) with basis \( (\f_1, \dots, \f_4) \). Write down a basis of \( V \otimes W \) and say which basis vector corresponds to the matrix unit \( \E_{23} \) under \( \Theta \).
:::
:::

::: {.solution}
(a) \( \dim(V \otimes W) = 3 \cdot 4 = 12 \) by @thm-tensor-basis, and then \( \dim((V \otimes W) \otimes U) = 12 \cdot 2 = 24 \), applying the theorem again to the pair \( (V \otimes W, U) \).

(b) \( \dim \cL(V \otimes W, U) = (\dim U)\dim(V \otimes W) = 2 \cdot 12 = 24 \) by @thm-linear-maps-isomorphic-to-matrices, and \( \dim \cM(V, W; U) = 2 \cdot 3 \cdot 4 = 24 \) by @eq-multilinear-dimension. They agree because @cor-bilinear-maps-linearized exhibits an isomorphism between the two spaces; the equality of numbers is that isomorphism, counted.

(c) The \( 12 \) tensors \( \e_i \otimes \f_j \) with \( 1 \le i \le 3 \) and \( 1 \le j \le 4 \). Since \( \Theta(\e_i \otimes \f_j) = \E_{ij} \), the basis vector corresponding to \( \E_{23} \) is \( \e_2 \otimes \f_3 \).
:::

### C. Going deeper

::: {#exr-tensor-product-c1}
[C1: The tensor product is commutative, up to a unique isomorphism]

Let \( V \) and \( W \) be vector spaces over \( F \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that there is a unique linear map \( \sigma \colon V \otimes W \to W \otimes V \) with \( \sigma(\v \otimes \w) = \w \otimes \v \) for all \( \v, \w \), and that it is an isomorphism.
2. Deduce that \( \sigma^{2} = \id \) when \( V = W \), where \( \sigma^2 \) means \( \sigma \) applied twice to \( V \otimes V \).
3. Explain why the argument in (a) never mentions a basis, and why that matters.
:::

*Hint for (a): the map \( (\v, \w) \mapsto \w \otimes \v \) is bilinear; then build the inverse the same way and use the uniqueness clause of (T1).*
:::

::: {.solution}
(a) The map \( V \times W \to W \otimes V \), \( (\v, \w) \mapsto \w \otimes \v \), is bilinear, because \( \otimes \) is bilinear and swapping the slots exchanges the two clauses of @def-multilinear-map. By (T1) for \( V \otimes W \) there is a unique linear \( \sigma \) with \( \sigma(\v \otimes \w) = \w \otimes \v \). Symmetrically, (T1) for \( W \otimes V \) gives a unique linear \( \sigma' \colon W \otimes V \to V \otimes W \) with \( \sigma'(\w \otimes \v) = \v \otimes \w \). Then \( \sigma'\sigma \) is a linear self-map of \( V \otimes W \) with \( (\sigma'\sigma)(\v \otimes \w) = \v \otimes \w \), and so is the identity; by the uniqueness clause of (T1) applied with \( Z = V \otimes W \) and \( \beta = \tau \), the two agree, so \( \sigma'\sigma = \id \). Symmetrically \( \sigma\sigma' = \id \). Hence \( \sigma \) is an isomorphism (@thm-inverse-is-linear).

(b) With \( V = W \), part (a) gives \( \sigma' = \sigma \), since both are the unique linear map sending \( \v \otimes \w \) to \( \w \otimes \v \). Hence \( \sigma^2 = \sigma'\sigma = \id \).

(c) Every step used only (T1) and the bilinearity of \( \otimes \). So the argument works for infinite-dimensional spaces, where @thm-tensor-basis is unavailable, and it produces a **canonical** isomorphism, whereas a basis-dependent construction would give one isomorphism per basis and no reason to prefer any of them.
:::

::: {#exr-tensor-product-c2}
[C2: Recovering the factors from a simple tensor]

Let \( V \) and \( W \) be finite-dimensional and let \( t = \v \otimes \w \ne \0 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that the subspace \( \Span(\v) \subseteq V \) depends only on \( t \), not on the chosen factorization.
2. Prove the corresponding statement for \( \Span(\w) \subseteq W \).
3. For \( V = F^m \) and \( W = F^n \), identify these two subspaces in terms of the matrix \( \Theta(t) \) of @thm-tensor-fn-matrices, and say why (a) and (b) are then statements you already knew.
:::
:::

::: {.solution}
(a) Suppose \( t = \v \otimes \w = \v' \otimes \w' \) with \( t \ne \0 \). By @prp-simple-tensor-equality there is \( c \ne 0 \) with \( \v' = c\v \). A non-zero scalar multiple spans the same subspace, so \( \Span(\v') = \Span(\v) \). Hence the line is determined by \( t \) alone.

(b) The same proposition gives \( \w' = c^{-1}\w \) with \( c^{-1} \ne 0 \), so \( \Span(\w') = \Span(\w) \).

(c) Under \( \Theta \), \( t \) corresponds to \( \A = \v\w\tp \), a matrix of rank \( 1 \) (@thm-tensor-fn-matrices). Every column of \( \A \) is a scalar multiple of \( \v \), and \( \A \) is non-zero, so \( \col(\A) = \Span(\v) \); every row is a multiple of \( \w\tp \), so \( \row(\A) = \Span(\w\tp) \). Thus (a) and (b) say that a matrix has a well-defined column space and row space, which Chapter 2 established long ago. The tensor language adds nothing here except the reason the statement looks surprising: it is surprising only if one expects \( \v \) itself, rather than its line, to be recoverable.
:::
