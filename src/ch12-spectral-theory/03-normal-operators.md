# Normal Operators

Section 2 collected everything a self-adjoint operator gives us: real eigenvalues, orthogonal eigenspaces, an invariant orthogonal complement. That is exactly the equipment an orthonormal basis of eigenvectors needs. But over \( \nC \) the hypothesis is too heavy, and this section finds the lighter one that still carries the load. It is a condition already met in Chapter 11, and the rest of the chapter runs on it.

As throughout, \( F \) is \( \nR \) or \( \nC \), inner products are linear in the first slot, and every inner product space is finite-dimensional unless we say otherwise.

## The hypothesis that self-adjointness overshoots

Take the operator on \( \nC^2 \) whose matrix in the standard basis is \( \D = \diag(1, i) \). The standard basis is orthonormal and consists of eigenvectors of \( \D \), so this operator has everything the spectral theorem promises. Yet it is not self-adjoint: one of its eigenvalues is \( i \), and a self-adjoint operator has only real eigenvalues (@thm-self-adjoint-real-eigenvalues). So over \( \nC \) self-adjointness cannot be the condition we are looking for. It is sufficient and not necessary, and we are throwing away every operator with a non-real eigenvalue — including every unitary operator other than the trivial ones.

What survives? Compare the two computations. For a self-adjoint \( T \) we have \( T^{*}T = TT = TT^{*} \). For \( \D = \diag(1, i) \) we have \( \D^{*} = \diag(1, -i) \), which is a different matrix, but
\[
\D^{*}\D = \diag(1, 1) = \D\D^{*} .
\]
Neither operator equals its adjoint; both **commute** with their adjoints. That is the common feature, and Chapter 11 already gave it a name.

*A normal operator is one that never gets in its adjoint's way: the two may be applied in either order.*

Recall @def-normal-operator: an operator \( T \in \cL(V) \) is **normal** when \( T^{*}T = TT^{*} \). That is a single equation between two operators, with no vectors and no quantifiers in it, and it is strictly weaker than \( T^{*} = T \). Section 6 of Chapter 11 checked the definition on self-adjoint operators, on unitary ones, on \( i\I \) and on diagonal matrices, and found the \( 2 \times 2 \) Jordan block \( \J_2(0) \) failing it. We take those for granted and go one step further: normality is best understood as a statement about **lengths**, and that is the content of the first theorem below.

Before it, a wider catalog, since the class is larger than Chapter 11's four examples suggest.

::: {#exm-normal-catalog}
[Which of these are normal?]

Decide which of the following matrices are normal, with the standard inner product on \( \nC^n \) or \( \nR^n \). For those that are, say which familiar family they belong to.

::: {.enumerate options="label=(\alph*)"}
1. \( \A = \begin{pmatrix} 2 & 1 + i \\ 1 - i & 3 \end{pmatrix} \) over \( \nC \).
2. \( \B = \begin{pmatrix} 0 & 2 \\ -2 & 0 \end{pmatrix} \) over \( \nR \).
3. \( \U = \tfrac1{\sqrt2}\begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix} \) over \( \nC \).
4. \( \C = \begin{pmatrix} 1 & 2 & 3 \\ 3 & 1 & 2 \\ 2 & 3 & 1 \end{pmatrix} \) over \( \nC \).
5. \( \M = \begin{pmatrix} 2 & 1 \\ -1 & 2 \end{pmatrix} \) over \( \nR \).
6. \( \N = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix} \) over \( \nR \).
:::
:::

::: {.solution}
(a) Normal. \( \A^{*} = \A \), since transposing swaps the off-diagonal entries and conjugating swaps them back, so \( \A \) is Hermitian and both products equal \( \A^2 \). Every **self-adjoint** operator is normal.

(b) Normal. \( \B\tp = -\B \), so \( \B\tp\B = -\B^2 = \B\B\tp \). An operator with \( T^{*} = -T \) is called **skew-adjoint**, and the same one-line computation makes every such operator normal.

(c) Normal. \( \U^{*}\U = \tfrac12\begin{pmatrix} 1 & -i \\ -i & 1 \end{pmatrix}\begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix} = \tfrac12\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = \I \), so \( \U \) is **unitary** (@def-unitary-orthogonal), and then \( \U^{*}\U = \I = \U\U^{*} \).

(d) Normal. Each row of \( \C \) is the previous one shifted cyclically to the right; such a matrix is called a **circulant**. Writing out the products,
\[
\C\tp\C = \C\C\tp = \begin{pmatrix} 14 & 11 & 11 \\ 11 & 14 & 11 \\ 11 & 11 & 14 \end{pmatrix} .
\]
Both entries in position \( (i, j) \) are the dot product of two rows of \( \C \), or of two columns, and cyclic shifting makes those two lists of dot products agree. Section 9 explains circulants properly and diagonalizes all of them at once.

