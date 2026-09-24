# Continuity of Roots

Chapter 16 §07 proved that the eigenvalues of a matrix move continuously with the matrix, but only after quoting a theorem it did not prove: the roots of a monic polynomial move continuously with its coefficients (@thm-roots-depend-continuously). This section proves that theorem, with nothing more than the compactness of closed bounded sets. It then asks two quantitative questions the qualitative theorem cannot answer. How far can an eigenvalue move when the matrix moves by a given amount, with no hypothesis on the matrix at all? And how many eigenvalues does a region of the plane hold? The second question finishes the story of Gershgorin's discs begun in Section 1: an isolated disc holds **exactly one** eigenvalue.

Throughout, matrices are complex and eigenvalues are listed with algebraic multiplicity, so that \( \A \in M_n(\nC) \) has exactly \( n \) of them (@cor-complex-polynomial-splits). Two imported facts of analysis are used, and each is named where it acts: compactness, fact (A3) of Chapter 16's introduction, and the intermediate value theorem, fact (A5).

## A bound for the roots

The proof of continuity will take a sequence of polynomials and follow their roots. For that to work, the roots must not escape to infinity, and the first step is a bound on the roots in terms of the coefficients.

::: {#lem-cauchy-root-bound}
[Cauchy's Bound for the Roots]

Let \( n \ge 1 \) and let \( p(x) = x^n + c_{n-1}x^{n-1} + \dots + c_1x + c_0 \in \nC[x] \) be monic. Put \( M = \max_{0 \le j \le n-1}\lvert c_j\rvert \). Then every root \( z \in \nC \) of \( p \) satisfies
\[
\lvert z\rvert \le 1 + M .
\]
:::

::: {.idea}
A root satisfies \( z^n = -(c_{n-1}z^{n-1} + \dots + c_0) \). If \( \lvert z\rvert \) is large, the left side is much bigger than every single term on the right, and there are only \( n \) terms; summing the geometric series on the right makes this precise.
:::

::: {.proof}
If \( \lvert z\rvert \le 1 \) there is nothing to prove, so suppose \( \lvert z\rvert > 1 \). Since \( p(z) = 0 \), we have \( z^n = -\sum_{j=0}^{n-1}c_jz^j \), and the triangle inequality (@thm-complex-triangle-inequality) gives
\[
\lvert z\rvert^n \le M\sum_{j=0}^{n-1}\lvert z\rvert^j
= M\,\frac{\lvert z\rvert^n - 1}{\lvert z\rvert - 1}
\le M\,\frac{\lvert z\rvert^n}{\lvert z\rvert - 1} ,
\]
where the equality sums a geometric series with ratio \( \lvert z\rvert \ne 1 \). Dividing by \( \lvert z\rvert^n > 0 \) and multiplying by \( \lvert z\rvert - 1 > 0 \) gives \( \lvert z\rvert - 1 \le M \), as claimed.
:::

The bound depends only on the size of the coefficients, and that is what the next proof needs. Polynomials whose coefficients stay bounded have roots that stay bounded.

::: {.check}
Show that the \( 1 \) in the bound cannot be dropped: find a monic polynomial with a root of modulus larger than \( M = \max_j\lvert c_j\rvert \).
:::

::: {.solution}
Take \( p(x) = x^2 - x - 1 \), with \( M = 1 \). Its roots are \( (1 \pm \sqrt5)/2 \), and \( (1 + \sqrt5)/2 \approx 1.618 > 1 \). The bound \( 1 + M = 2 \) does hold.
:::

## The roots move continuously

Here is the theorem of Chapter 16 (@thm-roots-depend-continuously), restated in full under its own label, since from now on it is a proved result.

::: {#thm-roots-continuous}
[Continuous Dependence of the Roots on the Coefficients]

Let \( n \ge 1 \) and let
\[
p(x) = x^n + c_{n-1}x^{n-1} + \dots + c_1x + c_0 \in \nC[x]
\]
be monic, with roots \( \mu_1, \dots, \mu_n \in \nC \) listed with multiplicity. Let \( \varepsilon > 0 \). Then there is \( \delta > 0 \) with the following property. If
\[
q(x) = x^n + b_{n-1}x^{n-1} + \dots + b_1x + b_0
\]
is monic of the **same degree** \( n \) and \( \lvert b_j - c_j\rvert < \delta \) for every \( j \), then the roots \( \nu_1, \dots, \nu_n \) of \( q \), listed with multiplicity, can be **numbered** so that \( \lvert \nu_i - \mu_i\rvert < \varepsilon \) for \( i = 1, \dots, n \).
:::

::: {.idea}
The hard direction, from coefficients to roots, has no formula. The easy direction does: expanding \( (x - \nu_1)\cdots(x - \nu_n) \) writes each coefficient as a polynomial in the roots. So argue by contradiction and let compactness supply the missing formula.

① A bad sequence \( q_k \to p \) has root vectors that stay bounded, by Cauchy's bound. ② By compactness, a subsequence of root vectors converges to some \( \vnu \in \nC^n \). ③ Coefficients are polynomials in roots, so \( (x - \nu_1)\cdots(x - \nu_n) \) has the limiting coefficients, which are those of \( p \). ④ Unique factorization says \( \vnu \) is a rearrangement of \( (\mu_1, \dots, \mu_n) \). ⑤ That rearrangement is a good numbering for the late \( q_k \), which were supposed to have none.
:::

::: {.proof}
Suppose the conclusion fails for some \( \varepsilon > 0 \). Then no \( \delta \) works; in particular \( \delta = 1/k \) fails for every integer \( k \ge 1 \). So there is a monic \( q_k(x) = x^n + \sum_{j<n}b_j^{(k)}x^j \) with \( \lvert b_j^{(k)} - c_j\rvert < 1/k \) for every \( j \), whose roots admit **no** numbering within \( \varepsilon \) of \( \mu_1, \dots, \mu_n \). By @cor-complex-polynomial-splits (a), \( q_k = (x - \nu_1^{(k)})\cdots(x - \nu_n^{(k)}) \) for some \( \vnu^{(k)} = (\nu_1^{(k)}, \dots, \nu_n^{(k)}) \in \nC^n \), which lists the roots of \( q_k \) with multiplicity.

*The root vectors are bounded.* Put \( M = \max_j\lvert c_j\rvert \). Then \( \lvert b_j^{(k)}\rvert < M + 1 \), so by @lem-cauchy-root-bound every \( \lvert \nu_i^{(k)}\rvert \le M + 2 \), and \( \norm{\vnu^{(k)}}_2 \le \sqrt n\,(M + 2) \). By compactness, fact (A3), the sequence \( (\vnu^{(k)}) \) has a subsequence \( (\vnu^{(k_l)})_{l \ge 1} \) converging in \( \nC^n \) to some \( \vnu = (\nu_1, \dots, \nu_n) \). Since \( \lvert \nu_i^{(k_l)} - \nu_i\rvert \le \norm{\vnu^{(k_l)} - \vnu}_2 \), each coordinate converges: \( \nu_i^{(k_l)} \to \nu_i \).

*The limit is a root vector of \( p \).* Expanding the product \( (x - z_1)\cdots(x - z_n) \) gives \( x^n + \sum_{j<n}s_j(z_1, \dots, z_n)x^j \), where each \( s_j \) is a fixed polynomial with integer coefficients in \( z_1, \dots, z_n \) (it is \( \pm \) the sum of all products of \( n - j \) of the \( z_i \) with distinct indices). Hence \( b_j^{(k)} = s_j(\vnu^{(k)}) \). Along the subsequence, the algebra of limits gives \( s_j(\vnu^{(k_l)}) \to s_j(\vnu) \), while \( b_j^{(k_l)} \to c_j \) by the choice of \( q_k \). Limits are unique, so \( s_j(\vnu) = c_j \) for every \( j \), that is,
\[
(x - \nu_1)(x - \nu_2)\cdots(x - \nu_n) = p(x) = (x - \mu_1)(x - \mu_2)\cdots(x - \mu_n) .
\]
Each factor \( x - a \) is monic of degree \( 1 \), hence irreducible, so both sides are factorizations of \( p \) into monic irreducibles. By the uniqueness in @thm-unique-factorization-polynomials (b), there is a permutation \( \pi \) of \( \{1, \dots, n\} \) with \( \nu_{\pi(i)} = \mu_i \) for every \( i \).

*The contradiction.* For each \( i \), \( \nu_{\pi(i)}^{(k_l)} \to \nu_{\pi(i)} = \mu_i \), so there is \( L_i \) with \( \lvert \nu_{\pi(i)}^{(k_l)} - \mu_i\rvert < \varepsilon \) for all \( l \ge L_i \). Take \( l \ge \max_i L_i \). Then the list \( \nu_{\pi(1)}^{(k_l)}, \dots, \nu_{\pi(n)}^{(k_l)} \) is a numbering of the roots of \( q_{k_l} \), with multiplicity, within \( \varepsilon \) of \( \mu_1, \dots, \mu_n \). This contradicts the choice of \( q_{k_l} \), and proves the theorem.
:::

Chapter 16 quoted this statement as @thm-roots-depend-continuously and left its proof to this section. The proof needed nothing beyond compactness and unique factorization, and @cor-eigenvalues-continuous, with everything Chapter 16 built on it, now rests on a proved theorem.

Each hypothesis of the theorem did a job in the proof. **Monic of the same degree** gave both the bound on the roots and the factorization of \( q_k \) with exactly \( n \) linear factors. **Numbered so that** is where the permutation \( \pi \) went. It was produced by unique factorization and depends on the subsequence, which is exactly the freedom that @prp-no-continuous-root-selection says cannot be removed.

::: {.remark}
The proof is an instance of a move worth naming: **compactness plus uniqueness**. To show that \( x \) depends continuously on \( y \) when only the inverse relation \( y = F(x) \) is explicit, take a sequence, extract a convergent subsequence by compactness, and use the uniqueness of the solution of \( y = F(x) \) to identify its limit. Here \( F \) sends a root vector to the coefficients, and "unique" means unique up to order.
:::

## How far: Elsner's bound

The theorem says that a small enough perturbation moves the roots a little, and it gives no rate. Chapter 16's example @exm-jordan-block-perturbation showed that no bound of the form \( L\norm{\E} \) can hold. What *does* hold, for every matrix, is a bound by the \( n \)-th root of \( \norm{\E} \). The proof bounds one determinant in two ways: from below by the eigenvalues, and from above by Hadamard's inequality.

::: {#thm-elsner-spectral-variation}
[Elsner's Spectral Variation Bound]

Let \( \A, \B \in M_n(\nC) \), and let \( \lambda_1, \dots, \lambda_n \) be the eigenvalues of \( \A \). Then every eigenvalue \( \mu \) of \( \B \) satisfies
\[
\min_{1 \le i \le n}\lvert \lambda_i - \mu\rvert \le
\bigl(\norm{\A}_2 + \norm{\B}_2\bigr)^{1 - 1/n}\,\norm{\A - \B}_2^{1/n} .
\]
(For \( n = 1 \) the first factor is \( 1 \).)
:::

::: {.idea}
The quantity \( \prod_i\lvert \lambda_i - \mu\rvert \) is \( \lvert \det(\A - \mu\I)\rvert \), and it is at least the \( n \)-th power of the smallest factor. Bound the determinant above by Hadamard's inequality, after rotating to an orthonormal basis whose first vector is an eigenvector \( \x \) of \( \B \). The first column is then \( (\A - \mu\I)\x = (\A - \B)\x \), which is small. The other \( n - 1 \) columns are merely bounded. So one small factor meets \( n - 1 \) bounded ones, and taking \( n \)-th roots produces the exponent \( 1/n \).
:::

::: {.proof}
Let \( \x \) be an eigenvector of \( \B \) for \( \mu \) with \( \norm{\x}_2 = 1 \). By @cor-extend-orthonormal-basis, extend \( (\x) \) to an orthonormal basis \( (\u_1, \dots, \u_n) \) of \( \nC^n \) with \( \u_1 = \x \), and let \( \U \) be the unitary matrix with these columns. Then \( \U^{*}\U = \I \), so \( \lvert\det\U\rvert^2 = \det\U^{*}\det\U = 1 \) by @thm-det-multiplicative and @thm-det-transpose.

By @cor-det-product-eigenvalues-again applied to \( \A - \mu\I \), whose eigenvalues are the \( \lambda_i - \mu \), listed with the same multiplicities (@thm-spectral-mapping, with \( q(x) = x - \mu \)), and by @thm-det-multiplicative,
\[
\prod_{i=1}^{n}\lvert \lambda_i - \mu\rvert
= \lvert\det(\A - \mu\I)\rvert
= \lvert\det\bigl((\A - \mu\I)\U\bigr)\rvert .
\]
The \( j \)-th column of \( (\A - \mu\I)\U \) is \( (\A - \mu\I)\u_j \). Hadamard's inequality @thm-hadamard-inequality (b) bounds the determinant by the product of the column lengths.

For \( j = 1 \), \( (\A - \mu\I)\x = \A\x - \B\x = (\A - \B)\x \), so \( \norm{(\A - \mu\I)\u_1}_2 \le \norm{\A - \B}_2 \) by @thm-operator-norm-properties (a). For \( j \ge 2 \), the triangle inequality (@cor-triangle-inequality) gives \( \norm{(\A - \mu\I)\u_j}_2 \le \norm{\A}_2 + \lvert\mu\rvert \), and \( \lvert\mu\rvert \le \rho(\B) \le \norm{\B}_2 \) by @thm-spectral-radius-le-norm. Writing \( \delta = \min_i\lvert \lambda_i - \mu\rvert \), each factor on the left is at least \( \delta \), so
\[
\delta^{n} \le \prod_{i=1}^{n}\lvert \lambda_i - \mu\rvert
\le \norm{\A - \B}_2\,\bigl(\norm{\A}_2 + \norm{\B}_2\bigr)^{n-1} .
\]
Taking non-negative \( n \)-th roots, which preserves inequalities between non-negative reals, gives the claim.
:::

The bound needs no hypothesis on \( \A \): no diagonalizability, no normality. It is a **Hölder modulus of continuity with exponent \( 1/n \)**. The next example shows that the exponent cannot be improved, and that is the quantitative form of the instability that Chapter 10 §03 warned about.

::: {#exm-jordan-root-perturbation}
[The Jordan block meets Elsner's bound]

Let \( n \ge 2 \) and \( 0 < \varepsilon \le 1 \), and put \( \A = \J_n(0) \) and \( \B = \J_n(0) + \varepsilon\,\e_n\e_1\tp \). Compare the movement of the eigenvalues with Elsner's bound, and show that no bound of the form \( C(\norm{\A}_2 + \norm{\B}_2)^{1-\alpha}\norm{\A - \B}_2^{\alpha} \) with \( \alpha > 1/n \) can hold for all \( \A, \B \in M_n(\nC) \).
:::

::: {.solution}
*The eigenvalues.* The matrix \( \B \) is the one of @exm-jordan-block-perturbation with \( k = n \), where \( p_{\B}(x) = x^n - \varepsilon \) was computed. So the eigenvalues of \( \B \) are the \( n \) complex \( n \)-th roots of \( \varepsilon \), each of modulus \( \varepsilon^{1/n} \), while \( \A \) has the single eigenvalue \( 0 \). Every eigenvalue has moved exactly \( \varepsilon^{1/n} \).

*The norms.* \( \A - \B = -\varepsilon\,\e_n\e_1\tp \) has the single non-zero entry \( -\varepsilon \), so \( \norm{\A - \B}_2 = \varepsilon \) (@thm-operator-norm-formulas (c)). Next, \( \B\e_1 = \varepsilon\e_n \) and \( \B\e_j = \e_{j-1} \) for \( j \ge 2 \), so for \( \x = (x_1, \dots, x_n) \)
\[
\norm{\B\x}_2^2 = \varepsilon^2\lvert x_1\rvert^2 + \sum_{j=2}^{n}\lvert x_j\rvert^2 \le \norm{\x}_2^2 ,
\]
with equality at \( \x = \e_2 \). Hence \( \norm{\B}_2 = 1 \), and the same computation with \( \varepsilon = 0 \) gives \( \norm{\A}_2 = 1 \).

*The comparison.* Elsner's bound is \( 2^{1 - 1/n}\varepsilon^{1/n} \), and the actual movement is \( \varepsilon^{1/n} \). The bound is attained up to a factor \( 2^{1 - 1/n} < 2 \).

*The exponent is optimal.* If a bound \( C\,2^{1-\alpha}\varepsilon^{\alpha} \) held for these pairs with \( \alpha > 1/n \), then \( \varepsilon^{1/n} \le C\,2^{1-\alpha}\varepsilon^{\alpha} \), that is, \( \varepsilon^{1/n - \alpha} \le 2^{1-\alpha}C \), for every \( \varepsilon \in (0, 1] \). But \( 1/n - \alpha < 0 \), so the left side tends to \( \infty \) as \( \varepsilon \to 0^{+} \). No such \( C \) exists.
:::

Put numbers on it. For \( n = 16 \) and \( \varepsilon = 10^{-16} \), a change in the sixteenth decimal place of one entry, the eigenvalues of \( \J_{16}(0) \) move to the circle of radius \( (10^{-16})^{1/16} = 10^{-1} \). This pays the debt of Chapter 10 §03, whose warning said that the Jordan form is not stable under small changes of the matrix and that Chapter 20 returns to this point. Elsner's theorem says how unstable the eigenvalues can be: never worse than \( \norm{\E}^{1/n} \). The Jordan block says that this worst case happens. Arithmetic that keeps about sixteen significant digits commits errors of about this relative size at every step. So what such a computation returns are, at best, the eigenvalues of some matrix within about \( 10^{-16} \) of \( \J_{16}(0) \), and these may be spread around a circle of radius \( 0.1 \). The computation cannot tell a nilpotent Jordan block from a diagonalizable matrix with sixteen distinct eigenvalues. This is the numerical reason the Jordan form is not computed in floating-point arithmetic.

## Counting eigenvalues in a region

Section 1 showed that every eigenvalue lies in the union of the Gershgorin discs (@thm-gershgorin), and left open how many lie in each part of that union. The tool for counting is a principle in the spirit of one the proof of @prp-no-continuous-root-selection already used: **an integer-valued function that varies continuously cannot change**. We apply it to the number of eigenvalues in a region, while the matrix moves along a segment.

::: {#lem-eigenvalue-count-constant}
[Eigenvalue Counts Are Constant Along a Path]

Let \( \A_0, \A_1 \in M_n(\nC) \), and put \( \A(t) = (1 - t)\A_0 + t\A_1 \) for \( t \in [0, 1] \). Let \( K, L \subseteq \nC \) be sets at **positive distance**: there is \( d > 0 \) with \( \lvert z - w\rvert \ge d \) for all \( z \in K \) and \( w \in L \). Suppose that for **every** \( t \in [0, 1] \), every eigenvalue of \( \A(t) \) lies in \( K \cup L \). Then the number \( N(t) \) of eigenvalues of \( \A(t) \) in \( K \), counted with algebraic multiplicity, does not depend on \( t \). In particular \( N(0) = N(1) \).
:::

::: {.idea}
The eigenvalues cannot jump across the gap between \( K \) and \( L \), because they move continuously and are never allowed inside the gap. So near each \( t_0 \) the count is unchanged, and a function that is locally constant on an interval is constant. The last step is the intermediate value theorem: a continuous function with integer values cannot pass from one integer to another without taking the values in between.
:::

::: {.proof}
Fix \( t_0 \in [0, 1] \). By @cor-eigenvalues-continuous, applied to \( \A(t_0) \) with the tolerance \( d \) and the norm \( \norm{\cdot}_2 \), there is \( \delta > 0 \) such that every \( \B \) with \( \norm{\B - \A(t_0)}_2 < \delta \) has its eigenvalues \( \mu_i \) numbered so that \( \lvert \mu_i - \lambda_i\rvert < d \), where \( \lambda_1, \dots, \lambda_n \) are the eigenvalues of \( \A(t_0) \). Now \( \A(t) - \A(t_0) = (t - t_0)(\A_1 - \A_0) \), so \( \norm{\A(t) - \A(t_0)}_2 < \delta \) whenever \( \lvert t - t_0\rvert\,\norm{\A_1 - \A_0}_2 < \delta \), which holds for all \( t \) close enough to \( t_0 \).

For such \( t \), number the eigenvalues \( \mu_i \) of \( \A(t) \) in this way. Both \( \lambda_i \) and \( \mu_i \) lie in \( K \cup L \), and a point of \( K \) is at distance at least \( d \) from every point of \( L \). Since \( \lvert \mu_i - \lambda_i\rvert < d \), the two lie in the same one of the two sets: \( \mu_i \in K \) if and only if \( \lambda_i \in K \). Counting indices, \( N(t) = N(t_0) \).

So \( N \) is constant on a neighborhood of each point of \( [0, 1] \). In particular \( N \) is continuous: if \( t_k \to t_0 \), then \( N(t_k) = N(t_0) \) for all large \( k \). Suppose \( N(s) \ne N(0) \) for some \( s \in (0, 1] \), say \( N(s) > N(0) \); the other case is symmetric. By the intermediate value theorem, fact (A5), applied to \( N \) on \( [0, s] \), there is \( t \) with \( N(t) = N(0) + \tfrac12 \), which is not an integer. This contradiction shows \( N(s) = N(0) \) for every \( s \in [0, 1] \), and proves the lemma.
:::

Now the counting theorem. The trick is to shrink the off-diagonal part of \( \A \) to zero. At the start of the path the matrix is diagonal and its eigenvalues are the disc centers, which we can count by looking.

::: {#thm-gershgorin-counting}
[Gershgorin's Counting Theorem]

Let \( \A \in M_n(\nC) \), let \( S \subseteq \{1, \dots, n\} \) have \( k \) elements with \( 1 \le k \le n - 1 \), and put
\[
U = \bigcup_{i \in S} D_i(\A), \qquad V = \bigcup_{i \notin S} D_i(\A) .
\]
If \( U \cap V = \emptyset \), then \( U \) contains exactly \( k \) eigenvalues of \( \A \) and \( V \) contains exactly \( n - k \), counted with algebraic multiplicity.
:::

::: {.idea}
Let \( \D = \diag(a_{11}, \dots, a_{nn}) \) and slide from \( \D \) to \( \A \) along \( \A(t) = (1 - t)\D + t\A \). The discs of \( \A(t) \) have the same centers and radii \( t\,r_i(\A) \), so they grow from points into the discs of \( \A \) and never leave \( U \cup V \). By @thm-gershgorin the eigenvalues never leave either, and @lem-eigenvalue-count-constant carries the count from \( t = 0 \), where it is \( k \), to \( t = 1 \).
:::

::: {.proof}
*The two unions are at positive distance.* Let \( i \in S \) and \( j \notin S \). The discs \( D_i(\A) \) and \( D_j(\A) \) are disjoint, so \( \lvert a_{ii} - a_{jj}\rvert > r_i(\A) + r_j(\A) \); otherwise the point on the segment from \( a_{ii} \) to \( a_{jj} \) at distance \( \min\{r_i(\A), \lvert a_{ii} - a_{jj}\rvert\} \) from \( a_{ii} \) would lie in both. For \( z \in D_i(\A) \) and \( w \in D_j(\A) \), the triangle inequality (@thm-complex-triangle-inequality) gives
\[
\lvert z - w\rvert \ge \lvert a_{ii} - a_{jj}\rvert - r_i(\A) - r_j(\A) > 0 .
\]
Call the middle quantity \( d_{ij} \). The minimum \( d \) of the finitely many \( d_{ij} \) is positive, and every point of \( U \) is at distance at least \( d \) from every point of \( V \).

*The path.* Let \( \D = \diag(a_{11}, \dots, a_{nn}) \) and \( \A(t) = (1 - t)\D + t\A \) for \( t \in [0, 1] \). The diagonal entries of \( \A(t) \) are the \( a_{ii} \), and its off-diagonal entries are \( t\,a_{ij} \), so \( r_i(\A(t)) = t\,r_i(\A) \le r_i(\A) \) and \( D_i(\A(t)) \subseteq D_i(\A) \). By @thm-gershgorin applied to \( \A(t) \), every eigenvalue of \( \A(t) \) lies in \( \bigcup_i D_i(\A(t)) \subseteq U \cup V \). By @lem-eigenvalue-count-constant with \( K = U \) and \( L = V \), the number of eigenvalues of \( \A(t) \) in \( U \) is the same at \( t = 0 \) and at \( t = 1 \).

*The count at \( t = 0 \).* \( \A(0) = \D \) is diagonal, so \( p_{\D}(x) = \prod_i(x - a_{ii}) \) by @thm-det-triangular, and its eigenvalue list is \( a_{11}, \dots, a_{nn} \). For \( i \in S \), \( a_{ii} \) is the center of \( D_i(\A) \), so \( a_{ii} \in U \). For \( i \notin S \), \( a_{ii} \in V \), hence \( a_{ii} \notin U \). So exactly \( k \) entries of the list lie in \( U \).

Therefore \( \A(1) = \A \) has exactly \( k \) eigenvalues in \( U \). All \( n \) eigenvalues lie in \( U \cup V \), and \( U \cap V = \emptyset \), so the other \( n - k \) lie in \( V \). This proves the theorem.
:::

The case \( k = 1 \) is the one used most, and for a real matrix it says something about reality as well.

::: {#cor-isolated-gershgorin-disc}
[An Isolated Disc Holds One Eigenvalue]

Let \( \A \in M_n(\nC) \) with \( n \ge 2 \), and suppose \( D_i(\A) \) is disjoint from \( D_j(\A) \) for every \( j \ne i \).

::: {.enumerate options="label=(\alph*)"}
1. \( D_i(\A) \) contains exactly one eigenvalue of \( \A \), and it is **algebraically simple**.
2. If \( \A \) is **real**, that eigenvalue is real, and it lies in the interval \( [a_{ii} - r_i(\A), a_{ii} + r_i(\A)] \).
:::
:::

::: {.proof}
(a) Take \( S = \{i\} \). Then \( U = D_i(\A) \) is disjoint from the union \( V \) of the other discs, because it is disjoint from each of them. By @thm-gershgorin-counting, \( D_i(\A) \) contains exactly one eigenvalue counted with algebraic multiplicity, so that eigenvalue \( \lambda \) has algebraic multiplicity \( 1 \).

(b) Suppose \( \lambda \notin \nR \). By @thm-real-matrix-complex-eigenvalues, \( \conj{\lambda} \ne \lambda \) is also an eigenvalue of \( \A \). The center \( a_{ii} \) is real, so \( \lvert \conj{\lambda} - a_{ii}\rvert = \lvert \conj{\lambda - a_{ii}}\rvert = \lvert \lambda - a_{ii}\rvert \le r_i(\A) \), and \( \conj{\lambda} \in D_i(\A) \) too. Then \( D_i(\A) \) contains two distinct eigenvalues, contradicting (a). So \( \lambda \) is real, and a real number within \( r_i(\A) \) of \( a_{ii} \) lies in the stated interval.
:::

Scaling (@prp-gershgorin-scaling) and counting work together. Scaling moves the radii around without changing the eigenvalues, and a disc that scaling manages to isolate then holds exactly one eigenvalue.

::: {#exm-gershgorin-isolate-real-eigenvalue}
[Isolating a real eigenvalue by scaling]

Let
\[
\A = \begin{pmatrix} 7 & 3 & -1 \\ 0 & -1 & -3 \\ 1 & 1 & 1 \end{pmatrix} .
\]
Show that \( \A \) has exactly one eigenvalue \( \lambda \) with \( \lvert \lambda - 7\rvert \le 2 \), and that it is real.
:::

::: {.solution}
*The unscaled discs do not decide it.* The row radii are \( r_1 = 4 \), \( r_2 = 3 \), \( r_3 = 2 \), so the discs are \( \lvert z - 7\rvert \le 4 \), \( \lvert z + 1\rvert \le 3 \) and \( \lvert z - 1\rvert \le 2 \). The first and the third meet at \( z = 3 \), since \( 7 - 1 = 4 + 2 \). So no disc is isolated, and @thm-gershgorin-counting does not apply.

*Scale.* Take \( \D = \diag(2, 1, 1) \). By @prp-gershgorin-scaling, \( \D^{-1}\A\D \) has the same eigenvalues as \( \A \), and its \( (i, j) \) entry is \( a_{ij}d_j/d_i \):
\[
\D^{-1}\A\D = \begin{pmatrix} 7 & 3/2 & -1/2 \\ 0 & -1 & -3 \\ 2 & 1 & 1 \end{pmatrix} .
\]
Its discs are \( \lvert z - 7\rvert \le 2 \), \( \lvert z + 1\rvert \le 3 \) and \( \lvert z - 1\rvert \le 3 \). The first is disjoint from the other two, because \( 7 - (-1) = 8 > 2 + 3 \) and \( 7 - 1 = 6 > 2 + 3 \).

*Count.* By @cor-isolated-gershgorin-disc, applied to the real matrix \( \D^{-1}\A\D \), the disc \( \lvert z - 7\rvert \le 2 \) contains exactly one eigenvalue, it is simple and real, and it lies in \( [5, 9] \). The other two eigenvalues lie in \( \lvert z + 1\rvert \le 3 \) or \( \lvert z - 1\rvert \le 3 \), outside \( [5, 9] \).

*A check by hand.* Expanding along the first column, \( p_{\A}(x) = x^3 - 7x^2 + 3x - 4 \). Then \( p_{\A}(5) = -39 < 0 \) and \( p_{\A}(9) = 185 > 0 \), consistent with a real root in \( (5, 9) \). (It is about \( 6.64 \). The other two roots are the non-real pair \( 0.18 \pm 0.75i \), approximately, so here Gershgorin has isolated the only real eigenvalue.)
:::

::: {.check}
A real \( 3 \times 3 \) matrix has three pairwise disjoint Gershgorin discs. What can you say about its eigenvalues, and is it diagonalizable?
:::

::: {.solution}
By @cor-isolated-gershgorin-disc, each disc contains exactly one eigenvalue, which is real. The discs are disjoint, so the three eigenvalues are distinct and real, and the matrix is diagonalizable over \( \nR \) by @cor-distinct-eigenvalues-diagonalizable.
:::

::: {.warning}
**The count is for the union, not for each disc in it.** Take \( \A = \begin{psmallmatrix} 0 & 1 & 0 \\ 4 & 0 & 0 \\ 0 & 0 & 10 \end{psmallmatrix} \). Its discs are \( \lvert z\rvert \le 1 \), \( \lvert z\rvert \le 4 \) and the single point \( \{10\} \). The union of the first two is disjoint from the third, and it does contain two eigenvalues, \( \pm 2 \). But both lie in the second disc, and the first disc contains none. Inside a cluster of overlapping discs, the counting theorem says nothing about the individual discs.
:::

## From one-sided to matched

Elsner's bound is **one-sided**. It says that every eigenvalue of \( \B \) is near **some** eigenvalue of \( \A \), and it does not forbid two eigenvalues of \( \B \) from crowding near the same eigenvalue of \( \A \) while another eigenvalue of \( \A \) is left alone. The counting lemma turns it into a statement about a **numbering**. The price is a factor that grows with \( n \).

::: {#thm-elsner-matching}
[Elsner's Matching Bound]

Let \( \A, \B \in M_n(\nC) \) have eigenvalues \( \lambda_1, \dots, \lambda_n \) and \( \mu_1, \dots, \mu_n \), and put
\[
R = \bigl(\norm{\A}_2 + \norm{\B}_2\bigr)^{1 - 1/n}\,\norm{\A - \B}_2^{1/n} .
\]
Then the \( \mu_i \) can be numbered so that \( \lvert \lambda_i - \mu_i\rvert \le (2n - 1)R \) for every \( i \).
:::

::: {.idea}
Slide from \( \A \) to \( \B \) along a segment. By @thm-elsner-spectral-variation, every matrix on the way has its eigenvalues in the discs of radius \( R \) about the \( \lambda_i \). Group those discs into clusters that do not touch one another. By @lem-eigenvalue-count-constant a cluster built from \( m \) of the \( \lambda_i \) holds exactly \( m \) eigenvalues of \( \B \), so we can pair within clusters. A cluster of \( m \) discs has diameter at most \( 2mR \), which gives the factor \( 2n - 1 \).
:::

::: {.proof}
The conclusion is symmetric in \( \A \) and \( \B \), and so is \( R \), so we may assume \( \norm{\A}_2 \le \norm{\B}_2 \). For \( t \in [0, 1] \) put \( \A(t) = (1 - t)\A + t\B \). Then \( \norm{\A(t)}_2 \le (1 - t)\norm{\A}_2 + t\norm{\B}_2 \le \norm{\B}_2 \) and \( \norm{\A - \A(t)}_2 = t\norm{\A - \B}_2 \le \norm{\A - \B}_2 \). By @thm-elsner-spectral-variation applied to \( \A \) and \( \A(t) \), and since the exponents \( 1 - 1/n \) and \( 1/n \) are non-negative, every eigenvalue of \( \A(t) \) lies within \( R \) of some \( \lambda_i \).

*Clusters.* Call indices \( i \) and \( j \) **linked** if \( \lvert \lambda_i - \lambda_j\rvert \le 2R \), and put two indices in the same **cluster** if a chain of links joins them. The clusters partition \( \{1, \dots, n\} \). For a cluster \( C \) let \( K_C \) be the set of \( z \) with \( \lvert z - \lambda_i\rvert \le R \) for some \( i \in C \), and let \( L_C \) be the union of the \( K_{C'} \) for the other clusters \( C' \). If \( i \in C \) and \( j \notin C \), then \( i \) and \( j \) are not linked, so for \( z \) within \( R \) of \( \lambda_i \) and \( w \) within \( R \) of \( \lambda_j \),
\[
\lvert z - w\rvert \ge \lvert \lambda_i - \lambda_j\rvert - 2R > 0 .
\]
Taking the minimum over the finitely many such pairs, \( K_C \) and \( L_C \) are at positive distance; and if \( C \) is the only cluster, \( L_C \) is empty, there is no pair to check, and the requirement holds with any \( d > 0 \). Every eigenvalue of every \( \A(t) \) lies in \( K_C \cup L_C \).

*Counting.* At \( t = 0 \) the eigenvalues are the \( \lambda_j \). Those with \( j \in C \) lie in \( K_C \), and the others lie in \( L_C \), hence not in \( K_C \); so \( \A(0) \) has exactly \( \lvert C\rvert \) eigenvalues in \( K_C \). By @lem-eigenvalue-count-constant, so does \( \A(1) = \B \). Each \( \mu \) lies in exactly one \( K_C \), since the \( K_C \) are pairwise disjoint and cover every eigenvalue. So we may number the \( \mu \)'s so that, for each cluster \( C \), those in \( K_C \) receive the indices in \( C \).

*Distances.* Let \( i \in C \), with \( m = \lvert C\rvert \). Since \( \mu_i \in K_C \), there is \( j \in C \) with \( \lvert \mu_i - \lambda_j\rvert \le R \). A chain of links from \( j \) to \( i \) inside \( C \) can be chosen without repeating an index, so it has at most \( m - 1 \) links, each of length at most \( 2R \), and \( \lvert \lambda_j - \lambda_i\rvert \le 2(m - 1)R \). Hence
\[
\lvert \mu_i - \lambda_i\rvert \le R + 2(m - 1)R = (2m - 1)R \le (2n - 1)R .
\]
This proves the theorem.
:::

The factor \( 2n - 1 \) is not the best possible, and bounds with a factor independent of \( n \) are known; we will not need them. What matters is the shape: a matching distance of order \( \norm{\A - \B}^{1/n} \), with no hypothesis on either matrix. Sections 4 and 5 replace the exponent \( 1/n \) by \( 1 \), and the price is a hypothesis on \( \A \): diagonalizable in Section 4, and normal in Section 5.

## Exercises

### A. Check your understanding

:::: {#exr-continuity-of-roots-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State @thm-roots-continuous, including both hypotheses on \( q \).
2. Which imported fact of analysis does the proof of @thm-roots-continuous use, and at which step? Which one does @lem-eigenvalue-count-constant use?
3. True or false: if \( \norm{\B - \A}_2 \le 10^{-8} \), then every eigenvalue of \( \B \) lies within \( 10^{-8} \) of an eigenvalue of \( \A \). Justify your answer.
4. True or false: if \( \A \in M_3(\nC) \) and \( D_1(\A) \cup D_2(\A) \) is disjoint from \( D_3(\A) \), then \( D_1(\A) \) contains exactly one eigenvalue. Justify your answer.
5. What is the difference between the conclusions of @thm-elsner-spectral-variation and @thm-elsner-matching?
:::
::::

::: {.solution}
(a) See @thm-roots-continuous. The polynomial \( q \) must be **monic** and of the **same degree** \( n \) as \( p \).

(b) Compactness, fact (A3), supplies a convergent subsequence of the bounded root vectors \( \vnu^{(k)} \). The lemma uses the intermediate value theorem, fact (A5), to show that a locally constant integer-valued function on \( [0, 1] \) is constant.

(c) False. Take \( \A = \J_2(0) \) and \( \B = \J_2(0) + 10^{-8}\e_2\e_1\tp \), so \( \norm{\B - \A}_2 = 10^{-8} \). By @exm-jordan-root-perturbation with \( n = 2 \), the eigenvalues of \( \B \) are \( \pm 10^{-4} \), at distance \( 10^{-4} \) from the only eigenvalue \( 0 \) of \( \A \).

(d) False. In the warning after @cor-isolated-gershgorin-disc, \( D_1 \cup D_2 \) is disjoint from \( D_3 = \{10\} \), yet \( D_1 = \{\lvert z\rvert \le 1\} \) contains neither eigenvalue \( \pm 2 \). The counting theorem counts in the union.

(e) The first is one-sided: every eigenvalue of \( \B \) is within \( R \) of **some** eigenvalue of \( \A \), and several may be near the same one. The second gives a **numbering** pairing each \( \mu_i \) with its own \( \lambda_i \), within \( (2n - 1)R \).
:::

### B. Practice

:::: {#exr-continuity-of-roots-b1}
[B1: Cauchy's bound]

Let \( p(x) = x^3 - 3x^2 + 4x - 12 \).

::: {.enumerate options="label=(\alph*)"}
1. Use @lem-cauchy-root-bound to bound the moduli of the roots of \( p \).
2. Find the roots exactly, and compare.
:::
::::

::: {.solution}
(a) Here \( M = \max\{3, 4, 12\} = 12 \), so every root has \( \lvert z\rvert \le 13 \).

(b) \( p(x) = x^2(x - 3) + 4(x - 3) = (x - 3)(x^2 + 4) \), so the roots are \( 3 \) and \( \pm 2i \), of moduli \( 3 \) and \( 2 \). The bound \( 13 \) is true but crude, because the constant term \( 12 \) dominates \( M \).
:::

:::: {#exr-continuity-of-roots-b2}
[B2: Counting with discs]

Let
\[
\A = \begin{pmatrix} 10 & 1 & -1 \\ 1 & 2 & 2 \\ 0 & -2 & 1 \end{pmatrix} .
\]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \A \) has exactly one eigenvalue \( \lambda_1 \) with \( \lvert \lambda_1 - 10\rvert \le 2 \), and that it is real.
2. Explain why the Gershgorin discs cannot decide whether the other two eigenvalues are real.
3. Use the trace to locate the sum of the other two eigenvalues in an interval.
:::
::::

::: {.solution}
(a) The row radii are \( r_1 = 2 \), \( r_2 = 3 \), \( r_3 = 2 \), so the discs are \( \lvert z - 10\rvert \le 2 \), \( \lvert z - 2\rvert \le 3 \) and \( \lvert z - 1\rvert \le 2 \). The first is disjoint from the other two, since \( 10 - 2 = 8 > 2 + 3 \) and \( 10 - 1 = 9 > 2 + 2 \). By @cor-isolated-gershgorin-disc, it contains exactly one eigenvalue, which is simple, real, and in \( [8, 12] \).

(b) The other two eigenvalues lie in \( \{\lvert z - 2\rvert \le 3\} \cup \{\lvert z - 1\rvert \le 2\} \), a union of two overlapping discs that contains both real and non-real points. The counting theorem only says that this union holds two eigenvalues. A conjugate pair and two real numbers are both consistent with that. (In fact they are the non-real pair \( 1.43 \pm 1.99i \), approximately.)

(c) By @cor-trace-sum-eigenvalues-again, \( \lambda_1 + \lambda_2 + \lambda_3 = \tr\A = 13 \). Since \( 8 \le \lambda_1 \le 12 \), the sum \( \lambda_2 + \lambda_3 = 13 - \lambda_1 \) is real and lies in \( [1, 5] \).
:::

### C. Going deeper

:::: {#exr-continuity-of-roots-c1}
[C1: Stability is an open condition]

::: {.enumerate options="label=(\alph*)"}
1. Let \( p \) be monic of degree \( n \) with every root in the open disc \( \{\lvert z\rvert < 1\} \). Prove that there is \( \delta > 0 \) such that every monic \( q \) of degree \( n \) whose coefficients are within \( \delta \) of those of \( p \) also has every root in \( \{\lvert z\rvert < 1\} \).
2. Deduce that the set of \( \A \in M_n(\nC) \) with \( \rho(\A) < 1 \) is **open**: for each such \( \A \) there is \( \eta > 0 \) with \( \rho(\B) < 1 \) whenever \( \norm{\B - \A}_2 < \eta \).
:::
::::

::: {.solution}
(a) Let \( \mu_1, \dots, \mu_n \) be the roots of \( p \) and put \( \varepsilon = 1 - \max_i\lvert \mu_i\rvert \), which is positive since there are finitely many roots, each of modulus less than \( 1 \). Let \( \delta \) be given by @thm-roots-continuous for this \( \varepsilon \). If \( q \) is within \( \delta \), number its roots so that \( \lvert \nu_i - \mu_i\rvert < \varepsilon \). Then \( \lvert \nu_i\rvert < \lvert \mu_i\rvert + \varepsilon \le 1 \) for every \( i \).

(b) Let \( \rho(\A) < 1 \), so every root of \( p_{\A} \) lies in \( \{\lvert z\rvert < 1\} \) (@def-spectral-radius). Take \( \delta \) from (a) for \( p = p_{\A} \). The coefficients of \( p_{\B} \) are polynomials in the entries of \( \B \), as noted after @lem-entrywise-polynomial-continuous, so that lemma gives \( \eta > 0 \) such that \( \norm{\B - \A}_2 < \eta \) makes every coefficient of \( p_{\B} \) within \( \delta \) of the corresponding coefficient of \( p_{\A} \). For such \( \B \), (a) puts every eigenvalue of \( \B \) in the open unit disc, and \( \rho(\B) < 1 \) because there are finitely many of them.
:::

:::: {#exr-continuity-of-roots-c2}
[C2: Why one-sided bounds do not give a matching]

For lists \( (\lambda_1, \dots, \lambda_n) \) and \( (\mu_1, \dots, \mu_n) \) of complex numbers and \( r \ge 0 \), say that the list of \( \mu \)'s is **\( r \)-close to** the list of \( \lambda \)'s if every \( \mu_j \) is within \( r \) of some \( \lambda_i \).

::: {.enumerate options="label=(\alph*)"}
1. Let \( n = 2 \). Prove that if each list is \( r \)-close to the other, then the \( \mu_j \) can be numbered so that \( \lvert \lambda_i - \mu_i\rvert \le r \) for \( i = 1, 2 \).
2. Show that (a) fails for \( n = 3 \): give two lists of length \( 3 \), each \( 0 \)-close to the other, such that every numbering has \( \max_i\lvert \lambda_i - \mu_i\rvert = 2 \).
3. Explain why the proof of @thm-elsner-matching needs @lem-eigenvalue-count-constant, and cannot simply apply @thm-elsner-spectral-variation twice, once in each direction.
:::
::::

::: {.solution}
(a) By hypothesis, \( \lambda_2 \) is within \( r \) of some \( \mu_j \); number the \( \mu \)'s so that this one is \( \mu_2 \), so \( \lvert \lambda_2 - \mu_2\rvert \le r \). The other one, \( \mu_1 \), is within \( r \) of \( \lambda_1 \) or of \( \lambda_2 \). If of \( \lambda_1 \), we are done. If not, then \( \lvert \mu_1 - \lambda_2\rvert \le r \) and \( \lvert \mu_1 - \lambda_1\rvert > r \). Now \( \lambda_1 \) is within \( r \) of some \( \mu_j \), and not of \( \mu_1 \), so \( \lvert \lambda_1 - \mu_2\rvert \le r \). Renumber by swapping \( \mu_1 \) and \( \mu_2 \). Then \( \lvert \lambda_1 - \mu_1\rvert \le r \) and \( \lvert \lambda_2 - \mu_2\rvert \le r \).

(b) Take \( (\lambda_1, \lambda_2, \lambda_3) = (0, 2, 2) \) and \( (\mu_1, \mu_2, \mu_3) = (0, 0, 2) \). Every entry of each list occurs in the other, so each is \( 0 \)-close to the other. But the \( \mu \)'s contain \( 0 \) twice and the \( \lambda \)'s only once, so every numbering pairs some \( \mu_i = 0 \) with some \( \lambda_i = 2 \), and \( \max_i\lvert \lambda_i - \mu_i\rvert = 2 \).

(c) Applying @thm-elsner-spectral-variation to \( (\A, \B) \) and to \( (\B, \A) \) gives exactly the two-sided closeness of (a) with \( r = R \), since \( R \) is symmetric in \( \A \) and \( \B \). By (b), two-sided closeness does not produce a numbering once \( n \ge 3 \), because it ignores multiplicities. The counting lemma supplies the missing information: each cluster of discs holds as many eigenvalues of \( \B \), counted with multiplicity, as it holds eigenvalues of \( \A \).
:::

:::: {#exr-continuity-of-roots-c3}
[C3: Sharpening Cauchy's bound by rescaling]

Let \( n \ge 1 \), let \( p(x) = x^n + c_{n-1}x^{n-1} + \dots + c_1x + c_0 \in \nC[x] \) be monic, and let \( s > 0 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( q(y) \coloneqq p(sy)/s^{n} \) is monic of degree \( n \), with coefficients \( c_j/s^{\,n-j} \), and that \( z \) is a root of \( p \) if and only if \( z/s \) is a root of \( q \). Hence deduce that every root \( z \) of \( p \) satisfies
\[
\lvert z\rvert \le s\Bigl(1 + \max_{0 \le j \le n-1}\frac{\lvert c_j\rvert}{s^{\,n-j}}\Bigr) .
\]
2. Apply (a) with \( s = 3 \) to \( p(x) = x^3 - 3x^2 + 4x - 12 \), and compare the bound with the one @lem-cauchy-root-bound gives directly and with the roots found in @exr-continuity-of-roots-b1.
:::
::::

::: {.solution}
(a) Substituting \( x = sy \) and dividing by \( s^{n} > 0 \),
\[
q(y) = \frac{p(sy)}{s^{n}} = \frac{s^{n}y^{n} + \sum_{j<n}c_js^{j}y^{j}}{s^{n}} = y^{n} + \sum_{j<n}\frac{c_j}{s^{\,n-j}}\,y^{j} ,
\]
which is monic of degree \( n \) with the stated coefficients. Since \( s^{n} \ne 0 \), the identity \( q(z/s) = p(z)/s^{n} \) shows that \( q(z/s) = 0 \) if and only if \( p(z) = 0 \). Now let \( z \) be a root of \( p \). Then \( z/s \) is a root of \( q \), so by @lem-cauchy-root-bound applied to \( q \), whose coefficient maximum is \( M_s = \max_j\lvert c_j\rvert/s^{\,n-j} \), we get \( \lvert z\rvert/s = \lvert z/s\rvert \le 1 + M_s \). Multiplying by \( s > 0 \) gives the bound.

(b) For \( s = 3 \) the coefficients of \( q \) are \( -3/3 = -1 \), \( 4/9 \) and \( -12/27 = -4/9 \), so \( M_3 = 1 \) and every root of \( p \) has \( \lvert z\rvert \le 3(1 + 1) = 6 \). Applied to \( p \) itself, @lem-cauchy-root-bound gives only \( \lvert z\rvert \le 13 \), as in @exr-continuity-of-roots-b1 (a). The true moduli are \( 3 \) and \( 2 \), so the rescaled bound is closer, and the trade-off is visible in the formula: enlarging \( s \) shrinks every \( \lvert c_j\rvert/s^{\,n-j} \) but multiplies the whole bound by \( s \).
:::
