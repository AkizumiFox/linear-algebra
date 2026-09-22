# Index Notation and the Transformation Law

Outside mathematics, a tensor is usually not a vector in \( T^{p}_{q}(V) \) at all: it is an array of numbers with some indices written upstairs and some downstairs, together with a rule saying how the array changes when the coordinates change. That older definition is still the working one in physics and in differential geometry, and a reader who meets it after this chapter deserves a dictionary. This section supplies one. We write the components of a tensor, derive — not assert — how they transform under a change of basis, and then prove that the classical definition and ours describe the same objects in finite dimensions. The section ends with the warning the classical definition exists to make: an array of numbers is not automatically a tensor.

## Components, upstairs and downstairs

Fix a finite-dimensional \( V \) over \( F \) with \( n = \dim V \ge 1 \), an ordered basis \( \sB = (\v_1, \dots, \v_n) \), and its dual basis \( \sB^{*} = (\varphi^1, \dots, \varphi^n) \), characterized by \( \varphi^i(\v_j) = \delta^i_j \) (@def-dual-basis). By @thm-tensor-basis, the \( n^{p+q} \) tensors
\[
\v_{i_1} \otimes \dots \otimes \v_{i_p} \otimes \varphi^{j_1} \otimes \dots \otimes \varphi^{j_q}
\]
form a basis of \( T^{p}_{q}(V) \), so every tensor has unique coordinates in it.

