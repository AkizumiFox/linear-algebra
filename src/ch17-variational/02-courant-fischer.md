# The Min–Max Theorem

Section 1 ended with a description of \( \lambda_k(\A) \) that works and cannot be used: a maximum of the Rayleigh quotient over the orthogonal complement of \( \A \)'s own top eigenvectors. The defect is that the constraint set is built from the answer. This section repairs it by a move that looks like an extravagance and is exactly the right one: keep the maximum over a subspace, stop insisting that the subspace be the right one, and let it range over **all** subspaces of the appropriate dimension. The minimum of what comes out is again \( \lambda_k(\A) \), and no eigenvector appears anywhere in the statement. That is the Courant–Fischer theorem, and everything in the rest of the chapter is a consequence of it.

**Throughout, \( F \) is \( \nR \) or \( \nC \) and every matrix is Hermitian.** The eigenvalues of a Hermitian \( \A \in M_n(F) \) are real (@thm-self-adjoint-real-eigenvalues) and are **indexed decreasingly**,
\[
\lambda_1(\A) \ \ge\ \lambda_2(\A)\ \ge\ \dots\ \ge\ \lambda_n(\A) ,
\]
each repeated according to multiplicity, so that the list has exactly \( n \) entries. This is the book's convention, fixed in Chapter 13 §05, and it is used without exception below. Many sources index the theorem of this section the other way round; the remark after the theorem gives that form, once.

## Two subspaces that have to meet

One dimension count does all the work in this chapter, and it is worth a label of its own, because four later proofs cite it.

*Two subspaces of an \( n \)-dimensional space cannot both be large and disjoint: if their dimensions add to more than \( n \), they share a non-zero vector.*

