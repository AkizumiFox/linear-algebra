# Eigenvalues and Eigenvectors

The previous section ended with an observation: an operator has a diagonal matrix exactly when the space splits into invariant lines, and a line \( \Span(\v) \) is invariant exactly when \( T\v \) is a multiple of \( \v \). This section turns that observation into the central notion of the chapter. We name the vectors that an operator only stretches, and the stretching factors. We find the factors as roots of the characteristic polynomial of Chapter 6, and we prove the two facts that everything later rests on: eigenvectors for different factors are independent, and over \( \nC \) every operator has at least one eigenvector.

## When is a matrix diagonal?

Chapter 3 asked how simple \( [T]_{\sB} \) can be made by choosing \( \sB \). The simplest square matrices are the diagonal ones, so start with the wish and unwind it.

Let \( V \) be finite-dimensional with basis \( \sB = (\v_1, \dots, \v_n) \), and \( T \in \cL(V) \). By @def-matrix-of-linear-map, column \( j \) of \( [T]_{\sB} \) holds the coordinates of \( T\v_j \). The matrix is \( \diag(\lambda_1, \dots, \lambda_n) \) exactly when column \( j \) is \( \lambda_j\e_j \) for each \( j \), that is,
\[
T\v_j = \lambda_j\v_j \qquad (j = 1, \dots, n).
\]
So the wish forces an equation: every basis vector must be sent to a multiple of itself. We met this in Chapter 3, where the reflection \( R(x, y) = (y, x) \) became \( \diag(1, -1) \) in the basis \( ((1, 1), (1, -1)) \) (@exm-reflection-diagonal-basis), precisely because \( R(1, 1) = (1, 1) \) and \( R(1, -1) = -(1, -1) \).

Where should we look for vectors with \( T\v = \lambda\v \)? Rewrite \( \lambda\v \) as \( \lambda\,\id_V(\v) \). Then the equation says \( (T - \lambda\,\id_V)\v = \0 \): the vector lies in a **kernel**. Kernels are subspaces we know how to compute, so this rewriting is a plan, not just a restatement.

*An eigenvector of \( T \) is a non-zero vector that \( T \) only stretches, and the eigenvalue is the stretching factor.*

::: {#def-eigenvalue}
[Eigenvalue and Eigenvector]

Let \( V \) be a vector space over \( F \) and \( T \in \cL(V) \). A scalar \( \lambda \in F \) is an **eigenvalue** of \( T \) if there **exists** a **non-zero** vector \( \v \in V \) with
\[
T\v = \lambda\v .
\]
Every **non-zero** \( \v \in V \) with \( T\v = \lambda\v \) is called **an eigenvector** of \( T \) for the eigenvalue \( \lambda \).

For a matrix \( \A \in M_n(F) \), the eigenvalues and eigenvectors of \( \A \) are those of \( T_{\A} \colon F^n \to F^n \): a scalar \( \lambda \in F \) and a non-zero \( \v \in F^n \) with \( \A\v = \lambda\v \).
:::

In words: an eigenvalue is a scalar **in the field \( F \)** over which \( V \) is a vector space. It qualifies if **some** non-zero vector is sent to \( \lambda \) times itself. The vector must be non-zero; the scalar may be anything, including \( 0 \). An eigenvector is a witness for its eigenvalue, and there are always many witnesses: if \( \v \) is one, so is \( c\v \) for every \( c \ne 0 \), since \( T(c\v) = cT\v = \lambda(c\v) \).

**Well-definedness.** An eigenvector determines its eigenvalue. If \( T\v = \lambda\v \) and \( T\v = \mu\v \) with \( \v \ne \0 \), then \( (\lambda - \mu)\v = \0 \), and @thm-zero-product gives \( \lambda = \mu \). So "the eigenvalue of \( \v \)" makes sense, while "the eigenvector of \( \lambda \)" does not.

The eigenvectors for one eigenvalue, together with \( \0 \), are exactly the kernel found above. That set is a subspace, and it deserves its own name.

::: {#def-eigenspace}
[Eigenspace]

Let \( T \in \cL(V) \) and \( \lambda \in F \). The **eigenspace** of \( T \) for \( \lambda \) is
\[
E_\lambda(T) \coloneqq \ker(T - \lambda\,\id_V) = \{ \v \in V : T\v = \lambda\v \}.
\]
For \( \A \in M_n(F) \) we write \( E_\lambda(\A) = E_\lambda(T_{\A}) = \nul(\A - \lambda \I_n) \).
:::

\( E_\lambda(T) \) is a subspace by @thm-prop-kernel, and it is \( T \)-invariant by @thm-kernel-image-of-polynomial-invariant (b) with \( p = x - \lambda \). It is defined for **every** \( \lambda \in F \), and \( \lambda \) is an eigenvalue exactly when \( E_\lambda(T) \ne \{\0\} \); in that case the eigenvectors for \( \lambda \) are the non-zero vectors of \( E_\lambda(T) \). The eigenspace is the home of all eigenvectors for \( \lambda \) at once, and it is one of the invariant subspaces of the previous section: on it, \( T \) acts as \( \lambda\,\id \).

**Examples.**

- **Diagonal matrices.** Let \( \A = \diag(d_1, \dots, d_n) \). Then \( \A\e_j = d_j\e_j \) and \( \e_j \ne \0 \), so each \( d_j \) is an eigenvalue with eigenvector \( \e_j \). The standard basis is a basis of eigenvectors, which is the observation we started from, read backwards.
- **Degenerate cases.** On \( V \ne \{\0\} \), the identity has the eigenvalue \( 1 \) with \( E_1(\id_V) = V \): **every** non-zero vector is an eigenvector. The zero operator has the eigenvalue \( 0 \) with \( E_0 = V \). On \( V = \{\0\} \), no operator has any eigenvalue, because there is no non-zero vector to be a witness. That last case matters: it is why the existence theorem later in this section must assume \( V \ne \{\0\} \).
- **Projections.** Let \( P \in \cL(V) \) be a projection, \( P^2 = P \) (@def-projection-operator). If \( P\v = \lambda\v \) with \( \v \ne \0 \), then \( \lambda\v = P\v = P^2\v = P(\lambda\v) = \lambda^2\v \), so \( (\lambda^2 - \lambda)\v = \0 \) and \( \lambda(\lambda - 1) = 0 \) by @thm-zero-product. So the only possible eigenvalues are \( 0 \) and \( 1 \). By definition \( E_0(P) = \ker P \). Also \( E_1(P) = \im P \): a vector with \( P\v = \v \) is in the image, and conversely \( P \) is the identity on \( \im P \) by @thm-projection-direct-sum (a). So a vector is fixed by \( P \) exactly when it is in the image, and killed exactly when it is in the kernel.
- **Differentiation of polynomials.** Let \( D \) act on \( V = \nR[x]_{\le n} \) with \( n \ge 1 \). Suppose \( Dp = \lambda p \) with \( p \ne 0 \). If \( \lambda \ne 0 \), then \( \deg(\lambda p) = \deg p \), while \( Dp \) is either \( 0 \) or of degree \( \deg p - 1 \); neither equals \( \deg p \) for \( p \ne 0 \). So \( \lambda = 0 \), and \( E_0(D) = \ker D \) is the space of constant polynomials. Differentiation on \( \nR[x]_{\le n} \) has exactly one eigenvalue, and its eigenvectors span only a line.

**Non-example by minimal change.** For \( \A = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix} \), the vector \( \e_1 \) is an eigenvector: \( \A\e_1 = 2\e_1 \). Move to the neighboring basis vector \( \e_2 \). It is still non-zero, and \( \A\e_2 = (1, 3) \) is still a vector of \( \nR^2 \). What fails is the equation \( \A\v = \lambda\v \): no \( \lambda \) makes \( (1, 3) = (0, \lambda) \). So \( \e_2 \) is not an eigenvector, and the line \( \Span(\e_2) \) is not invariant, as we saw in the previous section.

**Why this definition.** The clause "**non-zero**" is what gives the notion content. The zero vector satisfies \( T\0 = \lambda\0 \) for **every** \( \lambda \in F \), so if we allowed \( \v = \0 \), every scalar would be an eigenvalue of every operator. On the other hand we do **not** exclude \( \lambda = 0 \): the equation \( T\v = 0\v \) says \( \v \in \ker T \), and a non-zero kernel vector is exactly the kind of information we want to record. Requiring \( \lambda \in F \), rather than in some larger field, makes the notion depend on the field, and this is deliberate: a real matrix may have no real eigenvalues, and then no real basis diagonalizes it. The prefix *eigen* is German for "own": an eigenvector is a direction that belongs to \( T \), which \( T \) maps into itself.

::: {.warning}
**The eigenvalue may be \( 0 \); the eigenvector may not.** For \( \A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} \), the vector \( (2, -1) \) satisfies \( \A(2, -1) = (0, 0) = 0 \cdot (2, -1) \), so \( 0 \) is an eigenvalue. By contrast, \( \A\0 = 7 \cdot \0 \) does **not** make \( 7 \) an eigenvalue. And say "**an** eigenvector for \( 0 \)", never "the": \( (2, -1) \), \( (-4, 2) \) and \( (200, -100) \) are all eigenvectors for \( 0 \).
:::

