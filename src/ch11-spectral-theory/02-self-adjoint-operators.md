# Self-Adjoint Operators

Among complex numbers, the real ones are those fixed by conjugation: \( \conj{z} = z \). Among operators on an inner product space, conjugation is replaced by the adjoint, and the operators fixed by it are the **self-adjoint** ones, \( T^{*} = T \). The analogy is not decoration. Self-adjoint operators have real eigenvalues, they come with a real-valued quantity \( \inner{T\v}{\v} \) attached to every vector, they can be compared and ordered, and over \( \nR \) they are exactly the operators the spectral theorem applies to. This section collects everything about them that does not need a spectral theorem, and in doing so assembles every ingredient the real spectral theorem of Section 5 will use.

Throughout, \( V \) is a finite-dimensional inner product space over \( F = \nR \) or \( F = \nC \), and \( T \in \cL(V) \).

## The operators fixed by starring

Chapter 10 already made the definition, so we only recall it: \( T \in \cL(V) \) is **self-adjoint** when \( T^{*} = T \), equivalently when
\[
\inner{T\u}{\v} = \inner{\u}{T\v} \qquad \text{for all } \u, \v \in V
\]
(@def-self-adjoint). In an orthonormal basis this says the matrix is **Hermitian**, \( \A^{*} = \A \), which over \( \nR \) is **symmetric**, \( \A\tp = \A \) (@thm-matrix-of-adjoint). Three facts were proved there and will be used without further comment: \( \inner{T\v}{\v} \) is real for every \( \v \), even over \( \nC \); the diagonal entries of the matrix in an orthonormal basis are real; and every self-adjoint operator is normal (@prp-self-adjoint-immediate).

Deciding self-adjointness is always the same job — compute \( T^{*} \), or check the displayed identity on a basis — but the traps differ by example.

::: {#exm-self-adjoint-tests}
[Four Tests]

Determine which of the following are self-adjoint. Justify your answer; for those that are not, name the failing pair of vectors.

::: {.enumerate options="label=(\alph*)"}
1. \( T_{\A} \) on \( \nC^2 \) with the standard inner product, \( \A = \begin{pmatrix} 2 & 1 - i \\ 1 + i & 3 \end{pmatrix} \).
2. \( T_{\B} \) on \( \nC^2 \) with the standard inner product, \( \B = \begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix} \).
3. Differentiation \( D \) on \( V = \nR[x]_{\le 2} \) with \( \inner{p}{q} = \int_0^1 pq \).
4. The orthogonal projection \( P_U \) onto a subspace \( U \) of any \( V \).
:::
:::

::: {.solution}
(a) Self-adjoint. Transposing swaps the off-diagonal entries and conjugating swaps them back, while the diagonal entries \( 2 \) and \( 3 \) are real; so \( \A^{*} = \A \). The standard basis of \( \nC^2 \) is orthonormal, so @thm-matrix-of-adjoint turns this into \( T_{\A}^{*} = T_{\A} \).

(b) Not self-adjoint. It is **symmetric**, \( \B\tp = \B \), but \( \B^{*} = \begin{pmatrix} 1 & -i \\ -i & 1 \end{pmatrix} \ne \B \). The failing pair is \( \e_1, \e_2 \): \( \inner{\B\e_1}{\e_2} = i \), while \( \inner{\e_1}{\B\e_2} = \conj{i} = -i \).

(c) Not self-adjoint. Take \( p = x \) and \( q = 1 \). Then \( Dp = 1 \) and \( Dq = 0 \), so
\[
\inner{Dp}{q} = \int_0^1 1 \, \dd x = 1, \qquad \inner{p}{Dq} = 0 .
\]
The obstruction is visible in general: integration by parts gives
\[
\inner{Dp}{q} + \inner{p}{Dq} = p(1)q(1) - p(0)q(0),
\]
so \( D \) is as far from self-adjoint as it could be — the two sides add up rather than agreeing, apart from boundary terms.

(d) Self-adjoint, for every \( U \). By @thm-projection-formula (b), \( \inner{P_U\u}{\v} = \inner{\u}{P_U\v} \) for all \( \u, \v \), which is the displayed identity.
:::

::: {.warning}
**Over \( \nC \), symmetric is not the right notion; Hermitian is.** Part (b) above is symmetric and its eigenvalues are not even real: \( \tr\B = 2 \) and \( \det\B = 1 - i^2 = 2 \), so \( p_{\B} = x^2 - 2x + 2 \) and the eigenvalues are \( 1 + i \) and \( 1 - i \). Every theorem in this section would fail for it. The word "symmetric matrix" belongs to the **real** case, where conjugation does nothing and \( \A^{*} = \A\tp \); over \( \nC \) always write, and check, \( \A^{*} = \A \).
:::

## Eigenvalues are real

The first theorem is the operator version of "a number equal to its own conjugate is real", and its proof is the move that runs this whole chapter: compute one inner product two different ways.

