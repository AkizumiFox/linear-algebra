# Change of Basis and Similarity

The matrix \( \mtx{T}{\sB}{\sC} \) of a linear map depends on two choices of basis, and different choices can give very different matrices for the same map. This section answers two questions left open by that fact. How are two matrices of the same map related? And which properties of a matrix belong to the map itself, so that no choice of basis can change them? The answers are the change-of-basis formula, drawn as a commutative square, and the relation of similarity.

## Change-of-coordinates matrices

Recall the definition of the matrix of a map (@def-matrix-of-linear-map). If \( \sB = (\v_1, \dots, \v_n) \) is a basis of \( V \) and \( \sC \) is a basis of \( W \), then \( \mtx{T}{\sB}{\sC} \) is the matrix whose \( j \)-th column is \( \coord{T\v_j}{\sC} \), and it turns coordinates into coordinates: \( \coord{T\v}{\sC} = \mtx{T}{\sB}{\sC}\coord{\v}{\sB} \) (@thm-matrix-of-map-coordinates).

Recall the reflection from the previous section (@exm-matrix-of-reflection), which motivates this one. Let \( R \colon \nR^2 \to \nR^2 \) be the reflection across the line \( y = x \), so \( R(x, y) = (y, x) \). In the standard basis \( \sE = (\e_1, \e_2) \), we have \( R\e_1 = \e_2 \) and \( R\e_2 = \e_1 \), so
\[
\mtx{R}{\sE}{\sE} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}.
\]
Now use the basis \( \sB = ((1, 1), (1, -1)) \), one vector on the mirror line and one perpendicular to it. Then \( R(1, 1) = (1, 1) \) and \( R(1, -1) = (-1, 1) = -(1, -1) \), so
\[
\mtx{R}{\sB}{\sB} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.
\]
The second matrix shows at a glance what \( R \) does: it keeps one direction and flips the other. The two matrices describe the same map, so there must be a rule converting one into the other. The first step is to convert the **coordinates** of a single vector.

Take \( \v = (3, 1) \). Its standard coordinates are \( \coord{\v}{\sE} = (3, 1) \). In the basis \( \sB \), we solve \( a(1, 1) + b(1, -1) = (3, 1) \), which gives \( a = 2 \), \( b = 1 \), so \( \coord{\v}{\sB} = (2, 1) \). The same vector has two different coordinate columns, and we want a matrix that translates between them. Since the identity map \( \id_V \) sends every vector to itself, the matrix of \( \id_V \), with one basis on the input side and the other on the output side, should do exactly this job.

*A change-of-coordinates matrix is the matrix of "do nothing", read with one basis on the way in and another on the way out.*

