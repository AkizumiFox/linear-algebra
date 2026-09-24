# The Determinant as a Top Exterior Power

Chapter 7 built the determinant twice. First it proved that an alternating \( n \)-linear form on \( F^n \) is determined by its value at the standard basis (@thm-alternating-form-uniqueness), which says *at most one* normalized such form exists; then it wrote the Leibniz sum down and checked the three rules (@thm-leibniz-formula-alternating), which says *at least one* does. The number \( \det \A \) of @def-determinant is that form's value. This section builds the determinant a third time, and the honest way to describe what it adds is to say up front what it does not: no new value, no faster computation, and no theorem Chapter 7 was missing. What it adds is an **object**. The exterior powers of the previous section turn \( \det T \) from a number attached to a matrix into the operator that \( T \) induces on a one-dimensional space, and from that description multiplicativity stops being a computation and becomes the statement that composing two induced maps induces the composite.

Throughout, \( F \) is a field, \( V \) and \( W \) are finite-dimensional vector spaces over \( F \), and \( \Lambda^kV \), the wedge \( \v_1 \wedge \dots \wedge \v_k \), and the universal property for alternating maps are as in @def-exterior-power. We use freely that the wedges \( \v_{i_1} \wedge \dots \wedge \v_{i_k} \) over strictly increasing index tuples form a basis of \( \Lambda^kV \), so that \( \dim \Lambda^kV = \binom{n}{k} \) when \( \dim V = n \) (@thm-exterior-power-basis), and that a wedge of vectors is non-zero exactly when the list is linearly independent (@thm-wedge-nonzero-iff-independent).

## Wedging with a fixed vector

Two facts from the previous section will be used on every page, and one small tool is still missing.

The first fact is the **reordering rule**: the wedge map \( (\v_1, \dots, \v_k) \mapsto \v_1 \wedge \dots \wedge \v_k \) is alternating (@def-exterior-power), and an alternating multilinear map satisfies
\[
f(\v_{\sigma(1)}, \dots, \v_{\sigma(k)}) = \sgn(\sigma)\, f(\v_1, \dots, \v_k)
\]
for every \( \sigma \in S_k \), by @lem-alternating-map-properties (b). Reordering a wedge costs the sign of the permutation, and nothing else. The second is that \( \Lambda^nV \) is one-dimensional when \( \dim V = n \ge 1 \) (@cor-top-exterior-power-is-a-line); that is the whole engine of this section.

The missing tool is the ability to wedge a fixed vector onto a whole exterior power, not just onto a list of vectors. Section 10 builds the product on all of \( \Lambda V \); here one vector at a time is enough.

