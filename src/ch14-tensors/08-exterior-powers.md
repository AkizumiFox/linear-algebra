# Exterior Powers

The symmetric power made the slots of a tensor interchangeable. This section makes them *hostile*: we divide \( V^{\otimes k} \) by a subspace chosen so that a tensor dies as soon as two of its slots hold the same vector. The result, the exterior power \( \Lambda^k V \), has a basis indexed by **strictly increasing** index tuples, so \( \dim \Lambda^k V = \binom{n}{k} \) and \( \Lambda^k V = \{\0\} \) once \( k \) exceeds \( n \). That collapse is the whole reason the determinant exists, and Section 09 will read the determinant off the top exterior power.

One choice in the construction is delicate, and it is the choice Chapter 13 prepared us for. There are two natural ways to say "the value flips when two slots are exchanged", and they are not the same condition: @thm-alternating-vs-skew showed that *alternating* implies *skew-symmetric* over every field, while the converse needs \( \operatorname{char} F \ne 2 \). We must therefore decide which relation to divide by, and the answer is the one that works over every field.

This is Section 02's method for the third time: universal property, uniqueness, then a model built as a quotient of the tensor power. Throughout, \( F \) is a field, \( V \) is a finite-dimensional vector space over \( F \) with \( n = \dim V \), and \( k \ge 1 \) unless stated otherwise. **No hypothesis on the characteristic is made anywhere in this section**, and the construction is arranged so that none is needed.

## Alternating multilinear maps

Chapter 6 defined alternating \( k \)-linear **forms**, valued in \( F \) (@def-alternating-form), because that is all the determinant needed. The target plays no role in the definition, so we extend it, as Section 01 extended multilinearity.

*An alternating map dies the moment two of its arguments coincide.*