::: {.check}
Let \( T(x, y, z) = (x, z, y) \) on \( \nR^3 \). Which of \( \e_1 \), \( (0, 1, 1) \), \( (0, 1, -1) \), \( \e_2 \) are eigenvectors of \( T \), and for which eigenvalues?
:::

::: {.solution}
\( T\e_1 = \e_1 \), so \( \e_1 \) is an eigenvector for \( 1 \). \( T(0, 1, 1) = (0, 1, 1) \), an eigenvector for \( 1 \) as well. \( T(0, 1, -1) = (0, -1, 1) = -(0, 1, -1) \), an eigenvector for \( -1 \). \( T\e_2 = \e_3 \), which is not a multiple of \( \e_2 \), so \( \e_2 \) is **not** an eigenvector. The three eigenvectors form a basis of \( \nR^3 \), and in that basis \( [T] = \diag(1, 1, -1) \).
:::

## Finding eigenvalues

The definition asks for a non-zero vector in \( \ker(T - \lambda\,\id_V) \), a question about one \( \lambda \) at a time. In finite dimension, Chapters 3 and 6 turn it into a test that handles all \( \lambda \) at once. The last item is the one we compute with.

::: {#thm-eigenvalue-characterizations}
[Characterizations of Eigenvalues]

Let \( V \) be a finite-dimensional vector space over \( F \) with \( \dim V = n \ge 1 \), let \( T \in \cL(V) \) and \( \lambda \in F \). The following are equivalent:

::: {.enumerate options="label=(\alph*)"}
1. \( \lambda \) is an eigenvalue of \( T \);
2. \( E_\lambda(T) \ne \{\0\} \), that is, \( T - \lambda\,\id_V \) is **not injective**;
3. \( T - \lambda\,\id_V \) is **not invertible**;
4. \( \det(\lambda\,\id_V - T) = 0 \);
5. \( p_T(\lambda) = 0 \).
:::

In particular \( T \) has at most \( n \) eigenvalues. For \( \A \in M_n(F) \): \( \lambda \) is an eigenvalue of \( \A \) if and only if \( p_{\A}(\lambda) = 0 \), if and only if \( \lambda \I - \A \) is not invertible.
:::

::: {.proof}
(a) ⇔ (b). By @def-eigenvalue and @def-eigenspace, \( \lambda \) is an eigenvalue exactly when \( E_\lambda(T) = \ker(T - \lambda\,\id_V) \) contains a non-zero vector. By @thm-injective-iff-trivial-kernel, this happens exactly when \( T - \lambda\,\id_V \) is not injective.

(b) ⇔ (c). \( V \) is finite-dimensional, so by @thm-invertible-operator-tfae ((a) ⇔ (b)) an operator on \( V \) is invertible if and only if it is injective.

(c) ⇔ (d). The operators \( \lambda\,\id_V - T \) and \( T - \lambda\,\id_V \) differ by the factor \( -1 \), so one is invertible exactly when the other is. By @thm-det-operator-properties, \( \lambda\,\id_V - T \) is invertible if and only if \( \det(\lambda\,\id_V - T) \ne 0 \).

(c) ⇔ (e). Fix a basis \( \sB \) of \( V \) and put \( \A = [T]_{\sB} \). By @cor-matrix-of-polynomial-of-operator, \( [\lambda\,\id_V - T]_{\sB} = \lambda \I_n - \A \), and by @thm-rank-map-equals-rank-matrix (b), \( \lambda\,\id_V - T \) is invertible if and only if \( \lambda \I_n - \A \) is. By @thm-charpoly-root-iff-singular ((a), (i) ⇔ (ii)), \( \lambda \I_n - \A \) is not invertible if and only if \( p_{\A}(\lambda) = 0 \), and \( p_{\A} = p_T \) by @def-charpoly-operator.

The bound on the number of eigenvalues is @thm-charpoly-root-iff-singular (b) applied to \( \A \), since by (e) the eigenvalues of \( T \) are the roots of \( p_{\A} \) in \( F \). The statement for matrices is the case \( T = T_{\A} \), \( \sB \) standard, \( [T_{\A}]_{\sB} = \A \).
:::

For matrices, this is @thm-charpoly-root-iff-singular read in the new language: Chapter 6 found the scalars \( c \) with \( c\I - \A \) singular, and those are the eigenvalues. It gives a procedure with two steps.

1. Compute \( p_{\A}(x) = \det(x\I - \A) \) and find its roots **in \( F \)**. These are the eigenvalues.
2. For each eigenvalue \( \lambda \), solve the homogeneous system \( (\A - \lambda \I)\x = \0 \) by elimination. Its solution set is \( E_\lambda(\A) \), and a basis of it lists "all" eigenvectors for \( \lambda \) (@thm-basis-null-space).

::: {#exm-eigenvalues-2x2}
[Eigenvalues and Eigenspaces of a \( 2 \times 2 \) Matrix]

Find the eigenvalues and eigenspaces of \( \A = \begin{pmatrix} 1 & 2 \\ 3 & 2 \end{pmatrix} \in M_2(\nR) \).
:::

::: {.solution}
*Step 1.* For a \( 2 \times 2 \) matrix, \( p_{\A}(x) = x^2 - (\tr \A)x + \det \A \) (the examples after @def-characteristic-polynomial). Here \( \tr \A = 3 \) and \( \det \A = 2 - 6 = -4 \), so
\[
p_{\A}(x) = x^2 - 3x - 4 = (x - 4)(x + 1).
\]
By @thm-eigenvalue-characterizations, the eigenvalues are \( 4 \) and \( -1 \).

*Step 2.* For \( \lambda = 4 \),
\[
\A - 4\I = \begin{pmatrix} -3 & 2 \\ 3 & -2 \end{pmatrix}.
\]
The second row is \( -1 \) times the first, so the system reduces to \( -3x + 2y = 0 \), with solutions \( (x, y) = t(2, 3) \). Hence \( E_4(\A) = \Span((2, 3)) \). For \( \lambda = -1 \),
\[
\A + \I = \begin{pmatrix} 2 & 2 \\ 3 & 3 \end{pmatrix},
\]
which reduces to \( x + y = 0 \), so \( E_{-1}(\A) = \Span((1, -1)) \).

*Check.* \( \A(2, 3) = (2 + 6, 6 + 6) = (8, 12) = 4\,(2, 3) \) and \( \A(1, -1) = (1 - 2, 3 - 2) = (-1, 1) = -(1, -1) \). In the basis \( ((2, 3), (1, -1)) \), the operator \( T_{\A} \) has matrix \( \diag(4, -1) \), by the computation at the start of this section.
:::

In Step 2, the matrix \( \A - \lambda \I \) **must** be singular; if elimination produces only the trivial solution, then \( \lambda \) was not a root of \( p_{\A} \), and Step 1 contains an error. This is a built-in check.

**Triangular matrices.** If \( \A \) is upper or lower triangular, then \( p_{\A}(x) = (x - a_{11}) \cdots (x - a_{nn}) \) (the examples after @def-characteristic-polynomial), so the eigenvalues of a triangular matrix are its diagonal entries. For \( \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix} \) they are \( 2 \) and \( 3 \), with eigenvectors \( \e_1 \) and \( (1, 1) \), found in the previous section.

You can watch eigenvectors in the widget below. It shows the unit square and its image under \( \A = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix} \). The image \( \A\e_1 \) lies on the \( x \)-axis, which says that \( \e_1 \) is an eigenvector. The far corner of the image parallelogram is \( \A(1, 1) = \A\e_1 + \A\e_2 = (3, 3) \), and it lies on the diagonal line through \( (1, 1) \): so \( (1, 1) \) is an eigenvector too, for the eigenvalue \( 3 \). Drag \( \A\e_2 \) to \( (1, 2) \), which changes the matrix to \( \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} \). Now the far corner \( (3, 2) \) leaves the diagonal, and only the \( x \)-axis is still mapped into itself. The next section explains what was lost.

