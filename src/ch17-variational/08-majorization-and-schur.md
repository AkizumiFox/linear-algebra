# The Diagonal and the Spectrum

A Hermitian matrix carries two lists of \( n \) real numbers: its diagonal entries, read off at a glance, and its eigenvalues, computed with effort. Since Chapter 9 we have known that the two lists have the same sum, the trace. This section asks what else the eigenvalues force on the diagonal, and answers the question completely. The answer needs a name, **majorization**. One half of it, Schur's theorem, is §06's bound on partial sums of the diagonal in the new language. The other half, Horn's theorem, says that nothing more is forced; it is proved by an induction driven by a single \( 2 \times 2 \) rotation. The section ends with a short second proof of Hadamard's determinant inequality.

**Throughout, the field is \( \nR \) or \( \nC \), and every matrix whose eigenvalues are indexed is Hermitian**, with its eigenvalues real and listed **decreasingly** with multiplicity, \( \lambda_1(\A) \ge \dots \ge \lambda_n(\A) \). Two vectors in \( \nR^n \) are attached to such an \( \A \in M_n(F) \):
\[
\begin{aligned}
\d(\A) &= (a_{11}, a_{22}, \dots, a_{nn}) , \\
\vlambda(\A) &= \bigl(\lambda_1(\A), \lambda_2(\A), \dots, \lambda_n(\A)\bigr) .
\end{aligned}
\]
The first is the **diagonal vector**, in the order the entries sit on the diagonal; the second is the **eigenvalue vector**, always in decreasing order. The diagonal entries are real because \( \A^{*} = \A \) gives \( a_{ii} = \conj{a_{ii}} \), and the eigenvalues are real by @thm-self-adjoint-real-eigenvalues. The bold \( \d(\A) \) is a vector, not the diagonal matrix \( \diag(a_{11}, \dots, a_{nn}) \).

Two facts about a Hermitian \( \A \) are used below. The spectral theorem (@cor-spectral-complex-matrix over \( \nC \), @cor-spectral-real-matrix over \( \nR \)) makes \( \A \) similar to the real diagonal matrix of its eigenvalues, so its characteristic polynomial splits as \( \prod_i (x - \lambda_i(\A)) \). Then @thm-trace-det-eigenvalues gives
\[
\tr \A = \sum_{i=1}^{n} \lambda_i(\A) , \qquad \det \A = \prod_{i=1}^{n} \lambda_i(\A) .
\]

## What the diagonal already knows

Start with the smallest interesting case. The matrix
\[
\A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}
\]
has \( \d(\A) = (2, 2) \) and eigenvalues \( 3 \) and \( 1 \), with eigenvectors \( (1,1) \) and \( (1,-1) \), so \( \vlambda(\A) = (3, 1) \). The totals agree, \( 2 + 2 = 4 = 3 + 1 \). But the two lists are not alike: the diagonal is perfectly even, while the spectrum is spread out.

A larger example shows the pattern better. The tridiagonal matrix
\[
\A = \begin{pmatrix} 3 & 2 & 0 \\ 2 & 4 & 2 \\ 0 & 2 & 5 \end{pmatrix}
\]
has eigenvectors \( (1, 2, 2) \), \( (-2, -1, 2) \) and \( (2, -2, 1) \), with eigenvalues \( 7 \), \( 4 \) and \( 1 \). To check the first, \( \A(1,2,2) = (3 + 4,\ 2 + 8 + 4,\ 4 + 10) = (7, 14, 14) \); the other two are checked the same way. So \( \vlambda(\A) = (7, 4, 1) \), while \( \d(\A) = (3, 4, 5) \). Sort the diagonal decreasingly to \( (5, 4, 3) \) and compare the running totals of the two lists:
\[
\begin{array}{c|ccc}
k & 1 & 2 & 3 \\ \hline
\text{largest } k \text{ diagonal entries} & 5 & 9 & 12 \\
\text{largest } k \text{ eigenvalues} & 7 & 11 & 12
\end{array}
\]
Each running total of the eigenvalues is at least the matching running total of the diagonal, and at \( k = n \) the two are equal. None of this is new. @cor-ky-fan-diagonal says that any \( k \) diagonal entries add up to at most \( \lambda_1(\A) + \dots + \lambda_k(\A) \), with equality at \( k = n \), and the \( k \) largest diagonal entries are one such choice. What is new is the point of view: to ask which diagonals are **possible**, the corollary's list of inequalities has to be read as a single relation between two vectors.

Two features of this comparison deserve notice. First, the diagonal had to be **sorted**, and this is forced. For a permutation matrix \( \P_\sigma \) (@def-permutation-matrix), \( \P_\sigma\tp = \P_\sigma^{-1} \) by @lem-permutation-matrices (b), so \( \P_\sigma\tp\A\P_\sigma \) is Hermitian with the same eigenvalues as \( \A \), and its \( (j,j) \) entry is \( \e_{\sigma(j)}\tp\A\e_{\sigma(j)} = a_{\sigma(j)\sigma(j)} \). Relabeling the basis shuffles the diagonal and fixes the spectrum, so any true relation between \( \d(\A) \) and \( \vlambda(\A) \) must ignore the order of the diagonal. Second, the comparison is between **running totals from the top**, and it measures how unevenly a fixed total is spread.

## Majorization

*One vector is majorized by another when the two have the same total but the second piles more of it onto its largest entries: every "top \( k \)" sum of the second is at least that of the first.*

The sorting step gets a notation first. For \( \x = (x_1, \dots, x_n) \in \nR^n \), the **decreasing rearrangement** \( \x^{\downarrow} = (x^{\downarrow}_1, \dots, x^{\downarrow}_n) \) is the vector with the same entries, repeated as often as in \( \x \), listed so that \( x^{\downarrow}_1 \ge x^{\downarrow}_2 \ge \dots \ge x^{\downarrow}_n \). For example, \( (0, 3, 1, 3)^{\downarrow} = (3, 3, 1, 0) \). In this notation, \( \vlambda(\A) = \vlambda(\A)^{\downarrow} \) by convention, while \( \d(\A) \) usually needs sorting.

