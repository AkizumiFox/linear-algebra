# Adding a Rank-One Matrix

Section 4 deleted a row and the matching column and found that the spectrum of the smaller matrix is pinned between the eigenvalues of the larger one. This section makes the opposite kind of change: it leaves the size alone and adds the simplest non-zero Hermitian matrix there is, a positive multiple of \( \v\v^{*} \). The answer has the same shape — the new eigenvalues interlace the old ones — but here we can say more than that they interlace. Under one extra hypothesis the new eigenvalues are the roots of a single explicit scalar equation in one variable, and the graph of that function shows at a glance where every one of them sits.

**Throughout this section \( F = \nR \) or \( F = \nC \), the matrix \( \A \in M_n(F) \) is Hermitian, and its eigenvalues are indexed decreasingly**, \( \lambda_1(\A) \ge \dots \ge \lambda_n(\A) \), as everywhere in this chapter. We fix \( \v \in F^{n} \) and a real number \( \tau \), and study
\[
\widetilde{\A} \coloneqq \A + \tau\v\v^{*} .
\]
The added term is Hermitian, since \( (\v\v^{*})^{*} = \v\v^{*} \) and \( \tau \) is real, so \( \widetilde{\A} \) is Hermitian too and its eigenvalues are indexed the same way. The added term has rank \( 1 \) when \( \tau \ne 0 \) and \( \v \ne \0 \), and is the zero matrix otherwise. For \( \tau > 0 \) it is positive semidefinite, because
\[
\inner{\tau\v\v^{*}\x}{\x} = \tau\,\x^{*}\v\,\v^{*}\x = \tau\lvert\v^{*}\x\rvert^{2} \ \ge\ 0
\]
for every \( \x \), which is clause (P2) of @def-positive-semidefinite.

## One bump, every eigenvalue up

Adding a positive semidefinite matrix can only raise the quadratic form, so no eigenvalue can go down. The content of the theorem is the ceiling: however large \( \tau \) is, the \( i \)-th new eigenvalue cannot climb past the \( (i-1) \)-st old one. All the room created by the bump is spent at the top.