::: {.widget src="widgets/linear-map.js" matrix="2,1,0,3"}
::: {.print}
\begin{center}
\begin{tikzpicture}[scale=0.8]
    \draw[->] (-0.5,0) -- (3.8,0) node[right] {$x$};
    \draw[->] (0,-0.5) -- (0,3.8) node[above] {$y$};
    \draw[dotted] (-0.5,-0.5) -- (3.6,3.6);
    \draw[dashed] (0,0) rectangle (1,1);
    \fill[gray!25] (0,0) -- (2,0) -- (3,3) -- (1,3) -- cycle;
    \draw (0,0) -- (2,0) -- (3,3) -- (1,3) -- cycle;
    \draw[very thick, ->] (0,0) -- (2,0) node[below] {$A\mathbf{e}_1 = (2,0)$};
    \draw[very thick, ->] (0,0) -- (1,3) node[left] {$A\mathbf{e}_2 = (1,3)$};
    \fill (3,3) circle (1.5pt) node[right] {$A(1,1) = (3,3)$};
\end{tikzpicture}
\end{center}

The unit square (dashed) and its image under \( \A = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix} \). The image of \( \e_1 \) stays on the \( x \)-axis (eigenvalue \( 2 \)), and the image of \( (1, 1) \) stays on the dotted diagonal (eigenvalue \( 3 \)). The image of \( \e_2 \) leaves the \( y \)-axis, so \( \e_2 \) is not an eigenvector.
:::
:::

The set of all eigenvalues is used so often that it gets a symbol.

::: {#def-spectrum}
[Spectrum]

Let \( T \in \cL(V) \). The **spectrum** of \( T \) is the set \( \spec(T) \subseteq F \) of all eigenvalues of \( T \). For \( \A \in M_n(F) \), \( \spec(\A) \coloneqq \spec(T_{\A}) \).
:::

For instance \( \spec\begin{pmatrix} 1 & 2 \\ 3 & 2 \end{pmatrix} = \{4, -1\} \), \( \spec(\id_V) = \{1\} \) for \( V \ne \{\0\} \), and the spectrum of a projection is contained in \( \{0, 1\} \). By @thm-eigenvalue-characterizations, if \( \dim V = n \ge 1 \), then \( \spec(T) \) is the set of roots of \( p_T \) in \( F \), and it has at most \( n \) elements. It may be empty: the characteristic polynomial of the rotation \( \R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \) is \( x^2 + 1 \), which has no real root, so \( \spec(\R) = \emptyset \) over \( \nR \). This matches @exm-rotation-invariant-subspaces: no invariant lines, no eigenvectors.

**Infinite dimension.** Without a characteristic polynomial, we go back to the definition, and anything can happen.

- **Differentiation of smooth functions.** Let \( V \) be the space of infinitely differentiable functions \( \nR \to \nR \) (a subspace of \( \nR^{\nR} \), by the argument of @exm-differentiable-functions applied to all derivatives), and \( D f = f' \). Here we take three facts from calculus as known: \( e^{\lambda x} \) is smooth with derivative \( \lambda e^{\lambda x} \); the product rule; and a function on \( \nR \) with derivative \( 0 \) everywhere is constant. For **every** \( \lambda \in \nR \), the function \( f(x) = e^{\lambda x} \) is non-zero and satisfies \( Df = \lambda f \). So \( \spec(D) = \nR \), an infinite set. In fact \( E_\lambda(D) = \Span(e^{\lambda x}) \): if \( f' = \lambda f \), then by the product rule \( g(x) = e^{-\lambda x}f(x) \) has \( g' = e^{-\lambda x}(f' - \lambda f) = 0 \), so \( g \) is a constant \( c \) and \( f = ce^{\lambda x} \).
- **The right shift.** Let \( R(s_0, s_1, s_2, \dots) = (0, s_0, s_1, \dots) \) on \( F^{\nN} \) (@exm-shift). If \( R\s = \lambda\s \), compare entries: \( 0 = \lambda s_0 \), and \( s_k = \lambda s_{k+1} \) for all \( k \ge 0 \). If \( \lambda = 0 \), the second equation gives \( s_k = 0 \) for all \( k \). If \( \lambda \ne 0 \), the first gives \( s_0 = 0 \), and then \( s_{k+1} = \lambda^{-1}s_k \) gives \( s_1 = 0 \), \( s_2 = 0 \), and so on by induction. Either way \( \s = \0 \). So \( \spec(R) = \emptyset \), over **every** field.

