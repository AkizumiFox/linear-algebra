# Symmetric Powers

The tensor algebra is free, and being free it is useless on its own: it records the order of the slots even when nothing in the problem cares about the order. A symmetric bilinear form does not care (@def-symmetric-form); nor does a quadratic form; nor does the monomial \( x_1x_2 \), which is the same polynomial as \( x_2x_1 \). This section forces \( \operatorname{T}(V) \) to forget the order, by dividing the tensor power \( V^{\otimes k} \) by the span of the differences \( \u \otimes \w - \w \otimes \u \). The result, the symmetric power \( \Sym^k V \), turns out to have a basis indexed by non-decreasing index tuples, and the algebra assembled from all the \( \Sym^k V \) turns out to be the polynomial algebra of Chapter 0, one variable per basis vector.

The construction repeats Section 02's three moves for the second time: universal property, uniqueness, then a model built as a quotient. If the shape of the argument below feels familiar, that is the intention.

Throughout, \( F \) is a field, \( V \) is a finite-dimensional vector space over \( F \) with \( n = \dim V \ge 1 \), and \( k \ge 1 \) unless stated otherwise. **The field is arbitrary**, and the single place where the characteristic matters is isolated in the last part of the section.

## Symmetric multilinear maps

Before asking for a space, we name the maps it is supposed to linearize. Chapter 13 called a *bilinear form* symmetric when swapping its two arguments changed nothing (@def-symmetric-form). With \( k \) arguments there are more ways to rearrange them, and we demand invariance under all of them.

*A symmetric map cannot tell in which order its arguments were handed to it.*