::: {#def-change-of-coordinates-matrix}
[Change-of-coordinates matrix]

Let \( V \) be a finite-dimensional vector space over \( F \), and let \( \sB = (\v_1, \dots, \v_n) \) and \( \sC \) be **ordered** bases of \( V \). The **change-of-coordinates matrix from \( \sB \) to \( \sC \)** is the \( n \times n \) matrix
\[
\mtx{\id}{\sB}{\sC} \coloneqq \mtx{\id_V}{\sB}{\sC},
\]
the matrix of the identity map \( \id_V \colon V \to V \) with respect to the input basis \( \sB \) and the output basis \( \sC \). Its \( j \)-th column is \( \coord{\v_j}{\sC} \).
:::

In words: to build \( \mtx{\id}{\sB}{\sC} \), take the vectors of the **old** basis \( \sB \) one at a time, write each in the **new** basis \( \sC \), and put the coordinate columns side by side. The column description is @def-matrix-of-linear-map with \( T = \id_V \), since \( \id_V(\v_j) = \v_j \). Both bases must be bases of the **same** space \( V \), and both are ordered: reordering either one permutes the columns or the rows.

**Examples.**

- **Into the standard basis of \( F^n \).** If \( \sB = (\b_1, \dots, \b_n) \) is a basis of \( F^n \) and \( \sE \) is the standard basis, then \( \coord{\b_j}{\sE} = \b_j \). So \( \mtx{\id}{\sB}{\sE} \) is the matrix whose columns are the vectors of \( \sB \) themselves. For \( \sB = ((1, 1), (1, -1)) \) in \( \nR^2 \), \( \mtx{\id}{\sB}{\sE} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \), and indeed \( \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 1 \end{pmatrix} \) turns \( \coord{\v}{\sB} \) into \( \coord{\v}{\sE} \) for \( \v = (3, 1) \).
- **Out of the standard basis.** In the other direction, \( \mtx{\id}{\sE}{\sB} \) has columns \( \coord{\e_1}{\sB} \) and \( \coord{\e_2}{\sB} \). Solving \( a(1, 1) + b(1, -1) = (1, 0) \) gives \( a = b = \frac12 \), and solving for \( (0, 1) \) gives \( a = \frac12 \), \( b = -\frac12 \). So \( \mtx{\id}{\sE}{\sB} = \frac12 \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \). This is the inverse of the previous matrix, which the next theorem explains.
- **Polynomials.** In \( F[x]_{\le 2} \), let \( \sB = (1, x, x^2) \) and \( \sC = (1, x - 1, (x - 1)^2) \). Expanding \( (x - 1)^2 = 1 - 2x + x^2 \), the vectors of \( \sC \) have \( \sB \)-coordinates \( (1, 0, 0) \), \( (-1, 1, 0) \) and \( (1, -2, 1) \), so
  \[
  \mtx{\id}{\sC}{\sB} = \begin{pmatrix} 1 & -1 & 1 \\ 0 & 1 & -2 \\ 0 & 0 & 1 \end{pmatrix}.
  \]
- **Degenerate case.** If \( \sC = \sB \), then \( \coord{\v_j}{\sB} = \e_j \), so \( \mtx{\id}{\sB}{\sB} = \I_n \). Changing nothing is recorded by the identity matrix, as it should be.

**Non-example by minimal change.** Replace the basis \( ((1, 1), (1, -1)) \) by the list \( \sL = ((1, 1), (2, 2)) \). We can still write the matrix with these vectors as columns, but \( \sL \) is not a basis, so "coordinates with respect to \( \sL \)" are not defined: \( (2, 2) = 2(1, 1) + 0(2, 2) = 0(1, 1) + 1(2, 2) \) has two coordinate columns, and \( (1, 0) \) has none. The clause that fails is "\( \sB \) is a basis", which @def-coordinates needs for coordinates to exist and be unique.

::: {.warning}
**Watch the direction.** The columns of \( \mtx{\id}{\sB}{\sC} \) are the **\( \sB \)-vectors written in \( \sC \)**, and the matrix turns \( \sB \)-coordinates into \( \sC \)-coordinates. Using it the other way gives nonsense. With \( \sB = ((1, 1), (1, -1)) \), the matrix \( \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = \mtx{\id}{\sB}{\sE} \) applied to \( \coord{\v}{\sE} = (3, 1) \) gives \( (4, 2) \), which is **not** \( \coord{\v}{\sB} = (2, 1) \). A reliable test: the first column must be the first **input** basis vector written in the **output** basis. Here \( (1, 1) = 1 \cdot \e_1 + 1 \cdot \e_2 \), so the column \( (1, 1) \) belongs to \( \mtx{\id}{\sB}{\sE} \), which accepts \( \sB \)-coordinates.
:::

The examples suggest three facts: the matrix converts coordinates, converting twice multiplies the matrices, and converting back inverts the matrix. All three follow from results about matrices of maps, applied to the identity.

::: {#thm-change-of-coordinates}
[Change of Coordinates]

Let \( V \) be a vector space of dimension \( n \), and let \( \sB \), \( \sC \), \( \sD \) be bases of \( V \).

::: {.enumerate options="label=(\alph*)"}
1. For every \( \v \in V \), \( \coord{\v}{\sC} = \mtx{\id}{\sB}{\sC}\coord{\v}{\sB} \). Moreover, \( \mtx{\id}{\sB}{\sC} \) is the **only** matrix \( M \in M_n(F) \) with \( \coord{\v}{\sC} = M\coord{\v}{\sB} \) for every \( \v \in V \).
2. \( \mtx{\id}{\sB}{\sD} = \mtx{\id}{\sC}{\sD}\mtx{\id}{\sB}{\sC} \).
3. \( \mtx{\id}{\sB}{\sC} \) is invertible, and \( \big(\mtx{\id}{\sB}{\sC}\big)^{-1} = \mtx{\id}{\sC}{\sB} \).
:::
:::

::: {.proof}
(a) Apply @thm-matrix-of-map-coordinates, including its uniqueness clause, to \( \id_V \) with input basis \( \sB \) and output basis \( \sC \): since \( \id_V(\v) = \v \), it says \( \coord{\v}{\sC} = \mtx{\id}{\sB}{\sC}\coord{\v}{\sB} \) for every \( \v \), and that no other matrix has this property.

(b) Since \( \id_V = \id_V \circ \id_V \), @thm-matrix-of-composition, with \( \sB \) on the input, \( \sC \) in the middle and \( \sD \) on the output, gives \( \mtx{\id}{\sB}{\sD} = \mtx{\id}{\sC}{\sD}\mtx{\id}{\sB}{\sC} \).

(c) Taking \( \sD = \sB \) in (b) gives \( \mtx{\id}{\sC}{\sB}\mtx{\id}{\sB}{\sC} = \mtx{\id}{\sB}{\sB} = \I_n \), where the last equality holds because, writing \( \sB = (\v_1, \dots, \v_n) \), the \( j \)-th column of \( \mtx{\id}{\sB}{\sB} \) is \( \coord{\v_j}{\sB} = \e_j \). Swapping the roles of \( \sB \) and \( \sC \) gives \( \mtx{\id}{\sB}{\sC}\mtx{\id}{\sC}{\sB} = \I_n \). By @def-invertible-matrix, \( \mtx{\id}{\sB}{\sC} \) is invertible with inverse \( \mtx{\id}{\sC}{\sB} \).
:::

So every change-of-coordinates matrix is invertible. The converse is also true, and it will matter when we compare matrices: every invertible matrix is a change-of-coordinates matrix, for a suitable new basis.

::: {#prp-invertible-matrix-change-of-basis}
[Invertible matrices are changes of basis]

Let \( \sB = (\v_1, \dots, \v_n) \) be a basis of \( V \), and let \( \P = (p_{ij}) \in M_n(F) \) be invertible. Put
\[
\v_j' \coloneqq p_{1j}\v_1 + p_{2j}\v_2 + \dots + p_{nj}\v_n \qquad (j = 1, \dots, n).
\]
Then \( \sB' = (\v_1', \dots, \v_n') \) is a basis of \( V \), and \( \mtx{\id}{\sB'}{\sB} = \P \).
:::

::: {.proof}
By @def-coordinates, \( \coord{\v_j'}{\sB} \) is the \( j \)-th column \( \p_j \) of \( \P \). Let \( c_1, \dots, c_n \in F \) satisfy \( c_1\v_1' + \dots + c_n\v_n' = \0 \). Taking \( \sB \)-coordinates and using @thm-coordinates-linear,
\[
c_1\p_1 + \dots + c_n\p_n = \coord{\0}{\sB} = \0,
\]
that is, \( \P\c = \0 \) with \( \c = (c_1, \dots, c_n) \), by @thm-matrix-times-vector-columns. Since \( \P \) is invertible, @thm-invertible-tfae ((a) \( \Rightarrow \) (b)) gives \( \c = \0 \). So \( \sB' \) is linearly independent. It has length \( n = \dim V \), hence it is a basis by @thm-right-size-basis (a). Finally, the \( j \)-th column of \( \mtx{\id}{\sB'}{\sB} \) is \( \coord{\v_j'}{\sB} = \p_j \), so \( \mtx{\id}{\sB'}{\sB} = \P \).
:::

::: {#exm-change-of-coordinates-polynomials}
[Coordinates around the point \( 1 \)]

In \( \nR[x]_{\le 2} \), let \( \sB = (1, x, x^2) \) and \( \sC = (1, x - 1, (x - 1)^2) \). Find \( \mtx{\id}{\sB}{\sC} \), and use it to write \( p = 2 + 3x + x^2 \) in powers of \( x - 1 \).
:::

::: {.solution}
From the examples above, \( \mtx{\id}{\sC}{\sB} = \begin{pmatrix} 1 & -1 & 1 \\ 0 & 1 & -2 \\ 0 & 0 & 1 \end{pmatrix} \). By @thm-change-of-coordinates (c), \( \mtx{\id}{\sB}{\sC} \) is its inverse. We can also read it off directly: \( 1 = 1 \), \( x = 1 + (x - 1) \), and \( x^2 = (1 + (x - 1))^2 = 1 + 2(x - 1) + (x - 1)^2 \). So
\[
\mtx{\id}{\sB}{\sC} = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix},
\]
and multiplying the two matrices gives \( \I_3 \), as the theorem predicts. By @thm-change-of-coordinates (a),
\[
\coord{p}{\sC} = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 2 \\ 3 \\ 1 \end{pmatrix} = \begin{pmatrix} 6 \\ 5 \\ 1 \end{pmatrix}.
\]
Hence \( 2 + 3x + x^2 = 6 + 5(x - 1) + (x - 1)^2 \). Check at \( x = 1 \): both sides equal \( 6 \). The \( \sC \)-coordinates are \( p(1) \), \( p'(1) \) and \( p''(1)/2 \), the Taylor coefficients at \( 1 \).
:::

## Change of basis for linear maps

Now return to a linear map \( T \colon V \to W \) between finite-dimensional spaces. Suppose we know its matrix \( \mtx{T}{\sB}{\sC} \) and want the matrix \( \mtx{T}{\sB'}{\sC'} \) for new bases \( \sB' \) of \( V \) and \( \sC' \) of \( W \). The trick is to write \( T \) in a slightly more elaborate way that does nothing:
\[
T = \id_W \circ T \circ \id_V .
\]
Each factor can now carry its own pair of bases, and the matrix of the composite is the product of the matrices. The picture keeps track of which basis sits where.

\begin{center}
\begin{tikzpicture}[
    sp/.style={inner sep=5pt, font=\normalsize},
    arr/.style={->, thick, shorten >=3pt, shorten <=3pt},
    lab/.style={font=\small, align=center}]
  \node[sp] (VB) at (0, 2.6) {$V$ with $\sB$};
  \node[sp] (WC) at (6.4, 2.6) {$W$ with $\sC$};
  \node[sp] (VB2) at (0, 0) {$V$ with $\sB'$};
  \node[sp] (WC2) at (6.4, 0) {$W$ with $\sC'$};
  \draw[arr] (VB) -- node[above, lab] {$T$\\[1pt] $\mtx{T}{\sB}{\sC}$} (WC);
  \draw[arr] (VB2) -- node[below, lab] {$T$\\[1pt] $\mtx{T}{\sB'}{\sC'}$ (wanted)} (WC2);
  \draw[arr] (VB2) -- node[left, lab] {$\id_V$\\[1pt] $\mtx{\id}{\sB'}{\sB}$} (VB);
  \draw[arr] (WC) -- node[right, lab] {$\id_W$\\[1pt] $\mtx{\id}{\sC}{\sC'}$} (WC2);
\end{tikzpicture}
\end{center}

Going along the bottom edge applies \( T \). Going up, across the top and down applies \( \id_W \circ T \circ \id_V \), which is the same map. So the two routes must have the same matrix. Reading the long route, the step done **first** (up the left side) is written on the **right**.

::: {#thm-change-of-basis-maps}
[Change of Basis for Linear Maps]

Let \( V \) and \( W \) be finite-dimensional vector spaces over \( F \), let \( \sB, \sB' \) be bases of \( V \) and \( \sC, \sC' \) bases of \( W \), and let \( T \colon V \to W \) be linear. Then
\[
\mtx{T}{\sB'}{\sC'} = \mtx{\id}{\sC}{\sC'}\,\mtx{T}{\sB}{\sC}\,\mtx{\id}{\sB'}{\sB}.
\]
In particular, for an operator \( T \in \cL(V) \) and bases \( \sB, \sB' \) of \( V \), with \( \P = \mtx{\id}{\sB'}{\sB} \),
\[
\mtx{T}{\sB'}{\sB'} = \P^{-1}\,\mtx{T}{\sB}{\sB}\,\P .
\]
:::

::: {.idea}
Nothing is computed: the formula is the change-of-basis square read along its long route. ① Write \( T = \id_W \circ T \circ \id_V \). ② Give the middle factor the bases whose matrix we know. ③ Apply the composition rule twice. Do not memorize the formula; redraw the square and read it off, right to left.
:::

::: {.proof}
Since \( T = \id_W \circ (T \circ \id_V) \), @thm-matrix-of-composition with bases \( \sB' \), \( \sC \), \( \sC' \) gives \( \mtx{T}{\sB'}{\sC'} = \mtx{\id}{\sC}{\sC'}\,\mtx{T \circ \id_V}{\sB'}{\sC} \). Applying @thm-matrix-of-composition again, with bases \( \sB' \), \( \sB \), \( \sC \), gives \( \mtx{T \circ \id_V}{\sB'}{\sC} = \mtx{T}{\sB}{\sC}\,\mtx{\id}{\sB'}{\sB} \). Combining the two equations proves the first formula.

For an operator, take \( W = V \), \( \sC = \sB \) and \( \sC' = \sB' \). The first formula becomes \( \mtx{T}{\sB'}{\sB'} = \mtx{\id}{\sB}{\sB'}\,\mtx{T}{\sB}{\sB}\,\P \), and \( \mtx{\id}{\sB}{\sB'} = \P^{-1} \) by @thm-change-of-coordinates (c). This proves the theorem.
:::

We will call this move **the change-of-basis square**: whenever a question involves the same map in two bases, draw the square, label the arrows with bases, and read the formula off the long route. It also explains the word "coordinates": a matrix is a map seen through a choice of coordinates, and the side arrows re-express those coordinates.

::: {#exm-reflection-diagonal-basis}
[The reflection in a mirror-adapted basis]

Let \( R(x, y) = (y, x) \) on \( \nR^2 \), and \( \sB = ((1, 1), (1, -1)) \). Compute \( \mtx{R}{\sB}{\sB} \) from \( \mtx{R}{\sE}{\sE} \) using @thm-change-of-basis-maps, and compare with the direct computation at the start of the section.
:::

::: {.solution}
Here \( \P = \mtx{\id}{\sB}{\sE} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \), with inverse \( \P^{-1} = \mtx{\id}{\sE}{\sB} = \frac12 \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \), found in the examples after @def-change-of-coordinates-matrix. Then
\[
\begin{aligned}
\P^{-1}\mtx{R}{\sE}{\sE}\P
&= \frac12 \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \\
&= \frac12 \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}
= \frac12 \begin{pmatrix} 2 & 0 \\ 0 & -2 \end{pmatrix}
= \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix},
\end{aligned}
\]
which agrees with the direct computation. The direct route was shorter here, because we chose \( \sB \) so that \( R \) acts simply on it. The formula earns its keep when the new matrix is not visible by inspection, or when we want to go back from the simple matrix to the standard one: \( \mtx{R}{\sE}{\sE} = \P\,\mtx{R}{\sB}{\sB}\,\P^{-1} \).
:::

The next example changes basis in a polynomial space, where "standard" does not mean "best".

::: {#exm-differentiation-rescaled-basis}
[Differentiation with a rescaled basis]

Let \( D \colon \nR[x]_{\le 2} \to \nR[x]_{\le 2} \) be differentiation, \( \sB = (1, x, x^2) \) and \( \sB' = (1, x, \tfrac12 x^2) \). Find \( \mtx{D}{\sB'}{\sB'} \).
:::

::: {.solution}
In \( \sB \), \( D(1) = 0 \), \( D(x) = 1 \) and \( D(x^2) = 2x \), so \( \A = \mtx{D}{\sB}{\sB} = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix} \). The vectors of \( \sB' \) have \( \sB \)-coordinates \( \e_1 \), \( \e_2 \), \( \frac12\e_3 \), so \( \P = \mtx{\id}{\sB'}{\sB} = \diag(1, 1, \tfrac12) \) and \( \P^{-1} = \diag(1, 1, 2) \). Multiplying a matrix on the left by a diagonal matrix scales its rows, and on the right scales its columns, so
\[
\P^{-1}\A\P = \begin{pmatrix} 0 & 1 \cdot 1 \cdot 1 & 0 \\ 0 & 0 & 1 \cdot 2 \cdot \tfrac12 \\ 0 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}.
\]
Directly: \( D(1) = 0 \), \( D(x) = 1 \), \( D(\tfrac12 x^2) = x \), so \( D \) shifts each vector of \( \sB' \) to the previous one, and the matrix has \( 1 \)'s just above the diagonal. The factor \( 2 \) has disappeared into the basis.
:::

::: {.check}
Let \( T \colon V \to W \), and suppose we change only the basis of \( W \), from \( \sC \) to \( \sC' \), keeping \( \sB \). Which of the two side matrices in @thm-change-of-basis-maps becomes the identity, and what is the formula?
:::

::: {.solution}
With \( \sB' = \sB \), the left side of the square is \( \mtx{\id}{\sB}{\sB} = \I_n \). The formula becomes \( \mtx{T}{\sB}{\sC'} = \mtx{\id}{\sC}{\sC'}\,\mtx{T}{\sB}{\sC} \): only a multiplication on the left. Changing the output basis acts on the rows; changing the input basis acts on the columns.
:::

## Similar matrices

For an operator, the two bases on the two sides of the square are the same, and the formula takes the special shape \( \P^{-1}\A\P \). Recall from @exm-similarity that we already gave this shape a name in Chapter 0 and checked that it defines an equivalence relation. We now record it as a definition, because it is exactly the relation "same operator, different basis".

*Two square matrices are similar when one is obtained from the other by a change of basis applied on both sides at once.*

::: {#def-similar-matrices}
[Similar matrices]

Let \( \A, \B \in M_n(F) \). We say \( \A \) is **similar** to \( \B \), written \( \A \sim \B \), if there **exists** an **invertible** matrix \( \P \in M_n(F) \) such that
\[
\B = \P^{-1}\A\P .
\]
:::

In words: the **same** \( \P \) appears on both sides, once inverted. By @exm-similarity, \( \sim \) is an equivalence relation, so we may say "\( \A \) and \( \B \) are similar" without worrying about the order. The matrix \( \P \) is not unique: for instance \( \A = \P^{-1}\A\P \) holds for every invertible \( \P \) that commutes with \( \A \), such as any non-zero multiple of \( \I_n \). Writing \( \B = \Q\A\Q^{-1} \) defines the same relation, with \( \Q = \P^{-1} \).

**Examples.**

- **The reflection.** \( \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \sim \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \), by @exm-reflection-diagonal-basis.
- **A triangular matrix.** \( \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix} \sim \diag(1, 3) \), as computed in @exm-similarity with \( \P = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \).
- **Reordering a basis.** \( \diag(1, 2) \sim \diag(2, 1) \): with \( \P = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \P^{-1} \), we get \( \P^{-1}\diag(1, 2)\P = \diag(2, 1) \). This is the operator with matrix \( \diag(1, 2) \) in \( (\v_1, \v_2) \), read in the reordered basis \( (\v_2, \v_1) \).
- **Degenerate case: scalar matrices.** For \( c \in F \), \( \P^{-1}(c\I_n)\P = c\P^{-1}\P = c\I_n \) for every invertible \( \P \). So \( c\I_n \) is similar only to itself. In particular \( \I_n \) and the zero matrix are alone in their classes: the identity operator looks like \( \I_n \) in **every** basis.

**Non-example by minimal change.** Allow two different invertible matrices, \( \B = \Q\A\P \). With \( \A = \I_2 \), \( \Q = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) and \( \P = \I_2 \), we get \( \B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \ne \I_2 \). So \( \B = \Q\A\P \) holds, but \( \B \) is not similar to \( \I_2 \), which is similar only to itself. The clause that failed is "the **same** \( \P \) on both sides, once inverted". The relaxed relation is also useful; it is the subject of the next section.

The definition was designed to capture one idea, and the next theorem says it captures exactly that idea.

::: {#thm-similar-iff-same-operator}
[Similar Matrices Represent the Same Operator]

Let \( \A, \B \in M_n(F) \).

::: {.enumerate options="label=(\alph*)"}
1. If \( V \) is a vector space of dimension \( n \), \( T \in \cL(V) \), and \( \sB, \sC \) are bases of \( V \), then \( \mtx{T}{\sB}{\sB} \sim \mtx{T}{\sC}{\sC} \).
2. Conversely, suppose \( \A \sim \B \). Let \( V \) be any vector space of dimension \( n \) with a basis \( \sB \), and let \( T \in \cL(V) \) be an operator with \( \mtx{T}{\sB}{\sB} = \A \). Then there is a basis \( \sC \) of \( V \) with \( \mtx{T}{\sC}{\sC} = \B \).
3. Such an operator \( T \) in (b) always exists. In particular, \( \A \sim \B \) if and only if \( \A \) and \( \B \) are the matrices of the operator \( \x \mapsto \A\x \) on \( F^n \) in the standard basis and in some basis of \( F^n \), respectively.
:::
:::

::: {.proof}
(a) By @thm-change-of-basis-maps, \( \mtx{T}{\sC}{\sC} = \P^{-1}\mtx{T}{\sB}{\sB}\P \) with \( \P = \mtx{\id}{\sC}{\sB} \), which is invertible by @thm-change-of-coordinates (c).

(b) Suppose \( \B = \P^{-1}\A\P \) with \( \P \) invertible. By @prp-invertible-matrix-change-of-basis, there is a basis \( \sC \) of \( V \) with \( \mtx{\id}{\sC}{\sB} = \P \). By @thm-change-of-basis-maps, \( \mtx{T}{\sC}{\sC} = \P^{-1}\mtx{T}{\sB}{\sB}\P = \P^{-1}\A\P = \B \).

(c) Write \( \sB = (\v_1, \dots, \v_n) \). By @thm-linear-transform-basis, there is a linear map \( T \colon V \to V \) with \( T\v_j = a_{1j}\v_1 + \dots + a_{nj}\v_n \) for each \( j \). The \( j \)-th column of \( \mtx{T}{\sB}{\sB} \) is \( \coord{T\v_j}{\sB} \), which is the \( j \)-th column of \( \A \); so \( \mtx{T}{\sB}{\sB} = \A \). For \( V = F^n \) with the standard basis \( \sE \), the operator \( \x \mapsto \A\x \) works, since \( \A\e_j \) is the \( j \)-th column of \( \A \) (@thm-matrix-times-vector-columns). The last statement now follows from (a) and (b).
:::

This is the promise of Chapter 0 kept: similar matrices describe the same operator in two coordinate systems. So a question of the form "are \( \A \) and \( \B \) similar?" is really the question "is there a basis in which the operator \( \x \mapsto \A\x \) has matrix \( \B \)?". Deciding it is one of the central problems of the book, and it will take until Chapter 10 to answer it in general.

## Similarity invariants

If a quantity computed from a matrix does not change under \( \A \mapsto \P^{-1}\A\P \), then it is really a property of the operator, and we call it a **similarity invariant**. Invariants are the cheap way to prove that two matrices are **not** similar: find one invariant on which they differ. The trace is the first example, and it is the reason the trace will make sense for operators in this chapter's last section.

::: {#thm-trace-similarity-invariant}
[Trace Is a Similarity Invariant]

If \( \A, \B \in M_n(F) \) are similar, then \( \tr \A = \tr \B \).
:::

::: {.proof}
Let \( \B = \P^{-1}\A\P \) with \( \P \) invertible. By @thm-trace-properties (3), applied to the matrices \( \P^{-1} \) and \( \A\P \),
\[
\tr \B = \tr\big(\P^{-1}(\A\P)\big) = \tr\big((\A\P)\P^{-1}\big) = \tr\big(\A(\P\P^{-1})\big) = \tr \A,
\]
where the third equality is associativity of matrix multiplication. This proves the theorem.
:::

The proof never used that \( \B \) is "similar" in any geometric sense, only that the trace ignores the order of two factors. Several other quantities survive a change of basis, for simpler reasons.

::: {#prp-similarity-invariants}
[More similarity invariants]

Let \( \A, \B \in M_n(F) \) with \( \B = \P^{-1}\A\P \) for an invertible \( \P \).

::: {.enumerate options="label=(\alph*)"}
1. \( \rank \A = \rank \B \).
2. \( \A \) is invertible if and only if \( \B \) is invertible.
3. For every polynomial \( p \in F[x] \), \( p(\B) = \P^{-1}p(\A)\P \). In particular, \( p(\A) = 0 \) if and only if \( p(\B) = 0 \); for example, \( \A^2 = 0 \) if and only if \( \B^2 = 0 \).
:::
:::

::: {.proof}
(a) By @thm-rank-product-inequality, multiplying by invertible matrices on either side does not change the rank, so \( \rank(\P^{-1}\A\P) = \rank(\A\P) = \rank \A \).

(b) If \( \A \) is invertible, then \( \B = \P^{-1}\A\P \) is a product of invertible matrices, hence invertible by @thm-inverse-matrix-properties (part 3). Since \( \A = \P\B\P^{-1} = (\P^{-1})^{-1}\B \P^{-1} \), the same argument with the roles swapped gives the converse.

(c) First, \( \B^k = \P^{-1}\A^k\P \) for every \( k \ge 0 \), by induction on \( k \): for \( k = 0 \) both sides are \( \I_n \), and if it holds for \( k \), then \( \B^{k+1} = \B^k\B = (\P^{-1}\A^k\P)(\P^{-1}\A\P) = \P^{-1}\A^k(\P\P^{-1})\A\P = \P^{-1}\A^{k+1}\P \). Now let \( p = c_0 + c_1x + \dots + c_dx^d \). By @def-polynomial-of-matrix and the distributive and scalar laws of @thm-matrix-multiplication-properties,
\[
p(\B) = \sum_{k=0}^{d} c_k\B^k = \sum_{k=0}^{d} c_k\P^{-1}\A^k\P = \P^{-1}\Big(\sum_{k=0}^{d} c_k\A^k\Big)\P = \P^{-1}p(\A)\P .
\]
If \( p(\A) = 0 \), then \( p(\B) = \P^{-1}0\P = 0 \). Conversely, \( \A = \P\B\P^{-1} \) is of the same form with \( \P^{-1} \) in place of \( \P \), so \( p(\B) = 0 \) implies \( p(\A) = 0 \).
:::

For example, \( \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix} \) and \( \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix} \) are **not** similar, because their traces are \( 4 \) and \( 3 \). And \( \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) is not similar to the zero matrix, because their ranks are \( 1 \) and \( 0 \) (or because the zero matrix is similar only to itself).

It is tempting to turn this around and decide similarity by comparing a list of invariants. That fails.

::: {.warning}
**Shared invariants do not imply similarity.** Let \( \J = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \). Then \( \I_2 \) and \( \J \) have the same trace \( 2 \), the same rank \( 2 \), both are invertible, and both satisfy \( (\X - \I_2)^2 = 0 \). But they are **not** similar: for every invertible \( \P \), \( \P^{-1}\I_2\P = \I_2 \ne \J \). A sharper invariant does separate them: combining (a) and (c) of @prp-similarity-invariants, similar matrices \( \A \) and \( \B \) have \( \rank p(\A) = \rank p(\B) \) for every polynomial \( p \), and \( \rank(\I_2 - \I_2) = 0 \) while \( \rank(\J - \I_2) = 1 \). Which invariants suffice in general is the question Chapter 10 answers.
:::

::: {.check}
Are \( \diag(2, 5) \) and \( \diag(5, 2) \) similar? Are \( \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} \) and \( \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} \) similar?
:::

::: {.solution}
The first pair is similar: with \( \P = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \), which is its own inverse, \( \P^{-1}\diag(2, 5)\P = \diag(5, 2) \). The second pair is not: \( 2\I_2 \) is a scalar matrix, so it is similar only to itself, although both matrices have trace \( 4 \) and rank \( 2 \).
:::

## A basis adapted to the operator

The reflection became diagonal once we chose one basis vector the map keeps and one it flips. The same idea works whenever a map is simple on two complementary pieces of the space. For a map of rank \( 1 \) on \( \nR^2 \), the natural pieces are the image and the kernel, provided they are two different lines. (They need not be: for \( \x \mapsto \N\x \) with \( \N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \), both are \( \Span(\e_1) \), and @exr-change-of-basis-c3 shows what to do instead.)

::: {#exm-projection-adapted-basis}
[Making a matrix diagonal with a well-chosen basis]

Let \( T \colon \nR^2 \to \nR^2 \), \( T(x, y) = (2x - y,\ 2x - y) \). Find a basis \( \sB \) of \( \nR^2 \) such that \( \mtx{T}{\sB}{\sB} \) is diagonal, and check the answer with @thm-change-of-basis-maps.
:::

::: {.solution}
In the standard basis \( \A = \mtx{T}{\sE}{\sE} = \begin{pmatrix} 2 & -1 \\ 2 & -1 \end{pmatrix} \).

Both entries of \( T(x, y) \) are equal, so \( \im T \subseteq \Span((1, 1)) \), and \( T(1, 1) = (1, 1) \) shows \( \im T = \Span((1, 1)) \). The kernel is \( \{ (x, y) : y = 2x \} = \Span((1, 2)) \). So \( T \) fixes \( (1, 1) \) and kills \( (1, 2) \). These two vectors are not multiples of each other, so \( \sB = ((1, 1), (1, 2)) \) is independent, and it is a basis of \( \nR^2 \) by @thm-right-size-basis. Since \( T(1, 1) = 1 \cdot (1, 1) + 0 \cdot (1, 2) \) and \( T(1, 2) = \0 \),
\[
\mtx{T}{\sB}{\sB} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}.
\]
Check: \( \P = \mtx{\id}{\sB}{\sE} = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} \) has \( ad - bc = 1 \), so \( \P^{-1} = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix} \) by @thm-two-by-two-inverse. Then
\[
\P^{-1}\A\P = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix} \begin{pmatrix} 2 & -1 \\ 2 & -1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} = \begin{pmatrix} 2 & -1 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}.
\]
As @thm-trace-similarity-invariant and @prp-similarity-invariants require, \( \tr \A = 1 \) and \( \rank \A = 1 \) match the diagonal matrix. Its form also explains a property of \( \A \) that is not obvious from its entries: \( \diag(1, 0)^2 = \diag(1, 0) \), so \( \A^2 = \A \) by @prp-similarity-invariants (c) applied to \( p = x^2 - x \).
:::

The basis in this example consisted of vectors that \( T \) sends to multiples of themselves. Chapter 9 turns this into a method: such vectors are called eigenvectors, and an operator has a diagonal matrix exactly when there is a basis of them. Operators with \( T^2 = T \), like this one, are the projections of the last section of this chapter.

## Exercises

### A. Check your understanding

::: {#exr-change-of-basis-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the change-of-coordinates matrix \( \mtx{\id}{\sB}{\sC} \), and say what its columns are.
2. State the change-of-basis formula for an operator \( T \in \cL(V) \) and bases \( \sB, \sB' \), saying exactly which matrix \( \P \) is.
3. True or false: \( \mtx{\id}{\sB}{\sC} = \mtx{\id}{\sC}{\sB} \) for all bases \( \sB, \sC \) of \( V \). Justify your answer.
4. True or false: if \( \A \sim \B \), then \( \tr \A = \tr \B \) and \( \rank \A = \rank \B \). Justify your answer.
5. True or false: if \( \tr \A = \tr \B \) and \( \rank \A = \rank \B \), then \( \A \sim \B \). Justify your answer.
6. Describe the method for recovering the change-of-basis formula without memorizing it.
:::
:::

::: {.solution}
(a) For bases \( \sB = (\v_1, \dots, \v_n) \) and \( \sC \) of \( V \), \( \mtx{\id}{\sB}{\sC} \) is the matrix of \( \id_V \) with input basis \( \sB \) and output basis \( \sC \) (@def-change-of-coordinates-matrix). Its \( j \)-th column is \( \coord{\v_j}{\sC} \).

(b) \( \mtx{T}{\sB'}{\sB'} = \P^{-1}\mtx{T}{\sB}{\sB}\P \) with \( \P = \mtx{\id}{\sB'}{\sB} \), whose columns are the \( \sB \)-coordinates of the vectors of \( \sB' \) (@thm-change-of-basis-maps).

(c) False. By @thm-change-of-coordinates (c) the two matrices are inverse to each other, and an invertible matrix usually differs from its inverse: for \( \sB = ((1, 1), (1, -1)) \) and the standard basis \( \sE \) of \( \nR^2 \), \( \mtx{\id}{\sB}{\sE} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \) but \( \mtx{\id}{\sE}{\sB} = \frac12\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \).

(d) True, by @thm-trace-similarity-invariant and @prp-similarity-invariants (a).

(e) False. \( \I_2 \) and \( \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) both have trace \( 2 \) and rank \( 2 \), but \( \I_2 \) is similar only to itself.

(f) Draw the change-of-basis square: \( T \) along the top and bottom with the old and new bases, identity maps up the left side and down the right side. Since \( T = \id_W \circ T \circ \id_V \), the matrix of the bottom arrow is the product of the matrices along the long route, with the first step on the right.
:::

### B. Practice

::: {#exr-change-of-basis-b1}
[B1: Change-of-coordinates matrices]

::: {.enumerate options="label=(\alph*)"}
1. In \( \nR^2 \), let \( \sB = ((1, 2), (3, 5)) \) and \( \sC = ((1, 1), (1, 2)) \). Find \( \mtx{\id}{\sB}{\sC} \). If \( \coord{\v}{\sB} = (1, -1) \), find \( \coord{\v}{\sC} \), and check your answer by computing \( \v \) both ways.
2. In \( \nR[x]_{\le 2} \), let \( \sB = (1, x, x^2) \) and \( \sC = (1, 1 + x, 1 + x + x^2) \). Find \( \mtx{\id}{\sC}{\sB} \) and \( \mtx{\id}{\sB}{\sC} \). Hence find the \( \sC \)-coordinates of \( 3 - x + 2x^2 \).
:::
:::

::: {.solution}
(a) The columns are the \( \sC \)-coordinates of \( (1, 2) \) and \( (3, 5) \). Solving \( a(1, 1) + b(1, 2) = (1, 2) \) gives \( a + b = 1 \), \( a + 2b = 2 \), so \( b = 1 \), \( a = 0 \). Solving \( a(1, 1) + b(1, 2) = (3, 5) \) gives \( b = 2 \), \( a = 1 \). Hence
\[
\mtx{\id}{\sB}{\sC} = \begin{pmatrix} 0 & 1 \\ 1 & 2 \end{pmatrix}, \qquad \coord{\v}{\sC} = \begin{pmatrix} 0 & 1 \\ 1 & 2 \end{pmatrix}\begin{pmatrix} 1 \\ -1 \end{pmatrix} = \begin{pmatrix} -1 \\ -1 \end{pmatrix}
\]
by @thm-change-of-coordinates (a). Check: from \( \sB \), \( \v = (1, 2) - (3, 5) = (-2, -3) \); from \( \sC \), \( \v = -(1, 1) - (1, 2) = (-2, -3) \).

(b) The vectors of \( \sC \) have \( \sB \)-coordinates \( (1, 0, 0) \), \( (1, 1, 0) \), \( (1, 1, 1) \), so \( \mtx{\id}{\sC}{\sB} = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix} \). For the other direction, write the vectors of \( \sB \) in \( \sC \): \( 1 = 1 \), \( x = (1 + x) - 1 \), \( x^2 = (1 + x + x^2) - (1 + x) \). So
\[
\mtx{\id}{\sB}{\sC} = \begin{pmatrix} 1 & -1 & 0 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{pmatrix},
\]
and multiplying the two matrices gives \( \I_3 \), as @thm-change-of-coordinates (c) requires. Hence
\[
\coord{3 - x + 2x^2}{\sC} = \begin{pmatrix} 1 & -1 & 0 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{pmatrix}\begin{pmatrix} 3 \\ -1 \\ 2 \end{pmatrix} = \begin{pmatrix} 4 \\ -3 \\ 2 \end{pmatrix}.
\]
Check: \( 4 - 3(1 + x) + 2(1 + x + x^2) = 3 - x + 2x^2 \).
:::

::: {#exr-change-of-basis-b2}
[B2: A matrix in a new basis, two ways]

Let \( T \colon \nR^2 \to \nR^2 \), \( T(x, y) = (4x - 2y,\ x + y) \), and \( \sB = ((1, 1), (2, 1)) \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \mtx{T}{\sB}{\sB} \) directly from @def-matrix-of-linear-map.
2. Compute it again with @thm-change-of-basis-maps, starting from the standard matrix.
:::
:::

::: {.solution}
(a) \( T(1, 1) = (2, 2) = 2(1, 1) + 0(2, 1) \) and \( T(2, 1) = (6, 3) = 0(1, 1) + 3(2, 1) \). Hence \( \mtx{T}{\sB}{\sB} = \diag(2, 3) \).

(b) \( \A = \mtx{T}{\sE}{\sE} = \begin{pmatrix} 4 & -2 \\ 1 & 1 \end{pmatrix} \) and \( \P = \mtx{\id}{\sB}{\sE} = \begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix} \). Here \( ad - bc = -1 \), so by @thm-two-by-two-inverse \( \P^{-1} = \begin{pmatrix} -1 & 2 \\ 1 & -1 \end{pmatrix} \). Then
\[
\P^{-1}\A\P = \begin{pmatrix} -1 & 2 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} 4 & -2 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} -2 & 4 \\ 3 & -3 \end{pmatrix}\begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix},
\]
in agreement with (a).
:::

::: {#exr-change-of-basis-b3}
[B3: Similar or not?]

Determine which of the following pairs of real matrices are similar. Justify your answer, either with an invariant or with an explicit invertible \( \P \).

::: {.enumerate options="label=(\alph*)"}
1. \( \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix} \) and \( \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix} \).
2. \( \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) and \( \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} \).
3. \( \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix} \) and \( \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix} \).
4. \( \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} \) and \( \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} \).
5. \( \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \) and \( \begin{pmatrix} 2 & 0 \\ 0 & 0 \end{pmatrix} \).
:::
:::

