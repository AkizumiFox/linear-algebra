# Other Inclusion Regions

The Gershgorin discs of §01 come from one row of \( \A\x = \lambda\x \), read at the largest coordinate of \( \x \). That leaves two kinds of information unused. The first is the second largest coordinate, which the triangle inequality simply replaced by the largest; using it gives a region of ovals that is never worse than the discs. The second is the geometry of the inner product, which the discs ignore entirely: the number \( \x^{*}\A\x \) over unit vectors \( \x \) fills a region of the plane, the numerical range, that contains every eigenvalue. This section builds both regions. Its main theorem is that the numerical range is always convex. It ends with a rectangle for the spectrum whose sides are eigenvalues of Hermitian matrices, and with a warning about what these regions cannot do.

**Throughout, matrices are complex and \( n \ge 1 \),** and \( \norm{\cdot} \) on \( \nC^n \) is the Euclidean norm. As in §01, \( r_i(\A) = \sum_{j \ne i}\lvert a_{ij}\rvert \) is the \( i \)-th Gershgorin radius and \( D_i(\A) \) the \( i \)-th disc (@def-gershgorin-discs). The plane \( \nC \) is treated as a real vector space when convexity is discussed, as Chapter 17 §01 does.

## Using two coordinates: Brauer's ovals

In the proof of @thm-gershgorin every \( \lvert x_j\rvert \) with \( j \ne k \) was bounded by the largest one, \( \lvert x_k\rvert \). That is wasteful when the second largest coordinate is much smaller. So keep two indices: \( p \), where \( \lvert x_p\rvert \) is largest, and \( q \ne p \), where it is largest among the rest. Row \( p \) bounds \( \lvert\lambda - a_{pp}\rvert\lvert x_p\rvert \) by \( r_p\lvert x_q\rvert \), since every other coordinate is at most \( \lvert x_q\rvert \). Row \( q \) bounds \( \lvert\lambda - a_{qq}\rvert\lvert x_q\rvert \) by \( r_q\lvert x_p\rvert \). Multiplying the two bounds cancels the unknown coordinates. The result is a region defined by a product of distances.

