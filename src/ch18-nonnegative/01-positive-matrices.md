# Positive Matrices and Perron's Theorem

Chapter 8 §11 found the long-run behavior of a Markov chain by diagonalizing its transition matrix, and warned that nothing guaranteed the method would work. Chapter 15 §04 gave every square matrix a spectral radius, the largest modulus of an eigenvalue, but said nothing about whether that modulus is itself an eigenvalue. For a general matrix it need not be: the swap \( \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix} \) has spectral radius \( 1 \) and the eigenvalue \( -1 \) sitting on the circle beside it, and the rotation by a right angle has no real eigenvalue at all. This section shows that a single hypothesis on the **entries** removes every one of these difficulties: if every entry of \( \A \) is positive, then \( \rho(\A) \) is an eigenvalue, it is simple, it strictly dominates every other eigenvalue in modulus, and it has an eigenvector with positive entries. That is Perron's theorem, and the rest of the chapter extends it.

**Throughout, matrices and vectors have real entries**, except where complex eigenvectors appear. The eigenvalues of a real matrix are those of the same matrix read in \( M_n(\nC) \), exactly as in Chapter 15 §04, so that \( \rho(\A) \) is defined (@def-spectral-radius) and eigenvectors may have complex entries.

## The entrywise order

Chapter 17 §05 wrote \( \x \ge \0 \) for a real vector with every entry \( \ge 0 \). The same comparison, made one entry at a time, makes sense for matrices of any shape, and it is the only order this chapter uses. Its hook is a recurring expression: every probability argument of Chapter 8 §11 began "the entries are non-negative, so each entry of the product is a sum of non-negative terms". We name the hypothesis once and prove its consequences once.

*The entrywise order compares two matrices of the same shape position by position.*

::: {#def-entrywise-order}
[Entrywise Order; Non-negative and Positive Matrices]

Let \( \A = (a_{ij}) \) and \( \B = (b_{ij}) \) be real \( m \times n \) matrices.

::: {.enumerate options="label=(\alph*)"}
1. \( \A \ge \B \) means \( a_{ij} \ge b_{ij} \) for **every** \( i, j \), and \( \A > \B \) means \( a_{ij} > b_{ij} \) for **every** \( i, j \). We write \( \B \le \A \) and \( \B < \A \) for the same statements.
2. \( \A \) is **non-negative** if \( \A \ge 0 \), and **positive** if \( \A > 0 \), where \( 0 \) is the zero matrix of the same shape.
3. For a complex \( m \times n \) matrix \( \M = (m_{ij}) \), the **entrywise absolute value** is the real matrix \( \lvert\M\rvert \coloneqq (\lvert m_{ij}\rvert) \).
:::

Vectors are the case \( n = 1 \), so \( \x \ge \0 \), \( \x > \0 \) and \( \lvert\x\rvert = (\lvert x_1\rvert, \dots, \lvert x_n\rvert) \) have the same meaning as in Chapter 17 §05.
:::

In words: (a) compares every pair of corresponding entries, and asks for a strict inequality in **every** position in the strict version. So \( \A > \B \) is much stronger than "\( \A \ge \B \) and \( \A \ne \B \)", and the two must not be confused. Clause (b) is the special case \( \B = 0 \). Clause (c) takes the modulus of each entry separately; it has nothing to do with the absolute value \( (\A^{*}\A)^{1/2} \) of Chapter 12, and in this chapter \( \lvert\M\rvert \) always means the entrywise one.

Some examples, simplest first.

- \( \begin{pmatrix} 1 & 2 \\ 3 & 2 \end{pmatrix} > 0 \): every entry is positive. This is the matrix of @exm-eigenvalues-2x2.
- \( \I_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \ge 0 \), but \( \I_2 \) is **not** positive, since its off-diagonal entries are \( 0 \). Every stochastic matrix (@def-stochastic-matrix) is non-negative, and so is every permutation matrix.
- **The degenerate cases.** The zero matrix is non-negative and not positive. A \( 1 \times 1 \) matrix \( (a) \) is positive exactly when \( a > 0 \), and then everything this section proves reduces to the statement that \( a \) is an eigenvalue of \( (a) \) with eigenvector \( (1) \). It is worth keeping in mind that every theorem below must survive \( n = 1 \).
- For \( \M = \begin{pmatrix} 3 & -4i \\ 0 & -1 \end{pmatrix} \), \( \lvert\M\rvert = \begin{pmatrix} 3 & 4 \\ 0 & 1 \end{pmatrix} \).

**Non-example by minimal change.** Take the positive matrix \( \begin{pmatrix} 1 & 2 \\ 3 & 2 \end{pmatrix} \) and change its \( (1,2) \) entry to \( 0 \). The result \( \begin{pmatrix} 1 & 0 \\ 3 & 2 \end{pmatrix} \) is still non-negative and still \( \ge \I_2 \), but it is not positive: the clause "**every** entry \( > 0 \)" fails in one position. That one zero is enough to lose a conclusion of this section. The new matrix is triangular, with eigenvalues \( 1 \) and \( 2 \). Its eigenvectors for \( 2 \) are the multiples of \( \e_2 \), and those for \( 1 \) the multiples of \( (1, -3) \). So the dominant eigenvalue \( 2 \) has a non-negative eigenvector, but **no** positive one. Perron's theorem below says this cannot happen for a positive matrix.

::: {.warning}
**Positive is not positive definite, and positive definite is not positive.** The two words sound alike and measure different things. The entrywise order looks at entries; positive definiteness (@def-positive-semidefinite) looks at the quadratic form. The matrix \( \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix} \) is positive, and symmetric, but its eigenvalues are \( 3 \) and \( -1 \), so it is not positive definite: \( \x = (1, -1) \) gives \( \x\tp\A\x = -2 \). The matrix \( \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix} \) is positive definite, with eigenvalues \( 1 \) and \( 3 \), but it has negative entries, so it is not even non-negative. In this book \( \A \ge 0 \) and \( \A > 0 \) always mean the entrywise order, and the Loewner order is always written \( \A \succeq 0 \), \( \A \succ 0 \).
:::

**Why this definition.** The order is entrywise because the only operations the theory needs are sums and products of entries, and a sum or product of non-negative numbers is non-negative. The hypothesis is not coordinate-free: a change of basis destroys it at once. That is also why this chapter, unlike most of the book, cares about the **standard** basis: the hypothesis \( \A \ge 0 \) is a statement about the matrix, not about the operator \( T_{\A} \). The only changes of basis that preserve it are the ones that rearrange coordinates and rescale them by positive numbers, and §02 uses the first kind throughout.

The first facts are the ones used in every argument below. They are the three rules of arithmetic with non-negative numbers, carried to matrices.

