# Spectral Resolutions and Functions of a Normal Operator

The last two sections produce an orthonormal basis of eigenvectors. A basis, though, is a choice: permute it, or rotate inside the eigenspace of a repeated eigenvalue, and the basis changes while the operator does not. This section rewrites the same information with nothing chosen — a list of eigenvalues, and the orthogonal projections onto their eigenspaces — and then spends it. Once an operator is written as \( \lambda_1P_1 + \dots + \lambda_kP_k \), any function whatsoever on those \( k \) numbers produces a new operator, and powers, square roots and exponentials all become one line of arithmetic on the spectrum.

Throughout, \( V \) is a **non-zero** finite-dimensional inner product space over \( F = \nR \) or \( F = \nC \), and \( T \in \cL(V) \). We say that \( T \) satisfies

\[
(\ast) \qquad V \text{ has an orthonormal basis of eigenvectors of } T .
\]

By @thm-spectral-complex this holds over \( \nC \) exactly for the **normal** operators, and by @thm-spectral-real it holds over \( \nR \) exactly for the **self-adjoint** ones. Stating everything for an operator satisfying \( (\ast) \) covers both fields at once, and keeps in view the only property we ever use.

## Grouping an eigenbasis by eigenvalue

Here is the observation the section runs on. Let \( (\e_1, \dots, \e_n) \) be an orthonormal eigenbasis of \( T \), with \( T\e_j = \mu_j\e_j \). The list \( \mu_1, \dots, \mu_n \) repeats: an eigenvalue of geometric multiplicity \( 3 \) appears three times. Sort the basis vectors into bundles by the eigenvalue they carry, and each bundle spans one eigenspace. Summing the coordinates of a vector inside one bundle is exactly projecting it onto that eigenspace — orthogonally, because the basis is orthonormal. So \( T \) is a weighted sum of perpendicular projections, one weight per **distinct** eigenvalue, and the weights and the projections no longer remember the basis.

*A normal operator is a sum of perpendicular projections, weighted by its distinct eigenvalues.*