::: {#thm-brauer-ovals}
[Brauer's Ovals of Cassini]

Let \( n \ge 2 \) and \( \A \in M_n(\nC) \). For \( i \ne j \) put
\[
O_{ij}(\A) \coloneqq \bigl\{\, z \in \nC : \lvert z - a_{ii}\rvert\,\lvert z - a_{jj}\rvert \le r_i(\A)\,r_j(\A) \,\bigr\} .
\]

::: {.enumerate options="label=(\alph*)"}
1. Every eigenvalue of \( \A \) lies in \( \bigcup_{i \ne j} O_{ij}(\A) \).
2. \( O_{ij}(\A) \subseteq D_i(\A) \cup D_j(\A) \) for every \( i \ne j \). Hence \( \bigcup_{i \ne j}O_{ij}(\A) \subseteq \bigcup_i D_i(\A) \).
:::
:::

::: {.idea}
For (a), take the two largest coordinates of an eigenvector as above and multiply the two row estimates. One case needs separate care: if the second largest coordinate is \( 0 \), there is nothing to divide by, but then \( \x \) is a multiple of \( \e_p \) and \( \lambda = a_{pp} \), which lies in every oval through \( a_{pp} \). For (b), a point outside both discs is farther than \( r_i \) from \( a_{ii} \) and farther than \( r_j \) from \( a_{jj} \), so the product of its distances exceeds \( r_ir_j \).
:::

::: {.proof}
(a) Let \( \A\x = \lambda\x \) with \( \x \ne \0 \). Choose \( p \) with \( \lvert x_p\rvert = \max_j\lvert x_j\rvert \), which is positive, and then \( q \ne p \) with \( \lvert x_q\rvert = \max_{j \ne p}\lvert x_j\rvert \); this is possible because \( n \ge 2 \).

*Case 1: \( x_q = 0 \).* Then \( x_j = 0 \) for every \( j \ne p \), and row \( p \) of \( \A\x = \lambda\x \) reads \( a_{pp}x_p = \lambda x_p \). As \( x_p \ne 0 \), \( \lambda = a_{pp} \). The left side of the inequality defining \( O_{pq}(\A) \) is then \( 0 \), and the right side is \( \ge 0 \), so \( \lambda \in O_{pq}(\A) \).

*Case 2: \( x_q \ne 0 \).* Row \( p \) gives \( (\lambda - a_{pp})x_p = \sum_{j \ne p}a_{pj}x_j \). Every \( j \ne p \) has \( \lvert x_j\rvert \le \lvert x_q\rvert \), so by the triangle inequality (@thm-complex-triangle-inequality)
\[
\lvert\lambda - a_{pp}\rvert\,\lvert x_p\rvert \le r_p(\A)\,\lvert x_q\rvert .
\]
Row \( q \) gives \( (\lambda - a_{qq})x_q = \sum_{j \ne q}a_{qj}x_j \). Every \( j \) has \( \lvert x_j\rvert \le \lvert x_p\rvert \), so
\[
\lvert\lambda - a_{qq}\rvert\,\lvert x_q\rvert \le r_q(\A)\,\lvert x_p\rvert .
\]
Both sides of both inequalities are non-negative, so they may be multiplied:
\[
\lvert\lambda - a_{pp}\rvert\,\lvert\lambda - a_{qq}\rvert\,\lvert x_p\rvert\,\lvert x_q\rvert
\le r_p(\A)\,r_q(\A)\,\lvert x_p\rvert\,\lvert x_q\rvert .
\]
Dividing by \( \lvert x_p\rvert\lvert x_q\rvert > 0 \) gives \( \lambda \in O_{pq}(\A) \).

(b) Let \( z \notin D_i(\A) \cup D_j(\A) \), so \( a \coloneqq \lvert z - a_{ii}\rvert > r_i(\A) \ge 0 \) and \( c \coloneqq \lvert z - a_{jj}\rvert > r_j(\A) \ge 0 \). Since \( c > 0 \) and \( r_i(\A) \ge 0 \),
\[
ac > r_i(\A)\,c \ge r_i(\A)\,r_j(\A) ,
\]
so \( z \notin O_{ij}(\A) \). Taking complements, \( O_{ij}(\A) \subseteq D_i(\A) \cup D_j(\A) \), and taking the union over all pairs gives the last claim. This proves the theorem.
:::

The sets \( O_{ij}(\A) \) are the **ovals of Cassini**: the points whose distances to two fixed foci have product at most a constant. Since \( O_{ij}(\A) = O_{ji}(\A) \), there are \( n(n-1)/2 \) of them to draw, against \( n \) discs. The hypothesis \( n \ge 2 \) is there because an oval needs two distinct indices; for \( n = 1 \) there are none, and the eigenvalue \( a_{11} \) must be found some other way. For \( n = 2 \) the single oval is as good as a region can be. The eigenvalues satisfy \( (\lambda - a_{11})(\lambda - a_{22}) = a_{12}a_{21} \), so taking moduli, \( \lvert\lambda - a_{11}\rvert\lvert\lambda - a_{22}\rvert = r_1r_2 \): both eigenvalues lie on the boundary curve of \( O_{12} \).

::: {#exm-brauer-invertible}
[Ovals where discs fail]

Let \( \A = \begin{pmatrix} 4 & 1 & 0 \\ 0 & 4 & 1 \\ 1 & 1 & 1 \end{pmatrix} \). Show that the Gershgorin discs cannot prove \( \A \) invertible, and that the ovals can.
:::

::: {.solution}
The radii are \( r_1 = 1 \), \( r_2 = 1 \), \( r_3 = 2 \), and \( D_3(\A) = \{\lvert z - 1\rvert \le 2\} \) contains \( 0 \). So @thm-gershgorin (a) allows the eigenvalue \( 0 \). The column radii are \( 1, 2, 1 \), and the second column disc \( \lvert z - 4\rvert \le 2 \) misses \( 0 \), but the third, \( \lvert z - 1\rvert \le 1 \), contains it. So the discs cannot decide.

Now test \( z = 0 \) against the three ovals:
\[
\begin{aligned}
O_{12}&: \ \lvert 0 - 4\rvert\,\lvert 0 - 4\rvert = 16 > 1 = r_1r_2 ,\\
O_{13}&: \ \lvert 0 - 4\rvert\,\lvert 0 - 1\rvert = 4 > 2 = r_1r_3 ,\\
O_{23}&: \ \lvert 0 - 4\rvert\,\lvert 0 - 1\rvert = 4 > 2 = r_2r_3 .
\end{aligned}
\]
So \( 0 \) lies in no oval, it is not an eigenvalue by @thm-brauer-ovals (a), and \( \A \) is invertible by @thm-eigenvalue-characterizations. Indeed, expanding along the first row, \( \det\A = 4(4 - 1) - 1(0 - 1) = 13 \). The ovals also exclude the point \( -1 \), which lies on the boundary of \( D_3(\A) \): there \( \lvert -1 - 4\rvert\,\lvert -1 - 4\rvert = 25 > 1 \) rules out \( O_{12} \), and \( \lvert -1 - 4\rvert\,\lvert -1 - 1\rvert = 10 > 2 \) rules out \( O_{13} \) and \( O_{23} \).
:::

The same test gives a criterion in the spirit of @cor-diagonally-dominant-invertible: if \( n \ge 2 \), as in @thm-brauer-ovals, and \( \lvert a_{ii}\rvert\,\lvert a_{jj}\rvert > r_i(\A)\,r_j(\A) \) for **every** pair \( i \ne j \), then \( 0 \) lies in no oval and \( \A \) is invertible. One row may fail to dominate, as row \( 3 \) did above, provided every other row dominates enough to compensate.

::: {.check}
Why does the proof of @thm-brauer-ovals (a) choose \( q \) to maximize \( \lvert x_q\rvert \) among the indices other than \( p \), rather than taking any \( q \ne p \)?
:::

::: {.solution}
The estimate from row \( p \) bounds every \( \lvert x_j\rvert \), \( j \ne p \), by \( \lvert x_q\rvert \). That is true only if \( \lvert x_q\rvert \) is the largest of them. With an arbitrary \( q \) the row-\( p \) estimate could fail, and the product of the two estimates would no longer cancel down to \( r_pr_q \).
:::

## The numerical range

Now a different source of information. For a Hermitian \( \A \), Chapter 16 §01 studied the Rayleigh quotient, and @prp-rayleigh-basic showed that its values \( \x^{*}\A\x \) on unit vectors fill exactly the interval \( [\lambda_n(\A), \lambda_1(\A)] \), which contains every eigenvalue. The number \( \x^{*}\A\x = \inner{\A\x}{\x} \) makes sense for every square matrix. Without the Hermitian hypothesis it is complex, and its values fill a region of the plane rather than an interval.

*The numerical range is the set of all values \( \x^{*}\A\x \) as \( \x \) runs over the unit vectors.*

::: {#def-numerical-range}
[Numerical Range]

Let \( \A \in M_n(\nC) \). The **numerical range** of \( \A \) is the subset of \( \nC \)
\[
W(\A) \coloneqq \{\, \x^{*}\A\x : \x \in \nC^n,\ \norm{\x} = 1 \,\} .
\]
:::

In words: feed \( \A \) a vector of length **exactly** \( 1 \), take the inner product of the output with the input, and collect all the complex numbers that arise. The vectors range over **complex** unit vectors, even when \( \A \) is real, and the conjugate in \( \x^{*} \) is part of the definition. \( W(\A) \) is always non-empty, since \( \e_1 \) is a unit vector, and \( \e_i^{*}\A\e_i = a_{ii} \), so every diagonal entry lies in \( W(\A) \). The notation always carries its argument: \( W(\A) \), never \( W \) alone, since \( W \) also names subspaces.

Examples, simplest first.

- **\( n = 1 \), and scalar matrices.** For \( \A = (a) \) the unit vectors are the scalars \( x \) with \( \lvert x\rvert = 1 \), and \( \conj{x}ax = a\lvert x\rvert^2 = a \). So \( W((a)) = \{a\} \). Likewise \( W(c\I) = \{c\} \), since \( \x^{*}(c\I)\x = c\norm{\x}^2 = c \).
- **Diagonal matrices.** For \( \A = \diag(d_1, \dots, d_n) \), \( \x^{*}\A\x = \sum_i d_i\lvert x_i\rvert^2 \). The weights \( t_i = \lvert x_i\rvert^2 \) are non-negative with sum \( \norm{\x}^2 = 1 \), and every such list of weights arises, from \( x_i = \sqrt{t_i} \). So \( W(\A) \) is the set of all weighted averages of \( d_1, \dots, d_n \), which is \( \conv\{d_1, \dots, d_n\} \) by @thm-convex-hull-combinations. For \( \diag(1, i, -1) \) it is the filled triangle with these three vertices.
- **Hermitian matrices.** By @prp-rayleigh-basic, \( W(\A) = [\lambda_n(\A), \lambda_1(\A)] \), a segment of the real axis.
- **A Jordan block.** The next example computes \( W(\J_2(0)) \), and it is a whole disc, although the only eigenvalue is \( 0 \).

::: {#exm-numerical-range-jordan}
[The numerical range of a Jordan block]

Show that \( W(\J_2(0)) = \{ z \in \nC : \lvert z\rvert \le \tfrac12 \} \).
:::

::: {.solution}
Write \( \x = (x_1, x_2) \) with \( \lvert x_1\rvert^2 + \lvert x_2\rvert^2 = 1 \). Then \( \J_2(0)\x = (x_2, 0) \), so \( \x^{*}\J_2(0)\x = \conj{x_1}\,x_2 \).

\( (\subseteq) \) Since \( 0 \le (\lvert x_1\rvert - \lvert x_2\rvert)^2 = 1 - 2\lvert x_1\rvert\lvert x_2\rvert \), we get \( \lvert\conj{x_1}x_2\rvert = \lvert x_1\rvert\lvert x_2\rvert \le \tfrac12 \).

\( (\supseteq) \) Let \( z = \rho\,\omega \) with \( 0 \le \rho \le \tfrac12 \) and \( \lvert\omega\rvert = 1 \). Since \( 1 - 4\rho^2 \ge 0 \), we may put
\[
a = \sqrt{\tfrac{1 + \sqrt{1 - 4\rho^2}}{2}}, \qquad b = \sqrt{\tfrac{1 - \sqrt{1 - 4\rho^2}}{2}} ,
\]
both real and non-negative. Then \( a^2 + b^2 = 1 \) and \( a^2b^2 = \tfrac14\bigl(1 - (1 - 4\rho^2)\bigr) = \rho^2 \), so \( ab = \rho \). The unit vector \( \x = (a, b\,\omega) \) gives \( \x^{*}\J_2(0)\x = a\,b\,\omega = z \). Hence \( W(\J_2(0)) \) is the closed disc of radius \( \tfrac12 \) about \( 0 \).
:::

**Non-example by minimal change.** Drop the conjugate, and collect the numbers \( \x\tp\A\x \) for unit \( \x \) instead. For \( \A = \I_2 \) and the unit vector \( \x = \tfrac{1}{\sqrt2}(1, i) \), \( \x\tp\I_2\x = \tfrac12(1 + i^2) = 0 \), while \( \x^{*}\I_2\x = 1 \). The modified set for \( \I_2 \) contains \( 0 \), which is not an eigenvalue, while \( W(\I_2) = \{1\} \) is exactly the spectrum. What breaks is that \( \x\tp\x \) is not \( \norm{\x}^2 \) over \( \nC \). The conjugate is what makes \( \x^{*}(c\I)\x = c \) on the unit sphere, and every property below leans on that.

**Why this definition.** The unit length plays the role that division by \( \norm{\x}^2 \) played for the Rayleigh quotient. Without it the values \( \x^{*}\A\x \) over all \( \x \) form a set closed under multiplication by positive reals, which is all of \( \nC \) or a cone, and records nothing about the size of \( \A \). With it, the set is bounded, and the eigenvalues are in it.

::: {#prp-numerical-range-basic}
[Basic Properties of the Numerical Range]

Let \( \A \in M_n(\nC) \).

::: {.enumerate options="label=(\alph*)"}
1. \( \spec(\A) \subseteq W(\A) \).
2. \( W(\alpha\A + \beta\I) = \alpha W(\A) + \beta \coloneqq \{\alpha w + \beta : w \in W(\A)\} \) for all \( \alpha, \beta \in \nC \).
3. \( W(\U^{*}\A\U) = W(\A) \) for every unitary \( \U \in M_n(\nC) \).
4. \( W(\A) \) is compact: every sequence in \( W(\A) \) has a subsequence converging to a point of \( W(\A) \). In particular \( W(\A) \) is closed.
5. \( W(\A) \subseteq \{ z : \lvert z\rvert \le \norm{\A}_2 \} \).
:::
:::

::: {.idea}
Four of the five parts are one line of algebra with a unit vector: evaluate at a unit eigenvector for (a), push the scalars or the unitary through \( \x^{*}(\cdot)\x \) for (b) and (c), and apply Cauchy–Schwarz for (e). Only (d) needs analysis, and there the point is that \( W(\A) \) is the image of the unit sphere under a continuous map, so the compactness of the sphere passes to it.
:::

::: {.proof}
(a) Let \( \lambda \in \spec(\A) \), with eigenvector \( \v \). Then \( \x = \v/\norm{\v} \) is a unit eigenvector, and \( \x^{*}\A\x = \lambda\,\x^{*}\x = \lambda \).

(b) For a unit \( \x \), \( \x^{*}(\alpha\A + \beta\I)\x = \alpha\,\x^{*}\A\x + \beta\,\x^{*}\x = \alpha\,\x^{*}\A\x + \beta \). As \( \x \) runs over the unit vectors, the left side runs over \( W(\alpha\A + \beta\I) \) and the right side over \( \alpha W(\A) + \beta \).

(c) For a unit \( \x \), \( \x^{*}\U^{*}\A\U\x = (\U\x)^{*}\A(\U\x) \), and \( \U\x \) is a unit vector because \( \U \) is an isometry (@thm-isometry-characterizations). So \( W(\U^{*}\A\U) \subseteq W(\A) \). Conversely, every unit \( \y \) equals \( \U\x \) for the unit vector \( \x = \U^{*}\y \), so every value \( \y^{*}\A\y \) arises, and the two sets are equal.

(d) First, \( f(\x) = \x^{*}\A\x \) is continuous on the unit sphere. For unit vectors \( \x, \y \),
\[
\begin{aligned}
\lvert f(\x) - f(\y)\rvert
&= \lvert \x^{*}\A(\x - \y) + (\x - \y)^{*}\A\y \rvert \\
&\le 2\,\norm{\A}_2\,\norm{\x - \y} ,
\end{aligned}
\]
by the triangle inequality (@thm-complex-triangle-inequality), the Cauchy–Schwarz inequality (@thm-cauchy-schwarz) and @thm-operator-norm-properties (a). This is a bound of the kind fixed as the book's continuity test in Chapter 15's introduction. Now let \( (w_k) \) be a sequence in \( W(\A) \), with \( w_k = f(\x_k) \) and \( \norm{\x_k} = 1 \). By **the compactness of the unit sphere, fact (A3) of Chapter 15's introduction**, a subsequence \( (\x_{k_l}) \) converges to a unit vector \( \x \). By continuity, \( w_{k_l} = f(\x_{k_l}) \to f(\x) \in W(\A) \). If \( (w_k) \) itself converges to \( w \), its subsequence converges to \( w \) too, and limits are unique, so \( w = f(\x) \in W(\A) \): the set is closed.

(e) For a unit \( \x \), by the Cauchy–Schwarz inequality and @thm-operator-norm-properties (a), \( \lvert\x^{*}\A\x\rvert = \lvert\inner{\A\x}{\x}\rvert \le \norm{\A\x}\,\norm{\x} \le \norm{\A}_2 \).
:::

Part (a) makes \( W(\A) \) an inclusion region for the spectrum, and (e) puts it inside the disc of radius \( \norm{\A}_2 \), which upgrades \( \rho(\A) \le \norm{\A}_2 \) from the spectrum to the whole numerical range. Part (b) is the tool that lets us move any two points of \( W(\A) \) to \( 0 \) and \( 1 \), and the next proof depends on it. Part (c) says \( W(\A) \) depends only on the operator \( T_{\A} \) and the inner product, not on the orthonormal basis used to write it down.

## Convexity: the Toeplitz–Hausdorff theorem

The examples so far were all convex: a point, a segment, a triangle, a disc. That is not a coincidence. To prove it, split \( \A \) into two Hermitian pieces, the way a complex number splits into its real and imaginary parts.

::: {#lem-hermitian-parts}
[Real and Imaginary Parts of a Matrix]

Let \( \A \in M_n(\nC) \), and put
\[
\H = \frac{\A + \A^{*}}{2}, \qquad \K = \frac{\A - \A^{*}}{2i} .
\]
Then \( \H \) and \( \K \) are Hermitian, \( \A = \H + i\K \), and for every \( \x \in \nC^n \) the numbers \( \x^{*}\H\x \) and \( \x^{*}\K\x \) are real, with
\[
\operatorname{Re}(\x^{*}\A\x) = \x^{*}\H\x, \qquad \operatorname{Im}(\x^{*}\A\x) = \x^{*}\K\x .
\]
:::

::: {.proof}
By @def-conjugate-transpose, \( (\A^{*})^{*} = \A \), \( (\B + \C)^{*} = \B^{*} + \C^{*} \) and \( (c\B)^{*} = \conj{c}\B^{*} \). Hence \( \H^{*} = \tfrac12(\A^{*} + \A) = \H \) and \( \K^{*} = \tfrac{1}{-2i}(\A^{*} - \A) = \tfrac{1}{2i}(\A - \A^{*}) = \K \). Also \( \H + i\K = \tfrac12(\A + \A^{*}) + \tfrac12(\A - \A^{*}) = \A \). For \( \x \in \nC^n \), \( \x^{*}\H\x = \inner{\H\x}{\x} \) is real by @prp-self-adjoint-immediate (a), applied to the self-adjoint operator \( T_{\H} \), and likewise \( \x^{*}\K\x \). So \( \x^{*}\A\x = \x^{*}\H\x + i\,\x^{*}\K\x \) is the splitting of a complex number into real and imaginary parts.
:::

For example \( \J_2(0) \) has \( \H = \tfrac12\begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix} \) and \( \K = \tfrac{1}{2i}\begin{psmallmatrix} 0 & 1 \\ -1 & 0 \end{psmallmatrix} = \tfrac12\begin{psmallmatrix} 0 & -i \\ i & 0 \end{psmallmatrix} \), both with eigenvalues \( \pm\tfrac12 \). A Hermitian \( \A \) has \( \K = 0 \), and then \( W(\A) \) lies on the real axis.

::: {#thm-toeplitz-hausdorff}
[Toeplitz–Hausdorff Theorem]

For every \( \A \in M_n(\nC) \), the numerical range \( W(\A) \) is a convex subset of \( \nC \).
:::

::: {.idea}
**Step roadmap.** ① By @prp-numerical-range-basic (b), an affine change \( z \mapsto \alpha z + \beta \) carries any two points of \( W(\A) \) to \( 0 \) and \( 1 \), and carries segments to segments; so it suffices to show that \( [0, 1] \subseteq W(\B) \) whenever \( 0, 1 \in W(\B) \). ② Take unit vectors \( \x \), \( \y \) with \( \x^{*}\B\x = 0 \) and \( \y^{*}\B\y = 1 \), and walk from \( \x \) to \( \y \) along the straight path \( (1 - t)\x + t\y \). Along the way the value of \( \B \), normalized, moves continuously from \( 0 \) to \( 1 \), but it may wander off the real axis. ③ Its imaginary part along the path is \( \K \) evaluated there, and expanding shows that only the cross term \( \x^{*}\K\y + \y^{*}\K\x = 2\operatorname{Re}(\x^{*}\K\y) \) can be non-zero. Multiplying \( \y \) by a unimodular scalar rotates \( \x^{*}\K\y \) freely without changing \( \y^{*}\B\y \), so we rotate it onto the imaginary axis, where its real part is \( 0 \). ④ Then the path stays on the real axis, and the intermediate value theorem fills in \( [0, 1] \).
:::

::: {.proof}
**Step 1: reduction.** Let \( w_0, w_1 \in W(\A) \) and \( 0 \le s \le 1 \); we must show \( (1 - s)w_0 + sw_1 \in W(\A) \). If \( w_0 = w_1 \) there is nothing to prove. Otherwise put \( \alpha = 1/(w_1 - w_0) \), \( \beta = -\alpha w_0 \) and \( \B = \alpha\A + \beta\I \). By @prp-numerical-range-basic (b), \( W(\B) = \alpha W(\A) + \beta \), which contains \( \alpha w_0 + \beta = 0 \) and \( \alpha w_1 + \beta = 1 \). Suppose we show \( s \in W(\B) \). Then \( s = \alpha w + \beta \) for some \( w \in W(\A) \), and solving, \( w = w_0 + s(w_1 - w_0) = (1 - s)w_0 + sw_1 \). So it suffices to prove: **if \( 0, 1 \in W(\B) \), then \( [0, 1] \subseteq W(\B) \).**

**Step 2: choosing the vectors.** Let \( \B = \H + i\K \) as in @lem-hermitian-parts, and choose unit vectors \( \x \), \( \y_0 \) with \( \x^{*}\B\x = 0 \) and \( \y_0^{*}\B\y_0 = 1 \). By @lem-hermitian-parts, \( \x^{*}\H\x = \x^{*}\K\x = 0 \), \( \y_0^{*}\H\y_0 = 1 \) and \( \y_0^{*}\K\y_0 = 0 \). Let \( c = \x^{*}\K\y_0 \), and put \( \gamma = 1 \) if \( c = 0 \), and \( \gamma = i\conj{c}/\lvert c\rvert \) otherwise. In both cases \( \lvert\gamma\rvert = 1 \) and \( \gamma c = i\lvert c\rvert \) is purely imaginary. Set \( \y = \gamma\y_0 \). Then \( \norm{\y} = 1 \) and \( \y^{*}\B\y = \lvert\gamma\rvert^2\,\y_0^{*}\B\y_0 = 1 \), so still \( \y^{*}\H\y = 1 \) and \( \y^{*}\K\y = 0 \). Since \( \K \) is Hermitian, \( \y^{*}\K\x = (\x^{*}\K\y)^{*} = \conj{\x^{*}\K\y} \), and so
\[
\x^{*}\K\y + \y^{*}\K\x = 2\operatorname{Re}(\x^{*}\K\y) = 2\operatorname{Re}(\gamma c) = 0 .
\]
Finally, \( \x \) and \( \y \) are linearly independent. Otherwise, both being non-zero, \( \y = \mu\x \) for a scalar \( \mu \), and then \( 1 = \y^{*}\B\y = \lvert\mu\rvert^2\,\x^{*}\B\x = 0 \), which is absurd.

**Step 3: the path stays real.** For \( t \in [0, 1] \) put \( \v(t) = (1 - t)\x + t\y \). The coefficients \( 1 - t \) and \( t \) are not both zero, so \( \v(t) \ne \0 \) by independence. Expanding, and using \( \x^{*}\K\x = \y^{*}\K\y = 0 \) and Step 2,
\[
\v(t)^{*}\K\v(t) = (1 - t)^2\,\x^{*}\K\x + t^2\,\y^{*}\K\y + t(1 - t)\bigl(\x^{*}\K\y + \y^{*}\K\x\bigr) = 0 .
\]
So \( \v(t)^{*}\B\v(t) = \v(t)^{*}\H\v(t) \) is real for every \( t \). The same expansion with \( \H \) in place of \( \K \), and with \( \norm{\v(t)}^2 = \v(t)^{*}\v(t) \), gives
\[
\begin{aligned}
\v(t)^{*}\H\v(t) &= t^2 + 2t(1 - t)\operatorname{Re}(\x^{*}\H\y) ,\\
\norm{\v(t)}^2 &= (1 - t)^2 + t^2 + 2t(1 - t)\operatorname{Re}(\x^{*}\y) ,
\end{aligned}
\]
two polynomials in \( t \) with real coefficients, the second positive on \( [0, 1] \).

**Step 4: filling the segment.** The function
\[
f(t) = \frac{\v(t)^{*}\H\v(t)}{\norm{\v(t)}^2}, \qquad 0 \le t \le 1 ,
\]
is a quotient of polynomials with a denominator that never vanishes, hence continuous by the algebra of limits, and \( f(0) = \x^{*}\H\x = 0 \), \( f(1) = \y^{*}\H\y = 1 \). Let \( s \in [0, 1] \). By **the intermediate value theorem, fact (A5) of Chapter 15's introduction**, there is \( t_s \in [0, 1] \) with \( f(t_s) = s \). The vector \( \u = \v(t_s)/\norm{\v(t_s)} \) is a unit vector, and by Step 3,
\[
\u^{*}\B\u = \frac{\v(t_s)^{*}\B\v(t_s)}{\norm{\v(t_s)}^2} = \frac{\v(t_s)^{*}\H\v(t_s)}{\norm{\v(t_s)}^2} = f(t_s) = s .
\]
So \( s \in W(\B) \). By Step 1, \( W(\A) \) contains the segment between any two of its points, which is @def-convex-set. This proves the theorem.
:::

The phase choice in Step 2 is the heart of the proof. Without it the imaginary part along the path is \( 2t(1 - t)\operatorname{Re}(\x^{*}\K\y_0)/\norm{\v(t)}^2 \), which may be non-zero, and the path would leave the real axis between \( 0 \) and \( 1 \). The rotated vector \( \gamma\y_0 \) spans the same line as \( \y_0 \) and gives the same value of \( \B \), so the rotation costs nothing. Only the path between \( \x \) and \( \y \) changes.

With convexity, \( W(\A) \) contains the convex hull of \( \spec(\A) \), by (a) and @def-convex-hull, and it contains the diagonal entries, so it contains \( \conv\{a_{11}, \dots, a_{nn}\} \) as well.

## Normal matrices

For a diagonal matrix the numerical range is the convex hull of the diagonal entries, and those are the eigenvalues. Unitary similarity does not change \( W \), and a normal matrix is unitarily similar to a diagonal one. So for a normal matrix \( W(\A) \) is as small as (a) and convexity allow.

::: {#prp-numerical-range-normal}
[The Numerical Range of a Normal Matrix]

Let \( \A \in M_n(\nC) \) be normal, with eigenvalues \( \lambda_1, \dots, \lambda_n \), listed with multiplicity. Then
\[
W(\A) = \conv\{\lambda_1, \dots, \lambda_n\} .
\]
:::

::: {.idea}
Unitary similarity leaves \( W \) alone, by @prp-numerical-range-basic (c), so we may replace \( \A \) by a diagonal matrix of its eigenvalues. Then \( \x^{*}\A\x \) is the average of the \( \lambda_i \) with weights \( \lvert x_i\rvert^2 \), and the two inclusions say exactly that the lists of admissible weights and of convex coefficients are the same.
:::

::: {.proof}
By @cor-spectral-complex-matrix, \( \A = \U\D\U^{*} \) with \( \U \) unitary and \( \D = \diag(\lambda_1, \dots, \lambda_n) \). So \( \U^{*}\A\U = \D \), and \( W(\A) = W(\D) \) by @prp-numerical-range-basic (c). For a unit \( \x \), \( \x^{*}\D\x = \sum_i\lvert x_i\rvert^2\lambda_i \).

\( (\subseteq) \) The weights \( \lvert x_i\rvert^2 \) are non-negative with sum \( 1 \), so \( \x^{*}\D\x \) is a convex combination of \( \lambda_1, \dots, \lambda_n \), and lies in their convex hull by @thm-convex-hull-combinations.

\( (\supseteq) \) By @thm-convex-hull-combinations, a point of the hull is \( \sum_{k=1}^{m}t_k\mu_k \) with \( t_k \ge 0 \), \( \sum_k t_k = 1 \) and each \( \mu_k \) one of the \( \lambda_i \). Assign each \( k \) to one index \( i \) with \( \lambda_i = \mu_k \), and let \( s_i \) be the sum of the \( t_k \) assigned to \( i \). Then \( s_i \ge 0 \), \( \sum_i s_i = 1 \), and the point is \( \sum_i s_i\lambda_i \). The unit vector with \( x_i = \sqrt{s_i} \) gives \( \x^{*}\D\x = \sum_i s_i\lambda_i \).
:::

For a Hermitian matrix this recovers @prp-rayleigh-basic. For a unitary matrix, whose eigenvalues lie on the unit circle, \( W(\A) \) is the convex hull of those eigenvalues: a polygon inscribed in the circle when three or more of them are distinct, and a chord or a single point when there are two or one. For a non-normal matrix \( W(\A) \) can be much larger than \( \conv\spec(\A) \): by @exm-numerical-range-jordan, \( W(\J_2(0)) \) is a disc of radius \( \tfrac12 \) around the single eigenvalue \( 0 \). The extra room is a measure of non-normality, and Exercise C3 turns it into a comparison with \( \norm{\A}_2 \).

::: {.check}
Find \( W(\A) \) for the rotation \( \A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \), regarded as a complex matrix.
:::

::: {.solution}
\( \A\tp\A = \I \), so \( \A \) is real orthogonal, hence unitary and normal. Its characteristic polynomial is \( x^2 + 1 \), with roots \( \pm i \). By @prp-numerical-range-normal, \( W(\A) \) is the segment from \( -i \) to \( i \) on the imaginary axis. For real unit vectors \( \x \) the value \( \x^{*}\A\x \) is \( 0 \), which is why the real Rayleigh-type quotient of Chapter 16 §01 saw nothing; the complex unit vectors fill in the rest.
:::

## Bendixson's rectangle

By @lem-hermitian-parts, the real part of \( \x^{*}\A\x \) is a value of the Hermitian form of \( \H \), and @prp-rayleigh-basic confines those values to \( [\lambda_n(\H), \lambda_1(\H)] \). The same holds for the imaginary part and \( \K \). Together they box in the whole numerical range, hence the spectrum.

::: {#thm-bendixson}
[Bendixson's Theorem]

Let \( \A \in M_n(\nC) \), with \( \H = (\A + \A^{*})/2 \) and \( \K = (\A - \A^{*})/(2i) \). Every \( w \in W(\A) \) satisfies
\[
\begin{aligned}
\lambda_n(\H) &\le \operatorname{Re}w \le \lambda_1(\H) ,\\
\lambda_n(\K) &\le \operatorname{Im}w \le \lambda_1(\K) .
\end{aligned}
\]
In particular every eigenvalue \( \lambda \) of \( \A \) satisfies the same inequalities with \( \lambda \) in place of \( w \).
:::

::: {.proof}
Let \( w = \x^{*}\A\x \) with \( \norm{\x} = 1 \). By @lem-hermitian-parts, \( \operatorname{Re}w = \x^{*}\H\x = \inner{\H\x}{\x} \) and \( \operatorname{Im}w = \x^{*}\K\x \), and \( \H \), \( \K \) are Hermitian. By @lem-extreme-eigenvalues-quadratic-form, \( \lambda_n(\H) \le \inner{\H\x}{\x} \le \lambda_1(\H) \), and likewise for \( \K \). Every eigenvalue lies in \( W(\A) \) by @prp-numerical-range-basic (a).
:::

The most used consequence concerns the sign of the real parts. If \( \A + \A^{*} \succ 0 \), then \( \lambda_n(\H) > 0 \), so every eigenvalue of \( \A \) has positive real part, and in particular \( \A \) is invertible. This needs nothing about the size of the off-diagonal entries, only about their symmetric part.

::: {#exm-bendixson}
[A rectangle beats the discs]

Let \( \A = \begin{pmatrix} 3 & 2 \\ -4 & 1 \end{pmatrix} \). Show that every eigenvalue of \( \A \) has positive real part, using @thm-bendixson, and check that the Gershgorin discs cannot show it. Compare with the eigenvalues.
:::

::: {.solution}
Here \( \A^{*} = \A\tp \), so
\[
\H = \begin{pmatrix} 3 & -1 \\ -1 & 1 \end{pmatrix}, \qquad
\K = \frac{1}{2i}\begin{pmatrix} 0 & 6 \\ -6 & 0 \end{pmatrix} = \begin{pmatrix} 0 & -3i \\ 3i & 0 \end{pmatrix} .
\]
\( \H \) has trace \( 4 \) and determinant \( 2 \), so \( p_{\H}(x) = x^2 - 4x + 2 \), with roots \( 2 \pm \sqrt2 \). \( \K \) has trace \( 0 \) and determinant \( 0 - (-3i)(3i) = -9 \), so its eigenvalues are \( \pm 3 \). By @thm-bendixson, every eigenvalue lies in the rectangle
\[
2 - \sqrt2 \le \operatorname{Re}\lambda \le 2 + \sqrt2, \qquad -3 \le \operatorname{Im}\lambda \le 3 ,
\]
and in particular \( \operatorname{Re}\lambda \ge 2 - \sqrt2 > 0 \).

The row discs are \( \lvert z - 3\rvert \le 2 \) and \( \lvert z - 1\rvert \le 4 \), and the second contains \( -3 \). The column discs are \( \lvert z - 3\rvert \le 4 \) and \( \lvert z - 1\rvert \le 2 \), and the first contains \( -1 \). So neither union rules out an eigenvalue with negative real part.

Directly, \( p_{\A}(x) = x^2 - 4x + 11 \), so \( \lambda = 2 \pm i\sqrt7 \). The real part \( 2 \) lies in \( [2 - \sqrt2, 2 + \sqrt2] \), and the imaginary parts \( \pm\sqrt7 \approx \pm 2.65 \) lie in \( [-3, 3] \).
:::

## What these regions do not do

Every region in this section and the last is an **inclusion region**: it contains the spectrum. None of them is a perturbation bound in the sense of the rest of this chapter, which asks how far the eigenvalues move when \( \A \) changes by a small \( \E \). The numerical range does give a statement of that kind. For a unit \( \x \), \( \x^{*}(\A + \E)\x = \x^{*}\A\x + \x^{*}\E\x \), and \( \lvert\x^{*}\E\x\rvert \le \norm{\E}_2 \) by @prp-numerical-range-basic (e). Hence
\[
W(\A + \E) \subseteq W(\A) + W(\E) \subseteq \{\, w + e : w \in W(\A),\ \lvert e\rvert \le \norm{\E}_2 \,\} ,
\]
and so every eigenvalue of \( \A + \E \) lies within \( \norm{\E}_2 \) of \( W(\A) \). This is only as good as \( W(\A) \) is small.

::: {.warning}
**\( W(\A) \) can be far larger than \( \spec(\A) \), so "within \( \norm{\E}_2 \) of \( W(\A) \)" is not "within \( \norm{\E}_2 \) of an eigenvalue".** For \( \A = M\J_2(0) \) with \( M > 0 \), @prp-numerical-range-basic (b) and @exm-numerical-range-jordan give \( W(\A) = \{\lvert z\rvert \le M/2\} \), while \( \spec(\A) = \{0\} \). So the bound above allows the eigenvalues of \( \A + \E \) to lie anywhere in \( \lvert z\rvert \le M/2 + \norm{\E}_2 \), and this does not shrink as \( \E \to 0 \). The eigenvalues do move a long way: \( \A + \varepsilon\e_2\e_1\tp \) has characteristic polynomial \( x^2 - M\varepsilon \), so for \( \varepsilon > 0 \) its eigenvalues \( \pm\sqrt{M\varepsilon} \) have moved by \( \sqrt{M\varepsilon} \), far more than \( \varepsilon \). For a normal \( \A \), \( W(\A) = \conv\spec(\A) \) is small, but it still contains points far from every eigenvalue, such as the midpoint of two distant ones.
:::

The genuine perturbation bounds need a different mechanism: §03 proves that eigenvalues move continuously and at what rate in general, and §04 gives Bauer–Fike's bound, in which the distance to the nearest **eigenvalue** is controlled.

## Exercises

### A. Check your understanding

:::: {#exr-inclusion-regions-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the Brauer oval \( O_{ij}(\A) \) and the numerical range \( W(\A) \), and state the Toeplitz–Hausdorff theorem.
2. True or false: \( W(\A) = \conv\spec(\A) \) for every \( \A \in M_n(\nC) \). Justify your answer.
3. True or false: \( W(\A) \) is contained in the union of the Gershgorin discs of \( \A \). Justify your answer.
4. True or false: if \( \A + \A^{*} \succ 0 \), then \( \A \) is invertible. Justify your answer.
5. Why does @thm-brauer-ovals require \( n \ge 2 \)?
:::
::::

::: {.solution}
(a) For \( i \ne j \), \( O_{ij}(\A) = \{z : \lvert z - a_{ii}\rvert\lvert z - a_{jj}\rvert \le r_i(\A)r_j(\A)\} \), and \( W(\A) = \{\x^{*}\A\x : \norm{\x} = 1\} \). @thm-toeplitz-hausdorff: for every square complex \( \A \), \( W(\A) \) is convex.

(b) False. \( W(\J_2(0)) \) is the disc \( \lvert z\rvert \le \tfrac12 \) (@exm-numerical-range-jordan), while \( \conv\spec(\J_2(0)) = \{0\} \). Equality holds for normal matrices (@prp-numerical-range-normal).

(c) False. For \( \A = \diag(1, -1) \) the discs are the two points \( \{1\} \) and \( \{-1\} \), while \( W(\A) = [-1, 1] \) contains \( 0 \). The discs contain the spectrum, not the numerical range.

(d) True. By @thm-bendixson every eigenvalue has \( \operatorname{Re}\lambda \ge \lambda_n(\H) > 0 \), with \( \H = (\A + \A^{*})/2 \succ 0 \). So \( 0 \) is not an eigenvalue, and \( \A \) is invertible (@thm-eigenvalue-characterizations).

(e) An oval is built from two distinct indices \( i \ne j \), and the proof needs a second index \( q \ne p \). For \( n = 1 \) there are no ovals, and the union in (a) would be empty, although the matrix has an eigenvalue.
:::

### B. Practice

:::: {#exr-inclusion-regions-b1}
[B1: Invertibility from ovals]

Let \( \A = \begin{pmatrix} 5 & 1 & 1 \\ 1 & 5 & 1 \\ 2 & 2 & 2 \end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Show that neither the row discs nor the column discs of \( \A \) exclude \( 0 \).
2. Use @thm-brauer-ovals to show that \( \A \) is invertible.
3. Check that \( (1, -1, 0) \) is an eigenvector, and verify that its eigenvalue lies in \( O_{12}(\A) \).
:::
::::

::: {.solution}
(a) The row radii are \( 2, 2, 4 \), and \( D_3(\A) = \{\lvert z - 2\rvert \le 4\} \) contains \( 0 \). The column radii are \( 3, 3, 2 \), and the third column disc \( \lvert z - 2\rvert \le 2 \) contains \( 0 \).

(b) At \( z = 0 \): for \( O_{12} \), \( 5 \cdot 5 = 25 > 4 = r_1r_2 \); for \( O_{13} \) and \( O_{23} \), \( 5 \cdot 2 = 10 > 8 = r_1r_3 = r_2r_3 \). So \( 0 \) lies in no oval, is not an eigenvalue by @thm-brauer-ovals (a), and \( \A \) is invertible. (Its determinant is \( 32 \).)

(c) \( \A(1, -1, 0) = (5 - 1, 1 - 5, 2 - 2) = (4, -4, 0) \), so the eigenvalue is \( 4 \). For \( O_{12} \): \( \lvert 4 - 5\rvert\lvert 4 - 5\rvert = 1 \le 4 \).
:::

:::: {#exr-inclusion-regions-b2}
[B2: A Bendixson rectangle]

Let \( \A = \begin{pmatrix} 1 & 3 \\ -1 & 1 \end{pmatrix} \). Find the rectangle of @thm-bendixson, and hence show that every eigenvalue of \( \A \) satisfies \( 0 \le \operatorname{Re}\lambda \le 2 \) and \( \lvert\operatorname{Im}\lambda\rvert \le 2 \). Compare with the eigenvalues.
::::

::: {.solution}
\( \H = \tfrac12(\A + \A\tp) = \begin{psmallmatrix} 1 & 1 \\ 1 & 1 \end{psmallmatrix} \), with \( p_{\H}(x) = x^2 - 2x \), so its eigenvalues are \( 0 \) and \( 2 \). \( \K = \tfrac{1}{2i}(\A - \A\tp) = \tfrac{1}{2i}\begin{psmallmatrix} 0 & 4 \\ -4 & 0 \end{psmallmatrix} = \begin{psmallmatrix} 0 & -2i \\ 2i & 0 \end{psmallmatrix} \), with trace \( 0 \) and determinant \( -4 \), so its eigenvalues are \( \pm 2 \). By @thm-bendixson every eigenvalue has \( 0 \le \operatorname{Re}\lambda \le 2 \) and \( -2 \le \operatorname{Im}\lambda \le 2 \). Directly, \( p_{\A}(x) = x^2 - 2x + 4 \), so \( \lambda = 1 \pm i\sqrt3 \): the real part \( 1 \) lies in \( [0, 2] \), and \( \sqrt3 \approx 1.73 \le 2 \).
:::

:::: {#exr-inclusion-regions-b3}
[B3: Computing numerical ranges]

Determine \( W(\A) \) for each matrix. Justify your answers.

::: {.enumerate options="label=(\alph*)"}
1. \( \A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \)
2. \( \A = \diag(1, i, -1, -i) \)
3. \( \A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \)
:::
::::

::: {.solution}
(a) \( \A = 2\J_2(0) + \I \), so by @prp-numerical-range-basic (b) and @exm-numerical-range-jordan, \( W(\A) = 2W(\J_2(0)) + 1 = \{z : \lvert z - 1\rvert \le 1\} \), the closed disc of radius \( 1 \) about \( 1 \).

(b) A diagonal matrix is normal, so by @prp-numerical-range-normal \( W(\A) = \conv\{1, i, -1, -i\} \), the filled square with these four vertices.

(c) \( \A \) is real symmetric, with eigenvalues \( 3 \) and \( 1 \) (eigenvectors \( (1, 1) \) and \( (1, -1) \)). By @prp-rayleigh-basic, or @prp-numerical-range-normal, \( W(\A) = [1, 3] \).
:::

### C. Going deeper

:::: {#exr-inclusion-regions-c1}
[C1: Direct sums]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \B \in M_k(\nC) \) and \( \C \in M_m(\nC) \). Prove that \( W(\B \oplus \C) = \conv\bigl(W(\B) \cup W(\C)\bigr) \).
2. Deduce that \( \A = \diag(2, -2, 2i, -2i) \oplus \J_2(0) \) is not normal, but satisfies \( W(\A) = \conv\spec(\A) \).
:::

*Hint for (a): one inclusion needs @thm-toeplitz-hausdorff.*
::::

::: {.solution}
(a) \( (\subseteq) \) Write a unit vector of \( \nC^{k+m} \) as \( \x = (\y, \z) \), with \( \norm{\y}^2 + \norm{\z}^2 = 1 \). Then \( \x^{*}(\B \oplus \C)\x = \y^{*}\B\y + \z^{*}\C\z \). If \( \z = \0 \) this is a point of \( W(\B) \), and if \( \y = \0 \) a point of \( W(\C) \). Otherwise, with \( s = \norm{\y}^2 \in (0, 1) \),
\[
\x^{*}(\B \oplus \C)\x = s\,\frac{\y^{*}\B\y}{\norm{\y}^2} + (1 - s)\,\frac{\z^{*}\C\z}{\norm{\z}^2} ,
\]
a convex combination of a point of \( W(\B) \), at the unit vector \( \y/\norm{\y} \), and a point of \( W(\C) \). In every case the value lies in \( \conv(W(\B) \cup W(\C)) \), by @thm-convex-hull-combinations.

\( (\supseteq) \) Taking \( \x = (\y, \0) \) with \( \y \) a unit vector shows \( W(\B) \subseteq W(\B \oplus \C) \), and likewise \( W(\C) \subseteq W(\B \oplus \C) \). By @thm-toeplitz-hausdorff, \( W(\B \oplus \C) \) is convex, so it contains the smallest convex set containing \( W(\B) \cup W(\C) \) (@def-convex-hull).

(b) \( \A \) is not normal: its lower-right block is \( \J_2(0) \), and \( \A^{*}\A \) and \( \A\A^{*} \) differ in that block, since \( \J_2(0)^{*}\J_2(0) = \diag(0, 1) \) and \( \J_2(0)\J_2(0)^{*} = \diag(1, 0) \). By (a), @prp-numerical-range-normal and @exm-numerical-range-jordan, \( W(\A) \) is the convex hull of the square \( Q = \conv\{\pm 2, \pm 2i\} \) and the disc \( \{\lvert z\rvert \le \tfrac12\} \). The square contains the disc: \( Q = \{ z : \lvert\operatorname{Re}z\rvert + \lvert\operatorname{Im}z\rvert \le 2 \} \), and \( \lvert\operatorname{Re}z\rvert + \lvert\operatorname{Im}z\rvert \le 2\lvert z\rvert \le 1 \) on the disc. So \( W(\A) = Q \). The spectrum is \( \{\pm 2, \pm 2i, 0\} \), whose hull is also \( Q \), since \( 0 \in Q \). Hence \( W(\A) = \conv\spec(\A) \), although \( \A \) is not normal: the converse of @prp-numerical-range-normal fails.
:::

:::: {#exr-inclusion-regions-c2}
[C2: When the numerical range is real, or a point]

Let \( \A \in M_n(\nC) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( W(\A) \subseteq \nR \) if and only if \( \A \) is Hermitian.
2. Deduce that \( W(\A) = \{c\} \) for a single \( c \in \nC \) if and only if \( \A = c\I \).
:::
::::

::: {.solution}
(a) \( (\Leftarrow) \) If \( \A \) is Hermitian, \( \x^{*}\A\x = \inner{\A\x}{\x} \) is real by @prp-self-adjoint-immediate (a). \( (\Rightarrow) \) Write \( \A = \H + i\K \) as in @lem-hermitian-parts. If \( W(\A) \subseteq \nR \), then \( \x^{*}\K\x = \operatorname{Im}(\x^{*}\A\x) = 0 \) for every unit \( \x \). By @prp-rayleigh-basic, \( \lambda_1(\K) \) and \( \lambda_n(\K) \) are values of \( \x^{*}\K\x \) on unit vectors, so both are \( 0 \), and every eigenvalue of \( \K \) is \( 0 \). By @cor-spectral-complex-matrix, \( \K = \U\,0\,\U^{*} = 0 \). Hence \( \A = \H \) is Hermitian.

(b) \( (\Leftarrow) \) is the example \( W(c\I) = \{c\} \). \( (\Rightarrow) \) By @prp-numerical-range-basic (b), \( W(\A - c\I) = W(\A) - c = \{0\} \subseteq \nR \), so \( \A - c\I \) is Hermitian by (a). By @prp-rayleigh-basic its extreme eigenvalues are values of the form on unit vectors, hence both \( 0 \), and as in (a) the Hermitian matrix \( \A - c\I \) with all eigenvalues \( 0 \) is \( 0 \).
:::

:::: {#exr-inclusion-regions-c3}
[C3: The numerical radius]

For \( \A \in M_n(\nC) \), the **numerical radius** is \( w(\A) = \max\{\lvert z\rvert : z \in W(\A)\} \).

::: {.enumerate options="label=(\alph*)"}
1. Explain why the maximum exists, and prove that \( \rho(\A) \le w(\A) \le \norm{\A}_2 \).
2. Prove that \( \norm{\A}_2 \le 2\,w(\A) \).
3. Show that both constants are attained: \( w(\A) = \norm{\A}_2 \) for every normal \( \A \), and \( \norm{\A}_2 = 2\,w(\A) \) for \( \A = \J_2(0) \).
:::

*Hint for (b): bound \( \norm{\H}_2 \) and \( \norm{\K}_2 \) separately.*
::::

::: {.solution}
(a) \( W(\A) \) is non-empty and compact (@prp-numerical-range-basic (d)), and \( z \mapsto \lvert z\rvert \) is continuous, so the maximum is attained by **the extreme value theorem, fact (A4) of Chapter 15's introduction**. Every eigenvalue lies in \( W(\A) \), by @prp-numerical-range-basic (a), so \( \rho(\A) \le w(\A) \); and \( w(\A) \le \norm{\A}_2 \) by @prp-numerical-range-basic (e).

(b) Let \( \A = \H + i\K \) as in @lem-hermitian-parts. By @lem-hermitian-spectral-norm, \( \norm{\H}_2 \) is the larger of \( \lambda_1(\H) \) and \( -\lambda_n(\H) \). By @prp-rayleigh-basic there is a unit \( \x \) with
\[
\lambda_1(\H) = \x^{*}\H\x = \operatorname{Re}(\x^{*}\A\x) \le \lvert\x^{*}\A\x\rvert \le w(\A) ,
\]
and a unit \( \y \) with \( -\lambda_n(\H) = -\operatorname{Re}(\y^{*}\A\y) \le w(\A) \). So \( \norm{\H}_2 \le w(\A) \), and the same argument with imaginary parts gives \( \norm{\K}_2 \le w(\A) \). As the operator norm is a norm (@thm-operator-norm-properties (b)), \( \norm{\A}_2 \le \norm{\H}_2 + \norm{i\K}_2 \le 2\,w(\A) \).

(c) For normal \( \A \), \( \rho(\A) = \norm{\A}_2 \), as Chapter 15 §04 showed after @def-spectral-radius, so the chain in (a) collapses to equalities. For \( \J_2(0) \), @exm-numerical-range-jordan gives \( w(\J_2(0)) = \tfrac12 \), and \( \norm{\J_2(0)}_2 = 1 \), since \( \norm{\J_2(0)\x} = \lvert x_2\rvert \le \norm{\x} \) with equality at \( \x = \e_2 \). So \( \norm{\J_2(0)}_2 = 2\,w(\J_2(0)) \).
:::
