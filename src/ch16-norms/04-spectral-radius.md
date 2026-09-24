# The Spectral Radius

Every criterion in Chapter 10 §10 began by looking at the largest modulus of an eigenvalue, and that section gave the number a name in passing — the spectral radius — without a numbered definition and without a single norm available to compare it with. It also left a note: "Chapter 16 measures matrices by norms, proves that the spectral radius never exceeds the norm of \( \A \) induced by any vector norm, and recovers \( \rho(\A) \) as a limit built from the norms of the powers \( \A^{m} \)." This section pays that note in full, and is careful about what is new when it does.

**Throughout, matrices are complex.** A real matrix is read inside \( M_n(\nC) \), exactly as Chapter 10 §10 read it when it counted eigenvalues; over \( \nR \) a matrix may have no eigenvalue at all, and then there is nothing to take the largest modulus of.

## The number Chapter 10 named

*The spectral radius is the radius of the smallest disk about the origin that holds the whole spectrum.*

::: {#def-spectral-radius}
[Spectral Radius]

Let \( \A \in M_n(\nC) \) with \( n \ge 1 \). The **spectral radius** of \( \A \) is

\[
\rho(\A) \coloneqq \max\{\,\lvert\lambda\rvert : \lambda \in \spec(\A)\,\} .
\]

For an operator \( T \) on a non-zero finite-dimensional complex vector space, \( \rho(T) \) is defined by the same formula with \( \spec(T) \) in place of \( \spec(\A) \).
:::

The maximum is over a **finite non-empty** set, so it exists with no analysis at all: \( \spec(\A) \) is the root set of the characteristic polynomial \( p_{\A} \), which is non-empty by the Fundamental Theorem of Algebra (@thm-fundamental-theorem-of-algebra) and has at most \( n \) elements. It is the largest modulus of an eigenvalue, **not** the largest eigenvalue: over \( \nC \) there is no order to take a largest in, and even for a real spectrum \( \rho(\diag(-5, 1)) = 5 \), not \( 1 \). This is the number Chapter 10 §10 introduced in prose, now with a label so that later sections can cite it.

Some values, simplest first.

- **Diagonal or triangular.** The eigenvalues of a triangular matrix are its diagonal entries (@thm-diagonal-of-triangular-form (b)), so \( \rho \) is the largest modulus on the diagonal. For \( \diag(d_1, \dots, d_n) \) it is \( \max_i\lvert d_i\rvert \).
- **Normal.** If \( \A \) is normal then \( \A = \U\D\U^{*} \) with \( \D = \diag(\lambda_1, \dots, \lambda_n) \) (@cor-spectral-complex-matrix), so \( \A^{*}\A = \U\diag(\lvert\lambda_i\rvert^2)\U^{*} \) and the singular values of \( \A \) are the moduli \( \lvert\lambda_i\rvert \). Hence \( \rho(\A) = \sigma_1(\A) = \norm{\A}_2 \) by @thm-operator-norm-formulas (c). For a normal matrix the spectral radius **is** the spectral norm, which is where the second name comes from.
- **A rotation.** \( \begin{psmallmatrix} 0 & -1 \\ 1 & 0 \end{psmallmatrix} \) has eigenvalues \( \pm i \), so \( \rho = 1 \), although no real vector is left in place.
- **Nilpotent.** \( \J_k(0) \) is triangular with zero diagonal, so by the first bullet \( \rho(\J_k(0)) = 0 \). The matrix itself is not \( 0 \) when \( k \ge 2 \).

The last entry is the degenerate case, and it is the important one: it says at once that \( \rho \) is not a norm.

::: {.warning}
**\( \rho \) is not a norm, and it is neither subadditive nor submultiplicative.** Take

\[
\A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \qquad
\B = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} .
\]

Both are nilpotent, so \( \rho(\A) = \rho(\B) = 0 \) although neither is the zero matrix. Their sum \( \begin{psmallmatrix} 0 & 1 \\ 1 & 0\end{psmallmatrix} \) has eigenvalues \( \pm 1 \) and their product \( \A\B = \begin{psmallmatrix} 1 & 0 \\ 0 & 0\end{psmallmatrix} \) has eigenvalues \( 1 \) and \( 0 \). So \( \rho(\A + \B) = 1 > 0 = \rho(\A) + \rho(\B) \) and \( \rho(\A\B) = 1 > 0 = \rho(\A)\rho(\B) \). So positive definiteness and subadditivity both fail, and so does submultiplicativity, all on the same small pair. Only absolute homogeneity survives, since \( \rho(c\A) = \lvert c\rvert\rho(\A) \) for every scalar \( c \).
:::

So \( \rho \) is a genuinely different kind of measurement from the ones of the previous section. The relation between the two is the subject of the rest of this section, and it is one-sided.

## Every norm dominates the spectral radius

