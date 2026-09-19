# The Collatz–Wielandt Formula

Section 3 proved that the spectral radius of a non-negative matrix is an eigenvalue, and that for an irreducible matrix it comes with a positive eigenvector. It did not say how to find the number. Finding it through the characteristic polynomial means finding the largest root of a polynomial of degree \( n \), which in general has no formula in radicals once \( n \ge 5 \). This section gives a way to trap \( \rho(\A) \) between two numbers read off from a single test vector, with no eigenvalue computed. Each test vector gives a lower and an upper bound, and the bounds meet exactly at the Perron vector. That turns \( \rho(\A) \) into a maximum and a minimum over vectors, much as Chapter 16 turned the eigenvalues of a Hermitian matrix into extreme values of the Rayleigh quotient (@def-rayleigh-quotient).

Throughout, matrices have real entries, and \( \ge \), \( > \) between matrices or vectors are the entrywise order of Section 1. We use one elementary fact repeatedly. If \( \A \ge 0 \) and \( \u \ge \u' \), then \( \A\u \ge \A\u' \), because each entry of \( \A(\u - \u') \) is a sum of products of non-negative numbers. In words, a non-negative matrix preserves the order.

## Bounds from a single test vector

If \( \v > \0 \) is an eigenvector for \( \rho \), then the ratios \( (\A\v)_i / v_i \) are all equal to \( \rho \). For a vector that is not an eigenvector, the ratios spread out. The idea of this section is that \( \rho \) always lies somewhere in that spread.

Take \( \x = \1 \). Then \( (\A\1)_i \) is the \( i \)-th row sum, so the ratios are the row sums. For
\[
\A = \begin{pmatrix} 0 & 1 & 1 \\ 0 & 1 & 2 \\ 1 & 0 & 3 \end{pmatrix}
\]
they are \( 2, 3, 4 \). The characteristic polynomial is \( t^3 - 4t^2 + 2t - 1 \), and \( \rho(\A) \approx 3.51 \), which indeed lies between \( 2 \) and \( 4 \). Two propositions make "lies in the spread" precise, one for each end. The upper end is the classical one.

::: {#prp-subinvariance}
[Subinvariance]

Let \( \A \in M_n(\nR) \) with \( \A \ge 0 \), and let \( s \in \nR \).

::: {.enumerate options="label=(\alph*)"}
1. If \( \x > \0 \) and \( \A\x \le s\x \), then \( \rho(\A) \le s \).
2. If \( \A \) is irreducible, \( \x \ge \0 \), \( \x \ne \0 \) and \( \A\x \le s\x \), then \( \rho(\A) \le s \). If moreover \( \A\x \ne s\x \), then \( \rho(\A) < s \).
:::
:::

::: {.idea}
For (a), rescale the coordinates by the entries of \( \x \). In the new coordinates, \( \x \) becomes \( \1 \), the hypothesis says that every row sum is at most \( s \), and Chapter 15's row-sum bound finishes the job. For (b), \( \x \) may have zero entries, so no rescaling is possible. Instead, pair the inequality with the left Perron vector \( \w > \0 \), which turns \( \w\tp\A\x \) into \( \rho\,\w\tp\x \).
:::

::: {.proof}
(a) Let \( \D = \diag(x_1, \dots, x_n) \), which is invertible because every \( x_i > 0 \), and put \( \C = \D^{-1}\A\D \). Its entries are \( c_{ij} = a_{ij}x_j/x_i \ge 0 \), and its \( i \)-th row sum is
\[
\sum_{j=1}^{n} \frac{a_{ij}x_j}{x_i} = \frac{(\A\x)_i}{x_i} \le s ,
\]
where the inequality divides \( (\A\x)_i \le s x_i \) by \( x_i > 0 \). Since the entries of \( \C \) are non-negative, its absolute row sums are its row sums, so \( \norm{\C}_{\infty} \le s \) by @thm-operator-norm-formulas (b). The matrices \( \A \) and \( \C \) are similar, so they have the same characteristic polynomial (@thm-charpoly-similarity-invariant) and the same spectral radius. Hence \( \rho(\A) = \rho(\C) \le \norm{\C}_{\infty} \le s \) by @cor-spectral-radius-row-column-bound.

(b) Let \( \rho = \rho(\A) \) and let \( \w > \0 \) be a left eigenvector for \( \rho \) (@cor-left-perron-vector). Since \( \w \ge \0 \) and \( s\x - \A\x \ge \0 \), the number \( \w\tp(s\x - \A\x) \) is \( \ge 0 \). But \( \w\tp\A\x = \rho\,\w\tp\x \), so
\[
\w\tp(s\x - \A\x) = (s - \rho)\,\w\tp\x .
\]
Choose \( i \) with \( x_i > 0 \). Then \( \w\tp\x \ge w_ix_i > 0 \), so \( s - \rho \ge 0 \). If moreover \( \A\x \ne s\x \), then \( s\x - \A\x \) has some entry \( > 0 \), and pairing with \( \w > \0 \) gives \( \w\tp(s\x - \A\x) > 0 \), hence \( s - \rho > 0 \). This proves the proposition.
:::

The name comes from the inequality \( \A\x \le s\x \): the vector \( \x \) is carried into something no bigger than a multiple of itself, "sub-invariant" up to the factor \( s \).

::: {.warning}
**In part (a), the test vector must be positive unless \( \A \) is irreducible.** For \( \A = \diag(1, 5) \) and \( \x = \e_1 \), we have \( \A\x = \e_1 \le 1 \cdot \x \), yet \( \rho(\A) = 5 \). The zero entry of \( \x \) hides the second coordinate from the test entirely. Part (b) allows zero entries only because irreducibility guarantees that every coordinate is seen through \( \w > \0 \).
:::

The lower end needs no positivity at all, and it holds for every non-negative matrix.

::: {#prp-superinvariance}
[Superinvariance]

Let \( \A \in M_n(\nR) \) with \( \A \ge 0 \), let \( s \in \nR \), and let \( \x \ge \0 \), \( \x \ne \0 \), with \( \A\x \ge s\x \).

::: {.enumerate options="label=(\alph*)"}
1. Then \( \rho(\A) \ge s \).
2. If \( \A \) is irreducible and \( \A\x \ne s\x \), then \( \rho(\A) > s \).
:::
:::

::: {.idea}
For (a), the proof cannot use a similarity, because \( \x \) may have zero entries. Instead it iterates the inequality to get \( \A^k\x \ge s^k\x \), so the powers of \( \A \) grow at least like \( s^k \), and Gelfand's formula reads \( \rho(\A) \) off that growth. For (b), pair with the left Perron vector exactly as in @prp-subinvariance (b).
:::

::: {.proof}
(a) If \( s \le 0 \), then \( \rho(\A) \ge 0 \ge s \). Let \( s > 0 \). We claim that \( \A^k\x \ge s^k\x \) for every \( k \ge 0 \). The case \( k = 0 \) is an equality. If it holds for \( k \), then
\[
\A^{k+1}\x = \A(\A^k\x) \ge \A(s^k\x) = s^k\A\x \ge s^{k+1}\x ,
\]
where the first inequality holds because \( \A \ge 0 \) preserves the order, and the second multiplies \( \A\x \ge s\x \) by \( s^k > 0 \). This proves the claim.

Choose \( i \) with \( x_i = \norm{\x}_{\infty} \), which is positive since \( \x \ge \0 \) and \( \x \ne \0 \). By the claim, and @thm-operator-norm-properties (a),
\[
s^k\norm{\x}_{\infty} = s^kx_i \le (\A^k\x)_i \le \norm{\A^k\x}_{\infty} \le \norm{\A^k}_{\infty}\norm{\x}_{\infty} .
\]
Dividing by \( \norm{\x}_{\infty} > 0 \) and taking \( k \)-th roots gives \( \norm{\A^k}_{\infty}^{1/k} \ge s \) for every \( k \ge 1 \). The operator norm \( \norm{\cdot}_{\infty} \) is a matrix norm (@thm-operator-norm-properties (d)), so by Gelfand's formula (@thm-gelfand) the left side tends to \( \rho(\A) \) as \( k \to \infty \). A non-strict inequality survives the limit, so \( \rho(\A) \ge s \).

(b) Let \( \w > \0 \) be a left eigenvector of \( \A \) for \( \rho = \rho(\A) \) (@cor-left-perron-vector). As in the proof of @prp-subinvariance (b), \( \w\tp(\A\x - s\x) = (\rho - s)\,\w\tp\x \) with \( \w\tp\x > 0 \). Now \( \A\x - s\x \ge \0 \) has a positive entry, so the left side is \( > 0 \) and \( \rho > s \).
:::

::: {.remark}
For an irreducible \( \A \), part (a) also follows from the one-line pairing argument of part (b), exactly as in @prp-subinvariance (b). The detour through Gelfand's formula is what makes (a) hold for **every** non-negative matrix, where \( \w \) may have zero entries and \( \w\tp\x \) may vanish.
:::

::: {.check}
Let \( \A = \begin{pmatrix} 2 & 3 \\ 1 & 0 \end{pmatrix} \). Use \( \x = \1 \) and \( \x = (3, 1) \) to bound \( \rho(\A) \) above and below. What do you conclude?
:::

::: {.solution}
\( \A\1 = (5, 1) \), so \( \A\1 \ge 1 \cdot \1 \) and \( \A\1 \le 5 \cdot \1 \); the two propositions give \( 1 \le \rho(\A) \le 5 \). Next, \( \A(3, 1) = (9, 3) = 3 \cdot (3, 1) \), so \( 3 \le \rho(\A) \le 3 \), that is, \( \rho(\A) = 3 \). Indeed \( p_{\A}(t) = t^2 - 2t - 3 = (t - 3)(t + 1) \). A test vector that happens to be an eigenvector closes the gap completely.
:::

## The two Collatz–Wielandt functions

The propositions ask for a number \( s \) with \( \A\x \le s\x \) or \( \A\x \ge s\x \). The best such numbers for a given \( \x \) deserve names, since they are the bounds a test vector actually delivers.

::: {#def-collatz-wielandt-functions}
[Collatz–Wielandt Functions]

Let \( \A \in M_n(\nR) \) with \( \A \ge 0 \).

::: {.enumerate options="label=(\alph*)"}
1. For \( \x \ge \0 \) with \( \x \ne \0 \), the **lower Collatz–Wielandt function** is
   \[
   \underline{r}_{\A}(\x) \coloneqq \min\Bigl\{ \frac{(\A\x)_i}{x_i} : 1 \le i \le n,\ x_i > 0 \Bigr\} .
   \]
2. For \( \x > \0 \), the **upper Collatz–Wielandt function** is
   \[
   \overline{r}_{\A}(\x) \coloneqq \max\Bigl\{ \frac{(\A\x)_i}{x_i} : 1 \le i \le n \Bigr\} .
   \]
:::
:::

In words: \( \underline{r}_{\A}(\x) \) is the smallest of the ratios, taken only over the coordinates where \( \x \) is positive, and \( \overline{r}_{\A}(\x) \) is the largest of the ratios, for a vector with no zero coordinates. Both are well defined: the first set is non-empty because \( \x \ne \0 \), and both are finite sets of real numbers.

The definition is built so that
\[
\A\x \ge \underline{r}_{\A}(\x)\,\x \quad (\x \ge \0,\ \x \ne \0), \qquad
\A\x \le \overline{r}_{\A}(\x)\,\x \quad (\x > \0) .
\]
In the first, the coordinates with \( x_i > 0 \) satisfy \( (\A\x)_i \ge \underline{r}_{\A}(\x)x_i \) by the choice of the minimum, and the coordinates with \( x_i = 0 \) satisfy \( (\A\x)_i \ge 0 = \underline{r}_{\A}(\x)x_i \) because \( \A\x \ge \0 \). And \( \underline{r}_{\A}(\x) \) is the **largest** \( s \) with \( \A\x \ge s\x \), since any such \( s \) is at most each ratio; likewise \( \overline{r}_{\A}(\x) \) is the **smallest** \( s \) with \( \A\x \le s\x \).

Some examples, simplest first.

- **The all-ones vector.** \( \underline{r}_{\A}(\1) \) and \( \overline{r}_{\A}(\1) \) are the smallest and the largest row sum of \( \A \).
- **An eigenvector.** If \( \x > \0 \) and \( \A\x = \mu\x \), every ratio equals \( \mu \), so \( \underline{r}_{\A}(\x) = \overline{r}_{\A}(\x) = \mu \).
- **A standard basis vector.** \( \underline{r}_{\A}(\e_j) = a_{jj} \): only the coordinate \( j \) counts, and there the ratio is \( (\A\e_j)_j/1 = a_{jj} \).
- **The \( 1 \times 1 \) case.** For \( \A = (a) \), both functions are the constant \( a = \rho(\A) \).

**Non-example by minimal change.** Try to define \( \overline{r}_{\A} \) on vectors with zero entries in the same way as \( \underline{r}_{\A} \), as the maximum over the coordinates with \( x_i > 0 \). For the swap \( \A = \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix} \) and \( \x = \e_1 \), we get \( \A\x = \e_2 \), and the only ratio is \( 0/1 = 0 \). But \( \rho(\A) = 1 \), so this "upper bound" is \( 0 < \rho \). What fails is the inequality \( \A\x \le 0 \cdot \x \): in the ignored coordinate, \( (\A\x)_2 = 1 > 0 \). The coordinates where \( \x \) vanishes are harmless for a lower bound, where they contribute \( (\A\x)_i \ge 0 \), and fatal for an upper bound.

::: {.warning}
**The two functions are not mirror images.** The lower function accepts every non-zero \( \x \ge \0 \); the upper one accepts only \( \x > \0 \). The formula of the next subsection is therefore a maximum over the closed orthant and a minimum over the open one, and letting the minimum range over the closed orthant too would make it false, as the non-example shows.
:::

## The formula

With the two functions in hand, the propositions of the first subsection say that \( \underline{r}_{\A}(\x) \le \rho(\A) \le \overline{r}_{\A}(\x) \), and the second example shows both bounds attained at a positive eigenvector. For an irreducible matrix, such an eigenvector exists (@thm-perron-frobenius), and more is true: nothing else attains either bound.

::: {#thm-collatz-wielandt}
[Collatz–Wielandt Formula]

Let \( \A \in M_n(\nR) \) be non-negative and irreducible, with Perron vector \( \v \) (@def-perron-root-and-vectors). Then
\[
\rho(\A) = \max_{\substack{\x \ge \0 \\ \x \ne \0}} \underline{r}_{\A}(\x) = \min_{\x > \0} \overline{r}_{\A}(\x) ,
\]
both extreme values are attained at \( \x = \v \), and they are attained **only** at the positive multiples of \( \v \): if \( \x \ge \0 \), \( \x \ne \0 \) and \( \underline{r}_{\A}(\x) = \rho(\A) \), or if \( \x > \0 \) and \( \overline{r}_{\A}(\x) = \rho(\A) \), then \( \x \) is a positive multiple of \( \v \).
:::

::: {.idea}
The inequalities are the two propositions, applied with the best constants \( \underline{r}_{\A}(\x) \) and \( \overline{r}_{\A}(\x) \). Attainment is the eigenvector example. For the "only" clause, use the strict halves of the propositions: if \( \x \) attains a bound without being an eigenvector, the strict inequality would push \( \rho \) strictly past itself. The usual proofs of this formula start from the optimization problem and need a compactness argument, which is delicate for a matrix with zero entries: then \( \underline{r}_{\A} \) can jump where a coordinate of \( \x \) becomes \( 0 \), whereas for a positive matrix it is continuous. Here the compactness was spent once, in Sections 1 and 3, and it has already produced the maximizer.
:::

::: {.proof}
Let \( \rho = \rho(\A) \).

*The inequalities.* Let \( \x \ge \0 \), \( \x \ne \0 \). Since \( \A\x \ge \underline{r}_{\A}(\x)\,\x \), @prp-superinvariance (a) gives \( \underline{r}_{\A}(\x) \le \rho \). Let \( \x > \0 \). Since \( \A\x \le \overline{r}_{\A}(\x)\,\x \), @prp-subinvariance (a) gives \( \rho \le \overline{r}_{\A}(\x) \).

*Attainment.* By @thm-perron-frobenius (a) and @def-perron-root-and-vectors, \( \v > \0 \) and \( \A\v = \rho\v \), so every ratio \( (\A\v)_i/v_i \) equals \( \rho \), and \( \underline{r}_{\A}(\v) = \overline{r}_{\A}(\v) = \rho \). With the inequalities, this shows that \( \rho \) is the maximum of \( \underline{r}_{\A} \) and the minimum of \( \overline{r}_{\A} \).

*Only at multiples of \( \v \).* Let \( \x \ge \0 \), \( \x \ne \0 \), with \( \underline{r}_{\A}(\x) = \rho \), so that \( \A\x \ge \rho\x \). If \( \A\x \ne \rho\x \), then @prp-superinvariance (b) with \( s = \rho \) gives \( \rho > \rho \), which is absurd. Hence \( \A\x = \rho\x \), and \( \x \) is a positive multiple of \( \v \) by @thm-perron-frobenius (c). If instead \( \x > \0 \) and \( \overline{r}_{\A}(\x) = \rho \), then \( \A\x \le \rho\x \), and @prp-subinvariance (b) rules out \( \A\x \ne \rho\x \) in the same way. Conversely, \( \underline{r}_{\A}(c\v) = \overline{r}_{\A}(c\v) = \rho \) for \( c > 0 \), since the ratios do not change when \( \x \) is scaled. This proves the theorem.
:::

So \( \rho(\A) \) is characterized without eigenvalues: it is the largest growth factor that \( \A \) guarantees in every coordinate of some non-negative vector, and the smallest growth factor that bounds every coordinate of some positive vector.

::: {.remark}
Irreducibility is used only for the attainment of the minimum and for the "only" clause. For **every** \( \A \ge 0 \), the inequalities hold by the same two propositions, and the maximum is still attained, at the non-negative eigenvector \( \x \) of @thm-nonnegative-rho-eigenvalue: every ratio over a coordinate with \( x_i > 0 \) equals \( \rho \). The minimum can fail to be attained; Exercise C3 at the end of this section works out an example.
:::

## Row sums and column sums

The simplest test vector is \( \1 \), and the transpose supplies a second family of bounds for free. For a non-negative matrix, write \( r_i = \sum_j a_{ij} \) for the \( i \)-th row sum and \( c_j = \sum_i a_{ij} \) for the \( j \)-th column sum.

::: {#cor-row-sum-bounds-rho}
[Row and Column Sums Bound the Spectral Radius]

Let \( \A \in M_n(\nR) \) with \( \A \ge 0 \).

::: {.enumerate options="label=(\alph*)"}
1. \( \min_i r_i \le \rho(\A) \le \max_i r_i \) and \( \min_j c_j \le \rho(\A) \le \max_j c_j \).
2. If \( \A \) is irreducible, then \( \rho(\A) = \min_i r_i \) if and only if \( \rho(\A) = \max_i r_i \), if and only if all the row sums are equal. The same holds for the column sums.
:::
:::

::: {.idea}
Use the test vector \( \1 \), whose ratios are the row sums: the two propositions give (a) for rows, and the "only" clause of @thm-collatz-wielandt gives (b), since equality at \( \1 \) makes \( \1 \) an eigenvector. For columns, run the same argument on \( \A\tp \), which has the same spectral radius.
:::

::: {.proof}
(a) \( \A\1 \) is the vector of row sums, so \( \A\1 \ge (\min_i r_i)\1 \) and \( \A\1 \le (\max_i r_i)\1 \), with \( \1 > \0 \). @prp-superinvariance (a) and @prp-subinvariance (a) give the row bounds. The column sums of \( \A \) are the row sums of \( \A\tp \ge 0 \), and \( \rho(\A\tp) = \rho(\A) \) because \( p_{\A\tp} = p_{\A} \) (@prp-left-eigenvectors-transpose (b)); so the row bounds for \( \A\tp \) are the column bounds for \( \A \).

(b) If all row sums equal \( r \), then \( \min_i r_i = \max_i r_i = r \), and (a) gives \( \rho(\A) = r \). Conversely, suppose \( \rho(\A) = \min_i r_i = \underline{r}_{\A}(\1) \). By the "only" clause of @thm-collatz-wielandt, \( \1 \) is a positive multiple of the Perron vector, so \( \A\1 = \rho(\A)\1 \), and every row sum equals \( \rho(\A) \). The same argument with \( \overline{r}_{\A}(\1) = \max_i r_i \) handles the maximum. For the columns, apply this to \( \A\tp \), which is irreducible with \( \rho(\A\tp) = \rho(\A) \) by @cor-left-perron-vector (a).
:::

Compare this with Chapter 15. @cor-spectral-radius-row-column-bound gives \( \rho(\A) \le \norm{\A}_{\infty} \) and \( \rho(\A) \le \norm{\A}_1 \) for **every** complex matrix, and for \( \A \ge 0 \) these are exactly the upper bounds in (a), since the absolute row and column sums are then the row and column sums. What non-negativity adds is the **lower** bound. For a matrix with entries of both signs there is none:
\[
\M = \begin{pmatrix} 1 & -1 \\ 1 & -1 \end{pmatrix}
\]
has absolute row sums \( 2, 2 \), but \( \M^2 = 0 \), so every eigenvalue \( \lambda \) satisfies \( \lambda^2 = 0 \) and \( \rho(\M) = 0 \). Nor do the signed row sums help:
\[
\M' = \begin{pmatrix} 7 & -3 \\ 19 & -7 \end{pmatrix}
\]
has row sums \( 4 \) and \( 12 \), both larger than \( \rho(\M') = 2\sqrt2 \), since \( p_{\M'}(t) = t^2 + 8 \).

The equality clause (b) genuinely needs irreducibility. The reducible matrix \( \diag(1, 2) \) has \( \rho = 2 = \max_i r_i \) with unequal row sums, and \( \begin{psmallmatrix} 1 & 0 \\ 1 & 1 \end{psmallmatrix} \) has \( \rho = 1 = \min_i r_i \) with row sums \( 1 \) and \( 2 \).

::: {#exm-row-column-sum-bounds}
[Four bounds, and which one to keep]

Bound \( \rho(\A) \) above and below using row and column sums, for
\[
\A = \begin{pmatrix} 0 & 1 & 1 \\ 0 & 1 & 2 \\ 1 & 0 & 3 \end{pmatrix} .
\]
:::

::: {.solution}
The row sums are \( 2, 3, 4 \) and the column sums are \( 1, 2, 6 \). By @cor-row-sum-bounds-rho (a), \( 2 \le \rho(\A) \le 4 \) from the rows and \( 1 \le \rho(\A) \le 6 \) from the columns. Keep the larger lower bound and the smaller upper bound: \( 2 \le \rho(\A) \le 4 \). Chapter 15's @cor-spectral-radius-row-column-bound gives only the upper bound \( 4 \).

The matrix is irreducible: \( (\I + \A)^2 = \begin{psmallmatrix} 2 & 3 & 7 \\ 2 & 4 & 12 \\ 5 & 1 & 17 \end{psmallmatrix} > 0 \) (@thm-irreducible-power-positive). Its row sums are not all equal, so by @cor-row-sum-bounds-rho (b) both bounds are strict: \( 2 < \rho(\A) < 4 \).
:::

## Estimating the spectral radius

A bracket of width \( 2 \) is crude. The Collatz–Wielandt formula says that a better test vector gives a better bracket, and a test vector close to the Perron vector gives a very narrow one. There is a cheap way to improve a test vector: multiply it by \( \A \).

The improvement is guaranteed. Let \( \x > \0 \), and suppose \( \A\x > \0 \) too. Since \( \A \) preserves the order,
\[
\A(\A\x) \ge \A\bigl(\underline{r}_{\A}(\x)\,\x\bigr) = \underline{r}_{\A}(\x)\,\A\x ,
\]
so \( \underline{r}_{\A}(\A\x) \ge \underline{r}_{\A}(\x) \), because \( \underline{r}_{\A}(\A\x) \) is the largest \( s \) with \( \A(\A\x) \ge s\,\A\x \). In the same way \( \overline{r}_{\A}(\A\x) \le \overline{r}_{\A}(\x) \). So the brackets from \( \x, \A\x, \A^2\x, \dots \) are nested, as long as each \( \A^k\x > \0 \): each lower bound is at least the previous one, and each upper bound is at most the previous one. The condition holds whenever \( \x > \0 \) and \( \A \) is irreducible with \( n \ge 2 \), since no row of \( \A \) is then zero (a zero row, moved to the bottom by a permutation, would give the block form of @def-irreducible with \( k = n - 1 \)), so every entry of \( \A\y \) is positive when \( \y > \0 \).

::: {#exm-estimate-rho-test-vectors}
[Trapping the spectral radius]

For the matrix \( \A \) of @exm-row-column-sum-bounds, compute the brackets \( [\underline{r}_{\A}(\x), \overline{r}_{\A}(\x)] \) for \( \x = \1, \A\1, \A^2\1, \A^3\1, \A^4\1 \). Hence give \( \rho(\A) \) to two decimal places, and check the answer against the characteristic polynomial.
:::

::: {.solution}
Each step multiplies the previous vector by \( \A \), whose rows are \( (0, 1, 1) \), \( (0, 1, 2) \), \( (1, 0, 3) \). The ratios are taken coordinate by coordinate.

| \( \x \) | \( \A\x \) | ratios \( (\A\x)_i/x_i \) | bracket |
|---|---|---|---|
| \( (1, 1, 1) \) | \( (2, 3, 4) \) | \( 2,\ 3,\ 4 \) | \( [2,\ 4] \) |
| \( (2, 3, 4) \) | \( (7, 11, 14) \) | \( \tfrac72,\ \tfrac{11}{3},\ \tfrac72 \) | \( [\tfrac72,\ \tfrac{11}{3}] \) |
| \( (7, 11, 14) \) | \( (25, 39, 49) \) | \( \tfrac{25}{7},\ \tfrac{39}{11},\ \tfrac72 \) | \( [\tfrac72,\ \tfrac{25}{7}] \) |
| \( (25, 39, 49) \) | \( (88, 137, 172) \) | \( \tfrac{88}{25},\ \tfrac{137}{39},\ \tfrac{172}{49} \) | \( [\tfrac{172}{49},\ \tfrac{88}{25}] \) |
| \( (88, 137, 172) \) | \( (309, 481, 604) \) | \( \tfrac{309}{88},\ \tfrac{481}{137},\ \tfrac{151}{43} \) | \( [\tfrac{481}{137},\ \tfrac{151}{43}] \) |

For instance, in the last row \( \A(88, 137, 172) = (137 + 172,\ 137 + 344,\ 88 + 516) = (309, 481, 604) \), and \( \tfrac{604}{172} = \tfrac{151}{43} \). All five test vectors are positive, so each bracket is valid by @thm-collatz-wielandt, and they are nested, as the argument before the example predicts. The five brackets have widths \( 2 \), \( \tfrac16 \), \( \tfrac{1}{14} \), \( \tfrac{12}{1225} \) and \( \tfrac{4}{5891} \). Since \( \tfrac{481}{137} = 3.51094\ldots \) and \( \tfrac{151}{43} = 3.51162\ldots \),
\[
3.5109 < \rho(\A) < 3.5117 ,
\]
and therefore \( \rho(\A) = 3.51 \) to two decimal places.

*Check.* Expanding \( \det(t\I - \A) \) along the first column gives
\[
\begin{aligned}
p_{\A}(t) &= t\bigl((t - 1)(t - 3)\bigr) - \bigl((-1)(-2) - (-1)(t - 1)\bigr) \\
&= t^3 - 4t^2 + 2t - 1 .
\end{aligned}
\]
Exactly, \( p_{\A}(3.51) = -0.016849 < 0 \) and \( p_{\A}(3.512) = 0.004937728 > 0 \). A real polynomial that changes sign on an interval has a root there, by the intermediate value theorem, fact (A5) of Chapter 15's introduction. So \( p_{\A} \) has a real root between \( 3.51 \) and \( 3.512 \), consistent with the bracket.
:::

Two things about this computation deserve a comment. First, every number in it is a certified bound, not an approximation whose error is unknown: \( \rho(\A) \ge \tfrac{172}{49} \) is a theorem about this matrix, proved by one multiplication. Second, the iteration \( \x \mapsto \A\x \) is the power method, and Chapter 23 studies how fast it converges. Nesting alone does not make the brackets shrink to a point, as the next warning shows.

::: {.warning}
**The brackets need not close up.** For the swap \( \A = \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix} \), which is irreducible with \( \rho = 1 \), start from \( \x = (1, 2) \). Then \( \A\x = (2, 1) \), with ratios \( 2 \) and \( \tfrac12 \), and \( \A^2\x = \x \). The bracket is \( [\tfrac12, 2] \) at every step and never improves. The iteration only swaps the two coordinates, because the eigenvalue \( -1 \) has the same modulus as \( \rho \). Section 5 studies the irreducible matrices whose other eigenvalues all have modulus strictly less than \( \rho \).
:::

## Exercises

### A. Check your understanding

:::: {#exr-collatz-wielandt-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define \( \underline{r}_{\A}(\x) \) and \( \overline{r}_{\A}(\x) \), and state on which vectors each is defined.
2. For \( \A = \begin{psmallmatrix} 1 & 2 \\ 3 & 0 \end{psmallmatrix} \), compute \( \underline{r}_{\A}(\1) \) and \( \overline{r}_{\A}(\1) \). What do you conclude about \( \rho(\A) \)?
3. True or false: if \( \A \ge 0 \), \( \x \ge \0 \), \( \x \ne \0 \) and \( \A\x \le 2\x \), then \( \rho(\A) \le 2 \). Justify your answer.
4. True or false: for every \( \A \ge 0 \), \( \rho(\A) \) is at least the smallest row sum of \( \A \). Justify your answer.
5. Name the result from Chapter 15 that gives the upper bound in @cor-row-sum-bounds-rho (a), and say what that result does not give.
:::
::::

::: {.solution}
(a) See @def-collatz-wielandt-functions: \( \underline{r}_{\A}(\x) \) is the minimum of \( (\A\x)_i/x_i \) over the indices with \( x_i > 0 \), defined for \( \x \ge \0 \), \( \x \ne \0 \); \( \overline{r}_{\A}(\x) \) is the maximum of \( (\A\x)_i/x_i \) over all indices, defined only for \( \x > \0 \).

(b) \( \A\1 = (3, 3) \), so both equal \( 3 \), and \( \rho(\A) = 3 \) by @prp-superinvariance (a) and @prp-subinvariance (a). Indeed \( p_{\A}(t) = t^2 - t - 6 = (t - 3)(t + 2) \).

(c) False: \( \A = \diag(1, 5) \) and \( \x = \e_1 \) give \( \A\x = \x \le 2\x \), but \( \rho(\A) = 5 \). It becomes true if \( \x > \0 \) (@prp-subinvariance (a)) or if \( \A \) is irreducible (@prp-subinvariance (b)).

(d) True, by @cor-row-sum-bounds-rho (a), which rests on @prp-superinvariance (a) with \( \x = \1 \). No irreducibility is needed.

(e) @cor-spectral-radius-row-column-bound, which bounds \( \rho \) above by the largest absolute row sum and the largest absolute column sum of any complex matrix. It gives no lower bound, and none exists for matrices with entries of both signs: \( \begin{psmallmatrix} 1 & -1 \\ 1 & -1 \end{psmallmatrix} \) has \( \rho = 0 \).
:::

### B. Practice

:::: {#exr-collatz-wielandt-b1}
[B1: A certified bracket]

Let
\[
\A = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 3 \\ 1 & 0 & 2 \end{pmatrix} .
\]
Show that \( \A \) is irreducible. Compute the brackets \( [\underline{r}_{\A}(\x), \overline{r}_{\A}(\x)] \) for \( \x = \1 \) and for \( \x = (10, 11, 8) \). Hence show that \( 3.18 < \rho(\A) \le 3.25 \), and check this against \( p_{\A} \).
::::

::: {.solution}
*Irreducible.* \( \I + \A = \begin{psmallmatrix} 2 & 2 & 0 \\ 0 & 2 & 3 \\ 1 & 0 & 3 \end{psmallmatrix} \), and \( (\I + \A)^2 = \begin{psmallmatrix} 4 & 8 & 6 \\ 3 & 4 & 15 \\ 5 & 2 & 9 \end{psmallmatrix} > 0 \), so \( \A \) is irreducible by @thm-irreducible-power-positive.

*Brackets.* \( \A\1 = (3, 4, 3) \), giving \( [3, 4] \). Next,
\[
\A(10, 11, 8) = (10 + 22,\ 11 + 24,\ 10 + 16) = (32, 35, 26) ,
\]
with ratios \( \tfrac{32}{10} = 3.2 \), \( \tfrac{35}{11} = 3.1818\ldots \), \( \tfrac{26}{8} = 3.25 \). The bracket is \( [\tfrac{35}{11}, \tfrac{13}{4}] \). By @thm-collatz-wielandt, \( \tfrac{35}{11} \le \rho(\A) \le \tfrac{13}{4} \). Since \( \tfrac{35}{11} > 3.18 \), this gives \( 3.18 < \rho(\A) \le 3.25 \).

*Check.* Expanding along the first row,
\[
\begin{aligned}
p_{\A}(t) &= (t - 1)\bigl((t - 1)(t - 2)\bigr) + 2\bigl(0 - 3\bigr) \\
&= t^3 - 4t^2 + 5t - 8 .
\end{aligned}
\]
Then \( p_{\A}(\tfrac{35}{11}) = -\tfrac{498}{1331} < 0 \) and \( p_{\A}(\tfrac{13}{4}) = \tfrac{21}{64} > 0 \), so by the intermediate value theorem (fact (A5) of Chapter 15's introduction) \( p_{\A} \) has a root in the bracket, consistent with the estimate. (In fact \( \rho(\A) \approx 3.219 \).)
:::

:::: {#exr-collatz-wielandt-b2}
[B2: When a sum bound is exact]

For each matrix, give the bounds of @cor-row-sum-bounds-rho (a) from rows and from columns, and decide whether they determine \( \rho \). Justify your answers.
\[
\text{(a)}\ \begin{pmatrix} 1 & 2 & 1 \\ 3 & 0 & 1 \\ 0 & 2 & 2 \end{pmatrix} \qquad
\text{(b)}\ \begin{pmatrix} 1 & 3 \\ 2 & 0 \end{pmatrix} \qquad
\text{(c)}\ \begin{pmatrix} 2 & 0 \\ 5 & 3 \end{pmatrix}
\]
::::

::: {.solution}
(a) Row sums \( 4, 4, 4 \); column sums \( 4, 4, 4 \). Both bracket \( \rho \) in \( [4, 4] \), so \( \rho = 4 \), with eigenvector \( \1 \).

(b) Row sums \( 4, 2 \), giving \( [2, 4] \); column sums \( 3, 3 \), giving \( [3, 3] \). So \( \rho = 3 \), with \( \1 \) as a left eigenvector: \( \1\tp\A = (3, 3) \). Check: \( p(t) = t^2 - t - 6 = (t - 3)(t + 2) \). The matrix is irreducible (\( \I + \A > 0 \)), and the row sums are unequal, so by @cor-row-sum-bounds-rho (b) the row bracket is strict, \( 2 < 3 < 4 \), as it is.

(c) Row sums \( 2, 8 \), giving \( [2, 8] \); column sums \( 7, 3 \), giving \( [3, 7] \). Together, \( 3 \le \rho \le 7 \). The matrix is lower triangular, so its eigenvalues are \( 2 \) and \( 3 \) and \( \rho = 3 \), the smallest column sum, although the column sums are unequal. This does not contradict @cor-row-sum-bounds-rho (b): the matrix is reducible, since \( \I + \A \) has a zero entry in position \( (1, 2) \) and \( n - 1 = 1 \).
:::

:::: {#exr-collatz-wielandt-b3}
[B3: A weighted test vector]

Let
\[
\A = \frac{1}{10}\begin{pmatrix} 5 & 20 \\ 1 & 2 \end{pmatrix} .
\]
Show that neither the row sums nor the column sums prove \( \rho(\A) < 1 \). Then use the test vector \( \x = (5, 1) \) to prove \( \rho(\A) \le \tfrac{9}{10} \). Hence deduce that \( \A^k \to 0 \) as \( k \to \infty \).
::::

::: {.solution}
The row sums are \( \tfrac{25}{10} \) and \( \tfrac{3}{10} \), and the column sums \( \tfrac{6}{10} \) and \( \tfrac{22}{10} \). Each upper bound in @cor-row-sum-bounds-rho (a) exceeds \( 1 \), so neither proves \( \rho(\A) < 1 \).

With \( \x = (5, 1) > \0 \),
\[
\A\x = \tfrac{1}{10}(25 + 20,\ 5 + 2) = \bigl(\tfrac{45}{10},\ \tfrac{7}{10}\bigr) ,
\]
and the ratios are \( \tfrac{45}{50} = \tfrac{9}{10} \) and \( \tfrac{7}{10} \). So \( \A\x \le \tfrac{9}{10}\x \), and @prp-subinvariance (a) gives \( \rho(\A) \le \tfrac{9}{10} < 1 \). Hence \( \A^k \to 0 \) by @cor-powers-converge-iff-rho-lt-one (a).
:::

### C. Going deeper

:::: {#exr-collatz-wielandt-c1}
[C1: Lower bounds from single entries]

Let \( \A \in M_n(\nR) \) with \( \A \ge 0 \), not necessarily irreducible.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \rho(\A) \ge a_{ii} \) for every \( i \).
2. Prove that \( \rho(\A) \ge \sqrt{a_{ij}a_{ji}} \) for every \( i \ne j \).
3. Hence show that \( \begin{psmallmatrix} 1 & 4 & 0 \\ 9 & 2 & 0 \\ 0 & 0 & 5 \end{psmallmatrix} \) has \( \rho \ge 6 \), and check this exactly.
:::

*Hint: choose a test vector supported on \( \{i\} \) or on \( \{i, j\} \).*
::::

::: {.solution}
(a) Take \( \x = \e_i \). Then \( (\A\e_i)_i = a_{ii} \) and every other coordinate of \( \A\e_i \) is \( \ge 0 \), so \( \A\e_i \ge a_{ii}\e_i \), and @prp-superinvariance (a) gives \( \rho(\A) \ge a_{ii} \).

(b) If \( a_{ij}a_{ji} = 0 \), the claim is \( \rho(\A) \ge 0 \), which holds. Otherwise put \( s = \sqrt{a_{ij}a_{ji}} > 0 \) and \( \x = \sqrt{a_{ij}}\,\e_i + \sqrt{a_{ji}}\,\e_j \ge \0 \), \( \x \ne \0 \). Dropping non-negative terms,
\[
(\A\x)_i \ge a_{ij}\sqrt{a_{ji}} = s\sqrt{a_{ij}} = s x_i , \qquad
(\A\x)_j \ge a_{ji}\sqrt{a_{ij}} = s\sqrt{a_{ji}} = s x_j ,
\]
and the other coordinates satisfy \( (\A\x)_k \ge 0 = s x_k \). So \( \A\x \ge s\x \), and @prp-superinvariance (a) gives \( \rho(\A) \ge s \).

(c) With \( i = 1 \), \( j = 2 \): \( \sqrt{4 \cdot 9} = 6 \), so \( \rho \ge 6 \). The diagonal bound of (a) gives only \( 5 \). Exactly: the matrix is block diagonal, the \( 2 \times 2 \) block has \( p(t) = t^2 - 3t - 34 \) with roots \( \frac{3 \pm \sqrt{145}}{2} \), and the \( 1 \times 1 \) block contributes \( 5 \). So \( \rho = \frac{3 + \sqrt{145}}{2} \approx 7.52 \ge 6 \).
:::

:::: {#exr-collatz-wielandt-c2}
[C2: Strict monotonicity]

Let \( \A, \B \in M_n(\nR) \) with \( 0 \le \A \le \B \) and \( \A \ne \B \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( \A \) is irreducible, then so is \( \B \), and \( \rho(\A) < \rho(\B) \).
2. Show by an example that the strict inequality can fail if \( \A \) is reducible.
:::
::::

::: {.solution}
(a) Since \( \I + \B \ge \I + \A \ge 0 \) and a non-negative matrix preserves the order, induction on \( k \) gives \( (\I + \B)^k \ge (\I + \A)^k \): indeed \( (\I + \B)^{k+1} = (\I + \B)(\I + \B)^k \ge (\I + \B)(\I + \A)^k \ge (\I + \A)^{k+1} \), column by column. With \( k = n - 1 \), \( (\I + \B)^{n-1} \ge (\I + \A)^{n-1} > 0 \), so \( \B \) is irreducible by @thm-irreducible-power-positive.

Let \( \v > \0 \) be the Perron vector of \( \A \). Then \( \B\v = \A\v + (\B - \A)\v \ge \A\v = \rho(\A)\v \). Moreover \( \B - \A \ge 0 \) has some entry \( b_{ij} - a_{ij} > 0 \), and then \( \bigl((\B - \A)\v\bigr)_i \ge (b_{ij} - a_{ij})v_j > 0 \), so \( \B\v \ne \rho(\A)\v \). By @prp-superinvariance (b) applied to the irreducible \( \B \), \( \rho(\B) > \rho(\A) \).

(b) \( \A = \diag(1, 0) \) and \( \B = \diag(1, \tfrac12) \) satisfy \( 0 \le \A \le \B \), \( \A \ne \B \), and \( \rho(\A) = \rho(\B) = 1 \).
:::

:::: {#exr-collatz-wielandt-c3}
[C3: The minimum need not be attained]

Let \( \A = \begin{psmallmatrix} 1 & 1 \\ 0 & 1 \end{psmallmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \A \) is reducible and \( \rho(\A) = 1 \).
2. Show that \( \overline{r}_{\A}(\x) > 1 \) for every \( \x > \0 \), so that \( \min_{\x > \0}\overline{r}_{\A}(\x) \) does not exist.
3. Show that nevertheless \( \overline{r}_{\A}(\x) \) takes values as close to \( 1 \) as we like, and that \( \max_{\x \ge \0, \x \ne \0}\underline{r}_{\A}(\x) = 1 \) is attained.
:::
::::

::: {.solution}
(a) \( \I + \A = \begin{psmallmatrix} 2 & 1 \\ 0 & 2 \end{psmallmatrix} \) has a zero entry, so \( \A \) is reducible (@thm-irreducible-power-positive with \( n = 2 \)). It is triangular with diagonal \( 1, 1 \), so \( \rho(\A) = 1 \) (@thm-diagonal-of-triangular-form (b)).

(b) For \( \x = (x_1, x_2) > \0 \), \( \A\x = (x_1 + x_2,\ x_2) \), with ratios \( 1 + x_2/x_1 \) and \( 1 \). Hence \( \overline{r}_{\A}(\x) = 1 + x_2/x_1 > 1 \). Suppose some \( \x > \0 \) gave the smallest value \( m = 1 + x_2/x_1 \). Then \( \x' = (x_1, x_2/2) > \0 \) gives \( \overline{r}_{\A}(\x') = 1 + x_2/(2x_1) < m \), a contradiction. So there is no minimum.

(c) For \( \x = (1, t) \) with \( t > 0 \), \( \overline{r}_{\A}(\x) = 1 + t \), which is as close to \( 1 \) as we like. For the lower function, \( \x = \e_1 \) gives \( \A\e_1 = \e_1 \), so \( \underline{r}_{\A}(\e_1) = 1 = \rho(\A) \); since every value of \( \underline{r}_{\A} \) is \( \le \rho(\A) \) by @prp-superinvariance (a), the maximum is attained at \( \e_1 \), which is the non-negative eigenvector of @thm-nonnegative-rho-eigenvalue.
:::
