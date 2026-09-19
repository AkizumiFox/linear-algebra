# M-Matrices

Every section of this chapter so far has studied a non-negative matrix \( \B \) through its spectral radius. This last section looks at the matrices \( s\I - \B \) built from one, which turn up wherever a quantity is balanced against what flows into it from its neighbors: a discretized differential equation, an economy that consumes part of its own output, the fundamental matrix of an absorbing Markov chain. The question is always the same. When is \( s\I - \B \) invertible with a **non-negative** inverse, so that a non-negative right-hand side is guaranteed a non-negative solution? The answer is a single inequality, \( s > \rho(\B) \), and the section's main theorem shows that six other conditions, several of which can be checked by hand, say the same thing. The chapter's summary closes the section.

Throughout, matrices have real entries, the spectrum \( \spec(\A) \) of \( \A \in M_n(\nR) \) is taken in \( \nC \), as in the definition of the spectral radius (@def-spectral-radius), and \( \ge \), \( > \) between matrices or vectors are entrywise.

## Z-matrices and M-matrices

A matrix of the form \( s\I - \B \) with \( \B \ge 0 \) has an unmistakable sign pattern: the diagonal entries \( s - b_{ii} \) can be anything, and every entry off the diagonal is \( -b_{ij} \le 0 \). The pattern comes first, because it is what one sees on the page.