::: {#lem-wedge-by-a-vector}
[Wedging with a Fixed Vector]

Let \( \v \in V \) and \( k \ge 1 \). There is a **unique** linear map
\[
\varepsilon_{\v} \colon \Lambda^{k}V \to \Lambda^{k+1}V,
\qquad
\varepsilon_{\v}(\w_1 \wedge \dots \wedge \w_k) = \v \wedge \w_1 \wedge \dots \wedge \w_k .
\]
:::

::: {.proof}
The map \( V^k \to \Lambda^{k+1}V \) sending \( (\w_1, \dots, \w_k) \) to \( \v \wedge \w_1 \wedge \dots \wedge \w_k \) is \( k \)-linear, because the wedge of \( k+1 \) vectors is linear in each slot and the first slot is frozen at \( \v \); and it is alternating, because if \( \w_p = \w_r \) with \( p \ne r \) then the wedge of \( k+1 \) vectors has two equal arguments and is \( \0 \). By the universal property in @def-exterior-power it factors through \( \Lambda^kV \), giving a linear \( \varepsilon_{\v} \) with the stated values. Uniqueness holds because the wedges \( \w_1 \wedge \dots \wedge \w_k \) span \( \Lambda^kV \) (@thm-exterior-power-basis), and a linear map is determined on a spanning set.
:::

## Induced maps on exterior powers

A linear map should act on everything built from its domain. A map \( T \colon V \to W \) sends a list \( (\v_1, \dots, \v_k) \) to the list \( (T\v_1, \dots, T\v_k) \), so it ought to send the wedge \( \v_1 \wedge \dots \wedge \v_k \) to \( T\v_1 \wedge \dots \wedge T\v_k \). The only question is whether that rule defines a map at all: an element of \( \Lambda^kV \) can be written as a wedge in many ways, and an assignment made on wedges must be checked. The universal property answers it in two lines, and that is the point of having a universal property.

*The \( k \)-th exterior power of a map wedges its values together.*

::: {#def-exterior-power-of-map}
[Exterior Power of a Linear Map]

Let \( T \colon V \to W \) be linear and let \( k \ge 1 \). The **\( k \)-th exterior power** of \( T \) is the unique linear map
\[
\Lambda^{k}T \colon \Lambda^{k}V \to \Lambda^{k}W
\]
satisfying \( \Lambda^{k}T(\v_1 \wedge \dots \wedge \v_k) = T\v_1 \wedge \dots \wedge T\v_k \) for all \( \v_1, \dots, \v_k \in V \).
:::

**Well-definedness.** The map \( V^k \to \Lambda^kW \) sending \( (\v_1, \dots, \v_k) \) to \( T\v_1 \wedge \dots \wedge T\v_k \) is \( k \)-linear, since \( T \) is linear and the wedge in \( W \) is linear in each slot; and it is alternating, since \( \v_p = \v_r \) forces \( T\v_p = T\v_r \) and a wedge with two equal arguments is \( \0 \). So @def-exterior-power produces exactly one linear map on \( \Lambda^kV \) with the stated values, and the wedges span \( \Lambda^kV \) (@thm-exterior-power-basis), so no other linear map has them.

**Examples.**

- **\( k = 1 \).** \( \Lambda^1V = V \) and \( \Lambda^1T = T \): the definition says nothing new in degree one.
- **The identity.** \( \Lambda^k(\id_V) = \id \), since both sides send \( \v_1 \wedge \dots \wedge \v_k \) to itself.
- **A scalar.** For \( T = c\,\id_V \), \( \Lambda^kT(\v_1 \wedge \dots \wedge \v_k) = c^k\,\v_1 \wedge \dots \wedge \v_k \), so \( \Lambda^kT = c^k\,\id \). One factor of \( c \) comes out of each of the \( k \) slots.
- **A degenerate case.** If \( k > \dim V \) then \( \Lambda^kV = \{\0\} \) (@thm-exterior-power-basis) and \( \Lambda^kT \) is the zero map between zero spaces. Worth recording so that statements below need no size caveat.

**Non-example by minimal change.** Replace "alternating" by nothing: the rule \( \v_1 \otimes \dots \otimes \v_k \mapsto T\v_1 \wedge \dots \wedge T\v_k \) on \( V^{\otimes k} \) is perfectly well defined, but it is **not** the map above, because \( \Lambda^kV \) is a quotient of \( V^{\otimes k} \) and not a subspace of it. What makes @def-exterior-power-of-map legal is precisely that the rule kills the relations that were divided out.

The reason for having the notation is the next sentence.

::: {#thm-exterior-power-functorial}
[Exterior Powers Respect Composition]

Let \( T \colon U \to V \) and \( S \colon V \to W \) be linear, and let \( k \ge 1 \). Then
\[
\Lambda^{k}(ST) = (\Lambda^{k}S)(\Lambda^{k}T),
\qquad
\Lambda^{k}(\id_V) = \id_{\Lambda^{k}V} .
\]
:::

::: {.proof}
Both \( \Lambda^k(ST) \) and \( (\Lambda^kS)(\Lambda^kT) \) are linear maps \( \Lambda^kU \to \Lambda^kW \), so it suffices to compare them on the wedges, which span \( \Lambda^kU \) (@thm-exterior-power-basis). By @def-exterior-power-of-map applied three times,
\[
(\Lambda^{k}S)(\Lambda^{k}T)(\u_1 \wedge \dots \wedge \u_k)
= ST\u_1 \wedge \dots \wedge ST\u_k
= \Lambda^{k}(ST)(\u_1 \wedge \dots \wedge \u_k).
\]
The second identity was checked above. This proves the theorem.
:::

::: {#exm-lambda-two-of-a-three-by-three}
[The second exterior power of a 3 × 3 matrix]

Let \( T \colon \nQ^3 \to \nQ^3 \) have matrix
\[
\A = \begin{pmatrix} 2 & 1 & 3 \\ 0 & 4 & 1 \\ 5 & 2 & 1 \end{pmatrix}
\]
in the standard basis. Find the matrix of \( \Lambda^2T \) in the basis \( (\e_1 \wedge \e_2,\ \e_1 \wedge \e_3,\ \e_2 \wedge \e_3) \) of \( \Lambda^2\nQ^3 \), and compute its determinant.
:::

::: {.solution}
By @def-exterior-power-of-map, \( \Lambda^2T(\e_i \wedge \e_j) = \a_i \wedge \a_j \), where \( \a_1, \a_2, \a_3 \) are the columns of \( \A \). Expand one column:
\[
\begin{aligned}
\a_1 \wedge \a_2 &= (2\e_1 + 5\e_3) \wedge (\e_1 + 4\e_2 + 2\e_3) \\
&= 8\,\e_1 \wedge \e_2 + 4\,\e_1 \wedge \e_3 + 5\,\e_3 \wedge \e_1 + 20\,\e_3 \wedge \e_2 \\
&= 8\,\e_1 \wedge \e_2 - \e_1 \wedge \e_3 - 20\,\e_2 \wedge \e_3 ,
\end{aligned}
\]
where the terms \( 2\,\e_1 \wedge \e_1 \) and \( 10\,\e_3 \wedge \e_3 \) were dropped in the second line because a wedge with a repeated vector is \( \0 \), and the third line used \( \e_3 \wedge \e_1 = -\e_1 \wedge \e_3 \) and \( \e_3 \wedge \e_2 = -\e_2 \wedge \e_3 \) (@lem-alternating-map-properties (b)). The coefficients \( 8, -1, -20 \) are the three \( 2 \times 2 \) minors of the first two columns of \( \A \), on rows \( \{1,2\}, \{1,3\}, \{2,3\} \) — a pattern the last part of this section explains. Doing the same for the other two column pairs gives
\[
[\Lambda^2 T] = \begin{pmatrix} 8 & 2 & -11 \\ -1 & -13 & -5 \\ -20 & -5 & 2 \end{pmatrix},
\]
whose determinant is \( 2601 \). Since \( \det \A = -51 \), this is \( (\det \A)^2 \).
:::

::: {.check}
In the example, why is \( \Lambda^2 T \) **not** multiplication by a scalar, while \( \Lambda^3 T \) is?
:::

::: {.solution}
\( \dim \Lambda^2\nQ^3 = \binom{3}{2} = 3 \) by @thm-exterior-power-basis, and the displayed matrix is not a scalar multiple of \( \I_3 \), so \( \Lambda^2T \) is an operator on a three-dimensional space with no reason to be scalar. But \( \dim \Lambda^3\nQ^3 = \binom{3}{3} = 1 \), and every linear operator on a one-dimensional space is multiplication by a scalar. Being a line is what makes the top power special.
:::

## The top exterior power

That last observation is the whole theorem. When \( k \) equals \( \dim V \), the space \( \Lambda^kV \) is a line, an operator on a line is a scalar, and the scalar can be read off by feeding in a basis.

::: {#thm-det-is-top-exterior}
[The Determinant Is the Top Exterior Power]

Let \( V \) be a vector space over \( F \) with \( \dim V = n \ge 1 \), and let \( T \in \cL(V) \). Then \( \dim \Lambda^nV = 1 \), and \( \Lambda^nT \) is multiplication by \( \det T \):
\[
\Lambda^{n}T(\omega) = (\det T)\,\omega
\qquad \text{for every } \omega \in \Lambda^{n}V .
\]
Equivalently, for all \( \v_1, \dots, \v_n \in V \),
\[
T\v_1 \wedge \dots \wedge T\v_n = (\det T)\, \v_1 \wedge \dots \wedge \v_n .
\]{#eq-top-wedge-determinant}
:::

::: {.idea}
Three moves. ① \( \Lambda^nV \) is one-dimensional, so \( \Lambda^nT \) is multiplication by one unknown scalar \( c \). ② To find \( c \), evaluate on a basis wedge \( \v_1 \wedge \dots \wedge \v_n \) and expand each \( T\v_j \) in the basis. ③ The expansion produces one term for every function from slots to basis indices; the non-injective ones die because a wedge with a repeat is zero, and what survives is a sum over permutations with signs — the Leibniz formula, arriving on its own.
:::

::: {.proof}
Fix a basis \( \sB = (\v_1, \dots, \v_n) \) of \( V \). By @cor-top-exterior-power-is-a-line, \( \dim \Lambda^nV = 1 \) with basis the single wedge \( \omega_0 = \v_1 \wedge \dots \wedge \v_n \). Since \( \Lambda^nT \) is a linear operator on a one-dimensional space, there is a unique \( c \in F \) with \( \Lambda^nT(\omega_0) = c\,\omega_0 \), and then \( \Lambda^nT(a\omega_0) = ac\,\omega_0 \) for every \( a \in F \), so \( \Lambda^nT = c\,\id \) on all of \( \Lambda^nV \).

It remains to show \( c = \det T \). Let \( \A = \mtx{T}{\sB}{\sB} \) have entries \( a_{ij} \), so that \( T\v_j = \sum_{i=1}^{n} a_{ij}\v_i \) (@def-matrix-of-linear-map). The wedge of \( n \) vectors is linear in each slot, so expanding slot by slot gives one term for each function \( \varphi \colon \{1, \dots, n\} \to \{1, \dots, n\} \):
\[
T\v_1 \wedge \dots \wedge T\v_n
= \sum_{\varphi} a_{\varphi(1)1} \cdots a_{\varphi(n)n}\;
\v_{\varphi(1)} \wedge \dots \wedge \v_{\varphi(n)} .
\]
If \( \varphi \) is not injective, two slots hold the same vector and the wedge is \( \0 \). A non-injective \( \varphi \) is possible only because the domain and codomain are finite of the same size, so the surviving \( \varphi \) are exactly the bijections, that is, the permutations \( \sigma \in S_n \). For those, @lem-alternating-map-properties (b) gives \( \v_{\sigma(1)} \wedge \dots \wedge \v_{\sigma(n)} = \sgn(\sigma)\,\omega_0 \). Therefore
\[
\Lambda^{n}T(\omega_0)
= \Bigl( \sum_{\sigma \in S_n} \sgn(\sigma)\, a_{\sigma(1)1} \cdots a_{\sigma(n)n} \Bigr) \omega_0 ,
\]
and the bracket is \( \det \A \) by @def-determinant, which is \( \det T \) by @def-det-operator. So \( c = \det T \).

For the last display, note that both sides of @eq-top-wedge-determinant are \( n \)-linear in \( (\v_1, \dots, \v_n) \) and agree when the list is the basis \( \sB \); but in fact no extra argument is needed, since \( \v_1 \wedge \dots \wedge \v_n \in \Lambda^nV \) for **any** list, and the first display applies to it. This proves the theorem.
:::

::: {.warning}
**Only the top power is a line.** For \( 1 \le k < n \) the operator \( \Lambda^kT \) is not multiplication by a scalar in general: @exm-lambda-two-of-a-three-by-three exhibits a \( \Lambda^2T \) with three different diagonal entries. The determinant appears because \( \binom{n}{n} = 1 \), not because exterior powers are scalars.
:::

::: {.warning}
**A map between different spaces still has no determinant.** If \( T \colon V \to W \) is linear with \( \dim V = \dim W = n \), then \( \Lambda^nT \) is a linear map between two **different** one-dimensional spaces, and there is no scalar attached to it until bases of \( \Lambda^nV \) and \( \Lambda^nW \) are chosen. Changing the basis of \( \Lambda^nW \) alone rescales the number arbitrarily. This is the same obstruction Chapter 7 recorded after @def-det-operator, now visible as the failure of a line to have a canonical generator.
:::

::: {.check}
Let \( T \) be the operator on \( F^3 \) with \( T\e_1 = \e_2 \), \( T\e_2 = \e_3 \) and \( T\e_3 = \e_1 \). Read \( \det T \) off @eq-top-wedge-determinant, without writing down a matrix.
:::

::: {.solution}
\( T\e_1 \wedge T\e_2 \wedge T\e_3 = \e_2 \wedge \e_3 \wedge \e_1 \). The permutation carrying \( (1,2,3) \) to \( (2,3,1) \) is a \( 3 \)-cycle, of sign \( +1 \) (@prp-sign-of-cycle), so by @lem-alternating-map-properties (b) this equals \( \e_1 \wedge \e_2 \wedge \e_3 \). Comparing with @eq-top-wedge-determinant on the non-zero element \( \e_1 \wedge \e_2 \wedge \e_3 \) gives \( \det T = 1 \).
:::

## What the third construction adds

It is worth saying plainly, because the temptation to oversell a slick construction is real.

**It adds no new value.** The scalar produced in the proof is the Leibniz sum, arrived at by the same expansion that proved @thm-alternating-form-uniqueness in Chapter 7: expand multilinearly, discard the terms with a repeated basis vector, sort the survivors and collect signs. Anyone who has read Chapter 7 §04 has read that computation. The exterior power did not compute the determinant; it stored the same computation in a different place.

**It adds no faster method.** Nothing here helps evaluate a determinant. Elimination remains the way to do that (@exm-det-by-elimination).

**What it does add is that \( \det \) is a map, not just a number.** Chapter 7 defined \( \det \A \) by a formula in the entries and then had to *prove* that operators inherit it: the formula depends on a basis, so @cor-det-similarity-invariant was needed before @def-det-operator could be written down. Here \( \Lambda^nT \) is defined with no basis in sight, and the scalar exists because \( \Lambda^nV \) is a line. Basis-independence is not a theorem about the determinant; it is the absence of any choice to be independent of. One honest qualification: the route is not self-contained. @thm-exterior-power-basis, which is what makes \( \Lambda^n V \) a line in the first place, proves independence with a \( k \times k \) determinant, and the identification of the scalar with \( \det T \) goes through @def-det-operator. Chapter 7 is not being replaced here; it is being re-read.

**And from that, multiplicativity is free.**

::: {#cor-det-multiplicative-again}
[Multiplicativity and Invertibility, from Functoriality]

Let \( \dim V = n \ge 1 \) and \( S, T \in \cL(V) \).

::: {.enumerate options="label=(\alph*)"}
1. \( \det(ST) = \det S \, \det T \), and \( \det \id_V = 1 \).
2. \( T \) is invertible if and only if \( \det T \ne 0 \).
:::
:::

::: {.proof}
(a) By @thm-exterior-power-functorial, \( \Lambda^n(ST) = (\Lambda^nS)(\Lambda^nT) \). By @thm-det-is-top-exterior all three maps are multiplications by scalars on the line \( \Lambda^nV \), namely by \( \det(ST) \), \( \det S \) and \( \det T \); and multiplication by \( \det T \) followed by multiplication by \( \det S \) is multiplication by \( \det S \det T \). Two scalar multiplications on a non-zero space are equal only if the scalars are, so \( \det(ST) = \det S\,\det T \). Likewise \( \Lambda^n(\id_V) = \id \), so \( \det \id_V = 1 \).

(b) \( (\Rightarrow) \) If \( T \) is invertible, apply (a) to \( TT^{-1} = \id_V \): then \( \det T \cdot \det(T^{-1}) = 1 \), so \( \det T \ne 0 \). \( (\Leftarrow) \) Suppose \( T \) is not invertible. Then \( T \) is not injective, so \( \ker T \ne \{\0\} \); choose \( \v_1 \in \ker T \) with \( \v_1 \ne \0 \) and extend to a basis \( (\v_1, \dots, \v_n) \) of \( V \) (@thm-basis-extension). Since \( T\v_1 = \0 \) and the wedge is linear in its first slot, \( T\v_1 \wedge \dots \wedge T\v_n = \0 \). By @eq-top-wedge-determinant this is \( (\det T)\,\v_1 \wedge \dots \wedge \v_n \), and the wedge of a basis is non-zero (@thm-wedge-nonzero-iff-independent), so \( \det T = 0 \).
:::

Part (b) is the promise @thm-wedge-nonzero-iff-independent made: the test "is this list independent?" and the test "is this determinant non-zero?" are the same test, once the determinant is read as an induced map.

Compare the work this replaces. Chapter 7 proved @thm-det-multiplicative by fixing \( \A \), checking that \( \B \mapsto \det(\A\B) \) is alternating and \( n \)-linear in the columns of \( \B \), and applying uniqueness. That proof is short and correct; what the present one shows is that the content is not really about determinants at all. Multiplicativity is the statement that \( \Lambda^n \) turns composition into composition — and \( \Lambda^n \) does that for the same reason that \( \Lambda^k \) does it for every \( k \), where no scalar is available and no multiplicativity statement can even be phrased.

::: {.remark}
What is **not** improved: @thm-det-transpose. The identity \( \det \A\tp = \det \A \) is a statement about rows versus columns, and \( \Lambda^n \) sees only the map \( T \), which has no rows. Chapter 7's proof, reindexing the Leibniz sum by \( \sigma^{-1} \), remains the natural one.
:::

## The coordinates of a wedge

The example above produced the minors of a matrix as the coefficients of a wedge, apparently by accident. It was not an accident, and the general statement is the bridge between this chapter and Chapter 7 §07.

Fix \( n \ge 1 \), write \( [n] = \{1, \dots, n\} \) as Chapter 7 §07 does, and recall the notation of @def-submatrix-minor: for \( \A \in M_{n \times k}(F) \) and a set \( I = \{i_1 < \dots < i_k\} \subseteq [n] \) of size \( k \), the submatrix \( \A_{I,[k]} \in M_k(F) \) keeps the rows in \( I \) and all \( k \) columns, and its determinant is a \( k \times k \) minor of \( \A \). Write
\[
\e_I \coloneqq \e_{i_1} \wedge \e_{i_2} \wedge \dots \wedge \e_{i_k} \in \Lambda^{k}F^{n} ,
\]
so that the \( \e_I \), over all \( k \)-element \( I \subseteq [n] \), form the basis of @thm-exterior-power-basis.

::: {#thm-wedge-coordinates-are-minors}
[The Coordinates of a Wedge Are the Minors]

Let \( 1 \le k \le n \), let \( \v_1, \dots, \v_k \in F^n \), and let \( \A \in M_{n \times k}(F) \) be the matrix with these vectors as its columns. Then
\[
\v_1 \wedge \v_2 \wedge \dots \wedge \v_k
= \sum_{I} \bigl(\det \A_{I,[k]}\bigr)\, \e_I ,
\]
the sum running over all subsets \( I \subseteq [n] \) with \( \lvert I \rvert = k \). That is, the coordinate of \( \v_1 \wedge \dots \wedge \v_k \) at \( \e_I \) is the \( k \times k \) minor of \( \A \) on the rows \( I \).
:::

::: {.idea}
The same expansion as in @thm-det-is-top-exterior, but now the index functions run into a bigger set. An injective \( \varphi \colon [k] \to [n] \) is a choice of image set \( I \) followed by an ordering of it, so the terms group into one bunch per \( I \), and each bunch is a signed sum over \( S_k \): a determinant of size \( k \).
:::

::: {.proof}
Write \( \A = (a_{ij}) \), so \( \v_j = \sum_{i=1}^{n} a_{ij}\e_i \). Expanding the wedge in each of its \( k \) slots gives one term per function \( \varphi \colon [k] \to [n] \):
\[
\v_1 \wedge \dots \wedge \v_k
= \sum_{\varphi} a_{\varphi(1)1} \cdots a_{\varphi(k)k}\,
\e_{\varphi(1)} \wedge \dots \wedge \e_{\varphi(k)} .
\]
A non-injective \( \varphi \) repeats a basis vector, so its wedge is \( \0 \) and its term drops out. An injective \( \varphi \) is determined by its image \( I = \{i_1 < \dots < i_k\} \) together with the permutation \( \sigma \in S_k \) defined by \( \varphi(j) = i_{\sigma(j)} \); conversely every pair \( (I, \sigma) \) arises from exactly one injective \( \varphi \). For such a \( \varphi \), @lem-alternating-map-properties (b) gives
\[
\e_{\varphi(1)} \wedge \dots \wedge \e_{\varphi(k)}
= \e_{i_{\sigma(1)}} \wedge \dots \wedge \e_{i_{\sigma(k)}}
= \sgn(\sigma)\, \e_I .
\]
Grouping the terms by \( I \) therefore gives
\[
\v_1 \wedge \dots \wedge \v_k
= \sum_{I} \Bigl( \sum_{\sigma \in S_k} \sgn(\sigma)\, a_{i_{\sigma(1)}1} \cdots a_{i_{\sigma(k)}k} \Bigr) \e_I .
\]
By @def-submatrix-minor the \( (p, q) \)-entry of \( \A_{I,[k]} \) is \( a_{i_pq} \), so the inner sum is exactly the Leibniz sum of @def-determinant for the \( k \times k \) matrix \( \A_{I,[k]} \), that is, \( \det \A_{I,[k]} \). This proves the theorem.
:::

::: {#exm-wedge-coordinates-f4}
[A wedge of two vectors in four-dimensional space]

In \( \nQ^4 \), let \( \v_1 = (1, 0, 2, 1) \) and \( \v_2 = (0, 1, 1, 3) \). Write \( \v_1 \wedge \v_2 \) in the basis of \( \Lambda^2\nQ^4 \).
:::

::: {.solution}
Let \( \A \in M_{4 \times 2}(\nQ) \) have these two vectors as its columns, so that \( \A_{\{1,2\},[2]} = \begin{psmallmatrix} 1 & 0 \\ 0 & 1 \end{psmallmatrix} \) and the other five \( 2 \times 2 \) submatrices read off the same way. Their determinants are
\[
\begin{aligned}
&\det \A_{\{1,2\}} = 1, \quad \det \A_{\{1,3\}} = 1, \quad \det \A_{\{1,4\}} = 3, \\
&\det \A_{\{2,3\}} = -2, \quad \det \A_{\{2,4\}} = -1, \quad \det \A_{\{3,4\}} = 5,
\end{aligned}
\]
abbreviating \( \A_{I,[2]} \) to \( \A_I \). By @thm-wedge-coordinates-are-minors,
\[
\begin{aligned}
\v_1 \wedge \v_2 = {}& \e_{12} + \e_{13} + 3\,\e_{14} \\
& - 2\,\e_{23} - \e_{24} + 5\,\e_{34} .
\end{aligned}
\]
As a check, some coordinate is non-zero, so \( \v_1 \wedge \v_2 \ne \0 \), so \( (\v_1, \v_2) \) is linearly independent by @thm-wedge-nonzero-iff-independent — which is visible directly, since neither vector is a multiple of the other.
:::

That check generalizes at once, and what comes out is a theorem of Chapter 7.

::: {#cor-minors-detect-independence}
[Independence via Minors]

Let \( \v_1, \dots, \v_k \in F^n \) and let \( \A \in M_{n \times k}(F) \) have these vectors as its columns. Then \( (\v_1, \dots, \v_k) \) is linearly independent if and only if some \( k \times k \) minor of \( \A \) is non-zero.
:::

::: {.proof}
By @thm-wedge-nonzero-iff-independent the list is independent exactly when \( \v_1 \wedge \dots \wedge \v_k \ne \0 \). By @thm-wedge-coordinates-are-minors the coordinates of that wedge in the basis \( (\e_I) \) of @thm-exterior-power-basis are the \( k \times k \) minors of \( \A \), and a vector is \( \0 \) exactly when all of its coordinates in a basis vanish. (For \( k > n \) both sides fail: \( \Lambda^kF^n = \{\0\} \) and \( \A \) has no \( k \times k \) submatrix.)
:::

This is @thm-rank-via-minors in the case of full column rank, and the general case follows from it: \( \rank \A \) is the largest number of independent columns, hence the largest \( k \) for which some \( k \) columns carry a non-zero \( k \times k \) minor. Chapter 7 proved it with two careful steps involving pivot columns and row rank. The wedge proves it by naming the coordinates.

## Laplace expansion

Cofactor expansion also comes out of the coordinate theorem, once the wedge of \( n - 1 \) vectors is available. The route is: pull the chosen column out of the wedge, recognize what is left as an element of \( \Lambda^{n-1}F^n \) whose coordinates are the \( (n-1) \times (n-1) \) minors, and wedge \( \e_i \) back on.

::: {#cor-laplace-from-wedge}
[Cofactor Expansion, from a Wedge]

Let \( n \ge 2 \), let \( \A \in M_n(F) \) with minors \( M_{ij} \) as in @def-minor-cofactor, and fix \( j \in [n] \). Then
\[
\det \A = \sum_{i=1}^{n} (-1)^{i+j} a_{ij} M_{ij} .
\]
:::

::: {.idea}
Write \( \det \A \) as the wedge of the columns. Linearity in the \( j \)-th slot splits it into \( n \) pieces, one per \( i \), with \( \e_i \) sitting in that slot. Move \( \e_i \) to the front at a cost of \( (-1)^{j-1} \); the remaining \( n-1 \) columns form a wedge whose coordinates are the minors of the matrix with column \( j \) deleted, and wedging \( \e_i \) on kills every coordinate except the one whose index set misses \( i \).
:::

::: {.proof}
Let \( \a_1, \dots, \a_n \) be the columns of \( \A \) and \( \omega_0 = \e_1 \wedge \dots \wedge \e_n \). By @thm-det-is-top-exterior applied to the operator \( \x \mapsto \A\x \), whose matrix in the standard basis is \( \A \),
\[
\a_1 \wedge \dots \wedge \a_n = (\det \A)\,\omega_0 .
\]
Substituting \( \a_j = \sum_{i=1}^{n} a_{ij}\e_i \) and using linearity in slot \( j \),
\[
(\det \A)\,\omega_0
= \sum_{i=1}^{n} a_{ij}\;
\a_1 \wedge \dots \wedge \underset{\text{slot } j}{\e_i} \wedge \dots \wedge \a_n .
\]
Fix \( i \). Moving \( \e_i \) from slot \( j \) to the front means \( j - 1 \) exchanges of neighbors, so by @lem-alternating-map-properties (b) the \( i \)-th wedge above equals \( (-1)^{j-1}\, \varepsilon_{\e_i}(\eta) \), where \( \eta = \a_1 \wedge \dots \wedge \widehat{\a_j} \wedge \dots \wedge \a_n \in \Lambda^{n-1}F^n \) omits the \( j \)-th column, and \( \varepsilon_{\e_i} \) is the map of @lem-wedge-by-a-vector.

Let \( \B \in M_{n \times (n-1)}(F) \) be \( \A \) with column \( j \) deleted. By @thm-wedge-coordinates-are-minors,
\[
\eta = \sum_{l=1}^{n} \bigl(\det \B_{[n] \setminus \{l\},\,[n-1]}\bigr)\, \e_{[n] \setminus \{l\}} ,
\]
since the \( (n-1) \)-element subsets of \( [n] \) are exactly the complements of single elements. Deleting row \( l \) from \( \B \) deletes row \( l \) and column \( j \) from \( \A \), so \( \det \B_{[n] \setminus \{l\},[n-1]} = M_{lj} \) by @def-minor-cofactor. Now apply \( \varepsilon_{\e_i} \). For \( l \ne i \) the index set \( [n] \setminus \{l\} \) contains \( i \), so \( \e_i \wedge \e_{[n] \setminus \{l\}} \) repeats \( \e_i \) and vanishes; for \( l = i \), moving \( \e_i \) into its place costs \( i - 1 \) exchanges, so \( \e_i \wedge \e_{[n] \setminus \{i\}} = (-1)^{i-1}\omega_0 \) by @lem-alternating-map-properties (b). Hence \( \varepsilon_{\e_i}(\eta) = (-1)^{i-1}M_{ij}\,\omega_0 \), and
\[
(\det \A)\,\omega_0
= \sum_{i=1}^{n} a_{ij}(-1)^{j-1}(-1)^{i-1}M_{ij}\,\omega_0 .
\]
Since \( (-1)^{i+j-2} = (-1)^{i+j} \) and \( \omega_0 \ne \0 \) (@thm-wedge-nonzero-iff-independent), comparing coefficients gives the stated formula.
:::

This is @thm-laplace-expansion (a). The row version follows from it by @thm-det-transpose, exactly as in Chapter 7. The gain is again structural rather than practical: the sign \( (-1)^{i+j} \), which in Chapter 7 arrived from a careful count of row and column moves, is here the price of two reversals, \( j-1 \) in one direction and \( i-1 \) in the other.

## Exercises

### A. Check your understanding

:::: {#exr-determinant-as-top-exterior-power-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the defining property of \( \Lambda^kT \), and say why a rule given on wedges needs an argument before it defines a map.
2. State @thm-det-is-top-exterior.
3. Name one thing this section's construction of the determinant adds to Chapter 7's, and one thing it does not.
4. True or false: for every \( T \in \cL(V) \) and every \( k \), the map \( \Lambda^kT \) is multiplication by a scalar. Justify your answer.
5. What are the coordinates of \( \v_1 \wedge \dots \wedge \v_k \) in \( \Lambda^kF^n \), in the basis \( (\e_I) \)?
:::
::::

::: {.solution}
(a) \( \Lambda^kT \) is the unique linear map \( \Lambda^kV \to \Lambda^kW \) with \( \Lambda^kT(\v_1 \wedge \dots \wedge \v_k) = T\v_1 \wedge \dots \wedge T\v_k \) (@def-exterior-power-of-map). An element of \( \Lambda^kV \) has many expressions as a sum of wedges, so a rule stated on wedges might assign two different values to one element; the universal property of @def-exterior-power removes the danger by producing the map from an alternating multilinear map upstairs.

(b) If \( \dim V = n \ge 1 \) and \( T \in \cL(V) \), then \( \dim \Lambda^nV = 1 \) and \( \Lambda^nT(\omega) = (\det T)\omega \) for every \( \omega \in \Lambda^nV \).

(c) It adds that the determinant is the induced map on a line, so that no basis and no similarity-invariance argument is needed to define \( \det T \), and multiplicativity becomes @thm-exterior-power-functorial. It does not add a new value, a new method of computation, or any improvement to \( \det \A\tp = \det \A \).

(d) False. It is true when \( k = n = \dim V \), and when \( k > n \) for the trivial reason that \( \Lambda^kV = \{\0\} \). For \( 1 \le k < n \) it usually fails: see @exm-lambda-two-of-a-three-by-three, where \( \Lambda^2T \) has matrix with rows \( (8, 2, -11) \), \( (-1, -13, -5) \), \( (-20, -5, 2) \), not a scalar matrix.

(e) The \( k \times k \) minors of the matrix whose columns are \( \v_1, \dots, \v_k \): the coordinate at \( \e_I \) is \( \det \A_{I,[k]} \) (@thm-wedge-coordinates-are-minors).
:::

### B. Practice

::: {#exr-determinant-as-top-exterior-power-b1}
[B1: A second exterior power]

Let \( T \colon \nQ^3 \to \nQ^3 \) have standard matrix
\[
\A = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 3 \\ 2 & 0 & 1 \end{pmatrix}.
\]
Find the matrix of \( \Lambda^2T \) in the basis \( (\e_1 \wedge \e_2, \e_1 \wedge \e_3, \e_2 \wedge \e_3) \). Hence verify that \( \det(\Lambda^2T) = (\det T)^2 \).
:::

::: {.solution}
By @def-exterior-power-of-map and @thm-wedge-coordinates-are-minors, the entry of \( [\Lambda^2T] \) in row \( I \) and column \( J \) is \( \det \A_{I,J} \), with rows and columns indexed by \( \{1,2\}, \{1,3\}, \{2,3\} \) in that order. Computing the nine \( 2 \times 2 \) minors,
\[
[\Lambda^2T] = \begin{pmatrix} 1 & 3 & 6 \\ -4 & 1 & 2 \\ -2 & -6 & 1 \end{pmatrix}.
\]
Its determinant is \( 169 \). Expanding \( \det \A \) along the first column (@thm-laplace-expansion) gives \( 1 \cdot (1 - 0) + 2 \cdot (6 - 0) = 13 \), and \( 13^2 = 169 \).
:::

::: {#exr-determinant-as-top-exterior-power-b2}
[B2: Independence by minors]

In \( \nQ^4 \), let \( \v_1 = (1, 2, 0, 1) \), \( \v_2 = (0, 1, 1, 1) \) and \( \v_3 = (1, 0, -2, -1) \). Compute the coordinates of \( \v_1 \wedge \v_2 \wedge \v_3 \) in \( \Lambda^3\nQ^4 \), and hence determine whether the list is linearly independent. Justify your answer.
:::

::: {.solution}
Let \( \A \in M_{4 \times 3}(\nQ) \) have these columns. By @thm-wedge-coordinates-are-minors the four coordinates are the \( 3 \times 3 \) minors on the row sets \( \{1,2,3\}, \{1,2,4\}, \{1,3,4\}, \{2,3,4\} \). Computing them,
\[
\det \A_{\{1,2,3\}} = \det \begin{pmatrix} 1 & 0 & 1 \\ 2 & 1 & 0 \\ 0 & 1 & -2 \end{pmatrix} = 0 ,
\]
and the same for the other three: \( \det \A_{\{1,2,4\}} = \det \A_{\{1,3,4\}} = \det \A_{\{2,3,4\}} = 0 \). So \( \v_1 \wedge \v_2 \wedge \v_3 = \0 \), and by @thm-wedge-nonzero-iff-independent the list is **dependent**. Indeed \( \v_3 = \v_1 - 2\v_2 \).
:::

::: {#exr-determinant-as-top-exterior-power-b3}
[B3: Determinant of an inverse]

Let \( \dim V = n \ge 1 \) and let \( T \in \cL(V) \) be invertible. Using @thm-exterior-power-functorial and @thm-det-is-top-exterior, and no formula for the determinant, prove that \( \Lambda^nT \) is invertible and that \( \det(T^{-1}) = (\det T)^{-1} \).
:::

::: {.solution}
By @thm-exterior-power-functorial, \( (\Lambda^nT)(\Lambda^n T^{-1}) = \Lambda^n(TT^{-1}) = \Lambda^n(\id_V) = \id \), and symmetrically in the other order. So \( \Lambda^nT \) is invertible with inverse \( \Lambda^nT^{-1} \). By @thm-det-is-top-exterior these two maps are multiplication by \( \det T \) and by \( \det(T^{-1}) \) on the line \( \Lambda^nV \), and their composite is multiplication by \( \det T \cdot \det(T^{-1}) \), which equals \( \id \). Since \( \Lambda^nV \ne \{\0\} \), this forces \( \det T \cdot \det(T^{-1}) = 1 \). In particular \( \det T \ne 0 \), and \( \det(T^{-1}) = (\det T)^{-1} \).
:::

### C. Going deeper

:::: {#exr-determinant-as-top-exterior-power-c1}
[C1: The trace of an exterior power]

Let \( \A \in M_n(F) \) and \( 1 \le k \le n \), and let \( T \colon F^n \to F^n \) be \( \x \mapsto \A\x \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that the matrix of \( \Lambda^kT \) in the basis \( (\e_I) \) has \( (I, J) \)-entry \( \det \A_{I,J} \).
2. Deduce that \( \tr(\Lambda^kT) \) is the sum of the \( \binom{n}{k} \) **principal** \( k \times k \) minors of \( \A \), those with \( I = J \).
3. Compute \( \tr(\Lambda^2T) \) for the matrix \( \A \) of @exm-lambda-two-of-a-three-by-three, and check it against the matrix found there.
:::
::::

::: {.solution}
(a) Column \( J = \{j_1 < \dots < j_k\} \) of the matrix is the coordinate vector of \( \Lambda^kT(\e_J) = \a_{j_1} \wedge \dots \wedge \a_{j_k} \), where \( \a_j = T\e_j \) is the \( j \)-th column of \( \A \) (@def-exterior-power-of-map). By @thm-wedge-coordinates-are-minors applied to the \( n \times k \) matrix with columns \( \a_{j_1}, \dots, \a_{j_k} \), the coordinate at \( \e_I \) is the determinant of its submatrix on rows \( I \), which is \( \det \A_{I,J} \) (@def-submatrix-minor).

(b) The trace is the sum of the diagonal entries, that is, of the entries with \( I = J \), and by (a) those are the principal minors \( \det \A_{I,I} \).

(c) The three principal \( 2 \times 2 \) minors of \( \A \) are \( \det \begin{psmallmatrix} 2 & 1 \\ 0 & 4\end{psmallmatrix} = 8 \), \( \det \begin{psmallmatrix} 2 & 3 \\ 5 & 1\end{psmallmatrix} = -13 \) and \( \det \begin{psmallmatrix} 4 & 1 \\ 2 & 1\end{psmallmatrix} = 2 \). Their sum is \( -3 \), which is the sum of the diagonal entries \( 8, -13, 2 \) of the matrix computed in @exm-lambda-two-of-a-three-by-three.
:::

:::: {#exr-determinant-as-top-exterior-power-c2}
[C2: Cauchy–Binet from a wedge]

Let \( m \le n \), let \( \A \in M_{m \times n}(F) \) and \( \B \in M_{n \times m}(F) \), and let \( T_{\A} \colon F^n \to F^m \) and \( T_{\B} \colon F^m \to F^n \) be the associated maps.

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \Lambda^m T_{\B}(\e_1 \wedge \dots \wedge \e_m) = \sum_{J} (\det \B_{J,[m]})\, \e_J \), the sum over \( m \)-element subsets \( J \subseteq [n] \).
2. Show that \( \Lambda^m T_{\A}(\e_J) = (\det \A_{[m],J})\, \e_1 \wedge \dots \wedge \e_m \) for each such \( J \).
3. Hence deduce the Cauchy–Binet formula \( \det(\A\B) = \sum_{J} \det \A_{[m],J} \det \B_{J,[m]} \) (@thm-cauchy-binet).
:::
::::

::: {.solution}
(a) \( \Lambda^mT_{\B}(\e_1 \wedge \dots \wedge \e_m) = \B\e_1 \wedge \dots \wedge \B\e_m \) by @def-exterior-power-of-map, and the columns of \( \B \) are \( \B\e_1, \dots, \B\e_m \). Apply @thm-wedge-coordinates-are-minors in \( F^n \) with \( k = m \).

(b) Writing \( J = \{j_1 < \dots < j_m\} \), we get \( \Lambda^mT_{\A}(\e_J) = \A\e_{j_1} \wedge \dots \wedge \A\e_{j_m} \), a wedge of \( m \) vectors of \( F^m \). By @thm-wedge-coordinates-are-minors with \( k = m = n \) there is only one index set, \( [m] \) itself, and the coefficient is the determinant of the matrix with those columns, which is \( \A_{[m],J} \).

(c) By @thm-exterior-power-functorial, \( \Lambda^m(T_{\A}T_{\B}) = (\Lambda^mT_{\A})(\Lambda^mT_{\B}) \). The map \( T_{\A}T_{\B} \) is the operator on \( F^m \) with matrix \( \A\B \), so by @thm-det-is-top-exterior the left side sends \( \e_1 \wedge \dots \wedge \e_m \) to \( \det(\A\B)\,\e_1 \wedge \dots \wedge \e_m \). By (a) and then (b), the right side sends it to \( \sum_J \det \B_{J,[m]} \det \A_{[m],J}\, \e_1 \wedge \dots \wedge \e_m \). Comparing coefficients on the basis vector \( \e_1 \wedge \dots \wedge \e_m \ne \0 \) gives the formula.
:::

::: {#exr-determinant-as-top-exterior-power-c3}
[C3: Exterior powers of an injection]

Let \( T \colon V \to W \) be an **injective** linear map between finite-dimensional spaces and let \( 1 \le k \le \dim V \). Prove that \( \Lambda^kT \) is injective. Is the analogous statement true with "injective" replaced by "surjective"?

*Hint: choose a basis of \( V \) and use @thm-exterior-power-basis in both spaces.*
:::

::: {.solution}
Let \( (\v_1, \dots, \v_m) \) be a basis of \( V \). Since \( T \) is injective, \( (T\v_1, \dots, T\v_m) \) is linearly independent in \( W \), so it extends to a basis \( (T\v_1, \dots, T\v_m, \w_{m+1}, \dots) \) of \( W \) (@thm-basis-extension). By @thm-exterior-power-basis, the wedges \( \v_{i_1} \wedge \dots \wedge \v_{i_k} \) over increasing tuples form a basis of \( \Lambda^kV \), and \( \Lambda^kT \) sends each of them to \( T\v_{i_1} \wedge \dots \wedge T\v_{i_k} \), which is one of the basis vectors of \( \Lambda^kW \) provided by the extended basis. So \( \Lambda^kT \) carries a basis to a linearly independent list, hence is injective.

Yes for surjective as well, and more cheaply: if \( T \) is surjective then every \( \w_1 \wedge \dots \wedge \w_k \) equals \( T\v_1 \wedge \dots \wedge T\v_k \) for preimages \( \v_i \), so the image of \( \Lambda^kT \) contains a spanning set of \( \Lambda^kW \) (@thm-exterior-power-basis) and is therefore all of it.
:::