::: {#def-tensor-components}
[Components of a tensor]

Let \( t \in T^{p}_{q}(V) \). The **components of \( t \) in the basis \( \sB \)** are the unique scalars \( T^{i_1 \dots i_p}_{j_1 \dots j_q} \in F \), for \( 1 \le i_1, \dots, i_p, j_1, \dots, j_q \le n \), with
\[
t = \sum T^{i_1 \dots i_p}_{j_1 \dots j_q}\;
\v_{i_1} \otimes \dots \otimes \v_{i_p} \otimes \varphi^{j_1} \otimes \dots \otimes \varphi^{j_q},
\]
the sum running over all \( p + q \) indices from \( 1 \) to \( n \). An index written **upstairs** belongs to a \( V \)-slot and is called **contravariant**; an index written **downstairs** belongs to a \( V^{*} \)-slot and is called **covariant**.
:::

In words: the position of an index records which kind of slot it labels, so that the shape of a symbol already tells you the type of the tensor. Nothing here is new mathematics; it is the coordinate vector of @thm-tensor-basis, with the indices arranged to be readable.

Two pieces of shorthand come with it. The first is the placement rule: a vector has its coordinates upstairs, \( \v = \sum_i v^i \v_i \), while a functional has them downstairs, \( \xi = \sum_j \xi_j \varphi^j \) — which is @thm-dual-basis (c) written in the new notation. The second is the **summation convention**: an index appearing once upstairs and once downstairs in a product is summed over, and the \( \sum \) is not written. With it, the displayed formula above reads
\[
t = T^{i_1 \dots i_p}_{j_1 \dots j_q}\;
\v_{i_1} \otimes \dots \otimes \varphi^{j_q},
\]
and the evaluation of a functional on a vector is \( \xi(\v) = \xi_i v^i \). The rest of this book writes its sums out; this section is the one place where the convention is used, and it is used because the transformation law is unreadable without it.

**Examples.**

1. **Type \( (1,1) \): an operator.** If \( t \in T^1_1(V) \) corresponds to \( S \in \cL(V) \) under @thm-tensor-hom-iso, then \( T^i_j \) is the \( (i, j) \) entry of \( \mtx{S}{\sB}{\sB} \): the tensor \( \v_i \otimes \varphi^j \) is the operator \( \u \mapsto \varphi^j(\u)\v_i \), whose matrix is \( \E_{ij} \). Upper index = row, lower index = column.
2. **Type \( (0,2) \): a bilinear form.** If \( t \in T^0_2(V) \) corresponds to the bilinear form \( \beta \) (@prp-dual-of-tensor and @exr-contraction-and-trace-b3), then \( T_{ij} = \beta(\v_i, \v_j) \), which is the Gram matrix \( \mtx{\beta}{\sB}{\sB} \) of @def-form-matrix. Both indices downstairs.
3. **Contraction.** In components, @def-contraction-slots is "set an upper index equal to a lower one and sum". For \( t \in T^1_1(V) \),
\[
C^1_1(t) = T^i_i \quad \Big(= \sum_{i=1}^{n} T^i_i\Big),
\]
which is the trace, by @thm-trace-is-contraction. This is the whole reason the convention pairs an upper with a lower index: a repeated index is a contraction, and contraction is the only basis-free way to remove slots.

::: {.remark}
The names are historically backwards, and it is worth saying so once. A *contravariant* index sits upstairs, on a \( V \)-slot, and its components transform by the **inverse** of the matrix that transforms the basis vectors; a *covariant* index sits downstairs and transforms by the same matrix as the basis vectors. The names describe the components, not the slots. @thm-tensor-transformation-law below is what they refer to.
:::

## How the components change

Let \( \sB = (\v_1, \dots, \v_n) \) and \( \sB' = (\v'_1, \dots, \v'_n) \) be two ordered bases, and let
\[
\P = \mtx{\id}{\sB'}{\sB} = (p^i_j)
\]
be the change-of-coordinates matrix from \( \sB' \) to \( \sB \) (@def-change-of-coordinates-matrix), whose \( j \)-th column is \( \coord{\v'_j}{\sB} \). That is,
\[
\v'_j = \sum_{i=1}^{n} p^i_j\,\v_i ,
\]
with the row index upstairs and the column index downstairs. Write \( \Q = \P^{-1} = (q^i_j) \), which exists because a change-of-coordinates matrix is invertible (@prp-invertible-matrix-change-of-basis).

The dual bases move by the inverse matrix. This is the one computation the whole section rests on, so we do it first.

::: {#lem-dual-basis-transforms}
[Dual Bases Move by the Inverse Matrix]

With the notation above, \( \displaystyle (\varphi')^{k} = \sum_{l=1}^{n} q^{k}_{l}\,\varphi^{l} \) for each \( k \), where \( (\varphi')^{1}, \dots, (\varphi')^{n} \) is the dual basis of \( \sB' \) supplied by @thm-dual-basis.
:::

::: {.proof}
Both sides are linear maps on \( V \), so by the uniqueness clause of @thm-linear-transform-basis it is enough to check that they agree at each vector of the basis \( \sB' \). By @def-dual-basis the left side gives \( (\varphi')^{k}(\v'_j) = \delta^k_j \). The right side gives
\[
\sum_{l} q^k_l\,\varphi^l\Big(\sum_i p^i_j\v_i\Big)
= \sum_{l}\sum_{i} q^k_l\,p^i_j\,\delta^l_i
= \sum_{i} q^k_i p^i_j ,
\]
which is the \( (k, j) \) entry of \( \Q\P = \I_n \), that is \( \delta^k_j \). The two agree.
:::

So the dual basis vectors carry the entries of \( \P^{-1} \), while the basis vectors carry the entries of \( \P \). Substituting both into the expansion of a tensor gives the transformation law.

::: {#thm-tensor-transformation-law}
[Transformation Law for Components]

Let \( t \in T^{p}_{q}(V) \) have components \( T^{i_1 \dots i_p}_{j_1 \dots j_q} \) in \( \sB \) and \( (T')^{k_1 \dots k_p}_{l_1 \dots l_q} \) in \( \sB' \), and let \( \P = (p^i_j) \) and \( \Q = \P^{-1} = (q^i_j) \) be as above. Then, with the summation convention,
\[
\begin{aligned}
(T')^{k_1 \dots k_p}_{l_1 \dots l_q}
&= q^{k_1}_{i_1} \cdots q^{k_p}_{i_p} \\
&\qquad \times\;
p^{j_1}_{l_1} \cdots p^{j_q}_{l_q}\;
T^{i_1 \dots i_p}_{j_1 \dots j_q} .
\end{aligned}
\]
Each **upper** index is contracted with a factor of \( \P^{-1} \), each **lower** index with a factor of \( \P \).
:::

::: {.idea}
There is only one move: write \( t \) in the new basis, replace every new basis vector and every new dual basis vector by its expression in the old ones, multiply out using multilinearity of \( \otimes \), and compare with the expansion of \( t \) in the old basis. Coordinates in a basis are unique, so the comparison is an equality of coefficients. Doing it once for type \( (1,0) \) shows the whole pattern; the general case is the same computation with more indices.
:::

::: {.proof}
Start with the expansion of \( t \) in the new basis:
\[
t = (T')^{k_1 \dots k_p}_{l_1 \dots l_q}\;
\v'_{k_1} \otimes \dots \otimes \v'_{k_p} \otimes (\varphi')^{l_1} \otimes \dots \otimes (\varphi')^{l_q}.
\]
Substitute \( \v'_{k} = p^{i}_{k}\v_i \) and, by @lem-dual-basis-transforms, \( (\varphi')^{l} = q^{l}_{j}\varphi^{j} \). Since \( \otimes \) is linear in each of its slots, the scalars may be pulled out of all \( p + q \) factors at once, giving
\[
\begin{aligned}
t = (T')^{k_1 \dots k_p}_{l_1 \dots l_q}\;
&p^{i_1}_{k_1} \cdots p^{i_p}_{k_p}\;
q^{l_1}_{j_1} \cdots q^{l_q}_{j_q} \\
&\times\;
\v_{i_1} \otimes \dots \otimes \v_{i_p} \otimes \varphi^{j_1} \otimes \dots \otimes \varphi^{j_q}.
\end{aligned}
\]
The tensors on the right form a basis of \( T^p_q(V) \) (@thm-tensor-basis), so coordinates in them are unique (@thm-unique-representation). Comparing with @def-tensor-components,
\[
T^{i_1 \dots i_p}_{j_1 \dots j_q}
= p^{i_1}_{k_1} \cdots p^{i_p}_{k_p}\;
q^{l_1}_{j_1} \cdots q^{l_q}_{j_q}\;
(T')^{k_1 \dots k_p}_{l_1 \dots l_q}. \tag{$\ast$}
\]
It remains to invert \( (\ast) \). Contract both sides of \( (\ast) \) with \( q^{m_1}_{i_1} \cdots q^{m_p}_{i_p}\,p^{j_1}_{r_1} \cdots p^{j_q}_{r_q} \) and sum over \( i_1, \dots, i_p, j_1, \dots, j_q \). On the right, each pair \( q^{m}_{i}p^{i}_{k} \) sums to \( (\Q\P)^{m}_{k} = \delta^m_k \), and each pair \( q^{l}_{j}p^{j}_{r} \) sums to \( \delta^l_r \); every delta then collapses one summation. What survives on the right is \( (T')^{m_1 \dots m_p}_{r_1 \dots r_q} \), and what stands on the left is the asserted expression. Renaming \( m \) to \( k \) and \( r \) to \( l \) gives the theorem.
:::

The two smallest cases are results the book already has, and they are worth reading off as a check.

- **Type \( (1,1) \).** The law reads \( (T')^{k}_{l} = q^{k}_{i}\,p^{j}_{l}\,T^{i}_{j} \), that is \( \T' = \P^{-1}\T\P \). This is @thm-change-of-basis-maps: matrices of an operator in two bases are **similar**.
- **Type \( (0,2) \).** The law reads \( (T')_{kl} = p^{i}_{k}\,p^{j}_{l}\,T_{ij} \), that is \( \T' = \P\tp\T\P \). This is @thm-change-of-basis-form: Gram matrices of a bilinear form in two bases are **congruent**.

So similarity and congruence are not two unrelated relations that happen to look alike. They are the transformation laws of type \( (1,1) \) and type \( (0,2) \), and the difference between \( \P^{-1} \) and \( \P\tp \) is exactly the difference between an upper and a lower index.

## The classical definition

The classical definition turns the theorem into a definition: a tensor *is* a rule producing arrays that obey the law.

::: {#def-classical-tensor}
[Classical tensor]

Let \( V \) be a vector space over \( F \) with \( \dim V = n \ge 1 \), and let \( p, q \ge 0 \). A **classical tensor of type \( (p, q) \)** on \( V \) is a rule \( \sB \mapsto A_{\sB} \) assigning to **every** ordered basis \( \sB \) of \( V \) an array
\[
A_{\sB} = \big(A^{i_1 \dots i_p}_{j_1 \dots j_q}\big)
\]
of \( n^{p+q} \) scalars, such that for **any two** ordered bases \( \sB, \sB' \), with \( \P = \mtx{\id}{\sB'}{\sB} \) and \( \Q = \P^{-1} \),
\[
\begin{aligned}
(A_{\sB'})^{k_1 \dots k_p}_{l_1 \dots l_q}
&= q^{k_1}_{i_1} \cdots q^{k_p}_{i_p} \\
&\qquad \times\;
p^{j_1}_{l_1} \cdots p^{j_q}_{l_q}\;
(A_{\sB})^{i_1 \dots i_p}_{j_1 \dots j_q} .
\end{aligned}
\]
:::

::: {#thm-classical-equals-modern}
[The Two Definitions Agree]

Let \( V \) be finite-dimensional over \( F \) with \( \dim V = n \ge 1 \), and let \( p, q \ge 0 \). The map sending \( t \in T^{p}_{q}(V) \) to the rule
\[
\sB \longmapsto \big(\text{components of } t \text{ in } \sB\big)
\]
is a bijection from \( T^{p}_{q}(V) \) onto the set of classical tensors of type \( (p, q) \) on \( V \). It is linear for the entrywise operations on arrays.
:::

::: {.idea}
Well defined is @thm-tensor-transformation-law. Injective because a tensor is determined by its coordinates in one basis. Surjective is the only step with content, and it is short: fix one basis \( \sB_0 \), build the tensor whose components there are the given array, and then observe that its components in any other basis obey the same law as the rule's array does, starting from the same array — so the two agree.
:::

::: {.proof}
**Well defined.** If \( t \in T^p_q(V) \), its components in the various bases satisfy the required identity, by @thm-tensor-transformation-law. So the rule attached to \( t \) is a classical tensor.

**Injective.** Fix a basis \( \sB_0 \). If two tensors give the same rule, they have the same components in \( \sB_0 \), hence are equal, since coordinates in the basis of @thm-tensor-basis are unique (@thm-unique-representation).

**Surjective.** Let \( \sB \mapsto A_{\sB} \) be a classical tensor. Fix an ordered basis \( \sB_0 = (\v_1, \dots, \v_n) \) with dual basis \( (\varphi^1, \dots, \varphi^n) \), and define
\[
t \coloneqq (A_{\sB_0})^{i_1 \dots i_p}_{j_1 \dots j_q}\;
\v_{i_1} \otimes \dots \otimes \varphi^{j_q} \;\in\; T^p_q(V),
\]
so that the components of \( t \) in \( \sB_0 \) are exactly \( A_{\sB_0} \). Let \( \sB' \) be any other ordered basis and put \( \P = \mtx{\id}{\sB'}{\sB_0} \). By @thm-tensor-transformation-law the components of \( t \) in \( \sB' \) are obtained from \( A_{\sB_0} \) by the law with this \( \P \); by @def-classical-tensor, \( A_{\sB'} \) is obtained from \( A_{\sB_0} \) by the law with the same \( \P \). Both are the value of the same expression, so they are equal. Hence the rule attached to \( t \) is the given one.

**Linearity.** The components of \( t + ct' \) in each basis are \( A + cA' \), because coordinate maps are linear (@cor-coordinate-isomorphism).
:::

**Why the older definition survives.** It is tempting to file @def-classical-tensor as a historical curiosity, and that would be a mistake. Three honest reasons keep it in use.

- **Components are what gets measured and computed.** A stress tensor, a metric, an inertia tensor: the physicist has numbers in a chosen frame, and the question that matters is what those numbers become in another frame. The transformation law is not a consequence to be derived afterwards; it is the datum.
- **There is often no global basis to be abstract about.** On a curved space, the objects of interest are tensor *fields*, and a manifold generally admits no single coordinate system covering it. What it does admit is many local coordinate patches with prescribed rules for passing between them. In that setting "an array in each chart, transforming correctly on overlaps" is a definition that works, while "an element of \( T^p_q(V) \)" needs a \( V \) that varies from point to point, which is a later and heavier construction.
- **It is a usable test.** Given a recipe that produces an array from a basis, checking the transformation law is a finite computation, and it is the standard way to certify that a quantity is geometric rather than an artifact of the coordinates. The next warning is exactly such a test, failed.

## An array is not a tensor

::: {.warning}
**A matrix is not automatically a tensor.** Consider the rule that assigns to **every** ordered basis of \( V \) the same array, written as a matrix,
\[
\A_{\sB} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix},
\qquad \dim V = 2,
\]
read as a type \( (1,1) \) array. Take \( \sB = (\v_1, \v_2) \) and \( \sB' = (\v_1, \v_1 + \v_2) \), so that
\[
\P = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix},
\qquad
\P^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}.
\]
The law demands \( \A_{\sB'} = \P^{-1}\A_{\sB}\P \), which is \( \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix} \), not \( \A_{\sB} \). So this rule is **not** a classical tensor of type \( (1,1) \): it is a matrix, and nothing more. The operator it describes in \( \sB \) — projection onto \( \Span(\v_1) \) along \( \Span(\v_2) \) — is a perfectly good tensor, but then its array in \( \sB' \) is the second matrix, not the first. "Write down the same numbers in every basis" is a rule, and almost never a tensor.
:::

Two refinements of the same point are worth having.

**The same array can be two different tensors.** Take the array \( \I_2 \). As a type \( (1,1) \) rule it *is* a tensor: \( \P^{-1}\I_2\P = \I_2 \) for every \( \P \), and the tensor is the identity operator, which is the \( \iota \) of @exr-contraction-and-trace-c2. As a type \( (0,2) \) rule, the same constant array is **not** a tensor: the law demands \( \P\tp\I_2\P \), and for the \( \P \) above that is \( \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} \ne \I_2 \). Geometrically: "the identity operator" is basis-free, while "the bilinear form whose Gram matrix is the identity", that is, the choice of an inner product declaring the basis orthonormal, is not — it depends on the basis, and orthonormality, as Chapter 10 defines it, is relative to a chosen inner product.

::: {.warning}
**Which type an array has is not visible in the array.** The array \( \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \) transforms as \( \P^{-1}\A\P \) if it is the matrix of an operator and as \( \P\tp\A\P \) if it is the Gram matrix of a form, and for the \( \P \) above those give \( \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix} \) and \( \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \). Same numbers, same basis change, different answers. This is why index position is not decoration: writing \( A^i_j \) rather than \( A_{ij} \) is a statement about what the object is.
:::

::: {.check}
Let \( \dim V = 2 \). Is the rule assigning to every ordered basis the array \( A_{ij} = \delta_{ij} \) of type \( (0,2) \) ever a classical tensor — say, over \( \nF_2 \), or if we only allow bases obtained from one another by permutation? Decide, with a reason.
:::

::: {.solution}
Over \( \nF_2 \) it still fails: with \( \P = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \), the law demands \( \P\tp\I_2\P = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} \) (since \( 2 = 0 \) in \( \nF_2 \)), which is not \( \I_2 \). If the bases are restricted to permutations of one fixed basis, then \( \P \) is a permutation matrix, so \( \P\tp = \P^{-1} \) and \( \P\tp\I_2\P = \I_2 \): the rule survives. But @def-classical-tensor quantifies over **every** ordered basis, and a rule that works only for a restricted family is exactly the kind of coordinate-dependent object the definition is designed to exclude. The lesson is that the law is a demand about all changes of basis, not about some.
:::

## Exercises

### A. Check your understanding

:::: {#exr-index-notation-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the components of a tensor of type \( (p, q) \) in an ordered basis, and say which indices go upstairs.
2. State the summation convention, and write \( \xi(\v) \) with it.
3. For a type \( (1,1) \) tensor, write out the transformation law and name the relation it expresses between the two matrices.
4. Give the transformation law for type \( (0,2) \) and name the relation.
5. True or false: any \( n \times n \) array of scalars, attached to every basis, is a tensor of type \( (1,1) \). Justify your answer.
:::
::::

::: {.solution}
(a) They are the unique coordinates of \( t \) in the basis of @thm-tensor-basis built from \( \sB \) and \( \sB^{*} \) (@def-tensor-components). An index belonging to a \( V \)-slot goes upstairs; one belonging to a \( V^{*} \)-slot goes downstairs.

(b) An index occurring once upstairs and once downstairs in a product is summed from \( 1 \) to \( n \), with the summation sign suppressed. So \( \xi(\v) = \xi_i v^i \).

(c) \( (T')^{k}_{l} = q^{k}_{i}p^{j}_{l}T^{i}_{j} \), that is \( \T' = \P^{-1}\T\P \): the two matrices are **similar** (@thm-change-of-basis-maps).

(d) \( (T')_{kl} = p^{i}_{k}p^{j}_{l}T_{ij} \), that is \( \T' = \P\tp\T\P \): the two matrices are **congruent** (@thm-change-of-basis-form, @def-congruent).

(e) False. The rule must satisfy the transformation law; the constant rule \( \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \) does not, as the warning above shows.
:::

### B. Practice

:::: {#exr-index-notation-b1}
[B1: Transforming components]

Let \( V \) be a \( 2 \)-dimensional space over \( \nQ \) with basis \( \sB = (\v_1, \v_2) \), and let \( \sB' = (\v_1 + \v_2,\; \v_1 + 2\v_2) \).

::: {.enumerate options="label=(\alph*)"}
1. Write down \( \P = \mtx{\id}{\sB'}{\sB} \) and \( \Q = \P^{-1} \).
2. Let \( t \in T^1_1(V) \) have components \( T^1_1 = 1 \), \( T^1_2 = 2 \), \( T^2_1 = 3 \), \( T^2_2 = 4 \) in \( \sB \). Find its components in \( \sB' \).
3. Let \( s \in T^0_2(V) \) have the same array \( S_{ij} \) of components in \( \sB \). Find its components in \( \sB' \), and compare with (b).
4. Compute \( C^1_1(t) \) in both bases and check that the two answers agree.
:::
::::

::: {.solution}
(a) The columns of \( \P \) are the \( \sB \)-coordinates of the vectors of \( \sB' \), so
\[
\P = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix},
\qquad
\Q = \P^{-1} = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix},
\]
using @thm-two-by-two-inverse with \( \det \P = 1 \).

(b) By @thm-tensor-transformation-law, \( \T' = \P^{-1}\T\P \). With \( \T = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \),
\[
\P^{-1}\T = \begin{pmatrix} -1 & 0 \\ 2 & 2 \end{pmatrix},
\qquad
\T' = \begin{pmatrix} -1 & -1 \\ 4 & 6 \end{pmatrix}.
\]

(c) Now the law gives \( \S' = \P\tp\S\P \). With \( \P\tp = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} \) (this \( \P \) is symmetric),
\[
\P\tp\S = \begin{pmatrix} 4 & 6 \\ 7 & 10 \end{pmatrix},
\qquad
\S' = \begin{pmatrix} 10 & 16 \\ 17 & 27 \end{pmatrix}.
\]
The same array in the same two bases produces completely different answers, because the two objects are of different types.

(d) In \( \sB \): \( T^1_1 + T^2_2 = 1 + 4 = 5 \). In \( \sB' \): \( -1 + 6 = 5 \). They agree, as they must, since @def-contraction-slots is defined without reference to a basis. (By contrast, the "trace" of the type \( (0,2) \) arrays is \( 1 + 4 = 5 \) against \( 10 + 27 = 37 \): there is no contraction of two lower indices, and summing \( S_{ii} \) is not a basis-free operation.)
:::

:::: {#exr-index-notation-b2}
[B2: Tensor or not?]

Let \( \dim V = 2 \). For each rule below, determine whether it is a classical tensor of the stated type. Justify your answer, using \( \sB = (\v_1, \v_2) \) and \( \sB' = (\v_2, \v_1) \) or \( \sB' = (\v_1, \v_1 + \v_2) \) where a counterexample is needed.

::: {.enumerate options="label=(\alph*)"}
1. Type \( (1,1) \): \( A_{\sB} = \I_2 \) for every \( \sB \).
2. Type \( (1,1) \): \( A_{\sB} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) for every \( \sB \).
3. Type \( (0,2) \): \( A_{\sB} = \0 \) for every \( \sB \).
4. Type \( (1,1) \): \( A_{\sB} = (\tr \M_{\sB})\I_2 \), where \( \M_{\sB} \) is the matrix in \( \sB \) of one fixed operator \( M \in \cL(V) \).
:::
::::

::: {.solution}
(a) Yes. The law demands \( \P^{-1}\I_2\P = \I_2 \), which holds for every invertible \( \P \). The tensor is \( \id_V \).

(b) No. With \( \sB' = (\v_2, \v_1) \) we get \( \P = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \P^{-1} \), and \( \P^{-1}A\P = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \ne A \). (This is the standard non-diagonalizable matrix of Chapter 8; here it is failing a different test.)

(c) Yes. The law reads \( \0 = \P\tp\0\P \), which holds. The tensor is the zero tensor, and the zero array is the one array that is a tensor of every type.

(d) Yes. By @thm-trace-similarity-invariant the scalar \( c = \tr \M_{\sB} \) is the same for every \( \sB \), so the rule is the constant rule \( c\,\I_2 \), and \( \P^{-1}(c\I_2)\P = c\I_2 \). The tensor is \( c\,\id_V \). The point of contrast with (b) is that \( c \) was itself built basis-freely.
:::

### C. Going deeper

:::: {#exr-index-notation-c1}
[C1: Contraction in indices]

Let \( \dim V = n \) and let \( t \in T^{1}_{1}(V) \) have components \( T^i_j \) in \( \sB \) and \( (T')^k_l \) in \( \sB' \).

::: {.enumerate options="label=(\alph*)"}
1. Prove directly from @thm-tensor-transformation-law that \( (T')^{k}_{k} = T^{i}_{i} \), without using @thm-trace-is-contraction.
2. Let \( t \in T^{2}_{1}(V) \) with components \( T^{ij}_{k} \). Show that \( U^{j} \coloneqq T^{ij}_{i} \) are the components of a type \( (1,0) \) tensor, and identify it in terms of @def-contraction-slots.
3. Let \( s \in T^{2}_{0}(V) \) have components \( S^{ij} \). Show that the scalar \( \sum_i S^{ii} \) is **not** basis-independent, and say which step of (b) fails for it.
:::
::::

::: {.solution}
(a) By the law, \( (T')^{k}_{l} = q^{k}_{i}p^{j}_{l}T^{i}_{j} \). Setting \( l = k \) and summing,
\[
(T')^{k}_{k} = \sum_{k}\sum_{i,j} q^{k}_{i}p^{j}_{k}T^{i}_{j}
= \sum_{i,j}\Big(\sum_{k} p^{j}_{k}q^{k}_{i}\Big)T^{i}_{j}
= \sum_{i,j}\delta^{j}_{i}T^{i}_{j} = \sum_{i}T^{i}_{i},
\]
where the inner sum is the \( (j, i) \) entry of \( \P\Q = \I_n \).

(b) By @thm-tensor-transformation-law for type \( (2,1) \), \( (T')^{km}_{l} = q^{k}_{i}q^{m}_{j}p^{r}_{l}T^{ij}_{r} \). Setting \( l = k \) and summing over \( k \),
\[
(U')^{m} = \sum_{k}(T')^{km}_{k}
= q^{m}_{j}\Big(\sum_{k,i,r} q^{k}_{i}p^{r}_{k}T^{ij}_{r}\Big)
= q^{m}_{j}\,\delta^{r}_{i}T^{ij}_{r} = q^{m}_{j}U^{j},
\]
which is the transformation law for a single upper index. So \( (U^j) \) is a classical tensor of type \( (1,0) \), and by @thm-classical-equals-modern it is a vector; it is \( C^1_1(t) \), the contraction of the first upper slot against the lower one (@def-contraction-slots).

(c) Take \( n = 2 \) and \( s = \v_1 \otimes \v_1 \), so \( S^{11} = 1 \) and the other components vanish; then \( \sum_i S^{ii} = 1 \). Let \( \sB' = (\v_1 + \v_2,\ \v_2) \), so that \( \P = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} \) and \( \v_1 = \v'_1 - \v'_2 \). Expanding,
\[
s = (\v'_1 - \v'_2) \otimes (\v'_1 - \v'_2),
\]
so \( (S')^{11} = (S')^{22} = 1 \) and \( (S')^{12} = (S')^{21} = -1 \). Hence \( \sum_k (S')^{kk} = 2 \ne 1 \). The step that fails is the collapse in (b): setting the two indices equal pairs a factor \( q^{k}_{i} \) with another factor \( q^{k}_{j} \), and \( \sum_k q^{k}_{i}q^{k}_{j} \) is an entry of \( \Q\tp\Q \), not of \( \P\Q = \I_n \), so nothing cancels. Only an upper index repeated against a **lower** one is a contraction.
:::

:::: {#exr-index-notation-c2}
[C2: Raising an index needs a form]

Let \( V \) be finite-dimensional over \( F \) and let \( \beta \) be a non-degenerate bilinear form on \( V \), with components \( g_{ij} = \beta(\v_i, \v_j) \) in \( \sB \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that the matrix \( \G = (g_{ij}) \) is invertible, and let \( (g^{ij}) \) denote the entries of \( \G^{-1} \).
2. Let \( t \in T^{0}_{1}(V) \) have components \( T_{j} \). Show that \( U^{i} \coloneqq g^{ij}T_{j} \) satisfies the type \( (1,0) \) transformation law, so that "raising the index with \( \beta \)" produces a genuine tensor.
3. Explain in one or two sentences why this does **not** contradict the warning that there is no canonical map \( V^{*} \to V \).
:::
::::

::: {.solution}
(a) By @prp-nondegenerate-iff-invertible, \( \beta \) is non-degenerate exactly when \( \G = \mtx{\beta}{\sB}{\sB} \) is invertible.

(b) By @thm-change-of-basis-form, \( \G' = \P\tp\G\P \), so \( (\G')^{-1} = \P^{-1}\G^{-1}(\P\tp)^{-1} = \Q\G^{-1}\Q\tp \), that is \( (g')^{kl} = q^{k}_{i}q^{l}_{j}g^{ij} \): the inverse array carries two upper indices. Also \( (T')_{l} = p^{r}_{l}T_{r} \) by @thm-tensor-transformation-law. Hence
\[
\begin{aligned}
(U')^{k} &= (g')^{kl}(T')_{l}
= q^{k}_{i}\,g^{ij}\Big(\sum_{l} q^{l}_{j}p^{r}_{l}\Big)T_{r} \\
&= q^{k}_{i}\,g^{ij}\,\delta^{r}_{j}\,T_{r}
= q^{k}_{i}\,g^{ij}T_{j} = q^{k}_{i}U^{i},
\end{aligned}
\]
using \( \sum_{l} p^{r}_{l}q^{l}_{j} = (\P\Q)^{r}_{j} = \delta^{r}_{j} \). That is the type \( (1,0) \) law.

(c) The map is canonical *given \( \beta \)*, not given \( V \) alone: a different non-degenerate form raises indices differently, and there is no distinguished choice. This is the same point as the warning after @def-contraction: the isomorphism \( V \cong V^{*} \) is extra structure, which Chapter 10 supplies with an inner product and Chapter 13 with a form.
:::