::: {#def-spectral-resolution}
[Spectral Resolution]

Let \( T \in \cL(V) \) satisfy \( (\ast) \), let \( \lambda_1, \dots, \lambda_k \) be the **distinct** eigenvalues of \( T \), and write \( E_i = E_{\lambda_i}(T) \) for the corresponding eigenspaces. Let
\[
P_i \coloneqq P_{E_i} \in \cL(V)
\]
be the **orthogonal** projection onto \( E_i \) (@def-orthogonal-projection). The identity
\[
T = \lambda_1P_1 + \lambda_2P_2 + \dots + \lambda_kP_k
\]
is the **spectral resolution** of \( T \), and the family \( (P_1, \dots, P_k) \) is the **resolution of the identity** attached to \( T \).
:::

Two clauses carry weight. The eigenvalues are listed **once each**, so \( k \) is the number of distinct eigenvalues and not \( \dim V \); and the projections are **orthogonal**, which is the whole content of the definition, since every diagonalizable operator has *some* such expression with oblique projections. That the displayed identity is true, and that the \( P_i \) fit together as neatly as one could want, is the next theorem.

:::: {#thm-spectral-resolution}
[The Spectral Resolution and Its Projections]

Let \( T \in \cL(V) \) satisfy \( (\ast) \), with distinct eigenvalues \( \lambda_1, \dots, \lambda_k \), eigenspaces \( E_i = E_{\lambda_i}(T) \) and \( P_i = P_{E_i} \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( V = E_1 \oplus \dots \oplus E_k \), and \( E_i \perp E_j \) whenever \( i \ne j \);
2. \( P_i^{*} = P_i \) and \( P_i^2 = P_i \) for every \( i \), and \( P_iP_j = 0 \) whenever \( i \ne j \);
3. \( P_1 + \dots + P_k = \id_V \);
4. \( T = \lambda_1P_1 + \dots + \lambda_kP_k \);
5. \( TP_i = P_iT = \lambda_iP_i \) for every \( i \).
:::
::::

::: {.idea}
Everything is read off one orthonormal eigenbasis. Sorting its vectors by eigenvalue cuts it into \( k \) bundles; the only thing to check is that the \( i \)-th bundle spans the **whole** of \( E_i \), not just part of it, and that is a coordinate comparison. After that, (a) is the orthonormality of the basis, (c) and (d) are the coordinate formula \( \v = \sum_j\inner{\v}{\e_j}\e_j \) with its terms grouped, and (b) and (e) are bookkeeping.
:::

::: {.proof}
Let \( \sB = (\e_1, \dots, \e_n) \) be an orthonormal basis of \( V \) with \( T\e_j = \mu_j\e_j \), which exists by \( (\ast) \). Each \( \e_j \) is non-zero, so each \( \mu_j \) is an eigenvalue of \( T \) and therefore equals exactly one \( \lambda_i \). Put
\[
\sS_i \coloneqq \{\, j : \mu_j = \lambda_i \,\} ,
\]
so that \( \{1, \dots, n\} \) is the disjoint union of \( \sS_1, \dots, \sS_k \).

**Step 1.** *\( E_i = \Span(\e_j : j \in \sS_i) \).* The inclusion \( (\supseteq) \) is immediate, since \( T\e_j = \lambda_i\e_j \) for \( j \in \sS_i \). For \( (\subseteq) \), let \( \v \in E_i \) and write \( \v = \sum_{j}c_j\e_j \) in the basis \( \sB \). Applying \( T \),
\[
\sum_j c_j\mu_j\e_j = T\v = \lambda_i\v = \sum_j c_j\lambda_i\e_j .
\]
Coordinates in a basis are unique, so \( c_j(\mu_j - \lambda_i) = 0 \) for every \( j \), and hence \( c_j = 0 \) unless \( j \in \sS_i \). In particular \( \sS_i \ne \varnothing \), because \( E_i \ne \{\0\} \).

**Step 2 (a).** By Step 1, \( V = \Span(\sB) = E_1 + \dots + E_k \). If \( i \ne j \), then \( \sS_i \) and \( \sS_j \) are disjoint and \( \sB \) is orthonormal, so every spanning vector of \( E_i \) is orthogonal to every spanning vector of \( E_j \); hence \( E_i \perp E_j \). Pairwise orthogonal subspaces are independent: if \( \u_1 + \dots + \u_k = \0 \) with \( \u_i \in E_i \), then pairing with \( \u_l \) kills every term but one and leaves \( \norm{\u_l}^2 = 0 \), so \( \u_l = \0 \). By @thm-direct-sum-criteria the sum is direct.

**Step 3 (b).** Each \( P_i \) is self-adjoint by @thm-projection-formula (b), and satisfies \( P_i^2 = P_i \) with \( \im P_i = E_i \) and \( \ker P_i = E_i^{\perp} \) (@def-orthogonal-projection and the discussion following it). For \( i \ne j \), Step 2 gives \( E_j \subseteq E_i^{\perp} \), so \( \im P_j \subseteq \ker P_i \) and \( P_iP_j = 0 \).

**Step 4 (c) and (d).** By Step 1, \( (\e_j : j \in \sS_i) \) is an orthonormal basis of \( E_i \), so @thm-projection-formula (a) gives
\[
P_i\v = \sum_{j \in \sS_i}\inner{\v}{\e_j}\e_j \qquad (\v \in V).
\]
Summing over \( i \) collects every index \( j \) exactly once, so by @thm-orthonormal-coordinates,
\[
\sum_{i=1}^{k}P_i\v = \sum_{j=1}^{n}\inner{\v}{\e_j}\e_j = \v ,
\]
which is (c). Multiplying the \( i \)-th group by \( \lambda_i \) instead,
\[
\begin{aligned}
\sum_{i=1}^{k}\lambda_iP_i\v
  &= \sum_{i=1}^{k}\sum_{j \in \sS_i}\inner{\v}{\e_j}\,\lambda_i\e_j \\
  &= \sum_{j=1}^{n}\inner{\v}{\e_j}\,\mu_j\e_j
   = T\Bigl(\sum_{j=1}^{n}\inner{\v}{\e_j}\e_j\Bigr) = T\v ,
\end{aligned}
\]
where the second equality uses \( \mu_j = \lambda_i \) for \( j \in \sS_i \), and the third the linearity of \( T \) together with \( T\e_j = \mu_j\e_j \). This is (d).

**Step 5 (e).** For \( \v \in V \) we have \( P_i\v \in E_i \), so \( T(P_i\v) = \lambda_iP_i\v \); thus \( TP_i = \lambda_iP_i \). In the other order, (d) and (b) give
\[
P_iT = P_i\Bigl(\sum_{j=1}^{k}\lambda_jP_j\Bigr) = \lambda_iP_i^2 = \lambda_iP_i .
\]
This proves the theorem.
:::

For matrices the picture is the familiar one, packaged differently. If \( \A \in M_n(\nC) \) is normal, write \( \A = \U\D\U^{*} \) with \( \U \) unitary and \( \D \) diagonal (@cor-spectral-complex-matrix). Grouping the columns \( \q_1, \dots, \q_n \) of \( \U \) by their eigenvalue turns this into
\[
\A = \sum_{i=1}^{k}\lambda_i\P_i, \qquad \P_i = \sum_{j \in \sS_i}\q_j\q_j^{*},
\]
so each \( \P_i \) is a sum of rank-one projections and \( \rank\P_i = \dim E_i \).

::: {#exm-spectral-resolution-3x3}
[A Symmetric \( 3 \times 3 \) Matrix]

Let \( \A = \begin{pmatrix} 1 & 2 & 2 \\ 2 & 1 & 2 \\ 2 & 2 & 1 \end{pmatrix} \in M_3(\nR) \). Find the spectral resolution of \( \A \).
:::

::: {.solution}
Write \( \A = 2\J - \I \), where \( \J \) is the all-ones matrix. Since \( \J\x = (x_1 + x_2 + x_3)\1 \), we get \( \J\1 = 3\1 \) and \( \J\x = \0 \) exactly when \( x_1 + x_2 + x_3 = 0 \). So \( \J \) has eigenvalues \( 3 \) and \( 0 \), and \( \A \) has eigenvalues
\[
\lambda_1 = 2 \cdot 3 - 1 = 5, \qquad \lambda_2 = 2 \cdot 0 - 1 = -1,
\]
with \( E_5 = \Span(\1) \) of dimension \( 1 \) and \( E_{-1} = \1^{\perp} \) of dimension \( 2 \). Since \( \norm{\1}^2 = 3 \), the orthogonal projection onto \( E_5 \) is \( \P_1 = \tfrac13\1\1\tp = \tfrac13\J \), and \( \P_2 = \I - \P_1 \) by @thm-spectral-resolution (c). Concretely,
\[
\P_1 = \frac13\begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1\end{pmatrix},
\qquad
\P_2 = \frac13\begin{pmatrix} 2 & -1 & -1 \\ -1 & 2 & -1 \\ -1 & -1 & 2\end{pmatrix}.
\]
*Check.* Both are symmetric, both satisfy \( \P_i^2 = \P_i \), their product is \( 0 \), they sum to \( \I \), and
\[
5\P_1 - \P_2 = \tfrac53\J - \I + \tfrac13\J = 2\J - \I = \A .
\]
Note that the resolution has two terms, not three: \( k = 2 \) counts **distinct** eigenvalues, while \( \rank\P_2 = 2 \) records the multiplicity of \( -1 \).
:::

## Orthogonal projections versus oblique ones

An expression \( T = \sum\lambda_i\pi_i \) with idempotents summing to the identity is not by itself news. In the proof of @thm-jordan-chevalley the semisimple part of \( T \) is written as \( \sum_i\lambda_i\pi_i \), where \( \pi_i = h_i(T) \) projects onto the generalized eigenspace \( G_{\lambda_i}(T) \) along the sum of the others (@thm-primary-decomposition (d)); when \( T \) is diagonalizable, that is a decomposition of \( T \) itself, and those \( \pi_i \) satisfy \( \pi_i^2 = \pi_i \), \( \pi_i\pi_j = 0 \) for \( i \ne j \) and \( \sum_i\pi_i = \id_V \), exactly as in @thm-spectral-resolution (b) and (c). What they do **not** satisfy is \( \pi_i^{*} = \pi_i \), and that single missing condition is the whole difference between Chapter 10 and this section.

::: {#exm-oblique-projections}
[Two Projections That Are Not Orthogonal]

Let \( \A = \begin{pmatrix} 1 & 1 \\ 0 & 2\end{pmatrix} \in M_2(\nR) \), which is diagonalizable with eigenvalues \( 1 \) and \( 2 \). Compute the projections \( \vpi_1, \vpi_2 \) of @thm-primary-decomposition for \( \A \), verify that \( \A = \vpi_1 + 2\vpi_2 \), and decide whether they are orthogonal projections.
:::

::: {.solution}
The eigenspaces are \( E_1 = \Span(\e_1) \) and \( E_2 = \Span\bigl((1,1)\bigr) \), read off from \( \A - \I = \begin{pmatrix} 0 & 1 \\ 0 & 1\end{pmatrix} \) and \( \A - 2\I = \begin{pmatrix} -1 & 1 \\ 0 & 0\end{pmatrix} \). Since the eigenvalues are distinct, the generalized eigenspaces are the eigenspaces. With \( \P = \begin{pmatrix} 1 & 1 \\ 0 & 1\end{pmatrix} \) we have \( \P^{-1}\A\P = \diag(1, 2) \), so
\[
\vpi_1 = \P\begin{pmatrix} 1 & 0 \\ 0 & 0\end{pmatrix}\P^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 0\end{pmatrix},
\qquad
\vpi_2 = \I - \vpi_1 = \begin{pmatrix} 0 & 1 \\ 0 & 1\end{pmatrix}.
\]
Both square to themselves, their products vanish in both orders, they sum to \( \I \), and
\[
1 \cdot \vpi_1 + 2 \cdot \vpi_2 = \begin{pmatrix} 1 & -1 \\ 0 & 0\end{pmatrix} + \begin{pmatrix} 0 & 2 \\ 0 & 2\end{pmatrix} = \A .
\]
They are **not** orthogonal projections: \( \vpi_1\tp = \begin{pmatrix} 1 & 0 \\ -1 & 0\end{pmatrix} \ne \vpi_1 \). Geometrically, \( \vpi_1 \) projects onto \( \Span(\e_1) \) **along** \( \Span((1,1)) \), and those two lines meet at \( 45^{\circ} \), not at a right angle. Consistently, \( \A \) is not normal:
\[
\A\tp\A = \begin{pmatrix} 1 & 1 \\ 1 & 5\end{pmatrix}
\ne \begin{pmatrix} 2 & 2 \\ 2 & 4\end{pmatrix} = \A\A\tp .
\]
:::

::: {.warning}
**"Diagonalizable" gives projections; only "normal" makes them orthogonal.** Every diagonalizable operator splits as \( \sum\lambda_i\pi_i \) with idempotents that annihilate each other and sum to the identity, and @exm-oblique-projections is such a splitting for a matrix that is not normal. The projections there are not self-adjoint, so they are not the projections of @def-spectral-resolution, and the eigenspaces they project onto are not perpendicular. Whenever an argument needs \( \inner{P_i\u}{\v} = \inner{\u}{P_i\v} \) — and most of this section does — normality is what pays for it.
:::

## What makes a resolution the resolution

The projections in @def-spectral-resolution were built from the eigenspaces, so they are visibly determined by \( T \). It is much more useful to know the converse: that *any* decomposition with the right formal properties has to be that one. This is what lets us recognize a spectral resolution when it turns up by accident, and it is the engine of the uniqueness proof for square roots below.

:::: {#thm-spectral-resolution-unique}
[Uniqueness of the Spectral Resolution]

Let \( V \) be a non-zero finite-dimensional inner product space over \( F \) and let \( T \in \cL(V) \). Suppose
\[
T = \mu_1Q_1 + \mu_2Q_2 + \dots + \mu_mQ_m ,
\]
where \( \mu_1, \dots, \mu_m \in F \) are **distinct** and \( Q_1, \dots, Q_m \in \cL(V) \) are **non-zero** operators satisfying

::: {.enumerate options="label=(R\arabic*)"}
1. \( Q_i^{*} = Q_i \) and \( Q_i^2 = Q_i \) for every \( i \);
2. \( Q_iQ_j = 0 \) whenever \( i \ne j \);
3. \( Q_1 + \dots + Q_m = \id_V \).
:::

Then \( T \) satisfies \( (\ast) \), \( \spec(T) = \{\mu_1, \dots, \mu_m\} \), and \( Q_i \) is the orthogonal projection onto \( E_{\mu_i}(T) \) for every \( i \). In particular \( m \) is the number of distinct eigenvalues of \( T \), and the given decomposition is the spectral resolution of \( T \).
::::

::: {.idea}
Three moves. ① A self-adjoint idempotent is the orthogonal projection onto its own image: self-adjointness is used here and nowhere else, which is exactly why @exm-oblique-projections escapes the theorem. ② Conditions (R2) and (R3) then break \( V \) into the orthogonal direct sum of the images \( U_i = \im Q_i \). ③ On \( U_i \) the operator \( T \) is multiplication by \( \mu_i \), so \( U_i \subseteq E_{\mu_i}(T) \); and because the \( \mu_i \) are distinct, an eigenvector of \( T \) cannot spread across two pieces, which upgrades the inclusion to an equality.
:::

::: {.proof}
Write \( U_i = \im Q_i \), which is non-zero because \( Q_i \ne 0 \).

**Step 1.** *\( Q_i = P_{U_i} \).* Fix \( i \) and drop the subscript. If \( \u \in U \), say \( \u = Q\x \), then \( Q\u = Q^2\x = Q\x = \u \), so \( Q \) is the identity on \( U \). Next, \( \ker Q = U^{\perp} \). Indeed, if \( Q\w = \0 \), then for every \( \x \),
\[
\inner{\w}{Q\x} = \inner{Q\w}{\x} = 0
\]
by @def-adjoint and (R1), so \( \w \in U^{\perp} \); conversely if \( \w \in U^{\perp} \), then \( Q\w \in U \) and
\[
\norm{Q\w}^2 = \inner{Q\w}{Q\w} = \inner{\w}{Q^2\w} = \inner{\w}{Q\w} = 0 ,
\]
using (R1) twice and then \( Q\w \in U \perp \w \); so \( Q\w = \0 \). Finally, for any \( \v \in V \),
\[
\v = Q\v + (\v - Q\v), \qquad Q\v \in U, \quad Q(\v - Q\v) = Q\v - Q^2\v = \0 ,
\]
so \( \v - Q\v \in \ker Q = U^{\perp} \). This is the splitting of \( \v \) in \( U \oplus U^{\perp} \) (@thm-orthogonal-decomposition), so \( Q\v = P_U\v \) by @def-orthogonal-projection.

**Step 2.** *\( V = U_1 \oplus \dots \oplus U_m \), orthogonally.* By (R3), every \( \v \) equals \( \sum_iQ_i\v \in \sum_iU_i \). For \( i \ne j \), \( \u = Q_i\x \) and \( \w = Q_j\y \) satisfy
\[
\inner{\u}{\w} = \inner{Q_i\x}{Q_j\y} = \inner{Q_jQ_i\x}{\y} = 0
\]
by (R1) and (R2), so \( U_i \perp U_j \). As in Step 2 of the proof of @thm-spectral-resolution, pairwise orthogonal subspaces are independent, so the sum is direct.

**Step 3.** *\( T \) acts on \( U_i \) as multiplication by \( \mu_i \).* Let \( \u \in U_i \). By Step 1, \( Q_i\u = \u \), and for \( j \ne i \), \( Q_j\u = Q_jQ_i\u = \0 \) by (R2). Hence
\[
T\u = \sum_{l=1}^{m}\mu_lQ_l\u = \mu_i\u .
\]
Since \( U_i \ne \{\0\} \), this makes \( \mu_i \) an eigenvalue of \( T \), with \( U_i \subseteq E_{\mu_i}(T) \).

**Step 4.** *\( \spec(T) = \{\mu_1, \dots, \mu_m\} \) and \( U_i = E_{\mu_i}(T) \).* Let \( \lambda \) be an eigenvalue of \( T \) with eigenvector \( \v \ne \0 \). By (R3), \( \v = \sum_iQ_i\v \) with \( Q_i\v \in U_i \), and by Step 3,
\[
\sum_{i=1}^{m}\mu_iQ_i\v = T\v = \lambda\v = \sum_{i=1}^{m}\lambda Q_i\v .
\]
Subtracting, \( \sum_i(\mu_i - \lambda)Q_i\v = \0 \) with the \( i \)-th term in \( U_i \), so by the directness of Step 2 every term vanishes: \( Q_i\v = \0 \) whenever \( \mu_i \ne \lambda \). As \( \v \ne \0 \), some \( Q_i\v \ne \0 \), and for that \( i \) we get \( \lambda = \mu_i \). The \( \mu_l \) being distinct, \( i \) is the only index with \( \mu_i = \lambda \), so \( \v = Q_i\v \in U_i \). Therefore \( \spec(T) \subseteq \{\mu_1, \dots, \mu_m\} \) and \( E_{\mu_i}(T) \subseteq U_i \); with Step 3 both are equalities.

**Step 5.** By Steps 1 and 4, \( Q_i = P_{U_i} = P_{E_{\mu_i}(T)} \). Choosing an orthonormal basis of each \( U_i \) (@thm-gram-schmidt) and concatenating gives an orthonormal basis of \( V \) by Step 2, made of eigenvectors of \( T \) by Step 3; so \( T \) satisfies \( (\ast) \). This proves the theorem.
:::

Read the other way round, the theorem is the complex spectral theorem again with no basis in sight: over \( \nC \), an operator is normal **if and only if** it can be written as \( \sum\mu_iQ_i \) with distinct \( \mu_i \) and non-zero self-adjoint idempotents satisfying (R2) and (R3) (@thm-spectral-complex). Conditions (R1)–(R3) are the entire content of the theorem, compressed into three lines of algebra.

::: {.check}
The matrices \( \vpi_1, \vpi_2 \) of @exm-oblique-projections satisfy \( \vpi_i^2 = \vpi_i \), \( \vpi_1\vpi_2 = \vpi_2\vpi_1 = 0 \) and \( \vpi_1 + \vpi_2 = \I \), and the coefficients \( 1 \) and \( 2 \) are distinct. Which hypothesis of @thm-spectral-resolution-unique fails, and what does its failure cost?
:::

::: {.solution}
Self-adjointness in (R1): \( \vpi_1\tp \ne \vpi_1 \). Everything else holds. The cost is Step 1 of the proof: \( \vpi_1 \) is a projection onto \( \Span(\e_1) \), but along \( \Span((1,1)) \) rather than along \( \Span(\e_1)^{\perp} = \Span(\e_2) \), so it is not \( P_{\Span(\e_1)} \). Consequently the two images are not perpendicular, and the conclusion fails at its strongest point: \( \begin{pmatrix} 1 & 1 \\ 0 & 2\end{pmatrix} \) does not satisfy \( (\ast) \), since it is not normal.
:::

## Functions of an operator

Powers are now trivial. Multiplying the resolution by itself and using \( P_iP_j = 0 \) for \( i \ne j \) leaves only the diagonal terms:
\[
T^2 = \Bigl(\sum_i\lambda_iP_i\Bigr)\Bigl(\sum_j\lambda_jP_j\Bigr) = \sum_i\lambda_i^2P_i ,
\]
and the same computation repeated gives \( T^m = \sum_i\lambda_i^mP_i \). So \( p(T) = \sum_ip(\lambda_i)P_i \) for every polynomial \( p \). Stare at that formula and notice what it does **not** use: nothing about \( p \) except its \( k \) values on the spectrum. Any function at all supplies those.

::: {#def-function-of-normal-operator}
[Function of an Operator]

Let \( T \in \cL(V) \) satisfy \( (\ast) \), with distinct eigenvalues \( \lambda_1, \dots, \lambda_k \) and spectral resolution \( T = \sum_i\lambda_iP_i \). For **any** function \( f \colon \spec(T) \to F \), define
\[
f(T) \coloneqq \sum_{i=1}^{k}f(\lambda_i)\,P_i \ \in \cL(V) .
\]
:::

In words: apply \( f \) to each eigenvalue and reweight the same projections. The function needs no continuity, no differentiability and no formula — it is \( k \) numbers. And the definition is unambiguous: the \( \lambda_i \) and the \( P_i \) are determined by \( T \) alone, by @thm-spectral-resolution-unique, so no choice of basis or of eigenvectors enters.

Four instances show the range. Taking \( f(\lambda) = \lambda \) returns \( T \). Taking \( f \equiv 1 \) returns \( \id_V \), by @thm-spectral-resolution (c). Taking \( f(\lambda) = \conj{\lambda} \) returns \( T^{*} \), since \( P_i^{*} = P_i \). And if \( 0 \notin \spec(T) \), taking \( f(\lambda) = \lambda^{-1} \) returns \( T^{-1} \), because
\[
\Bigl(\sum_i\lambda_iP_i\Bigr)\Bigl(\sum_j\lambda_j^{-1}P_j\Bigr) = \sum_iP_i = \id_V .
\]

The notation is, on its face, dangerous. For a polynomial \( p \) the symbol \( p(T) \) already means something — the operator \( a_0\id_V + a_1T + \dots + a_NT^N \) of @def-polynomial-of-operator, which Chapter 6 studied at length. If @def-function-of-normal-operator disagreed with it, the whole notation would have to be abandoned. Part (a) below says it does not, and that is the reason the rest of the theorem is safe to use.

:::: {#thm-functional-calculus-properties}
[Properties of the Functional Calculus]

Let \( T \in \cL(V) \) satisfy \( (\ast) \), with distinct eigenvalues \( \lambda_1, \dots, \lambda_k \) and resolution of the identity \( (P_1, \dots, P_k) \). Let \( f, g \colon \spec(T) \to F \) and \( c \in F \), with \( f + g \), \( cf \) and \( fg \) taken pointwise.

::: {.enumerate options="label=(\alph*)"}
1. **(Compatibility)** For every \( p \in F[x] \), the operator \( p(T) \) of @def-polynomial-of-operator equals \( \sum_ip(\lambda_i)P_i \); that is, it agrees with @def-function-of-normal-operator applied to the restriction of \( p \) to \( \spec(T) \).
2. **(Algebra homomorphism)** \( (f + g)(T) = f(T) + g(T) \), \( (cf)(T) = c\,f(T) \), \( (fg)(T) = f(T)g(T) = g(T)f(T) \), and \( 1(T) = \id_V \).
3. **(Adjoints)** \( f(T)^{*} = \conj{f}(T) \), where \( \conj{f}(\lambda) = \conj{f(\lambda)} \). In particular \( f(T) \) is self-adjoint when \( f \) is real-valued, and unitary when \( \lvert f(\lambda_i) \rvert = 1 \) for every \( i \).
4. **(Spectral mapping)** \( f(T) \) satisfies \( (\ast) \), with the same orthonormal eigenbasis as \( T \), and \( \spec(f(T)) = f(\spec(T)) \).
5. **(Commutation)** If \( S \in \cL(V) \) commutes with \( T \), then \( S \) commutes with every \( P_i \) and hence with \( f(T) \). In particular \( T \) and \( f(T) \) commute.
:::
::::

::: {.idea}
Everything rests on one multiplication table, \( P_iP_j = \delta_{ij}P_i \). It says that the operators \( \sum_ic_iP_i \) multiply exactly the way the coefficient lists \( (c_1, \dots, c_k) \) multiply coordinatewise, so \( \cL(V) \) contains a copy of the algebra of all \( F \)-valued functions on \( \spec(T) \), and \( f \mapsto f(T) \) is the obvious map into it. That makes (b) and (c) one-line computations. The one statement needing an argument is (a) — that the copy sitting inside is the *same* copy Chapter 2 built by substituting \( T \) into polynomials — and the argument is to compute the powers of \( T \). For (e), a commuting \( S \) preserves each eigenspace, and an operator preserving all the summands of an orthogonal direct sum commutes with the projections onto them.
:::

::: {.proof}
(a) We first show that
\[
T^{m} = \sum_{i=1}^{k}\lambda_i^{m}P_i \qquad \text{for every integer } m \ge 0 ,
\]
with the usual convention \( \lambda^0 = 1 \). For \( m = 0 \) both sides equal \( \id_V \), by @thm-spectral-resolution (c). Assuming the formula for \( m \), @thm-spectral-resolution (d) and (b) give
\[
\begin{aligned}
T^{m+1} = T \cdot T^{m}
  &= \Bigl(\sum_{i}\lambda_iP_i\Bigr)\Bigl(\sum_{j}\lambda_j^{m}P_j\Bigr) \\
  &= \sum_{i,j}\lambda_i\lambda_j^{m}\,P_iP_j
   = \sum_{i}\lambda_i^{m+1}P_i ,
\end{aligned}
\]
since \( P_iP_j = 0 \) for \( i \ne j \) and \( P_i^2 = P_i \). Now let \( p = a_0 + a_1x + \dots + a_Nx^{N} \). By @def-polynomial-of-operator and the formula just proved,
\[
\begin{aligned}
p(T) = \sum_{m=0}^{N}a_mT^{m}
  &= \sum_{m=0}^{N}a_m\sum_{i=1}^{k}\lambda_i^{m}P_i \\
  &= \sum_{i=1}^{k}\Bigl(\sum_{m=0}^{N}a_m\lambda_i^{m}\Bigr)P_i
   = \sum_{i=1}^{k}p(\lambda_i)P_i ,
\end{aligned}
\]
the middle step being a rearrangement of a finite double sum.

(b) The first two identities are immediate from @def-function-of-normal-operator. For the product, @thm-spectral-resolution (b) gives
\[
f(T)g(T) = \sum_{i,j}f(\lambda_i)g(\lambda_j)P_iP_j = \sum_{i}f(\lambda_i)g(\lambda_i)P_i ,
\]
which is \( (fg)(T) \). The right-hand side is symmetric in \( f \) and \( g \), so \( f(T)g(T) = g(T)f(T) \). Finally \( 1(T) = \sum_iP_i = \id_V \) by @thm-spectral-resolution (c).

(c) By @thm-adjoint-properties (a) and (b), and \( P_i^{*} = P_i \),
\[
f(T)^{*} = \sum_{i=1}^{k}\conj{f(\lambda_i)}\,P_i^{*} = \conj{f}(T) .
\]
If \( f \) is real-valued then \( \conj{f} = f \) and \( f(T)^{*} = f(T) \). If \( \lvert f(\lambda_i) \rvert = 1 \) for all \( i \), then \( \conj{f}f \equiv 1 \), so by (b) \( f(T)^{*}f(T) = (\conj{f}f)(T) = \id_V \), and likewise \( f(T)f(T)^{*} = \id_V \); so \( f(T) \) is unitary (@def-unitary-orthogonal).

(d) Let \( \sB = (\e_1, \dots, \e_n) \) be an orthonormal eigenbasis of \( T \), with \( T\e_j = \mu_j\e_j \), and fix \( j \). Let \( i \) be the index with \( \mu_j = \lambda_i \). Then \( \e_j \in E_i \), so \( P_i\e_j = \e_j \), while \( P_l\e_j = \0 \) for \( l \ne i \) because \( E_i \subseteq E_l^{\perp} = \ker P_l \), by @thm-spectral-resolution (a) and @def-orthogonal-projection. Hence
\[
f(T)\e_j = f(\lambda_i)\e_j = f(\mu_j)\,\e_j .
\]
So \( \sB \) is an orthonormal basis of eigenvectors of \( f(T) \), which is \( (\ast) \) for \( f(T) \). The matrix of \( f(T) \) in \( \sB \) is \( \diag(f(\mu_1), \dots, f(\mu_n)) \), so its eigenvalues are exactly the numbers \( f(\mu_j) \), that is the numbers \( f(\lambda_i) \); hence \( \spec(f(T)) = f(\spec(T)) \).

(e) Suppose \( ST = TS \). Each \( E_i \) is \( S \)-invariant: if \( T\v = \lambda_i\v \), then \( T(S\v) = S(T\v) = \lambda_iS\v \). Let \( \v \in V \) and write \( \v = \sum_iP_i\v \) with \( P_i\v \in E_i \) (@thm-spectral-resolution (c)). Applying \( S \) gives \( S\v = \sum_iSP_i\v \) with \( SP_i\v \in E_i \), and this is the decomposition of \( S\v \) in \( E_1 \oplus \dots \oplus E_k \), which is unique. Comparing it with \( S\v = \sum_iP_i(S\v) \) gives \( P_iS\v = SP_i\v \) for every \( i \), that is \( SP_i = P_iS \). Hence \( S \) commutes with \( f(T) = \sum_if(\lambda_i)P_i \). Since \( T \) commutes with itself, the last claim follows. This proves the theorem.
:::

Part (a) is what makes the notation honest. Writing \( \sqrt{T} \), \( e^{T} \) and \( p(T) \) in the same paragraph is legitimate precisely because the polynomial case is common ground: the new definition extends the old one instead of competing with it. It also reconciles this section with Chapter 10. An operator satisfying \( (\ast) \) is diagonalizable, so every Jordan block of its matrix has size \( 1 \), and @def-matrix-function-jordan consults no derivatives at all — it too returns \( \sum_if(\lambda_i)\P_i \). The two constructions of \( f(\A) \) agree for normal \( \A \), and Chapter 10's extra machinery is precisely the price of dropping normality.

::: {.warning}
**Outside the normal case, \( f \) on the spectrum is not enough data.** For \( \A = \begin{pmatrix} 0 & 1 \\ 0 & 0\end{pmatrix} \) the only eigenvalue is \( 0 \), so the recipe "\( f(\A) = \sum_if(\lambda_i)\P_i \)" would read \( f(\A) = f(0)\I \) for every \( f \) — and with \( f(x) = x \) it would announce \( \A = 0 \). The recipe is not wrong, it is inapplicable: \( \A \) is not normal, so there is no resolution of the identity to expand in. Chapter 10's definition of \( f(\A) \) has to consult \( f'(0) \) as well (@def-matrix-function-jordan), and that derivative is exactly what the missing orthogonality would have spared us.
:::

::: {.check}
Let \( T \in \cL(V) \) satisfy \( (\ast) \) with \( \spec(T) = \{0, 1\} \). Identify \( T \).
:::

::: {.solution}
\( T \) is the orthogonal projection onto \( E_1(T) \). Indeed the spectral resolution reads \( T = 0 \cdot P_1 + 1 \cdot P_2 = P_2 = P_{E_1(T)} \). So the operators satisfying \( (\ast) \) with spectrum in \( \{0, 1\} \) are exactly the orthogonal projections, together with \( 0 \) and \( \id_V \) for the degenerate spectra \( \{0\} \) and \( \{1\} \).
:::

## Square roots

The function \( \lambda \mapsto \sqrt{\lambda} \) is defined on \( [0, \infty) \), so @def-function-of-normal-operator produces a square root of \( T \) as soon as the spectrum lies there. The interesting part is that the square root is **unique** once we ask it to be of the same kind, and the uniqueness proof is a direct application of @thm-spectral-resolution-unique: a square root's own resolution, squared, has to be \( T \)'s.

Note first that over \( \nC \) the hypothesis is stronger than it looks. If \( T \) satisfies \( (\ast) \) and \( \spec(T) \subseteq \nR \), then \( f(\lambda) = \lambda \) is real-valued on the spectrum, so \( T = f(T) \) is self-adjoint by @thm-functional-calculus-properties (c). A normal operator with real spectrum is self-adjoint.

:::: {#thm-normal-square-root}
[The Square Root of a Non-negative Normal Operator]

Let \( V \) be a non-zero finite-dimensional inner product space over \( F \) and let \( T \in \cL(V) \) satisfy \( (\ast) \) with \( \spec(T) \subseteq [0, \infty) \). Then there is **exactly one** operator \( S \in \cL(V) \) such that

::: {.enumerate options="label=(\roman*)"}
1. \( S \) satisfies \( (\ast) \);
2. \( \spec(S) \subseteq [0, \infty) \);
3. \( S^2 = T \).
:::

It is \( S = \sum_i\sqrt{\lambda_i}\,P_i \), where \( T = \sum_i\lambda_iP_i \) is the spectral resolution of \( T \). This \( S \) is self-adjoint, and it commutes with every operator that commutes with \( T \).
::::

::: {.idea}
Existence is the functional calculus applied to \( \sqrt{\ }\, \): squaring a function squares its values. Uniqueness is where the work is, and the trick is not to compare \( S \) with the candidate directly but to *square \( S \)'s own resolution*. If \( S = \sum_j\mu_jQ_j \), then \( S^2 = \sum_j\mu_j^2Q_j \), and the \( \mu_j^2 \) are still distinct because the \( \mu_j \) are distinct **and non-negative**. So \( \sum_j\mu_j^2Q_j \) meets every condition of @thm-spectral-resolution-unique for \( T \), which forces it to be \( T \)'s spectral resolution term by term.
:::

::: {.proof}
*Existence.* Let \( f(\lambda) = \sqrt{\lambda} \) on \( \spec(T) \subseteq [0, \infty) \), which takes values in \( [0, \infty) \subseteq F \), and put \( S = f(T) = \sum_i\sqrt{\lambda_i}P_i \). Then \( f^2 \) is the function \( \lambda \mapsto \lambda \), so by @thm-functional-calculus-properties (b) and (a),
\[
S^2 = f(T)f(T) = (f^2)(T) = T ,
\]
giving (iii). By @thm-functional-calculus-properties (d), \( S \) satisfies \( (\ast) \) and \( \spec(S) = \{\sqrt{\lambda_1}, \dots, \sqrt{\lambda_k}\} \subseteq [0, \infty) \), giving (i) and (ii). Since \( f \) is real-valued, \( S \) is self-adjoint by @thm-functional-calculus-properties (c), and it commutes with everything commuting with \( T \) by (e) of the same theorem.

*Uniqueness.* Let \( S \) satisfy (i), (ii) and (iii), and let
\[
S = \mu_1Q_1 + \dots + \mu_lQ_l
\]
be its spectral resolution (@thm-spectral-resolution): the \( \mu_j \) are the distinct eigenvalues of \( S \), and the \( Q_j \) are non-zero self-adjoint idempotents with \( Q_jQ_{j'} = 0 \) for \( j \ne j' \) and \( \sum_jQ_j = \id_V \). By @thm-functional-calculus-properties (a) applied to \( S \) and \( p = x^2 \),
\[
T = S^2 = \sum_{j=1}^{l}\mu_j^2\,Q_j .
\]
The scalars \( \mu_j^2 \) are **distinct**: the \( \mu_j \) are distinct by construction, and non-negative by (ii), so \( \mu_j^2 = \mu_{j'}^2 \) would force \( \mu_j = \mu_{j'} \). The family \( (Q_1, \dots, Q_l) \) satisfies (R1), (R2) and (R3) of @thm-spectral-resolution-unique, and every \( Q_j \) is non-zero. That theorem therefore identifies the displayed expression as the spectral resolution of \( T \): after renumbering, \( l = k \), \( \mu_j^2 = \lambda_j \) and \( Q_j = P_j \) for every \( j \). Since \( \mu_j \ge 0 \) and \( \mu_j^2 = \lambda_j \), we get \( \mu_j = \sqrt{\lambda_j} \), and hence
\[
S = \sum_{j=1}^{k}\sqrt{\lambda_j}\,P_j ,
\]
which is the operator constructed above. This proves the theorem.
:::

The square root is written \( \sqrt{T} \), or \( T^{1/2} \). Chapter 13 takes the hypothesis \( \spec(T) \subseteq [0, \infty) \) as the definition of a **positive** operator, proves that it is equivalent to \( \inner{T\v}{\v} \ge 0 \) for all \( \v \), and makes this theorem the tool behind polar decomposition and the singular value decomposition; the notation \( \A^{1/2} \) in the notation table refers to exactly the operator built here.

::: {#exm-normal-square-root-2x2}
[A Square Root, and Three Impostors]

Let \( \A = \begin{pmatrix} 10 & 6 \\ 6 & 10 \end{pmatrix} \in M_2(\nR) \). Find its spectral resolution, compute \( \sqrt{\A} \) and \( \A^{m} \), and find a symmetric square root of \( \A \) other than \( \sqrt{\A} \).
:::

::: {.solution}
*The resolution.* \( \A \) is symmetric, hence self-adjoint on \( \nR^2 \). Since \( \A(1,1) = (16,16) \) and \( \A(1,-1) = (4,-4) \), the eigenvalues are \( 16 \) and \( 4 \), with eigenlines \( \Span((1,1)) \) and \( \Span((1,-1)) \). Both spanning vectors have squared length \( 2 \), so
\[
\P_1 = \frac12\begin{pmatrix} 1 & 1 \\ 1 & 1\end{pmatrix},
\qquad
\P_2 = \frac12\begin{pmatrix} 1 & -1 \\ -1 & 1\end{pmatrix},
\qquad
\A = 16\P_1 + 4\P_2 .
\]

*The square root.* Both eigenvalues are positive, so @thm-normal-square-root applies:
\[
\sqrt{\A} = 4\P_1 + 2\P_2 = \begin{pmatrix} 2 & 2 \\ 2 & 2\end{pmatrix} + \begin{pmatrix} 1 & -1 \\ -1 & 1\end{pmatrix} = \begin{pmatrix} 3 & 1 \\ 1 & 3\end{pmatrix},
\]
and indeed \( \begin{pmatrix} 3 & 1 \\ 1 & 3\end{pmatrix}^2 = \begin{pmatrix} 10 & 6 \\ 6 & 10\end{pmatrix} \).

*Powers.* By @thm-functional-calculus-properties (a), \( \A^{m} = 16^{m}\P_1 + 4^{m}\P_2 \), that is
\[
\A^{m} = \frac12\begin{pmatrix} 16^{m} + 4^{m} & 16^{m} - 4^{m} \\ 16^{m} - 4^{m} & 16^{m} + 4^{m}\end{pmatrix} .
\]
For \( m = 3 \) this reads \( \begin{pmatrix} 2080 & 2016 \\ 2016 & 2080\end{pmatrix} \), which is \( \A^3 \).

*An impostor.* Changing one sign gives \( \B = 4\P_1 - 2\P_2 = \begin{pmatrix} 1 & 3 \\ 3 & 1\end{pmatrix} \), and \( \B^2 = \A \) as well. So \( \A \) has more than one symmetric square root; \( \B \) fails clause (ii) of @thm-normal-square-root, since \( \spec(\B) = \{4, -2\} \). Flipping the other sign, and both, gives \( -\B \) and \( -\sqrt{\A} \): four symmetric square roots, and exactly one of them has non-negative spectrum.
:::

::: {.warning}
**"A square root" and "the square root" are different things.** Uniqueness in @thm-normal-square-root needs all three clauses. Dropping (ii) admits the three sign-flipped roots of @exm-normal-square-root-2x2. Dropping (i) admits more still, and the cheapest witness is the zero operator on \( \nC^2 \). Take
\[
\S = \begin{pmatrix} 0 & 1 \\ 0 & 0\end{pmatrix}, \qquad \S^2 = \0 .
\]
Here \( \spec(\S) = \{0\} \subseteq [0, \infty) \), so (ii) holds, and (iii) holds by the display, yet \( \S \ne \0 = \sqrt{\0} \). Only (i) fails: \( \S^{*}\S = \diag(0, 1) \) while \( \S\S^{*} = \diag(1, 0) \). The phrase "**the** square root of \( T \)" always means the one satisfying all three.
:::

## The exponential and the unitary group

Chapter 10 defined \( e^{\A} \) for every \( \A \in M_n(\nC) \) as the sum of the series \( \sum_m\A^{m}/m! \) (@def-matrix-exponential) and proved that the series converges (@thm-exponential-series-converges). We do not redevelop any of that. What the spectral resolution adds is that for a normal matrix the series can be summed by inspection, and that the answer identifies the unitary matrices as the exponentials of the Hermitian ones — the matrix version of \( \lvert e^{i\theta} \rvert = 1 \).

:::: {#thm-unitary-exponential}
[Unitary Matrices Are Exponentials of Hermitian Matrices]

Let \( n \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. If \( \A \in M_n(\nC) \) is normal with spectral resolution \( \A = \sum_{i}\lambda_i\P_i \), then \( e^{\A} = \sum_{i}e^{\lambda_i}\P_i \).
2. If \( \H \in M_n(\nC) \) is Hermitian, then \( e^{i\H} \in \Unit(n) \), and \( \det e^{i\H} = e^{\,i\tr\H} \).
3. Conversely, every \( \U \in \Unit(n) \) equals \( e^{i\H} \) for some Hermitian \( \H \), which may be chosen with \( \spec(\H) \subseteq [0, 2\pi) \).
:::
::::

::: {.idea}
For (a), the partial sums of the series collapse: \( \A^{m} = \sum_i\lambda_i^{m}\P_i \), so each partial sum is a fixed combination of the \( k \) scalar partial sums of \( \sum_m\lambda_i^{m}/m! \), whose limits are the numbers \( e^{\lambda_i} \). For (b) and (c), the resolution turns everything into a statement about \( k \) complex numbers: \( \H \) Hermitian means real eigenvalues, \( e^{i\H} \) then has eigenvalues on the unit circle, and a unitary matrix has eigenvalues on the unit circle, each of which is \( e^{i\theta} \) for a unique \( \theta \in [0, 2\pi) \). Reading the last sentence backwards constructs \( \H \).
:::

::: {.proof}
(a) By @thm-functional-calculus-properties (a), \( \A^{m} = \sum_{i}\lambda_i^{m}\P_i \) for every \( m \ge 0 \), so for every \( N \ge 0 \),
\[
\sum_{m=0}^{N}\frac{\A^{m}}{m!} = \sum_{i=1}^{k}\Bigl(\sum_{m=0}^{N}\frac{\lambda_i^{m}}{m!}\Bigr)\P_i .
\]
Fix a position \( (r,s) \). Its entry on the right is \( \sum_{i}c_{N,i}\,(\P_i)_{rs} \), where \( c_{N,i} = \sum_{m \le N}\lambda_i^{m}/m! \) and the coefficients \( (\P_i)_{rs} \) do not depend on \( N \). Each \( c_{N,i} \to e^{\lambda_i} \) as \( N \to \infty \) by the scalar exponential series, so the entry converges to \( \sum_ie^{\lambda_i}(\P_i)_{rs} \). Hence the series converges entrywise to \( \sum_ie^{\lambda_i}\P_i \), and by @def-matrix-exponential this matrix is \( e^{\A} \).

(b) \( \H \) is normal, so it has a spectral resolution \( \H = \sum_j\theta_j\P_j \), and its eigenvalues \( \theta_j \) are real by @thm-self-adjoint-real-eigenvalues. The scalars \( i\theta_j \) are distinct, so \( i\H = \sum_ji\theta_j\P_j \) is the spectral resolution of \( i\H \) by @thm-spectral-resolution-unique, and (a) gives
\[
e^{i\H} = \sum_{j}e^{\,i\theta_j}\P_j .
\]
Each \( \theta_j \) is real, so \( \conj{e^{\,i\theta_j}}\,e^{\,i\theta_j} = \lvert e^{\,i\theta_j}\rvert^2 = 1 \). Hence, using \( \P_j^{*} = \P_j \) and \( \P_j\P_{j'} = \delta_{jj'}\P_j \) from @thm-spectral-resolution (b),
\[
\bigl(e^{i\H}\bigr)^{*}e^{i\H} = \sum_{j}\conj{e^{\,i\theta_j}}e^{\,i\theta_j}\,\P_j = \sum_{j}\P_j = \I ,
\]
so \( e^{i\H} \in \Unit(n) \) by @def-unitary-orthogonal-groups. For the determinant, @thm-exponential-properties (e) gives \( \det e^{i\H} = e^{\tr(i\H)} = e^{\,i\tr\H} \).

(c) Let \( \U \in \Unit(n) \). Then \( \U^{*}\U = \U\U^{*} = \I \), so \( \U \) is normal; let \( \U = \sum_j\nu_j\P_j \) be its spectral resolution. Every eigenvalue has \( \lvert\nu_j\rvert = 1 \): if \( \U\x = \nu_j\x \) with \( \x \ne \0 \), then \( \norm{\x} = \norm{\U\x} = \lvert\nu_j\rvert\,\norm{\x} \) because \( \U \) is an isometry (@thm-isometry-characterizations), and \( \norm{\x} \ne 0 \). So there is a unique \( \theta_j \in [0, 2\pi) \) with \( \nu_j = e^{\,i\theta_j} \), and the \( \theta_j \) are distinct because the \( \nu_j \) are. Put
\[
\H \coloneqq \sum_{j}\theta_j\P_j .
\]
The \( \theta_j \) are real, so \( \H^{*} = \sum_j\theta_j\P_j^{*} = \H \) by @thm-adjoint-properties (a), (b) and @thm-spectral-resolution (b): \( \H \) is Hermitian, with \( \spec(\H) = \{\theta_j\} \subseteq [0, 2\pi) \) by @thm-spectral-resolution-unique. By (a) applied to \( i\H \),
\[
e^{i\H} = \sum_{j}e^{\,i\theta_j}\P_j = \sum_{j}\nu_j\P_j = \U .
\]
This proves the theorem.
:::

Part (c) says that the exponential map from Hermitian matrices to \( \Unit(n) \) is **onto**. One consequence belongs to topology rather than algebra, so we only record it: the path \( t \mapsto e^{\,it\H} \), \( t \in [0,1] \), stays inside \( \Unit(n) \) and runs from \( \I \) to \( \U \), so every unitary matrix can be deformed continuously to the identity. Nothing of the sort holds in \( \Orth(n) \), where the determinant is \( \pm1 \) and cannot change sign along a path.

::: {#exm-unitary-exponential-2x2}
[Exponentiating a Hermitian Matrix, and Undoing It]

Let \( \H = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \). Compute \( e^{\,i\theta\H} \) for \( \theta \in \nR \). Then find a Hermitian \( \K \) with \( e^{i\K} = \Q \), where \( \Q = \tfrac{1}{\sqrt2}\begin{pmatrix} 1 & -1 \\ 1 & 1\end{pmatrix} \).
:::

::: {.solution}
*Forwards.* \( \H \) is symmetric with \( \H(1,1) = (1,1) \) and \( \H(1,-1) = -(1,-1) \), so its eigenvalues are \( \pm1 \) and
\[
\H = \P_{+} - \P_{-}, \qquad
\P_{\pm} = \frac12\begin{pmatrix} 1 & \pm1 \\ \pm1 & 1\end{pmatrix} .
\]
Hence \( i\theta\H \) has resolution \( i\theta\P_{+} - i\theta\P_{-} \) (for \( \theta \ne 0 \)), and @thm-unitary-exponential (a) gives
\[
\begin{aligned}
e^{\,i\theta\H} &= e^{\,i\theta}\P_{+} + e^{-i\theta}\P_{-} \\
  &= \begin{pmatrix} \cos\theta & i\sin\theta \\ i\sin\theta & \cos\theta \end{pmatrix},
\end{aligned}
\]
using \( e^{\pm i\theta} = \cos\theta \pm i\sin\theta \). Each row has squared length \( \cos^2\theta + \sin^2\theta = 1 \) and the two rows are orthogonal, confirming that the result is unitary.

*Backwards.* \( \Q \) is the rotation by \( \pi/4 \), hence unitary, with \( \Q(1,-i) = e^{\,i\pi/4}(1,-i) \) and \( \Q(1,i) = e^{-i\pi/4}(1,i) \). Both eigenvectors have squared length \( 2 \), so the spectral projections are
\[
\R_{+} = \frac12\begin{pmatrix} 1 & i \\ -i & 1\end{pmatrix},
\qquad
\R_{-} = \frac12\begin{pmatrix} 1 & -i \\ i & 1\end{pmatrix} .
\]
Writing \( e^{-i\pi/4} = e^{\,i\cdot 7\pi/4} \) to land in \( [0, 2\pi) \), the recipe of @thm-unitary-exponential (c) gives
\[
\K = \frac{\pi}{4}\R_{+} + \frac{7\pi}{4}\R_{-}
   = \begin{pmatrix} \pi & -\tfrac{3\pi i}{4} \\[2pt] \tfrac{3\pi i}{4} & \pi \end{pmatrix},
\]
Hermitian with spectrum \( \{\pi/4,\, 7\pi/4\} \). Leaving \( [0, 2\pi) \), the smaller choice \( \tfrac{\pi}{4}(\R_{+} - \R_{-}) = \tfrac{\pi}{4}\begin{pmatrix} 0 & i \\ -i & 0\end{pmatrix} \) works just as well: the Hermitian logarithm is far from unique.
:::

## Exercises

### A. Check your understanding

:::: {#exr-spectral-resolutions-and-functional-calculus-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the spectral resolution of \( T \), and say which operators have one over \( \nC \) and which over \( \nR \).
2. List the properties of the family \( (P_1, \dots, P_k) \) given by @thm-spectral-resolution, and say how many terms the resolution of a self-adjoint \( T \in \cL(\nR^5) \) with eigenvalues \( 2, 2, 2, 7, 7 \) has.
3. True or false: if \( T = \mu_1Q_1 + \mu_2Q_2 \) with \( \mu_1 \ne \mu_2 \) and \( Q_1, Q_2 \) non-zero operators satisfying \( Q_i^2 = Q_i \), \( Q_1Q_2 = Q_2Q_1 = 0 \) and \( Q_1 + Q_2 = \id_V \), then \( T \) is normal. Justify your answer.
4. Define \( f(T) \) for a function \( f \) on \( \spec(T) \), and say exactly how much information about \( f \) it uses.
5. State @thm-functional-calculus-properties (a) and explain in one sentence why the rest of the section would be unusable without it.
6. Give two different self-adjoint square roots of \( \id_V \) on \( \nR^2 \), and say which one @thm-normal-square-root singles out and why.
:::
::::

::: {.solution}
(a) For \( T \) with an orthonormal basis of eigenvectors, distinct eigenvalues \( \lambda_1, \dots, \lambda_k \) and \( P_i = P_{E_{\lambda_i}(T)} \) the orthogonal projection onto the \( i \)-th eigenspace, the spectral resolution is \( T = \sum_i\lambda_iP_i \) (@def-spectral-resolution). Over \( \nC \) the operators with one are exactly the normal operators (@thm-spectral-complex); over \( \nR \), exactly the self-adjoint ones (@thm-spectral-real).

(b) Each \( P_i \) is self-adjoint and idempotent, \( P_iP_j = 0 \) for \( i \ne j \), \( \sum_iP_i = \id_V \), and \( TP_i = P_iT = \lambda_iP_i \). The resolution has **two** terms, \( T = 2P_1 + 7P_2 \), with \( \rank P_1 = 3 \) and \( \rank P_2 = 2 \): the resolution counts distinct eigenvalues, not multiplicities.

(c) False. Self-adjointness of the \( Q_i \) is missing, and it is the one hypothesis of @thm-spectral-resolution-unique that does the work. The matrices \( \vpi_1, \vpi_2 \) of @exm-oblique-projections satisfy everything listed, with \( \mu_1 = 1 \) and \( \mu_2 = 2 \), and \( \vpi_1 + 2\vpi_2 = \begin{pmatrix} 1 & 1 \\ 0 & 2\end{pmatrix} \), which is not normal.

(d) \( f(T) = \sum_if(\lambda_i)P_i \) (@def-function-of-normal-operator). It uses exactly the \( k \) values \( f(\lambda_1), \dots, f(\lambda_k) \); two functions agreeing on \( \spec(T) \) give the same operator, and \( f \) need not be defined, let alone continuous, anywhere else.

(e) For \( p \in F[x] \), the operator \( \sum_ip(\lambda_i)P_i \) coincides with the operator \( p(T) \) of @def-polynomial-of-operator. Without it, the symbol \( p(T) \) would carry two unrelated meanings at once, and no computation mixing polynomials with other functions — for instance \( (\sqrt{T})^2 = T \) — could be trusted.

(f) \( \id \) and the reflection \( T_{\D} \) with \( \D = \diag(1, -1) \), both self-adjoint with square \( \id \). @thm-normal-square-root singles out \( \id \), because \( \spec(\id) = \{1\} \subseteq [0,\infty) \) while \( \spec(T_{\D}) = \{1, -1\} \) is not. (A third root is \( -\id \), and a fourth is \( T_{\D'} \) with \( \D' = \diag(-1, 1) \).)
:::

### B. Practice

:::: {#exr-spectral-resolutions-and-functional-calculus-b1}
[B1: Write these as \( \sum\lambda_i\P_i \)]

Find the spectral resolution of each of the following matrices, and check in each case that the projections are self-adjoint, idempotent, mutually annihilating and sum to \( \I \).

::: {.enumerate options="label=(\alph*)"}
1. \( \A = \begin{pmatrix} 2 & 1 - i \\ 1 + i & 3 \end{pmatrix} \in M_2(\nC) \).
2. \( \S = \begin{pmatrix} 2 & 0 & 1 \\ 0 & 3 & 0 \\ 1 & 0 & 2 \end{pmatrix} \in M_3(\nR) \).
3. \( \U = \tfrac{1}{\sqrt2}\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} \in M_2(\nC) \).
:::
::::

::: {.solution}
(a) \( \A^{*} = \A \), \( \tr\A = 5 \) and \( \det\A = 6 - (1-i)(1+i) = 4 \), so \( p_{\A} = x^2 - 5x + 4 \) and \( \spec(\A) = \{1, 4\} \). From \( \A - 4\I = \begin{pmatrix} -2 & 1-i \\ 1+i & -1\end{pmatrix} \) the first row gives the eigenvector \( \v_4 = (1-i, 2) \), with \( \norm{\v_4}^2 = 2 + 4 = 6 \); from \( \A - \I \) likewise \( \v_1 = (-1+i, 1) \), with \( \norm{\v_1}^2 = 3 \). Hence
\[
\P_4 = \frac{\v_4\v_4^{*}}{6} = \frac13\begin{pmatrix} 1 & 1-i \\ 1+i & 2\end{pmatrix},
\qquad
\P_1 = \frac13\begin{pmatrix} 2 & -1+i \\ -1-i & 1\end{pmatrix},
\]
and \( \A = 1 \cdot \P_1 + 4 \cdot \P_4 \). Both are Hermitian, both square to themselves, \( \P_1\P_4 = 0 \), and \( \P_1 + \P_4 = \I \).

(b) \( \S \) is symmetric, and \( \S(1,0,1) = 3(1,0,1) \), \( \S(0,1,0) = 3(0,1,0) \), \( \S(1,0,-1) = (1,0,-1) \), so \( \spec(\S) = \{3, 1\} \) with \( E_1 = \Span((1,0,-1)) \) and \( E_3 = \Span((1,0,1), (0,1,0)) \). Hence
\[
\P_1 = \frac12\begin{pmatrix} 1 & 0 & -1 \\ 0 & 0 & 0 \\ -1 & 0 & 1\end{pmatrix},
\qquad
\P_3 = \I - \P_1 = \frac12\begin{pmatrix} 1 & 0 & 1 \\ 0 & 2 & 0 \\ 1 & 0 & 1\end{pmatrix},
\]
and \( \S = \P_1 + 3\P_3 \). The stated properties follow from \( \P_1\tp = \P_1 \), \( \P_1^2 = \P_1 \) and \( \P_3 = \I - \P_1 \).

(c) \( \U \) is real orthogonal, hence unitary and normal. Since \( \U(1, -i) = \tfrac{1}{\sqrt2}(1 + i, 1 - i) = e^{\,i\pi/4}(1, -i) \), and similarly \( \U(1, i) = e^{-i\pi/4}(1, i) \), we get \( \spec(\U) = \{e^{\pm i\pi/4}\} \). Both eigenvectors have squared length \( 2 \), so with \( \v_{\pm} = (1, \mp i) \),
\[
\P_{\pm} = \frac{\v_{\pm}\v_{\pm}^{*}}{2} = \frac12\begin{pmatrix} 1 & \pm i \\ \mp i & 1\end{pmatrix},
\qquad
\U = e^{\,i\pi/4}\P_{+} + e^{-i\pi/4}\P_{-} .
\]
Both are Hermitian and idempotent, \( \P_{+}\P_{-} = 0 \) and \( \P_{+} + \P_{-} = \I \).
:::

:::: {#exr-spectral-resolutions-and-functional-calculus-b2}
[B2: Computing through the resolution]

Let \( \C = \begin{pmatrix} 13 & 12 \\ 12 & 13 \end{pmatrix} \in M_2(\nR) \).

::: {.enumerate options="label=(\alph*)"}
1. Find the spectral resolution of \( \C \).
2. Hence compute \( \sqrt{\C} \), and verify by squaring.
3. Hence give a closed formula for \( \C^{m} \) and write down \( \C^{100} \).
4. Hence compute \( e^{\C} \).
:::
::::

::: {.solution}
(a) \( \C(1,1) = 25(1,1) \) and \( \C(1,-1) = (1,-1) \), so \( \spec(\C) = \{25, 1\} \) and, both spanning vectors having squared length \( 2 \),
\[
\P_1 = \frac12\begin{pmatrix} 1 & 1 \\ 1 & 1\end{pmatrix},
\qquad
\P_2 = \frac12\begin{pmatrix} 1 & -1 \\ -1 & 1\end{pmatrix},
\qquad
\C = 25\P_1 + \P_2 .
\]

(b) Both eigenvalues are positive, so by @thm-normal-square-root,
\[
\sqrt{\C} = 5\P_1 + 1 \cdot \P_2 = \begin{pmatrix} 3 & 2 \\ 2 & 3\end{pmatrix},
\]
and \( \begin{pmatrix} 3 & 2 \\ 2 & 3\end{pmatrix}^2 = \begin{pmatrix} 13 & 12 \\ 12 & 13\end{pmatrix} = \C \).

(c) By @thm-functional-calculus-properties (a), \( \C^{m} = 25^{m}\P_1 + 1^{m}\P_2 \), that is
\[
\C^{m} = \frac12\begin{pmatrix} 25^{m} + 1 & 25^{m} - 1 \\ 25^{m} - 1 & 25^{m} + 1\end{pmatrix} ,
\]
so \( \C^{100} = \tfrac12\bigl(\begin{smallmatrix} 25^{100} + 1 & 25^{100} - 1 \\ 25^{100} - 1 & 25^{100} + 1\end{smallmatrix}\bigr) \). (As a check, \( m = 2 \) gives \( \tfrac12\bigl(\begin{smallmatrix} 626 & 624 \\ 624 & 626\end{smallmatrix}\bigr) = \bigl(\begin{smallmatrix} 313 & 312 \\ 312 & 313\end{smallmatrix}\bigr) \), which is \( \C^2 \).)

(d) By @thm-unitary-exponential (a),
\[
e^{\C} = e^{25}\P_1 + e\,\P_2 = \frac12\begin{pmatrix} e^{25} + e & e^{25} - e \\ e^{25} - e & e^{25} + e\end{pmatrix} .
\]
:::

:::: {#exr-spectral-resolutions-and-functional-calculus-b3}
[B3: Is it a spectral resolution?]

Determine which of the following displays the spectral resolution of the operator \( T_{\A} \) on the stated space. Justify your answer; for those that do not, name the condition of @thm-spectral-resolution-unique that fails and say what the correct resolution is.

::: {.enumerate options="label=(\alph*)"}
1. On \( \nR^2 \): \( \A = \begin{pmatrix} 2 & 0 \\ 0 & -1 \end{pmatrix} \), with \( \mu_1 = 2 \), \( \Q_1 = \begin{pmatrix} 1 & 0 \\ 0 & 0\end{pmatrix} \), \( \mu_2 = -1 \), \( \Q_2 = \begin{pmatrix} 0 & 0 \\ 0 & 1\end{pmatrix} \).
2. On \( \nR^2 \): \( \A = 3\I \), with \( \mu_1 = \mu_2 = 3 \), \( \Q_1 = \tfrac12\begin{pmatrix} 1 & 1 \\ 1 & 1\end{pmatrix} \), \( \Q_2 = \tfrac12\begin{pmatrix} 1 & -1 \\ -1 & 1\end{pmatrix} \).
3. On \( \nR^2 \): \( \A = \begin{pmatrix} 3 & 1 \\ 0 & 1 \end{pmatrix} \), with \( \mu_1 = 3 \), \( \Q_1 = \tfrac12\begin{pmatrix} 2 & 1 \\ 0 & 0\end{pmatrix} \), \( \mu_2 = 1 \), \( \Q_2 = \tfrac12\begin{pmatrix} 0 & -1 \\ 0 & 2\end{pmatrix} \).
:::
::::

::: {.solution}
(a) Yes. The two matrices are symmetric, idempotent, non-zero, annihilate each other and sum to \( \I \), and \( 2\Q_1 - \Q_2 = \A \); the coefficients \( 2 \) and \( -1 \) are distinct. By @thm-spectral-resolution-unique this is the spectral resolution, and indeed \( E_2 = \Span(\e_1) \), \( E_{-1} = \Span(\e_2) \).

(b) No: the scalars \( \mu_1, \mu_2 \) are not **distinct**, so the hypothesis of @thm-spectral-resolution-unique fails at once. The identity \( 3\Q_1 + 3\Q_2 = 3\I = \A \) is true but uninformative — the eigenvalue \( 3 \) has been split artificially across two projections. The spectral resolution of \( 3\I \) has a single term, \( 3\I = 3 \cdot \id \), since \( \spec(3\I) = \{3\} \) and \( E_3 = \nR^2 \).

(c) No: \( \Q_1 \) is not self-adjoint, since \( \Q_1^{\top} = \tfrac12\begin{pmatrix} 2 & 0 \\ 1 & 0\end{pmatrix} \ne \Q_1 \), so (R1) fails. Everything else holds: \( \Q_1^2 = \Q_1 \), \( \Q_2 = \I - \Q_1 \), \( \Q_1\Q_2 = \Q_2\Q_1 = 0 \) and \( 3\Q_1 + \Q_2 = \A \). There is no correct resolution to offer, because \( \A \) is not normal: \( \A\tp\A = \begin{pmatrix} 9 & 3 \\ 3 & 2\end{pmatrix} \) while \( \A\A\tp = \begin{pmatrix} 10 & 1 \\ 1 & 1\end{pmatrix} \). The projections here are onto \( E_3 = \Span(\e_1) \) along \( E_1 = \Span((-1, 2)) \), two lines that are not perpendicular.
:::

### C. Going deeper

:::: {#exr-spectral-resolutions-and-functional-calculus-c1}
[C1: The projections are polynomials in the operator]

Let \( T \in \cL(V) \) satisfy \( (\ast) \), with distinct eigenvalues \( \lambda_1, \dots, \lambda_k \in F \) and resolution of the identity \( (P_1, \dots, P_k) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( P_i = \ell_i(T) \), where \( \ell_i \in F[x] \) is the \( i \)-th Lagrange basis polynomial for the nodes \( \lambda_1, \dots, \lambda_k \).
2. Deduce that for every \( f \colon \spec(T) \to F \) there is a polynomial \( p \) of degree less than \( k \) with \( f(T) = p(T) \).
3. Deduce that every operator commuting with \( T \) commutes with each \( P_i \), re-proving @thm-functional-calculus-properties (e) by a different route.
:::

*Hint for (a): @def-lagrange-basis produces a polynomial taking prescribed values at prescribed nodes.*
::::

::: {.solution}
(a) The \( \lambda_i \) are \( k \) distinct elements of \( F \), so @def-lagrange-basis gives \( \ell_1, \dots, \ell_k \in F[x] \) of degree \( k - 1 \), and @thm-lagrange-interpolation (a) gives \( \ell_i(\lambda_j) = \delta_{ij} \). By @thm-functional-calculus-properties (a),
\[
\ell_i(T) = \sum_{j=1}^{k}\ell_i(\lambda_j)P_j = \sum_{j=1}^{k}\delta_{ij}P_j = P_i .
\]

(b) Let \( p \) be the interpolating polynomial of degree less than \( k \) with \( p(\lambda_i) = f(\lambda_i) \) for every \( i \), which exists by @thm-lagrange-interpolation. By @thm-functional-calculus-properties (a),
\[
p(T) = \sum_{i}p(\lambda_i)P_i = \sum_{i}f(\lambda_i)P_i = f(T) .
\]
Explicitly, \( p = \sum_if(\lambda_i)\ell_i \).

(c) If \( ST = TS \), then \( S \) commutes with every polynomial in \( T \) by @thm-evaluation-homomorphism (d), in particular with \( \ell_i(T) = P_i \).
:::

:::: {#exr-spectral-resolutions-and-functional-calculus-c2}
[C2: When the projections have rank one]

Let \( T \in \cL(V) \) satisfy \( (\ast) \), with \( \dim V = n \) and resolution of the identity \( (P_1, \dots, P_k) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \rank P_i = \dim E_{\lambda_i}(T) \) and that \( \sum_i\rank P_i = n \).
2. Deduce that every \( P_i \) has rank \( 1 \) if and only if \( T \) has \( n \) distinct eigenvalues.
3. Suppose every \( P_i \) has rank \( 1 \). Prove that every \( S \in \cL(V) \) commuting with \( T \) is a polynomial in \( T \).
:::
::::

::: {.solution}
(a) \( \im P_i = E_{\lambda_i}(T) \) by @def-orthogonal-projection, so \( \rank P_i = \dim E_{\lambda_i}(T) \). By @thm-spectral-resolution (a), \( V = E_1 \oplus \dots \oplus E_k \), so the dimensions add to \( n \).

(b) If every \( \rank P_i = 1 \), then (a) gives \( k = n \), so \( T \) has \( n \) distinct eigenvalues. Conversely, if \( T \) has \( n \) distinct eigenvalues, then \( k = n \) and (a) forces each of the \( n \) positive integers \( \rank P_i \) to be \( 1 \).

(c) By (b), \( k = n \) and each \( E_i \) is a line, say \( E_i = \Span(\e_i) \) with \( (\e_1, \dots, \e_n) \) an orthonormal eigenbasis. Let \( ST = TS \). As in the proof of @thm-functional-calculus-properties (e), \( S \) maps \( E_i \) into itself, so \( S\e_i = c_i\e_i \) for some \( c_i \in F \). Define \( f \colon \spec(T) \to F \) by \( f(\lambda_i) = c_i \). Then \( f(T)\e_i = c_i\e_i = S\e_i \) for every \( i \), and two operators agreeing on a basis are equal, so \( S = f(T) \). By @exr-spectral-resolutions-and-functional-calculus-c1 (b), \( f(T) \) is a polynomial in \( T \).
:::

:::: {#exr-spectral-resolutions-and-functional-calculus-c3}
[C3: What the functional calculus forgets]

Let \( T \in \cL(V) \) satisfy \( (\ast) \), with distinct eigenvalues \( \lambda_1, \dots, \lambda_k \), and let \( f, g \colon \spec(T) \to F \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( f(T) = 0 \) if and only if \( f(\lambda_i) = 0 \) for every \( i \). Deduce that \( f(T) = g(T) \) if and only if \( f = g \).
2. Deduce that \( \{ p(T) : p \in F[x] \} = \Span(P_1, \dots, P_k) \), a subspace of \( \cL(V) \) of dimension exactly \( k \).
3. Deduce that \( m_T = (x - \lambda_1)(x - \lambda_2)\cdots(x - \lambda_k) \), so that the minimal polynomial of an operator satisfying \( (\ast) \) has no repeated root.
:::
::::

::: {.solution}
(a) \( (\Leftarrow) \) is immediate from @def-function-of-normal-operator. For \( (\Rightarrow) \), fix \( i \) and pick \( \v \in E_{\lambda_i}(T) \) with \( \v \ne \0 \), which is possible because \( \lambda_i \) is an eigenvalue. Then \( P_i\v = \v \) and \( P_j\v = \0 \) for \( j \ne i \), since \( E_i \subseteq \ker P_j \) (@thm-spectral-resolution (a), (b)). Hence
\[
\0 = f(T)\v = \sum_{j}f(\lambda_j)P_j\v = f(\lambda_i)\v ,
\]
and \( \v \ne \0 \) forces \( f(\lambda_i) = 0 \). For the second claim, apply this to \( f - g \), using @thm-functional-calculus-properties (b).

(b) By @thm-functional-calculus-properties (a), every \( p(T) \) equals \( \sum_ip(\lambda_i)P_i \), so the left-hand side is contained in \( \Span(P_1, \dots, P_k) \); conversely every \( \sum_ic_iP_i \) is \( f(T) \) for the function \( f(\lambda_i) = c_i \), hence is a polynomial in \( T \) by @exr-spectral-resolutions-and-functional-calculus-c1 (b). The \( P_i \) are linearly independent: if \( \sum_ic_iP_i = 0 \), that operator is \( f(T) \) for \( f(\lambda_i) = c_i \), so every \( c_i = 0 \) by (a). Hence the dimension is \( k \).

(c) Put \( p = \prod_i(x - \lambda_i) \), monic of degree \( k \). Since \( p(\lambda_i) = 0 \) for every \( i \), part (a) gives \( p(T) = 0 \), so \( m_T \mid p \) by @thm-minimal-polynomial-divides. Conversely \( m_T(T) = 0 \), so \( m_T(\lambda_i) = 0 \) for every \( i \) by (a), and hence each \( x - \lambda_i \) divides \( m_T \) (@thm-remainder-theorem (b)). Distinct monic linear polynomials are coprime, since a common divisor would divide their difference, a non-zero constant; so \( p = \prod_i(x - \lambda_i) \) divides \( m_T \) by @lem-coprime-product (b). Two monic polynomials dividing each other are equal, so \( m_T = p \), a product of distinct linear factors.
:::
