# Least Squares and Minimum-Norm Solutions

Chapter 2 taught us to decide whether \( \A\x = \b \) has a solution, and to find them all when it does. Real data rarely cooperates. Measure a quantity that depends linearly on two unknowns, take ten measurements, and you have ten equations in two unknowns; each measurement carries a little error, and the ten equations are almost certainly inconsistent. Refusing to answer is not useful. This section replaces the question "which \( \x \) solves \( \A\x = \b \)?" with "which \( \x \) comes closest?", and shows that the new question always has an answer, computed by solving a square system.

The other half of the section handles the opposite complaint. When a system is consistent but underdetermined, there are too many solutions, and we want a canonical one. Orthogonality picks it: exactly one solution is perpendicular to the kernel, and it is the shortest.

Throughout, \( F = \nR \) or \( F = \nC \), and \( F^n \) and \( F^m \) carry the standard inner product \( \inner{\x}{\y} = \sum_i x_i\conj{y_i} \), with \( \norm{\x}^2 = \sum_i |x_i|^2 \).

## The residual, and a piece of notation

Given \( \A \in M_{m \times n}(F) \) and \( \b \in F^m \), write \( \r = \b - \A\x \) for the **residual** of a candidate \( \x \). The system is consistent exactly when some \( \x \) makes \( \r = \0 \). When none does, we ask for the \( \x \) making \( \r \) as short as possible, that is, minimizing
\[
\norm{\A\x - \b}^2 = \sum_{i=1}^{m} \bigl| (\A\x)_i - b_i \bigr|^2 ,
\]
a **sum of squares**; hence the name **least squares**.

Two observations turn this into geometry. First, as \( \x \) ranges over \( F^n \), the vector \( \A\x \) ranges over exactly the column space \( \col(\A) \subseteq F^m \) (@thm-matrix-times-vector-columns), a finite-dimensional subspace. Second, minimizing \( \norm{\A\x - \b} \) over all \( \x \) is therefore the same as finding the point of \( \col(\A) \) nearest to \( \b \). We already know that point: it is \( P_{\col(\A)}\b \), by @thm-best-approximation. All that remains is to turn "the residual is perpendicular to \( \col(\A) \)" into equations, and for that we need one piece of notation.

Recall the conjugate transpose \( \A^{*} \in M_{n \times m}(F) \) of @def-conjugate-transpose: the matrix with entries \( (\A^{*})_{ij} = \conj{a_{ji}} \), obtained by transposing and then conjugating every entry, so that \( \A^{*} = \A\tp \) over \( \nR \). Comparing entries and using @thm-transpose-properties together with the rules for conjugation (@thm-conjugate-properties) gives
\[
(\A + \B)^{*} = \A^{*} + \B^{*}, \quad (c\A)^{*} = \conj{c}\,\A^{*}, \quad (\A\B)^{*} = \B^{*}\A^{*}, \quad \A^{**} = \A ,
\]
whenever the sizes match. The third is the one worth seeing done: \( ((\A\B)^{*})_{ij} = \conj{(\A\B)_{ji}} = \conj{\sum_k a_{jk}b_{ki}} = \sum_k \conj{b_{ki}}\,\conj{a_{jk}} = \sum_k (\B^{*})_{ik}(\A^{*})_{kj} = (\B^{*}\A^{*})_{ij} \), which is where the order reverses. The one consequence we really use is the following.