::: {#def-symmetric-multilinear-map}
[Symmetric Multilinear Map]

Let \( W \) be a vector space over \( F \). A \( k \)-linear map \( f \colon V^k \to W \) (@def-multilinear-map) is **symmetric** if
\[
f(\u_{\sigma(1)}, \u_{\sigma(2)}, \dots, \u_{\sigma(k)}) = f(\u_1, \u_2, \dots, \u_k)
\]
**for every** permutation \( \sigma \in S_k \) and **for all** \( \u_1, \dots, \u_k \in V \).
:::

At \( k = 2 \) the only non-identity permutation is the swap, so this is exactly @def-symmetric-form with a general target \( W \) in place of \( F \). At \( k = 1 \) the condition is empty and every linear map is symmetric.

Three examples and one non-example.

- **A symmetric bilinear form**, \( \beta \colon V \times V \to F \) with \( \beta(\u, \w) = \beta(\w, \u) \). This is the case \( k = 2 \), \( W = F \).
- **Products of one fixed functional.** For \( \varphi \in V^{*} \), the map \( (\u_1, \dots, \u_k) \mapsto \varphi(\u_1)\varphi(\u_2)\cdots\varphi(\u_k) \) is \( k \)-linear, by the third example after @def-multilinear-form, and symmetric because multiplication in \( F \) is commutative: rearranging the factors does not change the product.
- **Multiplication in a commutative algebra.** If \( A \) is a commutative \( F \)-algebra and \( f \colon V \to A \) is linear, then \( (\u_1, \dots, \u_k) \mapsto f(\u_1)\cdots f(\u_k) \) is symmetric, by commutativity of \( A \).
- **A non-example by minimal change.** On \( V = F^2 \), the map \( (\u, \w) \mapsto u_1w_2 \) is bilinear but not symmetric: it sends \( (\e_1, \e_2) \) to \( 1 \) and \( (\e_2, \e_1) \) to \( 0 \). Only the symmetry clause fails; bilinearity survives untouched.

Note which permutations are allowed: **all** of \( S_k \), not only the swaps of adjacent slots. Nothing is lost by asking for all of them, and asking for all of them spares us a lemma about generating \( S_k \).

## The symmetric power

Now the object. The demand is @def-tensor-power's, restricted to the symmetric maps.

*The \( k \)-th symmetric power is the space in which symmetric \( k \)-linear maps become linear.*

::: {#def-symmetric-power}
[\( k \)-th Symmetric Power]

A **\( k \)-th symmetric power of \( V \)** is a pair \( (P, \pi) \), where \( P \) is a vector space over \( F \) and \( \pi \colon V^k \to P \) is a **symmetric** \( k \)-linear map, such that

::: {.enumerate options="label=(S\arabic*)"}
1. (**universal property**) for **every** vector space \( W \) over \( F \) and **every symmetric** \( k \)-linear map \( f \colon V^k \to W \), there is a **unique** linear map \( \bar f \colon P \to W \) with \( \bar f \circ \pi = f \).
:::

We write \( \Sym^k V \) for \( P \) and denote the value \( \pi(\u_1, \dots, \u_k) \) by juxtaposition,
\[
\u_1\u_2\cdots\u_k \coloneqq \pi(\u_1, \dots, \u_k),
\]
calling it a **symmetric product**. By convention \( \Sym^0 V = F \).
:::

The one difference from (T1) is the word **symmetric**, in two places: the structure map \( \pi \) is required to be symmetric, and only symmetric maps \( f \) are required to factor. Both changes are needed. If \( \pi \) were not symmetric, the notation \( \u\w = \w\u \) would be false; if non-symmetric maps had to factor, no space could do the job, since \( \bar f \circ \pi \) is symmetric whenever \( \pi \) is.

Uniqueness is the template of @thm-tensor-unique for the third time, and we no longer write it out.

::: {#thm-symmetric-power-unique}
[Uniqueness of the Symmetric Power]

Let \( (P, \pi) \) and \( (P', \pi') \) both be \( k \)-th symmetric powers of \( V \). Then there is a unique linear isomorphism \( \varphi \colon P \to P' \) with \( \varphi \circ \pi = \pi' \).
:::

::: {.proof}
Word for word the proof of @thm-tensor-power-unique, with "symmetric \( k \)-linear" in place of "\( k \)-linear" throughout: (S1) for \( P \) applied to the symmetric map \( \pi' \) gives \( \varphi \), (S1) for \( P' \) applied to \( \pi \) gives \( \psi \), the composite \( \psi\varphi \) is a linear self-map of \( P \) with \( \psi\varphi\pi = \pi \), and the uniqueness clause of (S1) applied to \( \pi \) forces \( \psi\varphi = \id_P \). Symmetrically \( \varphi\psi = \id_{P'} \). This proves the theorem.
:::

And now the model: the tensor power, divided by the relations we want to impose.

::: {#thm-symmetric-power-exists}
[Existence of the Symmetric Power]

Let \( C_k \subseteq V^{\otimes k} \) be the span of all the elements
\[
\u_1 \otimes \dots \otimes \u_k
- \u_{\sigma(1)} \otimes \dots \otimes \u_{\sigma(k)},
\qquad \u_i \in V, \ \sigma \in S_k ,
\]
and let \( q \colon V^{\otimes k} \to V^{\otimes k}/C_k \) be the quotient map (@def-quotient-space). Then \( V^{\otimes k}/C_k \), together with
\[
\pi(\u_1, \dots, \u_k) = q(\u_1 \otimes \dots \otimes \u_k),
\]
is a \( k \)-th symmetric power of \( V \). At \( k = 2 \) the subspace \( C_2 \) is the span of the elements \( \u \otimes \w - \w \otimes \u \).
:::

::: {.idea}
Two things to check, and both are one line each once the right tool is named. That \( \pi \) is symmetric is the definition of \( C_k \): permuting the arguments changes the tensor by an element of \( C_k \), which \( q \) kills. That symmetric maps factor is @thm-quotient-universal-property: turn \( f \) into a linear map on \( V^{\otimes k} \) by (T1), observe that symmetry of \( f \) makes it vanish on the generators of \( C_k \), and let the quotient's universal property do the rest. This is the move the chapter uses three times: **a quotient kills exactly the relations you want.**
:::

::: {.proof}
\( C_k \) is a subspace, being a span. The map \( \pi \) is \( k \)-linear, being the \( k \)-linear \( \mu_k \) of @thm-tensor-power-exists followed by the linear map \( q \). It is symmetric: for \( \sigma \in S_k \), the difference
\[
\u_1 \otimes \dots \otimes \u_k
- \u_{\sigma(1)} \otimes \dots \otimes \u_{\sigma(k)}
\]
lies in \( C_k \) by definition, so the two tensors have the same image under \( q \), that is, \( \pi(\u_{\sigma(1)}, \dots, \u_{\sigma(k)}) = \pi(\u_1, \dots, \u_k) \).

Now let \( f \colon V^k \to W \) be symmetric \( k \)-linear. By (T1) there is a unique linear \( \tilde f \colon V^{\otimes k} \to W \) with \( \tilde f(\u_1 \otimes \dots \otimes \u_k) = f(\u_1, \dots, \u_k) \). On a generator of \( C_k \),
\[
\tilde f\bigl(\u_1 \otimes \dots \otimes \u_k
- \u_{\sigma(1)} \otimes \dots \otimes \u_{\sigma(k)}\bigr)
= f(\u_1, \dots, \u_k) - f(\u_{\sigma(1)}, \dots, \u_{\sigma(k)}),
\]
which is \( 0 \) because \( f \) is symmetric. A linear map vanishing on a spanning set of \( C_k \) vanishes on \( C_k \), so \( C_k \subseteq \ker\tilde f \). By @thm-quotient-universal-property (a) there is exactly one linear \( \bar f \colon V^{\otimes k}/C_k \to W \) with \( \bar f \circ q = \tilde f \), and then
\[
\bar f \circ \pi = \bar f \circ q \circ \mu_k = \tilde f \circ \mu_k = f .
\]

For uniqueness, suppose \( h \) is linear with \( h \circ \pi = f \). Since \( q \) is surjective and \( V^{\otimes k} \) is spanned by its simple tensors (@thm-tensor-power-exists), the elements \( \pi(\u_1, \dots, \u_k) \) span \( V^{\otimes k}/C_k \). So \( h \) and \( \bar f \) agree on a spanning set, hence everywhere. This proves the theorem.
:::

::: {.warning}
**\( \Sym^k V \) is a quotient of \( V^{\otimes k} \), not a subspace of it.** Its elements are cosets, and the identity \( \u\w = \w\u \) in \( \Sym^2 V \) says that \( \u\otimes\w \) and \( \w\otimes\u \) lie in the **same** coset. It does **not** say \( \u \otimes \w = \w \otimes \u \) in \( V^{\otimes 2} \), which is false for independent \( \u, \w \) by @thm-tensor-power-basis. Confusing the two is the commonest error here; the safe habit is never to write an element of \( \Sym^k V \) as a tensor.
:::

## A basis, and the dimension

Sorting an index tuple is now legal, so the basis of @thm-tensor-power-basis collapses: only the sorted tuples survive. Counting them is the substance of the section.

::: {#thm-symmetric-power-basis}
[Basis of a Symmetric Power]

Let \( \sB = (\v_1, \dots, \v_n) \) be a basis of \( V \) and \( k \ge 1 \). Then the symmetric products
\[
\v_{i_1}\v_{i_2}\cdots\v_{i_k},
\qquad 1 \le i_1 \le i_2 \le \dots \le i_k \le n ,
\]
one for each **non-decreasing** tuple, form a basis of \( \Sym^k V \). Consequently
\[
\dim \Sym^k V = \binom{n + k - 1}{k},
\]
over **every** field \( F \).
:::

::: {.idea}
Spanning is sorting: the image of any index tuple equals the image of its sorted version, so the sorted ones already span. Independence needs one linear functional per non-decreasing tuple, and it must be built **without dividing by anything**, since we want the theorem over every field. The functional that works is a sum over all ways of dealing out the \( n \) dual basis functionals to the \( k \) slots with prescribed multiplicities: every coefficient in it is \( 1 \). Counting the tuples is then the stars-and-bars bijection, which turns a non-decreasing tuple into a strictly increasing one by adding \( 0, 1, 2, \dots \) to its entries.
:::

::: {.proof}
*Spanning.* By @thm-tensor-power-basis the tensors \( \v_{j_1}\otimes\dots\otimes\v_{j_k} \), over all tuples \( J \), form a basis of \( V^{\otimes k} \), and \( q \) is surjective, so their images \( \v_{j_1}\cdots\v_{j_k} \) span \( \Sym^k V \). Given any \( J \), let \( \sigma \in S_k \) sort it, so that \( (j_{\sigma(1)}, \dots, j_{\sigma(k)}) \) is non-decreasing. Since \( \pi \) is symmetric, \( \v_{j_1}\cdots\v_{j_k} = \v_{j_{\sigma(1)}}\cdots\v_{j_{\sigma(k)}} \). So the non-decreasing tuples already give a spanning set.

*Independence.* Let \( (\varphi_1, \dots, \varphi_n) \) be the dual basis of \( \sB \) (@thm-dual-basis). For a non-decreasing tuple \( I = (i_1, \dots, i_k) \), let
\[
m_j = \lvert\{\, t : i_t = j \,\}\rvert, \qquad j = 1, \dots, n,
\]
be its **multiplicity vector**, so \( m_1 + \dots + m_n = k \), and let \( \Phi(I) \) be the set of functions \( \tau \colon \{1, \dots, k\} \to \{1, \dots, n\} \) taking the value \( j \) exactly \( m_j \) times, for each \( j \). Define
\[
g_I(\u_1, \dots, \u_k)
= \sum_{\tau \in \Phi(I)} \varphi_{\tau(1)}(\u_1)\,\varphi_{\tau(2)}(\u_2)\cdots\varphi_{\tau(k)}(\u_k).
\]
Each summand is \( k \)-linear, being a product of one functional per slot, so \( g_I \) is \( k \)-linear.

It is symmetric. Let \( \rho \in S_k \). Substituting and then reindexing the product by \( s = \rho(t) \),
\[
g_I(\u_{\rho(1)}, \dots, \u_{\rho(k)})
= \sum_{\tau \in \Phi(I)} \prod_{s=1}^{k} \varphi_{(\tau\rho^{-1})(s)}(\u_s) .
\]
The map \( \tau \mapsto \tau\rho^{-1} \) is a bijection of \( \Phi(I) \) onto itself, since composing with a permutation of the domain does not change how often a value is taken. So the sum is unchanged, and \( g_I \) is symmetric.

By (S1), \( g_I \) induces a linear \( \bar g_I \colon \Sym^k V \to F \). Evaluate it on a basis candidate: for any tuple \( J \),
\[
\bar g_I(\v_{j_1}\cdots\v_{j_k})
= \sum_{\tau \in \Phi(I)} \prod_{t=1}^{k}\delta_{\tau(t)\,j_t} .
\]
A summand is \( 1 \) exactly when \( \tau(t) = j_t \) for every \( t \), and \( 0 \) otherwise; so the whole sum is \( 1 \) if the function \( t \mapsto j_t \) belongs to \( \Phi(I) \), and \( 0 \) if it does not. For non-decreasing \( I \) and \( J \), that function lies in \( \Phi(I) \) exactly when \( J \) has the same multiplicity vector as \( I \), which for non-decreasing tuples means \( J = I \). Hence \( \bar g_I(\v_{j_1}\cdots\v_{j_k}) = \delta_{IJ} \).

Now suppose \( \sum_I a_I\,\v_{i_1}\cdots\v_{i_k} = \0 \), the sum over non-decreasing tuples. Applying \( \bar g_J \) leaves \( a_J = 0 \). Since \( J \) was arbitrary, every coefficient is \( 0 \), and the list is independent. So it is a basis.

*The count.* Send a non-decreasing tuple \( (i_1, \dots, i_k) \) to
\[
(i_1,\ i_2 + 1,\ i_3 + 2,\ \dots,\ i_k + k - 1).
\]
Consecutive entries satisfy \( i_t + t - 1 < i_{t+1} + t \) because \( i_t \le i_{t+1} \), so the image is **strictly** increasing, and its entries lie between \( 1 \) and \( n + k - 1 \). Conversely, subtracting \( 0, 1, \dots, k-1 \) from a strictly increasing tuple in \( \{1, \dots, n+k-1\} \) returns a non-decreasing tuple in \( \{1, \dots, n\} \): the differences \( j_{t+1} - j_t \ge 1 \) become \( i_{t+1} - i_t \ge 0 \), and \( 1 \le j_1 \), \( j_k \le n + k - 1 \) give \( 1 \le i_1 \) and \( i_k \le n \). The two assignments are mutually inverse, so the non-decreasing \( k \)-tuples from \( \{1, \dots, n\} \) are in bijection with the \( k \)-element subsets of \( \{1, \dots, n+k-1\} \), and there are \( \binom{n+k-1}{k} \) of those. This proves the theorem.
:::

Nothing in the proof divided by an integer, which is why the conclusion holds over \( \nF_2 \) as it does over \( \nC \). Keep that in view: the last part of this section shows that a *different* and very common description of \( \Sym^k V \) does not survive over \( \nF_2 \), and the difference between the two is exactly one division.

::: {.check}
Let \( \dim V = 3 \). Compute \( \dim \Sym^2 V \) and \( \dim V^{\otimes 2} \), and say which basis tensors of \( V^{\otimes 2} \) become equal in \( \Sym^2 V \).
:::

::: {.solution}
\( \dim \Sym^2 V = \binom{4}{2} = 6 \) and \( \dim V^{\otimes 2} = 3^2 = 9 \). The six surviving basis elements are \( \v_1^2, \v_1\v_2, \v_1\v_3, \v_2^2, \v_2\v_3, \v_3^2 \). The three pairs \( \v_i \otimes \v_j \) and \( \v_j \otimes \v_i \) with \( i < j \) become equal, which removes \( 3 \) from the count: \( 9 - 3 = 6 \).
:::

::: {#exm-symmetric-square-of-plane}
[A symmetric square, in coordinates]

Let \( V = F^2 \). Write down a basis of \( \Sym^2 V \) and expand \( (\e_1 + 2\e_2)(3\e_1 - \e_2) \) in it.
:::

::: {.solution}
By @thm-symmetric-power-basis a basis is \( (\e_1^2,\ \e_1\e_2,\ \e_2^2) \), of size \( \binom{3}{2} = 3 \). Expanding one slot at a time and then using \( \e_2\e_1 = \e_1\e_2 \),
\[
\begin{aligned}
(\e_1 + 2\e_2)(3\e_1 - \e_2)
&= 3\e_1\e_1 - \e_1\e_2 + 6\e_2\e_1 - 2\e_2\e_2 \\
&= 3\e_1^2 + 5\e_1\e_2 - 2\e_2^2 .
\end{aligned}
\]
Compare with expanding \( (x + 2y)(3x - y) = 3x^2 + 5xy - 2y^2 \) in ordinary algebra. That is not a coincidence, and the next part of this section says exactly what it is.
:::

::: {.warning}
**Not every element of \( \Sym^k V \) is a product of \( k \) vectors.** Take \( F = \nR \), \( V = \nR^2 \) and \( \omega = \e_1^2 + \e_2^2 \in \Sym^2 V \). If \( \omega = \u\w \) with \( \u = a\e_1 + b\e_2 \) and \( \w = c\e_1 + d\e_2 \), then comparing coordinates in the basis \( (\e_1^2, \e_1\e_2, \e_2^2) \) gives \( ac = 1 \), \( ad + bc = 0 \) and \( bd = 1 \). The first and last force \( a, b, c, d \ne 0 \), and multiplying \( ad = -bc \) by \( bc \) gives \( -(bc)^2 = (ac)(bd) = 1 \), impossible in \( \nR \). This is the same phenomenon as the non-simple tensors of Section 02, and it is why \( \Sym^k V \) is much larger than the set of products.
:::

## The symmetric algebra is a polynomial algebra

Stacking the symmetric powers gives an algebra, exactly as stacking the tensor powers did, and the multiplication descends from concatenation.

::: {#prp-symmetric-product-well-defined}
[The Symmetric Product of Two Symmetric Tensors]

Let \( k, l \ge 1 \). There is a unique bilinear map \( \Sym^k V \times \Sym^l V \to \Sym^{k+l} V \) with
\[
(\u_1\cdots\u_k)\,(\w_1\cdots\w_l) = \u_1\cdots\u_k\w_1\cdots\w_l .
\]
:::

::: {.proof}
*Concatenation carries the relations into the relations.* Let \( x \in C_k \) and \( y \in V^{\otimes l} \). For a generator \( x = \u_1\otimes\dots\otimes\u_k - \u_{\sigma(1)}\otimes\dots\otimes\u_{\sigma(k)} \) and a simple \( y = \w_1\otimes\dots\otimes\w_l \), the product \( x\cdot y \) of @prp-tensor-concatenation is again a generator of \( C_{k+l} \), for the permutation acting as \( \sigma \) on the first \( k \) slots and fixing the last \( l \). Since generators span \( C_k \), since \( V^{\otimes l} \) is spanned by its simple tensors, and since \( \cdot \) is bilinear, \( C_k \cdot V^{\otimes l} \subseteq C_{k+l} \). Swapping the roles of the two blocks gives \( V^{\otimes k}\cdot C_l \subseteq C_{k+l} \).

*Descending, one argument at a time.* Let \( q_m \colon V^{\otimes m} \to \Sym^m V \) denote the quotient maps. Fix \( y \in V^{\otimes l} \). The linear map \( x \mapsto q_{k+l}(x \cdot y) \) kills \( C_k \) by the first inclusion, so @thm-quotient-universal-property gives a unique linear \( \beta_y \colon \Sym^k V \to \Sym^{k+l}V \) with \( \beta_y(q_k x) = q_{k+l}(x\cdot y) \). The assignment \( y \mapsto \beta_y \) is linear, since \( \beta_{ay + y'} \) and \( a\beta_y + \beta_{y'} \) agree on the spanning set \( q_k(V^{\otimes k}) = \Sym^k V \); and it kills \( C_l \), since \( y \in C_l \) gives \( x \cdot y \in C_{k+l} \) and hence \( \beta_y = 0 \). By @thm-quotient-universal-property again it descends to a linear map \( \Sym^l V \to \cL(\Sym^k V, \Sym^{k+l}V) \), and evaluating gives the required bilinear map. It is unique because the products of vectors span each factor. When \( k = 0 \) or \( l = 0 \) the product is scalar multiplication, as in Section 06. This proves the proposition.
:::

::: {#def-symmetric-algebra}
[Symmetric Algebra]

The **symmetric algebra** of \( V \) is the vector space
\[
\Sym(V) = \bigoplus_{k \ge 0}\Sym^k V,
\]
of sequences with finitely many non-zero components, with the multiplication assembled from @prp-symmetric-product-well-defined by \( (xy)_m = \sum_{k+l=m} x_ky_l \).
:::

::: {#prp-symmetric-algebra-commutative}
[\( \Sym(V) \) Is a Commutative Algebra]

\( \Sym(V) \) is an associative, **commutative**, unital \( F \)-algebra with identity \( 1 \in \Sym^0 V = F \), and \( \Sym^k V \cdot \Sym^l V \subseteq \Sym^{k+l}V \).
:::

::: {.proof}
Bilinearity, associativity and the identity are proved exactly as in @thm-tensor-algebra-is-an-algebra: all three are identities between multilinear expressions, so it suffices to check them on products of vectors, which span each \( \Sym^k V \), and there all three read "concatenate the strings".

Commutativity is the new point. Both \( (\u_1\cdots\u_k)(\w_1\cdots\w_l) \) and \( (\w_1\cdots\w_l)(\u_1\cdots\u_k) \) equal the symmetric product of the same \( k + l \) vectors in two different orders, and \( \pi \) is symmetric, so they are equal. Two bilinear maps agreeing on spanning sets of both arguments agree everywhere, so \( xy = yx \) for all \( x, y \). This proves the proposition.
:::

To name what \( \Sym(V) \) is, we need polynomials in more than one variable. Chapter 0 built \( F[x] \); the several-variable version is the same construction with monomials indexed by exponent vectors.

::: {#def-polynomial-algebra-several-variables}
[The Polynomial Algebra \( F[x_1, \dots, x_n] \)]

Let \( n \ge 1 \). The **polynomial algebra in \( n \) variables** over \( F \) is the vector space \( F[x_1, \dots, x_n] \) with basis the **monomials**
\[
x^{\a} = x_1^{a_1}x_2^{a_2}\cdots x_n^{a_n},
\qquad \a = (a_1, \dots, a_n) \in \nN^n ,
\]
with the unique bilinear multiplication satisfying \( x^{\a}x^{\b} = x^{\a + \b} \). The **degree** of \( x^{\a} \) is \( \lvert\a\rvert = a_1 + \dots + a_n \), and \( F[x_1, \dots, x_n]_k \) denotes the span of the monomials of degree \( k \).
:::

The bilinear extension exists and is unique because a bilinear map may be prescribed freely on a pair of bases, by the argument used twice in the proof of @prp-tensor-concatenation. The multiplication is associative, commutative and unital, with identity the monomial all of whose exponents are \( 0 \), because exponent addition in \( \nN^n \) is associative, commutative and has an identity. For \( n = 1 \) the monomials are \( 1, x, x^2, \dots \) and the rule is \( x^ax^b = x^{a+b} \), so \( F[x_1] \) is the ring \( F[x] \) of @def-polynomial-ring, whose basis of monomials is @exm-basis-of-polynomials. Everything Chapter 5 proved — division, greatest common divisors, unique factorization — lives in that one-variable case.

::: {#thm-symmetric-algebra-is-polynomials}
[The Symmetric Algebra Is a Polynomial Algebra]

Let \( \sB = (\v_1, \dots, \v_n) \) be a basis of \( V \). Then there is an isomorphism of \( F \)-algebras
\[
\Psi \colon \Sym(V) \xrightarrow{\ \sim\ } F[x_1, \dots, x_n],
\qquad \Psi(\v_i) = x_i ,
\]
and it carries \( \Sym^k V \) onto \( F[x_1, \dots, x_n]_k \). In particular
\[
\dim F[x_1, \dots, x_n]_k = \binom{n+k-1}{k} .
\]
:::

::: {.idea}
Both sides have a basis indexed by the same combinatorial object: a non-decreasing \( k \)-tuple on the left, a degree-\( k \) monomial on the right, and each is determined by its multiplicity vector \( \m \in \nN^n \) with \( \lvert\m\rvert = k \). So match the bases, which gives a linear isomorphism for free, and then check multiplicativity on basis elements, where both products are "add the exponent vectors".
:::

::: {.proof}
Write \( \lvert\m\rvert = m_1 + \dots + m_n \) for \( \m \in \nN^n \). Given \( \m \) with \( \lvert\m\rvert = k \), let \( I(\m) \) be the non-decreasing tuple taking the value \( j \) exactly \( m_j \) times, and write \( \v^{\m} \) for the corresponding symmetric product \( \v_{i_1}\cdots\v_{i_k} \). The assignment \( \m \mapsto I(\m) \) is a bijection onto the non-decreasing \( k \)-tuples, since a non-decreasing tuple is recovered from its multiplicity vector and conversely. So by @thm-symmetric-power-basis the family \( (\v^{\m})_{\lvert\m\rvert = k} \) is a basis of \( \Sym^k V \), and hence \( (\v^{\m})_{\m \in \nN^n} \) is a basis of \( \Sym(V) \).

Define \( \Psi \) to be the unique linear map with \( \Psi(\v^{\m}) = x^{\m} \), which exists by @thm-linear-map-from-any-basis. It sends a basis of \( \Sym(V) \) bijectively onto the basis of monomials, so it is a linear isomorphism, and it sends the degree-\( k \) basis onto the degree-\( k \) monomials, so \( \Psi(\Sym^k V) = F[x_1, \dots, x_n]_k \).

Multiplicativity: the maps \( (y, z) \mapsto \Psi(yz) \) and \( (y, z) \mapsto \Psi(y)\Psi(z) \) are bilinear, so it is enough to compare them on the basis. By @prp-symmetric-product-well-defined, \( \v^{\m}\v^{\m'} \) is the symmetric product of the \( \lvert\m\rvert + \lvert\m'\rvert \) vectors of the two strings, which after sorting is \( \v^{\m + \m'} \); and \( x^{\m}x^{\m'} = x^{\m+\m'} \) by @def-polynomial-algebra-several-variables. Also \( \Psi \) sends the empty product \( 1 \) to the monomial with all exponents \( 0 \), which is \( 1 \). Hence \( \Psi \) is an algebra isomorphism. Finally \( \v_i \) is the basis element \( \v^{\m} \) whose \( \m \) has a single \( 1 \) in position \( i \), so \( \Psi(\v_i) = x_i \).

The dimension formula follows from @thm-symmetric-power-basis, since \( \Psi \) restricts to an isomorphism in each degree. This proves the theorem.
:::

So the symmetric algebra is nothing exotic: *it is the polynomial algebra, with one variable per basis vector of \( V \).* The isomorphism depends on the basis, exactly as the coordinate isomorphism \( V \cong F^n \) does; \( \Sym(V) \) is the basis-free version of "polynomials in \( n \) variables", and \( \Sym^k V \) is the basis-free version of "homogeneous polynomials of degree \( k \)". Read backwards, the theorem also computes something Chapter 5 never did: the number of monomials of degree \( k \) in \( n \) variables is \( \binom{n+k-1}{k} \).

::: {.remark}
The case \( k = 2 \) recovers a count from Chapter 13. A symmetric bilinear form on \( V \) is a symmetric \( 2 \)-linear map into \( F \), so by (S1) the symmetric forms on \( V \) are in bijection with the linear functionals on \( \Sym^2 V \), and there are \( \binom{n+1}{2} = n(n+1)/2 \) dimensions of them — the number of entries on and above the diagonal of a symmetric matrix, which is what @prp-form-symmetry-matrix would give by counting.
:::

## Symmetric powers versus symmetric tensors

Here is the trap, and it is worth the space. Many treatments define the \( k \)-th symmetric power as a **subspace** of \( V^{\otimes k} \): the tensors left fixed by every permutation of the slots. That is a different construction from the quotient above, and over a field of characteristic \( 0 \) the two agree. Over \( \nF_2 \) they do not, and the reason is a single division by \( k! \).

We first need the permutation operators.

::: {#lem-slot-permutation}
[Permuting the Slots of a Tensor]

For each \( \sigma \in S_k \) there is a unique linear operator \( P_\sigma \) on \( V^{\otimes k} \) with
\[
P_\sigma(\u_1 \otimes \dots \otimes \u_k)
= \u_{\sigma(1)} \otimes \dots \otimes \u_{\sigma(k)} ,
\]
and \( P_\sigma P_\tau = P_{\tau\sigma} \) for all \( \sigma, \tau \in S_k \), with \( P_{\id} = \id \).
:::

::: {.proof}
The map \( (\u_1, \dots, \u_k) \mapsto \u_{\sigma(1)} \otimes \dots \otimes \u_{\sigma(k)} \) is \( k \)-linear, since in slot \( t \) it is \( \mu_k \) in slot \( \sigma^{-1}(t) \). So (T1) gives a unique linear \( P_\sigma \) with the stated values, and uniqueness holds because those tensors span \( V^{\otimes k} \). For the composition rule, put \( \w_t = \u_{\tau(t)} \); then
\[
P_\sigma P_\tau(\u_1\otimes\dots\otimes\u_k)
= P_\sigma(\w_1\otimes\dots\otimes\w_k)
= \w_{\sigma(1)}\otimes\dots\otimes\w_{\sigma(k)},
\]
and \( \w_{\sigma(t)} = \u_{\tau(\sigma(t))} \), which is the \( t \)-th argument of \( P_{\tau\sigma} \). Both sides are linear and agree on simple tensors, hence are equal. This proves the lemma.
:::

::: {#def-symmetric-tensor}
[Symmetric Tensor]

A tensor \( x \in V^{\otimes k} \) is **symmetric** if \( P_\sigma x = x \) for **every** \( \sigma \in S_k \). The symmetric tensors form a subspace of \( V^{\otimes k} \), which we write \( (V^{\otimes k})^{S_k} \); it is the intersection of the kernels of the linear maps \( P_\sigma - \id \).
:::

::: {#thm-symmetric-tensors-vs-symmetric-power}
[Symmetric Tensors and the Symmetric Power]

Let \( n = \dim V \ge 1 \) and \( k \ge 1 \), and let \( \iota \colon (V^{\otimes k})^{S_k} \to \Sym^k V \) be the restriction of the quotient map \( q \).

::: {.enumerate options="label=(\alph*)"}
1. Over **every** field, \( \dim (V^{\otimes k})^{S_k} = \binom{n+k-1}{k} = \dim \Sym^k V \).
2. If \( \operatorname{char} F = 0 \) or \( \operatorname{char} F > k \), then \( \iota \) is an isomorphism.
3. If \( \operatorname{char} F = 2 \), \( k = 2 \) and \( n \ge 2 \), then \( \iota \) is **neither** injective nor surjective.
:::
:::

::: {.idea}
For (a), a symmetric tensor must have equal coordinates along each orbit of basis tensors, so the **orbit sums** are a basis; orbits correspond to multisets, which @thm-symmetric-power-basis already counted. For (b), average: \( s = \sum_{\sigma} P_\sigma \) maps everything into the symmetric tensors and kills \( C_k \), so \( \frac{1}{k!}s \) is an inverse for \( \iota \) — provided \( k! \) is invertible, which is exactly the hypothesis. For (c), the tensor \( \v_1\otimes\v_2 + \v_2\otimes\v_1 \) is symmetric and non-zero, but its image is \( 2\v_1\v_2 = 0 \).
:::

::: {.proof}
(a) Let \( \sB = (\v_1, \dots, \v_n) \) be a basis of \( V \). For a tuple \( J \) write \( \v_J = \v_{j_1}\otimes\dots\otimes\v_{j_k} \), so that \( (\v_J)_J \) is a basis of \( V^{\otimes k} \) (@thm-tensor-power-basis), and note \( P_\sigma \v_J = \v_{J\sigma} \), where \( J\sigma \) is the tuple \( t \mapsto j_{\sigma(t)} \). Two tuples lie in the same **orbit** when one is a rearrangement of the other, that is, when they have the same multiplicity vector. For each non-decreasing \( I \) let \( s_I = \sum_{J \in O_I}\v_J \), the sum over the orbit of \( I \).

Each \( s_I \) is symmetric, because \( J \mapsto J\sigma \) permutes \( O_I \). The \( s_I \) are independent, because distinct orbits involve disjoint sets of basis vectors. They span: if \( x = \sum_J a_J\v_J \) satisfies \( P_\sigma x = x \) for every \( \sigma \), then comparing coordinates in \( \sum_J a_J \v_{J\sigma} = \sum_J a_J\v_J \) gives \( a_{J} = a_{J\sigma} \) for all \( J \) and \( \sigma \), so \( J \mapsto a_J \) is constant on orbits and \( x = \sum_I a_I s_I \). Hence \( (s_I) \) is a basis, with one member per orbit, that is, per multiplicity vector of total \( k \). By the bijection in the proof of @thm-symmetric-power-basis there are \( \binom{n+k-1}{k} \) of those. No division occurred, so this holds over every field.

(b) Let \( s = \sum_{\sigma \in S_k} P_\sigma \), a linear operator on \( V^{\otimes k} \). By @lem-slot-permutation, for any \( \tau \),
\[
P_\tau s = \sum_{\sigma} P_\tau P_\sigma = \sum_\sigma P_{\sigma\tau} = s ,
\qquad
s P_\tau = \sum_\sigma P_\sigma P_\tau = \sum_\sigma P_{\tau\sigma} = s ,
\]
since \( \sigma \mapsto \sigma\tau \) and \( \sigma \mapsto \tau\sigma \) are bijections of \( S_k \). The first identity says \( \im s \subseteq (V^{\otimes k})^{S_k} \). The second gives \( s(\id - P_\tau) = 0 \), and the generators of \( C_k \) are exactly the elements \( (\id - P_\sigma)(\u_1\otimes\dots\otimes\u_k) \), so \( C_k \subseteq \ker s \).

By hypothesis \( k! \cdot 1 \ne 0 \) in \( F \). Indeed \( k! \cdot 1 = (1\cdot 1)(2\cdot 1)\cdots(k \cdot 1) \) in \( F \), a product of \( k \) factors; if \( \operatorname{char} F = 0 \) none of them is \( 0 \), and if \( \operatorname{char} F = p > k \) then \( i \cdot 1 \ne 0 \) for \( 1 \le i \le k < p \) by @def-characteristic. A field has no zero divisors, so the product is non-zero, hence invertible. Since \( C_k \subseteq \ker s \), @thm-quotient-universal-property gives a linear map \( \theta \colon \Sym^k V \to (V^{\otimes k})^{S_k} \) with \( \theta(q(x)) = \frac{1}{k!}s(x) \).

Now compute both composites. For \( x \in V^{\otimes k} \), each \( P_\sigma x \) differs from \( x \) by an element of \( C_k \), so \( q(s(x)) = \sum_\sigma q(P_\sigma x) = k!\,q(x) \), whence
\[
\iota\theta(q(x)) = \tfrac{1}{k!}q(s(x)) = q(x),
\]
and \( q \) is surjective, so \( \iota\theta = \id \). Conversely, if \( x \) is symmetric then \( s(x) = \sum_\sigma P_\sigma x = k!\,x \), so \( \theta\iota(x) = \theta(q(x)) = \frac{1}{k!}k!\,x = x \). Hence \( \iota \) is an isomorphism with inverse \( \theta \).

(c) Let \( \operatorname{char} F = 2 \), \( k = 2 \), \( n \ge 2 \), and put \( t = \v_1\otimes\v_2 + \v_2\otimes\v_1 \). It is symmetric, since the only non-identity element of \( S_2 \) swaps the two summands, and it is non-zero, being a sum of two distinct basis vectors of \( V^{\otimes 2} \) (@thm-tensor-power-basis). But
\[
\iota(t) = \v_1\v_2 + \v_2\v_1 = 2\,\v_1\v_2 = 0
\]
because \( 1 + 1 = 0 \) in \( F \). So \( \ker\iota \ne \{\0\} \) and \( \iota \) is not injective. By (a) the two spaces have the same finite dimension, so a surjective \( \iota \) would be injective by @thm-rank-nullity; hence \( \iota \) is not surjective either. This proves the theorem.
:::

Part (b) is where the division lives, and part (c) is what it costs. The operator \( s \) still exists over \( \nF_2 \); what fails is the *rescaling* \( \frac{1}{k!}s \), and with it the splitting of the quotient.

::: {.warning}
**In characteristic \( p \le k \), "symmetric power" and "symmetric tensors" are different objects.** They have the same dimension by @thm-symmetric-tensors-vs-symmetric-power (a), so they are abstractly isomorphic, but the *natural* map between them is not an isomorphism, and no natural one is available. So: do not define \( \Sym^k V \) as \( (V^{\otimes k})^{S_k} \), do not write \( \frac{1}{k!}\sum_\sigma P_\sigma \) without saying that \( k! \) is invertible, and do not transport a statement proved for one to the other. This is Chapter 13's discipline again, where alternating and skew-symmetric forms coincided only away from characteristic \( 2 \) (@thm-alternating-vs-skew): the same clause, the same division, and the same smallest witness, \( \nF_2^2 \).
:::

Everything else in this section is characteristic-free. In particular @thm-symmetric-power-basis, @thm-symmetric-algebra-is-polynomials and the dimension \( \binom{n+k-1}{k} \) hold over every field, because the quotient construction never divides. The next section takes the same care with the same reward: the exterior power is built from a relation chosen so that no division is ever needed.

## Exercises

### A. Check your understanding

::: {#exr-symmetric-powers-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the universal property (S1), with every quantifier, and say which maps are required to factor.
2. Which subspace of \( V^{\otimes k} \) is divided out to build \( \Sym^k V \)? Write down its generators for \( k = 3 \).
3. Let \( \dim V = 4 \). Compute \( \dim \Sym^3 V \) and \( \dim V^{\otimes 3} \).
4. Determine whether \( \Sym^2 V \) is a subspace of \( V^{\otimes 2} \). Justify your answer.
5. What hypothesis on \( F \) makes the symmetric tensors of degree \( k \) naturally isomorphic to \( \Sym^k V \), and which step of the proof needs it?
:::
:::

::: {.solution}
(a) For every vector space \( W \) over \( F \) and every **symmetric** \( k \)-linear map \( f \colon V^k \to W \), there exists exactly one linear \( \bar f \colon \Sym^k V \to W \) with \( \bar f \circ \pi = f \). Only the symmetric maps factor; a non-symmetric one cannot, since \( \bar f\circ\pi \) is symmetric for every linear \( \bar f \).

(b) The subspace \( C_k \) of @thm-symmetric-power-exists, spanned by the differences \( \u_1\otimes\dots\otimes\u_k - \u_{\sigma(1)}\otimes\dots\otimes\u_{\sigma(k)} \). For \( k = 3 \) the generators are the six differences obtained from the six \( \sigma \in S_3 \), for all \( \u_1, \u_2, \u_3 \in V \).

(c) \( \dim \Sym^3 V = \binom{4+3-1}{3} = \binom{6}{3} = 20 \) and \( \dim V^{\otimes 3} = 4^3 = 64 \).

(d) No. It is a quotient of \( V^{\otimes 2} \), and its elements are cosets of \( C_2 \), not tensors. (Over a field of characteristic \( 0 \) there is a subspace of \( V^{\otimes 2} \) naturally isomorphic to it, namely the symmetric tensors, but the isomorphism is not an equality, and it does not exist in characteristic \( 2 \).)

(e) \( \operatorname{char} F = 0 \) or \( \operatorname{char} F > k \), so that \( k! \) is invertible in \( F \) (@thm-symmetric-tensors-vs-symmetric-power (b)). The step that needs it is the construction of the inverse map \( \theta \), which divides the symmetrization \( s = \sum_\sigma P_\sigma \) by \( k! \).
:::

### B. Practice

::: {#exr-symmetric-powers-b1}
[B1: Expanding symmetric products]

Let \( V = F^2 \).

::: {.enumerate options="label=(\alph*)"}
1. Expand \( (2\e_1 - \e_2)(\e_1 + 3\e_2) \) in the basis \( (\e_1^2, \e_1\e_2, \e_2^2) \) of \( \Sym^2 V \).
2. Expand \( (\e_1 + \e_2)(\e_1 - \e_2)\e_1 \) in the basis of \( \Sym^3 V \) given by @thm-symmetric-power-basis.
:::
:::

::: {.solution}
(a) Expanding one slot at a time and then using \( \e_2\e_1 = \e_1\e_2 \),
\[
(2\e_1 - \e_2)(\e_1 + 3\e_2)
= 2\e_1^2 + 6\e_1\e_2 - \e_1\e_2 - 3\e_2^2
= 2\e_1^2 + 5\e_1\e_2 - 3\e_2^2 .
\]

(b) The basis is \( (\e_1^3,\ \e_1^2\e_2,\ \e_1\e_2^2,\ \e_2^3) \), of size \( \binom{4}{3} = 4 \). Expanding the first two slots,
\[
(\e_1+\e_2)(\e_1-\e_2)\e_1
= \e_1^2\e_1 - \e_1\e_2\e_1 + \e_2\e_1\e_1 - \e_2^2\e_1 ,
\]
and the two middle terms are equal after sorting, so they cancel:
\[
(\e_1+\e_2)(\e_1-\e_2)\e_1 = \e_1^3 - \e_1\e_2^2 .
\]
In the polynomial language of @thm-symmetric-algebra-is-polynomials this is \( (x+y)(x-y)x = x^3 - xy^2 \).
:::

::: {#exr-symmetric-powers-b2}
[B2: Counting]

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \dim \Sym^k V \) for \( \dim V = 3 \) and \( k = 0, 1, 2, 3, 4 \).
2. For \( \dim V = n \), compute \( \dim \Sym^2 V \) in closed form and check it against the number of entries on or above the diagonal of an \( n \times n \) matrix.
3. Determine all pairs \( (n, k) \) with \( k \ge 1 \) for which \( \dim \Sym^k V = \dim V^{\otimes k} \). Justify your answer.
:::
:::

::: {.solution}
(a) \( \binom{k+2}{k} \) for \( n = 3 \), giving \( 1, 3, 6, 10, 15 \) for \( k = 0, 1, 2, 3, 4 \).

(b) \( \binom{n+1}{2} = n(n+1)/2 \). An \( n \times n \) matrix has \( n \) diagonal entries and \( (n^2-n)/2 \) entries strictly above the diagonal, and \( n + (n^2-n)/2 = n(n+1)/2 \). The agreement is the remark after @thm-symmetric-algebra-is-polynomials: a symmetric bilinear form is the same data as a functional on \( \Sym^2 V \), and also the same data as a symmetric matrix.

(c) Exactly those with \( n = 1 \), or with \( k = 1 \). If \( k = 1 \) both sides are \( n \). If \( n = 1 \) both sides are \( 1 \). Otherwise \( n \ge 2 \) and \( k \ge 2 \), and then \( \v_1\otimes\v_2 \ne \v_2\otimes\v_1 \) are two basis tensors with the same image, so \( C_k \ne \{\0\} \) and \( \dim\Sym^k V = n^k - \dim C_k < n^k \) by @thm-dimension-quotient.
:::

::: {#exr-symmetric-powers-b3}
[B3: A form factored through the symmetric square]

Let \( \beta \) be a symmetric bilinear form on \( V \). Prove that there is a unique linear functional \( \bar\beta \in (\Sym^2 V)^{*} \) with \( \bar\beta(\u\w) = \beta(\u, \w) \) for all \( \u, \w \in V \), and compute \( \bar\beta \) on the basis of @thm-symmetric-power-basis when \( V = F^2 \) and \( \beta(\x, \y) = x_1y_1 - x_2y_2 \).
:::

::: {.solution}
\( \beta \) is a symmetric \( 2 \)-linear map \( V^2 \to F \) (@def-symmetric-multilinear-map with \( k = 2 \), \( W = F \)), so (S1) gives exactly one linear \( \bar\beta \colon \Sym^2 V \to F \) with \( \bar\beta \circ \pi = \beta \), which is the displayed identity.

For the given \( \beta \): \( \bar\beta(\e_1^2) = \beta(\e_1, \e_1) = 1 \), \( \bar\beta(\e_1\e_2) = \beta(\e_1,\e_2) = 0 \) and \( \bar\beta(\e_2^2) = \beta(\e_2,\e_2) = -1 \). So in the coordinates given by the basis \( (\e_1^2, \e_1\e_2, \e_2^2) \) the functional reads \( (1, 0, -1) \), and under @thm-symmetric-algebra-is-polynomials it is the rule "read off the coefficients of \( x^2 \) and \( y^2 \) and subtract".
:::

### C. Going deeper

::: {#exr-symmetric-powers-c1}
[C1: The characteristic-two witness in full]

Let \( F = \nF_2 \) and \( V = \nF_2^2 \), and take \( k = 2 \).

::: {.enumerate options="label=(\alph*)"}
1. Write down a basis of \( (V^{\otimes 2})^{S_2} \) and verify that its dimension is \( 3 \).
2. Compute \( \dim C_2 \) and \( \dim\Sym^2 V \), and identify \( \ker\iota \) and \( \im\iota \) for the map \( \iota \) of @thm-symmetric-tensors-vs-symmetric-power.
3. Are \( (V^{\otimes 2})^{S_2} \) and \( \Sym^2 V \) isomorphic as vector spaces? Explain why this does not repair the situation.
:::
:::

::: {.solution}
(a) Here \( S_2 = \{\id, \sigma\} \) with \( \sigma \) the swap, and \( P_\sigma \) exchanges \( \e_1\otimes\e_2 \) with \( \e_2\otimes\e_1 \) and fixes \( \e_1\otimes\e_1 \) and \( \e_2\otimes\e_2 \). So \( x = a\,\e_1\otimes\e_1 + b\,\e_1\otimes\e_2 + c\,\e_2\otimes\e_1 + d\,\e_2\otimes\e_2 \) is symmetric if and only if \( b = c \). A basis is
\[
\e_1\otimes\e_1, \qquad \e_2\otimes\e_2, \qquad \e_1\otimes\e_2 + \e_2\otimes\e_1 ,
\]
the orbit sums of @thm-symmetric-tensors-vs-symmetric-power (a), so the dimension is \( 3 = \binom{3}{2} \).

(b) \( C_2 \) is spanned by the elements \( \u\otimes\w - \w\otimes\u \). Writing \( \u = a\e_1 + b\e_2 \) and \( \w = c\e_1 + d\e_2 \) and expanding both slots, the \( \e_1\otimes\e_1 \) and \( \e_2\otimes\e_2 \) terms cancel and
\[
\u\otimes\w - \w\otimes\u = (ad - bc)\bigl(\e_1\otimes\e_2 - \e_2\otimes\e_1\bigr).
\]
So \( C_2 \) is the line spanned by \( \e_1\otimes\e_2 + \e_2\otimes\e_1 \), the sign being irrelevant over \( \nF_2 \), and \( \dim C_2 = 1 \) and \( \dim\Sym^2 V = 4 - 1 = 3 \) by @thm-dimension-quotient. Now \( \ker\iota = (V^{\otimes 2})^{S_2} \cap C_2 = C_2 \), of dimension \( 1 \), and \( \im\iota \) is therefore \( 2 \)-dimensional, spanned by \( \e_1^2 \) and \( \e_2^2 \); it misses \( \e_1\e_2 \).

(c) Yes, they are isomorphic: both have dimension \( 3 \) over \( \nF_2 \), and @thm-isomorphic-iff-same-dimension applies. It does not repair anything, because the isomorphism is not \( \iota \) and does not respect the structure maps: an isomorphism chosen by hand would not satisfy \( \varphi(\u\otimes\w) = \u\w \), so it could not be used to transport statements about products of vectors. A construction is only as good as its universal property, and \( (V^{\otimes 2})^{S_2} \) has none here.
:::

::: {#exr-symmetric-powers-c2}
[C2: \( \Sym(V) \) is the free commutative algebra]

::: {.enumerate options="label=(\alph*)"}
1. Prove that the products \( \u_1\cdots\u_k \) with \( \u_i \in V \) span \( \Sym^k V \), and deduce that an algebra homomorphism out of \( \Sym(V) \) is determined by its restriction to \( V \).
2. Prove that for every **commutative** associative unital \( F \)-algebra \( A \) and every linear map \( f \colon V \to A \) there is a unique algebra homomorphism \( \bar f \colon \Sym(V) \to A \) with \( \bar f|_V = f \).
3. Explain in one sentence why (b) fails if the word "commutative" is deleted, and name the algebra that has the corresponding property for all \( A \).
:::
:::

::: {.solution}
(a) \( V^{\otimes k} \) is spanned by its simple tensors (@thm-tensor-power-exists) and \( q \) is surjective and linear, so their images, the products \( \u_1\cdots\u_k \), span \( \Sym^k V \). If \( \varphi, \psi \) are algebra homomorphisms agreeing on \( V \), then \( \varphi(\u_1\cdots\u_k) = \varphi(\u_1)\cdots\varphi(\u_k) = \psi(\u_1\cdots\u_k) \), and both send \( 1 \) to \( 1_A \); since these elements span \( \Sym(V) \) and both maps are linear, \( \varphi = \psi \).

(b) For \( k \ge 1 \) the map \( (\u_1, \dots, \u_k) \mapsto f(\u_1)\cdots f(\u_k) \) is \( k \)-linear, as in the proof of @thm-tensor-algebra-universal, and it is **symmetric** because \( A \) is commutative (the third example after @def-symmetric-multilinear-map). By (S1) it induces a linear \( \bar f_k \colon \Sym^k V \to A \); set \( \bar f_0(a) = a1_A \) and \( \bar f = \sum_k \bar f_k \) on the direct sum. Multiplicativity is checked on products of vectors, which span, exactly as in @thm-tensor-algebra-universal, and \( \bar f|_V = f \). Uniqueness is (a).

(c) It fails because \( \bar f \) would have to satisfy \( f(\u)f(\w) = \bar f(\u\w) = \bar f(\w\u) = f(\w)f(\u) \), so the images of \( V \) would be forced to commute, which need not happen in a non-commutative \( A \). The algebra with the property for **all** \( A \) is the tensor algebra \( \operatorname{T}(V) \), by @thm-tensor-algebra-universal.
:::

::: {#exr-symmetric-powers-c3}
[C3: One variable]

Let \( \dim V = 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( C_k = \{\0\} \) for every \( k \), and deduce that the quotient map \( \operatorname{T}(V) \to \Sym(V) \) assembled from the \( q \)'s is an isomorphism of algebras.
2. Hence deduce that \( \operatorname{T}(V) \cong \Sym(V) \cong F[x] \), and reconcile this with the fact that \( \operatorname{T}(V) \) is non-commutative for \( \dim V \ge 2 \).
:::
:::

::: {.solution}
(a) Write \( V = F\v \). By @thm-tensor-power-basis, \( V^{\otimes k} \) is spanned by \( \v^{\otimes k} \). A generator of \( C_k \) is \( \u_1\otimes\dots\otimes\u_k - \u_{\sigma(1)}\otimes\dots\otimes\u_{\sigma(k)} \); writing \( \u_t = c_t\v \) and expanding, both terms equal \( c_1c_2\cdots c_k\,\v^{\otimes k} \), since the scalars multiply in the same way whatever the order. So every generator is \( \0 \) and \( C_k = \{\0\} \). Hence each \( q \colon V^{\otimes k} \to \Sym^k V \) is an isomorphism (@thm-dimension-quotient, or directly: its kernel is \( C_k \)), and the assembled map is a bijective algebra homomorphism, so an isomorphism.

(b) By @exm-tensor-algebra-of-a-line, \( \operatorname{T}(V) \cong F[x] \), so (a) gives \( \Sym(V) \cong F[x] \) as well; the same conclusion comes from @thm-symmetric-algebra-is-polynomials with \( n = 1 \). There is no tension with non-commutativity: \( \operatorname{T}(V) \) is commutative precisely when \( \dim V \le 1 \), because non-commutativity needs two independent vectors to put in the two slots (the warning after @thm-tensor-algebra-is-an-algebra). With one variable there is nothing to reorder, so imposing the symmetry relations imposes nothing.
:::
