# Markov Chains

Chapter 8 §11 proved that a Markov chain settles down to a unique steady state, but only under three hypotheses on the eigenvalues of its transition matrix, one of them diagonalizability. It closed with a promise: the Perron–Frobenius theorem would give the same conclusions "for every stochastic matrix with some power having all entries positive, without assuming diagonalizability and without computing eigenvalues". This section keeps that promise, using the limit theorem of §05. It then asks what happens when no power is positive. Irreducible chains still have a unique steady state, and they approach it on average even when they oscillate. Reducible chains can have many steady states, and among them the absorbing chains, which end in a trap, have an exact theory built on the Neumann series.

**Conventions.** Stochastic means **column**-stochastic, as in @def-stochastic-matrix: \( \A \ge 0 \) and every column sums to \( 1 \), that is, \( \1\tp\A = \1\tp \). The entry \( a_{ij} \) is the probability of moving **to** state \( i \) **from** state \( j \), and a Markov chain is \( \x_{k+1} = \A\x_k \) (@def-markov-chain). Many books use rows and the transposed matrix; we never do. The order \( \ge \) is entrywise.

## Steady states and the Perron root

We first place stochastic matrices inside the theory of this chapter. Since \( \x_m = \A^{m}\x_0 \), the entry \( (\A^{m})_{ij} \) is the probability of being in state \( i \) after \( m \) steps when starting from state \( j \). By @lem-powers-and-walks (a) it is positive exactly when the graph \( G(\A) \) has a walk of length \( m \) from \( j \) to \( i \): the edges of the graph are the moves the chain can make in one step, and the walks are the routes it can take.

::: {#prp-stochastic-perron}
[The Perron Root of a Stochastic Matrix]

Let \( \A \in M_n(\nR) \) be stochastic. Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \rho(\A) = 1 \), and \( \1 \) is a positive left eigenvector for it;
2. the steady states of \( \A \) are exactly the non-negative eigenvectors for \( \rho(\A) \) whose entries sum to \( 1 \);
3. if \( \A \) is irreducible, then \( \A \) has **exactly one** steady state \( \v \), and \( \v > \0 \).
:::
:::

::: {.idea}
@exm-irreducible-stochastic-perron already found these facts for one matrix, and the argument there is general. The column sums make \( \1\tp \) a left eigenvector for \( 1 \), and no eigenvalue is larger in modulus; so a steady state is a non-negative eigenvector for the Perron root; when \( \A \) is irreducible, Perron–Frobenius with the normalization \( \1\tp\v = 1 \) leaves room for only one.
:::

::: {.proof}
(a) By @prp-stochastic-properties (c), \( 1 \in \spec(\A) \) and \( \1\tp\A = \1\tp \). By @cor-markov-powers-converge (a), every eigenvalue has modulus at most \( 1 \). So \( \rho(\A) = 1 \).

(b) This is @def-markov-chain read with (a): a steady state is a probability vector \( \v \) with \( \A\v = \v = \rho(\A)\v \).

(c) By @thm-perron-frobenius (a), there is \( \u > \0 \) with \( \A\u = \u \); then \( \v = \u/(\1\tp\u) \) is a steady state with \( \v > \0 \). If \( \v' \) is any steady state, it is a non-negative eigenvector, so \( \v' = c\v \) with \( c > 0 \) by @thm-perron-frobenius (c), and \( 1 = \1\tp\v' = c\,\1\tp\v = c \). Hence \( \v' = \v \).
:::

In the notation of §03, the Perron root of a stochastic matrix is \( 1 \), the all-ones vector is a positive left eigenvector, and for an irreducible stochastic matrix the steady state is the right Perron vector.

::: {.warning}
**A unique positive steady state does not make the chain converge.** The swap \( \S = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) is stochastic and irreducible, so by (c) it has exactly one steady state, \( (\frac12, \frac12) \), and it is positive. Yet the chain started at \( \e_1 \) alternates \( \e_1, \e_2, \e_1, \dots \) and never approaches it. Existence and uniqueness of the steady state come from irreducibility; convergence needs more.
:::

## The long-run theorem

The "more" is primitivity. Here are the three conclusions of @thm-markov-limit-diagonalizable, in the same words, under the hypothesis that Chapter 8 §11 promised.

