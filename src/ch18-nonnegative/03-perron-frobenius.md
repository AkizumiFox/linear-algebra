# The Perron–Frobenius Theorem

Section 1 proved Perron's theorem (@thm-perron): a matrix with **every** entry positive has its spectral radius as a simple eigenvalue, with an eigenvector whose entries are all positive. That hypothesis is rarely met in practice. A Markov chain whose states can only step to their neighbors has a transition matrix full of zeros, and so does the matrix of almost any network. This section asks which of Perron's conclusions survive when zeros are allowed. There are two answers. For **every** non-negative matrix, the spectral radius is still an eigenvalue with a non-negative eigenvector, and of Perron's conclusions nothing more survives. For an **irreducible** matrix, in the sense of Section 2, every conclusion survives except one: other eigenvalues may reach the spectral radius in modulus. The positivity of the spectral radius also needs \( n \ge 2 \), because the \( 1 \times 1 \) zero matrix counts as irreducible.

Throughout, matrices have real entries, and \( \A \ge 0 \), \( \A > 0 \), \( \x \ge \0 \) and \( \x > \0 \) are the entrywise order of Section 1. The spectrum is read in \( \nC \), as in @def-spectral-radius, so \( \rho(\A) \) is the largest modulus of a complex eigenvalue. We write \( \J \) for the \( n \times n \) matrix with every entry \( 1 \), and \( \1 \) for the all-ones vector.

## What survives for every non-negative matrix

Start with the weakest hypothesis, \( \A \ge 0 \), and see what can be rescued. Three small matrices show at once that most of Perron's theorem is lost.