::: {#thm-spectral-radius-le-norm}
[The Spectral Radius Is a Lower Bound for Every Norm]

Let \( \A \in M_n(\nC) \).

::: {.enumerate options="label=(\alph*)"}
1. If \( \norm{\cdot} \) is the operator norm on \( M_n(\nC) \) induced by a norm on \( \nC^n \) (@def-operator-norm), then \( \rho(\A) \le \norm{\A} \).
2. More generally, \( \rho(\A) \le \norm{\A} \) for **every** matrix norm \( \norm{\cdot} \) on \( M_n(\nC) \) (@def-matrix-norm).
:::
:::

::: {.idea}
For (a) there is nothing to do but write down the eigenvalue equation: an eigenvector is a vector on which \( \A \) acts by multiplication by \( \lambda \), so the stretching factor \( \lvert\lambda\rvert \) is one of the factors the maximum in @def-operator-norm ranges over. For (b) there is no vector to feed the norm, only matrices — so manufacture one: fill an \( n \times n \) matrix with copies of the eigenvector, and the eigenvalue equation becomes a matrix equation that submultiplicativity can be applied to.
:::

::: {.proof}
(a) Let \( \lambda \in \spec(\A) \) and let \( \x \ne \0 \) with \( \A\x = \lambda\x \). Then \( \norm{\A\x} = \lvert\lambda\rvert\,\norm{\x} \) by homogeneity, while \( \norm{\A\x} \le \norm{\A}\norm{\x} \) by @thm-operator-norm-properties (a). Since \( \x \ne \0 \) we have \( \norm{\x} > 0 \) and may divide, giving \( \lvert\lambda\rvert \le \norm{\A} \). This holds for every eigenvalue, so it holds for the largest modulus.

(b) Let \( \lambda \) and \( \x \) be as above, and let \( \X \in M_n(\nC) \) be the matrix all of whose \( n \) columns equal \( \x \). Then \( \X \ne 0 \), so \( \norm{\X} > 0 \). Computing column by column, \( \A\X \) has every column equal to \( \A\x = \lambda\x \), that is,

\[
\A\X = \lambda\X .
\]

Taking norms and using homogeneity on the left and submultiplicativity on the right,

\[
\lvert\lambda\rvert\,\norm{\X} = \norm{\A\X} \le \norm{\A}\,\norm{\X} .
\]

Dividing by \( \norm{\X} > 0 \) gives \( \lvert\lambda\rvert \le \norm{\A} \), and again the largest modulus obeys the same bound. This proves the theorem.
:::

This is the inequality Chapter 10 §10 promised: the spectral radius never exceeds the norm of \( \A \) induced by any vector norm. Part (b) says more than was promised, and costs one extra line.

The immediate use is that every computable norm is a computable *upper bound* for every eigenvalue — and two of the three formulas of @thm-operator-norm-formulas need no arithmetic beyond adding up moduli.

::: {#cor-spectral-radius-row-column-bound}
[Cheap Bounds on the Spectrum]

Let \( \A \in M_n(\nC) \). Then every eigenvalue \( \lambda \) of \( \A \) satisfies

\[
\lvert\lambda\rvert \le \rho(\A) \le
\min\bigl\{\norm{\A}_1,\ \norm{\A}_{\infty},\ \norm{\A}_F\bigr\} ,
\]

that is, \( \rho(\A) \) is at most the largest absolute column sum, at most the largest absolute row sum, and at most \( \norm{\A}_F \).
:::

::: {.proof}
The first two are operator norms (@thm-operator-norm-formulas (a), (b)), so @thm-spectral-radius-le-norm (a) applies; \( \norm{\cdot}_F \) is a matrix norm (@exm-frobenius-is-a-matrix-norm), so @thm-spectral-radius-le-norm (b) applies. A minimum of upper bounds is an upper bound.
:::

::: {.remark}
The bound \( \rho(\A) \le \norm{\A}_2 = \sigma_1(\A) \) is the same crude inequality \( \lvert\lambda\rvert \le \sigma_1 \) that Chapter 13 §08 obtained directly from \( \A\x = \lambda\x \). It is now one instance of a general principle rather than an isolated computation, and @thm-spectral-radius-le-norm (a) is that computation with the norm left unnamed.
:::

::: {#exm-cheap-spectral-bound}
[Bounding a spectrum without finding it]

Let \( \A = \tfrac{1}{10}\begin{pmatrix} 2 & 5 & 1 \\ 3 & 1 & 4 \\ 1 & 2 & 5 \end{pmatrix} \). Show that \( \rho(\A) \le \tfrac45 \), and hence that \( \A^{m} \to 0 \).
:::

::: {.solution}
Every row of \( \A \) sums to \( \tfrac{8}{10} = \tfrac45 \), so \( \norm{\A}_{\infty} = \tfrac45 \) by @thm-operator-norm-formulas (b), and \( \rho(\A) \le \tfrac45 \) by @cor-spectral-radius-row-column-bound. Since \( \tfrac45 < 1 \), every eigenvalue has modulus less than \( 1 \) and \( \A^{m} \to 0 \) by @thm-matrix-powers-converge-to-zero. No characteristic polynomial was computed.

The column sums are \( \tfrac{6}{10} \), \( \tfrac{8}{10} \) and \( 1 \), so \( \norm{\A}_1 = 1 \) and the column bound gives nothing. It is worth computing both and keeping the smaller. In fact \( \rho(\A) = \tfrac45 \) exactly, because the constant row sums make \( \1 \) an eigenvector with eigenvalue \( \tfrac45 \), so the row bound here is attained.
:::

::: {.check}
@thm-spectral-radius-le-norm says \( \rho(\A) \le \norm{\A} \) for every matrix norm. Why does it not follow that \( \rho \) is the smallest matrix norm?
:::

::: {.solution}
Because \( \rho \) is not a matrix norm at all: \( \rho \) vanishes on every non-zero nilpotent matrix, and it fails both subadditivity and submultiplicativity, as the warning above showed. The correct statement is that \( \rho(\A) \) is a lower bound for the *values* \( \norm{\A} \), one matrix at a time, and the next theorem shows it is the greatest such lower bound.
:::

## A norm as close to the spectral radius as we like

@thm-spectral-radius-le-norm leaves open how large the gap can be. It can be enormous for a fixed norm: \( \J_2(0) \) has \( \rho = 0 \) and \( \norm{\J_2(0)}_2 = 1 \), and multiplying the corner entry by \( 10^6 \) leaves \( \rho = 0 \) while the norm becomes \( 10^6 \). But the norm may be chosen after the matrix, and then the gap can be made as small as we please.

::: {#thm-norm-close-to-spectral-radius}
[Norms Close to the Spectral Radius]

Let \( \A \in M_n(\nC) \) and let \( \varepsilon > 0 \). Then there is a norm \( \norm{\cdot}_t \) on \( \nC^n \) whose induced operator norm satisfies

\[
\rho(\A) \le \norm{\A}_t \le \rho(\A) + \varepsilon .
\]
:::

::: {.idea}
Schur-triangularize and then squash. ① By @cor-schur-matrix, \( \A = \U\T\U^{*} \) with \( \T \) upper triangular carrying the eigenvalues on its diagonal; the row sums of \( \T \) are the diagonal entry plus the off-diagonal junk. ② Conjugating \( \T \) by \( \D_t = \diag(1, t, \dots, t^{n-1}) \) multiplies the entry in position \( (i,j) \) by \( t^{i-j} \), which leaves the diagonal alone and, for large \( t \), shrinks everything strictly above it, because \( i - j < 0 \) there. ③ Choose \( t \) so that every off-diagonal row sum is below \( \varepsilon \); the largest row sum is then below \( \rho(\A) + \varepsilon \), and the largest row sum is a norm we can compute, by @thm-operator-norm-formulas (b). ④ Transport that norm back to \( \nC^n \) along the invertible matrix \( \D_t\U^{*} \).
:::

::: {.proof}
By @cor-schur-matrix there are a unitary \( \U \) and an upper triangular \( \T = (t_{ij}) \) with \( \A = \U\T\U^{*} \) and \( t_{ii} = \lambda_i \), the eigenvalues of \( \A \). For \( t \ge 1 \) put \( \D_t = \diag(1, t, t^2, \dots, t^{n-1}) \), an invertible matrix, and \( \T_t = \D_t\T\D_t^{-1} \). Multiplying out,

\[
(\T_t)_{ij} = t^{\,i-1}\,t_{ij}\,t^{-(j-1)} = t^{\,i-j}t_{ij} .
\]

So \( \T_t \) is again upper triangular with the same diagonal \( \lambda_1, \dots, \lambda_n \), while for \( i < j \) the entry is scaled by \( t^{i-j} \le t^{-1} \), using \( t \ge 1 \) and \( j - i \ge 1 \). Let \( M = \max_{i<j}\lvert t_{ij}\rvert \) if \( n \ge 2 \), and \( M = 0 \) if \( n = 1 \). Then the \( i \)-th absolute row sum of \( \T_t \) is at most

\[
\lvert\lambda_i\rvert + \sum_{j > i}t^{-1}\lvert t_{ij}\rvert
\le \rho(\A) + \frac{(n-1)M}{t} .
\]

Choose \( t = \max\bigl(1,\ (n-1)M/\varepsilon\bigr) \). Then every absolute row sum of \( \T_t \) is at most \( \rho(\A) + \varepsilon \), so \( \norm{\T_t}_{\infty} \le \rho(\A) + \varepsilon \) by @thm-operator-norm-formulas (b).

Now define, for \( \x \in \nC^n \),

\[
\norm{\x}_t \coloneqq \norm{\D_t\U^{*}\x}_{\infty} .
\]

This is a norm: it is non-negative, homogeneous and subadditive because \( \norm{\cdot}_{\infty} \) is and \( \x \mapsto \D_t\U^{*}\x \) is linear, and it vanishes only at \( \x = \0 \) because \( \D_t\U^{*} \) is invertible.

It remains to compute the induced operator norm. Put \( \Q = \D_t\U^{*} \), so \( \norm{\x}_t = \norm{\Q\x}_{\infty} \). As \( \x \) runs over \( \{\norm{\x}_t = 1\} \), the vector \( \y = \Q\x \) runs over \( \{\norm{\y}_{\infty} = 1\} \), since \( \Q \) is a bijection. Moreover \( \Q\A\Q^{-1} = \D_t\U^{*}\A\U\D_t^{-1} = \D_t\T\D_t^{-1} = \T_t \), so

\[
\norm{\A\x}_t = \norm{\Q\A\x}_{\infty} = \norm{\T_t\,\y}_{\infty} .
\]

Taking maxima over the two matching sets gives \( \norm{\A}_t = \norm{\T_t}_{\infty} \le \rho(\A) + \varepsilon \). The lower bound \( \rho(\A) \le \norm{\A}_t \) is @thm-spectral-radius-le-norm (a). This proves the theorem.
:::

Read together, the last two theorems say

\[
\rho(\A) = \inf\{\norm{\A} : \norm{\cdot} \text{ an induced matrix norm}\} .
\]

::: {.remark}
The infimum need not be attained. If \( \A \ne 0 \) is nilpotent then \( \rho(\A) = 0 \) while \( \norm{\A} > 0 \) for every norm, so no norm achieves the value. At the other extreme, for a normal \( \A \) the spectral norm achieves it exactly: \( \norm{\A}_2 = \rho(\A) \), as computed at the start of this section. The gap between \( \rho \) and the norms is a measure of how far \( \A \) is from being normal, which is the theme Chapter 12 §11 opened with the departure from normality.
:::

## Gelfand's formula

The infimum above is over norms, and to use it we must choose one. There is a second description of \( \rho(\A) \) that needs no choice: fix any norm at all, and let the powers of \( \A \) tell you the answer.

::: {#thm-gelfand}
[Gelfand's Formula]

Let \( \A \in M_n(\nC) \) and let \( \norm{\cdot} \) be any matrix norm on \( M_n(\nC) \). Then

\[
\lim_{k \to \infty}\ \norm{\A^{k}}^{1/k} = \rho(\A) .
\]

In particular the limit exists and does not depend on which matrix norm is used.
:::

::: {.idea}
Two inequalities, one for each direction, and they come from opposite ends of the chapter. ① The lower bound \( \rho(\A) \le \norm{\A^k}^{1/k} \) is @thm-spectral-radius-le-norm applied to \( \A^{k} \), once we know \( \rho(\A^{k}) = \rho(\A)^{k} \) — which is the Spectral Mapping Theorem. This holds for every \( k \), with no limit taken. ② For the upper bound, scale \( \A \) down by a whisker more than \( \rho(\A) \). The scaled matrix has spectral radius below \( 1 \), so Chapter 10 §10's criterion makes its powers tend to \( 0 \), and once they are below \( 1 \) in norm the inequality we want has been written down. @thm-norm-close-to-spectral-radius says the same decay is geometric, which is what the corollary below extracts.
:::

::: {.proof}
**Lower bound.** Fix \( k \ge 1 \). By @thm-spectral-mapping applied to \( q(x) = x^{k} \), \( \spec(\A^{k}) = \{\lambda^{k} : \lambda \in \spec(\A)\} \), so

\[
\rho(\A^{k}) = \max_{\lambda \in \spec(\A)}\lvert\lambda\rvert^{k} = \rho(\A)^{k} .
\]

By @thm-spectral-radius-le-norm (b) applied to \( \A^{k} \), \( \rho(\A)^{k} = \rho(\A^{k}) \le \norm{\A^{k}} \). Taking \( k \)-th roots of these non-negative reals,

\[
\rho(\A) \le \norm{\A^{k}}^{1/k} \qquad \text{for every } k \ge 1 .
\]

**Upper bound.** Let \( \varepsilon > 0 \), put \( s = \rho(\A) + \varepsilon > 0 \) and \( \B = s^{-1}\A \). Every eigenvalue of \( \B \) is \( \lambda/s \) for some \( \lambda \in \spec(\A) \) (@thm-spectral-mapping with \( q(x) = x/s \)), so

\[
\rho(\B) = \frac{\rho(\A)}{\rho(\A) + \varepsilon} < 1 .
\]

By @thm-matrix-powers-converge-to-zero, \( \B^{k} \to 0 \) entrywise. Entrywise convergence of matrices is convergence in **every** norm on \( M_n(\nC) \), by @cor-entrywise-convergence-is-the-convergence, so \( \norm{\B^{k}} \to 0 \). A real sequence tending to \( 0 \) is eventually below \( 1 \): there is \( K \) with \( \norm{\B^{k}} \le 1 \) for all \( k \ge K \). Since \( \B^{k} = s^{-k}\A^{k} \), homogeneity gives \( \norm{\A^{k}} \le s^{k} \), that is,

\[
\norm{\A^{k}}^{1/k} \le \rho(\A) + \varepsilon \qquad (k \ge K) .
\]

**Conclusion.** Combining, for every \( \varepsilon > 0 \) there is \( K \) with

\[
\rho(\A) \le \norm{\A^{k}}^{1/k} \le \rho(\A) + \varepsilon \qquad (k \ge K),
\]

which is the definition of \( \norm{\A^{k}}^{1/k} \to \rho(\A) \). The independence of the norm is automatic, since the limit equals \( \rho(\A) \) whichever matrix norm was fixed at the start. This proves the theorem.
:::

::: {.remark}
**Which analysis was used.** The lower bound used none. The upper bound used @thm-matrix-powers-converge-to-zero, which is a theorem of this book, and @cor-entrywise-convergence-is-the-convergence, likewise; the only analysis is that a real sequence tending to \( 0 \) is eventually less than \( 1 \), and that a sequence trapped between \( \rho(\A) \) and \( \rho(\A) + \varepsilon \) for every \( \varepsilon > 0 \) converges to \( \rho(\A) \). Neither is an extra import: both are the definition of a limit of a real sequence, read forwards and backwards. Nothing from the list (A1)–(A4) of the chapter introduction is needed here, and nothing outside it is used.
:::

The formula is a genuine computation rule as well as a theorem. For a fixed \( k \) the number \( \norm{\A^{k}}^{1/k} \) is an *upper* estimate of \( \rho(\A) \) — that is the lower bound above, read the other way — and the estimates improve as \( k \) grows.

::: {#exm-gelfand-triangular}
[Watching the limit converge]

Let \( \A = \begin{pmatrix} 1/2 & 10 \\ 0 & 1/3 \end{pmatrix} \). Compute \( \norm{\A^{k}}_{\infty} \) exactly and confirm Gelfand's formula.
:::

::: {.solution}
\( \A \) is upper triangular, so \( \rho(\A) = \max(\tfrac12, \tfrac13) = \tfrac12 \) and the powers are upper triangular with diagonal \( 2^{-k}, 3^{-k} \). For the corner entry, induction on \( k \) gives

\[
(\A^{k})_{12} = 10\sum_{j=0}^{k-1}2^{-j}3^{-(k-1-j)}
= 60\bigl(2^{-k} - 3^{-k}\bigr),
\]

the last step by summing the geometric series with ratio \( 3/2 \). The two absolute row sums are \( 2^{-k} + 60(2^{-k} - 3^{-k}) \) and \( 3^{-k} \), the first being the larger, so by @thm-operator-norm-formulas (b)

\[
\norm{\A^{k}}_{\infty} = 61\cdot 2^{-k} - 60\cdot 3^{-k} .
\]

At \( k = 1 \) this is \( 10.5 \), which overestimates \( \rho(\A) = \tfrac12 \) by a factor of \( 21 \); the \( k \)-th roots run \( 10.5,\ 2.93,\ 1.75,\ 1.32,\ 1.11,\ 0.98, \dots \) and settle toward \( \tfrac12 \), which is what @thm-gelfand guarantees. The convergence is slow, and it has to be: the single number \( \norm{\A}_{\infty} \) cannot know that the entry \( 10 \) sits above the diagonal rather than on it.
:::

## What is new, and what is not

::: {#cor-powers-converge-iff-rho-lt-one}
[Powers Tending to Zero, with a Rate]

Let \( \A \in M_n(\nC) \) and let \( \norm{\cdot} \) be any matrix norm on \( M_n(\nC) \).

::: {.enumerate options="label=(\alph*)"}
1. \( \A^{k} \to 0 \) if and only if \( \rho(\A) < 1 \), and this holds if and only if \( \norm{\A^{k}} \to 0 \).
2. If \( \rho(\A) < 1 \), then for every \( q \) with \( \rho(\A) < q < 1 \) there is a constant \( C \ge 1 \), depending on \( \A \), on \( q \) and on the norm, such that \( \norm{\A^{k}} \le C\,q^{k} \) for **every** \( k \ge 0 \).
:::
:::

::: {.idea}
Part (a) is @thm-matrix-powers-converge-to-zero translated into norms by @cor-entrywise-convergence-is-the-convergence; nothing is proved that was not proved in Chapter 10. Part (b) is the new content, and it is @thm-norm-close-to-spectral-radius doing what it was built for: choose a norm in which \( \A \) itself is already smaller than \( q \), take powers there, and pay one fixed constant to return to the norm we were given.
:::

::: {.proof}
(a) The first equivalence is @thm-matrix-powers-converge-to-zero, since \( \rho(\A) < 1 \) says exactly that every eigenvalue has modulus less than \( 1 \). The second is @cor-entrywise-convergence-is-the-convergence: entrywise convergence of matrices and convergence in the norm \( \norm{\cdot} \) are the same thing.

(b) Let \( \varepsilon = q - \rho(\A) > 0 \). By @thm-norm-close-to-spectral-radius there is an induced matrix norm \( \norm{\cdot}_t \) on \( M_n(\nC) \) with \( \norm{\A}_t \le \rho(\A) + \varepsilon = q \). Submultiplicativity (@thm-operator-norm-properties (d)) gives \( \norm{\A^{k}}_t \le \norm{\A}_t^{k} \le q^{k} \) for every \( k \ge 0 \). By @thm-norm-equivalence, applied to the two norms \( \norm{\cdot} \) and \( \norm{\cdot}_t \) on the finite-dimensional space \( M_n(\nC) \), there is \( C_0 > 0 \) with \( \norm{\M} \le C_0\norm{\M}_t \) for every \( \M \). Taking \( C = \max(C_0, 1) \),

\[
\norm{\A^{k}} \le C_0\norm{\A^{k}}_t \le C\,q^{k} .
\]

This proves the corollary.
:::

It is worth being exact about the accounting. Part (a) is **not** new. Chapter 10 §10 proved that \( \A^{m} \to 0 \) if and only if every eigenvalue has modulus less than \( 1 \), and it proved it with the Jordan form and no norms whatsoever; all that has happened here is that the conclusion has been restated in a language where "small" is a number. What is new is part (b): a **rate**. Chapter 10 could say that the powers die; it could not say how fast, because it had nothing to measure a matrix with. Now every decaying matrix comes with a geometric envelope \( Cq^{k} \) for every \( q \) above its spectral radius, and that envelope is what later sections integrate, sum and differentiate.

Two honest limitations of the envelope deserve saying out loud.

::: {.warning}
**\( \rho(\A) < 1 \) promises eventual decay, not immediate decay.** The constant \( C \) in @cor-powers-converge-iff-rho-lt-one (b) is generally larger than \( 1 \) and grows as \( q \) approaches \( \rho(\A) \). For

\[
\A = \begin{pmatrix} 9/10 & 10 \\ 0 & 9/10 \end{pmatrix}, \qquad
\A^{k} = \begin{pmatrix} (9/10)^{k} & 10k(9/10)^{k-1} \\ 0 & (9/10)^{k} \end{pmatrix},
\]

we have \( \rho(\A) = 9/10 < 1 \), yet \( \norm{\A^{k}}_{\infty} = (9/10)^{k-1}(9/10 + 10k) \) **rises** from \( 10.9 \) at \( k = 1 \) to about \( 39.13 \) at \( k = 9 \) before beginning its decay, and does not fall below \( 1 \) until \( k = 63 \). A transient hump of this kind is invisible to the spectral radius and is exactly what the constant \( C \) is paying for.
:::

::: {.check}
For which matrices can one take \( C = 1 \) and \( q = \rho(\A) \) in the bound of @cor-powers-converge-iff-rho-lt-one (b), with the spectral norm?
:::

::: {.solution}
For normal \( \A \), among others. If \( \A \) is normal then so is \( \A^{k} \) (its adjoint is \( (\A^{*})^{k} \), and powers of commuting matrices commute), so \( \norm{\A^{k}}_2 = \rho(\A^{k}) = \rho(\A)^{k} \) by the computation at the start of this section together with @thm-spectral-mapping. There is then no transient at all: the norm of the powers is exactly geometric. The hump in the warning is possible only because that matrix is far from normal, with departure from normality \( 10 \) in the sense of @def-departure-from-normality.
:::

## Exercises

### A. Check your understanding

:::: {#exr-spectral-radius-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the **spectral radius**, and say why the maximum in the definition exists.
2. State @thm-spectral-radius-le-norm and @thm-gelfand.
3. Determine whether the following statement is correct, and justify your answer: \( \rho \) is a matrix norm on \( M_n(\nC) \).
4. Determine whether the following statement is correct, and justify your answer: if \( \rho(\A) < 1 \) then \( \norm{\A}_2 < 1 \).
5. Chapter 10 §10 already proved that \( \A^{m} \to 0 \) exactly when \( \rho(\A) < 1 \). What does @cor-powers-converge-iff-rho-lt-one add to that?
:::
::::

::: {.solution}
(a) \( \rho(\A) = \max\{\lvert\lambda\rvert : \lambda \in \spec(\A)\} \) (@def-spectral-radius). The set \( \spec(\A) \) is finite and non-empty — it is the root set of \( p_{\A} \), non-empty by @thm-fundamental-theorem-of-algebra — so the maximum of the finitely many moduli exists.

(b) For every matrix norm on \( M_n(\nC) \), \( \rho(\A) \le \norm{\A} \); and for every matrix norm, \( \norm{\A^{k}}^{1/k} \to \rho(\A) \) as \( k \to \infty \).

(c) Incorrect. \( \rho \) vanishes on non-zero nilpotent matrices, so it is not even a norm, and it is neither subadditive nor submultiplicative: see the warning after @def-spectral-radius.

(d) Incorrect. \( \A = \begin{psmallmatrix} 0 & 10 \\ 0 & 0\end{psmallmatrix} \) has \( \rho(\A) = 0 \) and \( \norm{\A}_2 = 10 \). The correct statement is that *some* norm has \( \norm{\A} < 1 \), by @thm-norm-close-to-spectral-radius.

(e) Nothing about the criterion, which is @thm-matrix-powers-converge-to-zero restated; what it adds is the quantitative envelope \( \norm{\A^{k}} \le Cq^{k} \) for every \( q \in (\rho(\A), 1) \), a rate of decay rather than the bare fact of it.
:::

### B. Practice

:::: {#exr-spectral-radius-b1}
[B1: Four numbers again]

Let \( \A = \begin{pmatrix} 0 & 2 \\ 1/4 & 0 \end{pmatrix} \). Compute \( \rho(\A) \), \( \norm{\A}_1 \), \( \norm{\A}_{\infty} \) and \( \norm{\A}_2 \), and verify @thm-spectral-radius-le-norm in each case.
::::

::: {.solution}
\( p_{\A}(x) = x^2 - \tfrac12 \), so \( \spec(\A) = \{\pm 1/\sqrt2\} \) and \( \rho(\A) = 1/\sqrt2 \approx 0.707 \).

The absolute column sums are \( \tfrac14 \) and \( 2 \), so \( \norm{\A}_1 = 2 \); the absolute row sums are \( 2 \) and \( \tfrac14 \), so \( \norm{\A}_{\infty} = 2 \). For the spectral norm, \( \A\tp\A = \diag(\tfrac1{16}, 4) \), whose eigenvalues are \( \tfrac1{16} \) and \( 4 \); hence \( \sigma_1 = 2 \) and \( \norm{\A}_2 = 2 \) by @thm-operator-norm-formulas (c).

So \( \rho(\A) = 0.707\dots \le 2 \) in all three cases, and the gap is a factor of nearly \( 3 \) even though \( \A \) is a very small matrix. The reason is the mismatch between the two off-diagonal entries: \( \A \) is far from normal.
:::

:::: {#exr-spectral-radius-b2}
[B2: Gelfand exactly]

With \( \A \) as in @exr-spectral-radius-b1, compute \( \A^{k} \) for every \( k \) and evaluate \( \lim_k\norm{\A^{k}}_{\infty}^{1/k} \) directly.
::::

::: {.solution}
\( \A^2 = \tfrac12\I \), so by induction \( \A^{2l} = 2^{-l}\I \) and \( \A^{2l+1} = 2^{-l}\A \). Hence

\[
\norm{\A^{2l}}_{\infty} = 2^{-l}, \qquad
\norm{\A^{2l+1}}_{\infty} = 2^{-l}\cdot 2 = 2^{1-l} .
\]

For even \( k = 2l \), \( \norm{\A^{k}}_{\infty}^{1/k} = (2^{-l})^{1/(2l)} = 2^{-1/2} \), exactly \( \rho(\A) \) for every \( l \). For odd \( k = 2l+1 \), \( \norm{\A^{k}}_{\infty}^{1/k} = 2^{(1-l)/(2l+1)} \), and \( (1-l)/(2l+1) \to -\tfrac12 \), so this too tends to \( 2^{-1/2} \). Both subsequences converge to \( 1/\sqrt2 = \rho(\A) \), confirming @thm-gelfand.
:::

:::: {#exr-spectral-radius-b3}
[B3: Deciding convergence without eigenvalues]

For each matrix, decide whether \( \A^{m} \to 0 \), using only @cor-spectral-radius-row-column-bound and @thm-matrix-powers-converge-to-zero.

::: {.enumerate options="label=(\alph*)"}
1. \( \A = \tfrac{1}{4}\begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \\ 2 & 0 & 1 \end{pmatrix} \).
2. \( \A = \begin{pmatrix} 1/2 & 3 \\ 0 & 2 \end{pmatrix} \).
:::
::::

::: {.solution}
(a) The absolute row sums are \( \tfrac34 \), \( \tfrac12 \) and \( \tfrac34 \), so \( \norm{\A}_{\infty} = \tfrac34 \) and \( \rho(\A) \le \tfrac34 < 1 \). By @thm-matrix-powers-converge-to-zero, \( \A^{m} \to 0 \).

(b) Here the row sums are \( \tfrac72 \) and \( 2 \) and the column sums are \( \tfrac12 \) and \( 5 \), so the bounds give only \( \rho(\A) \le \tfrac72 \) and decide nothing. But the bound is an upper bound, and here the matrix is triangular, so the eigenvalues are visible: \( \tfrac12 \) and \( 2 \), giving \( \rho(\A) = 2 > 1 \). By @thm-matrix-powers-converge-to-zero the powers do **not** tend to \( 0 \). The moral is that @cor-spectral-radius-row-column-bound can only ever certify convergence, never rule it out.
:::

### C. Going deeper

:::: {#exr-spectral-radius-c1}
[C1: A norm that sees the decay]

Let \( \A \in M_n(\nC) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( \norm{\A} < 1 \) for **some** matrix norm, then \( \A^{k} \to 0 \).
2. Give a matrix with \( \A^{k} \to 0 \) and \( \norm{\A}_2 > 1 \), so that the converse of (a) fails for a fixed norm.
3. Prove that the converse of (a) nevertheless holds if the norm is allowed to depend on \( \A \).
:::
::::

::: {.solution}
(a) Submultiplicativity gives \( \norm{\A^{k}} \le \norm{\A}^{k} \) by induction on \( k \). With \( r = \norm{\A} < 1 \) the right-hand side tends to \( 0 \), so \( \norm{\A^{k}} \to 0 \), and by @cor-entrywise-convergence-is-the-convergence this is the same as \( \A^{k} \to 0 \) entrywise.

(b) \( \A = \begin{psmallmatrix} 0 & 10 \\ 0 & 0\end{psmallmatrix} \) satisfies \( \A^2 = 0 \), so certainly \( \A^{k} \to 0 \); but \( \norm{\A}_2 = 10 > 1 \). The same happens for \( \begin{psmallmatrix} 1/2 & 10 \\ 0 & 1/2\end{psmallmatrix} \), which is not even nilpotent.

(c) Suppose \( \A^{k} \to 0 \). By @thm-matrix-powers-converge-to-zero, \( \rho(\A) < 1 \). Apply @thm-norm-close-to-spectral-radius with \( \varepsilon = \tfrac12(1 - \rho(\A)) > 0 \): it produces an induced matrix norm \( \norm{\cdot}_t \) with

\[
\norm{\A}_t \le \rho(\A) + \varepsilon = \tfrac12\bigl(1 + \rho(\A)\bigr) < 1 .
\]

So a norm witnessing the decay always exists, though it must be chosen after \( \A \).
:::

:::: {#exr-spectral-radius-c2}
[C2: Spectral radius zero]

Let \( \A \in M_n(\nC) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \rho(\A) = 0 \) if and only if \( \A \) is nilpotent.
2. Deduce that for a nilpotent \( \A \) and any matrix norm, \( \norm{\A^{k}}^{1/k} \to 0 \), and verify this directly for \( \A = \J_n(0) \).
3. Explain why (a) shows that no inequality of the form \( \norm{\A} \le c\,\rho(\A) \), with \( c \) depending only on \( n \), can hold.
:::
::::

::: {.solution}
(a) \( (\Rightarrow) \) If \( \rho(\A) = 0 \) then every eigenvalue is \( 0 \), so \( p_{\A}(x) = x^{n} \) because \( p_{\A} \) is monic of degree \( n \) and splits over \( \nC \) with all roots \( 0 \) (@thm-fundamental-theorem-of-algebra). By the Cayley–Hamilton theorem (@thm-cayley-hamilton), \( \A^{n} = p_{\A}(\A) = 0 \), so \( \A \) is nilpotent (@def-nilpotent).

\( (\Leftarrow) \) If \( \A^{d} = 0 \) and \( \A\x = \lambda\x \) with \( \x \ne \0 \), then \( \0 = \A^{d}\x = \lambda^{d}\x \), so \( \lambda^{d} = 0 \) and \( \lambda = 0 \). Hence \( \spec(\A) = \{0\} \) and \( \rho(\A) = 0 \).

(b) By @thm-gelfand the limit is \( \rho(\A) = 0 \). Directly for \( \A = \J_n(0) \): \( \A^{k} = 0 \) for \( k \ge n \), so \( \norm{\A^{k}}^{1/k} = 0 \) for all \( k \ge n \), and the sequence is eventually constant at \( 0 \).

(c) Such an inequality would force \( \norm{\A} = 0 \), hence \( \A = 0 \), for every nilpotent \( \A \). But \( \J_2(0) \ne 0 \) is nilpotent. So the two quantities cannot be compared in that direction at all; @thm-norm-close-to-spectral-radius is the best available substitute, and it buys its conclusion by changing the norm.
:::

:::: {#exr-spectral-radius-c3}
[C3: When the infimum is attained]

Call \( \A \in M_n(\nC) \) **radius-attaining** if \( \norm{\A} = \rho(\A) \) for some matrix norm.

::: {.enumerate options="label=(\alph*)"}
1. Prove that every normal \( \A \) is radius-attaining.
2. Prove that a non-zero nilpotent \( \A \) is not.
3. Deduce that \( \begin{psmallmatrix} 1 & 1 \\ 0 & 1 \end{psmallmatrix} \) is not radius-attaining, even though it is invertible.
:::

*Hint for (c): consider \( \A - \I \).*
::::

::: {.solution}
(a) Let \( \A \) be normal, so \( \A = \U\D\U^{*} \) with \( \U \) unitary and \( \D = \diag(\lambda_1, \dots, \lambda_n) \) (@cor-spectral-complex-matrix). Then \( \A^{*}\A = \U\diag(\lvert\lambda_i\rvert^2)\U^{*} \), so the singular values of \( \A \) are the \( \lvert\lambda_i\rvert \) in decreasing order and \( \norm{\A}_2 = \sigma_1 = \max_i\lvert\lambda_i\rvert = \rho(\A) \) by @thm-operator-norm-formulas (c).

(b) If \( \A \ne 0 \) is nilpotent then \( \rho(\A) = 0 \) by @exr-spectral-radius-c2 (a), while \( \norm{\A} > 0 \) for every norm, since a norm vanishes only at \( 0 \) (@def-norm). So no norm can give \( \norm{\A} = \rho(\A) \).

(c) Put \( \A = \begin{psmallmatrix} 1 & 1 \\ 0 & 1\end{psmallmatrix} \), whose only eigenvalue is \( 1 \), so \( \rho(\A) = 1 \). Suppose some matrix norm had \( \norm{\A} = 1 \). Then \( \norm{\A^{k}} \le \norm{\A}^{k} = 1 \) for every \( k \), so the sequence \( (\A^{k}) \) is bounded in that norm, hence bounded entrywise by @cor-entrywise-convergence-is-the-convergence, whose second sentence covers boundedness. But \( \A^{k} = \begin{psmallmatrix} 1 & k \\ 0 & 1\end{psmallmatrix} \), whose \( (1,2) \)-entry is unbounded. Contradiction. (The hint points at the same phenomenon: \( \A - \I \) is a non-zero nilpotent, so \( \A \) is a unipotent matrix, and it is the nilpotent part that the spectral radius cannot see.)
:::
