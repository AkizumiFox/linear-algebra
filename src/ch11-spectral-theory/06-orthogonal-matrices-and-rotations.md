# The Shape of an Orthogonal Matrix

An orthogonal matrix is normal, so the real normal form of the previous section applies to it — and the extra information that an orthogonal matrix carries, that every eigenvalue has modulus \( 1 \), collapses that form into something very small. What comes out is a complete description of the rigid motions of \( \nR^n \) fixing the origin: a few axes reversed, and the rest of the space turned in independent two-dimensional planes. In dimension \( 3 \) this is the statement that every rotation has an axis, and we push it as far as an explicit formula for the rotation matrix in terms of its axis and angle.

Throughout, \( \nR^n \) carries the standard inner product, and \( \Q \) is a real matrix.

## From the real normal form to the canonical form

Two pieces of notation, both recalled. For \( \theta \in \nR \), Chapter 10 wrote
\[
\R_{\theta} = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}
\]
for the matrix that rotates the plane by \( \theta \) (@thm-orthogonal-2x2). It is exactly the rotation-scaling block of Chapter 9 for a complex number on the unit circle: \( \R_{\theta} = \vLambda(e^{i\theta}) \) in the notation of @def-real-jordan-block, since \( e^{i\theta} = \cos\theta + i\sin\theta \). And \( \A \oplus \B \) is the block diagonal matrix with diagonal blocks \( \A \) and \( \B \).

Now the observation that starts everything. If \( \Q \in \Orth(n) \) then \( \Q\tp\Q = \I_n = \Q\Q\tp \), so \( \Q \) commutes with its own adjoint: **every orthogonal matrix is normal**. So @thm-real-normal-form applies. All that remains is to say what the blocks can be, and for that we use the one thing an orthogonal matrix has that a general normal matrix does not.

