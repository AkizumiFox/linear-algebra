# Projections and the Trace of an Operator

Chapter 1 ended its discussion of complements with a promise: a splitting \( V = U \oplus W \) should give a projection of \( V \) onto \( U \) along \( W \), and different complements should give different projections. This section keeps that promise. Projections are the operators that are simplest in a well-chosen basis, and computing their matrices there leads to a second topic: the trace of an operator, a number attached to \( T \in \cL(V) \) that no choice of basis can change. We end with involutions, which split a space into two pieces in the same way.

## Projections

Suppose \( V = U \oplus W \). By @def-direct-sum, every \( \v \in V \) can be written as \( \v = \u + \w \) with \( \u \in U \) and \( \w \in W \) in **exactly one** way. So the rule "\( \v \mapsto \u \)", keep the \( U \)-piece and throw away the \( W \)-piece, is a well-defined function \( V \to V \). In \( \nR^3 = \{\text{the } xy\text{-plane}\} \oplus \{\text{the } z\text{-axis}\} \), it sends \( (a, b, c) \) to \( (a, b, 0) \): the shadow of a point on the floor when light falls straight down.

What property does such a map have that singles it out? Apply it twice. The output \( \u \) already lies in \( U \), and its splitting is \( \u = \u + \0 \), so applying the rule again returns \( \u \). Doing it twice is the same as doing it once. We take this as the definition, because it can be checked without knowing \( U \) and \( W \) in advance.

*A projection is an operator that leaves alone everything it has already produced.*