::: {#exm-perron-conclusions-lost}
[Three non-negative matrices that break Perron's theorem]

For each matrix, find \( \rho \), its algebraic multiplicity, and all the non-negative eigenvectors, and say which conclusion of @thm-perron fails:
\[
\N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \qquad
\A_c = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & c \end{pmatrix}
\quad\text{with } c = 2 \text{ and with } c = 1 .
\]
:::

::: {.solution}
*The nilpotent matrix.* \( \N \) is upper triangular with zero diagonal, so its only eigenvalue is \( 0 \), with algebraic multiplicity \( 2 \) (@thm-diagonal-of-triangular-form (b)), and \( \rho(\N) = 0 \). The eigenvectors are the non-zero solutions of \( \N\x = \0 \), that is, of \( x_2 = 0 \): the non-zero multiples of \( \e_1 \). So \( \rho = 0 \) is not positive, it is not simple, and no eigenvector is positive. What does survive is that \( \rho(\N) = 0 \) is an eigenvalue with the non-negative eigenvector \( \e_1 \).

*The block matrix.* \( \A_c \) is block diagonal, with the \( 2 \times 2 \) block \( \begin{psmallmatrix} 1 & 1 \\ 1 & 1 \end{psmallmatrix} \) and the \( 1 \times 1 \) block \( (c) \). The \( 2 \times 2 \) block has trace \( 2 \) and determinant \( 0 \), so its eigenvalues are \( 2 \) and \( 0 \), with eigenvectors \( (1, 1) \) and \( (1, -1) \). Hence \( p_{\A_c}(t) = t(t - 2)(t - c) \), and the eigenvectors of \( \A_c \) are built from those of the blocks: \( (1, 1, 0) \) for \( 2 \), \( (1, -1, 0) \) for \( 0 \), and \( \e_3 \) for \( c \).

For \( c = 2 \): \( \rho = 2 \) has algebraic multiplicity \( 2 \). Its eigenspace is spanned by \( (1, 1, 0) \) and \( \e_3 \), which are non-negative and not proportional, so the non-negative eigenvector is **not unique up to scale**. (It does contain the positive vector \( (1, 1, 1) \), their sum.)

For \( c = 1 \): \( \rho = 2 \) is simple, but its eigenvectors are the multiples of \( (1, 1, 0) \), none of them positive. And \( \e_3 \ge \0 \) is an eigenvector for the eigenvalue \( 1 < \rho \): a **non-negative eigenvector for a smaller eigenvalue**, which @thm-perron rules out for positive matrices.
:::

In each case \( \rho \) was still an eigenvalue with a non-negative eigenvector. That is the part that survives in general, and of Perron's conclusions it is all that survives. The proof is the first real use in the book of a *limiting auxiliary matrix* with a non-negative matrix in the limit. Perron's theorem applies to \( \A + \varepsilon\J \), which is positive for every \( \varepsilon > 0 \); let \( \varepsilon \to 0^{+} \) and keep whatever passes to the limit.

::: {#thm-nonnegative-rho-eigenvalue}
[The Spectral Radius of a Non-negative Matrix Is an Eigenvalue]

Let \( \A \in M_n(\nR) \) with \( n \ge 1 \) and \( \A \ge 0 \). Then \( \rho(\A) \) is an eigenvalue of \( \A \), and there is a vector \( \x \in \nR^n \) with \( \x \ge \0 \), \( \x \neq \0 \) and \( \A\x = \rho(\A)\x \).
:::

::: {.idea}
① Perturb: \( \A_k = \A + \frac1k\J \) is positive, so @thm-perron gives it an eigenvalue \( \rho(\A_k) \) with a positive eigenvector \( \v_k \), which we scale into the simplex \( \Delta_n \). ② The matrices \( \A_k \) decrease as \( k \) grows, so by monotonicity the numbers \( \rho(\A_k) \) decrease and stay \( \ge \rho(\A) \); by monotone convergence they have a limit \( r \ge \rho(\A) \). ③ The \( \v_k \) need not converge, but they live in a closed bounded set, so a subsequence does. ④ Pass to the limit in \( \A_k\v_k = \rho(\A_k)\v_k \): the limit equation makes \( r \) an eigenvalue of \( \A \), so \( r \le \rho(\A) \), and \( r = \rho(\A) \). The scaling into \( \Delta_n \) is what stops the limit vector from being \( \0 \): its entries still add up to \( 1 \).
:::

::: {.proof}
Let \( \rho = \rho(\A) \), and for each integer \( k \ge 1 \) put \( \A_k = \A + \frac1k\J \). Every entry of \( \A_k \) is at least \( \frac1k > 0 \), so \( \A_k > 0 \). By @thm-perron, \( \rho_k \coloneqq \rho(\A_k) \) is an eigenvalue of \( \A_k \) with an eigenvector \( \v_k > \0 \). Dividing \( \v_k \) by the sum of its entries, which is positive, we may assume \( \v_k \in \Delta_n \) (@def-standard-simplex).

**Step 1: \( \rho_k \) converges to some \( r \ge \rho \).** Since \( \frac{1}{k+1} < \frac1k \) and \( \J \ge 0 \), we have \( 0 \le \A \le \A_{k+1} \le \A_k \) entrywise for every \( k \). By @prp-spectral-radius-monotone (a), applied to each of these two inequalities, \( \rho \le \rho_{k+1} \le \rho_k \). So the sequence \( (-\rho_k) \) is increasing and bounded above by \( -\rho \). By monotone convergence, fact (A2) of Chapter 15's introduction, it converges to its least upper bound, which is \( \le -\rho \) because \( -\rho \) is an upper bound. Hence \( \rho_k \to r \) for some real number \( r \ge \rho \).

**Step 2: a convergent subsequence.** The set \( \Delta_n \) is bounded, since every entry of a point of \( \Delta_n \) lies in \( [0, 1] \). It is closed: if points of \( \Delta_n \) converge to \( \v \), then each entry of \( \v \) is a limit of numbers \( \ge 0 \), hence \( \ge 0 \), and the entries of \( \v \) add up to a limit of sums equal to \( 1 \). By the compactness of closed bounded sets, fact (A3) of Chapter 15's introduction, the sequence \( (\v_k) \) has a subsequence \( (\v_{k_j}) \) converging to some \( \v \in \Delta_n \). In particular \( \v \ge \0 \), and \( \v \ne \0 \) because its entries add up to \( 1 \).

**Step 3: the limit.** For every \( j \) we have \( \A_{k_j}\v_{k_j} = \rho_{k_j}\v_{k_j} \). Convergence in the Euclidean norm is entrywise convergence (@cor-entrywise-convergence-is-the-convergence), and \( \A_{k_j} \to \A \) entrywise. Each entry of \( \A_{k_j}\v_{k_j} \) is a sum of products of entries of \( \A_{k_j} \) and of \( \v_{k_j} \), so by the algebra of limits it converges to the corresponding entry of \( \A\v \); likewise \( \rho_{k_j} \to r \) by Step 1, since a subsequence of a convergent sequence has the same limit, and so \( \rho_{k_j}\v_{k_j} \to r\v \). Limits are unique, so \( \A\v = r\v \) with \( \v \ne \0 \); \( r \) is an eigenvalue of \( \A \), hence \( r \le \rho \) by @def-spectral-radius; with \( r \ge \rho \), \( r = \rho \). So \( \A\v = \rho\v \), and \( \v \ge \0 \) is the required eigenvector. This proves the theorem.
:::

Two imported facts were used, both named where they act: (A2) in Step 1 and (A3) in Step 2. No statement about the roots of polynomials is needed.

::: {.remark}
Alternatively, \( \rho_k \to \rho \) also follows from the continuity of eigenvalues proved in Chapter 15 §07, but that rests on a theorem about the roots of polynomials which Chapter 15 quotes without proof; the route above needs nothing of the kind.
:::

The theorem is sharp, in the sense that each of Perron's further conclusions fails for some non-negative matrix. @exm-perron-conclusions-lost shows that \( \rho \) can be \( 0 \), it can be a repeated eigenvalue, the non-negative eigenvector can fail to be positive or unique, and another eigenvalue can have a non-negative eigenvector; and the swap matrix below shows that another eigenvalue can reach \( \lvert \lambda \rvert = \rho \). The positive conclusions of @thm-perron are *strict* statements — an entry is \( > 0 \), a multiplicity is \( 1 \), an inequality \( \lvert \lambda \rvert < \rho \) is strict — and strict inequalities do not survive limits. Positive numbers can tend to \( 0 \); two simple eigenvalues can merge.

::: {.warning}
**A non-negative eigenvector does not identify \( \rho \) for a general non-negative matrix.** In \( \A_1 \) of @exm-perron-conclusions-lost the vector \( \e_3 \ge \0 \) is an eigenvector, but its eigenvalue is \( 1 \), while \( \rho(\A_1) = 2 \). To find \( \rho \) from an eigenvector, you need either irreducibility (next subsection) or a **positive** eigenvector, which Exercise C1 at the end of this section shows is enough.
:::

## The theorem for irreducible matrices

What goes wrong in @exm-perron-conclusions-lost is visible in the zero pattern: \( \A_c \) splits into two blocks that do not talk to each other, and \( \N \) passes mass from one coordinate to the other but never back. Section 2 made "every coordinate eventually talks to every other" precise. A non-negative matrix is **irreducible** (@def-irreducible) when no simultaneous permutation of its rows and columns brings it to block upper triangular form, and by @thm-irreducible-power-positive this happens exactly when \( (\I + \A)^{n-1} > 0 \). That criterion is the bridge we need: it turns an irreducible matrix into a positive one, to which @thm-perron applies.

::: {#thm-perron-frobenius}
[Perron–Frobenius Theorem]

Let \( \A \in M_n(\nR) \) with \( n \ge 1 \) be non-negative and irreducible, and put \( \rho = \rho(\A) \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \rho \) is an eigenvalue of \( \A \) with an eigenvector \( \v > \0 \);
2. \( \rho \) is **algebraically simple**: \( a_{\A}(\rho) = 1 \);
3. every non-negative eigenvector of \( \A \), for **any** eigenvalue, is a positive multiple of \( \v \); in particular its eigenvalue is \( \rho \), and the non-negative eigenvector is unique up to scale;
4. if \( n \ge 2 \), then \( \rho > 0 \).
:::
:::

::: {.idea}
There are two ways to reach a positive matrix, and we take the one that keeps strict information. The perturbation \( \A + \varepsilon\J \) of the last proof needs a limit, and a limit cannot certify strict conclusions; Exercise C2 at the end of this section shows them lost when the limit matrix is reducible. So instead we use \( \B = (\I + \A)^{n-1} \), which is positive by @thm-irreducible-power-positive and needs no limit. Step roadmap:

① @thm-nonnegative-rho-eigenvalue gives \( \A\x = \rho\x \) with \( \x \ge \0 \), \( \x \ne \0 \).

② \( \B\x = (1 + \rho)^{n-1}\x \), and a positive matrix times a non-zero non-negative vector is positive; so \( \x > \0 \).

③ Every eigenvector of \( \A \) is an eigenvector of \( \B = q(\A) \), and the Spectral Mapping Theorem transports multiplicities. So a non-negative eigenvector of \( \A \), or a repeated \( \rho \), would be a non-negative eigenvector of \( \B \), or a repeated \( \rho(\B) \) — both of which @thm-perron controls.

④ If \( \rho = 0 \), then \( \A\x = \0 \) with \( \x > \0 \) forces \( \A = 0 \), which is not irreducible for \( n \ge 2 \).
:::

::: {.proof}
Let \( q(t) = (1 + t)^{n-1} \) and \( \B = q(\A) = (\I + \A)^{n-1} \). Since \( \A \) is irreducible, \( \B > 0 \) by @thm-irreducible-power-positive.

**Step 1: an eigenvector \( \v > \0 \) for \( \rho \).** By @thm-nonnegative-rho-eigenvalue there is \( \x \ge \0 \), \( \x \ne \0 \), with \( \A\x = \rho\x \). Then \( (\I + \A)\x = (1 + \rho)\x \), and applying this \( n - 1 \) times gives \( \B\x = (1 + \rho)^{n-1}\x \). Choose \( j_0 \) with \( x_{j_0} > 0 \), possible because \( \x \ge \0 \) and \( \x \ne \0 \). For every \( i \),
\[
(\B\x)_i = \sum_{j=1}^{n} b_{ij}x_j \ge b_{ij_0}x_{j_0} > 0 ,
\]
since every term is \( \ge 0 \) and \( b_{ij_0} > 0 \). So \( \B\x > \0 \). As \( 1 + \rho \ge 1 \), we may divide: \( \x = (1 + \rho)^{-(n-1)}\B\x > \0 \). Put \( \v = \x \). This proves (a).

**Step 2: eigenvectors of \( \A \) are eigenvectors of \( \B \).** If \( \A\y = \mu\y \) with \( \y \ne \0 \), then, exactly as in Step 1, \( \B\y = q(\mu)\y \). In particular \( \B\v = q(\rho)\v \) with \( \v > \0 \). By @thm-perron (d), a non-negative eigenvector of the positive matrix \( \B \) belongs to the eigenvalue \( \rho(\B) \); hence
\[
q(\rho) = (1 + \rho)^{n-1} = \rho(\B) .
\]

**Step 3: simplicity.** Over \( \nC \), write \( p_{\A}(t) = (t - \lambda_1)\cdots(t - \lambda_n) \) with each eigenvalue repeated according to its algebraic multiplicity (@cor-complex-polynomial-splits). By the Spectral Mapping Theorem (@thm-spectral-mapping),
\[
p_{\B}(t) = \bigl(t - q(\lambda_1)\bigr)\cdots\bigl(t - q(\lambda_n)\bigr) .
\]
Suppose \( a_{\A}(\rho) \ge 2 \), say \( \lambda_1 = \lambda_2 = \rho \). Then \( q(\rho) = \rho(\B) \) occurs at least twice in this factorization (other eigenvalues mapping to \( \rho(\B) \) could only increase this count), so \( a_{\B}(\rho(\B)) \ge 2 \), contradicting the simplicity of \( \rho(\B) \) in @thm-perron. Hence \( a_{\A}(\rho) = 1 \), which is (b).

**Step 4: non-negative eigenvectors.** Let \( \y \ge \0 \), \( \y \ne \0 \), with \( \A\y = \mu\y \) for some \( \mu \in \nC \). By Step 2, \( \y \) is a non-negative eigenvector of \( \B \), so by @thm-perron (d) it belongs to \( \rho(\B) \). So \( \y \) and \( \v \) both lie in the eigenspace \( E_{\rho(\B)}(\B) \). Since \( \rho(\B) \) is algebraically simple, @thm-geometric-le-algebraic gives \( \dim E_{\rho(\B)}(\B) = 1 \), so \( \y = c\v \) for some scalar \( c \ne 0 \). Choosing \( i \) with \( y_i > 0 \) gives \( c = y_i/v_i > 0 \). Finally \( \A\y = c\A\v = \rho\,c\v = \rho\y \), so \( \mu = \rho \). This proves (c).

**Step 5: \( \rho > 0 \) when \( n \ge 2 \).** Suppose \( \rho = 0 \). Then \( \A\v = \0 \), so for each \( i \) the sum \( \sum_j a_{ij}v_j \) of non-negative terms is \( 0 \), which forces \( a_{ij}v_j = 0 \) and hence \( a_{ij} = 0 \) for every \( j \), as \( v_j > 0 \). So \( \A = 0 \) and \( \B = \I_n \). For \( n \ge 2 \) the matrix \( \I_n \) has a zero entry off the diagonal, so it is not positive, contradicting \( \B > 0 \). This proves (d), and the theorem.
:::

The first sentence of the proof is where irreducibility did its work, and irreducibility was used only there. Note also what the theorem does **not** claim. For positive matrices, @thm-perron adds that every other eigenvalue has modulus strictly less than \( \rho \). For irreducible matrices this is false.

::: {.warning}
**Irreducible does not make \( \rho \) strictly dominant.** The swap \( \P = \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix} \) is irreducible, since \( \I + \P = \J \) is positive (@thm-irreducible-power-positive with \( n = 2 \)). Its eigenvalues are \( 1 \) and \( -1 \), with eigenvectors \( (1, 1) \) and \( (1, -1) \). The theorem holds as stated: \( \rho = 1 \) is simple with the positive eigenvector \( (1, 1) \), and \( (1, -1) \) is not non-negative. But \( \lvert -1 \rvert = \rho \). Section 5 identifies the irreducible matrices for which \( \rho \) is strictly dominant.
:::

The case \( n = 1 \) is worth one sentence. A \( 1 \times 1 \) matrix \( (a) \) with \( a \ge 0 \) has \( \rho = a \), simple, with the positive eigenvector \( (1) \), so clauses (a)–(c) hold for it outright; clause (d) must exclude \( n = 1 \), since \( (0) \) has \( \rho = 0 \). For \( n \ge 2 \) the zero matrix is the one thing (d) had to rule out, and irreducibility does.

::: {#exm-perron-frobenius-3x3}
[The theorem on a matrix with zeros]

Let
\[
\A = \begin{pmatrix} 0 & 1 & 0 \\ 2 & 0 & 1 \\ 2 & 1 & 0 \end{pmatrix} .
\]
Show that \( \A \) is irreducible, find \( \rho(\A) \) and a positive eigenvector, and check clause (c) of @thm-perron-frobenius against the other eigenvalue.
:::

::: {.solution}
*Irreducible.* We have \( \I + \A = \begin{psmallmatrix} 1 & 1 & 0 \\ 2 & 1 & 1 \\ 2 & 1 & 1 \end{psmallmatrix} \) and, multiplying out,
\[
(\I + \A)^2 = \begin{pmatrix} 3 & 2 & 1 \\ 6 & 4 & 2 \\ 6 & 4 & 2 \end{pmatrix} > 0 ,
\]
so \( \A \) is irreducible by @thm-irreducible-power-positive with \( n = 3 \). Note that \( \A \) itself has four zero entries and is not positive, so @thm-perron does not apply to it directly.

*The spectrum.* Expanding \( \det(t\I - \A) \) along the first row,
\[
\begin{aligned}
p_{\A}(t) &= t\,(t^2 - 1) + (-2t - 2) \\
&= t^3 - 3t - 2 = (t - 2)(t + 1)^2 .
\end{aligned}
\]
So the eigenvalues are \( 2 \) and \( -1 \), the latter with algebraic multiplicity \( 2 \), and \( \rho(\A) = 2 \), algebraically simple as clause (b) says. A repeated eigenvalue elsewhere in the spectrum is no contradiction: the theorem speaks only about \( \rho \).

*The eigenvector.* \( (\A - 2\I)\x = \0 \) reads \( -2x_1 + x_2 = 0 \), \( 2x_1 - 2x_2 + x_3 = 0 \), \( 2x_1 + x_2 - 2x_3 = 0 \). The first gives \( x_2 = 2x_1 \), the second then \( x_3 = 2x_1 \), and the third is satisfied: \( 2 + 2 - 4 = 0 \). So \( \v = (1, 2, 2) > \0 \) and \( \A\v = (2, 4, 4) = 2\v \).

*The other eigenvalue.* \( \A + \I = \begin{psmallmatrix} 1 & 1 & 0 \\ 2 & 1 & 1 \\ 2 & 1 & 1 \end{psmallmatrix} \) has rank \( 2 \), and its null space is spanned by \( (1, -1, -1) \): the first row gives \( x_2 = -x_1 \), the second \( x_3 = -2x_1 - x_2 = -x_1 \). Every eigenvector for \( -1 \) is a multiple of \( (1, -1, -1) \) and has entries of both signs, as clause (c) predicts.
:::

::: {.check}
For which values of \( c \ge 0 \) is the matrix \( \A_c \) of @exm-perron-conclusions-lost irreducible? Is the answer consistent with what the example found?
:::

::: {.solution}
For none. Whatever \( c \) is, \( \I + \A_c \) is block diagonal with blocks of sizes \( 2 \) and \( 1 \), so every power of it is block diagonal too, and \( (\I + \A_c)^2 \) has zeros in positions \( (1, 3) \), \( (2, 3) \), \( (3, 1) \), \( (3, 2) \). By @thm-irreducible-power-positive, \( \A_c \) is reducible. This is consistent: the example found conclusions of @thm-perron-frobenius failing for \( c = 1 \) and \( c = 2 \), which is possible only for a reducible matrix.
:::

## The left Perron vector

Everything so far concerned the equation \( \A\v = \rho\v \). A non-negative matrix acts on rows as well: in a Markov chain, the row \( \1\tp \) is a left eigenvector of every stochastic matrix (@prp-stochastic-properties (c)). Left eigenvectors of \( \A \) are eigenvectors of \( \A\tp \) (@prp-left-eigenvectors-transpose (a)), and irreducibility passes to the transpose, so the theorem applies to rows at no extra cost.

::: {#cor-left-perron-vector}
[The Left Perron Vector]

Let \( \A \in M_n(\nR) \) be non-negative and irreducible, with \( \rho = \rho(\A) \) and \( \v > \0 \) as in @thm-perron-frobenius. Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \A\tp \) is non-negative and irreducible, and \( \rho(\A\tp) = \rho \);
2. there is \( \w > \0 \) with \( \w\tp\A = \rho\,\w\tp \), and every non-negative left eigenvector of \( \A \) is a positive multiple of \( \w \);
3. \( \w\tp\v > 0 \), so \( \w \) can be scaled to make \( \w\tp\v = 1 \).
:::
:::

::: {.idea}
Apply @thm-perron-frobenius to \( \A\tp \) and read the answer back as rows. Two things must be checked first: that \( \A\tp \) meets the hypotheses, which holds because the test \( (\I + \A)^{n-1} > 0 \) survives transposition, and that \( \A\tp \) has the same spectral radius, which holds because it has the same characteristic polynomial. Positivity of both vectors then makes \( \w\tp\v \) a sum of positive terms.
:::

::: {.proof}
(a) The entries of \( \A\tp \) are those of \( \A \), so \( \A\tp \ge 0 \). Transposition reverses products and fixes \( \I \) (@thm-transpose-properties), so \( (\I + \A\tp)^{n-1} = \bigl((\I + \A)^{n-1}\bigr)\tp \), which is positive because \( (\I + \A)^{n-1} \) is; hence \( \A\tp \) is irreducible by @thm-irreducible-power-positive. By @prp-left-eigenvectors-transpose (b), \( p_{\A\tp} = p_{\A} \), so \( \A \) and \( \A\tp \) have the same eigenvalues and \( \rho(\A\tp) = \rho \).

(b) By (a) and @thm-perron-frobenius (a) applied to \( \A\tp \), there is \( \w > \0 \) with \( \A\tp\w = \rho\w \), which by @prp-left-eigenvectors-transpose (a) says \( \w\tp\A = \rho\w\tp \). A non-negative left eigenvector of \( \A \) is a non-negative eigenvector of \( \A\tp \), hence a positive multiple of \( \w \) by @thm-perron-frobenius (c) applied to \( \A\tp \).

(c) \( \w\tp\v = \sum_i w_iv_i \) is a sum of positive numbers, so it is positive, and \( \w/(\w\tp\v) \) has the stated property.
:::

This makes the following names well defined, since each vector is pinned down by (c) of the theorem or (b) of the corollary together with its normalization.

::: {#def-perron-root-and-vectors}
[Perron Root, Perron Vectors]

This definition extends @def-perron-vector from positive matrices to irreducible ones. Let \( \A \in M_n(\nR) \) be non-negative and irreducible. Its **Perron root** is \( \rho(\A) \). Its **(right) Perron vector** is the unique \( \v > \0 \) with \( \A\v = \rho(\A)\v \) and \( \1\tp\v = 1 \). Its **left Perron vector** is the unique \( \w > \0 \) with \( \w\tp\A = \rho(\A)\w\tp \) and \( \w\tp\v = 1 \).
:::

The two normalizations are chosen for what they do. \( \1\tp\v = 1 \) makes \( \v \) a probability vector, which is what a Markov chain wants; \( \w\tp\v = 1 \) makes the rank-one matrix \( \v\w\tp \) idempotent, since
\[
(\v\w\tp)(\v\w\tp) = \v\,(\w\tp\v)\,\w\tp = \v\w\tp .
\]

Section 5 shows that, for a large class of irreducible matrices, the powers \( (\A/\rho)^k \) converge to exactly this matrix.

A positive matrix is irreducible, since then \( (\I + \A)^{n-1} \ge \I + \A > 0 \) for \( n \ge 2 \): expand \( (\I + \A)^{n-1} \) by the binomial theorem, which applies because \( \I \) and \( \A \) commute, and note that every term is \( \ge 0 \) and two of them are \( \I \) and \( (n - 1)\A \ge \A \). So this definition covers the positive matrices of Section 1. For them the Perron root and both Perron vectors are those of @def-perron-vector.

For the matrix of @exm-perron-frobenius-3x3, the left eigenvector is \( (3, 2, 1) \): indeed \( (3, 2, 1)\A = (0 + 4 + 2,\ 3 + 0 + 1,\ 0 + 2 + 0) = (6, 4, 2) \). The right Perron vector is \( \v = \frac15(1, 2, 2) \), and \( (3, 2, 1) \cdot \frac15(1, 2, 2) = \frac95 \), so the left Perron vector is \( \w = \frac59(3, 2, 1) \).

::: {#exm-irreducible-stochastic-perron}
[An irreducible stochastic matrix]

Let
\[
\A = \begin{pmatrix} 0 & 1/2 & 1 \\ 1 & 0 & 0 \\ 0 & 1/2 & 0 \end{pmatrix} .
\]
Show that \( \A \) is stochastic and irreducible, and find its Perron root and its right and left Perron vectors.
:::

::: {.solution}
Each column is a probability vector, so \( \A \) is stochastic (@def-stochastic-matrix). Multiplying out,
\[
(\I + \A)^2 = \begin{pmatrix} 3/2 & 3/2 & 2 \\ 2 & 3/2 & 1 \\ 1/2 & 1 & 1 \end{pmatrix} > 0 ,
\]
so \( \A \) is irreducible (@thm-irreducible-power-positive).

*Perron root.* By @prp-stochastic-properties (c), \( 1 \) is an eigenvalue. Every column sum is \( 1 \), so \( \norm{\A}_1 = 1 \) and \( \rho(\A) \le 1 \) by @cor-spectral-radius-row-column-bound. Hence \( \rho(\A) = 1 \).

*Left Perron vector.* \( \1\tp\A = \1\tp \) with \( \1 > \0 \), so by @cor-left-perron-vector (b) the left Perron vector is a multiple of \( \1 \).

*Right Perron vector.* \( \A\x = \x \) reads \( \tfrac12x_2 + x_3 = x_1 \), \( x_1 = x_2 \), \( \tfrac12x_2 = x_3 \). With \( x_3 = 1 \) this gives \( x_2 = 2 \), \( x_1 = 2 \), and the first equation holds: \( 1 + 1 = 2 \). So \( \v = \frac15(2, 2, 1) \). Then \( \1\tp\v = 1 \), and the left Perron vector is \( \w = \1 \) itself.

By @thm-perron-frobenius (c), \( \v \) is the **only** probability vector with \( \A\v = \v \): this chain has exactly one steady state, and every state has positive probability in it. The other two eigenvalues are the roots of \( 2t^2 + 2t + 1 \), namely \( \frac{-1 \pm i}{2} \), of modulus \( 1/\sqrt2 < 1 \); the factorization is \( p_{\A}(t) = (t - 1)(t^2 + t + \frac12) \), which the reader can confirm by expanding \( \det(t\I - \A) \) along the first column.
:::

For every irreducible stochastic matrix the same three lines apply, and they show that the left Perron vector is always \( \1 \) and the steady state always unique and positive. Section 6 draws the consequences for Markov chains.

## Exercises

### A. Check your understanding

:::: {#exr-perron-frobenius-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the Perron–Frobenius theorem for irreducible non-negative matrices.
2. True or false: if \( \A \ge 0 \), then \( \rho(\A) > 0 \). Justify your answer.
3. True or false: if \( \A \ge 0 \) is irreducible, then every eigenvalue \( \lambda \ne \rho(\A) \) has \( \lvert \lambda \rvert < \rho(\A) \). Justify your answer.
4. True or false: if \( \A \ge 0 \) and \( \A\y = \mu\y \) with \( \y \ge \0 \), \( \y \ne \0 \), then \( \mu = \rho(\A) \). Justify your answer.
5. Which positive matrix does the proof of @thm-perron-frobenius apply @thm-perron to, and why not to \( \A + \varepsilon\J \)?
:::
::::

::: {.solution}
(a) See @thm-perron-frobenius: for \( \A \ge 0 \) irreducible, \( \rho(\A) \) is an algebraically simple eigenvalue with a positive eigenvector, every non-negative eigenvector is a positive multiple of that one, and \( \rho(\A) > 0 \) when \( n \ge 2 \).

(b) False. \( \N = \begin{psmallmatrix} 0 & 1 \\ 0 & 0 \end{psmallmatrix} \ge 0 \) has \( \rho(\N) = 0 \) (@exm-perron-conclusions-lost). It is reducible, so this does not contradict @thm-perron-frobenius (d).

(c) False. The swap \( \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix} \) is irreducible with eigenvalues \( 1 = \rho \) and \( -1 \), and \( \lvert -1 \rvert = \rho \).

(d) False in general: \( \A_1 \) of @exm-perron-conclusions-lost has \( \A_1\e_3 = \e_3 \) but \( \rho(\A_1) = 2 \). It is true when \( \A \) is irreducible, by @thm-perron-frobenius (c).

(e) To \( \B = (\I + \A)^{n-1} \), which is positive by @thm-irreducible-power-positive. The perturbation \( \A + \varepsilon\J \) requires a limit \( \varepsilon \to 0^{+} \), and a limit cannot certify strict conclusions — positivity of the eigenvector and simplicity of \( \rho \) — which are exactly what the theorem asserts; Exercise C2 shows them lost when the limit matrix is reducible.
:::

### B. Practice

:::: {#exr-perron-frobenius-b1}
[B1: Does the theorem apply?]

For each matrix, determine whether @thm-perron-frobenius applies. Where it does, find \( \rho \) and a positive eigenvector; where it does not, say which hypothesis fails and whether the conclusion fails too. Justify your answers.
\[
\text{(a)}\ \begin{pmatrix} 0 & 2 \\ 8 & 0 \end{pmatrix} \qquad
\text{(b)}\ \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix} \qquad
\text{(c)}\ \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix} \qquad
\text{(d)}\ \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}
\]
::::

::: {.solution}
(a) Non-negative, and \( \I + \A = \begin{psmallmatrix} 1 & 2 \\ 8 & 1 \end{psmallmatrix} > 0 \), so irreducible by @thm-irreducible-power-positive with \( n = 2 \). The theorem applies. \( p_{\A}(t) = t^2 - 16 \), so the eigenvalues are \( \pm 4 \) and \( \rho = 4 \). From \( -4x_1 + 2x_2 = 0 \), \( \v = (1, 2) > \0 \); check: \( \A\v = (4, 8) = 4\v \). As with the swap, \( -4 \) has the same modulus as \( \rho \).

(b) Non-negative, but \( (\I + \A)^1 = \begin{psmallmatrix} 2 & 2 \\ 0 & 4 \end{psmallmatrix} \) has a zero entry, so \( \A \) is reducible and the theorem does not apply. The eigenvalues are \( 1 \) and \( 3 \) (@thm-diagonal-of-triangular-form (b)), so \( \rho = 3 \). Here \( (\A - 3\I)\x = \0 \) reads \( -2x_1 + 2x_2 = 0 \), so \( (1, 1) > \0 \) is an eigenvector for \( \rho \): conclusions (a) and (b) happen to hold. Conclusion (c) fails: \( \e_1 \ge \0 \) is an eigenvector for \( 1 \ne \rho \).

(c) Non-negative. With \( \C \) this matrix, \( \C\e_1 = \e_3 \), \( \C\e_3 = \e_2 \), \( \C\e_2 = \e_1 \), and \( \I + \C + \C^2 = \J \); so \( (\I + \C)^2 = \I + 2\C + \C^2 \ge \I + \C + \C^2 = \J > 0 \), and \( \C \) is irreducible. The theorem applies. \( \C^3 = \I \), and \( p_{\C}(t) = t^3 - 1 \) (expand along the first column), so the eigenvalues are the three cube roots of unity, all of modulus \( 1 \), and \( \rho = 1 \) with \( \v = \1 \), since every row of \( \C \) has a single \( 1 \).

(d) Not non-negative, so the theorem does not apply, and its conclusion fails: \( p(t) = t^2 + 1 \), the eigenvalues are \( \pm i \), and \( \rho = 1 \) is not an eigenvalue at all.
:::

:::: {#exr-perron-frobenius-b2}
[B2: Both Perron vectors]

Let
\[
\A = \begin{pmatrix} 0 & 1 & 0 \\ 2 & 0 & 2 \\ 1 & 0 & 1 \end{pmatrix} .
\]
Show that \( \A \) is irreducible, and find its Perron root, its right Perron vector and its left Perron vector (@def-perron-root-and-vectors). Hence write down the matrix \( \v\w\tp \) and check that it is idempotent.
::::

::: {.solution}
*Irreducible.* \( \I + \A = \begin{psmallmatrix} 1 & 1 & 0 \\ 2 & 1 & 2 \\ 1 & 0 & 2 \end{psmallmatrix} \), and
\[
(\I + \A)^2 = \begin{pmatrix} 3 & 2 & 2 \\ 6 & 3 & 6 \\ 3 & 1 & 4 \end{pmatrix} > 0 ,
\]
so \( \A \) is irreducible by @thm-irreducible-power-positive.

*Perron root.* Expanding \( \det(t\I - \A) \) along the first row,
\[
\begin{aligned}
p_{\A}(t) &= t\bigl(t(t - 1) - 0\bigr) + \bigl(-2(t - 1) - 2\bigr) \\
&= t^3 - t^2 - 2t = t(t - 2)(t + 1) ,
\end{aligned}
\]
so the eigenvalues are \( 2, 0, -1 \) and \( \rho = 2 \).

*Right.* \( (\A - 2\I)\x = \0 \): the first row gives \( x_2 = 2x_1 \), the third \( x_1 - x_3 = 0 \). So \( \x = (1, 2, 1) \); check the second row: \( 2 - 4 + 2 = 0 \). Normalizing, \( \v = \frac14(1, 2, 1) \).

*Left.* \( (\A\tp - 2\I)\y = \0 \), with \( \A\tp = \begin{psmallmatrix} 0 & 2 & 1 \\ 1 & 0 & 0 \\ 0 & 2 & 1 \end{psmallmatrix} \): the second row gives \( y_1 = 2y_2 \), the third \( 2y_2 - y_3 = 0 \). So \( \y = (2, 1, 2) \); check the first row: \( -4 + 2 + 2 = 0 \). Then \( \y\tp\v = \frac14(2 + 2 + 2) = \frac32 \), so \( \w = \frac23(2, 1, 2) \).

*The product.*
\[
\v\w\tp = \frac14 \cdot \frac23 \begin{pmatrix} 2 & 1 & 2 \\ 4 & 2 & 4 \\ 2 & 1 & 2 \end{pmatrix} = \frac16 \begin{pmatrix} 2 & 1 & 2 \\ 4 & 2 & 4 \\ 2 & 1 & 2 \end{pmatrix} .
\]
It is idempotent because \( (\v\w\tp)^2 = \v(\w\tp\v)\w\tp = \v\w\tp \), as \( \w\tp\v = 1 \). Directly: call the displayed integer matrix \( \M \). Row \( i \) of \( \M^2 \) is row \( i \) of \( \M \) times \( \M \); the first row gives \( 2(2, 1, 2) + 1(4, 2, 4) + 2(2, 1, 2) = 6(2, 1, 2) \), and the other rows are multiples of the first, so \( \M^2 = 6\M \). Hence \( \bigl(\frac16\M\bigr)^2 = \frac{1}{36}\cdot 6\M = \frac16\M \).
:::

:::: {#exr-perron-frobenius-b3}
[B3: A reducible matrix, clause by clause]

Let
\[
\A = \begin{pmatrix} 2 & 0 & 0 \\ 1 & 3 & 0 \\ 0 & 1 & 2 \end{pmatrix} .
\]
Show that \( \A \) is reducible. Find \( \rho(\A) \) and every non-negative eigenvector of \( \A \). Hence decide which of the four conclusions of @thm-perron-frobenius hold for \( \A \) and which fail.
::::

::: {.solution}
*Reducible.* \( \I + \A \) is lower triangular, so \( (\I + \A)^2 \) is lower triangular and has zero entries above the diagonal; by @thm-irreducible-power-positive, \( \A \) is reducible.

*Spectrum.* \( \A \) is lower triangular, so its eigenvalues are \( 2, 3, 2 \) (@thm-diagonal-of-triangular-form (b), applied to \( \A\tp \), which has the same characteristic polynomial by @prp-left-eigenvectors-transpose (b)). So \( \rho = 3 \), with \( a_{\A}(3) = 1 \).

*Eigenvectors for 3.* \( (\A - 3\I)\x = \0 \) reads \( -x_1 = 0 \), \( x_1 = 0 \), \( x_2 - x_3 = 0 \); the solutions are the multiples of \( (0, 1, 1) \). *Eigenvectors for 2.* \( (\A - 2\I)\x = \0 \) reads \( x_1 + x_2 = 0 \), \( x_2 = 0 \); the solutions are the multiples of \( (0, 0, 1) \). So the non-negative eigenvectors are the positive multiples of \( (0, 1, 1) \) and of \( \e_3 \).

*Verdict.* Conclusion (b) holds and (d) holds (\( \rho = 3 > 0 \)). Conclusion (a) fails in its strong form: \( \rho \) is an eigenvalue, as @thm-nonnegative-rho-eigenvalue guarantees, but no eigenvector for it is positive. Conclusion (c) fails: \( \e_3 \ge \0 \) is an eigenvector for \( 2 \ne \rho \).
:::

### C. Going deeper

:::: {#exr-perron-frobenius-c1}
[C1: A positive eigenvector always belongs to the spectral radius]

Let \( \A \in M_n(\nR) \) with \( \A \ge 0 \), **not** assumed irreducible.

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( \A\x = \mu\x \) with \( \x > \0 \), then \( \mu = \rho(\A) \).
2. Deduce that if every row of \( \A \) has the same sum \( s \), then \( \rho(\A) = s \).
3. Show by an example that (a) fails if \( \x > \0 \) is weakened to \( \x \ge \0 \), \( \x \ne \0 \).
:::

*Hint: apply @thm-nonnegative-rho-eigenvalue to \( \A\tp \).*
::::

::: {.solution}
(a) Since \( \A \) and \( \x \) are real and \( \x \ne \0 \), \( \mu = (\A\x)_i/x_i \) for any \( i \) is real, and it is \( \ge 0 \) because \( (\A\x)_i \ge 0 \) and \( x_i > 0 \). By @prp-left-eigenvectors-transpose (b), \( \rho(\A\tp) = \rho(\A) = \rho \), and \( \A\tp \ge 0 \), so @thm-nonnegative-rho-eigenvalue gives \( \y \ge \0 \), \( \y \ne \0 \), with \( \A\tp\y = \rho\y \), that is, \( \y\tp\A = \rho\y\tp \). Compute \( \y\tp\A\x \) two ways:
\[
\rho\,\y\tp\x = (\y\tp\A)\x = \y\tp(\A\x) = \mu\,\y\tp\x .
\]
Now \( \y\tp\x = \sum_i y_ix_i > 0 \), as every term is \( \ge 0 \) and the terms with \( y_i > 0 \) are positive. Dividing, \( \mu = \rho \).

(b) Equal row sums \( s \) say \( \A\1 = s\1 \), and \( \1 > \0 \), so \( s = \rho(\A) \) by (a).

(c) \( \A_1 \) of @exm-perron-conclusions-lost has \( \A_1\e_3 = \e_3 \) with \( \e_3 \ge \0 \), \( \e_3 \ne \0 \), but \( \rho(\A_1) = 2 \ne 1 \).
:::

:::: {#exr-perron-frobenius-c2}
[C2: What the limit loses]

This exercise shows why the proof of @thm-perron-frobenius does not take the limit \( \A + \varepsilon\J \to \A \).

::: {.enumerate options="label=(\alph*)"}
1. For \( \varepsilon > 0 \), find the eigenvalues of \( \I_2 + \varepsilon\J \). Show that \( \rho \) is simple for every \( \varepsilon > 0 \), but not at \( \varepsilon = 0 \).
2. For \( \varepsilon > 0 \), let \( \N_{\varepsilon} = \begin{psmallmatrix} \varepsilon & 1 + \varepsilon \\ \varepsilon & \varepsilon \end{psmallmatrix} \), which is \( \N + \varepsilon\J \) for the nilpotent \( \N \) of @exm-perron-conclusions-lost. Show that \( \rho(\N_{\varepsilon}) = \varepsilon + \sqrt{\varepsilon(1 + \varepsilon)} \) with eigenvector \( \bigl(\sqrt{1 + \varepsilon},\ \sqrt{\varepsilon}\bigr) > \0 \), and find the limit of this eigenvector as \( \varepsilon \to 0^{+} \).
3. Which conclusions of @thm-perron survive the limit in these two examples, and which do not? Explain in one sentence why this is to be expected.
:::
::::

::: {.solution}
(a) \( \J\1 = 2\cdot\1 \) and \( \J(1, -1) = \0 \), so \( \I_2 + \varepsilon\J \) has the eigenvalue \( 1 + 2\varepsilon \) on \( (1, 1) \) and \( 1 \) on \( (1, -1) \). For \( \varepsilon > 0 \) these are distinct, so \( \rho = 1 + 2\varepsilon \) is simple. At \( \varepsilon = 0 \) the matrix is \( \I_2 \) and \( \rho = 1 \) has algebraic multiplicity \( 2 \).

(b) \( \N_{\varepsilon} - \varepsilon\I = \begin{psmallmatrix} 0 & 1 + \varepsilon \\ \varepsilon & 0 \end{psmallmatrix} \) has characteristic polynomial \( t^2 - \varepsilon(1 + \varepsilon) \), so the eigenvalues of \( \N_{\varepsilon} \) are \( \varepsilon \pm \sqrt{\varepsilon(1 + \varepsilon)} \), and \( \rho(\N_{\varepsilon}) = \varepsilon + \sqrt{\varepsilon(1 + \varepsilon)} \), which exceeds the modulus of the other one since \( \varepsilon > 0 \). With \( s = \sqrt{\varepsilon(1 + \varepsilon)} \) and \( \u = \bigl(\sqrt{1 + \varepsilon}, \sqrt\varepsilon\bigr) \),
\[
(\N_{\varepsilon} - \varepsilon\I)\u = \bigl((1 + \varepsilon)\sqrt\varepsilon,\ \varepsilon\sqrt{1 + \varepsilon}\bigr) = s\,\u ,
\]
since \( (1 + \varepsilon)\sqrt\varepsilon = s\sqrt{1 + \varepsilon} \) and \( \varepsilon\sqrt{1 + \varepsilon} = s\sqrt\varepsilon \). So \( \N_{\varepsilon}\u = (\varepsilon + s)\u \) with \( \u > \0 \). As \( \varepsilon \to 0^{+} \), \( \u \to (1, 0) = \e_1 \), which is non-negative but not positive.

(c) What survives is that \( \rho \) is an eigenvalue with a non-negative eigenvector, which is @thm-nonnegative-rho-eigenvalue. Simplicity is lost in (a), and positivity of the eigenvector in (b). This is expected because those conclusions are strict — a multiplicity equal to \( 1 \), entries \( > 0 \) — and a limit of positive numbers need only be \( \ge 0 \), while two distinct eigenvalues can converge to one.
:::

:::: {#exr-perron-frobenius-c3}
[C3: Uniqueness through the left Perron vector]

Let \( \A \ge 0 \) be irreducible, with left Perron vector \( \w \) (@def-perron-root-and-vectors, @cor-left-perron-vector).

::: {.enumerate options="label=(\alph*)"}
1. Using @thm-left-right-biorthogonal, give a second proof that if \( \A\y = \mu\y \) with \( \y \ge \0 \), \( \y \ne \0 \), then \( \mu = \rho(\A) \).
2. Deduce that an irreducible stochastic matrix has exactly one steady state (@def-markov-chain), and that it is positive.
:::
::::

::: {.solution}
(a) Suppose \( \mu \ne \rho(\A) \). The vector \( \w \) is a left eigenvector for \( \rho(\A) \) and \( \y \) a right eigenvector for \( \mu \), so @thm-left-right-biorthogonal gives \( \w\tp\y = 0 \). But \( \w > \0 \), \( \y \ge \0 \) and \( \y \ne \0 \), so \( \w\tp\y = \sum_i w_iy_i \ge w_iy_i > 0 \) for an index \( i \) with \( y_i > 0 \). This contradiction shows \( \mu = \rho(\A) \).

(b) Let \( \A \) be stochastic and irreducible. As in @exm-irreducible-stochastic-perron, \( \rho(\A) = 1 \): \( 1 \) is an eigenvalue by @prp-stochastic-properties (c), and \( \rho(\A) \le \norm{\A}_1 = 1 \) by @cor-spectral-radius-row-column-bound. A steady state is a probability vector \( \x \) with \( \A\x = \x \): a non-negative eigenvector for \( 1 = \rho(\A) \), normalized by \( \1\tp\x = 1 \). By @thm-perron-frobenius (c), every such \( \x \) is a positive multiple of the Perron vector \( \v \), and the normalization forces \( \x = \v \). So there is exactly one steady state, namely \( \v > \0 \).
:::