::: {.solution}
(a) Not similar: the traces are \( 4 \) and \( 3 \), contradicting @thm-trace-similarity-invariant.

(b) Not similar: the ranks are \( 1 \) and \( 0 \), contradicting @prp-similarity-invariants (a).

(c) Similar. Let \( \A \) be the first matrix. We look for a basis in which \( \x \mapsto \A\x \) is diagonal: \( \A\e_1 = \e_1 \), and \( \A(1, 1) = (2, 2) = 2(1, 1) \). With \( \P = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \), \( \P^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} \) and
\[
\P^{-1}\A\P = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 0 & 2 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}.
\]

(d) Not similar: \( 2\I_2 \) is a scalar matrix, so \( \P^{-1}(2\I_2)\P = 2\I_2 \) for every invertible \( \P \), and the second matrix is not \( 2\I_2 \). The traces and ranks agree, so invariants alone would not have decided this.

(e) Similar. Let \( \A \) be the first matrix. \( \A(1, 1) = (2, 2) \) and \( \A(1, -1) = (0, 0) \). With \( \P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \) and \( \P^{-1} = \frac12\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \),
\[
\P^{-1}\A\P = \frac12\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} 2 & 0 \\ 2 & 0 \end{pmatrix} = \frac12\begin{pmatrix} 4 & 0 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 0 & 0 \end{pmatrix},
\]
where \( \A\P = \begin{pmatrix} 2 & 0 \\ 2 & 0 \end{pmatrix} \) has columns \( \A(1, 1) \) and \( \A(1, -1) \).
:::

