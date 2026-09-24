# Projections Revisited

Chapter 4 built projections out of nothing but a direct sum: given \( V = U \oplus W \), the operator that keeps the \( U \)-piece and discards the \( W \)-piece satisfies \( P^2 = P \), and every operator satisfying \( P^2 = P \) arises this way. Chapter 11 built a second kind by taking \( W = U^{\perp} \), the orthogonal projection \( P_U \). The second is a special case of the first, and Chapter 4 left the comparison open, saying only that its projections "are often called **oblique** projections, to distinguish them from the orthogonal projections met later, in the chapters on inner product spaces". This section makes the distinction exact, measures how far an oblique projection is from being orthogonal, and closes Part III.

Throughout, \( V \) is a finite-dimensional inner product space over \( F = \nR \) or \( \nC \), and \( n = \dim V \).

## Which projections are orthogonal?

Two recollections, because the section is about the gap between them. From Chapter 2: an operator \( P \in \cL(V) \) with \( P^2 = P \) is a **projection**, also called an **idempotent** (@def-projection-operator); it satisfies \( V = \im P \oplus \ker P \), it is the identity on \( \im P \) and zero on \( \ker P \), and each splitting \( V = U \oplus W \) has exactly one projection with image \( U \) and kernel \( W \) (@thm-projection-direct-sum). No inner product appears there, and the field was arbitrary.

From Chapter 11: the splitting \( V = U \oplus U^{\perp} \) of @thm-orthogonal-decomposition is one of the many available, and \( P_U \) is the projection belonging to it (@def-orthogonal-projection). Chapter 4 warned that a subspace is the image of infinitely many projections, one per complement. Which one does the inner product pick out, and how is it recognized without being told the kernel?

*A projection is orthogonal exactly when it throws away perpendicularly — and that is the same as costing nothing to move across the inner product.*