::: {#def-projection-operator}
[Projection]

Let \( V \) be a vector space over \( F \). An operator \( P \in \cL(V) \) is a **projection** if
\[
P^2 = P,
\]
that is, \( P(P\v) = P\v \) **for every** \( \v \in V \).
:::

In words: \( P^2 \) is the composite \( PP \) (@def-polynomial-of-operator), so the condition says that \( P \) fixes each of its own outputs. Equivalently, \( P\x = \x \) **for every** \( \x \in \im P \): if \( \x = P\v \), then \( P\x = P^2(\v) = P\v = \x \), and conversely this for \( \x = P\v \) is \( P^2(\v) = P\v \). No inner product and no notion of angle is involved. The projections of this section are often called **oblique** projections, to distinguish them from the orthogonal projections met later, in the chapters on inner product spaces.

**Examples.**

- **Onto an axis.** \( P(x, y) = (x, 0) \) on \( F^2 \). Then \( P^2(x, y) = P(x, 0) = (x, 0) \), so \( P^2 = P \).
- **A rank-one projection.** \( T(x, y) = (2x - y,\ 2x - y) \) on \( \nR^2 \) from @exm-projection-adapted-basis. We saw there that its matrix \( A \) satisfies \( A^2 = A \); directly, \( T(2x - y, 2x - y) = (4x - 2y - 2x + y, \dots) = (2x - y, 2x - y) \).
- **Constant term.** On \( F[x]_{\le n} \), \( P(p) = p(0) \), the constant polynomial with value \( p(0) \). The constant polynomial \( c \) has value \( c \) at \( 0 \), so \( P(P(p)) = P(p) \).
- **Degenerate cases.** The identity \( \id_V \) and the zero operator are projections, since \( \id_V^2 = \id_V \) and \( 0^2 = 0 \). They correspond to keeping everything and keeping nothing.

**Non-example by minimal change.** Change the first example to \( T(x, y) = (2x, 0) \) on \( \nR^2 \). Its image is still the \( x \)-axis and its kernel is still the \( y \)-axis. But \( T^2(x, y) = (4x, 0) \ne T(x, y) \) when \( x \ne 0 \): \( T \) does not fix the vectors of its own image, since \( T(1, 0) = (2, 0) \). So having "the right image and kernel" is not enough; the clause \( P^2 = P \) is what forces \( P \) to be the identity on its image. Likewise the reflection \( R(x, y) = (y, x) \) is not a projection: \( R^2 = \id \ne R \).

Here is the promised correspondence. It says that projections and direct sum decompositions are two descriptions of the same thing.

::: {#thm-projection-direct-sum}
[Projections and Direct Sums]

Let \( V \) be a vector space.

::: {.enumerate options="label=(\alph*)"}
1. If \( P \in \cL(V) \) is a projection, then
   \[
   V = \im P \oplus \ker P,
   \]
   \( P \) is the identity on \( \im P \), and \( P \) is zero on \( \ker P \).
2. Conversely, suppose \( V = U \oplus W \). Then there is **exactly one** operator \( P \in \cL(V) \) with \( P\u = \u \) for all \( \u \in U \) and \( P\w = \0 \) for all \( \w \in W \), namely \( P(\u + \w) = \u \). It is a projection, with \( \im P = U \) and \( \ker P = W \). It is called the **projection onto \( U \) along \( W \)**.
:::
:::

::: {.idea}
For (a), every vector splits as "what \( P \) keeps" plus "what \( P \) removes": \( \v = P\v + (\v - P\v) \). The first piece is in the image by definition, and \( P^2 = P \) is exactly what puts the second piece in the kernel. For (b), uniqueness of the splitting makes the rule a function, and uniqueness again makes it linear.
:::

::: {.proof}
(a) Let \( \v \in V \). Then \( \v = P\v + (\v - P\v) \), where \( P\v \in \im P \) and \( P(\v - P\v) = P\v - P^2(\v) = \0 \) because \( P^2 = P \). Hence \( V = \im P + \ker P \). If \( \x \in \im P \cap \ker P \), then \( \x = P\x \), as shown after @def-projection-operator, and \( P\x = \0 \); so \( \x = \0 \). By @thm-direct-sum-criteria, \( V = \im P \oplus \ker P \). We have also seen that \( P \) fixes \( \im P \), and \( P \) is zero on \( \ker P \) by definition.

(b) *Existence.* By @def-direct-sum, each \( \v \in V \) has exactly one splitting \( \v = \u + \w \), so \( P\v \coloneqq \u \) defines a function \( V \to V \). It is linear: if \( \v = \u + \w \) and \( \v' = \u' + \w' \), then \( \v + \v' = (\u + \u') + (\w + \w') \) and \( a\v = a\u + a\w \) are splittings, because \( U \) and \( W \) are subspaces, so by uniqueness \( P(\v + \v') = \u + \u' = P\v + P\v' \) and \( P(a\v) = a\u = aP\v \). For \( \u \in U \) the splitting is \( \u = \u + \0 \), so \( P\u = \u \); for \( \w \in W \) it is \( \w = \0 + \w \), so \( P\w = \0 \).

*Properties.* Every value \( P\v \) lies in \( U \), and every \( \u \in U \) is \( P\u \); so \( \im P = U \). Then \( P(P\v) = P\v \) because \( P \) fixes \( U \); so \( P^2 = P \). Finally \( P(\u + \w) = \u \) is \( \0 \) exactly when \( \u = \0 \), that is, when \( \v = \w \in W \); so \( \ker P = W \).

*Uniqueness.* If \( P' \in \cL(V) \) is identity on \( U \) and zero on \( W \), then \( P'(\u + \w) = P'\u + P'\w = \u \) by linearity, so \( P' = P \).
:::

So a projection **is** a direct sum decomposition \( V = U \oplus W \), recorded as an operator: \( U \) is its image and \( W \) its kernel. Given \( P \), the decomposition is \( \im P \oplus \ker P \); given the decomposition, \( P \) is the projection onto \( U \) along \( W \). The two constructions undo each other, by the "exactly one" in (b).

Now the promise from Chapter 1. There, the \( x \)-axis \( U \) in \( \nR^2 \) had many complements, for instance the \( y \)-axis \( W \) and the line \( W' \) spanned by \( (1, 1) \). Each gives a projection onto the same line \( U \).

\begin{center}
\begin{tikzpicture}[scale=1.25]
  \draw[->, gray] (-2.6, 0) -- (2.8, 0) node[right] {$x$};
  \draw[very thick] (-2.4, 0) -- (2.4, 0);
  \node[above] at (-2.2, 0) {$U$};
  \draw[thick, dashed, black!55] (0, -1.2) -- (0, 2.5) node[above, black] {$W$};
  \draw[thick, dash dot, black!55] (-1.2, -1.2) -- (2.4, 2.4) node[above right, black] {$W'$};
  \fill (1, 2) circle (1.8pt) node[above] {$\v = (1, 2)$};
  \draw[->, thick, dashed] (1, 2) -- (1, 0.06);
  \draw[->, thick, dash dot] (1, 2) -- (-0.96, 0.04);
  \fill (1, 0) circle (1.8pt) node[below right] {$P\v = (1, 0)$};
  \fill (-1, 0) circle (1.8pt) node[below left] {$P'\v = (-1, 0)$};
\end{tikzpicture}
\end{center}

To project \( \v \) onto \( U \) along a complement, slide \( \v \) parallel to that complement until it hits \( U \). Along the \( y \)-axis, \( (1, 2) = (1, 0) + (0, 2) \) gives \( P\v = (1, 0) \) (dashed arrow). Along \( W' \), \( (1, 2) = (-1, 0) + (2, 2) \) gives \( P'\v = (-1, 0) \) (dash-dotted arrow). In general \( P(x, y) = (x, 0) \) and \( P'(x, y) = (x - y, 0) \), with standard matrices \( \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \) and \( \begin{pmatrix} 1 & -1 \\ 0 & 0 \end{pmatrix} \).

::: {.warning}
**"Projection onto \( U \)" is incomplete: the direction "along \( W \)" matters.** The two operators above are both projections, both have image \( U \), and they are different: \( P(1, 2) = (1, 0) \) but \( P'(1, 2) = (-1, 0) \). Since \( U \) has infinitely many complements in \( \nR^2 \), it is the image of infinitely many projections. A projection is determined by its image **and** its kernel together.
:::

In finite dimension, the direct sum \( V = \im P \oplus \ker P \) hands us a basis in which \( P \) is as simple as possible.

::: {#cor-projection-matrix}
[The matrix of a projection]

Let \( V \) be finite-dimensional and \( P \in \cL(V) \) a projection with \( \rank P = r \). Let \( (\u_1, \dots, \u_r) \) be a basis of \( \im P \) and \( (\w_1, \dots, \w_s) \) a basis of \( \ker P \). Then \( \sB = (\u_1, \dots, \u_r, \w_1, \dots, \w_s) \) is a basis of \( V \), and
\[
[P]_{\sB} = \begin{pmatrix} I_r & 0 \\ 0 & 0 \end{pmatrix} = \diag(1, \dots, 1, 0, \dots, 0),
\]
with \( r \) ones.
:::

::: {.proof}
By @thm-projection-direct-sum (a), \( V = \im P \oplus \ker P \), so the concatenated list \( \sB \) is a basis of \( V \) by @thm-direct-sum-k-criteria ((a) ⇒ (d)). Since \( P\u_i = \u_i \) and \( P\w_j = \0 \), the columns of \( [P]_{\sB} \) are \( \e_1, \dots, \e_r \) followed by \( s \) zero columns (@def-matrix-of-linear-map).
:::

Conversely, an operator whose matrix in some basis is \( \diag(1, \dots, 1, 0, \dots, 0) \) is a projection, since that matrix squares to itself. With the change-of-basis square, this gives a way to write down any projection in standard coordinates.

::: {#exm-projection-plane-along-line}
[Projecting onto a plane along a line]

In \( \nR^3 \), let \( U = \{ (x, y, z) : x + y + z = 0 \} \) and \( L = \Span((1, 1, 1)) \), so that \( \nR^3 = U \oplus L \) by @exm-plane-line-direct-sum. Find the standard matrix of the projection \( P \) onto \( U \) along \( L \), and check that it squares to itself.
:::

::: {.solution}
*Direct route.* By @exm-plane-line-direct-sum, \( (a, b, c) \) splits as \( \big(a - m, b - m, c - m\big) + m(1, 1, 1) \) with \( m = \frac{a + b + c}{3} \), and the first piece lies in \( U \). So
\[
P(a, b, c) = \Big(\tfrac{2a - b - c}{3},\ \tfrac{-a + 2b - c}{3},\ \tfrac{-a - b + 2c}{3}\Big), \qquad [P]_{\sE} = \frac13\begin{pmatrix} 2 & -1 & -1 \\ -1 & 2 & -1 \\ -1 & -1 & 2 \end{pmatrix}.
\]
*Adapted basis.* \( (1, -1, 0) \) and \( (0, -1, 1) \) lie in \( U \) and are independent (look at the first and third entries), so they form a basis of the \( 2 \)-dimensional plane \( U \). With \( \sB = ((1, -1, 0), (0, -1, 1), (1, 1, 1)) \), @cor-projection-matrix gives \( [P]_{\sB} = \diag(1, 1, 0) \), and by @thm-change-of-basis-maps \( [P]_{\sE} = M\,\diag(1, 1, 0)\,M^{-1} \) with \( M = \mtx{\id}{\sB}{\sE} \), whose columns are the vectors of \( \sB \). Multiplying out gives the same matrix as the direct route.

*Check.* Let \( A \) be the matrix found. The first column of \( A^2 \) is \( A \) applied to \( \frac13(2, -1, -1) \), which is \( \frac19(4 + 1 + 1,\ -2 - 2 + 1,\ -2 + 1 - 2) = \frac13(2, -1, -1) \), the first column of \( A \); the other columns work the same way by symmetry of the entries. Also \( A(1, 1, 1) = \0 \) and \( A(1, -1, 0) = (1, -1, 0) \), as a projection onto \( U \) along \( L \) must satisfy. The division by \( 3 \) needs \( 3 \ne 0 \) in the field, which holds over \( \nR \).
:::

::: {.check}
Is \( P = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix} \) (acting on \( \nR^2 \)) a projection? If so, onto which line, and along which line?

::: {.solution}
\( P^2 = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix} = P \), so yes. Its image is spanned by its columns, \( \Span((1, 0)) \), the \( x \)-axis. Its kernel is \( \{ x + y = 0 \} = \Span((1, -1)) \). By @thm-projection-direct-sum, it is the projection onto the \( x \)-axis along the line \( y = -x \).
:::
:::

## The trace of an operator

For a projection of rank \( r \), the diagonal matrix of @cor-projection-matrix has trace \( 1 + \dots + 1 = r \cdot 1 \). But traces are defined for matrices, and the same projection has many other matrices, such as the \( 3 \times 3 \) matrix of @exm-projection-plane-along-line, whose trace is \( \frac{2 + 2 + 2}{3} = 2 \). The agreement is no accident. In @thm-trace-similarity-invariant we proved that similar matrices have the same trace, and by @thm-similar-iff-same-operator all matrices of one operator are similar. So the trace belongs to the operator.

*The trace of an operator is the trace of its matrix in any basis; the basis does not matter.*

::: {#def-trace-operator}
[Trace of an operator]

Let \( V \) be a finite-dimensional vector space over \( F \) with \( \dim V \ge 1 \), and let \( T \in \cL(V) \). The **trace** of \( T \) is
\[
\tr T \coloneqq \tr [T]_{\sB},
\]
where \( \sB \) is **any** basis of \( V \). (For \( V = \{\0\} \) we set \( \tr T = 0 \).)
:::

In words: to find \( \tr T \), choose a basis, write down the matrix of \( T \) with that **same** basis on input and output, and add the diagonal entries.

**Well-definedness.** The definition names a basis but claims the answer does not depend on it. Let \( \sB \) and \( \sC \) be bases of \( V \). By @thm-change-of-basis-maps, \( [T]_{\sC} = P^{-1}[T]_{\sB}P \) with \( P = \mtx{\id}{\sC}{\sB} \) invertible, so the two matrices are similar, and by @thm-trace-similarity-invariant they have the same trace. Hence \( \tr T \) depends only on \( T \).

**Examples.**

- **Identity.** In every basis, \( [\id_V]_{\sB} = I_n \), so \( \tr \id_V = n \cdot 1 \), where \( n = \dim V \). Over \( \nR \) this is \( n \); over \( \nF_2 \) it is \( 0 \) when \( n \) is even.
- **Differentiation.** On \( F[x]_{\le n} \) with the basis \( (1, x, \dots, x^n) \), \( D(x^k) = kx^{k-1} \) has no \( x^k \)-component, so every diagonal entry of the matrix is \( 0 \) and \( \tr D = 0 \).
- **A shift of the variable.** On \( \nR[x]_{\le 2} \), let \( T(p) = p(x + 1) \). In \( (1, x, x^2) \), \( T(1) = 1 \), \( T(x) = 1 + x \), \( T(x^2) = 1 + 2x + x^2 \), so the matrix is \( \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix} \) and \( \tr T = 3 \).
- **The reflection.** \( R(x, y) = (y, x) \) has trace \( 0 \), whether computed from \( \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) or from \( \diag(1, -1) \) (@exm-reflection-diagonal-basis).

::: {.warning}
**The trace needs the same basis on both sides.** For an operator \( T \in \cL(V) \), the matrix \( \mtx{T}{\sB}{\sC} \) with \( \sB \ne \sC \) is square, but its trace depends on the bases. For \( \id \) on \( \nR^2 \), with \( \sE \) the standard basis and \( \sC = ((2, 0), (0, 1)) \), we get \( \mtx{\id}{\sE}{\sC} = \diag(\tfrac12, 1) \), of trace \( \tfrac32 \), while \( \tr \id = 2 \). Different bases on input and output give equivalent matrices, not similar ones, and equivalence does not preserve the trace. For the same reason there is no trace of a map \( V \to W \) between different spaces.
:::

The rules for the trace of a matrix carry over at once.

::: {#thm-trace-operator-properties}
[Properties of the Trace of an Operator]

Let \( V \) be finite-dimensional with \( n = \dim V \), let \( S, T \in \cL(V) \) and \( c \in F \). Then
\[
\tr(S + T) = \tr S + \tr T, \qquad \tr(cT) = c\,\tr T, \qquad \tr(ST) = \tr(TS), \qquad \tr \id_V = n \cdot 1 .
\]
:::

::: {.proof}
For \( n = 0 \) all traces are \( 0 \). Otherwise fix a basis \( \sB \) of \( V \). The map \( T \mapsto [T]_{\sB} \) is linear by @thm-linear-maps-isomorphic-to-matrices, so \( [S + T]_{\sB} = [S]_{\sB} + [T]_{\sB} \) and \( [cT]_{\sB} = c[T]_{\sB} \); and \( [ST]_{\sB} = [S]_{\sB}[T]_{\sB} \) by @thm-matrix-of-composition, and likewise for \( TS \). The first three identities now follow from @thm-trace-properties, since \( \tr T \) may be computed in \( \sB \). The last was computed in the examples.
:::

A first consequence: on a finite-dimensional space \( V \) of dimension \( n \ge 1 \) over a field in which \( n \cdot 1 \ne 0 \), such as \( \nR \), there are no operators with \( ST - TS = \id_V \), since the left side has trace \( 0 \) and the right side has trace \( n \cdot 1 \).

Now the trace of a projection. Over \( \nR \) it is simply the rank, but the precise statement is an equation in the field, and reading it as an equation of integers needs a hypothesis.

::: {#thm-rank-equals-trace-projection}
[Trace of a Projection]

Let \( V \) be a finite-dimensional vector space over \( F \) and \( P \in \cL(V) \) a projection. Then
\[
\tr P = (\rank P) \cdot 1 \quad \text{in } F .
\]
If \( F \) has characteristic \( 0 \), or characteristic \( p > \dim V \), then \( \rank P \) is determined by \( \tr P \): it is the unique integer \( r \) with \( 0 \le r \le \dim V \) and \( r \cdot 1 = \tr P \). In particular \( \rank P = \tr P \) for projections on real or complex spaces.
:::

::: {.proof}
Let \( r = \rank P \). If \( V = \{\0\} \), both sides are \( 0 \). Otherwise, by @cor-projection-matrix there is a basis \( \sB \) with \( [P]_{\sB} = \diag(1, \dots, 1, 0, \dots, 0) \) with \( r \) ones, so \( \tr P = r \cdot 1 \) by @def-trace-operator.

For the second statement, let \( n = \dim V \). Since \( 0 \le r \le n \) and \( r \cdot 1 = \tr P \), it remains to show uniqueness. Suppose \( k \cdot 1 = l \cdot 1 \) for integers \( 0 \le l \le k \le n \). By @lem-integer-multiples, \( (k - l) \cdot 1 + l \cdot 1 = k \cdot 1 = l \cdot 1 \), and adding \( -(l \cdot 1) \) to both sides gives \( (k - l) \cdot 1 = 0 \). If \( k - l > 0 \), then by @def-characteristic the characteristic of \( F \) is non-zero and at most \( k - l \le n \), which contradicts the hypothesis. Hence \( k = l \). In \( \nR \) and \( \nC \), \( r \cdot 1 \) is the number \( r \).
:::

The hypothesis cannot be dropped. Over \( \nF_2 \), the identity of \( \nF_2^2 \) is a projection of rank \( 2 \), and its trace is \( 1 + 1 = 0 \), the same as the trace of the zero projection, of rank \( 0 \). The equation \( \tr P = (\rank P) \cdot 1 \) still holds there; what fails is recovering the integer \( \rank P \) from the field element \( \tr P \).

## Involutions and reflections

A projection satisfies \( P^2 = P \). The other simple polynomial relation is \( T^2 = \id_V \): doing \( T \) twice changes nothing. Such an operator is called an **involution**. Examples are the reflection \( R(x, y) = (y, x) \), the transpose \( A \mapsto A\tp \) on \( M_n(F) \), and \( f(x) \mapsto f(-x) \) on functions \( \nR \to \nR \). In Chapter 1 the last two produced direct sums: symmetric plus skew-symmetric matrices (@exm-direct-sum-of-matrix), and even plus odd functions (@exm-even-odd-functions). The next theorem explains both at once. For an involution \( T \), write
\[
E_{+} \coloneqq \{ \v \in V : T\v = \v \}, \qquad E_{-} \coloneqq \{ \v \in V : T\v = -\v \}.
\]
These are subspaces, since \( E_{+} = \ker(T - \id_V) \) and \( E_{-} = \ker(T + \id_V) \) (@thm-prop-kernel).

::: {#thm-involution-decomposition}
[Involutions Split the Space]

Let \( F \) be a field of characteristic not \( 2 \), \( V \) a vector space over \( F \), and \( T \in \cL(V) \) with \( T^2 = \id_V \). Then
\[
V = E_{+} \oplus E_{-},
\]
and the projection onto \( E_{+} \) along \( E_{-} \) is \( \frac12(\id_V + T) \).
:::

::: {.idea}
Copy the even/odd split: \( \v = \frac12(\v + T\v) + \frac12(\v - T\v) \). Applying \( T \) swaps \( \v \) and \( T\v \), so the first piece is fixed and the second changes sign. Both halves of the argument divide by \( 2 \), which is where the characteristic enters.
:::

::: {.proof}
Since the characteristic is not \( 2 \), \( 2 = 1 + 1 \ne 0 \) in \( F \) (@def-characteristic), so \( \frac12 \) exists. Let \( \v \in V \), and put \( \v_{+} = \frac12(\v + T\v) \) and \( \v_{-} = \frac12(\v - T\v) \). Then \( \v = \v_{+} + \v_{-} \), and by linearity and \( T^2 = \id_V \),
\[
T\v_{+} = \tfrac12(T\v + \v) = \v_{+}, \qquad T\v_{-} = \tfrac12(T\v - \v) = -\v_{-} .
\]
So \( \v_{+} \in E_{+} \), \( \v_{-} \in E_{-} \), and \( V = E_{+} + E_{-} \). If \( \v \in E_{+} \cap E_{-} \), then \( \v = T\v = -\v \), so \( 2\v = \0 \) and \( \v = \frac12(2\v) = \0 \). By @thm-direct-sum-criteria, \( V = E_{+} \oplus E_{-} \).

The operator \( \frac12(\id_V + T) \) is linear by @thm-linear-maps-vector-space, sends \( \v \) to \( \v_{+} \), fixes \( E_{+} \) (where \( T\v = \v \)) and kills \( E_{-} \) (where \( T\v = -\v \)). By the uniqueness in @thm-projection-direct-sum (b), it is the projection onto \( E_{+} \) along \( E_{-} \).
:::

For the transpose, \( E_{+} \) is the symmetric and \( E_{-} \) the skew-symmetric matrices; for \( f(x) \mapsto f(-x) \), they are the even and odd functions; for the reflection \( R(x, y) = (y, x) \), they are the mirror line \( y = x \) and the perpendicular line \( y = -x \), and the adapted basis \( ((1, 1), (1, -1)) \) is the one of @exm-reflection-diagonal-basis. In finite dimension, a basis of \( E_{+} \) followed by a basis of \( E_{-} \) gives \( [T]_{\sB} = \diag(1, \dots, 1, -1, \dots, -1) \), and so \( \tr T = (\dim E_{+}) \cdot 1 - (\dim E_{-}) \cdot 1 \). In Chapter 8 the non-zero vectors of \( E_{+} \) and \( E_{-} \) will be called eigenvectors with eigenvalues \( 1 \) and \( -1 \).

::: {.warning}
**In characteristic \( 2 \) an involution need not split the space.** Over \( \nF_2 \), let \( T\x = J\x \) with \( J = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \). Then \( J^2 = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} = I_2 \), since \( 2 = 0 \). But \( -1 = 1 \), so \( E_{-} = E_{+} = \ker(J - I_2) = \Span(\e_1) \), and \( E_{+} + E_{-} = \Span(\e_1) \ne \nF_2^2 \).
:::

## Exercises

### A. Check your understanding

::: {#exr-projections-and-trace-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define a projection \( P \in \cL(V) \), and state the correspondence between projections and direct sum decompositions.
2. True or false: a projection is determined by its image. Justify your answer.
3. True or false: an operator \( T \) on \( \nR^2 \) with \( \im T \) the \( x \)-axis and \( \ker T \) the \( y \)-axis is a projection. Justify your answer.
4. Explain why \( \tr T \) does not depend on the basis used to compute it.
5. True or false: for every field \( F \) and every projection \( P \) on a finite-dimensional space over \( F \), the integer \( \rank P \) can be recovered from \( \tr P \in F \). Justify your answer.
6. Where does the hypothesis "characteristic not \( 2 \)" enter the proof of @thm-involution-decomposition?
:::
:::

::: {.solution}
(a) \( P \) is a projection if \( P^2 = P \) (@def-projection-operator). By @thm-projection-direct-sum, a projection gives \( V = \im P \oplus \ker P \), and each decomposition \( V = U \oplus W \) gives exactly one projection with image \( U \) and kernel \( W \).

(b) False. On \( \nR^2 \), \( P(x, y) = (x, 0) \) and \( P'(x, y) = (x - y, 0) \) are different projections with the same image, the \( x \)-axis. A projection is determined by its image and its kernel together.

(c) False. \( T(x, y) = (2x, 0) \) has this image and kernel, but \( T^2 \ne T \).

(d) Matrices of \( T \) in two bases are similar by @thm-change-of-basis-maps, and similar matrices have equal traces by @thm-trace-similarity-invariant.

(e) False. Over \( \nF_2 \), \( \id \) on \( \nF_2^2 \) has rank \( 2 \) and the zero operator has rank \( 0 \), but both have trace \( 0 \). It is true when the characteristic is \( 0 \) or larger than \( \dim V \) (@thm-rank-equals-trace-projection).

(f) Twice: to define \( \v_{\pm} = \frac12(\v \pm T\v) \), and to pass from \( 2\v = \0 \) to \( \v = \0 \). Both need \( 2 \ne 0 \) in \( F \).
:::

### B. Practice

::: {#exr-projections-and-trace-b1}
[B1: A projection in \( \nR^3 \)]

Let \( U = \{ (x, y, z) \in \nR^3 : x + y - z = 0 \} \) and \( L = \Span((1, 1, 1)) \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \nR^3 = U \oplus L \).
2. Find the standard matrix \( A \) of the projection \( P \) onto \( U \) along \( L \).
3. Verify that \( A^2 = A \), and that \( \tr A = \rank A \).
:::
:::

::: {.solution}
(a) \( U \) is the kernel of \( (x, y, z) \mapsto x + y - z \), which is non-zero; its image is then a non-zero subspace of \( \nR \), hence all of \( \nR \) (@thm-dim-impl-eq), so \( \dim U = 3 - 1 = 2 \) by @thm-rank-nullity. If \( t(1, 1, 1) \in U \), then \( t + t - t = t = 0 \), so \( U \cap L = \{\0\} \). By @thm-direct-sum-criteria, \( \dim(U + L) = 2 + 1 = 3 \), so \( U + L = \nR^3 \) by @thm-dim-impl-eq, and \( \nR^3 = U \oplus L \).

(b) Split \( (a, b, c) = \u + t(1, 1, 1) \) with \( \u = (a - t, b - t, c - t) \in U \): the condition \( (a - t) + (b - t) - (c - t) = 0 \) gives \( t = a + b - c \). So
\[
P(a, b, c) = (-b + c,\ -a + c,\ -a - b + 2c), \qquad A = \begin{pmatrix} 0 & -1 & 1 \\ -1 & 0 & 1 \\ -1 & -1 & 2 \end{pmatrix}.
\]
Check: \( A(1, 1, 1) = \0 \), and for the vectors \( (1, 0, 1), (0, 1, 1) \in U \), \( A(1, 0, 1) = (1, 0, 1) \) and \( A(0, 1, 1) = (0, 1, 1) \).

(c) Row by row,
\[
A^2 = \begin{pmatrix} 0 + 1 - 1 & 0 + 0 - 1 & 0 - 1 + 2 \\ 0 + 0 - 1 & 1 + 0 - 1 & -1 + 0 + 2 \\ 0 + 1 - 2 & 1 + 0 - 2 & -1 - 1 + 4 \end{pmatrix} = \begin{pmatrix} 0 & -1 & 1 \\ -1 & 0 & 1 \\ -1 & -1 & 2 \end{pmatrix} = A .
\]
\( \tr A = 0 + 0 + 2 = 2 \), and \( \rank A = \rank P = \dim U = 2 \) by @thm-projection-direct-sum (b), in agreement with @thm-rank-equals-trace-projection.
:::

::: {#exr-projections-and-trace-b2}
[B2: The complementary projection]

Let \( P \in \cL(V) \) be a projection.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \id_V - P \) is a projection.
2. Prove that \( \im(\id_V - P) = \ker P \) and \( \ker(\id_V - P) = \im P \).
3. Deduce that if \( P \) is the projection onto \( U \) along \( W \), then \( \id_V - P \) is the projection onto \( W \) along \( U \).
:::
:::

::: {.solution}
(a) By @thm-composition-linear (composition distributes over sums of maps), \( (\id_V - P)^2 = \id_V - 2P + P^2 = \id_V - 2P + P = \id_V - P \).

(b) (\( \subseteq \)) \( P((\id_V - P)(\v)) = P\v - P^2(\v) = \0 \), so \( \im(\id_V - P) \subseteq \ker P \). (\( \supseteq \)) If \( P\v = \0 \), then \( \v = (\id_V - P)(\v) \in \im(\id_V - P) \). For the kernel: \( (\id_V - P)(\v) = \0 \) means \( \v = P\v \). Such \( \v \) lies in \( \im P \), and conversely every \( \x \in \im P \) satisfies \( P\x = \x \), as shown after @def-projection-operator. So \( \ker(\id_V - P) = \im P \).

(c) By @thm-projection-direct-sum (b), \( \im P = U \) and \( \ker P = W \). By (a) and (b), \( \id_V - P \) is a projection with image \( W \) and kernel \( U \). By the uniqueness in @thm-projection-direct-sum (b), applied to \( V = W \oplus U \), it is the projection onto \( W \) along \( U \).
:::

::: {#exr-projections-and-trace-b3}
[B3: Traces of operators on matrices]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \tau \colon M_n(F) \to M_n(F) \), \( \tau(A) = A\tp \). Show that \( \tr \tau = n \cdot 1 \).
2. Fix \( B \in M_2(F) \), and let \( L_B \colon M_2(F) \to M_2(F) \), \( L_B(X) = BX \). Show that \( \tr L_B = 2\tr B \).
:::

*Hint: use the basis of matrix units \( E_{ij} \).*
:::

::: {.solution}
(a) Order the basis \( (E_{ij}) \) of \( M_n(F) \) in any way. Since \( \tau(E_{ij}) = E_{ji} \), the coordinate column of \( \tau(E_{ij}) \) has a \( 1 \) in the position of \( E_{ji} \) and \( 0 \) elsewhere. The diagonal entry of the matrix in the column of \( E_{ij} \) is therefore \( 1 \) if \( E_{ji} = E_{ij} \), that is \( i = j \), and \( 0 \) otherwise. There are \( n \) basis vectors \( E_{ii} \), so \( \tr \tau = n \cdot 1 \) by @def-trace-operator. (Consistently with @thm-involution-decomposition over \( \nR \): symmetric matrices have dimension \( \frac{n(n+1)}{2} \), skew-symmetric ones \( \frac{n(n-1)}{2} \), and the difference is \( n \).)

(b) Use the basis \( (E_{11}, E_{12}, E_{21}, E_{22}) \) and write \( B = (b_{ij}) \). The product \( BE_{ij} \) has the \( i \)-th column of \( B \) in column \( j \) and zeros elsewhere, so \( BE_{ij} = b_{1i}E_{1j} + b_{2i}E_{2j} \). The diagonal entry in the column of \( E_{ij} \) is the coefficient of \( E_{ij} \) itself, which is \( b_{ii} \). Adding over the four basis vectors, \( \tr L_B = b_{11} + b_{11} + b_{22} + b_{22} = 2\tr B \).
:::

### C. Going deeper

::: {#exr-projections-and-trace-c1}
[C1: When is a sum of projections a projection?]

Let \( F \) have characteristic not \( 2 \), and let \( P, Q \in \cL(V) \) be projections.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( P + Q \) is a projection if and only if \( PQ = QP = 0 \).
2. Show that (a) fails over \( \nF_2 \).
3. Suppose \( V \) is finite-dimensional over \( \nR \) and \( P + Q \) is a projection. Deduce that \( \rank(P + Q) = \rank P + \rank Q \).
:::

*Hint: for (⇒) in (a), use the relation \( PQ + QP = 0 \) together with \( P^2 = P \).*
:::

::: {.solution}
(a) By @thm-composition-linear, \( (P + Q)^2 = P^2 + PQ + QP + Q^2 = P + Q + PQ + QP \).

(⇐) If \( PQ = QP = 0 \), this is \( P + Q \).

(⇒) If \( (P + Q)^2 = P + Q \), then \( PQ + QP = 0 \). Multiplying on the left by \( P \) and using \( P^2 = P \) gives \( PQ + PQP = 0 \); multiplying on the right by \( P \) gives \( PQP + QP = 0 \). Subtracting, \( PQ - QP = 0 \), so \( PQ = QP \). Then \( 2PQ = PQ + QP = 0 \), and since \( 2 \ne 0 \) in \( F \), \( PQ = 0 \). Hence also \( QP = 0 \).

(b) Over \( \nF_2 \), let \( P = Q = \id_V \) with \( V \ne \{\0\} \). Then \( P + Q = 2\id_V = 0 \), which is a projection, but \( PQ = \id_V \ne 0 \). The step from \( 2PQ = 0 \) to \( PQ = 0 \) is the one that fails.

(c) By @thm-rank-equals-trace-projection over \( \nR \), and @thm-trace-operator-properties,
\[
\rank(P + Q) = \tr(P + Q) = \tr P + \tr Q = \rank P + \rank Q .
\]
:::

::: {#exr-projections-and-trace-c2}
[C2: The trace is the only trace-like functional]

Let \( n \ge 1 \), and let \( \varphi \colon M_n(F) \to F \) be linear with \( \varphi(AB) = \varphi(BA) \) for all \( A, B \in M_n(F) \).

::: {.enumerate options="label=(\alph*)"}
1. Using \( E_{ij}E_{jk} = E_{ik} \) and \( E_{jk}E_{ij} = 0 \) for \( k \ne i \), show that \( \varphi(E_{ik}) = 0 \) whenever \( i \ne k \).
2. Show that \( \varphi(E_{ii}) = \varphi(E_{jj}) \) for all \( i, j \).
3. Deduce that \( \varphi = c\,\tr \) for some \( c \in F \), and conversely that every \( c\,\tr \) has the property.
:::
:::

::: {.solution}
Recall that \( E_{ij}E_{kl} \) is \( E_{il} \) if \( j = k \) and \( 0 \) otherwise, by @def-matrix-multiplication.

(a) Let \( i \ne k \). Then \( E_{ik} = E_{ii}E_{ik} \) and \( E_{ik}E_{ii} = 0 \), because \( k \ne i \). By the hypothesis and linearity, \( \varphi(E_{ik}) = \varphi(E_{ii}E_{ik}) = \varphi(E_{ik}E_{ii}) = \varphi(0) = 0 \).

(b) \( E_{ii} = E_{ij}E_{ji} \) and \( E_{jj} = E_{ji}E_{ij} \). Hence \( \varphi(E_{ii}) = \varphi(E_{ij}E_{ji}) = \varphi(E_{ji}E_{ij}) = \varphi(E_{jj}) \).

(c) Let \( c = \varphi(E_{11}) \). For \( A = (a_{ij}) = \sum_{i,j} a_{ij}E_{ij} \), linearity with (a) and (b) gives
\[
\varphi(A) = \sum_{i,j} a_{ij}\varphi(E_{ij}) = \sum_{i} a_{ii}\varphi(E_{ii}) = c\sum_i a_{ii} = c\,\tr A .
\]
Conversely, \( c\,\tr \) is linear and \( c\,\tr(AB) = c\,\tr(BA) \) by @thm-trace-properties. So the linear functionals with \( \varphi(AB) = \varphi(BA) \) are exactly the multiples of the trace.
:::
