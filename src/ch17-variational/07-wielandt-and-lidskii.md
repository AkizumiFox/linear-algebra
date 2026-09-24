# Arbitrary Index Sets

The Courant–Fischer theorem describes one eigenvalue at a time, and Ky Fan's theorem describes the sum of the top \( k \). Between those two lies every other sum, for instance \( \lambda_2 + \lambda_4 \), and §06 ended by warning that the sharpest statements about eigenvalues tend to be statements about sums. This section describes the sum over an **arbitrary** index set as a max–min, which is Wielandt's theorem. It then uses that description to compare two Hermitian matrices across any index set at once, which is Lidskii's inequality. The price of the generality is that single subspaces are replaced by nested chains of them, and the proof takes some care.

**Throughout, \( F = \nR \) or \( F = \nC \), every matrix whose eigenvalues are indexed is Hermitian, and the indexing is decreasing**, \( \lambda_1(\A) \ge \dots \ge \lambda_n(\A) \), with multiplicity. An **index set** of size \( k \) is a list of integers \( 1 \le i_1 < i_2 < \dots < i_k \le n \).

## What adding up the min–max gives

Here is the question that drives the section. Let \( \A \) and \( \B \) be Hermitian and fix an index set. How large can
\[
\sum_{j=1}^{k}\lambda_{i_j}(\A) - \sum_{j=1}^{k}\lambda_{i_j}(\B)
\]
be, in terms of \( \A - \B \)? One answer is immediate. By @cor-weyl-monotone, applied to \( \B \) and the Hermitian matrix \( \A - \B \), each single difference satisfies \( \lambda_i(\A) - \lambda_i(\B) \le \lambda_1(\A - \B) \). Adding \( k \) of these gives the bound \( k\,\lambda_1(\A - \B) \).

That bound is poor, and a rank-one example shows by how much. Let \( \A = \B + \u\u^{*} \) with \( \norm{\u} = 1 \). By @thm-rank-one-interlacing every shift \( \lambda_i(\A) - \lambda_i(\B) \) is \( \ge 0 \), and by @cor-eigenvalue-shift-total the shifts add up to exactly \( \norm{\u}^2 = 1 \). So **every** partial sum of shifts is at most \( 1 \), whatever the index set. The eigenvalues of \( \u\u^{*} \) are \( 1, 0, \dots, 0 \), so \( 1 = \lambda_1 + \dots + \lambda_k \) of \( \A - \B \) for every \( k \). The summed Weyl bound says \( k \), which is wrong by a factor of \( k \).

The bound we would like is therefore
\[
\sum_{j=1}^{k}\lambda_{i_j}(\A) - \sum_{j=1}^{k}\lambda_{i_j}(\B)
\ \le\ \sum_{j=1}^{k}\lambda_j(\A - \B) ,
\]
and the obstruction is visible in the proof of Weyl's inequality. That proof finds, for each index, **one** good vector. Summing \( k \) such bounds uses \( k \) unrelated vectors, and the only control over \( \sum_j\inner{(\A-\B)\x_j}{\x_j} \) for unrelated unit vectors is \( k\,\lambda_1(\A-\B) \). If the \( \x_j \) were **orthonormal**, @thm-ky-fan would bound the same sum by \( \lambda_1 + \dots + \lambda_k \) of \( \A - \B \). So we need a single orthonormal list \( \x_1, \dots, \x_k \) that is simultaneously good for \( \A \) and good for \( \B \):
\[
\sum_{j}\inner{\A\x_j}{\x_j} \ \ge\ \sum_j\lambda_{i_j}(\A) ,
\qquad
\sum_{j}\inner{\B\x_j}{\x_j} \ \le\ \sum_j\lambda_{i_j}(\B) .
\]
The first requirement is easy to meet: it will hold whenever each \( \x_j \) lies in the span \( W_j \) of the top \( i_j \) eigenvectors of \( \A \). Those spans are nested, \( W_1 \subset W_2 \subset \dots \subset W_k \), and from \( \B \)'s point of view they are an arbitrary nested chain of subspaces. The second requirement is then a question about \( \B \) alone: **inside any nested chain of subspaces of these dimensions, is there an orthonormal list whose sum for \( \B \) is small?** Wielandt's theorem answers yes, and the chain needs a name.

## Flags and adapted lists

Chapter 9 §07 called a chain \( U_1 \subset U_2 \subset \dots \subset U_n = V \) with \( \dim U_k = k \) a **flag**, and a basis whose first \( k \) members span \( U_k \) a basis adapted to it. We need chains that skip dimensions, and lists that meet each member of the chain once.

*A flag of type \( (i_1, \dots, i_k) \) is a nested chain of subspaces with prescribed dimensions; an adapted list takes its \( j \)-th vector from the \( j \)-th subspace and is orthonormal.*