::: {#thm-idempotent-orthogonal-iff-selfadjoint}
[Orthogonal Projections Among the Idempotents]

Let \( V \) be a finite-dimensional inner product space over \( F \) and let \( P \in \cL(V) \) satisfy \( P^2 = P \). The following are equivalent.

::: {.enumerate options="label=(\alph*)"}
1. \( P \) is the orthogonal projection onto its image: \( P = P_U \) with \( U = \im P \).
2. \( \ker P = (\im P)^{\perp} \).
3. \( P^{*} = P \).
4. \( P \) is normal.
5. \( \norm{P\v} \le \norm{\v} \) **for every** \( \v \in V \).
:::
:::

::: {.idea}
Conditions (a) and (b) say one thing twice, once about the operator and once about its two subspaces. Going from (b) to (c) is a computation Chapter 11 has already done for \( P_U \). Coming back from (c) is the four-subspaces theorem: \( \ker P^{*} \) is always \( (\im P)^{\perp} \), so once \( P^{*} = P \) the kernel is forced; normality is the same remark with \( \ker P^{*} \) replaced by \( \ker P \). The one direction with work in it is (e) \( \Rightarrow \) (b), where a bound on lengths has to become a statement about angles. Feed \( P \) a vector \( \u + t\w \) with \( \u \in \im P \) and \( \w \in \ker P \): its image is \( \u \) whatever \( t \) is, so choosing \( t \) to make \( \norm{\u + t\w} \) as small as possible squeezes \( \inner{\u}{\w} \) to zero.
:::

::: {.proof}
**(a) \( \Leftrightarrow \) (b).** Write \( U = \im P \). \( (\Rightarrow) \) If \( P = P_U \), then \( \ker P = \ker P_U = U^{\perp} \), since \( P_U \) is the projection onto \( U \) along \( U^{\perp} \) (@def-orthogonal-projection and @thm-projection-direct-sum (b)). \( (\Leftarrow) \) If \( \ker P = U^{\perp} \), then \( P \) is a projection with image \( U \) and kernel \( U^{\perp} \), and so is \( P_U \); by the uniqueness in @thm-projection-direct-sum (b), applied to \( V = U \oplus U^{\perp} \), the two are equal.

**(b) \( \Rightarrow \) (c).** By the equivalence just proved, \( P = P_U \) with \( U = \im P \). By @thm-projection-formula (b), \( \inner{P\u}{\v} = \inner{\u}{P\v} \) for all \( \u, \v \in V \). That is the defining identity of the adjoint, so \( P^{*} = P \) by the uniqueness in @def-adjoint.

**(c) \( \Rightarrow \) (d).** If \( P^{*} = P \) then \( P^{*}P = P^2 = PP^{*} \), which is @def-normal-operator.

**(d) \( \Rightarrow \) (b).** Since \( P \) is normal, \( \ker P = \ker P^{*} \) by @cor-normal-kernel (a). By @thm-four-subspaces-orthogonal (a), \( \ker P^{*} = (\im P)^{\perp} \). Combining the two gives (b).

**(b) \( \Rightarrow \) (e).** Let \( \v \in V \) and split it as \( \v = P\v + (\v - P\v) \). The first piece lies in \( \im P \), and the second lies in \( \ker P \), because \( P(\v - P\v) = P\v - P^2\v = \0 \). By (b) the two pieces are orthogonal, so @thm-pythagoras gives
\[
\norm{\v}^2 = \norm{P\v}^2 + \norm{\v - P\v}^2 \ge \norm{P\v}^2 ,
\]
and taking non-negative square roots gives \( \norm{P\v} \le \norm{\v} \).

**(e) \( \Rightarrow \) (b).** We first show \( \inner{\u}{\w} = 0 \) for every \( \u \in \im P \) and every \( \w \in \ker P \). There is nothing to prove when \( \w = \0 \), so assume \( \w \ne \0 \), write \( z = \inner{\u}{\w} \), and put
\[
t = -\frac{z}{\norm{\w}^2}, \qquad \v = \u + t\w ,
\]
which is legitimate because \( \norm{\w} \ne 0 \). Then \( P\v = P\u + tP\w = \u \), since \( P \) is the identity on \( \im P \) and zero on \( \ker P \) (@thm-projection-direct-sum (a)). Expanding the norm squared and using conjugate symmetry,
\[
\begin{aligned}
\norm{\v}^2 &= \norm{\u}^2 + \conj{t}\inner{\u}{\w} + t\inner{\w}{\u} + \lvert t\rvert^2\norm{\w}^2 \\
&= \norm{\u}^2 - \frac{\lvert z\rvert^2}{\norm{\w}^2} - \frac{\lvert z\rvert^2}{\norm{\w}^2} + \frac{\lvert z\rvert^2}{\norm{\w}^2}
= \norm{\u}^2 - \frac{\lvert z\rvert^2}{\norm{\w}^2} .
\end{aligned}
\]
Now (e) applied to this \( \v \) says \( \norm{\u}^2 = \norm{P\v}^2 \le \norm{\v}^2 \), which forces \( \lvert z\rvert^2 \le 0 \) and hence \( z = 0 \).

So \( \ker P \subseteq (\im P)^{\perp} \). The two subspaces have the same dimension: \( \dim\ker P = n - \rank P \) by @thm-rank-nullity, and \( \dim(\im P)^{\perp} = n - \dim\im P = n - \rank P \) by @thm-orthogonal-decomposition (c). A subspace contained in another of the same finite dimension equals it (@thm-dim-impl-eq), so \( \ker P = (\im P)^{\perp} \). This closes the cycle and proves the theorem.
:::

The theorem is the promised comparison. Every projection of Chapter 4 that is **not** self-adjoint is oblique, and now "oblique" has a precise meaning: its kernel is a complement of its image that is not the perpendicular one. Chapter 12 has already met a pair of such projections, in @exm-oblique-projections, and the Quick check after @thm-spectral-resolution-unique traced exactly what their obliqueness cost.

Clause (c) also settles Chapter 4's warning that "projection onto \( U \)" is incomplete information.

::: {#cor-orthogonal-idempotent-unique}
[One Orthogonal Projection per Subspace]

Let \( U \) be a subspace of a finite-dimensional inner product space \( V \). Among the projections of \( V \) with image \( U \) — one for each complement of \( U \), by @thm-projection-direct-sum — exactly one is self-adjoint, namely \( P_U \).
:::

::: {.proof}
\( P_U \) has image \( U \) and is self-adjoint by @thm-idempotent-orthogonal-iff-selfadjoint, (a) \( \Rightarrow \) (c). Conversely, let \( P \) be a self-adjoint projection with \( \im P = U \). By the same theorem, (c) \( \Rightarrow \) (b), \( \ker P = U^{\perp} \), which is also \( \ker P_U \). Two projections with the same image and the same kernel are equal, by the uniqueness in @thm-projection-direct-sum (b).
:::

Chapter 4's own example is now decided by inspection. On \( \nR^2 \) with the dot product, \( P(x, y) = (x, 0) \) and \( P'(x, y) = (x - y, 0) \) are both projections onto the \( x \)-axis, with standard matrices
\[
\P = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix},
\qquad
\P' = \begin{pmatrix} 1 & -1 \\ 0 & 0 \end{pmatrix} .
\]
The standard basis is orthonormal, so @thm-matrix-of-adjoint says self-adjointness is symmetry of these matrices. The first is symmetric, so \( P = P_U \) for the \( x \)-axis \( U \). The second is not, so \( P' \) is oblique — as the picture in Chapter 4 showed, it slides along the line \( y = x \) rather than straight down. Clause (e) fails visibly at \( \v = (1, -1) \): there \( P'\v = (2, 0) \), and \( \norm{P'\v} = 2 \) while \( \norm{\v} = \sqrt2 \).

::: {.check}
Does \( \A = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix} \) act on \( \nR^2 \) as a projection? If so, is it an orthogonal projection?
:::

::: {.solution}
\( \A^2 = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix} = \A \), so yes, it is a projection. Its image is the span of its columns, \( \Span((1, 1)) \), and its kernel is \( \Span(\e_2) \). Since \( \inner{(1, 1)}{\e_2} = 1 \ne 0 \), the kernel is not \( (\im \A)^{\perp} \), so the projection is oblique by @thm-idempotent-orthogonal-iff-selfadjoint (b). The quickest route is clause (c): \( \A\tp \ne \A \).
:::