### C. Going deeper

::: {#exr-change-of-basis-c1}
[C1: Matrices similar only to themselves]

Let \( n \ge 1 \) and \( \A \in M_n(F) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \A \) is similar only to itself if and only if \( \A = c\I_n \) for some \( c \in F \).
2. Show that \( \N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) and \( \N\tp = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \) are similar, and explain the answer in terms of the operator \( \x \mapsto \N\x \) and a reordered basis.
:::

*Hint: for (a), use the invertible matrices \( \I_n + \E_{ij} \) with \( i \ne j \).*
:::

::: {.solution}
(a) \( (\Leftarrow) \) If \( \A = c\I_n \), then \( \P^{-1}\A\P = c\P^{-1}\P = c\I_n = \A \) for every invertible \( \P \), so the only matrix similar to \( \A \) is \( \A \).

\( (\Rightarrow) \) Suppose \( \P^{-1}\A\P = \A \) for every invertible \( \P \), that is, \( \A\P = \P\A \). If \( n = 1 \), \( \A = (a_{11}) = a_{11}\I_1 \). Let \( n \ge 2 \), and fix \( i \ne j \). The matrix \( \I_n + \E_{ij} \) is invertible, with inverse \( \I_n - \E_{ij} \), since \( \E_{ij}\E_{ij} = 0 \) for \( i \ne j \). So \( \A(\I_n + \E_{ij}) = (\I_n + \E_{ij})\A \), which gives \( \A\E_{ij} = \E_{ij}\A \). Compare the entries in position \( (k, l) \): by @def-matrix-multiplication,
\[
(\A\E_{ij})_{kl} = \begin{cases} a_{ki} & l = j \\ 0 & l \ne j \end{cases}, \qquad (\E_{ij}\A)_{kl} = \begin{cases} a_{jl} & k = i \\ 0 & k \ne i. \end{cases}
\]
Taking \( l = j \) and \( k \ne i \) gives \( a_{ki} = 0 \). Taking \( k = i \) and \( l = j \) gives \( a_{ii} = a_{jj} \). Since \( i \ne j \) were arbitrary (and every index \( i \) has some \( j \ne i \) because \( n \ge 2 \)), all off-diagonal entries of \( \A \) vanish and all diagonal entries are equal to \( c = a_{11} \). Hence \( \A = c\I_n \).

(b) Let \( \P = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \), so \( \P^{-1} = \P \). Then \( \N\P = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \) and \( \P^{-1}\N\P = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} = \N\tp \). In terms of operators: \( T\x = \N\x \) has \( T\e_1 = \0 \) and \( T\e_2 = \e_1 \). In the reordered basis \( \sB = (\e_2, \e_1) \), the first basis vector goes to the second and the second goes to \( \0 \), so \( \mtx{T}{\sB}{\sB} = \N\tp \). The same operator has both matrices, as @thm-similar-iff-same-operator predicts.
:::

