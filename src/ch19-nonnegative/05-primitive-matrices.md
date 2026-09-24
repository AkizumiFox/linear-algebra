# Primitive Matrices

The Perron–Frobenius theorem tells us what an irreducible non-negative matrix looks like at its spectral radius: \( \rho(\A) \) is an algebraically simple eigenvalue with a positive eigenvector. It says nothing about what the powers \( \A^{m} \) do, and Chapter 9 §11 already met the obstacle. The swap \( \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) is irreducible, has a positive eigenvector for \( \rho = 1 \), and its powers alternate forever. This section finds the extra hypothesis that makes the powers settle down, proves that under it \( (\A/\rho)^{m} \) converges to an explicit rank-one matrix, and explains what goes wrong without it: the eigenvalues of modulus \( \rho \) are then spread evenly around a circle, and their number is read off the zero pattern of \( \A \).

**Throughout, matrices are real and \( \A \ge 0 \) is meant entrywise**, as are \( \A > 0 \), \( \x \ge \0 \) and \( \x > \0 \). The spectrum is taken over \( \nC \), and \( \rho(\A) \) is the spectral radius (@def-spectral-radius).

## Walks in a non-negative matrix

Whether a power \( \A^{m} \) has a positive entry at position \( (i, j) \) depends only on which entries of \( \A \) are zero. The bookkeeping device is the directed graph \( G(\A) \) of §02 (@def-directed-graph-of-matrix): it has an edge \( j \to i \) for each non-zero entry \( a_{ij} \), and a walk of length \( m \) from \( j \) to \( i \) is a list \( j = i_0, i_1, \dots, i_m = i \) of vertices in which each \( i_{t-1} \to i_t \) is an edge. The edge for \( a_{ij} \) points from the column index to the row index, the direction in which a column-stochastic chain moves. A walk is **closed** if \( i_0 = i_m \) and \( m \ge 1 \).

By §02's count of walks (@lem-powers-and-walks (a)), for \( \A \ge 0 \) and \( m \ge 0 \), \( (\A^{m})_{ij} > 0 \) if and only if \( G(\A) \) has a walk of length \( m \) from \( j \) to \( i \). Everything in this section about zero patterns rests on that fact.

## Primitive matrices

Here is the property the swap lacks. Its powers are \( \I \) and the swap itself, and each of them has zero entries; no power ever mixes every state with every other.

*A primitive matrix is one that, after enough steps, connects every index to every index at once.*

::: {#def-primitive}
[Primitive Matrix]

A matrix \( \A \in M_n(\nR) \), \( n \ge 1 \), with \( \A \ge 0 \) is **primitive** if \( \A^{k} > 0 \) for **some** integer \( k \ge 1 \), that is, if **every** entry of some power of \( \A \) is **strictly** positive.
:::

In words: we are allowed to wait, but only for a finite number \( k \) of steps, and after those \( k \) steps all \( n^{2} \) entries must be positive together. By @lem-powers-and-walks (a), \( \A \) is primitive exactly when there is one length \( k \) such that every vertex of \( G(\A) \) has a walk of length \( k \) to every vertex, including to itself.

**Examples.**

- **Positive matrices.** If \( \A > 0 \), take \( k = 1 \). Perron's theorem (@thm-perron) is about these.
- **A matrix with zeros.** \( \A = \begin{pmatrix} 1 & 1 \\ 2 & 0 \end{pmatrix} \) has a zero entry, but \( \A^{2} = \begin{pmatrix} 3 & 1 \\ 2 & 2 \end{pmatrix} > 0 \). So \( \A \) is primitive with \( k = 2 \). In the graph: the edges are \( 1 \to 1 \), \( 1 \to 2 \) and \( 2 \to 1 \), and \( 1 \to 1 \to 1 \), \( 1 \to 1 \to 2 \), \( 2 \to 1 \to 1 \), \( 2 \to 1 \to 2 \) are walks of length \( 2 \) between every ordered pair.
- **A slower one.** \( \W = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix} \). Its edges are \( 2 \to 1 \), \( 3 \to 2 \), \( 1 \to 3 \) and \( 2 \to 3 \), so its closed walks include \( 1 \to 3 \to 2 \to 1 \) of length \( 3 \) and \( 2 \to 3 \to 2 \) of length \( 2 \). Multiplying out, \( \W^{4} = \begin{pmatrix} 0 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 2 & 1 \end{pmatrix} \) still has a zero, and \( \W^{5} = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 2 & 2 \end{pmatrix} > 0 \). So \( \W \) is primitive, and the smallest \( k \) is \( 5 \).
- **Degenerate case.** A \( 1 \times 1 \) matrix \( (a) \) is primitive if and only if \( a > 0 \). The zero \( 1 \times 1 \) matrix is not, which is why the statements below exclude it.

**Non-example by minimal change.** Change the \( (1,1) \)-entry of \( \begin{pmatrix} 1 & 1 \\ 2 & 0 \end{pmatrix} \) to \( 0 \). The result \( \A' = \begin{pmatrix} 0 & 1 \\ 2 & 0 \end{pmatrix} \) is still non-negative, and it is still irreducible, since \( (\I + \A')^{1} > 0 \) (@thm-irreducible-power-positive). But \( \A'^{2} = 2\I \), so the even powers of \( \A' \) are multiples of \( \I \) and the odd powers multiples of \( \A' \), and every power has two zero entries: \( \A' \) is not primitive. The clause that fails is "some power is positive"; what was lost is the loop \( 1 \to 1 \); without it every edge joins \( 1 \) and \( 2 \), so every closed walk has even length. More generally, the powers of a permutation matrix are permutation matrices (@lem-permutation-matrices), and for \( n \ge 2 \) a permutation matrix has zeros; so no permutation matrix of size \( n \ge 2 \) is primitive.

**Why this definition.** Asking for \( \A > 0 \) itself would be too strong: it excludes the matrices above, whose powers behave exactly like those of a positive matrix. Asking only that each position \( (i, j) \) be positive in **some** power, possibly a different power for each position, is too weak: that is irreducibility, and the swap satisfies it. Primitivity sits between the two. It asks for a **single** power that is positive everywhere.

::: {.warning}
**Irreducible does not mean primitive.** Irreducibility asks that each \( j \) be reachable from each \( i \) by a walk of **some** length; primitivity asks for walks of **one common** length. For the swap, every walk from \( 1 \) to \( 2 \) has odd length and every walk from \( 1 \) to \( 1 \) has even length, so no single power is positive at both \( (1,1) \) and \( (1,2) \).
:::

::: {.check}
Is \( \A = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix} \) primitive? Is \( \B = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \)?
:::

::: {.solution}
\( \A^{2} = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} > 0 \), so \( \A \) is primitive. For \( \B \), every power is upper triangular, \( \B^{m} = \begin{pmatrix} 1 & m \\ 0 & 1 \end{pmatrix} \), so the \( (2,1) \)-entry is always \( 0 \) and \( \B \) is not primitive: \( G(\B) \) has no walk from \( 1 \) to \( 2 \) at all.
:::

The first consequences of the definition come straight from the graph and from Perron's theorem applied to the positive power.

