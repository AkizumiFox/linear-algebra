# How Wrong Can the Answer Be

Chapter 3 solved \( \A\x = \b \) and Chapter 11 solved it when it had no solution. Neither chapter could ask the question a user of either method asks first: the vector \( \b \) is a measurement, so it is wrong in the last few digits, and the answer \( \x \) is then wrong too — by how much? The question needs a way to compare the size of an error with the size of the thing it corrupts, and that is what the last seven sections have built.

The answer turns out to be one number attached to \( \A \), independent of \( \b \), and it is the last object this chapter defines. It also carries a warning, and the warning is more useful than the number.

**Throughout, matrices are complex**, as in Sections 4 to 7, and \( \norm{\cdot} \) is a norm on \( \nC^{n} \) together with the operator norm it induces on \( M_n(\nC) \) (@def-operator-norm) — the standing convention of Section 5, whose results are used here throughout. A real matrix is read inside \( M_n(\nC) \), which changes none of the three norms we actually compute with, since @thm-operator-norm-formulas gives the same three formulas over either field.

## A recurring product

Let \( \A \in M_n(\nC) \) be invertible, let \( \b \ne \0 \), and let \( \x \) solve \( \A\x = \b \). Suppose the data arrives as \( \b + \Delta\b \) instead, so the computed answer solves \( \A\widetilde\x = \b + \Delta\b \). Subtracting the two equations, \( \A(\widetilde\x - \x) = \Delta\b \), so
\[
\widetilde\x - \x = \A^{-1}\Delta\b,
\qquad
\norm{\widetilde\x - \x} \le \norm{\A^{-1}}\,\norm{\Delta\b}
\]
by @thm-operator-norm-properties (a). That is an *absolute* bound, and absolute bounds are the wrong currency: whether an error of \( 10^{-3} \) is a catastrophe depends on whether the answer is of size \( 1 \) or of size \( 10^{6} \). Divide by \( \norm{\x} \), and use \( \norm{\b} = \norm{\A\x} \le \norm{\A}\norm{\x} \), that is \( 1/\norm{\x} \le \norm{\A}/\norm{\b} \):
\[
\frac{\norm{\widetilde\x - \x}}{\norm{\x}}
\;\le\; \norm{\A^{-1}}\,\norm{\Delta\b}\,\frac{\norm{\A}}{\norm{\b}}
\;=\; \norm{\A}\norm{\A^{-1}}\,\frac{\norm{\Delta\b}}{\norm{\b}} .
\]
The relative error in the answer is at most the relative error in the data, multiplied by \( \norm{\A}\norm{\A^{-1}} \). That product depends only on \( \A \). It will reappear in every estimate in this section, so we name it.

*The condition number is the worst factor by which \( \A \) can magnify a relative error.*

