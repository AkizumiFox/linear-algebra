# Multilinear Alternating Forms

The previous section found that signed area obeys a few rules: it is linear in each side separately, it vanishes when two sides are equal, and swapping the sides changes its sign. This section gives these rules names for functions of \( k \) vectors in an arbitrary vector space, and derives everything that follows from them before any formula exists. The main result is that "zero on equal arguments" already implies the swap rule, the shear rule and vanishing on dependent lists. The swap rule, in turn, gives back "zero on equal arguments" only when \( 1 + 1 \neq 0 \) in the field.

Throughout, \( V \) is a vector space over a field \( F \), \( k \ge 1 \) is an integer, and \( V^k = V \times \cdots \times V \) is the set of \( k \)-tuples of vectors (@def-n-tuple).

## Multilinear forms

Signed area is not a linear function of the pair \( (\u, \v) \): doubling both sides multiplies the area by four, not by two. What it does have is linearity in \( \u \) when \( \v \) is held fixed, and linearity in \( \v \) when \( \u \) is held fixed. This "one slot at a time" linearity recurs throughout the book: in the dot product, later in inner products and bilinear forms, and in the determinant. So we give it a name.

*A multilinear form is a function of several vectors that is linear in each vector while the others are held fixed.*

::: {#def-multilinear-form}
[Multilinear Form]

A function \( f \colon V^k \to F \) is **\( k \)-linear**, or a **multilinear form** on \( V \), if **for every** position \( i \in \{1, \dots, k\} \) and **every** choice of \( \v_1, \dots, \v_{i-1}, \v_{i+1}, \dots, \v_k \in V \), the function
\[
  V \to F, \qquad \x \mapsto f(\v_1, \dots, \v_{i-1}, \x, \v_{i+1}, \dots, \v_k)
\]
is linear. A \( 2 \)-linear form is called **bilinear**.
:::

In words: fix all arguments except the one in position \( i \). What remains is a function of one vector, and it must be a linear functional (@def-linear-functional). Written out, for all \( \x, \y \in V \) and \( c \in F \),
\[
  f(\dots, \x + \y, \dots) = f(\dots, \x, \dots) + f(\dots, \y, \dots), \qquad f(\dots, c\x, \dots) = c\,f(\dots, \x, \dots),
\]
where the dots stand for the same fixed vectors on both sides. The condition is imposed for **every** position \( i \), one at a time.

Some examples:

- **Signed area.** On \( F^2 \), \( f(\u, \v) = u_1v_2 - u_2v_1 \) is bilinear. For fixed \( \v \), the map \( \u \mapsto v_2u_1 - v_1u_2 \) is a linear functional on \( F^2 \), and for fixed \( \u \), so is \( \v \mapsto u_1v_2 - u_2v_1 \).
- **The dot product.** On \( F^n \), \( (\u, \v) \mapsto u_1v_1 + \dots + u_nv_n \) is bilinear, by the same one-slot check.
- **Products of functionals.** If \( \varphi_1, \dots, \varphi_k \in V^{*} \), then \( f(\v_1, \dots, \v_k) = \varphi_1(\v_1)\varphi_2(\v_2) \cdots \varphi_k(\v_k) \) is \( k \)-linear: in position \( i \) it is the linear functional \( \varphi_i \) multiplied by the fixed scalar \( \prod_{j \neq i} \varphi_j(\v_j) \). For instance, on \( F[x] \), \( (p, q) \mapsto p(0)q(1) \) is bilinear, since evaluation at a point is linear (@thm-evaluation-respects-operations).
- **The degenerate case \( k = 1 \).** A \( 1 \)-linear form is exactly a linear functional on \( V \). So multilinear forms generalize the dual space of Chapter 4.

::: {.warning}
**Multilinear is not linear.** A bilinear form is **not** a linear function of the pair. For the signed area \( f(\u, \v) = u_1v_2 - u_2v_1 \) on \( \nR^2 \), scaling both arguments by \( 2 \) gives \( f(2\e_1, 2\e_2) = 4 \), not \( 2f(\e_1, \e_2) = 2 \). Adding in both slots at once is not allowed either: \( f(\e_1 + \0, \e_1 + \e_2) = f(\e_1, \e_1 + \e_2) = 1 \), while \( f(\e_1, \e_1) + f(\0, \e_2) = 0 \). Pull out scalars and split sums **one slot at a time**.
:::

## Alternating and skew-symmetric forms

The second rule of signed area was geometric: if two edges coincide, the parallelogram or box is flat. There are two natural ways to put this into algebra. One says the value is **zero** when two arguments are equal. The other says the value **changes sign** when two arguments are swapped. They look like two phrasings of one idea, but they are not the same, and we must choose.

*An alternating form vanishes as soon as two of its arguments coincide.*

::: {#def-alternating-form}
[Alternating Form]

A \( k \)-linear form \( f \colon V^k \to F \) is **alternating** if \( f(\v_1, \dots, \v_k) = 0 \) **whenever** \( \v_i = \v_j \) for **some** pair of positions \( i \neq j \).
:::

::: {#def-skew-symmetric-form}
[Skew-Symmetric Form]

A \( k \)-linear form \( f \colon V^k \to F \) is **skew-symmetric** if, **for all** \( \v_1, \dots, \v_k \in V \) and **all** positions \( i < j \), swapping the arguments in positions \( i \) and \( j \) multiplies the value by \( -1 \):
\[
  f(\v_1, \dots, \v_j, \dots, \v_i, \dots, \v_k) = -f(\v_1, \dots, \v_i, \dots, \v_j, \dots, \v_k),
\]
where on the left \( \v_j \) sits in position \( i \), \( \v_i \) sits in position \( j \), and all other positions are unchanged.
:::

In words: "alternating" asks for the value \( 0 \) as soon as **any two** positions, adjacent or not, hold the same vector, whatever the remaining arguments are. It is a condition on the inputs where two entries coincide, and says nothing directly about other inputs. "Skew-symmetric" is a condition on **every** input: it compares the value at a list with the value at the list with two entries exchanged.

::: {#exm-alternating-forms}
[Alternating Forms]

Check that each of the following is an alternating form.

::: {.enumerate options="label=(\alph*)"}
1. On \( F^2 \), for a fixed \( c \in F \): \( f_c(\u, \v) = c(u_1v_2 - u_2v_1) \).
2. On \( F^3 \), for fixed coordinate indices \( 1 \le r < s \le 3 \): \( g_{rs}(\u, \v) = u_rv_s - u_sv_r \).
3. On \( F[x] \): \( h(p, q) = p(0)q(1) - p(1)q(0) \).
4. On any \( V \), with \( k = 1 \): any linear functional \( \varphi \in V^{*} \).
:::
:::

::: {.solution}
(a) Bilinearity is the one-slot check above, multiplied by the constant \( c \). With \( k = 2 \) the only pair of positions is \( (1, 2) \), and \( f_c(\u, \u) = c(u_1u_2 - u_2u_1) = 0 \) by commutativity in \( F \). So \( f_c \) is alternating. For \( c = 0 \) it is the zero form, which is alternating for the silly reason that it is zero everywhere; for \( c = 1 \) it is the signed area of the previous section.

(b) In each slot \( g_{rs} \) is a linear functional, as in (a), and \( g_{rs}(\u, \u) = u_ru_s - u_su_r = 0 \). Over \( \nR \) these three forms are, up to sign and order, the components of the cross product: \( \u \times \v = \bigl(g_{23}(\u, \v), -g_{13}(\u, \v), g_{12}(\u, \v)\bigr) \). This example shows that the number of arguments need not equal the dimension: here \( k = 2 \) and \( \dim F^3 = 3 \).

(c) Evaluation at \( 0 \) and at \( 1 \) are linear in \( p \) (@thm-evaluation-respects-operations), so for fixed \( q \) the map \( p \mapsto q(1)\,p(0) - q(0)\,p(1) \) is linear, and similarly in \( q \). Also \( h(p, p) = p(0)p(1) - p(1)p(0) = 0 \). It is not the zero form: \( h(1, x) = 1 \cdot 1 - 1 \cdot 0 = 1 \).

(d) A linear functional is \( 1 \)-linear. With a single position there is **no** pair \( i \neq j \), so the alternating condition holds vacuously (@exm-vacuous-truth). This degenerate case matters because it shows that "alternating" is purely a condition about **pairs** of positions; the interesting content starts at \( k = 2 \).
:::

Now a non-example, by a minimal change of (a). Over \( \nR \), replace the minus sign by a plus: \( s(\u, \v) = u_1v_2 + u_2v_1 \). Bilinearity survives, by the same one-slot check. But \( s(\e_1 + \e_2, \e_1 + \e_2) = 1 + 1 = 2 \neq 0 \), so the alternating clause fails. The dot product fails in the same way, \( \e_1 \cdot \e_1 = 1 \). A different minimal change keeps the alternating clause and breaks the other one. The unsigned area \( \lvert u_1v_2 - u_2v_1 \rvert \) on \( \nR^2 \) is still \( 0 \) whenever \( \u = \v \), but it is not linear in \( \u \): at \( \v = \e_2 \) it sends \( \e_1 \mapsto 1 \) and \( -\e_1 \mapsto 1 \neq -1 \). This is the failure that forced a sign onto area in the previous section.

::: {.check}
Is \( f(\u, \v) = u_1v_2 \) on \( F^2 \) alternating? Is it skew-symmetric?
:::

::: {.solution}
It is bilinear, but neither. With \( \u = \v = \e_1 + \e_2 \), \( f(\u, \u) = 1 \cdot 1 = 1 \neq 0 \), so it is not alternating. And \( f(\e_1, \e_2) = 1 \) while \( f(\e_2, \e_1) = 0 \); skew-symmetry would need \( 0 = -1 \), which fails in every field.
:::

**Why this definition.** We chose "zero when two arguments are equal" as the basic notion, and in the form "**any** two positions". There are two reasons. First, it is what the picture says directly: two equal edges make a flat box. Second, as we prove next, it implies the swap rule over **every** field, while the swap rule implies it only when \( 1 + 1 \neq 0 \). Allowing any pair of positions, not just adjacent ones, also spares us a separate argument moving equal entries next to each other.

## Consequences of the alternating condition

Everything that elimination does to a determinant will come from the following theorem. Its four parts are the column operations of Chapter 2 seen through a form: swap two arguments, add a multiple of one to another, scale one, and the extreme case of a dependent list.

::: {#thm-alternating-properties}
[Properties of Alternating Forms]

Let \( f \colon V^k \to F \) be an alternating \( k \)-linear form, let \( \v_1, \dots, \v_k \in V \), and let \( i \neq j \) be positions in \( \{1, \dots, k\} \).

::: {.enumerate options="label=(\alph*)"}
1. **(Swap)** Exchanging the arguments in positions \( i \) and \( j \) multiplies \( f(\v_1, \dots, \v_k) \) by \( -1 \). In particular, \( f \) is skew-symmetric.
2. **(Shear)** For every \( c \in F \), replacing \( \v_i \) by \( \v_i + c\v_j \) does not change \( f(\v_1, \dots, \v_k) \).
3. **(Scaling)** For every \( c \in F \), replacing \( \v_i \) by \( c\v_i \) multiplies \( f(\v_1, \dots, \v_k) \) by \( c \).
4. **(Dependence)** If the list \( (\v_1, \dots, \v_k) \) is linearly dependent, then \( f(\v_1, \dots, \v_k) = 0 \). In particular, \( f(\v_1, \dots, \v_k) = 0 \) if some \( \v_i = \0 \).
:::
:::

::: {.idea}
Parts (a)–(c) involve at most the two slots \( i \) and \( j \), so freeze the other \( k - 2 \) arguments. What is left is a bilinear form \( g(\x, \y) \) with \( g(\x, \x) = 0 \), and the \( k \)-argument statements become two-argument statements about \( g \). For the swap, the move is to feed \( g \) a sum in both slots, \( g(\x + \y, \x + \y) = 0 \), and expand: the two "square" terms die and the two cross terms must cancel. For (d), write one vector as a combination of the others and expand in its slot: every resulting term has a repeated argument.
:::

::: {.proof}
Suppose first \( i < j \); the case \( i > j \) is the same with the roles of \( i \) and \( j \) exchanged. For \( \x, \y \in V \), let
\[
  g(\x, \y) = f(\v_1, \dots, \v_{i-1}, \x, \v_{i+1}, \dots, \v_{j-1}, \y, \v_{j+1}, \dots, \v_k),
\]
the value of \( f \) with \( \x \) in position \( i \), \( \y \) in position \( j \), and \( \v_m \) in every other position \( m \). Since \( f \) is \( k \)-linear, \( g \) is bilinear, and since \( f \) is alternating, \( g(\x, \x) = 0 \) for every \( \x \in V \). In this notation \( f(\v_1, \dots, \v_k) = g(\v_i, \v_j) \).

(c) This is linearity of \( f \) in position \( i \): \( g(c\v_i, \v_j) = c\,g(\v_i, \v_j) \).

(b) By linearity in the first slot of \( g \) and \( g(\v_j, \v_j) = 0 \),
\[
  g(\v_i + c\v_j, \v_j) = g(\v_i, \v_j) + c\,g(\v_j, \v_j) = g(\v_i, \v_j).
\]

(a) By bilinearity of \( g \),
\[
  0 = g(\v_i + \v_j, \v_i + \v_j) = g(\v_i, \v_i) + g(\v_i, \v_j) + g(\v_j, \v_i) + g(\v_j, \v_j) = g(\v_i, \v_j) + g(\v_j, \v_i),
\]
where the first and last equalities use \( g(\x, \x) = 0 \). Hence \( g(\v_j, \v_i) = -g(\v_i, \v_j) \), which is the swap statement. Since \( \v_1, \dots, \v_k \) and \( i < j \) were arbitrary, \( f \) is skew-symmetric (@def-skew-symmetric-form).

(d) Suppose \( (\v_1, \dots, \v_k) \) is linearly dependent. By the Linear Dependence Lemma (@thm-linear-dependence-lemma), there is an index \( j \) with \( \v_j \in \Span(\v_1, \dots, \v_{j-1}) \). If \( j = 1 \), then \( \v_1 = \0 = 0 \cdot \v_1 \), and by (c) with \( c = 0 \), \( f(\v_1, \dots, \v_k) = 0 \cdot f(\v_1, \dots, \v_k) = 0 \). If \( j \ge 2 \), write \( \v_j = a_1\v_1 + \dots + a_{j-1}\v_{j-1} \) with \( a_m \in F \). By linearity of \( f \) in position \( j \),
\[
  f(\v_1, \dots, \v_k) = \sum_{m=1}^{j-1} a_m\, f(\v_1, \dots, \v_{j-1}, \v_m, \v_{j+1}, \dots, \v_k).
\]
In the \( m \)-th term, the vector \( \v_m \) sits both in position \( m \) and in position \( j \neq m \), so the term is \( 0 \) because \( f \) is alternating. Hence \( f(\v_1, \dots, \v_k) = 0 \). The last sentence of (d) holds because a list containing \( \0 \) is dependent. This proves the theorem.
:::

For the determinant, (a)–(c) will be the rules for column operations, and (d) explains at once why a matrix with dependent columns must have determinant \( 0 \). Part (d) also bounds the number of arguments: on a space of dimension \( n \), any \( k > n \) vectors are dependent, so a non-zero alternating form needs \( k \le n \) (Exercise C1).

## Alternating versus skew-symmetric

Part (a) says alternating forms are skew-symmetric. The converse depends on the field.

::: {#thm-skew-symmetric-alternating}
[Skew-Symmetric and Alternating Forms]

Let \( f \colon V^k \to F \) be a \( k \)-linear form.

::: {.enumerate options="label=(\alph*)"}
1. If \( f \) is alternating, then \( f \) is skew-symmetric.
2. If \( f \) is skew-symmetric and the characteristic of \( F \) is **not** \( 2 \), then \( f \) is alternating.
:::
:::

::: {.proof}
(a) is @thm-alternating-properties (a).

(b) Suppose \( \v_i = \v_j \) for some \( i < j \). Exchanging the arguments in positions \( i \) and \( j \) does not change the list, so skew-symmetry gives \( f(\v_1, \dots, \v_k) = -f(\v_1, \dots, \v_k) \), that is, \( (1 + 1)\,f(\v_1, \dots, \v_k) = 0 \). If \( 1 + 1 = 0 \) in \( F \), then \( 2 \cdot 1 = 0 \) while \( 1 \cdot 1 = 1 \neq 0 \), so the smallest positive \( n \) with \( n \cdot 1 = 0 \) would be \( 2 \), and the characteristic of \( F \) would be \( 2 \) (@def-characteristic). So \( 1 + 1 \neq 0 \), and multiplying by \( (1 + 1)^{-1} \) gives \( f(\v_1, \dots, \v_k) = 0 \). Hence \( f \) is alternating.
:::

::: {.warning}
**Skew-symmetric does not imply alternating over \( \nF_2 \).** In \( \nF_2 \) we have \( -1 = 1 \), so "skew-symmetric" just means "symmetric". Take \( f(\u, \v) = u_1v_1 \) on \( \nF_2^2 \). It is bilinear, and \( f(\v, \u) = v_1u_1 = u_1v_1 = -f(\u, \v) \), so it is skew-symmetric. But \( f(\e_1, \e_1) = 1 \neq 0 \), so it is **not** alternating. Checking all \( 16 \) pairs \( (\u, \v) \) confirms both claims: \( f(\u, \v) = f(\v, \u) \) always, and \( f(\u, \u) = u_1 \) is \( 1 \) for \( \u = (1, 0) \) and \( \u = (1, 1) \). This is why the determinant is built on alternating forms, not skew-symmetric ones: the construction must work over \( \nF_2 \) too.
:::

## The space of alternating forms

Alternating forms can be added and scaled, and the result is again alternating. This is what makes the uniqueness question later in the chapter a question about dimension.

::: {#thm-alternating-forms-space}
[Alternating Forms Form a Vector Space]

The \( k \)-linear forms on \( V \) form a subspace of the vector space \( F^{V^k} \) of all functions \( V^k \to F \), with the pointwise operations of @exm-vector-spaces (d). The alternating \( k \)-linear forms on \( V \) form a subspace of it. In particular, both are vector spaces over \( F \).
:::

::: {.proof}
We use the Subspace Test (@thm-subspace-test) twice.

The zero function is \( k \)-linear, since in each position it is the zero functional, and it is alternating, since all its values are \( 0 \).

Let \( f \) and \( g \) be \( k \)-linear and \( a \in F \). Fix a position \( i \) and vectors in the other positions, and write \( f(\dots, \x, \dots) \) for the value with \( \x \) in position \( i \). For \( \x, \y \in V \) and \( c \in F \), the pointwise definition and linearity of \( f \) and \( g \) in position \( i \) give
\[
  (f + g)(\dots, \x + \y, \dots) = f(\dots, \x, \dots) + f(\dots, \y, \dots) + g(\dots, \x, \dots) + g(\dots, \y, \dots) = (f + g)(\dots, \x, \dots) + (f + g)(\dots, \y, \dots)
\]
and
\[
  (f + g)(\dots, c\x, \dots) = c\,f(\dots, \x, \dots) + c\,g(\dots, \x, \dots) = c\,(f + g)(\dots, \x, \dots).
\]
So \( f + g \) is \( k \)-linear. In the same way \( (af)(\dots, \x + \y, \dots) = a f(\dots, \x, \dots) + a f(\dots, \y, \dots) \) and \( (af)(\dots, c\x, \dots) = c\,(af)(\dots, \x, \dots) \), using commutativity in \( F \), so \( af \) is \( k \)-linear.

If moreover \( f \) and \( g \) are alternating and \( \v_i = \v_j \) for some \( i \neq j \), then \( (f + g)(\v_1, \dots, \v_k) = 0 + 0 = 0 \) and \( (af)(\v_1, \dots, \v_k) = a \cdot 0 = 0 \). So the alternating forms are closed under both operations. This proves the theorem.
:::

For \( V = F^2 \) and \( k = 2 \), Exercise B2 shows that every alternating bilinear form is one of the forms \( f_c \) of @exm-alternating-forms (a), with \( c = f(\e_1, \e_2) \). So that space is spanned by the single non-zero form \( f_1 \), and has dimension \( 1 \). Later in this chapter we prove the same for all \( n \): the alternating \( n \)-linear forms on \( F^n \) form a space of dimension exactly \( 1 \), spanned by the determinant. The missing ingredient is how the value of an alternating form changes when its arguments are rearranged by more than one swap, which is the subject of the next section.

## Exercises

### A. Check your understanding

:::: {#exr-multilinear-alternating-forms-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define an alternating \( k \)-linear form on a vector space \( V \) over \( F \).
2. True or false: a bilinear form \( f \) on \( \nR^2 \) with \( f(\e_1, \e_1) = f(\e_2, \e_2) = 0 \) is alternating. Justify your answer.
3. True or false: every skew-symmetric bilinear form on \( \nR^5 \) is alternating. Justify your answer.
4. Let \( f \) be an alternating \( 3 \)-linear form on \( \nR^3 \) and \( \u, \v \in \nR^3 \). What is \( f(\u, \v, 2\u - \v) \)?
5. Name the move that proves an alternating form changes sign under a swap.
:::
::::

::: {.solution}
(a) A function \( f \colon V^k \to F \) that is linear in each argument when the others are fixed (@def-multilinear-form), and satisfies \( f(\v_1, \dots, \v_k) = 0 \) whenever \( \v_i = \v_j \) for some \( i \neq j \) (@def-alternating-form).

(b) False. The form \( s(\u, \v) = u_1v_2 + u_2v_1 \) is bilinear with \( s(\e_1, \e_1) = s(\e_2, \e_2) = 0 \), but \( s(\e_1 + \e_2, \e_1 + \e_2) = 2 \neq 0 \). Checking the basis vectors is not enough, because the alternating condition is about **all** vectors.

(c) True. \( \nR \) has characteristic \( 0 \), so @thm-skew-symmetric-alternating (b) applies.

(d) \( 0 \). The list \( (\u, \v, 2\u - \v) \) is linearly dependent, since \( 2\u - \v - (2\u - \v) = \0 \) with coefficients \( 2, -1, -1 \) not all zero. By @thm-alternating-properties (d) the value is \( 0 \).

(e) Put the sum of the two arguments into both positions, use \( f(\dots, \x + \y, \dots, \x + \y, \dots) = 0 \), and expand by linearity in both positions; the terms with equal arguments vanish and the two cross terms must cancel.
:::

### B. Practice

:::: {#exr-multilinear-alternating-forms-b1}
[B1: Multilinear or Alternating?]

Determine which of the following functions are multilinear, and which of those are alternating. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \nR^2 \times \nR^2 \to \nR \), \( (\u, \v) \mapsto 3u_1v_2 - 3u_2v_1 \).
2. \( \nR^2 \times \nR^2 \to \nR \), \( (\u, \v) \mapsto u_1v_2 - u_2v_1 + 1 \).
3. \( \nR^3 \times \nR^3 \times \nR^3 \to \nR \), \( (\u, \v, \w) \mapsto u_1v_2w_3 \).
4. \( M_2(\nR) \times M_2(\nR) \to \nR \), \( (A, B) \mapsto \tr(AB) - \tr(BA) \).
5. \( \nR[x] \times \nR[x] \to \nR \), \( (p, q) \mapsto p(1)q'(1) - p'(1)q(1) \).
:::
::::

::: {.solution}
(a) Multilinear and alternating: it is \( f_3 \) from @exm-alternating-forms (a) with \( c = 3 \).

(b) Not multilinear. A linear functional sends \( \0 \) to \( 0 \), but at \( \u = \0 \) the map \( \v \mapsto 0 - 0 + 1 = 1 \) does not. So it is not an alternating form either; in any case its value at \( (\u, \u) \) is \( 1 \neq 0 \).

(c) Multilinear: in each position it is a coordinate functional times a fixed scalar, as for products of functionals. Not alternating: with \( \u = \v = \e_1 + \e_2 \) and \( \w = \e_3 \), the value is \( 1 \cdot 1 \cdot 1 = 1 \neq 0 \).

(d) By @thm-trace-properties, \( \tr(AB) = \tr(BA) \), so this is the zero function. The zero function is multilinear and alternating (@thm-alternating-forms-space). This is the degenerate case.

(e) Multilinear: \( p \mapsto p(1) \) and \( p \mapsto p'(1) \) are linear, the second as a composition of differentiation (@exm-differentiation) with evaluation (@thm-evaluation-respects-operations). So for fixed \( q \), \( p \mapsto q'(1)\,p(1) - q(1)\,p'(1) \) is linear, and similarly in \( q \). Alternating: \( p(1)p'(1) - p'(1)p(1) = 0 \).
:::

:::: {#exr-multilinear-alternating-forms-b2}
[B2: Alternating Bilinear Forms on \( F^2 \)]

Let \( f \) be an alternating bilinear form on \( F^2 \). Prove that
\[
  f(\u, \v) = f(\e_1, \e_2)\,(u_1v_2 - u_2v_1) \qquad \text{for all } \u, \v \in F^2.
\]
Hence show that the alternating bilinear forms on \( F^2 \) form a space of dimension \( 1 \).
::::

::: {.solution}
Write \( \u = u_1\e_1 + u_2\e_2 \) and \( \v = v_1\e_1 + v_2\e_2 \). By linearity in the first and then in the second argument,
\[
  f(\u, \v) = u_1v_1 f(\e_1, \e_1) + u_1v_2 f(\e_1, \e_2) + u_2v_1 f(\e_2, \e_1) + u_2v_2 f(\e_2, \e_2).
\]
Since \( f \) is alternating, \( f(\e_1, \e_1) = f(\e_2, \e_2) = 0 \), and by @thm-alternating-properties (a), \( f(\e_2, \e_1) = -f(\e_1, \e_2) \). Hence \( f(\u, \v) = f(\e_1, \e_2)(u_1v_2 - u_2v_1) \).

By @thm-alternating-forms-space these forms form a vector space, and we have just shown \( f = f(\e_1, \e_2)\, f_1 \), where \( f_1(\u, \v) = u_1v_2 - u_2v_1 \) is alternating by @exm-alternating-forms (a). So \( (f_1) \) spans the space. It is non-zero, since \( f_1(\e_1, \e_2) = 1 \), so the list \( (f_1) \) is linearly independent and hence a basis. The dimension is \( 1 \).
:::

:::: {#exr-multilinear-alternating-forms-b3}
[B3: The Triple Product]

For \( \v, \w \in \nR^3 \) let \( \v \times \w = (v_2w_3 - v_3w_2,\ v_3w_1 - v_1w_3,\ v_1w_2 - v_2w_1) \), and define \( f(\u, \v, \w) = u_1(\v \times \w)_1 + u_2(\v \times \w)_2 + u_3(\v \times \w)_3 \). Show that \( f \) is an alternating \( 3 \)-linear form on \( \nR^3 \) with \( f(\e_1, \e_2, \e_3) = 1 \).
::::

::: {.solution}
*Multilinear.* Each component of \( \v \times \w \) is \( g_{rs}(\v, \w) \) or \( -g_{rs}(\v, \w) \) for a form of @exm-alternating-forms (b), hence bilinear in \( (\v, \w) \). For fixed \( \v, \w \), \( f \) is a linear functional of \( \u \) with coefficients \( (\v \times \w)_m \). For fixed \( \u \) and \( \w \), \( f = \sum_m u_m (\v \times \w)_m \) is a combination of linear functionals of \( \v \), hence linear in \( \v \); likewise in \( \w \).

*Alternating.* There are three pairs of positions. If \( \v = \w \), every component \( v_rv_s - v_sv_r \) is \( 0 \), so \( \v \times \v = \0 \) and \( f = 0 \). If \( \u = \v \),
\[
  f(\u, \u, \w) = u_1(u_2w_3 - u_3w_2) + u_2(u_3w_1 - u_1w_3) + u_3(u_1w_2 - u_2w_1) = 0,
\]
since the six terms cancel in pairs: \( u_1u_2w_3 \) with \( -u_2u_1w_3 \), \( -u_1u_3w_2 \) with \( u_3u_1w_2 \), and \( u_2u_3w_1 \) with \( -u_3u_2w_1 \). If \( \u = \w \), the same expansion \( u_1(v_2u_3 - v_3u_2) + u_2(v_3u_1 - v_1u_3) + u_3(v_1u_2 - v_2u_1) \) cancels in pairs in the same way.

*Value.* \( \e_2 \times \e_3 = (1 \cdot 1 - 0 \cdot 0,\ 0 \cdot 0 - 0 \cdot 1,\ 0 \cdot 0 - 1 \cdot 0) = (1, 0, 0) \), so \( f(\e_1, \e_2, \e_3) = 1 \).
:::

### C. Going deeper

:::: {#exr-multilinear-alternating-forms-c1}
[C1: Too Many Arguments]

Let \( V \) be finite-dimensional with \( \dim V = n \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that every alternating \( k \)-linear form on \( V \) with \( k > n \) is the zero form.
2. Deduce that the only alternating \( 3 \)-linear form on \( F^2 \) is zero, and give a non-zero alternating \( 2 \)-linear form on \( F^2 \) to show that the bound in (a) cannot be lowered to \( k \ge n \).
:::
::::

::: {.solution}
(a) Let \( f \) be an alternating \( k \)-linear form with \( k > n \), and let \( \v_1, \dots, \v_k \in V \). By @thm-size-bounds (a), a list of length \( k > \dim V \) is linearly dependent. By @thm-alternating-properties (d), \( f(\v_1, \dots, \v_k) = 0 \). Since the vectors were arbitrary, \( f \) is the zero form.

(b) Here \( \dim F^2 = 2 < 3 \), so (a) applies. For \( k = n = 2 \), the form \( f_1(\u, \v) = u_1v_2 - u_2v_1 \) of @exm-alternating-forms (a) is alternating with \( f_1(\e_1, \e_2) = 1 \neq 0 \).
:::

:::: {#exr-multilinear-alternating-forms-c2}
[C2: Bilinear Forms over \( \nF_2 \)]

::: {.enumerate options="label=(\alph*)"}
1. Let \( f \) be a bilinear form on \( F^2 \) and write \( b_{rs} = f(\e_r, \e_s) \). Show that \( f(\u, \v) = \sum_{r, s = 1}^{2} b_{rs} u_r v_s \), and that conversely every choice of four scalars \( b_{rs} \) defines a bilinear form this way. Hence there are exactly \( 16 \) bilinear forms on \( \nF_2^2 \).
2. Prove that a bilinear form on \( \nF_2^2 \) is skew-symmetric if and only if \( b_{12} = b_{21} \). How many are there?
3. Prove that a bilinear form on \( \nF_2^2 \) is alternating if and only if \( b_{11} = b_{22} = 0 \) and \( b_{12} = b_{21} \). How many are there?
4. Over \( \nR \), how do the analogous two sets of bilinear forms on \( \nR^2 \) compare? Justify your answer.
:::
::::

::: {.solution}
(a) Expanding \( \u = u_1\e_1 + u_2\e_2 \) and \( \v = v_1\e_1 + v_2\e_2 \) by linearity in each argument gives \( f(\u, \v) = \sum_{r, s} u_rv_s f(\e_r, \e_s) = \sum_{r, s} b_{rs}u_rv_s \). Conversely, for any scalars \( b_{rs} \), the function \( \sum_{r, s} b_{rs}u_rv_s \) is linear in \( \u \) for fixed \( \v \) (a combination of the coordinates \( u_r \) with coefficients \( \sum_s b_{rs}v_s \)) and similarly in \( \v \), and it takes the value \( b_{rs} \) at \( (\e_r, \e_s) \). So bilinear forms on \( F^2 \) correspond exactly to quadruples \( (b_{11}, b_{12}, b_{21}, b_{22}) \), and over \( \nF_2 \) there are \( 2^4 = 16 \).

(b) In \( \nF_2 \), \( -a = a \) for every \( a \), so \( f \) is skew-symmetric exactly when \( f(\v, \u) = f(\u, \v) \) for all \( \u, \v \). (⇒) Taking \( \u = \e_1 \), \( \v = \e_2 \) gives \( b_{21} = b_{12} \). (⇐) If \( b_{12} = b_{21} \), then \( b_{rs} = b_{sr} \) for all \( r, s \), and \( f(\v, \u) = \sum_{r, s} b_{rs}v_ru_s = \sum_{r, s} b_{sr}u_sv_r = f(\u, \v) \). The entries \( b_{11}, b_{22} \) and the common value \( b_{12} = b_{21} \) are free, so there are \( 2^3 = 8 \) skew-symmetric forms.

(c) (⇒) If \( f \) is alternating, then \( b_{11} = f(\e_1, \e_1) = 0 \) and \( b_{22} = 0 \), and \( 0 = f(\e_1 + \e_2, \e_1 + \e_2) = b_{11} + b_{12} + b_{21} + b_{22} = b_{12} + b_{21} \), so \( b_{21} = -b_{12} = b_{12} \). (⇐) With \( b_{11} = b_{22} = 0 \) and \( b_{12} = b_{21} = b \), \( f(\u, \u) = b(u_1u_2 + u_2u_1) = (1 + 1)\,b\,u_1u_2 = 0 \). Only \( b \in \{0, 1\} \) is free, so there are \( 2 \) alternating forms. Hence \( 8 - 2 = 6 \) skew-symmetric forms over \( \nF_2 \) are not alternating; \( u_1v_1 \) (with \( b_{11} = 1 \), all others \( 0 \)) is one of them, as in the warning. A brute-force check of all \( 16 \) forms against all pairs in \( \nF_2^2 \) gives the same counts, \( 8 \) and \( 2 \).

(d) Over \( \nR \) the two sets are **equal**. Alternating forms are skew-symmetric by @thm-skew-symmetric-alternating (a), and since \( \nR \) has characteristic \( 0 \), skew-symmetric forms are alternating by part (b) of that theorem. Concretely, both conditions say \( b_{11} = b_{22} = 0 \) and \( b_{21} = -b_{12} \).
:::