::: {#thm-orthogonal-canonical-form}
[Canonical Form of an Orthogonal Matrix]

Let \( \Q \in \Orth(n) \). Then there are integers \( p, q, m \ge 0 \) with \( p + q + 2m = n \), and angles \( \theta_1, \dots, \theta_m \) with \( 0 < \theta_j < \pi \), and a matrix \( \P \in \Orth(n) \), such that
\[
\P\tp\Q\P = \I_p \oplus (-\I_q) \oplus \R_{\theta_1} \oplus \cdots \oplus \R_{\theta_m} .
\]
Moreover \( \det \Q = (-1)^q \), and \( p \), \( q \) and the multiset \( \{\theta_1, \dots, \theta_m\} \) are determined by \( \Q \).
:::

::: {.idea}
\( \Q \) is normal, so @thm-real-normal-form already hands us a block diagonal matrix with \( 1 \times 1 \) blocks \( [a] \) and \( 2 \times 2 \) blocks \( \vLambda(\lambda) \). The blocks are unconstrained for a general normal matrix; here they are not, because the eigenvalues of an isometry lie on the unit circle. A real eigenvalue on the unit circle is \( \pm 1 \), and a conjugate pair on the unit circle is \( e^{\pm i\theta} \), which turns the scaling block into a pure rotation. Then sort the \( \pm 1 \)s to the front.
:::

::: {.proof}
The operator \( T_{\Q} \) on \( \nR^n \) satisfies \( T_{\Q}^{*} = T_{\Q\tp} \) by @thm-matrix-of-adjoint, since the standard basis is orthonormal, so \( T_{\Q}^{*}T_{\Q} = T_{\Q\tp\Q} = \id \) and likewise in the other order. Hence \( T_{\Q} \) is normal (@def-normal-operator), and by @thm-real-normal-form there is an orthonormal basis \( \sB \) of \( \nR^n \) in which
\[
\mtx{T_{\Q}}{\sB}{\sB} = [a_1] \oplus \cdots \oplus [a_r] \oplus \vLambda(\lambda_1) \oplus \cdots \oplus \vLambda(\lambda_m),
\]
where \( a_i \in \nR \) and \( \lambda_j = c_j + d_ji \) with \( d_j > 0 \). Let \( \P \) be the matrix whose columns are the vectors of \( \sB \). Its columns are orthonormal, so \( \P \in \Orth(n) \) by @thm-isometry-characterizations (f), and \( \P\tp\Q\P = \P^{-1}\Q\P = \mtx{T_{\Q}}{\sB}{\sB} \) by @thm-change-of-basis-maps.

**The blocks.** A block diagonal matrix is triangular by blocks, so the eigenvalues of \( \mtx{T_{\Q}}{\sB}{\sB} \) over \( \nC \) are the \( a_i \) together with the roots of each \( \det(x\I_2 - \vLambda(\lambda_j)) = (x - c_j)^2 + d_j^2 \), namely \( \lambda_j \) and \( \conj{\lambda_j} \). Now \( \Orth(n) = \Unit(n) \cap M_n(\nR) \) by @prp-orthogonal-group-properties (a), so \( \Q \) is unitary, and every complex eigenvalue \( \lambda \) of \( \Q \) satisfies \( \lvert\lambda\rvert = 1 \) by @prp-isometry-eigenvalues-modulus-one applied to \( T_{\Q} \) on \( \nC^n \). Therefore \( a_i = \pm 1 \) for each \( i \), and \( c_j^2 + d_j^2 = 1 \) for each \( j \). Since \( c_j^2 + d_j^2 = 1 \) and \( d_j > 0 \), there is a unique \( \theta_j \in (0, \pi) \) with \( c_j = \cos\theta_j \) and \( d_j = \sin\theta_j \), and then \( \vLambda(\lambda_j) = \R_{\theta_j} \).

**Sorting.** Let \( p \) be the number of \( i \) with \( a_i = 1 \) and \( q \) the number with \( a_i = -1 \), so \( p + q + 2m = n \). Reordering the vectors of \( \sB \) so that the \( +1 \) blocks come first, then the \( -1 \) blocks, then the rotation blocks in pairs, leaves the basis orthonormal and permutes the diagonal blocks; the new \( \P \) is the old one with its columns permuted, still orthogonal. This gives the displayed form.

**The determinant and uniqueness.** By @thm-det-multiplicative and @cor-det-similarity-invariant, \( \det \Q = \det(\P\tp\Q\P) \), and the determinant of a block diagonal matrix is the product of the determinants of its blocks (@thm-det-block-triangular), which are \( 1 \), \( -1 \) and \( \det\R_{\theta_j} = \cos^2\theta_j + \sin^2\theta_j = 1 \). Hence \( \det\Q = (-1)^q \). Finally, similar matrices have the same eigenvalues with the same multiplicities, and reading the eigenvalues off the displayed form gives \( 1 \) with multiplicity \( p \), \( -1 \) with multiplicity \( q \), and the pairs \( e^{\pm i\theta_j} \); so \( p \), \( q \) and the \( \theta_j \) are recovered from \( \Q \) alone. This proves the theorem.
:::

So an orthogonal matrix is, up to an orthogonal change of coordinates, nothing but a list of angles together with a count of reversed axes. The number \( q \) of reversed axes is not itself an invariant of the *geometry* — a \( -1 \) block and a \( -1 \) block together make \( -\I_2 = \R_{\pi} \), a rotation by \( \pi \) — which is why the theorem demands \( \theta_j \neq \pi \) and keeps the \( -1 \)s separate. What the determinant sees is only the parity of \( q \).

::: {.check}
What is the canonical form of a \( \Q \in \Orth(2) \) with \( \det\Q = -1 \)? Compare with @thm-orthogonal-2x2.
:::

::: {.solution}
Here \( p + q + 2m = 2 \) and \( (-1)^q = -1 \), so \( q \) is odd, forcing \( q = 1 \), \( p = 1 \), \( m = 0 \). The canonical form is \( \I_1 \oplus (-\I_1) = \diag(1, -1) \). Chapter 10 found that such a \( \Q \) is the reflection \( \M_{\theta} \) in a line \( L \), fixing \( L \) and negating \( L^{\perp} \); in the orthonormal basis of eigenvectors of @thm-orthogonal-2x2 (b) its matrix is exactly \( \diag(1, -1) \). Note what the canonical form drops: the angle of the mirror. All reflections of the plane are orthogonally similar to one another, and @exr-orthogonal-matrices-and-rotations-c1 makes this comparison precise.
:::

## Rotations of space

In dimension \( 3 \) the arithmetic \( p + q + 2m = 3 \) leaves very few possibilities, and they all look the same.

::: {#cor-so3-is-rotation}
[Orthogonal Matrices in Dimension Three]

Let \( \Q \in \Orth(3) \). Then there are an orthonormal basis \( (\u, \w_1, \w_2) \) of \( \nR^3 \) and an angle \( \theta \in [0, \pi] \) such that, in that basis, the matrix of \( T_{\Q} \) is
\[
[1] \oplus \R_{\theta} \quad\text{if } \det\Q = 1, \qquad
[-1] \oplus \R_{\theta} \quad\text{if } \det\Q = -1 .
\]
In particular every \( \Q \in \SO(3) \) fixes the line \( \Span(\u) \) pointwise and rotates the plane \( \Span(\u)^{\perp} \) by \( \theta \).
:::

::: {.proof}
Write the canonical form of @thm-orthogonal-canonical-form, with \( p + q + 2m = 3 \) and \( \det\Q = (-1)^q \).

*Case \( \det\Q = 1 \).* Then \( q \) is even, so \( q \in \{0, 2\} \). If \( q = 0 \) then \( p + 2m = 3 \), giving \( (p, m) = (3, 0) \) or \( (1, 1) \); if \( q = 2 \) then \( p = 1 \) and \( m = 0 \). The three forms are
\[
\I_3 = [1] \oplus \R_0, \qquad [1] \oplus \R_{\theta_1}, \qquad [1] \oplus (-\I_2) = [1] \oplus \R_{\pi},
\]
and in every case \( p \ge 1 \), so the form is \( [1] \oplus \R_{\theta} \) with \( \theta \in [0, \pi] \).

*Case \( \det\Q = -1 \).* Then \( q \) is odd, so \( q \in \{1, 3\} \). If \( q = 1 \) then \( p + 2m = 2 \), giving \( (p, m) = (2, 0) \) or \( (0, 1) \); if \( q = 3 \) then \( p = m = 0 \). The three forms are \( [-1] \oplus \I_2 = [-1] \oplus \R_0 \), then \( [-1] \oplus \R_{\theta_1} \), and \( -\I_3 = [-1] \oplus \R_{\pi} \).

In both cases the first basis vector \( \u \) spans the \( \pm 1 \) eigenline and \( (\w_1, \w_2) \) is an orthonormal basis of \( \Span(\u)^{\perp} \), which is what the last sentence asserts when \( \det\Q = 1 \).
:::

Chapter 10 proved the \( \SO(3) \) statement directly, as @thm-so3-rotation, by producing a real eigenvalue from the odd degree of the characteristic polynomial and then invoking the classification of \( \Orth(2) \). We do not repeat that argument: the point here is that the same conclusion falls out of the canonical form with no work at all, and that the same three lines also settle \( \det\Q = -1 \). An orthogonal matrix of determinant \( -1 \) in dimension \( 3 \) is a **rotatory reflection**: a rotation about an axis followed by the reflection in the plane perpendicular to it. Its two extreme cases are the plane reflection (\( \theta = 0 \)) and the antipodal map \( -\I_3 \) (\( \theta = \pi \)).

::: {.remark}
The angle \( \theta \) is determined by \( \Q \) only up to sign, because exchanging \( \w_1 \) and \( \w_2 \) replaces \( \R_{\theta} \) by \( \R_{-\theta} \). Restricting to \( \theta \in [0, \pi] \), as above, makes it unique; to speak of a *signed* angle one must also fix which of the two unit vectors on the axis is called \( \u \).
:::

## The cross-product matrix

The canonical form tells us that a rotation of \( \nR^3 \) exists in a suitable basis. For computation we want it in the standard basis, written directly in terms of the axis. The bookkeeping is done by one matrix.

Recall from Chapter 6 that the cross product of \( \a, \b \in \nR^3 \) is
\[
\a \times \b = (a_2b_3 - a_3b_2,\ a_3b_1 - a_1b_3,\ a_1b_2 - a_2b_1).
\]
For fixed \( \a \) this is linear in \( \b \), so it is given by a matrix.

::: {#def-cross-product-matrix}
[Cross-product Matrix]

For \( \n = (n_1, n_2, n_3) \in \nR^3 \), the **cross-product matrix** of \( \n \) is
\[
\K_{\n} \coloneqq \begin{pmatrix} 0 & -n_3 & n_2 \\ n_3 & 0 & -n_1 \\ -n_2 & n_1 & 0 \end{pmatrix} \in M_3(\nR),
\]
so that \( \K_{\n}\v = \n \times \v \) for every \( \v \in \nR^3 \).
:::

The last clause is a check of the three entries against the formula above, with \( \a = \n \) and \( \b = \v \). The map \( \n \mapsto \K_{\n} \) is linear and injective, and its image is exactly the set of skew-symmetric \( 3 \times 3 \) matrices: a skew matrix has zero diagonal and three free entries below it, and those three entries are \( n_3, -n_2, n_1 \). We record the facts we need, all of them for a **unit** vector.

::: {#lem-cross-matrix-properties}
[Properties of the Cross-product Matrix]

Let \( \n \in \nR^3 \) with \( \norm{\n} = 1 \), and write \( \K = \K_{\n} \). Then

::: {.enumerate options="label=(\alph*)"}
1. \( \K\tp = -\K \) and \( \K\n = \0 \);
2. \( \K^2 = \n\n\tp - \I_3 \), so \( \K^2 \) is symmetric and \( \K^2\v = -\v \) for every \( \v \perp \n \);
3. \( \K^3 = -\K \);
4. for every \( \v \perp \n \): \( \norm{\K\v} = \norm{\v} \), \( \K\v \perp \v \) and \( \K\v \perp \n \).
:::
:::

::: {.idea}
Everything follows from (b), and (b) is one entry of a matrix product together with \( n_1^2 + n_2^2 + n_3^2 = 1 \). Part (c) is (b) multiplied by \( \K \), where the term \( \K\n\n\tp \) dies by (a). For (d), a norm is computed through its square, and \( \norm{\K\v}^2 = \v\tp\K\tp\K\v = -\v\tp\K^2\v \) turns (d) into (b) as well.
:::

::: {.proof}
(a) Transposing \( \K_{\n} \) changes the sign of each of the three off-diagonal pairs, and the diagonal is zero. For the second claim, \( \K\n = \n \times \n = \0 \) directly from the formula, each coordinate being of the form \( n_in_j - n_jn_i \).

(b) The \( (1,1) \) entry of \( \K^2 \) is \( 0 \cdot 0 + (-n_3)n_3 + n_2(-n_2) = -n_2^2 - n_3^2 = n_1^2 - 1 \), using \( \norm{\n}^2 = 1 \); and \( (\n\n\tp - \I_3)_{11} = n_1^2 - 1 \). The \( (1,2) \) entry of \( \K^2 \) is \( 0(-n_3) + (-n_3)0 + n_2n_1 = n_1n_2 = (\n\n\tp)_{12} \), and the \( (1,3) \) entry is \( 0n_2 + (-n_3)(-n_1) + n_20 = n_1n_3 \). The remaining six entries are obtained by cycling the indices \( 1 \to 2 \to 3 \to 1 \), under which both \( \K \) and \( \n\n\tp - \I_3 \) are unchanged in form. Hence \( \K^2 = \n\n\tp - \I_3 \), which is symmetric since \( (\n\n\tp)\tp = \n\n\tp \). If \( \v \perp \n \) then \( \n\tp\v = 0 \), so \( \K^2\v = \n(\n\tp\v) - \v = -\v \).

(c) By (b) and (a), \( \K^3 = \K(\n\n\tp - \I_3) = (\K\n)\n\tp - \K = -\K \).

(d) Let \( \v \perp \n \). Using (a) and then (b),
\[
\norm{\K\v}^2 = (\K\v)\tp(\K\v) = \v\tp\K\tp\K\v = -\v\tp\K^2\v = \v\tp\v = \norm{\v}^2 .
\]
Next, \( \inner{\K\v}{\v} = \v\tp\K\v \) is a \( 1 \times 1 \) matrix, hence equal to its own transpose \( \v\tp\K\tp\v = -\v\tp\K\v \); a number equal to its own negative is \( 0 \), so \( \K\v \perp \v \). Finally \( \inner{\K\v}{\n} = \n\tp\K\v = (\K\tp\n)\tp\v = -(\K\n)\tp\v = 0 \) by (a). This proves the lemma.
:::

Part (c) is the identity that makes every power of \( \K \) reduce to \( \K \) or \( \K^2 \), and it is the reason Rodrigues' formula has only three terms and no more.

## Rodrigues' formula

Fix a unit vector \( \n \) and an angle \( \theta \). We want a formula for "turn space by \( \theta \) about the axis \( \Span(\n) \)". The construction is forced by the picture: split a vector into the part along the axis, which does not move, and the part perpendicular to the axis, which turns inside a single plane.

Write \( \v_{\parallel} = \inner{\v}{\n}\n = \n\n\tp\v \) for the component of \( \v \) along the axis and \( \v_{\perp} = \v - \v_{\parallel} \) for the component perpendicular to it; this is the splitting of @thm-orthogonal-decomposition for \( U = \Span(\n) \), and \( \v_{\parallel} = P_U\v \) by @thm-projection-formula (a) with the orthonormal basis \( (\n) \) of \( U \). Write \( \v' \) for the vector we want, the image of \( \v \) under the turn.

\begin{center}
\begin{tikzpicture}[scale=1.35, lab/.style={font=\small}]
    \draw[gray, thin] (0,-0.3) -- (0,2.8);
    \draw[dashed, black!45] (0,1.6) ellipse (1.8 and 0.5);
    \draw[->, thick, black!55] (0,0) -- (0,1.6);
    \node[lab] at (0.32,1.80) {$\v_{\parallel}$};
    \draw[->, very thick] (0,0) -- (0,0.8);
    \node[lab] at (0.18,0.42) {$\n$};
    \draw[->, very thick] (0,0) -- (-1.691,1.429) node[left, lab] {$\v$};
    \draw[->, thick] (0,1.6) -- (-1.691,1.429);
    \node[lab] at (-1.05,1.80) {$\v_{\perp}$};
    \draw[->, thick] (0,1.6) -- (0.616,1.130) node[right, lab] {$\n \times \v$};
    \draw[->, thick] (0,1.6) -- (-0.313,1.108);
    \draw[->, very thick] (0,0) -- (-0.313,1.108);
    \node[lab] at (-0.54,0.66) {$\v'$};
    \begin{scope}[shift={(0,1.6)}, xscale=1.2, yscale=0.333]
        \draw[->] (200:1) arc (200:260:1);
    \end{scope}
    \node[lab] at (-0.78,1.26) {$\theta$};
    \node[lab, align=center] at (0.1,-0.9) {the axis part stays, the perpendicular part turns};
\end{tikzpicture}
\end{center}

By @lem-cross-matrix-properties (d), the vector \( \K_{\n}\v_{\perp} \) has the same length as \( \v_{\perp} \) and is perpendicular to both \( \v_{\perp} \) and \( \n \): it is \( \v_{\perp} \) turned by a quarter turn inside the plane \( \n^{\perp} \). So turning \( \v_{\perp} \) by \( \theta \) means taking \( \cos\theta\,\v_{\perp} + \sin\theta\,\K_{\n}\v_{\perp} \), and \( \v' = \v_{\parallel} + \cos\theta\,\v_{\perp} + \sin\theta\,\K_{\n}\v_{\perp} \). Finally \( \K_{\n}\v_{\perp} = \K_{\n}\v \), since \( \K_{\n}\v_{\parallel} \) is a multiple of \( \K_{\n}\n = \0 \). That is the definition we take, and the theorem says it is the right one.

::: {#thm-rodrigues}
[Rodrigues' Rotation Formula]

Let \( \n \in \nR^3 \) be a unit vector, let \( \theta \in \nR \), and write \( \K = \K_{\n} \). Define
\[
\R_{\n,\theta} \coloneqq \I_3 + \sin\theta\,\K + (1 - \cos\theta)\,\K^2 .
\]

::: {.enumerate options="label=(\alph*)"}
1. For every \( \v \in \nR^3 \),
 \[
 \R_{\n,\theta}\v = \inner{\v}{\n}\n + \cos\theta\,\bigl(\v - \inner{\v}{\n}\n\bigr) + \sin\theta\,(\n \times \v) .
 \]
2. \( \R_{\n,\theta}\n = \n \), and for every unit \( \w \perp \n \) the list \( \sB = (\n, \w, \n \times \w) \) is an orthonormal basis of \( \nR^3 \) with \( \mtx{T_{\R_{\n,\theta}}}{\sB}{\sB} = [1] \oplus \R_{\theta} \). In particular \( \R_{\n,\theta} \in \SO(3) \).
3. Conversely, every \( \Q \in \SO(3) \) equals \( \R_{\n,\theta} \) for some unit vector \( \n \) and some \( \theta \in [0, \pi] \).
:::
:::

::: {.idea}
Part (a) is the paragraph above, read backwards: substitute \( \n\n\tp = \K^2 + \I_3 \) from @lem-cross-matrix-properties (b) into the geometric expression and collect terms. Part (b) then needs only the images of three basis vectors, and every one of them is a two-line computation with (a) and the lemma; the matrix that comes out is the canonical form of @cor-so3-is-rotation, which also gives orthogonality and the determinant for free. Part (c) runs @cor-so3-is-rotation in reverse: it hands us a basis \( (\u, \w_1, \w_2) \), and the only question is whether \( \w_2 \) is \( \u \times \w_1 \) or its negative — and if it is the negative, we change the sign of the angle.
:::

::: {.proof}
(a) By @lem-cross-matrix-properties (b), \( \n\n\tp = \K^2 + \I_3 \). Hence, writing \( \inner{\v}{\n}\n = \n\n\tp\v \) and \( \n \times \v = \K\v \),
\[
\begin{aligned}
&\n\n\tp\v + \cos\theta\,(\v - \n\n\tp\v) + \sin\theta\,\K\v \\
 &\qquad = \cos\theta\,\v + (1 - \cos\theta)\n\n\tp\v + \sin\theta\,\K\v \\
 &\qquad = \cos\theta\,\v + (1-\cos\theta)(\K^2 + \I_3)\v + \sin\theta\,\K\v \\
 &\qquad = \bigl(\I_3 + \sin\theta\,\K + (1-\cos\theta)\K^2\bigr)\v ,
\end{aligned}
\]
since \( \cos\theta + (1 - \cos\theta) = 1 \). The right-hand side is \( \R_{\n,\theta}\v \).

(b) First \( \K\n = \0 \) and \( \K^2\n = \K(\K\n) = \0 \) by @lem-cross-matrix-properties (a), so \( \R_{\n,\theta}\n = \n \).

Let \( \w \) be a unit vector with \( \w \perp \n \), and put \( \z = \K\w = \n \times \w \). By @lem-cross-matrix-properties (d), \( \norm{\z} = 1 \), \( \z \perp \w \) and \( \z \perp \n \), so \( \sB = (\n, \w, \z) \) is an orthonormal list of three vectors in \( \nR^3 \), hence an orthonormal basis (@thm-orthogonal-independent and @thm-right-size-basis). Now compute the three images. We have \( \R_{\n,\theta}\n = \n \). Next, \( \K^2\w = -\w \) by @lem-cross-matrix-properties (b), since \( \w \perp \n \), so
\[
\R_{\n,\theta}\w = \w + \sin\theta\,\z - (1 - \cos\theta)\w = \cos\theta\,\w + \sin\theta\,\z .
\]
Finally \( \z \perp \n \), so \( \K^2\z = -\z \), and \( \K\z = \K^2\w = -\w \); hence
\[
\R_{\n,\theta}\z = \z - \sin\theta\,\w - (1-\cos\theta)\z = -\sin\theta\,\w + \cos\theta\,\z .
\]
Reading off the columns (@def-matrix-of-linear-map), \( \mtx{T_{\R_{\n,\theta}}}{\sB}{\sB} = [1] \oplus \R_{\theta} \). This matrix is orthogonal, and it is the matrix of \( T_{\R_{\n,\theta}} \) in an orthonormal basis, so \( T_{\R_{\n,\theta}} \) is an isometry and \( \R_{\n,\theta} \in \Orth(3) \) by @thm-isometry-characterizations (f) and @def-unitary-orthogonal. The two matrices are matrices of the same operator, hence similar (@thm-similar-iff-same-operator (a)), so they have the same determinant (@cor-det-similarity-invariant), namely \( 1 \); so \( \R_{\n,\theta} \in \SO(3) \).

(c) Let \( \Q \in \SO(3) \). By @cor-so3-is-rotation there are an orthonormal basis \( \sC = (\u, \w_1, \w_2) \) of \( \nR^3 \) and \( \theta \in [0, \pi] \) with \( \mtx{T_{\Q}}{\sC}{\sC} = [1] \oplus \R_{\theta} \). The vector \( \u \times \w_1 \) is a unit vector orthogonal to \( \u \) and \( \w_1 \) by @lem-cross-matrix-properties (d), and so is \( \w_2 \); since \( \Span(\u, \w_1)^{\perp} \) is a line (@thm-orthogonal-decomposition (c)), its unit vectors are \( \pm\u \times \w_1 \), so \( \w_2 = \varepsilon\,\u \times \w_1 \) with \( \varepsilon = \pm 1 \).

*Case \( \varepsilon = 1 \).* Then (b), applied with \( \n = \u \) and \( \w = \w_1 \), gives \( \mtx{T_{\R_{\u,\theta}}}{\sC}{\sC} = [1] \oplus \R_{\theta} = \mtx{T_{\Q}}{\sC}{\sC} \). Operators with the same matrix in one basis are equal, so \( \Q = \R_{\u,\theta} \).

*Case \( \varepsilon = -1 \).* Then \( \u \times \w_1 = -\w_2 \), and the matrix of \( T_{\Q} \) in the basis \( (\u, \w_1, -\w_2) \) is obtained from \( [1] \oplus \R_{\theta} \) by changing the sign of the third basis vector, which changes the sign of the two off-diagonal entries of the \( \R_{\theta} \) block: it is \( [1] \oplus \R_{-\theta} \). By the previous case, \( \Q = \R_{\u,-\theta} \). Finally \( \K_{-\u} = -\K_{\u} \), so
\[
\R_{-\u,\theta} = \I_3 - \sin\theta\,\K_{\u} + (1-\cos\theta)\K_{\u}^2 = \R_{\u,-\theta},
\]
and \( \Q = \R_{-\u,\theta} \) with \( -\u \) a unit vector and \( \theta \in [0, \pi] \). This proves the theorem.
:::

Part (c) is worth restating on its own: **a rotation of \( \nR^3 \) is nothing but a unit vector and an angle**. That is three numbers of data, one of them redundant, for an object that started life as nine matrix entries subject to six equations.

::: {.check}
Compute \( \R_{\n,\pi} \) from Rodrigues' formula and identify the map geometrically.
:::

::: {.solution}
With \( \sin\pi = 0 \) and \( 1 - \cos\pi = 2 \), the formula gives \( \R_{\n,\pi} = \I_3 + 2\K^2 = \I_3 + 2(\n\n\tp - \I_3) = 2\n\n\tp - \I_3 \), using @lem-cross-matrix-properties (b). It fixes \( \n \) and negates every vector perpendicular to \( \n \): the half-turn about the axis. Equivalently \( \R_{\n,\pi} = -(\I_3 - 2\n\n\tp) = -\H_{\n} \), minus the Householder reflection of @def-householder-reflection in the plane \( \n^{\perp} \).
:::

## Reading off the axis and the angle

Rodrigues' formula runs one way: from \( (\n, \theta) \) to \( \Q \). The inverse direction is just as cheap, because the formula splits \( \Q \) into a symmetric part and a skew part that carry the two pieces of data separately.

::: {#thm-rotation-angle-trace}
[Axis and Angle from the Matrix]

Let \( \Q = \R_{\n,\theta} \in \SO(3) \) with \( \n \) a unit vector and \( \theta \in [0, \pi] \). Then

::: {.enumerate options="label=(\alph*)"}
1. \( \tr\Q = 1 + 2\cos\theta \), so \( \cos\theta = \tfrac12(\tr\Q - 1) \) and \( \theta \) is determined by \( \Q \);
2. \( \Q - \Q\tp = 2\sin\theta\,\K_{\n} \);
3. if \( 0 < \theta < \pi \), then \( \sin\theta > 0 \) and
 \[
 \n = \frac{1}{2\sin\theta}\,(q_{32} - q_{23},\ q_{13} - q_{31},\ q_{21} - q_{12}) ;
 \]
 if \( \theta = 0 \) then \( \Q = \I_3 \) and the axis is arbitrary; and if \( \theta = \pi \) then \( \Q + \I_3 = 2\n\n\tp \), whose non-zero columns are the multiples \( 2n_i\n \) of \( \n \).
:::
:::

::: {.proof}
Write \( \K = \K_{\n} \). By @lem-cross-matrix-properties (b), \( \K^2 = \n\n\tp - \I_3 \), so \( \tr\K^2 = \tr(\n\n\tp) - 3 = \norm{\n}^2 - 3 = -2 \); and \( \tr\K = 0 \), the diagonal of \( \K \) being zero.

(a) Taking traces in Rodrigues' formula, which is legitimate because the trace is linear (@thm-trace-properties (1)),
\[
\tr\Q = 3 + \sin\theta \cdot 0 + (1 - \cos\theta)(-2) = 1 + 2\cos\theta .
\]
Since \( \cos \) is injective on \( [0, \pi] \), this determines \( \theta \).

(b) By @lem-cross-matrix-properties (a) and (b), \( \K\tp = -\K \) and \( (\K^2)\tp = \K^2 \). Transposing Rodrigues' formula therefore gives \( \Q\tp = \I_3 - \sin\theta\,\K + (1-\cos\theta)\K^2 \), and subtracting, \( \Q - \Q\tp = 2\sin\theta\,\K \).

(c) For \( \theta \in (0, \pi) \) we have \( \sin\theta > 0 \), so (b) may be divided by \( 2\sin\theta \), and the three independent entries of \( \K_{\n} \) are \( (\K_{\n})_{32} = n_1 \), \( (\K_{\n})_{13} = n_2 \) and \( (\K_{\n})_{21} = n_3 \) by @def-cross-product-matrix; the displayed formula reads these off \( \Q - \Q\tp \). If \( \theta = 0 \) then Rodrigues' formula gives \( \Q = \I_3 \). If \( \theta = \pi \) then \( \Q = 2\n\n\tp - \I_3 \), as computed in the Quick check above, so \( \Q + \I_3 = 2\n\n\tp \), whose \( i \)-th column is \( 2n_i\n \); at least one \( n_i \neq 0 \), so at least one column is a non-zero multiple of \( \n \). This proves the theorem.
:::

The two degenerate angles are exactly the two at which the skew part \( \Q - \Q\tp \) vanishes, and they are exactly the two at which the axis is not determined by a *signed* angle: at \( \theta = 0 \) there is no rotation to speak of, and at \( \theta = \pi \) turning by \( +\pi \) and \( -\pi \) about the same axis give the same map. Everywhere else, part (c) is a two-subtraction recipe.

::: {#exm-rotation-axis-angle}
[Axis and Angle of a Space Rotation]

Let
\[
\Q = \tfrac19\begin{pmatrix} 1 & -4 & 8 \\ 8 & 4 & 1 \\ -4 & 7 & 4 \end{pmatrix} .
\]
Verify that \( \Q \in \SO(3) \), find its axis and angle, and confirm the answer with Rodrigues' formula.
:::

::: {.solution}
*Orthogonality.* The columns are \( \tfrac19(1, 8, -4) \), \( \tfrac19(-4, 4, 7) \) and \( \tfrac19(8, 1, 4) \). Each has squared norm \( \tfrac1{81}(1 + 64 + 16) = \tfrac1{81}(16+16+49) = \tfrac1{81}(64+1+16) = 1 \), and the three pairwise inner products are
\[
\tfrac1{81}(-4 + 32 - 28) = \tfrac1{81}(8 + 8 - 16) = \tfrac1{81}(-32 + 4 + 28) = 0 .
\]
So \( \Q \in \Orth(3) \) by @thm-isometry-characterizations (f).

*Determinant.* Expanding along the first row, \( 729\det\Q = 1(16 - 7) - (-4)(32 + 4) + 8(56 + 16) = 9 + 144 + 576 = 729 \), so \( \det\Q = 1 \) and \( \Q \in \SO(3) \).

*Angle.* \( \tr\Q = \tfrac19(1 + 4 + 4) = 1 \), so \( \cos\theta = \tfrac12(1 - 1) = 0 \) and \( \theta = \pi/2 \) by @thm-rotation-angle-trace (a).

*Axis.* Here \( 2\sin\theta = 2 \). The three entries needed by @thm-rotation-angle-trace (c) are
\[
\begin{aligned}
q_{32} - q_{23} &= \tfrac{7 - 1}{9} = \tfrac69, \\
q_{13} - q_{31} &= q_{21} - q_{12} = \tfrac{8 + 4}{9} = \tfrac{12}{9},
\end{aligned}
\]
so \( \n = \tfrac12\bigl(\tfrac69, \tfrac{12}9, \tfrac{12}9\bigr) = \tfrac13(1, 2, 2) \), which is a unit vector since \( 1 + 4 + 4 = 9 \).

*Check.* \( \Q(1,2,2) = \tfrac19(1 - 8 + 16,\ 8 + 8 + 2,\ -4 + 14 + 8) = \tfrac19(9, 18, 18) = (1, 2, 2) \), so the axis is fixed. And Rodrigues' formula with \( \theta = \pi/2 \) reads \( \R_{\n,\pi/2} = \I_3 + \K + \K^2 \), where
\[
\K = \tfrac13\begin{pmatrix} 0 & -2 & 2 \\ 2 & 0 & -1 \\ -2 & 1 & 0 \end{pmatrix},
\qquad
\K^2 = \n\n\tp - \I_3 = \tfrac19\begin{pmatrix} -8 & 2 & 2 \\ 2 & -5 & 4 \\ 2 & 4 & -5 \end{pmatrix} .
\]
Adding \( \I_3 + \K + \K^2 \) entry by entry, for instance \( 1 + 0 - \tfrac89 = \tfrac19 \) in position \( (1,1) \) and \( 0 - \tfrac23 + \tfrac29 = -\tfrac49 \) in position \( (1,2) \), returns \( \Q \).
:::

## Reflections generate

The canonical form is one way to say that an orthogonal matrix is built from simple pieces. Here is another, and the pieces are even simpler: mirrors. Recall from Chapter 10 the Householder reflection \( \H_{\w} = \I_n - 2\w\w\tp/\norm{\w}^2 \) determined by a non-zero \( \w \) (@def-householder-reflection); it is orthogonal, equal to its own inverse, and has determinant \( -1 \) (@prp-householder-properties).

::: {#lem-reflection-swaps-vectors}
[A Mirror Between Two Vectors of Equal Length]

Let \( \x, \y \in \nR^n \) with \( \norm{\x} = \norm{\y} \) and \( \x \neq \y \). Then \( \w \coloneqq \x - \y \) is non-zero and \( \H_{\w}\x = \y \).
:::

::: {.proof}
\( \w \neq \0 \) because \( \x \neq \y \). Expanding the two inner products and using \( \norm{\y}^2 = \norm{\x}^2 \),
\[
\begin{aligned}
\norm{\w}^2 &= \norm{\x}^2 - 2\inner{\x}{\y} + \norm{\y}^2 = 2\bigl(\norm{\x}^2 - \inner{\x}{\y}\bigr), \\
\inner{\x}{\w} &= \norm{\x}^2 - \inner{\x}{\y} ,
\end{aligned}
\]
so \( 2\inner{\x}{\w} = \norm{\w}^2 \). Hence, by the formula \( \H_{\w}\v = \v - 2\bigl(\inner{\v}{\w}/\norm{\w}^2\bigr)\w \) of @def-householder-reflection,
\[
\H_{\w}\x = \x - \w = \x - (\x - \y) = \y ,
\]
as claimed.
:::

This is @thm-householder-maps-vector with the target chosen for geometry rather than for arithmetic: there, \( \y \) was a prescribed multiple of \( \e_1 \) and the sign was picked to avoid cancellation; here \( \y \) is whatever we need, and the mirror is the perpendicular bisector of the segment from \( \x \) to \( \y \).

::: {#thm-cartan-dieudonne-small}
[Reflections Generate the Orthogonal Group]

Let \( n \ge 1 \) and \( \Q \in \Orth(n) \). Then \( \Q \) is a product of at most \( n \) Householder reflections. (The identity is the empty product, of zero reflections.)
:::

::: {.idea}
Induct on \( n \), and make the induction bite by fixing one coordinate at a time. If \( \Q \) already fixes \( \e_1 \), then it maps \( \e_1^{\perp} \) into itself, and the inductive hypothesis applied inside that \( (n-1) \)-dimensional space produces at most \( n - 1 \) reflections, each of which extends to a reflection of \( \nR^n \) by taking the same \( \w \). If \( \Q \) does not fix \( \e_1 \), spend one reflection making it do so: \( \Q\e_1 \) and \( \e_1 \) are two distinct vectors of the same length, and @lem-reflection-swaps-vectors is exactly the tool that swaps them.
:::

::: {.proof}
Induction on \( n \). For \( n = 1 \), a matrix \( [a] \in \Orth(1) \) satisfies \( a^{2} = [a]\tp[a] = 1 \), so \( (a-1)(a+1) = 0 \) and \( a = \pm 1 \); thus \( \Orth(1) = \{[1], [-1]\} \), where \( [1] \) is the empty product and \( [-1] = \H_{\e_1} \), one reflection.

Let \( n \ge 2 \) and assume the statement in dimension \( n - 1 \). Let \( \Q \in \Orth(n) \) and set \( \x = \Q\e_1 \), a unit vector since \( T_{\Q} \) is an isometry (@thm-isometry-characterizations).

**Case 1: \( \x = \e_1 \).** Put \( U = \Span(\e_1)^{\perp} \), of dimension \( n - 1 \) by @thm-orthogonal-decomposition (c). For \( \v \in U \) we have \( \inner{\Q\v}{\e_1} = \inner{\Q\v}{\Q\e_1} = \inner{\v}{\e_1} = 0 \), the middle equality by @thm-isometry-characterizations (b); so \( U \) is \( T_{\Q} \)-invariant. Identify \( U \) with \( \nR^{n-1} \) through the orthonormal basis \( (\e_2, \dots, \e_n) \). The restriction \( T_{\Q}|_U \) is an isometry of \( U \), so its matrix \( \Q' \) in that basis lies in \( \Orth(n-1) \) (@thm-isometry-characterizations (f)), and by the inductive hypothesis \( \Q' = \H_{\w'_1}\cdots\H_{\w'_k} \) with \( k \le n - 1 \) and \( \w'_i \in \nR^{n-1} \). Let \( \w_i \in U \subseteq \nR^n \) be the vector with coordinates \( \w'_i \) in the basis \( (\e_2, \dots, \e_n) \). Then \( \H_{\w_i} \) fixes \( \e_1 \), because \( \e_1 \perp \w_i \) (@prp-householder-properties (d)), and on \( U \) it acts as \( \H_{\w'_i} \), because the defining formula only involves inner products, which agree. Hence \( \Q \) and \( \H_{\w_1}\cdots\H_{\w_k} \) agree on \( \e_1 \) and on \( U \), so they agree on \( \nR^n = \Span(\e_1) \oplus U \), and \( \Q \) is a product of \( k \le n - 1 \le n \) reflections.

**Case 2: \( \x \neq \e_1 \).** Then \( \norm{\x} = 1 = \norm{\e_1} \), so \( \w \coloneqq \x - \e_1 \) is non-zero and \( \H_{\w}\x = \e_1 \) by @lem-reflection-swaps-vectors. The matrix \( \H_{\w}\Q \) is orthogonal, being a product of orthogonal matrices (@prp-orthogonal-group-properties (a)), and \( \H_{\w}\Q\e_1 = \H_{\w}\x = \e_1 \). By Case 1, \( \H_{\w}\Q \) is a product of at most \( n - 1 \) reflections. Multiplying on the left by \( \H_{\w} \) and using \( \H_{\w}^2 = \I_n \) (@prp-householder-properties (b)),
\[
\Q = \H_{\w}(\H_{\w}\Q),
\]
a product of at most \( n \) reflections. This completes the induction.
:::

Counting reflections recovers the determinant: each factor contributes \( -1 \) (@prp-householder-properties (e)), so a product of \( k \) reflections has determinant \( (-1)^k \), and an element of \( \SO(n) \) needs an even number of them. The bound \( n \) is sharp — \( -\I_n \) is a product of \( n \) reflections and no fewer, since a product of \( k \) reflections fixes the intersection of \( k \) hyperplanes, a subspace of dimension at least \( n - k \), while \( -\I_n \) fixes only \( \0 \).

::: {.remark}
The general theorem behind this one, due to Cartan and Dieudonné, says the same for the orthogonal group of any non-degenerate symmetric bilinear form over any field of characteristic \( \neq 2 \). Only the Euclidean case is proved here, and only the Euclidean case is used.
:::

## Composing rotations

Two rotations of the plane about the origin compose into a rotation, and the angles add: \( \R_{\alpha}\R_{\beta} = \R_{\alpha+\beta} \), so \( \SO(2) \) is abelian (Chapter 10). The reason is visible in the canonical form: in dimension \( 2 \) there is only one rotation block, so a rotation is a single number, and numbers commute.

In dimension \( 3 \) the picture changes completely, because there is an axis to move as well as an angle to add.

::: {#exm-rotations-do-not-commute}
[Two Quarter Turns in Two Orders]

Let \( \A = \R_{\e_1, \pi/2} \) and \( \B = \R_{\e_3, \pi/2} \), the quarter turns about the first and third coordinate axes. Compute \( \A\B \) and \( \B\A \), and find the axis and angle of each.
:::

::: {.solution}
From @thm-rodrigues (b), \( \A \) fixes \( \e_1 \) and turns the \( (\e_2, \e_3) \)-plane by \( \pi/2 \), and \( \B \) fixes \( \e_3 \) and turns the \( (\e_1, \e_2) \)-plane by \( \pi/2 \):
\[
\A = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix},
\qquad
\B = \begin{pmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} .
\]
Multiplying,
\[
\A\B = \begin{pmatrix} 0 & -1 & 0 \\ 0 & 0 & -1 \\ 1 & 0 & 0 \end{pmatrix},
\qquad
\B\A = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} .
\]
These are different matrices, so \( \SO(3) \) is not abelian. Both have trace \( 0 \), so both are rotations by the angle \( \theta \) with \( \cos\theta = \tfrac12(0 - 1) = -\tfrac12 \), that is \( \theta = 2\pi/3 \). Their axes differ. Solving \( \A\B\v = \v \) gives \( -v_2 = v_1 \), \( -v_3 = v_2 \), \( v_1 = v_3 \), so the axis of \( \A\B \) is \( \Span((1, -1, 1)) \); solving \( \B\A\v = \v \) gives \( v_3 = v_1 \), \( v_1 = v_2 \), \( v_2 = v_3 \), so the axis of \( \B\A \) is \( \Span((1, 1, 1)) \). Same angle, different axes: the order of two quarter turns changes where the resulting axis points.
:::

That the product is *again* a rotation is not an accident of this example: \( \SO(3) \) is a group (@prp-orthogonal-group-properties), so any product of rotations is orthogonal with determinant \( 1 \), and @cor-so3-is-rotation makes it a rotation. What no formula makes obvious is which one; @exr-orthogonal-matrices-and-rotations-c2 pursues this.

::: {.warning}
**In dimension \( 4 \) and above, \( \det\Q = 1 \) does not mean "rotation about an axis".** Take
\[
\Q = \R_{\pi/2} \oplus \R_{\pi/3} \in \Orth(4), \qquad \det\Q = 1 \cdot 1 = 1 .
\]
Its canonical form is itself, with \( p = q = 0 \) and \( m = 2 \), so \( 1 \) is not an eigenvalue and \( \Q \) fixes no non-zero vector at all: there is no axis. Worse, the two angles are different, so \( \Q \) is not a rotation "in a plane" either — it turns two orthogonal planes at two different speeds, and no single angle describes it. Chapter 10 made the same point with \( -\I_4 \in \SO(4) \); the canonical form explains it, since for even \( n \) the counts \( p = q = 0 \) are allowed. The clean statement "determinant \( 1 \) means a rotation about an axis" is a feature of dimension \( 3 \), where \( p + q + 2m = 3 \) is odd and forces \( p \ge 1 \) when \( q \) is even.
:::

## Exercises

### A. Check your understanding

::: {#exr-orthogonal-matrices-and-rotations-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the canonical form of an element of \( \Orth(n) \), saying what the blocks are and which angles are allowed.
2. Which hypothesis on \( \Q \) turns the rotation-scaling blocks of the real normal form into rotation blocks, and why?
3. Write down the cross-product matrix \( \K_{\n} \) and state the identity \( \K_{\n}^3 = ? \) for a unit \( \n \).
4. Given \( \Q \in \SO(3) \), how do you find its angle, and how do you find its axis? Name the two degenerate cases.
5. True or false: if \( \Q \in \Orth(n) \) and \( \det\Q = 1 \), then \( \Q \) fixes a non-zero vector. Justify your answer.
6. How many Householder reflections can be needed to write an element of \( \Orth(n) \), and what does the parity of that number say?
:::
:::

::: {.solution}
(a) By @thm-orthogonal-canonical-form, \( \P\tp\Q\P = \I_p \oplus (-\I_q) \oplus \R_{\theta_1} \oplus \cdots \oplus \R_{\theta_m} \) for some \( \P \in \Orth(n) \), with \( p + q + 2m = n \) and \( 0 < \theta_j < \pi \). The angles \( 0 \) and \( \pi \) are excluded because \( \R_0 = \I_2 \) and \( \R_{\pi} = -\I_2 \) are already accounted for by the \( \pm 1 \) blocks.

(b) Orthogonality. An orthogonal matrix is unitary as a complex matrix (@prp-orthogonal-group-properties (a)), so each of its eigenvalues has modulus \( 1 \) (@prp-isometry-eigenvalues-modulus-one). A block \( \vLambda(\lambda) \) has eigenvalues \( \lambda, \conj\lambda \), so \( \lvert\lambda\rvert = 1 \) and the scaling factor is \( 1 \).

(c) \( \K_{\n} \) has rows \( (0, -n_3, n_2) \), \( (n_3, 0, -n_1) \), \( (-n_2, n_1, 0) \) (@def-cross-product-matrix), and \( \K_{\n}^3 = -\K_{\n} \) when \( \norm{\n} = 1 \) (@lem-cross-matrix-properties (c)).

(d) The angle from the trace, \( \cos\theta = \tfrac12(\tr\Q - 1) \) with \( \theta \in [0, \pi] \); the axis from the skew part, \( \Q - \Q\tp = 2\sin\theta\,\K_{\n} \) (@thm-rotation-angle-trace). The degenerate cases are \( \theta = 0 \), where \( \Q = \I_3 \) and there is no axis to find, and \( \theta = \pi \), where the skew part vanishes and one reads \( \n \) off \( \Q + \I_3 = 2\n\n\tp \) instead.

(e) False for even \( n \). The matrix \( \R_{\pi/2} \oplus \R_{\pi/3} \in \SO(4) \) has no eigenvalue \( 1 \). It is true for odd \( n \): then \( p + q + 2m = n \) is odd and \( q \) is even, so \( p = n - q - 2m \) is odd, hence \( p \ge 1 \), and the \( \I_p \) block supplies a fixed vector.

(f) At most \( n \) (@thm-cartan-dieudonne-small). Each reflection has determinant \( -1 \), so the number used has the same parity in every such factorization as the sign of \( \det\Q \) dictates: even for \( \det\Q = 1 \), odd for \( \det\Q = -1 \).
:::

### B. Practice

::: {#exr-orthogonal-matrices-and-rotations-b1}
[B1: Axis and angle]

For each of the following, decide whether it lies in \( \SO(3) \), \( \Orth(3) \setminus \SO(3) \), or neither. For those in \( \SO(3) \), find the axis and the angle; for those in \( \Orth(3) \) with determinant \( -1 \), give the canonical form \( [-1] \oplus \R_{\theta} \) and say what the map is geometrically.

::: {.enumerate options="label=(\alph*)"}
1. \( \tfrac19\begin{pmatrix} 4 & -8 & 1 \\ 4 & 1 & -8 \\ 7 & 4 & 4 \end{pmatrix} \).
2. \( \tfrac19\begin{pmatrix} -7 & 4 & 4 \\ 4 & -1 & 8 \\ 4 & 8 & -1 \end{pmatrix} \).
3. \( \tfrac19\begin{pmatrix} 7 & -4 & -4 \\ -4 & 1 & -8 \\ -4 & -8 & 1 \end{pmatrix} \).
4. \( \tfrac19\begin{pmatrix} 4 & -8 & 1 \\ 4 & 1 & -8 \\ 7 & 4 & 5 \end{pmatrix} \).
:::
:::

::: {.solution}
(a) The columns \( \tfrac19(4, 4, 7) \), \( \tfrac19(-8, 1, 4) \), \( \tfrac19(1, -8, 4) \) have squared norms \( \tfrac1{81}(16+16+49) = \tfrac1{81}(64+1+16) = \tfrac1{81}(1+64+16) = 1 \) and pairwise inner products \( \tfrac1{81}(-32 + 4 + 28) = \tfrac1{81}(4 - 32 + 28) = \tfrac1{81}(-8 - 8 + 16) = 0 \), so the matrix is orthogonal. Expanding along the first row, \( 729\det = 4(4 + 32) + 8(16 + 56) + 1(16 - 7) = 144 + 576 + 9 = 729 \), so it lies in \( \SO(3) \). Its trace is \( \tfrac19(4 + 1 + 4) = 1 \), so \( \cos\theta = 0 \) and \( \theta = \pi/2 \). For the axis, \( q_{32} - q_{23} = \tfrac19(4 + 8) = \tfrac{12}9 \), \( q_{13} - q_{31} = \tfrac19(1 - 7) = -\tfrac69 \) and \( q_{21} - q_{12} = \tfrac19(4 + 8) = \tfrac{12}9 \); dividing by \( 2\sin\theta = 2 \) gives \( \n = \tfrac13(2, -1, 2) \). Check: \( \Q(2,-1,2) = \tfrac19(8 + 8 + 2,\ 8 - 1 - 16,\ 14 - 4 + 8) = (2, -1, 2) \).

(b) The matrix is symmetric. Each column has entries \( \pm7, \pm4, \pm4 \) in some order, so each has squared norm \( \tfrac1{81}(49+16+16) = 1 \), and the pairwise inner products are \( \tfrac1{81}(-28 - 4 + 32) = \tfrac1{81}(-28 + 32 - 4) = \tfrac1{81}(16 - 8 - 8) = 0 \); so it is orthogonal. Expanding along the first row, \( 729\det = -7(1 - 64) - 4(-4 - 32) + 4(32 + 4) = 441 + 144 + 144 = 729 \), so it lies in \( \SO(3) \). Its trace is \( \tfrac19(-7 - 1 - 1) = -1 \), so \( \cos\theta = -1 \) and \( \theta = \pi \): a half-turn. The skew part is \( \0 \), so use \( \Q + \I_3 = \tfrac19\begin{pmatrix} 2 & 4 & 4 \\ 4 & 8 & 8 \\ 4 & 8 & 8 \end{pmatrix} = 2\n\n\tp \) with \( \n = \tfrac13(1, 2, 2) \). Check: \( \Q(1,2,2) = \tfrac19(-7 + 8 + 8,\ 4 - 2 + 16,\ 4 + 16 - 2) = (1, 2, 2) \).

(c) This is the negative of (b), so it is orthogonal with \( \det = (-1)^3 \cdot 1 = -1 \). Its trace is \( 1 \), and for the form \( [-1] \oplus \R_{\theta} \) the trace is \( -1 + 2\cos\theta \), so \( \cos\theta = 1 \) and \( \theta = 0 \): the canonical form is \( [-1] \oplus \I_2 = \diag(-1, 1, 1) \), a reflection. Indeed it equals \( \I_3 - 2\n\n\tp = \H_{\n} \) with \( \n = \tfrac13(1,2,2) \), the reflection in the plane \( x_1 + 2x_2 + 2x_3 = 0 \).

(d) Neither. This is (a) with the \( (3,3) \) entry changed from \( 4 \) to \( 5 \). The third column \( \tfrac19(1, -8, 5) \) has squared norm \( \tfrac1{81}(1 + 64 + 25) = \tfrac{90}{81} = \tfrac{10}{9} \ne 1 \), so the columns are not orthonormal and the matrix is not orthogonal (@thm-isometry-characterizations (f)). Its determinant is \( \tfrac{85}{81} \), neither \( 1 \) nor \( -1 \), which settles it a second way (@prp-orthogonal-group-properties). Note that checking the determinant alone is never enough: \( \det = 1 \) does not make a matrix orthogonal.
:::

::: {#exr-orthogonal-matrices-and-rotations-b2}
[B2: Mirrors]

::: {.enumerate options="label=(\alph*)"}
1. Write the matrix \( \M = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix} \) as a Householder reflection \( \H_{\w} \), and say which plane is its mirror.
2. Following the proof of @thm-cartan-dieudonne-small, write \( \Q = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} \) as a product of Householder reflections, and check the count against \( \det\Q \).
:::
:::

::: {.solution}
(a) \( \M \) exchanges \( \e_1 \) and \( \e_3 \) and fixes \( \e_2 \). By @lem-reflection-swaps-vectors with \( \x = \e_1 \) and \( \y = \e_3 \), take \( \w = \e_1 - \e_3 = (1, 0, -1) \); then \( \norm{\w}^2 = 2 \) and
\[
\H_{\w} = \I_3 - \w\w\tp = \I_3 - \begin{pmatrix} 1 & 0 & -1 \\ 0 & 0 & 0 \\ -1 & 0 & 1 \end{pmatrix} = \M .
\]
The mirror is \( \Span(\w)^{\perp} \), the plane \( x_1 = x_3 \).

(b) \( \Q\e_1 = \e_2 \neq \e_1 \), so we are in Case 2 with \( \w_1 = \Q\e_1 - \e_1 = (-1, 1, 0) \) and \( \norm{\w_1}^2 = 2 \):
\[
\H_{\w_1} = \I_3 - \w_1\w_1\tp = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} .
\]
Then \( \H_{\w_1}\Q = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix} \), which fixes \( \e_1 \) and exchanges \( \e_2 \) and \( \e_3 \); the computation of (a), with the indices shifted, shows that it is \( \H_{\w_2} \) for \( \w_2 = \e_2 - \e_3 = (0, 1, -1) \). Hence \( \Q = \H_{\w_1}\H_{\w_2} \), a product of two reflections. The count is even, matching \( \det\Q = (-1)^2 = 1 \); and indeed \( \Q \) is the rotation by \( 2\pi/3 \) about \( (1,1,1) \) found in @exm-rotations-do-not-commute.
:::

::: {#exr-orthogonal-matrices-and-rotations-b3}
[B3: Rodrigues in an example]

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \R_{\e_3, \theta} \) from Rodrigues' formula and check that it is \( \R_{\theta} \oplus [1] \).
2. Compute \( \R_{\n, 2\pi/3} \) for \( \n = \tfrac1{\sqrt3}(1, 1, 1) \), and identify the resulting matrix.
:::
:::

::: {.solution}
(a) With \( \n = \e_3 \) we have \( \K = \begin{pmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} \) and \( \K^2 = \e_3\e_3\tp - \I_3 = \diag(-1, -1, 0) \). Hence
\[
\R_{\e_3,\theta} = \I_3 + \sin\theta\,\K + (1 - \cos\theta)\K^2
= \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix},
\]
the diagonal entries being \( 1 - (1 - \cos\theta) = \cos\theta \) twice and \( 1 \) once. This is \( \R_{\theta} \oplus [1] \), the rotation of the \( (\e_1, \e_2) \)-plane, as it must be.

(b) Here \( \cos\theta = -\tfrac12 \) and \( \sin\theta = \tfrac{\sqrt3}2 \). Writing \( \1 = (1,1,1) \), so that \( \n = \1/\sqrt3 \) and \( \n\n\tp = \tfrac13\1\1\tp \),
\[
\begin{aligned}
\sin\theta\,\K &= \tfrac{\sqrt3}{2}\cdot\tfrac1{\sqrt3}\,\K_{\1}
 = \tfrac12\begin{pmatrix} 0 & -1 & 1 \\ 1 & 0 & -1 \\ -1 & 1 & 0 \end{pmatrix}, \\
(1 - \cos\theta)\K^2 &= \tfrac32\bigl(\tfrac13\1\1\tp - \I_3\bigr)
 = \tfrac12\1\1\tp - \tfrac32\I_3 .
\end{aligned}
\]
Adding \( \I_3 \) to these two gives \( \tfrac12\1\1\tp - \tfrac12\I_3 \) plus the skew part. The first piece has \( 0 \) on the diagonal and \( \tfrac12 \) elsewhere, and adding the skew part turns each off-diagonal pair \( \tfrac12, \tfrac12 \) into \( 0, 1 \):
\[
\R_{\n,2\pi/3} = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} .
\]
This is the cyclic shift \( \e_1 \mapsto \e_2 \mapsto \e_3 \mapsto \e_1 \), which is the matrix \( \B\A \) of @exm-rotations-do-not-commute: same axis \( (1,1,1) \), same angle \( 2\pi/3 \).
:::

### C. Going deeper

::: {#exr-orthogonal-matrices-and-rotations-c1}
[C1: The plane, re-derived]

::: {.enumerate options="label=(\alph*)"}
1. Use @thm-orthogonal-canonical-form to prove that every \( \Q \in \Orth(2) \) is either orthogonally similar to \( \R_{\theta} \) for a unique \( \theta \in [0, \pi] \), or orthogonally similar to \( \diag(1, -1) \).
2. Chapter 10 proved more: \( \Q \) **equals** \( \R_{\theta} \) or \( \M_{\theta} \) (@thm-orthogonal-2x2). Explain exactly what information (a) loses, and why the canonical form must lose it.
3. Deduce that any two reflections of \( \nR^2 \) are orthogonally similar, and that \( \R_{\alpha} \) and \( \R_{\beta} \) are orthogonally similar if and only if \( \beta = \pm\alpha \).
:::
:::

::: {.solution}
(a) With \( n = 2 \), \( p + q + 2m = 2 \). If \( m = 1 \) then \( p = q = 0 \) and the form is \( \R_{\theta_1} \) with \( \theta_1 \in (0, \pi) \). If \( m = 0 \) then \( (p, q) \in \{(2,0), (1,1), (0,2)\} \), giving \( \I_2 = \R_0 \), \( \diag(1,-1) \) and \( -\I_2 = \R_{\pi} \). So the possibilities are \( \R_{\theta} \) with \( \theta \in [0, \pi] \) and \( \diag(1, -1) \), and they are distinguished by the determinant. Uniqueness of \( \theta \) follows from @thm-orthogonal-canonical-form, or directly from \( \tr\R_{\theta} = 2\cos\theta \) and the injectivity of \( \cos \) on \( [0, \pi] \).

(b) Part (a) determines \( \Q \) only up to orthogonal similarity, that is, up to a change of orthonormal coordinates. It therefore cannot see *which* line is the mirror of a reflection, nor the sign of the angle of a rotation. It must lose the mirror, because the mirror moves: if \( \P \) is the rotation by \( \varphi \) then \( \P\M_{\theta}\P\tp = \M_{\theta + 2\varphi} \), so all the \( \M_{\theta} \) are conjugate. It must lose the sign of the angle, because conjugating by \( \diag(1, -1) \) sends \( \R_{\theta} \) to \( \R_{-\theta} \).

(c) Every reflection has determinant \( -1 \), so by (a) each is orthogonally similar to \( \diag(1,-1) \), and orthogonal similarity is an equivalence relation, so any two of them are similar to each other. For rotations: if \( \beta = \pm\alpha \) then \( \R_{\beta} = \R_{\alpha} \) or \( \R_{\beta} = \diag(1,-1)\R_{\alpha}\diag(1,-1) \), so they are orthogonally similar. Conversely, similar matrices have equal traces (@thm-trace-similarity-invariant), so \( \cos\alpha = \cos\beta \), which for real angles means \( \beta \equiv \pm\alpha \) modulo \( 2\pi \).
:::

::: {#exr-orthogonal-matrices-and-rotations-c2}
[C2: Products of rotations]

::: {.enumerate options="label=(\alph*)"}
1. Prove that the product of two rotations of \( \nR^3 \) is a rotation of \( \nR^3 \), and explain which theorem supplies the axis.
2. Let \( \A \) and \( \B \) be the half-turns about two **perpendicular** axes \( \Span(\a) \) and \( \Span(\b) \), with \( \a \perp \b \) unit vectors. Prove that \( \A\B \) is the half-turn about the axis \( \Span(\a \times \b) \).
3. Deduce that every rotation of \( \nR^3 \) is a product of two half-turns.
:::

*Hint for (c): use @thm-cartan-dieudonne-small, or the description of a half-turn in the Quick check after @thm-rodrigues.*
:::

::: {.solution}
(a) \( \SO(3) \) is a group (@prp-orthogonal-group-properties (c)), so if \( \A, \B \in \SO(3) \) then \( \A\B \in \SO(3) \). By @cor-so3-is-rotation, \( \A\B \) fixes a line pointwise and rotates the perpendicular plane; that corollary is what supplies the axis, and it does so through the count \( p \ge 1 \) in the canonical form.

(b) Extend \( (\a, \b) \) to an orthonormal basis \( (\a, \b, \c) \) of \( \nR^3 \), where we may take \( \c = \a \times \b \): it is a unit vector orthogonal to \( \a \) and \( \b \) by @lem-cross-matrix-properties (d). By the Quick check after @thm-rodrigues, \( \A = 2\a\a\tp - \I_3 \) fixes \( \a \) and negates \( \a^{\perp} \), so in the basis \( (\a, \b, \c) \), \( \A \) is \( \diag(1, -1, -1) \) and \( \B \) is \( \diag(-1, 1, -1) \). Their product is \( \diag(-1, -1, 1) \), which fixes \( \c \) and negates \( \c^{\perp} \): the half-turn about \( \Span(\c) = \Span(\a \times \b) \). (Its trace is \( -1 \), confirming \( \theta = \pi \) through @thm-rotation-angle-trace (a).)

(c) Let \( \Q = \R_{\n,\theta} \in \SO(3) \), with \( \n \) a unit vector and \( \theta \in [0,\pi] \) (@thm-rodrigues (c)). Choose a unit \( \w \perp \n \), and work throughout in the orthonormal basis \( \sB = (\n, \w, \K_{\n}\w) \) of @thm-rodrigues (b), in which \( \Q \) has matrix \( [1] \oplus \R_{\theta} \). Put \( \w' = \R_{\n, \theta/2}\w \), again a unit vector perpendicular to \( \n \), since \( \R_{\n,\theta/2} \) fixes \( \n \) and is an isometry; by @thm-rodrigues (b) its coordinate vector in \( \sB \) is \( \d = (0, \cos\tfrac\theta2, \sin\tfrac\theta2) \). Let \( \A \) and \( \B \) be the half-turns about \( \Span(\w') \) and \( \Span(\w) \), so that in \( \sB \) their matrices are \( 2\d\d\tp - \I_3 \) and \( \diag(-1, 1, -1) \) respectively, by the Quick check after @thm-rodrigues. Using \( 2\cos^2\tfrac\theta2 - 1 = \cos\theta \), \( 2\sin^2\tfrac\theta2 - 1 = -\cos\theta \) and \( 2\cos\tfrac\theta2\sin\tfrac\theta2 = \sin\theta \),
\[
2\d\d\tp - \I_3 = [-1] \oplus \begin{pmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{pmatrix} .
\]
Multiplying the two matrices blockwise, \( \A\B \) has matrix
\[
[1] \oplus \begin{pmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
= [1] \oplus \R_{\theta},
\]
which is the matrix of \( \Q \) in the same basis. Hence \( \Q = \A\B \).
:::

::: {#exr-orthogonal-matrices-and-rotations-c3}
[C3: Moving one point of the sphere to another]

Let \( S = \{ \x \in \nR^3 : \norm{\x} = 1 \} \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that for all \( \u, \v \in S \) there is \( \Q \in \SO(3) \) with \( \Q\u = \v \). (One says that \( \SO(3) \) **acts transitively** on \( S \).)
2. Prove that \( \{ \Q \in \SO(3) : \Q\u = \u \} = \{ \R_{\u,\theta} : \theta \in \nR \} \), and that this set is an abelian subgroup of \( \SO(3) \).
3. Is the analogue of (a) true for \( \SO(2) \) acting on the unit circle of \( \nR^2 \)? And for \( \SO(4) \) acting on the unit sphere of \( \nR^4 \)? Justify your answers.
:::
:::

::: {.solution}
(a) Extend \( \u \) to an orthonormal basis \( (\u, \a_2, \a_3) \) of \( \nR^3 \) (@cor-extend-orthonormal-basis), and likewise extend \( \v \) to \( (\v, \b_2, \b_3) \). Let \( \A = (\u \mid \a_2 \mid \a_3) \) and \( \B = (\v \mid \b_2 \mid \b_3) \); both are orthogonal, since their columns are orthonormal (@thm-isometry-characterizations (f)). Replacing \( \a_3 \) by \( -\a_3 \) changes the sign of \( \det\A \) and keeps the basis orthonormal, so we may assume \( \det\A = 1 \), and likewise \( \det\B = 1 \). Put \( \Q = \B\A\tp \). Then \( \Q \in \Orth(3) \) and \( \det\Q = \det\B\det\A\tp = 1 \) by @thm-det-multiplicative and @thm-det-transpose, so \( \Q \in \SO(3) \); and \( \A\tp\u = \e_1 \), because the entries of \( \A\tp\u \) are the inner products of \( \u \) with the columns of \( \A \), so \( \Q\u = \B\e_1 = \v \).

(b) \( (\supseteq) \) Each \( \R_{\u,\theta} \) lies in \( \SO(3) \) and fixes \( \u \), by @thm-rodrigues (b). \( (\subseteq) \) If \( \Q \in \SO(3) \) fixes \( \u \), write \( \Q = \R_{\n,\theta} \) with \( \theta \in [0, \pi] \) (@thm-rodrigues (c)). If \( \theta = 0 \) then \( \Q = \I_3 = \R_{\u, 0} \). Otherwise the fixed space of \( \Q \) is exactly the line \( \Span(\n) \), since in the basis of @thm-rodrigues (b) the matrix is \( [1] \oplus \R_{\theta} \) and \( \R_{\theta} \) fixes no non-zero vector for \( \theta \in (0, \pi] \); so \( \u = \pm\n \), and \( \R_{-\n,\theta} = \R_{\n,-\theta} \) gives \( \Q = \R_{\u, \pm\theta} \). For the group claim: all these matrices are simultaneously \( [1] \oplus \R_{\theta} \) in the *same* orthonormal basis \( (\u, \w, \K_{\u}\w) \), and \( \R_{\alpha}\R_{\beta} = \R_{\alpha+\beta} = \R_{\beta}\R_{\alpha} \), so the set is closed under products and inverses and is abelian.

(c) Yes for \( \SO(2) \): given unit \( \u, \v \in \nR^2 \), write \( \u = (\cos\alpha, \sin\alpha) \) and \( \v = (\cos\beta, \sin\beta) \) and take \( \Q = \R_{\beta - \alpha} \), which is in \( \SO(2) \) and sends \( \u \) to \( \v \). Yes for \( \SO(4) \) as well, by the same argument as (a): extend \( \u \) and \( \v \) to orthonormal bases of \( \nR^4 \), fix the determinants to \( 1 \) by flipping the sign of the last vector if necessary, and take \( \Q = \B\A\tp \). Nothing in that argument used the dimension \( 3 \) — transitivity holds for \( \SO(n) \) with \( n \ge 2 \). What is special to \( n = 3 \) is the classification of the maps themselves, not their ability to move one unit vector to another.
:::
