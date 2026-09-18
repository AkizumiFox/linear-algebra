# Linear Maps

Chapter 1 studied vector spaces one at a time, and Chapter 2 studied one kind of question inside \( F^n \): does \( \A\x = \b \) have a solution? This chapter studies the functions **between** vector spaces that respect addition and scaling. This section defines them, collects examples from geometry, matrices, calculus and algebra, and proves the fact that makes them manageable: a linear map is completely determined by what it does to a basis.

## Functions that behave like matrices

Objects come first, then the maps between them that respect their structure. For sets the maps are functions; for groups they are homomorphisms (@def-group-homomorphism). For vector spaces the structure is addition and scalar multiplication, so we want functions that respect those two operations.

The standard example is a matrix. For \( \A \in M_{m \times n}(F) \), the rules of matrix multiplication (@thm-matrix-multiplication-properties) give
\[
\A(\x + \y) = \A\x + \A\y, \qquad \A(c\x) = c(\A\x) \qquad \text{for all } \x, \y \in F^n,\ c \in F .
\]
Now look at three functions that are not given by matrices at all.

- **Differentiation** on polynomials: \( (p + q)' = p' + q' \) and \( (cp)' = cp' \).
- **Trace** on square matrices: \( \tr(\A + \B) = \tr \A + \tr \B \) and \( \tr(c\A) = c\tr \A \) (@thm-trace-properties).
- **Rotation** of the plane about the origin: rotating a parallelogram gives a parallelogram, so the rotation of a sum is the sum of the rotations, and rotating a stretched arrow gives the stretched rotated arrow.

The inputs are polynomials, matrices and arrows, not columns. Yet all three obey exactly the two rules that matrices obey. Whatever we can prove from those two rules alone will hold for all of them at once. So we give the two rules a name.

*A linear map is a function that preserves linear combinations.*

## The definition

::: {#def-linear-transformation}
[Linear Map]

Let \( V \) and \( W \) be vector spaces **over the same field** \( F \). A function \( T \colon V \to W \) is a **linear map** (or **linear transformation**) **over \( F \)** if

::: {.enumerate options="label=(LT\arabic*)"}
1. \( T(\u + \v) = T(\u) + T(\v) \) **for all** \( \u, \v \in V \), and
2. \( T(c\v) = cT(\v) \) **for all** \( c \in F \) and **all** \( \v \in V \).
:::

A linear map \( T \colon V \to V \) from a space to itself is also called a **linear operator** on \( V \). We often write \( T\v \) for \( T(\v) \).
:::

In words: (LT1), **additivity**, says that adding first and then applying \( T \) gives the same result as applying \( T \) first and then adding. The sum on the left is taken in \( V \); the sum on the right is taken in \( W \). (LT2), **homogeneity**, says the same for scaling: the scalar \( c \) can be pulled out of \( T \). Both conditions must hold for **every** choice of vectors and scalars, so one counterexample is enough to show that a function is not linear.

The phrase "over the same field" matters. Scalars from \( F \) act on both sides of (LT2), so both spaces must accept them. We will see below that one function can be linear over \( \nR \) and not linear over \( \nC \). A general linear map is always named \( T \), \( S \) or \( R \) in this book, never \( f \); a specific map may get a letter that recalls what it does, such as \( D \) for differentiation.

## Examples

We check the examples against (LT1) and (LT2), grouped by where they come from.

**Matrices.**

::: {#exm-matrix-transformation}
[Multiplication by a Matrix]

Let \( \A \in M_{m \times n}(F) \). Show that \( T_\A \colon F^n \to F^m \), \( T_\A(\x) = \A\x \), is a linear map.
:::

::: {.solution}
Let \( \x, \y \in F^n \) and \( c \in F \). By the distributive law in @thm-matrix-multiplication-properties, \( T_\A(\x + \y) = \A(\x + \y) = \A\x + \A\y = T_\A(\x) + T_\A(\y) \), which is (LT1). By the scalar rule in the same theorem, \( T_\A(c\x) = \A(c\x) = c(\A\x) = cT_\A(\x) \), which is (LT2). Hence \( T_\A \) is linear.
:::

We will use the name \( T_\A \) for this map throughout the chapter. For \( F = \nR \) and \( n = m = 2 \), the map \( T_\A \) sends the unit square to the parallelogram spanned by \( \A\e_1 \) and \( \A\e_2 \), the columns of \( \A \) (@thm-matrix-times-vector-columns).

::: {.widget src="widgets/linear-map.js" matrix="2,1,0,1" determinant="false"}
::: {.print}
\begin{center}
\begin{tikzpicture}[scale=1.1]
    \draw[->] (-0.5,0) -- (3.5,0) node[right] {$x$};
    \draw[->] (0,-0.5) -- (0,1.8) node[above] {$y$};
    \draw[dashed, gray] (0,0) rectangle (1,1);
    \fill[green!50!black, opacity=0.15] (0,0) -- (2,0) -- (3,1) -- (1,1) -- cycle;
    \draw[green!50!black] (0,0) -- (2,0) -- (3,1) -- (1,1) -- cycle;
    \draw[thick, blue, ->] (0,0) -- (2,0) node[below] {$\A\e_1$};
    \draw[thick, red, ->] (0,0) -- (1,1) node[above left] {$\A\e_2$};
\end{tikzpicture}
\end{center}

The unit square (dashed) and its image under \( \A = \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix} \).
:::
:::

::: {.content-visible when-format="html"}
Drag the tips of the two arrows to change \( \A \).
:::

::: {#exm-coordinate-transformation}
[Maps Given by Formulas in Coordinates]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( T \colon F^3 \to F^2 \), \( T(a_1, a_2, a_3) = (2a_1 + a_3,\ a_2 - a_1) \), is linear.
2. Let \( \sB = (\v_1, \dots, \v_n) \) be a basis of a vector space \( V \) over \( F \). Show that the **coordinate map** \( V \to F^n \), \( \v \mapsto \coord{\v}{\sB} \), is linear.
:::
:::

::: {.solution}
(a) The formula is a matrix product:
\[
\begin{pmatrix} 2 & 0 & 1 \\ -1 & 1 & 0 \end{pmatrix}\begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix} = \begin{pmatrix} 2a_1 + a_3 \\ -a_1 + a_2 \end{pmatrix}.
\]
So \( T = T_\A \) for this \( 2 \times 3 \) matrix \( \A \), and \( T \) is linear by @exm-matrix-transformation. The same argument shows that every map \( F^n \to F^m \) whose output entries are combinations of the input entries, with constant coefficients and no constant terms, is linear.

(b) By @thm-coordinates-linear, \( \coord{\u + \v}{\sB} = \coord{\u}{\sB} + \coord{\v}{\sB} \) and \( \coord{c\v}{\sB} = c\coord{\v}{\sB} \). These are (LT1) and (LT2).
:::

**Geometry.**

::: {#exm-projection}
[Projection onto an Axis]

Show that \( T \colon \nR^2 \to \nR^2 \), \( T(a_1, a_2) = (a_1, 0) \), is linear.

\begin{center}
\begin{tikzpicture}[scale=1.2]
    \draw[->] (-0.5,0) -- (2.5,0) node[right] {$x$};
    \draw[->] (0,-0.5) -- (0,2) node[above] {$y$};
    \draw[thick,->] (0,0) -- (1,1.5) node[above right] {$(a_1,a_2)$};
    \draw[very thick,->] (0,0) -- (1,0) node[below right] {$(a_1,0)$};
    \draw[dashed] (1,1.5) -- (1,0);
\end{tikzpicture}
\end{center}
:::

::: {.solution}
Let \( \u = (a_1, a_2) \), \( \v = (b_1, b_2) \) and \( c \in \nR \). Then
\[
T(\u + \v) = (a_1 + b_1, 0) = (a_1, 0) + (b_1, 0) = T(\u) + T(\v), \qquad T(c\u) = (ca_1, 0) = c(a_1, 0) = cT(\u).
\]
So (LT1) and (LT2) hold. The map drops each point vertically onto the \( x \)-axis, like a shadow cast by light from straight above.
:::

::: {#exm-rotation}
[Rotation of the Plane]

Let \( \theta \in \nR \), and let \( R_\theta \colon \nR^2 \to \nR^2 \) rotate each vector counterclockwise about the origin by the angle \( \theta \). Find a formula for \( R_\theta \), and deduce that it is linear.

\begin{center}
\begin{tikzpicture}[scale=1.2]
    \draw[->] (-0.5,0) -- (2.5,0) node[right] {$x$};
    \draw[->] (0,-0.5) -- (0,2) node[above] {$y$};
    \draw[thick,->] (0,0) -- (1.5,0.5) node[right] {$(a_1,a_2)$};
    \draw[very thick,->] (0,0) -- (0.5,1.5) node[above right] {$R_\theta(a_1,a_2)$};
    \draw[dashed] (0.8,0.27) arc (18.43:71.57:0.84);
    \node at (0.62,0.62) {$\theta$};
\end{tikzpicture}
\end{center}
:::

::: {.solution}
Write \( (a_1, a_2) = (r\cos\varphi, r\sin\varphi) \) in polar coordinates. Rotating adds \( \theta \) to the angle and keeps the length \( r \), so by the addition formulas for sine and cosine,
\[
R_\theta(a_1, a_2) = \bigl(r\cos(\varphi + \theta),\ r\sin(\varphi + \theta)\bigr) = (a_1\cos\theta - a_2\sin\theta,\ a_1\sin\theta + a_2\cos\theta).
\]
This is \( T_\A \) for \( \A = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} \), so \( R_\theta \) is linear by @exm-matrix-transformation.
:::

**Calculus.** For a polynomial \( p = a_0 + a_1x + \dots + a_nx^n \in F[x] \), define its **(formal) derivative** as \( p' = a_1 + 2a_2x + \dots + na_nx^{n-1} \), where \( ka_k \) means \( a_k \) added to itself \( k \) times. Over \( \nR \) this is the derivative of calculus.

::: {#exm-differentiation}
[Differentiation]

Show that \( D \colon F[x] \to F[x] \), \( D(p) = p' \), is linear. Show also that \( D \) maps \( F[x]_{\le n} \) into \( F[x]_{\le n-1} \) for \( n \ge 1 \).
:::

::: {.solution}
Let \( p = \sum_k a_kx^k \) and \( q = \sum_k b_kx^k \), and \( c \in F \). The coefficient of \( x^{k-1} \) in \( D(p + q) \) is \( k(a_k + b_k) = ka_k + kb_k \), which is the coefficient of \( x^{k-1} \) in \( D(p) + D(q) \). The coefficient of \( x^{k-1} \) in \( D(cp) \) is \( k(ca_k) = c(ka_k) \), which is the coefficient in \( cD(p) \). Both steps use only the field axioms. Two polynomials with the same coefficients are equal (@def-polynomial), so (LT1) and (LT2) hold. If \( \deg p \le n \), the highest power in \( p' \) is at most \( x^{n-1} \), so \( D \) restricts to a linear map \( F[x]_{\le n} \to F[x]_{\le n-1} \).
:::

::: {#exm-integration}
[Integration]

Show that \( J \colon \nR[x] \to \nR[x] \), \( J(p)(x) = \int_0^x p(t)\,\dd t \), is linear.
:::

::: {.solution}
On coefficients, \( J \) sends \( a_0 + a_1x + \dots + a_nx^n \) to \( a_0x + \frac{a_1}{2}x^2 + \dots + \frac{a_n}{n + 1}x^{n+1} \), so it does map polynomials to polynomials. By linearity of the integral from calculus,
\[
J(p + q)(x) = \int_0^x \bigl(p(t) + q(t)\bigr)\,\dd t = J(p)(x) + J(q)(x), \qquad J(cp)(x) = \int_0^x cp(t)\,\dd t = cJ(p)(x)
\]
for every \( x \in \nR \). Hence \( J \) is linear. (The coefficient formula divides by \( k + 1 \); over a field such as \( \nF_2 \), where \( 1 + 1 = 0 \), it breaks down.)
:::

**Algebra and sequences.**

::: {#exm-multiplication-by-x}
[Multiplication by \( x \)]

Show that \( M \colon F[x] \to F[x] \), \( M(p) = xp \), is linear.
:::

::: {.solution}
By the distributive laws in @thm-polynomial-ring-laws, \( x(p + q) = xp + xq \), and \( x(cp) = c(xp) \) because the product of polynomials is associative and commutative and the constant \( c \) is a polynomial. These are (LT1) and (LT2).
:::

::: {#exm-trace-matrices}
[Trace and Transpose]

Show that the trace \( \tr \colon M_n(F) \to F \) and the transpose \( M_{m \times n}(F) \to M_{n \times m}(F) \), \( \A \mapsto \A\tp \), are linear.
:::

::: {.solution}
For the trace, @thm-trace-properties (1) says \( \tr(\A + \B) = \tr \A + \tr \B \) and \( \tr(c\A) = c\tr \A \), which are (LT1) and (LT2); the target is \( F \), regarded as a vector space over itself. For the transpose, the \( (i, j) \) entry of \( (\A + \B)\tp \) is \( a_{ji} + b_{ji} \), the \( (i, j) \) entry of \( \A\tp + \B\tp \); and the \( (i, j) \) entry of \( (c\A)\tp \) is \( ca_{ji} \), the \( (i, j) \) entry of \( c\A\tp \).
:::

::: {#exm-shift}
[The Shift Maps on Sequences]

On the space \( F^{\nN} \) of sequences (@exm-vector-spaces), define the **right shift** and the **left shift**
\[
R(s_0, s_1, s_2, \dots) = (0, s_0, s_1, \dots), \qquad L(s_0, s_1, s_2, \dots) = (s_1, s_2, s_3, \dots).
\]
Show that both are linear.
:::

::: {.solution}
The operations on \( F^{\nN} \) are termwise. The entry in position \( k \ge 1 \) of \( R(\mathbf{s} + \mathbf{t}) \) is \( s_{k-1} + t_{k-1} \), which is the entry of \( R(\mathbf{s}) + R(\mathbf{t}) \); in position \( 0 \) both have \( 0 = 0 + 0 \). Similarly, \( R(c\mathbf{s}) \) has entries \( 0 = c \cdot 0 \) and \( cs_{k-1} \), the entries of \( cR(\mathbf{s}) \). For \( L \), the entry in position \( k \) of \( L(\mathbf{s} + \mathbf{t}) \) is \( s_{k+1} + t_{k+1} \), and of \( L(c\mathbf{s}) \) is \( cs_{k+1} \), as required.
:::

The right shift is the map promised in the warning of Chapter 1, §8, on what changes in infinite dimension: it matches \( F^{\nN} \) one-to-one with the sequences whose first entry is \( 0 \), respecting addition and scaling. In the next section we measure exactly how \( R \) and \( L \) fail to be bijective.

::: {#exm-matrix-composition}
[Composition with a Fixed Function]

Let \( X \) and \( Y \) be sets and \( g \colon X \to Y \) a function. Show that \( C_g \colon F^Y \to F^X \), \( C_g(h) = h \circ g \), is linear. Deduce that \( \nR[x] \to \nR[x] \), \( p(x) \mapsto p(x + 1) \), is linear.
:::

::: {.solution}
The operations on function spaces are pointwise (@exm-vector-spaces). For \( t \in X \),
\[
C_g(h + k)(t) = (h + k)(g(t)) = h(g(t)) + k(g(t)) = \bigl(C_g(h) + C_g(k)\bigr)(t),
\]
and \( C_g(ch)(t) = c\,h(g(t)) = \bigl(cC_g(h)\bigr)(t) \). So (LT1) and (LT2) hold. The output is again a function, not a number; linearity is about the function \( h \) varying, while \( g \) stays fixed.

For the second claim, take \( X = Y = \nR \) and \( g(t) = t + 1 \), and regard each real polynomial as a function \( \nR \to \nR \). Then \( p(x + 1) = C_g(p) \), which is again a polynomial of the same degree. The identities \( C_g(p + q) = C_g(p) + C_g(q) \) and \( C_g(cp) = cC_g(p) \) hold as functions, hence as polynomials, because two real polynomials with the same values everywhere are equal (a consequence of @lem-root-bound). So the map is linear. (It translates the graph of \( p \) one unit to the left.)
:::

**The degenerate maps.** Three maps are always available: the identity on any space, the inclusion of any subspace, and the zero map between any two spaces. They look too simple to matter. They matter because every general statement about linear maps must be true for them, so they are the first test of any conjecture.

::: {#exm-identity}
[Identity Map]

The identity \( \id_V \colon V \to V \), \( \v \mapsto \v \), is linear: \( \id_V(\u + \v) = \u + \v = \id_V(\u) + \id_V(\v) \) and \( \id_V(c\v) = c\v = c\,\id_V(\v) \).
:::

::: {#exm-inclusion}
[Inclusion Map]

If \( U \) is a subspace of \( V \), the inclusion \( \iota \colon U \to V \), \( \iota(\u) = \u \), is linear, because the operations of \( U \) are those of \( V \). Its formula is the identity's, but its codomain is bigger. For instance \( \nR[x]_{\le 2} \to \nR[x] \) is an inclusion.
:::

::: {#exm-zero-map}
[Zero Map]

For any \( V \) and \( W \) over \( F \), the zero map \( 0 \colon V \to W \), \( \v \mapsto \0_W \), is linear: \( \0_W = \0_W + \0_W \) and \( \0_W = c\0_W \) (@thm-scalar-zero-vector).
:::

## Three consequences of linearity

The two axioms already force several other rules. The first is the quickest test for non-linearity.

::: {#thm-zero-maps-to-zero}
[Linear Maps Send Zero to Zero]

Let \( T \colon V \to W \) be linear. Then \( T(\0_V) = \0_W \).
:::

::: {.proof}
By (LT1), \( T(\0_V) = T(\0_V + \0_V) = T(\0_V) + T(\0_V) \). Adding \( -T(\0_V) \) to both sides gives \( \0_W = T(\0_V) \).
:::

The proof used only (LT1). Homogeneity with \( c = 0 \) would also give it: \( T(\0_V) = T(0\v) = 0T(\v) = \0_W \).

::: {#thm-preserves-negation}
[Linear Maps Preserve Negatives]

Let \( T \colon V \to W \) be linear. Then \( T(-\v) = -T(\v) \) and \( T(\u - \v) = T(\u) - T(\v) \) for all \( \u, \v \in V \).
:::

::: {.proof}
By @thm-negation-scalar, \( -\v = (-1)\v \). So (LT2) gives \( T(-\v) = (-1)T(\v) = -T(\v) \), using @thm-negation-scalar again in \( W \). Then (LT1) gives \( T(\u - \v) = T(\u + (-\v)) = T(\u) + T(-\v) = T(\u) - T(\v) \).
:::

Checking two conditions separately is often longer than necessary. One combined condition suffices.

::: {#thm-equivalent-condition}
[One-Line Test for Linearity]

Let \( V \) and \( W \) be vector spaces over \( F \), and let \( T \colon V \to W \) be a function. Then \( T \) is linear **if and only if**
\[
T(c\u + \v) = cT(\u) + T(\v) \qquad \text{for all } c \in F \text{ and all } \u, \v \in V .
\]
:::

::: {.proof}
\( (\Rightarrow) \) Suppose \( T \) is linear. By (LT1) and then (LT2), \( T(c\u + \v) = T(c\u) + T(\v) = cT(\u) + T(\v) \).

\( (\Leftarrow) \) Suppose the condition holds. Taking \( c = 1 \) gives \( T(\u + \v) = T(\u) + T(\v) \), which is (LT1). Taking \( \u = \v = \0 \) and \( c = 1 \) gives \( T(\0) = T(\0) + T(\0) \), so \( T(\0) = \0 \). Now taking \( \v = \0 \) gives \( T(c\u) = cT(\u) + T(\0) = cT(\u) \), which is (LT2).
:::

Finally, the slogan. Two applications of the axioms handle a combination of two vectors; induction handles any finite combination.

::: {#thm-linear-combination}
[Linear Maps Preserve Linear Combinations]

Let \( T \colon V \to W \) be linear, let \( \v_1, \dots, \v_k \in V \) and \( a_1, \dots, a_k \in F \), where \( k \ge 0 \). Then
\[
T(a_1\v_1 + \dots + a_k\v_k) = a_1T(\v_1) + \dots + a_kT(\v_k).
\]
:::

::: {.proof}
We use induction on \( k \). For \( k = 0 \) both sides are empty sums, so the claim is \( T(\0) = \0 \), which is @thm-zero-maps-to-zero. Let \( k \ge 1 \) and suppose the claim holds for \( k - 1 \) vectors. By (LT1), then the induction hypothesis and (LT2),
\[
T\Bigl(\sum_{i=1}^{k-1} a_i\v_i + a_k\v_k\Bigr) = T\Bigl(\sum_{i=1}^{k-1} a_i\v_i\Bigr) + T(a_k\v_k) = \sum_{i=1}^{k-1} a_iT(\v_i) + a_kT(\v_k).
\]
This completes the induction.
:::

In words: to apply \( T \) to a combination, apply it to each vector and keep the same coefficients. This is the property the slogan promised, and it is the property every later theorem about linear maps uses.

## Non-examples

A function fails to be linear as soon as **one** instance of (LT1) or (LT2) fails. The cheapest instance to try is \( \0 \), by @thm-zero-maps-to-zero.

::: {#exm-constant-function}
[A Constant Function]

Is \( T \colon \nR \to \nR \), \( T(x) = 5 \), linear?
:::

::: {.solution}
No. A linear map sends \( 0 \) to \( 0 \) by @thm-zero-maps-to-zero, but \( T(0) = 5 \neq 0 \).
:::

::: {#exm-translation}
[Translation]

Let \( \b \in \nR^2 \) be **non-zero**. Is the translation \( T \colon \nR^2 \to \nR^2 \), \( T(\v) = \v + \b \), linear?
:::

::: {.solution}
No: \( T(\0) = \b \neq \0 \), which is impossible for a linear map by @thm-zero-maps-to-zero. This is a minimal change of the identity map (@exm-identity): the formula differs only by the constant \( \b \), and that constant is exactly what breaks linearity. For the record, (LT1) fails too: \( T(\u + \v) = \u + \v + \b \), while \( T(\u) + T(\v) = \u + \v + 2\b \). Maps of the form \( \v \mapsto \A\v + \b \) are called **affine**; they are linear exactly when \( \b = \0 \).
:::

Passing the zero test does not make a function linear.

::: {#exm-squaring}
[Squaring]

Is \( T \colon \nR^2 \to \nR^2 \), \( T(a_1, a_2) = (a_1^2, 0) \), linear?
:::

::: {.solution}
No. Here \( T(\0) = \0 \), so the quick test says nothing. But (LT2) fails for \( \v = (1, 0) \) and \( c = 2 \): \( T(2\v) = T(2, 0) = (4, 0) \), while \( 2T(\v) = 2(1, 0) = (2, 0) \). Compare with the projection \( (a_1, a_2) \mapsto (a_1, 0) \) of @exm-projection: squaring the first entry is the one change, and it destroys homogeneity.
:::

::: {#exm-norm}
[Length]

Is \( T \colon \nR^2 \to \nR \), \( T(x, y) = \sqrt{x^2 + y^2} \), linear?
:::

::: {.solution}
No. Take \( \v = (1, 0) \) and \( c = -1 \). Then \( T(-\v) = 1 \), but \( -T(\v) = -1 \), so (LT2) fails. Length does satisfy \( T(c\v) = \lvert c \rvert T(\v) \), which agrees with \( cT(\v) \) only for \( c \ge 0 \). Additivity fails too: \( T((1, 0) + (0, 1)) = \sqrt{2} \), but \( T(1, 0) + T(0, 1) = 2 \).
:::

The last non-example shows that linearity depends on the field, not only on the function.

::: {#exm-complex-conjugation}
[Complex Conjugation: the Field Matters]

Let \( T \colon \nC \to \nC \), \( T(z) = \conj{z} \). Is \( T \) linear when \( \nC \) is regarded as a vector space **over \( \nC \)**? Over \( \nR \)?
:::

::: {.solution}
(LT1) holds in both cases, since \( \conj{z + w} = \conj{z} + \conj{w} \) (@thm-conjugate-properties).

**Over \( \nC \): not linear.** The scalars are all complex numbers. Take \( c = i \) and \( z = 1 \): then \( T(i \cdot 1) = \conj{i} = -i \), but \( iT(1) = i \cdot 1 = i \). So (LT2) fails.

**Over \( \nR \): linear.** Now (LT2) is only required for real \( c \). For \( c \in \nR \), \( T(cz) = \conj{c}\,\conj{z} = c\,\conj{z} = cT(z) \), by @thm-conjugate-properties and \( \conj{c} = c \).
:::

::: {.warning}
**"Linear" here is not the "linear function" of school.** A function \( f(x) = mx + b \) has a straight-line graph, but it is a linear map \( \nR \to \nR \) only when \( b = 0 \): \( f(0) = b \), and @thm-zero-maps-to-zero demands \( f(0) = 0 \). In fact every linear map \( T \colon \nR \to \nR \) has the form \( T(x) = mx \): by (LT2), \( T(x) = T(x \cdot 1) = xT(1) \), so \( m = T(1) \). And \( T(\0) = \0 \) is **necessary but not sufficient** for linearity, as @exm-squaring shows.
:::

::: {.check}
Which of these maps \( \nR^2 \to \nR^2 \) are linear? (i) \( (x, y) \mapsto (y, x) \); (ii) \( (x, y) \mapsto (x + y, 1) \); (iii) \( (x, y) \mapsto (xy, 0) \).
:::

::: {.solution}
(i) Linear: it is \( T_\A \) with \( \A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \). (ii) Not linear: \( (0, 0) \mapsto (0, 1) \neq \0 \). (iii) Not linear, although \( \0 \mapsto \0 \): \( (2, 2) \mapsto (4, 0) \), but \( 2 \cdot T(1, 1) = 2(1, 0) = (2, 0) \), so (LT2) fails.
:::

**Why this definition.** Could one condition be dropped? Complex conjugation on \( \nC \) over \( \nC \) satisfies (LT1) but not (LT2), so additivity alone is not enough. (Over \( \nQ \), surprisingly, additivity does imply homogeneity; see @exr-linear-maps-c1.) Conversely, \( T \colon \nR^2 \to \nR \), \( T(x, y) = \sqrt[3]{x^3 + y^3} \) (the real cube root), satisfies (LT2), since \( \sqrt[3]{c^3x^3 + c^3y^3} = c\sqrt[3]{x^3 + y^3} \) for every real \( c \). But \( T(1, 0) + T(0, 1) = 2 \), while \( T(1, 1) = \sqrt[3]{2} \), so (LT1) fails. Neither condition implies the other, and we need both to get @thm-linear-combination. The name comes from the case \( \nR \to \nR \) just described: the graph of a linear map is a line through the origin.

## A linear map is determined by a basis

A function on an infinite set normally needs infinitely many values to describe it. A linear map needs far fewer. If \( \sB = (\v_1, \dots, \v_n) \) is a basis of \( V \), every \( \v \in V \) is a combination \( a_1\v_1 + \dots + a_n\v_n \), and @thm-linear-combination forces
\[
T(\v) = a_1T(\v_1) + \dots + a_nT(\v_n).
\]
So the \( n \) vectors \( T(\v_1), \dots, T(\v_n) \) already fix every value of \( T \). The converse question is whether **any** choice of these \( n \) vectors comes from a linear map. It does, and that is the theorem.

::: {#thm-linear-transform-basis}
[Linear Maps Are Determined by a Basis]

Let \( V \) and \( W \) be vector spaces over \( F \), let \( \sB = (\v_1, \dots, \v_n) \) be a basis of \( V \), and let \( \w_1, \dots, \w_n \in W \) be **any** vectors. Then there **exists exactly one** linear map \( T \colon V \to W \) such that
\[
T(\v_i) = \w_i \qquad \text{for } i = 1, \dots, n .
\]
It is given by \( T(a_1\v_1 + \dots + a_n\v_n) = a_1\w_1 + \dots + a_n\w_n \) for all \( a_1, \dots, a_n \in F \).
:::

::: {.idea}
**Uniqueness** is the computation above: any linear \( T \) with these values must be given by the formula. **Existence** asks us to *use* the formula as a definition. The only danger is that a vector might have two expressions \( \sum a_i\v_i \), giving two candidate values; the basis rules that out, because coordinates are unique. So: ① define \( T(\v) \) from the coordinates of \( \v \); ② check (LT1), (LT2), using that coordinates respect the operations; ③ check \( T(\v_i) = \w_i \); ④ prove uniqueness by @thm-linear-combination.
:::

::: {.proof}
*Existence.* Let \( \v \in V \). By @thm-unique-representation, there are **unique** scalars \( a_1, \dots, a_n \in F \) with \( \v = a_1\v_1 + \dots + a_n\v_n \); they are the entries of \( \coord{\v}{\sB} \) (@def-coordinates). Define
\[
T(\v) \coloneqq a_1\w_1 + \dots + a_n\w_n .
\]
Since the scalars are unique, this assigns exactly one vector of \( W \) to each \( \v \in V \), so \( T \colon V \to W \) is a well-defined function.

Let \( \u, \v \in V \) and \( c \in F \), with \( \coord{\u}{\sB} = (b_1, \dots, b_n) \) and \( \coord{\v}{\sB} = (a_1, \dots, a_n) \). By @thm-coordinates-linear, \( \coord{c\u + \v}{\sB} = c\coord{\u}{\sB} + \coord{\v}{\sB} = (cb_1 + a_1, \dots, cb_n + a_n) \). Hence, by the definition of \( T \) and the vector space axioms in \( W \),
\[
T(c\u + \v) = \sum_{i=1}^n (cb_i + a_i)\w_i = c\sum_{i=1}^n b_i\w_i + \sum_{i=1}^n a_i\w_i = cT(\u) + T(\v).
\]
By @thm-equivalent-condition, \( T \) is linear. Moreover, \( \v_i = 0\v_1 + \dots + 1\v_i + \dots + 0\v_n \), so \( \coord{\v_i}{\sB} = \e_i \) and \( T(\v_i) = \w_i \).

*Uniqueness.* Let \( S \colon V \to W \) be any linear map with \( S(\v_i) = \w_i \) for all \( i \). For \( \v = a_1\v_1 + \dots + a_n\v_n \in V \), @thm-linear-combination gives
\[
S(\v) = a_1S(\v_1) + \dots + a_nS(\v_n) = a_1\w_1 + \dots + a_n\w_n = T(\v).
\]
Since \( S(\v) = T(\v) \) for every \( \v \in V \), the functions are equal: \( S = T \). This proves the theorem.
:::

The theorem has two halves, and they are used differently. Uniqueness says that **to check two linear maps are equal, check them on a basis**. Existence says that **to build a linear map, choose the images of a basis freely**. The same holds for the infinite bases of Chapter 1, §8, because every vector is still a unique **finite** combination of basis vectors; we record this as @thm-linear-map-from-any-basis below. Later in this chapter this theorem turns into the matrix of a linear map: once bases are fixed, the \( n \) vectors \( T(\v_i) \), written in coordinates, are the columns.

::: {#thm-linear-map-from-any-basis}
[Linear Maps on an Arbitrary Basis]

Let \( V \) and \( W \) be vector spaces over \( F \), let \( B \) be a basis of \( V \) (possibly infinite, in the sense of @thm-basis-extension-general), and for each \( \b \in B \) let \( \w_{\b} \in W \) be any vector. Then there is exactly one linear map \( T \colon V \to W \) with \( T\b = \w_{\b} \) for every \( \b \in B \).
:::

::: {.proof}
Let \( \v \in V \). Since \( B \) spans \( V \) and is independent, \( \v \) is a finite combination \( \v = \sum_{\b \in B} a_{\b}\b \) in which only finitely many \( a_{\b} \) are non-zero, and these coefficients are unique: two such expressions differ by a finite combination of distinct elements of \( B \) equal to \( \0 \), whose coefficients all vanish by independence. Define \( T\v = \sum_{\b \in B} a_{\b}\w_{\b} \), a finite sum. The coefficients of \( \v + \u \) and of \( c\v \) are \( a_{\b} + a'_{\b} \) and \( ca_{\b} \) by uniqueness, so \( T \) is linear, and \( T\b = \w_{\b} \) because the coefficients of \( \b \) are \( 1 \) at \( \b \) and \( 0 \) elsewhere. If \( S \) is another linear map with \( S\b = \w_{\b} \) for all \( \b \), then \( S\v = \sum a_{\b} S\b = T\v \) by @thm-linear-combination. This proves the theorem.
:::

::: {#exm-map-from-basis-values}
[Finding a Formula from Values on a Basis]

Show that there is exactly one linear map \( T \colon \nR^2 \to \nR^3 \) with
\[
T(1, 1) = (1, 2, 0), \qquad T(1, -1) = (3, 0, 2),
\]
and find \( T(x, y) \).
:::

::: {.solution}
First, \( ((1, 1), (1, -1)) \) is a basis of \( \nR^2 \). The matrix with these columns is \( \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \), and \( ad - bc = 1 \cdot (-1) - 1 \cdot 1 = -2 \neq 0 \). So the matrix is invertible (@thm-two-by-two-inverse), and its columns form a basis of \( \nR^2 \) (@thm-invertible-tfae). By @thm-linear-transform-basis, exactly one such \( T \) exists.

To find it, write \( (x, y) \) in the basis. Solving \( a(1, 1) + b(1, -1) = (x, y) \), that is \( a + b = x \) and \( a - b = y \), gives \( a = \frac{x + y}{2} \) and \( b = \frac{x - y}{2} \). By the formula in the theorem,
\[
T(x, y) = \frac{x + y}{2}(1, 2, 0) + \frac{x - y}{2}(3, 0, 2) = (2x - y,\ x + y,\ x - y).
\]
Check: \( T(1, 1) = (1, 2, 0) \) and \( T(1, -1) = (3, 0, 2) \).
:::

::: {#exm-deter}
[Too Many Conditions]

Is there a linear map \( T \colon \nR^2 \to \nR^3 \) with
\[
T(1, 0) = (2, 3, 4), \qquad T(1, 1) = (3, 4, 5), \qquad T(2, 3) = (4, 5, 6)?
\]
:::

::: {.solution}
No. The matrix \( \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) with columns \( (1, 0) \) and \( (1, 1) \) has \( ad - bc = 1 \cdot 1 - 1 \cdot 0 = 1 \neq 0 \), so as in @exm-map-from-basis-values these two vectors form a basis of \( \nR^2 \). By @thm-linear-transform-basis, the first two conditions already determine \( T \), and the third condition must be checked against them, not imposed. Since \( (2, 3) = -1 \cdot (1, 0) + 3 \cdot (1, 1) \), any linear \( T \) with the first two values satisfies
\[
T(2, 3) = -T(1, 0) + 3T(1, 1) = -(2, 3, 4) + 3(3, 4, 5) = (7, 9, 11)
\]
by @thm-linear-combination. As \( (7, 9, 11) \neq (4, 5, 6) \), no such \( T \) exists. Had the third value been \( (7, 9, 11) \), the answer would be yes, with exactly one such map.
:::

::: {#exm-deter-two}
[Recognizing Differentiation]

Show that the differentiation map \( D \colon \nR[x]_{\le 3} \to \nR[x]_{\le 2} \) is the **only** linear map \( T \colon \nR[x]_{\le 3} \to \nR[x]_{\le 2} \) with
\[
T(1) = 0, \qquad T(x) = 1, \qquad T(x^2) = 2x, \qquad T(x^3) = 3x^2 .
\]
:::

::: {.solution}
The list \( (1, x, x^2, x^3) \) is a basis of \( \nR[x]_{\le 3} \) (@exm-standard-bases). The map \( D \) is linear (@exm-differentiation), and \( D(1) = 0 \), \( D(x) = 1 \), \( D(x^2) = 2x \), \( D(x^3) = 3x^2 \), so \( D \) has the four prescribed values. By the uniqueness half of @thm-linear-transform-basis, every linear \( T \) with these values equals \( D \). Four values, the derivatives of the monomials, pin down the derivative of every cubic.
:::

::: {.warning}
**The values must be prescribed on a basis, or at least on an independent list.** On a dependent list, the values may contradict each other. There is **no** linear \( T \colon \nR^2 \to \nR^2 \) with \( T(1, 0) = (1, 0) \) and \( T(2, 0) = (0, 1) \): since \( (2, 0) = 2(1, 0) \), (LT2) forces \( T(2, 0) = 2T(1, 0) = (2, 0) \neq (0, 1) \). On the other hand, a list that does not span leaves \( T \) undetermined: many linear maps satisfy \( T(1, 0) = (1, 0) \) alone.
:::

::: {.check}
Let \( T \colon \nR^2 \to \nR \) be linear with \( T(1, 2) = 3 \) and \( T(2, 5) = 1 \). Find \( T(x, y) \).
:::

::: {.solution}
Here \( ad - bc = 1 \cdot 5 - 2 \cdot 2 = 1 \neq 0 \), so \( ((1, 2), (2, 5)) \) is a basis. Solving \( a(1, 2) + b(2, 5) = (x, y) \), that is \( a + 2b = x \) and \( 2a + 5b = y \), gives \( b = y - 2x \) and \( a = 5x - 2y \). Hence \( T(x, y) = 3(5x - 2y) + 1 \cdot (y - 2x) = 13x - 5y \). Check: \( 13 - 10 = 3 \) and \( 26 - 25 = 1 \).
:::

We now have a supply of linear maps and a way to build new ones from a basis. The next section attaches to every linear map two subspaces that measure how far it is from being injective and from being surjective.

## Exercises

### A. Check your understanding

::: {#exr-linear-maps-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define a linear map \( T \colon V \to W \) over \( F \).
2. State the theorem that says a linear map is determined by a basis, including both existence and uniqueness.
3. True or false: if \( T \colon V \to W \) satisfies \( T(\0) = \0 \), then \( T \) is linear. Justify your answer.
4. True or false: there is a linear map \( T \colon \nR^2 \to \nR^2 \) with \( T(1, 1) = (1, 0) \) and \( T(2, 2) = (3, 0) \). Justify your answer.
5. True or false: complex conjugation \( \nC \to \nC \) is linear over \( \nR \). Justify your answer.
:::
:::

::: {.solution}
(a) See @def-linear-transformation: \( V, W \) are vector spaces over the same field \( F \), and \( T(\u + \v) = T(\u) + T(\v) \) and \( T(c\v) = cT(\v) \) for all \( \u, \v \in V \) and \( c \in F \).

(b) See @thm-linear-transform-basis: if \( (\v_1, \dots, \v_n) \) is a basis of \( V \) and \( \w_1, \dots, \w_n \in W \) are arbitrary, there is one and only one linear \( T \colon V \to W \) with \( T(\v_i) = \w_i \) for all \( i \).

(c) False. \( T \colon \nR^2 \to \nR^2 \), \( T(a_1, a_2) = (a_1^2, 0) \), sends \( \0 \) to \( \0 \) but is not linear (@exm-squaring).

(d) False. By (LT2), \( T(2, 2) = 2T(1, 1) = (2, 0) \neq (3, 0) \).

(e) True. See @exm-complex-conjugation: for real \( c \), \( \conj{cz} = c\conj{z} \), and \( \conj{z + w} = \conj{z} + \conj{w} \).
:::

### B. Practice

::: {#exr-linear-maps-b1}
[B1: Which Maps Are Linear?]

Determine which of the following functions are linear maps over \( \nR \). Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( T \colon \nR^3 \to \nR^2 \), \( T(x, y, z) = (x - 2z,\ 3y) \).
2. \( T \colon \nR^2 \to \nR^2 \), \( T(x, y) = (x + 1,\ y) \).
3. \( T \colon M_2(\nR) \to \nR \), \( T\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc \).
4. \( T \colon \nR[x]_{\le 2} \to \nR[x]_{\le 3} \), \( T(p) = x^2p' \).
5. \( T \colon \nR^2 \to \nR \), \( T(x, y) = xy \).
6. \( T \colon \nR^{\nN} \to \nR^{\nN} \), \( T(s_0, s_1, s_2, \dots) = (s_1 - s_0,\ s_2 - s_1,\ s_3 - s_2,\ \dots) \).
:::
:::

::: {.solution}
(a) Linear. \( T = T_\A \) with \( \A = \begin{pmatrix} 1 & 0 & -2 \\ 0 & 3 & 0 \end{pmatrix} \), which is linear by @exm-matrix-transformation.

(b) Not linear. \( T(0, 0) = (1, 0) \neq \0 \), contradicting @thm-zero-maps-to-zero.

(c) Not linear. Take \( \I_2 \) and \( c = 2 \): \( T(2\I_2) = 2 \cdot 2 - 0 = 4 \), but \( 2T(\I_2) = 2 \cdot 1 = 2 \). So (LT2) fails. (Additivity fails too: \( T(\E_{11}) + T(\E_{22}) = 0 + 0 = 0 \), but \( T(\E_{11} + \E_{22}) = T(\I_2) = 1 \).)

(d) Linear. For \( p \in \nR[x]_{\le 2} \), \( p' \) has degree at most \( 1 \), so \( x^2p' \in \nR[x]_{\le 3} \). For \( p, q \) and \( c \in \nR \), by @exm-differentiation and the distributive law, \( T(cp + q) = x^2(cp' + q') = c\,x^2p' + x^2q' = cT(p) + T(q) \). By @thm-equivalent-condition, \( T \) is linear.

(e) Not linear, although \( T(0, 0) = 0 \). \( T(2(1, 1)) = T(2, 2) = 4 \), but \( 2T(1, 1) = 2 \).

(f) Linear. The entry in position \( k \) of \( T(c\mathbf{s} + \mathbf{t}) \) is \( (cs_{k+1} + t_{k+1}) - (cs_k + t_k) = c(s_{k+1} - s_k) + (t_{k+1} - t_k) \), which is the entry in position \( k \) of \( cT(\mathbf{s}) + T(\mathbf{t}) \). By @thm-equivalent-condition, \( T \) is linear.
:::

::: {#exr-linear-maps-b2}
[B2: A Formula from Values on a Basis]

::: {.enumerate options="label=(\alph*)"}
1. Show that there is exactly one linear map \( T \colon \nR^2 \to \nR^2 \) with \( T(2, 1) = (1, 4) \) and \( T(1, 1) = (0, 3) \). Hence find \( T(x, y) \) and a matrix \( \A \) with \( T = T_\A \).
2. Let \( S \colon \nR[x]_{\le 2} \to \nR \) be linear with \( S(1) = 1 \), \( S(1 + x) = 3 \) and \( S(1 + x + x^2) = 6 \). Find \( S(a + bx + cx^2) \).
:::
:::

::: {.solution}
(a) The matrix with columns \( (2, 1) \) and \( (1, 1) \) has \( ad - bc = 2 \cdot 1 - 1 \cdot 1 = 1 \neq 0 \), so it is invertible (@thm-two-by-two-inverse) and its columns form a basis of \( \nR^2 \) (@thm-invertible-tfae). By @thm-linear-transform-basis, exactly one such \( T \) exists. Solving \( a(2, 1) + b(1, 1) = (x, y) \), that is \( 2a + b = x \) and \( a + b = y \), gives \( a = x - y \) and \( b = 2y - x \). Hence
\[
T(x, y) = (x - y)(1, 4) + (2y - x)(0, 3) = (x - y,\ x + 2y).
\]
Check: \( T(2, 1) = (1, 4) \) and \( T(1, 1) = (0, 3) \). Hence \( T = T_\A \) with \( \A = \begin{pmatrix} 1 & -1 \\ 1 & 2 \end{pmatrix} \).

(b) The polynomials \( 1, 1 + x, 1 + x + x^2 \) are non-zero of distinct degrees, so they are independent (@thm-distinct-degrees-independent); there are \( 3 = \dim \nR[x]_{\le 2} \) of them, so they form a basis (@thm-right-size-basis). By (LT1) and @thm-preserves-negation, \( S(x) = S(1 + x) - S(1) = 2 \) and \( S(x^2) = S(1 + x + x^2) - S(1 + x) = 3 \). By @thm-linear-combination,
\[
S(a + bx + cx^2) = aS(1) + bS(x) + cS(x^2) = a + 2b + 3c .
\]
:::

::: {#exr-linear-maps-b3}
[B3: Evaluation and Integration]

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \varphi \colon \nR[x] \to \nR \), \( \varphi(p) = p(3) \), is linear.
2. Prove that \( \psi \colon \nR[x] \to \nR \), \( \psi(p) = \int_0^1 p(t)\,\dd t \), is linear.
3. Hence find \( \varphi(a + bx + cx^2) \) and \( \psi(a + bx + cx^2) \).
:::
:::

::: {.solution}
(a) Let \( p, q \in \nR[x] \) and \( c \in \nR \). By @thm-evaluation-respects-operations, \( (cp + q)(3) = c\,p(3) + q(3) \), where \( cp \) is the product of the constant polynomial \( c \) with \( p \), whose value at \( 3 \) is \( c\,p(3) \). So \( \varphi(cp + q) = c\varphi(p) + \varphi(q) \), and \( \varphi \) is linear by @thm-equivalent-condition.

(b) By linearity of the integral, \( \int_0^1 (cp(t) + q(t))\,\dd t = c\int_0^1 p(t)\,\dd t + \int_0^1 q(t)\,\dd t \). So \( \psi(cp + q) = c\psi(p) + \psi(q) \), and \( \psi \) is linear by @thm-equivalent-condition.

(c) On the basis: \( \varphi(1) = 1 \), \( \varphi(x) = 3 \), \( \varphi(x^2) = 9 \), and \( \psi(1) = 1 \), \( \psi(x) = \frac12 \), \( \psi(x^2) = \frac13 \). By @thm-linear-combination,
\[
\varphi(a + bx + cx^2) = a + 3b + 9c, \qquad \psi(a + bx + cx^2) = a + \tfrac12 b + \tfrac13 c .
\]
:::

### C. Going deeper

::: {#exr-linear-maps-c1}
[C1: Over \( \nQ \), Additivity Is Enough]

Let \( V \) and \( W \) be vector spaces over \( \nQ \), and let \( T \colon V \to W \) be **additive**: \( T(\u + \v) = T(\u) + T(\v) \) for all \( \u, \v \in V \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( T(n\v) = nT(\v) \) for every \( n \in \nN \) and \( \v \in V \).
2. Prove that \( T(n\v) = nT(\v) \) for every \( n \in \nZ \).
3. Prove that \( T(q\v) = qT(\v) \) for every \( q \in \nQ \). Deduce that \( T \) is linear.
:::

*Hint: for (c), apply (b) to the vector \( q\v \).*
:::

::: {.solution}
(a) We use induction on \( n \). For \( n = 0 \): the proof of @thm-zero-maps-to-zero used only additivity, so \( T(\0) = \0 \), that is, \( T(0\v) = 0T(\v) \). If \( T(n\v) = nT(\v) \), then by additivity \( T((n + 1)\v) = T(n\v + \v) = T(n\v) + T(\v) = nT(\v) + T(\v) = (n + 1)T(\v) \).

(b) Let \( n \in \nN \). By additivity and \( T(\0) = \0 \), \( \0 = T(n\v + (-n)\v) = T(n\v) + T((-n)\v) \), so \( T((-n)\v) = -T(n\v) = -nT(\v) = (-n)T(\v) \), using (a). Every integer is \( n \) or \( -n \) for some \( n \in \nN \).

(c) Let \( q = m/n \) with \( m \in \nZ \) and \( n \ge 1 \). By (b) applied to the vector \( q\v \), and then to \( \v \),
\[
nT(q\v) = T(nq\v) = T(m\v) = mT(\v).
\]
Multiplying by \( \frac1n \in \nQ \) gives \( T(q\v) = \frac{m}{n}T(\v) = qT(\v) \). So (LT2) holds for every scalar \( q \in \nQ \), and with additivity, which is (LT1), \( T \) is linear.
:::

::: {#exr-linear-maps-c2}
[C2: Over \( \nC \), Additivity Is Not Enough]

::: {.enumerate options="label=(\alph*)"}
1. Give an additive map \( \nC \to \nC \) that is **not** linear over \( \nC \), and explain which step of @exr-linear-maps-c1 fails for it.
2. Let \( V \) and \( W \) be vector spaces over \( \nC \). Regarding them also as spaces over \( \nR \), let \( T \colon V \to W \) be linear **over \( \nR \)**, and suppose \( T(i\v) = iT(\v) \) for all \( \v \in V \). Prove that \( T \) is linear over \( \nC \).
:::
:::

::: {.solution}
(a) Complex conjugation \( T(z) = \conj{z} \) is additive and not \( \nC \)-linear (@exm-complex-conjugation). The argument of @exr-linear-maps-c1 still shows \( T(q z) = qT(z) \) for rational \( q \), and that is true for conjugation. What fails is that the rational numbers are not all the scalars: nothing in that argument reaches a scalar like \( i \), which is not built from \( 1 \) by adding, subtracting, multiplying and dividing.

(b) (LT1) holds because \( T \) is linear over \( \nR \). For (LT2), let \( c = a + bi \in \nC \) with \( a, b \in \nR \), and \( \v \in V \). By the vector space axioms, \( c\v = a\v + b(i\v) \). Using (LT1), then \( \nR \)-homogeneity, then the hypothesis,
\[
T(c\v) = T(a\v) + T(b(i\v)) = aT(\v) + bT(i\v) = aT(\v) + b\,iT(\v) = (a + bi)T(\v) = cT(\v).
\]
Hence \( T \) is linear over \( \nC \).
:::