::: {#def-alternating-multilinear-map}
[Alternating Multilinear Map]

Let \( W \) be a vector space over \( F \). A \( k \)-linear map \( f \colon V^k \to W \) (@def-multilinear-map) is **alternating** if
\[
f(\u_1, \dots, \u_k) = \0
\qquad\text{whenever } \u_i = \u_j \text{ for some pair of positions } i \ne j .
\]
:::

The condition is on **some** pair of positions, adjacent or not, and it says nothing about inputs whose entries are all distinct. For \( W = F \) this is @def-alternating-form verbatim. The examples of Chapter 6 are all available: the determinant \( \det(\a_1, \dots, \a_n) \) as a function of the columns; the signed area \( (\u, \w) \mapsto u_1w_2 - u_2w_1 \) on \( F^2 \); any linear functional, vacuously, at \( k = 1 \). A non-example by minimal change: the dot product on \( F^2 \) is bilinear but \( \e_1 \cdot \e_1 = 1 \ne 0 \), so the alternating clause fails at that one input while bilinearity survives.

Everything Chapter 6 deduced from the definition used only the vector-space structure of the target, so it carries over.

::: {#lem-alternating-map-properties}
[Properties of Alternating Maps]

Let \( f \colon V^k \to W \) be alternating \( k \)-linear, let \( \u_1, \dots, \u_k \in V \), and let \( \sigma \in S_k \).

::: {.enumerate options="label=(\alph*)"}
1. Exchanging two arguments multiplies the value by \( -1 \); in particular \( f \) is skew-symmetric.
2. \( f(\u_{\sigma(1)}, \dots, \u_{\sigma(k)}) = \sgn(\sigma)\, f(\u_1, \dots, \u_k) \).
3. If \( (\u_1, \dots, \u_k) \) is linearly dependent, then \( f(\u_1, \dots, \u_k) = \0 \).
:::
:::

::: {.proof}
(a) Fix positions \( i < j \), freeze the other arguments, and let \( g(\x, \y) \in W \) be the value of \( f \) with \( \x \) in position \( i \) and \( \y \) in position \( j \). Then \( g \) is bilinear and \( g(\x, \x) = \0 \), so expanding
\[
\0 = g(\u_i + \u_j, \u_i + \u_j) = g(\u_i, \u_j) + g(\u_j, \u_i)
\]
gives the swap rule. This is the computation of @thm-alternating-properties (a), which used nothing about \( F \) as a target beyond its being a vector space.

(b) For \( k = 1 \) the only permutation is the identity and there is nothing to prove. For \( k \ge 2 \), use @thm-transpositions-generate to write \( \sigma = \tau_1\cdots\tau_r \) as a product of transpositions. Applying (a) once per transposition multiplies the value by \( (-1)^r \), and \( (-1)^r = \sgn(\sigma) \) by @thm-sign-multiplicative and @cor-sign-transposition. This is @lem-alternating-permute-arguments, with the same proof.

(c) By the Linear Dependence Lemma (@thm-linear-dependence-lemma) some \( \u_j \) lies in \( \Span(\u_1, \dots, \u_{j-1}) \). Expanding \( f \) in slot \( j \) writes the value as a combination of values in which some \( \u_m \) with \( m < j \) sits both in slot \( m \) and in slot \( j \), and each such value is \( \0 \). This is @thm-alternating-properties (d). If \( j = 1 \) then \( \u_1 = \0 \) and linearity in slot \( 1 \) gives \( \0 \) at once.
:::

## Which relation to divide by

Now the delicate point, stated before the definition so that the definition looks inevitable. We want a quotient of \( V^{\otimes k} \) in which the image of \( \u_1 \otimes \dots \otimes \u_k \) vanishes exactly when it should. There are two candidate subspaces to divide by:
\[
\begin{aligned}
A_k &= \Span\{\, \u_1 \otimes \dots \otimes \u_k \ :\ \u_i = \u_j \text{ for some } i \ne j \,\}, \\
N_k &= \Span\{\, x + P_{\tau}x \ :\ x \text{ a simple tensor},\ \tau \text{ a transposition}\,\},
\end{aligned}
\]
where \( P_\tau \) permutes the slots as in @lem-slot-permutation. Dividing by \( A_k \) imposes "repeat a vector and you get zero"; dividing by \( N_k \) imposes "swap two slots and the sign flips". The two are not the same subspace.

::: {#prp-alternating-relation-contains-skew}
[The Repetition Relations Are the Stronger Ones]

For every field \( F \) and every \( k \ge 2 \) we have \( N_k \subseteq A_k \). If \( \operatorname{char} F \ne 2 \), then \( N_k = A_k \). If \( \operatorname{char} F = 2 \), \( k = 2 \) and \( n \ge 1 \), the inclusion is **strict**.
:::

::: {.idea}
For the inclusion, feed the sum \( \u_i + \u_j \) into **both** slots \( i \) and \( j \): the resulting tensor is in \( A_k \), and expanding it produces the two "square" terms, also in \( A_k \), plus the two cross terms, whose sum is therefore in \( A_k \) too. That is @thm-alternating-vs-skew (a) transcribed into tensors. For the reverse, a tensor with a repeat is its own swap, so \( x + P_\tau x = 2x \), and recovering \( x \) is a division by \( 2 \) — the same division, in the same place, as in @thm-alternating-vs-skew (b).
:::

::: {.proof}
\( (\subseteq) \) Let \( x = \u_1 \otimes \dots \otimes \u_k \) be simple and \( \tau \) the transposition of positions \( i < j \). Let \( y \) be the tensor obtained from \( x \) by putting \( \u_i + \u_j \) in **both** positions \( i \) and \( j \), which lies in \( A_k \) because those two slots now agree. Expanding \( y \) by multilinearity in those two slots gives four terms:
\[
y = \bigl[\u_i, \u_i\bigr] + \bigl[\u_i, \u_j\bigr] + \bigl[\u_j, \u_i\bigr] + \bigl[\u_j, \u_j\bigr],
\]
where \( [\p, \q] \) denotes \( x \) with \( \p \) in position \( i \) and \( \q \) in position \( j \). The first and last terms lie in \( A_k \), again by a repeat, and \( [\u_i, \u_j] = x \) while \( [\u_j, \u_i] = P_\tau x \). Hence \( x + P_\tau x = y - [\u_i,\u_i] - [\u_j,\u_j] \in A_k \). Generators of \( N_k \) lie in \( A_k \), so \( N_k \subseteq A_k \).

\( (\supseteq) \), assuming \( \operatorname{char} F \ne 2 \). Let \( x = \u_1 \otimes \dots \otimes \u_k \) with \( \u_i = \u_j \), \( i \ne j \), and let \( \tau \) swap \( i \) and \( j \). Then \( P_\tau x = x \), so \( x + P_\tau x = (1+1)x \) lies in \( N_k \). Since \( \operatorname{char} F \ne 2 \), the scalar \( 1 + 1 \) is invertible (@def-characteristic), so \( x \in N_k \). Generators of \( A_k \) lie in \( N_k \), so \( A_k \subseteq N_k \).

*Strictness in characteristic \( 2 \), \( k = 2 \).* Suppose \( \operatorname{char} F = 2 \) and \( n \ge 1 \), and fix a basis \( (\v_1, \dots, \v_n) \). Expand a generator of \( N_2 \) in the basis of @thm-tensor-power-basis: writing \( \u = \sum_i a_i\v_i \) and \( \w = \sum_j b_j\v_j \),
\[
\u\otimes\w + \w\otimes\u
= \sum_{i, j}(a_ib_j + a_jb_i)\,\v_i\otimes\v_j ,
\]
and the coefficient of a **diagonal** basis tensor \( \v_i\otimes\v_i \) is \( 2a_ib_i = 0 \). Every element of \( N_2 \) therefore has coefficient \( 0 \) on \( \v_1\otimes\v_1 \). But \( \v_1\otimes\v_1 \) is itself a generator of \( A_2 \), and it is a basis vector of \( V^{\otimes 2} \), hence non-zero. So \( \v_1\otimes\v_1 \in A_2 \setminus N_2 \) and the inclusion is strict. This proves the proposition.
:::

So the two relations differ, and we must choose. **We divide by \( A_k \).** Three reasons, and they are the same three that made Chapter 6 build the determinant on alternation rather than skewness:

- The quotient by \( A_k \) is the object whose maps are the **alternating** ones, and alternating is the condition the determinant satisfies over every field.
- \( A_k \) is the larger subspace, so the quotient by it is the smaller space; and by @prp-alternating-relation-contains-skew the two quotients agree whenever \( \operatorname{char} F \ne 2 \). So nothing is lost outside characteristic \( 2 \), and something is gained inside it.
- The dimension \( \binom{n}{k} \) comes out right over every field. Dividing by \( N_2 \) instead would give, for \( V = \nF_2^2 \), a space of dimension \( 3 \) where \( \binom{2}{2} = 1 \) is wanted; Exercise C1 carries out that count.

## The exterior power

*The \( k \)-th exterior power is the space in which alternating \( k \)-linear maps become linear.*

::: {#def-exterior-power}
[\( k \)-th Exterior Power]

A **\( k \)-th exterior power of \( V \)** is a pair \( (P, \wedge) \), where \( P \) is a vector space over \( F \) and \( \wedge \colon V^k \to P \) is an **alternating** \( k \)-linear map, such that

::: {.enumerate options="label=(E\arabic*)"}
1. (**universal property**) for **every** vector space \( W \) over \( F \) and **every alternating** \( k \)-linear map \( f \colon V^k \to W \), there is a **unique** linear map \( \bar f \colon P \to W \) with \( \bar f \circ \wedge = f \).
:::

We write \( \Lambda^k V \) for \( P \) and
\[
\v_1 \wedge \v_2 \wedge \dots \wedge \v_k \coloneqq \wedge(\v_1, \dots, \v_k),
\]
calling it a **wedge** of the list. By convention \( \Lambda^0 V = F \).
:::

Clause by clause, and the small words matter. The structure map \( \wedge \) must itself be **alternating**, which is what makes \( \v \wedge \v = \0 \) a fact rather than a wish. Only **alternating** maps are required to factor, and that is forced: \( \bar f \circ \wedge \) is alternating for every linear \( \bar f \), so no space could linearize a non-alternating map. **Unique** does the usual two jobs: existence of \( \bar f \) says \( \Lambda^k V \) is large enough, uniqueness says it is no larger.

At \( k = 1 \) the condition is vacuous and \( (V, \id_V) \) works, so \( \Lambda^1 V = V \). At \( k = 0 \) the convention \( \Lambda^0 V = F \) is the one that makes \( \binom{n}{k} \) correct at \( k = 0 \), where it reads \( \binom{n}{0} = 1 \).

::: {#thm-exterior-power-unique}
[Uniqueness of the Exterior Power]

Let \( (P, \wedge) \) and \( (P', \wedge') \) both be \( k \)-th exterior powers of \( V \). Then there is a unique linear isomorphism \( \varphi \colon P \to P' \) with \( \varphi \circ \wedge = \wedge' \).
:::

::: {.proof}
The proof of @thm-tensor-power-unique, with "alternating \( k \)-linear" in place of "\( k \)-linear": (E1) for \( P \) applied to \( \wedge' \) gives \( \varphi \), (E1) for \( P' \) applied to \( \wedge \) gives \( \psi \), and \( \psi\varphi \) is a linear self-map of \( P \) with \( \psi\varphi\wedge = \wedge \), so the uniqueness clause of (E1) applied to \( \wedge \) forces \( \psi\varphi = \id_P \); symmetrically \( \varphi\psi = \id_{P'} \). This proves the theorem.
:::

::: {#thm-exterior-power-exists}
[Existence of the Exterior Power]

Let \( A_k \subseteq V^{\otimes k} \) be as above and let \( q \colon V^{\otimes k} \to V^{\otimes k}/A_k \) be the quotient map (@def-quotient-space). Then \( V^{\otimes k}/A_k \), together with
\[
\v_1 \wedge \dots \wedge \v_k = q(\v_1 \otimes \dots \otimes \v_k),
\]
is a \( k \)-th exterior power of \( V \).
:::

::: {.proof}
\( A_k \) is a subspace, being a span, and \( \wedge \) is \( k \)-linear, being \( \mu_k \) followed by the linear map \( q \). It is alternating: if \( \u_i = \u_j \) with \( i \ne j \), then \( \u_1 \otimes \dots \otimes \u_k \) is by definition a generator of \( A_k \), so its image under \( q \) is \( \0 \).

Let \( f \colon V^k \to W \) be alternating \( k \)-linear. By (T1) there is a unique linear \( \tilde f \colon V^{\otimes k} \to W \) with \( \tilde f(\u_1\otimes\dots\otimes\u_k) = f(\u_1, \dots, \u_k) \). On a generator of \( A_k \), that is, on a simple tensor with \( \u_i = \u_j \) for some \( i \ne j \), the value is \( f(\u_1, \dots, \u_k) = \0 \) because \( f \) is alternating. A linear map vanishing on a spanning set of \( A_k \) vanishes on \( A_k \), so \( A_k \subseteq \ker \tilde f \), and @thm-quotient-universal-property (a) gives exactly one linear \( \bar f \) on the quotient with \( \bar f \circ q = \tilde f \), whence \( \bar f \circ \wedge = f \).

Uniqueness: \( q \) is surjective and \( V^{\otimes k} \) is spanned by its simple tensors (@thm-tensor-power-exists), so the wedges \( \u_1 \wedge \dots \wedge \u_k \) span \( V^{\otimes k}/A_k \), and two linear maps agreeing on them agree everywhere. This proves the theorem.
:::

From @lem-alternating-map-properties applied to the alternating map \( \wedge \) itself we get the rules used in every computation below, for all \( \u_i \in V \) and \( \sigma \in S_k \):
\[
\begin{aligned}
\u_{\sigma(1)} \wedge \dots \wedge \u_{\sigma(k)}
&= \sgn(\sigma)\ \u_1 \wedge \dots \wedge \u_k , \\
\u_1 \wedge \dots \wedge \u_k &= \0
\quad\text{if the list is dependent.}
\end{aligned}
\]

Four instances, smallest first, and one look-alike that is not one.

- **One slot.** \( \Lambda^1 V = V \), and the wedge of a single vector is the vector itself. The alternating condition asks about pairs of positions, and with one position there are none.
- **The plane.** For \( V = F^2 \), expanding both slots and canceling the two repeats gives \( \u \wedge \w = (u_1w_2 - u_2w_1)\,\e_1\wedge\e_2 \). The coefficient is the signed area of Chapter 6 §01; the wedge is that number, moved out of \( F \) and into a line inside \( \Lambda^2 V \).
- **Polynomials.** On \( V = F[x]_{\le 2} \) with basis \( (1, x, x^2) \), the same expansion gives \( (1 + x) \wedge (x + x^2) = 1\wedge x + 1\wedge x^2 + x\wedge x^2 \), the term \( x \wedge x \) having died.
- **A degenerate case.** If \( V = \{\0\} \) then every wedge of \( k \ge 1 \) vectors is \( \0 \), so \( \Lambda^k V = \{\0\} \). It matters because it is the base of the count below: \( \binom{0}{k} = 0 \) for \( k \ge 1 \).
- **Not an example: the symmetric product.** In \( \Sym^2 V \) the product \( \u\w \) is bilinear and satisfies \( \u\w = \w\u \), but \( \e_1\e_1 \ne 0 \) by @thm-symmetric-power-basis, so the symmetric product map is **not** alternating. Exactly one clause differs between the two constructions, and it is this one.

::: {.warning}
**The relation is \( \v \wedge \v = \0 \), not \( \u\wedge\w = -\w\wedge\u \).** The second follows from the first (@lem-alternating-map-properties (a)), but not conversely: over \( \nF_2 \) the two say different things, since \( -1 = 1 \) there makes "\( \u\wedge\w = -\w\wedge\u \)" mean "\( \u\wedge\w = \w\wedge\u \)", which is no condition at all on a repeated slot. This is exactly @thm-alternating-vs-skew, transcribed from forms to tensors by @prp-alternating-relation-contains-skew, and it is why the construction above divides by \( A_k \). A reader who remembers that theorem should recognize the choice as the only characteristic-free one.
:::

::: {.check}
In \( \Lambda^2 V \), simplify \( (\u + \w) \wedge (\u - \w) \).
:::

::: {.solution}
Expand both slots: \( \u\wedge\u - \u\wedge\w + \w\wedge\u - \w\wedge\w \). The first and last terms are \( \0 \) because \( \wedge \) is alternating, and \( \w\wedge\u = -\u\wedge\w \) by @lem-alternating-map-properties (a). So the value is \( -2\,\u\wedge\w \). Over \( \nF_2 \) that is \( \0 \), which is correct there and not a sign of anything going wrong: over \( \nF_2 \), \( \u + \w \) and \( \u - \w \) are the same vector, so the wedge of the pair must vanish.
:::

## A basis, and the dimension

Sorting is again the move, but now it costs a sign, and tuples with a repeat are simply gone. What survives is the strictly increasing tuples.

::: {#thm-exterior-power-basis}
[Basis of an Exterior Power]

Let \( \sB = (\v_1, \dots, \v_n) \) be a basis of \( V \) and \( k \ge 1 \). Then the wedges
\[
\v_{i_1} \wedge \v_{i_2} \wedge \dots \wedge \v_{i_k},
\qquad 1 \le i_1 < i_2 < \dots < i_k \le n ,
\]
one for each **strictly increasing** tuple, form a basis of \( \Lambda^k V \). Consequently
\[
\dim \Lambda^k V = \binom{n}{k},
\qquad\text{and}\qquad
\Lambda^k V = \{\0\} \ \text{ for } k > n ,
\]
over **every** field \( F \).
:::

::: {.idea}
Spanning: start from the basis of @thm-tensor-power-basis, throw away every tuple with a repeated index — those wedges are \( \0 \) — and sort the rest, paying a sign. Independence: one linear functional per increasing tuple \( I \), and the functional must be **alternating**, so the natural candidate is a determinant: read the \( k \) arguments through the \( k \) dual functionals \( \varphi_{i_1}, \dots, \varphi_{i_k} \), assemble the \( k \times k \) matrix of values, and take its determinant. Determinants are alternating in their columns by construction, which is exactly what is needed, and the value at the basis wedge indexed by \( J \) is \( \det \I_k = 1 \) if \( I = J \) and \( 0 \) otherwise, because some row is then zero.
:::

::: {.proof}
*Spanning.* By @thm-tensor-power-basis the tensors \( \v_{j_1}\otimes\dots\otimes\v_{j_k} \), over all tuples \( J \), form a basis of \( V^{\otimes k} \), and \( q \) is surjective, so the wedges \( \v_{j_1}\wedge\dots\wedge\v_{j_k} \) span \( \Lambda^k V \). If \( J \) has two equal entries, the corresponding wedge is \( \0 \) because \( \wedge \) is alternating. If the entries of \( J \) are distinct, let \( \sigma \in S_k \) sort them into increasing order; then by @lem-alternating-map-properties (b) the wedge equals \( \pm \) the wedge of the sorted tuple. So the increasing tuples already span, and if \( k > n \) there are no such tuples at all, whence \( \Lambda^k V = \{\0\} \).

*Independence.* Let \( (\varphi_1, \dots, \varphi_n) \) be the dual basis of \( \sB \) (@thm-dual-basis). For an increasing tuple \( I = (i_1 < \dots < i_k) \) define
\[
g_I(\u_1, \dots, \u_k) = \det\Bigl(\varphi_{i_a}(\u_b)\Bigr)_{a, b = 1}^{k} \in F,
\]
the determinant of the \( k \times k \) matrix whose \( (a, b) \) entry is \( \varphi_{i_a}(\u_b) \). Column \( b \) of that matrix depends linearly on \( \u_b \), because each \( \varphi_{i_a} \) is linear, and \( \det \) is linear in each column and vanishes when two columns coincide (@thm-leibniz-formula-alternating). Hence \( g_I \) is \( k \)-linear, and alternating: if \( \u_a = \u_b \) with \( a \ne b \), two columns of the matrix are equal and the determinant is \( 0 \).

By (E1), \( g_I \) induces a linear \( \bar g_I \colon \Lambda^k V \to F \). Evaluate it at the wedge of an increasing tuple \( J \): the matrix has \( (a, b) \) entry \( \varphi_{i_a}(\v_{j_b}) = \delta_{i_a j_b} \). If \( I = J \) this matrix is \( \I_k \) and the determinant is \( 1 \). If \( I \ne J \), then since \( I \) and \( J \) each list \( k \) distinct indices and are not the same increasing tuple, some \( i_a \) is not among \( j_1, \dots, j_k \); row \( a \) is then zero, so the rows are dependent, and by @thm-det-transpose together with @thm-alternating-properties (d) the determinant is \( 0 \). Hence \( \bar g_I(\v_{j_1}\wedge\dots\wedge\v_{j_k}) = \delta_{IJ} \).

Now let \( \sum_I a_I\, \v_{i_1}\wedge\dots\wedge\v_{i_k} = \0 \), the sum over increasing tuples. Applying \( \bar g_J \) leaves \( a_J = 0 \), and \( J \) was arbitrary. So the list is independent, hence a basis.

*The count.* An increasing \( k \)-tuple in \( \{1, \dots, n\} \) is the same thing as a \( k \)-element subset of \( \{1, \dots, n\} \), listed in its only increasing order. There are \( \binom{n}{k} \) such subsets, and none at all when \( k > n \). No step divided by an integer, so the conclusion holds over every field. This proves the theorem.
:::

::: {#cor-top-exterior-power-is-a-line}
[The Top Exterior Power Is a Line]

If \( \dim V = n \ge 1 \), then \( \dim \Lambda^n V = 1 \), with basis the single wedge \( \v_1 \wedge \dots \wedge \v_n \) of any basis of \( V \). For \( k > n \), \( \Lambda^k V = \{\0\} \).
:::

::: {.proof}
There is exactly one increasing \( n \)-tuple in \( \{1, \dots, n\} \), namely \( (1, 2, \dots, n) \), so @thm-exterior-power-basis gives a basis with one member, and \( \binom{n}{n} = 1 \). The second statement is the last clause of that theorem.
:::

That one-dimensionality is the source of the determinant, and Section 09 is about it. For now, notice the shape of the numbers: \( \dim \Lambda^k V \) rises from \( 1 \) at \( k = 0 \) to a maximum in the middle and back to \( 1 \) at \( k = n \), and then stops. Compare \( \dim \Sym^k V = \binom{n+k-1}{k} \), which grows forever. The symmetric power forgets the order; the exterior power forgets the order **and** forbids repetition, and forbidding repetition is what makes the tower finite.

::: {.remark}
The two counts fit together at \( k = 2 \): \( \binom{n+1}{2} + \binom{n}{2} = n^2 = \dim V^{\otimes 2} \) over every field. In characteristic \( \ne 2 \) this reflects an actual decomposition of \( V^{\otimes 2} \) into symmetric and alternating tensors, in the manner of @thm-symmetric-alternating-decomposition. Over \( \nF_2 \) the identity between the numbers survives while the decomposition does not, exactly as in @thm-symmetric-tensors-vs-symmetric-power.
:::

::: {.warning}
**\( \Lambda^k V \) is a quotient of \( V^{\otimes k} \), not a subspace.** Its elements are cosets of \( A_k \), and \( \u\wedge\w = -\w\wedge\u \) is an identity between cosets, not between tensors. It is also a mistake to replace it by a subspace of \( V^{\otimes k} \) — say "the tensors that change sign under every swap of two slots". Over \( \nF_2 \) that subspace is the space of symmetric tensors of @def-symmetric-tensor, because \( -1 = 1 \) there; for \( V = \nF_2^2 \) and \( k = 2 \) it has dimension \( \binom{3}{2} = 3 \) by @thm-symmetric-tensors-vs-symmetric-power (a), while \( \Lambda^2 V \) has dimension \( \binom{2}{2} = 1 \).
:::

::: {#exm-wedge-in-three-space}
[A wedge in \( \Lambda^2(F^3) \)]

Let \( V = F^3 \), \( \u = \e_1 + 2\e_2 + 3\e_3 \) and \( \w = 4\e_1 + 5\e_2 + 6\e_3 \). Write out a basis of \( \Lambda^2 V \) and expand \( \u \wedge \w \) in it.
:::

::: {.solution}
By @thm-exterior-power-basis a basis is \( (\e_1\wedge\e_2,\ \e_1\wedge\e_3,\ \e_2\wedge\e_3) \), of size \( \binom{3}{2} = 3 \). Expanding both slots gives nine terms; the three with a repeated index vanish, and each remaining pair combines by \( \e_j\wedge\e_i = -\e_i\wedge\e_j \). The coefficient of \( \e_i\wedge\e_j \) is therefore \( u_iw_j - u_jw_i \):
\[
\begin{aligned}
\u \wedge \w = {}& (1\cdot 5 - 2\cdot 4)\,\e_1\wedge\e_2 + (1\cdot 6 - 3\cdot 4)\,\e_1\wedge\e_3 \\
&+ (2\cdot 6 - 3\cdot 5)\,\e_2\wedge\e_3 \\
={}& -3\,\e_1\wedge\e_2 - 6\,\e_1\wedge\e_3 - 3\,\e_2\wedge\e_3 .
\end{aligned}
\]
The three coefficients are the \( 2\times 2 \) minors of the \( 3 \times 2 \) matrix with columns \( \u \) and \( \w \). That is not an accident, and Section 09 proves it in general.
:::

## Independence detects wedges

The last result of the section is small to state and is the tool everything after it uses: **a wedge is non-zero exactly when its factors are independent.** One direction is @lem-alternating-map-properties (c); the other needs @thm-exterior-power-basis, which is why it comes last.

::: {#thm-wedge-nonzero-iff-independent}
[Wedges Detect Independence]

Let \( \u_1, \dots, \u_k \in V \) with \( 1 \le k \le n \). Then
\[
\begin{aligned}
&\u_1 \wedge \u_2 \wedge \dots \wedge \u_k \ne \0 \\
&\qquad\text{if and only if } (\u_1, \dots, \u_k) \text{ is independent.}
\end{aligned}
\]
For \( k > n \) the wedge is always \( \0 \).
:::

::: {.idea}
\( (\Rightarrow) \) is the contrapositive of "alternating maps kill dependent lists". \( (\Leftarrow) \) is the reason @thm-exterior-power-basis was worth proving: an independent list extends to a basis of \( V \), and that theorem then says its wedge **is** one of the basis vectors of \( \Lambda^k V \), hence non-zero.
:::

::: {.proof}
\( (\Rightarrow) \) We prove the contrapositive. If \( (\u_1, \dots, \u_k) \) is dependent, then \( \u_1\wedge\dots\wedge\u_k = \0 \) by @lem-alternating-map-properties (c), applied to the alternating map \( \wedge \).

\( (\Leftarrow) \) Suppose the list is independent. By the Basis Extension Theorem (@thm-basis-extension) it extends to a basis \( \sB = (\u_1, \dots, \u_k, \u_{k+1}, \dots, \u_n) \) of \( V \), which is possible because \( k \le n \). Apply @thm-exterior-power-basis to \( \sB \): the wedges indexed by increasing \( k \)-tuples form a basis of \( \Lambda^k V \), and \( \u_1\wedge\dots\wedge\u_k \) is the one indexed by \( (1, 2, \dots, k) \). A member of a basis is non-zero, so \( \u_1\wedge\dots\wedge\u_k \ne \0 \).

For \( k > n \), \( \Lambda^k V = \{\0\} \) by @thm-exterior-power-basis, so every wedge vanishes; consistently, any \( k > n \) vectors in \( V \) are dependent. This proves the theorem.
:::

::: {.remark}
The theorem turns a question about a list into a question about a single vector, and that is its value. Section 09 uses it to prove that \( \Lambda^n T \) is multiplication by \( \det T \) and that \( T \) is invertible exactly when that scalar is non-zero; Section 10 uses it to decide which elements of \( \Lambda^2 V \) are wedges at all. Note the hypothesis it does **not** need: no assumption on \( F \), because neither half divided by anything.
:::

## Exercises

### A. Check your understanding

::: {#exr-exterior-powers-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the universal property (E1), with every quantifier, and say which maps are required to factor.
2. Which subspace of \( V^{\otimes k} \) is divided out, and why is the other candidate \( N_k \) rejected?
3. Let \( \dim V = 5 \). Compute \( \dim\Lambda^k V \) for \( k = 0, 1, 2, 3, 4, 5, 6 \).
4. Determine whether \( \u\wedge\w\wedge\u \) can be non-zero. Justify your answer.
5. State the test for \( \u_1\wedge\dots\wedge\u_k \ne \0 \), and say which hypothesis on the field it needs.
:::
:::

::: {.solution}
(a) For every vector space \( W \) over \( F \) and every **alternating** \( k \)-linear map \( f \colon V^k \to W \), there exists exactly one linear \( \bar f \colon \Lambda^k V \to W \) with \( \bar f \circ \wedge = f \). Only alternating maps factor; a non-alternating one cannot, since \( \bar f \circ \wedge \) is alternating for every linear \( \bar f \).

(b) The subspace \( A_k \) spanned by the simple tensors with a repeated entry (@thm-exterior-power-exists). The candidate \( N_k \), spanned by the elements \( x + P_\tau x \), is rejected because \( N_k \subsetneq A_k \) in characteristic \( 2 \) (@prp-alternating-relation-contains-skew), so the quotient by \( N_k \) would have the wrong dimension there and its maps would be the skew-symmetric ones rather than the alternating ones.

(c) \( \binom{5}{k} \), giving \( 1, 5, 10, 10, 5, 1, 0 \) for \( k = 0, \dots, 6 \).

(d) No: the list \( (\u, \w, \u) \) repeats \( \u \) in positions \( 1 \) and \( 3 \), so the wedge is \( \0 \) because \( \wedge \) is alternating. (Equivalently, the list is dependent, so @thm-wedge-nonzero-iff-independent applies.)

(e) \( \u_1\wedge\dots\wedge\u_k \ne \0 \) if and only if the list is linearly independent (@thm-wedge-nonzero-iff-independent). It needs no hypothesis on \( F \).
:::

### B. Practice

::: {#exr-exterior-powers-b1}
[B1: Computing wedges]

Let \( V = F^3 \) with \( F = \nQ \).

::: {.enumerate options="label=(\alph*)"}
1. Expand \( (2\e_1 - \e_2 + \e_3)\wedge(\e_1 + \e_2 - \e_3) \) in the basis \( (\e_1\wedge\e_2, \e_1\wedge\e_3, \e_2\wedge\e_3) \).
2. Expand \( \e_1 \wedge (\e_1 + \e_2) \wedge (\e_1 + \e_2 + \e_3) \) in the basis of \( \Lambda^3 V \).
:::
:::

::: {.solution}
(a) With \( \u = (2, -1, 1) \) and \( \w = (1, 1, -1) \), the coefficient of \( \e_i\wedge\e_j \) is \( u_iw_j - u_jw_i \), as in @exm-wedge-in-three-space:
\[
\begin{aligned}
&2\cdot 1 - (-1)\cdot 1 = 3, \qquad
2\cdot(-1) - 1\cdot 1 = -3, \\
&(-1)\cdot(-1) - 1\cdot 1 = 0 ,
\end{aligned}
\]
so the wedge is \( 3\,\e_1\wedge\e_2 - 3\,\e_1\wedge\e_3 \).

(b) By @cor-top-exterior-power-is-a-line the basis is the single wedge \( \e_1\wedge\e_2\wedge\e_3 \). Expand from the left: in the second slot, \( \e_1 \wedge \e_1 \wedge \cdots = \0 \), so only \( \e_2 \) survives; then in the third slot, both \( \e_1 \) and \( \e_2 \) already occur, so only \( \e_3 \) survives. Hence the wedge is \( \e_1\wedge\e_2\wedge\e_3 \). (Equivalently, the three vectors are the columns of a unit upper triangular matrix, of determinant \( 1 \); Exercise C3 explains why the answer had to be that determinant.)
:::

::: {#exr-exterior-powers-b2}
[B2: Independence by wedging]

Determine whether each list is linearly independent, by computing a wedge. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \bigl((1, 2), (3, 6)\bigr) \) in \( \nQ^2 \).
2. \( \bigl((1, 0, 1), (0, 1, 1), (1, 1, 2)\bigr) \) in \( \nQ^3 \).
3. \( \bigl((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)\bigr) \) in \( \nQ^3 \).
:::
:::

::: {.solution}
(a) \( (1,2)\wedge(3,6) = (1\cdot 6 - 2\cdot 3)\,\e_1\wedge\e_2 = \0 \). By @thm-wedge-nonzero-iff-independent the list is dependent, as it visibly is: the second vector is three times the first.

(b) The minor computation \( (1\cdot 1 - 0\cdot 0,\ 1\cdot 1 - 1\cdot 0,\ 0\cdot 1 - 1\cdot 1) = (1, 1, -1) \) gives, for the first two vectors, \( \e_1\wedge\e_2 + \e_1\wedge\e_3 - \e_2\wedge\e_3 \). Wedging with the third vector \( (1,1,2) \) and keeping only the terms with all three indices distinct,
\[
\begin{aligned}
&\bigl(\e_1\wedge\e_2\bigr)\wedge 2\e_3 + \bigl(\e_1\wedge\e_3\bigr)\wedge\e_2
- \bigl(\e_2\wedge\e_3\bigr)\wedge\e_1 \\
&\qquad = (2 - 1 - 1)\,\e_1\wedge\e_2\wedge\e_3 = \0 ,
\end{aligned}
\]
using \( \e_1\wedge\e_3\wedge\e_2 = -\e_1\wedge\e_2\wedge\e_3 \) and \( \e_2\wedge\e_3\wedge\e_1 = \e_1\wedge\e_2\wedge\e_3 \) from @lem-alternating-map-properties (b). So the list is dependent; indeed the third vector is the sum of the first two.

(c) Here \( k = 4 > 3 = n \), so \( \Lambda^4(\nQ^3) = \{\0\} \) by @thm-exterior-power-basis and the wedge is \( \0 \) without any computation. The list is dependent, as any \( 4 \) vectors in a \( 3 \)-dimensional space must be.
:::

::: {#exr-exterior-powers-b3}
[B3: A functional built from the universal property]

Let \( V = F^3 \) and let \( f \colon V^2 \to F \) be \( f(\u, \w) = u_1w_3 - u_3w_1 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( f \) is alternating and bilinear, and deduce that there is a unique linear \( \bar f \colon \Lambda^2 V \to F \) with \( \bar f(\u\wedge\w) = f(\u, \w) \).
2. Compute \( \bar f \) on the basis \( (\e_1\wedge\e_2, \e_1\wedge\e_3, \e_2\wedge\e_3) \), and evaluate \( \bar f \) on the answer to @exm-wedge-in-three-space.
:::
:::

::: {.solution}
(a) Each slot is a linear functional with the other fixed, so \( f \) is bilinear, and \( f(\u, \u) = u_1u_3 - u_3u_1 = 0 \), so \( f \) is alternating (@def-alternating-multilinear-map with \( k = 2 \)). By (E1) there is exactly one linear \( \bar f \colon \Lambda^2 V \to F \) with \( \bar f \circ \wedge = f \).

(b) \( \bar f(\e_1\wedge\e_2) = f(\e_1, \e_2) = 0 \); \( \bar f(\e_1\wedge\e_3) = 1 \); \( \bar f(\e_2\wedge\e_3) = 0 \). So \( \bar f \) reads off the \( \e_1\wedge\e_3 \) coordinate. On \( \u\wedge\w = -3\e_1\wedge\e_2 - 6\e_1\wedge\e_3 - 3\e_2\wedge\e_3 \) it gives \( -6 \), which agrees with \( f(\u, \w) = 1\cdot 6 - 3\cdot 4 = -6 \).
:::

### C. Going deeper

::: {#exr-exterior-powers-c1}
[C1: The characteristic-two witness]

Let \( F = \nF_2 \), \( V = \nF_2^2 \) and \( k = 2 \).

::: {.enumerate options="label=(\alph*)"}
1. List the elements of \( A_2 \) and of \( N_2 \), and compute both dimensions.
2. Compute \( \dim\Lambda^2 V \) from (a) and check it against @thm-exterior-power-basis.
3. Compute \( \dim(V^{\otimes 2}/N_2) \) and explain, in one sentence, what would go wrong if the exterior power had been defined as that quotient.
:::
:::

::: {.solution}
(a) By @thm-tensor-power-basis, \( V^{\otimes 2} \) has basis \( \e_1\otimes\e_1, \e_1\otimes\e_2, \e_2\otimes\e_1, \e_2\otimes\e_2 \). Now \( A_2 \) is spanned by the tensors \( \u\otimes\u \), and the three choices \( \u = \e_1, \e_2, \e_1+\e_2 \) give
\[
\e_1\otimes\e_1, \quad \e_2\otimes\e_2, \quad
\e_1\otimes\e_1 + \e_1\otimes\e_2 + \e_2\otimes\e_1 + \e_2\otimes\e_2 ,
\]
whose span also contains \( t = \e_1\otimes\e_2 + \e_2\otimes\e_1 \). Those three vectors \( \e_1\otimes\e_1, \e_2\otimes\e_2, t \) are independent, being distinct disjoint sums of basis vectors, and they span all three listed generators, so \( \dim A_2 = 3 \); there are no further generators, since \( \0 \) is the only remaining vector of \( \nF_2^2 \). For \( N_2 \), the coefficient formula in the proof of @prp-alternating-relation-contains-skew gives
\[
\u\otimes\w + \w\otimes\u = (a_1b_2 + a_2b_1)\,t ,
\]
since the diagonal coefficients vanish and the two off-diagonal ones are equal. Hence \( N_2 = \Span(t) \) and \( \dim N_2 = 1 \).

(b) \( \dim\Lambda^2 V = 4 - 3 = 1 \) by @thm-dimension-quotient, matching \( \binom{2}{2} = 1 \).

(c) \( \dim(V^{\otimes 2}/N_2) = 4 - 1 = 3 \). Defining \( \Lambda^2 V \) as that quotient would make the image of \( \e_1\otimes\e_1 \) non-zero, so \( \v\wedge\v \ne \0 \) for some \( \v \), the structure map would be skew-symmetric but not alternating, and the dimension would be \( 3 \) instead of \( \binom{2}{2} = 1 \).
:::

::: {#exr-exterior-powers-c2}
[C2: Alternating forms, recounted]

::: {.enumerate options="label=(\alph*)"}
1. Prove that the alternating \( k \)-linear forms on \( V \) are in bijection with the linear functionals on \( \Lambda^k V \), and that the bijection is an isomorphism of vector spaces.
2. Deduce that the space of alternating \( k \)-linear forms on \( V \) has dimension \( \binom{n}{k} \).
3. Hence recover @cor-alternating-forms-one-dimensional: the alternating \( n \)-linear forms on \( F^n \) form a line.
:::
:::

::: {.solution}
(a) Write \( \cA \) for the space of alternating \( k \)-linear forms on \( V \), a vector space by @thm-alternating-forms-space. The map \( \Theta \colon (\Lambda^k V)^{*} \to \cA \), \( \Theta(\lambda) = \lambda \circ \wedge \), is well defined, since a composite of the alternating \( \wedge \) with a linear map is alternating and \( k \)-linear, and it is linear in \( \lambda \) because composition with a fixed map is. It is injective: if \( \lambda\circ\wedge = 0 \) then \( \lambda \) vanishes on the wedges, which span \( \Lambda^k V \) (@thm-exterior-power-exists), so \( \lambda = 0 \). It is surjective: given \( f \in \cA \), (E1) supplies \( \bar f \) with \( \bar f\circ\wedge = f \). So \( \Theta \) is an isomorphism.

(b) By (a) and @cor-dimension-dual-space, \( \dim\cA = \dim(\Lambda^k V)^{*} = \dim\Lambda^k V = \binom{n}{k} \), using @thm-exterior-power-basis.

(c) Take \( V = F^n \) and \( k = n \): the dimension is \( \binom{n}{n} = 1 \). Since \( \det \) is a non-zero alternating \( n \)-linear form (@thm-leibniz-formula-alternating, with \( \det \I_n = 1 \)), it spans that line, which is @cor-alternating-forms-one-dimensional.
:::

::: {#exr-exterior-powers-c3}
[C3: A wedge sees only the subspace]

Let \( (\u_1, \dots, \u_k) \) and \( (\w_1, \dots, \w_k) \) be two lists in \( V \) with \( \w_b = \sum_{a=1}^{k} p_{ab}\,\u_a \) for a matrix \( \P = (p_{ab}) \in M_k(F) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \w_1\wedge\dots\wedge\w_k = (\det\P)\; \u_1\wedge\dots\wedge\u_k \).
2. Deduce that if \( (\u_1, \dots, \u_k) \) and \( (\w_1, \dots, \w_k) \) are two bases of the **same** \( k \)-dimensional subspace \( U \subseteq V \), then their wedges differ by a non-zero scalar factor.
3. Deduce that the line \( \Span(\u_1\wedge\dots\wedge\u_k) \subseteq \Lambda^k V \) depends only on \( U \), not on the basis chosen for it.
:::

*Hint: for (a), expand every slot and use @lem-alternating-map-properties (b) together with @def-determinant.*
:::

::: {.solution}
(a) Expanding slot by slot,
\[
\w_1\wedge\dots\wedge\w_k
= \sum_{a_1, \dots, a_k} p_{a_1 1}\cdots p_{a_k k}\;
\u_{a_1}\wedge\dots\wedge\u_{a_k},
\]
the sum over all \( k \)-tuples \( (a_1, \dots, a_k) \) from \( \{1, \dots, k\} \). A term with two equal indices has a repeated argument, so its wedge is \( \0 \). A term with all indices distinct has \( (a_1, \dots, a_k) = (\sigma(1), \dots, \sigma(k)) \) for a unique \( \sigma \in S_k \), and then \( \u_{\sigma(1)}\wedge\dots\wedge\u_{\sigma(k)} = \sgn(\sigma)\,\u_1\wedge\dots\wedge\u_k \) by @lem-alternating-map-properties (b). Hence
\[
\w_1\wedge\dots\wedge\w_k
= \Bigl(\sum_{\sigma \in S_k}\sgn(\sigma)\,p_{\sigma(1)1}\cdots p_{\sigma(k)k}\Bigr)
\u_1\wedge\dots\wedge\u_k,
\]
and the bracket is \( \det\P \) by @def-determinant.

(b) Both lists are bases of \( U \), so each \( \w_b \) is a combination of the \( \u_a \), giving \( \P \) as above, and \( \P \) is the change-of-coordinates matrix between two bases of \( U \), hence invertible (@prp-invertible-matrix-change-of-basis). By @thm-det-nonzero-iff-invertible, \( \det\P \ne 0 \), and (a) gives the claim. Both wedges are non-zero, by @thm-wedge-nonzero-iff-independent.

(c) By (b) the two wedges are non-zero scalar multiples of each other, so they span the same one-dimensional subspace of \( \Lambda^k V \). Any basis of \( U \) therefore determines the same line, which consequently depends on \( U \) alone. (This line is the object that Section 09's coordinates — the \( k\times k \) minors — describe, and it is how a \( k \)-dimensional subspace is turned into a single point.)
:::
