# Gershgorin Discs

Chapter 16 bounded the whole spectrum with one number: every eigenvalue lies in the disc \( \lvert z\rvert \le \norm{\A}_{\infty} \) (@cor-spectral-radius-row-column-bound). That disc is centered at \( 0 \), and it knows nothing about where in it the eigenvalues sit. For a matrix that is nearly diagonal the answer ought to be visible at a glance: the eigenvalues should sit near the diagonal entries, and the off-diagonal entries should say how near. This section makes that precise. It puts one disc around each diagonal entry, with radius measured from the rest of its row, and proves that the discs together hold every eigenvalue. It then sharpens the picture twice: by rescaling the coordinates, and, for irreducible matrices, by looking at the boundary.

**Throughout, matrices are complex.** A real matrix is read inside \( M_n(\nC) \), as in Chapter 16 §04, because its eigenvalues may be non-real, and they are what we want to locate.

## Discs around the diagonal

Here is the situation to keep in mind. Take
\[
\A = \begin{pmatrix} 6 & 2 & 5 \\ 1 & -1 & 1 \\ 1 & 1 & -1 \end{pmatrix} .
\]
The row-sum bound gives \( \lvert\lambda\rvert \le \norm{\A}_{\infty} = 13 \) for every eigenvalue \( \lambda \), a disc of radius \( 13 \) about \( 0 \). But if the off-diagonal entries were \( 0 \), the eigenvalues would be exactly \( 6, -1, -1 \). The off-diagonal entries are a perturbation of the diagonal matrix, and the natural guess is that each eigenvalue stays within reach of some diagonal entry, where the reach of row \( i \) is measured by the size of the entries of row \( i \) off the diagonal. We give that reach a name.

*Around each diagonal entry, draw the disc whose radius is the total size of the other entries in its row.*