::: {.warning}
**Clause (e) is a statement about every vector, and one vector proves nothing.** For the oblique \( \P' \) above, \( \norm{\P'\e_1} = 1 = \norm{\e_1} \) and \( \norm{\P'(1, 1)} = 0 \le \sqrt2 \); both are consistent with the bound, and both are worthless as evidence. The bound fails only in the direction \( (1, -1) \). If you want to certify a projection as orthogonal by hand, check \( \P^{*} = \P \) in an orthonormal basis, not the length of one image.
:::

::: {.warning}
**An orthogonal projection is almost never an orthogonal matrix.** If \( \P \) is unitary and idempotent, it is invertible, so multiplying \( \P^2 = \P \) by \( \P^{-1} \) gives \( \P = \I \). Apart from the identity, every orthogonal projection is singular. "Orthogonal" in \( P_U \) names the direction of the discarding, not membership in \( \Orth(n) \).
:::

## The block that measures obliqueness

Chapter 2 already knows the shape of a projection up to a change of basis: with a basis of \( \im P \) followed by a basis of \( \ker P \), the matrix is \( \diag(1, \dots, 1, 0, \dots, 0) \) with \( \rank P \) ones (@cor-projection-matrix). That basis is built to fit \( P \) and is usually not orthonormal, so the normal form erases exactly the information we now want. Insisting on an orthonormal basis costs one extra block, and that block is the answer.

::: {#thm-idempotent-canonical-form}
[Canonical Form of an Idempotent in an Orthonormal Basis]

Let \( V \) be an \( n \)-dimensional inner product space over \( F \) and let \( P \in \cL(V) \) be a projection of rank \( r \). Let \( (\f_1, \dots, \f_r) \) be any orthonormal basis of \( \im P \) and \( (\f_{r+1}, \dots, \f_n) \) any orthonormal basis of \( (\im P)^{\perp} \). Then \( \sB = (\f_1, \dots, \f_n) \) is an orthonormal basis of \( V \), and
\[
\mtx{P}{\sB}{\sB} = \begin{pmatrix} \I_r & \X \\ 0 & 0 \end{pmatrix}
\]
for some \( \X \in M_{r \times (n - r)}(F) \). Moreover \( P \) is an orthogonal projection if and only if \( \X = 0 \).
:::

::: {.idea}
Only two facts are used, and both are already proved. First, \( P \) fixes its image, so the first \( r \) columns are forced to be \( \e_1, \dots, \e_r \). Second, every output of \( P \) lies in \( \im P \), so the last \( n - r \) columns have nothing below row \( r \). What sits **above** row \( r \) in those columns is unconstrained, and that is \( \X \): it records where \( P \) sends the directions perpendicular to its image, which an orthogonal projection would send to \( \0 \).
:::

::: {.proof}
Write \( U = \im P \), so \( \dim U = r \) and \( \dim U^{\perp} = n - r \) by @thm-orthogonal-decomposition (c). Each \( \f_i \) with \( i \le r \) is orthogonal to each \( \f_j \) with \( j > r \), since the first lies in \( U \) and the second in \( U^{\perp} \); so \( \sB \) is an orthonormal list of \( n \) vectors, hence an orthonormal basis of \( V \) (@thm-orthogonal-independent).

For \( i \le r \) we have \( \f_i \in \im P \), so \( P\f_i = \f_i \) by @thm-projection-direct-sum (a), and column \( i \) of \( \mtx{P}{\sB}{\sB} \) is \( \e_i \). For \( j > r \) we have \( P\f_j \in \im P = U = \Span(\f_1, \dots, \f_r) \), so \( P\f_j = \sum_{i \le r} x_{ij}\f_i \) for scalars \( x_{ij} \in F \), and column \( j \) has zeros in rows \( r + 1, \dots, n \). Collecting the \( x_{ij} \) into \( \X \) gives the displayed shape.

For the last claim, \( \sB \) is orthonormal, so \( \mtx{P^{*}}{\sB}{\sB} = (\mtx{P}{\sB}{\sB})^{*} \) by @thm-matrix-of-adjoint, and
\[
(\mtx{P}{\sB}{\sB})^{*} = \begin{pmatrix} \I_r & 0 \\ \X^{*} & 0 \end{pmatrix} .
\]
The two matrices agree if and only if \( \X = 0 \). Since an operator is determined by its matrix in a basis, \( P^{*} = P \) if and only if \( \X = 0 \), and \( P^{*} = P \) says \( P \) is an orthogonal projection by @thm-idempotent-orthogonal-iff-selfadjoint.
:::

The block \( \X \) is not unique, because the two orthonormal bases were not. Replacing them changes \( \X \) into \( \A^{*}\X\B \) for some unitary \( \A \in M_r(F) \) and \( \B \in M_{n-r}(F) \), and that leaves the singular values of \( \X \) alone: since
\[
(\A^{*}\X\B)^{*}(\A^{*}\X\B) = \B^{*}(\X^{*}\X)\B ,
\]
the two matrices \( (\A^{*}\X\B)^{*}(\A^{*}\X\B) \) and \( \X^{*}\X \) are unitarily similar, so they have the same eigenvalues, and @def-singular-values reads the singular values off those. So the list \( \sigma_1(\X) \ge \sigma_2(\X) \ge \dots \) belongs to \( P \) itself, and \( P \) is an orthogonal projection exactly when that list is all zeros.

### The two-dimensional case, in full

Take \( n = 2 \) and \( r = 1 \), so that \( \X \) is a single scalar \( x \in F \), and
\[
\mtx{P}{\sB}{\sB} = \begin{pmatrix} 1 & x \\ 0 & 0 \end{pmatrix},
\qquad \sB = (\f_1, \f_2),
\]
with \( \f_1 \) spanning the line \( \im P \) and \( \f_2 \) spanning the perpendicular line \( (\im P)^{\perp} \). Everything about \( P \) can be read off this one number.

**The kernel.** \( P(a\f_1 + b\f_2) = (a + xb)\f_1 \), which is \( \0 \) exactly when \( a = -xb \). So
\[
\ker P = \Span(-x\f_1 + \f_2) ,
\]
a line that meets \( (\im P)^{\perp} = \Span(\f_2) \) only at \( \0 \) unless \( x = 0 \).

**The angle.** Suppose \( F = \nR \). The two lines \( \im P \) and \( \ker P \) are distinct, since their intersection is \( \{\0\} \); let \( \theta \in (0, \pi/2] \) be the angle between them, meaning the angle of @def-angle between \( \f_1 \) and whichever of \( \pm(-x\f_1 + \f_2) \) makes it acute. With \( \k = -x\f_1 + \f_2 \) we have \( \norm{\k} = \sqrt{1 + x^2} \) and \( \inner{\f_1}{\k} = -x \), so
\[
\cos\theta = \frac{\lvert x\rvert}{\sqrt{1 + x^2}},
\qquad
\sin\theta = \frac{1}{\sqrt{1 + x^2}},
\qquad
\lvert x \rvert = \cot\theta .
\]
The dictionary is complete: \( x = 0 \) is \( \theta = \pi/2 \), the orthogonal case; and as the kernel tips toward the image, \( \theta \to 0 \) and \( \lvert x\rvert \to \infty \). The single entry \( x \) **is** the obliqueness, in the units of a cotangent.

**The stretching.** For a unit vector \( \v = a\f_1 + b\f_2 \), we have \( \norm{P\v} = \lvert a + xb\rvert = \lvert\inner{(a, b)}{(1, \conj{x})}\rvert \) in \( F^2 \) with the standard inner product, so @thm-cauchy-schwarz gives
\[
\norm{P\v} \le \sqrt{1 + \lvert x\rvert^2} ,
\]
with equality exactly when \( (a, b) \) is a multiple of \( (1, \conj{x}) \), for instance \( (a, b) = (1, \conj{x})/\sqrt{1 + \lvert x\rvert^2} \). So the largest value of \( \norm{P\v} \) over unit vectors \( \v \) is \( \sqrt{1 + \lvert x\rvert^2} \), which over \( \nR \) is \( 1/\sin\theta \). Chapter 16 will give this number a name, the operator norm \( \norm{P} \); here it is enough to say that an orthogonal projection never lengthens a vector, while an oblique one lengthens some vector by \( 1/\sin\theta \), a factor that is unbounded as the kernel closes in on the image.

::: {#exm-oblique-projection-2x2}
[Two Oblique Projections, Measured]

For each of
\[
\P' = \begin{pmatrix} 1 & -1 \\ 0 & 0 \end{pmatrix},
\qquad
\Q = \begin{pmatrix} 2 & -1 \\ 2 & -1 \end{pmatrix}
\]
on \( \nR^2 \), verify that it is a projection, put it in the form of @thm-idempotent-canonical-form, and find the angle between its image and its kernel and the largest length of an image of a unit vector.
:::

::: {.solution}
*The matrix \( \P' \).* \( (\P')^2 = \P' \) by direct multiplication, and \( \im\P' = \Span(\e_1) \), \( \ker\P' = \Span((1, 1)) \). Here \( \f_1 = \e_1 \) already spans the image and \( \f_2 = \e_2 \) spans its perpendicular, and the standard basis is orthonormal, so the given matrix **is** the canonical form, with \( x = -1 \). Hence \( \cot\theta = 1 \), that is \( \theta = \pi/4 \), and the largest value of \( \norm{\P'\v} \) on the unit circle is \( \sqrt{1 + 1} = \sqrt2 \), attained at \( \v = (1, -1)/\sqrt2 \). Both readings match Chapter 4's figure, where \( \P' \) projects along the line \( y = x \).

*The matrix \( \Q \).* \( \Q^2 = \begin{pmatrix} 4 - 2 & -2 + 1 \\ 4 - 2 & -2 + 1\end{pmatrix} = \Q \), so \( \Q \) is a projection, of rank \( 1 \). Its image is \( \Span((1, 1)) \) and its kernel is \( \Span((1, 2)) \), since \( \Q(1, 2) = (0, 0) \). Take
\[
\f_1 = \tfrac{1}{\sqrt2}(1, 1), \qquad \f_2 = \tfrac{1}{\sqrt2}(1, -1),
\]
an orthonormal basis of \( \im\Q \) and of \( (\im\Q)^{\perp} \) respectively. Then \( \Q\f_1 = \f_1 \) and \( \Q\f_2 = \tfrac{1}{\sqrt2}(3, 3) = 3\f_1 \), so \( x = 3 \) and
\[
\mtx{T_{\Q}}{\sB}{\sB} = \begin{pmatrix} 1 & 3 \\ 0 & 0 \end{pmatrix} .
\]
Hence \( \cot\theta = 3 \). Checking against the two lines directly: the angle between \( (1, 1) \) and \( (1, 2) \) has \( \cos\theta = 3/\sqrt{10} \) and \( \sin\theta = 1/\sqrt{10} \), so \( \cot\theta = 3 \), and the largest value of \( \norm{\Q\v} \) on the unit circle is \( \sqrt{1 + 9} = \sqrt{10} = 1/\sin\theta \). The two routes agree.
:::

In higher rank the same block \( \X \) does the same job, and @exr-projections-revisited-c3 turns its largest singular value into the largest value of \( \norm{P\v} \) over unit \( \v \), by the argument that just ran in the \( 2 \times 2 \) case. The reason the singular values appear is the one this chapter has used throughout: \( \X \) is a rectangular matrix, so its eigenvalues do not exist, and @thm-svd is what measures it instead.

## Looking back at Part III

Part III added one piece of structure to the vector spaces of Parts I and II, and spent three chapters finding out what it buys.

**Chapter 11 added the inner product**, and with it length, orthogonality and angle. Orthonormal bases made coordinates free, orthogonal complements split every space canonically, and projection onto a subspace solved the nearest-point problem, hence least squares. Its deepest construction was the **adjoint**, the price of moving an operator from one slot of the inner product to the other; the adjoint is what turned the kernel and the image into two orthogonal pairs of subspaces.

**Chapter 12 asked which operators the inner product can diagonalize**, and the adjoint answered: over \( \nC \) the normal ones, over \( \nR \) the self-adjoint ones. Written without bases, the spectral theorem says \( T = \sum_i\lambda_iP_i \) with the \( P_i \) orthogonal projections onto the eigenspaces — which is why the present section had to exist, and why @thm-spectral-resolution needed clause (b) at all. Once a matrix is diagonal in an orthonormal basis, anything can be done to its eigenvalues and undone afterwards, and that is the functional calculus.

**Chapter 13 asked which self-adjoint operators behave like non-negative numbers**, collected the equivalent answers in @thm-psd-characterizations, and used them twice: to build the square root and the absolute value \( \lvert\A\rvert = (\A^{*}\A)^{1/2} \) of @def-matrix-absolute-value, and then to get past the restriction that had hung over the whole part. The spectral theorem needs a square operator, and most matrices are not square — but \( \A^{*}\A \) always **is** square, self-adjoint and positive semidefinite, whatever \( \A \) is. Applying the spectral theorem to it and reading the result back through \( \A \) gives @thm-svd, and with it orthonormal bases of all four fundamental subspaces (@cor-svd-four-subspaces), the polar decomposition of @thm-polar-decomposition, the best low-rank approximation and the pseudoinverse. A rectangular matrix has no eigenvalues; it has singular values, and they do the work.

So the part is one chain, each link an application of the last: **inner product \( \to \) adjoint \( \to \) spectral theorem \( \to \) singular value decomposition**. Its named moves travel. To show a vector is zero, pair it with itself. To move an operator across the inner product, pay with the adjoint. Work with the norm squared. Fix an orthonormal basis. Project, then subtract. Test positivity with the single scalar \( \inner{\A\x}{\x} \), and factor a positive matrix as \( \B^{*}\B \). Diagonalize, work on the eigenvalues, come back. When the matrix is not square, apply the spectral theorem to \( \A^{*}\A \). And when the answer is a sum ordered by size, truncate it.

What comes next takes the quadratic form \( \x \mapsto \inner{\A\x}{\x} \), which was only a test in this chapter, and makes it the object of study: Chapter 14 classifies forms up to congruence, by inertia, over \( \nR \) and over \( \nC \). Chapter 16 gives the operator norm promised twice above, and Chapter 17 characterizes the eigenvalues of a Hermitian matrix as maxima and minima of \( \inner{\A\x}{\x} \) — at which point the test becomes the theory.

## Exercises

### A. Check your understanding

::: {#exr-projections-revisited-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define what it means for \( P \in \cL(V) \) to be a projection, and what it means for it to be the orthogonal projection onto a subspace \( U \). Which of the two definitions needs an inner product?
2. State three conditions on a projection \( P \), each equivalent to "\( P \) is an orthogonal projection".
3. Determine whether the following is correct, and justify your answer: if \( \norm{P\v} \le \norm{\v} \) for some non-zero \( \v \), then the projection \( P \) is orthogonal.
4. Determine whether the following is correct, and justify your answer: every projection of rank \( r \) on an \( n \)-dimensional inner product space has matrix \( \I_r \oplus 0 \) in some orthonormal basis.
:::
:::

::: {.solution}
(a) \( P \) is a projection when \( P^2 = P \) (@def-projection-operator); \( P \) is the orthogonal projection onto \( U \) when it is the projection onto \( U \) along \( U^{\perp} \) (@def-orthogonal-projection). Only the second needs an inner product, since \( U^{\perp} \) is undefined without one.

(b) By @thm-idempotent-orthogonal-iff-selfadjoint: \( \ker P = (\im P)^{\perp} \); \( P^{*} = P \); \( P \) is normal; \( \norm{P\v} \le \norm{\v} \) for every \( \v \). Any three of these will do.

(c) Incorrect. Take \( \P' = \begin{psmallmatrix} 1 & -1 \\ 0 & 0\end{psmallmatrix} \) on \( \nR^2 \) and \( \v = (1, 1) \). Then \( \P'\v = \0 \), so \( \norm{\P'\v} = 0 \le \sqrt2 \), yet \( \P' \) is oblique because \( (\P')\tp \ne \P' \). Clause (e) of @thm-idempotent-orthogonal-iff-selfadjoint quantifies over **every** \( \v \).

(d) Incorrect in general, and correct exactly for the orthogonal projections. By @thm-idempotent-canonical-form the matrix in a suitable orthonormal basis is \( \begin{psmallmatrix} \I_r & \X \\ 0 & 0\end{psmallmatrix} \), and it is \( \I_r \oplus 0 \) only when \( \X = 0 \). If some orthonormal basis gave \( \I_r \oplus 0 \), that matrix would be Hermitian, so \( P \) would be self-adjoint by @thm-matrix-of-adjoint. The matrix \( \P' \) of part (c) is a counterexample. (In a basis that is merely a basis, \( \I_r \oplus 0 \) is always attainable: that is @cor-projection-matrix.)
:::

### B. Practice

::: {#exr-projections-revisited-b1}
[B1: Which are orthogonal projections?]

Determine which of the following matrices are projections, and among those, which are orthogonal projections. Justify your answer. For the oblique ones over \( \nR \), find the angle between image and kernel.

::: {.enumerate options="label=(\alph*)"}
1. \( \A = \frac{1}{5}\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} \) on \( \nR^2 \).
2. \( \B = \begin{pmatrix} 1 & 0 \\ -2 & 0 \end{pmatrix} \) on \( \nR^2 \).
3. \( \C = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \) on \( \nR^2 \).
4. \( \D = \begin{pmatrix} 1 & i \\ 0 & 0 \end{pmatrix} \) on \( \nC^2 \).
:::
:::

::: {.solution}
(a) \( \A^2 = \frac{1}{25}\begin{psmallmatrix} 5 & 10 \\ 10 & 20\end{psmallmatrix} = \A \), so \( \A \) is a projection, and \( \A\tp = \A \). By @thm-idempotent-orthogonal-iff-selfadjoint it is the orthogonal projection onto \( \im\A = \Span((1, 2)) \).

(b) \( \B^2 = \B \), so \( \B \) is a projection, but \( \B\tp \ne \B \), so it is oblique. Its image is \( \Span((1, -2)) \) and its kernel is \( \Span(\e_2) \). The angle between these lines has \( \cos\theta = \lvert\inner{(1, -2)}{(0, 1)}\rvert/(\sqrt5 \cdot 1) = 2/\sqrt5 \), so \( \sin\theta = 1/\sqrt5 \) and \( \cot\theta = 2 \); that is \( \theta = \arctan(1/2) \), about \( 26.6^{\circ} \).

(c) \( \C^2 = \begin{psmallmatrix} 2 & 2 \\ 2 & 2\end{psmallmatrix} = 2\C \ne \C \), so \( \C \) is not a projection at all, although it is symmetric. Symmetry alone is not idempotence; \( \frac12\C \) is the orthogonal projection onto \( \Span((1, 1)) \).

(d) \( \D^2 = \D \), so \( \D \) is a projection, and \( \D^{*} = \begin{psmallmatrix} 1 & 0 \\ -i & 0\end{psmallmatrix} \ne \D \), so it is oblique. It is already in the canonical form of @thm-idempotent-canonical-form, with \( x = i \). There is no angle over \( \nC \) (@def-angle is stated for real spaces), but \( \lvert x\rvert = 1 \), and the largest value of \( \norm{\D\v} \) over unit \( \v \) is \( \sqrt{1 + 1} = \sqrt2 \), the same number the real matrix \( \P' \) produced.
:::

::: {#exr-projections-revisited-b2}
[B2: Putting a projection in canonical form]

Let \( \A = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \) act on \( \nR^3 \) with the dot product.

::: {.enumerate options="label=(\alph*)"}
1. Verify that \( \A \) is a projection and find \( \im\A \) and \( \ker\A \).
2. Find an orthonormal basis \( \sB \) of \( \nR^3 \) as in @thm-idempotent-canonical-form and write down \( \mtx{T_{\A}}{\sB}{\sB} \).
3. Hence determine whether \( \A \) is an orthogonal projection, and find \( \rank\A \) without row reducing.
:::
:::

::: {.solution}
(a) \( \A^2 = \A \), by multiplying out: the second column of \( \A^2 \) is \( \A(1, 1, 0) = (1, 1, 0) \), and the first and third columns are \( \0 \) and \( \e_3 \), unchanged. The columns of \( \A \) span \( \im\A = \Span((1, 1, 0), \e_3) \), which is \( 2 \)-dimensional. And \( \A\x = (x_2, x_2, x_3) \) is \( \0 \) exactly when \( x_2 = x_3 = 0 \), so \( \ker\A = \Span(\e_1) \).

(b) \( \im\A \) has the orthonormal basis \( \f_1 = \frac{1}{\sqrt2}(1, 1, 0) \), \( \f_2 = \e_3 \), and \( (\im\A)^{\perp} = \Span((1, -1, 0)) \) has the orthonormal basis \( \f_3 = \frac{1}{\sqrt2}(1, -1, 0) \). Now \( \A\f_1 = \f_1 \) and \( \A\f_2 = \f_2 \), while
\[
\A\f_3 = \tfrac{1}{\sqrt2}(-1, -1, 0) = -\f_1 .
\]
Hence
\[
\mtx{T_{\A}}{\sB}{\sB} = \begin{pmatrix} 1 & 0 & -1 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix},
\qquad \X = \begin{pmatrix} -1 \\ 0 \end{pmatrix} .
\]

(c) \( \X \ne 0 \), so \( \A \) is oblique by @thm-idempotent-canonical-form; indeed \( \ker\A = \Span(\e_1) \) is not \( (\im\A)^{\perp} = \Span((1, -1, 0)) \). The rank is the number of ones in the canonical form, namely \( 2 \); equivalently \( \rank\A = \tr\A = 0 + 1 + 1 = 2 \) by @thm-rank-equals-trace-projection.
:::

::: {#exr-projections-revisited-b3}
[B3: The complementary projection]

Let \( P \in \cL(V) \) be a projection on a finite-dimensional inner product space, with \( U = \im P \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( P \) is an orthogonal projection if and only if \( \id_V - P \) is.
2. Prove that in that case \( \id_V - P = P_{U^{\perp}} \).
:::

*Hint: @exr-projections-and-trace-b2 identifies the image and the kernel of \( \id_V - P \).*
:::

::: {.solution}
(a) By @exr-projections-and-trace-b2 (a), \( \id_V - P \) is a projection. By @thm-adjoint-properties (a), (b) and (d), \( (\id_V - P)^{*} = \id_V - P^{*} \). Hence \( (\id_V - P)^{*} = \id_V - P \) if and only if \( P^{*} = P \), and @thm-idempotent-orthogonal-iff-selfadjoint converts each side into the corresponding statement about orthogonal projections.

(b) Suppose \( P \) is an orthogonal projection. By @exr-projections-and-trace-b2 (b), \( \im(\id_V - P) = \ker P \), which is \( U^{\perp} \) by @thm-idempotent-orthogonal-iff-selfadjoint (b). By (a), \( \id_V - P \) is an orthogonal projection, so by clause (a) of that theorem it is the orthogonal projection onto its own image, that is \( P_{U^{\perp}} \).
:::

### C. Going deeper

::: {#exr-projections-revisited-c1}
[C1: Products of orthogonal projections]

Let \( P \) and \( Q \) be orthogonal projections on a finite-dimensional inner product space \( V \), with images \( U \) and \( W \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( PQ \) is an orthogonal projection if and only if \( PQ = QP \).
2. Suppose \( PQ = QP \). Prove that \( PQ = P_{U \cap W} \).
3. Give an explicit example of two orthogonal projections on \( \nR^2 \) whose product is not a projection.
:::
:::

::: {.solution}
(a) \( (\Leftarrow) \) Suppose \( PQ = QP \). Then \( (PQ)^2 = P(QP)Q = P(PQ)Q = P^2Q^2 = PQ \), so \( PQ \) is a projection, and \( (PQ)^{*} = Q^{*}P^{*} = QP = PQ \) by @thm-adjoint-properties (c) and self-adjointness of \( P \) and \( Q \). By @thm-idempotent-orthogonal-iff-selfadjoint, \( PQ \) is an orthogonal projection.

\( (\Rightarrow) \) Suppose \( PQ \) is an orthogonal projection. Then \( PQ = (PQ)^{*} = Q^{*}P^{*} = QP \).

(b) Assume \( PQ = QP \), so \( PQ \) is an orthogonal projection by (a), and by clause (a) of @thm-idempotent-orthogonal-iff-selfadjoint it equals \( P_{\im(PQ)} \). It remains to show \( \im(PQ) = U \cap W \). \( (\subseteq) \) Every value \( PQ\v \) lies in \( \im P = U \); and \( PQ\v = QP\v \) lies in \( \im Q = W \). \( (\supseteq) \) If \( \v \in U \cap W \), then \( Q\v = \v \) and \( P\v = \v \), since a projection fixes its image (@thm-projection-direct-sum (a)), so \( PQ\v = \v \) and \( \v \in \im(PQ) \).

(c) Project onto the \( x \)-axis and onto the line \( y = x \), with standard matrices
\[
\P = \begin{pmatrix} 1 & 0 \\ 0 & 0\end{pmatrix},
\qquad
\Q = \tfrac12\begin{pmatrix} 1 & 1 \\ 1 & 1\end{pmatrix} .
\]
Both are symmetric and idempotent, hence orthogonal projections. But \( \P\Q = \frac12\begin{psmallmatrix} 1 & 1 \\ 0 & 0\end{psmallmatrix} \) and \( (\P\Q)^2 = \frac14\begin{psmallmatrix} 1 & 1 \\ 0 & 0\end{psmallmatrix} \ne \P\Q \), so the product is not even a projection. Consistently with (a), \( \Q\P = \frac12\begin{psmallmatrix} 1 & 0 \\ 1 & 0\end{psmallmatrix} \ne \P\Q \).
:::

::: {#exr-projections-revisited-c2}
[C2: The Frobenius norm detects obliqueness]

Let \( \P \in M_n(F) \) be idempotent, of rank \( r \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \norm{\P}_F^2 \ge r \).
2. Prove that equality holds if and only if \( \P \) is an orthogonal projection.
:::

*Hint: the canonical form of @thm-idempotent-canonical-form, together with the invariance of the Frobenius norm under a unitary change of orthonormal basis.*
:::

::: {.solution}
Apply @thm-idempotent-canonical-form to the operator \( \x \mapsto \P\x \) on \( F^n \), and let \( \U \) be the matrix whose columns are the vectors of the orthonormal basis it produces. Then \( \U \) is unitary (@thm-isometry-characterizations (f)), and the change-of-basis formula gives
\[
\U^{*}\P\U = \U^{-1}\P\U = \begin{pmatrix} \I_r & \X \\ 0 & 0 \end{pmatrix} .
\]
By @lem-frobenius-unitarily-invariant, \( \norm{\P}_F = \norm{\U^{*}\P\U}_F \).

(a) Summing the squared moduli of the entries of the block matrix,
\[
\norm{\P}_F^2 = \norm{\I_r}_F^2 + \norm{\X}_F^2 = r + \norm{\X}_F^2 \ge r ,
\]
since \( \norm{\X}_F^2 \ge 0 \).

(b) Equality holds if and only if \( \norm{\X}_F = 0 \), that is \( \X = 0 \), which by @thm-idempotent-canonical-form is exactly the condition that \( \P \) be an orthogonal projection. (Note that \( r = \rank\P = \tr\P \) by @thm-rank-equals-trace-projection, so the criterion may also be written \( \tr(\P^{*}\P) = \tr\P \).)
:::

::: {#exr-projections-revisited-c3}
[C3: How far an oblique projection can stretch]

Let \( P \) be a projection of rank \( r \) on an \( n \)-dimensional inner product space \( V \) over \( F \), with \( 0 < r < n \), and let \( \X \) be the block of @thm-idempotent-canonical-form, with largest singular value \( \sigma_1 = \sigma_1(\X) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \norm{\X\z} \le \sigma_1\norm{\z} \) for every \( \z \in F^{\,n-r} \), with equality for some \( \z \ne \0 \).
2. Prove that the largest value of \( \norm{P\v} \) over unit vectors \( \v \in V \) is \( \sqrt{1 + \sigma_1^2} \).
3. Deduce the two-dimensional formula \( \sqrt{1 + \lvert x\rvert^2} \) of the text, and state what the answer becomes when \( P \) is an orthogonal projection.
:::
:::

::: {.solution}
(a) Write \( \X = \U\vSigma\V^{*} \) as in @thm-svd, with \( \U, \V \) unitary, and let \( p \) be the length of the list of singular values. For \( \z \in F^{\,n-r} \) put \( \w = \V^{*}\z \), so that \( \norm{\w} = \norm{\z} \) and \( \norm{\X\z} = \norm{\vSigma\w} \), a unitary matrix preserving norms (@thm-isometry-characterizations). The vector \( \vSigma\w \) has entries \( \sigma_i w_i \) for \( i \le p \) and \( 0 \) beyond, so
\[
\norm{\vSigma\w}^2 = \sum_{i \le p} \sigma_i^2\lvert w_i\rvert^2 \le \sigma_1^2\sum_{i \le p}\lvert w_i\rvert^2 \le \sigma_1^2\norm{\w}^2 = \sigma_1^2\norm{\z}^2 ,
\]
since \( \sigma_1 \) is the largest of the \( \sigma_i \). Taking \( \z = \V\e_1 \), a unit vector, gives \( \w = \e_1 \) and \( \norm{\X\z} = \sigma_1 \), so the bound is attained.

(b) Use the orthonormal basis \( \sB \) of @thm-idempotent-canonical-form and write a vector of \( V \) by its coordinate vector \( (\y, \z) \) with \( \y \in F^r \) and \( \z \in F^{\,n-r} \); since \( \sB \) is orthonormal, @thm-orthonormal-coordinates (c) gives \( \norm{\v}^2 = \norm{\y}^2 + \norm{\z}^2 \), and \( P\v \) has coordinates \( (\y + \X\z, \0) \). By @cor-triangle-inequality, then (a), then @thm-cauchy-schwarz in \( \nR^2 \) applied to \( (\norm{\y}, \norm{\z}) \) and \( (1, \sigma_1) \),
\[
\begin{aligned}
\norm{P\v} = \norm{\y + \X\z} &\le \norm{\y} + \sigma_1\norm{\z} \\
&\le \sqrt{1 + \sigma_1^2}\,\sqrt{\norm{\y}^2 + \norm{\z}^2} = \sqrt{1 + \sigma_1^2}\,\norm{\v} .
\end{aligned}
\]
For equality, let \( \z_0 \) be the unit vector of (a), so \( \X\z_0 = \sigma_1\u_0 \) with \( \norm{\u_0} = 1 \) (take \( \u_0 = \X\z_0/\sigma_1 \) if \( \sigma_1 > 0 \); if \( \sigma_1 = 0 \) take any unit \( \u_0 \)). Put
\[
\y = \frac{\u_0}{\sqrt{1 + \sigma_1^2}}, \qquad \z = \frac{\sigma_1\z_0}{\sqrt{1 + \sigma_1^2}} .
\]
Then \( \norm{\y}^2 + \norm{\z}^2 = 1 \) and \( \y + \X\z = (1 + \sigma_1^2)\u_0/\sqrt{1 + \sigma_1^2} \), whose norm is \( \sqrt{1 + \sigma_1^2} \).

(c) When \( n = 2 \) and \( r = 1 \), \( \X \) is the \( 1 \times 1 \) matrix \( (x) \), whose only singular value is \( \lvert x\rvert \); the formula becomes \( \sqrt{1 + \lvert x\rvert^2} \). When \( P \) is an orthogonal projection, \( \X = 0 \), so \( \sigma_1 = 0 \) and the largest value is \( 1 \) — an orthogonal projection never lengthens a vector, which is clause (e) of @thm-idempotent-orthogonal-iff-selfadjoint with the sharpest constant.
:::