::: {#lem-conjugate-transpose-pairing}
[Moving a matrix across the inner product]

Let \( \A \in M_{m \times n}(F) \). Then for all \( \x \in F^n \) and \( \y \in F^m \),
\[
\inner{\A\x}{\y} = \inner{\x}{\A^{*}\y}, \qquad \inner{\y}{\A\x} = \inner{\A^{*}\y}{\x} .
\]
:::

::: {.proof}
Regarding vectors as columns, \( \inner{\u}{\w} = \w^{*}\u \), a \( 1 \times 1 \) matrix identified with its entry. Hence
\[
\inner{\A\x}{\y} = \y^{*}(\A\x) = (\y^{*}\A)\x = \bigl((\A^{*}\y)^{*}\bigr)\x = \inner{\x}{\A^{*}\y},
\]
where the third equality uses \( (\A^{*}\y)^{*} = \y^{*}\A^{**} = \y^{*}\A \). The second identity follows by conjugating the first, since \( \inner{\y}{\A\x} = \conj{\inner{\A\x}{\y}} \) and \( \conj{\inner{\x}{\A^{*}\y}} = \inner{\A^{*}\y}{\x} \).
:::

The lemma is the matrix case of a general principle: *to move a map across an inner product, pay with its adjoint.* Section 6 develops that principle for linear maps between abstract inner product spaces; here the two lines above are all we need.

## The normal equations

:::: {#thm-least-squares}
[Least Squares Theorem]

Let \( \A \in M_{m \times n}(F) \) and \( \b \in F^m \), and write \( U = \col(\A) \). For \( \x \in F^n \), the following are equivalent:

::: {.enumerate options="label=(\alph*)"}
1. \( \norm{\A\x - \b} \le \norm{\A\z - \b} \) for every \( \z \in F^n \);
2. \( \A\x = P_U\b \);
3. \( \A^{*}\A\x = \A^{*}\b \).
:::

Moreover such an \( \x \) always exists. A vector satisfying these conditions is called a **least-squares solution** of \( \A\x = \b \), and the equations in (c) are the **normal equations**.
::::

::: {.idea}
Condition (a) is a minimization over \( \x \); condition (b) is the same minimization rewritten in \( F^m \), where @thm-best-approximation has already solved it. So (a) \( \Leftrightarrow \) (b) is a translation, not an argument. The content is (b) \( \Leftrightarrow \) (c): saying \( \A\x = P_U\b \) is the same as saying the residual is perpendicular to \( U \), and "perpendicular to every column of \( \A \)" is what \( \A^{*}(\b - \A\x) = \0 \) says. Existence is free, because \( P_U\b \) lies in \( U = \col(\A) \) and so is \( \A\x \) for some \( \x \).
:::

::: {.proof}
Since \( \{ \A\z : \z \in F^n \} = \col(\A) = U \) (@thm-matrix-times-vector-columns), condition (a) says that \( \A\x \) is a vector of \( U \) at least as close to \( \b \) as every other vector of \( U \). By @thm-best-approximation the unique such vector is \( P_U\b \). Hence (a) \( \Leftrightarrow \) (b).

(b) \( \Leftrightarrow \) (c). Write \( \b = P_U\b + (\b - P_U\b) \), the splitting of @thm-orthogonal-decomposition (a) with \( \b - P_U\b \in U^{\perp} \). For \( \x \in F^n \) we have \( \A\x \in U \), so \( \b - \A\x \in U^{\perp} \) holds if and only if \( \A\x \) is the \( U \)-part of \( \b \), that is, if and only if \( \A\x = P_U\b \). It remains to see that
\[
\b - \A\x \in U^{\perp} \iff \A^{*}\A\x = \A^{*}\b .
\]
Put \( \r = \b - \A\x \). By @prp-orthogonal-complement-subspace, \( \r \in U^{\perp} \) if and only if \( \r \) is orthogonal to every \( \A\z \), and by @lem-conjugate-transpose-pairing,
\[
\inner{\r}{\A\z} = \inner{\A^{*}\r}{\z} \qquad \text{for every } \z \in F^n .
\]
If \( \A^{*}\r = \0 \), all these vanish. Conversely, if all vanish, take \( \z = \A^{*}\r \) to get \( \inner{\A^{*}\r}{\A^{*}\r} = 0 \), hence \( \A^{*}\r = \0 \) by positive definiteness. So \( \r \in U^{\perp} \) if and only if \( \A^{*}\r = \0 \), which rearranges to \( \A^{*}\A\x = \A^{*}\b \).

*Existence.* \( P_U\b \in U = \col(\A) \), so \( P_U\b = \A\x \) for some \( \x \in F^n \), and that \( \x \) satisfies (b).
:::

Three things are worth extracting. The normal equations are a **square** \( n \times n \) system, whatever the shape of \( \A \). They are **always consistent**, by the existence clause, even when \( \A\x = \b \) is not. And the minimizing *value* \( \A\x \) is unique — it is \( P_U\b \) — even if the minimizing \( \x \) is not.

::: {.warning}
**"Closest" is measured by the inner product, so the answer moves when the inner product does.** Least squares is not a coordinate-free notion: it minimizes \( \norm{\A\x - \b} \) for a particular norm on \( F^m \), and rescaling one coordinate — reporting one measurement in centimeters instead of meters, say — is a change of inner product. Concretely, for the data \( (0, 2), (1, 1), (2, 8) \) the least-squares line is \( y = \tfrac23 + 3t \); if the middle point is trusted twice as much, so that the second coordinate of \( F^3 \) is weighted by \( 2 \), the best line becomes \( y = 3t \). Both are correct answers to their own question, and Exercise C1 works the general case out. Before fitting, decide which errors count equally.
:::

::: {.check}
The system \( \A\x = \b \) may have no solution at all, yet the normal equations \( \A^{*}\A\x = \A^{*}\b \) always have one. Where does the proof arrange that, and what stops the same argument from solving \( \A\x = \b \) itself?
:::

::: {.solution}
The existence clause uses that \( P_U\b \) lies in \( U = \col(\A) \), and every vector of \( \col(\A) \) is \( \A\x \) for some \( \x \). So the normal equations ask \( \A\x \) to hit \( P_U\b \), a target that is inside the column space by construction. The original system asks \( \A\x \) to hit \( \b \), which need not be in \( \col(\A) \) at all. Projecting first is exactly the step that moves the target into reach; what is given up is the requirement \( \r = \0 \), which becomes \( \r \perp \col(\A) \).
:::

## When is the least-squares solution unique?

The minimizers of \( \norm{\A\x - \b} \) are the solutions of the normal equations, so they form the solution set of a linear system: a coset \( \x_0 + \nul(\A^{*}\A) \) (@thm-general-solution-structure). To read off uniqueness we therefore need \( \nul(\A^{*}\A) \), and the following small lemma computes it.

::: {#lem-kernel-normal-equations}
[The null space of \( \A^{*}\A \)]

Let \( \A \in M_{m \times n}(F) \). Then \( \nul(\A^{*}\A) = \nul(\A) \).
:::

::: {.proof}
\( (\supseteq) \) If \( \A\x = \0 \), then \( \A^{*}\A\x = \A^{*}\0 = \0 \).

\( (\subseteq) \) Suppose \( \A^{*}\A\x = \0 \). Pair with \( \x \) and move \( \A^{*} \) across using @lem-conjugate-transpose-pairing:
\[
0 = \inner{\A^{*}(\A\x)}{\x} = \inner{\A\x}{\A\x} = \norm{\A\x}^2 .
\]
Hence \( \A\x = \0 \) by positive definiteness. This proves the lemma.
:::

This is the "pair it with itself" move once more, and it is the whole reason the normal equations behave well. It will return in Section 6 in the form \( \ker(T^{*}T) = \ker T \) for a linear map \( T \) between inner product spaces, with the same two-line proof; the matrix statement above is the case we need now.

:::: {#cor-least-squares-unique}
[Uniqueness of the least-squares solution]

Let \( \A \in M_{m \times n}(F) \) and \( \b \in F^m \). The following are equivalent:

::: {.enumerate options="label=(\alph*)"}
1. \( \A\x = \b \) has exactly one least-squares solution (for one, equivalently for every, \( \b \));
2. the columns of \( \A \) are linearly independent, that is \( \rank \A = n \);
3. \( \A^{*}\A \) is invertible.
:::

In that case the least-squares solution is \( \x = (\A^{*}\A)^{-1}\A^{*}\b \).
::::

::: {.proof}
By @thm-least-squares the least-squares solutions are the solutions of \( \A^{*}\A\x = \A^{*}\b \), a consistent system; by @thm-general-solution-structure its solution set is a coset of \( \nul(\A^{*}\A) \), which is \( \nul(\A) \) by @lem-kernel-normal-equations. So the solution is unique, for one \( \b \) or for all, exactly when \( \nul(\A) = \{\0\} \). Now \( \nul(\A) = \{\0\} \) says precisely that the only vanishing linear combination of the columns of \( \A \) is the trivial one, that is, that the columns are independent; and by @thm-rank-nullity-matrix this is the same as \( \rank\A = n \). This proves (a) \( \Leftrightarrow \) (b).

(b) \( \Leftrightarrow \) (c). The matrix \( \A^{*}\A \) is \( n \times n \), so it is invertible if and only if \( \nul(\A^{*}\A) = \{\0\} \) (@thm-invertible-tfae). By @lem-kernel-normal-equations this happens exactly when \( \nul(\A) = \{\0\} \).

Finally, if \( \A^{*}\A \) is invertible, multiplying the normal equations on the left by \( (\A^{*}\A)^{-1} \) gives the stated formula.
:::

::: {.warning}
**\( (\A^{*}\A)^{-1} \) is not \( \A^{-1}(\A^{*})^{-1} \).** The rule \( (\B\C)^{-1} = \C^{-1}\B^{-1} \) needs \( \B \) and \( \C \) to be invertible, and in least squares \( \A \) is usually not even square. Take
\[
\A = \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 1 \end{pmatrix}, \qquad \A\tp\A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}, \qquad (\A\tp\A)^{-1} = \frac13\begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}.
\]
The left side exists; the symbols \( \A^{-1} \) and \( (\A\tp)^{-1} \) do not exist at all, since \( \A \) is \( 3 \times 2 \). The formula \( \x = (\A^{*}\A)^{-1}\A^{*}\b \) must be read as one object \( (\A^{*}\A)^{-1} \) applied to \( \A^{*}\b \), never simplified.
:::

## Fitting a line and a parabola

::: {#exm-least-squares-line}
[The least-squares line through four points]

Find the line \( y = c + dt \) that minimizes the sum of the squared vertical errors at the four data points
\[
(1, 3), \quad (2, 1), \quad (3, 5), \quad (4, 5).
\]
Compute the residual and the minimum value of the sum of squares.
:::

::: {.solution}
Asking for \( c + dt_i = y_i \) at the four points is the system \( \A\x = \b \) with
\[
\A = \begin{pmatrix} 1 & 1 \\ 1 & 2 \\ 1 & 3 \\ 1 & 4 \end{pmatrix}, \qquad \x = \begin{pmatrix} c \\ d \end{pmatrix}, \qquad \b = \begin{pmatrix} 3 \\ 1 \\ 5 \\ 5 \end{pmatrix},
\]
and \( \norm{\A\x - \b}^2 \) is exactly the sum of the squared vertical errors. The columns of \( \A \) are independent (they are not multiples of each other), so @cor-least-squares-unique gives a unique answer. Over \( \nR \), \( \A^{*} = \A\tp \), and
\[
\A\tp\A = \begin{pmatrix} 4 & 10 \\ 10 & 30 \end{pmatrix}, \qquad \A\tp\b = \begin{pmatrix} 3 + 1 + 5 + 5 \\ 3 + 2 + 15 + 20 \end{pmatrix} = \begin{pmatrix} 14 \\ 40 \end{pmatrix}.
\]
The normal equations \( 4c + 10d = 14 \), \( 10c + 30d = 40 \) simplify to \( 2c + 5d = 7 \) and \( c + 3d = 4 \); subtracting twice the second from the first gives \( -d = -1 \), so \( d = 1 \) and \( c = 1 \). The least-squares line is
\[
y = 1 + t .
\]
Its values at \( t = 1, 2, 3, 4 \) are \( 2, 3, 4, 5 \), so the residual is
\[
\r = \b - \A\x = (3, 1, 5, 5) - (2, 3, 4, 5) = (1, -2, 1, 0),
\]
and the minimum sum of squares is \( \norm{\r}^2 = 1 + 4 + 1 + 0 = 6 \).

*Check.* The residual must be orthogonal to both columns of \( \A \): \( 1 - 2 + 1 + 0 = 0 \) and \( 1 - 4 + 3 + 0 = 0 \). Both hold, which confirms the normal equations.
:::

The same machinery fits any linear combination of prescribed functions; only the columns of \( \A \) change. "Linear" refers to the unknown coefficients, not to the shape of the curve.

::: {#exm-least-squares-quadratic}
[The least-squares parabola]

Find the quadratic \( y = a + bt + ct^2 \) minimizing the sum of squared errors at
\[
(-2, 7), \quad (-1, 6), \quad (0, 2), \quad (1, 0), \quad (2, 5).
\]
:::

::: {.solution}
Now \( \A \) has columns \( (1, 1, 1, 1, 1) \), \( (t_i) \) and \( (t_i^2) \):
\[
\A = \begin{pmatrix} 1 & -2 & 4 \\ 1 & -1 & 1 \\ 1 & 0 & 0 \\ 1 & 1 & 1 \\ 1 & 2 & 4 \end{pmatrix}, \qquad \b = \begin{pmatrix} 7 \\ 6 \\ 2 \\ 0 \\ 5 \end{pmatrix}.
\]
Because the nodes are symmetric about \( 0 \), every odd power sums to zero: \( \sum t_i = 0 \) and \( \sum t_i^3 = 0 \). With \( \sum t_i^2 = 10 \) and \( \sum t_i^4 = 34 \),
\[
\A\tp\A = \begin{pmatrix} 5 & 0 & 10 \\ 0 & 10 & 0 \\ 10 & 0 & 34 \end{pmatrix}, \qquad \A\tp\b = \begin{pmatrix} 20 \\ -10 \\ 54 \end{pmatrix}.
\]
The middle equation decouples: \( 10b = -10 \), so \( b = -1 \). The outer two are \( 5a + 10c = 20 \) and \( 10a + 34c = 54 \); the first gives \( a = 4 - 2c \), and substituting gives \( 40 + 14c = 54 \), so \( c = 1 \) and \( a = 2 \). The least-squares parabola is
\[
y = 2 - t + t^2 .
\]
Its values at the nodes are \( 8, 4, 2, 2, 4 \), so \( \r = (-1, 2, 0, -2, 1) \) and the minimum sum of squares is \( \norm{\r}^2 = 1 + 4 + 0 + 4 + 1 = 10 \).

*Check.* \( \sum r_i = 0 \), \( \sum t_ir_i = 2 - 2 + 0 - 2 + 2 = 0 \) and \( \sum t_i^2r_i = -4 + 2 + 0 - 2 + 4 = 0 \): the residual is orthogonal to all three columns.
:::

Two practical remarks. Choosing the nodes symmetrically, as above, made \( \A\tp\A \) nearly diagonal and the arithmetic painless; the same trick appears again in Section 9 when the columns are trigonometric functions. And although the normal equations are the right way to *understand* least squares, they are not always the right way to *compute* it: Section 8 solves the same problem through a QR factorization, which avoids forming \( \A^{*}\A \) at all.

## The minimum-norm solution

Now the opposite situation: \( \A\x = \b \) is consistent, but \( \A \) has a non-trivial null space, so the solutions form an infinite family \( \x_0 + \nul(\A) \) (@thm-general-solution-structure). Which one should we report? Orthogonality answers.

:::: {#thm-minimum-norm-solution}
[Minimum-Norm Solution]

Let \( \A \in M_{m \times n}(F) \) and let \( \b \in F^m \) be such that \( \A\x = \b \) is consistent. Write \( K = \nul(\A) \). Then:

::: {.enumerate options="label=(\alph*)"}
1. exactly one solution \( \x_{\min} \) of \( \A\x = \b \) lies in \( K^{\perp} \);
2. \( \norm{\x_{\min}} < \norm{\x} \) for every other solution \( \x \).
:::

We call \( \x_{\min} \) the **minimum-norm solution**.
::::

::: {.idea}
The solution set is a coset \( \x_0 + K \), and \( F^n = K \oplus K^{\perp} \). Throwing away the \( K \)-part of \( \x_0 \) keeps it a solution, because that part is in the kernel, and lands it in \( K^{\perp} \). Once there, Pythagoras compares it with every other solution: the others differ from it by a kernel vector, which is perpendicular to it and only adds length.
:::

::: {.proof}
(a) *Existence.* Let \( \x_0 \) be any solution. Since \( K \) is a subspace of the finite-dimensional space \( F^n \), @thm-orthogonal-decomposition (a) gives \( F^n = K \oplus K^{\perp} \); write \( \x_0 = \k + \x_{\min} \) with \( \k \in K \) and \( \x_{\min} \in K^{\perp} \). Then \( \A\x_{\min} = \A\x_0 - \A\k = \b - \0 = \b \), so \( \x_{\min} \) is a solution lying in \( K^{\perp} \).

*Uniqueness.* If \( \x_{\min} \) and \( \y \) are solutions in \( K^{\perp} \), then \( \A(\x_{\min} - \y) = \0 \), so \( \x_{\min} - \y \in K \cap K^{\perp} = \{\0\} \) by @thm-orthogonal-decomposition (a).

(b) Every solution has the form \( \x = \x_{\min} + \k \) with \( \k \in K \), by @thm-general-solution-structure. Since \( \x_{\min} \in K^{\perp} \) and \( \k \in K \), the two are orthogonal, and @thm-pythagoras gives
\[
\norm{\x}^2 = \norm{\x_{\min}}^2 + \norm{\k}^2 .
\]
If \( \x \neq \x_{\min} \), then \( \k \neq \0 \), so \( \norm{\k}^2 > 0 \) and \( \norm{\x} > \norm{\x_{\min}} \). This proves the theorem.
:::

The subspace \( K^{\perp} \) has a matrix description that makes \( \x_{\min} \) computable. For \( \x \in F^n \),
\[
\begin{aligned}
\x \in \col(\A^{*})^{\perp}
  &\iff \inner{\x}{\A^{*}\y} = 0 \ \text{ for all } \y \in F^m \\
  &\iff \inner{\A\x}{\y} = 0 \ \text{ for all } \y \in F^m \\
  &\iff \A\x = \0,
\end{aligned}
\]
where the first step is @def-orthogonal-complement together with \( \col(\A^{*}) = \{\A^{*}\y : \y \in F^m\} \) (@thm-matrix-times-vector-columns), the second is @lem-conjugate-transpose-pairing, and the last uses the choice \( \y = \A\x \) with positive definiteness. So \( \nul(\A) = \col(\A^{*})^{\perp} \), and applying \( \perp \) once more (@thm-orthogonal-decomposition (b)) gives
\[
\bigl(\nul(\A)\bigr)^{\perp} = \col(\A^{*}) .
\]
In words: the minimum-norm solution is the unique solution that is a combination of the columns of \( \A^{*} \), that is, of the conjugated rows of \( \A \). Section 6 proves the same statement for linear maps, together with the three companion identities that make up the four fundamental subspaces.

::: {#exm-minimum-norm-solution}
[A minimum-norm solution]

Find the solution of smallest norm of
\[
\begin{cases} x_1 + x_2 + x_3 = 3, \\ x_1 + 2x_2 + 3x_3 = 7. \end{cases}
\]
:::

::: {.solution}
Here \( \A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \end{pmatrix} \). Subtracting the first equation from the second gives \( x_2 + 2x_3 = 4 \), so \( x_2 = 4 - 2x_3 \) and then \( x_1 = 3 - x_2 - x_3 = x_3 - 1 \). With \( t = x_3 \) the solutions are
\[
\x(t) = (-1, 4, 0) + t(1, -2, 1), \qquad t \in \nR ,
\]
so \( K = \nul(\A) = \Span((1, -2, 1)) \). By @thm-minimum-norm-solution the answer is the unique \( t \) with \( \x(t) \perp (1, -2, 1) \):
\[
\inner{\x(t)}{(1, -2, 1)} = (-1 + t) - 2(4 - 2t) + t = 6t - 9 = 0, \qquad t = \tfrac32 .
\]
Hence \( \x_{\min} = \bigl(\tfrac12, 1, \tfrac32\bigr) \), with \( \norm{\x_{\min}}^2 = \tfrac14 + 1 + \tfrac94 = \tfrac72 \).

*Check.* It is a solution, since \( \tfrac12 + 1 + \tfrac32 = 3 \) and \( \tfrac12 + 2 + \tfrac92 = 7 \), and it is orthogonal to the kernel, since \( \tfrac12 - 2 + \tfrac32 = 0 \). By the identity \( (\nul\A)^{\perp} = \col(\A\tp) \) above it must also be a combination of the rows of \( \A \), and it is: \( \x_{\min} = \tfrac12(1, 2, 3) \), half the second row. Finally, the solution \( \x(0) = (-1, 4, 0) \) has \( \norm{\x(0)}^2 = 17 > \tfrac72 \), as @thm-minimum-norm-solution (b) requires.
:::

The two answers of this section — the least-squares solution and the minimum-norm solution — are usually wanted together: given any \( \A \) and \( \b \), first minimize \( \norm{\A\x - \b} \), then among the minimizers take the shortest. Chapter 12 packages the combined answer as a single matrix, the **pseudoinverse** \( \A^{+} \), with \( \x = \A^{+}\b \) in all cases at once.

## Exercises

### A. Check your understanding

:::: {#exr-least-squares-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define a least-squares solution of \( \A\x = \b \), and write down the normal equations.
2. True or false: if \( \A\x = \b \) is consistent, then its solutions are exactly its least-squares solutions. Justify your answer.
3. Explain in one sentence why the normal equations are always consistent.
4. Give a condition on the columns of \( \A \) equivalent to uniqueness of the least-squares solution.
5. Where does the minimum-norm solution of a consistent system live, and why is it unique there?
6. True or false: \( (\A^{*}\A)^{-1} = \A^{-1}(\A^{*})^{-1} \). Justify your answer.
:::
::::

::: {.solution}
(a) A vector \( \x \in F^n \) with \( \norm{\A\x - \b} \le \norm{\A\z - \b} \) for every \( \z \in F^n \). The normal equations are \( \A^{*}\A\x = \A^{*}\b \) (@thm-least-squares).

(b) True. If \( \A\x_0 = \b \) then \( \norm{\A\x_0 - \b} = 0 \), which is the smallest possible value, so \( \x_0 \) is a least-squares solution; conversely a least-squares solution \( \x \) has \( \norm{\A\x - \b} \le 0 \), hence \( \A\x = \b \). Least squares extends the notion of a solution without changing it when solutions exist.

(c) Because the target \( P_{\col(\A)}\b \) lies in \( \col(\A) \) by construction, so \( \A\x = P_{\col(\A)}\b \) is solvable (@thm-least-squares, existence).

(d) The columns are linearly independent, equivalently \( \rank\A = n \), equivalently \( \A^{*}\A \) is invertible (@cor-least-squares-unique).

(e) In \( (\nul \A)^{\perp} = \col(\A^{*}) \). Two solutions there would differ by an element of \( \nul(\A) \cap (\nul\A)^{\perp} = \{\0\} \) (@thm-minimum-norm-solution).

(f) False, and usually meaningless: \( \A \) need not be square, so \( \A^{-1} \) need not exist, while \( (\A^{*}\A)^{-1} \) can exist perfectly well — see the \( 3 \times 2 \) example in the warning after @cor-least-squares-unique.
:::

### B. Practice

:::: {#exr-least-squares-b1}
[B1: A least-squares line]

Find the least-squares line \( y = c + dt \) for the data \( (0, 3), (1, 2), (2, 3), (3, 6) \). Compute the residual, verify that it is orthogonal to both columns of \( \A \), and give the minimum sum of squares.
::::

::: {.solution}
With \( \A \) having columns \( (1,1,1,1) \) and \( (0,1,2,3) \) and \( \b = (3, 2, 3, 6) \),
\[
\A\tp\A = \begin{pmatrix} 4 & 6 \\ 6 & 14 \end{pmatrix}, \qquad \A\tp\b = \begin{pmatrix} 14 \\ 0 + 2 + 6 + 18 \end{pmatrix} = \begin{pmatrix} 14 \\ 26 \end{pmatrix}.
\]
The normal equations are \( 2c + 3d = 7 \) and \( 3c + 7d = 13 \). Multiplying the first by \( 3 \) and the second by \( 2 \) and subtracting gives \( 9d - 14d = 21 - 26 \), so \( d = 1 \), and then \( c = 2 \). The line is \( y = 2 + t \).

Its values at \( t = 0, 1, 2, 3 \) are \( 2, 3, 4, 5 \), so \( \r = (1, -1, -1, 1) \). Orthogonality: \( 1 - 1 - 1 + 1 = 0 \) against the first column and \( 0 - 1 - 2 + 3 = 0 \) against the second. The minimum sum of squares is \( \norm{\r}^2 = 4 \).
:::

:::: {#exr-least-squares-b2}
[B2: A least-squares parabola]

Find the least-squares quadratic \( y = a + bt + ct^2 \) for the data \( (-1, 2), (0, 8), (1, 6), (2, 16) \), and the minimum sum of squares. *Hint: write down \( \A\tp\A \) from the power sums \( \sum t_i^k \), \( k = 0, \dots, 4 \).*
::::

::: {.solution}
The power sums are \( \sum 1 = 4 \), \( \sum t_i = 2 \), \( \sum t_i^2 = 6 \), \( \sum t_i^3 = 8 \), \( \sum t_i^4 = 18 \), so
\[
\A\tp\A = \begin{pmatrix} 4 & 2 & 6 \\ 2 & 6 & 8 \\ 6 & 8 & 18 \end{pmatrix}, \qquad
\A\tp\b = \begin{pmatrix} 2 + 8 + 6 + 16 \\ -2 + 0 + 6 + 32 \\ 2 + 0 + 6 + 64 \end{pmatrix} = \begin{pmatrix} 32 \\ 36 \\ 72 \end{pmatrix}.
\]
Solving: from the first two equations, \( 2a + b + 3c = 16 \) and \( a + 3b + 4c = 18 \); eliminating \( a \) gives \( 5b + 5c = 20 \), so \( b + c = 4 \). The third equation is \( 3a + 4b + 9c = 36 \). Substituting \( b = 4 - c \) into \( 2a + b + 3c = 16 \) gives \( 2a + 2c = 12 \), so \( a = 6 - c \); then \( 3(6 - c) + 4(4 - c) + 9c = 36 \) becomes \( 34 + 2c = 36 \), so \( c = 1 \), \( b = 3 \), \( a = 5 \). The parabola is
\[
y = 5 + 3t + t^2 .
\]
Its values at \( t = -1, 0, 1, 2 \) are \( 3, 5, 9, 15 \), so \( \r = (-1, 3, -3, 1) \) and the minimum sum of squares is \( 1 + 9 + 9 + 1 = 20 \). *Check:* \( \sum r_i = 0 \), \( \sum t_ir_i = 1 + 0 - 3 + 2 = 0 \), \( \sum t_i^2r_i = -1 + 0 - 3 + 4 = 0 \).
:::

:::: {#exr-least-squares-b3}
[B3: A minimum-norm solution]

Find the minimum-norm solution of
\[
\begin{cases} x_1 + x_3 = 2, \\ x_2 + x_3 = 3, \end{cases}
\]
and verify that it is orthogonal to \( \nul(\A) \).
::::

::: {.solution}
With \( x_3 = t \) the solutions are \( \x(t) = (2 - t,\ 3 - t,\ t) = (2, 3, 0) + t(-1, -1, 1) \), so \( \nul(\A) = \Span((-1, -1, 1)) \). By @thm-minimum-norm-solution we need \( \inner{\x(t)}{(-1,-1,1)} = 0 \):
\[
-(2 - t) - (3 - t) + t = 3t - 5 = 0, \qquad t = \tfrac53 .
\]
So \( \x_{\min} = \bigl(\tfrac13, \tfrac43, \tfrac53\bigr) \), with \( \norm{\x_{\min}}^2 = \tfrac{1 + 16 + 25}{9} = \tfrac{14}{3} \). It solves the system, since \( \tfrac13 + \tfrac53 = 2 \) and \( \tfrac43 + \tfrac53 = 3 \), and \( -\tfrac13 - \tfrac43 + \tfrac53 = 0 \) confirms the orthogonality. For comparison, \( \norm{(2, 3, 0)}^2 = 13 > \tfrac{14}{3} \).
:::

### C. Going deeper

:::: {#exr-least-squares-c1}
[C1: Weighted least squares]

Let \( \A \in M_{m \times n}(\nR) \), \( \b \in \nR^m \), and let \( w_1, \dots, w_m > 0 \) be weights, with \( \W = \diag(w_1, \dots, w_m) \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \inner{\x}{\y}_{\W} = \y\tp\W\x \) is an inner product on \( \nR^m \).
2. Prove that the minimizers of \( \sum_{i=1}^{m} w_i\bigl((\A\x)_i - b_i\bigr)^2 \) are exactly the solutions of \( \A\tp\W\A\x = \A\tp\W\b \).
3. For the data \( (0, 2), (1, 1), (2, 8) \) with weights \( (1, 2, 1) \), find the weighted least-squares line, and compare it with the unweighted one.
:::
::::

::: {.solution}
(a) It is bilinear and symmetric because \( \y\tp\W\x = \sum_i w_ix_iy_i \), and \( \inner{\x}{\x}_{\W} = \sum_i w_ix_i^2 > 0 \) whenever some \( x_i \neq 0 \), because every \( w_i > 0 \). (This is where positivity of the weights is used; a zero weight would destroy definiteness.)

(b) Write \( \norm{\cdot}_{\W} \) for the norm induced by \( \inner{\cdot}{\cdot}_{\W} \). The quantity to minimize is exactly \( \norm{\A\x - \b}_{\W}^2 \). The proof of @thm-least-squares used nothing about the inner product except its axioms, so it applies verbatim with \( \inner{\cdot}{\cdot}_{\W} \) in place of the standard one: the minimizers are the \( \x \) for which \( \A\x - \b \) is \( \inner{\cdot}{\cdot}_{\W} \)-orthogonal to \( \col(\A) \), that is, for which \( \inner{\A\x - \b}{\A\z}_{\W} = 0 \) for all \( \z \in \nR^n \). Now
\[
\inner{\A\x - \b}{\A\z}_{\W} = (\A\z)\tp\W(\A\x - \b) = \z\tp\bigl(\A\tp\W\A\x - \A\tp\W\b\bigr),
\]
and this vanishes for all \( \z \in \nR^n \) exactly when \( \A\tp\W\A\x - \A\tp\W\b = \0 \), by taking \( \z \) equal to that vector.

(c) With \( \A \) having columns \( (1,1,1) \) and \( (0,1,2) \), \( \b = (2, 1, 8) \) and \( \W = \diag(1,2,1) \),
\[
\A\tp\W\A = \begin{pmatrix} 4 & 4 \\ 4 & 6 \end{pmatrix}, \qquad \A\tp\W\b = \begin{pmatrix} 2 + 2 + 8 \\ 0 + 2 + 16 \end{pmatrix} = \begin{pmatrix} 12 \\ 18 \end{pmatrix},
\]
so \( 4c + 4d = 12 \) and \( 4c + 6d = 18 \), giving \( d = 3 \) and \( c = 0 \): the weighted line is \( y = 3t \). Unweighted, \( \A\tp\A = \begin{pmatrix} 3 & 3 \\ 3 & 5 \end{pmatrix} \) and \( \A\tp\b = (11, 17) \), giving \( 3c + 3d = 11 \), \( 3c + 5d = 17 \), so \( d = 3 \) and \( c = \tfrac23 \): the unweighted line is \( y = \tfrac23 + 3t \). The middle point is trusted twice as much in the weighted fit, and the line moves down to pass closer to it. The weighted fit has weighted error \( 4 + 2 \cdot 4 + 4 = 16 \), smaller than the weighted error \( \tfrac{160}{9} \) of the unweighted line, while the unweighted fit has plain error \( \tfrac{32}{3} \), smaller than the plain error \( 12 \) of the weighted line: each line wins the contest it was designed for.
:::

:::: {#exr-least-squares-c2}
[C2: The residual, two ways]

Let \( \x \) be a least-squares solution of \( \A\x = \b \) and let \( \r = \b - \A\x \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \norm{\r}^2 = \norm{\b}^2 - \norm{\A\x}^2 \), and also that \( \norm{\r}^2 = \inner{\b}{\r} = \norm{\b}^2 - \inner{\A^{*}\b}{\x} \).
2. Use the second formula to recompute the minimum sum of squares in @exm-least-squares-line without finding the residual vector.
:::
::::

::: {.solution}
(a) By @thm-least-squares, \( \A\x = P_U\b \) with \( U = \col(\A) \), so \( \r = \b - P_U\b \in U^{\perp} \) while \( \A\x \in U \). The two are orthogonal, and \( \b = \A\x + \r \), so @thm-pythagoras gives \( \norm{\b}^2 = \norm{\A\x}^2 + \norm{\r}^2 \), which is the first identity.

For the second, \( \inner{\b}{\r} = \inner{\A\x + \r}{\r} = \inner{\A\x}{\r} + \norm{\r}^2 = \norm{\r}^2 \), since \( \inner{\A\x}{\r} = \conj{\inner{\r}{\A\x}} = 0 \) by orthogonality. Expanding the other way, and using @lem-conjugate-transpose-pairing,
\[
\inner{\b}{\r} = \inner{\b}{\b - \A\x} = \norm{\b}^2 - \inner{\b}{\A\x} = \norm{\b}^2 - \inner{\A^{*}\b}{\x} .
\]

(b) In @exm-least-squares-line, \( \norm{\b}^2 = 9 + 1 + 25 + 25 = 60 \), \( \A\tp\b = (14, 40) \) and \( \x = (1, 1) \), so
\[
\norm{\r}^2 = 60 - \inner{(14, 40)}{(1, 1)} = 60 - 54 = 6,
\]
matching the value found there. Only the data already assembled for the normal equations is needed.
:::

:::: {#exr-least-squares-c3}
[C3: A rank-deficient least-squares problem]

Let
\[
\A = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 2 \end{pmatrix}, \qquad \b = \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}.
\]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \A\x = \b \) is inconsistent and that \( \rank\A = 2 \).
2. Describe **all** least-squares solutions.
3. Find the one of smallest norm, and the minimum sum of squares.
:::
::::

::: {.solution}
(a) The third column is the sum of the first two, so the columns are dependent and \( \rank\A \le 2 \); the first two columns are independent, so \( \rank\A = 2 \) and \( \col(\A) = \Span\bigl((1,0,1), (0,1,1)\bigr) \). A vector \( (b_1, b_2, b_3) \) lies in \( \col(\A) \) exactly when \( b_3 = b_1 + b_2 \); here \( 0 \neq 1 + 2 \), so \( \b \notin \col(\A) \) and the system is inconsistent.

(b) By @thm-least-squares the least-squares solutions solve \( \A\tp\A\x = \A\tp\b \). Here
\[
\A\tp\A = \begin{pmatrix} 2 & 1 & 3 \\ 1 & 2 & 3 \\ 3 & 3 & 6 \end{pmatrix}, \qquad \A\tp\b = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}.
\]
Row reducing, the third row is the sum of the first two, and subtracting suitable multiples gives \( x_1 + x_3 = 0 \) and \( x_2 + x_3 = 1 \). Hence
\[
\x(t) = (0, 1, 0) + t(-1, -1, 1), \qquad t \in \nR ,
\]
a coset of \( \nul(\A) = \Span((-1,-1,1)) = \nul(\A\tp\A) \), as @lem-kernel-normal-equations predicts.

(c) The minimizers form a coset of \( \nul(\A) \), so the argument of @thm-minimum-norm-solution applies to it verbatim: the shortest is the one orthogonal to \( (-1, -1, 1) \). From \( -(-t) - (1 - t) + t = 3t - 1 = 0 \) we get \( t = \tfrac13 \) and
\[
\x_{\min} = \Bigl(-\tfrac13, \tfrac23, \tfrac13\Bigr), \qquad \norm{\x_{\min}}^2 = \tfrac{1 + 4 + 1}{9} = \tfrac23 .
\]
Every minimizer gives the same \( \A\x = (0, 1, 1) = P_{\col(\A)}\b \), with residual \( \r = (1, 1, -1) \) and minimum sum of squares \( \norm{\r}^2 = 3 \). *Check:* \( \r \) is orthogonal to \( (1,0,1) \) and to \( (0,1,1) \), since \( 1 - 1 = 0 \) and \( 1 - 1 = 0 \).
:::