::: {#def-condition-number}
[Condition Number]

Let \( \norm{\cdot} \) be a norm on \( \nC^n \), and write \( \norm{\cdot} \) also for the operator norm it induces on \( M_n(\nC) \). For \( \A \in M_n(\nC) \), the **condition number** of \( \A \) **with respect to that norm** is
\[
\kappa(\A) \coloneqq
\begin{cases}
\norm{\A}\,\norm{\A^{-1}} & \text{if } \A \text{ is invertible},\\[2pt]
\infty & \text{if } \A \text{ is singular}.
\end{cases}
\]
We write \( \kappa_1, \kappa_2, \kappa_{\infty} \) for the condition numbers with respect to \( \norm{\cdot}_1 \), \( \norm{\cdot}_2 \), \( \norm{\cdot}_{\infty} \); \( \kappa_2 \) is also called the **spectral condition number**. For a rectangular \( \A \in M_{m \times n}(\nC) \) with \( m \ge n \) and \( \rank\A = n \), we define
\[
\kappa_2(\A) \coloneqq \frac{\sigma_1(\A)}{\sigma_n(\A)} ,
\]
the ratio of the largest to the smallest singular value (@def-singular-values).
:::

Clause by clause. The number is attached to \( \A \) **and to a norm**: \( \kappa_1(\A) \), \( \kappa_2(\A) \) and \( \kappa_{\infty}(\A) \) are three different numbers, and a statement like "\( \kappa(\A) = 400 \)" is incomplete until the norm is named. They cannot disagree wildly — @thm-norm-equivalence traps them within dimension-dependent factors of each other, and @exr-condition-numbers-c1 makes that precise — so the *order of magnitude* of \( \kappa \), which is all anyone uses, does not depend on the choice. The value \( \infty \) for a singular matrix is a convention, and the right one: a singular \( \A \) either makes \( \A\x = \b \) unsolvable or makes its solution set a whole coset \( \x + \nul(\A) \) with \( \nul(\A) \ne \{\0\} \) (@thm-general-solution-structure), so no finite bound on the error can hold. Finally, the square case and the rectangular case agree where they overlap: @prp-condition-number-properties (d) shows \( \kappa_2(\A) = \sigma_1/\sigma_n \) for an invertible square \( \A \) as well.

Before the examples, a small lemma that says what \( \kappa \) is measuring. It is the one geometric picture in this section, and it is worth carrying.

::: {#lem-inverse-norm-min}
[The Inverse Measures the Smallest Stretch]

Let \( \A \in M_n(\nC) \) be invertible and let \( \norm{\cdot} \) be a norm on \( \nC^n \). Then
\[
\norm{\A^{-1}} = \frac{1}{\min\{\norm{\A\x} : \norm{\x} = 1\}},
\qquad
\kappa(\A) = \frac{\max\{\norm{\A\x} : \norm{\x} = 1\}}{\min\{\norm{\A\x} : \norm{\x} = 1\}} .
\]
:::

::: {.idea}
Both maxima and the minimum exist by compactness, which is @lem-operator-norm-attained and the same argument with a minimum. After that it is one substitution: as \( \x \) runs over the non-zero vectors so does \( \y = \A\x \), and the ratio \( \norm{\A^{-1}\y}/\norm{\y} \) is the reciprocal of \( \norm{\A\x}/\norm{\x} \).
:::

::: {.proof}
The function \( \x \mapsto \norm{\A\x} \) is continuous on the unit sphere \( S \), which is compact, so it attains a maximum and a minimum there (@lem-operator-norm-attained for the maximum; the same proof, or the extreme value theorem (A4) applied to the same continuous function, for the minimum). Write \( m = \min_{\x \in S}\norm{\A\x} \). Since \( \A \) is invertible, \( \A\x \ne \0 \) for \( \x \in S \), so \( m > 0 \).

By @def-operator-norm and homogeneity, \( \norm{\A^{-1}} = \max\{\norm{\A^{-1}\y}/\norm{\y} : \y \ne \0\} \). The map \( \y \mapsto \A^{-1}\y \) is a bijection of \( \nC^n \setminus \{\0\} \) onto itself, so substituting \( \y = \A\x \) with \( \x \ne \0 \),
\[
\norm{\A^{-1}}
= \max_{\x \ne \0}\frac{\norm{\x}}{\norm{\A\x}}
= \frac{1}{\displaystyle\min_{\x \ne \0}\frac{\norm{\A\x}}{\norm{\x}}}
= \frac{1}{m} ,
\]
the last step by homogeneity again, which lets the minimum over \( \x \ne \0 \) be taken over \( S \). Multiplying by \( \norm{\A} = \max_{\x \in S}\norm{\A\x} \) gives the second formula. This proves the lemma.
:::

So \( \kappa(\A) \) is the **distortion** of \( \A \): feed \( \A \) the unit sphere and it comes out as a lopsided surface, and \( \kappa \) is the ratio of its longest radius to its shortest. A matrix with \( \kappa = 1 \) carries the sphere to a sphere. A matrix with \( \kappa = 10^{6} \) flattens it into something a million times longer than it is wide, and a direction of \( \b \) that lands along the short axis has its errors magnified by a million on the way back.

Some values, simplest first.

- **The identity, and any unitary matrix.** \( \norm{\I} = 1 = \norm{\I^{-1}} \), so \( \kappa(\I) = 1 \) in every norm. For unitary \( \U \), \( \norm{\U\x}_2 = \norm{\x}_2 \) for every \( \x \) (@thm-isometry-characterizations), so every stretch is \( 1 \) and \( \kappa_2(\U) = 1 \) by @lem-inverse-norm-min. These are the best-conditioned matrices there are.
- **A diagonal matrix.** For \( \D = \diag(d_1, \dots, d_n) \) with all \( d_i \ne 0 \), \( \norm{\D}_2 = \max_i\lvert d_i\rvert \) and \( \norm{\D^{-1}}_2 = 1/\min_i\lvert d_i\rvert \), so \( \kappa_2(\D) \) is the ratio of the largest to the smallest modulus. Thus \( \kappa_2(\diag(1, 10^{-6})) = 10^{6} \).
- **A small matrix that is perfectly conditioned.** \( \A = 10^{-6}\I \) has \( \norm{\A}_2 = 10^{-6} \), a tiny norm, and \( \kappa_2(\A) = 1 \). Being small and being ill-conditioned are unrelated.
- **A singular matrix**, the degenerate case: \( \kappa = \infty \) by convention, consistent with @lem-inverse-norm-min, where the minimum stretch is \( 0 \).

::: {#exm-condition-numbers-2x2}
[Three condition numbers of one matrix]

Compute \( \kappa_{\infty}(\A) \) and \( \kappa_2(\A) \) for \( \A = \begin{pmatrix} 2 & 1 \\ 1 & 1\end{pmatrix} \).
:::

::: {.solution}
\( \det\A = 1 \), so \( \A^{-1} = \begin{psmallmatrix} 1 & -1 \\ -1 & 2\end{psmallmatrix} \). The largest absolute row sums are \( 3 \) for \( \A \) and \( 3 \) for \( \A^{-1} \), so by @thm-operator-norm-formulas (b), \( \kappa_{\infty}(\A) = 3 \cdot 3 = 9 \).

For \( \kappa_2 \): \( \A \) is real symmetric with \( \tr\A = 3 \) and \( \det\A = 1 \), so its eigenvalues are \( (3 \pm \sqrt5)/2 \), both positive, and the singular values of a symmetric matrix with positive eigenvalues are those eigenvalues (its \( \A^{*}\A = \A^2 \) has eigenvalues their squares). Hence
\[
\kappa_2(\A) = \frac{3 + \sqrt5}{3 - \sqrt5} = \frac{(3+\sqrt5)^2}{4} = \frac{7 + 3\sqrt5}{2} \approx 6.854 .
\]
Two different norms, two different numbers, the same order of magnitude — which is the general picture.
:::

::: {.warning}
**A large \( \kappa \) is not a large determinant defect, and a small determinant is not ill-conditioning.** The matrix \( 10^{-6}\I_{10} \) has determinant \( 10^{-60} \) and \( \kappa_2 = 1 \); the matrix \( \diag(10^{6}, 10^{-6}) \) has determinant \( 1 \) and \( \kappa_2 = 10^{12} \). The determinant scales with \( c^n \) under \( \A \mapsto c\A \) while \( \kappa \) does not move at all (@prp-condition-number-properties (b)), so no threshold on \( \lvert\det\A\rvert \) can detect ill-conditioning. This is the most common wrong test, and it fails in both directions.
:::

The basic properties are all one line each, and the third is the reason \( \kappa \) behaves well under the factorizations of Chapters 11 and 13.

::: {#prp-condition-number-properties}
[Properties of the Condition Number]

Let \( \A, \B \in M_n(\nC) \) be invertible and let \( c \in \nC \setminus\{0\} \). With respect to any operator norm:

::: {.enumerate options="label=(\alph*)"}
1. \( \kappa(\A) \ge 1 \);
2. \( \kappa(c\A) = \kappa(\A) \);
3. \( \kappa(\A\B) \le \kappa(\A)\kappa(\B) \);
4. \( \kappa_2(\A) = \sigma_1(\A)/\sigma_n(\A) \), and \( \kappa_2(\U\A\V) = \kappa_2(\A) \) for all unitary \( \U, \V \).
:::
:::

::: {.proof}
(a) \( 1 = \norm{\I} = \norm{\A\A^{-1}} \le \norm{\A}\norm{\A^{-1}} = \kappa(\A) \), using @thm-operator-norm-properties (c) and (d).

(b) \( (c\A)^{-1} = c^{-1}\A^{-1} \), so by homogeneity \( \norm{c\A}\norm{(c\A)^{-1}} = \lvert c\rvert\,\lvert c\rvert^{-1}\norm{\A}\norm{\A^{-1}} \).

(c) \( (\A\B)^{-1} = \B^{-1}\A^{-1} \), so submultiplicativity (@thm-operator-norm-properties (d)) gives \( \norm{\A\B}\norm{\B^{-1}\A^{-1}} \le \norm{\A}\norm{\B}\norm{\B^{-1}}\norm{\A^{-1}} \).

(d) By @thm-operator-norm-formulas (c), \( \norm{\A}_2 = \sigma_1(\A) \). By @lem-inverse-norm-min, \( \norm{\A^{-1}}_2 = 1/m \) with \( m = \min\{\norm{\A\x}_2 : \norm{\x}_2 = 1\} \), so it remains to see \( m = \sigma_n(\A) \). Write \( \A = \U\vSigma\V^{*} \) (@thm-svd) and \( \y = \V^{*}\x \); unitary matrices preserve \( \norm{\cdot}_2 \) (@thm-isometry-characterizations), so \( \norm{\x}_2 = \norm{\y}_2 \) and \( \norm{\A\x}_2 = \norm{\vSigma\y}_2 \). Then
\[
\norm{\vSigma\y}_2^2 = \sum_{i=1}^{n}\sigma_i^2\lvert y_i\rvert^2 \ge \sigma_n^2\sum_{i=1}^{n}\lvert y_i\rvert^2 = \sigma_n^2
\]
for \( \norm{\y}_2 = 1 \), with equality at \( \y = \e_n \), that is at \( \x = \v_n \), the last column of \( \V \). So \( m = \sigma_n \). For the last claim, if \( \A = \U_1\vSigma\V_1^{*} \) then \( \U\A\V = (\U\U_1)\vSigma(\V^{*}\V_1)^{*} \), and a product of unitary matrices is unitary, so this is a singular value decomposition of \( \U\A\V \) with the same \( \vSigma \): unitary factors do not change the singular values. This proves the proposition.
:::

Part (d) is the reason \( \kappa_2 \) is the condition number of choice in theory: it is invariant under the unitary changes of coordinates that Chapters 11 to 13 use throughout, so it is a property of the linear map and not of the basis it is written in.

## What the condition number predicts

The computation that opened the section is now a theorem, together with the version where \( \A \) itself, and not only \( \b \), carries the error. Both halves matter in practice: the entries of \( \A \) are measurements too. Section 5 already proved the two perturbations together, in @thm-perturbed-inverse-bound, and its constant \( \norm{\A}\norm{\A^{-1}} \) is the product we have just named; what is added here is that the first half is sharp on its own, and that it needs no smallness hypothesis at all.

::: {#thm-relative-error-bound}
[Relative Error Under Perturbation of the Data]

Let \( \A \in M_n(\nC) \) be invertible, let \( \b \ne \0 \), and let \( \A\x = \b \).

::: {.enumerate options="label=(\alph*)"}
1. **(Perturbing \( \b \).)** If \( \A\widetilde\x = \b + \Delta\b \), then
   \[
   \frac{\norm{\widetilde\x - \x}}{\norm{\x}} \le \kappa(\A)\,\frac{\norm{\Delta\b}}{\norm{\b}} ,
   \]
   and there are \( \b \) and \( \Delta\b \) for which equality holds.
2. **(Perturbing \( \A \).)** Let \( \E \in M_n(\nC) \) with \( r \coloneqq \kappa(\A)\norm{\E}/\norm{\A} < 1 \). Then \( \A + \E \) is invertible; and if \( (\A + \E)\widetilde\x = \b \), then
   \[
   \frac{\norm{\widetilde\x - \x}}{\norm{\widetilde\x}} \le \kappa(\A)\,\frac{\norm{\E}}{\norm{\A}},
   \qquad
   \frac{\norm{\widetilde\x - \x}}{\norm{\x}} \le \frac{r}{1 - r} .
   \]
:::
:::

::: {.idea}
For (a), the displayed computation at the head of the section, plus a choice of the two vectors that makes both inequalities in it equalities — and both are attained, because @lem-operator-norm-attained says an operator norm is a maximum and not a supremum. For (b), factor \( \A + \E = \A(\I + \A^{-1}\E) \) so that @thm-neumann-series decides invertibility, then subtract the two equations. Subtracting gives \( \widetilde\x - \x \) in terms of \( \widetilde\x \), which is why the clean bound is relative to \( \widetilde\x \); subadditivity of the norm converts it to a bound relative to \( \x \) at the cost of the factor \( 1/(1-r) \), and that factor is where "to first order" hides.
:::

::: {.proof}
*(a).* Subtracting \( \A\x = \b \) from \( \A\widetilde\x = \b + \Delta\b \) gives \( \A(\widetilde\x - \x) = \Delta\b \), so \( \widetilde\x - \x = \A^{-1}\Delta\b \) and \( \norm{\widetilde\x - \x} \le \norm{\A^{-1}}\norm{\Delta\b} \) by @thm-operator-norm-properties (a). Also \( \norm{\b} = \norm{\A\x} \le \norm{\A}\norm{\x} \), and \( \x \ne \0 \) because \( \b \ne \0 \), so \( 1/\norm{\x} \le \norm{\A}/\norm{\b} \). Multiplying the two estimates,
\[
\frac{\norm{\widetilde\x - \x}}{\norm{\x}}
\le \norm{\A^{-1}}\norm{\Delta\b}\cdot\frac{\norm{\A}}{\norm{\b}}
= \kappa(\A)\frac{\norm{\Delta\b}}{\norm{\b}} .
\]

For equality, use @lem-operator-norm-attained twice. Choose a unit vector \( \x \) with \( \norm{\A\x} = \norm{\A} \) and put \( \b = \A\x \), so that \( \norm{\b} = \norm{\A}\norm{\x} \) and the second estimate is an equality. Choose a unit vector \( \y \) with \( \norm{\A^{-1}\y} = \norm{\A^{-1}} \) and put \( \Delta\b = \y \), so that the first estimate is an equality. Then
\[
\frac{\norm{\widetilde\x - \x}}{\norm{\x}} \Big/ \frac{\norm{\Delta\b}}{\norm{\b}}
= \frac{\norm{\A^{-1}}}{1}\cdot\frac{\norm{\A}}{1}
= \kappa(\A) .
\]

*(b).* Write \( \A + \E = \A(\I + \A^{-1}\E) \). By @thm-operator-norm-properties (d),
\[
\norm{\A^{-1}\E} \le \norm{\A^{-1}}\norm{\E} = \kappa(\A)\frac{\norm{\E}}{\norm{\A}} = r < 1 ,
\]
so \( \I - (-\A^{-1}\E) \) is invertible by @thm-neumann-series, and \( \A + \E \) is a product of two invertible matrices, hence invertible. (This is the openness of \( \GL_n(F) \) recorded in @cor-invertible-matrices-open, with the radius made explicit.)

Since \( b \ne \0 \) we have \( \widetilde\x = (\A + \E)^{-1}\b \ne \0 \). Subtracting \( \A\x = \b \) from \( (\A + \E)\widetilde\x = \b \) gives \( \A\widetilde\x - \A\x = -\E\widetilde\x \), hence
\[
\widetilde\x - \x = -\A^{-1}\E\widetilde\x,
\qquad
\norm{\widetilde\x - \x} \le \norm{\A^{-1}}\norm{\E}\,\norm{\widetilde\x} = r\,\norm{\widetilde\x},
\]
which is the first bound. For the second, \( \norm{\widetilde\x} \le \norm{\x} + \norm{\widetilde\x - \x} \) since \( \norm{\cdot} \) is subadditive (@def-norm), so \( \norm{\widetilde\x - \x} \le r\norm{\x} + r\norm{\widetilde\x - \x} \); as \( r < 1 \) we may divide by \( 1 - r > 0 \) to get \( \norm{\widetilde\x - \x} \le \frac{r}{1-r}\norm{\x} \). This proves the theorem.
:::

The two bounds in (b) say the same thing differently. The first is exact and needs nothing but invertibility, but it measures the error against the *computed* answer. The second measures it against the true answer, at the cost of the factor \( 1/(1-r) \) — which is \( 1 + r + r^2 + \cdots \), so for a small \( r \) it is \( 1 \) to first order and the two bounds agree. That is all "to first order in the perturbation of \( \A \)" ever means here, and it is now a stated inequality rather than a gesture. Adding the two halves, with the factor \( 1/(1-r) \) covering both, recovers @thm-perturbed-inverse-bound exactly.

::: {.check}
Where in the proof of (a) is the hypothesis \( \b \ne \0 \) used, and what goes wrong without it?
:::

::: {.solution}
It is used to know \( \x \ne \0 \), so that \( \norm{\x} \) may be divided by, and to know \( \norm{\b} \ne 0 \), so that the relative perturbation \( \norm{\Delta\b}/\norm{\b} \) means anything. With \( \b = \0 \) the true solution is \( \x = \0 \) and *every* non-zero \( \Delta\b \) produces an infinite relative error. Relative error is only defined against a non-zero reference.
:::

Now a case where the bound of (a) is not merely an inequality. The point of computing the example exactly is to see that \( \kappa \) is not a pessimistic overestimate manufactured by the inequalities used to reach it: it is achieved.

::: {#exm-ill-conditioned-system}
[A system where the bound is attained]

Let
\[
\A = \begin{pmatrix} 1 & 1 \\ 1 & 1.01 \end{pmatrix},
\qquad
\b = \begin{pmatrix} 2 \\ 2.01 \end{pmatrix},
\]
whose solution is \( \x = (1, 1) \). Compute \( \kappa_{\infty}(\A) \); then perturb \( \b \) to \( \b + \Delta\b \) with \( \Delta\b = (0.01, -0.01) \), solve again, and compare the two relative errors.
:::

::: {.solution}
Work with exact fractions: \( 1.01 = \tfrac{101}{100} \) and \( \det\A = \tfrac{101}{100} - 1 = \tfrac1{100} \), so
\[
\A^{-1} = 100\begin{pmatrix} \tfrac{101}{100} & -1 \\ -1 & 1 \end{pmatrix}
= \begin{pmatrix} 101 & -100 \\ -100 & 100 \end{pmatrix}.
\]
The largest absolute row sums are \( \tfrac{201}{100} \) for \( \A \) and \( 201 \) for \( \A^{-1} \), so by @thm-operator-norm-formulas (b),
\[
\kappa_{\infty}(\A) = \tfrac{201}{100}\cdot 201 = \tfrac{40401}{100} = 404.01 .
\]

Check that \( \A\x = \b \): the two rows give \( 1 + 1 = 2 \) and \( 1 + \tfrac{101}{100} = \tfrac{201}{100} \). Now
\[
\widetilde\x - \x = \A^{-1}\Delta\b
= \tfrac1{100}\begin{pmatrix} 101 + 100 \\ -100 - 100\end{pmatrix}
= \begin{pmatrix} 2.01 \\ -2 \end{pmatrix},
\]
so \( \widetilde\x = (3.01, -1) \). Verify directly: \( 3.01 - 1 = 2.01 \) and \( 3.01 - 1.01 = 2 \), which is \( \b + \Delta\b = (2.01, 2) \).

The two relative errors, in \( \norm{\cdot}_{\infty} \):
\[
\begin{aligned}
\frac{\norm{\Delta\b}_{\infty}}{\norm{\b}_{\infty}}
  &= \frac{1/100}{201/100} = \frac{1}{201} \approx 0.50\%, \\
\frac{\norm{\widetilde\x - \x}_{\infty}}{\norm{\x}_{\infty}}
  &= \frac{201/100}{1} = \frac{201}{100} = 201\% .
\end{aligned}
\]
Their ratio is \( \tfrac{201}{100}\cdot 201 = 404.01 \), which is exactly \( \kappa_{\infty}(\A) \). A perturbation of half a percent in the data has turned the answer \( (1, 1) \) into \( (3.01, -1) \), and the bound of @thm-relative-error-bound (a) is attained, not approached.
:::

Geometrically the example is @lem-inverse-norm-min at work: the two rows of \( \A \) are nearly parallel, so the two lines whose intersection is \( \x \) cross at a very small angle, and moving either line slightly slides the crossing point a long way. Ill-conditioning is that picture, in any dimension.

::: {.warning}
**The condition number bounds the error; it does not produce it.** @thm-relative-error-bound is a worst case over all perturbations \( \Delta\b \) of a given size. A particular \( \Delta\b \) may do far less damage: in the example above, \( \Delta\b = (0.01, 0.01) \) gives \( \widetilde\x - \x = \A^{-1}\Delta\b = (0.01, 0) \), a relative error of \( 1\% \) against a relative perturbation of \( 0.5\% \) — a magnification of \( 2 \), not \( 404 \). A large \( \kappa \) says that *some* direction is dangerous, not that yours is.
:::

## Why the normal equations are worse

Chapter 11 §04 solved the least-squares problem through the normal equations \( \A^{*}\A\x = \A^{*}\b \) (@thm-least-squares), and Chapter 11 §08 then recommended against actually forming that system. Its words were: "The deeper reason to prefer it is not the operation count: forming \( \A^{*}\A \) squares the sensitivity of the problem to rounding, while \( (\dagger) \) never forms that product at all. Chapter 24 makes 'sensitivity' precise and proves the comparison; here we record only the practice." The word "sensitivity" now has a meaning, and the word "squares" is now a theorem.

::: {#thm-normal-equations-squares-conditioning}
[The Normal Equations Square the Condition Number]

Let \( m \ge n \ge 1 \) and let \( \A \in M_{m \times n}(\nC) \) have rank \( n \). Then \( \A^{*}\A \in M_n(\nC) \) is invertible, and
\[
\kappa_2(\A^{*}\A) = \kappa_2(\A)^2 .
\]
:::

::: {.idea}
An SVD of \( \A \) is also, after one multiplication, an eigenvalue decomposition of \( \A^{*}\A \): the singular values get squared and nothing else happens. Both condition numbers are then ratios of the same list of numbers, one list being the squares of the other.
:::

::: {.proof}
Write \( \A = \U\vSigma\V^{*} \) with \( \U \in M_m(\nC) \), \( \V \in M_n(\nC) \) unitary and \( \vSigma \in M_{m \times n}(\nR) \) carrying \( \sigma_1 \ge \dots \ge \sigma_n \ge 0 \) (@thm-svd). Since \( \rank\A = n \), exactly \( n \) singular values are non-zero (@thm-svd), so \( \sigma_n > 0 \). Using \( \U^{*}\U = \I_m \),
\[
\A^{*}\A = \V\vSigma^{*}\U^{*}\U\vSigma\V^{*} = \V(\vSigma^{*}\vSigma)\V^{*},
\qquad
\vSigma^{*}\vSigma = \diag(\sigma_1^2, \dots, \sigma_n^2) .
\]
So \( \A^{*}\A \) is unitarily similar to a diagonal matrix with the positive entries \( \sigma_i^2 \); it is therefore invertible, Hermitian and positive definite, with eigenvalues \( \sigma_1^2 \ge \dots \ge \sigma_n^2 > 0 \).

The singular values of \( \A^{*}\A \) are those same numbers. Indeed the displayed identity *is* a singular value decomposition of \( \A^{*}\A \), with both unitary factors equal to \( \V \) and the diagonal entries already in decreasing order; alternatively, \( (\A^{*}\A)^{*}(\A^{*}\A) = \V\diag(\sigma_i^4)\V^{*} \) has eigenvalues \( \sigma_i^4 \), whose non-negative square roots are the \( \sigma_i^2 \) (@def-singular-values). Hence by @def-condition-number and @prp-condition-number-properties (d),
\[
\kappa_2(\A^{*}\A) = \frac{\sigma_1^2}{\sigma_n^2} = \Bigl(\frac{\sigma_1}{\sigma_n}\Bigr)^{2} = \kappa_2(\A)^2 .
\]
This proves the theorem.
:::

::: {#exm-normal-equations-squaring}
[Squaring, on a \( 3 \times 2 \) example]

Let \( \A = \begin{pmatrix} 1 & 1 \\ 0.1 & 0 \\ 0 & 0.1 \end{pmatrix} \). Compute \( \kappa_2(\A) \) and \( \kappa_2(\A\tp\A) \).
:::

::: {.solution}
\( \A\tp\A = \begin{psmallmatrix} 1.01 & 1 \\ 1 & 1.01 \end{psmallmatrix} \). It sends \( (1, 1) \) to \( 2.01\,(1,1) \) and \( (1, -1) \) to \( 0.01\,(1,-1) \), so its eigenvalues are \( \tfrac{201}{100} \) and \( \tfrac1{100} \). Hence \( \sigma_1(\A) = \sqrt{201}/10 \) and \( \sigma_2(\A) = 1/10 \), so
\[
\kappa_2(\A) = \sqrt{201} \approx 14.18,
\qquad
\kappa_2(\A\tp\A) = \frac{201/100}{1/100} = 201 = \bigl(\sqrt{201}\bigr)^2 .
\]
A matrix whose conditioning is unremarkable becomes, on forming \( \A\tp\A \), a matrix whose conditioning is fourteen times worse.
:::

**What is proved here, and what is not.** @thm-normal-equations-squares-conditioning is a statement about matrices: the matrix one *forms* when one writes down the normal equations has the square of the condition number of the matrix one started with. Combined with @thm-relative-error-bound, it says that the linear system \( \A^{*}\A\x = \A^{*}\b \), considered as a problem in its own data, is more sensitive than \( \A \) itself by a factor \( \kappa_2(\A) \) — and the \( \Q\R \) route \( \R\x = \Q^{*}\b \) of Chapter 11 §08 never forms \( \A^{*}\A \), so it never incurs that factor. Indeed the triangular matrix it does solve with is no worse conditioned than \( \A \): from \( \A = \Q\R \) with \( \Q^{*}\Q = \I_n \) (@thm-qr-factorization) we get \( \A^{*}\A = \R^{*}\Q^{*}\Q\R = \R^{*}\R \), so \( \A \) and \( \R \) have the same singular values (@def-singular-values) and \( \kappa_2(\R) = \kappa_2(\A) \) exactly.

Three things are *not* proved here, and all three belong to Chapter 24.

- **The conditioning of the least-squares problem itself** is not \( \kappa_2(\A) \). The map \( \b \mapsto \x^{+} \) from data to least-squares solution has a sensitivity that depends on \( \kappa_2(\A) \), on the residual \( \norm{\A\x^{+} - \b} \) and on the angle between \( \b \) and \( \col(\A) \); when the residual is large, a term in \( \kappa_2(\A)^2 \) appears even for the QR route. The bound above is about the *linear systems being solved*, not about the underlying fitting problem.
- **Nothing here is about arithmetic.** A condition number describes a problem, and an error bound of the form "relative error \( \le \kappa \cdot \) (relative perturbation)" only becomes a statement about a computation once one knows how large a perturbation the computation itself introduces. That requires a model of floating-point arithmetic and a backward error analysis, neither of which exists in this book yet.
- **Hence the comparison of the two algorithms** — that a stable implementation of the QR route loses about \( \log_{10}\kappa_2(\A) \) decimal digits while forming and solving the normal equations loses about \( 2\log_{10}\kappa_2(\A) \) — is still Chapter 24's to prove. What this section supplies is the number that appears in both statements, and the reason a square appears in one of them.

## Conditioning is a property of the problem

This is the last warning of the chapter, and it is the one readers most often need.

::: {.warning}
**Conditioning belongs to the problem; stability belongs to the algorithm.** \( \kappa(\A) \) is computed from \( \A \) alone. It knows nothing about how anyone intends to solve \( \A\x = \b \), and it does not change if the method changes. Two consequences, both regularly got wrong:

- **A large \( \kappa(\A) \) does not mean a computed answer is wrong.** It means that the answer is not determined to high relative accuracy by data of limited accuracy — a statement about the information available, not about the arithmetic performed. If the data are exact and the arithmetic is exact, the answer is exact however large \( \kappa \) is. And even in inexact arithmetic, a good algorithm returns the exact answer to a problem whose data differ from yours by a rounding error, which is the most anyone can ask of it.
- **A small \( \kappa(\A) \) does not make an algorithm trustworthy.** An unstable method can wreck a perfectly conditioned problem all by itself, by introducing errors far larger than the data warrant; @exr-condition-numbers-c3 gives an elementary example in which \( \kappa_{\infty} \) is below \( 5 \) and a computed coordinate comes out as \( 0 \) instead of \( 1 \).

Chapter 24 draws the distinction properly, defines backward stability, and proves which of the algorithms in this book have it. Until then, read \( \kappa \) as an upper bound on what any method can promise, and never as a verdict on a particular answer.
:::

## What this chapter has settled

Nine chapters wrote promissory notes that only a norm could pay. Here is the ledger, with the section that closed each entry.

- **Chapter 11 §01** said that not every norm comes from an inner product and that the parallelogram law is the test. Section 1 proved it, in @thm-parallelogram-characterization, building on the \( \nR^2 \) case of @exr-inner-products-c1.
- **Chapter 10 §10** promised that this chapter would prove \( \rho(\A) \le \norm{\A} \) for the norm induced by any vector norm, and would recover \( \rho(\A) \) as a limit built from the norms of the powers. Section 4 did both: @thm-spectral-radius-le-norm and Gelfand's formula @thm-gelfand. The same section also gave \( \rho \) the labeled definition @def-spectral-radius that Chapter 10 used only in prose, and @cor-powers-converge-iff-rho-lt-one restored Chapter 10's convergence criterion with a rate attached. And Chapter 10's entrywise convergence turned out to be *the* convergence, by @cor-entrywise-convergence-is-the-convergence.
- **Chapter 13 §08 and §12** asked, twice, for a name for \( \max\{\norm{\A\x} : \norm{\x} = 1\} \). Section 3 supplied it — @def-operator-norm — and separated the name from the computation \( \norm{\A}_2 = \sigma_1(\A) \), which is @thm-operator-norm-formulas (c); @exm-oblique-projection-norm measured Chapter 13 §12's oblique projection. The spectral norm that Chapter 13 §10 needed in order even to *state* the second half of its approximation theorem now exists; the theorem itself waits for Chapter 17, which proves it from the min–max description of the singular values. The version covering every unitarily invariant norm at once is Chapter 21's.
- **Chapter 10 §09** promised a return to \( e^{\A} \) with norms available, giving quantitative bounds in place of exact formulas. Section 6 gave them, in @thm-exponential-norm-bound, and its @thm-exponential-decay is the statement Chapter 12 §10 pointed at when it said that the consequence of stability for \( \dot\x = \A\x \) belonged to Chapter 16.
- **Chapter 12 §01** said that this chapter, "where matrices acquire norms and limits can be spoken of properly, runs arguments of exactly this shape". Section 7 ran one: @cor-diagonalizable-dense-again and @cor-identity-by-density turn "prove it for diagonalizable matrices, then take a limit" into three lines, and @exm-cayley-hamilton-by-density is the demonstration.
- **Chapter 11 §08** deferred its reason for preferring \( \Q\R \) to the normal equations. @thm-normal-equations-squares-conditioning supplies the matrix half of it; the arithmetic half is Chapter 24's, as listed above.

What the chapter has *not* done is equally worth recording. It has not bounded how far an individual eigenvalue moves under a perturbation — @exm-jordan-block-perturbation shows there is no bound of the obvious kind, and the bounds that do exist, Weyl's and Bauer–Fike's, are Chapters 17 and 20. It has not said which norms are invariant under unitary multiplication, which is Chapter 21. And it has not touched arithmetic. The condition number is the bridge to that last subject: it is the exact point at which linear algebra stops and numerical analysis begins.

## Exercises

### A. Check your understanding

:::: {#exr-condition-numbers-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define \( \kappa(\A) \), naming what it depends on besides \( \A \).
2. Explain why \( \kappa(\A) \ge 1 \) for every invertible \( \A \).
3. Decide whether each statement is correct, and justify: (i) "if \( \kappa(\A) = 10^{8} \) then any computed solution of \( \A\x = \b \) has at most a few correct digits"; (ii) "if \( \kappa(\A) \) is small then any method of solving \( \A\x = \b \) is reliable".
4. State what \( \kappa_2(\A^{*}\A) \) is in terms of \( \kappa_2(\A) \), and say what that has to do with the \( \Q\R \) factorization.
:::
::::

::: {.solution}
(a) See @def-condition-number: \( \kappa(\A) = \norm{\A}\norm{\A^{-1}} \), with \( \kappa(\A) = \infty \) for singular \( \A \). Besides \( \A \) it depends on the **choice of vector norm**, through the operator norm it induces; \( \kappa_1 \), \( \kappa_2 \) and \( \kappa_{\infty} \) are three different numbers.

(b) \( 1 = \norm{\I} = \norm{\A\A^{-1}} \le \norm{\A}\norm{\A^{-1}} \), by @thm-operator-norm-properties (c) and (d). See @prp-condition-number-properties (a).

(c) (i) Incorrect. \( \kappa \) bounds the effect of a perturbation of the data; with exact data and exact arithmetic the answer is exact. It says that the answer *cannot be determined* to high relative accuracy from inaccurate data, which is a statement about the problem, not a verdict on a computed answer. (ii) Incorrect. Conditioning is a property of the problem and stability a property of the algorithm; a small \( \kappa \) leaves an unstable method free to introduce errors of its own.

(d) \( \kappa_2(\A^{*}\A) = \kappa_2(\A)^2 \) for \( \A \) of full column rank (@thm-normal-equations-squares-conditioning). The normal equations form \( \A^{*}\A \) and so solve a system with the squared condition number, while the route \( \R\x = \Q^{*}\b \) of Chapter 11 §08 never forms that product and keeps \( \kappa_2(\R) = \kappa_2(\A) \).
:::

### B. Practice

:::: {#exr-condition-numbers-b1}
[B1: Three condition numbers]

For \( \A = \begin{pmatrix} 3 & 0 \\ 0 & -\tfrac12 \end{pmatrix} \) and \( \B = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \), compute \( \kappa_{\infty} \) and \( \kappa_2 \) of each. *Hint: \( \B^{*}\B \) has trace \( 6 \) and determinant \( 1 \).*
::::

::: {.solution}
\( \A^{-1} = \diag(\tfrac13, -2) \). Largest absolute row sums: \( 3 \) for \( \A \), \( 2 \) for \( \A^{-1} \), so \( \kappa_{\infty}(\A) = 6 \) by @thm-operator-norm-formulas (b). For \( \kappa_2 \): \( \A^{*}\A = \diag(9, \tfrac14) \), so \( \sigma_1 = 3 \), \( \sigma_2 = \tfrac12 \) and \( \kappa_2(\A) = 6 \) by @prp-condition-number-properties (d). The two agree here because \( \A \) is diagonal.

\( \B^{-1} = \begin{psmallmatrix} 1 & -2 \\ 0 & 1\end{psmallmatrix} \), and both have largest absolute row sum \( 3 \), so \( \kappa_{\infty}(\B) = 9 \). For \( \kappa_2 \): \( \B^{*}\B = \begin{psmallmatrix} 1 & 2 \\ 2 & 5\end{psmallmatrix} \) has trace \( 6 \) and determinant \( 1 \), so its eigenvalues are \( 3 \pm 2\sqrt2 \), giving
\[
\kappa_2(\B) = \sqrt{\frac{3 + 2\sqrt2}{3 - 2\sqrt2}} = 3 + 2\sqrt2 \approx 5.828 ,
\]
using \( (3 - 2\sqrt2)(3 + 2\sqrt2) = 1 \), so that the ratio is \( (3 + 2\sqrt2)^2 \).
:::

:::: {#exr-condition-numbers-b2}
[B2: A perturbation, measured against the bound]

Let \( \A = \begin{pmatrix} 1 & 1 \\ 1 & 1.01\end{pmatrix} \) and \( \b = (2, 2.01) \) as in @exm-ill-conditioned-system, and take \( \Delta\b = (0, 0.01) \).

::: {.enumerate options="label=(\alph*)"}
1. Solve \( \A\widetilde\x = \b + \Delta\b \) exactly.
2. Compute both relative errors in \( \norm{\cdot}_{\infty} \) and the factor between them, and compare with \( \kappa_{\infty}(\A) = 404.01 \).
:::
::::

::: {.solution}
(a) With \( \A^{-1} = \begin{psmallmatrix} 101 & -100 \\ -100 & 100\end{psmallmatrix} \) from @exm-ill-conditioned-system and \( \Delta\b = (0, \tfrac1{100}) \),
\[
\widetilde\x - \x = \A^{-1}\Delta\b = \begin{pmatrix} -1 \\ 1 \end{pmatrix},
\qquad
\widetilde\x = \begin{pmatrix} 0 \\ 2 \end{pmatrix}.
\]
Check: \( 0 + 2 = 2 \) and \( 0 + 2\cdot\tfrac{101}{100} = \tfrac{202}{100} = 2.02 = \b + \Delta\b \) in the second coordinate.

(b) \( \norm{\Delta\b}_{\infty}/\norm{\b}_{\infty} = \tfrac{1/100}{201/100} = \tfrac1{201} \), and \( \norm{\widetilde\x - \x}_{\infty}/\norm{\x}_{\infty} = 1 \). The factor is \( 201 \), which is below \( \kappa_{\infty}(\A) = 404.01 \) by a factor of about \( 2 \). The bound holds, as @thm-relative-error-bound (a) requires, and is not attained: this \( \Delta\b \) is not the worst direction, which @exm-ill-conditioned-system found.
:::

:::: {#exr-condition-numbers-b3}
[B3: Squaring, again]

Let \( \A = \begin{pmatrix} 1 & 0 \\ 0 & \tfrac12 \\ 0 & 0\end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Compute the singular values of \( \A \) and \( \kappa_2(\A) \).
2. Compute \( \A\tp\A \) and \( \kappa_2(\A\tp\A) \) directly, and confirm @thm-normal-equations-squares-conditioning.
3. Does \( \kappa_{\infty} \) also square? Compute \( \kappa_{\infty}(\A\tp\A) \) and compare with \( \kappa_{\infty} \) of the square matrix \( \begin{psmallmatrix}1 & 0\\ 0 & \frac12\end{psmallmatrix} \).
:::
::::

::: {.solution}
(a) \( \A\tp\A = \diag(1, \tfrac14) \), whose eigenvalues are \( 1 \) and \( \tfrac14 \); so \( \sigma_1(\A) = 1 \), \( \sigma_2(\A) = \tfrac12 \) and \( \kappa_2(\A) = 2 \).

(b) \( \A\tp\A = \diag(1, \tfrac14) \) is diagonal with positive entries, so its singular values are \( 1 \) and \( \tfrac14 \) and \( \kappa_2(\A\tp\A) = 4 = 2^2 = \kappa_2(\A)^2 \), as @thm-normal-equations-squares-conditioning says.

(c) For a diagonal matrix every \( \kappa_p \) is the ratio of the largest to the smallest modulus on the diagonal, so \( \kappa_{\infty}(\A\tp\A) = 4 \) while \( \kappa_{\infty}(\diag(1, \tfrac12)) = 2 \); here the squaring happens in \( \kappa_{\infty} \) too. It does not in general: @thm-normal-equations-squares-conditioning is stated for \( \kappa_2 \), and the proof uses singular values, which only \( \norm{\cdot}_2 \) sees. @exr-condition-numbers-c1 bounds how far the other condition numbers can stray.
:::

### C. Going deeper

:::: {#exr-condition-numbers-c1}
[C1: Changing the norm changes \( \kappa \), but not much]

Let \( \norm{\cdot}_a \) and \( \norm{\cdot}_b \) be norms on \( \nC^n \) with \( c\norm{\v}_b \le \norm{\v}_a \le C\norm{\v}_b \) for all \( \v \), as supplied by @thm-norm-equivalence, and write \( \kappa_a, \kappa_b \) for the corresponding condition numbers.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \norm{\A}_a \le (C/c)\norm{\A}_b \) for every \( \A \in M_n(\nC) \).
2. Deduce that \( \kappa_a(\A) \le (C/c)^2\kappa_b(\A) \) and \( \kappa_b(\A) \le (C/c)^2\kappa_a(\A) \) for every invertible \( \A \).
3. Using \( \norm{\v}_{\infty} \le \norm{\v}_2 \le \sqrt n\,\norm{\v}_{\infty} \), bound \( \kappa_2 \) in terms of \( \kappa_{\infty} \) for \( n = 2 \), and check the bound on the matrix \( \B = \begin{psmallmatrix} 1 & 2 \\ 0 & 1\end{psmallmatrix} \) of @exr-condition-numbers-b1.
:::
::::

::: {.solution}
(a) Let \( \x \ne \0 \). Then
\[
\frac{\norm{\A\x}_a}{\norm{\x}_a}
\le \frac{C\norm{\A\x}_b}{c\norm{\x}_b}
\le \frac{C}{c}\,\norm{\A}_b ,
\]
using the two inequalities and @thm-operator-norm-properties (a) for \( \norm{\cdot}_b \). Taking the maximum over \( \x \ne \0 \), which is \( \norm{\A}_a \) by @def-operator-norm and homogeneity, gives the claim.

(b) Apply (a) to \( \A \) and to \( \A^{-1} \) and multiply: \( \kappa_a(\A) = \norm{\A}_a\norm{\A^{-1}}_a \le (C/c)^2\norm{\A}_b\norm{\A^{-1}}_b = (C/c)^2\kappa_b(\A) \). The reverse follows by symmetry, since the hypothesis also reads \( C^{-1}\norm{\v}_a \le \norm{\v}_b \le c^{-1}\norm{\v}_a \), whose ratio of constants is again \( C/c \).

(c) With \( \norm{\cdot}_a = \norm{\cdot}_2 \) and \( \norm{\cdot}_b = \norm{\cdot}_{\infty} \), we have \( c = 1 \) and \( C = \sqrt n = \sqrt2 \), so \( \kappa_2(\A) \le 2\kappa_{\infty}(\A) \) and \( \kappa_{\infty}(\A) \le 2\kappa_2(\A) \). For \( \A = \begin{psmallmatrix}1&2\\0&1\end{psmallmatrix} \): \( \kappa_2 = 3 + 2\sqrt2 \approx 5.83 \) and \( \kappa_{\infty} = 9 \), and indeed \( 5.83 \le 18 \) and \( 9 \le 11.66 \). Both bounds hold, with room to spare; the point is only that no choice of norm can turn a well-conditioned matrix into an ill-conditioned one.
:::

:::: {#exr-condition-numbers-c2}
[C2: The condition number is the reciprocal distance to singularity]

Let \( \A \in M_n(\nC) \) be invertible.

::: {.enumerate options="label=(\alph*)"}
1. Prove that every singular \( \B \in M_n(\nC) \) satisfies
   \[
   \frac{\norm{\A - \B}}{\norm{\A}} \ge \frac{1}{\kappa(\A)} .
   \]
2. For the \( 2 \)-norm, prove that equality is achieved: exhibit a singular \( \B \) with \( \norm{\A - \B}_2 = \sigma_n(\A) \). *Hint: use a singular value decomposition and delete one term.*
3. Hence interpret \( 1/\kappa_2(\A) \) in one sentence, and say what it gives for the matrix of @exm-ill-conditioned-system.
:::
::::

::: {.solution}
(a) Put \( \E = \B - \A \), so \( \A + \E = \B \) is singular. If \( \norm{\A^{-1}\E} < 1 \) then \( \A + \E = \A(\I + \A^{-1}\E) \) would be invertible, by @thm-neumann-series and the fact that a product of invertible matrices is invertible; so \( \norm{\A^{-1}\E} \ge 1 \). By @thm-operator-norm-properties (d), \( 1 \le \norm{\A^{-1}}\norm{\E} \), that is \( \norm{\E} \ge 1/\norm{\A^{-1}} \). Dividing by \( \norm{\A} \),
\[
\frac{\norm{\A - \B}}{\norm{\A}} = \frac{\norm{\E}}{\norm{\A}} \ge \frac{1}{\norm{\A}\,\norm{\A^{-1}}} = \frac{1}{\kappa(\A)} .
\]

(b) Let \( \A = \U\vSigma\V^{*} \) (@thm-svd) with \( \vSigma = \diag(\sigma_1, \dots, \sigma_n) \), and put
\[
\B = \U\,\diag(\sigma_1, \dots, \sigma_{n-1}, 0)\,\V^{*} .
\]
Then \( \B \) is singular, since \( \diag(\sigma_1, \dots, \sigma_{n-1}, 0) \) is and \( \U, \V \) are invertible; and \( \A - \B = \U\,\diag(0, \dots, 0, \sigma_n)\,\V^{*} \), whose singular values are those of \( \diag(0, \dots, 0, \sigma_n) \) — for any \( \M \), \( (\U\M\V^{*})^{*}(\U\M\V^{*}) = \V\M^{*}\M\V^{*} \) is similar to \( \M^{*}\M \), so unitary factors leave the singular values alone, invertible or not — the largest of them being \( \sigma_n \); so \( \norm{\A - \B}_2 = \sigma_n \) by @thm-operator-norm-formulas (c). Since \( \norm{\A}_2 = \sigma_1 \), the ratio is \( \sigma_n/\sigma_1 = 1/\kappa_2(\A) \), matching (a) with equality.

(c) \( 1/\kappa_2(\A) \) is the relative distance, in the \( 2 \)-norm, from \( \A \) to the nearest singular matrix. For \( \A = \begin{psmallmatrix} 1 & 1 \\ 1 & 1.01\end{psmallmatrix} \), whose \( \kappa_2 \) is the ratio of the eigenvalues \( (201 \pm \sqrt{40001})/200 \) of the symmetric \( \A \), one gets \( \kappa_2(\A) \approx 402.0 \), so a relative perturbation of about \( 0.25\% \) suffices to make \( \A \) singular. Ill-conditioned means *nearly singular*, in exactly this quantitative sense.
:::

:::: {#exr-condition-numbers-c3}
[C3: A well-conditioned problem and a bad method]

Consider the two-by-two system
\[
\begin{aligned}
10^{-15}x_1 + x_2 &= 1, \\
x_1 + x_2 &= 2 ,
\end{aligned}
\]
with coefficient matrix \( \A = \begin{psmallmatrix} 10^{-15} & 1 \\ 1 & 1\end{psmallmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \kappa_{\infty}(\A) < 5 \), so that the problem is well conditioned.
2. Solve the system exactly.
3. Eliminate \( x_1 \) using the **first** equation as the pivot row, rounding every intermediate quantity to \( 12 \) significant decimal digits, and compare the result with (b). Then do the same after exchanging the two equations, and say what the exchange achieved.
4. What does this show about the relationship between \( \kappa(\A) \) and the accuracy of a computed answer?
:::
::::

::: {.solution}
(a) Write \( \varepsilon = 10^{-15} \). Then \( \det\A = \varepsilon - 1 \ne 0 \) and
\[
\A^{-1} = \frac{1}{\varepsilon - 1}\begin{pmatrix} 1 & -1 \\ -1 & \varepsilon\end{pmatrix} .
\]
The largest absolute row sum of \( \A \) is \( 2 \), and that of \( \A^{-1} \) is \( 2/(1 - \varepsilon) \), so by @thm-operator-norm-formulas (b),
\[
\kappa_{\infty}(\A) = \frac{4}{1 - \varepsilon} < 5 .
\]

(b) Subtracting the first equation from the second gives \( (1 - \varepsilon)x_1 = 1 \), so
\[
x_1 = \frac{1}{1 - \varepsilon} = 1 + 10^{-15} + \dots,
\qquad
x_2 = 1 - \varepsilon x_1 = \frac{1 - 2\varepsilon}{1 - \varepsilon} = 1 - 10^{-15} + \dots .
\]
Both coordinates are \( 1 \) to fourteen decimal places.

(c) *Without the exchange.* The multiplier is \( 1/\varepsilon = 10^{15} \), and the second equation becomes
\[
(1 - 10^{15})x_2 = 2 - 10^{15} .
\]
Both sides need fifteen significant digits to be recorded exactly, so at twelve digits both round to \( -1.00000000000 \times 10^{15} \), and the computed \( x_2 \) is exactly \( 1 \) — accurate, as it happens. Back-substitution into the first equation then gives
\[
x_1 = \frac{1 - x_2}{\varepsilon} = \frac{0}{10^{-15}} = 0 ,
\]
against a true value of \( 1 + 10^{-15} \): every digit is wrong. The damage was done by subtracting two numbers that agree in all twelve retained digits, so that the difference retains none of them.

*With the exchange.* Pivoting on \( x_1 + x_2 = 2 \), the multiplier is \( \varepsilon = 10^{-15} \) and the second equation becomes \( (1 - \varepsilon)x_2 = 1 - 2\varepsilon \). At twelve digits both coefficients round to \( 1.00000000000 \), giving \( x_2 = 1.00000000000 \), and back-substitution gives \( x_1 = 2 - x_2 = 1.00000000000 \). Both agree with (b) to all twelve digits. The exchange achieved one thing: it made the multiplier at most \( 1 \) in modulus, so nothing in the elimination was amplified, and no large quantity was ever created to be subtracted from a comparable one. This is why every practical elimination scheme chooses the largest available pivot.

(d) The conditioning of the problem is excellent, \( \kappa_{\infty}(\A) < 5 \), and it is the same for both computations, since it does not mention a method. Yet one method returns \( (0, 1) \) and the other returns the right answer. Conditioning bounds what *any* method can promise; whether a given method keeps that promise is stability, and it is Chapter 24's subject.
:::
