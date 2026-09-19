# Deleting a Row and a Column

Take a Hermitian matrix, cross out the last row and the last column, and look at what is left. It is again Hermitian, one size smaller, and it has its own eigenvalues. Two lists of numbers are now in play, \( n \) of them and \( n - 1 \) of them, and they cannot be independent of each other: the smaller matrix is the larger one restricted to a hyperplane, and @thm-courant-fischer describes every eigenvalue by what happens on subspaces. Restricting the supply of subspaces can only make the description worse in one direction and better in the other, and the exact bookkeeping is this section's subject.

The answer is as tight as it could be. The \( n-1 \) eigenvalues of the corner fall into the \( n-1 \) gaps of the eigenvalues of the whole, one to a gap. Nothing stronger holds: every interlacing pattern actually occurs (Exercise C2 proves the case \( n = 2 \)).

**Throughout this section the field is \( \nR \) or \( \nC \), and every matrix whose eigenvalues are written down is Hermitian**, with eigenvalues real and indexed **decreasingly**. For an index set \( I \subseteq \{1, \dots, n\} \) we write \( \A_{I,I} \) for the **principal submatrix** of \( \A \) on the rows and columns indexed by \( I \), as in @def-submatrix-minor. A principal submatrix of a Hermitian matrix is Hermitian, since \( (\A_{I,I})^{*} = (\A^{*})_{I,I} = \A_{I,I} \).

## A matrix restricted to a coordinate hyperplane

Deleting row \( m \) and column \( m \) is not an arbitrary mutilation of \( \A \). It is what \( \A \) looks like to vectors whose \( m \)-th coordinate is zero, and that is the only observation the proof needs.