::: {#thm-self-adjoint-real-eigenvalues}
[Self-adjoint Operators Have Real Eigenvalues]

Let \( V \) be a finite-dimensional inner product space over \( F = \nR \) or \( F = \nC \) and let \( T \in \cL(V) \) be self-adjoint. Then every eigenvalue of \( T \) is real.
:::

::: {.idea}
Take \( T\v = \lambda\v \) with \( \v \ne \0 \) and pair it with \( \v \). Computing \( \inner{T\v}{\v} \) straight off the eigenvalue equation produces \( \lambda \); computing it by pushing \( T \) into the second slot produces \( \conj\lambda \), because a scalar leaving the second slot picks up a conjugate. The two answers must agree, and \( \norm{\v}^2 \ne 0 \) lets us cancel.
:::

::: {.proof}
Let \( \lambda \) be an eigenvalue of \( T \), with eigenvector \( \v \ne \0 \). On one side,
\[
\inner{T\v}{\v} = \inner{\lambda\v}{\v} = \lambda\norm{\v}^2 ,
\]
by linearity in the first slot. On the other, using @def-self-adjoint and then conjugate-linearity in the second slot,
\[
\inner{T\v}{\v} = \inner{\v}{T\v} = \inner{\v}{\lambda\v} = \conj{\lambda}\norm{\v}^2 .
\]
So \( \lambda\norm{\v}^2 = \conj{\lambda}\norm{\v}^2 \). Since \( \v \ne \0 \) we have \( \norm{\v}^2 \ne 0 \) by positive definiteness (@def-inner-product), and dividing gives \( \lambda = \conj{\lambda} \). A scalar equal to its own conjugate is real.
:::

Chapter 10 already proved this, in the remark after @prp-self-adjoint-immediate. It is promoted to a theorem here because Sections 3 to 5 lean on it constantly, and a result cited that often should have a number. Over \( \nR \) the conclusion sounds empty, because the eigenvalues of a real operator are real by definition. What is not empty over \( \nR \) is the corresponding statement about the **roots of the characteristic polynomial**, and that is the next theorem: it says the roots do not escape into \( \nC \), which is exactly what guarantees that a real self-adjoint operator has an eigenvector at all.

## Existence over the real numbers

Over \( \nC \) an eigenvalue is free (@thm-complex-operator-has-eigenvalue). Over \( \nR \) it is not, and the rotation of \( \nR^2 \) by a quarter turn has none. Self-adjointness is what rules that out.

::: {#thm-self-adjoint-has-eigenvalue}
[Real Self-adjoint Operators Have an Eigenvalue]

Let \( V \ne \{\0\} \) be a finite-dimensional inner product space over \( \nR \) and let \( T \in \cL(V) \) be self-adjoint. Then:

::: {.enumerate options="label=(\alph*)"}
1. every root of \( p_T \) in \( \nC \) is real, so \( p_T \) splits over \( \nR \);
2. \( T \) has an eigenvalue.
:::
:::

::: {.idea}
There is no complex number in sight, so we put one there. Fix an orthonormal basis; the matrix \( \A \) of \( T \) is real symmetric. The same array of numbers, read as a complex matrix, is Hermitian, and it acts on \( \nC^n \), which is the complexification of \( \nR^n \) (@def-complexification, @exm-complexification-rn) — the arena Chapter 1 built, and Chapter 8 put to work, precisely so that a real matrix could borrow complex eigenvalues. Over \( \nC \) an eigenvalue exists, and @thm-self-adjoint-real-eigenvalues says it is real. A real root of \( p_T \) is an eigenvalue of \( T \) itself, and we are back where we started, one eigenvalue richer.
:::

::: {.proof}
Let \( n = \dim V \ge 1 \). By @thm-gram-schmidt, \( V \) has an orthonormal basis \( \sB \); put \( \A = \mtx{T}{\sB}{\sB} \in M_n(\nR) \). By @thm-matrix-of-adjoint and @def-self-adjoint, \( \A^{*} = \A \), and since \( \A \) is real this says \( \A\tp = \A \).

Now read \( \A \) as an element of \( M_n(\nC) \), acting on \( \nC^n \) with the standard inner product; this is the extension of the real map \( T_{\A} \) to the complexification \( (\nR^n)_{\nC} = \nC^n \), which acts on \( \x + i\y \) by \( \A\x + i\A\y \) (Chapter 8, Section 2). Because \( \A \) is real and symmetric, \( \A^{*} = \conj{\A}\tp = \A\tp = \A \), so \( T_{\A} \) is self-adjoint as an operator on \( \nC^n \) (@thm-matrix-of-adjoint again, the standard basis of \( \nC^n \) being orthonormal).

(a) By @def-charpoly-operator, \( p_T = p_{\A} \), and the entries of \( x\I - \A \) are real, so this is the same polynomial whether the determinant is expanded over \( \nR \) or over \( \nC \); it lies in \( \nR[x] \subseteq \nC[x] \). Let \( \lambda \in \nC \) be a root of \( p_{\A} \). By @thm-eigenvalue-characterizations, \( \lambda \) is an eigenvalue of \( \A \) over \( \nC \), and \( \A \) is self-adjoint there, so \( \lambda \in \nR \) by @thm-self-adjoint-real-eigenvalues. Since every root of \( p_T \) in \( \nC \) lies in \( \nR \), and \( p_T \) splits over \( \nC \) by @cor-complex-polynomial-splits, it splits over \( \nR \).

(b) \( p_T \) is monic of degree \( n \ge 1 \) (@thm-charpoly-coefficients), so by (a) it has a root \( \lambda \in \nR \). By @thm-eigenvalue-characterizations ((e) \( \Rightarrow \) (a)), \( \lambda \) is an eigenvalue of \( T \). This proves the theorem.
:::

::: {.remark}
There is a second, very different route to (b): the function \( \v \mapsto \inner{T\v}{\v} \) is real-valued and continuous on the unit sphere of \( V \), which is closed and bounded, so it attains a maximum, and a vector where it does so turns out to be an eigenvector for the largest eigenvalue. That argument is shorter to state but it is analysis, not algebra, and it appeals to the extreme value theorem directly. We keep to the algebraic route, which reaches that theorem only at one remove: the proof just given rests on @cor-complex-polynomial-splits, hence on the fundamental theorem of algebra (@thm-fundamental-theorem-of-algebra), and the proof of that in Chapter 5 uses the extreme value theorem on a closed disc. The maximization picture returns in Chapter 16, where the Rayleigh quotient and the Courant–Fischer theorem describe every eigenvalue of a self-adjoint operator by optimization.
:::

::: {.check}
The rotation \( \R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \) on \( \nR^2 \) has no eigenvalue, and over \( \nC \) its eigenvalues \( \pm i \) are not real. Which hypothesis of @thm-self-adjoint-has-eigenvalue does it fail, and how do you see it in one line?
:::

::: {.solution}
Self-adjointness. In the standard orthonormal basis the matrix of \( \R^{*} \) is \( \R\tp = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = -\R \), which is not \( \R \). So \( \R \) is skew-adjoint, not self-adjoint, and neither theorem applies. (It is, however, normal, since \( \R\tp\R = \R\R\tp = \I \) — which is why Section 5 has to insist on self-adjoint rather than normal over \( \nR \).)
:::

## Eigenvectors for different eigenvalues are orthogonal

The second theorem is the same move with two vectors instead of one, and it is the geometric half of the spectral theorem: the eigenspaces are not merely independent, as in Chapter 8, but perpendicular.

::: {#thm-self-adjoint-orthogonal-eigenspaces}
[Distinct Eigenvalues Give Orthogonal Eigenvectors]

Let \( T \in \cL(V) \) be self-adjoint, and let \( \u, \v \in V \) satisfy \( T\u = \lambda\u \) and \( T\v = \mu\v \) with \( \lambda \ne \mu \). Then \( \inner{\u}{\v} = 0 \). Consequently \( E_\lambda(T) \perp E_\mu(T) \) for distinct eigenvalues \( \lambda, \mu \).
:::

::: {.proof}
Compute \( \inner{T\u}{\v} \) two ways. First, \( \inner{T\u}{\v} = \inner{\lambda\u}{\v} = \lambda\inner{\u}{\v} \). Second, by @def-self-adjoint and conjugate-linearity in the second slot,
\[
\inner{T\u}{\v} = \inner{\u}{T\v} = \inner{\u}{\mu\v} = \conj{\mu}\inner{\u}{\v} = \mu\inner{\u}{\v},
\]
the last step because \( \mu \) is real by @thm-self-adjoint-real-eigenvalues. Subtracting, \( (\lambda - \mu)\inner{\u}{\v} = 0 \), and \( \lambda - \mu \ne 0 \), so \( \inner{\u}{\v} = 0 \). Since every element of \( E_\lambda(T) \) is such a \( \u \) and every element of \( E_\mu(T) \) such a \( \v \), the two eigenspaces are orthogonal.
:::

Note where the previous theorem was spent: it made \( \conj{\mu} = \mu \), so that the conjugation which appears on the way out of the second slot does no damage. Without real eigenvalues the computation would end at \( \lambda\inner{\u}{\v} = \conj{\mu}\inner{\u}{\v} \), which says nothing when \( \lambda = \conj{\mu} \).

::: {#exm-hermitian-2x2-eigen}
[A Hermitian Two-by-Two]

For \( \A = \begin{pmatrix} 2 & 1 - i \\ 1 + i & 3 \end{pmatrix} \) on \( \nC^2 \), find the eigenvalues and an eigenvector for each, and verify that the two eigenvectors are orthogonal.
:::

::: {.solution}
Here \( \tr\A = 5 \) and \( \det\A = 6 - (1 - i)(1 + i) = 6 - 2 = 4 \), so
\[
p_{\A} = x^2 - 5x + 4 = (x - 1)(x - 4) .
\]
Both eigenvalues are real, as @thm-self-adjoint-real-eigenvalues promised.

For \( \lambda = 1 \): \( \A - \I = \begin{pmatrix} 1 & 1 - i \\ 1 + i & 2 \end{pmatrix} \), and the first row gives \( x + (1 - i)y = 0 \), so \( \u = (-1 + i, 1) \). Check the second row: \( (1 + i)(-1 + i) + 2 = (-1 + i - i + i^2) + 2 = -2 + 2 = 0 \).

For \( \lambda = 4 \): \( \A - 4\I = \begin{pmatrix} -2 & 1 - i \\ 1 + i & -1 \end{pmatrix} \), and the first row gives \( -2x + (1 - i)y = 0 \), so \( \v = (1 - i, 2) \).

Finally
\[
\inner{\u}{\v} = (-1 + i)\conj{(1 - i)} + 1 \cdot \conj{2} = (-1 + i)(1 + i) + 2 = -2 + 2 = 0 ,
\]
so \( \u \perp \v \), as @thm-self-adjoint-orthogonal-eigenspaces requires. Normalizing, \( \norm{\u}^2 = 2 + 1 = 3 \) and \( \norm{\v}^2 = 2 + 4 = 6 \), so
\[
\Bigl(\tfrac1{\sqrt3}(-1 + i, 1),\ \tfrac1{\sqrt6}(1 - i, 2)\Bigr)
\]
is an orthonormal basis of \( \nC^2 \) consisting of eigenvectors of \( \A \). Section 4 proves that this always happens, for exactly the operators it happens for.
:::

## Invariant complements

Section 5 will prove the real spectral theorem by the move named at the front of the chapter: find one eigenvector, pass to its orthogonal complement, induct. For that to work the complement must be invariant, and the restriction must again be self-adjoint so that the induction can be applied to it. Both hold, and neither needs an eigenvector — the statement is about any invariant subspace.

::: {#thm-self-adjoint-invariant-complement}
[Self-adjointness Passes to Orthogonal Complements]

Let \( T \in \cL(V) \) be self-adjoint and let \( U \subseteq V \) be a \( T \)-invariant subspace. Then:

::: {.enumerate options="label=(\alph*)"}
1. \( U^{\perp} \) is \( T \)-invariant;
2. \( T|_U \in \cL(U) \) and \( T|_{U^{\perp}} \in \cL(U^{\perp}) \) are self-adjoint, for the inner products inherited from \( V \).
:::
:::

::: {.proof}
(a) Since \( T \) is self-adjoint, \( T^{*} = T \), so \( U \) is \( T^{*} \)-invariant. By @lem-adjoint-eigenline-complement, \( U^{\perp} \) is \( T \)-invariant.

(b) \( U \) is \( T \)-invariant, so \( T|_U \) maps \( U \) to \( U \) and is an operator on \( U \). For \( \u_1, \u_2 \in U \),
\[
\inner{T|_U\u_1}{\u_2} = \inner{T\u_1}{\u_2} = \inner{\u_1}{T\u_2} = \inner{\u_1}{T|_U\u_2} ,
\]
where the inner products are those of \( V \), which is what \( U \) inherits. By @def-self-adjoint, \( T|_U \) is self-adjoint. The same three equalities with \( U^{\perp} \) in place of \( U \) give the second claim, using (a) to know that \( T|_{U^{\perp}} \) is an operator on \( U^{\perp} \).
:::

So the pair \( (U, U^{\perp}) \) splits a self-adjoint operator into two self-adjoint operators on smaller spaces, and nothing is lost: \( V = U \oplus U^{\perp} \) by @thm-orthogonal-decomposition (a). Combined with @thm-self-adjoint-has-eigenvalue, which guarantees that a non-zero space always offers an eigenvector to start from, this is a complete induction, and Section 5 will do no more than write it out.

## Two zero tests, and the gap between the fields

An operator carries the function \( \v \mapsto \inner{T\v}{\v} \), sometimes called its quadratic form. How much of \( T \) does that one function remember? The answer depends on the field, and the difference is the sharpest illustration in this book of why \( \nC \) is the easier place to work.

::: {#thm-self-adjoint-zero-test}
[The Zero Test for Self-adjoint Operators]

Let \( V \) be a finite-dimensional inner product space over \( F = \nR \) or \( F = \nC \) and let \( T \in \cL(V) \) be **self-adjoint**. If \( \inner{T\v}{\v} = 0 \) for every \( \v \in V \), then \( T = 0 \).
:::

::: {.idea}
The hypothesis only ever feeds \( T \) one vector, while the conclusion is about \( \inner{T\u}{\w} \) for **two**. So manufacture two out of one: apply the hypothesis to \( \u + \w \) and expand. The diagonal terms die by hypothesis and what is left is a statement about the cross terms, which self-adjointness turns into a statement about \( \inner{T\u}{\w} \) alone.
:::

::: {.proof}
Let \( \u, \w \in V \). Expanding \( \inner{T(\u + \w)}{\u + \w} \) in both slots,
\[
\begin{aligned}
0 &= \inner{T\u}{\u} + \inner{T\u}{\w} + \inner{T\w}{\u} + \inner{T\w}{\w} \\
&= \inner{T\u}{\w} + \inner{T\w}{\u},
\end{aligned}
\]
the two outer terms vanishing by hypothesis. Since \( T \) is self-adjoint, \( \inner{T\w}{\u} = \inner{\w}{T\u} = \conj{\inner{T\u}{\w}} \) by conjugate symmetry. Writing \( z = \inner{T\u}{\w} \), the display says \( z + \conj{z} = 0 \), that is
\[
\operatorname{Re}\inner{T\u}{\w} = 0 \qquad \text{for all } \u, \w \in V . \tag{$\ast$}
\]

If \( F = \nR \) this already says \( \inner{T\u}{\w} = 0 \) for all \( \u, \w \). If \( F = \nC \), apply \( (\ast) \) with \( i\w \) in place of \( \w \): since \( \inner{T\u}{i\w} = \conj{i}\,z = -iz \) and \( \operatorname{Re}(-iz) = \operatorname{Im}(z) \), we also get \( \operatorname{Im}\inner{T\u}{\w} = 0 \). Either way \( \inner{T\u}{\w} = 0 \) for all \( \u, \w \).

Taking \( \w = T\u \) gives \( \norm{T\u}^2 = 0 \), so \( T\u = \0 \) for every \( \u \), that is \( T = 0 \). This proves the theorem.
:::

Now drop the hypothesis. Over \( \nC \) nothing is lost.

::: {#thm-complex-zero-test}
[The Zero Test over the Complex Numbers]

Let \( V \) be a finite-dimensional **complex** inner product space and let \( T \in \cL(V) \) be any operator. If \( \inner{T\v}{\v} = 0 \) for every \( \v \in V \), then \( T = 0 \).
:::

::: {.idea}
The previous proof used self-adjointness in exactly one place: to convert \( \inner{T\w}{\u} \) into \( \conj{\inner{T\u}{\w}} \), which gave the real part only. Without it we must extract the imaginary part some other way, and over \( \nC \) there is another way — substitute \( \u + i\w \) as well as \( \u + \w \), and take a combination of the two identities. There is no third substitution available over \( \nR \), which is precisely why the real statement is false.
:::

::: {.proof}
Let \( \u, \w \in V \). Applying the hypothesis to \( \u + \w \) and expanding as before,
\[
\inner{T\u}{\w} + \inner{T\w}{\u} = 0 . \tag{1}
\]
Applying it to \( \u + i\w \) and using \( \inner{T\u}{i\w} = -i\inner{T\u}{\w} \), \( \inner{T(i\w)}{\u} = i\inner{T\w}{\u} \) and \( \inner{T(i\w)}{i\w} = i\conj{i}\inner{T\w}{\w} = 0 \),
\[
-i\inner{T\u}{\w} + i\inner{T\w}{\u} = 0 .
\]
Multiplying that by \( i \) gives
\[
\inner{T\u}{\w} - \inner{T\w}{\u} = 0 . \tag{2}
\]
Adding (1) and (2), \( 2\inner{T\u}{\w} = 0 \), so \( \inner{T\u}{\w} = 0 \) for all \( \u, \w \). Taking \( \w = T\u \) gives \( \norm{T\u}^2 = 0 \), hence \( T = 0 \).
:::

This statement appeared once already, as @exr-isometries-and-unitary-maps-c2 (b), where it was an exercise in the arithmetic of complex inner products. It is restated and proved here because Section 3 needs to cite it as a theorem: the four characterizations of a normal operator all come from applying it to \( T^{*}T - TT^{*} \). The proof is the same one; what is new is the company it now keeps.

::: {.warning}
**Over \( \nR \), the quadratic form does not determine the operator.** Let \( T \) be the quarter turn of \( \nR^2 \), \( T(x_1, x_2) = (-x_2, x_1) \). Then
\[
\inner{T\x}{\x} = -x_2x_1 + x_1x_2 = 0 \qquad \text{for every } \x \in \nR^2 ,
\]
and yet \( T \ne 0 \). So @thm-complex-zero-test genuinely fails over \( \nR \), and @thm-self-adjoint-zero-test genuinely needs its hypothesis: this \( T \) is not self-adjoint, since \( T^{*} = -T \). The general real statement is that \( \inner{T\v}{\v} = 0 \) for all \( \v \) forces \( T^{*} = -T \) and no more — @exr-self-adjoint-operators-c3.
:::

::: {.check}
Over \( \nC \), suppose \( \inner{T\v}{\v} \) is **real** for every \( \v \in V \). Must \( T \) be self-adjoint?
:::

::: {.solution}
Yes. Put \( S = T - T^{*} \). For every \( \v \), \( \inner{T^{*}\v}{\v} = \inner{\v}{T\v} = \conj{\inner{T\v}{\v}} = \inner{T\v}{\v} \), the last step because the number is real. Hence \( \inner{S\v}{\v} = 0 \) for all \( \v \), and @thm-complex-zero-test gives \( S = 0 \), that is \( T^{*} = T \). Combined with @prp-self-adjoint-immediate (a), this says that over \( \nC \) "self-adjoint" and "\( \inner{T\v}{\v} \) always real" are the same condition. Over \( \nR \) the criterion is useless, since \( \inner{T\v}{\v} \) is automatically real for every operator.
:::

## Exercises

### A. Check your understanding

:::: {#exr-self-adjoint-operators-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State what it means for \( T \in \cL(V) \) to be self-adjoint, in terms of \( T^{*} \) and in terms of inner products, and say what the matrix condition is and in which bases it may be used.
2. True or false: a symmetric matrix in \( M_2(\nC) \) has real eigenvalues. Justify your answer.
3. Which field does @thm-self-adjoint-has-eigenvalue concern, and which earlier theorem supplies the eigenvalue it borrows?
4. True or false: if \( T \) is self-adjoint and \( U \) is any subspace, then \( U^{\perp} \) is \( T \)-invariant. Justify your answer.
5. State the difference between @thm-self-adjoint-zero-test and @thm-complex-zero-test, and give the standard example showing the second has no real analogue.
6. Give a normal operator on \( \nR^2 \) that is not self-adjoint.
:::
::::

::: {.solution}
(a) \( T^{*} = T \); equivalently \( \inner{T\u}{\v} = \inner{\u}{T\v} \) for **all** \( \u, \v \in V \) (@def-self-adjoint). The matrix condition is \( \A^{*} = \A \), and by @thm-matrix-of-adjoint it may be used only in an **orthonormal** basis.

(b) False. \( \B = \begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix} \) is symmetric with eigenvalues \( 1 \pm i \) (@exm-self-adjoint-tests (b) and the warning after it). Over \( \nC \) the relevant condition is \( \A^{*} = \A \), not \( \A\tp = \A \).

(c) The real field: it says a self-adjoint operator on a non-zero **real** inner product space has an eigenvalue. The eigenvalue is borrowed from @thm-complex-operator-has-eigenvalue, applied to the matrix read as a complex matrix on the complexification \( \nC^n \) of \( \nR^n \), and is then shown to be real by @thm-self-adjoint-real-eigenvalues.

(d) False as stated: \( U \) must be **\( T \)-invariant** (@thm-self-adjoint-invariant-complement). For example, \( T = T_{\A} \) on \( \nR^2 \) with \( \A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) is self-adjoint, and \( U = \Span(\e_1) \) has \( U^{\perp} = \Span(\e_2) \) with \( T\e_2 = \e_1 \notin U^{\perp} \). Here \( U \) was not invariant either, since \( T\e_1 = \e_2 \).

(e) @thm-self-adjoint-zero-test holds over \( \nR \) and \( \nC \) but assumes \( T \) self-adjoint; @thm-complex-zero-test drops that assumption but holds only over \( \nC \). The quarter turn \( T(x_1, x_2) = (-x_2, x_1) \) of \( \nR^2 \) satisfies \( \inner{T\x}{\x} = 0 \) for every \( \x \) and is not zero.

(f) The same quarter turn: \( T^{*} = -T \), so \( T^{*}T = TT^{*} = \id \) and \( T \) is normal, while \( T^{*} \ne T \).
:::

### B. Practice

:::: {#exr-self-adjoint-operators-b1}
[B1: Determine which are self-adjoint]

Determine which of the following operators are self-adjoint. Justify your answer; for those that are not, exhibit a pair \( \u, \v \) with \( \inner{T\u}{\v} \ne \inner{\u}{T\v} \), or compute \( T^{*} \).

::: {.enumerate options="label=(\alph*)"}
1. \( T_{\A} \) on \( \nC^2 \), \( \A = \begin{pmatrix} 1 & 2 + i \\ 2 - i & -5 \end{pmatrix} \), standard inner product.
2. \( T_{\B} \) on \( \nC^2 \), \( \B = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} \), standard inner product.
3. \( T_{\C} \) on \( \nR^3 \), \( \C = \begin{pmatrix} 1 & 2 & 0 \\ 2 & 1 & 3 \\ 0 & 3 & 1 \end{pmatrix} \), standard inner product.
4. \( S^{*}S \), for an arbitrary \( S \in \cL(V, W) \) between finite-dimensional inner product spaces.
5. \( P_U - P_{U^{\perp}} \), for a subspace \( U \) of a finite-dimensional \( V \).
6. \( T(x_1, x_2) = (x_2, x_1) \) on \( \nR^2 \) with the standard inner product, whose matrix in the basis \( \sC = ((1, 0), (1, 2)) \) is \( \begin{pmatrix} -\tfrac12 & \tfrac32 \\ \tfrac12 & \tfrac12 \end{pmatrix} \), which is not symmetric.
:::
::::

::: {.solution}
(a) Self-adjoint. The diagonal entries \( 1 \) and \( -5 \) are real and the off-diagonal pair \( 2 + i \), \( 2 - i \) are conjugates, so \( \A^{*} = \A \); the standard basis is orthonormal, so @thm-matrix-of-adjoint applies.

(b) Not self-adjoint. \( \B^{*} = \B\tp = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = -\B \), so \( T_{\B} \) is skew-adjoint. Concretely \( \inner{\B\e_1}{\e_2} = -1 \) while \( \inner{\e_1}{\B\e_2} = 1 \).

(c) Self-adjoint. \( \C \) is real and \( \C\tp = \C \), and the standard basis of \( \nR^3 \) is orthonormal.

(d) Self-adjoint, for every \( S \). By @thm-adjoint-properties (c) and (d), \( (S^{*}S)^{*} = S^{*}S^{**} = S^{*}S \).

(e) Self-adjoint. Each of \( P_U \) and \( P_{U^{\perp}} \) is self-adjoint (@exm-self-adjoint-tests (d)), and by @thm-adjoint-properties (a) and (b) the difference of self-adjoint operators is self-adjoint: \( (P_U - P_{U^{\perp}})^{*} = P_U^{*} - P_{U^{\perp}}^{*} = P_U - P_{U^{\perp}} \).

(f) Self-adjoint, in spite of the non-symmetric matrix. The basis \( \sC \) is **not** orthonormal — \( \inner{(1,0)}{(1,2)} = 1 \ne 0 \) — so @thm-matrix-of-adjoint does not apply to it, and the shape of \( \mtx{T}{\sC}{\sC} \) says nothing either way. Test the definition instead: for \( \x, \y \in \nR^2 \),
\[
\inner{T\x}{\y} = x_2y_1 + x_1y_2 = \inner{\x}{T\y} ,
\]
so \( T^{*} = T \). In the standard basis, which *is* orthonormal, the matrix is \( \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \), symmetric as it must be. The moral is the one Chapter 10, Section 6 closes with: self-adjointness is a property of the operator and the inner product, never of a matrix taken on its own.
:::

:::: {#exr-self-adjoint-operators-b2}
[B2: Eigenvalues and orthogonality]

::: {.enumerate options="label=(\alph*)"}
1. For \( \A = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} \in M_2(\nC) \), check that \( \A \) is Hermitian, find its eigenvalues and an eigenvector for each, and verify that the eigenvectors are orthogonal.
2. For \( \S = \begin{pmatrix} 3 & 1 & 1 \\ 1 & 3 & 1 \\ 1 & 1 & 3 \end{pmatrix} \in M_3(\nR) \), find the eigenvalues with their multiplicities and bases of the eigenspaces, and verify that the two eigenspaces are orthogonal.
3. Hence write down an orthonormal basis of \( \nR^3 \) consisting of eigenvectors of \( \S \).
:::
::::

::: {.solution}
(a) \( \A^{*} = \conj{\A}\tp = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = \A \), so \( \A \) is Hermitian. Then \( \tr\A = 0 \) and \( \det\A = 0 - (-i)(i) = -1 \), so \( p_{\A} = x^2 - 1 \) and the eigenvalues are \( 1 \) and \( -1 \), both real.

\( \A(1, i) = (-i \cdot i,\; i \cdot 1) = (1, i) \), so \( \u = (1, i) \) works for \( \lambda = 1 \). \( \A(1, -i) = (-1,\; i) = -(1, -i) \), so \( \v = (1, -i) \) works for \( \lambda = -1 \). Finally
\[
\inner{\u}{\v} = 1 \cdot \conj{1} + i\,\conj{(-i)} = 1 + i \cdot i = 0 .
\]

(b) Expanding the determinant gives \( p_{\S} = (x - 5)(x - 2)^2 \), so \( \spec(\S) = \{5, 2\} \) with algebraic multiplicities \( 1 \) and \( 2 \). The eigenspaces are read off from \( \S = 2\I + \J \), where \( \J \) is the all-ones matrix: since \( \J(1, 1, 1) = (3, 3, 3) \) and \( \J\x = \0 \) exactly when \( x_1 + x_2 + x_3 = 0 \),
\[
E_5(\S) = \Span\bigl((1, 1, 1)\bigr), \quad E_2(\S) = \Span\bigl((1, -1, 0), (1, 0, -1)\bigr),
\]
of dimensions \( 1 \) and \( 2 \). Orthogonality: \( (1, 1, 1) \cdot (1, -1, 0) = 0 \) and \( (1, 1, 1) \cdot (1, 0, -1) = 0 \), so \( E_5(\S) \perp E_2(\S) \), as @thm-self-adjoint-orthogonal-eigenspaces requires.

(c) The two vectors spanning \( E_2(\S) \) are not orthogonal to each other, so run Gram–Schmidt inside that eigenspace (@thm-gram-schmidt). With \( \w_1 = (1, -1, 0) \),
\[
(1, 0, -1) - \tfrac{1}{2}(1, -1, 0) = \tfrac12(1, 1, -2) .
\]
Normalizing all three vectors gives the orthonormal eigenbasis
\[
\tfrac1{\sqrt3}(1, 1, 1), \quad \tfrac1{\sqrt2}(1, -1, 0), \quad \tfrac1{\sqrt6}(1, 1, -2) .
\]
The eigenvalues are \( 5, 2, 2 \) in that order.
:::

:::: {#exr-self-adjoint-operators-b3}
[B3: A self-adjoint square root of zero]

Let \( T \in \cL(V) \) be self-adjoint with \( T^2 = 0 \). Prove that \( T = 0 \). Deduce that a self-adjoint \( T \) with \( T^k = 0 \) for some \( k \ge 1 \) is zero.
::::

::: {.solution}
For every \( \v \in V \), by @def-self-adjoint,
\[
\norm{T\v}^2 = \inner{T\v}{T\v} = \inner{T^2\v}{\v} = \inner{\0}{\v} = 0 ,
\]
so \( T\v = \0 \). As \( \v \) was arbitrary, \( T = 0 \).

For the deduction, use strong induction on \( k \) (@thm-strong-induction). If \( k = 1 \) there is nothing to prove. Let \( k \ge 2 \) with \( T^k = 0 \), and put \( m = \lceil k/2 \rceil \), so that \( 1 \le m < k \) and \( 2m \ge k \). Then \( (T^m)^2 = T^{2m} = T^{2m-k}T^k = 0 \), and \( T^m \) is self-adjoint, since \( (T^m)^{*} = (T^{*})^m = T^m \) by @thm-adjoint-properties (c). By the first part, \( T^m = 0 \), and the inductive hypothesis applied to the exponent \( m \) gives \( T = 0 \).
:::

### C. Going deeper

:::: {#exr-self-adjoint-operators-c1}
[C1: The operator \( S^{*}S \)]

Let \( S \in \cL(V, W) \) between finite-dimensional inner product spaces over \( F \), and set \( T = S^{*}S \in \cL(V) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( T \) is self-adjoint and that \( \inner{T\v}{\v} \ge 0 \) for every \( \v \in V \), with equality if and only if \( S\v = \0 \).
2. Deduce that every eigenvalue of \( T \) is a non-negative real number.
3. Prove that \( T \) is invertible if and only if \( S \) is injective.
:::

*Hint for (a): the quantity \( \inner{T\v}{\v} \) is a norm squared in disguise.*
::::

::: {.solution}
(a) \( T^{*} = (S^{*}S)^{*} = S^{*}S^{**} = S^{*}S = T \), by @thm-adjoint-properties (c) and (d). For the second claim, use conjugate symmetry and then @def-adjoint:
\[
\inner{T\v}{\v} = \conj{\inner{\v}{S^{*}S\v}} = \conj{\inner{S\v}{S\v}} = \norm{S\v}^2 ,
\]
the last step because a norm squared is a non-negative real number and is its own conjugate. So \( \inner{T\v}{\v} \ge 0 \), with equality exactly when \( \norm{S\v} = 0 \), that is \( S\v = \0 \) (@def-inner-product).

(b) Let \( T\v = \lambda\v \) with \( \v \ne \0 \). By @thm-self-adjoint-real-eigenvalues, \( \lambda \in \nR \). By (a), \( 0 \le \inner{T\v}{\v} = \lambda\norm{\v}^2 \), and \( \norm{\v}^2 > 0 \), so \( \lambda \ge 0 \).

(c) \( (\Rightarrow) \) If \( S\v = \0 \) then \( T\v = \0 \), so injectivity of \( T \) forces \( \v = \0 \); and an invertible operator is injective. \( (\Leftarrow) \) If \( S \) is injective and \( T\v = \0 \), then by (a) \( \norm{S\v}^2 = \inner{T\v}{\v} = 0 \), so \( S\v = \0 \) and \( \v = \0 \). Thus \( \ker T = \{\0\} \), so \( T \) is injective, hence bijective by @cor-rank-nullity-consequences (e). This is @cor-rank-adjoint (b) again, seen from the quadratic form.

Operators with the property in (a) are called **positive**, and they are the subject of Chapter 12; part (b) is the first half of the characterization proved there.
:::

:::: {#exr-self-adjoint-operators-c2}
[C2: Sums and products]

Let \( S, T \in \cL(V) \) be self-adjoint.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( S + T \) and \( cT \) are self-adjoint for every **real** scalar \( c \), and show by example that \( cT \) need not be self-adjoint for \( c \in \nC \).
2. Prove that \( ST \) is self-adjoint if and only if \( ST = TS \).
3. Give self-adjoint \( S, T \in \cL(\nC^2) \) with \( ST \) not self-adjoint.
:::
::::

::: {.solution}
(a) By @thm-adjoint-properties (a), \( (S + T)^{*} = S^{*} + T^{*} = S + T \). By (b) of the same theorem, \( (cT)^{*} = \conj{c}\,T^{*} = \conj{c}\,T \), which equals \( cT \) exactly when \( \conj{c} = c \) or \( T = 0 \). For a complex counterexample take \( T = \id \) on \( \nC^2 \) and \( c = i \): then \( (i\,\id)^{*} = -i\,\id \ne i\,\id \).

(b) By @thm-adjoint-properties (c), \( (ST)^{*} = T^{*}S^{*} = TS \). So \( (ST)^{*} = ST \) if and only if \( TS = ST \).

(c) Take \( S = T_{\A} \) and \( T = T_{\B} \) on \( \nC^2 \) with
\[
\A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \qquad \B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} .
\]
Both are Hermitian. But \( \A\B = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) and \( \B\A = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \), which differ, so by (b) the product is not self-adjoint. Indeed \( (\A\B)^{*} = \B\A \ne \A\B \).
:::

:::: {#exr-self-adjoint-operators-c3}
[C3: What the real quadratic form does determine]

Let \( V \) be a finite-dimensional inner product space over \( \nR \) and \( T \in \cL(V) \). Call \( T \) **skew-adjoint** if \( T^{*} = -T \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \inner{T\v}{\v} = 0 \) for every \( \v \in V \) if and only if \( T \) is skew-adjoint.
2. Deduce that every \( T \in \cL(V) \) can be written uniquely as \( T = A + B \) with \( A \) self-adjoint and \( B \) skew-adjoint, and that \( \inner{T\v}{\v} = \inner{A\v}{\v} \) for every \( \v \).
3. Conclude that over \( \nR \) the function \( \v \mapsto \inner{T\v}{\v} \) determines \( A \) and nothing about \( B \). Contrast this with the complex case.
:::
::::

::: {.solution}
(a) \( (\Leftarrow) \) If \( T^{*} = -T \), then for every \( \v \), \( \inner{T\v}{\v} = \inner{\v}{T^{*}\v} = -\inner{\v}{T\v} = -\inner{T\v}{\v} \), the last step by symmetry of a real inner product. A real number equal to its own negative is \( 0 \).

\( (\Rightarrow) \) Suppose \( \inner{T\v}{\v} = 0 \) for all \( \v \). Expanding \( \inner{T(\u + \w)}{\u + \w} = 0 \) and canceling the two diagonal terms,
\[
\inner{T\u}{\w} + \inner{T\w}{\u} = 0 .
\]
Over \( \nR \), \( \inner{T\w}{\u} = \inner{\u}{T\w} \), so \( \inner{T\u}{\w} = \inner{\u}{-T\w} \) for all \( \u, \w \). By the uniqueness in @thm-adjoint-exists, \( T^{*} = -T \).

(b) Put \( A = \tfrac12(T + T^{*}) \) and \( B = \tfrac12(T - T^{*}) \). Then \( A + B = T \), and by @thm-adjoint-properties (a), (b) and (d), \( A^{*} = A \) and \( B^{*} = -B \). For uniqueness, if \( T = A' + B' \) is another such splitting, then \( T^{*} = A' - B' \), so \( A' = \tfrac12(T + T^{*}) = A \) and \( B' = B \). Finally \( \inner{B\v}{\v} = 0 \) for every \( \v \) by (a), so \( \inner{T\v}{\v} = \inner{A\v}{\v} + \inner{B\v}{\v} = \inner{A\v}{\v} \).

(c) By (b), two operators \( T \) and \( T' \) with the same self-adjoint part have the same quadratic form; and conversely, if \( \inner{T\v}{\v} = \inner{T'\v}{\v} \) for all \( \v \), then \( A - A' \) is self-adjoint with vanishing quadratic form, so \( A = A' \) by @thm-self-adjoint-zero-test. So the quadratic form sees exactly \( A \). The skew part is invisible: the quarter turn of \( \nR^2 \) is skew-adjoint, and adding it to any \( T \) changes nothing. Over \( \nC \), by contrast, @thm-complex-zero-test says the quadratic form determines \( T \) completely — there is no invisible part at all, which is why the complex theory is the easier one.
:::