(e) Normal, and in none of the families above: \( \M\tp \neq \pm\M \) and \( \M\tp\M = 5\I \neq \I \). Still,
\[
\M\tp\M = \M\M\tp = \begin{pmatrix} 5 & 0 \\ 0 & 5 \end{pmatrix} .
\]
This is \( \sqrt5 \) times a rotation of the plane, which is the rotation-scaling block \( \vLambda(2 + i) \) transposed (@def-real-jordan-block). Normality is genuinely wider than "self-adjoint or unitary".

(f) **Not** normal:
\[
\N\tp\N = \begin{pmatrix} 1 & 1 \\ 1 & 5 \end{pmatrix},
\qquad
\N\N\tp = \begin{pmatrix} 2 & 2 \\ 2 & 4 \end{pmatrix} .
\]
The \( (1,1) \) entries already disagree, \( 1 \neq 2 \). This matrix is diagonalizable, with eigenvalues \( 1 \) and \( 2 \); Section 4 shows what it costs to be diagonalizable and not normal.
:::

## Normality is a statement about lengths

The definition compares two operators. The next theorem turns it into a comparison of two numbers, one vector at a time, and that is the form every later proof uses. The engine is the zero test of Section 2: a self-adjoint operator \( S \) with \( \inner{S\v}{\v} = 0 \) for all \( \v \) is zero.

::: {#thm-normal-characterizations}
[Characterizations of Normality]

Let \( V \) be a finite-dimensional inner product space over \( F \) and let \( T \in \cL(V) \). The following are equivalent.

::: {.enumerate options="label=(\alph*)"}
1. \( T \) is normal.
2. \( \norm{T\v} = \norm{T^{*}\v} \) for every \( \v \in V \).
3. \( \inner{T\u}{T\v} = \inner{T^{*}\u}{T^{*}\v} \) for all \( \u, \v \in V \).
:::

Suppose in addition that \( F = \nC \), and set
\[
A = \tfrac12(T + T^{*}), \qquad B = \tfrac1{2i}(T - T^{*}),
\]
so that \( A \) and \( B \) are self-adjoint and \( T = A + iB \). Then (a)–(c) are further equivalent to

::: {.enumerate options="label=(\alph*)"}
4. \( AB = BA \).
:::
:::

::: {.idea}
Condition (a) says that the operator \( S = T^{*}T - TT^{*} \) is zero. That operator is self-adjoint, so by the zero test of @thm-self-adjoint-zero-test it is enough to know \( \inner{S\v}{\v} = 0 \) for every \( \v \) — and \( \inner{S\v}{\v} \) is exactly \( \norm{T\v}^2 - \norm{T^{*}\v}^2 \). So (a) and (b) are the same statement read at two different levels of resolution. Condition (c) is (b) with the two slots unglued, and it costs nothing in one direction and a specialization in the other. Condition (d) is the operator version of writing a complex number as \( a + bi \); that decomposition appeared in @exr-adjoints-c2 (c), and multiplying out \( TT^{*} - T^{*}T \) in terms of \( A \) and \( B \) leaves only the commutator.
:::

::: {.proof}
(a) \( \Rightarrow \) (c). For all \( \u, \v \in V \), by @def-adjoint and \( T^{**} = T \) (@thm-adjoint-properties (d)),
\[
\inner{T\u}{T\v} = \inner{T^{*}T\u}{\v},
\qquad
\inner{T^{*}\u}{T^{*}\v} = \inner{TT^{*}\u}{\v} .
\]
Since \( T^{*}T = TT^{*} \), the two right-hand sides agree.

(c) \( \Rightarrow \) (b). Take \( \u = \v \). Then \( \norm{T\v}^2 = \norm{T^{*}\v}^2 \), and both norms are non-negative reals, so they are equal.

(b) \( \Rightarrow \) (a). Put \( S = T^{*}T - TT^{*} \). Then \( S \) is self-adjoint: by @thm-adjoint-properties (a), (c) and (d),
\[
S^{*} = (T^{*}T)^{*} - (TT^{*})^{*} = T^{*}T^{**} - T^{**}T^{*} = T^{*}T - TT^{*} = S .
\]
For any \( \v \in V \), using @def-adjoint twice,
\[
\begin{aligned}
\inner{S\v}{\v}
&= \inner{T^{*}T\v}{\v} - \inner{TT^{*}\v}{\v} \\
&= \inner{T\v}{T\v} - \inner{T^{*}\v}{T^{*}\v} \\
&= \norm{T\v}^2 - \norm{T^{*}\v}^2 = 0
\end{aligned}
\]
by (b). Since \( S \) is self-adjoint, @thm-self-adjoint-zero-test gives \( S = 0 \), that is \( T^{*}T = TT^{*} \).

Now let \( F = \nC \). By @thm-adjoint-properties (a), (b) and (d),
\[
\begin{aligned}
A^{*} &= \tfrac12(T^{*} + T) = A, \\
B^{*} &= \conj{\Bigl(\tfrac1{2i}\Bigr)}(T^{*} - T)
= \tfrac1{2i}(T - T^{*}) = B,
\end{aligned}
\]
so both are self-adjoint, and \( A + iB = \tfrac12(T + T^{*}) + \tfrac12(T - T^{*}) = T \); this is the decomposition of @exr-adjoints-c2 (c). Expanding \( T = A + iB \) and \( T^{*} = A - iB \),
\[
\begin{aligned}
TT^{*} &= (A + iB)(A - iB) = A^2 + B^2 + i(BA - AB), \\
T^{*}T &= (A - iB)(A + iB) = A^2 + B^2 + i(AB - BA) .
\end{aligned}
\]
Subtracting, \( TT^{*} - T^{*}T = 2i(BA - AB) \). So \( T \) is normal exactly when \( AB = BA \), which is (a) \( \Leftrightarrow \) (d). This proves the theorem.
:::

Condition (b) is the one to remember. It says that \( T \) and \( T^{*} \) stretch every single vector by the same amount, even though they need not move it in the same direction. Everything in the next three sections is squeezed out of that sentence. Condition (d) records that normality over \( \nC \) is the operator analogue of the fact that any two real numbers commute: split \( T \) into a "real part" and an "imaginary part", and normality is precisely the failure of those two parts to interfere.

::: {.check}
The symmetric matrix \( \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) and the skew-symmetric matrix \( \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} \) are both normal, the first being self-adjoint and the second skew-adjoint. Is their sum normal?
:::

