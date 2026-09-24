# How Far from Normal

Every theorem so far in this chapter has been a yes-or-no statement. An operator either commutes with its adjoint or it does not; there either is an orthonormal basis of eigenvectors or there is not. That is unsatisfying, because the two matrices \( \begin{pmatrix} 1 & 10^{-6} \\ 0 & 2\end{pmatrix} \) and \( \begin{pmatrix} 1 & 10^{6} \\ 0 & 2\end{pmatrix} \) are both non-normal, and no one would want to treat them alike. This section replaces the yes-or-no answer with a number. The number comes out of Schur's theorem almost for free, once we know that the Frobenius norm cannot tell one orthonormal basis from another, and it turns out to measure exactly the mass that a Schur factorization is forced to leave above the diagonal.

Throughout, \( \A \in M_n(\nC) \) and \( \nC^n \) carries the standard inner product. Eigenvalues are always counted **in \( \nC \)** and **with algebraic multiplicity**, so that an \( n \times n \) matrix always has a list of exactly \( n \) of them (@cor-complex-polynomial-splits).

## The yardstick

Sizes here are measured in the **Frobenius norm**, which Chapter 10 §07 defined as the norm induced by the Frobenius inner product:
\[
\norm{\A}_F = \sqrt{\inner{\A}{\A}} = \Bigl( \sum_{i,j}\lvert a_{ij}\rvert^2 \Bigr)^{1/2}
= \sqrt{\tr(\A^{*}\A)} ,
\]
where \( \inner{\A}{\B} = \tr(\B^{*}\A) \). It is the right instrument here for one reason, proved there: unitary factors are invisible to it, so \( \norm{\U\A}_F = \norm{\A}_F = \norm{\A\V}_F \) for unitary \( \U \) and \( \V \), and in particular a unitary similarity leaves it alone (@lem-frobenius-unitarily-invariant). Everything below follows from that one sentence and from Schur's theorem.

## Schur's inequality

Here is the observation the section is built on. Write a matrix in a Schur form \( \A = \U\T\U^{*} \). The diagonal of \( \T \) holds the eigenvalues, so \( \sum_i \lvert\lambda_i\rvert^2 \) is the Frobenius mass sitting *on* the diagonal of \( \T \). The rest of \( \T \) sits strictly above it. And by @lem-frobenius-unitarily-invariant the total mass of \( \T \) is the total mass of \( \A \). Rearranged, that is a theorem.

