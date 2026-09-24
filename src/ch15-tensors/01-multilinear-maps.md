# Multilinear Maps

Chapter 7 needed functions of several vectors that were linear in each vector separately, and called them multilinear forms (@def-multilinear-form). Every one of them landed in the field \( F \): the determinant, the signed area, a product of functionals. This chapter needs the same idea with the output allowed to be any vector space, because three of the most familiar operations in the book — matrix multiplication, composition of linear maps, the cross product — are linear in each argument and return something that is not a scalar. So we begin by extending Chapter 7's definition, count how many such maps there are, and then state the problem that the rest of the chapter exists to solve: a multilinear map is **not** a linear map, so none of the machinery of Chapters 2 to 5 is available to it.

Throughout, \( F \) is a field, \( k \ge 1 \) is an integer, and all vector spaces are over \( F \). From the third subsection on, every space named is finite-dimensional.

## From forms to maps

Here are three operations the book has used constantly.

- **Matrix multiplication.** For fixed sizes, \( (\A, \B) \mapsto \A\B \) satisfies \( (\A + \A')\B = \A\B + \A'\B \) and \( \A(\B + \B') = \A\B + \A\B' \), and scalars pull out of either factor.
- **Composition of linear maps.** \( (S, T) \mapsto ST \) satisfies the same four rules.
- **The cross product** on \( \nR^3 \), which is linear in each factor and returns a vector.

Each is linear in one argument while the other is held fixed. Each therefore looks exactly like @def-multilinear-form with \( k = 2 \) — except that the value is a matrix, a linear map or a vector, not a scalar. Chapter 7 had no reason to allow that, because it was building the determinant. We do, so we widen the definition. Nothing about Chapter 7's statements changes; a multilinear **form** will simply be the special case where the target is \( F \), and we will keep using @def-multilinear-form by that name whenever the target really is \( F \).

*A multilinear map is a function of several vectors that is linear in each one while the others are held fixed, with values in a vector space rather than in the field.*

::: {#def-multilinear-map}
[Multilinear Map]

Let \( V_1, \dots, V_k \) and \( W \) be vector spaces over the **same** field \( F \), with \( k \ge 1 \). A function
\[
\beta \colon V_1 \times V_2 \times \cdots \times V_k \to W
\]
is **\( k \)-linear**, or a **multilinear map**, if **for every** position \( i \in \{1, \dots, k\} \) and **every** choice of fixed vectors \( \v_j \in V_j \) for the positions \( j \ne i \), the function
\[
V_i \to W, \qquad \x \mapsto \beta(\v_1, \dots, \v_{i-1}, \x, \v_{i+1}, \dots, \v_k),
\]
is linear. A \( 2 \)-linear map is called **bilinear**.

When \( V_1 = \cdots = V_k = V \) we say \( \beta \) is \( k \)-linear **on \( V \)**; when in addition \( W = F \), the definition is word for word @def-multilinear-form, and we call \( \beta \) a multilinear **form**.
:::

In words, clause by clause. **Same field:** all \( k + 1 \) spaces are over one \( F \), since otherwise "linear" would mean different things in different slots. **For every position:** the condition is imposed \( k \) separate times, once per slot. **Every choice of fixed vectors:** the other \( k - 1 \) arguments are frozen at arbitrary values, not at convenient ones. **Is linear:** written out, for all \( \x, \y \in V_i \) and all \( c \in F \),
\[
\begin{aligned}
\beta(\dots, \x + \y, \dots) &= \beta(\dots, \x, \dots) + \beta(\dots, \y, \dots), \\
\beta(\dots, c\x, \dots) &= c\,\beta(\dots, \x, \dots),
\end{aligned}
\]
where the dots stand for the same frozen vectors on both sides. The spaces \( V_1, \dots, V_k \) are allowed to be different from each other and from \( W \); nothing forces \( k \) to be related to any dimension.

Two consequences are free. Putting \( c = 0 \) in slot \( i \) gives \( \beta(\dots, \0, \dots) = \0 \): a multilinear map kills any tuple with a zero entry. And by induction on the number of terms, expanding one slot at a time,
\[
\beta\Bigl(\sum_{i_1} a_{i_1}\x_{i_1},\ \dots,\ \sum_{i_k} a_{i_k}\y_{i_k}\Bigr)
= \sum_{i_1, \dots, i_k} a_{i_1}\cdots a_{i_k}\, \beta(\x_{i_1}, \dots, \y_{i_k}),
\]
a sum over all tuples of indices, one index per slot. This identity is the whole of the section: it says that a multilinear map is determined by its values on tuples drawn from spanning sets, and that the number of such tuples is a product, not a sum.

::: {#exm-multilinear-maps-first}
[Seven functions of several vectors]

Decide which of the following are multilinear, and with which \( k \).

::: {.enumerate options="label=(\alph*)"}
1. Any linear map \( T \colon V \to W \), viewed as a function of one vector.
2. Scalar multiplication \( F \times V \to V \), \( (c, \v) \mapsto c\v \), with \( F \) regarded as a vector space over itself.
3. Matrix multiplication \( M_{m \times n}(F) \times M_{n \times p}(F) \to M_{m \times p}(F) \), \( (\A, \B) \mapsto \A\B \).
4. Composition \( \cL(W, Z) \times \cL(V, W) \to \cL(V, Z) \), \( (S, T) \mapsto ST \).
5. The determinant \( (F^n)^n \to F \) sending \( (\a_1, \dots, \a_n) \) to \( \det \A \), where \( \A \) has columns \( \a_1, \dots, \a_n \).
6. The evaluation pairing \( V^{*} \times V \to F \), \( (\varphi, \v) \mapsto \varphi(\v) \).
7. The cross product \( \nR^3 \times \nR^3 \to \nR^3 \).
:::
:::

::: {.solution}
(a) With \( k = 1 \) there is one position and no other argument to freeze, so the condition reads: \( \x \mapsto T\x \) is linear. That is the hypothesis. So a \( 1 \)-linear map is **exactly** a linear map (@def-linear-transformation), and @def-multilinear-map generalizes it.

(b) Fix \( \v \). Then \( c \mapsto c\v \) is linear by (VS6) and (VS7) of @def-vector-space, which give \( (a + b)\v = a\v + b\v \) and \( a(c\v) = (ac)\v \). Fix \( c \). Then \( \v \mapsto c\v \) is linear by (VS5) and (VS7), the second of which gives \( c(a\v) = (ca)\v = (ac)\v = a(c\v) \), using that \( F \) is commutative. So scalar multiplication is bilinear. It is the smallest interesting example, and it shows that the two input spaces need not be equal.

(c) Fix \( \B \). Then \( \A \mapsto \A\B \) is linear, since \( (\A + \A')\B = \A\B + \A'\B \) and \( (c\A)\B = c(\A\B) \) by @thm-matrix-multiplication-properties. Fixing \( \A \) gives the other slot. So matrix multiplication is bilinear, with three different spaces in play when \( m, n, p \) differ.

(d) Same check, with @thm-composition-linear (a) supplying linearity of \( ST \) and @thm-composition-linear (d) supplying the two slots. Bilinear.

(e) The determinant is \( n \)-linear in the columns, and alternating, by @thm-leibniz-formula-alternating. It is the standard example of a multilinear form with \( k \) equal to the dimension. Here \( k = n \) is forced by the shape of a square matrix, not by the definition.

(f) Fix \( \v \). Then \( \varphi \mapsto \varphi(\v) \) is linear because the operations on \( V^{*} \) are pointwise (@def-dual-space). Fix \( \varphi \). Then \( \v \mapsto \varphi(\v) \) is linear because \( \varphi \) is a linear functional. Bilinear. This one-line example is the source of the contraction operation of a later section.

(g) The cross product of Chapter 7 has components \( a_2b_3 - a_3b_2 \) and its two cousins, each bilinear as in @exm-alternating-forms (b). A vector of bilinear functions is bilinear, since linearity in a slot may be checked coordinate by coordinate. So it is bilinear, with values in \( \nR^3 \) — an example that genuinely needs @def-multilinear-map rather than @def-multilinear-form.
:::

**Non-example, by minimal change.** Keep \( k = 2 \), keep \( V_1 = V_2 = W = F \), and change multiplication to addition: \( \sigma(a, b) = a + b \). Freeze \( b = 1 \). The resulting function \( a \mapsto a + 1 \) sends \( 0 \) to \( 1 \), so it is not linear (@thm-zero-maps-to-zero), and the clause "is linear" fails in the first slot. What still works is that \( \sigma \) is linear as a function on the product space \( F \times F \) of @def-product-of-spaces. That is precisely the distinction the next subsection is about.

**Why this definition.** One could try to define a "map of several variables" by asking for linearity in all slots at once, that is, by asking for a linear map on \( V_1 \times \cdots \times V_k \). The result would be a different and much poorer notion: it would exclude multiplication, composition, the determinant and every inner product, and would include only sums of linear maps applied to the separate slots. Freezing all but one slot is what keeps products in the theory. The name says the same thing: *multi*, once per slot; *linear*, in that slot alone.

## Multilinear is not linear

The product \( V \times W \) is itself a vector space, with \( (\v, \w) + (\v', \w') = (\v + \v', \w + \w') \) and \( c(\v, \w) = (c\v, c\w) \) (@def-product-of-spaces). So a function \( \beta \colon V \times W \to Z \) has two different conditions it might satisfy, and they are stated on the same domain. They are not the same condition, and confusing them is the standard first error with tensors.

Side by side, for \( \beta \colon V \times W \to Z \):

- **Linear on the product** means \( \beta\bigl((\v, \w) + (\v', \w')\bigr) = \beta(\v, \w) + \beta(\v', \w') \) and \( \beta(c\v, c\w) = c\,\beta(\v,\w) \). Both slots move together.
- **Bilinear** means \( \beta(\v + \v', \w) = \beta(\v, \w) + \beta(\v', \w) \), and the same in the second slot with the first frozen. One slot moves at a time.

::: {.warning}
**Do not add in both slots at once.** For a bilinear \( \beta \), the correct expansion has **four** terms:
\[
\beta(\v + \v', \w + \w') = \beta(\v, \w) + \beta(\v, \w') + \beta(\v', \w) + \beta(\v', \w').
\]
Concretely, with \( \beta(a, b) = ab \) on \( F \times F \): \( \beta(1 + 1, 1 + 1) = 4 \), not \( \beta(1,1) + \beta(1,1) = 2 \). Scaling is worse: \( \beta(c\v, c\w) = c^2\beta(\v, \w) \), so a bilinear map scales by the **square**. Pull out scalars one slot at a time, always.
:::

::: {.check}
Is \( \beta(\x, \y) = x_1y_1 + x_2 \) a bilinear map \( F^2 \times F^2 \to F \)?
:::

::: {.solution}
No. Freeze \( \y \). Then \( \x \mapsto y_1x_1 + x_2 \) is a linear functional, so the first slot is fine. Freeze \( \x = \e_2 \). Then \( \y \mapsto 0 \cdot y_1 + 1 = 1 \) is the constant function \( 1 \), which sends \( \0 \) to \( 1 \) and so is not linear. The clause that fails is "is linear" at position \( i = 2 \). The extra summand \( x_2 \) does not involve \( \y \) at all, and a bilinear map must vanish whenever an argument is \( \0 \).
:::

## Values on basis tuples

A linear map may be prescribed arbitrarily on a basis and is determined by those values (@thm-linear-map-from-any-basis). The corresponding statement for multilinear maps replaces "basis vectors" by "tuples of basis vectors, one from each slot", and the proof is the expansion identity above read in both directions.

::: {#thm-multilinear-determined-by-basis}
[Multilinear Maps from Values on Basis Tuples]

Let \( V_1, \dots, V_k \) be finite-dimensional, with ordered bases \( \sB_i = (\v^{(i)}_1, \dots, \v^{(i)}_{n_i}) \) for \( i = 1, \dots, k \), and let \( W \) be any vector space over \( F \). For every family of vectors
\[
\w_{i_1 i_2 \dots i_k} \in W, \qquad 1 \le i_1 \le n_1, \ \dots, \ 1 \le i_k \le n_k,
\]
there is **exactly one** \( k \)-linear map \( \beta \colon V_1 \times \cdots \times V_k \to W \) with \( \beta(\v^{(1)}_{i_1}, \dots, \v^{(k)}_{i_k}) = \w_{i_1 \dots i_k} \) for every tuple of indices.
:::

::: {.idea}
Uniqueness is the expansion identity: write each argument in its basis, expand one slot at a time, and every value of \( \beta \) is a combination of the prescribed ones. For existence we need a formula, and the coefficients in that expansion are exactly the coordinates, which @thm-dual-basis supplies as linear functionals. So multiply the right functionals together and use them as coefficients.
:::

::: {.proof}
*Uniqueness.* Let \( \beta \) and \( \beta' \) be \( k \)-linear with the same values on all basis tuples, and let \( \x_i \in V_i \). Write \( \x_i = \sum_{j} a^{(i)}_{j}\v^{(i)}_{j} \). Expanding each slot in turn by @def-multilinear-map,
\[
\beta(\x_1, \dots, \x_k) = \sum_{i_1, \dots, i_k} a^{(1)}_{i_1}\cdots a^{(k)}_{i_k}\, \w_{i_1 \dots i_k},
\]
and the same computation applies to \( \beta' \). Hence \( \beta = \beta' \).

*Existence.* For each \( i \), let \( (\varphi^{(i)}_1, \dots, \varphi^{(i)}_{n_i}) \) be the basis of \( V_i^{*} \) dual to \( \sB_i \), so that \( \varphi^{(i)}_{a}(\v^{(i)}_{b}) = \delta_{ab} \) and \( \varphi^{(i)}_{j}(\x) \) is the \( j \)-th coordinate of \( \x \) (@thm-dual-basis). Define
\[
\beta(\x_1, \dots, \x_k) \coloneqq \sum_{i_1, \dots, i_k} \varphi^{(1)}_{i_1}(\x_1)\cdots\varphi^{(k)}_{i_k}(\x_k)\, \w_{i_1 \dots i_k},
\]
a finite sum of vectors of \( W \), so a well-defined element of \( W \).

It is \( k \)-linear: freeze every slot but the \( m \)-th. Each summand is then the vector \( \w_{i_1 \dots i_k} \) multiplied by a fixed scalar times \( \varphi^{(m)}_{i_m}(\x_m) \), and \( \varphi^{(m)}_{i_m} \) is linear; a finite sum of linear functions of \( \x_m \), each scaled by a fixed vector, is linear in \( \x_m \). This holds for every \( m \), which is the condition of @def-multilinear-map.

Its values are the prescribed ones: at \( \x_i = \v^{(i)}_{j_i} \) the coefficient \( \varphi^{(1)}_{i_1}(\v^{(1)}_{j_1})\cdots\varphi^{(k)}_{i_k}(\v^{(k)}_{j_k}) \) is \( 1 \) when \( i_1 = j_1, \dots, i_k = j_k \) and \( 0 \) otherwise, so only the term \( \w_{j_1 \dots j_k} \) survives. This proves the theorem.
:::

So a multilinear map is "nothing but" a family of vectors of \( W \) indexed by tuples of basis indices, exactly as a linear map is nothing but a family indexed by single basis indices. The count of tuples is where the product in the next theorem comes from.

## The space of multilinear maps

Two multilinear maps with the same slots and the same target can be added and scaled pointwise, and the results are again multilinear. That makes them a vector space, and we name it before counting it.

::: {#def-space-of-multilinear-maps}
[The Space of Multilinear Maps]

Let \( V_1, \dots, V_k \) and \( W \) be vector spaces over \( F \). Write
\[
\cM(V_1, \dots, V_k; W)
\]
for the set of all \( k \)-linear maps \( V_1 \times \cdots \times V_k \to W \), with the **pointwise** operations
\[
(\beta + \gamma)(\x_1, \dots, \x_k) \coloneqq \beta(\x_1, \dots, \x_k) + \gamma(\x_1, \dots, \x_k),
\]
and \( (c\beta)(\x_1, \dots, \x_k) \coloneqq c\,\beta(\x_1, \dots, \x_k) \). The semicolon separates the inputs from the output.
:::

**Well-definedness.** The set of *all* functions \( V_1 \times \cdots \times V_k \to W \) is a vector space under the pointwise operations, by the argument of @exm-vector-spaces (d) with \( F \) replaced by \( W \): two functions are equal when they agree at every point, so each axiom is checked one point at a time and reduces to the corresponding axiom in \( W \). Inside it, \( \cM(V_1, \dots, V_k; W) \) passes @thm-subspace-test. The zero function is \( k \)-linear, since freezing slots leaves the zero map. If \( \beta, \gamma \) are \( k \)-linear and \( c \in F \), then freezing all slots but the \( m \)-th turns \( \beta + \gamma \) and \( c\beta \) into a sum and a scalar multiple of linear maps \( V_m \to W \), which are linear by @thm-linear-maps-vector-space. So \( \cM(V_1, \dots, V_k; W) \) is a subspace, hence a vector space.

Two special cases are old friends. For \( k = 1 \), \( \cM(V; W) = \cL(V, W) \) by @exm-multilinear-maps-first (a). For \( W = F \), the elements are the multilinear forms of @def-multilinear-form; Chapter 7 wrote the space of alternating \( n \)-linear forms on \( F^n \) and proved it one-dimensional (@cor-alternating-forms-one-dimensional), which is a subspace of \( \cM(F^n, \dots, F^n; F) \).

::: {#thm-multilinear-maps-dimension}
[Dimension of the Space of Multilinear Maps]

Let \( V_1, \dots, V_k \) and \( W \) be finite-dimensional, with \( \dim V_i = n_i \) and \( \dim W = m \). Then \( \cM(V_1, \dots, V_k; W) \) is finite-dimensional, of dimension

\[
\dim \cM(V_1, \dots, V_k; W) = (\dim W)\prod_{i=1}^{k} \dim V_i = m\,n_1n_2\cdots n_k .
\]{#eq-multilinear-dimension}

Explicitly, fix bases \( \sB_i \) of \( V_i \) with dual bases \( (\varphi^{(i)}_j) \), and a basis \( (\w_1, \dots, \w_m) \) of \( W \). For a tuple \( I = (i_1, \dots, i_k) \) and an index \( r \), let
\[
E^{r}_{I}(\x_1, \dots, \x_k) \coloneqq \varphi^{(1)}_{i_1}(\x_1)\cdots\varphi^{(k)}_{i_k}(\x_k)\,\w_r .
\]
The \( m\,n_1\cdots n_k \) maps \( E^{r}_{I} \) form a basis of \( \cM(V_1, \dots, V_k; W) \).
:::

::: {.idea}
@thm-multilinear-determined-by-basis says a multilinear map is the same thing as a list of vectors of \( W \), one per index tuple. So count the lists: there are \( n_1\cdots n_k \) tuples and each entry needs \( m \) coordinates. The maps \( E^r_I \) are the maps whose list has a single \( \w_r \) in position \( I \) and zeros elsewhere, which is why they should be the basis.
:::

::: {.proof}
Each \( E^r_I \) is \( k \)-linear by the existence half of @thm-multilinear-determined-by-basis, being the map prescribed to take the value \( \w_r \) at the basis tuple \( (\v^{(1)}_{i_1}, \dots, \v^{(k)}_{i_k}) \) and \( \0 \) at every other basis tuple.

*Spanning.* Let \( \beta \in \cM(V_1, \dots, V_k; W) \). For each tuple \( I \) write its value on the corresponding basis tuple in the basis of \( W \):
\[
\beta(\v^{(1)}_{i_1}, \dots, \v^{(k)}_{i_k}) = \sum_{r=1}^{m} c_{I,r}\,\w_r ,
\]
which is possible, and with unique coefficients, since \( (\w_1, \dots, \w_m) \) is a basis. The map \( \sum_{I,r} c_{I,r}E^{r}_{I} \) is \( k \)-linear and takes exactly these values on the basis tuples. By the uniqueness half of @thm-multilinear-determined-by-basis it equals \( \beta \).

*Independence.* Suppose \( \sum_{I,r} c_{I,r}E^{r}_{I} = 0 \), the zero map. Evaluate at a basis tuple indexed by \( J \). By the displayed formula for \( E^r_I \), the coefficient \( \varphi^{(1)}_{i_1}(\v^{(1)}_{j_1})\cdots\varphi^{(k)}_{i_k}(\v^{(k)}_{j_k}) \) is \( 1 \) for \( I = J \) and \( 0 \) otherwise, so the value is \( \sum_{r} c_{J,r}\w_r = \0 \). Since \( (\w_r) \) is independent, \( c_{J,r} = 0 \) for every \( r \). As \( J \) was arbitrary, every coefficient vanishes.

Hence the \( E^r_I \) form a basis. There are \( n_1n_2\cdots n_k \) index tuples \( I \) and \( m \) choices of \( r \), so the count is \( m\,n_1\cdots n_k \), which is @eq-multilinear-dimension. This proves the theorem.
:::

**Aftermath.** Two sanity checks. With \( k = 1 \), @eq-multilinear-dimension reads \( \dim \cL(V, W) = (\dim W)(\dim V) \), which is @thm-linear-maps-isomorphic-to-matrices. With \( W = F \) and \( k = 2 \), it reads \( \dim \cM(V_1, V_2; F) = n_1n_2 \), which is the count of \( n_1 \times n_2 \) matrices — and indeed Chapter 14 recorded a bilinear form on a single space by its Gram matrix (@def-form-matrix). The \( n_i \) enter as a **product**, once per slot, and that is the number to remember.

::: {#exm-dimension-of-bilinear-maps}
[Counting bilinear maps]

::: {.enumerate options="label=(\alph*)"}
1. Find \( \dim \cM(F^2, F^3; F^2) \).
2. Find \( \dim \cM(F^3, F^3, F^3; F) \), and the dimension of the subspace of alternating forms inside it when \( F = \nR \).
3. Write the bilinear map \( \beta \colon F^2 \times F^2 \to F^2 \), \( \beta(\x, \y) = (x_1y_1,\ x_1y_2 + x_2y_1) \), in the basis of @thm-multilinear-maps-dimension for the standard bases.
:::
:::

::: {.solution}
(a) \( \dim W \cdot \dim V_1 \cdot \dim V_2 = 2 \cdot 2 \cdot 3 = 12 \).

(b) \( 1 \cdot 3 \cdot 3 \cdot 3 = 27 \). The alternating ones form a subspace of dimension \( 1 \) by @cor-alternating-forms-one-dimensional, spanned by the determinant. So alternation is a very strong condition: it cuts \( 27 \) down to \( 1 \).

(c) Here \( m = n_1 = n_2 = 2 \), so there are \( 2 \cdot 2 \cdot 2 = 8 \) basis maps \( E^{r}_{(i,j)} \), and \( E^{r}_{(i,j)}(\x, \y) = x_iy_j\e_r \). Evaluate \( \beta \) on the four basis pairs:
\[
\begin{aligned}
\beta(\e_1, \e_1) &= (1, 0) = \e_1, & \beta(\e_1, \e_2) &= (0, 1) = \e_2, \\
\beta(\e_2, \e_1) &= (0, 1) = \e_2, & \beta(\e_2, \e_2) &= (0, 0) = \0 .
\end{aligned}
\]
By the spanning argument, \( \beta = E^{1}_{(1,1)} + E^{2}_{(1,2)} + E^{2}_{(2,1)} \), with the other five coefficients zero. Reading the formula back, \( \beta(\x,\y) = x_1y_1\e_1 + x_1y_2\e_2 + x_2y_1\e_2 \), which is the given map.
:::

::: {.check}
What does @eq-multilinear-dimension give for \( \cM(V_1, V_2; W) \) when \( V_2 = \{\0\} \)? Does the answer make sense?
:::

::: {.solution}
It gives \( (\dim W) \cdot (\dim V_1) \cdot 0 = 0 \), so the space is \( \{0\} \). That is right: a bilinear map must satisfy \( \beta(\v, \0) = \0 \), and \( \0 \) is the only vector of \( V_2 \), so the only bilinear map is the zero map. The degenerate case is worth checking because it is where a formula with a product behaves differently from one with a sum.
:::

## The problem this chapter solves

We now have a good supply of multilinear maps and we know how many there are. What we do not have is any way to *work* with them. Consider what Chapters 2 to 5 give a linear map \( T \colon V \to W \): a matrix, a kernel, an image, a rank, Rank–Nullity, a dual map, a determinant when \( V = W \), eigenvalues, a Jordan form. A bilinear map \( \beta \colon V \times W \to Z \) has none of these. It has no matrix, because @def-matrix-of-linear-map applies to linear maps. It has no kernel that is a subspace: the set where \( \beta \) vanishes contains \( (\v, \0) \) and \( (\0, \w) \) for all \( \v, \w \) but usually not their sum. It is not an element of \( \cL(V \times W, Z) \), as the previous subsection insisted. Every fact we know about it has had to be proved by hand, one slot at a time.

The wish is therefore easy to state. **We want to replace multilinearity by linearity.** Concretely, for two spaces \( V \) and \( W \) we want a single vector space — call it \( X \) for now — and a single bilinear map \( \tau \colon V \times W \to X \), so universal that every bilinear map out of \( V \times W \) is \( \tau \) followed by a **linear** map. If that works, then bilinear maps \( V \times W \to Z \) correspond to linear maps \( X \to Z \), and the entire toolkit of Chapters 2 to 5 applies to the latter.

Before building anything, we can predict the size of \( X \), and the prediction is a good reason to believe the object exists. Suppose such an \( X \) and \( \tau \) existed, and suppose the correspondence "\( \beta \) on \( V \times W \) \( \leftrightarrow \) linear map on \( X \)" is a bijection for every target \( Z \). Take \( Z = F \). Then @eq-multilinear-dimension gives
\[
\dim \cM(V, W; F) = 1 \cdot \dim V \cdot \dim W,
\]
while @thm-linear-maps-isomorphic-to-matrices gives \( \dim \cL(X, F) = \dim X \). A bijection that respects addition and scalars forces these to agree, so
\[
\dim X = (\dim V)(\dim W).
\]
The product of the dimensions, not the sum. This already rules out the naive guess \( X = V \times W \), whose dimension is \( \dim V + \dim W \) by @thm-dimension-of-product, and it tells us what to aim for. The next section constructs \( X \), calls it \( V \otimes W \), and proves that its dimension is exactly this product.

One more remark before we go. The prediction used only the case \( Z = F \), but the same count works for every \( Z \): @eq-multilinear-dimension gives \( \dim Z \cdot \dim V \cdot \dim W \) on one side and \( \dim Z \cdot \dim X \) on the other, and the two agree precisely when \( \dim X = (\dim V)(\dim W) \). When the next section produces a basis of \( V \otimes W \) indexed by pairs \( (i, j) \) of basis indices, that is the same count seen a second time, and the agreement is not a coincidence — it is the universal property, counted.

## Exercises

### A. Check your understanding

::: {#exr-multilinear-maps-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define what it means for \( \beta \colon V_1 \times \cdots \times V_k \to W \) to be \( k \)-linear, with every quantifier.
2. State the difference between "\( \beta \) is bilinear" and "\( \beta \) is linear on the product space \( V \times W \)", and give a function that is one but not the other.
3. Write out \( \beta(\u + \u', \v + \v') \) for a bilinear \( \beta \). How many terms are there?
4. State \( \dim \cM(V_1, \dots, V_k; W) \) in terms of the dimensions of the spaces involved.
5. True or false: every bilinear map \( \beta \colon V \times W \to Z \) satisfies \( \beta(\v, \0) = \0 \). Justify your answer.
6. What is a \( 1 \)-linear map? What is a \( k \)-linear map with \( W = F \) called?
:::
:::

::: {.solution}
(a) It is \( k \)-linear if for **every** position \( i \) and **every** choice of fixed \( \v_j \in V_j \) with \( j \ne i \), the function \( \x \mapsto \beta(\v_1, \dots, \x, \dots, \v_k) \) with \( \x \) in position \( i \) is a linear map \( V_i \to W \) (@def-multilinear-map). All spaces are over the same field.

(b) Bilinear means linear in each slot with the other **frozen**; linear on the product means linear when both slots move **together**. The multiplication \( \beta(a, b) = ab \) on \( F \times F \) is bilinear but not linear on the product, since \( \beta(2 \cdot (1,1)) = 4 \ne 2\beta(1,1) \). The sum \( \sigma(a,b) = a + b \) is linear on the product but not bilinear, since \( a \mapsto a + 1 \) is not linear.

(c) \( \beta(\u, \v) + \beta(\u, \v') + \beta(\u', \v) + \beta(\u', \v') \): four terms.

(d) \( (\dim W)\prod_{i=1}^{k}\dim V_i \) (@eq-multilinear-dimension).

(e) True. Freeze \( \v \); the map \( \y \mapsto \beta(\v, \y) \) is linear, and a linear map sends \( \0 \) to \( \0 \) by @thm-zero-maps-to-zero.

(f) A \( 1 \)-linear map is exactly a linear map. A \( k \)-linear map into \( F \) is a multilinear form (@def-multilinear-form).
:::

### B. Practice

::: {#exr-multilinear-maps-b1}
[B1: Determine which are multilinear]

Determine which of the following are multilinear maps. For those that are, say what \( k \) is; for those that are not, name the clause that fails and give a concrete witness. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \beta \colon M_n(F) \times M_n(F) \to M_n(F) \), \( \beta(\A, \B) = \A\B - \B\A \).
2. \( \beta \colon \nR^2 \times \nR^2 \to \nR \), \( \beta(\x, \y) = x_1y_2 - x_2y_1 + 1 \).
3. \( \beta \colon F^n \times F^n \to M_n(F) \), \( \beta(\x, \y) = \x\y\tp \).
4. \( \beta \colon M_n(F) \times M_n(F) \to F \), \( \beta(\A, \B) = \det(\A\B) \), for \( n \ge 2 \).
5. \( \beta \colon V^{*} \times V^{*} \times V \times V \to F \), \( \beta(\varphi, \psi, \u, \v) = \varphi(\u)\psi(\v) \).
:::
:::

::: {.solution}
(a) Bilinear, \( k = 2 \). This is the commutator \( [\A, \B] \) of @def-commutator. Freeze \( \B \): then \( \A \mapsto \A\B - \B\A \) is a difference of two linear maps of \( \A \), hence linear (@thm-linear-maps-vector-space). Freezing \( \A \) is the same computation.

(b) Not multilinear. Freeze \( \y = \0 \); then \( \x \mapsto 1 \) is constant, so it sends \( \0 \) to \( 1 \) and the clause "is linear" fails at position \( 1 \). Removing the \( +1 \) leaves the signed area, which is bilinear.

(c) Bilinear, \( k = 2 \). The \( (i, j) \) entry of \( \x\y\tp \) is \( x_iy_j \). Freeze \( \y \): each entry is a linear functional of \( \x \) and the entries are the coordinates of the output in the basis of matrix units, so \( \x \mapsto \x\y\tp \) is linear. Symmetrically in \( \y \). This map will reappear as the model of the tensor product of two coordinate spaces.

(d) Not multilinear for \( n \ge 2 \). By @thm-det-multiplicative, \( \beta(\A, \B) = \det\A\,\det\B \). Freeze \( \B = \I_n \); then \( \A \mapsto \det \A \) is not linear, since \( \det(c\A) = c^n\det\A \) and \( n \ge 2 \). Concretely with \( n = 2 \), \( \det(2\I_2) = 4 \ne 2\det \I_2 = 2 \). The failing clause is again "is linear".

(e) \( 4 \)-linear. Freeze three of the four arguments; in each case what remains is one of \( \varphi \mapsto \varphi(\u) \cdot \psi(\v) \), \( \psi \mapsto \psi(\v)\cdot\varphi(\u) \), \( \u \mapsto \varphi(\u)\cdot\psi(\v) \), \( \v \mapsto \psi(\v)\cdot\varphi(\u) \), each a fixed scalar times a linear functional, hence linear. Note that the four slots do **not** all lie in the same space, which @def-multilinear-map allows and @def-multilinear-form does not.
:::

::: {#exr-multilinear-maps-b2}
[B2: Dimension counts]

Compute the dimension of each space. The field is \( F \) throughout.

::: {.enumerate options="label=(\alph*)"}
1. \( \cM(F^4, F^5; F^3) \).
2. \( \cM(F^2, F^2, F^2; F^2) \).
3. \( \cM(M_2(F), F^3; F) \).
4. \( \cM(F^n; W) \) for \( \dim W = m \), and the space \( \cL(F^n, W) \). Compare.
:::
:::

::: {.solution}
(a) \( 3 \cdot 4 \cdot 5 = 60 \) by @eq-multilinear-dimension.

(b) \( 2 \cdot 2 \cdot 2 \cdot 2 = 16 \).

(c) \( \dim M_2(F) = 4 \), so \( 1 \cdot 4 \cdot 3 = 12 \).

(d) Both are \( mn \). With \( k = 1 \) the two spaces are equal, by @exm-multilinear-maps-first (a), and @eq-multilinear-dimension reduces to @thm-linear-maps-isomorphic-to-matrices. The formula is consistent with what Chapter 2 already proved.
:::

::: {#exr-multilinear-maps-b3}
[B3: Expanding in the basis]

Let \( \beta \colon F^2 \times F^3 \to F^2 \) be given by
\[
\beta(\x, \y) = (x_1y_1 - 2x_2y_3,\ x_1y_2 + x_2y_1).
\]

::: {.enumerate options="label=(\alph*)"}
1. Verify that \( \beta \) is bilinear.
2. Compute the six values \( \beta(\e_i, \f_j) \), where \( (\e_1, \e_2) \) and \( (\f_1, \f_2, \f_3) \) are the standard bases.
3. Write \( \beta \) in the basis \( \{E^{r}_{(i,j)}\} \) of @thm-multilinear-maps-dimension, and say how many of the \( 12 \) coefficients are non-zero.
:::
:::

::: {.solution}
(a) Freeze \( \y \). Each output coordinate is a fixed linear combination of \( x_1 \) and \( x_2 \), hence a linear functional of \( \x \) (@thm-functionals-on-fn), and a map into \( F^2 \) whose coordinates are linear is linear. Freeze \( \x \): each output coordinate is a fixed linear combination of \( y_1, y_2, y_3 \), and the same argument applies. So \( \beta \) is bilinear.

(b) Substituting the standard basis vectors:
\[
\begin{aligned}
\beta(\e_1, \f_1) &= (1, 0), & \beta(\e_1, \f_2) &= (0, 1), & \beta(\e_1, \f_3) &= (0, 0), \\
\beta(\e_2, \f_1) &= (0, 1), & \beta(\e_2, \f_2) &= (0, 0), & \beta(\e_2, \f_3) &= (-2, 0).
\end{aligned}
\]

(c) Reading the coordinates off, \( c_{(1,1),1} = 1 \), \( c_{(1,2),2} = 1 \), \( c_{(2,1),2} = 1 \) and \( c_{(2,3),1} = -2 \), all others zero. Hence
\[
\beta = E^{1}_{(1,1)} + E^{2}_{(1,2)} + E^{2}_{(2,1)} - 2\,E^{1}_{(2,3)},
\]
so \( 4 \) of the \( 2 \cdot 2 \cdot 3 = 12 \) coefficients are non-zero.
:::

### C. Going deeper

::: {#exr-multilinear-maps-c1}
[C1: Bilinear forms on coordinate spaces are matrices]

Let \( m, n \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that for every bilinear \( \beta \colon F^m \times F^n \to F \) there is a **unique** \( \A \in M_{m \times n}(F) \) with \( \beta(\x, \y) = \x\tp\A\y \) for all \( \x, \y \).
2. Hence deduce that \( \dim \cM(F^m, F^n; F) = mn \), and check that this agrees with @eq-multilinear-dimension.
:::

*Hint for (a): the entries of \( \A \) can only be the values of \( \beta \) on pairs of standard basis vectors.*
:::

::: {.solution}
(a) *Existence.* Put \( a_{ij} \coloneqq \beta(\e_i, \f_j) \), where \( (\e_i) \) and \( (\f_j) \) are the standard bases of \( F^m \) and \( F^n \), and let \( \A = (a_{ij}) \). For \( \x = \sum_i x_i\e_i \) and \( \y = \sum_j y_j\f_j \), expanding one slot at a time by @def-multilinear-map gives
\[
\beta(\x, \y) = \sum_{i, j} x_iy_j\,\beta(\e_i, \f_j) = \sum_{i,j} x_ia_{ij}y_j = \x\tp\A\y .
\]

*Uniqueness.* If \( \x\tp\A\y = \x\tp\A'\y \) for all \( \x, \y \), take \( \x = \e_i \) and \( \y = \f_j \): the left side is \( a_{ij} \) and the right side is \( a'_{ij} \). Hence \( \A = \A' \).

(b) By (a) the map \( \cM(F^m, F^n; F) \to M_{m \times n}(F) \), \( \beta \mapsto \A \), is a bijection, and it is linear because the entries \( \beta(\e_i, \f_j) \) depend linearly on \( \beta \) by the definition of the pointwise operations. So it is an isomorphism, and \( \dim \cM(F^m, F^n; F) = \dim M_{m\times n}(F) = mn \) by @thm-isomorphic-iff-same-dimension. @eq-multilinear-dimension gives \( 1 \cdot m \cdot n = mn \), the same value.
:::

::: {#exr-multilinear-maps-c2}
[C2: Linear and bilinear at once]

Let \( V, W, Z \) be vector spaces over \( F \) and let \( \beta \colon V \times W \to Z \) be a function.

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( \beta \) is **both** bilinear and linear as a map on the product space \( V \times W \), then \( \beta \) is the zero map.
2. Give an example, with \( V = W = Z = F \), of a non-zero bilinear map and a non-zero linear map on the product, and say which property each one fails.
3. Does (a) still hold when \( V = \{\0\} \)? Explain what the statement says in that case.
:::
:::

::: {.solution}
(a) Let \( \v \in V \) and \( \w \in W \). In the product space, \( (\v, \w) = (\v, \0) + (\0, \w) \). Since \( \beta \) is linear on the product,
\[
\beta(\v, \w) = \beta(\v, \0) + \beta(\0, \w).
\]
Since \( \beta \) is bilinear, freezing the first slot at \( \v \) makes \( \y \mapsto \beta(\v, \y) \) linear, so \( \beta(\v, \0) = \0 \) by @thm-zero-maps-to-zero; freezing the second slot at \( \w \) gives \( \beta(\0, \w) = \0 \) likewise. Therefore \( \beta(\v, \w) = \0 \) for all \( \v, \w \), that is, \( \beta = 0 \).

(b) The product \( \mu(a, b) = ab \) is bilinear and fails linearity on the product, since \( \mu(2 \cdot (1,1)) = 4 \ne 2\mu(1,1) \). The sum \( \sigma(a, b) = a + b \) is linear on the product and fails bilinearity, since \( \sigma(0, 1) = 1 \ne 0 \) while a bilinear map must vanish when a slot is \( \0 \).

(c) Yes, but it says nothing: if \( V = \{\0\} \) then \( \v = \0 \) always, and the only function \( \{\0\} \times W \to Z \) that is bilinear is already the zero map, since \( \beta(\0, \w) = \0 \). The content of (a) appears only when both \( V \) and \( W \) are non-zero and \( Z \ne \{\0\} \).
:::

::: {#exr-multilinear-maps-c3}
[C3: Counting over a finite field]

Work over \( \nF_2 \), the field with two elements.

::: {.enumerate options="label=(\alph*)"}
1. How many bilinear maps \( \nF_2^2 \times \nF_2^2 \to \nF_2 \) are there? How many trilinear maps \( \nF_2^2 \times \nF_2^2 \times \nF_2^2 \to \nF_2 \)?
2. How many of the bilinear maps in (a) are symmetric, that is, satisfy \( \beta(\x, \y) = \beta(\y, \x) \) for all \( \x, \y \)? How many are alternating in the sense of @def-alternating-form?
3. Is every alternating bilinear form on \( \nF_2^2 \) symmetric? Is every symmetric one alternating?
:::
:::

::: {.solution}
(a) By @eq-multilinear-dimension, \( \dim \cM(\nF_2^2, \nF_2^2; \nF_2) = 1 \cdot 2 \cdot 2 = 4 \). A vector space of dimension \( d \) over \( \nF_2 \) has exactly \( 2^d \) elements, since each of the \( d \) coordinates is \( 0 \) or \( 1 \). So there are \( 2^4 = 16 \) bilinear maps. For three slots the dimension is \( 2^3 = 8 \), giving \( 2^8 = 256 \) trilinear maps.

(b) By @exr-multilinear-maps-c1 a bilinear form on \( \nF_2^2 \) is \( \x\tp\A\y \) for a unique \( \A \in M_2(\nF_2) \), and \( \beta \) is symmetric exactly when \( \A = \A\tp \) (compare the values at \( (\e_i, \e_j) \) and \( (\e_j, \e_i) \)). A symmetric \( 2 \times 2 \) matrix is determined by \( a_{11}, a_{12}, a_{22} \), so there are \( 2^3 = 8 \) symmetric ones. Alternating means \( \beta(\x, \x) = 0 \) for all \( \x \), which forces \( a_{11} = \beta(\e_1,\e_1) = 0 \), \( a_{22} = 0 \), and then \( \beta(\e_1 + \e_2, \e_1 + \e_2) = a_{12} + a_{21} = 0 \). Over \( \nF_2 \) that says \( a_{21} = a_{12} \), so \( \A = \begin{psmallmatrix} 0 & a \\ a & 0\end{psmallmatrix} \) and there are \( 2 \) alternating forms: the zero form and the signed area.

(c) Both alternating forms found in (b) have symmetric matrices, so yes, every alternating form here is symmetric — which is @thm-alternating-vs-skew in characteristic \( 2 \), where \( -1 = 1 \). The converse fails: the dot product \( \beta(\x, \y) = x_1y_1 + x_2y_2 \) is symmetric, and \( \beta(\e_1, \e_1) = 1 \ne 0 \), so it is not alternating. Of the \( 8 \) symmetric forms only \( 2 \) are alternating.
:::
