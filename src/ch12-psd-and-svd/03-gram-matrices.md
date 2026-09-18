# Gram Matrices

Chapter 10 attached to every list of vectors the matrix of its pairwise inner products and read three facts off it: it is Hermitian, its quadratic form is a squared length, and it is invertible exactly when the list is independent (@def-gram-matrix, @thm-gram-matrix-properties). One question was left standing. Given a square matrix, is it the Gram matrix of *something*? The answer is the shortest possible one: exactly when it is positive semidefinite. This section proves that, and then spends it twice — the determinant of a Gram matrix is a squared volume, and a ratio of two Gram determinants is a distance to a subspace.

Throughout, \( F = \nR \) or \( F = \nC \) and all inner product spaces are over \( F \). When the list must be named we write \( \G(\v_1, \dots, \v_k) \) for its Gram matrix, whose entries are \( \inner{\v_j}{\v_i} \) as in @def-gram-matrix.

## Which matrices are Gram matrices?

Half of the answer is already proved. By @thm-gram-matrix-properties (a) and (b), a Gram matrix \( \G \) is Hermitian and satisfies

\[
\x^{*}\G\x = \Big\lVert \sum_{j} x_j\v_j \Big\rVert^2 \ \ge\ 0
\]

for every \( \x \in F^k \). That is word for word the definition of positive semidefiniteness (@def-positive-semidefinite). So being positive semidefinite is **necessary**. The content of the next theorem is that nothing else is needed, and this is where the chapter's second signature move earns its keep: a positive semidefinite matrix factors as \( \B^{*}\B \), and the columns of \( \B \) are then the list we were looking for.