::: {.warning}
**In infinite dimension, "not invertible" does not produce an eigenvalue.** The step (b) ⇔ (c) of @thm-eigenvalue-characterizations used finite dimension. The right shift \( R \) is injective but not surjective (@exm-shift-kernel-image), so \( R - 0 \cdot \id \) is not invertible, yet \( 0 \) is not an eigenvalue of \( R \): nothing non-zero is sent to \( \0 \).
:::

## Distinct eigenvalues give independent eigenvectors

In @exm-eigenvalues-2x2 the eigenvectors \( (2, 3) \) and \( (1, -1) \) for the eigenvalues \( 4 \) and \( -1 \) formed a basis. That is no accident. Eigenvectors for different eigenvalues can never be linearly dependent.

::: {#thm-distinct-eigenvalues-independent}
[Distinct Eigenvalues Give Independent Eigenvectors]

Let \( T \in \cL(V) \), let \( \lambda_1, \dots, \lambda_k \in F \) be **distinct** eigenvalues of \( T \), and for each \( i \) let \( \v_i \) be an eigenvector of \( T \) for \( \lambda_i \). Then \( (\v_1, \dots, \v_k) \) is linearly independent.
:::

::: {.idea}
Try two vectors first. From \( a\v_1 + b\v_2 = \0 \), we want to kill one term, and the operator \( T - \lambda_2\id_V \) does exactly that: it sends \( \v_2 \) to \( \0 \) and \( \v_1 \) to \( (\lambda_1 - \lambda_2)\v_1 \). So \( a(\lambda_1 - \lambda_2)\v_1 = \0 \), and since \( \lambda_1 \ne \lambda_2 \) and \( \v_1 \ne \0 \), \( a = 0 \); then \( b = 0 \). In general, applying \( T - \lambda_j\id_V \) to a dependence kills the \( j \)-th vector and rescales the others by non-zero factors, producing a **shorter** dependence. So a shortest dependence cannot exist. The Linear Dependence Lemma lets us pick that shortest one cleanly.
:::

::: {.proof}
Suppose, for a contradiction, that \( (\v_1, \dots, \v_k) \) is linearly dependent. By @thm-linear-dependence-lemma (1), there is an index \( j \) with \( \v_j \in \Span(\v_1, \dots, \v_{j-1}) \); choose the **smallest** such \( j \). Since \( \v_1 \ne \0 \), \( j \ge 2 \). The list \( (\v_1, \dots, \v_{j-1}) \) is linearly independent: otherwise @thm-linear-dependence-lemma (1), applied to it, would give a smaller index with the same property. Write
\[
\v_j = a_1\v_1 + \dots + a_{j-1}\v_{j-1} \qquad (a_i \in F).
\]
Apply \( T - \lambda_j\id_V \) to both sides. Since \( (T - \lambda_j\id_V)\v_i = (\lambda_i - \lambda_j)\v_i \) for each \( i \), linearity gives
\[
\0 = a_1(\lambda_1 - \lambda_j)\v_1 + \dots + a_{j-1}(\lambda_{j-1} - \lambda_j)\v_{j-1}.
\]
By independence of \( (\v_1, \dots, \v_{j-1}) \), every coefficient \( a_i(\lambda_i - \lambda_j) \) is \( 0 \). The eigenvalues are distinct, so \( \lambda_i - \lambda_j \ne 0 \) for \( i < j \), and hence \( a_i = 0 \) for all \( i < j \). Then \( \v_j = \0 \), which contradicts the fact that an eigenvector is non-zero. This proves that \( (\v_1, \dots, \v_k) \) is linearly independent.
:::

The theorem works in any vector space, finite-dimensional or not. For instance, for distinct real numbers \( \lambda_1, \dots, \lambda_k \), the functions \( e^{\lambda_1x}, \dots, e^{\lambda_kx} \) are eigenvectors of differentiation for distinct eigenvalues, so they are linearly independent, with no computation at all. Two consequences follow at once, and the second is the first half of a promise made in Chapter 1, §7: eigenspaces sit inside \( V \) as a direct sum.

::: {#cor-eigenspaces-direct-sum}
[Eigenspaces Form a Direct Sum]

Let \( T \in \cL(V) \) and let \( \lambda_1, \dots, \lambda_k \in F \) be distinct. Then the sum \( E_{\lambda_1}(T) + \dots + E_{\lambda_k}(T) \) is direct. If \( V \) is finite-dimensional, then
\[
\dim E_{\lambda_1}(T) + \dots + \dim E_{\lambda_k}(T) \le \dim V,
\]
and \( T \) has at most \( \dim V \) distinct eigenvalues.
:::

::: {.proof}
By @thm-direct-sum-k-criteria ((b) ⇒ (a)), it suffices to show: if \( \u_1 + \dots + \u_k = \0 \) with \( \u_i \in E_{\lambda_i}(T) \), then every \( \u_i = \0 \). Suppose not, and let \( S \) be the non-empty set of indices \( i \) with \( \u_i \ne \0 \). For \( i \in S \), \( \u_i \) is an eigenvector of \( T \) for \( \lambda_i \), and these eigenvalues are distinct. By @thm-distinct-eigenvalues-independent, the list \( (\u_i)_{i \in S} \) is linearly independent. But \( \sum_{i \in S} 1 \cdot \u_i = \sum_{i=1}^{k} \u_i = \0 \) is a relation with all coefficients \( 1 \ne 0 \), a contradiction. So the sum is direct.

If \( V \) is finite-dimensional, @thm-direct-sum-k-criteria ((a) ⇒ (e)) gives \( \dim(E_{\lambda_1}(T) \oplus \dots \oplus E_{\lambda_k}(T)) = \sum_i \dim E_{\lambda_i}(T) \), and this is at most \( \dim V \) by @thm-subspace-dimension. If the \( \lambda_i \) are eigenvalues, each \( \dim E_{\lambda_i}(T) \ge 1 \), so \( k \le \dim V \).
:::

The corollary gives a second, polynomial-free proof that an operator on an \( n \)-dimensional space has at most \( n \) eigenvalues. Section 4 shows that \( T \) has a diagonal matrix exactly when the inequality is an equality.

## Existence over the complex numbers

We have seen operators without eigenvalues: the rotation of \( \nR^2 \), and the right shift. The rotation fails because \( \nR \) is missing the roots of \( x^2 + 1 \); the shift fails because its space is infinite-dimensional. Remove both obstacles and eigenvalues always exist.

::: {#thm-complex-operator-has-eigenvalue}
[Complex Operators Have Eigenvalues]

Let \( V \) be a finite-dimensional vector space over \( \nC \) with \( V \ne \{\0\} \), and let \( T \in \cL(V) \). Then \( T \) has an eigenvalue. The same holds for every \( \A \in M_n(\nC) \) with \( n \ge 1 \).
:::

::: {.proof}
Let \( n = \dim V \ge 1 \). By @thm-charpoly-coefficients and @def-charpoly-operator, \( p_T \in \nC[x] \) is monic of degree \( n \ge 1 \), so it is not constant. By the Fundamental Theorem of Algebra (@thm-fundamental-theorem-of-algebra), \( p_T(\lambda) = 0 \) for some \( \lambda \in \nC \). By @thm-eigenvalue-characterizations ((e) ⇒ (a)), \( \lambda \) is an eigenvalue of \( T \). For \( \A \in M_n(\nC) \), apply this to \( T_{\A} \).
:::

Alternatively, determinants can be avoided altogether, and the proof then shows where the eigenvector comes from. By @thm-annihilating-polynomial-exists, there is a non-zero \( p \in \nC[x] \) with \( p(T) = 0 \). It is not a non-zero constant \( c \), since \( c\,\id_V \ne 0 \) on \( V \ne \{\0\} \). By @cor-complex-polynomial-splits, \( p = c(x - z_1)\cdots(x - z_m) \) with \( c \ne 0 \) and \( m \ge 1 \), so by @thm-evaluation-homomorphism (a) and (b),
\[
0 = p(T) = c\,(T - z_1\id_V)(T - z_2\id_V)\cdots(T - z_m\id_V).
\]
Since \( c \ne 0 \), multiplying by \( c^{-1} \) shows that the composite \( (T - z_1\id_V)\cdots(T - z_m\id_V) \) is the zero operator, which is not injective on \( V \ne \{\0\} \). A composition of injective maps is injective (@thm-composition-preserves (a), applied \( m - 1 \) times), so at least one factor \( T - z_j\id_V \) is not injective, and \( z_j \) is an eigenvalue by @thm-eigenvalue-characterizations ((b) ⇒ (a)).

Both routes use the Fundamental Theorem of Algebra, and both need all three hypotheses. Over \( \nR \) the rotation has no eigenvalue. In infinite dimension the right shift on \( \nC^{\nN} \) has none, and indeed no non-zero polynomial annihilates it: for \( p = a_0 + a_1x + \dots + a_Nx^N \ne 0 \), the sequence \( p(R)(1, 0, 0, \dots) = (a_0, a_1, \dots, a_N, 0, \dots) \) is not zero. On \( V = \{\0\} \) there is nothing to be an eigenvector. This theorem pays off the promise made in Chapter 5, and it is the base step of every structure theorem over \( \nC \) in this book: find one eigenvector, then look at what is left.

::: {.check}
Does every operator on \( \nC^3 \) have an invariant line? Does every operator on \( \nR^2 \)?
:::

::: {.solution}
Every operator on \( \nC^3 \) has one: by @thm-complex-operator-has-eigenvalue it has an eigenvector \( \v \), and \( \Span(\v) \) is invariant by @prp-one-dimensional-invariant. Not every operator on \( \nR^2 \): the rotation by a right angle has no invariant line (@exm-rotation-invariant-subspaces).
:::

## Real matrices and complex eigenvalues

A real matrix may have no real eigenvalues, but it is also a complex matrix, and as such it has eigenvalues by @thm-complex-operator-has-eigenvalue. This is the situation Chapter 1, §9 prepared for. Let \( \A \in M_n(\nR) \). The complexification of \( \nR^n \) is \( \nC^n \): the pair \( (\x, \y) \) is the vector \( \x + i\y \) (@exm-complexification-rn). The real operator \( T_{\A} \) extends to the complexification by the only rule compatible with complex scalars,
\[
\x + i\y \;\mapsto\; \A\x + i\A\y = \A(\x + i\y),
\]
which is just \( T_{\A} \) for \( \A \) regarded as a matrix in \( M_n(\nC) \). By @thm-complexification-basis, the real standard basis is also a complex basis of \( \nC^n \), and in it the extended operator still has matrix \( \A \); in particular it has the same characteristic polynomial \( p_{\A} \in \nR[x] \subseteq \nC[x] \). So the **complex eigenvalues** of a real matrix are the roots of \( p_{\A} \) in \( \nC \), with eigenvectors in \( \nC^n \), and the real eigenvalues are among them. The complex ones cannot appear alone.

::: {#thm-real-matrix-complex-eigenvalues}
[Complex Eigenvalues of Real Matrices Come in Conjugate Pairs]

Let \( \A \in M_n(\nR) \), regarded as an element of \( M_n(\nC) \). If \( \lambda \in \nC \) is an eigenvalue of \( \A \) with eigenvector \( \v \in \nC^n \), then \( \conj{\lambda} \) is an eigenvalue of \( \A \) with eigenvector \( \conj{\v} \), the vector of conjugated entries. Moreover:

::: {.enumerate options="label=(\alph*)"}
1. \( \operatorname{mult}_\lambda(p_{\A}) = \operatorname{mult}_{\conj{\lambda}}(p_{\A}) \);
2. if \( \lambda \notin \nR \), then \( (\v, \conj{\v}) \) is linearly independent over \( \nC \).
:::
:::

::: {.proof}
Let \( \A\v = \lambda\v \) with \( \v = (v_1, \dots, v_n) \ne \0 \). For each \( k \), the \( k \)-th entry of \( \A\v \) is \( \sum_j a_{kj}v_j \) (@def-matrix-multiplication). By @thm-conjugate-properties (a) and (b), and since \( \conj{a_{kj}} = a_{kj} \) for the real entries of \( \A \),
\[
\conj{\textstyle\sum_j a_{kj}v_j} = \sum_j a_{kj}\conj{v_j}, \qquad \conj{\lambda v_k} = \conj{\lambda}\,\conj{v_k}.
\]
Conjugating the equation \( \A\v = \lambda\v \) entry by entry therefore gives \( \A\conj{\v} = \conj{\lambda}\,\conj{\v} \). Since \( \conj{\conj{v_k}} = v_k \), \( \conj{\v} = \0 \) would force \( \v = \0 \); so \( \conj{\v} \ne \0 \), and \( \conj{\v} \) is an eigenvector for \( \conj{\lambda} \).

(a) The entries of \( x\I - \A \) lie in \( \nR[x] \), so its determinant \( p_{\A} \) lies in \( \nR[x] \) (@def-characteristic-polynomial). By @thm-real-roots-conjugate-pairs, \( \operatorname{mult}_{\conj{\lambda}}(p_{\A}) = \operatorname{mult}_\lambda(p_{\A}) \).

(b) If \( \lambda \notin \nR \), then \( \conj{\lambda} \ne \lambda \), so \( \v \) and \( \conj{\v} \) are eigenvectors for distinct eigenvalues, and they are independent by @thm-distinct-eigenvalues-independent.
:::

For the rotation \( \R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \), the vector \( (1, -i) \) satisfies \( \R(1, -i) = (i, 1) = i\,(1, -i) \), so \( i \) is an eigenvalue. Conjugating, \( \R(1, i) = (-i, 1) = -i\,(1, i) \). Over \( \nC \), the two eigenvectors form a basis of \( \nC^2 \), and the rotation has a diagonal matrix \( \diag(i, -i) \) in it, although no real basis diagonalizes it. So the field matters for eigenvalues, and it will matter for diagonalization.

::: {#exm-complex-eigenvalues-real-matrix}
[A Real Matrix with Non-Real Eigenvalues]

Find the eigenvalues of \( \A = \begin{pmatrix} 3 & -2 \\ 4 & -1 \end{pmatrix} \) over \( \nC \), with an eigenvector for each.
:::

::: {.solution}
Here \( \tr \A = 2 \) and \( \det \A = -3 + 8 = 5 \), so \( p_{\A}(x) = x^2 - 2x + 5 = (x - 1)^2 + 4 \). Over \( \nR \) this has no root, so \( \spec(\A) = \emptyset \) over \( \nR \). Over \( \nC \), \( (x - 1)^2 = -4 \) gives the roots \( 1 + 2i \) and \( 1 - 2i \).

For \( \lambda = 1 + 2i \),
\[
\A - \lambda \I = \begin{pmatrix} 2 - 2i & -2 \\ 4 & -2 - 2i \end{pmatrix}.
\]
The first row gives \( (2 - 2i)x = 2y \), that is, \( y = (1 - i)x \); take \( \v = (1, 1 - i) \). Check the second row: \( 4 \cdot 1 + (-2 - 2i)(1 - i) = 4 + (-2 + 2i - 2i + 2i^2) = 4 - 4 = 0 \). So \( \v \) is an eigenvector for \( 1 + 2i \). By @thm-real-matrix-complex-eigenvalues, \( \conj{\v} = (1, 1 + i) \) is an eigenvector for \( 1 - 2i \), with no further computation.
:::

## The invertible matrix theorem grows

Chapter 2 listed eight conditions equivalent to invertibility (@thm-invertible-tfae), and Chapter 6 added the determinant (@thm-invertible-tfae-det). Eigenvalues give one more: a matrix is singular exactly when it kills a non-zero vector, which is to say, when it stretches some non-zero vector by the factor \( 0 \).

::: {#thm-invertible-tfae-eigen}
[Invertible Matrix Theorem, with Eigenvalues]

Let \( \A \in M_n(F) \) with \( n \ge 1 \). The following are equivalent, and each is equivalent to each of the conditions of @thm-invertible-tfae-det and @thm-invertible-tfae.

::: {.enumerate options="label=(\alph*)"}
1. \( \A \) is invertible.
2. \( 0 \) is **not** an eigenvalue of \( \A \), that is, \( 0 \notin \spec(\A) \).
:::

Likewise, an operator \( T \) on a finite-dimensional space \( V \ne \{\0\} \) is invertible if and only if \( 0 \notin \spec(T) \).
:::

::: {.proof}
By @def-eigenspace, \( E_0(\A) = \ker(T_{\A} - 0\,\id) = \ker T_{\A} \). So \( 0 \notin \spec(\A) \) if and only if \( \ker T_{\A} = \{\0\} \), if and only if \( T_{\A} \) is injective (@thm-injective-iff-trivial-kernel), if and only if \( \A \) is invertible (@thm-invertible-tfae-det, (a) ⇔ (b)). For an operator, \( E_0(T) = \ker T \), and @thm-invertible-operator-tfae ((a) ⇔ (c)) finishes the same way.
:::

For example, \( \spec\begin{pmatrix} 1 & 2 \\ 3 & 2 \end{pmatrix} = \{4, -1\} \) does not contain \( 0 \), so that matrix is invertible, while \( \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} \) has the eigenvalue \( 0 \) and is singular.

Eigenvalues are easy to compute for one matrix, and it is tempting to assume they behave well under the operations we use on matrices. Two such assumptions are false.

::: {.warning}
**Eigenvalues do not add or multiply.** Let \( \A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) and \( \B = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \). Both are triangular with zero diagonal, so \( \spec(\A) = \spec(\B) = \{0\} \). But \( \A + \B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) has \( p(x) = x^2 - 1 \) and eigenvalues \( \pm 1 \), which are not sums of eigenvalues of \( \A \) and \( \B \); and \( \A \B = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \) has the eigenvalue \( 1 \), which is not a product of them.
:::

::: {.warning}
**Row operations change eigenvalues.** Elimination preserves the solution set of \( \A\x = \0 \) (@thm-row-ops-preserve-solutions), not the solution sets of \( \A\x = \lambda\x \). For \( \A = \begin{pmatrix} 1 & 2 \\ 3 & 2 \end{pmatrix} \), with eigenvalues \( 4 \) and \( -1 \), subtracting \( 3 \) times row \( 1 \) from row \( 2 \) gives the triangular matrix \( \begin{pmatrix} 1 & 2 \\ 0 & -4 \end{pmatrix} \), whose eigenvalues are \( 1 \) and \( -4 \). So never row reduce \( \A \) to find its eigenvalues; row reduce \( \A - \lambda \I \) to find eigenvectors, once \( \lambda \) is known.
:::

## Exercises

### A. Check your understanding

:::: {#exr-eigenvalues-and-eigenvectors-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define eigenvalue, eigenvector and eigenspace of an operator \( T \in \cL(V) \).
2. True or false: \( \0 \) is an eigenvector of every operator. Justify your answer.
3. True or false: if \( 0 \) is an eigenvalue of \( \A \in M_n(F) \), then \( \A \) is not invertible. Justify your answer.
4. State four conditions equivalent to "\( \lambda \) is an eigenvalue of \( T \)" for an operator on a finite-dimensional space \( V \ne \{\0\} \).
5. True or false: every operator on \( \nR^2 \) has an eigenvalue. Justify your answer.
6. True or false: the eigenvalues of \( \A \) are the diagonal entries of a row echelon form of \( \A \). Justify your answer.
:::
::::

::: {.solution}
(a) \( \lambda \in F \) is an eigenvalue of \( T \) if \( T\v = \lambda\v \) for some **non-zero** \( \v \in V \); each such non-zero \( \v \) is an eigenvector for \( \lambda \) (@def-eigenvalue). The eigenspace is \( E_\lambda(T) = \ker(T - \lambda\,\id_V) \) (@def-eigenspace).

(b) False. Eigenvectors are non-zero by definition. (The equation \( T\0 = \lambda\0 \) holds for every \( \lambda \), which is why \( \0 \) is excluded.)

(c) True, by @thm-invertible-tfae-eigen.

(d) By @thm-eigenvalue-characterizations: \( T - \lambda\,\id_V \) is not injective; \( T - \lambda\,\id_V \) is not invertible; \( \det(\lambda\,\id_V - T) = 0 \); \( p_T(\lambda) = 0 \).

(e) False. The rotation \( R(x, y) = (-y, x) \) has \( p_R = x^2 + 1 \), with no real root, so it has no real eigenvalue.

(f) False. Row operations change eigenvalues: \( \begin{pmatrix} 1 & 2 \\ 3 & 2 \end{pmatrix} \) has eigenvalues \( 4, -1 \), but the echelon form \( \begin{pmatrix} 1 & 2 \\ 0 & -4 \end{pmatrix} \) has diagonal entries \( 1, -4 \).
:::

### B. Practice

:::: {#exr-eigenvalues-and-eigenvectors-b1}
[B1: Computing eigenvalues and eigenspaces]

Find the eigenvalues and a basis of each eigenspace of the following real matrices.

::: {.enumerate options="label=(\alph*)"}
1. \( \A = \begin{pmatrix} 5 & 4 \\ -2 & -1 \end{pmatrix} \).
2. \( \B = \begin{pmatrix} 2 & 0 & 1 \\ -1 & 3 & 1 \\ 2 & -2 & 1 \end{pmatrix} \).
:::

Hence write down a basis of \( \nR^2 \) consisting of eigenvectors of \( \A \), and a basis of \( \nR^3 \) consisting of eigenvectors of \( \B \).
::::

::: {.solution}
(a) \( \tr \A = 4 \) and \( \det \A = -5 + 8 = 3 \), so \( p_{\A}(x) = x^2 - 4x + 3 = (x - 1)(x - 3) \), and \( \spec(\A) = \{1, 3\} \) by @thm-eigenvalue-characterizations. For \( \lambda = 1 \), \( \A - \I = \begin{pmatrix} 4 & 4 \\ -2 & -2 \end{pmatrix} \) reduces to \( x + y = 0 \), so \( E_1(\A) = \Span((1, -1)) \). For \( \lambda = 3 \), \( \A - 3\I = \begin{pmatrix} 2 & 4 \\ -2 & -4 \end{pmatrix} \) reduces to \( x + 2y = 0 \), so \( E_3(\A) = \Span((2, -1)) \). Check: \( \A(1, -1) = (1, -1) \) and \( \A(2, -1) = (6, -3) = 3(2, -1) \).

(b) Expanding \( \det(x\I - \B) \) along the first row,
\[
p_{\B}(x) = \det\begin{pmatrix} x - 2 & 0 & -1 \\ 1 & x - 3 & -1 \\ -2 & 2 & x - 1 \end{pmatrix}
= (x - 2)\big[(x - 3)(x - 1) + 2\big] + (-1)\big[1 \cdot 2 - (x - 3)(-2)\big].
\]
The first bracket is \( x^2 - 4x + 5 \) and the second is \( 2x - 4 = 2(x - 2) \), so
\[
p_{\B}(x) = (x - 2)(x^2 - 4x + 5) - 2(x - 2) = (x - 2)(x^2 - 4x + 3) = (x - 1)(x - 2)(x - 3).
\]
So \( \spec(\B) = \{1, 2, 3\} \). Solving \( (\B - \lambda \I)\x = \0 \):

- \( \lambda = 1 \): \( \B - \I = \begin{pmatrix} 1 & 0 & 1 \\ -1 & 2 & 1 \\ 2 & -2 & 0 \end{pmatrix} \). The first row gives \( z = -x \), the third gives \( y = x \), and the second is then \( -x + 2x - x = 0 \). So \( E_1(\B) = \Span((1, 1, -1)) \).
- \( \lambda = 2 \): \( \B - 2\I = \begin{pmatrix} 0 & 0 & 1 \\ -1 & 1 & 1 \\ 2 & -2 & -1 \end{pmatrix} \). The first row gives \( z = 0 \), and then the second gives \( y = x \). So \( E_2(\B) = \Span((1, 1, 0)) \).
- \( \lambda = 3 \): \( \B - 3\I = \begin{pmatrix} -1 & 0 & 1 \\ -1 & 0 & 1 \\ 2 & -2 & -2 \end{pmatrix} \). The first row gives \( z = x \), and the third gives \( 2x - 2y - 2x = 0 \), so \( y = 0 \). So \( E_3(\B) = \Span((1, 0, 1)) \).

Check: \( \B(1, 1, -1) = (1, 1, -1) \), \( \B(1, 1, 0) = (2, 2, 0) \), \( \B(1, 0, 1) = (3, 0, 3) \).

Hence: the eigenvalues of \( \A \) are distinct, so by @thm-distinct-eigenvalues-independent the eigenvectors \( ((1, -1), (2, -1)) \) are independent, and two independent vectors in \( \nR^2 \) form a basis (@thm-right-size-basis). In the same way \( ((1, 1, -1), (1, 1, 0), (1, 0, 1)) \) is a basis of \( \nR^3 \) consisting of eigenvectors of \( \B \).
:::

:::: {#exr-eigenvalues-and-eigenvectors-b2}
[B2: The transpose map]

Let \( F \) be a field of characteristic not \( 2 \), and let \( \tau \colon M_2(F) \to M_2(F) \), \( \tau(\X) = \X\tp \).

::: {.enumerate options="label=(\alph*)"}
1. Show that every eigenvalue \( \lambda \) of \( \tau \) satisfies \( \lambda^2 = 1 \).
2. Find \( \spec(\tau) \), and describe \( E_1(\tau) \) and \( E_{-1}(\tau) \) with a basis of each.
:::
::::

::: {.solution}
(a) Let \( \tau(\X) = \lambda \X \) with \( \X \ne 0 \). Since \( (\X\tp)\tp = \X \) (@thm-transpose-properties), \( \X = \tau(\tau(\X)) = \tau(\lambda \X) = \lambda\tau(\X) = \lambda^2\X \). So \( (\lambda^2 - 1)\X = 0 \) with \( \X \ne 0 \), and \( \lambda^2 = 1 \) by @thm-zero-product.

(b) From \( \lambda^2 - 1 = (\lambda - 1)(\lambda + 1) = 0 \), the only candidates are \( 1 \) and \( -1 \), which are different because the characteristic is not \( 2 \). \( E_1(\tau) = \{ \X : \X\tp = \X \} \) is the space of symmetric matrices. Writing \( \X = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \), the condition is \( b = c \), so \( E_1(\tau) = \Span(\E_{11}, \E_{22}, \E_{12} + \E_{21}) \), and these three matrices are independent (compare entries). \( E_{-1}(\tau) = \{ \X : \X\tp = -\X \} \) is the space of skew-symmetric matrices. The condition \( \X\tp = -\X \) says \( a = -a \), \( d = -d \) and \( c = -b \); since \( 2 \ne 0 \), \( a = d = 0 \), so \( E_{-1}(\tau) = \Span(\E_{12} - \E_{21}) \). Both eigenspaces are non-zero, so \( \spec(\tau) = \{1, -1\} \). This agrees with @thm-involution-decomposition: \( \tau^2 = \id \), and \( M_2(F) = E_1(\tau) \oplus E_{-1}(\tau) \), with dimensions \( 3 + 1 = 4 \).
:::

:::: {#exr-eigenvalues-and-eigenvectors-b3}
[B3: Eigenvalues of powers and inverses]

Let \( T \in \cL(V) \) and let \( \v \) be an eigenvector of \( T \) for \( \lambda \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \v \) is an eigenvector of \( T^2 \) for \( \lambda^2 \), and more generally of \( p(T) \) for \( p(\lambda) \), for every \( p \in F[x] \).
2. Suppose \( T \) is invertible. Prove that \( \lambda \ne 0 \) and that \( \v \) is an eigenvector of \( T^{-1} \) for \( \lambda^{-1} \).
3. Show that the converse of the first statement in (a) fails: give \( T \in \cL(\nR^2) \) such that \( -1 \) is an eigenvalue of \( T^2 \) but \( T \) has no eigenvalue.
:::
::::

::: {.solution}
(a) \( T^2\v = T(T\v) = T(\lambda\v) = \lambda T\v = \lambda^2\v \), and \( \v \ne \0 \). By induction on \( k \), \( T^k\v = \lambda^k\v \): if \( T^k\v = \lambda^k\v \), then \( T^{k+1}\v = T(\lambda^k\v) = \lambda^{k+1}\v \). For \( p = \sum_k a_kx^k \), @def-polynomial-of-operator gives \( p(T)\v = \sum_k a_kT^k\v = \sum_k a_k\lambda^k\v = p(\lambda)\v \).

(b) An invertible operator is injective, so \( \ker T = \{\0\} \) and \( T\v \ne \0 \); as \( T\v = \lambda\v \), \( \lambda \ne 0 \) by @thm-zero-product. Applying \( T^{-1} \) to \( T\v = \lambda\v \) gives \( \v = \lambda T^{-1}\v \), so \( T^{-1}\v = \lambda^{-1}\v \).

(c) Take the rotation \( R(x, y) = (-y, x) \). It has no real eigenvalue (@exm-rotation-invariant-subspaces). But \( R^2(x, y) = R(-y, x) = (-x, -y) \), so \( R^2 = -\id \), and every non-zero vector is an eigenvector of \( R^2 \) for \( -1 \). Part (a) would need a real \( \lambda \) with \( \lambda^2 = -1 \), and there is none.
:::

### C. Going deeper

:::: {#exr-eigenvalues-and-eigenvectors-c1}
[C1: Every vector an eigenvector]

Let \( V \) be a vector space over \( F \) and \( T \in \cL(V) \). Suppose every non-zero vector of \( V \) is an eigenvector of \( T \). Prove that \( T = c\,\id_V \) for some \( c \in F \).

*Hint: compare the eigenvalues of \( \v \), \( \w \) and \( \v + \w \).*
::::

::: {.solution}
If \( V = \{\0\} \), then \( T = 0 = 1 \cdot \id_V \). Otherwise, for each \( \v \ne \0 \) let \( \lambda_\v \) be its eigenvalue, which is unique by the well-definedness remark after @def-eigenvalue. We show that \( \lambda_\v = \lambda_\w \) for all non-zero \( \v, \w \).

*Case 1: \( (\v, \w) \) is linearly dependent.* Then \( \w = a\v \) for some \( a \ne 0 \), and \( T\w = aT\v = \lambda_\v(a\v) = \lambda_\v\w \). By uniqueness of the eigenvalue of \( \w \), \( \lambda_\w = \lambda_\v \).

*Case 2: \( (\v, \w) \) is linearly independent.* Then \( \v + \w \ne \0 \), and
\[
\lambda_{\v + \w}\v + \lambda_{\v + \w}\w = T(\v + \w) = T\v + T\w = \lambda_\v\v + \lambda_\w\w .
\]
So \( (\lambda_{\v + \w} - \lambda_\v)\v + (\lambda_{\v + \w} - \lambda_\w)\w = \0 \), and by independence \( \lambda_\v = \lambda_{\v + \w} = \lambda_\w \).

Fix \( \v_0 \ne \0 \) and put \( c = \lambda_{\v_0} \). Then \( T\v = c\v \) for every \( \v \ne \0 \), and also for \( \v = \0 \). Hence \( T = c\,\id_V \).
:::

:::: {#exr-eigenvalues-and-eigenvectors-c2}
[C2: Nilpotent operators]

An operator \( T \in \cL(V) \) is **nilpotent** if \( T^k = 0 \) for some integer \( k \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Let \( V \ne \{\0\} \) and \( T \) nilpotent. Prove that \( \spec(T) = \{0\} \). (No finite dimension is needed.)
2. Let \( \A \in M_n(\nC) \), \( n \ge 1 \), be nilpotent. Deduce that \( p_{\A}(x) = x^n \).
3. Let \( \A \in M_n(F) \), \( n \ge 1 \), be nilpotent. Prove that \( \I + \A \) is invertible.
:::
::::

::: {.solution}
(a) Let \( T\v = \lambda\v \) with \( \v \ne \0 \). By @exr-eigenvalues-and-eigenvectors-b3 (a), \( \0 = T^k\v = \lambda^k\v \), so \( \lambda^k = 0 \) by @thm-zero-product, and hence \( \lambda = 0 \) (a product of non-zero elements of a field is non-zero, @thm-field-basic-properties). So \( \spec(T) \subseteq \{0\} \). Conversely, \( T^k = 0 \) is not injective on \( V \ne \{\0\} \); if \( T \) were injective, so would be the composite \( T^k \) (@thm-composition-preserves). So \( \ker T \ne \{\0\} \), and \( 0 \in \spec(T) \).

(b) By @cor-complex-polynomial-splits and @thm-charpoly-coefficients, \( p_{\A} = (x - z_1)\cdots(x - z_n) \) for some \( z_i \in \nC \). Each \( z_i \) is a root of \( p_{\A} \), hence an eigenvalue of \( \A \) by @thm-eigenvalue-characterizations, hence \( z_i = 0 \) by (a). So \( p_{\A} = x^n \).

(c) By @thm-invertible-tfae-eigen, it suffices to show \( 0 \notin \spec(\I + \A) \). Suppose \( (\I + \A)\v = \0 \) with \( \v \ne \0 \). Then \( \A\v = -\v \), so \( -1 \in \spec(\A) \). By (a), \( \spec(\A) = \{0\} \), but \( -1 \ne 0 \) in every field. This contradiction shows that \( \I + \A \) is invertible.
:::

:::: {#exr-eigenvalues-and-eigenvectors-c3}
[C3: Real matrices of odd size]

::: {.enumerate options="label=(\alph*)"}
1. Prove that every \( \A \in M_n(\nR) \) with \( n \) odd has a real eigenvalue.
2. Deduce that every operator on a real vector space of dimension \( 3 \) has an invariant line.
3. Show that (a) fails for \( n = 4 \): find \( \A \in M_4(\nR) \) with no real eigenvalue.
:::
::::

::: {.solution}
(a) By @thm-charpoly-coefficients, \( p_{\A} \in \nR[x] \) is monic of degree \( n \), which is odd. By @cor-odd-degree-real-root, \( p_{\A}(\lambda) = 0 \) for some \( \lambda \in \nR \), and \( \lambda \) is an eigenvalue of \( \A \) by @thm-eigenvalue-characterizations.

(b) Let \( \dim V = 3 \) over \( \nR \) and \( T \in \cL(V) \). Choose a basis \( \sB \). By (a), the real matrix \( [T]_{\sB} \) has a real eigenvalue \( \lambda \), which is a root of \( p_{[T]_{\sB}} = p_T \) (@thm-eigenvalue-characterizations, @def-charpoly-operator). So \( \lambda \) is an eigenvalue of \( T \), again by @thm-eigenvalue-characterizations, and \( T \) has an eigenvector \( \v \) for it. By @prp-one-dimensional-invariant, \( \Span(\v) \) is invariant.

(c) Let \( \R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \) and \( \A = \R \oplus \R \in M_4(\nR) \). Then \( x\I_4 - \A = (x\I_2 - \R) \oplus (x\I_2 - \R) \) is block diagonal, so by the block triangular determinant over \( \nR[x] \) (the remark after @thm-det-block-triangular), \( p_{\A} = p_{\R}^2 = (x^2 + 1)^2 \). For real \( \lambda \), \( (\lambda^2 + 1)^2 \ge 1 > 0 \), so \( p_{\A} \) has no real root, and \( \A \) has no real eigenvalue. The argument of (a) needs odd degree.
:::
