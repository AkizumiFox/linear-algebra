# The Matrix of a Linear Map

An isomorphism \( V \cong F^n \) turns the vectors of an abstract space into columns. This section does the same for **maps**. Once a basis is fixed on each side, every linear map between finite-dimensional spaces becomes a matrix, applying the map becomes multiplying by that matrix, and composing maps becomes multiplying matrices. This last fact finally explains the strange multiplication rule of Chapter 0, and it gives us the working method of the rest of the book: to study an abstract map, write down its matrix, compute there, and translate back.

## Writing a map as a matrix

We have seen one family of linear maps that is completely described by a table of numbers: the matrix maps \( T_\A \colon F^n \to F^m \), \( \x \mapsto \A\x \). In fact **every** linear map \( T \colon F^n \to F^m \) is one of them. By @thm-linear-combination and @thm-matrix-times-vector-columns, for \( \x = x_1\e_1 + \dots + x_n\e_n \),
\[
T\x = x_1T\e_1 + \dots + x_nT\e_n = \A\x, \qquad \text{where } \A = \begin{pmatrix} T\e_1 & \cdots & T\e_n \end{pmatrix}.
\]
The \( j \)-th column of \( \A \) is the image of the \( j \)-th basis vector. We want the same description for maps between arbitrary finite-dimensional spaces, such as differentiation on polynomials.

Take \( D \colon \nR[x]_{\le 3} \to \nR[x]_{\le 2} \). Then
\[
D(a_0 + a_1x + a_2x^2 + a_3x^3) = a_1 + 2a_2x + 3a_3x^2 .
\]
A polynomial is not a column, but its coordinates are. In the bases \( (1, x, x^2, x^3) \) and \( (1, x, x^2) \), the input has coordinates \( (a_0, a_1, a_2, a_3) \) and the output has coordinates \( (a_1, 2a_2, 3a_3) \), and
\[
\begin{pmatrix} a_1 \\ 2a_2 \\ 3a_3 \end{pmatrix} = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 3 \end{pmatrix} \begin{pmatrix} a_0 \\ a_1 \\ a_2 \\ a_3 \end{pmatrix}.
\]
Look at the columns of this matrix: \( (0, 0, 0) \), \( (1, 0, 0) \), \( (0, 2, 0) \), \( (0, 0, 3) \). They are the coordinates of \( D(1) = 0 \), \( D(x) = 1 \), \( D(x^2) = 2x \), \( D(x^3) = 3x^2 \). The standard example generalizes: record the images of the input basis, in coordinates of the output basis, as columns.

*The matrix of a linear map lists, column by column, where the input basis vectors go, written in coordinates of the output basis.*

