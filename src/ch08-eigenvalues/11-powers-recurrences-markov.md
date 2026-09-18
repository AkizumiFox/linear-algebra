# Powers, Recurrences and Markov Chains

Section 4 promised that diagonalization is a tool for computation, and the Fibonacci numbers gave a first taste. This section collects three situations in which a quantity evolves in discrete steps by a fixed linear rule: a vector recurrence \( \x_{k+1} = \A\x_k \), a scalar recurrence such as \( a_{k+3} = 2a_{k+2} + a_{k+1} - 2a_k \), and a system that moves at random between finitely many states. In each case the state after \( k \) steps is a matrix power applied to the starting state, and the eigenvalues decide what happens in the long run. We use only the explicit formula \( \A^k = \P \D^k\P^{-1} \) and limits of sequences of numbers, one entry at a time.

## Vector recurrences

A **linear recurrence** of first order is a rule \( \x_{k+1} = \A\x_k \) for \( k \in \nN \), with \( \A \in M_n(F) \) fixed and a starting vector \( \x_0 \in F^n \). By induction on \( k \), the unique sequence obeying the rule is \( \x_k = \A^k\x_0 \). The question is how to see this power, and diagonalization answers it by changing to coordinates in which \( \A \) acts coordinate by coordinate.

::: {#thm-linear-recurrence-solution}
[Solving a Diagonalizable Recurrence]

Let \( \A \in M_n(F) \) be diagonalizable, with \( \A = \P \D \P^{-1} \), \( \D = \diag(\lambda_1, \dots, \lambda_n) \), and let \( \v_1, \dots, \v_n \) be the columns of \( \P \). Let \( \x_0 \in F^n \), and let \( (c_1, \dots, c_n) = \P^{-1}\x_0 \), so that \( \x_0 = c_1\v_1 + \dots + c_n\v_n \). Then the sequence defined by \( \x_{k+1} = \A\x_k \) is
\[
\x_k = \A^k\x_0 = c_1\lambda_1^k\,\v_1 + c_2\lambda_2^k\,\v_2 + \dots + c_n\lambda_n^k\,\v_n \qquad (k \in \nN).
\]
:::

::: {.proof}
By induction on \( k \), \( \x_k = \A^k\x_0 \): this holds for \( k = 0 \) since \( \A^0 = \I \), and \( \x_{k+1} = \A\x_k = \A\cdot \A^k\x_0 = \A^{k+1}\x_0 \). By @thm-powers-diagonalizable, \( \A^k\x_0 = \P \D^k\P^{-1}\x_0 = \P \D^k\c \) with \( \c = (c_1, \dots, c_n) \). Now \( \D^k\c = (\lambda_1^kc_1, \dots, \lambda_n^kc_n) \), and by @thm-matrix-times-vector-columns, \( \P \) times this vector is \( \sum_i \lambda_i^kc_i\,\v_i \). Finally, \( \P\c = \x_0 \) says \( \x_0 = \sum_i c_i\v_i \), by the same result.
:::

In words: expand the starting vector in a basis of eigenvectors; each coordinate is then multiplied by its own eigenvalue at every step, independently of the others. Over \( \nR \) or \( \nC \), where absolute values are available, the long-run behavior is visible at once. Terms with \( |\lambda_i| < 1 \) die out, terms with \( |\lambda_i| > 1 \) grow, and the largest \( |\lambda_i| \) with \( c_i \ne 0 \) wins. The worked Fibonacci example (@exm-fibonacci-binet) is the case \( n = 2 \).

## Scalar recurrences and companion matrices

A recurrence such as \( a_{k+3} = 2a_{k+2} + a_{k+1} - 2a_k \) involves one number sequence but several previous terms. The trick of @exm-fibonacci-binet turns it into a vector recurrence: remember the last few terms as one vector.

Let \( n \ge 1 \) and \( c_0, \dots, c_{n-1} \in F \), and consider sequences \( (a_k)_{k \in \nN} \) in \( F \) with
\[
\begin{aligned}
a_{k+n} + c_{n-1}a_{k+n-1} + \dots + c_1a_{k+1} + c_0a_k &= 0 \\
&\qquad \text{for every } k \in \nN .
\end{aligned} \tag{$\ast$}
\]
Such a sequence is determined by its **initial values** \( a_0, \dots, a_{n-1} \), because \( (\ast) \) computes each later term from the \( n \) before it. The polynomial
\[
p(x) = x^n + c_{n-1}x^{n-1} + \dots + c_1x + c_0
\]
is called the **characteristic polynomial of the recurrence**; the name is justified below. Put \( \x_k = (a_k, a_{k+1}, \dots, a_{k+n-1}) \in F^n \). Then \( (\ast) \) says exactly \( \x_{k+1} = \C\x_k \), where
\[
\C = \begin{pmatrix} 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 1 & \cdots & 0 \\ \vdots & & & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & 1 \\ -c_0 & -c_1 & -c_2 & \cdots & -c_{n-1} \end{pmatrix}:
\]
the first \( n - 1 \) rows shift the window by one, and the last row is \( (\ast) \) solved for \( a_{k+n} \). For \( n \ge 2 \), \( \C \) is the transpose of the companion matrix \( \C(p) \) of @exr-characteristic-polynomial-c1, so \( p_{\C} = p_{\C(p)} = p \) by @exr-characteristic-polynomial-b2 and @exr-characteristic-polynomial-c1 (for \( n = 1 \), \( \C = (-c_0) \) and \( p_{\C} = x + c_0 = p \)). The eigenvalues of \( \C \) are the roots of \( p \).

::: {#thm-scalar-recurrence-distinct-roots}
[Scalar Recurrences with Distinct Roots]

Let \( n \ge 1 \), \( c_0, \dots, c_{n-1} \in F \), and suppose \( p = x^n + c_{n-1}x^{n-1} + \dots + c_0 \) has \( n \) **distinct** roots \( \lambda_1, \dots, \lambda_n \in F \). Then a sequence \( (a_k)_{k \in \nN} \) in \( F \) satisfies \( (\ast) \) if and only if there are \( b_1, \dots, b_n \in F \) with
\[
a_k = b_1\lambda_1^k + b_2\lambda_2^k + \dots + b_n\lambda_n^k \qquad \text{for every } k \in \nN .
\]
In that case \( b_1, \dots, b_n \) are uniquely determined by the initial values \( a_0, \dots, a_{n-1} \).
:::

::: {.idea}
Why powers of the roots? A geometric sequence \( a_k = \lambda^k \) satisfies \( (\ast) \) exactly when \( \lambda^k p(\lambda) = 0 \), so the roots of \( p \) give \( n \) solutions. To see that there are no others, use the matrix \( \C \): its eigenvector for \( \lambda_i \) is the window \( (1, \lambda_i, \dots, \lambda_i^{n-1}) \) of the geometric sequence, these eigenvectors form an invertible Vandermonde matrix, and @thm-linear-recurrence-solution does the rest.
:::

::: {.proof}
\( (\Leftarrow) \) For each \( i \) and \( k \), \( \lambda_i^{k+n} + c_{n-1}\lambda_i^{k+n-1} + \dots + c_0\lambda_i^k = \lambda_i^k\,p(\lambda_i) = 0 \). If \( a_k = \sum_i b_i\lambda_i^k \), then the left side of \( (\ast) \) is \( \sum_i b_i \cdot 0 = 0 \), after regrouping the finite sums.

\( (\Rightarrow) \) Let \( (a_k) \) satisfy \( (\ast) \), and let \( \x_k \) and \( \C \) be as above, so \( \x_{k+1} = \C\x_k \). For each \( i \), let \( \w_i = (1, \lambda_i, \lambda_i^2, \dots, \lambda_i^{n-1}) \). Then \( \C\w_i = \lambda_i\w_i \): for \( r \le n - 1 \), entry \( r \) of \( \C\w_i \) is entry \( r + 1 \) of \( \w_i \), which is \( \lambda_i^r = \lambda_i \cdot \lambda_i^{r-1} \); and the last entry is \( -(c_0 + c_1\lambda_i + \dots + c_{n-1}\lambda_i^{n-1}) = \lambda_i^n - p(\lambda_i) = \lambda_i^n = \lambda_i \cdot \lambda_i^{n-1} \). Let \( \W \) be the matrix with columns \( \w_1, \dots, \w_n \). Its \( (r, i) \)-entry is \( \lambda_i^{r-1} \), so \( \W = \V(\lambda_1, \dots, \lambda_n)\tp \) in the notation of @thm-vandermonde-determinant, and \( \W \) is invertible, since the \( \lambda_i \) are distinct: \( \det \W = \det \V(\lambda_1, \dots, \lambda_n) \ne 0 \) by @thm-det-transpose and @thm-vandermonde-determinant, and @thm-det-nonzero-iff-invertible applies. The columns of \( \C \W \) are \( \lambda_i\w_i \), which are the columns of \( \W\,\diag(\lambda_1, \dots, \lambda_n) \), so \( \C = \W\,\diag(\lambda_1, \dots, \lambda_n)\,\W^{-1} \).

By @thm-linear-recurrence-solution, with \( (b_1, \dots, b_n) = \W^{-1}\x_0 \),
\[
\x_k = b_1\lambda_1^k\,\w_1 + \dots + b_n\lambda_n^k\,\w_n .
\]
The first entry of \( \x_k \) is \( a_k \), and the first entry of each \( \w_i \) is \( 1 \), so \( a_k = \sum_i b_i\lambda_i^k \).

For uniqueness, suppose \( a_k = \sum_i b_i\lambda_i^k \) for all \( k \). Taking \( k = 0, \dots, n - 1 \) gives \( \W\b = (a_0, \dots, a_{n-1}) = \x_0 \), so \( \b = \W^{-1}\x_0 \) is determined by the initial values.
:::

So solving a recurrence with distinct roots comes down to three steps: find the roots of \( p \), write the general form \( \sum b_i\lambda_i^k \), and fit \( b_1, \dots, b_n \) to the initial values by solving a Vandermonde system.

::: {#exm-third-order-recurrence}
[A Third-Order Recurrence]

Find a formula for the sequence with \( a_0 = 3 \), \( a_1 = 2 \), \( a_2 = 6 \) and
\[
a_{k+3} = 2a_{k+2} + a_{k+1} - 2a_k \qquad (k \in \nN).
\]
:::

::: {.solution}
In the form \( (\ast) \), \( a_{k+3} - 2a_{k+2} - a_{k+1} + 2a_k = 0 \), so \( p(x) = x^3 - 2x^2 - x + 2 \). Grouping, \( p = x^2(x - 2) - (x - 2) = (x - 2)(x - 1)(x + 1) \), with the distinct roots \( 1, -1, 2 \). The window matrix is
\[
\C = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -2 & 1 & 2 \end{pmatrix},
\]
with eigenvectors \( (1, 1, 1) \), \( (1, -1, 1) \), \( (1, 2, 4) \); for instance \( \C(1, 2, 4) = (2, 4, -2 + 2 + 8) = 2(1, 2, 4) \).

By @thm-scalar-recurrence-distinct-roots, \( a_k = b_1 + b_2(-1)^k + b_32^k \). The initial values give the Vandermonde system
\[
b_1 + b_2 + b_3 = 3, \qquad b_1 - b_2 + 2b_3 = 2, \qquad b_1 + b_2 + 4b_3 = 6 .
\]
Subtracting the first equation from the third gives \( 3b_3 = 3 \), so \( b_3 = 1 \). Then \( b_1 + b_2 = 2 \) and \( b_1 - b_2 = 0 \), so \( b_1 = b_2 = 1 \). Hence
\[
a_k = 1 + (-1)^k + 2^k .
\]
*Check.* The recurrence gives \( a_3 = 2 \cdot 6 + 2 - 2 \cdot 3 = 8 \) and \( a_4 = 2 \cdot 8 + 6 - 2 \cdot 2 = 18 \); the formula gives \( 1 - 1 + 8 = 8 \) and \( 1 + 1 + 16 = 18 \). For large \( k \), \( a_k \approx 2^k \): the root of largest absolute value dominates.
:::

**Repeated roots.** When \( p \) has a repeated root, \( \C \) is not diagonalizable: for a root \( \lambda \), every eigenvector \( (w_1, \dots, w_n) \) of \( \C \) satisfies \( w_{r+1} = \lambda w_r \), so it is a multiple of \( (1, \lambda, \dots, \lambda^{n-1}) \), and \( g_{\C}(\lambda) = 1 \) whatever \( a_{\C}(\lambda) \) is. The general answer involves terms \( k\lambda^k, k^2\lambda^k, \dots \), and it follows from the Jordan canonical form of Chapter 9. The \( 2 \times 2 \) case can be done by hand.

::: {#exm-repeated-root-recurrence}
[A Repeated Root]

Over \( \nR \), find all sequences with \( a_{k+2} = 4a_{k+1} - 4a_k \) for every \( k \in \nN \).
:::

::: {.solution}
Here \( p = x^2 - 4x + 4 = (x - 2)^2 \), and the window matrix is \( \C = \begin{pmatrix} 0 & 1 \\ -4 & 4 \end{pmatrix} \). It is not diagonalizable, since \( \C - 2\I = \begin{pmatrix} -2 & 1 \\ -4 & 2 \end{pmatrix} \) has rank \( 1 \), so \( g(2) = 1 < 2 = a(2) \). But \( \N = \C - 2\I \) satisfies
\[
\N^2 = \begin{pmatrix} 4 - 4 & -2 + 2 \\ 8 - 8 & -4 + 4 \end{pmatrix} = 0 .
\]
*Claim:* \( \C^k = 2^k\I + k2^{k-1}\N \) for all \( k \in \nN \). For \( k = 0 \) both sides are \( \I \). If it holds for \( k \), then, since \( \C = 2\I + \N \) and \( \N^2 = 0 \),
\[
\begin{aligned}
\C^{k+1} &= \big(2^k\I + k2^{k-1}\N\big)(2\I + \N) \\
  &= 2^{k+1}\I + 2^k\N + k2^k\N + k2^{k-1}\N^2 = 2^{k+1}\I + (k + 1)2^k\N .
\end{aligned}

\]
Now \( \x_k = \C^k\x_0 \) with \( \x_0 = (a_0, a_1) \), and \( a_k \) is the first entry. Row \( 1 \) of \( \C^k \) is \( \big(2^k - 2k2^{k-1},\ k2^{k-1}\big) = \big((1 - k)2^k,\ k2^{k-1}\big) \), so
\[
a_k = (1 - k)2^ka_0 + k2^{k-1}a_1 = \Big(a_0 + \big(\tfrac{a_1}{2} - a_0\big)k\Big)2^k .
\]
So the solutions are exactly the sequences \( a_k = (b_1 + b_2k)2^k \) with \( b_1, b_2 \in \nR \): every solution has this form with \( b_1 = a_0 \), \( b_2 = a_1/2 - a_0 \), and every such sequence is the solution with \( a_0 = b_1 \), \( a_1 = 2b_1 + 2b_2 \). For example, \( a_0 = 1 \), \( a_1 = 4 \) gives \( a_k = (1 + k)2^k \), and indeed \( a_2 = 4 \cdot 4 - 4 \cdot 1 = 12 = 3 \cdot 4 \). The new term \( k2^k \) is the footprint of the missing eigenvector, just as the entry \( k \) was for \( \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}^k \) in Section 4.
:::

## Stochastic matrices

Now a system that moves at random. A shared bicycle is parked each night at one of a few stations; a machine is either working or under repair. We do not know the state for sure, but we know the probability of each state, and a fixed table of probabilities for moving from one state to another in one step.

Take states \( 1, \dots, n \). Record the probabilities of the states at step \( k \) as a column \( \x_k \in \nR^n \), and let \( a_{ij} \) be the probability of moving to state \( i \) in one step, given that the system is in state \( j \). The probability of being in state \( i \) at step \( k + 1 \) is the sum over the previous state \( j \) of "was in \( j \)" times "moved from \( j \) to \( i \)", that is, \( \sum_j a_{ij}(\x_k)_j \). So \( \x_{k+1} = \A\x_k \): a linear recurrence. The matrix \( \A \) has two features: its entries are probabilities, and from each state \( j \) the system must go **somewhere**, so column \( j \) adds up to \( 1 \).

*A stochastic matrix is a table of transition probabilities, one column for each starting state.*

::: {#def-stochastic-matrix}
[Stochastic Matrix, Probability Vector]

Let \( n \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. A vector \( \x \in \nR^n \) is a **probability vector** if \( x_i \ge 0 \) for every \( i \) and \( x_1 + \dots + x_n = 1 \).
2. A matrix \( \A \in M_n(\nR) \) is **stochastic** if every column of \( \A \) is a probability vector: \( a_{ij} \ge 0 \) for **all** \( i, j \), and \( \sum_{i=1}^{n} a_{ij} = 1 \) for **every** \( j \).
:::
:::

In words: the entries are non-negative and each **column** sums to \( 1 \). With \( \1 = (1, \dots, 1) \in \nR^n \), the column condition reads \( \1\tp \A = \1\tp \), and \( \1\tp\x = 1 \) says that the entries of \( \x \) add up to \( 1 \).

**Examples.**

- \( \begin{pmatrix} 9/10 & 1/5 \\ 1/10 & 4/5 \end{pmatrix} \): columns \( (9/10, 1/10) \) and \( (1/5, 4/5) \) are probability vectors.
- **Degenerate cases.** \( \I_n \) is stochastic: every state stays put. The \( 1 \times 1 \) matrix \( (1) \) is the only \( 1 \times 1 \) stochastic matrix. Every **permutation matrix** is stochastic, since each column is a standard basis vector; it moves the system deterministically.
- \( \frac14\begin{pmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 1 & 1 & 3 \end{pmatrix} \): the columns sum to \( \frac44 \), and all entries are non-negative.

**Non-example by minimal change.** Transpose the first example: \( \begin{pmatrix} 9/10 & 1/10 \\ 1/5 & 4/5 \end{pmatrix} \) still has non-negative entries, and its **rows** sum to \( 1 \), but its first column sums to \( 11/10 \). It fails the column condition. Likewise \( \begin{pmatrix} 3/2 & 0 \\ -1/2 & 1 \end{pmatrix} \) has columns summing to \( 1 \) but a negative entry.

**Why this convention.** Many books write probability vectors as **rows** and multiply on the left, \( \x_{k+1}\tp = \x_k\tp \M \); their "stochastic" matrices have rows summing to \( 1 \), and they are the transposes of ours. We keep column vectors and \( \x_{k+1} = \A\x_k \), in line with the rest of the book, so our stochastic matrices are **column-stochastic**. Translating between the conventions is a transpose, which changes neither eigenvalues nor their algebraic multiplicities (@prp-left-eigenvectors-transpose).

The first properties follow from \( \1\tp \A = \1\tp \).

::: {#prp-stochastic-properties}
[Basic Properties of Stochastic Matrices]

Let \( \A, \B \in M_n(\nR) \) be stochastic and \( \x \in \nR^n \) a probability vector. Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \A\x \) is a probability vector;
2. \( \A \B \) is stochastic, and so is \( \A^k \) for every \( k \in \nN \);
3. \( \1 \) is a left eigenvector of \( \A \) for the eigenvalue \( 1 \); in particular \( 1 \in \spec(\A) \).
:::
:::

::: {.proof}
(a) Each entry \( (\A\x)_i = \sum_j a_{ij}x_j \) is a sum of products of non-negative numbers, so it is non-negative. By associativity, \( \1\tp(\A\x) = (\1\tp \A)\x = \1\tp\x = 1 \).

(b) By @thm-three-views-of-product, column \( j \) of \( \A \B \) is \( \A\b_j \), where \( \b_j \) is column \( j \) of \( \B \), a probability vector. By (a), \( \A\b_j \) is a probability vector, so \( \A \B \) is stochastic. By induction on \( k \), \( \A^k \) is stochastic: \( \A^0 = \I \) is, and \( \A^{k+1} = \A^k\A \).

(c) \( \1\tp \A = \1\tp \) with \( \1 \ne \0 \) is @def-left-eigenvector with \( \lambda = 1 \), and @prp-left-eigenvectors-transpose gives \( 1 \in \spec(\A) \).
:::

::: {.warning}
**The all-ones vector is a left eigenvector, not a right one.** For \( \A = \begin{pmatrix} 9/10 & 1/5 \\ 1/10 & 4/5 \end{pmatrix} \), \( \A\1 = (11/10, 9/10) \ne \1 \). The right eigenvectors for \( 1 \) are the multiples of \( (2, 1) \), and they carry the interesting information: the long-run probabilities. Only when the **rows** also sum to \( 1 \) is \( \1 \) a right eigenvector.
:::

## Markov chains

::: {#def-markov-chain}
[Markov Chain, Steady State]

Let \( \A \in M_n(\nR) \) be stochastic. The **Markov chain** with **transition matrix** \( \A \) and initial probability vector \( \x_0 \) is the sequence of probability vectors \( \x_{k+1} = \A\x_k \), that is, \( \x_k = \A^k\x_0 \). A **steady state** of \( \A \) is a probability vector \( \v \) with \( \A\v = \v \).
:::

Each \( \x_k \) is a probability vector by @prp-stochastic-properties. A steady state is a right eigenvector for the eigenvalue \( 1 \), scaled so that its entries add up to \( 1 \) and required to have non-negative entries; if the chain starts there, it stays there.

To talk about the long run we need limits, and we use the simplest kind. A sequence of complex matrices \( \M_k \in M_{m \times n}(\nC) \) **converges entrywise** to \( \M \) if, for every position \( (r, s) \), the number sequence \( (\M_k)_{rs} \) converges to \( \M_{rs} \). We use four facts about sequences of complex numbers from calculus: sums and constant multiples of convergent sequences converge to the sums and multiples of the limits; \( z_k \to 0 \) if and only if \( |z_k| \to 0 \); \( r^k \to 0 \) for real \( 0 \le r < 1 \); and a convergent sequence of real numbers \( \ge 0 \) has a real limit \( \ge 0 \). In particular, if \( |\lambda| < 1 \), then \( |\lambda^k| = |\lambda|^k \to 0 \) (@thm-conjugate-properties), so \( \lambda^k \to 0 \).

::: {#exm-two-state-markov}
[A Two-State Chain]

A machine is either working (state \( 1 \)) or under repair (state \( 2 \)) each day. A working machine is still working the next day with probability \( 9/10 \); a machine under repair is back to work the next day with probability \( 1/5 \). So the transition matrix is
\[
\A = \begin{pmatrix} 9/10 & 1/5 \\ 1/10 & 4/5 \end{pmatrix}.
\]
Find \( \A^k \), its entrywise limit, and the long-run probability that the machine is working, if it is working on day \( 0 \).
:::

::: {.solution}
*Eigenvalues.* \( \tr \A = 17/10 \) and \( \det \A = 36/50 - 1/50 = 7/10 \), so, by the \( 2 \times 2 \) formula \( p_{\A} = x^2 - (\tr \A)x + \det \A \) (the examples after @def-characteristic-polynomial), \( p_{\A} = x^2 - \frac{17}{10}x + \frac{7}{10} = (x - 1)\big(x - \frac{7}{10}\big) \). The eigenvalue \( 1 \) was guaranteed by @prp-stochastic-properties.

*Eigenvectors.* \( \A - \I = \begin{pmatrix} -1/10 & 1/5 \\ 1/10 & -1/5 \end{pmatrix} \) gives \( x = 2y \), eigenvector \( (2, 1) \). \( \A - \frac{7}{10}\I = \begin{pmatrix} 1/5 & 1/5 \\ 1/10 & 1/10 \end{pmatrix} \) gives \( y = -x \), eigenvector \( (1, -1) \). The eigenvalues are distinct, so
\[
\P = \begin{pmatrix} 2 & 1 \\ 1 & -1 \end{pmatrix}, \qquad \D = \diag\big(1, \tfrac{7}{10}\big), \qquad \P^{-1} = \frac13\begin{pmatrix} 1 & 1 \\ 1 & -2 \end{pmatrix},
\]
using @thm-two-by-two-inverse with \( \det \P = -3 \).

*Powers.* By @thm-powers-diagonalizable, writing \( t = (7/10)^k \),
\[
\A^k = \P\begin{pmatrix} 1 & 0 \\ 0 & t \end{pmatrix}\P^{-1} = \frac13\begin{pmatrix} 2 & t \\ 1 & -t \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 1 & -2 \end{pmatrix} = \frac13\begin{pmatrix} 2 + t & 2 - 2t \\ 1 - t & 1 + 2t \end{pmatrix}.
\]
*Check:* for \( k = 1 \), \( t = 7/10 \) and \( \frac13\begin{pmatrix} 27/10 & 6/10 \\ 3/10 & 24/10 \end{pmatrix} = \A \); each column of \( \A^k \) sums to \( 1 \), as @prp-stochastic-properties requires.

*The limit.* Since \( 0 \le 7/10 < 1 \), \( t \to 0 \), so entrywise
\[
\A^k \to \frac13\begin{pmatrix} 2 & 2 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 2/3 \\ 1/3 \end{pmatrix}\begin{pmatrix} 1 & 1 \end{pmatrix}.
\]
Starting from \( \x_0 = \e_1 \), \( \x_k = \A^k\e_1 = \big(\frac{2 + t}{3}, \frac{1 - t}{3}\big) \to \big(\frac23, \frac13\big) \). In the long run the machine works on two days out of three. The limit does not depend on the start: for any probability vector \( \x_0 = (s, 1 - s) \), \( \A^k\x_0 \to \frac13(2s + 2(1 - s),\ s + (1 - s)) = (\frac23, \frac13) \). The vector \( \v = (\frac23, \frac13) \) is the steady state, the eigenvector \( (2, 1) \) scaled to sum \( 1 \).
:::

The example shows the general mechanism. The eigenvalue \( 1 \) survives in \( \D^k \), all others fade, and the surviving rank-one piece is (right eigenvector for \( 1 \)) times (left eigenvector for \( 1 \)), which for a stochastic matrix is the steady state times \( \1\tp \).

::: {#thm-markov-limit-diagonalizable}
[Long-Run Behavior of a Diagonalizable Markov Chain]

Let \( \A \in M_n(\nR) \), \( n \ge 1 \), be stochastic. Suppose that \( \A \) is diagonalizable over \( \nC \), that \( a_{\A}(1) = 1 \), and that every other eigenvalue \( \lambda \in \nC \) of \( \A \) has \( |\lambda| < 1 \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \A \) has exactly one steady state \( \v \);
2. \( \A^k \to \v\1\tp \) entrywise as \( k \to \infty \);
3. for every probability vector \( \x_0 \), the Markov chain \( \x_k = \A^k\x_0 \) converges entrywise to \( \v \).
:::
:::

::: {.idea}
Use the expansion \( \A^k = \sum_i \lambda_i^k\,\v_i\y_i\tp \) of Section 10. The terms with \( |\lambda_i| < 1 \) tend to \( 0 \), which leaves the single term for \( \lambda_1 = 1 \). Its left eigenvector \( \y_1 \) must be a multiple of \( \1 \), because the left eigenvectors for \( 1 \) form a line and \( \1 \) is one of them. Rescaling turns \( \v_1\y_1\tp \) into \( \v\1\tp \), and the non-negativity of \( \v \) comes for free as a limit of non-negative entries.
:::

::: {.proof}
Since \( \A \) is diagonalizable over \( \nC \), there are an invertible \( \P \in M_n(\nC) \) and \( \D = \diag(\lambda_1, \dots, \lambda_n) \) with \( \A = \P \D \P^{-1} \). A diagonal matrix is upper triangular, so each eigenvalue occurs on the diagonal of \( \D \) as often as its algebraic multiplicity (@thm-diagonal-of-triangular-form (b)); in particular \( 1 \) occurs exactly once, because \( a_{\A}(1) = 1 \). Permuting the columns of \( \P \) and the diagonal entries of \( \D \) together leaves \( \A = \P \D \P^{-1} \) intact, so we may assume \( \lambda_1 = 1 \), and then \( |\lambda_i| < 1 \) for \( i \ge 2 \) by hypothesis. Let \( \v_i \) be the columns of \( \P \) and \( \y_i\tp \) the rows of \( \P^{-1} \). By @prp-left-right-eigen-expansion, for every \( k \),
\[
\A^k = \v_1\y_1\tp + \sum_{i=2}^{n} \lambda_i^k\,\v_i\y_i\tp .
\]
Each entry of the sum is \( \sum_{i \ge 2} \lambda_i^k\,z_i \) for fixed complex numbers \( z_i \), and \( \lambda_i^k \to 0 \) for \( i \ge 2 \). Hence \( \A^k \to \L = \v_1\y_1\tp \) entrywise.

*The shape of \( \L \).* By @prp-left-right-eigen-expansion, \( \y_1 \) is a left eigenvector for \( 1 \), and so is \( \1 \) (@prp-stochastic-properties). Both lie in \( E_1(\A\tp) \subseteq \nC^n \) (@prp-left-eigenvectors-transpose (a)), which has dimension \( g_{\A\tp}(1) = g_{\A}(1) \le a_{\A}(1) = 1 \) by @prp-left-eigenvectors-transpose (b) and @thm-geometric-le-algebraic. Since \( \1 \ne \0 \), \( \y_1 = c\1 \) for some \( c \in \nC \). Put \( \v = c\v_1 \). Then \( \L = \v\1\tp \), \( \A\v = c\,\A\v_1 = \v \), and \( \1\tp\v = \y_1\tp\v_1 = 1 \) by @prp-left-right-eigen-expansion (b).

*\( \v \) is a steady state.* Column \( 1 \) of \( \L = \v\1\tp \) is \( \v \). It is the limit of column \( 1 \) of \( \A^k \), and \( \A^k \) is stochastic (@prp-stochastic-properties), so every entry of \( \v \) is a limit of real numbers \( \ge 0 \), hence real and \( \ge 0 \). With \( \1\tp\v = 1 \), \( \v \) is a probability vector, and \( \A\v = \v \).

*Uniqueness.* If \( \w \) is a steady state, then \( \w \in E_1(\A) \), a subspace of \( \nC^n \) of dimension \( g_{\A}(1) \le 1 \) that contains \( \v \ne \0 \). So \( \w = s\v \) for some \( s \in \nC \), and \( 1 = \1\tp\w = s\,\1\tp\v = s \). Hence \( \w = \v \). This proves (a) and (b).

(c) Entry \( r \) of \( \A^k\x_0 \) is \( \sum_s (\A^k)_{rs}(\x_0)_s \), which by (b) converges to \( \sum_s v_r(\x_0)_s = v_r\,(\1\tp\x_0) = v_r \).
:::

In practice: find the eigenvalues, check the hypotheses, and compute \( \v \) by solving \( (\A - \I)\v = \0 \) and scaling. Then (c) gives the long run **without** computing \( \P^{-1} \) at all.

::: {#exm-three-state-markov}
[Bicycles at Three Stations]

A shared bicycle is parked each night at station \( 1 \), \( 2 \) or \( 3 \). The transition matrix is
\[
\A = \frac14\begin{pmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 1 & 1 & 3 \end{pmatrix};
\]
for instance a bicycle at station \( 3 \) stays there with probability \( 3/4 \) and never goes to station \( 1 \) in one night. Find \( \A^k \), its limit, and the long-run distribution of the bicycle.
:::

::: {.solution}
*Eigenvectors.* We check three candidates:
\[
\A\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} = \frac14\begin{pmatrix} 4 \\ 8 \\ 12 \end{pmatrix}, \qquad
\A\begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix} = \frac14\begin{pmatrix} -2 \\ 0 \\ 2 \end{pmatrix}, \qquad
\A\begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix} = \frac14\begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix}.
\]
So \( 1, \frac12, \frac14 \) are eigenvalues, with eigenvectors \( \v_1 = (1, 2, 3) \), \( \v_2 = (-1, 0, 1) \), \( \v_3 = (-1, 1, 0) \). A \( 3 \times 3 \) matrix has at most three eigenvalues (@cor-eigenspaces-direct-sum), so these are all; they are distinct, so \( \A \) is diagonalizable (@cor-distinct-eigenvalues-diagonalizable) and \( a_{\A}(1) = 1 \). As a check, \( \tr \A = \frac74 = 1 + \frac12 + \frac14 \). The hypotheses of @thm-markov-limit-diagonalizable hold.

*The expansion.* With \( \P = \begin{pmatrix} 1 & -1 & -1 \\ 2 & 0 & 1 \\ 3 & 1 & 0 \end{pmatrix} \), whose determinant is \( -6 \),
\[
\P^{-1} = \begin{pmatrix} 1/6 & 1/6 & 1/6 \\ -1/2 & -1/2 & 1/2 \\ -1/3 & 2/3 & -1/3 \end{pmatrix},
\]
as multiplying out \( \P^{-1}\P = \I \) confirms. The first row is \( \frac16\1\tp \), a multiple of \( \1\tp \) as the proof of the theorem predicts. By @prp-left-right-eigen-expansion,
\[
\A^k = \frac16\begin{pmatrix} 1 & 1 & 1 \\ 2 & 2 & 2 \\ 3 & 3 & 3 \end{pmatrix} + \frac{1}{2^{k}}\cdot\frac12\begin{pmatrix} 1 & 1 & -1 \\ 0 & 0 & 0 \\ -1 & -1 & 1 \end{pmatrix} + \frac{1}{4^{k}}\cdot\frac13\begin{pmatrix} 1 & -2 & 1 \\ -1 & 2 & -1 \\ 0 & 0 & 0 \end{pmatrix}.
\]
For example, the \( (1, 1) \)-entry of \( \A^k \) is \( \frac16 + \frac12\cdot 2^{-k} + \frac13\cdot 4^{-k} \), which is \( 1 \) for \( k = 0 \) and \( \frac16 + \frac14 + \frac1{12} = \frac12 \) for \( k = 1 \), matching \( a_{11} = 2/4 \).

*The limit.* As \( k \to \infty \), \( 2^{-k} \to 0 \) and \( 4^{-k} \to 0 \), so
\[
\A^k \to \frac16\begin{pmatrix} 1 & 1 & 1 \\ 2 & 2 & 2 \\ 3 & 3 & 3 \end{pmatrix} = \v\1\tp, \qquad \v = \Big(\frac16, \frac13, \frac12\Big).
\]
Wherever the bicycle starts, in the long run it is at station \( 1 \), \( 2 \), \( 3 \) with probabilities \( \frac16, \frac13, \frac12 \). Directly, \( \v = \frac16\v_1 \) and \( \A\v = \v \). The slowest-fading term is the one with \( \frac12 \): each entry's gap to its limit roughly halves every night.
:::

::: {.warning}
**A stochastic matrix need not have convergent powers.** The swap \( \S = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) is stochastic, and \( \S^k \) is \( \I \) for even \( k \) and \( \S \) for odd \( k \), so \( \S^k \) does not converge. Starting from \( \x_0 = \e_1 \), the chain alternates \( \e_1, \e_2, \e_1, \dots \) forever, although \( \S \) has the steady state \( (\frac12, \frac12) \). The theorem does not apply: \( \S \) has the eigenvalue \( -1 \), with \( |-1| = 1 \). At the other extreme, \( \I_2 \) has convergent powers, but \( a(1) = 2 \), every probability vector is a steady state, and the limit of \( \x_k \) depends on \( \x_0 \).
:::

Chapter 18 proves the Perron–Frobenius theorem, which gives the conclusions of @thm-markov-limit-diagonalizable for every stochastic matrix with some power having all entries positive, without assuming diagonalizability and without computing eigenvalues. The exercises prove the first ingredient: no eigenvalue of a stochastic matrix has \( |\lambda| > 1 \).

::: {.check}
Is \( \A = \begin{pmatrix} 1/2 & 1/3 \\ 1/2 & 2/3 \end{pmatrix} \) stochastic? If so, find its steady state.
:::

::: {.solution}
Yes: the entries are non-negative and the columns sum to \( 1 \). From \( (\A - \I)\v = \0 \), the first row gives \( -\frac12v_1 + \frac13v_2 = 0 \), so \( v_2 = \frac32v_1 \). Scaling to sum \( 1 \): \( v_1 + \frac32v_1 = 1 \) gives \( \v = (\frac25, \frac35) \). (The eigenvalues are \( 1 \) and \( \tr \A - 1 = \frac16 \); they are distinct, so \( \A \) is diagonalizable with \( a_{\A}(1) = 1 \), and \( \v \) is the only steady state and the long-run distribution, by @thm-markov-limit-diagonalizable.)
:::

## A population model

Not every matrix of this kind is stochastic. In a population divided into age classes, individuals are born, age, and die, and the total need not be preserved. A **Leslie matrix** records, in its first row, the average number of offspring per individual of each age class, and just below the diagonal, the fraction surviving into the next class. The population vector evolves by \( \x_{k+1} = \L\x_k \), and @thm-linear-recurrence-solution describes the long run.

::: {#exm-leslie-population}
[Three Age Classes]

A species is counted once a year in three age classes: young, juvenile and adult. Half of the young survive to become juveniles, and half of the juveniles survive to become adults; no adult survives another year. Each juvenile has on average \( 7/2 \) offspring and each adult \( 3 \). The Leslie matrix is
\[
\L = \begin{pmatrix} 0 & 7/2 & 3 \\ 1/2 & 0 & 0 \\ 0 & 1/2 & 0 \end{pmatrix}.
\]
Starting from \( \x_0 = (20, 10, 5) \) (in hundreds of animals), find \( \x_k \) and describe the long-run growth and age distribution.
:::

::: {.solution}
*Characteristic polynomial.* Expanding \( \det(x\I - \L) \) along the first column,
\[
\begin{aligned}
p_{\L} &= x\det\begin{pmatrix} x & 0 \\ -1/2 & x \end{pmatrix} + \frac12\det\begin{pmatrix} -7/2 & -3 \\ -1/2 & x \end{pmatrix} \\
  &= x^3 + \frac12\Big(-\frac72x - \frac32\Big) = x^3 - \frac74x - \frac34 .
\end{aligned}
\]
Trying simple values, \( p_{\L}(-1) = -1 + \frac74 - \frac34 = 0 \), and dividing, \( p_{\L} = (x + 1)\big(x^2 - x - \frac34\big) = (x + 1)\big(x - \frac32\big)\big(x + \frac12\big) \). The eigenvalues \( \frac32, -1, -\frac12 \) are distinct, so \( \L \) is diagonalizable.

*Eigenvectors.* \( \L(w_1, w_2, w_3) = \lambda(w_1, w_2, w_3) \) forces \( \frac12w_1 = \lambda w_2 \) and \( \frac12w_2 = \lambda w_3 \), so taking \( w_3 = 1 \) gives \( w_2 = 2\lambda \), \( w_1 = 4\lambda^2 \). Hence, after scaling,
\[
\lambda = \tfrac32:\ (9, 3, 1), \qquad \lambda = -1:\ (4, -2, 1), \qquad \lambda = -\tfrac12:\ (1, -1, 1).
\]
For instance \( \L(9, 3, 1) = \big(\frac{21}{2} + 3, \frac92, \frac32\big) = \frac32(9, 3, 1) \).

*The initial vector.* Solving \( c_1(9, 3, 1) + c_2(4, -2, 1) + c_3(1, -1, 1) = (20, 10, 5) \) gives \( c_1 = 3 \), \( c_2 = -3 \), \( c_3 = 5 \): indeed \( (27 - 12 + 5,\ 9 + 6 - 5,\ 3 - 3 + 5) = (20, 10, 5) \). By @thm-linear-recurrence-solution,
\[
\x_k = 3\Big(\frac32\Big)^k\begin{pmatrix} 9 \\ 3 \\ 1 \end{pmatrix} - 3(-1)^k\begin{pmatrix} 4 \\ -2 \\ 1 \end{pmatrix} + 5\Big(-\frac12\Big)^k\begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}.
\]
*Check.* For \( k = 1 \): \( \big(\frac{81}{2} + 12 - \frac52,\ \frac{27}{2} - 6 + \frac52,\ \frac92 + 3 - \frac52\big) = (50, 10, 5) \), and directly \( \L\x_0 = (35 + 15, 10, 5) \).

*The long run.* Divide by \( (3/2)^k \):
\[
\Big(\frac23\Big)^k\x_k = 3\begin{pmatrix} 9 \\ 3 \\ 1 \end{pmatrix} - 3\Big(-\frac23\Big)^k\begin{pmatrix} 4 \\ -2 \\ 1 \end{pmatrix} + 5\Big(-\frac13\Big)^k\begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} \longrightarrow \begin{pmatrix} 27 \\ 9 \\ 3 \end{pmatrix},
\]
since \( |{-\frac23}| < 1 \) and \( |{-\frac13}| < 1 \). So the population eventually grows by the factor \( \frac32 \) each year, and the age classes approach the proportions \( 9 : 3 : 1 \), the entries of the eigenvector for the largest eigenvalue. The eigenvalue \( -1 \) makes the population oscillate from year to year, but its effect is bounded while the dominant term grows, so its share fades.
:::

## Exercises

### A. Check your understanding

:::: {#exr-powers-recurrences-markov-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define a stochastic matrix, and say which convention (rows or columns) this book uses.
2. True or false: for every stochastic \( \A \), the powers \( \A^k \) converge entrywise. Justify your answer.
3. True or false: \( \1 \) is a right eigenvector of every stochastic matrix. Justify your answer.
4. True or false: every stochastic matrix is invertible. Justify your answer.
5. Write down the general solution of \( a_{k+2} = 5a_{k+1} - 6a_k \) over \( \nR \).
6. In @thm-linear-recurrence-solution, what are the numbers \( c_1, \dots, c_n \)?
:::
::::

::: {.solution}
(a) \( \A \in M_n(\nR) \) is stochastic if all entries are non-negative and every **column** sums to \( 1 \) (@def-stochastic-matrix). This book uses columns, with \( \x_{k+1} = \A\x_k \).

(b) False. The swap \( \S = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) has \( \S^k \) alternating between \( \I \) and \( \S \).

(c) False. \( \A = \begin{pmatrix} 1 & 1/2 \\ 0 & 1/2 \end{pmatrix} \) is stochastic, and \( \A\1 = (3/2, 1/2) \) is not a multiple of \( \1 \). It is a **left** eigenvector (@prp-stochastic-properties).

(d) False. \( \begin{pmatrix} 1/2 & 1/2 \\ 1/2 & 1/2 \end{pmatrix} \) is stochastic with determinant \( 0 \).

(e) \( p = x^2 - 5x + 6 = (x - 2)(x - 3) \), so by @thm-scalar-recurrence-distinct-roots the solutions are \( a_k = b_12^k + b_23^k \) with \( b_1, b_2 \in \nR \).

(f) The coordinates of \( \x_0 \) in the basis of eigenvectors \( \v_1, \dots, \v_n \): \( (c_1, \dots, c_n) = \P^{-1}\x_0 \).
:::

### B. Practice

:::: {#exr-powers-recurrences-markov-b1}
[B1: Two recurrences]

::: {.enumerate options="label=(\alph*)"}
1. Solve \( a_{k+2} = a_{k+1} + 2a_k \) with \( a_0 = 0 \), \( a_1 = 3 \).
2. Solve \( a_{k+2} = 6a_{k+1} - 9a_k \) with \( a_0 = 1 \), \( a_1 = 6 \), by the method of @exm-repeated-root-recurrence.
:::
::::

::: {.solution}
(a) \( p = x^2 - x - 2 = (x - 2)(x + 1) \) has distinct roots, so by @thm-scalar-recurrence-distinct-roots, \( a_k = b_12^k + b_2(-1)^k \). From \( a_0 = b_1 + b_2 = 0 \) and \( a_1 = 2b_1 - b_2 = 3 \), \( 3b_1 = 3 \), so \( b_1 = 1 \), \( b_2 = -1 \). Hence \( a_k = 2^k - (-1)^k \). Check: \( a_2 = 3 + 0 = 3 = 4 - 1 \), \( a_3 = 3 + 6 = 9 = 8 + 1 \).

(b) The window matrix is \( \C = \begin{pmatrix} 0 & 1 \\ -9 & 6 \end{pmatrix} \), with \( p = (x - 3)^2 \). Put \( \N = \C - 3\I = \begin{pmatrix} -3 & 1 \\ -9 & 3 \end{pmatrix} \); then \( \N^2 = \begin{pmatrix} 9 - 9 & -3 + 3 \\ 27 - 27 & -9 + 9 \end{pmatrix} = 0 \). As in the example, by induction \( \C^k = 3^k\I + k3^{k-1}\N \): the step is \( (3^k\I + k3^{k-1}\N)(3\I + \N) = 3^{k+1}\I + 3^k\N + k3^k\N \). Row \( 1 \) of \( \C^k \) is \( \big(3^k - 3k3^{k-1},\ k3^{k-1}\big) = \big((1 - k)3^k,\ k3^{k-1}\big) \), so
\[
a_k = (1 - k)3^k \cdot 1 + k3^{k-1}\cdot 6 = (1 - k + 2k)3^k = (1 + k)3^k .
\]
Check: \( a_2 = 36 - 9 = 27 = 3 \cdot 9 \), \( a_3 = 6 \cdot 27 - 9 \cdot 6 = 108 = 4 \cdot 27 \).
:::

:::: {#exr-powers-recurrences-markov-b2}
[B2: A three-state chain]

Let
\[
\A = \begin{pmatrix} 1/2 & 1/2 & 1/4 \\ 1/4 & 0 & 1/4 \\ 1/4 & 1/2 & 1/2 \end{pmatrix}.
\]

::: {.enumerate options="label=(\alph*)"}
1. Verify that \( \A \) is stochastic, and find its steady state.
2. Verify that \( (-1, 0, 1) \) and \( (1, -2, 1) \) are eigenvectors of \( \A \), and find their eigenvalues.
3. Hence find the entrywise limit of \( \A^k \), and the limit of the chain started at \( \x_0 = \e_2 \).
:::
::::

::: {.solution}
(a) All entries are non-negative; the columns sum to \( \frac12 + \frac14 + \frac14 = 1 \), \( \frac12 + 0 + \frac12 = 1 \) and \( \frac14 + \frac14 + \frac12 = 1 \). For the steady state, solve \( (\A - \I)\v = \0 \):
\[
\A - \I = \begin{pmatrix} -1/2 & 1/2 & 1/4 \\ 1/4 & -1 & 1/4 \\ 1/4 & 1/2 & -1/2 \end{pmatrix}.
\]
Multiplying the rows by \( 4 \): \( -2v_1 + 2v_2 + v_3 = 0 \), \( v_1 - 4v_2 + v_3 = 0 \), \( v_1 + 2v_2 - 2v_3 = 0 \). Subtracting the second from the third gives \( 6v_2 - 3v_3 = 0 \), so \( v_3 = 2v_2 \); then the second gives \( v_1 = 4v_2 - 2v_2 = 2v_2 \), and the first holds: \( -4v_2 + 2v_2 + 2v_2 = 0 \). So \( E_1(\A) = \Span((2, 1, 2)) \), and scaling to sum \( 1 \), the steady state is \( \v = (\frac25, \frac15, \frac25) \).

(b) \( \A(-1, 0, 1) = (-\frac12 + \frac14,\ -\frac14 + \frac14,\ -\frac14 + \frac12) = (-\frac14, 0, \frac14) = \frac14(-1, 0, 1) \), eigenvalue \( \frac14 \). \( \A(1, -2, 1) = (\frac12 - 1 + \frac14,\ \frac14 + \frac14,\ \frac14 - 1 + \frac12) = (-\frac14, \frac12, -\frac14) = -\frac14(1, -2, 1) \), eigenvalue \( -\frac14 \).

(c) The eigenvalues \( 1, \frac14, -\frac14 \) are distinct, so they are all the eigenvalues of \( \A \), \( \A \) is diagonalizable (@cor-distinct-eigenvalues-diagonalizable), \( a_{\A}(1) = 1 \), and the other two have absolute value \( \frac14 < 1 \). By @thm-markov-limit-diagonalizable,
\[
\A^k \to \v\1\tp = \frac15\begin{pmatrix} 2 & 2 & 2 \\ 1 & 1 & 1 \\ 2 & 2 & 2 \end{pmatrix},
\]
and every chain, in particular the one started at \( \e_2 \), converges to \( \v = (\frac25, \frac15, \frac25) \).
:::

:::: {#exr-powers-recurrences-markov-b3}
[B3: The limit of a matrix power]

Let \( \A = \begin{pmatrix} 0 & 1 \\ -1/2 & 3/2 \end{pmatrix} \in M_2(\nR) \).

::: {.enumerate options="label=(\alph*)"}
1. Diagonalize \( \A \), and find a formula for \( \A^k \).
2. Find the entrywise limit of \( \A^k \).
3. Hence find \( \lim_{k \to \infty} a_k \) for the sequence with \( a_{k+2} = \frac32a_{k+1} - \frac12a_k \), in terms of \( a_0 \) and \( a_1 \).
:::
::::

::: {.solution}
(a) \( \tr \A = \frac32 \) and \( \det \A = \frac12 \), so \( p_{\A} = x^2 - \frac32x + \frac12 = (x - 1)(x - \frac12) \). \( \A - \I = \begin{pmatrix} -1 & 1 \\ -1/2 & 1/2 \end{pmatrix} \) gives the eigenvector \( (1, 1) \); \( \A - \frac12\I = \begin{pmatrix} -1/2 & 1 \\ -1/2 & 1 \end{pmatrix} \) gives \( (2, 1) \). So \( \P = \begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix} \), \( \D = \diag(1, \frac12) \), \( \P^{-1} = \begin{pmatrix} -1 & 2 \\ 1 & -1 \end{pmatrix} \) (\( \det \P = -1 \), @thm-two-by-two-inverse). By @thm-powers-diagonalizable, with \( t = 2^{-k} \),
\[
\A^k = \begin{pmatrix} 1 & 2t \\ 1 & t \end{pmatrix}\begin{pmatrix} -1 & 2 \\ 1 & -1 \end{pmatrix} = \begin{pmatrix} -1 + 2t & 2 - 2t \\ -1 + t & 2 - t \end{pmatrix}.
\]
For \( k = 1 \), \( t = \frac12 \) gives \( \begin{pmatrix} 0 & 1 \\ -1/2 & 3/2 \end{pmatrix} = \A \).

(b) Since \( t = 2^{-k} \to 0 \), \( \A^k \to \begin{pmatrix} -1 & 2 \\ -1 & 2 \end{pmatrix} \) entrywise.

(c) \( \A \) is the window matrix of this recurrence, so \( (a_k, a_{k+1}) = \A^k(a_0, a_1) \) and \( a_k = (-1 + 2t)a_0 + (2 - 2t)a_1 \). Hence \( a_k \to 2a_1 - a_0 \). (For instance \( a_0 = 0 \), \( a_1 = 1 \) gives \( 0, 1, \frac32, \frac74, \dots \to 2 \).)
:::

### C. Going deeper

:::: {#exr-powers-recurrences-markov-c1}
[C1: Eigenvalues of a stochastic matrix]

Let \( \A \in M_n(\nR) \) be stochastic, regarded as a complex matrix, and let \( \lambda \in \nC \) be an eigenvalue of \( \A \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( |\lambda| \le 1 \).
2. Refine the argument: prove that \( |\lambda - a_{ii}| \le 1 - a_{ii} \) for some index \( i \).
3. Deduce that if every diagonal entry of \( \A \) is positive, then \( -1 \) is not an eigenvalue of \( \A \).
4. Show by an example that (c) fails if a diagonal entry is \( 0 \).
:::

*Hint: take a left eigenvector \( \y \) for \( \lambda \) and an index \( i \) with \( |y_i| \) as large as possible.*
::::

::: {.solution}
(a) By @prp-left-eigenvectors-transpose (over \( \nC \)), there is \( \y \in \nC^n \), \( \y \ne \0 \), with \( \A\tp\y = \lambda\y \). Choose \( i \) with \( |y_i| \ge |y_j| \) for all \( j \); then \( |y_i| > 0 \), since \( \y \ne \0 \). Entry \( i \) of \( \A\tp\y = \lambda\y \) reads \( \sum_j a_{ji}y_j = \lambda y_i \), because row \( i \) of \( \A\tp \) is column \( i \) of \( \A \). By @thm-conjugate-properties (d) and @thm-complex-triangle-inequality, applied to the \( n \)-term sum by induction on \( n \), and since \( a_{ji} \ge 0 \) and column \( i \) sums to \( 1 \),
\[
|\lambda|\,|y_i| = \Big|\sum_{j} a_{ji}y_j\Big| \le \sum_{j} a_{ji}|y_j| \le \sum_j a_{ji}|y_i| = |y_i| .
\]
Dividing by \( |y_i| > 0 \) gives \( |\lambda| \le 1 \).

(b) With the same \( i \), move the diagonal term across: \( (\lambda - a_{ii})y_i = \sum_{j \ne i} a_{ji}y_j \). Hence, as in (a),
\[
|\lambda - a_{ii}|\,|y_i| \le \sum_{j \ne i} a_{ji}|y_j| \le \Big(\sum_{j \ne i} a_{ji}\Big)|y_i| = (1 - a_{ii})|y_i|,
\]
and dividing by \( |y_i| \) gives \( |\lambda - a_{ii}| \le 1 - a_{ii} \).

(c) Suppose \( \lambda = -1 \). By (b), some \( i \) has \( |-1 - a_{ii}| \le 1 - a_{ii} \). Since \( a_{ii} \ge 0 \), \( |-1 - a_{ii}| = 1 + a_{ii} \), so \( 1 + a_{ii} \le 1 - a_{ii} \) and \( a_{ii} \le 0 \). This contradicts \( a_{ii} > 0 \).

(d) The swap \( \S = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) is stochastic with zero diagonal, and \( \S(1, -1) = (-1, 1) \), so \( -1 \) is an eigenvalue.
:::

:::: {#exr-powers-recurrences-markov-c2}
[C2: Two-state chains]

Let \( 0 \le p, q \le 1 \) and \( \A = \begin{pmatrix} 1 - p & q \\ p & 1 - q \end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \A \) is stochastic, with eigenvalues \( 1 \) and \( 1 - p - q \).
2. Suppose \( 0 < p + q < 2 \). Prove that \( \A^k \) converges entrywise, and find the limit and the steady state.
3. In particular, if \( \A \) has no zero entry, then \( \A^k \) converges. What happens when \( p + q = 0 \) and when \( p + q = 2 \)?
:::
::::

::: {.solution}
(a) The entries lie in \( [0, 1] \), and the columns sum to \( (1 - p) + p = 1 \) and \( q + (1 - q) = 1 \). Since \( \tr \A = 2 - p - q \) and \( \det \A = (1 - p)(1 - q) - pq = 1 - p - q \), \( p_{\A} = x^2 - (2 - p - q)x + (1 - p - q) = (x - 1)\big(x - (1 - p - q)\big) \), as multiplying out confirms.

(b) Put \( r = 1 - p - q \). Since \( 0 < p + q < 2 \), \( -1 < r < 1 \), so \( r \ne 1 \) and \( |r| < 1 \). The eigenvalues \( 1 \ne r \) are distinct, so \( \A \) is diagonalizable (@cor-distinct-eigenvalues-diagonalizable). From \( \A - \I = \begin{pmatrix} -p & q \\ p & -q \end{pmatrix} \), \( (q, p) \) is an eigenvector for \( 1 \), non-zero because \( p + q > 0 \); from \( \A - r\I = \begin{pmatrix} q & q \\ p & p \end{pmatrix} \), \( (1, -1) \) is one for \( r \). So
\[
\P = \begin{pmatrix} q & 1 \\ p & -1 \end{pmatrix}, \qquad \P^{-1} = \frac{1}{p + q}\begin{pmatrix} 1 & 1 \\ p & -q \end{pmatrix},
\]
with \( \det \P = -(p + q) \ne 0 \). By @thm-powers-diagonalizable,
\[
\A^k = \frac{1}{p + q}\begin{pmatrix} q & r^k \\ p & -r^k \end{pmatrix}\begin{pmatrix} 1 & 1 \\ p & -q \end{pmatrix} = \frac{1}{p + q}\begin{pmatrix} q + pr^k & q - qr^k \\ p - pr^k & p + qr^k \end{pmatrix}.
\]
Since \( |r| < 1 \), \( r^k \to 0 \), and
\[
\A^k \to \frac{1}{p + q}\begin{pmatrix} q & q \\ p & p \end{pmatrix}, \qquad \v = \Big(\frac{q}{p + q}, \frac{p}{p + q}\Big).
\]
The limit is \( \v\1\tp \), and \( \v \) is the steady state, in agreement with @thm-markov-limit-diagonalizable.

(c) If no entry is zero, then \( 1 - p > 0 \) and \( p > 0 \), so \( 0 < p < 1 \), and likewise \( 0 < q < 1 \); hence \( 0 < p + q < 2 \) and (b) applies. If \( p + q = 0 \), then \( p = q = 0 \) and \( \A = \I \): the powers converge (to \( \I \)), but every probability vector is a steady state. If \( p + q = 2 \), then \( p = q = 1 \) and \( \A \) is the swap, whose powers do not converge.
:::