::: {#thm-schur-inequality}
[Schur's Inequality]

Let \( \A \in M_n(\nC) \) have eigenvalues \( \lambda_1, \dots, \lambda_n \), listed with algebraic multiplicity. Then
\[
\sum_{i=1}^{n} \lvert \lambda_i \rvert^2 \;\le\; \norm{\A}_F^2 ,
\]
with **equality if and only if \( \A \) is normal**.
:::

::: {.idea}
Schur-triangularize, then count. ① \( \A = \U\T\U^{*} \) with \( \T \) upper triangular and the \( \lambda_i \) on its diagonal (@cor-schur-matrix). ② The Frobenius norm does not notice the \( \U \)'s, so \( \norm{\A}_F = \norm{\T}_F \). ③ Splitting \( \norm{\T}_F^2 \) into its diagonal part and its strictly upper part gives the inequality on the nose, with the strictly upper part as the exact surplus. ④ For the equality case, that surplus vanishes exactly when \( \T \) is diagonal, and "triangular and normal" and "diagonal" were shown to be the same thing in @lem-triangular-normal-diagonal.
:::

::: {.proof}
By @cor-schur-matrix there are a unitary \( \U \) and an upper triangular \( \T = (t_{ij}) \) with \( \A = \U\T\U^{*} \) and \( t_{ii} = \lambda_i \) for every \( i \). Since \( t_{ij} = 0 \) whenever \( i > j \), the entries of \( \T \) fall into the diagonal ones and the strictly upper ones, so by @lem-frobenius-unitarily-invariant
\[
\begin{aligned}
\norm{\A}_F^2 = \norm{\T}_F^2
&= \sum_{i=1}^{n} \lvert t_{ii}\rvert^2 + \sum_{i < j} \lvert t_{ij}\rvert^2 \\
&= \sum_{i=1}^{n} \lvert \lambda_i\rvert^2 + \sum_{i < j} \lvert t_{ij}\rvert^2 .
\end{aligned}
\]{#eq-schur-split}
The second sum is a sum of non-negative reals, so it is \( \ge 0 \), and the inequality follows. Moreover equality holds if and only if that sum is \( 0 \), which happens if and only if \( t_{ij} = 0 \) for all \( i < j \), that is, if and only if **this** \( \T \) is diagonal.

\( (\Leftarrow) \) Suppose \( \A \) is normal. Then so is \( \T = \U^{*}\A\U \): using \( \U\U^{*} = \I \) in the middle of each product,
\[
\T^{*}\T = \U^{*}\A^{*}\A\U = \U^{*}\A\A^{*}\U = \T\T^{*} .
\]
A normal upper triangular matrix is diagonal (@lem-triangular-normal-diagonal), so \( \T \) is diagonal and @eq-schur-split gives equality.

\( (\Rightarrow) \) Suppose equality holds. Then, as noted, \( \T \) is diagonal, so \( \A = \U\T\U^{*} \) exhibits \( \A \) as unitarily diagonalizable, and @cor-spectral-complex-matrix makes \( \A \) normal.

This proves the inequality and both halves of the equality case.
:::

Notice that the proof never had to worry about *which* Schur factorization was used. The two sides of the inequality — the eigenvalue list and \( \norm{\A}_F \) — are determined by \( \A \) alone, so the surplus \( \sum_{i<j}\lvert t_{ij}\rvert^2 \) in @eq-schur-split comes out the same for every triangularization of \( \A \), even though the individual entries \( t_{ij} \) certainly do not. That is worth a second look, and we will look at it in a moment.

::: {#exm-schur-inequality-2x2}
[Both sides of Schur's inequality]

Verify @thm-schur-inequality for
\[
\A = \begin{pmatrix} 0 & 1 \\ 2 & 0 \end{pmatrix} ,
\]
and locate the surplus inside an explicit Schur factorization (@cor-schur-matrix).
:::

::: {.solution}
Here \( \tr\A = 0 \) and \( \det\A = -2 \), so \( p_{\A} = x^2 - 2 \) and the eigenvalues are \( \pm\sqrt2 \). Thus
\[
\sum_i \lvert\lambda_i\rvert^2 = 2 + 2 = 4,
\qquad
\norm{\A}_F^2 = 0 + 1 + 4 + 0 = 5 ,
\]
and indeed \( 4 < 5 \). The inequality is strict, so @thm-schur-inequality already says that \( \A \) is not normal — no product of matrices needed.

For the factorization, solve \( (\A - \sqrt2\I)\x = \0 \): the first row reads \( -\sqrt2 x_1 + x_2 = 0 \), giving the eigenvector \( (1, \sqrt2) \) of norm \( \sqrt3 \). Take
\[
\q_1 = \tfrac1{\sqrt3}(1, \sqrt2),
\qquad
\q_2 = \tfrac1{\sqrt3}(-\sqrt2, 1),
\]
a pair of orthonormal vectors, and let \( \U \) have them as columns. Then
\[
\U^{*}\A\U = \begin{pmatrix} \sqrt2 & -1 \\ 0 & -\sqrt2 \end{pmatrix} = \T .
\]
Its Frobenius mass is \( 2 + 1 + 2 = 5 = \norm{\A}_F^2 \), as @lem-frobenius-unitarily-invariant promises, and the split of @eq-schur-split reads \( 5 = 4 + 1 \): the whole surplus is the single entry \( -1 \) above the diagonal.
:::

::: {.check}
The real matrix \( \A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \) has \( \norm{\A}_F^2 = 2 \) and no real eigenvalue at all. Does @thm-schur-inequality fail for it?
:::

::: {.solution}
No, because the eigenvalues are counted in \( \nC \). They are \( i \) and \( -i \), so \( \sum_i\lvert\lambda_i\rvert^2 = 1 + 1 = 2 = \norm{\A}_F^2 \): equality, which is exactly right, since \( \A\tp\A = \A\A\tp = \I \) makes \( \A \) normal. Restricting the eigenvalue list to \( \nR \) would leave the left-hand side empty and the statement meaningless; this is one more place where the Fundamental Theorem of Algebra (@thm-fundamental-theorem-of-algebra) is doing silent work.
:::

## The departure from normality

Schur's inequality has a slack term, and the slack term is the interesting object. It is non-negative for every matrix; it vanishes exactly on the normal ones; and, both of its ingredients being unitary-similarity invariants, it survives a change of orthonormal basis. Those are precisely the properties one wants of a measurement, so we name it.

*The departure from normality is the Frobenius mass that no Schur factorization can push onto the diagonal.*

::: {#def-departure-from-normality}
[Departure from Normality]

Let \( \A \in M_n(\nC) \) have eigenvalues \( \lambda_1, \dots, \lambda_n \), listed with algebraic multiplicity. The **departure from normality** of \( \A \) is the non-negative real number \( \Delta(\A) \) defined by
\[
\Delta(\A)^2 \coloneqq \norm{\A}_F^2 - \sum_{i=1}^{n} \lvert\lambda_i\rvert^2 .
\]
:::

Clause by clause: the quantity on the right is a real number because \( \norm{\A}_F^2 \) and each \( \lvert\lambda_i\rvert^2 \) are real; it is **non-negative** by @thm-schur-inequality, which is what allows us to take its non-negative square root and call the result \( \Delta(\A) \); and the eigenvalue list, though it comes with no preferred order, contributes a sum that does not care about the order. So \( \Delta(\A) \) is well defined, with no choices made anywhere.

Two facts come straight from @thm-schur-inequality and its proof.

- \( \Delta(\A) = 0 \) **if and only if \( \A \) is normal.** This is the equality case, restated.
- \( \Delta(\A) = \bigl(\sum_{i<j}\lvert t_{ij}\rvert^2\bigr)^{1/2} \) **for every** Schur factorization \( \A = \U\T\U^{*} \), by @eq-schur-split. So \( \Delta(\A) \) is the length of the strictly upper triangular part of \( \T \), and the remark after @thm-schur-inequality says that this length is the same for all of them, even though the entries are not.

And one more, which is the reason the number deserves to be called a measurement rather than a coincidence: \( \Delta(\U^{*}\A\U) = \Delta(\A) \) for every unitary \( \U \). Both ingredients are unitary-similarity invariants — the Frobenius norm by @lem-frobenius-unitarily-invariant, the eigenvalue list because similar matrices have the same characteristic polynomial (@thm-charpoly-similarity-invariant). @exr-defect-from-normality-c1 asks for the details, and for an example showing that ordinary similarity wrecks the number completely.

::: {#exm-defect-jordan-block}
[The defect of a Jordan block]

Compute \( \Delta(\J_k(\lambda)) \) for the \( k \times k \) Jordan block with eigenvalue \( \lambda \).
:::

::: {.solution}
The matrix \( \J_k(\lambda) \) has \( \lambda \) in each of its \( k \) diagonal positions and \( 1 \) in each of the \( k - 1 \) superdiagonal positions, and zeros elsewhere, so
\[
\norm{\J_k(\lambda)}_F^2 = k\lvert\lambda\rvert^2 + (k - 1) .
\]
It is upper triangular, so its eigenvalue list is \( \lambda \) repeated \( k \) times (@thm-diagonal-of-triangular-form), giving \( \sum_i\lvert\lambda_i\rvert^2 = k\lvert\lambda\rvert^2 \). Subtracting,
\[
\Delta(\J_k(\lambda))^2 = k - 1,
\qquad
\Delta(\J_k(\lambda)) = \sqrt{k - 1} .
\]
Three things are worth reading off. The answer does not depend on \( \lambda \): sliding a Jordan block up and down the complex plane does not make it more or less normal. It is \( 0 \) exactly when \( k = 1 \), agreeing with the fact that a \( 1 \times 1 \) matrix is normal. And it grows with the block, which matches what @thm-normal-powers gave us in Section 3: a normal operator has no Jordan block of size larger than \( 1 \) (@thm-jordan-canonical-form). Here the defect is counting exactly the superdiagonal ones that normality forbids.
:::

A minimal-change non-example makes the same point on a smaller scale. The matrix \( \diag(1, 3) \) is normal, so its defect is \( 0 \). Change the single entry in position \( (1, 2) \) from \( 0 \) to \( 2 \):
\[
\A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix},
\qquad
\norm{\A}_F^2 = 14,
\qquad
\sum_i\lvert\lambda_i\rvert^2 = 1 + 9 = 10 ,
\]
so \( \Delta(\A) = 2 \). The eigenvalues did not move — a triangular matrix wears them on its diagonal — and the entire change went into the defect. That is the general picture for triangular matrices: for them, \( \Delta \) is just the length of everything above the diagonal.

The defect also bounds something one might actually want to know. Fix a Schur factorization \( \A = \U\T\U^{*} \) (@cor-schur-matrix), write \( \D \) for the diagonal part of \( \T \), and put \( \N = \U\D\U^{*} \), which is normal by @cor-spectral-complex-matrix. Then
\[
\norm{\A - \N}_F = \norm{\T - \D}_F = \Delta(\A) ,
\]
the first step by @lem-frobenius-unitarily-invariant. So \( \Delta(\A) \) is an upper bound for the Frobenius distance from \( \A \) to the set of normal matrices. It is not that distance.

::: {.warning}
**\( \Delta \) is a defect, not a distance.** It is tempting to read \( \Delta(\A) \) as "how far \( \A \) is from the nearest normal matrix", and the displayed bound above makes the temptation worse. But the bound can be strict. Take \( \A = \J_2(0) = \begin{pmatrix} 0 & 1 \\ 0 & 0\end{pmatrix} \), so that \( \Delta(\A) = 1 \) by @exm-defect-jordan-block. The symmetric — hence normal — matrix \( \N = \tfrac12\begin{pmatrix} 0 & 1 \\ 1 & 0\end{pmatrix} \) satisfies
\[
\norm{\A - \N}_F
= \Bigl\lVert \tfrac12\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} \Bigr\rVert_F
= \tfrac1{\sqrt2} < 1 .
\]
So some normal matrix is strictly nearer to \( \A \) than \( \Delta(\A) \). What \( \Delta(\A) \) measures is the mass that survives *triangularization*, which is a genuine and useful quantity, but it is an upper bound for the distance and not the distance itself.
:::

## Eigenvalues that will not sit still

Here is why anyone outside this chapter cares. Eigenvalues are computed, in practice, from data that is only approximately right, so the question "if I move the matrix a little, how far do the eigenvalues move?" is not academic. For a normal matrix the answer is "just as little". For a matrix with a large defect it can be "enormously further". The following pair of \( 2 \times 2 \) matrices shows the whole phenomenon with nothing but the quadratic formula.

::: {#exm-eigenvalue-sensitivity}
[A perturbation that moves the eigenvalues a thousand times as far]

Fix a real number \( M > 0 \) and a real \( \varepsilon \) with \( 0 < \varepsilon < M \). Compare the effect of adding \( \varepsilon \) to the lower-left entry of each of
\[
\A = \begin{pmatrix} 1 & M \\ 0 & 1 \end{pmatrix}
\qquad\text{and}\qquad
\N = \begin{pmatrix} 1 & M \\ -M & 1 \end{pmatrix} .
\]
Compute the defects of \( \A \) and \( \N \), the eigenvalues of both perturbed matrices exactly, and the distance each eigenvalue travels.
:::

::: {.solution}
*The two defects.* The matrix \( \A \) is upper triangular with both diagonal entries \( 1 \), so its eigenvalue list is \( 1, 1 \) and
\[
\Delta(\A)^2 = (1 + M^2 + 1) - (1 + 1) = M^2,
\qquad
\Delta(\A) = M .
\]
The matrix \( \N \) is normal: \( \N\tp\N = \N\N\tp = (1 + M^2)\I \), a direct multiplication. So \( \Delta(\N) = 0 \). Its eigenvalues are \( 1 \pm Mi \), since \( p_{\N} = (x-1)^2 + M^2 \). The two matrices have the same diagonal and the same entry \( M \) in the corner we are leaving alone; where they differ is that one has defect \( M \) and the other defect \( 0 \).

*The non-normal one.* Perturbing the corner gives \( \A_{\varepsilon} = \begin{pmatrix} 1 & M \\ \varepsilon & 1\end{pmatrix} \), with
\[
p_{\A_{\varepsilon}} = (x - 1)^2 - M\varepsilon,
\qquad
\lambda_{\pm} = 1 \pm \sqrt{M\varepsilon} .
\]
The perturbation has size \( \norm{\A_{\varepsilon} - \A}_F = \varepsilon \), and each eigenvalue has moved a distance \( \sqrt{M\varepsilon} \), which is \( \sqrt{M/\varepsilon} \) times the size of the perturbation. With \( M = 100 \) and \( \varepsilon = 10^{-4} \), the perturbation is one ten-thousandth and the eigenvalues move by \( \sqrt{100 \cdot 10^{-4}} = 1/10 \): a thousandfold amplification.

*The normal one.* Perturbing the same corner gives \( \N_{\varepsilon} = \begin{pmatrix} 1 & M \\ -M + \varepsilon & 1\end{pmatrix} \), with
\[
p_{\N_{\varepsilon}} = (x - 1)^2 + M(M - \varepsilon),
\qquad
\mu_{\pm} = 1 \pm i\sqrt{M^2 - M\varepsilon} ,
\]
the square root being a real number because \( \varepsilon < M \). The eigenvalue \( 1 + Mi \) has moved to \( 1 + i\sqrt{M^2 - M\varepsilon} \), a distance of
\[
M - \sqrt{M^2 - M\varepsilon}
= \frac{M\varepsilon}{M + \sqrt{M^2 - M\varepsilon}}
\le \frac{M\varepsilon}{M} = \varepsilon ,
\]
where the middle equality multiplies top and bottom by \( M + \sqrt{M^2 - M\varepsilon} \) and the last step uses \( \sqrt{M^2 - M\varepsilon} \ge 0 \). So here the eigenvalues move by **at most** the size of the perturbation. The same denominator is at most \( 2M \), so the movement is also at least \( \varepsilon/2 \): with \( M = 100 \) and \( \varepsilon = 10^{-4} \) it is a shade over \( \varepsilon/2 \).
:::

The contrast is not an accident of these two matrices, and it is not a theorem we can prove here either. The general statement — that for a diagonalizable \( \A \) every eigenvalue of a perturbed \( \A + \E \) lies within \( \kappa\norm{\E} \) of some eigenvalue of \( \A \), where \( \kappa \) measures how far from unitary the diagonalizing matrix is, and that \( \kappa = 1 \) exactly in the normal case — is the Bauer–Fike theorem. It needs matrix norms and a little analysis, and Chapter 19 develops both and proves it. What the example above establishes on its own is modest and exact: of two \( 2 \times 2 \) matrices with the same diagonal and the same large off-diagonal entry, the one with defect \( 0 \) amplifies a corner perturbation by a factor of at most \( 1 \), and the one with defect \( M \) amplifies it by \( \sqrt{M/\varepsilon} \). The defect is not bookkeeping.

::: {.remark}
The amplification \( \sqrt{M\varepsilon} \) in @exm-eigenvalue-sensitivity has a square root in it, and that square root is the signature of a repeated eigenvalue. The unperturbed \( \A \) has the single eigenvalue \( 1 \) twice over with only one eigenvector, so it is a Jordan block in disguise; splitting a double root is what costs the square root. A matrix with well-separated eigenvalues and a large defect behaves less dramatically.
:::

## The characterizations collected

Schur's inequality gives a normality test of a new kind. Every earlier test compared two matrix products or ranged over all vectors; this one compares two numbers, and one of them is a trace.

::: {#thm-normal-trace-criterion}
[Normality as a Trace Identity]

Let \( \A \in M_n(\nC) \) have eigenvalues \( \lambda_1, \dots, \lambda_n \), listed with algebraic multiplicity. Then \( \A \) is normal if and only if
\[
\tr(\A^{*}\A) = \sum_{i=1}^{n} \lvert\lambda_i\rvert^2 .
\]
:::

::: {.proof}
We showed above that \( \tr(\A^{*}\A) = \norm{\A}_F^2 \). So the displayed equation is the equality case of @thm-schur-inequality, which holds exactly when \( \A \) is normal.
:::

Small as it is, this is the first criterion in the chapter that never asks for \( \A\A^{*} \). If the spectrum is already known — from the characteristic polynomial, or because the matrix arrived in triangular form — normality costs one sum of \( n^2 \) squared moduli and one sum of \( n \) more.

We can now put every description of normality in one place. Sections 3 and 4 proved most of them; this section adds the last one; and one equivalence, the converse of @cor-normal-commuting-poly, has not been proved anywhere and is proved here.

::: {#thm-normal-tfae}
[Normality: The Complete List]

Let \( \A \in M_n(\nC) \) have eigenvalues \( \lambda_1, \dots, \lambda_n \), listed with algebraic multiplicity, and put
\[
\H = \tfrac12(\A + \A^{*}),
\qquad
\K = \tfrac1{2i}(\A - \A^{*}) ,
\]
both of which are Hermitian, with \( \A = \H + i\K \). The following are equivalent.

::: {.enumerate options="label=(\alph*)"}
1. \( \A^{*}\A = \A\A^{*} \), that is, \( \A \) is normal.
2. \( \norm{\A\x} = \norm{\A^{*}\x} \) for every \( \x \in \nC^n \).
3. \( \inner{\A\x}{\A\y} = \inner{\A^{*}\x}{\A^{*}\y} \) for all \( \x, \y \in \nC^n \).
4. \( \H\K = \K\H \).
5. \( \nC^n \) has an orthonormal basis of eigenvectors of \( \A \).
6. \( \A = \U\D\U^{*} \) for some unitary \( \U \) and some diagonal \( \D \).
7. \( \A^{*} = p(\A) \) for some polynomial \( p \in \nC[x] \).
8. \( \sum_{i=1}^{n} \lvert\lambda_i\rvert^2 = \norm{\A}_F^2 \).
:::
:::

::: {.proof}
Let \( T = T_{\A} \) on \( \nC^n \) with its standard inner product, for which the standard basis is orthonormal; then \( T^{*} = T_{\A^{*}} \) by @thm-matrix-of-adjoint, and \( T \) is normal exactly when \( \A \) is.

(a), (b), (c) and (d) are equivalent by @thm-normal-characterizations applied to \( T \), whose four conditions are these four read for \( T \) instead of \( \A \). (a) \( \Leftrightarrow \) (e) is @thm-spectral-complex, again for \( T \). (a) \( \Leftrightarrow \) (f) is @cor-spectral-complex-matrix. (a) \( \Leftrightarrow \) (h) is @thm-normal-trace-criterion, since \( \norm{\A}_F^2 = \tr(\A^{*}\A) \). (a) \( \Rightarrow \) (g) is @cor-normal-commuting-poly, applied to \( T \) and read back as matrices.

It remains to prove (g) \( \Rightarrow \) (a). Suppose \( \A^{*} = p(\A) \) with \( p = c_0 + c_1x + \dots + c_dx^d \). Every power of \( \A \) commutes with \( \A \), hence so does any linear combination of powers:
\[
p(\A)\A = \sum_{k=0}^{d} c_k\A^{k+1} = \A\,p(\A) .
\]
Substituting \( \A^{*} \) for \( p(\A) \) on both sides gives \( \A^{*}\A = \A\A^{*} \), which is (a). This closes the loop and proves the theorem.
:::

This list is the summary result of the chapter, and it is worth reading as a whole rather than as eight separate facts. Conditions (a) and (d) are algebraic: one equation between products. Conditions (b) and (c) are metric: \( \A \) and \( \A^{*} \) distort lengths and angles identically. Conditions (e) and (f) are geometric: the eigenvectors can be chosen perpendicular. Condition (g) is a surprise, and says that for a normal matrix the adjoint carries no information beyond \( \A \) itself. And condition (h) is quantitative: it is the only one on the list that comes with a *number* attached, so that when it fails one can ask by how much. That number is \( \Delta(\A) \), and it is the reason this section exists.

The operator versions of (a)–(g) hold verbatim on any finite-dimensional complex inner product space, by passing to the matrix in an orthonormal basis. So does (h), once \( \norm{\cdot}_F \) is read as the Frobenius norm of that matrix, which @lem-frobenius-unitarily-invariant showed does not depend on which orthonormal basis is used.

## Exercises

### A. Check your understanding

::: {#exr-defect-from-normality-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the Frobenius norm of a matrix, and give the expression for \( \norm{\A}_F^2 \) as a trace.
2. State @thm-schur-inequality, including the equality case and how the eigenvalues are counted.
3. Define \( \Delta(\A) \), and say why the definition needs @thm-schur-inequality before it can be made.
4. True or false: \( \Delta(\A) \) equals the Frobenius distance from \( \A \) to the nearest normal matrix. Justify your answer.
5. True or false: if \( \A \) and \( \B \) are similar then \( \Delta(\A) = \Delta(\B) \). Justify your answer.
6. Name the two facts about the Frobenius norm and about triangular matrices that the proof of @thm-schur-inequality rests on.
:::
:::

::: {.solution}
(a) \( \norm{\A}_F = \bigl(\sum_{i,j}\lvert a_{ij}\rvert^2\bigr)^{1/2} \), the norm induced by the Frobenius inner product \( \inner{\A}{\B} = \tr(\B^{*}\A) \) of Chapter 10. As a trace, \( \norm{\A}_F^2 = \tr(\A^{*}\A) \).

(b) For \( \A \in M_n(\nC) \) with eigenvalues \( \lambda_1, \dots, \lambda_n \) listed **in \( \nC \) and with algebraic multiplicity**, \( \sum_i\lvert\lambda_i\rvert^2 \le \norm{\A}_F^2 \), with equality if and only if \( \A \) is normal.

(c) \( \Delta(\A)^2 = \norm{\A}_F^2 - \sum_i\lvert\lambda_i\rvert^2 \), and \( \Delta(\A) \) is its non-negative square root. Without @thm-schur-inequality the right-hand side might be negative, and there would be no real square root to take.

(d) False. It is an upper bound for that distance, as the paragraph before the warning shows, but the warning gives \( \A = \J_2(0) \) with \( \Delta(\A) = 1 \) and a normal matrix at distance \( 1/\sqrt2 \).

(e) False. The matrices \( \begin{pmatrix} 1 & 1 \\ 0 & 2\end{pmatrix} \) and \( \diag(1, 2) \) are similar, since the first is diagonalizable with eigenvalues \( 1 \) and \( 2 \), yet their defects are \( 1 \) and \( 0 \). What is true is that \( \Delta \) is unchanged by **unitary** similarity; see @exr-defect-from-normality-c1.

(f) That the Frobenius norm is unchanged by unitary factors (@lem-frobenius-unitarily-invariant), so that \( \norm{\A}_F = \norm{\T}_F \); and that a normal upper triangular matrix is diagonal (@lem-triangular-normal-diagonal), which is what makes the equality case work in the direction \( (\Leftarrow) \).
:::

### B. Practice

::: {#exr-defect-from-normality-b1}
[B1: Computing the defect]

For each matrix below, compute \( \norm{\A}_F^2 \), the eigenvalue list, and \( \Delta(\A) \). State in each case whether the matrix is normal, and say how you know without multiplying \( \A \) by \( \A^{*} \).

::: {.enumerate options="label=(\alph*)"}
1. \( \begin{pmatrix} 3 & 4 \\ 0 & 5 \end{pmatrix} \)
2. \( \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix} \)
3. \( \J_3(2) \)
4. \( \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix} \)
:::
:::

::: {.solution}
(a) \( \norm{\A}_F^2 = 9 + 16 + 25 = 50 \). The matrix is upper triangular, so its eigenvalues are \( 3 \) and \( 5 \) (@thm-diagonal-of-triangular-form) and \( \sum_i\lvert\lambda_i\rvert^2 = 34 \). Hence \( \Delta(\A)^2 = 16 \) and \( \Delta(\A) = 4 \). Since \( \Delta(\A) \neq 0 \), the matrix is not normal (@thm-schur-inequality).

(b) \( \norm{\A}_F^2 = 1 + 1 + 1 + 1 = 4 \). Here \( \tr\A = 2 \) and \( \det\A = 1 + 1 = 2 \), so \( p_{\A} = x^2 - 2x + 2 \) and the eigenvalues are \( 1 \pm i \), each of modulus \( \sqrt2 \). Then \( \sum_i\lvert\lambda_i\rvert^2 = 2 + 2 = 4 \), so \( \Delta(\A) = 0 \) and the matrix **is** normal.

(c) \( \norm{\J_3(2)}_F^2 = 3 \cdot 4 + 2 = 14 \), the eigenvalue is \( 2 \) three times, and \( \sum_i\lvert\lambda_i\rvert^2 = 12 \). So \( \Delta^2 = 2 \) and \( \Delta = \sqrt2 \), which is \( \sqrt{k-1} \) with \( k = 3 \), as @exm-defect-jordan-block says. Not normal.

(d) \( \norm{\A}_F^2 = 3 \). The matrix is the cyclic shift, with \( p_{\A} = x^3 - 1 \) (expand along the first row, or note \( \A^3 = \I \) and \( \A \neq \I \) with \( \A \) having no repeated eigenvalue). Its eigenvalues are the three cube roots of unity, each of modulus \( 1 \), so \( \sum_i\lvert\lambda_i\rvert^2 = 3 \) and \( \Delta(\A) = 0 \): normal.
:::

::: {#exr-defect-from-normality-b2}
[B2: Verifying Schur's inequality]

Let
\[
\A = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 2 & 1 \\ 0 & 0 & 3 \end{pmatrix} .
\]

::: {.enumerate options="label=(\alph*)"}
1. Compute both sides of @thm-schur-inequality for \( \A \) and verify the inequality.
2. Hence determine whether \( \A \) is normal, without computing \( \A^{*}\A \) or \( \A\A^{*} \).
3. Write down a normal matrix \( \N \) with \( \norm{\A - \N}_F = \Delta(\A) \), and verify the equality.
:::
:::

::: {.solution}
(a) \( \norm{\A}_F^2 = 1 + 1 + 1 + 4 + 1 + 9 = 17 \). The matrix is upper triangular, so its eigenvalues are \( 1, 2, 3 \) (@thm-diagonal-of-triangular-form) and \( \sum_i\lvert\lambda_i\rvert^2 = 1 + 4 + 9 = 14 \). Indeed \( 14 \le 17 \).

(b) The inequality is strict, so by the equality case of @thm-schur-inequality the matrix is not normal. Equivalently \( \Delta(\A) = \sqrt{17 - 14} = \sqrt3 \neq 0 \).

(c) Since \( \A \) is already upper triangular, \( \A = \I\A\I^{*} \) is a Schur factorization (@cor-schur-matrix) with \( \U = \I \) and \( \T = \A \). The construction before the warning takes \( \N \) to be the diagonal part, \( \N = \diag(1, 2, 3) \), which is normal. Then \( \A - \N \) has the three entries \( 1 \) above the diagonal and zeros elsewhere, so \( \norm{\A - \N}_F = \sqrt3 = \Delta(\A) \).
:::

::: {#exr-defect-from-normality-b3}
[B3: The nearest symmetric matrix]

Let \( \A \in M_n(\nR) \) and write \( \S = \tfrac12(\A + \A\tp) \) and \( \W = \tfrac12(\A - \A\tp) \), so that \( \A = \S + \W \) with \( \S\tp = \S \) and \( \W\tp = -\W \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \inner{\B}{\C} = 0 \) in the Frobenius inner product whenever \( \B \in M_n(\nR) \) is symmetric and \( \C \in M_n(\nR) \) is skew-symmetric.
2. Deduce that \( \norm{\A - \B}_F \ge \norm{\W}_F \) for every symmetric \( \B \in M_n(\nR) \), with equality only for \( \B = \S \). Hence \( \S \) is the nearest symmetric matrix to \( \A \).
3. Carry this out for \( \A = \begin{pmatrix} 2 & 4 \\ 0 & -2 \end{pmatrix} \), and compare the resulting distance with \( \Delta(\A) \).
:::
:::

::: {.solution}
(a) For real matrices \( \inner{\B}{\C} = \tr(\C\tp\B) \). Since \( \C\tp = -\C \), this is \( -\tr(\C\B) \). On the other hand \( \tr(\C\B) = \tr\bigl((\C\B)\tp\bigr) \) by @thm-trace-properties (2), and \( (\C\B)\tp = \B\tp\C\tp = -\B\C \), so \( \tr(\C\B) = -\tr(\B\C) = -\tr(\C\B) \), the last step by @thm-trace-properties (3). A number equal to its own negative is \( 0 \), so \( \tr(\C\B) = 0 \) and \( \inner{\B}{\C} = 0 \).

(b) Let \( \B \) be symmetric. Then \( \A - \B = (\S - \B) + \W \), where \( \S - \B \) is symmetric and \( \W \) is skew-symmetric, so the two are orthogonal by (a) and Pythagoras (@thm-pythagoras) gives
\[
\norm{\A - \B}_F^2 = \norm{\S - \B}_F^2 + \norm{\W}_F^2 \ge \norm{\W}_F^2 .
\]
Equality forces \( \norm{\S - \B}_F = 0 \), that is \( \B = \S \) (@thm-norm-properties (a)). So \( \S \) is the unique nearest symmetric matrix, at distance \( \norm{\W}_F \).

(c) Here \( \S = \begin{pmatrix} 2 & 2 \\ 2 & -2\end{pmatrix} \) and \( \W = \begin{pmatrix} 0 & 2 \\ -2 & 0\end{pmatrix} \), so the distance from \( \A \) to the symmetric matrices is \( \norm{\W}_F = \sqrt{8} = 2\sqrt2 \). For the defect, \( \norm{\A}_F^2 = 4 + 16 + 4 = 24 \), and \( \A \) is triangular with eigenvalues \( 2 \) and \( -2 \), so \( \sum_i\lvert\lambda_i\rvert^2 = 8 \) and \( \Delta(\A) = 4 \). A symmetric matrix is normal, so this again exhibits a normal matrix strictly closer than \( \Delta(\A) \): \( 2\sqrt2 \approx 2.83 < 4 \).
:::

### C. Going deeper

::: {#exr-defect-from-normality-c1}
[C1: Unitary similarity preserves the defect, ordinary similarity does not]

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \Delta(\U^{*}\A\U) = \Delta(\A) \) for every \( \A \in M_n(\nC) \) and every unitary \( \U \).
2. Give \( \A, \B \in M_2(\nC) \) that are similar with \( \Delta(\A) \neq \Delta(\B) \), exhibiting an explicit \( \P \) with \( \P^{-1}\A\P = \B \).
3. Deduce that two similar matrices with different defects cannot be unitarily similar, and use this to show that \( \begin{pmatrix} 1 & 1 \\ 0 & 2\end{pmatrix} \) and \( \diag(1, 2) \) are not unitarily similar.
:::
:::

::: {.solution}
(a) Put \( \B = \U^{*}\A\U \). By @lem-frobenius-unitarily-invariant, \( \norm{\B}_F = \norm{\A}_F \). Also \( \B \) is similar to \( \A \), so \( p_{\B} = p_{\A} \) (@thm-charpoly-similarity-invariant) and the two matrices have the same eigenvalue list with multiplicities. Both terms in @def-departure-from-normality therefore agree, so \( \Delta(\B)^2 = \Delta(\A)^2 \), and the defects are equal since both are non-negative.

(b) Take \( \A = \begin{pmatrix} 1 & 1 \\ 0 & 2\end{pmatrix} \) and \( \B = \diag(1, 2) \). Then \( \norm{\A}_F^2 = 1 + 1 + 4 = 6 \) with eigenvalues \( 1, 2 \), so \( \Delta(\A)^2 = 6 - 5 = 1 \) and \( \Delta(\A) = 1 \), while \( \Delta(\B) = 0 \) because \( \B \) is diagonal, hence normal. They are similar: eigenvectors of \( \A \) are \( (1, 0) \) for \( \lambda = 1 \) and \( (1, 1) \) for \( \lambda = 2 \), so with \( \P = \begin{pmatrix} 1 & 1 \\ 0 & 1\end{pmatrix} \), whose inverse is \( \begin{pmatrix} 1 & -1 \\ 0 & 1\end{pmatrix} \), we get \( \P^{-1}\A\P = \B \) by direct multiplication.

(c) By (a), unitarily similar matrices have equal defects. So if \( \Delta(\A) \neq \Delta(\B) \) then no unitary \( \U \) can satisfy \( \U^{*}\A\U = \B \). The pair in (b) has defects \( 1 \) and \( 0 \), so it is similar but not unitarily similar. (This is the failure of "diagonalizable" to imply "unitarily diagonalizable", seen through a number instead of through @exm-diagonalizable-not-normal.)
:::

::: {#exr-defect-from-normality-c2}
[C2: Equality plus a single eigenvalue forces a scalar]

Let \( \A \in M_n(\nC) \) satisfy \( \norm{\A}_F^2 = \sum_{i=1}^{n}\lvert\lambda_i\rvert^2 \), and suppose \( \A \) has **only one** distinct eigenvalue \( \lambda \), so that \( p_{\A} = (x - \lambda)^n \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \A = \lambda\I \).
2. Deduce that a normal matrix whose characteristic polynomial is \( x^n \) is the zero matrix.
3. Show that the hypothesis of equality cannot be dropped, by computing \( \Delta \) for a matrix with \( p_{\A} = (x - \lambda)^n \) that is not \( \lambda\I \).
:::
:::

::: {.solution}
(a) By the equality case of @thm-schur-inequality, \( \A \) is normal. So by @cor-spectral-complex-matrix there are a unitary \( \U \) and a diagonal \( \D \) with \( \A = \U\D\U^{*} \), the diagonal of \( \D \) being the eigenvalue list of \( \A \). That list is \( \lambda \) repeated \( n \) times, so \( \D = \lambda\I \) and
\[
\A = \U(\lambda\I)\U^{*} = \lambda\U\U^{*} = \lambda\I .
\]

(b) A normal matrix satisfies the equality hypothesis (@thm-schur-inequality again), and \( p_{\A} = x^n \) says its only eigenvalue is \( 0 \). By (a), \( \A = 0\cdot\I = 0 \). In words: a normal nilpotent matrix is zero, which is @thm-normal-powers seen from the quantitative side.

(c) Take \( \A = \J_n(\lambda) \) with \( n \ge 2 \). Its characteristic polynomial is \( (x - \lambda)^n \) and it is not \( \lambda\I \), and \( \Delta(\A) = \sqrt{n-1} \neq 0 \) by @exm-defect-jordan-block. So equality in @thm-schur-inequality fails, exactly as it must.
:::

::: {#exr-defect-from-normality-c3}
[C3: The commutator is at least as big as the defect squared]

For \( \A \in M_n(\nC) \) write \( [\A, \A^{*}] = \A\A^{*} - \A^{*}\A \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \norm{[\A, \A^{*}]}_F \) is unchanged when \( \A \) is replaced by \( \U^{*}\A\U \) with \( \U \) unitary.
2. Let \( \T = \begin{pmatrix} \lambda_1 & b \\ 0 & \lambda_2 \end{pmatrix} \). Compute \( [\T, \T^{*}] \) and show that
\[
\norm{[\T, \T^{*}]}_F^2
= 2\lvert b\rvert^4 + 2\lvert b\rvert^2\lvert\lambda_1 - \lambda_2\rvert^2 .
\]
3. Deduce that every \( \A \in M_2(\nC) \) satisfies \( \norm{[\A, \A^{*}]}_F \ge \sqrt2\,\Delta(\A)^2 \), and determine exactly when equality holds.
:::

*Hint for (c): Schur-triangularize, and use (a) to move the computation to the triangular factor.*
:::

::: {.solution}
(a) Put \( \B = \U^{*}\A\U \), so \( \B^{*} = \U^{*}\A^{*}\U \). Inserting \( \U\U^{*} = \I \) between the factors,
\[
[\B, \B^{*}] = \U^{*}(\A\A^{*} - \A^{*}\A)\U = \U^{*}[\A, \A^{*}]\U ,
\]
and @lem-frobenius-unitarily-invariant gives \( \norm{[\B, \B^{*}]}_F = \norm{[\A, \A^{*}]}_F \).

(b) Multiplying out,
\[
\begin{aligned}
\T\T^{*} &= \begin{pmatrix}
\lvert\lambda_1\rvert^2 + \lvert b\rvert^2 & b\conj{\lambda_2} \\
\lambda_2\conj{b} & \lvert\lambda_2\rvert^2
\end{pmatrix}, \\[2pt]
\T^{*}\T &= \begin{pmatrix}
\lvert\lambda_1\rvert^2 & \conj{\lambda_1}b \\
\lambda_1\conj{b} & \lvert b\rvert^2 + \lvert\lambda_2\rvert^2
\end{pmatrix} .
\end{aligned}
\]
Subtracting,
\[
[\T, \T^{*}] = \begin{pmatrix}
\lvert b\rvert^2 & b\,\conj{(\lambda_2 - \lambda_1)} \\
\conj{b}\,(\lambda_2 - \lambda_1) & -\lvert b\rvert^2
\end{pmatrix} .
\]
Its four squared moduli are \( \lvert b\rvert^4 \), \( \lvert b\rvert^2\lvert\lambda_1 - \lambda_2\rvert^2 \), \( \lvert b\rvert^2\lvert\lambda_1 - \lambda_2\rvert^2 \) and \( \lvert b\rvert^4 \). Adding them gives the stated formula.

(c) Let \( \A \in M_2(\nC) \) and write \( \A = \U\T\U^{*} \) as in @cor-schur-matrix, with \( \T \) upper triangular of the shape in (b) and \( \lambda_1, \lambda_2 \) the eigenvalues of \( \A \). By @eq-schur-split, \( \Delta(\A)^2 = \lvert b\rvert^2 \). By (a) and (b),
\[
\norm{[\A, \A^{*}]}_F^2
= 2\lvert b\rvert^4 + 2\lvert b\rvert^2\lvert\lambda_1 - \lambda_2\rvert^2
\ge 2\lvert b\rvert^4 = 2\,\Delta(\A)^4 ,
\]
and taking non-negative square roots gives \( \norm{[\A, \A^{*}]}_F \ge \sqrt2\,\Delta(\A)^2 \).

Equality holds exactly when \( \lvert b\rvert^2\lvert\lambda_1 - \lambda_2\rvert^2 = 0 \), that is, when \( b = 0 \) or \( \lambda_1 = \lambda_2 \). The first case says \( \Delta(\A) = 0 \), that is, \( \A \) is normal, and then both sides are \( 0 \). So equality holds if and only if \( \A \) is normal or its two eigenvalues coincide.
:::