::: {#def-matrix-of-linear-map}
[Matrix of a Linear Map]

Let \( V \) and \( W \) be finite-dimensional vector spaces over \( F \), with **ordered** bases \( \sB = (\v_1, \dots, \v_n) \) of \( V \) and \( \sC = (\w_1, \dots, \w_m) \) of \( W \), and let \( T \in \cL(V, W) \). The **matrix of \( T \) with respect to \( \sB \) and \( \sC \)** is the \( m \times n \) matrix
\[
\mtx{T}{\sB}{\sC} \coloneqq \begin{pmatrix} \coord{T\v_1}{\sC} & \coord{T\v_2}{\sC} & \cdots & \coord{T\v_n}{\sC} \end{pmatrix} \in M_{m \times n}(F),
\]
whose \( j \)-th column is the coordinate vector of \( T\v_j \) with respect to \( \sC \). Equivalently, its entries \( a_{ij} \) are the **unique** scalars with
\[
T\v_j = a_{1j}\w_1 + a_{2j}\w_2 + \dots + a_{mj}\w_m \qquad (j = 1, \dots, n).
\]
When \( V = W \) and \( \sB = \sC \), we call \( \mtx{T}{\sB}{\sB} \) the **matrix of the operator \( T \) with respect to \( \sB \)**; the basis is written in both slots even though it is the same one on each side.
:::

In words, clause by clause:

- **The input basis \( \sB \) is the subscript, the output basis \( \sC \) is the superscript.** The subscript sits next to where the input goes, as in \( \mtx{T}{\sB}{\sC}\coord{\v}{\sB} \) below.
- **Columns correspond to input basis vectors**, so there are \( n = \dim V \) of them; **rows correspond to output basis vectors**, so there are \( m = \dim W \). The size is "\( \dim(\text{codomain}) \times \dim(\text{domain}) \)", the same order as \( M_{m \times n} \) for \( T_\A \colon F^n \to F^m \).
- Column \( j \) answers one question: **where does \( \v_j \) go?**

**Well-definedness.** Each \( T\v_j \) lies in \( W \), and \( \sC \) is a basis, so \( \coord{T\v_j}{\sC} \) exists and is unique by @thm-unique-representation. So the matrix is determined by \( T \), \( \sB \) and \( \sC \). It is **not** determined by \( T \) alone: change either basis, or even the **order** of the vectors in one of them, and the matrix changes. That is why the bases are ordered.

::: {#exm-matrix-of-differentiation}
[Differentiation on Cubic Polynomials]

Let \( \sE_3 = (1, x, x^2, x^3) \) and \( \sE_2 = (1, x, x^2) \). Find \( \mtx{D}{\sE_3}{\sE_2} \) for \( D \colon \nR[x]_{\le 3} \to \nR[x]_{\le 2} \), and \( \mtx{D}{\sE_3}{\sE_3} \) for \( D \) regarded as an operator on \( \nR[x]_{\le 3} \).
:::

::: {.solution}
The images of the input basis are \( D(1) = 0 \), \( D(x) = 1 \), \( D(x^2) = 2x \), \( D(x^3) = 3x^2 \). In \( \sE_2 \) their coordinates are \( (0, 0, 0) \), \( (1, 0, 0) \), \( (0, 2, 0) \), \( (0, 0, 3) \); in \( \sE_3 \) the same vectors have a fourth coordinate \( 0 \). So
\[
\mtx{D}{\sE_3}{\sE_2} = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 3 \end{pmatrix}, \qquad
\mtx{D}{\sE_3}{\sE_3} = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 3 \\ 0 & 0 & 0 & 0 \end{pmatrix}.
\]
The same rule \( p \mapsto p' \) gives a \( 3 \times 4 \) or a \( 4 \times 4 \) matrix, depending on the codomain we declare. The superdiagonal \( 1, 2, 3 \) records "\( x^k \mapsto kx^{k-1} \)".
:::

::: {#exm-matrix-of-matrix-map}
[Matrix Maps and the Identity]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \A \in M_{m \times n}(F) \), and let \( \sE_n \), \( \sE_m \) be the standard bases of \( F^n \), \( F^m \). Show that \( \mtx{T_\A}{\sE_n}{\sE_m} = \A \).
2. Let \( \sB \) be any basis of an \( n \)-dimensional space \( V \). Find \( \mtx{\id_V}{\sB}{\sB} \) and the matrix of the zero map \( V \to W \) for any bases.
:::
:::

::: {.solution}
(a) The \( j \)-th column of \( \mtx{T_\A}{\sE_n}{\sE_m} \) is \( \coord{\A\e_j}{\sE_m} = \A\e_j \), since coordinates in the standard basis of \( F^m \) are the entries themselves; and \( \A\e_j \) is the \( j \)-th column of \( \A \) (@thm-matrix-times-vector-columns). So the matrix of a matrix map in the standard bases is the matrix we started with.

(b) \( \id_V\v_j = \v_j = 0\v_1 + \dots + 1\v_j + \dots + 0\v_n \), so the \( j \)-th column of \( \mtx{\id_V}{\sB}{\sB} \) is \( \e_j \), and \( \mtx{\id_V}{\sB}{\sB} = \I_n \). The zero map sends every \( \v_j \) to \( \0 \), whose coordinates are all \( 0 \), so its matrix is the zero matrix of size \( \dim W \times \dim V \), whatever the bases. These degenerate cases fix the expectations "identity map, identity matrix" and "zero map, zero matrix". The first needs the **same** basis on both sides, as the warning below shows.
:::

::: {#exm-matrix-of-transpose}
[The Transpose Map]

Let \( T \colon M_2(F) \to M_2(F) \), \( T(\X) = \X\tp \), and let \( \sE = (\E_{11}, \E_{12}, \E_{21}, \E_{22}) \). Find \( \mtx{T}{\sE}{\sE} \).
:::

::: {.solution}
\( T \) is linear by @thm-transpose-properties. Its values on the basis are \( \E_{11}\tp = \E_{11} \), \( \E_{12}\tp = \E_{21} \), \( \E_{21}\tp = \E_{12} \), \( \E_{22}\tp = \E_{22} \). In \( \sE \), these have coordinates \( \e_1, \e_3, \e_2, \e_4 \). So
\[
\mtx{T}{\sE}{\sE} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}.
\]
A map on a space of \( 2 \times 2 \) matrices is described by a \( 4 \times 4 \) matrix, because \( \dim M_2(F) = 4 \). Do not confuse the matrix \( \X \) that \( T \) acts on with the matrix \( \mtx{T}{\sE}{\sE} \) that describes \( T \).
:::

::: {#exm-matrix-of-reflection}
[A Reflection in Two Bases]

Let \( T \colon \nR^2 \to \nR^2 \) be the reflection across the line \( y = x \), \( T(x, y) = (y, x) \). Find \( \mtx{T}{\sE}{\sE} \) for the standard basis \( \sE = (\e_1, \e_2) \), and \( \mtx{T}{\sB}{\sB} \) for \( \sB = (\u_1, \u_2) \) with \( \u_1 = (1, 1) \) and \( \u_2 = (1, -1) \).
:::

::: {.solution}
\( T\e_1 = (0, 1) = \e_2 \) and \( T\e_2 = \e_1 \), so \( \mtx{T}{\sE}{\sE} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \).

The vectors \( \u_1, \u_2 \) are independent (neither is a multiple of the other), hence a basis of \( \nR^2 \) by @thm-right-size-basis. The first lies **on** the mirror line and the second is **perpendicular** to it: \( T\u_1 = (1, 1) = 1\u_1 + 0\u_2 \) and \( T\u_2 = (-1, 1) = 0\u_1 + (-1)\u_2 \). So
\[
\mtx{T}{\sB}{\sB} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.
\]
In the basis adapted to the geometry, the reflection is visibly "keep one direction, flip the other". The same map has a diagonal matrix in one basis and a non-diagonal one in another. How the two matrices are related is the subject of the next section.

The matrix also works in reverse: from \( \mtx{T}{\sB}{\sB} \) alone we can recover \( T \). Take \( \v = (3, 1) \). Its coordinates in \( \sB \) solve \( a\u_1 + b\u_2 = (3, 1) \), that is, \( a + b = 3 \) and \( a - b = 1 \), so \( \coord{\v}{\sB} = (2, 1) \), that is, \( \v = 2\u_1 + \u_2 \). By linearity, \( T\v = 2T\u_1 + T\u_2 \). The columns of \( \mtx{T}{\sB}{\sB} \) say \( T\u_1 = 1\u_1 + 0\u_2 \) and \( T\u_2 = 0\u_1 + (-1)\u_2 \), so \( T\v = 2\u_1 - \u_2 = (1, 3) \), which is indeed \( (y, x) \) at \( (3, 1) \). In coordinates, we turned \( (2, 1) \) into \( (2, -1) = \mtx{T}{\sB}{\sB}\begin{pmatrix} 2 \\ 1 \end{pmatrix} \); the next subsection proves that this "coordinates in, multiply, combine out" recipe always works.
:::

Here is a non-example by minimal change. In @exm-matrix-of-differentiation, write the coordinate vectors \( \coord{D(x^j)}{\sE_2} \) as **rows** instead of columns. The numbers are the same, but the result is the \( 4 \times 3 \) matrix \( \begin{pmatrix} 0 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix} \), and it cannot even be multiplied by the coordinate vector \( (a_0, a_1, a_2, a_3) \) of an input polynomial. The clause that fails is "the \( j \)-th **column** is \( \coord{T\v_j}{\sC} \)".

**Why this definition.** Why columns, and why coordinates in \( \sC \)? Because these are the choices under which "apply \( T \)" becomes "multiply by the matrix", as the \( D \) computation above suggested; we prove this next. With rows, we would get the transpose, and the natural formula \( \coord{T\v}{\sC} = \A\coord{\v}{\sB} \) would fail. The convention that the input basis is the subscript is chosen to make that formula easy to read: the \( \sB \) of the matrix sits next to the \( \sB \) of the vector.

::: {.warning}
**Three ways to get a matrix of a map wrong.**
(1) **Columns, not rows.** The \( j \)-th **column** is \( \coord{T\v_j}{\sC} \), as in the non-example above.
(2) **Order matters.** In @exm-matrix-of-reflection, reordering the standard basis as \( (\e_2, \e_1) \) leaves the matrix \( \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) unchanged, but reordering \( \sB \) as \( (\u_2, \u_1) \) gives \( \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix} \neq \mtx{T}{\sB}{\sB} \).
(3) **Input subscript, output superscript.** \( \mtx{T}{\sB}{\sC} \) and \( \mtx{T}{\sC}{\sB} \) are different objects, and for \( T \colon V \to W \) with \( V \neq W \) only one of them makes sense. Also \( \mtx{\id_V}{\sB}{\sC} \neq \I_n \) when \( \sB \neq \sC \): for \( \sB = (\e_1, \e_2) \) and \( \sC = (\e_2, \e_1) \) in \( \nR^2 \), \( \mtx{\id}{\sB}{\sC} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \).
:::

::: {.check}
What is the size of \( \mtx{T}{\sB}{\sC} \) for a linear map \( T \colon M_{2 \times 3}(\nR) \to \nR[x]_{\le 2} \)? And what is the first column of \( \mtx{T}{\sE}{\sE'} \) for \( T \colon \nR[x]_{\le 2} \to \nR^2 \), \( T(p) = (p(0), p(1)) \), with \( \sE = (1, x, x^2) \) and \( \sE' \) the standard basis of \( \nR^2 \)?
:::

::: {.solution}
\( \dim \nR[x]_{\le 2} = 3 \) and \( \dim M_{2 \times 3}(\nR) = 6 \), so the matrix is \( 3 \times 6 \): rows for the codomain, columns for the domain. For the second map, the first column is the coordinate vector of the image of the first basis vector \( 1 \): \( T(1) = (1, 1) \), so the column is \( (1, 1) \).
:::

## The fundamental square

Here is the promise behind the definition: once coordinates are taken on both sides, applying \( T \) **is** multiplying by its matrix.

::: {#thm-matrix-of-map-coordinates}
[Coordinates of an Image]

Let \( V \) and \( W \) be finite-dimensional vector spaces over \( F \) with ordered bases \( \sB = (\v_1, \dots, \v_n) \) and \( \sC = (\w_1, \dots, \w_m) \), and let \( T \in \cL(V, W) \). Then for every \( \v \in V \),
\[
\coord{T\v}{\sC} = \mtx{T}{\sB}{\sC}\,\coord{\v}{\sB} .
\]
Moreover, \( \mtx{T}{\sB}{\sC} \) is the **only** matrix \( \A \in M_{m \times n}(F) \) with \( \coord{T\v}{\sC} = \A\coord{\v}{\sB} \) for all \( \v \in V \).
:::

The statement says that the following square **commutes**: starting from \( \v \) in the top-left corner, the two routes to the bottom-right corner give the same column.

\begin{center}
\begin{tikzpicture}[>=Stealth, x=4.2cm, y=2.3cm]
  \node (V) at (0,1) {$V$};
  \node (W) at (1,1) {$W$};
  \node (Fn) at (0,0) {$F^n$};
  \node (Fm) at (1,0) {$F^m$};
  \draw[->] (V) -- node[above] {$T$} (W);
  \draw[->] (Fn) -- node[below] {multiply by $\mtx{T}{\sB}{\sC}$} (Fm);
  \draw[->] (V) -- node[left] {$\v \mapsto \coord{\v}{\sB}$} (Fn);
  \draw[->] (W) -- node[right] {$\w \mapsto \coord{\w}{\sC}$} (Fm);
  \node[font=\small] at (0,1.3) {$\v$};
  \node[font=\small] at (1,1.3) {$T\v$};
  \node[font=\small] at (0,-0.32) {$\coord{\v}{\sB}$};
  \node[font=\small] at (1,-0.32) {$\coord{T\v}{\sC} = \mtx{T}{\sB}{\sC}\coord{\v}{\sB}$};
\end{tikzpicture}
\end{center}

The top row is the abstract world, where \( T \) acts on vectors of \( V \). The bottom row is the matrix world, where a matrix acts on columns. The vertical arrows are the coordinate isomorphisms of @cor-coordinate-isomorphism, so nothing is lost going down or coming back up. **Right then down** (apply \( T \), then take coordinates) equals **down then right** (take coordinates, then multiply by the matrix).

::: {.idea}
Both sides are linear in \( \v \), so it is enough to check the formula on the basis vectors \( \v_j \), and there it is the definition: \( \coord{\v_j}{\sB} = \e_j \), and multiplying a matrix by \( \e_j \) picks out its \( j \)-th column, which was defined to be \( \coord{T\v_j}{\sC} \). Written out for a general \( \v \), this becomes a one-line chain. Uniqueness uses the same observation backwards: any \( \A \) that works must have \( \coord{T\v_j}{\sC} \) as its \( j \)-th column.
:::

::: {.proof}
Let \( \v \in V \) and \( \coord{\v}{\sB} = (x_1, \dots, x_n) \), so that \( \v = x_1\v_1 + \dots + x_n\v_n \). Since \( T \) is linear, @thm-linear-combination gives \( T\v = x_1T\v_1 + \dots + x_nT\v_n \). Since taking coordinates respects sums and scalar multiples (@thm-coordinates-linear),
\[
\coord{T\v}{\sC} = x_1\coord{T\v_1}{\sC} + \dots + x_n\coord{T\v_n}{\sC} = \mtx{T}{\sB}{\sC}\begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} = \mtx{T}{\sB}{\sC}\coord{\v}{\sB},
\]
where the middle equality is @thm-matrix-times-vector-columns applied to the columns \( \coord{T\v_j}{\sC} \) of \( \mtx{T}{\sB}{\sC} \).

For uniqueness, suppose \( \A \in M_{m \times n}(F) \) satisfies \( \coord{T\v}{\sC} = \A\coord{\v}{\sB} \) for all \( \v \). Taking \( \v = \v_j \), whose coordinate vector is \( \e_j \), the \( j \)-th column of \( \A \) is \( \A\e_j = \coord{T\v_j}{\sC} \) (@thm-matrix-times-vector-columns), which is the \( j \)-th column of \( \mtx{T}{\sB}{\sC} \). Hence \( \A = \mtx{T}{\sB}{\sC} \). This proves the theorem.
:::

This is the dictionary that lets us "write down a matrix first". A question about \( T \) (its kernel, its image, a preimage) becomes a question about a matrix, which Chapter 2 taught us to answer by row reduction; the coordinate isomorphisms carry the answer back.

::: {#exm-kernel-via-matrix}
[Kernel and Image Through a Matrix]

Let \( T \colon \nR[x]_{\le 2} \to \nR^2 \), \( T(p) = (p(1), p(-1)) \). Find \( \ker T \) and decide whether \( T \) is surjective, by working with the matrix of \( T \) in the bases \( \sE = (1, x, x^2) \) and the standard basis \( \sE' \) of \( \nR^2 \).
:::

::: {.solution}
*Write down the matrix.* \( T(1) = (1, 1) \), \( T(x) = (1, -1) \), \( T(x^2) = (1, 1) \), so
\[
\A = \mtx{T}{\sE}{\sE'} = \begin{pmatrix} 1 & 1 & 1 \\ 1 & -1 & 1 \end{pmatrix}.
\]
*Solve in the matrix world.* Subtracting the first row from the second gives \( \begin{pmatrix} 1 & 1 & 1 \\ 0 & -2 & 0 \end{pmatrix} \), so \( \A\x = \0 \) means \( x_2 = 0 \) and \( x_1 = -x_3 \): \( \nul(\A) = \Span\bigl((-1, 0, 1)\bigr) \). Both rows are pivot rows, so \( \rank \A = 2 \).

*Translate back.* By @thm-matrix-of-map-coordinates, \( T(p) = \0 \) exactly when \( \A\coord{p}{\sE} = \0 \) (the only vector with zero coordinates is \( \0 \)). The coordinate vector \( (-1, 0, 1) \) belongs to \( p = -1 + x^2 \). So
\[
\ker T = \Span(x^2 - 1),
\]
as a check confirms: \( x^2 - 1 \) vanishes at \( 1 \) and \( -1 \). By @thm-rank-nullity, \( \rank T = 3 - 1 = 2 = \dim \nR^2 \), so \( \im T = \nR^2 \) by @thm-dim-impl-eq, and \( T \) is surjective: any two values \( p(1) \), \( p(-1) \) can be prescribed.
:::

## Composition is matrix multiplication

In Chapter 0, §9 we asked why matrices are multiplied row-against-column. The answer given there was **substitution**. If \( \y = \B\x \) and \( \z = \A\y \), with
\[
\B = \begin{pmatrix} 2 & 1 \\ 1 & 4 \end{pmatrix}, \qquad \A = \begin{pmatrix} 1 & 2 \\ 3 & -1 \end{pmatrix},
\]
then substituting gives \( \z = \begin{pmatrix} 4 & 9 \\ 5 & -1 \end{pmatrix}\x \), and the table of the combined substitution turned out to be \( \A\B \). At the time we promised that this fact would become a statement about linear maps. We can now say what it is. Each substitution is a linear map, \( T_\B \colon \x \mapsto \y \) and \( T_\A \colon \y \mapsto \z \), and substituting one into the other is **composing** them: \( \z = T_\A(T_\B\x) = (T_\A T_\B)\x \). So the Chapter 0 computation says \( T_\A T_\B = T_{\A\B} \). Here is the general statement, for arbitrary spaces and bases.

::: {#thm-matrix-of-composition}
[Matrix of a Composition]

Let \( U, V, W \) be finite-dimensional vector spaces over \( F \) with ordered bases \( \sB \), \( \sC \), \( \sD \) respectively. Let \( T \in \cL(U, V) \) and \( S \in \cL(V, W) \). Then
\[
\mtx{ST}{\sB}{\sD} = \mtx{S}{\sC}{\sD}\,\mtx{T}{\sB}{\sC} .
\]
:::

Notice how the notation checks itself: the middle basis \( \sC \) appears as the output of \( T \) and the input of \( S \), and it "cancels", leaving \( \sB \) below and \( \sD \) above. The order of the factors is the order of the maps: the map applied first is on the right, in both \( ST \) and the product.

::: {.idea}
Glue two commutative squares side by side. The left square is \( T \) with its matrix, the right square is \( S \) with its matrix, and they share the middle column \( V \to F^{\dim V} \). Going along the top from \( U \) to \( W \) is \( ST \); going along the bottom is multiplication by \( \mtx{T}{\sB}{\sC} \) followed by multiplication by \( \mtx{S}{\sC}{\sD} \), which is multiplication by their product. The big rectangle commutes because both small squares do, and the uniqueness part of @thm-matrix-of-map-coordinates identifies the product as the matrix of \( ST \).

\begin{center}
\begin{tikzpicture}[>=Stealth, x=3.2cm, y=2.1cm]
  \node (U) at (0,1) {$U$};
  \node (V) at (1,1) {$V$};
  \node (W) at (2,1) {$W$};
  \node (Fp) at (0,0) {$F^{p}$};
  \node (Fn) at (1,0) {$F^{n}$};
  \node (Fm) at (2,0) {$F^{m}$};
  \draw[->] (U) -- node[above] {$T$} (V);
  \draw[->] (V) -- node[above] {$S$} (W);
  \draw[->] (Fp) -- node[below] {$\mtx{T}{\sB}{\sC}$} (Fn);
  \draw[->] (Fn) -- node[below] {$\mtx{S}{\sC}{\sD}$} (Fm);
  \draw[->] (U) -- node[left] {$\coord{\cdot}{\sB}$} (Fp);
  \draw[->] (V) -- node[left] {$\coord{\cdot}{\sC}$} (Fn);
  \draw[->] (W) -- node[right] {$\coord{\cdot}{\sD}$} (Fm);
\end{tikzpicture}
\end{center}
:::

::: {.proof}
Let \( p = \dim U \) and \( m = \dim W \), and let \( \u \in U \). Applying @thm-matrix-of-map-coordinates first to \( S \) and the vector \( T\u \), then to \( T \) and \( \u \),
\[
\coord{ST\u}{\sD} = \coord{S(T\u)}{\sD} = \mtx{S}{\sC}{\sD}\coord{T\u}{\sC} = \mtx{S}{\sC}{\sD}\bigl(\mtx{T}{\sB}{\sC}\coord{\u}{\sB}\bigr) = \bigl(\mtx{S}{\sC}{\sD}\mtx{T}{\sB}{\sC}\bigr)\coord{\u}{\sB},
\]
where the last equality is associativity of matrix multiplication (@thm-matrix-multiplication-properties). The map \( ST \) is linear (@thm-composition-linear), and the \( m \times p \) matrix \( \mtx{S}{\sC}{\sD}\mtx{T}{\sB}{\sC} \) satisfies \( \coord{ST\u}{\sD} = \bigl(\mtx{S}{\sC}{\sD}\mtx{T}{\sB}{\sC}\bigr)\coord{\u}{\sB} \) for every \( \u \in U \). By the uniqueness part of @thm-matrix-of-map-coordinates, it equals \( \mtx{ST}{\sB}{\sD} \). This proves the theorem.
:::

This is the payoff of the hook in Chapter 0, §9 (@def-matrix-multiplication). The row-times-column rule was not an arbitrary convention: it is the **only** rule under which the matrix of a composition is the product of the matrices, because composing linear maps is substituting one coordinate formula into another. Everything Chapter 0 proved about matrix multiplication now has a meaning for maps, and conversely:

- **associativity** of matrix multiplication is associativity of composition (@thm-composition-associative);
- \( \A\B \neq \B\A \) in general is \( ST \neq TS \) (@exm-rotation-projection-dont-commute);
- the size condition "columns of \( \A \) = rows of \( \B \)" is "the codomain of the first map is the domain of the second";
- in particular \( T_\A T_\B = T_{\A\B} \): apply the theorem with standard bases and @exm-matrix-of-matrix-map (a).

::: {#exm-matrix-of-composition}
[Multiply by \( x \), Then Differentiate]

Let \( S \colon \nR[x]_{\le 2} \to \nR[x]_{\le 3} \), \( S(p) = xp \), and \( D \colon \nR[x]_{\le 3} \to \nR[x]_{\le 2} \), \( D(p) = p' \), with the monomial bases \( \sE_2 = (1, x, x^2) \) and \( \sE_3 = (1, x, x^2, x^3) \). Compute \( \mtx{DS}{\sE_2}{\sE_2} \) and \( \mtx{SD}{\sE_3}{\sE_3} \), both directly and as products.
:::

::: {.solution}
*Matrices of the factors.* \( S(1) = x \), \( S(x) = x^2 \), \( S(x^2) = x^3 \), and \( \mtx{D}{\sE_3}{\sE_2} \) was found in @exm-matrix-of-differentiation:
\[
\mtx{S}{\sE_2}{\sE_3} = \begin{pmatrix} 0 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad
\mtx{D}{\sE_3}{\sE_2} = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 3 \end{pmatrix}.
\]
*Products.* By @thm-matrix-of-composition,
\[
\mtx{DS}{\sE_2}{\sE_2} = \mtx{D}{\sE_3}{\sE_2}\mtx{S}{\sE_2}{\sE_3} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix}, \qquad
\mtx{SD}{\sE_3}{\sE_3} = \mtx{S}{\sE_2}{\sE_3}\mtx{D}{\sE_3}{\sE_2} = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 3 \end{pmatrix}.
\]
*Directly.* \( DS(x^k) = (x^{k+1})' = (k + 1)x^k \) for \( k = 0, 1, 2 \), giving the diagonal \( 1, 2, 3 \). And \( SD(x^k) = x \cdot kx^{k-1} = kx^k \) for \( k \ge 1 \), with \( SD(1) = 0 \), giving the diagonal \( 0, 1, 2, 3 \). Both computations agree. The two composites are not even the same size: \( DS \) is an operator on \( \nR[x]_{\le 2} \) and \( SD \) an operator on \( \nR[x]_{\le 3} \).
:::

For operators, the theorem applies with \( \sB = \sC = \sD \), and gives powers and polynomials.

::: {#cor-matrix-of-polynomial-of-operator}
[Matrices of Powers and Polynomials]

Let \( \sB = (\v_1, \dots, \v_n) \) be a basis of a finite-dimensional space \( V \), let \( T, S \in \cL(V) \), \( c \in F \) and \( p \in F[x] \). Then \( \mtx{ST}{\sB}{\sB} = \mtx{S}{\sB}{\sB}\mtx{T}{\sB}{\sB} \), \( \mtx{S + T}{\sB}{\sB} = \mtx{S}{\sB}{\sB} + \mtx{T}{\sB}{\sB} \), \( \mtx{cT}{\sB}{\sB} = c\mtx{T}{\sB}{\sB} \), \( \mtx{T^k}{\sB}{\sB} = (\mtx{T}{\sB}{\sB})^k \) for \( k \in \nN \), and
\[
\mtx{p(T)}{\sB}{\sB} = p\bigl(\mtx{T}{\sB}{\sB}\bigr).
\]
:::

::: {.proof}
The first formula is @thm-matrix-of-composition with \( \sB = \sC = \sD \). For sums and scalar multiples, the \( j \)-th column of \( \mtx{S + T}{\sB}{\sB} \) is \( \coord{S\v_j + T\v_j}{\sB} = \coord{S\v_j}{\sB} + \coord{T\v_j}{\sB} \) by @thm-coordinates-linear, and similarly \( \coord{cT\v_j}{\sB} = c\coord{T\v_j}{\sB} \). For powers we induct on \( k \): \( \mtx{T^0}{\sB}{\sB} = \mtx{\id_V}{\sB}{\sB} = \I_n \) by @exm-matrix-of-matrix-map (b), and if \( \mtx{T^k}{\sB}{\sB} = (\mtx{T}{\sB}{\sB})^k \), then \( \mtx{T^{k+1}}{\sB}{\sB} = \mtx{T^kT}{\sB}{\sB} = (\mtx{T}{\sB}{\sB})^k\mtx{T}{\sB}{\sB} = (\mtx{T}{\sB}{\sB})^{k+1} \), by the first formula and @def-polynomial-of-matrix. Finally, for \( p = \sum_k a_kx^k \), combining the three rules gives \( \mtx{p(T)}{\sB}{\sB} = \sum_k a_k\mtx{T^k}{\sB}{\sB} = \sum_k a_k(\mtx{T}{\sB}{\sB})^k = p(\mtx{T}{\sB}{\sB}) \), using @def-polynomial-of-operator and @def-polynomial-of-matrix.
:::

For example, with \( \mtx{D}{\sE_3}{\sE_3} \) from @exm-matrix-of-differentiation, \( (\mtx{D}{\sE_3}{\sE_3})^4 = \mtx{D^4}{\sE_3}{\sE_3} = 0 \), recovering @exm-differentiation-nilpotent in matrix form.

## Linear maps are matrices

The sums in @cor-matrix-of-polynomial-of-operator work between different spaces too, and together with the construction of maps from values on a basis they show that, after choosing bases, there is no difference at all between linear maps and matrices.

::: {#thm-linear-maps-isomorphic-to-matrices}
[\( \cL(V, W) \cong M_{m \times n}(F) \)]

Let \( V \) and \( W \) be finite-dimensional vector spaces over \( F \) with ordered bases \( \sB = (\v_1, \dots, \v_n) \) and \( \sC = (\w_1, \dots, \w_m) \). Then the map
\[
\Phi \colon \cL(V, W) \to M_{m \times n}(F), \qquad T \mapsto \mtx{T}{\sB}{\sC},
\]
is an isomorphism. In particular, \( \dim \cL(V, W) = mn = (\dim V)(\dim W) \).
:::

::: {.idea}
Three things to check. *Linear:* columns of \( \mtx{S + T}{\sB}{\sC} \) are coordinates of \( S\v_j + T\v_j \), and coordinates respect sums. *Injective:* a map whose matrix is zero kills every basis vector, so it is the zero map. *Surjective:* a matrix prescribes the value of each \( \v_j \), and a linear map with prescribed values on a basis exists. The last two are the uniqueness and existence halves of the same theorem about bases, which is why a linear map is "nothing but" its values on a basis.
:::

::: {.proof}
*Linear.* Let \( S, T \in \cL(V, W) \) and \( c \in F \). By @def-space-of-linear-maps and @thm-coordinates-linear, the \( j \)-th column of \( \mtx{S + T}{\sB}{\sC} \) is \( \coord{S\v_j + T\v_j}{\sC} = \coord{S\v_j}{\sC} + \coord{T\v_j}{\sC} \), and that of \( \mtx{cT}{\sB}{\sC} \) is \( \coord{cT\v_j}{\sC} = c\coord{T\v_j}{\sC} \). Hence \( \Phi(S + T) = \Phi(S) + \Phi(T) \) and \( \Phi(cT) = c\,\Phi(T) \).

*Injective.* Suppose \( \Phi(T) = 0 \). Then \( \coord{T\v_j}{\sC} = \0 \), so \( T\v_j = \0 \) for every \( j \). The zero map also sends every \( \v_j \) to \( \0 \), so \( T = 0 \) by the uniqueness part of @thm-linear-transform-basis. Hence \( \ker \Phi = \{0\} \), and \( \Phi \) is injective by @thm-injective-iff-trivial-kernel.

*Surjective.* Let \( \A = (a_{ij}) \in M_{m \times n}(F) \). By the existence part of @thm-linear-transform-basis there is \( T \in \cL(V, W) \) with \( T\v_j = a_{1j}\w_1 + \dots + a_{mj}\w_m \) for each \( j \). By @def-matrix-of-linear-map, \( \mtx{T}{\sB}{\sC} = \A \).

So \( \Phi \) is a bijective linear map, an isomorphism by @thm-inverse-is-linear. For the dimension, we cannot quote @thm-isomorphic-iff-same-dimension directly, since we do not yet know that \( \cL(V, W) \) is finite-dimensional. Instead, \( M_{m \times n}(F) \) has a basis of \( mn \) matrix units (@exm-dimensions), and the inverse isomorphism \( \Phi^{-1} \) carries it to a basis of \( \cL(V, W) \) of length \( mn \) (@thm-isomorphism-preserves-bases, applied to \( \Phi^{-1} \), which is an isomorphism by @thm-isomorphic-equivalence-relation). Hence \( \dim \cL(V, W) = mn \). This proves the theorem.
:::

With @thm-matrix-of-composition, the isomorphism \( \Phi \) also turns composition into multiplication. So, for \( V = W \) and \( \sB = \sC \), the algebra \( \cL(V) \) of the previous sections and the algebra \( M_n(F) \) of Chapter 0 are the same algebra, written in two languages. The dictionary depends on the basis, as every isomorphism to \( F^n \) does.

## Reading rank and invertibility from a matrix

Chapter 2 developed tools for the rank and the invertibility of matrices. The square of @thm-matrix-of-map-coordinates transfers all of them to linear maps.

::: {#thm-rank-map-equals-rank-matrix}
[Rank and Invertibility from the Matrix]

Let \( V \) and \( W \) be finite-dimensional vector spaces over \( F \) with ordered bases \( \sB \) and \( \sC \), let \( T \in \cL(V, W) \), and let \( \A = \mtx{T}{\sB}{\sC} \).

::: {.enumerate options="label=(\alph*)"}
1. The coordinate map \( \v \mapsto \coord{\v}{\sB} \) restricts to an isomorphism \( \ker T \to \nul(\A) \), and the coordinate map \( \w \mapsto \coord{\w}{\sC} \) restricts to an isomorphism \( \im T \to \col(\A) \). Hence
\[
\rank T = \rank \A \qquad \text{and} \qquad \nullity T = \nullity \A .
\]
2. Suppose \( \dim V = \dim W \). Then \( T \) is invertible if and only if \( \A \) is invertible, and in that case \( \mtx{T^{-1}}{\sC}{\sB} = \A^{-1} \).
:::
:::

::: {.idea}
For (a), the commutative square says a vector is killed by \( T \) exactly when its coordinate column is killed by \( \A \), and the outputs of \( T \), in coordinates, are exactly the outputs of \( \A \). Isomorphic subspaces have the same dimension. For (b), \( T^{-1}T = \id_V \) translates, by the composition theorem, into a matrix equation with \( \I_n \) on the right; conversely an inverse matrix is the matrix of **some** map, by the isomorphism \( \cL(W, V) \cong M_n(F) \), and that map is the inverse of \( T \).
:::

::: {.proof}
Let \( n = \dim V \) and \( m = \dim W \), and write \( C_{\sB} \colon V \to F^n \) and \( C_{\sC} \colon W \to F^m \) for the coordinate isomorphisms (@cor-coordinate-isomorphism).

(a) *Kernel.* For \( \v \in V \): \( \v \in \ker T \) iff \( T\v = \0 \) iff \( \coord{T\v}{\sC} = \0 \) (since \( C_{\sC} \) is injective) iff \( \A\coord{\v}{\sB} = \0 \) (@thm-matrix-of-map-coordinates) iff \( \coord{\v}{\sB} \in \nul(\A) \). So \( C_{\sB} \) maps \( \ker T \) into \( \nul(\A) \), and every \( \x \in \nul(\A) \) is \( \coord{\v}{\sB} \) for some \( \v \in V \) (surjectivity of \( C_{\sB} \)), which then lies in \( \ker T \). Thus the restriction of \( C_{\sB} \) is a linear map \( \ker T \to \nul(\A) \), injective because \( C_{\sB} \) is, and surjective. By @thm-inverse-is-linear it is an isomorphism.

*Image.* By @thm-matrix-of-map-coordinates, \( C_{\sC}(T\v) = \A\,C_{\sB}(\v) \) for every \( \v \in V \). As \( \v \) runs over \( V \), \( C_{\sB}(\v) \) runs over all of \( F^n \), so \( \{ C_{\sC}(\w) : \w \in \im T \} = \{ \A\x : \x \in F^n \} = \col(\A) \) (@def-column-space). So the restriction of \( C_{\sC} \) is a linear map \( \im T \to \col(\A) \), surjective by this computation and injective because \( C_{\sC} \) is; hence an isomorphism.

The subspaces involved are finite-dimensional (@thm-subspace-dimension), so @thm-isomorphic-iff-same-dimension gives \( \dim \ker T = \dim \nul(\A) \) and \( \dim \im T = \dim \col(\A) \), which are the stated equalities by @def-nullity, @def-rank, @def-nullity-matrix and @def-rank-matrix.

(b) \( (\Rightarrow) \) Suppose \( T \) is invertible. By @thm-matrix-of-composition and @exm-matrix-of-matrix-map (b),
\[
\mtx{T^{-1}}{\sC}{\sB}\,\A = \mtx{T^{-1}T}{\sB}{\sB} = \mtx{\id_V}{\sB}{\sB} = \I_n, \qquad \A\,\mtx{T^{-1}}{\sC}{\sB} = \mtx{TT^{-1}}{\sC}{\sC} = \mtx{\id_W}{\sC}{\sC} = \I_n .
\]
So \( \A \) is invertible with \( \A^{-1} = \mtx{T^{-1}}{\sC}{\sB} \) (@def-invertible-matrix).

\( (\Leftarrow) \) Suppose \( \A \) is invertible. By @thm-linear-maps-isomorphic-to-matrices (for \( \cL(W, V) \) with bases \( \sC \) and \( \sB \)), there is \( S \in \cL(W, V) \) with \( \mtx{S}{\sC}{\sB} = \A^{-1} \). Then by @thm-matrix-of-composition, \( \mtx{ST}{\sB}{\sB} = \A^{-1}\A = \I_n = \mtx{\id_V}{\sB}{\sB} \). Since \( T' \mapsto \mtx{T'}{\sB}{\sB} \) is injective on \( \cL(V) \) (@thm-linear-maps-isomorphic-to-matrices), \( ST = \id_V \). By @thm-one-sided-inverse-maps, \( T \) is invertible with \( T^{-1} = S \). This proves the theorem.
:::

So we may add one more item to the Invertible Operator Theorem (@thm-invertible-operator-tfae): for \( T \in \cL(V) \) and **any** basis \( \sB \) of \( V \), \( T \) is invertible if and only if \( \mtx{T}{\sB}{\sB} \) is invertible. Every item of the Invertible Matrix Theorem (@thm-invertible-tfae) now becomes a test for operators.

::: {#exm-rank-from-matrix}
[Rank of \( \X \mapsto \X + \X\tp \)]

Let \( T \colon M_2(\nR) \to M_2(\nR) \), \( T(\X) = \X + \X\tp \), and \( \sE = (\E_{11}, \E_{12}, \E_{21}, \E_{22}) \). Find \( \mtx{T}{\sE}{\sE} \), use it to find \( \rank T \), a basis of \( \ker T \) and a basis of \( \im T \), and decide whether \( T \) is invertible. Then do the same for the transpose map of @exm-matrix-of-transpose.
:::

::: {.solution}
*Matrix.* \( T(\E_{11}) = 2\E_{11} \), \( T(\E_{12}) = \E_{12} + \E_{21} = T(\E_{21}) \), \( T(\E_{22}) = 2\E_{22} \). So
\[
\A = \mtx{T}{\sE}{\sE} = \begin{pmatrix} 2 & 0 & 0 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 2 \end{pmatrix}.
\]
*Matrix world.* Subtracting row 2 from row 3 turns row 3 into a zero row; moving it to the bottom gives an echelon form with three non-zero rows and pivots in columns 1, 2, 4. So \( \rank \A = 3 \) and \( \nullity \A = 1 \). The free column is column 3, and \( \A\x = \0 \) gives \( x_1 = x_4 = 0 \), \( x_2 = -x_3 \), so \( \nul(\A) = \Span\bigl((0, -1, 1, 0)\bigr) \). By @thm-basis-column-space, the pivot columns \( (2, 0, 0, 0) \), \( (0, 1, 1, 0) \), \( (0, 0, 0, 2) \) form a basis of \( \col(\A) \).

*Translate back.* By @thm-rank-map-equals-rank-matrix, \( \rank T = 3 \). The column \( (0, -1, 1, 0) \) is the coordinate vector of \( \E_{21} - \E_{12} \), so \( \ker T = \Span\left(\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\right) \), the skew-symmetric matrices. The basis of \( \col(\A) \) translates to \( 2\E_{11} \), \( \E_{12} + \E_{21} \), \( 2\E_{22} \), a basis of \( \im T \), which is therefore the space of symmetric matrices. Since \( \rank \A = 3 < 4 \), \( \A \) is not invertible (@thm-invertible-tfae), and neither is \( T \).

*Transpose.* The matrix \( \P = \mtx{\X \mapsto \X\tp}{\sE}{\sE} \) from @exm-matrix-of-transpose satisfies \( \P^2 = \I_4 \) (swapping two coordinates twice does nothing). So \( \P \) is invertible with \( \P^{-1} = \P \), and by @thm-rank-map-equals-rank-matrix (b) the transpose map is invertible and is its own inverse, which is \( (\X\tp)\tp = \X \) again.
:::

We now have both halves of the working method: a basis turns spaces into \( F^n \) and maps into matrices, and every computation can be done with Chapter 2's tools. What we have not yet controlled is the choice. @exm-matrix-of-reflection shows that one map can have a complicated matrix in one basis and a diagonal one in another; the next section finds the formula relating the two.

## Exercises

### A. Check your understanding

::: {#exr-matrix-of-a-map-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define \( \mtx{T}{\sB}{\sC} \) for \( T \in \cL(V, W) \) and ordered bases \( \sB \) of \( V \), \( \sC \) of \( W \).
2. State the formula relating \( \coord{T\v}{\sC} \) and \( \coord{\v}{\sB} \), and the formula for the matrix of a composition.
3. True or false: the \( j \)-th **row** of \( \mtx{T}{\sB}{\sC} \) is \( \coord{T\v_j}{\sC} \). Justify your answer.
4. True or false: \( \mtx{\id_V}{\sB}{\sC} = \I_n \) for any two bases \( \sB \), \( \sC \) of an \( n \)-dimensional space \( V \). Justify your answer.
5. What is \( \dim \cL(\nR^3, \nR[x]_{\le 2}) \)?
:::
:::

::: {.solution}
(a) If \( \sB = (\v_1, \dots, \v_n) \), then \( \mtx{T}{\sB}{\sC} \) is the \( \dim W \times n \) matrix whose \( j \)-th column is \( \coord{T\v_j}{\sC} \) (@def-matrix-of-linear-map).

(b) \( \coord{T\v}{\sC} = \mtx{T}{\sB}{\sC}\coord{\v}{\sB} \) (@thm-matrix-of-map-coordinates), and \( \mtx{ST}{\sB}{\sD} = \mtx{S}{\sC}{\sD}\mtx{T}{\sB}{\sC} \) (@thm-matrix-of-composition).

(c) False. It is the \( j \)-th **column**. For \( D \colon \nR[x]_{\le 3} \to \nR[x]_{\le 2} \) in @exm-matrix-of-differentiation, \( \coord{D(x)}{\sE_2} = (1, 0, 0) \) is the second column, while the second row is \( (0, 0, 2, 0) \).

(d) False. In \( \nR^2 \) with \( \sB = (\e_1, \e_2) \) and \( \sC = (\e_2, \e_1) \), \( \coord{\e_1}{\sC} = (0, 1) \), so the first column of \( \mtx{\id}{\sB}{\sC} \) is \( (0, 1) \neq \e_1 \). It is true when \( \sB = \sC \) (@exm-matrix-of-matrix-map (b)).

(e) \( 3 \cdot 3 = 9 \), by @thm-linear-maps-isomorphic-to-matrices.
:::

### B. Practice

::: {#exr-matrix-of-a-map-b1}
[B1: Matrices in given bases]

Find the matrix of each operator in the given basis. (Both maps are linear; you may take this as given.)

::: {.enumerate options="label=(\alph*)"}
1. \( T \colon \nR[x]_{\le 2} \to \nR[x]_{\le 2} \), \( T(p) = p(x + 1) \), in \( \sE = (1, x, x^2) \).
2. \( T \colon M_2(\nR) \to M_2(\nR) \), \( T(\X) = \B\X \) with \( \B = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \), in \( \sE = (\E_{11}, \E_{12}, \E_{21}, \E_{22}) \).
:::
:::

::: {.solution}
(a) \( T(1) = 1 \), \( T(x) = x + 1 = 1 + x \), \( T(x^2) = (x + 1)^2 = 1 + 2x + x^2 \). Their coordinates are \( (1, 0, 0) \), \( (1, 1, 0) \), \( (1, 2, 1) \), so
\[
\mtx{T}{\sE}{\sE} = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix}.
\]
(b) Multiplying \( \B \) by a matrix unit \( \E_{kj} \) on the right keeps column \( k \) of \( \B \) and moves it to column \( j \):
\[
\B\E_{11} = \begin{pmatrix} 1 & 0 \\ 3 & 0 \end{pmatrix}, \quad \B\E_{12} = \begin{pmatrix} 0 & 1 \\ 0 & 3 \end{pmatrix}, \quad \B\E_{21} = \begin{pmatrix} 2 & 0 \\ 4 & 0 \end{pmatrix}, \quad \B\E_{22} = \begin{pmatrix} 0 & 2 \\ 0 & 4 \end{pmatrix}.
\]
Reading entries in the order \( (1,1), (1,2), (2,1), (2,2) \) gives the columns \( (1, 0, 3, 0) \), \( (0, 1, 0, 3) \), \( (2, 0, 4, 0) \), \( (0, 2, 0, 4) \), so
\[
\mtx{T}{\sE}{\sE} = \begin{pmatrix} 1 & 0 & 2 & 0 \\ 0 & 1 & 0 & 2 \\ 3 & 0 & 4 & 0 \\ 0 & 3 & 0 & 4 \end{pmatrix}.
\]
:::

::: {#exr-matrix-of-a-map-b2}
[B2: Recovering a map from its matrix]

Let \( \sB = (1, \, 1 + x, \, x^2) \), a basis of \( \nR[x]_{\le 2} \), and let \( \sE' \) be the standard basis of \( \nR^2 \). A linear map \( T \colon \nR[x]_{\le 2} \to \nR^2 \) has
\[
\mtx{T}{\sB}{\sE'} = \begin{pmatrix} 1 & 0 & 2 \\ 0 & 1 & -1 \end{pmatrix}.
\]
Find \( T(a + bx + cx^2) \). Hence find a basis of \( \ker T \).
:::

::: {.solution}
First find the coordinates of \( p = a + bx + cx^2 \) in \( \sB \): \( p = (a - b) \cdot 1 + b(1 + x) + cx^2 \), so \( \coord{p}{\sB} = (a - b, \, b, \, c) \), unique by @thm-unique-representation. By @thm-matrix-of-map-coordinates, and since coordinates in \( \sE' \) are the entries,
\[
T(p) = \begin{pmatrix} 1 & 0 & 2 \\ 0 & 1 & -1 \end{pmatrix}\begin{pmatrix} a - b \\ b \\ c \end{pmatrix} = (a - b + 2c, \; b - c).
\]
Hence \( T(p) = \0 \) iff \( b = c \) and \( a = b - 2c = -c \), that is, \( p = c(-1 + x + x^2) \). So \( (x^2 + x - 1) \) is a basis of \( \ker T \). Check: \( \coord{x^2 + x - 1}{\sB} = (-2, 1, 1) \), and \( \begin{pmatrix} 1 & 0 & 2 \\ 0 & 1 & -1 \end{pmatrix}(-2, 1, 1) = (0, 0) \).
:::

::: {#exr-matrix-of-a-map-b3}
[B3: A composition computed two ways]

Let \( T \colon \nR[x]_{\le 1} \to \nR[x]_{\le 2} \), \( T(p) = xp \), and \( S \colon \nR[x]_{\le 2} \to \nR^2 \), \( S(p) = (p(0), p(1)) \). Use the monomial bases and the standard basis of \( \nR^2 \). Compute the matrix of \( ST \) directly, and again as a product of the matrices of \( S \) and \( T \).
:::

::: {.solution}
Let \( \sE_1 = (1, x) \), \( \sE_2 = (1, x, x^2) \) and \( \sE' \) the standard basis of \( \nR^2 \).

*Factors.* \( T(1) = x \), \( T(x) = x^2 \), so \( \mtx{T}{\sE_1}{\sE_2} = \begin{pmatrix} 0 & 0 \\ 1 & 0 \\ 0 & 1 \end{pmatrix} \). \( S(1) = (1, 1) \), \( S(x) = (0, 1) \), \( S(x^2) = (0, 1) \), so \( \mtx{S}{\sE_2}{\sE'} = \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 1 \end{pmatrix} \).

*Product.* By @thm-matrix-of-composition,
\[
\mtx{ST}{\sE_1}{\sE'} = \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 1 \end{pmatrix}\begin{pmatrix} 0 & 0 \\ 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 1 & 1 \end{pmatrix}.
\]
*Directly.* \( ST(1) = S(x) = (0, 1) \) and \( ST(x) = S(x^2) = (0, 1) \), so the columns are \( (0, 1) \) and \( (0, 1) \), in agreement. In words, \( ST(a + bx) = (0, \, a + b) \).
:::

### C. Going deeper

::: {#exr-matrix-of-a-map-c1}
[C1: Upper triangular matrices and invariant subspaces]

Let \( V \) be finite-dimensional and \( T \in \cL(V) \). A subspace \( U \) of \( V \) is **\( T \)-invariant** if \( T\u \in U \) for every \( \u \in U \). Let \( \sB = (\v_1, \dots, \v_n) \) be a basis of \( V \), and for \( 1 \le k \le n \) let \( U_k = \Span(\v_1, \dots, \v_k) \). Prove that \( \mtx{T}{\sB}{\sB} \) is upper triangular if and only if every \( U_k \) is \( T \)-invariant.
:::

::: {.solution}
Let \( \mtx{T}{\sB}{\sB} = (a_{ij}) \), so \( T\v_j = \sum_{i=1}^{n} a_{ij}\v_i \) with unique coefficients (@def-matrix-of-linear-map). By @def-upper-triangular, \( \mtx{T}{\sB}{\sB} \) is upper triangular iff \( a_{ij} = 0 \) whenever \( i > j \), that is, iff
\[
T\v_j \in U_j \quad \text{for every } j = 1, \dots, n. \tag{$\ast$}
\]
Indeed, if \( a_{ij} = 0 \) for \( i > j \), then \( T\v_j = \sum_{i \le j} a_{ij}\v_i \in U_j \); conversely, if \( T\v_j = \sum_{i \le j} b_i\v_i \), then by uniqueness of coordinates \( a_{ij} = 0 \) for \( i > j \).

\( (\Rightarrow) \) Assume \( (\ast) \), and fix \( k \). For \( j \le k \), \( T\v_j \in U_j \subseteq U_k \). Let \( \u = \sum_{j \le k} c_j\v_j \in U_k \). Then \( T\u = \sum_{j \le k} c_jT\v_j \) by @thm-linear-combination, a combination of vectors of the subspace \( U_k \), so \( T\u \in U_k \) by @thm-span-subspace. Hence \( U_k \) is \( T \)-invariant.

\( (\Leftarrow) \) Assume every \( U_k \) is \( T \)-invariant. For each \( j \), \( \v_j \in U_j \), so \( T\v_j \in U_j \) by invariance of \( U_j \). This is \( (\ast) \), so \( \mtx{T}{\sB}{\sB} \) is upper triangular.
:::

::: {#exr-matrix-of-a-map-c2}
[C2: Integrating with a matrix]

Let \( f_1(x) = e^x \), \( f_2(x) = xe^x \), \( f_3(x) = x^2e^x \), and let \( V = \Span(f_1, f_2, f_3) \) inside the real vector space of all functions \( \nR \to \nR \) (@exm-vector-spaces (d)).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \sB = (f_1, f_2, f_3) \) is a basis of \( V \).
2. Show that differentiation maps \( V \) into \( V \), and find \( \mtx{D}{\sB}{\sB} \) for \( D \in \cL(V) \), \( D(f) = f' \).
3. Hence show that \( D \) is invertible on \( V \), and use \( (\mtx{D}{\sB}{\sB})^{-1} \) to find a function \( g \in V \) with \( g' = x^2e^x \).
:::

*Hint: for (a), divide a vanishing combination by \( e^x \) and count roots.*
:::

::: {.solution}
(a) \( \sB \) spans \( V \) by definition. Suppose \( af_1 + bf_2 + cf_3 = 0 \), the zero function. Then \( (a + bx + cx^2)e^x = 0 \) for every \( x \in \nR \), and \( e^x \neq 0 \), so the polynomial \( a + bx + cx^2 \) vanishes at every real number. It has infinitely many roots, so it is the zero polynomial by @lem-root-bound, and \( a = b = c = 0 \). Hence \( \sB \) is independent, and a basis of \( V \).

(b) By the product rule,
\[
f_1' = e^x = f_1, \qquad f_2' = e^x + xe^x = f_1 + f_2, \qquad f_3' = 2xe^x + x^2e^x = 2f_2 + f_3 .
\]
Each lies in \( V \), and \( D \) is linear, so \( D \) maps every combination of \( f_1, f_2, f_3 \) into \( V \) (@thm-linear-combination). Reading off coordinates as columns,
\[
\mtx{D}{\sB}{\sB} = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix}.
\]
(c) The matrix is upper triangular with non-zero diagonal entries, and one checks directly that
\[
\begin{pmatrix} 1 & -1 & 2 \\ 0 & 1 & -2 \\ 0 & 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix} = \I_3,
\]
so \( \mtx{D}{\sB}{\sB} \) is invertible with this inverse (@thm-one-sided-inverse). By @thm-rank-map-equals-rank-matrix (b), \( D \) is invertible on \( V \) and \( \mtx{D^{-1}}{\sB}{\sB} = (\mtx{D}{\sB}{\sB})^{-1} \). We want \( g = D^{-1}(f_3) \). Since \( \coord{f_3}{\sB} = (0, 0, 1) \), @thm-matrix-of-map-coordinates gives
\[
\coord{g}{\sB} = \begin{pmatrix} 1 & -1 & 2 \\ 0 & 1 & -2 \\ 0 & 0 & 1 \end{pmatrix}\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 2 \\ -2 \\ 1 \end{pmatrix},
\]
so \( g = 2f_1 - 2f_2 + f_3 = (x^2 - 2x + 2)e^x \). Check: \( g' = (2x - 2)e^x + (x^2 - 2x + 2)e^x = x^2e^x \). No integration by parts was needed.
:::
