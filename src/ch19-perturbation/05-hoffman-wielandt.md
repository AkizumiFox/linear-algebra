# The Hoffman–Wielandt Theorem

Section 04 showed that for a normal \( \A \), every eigenvalue of \( \A + \E \) lies within \( \norm{\E}_2 \) of **some** eigenvalue of \( \A \). That answers "how far", one perturbed eigenvalue at a time. It does not answer "which goes where": it never says that the eigenvalues of the two matrices can be **paired off**, each with a partner of its own. This section proves that for two normal matrices they can, with the total squared distance of the pairs bounded by \( \norm{\A - \B}_F^2 \). The proof is short once the right tool is in hand, and the tool is Birkhoff's theorem from Chapter 18 §07. We then sharpen the result for Hermitian matrices, where the pairing is simply the decreasing order, and show that without normality the inequality fails for every pairing.

Throughout, the field is \( \nC \), and eigenvalues are listed **with algebraic multiplicity**. For a Hermitian matrix, \( \lambda_1(\A) \ge \dots \ge \lambda_n(\A) \) is the decreasing list, as in Chapter 16.

## One-sided bounds do not pair eigenvalues

Recall @cor-bauer-fike-normal (a): if \( \A \in M_n(\nC) \) is normal and \( \E \in M_n(\nC) \) is arbitrary, then every eigenvalue \( \mu \) of \( \A + \E \) satisfies \( \min_i\lvert\lambda_i - \mu\rvert \le \norm{\E}_2 \), where \( \lambda_1, \dots, \lambda_n \) are the eigenvalues of \( \A \). The statement starts from a perturbed eigenvalue and finds a partner for it. Nothing in it stops two perturbed eigenvalues from choosing the **same** partner.

Here is the smallest case. Let
\[
\A = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} , \qquad
\A + \E = \begin{pmatrix} \tfrac15 & 0 \\ 0 & \tfrac25 \end{pmatrix} , \qquad
\E = \begin{pmatrix} \tfrac15 & 0 \\ 0 & -\tfrac35 \end{pmatrix} .
\]
Then \( \norm{\E}_2 = \tfrac35 \), and both perturbed eigenvalues are within \( \tfrac35 \) of an eigenvalue of \( \A \), as the corollary promises. But if each one goes to its **nearest** eigenvalue of \( \A \), both go to \( 0 \): the distances are \( \tfrac15 \) and \( \tfrac25 \) to \( 0 \), against \( \tfrac45 \) and \( \tfrac35 \) to \( 1 \). The nearest-eigenvalue map is not a bijection, and the eigenvalue \( 1 \) is left without a partner. A pairing does exist here, \( 0 \leftrightarrow \tfrac15 \) and \( 1 \leftrightarrow \tfrac25 \), with distances \( \tfrac15 \) and \( \tfrac35 \), but finding it was not the corollary's doing.

Why ask for a pairing at all? Because it is what "the eigenvalues move a little" should mean. Chapter 15's @cor-eigenvalues-continuous is a pairing statement: the eigenvalues of a nearby matrix **can be numbered** so that each is close to its counterpart. It gives no rate. For Hermitian matrices, Weyl's @cor-weyl-perturbation gives a pairing with a rate, and the pairing is the decreasing order. For normal matrices with complex eigenvalues there is no decreasing order, and the pairing has to be found.

To say this precisely, let \( \lambda_1, \dots, \lambda_n \) and \( \mu_1, \dots, \mu_n \) be two lists of complex numbers. A **pairing** of them is a permutation \( \sigma \in S_n \), which matches \( \lambda_i \) with \( \mu_{\sigma(i)} \). Its cost, in the sense of this section, is the sum of squared distances
\[
\sum_{i=1}^{n}\lvert\lambda_i - \mu_{\sigma(i)}\rvert^2 .
\]
A one-sided statement, "every \( \mu_j \) is within \( r \) of some \( \lambda_i \)", is a statement about sets. A pairing is a statement about lists with multiplicity, and it is strictly stronger.

::: {.check}
Let \( \A = \diag(0, 0, 1) \) and \( \B = \diag(0, 1, 1) \). Show that every eigenvalue of \( \B \) is an eigenvalue of \( \A \) and conversely, so each one-sided distance is \( 0 \). What is the smallest possible largest distance \( \max_i\lvert\lambda_i - \mu_{\sigma(i)}\rvert \) over all pairings \( \sigma \)?
:::

::: {.solution}
Both matrices have the eigenvalue set \( \{0, 1\} \), so every eigenvalue of either one is at distance \( 0 \) from an eigenvalue of the other. As lists, \( \A \) has \( (0, 0, 1) \) and \( \B \) has \( (0, 1, 1) \). Any pairing must send one of the two \( 0 \)'s of \( \A \) to a \( 1 \) of \( \B \), since \( \B \) has only one \( 0 \). So every pairing has largest distance at least \( 1 \), and the identity pairing attains \( 1 \). Sets that agree can still be far apart as lists.
:::

## Birkhoff turns weights into a permutation

The proof below will produce a sum of the form \( \sum_{i,j}s_{ij}c_{ij} \), in which \( c_{ij} = \lvert\lambda_i - \mu_j\rvert^2 \) is the cost of pairing \( \lambda_i \) with \( \mu_j \), and the weights \( s_{ij} \) form a doubly stochastic matrix. Such a sum is a **fractional pairing**: every \( \lambda_i \) spreads a total weight \( 1 \) over the \( \mu_j \), and every \( \mu_j \) receives a total weight \( 1 \). A genuine pairing is the special case where each weight is \( 0 \) or \( 1 \), that is, where \( (s_{ij}) \) is a permutation matrix. The lemma says that fractional pairings never beat the best genuine one.

Recall @def-doubly-stochastic: \( \S \in M_n(\nR) \) is doubly stochastic if its entries are non-negative and every row and every column adds up to \( 1 \); the set of such matrices is \( \Omega_n \). Recall also @def-permutation-matrix: \( \P_\sigma \) is the matrix whose \( j \)-th column is \( \e_{\sigma(j)} \), so its entry in position \( (\sigma(j), j) \) is \( 1 \) for each \( j \), and all its other entries are \( 0 \).