::: {#def-gershgorin-discs}
[Gershgorin Discs]

Let \( n \ge 1 \) and \( \A = (a_{ij}) \in M_n(\nC) \). For \( i = 1, \dots, n \), the **\( i \)-th Gershgorin radius** of \( \A \) is the real number
\[
r_i(\A) \coloneqq \sum_{j \ne i} \lvert a_{ij}\rvert \ \ge 0 ,
\]
the sum over **all** \( j \in \{1, \dots, n\} \) **other than** \( i \), and the **\( i \)-th Gershgorin disc** is the **closed** disc
\[
D_i(\A) \coloneqq \{\, z \in \nC : \lvert z - a_{ii}\rvert \le r_i(\A) \,\} .
\]
The discs \( D_i(\A\tp) \), whose radii \( r_i(\A\tp) = \sum_{j \ne i}\lvert a_{ji}\rvert \) are taken from the **columns** of \( \A \), are the **column discs**.
:::

In words: the center of \( D_i(\A) \) is the diagonal entry \( a_{ii} \), and the radius adds up the moduli of the entries of row \( i \) that are **not** on the diagonal. The disc includes its boundary circle. A radius may be \( 0 \), and then the disc is the single point \( a_{ii} \). Since \( \A\tp \) has the same diagonal as \( \A \), the column discs have the same centers as the row discs and, in general, different radii. The letter \( r \) is lowercase on purpose, since \( R_{\A} \) is the Rayleigh quotient, and the plain \( D_i \) is a set of complex numbers, not the bold diagonal matrix \( \D \).

Some examples, simplest first.

- **Diagonal matrices and \( n = 1 \).** For \( \A = \diag(d_1, \dots, d_n) \) every radius is \( 0 \), because every off-diagonal entry is \( 0 \), and \( D_i(\A) = \{d_i\} \). The discs are the eigenvalues. A \( 1 \times 1 \) matrix \( (a) \) is the case \( n = 1 \): the sum defining \( r_1 \) is empty, so \( D_1 = \{a\} \). These degenerate cases are the ones any theorem about the discs must get exactly right.
- **A \( 2 \times 2 \) matrix.** For \( \B = \begin{psmallmatrix} 0 & 1 \\ 4 & 0 \end{psmallmatrix} \), \( r_1(\B) = 1 \) and \( r_2(\B) = 4 \), so the row discs are \( \lvert z\rvert \le 1 \) and \( \lvert z\rvert \le 4 \). The column discs swap the radii: \( \lvert z\rvert \le 4 \) and \( \lvert z\rvert \le 1 \).
- **The matrix above.** \( r_1(\A) = 2 + 5 = 7 \), \( r_2(\A) = 1 + 1 = 2 \) and \( r_3(\A) = 1 + 1 = 2 \), so \( D_1(\A) = \{\lvert z - 6\rvert \le 7\} \) and \( D_2(\A) = D_3(\A) = \{\lvert z + 1\rvert \le 2\} \). The column radii are \( 1 + 1 = 2 \), \( 2 + 1 = 3 \) and \( 5 + 1 = 6 \).

**Non-example by minimal change.** Keep the radius and move the center to \( 0 \): replace \( D_i(\A) \) by \( \{\lvert z\rvert \le r_i(\A)\} \). For \( \diag(1, 2) \) both radii are \( 0 \) and the modified "discs" are both \( \{0\} \), which misses both eigenvalues. The clause that changed is the center, and the diagonal example shows it is the part that carries the information: the radius only measures how far the off-diagonal part can pull an eigenvalue away from it.

## The theorem

It turns out that the guess is right, with no loss at all in the constant:

::: {#thm-gershgorin}
[Gershgorin's Theorem]

Let \( n \ge 1 \), \( \A \in M_n(\nC) \), and let \( \lambda \) be an eigenvalue of \( \A \) with eigenvector \( \x = (x_1, \dots, x_n) \). If \( k \) is an index with \( \lvert x_k\rvert = \max_j \lvert x_j\rvert \), then \( \lambda \in D_k(\A) \). Consequently:

::: {.enumerate options="label=(\alph*)"}
1. every eigenvalue of \( \A \) lies in the union \( D_1(\A) \cup \dots \cup D_n(\A) \) of the row discs;
2. every eigenvalue of \( \A \) lies in the union \( D_1(\A\tp) \cup \dots \cup D_n(\A\tp) \) of the column discs;
3. hence every eigenvalue lies in the intersection of the two unions.
:::
:::

::: {.idea}
We want \( \lvert\lambda - a_{kk}\rvert \) to be small for one well-chosen \( k \), so look at row \( k \) of \( \A\x = \lambda\x \) and move the diagonal term across: \( (\lambda - a_{kk})x_k = \sum_{j \ne k} a_{kj}x_j \). The triangle inequality bounds the right side by \( \sum_{j \ne k}\lvert a_{kj}\rvert\lvert x_j\rvert \), and this becomes \( r_k(\A)\lvert x_k\rvert \) exactly when every \( \lvert x_j\rvert \le \lvert x_k\rvert \). So choose \( k \) where the eigenvector is largest in modulus. Then divide by \( \lvert x_k\rvert \), which is positive because \( \x \ne \0 \).
:::

::: {.proof}
Let \( \A\x = \lambda\x \) with \( \x \ne \0 \), and let \( k \) be as in the statement; such a \( k \) exists because a finite set of real numbers has a largest element. Since \( \x \ne \0 \), some \( x_j \ne 0 \), so \( \lvert x_k\rvert > 0 \). Row \( k \) of \( \A\x = \lambda\x \) reads \( \sum_{j} a_{kj}x_j = \lambda x_k \), that is,
\[
(\lambda - a_{kk})\,x_k = \sum_{j \ne k} a_{kj}x_j .
\]
Taking moduli and using the triangle inequality (@thm-complex-triangle-inequality), then \( \lvert x_j\rvert \le \lvert x_k\rvert \) for every \( j \),
\[
\lvert\lambda - a_{kk}\rvert\,\lvert x_k\rvert
\le \sum_{j \ne k}\lvert a_{kj}\rvert\,\lvert x_j\rvert
\le \Bigl(\sum_{j \ne k}\lvert a_{kj}\rvert\Bigr)\lvert x_k\rvert
= r_k(\A)\,\lvert x_k\rvert .
\]
Dividing by \( \lvert x_k\rvert > 0 \) gives \( \lvert\lambda - a_{kk}\rvert \le r_k(\A) \), that is, \( \lambda \in D_k(\A) \).

(a) Every eigenvalue has an eigenvector, and the disc just found is one of the \( D_i(\A) \).

(b) By @prp-left-eigenvectors-transpose (b), \( \A\tp \) has the same eigenvalues as \( \A \). Applying (a) to \( \A\tp \) puts each of them in \( D_1(\A\tp) \cup \dots \cup D_n(\A\tp) \).

(c) A point lying in each of two sets lies in their intersection. This proves the theorem.
:::

The move in this proof is worth naming, since the chapter uses it again: **choose the dominant coordinate of an eigenvector, then apply the triangle inequality to its row.** The choice of the largest coordinate is exactly what lets every \( \lvert x_j\rvert \) be replaced by \( \lvert x_k\rvert \) without looking at the others.

The theorem recovers Chapter 16's bound and improves on it. If \( \lambda \in D_k(\A) \), then
\[
\begin{aligned}
\lvert\lambda\rvert &\le \lvert a_{kk}\rvert + \lvert\lambda - a_{kk}\rvert \le \lvert a_{kk}\rvert + r_k(\A) \\
&= \sum_{j}\lvert a_{kj}\rvert \le \norm{\A}_{\infty} ,
\end{aligned}
\]
so (a) implies \( \rho(\A) \le \norm{\A}_{\infty} \), and (b) likewise implies \( \rho(\A) \le \norm{\A}_1 \). The union of the discs is never larger than the row-sum disc, and it is usually much smaller, because it keeps the centers.

::: {#exm-gershgorin-three}
[Discs, eigenvectors, and where each eigenvalue sits]

Let \( \A = \begin{pmatrix} 6 & 2 & 5 \\ 1 & -1 & 1 \\ 1 & 1 & -1 \end{pmatrix} \). Describe the regions given by @thm-gershgorin (a) and (b). Then check that \( (7, 1, 1) \), \( (-1, 1, 1) \) and \( (1, 1, -2) \) are eigenvectors, and locate each eigenvalue in the disc the theorem assigns to it.
:::

::: {.solution}
From the radii computed after @def-gershgorin-discs, the row discs give
\[
\{\lvert z - 6\rvert \le 7\} \cup \{\lvert z + 1\rvert \le 2\} ,
\]
the second disc counted twice, and the column discs give \( \{\lvert z - 6\rvert \le 2\} \cup \{\lvert z + 1\rvert \le 3\} \cup \{\lvert z + 1\rvert \le 6\} \), where the middle disc lies inside the last. So every eigenvalue lies in \( \{\lvert z - 6\rvert \le 2\} \cup \{\lvert z + 1\rvert \le 6\} \), and also in \( \{\lvert z - 6\rvert \le 7\} \cup \{\lvert z + 1\rvert \le 2\} \). The column discs have separated the two groups of centers; the row discs have not.

Multiplying out,
\[
\A\begin{pmatrix} 7 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 49 \\ 7 \\ 7 \end{pmatrix}, \quad
\A\begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \\ -1 \end{pmatrix}, \quad
\A\begin{pmatrix} 1 \\ 1 \\ -2 \end{pmatrix} = \begin{pmatrix} -2 \\ -2 \\ 4 \end{pmatrix},
\]
so the eigenvalues include \( 7 \), \( -1 \) and \( -2 \). These are three distinct eigenvalues of a \( 3 \times 3 \) matrix, hence three distinct roots of the degree-\( 3 \) polynomial \( p_{\A} \) (@thm-eigenvalue-characterizations), so by @cor-root-bound-general there are no others.

- The eigenvector \( (7, 1, 1) \) peaks at \( k = 1 \), and indeed \( \lvert 7 - 6\rvert = 1 \le 7 \): \( 7 \in D_1(\A) \).
- The eigenvector \( (1, 1, -2) \) peaks at \( k = 3 \), and \( \lvert -2 + 1\rvert = 1 \le 2 \): \( -2 \in D_3(\A) \).
- The eigenvector \( (-1, 1, 1) \) has all three coordinates of modulus \( 1 \), so every \( k \) is a peak and \( -1 \) must lie in every row disc. It does: \( \lvert -1 - 6\rvert = 7 = r_1(\A) \), so it sits on the boundary circle of \( D_1(\A) \), and it is the center of the other two.

Both unions pass the test, and the eigenvector tells us which disc to look in. The row-sum disc \( \lvert z\rvert \le 13 \) says only that \( \lvert\lambda\rvert \le 13 \).
:::

::: {.warning}
**The union is the claim, not each disc.** A single Gershgorin disc need not contain any eigenvalue. For \( \B = \begin{psmallmatrix} 0 & 1 \\ 4 & 0 \end{psmallmatrix} \), \( p_{\B}(x) = x^2 - 4 \), so the eigenvalues are \( \pm 2 \), while the first row disc is \( \lvert z\rvert \le 1 \): it contains neither. Both eigenvalues lie in the second disc \( \lvert z\rvert \le 4 \). Nor may the row disc and the column disc of the same index be intersected: \( D_1(\B) \cap D_1(\B\tp) \) and \( D_2(\B) \cap D_2(\B\tp) \) are both \( \lvert z\rvert \le 1 \), and \( \pm 2 \) lies in neither. Part (c) of the theorem intersects the two **unions**.
:::

::: {.check}
Without computing any eigenvalue, show that every eigenvalue of \( \M = \begin{pmatrix} 5 & 2 & -1 \\ 1 & 6 & 2 \\ -1 & 0 & 3 \end{pmatrix} \) has real part at least \( 2 \).
:::

::: {.solution}
The row discs are \( \lvert z - 5\rvert \le 3 \), \( \lvert z - 6\rvert \le 3 \) and \( \lvert z - 3\rvert \le 1 \). A point \( z \) of the first has \( \operatorname{Re} z \ge 5 - \lvert z - 5\rvert \ge 2 \), of the second \( \operatorname{Re} z \ge 3 \), of the third \( \operatorname{Re} z \ge 2 \). By @thm-gershgorin (a) every eigenvalue lies in one of them, so its real part is at least \( 2 \). In particular \( 0 \) is not an eigenvalue, and \( \M \) is invertible.
:::

## Diagonal dominance

The last sentence of the Quick check is a pattern. If \( 0 \) lies outside every disc, then \( 0 \) is not an eigenvalue, and the matrix is invertible. The point \( 0 \) lies outside \( D_i(\A) \) exactly when \( \lvert 0 - a_{ii}\rvert > r_i(\A) \), which is a condition on row \( i \) alone.

::: {#cor-diagonally-dominant-invertible}
[Strict Diagonal Dominance Implies Invertibility]

Let \( n \ge 1 \) and \( \A \in M_n(\nC) \). Call \( \A \) **strictly diagonally dominant** (by rows) if
\[
\lvert a_{ii}\rvert > r_i(\A) = \sum_{j \ne i}\lvert a_{ij}\rvert \qquad\text{for **every** } i = 1, \dots, n .
\]
A strictly diagonally dominant matrix is invertible. The same holds if \( \A \) is strictly diagonally dominant **by columns**, that is, if \( \A\tp \) is strictly diagonally dominant.
:::

::: {.proof}
Suppose \( \A \) is strictly diagonally dominant. For every \( i \), \( \lvert 0 - a_{ii}\rvert > r_i(\A) \), so \( 0 \notin D_i(\A) \). Hence \( 0 \) lies in no row disc, and by @thm-gershgorin (a) it is not an eigenvalue. By @thm-eigenvalue-characterizations, \( 0\I - \A = -\A \) is invertible, and so is \( \A \). If instead \( \A\tp \) is strictly diagonally dominant, then \( 0 \) lies in no column disc, and @thm-gershgorin (b) finishes in the same way.
:::

This is the **Lévy–Desplanques theorem**. The word **strictly** carries the weight, and the definition asks it of **every** row. Examples: \( \begin{psmallmatrix} 3 & 1 & 1 \\ 0 & 2 & 1 \\ 1 & -1 & 4 \end{psmallmatrix} \) is strictly dominant, since \( 3 > 2 \), \( 2 > 1 \), \( 4 > 2 \); every diagonal matrix with non-zero diagonal is, since every radius is \( 0 \); and a \( 1 \times 1 \) matrix \( (a) \) is strictly dominant exactly when \( a \ne 0 \). A minimal change breaks it. \( \begin{psmallmatrix} 1 & 1 \\ 1 & 1 \end{psmallmatrix} \) has \( \lvert a_{ii}\rvert = 1 = r_i \) in both rows: it is dominant only weakly, and it is singular. The converse of the corollary is false: \( \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix} \) is invertible and has zero diagonal. Diagonal dominance is a certificate of invertibility, cheap to check and often available, not a characterization.

## Hermitian matrices, and intervals

For a Hermitian \( \A \) the eigenvalues are real (@thm-self-adjoint-real-eigenvalues), and so are the diagonal entries, since \( a_{ii} = \conj{a_{ii}} \). So only the part of each disc on the real line matters, which is the interval \( [a_{ii} - r_i(\A),\, a_{ii} + r_i(\A)] \). @thm-gershgorin (a) then says
\[
\min_i\bigl(a_{ii} - r_i(\A)\bigr) \le \lambda_n(\A) \le \lambda_1(\A) \le \max_i\bigl(a_{ii} + r_i(\A)\bigr) .
\]
For \( \A = \begin{psmallmatrix} 4 & 1 & 0 \\ 1 & 6 & 2 \\ 0 & 2 & 9 \end{psmallmatrix} \) the intervals are \( [3, 5] \), \( [3, 9] \) and \( [7, 11] \), so every eigenvalue lies in \( [3, 11] \), and \( \A \) is positive definite by @thm-pd-characterizations, since its eigenvalues are positive; Exercise C1 turns this into a general criterion. For a Hermitian matrix the row and column discs coincide, since \( \lvert a_{ji}\rvert = \lvert\conj{a_{ij}}\rvert \), so (b) adds nothing.

## Scaling the discs

The discs depend on the matrix, and the eigenvalues depend only on its similarity class. So any similarity that is easy to compute gives new discs for the same eigenvalues. The cheapest one rescales the coordinates.

::: {#prp-gershgorin-scaling}
[Rescaling the Gershgorin Discs]

Let \( \A \in M_n(\nC) \), let \( d_1, \dots, d_n \) be **positive** real numbers, and \( \D = \diag(d_1, \dots, d_n) \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \D^{-1}\A\D \) has entries \( a_{ij}d_j/d_i \). It has the same diagonal as \( \A \), and the same eigenvalues with the same algebraic multiplicities.
2. \( r_i(\D^{-1}\A\D) = \dfrac{1}{d_i}\sum_{j \ne i}\lvert a_{ij}\rvert\,d_j \) for each \( i \).
3. Every eigenvalue of \( \A \) lies in
\[
\bigcup_{i=1}^{n}\Bigl\{\, z : \lvert z - a_{ii}\rvert \le \frac{1}{d_i}\sum_{j \ne i}\lvert a_{ij}\rvert\,d_j \,\Bigr\} .
\]
:::
:::

::: {.proof}
(a) \( \D \) is invertible with \( \D^{-1} = \diag(1/d_1, \dots, 1/d_n) \), because every \( d_i \ne 0 \). Multiplying by a diagonal matrix on the left scales rows and on the right scales columns, so \( (\D^{-1}\A\D)_{ij} = d_i^{-1}a_{ij}d_j \), and for \( i = j \) this is \( a_{ii} \). The matrices \( \A \) and \( \D^{-1}\A\D \) are similar, so they have the same characteristic polynomial (@thm-charpoly-similarity-invariant), hence the same eigenvalues with the same multiplicities.

(b) By (a) and \( d_i, d_j > 0 \), \( \lvert a_{ij}d_j/d_i\rvert = \lvert a_{ij}\rvert d_j/d_i \); sum over \( j \ne i \).

(c) Apply @thm-gershgorin (a) to \( \D^{-1}\A\D \) and use (a) and (b).
:::

Taking \( d_1 > 1 \) and the other \( d_j = 1 \) divides the first radius by \( d_1 \) and multiplies the entry \( \lvert a_{i1}\rvert \) inside every other radius by \( d_1 \). So scaling shrinks some discs at the expense of others, and the art is to shrink the disc we care about while the others can afford to grow. The same move appeared in Chapter 19 §09, where \( \D = \diag(\x) \) turned the entries of \( \B\x \) into row sums.

::: {#exm-gershgorin-scaling}
[Separating a disc by scaling]

For \( \A = \begin{pmatrix} 6 & 2 & 5 \\ 1 & -1 & 1 \\ 1 & 1 & -1 \end{pmatrix} \) of @exm-gershgorin-three, the row disc \( D_1(\A) = \{\lvert z - 6\rvert \le 7\} \) overlaps \( \{\lvert z + 1\rvert \le 2\} \). Find a scaling \( \D = \diag(d, 1, 1) \) whose row discs split into two disjoint groups, and find the range of \( d \) that does it.
:::

::: {.solution}
By @prp-gershgorin-scaling (b) with \( d_1 = d \) and \( d_2 = d_3 = 1 \), the scaled radii are
\[
r_1 = \frac{2 + 5}{d} = \frac{7}{d}, \qquad r_2 = 1\cdot d + 1 = d + 1, \qquad r_3 = d + 1 ,
\]
with centers \( 6 \), \( -1 \), \( -1 \). The first disc is disjoint from the other two exactly when the distance \( 7 \) between the centers exceeds the sum of the radii:
\[
\frac{7}{d} + d + 1 < 7 \iff d^2 - 6d + 7 < 0 \iff 3 - \sqrt2 < d < 3 + \sqrt2 ,
\]
where we multiplied by \( d > 0 \). For instance \( d = 2 \) gives \( \D^{-1}\A\D = \begin{psmallmatrix} 6 & 1 & 5/2 \\ 2 & -1 & 1 \\ 2 & 1 & -1 \end{psmallmatrix} \) and the discs
\[
\{\lvert z - 6\rvert \le \tfrac72\} \quad\text{and}\quad \{\lvert z + 1\rvert \le 3\} ,
\]
the second counted twice, which are disjoint since \( \tfrac72 + 3 < 7 \). The eigenvalues \( 7 \), \( -1 \), \( -2 \) are distributed one in the first disc and two in the second, as the figure shows.
:::

\begin{center}
\begin{tikzpicture}[scale=0.26, lab/.style={font=\small}]
  \begin{scope}
    \draw[->, gray] (-4,0) -- (14,0);
    \draw[->, gray] (0,-7.6) -- (0,7.6);
    \draw[thick] (6,0) circle (7);
    \draw[thick, dashed] (-1,0) circle (2);
    \fill (7,0) circle (0.25);
    \fill (-1,0) circle (0.25);
    \fill (-2,0) circle (0.25);
    \node[lab] at (5,-9) {unscaled};
  \end{scope}
  \begin{scope}[xshift=22cm]
    \draw[->, gray] (-4.6,0) -- (10.5,0);
    \draw[->, gray] (0,-7.6) -- (0,7.6);
    \draw[thick] (6,0) circle (3.5);
    \draw[thick, dashed] (-1,0) circle (3);
    \fill (7,0) circle (0.25);
    \fill (-1,0) circle (0.25);
    \fill (-2,0) circle (0.25);
    \node[lab] at (3,-9) {scaled by $\mathrm{diag}(2,1,1)$};
  \end{scope}
  \node[lab, align=center] at (13,-12.5)
    {Row discs of the matrix of the example before and after scaling: the solid disc is centered\\
     at $6$, the dashed disc at $-1$ (rows $2$ and $3$), and the dots are the eigenvalues $7$, $-1$, $-2$};
\end{tikzpicture}
\end{center}

Scaling has bought a picture in which the eigenvalues fall into two groups, one near \( 6 \) and two near \( -1 \). What it has **not** yet bought is the statement that the first disc contains exactly one eigenvalue. @thm-gershgorin says only that the union holds all three, and nothing so far forbids all three from lying in the second disc. The counting statement is true, but it needs the eigenvalues to move continuously as the off-diagonal part is switched on, and §03 proves it. For a real matrix like this one, §03 will also show that an isolated disc centered on the real axis holds a **real** eigenvalue.

## Eigenvalues on the boundary

Diagonal dominance fails for a matrix that matters. The second-difference matrix \( \K_n \) of Chapter 19 §09 has \( 2 \) on the diagonal and \( -1 \) beside it, so for \( n \ge 3 \) its interior rows have \( \lvert a_{ii}\rvert = 2 = r_i(\K_n) \). The discs \( \lvert z - 2\rvert \le 2 \) pass through \( 0 \), and @cor-diagonally-dominant-invertible says nothing, although \( \K_n \) is invertible. Only the first and last rows are strict. What rescues it is that the rows are **linked**: the dominant coordinate of an eigenvector cannot stay in the equality rows without spreading to the strict ones. The link is irreducibility, in the sense of @def-irreducible, and by @thm-irreducible-iff-strongly-connected it means that the graph \( G(\A) \), with an edge \( j \to i \) whenever \( a_{ij} \ne 0 \), is strongly connected.

::: {#thm-taussky}
[Taussky's Theorem]

Let \( n \ge 1 \), let \( \A \in M_n(\nC) \) be **irreducible**, and let \( \lambda \) be an eigenvalue of \( \A \) with
\[
\lvert\lambda - a_{ii}\rvert \ge r_i(\A) \qquad\text{for **every** } i ,
\]
that is, \( \lambda \) lies in no open disc \( \{\lvert z - a_{ii}\rvert < r_i(\A)\} \). Then \( \lvert\lambda - a_{ii}\rvert = r_i(\A) \) for every \( i \): the eigenvalue lies on the boundary circle of **every** Gershgorin disc. Moreover, every eigenvector for \( \lambda \) has all its coordinates of the same modulus. The hypothesis holds in particular when \( \lambda \) is a boundary point (@def-interior-point) of \( D_1(\A) \cup \dots \cup D_n(\A) \).
:::

::: {.idea}
Run the proof of @thm-gershgorin at a peak index \( k \). The hypothesis \( \lvert\lambda - a_{kk}\rvert \ge r_k \) makes the two ends of its chain of inequalities equal, so every inequality in the chain is an equality. The second one, \( \sum_{j \ne k}\lvert a_{kj}\rvert\lvert x_j\rvert \le r_k\lvert x_k\rvert \), is an equality only if \( \lvert x_j\rvert = \lvert x_k\rvert \) whenever \( a_{kj} \ne 0 \). So the set of peak indices is closed under following edges of \( G(\A) \) backwards. Strong connectivity then drags every index into it.
:::

::: {.proof}
Let \( \A\x = \lambda\x \) with \( \x \ne \0 \), put \( m = \max_j\lvert x_j\rvert > 0 \) and \( S = \{k : \lvert x_k\rvert = m\} \), which is non-empty.

::: {.claim}
If \( k \in S \), then \( \lvert\lambda - a_{kk}\rvert = r_k(\A) \), and every \( j \ne k \) with \( a_{kj} \ne 0 \) lies in \( S \).

::: {.proof}
By the hypothesis and the chain of inequalities in the proof of @thm-gershgorin, with \( \lvert x_k\rvert = m \),
\[
r_k(\A)\,m \le \lvert\lambda - a_{kk}\rvert\,m \le \sum_{j \ne k}\lvert a_{kj}\rvert\,\lvert x_j\rvert \le r_k(\A)\,m .
\]
The two ends agree, so every inequality is an equality. The first gives \( \lvert\lambda - a_{kk}\rvert = r_k(\A) \), after dividing by \( m > 0 \). The last says \( \sum_{j \ne k}\lvert a_{kj}\rvert\,(m - \lvert x_j\rvert) = 0 \). Each term is non-negative, so each is \( 0 \), and \( a_{kj} \ne 0 \) forces \( \lvert x_j\rvert = m \), that is, \( j \in S \).
:::
:::

Now let \( i \) be any index and fix \( k \in S \). By @thm-irreducible-iff-strongly-connected, \( G(\A) \) has a walk \( i = i_0, i_1, \dots, i_t = k \). We show \( i_s \in S \) for \( s = t, t-1, \dots, 0 \). For \( s = t \) this is \( k \in S \). If \( i_s \in S \) with \( s \ge 1 \), then \( i_{s-1} \to i_s \) is an edge, so \( a_{i_s i_{s-1}} \ne 0 \); either \( i_{s-1} = i_s \in S \), or the Claim applied to \( i_s \) puts \( i_{s-1} \) in \( S \). Hence \( i \in S \). So \( S = \{1, \dots, n\} \): every coordinate of \( \x \) has modulus \( m \), and the Claim gives \( \lvert\lambda - a_{ii}\rvert = r_i(\A) \) for every \( i \).

For the last sentence, suppose \( \lvert\lambda - a_{ii}\rvert < r_i(\A) \) for some \( i \), and put \( \delta = r_i(\A) - \lvert\lambda - a_{ii}\rvert > 0 \). Every \( z \) with \( \lvert z - \lambda\rvert < \delta \) satisfies \( \lvert z - a_{ii}\rvert \le \lvert z - \lambda\rvert + \lvert\lambda - a_{ii}\rvert < r_i(\A) \), so it lies in \( D_i(\A) \) and in the union. Then \( \lambda \) is an interior point of the union, not a boundary point. This proves the theorem.
:::

For \( n = 1 \) the theorem is empty but true: \( r_1 = 0 \) and the only eigenvalue is \( a_{11} \). For the all-ones matrix \( \J \in M_n(\nC) \), \( n \ge 2 \), which is irreducible because every entry is non-zero, every disc is \( \lvert z - 1\rvert \le n - 1 \), and the eigenvalue \( n \), with eigenvector \( \1 \), satisfies \( \lvert n - 1\rvert = n - 1 \): it lies on all of the boundary circles at once, and its eigenvector has equal coordinates, exactly as the theorem predicts.

The corollary is the one \( \K_n \) needed: equality in most rows is allowed, provided one row is strict and the rows are linked.

::: {#cor-irreducibly-dominant-invertible}
[Irreducible Diagonal Dominance Implies Invertibility]

Let \( n \ge 1 \) and let \( \A \in M_n(\nC) \) be **irreducible**, with
\[
\lvert a_{ii}\rvert \ge r_i(\A) \quad\text{for every } i, \qquad \lvert a_{ii}\rvert > r_i(\A) \quad\text{for **at least one** } i .
\]
Then \( \A \) is invertible.
:::

::: {.proof}
Suppose \( \A \) is not invertible. By @thm-eigenvalue-characterizations, \( 0 \) is an eigenvalue. The first hypothesis says \( \lvert 0 - a_{ii}\rvert \ge r_i(\A) \) for every \( i \), so @thm-taussky applies to \( \lambda = 0 \) and gives \( \lvert a_{ii}\rvert = r_i(\A) \) for every \( i \). This contradicts the second hypothesis. Hence \( \A \) is invertible.
:::

Both hypotheses are needed. \( \begin{psmallmatrix} 1 & 1 \\ 1 & 1 \end{psmallmatrix} \) is irreducible and weakly dominant, with no strict row, and it is singular: its eigenvalue \( 0 \) lies on both circles \( \lvert z - 1\rvert = 1 \). Exercise C2 shows that irreducibility cannot be dropped either.

::: {#exm-second-difference-taussky}
[The second-difference matrix]

Show that \( \K_n \) is invertible for every \( n \ge 1 \), and that its eigenvalues lie in the open interval \( (0, 4) \).
:::

::: {.solution}
For \( n = 1 \), \( \K_1 = (2) \), with eigenvalue \( 2 \). Let \( n \ge 2 \). (Chapter 19 §09 proved invertibility by exhibiting the inverse, @prp-second-difference-inverse; here the entries alone suffice.) The only non-zero entries off the diagonal are \( a_{i,i+1} = a_{i+1,i} = -1 \), so \( G(\K_n) \) has the edges \( i \to i + 1 \) and \( i + 1 \to i \), and walking along them reaches every vertex from every vertex. So \( \K_n \) is irreducible by @thm-irreducible-iff-strongly-connected. Its rows have \( r_1 = r_n = 1 < 2 \) and, when \( n \ge 3 \), \( r_i = 2 \) for \( 1 < i < n \). So \( \lvert a_{ii}\rvert \ge r_i \) everywhere, strictly in row \( 1 \), and \( \K_n \) is invertible by @cor-irreducibly-dominant-invertible.

\( \K_n \) is real symmetric, so its eigenvalues are real, and by @thm-gershgorin (a) they lie in \( \bigcup_i[2 - r_i, 2 + r_i] \subseteq [0, 4] \). The value \( 0 \) is excluded by invertibility. The value \( 4 \) satisfies \( \lvert 4 - 2\rvert = 2 \ge r_i \) for every \( i \), so if it were an eigenvalue, @thm-taussky would give \( 2 = r_1 = 1 \), which is false. Hence every eigenvalue lies in \( (0, 4) \). In particular \( \K_n \succ 0 \), which Chapter 19 §09 obtained from its M-matrix structure.
:::

::: {.check}
The all-ones matrix \( \J \in M_3(\nC) \) is irreducible, and \( 0 \) is an eigenvalue of it, since \( \J \) has rank \( 1 \). But \( 0 \) does not lie on the circle \( \lvert z - 1\rvert = 2 \). Does this contradict @thm-taussky?
:::

::: {.solution}
No. The theorem applies only to an eigenvalue with \( \lvert\lambda - a_{ii}\rvert \ge r_i(\J) \) for every \( i \), and \( \lvert 0 - 1\rvert = 1 < 2 = r_i(\J) \): the eigenvalue \( 0 \) lies inside every open disc, so the hypothesis fails and the theorem says nothing about it. The other eigenvalue, \( 3 \), satisfies \( \lvert 3 - 1\rvert = 2 \), and it does lie on every circle.
:::

The picture to take away is this. The union of the discs holds the spectrum. An eigenvalue sits in the disc of the row where its eigenvector peaks. Scaling moves radius from one disc to another. And for an irreducible matrix, an eigenvalue can reach the outer edge of the union only by reaching the edge of every disc at once. §02 replaces the discs by other regions built from the same entries, and §03 counts the eigenvalues inside a group of discs.

## Exercises

### A. Check your understanding

:::: {#exr-gershgorin-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the Gershgorin radius \( r_i(\A) \) and the disc \( D_i(\A) \), and state @thm-gershgorin, including the statement about the peak coordinate of an eigenvector.
2. True or false: every Gershgorin disc of \( \A \) contains an eigenvalue of \( \A \). Justify your answer.
3. True or false: every eigenvalue of \( \A \) lies in \( \bigcup_i\bigl(D_i(\A) \cap D_i(\A\tp)\bigr) \). Justify your answer.
4. True or false: an invertible matrix is strictly diagonally dominant by rows or by columns. Justify your answer.
5. True or false: an irreducible matrix with \( \lvert a_{ii}\rvert \ge r_i(\A) \) for every \( i \) is invertible. Justify your answer.
6. Name the method of proof of @thm-gershgorin in one line.
:::
::::

::: {.solution}
(a) \( r_i(\A) = \sum_{j \ne i}\lvert a_{ij}\rvert \) and \( D_i(\A) = \{z \in \nC : \lvert z - a_{ii}\rvert \le r_i(\A)\} \). If \( \A\x = \lambda\x \) with \( \x \ne \0 \) and \( \lvert x_k\rvert = \max_j\lvert x_j\rvert \), then \( \lambda \in D_k(\A) \); hence every eigenvalue lies in \( \bigcup_i D_i(\A) \), in \( \bigcup_i D_i(\A\tp) \), and in the intersection of these two unions.

(b) False. For \( \begin{psmallmatrix} 0 & 1 \\ 4 & 0 \end{psmallmatrix} \) the eigenvalues are \( \pm 2 \) and the first disc is \( \lvert z\rvert \le 1 \).

(c) False. For the same matrix both intersections are \( \lvert z\rvert \le 1 \), which misses \( \pm 2 \).

(d) False. \( \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix} \) is invertible, and \( \lvert a_{11}\rvert = 0 < 1 \) both for rows and for columns.

(e) False. \( \begin{psmallmatrix} 1 & 1 \\ 1 & 1 \end{psmallmatrix} \) is irreducible, with \( \lvert a_{ii}\rvert = 1 = r_i \), and singular. @cor-irreducibly-dominant-invertible needs one strict row.

(f) Choose the coordinate of the eigenvector of largest modulus, and apply the triangle inequality (@thm-complex-triangle-inequality) to that row of \( \A\x = \lambda\x \).
:::

### B. Practice

:::: {#exr-gershgorin-b1}
[B1: Deciding invertibility]

Determine which of the following matrices are invertible. Justify your answers, using the results of this section where they apply and a direct computation where they do not.

::: {.enumerate options="label=(\alph*)"}
1. \( \begin{pmatrix} 5 & 2 & -2 \\ 1 & -4 & 2 \\ 0 & 3 & 4i \end{pmatrix} \)
2. \( \begin{pmatrix} 3 & 1 & 2 \\ 1 & 3 & 1 \\ 1 & 1 & 3 \end{pmatrix} \)
3. \( \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix} \)
4. \( \begin{pmatrix} 1 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 1 & 2 \end{pmatrix} \)
:::
::::

::: {.solution}
(a) The radii are \( 4, 3, 3 \) and the diagonal moduli \( 5, 4, \lvert 4i\rvert = 4 \), so every row is strictly dominant. The matrix is invertible by @cor-diagonally-dominant-invertible.

(b) Row \( 1 \) has \( 3 = 1 + 2 \), and rows \( 2 \) and \( 3 \) have \( 3 > 2 \). Every off-diagonal entry is non-zero, so every edge \( j \to i \) with \( i \ne j \) is present in the graph, which is strongly connected, and the matrix is irreducible (@thm-irreducible-iff-strongly-connected). It is invertible by @cor-irreducibly-dominant-invertible. (Indeed its determinant is \( 18 \).)

(c) Every row has \( 2 = 1 + 1 \): no row is strict, so neither corollary applies. Directly, the matrix is \( \I + \J \), and \( \J\1 = 3\cdot\1 \), while \( \J\v = \0 \) for \( \v = (1, -1, 0) \) and \( \v = (1, 0, -1) \). So the eigenvalues of \( \I + \J \) are \( 4, 1, 1 \), none zero, and the matrix is invertible, with determinant \( 4 \). The corollaries give sufficient conditions only.

(d) Rows \( 1 \) and \( 2 \) have equality and row \( 3 \) is strict, but the matrix is singular: its first two rows are equal. The corollary does not apply because the matrix is reducible: column \( 3 \) is zero outside row \( 3 \), so no edge leaves vertex \( 3 \), and there is no walk from \( 3 \) to \( 1 \).
:::

:::: {#exr-gershgorin-b2}
[B2: An interval for a symmetric matrix]

Let \( \A = \begin{pmatrix} 5 & 1 & -1 \\ 1 & 3 & 1 \\ -1 & 1 & 6 \end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Use @thm-gershgorin to find an interval containing every eigenvalue of \( \A \), and compare it with the interval \( [-\norm{\A}_{\infty}, \norm{\A}_{\infty}] \) given by @cor-spectral-radius-row-column-bound.
2. Hence show that \( \A \) is positive definite, and that \( \det\A \) lies between \( 1 \) and \( 8^3 \).
:::
::::

::: {.solution}
(a) \( \A \) is real symmetric, so its eigenvalues are real. The radii are \( 2, 2, 2 \), so the discs meet \( \nR \) in \( [3, 7] \), \( [1, 5] \), \( [4, 8] \), whose union is \( [1, 8] \). By @thm-gershgorin (a), every eigenvalue lies in \( [1, 8] \). The largest absolute row sum is \( \norm{\A}_{\infty} = 8 \), so Chapter 16's bound gives only \( [-8, 8] \); the upper ends agree, but only the discs see that the eigenvalues are positive.

(b) Every eigenvalue is at least \( 1 > 0 \), so \( \A \succ 0 \) by @thm-pd-characterizations. The determinant is the product of the three eigenvalues, each in \( [1, 8] \), so \( 1 \le \det\A \le 8^3 = 512 \). (In fact \( \det\A = 74 \).)
:::

:::: {#exr-gershgorin-b3}
[B3: Choosing the scaling]

Let \( \A = \begin{pmatrix} 7 & 4 & 4 \\ 1 & 0 & -1 \\ -1 & -2 & -1 \end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Show that the row disc \( D_1(\A) \) meets the other two row discs.
2. For \( \D = \diag(d, 1, 1) \) with \( d > 0 \), find the scaled radii, and find all \( d \) for which the first scaled disc is disjoint from the other two.
3. Check that \( (-6, -1, 1) \) is an eigenvector of \( \A \), and that its eigenvalue lies in the first scaled disc for \( d = 3 \).
:::
::::

::: {.solution}
(a) The discs are \( \lvert z - 7\rvert \le 8 \), \( \lvert z\rvert \le 2 \) and \( \lvert z + 1\rvert \le 3 \). The point \( 0 \) lies in the first two, and \( -1 \) in the first and third.

(b) By @prp-gershgorin-scaling (b), the radii of \( \D^{-1}\A\D \) are \( r_1 = 8/d \), \( r_2 = 1\cdot d + 1 = d + 1 \) and \( r_3 = 1\cdot d + 2 = d + 2 \), with centers \( 7, 0, -1 \). The first disc misses the second when \( 8/d + d + 1 < 7 \), and misses the third when \( 8/d + d + 2 < 8 \): both say \( d + 8/d < 6 \). Multiplying by \( d > 0 \), this is \( d^2 - 6d + 8 < 0 \), that is, \( (d - 2)(d - 4) < 0 \), so \( 2 < d < 4 \). At \( d = 2 \) the discs touch.

(c) Here
\[
\begin{aligned}
\A(-6, -1, 1) &= (-42 - 4 + 4,\ -6 + 0 - 1,\ 6 + 2 - 1) \\
&= (-42, -7, 7) = 7\,(-6, -1, 1) ,
\end{aligned}
\]
so \( 7 \) is an eigenvalue. For \( d = 3 \) the first scaled disc is \( \lvert z - 7\rvert \le \tfrac83 \), which contains \( 7 \). The eigenvector peaks at the first coordinate, so @thm-gershgorin already placed \( 7 \) in \( D_1 \); the scaled theorem places it in the smaller disc.
:::

### C. Going deeper

:::: {#exr-gershgorin-c1}
[C1: Dominance and definiteness]

::: {.enumerate options="label=(\alph*)"}
1. Prove that a Hermitian matrix \( \A \) with \( a_{ii} > r_i(\A) \) for every \( i \) is positive definite.
2. Prove that a Hermitian **irreducible** matrix with \( a_{ii} \ge r_i(\A) \) for every \( i \), strictly for at least one \( i \), is positive definite.
3. Deduce that for every \( n \ge 1 \) and every real \( t \ge 0 \), the matrix \( \K_n + t\,\e_1\e_1\tp \) is positive definite.
:::

*Hint for (b): apply (a)'s argument to find where the eigenvalues can be, and then use @thm-taussky.*
::::

::: {.solution}
(a) The diagonal entries of a Hermitian matrix are real, and so are its eigenvalues (@thm-self-adjoint-real-eigenvalues). By @thm-gershgorin (a), each eigenvalue \( \lambda \) lies in some \( D_k(\A) \), so \( \lambda \ge a_{kk} - \lvert\lambda - a_{kk}\rvert \ge a_{kk} - r_k(\A) > 0 \). A Hermitian matrix with only positive eigenvalues is positive definite (@thm-pd-characterizations).

(b) As in (a), every eigenvalue satisfies \( \lambda \ge a_{kk} - r_k(\A) \ge 0 \) for some \( k \), so it is enough to show that \( 0 \) is not an eigenvalue. The hypothesis gives \( \lvert 0 - a_{ii}\rvert = a_{ii} \ge r_i(\A) \) for every \( i \), since \( a_{ii} \ge r_i(\A) \ge 0 \). If \( 0 \) were an eigenvalue, @thm-taussky would give \( a_{ii} = r_i(\A) \) for every \( i \), contradicting the strict row. Hence all eigenvalues are positive and \( \A \succ 0 \). (This is also @cor-irreducibly-dominant-invertible, together with the sign information from (a).)

(c) The matrix is real symmetric, and it differs from \( \K_n \) only in the \( (1,1) \) entry, which is \( 2 + t \). The graph is unchanged, so for \( n \ge 2 \) it is irreducible, as shown in @exm-second-difference-taussky. Its rows satisfy \( a_{ii} \ge r_i \), with \( 2 + t > 1 \) in row \( 1 \). By (b), it is positive definite. For \( n = 1 \) the matrix is \( (2 + t) \) with \( 2 + t > 0 \).
:::

:::: {#exr-gershgorin-c2}
[C2: Irreducibility cannot be dropped]

::: {.enumerate options="label=(\alph*)"}
1. Give a \( 3 \times 3 \) reducible matrix with \( \lvert a_{ii}\rvert \ge r_i(\A) \) for every \( i \), strictly in at least one row, that is singular. Which step of the proof of @thm-taussky fails for it?
2. Let \( \A \) be irreducible and let \( \lambda \) be an eigenvalue with \( \lvert\lambda - a_{ii}\rvert \ge r_i(\A) \) for every \( i \). Prove that the eigenspace \( E_\lambda(\A) \) has dimension \( 1 \).
:::

*Hint for (b): given two independent eigenvectors, form a combination with a zero coordinate.*
::::

::: {.solution}
(a) Take \( \A = \begin{psmallmatrix} 1 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 1 & 2 \end{psmallmatrix} \) from @exr-gershgorin-b1 (d): rows \( 1 \) and \( 2 \) have equality, row \( 3 \) is strict, and the first two rows are equal, so \( \A \) is singular. The eigenvector \( \x = (1, -1, \tfrac12) \) for \( 0 \) has \( \A\x = (0, 0, -1 + 1) = \0 \). Its peak set is \( S = \{1, 2\} \), and the Claim of the proof holds: the rows in \( S \) have equality and their off-diagonal non-zero entries point into \( S \). What fails is the spreading step. There is no walk from \( 3 \) to \( 1 \) in \( G(\A) \), so nothing forces \( 3 \in S \), and the strict row \( 3 \) is never reached.

(b) Suppose \( \x \) and \( \y \) are linearly independent eigenvectors for \( \lambda \). Since \( \y \ne \0 \), choose \( i \) with \( y_i \ne 0 \), and put \( \z = \x - (x_i/y_i)\y \). Then \( \z \ne \0 \), by independence, and \( \A\z = \lambda\z \), so \( \z \) is an eigenvector for \( \lambda \) with \( z_i = 0 \). But by @thm-taussky every eigenvector for \( \lambda \) has all coordinates of the same modulus, which is positive because the vector is non-zero. This contradiction shows \( \dim E_\lambda(\A) \le 1 \), and \( \dim E_\lambda(\A) \ge 1 \) because \( \lambda \) is an eigenvalue.
:::
