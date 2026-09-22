# Three Kinds of Form

A bilinear form has two slots, and so far nothing has related them. Almost every form that occurs in practice does relate them: the dot product does not care which vector goes first, while the determinant of a \( 2 \times 2 \) matrix changes sign when its columns are swapped. This section names the three symmetry conditions the rest of the chapter runs on, shows that two of them are the same condition exactly when \( 1 + 1 \ne 0 \) in the field, and extracts from a symmetric form the single-variable function \( q(\v) = \beta(\v, \v) \) that carries all of its information.

Throughout, \( V \) is a finite-dimensional vector space over a field \( F \), and \( \beta \) is a bilinear form on \( V \) (@def-bilinear-form). The characteristic hypothesis is stated wherever it is needed and nowhere else.

## Symmetric forms

The dot product on \( F^n \) satisfies \( \x \cdot \y = \y \cdot \x \), and so does every integral pairing \( \int_0^1 fg \), and so does \( \x\tp\A\y \) whenever \( \A \) happens to satisfy \( \A\tp = \A \). The condition recurs, so it gets a name.

*A symmetric form cannot tell its two arguments apart.*

::: {#def-symmetric-form}
[Symmetric Bilinear Form]

A bilinear form \( \beta \colon V \times V \to F \) is **symmetric** if
\[
\beta(\u, \v) = \beta(\v, \u)
\]
**for all** \( \u, \v \in V \).
:::

In words: the value is unchanged by swapping the two inputs. The condition is imposed for **every** pair, not just for pairs of basis vectors — although, as the next result shows, checking it on basis vectors is enough.

Three examples and one non-example.

- **The dot product** on \( F^n \), \( \beta(\x, \y) = x_1y_1 + \dots + x_ny_n \). Each product \( x_iy_i \) is unchanged by the swap because multiplication in \( F \) is commutative.
- **A symmetric matrix**, \( \beta(\x, \y) = \x\tp\A\y \) with \( \A\tp = \A \) (@def-symmetric-matrix). Here \( \x\tp\A\y \) is a \( 1 \times 1 \) matrix, so it equals its own transpose \( \y\tp\A\tp\x = \y\tp\A\x \) by @thm-transpose-properties.
- **Evaluation pairings.** On \( F[x]_{\le n} \), fix scalars \( t_1, \dots, t_k \in F \) and set \( \beta(p, q) = \sum_i p(t_i)q(t_i) \). Symmetry is again commutativity of \( F \).
- **A non-example by minimal change.** On \( F^2 \) put \( \beta(\x, \y) = x_1y_2 \). It is bilinear, by the one-slot check of @def-multilinear-form. But \( \beta(\e_1, \e_2) = 1 \) and \( \beta(\e_2, \e_1) = 0 \), so the symmetry clause fails at that one pair. Exactly one clause has been broken: bilinearity survives untouched.

The matrix of a form (@def-form-matrix) turns the condition into a matrix condition, and turns "for all \( \u, \v \)" into a finite check.

::: {#prp-form-symmetry-matrix}
[Symmetry Is Visible in the Matrix]

Let \( \sB \) be a basis of \( V \) and \( \A = \mtx{\beta}{\sB}{\sB} \). Then \( \beta \) is symmetric if and only if \( \A\tp = \A \).
:::

::: {.proof}
\( (\Rightarrow) \) Suppose \( \beta \) is symmetric. Writing \( \sB = (\v_1, \dots, \v_n) \), the entries of \( \A \) are \( a_{ij} = \beta(\v_i, \v_j) \), so \( a_{ij} = \beta(\v_j, \v_i) = a_{ji} \), which is @def-symmetric-matrix.

\( (\Leftarrow) \) Suppose \( \A\tp = \A \), and let \( \u, \v \in V \). By @thm-form-matrix-determines,
\[
\beta(\u, \v) = \coord{\u}{\sB}\tp \A \coord{\v}{\sB} .
\]
The right-hand side is a \( 1 \times 1 \) matrix, hence equal to its transpose, which by @thm-transpose-properties is \( \coord{\v}{\sB}\tp \A\tp \coord{\u}{\sB} = \coord{\v}{\sB}\tp \A \coord{\u}{\sB} = \beta(\v, \u) \). This proves the equivalence.
:::

Because congruence sends \( \A \) to \( \P\tp\A\P \) and \( (\P\tp\A\P)\tp = \P\tp\A\tp\P \) by @thm-transpose-properties, a congruent copy of a symmetric matrix is symmetric. So the condition \( \A\tp = \A \) does not depend on which basis was used to build \( \A \) — as it must not, since by @prp-form-symmetry-matrix it says something about \( \beta \) alone.

## Alternating and skew-symmetric forms

Chapter 6 needed two ways of saying "the value collapses when two arguments coincide", and found that they are not the same condition. Both were defined there for \( k \)-linear forms, and a bilinear form is the case \( k = 2 \), so nothing needs redefining. Read at \( k = 2 \):

- \( \beta \) is **alternating** (@def-alternating-form) if \( \beta(\v, \v) = 0 \) for **every** \( \v \in V \);
- \( \beta \) is **skew-symmetric** (@def-skew-symmetric-form) if \( \beta(\u, \v) = -\beta(\v, \u) \) for **all** \( \u, \v \in V \).

The standard example of both is the signed area \( \beta(\x, \y) = x_1y_2 - x_2y_1 \) on \( F^2 \), which is the determinant of the matrix with columns \( \x \) and \( \y \). A second family, the one Section 9 will be about, is the **standard alternating form** on \( F^{2m} \),
\[
\beta(\x, \y) = \sum_{i=1}^{m}\bigl(x_iy_{m+i} - x_{m+i}y_i\bigr),
\]
which pairs the first block of coordinates against the second.

Each condition reads off the matrix, and the two readings differ by the diagonal.

::: {#prp-alternating-form-matrix}
[Alternation and Skewness in the Matrix]

Let \( \sB = (\v_1, \dots, \v_n) \) be a basis of \( V \) and \( \A = \mtx{\beta}{\sB}{\sB} \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \beta \) is skew-symmetric if and only if \( \A\tp = -\A \);
2. \( \beta \) is alternating if and only if \( \A\tp = -\A \) **and** \( a_{ii} = 0 \) for every \( i \).
:::
:::

::: {.proof}
(a) repeats the proof of @prp-form-symmetry-matrix with a minus sign throughout.

(b) \( (\Rightarrow) \) If \( \beta \) is alternating then \( a_{ii} = \beta(\v_i, \v_i) = 0 \), and \( \beta \) is skew-symmetric by @thm-alternating-properties (a), so \( \A\tp = -\A \) by (a).

\( (\Leftarrow) \) Suppose \( \A\tp = -\A \) with zero diagonal, and let \( \v \in V \) have coordinates \( \coord{\v}{\sB} = (c_1, \dots, c_n) \). By @thm-form-matrix-determines and bilinearity,
\[
\beta(\v, \v) = \sum_{i, j} c_ic_j a_{ij}
= \sum_{i} c_i^2 a_{ii} + \sum_{i < j} c_ic_j\bigl(a_{ij} + a_{ji}\bigr),
\]
where the second sum collects the terms \( (i, j) \) and \( (j, i) \) together. Every \( a_{ii} \) is \( 0 \), and every \( a_{ij} + a_{ji} \) is \( 0 \) because \( \A\tp = -\A \). So \( \beta(\v, \v) = 0 \). This proves the equivalence.
:::

Part (b) is the whole difficulty in one line: a skew-symmetric matrix has \( a_{ii} = -a_{ii} \), and *usually* that forces \( a_{ii} = 0 \). Usually, but not always.

## Where characteristic 2 earns its keep

Chapter 0 warned that in a field of characteristic \( 2 \) the argument "\( x = -x \), so \( 2x = 0 \), so \( x = 0 \)" divides by \( 2 = 1 + 1 \), which is \( 0 \) there, and it promised that this is why later results on symmetric bilinear forms would carry the hypothesis "characteristic \( \ne 2 \)" (@def-characteristic). This is the theorem the promise was about.

::: {#thm-alternating-vs-skew}
[Alternating Versus Skew-Symmetric]

Let \( F \) be a field and let \( V \) be a vector space over \( F \).

::: {.enumerate options="label=(\alph*)"}
1. Every alternating bilinear form on \( V \) is skew-symmetric. No hypothesis on \( F \) or on \( V \) is needed.
2. If \( \operatorname{char} F \ne 2 \), every skew-symmetric bilinear form on \( V \) is alternating. Again \( V \) is arbitrary.
3. If \( \operatorname{char} F = 2 \) and \( V \ne \{\0\} \), there is a skew-symmetric bilinear form on \( V \) that is **not** alternating.
:::

So the converse of (a) holds **if and only if** \( \operatorname{char} F \ne 2 \).
:::

::: {.idea}
For (a), feed \( \u + \v \) into both slots and expand: the two diagonal terms vanish by hypothesis, and what is left is exactly the skew identity. For (b), feed \( \v \) into both slots of the skew identity, which gives \( \beta(\v,\v) = -\beta(\v,\v) \); canceling needs \( 1 + 1 \) to be invertible, and that is precisely what characteristic \( \ne 2 \) supplies. For (c), notice that in characteristic \( 2 \) the words "skew-symmetric" and "symmetric" mean the same thing, so any symmetric form that is non-zero on some vector **paired with itself** is a witness — and the dot product is one.
:::

::: {.proof}
(a) Let \( \beta \) be alternating and let \( \u, \v \in V \). Expanding by bilinearity,
\[
0 = \beta(\u + \v, \u + \v)
= \beta(\u,\u) + \beta(\u,\v) + \beta(\v,\u) + \beta(\v,\v),
\]
and the first and last terms are \( 0 \) because \( \beta \) is alternating. Hence \( \beta(\u,\v) = -\beta(\v,\u) \). (This is @thm-alternating-properties (a) at \( k = 2 \).)

(b) Let \( \beta \) be skew-symmetric and \( \v \in V \). Taking \( \u = \v \) in the defining identity gives \( \beta(\v,\v) = -\beta(\v,\v) \), that is, \( (1 + 1)\beta(\v,\v) = 0 \). Since \( \operatorname{char} F \ne 2 \), we have \( 1 + 1 \ne 0 \) in \( F \): otherwise the smallest positive \( n \) with \( n \cdot 1 = 0 \) would be \( 2 \), which is @def-characteristic. A non-zero element of a field is invertible, so multiplying by \( (1+1)^{-1} \) gives \( \beta(\v,\v) = 0 \). (This is @thm-skew-symmetric-alternating at \( k = 2 \).)

(c) Suppose \( \operatorname{char} F = 2 \), so that \( -1 = 1 \) in \( F \). Since \( V \ne \{\0\} \) is finite-dimensional, it has a basis with at least one vector, and we may take \( \varphi \in V^{*} \) to be the coordinate functional of its first vector \( \v_1 \), so that \( \varphi(\v_1) = 1 \). Define
\[
\beta(\u, \v) = \varphi(\u)\,\varphi(\v) .
\]
This is bilinear, being a product of two linear functionals, and it is symmetric. Because \( -1 = 1 \), symmetric and skew-symmetric say the same thing, so \( \beta \) is skew-symmetric. But \( \beta(\v_1, \v_1) = 1 \ne 0 \), so \( \beta \) is not alternating.

Finally, (b) and (c) together say that the converse of (a) holds exactly when \( \operatorname{char} F \ne 2 \). This proves the theorem.
:::

The concrete witness is worth writing down.

::: {#exm-char-two-dot-product}
[The dot product over the field with two elements]

Let \( F = \nF_2 \) and \( V = \nF_2^2 \), and let \( \beta \) be the dot product, \( \beta(\x, \y) = x_1y_1 + x_2y_2 \). Decide whether \( \beta \) is symmetric, skew-symmetric and alternating, and compute the function \( \v \mapsto \beta(\v,\v) \) on all four vectors of \( V \).
:::

::: {.solution}
The matrix of \( \beta \) in the standard basis is \( \I_2 \). It is symmetric, so \( \beta \) is symmetric by @prp-form-symmetry-matrix. Over \( \nF_2 \) we have \( -\I_2 = \I_2 \), so the matrix also satisfies \( \I_2\tp = -\I_2 \), and \( \beta \) is skew-symmetric by @prp-alternating-form-matrix (a). It is **not** alternating: the diagonal entries of \( \I_2 \) are \( 1 \ne 0 \), and indeed \( \beta(\e_1, \e_1) = 1 \).

On the four vectors, \( \beta(\v,\v) = v_1^2 + v_2^2 \). In \( \nF_2 \) both elements satisfy \( c^2 = c \), so this equals \( v_1 + v_2 \):
\[
\beta(\0,\0) = 0, \quad \beta(\e_1,\e_1) = 1, \quad \beta(\e_2,\e_2) = 1, \quad \beta(\1,\1) = 0 .
\]
Notice what that list is: the function \( \v \mapsto \beta(\v,\v) \) is the **linear** functional \( v_1 + v_2 \). In characteristic \( 2 \) a "quadratic" function coming from a bilinear form can be linear, which is the first sign that the notions below will not behave.
:::

::: {.warning}
**In characteristic \( 2 \), "skew-symmetric" carries no information beyond "symmetric".** Since \( -1 = 1 \), the two conditions are literally the same condition, and the useful notion is the strictly stronger one, alternating. This is why Chapter 6 built the determinant on alternation rather than skewness, and why every statement below that pairs symmetric against alternating needs \( \operatorname{char} F \ne 2 \).
:::

## Splitting a form into two halves

In characteristic \( \ne 2 \) the two conditions are complementary in the strongest possible sense: every bilinear form is a symmetric one plus an alternating one, in exactly one way. The recipe is the one that splits a function on \( \nR \) into its even and odd parts.

::: {#thm-symmetric-alternating-decomposition}
[Symmetric Plus Alternating]

Let \( \operatorname{char} F \ne 2 \) and let \( \beta \) be a bilinear form on \( V \). Then there are a **unique** symmetric form \( \beta_{s} \) and a **unique** alternating form \( \beta_{a} \) on \( V \) with \( \beta = \beta_{s} + \beta_{a} \), namely
\[
\begin{aligned}
\beta_{s}(\u,\v) &= \tfrac12\bigl(\beta(\u,\v) + \beta(\v,\u)\bigr), \\
\beta_{a}(\u,\v) &= \tfrac12\bigl(\beta(\u,\v) - \beta(\v,\u)\bigr).
\end{aligned}
\]
In matrices: \( \A = \tfrac12(\A + \A\tp) + \tfrac12(\A - \A\tp) \).
:::

::: {.proof}
Since \( \operatorname{char} F \ne 2 \), the element \( 1 + 1 \) is non-zero, hence invertible, and \( \tfrac12 \) denotes \( (1+1)^{-1} \). Both displayed formulas are bilinear, being combinations of the bilinear maps \( (\u,\v) \mapsto \beta(\u,\v) \) and \( (\u,\v) \mapsto \beta(\v,\u) \), and their sum is \( \beta \). Swapping \( \u \) and \( \v \) leaves \( \beta_{s} \) unchanged, so \( \beta_{s} \) is symmetric; and \( \beta_{a}(\v,\v) = \tfrac12(\beta(\v,\v) - \beta(\v,\v)) = 0 \), so \( \beta_{a} \) is alternating.

For uniqueness, suppose \( \beta_s + \beta_a = \beta_s' + \beta_a' \) with \( \beta_s, \beta_s' \) symmetric and \( \beta_a, \beta_a' \) alternating, and put \( \delta = \beta_s - \beta_s' = \beta_a' - \beta_a \). Then \( \delta \) is symmetric, being a difference of symmetric forms, and alternating, being a difference of alternating forms. By @thm-alternating-vs-skew (a) it is also skew-symmetric, so for all \( \u, \v \),
\[
\delta(\u,\v) = \delta(\v,\u) = -\delta(\u,\v),
\]
giving \( (1+1)\delta(\u,\v) = 0 \) and hence \( \delta(\u,\v) = 0 \). Therefore \( \beta_s = \beta_s' \) and \( \beta_a = \beta_a' \), as claimed.
:::

Both halves of the argument divided by \( 1 + 1 \), and both failures are real. In characteristic \( 2 \) the formulas are meaningless, and more than that, the statement itself is false: alternating forms are then a *subset* of the symmetric ones, not a complement to them.

::: {.warning}
**In characteristic \( 2 \), symmetric and alternating forms are not complementary.** Over \( \nF_2 \) take \( \beta(\x,\y) = x_1y_2 \) on \( \nF_2^2 \). An alternating form is skew-symmetric (@thm-alternating-vs-skew (a)), and skew-symmetric means symmetric here, so **every** sum of a symmetric form and an alternating form is symmetric. But \( \beta(\e_1,\e_2) = 1 \) while \( \beta(\e_2,\e_1) = 0 \), so \( \beta \) is not symmetric and therefore cannot be written as such a sum at all. The decomposition does not merely lose uniqueness; existence fails.
:::

## The quadratic form

A bilinear form is a function of two vectors, which makes it awkward to plot, to differentiate, or to write on a page. Feeding the same vector into both slots turns it into a function of one vector. Chapter 11 met this function on \( \nR^n \) under the name **quadratic form** and used it to identify conics; here is the general definition, and the surprising fact that nothing is lost.

*A quadratic form is what a bilinear form sees when both of its arguments are the same vector.*

::: {#def-quadratic-form}
[Quadratic Form]

Let \( \beta \) be a bilinear form on \( V \). The **quadratic form associated with** \( \beta \) is the function
\[
q \colon V \to F, \qquad q(\v) = \beta(\v, \v) .
\]
A function \( q \colon V \to F \) is called **a quadratic form on \( V \)** if \( q(\v) = \beta(\v,\v) \) for some **symmetric** bilinear form \( \beta \) on \( V \).
:::

Two clauses deserve separate readings. The first says how to build \( q \) from a given \( \beta \), for **any** \( \beta \) over **any** field. The second says which functions \( V \to F \) are entitled to the name, and it insists on a **symmetric** \( \beta \); the polarization theorem below will show that over a field of characteristic \( \ne 2 \) this symmetric \( \beta \) is then unique, so that "the" bilinear form of a quadratic form is well defined.

Insisting on symmetry costs nothing in characteristic \( \ne 2 \). If \( q(\v) = \beta(\v,\v) \) for some bilinear \( \beta \), then by @thm-symmetric-alternating-decomposition we may split \( \beta = \beta_s + \beta_a \), and \( \beta_a(\v,\v) = 0 \), so \( q(\v) = \beta_s(\v,\v) \) with \( \beta_s \) symmetric. The alternating part is invisible to \( q \).

In coordinates, with \( \A = \mtx{\beta}{\sB}{\sB} \) symmetric and \( \x = \coord{\v}{\sB} \),

\[
q(\v) = \x\tp\A\x = \sum_{i} a_{ii}x_i^2 + 2\sum_{i<j} a_{ij}x_ix_j ,
\]{#eq-quadratic-in-coordinates}

which is a homogeneous polynomial of degree \( 2 \) in the coordinates: hence the name. Reading @eq-quadratic-in-coordinates backwards recovers \( \A \) from the polynomial: \( a_{ii} \) is the coefficient of \( x_i^2 \), and \( a_{ij} \) for \( i \ne j \) is **half** the coefficient of \( x_ix_j \). That is word for word the recipe Chapter 11 gave for the symmetric matrix of a real quadratic form, and the halving is the same division by \( 1 + 1 \) as everywhere else in this section.

::: {#exm-quadratic-form-coefficients}
[From a polynomial to its matrix and back]

Over \( \nQ \), let \( q(x_1, x_2, x_3) = 2x_1^2 - x_2^2 + 6x_1x_2 - 4x_2x_3 \). Find the symmetric matrix \( \A \) with \( q(\x) = \x\tp\A\x \), and evaluate \( q(1, 1, 1) \) both from the polynomial and from \( \A \).
:::

::: {.solution}
The squared terms give \( a_{11} = 2 \), \( a_{22} = -1 \) and \( a_{33} = 0 \). The cross terms give \( a_{12} = a_{21} = 3 \) (half of \( 6 \)), \( a_{23} = a_{32} = -2 \) (half of \( -4 \)), and \( a_{13} = a_{31} = 0 \) since \( x_1x_3 \) does not appear. So
\[
\A = \begin{pmatrix} 2 & 3 & 0 \\ 3 & -1 & -2 \\ 0 & -2 & 0 \end{pmatrix}.
\]
From the polynomial, \( q(1,1,1) = 2 - 1 + 6 - 4 = 3 \). From the matrix, \( \A(1,1,1) = (5, 0, -2) \) and \( (1,1,1) \cdot (5,0,-2) = 3 \). The two agree.
:::

Now the theorem that makes \( q \) as good as \( \beta \).

::: {#thm-polarization-forms}
[Polarization]

Let \( \operatorname{char} F \ne 2 \). The map \( \beta \mapsto q \), \( q(\v) = \beta(\v,\v) \), is a bijection from the set of symmetric bilinear forms on \( V \) onto the set of quadratic forms on \( V \). Its inverse is given by either of
\[
\begin{aligned}
\beta(\u,\v) &= \tfrac12\bigl(q(\u+\v) - q(\u) - q(\v)\bigr) \\
&= \tfrac14\bigl(q(\u+\v) - q(\u-\v)\bigr).
\end{aligned}
\]
In particular a symmetric form is determined by its quadratic form: if \( \beta(\v,\v) = \beta'(\v,\v) \) for all \( \v \), then \( \beta = \beta' \).
:::

::: {.idea}
Only one computation is needed, and it is the expansion of \( q(\u \pm \v) \) by bilinearity. Symmetry merges the two cross terms into one, so the cross term appears with a factor \( 1 + 1 \), and dividing by it is the whole trick. Surjectivity is the definition of "quadratic form"; injectivity is the displayed formula.
:::

::: {.proof}
Let \( \beta \) be symmetric with quadratic form \( q \), and let \( \u, \v \in V \). By bilinearity and then symmetry,
\[
q(\u \pm \v) = \beta(\u,\u) \pm \beta(\u,\v) \pm \beta(\v,\u) + \beta(\v,\v),
\]
so \( q(\u \pm \v) = q(\u) + q(\v) \pm (1+1)\beta(\u,\v) \). Since \( \operatorname{char} F \ne 2 \), the element \( 1 + 1 \) is invertible, and taking the upper sign gives the first formula. Subtracting the two versions gives \( q(\u+\v) - q(\u-\v) = (1+1)^2\beta(\u,\v) \), which is the second.

The map \( \beta \mapsto q \) is onto the set of quadratic forms by @def-quadratic-form, which defines that set as the image. It is injective because the first displayed formula recovers \( \beta(\u,\v) \) from \( q \) alone; so if two symmetric forms have the same \( q \), the formula returns the same value for each, and they are equal. Hence the map is a bijection with the stated inverse. This proves the theorem.
:::

::: {.check}
Which bilinear forms are both symmetric and alternating, over a field of characteristic \( \ne 2 \)?
:::

::: {.solution}
Only the zero form. If \( \beta \) is alternating then \( q = 0 \), and if \( \beta \) is also symmetric then @thm-polarization-forms recovers \( \beta(\u,\v) = \tfrac12(0 - 0 - 0) = 0 \). (Over \( \nF_2 \) the answer is different: every alternating form is symmetric there, as @thm-alternating-vs-skew shows, and there are plenty of non-zero ones.)
:::

The second formula of @thm-polarization-forms should look familiar. Over \( \nR \), an inner product is a symmetric bilinear form whose quadratic form is \( q(\v) = \norm{\v}^2 \), and the formula reads
\[
\inner{\u}{\v} = \tfrac14\bigl(\norm{\u+\v}^2 - \norm{\u-\v}^2\bigr),
\]
which is exactly @lem-polarization-identities (a). Chapter 10 proved it to show that an isometry automatically preserves angles; the content here is the same, stripped of positivity and of \( \nR \). What Chapter 10 needed positivity for was the *norm*, not the identity.

## Hermitian forms

Over \( \nC \) the pattern changes, because \( \inner{\v}{\v} \) is required to be a positive real number and no bilinear form can deliver that: bilinearity gives \( \beta(i\v, i\v) = i^2\beta(\v,\v) = -\beta(\v,\v) \), so the values at \( \v \) and \( i\v \) have opposite signs. Chapter 10 solved this by making the second slot conjugate-linear. That fix has nothing to do with positivity, so it can be made here too.

::: {#def-hermitian-form}
[Hermitian Form]

Let \( V \) be a vector space over \( \nC \). A function \( \beta \colon V \times V \to \nC \) is a **Hermitian form** if it is **linear in the first argument**, and
\[
\beta(\v, \u) = \conj{\beta(\u, \v)} \qquad \text{for all } \u, \v \in V .
\]
:::

Two remarks on the clauses. First, the two conditions together force conjugate-linearity in the second argument: \( \beta(\u, c\v) = \conj{\beta(c\v,\u)} = \conj{c\,\beta(\v,\u)} = \conj{c}\,\beta(\u,\v) \). So a Hermitian form is **not** bilinear, and @def-bilinear-form does not cover it. Second, taking \( \u = \v \) gives \( \beta(\v,\v) = \conj{\beta(\v,\v)} \), so the associated function \( q(\v) = \beta(\v,\v) \) takes **real** values even though \( \beta \) does not.

The examples are the ones from Chapter 10 with positivity dropped: \( \beta(\x,\y) = \y^{*}\A\x \) on \( \nC^n \) for any \( \A \) with \( \A^{*} = \A \), including indefinite choices such as \( \A = \diag(1,-1) \). The matrix criterion is the same proof as @prp-form-symmetry-matrix with stars in place of transposes.

::: {#prp-hermitian-form-matrix}
[Hermitian Forms and Hermitian Matrices]

Let \( \beta \) be linear in the first argument and conjugate-linear in the second, let \( \sB = (\v_1, \dots, \v_n) \) be a basis of \( V \), and let \( \A \) be the matrix with entries \( a_{ij} = \beta(\v_j, \v_i) \). Then \( \beta \) is Hermitian if and only if \( \A^{*} = \A \), and in that case \( \beta(\u,\v) = \coord{\v}{\sB}^{*}\A\coord{\u}{\sB} \).
:::

::: {.proof}
The index order \( a_{ij} = \beta(\v_j, \v_i) \) is the one used for Gram matrices in Chapter 10 (\( \G \) in @def-gram-matrix), chosen so that the displayed formula comes out with no transposing of the answer. Expanding \( \u = \sum_j c_j\v_j \) and \( \v = \sum_i d_i\v_i \) by linearity in the first slot and conjugate-linearity in the second,
\[
\beta(\u,\v) = \sum_{i,j} c_j\conj{d_i}\,\beta(\v_j,\v_i)
= \sum_{i,j} \conj{d_i}\,a_{ij}c_j ,
\]
which is the matrix product \( \coord{\v}{\sB}^{*}\A\coord{\u}{\sB} \). If \( \beta \) is Hermitian then in particular \( a_{ji} = \beta(\v_i,\v_j) = \conj{\beta(\v_j,\v_i)} = \conj{a_{ij}} \), which is \( \A^{*} = \A \). Conversely, if \( a_{ji} = \conj{a_{ij}} \) then conjugating the display gives
\[
\conj{\beta(\u,\v)} = \sum_{i,j} d_i\,\conj{a_{ij}}\,\conj{c_j} = \sum_{i,j} \conj{c_j}\,a_{ji}\,d_i = \beta(\v,\u),
\]
so \( \beta \) is Hermitian.
:::

Polarization works for Hermitian forms too, and it is the four-term identity rather than the two-term one: by @lem-polarization-identities (b) with \( q(\v) = \beta(\v,\v) \),
\[
\beta(\u,\v) = \tfrac14\sum_{k=0}^{3} i^k\, q(\u + i^k\v).
\]
The computation in Chapter 10 expanded each term using linearity in the first slot, conjugate-linearity in the second and \( \beta(\v,\u) = \conj{\beta(\u,\v)} \), and used positivity nowhere, so it proves this identity too. Note the contrast with the real case: over \( \nC \) there is no characteristic to worry about, since \( \operatorname{char}\nC = 0 \), and the reason a Hermitian form is recoverable from \( q \) is the extra room provided by \( i \).

::: {.warning}
**A quadratic form over a field of characteristic \( 2 \) is a different object, and this book does not define it.** Two things go wrong there, and @thm-polarization-forms repairs neither. *The form is not determined by \( q \).* Over \( \nF_2 \), the symmetric form \( \beta(\x,\y) = x_1y_2 + x_2y_1 \) has \( q(\x) = 2x_1x_2 = 0 \), the same \( q \) as the zero form, so \( \beta \mapsto q \) is not injective on symmetric forms. *And @def-quadratic-form names too few functions.* The function \( q(\x) = x_1x_2 \) on \( \nF_2^2 \) is \( \beta(\x,\x) \) for the bilinear \( \beta(\x,\y) = x_1y_2 \), yet it is \( \beta(\x,\x) \) for **no symmetric** \( \beta \): for a symmetric \( \A \), @eq-quadratic-in-coordinates gives \( a_{11}x_1^2 + a_{22}x_2^2 = a_{11}x_1 + a_{22}x_2 \) over \( \nF_2 \), whose values at \( (1,1) \), \( (1,0) \) and \( (0,1) \) are \( a_{11} + a_{22} \), \( a_{11} \) and \( a_{22} \), and no choice makes those \( 1, 0, 0 \). The theory of quadratic forms in characteristic \( 2 \) therefore defines \( q \) first, by the axioms \( q(c\v) = c^2q(\v) \) and "\( q(\u+\v) - q(\u) - q(\v) \) is bilinear", and treats \( \beta \) as derived data. Everything that follows assumes \( \operatorname{char} F \ne 2 \) precisely to stay out of that theory.
:::

Three kinds of form, then, and three matrix shapes: symmetric, alternating, Hermitian. The next two sections take the first of them and classify it up to congruence, first over any field of characteristic \( \ne 2 \), then over \( \nR \).

## Exercises

### A. Check your understanding

:::: {#exr-symmetric-alternating-hermitian-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define what it means for a bilinear form \( \beta \) on \( V \) to be **symmetric**, **alternating** and **skew-symmetric**.
2. State the relationship between alternating and skew-symmetric forms, including the exact role of the characteristic.
3. Write down the matrix condition, in a fixed basis, for each of the three notions in (a).
4. Determine whether the following statement is correct, and justify your answer: over \( \nQ \), a bilinear form is determined by the function \( \v \mapsto \beta(\v,\v) \).
5. Why is a Hermitian form not an example of @def-bilinear-form?
:::
::::

::: {.solution}
(a) Symmetric: \( \beta(\u,\v) = \beta(\v,\u) \) for all \( \u,\v \). Alternating: \( \beta(\v,\v) = 0 \) for all \( \v \). Skew-symmetric: \( \beta(\u,\v) = -\beta(\v,\u) \) for all \( \u,\v \).

(b) Alternating always implies skew-symmetric (@thm-alternating-vs-skew (a)). The converse holds if and only if \( \operatorname{char} F \ne 2 \); in characteristic \( 2 \) the dot product on \( \nF_2^2 \) is skew-symmetric and not alternating.

(c) With \( \A = \mtx{\beta}{\sB}{\sB} \): symmetric means \( \A\tp = \A \); skew-symmetric means \( \A\tp = -\A \); alternating means \( \A\tp = -\A \) together with \( a_{ii} = 0 \) for all \( i \) (@prp-form-symmetry-matrix, @prp-alternating-form-matrix).

(d) Incorrect. Since \( \operatorname{char}\nQ = 0 \ne 2 \), only the **symmetric** part is determined: any alternating form has \( \beta(\v,\v) = 0 \) identically, so \( \beta \) and \( \beta + \beta_a \) have the same quadratic form for every alternating \( \beta_a \). What is true is @thm-polarization-forms, which determines \( \beta \) among *symmetric* forms.

(e) It is not linear in the second argument: \( \beta(\u, c\v) = \conj{c}\,\beta(\u,\v) \), and \( \conj{c} \ne c \) for \( c \notin \nR \).
:::

### B. Practice

:::: {#exr-symmetric-alternating-hermitian-b1}
[B1: Determine which of the following]

Over \( \nQ \), with \( V = \nQ^2 \) and \( \x = (x_1,x_2) \), \( \y = (y_1,y_2) \), determine for each of the following bilinear forms whether it is symmetric, whether it is alternating, and whether it is skew-symmetric. Justify each answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \beta(\x,\y) = x_1y_1 - x_2y_2 \).
2. \( \beta(\x,\y) = 3x_1y_2 - 3x_2y_1 \).
3. \( \beta(\x,\y) = x_1y_2 + 2x_2y_1 \).
4. \( \beta(\x,\y) = 0 \).
:::
::::

::: {.solution}
Write down the matrix \( \A \) in the standard basis in each case and apply @prp-form-symmetry-matrix and @prp-alternating-form-matrix.

(a) \( \A = \diag(1,-1) \), which satisfies \( \A\tp = \A \): symmetric. Not skew-symmetric, since \( \A\tp = -\A \) would need \( 1 = -1 \) in \( \nQ \). Not alternating, since \( \beta(\e_1,\e_1) = 1 \).

(b) \( \A = \begin{psmallmatrix} 0 & 3 \\ -3 & 0\end{psmallmatrix} \), with \( \A\tp = -\A \) and zero diagonal: skew-symmetric and alternating. Not symmetric, since \( 3 \ne -3 \).

(c) \( \A = \begin{psmallmatrix} 0 & 1 \\ 2 & 0\end{psmallmatrix} \). Symmetry would need \( 1 = 2 \) and skewness would need \( 1 = -2 \), both false in \( \nQ \); so it is neither, and it is not alternating either, since an alternating form is skew-symmetric. (Its diagonal entries do vanish, so \( \beta(\e_i,\e_i) = 0 \) for the two basis vectors — but \( \beta(\1,\1) = 1 + 2 = 3 \ne 0 \). Checking the basis vectors alone is not enough.)

(d) The zero form is symmetric, skew-symmetric and alternating at once; its matrix is \( \0 \), which satisfies every condition. By the Quick check above it is the only form that is both symmetric and alternating over \( \nQ \).
:::

:::: {#exr-symmetric-alternating-hermitian-b2}
[B2: Polarizing a quadratic form]

Over \( \nR \), let \( q(x_1,x_2,x_3) = x_1^2 + 4x_1x_2 - 2x_2x_3 + 5x_3^2 \).

::: {.enumerate options="label=(\alph*)"}
1. Find the symmetric matrix \( \A \) with \( q(\x) = \x\tp\A\x \).
2. Compute \( \beta(\e_1 + \e_2, \e_3) \) directly from \( \A \), and again from the polarization formula \( \tfrac12(q(\u+\v) - q(\u) - q(\v)) \).
:::
::::

::: {.solution}
(a) The squared terms give \( a_{11} = 1 \), \( a_{22} = 0 \), \( a_{33} = 5 \); the cross terms give \( a_{12} = a_{21} = 2 \), \( a_{23} = a_{32} = -1 \), \( a_{13} = a_{31} = 0 \). So
\[
\A = \begin{pmatrix} 1 & 2 & 0 \\ 2 & 0 & -1 \\ 0 & -1 & 5 \end{pmatrix}.
\]

(b) Put \( \u = (1,1,0) \) and \( \v = (0,0,1) \). Directly, \( \A\v = (0,-1,5) \) and \( \u\tp(\A\v) = 0 - 1 = -1 \).

By polarization, \( q(\u) = 1 + 4 = 5 \) and \( q(\v) = 5 \), while \( \u + \v = (1,1,1) \) gives \( q(\u+\v) = 1 + 4 - 2 + 5 = 8 \). Hence \( \tfrac12(8 - 5 - 5) = -1 \). The two agree, as @thm-polarization-forms says they must.
:::

:::: {#exr-symmetric-alternating-hermitian-b3}
[B3: Splitting a form]

Let \( \A = \begin{pmatrix} 1 & 5 \\ -1 & 4 \end{pmatrix} \) over \( \nQ \), and let \( \beta(\x,\y) = \x\tp\A\y \). Write \( \beta = \beta_s + \beta_a \) as in @thm-symmetric-alternating-decomposition, giving the matrix of each part, and verify that \( \beta \) and \( \beta_s \) have the same quadratic form.
::::

::: {.solution}
We have \( \A\tp = \begin{psmallmatrix} 1 & -1 \\ 5 & 4\end{psmallmatrix} \), so
\[
\tfrac12(\A + \A\tp) = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix},
\qquad
\tfrac12(\A - \A\tp) = \begin{pmatrix} 0 & 3 \\ -3 & 0 \end{pmatrix}.
\]
The first is symmetric and the second is alternating, and they sum to \( \A \). For the quadratic forms, \( \x\tp\A\x = x_1^2 + 5x_1x_2 - x_2x_1 + 4x_2^2 = x_1^2 + 4x_1x_2 + 4x_2^2 \), and the symmetric part gives \( x_1^2 + 2x_1x_2 + 2x_2x_1 + 4x_2^2 \), the same polynomial. The alternating part contributes \( 3x_1x_2 - 3x_2x_1 = 0 \).
:::

### C. Going deeper

:::: {#exr-symmetric-alternating-hermitian-c1}
[C1: Is this still true over \( \nF_2 \)?]

Let \( V \) be a vector space over \( \nF_2 \) with \( \dim V = n \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that every alternating bilinear form on \( V \) is symmetric.
2. Prove that the alternating forms on \( V \) form a subspace of the space of all bilinear forms, and compute its dimension.
3. Deduce that for \( n = 2 \) there is exactly one non-zero alternating form on \( V \), and write down its matrix.
:::

*Hint: for (b), use @prp-alternating-form-matrix.*
::::

::: {.solution}
(a) Let \( \beta \) be alternating. By @thm-alternating-vs-skew (a), \( \beta(\u,\v) = -\beta(\v,\u) \). Over \( \nF_2 \) we have \( -1 = 1 \), so \( -\beta(\v,\u) = \beta(\v,\u) \) and \( \beta \) is symmetric.

(b) Fix a basis \( \sB \). The map \( \beta \mapsto \mtx{\beta}{\sB}{\sB} \) is a linear bijection from bilinear forms to \( M_n(\nF_2) \) (@thm-form-matrix-determines). By @prp-alternating-form-matrix (b), \( \beta \) is alternating exactly when its matrix satisfies \( \A\tp = -\A \) with zero diagonal; over \( \nF_2 \) the first condition is \( \A\tp = \A \), so the image is the set of symmetric matrices with zero diagonal. Such a matrix is determined freely by its entries \( a_{ij} \) with \( i < j \), of which there are \( \binom{n}{2} \). These conditions are linear, so the set of alternating forms is a subspace, of dimension \( n(n-1)/2 \).

(c) For \( n = 2 \) the dimension is \( 1 \), so the space of alternating forms is \( \{\0, \beta\} \) for a single non-zero \( \beta \), whose matrix must be \( \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix} \) — the only symmetric \( \nF_2 \)-matrix with zero diagonal other than \( \0 \). Concretely \( \beta(\x,\y) = x_1y_2 + x_2y_1 \), and indeed \( \beta(\x,\x) = 2x_1x_2 = 0 \).
:::

:::: {#exr-symmetric-alternating-hermitian-c2}
[C2: How much of a form does \( q \) see?]

Let \( \operatorname{char} F \ne 2 \) and let \( \beta \) be any bilinear form on \( V \), with \( q(\v) = \beta(\v,\v) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that two bilinear forms have the same quadratic form if and only if their difference is alternating.
2. Deduce that the set of bilinear forms with a given quadratic form \( q \) contains exactly one symmetric form.
3. For \( \dim V = n \), how many bilinear forms share a given quadratic form when \( F = \nF_3 \)?
:::
::::

::: {.solution}
(a) \( (\Rightarrow) \) Suppose \( \beta_1(\v,\v) = \beta_2(\v,\v) \) for all \( \v \). Then \( \delta = \beta_1 - \beta_2 \) is bilinear with \( \delta(\v,\v) = 0 \) for all \( \v \), which is @def-alternating-form at \( k = 2 \).

\( (\Leftarrow) \) If \( \delta = \beta_1 - \beta_2 \) is alternating then \( \beta_1(\v,\v) - \beta_2(\v,\v) = \delta(\v,\v) = 0 \) for every \( \v \).

(b) Existence: by @thm-symmetric-alternating-decomposition write \( \beta = \beta_s + \beta_a \); then \( \beta_s \) is symmetric with the same quadratic form, since \( \beta_a(\v,\v) = 0 \). Uniqueness: two symmetric forms with the same \( q \) are equal by @thm-polarization-forms.

(c) By (a), the forms sharing \( q \) are exactly \( \beta_s + \beta_a \) with \( \beta_a \) alternating, so there are as many as there are alternating forms. Over a field with \( 3 \) elements, an alternating form corresponds by @prp-alternating-form-matrix (b) to a matrix with \( \A\tp = -\A \) and zero diagonal, which is determined freely by the \( \binom{n}{2} \) entries above the diagonal. So there are \( 3^{n(n-1)/2} \) of them.
:::

:::: {#exr-symmetric-alternating-hermitian-c3}
[C3: A Hermitian form is a real symmetric form in disguise]

Let \( \beta \) be a Hermitian form on \( \nC^n \) with matrix \( \A = \A^{*} \) as in @prp-hermitian-form-matrix, and regard \( \nC^n \) as a real vector space of dimension \( 2n \) by forgetting multiplication by \( i \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \tau(\u,\v) = \operatorname{Re}\beta(\u,\v) \) is a symmetric \( \nR \)-bilinear form on that real space, with \( \tau(\v,\v) = \beta(\v,\v) \).
2. Prove that \( \omega(\u,\v) = \operatorname{Im}\beta(\u,\v) \) is an alternating \( \nR \)-bilinear form.
3. For \( n = 1 \) and \( \A = (1) \), write both \( \tau \) and \( \omega \) as explicit forms on \( \nR^2 \).
:::
::::

::: {.solution}
(a) Taking real parts of an \( \nR \)-linear identity is \( \nR \)-linear, and \( \beta \) is additive in each slot and commutes with real scalars in each slot (conjugation fixes \( \nR \)), so \( \tau \) is \( \nR \)-bilinear. Symmetry: \( \beta(\v,\u) = \conj{\beta(\u,\v)} \), and conjugate numbers have equal real parts, so \( \tau(\v,\u) = \tau(\u,\v) \). Finally \( \beta(\v,\v) \) is real, as noted after @def-hermitian-form, so \( \tau(\v,\v) = \beta(\v,\v) \).

(b) \( \nR \)-bilinearity is the same argument with imaginary parts. Conjugate numbers have opposite imaginary parts, so \( \omega(\v,\u) = -\omega(\u,\v) \): \( \omega \) is skew-symmetric, and since \( \operatorname{char}\nR = 0 \ne 2 \), @thm-alternating-vs-skew (b) makes it alternating. (Directly: \( \beta(\v,\v) \) is real, so its imaginary part is \( 0 \).)

(c) Here \( \beta(u,v) = u\conj{v} \) for \( u, v \in \nC \). Writing \( u = x_1 + ix_2 \) and \( v = y_1 + iy_2 \), we get \( u\conj{v} = (x_1y_1 + x_2y_2) + i(x_2y_1 - x_1y_2) \). So \( \tau \) is the dot product on \( \nR^2 \) and \( \omega(\x,\y) = x_2y_1 - x_1y_2 \), the negative of the signed area.
:::