::: {#def-z-matrix}
[Z-Matrix]

A matrix \( \A = (a_{ij}) \in M_n(\nR) \), \( n \ge 1 \), is a **Z-matrix** if \( a_{ij} \le 0 \) for **every** pair \( i \ne j \).
:::

The diagonal is unrestricted. The identity is a Z-matrix, and so is \( -\I \); every \( 1 \times 1 \) matrix is one, since there is no off-diagonal entry to check. The matrix \( \begin{psmallmatrix} 2 & -1 \\ -1 & 2 \end{psmallmatrix} \) is one; \( \begin{psmallmatrix} 2 & 1 \\ -1 & 2 \end{psmallmatrix} \) is not, because of the single entry \( a_{12} = 1 > 0 \).

::: {#lem-z-matrix-as-shift}
[Z-Matrices Are Shifts of Non-negative Matrices]

A matrix \( \A \in M_n(\nR) \) is a Z-matrix if and only if \( \A = s\I - \B \) for some real \( s \) and some \( \B \in M_n(\nR) \) with \( \B \ge 0 \). For a Z-matrix, **every** \( s \ge \max_i a_{ii} \) gives such a representation, with \( \B = s\I - \A \).
:::

::: {.proof}
If \( \A = s\I - \B \) with \( \B \ge 0 \), then \( a_{ij} = -b_{ij} \le 0 \) for \( i \ne j \). Conversely, let \( \A \) be a Z-matrix, let \( s \ge \max_i a_{ii} \) and put \( \B = s\I - \A \). Its diagonal entries are \( s - a_{ii} \ge 0 \) by the choice of \( s \), and its off-diagonal entries are \( -a_{ij} \ge 0 \) because \( \A \) is a Z-matrix. So \( \B \ge 0 \) and \( \A = s\I - \B \).
:::

The representation is far from unique: raising \( s \) by \( t \) raises every diagonal entry of \( \B \) by \( t \). A definition built on it must therefore not depend on which representation is used, and that is the first thing to check below.

Now the goal. For a Z-matrix \( \A = s\I - \B \) with \( s > 0 \), write \( \A = s(\I - s^{-1}\B) \). If \( \rho(\B) < s \), the Neumann series of Chapter 9 (@thm-neumann-series-spectral) inverts the second factor as \( \sum_k (s^{-1}\B)^k \), a sum of non-negative matrices. So a comparison between \( s \) and \( \rho(\B) \) is exactly what decides whether the inverse is non-negative, and it deserves a name.

*An M-matrix is a non-negative matrix subtracted from a multiple of the identity large enough to dominate its spectral radius.*

::: {#def-m-matrix}
[M-Matrix]

A matrix \( \A \in M_n(\nR) \), \( n \ge 1 \), is an **M-matrix** if it can be written as
\[
\A = s\I - \B \qquad \text{with } s \in \nR,\ \B \in M_n(\nR),\ \B \ge 0 \text{ and } s \ge \rho(\B) .
\]
An M-matrix that is **invertible** is a **non-singular M-matrix**.
:::

In words: the first clause asks that \( \A \) be a Z-matrix (by @lem-z-matrix-as-shift, that is what "\( s\I - \B \) with \( \B \ge 0 \)" means), and the second asks that the shift \( s \) be **at least** the spectral radius of what is subtracted. The definition says "can be written", so a single good representation suffices. The next lemma shows that one representation is as good as any other, and also identifies the singular case.

::: {#lem-smallest-real-eigenvalue-z-matrix}
[The Smallest Real Eigenvalue of a Z-Matrix]

Let \( \A \in M_n(\nR) \) be a Z-matrix, and let \( \A = s\I - \B \) with \( \B \ge 0 \) be **any** representation as in @lem-z-matrix-as-shift.

::: {.enumerate options="label=(\alph*)"}
1. \( s - \rho(\B) \) is an eigenvalue of \( \A \), and every \( \lambda \in \spec(\A) \) satisfies \( \operatorname{Re}\lambda \ge s - \rho(\B) \). In particular \( s - \rho(\B) \) is the **smallest real eigenvalue** of \( \A \), and so it is the same number for every representation.
2. \( \A \) is an M-matrix if and only if \( s \ge \rho(\B) \), and a non-singular M-matrix if and only if \( s > \rho(\B) \).
:::
:::

::: {.idea}
Shifting by \( s\I \) moves the spectrum rigidly: the eigenvalues of \( \A \) are \( s - \mu \) for the eigenvalues \( \mu \) of \( \B \). All of those \( \mu \) lie in the disc of radius \( \rho(\B) \), and the point of that disc farthest to the right, \( \rho(\B) \) itself, is an eigenvalue because \( \B \ge 0 \). Reflected through \( s \), that point becomes the leftmost point of the spectrum of \( \A \), and it is real.
:::

::: {.proof}
(a) For \( \v \in \nC^n \) and \( \lambda \in \nC \), \( \A\v = \lambda\v \) if and only if \( \B\v = (s - \lambda)\v \). Hence \( \spec(\A) = \{s - \mu : \mu \in \spec(\B)\} \). By @thm-nonnegative-rho-eigenvalue, \( \rho(\B) \in \spec(\B) \), so \( s - \rho(\B) \in \spec(\A) \). Now let \( \lambda \in \spec(\A) \) and put \( \mu = s - \lambda \in \spec(\B) \). By @def-spectral-radius, \( \lvert\mu\rvert \le \rho(\B) \), so
\[
\operatorname{Re}\lambda = s - \operatorname{Re}\mu \ge s - \lvert\mu\rvert \ge s - \rho(\B) .
\]
For real \( \lambda \) this reads \( \lambda \ge s - \rho(\B) \). So \( s - \rho(\B) \) is the smallest real eigenvalue of \( \A \), a number determined by \( \A \) alone.

(b) If \( s \ge \rho(\B) \), then \( \A \) is an M-matrix by @def-m-matrix. Conversely, if \( \A \) is an M-matrix, there is a representation \( \A = s'\I - \B' \) with \( \B' \ge 0 \) and \( s' \ge \rho(\B') \), and by (a) \( s - \rho(\B) = s' - \rho(\B') \ge 0 \). For the second statement, \( \A \) is invertible if and only if \( 0 \notin \spec(\A) \) (@thm-invertible-tfae-eigen). If \( s > \rho(\B) \), every eigenvalue has real part at least \( s - \rho(\B) > 0 \) by (a), so \( 0 \notin \spec(\A) \). If \( s = \rho(\B) \), then \( 0 = s - \rho(\B) \in \spec(\A) \) by (a), and \( \A \) is singular. This proves the lemma.
:::

So the M-matrix test can be run with the most convenient representation, usually the smallest admissible shift \( s = \max_i a_{ii} \), and the verdict does not change.

**Examples.**

- *Size one.* The \( 1 \times 1 \) matrix \( (a) \) is \( s - (s - a) \) for any \( s \ge a \), and \( \rho(s - a) = s - a \). So \( (a) \) is an M-matrix exactly when \( s \ge s - a \), that is, \( a \ge 0 \), and non-singular exactly when \( a > 0 \). This degenerate case is worth keeping in mind: an M-matrix is the matrix version of a **non-negative number**, and a non-singular one the version of a **positive number**, whose reciprocal is again positive.
- *A standard example.* \( \A = \begin{psmallmatrix} 2 & -1 \\ -1 & 2 \end{psmallmatrix} = 2\I - \B \) with \( \B = \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix} \). Here \( p_{\B}(x) = x^2 - 1 \), so \( \spec(\B) = \{1, -1\} \) and \( \rho(\B) = 1 < 2 \). By @lem-smallest-real-eigenvalue-z-matrix, \( \A \) is a non-singular M-matrix, and indeed \( \A^{-1} = \tfrac13\begin{psmallmatrix} 2 & 1 \\ 1 & 2 \end{psmallmatrix} \ge 0 \).

**Non-example by minimal change.** Double the off-diagonal entries of the standard example: \( \A' = \begin{psmallmatrix} 2 & -2 \\ -2 & 2 \end{psmallmatrix} = 2\I - 2\B \), with \( \rho(2\B) = 2 \). It is still a Z-matrix and still has the smallest shift \( s = 2 \), but now \( s = \rho(2\B) \): an M-matrix, and a singular one (\( \A'\1 = \0 \)). Go one step further, to \( \A'' = \begin{psmallmatrix} 1 & -2 \\ -2 & 1 \end{psmallmatrix} = \I - 2\B \). The clause that fails is the comparison of the shift with the spectral radius: here \( s = 1 < 2 = \rho(2\B) \). By @lem-smallest-real-eigenvalue-z-matrix its smallest real eigenvalue is \( 1 - 2 = -1 \), and its inverse, \( -\tfrac13\begin{psmallmatrix} 1 & 2 \\ 2 & 1 \end{psmallmatrix} \), is entrywise negative.

**Why this definition.** Drop the clause \( s \ge \rho(\B) \) and the definition describes every Z-matrix, including \( \A'' \), whose inverse has the wrong sign everywhere; the whole point is lost. Drop the sign pattern instead, and ask only that some shift of \( \A \) have small spectral radius, and the non-negativity of the terms \( (s^{-1}\B)^k \) in the Neumann series disappears with it. The strict inequality \( s > \rho(\B) \) is what the series needs to converge, and the lemma shows that the boundary case \( s = \rho(\B) \) is exactly the singular one, which is why the definition admits it but names the non-singular case separately.

::: {.warning}
**Positive diagonal and non-positive off-diagonal entries do not make an M-matrix.** The matrix \( \A'' = \begin{psmallmatrix} 1 & -2 \\ -2 & 1 \end{psmallmatrix} \) has both, yet \( \det\A'' = -3 < 0 \) and its inverse has no non-negative entry at all. The sign pattern is only half the definition; the size of the off-diagonal entries relative to the diagonal is the other half, and it is measured by \( \rho(\B) \), not entry by entry.
:::

::: {.check}
Is \( \begin{psmallmatrix} 1 & -1 \\ -1 & 1 \end{psmallmatrix} \) an M-matrix? Is it a non-singular one?
:::

::: {.solution}
Take \( s = 1 \) and \( \B = \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix} \ge 0 \), whose spectrum is \( \{1, -1\} \), so \( \rho(\B) = 1 = s \). By @lem-smallest-real-eigenvalue-z-matrix (b) the matrix is an M-matrix but not a non-singular one. Directly: it sends \( \1 \) to \( \0 \).
:::

The payoff of the lemma is already visible: for a Z-matrix, the leftmost point of the spectrum is a real eigenvalue, and being a (non-singular) M-matrix means precisely that this eigenvalue is non-negative (positive). The theorem below turns that into conditions that can be checked without finding any eigenvalue.

## The characterization theorem

Deciding \( s > \rho(\B) \) directly means locating the eigenvalues of \( \B \), which is the one computation we would like to avoid. The theorem gives three kinds of substitute: a certificate (one positive vector), a sign condition on the inverse, and a finite list of determinants. Its proof needs one small observation about certificates.

::: {#lem-test-vector-principal-submatrix}
[Test Vectors Survive Deletion]

Let \( \A \in M_n(\nR) \) be a Z-matrix, and let \( \x \in \nR^n \) satisfy \( \x > \0 \) and \( \A\x > \0 \). Let \( S \subseteq [n] \) be non-empty, let \( \A_{S,S} \) be the principal submatrix on rows and columns \( S \) (@def-submatrix-minor), and let \( \x_S \) be the vector of the entries \( x_j \), \( j \in S \), in increasing order of \( j \). Then \( \A_{S,S} \) is a Z-matrix, \( \x_S > \0 \) and \( \A_{S,S}\x_S > \0 \).
:::


::: {.idea}
Deleting columns throws away only non-positive contributions to each row, so the surviving rows can only get more positive. That is the whole reason principal minors enter the story.
:::

::: {.proof}
The off-diagonal entries of \( \A_{S,S} \) are off-diagonal entries of \( \A \), so they are \( \le 0 \), and \( \x_S > \0 \) because \( \x > \0 \). Let \( i \in S \). The entry of \( \A_{S,S}\x_S \) belonging to \( i \) is
\[
\sum_{j \in S} a_{ij}x_j = (\A\x)_i - \sum_{j \notin S} a_{ij}x_j \ge (\A\x)_i > 0 ,
\]
because each \( j \notin S \) differs from \( i \in S \), so \( a_{ij} \le 0 \), while \( x_j > 0 \); every subtracted term is therefore \( \le 0 \). This proves the lemma.
:::

Write \( \A_k \) for the leading principal submatrix \( \A_{[k],[k]} \), the top-left \( k \times k \) corner, as in Sylvester's criterion (@thm-pd-characterizations).

::: {#thm-m-matrix-characterizations}
[Characterizations of Non-singular M-Matrices]

Let \( \A \in M_n(\nR) \), \( n \ge 1 \), be a Z-matrix. The following are equivalent.

::: {.enumerate options="label=(\alph*)"}
1. \( \A \) is a non-singular M-matrix.
2. \( \A \) is invertible and \( \A^{-1} \ge 0 \).
3. There is \( \x \in \nR^n \) with \( \x > \0 \) and \( \A\x > \0 \).
4. Every eigenvalue of \( \A \) in \( \nC \) has positive real part.
5. Every real eigenvalue of \( \A \) is positive.
6. Every principal minor of \( \A \) is positive: \( \det\A_{S,S} > 0 \) for every non-empty \( S \subseteq [n] \).
7. Every leading principal minor of \( \A \) is positive: \( \det\A_k > 0 \) for \( k = 1, \dots, n \).
:::
:::

::: {.idea}
Three loops, all passing through (a), (b) or (c).

① (a) \( \Rightarrow \) (b) \( \Rightarrow \) (c) \( \Rightarrow \) (a). The Neumann series writes \( \A^{-1} \) as a sum of non-negative matrices. The vector \( \A^{-1}\1 \) is then a certificate for (c). And a certificate \( \x \) bounds \( \rho(\B) \): rescaling the coordinates by \( \x \) turns \( \B\x < s\x \) into "every row sum is less than \( s \)", and Chapter 15 bounds a spectral radius by row sums.

② (a) \( \Rightarrow \) (d) \( \Rightarrow \) (e) \( \Rightarrow \) (a). This is @lem-smallest-real-eigenvalue-z-matrix read three ways.

③ (c) \( \Rightarrow \) (f) \( \Rightarrow \) (g) \( \Rightarrow \) (b). A certificate survives deletion (@lem-test-vector-principal-submatrix), so every principal submatrix has a non-negative inverse by ①, and one cofactor of that inverse compares two nested minors. The way back from (g) is the induction of Sylvester's criterion: peel off the last row and column, and read the sign of every block of the inverse from Chapter 7's block inverse formula.
:::

::: {.proof}
**(a) \( \Rightarrow \) (b).** By @lem-smallest-real-eigenvalue-z-matrix (b), \( \A = s\I - \B \) with \( \B \ge 0 \) and \( s > \rho(\B) \ge 0 \); in particular \( s > 0 \). Put \( \C = s^{-1}\B \ge 0 \). Its eigenvalues are the numbers \( \mu/s \), \( \mu \in \spec(\B) \), so \( \rho(\C) = \rho(\B)/s < 1 \). By @thm-neumann-series-spectral, \( \I - \C \) is invertible and \( (\I - \C)^{-1} = \sum_{k \ge 0}\C^k \). Every partial sum \( \sum_{k=0}^{K}\C^k \) is \( \ge 0 \), since sums and products of non-negative matrices are non-negative; a non-strict inequality survives a limit (the algebra of limits quoted in Chapter 15's introduction), so \( (\I - \C)^{-1} \ge 0 \). Hence \( \A = s(\I - \C) \) is invertible with \( \A^{-1} = s^{-1}(\I - \C)^{-1} \ge 0 \).

**(b) \( \Rightarrow \) (c).** Put \( \x = \A^{-1}\1 \), so that \( \A\x = \1 > \0 \). Each \( x_i = \sum_j (\A^{-1})_{ij} \) is a sum of non-negative numbers, and it is \( 0 \) only if row \( i \) of \( \A^{-1} \) is zero. That cannot happen: row \( i \) of \( \A^{-1}\A = \I \) is \( \e_i\tp \ne \0 \). Hence \( \x > \0 \).

**(c) \( \Rightarrow \) (a).** Let \( \x > \0 \) with \( \A\x > \0 \). Choose \( s \ge \max_i a_{ii} \), so that \( \B = s\I - \A \ge 0 \) by @lem-z-matrix-as-shift. Then \( \B\x = s\x - \A\x \), so \( (\B\x)_i < sx_i \) for every \( i \). Let \( \D = \diag(x_1, \dots, x_n) \), invertible because every \( x_i > 0 \). The matrix \( \D^{-1}\B\D \) has entries \( b_{ij}x_j/x_i \ge 0 \), and its \( i \)-th row sum is \( (\B\x)_i/x_i < s \). By @cor-spectral-radius-row-column-bound, \( \rho(\D^{-1}\B\D) \) is at most the largest of these row sums, so \( \rho(\D^{-1}\B\D) < s \). Similar matrices have the same characteristic polynomial (@thm-charpoly-similarity-invariant), hence the same eigenvalues, so \( \rho(\B) < s \). By @lem-smallest-real-eigenvalue-z-matrix (b), \( \A \) is a non-singular M-matrix.

**(a) \( \Rightarrow \) (d).** Write \( \A = s\I - \B \) with \( \B \ge 0 \) and \( s > \rho(\B) \), by @lem-smallest-real-eigenvalue-z-matrix (b). By part (a) of the same lemma, every \( \lambda \in \spec(\A) \) has \( \operatorname{Re}\lambda \ge s - \rho(\B) > 0 \).

**(d) \( \Rightarrow \) (e).** A real eigenvalue is its own real part.

**(e) \( \Rightarrow \) (a).** Write \( \A = s\I - \B \) with \( \B \ge 0 \) (@lem-z-matrix-as-shift). By @lem-smallest-real-eigenvalue-z-matrix (a), \( s - \rho(\B) \) is a real eigenvalue of \( \A \), so it is positive by (e). Hence \( s > \rho(\B) \), and \( \A \) is a non-singular M-matrix by part (b) of the lemma.

**(c) \( \Rightarrow \) (f).** Let \( \x > \0 \) with \( \A\x > \0 \). We show \( \det\A_{S,S} > 0 \) by induction on \( k = \lvert S\rvert \). If \( k = 1 \), say \( S = \{i\} \), then \( a_{ii}x_i > 0 \) by @lem-test-vector-principal-submatrix, so \( \det\A_{S,S} = a_{ii} > 0 \). Let \( k \ge 2 \), and suppose every principal minor of size \( k - 1 \) is positive. Put \( \N = \A_{S,S} \in M_k(\nR) \). By @lem-test-vector-principal-submatrix, \( \N \) is a Z-matrix satisfying (c), so the implications (c) \( \Rightarrow \) (a) \( \Rightarrow \) (b), already proved for Z-matrices of every size, show that \( \N \) is invertible with \( \N^{-1} \ge 0 \). In particular \( \det\N \ne 0 \) (@thm-det-nonzero-iff-invertible). Deleting the last row and column of \( \N \) leaves \( \A_{S',S'} \), where \( S' \) is \( S \) without its largest element; so the \( (k,k) \) cofactor of \( \N \) is \( \det\A_{S',S'} \), which is positive by the induction hypothesis. By @cor-inverse-formula, \( \N^{-1} = (\det\N)^{-1}\adj\N \), whose \( (k,k) \)-entry is therefore
\[
(\N^{-1})_{kk} = \frac{\det\A_{S',S'}}{\det\N} .
\]
This number is \( \ge 0 \) because \( \N^{-1} \ge 0 \), and non-zero because its numerator is. So it is positive, and \( \det\N = \det\A_{S',S'}/(\N^{-1})_{kk} > 0 \).

**(f) \( \Rightarrow \) (g).** A leading principal minor is the principal minor with \( S = [k] \).

**(g) \( \Rightarrow \) (b).** By induction on \( n \). If \( n = 1 \), then \( \A = (a_{11}) \) with \( a_{11} = \det\A_1 > 0 \), and \( \A^{-1} = (1/a_{11}) \ge 0 \). Let \( n \ge 2 \), and assume the implication for Z-matrices of size \( n - 1 \). Partition
\[
\A = \begin{pmatrix} \A_{n-1} & \b \\ \c\tp & a_{nn} \end{pmatrix}, \qquad \b, \c \in \nR^{n-1} .
\]
The corner \( \A_{n-1} \) is a Z-matrix whose leading principal minors \( \det\A_1, \dots, \det\A_{n-1} \) are positive, so by the induction hypothesis it is invertible with \( \A_{n-1}^{-1} \ge 0 \). The entries of \( \b \) and \( \c \) are off-diagonal entries of \( \A \), so \( \b \le \0 \) and \( \c \le \0 \). By @thm-schur-determinant (a), \( \det\A = \det\A_{n-1}\cdot\sigma \), where \( \sigma = a_{nn} - \c\tp\A_{n-1}^{-1}\b \) is the Schur complement of \( \A_{n-1} \); since \( \det\A > 0 \) and \( \det\A_{n-1} > 0 \), \( \sigma > 0 \). By @thm-block-inverse-formula (a), \( \A \) is invertible and
\[
\A^{-1} = \begin{pmatrix} \A_{n-1}^{-1} + \sigma^{-1}\u\w\tp & -\sigma^{-1}\u \\ -\sigma^{-1}\w\tp & \sigma^{-1} \end{pmatrix},
\qquad \u = \A_{n-1}^{-1}\b,\ \ \w\tp = \c\tp\A_{n-1}^{-1} .
\]
Now \( \u \le \0 \), being a non-negative matrix times a non-positive vector, and likewise \( \w \le \0 \). Hence \( \u\w\tp \ge 0 \), each of its entries being a product of two non-positive numbers, and \( -\sigma^{-1}\u \ge \0 \), \( -\sigma^{-1}\w \ge \0 \), \( \sigma^{-1} > 0 \). Every block of \( \A^{-1} \) is therefore non-negative, so \( \A^{-1} \ge 0 \).

The three loops connect all seven conditions, which proves the theorem.
:::

Each condition has its use. Condition (c) is a **certificate**: to prove that a given Z-matrix is a non-singular M-matrix, exhibit one positive vector and multiply. Condition (g) is a **finite test** of \( n \) determinants, the counterpart for Z-matrices of Sylvester's criterion for Hermitian matrices, and condition (b) is the **payoff**: \( \A\x = \b \) with \( \b \ge \0 \) has exactly one solution, and it is \( \ge \0 \). Condition (d) links the theorem to differential equations: \( -\A \) is stable, so the solutions of \( \x' = -\A\x \) decay (exercise C3).

::: {.remark}
The two determinant conditions need the Z-hypothesis, and they need **strict** positivity. The matrix \( \begin{psmallmatrix} 1 & 2 \\ 0 & 1 \end{psmallmatrix} \) has all three principal minors equal to \( 1 \), but it is not a Z-matrix and its inverse \( \begin{psmallmatrix} 1 & -2 \\ 0 & 1 \end{psmallmatrix} \) has a negative entry. And the Z-matrix \( \begin{psmallmatrix} 0 & -1 \\ 0 & -1 \end{psmallmatrix} \) has leading principal minors \( 0 \) and \( 0 \), both non-negative, but its eigenvalue \( -1 \) shows it is not an M-matrix of any kind (exercise C2).
:::

::: {.remark}
**Stated, not proved.** There is a companion statement for M-matrices that may be singular: *a Z-matrix is an M-matrix if and only if every principal minor is non-negative.* Exercise C2 proves the forward direction by a limiting argument; the converse is not proved in this book and is used nowhere. Longer lists of equivalent conditions exist in the literature; the seven above are the ones proved here.
:::

::: {.warning}
**A non-negative inverse does not make a matrix a Z-matrix, and so does not make it an M-matrix.** Condition (b) characterizes non-singular M-matrices only **among Z-matrices**. Take
\[
\W = \begin{pmatrix} 1 & -1 & 1 \\ 1 & 1 & -1 \\ -1 & 1 & 1 \end{pmatrix},
\qquad
\W^{-1} = \frac12\begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix} \ge 0 .
\]
Multiplying out confirms \( \W\W^{-1} = \I \): for instance row \( 1 \) of \( \W \) against the columns of \( 2\W^{-1} \) gives \( 1 - 0 + 1 = 2 \), \( 1 - 1 + 0 = 0 \) and \( 0 - 1 + 1 = 0 \). The diagonal of \( \W \) is positive, its principal minors are \( 1, 1, 1, 2, 2, 2, 4 \), \( \W\1 = \1 > \0 \), and its eigenvalues \( 1 \) and \( 1 \pm i\sqrt3 \) have positive real parts. So \( \W \) satisfies every one of (b)–(g), yet \( w_{13} = 1 > 0 \): it is not a Z-matrix, and not an M-matrix.
:::

::: {.check}
Let \( \A = \begin{psmallmatrix} a & -b \\ -c & d \end{psmallmatrix} \) with \( b, c \ge 0 \). Use the theorem to write down exactly when \( \A \) is a non-singular M-matrix, and explain why the condition \( d > 0 \) need not be listed.
:::

::: {.solution}
\( \A \) is a Z-matrix, so by (g) it is a non-singular M-matrix if and only if \( a > 0 \) and \( ad - bc > 0 \). Then \( ad > bc \ge 0 \) and \( a > 0 \) force \( d > 0 \); so condition (f), which also asks for \( d > 0 \), adds nothing, as the theorem says it cannot.
:::

A symmetric Z-matrix has one more characterization, because condition (g) is Sylvester's criterion word for word.

::: {#cor-symmetric-m-matrix-positive-definite}
[Symmetric M-Matrices Are Positive Definite]

A symmetric Z-matrix \( \A \in M_n(\nR) \) is a non-singular M-matrix if and only if \( \A \succ 0 \).
:::

::: {.proof}
By @thm-m-matrix-characterizations, \( \A \) is a non-singular M-matrix if and only if \( \det\A_k > 0 \) for every \( k \). By Sylvester's criterion, @thm-pd-characterizations (d), a real symmetric matrix satisfies this if and only if \( \A \succ 0 \).
:::

The Z-hypothesis cannot be dropped here either: \( \begin{psmallmatrix} 2 & 1 \\ 1 & 2 \end{psmallmatrix} \succ 0 \), but its inverse \( \tfrac13\begin{psmallmatrix} 2 & -1 \\ -1 & 2 \end{psmallmatrix} \) has negative entries. Entrywise order and the Loewner order answer different questions, and the corollary is a place where they meet.

## The second-difference matrix

The first application is the one that gave M-matrices their importance. To solve \( -u''(t) = f(t) \) on \( [0, 1] \) with \( u(0) = u(1) = 0 \), choose \( n \), put \( h = 1/(n+1) \) and \( t_i = ih \), and replace \( u(t_i) \) by an unknown \( u_i \) and \( -u''(t_i) \) by the second difference \( (2u_i - u_{i-1} - u_{i+1})/h^2 \), with \( u_0 = u_{n+1} = 0 \). The equations become
\[
\frac{1}{h^2}\K_n\u = \f, \qquad
\K_n = \begin{pmatrix} 2 & -1 & & \\ -1 & 2 & \ddots & \\ & \ddots & \ddots & -1 \\ & & -1 & 2 \end{pmatrix} \in M_n(\nR),
\]
where \( \f = (f(t_1), \dots, f(t_n)) \). Physically \( u \) is the sag of a string under the load \( f \), and a load pushing everywhere in one direction should never make any part of the string move the other way. In matrix language: \( \K_n^{-1} \) should be non-negative.

\( \K_n \) is a Z-matrix, but the obvious certificate fails. Its rows sum to \( 1, 0, \dots, 0, 1 \), so \( \K_n\1 \) has zero entries once \( n \ge 3 \): the matrix is diagonally dominant, but only weakly. The continuous problem suggests a better test vector. The function \( u(t) = t(1 - t) \) solves \( -u'' = 2 \) with zero boundary values, so try its samples, scaled to be integers.

::: {#prp-second-difference-inverse}
[The Second-Difference Matrix]

Let \( n \ge 1 \). Then \( \K_n \) is a non-singular M-matrix, and its inverse is the matrix with entries
\[
(\K_n^{-1})_{ij} = \frac{\min(i,j)\,\bigl(n + 1 - \max(i,j)\bigr)}{n + 1}, \qquad 1 \le i, j \le n .
\]
In particular every entry of \( \K_n^{-1} \) is positive.
:::

::: {.idea}
For the M-matrix property, feed \( \K_n \) the vector \( x_i = i(n + 1 - i) \), a sampled parabola: second differences of a quadratic are constant, so \( \K_n\x = 2\1 \). For the inverse, guess column \( j \) from the continuous picture: the response to a point load at \( t_j \) is a tent, linear on each side of \( j \) and zero at both ends. The second difference of a function that is linear on each side of \( j \) vanishes except at the kink, and there it equals the change in slope.
:::

::: {.proof}
*The certificate.* Put \( x_i = i(n + 1 - i) \) for \( 0 \le i \le n + 1 \), so that \( x_0 = x_{n+1} = 0 \) and \( x_i > 0 \) for \( 1 \le i \le n \). For \( 1 \le i \le n \), the \( i \)-th entry of \( \K_n\x \) is \( 2x_i - x_{i-1} - x_{i+1} \), where the terms \( x_0 \) and \( x_{n+1} \), which do not occur in rows \( 1 \) and \( n \), are zero anyway. Writing \( x_i = (n+1)i - i^2 \), the linear part contributes \( (n+1)(2i - (i - 1) - (i + 1)) = 0 \), and the quadratic part contributes
\[
-2i^2 + (i-1)^2 + (i+1)^2 = 2 .
\]
So \( \K_n\x = 2\1 > \0 \) with \( \x > \0 \), and @thm-m-matrix-characterizations, (c) \( \Rightarrow \) (a), shows that \( \K_n \) is a non-singular M-matrix.

*The inverse.* Let \( \G \) be the matrix given by the formula, fix a column \( j \), and put \( g_i = \min(i,j)(n + 1 - \max(i,j))/(n+1) \) for \( 0 \le i \le n + 1 \). Then
\[
g_i = \begin{cases} i\,\dfrac{n + 1 - j}{n + 1} & (0 \le i \le j), \\ j\,\dfrac{n + 1 - i}{n + 1} & (j \le i \le n + 1), \end{cases}
\]
the two lines agreeing at \( i = j \). So \( g_0 = g_{n+1} = 0 \), and \( (g_i) \) is an affine function of \( i \) on \( 0 \le i \le j \), with slope \( (n+1-j)/(n+1) \), and on \( j \le i \le n+1 \), with slope \( -j/(n+1) \). For \( 1 \le i \le n \), entry \( i \) of \( \K_n \) times column \( j \) of \( \G \) is \( 2g_i - g_{i-1} - g_{i+1} = (g_i - g_{i-1}) - (g_{i+1} - g_i) \). If \( i < j \) or \( i > j \), the three points \( i - 1, i, i + 1 \) lie on one side of \( j \), both differences are the same slope, and the entry is \( 0 \). If \( i = j \), it is
\[
\frac{n + 1 - j}{n + 1} - \Bigl(-\frac{j}{n + 1}\Bigr) = 1 .
\]
Hence \( \K_n\G = \I \), so \( \G = \K_n^{-1} \). Finally \( \min(i,j) \ge 1 \) and \( n + 1 - \max(i,j) \ge 1 \), so every entry is at least \( 1/(n+1) > 0 \).
:::

The matrix \( \K_n^{-1} \) is a **discrete Green's function**: column \( j \) is the sag produced by a unit load at the single point \( t_j \), and positivity of every entry says that a load at one point moves every point of the string, in the same direction. The non-negativity of \( \K_n^{-1} \) is the discrete **maximum principle**: if \( \K_n\u \ge \0 \) then \( \u \ge \0 \). Since \( \K_n \) is symmetric, @cor-symmetric-m-matrix-positive-definite also shows \( \K_n \succ 0 \), which Chapter 6 foreshadowed by computing \( \det\K_n = n + 1 \) in @exr-special-determinants-b2.

::: {#exm-second-difference-four}
[The Case n = 4]

Write down \( \K_4^{-1} \), check one column against \( \K_4 \), and recover the certificate \( \x \) from it.
:::

::: {.solution}
With \( n + 1 = 5 \), @prp-second-difference-inverse gives
\[
\K_4^{-1} = \frac15\begin{pmatrix} 4 & 3 & 2 & 1 \\ 3 & 6 & 4 & 2 \\ 2 & 4 & 6 & 3 \\ 1 & 2 & 3 & 4 \end{pmatrix} .
\]
*Check of column 2.* \( \K_4 \) applied to \( (3, 6, 4, 2) \) gives \( (6 - 6,\ -3 + 12 - 4,\ -6 + 8 - 2,\ -4 + 4) = (0, 5, 0, 0) \), and dividing by \( 5 \) gives \( \e_2 \), as it must. Each column is a tent: column 2 rises by \( 3 \) per step up to row \( 2 \) and then falls by \( 2 \) per step towards the zero at the fictitious row \( 5 \).

*The certificate.* The row sums of \( 5\K_4^{-1} \) are \( 10, 15, 15, 10 \), so \( \K_4^{-1}\1 = (2, 3, 3, 2) \), which is \( \tfrac12(1\cdot4, 2\cdot3, 3\cdot2, 4\cdot1) = \tfrac12\x \). This is the proof of (b) \( \Rightarrow \) (c) run backwards: the vector \( \A^{-1}\1 \) is always a certificate, and here it is the sampled parabola.
:::

## The Leontief input–output model

The second application comes from economics. An economy has \( n \) sectors, each producing one good. To produce one unit of good \( j \), sector \( j \) consumes \( c_{ij} \ge 0 \) units of good \( i \), so column \( j \) of the **consumption matrix** \( \C = (c_{ij}) \ge 0 \) is sector \( j \)'s recipe. A production plan \( \x \ge \0 \) uses up \( \C\x \) as inputs and leaves the net output \( \x - \C\x \) for outside use. Given a final demand \( \d \ge \0 \), the planner needs
\[
(\I - \C)\x = \d, \qquad \x \ge \0 .
\]
The economy is **productive** if this has a solution for **every** \( \d \ge \0 \). The matrix \( \I - \C \) is a Z-matrix, and the theorem answers the question completely.

::: {#cor-leontief-productive}
[Productive Economies]

Let \( \C \in M_n(\nR) \) with \( \C \ge 0 \). The following are equivalent.

::: {.enumerate options="label=(\roman*)"}
1. For every \( \d \ge \0 \) there is \( \x \ge \0 \) with \( (\I - \C)\x = \d \).
2. There is \( \x \ge \0 \) with \( \x - \C\x > \0 \): some plan leaves a surplus of every good.
3. \( \rho(\C) < 1 \).
4. \( \I - \C \) is invertible and \( (\I - \C)^{-1} \ge 0 \).
5. Every leading principal minor of \( \I - \C \) is positive.
:::

When they hold, the solution in (i) is unique, and \( (\I - \C)^{-1} = \I + \C + \C^2 + \cdots \). They hold in particular when every column sum of \( \C \) is less than \( 1 \).
:::


::: {.idea}
The matrix \( \I - \C \) is a Z-matrix, so this is the main theorem read in economic terms: (iii) is (a) with \( s = 1 \); (ii), (iv) and (v) are (c), (b) and (g), where in (ii) a plan \( \x \ge \0 \) with a surplus is automatically positive, since \( \x > \C\x \ge \0 \); and (i) sits between (iv) and (ii).
:::

::: {.proof}
\( \I - \C \) is a Z-matrix with the representation \( s = 1 \), \( \B = \C \), so (iii) says, by @lem-smallest-real-eigenvalue-z-matrix (b), that \( \I - \C \) is a non-singular M-matrix. By @thm-m-matrix-characterizations, (iii) is therefore equivalent to (iv) (condition (b) there) and to (v) (condition (g)). It is also equivalent to (ii): if \( \x \ge \0 \) and \( \x - \C\x > \0 \), then \( \x > \C\x \ge \0 \), so \( \x > \0 \) and condition (c) of the theorem holds; conversely (c) supplies such an \( \x \).

(iv) \( \Rightarrow \) (i): given \( \d \ge \0 \), the vector \( \x = (\I - \C)^{-1}\d \) is a product of non-negative factors, hence \( \ge \0 \), and it solves the system. (i) \( \Rightarrow \) (ii): take \( \d = \1 \).

When they hold, \( \I - \C \) is invertible, so the solution is unique, and \( \rho(\C) < 1 \) gives the series by @thm-neumann-series-spectral. Finally, if every column sum of \( \C \) is less than \( 1 \), then \( \rho(\C) \le \norm{\C}_1 < 1 \) by @cor-spectral-radius-row-column-bound, which is (iii).
:::

Condition (v) is known to economists as the Hawkins–Simon condition, and the series has a direct reading. To deliver \( \d \), the economy must first produce \( \d \); that production consumes \( \C\d \), which must also be produced; that consumes \( \C^2\d \); and so on. The Leontief inverse \( (\I - \C)^{-1} \) adds up all the rounds, and its \( (i, j) \)-entry is the total amount of good \( i \) that the economy must produce, directly and indirectly, to deliver one unit of good \( j \).

::: {#exm-leontief-three-sectors}
[Three Sectors]

An economy has three sectors, agriculture, manufacturing and services, with consumption matrix
\[
\C = \frac15\begin{pmatrix} 1 & 1 & 1 \\ 2 & 0 & 1 \\ 0 & 2 & 1 \end{pmatrix} .
\]
Show that it is productive, find \( \rho(\C) \) exactly, compute the Leontief inverse, and find the production plan meeting the demand \( \d = (12, 6, 6) \).
:::

::: {.solution}
*Productive.* Every column of \( 5\C \) sums to \( 3 \), so every column sum of \( \C \) is \( \tfrac35 < 1 \), and @cor-leontief-productive applies.

*The spectral radius.* Expanding \( \det(x\I - \C) \) along the first row gives
\[
p_{\C}(x) = x^3 - \tfrac25x^2 - \tfrac{3}{25}x = x\bigl(x - \tfrac35\bigr)\bigl(x + \tfrac15\bigr),
\]
so \( \spec(\C) = \{0, \tfrac35, -\tfrac15\} \) and \( \rho(\C) = \tfrac35 \), equal to the column-sum bound \( \norm{\C}_1 \) of @cor-spectral-radius-row-column-bound. The bound is attained because all column sums are equal: \( \C\tp\1 = \tfrac35\1 \).

*The Leontief inverse.* Here \( \I - \C = \tfrac15\begin{psmallmatrix} 4 & -1 & -1 \\ -2 & 5 & -1 \\ 0 & -2 & 4 \end{psmallmatrix} \), and
\[
(\I - \C)^{-1} = \frac16\begin{pmatrix} 9 & 3 & 3 \\ 4 & 8 & 3 \\ 2 & 4 & 9 \end{pmatrix} .
\]
To check, multiply \( \begin{psmallmatrix} 4 & -1 & -1 \\ -2 & 5 & -1 \\ 0 & -2 & 4 \end{psmallmatrix} \) by \( \begin{psmallmatrix} 9 & 3 & 3 \\ 4 & 8 & 3 \\ 2 & 4 & 9 \end{psmallmatrix} \): the first row gives \( 36 - 4 - 2 = 30 \), \( 12 - 8 - 4 = 0 \), \( 12 - 3 - 9 = 0 \); the second \( -18 + 20 - 2 = 0 \), \( -6 + 40 - 4 = 30 \), \( -6 + 15 - 9 = 0 \); the third \( -8 + 8 = 0 \), \( -16 + 16 = 0 \), \( -6 + 36 = 30 \). The product is \( 30\I \), and \( \tfrac15\cdot\tfrac16\cdot 30 = 1 \). Every entry of the inverse is positive: extra demand for any one good raises the output of every sector. For instance, one extra unit of services requires \( \tfrac12 \) unit of agricultural output in total, although services consume only \( \tfrac15 \) unit of it directly.

*The plan.*
\[
\x = (\I - \C)^{-1}\d = \frac16\begin{pmatrix} 108 + 18 + 18 \\ 48 + 48 + 18 \\ 24 + 24 + 54 \end{pmatrix} = \begin{pmatrix} 24 \\ 19 \\ 17 \end{pmatrix} .
\]
Check: \( \C\x = \tfrac15(24 + 19 + 17,\ 48 + 17,\ 38 + 17) = (12, 13, 11) \), and \( \x - \C\x = (12, 6, 6) = \d \). Delivering this demand takes \( 24 \) units of agricultural output, twice the \( 12 \) that leave the economy.
:::

::: {.check}
A two-sector economy has \( \C = \begin{psmallmatrix} 1/2 & 1 \\ 1/2 & 0 \end{psmallmatrix} \). Is it productive?
:::

::: {.solution}
No. The leading principal minors of \( \I - \C = \begin{psmallmatrix} 1/2 & -1 \\ -1/2 & 1 \end{psmallmatrix} \) are \( \tfrac12 \) and \( \tfrac12 - \tfrac12 = 0 \), so (v) of @cor-leontief-productive fails. Indeed \( \C\begin{psmallmatrix} 2 \\ 1 \end{psmallmatrix} = \begin{psmallmatrix} 2 \\ 1 \end{psmallmatrix} \): running the sectors in the ratio \( 2 : 1 \) exactly reproduces its own inputs and leaves nothing over, and \( \rho(\C) = 1 \).
:::

## Summary and transfer

The chapter set out to explain what the sign of the entries alone forces on the spectrum. For a positive matrix the answer is Perron's theorem (§01, Positive matrices and Perron's theorem): the spectral radius is a simple eigenvalue with a positive eigenvector, and it strictly dominates every other eigenvalue in modulus. Irreducibility, a property of the zero pattern read off a directed graph (§02, Irreducibility and graphs), is what keeps most of that conclusion alive when zeros are allowed (§03, The Perron–Frobenius theorem), and without it one still has \( \rho(\B) \) as an eigenvalue with a non-negative eigenvector. From there the chapter drew the long-run behavior of powers (§05, Primitive matrices), Markov chains (§06, Markov chains), the extreme points of the doubly stochastic matrices (§07, Birkhoff's theorem), a ranking of web pages (§08, PageRank), and in this section the matrices \( s\I - \B \). Six moves did the work.

- **Compare entrywise, then take the spectral radius.** Non-negativity makes the spectral radius monotone and lets \( \lvert\A\x\rvert \le \lvert\A\rvert\lvert\x\rvert \) replace cancellation by an inequality (§01, Positive matrices and Perron's theorem). *Transfer:* to bound the spectral radius of a matrix you do not understand, dominate it entrywise by one you do.
- **A positive test vector bounds \( \rho \) from both sides.** The ratios \( (\A\x)_i/x_i \) for a single \( \x > \0 \) trap \( \rho(\A) \) between their minimum and maximum (§04, The Collatz–Wielandt formula), and in this section one \( \x > \0 \) with \( \A\x > \0 \) certified a non-singular M-matrix. The mechanism used here is the rescaling \( \D^{-1}\B\D \) with \( \D = \diag(\x) \), which turns \( \B\x \) into row sums. *Transfer:* guess a positive vector from the structure of the problem, the parabola for \( \K_n \), and verify it by one multiplication.
- **Read the zero pattern as a graph.** Which entries of \( \A^k \) are positive depends only on which entries of \( \A \) are, and that is a question about paths (§02, Irreducibility and graphs; §05, Primitive matrices). *Transfer:* when only signs matter, draw the graph and count paths.
- **Prove it for positive matrices, then reach the boundary.** Perron's theorem is proved where every entry is positive, and the non-negative and irreducible cases are reached from it through positive matrices built from \( \A \) (§03, The Perron–Frobenius theorem). *Transfer:* when a hypothesis is an inequality that may hold with equality, prove the strict case and ask what survives the passage to the boundary; \( s > \rho(\B) \) versus \( s \ge \rho(\B) \) in this section is the same division.
- **Divide by the Perron root, then use Chapter 9.** Once \( \rho(\A) \) is known to be a simple eigenvalue dominating the others, \( \A/\rho(\A) \) meets the hypotheses of the convergence theorems of Chapter 9 §10, and no diagonalizability is ever needed (§05, Primitive matrices; §06, Markov chains). *Transfer:* normalize the dominant eigenvalue to \( 1 \) before asking about limits.
- **Invert with a series of non-negative terms.** If \( \B \ge 0 \) and \( \rho(\B) < 1 \), then \( (\I - \B)^{-1} = \sum_k \B^k \ge 0 \). This is the fundamental matrix of an absorbing chain (§06, Markov chains), the Leontief inverse, and the non-negativity of the inverse of every non-singular M-matrix. *Transfer:* to prove that an inverse is non-negative, or to interpret its entries, expand it as the sum of the rounds of a process.

The chapter also paid promises made in earlier chapters.

| The promise | Made in | Paid by |
|---|---|---|
| "Chapter 18 proves the Perron–Frobenius theorem, which gives the conclusions of @thm-markov-limit-diagonalizable for every stochastic matrix with some power having all entries positive, without assuming diagonalizability and without computing eigenvalues" | Chapter 8 §11 | §06 (Stochastic matrices and Markov chains), resting on §03 (The Perron–Frobenius theorem) and §05 (Primitive matrices and the limit theorem) |
| "We do not prove Birkhoff's theorem here; Chapter 18 does" | Chapter 17 §08, and again in its summary, §11 | §07 (Doubly stochastic matrices and Birkhoff's theorem) |

Some things the chapter did not do. The characterization of possibly singular M-matrices by non-negative principal minors was stated here and proved in one direction only. The theorem of Hardy, Littlewood and Pólya, that \( \x \prec \y \) exactly when \( \x = \D\y \) for a doubly stochastic \( \D \), belongs to Chapter 20. And the power method, the algorithm that computes a Perron vector at the size of the web, belongs to Chapter 23.

## Exercises

### A. Check your understanding

:::: {#exr-m-matrices-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define a Z-matrix and a non-singular M-matrix.
2. True or false: every Z-matrix with positive diagonal entries is a non-singular M-matrix. Justify your answer.
3. True or false: every principal submatrix of a non-singular M-matrix is a non-singular M-matrix. Justify your answer.
4. True or false: if \( \A \) is invertible and \( \A^{-1} \ge 0 \), then \( \A \) is an M-matrix. Justify your answer.
5. True or false: the inverse of a non-singular M-matrix has every entry positive. Justify your answer.
6. Name a vector \( \x > \0 \) with \( \K_n\x > \0 \), and explain why \( \x = \1 \) does not work when \( n \ge 3 \).
:::
::::

::: {.solution}
(a) \( \A \in M_n(\nR) \) is a Z-matrix if \( a_{ij} \le 0 \) for all \( i \ne j \) (@def-z-matrix). It is a non-singular M-matrix if \( \A = s\I - \B \) with \( \B \ge 0 \) and \( s \ge \rho(\B) \), and \( \A \) is invertible; equivalently, \( s > \rho(\B) \) (@def-m-matrix, @lem-smallest-real-eigenvalue-z-matrix (b)).

(b) False. \( \begin{psmallmatrix} 1 & -2 \\ -2 & 1 \end{psmallmatrix} \) is a Z-matrix with positive diagonal, but its determinant is \( 1 - 4 = -3 \), so condition (g) of @thm-m-matrix-characterizations fails.

(c) True. Let \( \A \) be a non-singular M-matrix. By @thm-m-matrix-characterizations there is \( \x > \0 \) with \( \A\x > \0 \). By @lem-test-vector-principal-submatrix, \( \A_{S,S} \) is a Z-matrix with \( \A_{S,S}\x_S > \0 \) and \( \x_S > \0 \), so it is a non-singular M-matrix by (c) \( \Rightarrow \) (a) of the theorem.

(d) False. The swap \( \P = \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix} \) satisfies \( \P^{-1} = \P \ge 0 \), but \( p_{12} = 1 > 0 \), so \( \P \) is not a Z-matrix, and every M-matrix is one.

(e) False. \( \I_2 \) is a non-singular M-matrix, and \( \I_2^{-1} = \I_2 \) has zero off-diagonal entries.

(f) \( x_i = i(n + 1 - i) \), for which \( \K_n\x = 2\1 \) (@prp-second-difference-inverse). For \( \x = \1 \), row \( i \) of \( \K_n\1 \) is \( 2 - 1 - 1 = 0 \) for every \( 2 \le i \le n - 1 \), and such rows exist when \( n \ge 3 \).
:::

### B. Practice

:::: {#exr-m-matrices-b1}
[B1: Which are non-singular M-matrices?]

Determine which of the following are non-singular M-matrices. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \begin{pmatrix} 3 & -1 & -1 \\ -1 & 3 & -1 \\ -1 & -1 & 3 \end{pmatrix} \)
2. \( \begin{pmatrix} 1 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{pmatrix} \)
3. \( \begin{pmatrix} 2 & -3 \\ -1 & 2 \end{pmatrix} \)
4. \( \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \)
5. \( \begin{pmatrix} 1 & -2 & 0 \\ 0 & 1 & -2 \\ -2 & 0 & 1 \end{pmatrix} \)
:::
::::

::: {.solution}
(a) Yes. It is a Z-matrix, and every row sums to \( 1 \), so \( \x = \1 > \0 \) gives \( \A\x = \1 > \0 \). By @thm-m-matrix-characterizations, (c) \( \Rightarrow \) (a), it is a non-singular M-matrix. (Its inverse is \( \tfrac14\begin{psmallmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{psmallmatrix} \ge 0 \), as (b) predicts.)

(b) No. Every row sums to \( 0 \), so \( \A\1 = \0 \) and \( \A \) is singular. (It is a singular M-matrix: with \( s = 2 \), \( \B = 2\I - \A \) has every row sum equal to \( 2 \), so \( \rho(\B) \le 2 \) by @cor-spectral-radius-row-column-bound, while \( \B\1 = 2\1 \) gives \( \rho(\B) \ge 2 \).)

(c) Yes. It is a Z-matrix with leading principal minors \( 2 > 0 \) and \( 4 - 3 = 1 > 0 \), so (g) \( \Rightarrow \) (a) applies. Check: \( \A^{-1} = \begin{psmallmatrix} 2 & 3 \\ 1 & 2 \end{psmallmatrix} \ge 0 \).

(d) No. The off-diagonal entries are \( 1 > 0 \), so it is not a Z-matrix. (It is positive definite, and its inverse \( \tfrac13\begin{psmallmatrix} 2 & -1 \\ -1 & 2 \end{psmallmatrix} \) has negative entries.)

(e) No. It is a Z-matrix, but expanding along the first row,
\[
\det\A = 1\cdot(1 - 0) - (-2)\cdot(0 - 4) + 0 = 1 - 8 = -7 < 0 ,
\]
so condition (f) of @thm-m-matrix-characterizations fails.
:::

:::: {#exr-m-matrices-b2}
[B2: A string with a free end]

Let
\[
\A = \begin{pmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{pmatrix} .
\]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \A\1 \) is not positive, and find \( \x > \0 \) with \( \A\x > \0 \).
2. Compute the leading principal minors of \( \A \), and check that they agree with (a).
3. Compute \( \A^{-1} \) and check that \( \A^{-1} \ge 0 \). Hence solve \( \A\u = \e_3 \), and say why the answer had to be non-negative.
:::

*Hint: try an increasing \( \x \) whose increments decrease.*
::::

::: {.solution}
(a) \( \A\1 = (1, 0, 0) \), which is not positive. Take \( \x = (3, 5, 6) \): then \( \A\x = (6 - 5,\ -3 + 10 - 6,\ -5 + 6) = (1, 1, 1) > \0 \). Since \( \A \) is a Z-matrix, it is a non-singular M-matrix by @thm-m-matrix-characterizations, (c) \( \Rightarrow \) (a).

(b) \( \det\A_1 = 2 \), \( \det\A_2 = 4 - 1 = 3 \), and, expanding along the first row, \( \det\A = 2(2 - 1) - (-1)(-1 - 0) = 2 - 1 = 1 \). All three are positive, which is condition (g), as (a) and the theorem require.

(c)
\[
\A^{-1} = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 2 \\ 1 & 2 & 3 \end{pmatrix},
\]
the matrix with entries \( \min(i, j) \). Check: row 1 of \( \A \) against the columns gives \( 2 - 1 = 1 \), \( 2 - 2 = 0 \), \( 2 - 2 = 0 \); row 2 gives \( -1 + 2 - 1 = 0 \), \( -1 + 4 - 2 = 1 \), \( -1 + 4 - 3 = 0 \); row 3 gives \( -1 + 1 = 0 \), \( -2 + 2 = 0 \), \( -2 + 3 = 1 \). So \( \A\A^{-1} = \I \), and \( \A^{-1} \ge 0 \). Hence \( \u = \A^{-1}\e_3 = (1, 2, 3) \). It had to be \( \ge \0 \) because \( \e_3 \ge \0 \) and \( \A^{-1} \ge 0 \). Note that \( \A^{-1}\1 = (3, 5, 6) \) is the certificate of (a).
:::

:::: {#exr-m-matrices-b3}
[B3: A two-sector economy]

Let
\[
\C = \begin{pmatrix} 1/5 & 2/5 \\ 3/10 & 1/10 \end{pmatrix} .
\]

::: {.enumerate options="label=(\alph*)"}
1. Show that the economy with consumption matrix \( \C \) is productive.
2. Compute the Leontief inverse \( (\I - \C)^{-1} \).
3. Find the production plan meeting the demand \( \d = (30, 60) \), and check it.
4. Find \( \rho(\C) \) exactly.
:::
::::

::: {.solution}
(a) The column sums are \( \tfrac15 + \tfrac{3}{10} = \tfrac12 \) and \( \tfrac25 + \tfrac{1}{10} = \tfrac12 \), both less than \( 1 \), so the economy is productive by @cor-leontief-productive.

(b) \( \I - \C = \begin{psmallmatrix} 4/5 & -2/5 \\ -3/10 & 9/10 \end{psmallmatrix} \), with determinant \( \tfrac{36}{50} - \tfrac{6}{50} = \tfrac35 \). By @thm-two-by-two-inverse,
\[
(\I - \C)^{-1} = \frac53\begin{pmatrix} 9/10 & 2/5 \\ 3/10 & 4/5 \end{pmatrix} = \begin{pmatrix} 3/2 & 2/3 \\ 1/2 & 4/3 \end{pmatrix} \ge 0 .
\]

(c) \( \x = (\tfrac32\cdot30 + \tfrac23\cdot60,\ \tfrac12\cdot30 + \tfrac43\cdot60) = (85, 95) \). Check: \( \C\x = (17 + 38,\ \tfrac{51}{2} + \tfrac{19}{2}) = (55, 35) \), and \( \x - \C\x = (30, 60) \).

(d) \( p_{\C}(x) = x^2 - \tfrac{3}{10}x + \bigl(\tfrac{1}{50} - \tfrac{12}{100}\bigr) = x^2 - \tfrac{3}{10}x - \tfrac{1}{10} = (x - \tfrac12)(x + \tfrac15) \). So \( \spec(\C) = \{\tfrac12, -\tfrac15\} \) and \( \rho(\C) = \tfrac12 \). Here the column-sum bound \( \norm{\C}_1 = \tfrac12 \) is attained, as it must be when all column sums are equal.
:::

### C. Going deeper

:::: {#exr-m-matrices-c1}
[C1: Raising the diagonal]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \A \) be a non-singular M-matrix and \( \M \) a Z-matrix of the same size with \( \M \ge \A \) entrywise. Prove that \( \M \) is a non-singular M-matrix and that \( 0 \le \M^{-1} \le \A^{-1} \).
2. Deduce that for every diagonal \( \D \ge 0 \), \( \K_n + \D \) is a non-singular M-matrix with \( (\K_n + \D)^{-1} \le \K_n^{-1} \). Check this for \( n = 2 \) and \( \D = \diag(1, 0) \).
:::

*Hint: for the inequality, factor \( \A^{-1} - \M^{-1} \).*
::::

::: {.solution}
(a) By @thm-m-matrix-characterizations there is \( \x > \0 \) with \( \A\x > \0 \). Since \( \M - \A \ge 0 \) and \( \x > \0 \), \( (\M - \A)\x \ge \0 \), so \( \M\x = \A\x + (\M - \A)\x > \0 \). As \( \M \) is a Z-matrix, (c) \( \Rightarrow \) (a) of the theorem makes it a non-singular M-matrix, and (a) \( \Rightarrow \) (b) gives \( \M^{-1} \ge 0 \). Next,
\[
\A^{-1} - \M^{-1} = \A^{-1}\M\M^{-1} - \A^{-1}\A\M^{-1} = \A^{-1}(\M - \A)\M^{-1} ,
\]
a product of three non-negative matrices, hence \( \ge 0 \). This proves \( 0 \le \M^{-1} \le \A^{-1} \).

(b) \( \K_n \) is a non-singular M-matrix by @prp-second-difference-inverse, and \( \K_n + \D \) is a Z-matrix with \( \K_n + \D \ge \K_n \), since \( \D \) only changes the diagonal and does so upwards. Part (a) gives the claim. For \( n = 2 \): \( \K_2^{-1} = \tfrac13\begin{psmallmatrix} 2 & 1 \\ 1 & 2 \end{psmallmatrix} \), and \( \K_2 + \D = \begin{psmallmatrix} 3 & -1 \\ -1 & 2 \end{psmallmatrix} \) has determinant \( 5 \) and inverse \( \tfrac15\begin{psmallmatrix} 2 & 1 \\ 1 & 3 \end{psmallmatrix} \). The difference is
\[
\frac13\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} - \frac15\begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} = \frac{1}{15}\begin{pmatrix} 4 & 2 \\ 2 & 1 \end{pmatrix} \ge 0 .
\]

:::

:::: {#exr-m-matrices-c2}
[C2: The singular case]

::: {.enumerate options="label=(\alph*)"}
1. Show that the Z-matrix \( \Z = \begin{psmallmatrix} 0 & -1 \\ 0 & -1 \end{psmallmatrix} \) has non-negative leading principal minors but is not an M-matrix.
2. Let \( \A \) be an M-matrix. Prove that \( \A + \varepsilon\I \) is a non-singular M-matrix for every real \( \varepsilon > 0 \).
3. Deduce that every principal minor of an M-matrix is non-negative.
4. Check (c) for \( \begin{psmallmatrix} 1 & -1 \\ -1 & 1 \end{psmallmatrix} \), and explain why (a) does not contradict the stated converse in the remark after @thm-m-matrix-characterizations.
:::
::::

::: {.solution}
(a) \( \det\Z_1 = 0 \) and \( \det\Z = 0\cdot(-1) - (-1)\cdot 0 = 0 \), both non-negative. \( \Z \) is upper triangular, so its eigenvalues are its diagonal entries \( 0 \) and \( -1 \) (@thm-diagonal-of-triangular-form). Its smallest real eigenvalue is \( -1 < 0 \), so by @lem-smallest-real-eigenvalue-z-matrix it is not an M-matrix: for any representation \( \Z = s\I - \B \), \( s - \rho(\B) = -1 \).

(b) Write \( \A = s\I - \B \) with \( \B \ge 0 \) and \( s \ge \rho(\B) \). Then \( \A + \varepsilon\I = (s + \varepsilon)\I - \B \) with \( s + \varepsilon > \rho(\B) \), so it is a non-singular M-matrix by @lem-smallest-real-eigenvalue-z-matrix (b).

(c) Fix a non-empty \( S \subseteq [n] \) with \( k \) elements. Then \( (\A + \varepsilon\I)_{S,S} = \A_{S,S} + \varepsilon\I_k \). By (b) and condition (f) of @thm-m-matrix-characterizations, \( q(\varepsilon) = \det(\A_{S,S} + \varepsilon\I_k) > 0 \) for every \( \varepsilon > 0 \). By the Leibniz formula, \( q \) is a polynomial in \( \varepsilon \), hence continuous by the algebra of limits quoted in Chapter 15's introduction, so \( q(1/m) \to q(0) \) as \( m \to \infty \). A non-strict inequality survives a limit, so \( \det\A_{S,S} = q(0) \ge 0 \).

(d) It is an M-matrix (see the Quick check after @lem-smallest-real-eigenvalue-z-matrix). Its principal minors are \( 1 \), \( 1 \) and \( 1 - 1 = 0 \), all non-negative. The converse in the remark asks for **all** principal minors to be non-negative, and \( \Z \) of (a) has the principal minor \( \det\Z_{\{2\},\{2\}} = -1 < 0 \). Only its **leading** ones are non-negative, and for the non-strict inequality leading minors are not enough.
:::

:::: {#exr-m-matrices-c3}
[C3: Non-negative dynamics]

Let \( \A \in M_n(\nR) \) be a Z-matrix, written as \( \A = s\I - \B \) with \( \B \ge 0 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( e^{-t\A} \ge 0 \) for every real \( t \ge 0 \).
2. Suppose \( \A \) is a non-singular M-matrix, and let \( \x \) be the solution of \( \x' = -\A\x \) with \( \x(0) = \x_0 \ge \0 \). Prove that \( \x(t) \ge \0 \) for every \( t \ge 0 \) and that \( \x(t) \to \0 \) as \( t \to \infty \).
:::

*Hint: split \( -t\A \) into two commuting matrices.*
::::

::: {.solution}
(a) \( -t\A = t\B + (-ts)\I \), and the two terms commute because every matrix commutes with a multiple of \( \I \). By @thm-exponential-properties (d), \( e^{-t\A} = e^{t\B}e^{-ts\I} \). Every partial sum of the series for \( e^{-ts\I} \) is \( \bigl(\sum_{m=0}^{M}(-ts)^m/m!\bigr)\I \), so \( e^{-ts\I} = e^{-ts}\I \). The series for \( e^{t\B} \) converges by @thm-exponential-series-converges, and its partial sums \( \sum_{m=0}^{M}t^m\B^m/m! \) are \( \ge 0 \) because \( t \ge 0 \) and \( \B \ge 0 \); a non-strict inequality survives a limit, so \( e^{t\B} \ge 0 \). Hence \( e^{-t\A} = e^{-ts}e^{t\B} \ge 0 \).

(b) By @thm-linear-ode-solution, \( \x(t) = e^{-t\A}\x_0 \), which is \( \ge \0 \) for \( t \ge 0 \) by (a). By @thm-m-matrix-characterizations (d), every eigenvalue of \( \A \) has positive real part, so every eigenvalue of \( -\A \) has negative real part: \( -\A \) is stable. By @thm-exponential-decay, \( \x(t) \to \0 \). Both conclusions matter in models of concentrations or populations, which must stay non-negative and, when \( -\A \) is stable, die out.
:::