::: {#prp-primitive-basic}
[First Properties of Primitive Matrices]

Let \( \A \in M_n(\nR) \) be primitive, with \( \A^{k} > 0 \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \A^{m} > 0 \) for **every** \( m \ge k \);
2. \( \A \) is irreducible;
3. \( \rho(\A) > 0 \), and \( \rho(\A) \) is the **only** eigenvalue of \( \A \) of modulus \( \rho(\A) \).
:::
:::

::: {.idea}
(a) Multiplying a positive matrix by a non-negative matrix with no zero column keeps it positive. (b) A positive power gives walks between all vertices, which is strong connectivity. (c) The eigenvalues of \( \A^{k} \) are the \( k \)-th powers of those of \( \A \). A second eigenvalue of \( \A \) on the circle of radius \( \rho \) would land, after raising to the \( k \)-th power, on the circle where Perron's theorem allows only the simple eigenvalue \( \rho(\A^{k}) \).
:::

::: {.proof}
(a) Column \( j \) of \( \A^{k} \) is \( \A^{k-1} \) times column \( j \) of \( \A \) (@thm-three-views-of-product; for \( k = 1 \) read \( \A^{0} = \I \)). Since \( \A^{k} > 0 \), no column of \( \A \) is zero. Now suppose \( \A^{m} > 0 \) for some \( m \ge k \). Then \( (\A^{m+1})_{ij} = \sum_l (\A^{m})_{il}a_{lj} \) is a sum of non-negative terms, and the term for an \( l \) with \( a_{lj} > 0 \) is positive. So \( \A^{m+1} > 0 \), and (a) follows by induction on \( m \).

(b) For every ordered pair \( (j, i) \), \( (\A^{k})_{ij} > 0 \), so @lem-powers-and-walks (a) gives a walk from \( j \) to \( i \) in \( G(\A) \). So \( G(\A) \) is strongly connected (@def-strongly-connected), and \( \A \) is irreducible by @thm-irreducible-iff-strongly-connected.

(c) Over \( \nC \), write \( p_{\A} = (x - \lambda_1)\cdots(x - \lambda_n) \), with each eigenvalue repeated according to its algebraic multiplicity. By the Spectral Mapping Theorem (@thm-spectral-mapping) with \( q = x^{k} \),
\[
p_{\A^{k}} = (x - \lambda_1^{k})\cdots(x - \lambda_n^{k}) .
\]
So \( \rho(\A^{k}) = \max_i\lvert\lambda_i\rvert^{k} = \rho(\A)^{k} \). By @thm-perron applied to \( \A^{k} > 0 \), \( \rho(\A^{k}) > 0 \) is an algebraically simple eigenvalue of \( \A^{k} \), and every other eigenvalue of \( \A^{k} \) has modulus less than \( \rho(\A^{k}) \). In particular \( \rho(\A)^{k} > 0 \), so \( \rho(\A) > 0 \).

By (b) and @thm-perron-frobenius, \( \rho \coloneqq \rho(\A) \) is an eigenvalue of \( \A \); say \( \lambda_1 = \rho \). Suppose some \( \lambda_s \) with \( s \ge 2 \) had \( \lvert\lambda_s\rvert = \rho \) but \( \lambda_s \ne \rho \). Then \( \lambda_s^{k} \) is an eigenvalue of \( \A^{k} \) of modulus \( \rho^{k} = \rho(\A^{k}) \), so by Perron's theorem it is not an "other" eigenvalue: \( \lambda_s^{k} = \rho^{k} \). Then \( \rho^{k} \) occurs at least twice in the list \( \lambda_1^{k}, \dots, \lambda_n^{k} \), at positions \( 1 \) and \( s \), so \( a_{\A^{k}}(\rho^{k}) \ge 2 \), contradicting simplicity. Hence \( \rho \) is the only eigenvalue of modulus \( \rho \).
:::

Part (c) is the whole spectral content of primitivity, and the rest of the section shows that it is also enough. Part (a) says that once the powers become positive they stay positive, so the least such \( k \), the **exponent** of \( \A \), is well defined and marks a permanent change.

## The limit theorem

For the swap, \( \rho = 1 \) and the powers do not converge. We now show that primitivity is exactly what makes \( (\A/\rho)^{m} \) converge, and we identify the limit. The answer involves eigenvectors on both sides.

If \( \A \ge 0 \) is irreducible, then @thm-perron-frobenius (a) and @cor-left-perron-vector (a)–(c) provide \( \v > \0 \) and \( \w > \0 \) with \( \A\v = \rho(\A)\v \), \( \w\tp\A = \rho(\A)\w\tp \) and \( \w\tp\v > 0 \), and the right and left Perron vectors of @def-perron-root-and-vectors are the pair scaled so that \( \1\tp\v = 1 \) and \( \w\tp\v = 1 \). Each of \( \v, \w \) is determined up to a positive factor, because \( \rho(\A) \) is algebraically simple (@thm-perron-frobenius (b)), so its eigenspaces for \( \A \) and \( \A\tp \) are lines (@thm-geometric-le-algebraic, @prp-left-eigenvectors-transpose (b)).

::: {#thm-primitive-limit}
[Limit Theorem for Primitive Matrices]

Let \( \A \in M_n(\nR) \) be primitive, \( \rho = \rho(\A) \), and let \( \v > \0 \) and \( \w > \0 \) satisfy \( \A\v = \rho\v \) and \( \w\tp\A = \rho\w\tp \), for instance the right and left Perron vectors of \( \A \). Then, entrywise,
\[
\Big(\frac{1}{\rho}\A\Big)^{m} \longrightarrow \frac{\v\w\tp}{\w\tp\v} \qquad (m \to \infty).
\]
The limit is a positive matrix of rank one, and it does not depend on how \( \v \) and \( \w \) are scaled. The same conclusion holds for every irreducible \( \A \ge 0 \) with \( \rho(\A) > 0 \) whose only eigenvalue of modulus \( \rho(\A) \) is \( \rho(\A) \) itself.
:::

::: {.idea}
Divide by \( \rho \), so that the Perron eigenvalue becomes \( 1 \) and every other eigenvalue lies strictly inside the unit circle. Chapter 10 §10 then says the powers converge, with no diagonalizability needed, because it works with the Jordan form. It remains to name the limit \( \L \). Three identities pin it down: \( \B\L = \L \) puts every column of \( \L \) on the line through \( \v \); \( \L\B = \L \) puts every row on the line through \( \w\tp \); and \( \L\v = \v \) fixes the scale.
:::

::: {.proof}
It suffices to prove the last sentence, since a primitive matrix is irreducible with \( \rho(\A) > 0 \) and has \( \rho(\A) \) as its only eigenvalue of modulus \( \rho(\A) \), by @prp-primitive-basic (b) and (c).

So let \( \A \ge 0 \) be irreducible with \( \rho > 0 \) the only eigenvalue of modulus \( \rho \), and put \( \B = \rho^{-1}\A \). By @thm-spectral-mapping with \( q = x/\rho \), the eigenvalues of \( \B \) are the numbers \( \lambda/\rho \), \( \lambda \in \spec(\A) \), with the same algebraic multiplicities. So \( 1 \) is an eigenvalue of \( \B \) with \( a_{\B}(1) = a_{\A}(\rho) = 1 \) by @thm-perron-frobenius, and every other eigenvalue of \( \B \) has modulus less than \( 1 \). Since the \( 1 \)-blocks in a Jordan form of \( \B \) have total size \( a_{\B}(1) = 1 \) (@cor-jordan-invariants (a)), there is a single \( 1 \)-block, of size \( 1 \). By @thm-matrix-powers-converge, \( \B^{m} \) converges to some \( \L \in M_n(\nC) \).

*Three identities.* By the algebra of limits, (B3) of Chapter 10 §10, applied entry by entry, \( \B^{m+1} = \B\,\B^{m} \to \B\L \) and \( \B^{m+1} = \B^{m}\B \to \L\B \); but \( (\B^{m+1}) \) is a tail of \( (\B^{m}) \), so it also tends to \( \L \). Hence \( \B\L = \L = \L\B \). Also \( \B\v = \v \), so \( \B^{m}\v = \v \) for every \( m \), and letting \( m \to \infty \) gives \( \L\v = \v \).

*The columns.* \( \B\L = \L \) says that every column of \( \L \) lies in \( E_1(\B) = E_{\rho}(\A) \), which is the line \( \Span(\v) \), as noted before the theorem. So column \( j \) of \( \L \) is \( u_j\v \) for some \( u_j \in \nC \), that is, \( \L = \v\u\tp \) with \( \u = (u_1, \dots, u_n) \).

*The rows.* \( \L\B = \L \) reads \( \v(\u\tp\B) = \v\u\tp \). Choose \( r \) with \( v_r \ne 0 \) and compare row \( r \): \( \u\tp\B = \u\tp \), so \( \B\tp\u = \u \), and \( \u \) lies in the eigenspace of \( \A\tp \) for \( \rho \). That eigenspace is the line through \( \w \), so \( \u = c\w \) for some \( c \in \nC \).

*The scale.* Now \( \v = \L\v = c\,\v(\w\tp\v) \), and comparing entry \( r \) gives \( c\,\w\tp\v = 1 \). Since \( \w\tp\v > 0 \), \( c = 1/(\w\tp\v) \), and \( \L = \v\w\tp/(\w\tp\v) \).

Finally, \( \v\w\tp \) has \( (i,j) \)-entry \( v_iw_j > 0 \) and every column a multiple of \( \v \), so the limit is positive of rank one; replacing \( \v, \w \) by \( s\v, t\w \) with \( s, t > 0 \) multiplies numerator and denominator by \( st \). This proves the theorem.
:::

Note what the proof did **not** use: no eigenvector basis, no computation of the other eigenvalues. Chapter 10's Jordan-form criterion did the analysis once and for all; Perron–Frobenius supplied the simple eigenvalue and the two positive eigenvectors. With the normalization \( \w\tp\v = 1 \) of §03, the limit is simply the idempotent \( \v\w\tp \). §06 turns the theorem into the long-run theorem for Markov chains.

::: {#exm-primitive-limit-2x2}
[A Limit Computed Two Ways]

Let \( \A = \begin{pmatrix} 1 & 1 \\ 2 & 0 \end{pmatrix} \), which is primitive since \( \A^{2} > 0 \). Find \( \lim_m (\A/\rho)^{m} \) from @thm-primitive-limit, and confirm it with an exact formula for \( \A^{m} \).
:::

::: {.solution}
*The theorem.* \( p_{\A} = x^{2} - x - 2 = (x - 2)(x + 1) \), so \( \rho = 2 \). A positive right eigenvector solves \( (\A - 2\I)\v = \0 \), that is, \( -v_1 + v_2 = 0 \): take \( \v = (1, 1) \). A positive left eigenvector solves \( (\A\tp - 2\I)\w = \0 \), with \( \A\tp - 2\I = \begin{pmatrix} -1 & 2 \\ 1 & -2 \end{pmatrix} \): take \( \w = (2, 1) \). Then \( \w\tp\v = 3 \), and
\[
\Big(\frac{1}{2}\A\Big)^{m} \longrightarrow \L = \frac13\begin{pmatrix} 1 \\ 1 \end{pmatrix}\begin{pmatrix} 2 & 1 \end{pmatrix} = \frac13\begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix} .
\]
*The formula.* \( \L^{2} = \L \), because \( \w\tp\v/3 = 1 \), and \( \L(\I - \L) = \0 \). A direct check gives \( 3\L - \I = \begin{pmatrix} 1 & 1 \\ 2 & 0 \end{pmatrix} = \A \), so \( \A = 2\L - (\I - \L) \). Since \( \L \) and \( \I - \L \) are complementary projections, induction on \( m \) gives
\[
\begin{aligned}
\A^{m} &= 2^{m}\L + (-1)^{m}(\I - \L), \\
\Big(\frac12\A\Big)^{m} &= \L + \Big(-\frac12\Big)^{m}\frac13\begin{pmatrix} 1 & -1 \\ -2 & 2 \end{pmatrix} .
\end{aligned}
\]
For \( m = 2 \) this is \( \frac13\begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix} + \frac1{12}\begin{pmatrix} 1 & -1 \\ -2 & 2 \end{pmatrix} = \frac14\begin{pmatrix} 3 & 1 \\ 2 & 2 \end{pmatrix} \), which is \( \A^{2}/4 \). The error term is \( (-\frac12)^{m} \) times a fixed matrix: it decays at the rate \( \lvert\lambda_2\rvert/\rho = \frac12 \) and changes sign at every step.
:::

::: {.warning}
**The limit uses the left eigenvector, not the transpose of the right one.** For the matrix above, \( \v\v\tp/(\v\tp\v) = \frac12\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \), which is not the limit. The two agree when \( \A \) is symmetric, since then \( \w = \v \); in general \( \w \) carries the information about how much each starting index contributes in the long run.
:::

The limit theorem also gives the converse of @prp-primitive-basic (c).

::: {#thm-primitive-iff-single-peripheral}
[Primitivity from the Spectrum]

Let \( \A \in M_n(\nR) \), \( \A \ge 0 \), be irreducible with \( \rho(\A) > 0 \). Then \( \A \) is primitive if and only if \( \rho(\A) \) is the only eigenvalue of \( \A \) of modulus \( \rho(\A) \).
:::

::: {.idea}
One direction is already proved. For the other, the limit theorem gives a **positive** limit, and a sequence that converges to a positive number is eventually positive. There are only \( n^{2} \) entries to wait for, so some single power is positive everywhere.
:::

::: {.proof}
\( (\Rightarrow) \) This is @prp-primitive-basic (c).

\( (\Leftarrow) \) By the last sentence of @thm-primitive-limit, \( (\A/\rho)^{m} \to \L \) with \( \L > 0 \). Each of the \( n^{2} \) entries of \( (\A/\rho)^{m} \) converges to a positive number \( c_{ij} \), so it is positive for all \( m \) beyond some \( m_{ij} \): this is the definition of the limit with \( \varepsilon = c_{ij}/2 \). For \( m \) larger than the largest of these finitely many \( m_{ij} \), \( (\A/\rho)^{m} > 0 \), and hence \( \A^{m} = \rho^{m}(\A/\rho)^{m} > 0 \). So \( \A \) is primitive.
:::

The hypothesis \( \rho(\A) > 0 \) excludes only the \( 1 \times 1 \) zero matrix: for \( n \ge 2 \) it holds for every irreducible \( \A \ge 0 \) by @thm-perron-frobenius (d), and for \( n = 1 \), \( \rho((a)) = a \).

## The peripheral spectrum and the period

What does an irreducible, non-primitive matrix look like? The eigenvalues of modulus \( \rho(\A) \) are called the **peripheral eigenvalues** of \( \A \), and the theorem just proved says that a non-primitive irreducible matrix, other than the \( 1 \times 1 \) zero matrix, has more than one of them. For the swap they are \( \pm 1 \). For the \( 3 \times 3 \) cyclic permutation they are the three cube roots of unity, as we shall compute. The pattern is general, and it is controlled by a number read off the walks.

*The period is the common step size of all round trips.*

::: {#def-period}
[Period]

Let \( \A \in M_n(\nR) \), \( \A \ge 0 \), be irreducible and not the \( 1 \times 1 \) zero matrix. The **period** of \( \A \) is the greatest common divisor of the lengths of all closed walks in \( \A \).
:::

There is at least one closed walk, so the definition makes sense. If \( n = 1 \), then \( \A = (a) \) with \( a > 0 \), and the loop \( 1 \to 1 \) is a closed walk of length \( 1 \). If \( n \ge 2 \), then \( G(\A) \) is strongly connected (@thm-irreducible-iff-strongly-connected), so there are walks from \( 1 \) to \( 2 \) and from \( 2 \) to \( 1 \), and one followed by the other is a closed walk. For the swap, every edge joins \( 1 \) and \( 2 \), so closed walks have even length, and \( 1 \to 2 \to 1 \) has length \( 2 \): the period is \( 2 \). For \( \W \) above, closed walks of lengths \( 3 \) and \( 2 \) give period \( 1 \). A single positive diagonal entry \( a_{ii} \) is a loop \( i \to i \), a closed walk of length \( 1 \), and forces period \( 1 \).

The main theorem of this part says that the period counts the peripheral eigenvalues, and that they sit at the corners of a regular polygon. As in §01, \( \lvert\z\rvert = (\lvert z_1\rvert, \dots, \lvert z_n\rvert) \) is the entrywise absolute value of \( \z \in \nC^{n} \).

::: {#thm-peripheral-spectrum}
[The Peripheral Spectrum]

Let \( \A \in M_n(\nR) \), \( \A \ge 0 \), be irreducible and not the \( 1 \times 1 \) zero matrix. Put \( \rho = \rho(\A) \), let \( h \) be the number of **distinct** eigenvalues of \( \A \) of modulus \( \rho \), and let \( \omega = e^{2\pi i/h} \). Then:

::: {.enumerate options="label=(\alph*)"}
1. the eigenvalues of \( \A \) of modulus \( \rho \) are exactly \( \rho, \rho\omega, \rho\omega^{2}, \dots, \rho\omega^{h-1} \), and each is algebraically simple;
2. \( \A \) is similar to \( \omega\A \); in particular \( \spec(\A) \) is unchanged by multiplication by \( \omega \), with algebraic multiplicities;
3. \( h \) equals the period of \( \A \).
:::
:::

::: {.idea}
**Step roadmap.** ① Take an eigenvector \( \z \) for a peripheral eigenvalue \( \rho e^{i\theta} \). The triangle inequality (@thm-complex-triangle-inequality) gives \( \A\lvert\z\rvert \ge \rho\lvert\z\rvert \), and superinvariance (@prp-superinvariance) forces equality, so \( \lvert\z\rvert \) is a positive multiple of \( \v \). Equality in the triangle inequality then says all terms of each row sum point in the same direction, and that is a similarity \( \D^{-1}\A\D = e^{i\theta}\A \) with \( \D \) diagonal. ② So the spectrum is invariant under rotation by every peripheral angle, the peripheral points form a finite group of rotations, and a finite group of \( h \) points on the unit circle must be the \( h \)-th roots of unity. ③ The diagonal matrix \( \D \) records a phase at each vertex, and each edge advances the phase by one step; going round a closed walk returns the phase, which ties \( h \) to walk lengths.
:::

::: {.proof}
Recall that \( \rho > 0 \) (the remark after @thm-primitive-iff-single-peripheral), and let \( \v > \0 \) be an eigenvector of \( \A \) for \( \rho \) (@thm-perron-frobenius (a)).

**Step 1.** *Let \( \lambda = \rho e^{i\theta} \) be an eigenvalue. Then there are real numbers \( \varphi_1, \dots, \varphi_n \) such that \( e^{i\varphi_j} = e^{i\theta}e^{i\varphi_i} \) whenever \( a_{ij} > 0 \); consequently, with \( \D = \diag(e^{i\varphi_1}, \dots, e^{i\varphi_n}) \), we have \( \D^{-1}\A\D = e^{i\theta}\A \).*

Let \( \A\z = \lambda\z \) with \( \z \ne \0 \). By @lem-entrywise-absolute-value (a), with \( \lvert\A\rvert = \A \) since \( \A \ge 0 \), in each row
\[
\rho\,\lvert z_i\rvert = \lvert\lambda z_i\rvert = \Big\lvert\sum_j a_{ij}z_j\Big\rvert \le \sum_j a_{ij}\lvert z_j\rvert = (\A\lvert\z\rvert)_i .
\]
So \( \A\lvert\z\rvert \ge \rho\lvert\z\rvert \), where \( \lvert\z\rvert \ge \0 \) and \( \lvert\z\rvert \ne \0 \). If \( \A\lvert\z\rvert \ne \rho\lvert\z\rvert \), then @prp-superinvariance (b) with \( s = \rho \) would give \( \rho > \rho \); hence \( \A\lvert\z\rvert = \rho\lvert\z\rvert \). So \( \lvert\z\rvert \) is a non-negative eigenvector of \( \A \), and by @thm-perron-frobenius (c) it is a positive multiple of \( \v \). Therefore \( \lvert\z\rvert > \0 \), and we may write \( z_j = \lvert z_j\rvert e^{i\varphi_j} \) in polar form.

Now every inequality in the display is an equality. Fix \( i \). The number \( S = \sum_j a_{ij}z_j = \lambda z_i = \rho\lvert z_i\rvert e^{i(\theta + \varphi_i)} \) (@thm-polar-multiplication) is non-zero, since \( \rho > 0 \) and \( \lvert z_i\rvert > 0 \), and \( \lvert S\rvert = \sum_j\lvert a_{ij}z_j\rvert \). So @lem-triangle-equality-complex, applied to the \( n \) numbers \( a_{ij}z_j \), with \( S/\lvert S\rvert = e^{i(\theta + \varphi_i)} \), gives \( a_{ij}z_j = a_{ij}\lvert z_j\rvert e^{i(\theta + \varphi_i)} \) for every \( j \). If \( a_{ij} > 0 \), dividing by \( a_{ij}\lvert z_j\rvert > 0 \) gives \( e^{i\varphi_j} = e^{i(\theta + \varphi_i)} = e^{i\theta}e^{i\varphi_i} \). This is the first statement. For the second, the \( (i,j) \)-entry of \( \D^{-1}\A\D \) is \( e^{-i\varphi_i}a_{ij}e^{i\varphi_j} \), which is \( e^{i\theta}a_{ij} \) when \( a_{ij} > 0 \) and \( 0 = e^{i\theta}a_{ij} \) when \( a_{ij} = 0 \).

**Step 2.** *Proof of (a) and (b).* Write \( p_{\A} = (x - \lambda_1)\cdots(x - \lambda_n) \) over \( \nC \). For every peripheral \( \lambda = \rho e^{i\theta} \), Step 1 and @thm-charpoly-similarity-invariant give \( p_{\A} = p_{e^{i\theta}\A} \), and by @thm-spectral-mapping with \( q = e^{i\theta}x \),
\[
\begin{aligned}
(x - \lambda_1)\cdots(x - \lambda_n) &= p_{\A} = p_{e^{i\theta}\A} \\
&= (x - e^{i\theta}\lambda_1)\cdots(x - e^{i\theta}\lambda_n) .
\end{aligned}
\]
So multiplication by \( e^{i\theta} \) permutes the eigenvalues listed with multiplicity:
\[
a_{\A}(e^{i\theta}\mu) = a_{\A}(\mu) \qquad \text{for every } \mu \in \nC .
\]

Let \( G = \{\lambda/\rho : \lambda \in \spec(\A),\ \lvert\lambda\rvert = \rho\} \), a set of \( h \) complex numbers of modulus \( 1 \) containing \( 1 \), because \( \rho \in \spec(\A) \) by @thm-perron-frobenius. If \( g = e^{i\theta} \) and \( g' \) lie in \( G \), then \( \rho g' \in \spec(\A) \), so \( g\rho g' \in \spec(\A) \) by the invariance just proved, and it has modulus \( \rho \): thus \( gg' \in G \). For fixed \( g \in G \), the map \( G \to G \), \( x \mapsto gx \), is injective, since \( g \ne 0 \); as \( G \) is finite it is a bijection. Hence the product \( \Pi \) of all elements of \( G \) satisfies \( \Pi = \prod_{x \in G} gx = g^{h}\,\Pi \), and \( \Pi \ne 0 \), so \( g^{h} = 1 \). So \( G \) is contained in the set of \( h \)-th roots of unity, which has exactly \( h \) elements \( 1, \omega, \dots, \omega^{h-1} \) (@exm-roots-of-unity). Both sets have \( h \) elements, so they are equal. This proves the first half of (a).

Each \( \rho\omega^{j} \) has \( a_{\A}(\rho\omega^{j}) = a_{\A}(\rho) = 1 \), by the invariance with \( e^{i\theta} = \omega^{j} \) and @thm-perron-frobenius. This proves (a). Taking \( \lambda = \rho\omega \) in Step 1 gives (b).

**Step 3.** *Proof of (c).* Let \( d \) be the period.

*\( h \) divides \( d \).* Apply Step 1 to \( \lambda = \rho\omega \), so \( e^{i\theta} = \omega \). Along a closed walk \( i_0 \to i_1 \to \dots \to i_L = i_0 \) each entry \( a_{i_ti_{t-1}} \) is positive, so Step 1 gives \( e^{i\varphi_{i_{t-1}}} = \omega e^{i\varphi_{i_t}} \) for each \( t \), and chaining these \( L \) equations gives \( e^{i\varphi_{i_0}} = \omega^{L}e^{i\varphi_{i_L}} = \omega^{L}e^{i\varphi_{i_0}} \). So \( \omega^{L} = 1 \), and \( h \) divides \( L \) (@exm-roots-of-unity). As this holds for every closed walk, \( h \) divides \( d \).

*\( d \) divides \( h \).* If \( n = 1 \) then \( d = 1 \). Let \( n \ge 2 \). Since \( G(\A) \) is strongly connected (@thm-irreducible-iff-strongly-connected), every vertex \( j \) is joined to vertex \( 1 \) by walks in both directions; for \( j = 1 \) this includes the walk of length \( 0 \). Choose for each \( j \) the length \( \ell_j \) of some walk from \( 1 \) to \( j \), with \( \ell_1 = 0 \). Any two walks from \( 1 \) to \( j \), of lengths \( \ell \) and \( \ell' \), have lengths congruent modulo \( d \): following either by a fixed walk from \( j \) back to \( 1 \), of length \( s \), gives closed walks of lengths \( \ell + s \) and \( \ell' + s \) (or length \( 0 \), trivially a multiple of \( d \)), both multiples of \( d \). Now if \( a_{ij} > 0 \), a walk from \( 1 \) to \( j \) followed by the edge \( j \to i \) is a walk from \( 1 \) to \( i \) of length \( \ell_j + 1 \), so \( \ell_i \equiv \ell_j + 1 \pmod d \). Put \( \zeta = e^{2\pi i/d} \) and \( \E = \diag(\zeta^{-\ell_1}, \dots, \zeta^{-\ell_n}) \). Then the \( (i,j) \)-entry of \( \E^{-1}\A\E \) is \( \zeta^{\ell_i - \ell_j}a_{ij} = \zeta a_{ij} \) when \( a_{ij} > 0 \), since \( \zeta^{d} = 1 \), and \( 0 \) otherwise. So \( \E^{-1}\A\E = \zeta\A \). As in Step 2, \( \spec(\A) = \zeta\spec(\A) \), so \( \zeta\rho \in \spec(\A) \), with modulus \( \rho \). By (a), \( \zeta = \omega^{j} \) for some \( j \), so \( \zeta^{h} = (\omega^{h})^{j} = 1 \), and \( d \) divides \( h \): \( e^{2\pi ih/d} = 1 = e^{2\pi i\cdot 0/d} \), and two integers \( k, l \) give the same number \( e^{2\pi ik/d} = e^{2\pi il/d} \) only when \( d \) divides \( k - l \) (@exm-roots-of-unity).

Both \( h \) and \( d \) are positive, so \( h = d \). This proves the theorem.
:::

The two halves of Step 3 are mirror images. The diagonal similarity attached to a peripheral eigenvalue is a consistent labeling of the indices by \( h \) phases, with every positive entry advancing the phase by one; the walks of \( \A \) build such a labeling with \( d \) phases.

Combining (c) with @thm-primitive-iff-single-peripheral gives a test that needs no eigenvalues at all.

::: {#cor-primitive-iff-aperiodic}
[Primitivity from Walks]

Let \( \A \in M_n(\nR) \), \( \A \ge 0 \), be irreducible and not the \( 1 \times 1 \) zero matrix. Then \( \A \) is primitive if and only if its period is \( 1 \). In particular, an irreducible \( \A \ge 0 \) with at least one positive diagonal entry is primitive.
:::

::: {.proof}
Since \( \A \) is not the \( 1 \times 1 \) zero matrix, \( \rho(\A) > 0 \) by the remark after @thm-primitive-iff-single-peripheral. So by that theorem, \( \A \) is primitive if and only if \( h = 1 \), and \( h \) is the period by @thm-peripheral-spectrum (c). A positive diagonal entry is a closed walk of length \( 1 \), so the period divides \( 1 \).
:::

## The cyclic permutation

The standard irreducible matrix that is not primitive is the cyclic shift. It generalizes Chapter 9's swap, and it shows every part of @thm-peripheral-spectrum at once.

::: {#exm-cyclic-permutation}
[The Cyclic Permutation]

Let \( n \ge 2 \) and let \( \sigma \in S_n \) send \( j \mapsto j + 1 \) for \( j < n \) and \( n \mapsto 1 \). Its permutation matrix \( \P = \P_\sigma \) (@def-permutation-matrix) has columns \( \e_2, \e_3, \dots, \e_n, \e_1 \). Show that \( \P \) is irreducible with period \( n \), find its peripheral eigenvalues, and show that \( \P^{m} \) does not converge.
:::

::: {.solution}
*Walks.* The non-zero entries of \( \P \) are \( p_{j+1,\,j} \) for \( j < n \) and \( p_{1n} \), so the edges of \( G(\P) \) are \( j \to j + 1 \) for \( j < n \) and \( n \to 1 \): the graph is the cycle \( 1 \to 2 \to \dots \to n \to 1 \). Every walk runs round it, and a closed walk goes round a whole number of times, so its length is a multiple of \( n \); the walk \( 1 \to 2 \to \dots \to n \to 1 \) has length \( n \). So the period is \( n \). Following the cycle, every vertex reaches every vertex, so \( G(\P) \) is strongly connected and \( \P \) is irreducible (@thm-irreducible-iff-strongly-connected).

*Eigenvalues.* Since \( \P\e_j = \e_{\sigma(j)} \) and \( \sigma^{n} \) is the identity, \( \P^{n}\e_j = \e_j \) for every \( j \), so \( \P^{n} = \I \). If \( \P\z = \lambda\z \) with \( \z \ne \0 \), then \( \z = \P^{n}\z = \lambda^{n}\z \), so \( \lambda^{n} = 1 \) and \( \lvert\lambda\rvert = 1 \). Hence \( \rho(\P) = 1 \) and **every** eigenvalue is peripheral. By @thm-peripheral-spectrum, \( h = n \), so the peripheral eigenvalues are the \( n \) numbers \( 1, \omega, \dots, \omega^{n-1} \), \( \omega = e^{2\pi i/n} \), each algebraically simple. That accounts for all \( n \) eigenvalues, and \( p_{\P} = (x - 1)(x - \omega)\cdots(x - \omega^{n-1}) = x^{n} - 1 \), the last equality because both sides are monic of degree \( n \) with the same \( n \) distinct roots.

*Powers.* \( \P^{n} = \I \), so the sequence \( \P, \P^{2}, \dots \) repeats with period \( n \), and \( \P^{m} \) runs through \( n \) distinct permutation matrices. A sequence that returns to each of two different matrices infinitely often has no limit, so \( \P^{m} \) does not converge. Starting a chain at \( \e_1 \), \( \P^{m}\e_1 \) runs round \( \e_1, \e_2, \dots, \e_n, \e_1, \dots \) forever, although \( \P \) has the steady state \( \frac1n\1 \).
:::

For \( n = 2 \) this is exactly the warning in Chapter 9 §11: the swap has the eigenvalue \( -1 = e^{2\pi i/2} \), and Chapter 10 §10 identified an eigenvalue of modulus \( 1 \) other than \( 1 \) as the only obstruction to convergence (@cor-markov-powers-converge). We now know where that eigenvalue comes from. It is forced by the period: every closed walk has even length. §06 shows that the chain still settles down **on average**.

## How large a power is needed

The definition of primitivity asks for some \( \A^{k} > 0 \) but gives no bound on \( k \), so a direct check might seem to require computing powers without end. By @lem-powers-and-walks (a), the zero pattern of \( \A^{m} \) depends only on the zero pattern of \( \A \), and there are finitely many patterns, so in principle the question is finite. The sharp answer is classical.

::: {#thm-wielandt-bound}
[Wielandt's Bound]

If \( \A \in M_n(\nR) \) is primitive, then \( \A^{(n-1)^{2}+1} > 0 \). The bound cannot be improved: for \( n \ge 2 \) the matrix \( \W_n \) with ones at the positions \( (i, i+1) \) for \( i < n \) and at \( (n, 1) \) and \( (n, 2) \), and zeros elsewhere, is primitive and \( \W_n^{(n-1)^{2}} \) has a zero entry.
:::

This theorem is due to H. Wielandt (1950). **We state it without proof**; the proof is a careful count of walk lengths, and nothing in this book depends on it. The matrix \( \W_3 \) is the matrix \( \W \) of the examples, where we saw that \( \W^{4} \) has a zero at position \( (1, 1) \) and \( \W^{5} > 0 \); here \( (n-1)^{2} + 1 = 5 \). In the walks: a closed walk at \( 1 \) must leave by \( 1 \to 3 \) and return by \( 2 \to 1 \), so it is made of \( 3 \)-cycles \( 1 \to 3 \to 2 \to 1 \) and detours round \( 3 \to 2 \to 3 \), and its length \( 3 + 3a + 2b \), with \( a, b \ge 0 \), is never \( 4 \). For \( n = 4 \) the bound is \( 10 \), and \( \W_4^{9} \) is not positive while \( \W_4^{10} \) is.

::: {.remark}
The bound is quadratic in \( n \), not \( n - 1 \) as for \( (\I + \A)^{n-1} \) in @thm-irreducible-power-positive. Adding \( \I \) puts a loop at every vertex, which lets walks wait; a primitive matrix may have no such loops, and then the walks must make up lengths from long cycles, as \( \W_n \) does with its cycles of lengths \( n \) and \( n - 1 \).
:::

## Exercises

### A. Check your understanding

:::: {#exr-primitive-matrices-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define a primitive matrix, and state the limit theorem for primitive matrices.
2. True or false: every primitive matrix is irreducible. Justify your answer.
3. True or false: every irreducible non-negative matrix is primitive. Justify your answer.
4. True or false: if \( \A \ge 0 \) is irreducible and \( a_{11} > 0 \), then \( \A \) is primitive. Justify your answer.
5. An irreducible \( \A \ge 0 \) has \( \rho(\A) = 2 \) and period \( 4 \). Which of its eigenvalues can you name without further information?
6. Name the two ingredients from earlier chapters that the proof of @thm-primitive-limit combines.
:::
::::

::: {.solution}
(a) \( \A \in M_n(\nR) \), \( \A \ge 0 \), is primitive if \( \A^{k} > 0 \) for some \( k \ge 1 \) (@def-primitive). @thm-primitive-limit: if \( \A \) is primitive with \( \rho = \rho(\A) \), and \( \v > \0 \), \( \w > \0 \) satisfy \( \A\v = \rho\v \) and \( \w\tp\A = \rho\w\tp \), then \( (\A/\rho)^{m} \to \v\w\tp/(\w\tp\v) \) entrywise.

(b) True, by @prp-primitive-basic (b).

(c) False. The swap \( \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) is irreducible, but each of its powers is \( \I \) or the swap, and both have zero entries.

(d) True, by @cor-primitive-iff-aperiodic: the loop \( 1 \to 1 \) is a closed walk of length \( 1 \), so the period is \( 1 \). (If \( n = 1 \), then \( \A = (a_{11}) \) with \( a_{11} > 0 \) is primitive directly.)

(e) By @thm-peripheral-spectrum, \( h = 4 \), so the eigenvalues of modulus \( 2 \) are \( 2, 2i, -2, -2i \), each algebraically simple. The others cannot be named, but they come in orbits of multiplication by \( i \), by part (b) of that theorem.

(f) The Jordan-form convergence criterion of Chapter 10 §10 (@thm-matrix-powers-converge), which gives convergence of \( (\A/\rho)^{m} \); and the Perron–Frobenius theorem (@thm-perron-frobenius), which gives the simple eigenvalue \( \rho \) and the positive vectors \( \v, \w \) that identify the limit.
:::

### B. Practice

:::: {#exr-primitive-matrices-b1}
[B1: Which are primitive?]

Determine which of the following matrices are primitive. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix} \).
2. \( \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix} \).
3. \( \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix} \).
4. \( \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix} \).
:::
::::

::: {.solution}
(a) Primitive: its square is \( \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} > 0 \).

(b) Not primitive. It is the cyclic permutation matrix of @exm-cyclic-permutation with \( n = 3 \) (columns \( \e_3, \e_1, \e_2 \), the same shift run the other way), and every power of a permutation matrix is a permutation matrix (@lem-permutation-matrices), which has zero entries.

(c) Not primitive. The positive entries are at \( (1,2), (2,1), (2,3), (3,2) \), so the edges of \( G(\A) \) are \( 1 \to 2 \), \( 2 \to 1 \), \( 2 \to 3 \) and \( 3 \to 2 \), and every edge joins vertex \( 2 \) to the set \( \{1, 3\} \). A closed walk therefore has even length, and \( 1 \to 2 \to 1 \) has length \( 2 \): the matrix has period \( 2 \). It is irreducible, since every vertex reaches every other through \( 2 \), so \( G(\A) \) is strongly connected (@thm-irreducible-iff-strongly-connected). By @cor-primitive-iff-aperiodic it is not primitive. (Directly: \( \A^{m} \) has zero \( (1,2) \)-entry for even \( m \) and zero \( (1,1) \)-entry for odd \( m \).)

(d) Not primitive. The positive entries sit at positions \( (i, j) \) with \( i \le j \), so every edge \( j \to i \) has \( i \le j \), vertex numbers never increase along a walk, and there is no walk from \( 1 \) to \( 2 \). By @lem-powers-and-walks (a), the \( (2,1) \)-entry of every power is \( 0 \).
:::

:::: {#exr-primitive-matrices-b2}
[B2: A limit without diagonalizing]

Let \( \A = \begin{pmatrix} 0 & 0 & 1 \\ 2 & 0 & 1 \\ 2 & 1 & 0 \end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \A \) is primitive.
2. Show that \( p_{\A} = (x - 2)(x + 1)^{2} \), and that \( \A \) is **not** diagonalizable.
3. Find positive right and left eigenvectors for \( \rho(\A) \), and hence \( \lim_m (\A/2)^{m} \).
:::
::::

::: {.solution}
(a) Compute
\[
\A^{2} = \begin{pmatrix} 2 & 1 & 0 \\ 2 & 1 & 2 \\ 2 & 0 & 3 \end{pmatrix}, \qquad \A^{4} = (\A^{2})^{2} = \begin{pmatrix} 6 & 3 & 2 \\ 10 & 3 & 8 \\ 10 & 2 & 9 \end{pmatrix} > 0 .
\]
So \( \A \) is primitive.

(b) Here \( x\I - \A = \begin{pmatrix} x & 0 & -1 \\ -2 & x & -1 \\ -2 & -1 & x \end{pmatrix} \), and expansion along the first row gives
\[
\begin{aligned}
p_{\A} &= x\bigl(x^{2} - 1\bigr) + (-1)\bigl((-2)(-1) - x(-2)\bigr) \\
&= x^{3} - x - 2 - 2x = x^{3} - 3x - 2 .
\end{aligned}
\]
Since \( (x - 2)(x + 1)^{2} = (x - 2)(x^{2} + 2x + 1) = x^{3} - 3x - 2 \), this is the claimed factorization. For \( \lambda = -1 \), \( \A + \I = \begin{pmatrix} 1 & 0 & 1 \\ 2 & 1 & 1 \\ 2 & 1 & 1 \end{pmatrix} \) has rank \( 2 \) (rows 2 and 3 agree, rows 1 and 2 are independent), so \( g_{\A}(-1) = 1 < 2 = a_{\A}(-1) \), and \( \A \) is not diagonalizable.

(c) \( \A - 2\I = \begin{pmatrix} -2 & 0 & 1 \\ 2 & -2 & 1 \\ 2 & 1 & -2 \end{pmatrix} \): the first row gives \( v_3 = 2v_1 \), and then the second gives \( 2v_1 - 2v_2 + 2v_1 = 0 \), so \( v_2 = 2v_1 \). Take \( \v = (1, 2, 2) \); check: \( \A\v = (2, 4, 4) \). For the left vector, \( \A\tp - 2\I = \begin{pmatrix} -2 & 2 & 2 \\ 0 & -2 & 1 \\ 1 & 1 & -2 \end{pmatrix} \): the second row gives \( w_3 = 2w_2 \), and the first gives \( w_1 = w_2 + w_3 = 3w_2 \). Take \( \w = (3, 1, 2) \); check: \( \w\tp\A = (0 + 2 + 4,\ 0 + 0 + 2,\ 3 + 1 + 0) = (6, 2, 4) = 2\w\tp \). Then \( \w\tp\v = 3 + 2 + 4 = 9 \), and by @thm-primitive-limit
\[
\Big(\frac12\A\Big)^{m} \longrightarrow \frac19\begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix}\begin{pmatrix} 3 & 1 & 2 \end{pmatrix} = \frac19\begin{pmatrix} 3 & 1 & 2 \\ 6 & 2 & 4 \\ 6 & 2 & 4 \end{pmatrix} .
\]
Part (b) shows that Chapter 9's diagonalization method is unavailable here; the theorem does not need it.
:::

:::: {#exr-primitive-matrices-b3}
[B3: Period and peripheral eigenvalues]

Let \( \A = \begin{pmatrix} 0 & 1 & 0 \\ 2 & 0 & 2 \\ 0 & 1 & 0 \end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \A \) is irreducible with period \( 2 \).
2. Use @thm-peripheral-spectrum to predict the eigenvalues of modulus \( \rho(\A) \) in terms of \( \rho(\A) \), then compute \( p_{\A} \) and confirm.
3. Hence explain why \( (\A/\rho(\A))^{m} \) does not converge.
:::
::::

::: {.solution}
(a) The positive entries are at \( (1,2), (2,1), (2,3), (3,2) \), the same pattern as in B1(c), so the argument there applies: \( \A \) is irreducible with period \( 2 \).

(b) With \( h = 2 \) and \( \omega = -1 \), the peripheral eigenvalues are \( \rho \) and \( -\rho \), and the spectrum is symmetric under \( \lambda \mapsto -\lambda \). Expanding along the first row,
\[
p_{\A} = \det\begin{pmatrix} x & -1 & 0 \\ -2 & x & -2 \\ 0 & -1 & x \end{pmatrix} = x(x^{2} - 2) + 1\cdot(-2x) = x(x - 2)(x + 2) .
\]
So \( \rho = 2 \), the peripheral eigenvalues are \( \pm 2 \), and the remaining eigenvalue \( 0 \) is its own negative, as predicted.

(c) The vector \( \z = (1, -2, 1) \) satisfies \( \A\z = (-2, 4, -2) = -2\z \), so \( \A/2 \) has the eigenvalue \( -1 \). By @thm-matrix-powers-converge, the powers of a matrix with an eigenvalue of modulus \( 1 \) other than \( 1 \) do not converge. Concretely, \( (\A/2)^{m}\z = (-1)^{m}\z \) alternates in sign.
:::

### C. Going deeper

:::: {#exr-primitive-matrices-c1}
[C1: Shifting by the identity]

Let \( \A \in M_n(\nR) \), \( \A \ge 0 \), be irreducible, with right and left Perron vectors \( \v, \w \), and let \( t > 0 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \A + t\I \) is primitive, with \( \rho(\A + t\I) = \rho(\A) + t \) and the same Perron vectors \( \v, \w \).
2. Deduce that \( \bigl((\A + t\I)/(\rho(\A) + t)\bigr)^{m} \to \v\w\tp/(\w\tp\v) \), and apply this to the swap with \( t = 1 \).
:::
::::

::: {.solution}
(a) \( \A + t\I \ge 0 \) has the same off-diagonal pattern as \( \A \), so \( (\I + \A + t\I)^{n-1} \ge (\I + \A)^{n-1} > 0 \) entrywise, since each product of non-negative matrices can only grow when an entry grows; so \( \A + t\I \) is irreducible (@thm-irreducible-power-positive). Its diagonal entries are \( \ge t > 0 \), so it is primitive by @cor-primitive-iff-aperiodic. By @thm-spectral-mapping with \( q = x + t \), its eigenvalues are \( \lambda + t \), \( \lambda \in \spec(\A) \), and \( \lvert\lambda + t\rvert \le \lvert\lambda\rvert + t \le \rho(\A) + t \) by @thm-complex-triangle-inequality, with \( \rho(\A) + t \) itself an eigenvalue, since \( \rho(\A) \in \spec(\A) \). So \( \rho(\A + t\I) = \rho(\A) + t \). Finally \( (\A + t\I)\v = (\rho(\A) + t)\v \) and \( \w\tp(\A + t\I) = (\rho(\A) + t)\w\tp \), with \( \v, \w > \0 \).

(b) By (a) and @thm-primitive-limit applied to \( \A + t\I \). For the swap \( \S \), \( \rho = 1 \), and \( \1 \) is a positive right and left eigenvector, so the limit is \( \1\1\tp/(\1\tp\1) = \1\1\tp/2 \). Directly, \( (\S + \I)/2 = \frac12\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \), whose powers are all equal to itself, in agreement.
:::

:::: {#exr-primitive-matrices-c2}
[C2: Traces detect the period]

Let \( \A \ge 0 \) be irreducible, not the \( 1 \times 1 \) zero matrix, with period \( h \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \tr(\A^{m}) = 0 \) for every \( m \ge 1 \) that is not a multiple of \( h \), in two ways: from @thm-peripheral-spectrum (b), and from @lem-powers-and-walks (a).
2. Deduce that if \( \tr(\A^{2}) > 0 \) and \( \tr(\A^{3}) > 0 \), then \( \A \) is primitive.
3. Check (b) on the matrix \( \W \) of the examples.
:::
::::

::: {.solution}
(a) *Spectrum.* Let \( \omega = e^{2\pi i/h} \) and \( p_{\A} = \prod_i(x - \lambda_i) \). By @thm-peripheral-spectrum (c), the period \( h \) is also the number of peripheral eigenvalues, so part (b) of that theorem applies with this \( \omega \). By @cor-trace-det-of-polynomial, applied over \( \nC \), \( \tr(\A^{m}) = \sum_i\lambda_i^{m} \). By @thm-peripheral-spectrum (b), the list \( \omega\lambda_1, \dots, \omega\lambda_n \) is a rearrangement of \( \lambda_1, \dots, \lambda_n \), so \( \sum_i\lambda_i^{m} = \sum_i(\omega\lambda_i)^{m} = \omega^{m}\sum_i\lambda_i^{m} \). If \( h \nmid m \), then \( \omega^{m} \ne 1 \) (@exm-roots-of-unity), so \( \tr(\A^{m}) = 0 \).

*Walks.* \( \tr(\A^{m}) = \sum_i(\A^{m})_{ii} \) is a sum of non-negative terms, positive exactly when some \( (\A^{m})_{ii} > 0 \), that is, by @lem-powers-and-walks (a), when there is a closed walk of length \( m \). Every closed walk has length a multiple of the period, so for \( h \nmid m \) the trace is \( 0 \).

(b) By (a), \( h \mid 2 \) and \( h \mid 3 \), so \( h = 1 \), and \( \A \) is primitive by @cor-primitive-iff-aperiodic.

(c) \( \W^{2} = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix} \) has trace \( 2 \), and \( \W^{3} = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix} \) has trace \( 3 \); so \( \W \) is primitive, as found directly.
:::

:::: {#exr-primitive-matrices-c3}
[C3: A finite test for primitivity]

Let \( \A \in M_n(\nR) \), \( \A \ge 0 \), and let \( \Z_m \) be the zero pattern of \( \A^{m} \): the \( 0/1 \) matrix with a \( 1 \) exactly where \( \A^{m} \) is positive.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \Z_{m+1} \) is determined by \( \Z_m \) and \( \Z_1 \).
2. Deduce that if \( \Z_a = \Z_b \) with \( a < b \), then \( \Z_{a+j} = \Z_{b+j} \) for every \( j \ge 0 \).
3. Prove that if \( \A \) is primitive, then \( \A^{k} > 0 \) for some \( k \le 2^{n^{2}} \). Compare with @thm-wielandt-bound.
:::

*Hint: there are only \( 2^{n^{2}} \) zero patterns; use @prp-primitive-basic (a).*
::::

::: {.solution}
(a) \( (\A^{m+1})_{ij} = \sum_l(\A^{m})_{il}a_{lj} \) is a sum of non-negative terms, positive exactly when some \( l \) has \( (\A^{m})_{il} > 0 \) and \( a_{lj} > 0 \). So \( (\Z_{m+1})_{ij} = 1 \) if and only if \( (\Z_m)_{il} = (\Z_1)_{lj} = 1 \) for some \( l \), which depends only on \( \Z_m \) and \( \Z_1 \).

(b) By induction on \( j \): the case \( j = 0 \) is the hypothesis, and if \( \Z_{a+j} = \Z_{b+j} \), then (a) applied to both gives \( \Z_{a+j+1} = \Z_{b+j+1} \).

(c) Among \( \Z_1, \dots, \Z_{N+1} \), \( N = 2^{n^{2}} \), two agree, say \( \Z_a = \Z_b \) with \( a < b \le N + 1 \), so \( a \le N \). By (b), \( \Z_{a + q(b-a)} = \Z_a \) for every \( q \ge 0 \), by induction on \( q \). If \( \A^{k} > 0 \), then by @prp-primitive-basic (a) \( \A^{m} > 0 \) for all \( m \ge k \); choosing \( q \) with \( a + q(b - a) \ge k \) shows that \( \Z_a \) is the all-ones pattern, so \( \A^{a} > 0 \) with \( a \le 2^{n^{2}} \). Wielandt's bound \( (n-1)^{2} + 1 \) is enormously smaller: for \( n = 3 \) it is \( 5 \) against \( 512 \).
:::
