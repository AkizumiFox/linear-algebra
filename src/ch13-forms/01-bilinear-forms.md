# Bilinear Forms and Their Matrices

Chapter 6 needed a function of several vectors that was linear in each of them separately, and called it a multilinear form (@def-multilinear-form). Chapter 10 needed a function of two vectors that was linear in the first, conjugate-linear in the second, and positive on the diagonal, and called it an inner product. This section takes the common skeleton of the two — two slots, linear in each, nothing else assumed — and studies it on its own. The payoff is immediate: such a function is recorded by a square matrix, exactly as a linear map is, and the whole rest of the chapter is about how that matrix behaves.

Throughout, \( V \) is a vector space over a field \( F \). From the second subsection on, \( V \) is finite-dimensional with \( \dim V = n \ge 1 \), and \( \sB = (\v_1, \dots, \v_n) \) is an ordered basis of \( V \). **No hypothesis on the characteristic of \( F \) is used anywhere in this section**, and none is used in the next one either.

## Pairing without measuring

The dot product on \( F^n \) is a machine with two inputs and one scalar output. Over \( \nR \) it does two different jobs. It **pairs**: it takes \( \x \) and \( \y \) and returns \( \sum_i x_iy_i \), linearly in each of them. And it **measures**: \( \x \cdot \x \) is a sum of squares, so it is positive unless \( \x = \0 \), and from that one fact Chapter 10 extracted lengths, angles, orthonormal bases and everything built on them.

Measuring is the fragile half. It needs an order on \( F \), so it is meaningless over \( \nC \) without a conjugation and meaningless over \( \nF_5 \) altogether. Pairing needs nothing: \( \sum_i x_iy_i \) makes sense over every field, and so do plenty of other two-slot expressions, such as \( x_1y_2 - x_2y_1 \) or \( x_1y_1 - x_2y_2 \). Chapter 6 already met the first of these as the signed area, and met the general notion as the case \( k = 2 \) of a multilinear form. We give that case its own name, because from here on it is the object of study rather than a step toward the determinant.

*A bilinear form pairs two vectors of the same space into a scalar, linearly in each slot separately.*