::: {#exr-change-of-basis-c2}
[C2: \( \A\B \) and \( \B\A \)]

Let \( \A, \B \in M_n(F) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( \A \) is invertible, then \( \A\B \sim \B\A \).
2. Show that (a) fails without the invertibility hypothesis, even though \( \tr(\A\B) = \tr(\B\A) \) always holds.
:::
:::

::: {.solution}
(a) Since \( \A \) is invertible, \( \A^{-1}(\A\B)\A = (\A^{-1}\A)(\B\A) = \B\A \) by associativity. With \( \P = \A \) this is \( \B\A = \P^{-1}(\A\B)\P \), so \( \A\B \sim \B\A \).

(b) Take \( \A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \) and \( \B = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \). Then \( \A\B = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \), of rank \( 1 \), and \( \B\A = 0 \), of rank \( 0 \). By @prp-similarity-invariants (a), \( \A\B \not\sim \B\A \). Both traces are \( 0 \), in agreement with @thm-trace-properties; the trace simply cannot detect the difference.
:::

::: {#exr-change-of-basis-c3}
[C3: Every non-zero \( 2 \times 2 \) matrix with square zero]

Let \( \N \in M_2(F) \) with \( \N \ne 0 \) and \( \N^2 = 0 \), and let \( T \colon F^2 \to F^2 \), \( T\x = \N\x \).

::: {.enumerate options="label=(\alph*)"}
1. Explain why there is \( \v \in F^2 \) with \( \N\v \ne \0 \), and show that \( \sB = (\N\v, \v) \) is a basis of \( F^2 \).
2. Compute \( \mtx{T}{\sB}{\sB} \), and deduce that \( \N \sim \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \).
3. Hence show that \( \begin{pmatrix} 2 & -4 \\ 1 & -2 \end{pmatrix} \sim \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) in \( M_2(\nR) \), with an explicit \( \P \).
:::
:::

::: {.solution}
(a) Since \( \N \ne 0 \), some column \( \N\e_j \) is non-zero (@thm-matrix-times-vector-columns); take \( \v = \e_j \). Let \( a\N\v + b\v = \0 \). Multiplying by \( \N \) and using \( \N^2 = 0 \) gives \( b\N\v = \0 \), so \( b = 0 \) because \( \N\v \ne \0 \) (@thm-zero-product). Then \( a\N\v = \0 \) forces \( a = 0 \) for the same reason. So \( \sB \) is linearly independent of length \( 2 = \dim F^2 \), hence a basis by @thm-right-size-basis.

(b) \( T(\N\v) = \N^2\v = \0 \) and \( T\v = \N\v = 1 \cdot \N\v + 0 \cdot \v \). The columns of \( \mtx{T}{\sB}{\sB} \) are therefore \( (0, 0) \) and \( (1, 0) \), so \( \mtx{T}{\sB}{\sB} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \). Also \( \mtx{T}{\sE}{\sE} = \N \). By @thm-similar-iff-same-operator (a), \( \N \sim \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \).

(c) Let \( \N = \begin{pmatrix} 2 & -4 \\ 1 & -2 \end{pmatrix} \). Then \( \N^2 = \begin{pmatrix} 4 - 4 & -8 + 8 \\ 2 - 2 & -4 + 4 \end{pmatrix} = 0 \) and \( \N \ne 0 \). Take \( \v = \e_1 \), so \( \N\v = (2, 1) \), and \( \sB = ((2, 1), (1, 0)) \). By @thm-change-of-basis-maps, \( \P = \mtx{\id}{\sB}{\sE} = \begin{pmatrix} 2 & 1 \\ 1 & 0 \end{pmatrix} \) satisfies \( \P^{-1}\N\P = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \). Check: \( \P^{-1} = \begin{pmatrix} 0 & 1 \\ 1 & -2 \end{pmatrix} \) by @thm-two-by-two-inverse (here \( ad - bc = -1 \)), \( \N\P = \begin{pmatrix} 0 & 2 \\ 0 & 1 \end{pmatrix} \), and \( \P^{-1}\N\P = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \).
:::
