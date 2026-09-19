# Inertia, Again and Additively

Chapter 13 attached three numbers to a real symmetric matrix — how many positive, how many negative, how many zero entries appear on the diagonal after a congruence — and proved that the three do not depend on which congruence was used. The proof there was elementary and self-contained: an orthogonal basis for the form, two subspaces, a dimension count. This section proves the same theorem a second time, from the min–max description of the eigenvalues, and then shows what the second proof buys that the first could not: the three numbers become **additive across a Schur complement**.

**Throughout, \( F = \nR \) or \( F = \nC \), and every matrix whose eigenvalues or inertia are named is Hermitian** — real symmetric when \( F = \nR \). Its eigenvalues are real and are indexed decreasingly, \( \lambda_1(\A) \ge \dots \ge \lambda_n(\A) \), as everywhere in this chapter. **Congruence** means the operation \( \A \mapsto \P^{*}\A\P \) with \( \P \) invertible, which sends Hermitian matrices to Hermitian matrices; over \( \nR \) the star is the plain transpose and this is exactly the relation \( \A \simeq \B \) of @def-congruent, and Chapter 12 already used the complex version in @prp-congruence-positivity.

## A symbol for the triple

Chapter 13 §05 named the three counts and proved them well defined, and @def-signature records the words: the triple \( (n_+, n_-, n_0) \) is the **inertia** and the pair \( (n_+, n_-) \) the **signature**. What it did not do is give the triple a symbol, because it never needed to write an equation between two triples. This section writes several, so the symbol is worth the line it costs.