::: {#thm-markov-limit-primitive}
[Long-Run Behavior of a Markov Chain]

Let \( \A \in M_n(\nR) \) be stochastic, and suppose that \( \A^{k} > 0 \) for some \( k \ge 1 \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \A \) has exactly one steady state \( \v \), and \( \v > \0 \);
2. \( \A^{m} \to \v\1\tp \) entrywise as \( m \to \infty \);
3. for every probability vector \( \x_0 \), the Markov chain \( \x_m = \A^{m}\x_0 \) converges entrywise to \( \v \).
:::
:::

::: {.idea}
For a stochastic matrix, @thm-primitive-limit has \( \rho = 1 \), and the left eigenvector can be taken to be \( \1 \), so the limit \( \v\w\tp/(\w\tp\v) \) becomes \( \v\1\tp \) once the steady state is normalized by \( \1\tp\v = 1 \). The chain inherits the limit column by column.
:::

::: {.proof}
By hypothesis \( \A \) is primitive (@def-primitive), hence irreducible (@prp-primitive-basic (b)). So (a) is @prp-stochastic-perron (c).

(b) By @prp-stochastic-perron (a), \( \rho(\A) = 1 \) and \( \w = \1 \) is positive with \( \w\tp\A = \w\tp \); and \( \v > \0 \) satisfies \( \A\v = \v \). By @thm-primitive-limit,
\[
\A^{m} = \Big(\frac{1}{\rho(\A)}\A\Big)^{m} \longrightarrow \frac{\v\1\tp}{\1\tp\v} = \v\1\tp ,
\]
since \( \1\tp\v = 1 \).

(c) Entry \( r \) of \( \A^{m}\x_0 \) is \( \sum_s(\A^{m})_{rs}(\x_0)_s \), which by (b) converges to \( \sum_s v_r(\x_0)_s = v_r\,(\1\tp\x_0) = v_r \).
:::

Compare the hypotheses with those of @thm-markov-limit-diagonalizable. That theorem asked for three facts about the eigenvalues: \( \A \) diagonalizable over \( \nC \), \( a_{\A}(1) = 1 \), and \( \lvert\lambda\rvert < 1 \) for every other eigenvalue. Chapter 9 §10 (@cor-markov-powers-converge) removed the first, but still asked to locate every eigenvalue on the unit circle. The new hypothesis is a statement about the **zero pattern** of one power of \( \A \), checked by multiplying matrices; no eigenvalue is computed, and none needs to be. The last two eigenvalue conditions become conclusions, by @prp-primitive-basic (c) and @thm-perron-frobenius (b), and diagonalizability is simply irrelevant. By @cor-primitive-iff-aperiodic the hypothesis can often be checked without multiplying at all: an irreducible stochastic matrix with one positive diagonal entry, a state that can stay put, qualifies. In the vocabulary of probability, a stochastic matrix with a positive power is called **regular**.

::: {#exm-markov-non-diagonalizable}
[A Chain that Cannot Be Diagonalized]

A token moves among three positions. From position \( 1 \) it always moves to \( 3 \); from \( 2 \) it moves to \( 1 \) or \( 3 \) with probability \( \frac12 \) each; from \( 3 \) it moves to \( 1 \) or \( 2 \) with probability \( \frac12 \) each. So
\[
\A = \begin{pmatrix} 0 & 1/2 & 1/2 \\ 0 & 0 & 1/2 \\ 1 & 1/2 & 0 \end{pmatrix} .
\]
Show that @thm-markov-limit-diagonalizable does not apply but @thm-markov-limit-primitive does, and find the long-run distribution.
:::

::: {.solution}
*Diagonalization fails.* Expanding \( \det(x\I - \A) \) along the first column,
\[
\begin{aligned}
p_{\A} &= x\Big(x^{2} - \frac14\Big) - \Big(\frac14 + \frac{x}{2}\Big) \\
&= x^{3} - \frac34x - \frac14 = (x - 1)\Big(x + \frac12\Big)^{2} .
\end{aligned}
\]
For the double eigenvalue, \( \A + \frac12\I = \begin{pmatrix} 1/2 & 1/2 & 1/2 \\ 0 & 1/2 & 1/2 \\ 1 & 1/2 & 1/2 \end{pmatrix} \) has rank \( 2 \): its first two rows are independent, and the third is twice the first minus the second. So \( g_{\A}(-\frac12) = 1 < 2 = a_{\A}(-\frac12) \), and \( \A \) is not diagonalizable (@thm-diagonalization). @thm-markov-limit-diagonalizable does not apply.

*A positive power.* Squaring,
\[
\A^{2} = \begin{pmatrix} 1/2 & 1/4 & 1/4 \\ 1/2 & 1/4 & 0 \\ 0 & 1/2 & 3/4 \end{pmatrix}, \qquad
\A^{4} = (\A^{2})^{2} = \begin{pmatrix} 3/8 & 5/16 & 5/16 \\ 3/8 & 3/16 & 1/8 \\ 1/4 & 1/2 & 9/16 \end{pmatrix} > 0 .
\]
So @thm-markov-limit-primitive applies with \( k = 4 \). (\( \A^{3} \) still has a zero at position \( (2, 1) \): three steps cannot take the token from \( 1 \) to \( 2 \).)

*The steady state.* \( (\A - \I)\v = \0 \) reads \( -v_1 + \frac12v_2 + \frac12v_3 = 0 \) and \( -v_2 + \frac12v_3 = 0 \). So \( v_3 = 2v_2 \), then \( v_1 = \frac12v_2 + v_2 = \frac32v_2 \), and \( \v \) is a multiple of \( (3, 2, 4) \). Scaling to sum \( 1 \),
\[
\v = \Big(\frac13, \frac29, \frac49\Big), \qquad \A^{m} \longrightarrow \v\1\tp .
\]
Check: \( \A\v = (\frac19 + \frac29,\ \frac29,\ \frac13 + \frac19) = (\frac13, \frac29, \frac49) \). In the long run the token is at position \( 3 \) four times out of nine, wherever it starts.

*What the Jordan block does.* Solving the recurrence exactly (for instance from the Jordan form, as in Chapter 9 §10) gives
\[
\begin{aligned}
(\A^{m})_{11} &= \frac13\Big(1 + 2\Big(-\frac12\Big)^{m}\Big), \\
(\A^{m})_{21} &= \frac29\Big(1 + (3m - 1)\Big(-\frac12\Big)^{m}\Big),
\end{aligned}
\]
which one can confirm for \( m = 0, 1, 2 \) against \( \I, \A, \A^{2} \). The factor \( m \) in the second formula comes from the \( 2 \times 2 \) Jordan block for \( -\frac12 \), whose powers carry the entry \( m\lambda^{m-1} \) (Chapter 9 §10): the error decays like \( m\,2^{-m} \) rather than \( 2^{-m} \). It still decays, and the theorem never needed to know.
:::

::: {.check}
Does @thm-markov-limit-primitive apply to \( \A = \begin{pmatrix} 1/2 & 1 \\ 1/2 & 0 \end{pmatrix} \)? If so, what is \( \lim_m \A^{m} \)?
:::

::: {.solution}
Yes: \( \A \) is stochastic and \( \A^{2} = \begin{pmatrix} 3/4 & 1/2 \\ 1/4 & 1/2 \end{pmatrix} > 0 \). The steady state solves \( -\frac12v_1 + v_2 = 0 \), so \( \v = (\frac23, \frac13) \), and \( \A^{m} \to \v\1\tp = \begin{pmatrix} 2/3 & 2/3 \\ 1/3 & 1/3 \end{pmatrix} \).
:::

The hypothesis of @thm-markov-limit-primitive is also necessary for the theorem as stated: if \( \A^{m} \to \v\1\tp \) with \( \v > \0 \), then \( \A \) is primitive (exercise C2). Without the positivity of \( \v \) it is not needed for convergence: \( \begin{pmatrix} 1 & 1/2 \\ 0 & 1/2 \end{pmatrix} \) has no positive power, yet its powers converge to \( \e_1\1\tp \), whose steady state has a zero entry.

## Irreducible chains: convergence on average

Now drop primitivity but keep irreducibility. By @prp-stochastic-perron (c) the steady state \( \v \) is still unique and positive, but by @thm-primitive-iff-single-peripheral and @thm-peripheral-spectrum the chain has \( h \ge 2 \) eigenvalues on the unit circle, and its powers do not converge (@cor-markov-powers-converge (b)). What survives is convergence of **averages**. The average \( \frac1m(\x_0 + \x_1 + \dots + \x_{m-1}) \) is, entry by entry, the average over the first \( m \) steps of the probability of being in each state; read through linearity of expectation (see the end of this section), it is the expected fraction of those steps spent there. It is this that settles down.

::: {#thm-markov-cesaro}
[Averages of an Irreducible Chain]

Let \( \A \in M_n(\nR) \) be stochastic and irreducible, with steady state \( \v \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \frac1m\big(\I + \A + \A^{2} + \dots + \A^{m-1}\big) \to \v\1\tp \) as \( m \to \infty \);
2. for every probability vector \( \x_0 \), the averages \( \frac1m(\x_0 + \x_1 + \dots + \x_{m-1}) \) of the chain converge to \( \v \);
3. \( \A^{m} \) converges if and only if \( \A \) is primitive.
:::
:::

::: {.idea}
Split every vector into its component along \( \v \) and a remainder whose entries sum to \( 0 \). The remainder lies in the image of \( \I - \A \), by a dimension count, and on that image the sum \( \sum_{k<m}\A^{k} \) telescopes: \( \sum_{k<m}\A^{k}(\I - \A)\y = \y - \A^{m}\y \), which stays bounded, so dividing by \( m \) kills it. The component along \( \v \) is fixed by every power.
:::

::: {.proof}
(a) Let \( U = \{\x \in \nR^{n} : \1\tp\x = 0\} \), the kernel of the non-zero linear functional \( \x \mapsto \1\tp\x \), so \( \dim U = n - 1 \) by Rank–Nullity (@thm-rank-nullity). Since \( \1\tp(\I - \A) = \1\tp - \1\tp = \0\tp \), the image of \( \I - \A \) lies in \( U \). The kernel of \( \I - \A \) on \( \nR^{n} \) is the real eigenspace of \( \A \) for \( 1 \); it contains \( \v \ne \0 \), and it has dimension at most \( g_{\A}(1) \le a_{\A}(1) = 1 \) by @thm-geometric-le-algebraic and @thm-perron-frobenius (b). (The real and the complex kernel of the real matrix \( \I - \A \) have the same dimension, \( n \) minus its rank, since row reduction uses only real arithmetic.) So \( \rank(\I - \A) = n - 1 \) by Rank–Nullity, and an inclusion of subspaces of equal dimension is an equality: \( \im(\I - \A) = U \).

Now fix \( \x \in \nR^{n} \). Since \( \1\tp\v = 1 \), the vector \( \x - (\1\tp\x)\v \) lies in \( U \), so \( \x = (\1\tp\x)\v + (\I - \A)\y \) for some \( \y \in \nR^{n} \). As \( \A^{k}\v = \v \) for every \( k \),
\[
\begin{aligned}
\sum_{k=0}^{m-1}\A^{k}\x &= m\,(\1\tp\x)\v + \sum_{k=0}^{m-1}\big(\A^{k}\y - \A^{k+1}\y\big) \\
&= m\,(\1\tp\x)\v + \y - \A^{m}\y .
\end{aligned}
\]
Every \( \A^{m} \) is stochastic (@prp-stochastic-properties (b)), so its entries lie in \( [0, 1] \) and \( \lvert(\A^{m}\y)_i\rvert \le \sum_j\lvert y_j\rvert \). Hence each entry of \( \frac1m(\y - \A^{m}\y) \) has modulus at most \( \frac2m\sum_j\lvert y_j\rvert \), which tends to \( 0 \) because \( \frac1m \to 0 \), by the Archimedean property, a consequence of completeness (fact (A1) in the introduction to Chapter 15). Dividing the display by \( m \), \( \frac1m\sum_{k<m}\A^{k}\x \to (\1\tp\x)\v = \v\1\tp\x \). Taking \( \x = \e_j \) gives the convergence of column \( j \), for each \( j \).

(b) \( \frac1m\sum_{k<m}\x_k = \bigl(\frac1m\sum_{k<m}\A^{k}\bigr)\x_0 \to \v\1\tp\x_0 = \v \) by (a), entry by entry as in the proof of @thm-markov-limit-primitive (c).

(c) \( (\Leftarrow) \) is @thm-markov-limit-primitive (b). \( (\Rightarrow) \) Suppose \( \A^{m} \to \L \). Then \( \A^{m+1} = \A\A^{m} \) tends both to \( \L \) and to \( \A\L \), so \( \A\L = \L \), and every column of \( \L \) lies in the real eigenspace for \( 1 \), which is \( \Span(\v) \) by the proof of (a). Each column of \( \A^{m} \) has entries \( \ge 0 \) summing to \( 1 \), and both properties survive the limit, by the elementary algebra of limits recalled in the introduction to Chapter 15 (limits respect sums, and a non-strict inequality survives a limit), so each column of \( \L \) is a probability vector on the line \( \Span(\v) \), namely \( \v \) itself. Thus \( \L = \v\1\tp > 0 \). As in the proof of @thm-primitive-iff-single-peripheral, the \( n^{2} \) entries of \( \A^{m} \) are then positive for all large \( m \), so \( \A \) is primitive.
:::

The proof of (a) used irreducibility only to know that the eigenspace for \( 1 \) is a line through a probability vector \( \v \); nothing about the period or the other eigenvalues entered.

::: {#exm-reflecting-walk}
[A Walk that Oscillates]

A walker on three sites \( 1, 2, 3 \) in a row steps to a neighboring site at every step, choosing each neighbor with probability \( \frac12 \) when there are two. So
\[
\A = \begin{pmatrix} 0 & 1/2 & 0 \\ 1 & 0 & 1 \\ 0 & 1/2 & 0 \end{pmatrix} .
\]
Show that \( \A^{m} \) does not converge, and compute the averages of @thm-markov-cesaro exactly.
:::

::: {.solution}
The edges of \( G(\A) \) are \( 1 \to 2 \), \( 2 \to 1 \), \( 2 \to 3 \) and \( 3 \to 2 \). Every site reaches every other through site \( 2 \), so \( \A \) is irreducible (@thm-irreducible-iff-strongly-connected); and every edge joins site \( 2 \) to \( \{1, 3\} \), so closed walks have even length and the period is \( 2 \). The steady state solves \( v_1 = \frac12v_2 \), \( v_3 = \frac12v_2 \), so \( \v = (\frac14, \frac12, \frac14) \). Multiplying out,
\[
\A^{2} = \begin{pmatrix} 1/2 & 0 & 1/2 \\ 0 & 1 & 0 \\ 1/2 & 0 & 1/2 \end{pmatrix}, \qquad \A^{3} = \A\A^{2} = \A .
\]
So \( \A^{m} = \A \) for odd \( m \) and \( \A^{m} = \A^{2} \) for even \( m \ge 2 \), and since \( \A \ne \A^{2} \) the powers do not converge. A walker who starts at site \( 2 \) is at site \( 2 \) at every even step and never at an odd one.

For the averages, note that \( \frac12(\A + \A^{2}) = \begin{pmatrix} 1/4 & 1/4 & 1/4 \\ 1/2 & 1/2 & 1/2 \\ 1/4 & 1/4 & 1/4 \end{pmatrix} = \v\1\tp \). For \( m = 2p \), the sum \( \sum_{k<2p}\A^{k} \) contains \( \I \) once, \( \A \) \( p \) times and \( \A^{2} \) \( p - 1 \) times, so
\[
\begin{aligned}
\frac1{2p}\sum_{k=0}^{2p-1}\A^{k} &= \frac{\I - \A^{2} + p(\A + \A^{2})}{2p} \\
&= \v\1\tp + \frac1{2p}\big(\I - \A^{2}\big) \longrightarrow \v\1\tp .
\end{aligned}
\]
For \( m = 2p + 1 \) there is one more term, \( \A^{2p} = \A^{2} \), which changes the average by at most \( \frac1m \) in each entry. So the walker spends, in the long run, half its time at the middle site and a quarter at each end, although at no single time is its distribution close to \( \v \) if it starts at a site.
:::

The oscillation can also be removed rather than averaged. The **lazy** chain \( \frac12(\I + \A) \), which at each step stays put with probability \( \frac12 \) and otherwise moves by \( \A \), is stochastic, irreducible and has positive diagonal, so it is primitive by @cor-primitive-iff-aperiodic, and it has the same steady state; exercise C1 works this out.

## Reducible chains: many steady states

Without irreducibility, uniqueness fails too. The chain can split into parts that never communicate, and each can carry its own equilibrium.

::: {#exm-reducible-chain}
[Two Traps]

States \( 1 \) and \( 2 \) exchange with each other and are never left; state \( 3 \) is never left either; state \( 4 \) stays with probability \( \frac14 \) and otherwise moves to \( 1 \), \( 2 \) or \( 3 \) with probability \( \frac14 \) each:
\[
\A = \begin{pmatrix} 1/2 & 1/4 & 0 & 1/4 \\ 1/2 & 3/4 & 0 & 1/4 \\ 0 & 0 & 1 & 1/4 \\ 0 & 0 & 0 & 1/4 \end{pmatrix} .
\]
Find all steady states, and the limit of the chain from each starting state.
:::

::: {.solution}
*Steady states.* Let \( \A\u = \u \) with \( \u \) a probability vector. The last row gives \( \frac14u_4 = u_4 \), so \( u_4 = 0 \). The first row then gives \( \frac12u_1 + \frac14u_2 = u_1 \), so \( u_2 = 2u_1 \); the second and third rows then hold automatically. So \( \u = (s, 2s, t, 0) \) with \( s, t \ge 0 \) and \( 3s + t = 1 \). Writing \( \v_1 = (\frac13, \frac23, 0, 0) \) and \( \v_2 = \e_3 \), the steady states are exactly
\[
\u = c\,\v_1 + (1 - c)\,\v_2, \qquad 0 \le c \le 1 ,
\]
the whole segment \( [\v_2, \v_1] \) of Chapter 17. There are infinitely many, and \( E_1(\A) = \Span(\v_1, \v_2) \) is a plane: \( a_{\A}(1) = 2 \), since \( p_{\A} = (x - 1)^{2}(x - \frac14)^{2} \), the first factor from the block of states \( 1, 2 \) and from state \( 3 \), the second from the block's other eigenvalue \( \frac14 \) and from state \( 4 \). In particular \( \A \) is not irreducible, by @prp-stochastic-perron (c).

*Limits.* The only eigenvalue of modulus \( 1 \) is \( 1 \), so \( \A^{m} \) converges by @cor-markov-powers-converge (b). Its limit \( \vPi \) satisfies \( \A\vPi = \vPi \), as in the proof of @thm-markov-cesaro (c), and its columns are limits of probability vectors, hence probability vectors; so each column of \( \vPi \) is a steady state. Columns \( 1 \) and \( 2 \) of every \( \A^{m} \) have zeros in rows \( 3 \) and \( 4 \), by induction on \( m \): \( \A \) maps a vector with zeros in those rows to a combination of its own first two columns, which again has zeros there. So columns \( 1 \) and \( 2 \) of \( \vPi \) are steady states with \( u_3 = 0 \), that is, \( \v_1 \). Column \( 3 \) of \( \A \) is \( \e_3 \), so column \( 3 \) of every power, and of \( \vPi \), is \( \e_3 = \v_2 \). For column \( 4 \), write it as \( c\v_1 + (1 - c)\v_2 \) and find \( c \) from a conserved quantity: the row vector \( \y\tp = (1, 1, 0, \frac23) \) satisfies \( \y\tp\A = \y\tp \), as a column-by-column check shows (column \( 4 \): \( \frac14 + \frac14 + \frac23\cdot\frac14 = \frac23 \)). Then \( \y\tp\A^{m} = \y\tp \) for all \( m \), hence \( \y\tp\vPi = \y\tp \), and entry \( 4 \) gives \( \y\tp(c\v_1 + (1 - c)\v_2) = c = \frac23 \). Thus
\[
\vPi = \begin{pmatrix} 1/3 & 1/3 & 0 & 2/9 \\ 2/3 & 2/3 & 0 & 4/9 \\ 0 & 0 & 1 & 1/3 \\ 0 & 0 & 0 & 0 \end{pmatrix} ,
\]
with last column \( \frac23\v_1 + \frac13\v_2 \). The long run depends on where the chain starts: from state \( 4 \), the chain ends up in the pair \( \{1, 2\} \) with probability \( \frac23 \) and in state \( 3 \) with probability \( \frac13 \), the ratio \( \frac12 : \frac14 \) of the one-step probabilities of leaving \( 4 \) for each.
:::

In general the steady states of a stochastic matrix form a convex set, since a convex combination of probability vectors fixed by \( \A \) is again one; the example shows it can be a segment rather than a point. One steady state for each part of the chain that, once entered, is never left, and all convex combinations of these: that is the general picture, which we do not prove here.

## Absorbing chains

The simplest traps are single states. A state \( j \) is **absorbing** if \( a_{jj} = 1 \), so that column \( j \) of \( \A \) is \( \e_j \): once there, the chain stays. Absorbing states model the end of a process: a game won or lost, a customer who has left, a molecule that has reacted.

::: {#def-absorbing-chain}
[Absorbing Chain]

A stochastic matrix \( \A \in M_n(\nR) \) is **absorbing** if it has at least one absorbing state, and **from every state some absorbing state can be reached**: for every \( j \) there are an absorbing state \( i \) and an \( m \ge 0 \) with \( (\A^{m})_{ij} > 0 \). The states that are not absorbing are called **transient**.
:::

Number the states so that the \( t \ge 1 \) transient states come first and the \( r \ge 1 \) absorbing states last. Column \( j \) for a transient \( j \) splits into the probabilities of moving to transient states and to absorbing states, and the column of an absorbing state is a standard basis vector. So \( \A \) has the block form
\[
\A = \begin{pmatrix} \Q & 0 \\ \R & \I_r \end{pmatrix}, \qquad \Q \in M_t(\nR), \quad \R \in M_{r \times t}(\nR),
\]
with \( \Q, \R \ge 0 \) and \( \1\tp\Q + \1\tp\R = \1\tp \). Multiplying blocks and inducting on \( m \),
\[
\A^{m} = \begin{pmatrix} \Q^{m} & 0 \\ \R_m & \I_r \end{pmatrix}, \qquad \R_m = \R\big(\I + \Q + \dots + \Q^{m-1}\big) ,
\]
since \( \A^{m+1} = \A\A^{m} \) has lower-left block \( \R\Q^{m} + \R_m = \R_{m+1} \). The entry \( (\Q^{m})_{ij} \) is the probability of being at transient state \( i \) after \( m \) steps from transient state \( j \); the column sums of \( \Q^{m} \) are the probabilities of not yet having been absorbed.

::: {#lem-absorbing-transient-decay}
[Transient Mass Dies Out]

If \( \A \) is absorbing, with \( \Q \) as above, then every eigenvalue of \( \Q \) has modulus less than \( 1 \), and \( \Q^{m} \to 0 \).
:::

::: {.idea}
Every column of \( \Q \) sums to at most \( 1 \), which only gives \( \rho(\Q) \le 1 \). But after enough steps every transient state has leaked some mass into an absorbing state, so every column of a suitable power \( \Q^{M} \) sums to **strictly** less than \( 1 \), and the column-sum bound of Chapter 15 gives \( \rho(\Q^{M}) < 1 \).
:::

::: {.proof}
For absorbing \( i \) and any \( j \), \( (\A^{m+1})_{ij} = \sum_l a_{il}(\A^{m})_{lj} \ge a_{ii}(\A^{m})_{ij} = (\A^{m})_{ij} \), since all terms are non-negative; so the probability of being at \( i \) never decreases. Fix a transient \( j \). By @def-absorbing-chain there are an absorbing \( i \) and \( m_j \) with \( (\A^{m_j})_{ij} > 0 \), and then \( (\A^{m})_{ij} > 0 \) for every \( m \ge m_j \). Let \( M \) be the largest of the \( m_j \) over the transient \( j \). Column \( j \) of \( \A^{M} \) sums to \( 1 \) (@prp-stochastic-properties (b)) and has a positive entry \( (\A^{M})_{ij} \) in the absorbing rows, so column \( j \) of \( \Q^{M} \) sums to less than \( 1 \). Since \( \Q^{M} \ge 0 \), its largest absolute column sum is some \( c < 1 \), and by @cor-spectral-radius-row-column-bound, \( \rho(\Q^{M}) \le c < 1 \). By @thm-spectral-mapping with \( q = x^{M} \), the eigenvalues of \( \Q^{M} \) are the \( M \)-th powers of those of \( \Q \), so \( \rho(\Q)^{M} = \rho(\Q^{M}) < 1 \) and \( \rho(\Q) < 1 \). Finally \( \Q^{m} \to 0 \) by @thm-matrix-powers-converge-to-zero.
:::

The Neumann series now does all the work.

::: {#thm-absorbing-chain}
[Absorbing Chains]

Let \( \A = \begin{pmatrix} \Q & 0 \\ \R & \I_r \end{pmatrix} \) be absorbing, in the block form above. Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \I - \Q \) is invertible, and the **fundamental matrix** \( \N \coloneqq (\I - \Q)^{-1} = \sum_{k \ge 0}\Q^{k} \) satisfies \( \N \ge 0 \);
2. \( \A^{m} \to \begin{pmatrix} 0 & 0 \\ \R\N & \I_r \end{pmatrix} \) entrywise;
3. every column of the \( r \times t \) matrix \( \B \coloneqq \R\N \) is a probability vector.
:::
:::

::: {.idea}
The lemma gives \( \rho(\Q) < 1 \), which is exactly what the Neumann series needs. In the block formula for \( \A^{m} \), the lower-left block is \( \R \) times a partial sum of that series, so it converges to \( \R\N \); and column sums equal to \( 1 \) pass to the limit.
:::

::: {.proof}
(a) By @lem-absorbing-transient-decay and @thm-neumann-series-spectral, \( \sum_k\Q^{k} \) converges and equals \( (\I - \Q)^{-1} \). Each partial sum is \( \ge 0 \), and a limit of non-negative numbers is non-negative, since a non-strict inequality survives a limit (the elementary algebra of limits, recalled in the introduction to Chapter 15); so \( \N \ge 0 \).

(b) By the block formula, the upper-left block of \( \A^{m} \) is \( \Q^{m} \to 0 \) (@lem-absorbing-transient-decay), and the lower-left block is \( \R_m = \R\sum_{k<m}\Q^{k} \). Each entry of \( \R_m \) is a fixed linear combination of entries of the partial sum, so \( \R_m \to \R\N \) by the algebra of limits, (B3) of Chapter 9 §10. The other two blocks do not depend on \( m \).

(c) Every column of \( \A^{m} \) sums to \( 1 \), and so does every column of the limit in (b). For a transient \( j \), column \( j \) of the limit is \( (\0, \B\e_j) \), so the entries of \( \B\e_j \) sum to \( 1 \); they are non-negative because \( \R, \N \ge 0 \).
:::

**Reading the answer.** The theorem is pure algebra; its meaning comes from reading entries as probabilities. The \( (i, j) \)-entry of the limit in (b), for absorbing \( i \) and transient \( j \), is the limit of the non-decreasing probabilities of being at \( i \) after \( m \) steps from \( j \): the **probability of being absorbed at \( i \)**. So \( \B = \R\N \) is the matrix of absorption probabilities. Two further readings use a fact from probability that this book does not develop, **linearity of expectation**: the expected number of steps at which an event occurs is the sum over the steps of the probabilities of that event. With it, since \( (\Q^{k})_{ij} \) is the probability of being at transient \( i \) at step \( k \) from \( j \),
\[
\begin{aligned}
N_{ij} &= \sum_{k \ge 0}(\Q^{k})_{ij} \\
&= \text{expected number of visits to } i \text{ starting from } j ,
\end{aligned}
\]
counting the visit at step \( 0 \) when \( i = j \); and summing over \( i \), the column sums \( \tau_j = (\1\tp\N)_j \) are the **expected numbers of steps before absorption**. Nothing in the proofs depends on these readings.

::: {#exm-gamblers-ruin}
[Gambler's Ruin]

A gambler holds \( 1 \), \( 2 \) or \( 3 \) coins and bets one coin at a time on a fair toss, winning or losing a coin with probability \( \frac12 \) each. Play stops when the gambler holds \( 0 \) coins (ruin) or \( 4 \) coins (target). Find the fundamental matrix, the expected length of play, and the probability of reaching the target, from each starting fortune.
:::

::: {.solution}
The transient states are the fortunes \( 1, 2, 3 \), in that order, and the absorbing ones are \( 0 \) and \( 4 \), in that order. From fortune \( j \) the gambler moves to \( j - 1 \) or \( j + 1 \) with probability \( \frac12 \) each, so
\[
\Q = \begin{pmatrix} 0 & 1/2 & 0 \\ 1/2 & 0 & 1/2 \\ 0 & 1/2 & 0 \end{pmatrix}, \qquad \R = \begin{pmatrix} 1/2 & 0 & 0 \\ 0 & 0 & 1/2 \end{pmatrix} ,
\]
the first row of \( \R \) recording ruin from fortune \( 1 \) and the second reaching the target from fortune \( 3 \). Each column of \( \begin{pmatrix} \Q \\ \R \end{pmatrix} \) sums to \( 1 \), and every fortune reaches \( 0 \) by losing, so the chain is absorbing.

*The fundamental matrix.* Solve \( (\I - \Q)\N = \I \) with \( \I - \Q = \begin{pmatrix} 1 & -1/2 & 0 \\ -1/2 & 1 & -1/2 \\ 0 & -1/2 & 1 \end{pmatrix} \). The result is
\[
\N = \begin{pmatrix} 3/2 & 1 & 1/2 \\ 1 & 2 & 1 \\ 1/2 & 1 & 3/2 \end{pmatrix} ;
\]
check the first column: \( (\I - \Q)(\frac32, 1, \frac12) = (\frac32 - \frac12,\ -\frac34 + 1 - \frac14,\ -\frac12 + \frac12) = (1, 0, 0) \), and the other columns likewise. A gambler starting with \( 2 \) coins holds exactly \( 2 \) coins at \( 2 \) steps on average, counting the start, and holds \( 1 \) or \( 3 \) coins at one step each on average.

*Length of play.* \( \1\tp\N = (3, 4, 3) \): from fortunes \( 1, 2, 3 \) the game lasts \( 3 \), \( 4 \), \( 3 \) tosses on average.

*Absorption.*
\[
\B = \R\N = \begin{pmatrix} 3/4 & 1/2 & 1/4 \\ 1/4 & 1/2 & 3/4 \end{pmatrix} .
\]
From fortune \( j \) the gambler reaches the target with probability \( j/4 \) and is ruined with probability \( 1 - j/4 \). Each column sums to \( 1 \), as @thm-absorbing-chain (c) requires: the game ends with probability \( 1 \). Both answers match the classical formulas for a fair game with target \( T = 4 \): success probability \( j/T \) and expected length \( j(T - j) \), which gives \( 3, 4, 3 \).
:::

The matrix \( \Q \) of this example has eigenvalues \( 0 \) and \( \pm\frac{1}{\sqrt2} \), of modulus less than \( 1 \) as @lem-absorbing-transient-decay requires; but the lemma was proved without finding them, which is the pattern of this whole section.

## Exercises

### A. Check your understanding

:::: {#exr-markov-chains-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the long-run theorem @thm-markov-limit-primitive, and name the three hypotheses of @thm-markov-limit-diagonalizable that it no longer needs.
2. True or false: every irreducible stochastic matrix has exactly one steady state. Justify your answer.
3. True or false: for every irreducible stochastic matrix, \( \A^{m} \) converges. Justify your answer.
4. True or false: if a stochastic matrix has two different steady states, it has infinitely many. Justify your answer.
5. In an absorbing chain, what do the column sums of the fundamental matrix measure, and why do the columns of \( \R\N \) sum to \( 1 \)?
:::
::::

::: {.solution}
(a) If \( \A \) is stochastic and \( \A^{k} > 0 \) for some \( k \), then \( \A \) has exactly one steady state \( \v \), it is positive, \( \A^{m} \to \v\1\tp \), and every chain \( \A^{m}\x_0 \) converges to \( \v \). It no longer assumes that \( \A \) is diagonalizable, that \( a_{\A}(1) = 1 \), or that every other eigenvalue has modulus less than \( 1 \).

(b) True, by @prp-stochastic-perron (c); moreover the steady state is positive.

(c) False. The swap \( \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) is irreducible and stochastic, and its powers alternate between \( \I \) and itself. By @thm-markov-cesaro (c), the powers converge exactly when the matrix is primitive.

(d) True. If \( \u \ne \u' \) are steady states, then \( c\u + (1 - c)\u' \) for \( 0 \le c \le 1 \) is non-negative, has entries summing to \( 1 \), and is fixed by \( \A \); different \( c \) give different vectors, since \( \u - \u' \ne \0 \).

(e) The column sum \( (\1\tp\N)_j \) is the expected number of steps before absorption from transient state \( j \). The columns of \( \R\N \) sum to \( 1 \) because the columns of \( \A^{m} \) do and \( \Q^{m} \to 0 \) (@thm-absorbing-chain (c)): absorption is certain.
:::

### B. Practice

:::: {#exr-markov-chains-b1}
[B1: When does the long-run theorem apply?]

For each stochastic matrix, determine whether @thm-markov-limit-primitive applies. Justify your answer, and when it applies, find the limit of \( \A^{m} \).

::: {.enumerate options="label=(\alph*)"}
1. \( \begin{pmatrix} 0 & 0 & 1/2 \\ 1 & 0 & 0 \\ 0 & 1 & 1/2 \end{pmatrix} \).
2. \( \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} \).
3. \( \begin{pmatrix} 1/2 & 0 \\ 1/2 & 1 \end{pmatrix} \).
:::
::::

::: {.solution}
(a) It applies. The edges of \( G(\A) \) are \( 1 \to 2 \), \( 2 \to 3 \), \( 3 \to 1 \) and the loop \( 3 \to 3 \). The cycle \( 1 \to 2 \to 3 \to 1 \) reaches every state from every state, so \( \A \) is irreducible (@thm-irreducible-iff-strongly-connected). It has the positive diagonal entry \( a_{33} \), so it is primitive by @cor-primitive-iff-aperiodic. The steady state solves \( v_1 = \frac12v_3 \), \( v_2 = v_1 \), so \( \v = (1, 1, 2)/4 \), and \( \A^{m} \to \v\1\tp \), every column equal to \( (\frac14, \frac14, \frac12) \). Check: \( \A\v = (\frac14, \frac14, \frac14 + \frac14) = \v \).

(b) It does not apply. This is a permutation matrix, so every power is a permutation matrix (@lem-permutation-matrices) and has zero entries. Its powers cycle with period \( 3 \) (@exm-cyclic-permutation) and do not converge.

(c) It does not apply. Every power is lower triangular with \( (1,2) \)-entry \( 0 \), as one checks by induction: \( \A^{m} = \begin{pmatrix} 2^{-m} & 0 \\ 1 - 2^{-m} & 1 \end{pmatrix} \). The powers converge nonetheless, to \( \begin{pmatrix} 0 & 0 \\ 1 & 1 \end{pmatrix} = \e_2\1\tp \): state \( 2 \) is absorbing, and \( \e_2 \) is the unique steady state, with a zero entry.
:::

:::: {#exr-markov-chains-b2}
[B2: A three-state chain]

Let \( \A = \begin{pmatrix} 1/2 & 1/4 & 0 \\ 1/2 & 1/2 & 1/2 \\ 0 & 1/4 & 1/2 \end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \A \) is stochastic and that \( \A^{2} > 0 \).
2. Find the steady state, and hence \( \lim_m \A^{m} \) and the long-run distribution of every chain with this transition matrix.
:::
::::

::: {.solution}
(a) The entries are non-negative and the columns sum to \( 1 \). Multiplying out,
\[
\A^{2} = \begin{pmatrix} 3/8 & 1/4 & 1/8 \\ 1/2 & 1/2 & 1/2 \\ 1/8 & 1/4 & 3/8 \end{pmatrix} > 0 .
\]
(b) \( (\A - \I)\v = \0 \): the first row gives \( -\frac12v_1 + \frac14v_2 = 0 \), so \( v_2 = 2v_1 \), and the third gives \( \frac14v_2 - \frac12v_3 = 0 \), so \( v_3 = \frac12v_2 = v_1 \). So \( \v \) is a multiple of \( (1, 2, 1) \), and scaling to sum \( 1 \) gives \( \v = (\frac14, \frac12, \frac14) \). By @thm-markov-limit-primitive, \( \A^{m} \to \v\1\tp \), every column equal to \( \v \), and every chain converges to \( \v \) whatever its initial distribution.
:::

:::: {#exr-markov-chains-b3}
[B3: An unfair game]

A gambler holds \( 1 \) or \( 2 \) coins and wins each toss with probability \( \frac13 \), losing with probability \( \frac23 \). Play stops at \( 0 \) or \( 3 \) coins. Find the fundamental matrix, the expected length of play and the probability of reaching \( 3 \) coins from each starting fortune.
::::

::: {.solution}
Order the states as \( 1, 2 \) (transient) and \( 0, 3 \) (absorbing). From \( 1 \): to \( 2 \) with probability \( \frac13 \), to \( 0 \) with \( \frac23 \). From \( 2 \): to \( 3 \) with \( \frac13 \), to \( 1 \) with \( \frac23 \). So
\[
\Q = \begin{pmatrix} 0 & 2/3 \\ 1/3 & 0 \end{pmatrix}, \qquad \R = \begin{pmatrix} 2/3 & 0 \\ 0 & 1/3 \end{pmatrix} .
\]
The chain is absorbing, since from either fortune repeated losses reach \( 0 \). Then \( \I - \Q = \begin{pmatrix} 1 & -2/3 \\ -1/3 & 1 \end{pmatrix} \) has determinant \( 1 - \frac29 = \frac79 \), so by @thm-two-by-two-inverse
\[
\N = \frac97\begin{pmatrix} 1 & 2/3 \\ 1/3 & 1 \end{pmatrix} = \begin{pmatrix} 9/7 & 6/7 \\ 3/7 & 9/7 \end{pmatrix} .
\]
The expected lengths of play are \( \1\tp\N = (\frac{12}{7}, \frac{15}{7}) \), and
\[
\R\N = \begin{pmatrix} 6/7 & 4/7 \\ 1/7 & 3/7 \end{pmatrix} .
\]
So the probability of reaching \( 3 \) coins is \( \frac17 \) from \( 1 \) coin and \( \frac37 \) from \( 2 \) coins, far below the fair values \( \frac13 \) and \( \frac23 \). The columns of \( \R\N \) sum to \( 1 \), as they must.
:::

### C. Going deeper

:::: {#exr-markov-chains-c1}
[C1: The lazy chain]

Let \( \A \in M_n(\nR) \) be stochastic and irreducible, with steady state \( \v \), and let \( \M = \frac12(\I + \A) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \M \) is stochastic and primitive, and that \( \v \) is its unique steady state. Deduce that \( \M^{m} \to \v\1\tp \).
2. Let \( \A \) be the walk of @exm-reflecting-walk. Show that \( \M \) is the matrix of exercise B2, and that \( \M^{m} = \v\1\tp + 2^{-m}\F \) for every \( m \ge 1 \), where \( \F = \frac12\begin{psmallmatrix} 1 & 0 & -1 \\ 0 & 0 & 0 \\ -1 & 0 & 1 \end{psmallmatrix} \).
:::

*Hint: write \( \M \) in terms of \( \v\1\tp \) and \( \F \).*
::::

::: {.solution}
(a) \( \M \ge 0 \), and \( \1\tp\M = \frac12(\1\tp + \1\tp\A) = \1\tp \), so \( \M \) is stochastic. By @exr-primitive-matrices-c1 (a) with \( t = 1 \), \( \A + \I \) is primitive, say \( (\A + \I)^{k} > 0 \); then \( \M^{k} = 2^{-k}(\A + \I)^{k} > 0 \), so \( \M \) is primitive. Also \( \M\v = \frac12(\v + \v) = \v \). By @thm-markov-limit-primitive (a), \( \M \) has exactly one steady state, so it is \( \v \), and by part (b) of that theorem \( \M^{m} \to \v\1\tp \).

(b) With \( \A \) as in @exm-reflecting-walk,
\[
\M = \frac12\begin{pmatrix} 1 & 1/2 & 0 \\ 1 & 1 & 1 \\ 0 & 1/2 & 1 \end{pmatrix} = \begin{pmatrix} 1/2 & 1/4 & 0 \\ 1/2 & 1/2 & 1/2 \\ 0 & 1/4 & 1/2 \end{pmatrix} ,
\]
the matrix of @exr-markov-chains-b2, and \( \v = (\frac14, \frac12, \frac14) \). Put \( \L = \v\1\tp \), every column equal to \( \v \). Then \( \L^{2} = \v(\1\tp\v)\1\tp = \L \); \( \1\tp\F = \0\tp \), since each column of \( \F \) sums to \( 0 \), so \( \L\F = \v(\1\tp\F) = 0 \); and \( \F\v = \frac12(\frac14 - \frac14,\ 0,\ -\frac14 + \frac14) = \0 \), so \( \F\L = (\F\v)\1\tp = 0 \). Also \( \F^{2} = \frac14\begin{pmatrix} 2 & 0 & -2 \\ 0 & 0 & 0 \\ -2 & 0 & 2 \end{pmatrix} = \F \). Subtracting, \( \M - \L = \frac14\begin{pmatrix} 1 & 0 & -1 \\ 0 & 0 & 0 \\ -1 & 0 & 1 \end{pmatrix} = \frac12\F \), so \( \M = \L + \frac12\F \). If \( \M^{m} = \L + 2^{-m}\F \), then
\[
\begin{aligned}
\M^{m+1} &= \Big(\L + \frac12\F\Big)\big(\L + 2^{-m}\F\big) \\
&= \L^{2} + 2^{-m}\L\F + \frac12\F\L + 2^{-m-1}\F^{2} = \L + 2^{-(m+1)}\F ,
\end{aligned}
\]
so the formula holds for every \( m \ge 1 \) by induction, starting from \( \M = \L + \frac12\F \). The lazy walk converges although the walk itself oscillates, and its distance to the limit halves at every step.
:::

:::: {#exr-markov-chains-c2}
[C2: The converse of the long-run theorem]

Let \( \A \in M_n(\nR) \) be stochastic.

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( \A^{m} \to \v\1\tp \) for some \( \v > \0 \), then \( \A \) is primitive.
2. Give a stochastic \( \A \) with \( \A^{m} \to \v\1\tp \) for a probability vector \( \v \), but no power of \( \A \) positive. Which entry of \( \v \) is responsible?
:::
::::

::: {.solution}
(a) The limit \( \v\1\tp \) has \( (i, j) \)-entry \( v_i > 0 \). Each of the \( n^{2} \) entries of \( \A^{m} \) converges to a positive number, so it is positive for all \( m \) beyond some \( m_{ij} \); for \( m \) larger than all the \( m_{ij} \), \( \A^{m} > 0 \). So \( \A \) is primitive.

(b) \( \A = \begin{pmatrix} 1 & 1/2 \\ 0 & 1/2 \end{pmatrix} \). By induction \( \A^{m} = \begin{pmatrix} 1 & 1 - 2^{-m} \\ 0 & 2^{-m} \end{pmatrix} \): indeed \( \A\A^{m} \) has first row \( (1,\ 1 - 2^{-m} + 2^{-m-1}) = (1,\ 1 - 2^{-(m+1)}) \) and second row \( (0,\ 2^{-(m+1)}) \). So \( \A^{m} \to \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix} = \e_1\1\tp \), while every power has \( (2,1) \)-entry \( 0 \). The responsible entry is \( v_2 = 0 \): (a) fails exactly because \( \v \) is not positive.
:::

:::: {#exr-markov-chains-c3}
[C3: First-step analysis]

Let \( \A \) be absorbing, with fundamental matrix \( \N \) and \( \vtau\tp = \1\tp\N \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \N = \I + \N\Q \), and deduce that \( \tau_j = 1 + \sum_i q_{ij}\tau_i \) for every transient \( j \). Interpret this equation.
2. Prove, by multiplying by \( \R \), that \( \B = \R\N \) satisfies \( \B = \R + \B\Q \), and interpret it.
3. Use (a) to recompute the expected lengths of play \( (3, 4, 3) \) of @exm-gamblers-ruin without inverting a matrix.
:::
::::

::: {.solution}
(a) \( \N(\I - \Q) = \I \) because \( \N \) is the inverse of \( \I - \Q \), so \( \N = \I + \N\Q \). Multiplying on the left by \( \1\tp \), \( \vtau\tp = \1\tp + \vtau\tp\Q \), whose \( j \)-th entry is \( \tau_j = 1 + \sum_i\tau_iq_{ij} \). In words: from \( j \), one step is taken, the chain lands at transient \( i \) with probability \( q_{ij} \), and from there the expected remaining time is \( \tau_i \); landing at an absorbing state contributes nothing more.

(b) Multiply \( \N = \I + \N\Q \) on the left by \( \R \): \( \B = \R + \B\Q \), that is, \( b_{ij} = r_{ij} + \sum_l b_{il}q_{lj} \). The probability of absorption at \( i \) from \( j \) is the probability of stepping into \( i \) at once, plus the probability of stepping to a transient \( l \) and being absorbed at \( i \) from there.

(c) With \( \Q \) as in @exm-gamblers-ruin, (a) reads \( \tau_1 = 1 + \frac12\tau_2 \), \( \tau_2 = 1 + \frac12\tau_1 + \frac12\tau_3 \), \( \tau_3 = 1 + \frac12\tau_2 \). The first and third equations give \( \tau_1 = \tau_3 = 1 + \frac12\tau_2 \), so \( \tau_2 = 1 + \tau_1 = 1 + 1 + \frac12\tau_2 \), giving \( \tau_2 = 4 \) and \( \tau_1 = \tau_3 = 3 \). (The system has only one solution, since its matrix is \( (\I - \Q)\tp \), which is invertible by @thm-absorbing-chain (a).)
:::