::: {#lem-subspace-intersection}
[Large Subspaces Intersect]

Let \( V \) be a vector space with \( \dim V = n \) over any field, and let \( U \) and \( W \) be subspaces of \( V \) with
\[
\dim U + \dim W > n .
\]
Then \( U \cap W \ne \{\0\} \). More precisely, \( \dim(U \cap W) \ge \dim U + \dim W - n \).
:::

::: {.proof}
By @thm-dimension-formula-subspace-dim,
\[
\dim(U + W) = \dim U + \dim W - \dim(U \cap W) .
\]
Both \( U \) and \( W \) are finite-dimensional, being subspaces of the \( n \)-dimensional \( V \) (@thm-subspace-dimension); \( U + W \) is a subspace of \( V \) (@thm-subspace-sum), so the same theorem gives \( \dim(U+W) \le n \), and rearranging gives
\[
\dim(U \cap W) \ \ge\ \dim U + \dim W - n ,
\]
which is \( > 0 \) by hypothesis. A subspace of positive dimension contains a non-zero vector. This proves the lemma.
:::

::: {.remark}
The bound is sharp, and the hypothesis cannot be weakened to \( \dim U + \dim W = n \): two distinct lines in \( \nR^2 \) meet only at \( \0 \), and so do a line and a plane in \( \nR^3 \) chosen in general position. What makes the count useful is that it needs nothing about the two subspaces beyond their dimensions — in every application below, one of them is a span of eigenvectors that we choose and the other is an arbitrary competitor we know nothing about.
:::

## The quotient on a subspace

Before quantifying over subspaces, we must know that the inner maximum and minimum exist. They do, and for an algebraic reason: restricting the quadratic form to a subspace produces a smaller Hermitian matrix, to which @prp-rayleigh-basic applies verbatim.

::: {#lem-rayleigh-range-on-subspace}
[The Rayleigh Quotient on a Subspace]

Let \( \A \in M_n(F) \) be Hermitian and let \( W \subseteq F^n \) be a subspace with \( \dim W = m \ge 1 \). Let \( \Q \in M_{n \times m}(F) \) be a matrix whose columns form an orthonormal basis of \( W \), and put \( \B = \Q^{*}\A\Q \in M_m(F) \). Then \( \B \) is Hermitian and
\[
\bigl\{ R_{\A}(\x) : \0 \ne \x \in W \bigr\}
= \bigl[ \lambda_m(\B),\ \lambda_1(\B) \bigr] .
\]
In particular \( \max_{\0 \ne \x \in W}R_{\A}(\x) \) and \( \min_{\0 \ne \x \in W}R_{\A}(\x) \) exist and are attained.
:::

::: {.idea}
Coordinates on \( W \). Writing a vector of \( W \) as \( \Q\c \) turns \( \inner{\A\x}{\x} \) into \( \inner{\B\c}{\c} \) and, because the columns of \( \Q \) are orthonormal, turns \( \inner{\x}{\x} \) into \( \inner{\c}{\c} \) with no distortion. So the Rayleigh quotient of \( \A \) on \( W \) *is* the Rayleigh quotient of \( \B \) on \( F^m \), and @prp-rayleigh-basic answers the question there.
:::

::: {.proof}
Such a \( \Q \) exists: \( W \) has an orthonormal basis by @thm-gram-schmidt, and we take its members as columns. Orthonormality of the columns says exactly \( \Q^{*}\Q = \I_m \). Then \( \B^{*} = \Q^{*}\A^{*}\Q = \Q^{*}\A\Q = \B \), so \( \B \) is Hermitian and @prp-rayleigh-basic applies to it.

The map \( \c \mapsto \Q\c \) sends \( F^m \) onto \( W \), since the columns of \( \Q \) span \( W \), and it is injective, since \( \Q\c = \0 \) gives \( \c = \Q^{*}\Q\c = \0 \). So it is a bijection \( F^m \to W \) carrying \( \0 \) to \( \0 \), hence a bijection from the non-zero vectors of \( F^m \) onto those of \( W \). For \( \c \ne \0 \), writing the standard inner product as \( \inner{\u}{\v} = \v^{*}\u \),
\[
\begin{aligned}
\inner{\A\Q\c}{\Q\c} &= \c^{*}\Q^{*}\A\Q\c = \inner{\B\c}{\c} , \\
\inner{\Q\c}{\Q\c} &= \c^{*}\Q^{*}\Q\c = \inner{\c}{\c} ,
\end{aligned}
\]
so \( R_{\A}(\Q\c) = R_{\B}(\c) \). Therefore the two value sets
\( \{R_{\A}(\x) : \0 \ne \x \in W\} \) and \( \{R_{\B}(\c) : \0 \ne \c \in F^m\} \)
are equal, and the second is \( [\lambda_m(\B), \lambda_1(\B)] \) with both ends attained, by @prp-rayleigh-basic. This proves the lemma.
:::

::: {.remark}
**Which analysis was invoked: none.** The existence of a maximum of a function over an infinite set is normally an analytic fact — the set of unit vectors of \( W \) is compact, by fact (A3) of Chapter 16's introduction, and \( R_{\A} \) is continuous on it, so the extreme value theorem, fact (A4), applies. That route is available and correct. It is not needed. The spectral theorem, already proved in Chapter 12, produces the maximizing vector by name, and @lem-rayleigh-range-on-subspace inherits that. Nothing in this section, or in §01, uses an item of Chapter 16's imported-analysis list. The analysis has not vanished, only moved: the spectral theorem rests on the fundamental theorem of algebra (@thm-fundamental-theorem-of-algebra), whose proof in Chapter 6 §05 uses the extreme value theorem on a closed disc.
:::

## Every eigenvalue is a min–max

::: {#thm-courant-fischer}
[Courant–Fischer Min–Max Theorem]

Let \( F \) be \( \nR \) or \( \nC \), let \( \A \in M_n(F) \) be Hermitian and let \( 1 \le k \le n \). Then
\[
\begin{aligned}
\lambda_k(\A)
&= \min_{\dim W = n-k+1}\ \ \max_{\0 \ne \x \in W}\ R_{\A}(\x) \\[2pt]
&= \max_{\dim W = k}\ \ \min_{\0 \ne \x \in W}\ R_{\A}(\x) ,
\end{aligned}
\]
where in each line \( W \) runs over **all** subspaces of \( F^n \) of the stated dimension. All four extrema are attained.
:::

::: {.idea}
Read the second line first, because it is the one with a slogan: *\( \lambda_k \) is the best value you can guarantee on a \( k \)-dimensional subspace.* On a \( k \)-dimensional subspace the quotient has a smallest value, which is what that subspace guarantees; the span of the top \( k \) eigenvectors guarantees \( \lambda_k \), and no other \( k \)-dimensional subspace guarantees more.

The proof is three steps, and the first two have entirely different characters. **Step 1** exhibits a **witness** subspace and computes on it, giving one inequality. **Step 2** takes an **arbitrary** competitor subspace and shows it cannot beat the witness; the only thing known about a competitor is its dimension, so the only available tool is @lem-subspace-intersection, which forces the competitor to meet a span of eigenvectors from the other end of the list. On that shared non-zero vector the quotient is pinned, and the inequality follows. **Step 3** obtains the second line from the first by applying it to \( -\A \), which reverses the order of the eigenvalues and turns every maximum into a minimum.
:::

::: {.proof}
By @cor-spectral-complex-matrix over \( \nC \), or @cor-spectral-real-matrix over \( \nR \), fix an orthonormal basis \( (\q_1, \dots, \q_n) \) of \( F^n \) with \( \A\q_i = \lambda_i(\A)\q_i \) for every \( i \). Abbreviate \( \lambda_i = \lambda_i(\A) \) and put
\[
U_j = \Span(\q_1, \dots, \q_j), \qquad
L_j = \Span(\q_j, \dots, \q_n) ,
\]
so that \( \dim U_j = j \) and \( \dim L_j = n - j + 1 \), the lists being orthonormal and hence independent. By @lem-rayleigh-range-on-subspace the inner extrema below all exist.

::: {.claim}
For every \( j \): \( R_{\A}(\x) \ge \lambda_j \) for all \( \0 \ne \x \in U_j \), and \( R_{\A}(\x) \le \lambda_j \) for all \( \0 \ne \x \in L_j \). Both bounds are attained at \( \q_j \).
:::

::: {.proof}
Let \( \0 \ne \x \in U_j \) and write \( c_i = \inner{\x}{\q_i} \), so \( \x = \sum_{i \le j}c_i\q_i \) by @thm-orthonormal-coordinates (a) and the definition of \( U_j \). Then \( \A\x = \sum_{i\le j}\lambda_ic_i\q_i \), and @thm-orthonormal-coordinates (b), (c) give
\[
R_{\A}(\x) = \frac{\sum_{i \le j}\lambda_i\lvert c_i\rvert^2}{\sum_{i\le j}\lvert c_i\rvert^2} ,
\]
a weighted average of \( \lambda_1, \dots, \lambda_j \) with non-negative weights summing to \( 1 \). Since the list is indexed decreasingly, the smallest of those eigenvalues is \( \lambda_j \), so the average is \( \ge \lambda_j \). The statement for \( L_j \) is @prp-rayleigh-deflation: \( L_j \) is precisely the set of vectors orthogonal to \( \q_1, \dots, \q_{j-1} \), and the maximum of \( R_{\A} \) there is \( \lambda_j \). In both cases \( R_{\A}(\q_j) = \lambda_j \).
:::

**Step 1. The witness for the first line.** For each subspace \( W \) of dimension \( n-k+1 \) write \( f(W) = \max_{\0 \ne \x \in W} R_{\A}(\x) \), which exists by @lem-rayleigh-range-on-subspace. The outer minimum of \( f \) over all such \( W \) is not yet known to exist — there are infinitely many \( W \) — so we show that \( \lambda_k \) is a value of \( f \) and a lower bound for all its values; it is then the least value, which is what the minimum means. For the first half take \( W = L_k \), of dimension \( n-k+1 \): by the claim, \( f(L_k) = \lambda_k \).

**Step 2. Every competitor is at least as large.** Let \( W \subseteq F^n \) be any subspace with \( \dim W = n-k+1 \). Then
\[
\dim W + \dim U_k = (n-k+1) + k = n+1 > n ,
\]
so by @lem-subspace-intersection there is a vector \( \x \ne \0 \) lying in \( W \cap U_k \). Being in \( U_k \), it satisfies \( R_{\A}(\x) \ge \lambda_k \) by the claim; being in \( W \), it is one of the vectors the inner maximum ranges over. Therefore
\[
\max_{\0 \ne \y \in W} R_{\A}(\y) \ \ge\ R_{\A}(\x) \ \ge\ \lambda_k .
\]
This holds for every competitor \( W \), so \( f(W) \ge \lambda_k \) for all of them. With Step 1, \( \lambda_k \) is a value of \( f \) and a lower bound for every value, so it is the least value: the minimum exists, equals \( \lambda_k \), and is attained at \( W = L_k \). This proves the first line.

**Step 3. The second line, from the first applied to \( -\A \).** The matrix \( -\A \) is Hermitian, its eigenvalues are the numbers \( -\lambda_i \), and sorting those decreasingly reverses the list:
\[
\lambda_j(-\A) = -\lambda_{n+1-j}(\A) \qquad (1 \le j \le n) .
\]
Also \( R_{-\A}(\x) = -R_{\A}(\x) \) for every \( \x \ne \0 \), directly from the definition. Since negation turns a maximum of a set of reals into the minimum of the negated set, and a minimum into a maximum,
\[
\begin{aligned}
\max_{\0\ne\x\in W}R_{-\A}(\x) &= -\min_{\0\ne\x\in W}R_{\A}(\x) , \\
\min_{\dim W = m}\ \bigl(-f(W)\bigr) &= -\max_{\dim W = m} f(W)
\end{aligned}
\]
for any real-valued \( f \) on subspaces, where each side exists exactly when the other does. Apply the first line, already proved, to \( -\A \) with index \( j \):
\[
\begin{aligned}
-\lambda_{n+1-j}(\A)
&= \lambda_j(-\A)
= \min_{\dim W = n-j+1}\ \max_{\0\ne\x\in W} R_{-\A}(\x) \\
&= -\max_{\dim W = n-j+1}\ \min_{\0\ne\x\in W} R_{\A}(\x) .
\end{aligned}
\]
Now substitute \( j = n+1-k \), so that \( n-j+1 = k \) and \( n+1-j = k \). Multiplying by \( -1 \) gives
\[
\lambda_k(\A) = \max_{\dim W = k}\ \min_{\0 \ne \x \in W} R_{\A}(\x) ,
\]
with the maximum attained, the attainment transported from Step 1 by the same negation; explicitly it occurs at \( W = U_k \), which is the subspace \( L_{n+1-k} \) of the eigenbasis of \( -\A \) taken in its own decreasing order. This proves the theorem.
:::

The theorem removes the eigenvectors from the description of \( \lambda_k(\A) \). What is left mentions only \( \A \), through \( R_{\A} \), and the subspaces of \( F^n \), which are the same for every matrix. Two Hermitian matrices of the same size can therefore be compared term by term, and that is the whole reason this chapter exists.

::: {.remark}
**The increasing-index form.** If the eigenvalues are listed *increasingly* as \( \mu_1 \le \mu_2 \le \dots \le \mu_n \), then \( \mu_j = \lambda_{n+1-j}(\A) \), and substituting \( k = n+1-j \) in @thm-courant-fischer turns it into
\[
\begin{aligned}
\mu_j &= \min_{\dim W = j}\ \max_{\0\ne\x\in W} R_{\A}(\x) \\
&= \max_{\dim W = n-j+1}\ \min_{\0\ne\x\in W}R_{\A}(\x) .
\end{aligned}
\]
The pairing of \( \min\max \) with \( \max\min \) is unchanged; only the dimensions move. Many books state the theorem this way, so a reader comparing sources should check which convention is in force before comparing formulas. This book uses the decreasing one everywhere, and this is the only place the other appears.
:::

::: {.warning}
**Both the order of the two extrema and the dimension attached to each are load-bearing.** Neither
\[
\max_{\dim W = n-k+1}\ \min_{\0\ne\x\in W}R_{\A}(\x)
\qquad\text{nor}\qquad
\min_{\dim W = k}\ \max_{\0\ne\x\in W}R_{\A}(\x)
\]
equals \( \lambda_k(\A) \). Each of them is, by @thm-courant-fischer itself, equal to \( \lambda_{n+1-k}(\A) \): the first is the second line of the theorem at index \( n-k+1 \), and the second is the first line at the index \( j \) with \( n-j+1 = k \), namely \( j = n-k+1 \). So swapping either the order or the dimension returns the eigenvalue counted from the *other end* of the list.

For a witness take \( \A = \diag(2, 0) \) and \( k = 1 \), so that \( \lambda_1(\A) = 2 \). The first false expression maximizes over the single subspace \( W = F^2 \) the minimum of \( R_{\A} \), which is \( 0 \). The second minimizes over lines the maximum on the line, which is the value of \( R_{\A} \) on that line, and the smallest such value is again \( 0 \). Both return \( \lambda_2(\A) = 0 \) instead of \( 2 \). The mistake is invisible when \( n = 2k-1 \), since then \( n+1-k = k \), and this is exactly why it survives in the wild.
:::

::: {.check}
In the first line of @thm-courant-fischer, why is the dimension \( n-k+1 \) rather than \( k \)? Check your reason against \( k = 1 \).
:::

::: {.solution}
The competitor \( W \) must be forced to meet \( U_k = \Span(\q_1,\dots,\q_k) \), which has dimension \( k \); by @lem-subspace-intersection that needs \( \dim W > n - k \), and \( n-k+1 \) is the smallest such dimension. It must not be larger either: competitors of dimension \( n-k+2 \) would be forced to meet \( U_{k-1} \) as well, and by the theorem itself the min–max over them is \( \lambda_{k-1}(\A) \), the wrong eigenvalue.

At \( k = 1 \) the dimension is \( n-1+1 = n \), so the only competitor is \( W = F^n \), and the statement reads \( \lambda_1(\A) = \max_{\x\ne\0}R_{\A}(\x) \), which is @prp-rayleigh-basic. With the dimension \( k = 1 \) instead, we would be computing \( \min \) over lines of the single value of \( R_{\A} \) on the line, which is \( \lambda_n(\A) \) — the wrong end.
:::

::: {#exm-courant-fischer-3x3}
[Both forms on one matrix]

Let
\[
\A = \begin{pmatrix} 2 & 2 & 0 \\ 2 & 3 & 2 \\ 0 & 2 & 4\end{pmatrix} \in M_3(\nR) ,
\]
whose eigenvalues are \( 6, 3, 0 \), with orthonormal eigenvectors
\[
\q_1 = \tfrac13(1,2,2), \qquad
\q_2 = \tfrac13(2,1,-2), \qquad
\q_3 = \tfrac13(2,-2,1) .
\]
Verify both lines of @thm-courant-fischer for \( k = 2 \) by computing the witness and two competitors in each case.
:::

::: {.solution}
Throughout we use @lem-rayleigh-range-on-subspace: for a subspace \( W \) with orthonormal basis the columns of \( \Q \), the values of \( R_{\A} \) on \( W \) fill the interval between the smallest and largest eigenvalues of the \( 2\times2 \) matrix \( \B = \Q\tp\A\Q \).

**Max–min form**, \( \dim W = k = 2 \). The witness is \( U_2 = \Span(\q_1, \q_2) \); since \( \q_1, \q_2 \) are eigenvectors, \( \B = \diag(6, 3) \) and the minimum of \( R_{\A} \) on \( U_2 \) is \( 3 = \lambda_2(\A) \). Two competitors:

- \( W = \Span(\e_1, \e_2) \), where \( \B \) is the top-left \( 2\times 2 \) block \( \bigl(\begin{smallmatrix} 2 & 2 \\ 2 & 3\end{smallmatrix}\bigr) \), with eigenvalues \( \tfrac12(5 \pm \sqrt{17}) \). Its minimum is \( \tfrac12(5-\sqrt{17}) \approx 0.438 \), well below \( 3 \).
- \( W = \Span(\e_1, \e_3) \), where \( \B = \diag(2, 4) \) because \( a_{13} = 0 \). Its minimum is \( 2 \), again below \( 3 \).

**Min–max form**, \( \dim W = n-k+1 = 2 \) as well, since \( n = 3 \). The witness is \( L_2 = \Span(\q_2,\q_3) \), where \( \B = \diag(3, 0) \) and the maximum is \( 3 = \lambda_2(\A) \). The same two competitors now go the other way:

- on \( \Span(\e_1,\e_2) \) the maximum is \( \tfrac12(5+\sqrt{17}) \approx 4.562 > 3 \);
- on \( \Span(\e_1,\e_3) \) the maximum is \( 4 > 3 \).

So each competitor overshoots in the min–max form and undershoots in the max–min form, and the two witnesses pin \( \lambda_2(\A) = 3 \) from both sides. Notice that the competitor \( \Span(\e_1,\e_2) \) is the coordinate plane obtained by deleting the third row and column, and its two eigenvalues \( 0.438\ldots \) and \( 4.562\ldots \) are caught between consecutive eigenvalues \( 0 \le 0.438 \le 3 \le 4.562 \le 6 \) of \( \A \). That is no accident; it is the interlacing theorem of §04.
:::

## The two debts this pays at once

::: {#cor-loewner-eigenvalue-monotone}
[The Loewner Order Compares Every Eigenvalue]

Let \( \A, \B \in M_n(F) \) be Hermitian with \( \A \succeq \B \). Then
\[
\lambda_i(\A) \ \ge\ \lambda_i(\B) \qquad \text{for every } i = 1, \dots, n .
\]
:::


::: {.idea}
\( \A \succeq \B \) says the Rayleigh quotient of \( \A \) sits above that of \( \B \) at every vector. Courant–Fischer builds each \( \lambda_i \) out of the Rayleigh quotient by a minimum and then a maximum, and both operations preserve "everywhere above". So the domination passes straight through to every eigenvalue.
:::

::: {.proof}
By @def-loewner-order, \( \A \succeq \B \) means \( \A - \B \succeq 0 \), so \( \inner{(\A-\B)\x}{\x} \ge 0 \) for every \( \x \). Dividing by \( \inner{\x}{\x} > 0 \) for \( \x \ne \0 \),
\[
R_{\A}(\x) \ \ge\ R_{\B}(\x) \qquad \text{for every } \x \ne \0 .
\]

Fix \( i \) and let \( W \) be any subspace of \( F^n \) with \( \dim W = i \). Let \( \x_1 \in W \setminus\{\0\} \) attain \( \min_{\0\ne\x\in W}R_{\A}(\x) \), which exists by @lem-rayleigh-range-on-subspace. Then
\[
\min_{\0\ne\x\in W}R_{\A}(\x) = R_{\A}(\x_1) \ \ge\ R_{\B}(\x_1)
\ \ge\ \min_{\0\ne\x\in W}R_{\B}(\x) .
\]
So the function \( W \mapsto \min_{\0\ne\x\in W}R_{\A}(\x) \) dominates the corresponding function for \( \B \) at every \( W \), and therefore so do their maxima over the subspaces of dimension \( i \). By @thm-courant-fischer applied to \( \A \) and to \( \B \), those maxima are \( \lambda_i(\A) \) and \( \lambda_i(\B) \). This proves the corollary.
:::

::: {#exm-loewner-eigenvalue-check}
[Checking the corollary on a pair]

Let \( \A = \begin{psmallmatrix} 4 & 1 \\ 1 & 3\end{psmallmatrix} \) and \( \B = \begin{psmallmatrix} 2 & 1 \\ 1 & 2\end{psmallmatrix} \). Then \( \A - \B = \diag(2, 1) \), which is positive semidefinite, so \( \A \succeq \B \). The eigenvalues of \( \B \) are \( 3 \) and \( 1 \), from trace \( 4 \) and determinant \( 3 \); those of \( \A \) are \( \tfrac{7 \pm \sqrt5}{2} \approx 4.618,\ 2.382 \), from trace \( 7 \) and determinant \( 11 \). So \( \lambda_1(\A) \approx 4.618 \ge 3 = \lambda_1(\B) \) and \( \lambda_2(\A) \approx 2.382 \ge 1 = \lambda_2(\B) \), as the corollary demands. Note that the two gaps, \( \tfrac{1+\sqrt5}{2} \approx 1.618 \) and \( \tfrac{5-\sqrt5}{2} \approx 1.382 \), are different: the corollary orders the eigenvalues, and says nothing about moving them by the same amount.
:::

This settles an account opened in Chapter 13 §05. Discussing @thm-loewner-basic (b), which proved only \( \lambda_1(\A) \ge \lambda_1(\B) \) and \( \lambda_n(\A) \ge \lambda_n(\B) \), that section said: "The full statement is that \( \lambda_i(\A) \ge \lambda_i(\B) \) for **every** \( i \), not only for \( i = 1 \) and \( i = n \); but the intermediate eigenvalues have no description as a plain maximum over the whole unit sphere, and the min–max description that does the job is the Courant–Fischer theorem of Chapter 17." @cor-loewner-eigenvalue-monotone is that full statement, and the diagnosis was exact: what was missing was not an extra trick but a description of \( \lambda_i \) that two different matrices could be measured against. The proof above is short, and all of its weight is carried by @thm-courant-fischer.

::: {#cor-courant-fischer-operator}
[Courant–Fischer for a Self-Adjoint Operator]

Let \( V \) be a finite-dimensional inner product space over \( F = \nR \) or \( F = \nC \), with \( \dim V = n \ge 1 \), and let \( T \in \cL(V) \) be self-adjoint, with eigenvalues \( \lambda_1(T) \ge \dots \ge \lambda_n(T) \) repeated according to multiplicity. Then for every \( k \) with \( 1 \le k \le n \),
\[
\begin{aligned}
\lambda_k(T) &= \min_{\dim U = n-k+1}\ \max_{\0 \ne \v \in U} \frac{\inner{T\v}{\v}}{\inner{\v}{\v}} \\[2pt]
&= \max_{\dim U = k}\ \min_{\0 \ne \v \in U} \frac{\inner{T\v}{\v}}{\inner{\v}{\v}} ,
\end{aligned}
\]
where \( U \) runs over the subspaces of \( V \) of the stated dimension.
:::

::: {.idea}
Transport the theorem along coordinates. An orthonormal basis of eigenvectors turns \( V \) into \( F^n \) without changing any inner product, turns \( T \) into a real diagonal matrix, and matches subspaces with subspaces of the same dimension. There is nothing to prove beyond checking that each of those three things is true.
:::

::: {.proof}
By @prp-self-adjoint-immediate (c) a self-adjoint operator is normal, so @thm-spectral-complex over \( \nC \), and @thm-spectral-real over \( \nR \), give an orthonormal basis \( \sE = (\e_1, \dots, \e_n) \) of \( V \) consisting of eigenvectors of \( T \); relabel it so that \( T\e_i = \lambda_i(T)\e_i \) with the eigenvalues in decreasing order, which is possible because they are real by @thm-self-adjoint-real-eigenvalues. In particular the eigenvalue list of \( T \), repeated according to multiplicity, has exactly \( n \) entries.

Let \( \Phi \colon V \to F^n \), \( \Phi(\v) = \coord{\v}{\sE} \), be the coordinate map, an isomorphism by @cor-coordinate-isomorphism. By @thm-orthonormal-coordinates (b), \( \inner{\Phi\u}{\Phi\v} = \inner{\u}{\v} \) for all \( \u, \v \in V \), so \( \Phi \) is an isometric isomorphism in the sense of @cor-inner-product-spaces-isomorphic. Put \( \A = \mtx{T}{\sE}{\sE} = \diag(\lambda_1(T), \dots, \lambda_n(T)) \), a real diagonal matrix, hence Hermitian, with \( \lambda_i(\A) = \lambda_i(T) \) for every \( i \). By @thm-matrix-of-map-coordinates, \( \Phi(T\v) = \A\,\Phi(\v) \).

Consequently, for \( \v \ne \0 \),
\[
\frac{\inner{T\v}{\v}}{\inner{\v}{\v}}
= \frac{\inner{\A\Phi\v}{\Phi\v}}{\inner{\Phi\v}{\Phi\v}}
= R_{\A}(\Phi\v) ,
\]
and \( \Phi\v \ne \0 \) because \( \Phi \) is injective. Finally \( U \mapsto \Phi(U) \) is a bijection from the subspaces of \( V \) to the subspaces of \( F^n \) preserving dimension, by @thm-isomorphism-preserves-bases, and it matches the non-zero vectors of \( U \) with those of \( \Phi(U) \). So each of the two displayed expressions equals the corresponding expression for \( \A \) in @thm-courant-fischer, which is \( \lambda_k(\A) = \lambda_k(T) \). This proves the corollary.
:::

This is the statement Chapter 12 §02 promised when it wrote that "the maximization picture returns in Chapter 17, where the Rayleigh quotient and the Courant–Fischer theorem describe every eigenvalue of a self-adjoint operator by optimization". The picture has returned and the description is complete: every eigenvalue, not merely the extreme two, and stated for an operator on an abstract inner product space, which is the setting Chapter 12 worked in. The remark in §01 records what it cost — nothing. Chapter 12 declined the maximization route because it would have needed the extreme value theorem to know that a maximum exists; here the spectral theorem supplies the maximizing vectors explicitly, so the min–max description is a *consequence* of Chapter 12 rather than an alternative to it, and no analysis has been imported.

What has been bought is comparison. Two Hermitian matrices are now comparable eigenvalue by eigenvalue whenever their Rayleigh quotients are comparable vector by vector, and @cor-loewner-eigenvalue-monotone is the first instance. Section 3 takes the same idea and applies it to \( \A \) and \( \A + \E \), where the quotients differ by at most \( \norm{\E}_2 \), and gets the perturbation bound that Chapter 16 could not state.

## Exercises

### A. Check your understanding

:::: {#exr-courant-fischer-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State both lines of @thm-courant-fischer, being careful about which dimension goes with which line.
2. State @lem-subspace-intersection, and say at which point of the proof of @thm-courant-fischer it is used and what it is used on.
3. Determine whether the following is correct, and justify your answer:
   \[
   \lambda_k(\A) = \min_{\dim W = k}\ \max_{\0\ne\x\in W} R_{\A}(\x) .
   \]
4. Write the first line of @thm-courant-fischer in the increasing-index convention \( \mu_1 \le \dots \le \mu_n \).
5. Explain in one or two sentences why @thm-loewner-basic (b) could not be extended to intermediate eigenvalues by the argument Chapter 13 used, and what @thm-courant-fischer supplies instead.
:::
::::

::: {.solution}
(a) For Hermitian \( \A \in M_n(F) \) and \( 1 \le k \le n \): \( \lambda_k(\A) = \min\max \) over subspaces of dimension \( n-k+1 \) of the Rayleigh quotient, and \( = \max\min \) over subspaces of dimension \( k \). The large dimension goes with the minimum of maxima; the small one with the maximum of minima.

(b) If \( U, W \) are subspaces of an \( n \)-dimensional space with \( \dim U + \dim W > n \), then \( U \cap W \ne \{\0\} \). It is used in Step 2, applied to an arbitrary competitor \( W \) of dimension \( n-k+1 \) and the span \( U_k \) of the top \( k \) eigenvectors, whose dimensions add to \( n+1 \).

(c) Incorrect. By @thm-courant-fischer itself, that expression is the first line evaluated at the index \( j \) with \( n-j+1 = k \), so it equals \( \lambda_{n-k+1}(\A) \). For \( \A = \diag(2,0) \) and \( k = 1 \) it returns \( 0 \), not \( \lambda_1(\A) = 2 \).

(d) \( \mu_j = \min_{\dim W = j}\max_{\0\ne\x\in W}R_{\A}(\x) \), obtained by setting \( k = n+1-j \).

(e) Chapter 13's argument evaluated the quadratic form at a vector that is extremal for the *other* matrix, which works only when the extremal vector is characterized by a plain maximum over the whole sphere — true for \( \lambda_1 \) and \( \lambda_n \) and for no other index, since the range of \( R_{\A} \) is an interval (@prp-rayleigh-basic). @thm-courant-fischer supplies a description of every \( \lambda_i \) as an optimization over a family of subspaces that does not depend on the matrix, so the same subspace can be fed to both matrices; that is exactly what the proof of @cor-loewner-eigenvalue-monotone does.
:::

### B. Practice

:::: {#exr-courant-fischer-b1}
[B1: Both forms on a diagonal matrix]

Let \( \A = \diag(5, 2, -1) \in M_3(\nR) \) and \( k = 2 \).

::: {.enumerate options="label=(\alph*)"}
1. Give the witness subspace for the max–min form, compute the minimum of \( R_{\A} \) on it, and check the value against @thm-courant-fischer.
2. Do the same for the min–max form.
3. Put \( \u = \tfrac1{\sqrt2}(0,1,1) \). Compute the minimum of \( R_{\A} \) over the non-zero vectors of \( \Span(\e_1, \u) \), and over those of \( \Span(\e_2, \e_3) \), and verify that neither subspace beats the witness in (a).
:::
::::

::: {.solution}
(a) The eigenvalues are \( \lambda_1 = 5 \), \( \lambda_2 = 2 \), \( \lambda_3 = -1 \) with eigenvectors \( \e_1, \e_2, \e_3 \). The witness is \( U_2 = \Span(\e_1,\e_2) \), of dimension \( k = 2 \). There \( \B = \diag(5,2) \), so by @lem-rayleigh-range-on-subspace the values of \( R_{\A} \) fill \( [2,5] \) and the minimum is \( 2 = \lambda_2(\A) \).

(b) Here \( n-k+1 = 2 \) as well, and the witness is \( L_2 = \Span(\e_2,\e_3) \), where \( \B = \diag(2,-1) \); the values fill \( [-1,2] \) and the maximum is \( 2 = \lambda_2(\A) \).

(c) For \( W = \Span(\e_1, \u) \) the two spanning vectors are orthonormal, and
\[
\B = \begin{pmatrix} 5 & 0 \\ 0 & \tfrac12(2 - 1)\end{pmatrix} = \diag\bigl(5, \tfrac12\bigr) ,
\]
the off-diagonal entry vanishing because \( \A\e_1 = 5\e_1 \) is orthogonal to \( (0,1,1) \). So the minimum is \( \tfrac12 < 2 \). For \( W = \Span(\e_2,\e_3) \) we get \( \B = \diag(2,-1) \) and minimum \( -1 < 2 \). Neither competitor reaches \( \lambda_2(\A) = 2 \), as @thm-courant-fischer requires.
:::

:::: {#exr-courant-fischer-b2}
[B2: Shifting by a multiple of the identity]

Let \( \A \in M_n(F) \) be Hermitian and let \( c \in \nR \). Prove that \( \lambda_k(\A + c\I) = \lambda_k(\A) + c \) for every \( k \), using the first line of @thm-courant-fischer for both matrices.
::::

::: {.solution}
The matrix \( \A + c\I \) is Hermitian, since \( c \) is real. For every \( \x \ne \0 \),
\[
R_{\A + c\I}(\x) = \frac{\inner{\A\x}{\x} + c\inner{\x}{\x}}{\inner{\x}{\x}}
= R_{\A}(\x) + c .
\]
Adding a constant to a real-valued function adds it to every maximum and every minimum of that function over any non-empty set. So for each subspace \( W \),
\[
\max_{\0\ne\x\in W}R_{\A+c\I}(\x) = \Bigl(\max_{\0\ne\x\in W}R_{\A}(\x)\Bigr) + c ,
\]
and taking the minimum over all \( W \) of dimension \( n-k+1 \) adds \( c \) again. By @thm-courant-fischer applied to \( \A + c\I \) on the left and to \( \A \) on the right, \( \lambda_k(\A + c\I) = \lambda_k(\A) + c \).
:::

:::: {#exr-courant-fischer-b3}
[B3: Comparing two matrices]

Let
\[
\A = \begin{pmatrix} 3 & 1 \\ 1 & 3\end{pmatrix},
\qquad
\B = \begin{pmatrix} 2 & 0 \\ 0 & 1\end{pmatrix} .
\]
Verify that \( \A \succeq \B \), compute both eigenvalue lists, and check @cor-loewner-eigenvalue-monotone. Check whether \( \lambda_1(\A) - \lambda_1(\B) \le \lambda_1(\A - \B) \) holds for this pair. (Whether it holds for every pair is a question for Section 3.)
::::

::: {.solution}
\( \A - \B = \bigl(\begin{smallmatrix} 1 & 1 \\ 1 & 2\end{smallmatrix}\bigr) \) is symmetric with leading principal minors \( 1 > 0 \) and \( \det = 2 - 1 = 1 > 0 \), so \( \A - \B \succ 0 \) by @thm-pd-characterizations; in particular \( \A \succeq \B \).

The eigenvalues: \( \A \) has \( p_{\A}(x) = (x-3)^2 - 1 \), so \( \lambda_1(\A) = 4 \), \( \lambda_2(\A) = 2 \); and \( \B \) is diagonal with \( \lambda_1(\B) = 2 \), \( \lambda_2(\B) = 1 \). Indeed \( 4 \ge 2 \) and \( 2 \ge 1 \), as @cor-loewner-eigenvalue-monotone requires.

For the last question, \( \A - \B \) has trace \( 3 \) and determinant \( 1 \), so its eigenvalues are \( \tfrac12(3 \pm \sqrt5) \) and \( \lambda_1(\A - \B) = \tfrac12(3+\sqrt5) \approx 2.618 \). The inequality asks whether \( 4 - 2 \le 2.618 \), which holds. (It is not an accident: it is the simplest of the perturbation inequalities of §03, which carry Weyl's name. Note that @cor-loewner-eigenvalue-monotone alone gives no upper bound on the gap \( \lambda_i(\A) - \lambda_i(\B) \).)
:::

### C. Going deeper

:::: {#exr-courant-fischer-c1}
[C1: The definite generalized eigenvalue problem]

Let \( \A, \B \in M_n(F) \) be Hermitian with \( \A \succ 0 \), and recall @def-generalized-eigenvalue: \( \lambda \) is a generalized eigenvalue of the pair \( (\A,\B) \) when \( \B\x = \lambda\A\x \) for some \( \x \ne \0 \). Define the **generalized Rayleigh quotient**
\[
R_{\A,\B}(\x) = \frac{\inner{\B\x}{\x}}{\inner{\A\x}{\x}} \qquad (\x \ne \0) .
\]

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( R_{\A,\B} \) is well defined and real-valued.
2. Put \( \C = \A^{-1/2}\B\A^{-1/2} \). Prove that \( \C \) is Hermitian and that \( \det(\B - \lambda\A) = \det(\A)\det(\C - \lambda\I) \), so that the generalized eigenvalues of \( (\A,\B) \), with multiplicity, are exactly the eigenvalues of \( \C \). Write them \( d_1 \ge \dots \ge d_n \).
3. Prove that for every \( k \),
\[
d_k = \min_{\dim W = n-k+1}\ \max_{\0\ne\x\in W}R_{\A,\B}(\x) .
\]
:::

*Hint for (c): the substitution \( \x = \A^{-1/2}\y \).*
::::

::: {.solution}
(a) By @thm-psd-square-root and @thm-pd-characterizations, \( \A \succ 0 \) has a positive definite square root \( \A^{1/2} \), which is invertible; write \( \A^{-1/2} \) for its inverse, again Hermitian and positive definite. For \( \x \ne \0 \), \( \inner{\A\x}{\x} > 0 \) by definiteness, so the denominator is a non-zero real; the numerator is real by @prp-self-adjoint-immediate (a). So the quotient is a well-defined real number.

(b) \( \C^{*} = \A^{-1/2}\B^{*}\A^{-1/2} = \C \). Since \( \A^{1/2}\C\A^{1/2} = \B \) and \( \A^{1/2}\A^{1/2} = \A \),
\[
\B - \lambda\A = \A^{1/2}(\C - \lambda\I)\A^{1/2} ,
\]
so taking determinants and using @thm-det-multiplicative gives
\[
\det(\B-\lambda\A) = \det(\A^{1/2})^2\det(\C-\lambda\I) = \det(\A)\det(\C - \lambda\I) .
\] Since \( \det \A \ne 0 \), the two polynomials in \( \lambda \) have the same roots with the same multiplicities. By @thm-generalized-eigenvalues-real (b) the generalized eigenvalues of \( (\A,\B) \) are the roots of \( \det(\B - \lambda\A) \), so they are the eigenvalues of \( \C \), all real because \( \C \) is Hermitian.

(c) Put \( \S = \A^{-1/2} \), which is Hermitian and invertible. For \( \y \ne \0 \) set \( \x = \S\y \ne \0 \). Then
\[
\inner{\B\x}{\x} = \inner{\S\B\S\y}{\y} = \inner{\C\y}{\y},
\qquad
\inner{\A\x}{\x} = \inner{\S\A\S\y}{\y} = \inner{\y}{\y} ,
\]
using \( \S\A\S = \A^{-1/2}\A\A^{-1/2} = \I \). Hence \( R_{\A,\B}(\S\y) = R_{\C}(\y) \). The map \( \y \mapsto \S\y \) is an isomorphism of \( F^n \), so \( W \mapsto \S^{-1}W \) is a bijection of the subspaces of dimension \( n-k+1 \) onto themselves, matching non-zero vectors with non-zero vectors. Therefore
\[
\max_{\0\ne\x\in W}R_{\A,\B}(\x) = \max_{\0\ne\y\in \S^{-1}W}R_{\C}(\y) ,
\]
and minimizing both sides over all \( W \) of dimension \( n-k+1 \) gives, by @thm-courant-fischer applied to \( \C \), the value \( \lambda_k(\C) = d_k \).
:::

:::: {#exr-courant-fischer-c2}
[C2: How much weaker the eigenvalue comparison is]

::: {.enumerate options="label=(\alph*)"}
1. Give Hermitian \( \A, \B \in M_2(\nR) \) with \( \lambda_i(\A) \ge \lambda_i(\B) \) for \( i = 1, 2 \) but \( \A \not\succeq \B \). So the converse of @cor-loewner-eigenvalue-monotone is false.
2. Prove that if \( \A \) and \( \B \) are Hermitian with \( \lambda_i(\A) \ge \lambda_i(\B) \) for every \( i \) and \( \tr\A = \tr\B \), then \( \lambda_i(\A) = \lambda_i(\B) \) for every \( i \).
3. Prove that if \( \A \succeq \B \) and \( \tr\A = \tr\B \), then \( \A = \B \).
:::
::::

::: {.solution}
(a) Take \( \A = \diag(2, 0) \) and \( \B = \diag(0, 1) \). Then \( \lambda_1(\A) = 2 \ge 1 = \lambda_1(\B) \) and \( \lambda_2(\A) = 0 \ge 0 = \lambda_2(\B) \). But \( \A - \B = \diag(2, -1) \) has the eigenvalue \( -1 < 0 \), so \( \A - \B \not\succeq 0 \) by @thm-psd-characterizations and \( \A \not\succeq \B \). Ordering the two spectra says nothing about how the eigen*vectors* are placed relative to each other, and the Loewner order sees both.

(b) By @thm-trace-det-eigenvalues the trace is the sum of the eigenvalues with multiplicity, so
\[
0 = \tr\A - \tr\B = \sum_{i=1}^{n}\bigl(\lambda_i(\A) - \lambda_i(\B)\bigr) .
\]
Every summand is \( \ge 0 \) by hypothesis, and a sum of non-negative reals is zero only if each is zero. Hence \( \lambda_i(\A) = \lambda_i(\B) \) for every \( i \).

(c) Put \( \C = \A - \B \), Hermitian with \( \C \succeq 0 \), so every eigenvalue of \( \C \) is \( \ge 0 \) by @thm-psd-characterizations. Also \( \tr\C = \tr\A - \tr\B = 0 \), which by @thm-trace-det-eigenvalues is the sum of those eigenvalues; a sum of non-negative reals vanishing forces each to vanish, so every eigenvalue of \( \C \) is \( 0 \). By @cor-spectral-complex-matrix (or @cor-spectral-real-matrix), \( \C = \U\D\U^{*} \) with \( \D \) the diagonal matrix of eigenvalues, which is \( \0 \); hence \( \C = \0 \) and \( \A = \B \). (One may also finish with (b) and @cor-loewner-eigenvalue-monotone, which give the equality of the two spectra but not yet of the matrices; the trace argument on \( \C \) is what closes the gap.)
:::

:::: {#exr-courant-fischer-c3}
[C3: Does enlarging the field change the answer?]

Let \( \A \in M_n(\nR) \) be symmetric. It may be read as an element of \( M_n(\nC) \), where it is Hermitian, and then @thm-courant-fischer minimizes over a much larger collection of subspaces.

::: {.enumerate options="label=(\alph*)"}
1. Prove that the eigenvalue lists of \( \A \) over \( \nR \) and over \( \nC \), with multiplicity, are the same.
2. Deduce that for every \( k \),
\[
\min_{\substack{W \subseteq \nR^n \\ \dim W = n-k+1}} \max_{\0\ne\x\in W}R_{\A}(\x)
= \min_{\substack{W \subseteq \nC^n \\ \dim W = n-k+1}} \max_{\0\ne\x\in W}R_{\A}(\x) .
\]
3. Show that the second minimum really does range over strictly more subspaces, by exhibiting a one-dimensional subspace of \( \nC^2 \) that contains no non-zero real vector.
:::
::::

::: {.solution}
(a) By @cor-spectral-real-matrix there is an orthogonal \( \Q \in M_n(\nR) \) and a real diagonal \( \D \) with \( \A = \Q\D\Q\tp \), and the diagonal of \( \D \) is the eigenvalue list of \( \A \) over \( \nR \) with multiplicity. Read over \( \nC \), the same \( \Q \) is unitary, since \( \Q^{*} = \conj{\Q}\tp = \Q\tp = \Q^{-1} \), and the same equation \( \A = \Q\D\Q^{*} \) holds. So \( \A \) is unitarily similar over \( \nC \) to the same \( \D \), and its complex eigenvalue list with multiplicity is again the diagonal of \( \D \).

(b) Apply @thm-courant-fischer twice: once with \( F = \nR \), where the left-hand side equals \( \lambda_k(\A) \) computed over \( \nR \), and once with \( F = \nC \), where the right-hand side equals \( \lambda_k(\A) \) computed over \( \nC \). By (a) these are the same number.

(c) Take \( W = \Span_{\nC}\{(1, i)\} \subseteq \nC^2 \). A non-zero element of \( W \) is \( c(1,i) = (c, ci) \) with \( c \ne 0 \); for it to be real we would need \( c \in \nR \) and \( ci \in \nR \), and \( c \ne 0 \) makes the second impossible. So \( W \) is not the complex span of any real subspace.

The lesson is worth stating. Enlarging the field adds competitors to the minimization, which can only push the minimum **down**, and adds vectors to each inner maximization, which can only push those maxima **up**. The two effects cancel exactly, because both the witness subspace and the bound of Step 2 in the proof of @thm-courant-fischer survive the enlargement unchanged: the witness is spanned by real eigenvectors, and the dimension count of @lem-subspace-intersection holds over any field.
:::
