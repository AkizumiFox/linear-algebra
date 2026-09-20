# Principal Angles

The sections so far measured how far eigenvalues move. The next section asks how far **eigenvectors** move, and more generally invariant subspaces, and before it can answer it needs a way to say how far apart two subspaces are. For two lines there is an obvious answer, the angle between them. This section shows that for subspaces of dimension \( k \ge 2 \) one angle is not enough, and that the right replacement is a list of \( k \) angles read off from a singular value decomposition. It then proves the two facts Section 9 will use: the sines of these angles are the singular values of a matrix built from the orthogonal complement, and the largest sine is the distance between the two orthogonal projections.

**Throughout**, \( F \) is \( \nR \) or \( \nC \), and \( F^n \) carries its standard inner product \( \inner{\x}{\y} = \y^{*}\x \), with \( \x^{*} = \x\tp \) when \( F = \nR \). For a subspace \( U \) of \( F^n \), \( P_U \) is the orthogonal projection onto \( U \) (@def-orthogonal-projection), identified with its matrix in the standard basis. Singular values of a matrix with \( k \) columns follow the convention of Chapter 16 §09: \( \sigma_i \coloneqq 0 \) for \( \min(\text{rows}, k) < i \le k \), so that \( \sigma_i^2 \) is the \( i \)-th largest eigenvalue of \( \A^{*}\A \) for every \( i \le k \) (@eq-sv-eigen).

## One angle is not enough

For two lines \( \Span(\u) \) and \( \Span(\w) \) there is one number to compute, the angle between them. For planes the first idea is to copy it: call the angle between \( U \) and \( W \) the **smallest** angle between a line in \( U \) and a line in \( W \).

That idea fails at once in \( \nR^3 \). Two distinct planes \( U, W \subseteq \nR^3 \) always meet in a line, since
\[
\dim(U \cap W) = 2 + 2 - \dim(U + W) \ge 4 - 3 = 1
\]
by @thm-dimension-formula-subspace-dim. So the smallest angle is \( 0 \) for **every** pair of planes: it cannot tell a plane tilted by one degree from a plane at right angles.

Taking the **largest** such angle instead does no better in \( \nR^4 \). Let \( U = \Span(\e_1, \e_2) \) and compare
\[
W_1 = \Span(\e_1, \e_3), \qquad W_2 = \Span(\e_3, \e_4) .
\]
Each contains a vector perpendicular to all of \( U \) (namely \( \e_3 \)), so each has a line at angle \( \pi/2 \) from \( U \). But \( W_1 \) shares the whole line \( \Span(\e_1) \) with \( U \), while \( W_2 \) is perpendicular to \( U \) in every direction. One number cannot record both facts. A list can: \( (0, \pi/2) \) for \( W_1 \) and \( (\pi/2, \pi/2) \) for \( W_2 \). The rest of this section explains where such a list comes from in general, when the subspaces are not lined up with the coordinate axes.

*Two subspaces can be given orthonormal bases that face each other in pairs; the principal angles are the angles between the partners.*

## Principal angles

Everything will be computed from orthonormal bases written as the columns of a matrix, so we first record how such matrices behave.

Let \( U \subseteq F^n \) be a subspace with \( \dim U = k \ge 1 \). An **orthonormal basis matrix** of \( U \) is a matrix \( \Q \in M_{n \times k}(F) \) whose columns form an orthonormal basis of \( U \). One exists: apply Gram–Schmidt (@thm-gram-schmidt) to any basis of \( U \).