::: {.solution}
No. The sum is \( \begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix} = 2\J_2(0) \), which is twice the standard non-normal example: it kills \( \e_1 \) and sends \( \e_2 \) to a vector of length \( 2 \), while its transpose does the opposite, so condition (b) fails at \( \v = \e_1 \). The normal operators do not form a subspace of \( \cL(V) \), and they are not closed under composition either.
:::

## What normality buys

Four consequences, all short, all obtained by turning some statement about \( T \) into the same statement about \( T^{*} \).

::: {#cor-normal-kernel}
[Kernel, Image and an Orthogonal Splitting]

Let \( T \in \cL(V) \) be normal on a finite-dimensional inner product space \( V \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \ker T = \ker T^{*} \);
2. \( \im T = \im T^{*} \);
3. \( V = \ker T \oplus \im T \), and the two summands are orthogonal to each other.
:::
:::

::: {.proof}
(a) For \( \v \in V \), @thm-normal-characterizations (b) gives \( \norm{T\v} = \norm{T^{*}\v} \). So \( T\v = \0 \) if and only if \( \norm{T\v} = 0 \), if and only if \( \norm{T^{*}\v} = 0 \), if and only if \( T^{*}\v = \0 \).

(b) By @thm-four-subspaces-orthogonal (b) applied to \( T^{*} \) in place of \( T \), and using \( T^{**} = T \) (@thm-adjoint-properties (d)),
\[
\im T = \im T^{**} = (\ker T^{*})^{\perp} = (\ker T)^{\perp} = \im T^{*},
\]
where the third equality is (a) and the fourth is @thm-four-subspaces-orthogonal (b) for \( T \).

(c) By (b), \( \im T = (\ker T)^{\perp} \), and \( V = \ker T \oplus (\ker T)^{\perp} \) by @thm-orthogonal-decomposition (a). Orthogonality of the summands is the definition of the orthogonal complement.
:::

Part (c) fails badly without normality, and the failure is not subtle: for a general operator \( \ker T \) and \( \im T \) can be **equal**. Take \( T \) with matrix \( \J_2(0) = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) on \( \nC^2 \). Then \( T\e_1 = \0 \) and \( T\e_2 = \e_1 \), so
\[
\ker T = \Span(\e_1) = \im T .
\]
The sum \( \ker T + \im T \) is one-dimensional, so it is neither direct nor all of \( \nC^2 \). Normality is exactly what rules this out.

::: {#thm-normal-eigenvector-shared}
[An Eigenvector of a Normal Operator Is an Eigenvector of Its Adjoint]

Let \( T \in \cL(V) \) be normal, let \( \lambda \in F \) and let \( \v \in V \). Then
\[
T\v = \lambda\v
\quad \text{if and only if} \quad
T^{*}\v = \conj{\lambda}\,\v .
\]
In particular \( E_{\lambda}(T) = E_{\conj{\lambda}}(T^{*}) \), and \( \lambda \in \spec(T) \) if and only if \( \conj{\lambda} \in \spec(T^{*}) \).
:::

::: {.idea}
Both sides say that \( \v \) lies in a kernel: the left in \( \ker(T - \lambda\,\id_V) \), the right in \( \ker(T^{*} - \conj{\lambda}\,\id_V) \). Those two operators are adjoint to each other, so @cor-normal-kernel (a) closes the gap — provided \( T - \lambda\,\id_V \) is itself normal, which is the only thing to check.
:::

::: {.proof}
Write \( S = T - \lambda\,\id_V \). By @thm-adjoint-properties (a), (b) and (d), \( S^{*} = T^{*} - \conj{\lambda}\,\id_V \). Since \( T^{*}T = TT^{*} \) and \( \id_V \) commutes with everything,
\[
\begin{aligned}
S^{*}S &= T^{*}T - \conj{\lambda}T - \lambda T^{*} + \lvert\lambda\rvert^2\,\id_V \\
&= TT^{*} - \lambda T^{*} - \conj{\lambda}T + \lvert\lambda\rvert^2\,\id_V = SS^{*} ,
\end{aligned}
\]
so \( S \) is normal. By @cor-normal-kernel (a), \( \ker S = \ker S^{*} \). Now \( T\v = \lambda\v \) says \( \v \in \ker S \), and \( T^{*}\v = \conj{\lambda}\v \) says \( \v \in \ker S^{*} \), so the two conditions agree. The statement about eigenspaces is the equality \( \ker S = \ker S^{*} \) rewritten, and the statement about spectra follows because an eigenspace is non-zero exactly when the scalar is an eigenvalue (@thm-eigenvalue-characterizations).
:::

The theorem is the reason normal operators are so easy to handle: \( T \) and \( T^{*} \) have the *same* eigenvectors, with conjugate eigenvalues. The proof of the next corollary is the classical self-adjoint argument (@thm-self-adjoint-orthogonal-eigenspaces) with one conjugate bar inserted, and that bar is exactly what @thm-normal-eigenvector-shared supplies.

::: {#cor-normal-orthogonal-eigenspaces}
[Eigenvectors for Distinct Eigenvalues Are Orthogonal]

Let \( T \in \cL(V) \) be normal, let \( \lambda \neq \mu \) be eigenvalues of \( T \), and let \( T\u = \lambda\u \) and \( T\v = \mu\v \). Then \( \inner{\u}{\v} = 0 \). Hence \( E_{\lambda}(T) \perp E_{\mu}(T) \) whenever \( \lambda \neq \mu \).
:::

::: {.proof}
Compute \( \inner{T\u}{\v} \) in two ways. First, \( \inner{T\u}{\v} = \inner{\lambda\u}{\v} = \lambda\inner{\u}{\v} \). Second, by @def-adjoint and then @thm-normal-eigenvector-shared applied to \( \v \),
\[
\inner{T\u}{\v} = \inner{\u}{T^{*}\v} = \inner{\u}{\conj{\mu}\,\v} = \mu\inner{\u}{\v},
\]
the last step because a scalar leaves the second slot conjugated. Subtracting, \( (\lambda - \mu)\inner{\u}{\v} = 0 \), and \( \lambda - \mu \neq 0 \), so \( \inner{\u}{\v} = 0 \). Every vector of \( E_{\lambda}(T) \) is orthogonal to every vector of \( E_{\mu}(T) \) by the same computation.
:::

::: {#thm-normal-powers}
[A Normal Operator Has No Hidden Kernel]

Let \( T \in \cL(V) \) be normal. Then \( \ker T^{k} = \ker T \) for every integer \( k \ge 1 \). In particular, if \( T^{k} = 0 \) for some \( k \ge 1 \) — that is, if \( T \) is **nilpotent** (@def-nilpotent) — then \( T = 0 \).
:::

::: {.idea}
The inclusion \( \ker T \subseteq \ker T^2 \) is free, and the whole content is the reverse one. If \( T^2\v = \0 \), then the vector \( \w = T\v \) lies in \( \ker T \), hence also in \( \ker T^{*} \) by @cor-normal-kernel; and a vector that is killed by \( T^{*} \) and is itself in the image of \( T \) must be \( \0 \), because pairing it with itself moves \( T \) across the inner product and hits the \( T^{*} \).
:::

::: {.proof}
First take \( k = 2 \). The inclusion \( \ker T \subseteq \ker T^2 \) holds for every operator. Conversely, suppose \( T^2\v = \0 \) and put \( \w = T\v \). Then \( T\w = \0 \), so \( T^{*}\w = \0 \) by @cor-normal-kernel (a). Therefore, by @def-adjoint,
\[
\begin{aligned}
\norm{\w}^2 &= \inner{\w}{\w} = \inner{T\v}{\w} \\
&= \inner{\v}{T^{*}\w} = \inner{\v}{\0} = 0 ,
\end{aligned}
\]
so \( \w = T\v = \0 \) and \( \v \in \ker T \). Hence \( \ker T^2 = \ker T \).

Now induct on \( k \). The cases \( k = 1, 2 \) are done. Let \( k \ge 2 \) and assume \( \ker T^{k} = \ker T \). If \( T^{k+1}\v = \0 \), then \( T^{2}\bigl(T^{k-1}\v\bigr) = \0 \), so \( T^{k}\v = T\bigl(T^{k-1}\v\bigr) = \0 \) by the case \( k = 2 \), and then \( T\v = \0 \) by the inductive hypothesis. So \( \ker T^{k+1} \subseteq \ker T \), and the reverse inclusion is again free.

Finally, if \( T^{k} = 0 \) for some \( k \ge 1 \), then \( \ker T = \ker T^{k} = V \), so \( T = 0 \).
:::

This is the sentence that explains why normal operators never produce Jordan blocks. Over \( \nC \), a Jordan block of size \( m \ge 2 \) for the eigenvalue \( \lambda \) contributes a vector killed by \( (T - \lambda\,\id_V)^{m} \) but not by \( T - \lambda\,\id_V \) (@def-jordan-chain). For a normal \( T \) the operator \( T - \lambda\,\id_V \) is normal, as the proof of @thm-normal-eigenvector-shared showed, so @thm-normal-powers forbids such a vector. Every block in the Jordan form of a normal operator therefore has size \( 1 \), and a normal operator on a complex space is diagonalizable (@thm-jordan-canonical-form, @def-diagonalizable).

::: {.remark}
That is diagonalizable, not yet **orthogonally** diagonalizable. The eigenspaces of distinct eigenvalues are already mutually orthogonal by @cor-normal-orthogonal-eigenspaces, so all that is missing is an orthonormal basis inside each eigenspace, which Gram–Schmidt supplies (@thm-gram-schmidt). Section 4 proves the whole statement in one stroke instead, from Schur's theorem, because that proof also delivers the converse and works without Chapter 10.
:::

Two converses are worth flagging now, so that you know they are coming and do not try to prove them here. A normal operator whose eigenvalues are all real is self-adjoint, and a normal operator whose eigenvalues all have modulus \( 1 \) is unitary. Both are false without normality, and neither can be reached with the tools of this section: they need an orthonormal basis of eigenvectors, which is the business of Section 4.

Before the warning, one structural fact deserves to be stated where later sections can lean on it. It is the reason a normal operator can be taken apart orthogonally at all.

::: {#prp-normal-invariant-reducing}
[An Invariant Subspace of a Normal Operator Is Reducing]

Let \( T \in \cL(V) \) be normal on a finite-dimensional inner product space, and let \( U \subseteq V \) be \( T \)-invariant. Then \( U \) is \( T^{*} \)-invariant, \( U^{\perp} \) is \( T \)-invariant, and \( T|_U \) is a normal operator on \( U \).
:::

::: {.idea}
Write the matrix in an orthonormal basis adapted to \( U \). Invariance kills the block below the diagonal, and normality, read on the top-left block alone, kills the block above it. The trace is what converts "these two blocks agree" into "that block is zero".
:::

::: {.proof}
Choose an orthonormal basis \( \sB_U = (\e_1, \dots, \e_r) \) of \( U \) and extend it to an orthonormal basis \( \sB \) of \( V \) (@cor-extend-orthonormal-basis). Since \( T\e_j \in U \) for \( j \le r \), the first \( r \) columns of \( \A = \mtx{T}{\sB}{\sB} \) have zeros below row \( r \), so
\[
\A = \begin{pmatrix} \B & \C \\ \0 & \D \end{pmatrix},
\]
with \( \B \) of size \( r \times r \). Because \( \sB \) is orthonormal, \( \mtx{T^{*}}{\sB}{\sB} = \A^{*} \) (@thm-matrix-of-adjoint), and \( T \) normal means \( \A^{*}\A = \A\A^{*} \). Comparing the \( (1,1) \) blocks (@thm-block-multiplication),
\[
(\A^{*}\A)_{11} = \B^{*}\B, \qquad (\A\A^{*})_{11} = \B\B^{*} + \C\C^{*} .
\]
Taking traces and using \( \tr(\B^{*}\B) = \tr(\B\B^{*}) \) (@thm-trace-properties (3)) gives \( \tr(\C\C^{*}) = 0 \). But \( \tr(\C\C^{*}) = \sum_{i,j}\lvert c_{ij}\rvert^2 \), a sum of non-negative reals, so \( \C = \0 \).

Hence \( \A = \B \oplus \D \). Reading the last \( n - r \) columns, \( T\e_j \in U^{\perp} \) for \( j > r \), so \( U^{\perp} \) is \( T \)-invariant; reading the first \( r \) columns of \( \A^{*} \), \( U \) is \( T^{*} \)-invariant. Finally \( \mtx{T|_U}{\sB_U}{\sB_U} = \B \) and the \( (1,1) \) blocks above now read \( \B^{*}\B = \B\B^{*} \), so \( T|_U \) is normal. This shows all three claims.
:::

::: {.warning}
**Normality cannot be read off a corner.** A principal submatrix of a normal matrix need not be normal. The \( 3 \times 3 \) cyclic shift
\[
\S = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}
\]
is a permutation matrix, hence orthogonal (@exr-isometries-and-unitary-maps-b3), hence normal; but deleting its last row and column leaves \( \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \), the transpose of \( \J_2(0) \), which is not normal. Equivalently: the operator that \( \S \) compresses to \( \Span(\e_1, \e_2) \) is not normal, because that subspace is not \( \S \)-invariant. What **is** true is that an invariant subspace of a normal operator is automatically invariant under the adjoint too, and the restriction there is normal; that is @prp-normal-invariant-reducing, proved just above.
:::

## Exercises

### A. Check your understanding

::: {#exr-normal-operators-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the definition of a normal operator, and state one equivalent condition phrased in terms of norms.
2. True or false: every self-adjoint operator is normal, and every normal operator is self-adjoint. Justify both halves.
3. Let \( T \) be normal with \( T\v = 3\v \). What is \( T^{*}\v \)? What if \( T\v = 3i\v \)?
4. Give a normal operator on \( \nR^2 \) that is neither self-adjoint nor unitary.
5. True or false: if \( S \) and \( T \) are normal then \( S + T \) is normal. Justify your answer.
6. Explain in one sentence why a normal operator cannot be nilpotent unless it is zero.
:::
:::

::: {.solution}
(a) \( T \) is normal when \( T^{*}T = TT^{*} \) (@def-normal-operator). Equivalently, \( \norm{T\v} = \norm{T^{*}\v} \) for every \( \v \in V \) (@thm-normal-characterizations (b)).

(b) The first half is true: if \( T^{*} = T \) then both products are \( T^2 \). The second half is false: \( \diag(1, i) \) on \( \nC^2 \) is normal and has a non-real eigenvalue, so it is not self-adjoint (@thm-self-adjoint-real-eigenvalues).

(c) \( T^{*}\v = 3\v \) in the first case and \( T^{*}\v = -3i\v \) in the second, by @thm-normal-eigenvector-shared: the adjoint has the conjugate eigenvalue on the same eigenvector.

(d) \( \begin{pmatrix} 2 & 1 \\ -1 & 2 \end{pmatrix} \) works (@exm-normal-catalog (e)): it is not symmetric, and \( \M\tp\M = 5\I \neq \I \). Any \( \vLambda(\lambda) \) with \( \lvert\lambda\rvert \neq 1 \) and \( \operatorname{Im}\lambda \neq 0 \) does.

(e) False. \( \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} + \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix} \) is a sum of two normal matrices and is not normal.

(f) If \( T^{k} = 0 \) then \( \ker T = \ker T^{k} = V \) by @thm-normal-powers, so \( T = 0 \).
:::

### B. Practice

::: {#exr-normal-operators-b1}
[B1: Determine which are normal]

Determine which of the following matrices are normal, with the standard inner product. Justify your answer; for those that are not, exhibit a vector \( \v \) with \( \norm{\A\v} \neq \norm{\A^{*}\v} \).

::: {.enumerate options="label=(\alph*)"}
1. \( \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \) over \( \nR \).
2. \( \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) over \( \nR \).
3. \( \begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix} \) over \( \nC \).
4. \( \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix} \) over \( \nR \).
5. \( \begin{pmatrix} i & 1 \\ 0 & i \end{pmatrix} \) over \( \nC \).
:::
:::

::: {.solution}
(a) Normal: the matrix is symmetric, so it is self-adjoint over \( \nR \), and self-adjoint implies normal.

(b) Not normal. \( \A\tp\A = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} \) and \( \A\A\tp = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \). With \( \v = \e_1 \), \( \norm{\A\e_1} = \norm{(1,0)} = 1 \) while \( \norm{\A\tp\e_1} = \norm{(1,1)} = \sqrt2 \).

(c) Normal. \( \A^{*} = \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix} = -\A \), so \( \A \) is skew-adjoint and \( \A^{*}\A = -\A^2 = \A\A^{*} \). (Concretely both products are \( \I \).)