:::: {#def-majorization}
[Majorization]

Let \( n \ge 1 \) and let \( \x, \y \in \nR^n \) be **real** vectors with the **same number** of entries. We say that \( \x \) is **majorized by** \( \y \), and write \( \x \prec \y \), if

::: {.enumerate options="label=(M\arabic*)"}
1. \( \displaystyle\sum_{i=1}^{k} x^{\downarrow}_i \le \sum_{i=1}^{k} y^{\downarrow}_i \) for **every** \( k = 1, \dots, n-1 \); and
2. \( \displaystyle\sum_{i=1}^{n} x_i = \sum_{i=1}^{n} y_i \)  (**equal totals**).
:::

We say that \( \x \) is **weakly majorized by** \( \y \), and write \( \x \prec_w \y \), if the inequality in (M1) holds for **every** \( k = 1, \dots, n \), including \( k = n \), and (M2) is dropped.
::::

In words, clause by clause. (M1) sorts both vectors and compares their **running totals from the top**: the largest entry of \( \x \) is at most the largest entry of \( \y \), the two largest of \( \x \) add up to at most the two largest of \( \y \), and so on up to \( k = n - 1 \). The word **every** matters: one failing \( k \) refutes \( \x \prec \y \). (M2) says the totals are equal; a sum does not care about order, so no sorting is needed there. Weak majorization keeps (M1), adds its case \( k = n \), which reads \( \sum_i x_i \le \sum_i y_i \), and asks nothing more. Comparing the definitions: \( \x \prec \y \) holds **exactly when** \( \x \prec_w \y \) and the totals are equal.

There is an equivalent way to read (M1) from the bottom. Subtracting the \( k \)-th running total from the equal totals of (M2) gives
\[
\sum_{i=k+1}^{n} x^{\downarrow}_i \ \ge\ \sum_{i=k+1}^{n} y^{\downarrow}_i \qquad (k = 1, \dots, n-1) ,
\]
so under (M2), the \( n-k \) **smallest** entries of \( \x \) add up to at least the \( n-k \) smallest entries of \( \y \). The vector \( \y \) is more extreme at both ends: its top is heavier and its bottom is lighter.

The definition makes sense because \( \x^{\downarrow} \) is determined by \( \x \): when two entries are equal, it does not matter which is written first. A consequence worth recording: **the relation sees only which numbers occur in each vector and how often, not where they sit.** If \( \x' \) is a rearrangement of \( \x \) and \( \y' \) of \( \y \), then \( \x \prec \y \) if and only if \( \x' \prec \y' \), because the rearrangements have the same decreasing rearrangements and the same totals.

::: {#exm-majorization-first-examples}
[A chain, the two extremes, and size one]

Check each claim against @def-majorization.

::: {.enumerate options="label=(\alph*)"}
1. \( (1, 1, 1) \prec (2, 1, 0) \prec (3, 0, 0) \).
2. For every \( \x \in \nR^n \) with mean \( m = \tfrac1n\sum_i x_i \), the **flat vector** \( m\1 = (m, \dots, m) \) satisfies \( m\1 \prec \x \).
3. For every \( \x \in \nR^n \) with **non-negative** entries and total \( s = \sum_i x_i \), \( \x \prec (s, 0, \dots, 0) \).
4. For \( n = 1 \), \( \x \prec \y \) if and only if \( \x = \y \).
:::
:::

::: {.solution}
(a) All three vectors are already decreasing, and all have total \( 3 \), so (M2) holds for both pairs. Their running totals are
\[
(1, 1, 1)\colon\ 1,\ 2,\ 3; \qquad (2, 1, 0)\colon\ 2,\ 3,\ 3; \qquad (3, 0, 0)\colon\ 3,\ 3,\ 3 .
\]
At \( k = 1 \) and \( k = 2 \) the first row is at most the second (\( 1 \le 2 \), \( 2 \le 3 \)), and the second is at most the third (\( 2 \le 3 \), \( 3 \le 3 \)). So (M1) holds for both pairs.

(b) The totals are \( nm = \sum_i x_i \), so (M2) holds. For (M1), fix \( k \) and let \( a = \tfrac1k\sum_{i \le k} x^{\downarrow}_i \) be the average of the \( k \) largest entries. Each of these is at least \( x^{\downarrow}_k \), so \( a \ge x^{\downarrow}_k \). Every remaining entry \( x^{\downarrow}_j \) with \( j > k \) is at most \( x^{\downarrow}_k \), hence at most \( a \). Therefore
\[
nm = \sum_{i \le k} x^{\downarrow}_i + \sum_{j > k} x^{\downarrow}_j \le ka + (n - k)a = na ,
\]
so \( m \le a \), and multiplying by \( k \) gives \( km \le \sum_{i \le k} x^{\downarrow}_i \). The left side is the \( k \)-th running total of \( m\1 \). This is (M1).

(c) The totals are both \( s \). Every running total of \( (s, 0, \dots, 0) \) equals \( s \), and \( \sum_{i \le k} x^{\downarrow}_i \le s \) because the omitted entries \( x^{\downarrow}_{k+1}, \dots, x^{\downarrow}_n \) are \( \ge 0 \). This is (M1). Non-negativity is really needed: \( (1, -1) \) has total \( 0 \), but \( (1, -1) \prec (0, 0) \) fails at \( k = 1 \), since \( 1 > 0 \).

(d) For \( n = 1 \) there are no values of \( k \) in (M1), since \( k \) runs from \( 1 \) to \( 0 \). So only (M2) remains, and it says \( x_1 = y_1 \).
:::

Parts (b) and (c) are the two ends of the order: among vectors with a given total, the flat vector is the most evenly spread, and among non-negative ones, the vector that puts everything in one entry is the least. Part (d) is the degenerate case: with a single entry there is nothing to spread, and the relation collapses to equality.

The chain in (a) might suggest that any two vectors with the same total can be ranked this way. They cannot.

::: {#exm-majorization-incomparable}
[Neither majorizes the other]

Show that \( \x = (4, 1, 1) \) and \( \y = (3, 3, 0) \) have the same total, that neither \( \x \prec \y \) nor \( \y \prec \x \), and that both are majorized by \( (4, 2, 0) \).
:::

::: {.solution}
Both totals are \( 6 \), and both vectors are already decreasing. Their running totals are
\[
\x\colon\ 4,\ 5,\ 6; \qquad \y\colon\ 3,\ 6,\ 6 .
\]
At \( k = 1 \), \( 4 > 3 \), so (M1) fails for \( \x \prec \y \). At \( k = 2 \), \( 6 > 5 \), so (M1) fails for \( \y \prec \x \). The vector \( (4, 2, 0) \) has total \( 6 \) and running totals \( 4, 6, 6 \), which are at least both \( 4, 5 \) and \( 3, 6 \) at \( k = 1, 2 \). So \( \x \prec (4, 2, 0) \) and \( \y \prec (4, 2, 0) \).
:::

This is the non-example by minimal change. Start from the comparable pair \( (4,1,1) \prec (4,2,0) \), move one unit in the second vector from its top entry to its middle entry to get \( (3,3,0) \), and the pair becomes incomparable. (M2) still holds; what fails is (M1), at a **different** \( k \) in each direction. Spreading is not a single number.

The picture makes this visible. Plot the running totals of a sorted vector against \( k \), joined by segments, starting from \( (0, 0) \). Then \( \x \prec \y \) says that the curve of \( \y \) lies on or above the curve of \( \x \) and ends at the same height. Two curves can also cross.

\begin{center}
\begin{tikzpicture}[lab/.style={font=\small}, dot/.style={circle, fill, inner sep=1.1pt}]
  \begin{scope}[xscale=1.1, yscale=0.8]
    \draw[->, gray] (0,0) -- (3.6,0) node[right, black, lab] {$k$};
    \draw[->, gray] (0,0) -- (0,3.6);
    \foreach \tk in {1,2,3} {
      \draw[gray] (\tk,0.08) -- (\tk,-0.08) node[below, black, lab] {$\tk$};
      \draw[gray] (0.08,\tk) -- (-0.08,\tk) node[left, black, lab] {$\tk$};
    }
    \draw[thick, dotted] (0,0) -- (1,1) -- (2,2) -- (3,3);
    \draw[thick, dashed] (0,0) -- (1,2) -- (2,3) -- (3,3);
    \draw[very thick] (0,0) -- (1,3) -- (2,3) -- (3,3);
    \foreach \p in {(1,1),(2,2),(1,2),(2,3),(1,3),(3,3)} \node[dot] at \p {};
    \node[lab, align=left, anchor=north west] at (-0.3,-0.7)
      {solid: $(3,0,0)$\\ dashed: $(2,1,0)$\\ dotted: $(1,1,1)$\\ nested, same endpoint};
  \end{scope}
  \begin{scope}[xshift=5.4cm, xscale=1.1, yscale=0.4]
    \draw[->, gray] (0,0) -- (3.6,0) node[right, black, lab] {$k$};
    \draw[->, gray] (0,0) -- (0,7.2);
    \foreach \tk in {1,2,3} \draw[gray] (\tk,0.16) -- (\tk,-0.16) node[below, black, lab] {$\tk$};
    \foreach \sv in {2,4,6} \draw[gray] (0.08,\sv) -- (-0.08,\sv) node[left, black, lab] {$\sv$};
    \draw[very thick] (0,0) -- (1,4) -- (2,5) -- (3,6);
    \draw[thick, dashed] (0,0) -- (1,3) -- (2,6) -- (3,6);
    \foreach \p in {(1,4),(2,5),(3,6),(1,3),(2,6)} \node[dot] at \p {};
    \node[lab, align=left, anchor=north west] at (-0.3,-1.4)
      {solid: $(4,1,1)$\\ dashed: $(3,3,0)$\\ the curves cross:\\ incomparable};
  \end{scope}
\end{tikzpicture}
\end{center}

**Why this definition.** Each clause earns its place, and changing any one of them changes the subject.

- *Sorting.* Relabeling a basis shuffles \( \d(\A) \) and fixes \( \vlambda(\A) \), so a relation comparing unsorted entries would answer a question the matrix does not pose.
- *Running totals from the top, with \( \le \).* These are the quantities that @thm-ky-fan and @cor-ky-fan-diagonal control: the top \( k \) eigenvalues sum to a maximum. Totals from the bottom add nothing new, as shown above, because under (M2) they are the same information.
- *Equal totals.* This is the trace. Dropping it gives weak majorization, the right notion when there is no conservation law to enforce: \( (1, 0) \prec_w (2, 0) \), but \( (1, 0) \not\prec (2, 0) \), because the totals differ.

::: {.warning}
**\( \x \prec \y \) does not mean \( x_i \le y_i \), not even after sorting both vectors.** In \( (1, 1, 1) \prec (2, 1, 0) \), the third entries are \( 1 \) and \( 0 \), and \( 1 > 0 \). This is no accident: subtracting (M1) at \( k = n - 1 \) from (M2) gives \( x^{\downarrow}_n \ge y^{\downarrow}_n \) whenever \( \x \prec \y \), so at the bottom the inequality always runs the other way. Majorization compares **sums of the largest entries**, not entries one at a time.
:::

::: {.check}
Arrange the five vectors \( (2, 1, 1, 0) \), \( (4, 0, 0, 0) \), \( (1, 1, 1, 1) \), \( (3, 1, 0, 0) \) and \( (2, 2, 0, 0) \) in a chain \( \x^{(1)} \prec \x^{(2)} \prec \dots \prec \x^{(5)} \).
:::

::: {.solution}
All five are decreasing and all have total \( 4 \). Their running totals at \( k = 1, 2, 3 \) are
\[
\begin{aligned}
(1,1,1,1)&\colon\ 1,\ 2,\ 3; &\quad (2,1,1,0)&\colon\ 2,\ 3,\ 4; \\
(2,2,0,0)&\colon\ 2,\ 4,\ 4; &\quad (3,1,0,0)&\colon\ 3,\ 4,\ 4; \\
(4,0,0,0)&\colon\ 4,\ 4,\ 4 .
\end{aligned}
\]
Read in this order, each triple is entrywise at most the next, so
\[
(1,1,1,1) \prec (2,1,1,0) \prec (2,2,0,0) \prec (3,1,0,0) \prec (4,0,0,0) .
\]
The ends are the flat vector and the concentrated vector of @exm-majorization-first-examples (b) and (c), as they must be. These five happen to be comparable in pairs, but @exm-majorization-incomparable shows that this is not always so.
:::

## Majorization is an order

The first small result is that \( \prec \) behaves like an order, and it says precisely how it falls short of being a partial order on \( \nR^n \).

::: {#prp-majorization-basic}
[Basic Properties of Majorization]

Let \( \x, \y, \z \in \nR^n \).

::: {.enumerate options="label=(\alph*)"}
1. \( \x \prec \x \).
2. If \( \x \prec \y \) and \( \y \prec \z \), then \( \x \prec \z \).
3. If \( \x \prec \y \) and \( \y \prec \x \), then \( \x^{\downarrow} = \y^{\downarrow} \); that is, \( \y \) is a rearrangement of \( \x \).
:::

Statements (a) and (b) hold with \( \prec_w \) in place of \( \prec \).
:::

::: {.proof}
For \( k = 1, \dots, n \), write \( X_k = \sum_{i \le k} x^{\downarrow}_i \), and define \( Y_k \) and \( Z_k \) in the same way. Since \( X_n = \sum_i x_i \), @def-majorization says that \( \x \prec \y \) means \( X_k \le Y_k \) for \( k < n \) and \( X_n = Y_n \).

(a) \( X_k \le X_k \) for every \( k \), and \( X_n = X_n \).

(b) For \( k < n \), \( X_k \le Y_k \le Z_k \). At \( k = n \), \( X_n = Y_n = Z_n \). Hence \( \x \prec \z \).

(c) The hypotheses give \( X_k \le Y_k \) and \( Y_k \le X_k \) for \( k < n \), and \( X_n = Y_n \), so \( X_k = Y_k \) for every \( k = 1, \dots, n \). Put \( X_0 = Y_0 = 0 \). Then for each \( k \),
\[
x^{\downarrow}_k = X_k - X_{k-1} = Y_k - Y_{k-1} = y^{\downarrow}_k ,
\]
so \( \x^{\downarrow} = \y^{\downarrow} \). Two vectors with the same decreasing rearrangement contain the same numbers, each the same number of times, so each is a rearrangement of the other.

For \( \prec_w \), the arguments for (a) and (b) are the same with every \( k \le n \) treated like \( k < n \). This proves the proposition.
:::

So \( \prec \) is reflexive and transitive. A relation with these two properties is called a **preorder**. Part (c) is antisymmetry up to rearrangement, and no more: \( (1, 0) \prec (0, 1) \prec (1, 0) \), yet \( (1, 0) \ne (0, 1) \). So \( \prec \) is **not** a partial order on \( \nR^n \). Restricted to **decreasing** vectors, where a rearrangement is the vector itself, (c) is exact antisymmetry, and there \( \prec \) is a partial order. By @exm-majorization-incomparable it is **not total**, not even among non-negative decreasing vectors with the same total. Like the Loewner order of Chapter 13 (@prp-loewner-partial-order), it leaves many pairs uncompared.

## Schur's theorem

The running totals in the \( 3 \times 3 \) example were not a coincidence. Restated in the language of majorization, §06's @cor-ky-fan-diagonal says that for every Hermitian matrix the diagonal is more evenly spread than the spectrum:

::: {#thm-schur-majorization}
[Schur's Majorization Theorem]

Let \( F = \nR \) or \( F = \nC \), and let \( \A \in M_n(F) \) be Hermitian. Then
\[
\d(\A) \prec \vlambda(\A) .
\]
Explicitly, if \( \d(\A)^{\downarrow} = (a^{\downarrow}_1, \dots, a^{\downarrow}_n) \) lists the diagonal entries of \( \A \) decreasingly, then
\[
\begin{aligned}
a^{\downarrow}_1 + \dots + a^{\downarrow}_k &\le \lambda_1(\A) + \dots + \lambda_k(\A) \qquad (1 \le k \le n-1), \\
a^{\downarrow}_1 + \dots + a^{\downarrow}_n &= \lambda_1(\A) + \dots + \lambda_n(\A) .
\end{aligned}
\]
:::

::: {.proof}
Both vectors lie in \( \nR^n \), as noted at the start of the section. Fix \( k \) with \( 1 \le k \le n \). List the positions \( 1, \dots, n \) in an order in which the diagonal entries decrease, breaking ties arbitrarily, and let \( i_1 < \dots < i_k \) be the first \( k \) positions of that list, written in increasing order. Then \( a_{i_1i_1}, \dots, a_{i_ki_k} \) are \( a^{\downarrow}_1, \dots, a^{\downarrow}_k \) in some order, so @cor-ky-fan-diagonal gives
\[
a^{\downarrow}_1 + \dots + a^{\downarrow}_k = \sum_{j=1}^{k} a_{i_ji_j} \le \lambda_1(\A) + \dots + \lambda_k(\A) ,
\]
with equality when \( k = n \). For \( k \le n - 1 \) this is (M1). For \( k = n \) it is (M2), since a sum does not depend on the order of its terms. This proves the theorem.
:::

So Schur's theorem is @cor-ky-fan-diagonal restated. What the restatement adds is a relation between two vectors, and a relation has a converse that can be asked about. Read from the bottom, (M1) says that the \( n - k \) smallest diagonal entries add up to **at least** the \( n - k \) smallest eigenvalues. At the two ends of @exm-majorization-first-examples, a **diagonal** matrix has \( \d(\A) \) a rearrangement of \( \vlambda(\A) \), the most spread a diagonal can be; a **constant** diagonal \( t \) is the flat vector \( t\1 \), where Schur's theorem says only that \( nt = \lambda_1(\A) + \dots + \lambda_n(\A) \).

::: {#exm-schur-three-by-three}
[Coordinate vectors against eigenvectors]

For the matrix
\[
\A = \begin{pmatrix} 3 & 2 & 0 \\ 2 & 4 & 2 \\ 0 & 2 & 5 \end{pmatrix}
\]
from the start of the section, whose running totals were tabulated there, exhibit for \( k = 2 \) the coordinate pair that the proof of @cor-ky-fan-diagonal feeds to @thm-ky-fan and an orthonormal pair that attains the maximum in @thm-ky-fan. Account for the difference between the two sums.
:::

::: {.solution}
We found \( \vlambda(\A) = (7, 4, 1) \), with unit eigenvectors \( \u_1 = \tfrac13(1, 2, 2) \), \( \u_2 = \tfrac13(-2, -1, 2) \) and \( \u_3 = \tfrac13(2, -2, 1) \). They are pairwise orthogonal (for instance \( \inner{(1,2,2)}{(-2,-1,2)} = -2 - 2 + 4 = 0 \)), and each vector in parentheses has length \( 3 \).

For \( k = 2 \) the proof uses the two largest diagonal entries, \( a_{33} = 5 \) and \( a_{22} = 4 \), so the coordinate pair is \( (\e_2, \e_3) \), and \( \inner{\A\e_2}{\e_2} + \inner{\A\e_3}{\e_3} = 9 \). The pair \( (\u_1, \u_2) \) gives \( \inner{\A\u_1}{\u_1} + \inner{\A\u_2}{\u_2} = 7 + 4 = 11 \), since \( \inner{\A\u_i}{\u_i} = \lambda_i\norm{\u_i}^2 = \lambda_i \). The coordinate pair falls short of the eigenvector pair by \( 2 \), and that shortfall is exactly the slack in Schur's theorem at \( k = 2 \). Ky Fan's maximum is attained by eigenvectors, and the diagonal only ever sees coordinate vectors.
:::

::: {.check}
A Hermitian \( 3 \times 3 \) matrix \( \A \) has diagonal entries \( 4, -1, 2 \). Without knowing anything else about \( \A \), what does @thm-schur-majorization say about \( \lambda_1(\A) \), about \( \lambda_1(\A) + \lambda_2(\A) \), and about \( \lambda_3(\A) \)?
:::

::: {.solution}
Sorted, \( \d(\A)^{\downarrow} = (4, 2, -1) \), with running totals \( 4, 6, 5 \). So \( \lambda_1(\A) \ge 4 \), \( \lambda_1(\A) + \lambda_2(\A) \ge 6 \), and \( \lambda_1(\A) + \lambda_2(\A) + \lambda_3(\A) = 5 \). Subtracting the middle inequality from the last equality gives \( \lambda_3(\A) \le 5 - 6 = -1 \). In particular \( \A \) is indefinite, since \( \lambda_1(\A) > 0 > \lambda_3(\A) \), and that was visible without computing any eigenvalue.
:::

## Horn's converse

Schur's theorem gives a **necessary** condition on a diagonal. Is it also sufficient? Given \( \d \prec \vlambda \), is there a Hermitian matrix with eigenvalues \( \lambda_1, \dots, \lambda_n \) and diagonal entries \( d_1, \dots, d_n \), in the given order? For \( n = 2 \) a rotation answers the question. Turning the eigenbasis of \( \diag(\lambda_1, \lambda_2) \) moves its first diagonal entry through every value between \( \lambda_2 \) and \( \lambda_1 \), and the trace fixes the second entry.

::: {#lem-horn-two-by-two}
[The Two-by-Two Rotation]

Let \( \lambda_1 \ge \lambda_2 \) and \( t \) be real numbers with \( \lambda_2 \le t \le \lambda_1 \). Put \( b = \sqrt{(\lambda_1 - t)(t - \lambda_2)} \). Then there is an orthogonal \( \R \in \Orth(2) \) with
\[
\R\diag(\lambda_1, \lambda_2)\R\tp = \begin{pmatrix} t & b \\ b & \lambda_1 + \lambda_2 - t \end{pmatrix} .
\]
:::

::: {.idea}
If the first row of \( \R \) is \( (c, -s) \) with \( c^2 + s^2 = 1 \), the \( (1,1) \) entry of \( \R\diag(\lambda_1, \lambda_2)\R\tp \) is \( c^2\lambda_1 + s^2\lambda_2 \), an average of \( \lambda_1 \) and \( \lambda_2 \) with weights \( c^2 \) and \( s^2 \). Every \( t \) between them is such an average, and solving for the weights gives \( c \) and \( s \).
:::

::: {.proof}
If \( \lambda_1 = \lambda_2 \), then \( t = \lambda_1 = \lambda_2 \) and \( b = 0 \), and \( \R = \I \) works. Otherwise \( \lambda_1 - \lambda_2 > 0 \), and
\[
c = \sqrt{\frac{t - \lambda_2}{\lambda_1 - \lambda_2}} , \qquad s = \sqrt{\frac{\lambda_1 - t}{\lambda_1 - \lambda_2}}
\]
are real numbers, because both radicands are \( \ge 0 \) by the hypothesis on \( t \). They satisfy \( c^2 + s^2 = 1 \). Let \( \R = \begin{psmallmatrix} c & -s \\ s & c \end{psmallmatrix} \). Then \( \R\tp\R = (c^2 + s^2)\I = \I \), so \( \R \in \Orth(2) \). Multiplying out,
\[
\R\diag(\lambda_1, \lambda_2)\R\tp
= \begin{pmatrix} c^2\lambda_1 + s^2\lambda_2 & cs(\lambda_1 - \lambda_2) \\ cs(\lambda_1 - \lambda_2) & s^2\lambda_1 + c^2\lambda_2 \end{pmatrix} .
\]
Since \( s^2 = 1 - c^2 \), the \( (1,1) \) entry is \( \lambda_2 + c^2(\lambda_1 - \lambda_2) = \lambda_2 + (t - \lambda_2) = t \). The two diagonal entries add up to \( (c^2 + s^2)(\lambda_1 + \lambda_2) = \lambda_1 + \lambda_2 \), so the \( (2,2) \) entry is \( \lambda_1 + \lambda_2 - t \). Finally \( cs(\lambda_1 - \lambda_2) = \sqrt{(t - \lambda_2)(\lambda_1 - t)} = b \). This proves the lemma.
:::

This is the converse for \( n = 2 \): if \( \lambda_1 \ge \lambda_2 \) and \( (d_1, d_2) \prec (\lambda_1, \lambda_2) \), then \( d_1, d_2 \le d^{\downarrow}_1 \le \lambda_1 \) by (M1), so by (M2) \( d_1 = \lambda_1 + \lambda_2 - d_2 \ge \lambda_2 \), so \( t = d_1 \) is allowed. For larger \( n \), the lemma is used once, on a well-chosen pair of eigenvalues, to put \( d_1 \) in the corner, and induction does the rest.

::: {#thm-horn}
[Horn's Theorem]

Let \( n \ge 1 \), and let \( \d = (d_1, \dots, d_n) \) and \( \vlambda = (\lambda_1, \dots, \lambda_n) \) be vectors in \( \nR^n \) with \( \d \prec \vlambda \). Then there is an orthogonal \( \Q \in \Orth(n) \) such that the matrix
\[
\A = \Q\diag(\lambda_1, \dots, \lambda_n)\Q\tp
\]
has diagonal entries \( d_1, d_2, \dots, d_n \), **in this order**. So \( \A \) is a real symmetric matrix with \( \d(\A) = \d \) and \( \vlambda(\A) = \vlambda^{\downarrow} \).
:::

::: {.idea}
Induction on \( n \), one diagonal entry at a time.

① Permutation matrices are orthogonal and shuffle diagonal entries, so it is enough to treat \( \d \) and \( \vlambda \) both decreasing.
② The top and bottom clauses of majorization put \( d_1 \) between \( \lambda_n \) and \( \lambda_1 \), hence between two **consecutive** eigenvalues, \( \lambda_k \ge d_1 \ge \lambda_{k+1} \). The lemma rotates that pair so that \( d_1 \) sits in the corner, with \( \eta = \lambda_k + \lambda_{k+1} - d_1 \) next to it.
③ The Claim: what is left over, the diagonal \( d_2, \dots, d_n \) and the spectrum with \( \lambda_k, \lambda_{k+1} \) replaced by \( \eta \), satisfies the hypothesis again, in size \( n - 1 \).
④ Induction rotates the lower \( (n-1) \times (n-1) \) block into place without touching the corner.

Step ③ is where the choice of \( k \) matters.
:::

::: {.proof}
For every \( \Q \in \Orth(n) \), the matrix \( \A = \Q\diag(\lambda_1, \dots, \lambda_n)\Q\tp \) is real and symmetric, and by @cor-spectral-real-matrix its eigenvalues, with multiplicity, are \( \lambda_1, \dots, \lambda_n \); listed decreasingly they form \( \vlambda^{\downarrow} \). So only the diagonal needs work. We use two facts repeatedly. A product of orthogonal matrices is orthogonal, since \( (\X\Y)\tp\X\Y = \Y\tp\X\tp\X\Y = \I \). And for a permutation \( \pi \in S_n \) and any \( \M \in M_n(\nR) \), @def-permutation-matrix gives
\[
(\P_\pi\tp\M\P_\pi)_{ij} = \e_{\pi(i)}\tp\M\e_{\pi(j)} = m_{\pi(i)\pi(j)} , \tag{$\dagger$}
\]
where \( \P_\pi \) is orthogonal by @lem-permutation-matrices (b).

**Step 1: reduction to decreasing vectors.** Suppose the theorem holds whenever \( \d \) and \( \vlambda \) are both decreasing, and let \( \d \prec \vlambda \) be arbitrary. Majorization sees only rearrangements (as noted after @def-majorization), so \( \d^{\downarrow} \prec \vlambda^{\downarrow} \), and there is \( \Q_0 \in \Orth(n) \) such that \( \B = \Q_0\diag(\vlambda^{\downarrow})\Q_0\tp \) has diagonal \( \d^{\downarrow} \). Here \( \diag(\vlambda^{\downarrow}) \) is the diagonal matrix with diagonal \( \lambda^{\downarrow}_1, \dots, \lambda^{\downarrow}_n \). Since \( \vlambda^{\downarrow} \) is a rearrangement of \( \vlambda \), and \( \d^{\downarrow} \) of \( \d \), there are permutations \( \sigma, \tau \in S_n \) with \( \lambda_{\sigma(i)} = \lambda^{\downarrow}_i \) and \( d^{\downarrow}_{\tau(j)} = d_j \) for all \( i, j \). By \( (\dagger) \), \( \P_\sigma\tp\diag(\lambda_1, \dots, \lambda_n)\P_\sigma = \diag(\vlambda^{\downarrow}) \), and the \( (j,j) \) entry of \( \P_\tau\tp\B\P_\tau \) is \( b_{\tau(j)\tau(j)} = d^{\downarrow}_{\tau(j)} = d_j \). So \( \Q = \P_\tau\tp\Q_0\P_\sigma\tp \) is orthogonal and
\[
\begin{aligned}
\Q\diag(\lambda_1, \dots, \lambda_n)\Q\tp
&= \P_\tau\tp\Q_0\diag(\vlambda^{\downarrow})\Q_0\tp\P_\tau \\
&= \P_\tau\tp\B\P_\tau
\end{aligned}
\]
has diagonal \( \d \). It therefore suffices to prove the theorem for decreasing \( \d \) and \( \vlambda \), and we do so by induction on \( n \).

**Step 2: the corner.** For \( n = 1 \), \( \d \prec \vlambda \) means \( d_1 = \lambda_1 \) (@exm-majorization-first-examples (d)), and \( \Q = (1) \) works. Let \( n \ge 2 \), assume the theorem for \( n - 1 \) (for vectors in any order, by Step 1), and let \( \d \) and \( \vlambda \) be decreasing with \( \d \prec \vlambda \). By (M1) at \( k = 1 \), \( d_1 \le \lambda_1 \). Subtracting (M1) at \( k = n - 1 \) from (M2) gives \( d_n \ge \lambda_n \), so \( d_1 \ge d_n \ge \lambda_n \). Let \( k \) be the smallest index in \( \{1, \dots, n-1\} \) with \( \lambda_{k+1} \le d_1 \); one exists, since \( \lambda_n \le d_1 \). Then \( \lambda_k \ge d_1 \): for \( k = 1 \) this is \( d_1 \le \lambda_1 \), and for \( k \ge 2 \) the minimality of \( k \) gives \( \lambda_k > d_1 \). So
\[
\lambda_k \ge d_1 \ge \lambda_{k+1} .
\]
By @lem-horn-two-by-two with \( t = d_1 \), there are \( \R \in \Orth(2) \) and a real \( b \) with
\[
\R\diag(\lambda_k, \lambda_{k+1})\R\tp = \begin{pmatrix} d_1 & b \\ b & \eta \end{pmatrix} ,
\qquad \eta = \lambda_k + \lambda_{k+1} - d_1 .
\]
Moreover \( \lambda_{k+1} \le \eta \le \lambda_k \), since \( \eta - \lambda_{k+1} = \lambda_k - d_1 \ge 0 \) and \( \lambda_k - \eta = d_1 - \lambda_{k+1} \ge 0 \).

**Step 3: the leftover data.** Put
\[
\begin{aligned}
\d' &= (d_2, \dots, d_n) , \\
\vlambda' &= (\eta, \lambda_1, \dots, \lambda_{k-1}, \lambda_{k+2}, \dots, \lambda_n) ,
\end{aligned}
\]
two vectors in \( \nR^{n-1} \). So \( \vlambda' \) is \( \vlambda \) with the pair \( \lambda_k, \lambda_{k+1} \) replaced by the single number \( \eta \), written first.

::: {.claim}
\( \d' \prec \vlambda' \).

::: {.proof}
By Step 2, \( \lambda_{k-1} \ge \lambda_k \ge \eta \ge \lambda_{k+1} \ge \lambda_{k+2} \), for those of these indices that exist. So
\[
(\mu_1, \dots, \mu_{n-1}) = (\lambda_1, \dots, \lambda_{k-1}, \eta, \lambda_{k+2}, \dots, \lambda_n)
\]
is \( (\vlambda')^{\downarrow} \), and \( \d' \) is already decreasing. For (M2), \( \sum_i d'_i = \sum_i d_i - d_1 = \sum_i \lambda_i - d_1 = \sum_i \lambda'_i \), by (M2) for \( \d \prec \vlambda \) and the definition of \( \eta \). For (M1), fix \( m \) with \( 1 \le m \le n - 2 \); when \( n = 2 \) there is nothing to check.

*Case \( m \le k - 1 \).* Then \( \mu_i = \lambda_i \) for \( i \le m \). For each such \( i \), \( d_{i+1} \le d_1 \le \lambda_k \le \lambda_i \), because \( \d \) and \( \vlambda \) are decreasing and \( i < k \). Summing over \( i \le m \) gives \( d_2 + \dots + d_{m+1} \le \mu_1 + \dots + \mu_m \).

*Case \( m \ge k \).* The first \( m \) entries of \( (\vlambda')^{\downarrow} \) are \( \lambda_1, \dots, \lambda_{k-1} \), then \( \eta \), then \( \lambda_{k+2}, \dots, \lambda_{m+1} \). So
\[
\begin{aligned}
\mu_1 + \dots + \mu_m &= (\lambda_1 + \dots + \lambda_{m+1}) - \lambda_k - \lambda_{k+1} + \eta \\
&= (\lambda_1 + \dots + \lambda_{m+1}) - d_1 .
\end{aligned}
\]
Since \( m + 1 \le n - 1 \), (M1) for \( \d \prec \vlambda \) applies at \( m + 1 \) and gives
\[
\begin{aligned}
d_2 + \dots + d_{m+1} &= (d_1 + \dots + d_{m+1}) - d_1 \\
&\le (\lambda_1 + \dots + \lambda_{m+1}) - d_1 = \mu_1 + \dots + \mu_m .
\end{aligned}
\]
In both cases (M1) holds, which proves the claim.
:::
:::

**Step 4: assembly.** Let \( \sigma \in S_n \) list the indices \( k, k+1 \) first and the others after them in increasing order: \( \sigma(1) = k \), \( \sigma(2) = k + 1 \), and \( \sigma(3), \dots, \sigma(n) \) are \( 1, \dots, k-1, k+2, \dots, n \). By \( (\dagger) \),
\[
\P_\sigma\tp\diag(\lambda_1, \dots, \lambda_n)\P_\sigma = \begin{pmatrix} \diag(\lambda_k, \lambda_{k+1}) & \0 \\ \0 & \D_1 \end{pmatrix} ,
\]
where \( \D_1 = \diag(\lambda_1, \dots, \lambda_{k-1}, \lambda_{k+2}, \dots, \lambda_n) \in M_{n-2}(\nR) \); when \( n = 2 \) the blocks involving \( \D_1 \) are absent. Let \( \R_1 = \begin{psmallmatrix} \R & \0 \\ \0 & \I_{n-2} \end{psmallmatrix} \). Multiplying blocks and using Step 2,
\[
\M = \R_1\P_\sigma\tp\diag(\lambda_1, \dots, \lambda_n)\P_\sigma\R_1\tp
= \begin{pmatrix} d_1 & b & \0 \\ b & \eta & \0 \\ \0 & \0 & \D_1 \end{pmatrix}
= \begin{pmatrix} d_1 & b\,\e_1\tp \\ b\,\e_1 & \E \end{pmatrix} ,
\]
where \( \e_1 \) is the first standard basis vector of \( \nR^{n-1} \) and \( \E = \diag(\eta, \lambda_1, \dots, \lambda_{k-1}, \lambda_{k+2}, \dots, \lambda_n) \) is the diagonal matrix of \( \vlambda' \). By the Claim and the inductive hypothesis, there is \( \W \in \Orth(n-1) \) such that \( \W\E\W\tp \) has diagonal entries \( d_2, \dots, d_n \). Let \( \W_1 = \begin{psmallmatrix} 1 & \0\tp \\ \0 & \W \end{psmallmatrix} \). Then
\[
\W_1\M\W_1\tp = \begin{pmatrix} d_1 & b\,(\W\e_1)\tp \\ b\,\W\e_1 & \W\E\W\tp \end{pmatrix} ,
\]
whose diagonal entries are \( d_1, d_2, \dots, d_n \). The block matrices \( \R_1 \) and \( \W_1 \) are orthogonal, since \( \R_1\tp\R_1 \) and \( \W_1\tp\W_1 \) are block diagonal with blocks \( \R\tp\R = \I \), \( \I \), and \( 1 \), \( \W\tp\W = \I \). So \( \Q = \W_1\R_1\P_\sigma\tp \) is orthogonal, and \( \Q\diag(\lambda_1, \dots, \lambda_n)\Q\tp = \W_1\M\W_1\tp \). This completes the induction and proves the theorem.
:::

Over \( \nC \) nothing more is needed, because an orthogonal matrix is unitary and a real symmetric matrix is Hermitian. Together with Schur's theorem, this settles the question the section began with.

::: {#thm-schur-horn}
[Schur–Horn Theorem]

Let \( F = \nR \) or \( F = \nC \), and let \( \d, \vlambda \in \nR^n \). There is a Hermitian \( \A \in M_n(F) \) with \( \vlambda(\A) = \vlambda^{\downarrow} \) and \( \d(\A) = \d \) if and only if \( \d \prec \vlambda \). In words: the diagonals of the Hermitian matrices with spectrum \( \vlambda \) are **exactly** the vectors majorized by \( \vlambda \), and real symmetric matrices already give all of them.
:::

::: {.proof}
\( (\Rightarrow) \) By @thm-schur-majorization, \( \d = \d(\A) \prec \vlambda(\A) = \vlambda^{\downarrow} \). Since majorization sees only rearrangements, \( \d \prec \vlambda \).

\( (\Leftarrow) \) @thm-horn gives a real symmetric \( \A \in M_n(\nR) \subseteq M_n(F) \) with \( \d(\A) = \d \) and \( \vlambda(\A) = \vlambda^{\downarrow} \), and a real symmetric matrix is Hermitian.
:::

::: {#exm-horn-construction}
[Building a matrix from its diagonal and spectrum]

Find a real symmetric matrix with eigenvalues \( 6, 1, 0 \) and diagonal \( (4, 2, 1) \).
:::

::: {.solution}
Both vectors are decreasing, and \( (4, 2, 1) \prec (6, 1, 0) \): the running totals are \( 4, 6 \) against \( 6, 7 \), and both totals are \( 7 \). Follow the proof of @thm-horn.

*The corner.* \( d_1 = 4 \) lies between \( \lambda_1 = 6 \) and \( \lambda_2 = 1 \), so \( k = 1 \), \( \eta = 6 + 1 - 4 = 3 \), and @lem-horn-two-by-two gives \( b = \sqrt{(6 - 4)(4 - 1)} = \sqrt6 \). After the first rotation the matrix is
\[
\M = \begin{pmatrix} 4 & \sqrt6 & 0 \\ \sqrt6 & 3 & 0 \\ 0 & 0 & 0 \end{pmatrix} .
\]

*The leftover.* \( \d' = (2, 1) \) and \( \vlambda' = (3, 0) \), with \( 2 \le 3 \) and \( 2 + 1 = 3 + 0 \), so \( \d' \prec \vlambda' \), as the Claim promises. The lemma with \( t = 2 \) gives \( c = \sqrt{2/3} \), \( s = \sqrt{1/3} \), and
\[
\W\diag(3, 0)\W\tp = \begin{pmatrix} 2 & \sqrt2 \\ \sqrt2 & 1 \end{pmatrix} , \qquad \W\e_1 = (c, s) .
\]

*Assembly.* The first row becomes \( \bigl(4,\ \sqrt6\,c,\ \sqrt6\,s\bigr) = (4, 2, \sqrt2) \), so
\[
\A = \begin{pmatrix} 4 & 2 & \sqrt2 \\ 2 & 2 & \sqrt2 \\ \sqrt2 & \sqrt2 & 1 \end{pmatrix} .
\]
Check directly: \( \A(3, 2, \sqrt2) = (18, 12, 6\sqrt2) = 6\,(3, 2, \sqrt2) \), \( \A(-\sqrt2, \sqrt2, 1) = (-\sqrt2, \sqrt2, 1) \), and \( \A(0, -1, \sqrt2) = (0, 0, 0) \). Three eigenvectors with distinct eigenvalues \( 6, 1, 0 \) give the whole spectrum, and the diagonal is \( (4, 2, 1) \).
:::

## Hadamard's inequality from the diagonal

Chapter 13 §06 proved @thm-hadamard-inequality: for a positive semidefinite \( \A \), \( \det \A \le a_{11}a_{22}\cdots a_{nn} \), with equality if and only if \( \A \) is diagonal or some \( a_{ii} = 0 \). That proof inducts on the size through Fischer's inequality (@cor-fischer-inequality). A much shorter route scales \( \A \) so that its diagonal is flat, and then compares the product of the eigenvalues with their sum. That comparison is the inequality between the arithmetic and geometric means, which the book has not yet proved; it is pure algebra, and it comes first.

::: {#lem-am-gm}
[The Arithmetic–Geometric Mean Inequality]

Let \( n \ge 1 \) and let \( t_1, \dots, t_n \) be **non-negative** real numbers. Then
\[
t_1t_2\cdots t_n \le \Bigl(\frac{t_1 + t_2 + \dots + t_n}{n}\Bigr)^{n} ,
\]
with equality if and only if \( t_1 = t_2 = \dots = t_n \).
:::

::: {.idea}
Scale so that the mean is \( 1 \). If the numbers are not all \( 1 \), one of them lies above \( 1 \) and another below. Merge that pair into the single number \( t_j + t_k - 1 \). This leaves \( n - 1 \) non-negative numbers with mean \( 1 \), so induction applies to them. The merge can only increase the product, because
\[
(t_j + t_k - 1) - t_jt_k = (t_j - 1)(1 - t_k) ,
\]
and both factors are positive. So the original product is at most, and when it is non-zero strictly less than, a product that induction bounds by \( 1 \).
:::

::: {.proof}
**Step 1: mean \( 1 \).** We prove by induction on \( n \ge 1 \): if \( t_1, \dots, t_n \ge 0 \) and \( t_1 + \dots + t_n = n \), then \( t_1\cdots t_n \le 1 \), with equality only when every \( t_i = 1 \). For \( n = 1 \) the hypothesis says \( t_1 = 1 \), and the product is \( 1 \).

Let \( n \ge 2 \) and assume the claim for \( n - 1 \) numbers. If every \( t_i = 1 \), the product is \( 1 \). Otherwise some \( t_j > 1 \): if every \( t_i \le 1 \) with at least one strictly smaller, the sum would be less than \( n \). Similarly some \( t_k < 1 \), since if every \( t_i \ge 1 \) with at least one strictly larger, the sum would exceed \( n \). Then \( j \ne k \). Neither the sum nor the product depends on the order of the numbers, so we may relabel so that \( j = n - 1 \) and \( k = n \). Put
\[
s = t_{n-1} + t_n - 1 .
\]
Then \( s > 0 \), since \( t_{n-1} > 1 \) and \( t_n \ge 0 \). The \( n - 1 \) numbers \( t_1, \dots, t_{n-2}, s \) are non-negative and add up to \( n - 1 \). So by the inductive hypothesis \( p\,s \le 1 \), where \( p = t_1\cdots t_{n-2} \ge 0 \) (with \( p = 1 \) when \( n = 2 \)). Moreover
\[
s - t_{n-1}t_n = (t_{n-1} - 1)(1 - t_n) > 0 .
\]
If \( p = 0 \), then \( t_1\cdots t_n = 0 < 1 \). If \( p > 0 \), then \( t_1\cdots t_n = p\,t_{n-1}t_n < p\,s \le 1 \). In either case the product is strictly less than \( 1 \) when the \( t_i \) are not all \( 1 \). This completes the induction.

**Step 2: the general case.** Let \( m = \tfrac1n(t_1 + \dots + t_n) \ge 0 \). If \( m = 0 \), then every \( t_i = 0 \), since non-negative numbers with sum \( 0 \) are all \( 0 \). Both sides are then \( 0 \), and the \( t_i \) are all equal. If \( m > 0 \), the numbers \( t_i/m \) are non-negative with sum \( n \). By Step 1,
\[
\frac{t_1}{m}\cdots\frac{t_n}{m} \le 1 , \qquad\text{that is,}\qquad t_1\cdots t_n \le m^n ,
\]
with equality if and only if every \( t_i/m = 1 \), that is, every \( t_i = m \). Numbers that are all equal to some \( c \) have mean \( m = c \), so "every \( t_i = m \)" is the same as "all the \( t_i \) are equal". This proves the lemma.
:::

In the language of this section, the lemma says that among non-negative vectors with a fixed total, the **flat** vector, which is the bottom of the majorization order (@exm-majorization-first-examples (b)), has the largest product.

::: {#cor-hadamard-from-majorization}
[Hadamard's Inequality, Second Proof]

Let \( F = \nR \) or \( F = \nC \), and let \( \A \in M_n(F) \) with \( \A \succeq 0 \). Then
\[
\det \A \le a_{11}a_{22}\cdots a_{nn} ,
\]
with equality if and only if \( \A \) is diagonal or some \( a_{ii} = 0 \).
:::

This is @thm-hadamard-inequality (a) again, with the same hypothesis and the same equality condition. What is new is the proof.

::: {.idea}
Suppose first that every diagonal entry equals \( 1 \). Then \( \tr\A = n \), so the eigenvalues, which are non-negative, add up to \( n \), and @lem-am-gm gives \( \det \A = \prod_i \lambda_i(\A) \le 1 = \prod_i a_{ii} \). A general diagonal is made flat by a diagonal congruence \( \A \mapsto \S\A\S \) with \( \S = \diag(a_{11}^{-1/2}, \dots, a_{nn}^{-1/2}) \). This congruence preserves positivity and divides both sides of the inequality by the same number \( a_{11}\cdots a_{nn} \). Zero diagonal entries, where \( \S \) does not exist, are handled first and separately.
:::

::: {.proof}
Each \( a_{ii} = \inner{\A\e_i}{\e_i} \ge 0 \) by @def-positive-semidefinite, and each \( \lambda_i(\A) \ge 0 \) by @thm-psd-characterizations (b).

*Case 1: some \( a_{ii} = 0 \).* The right-hand side is \( 0 \). Suppose \( \det \A \ne 0 \). By @thm-trace-det-eigenvalues, \( \det \A = \prod_j \lambda_j(\A) \), so every \( \lambda_j(\A) \) is non-zero, hence positive. By @thm-pd-characterizations (b), \( \A \succ 0 \), so \( a_{ii} = \inner{\A\e_i}{\e_i} > 0 \), a contradiction. Hence \( \det \A = 0 \), and the inequality holds with equality, as the statement says it should when some \( a_{ii} = 0 \).

*Case 2: every \( a_{ii} > 0 \).* Let \( \S = \diag(a_{11}^{-1/2}, \dots, a_{nn}^{-1/2}) \), a real diagonal matrix with non-zero diagonal, so \( \S^{*} = \S \) and \( \S \) is invertible. Put \( \B = \S^{*}\A\S = \S\A\S \). By @prp-congruence-positivity (a), \( \B \succeq 0 \). Its entries are \( b_{ij} = a_{ij}/\sqrt{a_{ii}a_{jj}} \), so \( b_{ii} = 1 \) for every \( i \), and \( \tr\B = n \). By @thm-trace-det-eigenvalues,
\[
\lambda_1(\B) + \dots + \lambda_n(\B) = n .
\]
The \( \lambda_i(\B) \) are non-negative by @thm-psd-characterizations (b). So @lem-am-gm and @thm-trace-det-eigenvalues give
\[
\det \B = \prod_{i=1}^{n}\lambda_i(\B) \le \Bigl(\frac{n}{n}\Bigr)^{n} = 1 ,
\]
with equality if and only if all \( \lambda_i(\B) \) are equal, hence all equal to \( 1 \). By @thm-det-multiplicative, and since \( \det \S = (a_{11}\cdots a_{nn})^{-1/2} \),
\[
\det \B = (\det \S)^2\det \A = \frac{\det \A}{a_{11}a_{22}\cdots a_{nn}} .
\]
Multiplying \( \det \B \le 1 \) by the positive number \( a_{11}\cdots a_{nn} \) gives \( \det \A \le a_{11}\cdots a_{nn} \).

For equality in Case 2: equality holds exactly when every \( \lambda_i(\B) = 1 \). If so, the spectral theorem (@cor-spectral-complex-matrix, or @cor-spectral-real-matrix over \( \nR \)) gives \( \B = \U\I\U^{*} = \I \) for some unitary (or orthogonal) \( \U \). Then \( \A = \S^{-1}\B\S^{-1} = \S^{-2} = \diag(a_{11}, \dots, a_{nn}) \) is diagonal. Conversely, if \( \A \) is diagonal, then \( \B = \S\A\S = \I \), and every \( \lambda_i(\B) = 1 \). So in Case 2, equality holds if and only if \( \A \) is diagonal. Together with Case 1, this is the stated equality condition. This proves the corollary.
:::

For the matrix of @exm-schur-three-by-three, which is positive definite since its eigenvalues are \( 7, 4, 1 \), the inequality reads \( \det \A = 7 \cdot 4 \cdot 1 = 28 \le 60 = 3 \cdot 4 \cdot 5 \).

The two proofs show different things. The first proves more along the way: Fischer's inequality for blocks of any sizes. The second shows that once the diagonal is scaled flat, the trace and the arithmetic–geometric mean inequality suffice. Of \( \d(\B) \prec \vlambda(\B) \) it uses only clause (M2), which for a matrix is just the trace.

::: {.remark}
A proof by majorization in earnest would use all of \( \d(\A) \prec \vlambda(\A) \), without scaling, together with the fact that for vectors with **non-negative** entries, \( \x \prec \y \) implies \( x_1\cdots x_n \ge y_1\cdots y_n \) (the product is **Schur-concave**). That fact is true but **not proved in this book yet**; Chapter 21 proves it, for the whole class of functions that reverse majorization.
:::

Majorization is the language this chapter's eigenvalue inequalities were already using, and the Schur–Horn theorem shows that it fits the diagonal problem exactly. The same language compresses the inequality of Section 7 for arbitrary index sets, @thm-lidskii-inequality, into one line. The \( k \) largest entries of the vector \( \vlambda(\A) - \vlambda(\B) \) add up to the largest value of \( \sum_j \bigl(\lambda_{i_j}(\A) - \lambda_{i_j}(\B)\bigr) \) over index sets of size \( k \), and the totals are \( \tr \A - \tr \B = \tr(\A - \B) \). So a bound of every such sum by \( \sum_{j \le k}\lambda_j(\A - \B) \) says exactly that
\[
\vlambda(\A) - \vlambda(\B) \prec \vlambda(\A - \B) .
\]
The diagonal of a Hermitian matrix and the eigenvalues of a difference are both controlled by one ordering of vectors in \( \nR^n \).

## Exercises

### A. Check your understanding

:::: {#exr-majorization-and-schur-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the definitions of \( \x \prec \y \) and \( \x \prec_w \y \) for \( \x, \y \in \nR^n \).
2. Decide whether \( (2, 1, 1) \prec (2, 2, 0) \), and whether \( (2, 2, 0) \prec (2, 1, 1) \).
3. True or false: if \( \x \prec \y \), then \( x_1 \le y_1 \). Justify your answer.
4. State @thm-schur-majorization. Which result of §06 is it a restatement of?
5. State @thm-schur-horn. Which half is proved by induction on \( n \), and which lemma does each step of that induction use?
:::
::::

::: {.solution}
(a) \( \x \prec \y \) means that \( \sum_{i \le k} x^{\downarrow}_i \le \sum_{i \le k} y^{\downarrow}_i \) for every \( k = 1, \dots, n-1 \), and \( \sum_{i=1}^n x_i = \sum_{i=1}^n y_i \) (@def-majorization). \( \x \prec_w \y \) means that the same inequality holds for every \( k = 1, \dots, n \), with no condition on the totals.

(b) Both vectors are decreasing with total \( 4 \). Their running totals at \( k = 1, 2 \) are \( 2, 3 \) and \( 2, 4 \). Since \( 2 \le 2 \) and \( 3 \le 4 \), \( (2, 1, 1) \prec (2, 2, 0) \). The reverse fails at \( k = 2 \), since \( 4 > 3 \).

(c) False. The definition compares **sorted** vectors, so the unsorted first entries can go either way. Take \( \x = (1, 0) \) and \( \y = (0, 1) \). Both have decreasing rearrangement \( (1, 0) \), so (M1) at \( k = 1 \) reads \( 1 \le 1 \), and both totals are \( 1 \); hence \( \x \prec \y \). But \( x_1 = 1 > 0 = y_1 \). What is true is \( x^{\downarrow}_1 \le y^{\downarrow}_1 \), which is (M1) at \( k = 1 \).

(d) For a Hermitian \( \A \in M_n(F) \), \( F = \nR \) or \( \nC \), \( \d(\A) \prec \vlambda(\A) \). It restates @cor-ky-fan-diagonal: applied to the positions of the \( k \) largest diagonal entries, the corollary gives (M1), and its equality at \( k = n \) gives (M2).

(e) For \( \d, \vlambda \in \nR^n \), there is a Hermitian matrix over \( \nR \) or \( \nC \) with diagonal \( \d \), in the given order, and eigenvalues \( \lambda_1, \dots, \lambda_n \) if and only if \( \d \prec \vlambda \). The half "\( \d \prec \vlambda \) implies such a matrix exists" is Horn's theorem, @thm-horn, proved by induction on \( n \). Each step uses @lem-horn-two-by-two, applied to a pair of consecutive eigenvalues \( \lambda_k \ge d_1 \ge \lambda_{k+1} \), to put \( d_1 \) in the corner. The other half is Schur's theorem.
:::

### B. Practice

:::: {#exr-majorization-and-schur-b1}
[B1: Determine which pairs are comparable]

For each pair, determine whether \( \x \prec \y \) and whether \( \x \prec_w \y \). Where a relation fails, name the exact clause and the value of \( k \) at which it fails. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \x = (2, 2, 1, 1) \), \( \y = (3, 2, 1, 0) \).
2. \( \x = (0, 3, 1) \), \( \y = (4, 0, 0) \).
3. \( \x = (1, 1, 0) \), \( \y = (2, 1, 0) \).
4. \( \x = (-1, 2, 2) \), \( \y = (3, 0, 0) \).
5. \( \x = (3, 1, 1, 1) \), \( \y = (2, 2, 2, 0) \); decide also whether \( \y \prec \x \).
:::
::::

::: {.solution}
In each case, sort first, then compare running totals.

(a) Both are decreasing with total \( 6 \). Running totals: \( 2, 4, 5, 6 \) and \( 3, 5, 6, 6 \). Every entry of the first list is at most the matching entry of the second, so \( \x \prec \y \) and hence \( \x \prec_w \y \).

(b) \( \x^{\downarrow} = (3, 1, 0) \) with running totals \( 3, 4, 4 \), and \( \y \) has running totals \( 4, 4, 4 \). The totals agree and \( 3 \le 4 \), \( 4 \le 4 \), so \( \x \prec \y \) and \( \x \prec_w \y \). This is @exm-majorization-first-examples (c), applied after sorting.

(c) Running totals \( 1, 2, 2 \) and \( 2, 3, 3 \). Every inequality holds, including at \( k = 3 \), so \( \x \prec_w \y \). But the totals are \( 2 \ne 3 \), so **(M2) fails** and \( \x \not\prec \y \).

(d) \( \x^{\downarrow} = (2, 2, -1) \) with running totals \( 2, 4, 3 \), and \( \y \) has running totals \( 3, 3, 3 \). The totals agree, but at \( k = 2 \), \( 4 > 3 \), so **(M1) fails at \( k = 2 \)**. Neither \( \x \prec \y \) nor \( \x \prec_w \y \) holds.

(e) Both are decreasing with total \( 6 \). Running totals: \( 3, 4, 5, 6 \) and \( 2, 4, 6, 6 \). At \( k = 1 \), \( 3 > 2 \), so **(M1) fails at \( k = 1 \)** and \( \x \not\prec \y \), and also \( \x \not\prec_w \y \). For \( \y \prec \x \), the inequalities \( 2 \le 3 \) and \( 4 \le 4 \) hold, but \( 6 > 5 \) at \( k = 3 \), so **(M1) fails at \( k = 3 \)**. The pair is incomparable, like @exm-majorization-incomparable.
:::

:::: {#exr-majorization-and-schur-b2}
[B2: Schur's theorem for one matrix]

Let
\[
\A = \begin{pmatrix} 3 & 2 & 2 \\ 2 & 4 & 0 \\ 2 & 0 & 7 \end{pmatrix} .
\]

::: {.enumerate options="label=(\alph*)"}
1. Verify that \( (2, 1, 4) \), \( (-1, -2, 1) \) and \( (-3, 2, 1) \) are eigenvectors of \( \A \), and find \( \vlambda(\A) \).
2. Write down \( \d(\A) \) and verify every clause of \( \d(\A) \prec \vlambda(\A) \).
3. Hence verify Hadamard's inequality (@thm-hadamard-inequality) for \( \A \).
:::
::::

::: {.solution}
(a) Multiply out:
\[
\begin{aligned}
\A(2, 1, 4) &= (6 + 2 + 8,\ 4 + 4,\ 4 + 28) = (16, 8, 32) = 8\,(2, 1, 4), \\
\A(-1, -2, 1) &= (-3 - 4 + 2,\ -2 - 8,\ -2 + 7) = (-5, -10, 5) = 5\,(-1, -2, 1), \\
\A(-3, 2, 1) &= (-9 + 4 + 2,\ -6 + 8,\ -6 + 7) = (-3, 2, 1) = 1\,(-3, 2, 1).
\end{aligned}
\]
Three distinct eigenvalues of a \( 3 \times 3 \) matrix account for the whole spectrum, so \( \vlambda(\A) = (8, 5, 1) \).

(b) \( \d(\A) = (3, 4, 7) \), and \( \d(\A)^{\downarrow} = (7, 4, 3) \). (M1): at \( k = 1 \), \( 7 \le 8 \); at \( k = 2 \), \( 7 + 4 = 11 \le 13 = 8 + 5 \). (M2): \( 3 + 4 + 7 = 14 = 8 + 5 + 1 \). Hence \( \d(\A) \prec \vlambda(\A) \), as @thm-schur-majorization requires.

(c) All eigenvalues are positive, so \( \A \succ 0 \) by @thm-pd-characterizations (b), and @cor-hadamard-from-majorization applies. By @thm-trace-det-eigenvalues, \( \det \A = 8 \cdot 5 \cdot 1 = 40 \), while \( a_{11}a_{22}a_{33} = 3 \cdot 4 \cdot 7 = 84 \). Hence \( 40 \le 84 \). The inequality is strict, as it must be, since \( \A \) is not diagonal and no diagonal entry is \( 0 \).
:::

:::: {#exr-majorization-and-schur-b3}
[B3: Which diagonals are ruled out?]

A Hermitian \( 3 \times 3 \) matrix has eigenvalues \( 5, 1, 0 \). For each proposed list of diagonal entries, determine whether @thm-schur-majorization rules it out. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( 4, 2, 0 \).
2. \( 6, 0, 0 \).
3. \( 3, 3, 1 \).
4. \( 2, 2, 2 \).
5. \( -1, 4, 3 \).
:::

For the lists that are not ruled out, what does @thm-schur-horn add?
::::

::: {.solution}
Here \( \vlambda = (5, 1, 0) \), with running totals \( 5, 6 \) and total \( 6 \).

(a) Running totals \( 4, 6 \), total \( 6 \). Since \( 4 \le 5 \) and \( 6 \le 6 \), the list is **not** ruled out.

(b) At \( k = 1 \), \( 6 > 5 \). **Ruled out.** No diagonal entry can exceed \( \lambda_1 \).

(c) The total is \( 7 \ne 6 \). **Ruled out** by (M2): the trace would be wrong.

(d) This is the flat vector with total \( 6 \), which is majorized by every vector with total \( 6 \) (@exm-majorization-first-examples (b)). **Not** ruled out.

(e) Sorted, it is \( (4, 3, -1) \), with running totals \( 4, 7 \) and total \( 6 \). At \( k = 2 \), \( 7 > 6 \). **Ruled out.** Independently, \( -1 < 0 = \lambda_3 \) contradicts the bottom-end inequality of the warning.

Schur's theorem is only a necessary condition, so for (a) and (d) it shows only that nothing forbids these diagonals. @thm-schur-horn adds that they occur: for each of them there is a real symmetric matrix with eigenvalues \( 5, 1, 0 \) and that diagonal.
:::

### C. Going deeper

:::: {#exr-majorization-and-schur-c1}
[C1: Majorization squeezes the range]

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( \x \prec \y \), then \( y^{\downarrow}_n \le x^{\downarrow}_n \le x^{\downarrow}_1 \le y^{\downarrow}_1 \).
2. Deduce that every diagonal entry of a Hermitian \( \A \) lies in \( [\lambda_n(\A), \lambda_1(\A)] \).
3. Show that the conclusion of (b), together with equal totals, does **not** imply majorization. Prove that no Hermitian matrix has eigenvalues \( 4, 1, 1, 0 \) and diagonal entries \( 3, 3, 0, 0 \), although every one of these entries lies in \( [0, 4] \) and the totals agree.
:::
::::

::: {.solution}
(a) The inequality \( x^{\downarrow}_1 \le y^{\downarrow}_1 \) is (M1) at \( k = 1 \) (for \( n = 1 \), \( \x = \y \) by @exm-majorization-first-examples (d), and there is nothing to prove). The middle inequality holds because \( \x^{\downarrow} \) is decreasing. For the left inequality, subtract (M1) at \( k = n - 1 \) from (M2):
\[
\begin{aligned}
x^{\downarrow}_n &= \sum_{i=1}^{n} x_i - \sum_{i=1}^{n-1} x^{\downarrow}_i \\
&\ge \sum_{i=1}^{n} y_i - \sum_{i=1}^{n-1} y^{\downarrow}_i = y^{\downarrow}_n .
\end{aligned}
\]

(b) By @thm-schur-majorization, \( \d(\A) \prec \vlambda(\A) \). Apply (a) with \( \x = \d(\A) \) and \( \y = \vlambda(\A) \), using \( \vlambda(\A)^{\downarrow} = \vlambda(\A) \). Every diagonal entry lies between the smallest and the largest diagonal entry, which (a) places between \( \lambda_n(\A) \) and \( \lambda_1(\A) \). (This also follows from @lem-extreme-eigenvalues-quadratic-form at \( \x = \e_i \). The point of (a) is that it is a property of majorization itself.)

(c) The vector \( (3, 3, 0, 0) \) has running totals \( 3, 6, 6 \), and \( (4, 1, 1, 0) \) has \( 4, 5, 6 \). At \( k = 2 \), \( 6 > 5 \), so \( (3, 3, 0, 0) \not\prec (4, 1, 1, 0) \), and by @thm-schur-majorization no Hermitian matrix has this diagonal and this spectrum. Yet \( 0 \le 3, 3, 0, 0 \le 4 \), and both totals are \( 6 \). The range condition controls only the running totals at \( k = 1 \) and \( k = n - 1 \), while majorization constrains the middle ones too, which is why the example needs \( n \ge 4 \).
:::

:::: {#exr-majorization-and-schur-c2}
[C2: A weaker determinant bound]

Let \( \A \in M_n(F) \) with \( \A \succeq 0 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \det \A \le \bigl(\tfrac1n\tr \A\bigr)^{n} \), with equality if and only if \( \A = c\I \) for some real \( c \ge 0 \).
2. Prove that \( a_{11}\cdots a_{nn} \le \bigl(\tfrac1n\tr \A\bigr)^{n} \). Deduce that Hadamard's inequality (@thm-hadamard-inequality) always implies the bound in (a).
3. For
\[
\A = \begin{pmatrix} 2 & 0 & 2 \\ 0 & 5 & 2 \\ 2 & 2 & 6 \end{pmatrix} ,
\]
whose eigenvectors are \( (1, 2, 3) \), \( (1, -2, 1) \) and \( (-4, -1, 2) \), compute the three numbers \( \det \A \), \( a_{11}a_{22}a_{33} \) and \( \bigl(\tfrac13\tr\A\bigr)^{3} \).
:::
::::

::: {.solution}
(a) The eigenvalues \( \lambda_i(\A) \) are non-negative by @thm-psd-characterizations (b). By @thm-trace-det-eigenvalues and @lem-am-gm,
\[
\det \A = \prod_i \lambda_i(\A) \le \Bigl(\frac1n\sum_i\lambda_i(\A)\Bigr)^{n} = \Bigl(\frac1n\tr \A\Bigr)^{n} .
\]
Equality holds if and only if all \( \lambda_i(\A) \) equal a common value \( c \ge 0 \). By the spectral theorem this happens if and only if \( \A = \U(c\I)\U^{*} = c\I \). Conversely, \( \A = c\I \) gives equality directly.

(b) The \( a_{ii} \) are non-negative (as in the proof of @cor-hadamard-from-majorization) and add up to \( \tr \A \). So @lem-am-gm gives \( \prod_i a_{ii} \le (\tfrac1n\tr\A)^{n} \). Combined with @cor-hadamard-from-majorization, this gives \( \det \A \le \prod_i a_{ii} \le (\tfrac1n\tr\A)^n \), so the Hadamard bound always sits between \( \det \A \) and the bound of (a). The bound in (a) sees only the total of the diagonal, while Hadamard's bound sees each entry, and so it is never worse.

(c) Check the eigenvectors: \( \A(1,2,3) = (2 + 6,\ 10 + 6,\ 2 + 4 + 18) = (8, 16, 24) \); \( \A(1,-2,1) = (2 + 2,\ -10 + 2,\ 2 - 4 + 6) = (4, -8, 4) \); \( \A(-4,-1,2) = (-8 + 4,\ -5 + 4,\ -8 - 2 + 12) = (-4, -1, 2) \). So \( \vlambda(\A) = (8, 4, 1) \), and \( \A \succ 0 \). Then
\[
\begin{aligned}
\det \A &= 8 \cdot 4 \cdot 1 = 32, \qquad a_{11}a_{22}a_{33} = 2 \cdot 5 \cdot 6 = 60, \\
\Bigl(\frac{\tr \A}{3}\Bigr)^{3} &= \Bigl(\frac{13}{3}\Bigr)^{3} = \frac{2197}{27} \approx 81.4 ,
\end{aligned}
\]
and \( 32 \le 60 \le 81.4 \), with both inequalities strict.
:::

:::: {#exr-majorization-and-schur-c3}
[C3: The possible diagonals form a convex set]

For \( \x \in \nR^n \) and \( 1 \le k \le n \), write \( s_k(\x) = x^{\downarrow}_1 + \dots + x^{\downarrow}_k \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( s_k(\x) = \max\bigl\{ \sum_{i \in I} x_i : I \subseteq \{1, \dots, n\},\ \lvert I\rvert = k \bigr\} \).
2. Deduce that \( s_k(\x + \y) \le s_k(\x) + s_k(\y) \) for all \( \x, \y \in \nR^n \).
3. Let \( \vlambda \in \nR^n \). Prove that if \( \d \prec \vlambda \) and \( \d' \prec \vlambda \), then \( t\d + (1 - t)\d' \prec \vlambda \) for every \( 0 \le t \le 1 \).
4. Hence show that if \( \A \) and \( \B \) are Hermitian \( n \times n \) matrices with the same eigenvalues, then for every \( 0 \le t \le 1 \) there is a real symmetric matrix with those eigenvalues and diagonal \( t\,\d(\A) + (1 - t)\,\d(\B) \).
:::

*Hint for (a): if \( v_1 \ge \dots \ge v_k \) are the entries \( x_i \), \( i \in I \), in decreasing order, count how many entries of \( \x \) are at least \( v_j \).*
::::

::: {.solution}
(a) Let \( \lvert I\rvert = k \), and list the entries \( x_i \), \( i \in I \), decreasingly as \( v_1 \ge \dots \ge v_k \). For each \( j \le k \), the entries \( v_1, \dots, v_j \) sit at \( j \) different positions of \( \x \) and are all \( \ge v_j \). If \( x^{\downarrow}_j < v_j \), then, since \( \x^{\downarrow} \) is decreasing, only \( x^{\downarrow}_1, \dots, x^{\downarrow}_{j-1} \) could be \( \ge v_j \), which is fewer than \( j \) entries. Hence \( v_j \le x^{\downarrow}_j \) for every \( j \), and summing gives \( \sum_{i \in I} x_i \le s_k(\x) \). The bound is attained by the positions of the \( k \) largest entries, chosen as in the proof of @thm-schur-majorization. This proves (a).

(b) Let \( I \) be a set of \( k \) positions at which \( \x + \y \) attains the maximum in (a). Applying (a) three times,
\[
s_k(\x + \y) = \sum_{i \in I} x_i + \sum_{i \in I} y_i \le s_k(\x) + s_k(\y) .
\]

(c) Put \( \z = t\d + (1 - t)\d' \). Its total is \( t\sum_i \lambda_i + (1 - t)\sum_i \lambda_i = \sum_i \lambda_i \), by (M2) for both hypotheses. For a scalar \( c \ge 0 \), multiplying by \( c \) does not change the order of the entries, so \( s_k(c\x) = c\,s_k(\x) \). For \( 1 \le k \le n - 1 \), (b) and (M1) for both hypotheses give
\[
s_k(\z) \le t\,s_k(\d) + (1 - t)\,s_k(\d') \le t\,s_k(\vlambda) + (1 - t)\,s_k(\vlambda) = s_k(\vlambda) .
\]
So \( \z \prec \vlambda \).

(d) Let \( \vlambda = \vlambda(\A) = \vlambda(\B) \). By @thm-schur-majorization, \( \d(\A) \prec \vlambda \) and \( \d(\B) \prec \vlambda \). By (c), \( t\,\d(\A) + (1 - t)\,\d(\B) \prec \vlambda \). By @thm-horn there is a real symmetric matrix with eigenvalues \( \vlambda \) and exactly this diagonal. So among Hermitian matrices with a fixed spectrum, the set of diagonals contains the segment between any two of its points: it is **convex**.
:::