:::: {#thm-gram-iff-psd}
[Gram Matrices Are Exactly the Positive Semidefinite Matrices]

Let \( \G \in M_k(F) \). The following are equivalent.

::: {.enumerate options="label=(\alph*)"}
1. \( \G \) is the Gram matrix of some list of \( k \) vectors in some inner product space over \( F \);
2. \( \G \) is the Gram matrix of some list of \( k \) vectors in \( F^{r} \) with the standard inner product, where \( r = \rank \G \);
3. \( \G \succeq 0 \).
:::

Moreover the list is unique up to an isometry: if \( (\v_1, \dots, \v_k) \) in \( V \) and \( (\w_1, \dots, \w_k) \) in \( W \) have the same Gram matrix, then there is an isometry from \( \Span(\v_1, \dots, \v_k) \) onto \( \Span(\w_1, \dots, \w_k) \) carrying \( \v_j \) to \( \w_j \) for every \( j \).
::::

::: {.idea}
(a) \( \Rightarrow \) (c) is the display above. For (c) \( \Rightarrow \) (b), diagonalize: the spectral theorem writes \( \G = \U\D\U^{*} \) with \( \D \) diagonal and, by @thm-psd-characterizations, with non-negative diagonal. Then \( \D^{1/2}\U^{*} \) is a square root of \( \G \) in the \( \B^{*}\B \) sense, and its rows beyond the \( r \)-th are zero, so the columns already live in \( F^{r} \). For the uniqueness clause, the Gram matrix *is* the recipe for every inner product among the vectors, so the obvious map \( \sum a_j\v_j \mapsto \sum a_j\w_j \) has no choice but to preserve them; the only thing needing care is that it is well defined, and part (b) of @thm-gram-matrix-properties says precisely that.
:::

::: {.proof}
(b) \( \Rightarrow \) (a) is immediate, since \( F^{r} \) with the standard inner product is an inner product space.

(a) \( \Rightarrow \) (c). Let \( \G \) be the Gram matrix of \( (\v_1, \dots, \v_k) \). By @thm-gram-matrix-properties (a), \( \G^{*} = \G \), and by (b) of the same theorem \( \x^{*}\G\x = \lVert\sum_j x_j\v_j\rVert^2 \ge 0 \) for every \( \x \in F^k \). Hence \( \G \succeq 0 \) by @def-positive-semidefinite.

(c) \( \Rightarrow \) (b). Since \( \G \) is Hermitian, the spectral theorem for matrices gives a unitary \( \U \) and a diagonal \( \D \) with \( \G = \U\D\U^{*} \) (@cor-spectral-complex-matrix over \( \nC \); @cor-spectral-real-matrix over \( \nR \), with \( \U \) orthogonal and \( \D \) real). The diagonal entries of \( \D \) are the eigenvalues of \( \G \), so they are real and \( \ge 0 \) by @thm-psd-characterizations, and we may prescribe their order: let \( d_1, \dots, d_r > 0 \) and \( d_{r+1} = \dots = d_k = 0 \). Here \( r \) is the number of non-zero eigenvalues, which is \( \rank \G \), because \( \G \) and \( \D \) have the same rank.

Put \( \B = \D^{1/2}\U^{*} \in M_k(F) \), where \( \D^{1/2} = \diag(\sqrt{d_1}, \dots, \sqrt{d_k}) \). Then
\[
\B^{*}\B = \U\D^{1/2}\D^{1/2}\U^{*} = \U\D\U^{*} = \G ,
\]
using \( (\D^{1/2})^{*} = \D^{1/2} \). Rows \( r+1, \dots, k \) of \( \B \) are zero, since row \( p \) of \( \D^{1/2}\U^{*} \) is \( \sqrt{d_p} \) times row \( p \) of \( \U^{*} \). Let \( \B' \in M_{r \times k}(F) \) consist of the first \( r \) rows of \( \B \); deleting zero rows changes no entry of \( \B^{*}\B \), so \( (\B')^{*}\B' = \G \) as well. Let \( \v_1, \dots, \v_k \in F^{r} \) be the columns of \( \B' \). With the standard inner product \( \inner{\x}{\y} = \y^{*}\x \) on \( F^{r} \),
\[
\inner{\v_j}{\v_i} = \v_i^{*}\v_j = \big((\B')^{*}\B'\big)_{ij} = (\G)_{ij} ,
\]
so \( \G \) is the Gram matrix of \( (\v_1, \dots, \v_k) \).

*The uniqueness clause.* Let \( (\v_1, \dots, \v_k) \) in \( V \) and \( (\w_1, \dots, \w_k) \) in \( W \) both have Gram matrix \( \G \), and put \( U = \Span(\v_1, \dots, \v_k) \) and \( U' = \Span(\w_1, \dots, \w_k) \). Define \( T \colon U \to U' \) by
\[
T\Big(\sum_{j} a_j\v_j\Big) = \sum_{j} a_j\w_j .
\]
This is well defined: if \( \sum_j a_j\v_j = \sum_j b_j\v_j \), let \( \x \in F^k \) be the vector with entries \( x_j = a_j - b_j \); then @thm-gram-matrix-properties (b), applied to each list in turn, gives
\[
\Big\lVert \sum_{j} x_j\w_j \Big\rVert^2 = \x^{*}\G\x = \Big\lVert \sum_{j} x_j\v_j \Big\rVert^2 = 0 ,
\]
so \( \sum_j a_j\w_j = \sum_j b_j\w_j \). The same display with every \( b_j = 0 \) shows \( \norm{T\u} = \norm{\u} \) for every \( \u \in U \), so \( T \) is an isometry (@def-isometry); it is linear and surjective by its definition on spanning vectors. This proves the theorem.
:::

Three consequences are worth naming at once.

First, the corollary promised in Chapter 6 is now proved from the right principle. @cor-gram-determinant-nonnegative said that \( \det(\A\A\tp) \ge 0 \) for real \( \A \), with equality exactly when the rows of \( \A \) are dependent, and it proved this by writing the determinant as a sum of squares of minors. The structural reason is the theorem above: \( \A\A\tp \) is a Gram matrix, hence positive semidefinite, hence has non-negative eigenvalues, and its determinant is their product. Positivity of the determinant is not an accident of Cauchy–Binet; it is one shadow of a much stronger property, and the other shadows come free — **every** principal minor of a Gram matrix is \( \ge 0 \) too, since a principal submatrix of \( \G(\v_1, \dots, \v_k) \) is the Gram matrix of a sublist.

Second, the smallest space that can hold a realization of \( \G \) has dimension \( \rank \G \), and no smaller one will do: a list of \( k \) vectors in a space of dimension \( s \) has a Gram matrix of rank at most \( s \), because \( \G = \A^{*}\A \) for the \( s \times k \) coordinate matrix \( \A \) of the list and \( \rank(\A^{*}\A) = \rank \A \le s \) by @cor-rank-adjoint (b).

Third, the theorem is a free source of examples in both directions: any vectors at all produce a positive semidefinite table, and conversely positivity is a real constraint on a table of numbers — a stronger one than most readers expect.

::: {.warning}
**Plausible-looking symmetric tables need not be Gram matrices.** The condition is not "symmetric with non-negative diagonal", and it is not even "every \( 2 \times 2 \) principal minor is \( \ge 0 \)". Take
\[
\G = \begin{pmatrix} 5 & -3 & -3 \\ -3 & 5 & -3 \\ -3 & -3 & 5 \end{pmatrix} .
\]
Its three \( 2 \times 2 \) principal minors are all \( 25 - 9 = 16 > 0 \), so any two of the three vectors would be a legitimate pair. But \( \G(1,1,1)\tp = (-1, -1, -1)\tp \), so \( -1 \) is an eigenvalue and \( \G \not\succeq 0 \): no three vectors in any inner product space have this table. In words, three vectors of squared length \( 5 \) cannot be **pairwise** at an angle with cosine \( -3/5 \); two of them can.
:::

::: {.check}
Is the \( k \times k \) matrix with every entry equal to \( 1 \) a Gram matrix? If so, exhibit a list; if not, say which clause fails.
:::

::: {.solution}
It is. Take \( \v_1 = \dots = \v_k = \v \) for any unit vector \( \v \): then \( \inner{\v_j}{\v_i} = 1 \) for all \( i, j \). Consistently, the matrix has rank \( 1 \), and @thm-gram-iff-psd (b) predicts a realization in \( F^1 \); the list \( (1, 1, \dots, 1) \) in \( F \) is one.
:::

## The Gram determinant is a squared volume

Chapter 6 defined the volume of a parallelepiped spanned by \( n \) vectors of \( \nR^n \) as \( \lvert\det\rvert \) of the matrix of their coordinates (@def-parallelepiped-volume). That definition needs a **square** matrix, so it says nothing about two vectors in \( \nR^3 \). The missing notion was already present in Chapter 6's motivation, though: volume is base times height. Turning that into a definition costs one line, now that we have distances to subspaces.

::: {#def-k-volume}
[Volume of a list]

Let \( (\v_1, \dots, \v_k) \) be a list in an inner product space \( V \) over \( F \). Its **\( k \)-dimensional volume** \( \vol(\v_1, \dots, \v_k) \ge 0 \) is defined recursively by
\[
\vol(\v_1) = \norm{\v_1}, \qquad
\vol(\v_1, \dots, \v_k) = \vol(\v_1, \dots, \v_{k-1}) \cdot d(\v_k, U_{k-1}) ,
\]
where \( U_{k-1} = \Span(\v_1, \dots, \v_{k-1}) \) and \( d(\cdot, \cdot) \) is the distance of @def-distance-to-subspace.
:::

In words: the volume of the last vector's parallelepiped is the volume of the one below it, times the height of the last vector above the subspace the others span. For \( k = 2 \) this is base times height for a parallelogram, and it is \( 0 \) exactly when \( \v_2 \) lies on the line through \( \v_1 \).

\begin{center}
\begin{tikzpicture}[x={(1cm,0cm)}, y={(0.45cm,0.75cm)}, z={(0cm,1cm)},
                    scale=0.9, lab/.style={font=\small}]
  \fill[gray!8] (-1.2,-0.8,0) -- (6.4,-0.8,0) -- (6.4,3.5,0) -- (-1.2,3.5,0) -- cycle;
  \coordinate (O)  at (0,0,0);
  \coordinate (V1) at (4,0,0);
  \coordinate (V2) at (1,2.4,0);
  \coordinate (SM) at (5,2.4,0);
  \coordinate (FT) at (1,0,0);
  \fill[gray!30] (O) -- (V1) -- (SM) -- (V2) -- cycle;
  \draw[black!65] (O) -- (V1) -- (SM) -- (V2) -- cycle;
  \draw[dashed, thick] (V2) -- (FT);
  \draw[black!65] (1,0,0) -- (1.3,0,0) -- (1.3,0.3,0);
  \draw[very thick, ->] (O) -- (V1);
  \draw[very thick, ->] (O) -- (V2);
  \node[lab, below] at (3.4,0,0) {$\v_1$};
  \node[lab, left] at (0.9,2.3,0) {$\v_2$};
  \node[lab] at (2.1,0.85,0) {$d(\v_2, U_1)$};
  \node[lab, black!60] at (4.0,3.0,0) {$U = \Span(\v_1,\v_2)$};
  \node[lab, align=center] at (2.6,-1.7,0)
    {base times height: $\vol(\v_1,\v_2) = \norm{\v_1}\,d(\v_2, U_1)$};
\end{tikzpicture}
\end{center}

The recursion is easy to state and awkward to compute with, because each step needs a projection. The Gram determinant computes all of it at once.

::: {#lem-gram-bordered}
[Bordering a Gram matrix]

Let \( (\v_1, \dots, \v_k) \) be a list in an inner product space \( V \), let \( U = \Span(\v_1, \dots, \v_k) \), and let \( \w \in V \). Then
\[
\det \G(\v_1, \dots, \v_k, \w) = \det \G(\v_1, \dots, \v_k)\cdot d(\w, U)^2 .
\]
:::

::: {.idea}
Replace \( \w \) by \( \w - P_U\w \). That is a column operation on the *list*, and a column operation on the list is a congruence \( \G \mapsto \E^{*}\G\E \) on the Gram matrix, with \( \E \) unitriangular, so the determinant does not move. After the replacement the last vector is orthogonal to all the others, and the Gram matrix has become block diagonal.
:::

::: {.proof}
First record how the Gram matrix responds to a change of list. If \( \u_j = \sum_t e_{tj}\v_t \) for a matrix \( \E = (e_{tj}) \), then by sesquilinearity
\[
\inner{\u_j}{\u_i} = \sum_{t}\sum_{s} e_{tj}\conj{e_{si}}\inner{\v_t}{\v_s} ,
\]
which is the \( (i, j) \)-entry of \( \E^{*}\G\E \); that is, \( \G(\u_1, \dots, \u_m) = \E^{*}\G(\v_1, \dots, \v_k)\E \).

Now write \( \w = \p + \h \) with \( \p = P_U\w \in U \) and \( \h = \w - \p \in U^{\perp} \), which is possible by @thm-orthogonal-decomposition (a). Since \( \p \in U \), there are scalars \( c_1, \dots, c_k \) with \( \p = \sum_t c_t\v_t \). Let \( \E \in M_{k+1}(F) \) be the identity matrix with its last column replaced by \( (-c_1, \dots, -c_k, 1) \). Applying the rule above to the list \( (\v_1, \dots, \v_k, \w) \) and this \( \E \) turns it into \( (\v_1, \dots, \v_k, \h) \), so
\[
\G(\v_1, \dots, \v_k, \h) = \E^{*}\,\G(\v_1, \dots, \v_k, \w)\,\E .
\]
The matrix \( \E \) is triangular with ones on the diagonal, so \( \det \E = 1 \) by @thm-det-triangular, and \( \det(\E^{*}) = \conj{\det \E} = 1 \). By @thm-det-multiplicative the two Gram determinants are equal.

Finally, \( \h \in U^{\perp} \) gives \( \inner{\h}{\v_i} = \inner{\v_i}{\h} = 0 \) for every \( i \), so
\[
\G(\v_1, \dots, \v_k, \h) =
\begin{pmatrix} \G(\v_1, \dots, \v_k) & \0 \\ \0 & \norm{\h}^2 \end{pmatrix},
\]
whose determinant is \( \det \G(\v_1, \dots, \v_k)\cdot\norm{\h}^2 \) by cofactor expansion along the last row. Since \( \norm{\h} = \norm{\w - P_U\w} = d(\w, U) \) by @def-distance-to-subspace, this proves the lemma.
:::

The recursion names the vectors in a particular order, and the last one plays a special role. The value does not depend on that choice: @thm-gram-determinant-volume below identifies \( \vol(\v_1, \dots, \v_k)^2 \) with \( \det\G \), and permuting the list permutes the rows of \( \G \) and the columns in the same way, which leaves the determinant unchanged (@thm-det-row-operations (a) applied once to the rows and once to the columns, so the two sign changes cancel). So the volume is an invariant of the list as a set of vectors, and we are free to order it however a computation prefers.

::: {#thm-gram-determinant-volume}
[The Gram Determinant Is the Squared Volume]

Let \( (\v_1, \dots, \v_k) \) be a list in an inner product space over \( F \). Then
\[
\det \G(\v_1, \dots, \v_k) = \vol(\v_1, \dots, \v_k)^2 .
\]
In particular, if \( \A \in M_{m \times k}(F) \) has columns \( \v_1, \dots, \v_k \in F^m \), then \( \vol(\v_1, \dots, \v_k) = \sqrt{\det(\A^{*}\A)} \).
:::

::: {.proof}
Induction on \( k \). For \( k = 1 \), \( \G(\v_1) = (\norm{\v_1}^2) \) and \( \vol(\v_1) = \norm{\v_1} \).

Let \( k \ge 2 \) and assume the statement for \( k - 1 \). With \( U_{k-1} = \Span(\v_1, \dots, \v_{k-1}) \), @lem-gram-bordered and then the induction hypothesis give
\[
\begin{aligned}
\det \G(\v_1, \dots, \v_k)
&= \det \G(\v_1, \dots, \v_{k-1})\cdot d(\v_k, U_{k-1})^2 \\
&= \vol(\v_1, \dots, \v_{k-1})^2 \cdot d(\v_k, U_{k-1})^2 ,
\end{aligned}
\]
and the right-hand side is \( \vol(\v_1, \dots, \v_k)^2 \) by @def-k-volume.

For the last claim, \( \inner{\v_j}{\v_i} = \v_i^{*}\v_j = (\A^{*}\A)_{ij} \) in \( F^m \) with the standard inner product, so \( \G(\v_1, \dots, \v_k) = \A^{*}\A \), and the volume is the non-negative square root of its determinant.
:::

Two checks that the definition is the right one. If \( k = m \) and \( F = \nR \), then \( \A \) is square and \( \det(\A\tp\A) = (\det\A)^2 \) by @thm-det-multiplicative and @thm-det-transpose, so \( \vol(\v_1, \dots, \v_m) = \lvert\det\A\rvert \): @def-k-volume agrees with @def-parallelepiped-volume whenever both apply. And for \( k = 2 \) in \( \nR^3 \), @exr-orientation-and-volume-c1 *defined* the area of a parallelogram in space to be \( \sqrt{\det(\A\tp\A)} \) and promised a justification from inner products; the theorem is that justification, since base times height is what an area should be.

The volume vanishes exactly when the list is dependent, which is @thm-gram-matrix-properties (d) read through the theorem: a flat parallelepiped has no volume.

## Distance to a subspace, by determinants

Dividing in @lem-gram-bordered gives a formula for a distance with no projection in sight.

::: {#thm-gram-distance-formula}
[Distance by Gram Determinants]

Let \( U \) be a finite-dimensional subspace of an inner product space \( V \), let \( (\v_1, \dots, \v_k) \) be a **basis** of \( U \), and let \( \w \in V \). Then
\[
d(\w, U)^2 = \frac{\det \G(\v_1, \dots, \v_k, \w)}{\det \G(\v_1, \dots, \v_k)} .
\]
:::

::: {.proof}
The list \( (\v_1, \dots, \v_k) \) is independent, so \( \det \G(\v_1, \dots, \v_k) > 0 \) by @thm-gram-matrix-properties (d) and the quotient is defined. Dividing the identity of @lem-gram-bordered by it gives the formula.
:::

No orthonormal basis, no Gram–Schmidt and no projection: two determinants and a division. The price is a \( (k+1) \times (k+1) \) determinant in the numerator, so for large \( k \) the projection route of Chapter 10 is faster. The quotient is also a ratio of squared volumes, \( \vol(\v_1, \dots, \v_k, \w)^2/\vol(\v_1, \dots, \v_k)^2 \): volume over base area, which is the height.

:::: {#exm-gram-distance-plane}
[The same distance twice]

In \( \nR^3 \) with the dot product, let \( U = \{(x, y, z) : x + y + z = 0\} \) and \( \w = (1, 2, 3) \). Compute \( d(\w, U) \) by @thm-gram-distance-formula, and compare with @exm-distance-to-plane.
::::

::: {.solution}
The vectors \( \v_1 = (1, -1, 0) \) and \( \v_2 = (0, 1, -1) \) lie in \( U \) and are independent, and \( \dim U = 2 \), so they are a basis of \( U \). Their inner products are \( \inner{\v_1}{\v_1} = 2 \), \( \inner{\v_2}{\v_2} = 2 \), \( \inner{\v_1}{\v_2} = -1 \), and with \( \w \): \( \inner{\w}{\w} = 14 \), \( \inner{\w}{\v_1} = 1 - 2 = -1 \), \( \inner{\w}{\v_2} = 2 - 3 = -1 \). Hence
\[
\G(\v_1, \v_2) = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}, \qquad
\G(\v_1, \v_2, \w) = \begin{pmatrix} 2 & -1 & -1 \\ -1 & 2 & -1 \\ -1 & -1 & 14 \end{pmatrix} .
\]
The first determinant is \( 4 - 1 = 3 \). Expanding the second along the first row,
\[
2(28 - 1) + 1(-14 - 1) - 1(1 + 2) = 54 - 15 - 3 = 36 .
\]
So \( d(\w, U)^2 = 36/3 = 12 \) and \( d(\w, U) = 2\sqrt3 \). @exm-distance-to-plane obtained \( \norm{(2,2,2)} = 2\sqrt3 \) by projecting onto the normal line. The two routes never meet on the page, and they agree.
:::

::: {.remark}
The numerator \( 36 \) is the squared volume of the parallelepiped on \( \v_1, \v_2, \w \), and the denominator \( 3 \) is the squared area of its base. The determinant of the coordinate matrix of \( (\v_1, \v_2, \w) \) is \( 6 \), and indeed \( 6^2 = 36 \): @thm-gram-determinant-volume in the square case.
:::

## Exercises

### A. Check your understanding

:::: {#exr-gram-matrices-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the criterion for a matrix \( \G \in M_k(F) \) to be the Gram matrix of some list of vectors.
2. Determine whether the following statement is correct, and justify your answer: every symmetric matrix with non-negative entries is a Gram matrix.
3. A list of \( 5 \) vectors in \( \nR^3 \) has a \( 5 \times 5 \) Gram matrix. What are the possible values of its rank, and what is its determinant?
4. Write down the formula for \( d(\w, U) \) in terms of Gram determinants, saying what list is used.
5. Define the \( k \)-dimensional volume of a list, and say what @thm-gram-determinant-volume asserts about it.
:::
::::

::: {.solution}
(a) \( \G \) is a Gram matrix if and only if \( \G \succeq 0 \) (@thm-gram-iff-psd). The list may then be taken in \( F^{r} \) with \( r = \rank\G \).

(b) Incorrect. \( \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix} \) has non-negative entries and eigenvalues \( 3 \) and \( -1 \), so it is not positive semidefinite and by @thm-gram-iff-psd it is no Gram matrix. (Concretely: two unit vectors cannot have inner product \( 2 \), by Cauchy–Schwarz, @thm-cauchy-schwarz.)

(c) The rank is \( \rank \G = \dim\Span(\v_1, \dots, \v_5) \le 3 \), so it is \( 0, 1, 2 \) or \( 3 \); in particular \( \G \) is singular and \( \det \G = 0 \). (A list of \( 5 \) vectors in a \( 3 \)-dimensional space is dependent, so @thm-gram-matrix-properties (d) gives \( \det \G = 0 \) directly.)

(d) If \( (\v_1, \dots, \v_k) \) is a **basis** of \( U \), then
\[
d(\w, U)^2 = \frac{\det\G(\v_1, \dots, \v_k, \w)}{\det\G(\v_1, \dots, \v_k)}
\]
by @thm-gram-distance-formula.

(e) \( \vol(\v_1) = \norm{\v_1} \) and \( \vol(\v_1, \dots, \v_k) = \vol(\v_1, \dots, \v_{k-1})\,d(\v_k, \Span(\v_1, \dots, \v_{k-1})) \) (@def-k-volume). @thm-gram-determinant-volume says \( \det\G(\v_1, \dots, \v_k) = \vol(\v_1, \dots, \v_k)^2 \).
:::

### B. Practice

:::: {#exr-gram-matrices-b1}
[B1: Which are Gram matrices?]

Determine which of the following are Gram matrices of some list of vectors in some real inner product space. For those that are, exhibit a list; for those that are not, give a reason.

::: {.enumerate options="label=(\roman*)"}
1. \( \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \)
2. \( \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \)
3. \( \begin{pmatrix} 2 & -1 & -1 \\ -1 & 2 & -1 \\ -1 & -1 & 2 \end{pmatrix} \)
4. \( \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix} \)
:::
::::

::: {.solution}
(i) Yes. It is symmetric with eigenvalues \( 1 \) and \( 3 \), both \( > 0 \), so it is positive definite and @thm-gram-iff-psd applies. A list: \( \v_1 = (1, 1, 0) \), \( \v_2 = (1, 0, 1) \) in \( \nR^3 \), whose Gram matrix is exactly this.

(ii) No. It is not symmetric, so it is not Hermitian and @def-positive-semidefinite fails at once; a Gram matrix over \( \nR \) is symmetric by @thm-gram-matrix-properties (a).

(iii) Yes. Its rank is \( 2 \): the rows sum to zero, and the top-left \( 2 \times 2 \) minor is \( 3 \ne 0 \). Its eigenvalues are \( 0 \) (eigenvector \( (1,1,1) \)) and \( 3 \) (twice, on the plane \( x + y + z = 0 \)), all \( \ge 0 \). A list in \( \nR^2 \), as @thm-gram-iff-psd (b) promises with \( r = 2 \): the three vectors \( (\sqrt2, 0) \), \( (-\tfrac{1}{\sqrt2}, \sqrt{\tfrac32}) \), \( (-\tfrac{1}{\sqrt2}, -\sqrt{\tfrac32}) \), three vectors of length \( \sqrt2 \) at \( 120^{\circ} \) to each other.

(iv) No. It is symmetric, but its leading principal minors are \( 1, 1, -1 \), and the determinant of a positive semidefinite matrix is \( \ge 0 \) (its eigenvalues are \( \ge 0 \)). So it is not positive semidefinite, and by @thm-gram-iff-psd it is not a Gram matrix. (Its eigenvalues are \( 1 \) and \( 1 \pm \sqrt2 \), one of which is negative.)
:::

:::: {#exr-gram-matrices-b2}
[B2: A volume two ways]

In \( \nR^3 \), let \( \v_1 = (1,1,0) \), \( \v_2 = (1,0,1) \), \( \v_3 = (0,1,1) \). Compute \( \vol(\v_1, \v_2, \v_3) \) with @thm-gram-determinant-volume, and check the answer against @def-parallelepiped-volume.
::::

::: {.solution}
The pairwise dot products give
\[
\G = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix},
\]
and expanding along the first row, \( \det\G = 2(4-1) - 1(2-1) + 1(1-2) = 6 - 1 - 1 = 4 \). By @thm-gram-determinant-volume, \( \vol(\v_1,\v_2,\v_3) = \sqrt4 = 2 \).

Directly, the matrix \( \A \) with these columns has \( \det \A = 1(0-1) - 1(1-0) + 0 = -2 \), so @def-parallelepiped-volume gives \( \lvert -2\rvert = 2 \). The two agree, as they must, since \( \det(\A\tp\A) = (\det\A)^2 \).
:::

:::: {#exr-gram-matrices-b3}
[B3: A distance in \( \nR^4 \)]

In \( \nR^4 \) with the dot product, let \( U = \Span\big((1,1,0,0), (0,1,1,0)\big) \) and \( \w = (1,0,0,1) \). Find \( d(\w, U) \) using @thm-gram-distance-formula.
::::

::: {.solution}
Write \( \v_1 = (1,1,0,0) \) and \( \v_2 = (0,1,1,0) \); they are independent, hence a basis of \( U \). The inner products are \( \inner{\v_1}{\v_1} = \inner{\v_2}{\v_2} = 2 \), \( \inner{\v_1}{\v_2} = 1 \), \( \inner{\w}{\w} = 2 \), \( \inner{\w}{\v_1} = 1 \), \( \inner{\w}{\v_2} = 0 \). So
\[
\G(\v_1, \v_2) = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}, \qquad
\G(\v_1, \v_2, \w) = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 0 \\ 1 & 0 & 2 \end{pmatrix},
\]
with determinants \( 3 \) and \( 2(4) - 1(2) + 1(-2) = 4 \). Hence \( d(\w, U)^2 = 4/3 \) and \( d(\w, U) = 2/\sqrt3 \).

*Check.* The projection is \( P_U\w = \tfrac13(2, 1, -1, 0) \), so \( \w - P_U\w = \tfrac13(1, -1, 1, 3) \), of norm \( \tfrac13\sqrt{12} = 2/\sqrt3 \).
:::

### C. Going deeper

:::: {#exr-gram-matrices-c1}
[C1: Rank of a Gram matrix]

Let \( (\v_1, \dots, \v_k) \) be a list in a finite-dimensional inner product space \( V \) over \( F \), with Gram matrix \( \G \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \rank \G = \dim\Span(\v_1, \dots, \v_k) \).
2. Deduce @thm-gram-matrix-properties (c): \( \G \) is invertible if and only if the list is independent.
:::

*Hint for (a): the coordinate matrix of the list in an orthonormal basis of the span.*
::::

::: {.solution}
(a) Let \( U = \Span(\v_1, \dots, \v_k) \), \( r = \dim U \), and let \( (\e_1, \dots, \e_r) \) be an orthonormal basis of \( U \), which exists by @thm-gram-schmidt. Let \( \A \in M_{r \times k}(F) \) have as its \( j \)-th column the coordinate vector of \( \v_j \). As computed in the proof of @thm-gram-matrix-properties (d), \( \G = \A^{*}\A \). By @cor-rank-adjoint (b), \( \rank\G = \rank(\A^{*}\A) = \rank\A \). Finally \( \rank\A = r \): the columns of \( \A \) span \( F^{r} \), because the coordinate map \( U \to F^{r} \) is an isomorphism carrying the spanning list \( (\v_1, \dots, \v_k) \) of \( U \) to the columns of \( \A \).

(b) \( \G \) is a \( k \times k \) matrix, so it is invertible if and only if \( \rank\G = k \) (@thm-invertible-tfae). By (a) that says \( \dim\Span(\v_1, \dots, \v_k) = k \), which holds exactly when the list is independent.
:::

:::: {#exr-gram-matrices-c2}
[C2: Why the conjugate is not optional]

Over \( \nC \), one might try to build a table of inner products with the **bilinear** expression \( \v_i\tp\v_j \), without any conjugate. Let \( \v = (1, i) \in \nC^2 \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \v\tp\v \) and \( \v^{*}\v \), and explain why only one of them is a legitimate squared length.
2. The list \( (\v) \) is independent, yet the \( 1 \times 1 \) "bilinear Gram matrix" \( (\v\tp\v) \) is singular. Which hypothesis of @thm-gram-iff-psd is being violated, and which statement of Chapter 6 does this illustrate?
:::
::::

::: {.solution}
(a) \( \v\tp\v = 1^2 + i^2 = 0 \), while \( \v^{*}\v = \lvert 1\rvert^2 + \lvert i\rvert^2 = 2 \). A squared length must be \( \ge 0 \) and must vanish only for the zero vector (@def-inner-product), and \( \v \ne \0 \); so \( \v\tp\v \) cannot be one, and \( \v^{*}\v = \norm{\v}^2 \) is the correct value.

(b) @thm-gram-iff-psd is a statement about the Gram matrix of @def-gram-matrix, whose entries are \( \inner{\v_j}{\v_i} = \v_i^{*}\v_j \). The matrix \( (\v\tp\v) = (0) \) is not that matrix, so the theorem simply does not apply; the genuine Gram matrix here is \( (2) \), which is positive definite, as it must be for an independent list. This is exactly the failure recorded after @cor-gram-determinant-nonnegative: over \( \nC \), \( \A = \begin{pmatrix} 1 & i \end{pmatrix} \) has rank \( 1 \) while \( \A\A\tp = (0) \), so the real equality case of that corollary has no complex analogue — unless the transpose is replaced by the conjugate transpose.
:::

:::: {#exr-gram-matrices-c3}
[C3: Height and volume]

Let \( (\v_1, \dots, \v_k) \) be an independent list in an inner product space over \( F \). For each \( j \), write \( U_j \) for the span of \( \v_1, \dots, \v_j \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \vol(\v_1, \dots, \v_k) \le \norm{\v_1}\norm{\v_2}\cdots\norm{\v_k} \), with equality if and only if the list is orthogonal.
2. Deduce that \( \det\G(\v_1, \dots, \v_k) \le \norm{\v_1}^2\cdots\norm{\v_k}^2 \).
:::

*Hint for (a): compare each height with the corresponding length.*
::::

::: {.solution}
(a) Fix \( j \ge 2 \) and write \( \v_j = P_{U_{j-1}}\v_j + \h_j \) with \( \h_j \in U_{j-1}^{\perp} \), as in @thm-orthogonal-decomposition (a). The two summands are orthogonal, so @thm-pythagoras gives
\[
\norm{\v_j}^2 = \norm{P_{U_{j-1}}\v_j}^2 + \norm{\h_j}^2 \ \ge\ \norm{\h_j}^2 = d(\v_j, U_{j-1})^2 ,
\]
with equality if and only if \( P_{U_{j-1}}\v_j = \0 \). Multiplying the \( k \) inequalities \( d(\v_j, U_{j-1}) \le \norm{\v_j} \) (with \( d(\v_1, U_0) \) read as \( \norm{\v_1} \)) and using @def-k-volume repeatedly gives
\[
\vol(\v_1, \dots, \v_k) \le \norm{\v_1}\cdots\norm{\v_k} .
\]
All factors are \( > 0 \), since the list is independent, so equality holds if and only if it holds in every factor, that is \( P_{U_{j-1}}\v_j = \0 \) for every \( j \ge 2 \). That says each \( \v_j \) is orthogonal to \( U_{j-1} \), hence to every earlier \( \v_i \); and conversely an orthogonal list has \( P_{U_{j-1}}\v_j = \0 \) by @thm-projection-formula (a).

(b) Square (a) and apply @thm-gram-determinant-volume.
:::