::: {#lem-orthonormal-basis-matrix}
[Orthonormal Basis Matrices]

Let \( U \subseteq F^n \) have dimension \( k \ge 1 \) and let \( \Q \in M_{n \times k}(F) \) be an orthonormal basis matrix of \( U \).

::: {.enumerate options="label=(\alph*)"}
1. \( \Q^{*}\Q = \I_k \) and \( P_U = \Q\Q^{*} \).
2. \( \norm{\Q\y} = \norm{\y} \) for every \( \y \in F^k \). For every matrix \( \Y \) with \( k \) rows and every matrix \( \Z \) with \( k \) columns,
   \[
   \begin{aligned}
   \norm{\Q\Y}_2 &= \norm{\Y}_2, & \norm{\Q\Y}_F &= \norm{\Y}_F, \\
   \norm{\Z\Q^{*}}_2 &= \norm{\Z}_2, & \norm{\Z\Q^{*}}_F &= \norm{\Z}_F .
   \end{aligned}
   \]
3. Every orthonormal basis matrix of \( U \) is \( \Q\R \) for some \( \R \in \Unit(k) \) (orthogonal when \( F = \nR \)).
4. \( \I_n - P_U = P_{U^{\perp}} \). If moreover \( k < n \) and \( \Q_{\perp} \in M_{n \times (n-k)}(F) \) is an orthonormal basis matrix of \( U^{\perp} \), then the square matrix \( (\Q \mid \Q_{\perp}) \) is unitary, and
   \[
   \Q\Q^{*} + \Q_{\perp}\Q_{\perp}^{*} = \I_n .
   \]
:::
:::

::: {.proof}
(a) The \( (i, j) \) entry of \( \Q^{*}\Q \) is \( \q_i^{*}\q_j = \inner{\q_j}{\q_i} = \delta_{ij} \), because the columns \( \q_1, \dots, \q_k \) are orthonormal. By @thm-projection-formula (a), for every \( \v \in F^n \),
\[
P_U\v = \sum_{i=1}^{k}\inner{\v}{\q_i}\q_i = \sum_{i=1}^{k}\q_i(\q_i^{*}\v) = \Q\Q^{*}\v ,
\]
the last step being column-times-row expansion of \( \Q\Q^{*} \).

(b) By (a), \( \norm{\Q\y}^2 = \y^{*}\Q^{*}\Q\y = \y^{*}\y = \norm{\y}^2 \). Hence \( \norm{\Q\Y\x} = \norm{\Y\x} \) for every \( \x \), and taking the maximum over unit \( \x \) (@def-operator-norm) gives \( \norm{\Q\Y}_2 = \norm{\Y}_2 \). For the Frobenius norm, \( \norm{\Q\Y}_F^2 = \tr(\Y^{*}\Q^{*}\Q\Y) = \tr(\Y^{*}\Y) = \norm{\Y}_F^2 \). Next, \( \norm{\Z\Q^{*}}_F^2 = \tr(\Q\Z^{*}\Z\Q^{*}) = \tr(\Z^{*}\Z\Q^{*}\Q) = \norm{\Z}_F^2 \), by @thm-trace-properties (c). For the spectral norm, let \( \x \in F^n \). By the first sentence and (a), \( \norm{\Q^{*}\x} = \norm{\Q\Q^{*}\x} = \norm{P_U\x} \le \norm{\x} \) (@thm-projection-formula (c)). So \( \norm{\Z\Q^{*}\x} \le \norm{\Z}_2\norm{\Q^{*}\x} \le \norm{\Z}_2\norm{\x} \) by @thm-operator-norm-properties (a), and \( \norm{\Z\Q^{*}}_2 \le \norm{\Z}_2 \). Conversely, choose a unit \( \y \in F^k \) with \( \norm{\Z\y} = \norm{\Z}_2 \) (@lem-operator-norm-attained). Then \( \x = \Q\y \) is a unit vector with \( \Z\Q^{*}\x = \Z\y \), so \( \norm{\Z\Q^{*}}_2 \ge \norm{\Z}_2 \).

(c) Let \( \Q' \) be another orthonormal basis matrix of \( U \), and put \( \R = \Q^{*}\Q' \in M_k(F) \). Each column of \( \Q' \) lies in \( U \), where \( P_U \) is the identity, so \( \Q' = P_U\Q' = \Q\Q^{*}\Q' = \Q\R \) by (a). Then \( \R^{*}\R = \Q'^{*}\Q\Q^{*}\Q' = \Q'^{*}P_U\Q' = \Q'^{*}\Q' = \I_k \), so the square matrix \( \R \) is unitary (@def-unitary-orthogonal).

(d) For the first identity, let \( \v \in F^n \) and write \( \v = \u + \w \) with \( \u \in U \) and \( \w \in U^{\perp} \), which is possible in exactly one way by @thm-orthogonal-decomposition (a). Then \( P_U\v = \u \) by @def-orthogonal-projection. Since \( (U^{\perp})^{\perp} = U \) by @thm-orthogonal-decomposition (b), the splitting \( \v = \w + \u \) is also the one that defines \( P_{U^{\perp}} \), so \( P_{U^{\perp}}\v = \w = \v - P_U\v \). As \( \v \) was arbitrary, \( \I_n - P_U = P_{U^{\perp}} \). Nothing here restricts \( k \): when \( k = n \), \( U^{\perp} = \{\0\} \) and both sides are \( \0 \).

Now let \( k < n \). The columns of \( \Q \) and of \( \Q_{\perp} \) are orthonormal, and each column of \( \Q \) is orthogonal to each column of \( \Q_{\perp} \) because \( U \perp U^{\perp} \). Their number is \( k + (n - k) = n \), by @thm-orthogonal-decomposition (c). So the square matrix \( \O = (\Q \mid \Q_{\perp}) \in M_n(F) \) satisfies \( \O^{*}\O = \I_n \), hence is unitary, and then \( \O\O^{*} = \I_n \) as well, since \( \O^{*} = \O^{-1} \). By block multiplication (@thm-block-multiplication), \( \O\O^{*} = \Q\Q^{*} + \Q_{\perp}\Q_{\perp}^{*} \). This also re-proves the first identity here, since \( \Q_{\perp}\Q_{\perp}^{*} = P_{U^{\perp}} \) by (a) applied to \( U^{\perp} \).
:::

Now the definition. The question is how much of \( U \) survives when it is projected into \( W \). By parts (a) and (b) of the lemma, for a unit vector \( \u = \Q_U\y \) of \( U \) the surviving length is \( \norm{P_W\u} = \norm{\Q_W\Q_W^{*}\u} = \norm{\Q_W^{*}\u} = \norm{(\Q_W^{*}\Q_U)\y} \). So the matrix \( \Q_W^{*}\Q_U \) records the answer for every direction of \( U \) at once, and its singular values are the stretch factors along the best directions.

::: {#def-principal-angles}
[Principal Angles]

Let \( U, W \subseteq F^n \) be subspaces with
\[
1 \le k = \dim U \le l = \dim W ,
\]
and let \( \Q_U \in M_{n \times k}(F) \) and \( \Q_W \in M_{n \times l}(F) \) be orthonormal basis matrices of \( U \) and \( W \). The **principal angles** between \( U \) and \( W \) are the \( k \) numbers
\[
0 \le \theta_1 \le \theta_2 \le \dots \le \theta_k \le \frac{\pi}{2}
\]
determined by
\[
\cos\theta_i = \sigma_i(\Q_W^{*}\Q_U) \qquad (i = 1, \dots, k) .
\]
We write \( \Theta(U, W) = \diag(\theta_1, \dots, \theta_k) \) and \( \sin\Theta(U, W) = \diag(\sin\theta_1, \dots, \sin\theta_k) \).
:::

In words: fix orthonormal bases of the two subspaces, form the \( l \times k \) matrix whose \( (i, j) \) entry is the inner product of the \( j \)-th basis vector of \( U \) with the \( i \)-th basis vector of \( W \), and take its \( k \) singular values. These lie in \( [0, 1] \), as we check next, so each is the cosine of exactly one angle in \( [0, \pi/2] \). The largest cosine gives the **smallest** angle, so the decreasing singular values produce increasing angles. The number of angles is the **smaller** dimension, \( k \), and the definition asks for \( k \le l \); for a pair with \( \dim U > \dim W \), swap the names. The two notations at the end are for use in norms: \( \norm{\sin\Theta(U, W)}_2 = \sin\theta_k \), the largest entry of a non-negative diagonal matrix (@lem-hermitian-spectral-norm), and \( \norm{\sin\Theta(U, W)}_F = \bigl(\sum_i\sin^2\theta_i\bigr)^{1/2} \).

**Well-definedness.** Three things need checking. The answer must not depend on the orthonormal bases chosen. The singular values must be at most \( 1 \), or there is no angle. And when \( k = l \) the definition treats \( U \) and \( W \) asymmetrically, so we should check that swapping them changes nothing.

::: {#prp-principal-angles-well-defined}
[Principal Angles Are Well Defined]

In the setting of @def-principal-angles, put \( \M = \Q_W^{*}\Q_U \in M_{l \times k}(F) \).

::: {.enumerate options="label=(\alph*)"}
1. The singular values of \( \M \) do not depend on the choice of the orthonormal basis matrices \( \Q_U \) and \( \Q_W \).
2. \( 1 \ge \sigma_1(\M) \ge \dots \ge \sigma_k(\M) \ge 0 \), so \( \theta_1, \dots, \theta_k \) exist, are unique, and are non-decreasing.
3. \( \sigma_i(\Q_U^{*}\Q_W) = \sigma_i(\M) \) for \( i = 1, \dots, k \). In particular, if \( k = l \), the principal angles between \( W \) and \( U \) are those between \( U \) and \( W \).
4. If \( k = 1 \) and \( U = \Span(\u) \) with \( \norm{\u} = 1 \), then \( \cos\theta_1 = \norm{P_W\u} \). If also \( l = 1 \) and \( W = \Span(\w) \) with \( \norm{\w} = 1 \), then \( \cos\theta_1 = \lvert\inner{\u}{\w}\rvert \).
:::
:::

::: {.proof}
(a) By @lem-orthonormal-basis-matrix (c), any other choices are \( \Q_U\R \) and \( \Q_W\R' \) with \( \R \in \Unit(k) \) and \( \R' \in \Unit(l) \). The new matrix is \( \M' = \R'^{*}\M\R \), and
\[
\M'^{*}\M' = \R^{*}\M^{*}\R'\R'^{*}\M\R = \R^{*}(\M^{*}\M)\R ,
\]
using \( \R'\R'^{*} = \I_l \). Since \( \R^{*} = \R^{-1} \), this is similar to \( \M^{*}\M \), so the two have the same characteristic polynomial (@thm-charpoly-similarity-invariant) and the same eigenvalues with multiplicity. By @def-singular-values, \( \M' \) and \( \M \) have the same singular values.

(b) By @thm-operator-norm-properties (d) and @lem-orthonormal-basis-matrix (b), \( \norm{\M}_2 \le \norm{\Q_W^{*}}_2\norm{\Q_U}_2 \), and \( \norm{\Q_U}_2 = \norm{\Q_U\I_k}_2 = \norm{\I_k}_2 = 1 \) by @thm-operator-norm-properties (c). Also \( \norm{\Q_W^{*}\x} = \norm{P_W\x} \le \norm{\x} \), as in the proof of that lemma, so \( \norm{\Q_W^{*}}_2 \le 1 \). Hence \( \sigma_1(\M) = \norm{\M}_2 \le 1 \) by @thm-operator-norm-formulas (c), and all singular values lie in \( [0, 1] \). The cosine is a strictly decreasing bijection from \( [0, \pi/2] \) onto \( [0, 1] \), so each \( \sigma_i(\M) \) is \( \cos\theta_i \) for exactly one \( \theta_i \in [0, \pi/2] \), and \( \sigma_1 \ge \dots \ge \sigma_k \) gives \( \theta_1 \le \dots \le \theta_k \).

(c) Let \( \M = \Y\vSigma\Z^{*} \) be a singular value decomposition (@thm-svd). Then \( \M^{*} = \Z\vSigma\tp\Y^{*} \), where \( \Z, \Y \) are unitary and \( \vSigma\tp \in M_{k \times l}(\nR) \) carries the same diagonal entries \( \sigma_1(\M) \ge \dots \ge \sigma_k(\M) \) and zeros elsewhere. So this is a factorization of \( \M^{*} \) of the shape in @thm-svd, and @thm-singular-values-unique gives \( \sigma_i(\M^{*}) = \sigma_i(\M) \). Since \( \M^{*} = \Q_U^{*}\Q_W \), this is the first claim. When \( k = l \), the principal angles between \( W \) and \( U \) are defined by \( \sigma_i(\Q_U^{*}\Q_W) \), so they coincide with those between \( U \) and \( W \).

(d) With \( \Q_U = \u \), the matrix \( \M = \Q_W^{*}\u \) is a single column, and its one singular value is \( (\M^{*}\M)^{1/2} = \norm{\Q_W^{*}\u} \). By @lem-orthonormal-basis-matrix (b) and (a), \( \norm{\Q_W^{*}\u} = \norm{\Q_W\Q_W^{*}\u} = \norm{P_W\u} \). If \( l = 1 \) and \( \Q_W = \w \), then \( \M = \w^{*}\u = \inner{\u}{\w} \), whose singular value is \( \lvert\inner{\u}{\w}\rvert \).
:::

**Examples.**

1. **Two lines in \( \nR^2 \).** For \( \u = \e_1 \) and \( \w = (1, 1)/\sqrt2 \), part (d) gives \( \cos\theta_1 = 1/\sqrt2 \), so \( \theta_1 = \pi/4 \). Replacing \( \w \) by \( -\w \) changes neither the line nor the answer.
2. **Nested subspaces.** If \( U \subseteq W \), then every column of \( \Q_U \) is fixed by \( P_W \), so \( \M^{*}\M = \Q_U^{*}\Q_W\Q_W^{*}\Q_U = \Q_U^{*}P_W\Q_U = \Q_U^{*}\Q_U = \I_k \). All singular values are \( 1 \) and all principal angles are \( 0 \). The degenerate case \( U = W \) is included, and it is the reason the angles start at \( 0 \).
3. **Perpendicular subspaces.** If \( U \subseteq W^{\perp} \), every entry of \( \M \) is the inner product of a vector of \( U \) with a vector of \( W \), hence \( 0 \), so all principal angles are \( \pi/2 \).
4. **The planes of the opening.** For \( U = \Span(\e_1, \e_2) \) and \( W_1 = \Span(\e_1, \e_3) \), take the standard vectors as orthonormal bases. Then \( \M = \Q_{W_1}\tp\Q_U = \begin{psmallmatrix} 1 & 0 \\ 0 & 0 \end{psmallmatrix} \), with singular values \( 1, 0 \), so the principal angles are \( (0, \pi/2) \). For \( W_2 = \Span(\e_3, \e_4) \) we are in Example 3, with angles \( (\pi/2, \pi/2) \). These are the two lists that the single-number attempts could not tell apart.

**Non-example by minimal change.** In Example 4, replace the orthonormal basis \( (\e_1, \e_3) \) of \( W_1 \) by the basis \( (\e_1, (\e_1 + \e_3)/\sqrt2) \), whose vectors still have length \( 1 \) but are no longer orthogonal. The matrix of inner products becomes \( \begin{psmallmatrix} 1 & 0 \\ 1/\sqrt2 & 0 \end{psmallmatrix} \), with largest singular value \( \sqrt{3/2} > 1 \), and no angle has that cosine. What fails is the orthogonality of the columns of \( \Q_W \): without it, \( \Q_W\Q_W^{*} \) is not the projection \( P_W \), and the matrix no longer measures how much of \( U \) survives in \( W \).

**Why this definition: the principal vectors.** The singular value decomposition of \( \M \) does more than produce numbers. It produces bases of \( U \) and \( W \) in which the whole configuration is visible, and this is the precise meaning of the slogan.

::: {#prp-principal-vectors}
[Principal Vectors]

In the setting of @def-principal-angles, let \( \Q_W^{*}\Q_U = \Y\vSigma\Z^{*} \) be a singular value decomposition, with \( \Y \in M_l(F) \) and \( \Z \in M_k(F) \) unitary, columns \( \y_1, \dots, \y_l \) and \( \z_1, \dots, \z_k \). Put
\[
\u_i = \Q_U\z_i \ (1 \le i \le k), \qquad \w_j = \Q_W\y_j \ (1 \le j \le l) .
\]
Then \( (\u_1, \dots, \u_k) \) is an orthonormal basis of \( U \), \( (\w_1, \dots, \w_l) \) is an orthonormal basis of \( W \), and
\[
\inner{\u_i}{\w_j} = \begin{cases} \cos\theta_i & \text{if } i = j, \\ 0 & \text{if } i \ne j . \end{cases}
\]
:::

::: {.proof}
The matrix \( \Q_U\Z \) has columns \( \u_1, \dots, \u_k \), all in \( U \), and \( (\Q_U\Z)^{*}(\Q_U\Z) = \Z^{*}\Z = \I_k \) by @lem-orthonormal-basis-matrix (a). So the \( \u_i \) are \( k \) orthonormal vectors of \( U \). They are linearly independent (@thm-orthogonal-independent), and \( \dim U = k \), so they form a basis. The same argument applies to the \( \w_j \) in \( W \). Finally,
\[
\inner{\u_i}{\w_j} = \w_j^{*}\u_i = \y_j^{*}(\Q_W^{*}\Q_U)\z_i = \y_j^{*}\Y\vSigma\Z^{*}\z_i = \e_j^{*}\vSigma\e_i ,
\]
which is the \( (j, i) \) entry of \( \vSigma \): it equals \( \sigma_i = \cos\theta_i \) when \( j = i \), and \( 0 \) otherwise.
:::

So \( U \) and \( W \) have orthonormal bases that face each other in pairs. Each \( \u_i \) makes the angle \( \theta_i \) with its partner \( \w_i \), in the sense of part (d) of the proposition, and is perpendicular to every other \( \w_j \). The last \( l - k \) vectors of \( W \) have no partner, and they are perpendicular to all of \( U \). The vectors \( \u_i, \w_i \) are called **principal vectors**. Two subspaces, however they sit in \( F^n \), look like a list of \( k \) independent pairs of lines, and the principal angles are the angles within the pairs.

The principal vectors are usually **not** the basis vectors one started with. For \( U = W = \nR^2 \) with bases \( (\e_1, \e_2) \) and \( ((\e_1 + \e_2)/\sqrt2, (\e_1 - \e_2)/\sqrt2) \), each given basis vector of \( U \) is at angle \( \pi/4 \) from each given basis vector of \( W \). The principal angles are nevertheless \( 0, 0 \), by Example 2, since the subspaces are equal. Pairing the given columns one by one measures the bases, not the subspaces.

::: {.warning}
**Lines have no orientation, so principal angles use \( \lvert\inner{\u}{\w}\rvert \) and lie in \( [0, \pi/2] \).** The angle of @def-angle is between **vectors** in a **real** space, and it can reach \( \pi \). For \( \u = \e_1 \) and \( \w = -\e_1 \) in \( \nR^2 \) that angle is \( \pi \), yet \( \Span(\u) = \Span(\w) \) and the principal angle is \( 0 \). Over \( \nC \) the vector angle is not even defined: \( \u = \e_1 \) and \( \w = i\e_1 \) span the same complex line, \( \inner{\u}{\w} = \conj{i} = -i \) is not real, and the principal angle is again \( 0 \) because \( \lvert -i\rvert = 1 \).
:::

::: {.check}
Find the principal angle between the line \( U = \Span\bigl((1, 2, 2)\bigr) \) and the plane \( W = \{\x \in \nR^3 : x_3 = 0\} \).
:::

::: {.solution}
Here \( k = 1 \le 2 = l \). The unit vector \( \u = \tfrac13(1, 2, 2) \) spans \( U \), and \( P_W\u = \tfrac13(1, 2, 0) \), since \( (\e_1, \e_2) \) is an orthonormal basis of \( W \) (@thm-projection-formula (a)). By @prp-principal-angles-well-defined (d), \( \cos\theta_1 = \norm{P_W\u} = \sqrt5/3 \). So \( \theta_1 = \arccos(\sqrt5/3) \approx 41.8^\circ \), and \( \sin\theta_1 = 2/3 \), which is the distance from \( \u \) to the plane.
:::

## Sines and the orthogonal complement

The cosines measure how much of \( U \) survives projection into \( W \). What Section 9 can actually bound is the part that does **not** survive: the component of \( U \) in \( W^{\perp} \). Pythagoras says the two parts are complementary, and the theorem makes this exact.

::: {#thm-sines-of-principal-angles}
[Sines of Principal Angles]

Let \( U, W \subseteq F^n \) with \( 1 \le k = \dim U \le l = \dim W \), principal angles \( \theta_1 \le \dots \le \theta_k \), and orthonormal basis matrices \( \Q_U, \Q_W \).

::: {.enumerate options="label=(\alph*)"}
1. Suppose \( l < n \), and let \( \Q_{W^{\perp}} \in M_{n \times (n-l)}(F) \) be an orthonormal basis matrix of \( W^{\perp} \). Put \( \M = \Q_W^{*}\Q_U \) and \( \N = \Q_{W^{\perp}}^{*}\Q_U \in M_{(n-l) \times k}(F) \). Then
   \[
   \M^{*}\M + \N^{*}\N = \I_k ,
   \]
   and the eigenvalues of \( \N^{*}\N \), with multiplicity, are \( \sin^2\theta_1, \dots, \sin^2\theta_k \). Equivalently, \( \sigma_i(\N) = \sin\theta_{k+1-i} \) for \( i = 1, \dots, k \), with the convention for \( \sigma_i \) stated at the start of the section.
2. For every \( l \le n \),
   \[
   \norm{(\I - P_W)P_U}_2 = \norm{(\I - P_W)\Q_U}_2 = \sin\theta_k = \norm{\sin\Theta(U, W)}_2 ,
   \]
   and
   \[
   \norm{(\I - P_W)P_U}_F = \norm{(\I - P_W)\Q_U}_F = \norm{\sin\Theta(U, W)}_F .
   \]
:::
:::

::: {.idea}
Split the identity of \( F^n \) along \( W \oplus W^{\perp} \) and sandwich it between \( \Q_U^{*} \) and \( \Q_U \). That gives two Hermitian \( k \times k \) matrices adding up to \( \I_k \), and such matrices share their eigenvectors, with eigenvalues \( c \) and \( 1 - c \). The first has eigenvalues \( \cos^2\theta_i \) by definition, so the second has eigenvalues \( \sin^2\theta_i \). Part (b) then removes the orthonormal factors, which change no norm.
:::

::: {.proof}
(a) By @lem-orthonormal-basis-matrix (d) applied to \( W \), \( \I_n = \Q_W\Q_W^{*} + \Q_{W^{\perp}}\Q_{W^{\perp}}^{*} \). Multiplying on the left by \( \Q_U^{*} \) and on the right by \( \Q_U \), and using \( \Q_U^{*}\Q_U = \I_k \) (part (a) of the lemma), gives \( \I_k = \M^{*}\M + \N^{*}\N \).

The matrix \( \M^{*}\M \in M_k(F) \) is Hermitian (real symmetric when \( F = \nR \)). By @cor-spectral-complex-matrix (or @cor-spectral-real-matrix when \( F = \nR \)) there is an orthonormal basis \( \z_1, \dots, \z_k \) of \( F^k \) consisting of eigenvectors of \( \M^{*}\M \). Since \( \M \) has \( l \ge k \) rows, all \( k \) eigenvalues of \( \M^{*}\M \) are squared singular values (@def-singular-values), so we may number the \( \z_i \) so that \( \M^{*}\M\z_i = \sigma_i(\M)^2\z_i = \cos^2\theta_i\,\z_i \). Then
\[
\N^{*}\N\z_i = (\I_k - \M^{*}\M)\z_i = (1 - \cos^2\theta_i)\z_i = \sin^2\theta_i\,\z_i .
\]
So the unitary matrix with columns \( \z_1, \dots, \z_k \) diagonalizes \( \N^{*}\N \) with diagonal \( \sin^2\theta_1, \dots, \sin^2\theta_k \), and these are its eigenvalues with multiplicity (@thm-charpoly-similarity-invariant). The sine is increasing on \( [0, \pi/2] \), so in decreasing order they read \( \sin^2\theta_k \ge \dots \ge \sin^2\theta_1 \ge 0 \). By @eq-sv-eigen, the \( i \)-th largest eigenvalue of \( \N^{*}\N \) is \( \sigma_i(\N)^2 \) for every \( i \le k \), with the stated convention. Taking non-negative square roots gives \( \sigma_i(\N) = \sin\theta_{k+1-i} \).

(b) If \( l = n \), then \( W = F^n \), so \( U \subseteq W \) and every \( \theta_i = 0 \) (Example 2 above), while \( \I - P_W = \0 \); all four norms are \( 0 \). Suppose \( l < n \). By @lem-orthonormal-basis-matrix (d) and (a),
\[
(\I - P_W)\Q_U = \Q_{W^{\perp}}\Q_{W^{\perp}}^{*}\Q_U = \Q_{W^{\perp}}\N ,
\]
and \( (\I - P_W)P_U = \Q_{W^{\perp}}\N\Q_U^{*} \). By part (b) of the lemma, applied to \( \Q_{W^{\perp}} \) and then to \( \Q_U \), both matrices have the spectral and Frobenius norms of \( \N \). Now \( \norm{\N}_2 = \sigma_1(\N) = \sin\theta_k \) by @thm-operator-norm-formulas (c) and part (a). Also \( \norm{\N}_F^2 = \tr(\N^{*}\N) \), which is the sum of the eigenvalues of \( \N^{*}\N \) (@thm-trace-det-eigenvalues), that is \( \sum_i\sin^2\theta_i = \norm{\sin\Theta(U, W)}_F^2 \). This proves the theorem.
:::

Part (b) has a plain geometric reading. For a unit vector \( \u \in U \), the vector \( (\I - P_W)\u \) is the error in approximating \( \u \) from \( W \), and its length is the distance from \( \u \) to \( W \) (@thm-best-approximation). So \( \sin\theta_k \) is the **largest distance from a unit vector of \( U \) to \( W \)**, and \( \theta_k \) is the worst angle any direction of \( U \) makes with \( W \). That is the number to bound when one asks whether a computed subspace is close to the true one, and part (a) turns it into the norm of the concrete matrix \( \Q_{W^{\perp}}^{*}\Q_U \). In Section 9, \( U \) will be an invariant subspace of \( \A \) and \( W \) the corresponding one for \( \A + \E \). The columns of \( \Q_{W^{\perp}} \) will be the remaining eigenvectors of \( \A + \E \), and \( \N \) will turn out to satisfy a Sylvester equation, so the bounds of Section 7 will apply to it.

## The distance between two subspaces

A subspace is determined by its orthogonal projection, since \( U = \im P_U \) by @thm-projection-direct-sum (b), applied to \( F^n = U \oplus U^{\perp} \). So a second natural way to compare \( U \) and \( W \) is the size of \( P_U - P_W \). When the dimensions agree, this measures exactly the largest principal angle.

::: {#thm-projection-difference-norm}
[The Distance Between Projections]

Let \( U, W \subseteq F^n \) with \( \dim U = \dim W = k \ge 1 \), and principal angles \( \theta_1 \le \dots \le \theta_k \). Then

::: {.enumerate options="label=(\alph*)"}
1. \( \norm{P_U - P_W}_2 = \sin\theta_k \);
2. \( \norm{P_U - P_W}_F = \sqrt2\,\norm{\sin\Theta(U, W)}_F \);
3. \( \norm{P_U - P_W}_2 \le 1 \), with equality if and only if \( U \cap W^{\perp} \ne \{\0\} \).
:::
:::

::: {.idea}
For (b), the **squared** Frobenius norm of the Hermitian matrix \( \D = P_U - P_W \) is \( \tr(\D^2) \), which expands into traces of projections: \( k + k - 2\tr(P_UP_W) \), and \( \tr(P_UP_W) = \sum\cos^2\theta_i \). For (a), split \( \x = \x_1 + \x_2 \) along \( U \oplus U^{\perp} \). Then \( \D \) sends \( \x_1 \) to \( (\I - P_W)\x_1 \in W^{\perp} \) and \( \x_2 \) to \( -P_W\x_2 \in W \), so Pythagoras separates the two contributions. The first is controlled by the sines for \( (U, W) \), the second by the sines for \( (W, U) \), and equal dimensions make these the same list.
:::

::: {.proof}
Put \( \D = P_U - P_W \), and let \( \Q_U, \Q_W \) be orthonormal basis matrices and \( \M = \Q_W^{*}\Q_U \in M_k(F) \).

(b) By @lem-orthonormal-basis-matrix (a), \( P_U = \Q_U\Q_U^{*} \) and \( P_W = \Q_W\Q_W^{*} \) are Hermitian and satisfy \( P_U^2 = P_U \), \( P_W^2 = P_W \). Hence \( \D \) is Hermitian and
\[
\begin{aligned}
\norm{\D}_F^2 &= \tr(\D^{*}\D) = \tr(\D^2) \\
&= \tr(P_U) + \tr(P_W) - \tr(P_UP_W) - \tr(P_WP_U) .
\end{aligned}
\]
By @thm-trace-properties (c), \( \tr(P_U) = \tr(\Q_U^{*}\Q_U) = \tr(\I_k) = k \), likewise \( \tr(P_W) = k \), and \( \tr(P_WP_U) = \tr(P_UP_W) \). Also
\[
\begin{aligned}
\tr(P_UP_W) &= \tr(\Q_U\Q_U^{*}\Q_W\Q_W^{*}) \\
&= \tr(\Q_W^{*}\Q_U\Q_U^{*}\Q_W) = \tr(\M\M^{*}) ,
\end{aligned}
\]
and \( \tr(\M\M^{*}) = \norm{\M^{*}}_F^2 = \norm{\M}_F^2 = \tr(\M^{*}\M) = \sum_i\cos^2\theta_i \), since the eigenvalues of \( \M^{*}\M \) are \( \cos^2\theta_1, \dots, \cos^2\theta_k \) (@def-singular-values, @thm-trace-det-eigenvalues). Therefore
\[
\norm{\D}_F^2 = 2k - 2\sum_{i=1}^{k}\cos^2\theta_i = 2\sum_{i=1}^{k}\sin^2\theta_i ,
\]
which is (b).

(a) Put \( s = \sin\theta_k \). By @thm-sines-of-principal-angles (b), \( \norm{(\I - P_W)P_U}_2 = s \). The same theorem with the roles of \( U \) and \( W \) exchanged, which is allowed because \( \dim W = \dim U \), gives \( \norm{(\I - P_U)P_W}_2 = s \) too, because by @prp-principal-angles-well-defined (c) the principal angles between \( W \) and \( U \) are those between \( U \) and \( W \).

Let \( \x \in F^n \), and write \( \x_1 = P_U\x \in U \) and \( \x_2 = \x - \x_1 \in U^{\perp} \) (@def-orthogonal-projection). Then \( P_U\x = \x_1 \) and \( P_W\x = P_W\x_1 + P_W\x_2 \), so
\[
\D\x = (\I - P_W)\x_1 - P_W\x_2 .
\]
The first term lies in \( W^{\perp} \) and the second in \( W \), by @thm-orthogonal-decomposition, so they are orthogonal, and by @thm-pythagoras
\[
\norm{\D\x}^2 = \norm{(\I - P_W)\x_1}^2 + \norm{P_W\x_2}^2 .
\]{#eq-projection-difference-split}
We bound the two terms. Since \( \x_1 = P_U\x_1 \), \( \norm{(\I - P_W)\x_1} = \norm{(\I - P_W)P_U\x_1} \le s\norm{\x_1} \) by @thm-operator-norm-properties (a). For the second term, \( P_W \) is Hermitian and idempotent and \( \x_2 = (\I - P_U)\x_2 \), so
\[
\begin{aligned}
\norm{P_W\x_2}^2 &= \inner{P_W\x_2}{\x_2} = \inner{P_W\x_2}{(\I - P_U)\x_2} \\
&= \inner{(\I - P_U)P_W(P_W\x_2)}{\x_2} \le s\,\norm{P_W\x_2}\,\norm{\x_2} ,
\end{aligned}
\]
using @thm-projection-formula (b) for \( \I - P_U = P_{U^{\perp}} \) (@lem-orthonormal-basis-matrix (d)), then \( P_W = P_W^2 \), then Cauchy–Schwarz (@thm-cauchy-schwarz) with \( \norm{(\I - P_U)P_W}_2 = s \). Hence \( \norm{P_W\x_2} \le s\norm{\x_2} \), the case \( P_W\x_2 = \0 \) being trivial. Adding, and using \( \norm{\x_1}^2 + \norm{\x_2}^2 = \norm{\x}^2 \) (@thm-pythagoras),
\[
\norm{\D\x}^2 \le s^2\bigl(\norm{\x_1}^2 + \norm{\x_2}^2\bigr) = s^2\norm{\x}^2 .
\]
So \( \norm{\D}_2 \le s \). For the reverse, @thm-sines-of-principal-angles (b) gives \( \norm{(\I - P_W)\Q_U}_2 = s \), and by @lem-operator-norm-attained there is a unit \( \y \in F^k \) with \( \norm{(\I - P_W)\Q_U\y} = s \). The vector \( \x = \Q_U\y \in U \) is a unit vector (@lem-orthonormal-basis-matrix (b)) with \( P_U\x = \x \), so \( \D\x = (\I - P_W)\x \) and \( \norm{\D\x} = s \). Hence \( \norm{\D}_2 = s \).

(c) By (a) and @prp-principal-angles-well-defined (b), \( \norm{\D}_2 = \sin\theta_k \le 1 \), with equality if and only if \( \cos\theta_k = \sigma_k(\M) = 0 \). The square matrix \( \M \) has \( \sigma_k(\M) = 0 \) if and only if \( \rank\M < k \) (@thm-svd), that is, if and only if \( \M\y = \0 \) for some \( \y \ne \0 \). Put \( \u = \Q_U\y \), which is a non-zero vector of \( U \) exactly when \( \y \ne \0 \), by @lem-orthonormal-basis-matrix (b). Then \( \M\y = \Q_W^{*}\u \), and \( \Q_W^{*}\u = \0 \) if and only if \( P_W\u = \Q_W\Q_W^{*}\u = \0 \), again by parts (b) and (a) of the lemma. Finally \( P_W\u = \0 \) means that \( \u \in \ker P_W = W^{\perp} \), by @thm-projection-direct-sum (b) applied to \( F^n = W \oplus W^{\perp} \). So equality holds if and only if \( U \) contains a non-zero vector of \( W^{\perp} \).
:::

The factor \( \sqrt2 \) in (b) has a clean explanation. When \( k = l \), the principal vectors of @prp-principal-vectors give \( P_U = \sum_i\u_i\u_i^{*} \) and \( P_W = \sum_i\w_i\w_i^{*} \) (@lem-orthonormal-basis-matrix (a)), so \( P_U - P_W \) is a sum of the \( k \) terms \( \u_i\u_i^{*} - \w_i\w_i^{*} \). These act in the mutually orthogonal planes \( \Span(\u_i, \w_i) \). Each term is Hermitian with trace \( 0 \) and rank at most \( 2 \), so its non-zero eigenvalues are a pair \( \pm t_i \), and being Hermitian it is normal, so \( \norm{\u_i\u_i^{*} - \w_i\w_i^{*}}_F^2 = t_i^2 + t_i^2 \) by @thm-schur-inequality. On the other hand, expanding the trace with \( \u_i^{*}\u_i = \w_i^{*}\w_i = 1 \) and \( \lvert\inner{\u_i}{\w_i}\rvert = \cos\theta_i \) (@prp-principal-vectors),
\[
\norm{\u_i\u_i^{*} - \w_i\w_i^{*}}_F^2 = 2 - 2\lvert\inner{\u_i}{\w_i}\rvert^2 = 2\sin^2\theta_i ,
\]
so \( t_i = \sin\theta_i \). Each angle is therefore counted twice in the Frobenius norm and once in the spectral norm. The worked example below shows the \( \pm \) pairs explicitly.

::: {#exm-two-planes-in-r4}
[Two Planes in Four Dimensions]

Let \( U = \Span(\e_1, \e_2) \subseteq \nR^4 \) and \( W = \Span(\a, \b) \), where
\[
\a = (3, 4, 4, 3), \qquad \b = (3, -4, 4, -3) .
\]
Find the principal angles, a pair of principal vectors for each, the sines from @thm-sines-of-principal-angles, and \( \norm{P_U - P_W} \) in both norms. Then check the last two numbers directly.
:::

::: {.solution}
**Orthonormal bases.** \( \inner{\a}{\b} = 9 - 16 + 16 - 9 = 0 \) and \( \norm{\a}^2 = \norm{\b}^2 = 50 \), so \( \Q_W = \frac{1}{5\sqrt2}(\a \mid \b) \) is an orthonormal basis matrix of \( W \), and \( \Q_U = (\e_1 \mid \e_2) \). The matrix \( \Q_W\tp\Q_U \) holds the first two entries of \( \a \) and \( \b \):
\[
\M = \Q_W\tp\Q_U = \frac{1}{5\sqrt2}\begin{pmatrix} 3 & 4 \\ 3 & -4 \end{pmatrix}, \qquad \M\tp\M = \begin{pmatrix} 9/25 & 0 \\ 0 & 16/25 \end{pmatrix} .
\]
So the singular values are \( 4/5 \) and \( 3/5 \), and
\[
\theta_1 = \arccos\tfrac45 \approx 36.87^\circ, \qquad \theta_2 = \arccos\tfrac35 \approx 53.13^\circ .
\]
Note \( \sin\theta_1 = 3/5 = \cos\theta_2 \), so \( \theta_1 + \theta_2 = \pi/2 \) here.

**Principal vectors.** The eigenvector of \( \M\tp\M \) for \( 16/25 \) is \( \z_1 = \e_2 \), and \( \y_1 = \M\z_1/\sigma_1 = \frac{1}{5\sqrt2}(4, -4)\cdot\frac54 = \frac{1}{\sqrt2}(1, -1) \). By @prp-principal-vectors,
\[
\u_1 = \e_2, \qquad \w_1 = \Q_W\y_1 = \tfrac{1}{10}(\a - \b) = \bigl(0, \tfrac45, 0, \tfrac35\bigr) ,
\]
and \( \inner{\u_1}{\w_1} = 4/5 \). Likewise \( \z_2 = \e_1 \), \( \y_2 = \frac{1}{\sqrt2}(1, 1) \), \( \u_2 = \e_1 \) and \( \w_2 = \frac{1}{10}(\a + \b) = (\tfrac35, 0, \tfrac45, 0) \), with \( \inner{\u_2}{\w_2} = 3/5 \), while \( \inner{\u_1}{\w_2} = \inner{\u_2}{\w_1} = 0 \). So \( W \) is obtained from \( U \) by tilting \( \e_2 \) towards \( \e_4 \) through \( \theta_1 \) and \( \e_1 \) towards \( \e_3 \) through \( \theta_2 \), in two perpendicular planes.

**Sines.** The vectors \( \c = (4, -3, -3, 4) \) and \( \d = (4, 3, -3, -4) \) are orthogonal to \( \a \), to \( \b \) and to each other:
\[
\begin{aligned}
\inner{\c}{\a} &= 12 - 12 - 12 + 12 = 0, & \inner{\c}{\b} &= 12 + 12 - 12 - 12 = 0, \\
\inner{\d}{\a} &= 12 + 12 - 12 - 12 = 0, & \inner{\d}{\b} &= 12 - 12 - 12 + 12 = 0,
\end{aligned}
\]
and \( \inner{\c}{\d} = 16 - 9 + 9 - 16 = 0 \). Also \( \norm{\c}^2 = \norm{\d}^2 = 50 \). Since \( \dim W^{\perp} = 2 \) (@thm-orthogonal-decomposition (c)), \( \Q_{W^{\perp}} = \frac{1}{5\sqrt2}(\c \mid \d) \) is an orthonormal basis matrix of \( W^{\perp} \), and
\[
\N = \Q_{W^{\perp}}\tp\Q_U = \frac{1}{5\sqrt2}\begin{pmatrix} 4 & -3 \\ 4 & 3 \end{pmatrix}, \qquad \N\tp\N = \begin{pmatrix} 16/25 & 0 \\ 0 & 9/25 \end{pmatrix} .
\]
Its eigenvalues are \( 16/25 = \sin^2\theta_2 \) and \( 9/25 = \sin^2\theta_1 \), and \( \M\tp\M + \N\tp\N = \I_2 \), as @thm-sines-of-principal-angles (a) says.

**Distances.** By @thm-projection-difference-norm, \( \norm{P_U - P_W}_2 = \sin\theta_2 = 4/5 \) and \( \norm{P_U - P_W}_F = \sqrt2\bigl(\tfrac{9}{25} + \tfrac{16}{25}\bigr)^{1/2} = \sqrt2 \).

**Direct check.** By @lem-orthonormal-basis-matrix (a), \( P_W = \Q_W\Q_W\tp = \frac{1}{50}(\a\a\tp + \b\b\tp) \), and
\[
P_W = \frac{1}{50}\begin{pmatrix} 18 & 0 & 24 & 0 \\ 0 & 32 & 0 & 24 \\ 24 & 0 & 32 & 0 \\ 0 & 24 & 0 & 18 \end{pmatrix}, \qquad P_U = \diag(1, 1, 0, 0) .
\]
In \( \D = P_U - P_W \), coordinates \( 1, 3 \) do not interact with coordinates \( 2, 4 \), and the two \( 2 \times 2 \) blocks are
\[
\frac{1}{50}\begin{pmatrix} 32 & -24 \\ -24 & -32 \end{pmatrix}, \qquad \frac{1}{50}\begin{pmatrix} 18 & -24 \\ -24 & -18 \end{pmatrix} .
\]
Each is symmetric with trace \( 0 \), so its eigenvalues are \( \pm\sqrt{-\det} \): \( \pm\frac{1}{50}\sqrt{32^2 + 24^2} = \pm\frac45 \) and \( \pm\frac{1}{50}\sqrt{18^2 + 24^2} = \pm\frac35 \). So \( \D \) has eigenvalues \( \pm\frac45, \pm\frac35 \). By @lem-hermitian-spectral-norm, \( \norm{\D}_2 = 4/5 \), and \( \norm{\D}_F^2 = \tr(\D^2) = 2\bigl(\tfrac{16}{25} + \tfrac{9}{25}\bigr) = 2 \). Both agree with the theorem, and the eigenvalues come in the \( \pm\sin\theta_i \) pairs described before the example.
:::

::: {.remark}
**A metric, and why the dimensions must match.** On the set of \( k \)-dimensional subspaces of \( F^n \), the number \( d(U, W) = \norm{P_U - P_W}_2 = \sin\theta_k \) is a metric. It is symmetric. It is zero only when \( P_U = P_W \), that is, when \( U = \im P_U = \im P_W = W \). And it satisfies the triangle inequality because \( \norm{\cdot}_2 \) is a norm (@thm-operator-norm-properties (b)). Between subspaces of **different** dimensions it is useless. If \( k < l \), then \( \dim(W \cap U^{\perp}) \ge l + (n - k) - n > 0 \) by @thm-dimension-formula-subspace-dim, so some unit \( \w \in W \) is perpendicular to \( U \). For it \( (P_U - P_W)\w = -\w \), so \( \norm{P_U - P_W}_2 \ge 1 \). On the other hand, @eq-projection-difference-split, which did not use the dimensions, together with \( \norm{P\v} \le \norm{\v} \) for orthogonal projections (@thm-projection-formula (c)), gives \( \norm{P_U - P_W}_2 \le 1 \). So the distance is exactly \( 1 \), whatever the principal angles are. This is why Section 9 always compares invariant subspaces of the same dimension.
:::

## Exercises

### A. Check your understanding

:::: {#exr-principal-angles-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the principal angles between subspaces \( U, W \subseteq F^n \) with \( 1 \le \dim U \le \dim W \).
2. True or false: if \( U \subseteq W \), then every principal angle between \( U \) and \( W \) is \( 0 \). Justify your answer.
3. True or false: the principal angle between \( \Span(\u) \) and \( \Span(-\u) \), for \( \u \ne \0 \), is \( \pi \). Justify your answer.
4. True or false: if \( U \cap W \ne \{\0\} \), then \( \theta_1 = 0 \). Justify your answer.
5. State the formula for \( \norm{P_U - P_W}_2 \) in terms of principal angles, with its hypothesis.
6. True or false: for two distinct lines \( U, W \) in \( \nR^2 \), \( \norm{P_U - P_W}_2 < 1 \). Justify your answer.
:::
::::

::: {.solution}
(a) Choose orthonormal basis matrices \( \Q_U \in M_{n \times k}(F) \) and \( \Q_W \in M_{n \times l}(F) \). The principal angles \( 0 \le \theta_1 \le \dots \le \theta_k \le \pi/2 \) are defined by \( \cos\theta_i = \sigma_i(\Q_W^{*}\Q_U) \), \( i = 1, \dots, k \) (@def-principal-angles). They do not depend on the bases (@prp-principal-angles-well-defined).

(b) True. As in Example 2 after @prp-principal-angles-well-defined, \( \M^{*}\M = \Q_U^{*}P_W\Q_U = \Q_U^{*}\Q_U = \I_k \), so every \( \cos\theta_i = 1 \).

(c) False. The two lines are equal, so the angle is \( 0 \): with \( \u_0 = \u/\norm{\u} \), \( \lvert\inner{\u_0}{-\u_0}\rvert = 1 \) (@prp-principal-angles-well-defined (d)). The value \( \pi \) is the angle between the vectors \( \u \) and \( -\u \) of @def-angle, which is a different notion.

(d) True. Take a unit \( \u \in U \cap W \) and write \( \u = \Q_U\y \) with \( \norm{\y} = 1 \) (@lem-orthonormal-basis-matrix (b)). Then \( \norm{\M\y} = \norm{\Q_W^{*}\u} = \norm{P_W\u} = \norm{\u} = 1 \), so \( \sigma_1(\M) = \norm{\M}_2 \ge 1 \). With @prp-principal-angles-well-defined (b), \( \cos\theta_1 = 1 \).

(e) If \( \dim U = \dim W = k \ge 1 \), then \( \norm{P_U - P_W}_2 = \sin\theta_k \), the sine of the largest principal angle (@thm-projection-difference-norm (a)).

(f) False. The two axes \( U = \Span(\e_1) \) and \( W = \Span(\e_2) \) have \( U \cap W^{\perp} = U \ne \{\0\} \), so \( \norm{P_U - P_W}_2 = 1 \) by @thm-projection-difference-norm (c). Directly, \( P_U - P_W = \diag(1, -1) \).
:::

### B. Practice

:::: {#exr-principal-angles-b1}
[B1: Two planes in three dimensions]

Let \( U = \Span(\e_1, \e_2) \) and \( W = \Span\bigl((1, 0, 0), (1, 3, 4)\bigr) \) in \( \nR^3 \).

::: {.enumerate options="label=(\alph*)"}
1. Find an orthonormal basis matrix of \( W \).
2. Compute the principal angles between \( U \) and \( W \).
3. Hence compute \( \norm{P_U - P_W}_2 \) and \( \norm{P_U - P_W}_F \).
4. Explain why \( \theta_1 = 0 \) could have been predicted without computation.
:::
::::

::: {.solution}
(a) Gram–Schmidt: \( \q_1 = \e_1 \), and \( (1, 3, 4) - \inner{(1, 3, 4)}{\e_1}\e_1 = (0, 3, 4) \), of length \( 5 \), so \( \q_2 = (0, \tfrac35, \tfrac45) \) and \( \Q_W = (\q_1 \mid \q_2) \).

(b) With \( \Q_U = (\e_1 \mid \e_2) \), the matrix \( \M = \Q_W\tp\Q_U \) holds the first two entries of \( \q_1 \) and \( \q_2 \):
\[
\M = \begin{pmatrix} 1 & 0 \\ 0 & 3/5 \end{pmatrix} .
\]
It is diagonal with non-negative entries, so \( \M\tp\M = \diag(1, \tfrac{9}{25}) \) and the singular values are \( 1 \) and \( \tfrac35 \). So \( \theta_1 = 0 \) and \( \theta_2 = \arccos\tfrac35 \approx 53.13^\circ \), with \( \sin\theta_2 = \tfrac45 \).

(c) By @thm-projection-difference-norm, \( \norm{P_U - P_W}_2 = \sin\theta_2 = \tfrac45 \) and \( \norm{P_U - P_W}_F = \sqrt2\,(0 + \tfrac{16}{25})^{1/2} = \tfrac{4\sqrt2}{5} \).

(d) Two planes in \( \nR^3 \) meet in a line (@thm-dimension-formula-subspace-dim, as in the opening of the section), and a common unit vector forces \( \cos\theta_1 = 1 \) (Exercise A1 (d)). Here the common line is \( \Span(\e_1) \).
:::

:::: {#exr-principal-angles-b2}
[B2: Which projections are at distance one?]

Determine, for each pair, whether \( \norm{P_U - P_W}_2 = 1 \). Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( U = \Span(\e_1, \e_2) \) and \( W = \Span(\e_2, \e_3) \) in \( \nR^3 \).
2. \( U = \Span\bigl((1, 1, 0)\bigr) \) and \( W = \Span\bigl((1, -1, 1)\bigr) \) in \( \nR^3 \).
3. \( U = \Span(\e_1, \e_2) \) and \( W = \Span\bigl((1, 0, 1), (0, 1, 1)\bigr) \) in \( \nR^3 \).
4. \( U = \Span\bigl((1, 2, 3)\bigr) \) and \( W = \Span\bigl((1, 0, 0), (0, 1, 0)\bigr) \) in \( \nR^3 \).
:::
::::

::: {.solution}
(a) Yes. \( W^{\perp} = \Span(\e_1) \subseteq U \), so \( U \cap W^{\perp} \ne \{\0\} \), and @thm-projection-difference-norm (c) applies since both dimensions are \( 2 \).

(b) Yes. \( \inner{(1, 1, 0)}{(1, -1, 1)} = 0 \), so \( U \subseteq W^{\perp} \), and (c) of the theorem applies with \( k = 1 \).

(c) No. Both are planes, and \( W^{\perp} = \Span\bigl((1, 1, -1)\bigr) \), since \( (1, 1, -1) \) is orthogonal to both spanning vectors of \( W \) and \( \dim W^{\perp} = 1 \). This vector has non-zero third entry, so it is not in \( U \), and \( U \cap W^{\perp} = \{\0\} \). By the theorem, \( \norm{P_U - P_W}_2 < 1 \). (In fact the principal angles are \( 0 \) and \( \arccos(1/\sqrt3) \), so the distance is \( \sqrt{2/3} \).)

(d) Yes, for a different reason: the dimensions are \( 1 \) and \( 2 \), and the remark after @exm-two-planes-in-r4 shows that \( \norm{P_U - P_W}_2 = 1 \) whenever the dimensions differ. The theorem itself does not apply. Its principal angle \( \theta_1 = \arccos(\sqrt5/\sqrt{14}) \) is far from \( \pi/2 \), which illustrates why the projection distance is only used for equal dimensions.
:::

:::: {#exr-principal-angles-b3}
[B3: Two lines]

Let \( \u, \w \in F^n \) be unit vectors and \( c = \lvert\inner{\u}{\w}\rvert \). Prove that
\[
\norm{\u\u^{*} - \w\w^{*}}_2 = \sqrt{1 - c^2}, \qquad \norm{\u\u^{*} - \w\w^{*}}_F = \sqrt2\,\sqrt{1 - c^2} .
\]
::::

::: {.solution}
Let \( U = \Span(\u) \) and \( W = \Span(\w) \), both of dimension \( 1 \). By @lem-orthonormal-basis-matrix (a) with \( \Q_U = \u \) and \( \Q_W = \w \), \( P_U = \u\u^{*} \) and \( P_W = \w\w^{*} \). By @prp-principal-angles-well-defined (d), the single principal angle satisfies \( \cos\theta_1 = c \), so \( \sin\theta_1 = \sqrt{1 - c^2} \), since \( \sin\theta_1 \ge 0 \) on \( [0, \pi/2] \). Now @thm-projection-difference-norm (a) and (b) with \( k = 1 \) give \( \norm{P_U - P_W}_2 = \sin\theta_1 \) and \( \norm{P_U - P_W}_F = \sqrt2\sin\theta_1 \), which are the two claims.
:::

### C. Going deeper

:::: {#exr-principal-angles-c1}
[C1: Counting zero and right angles]

Let \( U, W \subseteq F^n \) with \( 1 \le k = \dim U \le l = \dim W \), orthonormal basis matrices \( \Q_U, \Q_W \), and \( \M = \Q_W^{*}\Q_U \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \y^{*}(\I_k - \M^{*}\M)\y = \norm{(\I - P_W)\Q_U\y}^2 \) for every \( \y \in F^k \).
2. Deduce that the number of principal angles equal to \( 0 \) is \( \dim(U \cap W) \).
3. Prove that the number of principal angles equal to \( \pi/2 \) is \( \dim(U \cap W^{\perp}) \).
:::

*Hint for (b): a positive semidefinite matrix \( \B \) with \( \y^{*}\B\y = 0 \) has \( \B\y = \0 \).*
::::

::: {.solution}
(a) Let \( \u = \Q_U\y \). By @lem-orthonormal-basis-matrix (a) and (b), \( \y^{*}\y = \norm{\u}^2 \) and \( \y^{*}\M^{*}\M\y = \norm{\Q_W^{*}\u}^2 = \norm{P_W\u}^2 \). Since \( \u = P_W\u + (\I - P_W)\u \) with the two parts orthogonal (@thm-orthogonal-decomposition), @thm-pythagoras gives \( \norm{\u}^2 - \norm{P_W\u}^2 = \norm{(\I - P_W)\u}^2 \).

(b) Put \( \B = \I_k - \M^{*}\M \). It is Hermitian, and by (a) it is positive semidefinite (@def-positive-semidefinite). Its eigenvalues are \( 1 - \cos^2\theta_i = \sin^2\theta_i \), with an orthonormal eigenbasis \( \z_1, \dots, \z_k \) (as in the proof of @thm-sines-of-principal-angles). So the number of \( i \) with \( \theta_i = 0 \) is the number of zero eigenvalues, which is \( \dim\ker\B \).

We claim \( \ker\B = \{\y : \Q_U\y \in W\} \). If \( \B\y = \0 \), then \( \y^{*}\B\y = 0 \), so \( (\I - P_W)\Q_U\y = \0 \) by (a), and \( \Q_U\y = P_W\Q_U\y \in W \). Conversely, if \( \Q_U\y \in W \), then \( \y^{*}\B\y = 0 \) by (a). Writing \( \y = \sum_ic_i\z_i \), this says \( \sum_i\sin^2\theta_i\lvert c_i\rvert^2 = 0 \). So \( c_i = 0 \) whenever \( \sin\theta_i \ne 0 \), and then \( \B\y = \sum_ic_i\sin^2\theta_i\z_i = \0 \). This proves the claim; the second half of it is the fact in the hint, proved here for this \( \B \).

The map \( \y \mapsto \Q_U\y \) is linear and injective (@lem-orthonormal-basis-matrix (b)). It carries \( \ker\B \) onto \( \{\u \in U : \u \in W\} = U \cap W \), because every vector of \( U \) is \( \Q_U\y \) for some \( \y \). So \( \dim\ker\B = \dim(U \cap W) \).

(c) \( \theta_i = \pi/2 \) exactly when \( \sigma_i(\M) = 0 \). The number of non-zero singular values of \( \M \) is \( \rank\M \) (@thm-svd), so the number of zero ones among the \( k \) is \( k - \rank\M = \dim\ker\M \), by the Rank–Nullity Theorem (@thm-rank-nullity) for \( \y \mapsto \M\y \) on \( F^k \). Next, \( \M\y = \Q_W^{*}\Q_U\y = \0 \) if and only if \( P_W\Q_U\y = \Q_W(\Q_W^{*}\Q_U\y) = \0 \), because \( \Q_W \) is injective. That holds if and only if \( \Q_U\y \in W^{\perp} \). As in (b), \( \y \mapsto \Q_U\y \) carries \( \ker\M \) injectively onto \( U \cap W^{\perp} \), so the count is \( \dim(U \cap W^{\perp}) \).
:::

:::: {#exr-principal-angles-c2}
[C2: The smallest angle as a maximum]

Let \( U, W \subseteq F^n \) with \( 1 \le k = \dim U \le l = \dim W \) and principal angles \( \theta_1 \le \dots \le \theta_k \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that
   \[
   \cos\theta_1 = \max\bigl\{\lvert\inner{\u}{\w}\rvert : \u \in U,\ \w \in W,\ \norm{\u} = \norm{\w} = 1\bigr\} ,
   \]
   and that the maximum is attained at the principal vectors \( \u_1, \w_1 \).
2. Deduce that \( \theta_1 \) is the smallest principal angle between a line of \( U \) and a line of \( W \), which is the notion tried and rejected at the start of the section.
3. Hence explain, in one sentence, why \( \theta_1 \) alone cannot distinguish the pairs \( (U, W_1) \) and \( (U, U) \) of the opening, but the full list \( \theta_1, \theta_2 \) can.
:::
::::

::: {.solution}
(a) Let \( \u \in U \) and \( \w \in W \) be unit vectors. By @lem-orthonormal-basis-matrix (a) and (b), \( \u = \Q_U\y \) and \( \w = \Q_W\z \) with \( \y = \Q_U^{*}\u \) and \( \z = \Q_W^{*}\w \) unit vectors. Then \( \inner{\u}{\w} = \z^{*}\Q_W^{*}\Q_U\y = \z^{*}\M\y \), and by Cauchy–Schwarz and @thm-operator-norm-properties (a),
\[
\lvert\inner{\u}{\w}\rvert \le \norm{\z}\,\norm{\M\y} \le \norm{\M}_2 = \sigma_1(\M) = \cos\theta_1 ,
\]
using @thm-operator-norm-formulas (c). By @prp-principal-vectors, the unit vectors \( \u_1 \in U \) and \( \w_1 \in W \) satisfy \( \inner{\u_1}{\w_1} = \cos\theta_1 \), so the maximum exists and equals \( \cos\theta_1 \).

(b) By @prp-principal-angles-well-defined (d), the principal angle between the lines \( \Span(\u) \) and \( \Span(\w) \) is \( \arccos\lvert\inner{\u}{\w}\rvert \). Since \( \arccos \) is decreasing, the smallest such angle corresponds to the largest \( \lvert\inner{\u}{\w}\rvert \), which by (a) is \( \cos\theta_1 \).

(c) Both pairs share a line, so both have \( \theta_1 = 0 \), and the first number cannot separate them. The second angle is \( \pi/2 \) for \( (U, W_1) \) and \( 0 \) for \( (U, U) \), by Examples 4 and 2 after @prp-principal-angles-well-defined.
:::