::: {#def-flag-adapted-list}
[Flags of a given type, and adapted lists]

Let \( F = \nR \) or \( \nC \), and let \( 1 \le i_1 < \dots < i_k \le n \) be an index set. A **flag of type \( (i_1, \dots, i_k) \)** in \( F^n \) is a list \( \cW = (W_1, \dots, W_k) \) of subspaces of \( F^n \) with
\[
W_1 \subseteq W_2 \subseteq \dots \subseteq W_k
\qquad\text{and}\qquad
\dim W_j = i_j \ \text{ for every } j .
\]
A list \( (\x_1, \dots, \x_k) \) of vectors of \( F^n \) is **adapted to** \( \cW \) if it is **orthonormal** and \( \x_j \in W_j \) for **every** \( j \).
:::

In words. The subspaces are nested, and the \( j \)-th one has dimension equal to the \( j \)-th **index** \( i_j \), not to \( j \); since the indices strictly increase, so do the dimensions, and each inclusion is proper. An adapted list has exactly one vector per subspace; the \( j \)-th vector may be taken anywhere in \( W_j \), including in the smaller \( W_1, \dots, W_{j-1} \), but the whole list must be orthonormal.

**Every flag has an adapted list.** Choose a basis of \( W_1 \), extend it to a basis of \( W_2 \) (@thm-basis-extension), then to \( W_3 \), and so on up to \( W_k \). This gives a basis \( \v_1, \dots, \v_{i_k} \) of \( W_k \) whose first \( i_j \) members span \( W_j \). Applying @thm-gram-schmidt yields an orthonormal list \( \e_1, \dots, \e_{i_k} \) with \( \Span(\e_1, \dots, \e_{i_j}) = W_j \) for each \( j \), and \( (\e_{i_1}, \dots, \e_{i_k}) \) is adapted to \( \cW \).

Four cases to keep in mind.

- **One index.** For \( k = 1 \) a flag is a single subspace \( W_1 \) of dimension \( i_1 \), and an adapted list is a single unit vector in it.
- **An initial segment.** For the index set \( (1, 2, \dots, k) \), \( W_j \) has dimension \( j \). An adapted list is then an orthonormal basis of \( W_k \) whose first \( j \) vectors span \( W_j \), since \( j \) orthonormal vectors in the \( j \)-dimensional \( W_j \) span it. With \( k = n \) this is Chapter 9's complete flag.
- **The eigenflag.** Let \( (\u_1, \dots, \u_n) \) be an orthonormal basis of \( F^n \) with \( \A\u_p = \lambda_p(\A)\u_p \), and put \( W_j = \Span(\u_1, \dots, \u_{i_j}) \). This is a flag of type \( (i_1, \dots, i_k) \), and \( (\u_{i_1}, \dots, \u_{i_k}) \) is adapted to it, since \( \u_{i_j} \) is among the vectors spanning \( W_j \).
- **The degenerate case \( k = n \).** Then \( i_j = j \) is forced, \( W_n = F^n \), and an adapted list is an orthonormal basis of \( F^n \) whose first \( j \) vectors span \( W_j \).

A minimal change breaks adaptedness. For the eigenflag of type \( (1, 3) \) in \( F^3 \), namely \( \Span(\u_1) \subset F^3 \), the list \( (\u_1, \u_3) \) is adapted. Swap the two vectors to get \( (\u_3, \u_1) \). It is still orthonormal and its members still lie in \( W_2 = F^3 \), but the clause \( \x_1 \in W_1 \) fails: \( \u_3 \notin \Span(\u_1) \).

Why this definition? Orthonormality is what makes \( \sum_j \inner{\A\x_j}{\x_j} \) the trace of a compression, which is what @thm-ky-fan controls. The nesting will let us orthonormalize a list by Gram–Schmidt without moving any vector out of its own subspace, since Gram–Schmidt keeps the \( j \)-th vector in the span of the first \( j \).

::: {.check}
In \( \nR^3 \), take the flag \( W_1 = \Span(\e_1) \subset W_2 = \Span(\e_1, \e_2, \e_3) \), of type \( (1, 3) \). Which of these lists are adapted to it: (a) \( (\e_1, \e_3) \); (b) \( (\e_3, \e_1) \); (c) \( (\e_1, \e_1 + \e_2) \); (d) \( (-\e_1, \tfrac{1}{\sqrt2}(\e_2 - \e_3)) \)?
:::

::: {.solution}
(a) Yes: orthonormal, \( \e_1 \in W_1 \) and \( \e_3 \in W_2 \). (b) No: \( \x_1 = \e_3 \) is not in \( W_1 \). (c) No: the list is not orthonormal, since \( \inner{\e_1}{\e_1 + \e_2} = 1 \) and \( \norm{\e_1 + \e_2} = \sqrt2 \). (d) Yes: \( -\e_1 \in W_1 \), the second vector has length \( 1 \) and is orthogonal to \( \e_1 \), and every vector lies in \( W_2 = \nR^3 \).
:::

## Wielandt's minimax principle

The eigenflag guarantees every adapted list a large sum, and no flag of the same type can guarantee more. That is the statement; the second half is the hard one.

::: {#thm-wielandt-minimax}
[Wielandt's Minimax Principle]

Let \( \A \in M_n(F) \) be Hermitian, with \( F = \nR \) or \( \nC \), and let \( 1 \le i_1 < \dots < i_k \le n \).

::: {.enumerate options="label=(\alph*)"}
1. For **every** flag \( \cW \) of type \( (i_1, \dots, i_k) \) there is a list \( (\x_1, \dots, \x_k) \) adapted to \( \cW \) with
   \[
   \sum_{j=1}^{k}\inner{\A\x_j}{\x_j} \ \le\ \sum_{j=1}^{k}\lambda_{i_j}(\A) .
   \]
2. Let \( (\u_1, \dots, \u_n) \) be an orthonormal basis with \( \A\u_p = \lambda_p(\A)\u_p \) for every \( p \), and let \( \cW^{\A} \) be the flag \( W_j = \Span(\u_1, \dots, \u_{i_j}) \). Then **every** list \( (\x_1, \dots, \x_k) \) adapted to \( \cW^{\A} \) satisfies
   \[
   \sum_{j=1}^{k}\inner{\A\x_j}{\x_j} \ \ge\ \sum_{j=1}^{k}\lambda_{i_j}(\A) ,
   \]
   with equality for \( \x_j = \u_{i_j} \).
3. Consequently
   \[
   \sum_{j=1}^{k}\lambda_{i_j}(\A)
   = \max_{\cW}\ \min_{(\x_1, \dots, \x_k)}\ \sum_{j=1}^{k}\inner{\A\x_j}{\x_j} ,
   \]
   where \( \cW \) runs over all flags of type \( (i_1, \dots, i_k) \) in \( F^n \), and for each \( \cW \) the list runs over all lists adapted to \( \cW \). The inner minimum exists for every \( \cW \), and the outer maximum is attained at \( \cW^{\A} \).
:::
:::

::: {.idea}
Two inequalities of different characters, as in @thm-courant-fischer. In both, the sum \( \sum_j\inner{\A\x_j}{\x_j} \) is the trace of the compression \( \B \) of \( \A \) to the span of the list, so it is \( \sum_j\lambda_j(\B) \). Both parts therefore come down to comparing \( \lambda_j(\B) \) with \( \lambda_{i_j}(\A) \), one \( j \) at a time, by Courant–Fischer applied to the small matrix \( \B \).

For (b), the first \( j \) vectors of the list lie in \( \Span(\u_1, \dots, \u_{i_j}) \), where \( R_{\A} \ge \lambda_{i_j}(\A) \), so \( \lambda_j(\B) \ge \lambda_{i_j}(\A) \).

For (a), we need a list whose span \( X \) meets each bottom span \( L_{i_j} = \Span(\u_{i_j}, \dots, \u_n) \) in dimension at least \( k - j + 1 \), since \( R_{\A} \le \lambda_{i_j}(\A) \) there. For a **single** \( j \), @lem-subspace-intersection gives such a meeting. For all \( j \) at once, with one \( X \), it does not: the vectors chosen for different \( j \) can collide, and the example after the proof shows that they do. The remedy is to count in coordinates. Record, for each vector, the first eigenvector coordinate at which it is non-zero; vectors with different first coordinates are independent; and a greedy choice of these first coordinates achieves every count at once.

**Step roadmap.** A preliminary claim turns bounds on \( R_{\A} \) over subspaces into bounds on the eigenvalues of a compression. **Step 1** proves (b). **Step 2** introduces leading indices and makes the greedy selection. **Step 3** orthonormalizes the selected vectors and proves (a). **Step 4** proves that the inner minimum exists, which is the only place analysis enters, and deduces (c).
:::

::: {.proof}
Let \( (\u_1, \dots, \u_n) \) be an orthonormal basis of \( F^n \) with \( \A\u_p = \lambda_p(\A)\u_p \) for every \( p \); such a basis exists by @cor-spectral-complex-matrix over \( \nC \) or @cor-spectral-real-matrix over \( \nR \). For part (b) take the basis named there; for part (a) any such basis will do. Abbreviate \( \lambda_p = \lambda_p(\A) \). For \( 1 \le p \le n \) put
\[
L_p = \Span(\u_p, \u_{p+1}, \dots, \u_n), \qquad L_{n+1} = \{\0\} .
\]
By @lem-rayleigh-on-eigenspan, \( R_{\A}(\x) \le \lambda_p \) for every non-zero \( \x \in L_p \), and \( R_{\A}(\x) \ge \lambda_p \) for every non-zero \( \x \in \Span(\u_1, \dots, \u_p) \).

::: {.claim}
**Claim 1 (compression bounds).** Let \( (\y_1, \dots, \y_k) \) be orthonormal, let \( Y \) be its span, let \( \Q \in M_{n \times k}(F) \) have columns \( \y_1, \dots, \y_k \), and let \( \B = \Q^{*}\A\Q \) be the compression of @def-compression. Let \( 1 \le m \le k \) and \( c \in \nR \).

(i) If \( S \subseteq Y \) is a subspace with \( \dim S = m \) and \( R_{\A}(\x) \ge c \) for every non-zero \( \x \in S \), then \( \lambda_m(\B) \ge c \).

(ii) If \( S \subseteq Y \) is a subspace with \( \dim S = k - m + 1 \) and \( R_{\A}(\x) \le c \) for every non-zero \( \x \in S \), then \( \lambda_m(\B) \le c \).

Moreover \( \sum_{j=1}^{k}\inner{\A\y_j}{\y_j} = \tr\B = \sum_{j=1}^{k}\lambda_j(\B) \).
:::

::: {.proof}
The matrix \( \B \) is Hermitian, and the map \( \c \mapsto \Q\c \) is a linear bijection \( F^k \to Y \) with \( R_{\B}(\c) = R_{\A}(\Q\c) \) for \( \c \ne \0 \), as computed in the proof of @lem-rayleigh-range-on-subspace. Let \( S' = \{\c \in F^k : \Q\c \in S\} \); it is a subspace, and \( \c \mapsto \Q\c \) maps it bijectively onto \( S \), so \( \dim S' = \dim S \).

(i) By the max–min line of @thm-courant-fischer for \( \B \in M_k(F) \), \( \lambda_m(\B) \) is the largest of the numbers \( \min_{\0\ne\c\in T}R_{\B}(\c) \) over subspaces \( T \subseteq F^k \) of dimension \( m \). Taking \( T = S' \),
\[
\lambda_m(\B) \ \ge\ \min_{\0\ne\c\in S'}R_{\B}(\c) = \min_{\0\ne\x\in S}R_{\A}(\x) \ \ge\ c .
\]

(ii) By the min–max line of @thm-courant-fischer for \( \B \), with \( T = S' \) of dimension \( k - m + 1 \),
\[
\lambda_m(\B) \ \le\ \max_{\0\ne\c\in S'}R_{\B}(\c) = \max_{\0\ne\x\in S}R_{\A}(\x) \ \le\ c .
\]

Finally, the diagonal entries of \( \B \) are \( \inner{\A\y_j}{\y_j} \) by @def-compression, and the trace of the Hermitian \( \B \) is the sum of its eigenvalues by @cor-trace-sum-eigenvalues-again.
:::

**Step 1. The eigenflag guarantees the sum: part (b).** Let \( (\x_1, \dots, \x_k) \) be adapted to \( \cW^{\A} \), so \( \x_j \in W_j = \Span(\u_1, \dots, \u_{i_j}) \). Fix \( j \) and put \( S = \Span(\x_1, \dots, \x_j) \). The list is orthonormal, hence independent, so \( \dim S = j \). Each \( \x_m \) with \( m \le j \) lies in \( W_m \subseteq W_j \), so \( S \subseteq W_j \), where \( R_{\A} \ge \lambda_{i_j} \). By Claim 1 (i) with \( m = j \), \( \lambda_j(\B) \ge \lambda_{i_j} \), where \( \B \) is the compression to the span of the list. Summing over \( j \) and using the last line of Claim 1,
\[
\sum_{j=1}^{k}\inner{\A\x_j}{\x_j} = \sum_{j=1}^{k}\lambda_j(\B) \ \ge\ \sum_{j=1}^{k}\lambda_{i_j} .
\]
For \( \x_j = \u_{i_j} \) each term is \( \inner{\A\u_{i_j}}{\u_{i_j}} = \lambda_{i_j} \), so equality holds. This proves (b).

**Step 2. Leading indices, and a selection.** Let \( \cW = (W_1, \dots, W_k) \) be an arbitrary flag of type \( (i_1, \dots, i_k) \). For \( \x \in F^n \) write \( c_p(\x) = \inner{\x}{\u_p} \), so that \( \x = \sum_p c_p(\x)\u_p \) by @thm-orthonormal-coordinates (a). Then \( \x \in L_p \) exactly when \( c_1(\x) = \dots = c_{p-1}(\x) = 0 \). The **leading index** \( \ell(\x) \) of a non-zero \( \x \) is the smallest \( p \) with \( c_p(\x) \ne 0 \), so that
\[
\x \in L_p \iff \ell(\x) \ge p \qquad (\x \ne \0) .
\]
For a subspace \( V \subseteq F^n \), let \( J(V) \) be the set of \( p \in \{1, \dots, n\} \) with \( V \cap L_{p+1} \ne V \cap L_p \). These are the indices at which the chain \( V = V \cap L_1 \supseteq V \cap L_2 \supseteq \dots \supseteq V \cap L_{n+1} = \{\0\} \) gets strictly smaller.

::: {.claim}
**Claim 2 (the jumps count the dimension).** For every subspace \( V \subseteq F^n \) and every \( 1 \le p \le n+1 \),
\[
\dim(V \cap L_p) = \bigl\lvert J(V) \cap \{p, p+1, \dots, n\} \bigr\rvert .
\]
In particular \( \lvert J(V)\rvert = \dim V \). Moreover, for each \( p \in J(V) \) there is \( \x \in V \) with \( \ell(\x) = p \).
:::

::: {.proof}
Fix \( p \le n \). The map \( \varphi_p \colon V \cap L_p \to F \), \( \x \mapsto c_p(\x) \), is linear. A vector of \( V \cap L_p \) already has \( c_1 = \dots = c_{p-1} = 0 \), so it lies in \( L_{p+1} \) exactly when also \( c_p = 0 \); hence \( \ker\varphi_p = V \cap L_{p+1} \). By @thm-rank-nullity,
\[
\dim(V \cap L_p) - \dim(V \cap L_{p+1}) = \rank\varphi_p ,
\]
and \( \rank\varphi_p \le \dim F = 1 \). The rank is \( 1 \) exactly when \( \ker\varphi_p \ne V \cap L_p \), that is, when \( p \in J(V) \). Adding these equations for \( p, p+1, \dots, n \), the left side telescopes to \( \dim(V \cap L_p) - \dim(V \cap L_{n+1}) = \dim(V \cap L_p) \), and the right side counts the elements of \( J(V) \) that are \( \ge p \). This proves the formula, which for \( p = n+1 \) reads \( 0 = 0 \). At \( p = 1 \), \( L_1 = F^n \) gives \( \lvert J(V)\rvert = \dim V \). Finally, if \( p \in J(V) \), pick \( \x \in (V \cap L_p) \setminus L_{p+1} \); then \( c_1(\x) = \dots = c_{p-1}(\x) = 0 \ne c_p(\x) \), so \( \ell(\x) = p \).
:::

::: {.claim}
**Claim 3 (distinct leading indices force independence).** Non-zero vectors \( \x_1, \dots, \x_r \) whose leading indices are pairwise distinct are linearly independent.
:::

::: {.proof}
Suppose \( \sum_m a_m\x_m = \0 \) with not all \( a_m \) zero. Among the \( m \) with \( a_m \ne 0 \), let \( m_0 \) be the one with the smallest leading index, \( q = \ell(\x_{m_0}) \). Apply \( c_q \). Every other \( \x_m \) with \( a_m \ne 0 \) has \( \ell(\x_m) > q \), so \( c_q(\x_m) = 0 \). Hence \( 0 = a_{m_0}c_q(\x_{m_0}) \), a product of two non-zero numbers, which is a contradiction.
:::

::: {.claim}
**Claim 4 (a greedy selection).** There are non-zero vectors \( \x_1, \dots, \x_k \) with \( \x_m \in W_m \), with pairwise distinct leading indices \( q_m = \ell(\x_m) \), and such that for every \( j \),
\[
\#\{\, m : q_m \ge i_j \,\} \ \ge\ k - j + 1 .
\]
:::

::: {.proof}
Choose \( q_1, \dots, q_k \) in turn: \( q_m \) is the **largest** element of \( J(W_m) \) not among \( q_1, \dots, q_{m-1} \). This is possible, because \( J(W_m) \) has \( \dim W_m = i_m \ge m \) elements by Claim 2, so at most \( m - 1 \) of them are used. By the last part of Claim 2, pick \( \x_m \in W_m \) with \( \ell(\x_m) = q_m \). The \( q_m \) are distinct by construction.

Fix \( j \), and for \( m \ge j - 1 \) let \( N_m \) be the number of \( l \le m \) with \( q_l \ge i_j \). We show \( N_m \ge m - j + 1 \) by induction on \( m \). For \( m = j - 1 \) this says \( N_{j-1} \ge 0 \), which is true. Let \( m \ge j \) and assume \( N_{m-1} \ge m - j \).

*Case 1: \( q_m \ge i_j \).* Then \( N_m = N_{m-1} + 1 \ge m - j + 1 \).

*Case 2: \( q_m < i_j \).* By Claim 2, \( J(W_m) \) has \( i_m \) elements, of which at most \( i_j - 1 \) are smaller than \( i_j \). So at least \( i_m - i_j + 1 \) of them are \( \ge i_j \), and \( i_m - i_j \ge m - j \) because the indices are strictly increasing integers. Every element of \( J(W_m) \) that is \( \ge i_j \) exceeds \( q_m \), so by the choice of \( q_m \) as the largest unused element, each of them is already among \( q_1, \dots, q_{m-1} \). These are at least \( i_m - i_j + 1 \ge m - j + 1 \) of the earlier \( q_l \), all \( \ge i_j \), so \( N_{m-1} \ge m - j + 1 \). Hence \( N_m = N_{m-1} \ge m - j + 1 \).

At \( m = k \) this gives \( N_k \ge k - j + 1 \), which is the claim.
:::

**Step 3. An adapted list with a small sum: part (a).** Take \( \x_1, \dots, \x_k \) from Claim 4. They are linearly independent by Claim 3, so @thm-gram-schmidt applies and produces an orthonormal list \( (\y_1, \dots, \y_k) \) with \( \Span(\y_1, \dots, \y_j) = \Span(\x_1, \dots, \x_j) \) for each \( j \). Since \( \x_m \in W_m \subseteq W_j \) for \( m \le j \), the vector \( \y_j \) lies in \( W_j \). So \( (\y_1, \dots, \y_k) \) is adapted to \( \cW \).

Let \( X = \Span(\y_1, \dots, \y_k) = \Span(\x_1, \dots, \x_k) \), and let \( \B \) be the compression of \( \A \) to it with respect to the \( \y_j \). Fix \( j \). By Claim 4 at least \( k - j + 1 \) of the \( \x_m \) have \( q_m \ge i_j \); each of them lies in \( L_{i_j} \), and any \( k - j + 1 \) of them are independent by Claim 3. Let \( S \) be the span of \( k - j + 1 \) of them, so \( S \subseteq X \cap L_{i_j} \) and \( \dim S = k - j + 1 \). On \( S \subseteq L_{i_j} \) we have \( R_{\A} \le \lambda_{i_j} \), so Claim 1 (ii) with \( m = j \) gives \( \lambda_j(\B) \le \lambda_{i_j} \). Summing over \( j \) and using the last line of Claim 1,
\[
\sum_{j=1}^{k}\inner{\A\y_j}{\y_j} = \sum_{j=1}^{k}\lambda_j(\B) \ \le\ \sum_{j=1}^{k}\lambda_{i_j} .
\]
This proves (a).

**Step 4. The minimum exists, and the max–min formula: part (c).** Fix a flag \( \cW \). Identify a list \( (\x_1, \dots, \x_k) \) with the column of \( F^{nk} \) obtained by stacking the \( \x_j \); its Euclidean norm is \( (\sum_j\norm{\x_j}^2)^{1/2} \). Let \( \cO \) be the set of lists adapted to \( \cW \). It is non-empty, by the paragraph after @def-flag-adapted-list. It is bounded, since every element has norm \( \sqrt{k} \). And it contains the limit of each of its convergent sequences. Indeed, the conditions \( \inner{\x_i}{\x_j} = \delta_{ij} \) are equations between sums of products of the entries and their conjugates, which pass to limits. Each condition \( \x_j \in W_j \) says \( \M_j\x_j = \0 \) for a matrix \( \M_j \) whose null space is \( W_j \), for instance the matrix whose rows are the conjugate transposes of a basis of \( W_j^{\perp} \) (the zero matrix if \( W_j = F^n \)), and this passes to limits too. So by fact (A3) of Chapter 16's introduction, every sequence in \( \cO \) has a subsequence converging to a point of \( \cO \). The function \( (\x_1, \dots, \x_k) \mapsto \sum_j\inner{\A\x_j}{\x_j} \) is built from the real and imaginary parts of the entries by sums and products, so it is continuous, and it is real-valued since \( \A \) is Hermitian. By fact (A4) it attains a minimum on \( \cO \).

Call that minimum \( v(\cW) \). By (a), some adapted list has sum \( \le \sum_j\lambda_{i_j} \), so \( v(\cW) \le \sum_j\lambda_{i_j} \) for every \( \cW \). By (b), every list adapted to \( \cW^{\A} \) has sum \( \ge \sum_j\lambda_{i_j} \), with equality at \( (\u_{i_1}, \dots, \u_{i_k}) \), so \( v(\cW^{\A}) = \sum_j\lambda_{i_j} \). Hence the largest value of \( v(\cW) \) over all flags of the type exists, is attained at \( \cW^{\A} \), and equals \( \sum_j\lambda_{i_j} \). This proves (c), and the theorem.
:::

::: {.remark}
**Where the analysis went.** Parts (a) and (b) are pure algebra: a dimension count, Gram–Schmidt, and Courant–Fischer for a small matrix. The only analytic input is in Step 4, facts (A3) and (A4) of Chapter 16's introduction. This is the first time in the chapter that an item of that list is used rather than merely mentioned, and it is used only so that the word "min" in (c) refers to a value that is attained. Every later *result* in this section uses (a) and (b) alone, so no later result depends on analysis; only the exercises that quote (c), such as A1(b), lean on the attained minimum.
:::

Two index sets give back what we already have. For \( k = 1 \) a flag is a single subspace \( W \) of dimension \( i_1 \), an adapted list is a unit vector \( \x \in W \), and \( \inner{\A\x}{\x} = R_{\A}(\x) \). So (c) reads \( \lambda_{i_1}(\A) = \max_{\dim W = i_1}\min_{\0\ne\x\in W}R_{\A}(\x) \), the max–min line of @thm-courant-fischer. For the initial segment \( (1, \dots, k) \), an adapted list is an orthonormal basis of the \( k \)-dimensional \( W_k \), and conversely every orthonormal basis \( (\x_1, \dots, \x_k) \) of a \( k \)-dimensional subspace is adapted to the flag \( \Span(\x_1) \subset \Span(\x_1, \x_2) \subset \dots \). The sum \( \sum_j\inner{\A\x_j}{\x_j} \) is the trace of the compression to \( W_k \). That trace does not depend on the orthonormal basis, because §06 showed that a change of orthonormal basis changes the compression by a unitary similarity. So the inner minimum is constant, and (c) says that \( \sum_{j\le k}\lambda_j(\A) \) is the largest trace of a compression to a \( k \)-dimensional subspace, which is @thm-ky-fan. What is new is everything in between: index sets with gaps, such as \( (2, 4) \), and index sets that do not start at \( 1 \).

::: {#exm-wielandt-selection}
[The selection at work, and why it is needed]

Let \( \A = \diag(4, 2, 1, -1) \in M_4(\nR) \), take the index set \( (2, 4) \), and take the flag
\[
W_1 = \Span\bigl((1,1,0,0),\ \e_4\bigr) \ \subset\ W_2 = \nR^4 ,
\]
of type \( (2, 4) \). Show that the naive attempt, choosing \( \x_j \in W_j \cap L_{i_j} \) for each \( j \) separately, cannot produce an adapted list. Then follow the proof of part (a) to produce one with sum at most \( \lambda_2(\A) + \lambda_4(\A) \).
:::

::: {.solution}
Here the eigenvectors are \( \u_p = \e_p \), so \( L_p = \Span(\e_p, \dots, \e_4) \) is the set of vectors whose first \( p - 1 \) entries vanish, and the target is \( \lambda_2 + \lambda_4 = 2 + (-1) = 1 \).

*The naive attempt.* A vector \( a(1,1,0,0) + b\e_4 \) of \( W_1 \) lies in \( L_2 \) exactly when its first entry \( a \) is \( 0 \), so \( W_1 \cap L_2 = \Span(\e_4) \). Also \( W_2 \cap L_4 = L_4 = \Span(\e_4) \). Both vectors would have to be multiples of \( \e_4 \), and two such vectors are never orthonormal. Each of the two intersections is non-zero, as @lem-subspace-intersection promises, but the two choices collide.

*The selection.* The vectors of \( W_1 \) have the form \( (a, a, 0, b) \). They lie in \( L_2 \), \( L_3 \) or \( L_4 \) exactly when \( a = 0 \), and in \( L_5 = \{\0\} \) only when also \( b = 0 \). So the dimensions of \( W_1 \cap L_p \) for \( p = 1, \dots, 5 \) are \( 2, 1, 1, 1, 0 \), and the chain drops at \( p = 1 \) and \( p = 4 \): \( J(W_1) = \{1, 4\} \). For \( W_2 = \nR^4 \) the dimensions are \( 4, 3, 2, 1, 0 \), so \( J(W_2) = \{1, 2, 3, 4\} \). The greedy rule takes \( q_1 = \max J(W_1) = 4 \), with \( \x_1 = \e_4 \in W_1 \). It then takes \( q_2 = \max\bigl(J(W_2) \setminus \{4\}\bigr) = 3 \), with \( \x_2 = \e_3 \).

*The counts of Claim 4.* For \( j = 1 \), \( i_1 = 2 \), and both \( q_1 = 4 \) and \( q_2 = 3 \) are \( \ge 2 \): the count is \( 2 \ge 2 \). For \( j = 2 \), \( i_2 = 4 \), and only \( q_1 = 4 \) is \( \ge 4 \): the count is \( 1 \ge 1 \). Notice that the requirement for \( j = 2 \) is met by \( \x_1 \), not by \( \x_2 \); insisting that \( \x_2 \) itself lie in \( L_4 \) is exactly the naive attempt that failed.

*The list and its sum.* \( (\e_4, \e_3) \) is already orthonormal, so Gram–Schmidt leaves it alone, and it is adapted: \( \e_4 \in W_1 \), \( \e_3 \in W_2 \). Its sum is \( \inner{\A\e_4}{\e_4} + \inner{\A\e_3}{\e_3} = -1 + 1 = 0 \le 1 \). The compression to \( X = \Span(\e_4, \e_3) \) is \( \diag(-1, 1) \), with eigenvalues \( 1 \le \lambda_2(\A) = 2 \) and \( -1 \le \lambda_4(\A) = -1 \), as Step 3 predicts one index at a time.
:::

::: {.check}
Suppose "orthonormal" is weakened to "each \( \x_j \) is a unit vector" in the definition of an adapted list. Show that the formula (c) of @thm-wielandt-minimax remains true. Why is this weaker version useless for comparing two matrices?
:::

::: {.solution}
With the \( \x_j \) chosen independently, the inner minimum splits as \( \sum_j\min_{\0\ne\x\in W_j}R_{\A}(\x) \), one term per subspace. By @thm-courant-fischer each term is at most \( \lambda_{i_j}(\A) \), since \( \dim W_j = i_j \), and the eigenflag makes every term equal to \( \lambda_{i_j}(\A) \) at once. So the max–min is still \( \sum_j\lambda_{i_j}(\A) \); it is just Courant–Fischer added up. But the lists it produces are not orthonormal, so @thm-ky-fan cannot be applied to them. Comparing \( \A \) with \( \B \) through such lists gives only the summed Weyl bound \( k\,\lambda_1(\A - \B) \) of the first subsection. The whole content of Wielandt's theorem is that orthonormality costs nothing.
:::

## Lidskii's inequality

The plan of the first subsection can now be carried out.

::: {#thm-lidskii-inequality}
[Lidskii's Inequality]

Let \( \A, \B \in M_n(F) \) be Hermitian, with \( F = \nR \) or \( \nC \). Then for every index set \( 1 \le i_1 < \dots < i_k \le n \),
\[
\sum_{j=1}^{k}\lambda_{i_j}(\A) - \sum_{j=1}^{k}\lambda_{i_j}(\B)
\ \le\ \sum_{j=1}^{k}\lambda_j(\A - \B) .
\]
:::

::: {.idea}
Find one orthonormal list that is good for both matrices. Take the eigenflag of \( \A \). Part (b) of @thm-wielandt-minimax says that **every** list adapted to it is good for \( \A \). Part (a), applied to \( \B \) and this same flag, produces **one** adapted list that is good for \( \B \). Subtract the two sums. What remains is \( \sum_j\inner{(\A - \B)\x_j}{\x_j} \) over an orthonormal list, which @thm-ky-fan bounds by the top \( k \) eigenvalues of \( \A - \B \).
:::

::: {.proof}
Let \( (\u_1, \dots, \u_n) \) be an orthonormal basis of \( F^n \) with \( \A\u_p = \lambda_p(\A)\u_p \), which exists by @cor-spectral-complex-matrix or @cor-spectral-real-matrix, and let \( \cW^{\A} \) be the flag \( W_j = \Span(\u_1, \dots, \u_{i_j}) \), of type \( (i_1, \dots, i_k) \). By @thm-wielandt-minimax (a) applied to the Hermitian matrix \( \B \) and the flag \( \cW^{\A} \), there is a list \( (\x_1, \dots, \x_k) \) adapted to \( \cW^{\A} \) with
\[
\sum_{j=1}^{k}\inner{\B\x_j}{\x_j} \ \le\ \sum_{j=1}^{k}\lambda_{i_j}(\B) .
\]
By @thm-wielandt-minimax (b) applied to \( \A \), the same list satisfies
\[
\sum_{j=1}^{k}\inner{\A\x_j}{\x_j} \ \ge\ \sum_{j=1}^{k}\lambda_{i_j}(\A) .
\]
Subtracting the first inequality from the second, and using that the inner product is linear in its first slot,
\[
\sum_{j=1}^{k}\lambda_{i_j}(\A) - \sum_{j=1}^{k}\lambda_{i_j}(\B)
\ \le\ \sum_{j=1}^{k}\inner{(\A - \B)\x_j}{\x_j} .
\]
The matrix \( \A - \B \) is Hermitian and \( \x_1, \dots, \x_k \) are orthonormal, so @thm-ky-fan bounds the right-hand side by \( \sum_{j=1}^{k}\lambda_j(\A - \B) \). This proves the theorem.
:::

For the rank-one example of the first subsection, the right-hand side is \( \lambda_1 + \dots + \lambda_k \) of \( \u\u^{*} \), which is \( 1 \) for every \( k \): the theorem gives exactly the bound that the interlacing argument found there, and it gives it for every Hermitian \( \A - \B \), whatever its rank. One feature of the statement deserves a warning.

::: {.warning}
**The left side compares the two spectra at the same indices; the right side always uses the top \( k \) eigenvalues of \( \A - \B \), whatever the index set.** The tempting "index-by-index" version
\[
\lambda_{i}(\A) - \lambda_{i}(\B) \ \le\ \lambda_{i}(\A - \B)
\]
is false. Take \( \A = \diag(1, 1) \) and \( \B = \diag(1, 0) \), so \( \A - \B = \diag(0, 1) \) with \( \lambda_1(\A-\B) = 1 \) and \( \lambda_2(\A - \B) = 0 \). At \( i = 2 \) the left side is \( 1 - 0 = 1 \), which exceeds \( \lambda_2(\A - \B) = 0 \). Lidskii's bound is \( \lambda_1(\A - \B) = 1 \), and it is attained.
:::

::: {#exm-lidskii-3x3}
[All seven index sets]

Let
\[
\A = \begin{pmatrix} 0 & 2 & 0 \\ 2 & 1 & 2 \\ 0 & 2 & 2 \end{pmatrix},
\qquad
\B = \diag(0, 2, -1) .
\]
Find the three spectra, check @thm-lidskii-inequality for every index set, and compare with the summed Weyl bound \( k\,\lambda_1(\A - \B) \).
:::

::: {.solution}
*The spectra.* The vectors \( (1, 2, 2) \), \( (2, 1, -2) \), \( (2, -2, 1) \) are eigenvectors of \( \A \): for instance \( \A(1,2,2) = (4, 2 + 2 + 4, 4 + 4) = 4(1,2,2) \), and the other two give the eigenvalues \( 1 \) and \( -2 \) in the same way. So \( \vlambda(\A) = (4, 1, -2) \), writing \( \vlambda(\A) \) for the vector of eigenvalues in decreasing order. Sorting the diagonal of \( \B \) gives \( \vlambda(\B) = (2, 0, -1) \). Next,
\[
\A - \B = \begin{pmatrix} 0 & 2 & 0 \\ 2 & -1 & 2 \\ 0 & 2 & 3 \end{pmatrix}
\]
has eigenvectors \( (1, 2, 4) \), \( (-2, -1, 1) \), \( (2, -3, 1) \). For example \( (\A - \B)(1,2,4) = (4,\ 2 - 2 + 8,\ 4 + 12) = 4(1,2,4) \). So \( \vlambda(\A - \B) = (4, 1, -3) \), whose running totals from the top are \( 4, 5, 2 \).

*The inequalities.* The differences at equal indices are \( \lambda_i(\A) - \lambda_i(\B) = 2, 1, -1 \) for \( i = 1, 2, 3 \).

| index set | left side | Lidskii bound | summed Weyl bound |
|---|---|---|---|
| \( (1) \), \( (2) \), \( (3) \) | \( 2,\ 1,\ -1 \) | \( 4 \) | \( 4 \) |
| \( (1,2) \), \( (1,3) \), \( (2,3) \) | \( 3,\ 1,\ 0 \) | \( 5 \) | \( 8 \) |
| \( (1,2,3) \) | \( 2 \) | \( 2 \) | \( 12 \) |

Every inequality holds. For \( k = 3 \) it is an equality, and must be: both sides are then \( \tr\A - \tr\B = \tr(\A - \B) \), by @cor-trace-sum-eigenvalues-again and @thm-trace-properties (1). The summed Weyl bound grows like \( k\,\lambda_1(\A - \B) \), while Lidskii's bound can even decrease, because the eigenvalue \( -3 \) of \( \A - \B \) enters the sum as soon as \( k = 3 \).
:::

The index sets that give the results we already have are the two families from the discussion of Wielandt's theorem, now at the level of two matrices.

::: {#cor-lidskii-special-cases}
[Weyl and Ky Fan as Cases of Lidskii]

Let \( \A, \B \in M_n(F) \) be Hermitian.

::: {.enumerate options="label=(\alph*)"}
1. **(One index.)** For every \( i \),
   \[
   \lambda_n(\A - \B) \ \le\ \lambda_i(\A) - \lambda_i(\B) \ \le\ \lambda_1(\A - \B) ,
   \]
   and in particular \( \lvert\lambda_i(\A) - \lambda_i(\B)\rvert \le \norm{\A - \B}_2 \).
2. **(An initial segment.)** For every \( k \),
   \[
   \sum_{i=1}^{k}\lambda_i(\A) - \sum_{i=1}^{k}\lambda_i(\B)
   \ \le\ \sum_{i=1}^{k}\lambda_i(\A - \B) .
   \]
:::
:::

::: {.idea}
Both are @thm-lidskii-inequality with a particular index set, the lower bound in (a) coming from the same theorem with \( \A \) and \( \B \) exchanged.
:::

::: {.proof}
(a) The upper bound is @thm-lidskii-inequality with \( k = 1 \) and the index set \( (i) \). Exchanging \( \A \) and \( \B \) in the same case gives \( \lambda_i(\B) - \lambda_i(\A) \le \lambda_1(\B - \A) \). By @lem-eigenvalues-of-negation with \( p = 1 \), \( \lambda_1(\B - \A) = \lambda_1(-(\A - \B)) = -\lambda_n(\A - \B) \), and multiplying by \( -1 \) gives the lower bound. So \( \lambda_i(\A) - \lambda_i(\B) \) lies between \( \lambda_n(\A-\B) \) and \( \lambda_1(\A-\B) \), and its absolute value is at most \( \max\bigl(\lambda_1(\A-\B), -\lambda_n(\A-\B)\bigr) \), which is \( \norm{\A - \B}_2 \) by @lem-hermitian-spectral-norm.

(b) This is @thm-lidskii-inequality with the index set \( (1, 2, \dots, k) \).
:::

Read with \( \A = \X + \Y \) and \( \B = \X \), part (a) is @cor-weyl-monotone for the pair \( \X, \Y \); read with \( \B = \Y \) instead, it is the same corollary with \( \X \) and \( \Y \) exchanged. Together these are the cases of @thm-weyl-inequalities in which one of the two indices on the right is \( 1 \) (in part (a) of that theorem) or \( n \) (in its part (b)); applied to negated pairs, the one-index case gives a few more, as the remark below explains. The last clause of part (a) is @cor-weyl-perturbation. Part (b), read the same way, is @cor-ky-fan-subadditive. Here is the hierarchy, one row per index set.

| index set | @thm-wielandt-minimax gives | @thm-lidskii-inequality gives |
|---|---|---|
| \( (i) \), one index | @thm-courant-fischer, max–min line | @thm-weyl-inequalities with one index \( 1 \) or \( n \) (and, through negation, with \( i + j - 1 = n \)); @cor-weyl-perturbation |
| \( (1, \dots, k) \) | @thm-ky-fan | @cor-ky-fan-subadditive |
| any other, such as \( (2, 4) \) | new | new |

::: {.remark}
**Not all of Weyl's inequalities are cases of Lidskii's.** To test this fairly, @thm-lidskii-inequality must be allowed every pair it can see: all pairs of matrices among \( \pm\X \), \( \pm\Y \), \( \pm(\X + \Y) \) whose difference is another of the six. Negation matters. With it, the one-index case already reaches some Weyl inequalities with both indices inside: applied to \( \A = -\X \), \( \B = \Y \), whose difference is \( -(\X+\Y) \), and read through @lem-eigenvalues-of-negation, it gives \( \lambda_n(\X + \Y) \le \lambda_{n+1-i}(\X) + \lambda_i(\Y) \) for every \( i \), which is exactly the Weyl inequality (a) with \( i + j - 1 = n \). So a small example that ignores negation can look like a counterexample and not be one.

Even with every signed pair allowed, the family does not contain all of Weyl's. Take \( n = 4 \) and the candidate spectra
\[
\begin{aligned}
\vlambda(\X) &= (2, 0, 0, -1), \qquad \vlambda(\Y) = (2, 0, 0, 0), \\
\vlambda(\X + \Y) &= (2, 1, 1, -1) .
\end{aligned}
\]
The totals agree, \( 1 + 2 = 3 \), and a direct check of every index set shows that all twelve signed pairs satisfy every inequality of @thm-lidskii-inequality. Yet Weyl's inequality with \( i = j = 2 \) demands \( \lambda_3(\X + \Y) \le \lambda_2(\X) + \lambda_2(\Y) = 0 \), and here \( \lambda_3(\X + \Y) = 1 \). Since @thm-weyl-inequalities is a theorem, no Hermitian \( \X \), \( \Y \) have these spectra: the lists are ruled out by Weyl and not by Lidskii.
:::

::: {.remark}
**The majorization form.** Section 8 introduces the language that turns this family of inequalities into a single statement. We record the translation here, together with exactly what has been proved. For a real vector \( \x \in \nR^n \), the sum of its \( k \) largest entries is the largest value of \( \sum_{i \in S}x_i \) over the sets \( S \) of \( k \) positions: sorting the entries shows that the \( k \) largest do best. Apply this to \( \x = \vlambda(\A) - \vlambda(\B) \), whose \( i \)-th entry is \( \lambda_i(\A) - \lambda_i(\B) \) and which need not be decreasing. Then @thm-lidskii-inequality, over all index sets of size \( k \), says that the \( k \) largest entries of \( \vlambda(\A) - \vlambda(\B) \) add up to at most \( \sum_{j\le k}\lambda_j(\A - \B) \), for every \( k \). The two vectors also have the same total, \( \tr\A - \tr\B = \tr(\A - \B) \). In the notation of Section 8 this is
\[
\vlambda(\A) - \vlambda(\B) \ \prec\ \vlambda(\A - \B) .
\]
**Proved here:** every inequality in this majorization, namely @thm-lidskii-inequality for every index set, and the equality of totals, which is the trace. **Not proved here, and left to Chapter 21:** the general consequences of a majorization \( \x \prec \y \), namely \( \sum_i\phi(x_i) \le \sum_i\phi(y_i) \) for every convex \( \phi \colon \nR \to \nR \), together with the matching statement for the unitarily invariant norms of that chapter. Applied to the display above, they bound \( \sum_i\phi\bigl(\lambda_i(\A) - \lambda_i(\B)\bigr) \) by \( \sum_i\phi\bigl(\lambda_i(\A - \B)\bigr) \) for every convex \( \phi \). One case, \( \phi(t) = \lvert t\rvert \), follows from this section directly, and exercise C2 proves it. Nothing in this chapter uses the general case.
:::

## What the flags bought

Courant–Fischer turned each eigenvalue into an optimization that two matrices can share, and the comparison theorems of §§02–05 followed one index at a time. Ky Fan did the same for the top partial sums. Wielandt's theorem does it for every sum, at the price of optimizing over flags instead of subspaces, and Lidskii's inequality is what the shared optimization yields: the eigenvalue shifts \( \lambda_i(\A) - \lambda_i(\B) \), summed over **any** \( k \) indices, never exceed the top \( k \) eigenvalues of \( \A - \B \). The single idea behind it is the one the first subsection isolated. A comparison of sums needs one orthonormal list that serves both matrices, and a flag is exactly the structure that lets such a list be found by counting.

## Exercises

### A. Check your understanding

:::: {#exr-wielandt-and-lidskii-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define a flag of type \( (i_1, \dots, i_k) \) in \( F^n \) and a list adapted to it.
2. State the max–min formula of @thm-wielandt-minimax, and name the index sets for which it reduces to @thm-courant-fischer and to @thm-ky-fan.
3. Determine whether the following is true, and justify your answer: if \( (\x_1, \dots, \x_k) \) is adapted to a flag \( (W_1, \dots, W_k) \), then \( \Span(\x_1, \dots, \x_j) = W_j \) for every \( j \).
4. Determine whether the following is true for all Hermitian \( \A, \B \in M_n(F) \), and justify your answer: \( \lambda_2(\A) - \lambda_2(\B) \le \lambda_2(\A - \B) \).
5. In the proof of @thm-lidskii-inequality, which part of @thm-wielandt-minimax is applied to \( \A \), which to \( \B \), and with which flag?
:::
::::

::: {.solution}
(a) For an index set \( 1 \le i_1 < \dots < i_k \le n \), a flag of that type is a list \( (W_1, \dots, W_k) \) of subspaces of \( F^n \) with \( W_1 \subseteq \dots \subseteq W_k \) and \( \dim W_j = i_j \). A list \( (\x_1, \dots, \x_k) \) is adapted to it if it is orthonormal and \( \x_j \in W_j \) for every \( j \).

(b) \( \sum_j\lambda_{i_j}(\A) \) is the maximum over flags \( \cW \) of type \( (i_1, \dots, i_k) \) of the minimum of \( \sum_j\inner{\A\x_j}{\x_j} \) over lists adapted to \( \cW \). For \( k = 1 \), with index set \( (i) \), it is the max–min line of Courant–Fischer for \( \lambda_i \). For the initial segment \( (1, \dots, k) \) it is Ky Fan's theorem for \( \sum_{j\le k}\lambda_j \).

(c) False in general. The span of \( j \) orthonormal vectors has dimension \( j \), while \( \dim W_j = i_j \), which exceeds \( j \) unless \( i_j = j \). For instance, with \( k = 1 \) and the flag \( W_1 = \nR^2 \) of type \( (2) \), the adapted list \( (\e_1) \) spans a line. What is true is \( \Span(\x_1, \dots, \x_j) \subseteq W_j \).

(d) False. With \( \A = \diag(1,1) \) and \( \B = \diag(1,0) \), the left side is \( 1 - 0 = 1 \) and \( \lambda_2(\A - \B) = \lambda_2(\diag(0,1)) = 0 \). The correct bound, from @thm-lidskii-inequality with \( k = 1 \), is \( \lambda_1(\A - \B) \).

(e) The flag is the eigenflag \( \cW^{\A} \) of \( \A \) for the given index set. Part (b) is applied to \( \A \): every list adapted to \( \cW^{\A} \) has \( \A \)-sum at least \( \sum_j\lambda_{i_j}(\A) \). Part (a) is applied to \( \B \) with the same flag: some adapted list has \( \B \)-sum at most \( \sum_j\lambda_{i_j}(\B) \).
:::

### B. Practice

:::: {#exr-wielandt-and-lidskii-b1}
[B1: Running the selection]

Let \( \A = \diag(4, 1, -1) \in M_3(\nR) \), take the index set \( (1, 3) \), and let \( \cW \) be the flag \( W_1 = \Span\bigl((1,1,1)\bigr) \subset W_2 = \nR^3 \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \lambda_1(\A) + \lambda_3(\A) \), and show directly that every list adapted to the eigenflag \( \Span(\e_1) \subset \nR^3 \) has sum at least this number.
2. Follow the proof of @thm-wielandt-minimax (a) for \( \cW \): find \( J(W_1) \) and \( J(W_2) \), select \( \x_1, \x_2 \), apply Gram–Schmidt, and compute \( \sum_j\inner{\A\y_j}{\y_j} \).
3. Compute the compression \( \B \) of \( \A \) to \( \Span(\y_1, \y_2) \) and its eigenvalues, and check \( \lambda_j(\B) \le \lambda_{i_j}(\A) \) for \( j = 1, 2 \).
4. Find the minimum of \( \sum_j\inner{\A\x_j}{\x_j} \) over all lists adapted to \( \cW \). Is it the value found in (b)?
:::
::::

::: {.solution}
(a) The eigenvalues are \( 4, 1, -1 \) with eigenvectors \( \e_1, \e_2, \e_3 \), so \( \lambda_1 + \lambda_3 = 3 \), and \( \Span(\e_1) \subset \nR^3 \) is the eigenflag of type \( (1, 3) \). An adapted list has \( \x_1 = \pm\e_1 \), the unit vectors of the line, so \( \inner{\A\x_1}{\x_1} = 4 \). Its \( \x_2 \) is a unit vector orthogonal to \( \e_1 \), so \( \x_2 = (0, b, c) \) with \( b^2 + c^2 = 1 \), and \( \inner{\A\x_2}{\x_2} = b^2 - c^2 \ge -1 \). The sum is at least \( 4 - 1 = 3 \), with equality at \( \x_2 = \pm\e_3 \), as part (b) of the theorem says.

(b) Here \( L_p = \Span(\e_p, \dots, \e_3) \). The line \( W_1 \) is spanned by \( \w = (1,1,1) \), whose first entry is non-zero, so \( W_1 \cap L_2 = \{\0\} \) and \( J(W_1) = \{1\} \). For \( W_2 = \nR^3 \), \( J(W_2) = \{1, 2, 3\} \). The greedy rule gives \( q_1 = 1 \) with \( \x_1 = \w \), and \( q_2 = \max\{2, 3\} = 3 \) with \( \x_2 = \e_3 \). The counts of Claim 4 hold: for \( j = 1 \), both \( q \)'s are \( \ge i_1 = 1 \); for \( j = 2 \), \( q_2 = 3 \ge i_2 = 3 \). Gram–Schmidt gives \( \y_1 = \tfrac{1}{\sqrt3}(1,1,1) \) and
\[
\e_3 - \inner{\e_3}{\y_1}\y_1 = \tfrac13(-1, -1, 2), \qquad
\y_2 = \tfrac{1}{\sqrt6}(-1, -1, 2) .
\]
Then \( \inner{\A\y_1}{\y_1} = \tfrac13(4 + 1 - 1) = \tfrac43 \) and \( \inner{\A\y_2}{\y_2} = \tfrac16(4 + 1 - 4) = \tfrac16 \), so the sum is \( \tfrac32 \le 3 \), as the theorem requires.

(c) The off-diagonal entry is \( \inner{\A\y_2}{\y_1} = \tfrac{1}{\sqrt{18}}(-4 - 1 - 2) = -\tfrac{7}{3\sqrt2} \), so
\[
\B = \begin{pmatrix} 4/3 & -7/(3\sqrt2) \\ -7/(3\sqrt2) & 1/6 \end{pmatrix},
\qquad
\tr\B = \tfrac32, \quad \det\B = \tfrac29 - \tfrac{49}{18} = -\tfrac52 .
\]
The characteristic polynomial is \( t^2 - \tfrac32 t - \tfrac52 \), that is \( \tfrac12(2t - 5)(t + 1) \), so \( \lambda_1(\B) = \tfrac52 \le 4 = \lambda_1(\A) \) and \( \lambda_2(\B) = -1 \le -1 = \lambda_3(\A) \). The second is an equality, as it must be: @thm-poincare-separation with \( n = 3 \), \( k = 2 \) gives the reverse bound \( \lambda_2(\B) \ge \lambda_3(\A) \).

(d) An adapted list has \( \x_1 = \pm\y_1 \), contributing \( \tfrac43 \), and \( \x_2 \) is any unit vector of \( \w^{\perp} \). By @lem-rayleigh-range-on-subspace the smallest value of \( \inner{\A\x_2}{\x_2} \) there is the smallest eigenvalue of the compression of \( \A \) to \( \w^{\perp} \). With the orthonormal basis \( \tfrac1{\sqrt2}(1,-1,0) \), \( \tfrac1{\sqrt6}(1,1,-2) \) of \( \w^{\perp} \), that compression is
\[
\begin{pmatrix} 5/2 & \sqrt3/2 \\ \sqrt3/2 & 1/6 \end{pmatrix},
\]
with trace \( \tfrac83 \), determinant \( \tfrac5{12} - \tfrac34 = -\tfrac13 \), and characteristic polynomial \( \tfrac13(3t^2 - 8t - 1) \). Its smaller eigenvalue is \( \tfrac13(4 - \sqrt{19}) \). So the minimum over lists adapted to \( \cW \) is
\[
\tfrac43 + \tfrac13(4 - \sqrt{19}) = \tfrac13(8 - \sqrt{19}) \approx 1.214 .
\]
This is smaller than \( \tfrac32 \). The construction in the proof finds **an** adapted list below the bound \( 3 \), which is all part (a) asks; it need not find the best one. Both numbers are below \( 3 \), the value at the eigenflag, as part (c) requires.
:::

:::: {#exr-wielandt-and-lidskii-b2}
[B2: A complex pair]

Let
\[
\A = \begin{pmatrix} 2 & 1 + i \\ 1 - i & 1 \end{pmatrix},
\qquad
\B = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
\quad\text{in } M_2(\nC) .
\]

::: {.enumerate options="label=(\alph*)"}
1. Check that \( \A \) and \( \B \) are Hermitian, and compute \( \vlambda(\A) \), \( \vlambda(\B) \) and \( \vlambda(\A - \B) \).
2. Verify @thm-lidskii-inequality for all three index sets, and say which inequality is an equality and why it had to be.
3. Verify both bounds of @cor-lidskii-special-cases (a), and explain why here every \( \lambda_i(\A) - \lambda_i(\B) \) had to be non-negative.
:::
::::

::: {.solution}
(a) The diagonal of \( \A \) is real and \( a_{21} = 1 - i = \conj{a_{12}} \), so \( \A^{*} = \A \); \( \B \) is real diagonal. For \( \A \), \( \tr\A = 3 \) and \( \det\A = 2 - (1+i)(1-i) = 2 - 2 = 0 \), so \( \vlambda(\A) = (3, 0) \). Next, \( \vlambda(\B) = (1, -1) \). Finally
\[
\A - \B = \begin{pmatrix} 1 & 1 + i \\ 1 - i & 2 \end{pmatrix}
\]
has trace \( 3 \) and determinant \( 2 - 2 = 0 \), so \( \vlambda(\A - \B) = (3, 0) \).

(b) The differences at equal indices are \( 3 - 1 = 2 \) and \( 0 - (-1) = 1 \). For \( (1) \): \( 2 \le 3 \). For \( (2) \): \( 1 \le 3 \). For \( (1, 2) \): \( 3 \le 3 + 0 = 3 \), an equality. It had to be one, since for the full index set both sides equal \( \tr\A - \tr\B = \tr(\A - \B) \).

(c) The bounds are \( \lambda_2(\A - \B) = 0 \le 2 \le 3 \) and \( 0 \le 1 \le 3 \). The lower bound \( \lambda_n(\A - \B) = 0 \) is non-negative because \( \A - \B \succeq 0 \): it is Hermitian with eigenvalues \( 3, 0 \ge 0 \) (@thm-psd-characterizations). So \( \A \succeq \B \), and @cor-loewner-eigenvalue-monotone already forces \( \lambda_i(\A) \ge \lambda_i(\B) \) for each \( i \).
:::

:::: {#exr-wielandt-and-lidskii-b3}
[B3: The lower bound]

Let \( \A, \B \in M_n(F) \) be Hermitian and \( 1 \le i_1 < \dots < i_k \le n \). Prove that
\[
\sum_{j=1}^{k}\lambda_{i_j}(\A) - \sum_{j=1}^{k}\lambda_{i_j}(\B)
\ \ge\ \sum_{j=n-k+1}^{n}\lambda_j(\A - \B) ,
\]
that is, the shifts over any \( k \) indices add up to at least the \( k \) **smallest** eigenvalues of \( \A - \B \). Check the result on @exm-lidskii-3x3.
::::

::: {.solution}
Apply @thm-lidskii-inequality with the roles of \( \A \) and \( \B \) exchanged:
\[
\sum_{j=1}^{k}\lambda_{i_j}(\B) - \sum_{j=1}^{k}\lambda_{i_j}(\A)
\ \le\ \sum_{j=1}^{k}\lambda_j(\B - \A) .
\]
Since \( \B - \A = -(\A - \B) \), @lem-eigenvalues-of-negation gives \( \lambda_j(\B - \A) = -\lambda_{n+1-j}(\A - \B) \). As \( j \) runs over \( 1, \dots, k \), the index \( n + 1 - j \) runs over \( n, \dots, n - k + 1 \), so the right-hand side is \( -\sum_{j=n-k+1}^{n}\lambda_j(\A - \B) \). Multiplying the inequality by \( -1 \) gives the claim.

In @exm-lidskii-3x3, \( \vlambda(\A - \B) = (4, 1, -3) \), whose bottom partial sums are \( -3 \), \( -2 \), \( 2 \) for \( k = 1, 2, 3 \). The left sides are \( 2, 1, -1 \) for \( k = 1 \), then \( 3, 1, 0 \) for \( k = 2 \), then \( 2 \) for \( k = 3 \). Each is at least the corresponding bottom sum.
:::

### C. Going deeper

:::: {#exr-wielandt-and-lidskii-c1}
[C1: A second proof of Lidskii's inequality]

Let \( \A, \B \in M_n(F) \) be Hermitian, put \( \C = \A - \B \), and fix an index set \( 1 \le i_1 < \dots < i_k \le n \).

::: {.enumerate options="label=(\alph*)"}
1. Let \( c \in \nR \). Show that replacing \( \A \) by \( \A - c\I \), with \( \B \) unchanged, lowers both sides of @thm-lidskii-inequality by \( kc \). Deduce that it suffices to prove the inequality when \( \lambda_k(\C) = 0 \).
2. Assume \( \lambda_k(\C) = 0 \). Write \( \C = \U\D\U^{*} \) with \( \U \) unitary and \( \D = \diag(\lambda_1(\C), \dots, \lambda_n(\C)) \), and put \( \C_+ = \U\D_+\U^{*} \), where \( \D_+ \) replaces each negative diagonal entry of \( \D \) by \( 0 \). Prove that \( \C_+ \succeq \C \), \( \C_+ \succeq 0 \) and \( \tr\C_+ = \sum_{j\le k}\lambda_j(\C) \).
3. Prove that \( \lambda_i(\A) \le \lambda_i(\B + \C_+) \) and \( \lambda_i(\B + \C_+) \ge \lambda_i(\B) \) for every \( i \), and deduce @thm-lidskii-inequality.
4. Which of the ingredients of this proof were available before this section? What does this proof not give that @thm-wielandt-minimax does?
:::

*Hint: @cor-loewner-eigenvalue-monotone.*
::::

::: {.solution}
(a) For every Hermitian \( \M \) and real \( c \), \( \lambda_i(\M - c\I) = \lambda_i(\M) - c \) for all \( i \). Indeed, if \( \M = \U\D\U^{*} \) with \( \U \) unitary and \( \D \) real diagonal (@cor-spectral-complex-matrix, or @cor-spectral-real-matrix over \( \nR \)), then \( \M - c\I = \U(\D - c\I)\U^{*} \), and subtracting \( c \) from every diagonal entry keeps the order. Replacing \( \A \) by \( \A - c\I \) lowers each \( \lambda_{i_j}(\A) \) by \( c \), so the left side drops by \( kc \). It also replaces \( \C \) by \( \C - c\I \), so each \( \lambda_j(\C) \) drops by \( c \) and the right side drops by \( kc \). So the inequality for \( (\A - c\I, \B) \) is equivalent to the one for \( (\A, \B) \). With \( c = \lambda_k(\C) \), the new difference \( \C - c\I \) has \( \lambda_k = 0 \).

(b) \( \C_+ - \C = \U(\D_+ - \D)\U^{*} \), and \( \D_+ - \D \) is diagonal with entries \( \max(-\lambda_i(\C), 0) \ge 0 \). So \( \C_+ - \C \) is Hermitian with non-negative eigenvalues, hence \( \C_+ - \C \succeq 0 \) by @thm-psd-characterizations, that is, \( \C_+ \succeq \C \). In the same way \( \C_+ \succeq 0 \), since the entries of \( \D_+ \) are \( \ge 0 \). For the trace, \( \tr\C_+ = \tr\D_+ = \sum_i\max(\lambda_i(\C), 0) \) by @thm-trace-properties (3). For \( i \le k \), \( \lambda_i(\C) \ge \lambda_k(\C) = 0 \), so the term is \( \lambda_i(\C) \). For \( i > k \), \( \lambda_i(\C) \le 0 \), so the term is \( 0 \). Hence \( \tr\C_+ = \sum_{j\le k}\lambda_j(\C) \).

(c) \( \A = \B + \C \preceq \B + \C_+ \) by (b), and \( \B + \C_+ \succeq \B \) because \( \C_+ \succeq 0 \). @cor-loewner-eigenvalue-monotone turns both into the stated eigenvalue inequalities. Therefore
\[
\begin{aligned}
\sum_{j=1}^{k}\bigl(\lambda_{i_j}(\A) - \lambda_{i_j}(\B)\bigr)
&\le \sum_{j=1}^{k}\bigl(\lambda_{i_j}(\B + \C_+) - \lambda_{i_j}(\B)\bigr) \\
&\le \sum_{i=1}^{n}\bigl(\lambda_i(\B + \C_+) - \lambda_i(\B)\bigr) ,
\end{aligned}
\]
the second step adding the \( n - k \) omitted terms, each \( \ge 0 \). The last sum is \( \tr(\B + \C_+) - \tr\B = \tr\C_+ \), by @cor-trace-sum-eigenvalues-again and @thm-trace-properties (1), and \( \tr\C_+ = \sum_{j\le k}\lambda_j(\C) \) by (b).

(d) Everything used here was available after §02: the spectral theorem, the characterization of positive semidefiniteness by eigenvalues, the trace, and @cor-loewner-eigenvalue-monotone. The proof never looks at a flag. What it does not give is the variational description itself. @thm-wielandt-minimax expresses \( \sum_j\lambda_{i_j}(\A) \) as an optimization involving \( \A \) alone, and like Courant–Fischer and Ky Fan before it, such a description can be reused for other comparisons. This proof is a clever route to one consequence of that description.
:::

:::: {#exr-wielandt-and-lidskii-c2}
[C2: The total absolute shift]

Let \( \A, \B \in M_n(F) \) be Hermitian.

::: {.enumerate options="label=(\alph*)"}
1. Prove that
   \[
   \sum_{i=1}^{n}\bigl\lvert\lambda_i(\A) - \lambda_i(\B)\bigr\rvert
   \ \le\ \sum_{i=1}^{n}\bigl\lvert\lambda_i(\A - \B)\bigr\rvert .
   \]
2. Show that equality holds when \( \A \succeq \B \). Compute both sides for @exm-lidskii-3x3, and compare with the bound \( n\norm{\A - \B}_2 \) obtained by adding the bounds of @cor-weyl-perturbation.
:::

*Hint for (a): use the set of indices at which \( \lambda_i(\A) > \lambda_i(\B) \).*
::::

::: {.solution}
(a) Write \( d_i = \lambda_i(\A) - \lambda_i(\B) \) and \( \mu_j = \lambda_j(\A - \B) \). Let \( S = \{i : d_i > 0\} \) and \( k = \lvert S\rvert \). Then
\[
\sum_{i=1}^{n}\lvert d_i\rvert = \sum_{i \in S}d_i - \sum_{i \notin S}d_i
= 2\sum_{i\in S}d_i - \sum_{i=1}^{n}d_i .
\]
The total is \( \sum_i d_i = \tr\A - \tr\B = \tr(\A - \B) = \sum_j\mu_j \), by @cor-trace-sum-eigenvalues-again and @thm-trace-properties (1). If \( k \ge 1 \), @thm-lidskii-inequality with the elements of \( S \) as index set gives \( \sum_{i\in S}d_i \le \sum_{j\le k}\mu_j \); if \( k = 0 \) both sides of this inequality are the empty sum \( 0 \). In either case
\[
\sum_{i=1}^{n}\lvert d_i\rvert \ \le\ 2\sum_{j\le k}\mu_j - \sum_{j=1}^{n}\mu_j
= \sum_{j\le k}\mu_j - \sum_{j>k}\mu_j
\ \le\ \sum_{j=1}^{n}\lvert\mu_j\rvert ,
\]
the last step because \( \pm\mu_j \le \lvert\mu_j\rvert \) for each \( j \).

(b) If \( \A \succeq \B \) then every \( d_i \ge 0 \) by @cor-loewner-eigenvalue-monotone, and every \( \mu_j \ge 0 \) by @thm-psd-characterizations. Both sides then equal their plain sums, and those are equal, both being \( \tr(\A - \B) \).

In @exm-lidskii-3x3, the \( d_i \) are \( 2, 1, -1 \), so the left side is \( 4 \); the \( \mu_j \) are \( 4, 1, -3 \), so the right side is \( 8 \). By @lem-hermitian-spectral-norm, \( \norm{\A - \B}_2 = \max(4, 3) = 4 \), and adding the three bounds of @cor-weyl-perturbation gives \( 3 \cdot 4 = 12 \). The bound of (a) is never worse than this one: each \( \lvert\mu_j\rvert \le \norm{\A - \B}_2 \), so the right side of (a) is at most \( n\norm{\A - \B}_2 \), and it is often much smaller.
:::