(d) Normal: the matrix is \( (1) \oplus \vLambda(i) \), a direct sum of a \( 1 \times 1 \) block and a rotation by a quarter turn, and its columns are orthonormal, so it is orthogonal (@thm-isometry-characterizations (f)).

(e) Not normal. \( \A^{*}\A = \begin{pmatrix} 1 & -i \\ i & 2 \end{pmatrix} \) and \( \A\A^{*} = \begin{pmatrix} 2 & -i \\ i & 1 \end{pmatrix} \); with \( \v = \e_1 \) we get \( \norm{\A\e_1} = \lvert i\rvert = 1 \) and \( \norm{\A^{*}\e_1} = \norm{(-i, 1)} = \sqrt2 \). Adding \( i\I \) to a non-normal matrix does not repair it: \( \A = i\I + \J_2(0) \) and \( i\I \) is normal, but sums of normal matrices need not be normal.
:::

::: {#exr-normal-operators-b2}
[B2: The splitting of a singular normal operator]

Let \( \C = \begin{pmatrix} 1 & -1 & 0 \\ 0 & 1 & -1 \\ -1 & 0 & 1 \end{pmatrix} \in M_3(\nR) \), and let \( T = T_{\C} \) be the operator it defines on \( \nR^3 \).

::: {.enumerate options="label=(\alph*)"}
1. Verify that \( T \) is normal.
2. Compute \( \ker T \) and \( \ker T^{*} \) and check that they agree.
3. Compute \( \im T \), and verify directly that \( \nR^3 = \ker T \oplus \im T \) with the two summands orthogonal, as @cor-normal-kernel (c) predicts.
:::
:::

::: {.solution}
(a) Each row of \( \C \) is the previous one shifted cyclically, so \( \C \) is a circulant. Explicitly,
\[
\C\tp\C = \C\C\tp = \begin{pmatrix} 2 & -1 & -1 \\ -1 & 2 & -1 \\ -1 & -1 & 2 \end{pmatrix},
\]
so \( T \) is normal.

(b) \( \C\x = \0 \) reads \( x_1 = x_2 = x_3 \), because the first two rows give \( x_1 = x_2 \) and \( x_2 = x_3 \). So \( \ker T = \Span\bigl((1,1,1)\bigr) \). The transpose \( \C\tp \) has rows \( (1, 0, -1) \), \( (-1, 1, 0) \), \( (0, -1, 1) \), and \( \C\tp\x = \0 \) again reads \( x_1 = x_3 \) and \( x_1 = x_2 \). The two kernels agree, as @cor-normal-kernel (a) requires.

(c) The rank is \( 3 - 1 = 2 \) by @thm-rank-nullity, and the first two columns \( (1, 0, -1) \) and \( (-1, 1, 0) \) are independent, so
\[
\im T = \Span\bigl((1,0,-1),\ (-1,1,0)\bigr) .
\]
Both spanning vectors have coordinate sum \( 0 \), hence are orthogonal to \( (1,1,1) \), so \( \im T \perp \ker T \). Since \( \dim\ker T + \dim\im T = 1 + 2 = 3 \) and the two subspaces meet only in \( \0 \) (being orthogonal), \( \nR^3 = \ker T \oplus \im T \). Indeed \( \im T = \{\x : x_1 + x_2 + x_3 = 0\} = (\ker T)^{\perp} \).
:::

::: {#exr-normal-operators-b3}
[B3: Triangular and normal, by hand]

Let \( \A = \begin{pmatrix} a & b \\ 0 & d \end{pmatrix} \in M_2(\nC) \).

::: {.enumerate options="label=(\alph*)"}
1. Compute the \( (1,1) \) entries of \( \A^{*}\A \) and of \( \A\A^{*} \).
2. Hence prove that \( \A \) is normal if and only if \( b = 0 \), that is, if and only if \( \A \) is diagonal.
3. Which upper triangular matrices in \( M_2(\nC) \) are unitary?
:::

*Hint: for (a), you only need one entry of each product.*
:::

::: {.solution}
(a) The \( (1,1) \) entry of \( \A^{*}\A \) is the squared norm of the first **column** of \( \A \), namely \( \lvert a\rvert^2 \). The \( (1,1) \) entry of \( \A\A^{*} \) is the squared norm of the first **row**, namely \( \lvert a\rvert^2 + \lvert b\rvert^2 \). In full,
\[
\begin{aligned}
\A^{*}\A &= \begin{pmatrix} \lvert a\rvert^2 & \conj{a}b \\ a\conj{b} & \lvert b\rvert^2 + \lvert d\rvert^2 \end{pmatrix}, \\[4pt]
\A\A^{*} &= \begin{pmatrix} \lvert a\rvert^2 + \lvert b\rvert^2 & b\conj{d} \\ \conj{b}d & \lvert d\rvert^2 \end{pmatrix} .
\end{aligned}
\]

(b) \( (\Rightarrow) \) If \( \A \) is normal, comparing the \( (1,1) \) entries gives \( \lvert a\rvert^2 = \lvert a\rvert^2 + \lvert b\rvert^2 \), so \( \lvert b\rvert^2 = 0 \) and \( b = 0 \). \( (\Leftarrow) \) A diagonal matrix is normal, since \( \D^{*}\D = \D\D^{*} = \diag(\lvert a\rvert^2, \lvert d\rvert^2) \).

(c) A unitary matrix is normal, so by (b) it must be diagonal, \( \diag(a, d) \), and then \( \A^{*}\A = \diag(\lvert a\rvert^2, \lvert d\rvert^2) = \I \) forces \( \lvert a\rvert = \lvert d\rvert = 1 \). Conversely every such matrix is unitary. So the upper triangular unitary matrices are exactly \( \diag(a, d) \) with \( \lvert a\rvert = \lvert d\rvert = 1 \).
:::

### C. Going deeper

::: {#exr-normal-operators-c1}
[C1: A normal operator with no proper invariant subspace]

Let \( V \) be a finite-dimensional complex inner product space with \( V \neq \{\0\} \), and let \( T \in \cL(V) \) be normal. Suppose the only \( T \)-invariant subspaces of \( V \) are \( \{\0\} \) and \( V \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \dim V = 1 \).
2. Show that the conclusion fails over \( \nR \), by exhibiting a normal operator on \( \nR^2 \) whose only invariant subspaces are \( \{\0\} \) and \( \nR^2 \).
3. Where exactly does the argument of (a) use that the field is \( \nC \)?
:::

*Hint: an eigenvector spans an invariant subspace.*
:::

::: {.solution}
(a) Since \( V \neq \{\0\} \) and the field is \( \nC \), \( T \) has an eigenvector \( \v \ne \0 \) (@thm-complex-operator-has-eigenvalue). Then \( \Span(\v) \) is \( T \)-invariant and non-zero, so by hypothesis \( \Span(\v) = V \) and \( \dim V = 1 \). Normality is not needed for this direction.

(b) The quarter turn \( \R_{\pi/2} = \begin{pmatrix} 0 & -1 \\ 1 & 0\end{pmatrix} \) is orthogonal, hence normal. A \( 1 \)-dimensional invariant subspace would be spanned by a real eigenvector, and \( \R_{\pi/2} \) has none: its characteristic polynomial is \( x^2 + 1 \), with no real root. So its only invariant subspaces are \( \{\0\} \) and \( \nR^2 \), while \( \dim \nR^2 = 2 \).

(c) Only in the existence of an eigenvector. Over \( \nC \) that is the Fundamental Theorem of Algebra (@thm-fundamental-theorem-of-algebra) reaching the characteristic polynomial; over \( \nR \) the polynomial may have no root, which is exactly what (b) exploits. Note that @prp-normal-invariant-reducing still holds over \( \nR \) — it says nothing about invariant subspaces *existing*.
:::

::: {#exr-normal-operators-c2}
[C2: Arithmetic of normal operators]

Let \( S, T \in \cL(V) \) be normal.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( T^{*} \) is normal and that \( cT \) is normal for every \( c \in F \).
2. Prove that \( p(T) \) is normal for every polynomial \( p \in F[x] \).
3. Give a concrete \( S \) and \( T \), both normal, with \( ST \) not normal. (Part (b) shows that this cannot happen when \( S \) is a polynomial in \( T \).)
:::
:::

::: {.solution}
(a) \( (T^{*})^{*}T^{*} = TT^{*} = T^{*}T = T^{*}(T^{*})^{*} \), using \( T^{**} = T \) (@thm-adjoint-properties (d)). For \( cT \), by @thm-adjoint-properties (b) we have \( (cT)^{*} = \conj{c}T^{*} \), so
\[
(cT)^{*}(cT) = \conj{c}c\,T^{*}T = \lvert c\rvert^2\,TT^{*} = (cT)(cT)^{*} .
\]

(b) Write \( p(x) = \sum_{k} a_kx^{k} \). Then \( p(T)^{*} = \sum_k \conj{a_k}(T^{*})^{k} \) by @thm-adjoint-properties (a), (b) and (c). Every power of \( T \) commutes with every power of \( T^{*} \): from \( TT^{*} = T^{*}T \) one moves a \( T^{*} \) past one \( T \) at a time. Hence \( p(T) \) and \( p(T)^{*} \), being sums of products of such powers, commute, and \( p(T) \) is normal.

(c) Take \( S = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix} \) and \( T = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \), both symmetric and hence normal. Then
\[
\begin{aligned}
ST &= \begin{pmatrix} 0 & 1 \\ 2 & 0 \end{pmatrix}, \\[4pt]
(ST)\tp(ST) &= \begin{pmatrix} 4 & 0 \\ 0 & 1 \end{pmatrix},
\qquad
(ST)(ST)\tp = \begin{pmatrix} 1 & 0 \\ 0 & 4 \end{pmatrix},
\end{aligned}
\]
so \( ST \) is not normal.
:::

::: {#exr-normal-operators-c3}
[C3: Normality depends on the inner product]

Normality is a property of \( T \) **together with** an inner product, not of \( T \) alone. Work on \( V = \nR^2 \) with the operator \( T \) whose standard matrix is \( \A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Verify that \( T \) is normal for the standard inner product.
2. Now use \( \inner{\x}{\y}_{\G} = \y\tp\G\x \) with \( \G = \diag(1, 2) \), which is an inner product on \( \nR^2 \). Using the rule \( \mtx{T^{*}}{\sE}{\sE} = \G^{-1}\A\tp\G \) in the standard basis \( \sE \) (@exr-adjoints-c3), compute the matrix of the adjoint of \( T \) for this inner product.
3. Show that \( T \) is **not** normal for \( \inner{\cdot}{\cdot}_{\G} \), and reconcile this with (a).
:::
:::

::: {.solution}
(a) \( \A\tp\A = \A\A\tp = \I \), so \( T \) is even orthogonal, hence normal.

(b) \( \G^{-1} = \diag(1, \tfrac12) \), so
\[
\begin{aligned}
\G^{-1}\A\tp\G
&= \begin{pmatrix} 1 & 0 \\ 0 & \tfrac12 \end{pmatrix}
\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}
\begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix} \\[4pt]
&= \begin{pmatrix} 0 & 2 \\ -\tfrac12 & 0 \end{pmatrix} .
\end{aligned}
\]
Call this matrix \( \A^{\star} \).

(c) Computing both products,
\[
\A\A^{\star} = \begin{pmatrix} \tfrac12 & 0 \\ 0 & 2 \end{pmatrix},
\qquad
\A^{\star}\A = \begin{pmatrix} 2 & 0 \\ 0 & \tfrac12 \end{pmatrix},
\]
which differ, so \( T \) is not normal for \( \inner{\cdot}{\cdot}_{\G} \). There is no contradiction: the adjoint is built from the inner product (@def-adjoint), so changing the inner product changes \( T^{*} \), and with it the equation \( T^{*}T = TT^{*} \). The standard basis is orthonormal for the first inner product and not for the second, which is exactly the hypothesis @thm-matrix-of-adjoint needs.
:::