::: {#def-inertia-triple}
[The Inertia Triple]

Let \( \A \in M_n(F) \) be Hermitian, with eigenvalues \( \lambda_1(\A) \ge \dots \ge \lambda_n(\A) \) listed **with multiplicity**. Write \( n_+(\A) \), \( n_-(\A) \) and \( n_0(\A) \) for the numbers of indices \( i \) with \( \lambda_i(\A) > 0 \), with \( \lambda_i(\A) < 0 \) and with \( \lambda_i(\A) = 0 \), and set
\[
\operatorname{In}(\A) \coloneqq \bigl(n_+(\A),\ n_-(\A),\ n_0(\A)\bigr) \in \nN^3 .
\]
Triples are added **entrywise**.
:::

Clause by clause. Every eigenvalue is counted, so \( n_+ + n_- + n_0 = n \) always. The counts are *with multiplicity*: \( \operatorname{In}(\I_n) = (n, 0, 0) \), not \( (1,0,0) \). And \( n_0(\A) = \dim\nul(\A) \), because a Hermitian matrix is unitarily diagonalizable (@cor-spectral-complex-matrix, or @cor-spectral-real-matrix when \( F = \nR \)), so the eigenspace for \( 0 \) has dimension equal to the multiplicity of \( 0 \) in the list; equivalently \( n_+ + n_- = \rank\A \).

For \( F = \nR \) this is not a new object. @thm-inertia-from-eigenvalues says precisely that the numbers of positive, negative and zero *eigenvalues* of a real symmetric \( \A \) are the numbers of positive, negative and zero *diagonal entries* after any congruence to diagonal form — that is, the inertia of @def-signature. So \( \operatorname{In}(\A) \) is the old triple, freshly abbreviated.

A few values, and the dictionary with definiteness. \( \operatorname{In}(\0_n) = (0, 0, n) \), and \( \operatorname{In}(\diag(1,-1)) = (1,1,0) \). By @thm-psd-characterizations, \( \A \succeq 0 \) exactly when every eigenvalue is \( \ge 0 \), that is when \( n_-(\A) = 0 \); by @thm-pd-characterizations, \( \A \succ 0 \) exactly when \( \operatorname{In}(\A) = (n, 0, 0) \). Definiteness is the extreme case of inertia, and everything below degenerates to a known statement about definiteness when the triple is extreme.

## Sylvester's law, proved again

The description of \( n_+ \) that this chapter can supply is not a count of diagonal entries at all. It is a maximum over subspaces, and it mentions no basis, no diagonalization and no matrix.

::: {#thm-inertia-second-proof}
[Sylvester's Law of Inertia, Second Proof]

Let \( \A \in M_n(F) \) be Hermitian. Call a subspace \( W \le F^n \) **\( \A \)-positive** if \( \inner{\A\x}{\x} > 0 \) for every \( \x \in W \) with \( \x \ne \0 \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( n_+(\A) = \max\{\dim W : W \text{ is } \A\text{-positive}\} \), and the maximum is attained at the span of an orthonormal family of eigenvectors for the positive eigenvalues of \( \A \);
2. for every invertible \( \P \in M_n(F) \), the matrix \( \P^{*}\A\P \) is Hermitian and
\[
\operatorname{In}(\P^{*}\A\P) = \operatorname{In}(\A) .
\]
:::

Over \( \nR \), part (b) is Sylvester's Law of Inertia, @thm-sylvester-inertia.
:::

::: {.idea}
For (a), read @thm-courant-fischer through a sign. Its max–min form says \( \lambda_k(\A) \) is the largest value that \( R_{\A} \) can be *guaranteed* to exceed on a \( k \)-dimensional subspace; and "\( W \) is \( \A \)-positive" says exactly that \( R_{\A} \) is guaranteed to be positive on \( W \). So \( \A \)-positive subspaces of dimension \( k \) exist precisely when \( \lambda_k(\A) > 0 \), which is precisely when \( k \le n_+ \). For (b), the right-hand side of (a) is defined from the quadratic form alone, and a congruence is a change of variables inside that form: \( \x \mapsto \P\x \) matches up the two families of positive subspaces, dimension for dimension.
:::

::: {.proof}
Throughout, note that \( \inner{\A\x}{\x} = \x^{*}\A\x \) is real for Hermitian \( \A \) (@prp-self-adjoint-immediate (a), or directly: \( \conj{\x^{*}\A\x} = \x^{*}\A^{*}\x = \x^{*}\A\x \)), and that for \( \x \ne \0 \) the sign of \( \inner{\A\x}{\x} \) is the sign of the Rayleigh quotient \( R_{\A}(\x) = \inner{\A\x}{\x}/\inner{\x}{\x} \) of @def-rayleigh-quotient, since \( \inner{\x}{\x} = \norm{\x}^2 > 0 \). So \( W \) is \( \A \)-positive if and only if \( R_{\A}(\x) > 0 \) for every \( \x \in W \setminus \{\0\} \).

*(a), the lower bound.* Put \( k = n_+(\A) \). If \( k = 0 \) the zero subspace is \( \A \)-positive and there is nothing to prove, so assume \( k \ge 1 \). By the spectral theorem (@cor-spectral-complex-matrix, or @cor-spectral-real-matrix when \( F = \nR \)) there is an orthonormal basis \( \q_1, \dots, \q_n \) of \( F^n \) with \( \A\q_i = \lambda_i(\A)\q_i \), the eigenvalues in decreasing order. Put \( W_0 = \Span(\q_1, \dots, \q_k) \), of dimension \( k \). For \( \0 \ne \x = \sum_{i \le k}c_i\q_i \), expanding by orthonormality,
\[
\inner{\A\x}{\x} = \sum_{i=1}^{k}\lambda_i(\A)\lvert c_i\rvert^2 \ \ge\ \lambda_k(\A)\sum_{i=1}^{k}\lvert c_i\rvert^2 = \lambda_k(\A)\norm{\x}^2 > 0 ,
\]
because \( \lambda_i(\A) \ge \lambda_k(\A) \) for \( i \le k \) and \( \lambda_k(\A) > 0 \), the latter since \( k = n_+(\A) \) counts the positive eigenvalues of a decreasing list. So \( W_0 \) is \( \A \)-positive of dimension \( n_+(\A) \).

*(a), the upper bound.* Let \( W \) be \( \A \)-positive with \( d = \dim W \ge 1 \). The unit sphere \( S_W = \{\x \in W : \norm{\x} = 1\} \) is a closed bounded subset of \( F^n \), hence compact by fact (A3) of Chapter 15's introduction, and it is non-empty because \( d \ge 1 \). The function \( \x \mapsto R_{\A}(\x) \) is continuous on it, so by the extreme value theorem — fact (A4) of Chapter 15's introduction — it attains a minimum \( m = R_{\A}(\x_0) \) there, and \( m > 0 \) because \( \x_0 \in W \) is non-zero. By homogeneity of \( R_{\A} \), the same \( m \) is the minimum over all non-zero \( \x \in W \). Now \( W \) is one competitor in the max–min form of @thm-courant-fischer, so
\[
\lambda_d(\A) = \max_{\dim W' = d}\ \min_{\0 \ne \x \in W'} R_{\A}(\x) \ \ge\ m \ >\ 0 .
\]
A decreasing list with \( \lambda_d > 0 \) has at least \( d \) positive entries, so \( d \le n_+(\A) \). Together with the lower bound this proves (a).

*(b).* Put \( \B = \P^{*}\A\P \). Then \( \B^{*} = \P^{*}\A^{*}\P = \B \), so \( \B \) is Hermitian. For every \( \x \in F^n \),
\[
\inner{\B\x}{\x} = \x^{*}\P^{*}\A\P\x = (\P\x)^{*}\A(\P\x) = \inner{\A(\P\x)}{\P\x} .
\]
Since \( \P \) is invertible, \( \x \mapsto \P\x \) is an isomorphism of \( F^n \); its restriction to a subspace \( W \) is an isomorphism \( W \to \P W \), which carries a basis to a basis (@thm-isomorphism-preserves-bases), so \( \dim\P W = \dim W \). And \( W \mapsto \P W \) is a bijection on subspaces, with inverse \( W' \mapsto \P^{-1}W' \). Moreover \( W \) is \( \B \)-positive if and only if \( \P W \) is \( \A \)-positive: the non-zero vectors of \( \P W \) are exactly the vectors \( \P\x \) with \( \0 \ne \x \in W \), and the display says the two quadratic forms agree at matched vectors. Hence the two sets of dimensions appearing in (a) coincide, and (a) gives \( n_+(\B) = n_+(\A) \).

Applying this to \( -\A \), whose eigenvalues are the negatives of those of \( \A \) and whose congruence by \( \P \) is \( -\B \), gives \( n_-(\B) = n_+(-\B) = n_+(-\A) = n_-(\A) \). Finally \( n_0 = n - n_+ - n_- \) for both. This proves the theorem.
:::

**What each proof gives.** Over \( \nR \) the two theorems say the same thing, since a congruence is exactly a change of basis for the underlying form (@thm-change-of-basis-form). They are not interchangeable.

Chapter 13's proof uses only the existence of an orthogonal basis for the form, the invariance of rank under congruence and the dimension formula. It mentions no inner product, no eigenvalue and no limit — in Chapter 13 the eigenvalues enter only afterwards, in @thm-inertia-from-eigenvalues — and it is the proof to give for a symmetric bilinear form on an abstract real vector space, where no inner product has been chosen and the words "Hermitian matrix" have no meaning until one is.

The proof above costs the spectral theorem and one appeal to compactness. In exchange it gives three things. First, a **description of \( n_+ \) with no basis in it at all** — a maximum over subspaces — together with an explicit optimal subspace, which is what @exr-sylvesters-law-of-inertia-c1 asked the reader to establish by hand from an orthogonal basis; here it falls out of the min–max, with the eigenvalues attached. Second, it works **over \( \nC \)**, for Hermitian matrices and the congruence \( \A \mapsto \P^{*}\A\P \), which @thm-sylvester-inertia does not cover. Third, it keeps the eigenvalues in view, so the perturbation theory of Section 3 applies to the inertia directly; that is the next theorem. Haynsworth's theorem at the end of the section leans on the second gain: for complex Hermitian matrices, only this proof supplies the law of inertia it needs.

The companions of part (a) are worth stating, because one of them is a trap.

::: {#cor-inertia-subspace-characterization}
[What Each Count Is a Maximum Of]

Let \( \A \in M_n(F) \) be Hermitian.

::: {.enumerate options="label=(\alph*)"}
1. \( n_-(\A) = \max\{\dim W : \inner{\A\x}{\x} < 0 \text{ for every } \0 \ne \x \in W\} \);
2. \( n_+(\A) + n_0(\A) = \max\{\dim W : \inner{\A\x}{\x} \ge 0 \text{ for every } \x \in W\} \), and symmetrically \( n_-(\A) + n_0(\A) \) is the largest dimension of a subspace on which \( \inner{\A\x}{\x} \le 0 \);
3. \( n_0(\A) = \dim\nul(\A) = n - n_+(\A) - n_-(\A) \).
:::
:::


::: {.idea}
Each claim has a witness and a competitor, as in Courant–Fischer. The witness is the span of the eigenvectors with the right sign; any competing subspace that is too large must meet the span of the eigenvectors of the wrong sign, and on that intersection the form has the wrong sign. For (c), no maximum is involved at all — the kernel is read off the eigenvalues.
:::

::: {.proof}
(a) Apply @thm-inertia-second-proof (a) to \( -\A \): its eigenvalues are the negatives of those of \( \A \), so \( n_+(-\A) = n_-(\A) \), and a subspace is \( (-\A) \)-positive exactly when \( \inner{\A\x}{\x} < 0 \) on its non-zero vectors.

(b) Fix, as in the previous proof, an orthonormal eigenbasis \( \q_1, \dots, \q_n \) of \( \A \) with \( \A\q_i = \lambda_i(\A)\q_i \) (@cor-spectral-complex-matrix). Let \( t = n_+(\A) + n_0(\A) \), so that \( \lambda_i(\A) \ge 0 \) exactly for \( i \le t \). On \( W_1 = \Span(\q_1, \dots, \q_t) \) the same expansion gives \( \inner{\A\x}{\x} = \sum_{i \le t}\lambda_i(\A)\lvert c_i\rvert^2 \ge 0 \), so the maximum is at least \( t \). Conversely let \( W \) satisfy \( \inner{\A\x}{\x} \ge 0 \) throughout and suppose \( \dim W > t \). Put \( W_2 = \Span(\q_{t+1}, \dots, \q_n) \), of dimension \( n - t = n_-(\A) \), on whose non-zero vectors \( \inner{\A\x}{\x} = \sum_{i > t}\lambda_i(\A)\lvert c_i\rvert^2 < 0 \), every \( \lambda_i(\A) \) with \( i > t \) being negative. Since \( \dim W + \dim W_2 > t + (n - t) = n \), @lem-subspace-intersection produces \( \0 \ne \x \in W \cap W_2 \), for which \( \inner{\A\x}{\x} \) is both \( \ge 0 \) and \( < 0 \). This is impossible, so \( \dim W \le t \). The statement with \( \le \) follows by applying this one to \( -\A \).

(c) The first equality was recorded after @def-inertia-triple, and the second is \( n_+ + n_- + n_0 = n \).
:::

::: {.warning}
**\( n_0 \) is not the largest dimension of a subspace on which the form vanishes.** Parts (a) and (b) describe \( n_- \), \( n_+ \) and their sums with \( n_0 \) as maxima over subspaces; \( n_0 \) itself has no such description, and guessing one is the standard error here. Take \( \A = \diag(1, -1) \), so \( \operatorname{In}(\A) = (1, 1, 0) \) and \( n_0(\A) = 0 \). On the line \( W = \Span\bigl((1,1)\bigr) \),
\[
\inner{\A\x}{\x} = x_1^2 - x_2^2 = 0 \qquad \text{for every } \x \in W ,
\]
so a subspace of dimension \( 1 \) carries the identically zero form while \( n_0(\A) = 0 \). What \( n_0 \) *is* is \( \dim\nul(\A) \), by (c) — a kernel, not a maximum. The largest dimension of a subspace on which the form vanishes identically is a different invariant. For a real symmetric **invertible** \( \A \) it is the Witt index of Chapter 13 §07, which that section defines only for non-degenerate forms and bounds by \( n/2 \). For a singular \( \A \) the bound fails — for \( \A = 0 \) the whole space qualifies — and in general the answer is \( n_0 + \min(n_+, n_-) \), which @exr-inertia-revisited-c1 computes.
:::

::: {.check}
A Hermitian \( \A \in M_5(F) \) has \( \operatorname{In}(\A) = (2, 2, 1) \). What is the largest dimension of a subspace on which \( \inner{\A\x}{\x} > 0 \) for all non-zero \( \x \), and the largest on which \( \inner{\A\x}{\x} \ge 0 \) for all \( \x \)?
:::

::: {.solution}
\( 2 \) and \( 3 \). The first is \( n_+(\A) = 2 \) by @thm-inertia-second-proof (a); the second is \( n_+(\A) + n_0(\A) = 2 + 1 = 3 \) by @cor-inertia-subspace-characterization (b). The kernel direction may be added to a positive subspace without breaking \( \ge 0 \), but it does break \( > 0 \) — which is the whole difference between the two numbers.
:::

## Inertia under a perturbation of small rank

A congruence leaves the inertia alone and does nothing else: it can move the eigenvalues anywhere compatible with their signs. Chapter 13 §05's warning displayed the pair
\[
\A = \diag(1, -1), \qquad \P\tp\A\P = \diag(4, -9) \quad (\P = \diag(2, 3)) ,
\]
where \( \lambda_1 \) rose from \( 1 \) to \( 4 \) and \( \lambda_2 \) fell from \( -1 \) to \( -9 \). There is no interlacing here: \( \lambda_1(\A) \ge \lambda_1(\P\tp\A\P) \) already fails. A congruence *is* a perturbation, \( \P^{*}\A\P = \A + \E \) with \( \E = \P^{*}\A\P - \A \), but \( \E \) can have full rank, and then the rank bound of Section 3 says nothing. When the perturbation has small rank, it does.

::: {#thm-inertia-rank-perturbation}
[Inertia Moves by at Most the Rank]

Let \( \A, \E \in M_n(F) \) be Hermitian with \( \rank\E \le r \). Then
\[
\lvert n_+(\A + \E) - n_+(\A)\rvert \le r,
\qquad
\lvert n_-(\A + \E) - n_-(\A)\rvert \le r ,
\]
and \( \lvert n_0(\A + \E) - n_0(\A)\rvert \le r \) as well.
:::

::: {.idea}
@cor-weyl-rank-bound says that adding a matrix of rank \( r \) shifts each eigenvalue by at most \( r \) places in the ordered list. A count of positive eigenvalues is a count of places, so it too can move by at most \( r \).
:::

::: {.proof}
Put \( s = n_+(\A + \E) \). If \( s \le r \) then certainly \( n_+(\A) \ge 0 \ge s - r \). Otherwise \( i \coloneqq s - r \) satisfies \( 1 \le i \) and \( i + r = s \le n \), so @cor-weyl-rank-bound applies with this \( i \) and gives
\[
\lambda_{s}(\A + \E) = \lambda_{i+r}(\A + \E) \ \le\ \lambda_i(\A) = \lambda_{s-r}(\A) .
\]
Since \( s = n_+(\A+\E) \) we have \( \lambda_s(\A+\E) > 0 \), hence \( \lambda_{s-r}(\A) > 0 \), hence \( n_+(\A) \ge s - r \). In either case
\[
n_+(\A + \E) - n_+(\A) \le r .
\]
For the opposite inequality, write \( \A = (\A + \E) + (-\E) \), where \( -\E \) is Hermitian with \( \rank(-\E) = \rank\E \le r \), and apply what was just proved with \( \A + \E \) in the role of \( \A \): \( n_+(\A) - n_+(\A+\E) \le r \). The two together give the first claim.

The second claim is the first applied to the Hermitian pair \( -\A, -\E \), using \( n_-(\M) = n_+(-\M) \). For the third, adding the first two would only give \( 2r \); the sharp bound comes from kernels instead. By @cor-inertia-subspace-characterization (c), \( n_0(\M) = \dim\nul(\M) \) for every Hermitian \( \M \). A vector killed by both \( \A \) and \( \E \) is killed by \( \A + \E \), so \( \nul(\A) \cap \nul(\E) \subseteq \nul(\A + \E) \); and \( \dim\nul(\E) = n - \rank\E \ge n - r \) by @thm-rank-nullity. The sharper form of @lem-subspace-intersection then gives
\[
n_0(\A + \E) \ \ge\ \dim\bigl(\nul(\A) \cap \nul(\E)\bigr) \ \ge\ n_0(\A) + (n - r) - n \ =\ n_0(\A) - r .
\]
Applied to \( \A = (\A + \E) + (-\E) \) the same argument gives \( n_0(\A) \ge n_0(\A + \E) - r \), and the two together are the claim. The bound is attained: \( \A = \I_r \oplus 0 \) and \( \E = -\I_r \oplus 0 \) give \( n_0(\A) = n - r \) and \( n_0(\A + \E) = n \).
This proves the theorem.
:::

::: {#exm-inertia-rank-one}
[A rank-one perturbation, three ways]

Let \( \A = \diag(3, -1, -2) \) and \( \v = (1, 1, 0) \), and let \( \E_t = t\,\v\v\tp \), which has rank \( 1 \) for \( t \ne 0 \). Find \( \operatorname{In}(\A + \E_t) \) for \( t = 2 \), \( t = \tfrac32 \) and \( t = -5 \), and check @thm-inertia-rank-perturbation.
:::

::: {.solution}
\( \operatorname{In}(\A) = (1, 2, 0) \), read off the diagonal. Since \( \v \) has third entry \( 0 \),
\[
\A + \E_t = \begin{pmatrix} 3 + t & t & 0 \\ t & t - 1 & 0 \\ 0 & 0 & -2\end{pmatrix}
= \begin{pmatrix} 3+t & t \\ t & t-1\end{pmatrix} \oplus (-2) ,
\]
and the eigenvalue list of a block diagonal matrix is the two lists together (its characteristic polynomial is the product of the two, by @thm-det-block-triangular). The entry \( -2 \) contributes one negative eigenvalue for every \( t \). The \( 2\times2 \) block has
\[
\det = (3+t)(t-1) - t^2 = 2t - 3, \qquad \tr = 2t + 2 ,
\]
and since the determinant of a real symmetric \( 2\times2 \) matrix is the product of its two real eigenvalues and the trace is their sum, the eigenvalues both have the sign of the trace when the determinant is positive, have opposite signs when it is negative, and are \( 0 \) and \( \tr \) when it is zero.

- \( t = 2 \): \( \det = 1 > 0 \), \( \tr = 6 > 0 \), so the block contributes \( (2, 0, 0) \) and \( \operatorname{In}(\A + \E_2) = (2, 1, 0) \).
- \( t = \tfrac32 \): \( \det = 0 \), \( \tr = 5 \), so the block contributes \( (1, 0, 1) \) and \( \operatorname{In}(\A + \E_{3/2}) = (1, 1, 1) \).
- \( t = -5 \): \( \det = -13 < 0 \), so the block contributes \( (1, 1, 0) \) and \( \operatorname{In}(\A + \E_{-5}) = (1, 2, 0) \), unchanged.

Against \( \operatorname{In}(\A) = (1, 2, 0) \): at \( t = 2 \) one negative direction has become positive, so \( n_+ \) and \( n_- \) each move by \( 1 = r \) and the bound of @thm-inertia-rank-perturbation is attained; at \( t = \tfrac32 \), exactly on the way between, the direction passes through \( 0 \), so \( n_- \) and \( n_0 \) each move by \( 1 \). No rank-one perturbation of this \( \A \) can reach \( (3, 0, 0) \), which would need \( n_+ \) to move by \( 2 \).
:::

## Additivity across a Schur complement

Chapter 7 built the Schur complement out of block elimination and proved two things about it: \( \det\M = \det\A\cdot\det(\M/\A) \) (@thm-schur-determinant) and \( \rank\M = k + \rank(\M/\A) \) (@thm-schur-rank). Chapter 12 then used the same elimination on Hermitian matrices — in §01, observing that it is the block \( \L\D\U \) factorization written as a congruence, and in §06, to prove @thm-block-psd-schur — and each time read off a statement about positive definiteness only. Haynsworth's theorem is what that congruence is worth in general: the rank does not merely add, the *signs* add.

::: {#thm-haynsworth}
[Haynsworth's Inertia Additivity Formula]

Let \( 1 \le k \le n-1 \) and let
\[
\M = \begin{pmatrix} \A & \B \\ \B^{*} & \D \end{pmatrix} \in M_n(F)
\]
be Hermitian, with \( \A \in M_k(F) \) **invertible**, \( \B \in M_{k \times (n-k)}(F) \) and \( \D \in M_{n-k}(F) \). Then \( \A \) and the Schur complement \( \M/\A = \D - \B^{*}\A^{-1}\B \) (@def-schur-complement) are Hermitian, and
\[
\operatorname{In}(\M) = \operatorname{In}(\A) + \operatorname{In}(\M/\A) .
\]
:::

::: {.idea}
Block elimination factors \( \M \) as \( \L\,(\A \oplus \M/\A)\,\U \) with \( \L \) lower and \( \U \) upper unit block triangular (@thm-block-ldu). For a **Hermitian** \( \M \) with \( \A \) Hermitian, the two outer factors are conjugate transposes of each other, so the factorization is a congruence and not merely a factorization. @thm-inertia-second-proof (b) then says the inertia of \( \M \) is the inertia of \( \A \oplus \M/\A \), and the inertia of a block diagonal matrix is the sum of the inertias of its blocks, because its characteristic polynomial is the product.
:::

::: {.proof}
Since \( \M^{*} = \M \), comparing blocks gives \( \A^{*} = \A \) and \( \D^{*} = \D \). As \( \A \) is Hermitian and invertible, \( (\A^{-1})^{*} = (\A^{*})^{-1} = \A^{-1} \), so \( \A^{-1} \) is Hermitian and
\[
(\M/\A)^{*} = \D^{*} - \B^{*}(\A^{-1})^{*}\B = \D - \B^{*}\A^{-1}\B = \M/\A .
\]

**Step 1: the elimination is a congruence.** By @thm-block-ldu (a), applied with \( \C = \B^{*} \),
\[
\M = \L\,\bigl(\A \oplus (\M/\A)\bigr)\,\U,
\qquad
\L = \begin{pmatrix} \I_k & \0 \\ \B^{*}\A^{-1} & \I_{n-k}\end{pmatrix},
\quad
\U = \begin{pmatrix} \I_k & \A^{-1}\B \\ \0 & \I_{n-k}\end{pmatrix} .
\]
Now \( \U^{*} \) has blocks \( \I_k, \0 \) on top and \( (\A^{-1}\B)^{*} = \B^{*}\A^{-1} \), \( \I_{n-k} \) below, using that \( \A^{-1} \) is Hermitian; that is, \( \U^{*} = \L \). So
\[
\M = \U^{*}\bigl(\A \oplus (\M/\A)\bigr)\U .
\]
The matrix \( \U \) is invertible, with inverse \( \P \coloneqq \begin{psmallmatrix} \I_k & -\A^{-1}\B \\ \0 & \I_{n-k}\end{psmallmatrix} \), as multiplying out confirms. Multiplying the display by \( \P^{*} \) on the left and \( \P \) on the right, and using \( \P^{*}\U^{*} = (\U\P)^{*} = \I_n \),
\[
\P^{*}\M\P = \A \oplus (\M/\A) .
\]{#eq-haynsworth-congruence}

**Step 2: apply the law of inertia.** \( \P \) is invertible, so @thm-inertia-second-proof (b) gives
\[
\operatorname{In}(\M) = \operatorname{In}(\P^{*}\M\P) = \operatorname{In}\bigl(\A \oplus (\M/\A)\bigr) .
\]

**Step 3: inertia is additive over a block diagonal sum.** Let \( \X \in M_k(F) \) and \( \Y \in M_{n-k}(F) \) be Hermitian. The matrix \( x\I_n - (\X \oplus \Y) \) is block diagonal with blocks \( x\I_k - \X \) and \( x\I_{n-k} - \Y \), so by @thm-det-block-triangular its determinant is \( \det(x\I_k - \X)\det(x\I_{n-k} - \Y) \); that is, \( p_{\X \oplus \Y} = p_{\X}\,p_{\Y} \). The eigenvalue list of a Hermitian matrix with multiplicity is the list of roots of its characteristic polynomial with multiplicity, so the list for \( \X \oplus \Y \) is the two lists concatenated. Counting positive, negative and zero entries gives \( \operatorname{In}(\X\oplus\Y) = \operatorname{In}(\X) + \operatorname{In}(\Y) \).

Applying Step 3 with \( \X = \A \) and \( \Y = \M/\A \) to the conclusion of Step 2 proves the theorem.
:::

Three remarks. First, @eq-haynsworth-congruence is the cleanest illustration in the book of what a Schur complement *is*: the block elimination of Chapter 7, performed with the same matrix on both sides, is a congruence, and \( \M/\A \) is simply what the congruence leaves in the lower corner. For Hermitian \( \M \), Chapter 7's determinant and rank formulas are both shadows of this one identity. Second, taking ranks in @eq-haynsworth-congruence recovers @thm-schur-rank for Hermitian \( \M \), since \( n_+ + n_- = \rank \); Haynsworth refines the rank formula by splitting each rank into its two signs. Third, the theorem needs \( \A \) invertible and nothing else — no definiteness anywhere, which is what separates it from Chapter 12 §06's test.

::: {#exm-haynsworth-3x3}
[The Chapter 13 example, through a Schur complement]

Find \( \operatorname{In}(\M) \) for
\[
\M = \begin{pmatrix} 1 & 1 & 2 \\ 1 & 2 & 3 \\ 2 & 3 & 1\end{pmatrix},
\]
the matrix of @exm-inertia-by-elimination, using @thm-haynsworth with the leading \( 2\times2 \) block.
:::

::: {.solution}
Take \( \A = \begin{psmallmatrix} 1 & 1 \\ 1 & 2\end{psmallmatrix} \), \( \B = (2, 3)\tp \) and \( \D = (1) \). Then \( \det\A = 1 \ne 0 \), so \( \A \) is invertible with \( \A^{-1} = \begin{psmallmatrix} 2 & -1 \\ -1 & 1\end{psmallmatrix} \). Its leading principal minors are \( 1 \) and \( 1 \), both positive, so \( \A \succ 0 \) by @thm-pd-characterizations and \( \operatorname{In}(\A) = (2, 0, 0) \).

For the Schur complement, \( \B\tp\A^{-1} = (2, 3)\begin{psmallmatrix} 2 & -1 \\ -1 & 1\end{psmallmatrix} = (1, 1) \), so \( \B\tp\A^{-1}\B = (1,1)\cdot(2,3) = 5 \) and
\[
\M/\A = 1 - 5 = -4, \qquad \operatorname{In}(\M/\A) = (0, 1, 0) .
\]
Hence \( \operatorname{In}(\M) = (2,0,0) + (0,1,0) = (2, 1, 0) \).

Two checks. The congruence of @eq-haynsworth-congruence is given by \( \A^{-1}\B = (1, 1)\tp \), hence
\[
\P = \begin{pmatrix} 1 & 0 & -1 \\ 0 & 1 & -1 \\ 0 & 0 & 1\end{pmatrix},
\qquad
\P\tp\M\P = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 2 & 0 \\ 0 & 0 & -4\end{pmatrix},
\]
which is \( \A \oplus (-4) \) as the theorem says; and @exm-inertia-by-elimination reached \( \diag(1, 1, -4) \) by paired row and column operations, finding the same \( -4 \). The Schur complement of the leading block *is* the last pivot of the symmetric elimination. The eigenvalues were never needed: they are the roots of \( x^3 - 4x^2 - 9x + 4 \), which @exm-inertia-by-elimination already noted are irrational.
:::

::: {#exm-haynsworth-4x4}
[A 4 × 4 inertia in two lines]

Find \( \operatorname{In}(\N) \) for
\[
\N = \begin{pmatrix} 1 & 0 & 1 & 2 \\ 0 & 1 & 1 & -1 \\ 1 & 1 & 1 & 0 \\ 2 & -1 & 0 & 3 \end{pmatrix} .
\]
:::

::: {.solution}
The leading \( 2 \times 2 \) block is \( \A = \I_2 \), which is invertible with \( \operatorname{In}(\A) = (2, 0, 0) \) and \( \A^{-1} = \I_2 \). With
\[
\B = \begin{pmatrix} 1 & 2 \\ 1 & -1\end{pmatrix},
\qquad
\D = \begin{pmatrix} 1 & 0 \\ 0 & 3\end{pmatrix},
\]
the Schur complement needs no inversion at all:
\[
\N/\A = \D - \B\tp\B = \begin{pmatrix} 1 & 0 \\ 0 & 3\end{pmatrix} - \begin{pmatrix} 2 & 1 \\ 1 & 5\end{pmatrix} = \begin{pmatrix} -1 & -1 \\ -1 & -2\end{pmatrix} .
\]
This \( 2\times2 \) matrix has determinant \( 2 - 1 = 1 > 0 \) and trace \( -3 < 0 \), so both its eigenvalues are negative and \( \operatorname{In}(\N/\A) = (0, 2, 0) \). By @thm-haynsworth,
\[
\operatorname{In}(\N) = (2, 0, 0) + (0, 2, 0) = (2, 2, 0) .
\]
In particular \( \N \) is invertible and indefinite. The characteristic polynomial of \( \N \) is \( x^4 - 6x^3 + 5x^2 + 8x + 1 \), which has no rational root; the four eigenvalues were never computed, and the signature came from one \( 2\times2 \) determinant and one trace.
:::

::: {.warning}
**\( \A \) must be invertible, and the off-diagonal block is not a spectator.** Take \( \M = \begin{psmallmatrix} 0 & 1 \\ 1 & 0\end{psmallmatrix} \), with \( k = 1 \). Neither diagonal block is invertible, so no Schur complement exists for this partition and @thm-haynsworth does not apply — and its conclusion would be false if one tried to read the blocks directly: \( \operatorname{In}(\M) = (1,1,0) \), since the eigenvalues are \( \pm1 \), while the two diagonal blocks contribute \( (0,0,1) + (0,0,1) = (0,0,2) \). Even when \( \A \) *is* invertible, the diagonal blocks alone decide nothing: for \( \M_b = \begin{psmallmatrix} 1 & b \\ b & 1\end{psmallmatrix} \) with \( b \) real, the Schur complement is \( 1 - b^2 \), so \( \operatorname{In}(\M_b) \) is \( (2,0,0) \), \( (1,0,1) \) or \( (1,1,0) \) according as \( \lvert b\rvert < 1 \), \( = 1 \) or \( > 1 \). All the information is in the coupling.
:::

The positive definite case of Haynsworth is a theorem Chapter 12 proved by hand, and it is now one line.

::: {#cor-block-psd-by-inertia}
[Block Definiteness, a Second Proof]

Let \( 1 \le k \le n - 1 \) and let \( \M = \begin{psmallmatrix} \A & \B \\ \B^{*} & \D\end{psmallmatrix} \in M_n(F) \) be Hermitian with \( \A \in M_k(F) \) and \( \A \succ 0 \). Then
\[
\M \succ 0 \iff \M/\A \succ 0 ,
\qquad
\M \succeq 0 \iff \M/\A \succeq 0 .
\]
:::

::: {.proof}
\( \A \succ 0 \) is invertible (@thm-pd-characterizations) with \( \operatorname{In}(\A) = (k, 0, 0) \), so @thm-haynsworth gives
\[
\operatorname{In}(\M) = (k, 0, 0) + \operatorname{In}(\M/\A) .
\]
Comparing entries, \( n_+(\M) = k + n_+(\M/\A) \) and \( n_-(\M) = n_-(\M/\A) \), while \( \M/\A \in M_{n-k}(F) \).

Now \( \M \succ 0 \) means \( n_+(\M) = n \) (@thm-pd-characterizations), that is \( n_+(\M/\A) = n - k \), that is \( \M/\A \succ 0 \). And \( \M \succeq 0 \) means \( n_-(\M) = 0 \) (@thm-psd-characterizations), that is \( n_-(\M/\A) = 0 \), that is \( \M/\A \succeq 0 \). This proves the corollary.
:::

This is @thm-block-psd-schur (b). Chapter 12 §06 proved it with the very same congruence, and then read positivity directly off the split quadratic form \( \y_1^{*}\A\y_1 + \y_2^{*}(\M/\A)\y_2 \), with no eigenvalue in sight. The two proofs share their first step and differ in the second: Chapter 12's is shorter and needs nothing beyond @prp-congruence-positivity, while the one above reads the verdict off a count, and so shows the definite case as the extreme instance of an equality that holds for every Hermitian \( \M \) with \( \A \) invertible, definite or not.

## Exercises

### A. Check your understanding

:::: {#exr-inertia-revisited-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define \( \operatorname{In}(\A) \) for a Hermitian \( \A \), and say what \( n_+ + n_- \) equals.
2. State the subspace description of \( n_+(\A) \) and name the subspace that attains it.
3. Determine whether the following is correct, and justify: "\( n_0(\A) \) is the largest dimension of a subspace on which \( \inner{\A\x}{\x} \) vanishes identically."
4. State @thm-haynsworth, with all hypotheses.
5. A congruence preserves the inertia of a Hermitian matrix. Does it preserve the eigenvalues, the trace, or the rank? Justify each answer.
:::
::::

::: {.solution}
(a) \( \operatorname{In}(\A) = (n_+, n_-, n_0) \), the numbers of positive, negative and zero eigenvalues of \( \A \) counted with multiplicity (@def-inertia-triple). Their sum is \( n \), and \( n_+ + n_- = \rank\A \), since \( n_0 = \dim\nul(\A) \) by @cor-inertia-subspace-characterization (c).

(b) \( n_+(\A) \) is the largest dimension of a subspace \( W \) with \( \inner{\A\x}{\x} > 0 \) for every non-zero \( \x \in W \) (@thm-inertia-second-proof (a)), attained at the span of orthonormal eigenvectors for the positive eigenvalues, that is at \( \Span(\q_1, \dots, \q_{n_+}) \) in an eigenbasis ordered decreasingly.

(c) Incorrect. For \( \A = \diag(1,-1) \) we have \( n_0(\A) = 0 \), yet \( \inner{\A\x}{\x} = x_1^2 - x_2^2 \) vanishes identically on the line spanned by \( (1,1) \). The correct description is \( n_0(\A) = \dim\nul(\A) \).

(d) If \( \M = \begin{psmallmatrix}\A & \B\\ \B^{*} & \D\end{psmallmatrix} \in M_n(F) \) is Hermitian with \( \A \in M_k(F) \) invertible and \( 1 \le k \le n-1 \), then \( \operatorname{In}(\M) = \operatorname{In}(\A) + \operatorname{In}(\M/\A) \), where \( \M/\A = \D - \B^{*}\A^{-1}\B \).

(e) Rank: yes, since \( \rank = n_+ + n_- \) is determined by the inertia (and independently, congruence by an invertible matrix preserves rank by @thm-rank-product-inequality). Eigenvalues: no — \( \diag(1,-1) \) and \( \diag(4,-9) \) are congruent by \( \P = \diag(2,3) \). Trace: no, by the same pair, whose traces are \( 0 \) and \( -5 \).
:::

### B. Practice

:::: {#exr-inertia-revisited-b1}
[B1: Two inertias by Schur complement]

Find the inertia of each of the following, using @thm-haynsworth with the leading \( 2\times2 \) block, and compute no eigenvalues.

::: {.enumerate options="label=(\alph*)"}
1. \( \M = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 1 & 0 \\ 1 & 0 & -1\end{pmatrix} \).
2. \( \N = \begin{pmatrix} 1 & 0 & 1 & 1 \\ 0 & -1 & 1 & 0 \\ 1 & 1 & 2 & 0 \\ 1 & 0 & 0 & 1\end{pmatrix} \).
:::
::::

::: {.solution}
(a) \( \A = \begin{psmallmatrix} 2 & 1 \\ 1 & 1\end{psmallmatrix} \) has leading principal minors \( 2 \) and \( 1 \), both positive, so \( \A \succ 0 \) (@thm-pd-characterizations) and \( \operatorname{In}(\A) = (2,0,0) \); also \( \A^{-1} = \begin{psmallmatrix} 1 & -1 \\ -1 & 2\end{psmallmatrix} \). With \( \B = (1, 0)\tp \) and \( \D = (-1) \),
\[
\B\tp\A^{-1}\B = (1, 0)\begin{pmatrix} 1 & -1 \\ -1 & 2\end{pmatrix}\begin{pmatrix} 1 \\ 0\end{pmatrix} = 1 ,
\]
so \( \M/\A = -1 - 1 = -2 \) and \( \operatorname{In}(\M/\A) = (0,1,0) \). Hence \( \operatorname{In}(\M) = (2,1,0) \). (Consistency check: \( \det\M = \det\A\cdot(\M/\A) = 1\cdot(-2) = -2 \) by @thm-schur-determinant, and a \( 3\times3 \) matrix with inertia \( (2,1,0) \) has negative determinant.)

(b) \( \A = \diag(1, -1) \) is invertible with \( \A^{-1} = \A \) and \( \operatorname{In}(\A) = (1,1,0) \). With
\[
\B = \begin{pmatrix} 1 & 1 \\ 1 & 0\end{pmatrix},
\qquad
\D = \begin{pmatrix} 2 & 0 \\ 0 & 1\end{pmatrix},
\]
we get \( \A^{-1}\B = \begin{psmallmatrix} 1 & 1 \\ -1 & 0\end{psmallmatrix} \) and
\[
\B\tp\A^{-1}\B = \begin{pmatrix} 1 & 1 \\ 1 & 0\end{pmatrix}\begin{pmatrix} 1 & 1 \\ -1 & 0\end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 1\end{pmatrix} ,
\]
so
\[
\N/\A = \begin{pmatrix} 2 & 0 \\ 0 & 1\end{pmatrix} - \begin{pmatrix} 0 & 1 \\ 1 & 1\end{pmatrix} = \begin{pmatrix} 2 & -1 \\ -1 & 0\end{pmatrix} ,
\]
whose determinant is \( -1 < 0 \), so its two eigenvalues have opposite signs and \( \operatorname{In}(\N/\A) = (1,1,0) \). Hence \( \operatorname{In}(\N) = (1,1,0) + (1,1,0) = (2,2,0) \).
:::

:::: {#exr-inertia-revisited-b2}
[B2: How much can a rank-two perturbation do?]

Let \( \A \in M_6(\nR) \) be symmetric with \( \operatorname{In}(\A) = (4, 1, 1) \), and let \( \E \) be symmetric with \( \rank\E = 2 \).

::: {.enumerate options="label=(\alph*)"}
1. Which values of \( n_+(\A + \E) \) does @thm-inertia-rank-perturbation allow?
2. Show that the two extreme values are both achieved, for suitable \( \A \) and \( \E \).
3. Can \( \A + \E \) be negative definite? Justify.
:::
::::

::: {.solution}
(a) By @thm-inertia-rank-perturbation with \( r = 2 \), \( \lvert n_+(\A+\E) - 4\rvert \le 2 \), and \( n_+ \le 6 \) always, so \( n_+(\A+\E) \in \{2, 3, 4, 5, 6\} \).

(b) Take \( \A = \diag(1,1,1,1,-1,0) \), which has inertia \( (4,1,1) \). With \( \E = \diag(0,0,0,0,2,1) \), of rank \( 2 \), we get \( \A + \E = \I_6 \), so \( n_+ = 6 \). With \( \E = \diag(-2,-2,0,0,0,0) \), of rank \( 2 \), we get \( \A + \E = \diag(-1,-1,1,1,-1,0) \), so \( n_+ = 2 \).

(c) No. Negative definiteness would mean \( n_+(\A+\E) = 0 \), and \( \lvert 0 - 4\rvert = 4 > 2 \) contradicts @thm-inertia-rank-perturbation.
:::

:::: {#exr-inertia-revisited-b3}
[B3: A bordered matrix]

Let \( \D \in M_n(\nR) \) be symmetric and invertible, let \( \b \in \nR^n \) and \( c \in \nR \), and put \( \M = \begin{psmallmatrix} \D & \b \\ \b\tp & c\end{psmallmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Express \( \operatorname{In}(\M) \) in terms of \( \operatorname{In}(\D) \) and the scalar \( s = c - \b\tp\D^{-1}\b \).
2. Take \( \D = \diag(1,-1) \) and \( \b = (1,1) \). Compute \( \operatorname{In}(\M) \) for \( c = 0 \), \( c = 1 \) and \( c = -1 \).
3. For which \( c \) is \( \M \) singular?
:::
::::

::: {.solution}
(a) By @thm-haynsworth with \( \A = \D \), and \( \M/\D = s \) a \( 1\times1 \) matrix,
\[
\operatorname{In}(\M) = \operatorname{In}(\D) + \begin{cases} (1,0,0) & s > 0, \\ (0,1,0) & s < 0, \\ (0,0,1) & s = 0. \end{cases}
\]

(b) Here \( \D^{-1} = \diag(1,-1) = \D \), so \( \b\tp\D^{-1}\b = 1 - 1 = 0 \) and \( s = c \). Also \( \operatorname{In}(\D) = (1,1,0) \). Hence \( \operatorname{In}(\M) \) is \( (1,1,1) \) for \( c = 0 \), \( (2,1,0) \) for \( c = 1 \), and \( (1,2,0) \) for \( c = -1 \). The case \( c = 0 \) recovers @exr-sylvesters-law-of-inertia-c3 (c), which found the same triple by exhibiting the congruence directly.

(c) \( \M \) is singular exactly when \( n_0(\M) \ge 1 \), which by (a) happens exactly when \( s = 0 \), since \( \D \) is invertible and so contributes \( n_0(\D) = 0 \). Here that is \( c = 0 \).
:::

### C. Going deeper

:::: {#exr-inertia-revisited-c1}
[C1: How large can a subspace be on which the form vanishes?]

Let \( \A \in M_n(F) \) be Hermitian with \( \operatorname{In}(\A) = (n_+, n_-, n_0) \). Call a subspace \( W \le F^n \) **totally isotropic** for \( \A \) if \( \inner{\A\x}{\x} = 0 \) for every \( \x \in W \); for real symmetric \( \A \) this is the notion of Chapter 13 §07, in the form that section derives from polarization.

::: {.enumerate options="label=(\alph*)"}
1. Prove that every totally isotropic \( W \) satisfies \( \dim W \le n_0 + \min(n_+, n_-) \).
2. Construct a totally isotropic subspace of dimension exactly \( n_0 + \min(n_+, n_-) \).
3. Deduce that the largest dimension of a totally isotropic subspace equals \( n_0 \) if and only if \( \A \) is positive semidefinite or negative semidefinite.
:::

*Hint: for (a), a totally isotropic subspace satisfies both inequalities of @cor-inertia-subspace-characterization (b). For (b), pair up a positive eigenvector with a negative one.*
::::

::: {.solution}
(a) A totally isotropic \( W \) satisfies \( \inner{\A\x}{\x} \ge 0 \) throughout and also \( \inner{\A\x}{\x} \le 0 \) throughout. By @cor-inertia-subspace-characterization (b), the first gives \( \dim W \le n_+ + n_0 \) and the second \( \dim W \le n_- + n_0 \). Hence \( \dim W \le n_0 + \min(n_+, n_-) \).

(b) Fix an orthonormal eigenbasis \( \q_1, \dots, \q_n \) with \( \A\q_i = \lambda_i\q_i \) and \( \lambda_1 \ge \dots \ge \lambda_n \) (@cor-spectral-complex-matrix, or @cor-spectral-real-matrix when \( F = \nR \)), so that \( \lambda_i > 0 \) for \( i \le n_+ \), \( \lambda_i = 0 \) for \( n_+ < i \le n_+ + n_0 \), and \( \lambda_i < 0 \) for \( i > n_+ + n_0 \). Put \( t = \min(n_+, n_-) \) and, for \( 1 \le j \le t \), let \( j' = n + 1 - j \). Then \( j \le n_+ \) and \( j' \ge n + 1 - n_- > n_+ + n_0 \), so \( \lambda_j > 0 > \lambda_{j'} \) and the indices \( 1, \dots, t,\ 1', \dots, t' \) are \( 2t \) distinct indices, none of them in the zero block. Put
\[
\x_j = \frac{\q_j}{\sqrt{\lambda_j}} + \frac{\q_{j'}}{\sqrt{-\lambda_{j'}}} \qquad (1 \le j \le t),
\]
and let \( W \) be spanned by \( \x_1, \dots, \x_t \) together with the \( n_0 \) vectors \( \q_i \) with \( \lambda_i = 0 \). These \( t + n_0 \) vectors are independent, since they are non-zero combinations of pairwise disjoint sets of vectors from a basis.

For \( \x \in W \) write \( \x = \sum_j c_j\x_j + \z \) with \( \A\z = \0 \). Then \( \A\x = \sum_j c_j\A\x_j \) with \( \A\x_j = \sqrt{\lambda_j}\,\q_j - \sqrt{-\lambda_{j'}}\,\q_{j'} \), and
\[
\inner{\A\x}{\x} = \x^{*}\A\x = \sum_{j,k}\conj{c_k}\,c_j\,\x_k^{*}\A\x_j + \sum_j c_j\,\z^{*}\A\x_j .
\]
Each \( \z^{*}\A\x_j = 0 \), because \( \z \) lies in the span of eigenvectors orthogonal to \( \q_j \) and \( \q_{j'} \). For \( k \ne j \), \( \x_k^{*}\A\x_j = 0 \), because \( \x_k \) and \( \A\x_j \) are combinations of disjoint sets of orthonormal vectors. And
\[
\x_j^{*}\A\x_j = \frac{\sqrt{\lambda_j}}{\sqrt{\lambda_j}} - \frac{\sqrt{-\lambda_{j'}}}{\sqrt{-\lambda_{j'}}} = 1 - 1 = 0 .
\]
Hence \( \inner{\A\x}{\x} = 0 \) for every \( \x \in W \), and \( W \) is totally isotropic of dimension \( n_0 + \min(n_+, n_-) \).

(c) By (a) and (b) the largest totally isotropic dimension is \( n_0 + \min(n_+, n_-) \), which equals \( n_0 \) exactly when \( \min(n_+, n_-) = 0 \), that is when \( n_- = 0 \) or \( n_+ = 0 \), that is when \( \A \succeq 0 \) or \( -\A \succeq 0 \) (@thm-psd-characterizations).
:::

:::: {#exr-inertia-revisited-c2}
[C2: The inertia of a Hermitian dilation]

Let \( \A \in M_{m\times n}(F) \) have rank \( r \), and let \( \cH(\A) = \begin{psmallmatrix} \0 & \A \\ \A^{*} & \0\end{psmallmatrix} \in M_{m+n}(F) \) be the Hermitian dilation of @prp-hermitian-dilation.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \operatorname{In}(\cH(\A)) = (r,\ r,\ m + n - 2r) \).
2. Deduce a formula for \( \rank\A \) in terms of the inertia of \( \cH(\A) \), and check that it gives \( \rank\0 = 0 \).
3. Verify (a) for \( \A = \begin{psmallmatrix} 1 & 0 & 2 \\ 0 & 1 & 1\end{psmallmatrix} \).
:::
::::

::: {.solution}
(a) By @prp-hermitian-dilation the eigenvalue list of \( \cH(\A) \) with multiplicity consists of \( \pm\sigma_i(\A) \) for \( 1 \le i \le p = \min(m,n) \), together with \( m + n - 2p \) zeros. Exactly \( r \) of the \( \sigma_i(\A) \) are non-zero (@thm-compact-svd), so the positive entries are the \( r \) numbers \( \sigma_1, \dots, \sigma_r \) and the negative entries are their negatives, giving \( n_+ = n_- = r \). The rest are zero: \( (m+n) - 2r \) of them. Hence \( \operatorname{In}(\cH(\A)) = (r, r, m+n-2r) \).

(b) \( \rank\A = n_+(\cH(\A)) = \tfrac12\bigl(\rank\cH(\A)\bigr) \), using \( n_+ + n_- = \rank \). For \( \A = \0 \) the dilation is the zero matrix of size \( m+n \), whose inertia is \( (0, 0, m+n) \), so the formula returns \( 0 \).

(c) Here \( m = 2 \), \( n = 3 \) and \( \rank\A = 2 \), since the first two columns are \( \e_1, \e_2 \). Also
\[
\A\A\tp = \begin{pmatrix} 5 & 2 \\ 2 & 2\end{pmatrix},
\]
of trace \( 7 \) and determinant \( 6 \), hence eigenvalues \( 6 \) and \( 1 \); so \( \sigma_1(\A) = \sqrt6 \) and \( \sigma_2(\A) = 1 \). By @prp-hermitian-dilation the eigenvalues of the \( 5\times5 \) matrix \( \cH(\A) \) are \( \pm\sqrt6, \pm1 \) and one \( 0 \), so \( \operatorname{In}(\cH(\A)) = (2, 2, 1) \), which is \( (r, r, m+n-2r) = (2, 2, 5-4) \).
:::

:::: {#exr-inertia-revisited-c3}
[C3: Inertia from the leading principal minors]

Let \( \M \in M_n(F) \) be Hermitian and suppose that every leading principal submatrix \( \M_k \in M_k(F) \) (rows and columns \( 1, \dots, k \)) is **invertible**, for \( k = 1, \dots, n \). Write \( d_k = \det\M_k \) and \( d_0 = 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that for \( 2 \le k \le n \) the Schur complement \( \M_k/\M_{k-1} \) is the scalar \( d_k/d_{k-1} \).
2. Deduce that \( \operatorname{In}(\M) = (n_+, n_-, 0) \), where \( n_- \) is the number of indices \( k \in \{1, \dots, n\} \) with \( d_k/d_{k-1} < 0 \) — that is, the number of **sign changes** in the sequence \( d_0, d_1, \dots, d_n \).
3. Apply this to the matrix \( \M \) of @exm-haynsworth-3x3 and compare.
:::

*Hint: for (b), induct on \( k \) using @thm-haynsworth.*
::::

::: {.solution}
(a) Write \( \M_k = \begin{psmallmatrix} \M_{k-1} & \b \\ \b^{*} & c\end{psmallmatrix} \). Since \( \M_{k-1} \) is invertible, \( \M_k/\M_{k-1} \) is defined and is a \( 1\times1 \) matrix, and @thm-schur-determinant (a) gives \( d_k = \det\M_k = \det\M_{k-1}\cdot(\M_k/\M_{k-1}) = d_{k-1}(\M_k/\M_{k-1}) \). As \( d_{k-1} \ne 0 \), dividing gives \( \M_k/\M_{k-1} = d_k/d_{k-1} \).

(b) Induct on \( k \). For \( k = 1 \), \( \M_1 = (d_1) \) is a non-zero real scalar (real because \( \M \) is Hermitian), and \( \operatorname{In}(\M_1) \) is \( (1,0,0) \) or \( (0,1,0) \) according to the sign of \( d_1/d_0 = d_1 \). For the step, \( \M_{k-1} \) is invertible, so @thm-haynsworth applies to \( \M_k \) with \( \A = \M_{k-1} \):
\[
\operatorname{In}(\M_k) = \operatorname{In}(\M_{k-1}) + \operatorname{In}(d_k/d_{k-1}) ,
\]
and the last term is \( (1,0,0) \) or \( (0,1,0) \) according to the sign of the ratio, which is non-zero. Summing from \( k = 1 \) to \( n \),
\[
\operatorname{In}(\M) = \operatorname{In}(\M_n) = \bigl(\#\{k : d_k/d_{k-1} > 0\},\ \#\{k : d_k/d_{k-1} < 0\},\ 0\bigr) ,
\]
and \( d_k/d_{k-1} < 0 \) says exactly that \( d_{k-1} \) and \( d_k \) have opposite signs. (Taking \( n_- = 0 \) here recovers the leading-minor criterion of @thm-pd-characterizations: all \( d_k > 0 \) if and only if \( \M \succ 0 \).)

(c) For \( \M = \begin{psmallmatrix} 1 & 1 & 2 \\ 1 & 2 & 3 \\ 2 & 3 & 1\end{psmallmatrix} \) the leading minors are \( d_1 = 1 \), \( d_2 = 2 - 1 = 1 \) and \( d_3 = -4 \), all non-zero, so (b) applies. The sequence \( d_0, d_1, d_2, d_3 = 1, 1, 1, -4 \) has exactly one sign change, at the last step. Hence \( n_- = 1 \), \( n_+ = 2 \) and \( \operatorname{In}(\M) = (2,1,0) \), agreeing with @exm-haynsworth-3x3 and with @exm-inertia-by-elimination.
:::