::: {#thm-rank-one-interlacing}
[Interlacing for a Rank-One Update]

Let \( \A \in M_n(F) \) be Hermitian, let \( \v \in F^{n} \), let \( \tau \ge 0 \), and put \( \widetilde{\A} = \A + \tau\v\v^{*} \). Then
\[
\lambda_i(\widetilde{\A}) \ \ge\ \lambda_i(\A) \ \ge\ \lambda_{i+1}(\widetilde{\A})
\qquad (1 \le i \le n-1),
\]
and \( \lambda_n(\widetilde{\A}) \ge \lambda_n(\A) \). Written as one chain,
\[
\begin{aligned}
\lambda_1(\widetilde{\A}) \ \ge\ \lambda_1(\A) \ \ge\ \lambda_2(\widetilde{\A}) \ \ge\ \lambda_2(\A) \\
\ \ge\ \dots \ \ge\ \lambda_n(\widetilde{\A}) \ \ge\ \lambda_n(\A) .
\end{aligned}
\]
:::

::: {.idea}
The two halves have different characters and different sources. The left-hand inequalities say the eigenvalues go **up**, and that is a statement about the quadratic form: on every vector, \( \widetilde{\A} \) scores at least what \( \A \) scores, so every max–min it competes in can only improve. The right-hand inequalities say the eigenvalues go up **by at most one index**, and that has nothing to do with the sign of \( \tau \): it is the rank of the perturbation doing the work, and @cor-weyl-rank-bound has already isolated exactly that.
:::

::: {.proof}
If \( \tau = 0 \) or \( \v = \0 \) then \( \widetilde{\A} = \A \) and every inequality is an equality, so assume \( \tau > 0 \) and \( \v \ne \0 \).

For the inequalities \( \lambda_i(\widetilde{\A}) \ge \lambda_i(\A) \), fix \( i \) and let \( \x \ne \0 \). By the computation above,
\[
R_{\widetilde{\A}}(\x)
= R_{\A}(\x) + \frac{\tau\lvert\v^{*}\x\rvert^{2}}{\norm{\x}^{2}}
\ \ge\ R_{\A}(\x) ,
\]
using @def-rayleigh-quotient and \( \tau > 0 \). Multiplying through by \( \norm{\x}^2 \), this says \( \inner{\widetilde{\A}\x}{\x} \ge \inner{\A\x}{\x} \) for every \( \x \), that is, \( \widetilde{\A} \succeq \A \) in the Loewner order of @def-loewner-order. So @cor-loewner-eigenvalue-monotone gives \( \lambda_i(\widetilde{\A}) \ge \lambda_i(\A) \) for every \( i \).

For the inequalities \( \lambda_i(\A) \ge \lambda_{i+1}(\widetilde{\A}) \), note that \( \rank(\tau\v\v^{*}) = 1 \), because every column of \( \v\v^{*} \) is a multiple of \( \v \ne \0 \) and at least one of them is non-zero. So @cor-weyl-rank-bound applies with \( \B = \tau\v\v^{*} \) and \( r = 1 \), and its first inequality reads
\[
\lambda_{i+1}(\A + \tau\v\v^{*}) \ \le\ \lambda_i(\A)
\]
for \( 1 \le i \le n-1 \). This proves the theorem.
:::

Two remarks on the proof. The first half used nothing about the rank: it is @cor-loewner-eigenvalue-monotone, the general fact that \( \widetilde{\A} \succeq \A \) forces \( \lambda_i(\widetilde{\A}) \ge \lambda_i(\A) \) for every \( i \), specialized to a rank-one increment. The second half used nothing about the sign: the eigenvalues of \( \A + \B \) and of \( \A \) are never more than \( \rank\B \) indices apart. Interlacing is what happens when both restrictions apply at once.

The secular equation of the next subsection gives a sharper, **strict** version of the theorem — it locates each new eigenvalue exactly, strictly between consecutive old ones — but only under extra hypotheses (a diagonal \( \A \) with distinct entries, and a \( \v \) with no zero coordinate), so it is not a second proof of the general statement. The other short route to the general theorem is Cauchy interlacing (@thm-cauchy-interlacing) applied to a suitable bordered matrix.

::: {#exm-rank-one-two-by-two}
[A bump on a diagonal matrix]

Let \( \A = \diag(4, 1) \), \( \v = (1, 2) \) and \( \tau = 1 \). Compute \( \widetilde{\A} \) and its eigenvalues, and check @thm-rank-one-interlacing.
:::

::: {.solution}
Here \( \v\v\tp = \begin{psmallmatrix} 1 & 2 \\ 2 & 4\end{psmallmatrix} \), so
\[
\widetilde{\A} = \begin{pmatrix} 4 & 0 \\ 0 & 1 \end{pmatrix} + \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}
= \begin{pmatrix} 5 & 2 \\ 2 & 5 \end{pmatrix} .
\]
Its trace is \( 10 \) and its determinant is \( 25 - 4 = 21 \), so its characteristic polynomial is \( x^{2} - 10x + 21 = (x-7)(x-3) \) and \( \lambda_1(\widetilde{\A}) = 7 \), \( \lambda_2(\widetilde{\A}) = 3 \). The chain of the theorem reads
\[
7 \ \ge\ 4 \ \ge\ 3 \ \ge\ 1 ,
\]
and all four inequalities are strict. Note the accounting: the two eigenvalues rose by \( 3 \) and by \( 2 \), a total of \( 5 = \norm{\v}^{2} \). That is no coincidence, and the last result of this section says why.
:::

::: {.check}
The matrix \( \A = \diag(9, 5, 2) \) is bumped by \( \tau\v\v^{*} \) with \( \tau > 0 \). Without knowing \( \v \) or \( \tau \), what is the largest possible value of \( \lambda_3(\A + \tau\v\v^{*}) \), and what is the smallest?
:::

::: {.solution}
By @thm-rank-one-interlacing, \( \lambda_2(\A) \ge \lambda_3(\widetilde{\A}) \ge \lambda_3(\A) \), that is, \( 5 \ge \lambda_3(\widetilde{\A}) \ge 2 \). Both ends are reached: \( \v = \e_3 \) with \( \tau \) large gives \( \widetilde{\A} = \diag(9, 5, 2 + \tau) \), whose third eigenvalue is \( 5 \) as soon as \( \tau \ge 3 \); and \( \v = \e_1 \) gives \( \widetilde{\A} = \diag(9 + \tau, 5, 2) \), whose third eigenvalue is \( 2 \). So the smallest eigenvalue can be pushed up as far as the *second* smallest of \( \A \) and no further, no matter how big \( \tau \) is.
:::

## Where the new eigenvalues actually are

Interlacing brackets each new eigenvalue in an interval. To pin it down we need an equation, and there is a cheap one: an eigenvalue of \( \widetilde{\A} \) is a number \( \lambda \) making \( \widetilde{\A} - \lambda\I \) singular, and \( \widetilde{\A} - \lambda\I = (\A - \lambda\I) + \tau\v\v^{*} \) is a rank-one update of a matrix whose determinant we know. Chapter 8 computed the determinant of exactly such an update.

*Divide the characteristic polynomial of the bumped matrix by that of the original one; what is left is a sum of \( n \) simple fractions.*

::: {#def-secular-function}
[Secular function]

Let \( \A = \diag(d_1, \dots, d_n) \) with \( d_1, \dots, d_n \in \nR \), let \( \v \in F^{n} \) and let \( \tau \in \nR \). The **secular function** of the update \( \A + \tau\v\v^{*} \) is
\[
f(\lambda) \coloneqq 1 + \tau\sum_{i=1}^{n} \frac{\lvert v_i\rvert^{2}}{d_i - \lambda} ,
\]
defined for every real \( \lambda \) **other than** \( d_1, \dots, d_n \). The equation \( f(\lambda) = 0 \) is the **secular equation**.
:::

In words: \( f \) is the constant \( 1 \) plus one simple pole at each diagonal entry of \( \A \), weighted by \( \tau \) times the squared modulus of the matching coordinate of \( \v \). The name is inherited from celestial mechanics, where equations of this shape governed slow ("secular") drifts in planetary orbits.

::: {#thm-secular-equation}
[Eigenvalues from the Secular Equation]

Let \( \A = \diag(d_1, \dots, d_n) \) with
\[
d_1 > d_2 > \dots > d_n
\]
**strictly decreasing** and real, let \( \tau > 0 \), and let \( \v \in F^{n} \) have **every** coordinate non-zero. Write \( \widetilde{\A} = \A + \tau\v\v^{*} \) and let \( f \) be its secular function. Then:

::: {.enumerate options="label=(\alph*)"}
1. no \( d_i \) is an eigenvalue of \( \widetilde{\A} \);
2. a real number \( \lambda \notin \{d_1, \dots, d_n\} \) is an eigenvalue of \( \widetilde{\A} \) if and only if \( f(\lambda) = 0 \);
3. \( f \) has exactly \( n \) roots \( \mu_1 > \dots > \mu_n \), one in each of the intervals
   \[
   (d_1, \infty), \ (d_2, d_1), \ \dots, \ (d_n, d_{n-1}) ,
   \]
   and none below \( d_n \); these are the eigenvalues of \( \widetilde{\A} \), each simple, and
   \[
   \mu_1 > d_1 > \mu_2 > d_2 > \dots > \mu_n > d_n ;
   \]
4. for each \( j \), the vector \( (\A - \mu_j\I)^{-1}\v \) is an eigenvector of \( \widetilde{\A} \) for \( \mu_j \).
:::
:::

::: {.idea}
Part (b) is one line of Chapter 8 once (a) has cleared the denominators out of the way. Part (c) is a picture. Each term \( \lvert v_i\rvert^{2}/(d_i - \lambda) \) increases with \( \lambda \) on any interval that avoids \( d_i \), so on each of the \( n+1 \) open intervals into which the poles cut the line \( f \) climbs steadily from left to right. Just to the left of each pole \( f \) shoots up to \( +\infty \); just to the right it starts again from \( -\infty \); and far out in either direction it settles at \( 1 \). Draw that, and the roots count themselves. The proof turns the picture into a count that needs no limits at all: the \( n \) eigenvalues turn out to be distinct, there are exactly \( n \) intervals where a root can live, and each holds at most one.

\begin{center}
\begin{tikzpicture}[xscale=0.68, yscale=0.62, lab/.style={font=\small}]
    \draw[dashed, gray] (-5.0,1) -- (7.7,1);
    \node[lab, gray] at (-5.6,1) {$y=1$};
    \foreach \p in {-2,0,3} \draw[dotted, gray] (\p,-3.4) -- (\p,3.4);
    \draw[->] (-5.1,0) -- (8.0,0) node[right, lab] {$\lambda$};
    \draw[very thick] plot[smooth] coordinates
      {(-4.80,1.69) (-4.40,1.78) (-4.00,1.89) (-3.61,2.05)
       (-3.25,2.27) (-2.94,2.57) (-2.69,3.00)};
    \draw[very thick] plot[smooth] coordinates
      {(-1.79,-3.00) (-1.77,-2.55) (-1.74,-2.10) (-1.71,-1.64)
       (-1.67,-1.20) (-1.61,-0.75) (-1.54,-0.30) (-1.44,0.14)
       (-1.30,0.56) (-1.13,0.97) (-0.94,1.37) (-0.76,1.78)
       (-0.61,2.20) (-0.50,2.63) (-0.43,3.00)};
    \draw[very thick] plot[smooth] coordinates
      {(0.26,-3.00) (0.29,-2.55) (0.33,-2.10) (0.38,-1.65)
       (0.46,-1.21) (0.56,-0.77) (0.71,-0.35) (0.92,0.04)
       (1.18,0.39) (1.48,0.70) (1.79,1.00) (2.06,1.34)
       (2.28,1.72) (2.44,2.14) (2.54,2.57) (2.62,3.00)};
    \draw[very thick] plot[smooth] coordinates
      {(3.29,-3.00) (3.33,-2.55) (3.38,-2.10) (3.46,-1.65)
       (3.57,-1.22) (3.73,-0.80) (3.98,-0.44) (4.30,-0.16)
       (4.67,0.04) (5.06,0.18) (5.47,0.28) (5.87,0.35)
       (6.28,0.42) (6.69,0.46) (7.10,0.51) (7.40,0.53)};
    \node[circle, fill, inner sep=1.3pt] at (-1.474,0) {};
    \node[circle, fill, inner sep=1.3pt] at (0.887,0) {};
    \node[circle, fill, inner sep=1.3pt] at (4.587,0) {};
    \node[lab, below right] at (-1.474,0) {$\mu_3$};
    \node[lab, below right] at (0.887,0) {$\mu_2$};
    \node[lab, below right] at (4.587,0) {$\mu_1$};
    \node[lab, above, gray] at (-2,3.4) {$d_3$};
    \node[lab, above, gray] at (0,3.4) {$d_2$};
    \node[lab, above, gray] at (3,3.4) {$d_1$};
\end{tikzpicture}
\end{center}

The dotted verticals are the poles, at the old eigenvalues \( d_3 < d_2 < d_1 \); the dashed horizontal is \( y = 1 \), the level \( f \) approaches at both ends. On the branch left of \( d_3 \) every term of the sum is positive, so the curve stays above \( 1 \) and never meets the axis. Each of the other three branches runs from \( -\infty \) to \( +\infty \) or from \( -\infty \) to \( 1 \), increasing throughout, so each crosses the axis exactly once. Three branches, three roots, one strictly inside each gap and one above the top pole.
:::

::: {.proof}
**(a)** Suppose \( \widetilde{\A}\x = d_i\x \) for some \( \x \ne \0 \). Rearranging, \( (\A - d_i\I)\x = -\tau(\v^{*}\x)\v \). The matrix \( \A - d_i\I \) is diagonal with \( i \)-th diagonal entry \( 0 \), so the \( i \)-th coordinate of the left-hand side is \( 0 \); the \( i \)-th coordinate of the right-hand side is \( -\tau(\v^{*}\x)v_i \). Since \( \tau \ne 0 \) and \( v_i \ne 0 \), this forces \( \v^{*}\x = 0 \), and then \( (\A - d_i\I)\x = \0 \). The diagonal entries \( d_j \) are distinct, so the only diagonal entry of \( \A - d_i\I \) that vanishes is the \( i \)-th, and therefore \( \x = c\e_i \) for some scalar \( c \). But then \( 0 = \v^{*}\x = c\,\conj{v_i} \), and \( v_i \ne 0 \) gives \( c = 0 \), so \( \x = \0 \) — a contradiction.

**(b)** Let \( \lambda \notin \{d_1, \dots, d_n\} \). Then \( \A - \lambda\I \) is diagonal with non-zero diagonal entries, hence invertible, with
\[
(\A - \lambda\I)^{-1} = \diag\Bigl(\frac{1}{d_1 - \lambda}, \dots, \frac{1}{d_n - \lambda}\Bigr) .
\]
Apply the determinant statement of @cor-sherman-morrison — itself a \( 1 \times 1 \) case of @thm-schur-determinant — to the invertible matrix \( \A - \lambda\I \), with the column \( \tau\v \) and the row \( \v^{*} \) — that is, with \( \tau\v \) as its \( \u \) and \( \conj{\v} \) in place of its \( \v \), so that its \( \v\tp \) is our \( \v^{*} \):
\[
\begin{aligned}
\det(\widetilde{\A} - \lambda\I)
 &= \det\bigl((\A - \lambda\I) + (\tau\v)\v^{*}\bigr) \\
 &= \det(\A - \lambda\I)\,\bigl(1 + \tau\,\v^{*}(\A - \lambda\I)^{-1}\v\bigr) .
\end{aligned}
\]
The scalar in the second factor is \( \sum_i \lvert v_i\rvert^{2}/(d_i - \lambda) \), since \( \v^{*}\D\v = \sum_i \conj{v_i}\,d_{ii}v_i \) for diagonal \( \D \). So
\[
\det(\widetilde{\A} - \lambda\I) = \Bigl(\prod_{i=1}^{n}(d_i - \lambda)\Bigr) f(\lambda) ,
\tag{$\ast$}
\]
and the product is non-zero. Hence \( \det(\widetilde{\A} - \lambda\I) = 0 \) if and only if \( f(\lambda) = 0 \). Finally \( \det(\lambda\I - \widetilde{\A}) = (-1)^{n}\det(\widetilde{\A} - \lambda\I) \), since negating all \( n \) rows of a matrix multiplies its determinant by \( (-1)^{n} \), by \( n \) applications of @thm-det-row-operations (b); so the two determinants vanish together, and by @thm-charpoly-root-iff-singular (a) this happens exactly when \( \lambda \) is an eigenvalue of \( \widetilde{\A} \).

**(c)** Let \( J \) be one of the \( n+1 \) open intervals into which \( d_1, \dots, d_n \) cut the real line, and let \( \lambda < \lambda' \) lie in \( J \). For each \( i \), the numbers \( d_i - \lambda \) and \( d_i - \lambda' \) are non-zero and have the same sign, because \( d_i \notin J \); hence
\[
\frac{1}{d_i - \lambda'} - \frac{1}{d_i - \lambda}
= \frac{\lambda' - \lambda}{(d_i - \lambda)(d_i - \lambda')} \ >\ 0 .
\]
Multiplying by \( \tau\lvert v_i\rvert^{2} > 0 \) and summing over \( i \) gives \( f(\lambda') > f(\lambda) \). So \( f \) is **strictly increasing** on each such interval, and in particular has at most one root in each.

Next, every eigenspace of \( \widetilde{\A} \) is one-dimensional. Let \( \widetilde{\A}\x = \mu\x \). By (a), \( \mu \notin \{d_1, \dots, d_n\} \), so \( \A - \mu\I \) is invertible, and rearranging as in (a) gives \( (\A - \mu\I)\x = -\tau(\v^{*}\x)\v \), that is,
\[
\x = -\tau(\v^{*}\x)\,(\A - \mu\I)^{-1}\v .
\]
So \( \ker(\widetilde{\A} - \mu\I) \subseteq \Span\bigl((\A - \mu\I)^{-1}\v\bigr) \), a space of dimension \( 1 \). Now write \( \widetilde{\A} = \U\D\U^{*} \) with \( \U \) unitary and \( \D \) diagonal carrying the eigenvalue list of \( \widetilde{\A} \) with multiplicity (@cor-spectral-complex-matrix, or @cor-spectral-real-matrix over \( \nR \)). Since \( \U \) is invertible, \( \ker(\widetilde{\A} - \mu\I) = \U\ker(\D - \mu\I) \), and \( \dim\ker(\D - \mu\I) \) is the number of diagonal entries of \( \D \) equal to \( \mu \). That number is therefore at most \( 1 \): the \( n \) eigenvalues of \( \widetilde{\A} \) are **distinct**, and each is simple.

Now count. Call the eigenvalues \( \mu_1 > \dots > \mu_n \). By (b) each is a root of \( f \), and by (a) none equals a \( d_i \), so each lies in one of the \( n+1 \) open intervals. None lies in \( (-\infty, d_n) \): there every \( d_i - \lambda \) is positive, so every term of the sum is positive and \( f(\lambda) > 1 \). That leaves \( n \) intervals, each containing at most one root of \( f \), to accommodate \( n \) distinct roots — so each of the intervals \( (d_1, \infty), (d_2, d_1), \dots, (d_n, d_{n-1}) \) contains exactly one of them, and since they are listed in decreasing order, \( \mu_1 \in (d_1, \infty) \) and \( \mu_{i+1} \in (d_{i+1}, d_i) \). Conversely every root of \( f \) is an eigenvalue by (b), so \( f \) has no roots besides these \( n \). Reading the intervals in decreasing order gives the displayed chain.

**(d)** Fix \( j \) and put \( \x = (\A - \mu_j\I)^{-1}\v \), which is defined because \( \mu_j \notin \{d_1, \dots, d_n\} \) and non-zero because \( \v \ne \0 \). As in (b),
\[
\tau\,\v^{*}(\A - \mu_j\I)^{-1}\v
= \tau\sum_{i}\frac{\lvert v_i\rvert^{2}}{d_i - \mu_j}
= f(\mu_j) - 1 = -1 .
\]
Therefore
\[
\begin{aligned}
(\widetilde{\A} - \mu_j\I)\x
 &= (\A - \mu_j\I)\x + \tau\v(\v^{*}\x) \\
 &= \v + \v\,\bigl(\tau\,\v^{*}(\A - \mu_j\I)^{-1}\v\bigr)
  = \v - \v = \0 .
\end{aligned}
\]
This proves the theorem.
:::

Identity \( (\ast) \) is worth keeping on its own: it says that the characteristic polynomial of the bumped matrix is the characteristic polynomial of the original one multiplied by the secular function. The poles of \( f \) cancel the roots of the product exactly, and what survives is a polynomial of the same degree with its roots shifted one gap to the right.

::: {#exm-secular-3x3}
[A three-by-three update, found from its secular equation]

Let
\[
\A = \diag(7, 1, -3), \qquad \v = (2, 1, 2), \qquad \tau = 1 .
\]
Write down \( \widetilde{\A} = \A + \v\v\tp \) and its secular function, find all three eigenvalues from the secular equation, and confirm them independently.
:::

::: {.solution}
*The matrix.* \( \v\v\tp \) has \( (i,j) \) entry \( v_iv_j \), so
\[
\widetilde{\A} = \begin{pmatrix} 7 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -3 \end{pmatrix} + \begin{pmatrix} 4 & 2 & 4 \\ 2 & 1 & 2 \\ 4 & 2 & 4 \end{pmatrix}
= \begin{pmatrix} 11 & 2 & 4 \\ 2 & 2 & 2 \\ 4 & 2 & 1 \end{pmatrix} .
\]
The hypotheses of @thm-secular-equation hold: \( 7 > 1 > -3 \) are distinct, \( \tau = 1 > 0 \), and no coordinate of \( \v \) vanishes.

*The secular function.* With \( \lvert v_i\rvert^{2} = 4, 1, 4 \),
\[
f(\lambda) = 1 + \frac{4}{7 - \lambda} + \frac{1}{1 - \lambda} + \frac{4}{-3 - \lambda} .
\]

*The roots.* Multiply through by \( (7-\lambda)(1-\lambda)(-3-\lambda) \), which by \( (\ast) \) turns \( f \) into \( \det(\widetilde{\A} - \lambda\I) \):
\[
\begin{aligned}
&(7-\lambda)(1-\lambda)(-3-\lambda) + 4(1-\lambda)(-3-\lambda) \\
&\qquad {}+ (7-\lambda)(-3-\lambda) + 4(7-\lambda)(1-\lambda) \\
&\quad = -(\lambda - 13)(\lambda - 2)(\lambda + 1) .
\end{aligned}
\]
So the eigenvalues are \( \mu_1 = 13 \), \( \mu_2 = 2 \), \( \mu_3 = -1 \). They sit where the theorem promised:
\[
13 > 7 > 2 > 1 > -1 > -3 .
\]
It is quicker to check the three roots than to expand the product. At \( \lambda = 13 \),
\[
f(13) = 1 - \tfrac46 - \tfrac1{12} - \tfrac4{16}
= \tfrac{12 - 8 - 1 - 3}{12} = 0 ;
\]
at \( \lambda = 2 \), \( f(2) = 1 + \tfrac45 - 1 - \tfrac45 = 0 \); at \( \lambda = -1 \), \( f(-1) = 1 + \tfrac12 + \tfrac12 - 2 = 0 \).

*An independent confirmation.* Part (d) of the theorem produces eigenvectors without any further elimination: \( (\A - \mu\I)^{-1}\v \) is diagonal applied to \( \v \). For \( \mu = 13 \), \( \A - 13\I = \diag(-6, -12, -16) \) and
\[
(\A - 13\I)^{-1}\v = \bigl(-\tfrac13, -\tfrac1{12}, -\tfrac18\bigr)
\ \sim\ (8, 2, 3)
\]
after scaling by \( -24 \). Multiplying out, \( \widetilde{\A}(8,2,3) = (88 + 4 + 12,\ 16 + 4 + 6,\ 32 + 4 + 3) = (104, 26, 39) = 13\,(8, 2, 3) \). The same recipe gives \( (2, -5, -2) \) for \( \mu = 2 \) and \( (1, 2, -4) \) for \( \mu = -1 \), and both check by one matrix–vector product. Finally the trace: \( 11 + 2 + 1 = 14 = 13 + 2 - 1 \), as @cor-trace-sum-eigenvalues-again requires.
:::

::: {.warning}
**Both extra hypotheses of @thm-secular-equation earn their place, and the sign of \( \tau \) reverses the picture.**

*A zero coordinate deflates.* Take \( \A = \diag(2, 1, 0) \) and \( \v = (1, 0, 1) \), so \( v_2 = 0 \). Then \( \e_2 \) is an eigenvector of \( \widetilde{\A} = \A + \v\v\tp \) with eigenvalue \( 1 = d_2 \), because \( \v^{*}\e_2 = 0 \). So conclusion (a) fails. The secular function \( 1 + 1/(2-\lambda) - 1/\lambda \) has only two poles and only two roots, \( 2 \pm \sqrt2 \); the third eigenvalue, \( 1 \), is invisible to it. The eigenvalues still interlace, \( 2+\sqrt2 \ge 2 \ge 1 \ge 1 \ge 2 - \sqrt2 \ge 0 \), but not strictly.

*A repeated \( d_i \) deflates too.* If \( d_1 = d_2 \), any vector in \( \Span(\e_1, \e_2) \) orthogonal to \( \v \) is an eigenvector of \( \widetilde{\A} \) for \( d_1 \), for the same reason.

*Negative \( \tau \) reverses the interlacing.* For \( \tau < 0 \) the matrix \( \tau\v\v^{*} \) is negative semidefinite and every eigenvalue goes **down**: applying @thm-rank-one-interlacing to \( \widetilde{\A} \) and \( -\tau > 0 \) gives \( \lambda_i(\A) \ge \lambda_i(\widetilde{\A}) \ge \lambda_{i+1}(\A) \). Reading the chain of the theorem in the wrong direction is the standard way to get this backwards.
:::

## The shifts add up

Interlacing says where each eigenvalue may go. One number says how far they all go together, and it costs a line.

::: {#cor-eigenvalue-shift-total}
[Total Eigenvalue Shift]

Let \( \A \in M_n(F) \) be Hermitian, \( \v \in F^{n} \), \( \tau \in \nR \), and \( \widetilde{\A} = \A + \tau\v\v^{*} \). Then
\[
\sum_{i=1}^{n}\bigl(\lambda_i(\widetilde{\A}) - \lambda_i(\A)\bigr) = \tau\norm{\v}^{2} .
\]
:::

::: {.proof}
By @thm-trace-properties (3) applied to the \( n \times 1 \) matrix \( \v \) and the \( 1 \times n \) matrix \( \v^{*} \),
\[
\tr(\v\v^{*}) = \tr(\v^{*}\v) = \norm{\v}^{2} .
\]
Hence \( \tr\widetilde{\A} = \tr\A + \tau\norm{\v}^{2} \), by part (1) of the same theorem. Both \( \A \) and \( \widetilde{\A} \) are Hermitian, so @cor-trace-sum-eigenvalues-again expresses each trace as the sum of the eigenvalues with multiplicity, and subtracting the two expressions gives the claim.
:::

So the whole budget for the movement is \( \tau\norm{\v}^{2} \), and for \( \tau \ge 0 \) @thm-rank-one-interlacing says how it may be spent: each eigenvalue takes a non-negative share, and no share except the top one is large enough to carry an eigenvalue past its old upper neighbor. In @exm-rank-one-two-by-two the budget \( 5 \) was split as \( 3 + 2 \); in @exm-secular-3x3 the budget \( \norm{\v}^{2} = 9 \) was split as \( 6 + 1 + 2 \).

::: {.remark}
The secular equation of @thm-secular-equation is not only a proof device. Because \( f \) is increasing between consecutive poles and the bracketing interval is known in advance, each root can be located by bisection on an interval that is guaranteed to contain exactly one of them — a far better-behaved problem than finding the roots of a characteristic polynomial. The secular equation is the engine of the divide-and-conquer eigenvalue algorithms for Hermitian matrices, which split the matrix into two halves joined by a rank-one term and solve one secular equation to merge their spectra. The deflation observed in the warning above, where a zero coordinate of \( \v \) hands over an eigenvalue for free, is the same phenomenon that makes the algorithm fast in practice.
:::

## Exercises

### A. Check your understanding

:::: {#exr-rank-one-updates-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State @thm-rank-one-interlacing, including the hypothesis on \( \tau \).
2. Write down the secular function of \( \A + 2\v\v\tp \) for \( \A = \diag(6, 2, -1) \) and \( \v = (1, 3, 1) \).
3. Explain in one sentence why no \( d_i \) is an eigenvalue of \( \A + \tau\v\v^{*} \) under the hypotheses of @thm-secular-equation.
4. Determine whether the following is correct, and justify your answer: if \( \tau < 0 \) then \( \lambda_i(\A + \tau\v\v^{*}) \ge \lambda_i(\A) \) for every \( i \).
5. A Hermitian \( 4 \times 4 \) matrix \( \A \) has eigenvalues \( 8, 5, 5, 0 \). What does @cor-eigenvalue-shift-total say about \( \A + 3\v\v^{*} \) when \( \norm{\v} = 2 \)?
:::
::::

::: {.solution}
(a) For Hermitian \( \A \in M_n(F) \), \( \v \in F^{n} \) and \( \tau \ge 0 \), the eigenvalues of \( \widetilde{\A} = \A + \tau\v\v^{*} \) satisfy \( \lambda_i(\widetilde{\A}) \ge \lambda_i(\A) \ge \lambda_{i+1}(\widetilde{\A}) \) for \( 1 \le i \le n-1 \), together with \( \lambda_n(\widetilde{\A}) \ge \lambda_n(\A) \). The hypothesis \( \tau \ge 0 \) is what makes the perturbation positive semidefinite; without it only the second family of inequalities survives.

(b) \( \displaystyle f(\lambda) = 1 + 2\Bigl(\frac{1}{6 - \lambda} + \frac{9}{2 - \lambda} + \frac{1}{-1 - \lambda}\Bigr) \).

(c) If \( \widetilde{\A}\x = d_i\x \), comparing \( i \)-th coordinates in \( (\A - d_i\I)\x = -\tau(\v^{*}\x)\v \) forces \( \v^{*}\x = 0 \) because \( v_i \ne 0 \); then \( \x \) is a multiple of \( \e_i \), and \( \v^{*}\x = 0 \) forces that multiple to be \( 0 \).

(d) Incorrect; the inequality goes the other way. For \( \tau < 0 \) the added matrix is negative semidefinite, and \( \lambda_i(\A) \ge \lambda_i(\A + \tau\v\v^{*}) \) for every \( i \). Concretely, \( \A = \diag(1, 0) \), \( \tau = -1 \), \( \v = \e_1 \) gives \( \widetilde{\A} = \diag(0,0) \) and \( \lambda_1 \) drops from \( 1 \) to \( 0 \).

(e) It says the four eigenvalues of \( \A + 3\v\v^{*} \) sum to \( 8 + 5 + 5 + 0 + 3 \cdot 4 = 30 \), that is, \( 12 \) more than those of \( \A \). Combined with @thm-rank-one-interlacing, which caps \( \lambda_2 \) at \( 8 \), \( \lambda_3 \) at \( 5 \) and \( \lambda_4 \) at \( 5 \), it forces \( \lambda_1(\A + 3\v\v^{*}) \ge 30 - 18 = 12 \).
:::

### B. Practice

:::: {#exr-rank-one-updates-b1}
[B1: A secular equation, end to end]

Let \( \A = \diag(7, 0, -3) \), \( \v = (3, 2, 2) \) and \( \tau = 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Write down \( \widetilde{\A} = \A + \v\v\tp \) and the secular function \( f \).
2. Verify that \( 21 \), \( 2 \) and \( -2 \) are roots of \( f \), and explain why these are all the eigenvalues of \( \widetilde{\A} \).
3. Exhibit the interlacing chain of @thm-rank-one-interlacing for this pair.
:::
::::

::: {.solution}
(a) \( \v\v\tp \) has entries \( v_iv_j \), so
\[
\widetilde{\A} = \begin{pmatrix} 7 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & -3\end{pmatrix} + \begin{pmatrix} 9 & 6 & 6 \\ 6 & 4 & 4 \\ 6 & 4 & 4 \end{pmatrix}
= \begin{pmatrix} 16 & 6 & 6 \\ 6 & 4 & 4 \\ 6 & 4 & 1 \end{pmatrix},
\]
and \( \displaystyle f(\lambda) = 1 + \frac{9}{7 - \lambda} + \frac{4}{0 - \lambda} + \frac{4}{-3 - \lambda} \).

(b) At \( \lambda = 21 \): \( 1 - \tfrac9{14} - \tfrac4{21} - \tfrac4{24} = 1 - \tfrac9{14} - \tfrac4{21} - \tfrac16 \). Over \( 42 \) this is \( (42 - 27 - 8 - 7)/42 = 0 \). At \( \lambda = 2 \): \( 1 + \tfrac95 - 2 - \tfrac45 = (5 + 9 - 10 - 4)/5 = 0 \). At \( \lambda = -2 \): \( 1 + 1 + 2 - 4 = 0 \). The hypotheses of @thm-secular-equation hold — \( 7 > 0 > -3 \) are distinct, \( \tau = 1 > 0 \), and every coordinate of \( \v \) is non-zero — so by part (c) the secular function has exactly three roots and they are the eigenvalues. We have found three distinct roots, so there are no others.

(c) \( 21 \ge 7 \ge 2 \ge 0 \ge -2 \ge -3 \), all strict, as part (c) of @thm-secular-equation predicts.
:::

:::: {#exr-rank-one-updates-b2}
[B2: Reading the chain backwards]

Let \( \B = \begin{pmatrix} 5 & 2 \\ 2 & 5\end{pmatrix} \) and \( \v = (1, 2) \).

::: {.enumerate options="label=(\alph*)"}
1. Compute the eigenvalues of \( \B \) and of \( \B - \v\v\tp \).
2. State which chain of inequalities @thm-rank-one-interlacing gives here, being careful about which matrix plays the role of \( \A \).
:::
::::

::: {.solution}
(a) \( \B \) has trace \( 10 \) and determinant \( 21 \), so its characteristic polynomial is \( x^{2} - 10x + 21 = (x-7)(x-3) \) and its eigenvalues are \( 7 \) and \( 3 \). Also
\[
\B - \v\v\tp = \begin{pmatrix} 5 & 2 \\ 2 & 5\end{pmatrix} - \begin{pmatrix} 1 & 2 \\ 2 & 4\end{pmatrix}
= \begin{pmatrix} 4 & 0 \\ 0 & 1 \end{pmatrix},
\]
with eigenvalues \( 4 \) and \( 1 \).

(b) Put \( \A = \B - \v\v\tp = \diag(4,1) \) and \( \tau = 1 \), so that \( \B = \A + \tau\v\v\tp \) is the *bumped* matrix. The theorem then reads \( \lambda_1(\B) \ge \lambda_1(\A) \ge \lambda_2(\B) \ge \lambda_2(\A) \), that is, \( 7 \ge 4 \ge 3 \ge 1 \). Taking \( \B \) for \( \A \) and \( \tau = -1 \) instead would give the reversed chain \( \lambda_i(\B) \ge \lambda_i(\B - \v\v\tp) \ge \lambda_{i+1}(\B) \), namely \( 7 \ge 4 \ge 3 \ge 1 \) again: the same four numbers, read from the other side.
:::

:::: {#exr-rank-one-updates-b3}
[B3: The missing eigenvalue]

Let \( \A = \diag(5, 3, 0) \), \( \v = (2, 2, 2) \) and \( \tau = 1 \). It is given that two of the eigenvalues of \( \widetilde{\A} = \A + \v\v\tp \) are \( 15 \) and \( 4 \). Find the third without computing a characteristic polynomial, and then confirm it from the secular equation.
::::

::: {.solution}
By @cor-eigenvalue-shift-total the eigenvalues of \( \widetilde{\A} \) sum to
\[
(5 + 3 + 0) + \norm{\v}^{2} = 8 + 12 = 20 .
\]
Hence the third eigenvalue is \( 20 - 15 - 4 = 1 \).

For the confirmation, \( \lvert v_i\rvert^{2} = 4 \) for each \( i \), so
\[
f(\lambda) = 1 + \frac{4}{5-\lambda} + \frac{4}{3-\lambda} + \frac{4}{-\lambda} ,
\]
and \( f(1) = 1 + 1 + 2 - 4 = 0 \). The hypotheses of @thm-secular-equation hold, and \( 1 \) lies in the interval \( (0, 3) \) where part (c) puts the third root. As a check on the other two, \( 15 > 5 \) and \( 4 \in (3, 5) \), exactly as the theorem requires.
:::

### C. Going deeper

:::: {#exr-rank-one-updates-c1}
[C1: What a zero coordinate does]

Let \( \A = \diag(d_1, \dots, d_n) \) with the \( d_i \) real, let \( \tau \in \nR \) and let \( \v \in F^{n} \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( v_i = 0 \) then \( \e_i \) is an eigenvector of \( \A + \tau\v\v^{*} \) with eigenvalue \( d_i \).
2. Suppose \( \tau > 0 \), the \( d_i \) are strictly decreasing, and exactly one coordinate \( v_k \) vanishes. Show that the remaining \( n - 1 \) eigenvalues of \( \A + \tau\v\v^{*} \) are the roots of the function obtained from the secular function by deleting the \( k \)-th term. *Hint: restrict to the coordinate subspace spanned by the \( \e_i \) with \( i \ne k \).*
3. Illustrate both parts with \( \A = \diag(2, 1, 0) \), \( \v = (1, 0, 1) \) and \( \tau = 1 \).
:::
::::

::: {.solution}
(a) \( \v^{*}\e_i = \conj{v_i} = 0 \), so \( (\A + \tau\v\v^{*})\e_i = \A\e_i + \tau\v(\v^{*}\e_i) = d_i\e_i \).

(b) Let \( U = \Span(\e_i : i \ne k) \), a subspace of dimension \( n - 1 \). Every column of \( \A \) other than the \( k \)-th lies in \( U \), and \( \v \in U \) because \( v_k = 0 \); hence \( (\A + \tau\v\v^{*})U \subseteq U \). In the ordered basis \( (\e_i)_{i \ne k} \) of \( U \), the restriction of \( \A + \tau\v\v^{*} \) to \( U \) has matrix \( \A' + \tau\v'(\v')^{*} \), where \( \A' = \diag(d_i : i \ne k) \) and \( \v' \) is \( \v \) with its \( k \)-th coordinate removed. Since \( U \oplus \Span(\e_k) = F^{n} \) and \( \Span(\e_k) \) is also invariant by (a), the eigenvalues of \( \A + \tau\v\v^{*} \) are those of the restriction to \( U \) together with \( d_k \). Now \( \A' \) has strictly decreasing diagonal entries, \( \tau > 0 \), and \( \v' \) has no zero coordinate, so @thm-secular-equation applies to \( \A' + \tau\v'(\v')^{*} \): its \( n - 1 \) eigenvalues are exactly the roots of its secular function. That function is the secular function of the original update with the \( k \)-th term deleted, because that term was \( \tau\lvert v_k\rvert^{2}/(d_k - \lambda) = 0 \) anyway.

(c) Here \( v_2 = 0 \), so \( \e_2 \) is an eigenvector with eigenvalue \( d_2 = 1 \) by (a). By (b) the other two eigenvalues are the roots of
\[
1 + \frac{1}{2 - \lambda} + \frac{1}{-\lambda} = 0 ,
\]
that is, of \( \lambda(2-\lambda) + \lambda - (2 - \lambda) = 0 \), i.e. \( \lambda^{2} - 4\lambda + 2 = 0 \), with roots \( 2 \pm \sqrt2 \). So the spectrum is \( \{2 + \sqrt2,\ 1,\ 2 - \sqrt2\} \). Directly,
\[
\A + \v\v\tp = \begin{pmatrix} 3 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix},
\]
whose second row and column confirm the eigenvalue \( 1 \), and whose remaining \( 2 \times 2 \) block \( \begin{psmallmatrix} 3 & 1 \\ 1 & 1\end{psmallmatrix} \) has trace \( 4 \) and determinant \( 2 \).
:::

:::: {#exr-rank-one-updates-c2}
[C2: Only one eigenvalue can escape]

Let \( \A \in M_n(F) \) be Hermitian, \( \v \in F^{n} \), \( \tau \in \nR \), and \( \widetilde{\A} = \A + \tau\v\v^{*} \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that **at most one** eigenvalue of \( \widetilde{\A} \) lies outside the closed interval \( [\lambda_n(\A), \lambda_1(\A)] \), and say which one it is and on which side, according to the sign of \( \tau \).
2. Prove that the escaping eigenvalue moves by at most \( \lvert\tau\rvert\norm{\v}^{2} \), and show by examples with \( n = 2 \) that it may move by exactly that amount, and that it may not escape at all.
:::
::::

::: {.solution}
(a) Suppose first \( \tau \ge 0 \). By @thm-rank-one-interlacing, \( \lambda_n(\widetilde{\A}) \ge \lambda_n(\A) \), so no eigenvalue of \( \widetilde{\A} \) falls below the interval; and for \( i \ge 2 \), \( \lambda_i(\widetilde{\A}) \le \lambda_{i-1}(\A) \le \lambda_1(\A) \), so only \( \lambda_1(\widetilde{\A}) \) can rise above it. So at most one eigenvalue escapes, namely the largest, and it escapes upwards.

For \( \tau < 0 \), the warning above gives \( \lambda_i(\A) \ge \lambda_i(\widetilde{\A}) \ge \lambda_{i+1}(\A) \) for \( i \le n-1 \) and \( \lambda_n(\A) \ge \lambda_n(\widetilde{\A}) \). Hence \( \lambda_1(\widetilde{\A}) \le \lambda_1(\A) \), and \( \lambda_i(\widetilde{\A}) \ge \lambda_{i+1}(\A) \ge \lambda_n(\A) \) for \( i \le n-1 \). So only \( \lambda_n(\widetilde{\A}) \) can escape, and it escapes downwards.

(b) Take \( \tau > 0 \); the case \( \tau < 0 \) is the mirror image. By @thm-rank-one-interlacing every shift \( \lambda_i(\widetilde{\A}) - \lambda_i(\A) \) is \( \ge 0 \), and by @cor-eigenvalue-shift-total they sum to \( \tau\norm{\v}^{2} \). So each shift, in particular that of \( \lambda_1 \), is at most \( \tau\norm{\v}^{2} \).

For equality, let \( \A = \diag(2, 1) \), \( \v = \e_1 \), \( \tau = 3 \): then \( \widetilde{\A} = \diag(5, 1) \), and \( \lambda_1 \) moves from \( 2 \) to \( 5 \), by exactly \( \tau\norm{\v}^{2} = 3 \). For no escape, let \( \v = \e_2 \) and \( \tau = 1 \): then \( \widetilde{\A} = \diag(2, 2) \), whose eigenvalues both lie in \( [1, 2] \). The whole budget went to \( \lambda_2 \), which @thm-rank-one-interlacing caps at \( \lambda_1(\A) = 2 \).
:::

:::: {#exr-rank-one-updates-c3}
[C3: Bumping along an eigenvector]

Let \( \A \in M_n(F) \) be Hermitian with an orthonormal basis of eigenvectors \( \u_1, \dots, \u_n \), where \( \A\u_i = \lambda_i(\A)\u_i \).

::: {.enumerate options="label=(\alph*)"}
1. Fix \( k \) and \( \tau \in \nR \). Prove that the eigenvalues of \( \A + \tau\u_k\u_k^{*} \), listed with multiplicity but not necessarily in order, are \( \lambda_k(\A) + \tau \) together with \( \lambda_i(\A) \) for \( i \ne k \).
2. Deduce that \( \A - \lambda_1(\A)\u_1\u_1^{*} \) has eigenvalue list \( 0, \lambda_2(\A), \dots, \lambda_n(\A) \). (This is the **deflation** step: it removes the top eigenvalue and leaves the rest untouched, which is what makes it possible to find eigenvalues one at a time.)
3. Explain why (a) does not contradict part (c) of @thm-secular-equation.
:::
::::

::: {.solution}
(a) For \( i \ne k \), orthonormality gives \( \u_k^{*}\u_i = 0 \), so
\[
(\A + \tau\u_k\u_k^{*})\u_i = \A\u_i + \tau\u_k(\u_k^{*}\u_i) = \lambda_i(\A)\u_i .
\]
For \( i = k \), \( \u_k^{*}\u_k = 1 \) gives \( (\A + \tau\u_k\u_k^{*})\u_k = (\lambda_k(\A) + \tau)\u_k \). So \( (\u_1, \dots, \u_n) \) is a basis of \( F^{n} \) consisting of eigenvectors of \( \A + \tau\u_k\u_k^{*} \), with the stated eigenvalues. A basis of eigenvectors exhibits the whole eigenvalue list with multiplicity.

(b) Take \( k = 1 \) and \( \tau = -\lambda_1(\A) \) in (a).

(c) There is no contradiction, because the hypothesis of @thm-secular-equation that fails here fails as badly as possible. Writing everything in the orthonormal eigenbasis, the update vector is \( \u_k \), whose coordinate vector is \( \e_k \): **all but one** of its coordinates are zero. Part (a) is the extreme case of @exr-rank-one-updates-c1 (a), with \( n - 1 \) coordinates deflating at once, and only one eigenvalue is left to move.
:::