::: {#lem-entrywise-order-rules}
[Rules of the Entrywise Order]

Let \( \A, \B \in M_{m \times n}(\nR) \), \( \C, \D \in M_{n \times p}(\nR) \) and \( \x, \y \in \nR^n \).

::: {.enumerate options="label=(\alph*)"}
1. If \( 0 \le \A \le \B \) and \( \0 \le \x \le \y \), then \( \0 \le \A\x \le \B\y \).
2. If \( \A > 0 \), \( \x \ge \0 \) and \( \x \ne \0 \), then \( \A\x > \0 \).
3. If \( 0 \le \A \le \B \) and \( 0 \le \C \le \D \), then \( 0 \le \A\C \le \B\D \). In particular, for square \( 0 \le \A \le \B \), \( 0 \le \A^{k} \le \B^{k} \) for every \( k \ge 0 \).
:::
:::

::: {.idea}
Each entry of a product is a sum of products of entries, so every rule comes down to the arithmetic of non-negative numbers. For the comparison in (a), write \( \B\y - \A\x \) as a sum of two products of non-negative factors; for (b), one positive term in a sum of non-negative terms is enough; and (c) is (a) applied one column at a time.
:::

::: {.proof}
(a) Each entry \( (\A\x)_i = \sum_j a_{ij}x_j \) is a sum of products of non-negative numbers, so \( \A\x \ge \0 \). Next, \( \B\y - \A\x = \B(\y - \x) + (\B - \A)\x \), and both terms are non-negative by what was just shown, because \( \B \ge 0 \), \( \y - \x \ge \0 \), \( \B - \A \ge 0 \) and \( \x \ge \0 \).

(b) Since \( \x \ne \0 \) and \( \x \ge \0 \), some entry \( x_k \) is positive. For every \( i \), \( (\A\x)_i = \sum_j a_{ij}x_j \ge a_{ik}x_k > 0 \), because the other terms are \( \ge 0 \) and \( a_{ik} > 0 \).

(c) By @thm-three-views-of-product, column \( l \) of \( \A\C \) is \( \A\c_l \), where \( \c_l \) is column \( l \) of \( \C \), and likewise for \( \B\D \). Since \( \0 \le \c_l \le \d_l \), part (a) gives \( \0 \le \A\c_l \le \B\d_l \) for every \( l \). The statement about powers follows by induction on \( k \): \( \A^{0} = \B^{0} = \I \), and \( \A^{k+1} = \A^{k}\A \le \B^{k}\B = \B^{k+1} \) by the case just proved.
:::

The absolute value interacts with products through the triangle inequality, which is the second tool.

::: {#lem-entrywise-absolute-value}
[Absolute Value of a Product]

Let \( \A \in M_{m \times n}(\nC) \), \( \B \in M_{n \times p}(\nC) \) and \( \x \in \nC^n \). Then

::: {.enumerate options="label=(\alph*)"}
1. \( \lvert\A\x\rvert \le \lvert\A\rvert\,\lvert\x\rvert \);
2. \( \lvert\A\B\rvert \le \lvert\A\rvert\,\lvert\B\rvert \);
3. if \( m = n \), then \( \lvert\A^{k}\rvert \le \lvert\A\rvert^{k} \) for every \( k \ge 0 \).
:::
:::

::: {.idea}
Each entry of \( \A\x \) is a sum of products, and the triangle inequality bounds its modulus by the sum of the moduli of the products: that is (a). Then (b) is (a) one column at a time, and (c) follows from (b) by induction on \( k \), with the order rules to replace \( \lvert\A^{k}\rvert \) by the larger \( \lvert\A\rvert^{k} \).
:::

::: {.proof}
(a) For each \( i \), the triangle inequality (@thm-complex-triangle-inequality, extended to finitely many terms by induction) and the multiplicativity of the modulus (@thm-conjugate-properties (d)) give
\[
\lvert(\A\x)_i\rvert = \Bigl\lvert\sum_{j} a_{ij}x_j\Bigr\rvert \le \sum_{j}\lvert a_{ij}\rvert\,\lvert x_j\rvert = \bigl(\lvert\A\rvert\,\lvert\x\rvert\bigr)_i .
\]

(b) Apply (a) to each column of \( \B \), using @thm-three-views-of-product as in the previous proof.

(c) Induction on \( k \). For \( k = 0 \), \( \lvert\I\rvert = \I \). If \( \lvert\A^{k}\rvert \le \lvert\A\rvert^{k} \), then by (b) and @lem-entrywise-order-rules (c),
\[
\lvert\A^{k+1}\rvert = \lvert\A^{k}\A\rvert \le \lvert\A^{k}\rvert\,\lvert\A\rvert \le \lvert\A\rvert^{k}\lvert\A\rvert = \lvert\A\rvert^{k+1} .
\]
This proves the lemma.
:::

For a non-negative \( \A \) we have \( \lvert\A\rvert = \A \), and (a) reads \( \lvert\A\x\rvert \le \A\lvert\x\rvert \). That is the form used below: whatever cancellation happens inside \( \A\x \) can only make it smaller.

The proof of Perron's theorem also needs to know when the triangle inequality is an equality, a case Chapter 0 did not record. The answer is the expected one: when all the terms point in the same direction.

::: {#lem-triangle-equality-complex}
[Equality in the Triangle Inequality]

Let \( z_1, \dots, z_m \in \nC \), put \( s = z_1 + \dots + z_m \), and suppose \( \lvert s\rvert = \lvert z_1\rvert + \dots + \lvert z_m\rvert \) and \( s \ne 0 \). Then \( z_j = \lvert z_j\rvert\,c \) for every \( j \), where \( c = s/\lvert s\rvert \) has \( \lvert c\rvert = 1 \).
:::

::: {.idea}
Rotate the sum onto the positive real axis: multiplying by \( d = \conj{s}/\lvert s\rvert \) turns \( s \) into the real number \( \lvert s\rvert \). Then \( \lvert s\rvert \) is the real part of \( \sum_j dz_j \), which is at most \( \sum_j\lvert z_j\rvert \) term by term. Equality of the totals forces equality in every term, and a complex number whose real part equals its modulus is a real number \( \ge 0 \).
:::

::: {.proof}
Recall from the proof of @thm-complex-triangle-inequality that \( \operatorname{Re}u = x \le \lvert x\rvert \le \sqrt{x^2 + y^2} = \lvert u\rvert \) for \( u = x + yi \). Equality \( \operatorname{Re}u = \lvert u\rvert \) forces equality in both steps, that is \( y^2 = 0 \) and \( x = \lvert x\rvert \), so \( u \) is a real number \( \ge 0 \) and \( u = \lvert u\rvert \).

Put \( d = \conj{s}/\lvert s\rvert \). Then \( \lvert d\rvert = 1 \) and \( ds = \lvert s\rvert^2/\lvert s\rvert = \lvert s\rvert \) by @thm-conjugate-properties (c), (d). Hence
\[
\sum_j\lvert z_j\rvert = \lvert s\rvert = ds = \operatorname{Re}\sum_j dz_j = \sum_j\operatorname{Re}(dz_j) \le \sum_j\lvert dz_j\rvert = \sum_j\lvert z_j\rvert .
\]
So the inequality in the middle is an equality. It is a sum of the inequalities \( \operatorname{Re}(dz_j) \le \lvert dz_j\rvert \), so each of them is an equality, and by the first paragraph \( dz_j = \lvert dz_j\rvert = \lvert z_j\rvert \). Multiplying by \( c = s/\lvert s\rvert \), which satisfies \( cd = s\conj{s}/\lvert s\rvert^2 = 1 \), gives \( z_j = \lvert z_j\rvert\,c \).
:::

## The spectral radius is monotone

A first payoff joins the entrywise order to Chapter 15. Enlarging the entries of a non-negative matrix should not shrink its eigenvalues, and for the spectral radius this is true.

::: {#prp-spectral-radius-monotone}
[Monotonicity of the Spectral Radius]

::: {.enumerate options="label=(\alph*)"}
1. If \( \A, \B \in M_n(\nR) \) and \( 0 \le \A \le \B \), then \( \rho(\A) \le \rho(\B) \).
2. More generally, if \( \A \in M_n(\nC) \), \( \B \in M_n(\nR) \) and \( \lvert\A\rvert \le \B \), then \( \rho(\A) \le \rho(\lvert\A\rvert) \le \rho(\B) \).
:::
:::

::: {.idea}
Eigenvalues do not see the entries directly, but Gelfand's formula (@thm-gelfand) expresses \( \rho \) through the norms of the powers, and the largest absolute row sum \( \norm{\cdot}_{\infty} \) is a norm that does see the entries, monotonically. So compare the powers entrywise, take norms, take \( k \)-th roots and pass to the limit.
:::

::: {.proof}
(b) First, \( \lvert\A^{k}\rvert \le \lvert\A\rvert^{k} \le \B^{k} \) for every \( k \ge 1 \): the first inequality is @lem-entrywise-absolute-value (c), and the second is @lem-entrywise-order-rules (c) applied to \( 0 \le \lvert\A\rvert \le \B \). By @thm-operator-norm-formulas (b), \( \norm{\M}_{\infty} \) is the largest absolute row sum of \( \M \), so it depends only on \( \lvert\M\rvert \) and does not decrease when the entries of \( \lvert\M\rvert \) increase. Hence
\[
\norm{\A^{k}}_{\infty} \le \norm{\lvert\A\rvert^{k}}_{\infty} \le \norm{\B^{k}}_{\infty} \qquad (k \ge 1) .
\]
The \( k \)-th root is increasing on the non-negative reals, so the same inequalities hold between the \( k \)-th roots. The operator norm \( \norm{\cdot}_{\infty} \) is a matrix norm (@thm-operator-norm-properties (d)), so by @thm-gelfand the three sequences of \( k \)-th roots converge to \( \rho(\A) \), \( \rho(\lvert\A\rvert) \) and \( \rho(\B) \). A non-strict inequality survives a limit, which gives \( \rho(\A) \le \rho(\lvert\A\rvert) \le \rho(\B) \).

(a) If \( 0 \le \A \le \B \), then \( \lvert\A\rvert = \A \), and (b) gives \( \rho(\A) \le \rho(\B) \).
:::

The inequality need not be strict, even when \( \A \ne \B \): \( \diag(1, 0) \le \I_2 \) and both have spectral radius \( 1 \). For positive matrices it is strict, which is Exercise C3. The hypothesis \( 0 \le \A \) cannot be dropped from (a): \( \diag(-3, 0) \le 0 \) entrywise, yet \( \rho(\diag(-3, 0)) = 3 > 0 = \rho(0) \).

::: {#exm-spectral-radius-monotone}
[Enlarging one entry]

Let \( \A = \begin{pmatrix} 1 & 2 \\ 1 & 0 \end{pmatrix} \) and \( \B = \begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix} \). Compute both spectral radii and compare with @prp-spectral-radius-monotone.
:::

::: {.solution}
\( 0 \le \A \le \B \), with a difference only in the \( (2,2) \) entry. By the \( 2 \times 2 \) formula \( p(x) = x^2 - (\tr)x + \det \), \( p_{\A}(x) = x^2 - x - 2 = (x - 2)(x + 1) \), so \( \rho(\A) = 2 \), and \( p_{\B}(x) = x^2 - 2x - 1 \), with roots \( 1 \pm \sqrt2 \), so \( \rho(\B) = 1 + \sqrt2 \approx 2.414 \). Indeed \( \rho(\A) \le \rho(\B) \). In both cases the eigenvalue of largest modulus is positive, which Perron's theorem below (@thm-perron) guarantees for the positive \( \B \).
:::

## Perron's theorem

Here is the theorem this section is built around.

::: {#thm-perron}
[Perron's Theorem]

Let \( n \ge 1 \) and let \( \A \in M_n(\nR) \) be **positive**, \( \A > 0 \). Write \( r = \rho(\A) \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( r > 0 \), and \( r \) is an eigenvalue of \( \A \) with an eigenvector \( \v > \0 \);
2. \( r \) is **algebraically simple**: \( a_{\A}(r) = 1 \). In particular \( E_r(\A) = \Span(\v) \);
3. every eigenvalue \( \lambda \in \nC \) of \( \A \) with \( \lambda \ne r \) satisfies \( \lvert\lambda\rvert < r \);
4. every non-negative eigenvector of \( \A \) is a positive multiple of \( \v \). In particular, no eigenvector of \( \A \) for an eigenvalue other than \( r \) is non-negative;
5. \( \A\tp \) is positive with \( \rho(\A\tp) = r \), so (a)–(d) hold for \( \A\tp \): there is \( \w > \0 \) with \( \w\tp\A = r\w\tp \).
:::
:::

**The route.** There are several proofs of Perron's theorem. We take the one that finds \( r \) as the answer to an optimization problem: **how large can \( t \) be if \( \A\x \ge t\x \) for some probability vector \( \x \)?** Its advantage is that it produces the positive eigenvector and the eigenvalue together, and that compactness is used exactly once. The quotient form of this question, maximizing \( \min_i (\A\x)_i/x_i \) over \( \x \in \Delta_n \), is the Collatz–Wielandt formula, which §04 develops for all irreducible matrices.

The quotient itself is awkward on the boundary of the simplex. Where some \( x_i = 0 \), the \( i \)-th ratio is undefined, and the natural repair, taking the minimum over the indices with \( x_i > 0 \) only, gives a function that need not be continuous. For \( \D = \diag(2, 1) \) that function takes the value \( 2 \) at the corner \( \e_1 \), where only the first ratio counts, but the value \( \min(2, 1) = 1 \) at every point \( (1 - t, t) \) with \( 0 < t < 1 \). So the extreme value theorem cannot be applied to it as it stands. (For positive \( \A \) the repaired function is in fact continuous, but proving that costs more than the route below; for the non-negative matrices of §04 it can genuinely fail.) We avoid the quotient: instead of maximizing a function on \( \Delta_n \), we maximize the coordinate \( t \) over the set of pairs \( (\x, t) \) with \( \A\x \ge t\x \), which is closed, and on which \( t \) is continuous.

::: {.idea}
**Step roadmap.** ① The set \( S = \{(\x, t) : \x \in \Delta_n,\ t \ge 0,\ \A\x \ge t\x\} \) is compact, so \( t \) attains a maximum \( r \) on it: facts (A3) and (A4) of Chapter 15's introduction. ② **Push-up claim:** if \( \u \ge \0 \), \( \u \ne \0 \) and \( \A\u \ge r\u \), then \( \A\u = r\u \) and \( \u > \0 \). Otherwise one more application of the positive matrix \( \A \) turns the slack \( \A\u - r\u \) into a **strict** inequality, and a strict inequality leaves room to increase \( r \), contradicting maximality. The maximizer therefore gives the positive eigenvector. ③ For any eigenvalue \( \lambda \) with eigenvector \( \x \), \( \lvert\lambda\rvert\lvert\x\rvert \le \A\lvert\x\rvert \), so \( \lvert\lambda\rvert \le r \) by maximality; hence \( r = \rho(\A) \). ④ If \( \lvert\lambda\rvert = r \), the push-up claim forces equality in the triangle inequality, which aligns all entries of \( \x \) and gives \( \lambda = r \). ⑤ Subtract a multiple of \( \v \) until an entry vanishes: the push-up claim leaves nothing, so \( E_r(\A) \) is a line. ⑥ Steps ①–⑤ for \( \A\tp \) give a positive \( \w \) with \( \A\tp\w = \rho(\A\tp)\w \), and pairing with \( \v \) shows \( \rho(\A\tp) = r \). A second vector in the generalized eigenspace would give \( (\A - r\I)\y = \v \), and pairing with \( \w \) yields \( 0 = \w\tp\v > 0 \). ⑦ A non-negative eigenvector for \( \lambda \ne r \) would be orthogonal to \( \w > \0 \), which is impossible.
:::

Here is the proof, following the roadmap.

::: {.proof}
Let \( \A > 0 \) be \( n \times n \). By @def-standard-simplex, \( \Delta_n \) is the set of probability vectors in \( \nR^n \). Define
\[
S = \bigl\{(\x, t) \in \nR^n \times \nR : \x \in \Delta_n,\ t \ge 0,\ \A\x \ge t\x\bigr\} .
\]

**Step 1: a maximal \( t \).** \( S \) is non-empty: it contains \( (\x, 0) \) for every \( \x \in \Delta_n \), by @lem-entrywise-order-rules (a).

\( S \) is bounded for the Euclidean norm on \( \nR^{n+1} \), the norm with which (A3) is stated. Let \( M \) be the largest entry of \( \A \). If \( (\x, t) \in S \), then \( 0 \le x_i \le 1 \) for every \( i \), and since the \( n \) entries of \( \x \) add up to \( 1 \), some \( x_k \ge 1/n \). Then
\[
\frac{t}{n} \le t\,x_k \le (\A\x)_k = \sum_j a_{kj}x_j \le M\sum_j x_j = M ,
\]
so \( 0 \le t \le nM \). Hence \( \norm{(\x, t)}_2^2 = \sum_i x_i^2 + t^2 \le n + (nM)^2 \), and \( \norm{(\x, t)}_2 \le \sqrt n + nM \).

\( S \) is closed in \( \nR^{n+1} \) (@def-closed-set). Let \( (\x_k, t_k) \in S \) converge to \( (\x, t) \) in the Euclidean norm. Then each coordinate converges, since \( \lvert u_i\rvert \le \norm{\u}_2 \) for every \( \u \in \nR^{n+1} \). Every condition defining \( S \) is a finite list of non-strict inequalities and one equation between expressions built from the entries by sums and products: \( x_i \ge 0 \), \( \sum_i x_i = 1 \), \( t \ge 0 \), and \( (\A\x)_i - t\,x_i \ge 0 \). Each holds for every \( (\x_k, t_k) \), and by the algebra of limits of Chapter 15's introduction each survives the limit. So \( (\x, t) \in S \).

By fact (A3) of Chapter 15's introduction, the closed bounded set \( S \subseteq \nR^{n+1} \) is compact, and the function \( (\x, t) \mapsto t \) is continuous on it. By fact (A4), the extreme value theorem, it attains a maximum: there are \( \z \in \Delta_n \) and a largest number \( r \) such that
\[
\A\z \ge r\z, \qquad\text{and } t \le r \text{ for every } (\x, t) \in S .
\]
Moreover \( r > 0 \). Indeed, let \( s \) be the smallest row sum of \( \A \), which is positive as \( \A > 0 \). The vector \( \x = \frac1n\1 \in \Delta_n \) satisfies \( (\A\x)_i = \frac1n\sum_j a_{ij} \ge \frac{s}{n} = s\,x_i \), so \( (\frac1n\1, s) \in S \) and \( r \ge s > 0 \).

**Step 2: the push-up claim.**

::: {.claim}
If \( \u \in \nR^n \), \( \u \ge \0 \), \( \u \ne \0 \) and \( \A\u \ge r\u \), then \( \A\u = r\u \) and \( \u > \0 \).

::: {.proof}
Suppose \( \A\u \ne r\u \). Then \( \y = \A\u - r\u \) satisfies \( \y \ge \0 \) and \( \y \ne \0 \), so \( \A\y > \0 \) by @lem-entrywise-order-rules (b). Put \( \q = \A\u \); by the same rule \( \q > \0 \), and
\[
\A\q - r\q = \A(\A\u - r\u) = \A\y > \0 .
\]
Every \( q_i > 0 \), so \( \varepsilon = \min_i (\A\y)_i/q_i \) is defined and positive, and \( (\A\q)_i - r\,q_i = (\A\y)_i \ge \varepsilon q_i \) for every \( i \), that is, \( \A\q \ge (r + \varepsilon)\q \). Let \( \sigma = q_1 + \dots + q_n > 0 \) and \( \x = \q/\sigma \). Then \( \x \in \Delta_n \), and dividing by \( \sigma > 0 \) preserves the inequality, so \( \A\x \ge (r + \varepsilon)\x \). Hence \( (\x, r + \varepsilon) \in S \), which contradicts the maximality of \( r \). Therefore \( \A\u = r\u \). Finally \( \A\u > \0 \) by @lem-entrywise-order-rules (b), and \( r > 0 \), so \( \u = r^{-1}\A\u > \0 \).
:::
:::

Apply the claim to \( \u = \z \), which is non-negative and non-zero because its entries add up to \( 1 \). It gives \( \A\z = r\z \) with \( \z > \0 \). Put \( \v = \z \). So \( r \) is an eigenvalue of \( \A \) with a positive eigenvector.

**Step 3: \( r = \rho(\A) \).** Let \( \lambda \in \nC \) be an eigenvalue of \( \A \) and \( \x \in \nC^n \) an eigenvector for it. By @thm-conjugate-properties (d) and @lem-entrywise-absolute-value (a), with \( \lvert\A\rvert = \A \),
\[
\lvert\lambda\rvert\,\lvert\x\rvert = \lvert\lambda\x\rvert = \lvert\A\x\rvert \le \A\lvert\x\rvert .
\]
The vector \( \lvert\x\rvert \) is non-negative and non-zero, since \( \x \ne \0 \). Dividing by the sum \( \sigma > 0 \) of its entries, \( \x' = \lvert\x\rvert/\sigma \in \Delta_n \) satisfies \( \A\x' \ge \lvert\lambda\rvert\x' \), so \( (\x', \lvert\lambda\rvert) \in S \) and \( \lvert\lambda\rvert \le r \). Since \( r \) is itself an eigenvalue, \( r = \max\{\lvert\lambda\rvert : \lambda \in \spec(\A)\} = \rho(\A) \) (@def-spectral-radius). This proves (a).

**Step 4: eigenvalues of modulus \( r \).** Let \( \lambda \) be an eigenvalue with \( \lvert\lambda\rvert = r \), and \( \x \) an eigenvector. The display of Step 3 reads \( \A\lvert\x\rvert \ge r\lvert\x\rvert \), so the push-up claim applies to \( \lvert\x\rvert \) and gives
\[
\A\lvert\x\rvert = r\lvert\x\rvert \quad\text{and}\quad \lvert\x\rvert > \0 .
\]
Hence \( \lvert\A\x\rvert = \lvert\lambda\rvert\lvert\x\rvert = r\lvert\x\rvert = \A\lvert\x\rvert \). Read the first entry: with \( z_j = a_{1j}x_j \),
\[
\Bigl\lvert\sum_j z_j\Bigr\rvert = \lvert(\A\x)_1\rvert = (\A\lvert\x\rvert)_1 = \sum_j a_{1j}\lvert x_j\rvert = \sum_j\lvert z_j\rvert ,
\]
and \( \sum_j z_j = (\A\x)_1 = \lambda x_1 \ne 0 \), because \( \lvert\lambda x_1\rvert = r\lvert x_1\rvert > 0 \). By @lem-triangle-equality-complex there is \( c \in \nC \) with \( \lvert c\rvert = 1 \) and \( a_{1j}x_j = a_{1j}\lvert x_j\rvert\,c \) for every \( j \). Since \( a_{1j} > 0 \), we may divide: \( x_j = c\lvert x_j\rvert \), that is, \( \x = c\lvert\x\rvert \). Therefore
\[
\lambda\x = \A\x = c\,\A\lvert\x\rvert = c\,r\lvert\x\rvert = r\x ,
\]
and as \( \x \ne \0 \), \( \lambda = r \). So every eigenvalue other than \( r \) has modulus \( < r \), by Step 3. This proves (c). We record what the step showed for \( \lambda = r \) itself: **every eigenvector \( \x \) for \( r \) has the form \( c\lvert\x\rvert \) with \( \lvert c\rvert = 1 \), \( \lvert\x\rvert > \0 \) and \( \A\lvert\x\rvert = r\lvert\x\rvert \).**

**Step 5: \( E_r(\A) = \Span(\v) \).** Let \( \x \) be an eigenvector for \( r \), and write \( \x = c\,\u \) with \( \u = \lvert\x\rvert > \0 \) and \( \A\u = r\u \), as just recorded. Let \( \theta = \min_i u_i/v_i \), which is positive, and put \( \y = \u - \theta\v \). Then \( \y \) is real, \( \y \ge \0 \) by the choice of \( \theta \), \( y_i = 0 \) for an index \( i \) attaining the minimum, and \( \A\y = r\y \). If \( \y \ne \0 \), the push-up claim would give \( \y > \0 \), contradicting \( y_i = 0 \). So \( \y = \0 \), and \( \x = c\theta\,\v \in \Span(\v) \). Hence \( E_r(\A) = \Span(\v) \) and \( g_{\A}(r) = 1 \).

**Step 6: \( a_{\A}(r) = 1 \).** First a positive left eigenvector. \( \A\tp \) is positive, since it has the same entries, and Steps 1–5 used nothing about \( \A \) but its positivity. Applied to \( \A\tp \), they give \( \w > \0 \) with \( \A\tp\w = r'\w \), where \( r' = \rho(\A\tp) \). By @thm-transpose-properties, \( (\A\tp\w)\tp = \w\tp\A \), so
\[
r'\,\w\tp\v = (\A\tp\w)\tp\v = \w\tp\A\v = r\,\w\tp\v .
\]
Here \( \w\tp\v = \sum_i w_iv_i > 0 \), because every term is positive, so \( r' = r \). Hence \( \rho(\A\tp) = r \) and \( \w\tp\A = r\w\tp \).

Now suppose \( a_{\A}(r) \ge 2 \). The characteristic polynomial splits over \( \nC \) (@cor-complex-polynomial-splits), so @thm-generalized-eigenspace-decomposition (c) applies to \( \A \in M_n(\nC) \) and gives \( \dim G_r(\A) = a_{\A}(r) \ge 2 > 1 = \dim E_r(\A) \). Choose \( \x \in G_r(\A) \) with \( \x \notin E_r(\A) \), put \( \N = \A - r\I \), and let \( k \ge 1 \) be least with \( \N^{k}\x = \0 \), which exists by @def-generalized-eigenspace and @thm-well-ordering. Since \( \N\x \ne \0 \), \( k \ge 2 \). Put \( \y = \N^{k-2}\x \). Then \( \N\y = \N^{k-1}\x \ne \0 \) by the minimality of \( k \), and \( \N(\N\y) = \N^{k}\x = \0 \). So \( \N\y \) is an eigenvector for \( r \), and by Step 5, \( \N\y = b\v \) with \( b \ne 0 \). But \( \w\tp\N = \w\tp\A - r\w\tp = \0\tp \), so
\[
0 = (\w\tp\N)\y = \w\tp(\N\y) = b\,\w\tp\v .
\]
Since \( \w\tp\v > 0 \) and \( b \ne 0 \), this is a contradiction. Hence \( a_{\A}(r) \le 1 \), and \( a_{\A}(r) \ge 1 \) because \( r \) is an eigenvalue. Together with Step 5 this proves (b).

**Step 7: non-negative eigenvectors.** Let \( \x \ge \0 \), \( \x \ne \0 \), be an eigenvector for an eigenvalue \( \lambda \). If \( \lambda \ne r \), then @thm-left-right-biorthogonal, applied over \( \nC \) to the left eigenvector \( \w \) for \( r \) and the right eigenvector \( \x \) for \( \lambda \), gives \( \w\tp\x = 0 \). But \( \w\tp\x > 0 \) by @lem-entrywise-order-rules (b), applied to the positive \( 1 \times n \) matrix \( \w\tp \). So \( \lambda = r \), and by Step 5, \( \x = \theta\v \) for a scalar \( \theta \). Comparing any entry, \( \theta = x_i/v_i \) is real and \( \ge 0 \), and it is not \( 0 \) because \( \x \ne \0 \). This proves (d).

Finally, (e): \( \A\tp \) is positive, and Step 6 showed \( \rho(\A\tp) = r \) by pairing with \( \v \), so (a)–(d) hold for \( \A\tp \) by what has been proved, with the positive eigenvector \( \w \) of Step 6. This completes the proof.
:::

::: {.remark}
**Which analysis was used.** Exactly two facts from Chapter 15's introduction, both in Step 1: (A3), that the closed bounded set \( S \) is compact, and (A4), that the continuous function \( t \) attains its maximum on it, together with the algebra of limits from the same introduction, which showed that \( S \) is closed. Everything else is algebra: the order rules, the triangle inequality with its equality case, and the generalized eigenspaces of Chapter 9.
:::

Two examples show what the theorem says.

::: {#exm-perron-two-by-two}
[Perron's theorem for Chapter 8's first example]

Check each part of @thm-perron for \( \A = \begin{pmatrix} 1 & 2 \\ 3 & 2 \end{pmatrix} \).
:::

::: {.solution}
@exm-eigenvalues-2x2 found \( p_{\A}(x) = (x - 4)(x + 1) \), \( E_4(\A) = \Span((2, 3)) \) and \( E_{-1}(\A) = \Span((1, -1)) \). So \( r = \rho(\A) = 4 > 0 \) is an eigenvalue, with the positive eigenvector \( \v = (2, 3) \): part (a). It is a simple root of \( p_{\A} \): part (b). The other eigenvalue has \( \lvert -1\rvert = 1 < 4 \): part (c). Every eigenvector for \( -1 \) is \( t(1, -1) \) with \( t \ne 0 \), which has entries of opposite signs, so none is non-negative: part (d). For (e), the columns of \( \A \) both sum to \( 4 \), so \( \1\tp\A = 4\,\1\tp \) and \( \w = (1, 1) \) is a positive left eigenvector for \( 4 \), as the text after @def-left-eigenvector already observed.
:::

::: {#exm-perron-three-by-three}
[A positive \( 3 \times 3 \) matrix]

Let \( \A = \begin{pmatrix} 1 & 3 & 1 \\ 2 & 2 & 1 \\ 4 & 2 & 3 \end{pmatrix} \). Find its eigenvalues and eigenvectors, and its positive left eigenvector.
:::

::: {.solution}
Try the three vectors \( (1, 1, 2) \), \( (-1, -1, 3) \) and \( (-5, 2, 4) \):
\[
\A\begin{pmatrix} 1 \\ 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 6 \\ 6 \\ 12 \end{pmatrix}, \qquad
\A\begin{pmatrix} -1 \\ -1 \\ 3 \end{pmatrix} = \begin{pmatrix} -1 \\ -1 \\ 3 \end{pmatrix}, \qquad
\A\begin{pmatrix} -5 \\ 2 \\ 4 \end{pmatrix} = \begin{pmatrix} 5 \\ -2 \\ -4 \end{pmatrix} .
\]
So \( 6 \), \( 1 \) and \( -1 \) are eigenvalues. They are distinct, and a \( 3 \times 3 \) matrix has at most three eigenvalues (@cor-eigenspaces-direct-sum), so these are all, each with algebraic multiplicity \( 1 \) because the multiplicities add up to \( 3 \) (@cor-complex-polynomial-splits (a)). As checks, \( \tr\A = 6 = 6 + 1 - 1 \) and \( \det\A = -6 = 6 \cdot 1 \cdot (-1) \). Hence \( \rho(\A) = 6 \), with the positive eigenvector \( \v = (1, 1, 2) \), and the other two eigenvalues have modulus \( 1 < 6 \). The eigenvectors for \( 1 \) and \( -1 \) are the non-zero multiples of \( (-1, -1, 3) \) and \( (-5, 2, 4) \), and each has entries of both signs, as @thm-perron (d) requires.

For the left eigenvector, solve \( (\A\tp - 6\I)\w = \0 \). Row reduction gives \( \w = (10, 11, 7) \), and indeed
\[
\w\tp\A = \begin{pmatrix} 10 + 22 + 28 & 30 + 22 + 14 & 10 + 11 + 21 \end{pmatrix} = \begin{pmatrix} 60 & 66 & 42 \end{pmatrix} = 6\,\w\tp .
\]
The left and right eigenvectors for \( \rho(\A) \) are unrelated in general; here \( \w\tp\v = 10 + 11 + 14 = 35 \) for \( \v = (1, 1, 2) \). @def-perron-vector below scales them so that this pairing is \( 1 \).
:::

::: {.check}
The swap \( \S = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) is non-negative. Which conclusions of @thm-perron hold for \( \S \), and which fail?
:::

::: {.solution}
\( \S \) has eigenvalues \( 1 \) and \( -1 \), with eigenvectors \( (1, 1) \) and \( (1, -1) \). So \( \rho(\S) = 1 \) is an eigenvalue with a positive eigenvector, it is simple, and the only non-negative eigenvectors are the positive multiples of \( (1,1) \): (a), (b), (d) and (e) hold. Part (c) fails, since \( -1 \ne 1 \) and \( \lvert -1\rvert = 1 = \rho(\S) \). The hypothesis that fails is \( \S > 0 \): two entries are \( 0 \). This is the matrix whose powers do not converge in the warning of Chapter 8 §11, and (c) is exactly what was missing there.
:::

The positive eigenvector is so useful that it gets a name.

::: {#def-perron-vector}
[Perron Root, Perron Vector]

Let \( \A \in M_n(\nR) \) be positive. The number \( \rho(\A) \) is the **Perron root** of \( \A \). The **Perron vector** of \( \A \) is the unique \( \v > \0 \) with \( \A\v = \rho(\A)\v \) and \( v_1 + \dots + v_n = 1 \). The **left Perron vector** of \( \A \) is the unique \( \w > \0 \) with \( \w\tp\A = \rho(\A)\w\tp \) and \( \w\tp\v = 1 \), where \( \v \) is the Perron vector.
:::

Existence and uniqueness are @thm-perron (a) and (b): the eigenspace for \( \rho(\A) \) is a line through a positive vector, and it meets the hyperplane \( \{\1\tp\x = 1\} \) in exactly one point, the vector \( \v/(\1\tp\v) \). By (d), the Perron vector is also the **only** eigenvector of \( \A \) in \( \Delta_n \). Likewise, by (e) and (b) applied to \( \A\tp \), the positive left eigenvectors for \( \rho(\A) \) are the positive multiples of one \( \w_0 > \0 \), and since \( \w_0\tp\v > 0 \), exactly one of them, \( \w_0/(\w_0\tp\v) \), pairs with the Perron vector to \( 1 \). The two normalizations differ on purpose: \( \v \) is a probability vector, and \( \w\tp\v = 1 \) makes \( \v\w\tp \) a projection, the limit of \( (\A/\rho(\A))^{k} \) that §05 finds. For @exm-perron-two-by-two the Perron vector is \( \frac15(2, 3) \) and the left Perron vector is \( (1, 1) \), since \( \1\tp\v = 1 \). For @exm-perron-three-by-three the Perron vector is \( \frac14(1, 1, 2) \), and the left Perron vector is \( \frac{4}{35}(10, 11, 7) \), since \( (10, 11, 7) \) pairs with \( \frac14(1, 1, 2) \) to \( \frac{35}{4} \).

::: {.warning}
**Perron's theorem says nothing about the other eigenvalues except their size.** They may be negative, as \( -1 \) is in @exm-perron-two-by-two, or non-real: the positive matrix \( \begin{psmallmatrix} 1 & 2 & 3 \\ 3 & 1 & 2 \\ 2 & 3 & 1 \end{psmallmatrix} \) has row sums \( 6 \), hence the eigenvector \( \1 \) for \( 6 \), and its other two eigenvalues are the roots of \( x^2 + 3x + 3 \), namely \( \frac{-3 \pm i\sqrt3}{2} \), of modulus \( \sqrt3 < 6 \). They may also be repeated, as the eigenvalue \( 1 \) of \( \begin{psmallmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{psmallmatrix} \) is. Simplicity is claimed for \( \rho(\A) \) alone.
:::

## What positivity buys, and what it costs

Each hypothesis of @thm-perron has a job, and it is instructive to see where it went. **Positivity** of \( \A \) was used in the push-up claim, to turn a non-negative, non-zero slack into a strictly positive one; in Step 4, to divide by \( a_{1j} \); and in Step 1, to make \( r > 0 \). For a matrix that is only non-negative, each of these uses fails, and so can each conclusion: Exercise C2 gives a non-negative \( 2 \times 2 \) matrix for each of (a)–(d), and the swap of the Quick check is the one for (c).

§03 shows that one conclusion survives in general, that \( \rho(\A) \) is an eigenvalue with a non-negative eigenvector, and that most of the rest returns under a hypothesis much weaker than positivity. That hypothesis, **irreducibility**, is a condition on where the zero entries are, and §02 introduces it.

Here is the payoff for Chapter 8. A stochastic matrix has \( \1\tp\A = \1\tp \), so \( \1 \) is a positive left eigenvector for \( 1 \). If \( \A \) is stochastic and positive, @thm-perron (d) applied to \( \A\tp \) says that \( \1 \) is a left eigenvector for \( \rho(\A) \) and for no other eigenvalue, so \( \rho(\A) = 1 \). Then (b) and (c) say that \( 1 \) is simple and every other eigenvalue has modulus less than \( 1 \): two of the three hypotheses of @thm-markov-limit-diagonalizable hold automatically. The third, diagonalizability, is the one §06 removes.

## Exercises

### A. Check your understanding

:::: {#exr-positive-matrices-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define what it means for a real matrix to be **non-negative** and to be **positive**, and define \( \lvert\M\rvert \) for a complex matrix \( \M \).
2. State @thm-perron.
3. True or false: a positive symmetric matrix is positive definite. Justify your answer.
4. True or false: a positive matrix has no negative eigenvalue. Justify your answer.
5. True or false: if \( 0 \le \A \le \B \) and \( \A \ne \B \), then \( \rho(\A) < \rho(\B) \). Justify your answer.
6. In the proof of @thm-perron, which step uses compactness, and why is the quotient \( \min_i(\A\x)_i/x_i \) not maximized directly?
:::
::::

::: {.solution}
(a) \( \A \) is non-negative if every entry is \( \ge 0 \), and positive if every entry is \( > 0 \) (@def-entrywise-order). \( \lvert\M\rvert \) is the real matrix whose \( (i,j) \) entry is \( \lvert m_{ij}\rvert \).

(b) If \( \A \in M_n(\nR) \) and \( \A > 0 \), then \( r = \rho(\A) > 0 \) is an eigenvalue of \( \A \) with a positive eigenvector \( \v \); it is algebraically simple; every other eigenvalue has modulus less than \( r \); every non-negative eigenvector is a positive multiple of \( \v \); and the same holds for \( \A\tp \), which gives a positive left eigenvector.

(c) False. \( \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix} \) is positive and symmetric with the eigenvalue \( -1 \); the warning after @def-entrywise-order computes \( \x\tp\A\x = -2 \) for \( \x = (1, -1) \).

(d) False. \( \begin{pmatrix} 1 & 2 \\ 3 & 2 \end{pmatrix} \) has the eigenvalue \( -1 \) (@exm-perron-two-by-two). Perron's theorem controls only the modulus of the other eigenvalues.

(e) False. \( \diag(1, 0) \le \I_2 \), the two differ, and both have spectral radius \( 1 \).

(f) Step 1: the set \( S \) is closed and bounded, so by (A3) and (A4) the coordinate \( t \) attains a maximum on it. The quotient is undefined where some \( x_i = 0 \). For a non-negative matrix its natural repair can be discontinuous on the boundary of \( \Delta_n \) (for \( \diag(2, 1) \) it jumps at \( \e_1 \)), so the extreme value theorem does not apply to it directly. For positive \( \A \) the repair is in fact continuous, but proving that costs more than maximizing \( t \) over \( S \).
:::

### B. Practice

:::: {#exr-positive-matrices-b1}
[B1: A Perron vector by hand]

Let \( \A = \begin{pmatrix} 2 & 1 & 1 \\ 3 & 4 & 3 \\ 3 & 1 & 4 \end{pmatrix} \). Find the eigenvalues of \( \A \), its Perron root, Perron vector and left Perron vector. Check that no eigenvector for the other eigenvalues is non-negative.
::::

::: {.solution}
Expanding \( \det(x\I - \A) \) along the first row,
\[
\begin{aligned}
p_{\A}(x) &= (x - 2)\bigl((x - 4)^2 - 3\bigr) + \bigl(-3(x - 4) - 9\bigr) - \bigl(3 + 3(x - 4)\bigr) \\
&= x^3 - 10x^2 + 23x - 14 = (x - 1)(x - 2)(x - 7) .
\end{aligned}
\]
(Check: \( \tr\A = 10 \) and \( \det\A = 14 \).) So the eigenvalues are \( 7, 2, 1 \), and \( \rho(\A) = 7 \). Solving \( (\A - 7\I)\x = \0 \), whose first two rows are \( -5x_1 + x_2 + x_3 = 0 \) and \( 3x_1 - 3x_2 + 3x_3 = 0 \), gives \( \x = t(1, 3, 2) \); indeed \( \A(1, 3, 2) = (7, 21, 14) \). The entries of \( (1, 3, 2) \) add up to \( 6 \), so the Perron vector is \( \frac16(1, 3, 2) \).

For the left eigenvector, \( (\A\tp - 7\I)\w = \0 \) gives the multiples of \( (3, 2, 3) \), and \( (3, 2, 3)\A = (21, 14, 21) = 7\,(3, 2, 3) \). Against the Perron vector, \( (3, 2, 3) \cdot \frac16(1, 3, 2) = \frac{15}{6} = \frac52 \), so by @def-perron-vector the left Perron vector is \( \frac25(3, 2, 3) = \bigl(\frac65, \frac45, \frac65\bigr) \).

For \( 2 \): \( (\A - 2\I)\x = \0 \) gives \( \x = t(1, 3, -3) \), since \( \A(1, 3, -3) = (2, 6, -6) \). For \( 1 \): \( \x = t(1, 0, -1) \), since \( \A(1, 0, -1) = (1, 0, -1) \). For \( t \ne 0 \) each has entries of both signs, so neither is non-negative, as @thm-perron (d) predicts.
:::

:::: {#exr-positive-matrices-b2}
[B2: Which order?]

For each matrix, decide whether it is non-negative, whether it is positive, and whether it is positive definite. Justify your answers, and say whether @thm-perron applies.

::: {.enumerate options="label=(\alph*)"}
1. \( \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \)
2. \( \begin{pmatrix} 1 & 3 \\ 3 & 1 \end{pmatrix} \)
3. \( \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix} \)
4. \( \begin{pmatrix} 1 & 0 \\ 2 & 3 \end{pmatrix} \)
5. \( \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \)
:::
::::

::: {.solution}
For a real symmetric \( 2 \times 2 \) matrix, positive definite means both eigenvalues are positive (@def-positive-semidefinite, with the spectral theorem).

(a) Positive, hence non-negative. Eigenvalues \( 3, 1 \), both positive, so positive definite. Perron applies: \( \rho = 3 \) with eigenvector \( (1, 1) \).

(b) Positive, hence non-negative. Eigenvalues \( 4, -2 \), so **not** positive definite. Perron applies: \( \rho = 4 \) with eigenvector \( (1,1) \), and \( \lvert -2\rvert < 4 \).

(c) Not non-negative, since the off-diagonal entries are \( -1 \); so not positive, and Perron does not apply. It is positive definite, with eigenvalues \( 1, 3 \).

(d) Non-negative, not positive (the \( (1,2) \) entry is \( 0 \)), and not symmetric, so not positive definite by clause (P1). Perron does not apply, although here \( \rho = 3 \) is an eigenvalue with the eigenvector \( \e_2 \ge \0 \), which is not positive.

(e) Positive. Eigenvalues \( 2 \) and \( 0 \), so positive semidefinite but **not** positive definite, as \( \x = (1, -1) \) gives \( \x\tp\A\x = 0 \). Perron applies: \( \rho = 2 \), eigenvector \( (1,1) \), and the eigenvalue \( 0 \) has modulus less than \( 2 \).
:::

:::: {#exr-positive-matrices-b3}
[B3: Bounds from the smallest and largest entry]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \rho(c\J) = nc \) for every real \( c \ge 0 \), where \( \J \) is the \( n \times n \) all-ones matrix.
2. Let \( \A \in M_n(\nR) \) with \( a \le a_{ij} \le b \) for all \( i, j \), where \( 0 \le a \le b \). Prove that \( na \le \rho(\A) \le nb \).
3. Hence bound \( \rho(\A) \) for \( \A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 3 & 1 \\ 3 & 1 & 2 \end{pmatrix} \), and compare with its exact value.
:::
::::

::: {.solution}
(a) \( \J\1 = n\1 \), so \( n \) is an eigenvalue of \( \J \). Also \( \J^2 = n\J \), since every entry of \( \J^2 \) is a sum of \( n \) ones. If \( \J\x = \lambda\x \) with \( \x \ne \0 \), then \( \lambda^2\x = \J^2\x = n\J\x = n\lambda\x \), so \( \lambda^2 = n\lambda \) and \( \lambda \in \{0, n\} \). Hence \( \rho(\J) = n \), and \( \rho(c\J) = c\,\rho(\J) = nc \) because the eigenvalues of \( c\J \) are \( c \) times those of \( \J \).

(b) The hypothesis says \( 0 \le a\J \le \A \le b\J \). By @prp-spectral-radius-monotone (a), applied twice, \( \rho(a\J) \le \rho(\A) \le \rho(b\J) \), and by (a) this reads \( na \le \rho(\A) \le nb \).

(c) The entries lie between \( 1 \) and \( 3 \) and \( n = 3 \), so \( 3 \le \rho(\A) \le 9 \). In fact every row sums to \( 6 \), so \( \A\1 = 6\,\1 \), and @thm-perron (d) says the positive eigenvector \( \1 \) belongs to \( \rho(\A) \). Hence \( \rho(\A) = 6 \).
:::

### C. Going deeper

:::: {#exr-positive-matrices-c1}
[C1: Symmetry passes to the Perron vector]

Let \( \A > 0 \) be \( n \times n \) with Perron vector \( \v \), and let \( \P \) be a permutation matrix with \( \P\tp\A\P = \A \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \P\v = \v \).
2. Deduce that the Perron vector of \( \A = \begin{pmatrix} 1 & 1 & 3 \\ 1 & 1 & 3 \\ 1 & 1 & 1 \end{pmatrix} \) has equal first and second entries, and find it.
3. Deduce that if \( \A > 0 \) commutes with the cyclic permutation matrix of \( 1 \to 2 \to \dots \to n \to 1 \), then its Perron vector is \( \frac1n\1 \).
:::

*Hint: for (a), \( \P\v \) is a positive vector in \( \Delta_n \).*
::::

::: {.solution}
(a) By @lem-permutation-matrices (b), \( \P\P\tp = \I \), so \( \A\P = \P\P\tp\A\P = \P\A \). Hence \( \A(\P\v) = \P\A\v = \rho(\A)\,\P\v \). The entries of \( \P\v \) are those of \( \v \) in another order (\( \P = \P_\sigma \) sends \( \e_j \) to \( \e_{\sigma(j)} \)), so \( \P\v > \0 \) and its entries add up to \( 1 \). By @def-perron-vector and the uniqueness proved after it, \( \P\v = \v \).

(b) Let \( \P \) be the permutation matrix that swaps \( \e_1 \) and \( \e_2 \). Then \( \P\tp\A\P \) is \( \A \) with rows \( 1, 2 \) swapped and columns \( 1, 2 \) swapped, which is \( \A \) again, because rows \( 1 \) and \( 2 \) of \( \A \) are equal and so are columns \( 1 \) and \( 2 \). By (a), \( \P\v = \v \), that is, \( v_1 = v_2 \). Now try \( \v = (1, 1, c) \): \( \A\v = (2 + 3c, 2 + 3c, 2 + c) \), and \( \A\v = \lambda\v \) requires \( \lambda = 2 + 3c \) and \( 2 + c = (2 + 3c)c \), that is, \( 3c^2 + c - 2 = 0 \), so \( c = \frac23 \) or \( c = -1 \). The positive choice \( c = \frac23 \) gives the eigenvector \( (3, 3, 2) \) with eigenvalue \( 4 \), and by @thm-perron (d) this is the Perron eigenvector, so \( \rho(\A) = 4 \) and the Perron vector is \( \frac18(3, 3, 2) \).

(c) Let \( \C \) be the cyclic permutation matrix, \( \C\e_j = \e_{j+1} \) for \( j < n \) and \( \C\e_n = \e_1 \). If \( \A\C = \C\A \), then \( \C\tp\A\C = \C\tp\C\A = \A \) by @lem-permutation-matrices (b). By (a), \( \C\v = \v \), which says \( v_n = v_1 \) and \( v_j = v_{j+1} \) for \( j < n \), so all entries are equal. As they add up to \( 1 \), \( \v = \frac1n\1 \).
:::

:::: {#exr-positive-matrices-c2}
[C2: Every conclusion fails for some non-negative matrix]

For each part of @thm-perron, (a) to (d), give a non-negative \( 2 \times 2 \) matrix for which that part fails, and name the step of the proof that breaks. Then give a non-negative matrix for which (a), (b) and (c) fail at the same time.
::::

::: {.solution}
(a) \( \J_2(0) = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) has \( \rho = 0 \), and its eigenvectors are the non-zero multiples of \( \e_1 \), none positive. In the proof, \( r > 0 \) came from the smallest row sum, which here is \( 0 \); and the push-up claim fails, since \( \u = \e_1 \) satisfies \( \A\u = 0\cdot\u \) without being positive.

(b) \( \I_2 \): \( \rho = 1 \) is a double eigenvalue and \( E_1 = \nR^2 \). Step 5 fails: \( \u - \theta\v \) can be non-zero and non-negative with a zero entry, since \( \A\y > \0 \) is no longer forced.

(c) \( \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \): the eigenvalue \( -1 \) has modulus \( \rho = 1 \). Step 4 fails: equality in the triangle inequality (@lem-triangle-equality-complex) is automatic when each row has a single non-zero term, so it aligns nothing.

(d) \( \diag(2, 1) \): the eigenvector \( \e_2 \ge \0 \) belongs to \( 1 \ne 2 = \rho \). Step 7 fails, because the left eigenvector for \( 2 \) is \( \e_1 \), which is not positive, and \( \e_1\tp\e_2 = 0 \) is no contradiction.

For all three at once, take
\[
\A = \begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} .
\]
It is block upper triangular with diagonal blocks \( \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) and \( (1) \), so \( p_{\A}(x) = (x^2 - 1)(x - 1) = (x - 1)^2(x + 1) \) by @thm-det-block-triangular, applied to \( x\I - \A \) over \( F[x] \), as the paragraph after it notes. Hence \( \rho(\A) = 1 \) and \( a_{\A}(1) = 2 \), so (b) fails, and \( \lvert -1\rvert = \rho(\A) \), so (c) fails. The system \( (\A - \I)\x = \0 \) reads \( -x_1 + x_2 + x_3 = 0 \) and \( x_1 - x_2 = 0 \), which forces \( x_3 = 0 \); so every eigenvector for \( 1 \) is a multiple of \( (1, 1, 0) \), none of them positive, and (a) fails.
:::

:::: {#exr-positive-matrices-c3}
[C3: The Perron root is strictly monotone]

Let \( \A, \B \in M_n(\nR) \) with \( 0 < \A \le \B \) and \( \A \ne \B \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \rho(\A) < \rho(\B) \).
2. Show by an example that the conclusion fails if \( \A > 0 \) is weakened to \( \A \ge 0 \).
:::

*Hint: pair \( \B\v \) with a positive left eigenvector of \( \B \), where \( \v \) is the Perron vector of \( \A \).*
::::

::: {.solution}
(a) \( \B \ge \A > 0 \), so \( \B \) is positive too. Let \( \v > \0 \) be the Perron vector of \( \A \), and by @thm-perron (e) let \( \w > \0 \) satisfy \( \w\tp\B = \rho(\B)\w\tp \). Then
\[
\rho(\B)\,\w\tp\v = \w\tp\B\v = \w\tp\A\v + \w\tp(\B - \A)\v = \rho(\A)\,\w\tp\v + \w\tp(\B - \A)\v .
\]
The matrix \( \B - \A \) is non-negative and non-zero, say \( b_{kl} - a_{kl} > 0 \), so \( \w\tp(\B - \A)\v \ge w_k(b_{kl} - a_{kl})v_l > 0 \), every other term being \( \ge 0 \). Since \( \w\tp\v > 0 \), dividing gives \( \rho(\B) > \rho(\A) \).

(b) \( \A = \diag(1, 0) \) and \( \B = \I_2 \) satisfy \( 0 \le \A \le \B \) and \( \A \ne \B \), with \( \rho(\A) = \rho(\B) = 1 \). In the argument of (a), the Perron vector of \( \A \) is replaced by \( \e_1 \), and \( (\B - \A)\e_1 = \0 \): the extra mass sits where the eigenvector does not look.
:::