::: {#lem-coordinate-compression}
[Deleting a Row and a Column Is Restricting to a Hyperplane]

Let \( \A \in M_n(F) \) be Hermitian with \( n \ge 2 \), fix \( m \) with \( 1 \le m \le n \), put \( I = \{1, \dots, n\}\setminus\{m\} \) and \( \B = \A_{I,I} \in M_{n-1}(F) \). Let
\[
H = \{\x \in F^n : x_m = 0\} ,
\]
and let \( \varphi \colon H \to F^{n-1} \) delete the \( m \)-th coordinate. Then \( \varphi \) is a linear isomorphism, and for every \( \x \in H \),
\[
\inner{\A\x}{\x} = \inner{\B\varphi(\x)}{\varphi(\x)}, \qquad \norm{\x} = \norm{\varphi(\x)} .
\]
In particular \( R_{\A}(\x) = R_{\B}(\varphi(\x)) \) for every \( \x \in H \) with \( \x \ne \0 \).
:::

::: {.proof}
The map \( \varphi \) is linear, being given by deleting a coordinate, and it is bijective from \( H \) to \( F^{n-1} \) because inserting \( 0 \) in position \( m \) inverts it. Write \( I = \{i_1 < \dots < i_{n-1}\} \), so that \( \varphi(\x)_r = x_{i_r} \) and \( (\B)_{rs} = a_{i_r i_s} \) by @def-submatrix-minor.

Let \( \x \in H \). Expanding the inner product of \( F^n \), which is linear in the first slot and conjugate-linear in the second,
\[
\inner{\A\x}{\x} = \sum_{p=1}^{n}\sum_{q=1}^{n} a_{pq}\,x_q\,\conj{x_p} .
\]
Every term with \( p = m \) or \( q = m \) vanishes, because \( x_m = 0 \). The remaining terms are indexed by \( p, q \in I \), say \( p = i_r \) and \( q = i_s \), and there the summand is \( a_{i_ri_s}\varphi(\x)_s\conj{\varphi(\x)_r} = (\B)_{rs}\varphi(\x)_s\conj{\varphi(\x)_r} \). Summing over \( r, s \) gives \( \inner{\B\varphi(\x)}{\varphi(\x)} \). The same deletion of a zero coordinate gives \( \norm{\x}^2 = \sum_{p \ne m}\lvert x_p\rvert^2 = \norm{\varphi(\x)}^2 \). Dividing the first identity by the second, which is positive when \( \x \ne \0 \), gives the statement about the Rayleigh quotients (@def-rayleigh-quotient). This proves the lemma.
:::

Because \( \varphi \) is an isomorphism, it matches the \( k \)-dimensional subspaces of \( H \) with the \( k \)-dimensional subspaces of \( F^{n-1} \), for every \( k \). So a statement about \( R_{\B} \) on subspaces of \( F^{n-1} \) *is* a statement about \( R_{\A} \) on subspaces of \( H \), and the only thing lost in passing from \( \A \) to \( \B \) is the subspaces of \( F^n \) that are not inside \( H \).

## Interlacing

::: {#thm-cauchy-interlacing}
[Cauchy's Interlacing Theorem]

Let \( \A \in M_n(F) \) be Hermitian with \( n \ge 2 \), let \( I \subseteq \{1, \dots, n\} \) with \( \lvert I\rvert = n-1 \), and let \( \B = \A_{I,I} \). Then
\[
\lambda_k(\A) \ \ge\ \lambda_k(\B) \ \ge\ \lambda_{k+1}(\A)
\qquad (1 \le k \le n-1) ,
\]
that is,
\[
\lambda_1(\A) \ge \lambda_1(\B) \ge \lambda_2(\A) \ge \lambda_2(\B) \ge \dots \ge \lambda_{n-1}(\B) \ge \lambda_n(\A) .
\]
:::

::: {.idea}
Both halves of @thm-courant-fischer are used, one for each inequality, and each time the move is the same: a subspace of \( H \) is also a subspace of \( F^n \).

① For \( \lambda_k(\B) \le \lambda_k(\A) \) use the **max–min** form. The best \( k \)-dimensional subspace for \( \B \) lives inside \( H \); transplanted to \( F^n \) it is one competitor among more, so the maximum over all of them is at least as large.

② For \( \lambda_{k+1}(\A) \le \lambda_k(\B) \) use the **min–max** form, and count dimensions. The best subspace for \( \B \) there has dimension \( (n-1) - k + 1 = n-k \), and \( n - k = n - (k+1) + 1 \) is exactly the dimension the min–max form for \( \lambda_{k+1}(\A) \) asks for. So the same subspace, viewed in \( F^n \), is admissible for \( \A \) at the index \( k+1 \).

The dimension count that makes min–max work at all is @lem-subspace-intersection, and it has already been spent inside @thm-courant-fischer; nothing more is needed here than the coincidence of the two numbers in ②.
:::

::: {.proof}
Let \( m \) be the index not in \( I \), and let \( H \) and \( \varphi \) be as in @lem-coordinate-compression, so that \( R_{\A}(\x) = R_{\B}(\varphi(\x)) \) for every non-zero \( \x \in H \). Both \( \A \) and \( \B \) are Hermitian, so @thm-courant-fischer applies to each, to \( \A \) with \( n \) and to \( \B \) with \( n-1 \) in the role of the size. Fix \( k \) with \( 1 \le k \le n-1 \).

\( (\lambda_k(\B) \le \lambda_k(\A)) \) By the max–min form of @thm-courant-fischer for \( \B \), there is a subspace \( W' \le F^{n-1} \) with \( \dim W' = k \) and
\[
\lambda_k(\B) = \min_{\0 \ne \y \in W'} R_{\B}(\y) .
\]
Put \( W = \varphi^{-1}(W') \le H \le F^n \). Since \( \varphi \) is an isomorphism, \( \dim W = k \), and \( \varphi \) carries the non-zero vectors of \( W \) onto the non-zero vectors of \( W' \), so
\[
\min_{\0 \ne \x \in W} R_{\A}(\x) = \min_{\0 \ne \y \in W'} R_{\B}(\y) = \lambda_k(\B) .
\]
Now \( W \) is one of the \( k \)-dimensional subspaces of \( F^n \) over which the max–min form for \( \A \) takes its maximum, so \( \lambda_k(\A) \ge \lambda_k(\B) \).

\( (\lambda_{k+1}(\A) \le \lambda_k(\B)) \) By the min–max form of @thm-courant-fischer for \( \B \), whose matrices have size \( n-1 \), there is a subspace \( W' \le F^{n-1} \) with \( \dim W' = (n-1)-k+1 = n-k \) and
\[
\lambda_k(\B) = \max_{\0 \ne \y \in W'} R_{\B}(\y) .
\]
Put \( W = \varphi^{-1}(W') \le F^n \), of dimension \( n-k \). Since \( 1 \le k+1 \le n \) and \( n - (k+1) + 1 = n-k = \dim W \), the subspace \( W \) is admissible in the min–max form for \( \lambda_{k+1}(\A) \), and that form takes the minimum over all such subspaces. Hence
\[
\lambda_{k+1}(\A) \ \le\ \max_{\0 \ne \x \in W} R_{\A}(\x) = \max_{\0 \ne \y \in W'} R_{\B}(\y) = \lambda_k(\B) .
\]
This proves the theorem.
:::

The picture to keep is one of nesting. The interval \( [\lambda_n(\A), \lambda_1(\A)] \) contains the interval \( [\lambda_{n-1}(\B), \lambda_1(\B)] \), and inside it the two lists alternate, an eigenvalue of \( \B \) between each consecutive pair of eigenvalues of \( \A \). Deleting a row and a column can only shrink the spectrum inward, never spread it out.

::: {.check}
Both inequalities in @thm-cauchy-interlacing can be equalities. Give a matrix \( \A \) for which \( \lambda_1(\A) = \lambda_1(\B) \), and one for which \( \lambda_1(\B) = \lambda_2(\A) \).
:::

::: {.solution}
For the first, \( \A = \I_2 \) with \( I = \{1\} \): then \( \B = (1) \) and \( \lambda_1(\A) = \lambda_1(\B) = 1 \). For the second, \( \A = \diag(1, 0) \) with \( I = \{2\} \): then \( \B = (0) \), and \( \lambda_1(\B) = 0 = \lambda_2(\A) \). Nothing in the theorem forces a gap; when a gap is forced is exactly the question settled later in this section.
:::

Deleting one index at a time and iterating gives the general statement.

::: {#cor-interlacing-general-submatrix}
[Deleting \( m \) Rows and the Same \( m \) Columns]

Let \( \A \in M_n(F) \) be Hermitian, let \( 0 \le m \le n-1 \), let \( I \subseteq \{1,\dots,n\} \) with \( \lvert I\rvert = n - m \), and let \( \B = \A_{I,I} \). Then
\[
\lambda_i(\A) \ \ge\ \lambda_i(\B) \ \ge\ \lambda_{i+m}(\A)
\qquad (1 \le i \le n-m) .
\]
:::

::: {.proof}
Induction on \( m \). For \( m = 0 \) we have \( \B = \A \) and both inequalities are equalities.

Let \( m \ge 1 \) and suppose the statement holds for \( m - 1 \), for every Hermitian matrix. Choose an index \( j \notin I \) and put \( I' = I \cup \{j\} \), so \( \lvert I'\rvert = n - m + 1 \), and \( \B' = \A_{I', I'} \in M_{n-m+1}(F) \), which is Hermitian. Since \( I \subseteq I' \), taking the principal submatrix on \( I \) of \( \B' \) means keeping the rows and columns of \( \A \) indexed by \( I \), so \( (\B')_{I,I} = \B \) after relabeling the indices of \( I \) inside \( I' \); and \( \lvert I \rvert = \lvert I'\rvert - 1 \).

Fix \( i \) with \( 1 \le i \le n-m \). By the inductive hypothesis applied to \( \A \) and \( \B' \),
\[
\lambda_i(\A) \ \ge\ \lambda_i(\B') \ \ge\ \lambda_{i+m-1}(\A) ,
\]
which is available because \( i \le n-m < n-m+1 \). By @thm-cauchy-interlacing applied to \( \B' \) and its principal submatrix \( \B \), which is one size smaller,
\[
\lambda_k(\B') \ \ge\ \lambda_k(\B) \ \ge\ \lambda_{k+1}(\B')
\qquad (1 \le k \le n-m) .
\]
Combining, \( \lambda_i(\B) \le \lambda_i(\B') \le \lambda_i(\A) \), which is the first inequality. For the second, take \( k = i \) in the display above and then use the inductive hypothesis at the index \( i+1 \), legitimate since \( i + 1 \le n - m + 1 \):
\[
\lambda_i(\B) \ \ge\ \lambda_{i+1}(\B') \ \ge\ \lambda_{(i+1)+m-1}(\A) = \lambda_{i+m}(\A) .
\]
This proves the corollary.
:::

The extreme case \( m = n-1 \) is worth writing down, because it recovers a fact about diagonal entries that also follows from Chapter 12's description of the extreme eigenvalues.

::: {#exm-diagonal-entries-interlace}
[The diagonal lies inside the spectrum]

Let \( \A \in M_n(F) \) be Hermitian. Show that \( \lambda_n(\A) \le a_{ii} \le \lambda_1(\A) \) for every \( i \).
:::

::: {.solution}
Take \( I = \{i\} \), so \( m = n-1 \) and \( \B = \A_{I,I} = (a_{ii}) \), a \( 1 \times 1 \) Hermitian matrix whose single eigenvalue is \( a_{ii} \) — real, as a diagonal entry of a Hermitian matrix must be. @cor-interlacing-general-submatrix at \( i = 1 \) gives
\[
\lambda_1(\A) \ \ge\ \lambda_1(\B) = a_{ii} \ \ge\ \lambda_{1 + (n-1)}(\A) = \lambda_n(\A) .
\]
The same conclusion follows from @lem-extreme-eigenvalues-quadratic-form applied to the unit vector \( \e_i \), since \( \inner{\A\e_i}{\e_i} = a_{ii} \). What interlacing adds is the version for larger index sets: any \( k \) diagonal entries are the diagonal of a \( k \times k \) principal submatrix, whose \( i \)-th eigenvalue is trapped between \( \lambda_{i + n - k}(\A) \) and \( \lambda_i(\A) \). How much more can be said about the diagonal of a Hermitian matrix, given its spectrum, is the subject of Section 8.
:::

## When is the interlacing strict?

@thm-cauchy-interlacing allows equalities, and the Quick check produced them. Deciding when they occur is the delicate part of the subject, and it is easiest to see when the deleted index is the last one, so that \( \A \) is presented as \( \B \) with a border added.

::: {#thm-bordered-matrix}
[Bordering a Hermitian Matrix]

Let \( \B \in M_{n-1}(F) \) be Hermitian with \( n \ge 2 \), let \( \b \in F^{n-1} \), let \( c \in \nR \), and let
\[
\A = \begin{pmatrix} \B & \b \\ \b^{*} & c \end{pmatrix} \in M_n(F) ,
\]
which is Hermitian and has \( \A_{I,I} = \B \) for \( I = \{1, \dots, n-1\} \). For an eigenvalue \( \nu \) of \( \B \), write \( P_{\nu} \) for the orthogonal projection of \( F^{n-1} \) onto the eigenspace \( E_{\nu}(\B) \), and \( m_{\nu} = \dim E_{\nu}(\B) \).

::: {.enumerate options="label=(\alph*)"}
1. If \( P_{\nu}\b \ne \0 \), then \( \nu \) is a root of \( p_{\A} \) of multiplicity **exactly** \( m_{\nu} - 1 \); in particular, if \( m_{\nu} = 1 \) then \( \nu \) is not an eigenvalue of \( \A \).
2. If \( P_{\nu}\b = \0 \), then \( \nu \) is a root of \( p_{\A} \) of multiplicity **at least** \( m_{\nu} \).
3. The interlacing \( \lambda_1(\A) \ge \lambda_1(\B) \ge \dots \ge \lambda_{n-1}(\B) \ge \lambda_n(\A) \) is strict at every one of its \( 2(n-1) \) inequalities if and only if \( \B \) has \( n-1 \) **distinct** eigenvalues **and** \( P_{\nu}\b \ne \0 \) for every eigenvalue \( \nu \) of \( \B \).
:::
:::

::: {.idea}
Write the characteristic polynomial of \( \A \) down. With \( \B \) diagonalized, a Schur complement turns \( \det(x\I - \A) \) into
\[
\Bigl(\prod_k (x - \mu_k)\Bigr)\Bigl( (x - c) - \sum_k \frac{\lvert \tilde b_k\rvert^2}{x - \mu_k}\Bigr) ,
\]
and clearing the denominators leaves a polynomial identity in which each \( \mu_k \) appears with one factor fewer than one might expect — provided \( P_{\nu}\b \ne \0 \), that is, provided the \( \lvert \tilde b_k\rvert^2 \) over the group belonging to that eigenvalue do not all vanish (for a repeated eigenvalue the individual \( \tilde b_k \) depend on the choice of basis, but their sum does not). Part (c) then costs almost nothing: strict interlacing means the combined list of \( 2n-1 \) numbers is strictly decreasing, hence has no repetitions at all, and (a) and (b) say exactly which repetitions are possible.
:::

::: {.proof}
**Step 1: diagonalize the corner.** By the spectral theorem (@cor-spectral-complex-matrix over \( \nC \), @cor-spectral-real-matrix over \( \nR \)) write \( \B = \U\D\U^{*} \) with \( \U \in M_{n-1}(F) \) unitary and \( \D = \diag(\mu_1, \dots, \mu_{n-1}) \) carrying the eigenvalues of \( \B \) in decreasing order, the columns \( \u_1, \dots, \u_{n-1} \) of \( \U \) being an orthonormal basis of eigenvectors. Let \( \V = \begin{psmallmatrix} \U & \0 \\ \0^{*} & 1\end{psmallmatrix} \in M_n(F) \), which is unitary because \( \V^{*}\V = \I_n \). Multiplying in blocks (@thm-block-multiplication) gives
\[
\V^{*}\A\V = \begin{pmatrix} \D & \tilde\b \\ \tilde\b^{*} & c\end{pmatrix},
\qquad \tilde\b = \U^{*}\b .
\]
Similar matrices have the same characteristic polynomial (@thm-charpoly-similarity-invariant), so we may compute with the right-hand side. Moreover \( \tilde b_k = (\U^{*}\b)_k = \inner{\b}{\u_k} \), and the \( \u_k \) with \( \mu_k = \nu \) form an orthonormal basis of \( E_{\nu}(\B) \): they lie in it, and a vector \( \x = \sum_k c_k\u_k \) with \( \B\x = \nu\x \) has \( (\mu_k - \nu)c_k = 0 \) for every \( k \), so \( c_k = 0 \) unless \( \mu_k = \nu \). Hence exactly \( m_{\nu} \) of the \( \mu_k \) equal \( \nu \), and
\[
P_{\nu}\b = \sum_{k : \mu_k = \nu} \inner{\b}{\u_k}\,\u_k
\quad\text{and}\quad
\norm{P_{\nu}\b}^2 = \sum_{k : \mu_k = \nu}\lvert \tilde b_k\rvert^2 .
\]
In particular \( P_{\nu}\b = \0 \) exactly when \( \tilde b_k = 0 \) for every \( k \) with \( \mu_k = \nu \).

**Step 2: the characteristic polynomial.** We claim that, as polynomials in \( x \),
\[
\begin{aligned}
p_{\A}(x) &= (x - c)\prod_{k=1}^{n-1}(x - \mu_k) \\
&\qquad - \sum_{k=1}^{n-1}\lvert \tilde b_k\rvert^2 \prod_{l \ne k}(x - \mu_l) .
\end{aligned}
\]{#eq-bordered-determinant}

::: {.claim}
@eq-bordered-determinant holds.
:::

::: {.proof}
Fix a scalar \( x_0 \) that is not an eigenvalue of \( \B \). Then \( x_0\I_{n-1} - \D \) is invertible, being diagonal with non-zero diagonal entries, so @thm-schur-determinant (a), applied to
\[
\M = x_0\I_n - \V^{*}\A\V = \begin{pmatrix} x_0\I_{n-1} - \D & -\tilde\b \\ -\tilde\b^{*} & x_0 - c\end{pmatrix}
\]
with the invertible block in the top left, gives \( \det\M = \det(x_0\I - \D)\cdot\det(\M/(x_0\I-\D)) \), where the Schur complement is the \( 1 \times 1 \) matrix
\[
(x_0 - c) - (-\tilde\b^{*})(x_0\I - \D)^{-1}(-\tilde\b)
= (x_0 - c) - \sum_{k}\frac{\lvert \tilde b_k\rvert^2}{x_0 - \mu_k} .
\]
Multiplying out \( \det(x_0\I - \D) = \prod_k(x_0 - \mu_k) \) against this scalar, and canceling one factor \( (x_0 - \mu_k) \) in the \( k \)-th summand, gives exactly the right-hand side of @eq-bordered-determinant evaluated at \( x_0 \). So the two sides of @eq-bordered-determinant, which are polynomials of degree \( n \), agree at every scalar outside the finite set \( \spec(\B) \). Their difference is therefore a polynomial of degree at most \( n \) with infinitely many roots in \( F \), and a non-zero polynomial of degree at most \( n \) has at most \( n \) roots (@cor-root-bound-general); so the difference is zero.
:::

**Step 3: multiplicities.** Let \( \nu_1 > \dots > \nu_p \) be the distinct eigenvalues of \( \B \), with multiplicities \( m_1, \dots, m_p \) summing to \( n-1 \), and put \( \beta_t = \norm{P_{\nu_t}\b}^2 \). Grouping equal \( \mu_k \) in @eq-bordered-determinant — the product \( \prod_{l \ne k}(x - \mu_l) \) is the same for all \( k \) in one group, and the coefficients \( \lvert\tilde b_k\rvert^2 \) add up to \( \beta_t \) by Step 1 — turns it into
\[
\begin{aligned}
p_{\A}(x) &= (x-c)\prod_{t=1}^{p}(x-\nu_t)^{m_t} \\
&\qquad - \sum_{t=1}^{p}\beta_t\,(x-\nu_t)^{m_t - 1}\prod_{s \ne t}(x-\nu_s)^{m_s} .
\end{aligned}
\]
Fix \( t \). Every term on the right is divisible by \( (x - \nu_t)^{m_t-1} \), so \( p_{\A}(x) = (x-\nu_t)^{m_t-1}g(x) \) with
\[
\begin{aligned}
g(x) &= (x-c)(x-\nu_t)\prod_{s\ne t}(x-\nu_s)^{m_s} - \beta_t\prod_{s \ne t}(x-\nu_s)^{m_s} \\
&\qquad - \sum_{u \ne t}\beta_u\,(x-\nu_t)(x-\nu_u)^{m_u-1}\prod_{s \ne u, t}(x-\nu_s)^{m_s} .
\end{aligned}
\]
Evaluate at \( x = \nu_t \). The first term vanishes because of its factor \( (x - \nu_t) \), and so does every summand of the third, for the same reason. What is left is
\[
g(\nu_t) = -\beta_t\prod_{s \ne t}(\nu_t - \nu_s)^{m_s} ,
\]
and the product is non-zero because the \( \nu_s \) are distinct. So \( g(\nu_t) \ne 0 \) exactly when \( \beta_t \ne 0 \), that is, exactly when \( P_{\nu_t}\b \ne \0 \). In that case \( \nu_t \) is a root of \( p_{\A} \) of multiplicity exactly \( m_t - 1 \), which proves (a); in the other case \( (x - \nu_t) \) divides \( g \), so the multiplicity is at least \( m_t \), which proves (b).

**Step 4: strictness.** \( (\Leftarrow) \) Suppose \( \B \) has \( n-1 \) distinct eigenvalues, so every \( m_t = 1 \), and \( P_{\nu}\b \ne \0 \) for each of them. By (a), no eigenvalue of \( \B \) is an eigenvalue of \( \A \). @thm-cauchy-interlacing gives \( \lambda_k(\A) \ge \lambda_k(\B) \ge \lambda_{k+1}(\A) \) for each \( k \); since \( \lambda_k(\B) \) is an eigenvalue of \( \B \) and \( \lambda_k(\A) \), \( \lambda_{k+1}(\A) \) are eigenvalues of \( \A \), neither inequality can be an equality. So all \( 2(n-1) \) of them are strict.

\( (\Rightarrow) \) Suppose all of them are strict, that is,
\[
\lambda_1(\A) > \lambda_1(\B) > \lambda_2(\A) > \dots > \lambda_{n-1}(\B) > \lambda_n(\A) .
\]
Reading two steps at a time gives \( \lambda_k(\B) > \lambda_{k+1}(\A) > \lambda_{k+1}(\B) \) for \( 1 \le k \le n-2 \), so the eigenvalues of \( \B \) are distinct. And the displayed chain is strictly decreasing, so its \( 2n-1 \) entries are pairwise distinct; in particular no eigenvalue of \( \B \) is an eigenvalue of \( \A \). By (b), read as a contrapositive, \( P_{\nu}\b \ne \0 \) for every eigenvalue \( \nu \) of \( \B \). This proves the theorem.
:::

::: {.remark}
Part (b) is deliberately one-sided. When \( P_{\nu}\b = \0 \) the multiplicity of \( \nu \) in \( p_{\A} \) may be \( m_{\nu} \) or \( m_{\nu}+1 \) — never more, since by Cauchy interlacing \( q \) equal eigenvalues \( \nu \) of \( \A \) squeeze \( q - 1 \) eigenvalues of \( \B \) to \( \nu \) — and both occur: \( \B = \diag(3,1) \), \( \b = (0,1) \), \( c = 0 \) gives \( p_{\A}(x) = (x-3)(x^2 - x - 1) \), where \( 3 \) keeps multiplicity \( 1 = m_3 \); while \( \B = (\mu) \), \( \b = \0 \), \( c = \mu \) gives \( \A = \mu\I_2 \), where \( \mu \) has multiplicity \( 2 = m_{\mu} + 1 \). Deciding between the two needs the value of \( c \) as well, and @thm-bordered-matrix does not attempt it; what it does settle completely is the strictness question (c), which is what interlacing asks.
:::

::: {.warning}
**Strictness needs both clauses, and a non-zero border is not enough.** It is tempting to say that the interlacing is strict as soon as \( \b \ne \0 \), or as soon as \( \b \) meets every eigenspace of \( \B \). The first is wrong even when the eigenvalues of \( \B \) are distinct (Exercise B3(a)); the second fails exactly when \( \B \) has a repeated eigenvalue. Take \( \B = 2\I_2 \), \( \b = (1,1) \) and \( c = 2 \). Here \( \b \) has a non-zero component in the one eigenspace \( E_2(\B) = F^2 \), and yet \( \lambda_1(\B) = \lambda_2(\B) = 2 \), so the middle of the interlacing chain reads \( 2 \ge \lambda_2(\A) \ge 2 \) and \( \lambda_2(\A) = 2 \) with no freedom at all. A repeated eigenvalue of \( \B \) is passed on to \( \A \), by @thm-bordered-matrix (a) with \( m_{\nu} = 2 \).
:::

To apply @thm-bordered-matrix when the deleted index is not the last one, permute. Let \( I = \{i_1 < \dots < i_{n-1}\} = \{1,\dots,n\}\setminus\{m\} \), and let \( \P \) be the matrix with columns \( \e_{i_1}, \dots, \e_{i_{n-1}}, \e_m \), a permutation matrix. Its columns are orthonormal, so \( \P\tp\P = \I \) and \( \P \) is unitary (@lem-permutation-matrices (b)); hence \( \P\tp\A\P \) is Hermitian and similar to \( \A \), with the same eigenvalues. Its \( (r,s) \) entry is \( \e_{i_r}\tp\A\e_{i_s} = a_{i_ri_s} \) for \( r, s \le n-1 \), so its leading \( (n-1)\times(n-1) \) corner is \( \A_{I,I} \), and its border is the column \( (a_{i_1m}, \dots, a_{i_{n-1}m}) \) with corner entry \( a_{mm} \). So \( \P\tp\A\P \) is a bordered matrix with corner \( \A_{I,I} \), and @thm-bordered-matrix applies to it verbatim.

The strictness criterion pays a debt from Chapter 10. The solution of @exr-orthogonal-polynomials-c1 proved by hand that the roots of consecutive orthogonal polynomials interlace for degrees \( 1, 2, 3 \), and then said: "The general case is not proved this way. The coefficients \( a_k \) and \( b_k \) assemble into a symmetric tridiagonal matrix whose characteristic polynomial is \( p_k \), and the interlacing then follows from the interlacing theorem for the eigenvalues of a symmetric matrix and its leading submatrices, which is Chapter 16's business." Two things in that sentence were asserted, not proved: that the characteristic polynomial is \( p_k \), and that the interlacing is **strict**, which is what "exactly one root strictly between" demands. Plain @thm-cauchy-interlacing gives only \( \ge \). Strictness needs @thm-bordered-matrix (c), and (c) needs one fact about tridiagonal matrices.

::: {#lem-tridiagonal-eigenvector-ends}
[Eigenvectors of an Unreduced Tridiagonal Matrix]

Let \( \T \in M_k(\nR) \) be symmetric and tridiagonal, with every entry \( t_{i,i+1} = t_{i+1,i} \) (\( 1 \le i \le k-1 \)) **non-zero**. Then every eigenvector \( \u \) of \( \T \) has \( u_k \ne 0 \). Consequently every eigenspace of \( \T \) has dimension \( 1 \), so \( \T \) has \( k \) distinct eigenvalues.
:::

::: {.proof}
Let \( \T\u = \nu\u \) and suppose \( u_k = 0 \); we show \( \u = \0 \). If \( k = 1 \) this is immediate. Otherwise row \( k \) of \( \T\u = \nu\u \) reads \( t_{k,k-1}u_{k-1} + t_{kk}u_k = \nu u_k \), so \( t_{k,k-1}u_{k-1} = 0 \) and \( u_{k-1} = 0 \), since \( t_{k,k-1} \ne 0 \). Now suppose \( u_{i} = u_{i+1} = 0 \) for some \( 2 \le i \le k-1 \). Row \( i \) reads \( t_{i,i-1}u_{i-1} + t_{ii}u_i + t_{i,i+1}u_{i+1} = \nu u_i \), so \( t_{i,i-1}u_{i-1} = 0 \) and \( u_{i-1} = 0 \). Walking up from \( i = k-1 \) to \( i = 2 \) gives \( u_{k-2} = \dots = u_1 = 0 \), so \( \u = \0 \), and \( \u \) is not an eigenvector.

If some eigenspace \( E_{\nu}(\T) \) contained two independent vectors \( \u, \u' \), then \( u'_k\u - u_k\u' \) would be a non-zero vector of \( E_{\nu}(\T) \) — non-zero by independence, since \( u_k \ne 0 \) — with last coordinate \( 0 \), which we have just excluded. So each eigenspace is a line. Since \( \T \) is real symmetric, its eigenspaces have dimensions adding up to \( k \) (@cor-spectral-real-matrix), so there are \( k \) of them, that is, \( k \) distinct eigenvalues. This proves the lemma.
:::

::: {#cor-orthogonal-polynomial-zeros-interlace}
[Zeros of Orthogonal Polynomials Interlace]

Let \( (p_k) \) be the monic orthogonal polynomial sequence of an inner product on \( \nR[x] \) to which @thm-three-term-recurrence applies, with coefficients \( a_k \) and \( b_k > 0 \); for the node inner product on \( \nR[x]_{\le n} \) read everything below for \( k + 1 \le n \). For \( k \ge 1 \) let \( \T_k \) (the **Jacobi matrix** of the sequence) be the \( k \times k \) real symmetric tridiagonal matrix with diagonal \( a_0, a_1, \dots, a_{k-1} \) and entries \( \sqrt{b_1}, \dots, \sqrt{b_{k-1}} \) just above and just below it.

::: {.enumerate options="label=(\alph*)"}
1. \( p_{\T_k} = p_k \); so the roots of \( p_k \) are the eigenvalues of \( \T_k \), and they are real and distinct.
2. If \( r_1 > \dots > r_{k+1} \) are the roots of \( p_{k+1} \) and \( s_1 > \dots > s_k \) those of \( p_k \), then
\[
r_1 > s_1 > r_2 > s_2 > \dots > s_k > r_{k+1} .
\]
:::
:::


::: {.idea}
The polynomials \( p_k \) are the characteristic polynomials of a nested family of symmetric tridiagonal matrices, each the leading corner of the next. So their zeros are eigenvalues of a matrix and of its corner, and Cauchy interlacing applies at once — non-strictly. Strictness is the bordered-matrix criterion, and both of its clauses come from one fact about tridiagonal matrices with non-zero off-diagonal entries: an eigenvector can never end in a zero.
:::

::: {.proof}
(a) Put \( D_k(x) = \det(x\I_k - \T_k) \) and \( D_0 = 1 \). For each real \( x_0 \), the matrix \( x_0\I_k - \T_k \) is tridiagonal in the sense of Chapter 6, with diagonal entries \( x_0 - a_{i-1} \) and off-diagonal entries \( -\sqrt{b_i} \) in both positions \( (i, i+1) \) and \( (i+1, i) \), so @thm-tridiagonal-recurrence gives \( D_1(x_0) = x_0 - a_0 \) and
\[
\begin{aligned}
D_{k+1}(x_0) &= (x_0 - a_k)D_k(x_0) - (-\sqrt{b_k})^2 D_{k-1}(x_0) \\
&= (x_0 - a_k)D_k(x_0) - b_kD_{k-1}(x_0)
\end{aligned}
\]
for \( k \ge 1 \). Here \( D_k(x_0) = \det(x_0\I - \T_k) \) is the characteristic polynomial evaluated at \( x_0 \) (@lem-charpoly-evaluation), and two real polynomials that agree at every real number are equal (@thm-polynomial-function-determines-polynomial (b)), so these identities hold as polynomials. They are the recurrence of @thm-three-term-recurrence with the same starting values \( p_0 = 1 \), \( p_1 = x - a_0 \), so \( D_k = p_k \) for every \( k \) by induction. The roots of \( p_{\T_k} \) are the eigenvalues of \( \T_k \) (@thm-eigenvalue-characterizations), which are real because \( \T_k \) is real symmetric (@thm-self-adjoint-real-eigenvalues) and distinct by @lem-tridiagonal-eigenvector-ends, whose hypothesis holds because every \( \sqrt{b_i} > 0 \).

(b) Write \( \T_{k+1} \) in bordered form:
\[
\T_{k+1} = \begin{pmatrix} \T_k & \sqrt{b_k}\,\e_k \\ \sqrt{b_k}\,\e_k\tp & a_k \end{pmatrix}, \qquad \e_k \in \nR^k .
\]
The border of \( \T_{k+1} \) is \( \w = \sqrt{b_k}\,\e_k \), whose \( k \)-th entry is \( \sqrt{b_k} \). We call it \( \w \) rather than \( \b \) because \( b_k \) already names a recurrence coefficient. We check the two clauses of @thm-bordered-matrix (c) for \( \B = \T_k \), with \( \w \) in place of \( \b \). By @lem-tridiagonal-eigenvector-ends, \( \T_k \) has \( k \) distinct eigenvalues. For each eigenvalue \( \nu \), the eigenspace \( E_{\nu}(\T_k) \) is spanned by one unit vector \( \u \), so \( P_{\nu}\w = \inner{\w}{\u}\u = \sqrt{b_k}\,u_k\,\u \), which is non-zero because \( b_k > 0 \) and \( u_k \ne 0 \) by the same lemma. So @thm-bordered-matrix (c) applies, and the eigenvalues of \( \T_{k+1} \) and of \( \T_k \) interlace strictly. By (a) these are the roots of \( p_{k+1} \) and of \( p_k \). This proves the corollary.
:::

Part (a) gives a second proof, with no integrals, that the roots of \( p_k \) are real and simple — half of @thm-orthogonal-polynomial-roots. The other half, that they lie inside the interval of the weight, is not visible in the matrix and still needs the argument of Chapter 10. For the monic Legendre polynomials of @exm-legendre-recurrence, \( a_k = 0 \), \( b_1 = \tfrac13 \) and \( b_2 = \tfrac4{15} \), so
\[
\T_3 = \begin{pmatrix} 0 & 1/\sqrt3 & 0 \\ 1/\sqrt3 & 0 & 2/\sqrt{15} \\ 0 & 2/\sqrt{15} & 0 \end{pmatrix} ,
\]
and expanding along the first row,
\[
p_{\T_3}(x) = x^3 - \bigl(\tfrac13 + \tfrac4{15}\bigr)x = x^3 - \tfrac35 x = p_3 .
\]
Its leading corner \( \T_2 \) has characteristic polynomial \( x^2 - \tfrac13 = p_2 \) and unit eigenvectors \( \tfrac1{\sqrt2}(1, \pm 1) \), both with non-zero last coordinate, so the border \( \tfrac{2}{\sqrt{15}}\e_2 \) meets both eigenspaces. The prediction is strict interlacing, and indeed
\[
\sqrt{3/5} > 1/\sqrt3 > 0 > -1/\sqrt3 > -\sqrt{3/5} ,
\]
that is \( 0.7746 > 0.5774 > 0 > -0.5774 > -0.7746 \), where the strict comparisons \( 3/5 > 1/3 \) and \( 1/\sqrt3 > 0 \) need no decimals.

## A worked example

::: {#exm-interlacing-3x3}
[One matrix and all three of its corners]

Let
\[
\A = \begin{pmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2 \end{pmatrix} .
\]
Compute the eigenvalues of \( \A \) and of each of its three \( 2 \times 2 \) principal submatrices, exhibit the interlacing in each case, and explain the pattern of strict and non-strict inequalities using @thm-bordered-matrix.
:::

::: {.solution}
*The eigenvalues of \( \A \).* Expanding \( \det(x\I - \A) \) along the first row,
\[
\begin{aligned}
p_{\A}(x)
&= (x-2)\bigl[(x-2)^2 - 1\bigr] + 1\cdot\bigl[-(x-2)\bigr] \\
&= (x-2)\bigl[(x-2)^2 - 2\bigr] ,
\end{aligned}
\]
so
\[
\lambda(\A) = \bigl(2+\sqrt2,\ 2,\ 2-\sqrt2\bigr) \approx (3.41421,\ 2,\ 0.58579) .
\]

*The three corners.* With \( I \) the index set kept,
\[
\A_{\{1,2\},\{1,2\}} = \begin{pmatrix} 2 & 1 \\ 1 & 2\end{pmatrix},
\quad
\A_{\{1,3\},\{1,3\}} = \begin{pmatrix} 2 & 0 \\ 0 & 2\end{pmatrix},
\quad
\A_{\{2,3\},\{2,3\}} = \begin{pmatrix} 2 & 1 \\ 1 & 2\end{pmatrix} .
\]
A matrix \( \begin{psmallmatrix} 2 & 1 \\ 1 & 2\end{psmallmatrix} \) has trace \( 4 \) and determinant \( 3 \), so its eigenvalues are \( 3 \) and \( 1 \); and \( 2\I_2 \) has the eigenvalue \( 2 \) twice.

*The interlacing.* In all three cases @thm-cauchy-interlacing is confirmed:
\[
\begin{aligned}
I = \{1,2\} &: \quad 3.41421 > 3 > 2 > 1 > 0.58579, \\
I = \{1,3\} &: \quad 3.41421 > 2 = 2 = 2 > 0.58579, \\
I = \{2,3\} &: \quad 3.41421 > 3 > 2 > 1 > 0.58579 .
\end{aligned}
\]
The first and third are strict everywhere; the second has two equalities in the middle. The exact comparisons need no decimals: \( 2 + \sqrt2 > 3 \) is \( \sqrt2 > 1 \), and \( 1 > 2 - \sqrt2 \) is \( \sqrt2 > 1 \) again.

*Why.* Read \( \A \) as a bordered matrix in each case, using the permutation remark above.

For \( I = \{1,2\} \) the deleted index is already the last one, so \( \B = \begin{psmallmatrix} 2&1\\1&2\end{psmallmatrix} \), \( \b = (0, 1) \) and \( c = 2 \). The eigenvalues \( 3 \) and \( 1 \) of \( \B \) are distinct, with unit eigenvectors \( \tfrac1{\sqrt2}(1,1) \) and \( \tfrac1{\sqrt2}(1,-1) \). Both inner products with \( \b \) are non-zero:
\[
\inner{\b}{\tfrac1{\sqrt2}(1,1)} = \tfrac1{\sqrt2}, \qquad
\inner{\b}{\tfrac1{\sqrt2}(1,-1)} = -\tfrac1{\sqrt2} .
\]
So both clauses of @thm-bordered-matrix (c) hold and the interlacing is strict, as computed. The case \( I = \{2,3\} \) is the same: moving index \( 1 \) to the end gives the corner \( \begin{psmallmatrix} 2&1\\1&2\end{psmallmatrix} \) again, with border \( (a_{21}, a_{31}) = (1, 0) \), whose inner products with the two unit eigenvectors \( \tfrac1{\sqrt2}(1, \pm 1) \) are both \( \tfrac1{\sqrt2} \), non-zero.

For \( I = \{1,3\} \) the deleted index is \( 2 \). Conjugating by the permutation matrix that sends the coordinate order \( (1,2,3) \) to \( (1,3,2) \) turns \( \A \) into
\[
\begin{pmatrix} 2 & 0 & 1 \\ 0 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix},
\qquad \B = 2\I_2, \quad \b = (1,1), \quad c = 2 .
\]
Here \( \b \ne \0 \) and \( P_2\b = \b \ne \0 \), so the first clause of @thm-bordered-matrix (c) is the one that fails: \( \B \) has the repeated eigenvalue \( 2 \). Part (a) with \( m_2 = 2 \) then says that \( 2 \) is an eigenvalue of \( \A \) of multiplicity exactly \( 1 \), which is visible in \( p_{\A} \), and the interlacing collapses at the middle to \( 2 = 2 = 2 \). This is exactly the situation of the warning above, occurring inside a perfectly ordinary integer matrix.
:::

## Inertia under compression

Interlacing controls not only where the eigenvalues are but how many of them have each sign, and that is a statement about inertia.

::: {#cor-interlacing-inertia}
[A Principal Submatrix Keeps Most of the Inertia]

Let \( \A \in M_n(F) \) be Hermitian, let \( 0 \le m \le n-1 \), let \( \lvert I\rvert = n-m \) and \( \B = \A_{I,I} \). Write \( n_+(\M) \) and \( n_-(\M) \) for the number of positive and of negative eigenvalues of a Hermitian \( \M \), counted with multiplicity. Then
\[
n_+(\B) \le n_+(\A) \le n_+(\B) + m,
\qquad
n_-(\B) \le n_-(\A) \le n_-(\B) + m .
\]
In particular \( \A \succeq 0 \) implies \( \B \succeq 0 \), and \( \A \succ 0 \) implies \( \B \succ 0 \).
:::

::: {.proof}
Write \( r = n_+(\B) \) and \( s = n_+(\A) \), and abbreviate \( \lambda_i = \lambda_i(\A) \), \( \mu_i = \lambda_i(\B) \). By @cor-interlacing-general-submatrix, \( \lambda_i \ge \mu_i \ge \lambda_{i+m} \) for \( 1 \le i \le n-m \).

\( (n_+(\B) \le n_+(\A)) \) For \( i \le r \) we have \( \mu_i > 0 \), hence \( \lambda_i \ge \mu_i > 0 \). So \( \A \) has at least \( r \) positive eigenvalues.

\( (n_+(\A) \le n_+(\B) + m) \) If \( r + m \ge n \) there is nothing to prove, since \( s \le n \). Otherwise \( r + 1 \le n - m \), so the index \( i = r+1 \) is admissible and \( \mu_{r+1} \le 0 \) by the definition of \( r \); hence \( \lambda_{r+1+m} \le \mu_{r+1} \le 0 \), and the eigenvalues \( \lambda_{r+m+1}, \dots, \lambda_n \) are all \( \le 0 \) by the decreasing indexing. So \( s \le r + m \).

For the two statements about \( n_- \), apply what has just been proved to \( -\A \), whose principal submatrix on \( I \) is \( -\B \). By @lem-eigenvalues-of-negation the eigenvalue lists are negated and reversed, so \( n_+(-\A) = n_-(\A) \) and \( n_+(-\B) = n_-(\B) \), and the two displayed chains are the same statement.

Finally, \( \A \succeq 0 \) means every eigenvalue of \( \A \) is \( \ge 0 \) (@thm-psd-characterizations (b)), that is, \( n_-(\A) = 0 \); then \( n_-(\B) \le n_-(\A) = 0 \), so \( \B \succeq 0 \). And \( \A \succ 0 \) means \( n_+(\A) = n \) (@thm-pd-characterizations (b)); then \( n_+(\B) \ge n_+(\A) - m = n - m \), which is the size of \( \B \), so every eigenvalue of \( \B \) is positive and \( \B \succ 0 \). This proves the corollary.
:::

The last two sentences are a second proof of something Chapter 12 already knew. That a principal submatrix of a positive semidefinite matrix is positive semidefinite is the step (a) \( \Rightarrow \) (e) in the proof of @thm-psd-characterizations, where it comes from the observation that a principal submatrix is what the quadratic form does to vectors supported on the corresponding coordinates — one line, needing no interlacing. What is new here is the quantitative form. Sylvester's law of inertia (@thm-sylvester-inertia) says that the triple of counts is an invariant of a real symmetric matrix up to congruence, and @thm-inertia-from-eigenvalues identifies Chapter 13's counts with the eigenvalue counts \( n_+ \) and \( n_- \) used here; the corollary says that deleting \( m \) rows and the matching \( m \) columns can destroy at most \( m \) positive and at most \( m \) negative eigenvalues, and create none of either. Section 10 gives a second proof of Sylvester's law from Courant–Fischer, and bounds how far a low-rank perturbation can move the inertia.

## Interlacing is a Hermitian phenomenon

Everything above rests on @thm-courant-fischer, which rests on the quadratic form being real. Without the Hermitian hypothesis, nothing survives — not a weakened interlacing, not even a bound.

::: {#exm-interlacing-fails-nonhermitian}
[A corner outside the spectrum]

Let
\[
\A = \begin{pmatrix} 5 & 1 \\ -8 & -1\end{pmatrix} .
\]
Show that \( \A \) has real eigenvalues, so that the conclusion of @thm-cauchy-interlacing can be stated for it, and that the conclusion is false.
:::

::: {.solution}
\( \tr\A = 4 \) and \( \det\A = 5(-1) - 1(-8) = 3 \), so \( p_{\A}(x) = x^2 - 4x + 3 = (x-3)(x-1) \) and the eigenvalues are \( 3 \) and \( 1 \), both real. The two \( 1 \times 1 \) principal submatrices are \( \A_{\{1\},\{1\}} = (5) \) and \( \A_{\{2\},\{2\}} = (-1) \), with eigenvalues \( 5 \) and \( -1 \).

Interlacing would require \( 3 \ge 5 \ge 1 \) in the first case and \( 3 \ge -1 \ge 1 \) in the second. Both fail, and they fail on opposite sides: the diagonal entries \( 5 \) and \( -1 \) lie outside the interval \( [1, 3] \), which is the convex hull of the spectrum. For a Hermitian matrix that is impossible, by @exm-diagonal-entries-interlace.
:::

::: {.remark}
The failure is total, not marginal. For any \( a \in F \), the matrix
\[
\A_a = \begin{pmatrix} a & 1 \\ -(a-1)(a-3) & 4-a \end{pmatrix}
\]
has trace \( 4 \) and determinant \( a(4-a) + (a-1)(a-3) = 4a - a^2 + a^2 - 4a + 3 = 3 \), hence the same characteristic polynomial \( (x-3)(x-1) \) as above. Its \( (1,1) \) principal submatrix is \( (a) \). So a general matrix with spectrum \( \{1, 3\} \) can have any prescribed number whatsoever as its \( (1,1) \) entry: the eigenvalue of a single principal submatrix is subject to no constraint at all. (The two diagonal entries together still add up to the trace, \( 4 \); that constraint holds for every matrix and has nothing to do with interlacing.) The choice \( a = 5 \) recovers \( \A \), and \( a = 0 \) gives \( \begin{psmallmatrix} 0 & 1 \\ -3 & 4\end{psmallmatrix} \).
:::

::: {.warning}
**Principal means the same index set on both sides.** Interlacing says nothing about a submatrix obtained by deleting row \( i \) and column \( j \) with \( i \ne j \), even for a Hermitian \( \A \). Take \( \A = \begin{psmallmatrix} -10 & 1 \\ 1 & -10 \end{psmallmatrix} \), whose eigenvalues are \( -9 \) and \( -11 \). Deleting row \( 1 \) and column \( 2 \) leaves the \( 1 \times 1 \) matrix \( (1) \), and \( 1 \) is nowhere near \( [-11, -9] \). The submatrix in @thm-cauchy-interlacing is \( \A_{I,I} \), and the two \( I \)'s are not decoration.
:::

## Exercises

### A. Check your understanding

:::: {#exr-cauchy-interlacing-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State @thm-cauchy-interlacing, and say which hypothesis on \( \A \) and which hypothesis on the submatrix are used.
2. Let \( \A \in M_6(\nC) \) be Hermitian and let \( \B = \A_{I,I} \) with \( \lvert I\rvert = 4 \). Which eigenvalues of \( \A \) bound \( \lambda_3(\B) \) above and below?
3. Determine whether the following is correct, and justify your answer: if \( \b \ne \0 \) then the interlacing between \( \begin{psmallmatrix} \B & \b \\ \b^{*} & c\end{psmallmatrix} \) and \( \B \) is strict.
4. Explain why a principal submatrix of a positive semidefinite matrix is positive semidefinite, in one sentence, without using interlacing.
5. Give a \( 2 \times 2 \) matrix with real eigenvalues whose \( (1,1) \) entry is larger than both of them.
:::
::::

::: {.solution}
(a) See @thm-cauchy-interlacing. The matrix \( \A \) must be **Hermitian**, so that @thm-courant-fischer applies and the eigenvalues are real and can be put in order; and \( \B \) must be a **principal** submatrix, \( \B = \A_{I,I} \) with the same index set on rows and columns, so that @lem-coordinate-compression identifies \( R_{\B} \) with \( R_{\A} \) restricted to a coordinate hyperplane.

(b) Here \( n = 6 \) and \( m = 2 \), so @cor-interlacing-general-submatrix gives \( \lambda_3(\A) \ge \lambda_3(\B) \ge \lambda_5(\A) \).

(c) Incorrect. The warning after @thm-bordered-matrix gives \( \B = 2\I_2 \), \( \b = (1,1) \), \( c = 2 \), where \( \b \ne \0 \) and the interlacing is not strict, because \( \B \) has a repeated eigenvalue. The correct criterion is @thm-bordered-matrix (c), which needs distinct eigenvalues of \( \B \) as well as \( P_{\nu}\b \ne \0 \) for each \( \nu \).

(d) Because \( \inner{\B\y}{\y} = \inner{\A\x}{\x} \ge 0 \), where \( \x \in F^n \) is \( \y \) placed in the coordinates of \( I \) and \( 0 \) elsewhere (@lem-coordinate-compression); this is how @thm-psd-characterizations obtained its clause (e).

(e) \( \begin{psmallmatrix} 5 & 1 \\ -8 & -1\end{psmallmatrix} \), with eigenvalues \( 3 \) and \( 1 \) and \( (1,1) \) entry \( 5 \) (@exm-interlacing-fails-nonhermitian). It is necessarily non-Hermitian, by @exm-diagonal-entries-interlace.
:::

### B. Practice

:::: {#exr-cauchy-interlacing-b1}
[B1: Interlacing in integers]

Let
\[
\A = \begin{pmatrix} 0 & 1 & 2 \\ 1 & 0 & 2 \\ 2 & 2 & 3\end{pmatrix} .
\]
Compute the eigenvalues of \( \A \) and of all three of its \( 2\times 2 \) principal submatrices, and exhibit the interlacing in each case. Hence say, for each corner, whether the interlacing is strict.
::::

::: {.solution}
*The eigenvalues of \( \A \).* The vector \( (1,-1,0) \) satisfies \( \A(1,-1,0) = (-1, 1, 0) \), so \( -1 \) is an eigenvalue. Dividing, \( p_{\A}(x) = x^3 - 3x^2 - 9x - 5 = (x-5)(x+1)^2 \), so
\[
\lambda(\A) = (5,\ -1,\ -1) .
\]
(As a check, \( \tr\A = 3 = 5 - 1 - 1 \), and expanding along the first row \( \det\A = 0 - 1(3 - 4) + 2(2 - 0) = 5 = 5\cdot(-1)\cdot(-1) \).)

*The corners.*
\[
\A_{\{1,2\},\{1,2\}} = \begin{pmatrix} 0 & 1 \\ 1 & 0\end{pmatrix},
\qquad
\A_{\{1,3\},\{1,3\}} = \A_{\{2,3\},\{2,3\}} = \begin{pmatrix} 0 & 2 \\ 2 & 3\end{pmatrix} .
\]
The first has trace \( 0 \) and determinant \( -1 \), so its eigenvalues are \( 1 \) and \( -1 \). The second has trace \( 3 \) and determinant \( -4 \), so its characteristic polynomial is \( x^2 - 3x - 4 = (x-4)(x+1) \) and its eigenvalues are \( 4 \) and \( -1 \).

*Interlacing.*
\[
\begin{aligned}
I = \{1,2\} &: \quad 5 > 1 > -1 = -1 = -1, \\
I = \{1,3\} &: \quad 5 > 4 > -1 = -1 = -1, \\
I = \{2,3\} &: \quad 5 > 4 > -1 = -1 = -1 .
\end{aligned}
\]
No corner gives strict interlacing, and the reason is on the side of \( \A \): whichever index is deleted, \( \lambda_2(\A) = \lambda_3(\A) = -1 \), so the chain \( \lambda_2(\A) \ge \lambda_2(\B) \ge \lambda_3(\A) \) squeezes \( \lambda_2(\B) \) to \( -1 \). Strict interlacing would make the combined chain strictly decreasing, and so would force \( \A \) to have three distinct eigenvalues. @thm-bordered-matrix sees the same thing from the side of the corner. For \( I = \{1,2\} \) the border is \( \b = (2,2) \), orthogonal to \( (1,-1) \), which spans \( E_{-1}(\B) \); so \( P_{-1}\b = \0 \), and part (b) predicts that \( -1 \) is an eigenvalue of \( \A \). For \( I = \{1,3\} \) the border is \( (a_{12}, a_{32}) = (1, 2) \), orthogonal to \( (2,-1) \), which spans \( E_{-1} \) of \( \begin{psmallmatrix} 0&2\\2&3\end{psmallmatrix} \), with the same conclusion.
:::

:::: {#exr-cauchy-interlacing-b2}
[B2: Bounds without a characteristic polynomial]

Let \( \A \in M_4(\nR) \) be symmetric with
\[
\A = \begin{pmatrix} 7 & \ast & \ast & \ast \\ \ast & 2 & \ast & \ast \\ \ast & \ast & -3 & \ast \\ \ast & \ast & \ast & 1\end{pmatrix} ,
\]
the entries marked \( \ast \) being unknown.

::: {.enumerate options="label=(\alph*)"}
1. What do @cor-interlacing-general-submatrix and @exm-diagonal-entries-interlace say about \( \lambda_1(\A) \) and \( \lambda_4(\A) \)?
2. Suppose in addition that \( \A_{\{1,2\},\{1,2\}} = \begin{psmallmatrix} 7 & 4 \\ 4 & 2\end{psmallmatrix} \). Improve the lower bound on \( \lambda_1(\A) \), and give a lower bound on \( \lambda_2(\A) \).
:::
::::

::: {.solution}
(a) Each diagonal entry is a \( 1\times 1 \) principal submatrix, so \( \lambda_1(\A) \ge \max\{7, 2, -3, 1\} = 7 \) and \( \lambda_4(\A) \le \min\{7,2,-3,1\} = -3 \). In particular \( \A \) is indefinite whatever the unknown entries are.

(b) The submatrix \( \B = \begin{psmallmatrix} 7&4\\4&2\end{psmallmatrix} \) has trace \( 9 \) and determinant \( 14 - 16 = -2 \), so its characteristic polynomial is \( x^2 - 9x - 2 \) and its eigenvalues are
\[
\lambda_1(\B) = \tfrac{9 + \sqrt{89}}{2} \approx 9.2170,
\qquad
\lambda_2(\B) = \tfrac{9 - \sqrt{89}}{2} \approx -0.2170 .
\]
Here \( n = 4 \) and \( m = 2 \), and the left-hand inequality \( \lambda_i(\A) \ge \lambda_i(\B) \) of @cor-interlacing-general-submatrix at \( i = 1, 2 \) gives
\[
\lambda_1(\A) \ \ge\ \tfrac{9+\sqrt{89}}{2} \approx 9.2170,
\qquad
\lambda_2(\A) \ \ge\ \tfrac{9 - \sqrt{89}}{2} \approx -0.2170 .
\]
The first improves the bound \( 7 \) from (a). The second is new: the diagonal entries alone say nothing about \( \lambda_2(\A) \). The right-hand inequalities \( \lambda_i(\B) \ge \lambda_{i+2}(\A) \) give \( \lambda_3(\A) \le 9.2170 \), which is true but of little use, and \( \lambda_4(\A) \le -0.2170 \), which is weaker than the bound \( \lambda_4(\A) \le -3 \) of (a). Each principal submatrix contributes what it can, and one keeps the best of the bounds.
:::

:::: {#exr-cauchy-interlacing-b3}
[B3: Deciding strictness]

For each of the following bordered matrices \( \A = \begin{psmallmatrix} \B & \b \\ \b\tp & c \end{psmallmatrix} \), decide without computing \( p_{\A} \) whether the interlacing between \( \A \) and \( \B \) is strict, and justify with @thm-bordered-matrix.

::: {.enumerate options="label=(\alph*)"}
1. \( \B = \diag(3,1) \), \( \b = (0,1) \), \( c = 0 \).
2. \( \B = \diag(3,1) \), \( \b = (2,-1) \), \( c = 5 \).
3. \( \B = \begin{psmallmatrix} 4 & 0 \\ 0 & 4\end{psmallmatrix} \), \( \b = (1,2) \), \( c = 0 \).
:::
::::

::: {.solution}
In each case \( \B \) is diagonal, so the standard basis vectors are an orthonormal eigenbasis and \( P_{\nu}\b \) is just the part of \( \b \) in the coordinates where the diagonal entry equals \( \nu \).

(a) Not strict. The eigenvalues \( 3, 1 \) of \( \B \) are distinct, but \( P_3\b = (0,0) = \0 \). By @thm-bordered-matrix (b), \( 3 \) is an eigenvalue of \( \A \), so one of the inequalities \( \lambda_1(\A) \ge 3 \ge \lambda_2(\A) \) is an equality. (Indeed \( p_{\A}(x) = (x-3)(x^2 - x - 1) \).)

(b) Strict. The eigenvalues \( 3, 1 \) are distinct and \( P_3\b = (2,0) \ne \0 \), \( P_1\b = (0,-1) \ne \0 \). Both clauses of @thm-bordered-matrix (c) hold. (Indeed \( p_{\A}(x) = (x-2)(x^2 - 7x + 4) \), with roots \( \tfrac{7 + \sqrt{33}}{2} \approx 6.372 \), \( 2 \) and \( \tfrac{7 - \sqrt{33}}{2} \approx 0.628 \), and \( 6.372 > 3 > 2 > 1 > 0.628 \).)

(c) Not strict. \( P_4\b = \b = (1,2) \ne \0 \), so the second clause holds, but \( \B \) has the repeated eigenvalue \( 4 \) and the first clause fails. By @thm-bordered-matrix (a) with \( m_4 = 2 \), the number \( 4 \) is an eigenvalue of \( \A \) of multiplicity exactly \( 1 \), and the middle of the chain reads \( 4 \ge \lambda_2(\A) \ge 4 \). (Indeed \( p_{\A}(x) = (x-5)(x-4)(x+1) \).)
:::

### C. Going deeper

:::: {#exr-cauchy-interlacing-c1}
[C1: Rank under compression]

Let \( \A \in M_n(F) \) be Hermitian of rank \( r \), and let \( \B = \A_{I,I} \) with \( \lvert I\rvert = n-m \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \rank\B \ge r - 2m \).
2. Show that the bound is attained, by exhibiting for each \( n \) and each \( m \le n/2 \) a Hermitian \( \A \) of rank \( 2m \) with a principal submatrix of size \( n-m \) and rank \( 0 \).
:::
::::

::: {.solution}
(a) For a Hermitian matrix \( \M \), diagonalizing by the spectral theorem gives \( \rank\M = n_+(\M) + n_-(\M) \), the total number of non-zero eigenvalues. By @cor-interlacing-inertia, \( n_+(\B) \ge n_+(\A) - m \) and \( n_-(\B) \ge n_-(\A) - m \). Adding,
\[
\rank\B = n_+(\B) + n_-(\B) \ \ge\ \bigl(n_+(\A) + n_-(\A)\bigr) - 2m = r - 2m .
\]

(b) Let \( m \le n/2 \) and let \( I = \{m+1, m+2, \dots, n\} \), of size \( n - m \). Define \( \A \) by \( a_{i, m+i} = a_{m+i, i} = 1 \) for \( 1 \le i \le m \), and all other entries \( 0 \). Then \( \A \) is real symmetric. It is a direct sum of \( m \) copies of \( \begin{psmallmatrix} 0&1\\1&0\end{psmallmatrix} \), acting on the coordinate pairs \( \{i, m+i\} \), together with zeros on the remaining coordinates, so its eigenvalues are \( \pm 1 \) each \( m \) times and \( 0 \) otherwise; hence \( \rank\A = 2m \) and \( n_+(\A) = n_-(\A) = m \). Every non-zero entry of \( \A \) has one index in \( \{1,\dots,m\} \), which \( I \) omits, so \( \A_{I,I} = \0 \) and \( \rank\A_{I,I} = 0 = \rank\A - 2m \). The bound in (a) is therefore sharp for every \( m \).
:::

:::: {#exr-cauchy-interlacing-c2}
[C2: The converse, in the smallest case]

@thm-cauchy-interlacing says that the spectrum of a corner interlaces the spectrum of the whole. This exercise asks whether every interlacing pattern occurs.

::: {.enumerate options="label=(\alph*)"}
1. Let \( \lambda_1 > \mu_1 > \lambda_2 \) be real numbers. Find \( b \in \nR \) and \( c \in \nR \) such that \( \A = \begin{psmallmatrix} \mu_1 & b \\ b & c\end{psmallmatrix} \) has eigenvalues \( \lambda_1 \) and \( \lambda_2 \).
2. Deduce that for \( n = 2 \) the interlacing condition of @thm-cauchy-interlacing is not merely necessary but also sufficient.
3. Explain why the strict hypothesis \( \lambda_1 > \mu_1 > \lambda_2 \) may be relaxed to \( \lambda_1 \ge \mu_1 \ge \lambda_2 \).
:::

*Hint: match the trace and the determinant.*
::::

::: {.solution}
(a) A real symmetric \( 2 \times 2 \) matrix with eigenvalues \( \lambda_1, \lambda_2 \) must have \( \tr\A = \lambda_1 + \lambda_2 \) and \( \det\A = \lambda_1\lambda_2 \). The first forces
\[
c = \lambda_1 + \lambda_2 - \mu_1 ,
\]
and the second then forces \( \mu_1 c - b^2 = \lambda_1\lambda_2 \), that is,
\[
b^2 = \mu_1(\lambda_1 + \lambda_2 - \mu_1) - \lambda_1\lambda_2
= -(\mu_1 - \lambda_1)(\mu_1 - \lambda_2)
= (\lambda_1 - \mu_1)(\mu_1 - \lambda_2) ,
\]
where the middle equality is the expansion \( -(\mu_1^2 - (\lambda_1+\lambda_2)\mu_1 + \lambda_1\lambda_2) \). The hypothesis \( \lambda_1 > \mu_1 > \lambda_2 \) makes both factors positive, so \( b = \sqrt{(\lambda_1-\mu_1)(\mu_1-\lambda_2)} \) is a real number. With this \( b \) and \( c \), the matrix \( \A \) is real symmetric with the prescribed trace and determinant, hence with characteristic polynomial \( x^2 - (\lambda_1+\lambda_2)x + \lambda_1\lambda_2 = (x-\lambda_1)(x-\lambda_2) \), hence with eigenvalues \( \lambda_1 \) and \( \lambda_2 \).

For example \( \lambda_1 = 4 \), \( \mu_1 = 2 \), \( \lambda_2 = 1 \) gives \( c = 3 \) and \( b^2 = 2 \), that is \( \A = \begin{psmallmatrix} 2 & \sqrt2 \\ \sqrt2 & 3\end{psmallmatrix} \), whose trace is \( 5 \) and determinant \( 6 - 2 = 4 \), as required.

(b) Necessity is @thm-cauchy-interlacing with \( n = 2 \) and \( I = \{1\} \). Sufficiency is part (a): given any \( \lambda_1 > \mu_1 > \lambda_2 \), a Hermitian \( \A \) with spectrum \( \{\lambda_1, \lambda_2\} \) and \( \A_{\{1\},\{1\}} = (\mu_1) \) exists.

(c) If \( \mu_1 = \lambda_1 \) or \( \mu_1 = \lambda_2 \) then the formula gives \( b = 0 \), and \( \A = \diag(\mu_1, \lambda_1 + \lambda_2 - \mu_1) \) is diagonal with the two entries \( \lambda_1 \) and \( \lambda_2 \) in one order or the other. So the construction still works, with a zero border; consistently with @thm-bordered-matrix, a zero border is exactly what makes the interlacing non-strict.
:::

:::: {#exr-cauchy-interlacing-c3}
[C3: How far apart can the extremes be]

Let \( \A \in M_n(F) \) be Hermitian.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \lambda_1(\A) - \lambda_n(\A) \ge \max_{i,j}\ \lvert a_{ii} - a_{jj}\rvert \).
2. Prove that \( \lambda_1(\A) - \lambda_n(\A) \ge 2\max_{i \ne j}\lvert a_{ij}\rvert \).
:::

*Hint for (b): look at a \( 2 \times 2 \) principal submatrix.*
::::

::: {.solution}
(a) By @exm-diagonal-entries-interlace, \( \lambda_n(\A) \le a_{kk} \le \lambda_1(\A) \) for every \( k \). So for any \( i, j \), both \( a_{ii} - a_{jj} \) and \( a_{jj} - a_{ii} \) are at most \( \lambda_1(\A) - \lambda_n(\A) \), which gives the bound after taking the maximum over \( i, j \).

(b) Fix \( i \ne j \) and let \( I = \{i, j\} \), so that
\[
\B = \A_{I,I} = \begin{pmatrix} a_{ii} & a_{ij} \\ \conj{a_{ij}} & a_{jj}\end{pmatrix}
\]
is Hermitian of size \( 2 \). Its trace is \( a_{ii} + a_{jj} \) and its determinant is \( a_{ii}a_{jj} - \lvert a_{ij}\rvert^2 \), so its eigenvalues are
\[
\frac{a_{ii}+a_{jj}}{2} \pm \sqrt{\Bigl(\frac{a_{ii}-a_{jj}}{2}\Bigr)^2 + \lvert a_{ij}\rvert^2} ,
\]
and their difference is \( 2\sqrt{((a_{ii}-a_{jj})/2)^2 + \lvert a_{ij}\rvert^2} \ge 2\lvert a_{ij}\rvert \). Now apply @cor-interlacing-general-submatrix with \( m = n-2 \): it gives \( \lambda_1(\A) \ge \lambda_1(\B) \) and \( \lambda_2(\B) \ge \lambda_{2 + (n-2)}(\A) = \lambda_n(\A) \), so
\[
\lambda_1(\A) - \lambda_n(\A) \ \ge\ \lambda_1(\B) - \lambda_2(\B) \ \ge\ 2\lvert a_{ij}\rvert .
\]
Taking the maximum over the pairs \( i \ne j \) finishes the proof. (For \( n = 2 \) the step with \( m = 0 \) is the identity \( \B = \A \), and the conclusion is the computation itself.)
:::