::: {#def-bilinear-form}
[Bilinear Form]

Let \( V \) be a vector space over a field \( F \). A **bilinear form** on \( V \) is a function \( \beta \colon V \times V \to F \) that is linear in each argument when the other is held fixed: **for all** \( \u, \u', \v, \v' \in V \) and **all** \( c \in F \),

::: {.enumerate options="label=(B\arabic*)"}
1. \( \beta(\u + \u', \v) = \beta(\u, \v) + \beta(\u', \v) \) and \( \beta(c\u, \v) = c\,\beta(\u, \v) \);
2. \( \beta(\u, \v + \v') = \beta(\u, \v) + \beta(\u, \v') \) and \( \beta(\u, c\v) = c\,\beta(\u, \v) \).
:::

Equivalently, \( \beta \) is a \( 2 \)-linear form on \( V \) in the sense of @def-multilinear-form.
:::

In words: (B1) says that for each fixed \( \v \), the function \( \u \mapsto \beta(\u, \v) \) is a linear functional on \( V \) (@def-linear-functional), and (B2) says the same for \( \v \mapsto \beta(\u, \v) \) with \( \u \) fixed. The word **fixed** is the whole content. Nothing is assumed about how the two slots compare: \( \beta(\u, \v) \) and \( \beta(\v, \u) \) may be unrelated, and \( \beta(\v, \v) \) may be any scalar at all, including \( 0 \) for a non-zero \( \v \).

Two consequences come free from linearity in one slot. Taking \( c = 0 \) in (B1) gives \( \beta(\0, \v) = 0 \) for every \( \v \), and likewise \( \beta(\u, \0) = 0 \). And by induction on the number of terms,
\[
\beta\Bigl(\sum_i a_i\u_i,\ \sum_j b_j\v_j\Bigr) = \sum_{i,j} a_ib_j\,\beta(\u_i, \v_j),
\]
which is the identity everything in this section rests on: a bilinear form is determined by its values on pairs drawn from a spanning set.

::: {#exm-bilinear-forms-first}
[Six two-slot functions]

Decide which of the following are bilinear forms on the given space over the given field.

::: {.enumerate options="label=(\alph*)"}
1. The dot product on \( F^n \): \( \beta(\x, \y) = x_1y_1 + \dots + x_ny_n \).
2. On \( F^n \), for a fixed \( \A \in M_n(F) \): \( \beta_{\A}(\x, \y) = \x\tp\A\y \).
3. On \( F^2 \): \( \beta(\x, \y) = x_1y_2 - x_2y_1 \).
4. On \( \nR[x]_{\le 2} \): \( \beta(f, g) = \int_0^1 f(t)g(t)\,\dd t \).
5. On any \( V \): the zero function \( \beta(\u, \v) = 0 \).
6. On \( \nR^n \): \( \beta(\x, \y) = \norm{\x}\,\norm{\y} \), the product of the Euclidean lengths.
:::
:::

::: {.solution}
(a) Fix \( \y \). Then \( \x \mapsto \sum_i x_iy_i \) is a linear functional on \( F^n \), since it is a fixed linear combination of the coordinate functionals (@thm-functionals-on-fn). Fixing \( \x \) gives the same statement in \( \y \). So (B1) and (B2) hold and the dot product is bilinear.

(b) With \( \A = \I_n \) this is (a). In general, write out the entries: \( \x\tp\A\y = \sum_{i,j} a_{ij}x_iy_j \). For fixed \( \y \) this is \( \sum_i \bigl(\sum_j a_{ij}y_j\bigr)x_i \), a fixed linear combination of the coordinates of \( \x \), hence a linear functional; symmetrically in \( \y \). So \( \beta_{\A} \) is bilinear for **every** \( \A \), symmetric or not. Part (c) below is the case \( \A = \begin{psmallmatrix} 0 & 1 \\ -1 & 0\end{psmallmatrix} \).

(c) This is the signed area of Chapter 6, and it is bilinear by @exm-alternating-forms (a). It is worth noticing what it does on the diagonal: \( \beta(\x, \x) = x_1x_2 - x_2x_1 = 0 \) for **every** \( \x \). A bilinear form may vanish identically on the diagonal without being the zero form.

(d) For fixed \( g \), the map \( f \mapsto \int_0^1 fg \) is linear, because the integral of a sum is the sum of the integrals and constants come out. Symmetrically in \( g \). So \( \beta \) is bilinear. Here \( \beta(f, f) = \int_0^1 f^2 \ge 0 \), so over \( \nR \) this form does measure: it is the inner product of Chapter 10.

(e) Both clauses read \( 0 = 0 + 0 \) and \( 0 = c \cdot 0 \). The zero form is bilinear on every space over every field. It is the degenerate case, and it matters: it shows that a bilinear form can carry no information whatsoever, and it is the form whose matrix below is the zero matrix.

(f) Not bilinear. Fix \( \y = \e_1 \). Then \( \beta(\e_1, \e_1) + \beta(-\e_1, \e_1) = 1 + 1 = 2 \), while \( \beta(\e_1 + (-\e_1), \e_1) = \beta(\0, \e_1) = 0 \). Additivity in the first slot fails, so (B1) fails. The homogeneity half of (B1) also fails, since \( \beta(-\e_1, \e_1) = 1 \ne -\beta(\e_1, \e_1) \).
:::

Item (f) is the non-example by minimal change worth remembering: the Cauchy–Schwarz inequality says that \( \lvert\x \cdot \y\rvert \le \norm{\x}\norm{\y} \), so \( \norm{\x}\norm{\y} \) sits right next to the dot product numerically, and yet it is not a form at all, because the absolute value hidden in the norm destroys additivity. A second minimal change makes the same point more cheaply: \( \beta(\x, \y) = x_1y_1 + 1 \) fails (B1) because \( \beta(\0, \0) = 1 \ne 0 \).

::: {.warning}
**Bilinear is not linear.** A bilinear form is not a linear function of the pair \( (\u, \v) \), and the two properties are not even compatible in general. For the dot product on \( \nR^2 \), doubling both arguments multiplies the value by \( 4 \): \( \beta(2\e_1, 2\e_1) = 4 \), not \( 2\beta(\e_1, \e_1) = 2 \). Sums may only be split **one slot at a time**, with the other slot held frozen. Chapter 6 gave this warning for multilinear forms in general; it is repeated here because it is the mistake readers make most often when a form is written with the familiar-looking symbol \( \x\tp\A\y \).
:::

::: {.remark}
The same definition with two different spaces, \( \beta \colon V \times W \to F \) linear in each slot, is called a **bilinear pairing** of \( V \) and \( W \). The basic example is the evaluation pairing \( V^{*} \times V \to F \), \( (\varphi, \v) \mapsto \varphi(\v) \), which is linear in \( \varphi \) by the definition of the operations on \( V^{*} \) (@def-dual-space) and linear in \( \v \) because \( \varphi \) is. We insist on \( V = W \) in @def-bilinear-form because the questions of this chapter — is \( \beta(\u,\v) \) equal to \( \beta(\v,\u) \), what is \( \beta(\v,\v) \), which vectors are orthogonal to which — only make sense when both slots hold vectors of the same space.
:::

## The matrix of a form

The displayed expansion above says that a bilinear form on a finite-dimensional space is determined by finitely many numbers: the values \( \beta(\v_i, \v_j) \) on pairs of basis vectors. There are \( n^2 \) of them, they are indexed by a row and a column, and that is a matrix. Chapter 3 recorded a linear map by a matrix in exactly the same spirit (@def-matrix-of-linear-map), and the only difference is where the bases sit. There the two bases belonged to the input space and the output space. A form has no output space to speak of, but it has two **slots**, and each slot has to be fed a basis before the table can be written down. Throughout this chapter both slots hold vectors of the same \( V \) and we feed them the same basis, so the two choices coincide; the notation still records both, with the subscript naming the basis used on the first slot and the superscript the basis used on the second.

*The matrix of a form is its table of values on pairs of basis vectors.*

::: {#def-form-matrix}
[Matrix of a Bilinear Form]

Let \( \beta \) be a bilinear form on a finite-dimensional \( V \) with ordered basis \( \sB = (\v_1, \dots, \v_n) \). The **matrix of \( \beta \) with respect to \( \sB \)**, also called its **Gram matrix**, is the matrix \( \mtx{\beta}{\sB}{\sB} \in M_n(F) \) with entries
\[
\bigl(\mtx{\beta}{\sB}{\sB}\bigr)_{ij} \coloneqq \beta(\v_i, \v_j) .
\]
:::

In words: the entry in row \( i \) and column \( j \) is the value of \( \beta \) with the \( i \)-th basis vector in the **left** slot and the \( j \)-th in the **right** slot. The subscript is the basis read into the left slot and the superscript the basis read into the right one; here they are the same \( \sB \), and the notation writes it twice rather than leaving a slot empty. The order matters, because \( \beta(\v_i, \v_j) \) and \( \beta(\v_j, \v_i) \) need not agree; the convention chosen here is the one that makes the recovery formula below carry no transpose on the **matrix**.

Chapter 10 also called a matrix of pairings a Gram matrix, and the two conventions differ, so it is worth saying how. @def-gram-matrix set \( (\G)_{ij} = \inner{\v_j}{\v_i} \), with the indices crossed, because an inner product is conjugate-linear in its second slot and the crossing is what makes \( \G \) Hermitian and \( \x^{*}\G\x \) come out as a squared norm. A bilinear form has no conjugation to accommodate, so here the natural order is the uncrossed one, which is what makes the recovery formula below free of transposes. For a real symmetric form the two agree; in general each is the transpose of the other.

Nothing needs checking for well-definedness: once \( \sB \) is fixed, each entry is a single value of a function. What does need saying is that no information is lost.

::: {#thm-form-matrix-determines}
[Forms and Matrices Correspond]

Let \( V \) be an \( n \)-dimensional vector space over \( F \) with ordered basis \( \sB \), and let \( \beta \) be a bilinear form on \( V \) with \( \A = \mtx{\beta}{\sB}{\sB} \).

::: {.enumerate options="label=(\alph*)"}
1. For all \( \u, \v \in V \),
\[
\beta(\u, \v) = \coord{\u}{\sB}\tp\,\A\,\coord{\v}{\sB} .
\]
2. \( \A \) is the **only** matrix in \( M_n(F) \) with this property.
3. The assignment \( \beta \mapsto \mtx{\beta}{\sB}{\sB} \) is a bijection from the set of bilinear forms on \( V \) onto \( M_n(F) \), and it respects sums and scalar multiples: \( \mtx{\beta + \gamma}{\sB}{\sB} = \mtx{\beta}{\sB}{\sB} + \mtx{\gamma}{\sB}{\sB} \) and \( \mtx{c\beta}{\sB}{\sB} = c\,\mtx{\beta}{\sB}{\sB} \).
:::
:::

::: {.idea}
Part (a) is the expansion \( \beta(\sum a_i\v_i, \sum b_j\v_j) = \sum_{i,j}a_ib_j\beta(\v_i,\v_j) \) with the double sum recognized as a matrix product. For (b), feed the property a pair of basis vectors and watch it return a single entry. For (c), (b) gives injectivity, and surjectivity is @exm-bilinear-forms-first (b) transported to \( V \) through coordinates.
:::

::: {.proof}
(a) Write \( \coord{\u}{\sB} = (a_1, \dots, a_n) \) and \( \coord{\v}{\sB} = (b_1, \dots, b_n) \), so that \( \u = \sum_i a_i\v_i \) and \( \v = \sum_j b_j\v_j \). Expanding one slot at a time, by (B1) and then (B2),
\[
\beta(\u, \v) = \sum_{i=1}^{n}\sum_{j=1}^{n} a_ib_j\,\beta(\v_i, \v_j) = \sum_{i,j} a_i\,a_{ij}\,b_j ,
\]
writing \( a_{ij} = \beta(\v_i, \v_j) \) for the entries of \( \A \). The last sum is the \( 1 \times 1 \) matrix product \( \coord{\u}{\sB}\tp\A\coord{\v}{\sB} \), by the definition of matrix multiplication (@def-matrix-multiplication).

(b) Suppose \( \M \in M_n(F) \) also satisfies \( \beta(\u, \v) = \coord{\u}{\sB}\tp\M\coord{\v}{\sB} \) for all \( \u, \v \). Take \( \u = \v_i \) and \( \v = \v_j \). Then \( \coord{\v_i}{\sB} = \e_i \) and \( \coord{\v_j}{\sB} = \e_j \), so the right-hand side is \( \e_i\tp\M\e_j = m_{ij} \), while the left-hand side is \( \beta(\v_i, \v_j) = a_{ij} \). Hence \( m_{ij} = a_{ij} \) for all \( i, j \), that is, \( \M = \A \).

(c) *Injective.* If \( \mtx{\beta}{\sB}{\sB} = \mtx{\gamma}{\sB}{\sB} \), then by (a) the two forms agree at every pair \( (\u, \v) \), so \( \beta = \gamma \).

*Surjective.* Given \( \M \in M_n(F) \), define \( \gamma(\u, \v) \coloneqq \coord{\u}{\sB}\tp\M\coord{\v}{\sB} \). The coordinate map \( \v \mapsto \coord{\v}{\sB} \) is linear (@cor-coordinate-isomorphism), and \( (\x, \y) \mapsto \x\tp\M\y \) is bilinear on \( F^n \) by @exm-bilinear-forms-first (b); composing a bilinear form with a linear map in each slot leaves it bilinear, so \( \gamma \) is a bilinear form on \( V \). By (b) its matrix is \( \M \).

*Linear.* The forms \( \beta + \gamma \) and \( c\beta \) are defined pointwise, so their values at \( (\v_i, \v_j) \) are \( \beta(\v_i,\v_j) + \gamma(\v_i,\v_j) \) and \( c\,\beta(\v_i,\v_j) \). These are the entries of \( \mtx{\beta}{\sB}{\sB} + \mtx{\gamma}{\sB}{\sB} \) and of \( c\,\mtx{\beta}{\sB}{\sB} \). This proves the theorem.
:::

So bilinear forms on an \( n \)-dimensional space are the same thing as \( n \times n \) matrices, once a basis is fixed — and in particular they form a vector space of dimension \( n^2 \). The qualification "once a basis is fixed" is not decoration; the next section is entirely about what happens when the basis is changed.

::: {#exm-form-matrices}
[Four Gram matrices]

Compute \( \mtx{\beta}{\sB}{\sB} \) in each case.

::: {.enumerate options="label=(\alph*)"}
1. The dot product on \( F^n \), with \( \sB = \sE \) the standard basis.
2. \( \beta_{\A}(\x, \y) = \x\tp\A\y \) on \( F^n \), with \( \sB = \sE \).
3. The signed area \( \beta(\x, \y) = x_1y_2 - x_2y_1 \) on \( F^2 \), with \( \sB = \sE \).
4. \( \beta(f, g) = \int_0^1 fg \) on \( \nR[x]_{\le 2} \), with \( \sB = (1, x, x^2) \).
:::
:::

::: {.solution}
(a) \( \beta(\e_i, \e_j) = \delta_{ij} \), so \( \mtx{\beta}{\sE}{\sE} = \I_n \). The dot product is the form whose matrix is the identity.

(b) \( \beta_{\A}(\e_i, \e_j) = \e_i\tp\A\e_j = a_{ij} \), so \( \mtx{\beta_{\A}}{\sE}{\sE} = \A \). Together with @thm-form-matrix-determines (c) this says that on \( F^n \) with the standard basis, "form" and "matrix" are two words for the same data, and \( \x\tp\A\y \) is the general form.

(c) \( \beta(\e_1, \e_1) = 0 \), \( \beta(\e_1, \e_2) = 1 \), \( \beta(\e_2, \e_1) = -1 \), \( \beta(\e_2, \e_2) = 0 \), so
\[
\mtx{\beta}{\sE}{\sE} = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}.
\]
The matrix is not symmetric, and its diagonal is zero — the two features that will separate this form from the dot product throughout the chapter.

(d) With \( \sB = (1, x, x^2) \) the \( (i,j) \) entry is \( \int_0^1 t^{\,i-1}t^{\,j-1}\dd t = 1/(i + j - 1) \), so
\[
\mtx{\beta}{\sB}{\sB} = \begin{pmatrix}
1 & \tfrac12 & \tfrac13 \\[2pt]
\tfrac12 & \tfrac13 & \tfrac14 \\[2pt]
\tfrac13 & \tfrac14 & \tfrac15
\end{pmatrix}.
\]
This matrix is symmetric, as it must be, since \( \beta(f, g) = \beta(g, f) \). Its determinant is \( 1/2160 \), so it is invertible; what that means for \( \beta \) is the subject of the last part of this section.
:::

::: {.check}
A bilinear form \( \beta \) on \( F^2 \) satisfies \( \beta(\e_1, \e_1) = 2 \), \( \beta(\e_1, \e_2) = -1 \), \( \beta(\e_2, \e_1) = 3 \) and \( \beta(\e_2, \e_2) = 0 \). What is \( \beta\bigl((1,1), (1,-1)\bigr) \)?
:::

::: {.solution}
The matrix is \( \A = \begin{psmallmatrix} 2 & -1 \\ 3 & 0\end{psmallmatrix} \), and by @thm-form-matrix-determines (a),
\[
\beta\bigl((1,1),(1,-1)\bigr)
= \begin{pmatrix} 1 & 1\end{pmatrix}
\begin{pmatrix} 2 & -1 \\ 3 & 0\end{pmatrix}
\begin{pmatrix} 1 \\ -1\end{pmatrix}
= 6 .
\]
Expanding by hand gives the same. The pair is \( (\e_1 + \e_2,\ \e_1 - \e_2) \), so the four terms are
\[
\beta(\e_1,\e_1) - \beta(\e_1,\e_2) + \beta(\e_2,\e_1) - \beta(\e_2,\e_2),
\]
which is \( 2 - (-1) + 3 - 0 = 6 \). Note that the two off-diagonal values enter with **opposite** roles: \( \beta(\e_1,\e_2) \) comes from the minus sign in the right slot, \( \beta(\e_2,\e_1) \) from the plus sign in the left one. Since \( \beta(\e_1,\e_2) \ne \beta(\e_2,\e_1) \) here, swapping them would change the answer.
:::

Now the warning that the rest of the chapter exists to manage.

::: {.warning}
**The matrix of a form and the matrix of a map are different objects with the same name.** Both are square arrays attached to \( V \) and a basis, both are written \( \A \), and both change when the basis changes — by **different rules**. If \( \P \) is the change-of-coordinates matrix between the old and the new basis, then
\[
\text{a map: } \A \mapsto \P^{-1}\A\P,
\qquad
\text{a form: } \A \mapsto \P\tp\A\P .
\]
The first is @thm-change-of-basis-maps; the second is proved in the next section. They agree only when \( \P\tp = \P^{-1} \). Concretely, take \( \A = \diag(1,2) \) and \( \P = \begin{psmallmatrix} 1 & 1 \\ 0 & 1\end{psmallmatrix} \). Then
\[
\P^{-1}\A\P = \begin{pmatrix} 1 & -1 \\ 0 & 2\end{pmatrix},
\qquad
\P\tp\A\P = \begin{pmatrix} 1 & 1 \\ 1 & 3\end{pmatrix} .
\]
The first still has eigenvalues \( 1 \) and \( 2 \); the second has eigenvalues \( 2 \pm \sqrt2 \). Same \( \A \), same \( \P \), two answers with nothing in common. Before writing \( \A \) down, ask what it eats: a map eats one vector and returns a vector, so \( \A\x \) is meaningful; a form eats two vectors and returns a scalar, so \( \x\tp\A\y \) is meaningful and \( \A\x \) is a meaningless intermediate. Almost every error in this chapter is this confusion.
:::

## The form as a map into the dual space

Fixing the right slot of \( \beta \) leaves a function of the left slot, and clause (B1) says that function is a linear functional. So each \( \v \in V \) produces an element of \( V^{*} \) (@def-dual-space), and clause (B2) says the production is itself linear. That is a linear map \( V \to V^{*} \), and it is the cleanest way to say what it means for a form to be non-degenerate.

Write \( R_\beta \colon V \to V^{*} \) for the map sending \( \v \) to the functional \( \beta(\cdot, \v) \), that is,
\[
\bigl(R_\beta(\v)\bigr)(\u) = \beta(\u, \v) \qquad (\u, \v \in V).
\]
The letter is local to this section and the subscript names the form; \( R \) is for the **right** slot, the one that is fixed. That \( R_\beta(\v) \) lies in \( V^{*} \) is (B1), and that \( R_\beta \) is linear is (B2). Its kernel has a name.

::: {#def-radical}
[Radical of a Form]

Let \( \beta \) be a bilinear form on \( V \). The **radical** of \( \beta \) is
\[
\operatorname{rad}(\beta) \coloneqq \{\, \v \in V : \beta(\u, \v) = 0 \text{ for every } \u \in V \,\} = \ker R_\beta ,
\]
a subspace of \( V \). Its elements are the vectors that **every** vector is orthogonal to.
:::

::: {#def-nondegenerate}
[Non-degenerate Form]

A bilinear form \( \beta \) on \( V \) is **non-degenerate** if \( \operatorname{rad}(\beta) = \{\0\} \), that is, if for every **non-zero** \( \v \in V \) there **exists** \( \u \in V \) with \( \beta(\u, \v) \ne 0 \). Otherwise \( \beta \) is **degenerate**.
:::

In words: non-degeneracy says that no non-zero vector is invisible to the form. It does not say that \( \beta(\v,\v) \ne 0 \), and it does not say that \( \beta \) is positive in any sense; it only says that a vector which the form cannot distinguish from \( \0 \) must be \( \0 \). On a finite-dimensional space it is a rank condition.

::: {#prp-nondegenerate-iff-invertible}
[Non-degeneracy is invertibility of the Gram matrix]

Let \( \beta \) be a bilinear form on an \( n \)-dimensional \( V \) with ordered basis \( \sB \), and put \( \A = \mtx{\beta}{\sB}{\sB} \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \A \) is the matrix of \( R_\beta \) from the basis \( \sB \) to the dual basis \( \sB^{*} \); that is, \( \A = \mtx{R_\beta}{\sB}{\sB^{*}} \).
2. \( \dim\operatorname{rad}(\beta) = n - \rank\A \).
3. The following are equivalent: \( \beta \) is non-degenerate; \( \A \) is invertible; \( R_\beta \) is an isomorphism \( V \to V^{*} \).
:::
:::

::: {.idea}
Only (a) has content, and it is one line once the right formula is recalled: the coordinates of a functional in the dual basis are its values on \( \sB \) (@thm-dual-basis (c)), and the values of \( R_\beta(\v_j) \) on \( \sB \) are the entries of the \( j \)-th column of \( \A \). Parts (b) and (c) are then Rank–Nullity and the invertible matrix theorem, applied to a map we now know the matrix of.
:::

::: {.proof}
(a) By @def-matrix-of-linear-map, the \( j \)-th column of \( \mtx{R_\beta}{\sB}{\sB^{*}} \) is \( \coord{R_\beta(\v_j)}{\sB^{*}} \). By @thm-dual-basis (c), a functional \( \varphi \in V^{*} \) has \( \varphi = \sum_i \varphi(\v_i)\varphi_i \) in the dual basis \( \sB^{*} = (\varphi_1, \dots, \varphi_n) \), so the \( i \)-th coordinate of \( R_\beta(\v_j) \) is \( \bigl(R_\beta(\v_j)\bigr)(\v_i) = \beta(\v_i, \v_j) = a_{ij} \). Hence the \( (i,j) \) entry of \( \mtx{R_\beta}{\sB}{\sB^{*}} \) is \( a_{ij} \), as claimed.

(b) By (a) and @thm-rank-map-equals-rank-matrix, \( \rank R_\beta = \rank\A \). Since \( \operatorname{rad}(\beta) = \ker R_\beta \), Rank–Nullity (@thm-rank-nullity) gives \( \dim\operatorname{rad}(\beta) = n - \rank\A \).

(c) By (b), \( \operatorname{rad}(\beta) = \{\0\} \) if and only if \( \rank\A = n \), which by @thm-invertible-tfae is exactly invertibility of \( \A \). Since \( \dim V^{*} = n = \dim V \) (@cor-dimension-dual-space), the map \( R_\beta \) is an isomorphism if and only if it is injective (@cor-rank-nullity-consequences (e)), that is, if and only if its kernel is \( \{\0\} \) (@thm-injective-iff-trivial-kernel). This proves the proposition.
:::

::: {.remark}
Freezing the **left** slot instead gives a second map \( \u \mapsto \beta(\u, \cdot) \), whose kernel is the **left radical** \( \{\u : \beta(\u,\v) = 0 \text{ for all } \v\} \). The same computation shows its matrix is \( \A\tp \), so by @thm-row-rank-equals-column-rank and @thm-rank-nullity the two radicals have the same dimension — although, as @exr-bilinear-forms-b3 shows, they need not be the same subspace. In particular "non-degenerate" means the same thing read from either side, and for the symmetric forms that occupy most of this chapter the two radicals coincide.
:::

::: {#exm-radical-examples}
[Three radicals]

Find \( \operatorname{rad}(\beta) \) and decide degeneracy.

::: {.enumerate options="label=(\alph*)"}
1. \( \beta(\x, \y) = x_1y_1 \) on \( F^2 \).
2. \( \beta(\x, \y) = x_1y_1 - x_2y_2 \) on \( \nR^2 \).
3. The zero form on any \( V \ne \{\0\} \).
:::
:::

::: {.solution}
(a) \( \mtx{\beta}{\sE}{\sE} = \begin{psmallmatrix} 1 & 0 \\ 0 & 0\end{psmallmatrix} \), of rank \( 1 \), so the radical is one-dimensional by @prp-nondegenerate-iff-invertible (b). Explicitly, \( \beta(\u, \v) = u_1v_1 \) vanishes for all \( \u \) exactly when \( v_1 = 0 \), so \( \operatorname{rad}(\beta) = \Span(\e_2) \). Degenerate.

(b) \( \mtx{\beta}{\sE}{\sE} = \diag(1, -1) \), invertible, so \( \beta \) is non-degenerate. Yet \( \beta\bigl((1,1),(1,1)\bigr) = 1 - 1 = 0 \): a non-zero vector on which the form vanishes when paired **with itself**. Non-degeneracy forbids a vector orthogonal to everything; it says nothing about a vector orthogonal to itself. This form is the one this chapter returns to twice, in the sections on isotropic vectors and on Minkowski space.

(c) The matrix is \( 0 \), of rank \( 0 \), and \( \operatorname{rad}(\beta) = V \). This is the extreme degenerate case: every vector is invisible.
:::

::: {.warning}
**Non-degenerate does not mean definite, and the radical is not the set where \( \beta(\v,\v) = 0 \).** Example (b) above is non-degenerate, and the set \( \{\v : \beta(\v,\v) = 0\} \) is the pair of lines \( x_2 = \pm x_1 \) — not a subspace, and not the radical, which is \( \{\0\} \). Example (c) of @exm-bilinear-forms-first has \( \beta(\v,\v) = 0 \) for **every** \( \v \) and is still non-degenerate, since its matrix \( \begin{psmallmatrix} 0 & 1 \\ -1 & 0\end{psmallmatrix} \) is invertible. An inner-product-trained reader expects "\( \beta(\v,\v) = 0 \Rightarrow \v = \0 \)", and that expectation is a theorem about positive definite forms over \( \nR \), not about forms.
:::

::: {.check}
Let \( \beta \) be a bilinear form on a finite-dimensional \( V \), and let \( U = \operatorname{rad}(\beta) \). Is \( \beta \) non-degenerate on the subspace \( U \)?
:::

::: {.solution}
No, unless \( U = \{\0\} \) — and then only for a silly reason. The restriction of \( \beta \) to \( U \times U \) is the **zero** form, since \( \beta(\u, \v) = 0 \) already for \( \u \in V \) and \( \v \in U \). The zero form on a non-zero space is degenerate, so the restriction is non-degenerate exactly when \( U = \{\0\} \), that is, exactly when \( \beta \) was non-degenerate to begin with. The point of the question is that "non-degenerate" is a property of a form **on a specified space**, and restricting changes the space.
:::

## Exercises

### A. Check your understanding

::: {#exr-bilinear-forms-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define what it means for \( \beta \colon V \times V \to F \) to be a bilinear form, stating both clauses in full.
2. Define the matrix \( \mtx{\beta}{\sB}{\sB} \) of a bilinear form with respect to an ordered basis \( \sB \), and state how \( \beta(\u, \v) \) is recovered from it.
3. Determine whether the following is correct, with a reason: every bilinear form on \( F^n \) is \( \beta(\x, \y) = \x\tp\A\y \) for exactly one \( \A \in M_n(F) \).
4. Define the radical of \( \beta \) and state what it means for \( \beta \) to be non-degenerate.
5. Determine whether the following is correct, with a reason: if \( \beta(\v, \v) = 0 \) for some \( \v \ne \0 \), then \( \beta \) is degenerate.
:::
:::

::: {.solution}
(a) @def-bilinear-form: linearity in the left slot for each fixed right argument, (B1), and linearity in the right slot for each fixed left argument, (B2).

(b) @def-form-matrix: \( \bigl(\mtx{\beta}{\sB}{\sB}\bigr)_{ij} = \beta(\v_i, \v_j) \). Recovery is @thm-form-matrix-determines (a): \( \beta(\u,\v) = \coord{\u}{\sB}\tp\mtx{\beta}{\sB}{\sB}\coord{\v}{\sB} \).

(c) Correct. Existence and uniqueness are @thm-form-matrix-determines (c) and (b) with \( \sB = \sE \), for which \( \coord{\x}{\sE} = \x \).

(d) @def-radical and @def-nondegenerate: \( \operatorname{rad}(\beta) = \{\v : \beta(\u,\v) = 0 \text{ for all } \u\} \), and \( \beta \) is non-degenerate when this is \( \{\0\} \).

(e) Incorrect. The two conditions are unrelated. The signed area on \( F^2 \) has \( \beta(\v,\v) = 0 \) for every \( \v \) and is non-degenerate, since its matrix \( \begin{psmallmatrix} 0 & 1 \\ -1 & 0\end{psmallmatrix} \) is invertible (@prp-nondegenerate-iff-invertible).
:::

### B. Practice

::: {#exr-bilinear-forms-b1}
[B1: Which are forms?]

Determine which of the following are bilinear forms on the given space. Justify your answer; for those that fail, name the clause that fails and give a witness.

::: {.enumerate options="label=(\alph*)"}
1. On \( \nR^2 \): \( \beta(\x, \y) = x_1y_1 + 2x_1y_2 - 3x_2y_1 \).
2. On \( \nR^2 \): \( \beta(\x, \y) = x_1y_1 + 1 \).
3. On \( \nR[x]_{\le 2} \): \( \beta(f, g) = f(1)g(2) - f(0)g(0) \).
4. On \( \nR^2 \): \( \beta(\x, \y) = x_1^2y_1 \).
5. On \( M_2(\nR) \): \( \beta(\X, \Y) = \tr(\X\tp\Y) \).
:::
:::

::: {.solution}
(a) Bilinear: it is \( \x\tp\A\y \) with \( \A = \begin{psmallmatrix} 1 & 2 \\ -3 & 0\end{psmallmatrix} \), so @exm-bilinear-forms-first (b) applies.

(b) Not bilinear. Clause (B1) fails: \( \beta(\0, \0) = 1 \), whereas homogeneity with \( c = 0 \) forces \( \beta(\0, \y) = 0 \) for any bilinear form.

(c) Bilinear. Evaluation at a point is linear (@thm-evaluation-respects-operations), so for fixed \( g \) the map \( f \mapsto g(2)f(1) - g(0)f(0) \) is a linear combination of two linear functionals, hence linear; symmetrically in \( g \).

(d) Not bilinear. Clause (B1) fails in the additive half: with \( \y = \e_1 \), \( \beta(\e_1 + \e_1, \e_1) = 4 \) while \( \beta(\e_1,\e_1) + \beta(\e_1,\e_1) = 2 \). The homogeneity half fails too, since \( \beta(c\x, \y) = c^2x_1^2y_1 \).

(e) Bilinear. By @thm-transpose-properties and linearity of the trace (@thm-trace-properties), for fixed \( \Y \) the map \( \X \mapsto \tr(\X\tp\Y) \) is linear, and for fixed \( \X \) the map \( \Y \mapsto \tr(\X\tp\Y) \) is linear. This is the Frobenius inner product of Chapter 10, seen as a form.
:::

::: {#exr-bilinear-forms-b2}
[B2: A Gram matrix from sample values]

On \( V = \nR[x]_{\le 2} \), define \( \beta(f, g) = f(0)g(0) + f(1)g(1) + f(2)g(2) \).

::: {.enumerate options="label=(\alph*)"}
1. Verify that \( \beta \) is a bilinear form and compute \( \mtx{\beta}{\sB}{\sB} \) for \( \sB = (1, x, x^2) \).
2. Compute \( \beta(1 + x,\ x^2 - 1) \) directly from the definition, and again from the matrix. Check that the answers agree.
3. Hence decide whether \( \beta \) is non-degenerate.
:::
:::

::: {.solution}
(a) Each of the three terms is a product of two evaluations, hence bilinear as in @exr-bilinear-forms-b1 (c), and a sum of bilinear forms is bilinear by @thm-form-matrix-determines (c). Numbering rows and columns \( 1, 2, 3 \) for \( 1, x, x^2 \), the \( (i,j) \) entry is \( \sum_{t \in \{0,1,2\}} t^{\,i-1}t^{\,j-1} \), with \( 0^0 = 1 \). So
\[
\mtx{\beta}{\sB}{\sB} = \begin{pmatrix} 3 & 3 & 5 \\ 3 & 5 & 9 \\ 5 & 9 & 17 \end{pmatrix}.
\]

(b) Directly: \( f = 1 + x \) takes the values \( 1, 2, 3 \) at \( 0, 1, 2 \), and \( g = x^2 - 1 \) takes the values \( -1, 0, 3 \). So \( \beta(f, g) = 1(-1) + 2 \cdot 0 + 3 \cdot 3 = 8 \). From the matrix, \( \coord{f}{\sB} = (1,1,0) \) and \( \coord{g}{\sB} = (-1,0,1) \), and
\[
\mtx{\beta}{\sB}{\sB}\coord{g}{\sB} = (2, 6, 12),
\qquad
(1,1,0) \cdot (2,6,12) = 8 .
\]

(c) Let \( \M \) be the matrix with rows \( (1, t, t^2) \) for \( t = 0, 1, 2 \). Then \( \mtx{\beta}{\sB}{\sB} = \M\tp\M \), and \( \det\M = 2 \) by the Vandermonde formula (@thm-vandermonde-determinant), so \( \det\mtx{\beta}{\sB}{\sB} = 4 \ne 0 \) by @thm-det-multiplicative and @thm-det-transpose. By @prp-nondegenerate-iff-invertible, \( \beta \) is non-degenerate.
:::

::: {#exr-bilinear-forms-b3}
[B3: Two radicals]

On \( F^3 \), let \( \beta(\x, \y) = \x\tp\A\y \) with
\[
\A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 1 & 2 & 3 \end{pmatrix}.
\]
Find \( \operatorname{rad}(\beta) \) and the left radical, give a basis of each, and decide whether they are equal.
:::

::: {.solution}
Every row of \( \A \) is a multiple of \( (1, 2, 3) \), so \( \rank\A = 1 \) and both radicals have dimension \( 3 - 1 = 2 \), by @prp-nondegenerate-iff-invertible (b) and the remark following it.

The radical is \( \nul(\A) = \{\y : y_1 + 2y_2 + 3y_3 = 0\} \), with basis \( (-2, 1, 0) \) and \( (-3, 0, 1) \).

The left radical is \( \nul(\A\tp) \). Every row of \( \A\tp \) is a multiple of \( (1, 2, 1) \), so it is \( \{\x : x_1 + 2x_2 + x_3 = 0\} \), with basis \( (-2, 1, 0) \) and \( (-1, 0, 1) \).

They are **not** equal: \( (-3, 0, 1) \) lies in the radical but \( -3 + 0 + 1 = -2 \ne 0 \), so it is not in the left radical. Equal dimensions, different subspaces. In particular \( \beta \) is degenerate.
:::

### C. Going deeper

::: {#exr-bilinear-forms-c1}
[C1: Over \( \nF_2 \)]

Let \( \beta(\x, \y) = x_1y_1 + x_2y_2 \) on \( V = \nF_2^2 \).

::: {.enumerate options="label=(\alph*)"}
1. Write down \( \mtx{\beta}{\sE}{\sE} \) and prove that \( \beta \) is non-degenerate.
2. Find every \( \v \in V \) with \( \beta(\v, \v) = 0 \).
3. Hence explain why the argument "\( \beta(\v,\v) = 0 \) only for \( \v = \0 \)" cannot be used to prove non-degeneracy over a general field, even for the dot product.
:::
:::

::: {.solution}
(a) \( \mtx{\beta}{\sE}{\sE} = \I_2 \), which is invertible, so \( \beta \) is non-degenerate by @prp-nondegenerate-iff-invertible.

(b) \( \beta(\v, \v) = v_1^2 + v_2^2 \). In \( \nF_2 \) every element satisfies \( t^2 = t \), so this is \( v_1 + v_2 \), which vanishes for \( \v = (0,0) \) and \( \v = (1,1) \). So the non-zero vector \( (1,1) \) satisfies \( \beta(\v,\v) = 0 \).

(c) Over \( \nR \), \( \beta(\v,\v) = v_1^2 + v_2^2 \) is a sum of squares and vanishes only at \( \0 \), so the implication holds there; the proof uses that a sum of non-negative reals is zero only when each term is. Over \( \nF_2 \) there is no order, nothing is non-negative, and the conclusion is false for \( (1,1) \) even though the form is the dot product and is non-degenerate. Non-degeneracy is a statement about the rank of a matrix and survives the change of field; the diagonal statement is a statement about positivity and does not.
:::

::: {#exr-bilinear-forms-c2}
[C2: Orthogonal complements for a form]

Let \( \beta \) be a bilinear form on a vector space \( V \) with \( \dim V = n \), and for a subspace \( U \subseteq V \) put
\[
U^{\perp_\beta} \coloneqq \{\, \v \in V : \beta(\u, \v) = 0 \text{ for every } \u \in U \,\}.
\]

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( U^{\perp_\beta} \) is a subspace and that \( \dim U^{\perp_\beta} \ge n - \dim U \).
2. Prove that equality holds when \( \beta \) is non-degenerate.
3. Give an example with \( \dim U = 1 \) in which the inequality in (a) is strict.
:::

*Hint: consider the map \( V \to U^{*} \) that sends \( \v \) to the restriction of \( \beta(\cdot, \v) \) to \( U \).*
:::

::: {.solution}
(a) Let \( \rho \colon V^{*} \to U^{*} \) be the restriction map and \( S = \rho R_\beta \colon V \to U^{*} \), so \( S(\v) = \beta(\cdot, \v)\big|_U \). Both factors are linear, so \( S \) is linear, and \( U^{\perp_\beta} = \ker S \) by the definition of \( S \); hence \( U^{\perp_\beta} \) is a subspace. By Rank–Nullity (@thm-rank-nullity),
\[
\dim U^{\perp_\beta} = n - \rank S \ge n - \dim U^{*} = n - \dim U ,
\]
using \( \im S \subseteq U^{*} \) and \( \dim U^{*} = \dim U \) (@cor-dimension-dual-space).

(b) If \( \beta \) is non-degenerate then \( R_\beta \) is an isomorphism (@prp-nondegenerate-iff-invertible (c)), and \( \rho \) is surjective (@thm-dual-of-subspace). So \( S = \rho R_\beta \) is surjective, \( \rank S = \dim U \), and the inequality in (a) is an equality.

(c) Take \( \beta(\x, \y) = x_1y_1 \) on \( F^2 \) and \( U = \Span(\e_2) \). Then \( \beta(\e_2, \v) = 0 \) for every \( \v \), so \( U^{\perp_\beta} = F^2 \) has dimension \( 2 \), while \( n - \dim U = 1 \). The form is degenerate, as (b) requires it to be.
:::

::: {#exr-bilinear-forms-c3}
[C3: The evaluation pairing]

Let \( V \) be finite-dimensional and let \( W = V^{*} \times V \). Define \( \beta \) on \( W \) by
\[
\beta\bigl((\varphi, \v), (\psi, \w)\bigr) \coloneqq \psi(\v) + \varphi(\w).
\]

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \beta \) is a bilinear form on \( W \).
2. Prove that \( \beta \) is non-degenerate. *Hint: the two summands of an element of the radical can be killed separately.*
3. Deduce that if \( \v \in V \) satisfies \( \varphi(\v) = 0 \) for every \( \varphi \in V^{*} \), then \( \v = \0 \), and name the result of Chapter 4 this recovers.
:::
:::

::: {.solution}
(a) Fix \( (\psi, \w) \). The map \( (\varphi, \v) \mapsto \psi(\v) + \varphi(\w) \) is the sum of \( (\varphi,\v) \mapsto \psi(\v) \), which is linear because \( \psi \) is and because projection onto the second summand is linear, and \( (\varphi, \v) \mapsto \varphi(\w) = \ev_{\w}(\varphi) \), which is linear because \( \ev_{\w} \in V^{**} \) (@thm-evaluation-map-linear-injective). So clause (B1) holds. Clause (B2) follows by the same argument with the roles of the two arguments exchanged, since the defining expression is symmetric in them.

(b) Suppose \( (\psi, \w) \in \operatorname{rad}(\beta) \), so \( \psi(\v) + \varphi(\w) = 0 \) for all \( \varphi \in V^{*} \) and all \( \v \in V \). Taking \( \varphi = 0 \) gives \( \psi(\v) = 0 \) for every \( \v \), so \( \psi = 0 \). Taking \( \v = \0 \) then gives \( \varphi(\w) = 0 \) for every \( \varphi \in V^{*} \), so \( \ev_{\w} = 0 \) in \( V^{**} \), and \( \w = \0 \) because \( \ev_V \) is injective (@thm-evaluation-map-linear-injective). Hence the radical is \( \{\0\} \).

(c) The second half of (b) is exactly that statement: \( \varphi(\v) = 0 \) for all \( \varphi \in V^{*} \) forces \( \v = \0 \). It recovers the injectivity of the evaluation map \( \ev_V \colon V \to V^{**} \) of @thm-evaluation-map-linear-injective, which is the first half of @thm-double-dual-isomorphism. So the non-degeneracy of this form is the statement that functionals separate points (@thm-functionals-separate-points).
:::