::: {#lem-doubly-stochastic-linear-min}
[A Fractional Pairing Is Never Cheaper]

Let \( \C = (c_{ij}) \in M_n(\nR) \) and \( \S = (s_{ij}) \in \Omega_n \). Then there is a permutation \( \sigma \in S_n \) with
\[
\sum_{j=1}^{n} c_{\sigma(j)j} \ \le\ \sum_{i,j=1}^{n} s_{ij}c_{ij} .
\]
:::

::: {.idea}
Write \( f(\X) = \sum_{i,j}x_{ij}c_{ij} \), a linear function of \( \X \). Birkhoff's theorem writes \( \S \) as an average of permutation matrices, so \( f(\S) \) is the same average of the numbers \( f(\P_\sigma) \), and an average is at least its smallest term.
:::

::: {.proof}
Let \( f(\X) = \sum_{i,j}x_{ij}c_{ij} \) for \( \X \in M_n(\nR) \); it is linear in \( \X \). By @thm-birkhoff, \( \S = \sum_{k=1}^{m}t_k\P_{\sigma_k} \) for some permutations \( \sigma_1, \dots, \sigma_m \) and weights \( t_k \ge 0 \) with \( \sum_k t_k = 1 \). By linearity,
\[
f(\S) = \sum_{k=1}^{m}t_k\,f(\P_{\sigma_k}) \ \ge\ \Bigl(\sum_{k=1}^{m}t_k\Bigr)\min_{k}f(\P_{\sigma_k}) = \min_{k}f(\P_{\sigma_k}) ,
\]
where the inequality uses \( t_k \ge 0 \). Let \( \sigma \) be a \( \sigma_k \) attaining the minimum. The only non-zero entries of \( \P_\sigma \) are the \( 1 \)'s in positions \( (\sigma(j), j) \), so \( f(\P_\sigma) = \sum_j c_{\sigma(j)j} \). Hence \( \sum_j c_{\sigma(j)j} \le f(\S) \), as claimed.
:::

In the language of Chapter 17, this is @cor-linear-max-at-extreme applied to \( \Omega_n \). With the Frobenius inner product \( \inner{\X}{\C} = \tr(\C\tp\X) = \sum_{i,j}x_{ij}c_{ij} \), the function \( f \) is \( \X \mapsto \inner{\X}{\C} \). The set \( \Omega_n \) is non-empty, compact and convex (Chapter 17 §08), so the minimum of \( f \) over it is attained at an extreme point, and by @thm-birkhoff the extreme points are the permutation matrices. The proof above uses the second form of Birkhoff's theorem instead, so no compactness argument appears in it.

## The theorem

We can now prove that two normal matrices have a pairing of their eigenvalues whose cost is at most the squared Frobenius distance between the matrices.

::: {#thm-hoffman-wielandt}
[Hoffman–Wielandt Theorem]

Let \( \A, \B \in M_n(\nC) \) be **normal**, with eigenvalues \( \lambda_1, \dots, \lambda_n \) and \( \mu_1, \dots, \mu_n \) respectively, each listed with algebraic multiplicity in any order. Then there is a permutation \( \sigma \in S_n \) with
\[
\sum_{i=1}^{n}\bigl\lvert\lambda_i - \mu_{\sigma(i)}\bigr\rvert^2 \ \le\ \norm{\A - \B}_F^2 .
\]
:::

::: {.idea}
**Step roadmap.**

① **Diagonalize both.** The spectral theorem gives \( \A = \U\vLambda\U^{*} \) and \( \B = \V\M\V^{*} \) with \( \U, \V \) unitary and \( \vLambda, \M \) diagonal. The two orthonormal bases of eigenvectors are different, and the unitary \( \W = \U^{*}\V \) records how they sit relative to each other.

② **Compute the distance.** The Frobenius norm does not see unitary factors, so \( \norm{\A - \B}_F = \norm{\vLambda\W - \W\M}_F \). The \( (i,j) \) entry of \( \vLambda\W - \W\M \) is \( (\lambda_i - \mu_j)w_{ij} \), so \( \norm{\A - \B}_F^2 = \sum_{i,j}\lvert w_{ij}\rvert^2\lvert\lambda_i - \mu_j\rvert^2 \). This is a fractional pairing with weights \( \lvert w_{ij}\rvert^2 \).

③ **Round it.** The weights form a doubly stochastic matrix, because the rows and the columns of a unitary matrix are unit vectors. The lemma replaces the fractional pairing by a genuine one that costs no more.
:::

::: {.proof}
By @cor-spectral-complex-matrix, since \( \A \) and \( \B \) are normal, there are unitary \( \U, \V \in \Unit(n) \) with
\[
\A = \U\vLambda\U^{*} , \qquad \B = \V\M\V^{*} ,
\]
where \( \vLambda = \diag(\lambda_1, \dots, \lambda_n) \) and \( \M = \diag(\mu_1, \dots, \mu_n) \) in the given orders. Put \( \W = \U^{*}\V \), which is unitary as a product of unitary matrices. Since \( \U^{*}\U = \I \) and \( \V^{*}\V = \I \),
\[
\U^{*}(\A - \B)\V = \vLambda\U^{*}\V - \U^{*}\V\M = \vLambda\W - \W\M .
\]
By @lem-frobenius-unitarily-invariant, applied with the unitary factors \( \U^{*} \) on the left and \( \V \) on the right, \( \norm{\A - \B}_F = \norm{\vLambda\W - \W\M}_F \). The \( (i,j) \) entry of \( \vLambda\W \) is \( \lambda_iw_{ij} \) and that of \( \W\M \) is \( w_{ij}\mu_j \), since multiplying by a diagonal matrix on the left scales rows and on the right scales columns. Hence
\[
\norm{\A - \B}_F^2 = \sum_{i,j=1}^{n}\lvert w_{ij}\rvert^2\,\lvert\lambda_i - \mu_j\rvert^2 .
\]{#eq-hoffman-wielandt-weights}

Let \( \S = (s_{ij}) \) with \( s_{ij} = \lvert w_{ij}\rvert^2 \). Its entries are non-negative. Row \( i \) adds up to \( \sum_j\lvert w_{ij}\rvert^2 = (\W\W^{*})_{ii} = 1 \), and column \( j \) adds up to \( \sum_i\lvert w_{ij}\rvert^2 = (\W^{*}\W)_{jj} = 1 \), since \( \W \) is unitary. So \( \S \in \Omega_n \). Apply @lem-doubly-stochastic-linear-min to \( \S \) and the real matrix \( \C \) with \( c_{ij} = \lvert\lambda_i - \mu_j\rvert^2 \). It gives \( \tau \in S_n \) with
\[
\sum_{j=1}^{n}\lvert\lambda_{\tau(j)} - \mu_j\rvert^2 \ \le\ \sum_{i,j}s_{ij}c_{ij} = \norm{\A - \B}_F^2 ,
\]
the equality being @eq-hoffman-wielandt-weights. Put \( \sigma = \tau^{-1} \). As \( j \) runs over \( 1, \dots, n \), so does \( i = \tau(j) \), and \( j = \sigma(i) \); so the left-hand side is \( \sum_i\lvert\lambda_i - \mu_{\sigma(i)}\rvert^2 \). This proves the theorem.
:::

Both hypotheses were used in the first line and nowhere else: normality is what makes the diagonalizing matrices unitary. The rest of the proof is bookkeeping and Birkhoff's theorem, which is where Chapter 18 §07's theorem earns its keep.

In words: *the eigenvalues of a normal matrix, as a list with multiplicity, are a \( 1 \)-Lipschitz function of the matrix, when matrices are measured in the Frobenius norm and lists by their best pairing.* In particular every pair in the best pairing is within \( \norm{\A - \B}_F \), so each eigenvalue of \( \B \) has its own partner among those of \( \A \) within that distance. This is a matching bound, with a constant, valid for all normal matrices at once. Compare @cor-eigenvalues-continuous, which gives a matching with no constant for all matrices, and @cor-bauer-fike-normal, which gives a constant with no matching.

The theorem asserts that **some** pairing is cheap. The proof does not say which, beyond what the lemma gives, but the cheapest of the \( n! \) pairings certainly works, since it costs no more than any other. The next example shows that a pairing chosen by any other rule can fail.

::: {#exm-hoffman-wielandt-two-by-two}
[A Hermitian and a diagonal matrix]

Let
\[
\A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} , \qquad
\B = \begin{pmatrix} i & 0 \\ 0 & 2 + i \end{pmatrix} .
\]
Both are normal. Compute \( \norm{\A - \B}_F^2 \), the cost of both pairings of the eigenvalues, and the matrix \( \S \) of the proof. Which pairings satisfy the conclusion of @thm-hoffman-wielandt?
:::

::: {.solution}
\( \A \) is real symmetric, hence Hermitian and normal, and \( \B \) is diagonal, hence normal. The eigenvalues of \( \A \) are \( \lambda_1 = 3 \) and \( \lambda_2 = 1 \), with unit eigenvectors \( \tfrac{1}{\sqrt2}(1, 1) \) and \( \tfrac{1}{\sqrt2}(1, -1) \): indeed \( \A(1,1) = (3,3) \) and \( \A(1,-1) = (1,-1) \). Those of \( \B \) are \( \mu_1 = i \) and \( \mu_2 = 2 + i \), with eigenvectors \( \e_1, \e_2 \).

*The distance.* \( \A - \B = \begin{psmallmatrix} 2 - i & 1 \\ 1 & -i \end{psmallmatrix} \), so
\[
\norm{\A - \B}_F^2 = \lvert 2 - i\rvert^2 + 1 + 1 + \lvert -i\rvert^2 = 5 + 1 + 1 + 1 = 8 .
\]

*The costs.* The four squared distances \( c_{ij} = \lvert\lambda_i - \mu_j\rvert^2 \) are
\[
\begin{aligned}
c_{11} &= \lvert 3 - i\rvert^2 = 10 , \qquad c_{12} = \lvert 1 - i\rvert^2 = 2 , \\
c_{21} &= \lvert 1 - i\rvert^2 = 2 , \qquad c_{22} = \lvert -1 - i\rvert^2 = 2 .
\end{aligned}
\]
The identity pairing \( 3 \leftrightarrow i \), \( 1 \leftrightarrow 2 + i \) costs \( c_{11} + c_{22} = 12 \). The swap \( 3 \leftrightarrow 2 + i \), \( 1 \leftrightarrow i \) costs \( c_{12} + c_{21} = 4 \).

*The weights.* With \( \U = \tfrac{1}{\sqrt2}\begin{psmallmatrix} 1 & 1 \\ 1 & -1 \end{psmallmatrix} \) and \( \V = \I \), \( \W = \U^{*} \), and every entry of \( \W \) has modulus \( \tfrac{1}{\sqrt2} \). So \( \S = \tfrac12\J \), and @eq-hoffman-wielandt-weights reads
\[
\norm{\A - \B}_F^2 = \tfrac12(10 + 2 + 2 + 2) = 8 ,
\]
the average of the two costs, \( \tfrac12(12 + 4) \). An average lies between its terms, so the cheaper pairing, the swap with cost \( 4 \), satisfies \( 4 \le 8 \). The identity pairing, with cost \( 12 > 8 \), does not.
:::

::: {.warning}
**The theorem does not say that the given numbering works.** In the example, the lists \( (3, 1) \) and \( (i, 2 + i) \), paired in the order written, cost \( 12 > 8 = \norm{\A - \B}_F^2 \). Complex numbers have no natural order to sort by, so, unlike the Hermitian case below, there is no rule fixed in advance that always picks a good pairing. The safe reading is: the **cheapest** pairing satisfies the inequality.
:::

## Normality cannot be dropped

The proof used normality once, in its first line, to make the diagonalizing matrices unitary. For diagonalizable matrices \( \A = \X\vLambda\X^{-1} \) and \( \B = \Y\M\Y^{-1} \) with \( \X \), \( \Y \) not unitary, @lem-frobenius-unitarily-invariant no longer applies, and \( \norm{\A - \B}_F \) is no longer the norm of \( \vLambda\W - \W\M \) with \( \W = \X^{-1}\Y \). The failure is real, not an artifact of the proof.

::: {#exm-hoffman-wielandt-fails}
[Every pairing fails]

Let
\[
\A = \begin{pmatrix} 1 & 3 \\ 0 & -1 \end{pmatrix} , \qquad
\B = \begin{pmatrix} 1 & 3 \\ 1 & -1 \end{pmatrix} .
\]
Show that \( \A \) and \( \B \) are diagonalizable but not normal, and that the inequality of @thm-hoffman-wielandt fails for **every** pairing of their eigenvalues.
:::

::: {.solution}
\( \A \) is triangular with eigenvalues \( 1 \) and \( -1 \). The matrix \( \B \) has trace \( 0 \) and determinant \( -1 - 3 = -4 \), so its characteristic polynomial is \( x^2 - 4 \) and its eigenvalues are \( 2 \) and \( -2 \). Each has two distinct eigenvalues, so each is diagonalizable (@thm-diagonalization). Neither is normal:
\[
\begin{aligned}
\A^{*}\A &= \begin{pmatrix} 1 & 3 \\ 3 & 10 \end{pmatrix} \ne \begin{pmatrix} 10 & -3 \\ -3 & 1 \end{pmatrix} = \A\A^{*} , \\
\B^{*}\B &= \begin{pmatrix} 2 & 2 \\ 2 & 10 \end{pmatrix} \ne \begin{pmatrix} 10 & -2 \\ -2 & 2 \end{pmatrix} = \B\B^{*} .
\end{aligned}
\]
The difference \( \A - \B \) has a single non-zero entry, \( -1 \) in position \( (2,1) \), so \( \norm{\A - \B}_F^2 = 1 \).

There are two pairings. The one that matches signs, \( 1 \leftrightarrow 2 \) and \( -1 \leftrightarrow -2 \), costs \( 1^2 + 1^2 = 2 \). The other, \( 1 \leftrightarrow -2 \) and \( -1 \leftrightarrow 2 \), costs \( 3^2 + 3^2 = 18 \). Both exceed \( 1 \), so no pairing satisfies the inequality.
:::

The entry \( 3 \) is what makes this work, and the failure is not confined to a perturbation as large as \( 1 \). Put \( \delta > 0 \) in the corner instead: \( \B_\delta = \begin{psmallmatrix} 1 & 3 \\ \delta & -1 \end{psmallmatrix} \) has determinant \( -1 - 3\delta \) and eigenvalues \( \pm\sqrt{1 + 3\delta} \), each of which moves by \( \sqrt{1 + 3\delta} - 1 \), about \( \tfrac32\delta \) for small \( \delta \). So the cheaper pairing costs about \( 2\bigl(\tfrac32\delta\bigr)^2 = \tfrac92\delta^2 \), well above \( \norm{\A - \B_\delta}_F^2 = \delta^2 \). With an entry \( m \) in place of \( 3 \) the cost is about \( \tfrac12m^2\delta^2 \), so the inequality fails for small \( \delta \) as soon as \( m > \sqrt2 \). A large entry above the diagonal is exactly what Chapter 11 §11 measured as departure from normality, and it is what makes the eigenvalues sensitive.

A Jordan block shows that no constant can repair the inequality. Let \( \A = \J_2(0) \) and, for \( \varepsilon > 0 \), \( \B_\varepsilon = \begin{psmallmatrix} 0 & 1 \\ \varepsilon & 0 \end{psmallmatrix} \). Then \( \A \) has the eigenvalue \( 0 \) twice, \( \B_\varepsilon \) has characteristic polynomial \( x^2 - \varepsilon \) and eigenvalues \( \pm\sqrt\varepsilon \), and \( \norm{\A - \B_\varepsilon}_F^2 = \varepsilon^2 \). Both pairings cost the same, \( (\sqrt\varepsilon)^2 + (\sqrt\varepsilon)^2 = 2\varepsilon \), and
\[
\frac{2\varepsilon}{\varepsilon^2} = \frac{2}{\varepsilon} \longrightarrow \infty \qquad (\varepsilon \to 0^{+}) .
\]
So there is no constant \( K \) with \( \min_\sigma\sum_i\lvert\lambda_i - \mu_{\sigma(i)}\rvert^2 \le K\norm{\A - \B}_F^2 \) for all pairs of matrices. This is @exm-jordan-block-perturbation of Chapter 15 read in the language of pairings: the eigenvalues move like \( \sqrt\varepsilon \) while the matrix moves by \( \varepsilon \).

::: {.warning}
**Diagonalizable is not enough, and one normal matrix is not enough.** In @exm-hoffman-wielandt-fails both matrices are diagonalizable, and every pairing fails. Nor does it help to make just one of the two matrices normal: for \( \A = \J_2(0) \) and the Hermitian \( \B = \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix} \), with eigenvalues \( \pm 1 \), both pairings cost \( 1 + 1 = 2 \), while \( \norm{\A - \B}_F^2 = 1 \). The theorem needs **both** matrices normal.
:::

## Hermitian matrices: the pairing is the order

When both matrices are Hermitian, the eigenvalues are real, and there is a natural guess for the best pairing: largest with largest, second with second, and so on. The guess is right, and the reason is a fact about real numbers alone.

::: {#lem-sorted-pairing}
[The Sorted Pairing Is Cheapest]

Let \( a_1 \ge a_2 \ge \dots \ge a_n \) and \( b_1 \ge b_2 \ge \dots \ge b_n \) be real numbers. Then for every \( \sigma \in S_n \),
\[
\sum_{i=1}^{n}(a_i - b_i)^2 \ \le\ \sum_{i=1}^{n}(a_i - b_{\sigma(i)})^2 .
\]
:::

::: {.idea}
Expanding the squares, \( \sum_i a_i^2 \) and \( \sum_i b_{\sigma(i)}^2 = \sum_j b_j^2 \) do not depend on \( \sigma \), so the claim is that the cross term \( \sum_i a_ib_{\sigma(i)} \) is largest at the identity. If \( \sigma \) puts a smaller \( b \) before a larger one in two neighboring positions, swapping those two values can only increase the cross term, and it removes one inversion. Repeating the swap sorts \( \sigma \) into the identity.
:::

::: {.proof}
For every \( \sigma \), since \( \sigma \) is a bijection, \( \sum_i b_{\sigma(i)}^2 = \sum_j b_j^2 \), and so
\[
\begin{aligned}
\sum_{i=1}^{n}(a_i - b_{\sigma(i)})^2 &= \sum_i a_i^2 + \sum_j b_j^2 - 2g(\sigma) , \\
g(\sigma) &= \sum_{i=1}^{n}a_ib_{\sigma(i)} .
\end{aligned}
\]
It therefore suffices to show \( g(\sigma) \le g(\id) \) for every \( \sigma \). The set \( S_n \) is finite, so \( g \) attains a maximum on it; among the permutations where it does, choose one, \( \sigma \), with the fewest inversions (@def-inversion). Suppose \( \sigma \ne \id \). Then \( \sigma(i) > \sigma(i+1) \) for some \( i \), since a permutation with \( \sigma(1) < \sigma(2) < \dots < \sigma(n) \) is the identity. Let \( \sigma' \) agree with \( \sigma \) except that \( \sigma'(i) = \sigma(i+1) \) and \( \sigma'(i+1) = \sigma(i) \). Then
\[
g(\sigma') - g(\sigma) = (a_i - a_{i+1})\bigl(b_{\sigma(i+1)} - b_{\sigma(i)}\bigr) \ \ge\ 0 ,
\]
because \( a_i \ge a_{i+1} \), and \( \sigma(i+1) < \sigma(i) \) gives \( b_{\sigma(i+1)} \ge b_{\sigma(i)} \). So \( \sigma' \) also maximizes \( g \). Now count inversions. The pair of positions \( (i, i+1) \) is an inversion of \( \sigma \) and not of \( \sigma' \). A pair involving neither \( i \) nor \( i+1 \) sees the same values under both. For a position \( p \notin \{i, i+1\} \), the two pairs joining \( p \) to \( i \) and to \( i+1 \) compare \( \sigma(p) \) with the same two values \( \sigma(i), \sigma(i+1) \) under \( \sigma \) and under \( \sigma' \), from the same side, so together they contain the same number of inversions. Hence \( \sigma' \) has one inversion fewer than \( \sigma \), contradicting the choice of \( \sigma \). So \( \sigma = \id \) maximizes \( g \), and \( g(\sigma) \le g(\id) \) for every \( \sigma \). This proves the lemma.
:::

The move is an **exchange argument**: to show that an arrangement is optimal, show that repairing one local defect never makes things worse. The inequality \( \sum_i a_ib_{\sigma(i)} \le \sum_i a_ib_i \) is known as the rearrangement inequality.

::: {#exm-sorted-pairing-three}
[Three numbers, six pairings]

Let \( \a = (4, 2, 1) \) and \( \b = (3, 0, -1) \), both decreasing. Compute \( \sum_i(a_i - b_{\sigma(i)})^2 \) for all six \( \sigma \in S_3 \), and find the cheapest and the dearest.
:::

::: {.solution}
The nine squared distances \( (a_i - b_j)^2 \), with \( i \) the row and \( j \) the column, are
\[
\begin{pmatrix} 1 & 16 & 25 \\ 1 & 4 & 9 \\ 4 & 1 & 4 \end{pmatrix} .
\]
A pairing picks one entry from each row and each column. Writing \( \sigma \) by its values \( (\sigma(1), \sigma(2), \sigma(3)) \),
\[
\begin{aligned}
(1,2,3) &: 1 + 4 + 4 = 9 , & (1,3,2) &: 1 + 9 + 1 = 11 , \\
(2,1,3) &: 16 + 1 + 4 = 21 , & (2,3,1) &: 16 + 9 + 4 = 29 , \\
(3,1,2) &: 25 + 1 + 1 = 27 , & (3,2,1) &: 25 + 4 + 4 = 33 .
\end{aligned}
\]
The identity, which pairs the two sorted lists in order, costs \( 9 \), the least of the six, as @lem-sorted-pairing says. The dearest is the reversed pairing \( (3,2,1) \), at \( 33 \).

One exchange step of the proof is visible here. The permutation \( (1,3,2) \) has the single inversion \( \sigma(2) > \sigma(3) \); undoing it gives the identity and lowers the cost by \( 2 \), which is \( 2(a_2 - a_3)(b_2 - b_3) = 2 \cdot 1 \cdot 1 \).
:::

::: {#cor-hoffman-wielandt-hermitian}
[Hoffman–Wielandt for Hermitian Matrices]

Let \( \A, \B \in M_n(\nC) \) be Hermitian. Then
\[
\sum_{i=1}^{n}\bigl(\lambda_i(\A) - \lambda_i(\B)\bigr)^2 \ \le\ \norm{\A - \B}_F^2 .
\]
:::

::: {.proof}
Hermitian matrices are normal (@prp-self-adjoint-immediate (c)) and have real eigenvalues. By @thm-hoffman-wielandt applied to the lists \( \lambda_1(\A), \dots, \lambda_n(\A) \) and \( \lambda_1(\B), \dots, \lambda_n(\B) \), there is \( \sigma \in S_n \) with \( \sum_i\bigl(\lambda_i(\A) - \lambda_{\sigma(i)}(\B)\bigr)^2 \le \norm{\A - \B}_F^2 \), where \( \lvert t\rvert^2 = t^2 \) for real \( t \). Both lists are decreasing, so by @lem-sorted-pairing the sorted pairing costs no more than \( \sigma \). This proves the corollary.
:::

This is the Frobenius-norm companion of Weyl's bound. Put \( \E = \A - \B \), Hermitian. By the spectral theorem \( \E = \U\D\U^{*} \) with \( \U \) unitary and \( \D = \diag(\lambda_1(\E), \dots, \lambda_n(\E)) \), so @lem-frobenius-unitarily-invariant gives \( \norm{\E}_F^2 = \norm{\D}_F^2 = \sum_i\lambda_i(\E)^2 \), while \( \norm{\E}_2 = \max_i\lvert\lambda_i(\E)\rvert \) by @lem-hermitian-spectral-norm. So Weyl's @cor-weyl-perturbation says
\[
\max_i\,\bigl\lvert\lambda_i(\A) - \lambda_i(\B)\bigr\rvert \ \le\ \max_i\,\lvert\lambda_i(\E)\rvert ,
\]
and @cor-hoffman-wielandt-hermitian says
\[
\sum_i\bigl(\lambda_i(\A) - \lambda_i(\B)\bigr)^2 \ \le\ \sum_i\lambda_i(\E)^2 .
\]
In both, a norm of the vector of shifts \( \vlambda(\A) - \vlambda(\B) \) is bounded by the same norm of \( \vlambda(\E) \): the \( \infty \)-norm for Weyl, the \( 2 \)-norm for Hoffman–Wielandt.

Neither implies the other. For \( \E = t\I \) with \( t > 0 \), every eigenvalue shifts by \( t \); Weyl's bound \( t \) is exact for each shift, while Hoffman–Wielandt alone allows a single shift as large as \( \norm{\E}_F = \sqrt n\,t \). For a rank-one \( \E = t\,\x\x^{*} \) with \( \norm{\x}_2 = 1 \), \( \norm{\E}_F = \norm{\E}_2 = t \); Weyl lets **every** eigenvalue move by up to \( t \), while Hoffman–Wielandt says that the squared shifts together use up at most \( t^2 \), so if one eigenvalue moves by \( t \), none of the others moves at all.

::: {.remark}
Lidskii's inequality contains both. Chapter 16 §07 proved \( \vlambda(\A) - \vlambda(\B) \prec \vlambda(\A - \B) \) (the remark after @thm-lidskii-inequality), and Weyl's bound follows from it there, as @cor-lidskii-special-cases (a). Chapter 20 shows that a majorization \( \x \prec \y \) gives \( \sum_i\phi(x_i) \le \sum_i\phi(y_i) \) for every convex \( \phi \); with \( \phi(t) = t^2 \) this is @cor-hoffman-wielandt-hermitian again, and Chapter 20 turns the same majorization into one bound for every unitarily invariant norm. Nothing here depends on that route; the proof above goes through Birkhoff's theorem, @thm-birkhoff.
:::

::: {.check}
Let \( \A = \diag(3, 1) \) and \( \B = \begin{psmallmatrix} 2 & 1 \\ 1 & 2 \end{psmallmatrix} \). Compute \( \norm{\A - \B}_F^2 \) and both sides of @cor-hoffman-wielandt-hermitian. What does the reversed pairing \( \lambda_1(\A) \leftrightarrow \lambda_2(\B) \), \( \lambda_2(\A) \leftrightarrow \lambda_1(\B) \) cost?
:::

::: {.solution}
\( \A - \B = \begin{psmallmatrix} 1 & -1 \\ -1 & -1 \end{psmallmatrix} \), so \( \norm{\A - \B}_F^2 = 4 \). The eigenvalues of \( \B \) are \( 3 \) and \( 1 \) (as in @exm-hoffman-wielandt-two-by-two), the same as those of \( \A \). So the left side of the corollary is \( 0 \le 4 \): two matrices at Frobenius distance \( 2 \) can have identical spectra, and the inequality is only an upper bound. The reversed pairing costs \( (3 - 1)^2 + (1 - 3)^2 = 8 > 4 \). Even for Hermitian matrices, the pairing matters.
:::

## Exercises

### A. Check your understanding

:::: {#exr-hoffman-wielandt-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the Hoffman–Wielandt theorem, with its hypotheses.
2. True or false: if \( \A \) and \( \B \) are normal, the eigenvalues of \( \B \) listed in any order satisfy \( \sum_i\lvert\lambda_i - \mu_i\rvert^2 \le \norm{\A - \B}_F^2 \). Justify your answer.
3. True or false: the Hoffman–Wielandt inequality holds for every pair of diagonalizable matrices. Justify your answer.
4. For normal \( \A \) and \( \B \), what bound does the theorem give on the distance between an eigenvalue of \( \B \) and its partner?
5. Where exactly does Birkhoff's theorem (@thm-birkhoff) enter the proof, and what would be missing without it?
6. For Hermitian \( \A \), \( \B \) with \( \E = \A - \B \) of rank one, explain why at most one eigenvalue can move by the full amount \( \norm{\E}_2 \).
:::
::::

::: {.solution}
(a) If \( \A, \B \in M_n(\nC) \) are normal, with eigenvalues \( \lambda_1, \dots, \lambda_n \) and \( \mu_1, \dots, \mu_n \) listed with multiplicity, then there is a permutation \( \sigma \) with \( \sum_i\lvert\lambda_i - \mu_{\sigma(i)}\rvert^2 \le \norm{\A - \B}_F^2 \).

(b) False. In @exm-hoffman-wielandt-two-by-two, the order \( (3, 1) \) and \( (i, 2 + i) \) costs \( 12 > 8 \). Only a suitable pairing, for instance the cheapest one, is guaranteed.

(c) False. In @exm-hoffman-wielandt-fails both matrices have two distinct eigenvalues, hence are diagonalizable, and both pairings cost more than \( \norm{\A - \B}_F^2 = 1 \).

(d) Each summand is at most the whole sum, so \( \lvert\lambda_i - \mu_{\sigma(i)}\rvert \le \norm{\A - \B}_F \) for every \( i \), for the pairing \( \sigma \) of the theorem.

(e) The proof writes \( \norm{\A - \B}_F^2 \) as \( \sum_{i,j}s_{ij}\lvert\lambda_i - \mu_j\rvert^2 \) with \( (s_{ij}) \) doubly stochastic, a fractional pairing. Birkhoff's theorem, through @lem-doubly-stochastic-linear-min, replaces it by a genuine pairing that costs no more. Without it, we would know only that a weighted average of the costs \( \lvert\lambda_i - \mu_j\rvert^2 \) is small, which does not produce a permutation.

(f) For Hermitian \( \E \) of rank one, \( \E \) has at most one non-zero eigenvalue, so \( \norm{\E}_F^2 = \sum_i\lambda_i(\E)^2 = \norm{\E}_2^2 \). By @cor-hoffman-wielandt-hermitian the squared shifts add up to at most \( \norm{\E}_2^2 \). If one shift equals \( \norm{\E}_2 \) in absolute value, the others are \( 0 \).
:::

### B. Practice

:::: {#exr-hoffman-wielandt-b1}
[B1: A pair of normal matrices]

Let
\[
\A = \begin{pmatrix} 0 & 2 \\ 2 & 0 \end{pmatrix} , \qquad
\B = \begin{pmatrix} 1 & 0 \\ 0 & -1 + 2i \end{pmatrix} .
\]
Check that both are normal, compute \( \norm{\A - \B}_F^2 \) and the costs of both pairings of the eigenvalues, and compute the matrix \( \S \) of the proof of @thm-hoffman-wielandt. Hence decide which pairings satisfy the Hoffman–Wielandt inequality.
::::

::: {.solution}
\( \A \) is real symmetric, hence normal, and \( \B \) is diagonal, hence normal. \( \A(1,1) = (2,2) \) and \( \A(1,-1) = (-2,2) \), so \( \A \) has eigenvalues \( \lambda_1 = 2 \), \( \lambda_2 = -2 \) with unit eigenvectors \( \tfrac{1}{\sqrt2}(1, \pm1) \). \( \B \) has eigenvalues \( \mu_1 = 1 \), \( \mu_2 = -1 + 2i \).

\( \A - \B = \begin{psmallmatrix} -1 & 2 \\ 2 & 1 - 2i \end{psmallmatrix} \), so \( \norm{\A - \B}_F^2 = 1 + 4 + 4 + 5 = 14 \).

The squared distances are \( c_{11} = \lvert 2 - 1\rvert^2 = 1 \), \( c_{12} = \lvert 3 - 2i\rvert^2 = 13 \), \( c_{21} = \lvert -3\rvert^2 = 9 \), \( c_{22} = \lvert -1 - 2i\rvert^2 = 5 \). The identity pairing costs \( 1 + 5 = 6 \), and the swap costs \( 13 + 9 = 22 \).

With \( \U = \tfrac{1}{\sqrt2}\begin{psmallmatrix} 1 & 1 \\ 1 & -1 \end{psmallmatrix} \) and \( \V = \I \), \( \W = \U^{*} \) has all entries of modulus \( \tfrac1{\sqrt2} \), so \( \S = \tfrac12\J \), and indeed \( \tfrac12(1 + 13 + 9 + 5) = 14 \). Hence the identity pairing satisfies the inequality, \( 6 \le 14 \), and the swap does not, \( 22 > 14 \).
:::

:::: {#exr-hoffman-wielandt-b2}
[B2: Hermitian, compared with Weyl]

Let
\[
\A = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix} , \qquad
\B = \begin{pmatrix} 2 & 1 & 0 \\ 1 & 2 & 0 \\ 0 & 0 & -1 \end{pmatrix} .
\]
Compute \( \vlambda(\A) \), \( \vlambda(\B) \), \( \norm{\A - \B}_F \) and \( \norm{\A - \B}_2 \). Verify @cor-hoffman-wielandt-hermitian and @cor-weyl-perturbation for this pair. Hence say which of the two bounds is closer to the truth here.
::::

::: {.solution}
\( \vlambda(\A) = (2, 1, 0) \). The top-left block of \( \B \) has eigenvalues \( 3 \) and \( 1 \) (with eigenvectors \( (1,1) \) and \( (1,-1) \)), and the last entry is \( -1 \), so \( \vlambda(\B) = (3, 1, -1) \). The shifts are \( \lambda_i(\B) - \lambda_i(\A) = 1, 0, -1 \).

\( \E = \B - \A = \begin{psmallmatrix} 0 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & -1 \end{psmallmatrix} \), so \( \norm{\E}_F^2 = 1 + 1 + 1 + 1 = 4 \) and \( \norm{\E}_F = 2 \). Its top-left block has characteristic polynomial \( x^2 - x - 1 \), with roots \( \tfrac{1 \pm \sqrt5}{2} \), and its last eigenvalue is \( -1 \). By @lem-hermitian-spectral-norm, \( \norm{\E}_2 = \tfrac{1 + \sqrt5}{2} \approx 1.618 \).

Hoffman–Wielandt: \( 1^2 + 0^2 + (-1)^2 = 2 \le 4 \). Weyl: each \( \lvert\text{shift}\rvert \le 1 \le 1.618 \). Hence both hold. Weyl overestimates the largest shift by a factor of about \( 1.6 \); Hoffman–Wielandt overestimates the sum of squares by a factor of \( 2 \). Neither is sharp here, and neither dominates.
:::

:::: {#exr-hoffman-wielandt-b3}
[B3: Sorting]

Let \( \a = (5, 2, -1) \) and \( \b = (4, 3, 0) \). Compute \( \sum_i(a_i - b_{\sigma(i)})^2 \) for all six \( \sigma \in S_3 \). Hence confirm @lem-sorted-pairing, and say which pairing is the most expensive.
::::

::: {.solution}
Write \( \sigma \) by its values \( (\sigma(1), \sigma(2), \sigma(3)) \). Then
\[
\begin{aligned}
(1,2,3) &: 1 + 1 + 1 = 3 , & (1,3,2) &: 1 + 4 + 16 = 21 , \\
(2,1,3) &: 4 + 4 + 1 = 9 , & (2,3,1) &: 4 + 4 + 25 = 33 , \\
(3,1,2) &: 25 + 4 + 16 = 45 , & (3,2,1) &: 25 + 1 + 25 = 51 .
\end{aligned}
\]
The identity, which pairs the sorted lists in order, costs \( 3 \), the least of the six, as the lemma says. The most expensive is \( (3,2,1) \), which pairs the largest \( a \) with the smallest \( b \) and so on: the reversed order. Exercise C1 (b) shows this is no accident.
:::

### C. Going deeper

:::: {#exr-hoffman-wielandt-c1}
[C1: The most expensive pairing]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \A, \B \in M_n(\nC) \) be normal, with eigenvalues \( \lambda_i \) and \( \mu_i \). Prove that there is also a permutation \( \sigma \) with \( \sum_i\lvert\lambda_i - \mu_{\sigma(i)}\rvert^2 \ge \norm{\A - \B}_F^2 \).
2. Deduce that for Hermitian \( \A, \B \),
\[
\sum_{i=1}^{n}\bigl(\lambda_i(\A) - \lambda_{n+1-i}(\B)\bigr)^2 \ \ge\ \norm{\A - \B}_F^2 .
\]
:::

*Hint for (b): apply @lem-sorted-pairing to the list \( -\lambda_{n+1-i}(\B) \).*
::::

::: {.solution}
(a) Apply @lem-doubly-stochastic-linear-min to the same \( \S \in \Omega_n \) as in the proof of @thm-hoffman-wielandt and to the matrix \( -\C \), where \( c_{ij} = \lvert\lambda_i - \mu_j\rvert^2 \). It gives \( \tau \) with \( -\sum_j c_{\tau(j)j} \le -\sum_{i,j}s_{ij}c_{ij} = -\norm{\A - \B}_F^2 \), by @eq-hoffman-wielandt-weights. Multiplying by \( -1 \) and putting \( \sigma = \tau^{-1} \), as in that proof, gives \( \sum_i\lvert\lambda_i - \mu_{\sigma(i)}\rvert^2 \ge \norm{\A - \B}_F^2 \).

(b) Write \( a_i = \lambda_i(\A) \) and \( c_i = \lambda_i(\B) \), and let \( b_i = -c_{n+1-i} \). Both \( (a_i) \) and \( (b_i) \) are decreasing, the second because \( c_{n+1-i} \) increases with \( i \). Let \( \pi \in S_n \), and let \( \sigma(i) = n + 1 - \pi(i) \), which is again a permutation, with \( b_{\sigma(i)} = -c_{\pi(i)} \). By @lem-sorted-pairing, \( \sum_i(a_i - b_i)^2 \le \sum_i(a_i - b_{\sigma(i)})^2 \), that is,
\[
\sum_i(a_i + c_{n+1-i})^2 \ \le\ \sum_i(a_i + c_{\pi(i)})^2 .
\]
Expanding both sides, the squares \( \sum_i a_i^2 \) and \( \sum_j c_j^2 \) cancel, and what remains is \( \sum_i a_ic_{n+1-i} \le \sum_i a_ic_{\pi(i)} \). Hence
\[
\sum_i(a_i - c_{\pi(i)})^2 = \sum_i a_i^2 + \sum_j c_j^2 - 2\sum_i a_ic_{\pi(i)} \ \le\ \sum_i(a_i - c_{n+1-i})^2 .
\]
So the reversed pairing \( i \mapsto n + 1 - i \) is the most expensive of all. By (a) some pairing costs at least \( \norm{\A - \B}_F^2 \), so the most expensive one does too, which is the claim.
:::

:::: {#exr-hoffman-wielandt-c2}
[C2: Each eigenvalue keeps its own disc]

Let \( \A \in M_n(\nC) \) be normal with **distinct** eigenvalues \( \lambda_1, \dots, \lambda_n \), and let \( \delta = \min_{i \ne j}\lvert\lambda_i - \lambda_j\rvert \). Let \( \B \) be normal with \( \norm{\A - \B}_F < \delta/2 \). Prove that each open disc \( \{z : \lvert z - \lambda_i\rvert < \delta/2\} \) contains **exactly one** eigenvalue of \( \B \), counted with multiplicity. Explain why @cor-bauer-fike-normal alone does not give this.
::::

::: {.solution}
The discs are pairwise disjoint: if \( \lvert z - \lambda_i\rvert < \delta/2 \) and \( \lvert z - \lambda_j\rvert < \delta/2 \) with \( i \ne j \), the triangle inequality (@thm-complex-triangle-inequality) gives \( \lvert\lambda_i - \lambda_j\rvert < \delta \), contradicting the definition of \( \delta \). By @thm-hoffman-wielandt there is \( \sigma \) with \( \sum_i\lvert\lambda_i - \mu_{\sigma(i)}\rvert^2 \le \norm{\A - \B}_F^2 < \delta^2/4 \), so \( \lvert\lambda_i - \mu_{\sigma(i)}\rvert < \delta/2 \) for every \( i \). Thus the entry \( \mu_{\sigma(i)} \) of the list lies in the \( i \)-th disc, and, the discs being disjoint, in no other. Since \( \sigma \) is a bijection, every entry of the list \( \mu_1, \dots, \mu_n \) is \( \mu_{\sigma(i)} \) for exactly one \( i \). So the \( i \)-th disc contains exactly one entry of the list, namely \( \mu_{\sigma(i)} \), which is the claim.

@cor-bauer-fike-normal (a), with \( \norm{\A - \B}_2 \le \norm{\A - \B}_F < \delta/2 \) (@prp-spectral-vs-frobenius, or both norms being \( 0 \) if \( \A = \B \), the case the proposition excludes), puts every eigenvalue of \( \B \) in the union of the discs, but, as in the first example of this section, it allows two of them to fall in the same disc and leave another disc empty.
:::

:::: {#exr-hoffman-wielandt-c3}
[C3: A Jordan block of any size]

Let \( n \ge 2 \), \( \varepsilon > 0 \), \( \A = \J_n(0) \) and \( \B = \J_n(0) + \varepsilon\E_{n1} \), where \( \E_{n1} \) is the matrix unit.

::: {.enumerate options="label=(\alph*)"}
1. Show that the characteristic polynomial of \( \B \) is \( x^n - \varepsilon \), and hence that every pairing of the eigenvalues of \( \A \) and \( \B \) costs \( n\varepsilon^{2/n} \).
2. Deduce that the Hoffman–Wielandt inequality fails for every pairing whenever \( 0 < \varepsilon < n^{n/(2n-2)} \), and that the ratio of the cost to \( \norm{\A - \B}_F^2 \) tends to \( \infty \) as \( \varepsilon \to 0^{+} \).
:::

*Hint for (a): expand \( \det(x\I - \B) \) along the first column.*
::::

::: {.solution}
(a) \( x\I - \B \) has \( x \) on the diagonal, \( -1 \) on the superdiagonal, \( -\varepsilon \) in position \( (n, 1) \) and zeros elsewhere. Expanding along the first column, the \( (1,1) \) entry \( x \) multiplies the determinant of an upper triangular matrix with diagonal \( x \), which is \( x^{n-1} \). The \( (n,1) \) entry \( -\varepsilon \) carries the sign \( (-1)^{n+1} \) and multiplies the determinant of the matrix left after deleting row \( n \) and column \( 1 \), which is lower triangular with diagonal entries \( -1 \), hence has determinant \( (-1)^{n-1} \). So
\[
\det(x\I - \B) = x^n + (-1)^{n+1}(-\varepsilon)(-1)^{n-1} = x^n - \varepsilon .
\]
Its roots are the \( n \) complex numbers \( z \) with \( z^n = \varepsilon \), each of modulus \( \varepsilon^{1/n} \) (these are Chapter 15's computation in @exm-jordan-block-perturbation). Every eigenvalue of \( \A \) is \( 0 \), so every pairing costs \( \sum_i\lvert 0 - \mu_{\sigma(i)}\rvert^2 = n\,\varepsilon^{2/n} \).

(b) \( \A - \B = -\varepsilon\E_{n1} \), so \( \norm{\A - \B}_F^2 = \varepsilon^2 \). The inequality fails for every pairing exactly when \( n\varepsilon^{2/n} > \varepsilon^2 \), that is, \( \varepsilon^{2 - 2/n} < n \), that is, \( \varepsilon < n^{1/(2 - 2/n)} = n^{n/(2n-2)} \); for \( n = 2 \) this is \( \varepsilon < 2 \), as in the text. The ratio is \( n\varepsilon^{2/n}/\varepsilon^2 = n\varepsilon^{-(2n-2)/n} \), and the exponent \( -(2n-2)/n \) is negative, so the ratio tends to \( \infty \) as \( \varepsilon \to 0^{+} \).
:::
