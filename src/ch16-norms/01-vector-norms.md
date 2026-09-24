# Norms

Chapter 11 measured vectors, and measured them in exactly one way: \( \norm{\v} = \sqrt{\inner{\v}{\v}} \). Every length in Chapters 11 to 13 came out of that formula. This section keeps the measuring and throws the inner product away. The reason is not economy. The quantities this part of the book owes — how fast a sequence of matrices settles down, how far a solution moves when the data moves — are often measured most naturally by a size that no inner product produces, and the arguments that use them turn out to need only three properties of a length.

**The field here is \( \nR \) or \( \nC \)**, as it is throughout the chapter. A length is a real number, and the scaling rule below multiplies it by \( \lvert c \rvert \); so the scalars must carry an absolute value, and these are the only fields in this book that do.

## What measurement actually needs

Look back at how \( \norm{\cdot} \) was used after Chapter 11 defined it. Cauchy–Schwarz needed the inner product. So did Pythagoras, orthogonality and the adjoint. But a long list of arguments did not: that a convergent sequence is bounded, that \( \norm{\A\x} \) is small when \( \x \) is small, that a limit of unit vectors is a unit vector, that \( \norm{\u - \w} \le \norm{\u - \v} + \norm{\v - \w} \). Every one of those used only that \( \norm{\v} \) vanishes just for \( \v = \0 \), that \( \norm{c\v} = \lvert c \rvert\norm{\v} \), and the triangle inequality of @cor-triangle-inequality. Three properties, used over and over. Following the book's habit, we give the three of them a name and see what else satisfies them.

*A norm is a length: zero only at the zero vector, scaling with the scalar, and never rewarding a detour.*

:::: {#def-norm}
[Norm]

Let \( F \) be \( \nR \) or \( \nC \) and let \( V \) be a vector space **over \( F \)**. A **norm** on \( V \) is a function
\[
\norm{\cdot} \colon V \to \nR
\]
such that for **all** \( \u, \v \in V \) and **all** \( c \in F \):

::: {.enumerate options="label=(N\arabic*)"}
1. \( \norm{\v} \ge 0 \), and \( \norm{\v} = 0 \) **only** for \( \v = \0 \)  (**positive definiteness**);
2. \( \norm{c\v} = \lvert c \rvert\,\norm{\v} \)  (**absolute homogeneity**);
3. \( \norm{\u + \v} \le \norm{\u} + \norm{\v} \)  (**the triangle inequality**).
:::

A vector space carrying a norm is a **normed space**. A vector with \( \norm{\v} = 1 \) is a **unit vector**, and replacing a non-zero \( \v \) by \( \v/\norm{\v} \) is **normalizing** it.
::::

In words, clause by clause. (N1) says the output is a genuine non-negative size, and that only the zero vector has size zero; the word **only** is the whole content, since the reverse implication is free (take \( c = 0 \) in (N2) to get \( \norm{\0} = 0\cdot\norm{\0} = 0 \)). (N2) says that stretching a vector by \( c \) stretches its length by \( \lvert c \rvert \) — the **absolute value** of \( c \), so that \( \norm{-\v} = \norm{\v} \) and, over \( \nC \), \( \norm{i\v} = \norm{\v} \). (N3) says that going from \( \0 \) to \( \u + \v \) directly is at most as long as going by way of \( \u \). Note what the definition does not mention: no second vector is paired with the first, no angle appears, and there is no inner product anywhere.

Two remarks on the shape of the definition. First, the codomain is \( \nR \) even when \( F = \nC \): a length is never complex. Second, the three clauses are not independent of the arithmetic of \( \nR \) — (N3) is an inequality, and inequalities are why the field had to be restricted.

::: {#exm-p-norms}
[The \( 1 \)-, \( 2 \)- and \( \infty \)-norms on \( F^n \)]

For \( \x = (x_1, \dots, x_n) \in F^n \) put
\[
\begin{aligned}
\norm{\x}_1 &= \lvert x_1\rvert + \dots + \lvert x_n\rvert , \\
\norm{\x}_2 &= \bigl(\lvert x_1\rvert^2 + \dots + \lvert x_n\rvert^2\bigr)^{1/2} , \\
\norm{\x}_\infty &= \max\{\lvert x_1\rvert, \dots, \lvert x_n\rvert\} .
\end{aligned}
\]
Check each of them against @def-norm.
:::

::: {.solution}
(N1) holds for all three: each is a sum, a square root of a sum, or a maximum of the non-negative numbers \( \lvert x_i\rvert \), so each is \( \ge 0 \); and each vanishes only when every \( \lvert x_i \rvert = 0 \), that is, only for \( \x = \0 \). (N2) holds because \( \lvert cx_i\rvert = \lvert c\rvert\lvert x_i\rvert \) for every \( i \), and the common factor \( \lvert c \rvert \) comes out of a sum, out of a square root of a sum of squares, and out of a maximum of non-negative numbers alike.

For (N3), the \( 1 \)-norm inherits it one coordinate at a time: \( \lvert x_i + y_i\rvert \le \lvert x_i\rvert + \lvert y_i\rvert \) for each \( i \) by the triangle inequality for the modulus (@thm-complex-triangle-inequality, which covers \( F = \nR \) as well), and summing over \( i \) gives \( \norm{\x + \y}_1 \le \norm{\x}_1 + \norm{\y}_1 \). The \( \infty \)-norm inherits it too, but from one coordinate rather than all: for each \( i \),
\[
\lvert x_i + y_i\rvert \le \lvert x_i\rvert + \lvert y_i\rvert
\le \norm{\x}_\infty + \norm{\y}_\infty ,
\]
and a bound valid for every \( i \) bounds the maximum. The \( 2 \)-norm is the norm induced by the standard inner product on \( F^n \) (@def-induced-norm), so its triangle inequality is @cor-triangle-inequality and needs no fresh argument.
:::

So one space carries at least three different norms. For \( \x = (3, -4, 12) \in \nR^3 \) they give \( \norm{\x}_1 = 19 \), \( \norm{\x}_2 = 13 \) and \( \norm{\x}_\infty = 12 \) — three honest answers to "how big is \( \x \)", and no reason yet to prefer one.

::: {.remark}
There is a \( p \)-norm \( \norm{\x}_p = \bigl(\sum_i\lvert x_i\rvert^{p}\bigr)^{1/p} \) for every real \( p \ge 1 \), and \( \norm{\x}_\infty \) is its limit as \( p \to \infty \). Its triangle inequality is Minkowski's inequality, which Chapter 18 proves from Hölder's inequality (and which is the first place real powers \( t^{p} \) and the logarithm are set up properly). This chapter uses only \( p = 1, 2, \infty \), and each of those was verified above from scratch.
:::

::: {#exm-induced-and-weighted-norms}
[Inner products, weights, and a function space]

Three further families.

::: {.enumerate options="label=(\alph*)"}
1. **Every inner product gives a norm.** If \( V \) is an inner product space, then \( \norm{\v} = \sqrt{\inner{\v}{\v}} \) satisfies (N1) and (N2) by @thm-norm-properties (a), (b) and (N3) by @cor-triangle-inequality. In particular the Frobenius norm \( \norm{\A}_F \) on \( M_{m\times n}(F) \) and the norm \( \bigl(\int_0^1\lvert f\rvert^2\bigr)^{1/2} \) on \( C[0,1] \) are norms.
2. **Weighted norms.** Fix real weights \( w_1, \dots, w_n > 0 \) and put \( \norm{\x}_{w} = \max_i w_i\lvert x_i\rvert \). All three clauses go through exactly as for \( \norm{\cdot}_\infty \), the weights riding along untouched; positivity of every \( w_i \) is what (N1) needs.
3. **The sup norm.** On \( C[0,1] \), the real continuous functions on \( [0,1] \), put \( \norm{f}_\infty = \max_{t\in[0,1]}\lvert f(t)\rvert \).
:::
:::

For (c) the maximum has to exist before the formula defines anything, and that is the first place this chapter borrows: \( [0,1] \) is compact and \( \lvert f\rvert \) is continuous, so by **the extreme value theorem, fact (A4) of the chapter introduction**, the maximum is attained. Granting that, (N1) says a continuous function with \( \max\lvert f\rvert = 0 \) is the zero function, which is true pointwise; (N2) and (N3) follow from the corresponding facts about \( \lvert\cdot\rvert \) at each point, exactly as for \( \norm{\cdot}_\infty \) on \( F^n \). Note that \( C[0,1] \) is infinite-dimensional — it contains all the polynomials — and it is kept in view deliberately, because §02's main theorem will fail on it.

A degenerate case is worth one line. On \( V = F \) itself, \( \norm{c} = \lvert c\rvert \) is a norm, and (N2) forces every norm on \( F \) to be \( \norm{c} = \lvert c\rvert\norm{1} \), a positive multiple of that one. On the zero space \( V = \{\0\} \) the only function to \( \nR \) is \( \norm{\0} = 0 \), and it is a norm. Both matter: they say that the theory is not empty at the bottom, and the first of them is the model for the general statement that any two norms differ by bounded factors.

::: {#exm-norm-non-example}
[Three near misses]

Change one feature of an example above and watch a single clause break.

::: {.enumerate options="label=(\alph*)"}
1. **Drop the square root.** On \( F^n \) put \( N(\x) = \lvert x_1\rvert^2 + \dots + \lvert x_n\rvert^2 \). Then (N1) still holds. But \( N(c\x) = \lvert c\rvert^2 N(\x) \), so (N2) fails as soon as \( \lvert c \rvert \ne 0, 1 \): for \( \x = \e_1 \) and \( c = 2 \) it gives \( N(2\e_1) = 4 \ne 2 = \lvert 2\rvert N(\e_1) \). The square root in \( \norm{\cdot}_2 \) is there for exactly this reason.
2. **Forget a coordinate.** On \( F^2 \) put \( N(\x) = \lvert x_1\rvert \). Then (N2) and (N3) both hold, inherited from \( \lvert\cdot\rvert \) on \( F \). What fails is the word **only** in (N1): \( N(\e_2) = 0 \) while \( \e_2 \ne \0 \). A function satisfying (N1) with "only" deleted, together with (N2) and (N3), is called a **seminorm**; it measures a quotient of \( V \) rather than \( V \).
3. **Bend the exponent the other way.** On \( \nR^2 \) put \( N(\x) = \bigl(\lvert x_1\rvert^{1/2} + \lvert x_2\rvert^{1/2}\bigr)^2 \). Then (N1) holds, and (N2) holds because \( \lvert c\rvert^{1/2} \) factors out of the inner sum and is squared back to \( \lvert c\rvert \). Only (N3) fails: \( N(\e_1) = N(\e_2) = 1 \) but \( N(\e_1 + \e_2) = (1 + 1)^2 = 4 > 2 \).
:::
:::

Item (c) is the one to remember, because it shows the three clauses are genuinely independent: two of them can hold exactly while the third fails, and it is the failing one that carries all the geometry.

::: {.warning}
**A norm is not determined by what it does to the standard basis.** Both \( \norm{\cdot}_1 \) and \( \norm{\cdot}_\infty \) give every \( \e_i \) length \( 1 \), and so does \( \norm{\cdot}_2 \), yet the three disagree everywhere else: on \( \1 = (1, \dots, 1) \) they return \( n \), \( 1 \) and \( \sqrt n \). Knowing the lengths of a basis pins down nothing, and this is worth holding on to, because §02's theorem is sometimes misremembered as saying that norms which agree on a basis agree everywhere. It says no such thing.
:::

One small consequence of (N3) will be used twice below and again in §02, so it gets a name here. It is @exr-inner-products-b4 with the inner product removed from the proof.

::: {#lem-reverse-triangle-norm}
[Reverse Triangle Inequality]

Let \( \norm{\cdot} \) be a norm on \( V \). Then for all \( \u, \v \in V \),
\[
\bigl\lvert\, \norm{\u} - \norm{\v} \,\bigr\rvert \le \norm{\u - \v} .
\]
:::

::: {.proof}
By (N3) applied to \( \u = (\u - \v) + \v \), we have \( \norm{\u} \le \norm{\u - \v} + \norm{\v} \), so \( \norm{\u} - \norm{\v} \le \norm{\u - \v} \). Swapping the roles of \( \u \) and \( \v \) gives \( \norm{\v} - \norm{\u} \le \norm{\v - \u} \), and \( \norm{\v - \u} = \lvert -1\rvert\norm{\u - \v} = \norm{\u - \v} \) by (N2). The number \( \lvert\norm{\u} - \norm{\v}\rvert \) is one of the two quantities just bounded, so it is at most \( \norm{\u - \v} \). This proves the inequality.
:::

Read with \( \v \) replaced by \( \v' \), it says that the function \( \norm{\cdot} \) changes by at most \( \norm{\u - \v} \) when its argument moves from \( \u \) to \( \v \). That is a Lipschitz estimate, and it is the reason a norm is continuous with respect to itself — a fact §02 turns into the main theorem.

## Unit balls

The quickest way to see the difference between two norms is to draw the set of vectors they call short.

::: {#def-unit-ball}
[Closed Unit Ball]

Let \( \norm{\cdot} \) be a norm on \( V \). Its **closed unit ball** is
\[
B_{\norm{\cdot}} = \{\v \in V : \norm{\v} \le 1\} .
\]
In \( F^n \) we write \( B_1 \), \( B_2 \) and \( B_\infty \) for the balls of @exm-p-norms.
:::

In \( \nR^2 \) the three are a diamond, a disc and a square, and they are nested.

\begin{center}
\begin{tikzpicture}[scale=1.6, lab/.style={font=\small}]
    \fill[black!5] (-1,-1) rectangle (1,1);
    \fill[black!14] (1,0) -- (0,1) -- (-1,0) -- (0,-1) -- cycle;
    \draw[->, gray] (-1.4,0) -- (1.62,0) node[above, black, lab] {$x_1$};
    \draw[->, gray] (0,-1.4) -- (0,1.45) node[left, black, lab] {$x_2$};
    \draw[very thick] (-1,-1) rectangle (1,1);
    \draw[thick, dashed] (0,0) circle (1);
    \draw[thick, dotted] (1,0) -- (0,1) -- (-1,0) -- (0,-1) -- cycle;
    \fill (1,0) circle (0.025);
    \draw[gray] (1.22,-0.26) -- (1.04,-0.05);
    \fill (1,1) circle (0.025);
    \node[lab] at (1.30,-0.34) {$\mathbf{e}_1$};
    \node[lab, above right] at (1,1) {$(1,1)$};
    \draw[very thick] (1.8,0.55) -- (2.2,0.55);
    \node[lab, right] at (2.3,0.55) {$B_\infty$, the square};
    \draw[thick, dashed] (1.8,0.15) -- (2.2,0.15);
    \node[lab, right] at (2.3,0.15) {$B_2$, the disc};
    \draw[thick, dotted] (1.8,-0.25) -- (2.2,-0.25);
    \node[lab, right] at (2.3,-0.25) {$B_1$, the diamond};
    \node[lab, align=center] at (1.1,-1.95)
      {The closed unit balls of the three norms on $\mathbb{R}^2$. A smaller ball\\
       belongs to a larger norm: $B_1 \subseteq B_2 \subseteq B_\infty$ says exactly that\\
       $\|\mathbf{x}\|_\infty \le \|\mathbf{x}\|_2 \le \|\mathbf{x}\|_1$, and all three agree at $\mathbf{e}_1$};
\end{tikzpicture}
\end{center}

Two features of the picture are general. Each ball is **symmetric**, \( \v \in B \) if and only if \( -\v \in B \), which is (N2) with \( c = -1 \); and each is **convex**, since if \( \norm{\u}, \norm{\v} \le 1 \) and \( 0 \le t \le 1 \) then
\[
\norm{t\u + (1-t)\v} \le t\norm{\u} + (1-t)\norm{\v} \le 1
\]
by (N3) and (N2). The diamond has corners and the square has corners; convexity is what the triangle inequality buys, and it is all it buys. The disc is rounder than the other two for a reason that is the subject of the last part of this section.

The nesting in the picture is an inequality, and it holds in every dimension, with a matching chain running the other way.

::: {#prp-p-norm-inequalities}
[Comparing the Three Norms]

For every \( \x \in F^n \),
\[
\norm{\x}_\infty \le \norm{\x}_2 \le \norm{\x}_1
\]
and
\[
\norm{\x}_1 \le \sqrt n\,\norm{\x}_2 , \qquad
\norm{\x}_2 \le \sqrt n\,\norm{\x}_\infty .
\]
Each of the four inequalities is attained: the first two by \( \x = \e_1 \), the last two by \( \x = \1 \).
:::

::: {.idea}
Four inequalities, two moves. The ones **without** a \( \sqrt n \) compare a sum against its largest term, or a sum of squares against the square of a sum, and need nothing but non-negativity. The ones **with** a \( \sqrt n \) are a trade of \( n \) terms against one, and the sharp constant comes from Cauchy–Schwarz against the all-ones vector \( \1 \) — which is exactly why \( \1 \) is the vector that attains them.
:::

::: {.proof}
Write \( a_i = \lvert x_i\rvert \ge 0 \) and let \( a_k = \max_i a_i \). Then \( a_k^2 \le \sum_i a_i^2 \), and taking non-negative square roots gives \( \norm{\x}_\infty \le \norm{\x}_2 \). Next,
\[
\norm{\x}_1^2 = \Bigl(\sum_i a_i\Bigr)^2
= \sum_i a_i^2 + \sum_{i \ne j} a_ia_j \ \ge\ \norm{\x}_2^2 ,
\]
since every cross term \( a_ia_j \) is \( \ge 0 \); taking square roots gives \( \norm{\x}_2 \le \norm{\x}_1 \).

For the third inequality, apply @thm-cauchy-schwarz in \( \nR^n \) with the dot product to the vectors \( (a_1, \dots, a_n) \) and \( \1 \):
\[
\norm{\x}_1 = \sum_i a_i \cdot 1
\le \Bigl(\sum_i a_i^2\Bigr)^{1/2}\Bigl(\sum_i 1\Bigr)^{1/2}
= \sqrt n\,\norm{\x}_2 .
\]
For the fourth, \( \sum_i a_i^2 \le n\max_i a_i^2 \), and taking square roots gives \( \norm{\x}_2 \le \sqrt n\,\norm{\x}_\infty \).

For the equality cases, \( \e_1 \) has \( \norm{\e_1}_1 = \norm{\e_1}_2 = \norm{\e_1}_\infty = 1 \), and \( \1 \) has \( \norm{\1}_1 = n \), \( \norm{\1}_2 = \sqrt n \) and \( \norm{\1}_\infty = 1 \), so \( \norm{\1}_1 = \sqrt n\,\norm{\1}_2 \) and \( \norm{\1}_2 = \sqrt n\,\norm{\1}_\infty \). This proves the proposition.
:::

So the three norms never disagree by a factor worse than \( \sqrt n \), and the factor \( \sqrt n \) really occurs. Hold on to both halves of that sentence: §02 proves the first half for *every* pair of norms, and the second half is why its constants cannot be made to forget the dimension.

::: {.check}
Sketch the set \( \{\x \in \nR^2 : \norm{\x}_{w} \le 1\} \) for the weighted norm \( \norm{\x}_{w} = \max(\lvert x_1\rvert, 2\lvert x_2\rvert) \) of @exm-induced-and-weighted-norms (b), and find the smallest \( C \) with \( \norm{\x}_\infty \le C\norm{\x}_{w} \) for all \( \x \).
:::

::: {.solution}
The ball is the rectangle \( \lvert x_1\rvert \le 1 \), \( \lvert x_2\rvert \le \tfrac12 \): the square \( B_\infty \) squashed vertically by a factor \( 2 \). Since \( \lvert x_1\rvert \le \norm{\x}_{w} \) and \( \lvert x_2\rvert \le \tfrac12\norm{\x}_{w} \), we get \( \norm{\x}_\infty \le \norm{\x}_{w} \), so \( C = 1 \) works, and it is smallest because \( \x = \e_1 \) gives \( \norm{\x}_\infty = \norm{\x}_{w} = 1 \). The other direction costs a factor: \( \norm{\x}_{w} \le 2\norm{\x}_\infty \), attained at \( \e_2 \). Squashing a ball inward enlarges the norm, and the largest squash factor is the constant.
:::

## Which norms come from an inner product

Chapter 11 §01 closed with a promise. It observed that @thm-norm-properties (a), (b) and @cor-triangle-inequality make every induced norm a norm in the general sense, warned that the converse fails, and named the test: the **parallelogram law**
\[
\norm{\u + \v}^2 + \norm{\u - \v}^2
= 2\norm{\u}^2 + 2\norm{\v}^2 . \tag{$\ast$}
\]
It then proved one direction outright — expand both sides with @thm-norm-properties (c) and add — and left the converse to @exr-inner-products-c1, which carries it out in \( \nR^2 \) while **granting** one step, the homogeneity \( \beta(\u, t\v) = t\beta(\u, \v) \) for real \( t \). That exercise's own remark says where the gap is: additivity gives homogeneity for rational \( t \) by induction, and passing to real \( t \) needs a limit.

Here is what this section adds. The dimension \( 2 \) in @exr-inner-products-c1 was never used, so the computation runs in any real space; the granted step is supplied by a limit, using the completeness of \( \nR \); and the complex case, which Chapter 11 did not touch at all, is built from the real one. The result is the theorem the promise described, with no hypothesis on the dimension.

::: {#thm-parallelogram-characterization}
[The Parallelogram Law Characterizes Inner-Product Norms]

Let \( F \) be \( \nR \) or \( \nC \), let \( V \) be a vector space over \( F \), and let \( \norm{\cdot} \) be a norm on \( V \). Then there is an inner product on \( V \) with \( \inner{\v}{\v} = \norm{\v}^2 \) for every \( \v \) **if and only if** \( \norm{\cdot} \) satisfies the parallelogram law \( (\ast) \) for all \( \u, \v \in V \). When it exists, that inner product is unique.
:::

::: {.idea}
The forward direction is Chapter 11's computation. For the converse there is only one candidate for the inner product, because @exr-inner-products-c2 already shows that an inner product is determined by its norm through polarization; so write down the polarization formula and check the axioms. ① Over \( \nR \) the symmetry and the additivity are the computation of @exr-inner-products-c1, which never mentions the dimension. ② Homogeneity comes free for rational scalars and is pushed to real scalars by a limit, which is the one analytic step. ③ Over \( \nC \), apply ① and ② to \( V \) regarded as a real space, then glue the real form \( \beta \) and its twist \( \beta(\u, i\v) \) into a complex inner product; the single identity \( \beta(i\u, i\v) = \beta(\u, \v) \) does all the work.
:::

::: {.proof}
\( (\Rightarrow) \) Suppose \( \inner{\v}{\v} = \norm{\v}^2 \) for an inner product on \( V \). By @thm-norm-properties (c) and the same identity with \( -\v \) in place of \( \v \),
\[
\begin{aligned}
\norm{\u + \v}^2 &= \norm{\u}^2 + 2\operatorname{Re}\inner{\u}{\v} + \norm{\v}^2 ,\\
\norm{\u - \v}^2 &= \norm{\u}^2 - 2\operatorname{Re}\inner{\u}{\v} + \norm{\v}^2 .
\end{aligned}
\]
Adding them gives \( (\ast) \).

\( (\Leftarrow) \) Suppose \( (\ast) \) holds. Regard \( V \) as a vector space over \( \nR \), by restricting which scalars are allowed. This changes nothing about \( \norm{\cdot} \): the vectors, the addition and the values of the norm are the same, and (N2) for real \( c \) is a special case of (N2) for \( c \in F \). Define
\[
\beta(\u, \v)
= \tfrac14\bigl(\norm{\u + \v}^2 - \norm{\u - \v}^2\bigr) .
\]

**Step 1. \( \beta \) is symmetric and additive in each slot.** @exr-inner-products-c1 runs this computation in \( \nR^2 \); rather than transport an exercise past the hypotheses it was stated under, here it is in full, for an arbitrary \( V \).

Setting \( \v = \u \) gives \( \beta(\u,\u) = \tfrac14\norm{2\u}^2 = \norm{\u}^2 \) by (N2). Swapping the arguments replaces \( \norm{\u - \v} \) by \( \norm{\v - \u} \), equal by (N2) with \( c = -1 \), so \( \beta(\u,\v) = \beta(\v,\u) \); and \( \beta(\u,\0) = 0 \).

For additivity, apply \( (\ast) \) twice. To the pair \( \u + \tfrac12(\v + \w) \), \( \tfrac12(\v - \w) \), whose sum is \( \u + \v \) and whose difference is \( \u + \w \):
\[
\norm{\u + \v}^2 + \norm{\u + \w}^2
= 2\norm{\u + \tfrac12(\v + \w)}^2 + 2\norm{\tfrac12(\v - \w)}^2 .
\]
Then to the pair \( \u - \tfrac12(\v + \w) \), \( \tfrac12(\w - \v) \), whose sum is \( \u - \v \) and whose difference is \( \u - \w \):
\[
\norm{\u - \v}^2 + \norm{\u - \w}^2
= 2\norm{\u - \tfrac12(\v + \w)}^2 + 2\norm{\tfrac12(\w - \v)}^2 .
\]
Subtract the second from the first. On the left, the two differences of squares are \( 4\beta(\u,\v) \) and \( 4\beta(\u,\w) \), by the definition of \( \beta \). On the right, the last terms cancel, since \( \norm{\tfrac12(\v-\w)} = \norm{\tfrac12(\w-\v)} \) by (N2) with \( c = -1 \), and the remaining difference of squares is \( 4\beta\bigl(\u, \tfrac12(\v+\w)\bigr) \). So \( 4\beta(\u,\v) + 4\beta(\u,\w) = 8\beta\bigl(\u,\tfrac12(\v+\w)\bigr) \), that is,
\[
\beta(\u, \v) + \beta(\u, \w) = 2\,\beta\bigl(\u, \tfrac12(\v + \w)\bigr) .
\]
Taking \( \w = \0 \) and using \( \beta(\u,\0) = 0 \) turns the right-hand side into \( 2\beta(\u, \tfrac12\v) \), so \( \beta(\u, \v) = 2\beta(\u, \tfrac12\v) \) for every \( \v \); substituting that back with \( \v + \w \) in place of \( \v \) gives
\[
\beta(\u, \v) + \beta(\u, \w) = \beta(\u, \v + \w)
\]
for all \( \u, \v, \w \in V \). Nothing in this argument mentions a dimension. Additivity in the first slot follows from the symmetry.

**Step 2. \( \beta(\u, t\v) = t\,\beta(\u, \v) \) for every real \( t \).** This is the step @exr-inner-products-c1 granted. First, \( \beta(\u, -\v) = -\beta(\u,\v) \), directly from the definition of \( \beta \), since replacing \( \v \) by \( -\v \) exchanges the two terms. Next, induction on \( m \ge 0 \) using Step 1 gives \( \beta(\u, m\v) = m\beta(\u,\v) \), the case \( m = 0 \) being \( \beta(\u,\0) = 0 \); combined with the previous sentence this covers every integer \( m \). For a rational \( q = m/n \) with \( n \ge 1 \),
\[
n\,\beta\bigl(\u, q\v\bigr) = \beta\bigl(\u, nq\v\bigr) = \beta(\u, m\v) = m\,\beta(\u,\v),
\]
so \( \beta(\u, q\v) = q\beta(\u,\v) \).

Now fix a real \( t \) and put \( M = \norm{\u} + (\lvert t\rvert + 1)\norm{\v} \). For any rational \( q \) with \( \lvert q - t\rvert \le 1 \), both \( \norm{\u \pm t\v} \) and \( \norm{\u \pm q\v} \) are at most \( M \) by (N2) and (N3), while @lem-reverse-triangle-norm and (N2) give
\[
\bigl\lvert \norm{\u \pm t\v} - \norm{\u \pm q\v} \bigr\rvert
\le \lvert t - q\rvert\,\norm{\v} .
\]
Since \( \lvert a^2 - b^2\rvert = \lvert a - b\rvert(a + b) \) for \( a, b \ge 0 \), each of the two squared terms in \( \beta \) moves by at most \( 2M\norm{\v}\lvert t - q\rvert \), and therefore
\[
\bigl\lvert \beta(\u, t\v) - \beta(\u, q\v) \bigr\rvert
\le M\norm{\v}\,\lvert t - q\rvert .
\]
By **the completeness of \( \nR \), fact (A1) of the chapter introduction**, there is a sequence of rationals \( q_k \to t \), and we may assume \( \lvert q_k - t\rvert \le 1 \). Then
\[
\begin{aligned}
&\bigl\lvert \beta(\u,t\v) - t\beta(\u,\v) \bigr\rvert \\
&\qquad \le \bigl\lvert \beta(\u,t\v) - \beta(\u,q_k\v) \bigr\rvert + \lvert q_k - t\rvert\,\lvert\beta(\u,\v)\rvert \\
&\qquad \le \bigl(M\norm{\v} + \lvert\beta(\u,\v)\rvert\bigr)\lvert q_k - t\rvert ,
\end{aligned}
\]
where the middle term used \( \beta(\u, q_k\v) = q_k\beta(\u,\v) \). The left-hand side does not depend on \( k \), and the right-hand side tends to \( 0 \), so the left-hand side is \( 0 \).

If \( F = \nR \), we are done: \( \beta \) is symmetric, bilinear by Steps 1 and 2, and \( \beta(\v,\v) = \norm{\v}^2 > 0 \) for \( \v \ne \0 \) by (N1), so (IP1), (IP2) and (IP3) of @def-inner-product all hold and the induced norm is \( \norm{\cdot} \).

**Step 3. The complex case.** Suppose \( F = \nC \). Steps 1 and 2 apply to \( V \) as a real space, so \( \beta \) is a symmetric \( \nR \)-bilinear form with \( \beta(\v,\v) = \norm{\v}^2 \). Define
\[
\inner{\u}{\v} = \beta(\u, \v) + i\,\beta(\u, i\v) .
\]
Everything follows from one identity: \( \beta(i\u, i\v) = \beta(\u,\v) \), which holds because \( \norm{i\u \pm i\v} = \norm{i(\u \pm \v)} = \lvert i\rvert\norm{\u \pm \v} = \norm{\u \pm \v} \) by (N2). Applying it twice, \( \beta(i\u, \v) = \beta(i\cdot i\u, i\v) = -\beta(\u, i\v) \).

(IP3) and the norm: \( \beta(\u, i\u) = \tfrac14(\norm{\u + i\u}^2 - \norm{\u - i\u}^2) \), and (N2) turns this into \( \tfrac14(\lvert 1 + i\rvert^2 - \lvert 1 - i\rvert^2)\norm{\u}^2 = 0 \). Hence \( \inner{\u}{\u} = \beta(\u,\u) = \norm{\u}^2 \), which is \( > 0 \) for \( \u \ne \0 \), and the induced norm is \( \norm{\cdot} \).

(IP1): additivity in the first slot and homogeneity for real scalars come from Steps 1 and 2 applied to both \( \beta(\cdot, \v) \) and \( \beta(\cdot, i\v) \). For the scalar \( i \),
\[
\begin{aligned}
\inner{i\u}{\v}
&= \beta(i\u, \v) + i\,\beta(i\u, i\v) \\
&= -\beta(\u, i\v) + i\,\beta(\u, \v)
= i\,\inner{\u}{\v} .
\end{aligned}
\]
Every complex scalar is \( a + bi \) with \( a, b \) real, so (IP1) follows.

(IP2): using \( \beta(\v, i\u) = \beta(i\v, i\cdot i\u) = -\beta(\u, i\v) \) and the symmetry of \( \beta \),
\[
\inner{\v}{\u} = \beta(\u,\v) - i\,\beta(\u, i\v) = \conj{\inner{\u}{\v}} .
\]

So \( \inner{\cdot}{\cdot} \) is an inner product inducing \( \norm{\cdot} \).

**Uniqueness.** Suppose \( \inner{\cdot}{\cdot}' \) is any inner product on \( V \) with \( \inner{\v}{\v}' = \norm{\v}^2 \) for every \( \v \). The two displays of the \( (\Rightarrow) \) direction apply to it verbatim, and subtracting them instead of adding them gives
\[
\norm{\u + \v}^2 - \norm{\u - \v}^2 = 4\operatorname{Re}\inner{\u}{\v}' ,
\]
that is, \( \operatorname{Re}\inner{\u}{\v}' = \beta(\u,\v) \): the real part of \( \inner{\cdot}{\cdot}' \) is forced to be the \( \beta \) built above. Over \( \nR \) an inner product is real-valued, so \( \inner{\u}{\v}' = \beta(\u,\v) \) and there is nothing left to choose. Over \( \nC \), apply the same identity to the pair \( \u, i\v \). By (IP1) and (IP2) together the form is conjugate-linear in its second slot, so \( \inner{\u}{i\v}' = \conj{i}\,\inner{\u}{\v}' = -i\,\inner{\u}{\v}' \), whose real part is \( \operatorname{Im}\inner{\u}{\v}' \). Hence \( \operatorname{Im}\inner{\u}{\v}' = \beta(\u, i\v) \), and the two parts together give \( \inner{\u}{\v}' = \beta(\u,\v) + i\,\beta(\u, i\v) \), which is exactly the inner product constructed above. So it is the only one. (@exr-inner-products-c2 set this computation as an exercise in Chapter 11; it is carried out here because the theorem rests on it.)

This proves the theorem.
:::

The theorem says that the parallelogram law is not one property of induced norms among many — it is the whole difference. A norm either obeys it, and then it is secretly an inner product with an inner product's entire apparatus of angles, orthogonality and adjoints; or it violates it once, and then no inner product will ever produce it.

::: {.warning}
**Neither \( \norm{\cdot}_1 \) nor \( \norm{\cdot}_\infty \) comes from an inner product.** Test \( (\ast) \) on \( \u = \e_1 \) and \( \v = \e_2 \) in \( F^2 \). Both \( \u + \v = (1,1) \) and \( \u - \v = (1,-1) \) have \( \norm{\cdot}_1 = 2 \), so the left side of \( (\ast) \) is \( 4 + 4 = 8 \), while the right side is \( 2 + 2 = 4 \). For \( \norm{\cdot}_\infty \) both have norm \( 1 \), so the left side is \( 2 \) and the right side is again \( 4 \). One failing pair is enough, and there is no repair: by @thm-parallelogram-characterization no inner product whatsoever induces these norms, in any dimension \( \ge 2 \). The same two vectors \( f(t) = t \) and \( g(t) = 1 - t \) in \( C[0,1] \) refute it for the sup norm, since \( \norm{f}_\infty = \norm{g}_\infty = \norm{f+g}_\infty = \norm{f-g}_\infty = 1 \).
:::

::: {.check}
The function \( N(\x) = \bigl(x_1^2 + 4x_2^2\bigr)^{1/2} \) is a norm on \( \nR^2 \), and it is lopsided: \( N(\e_1) = 1 \) while \( N(\e_2) = 2 \). Does it come from an inner product?
:::

::: {.solution}
Yes. It is the norm induced by \( \inner{\x}{\y} = x_1y_1 + 4x_2y_2 \), which satisfies (IP1) and (IP2) by inspection and (IP3) because \( x_1^2 + 4x_2^2 > 0 \) for \( \x \ne \0 \). One may also check \( (\ast) \) directly: both sides expand to \( 2x_1^2 + 8x_2^2 + 2y_1^2 + 8y_2^2 \). The lesson is that a norm can be visibly lopsided — its unit ball here is an ellipse, not a circle — and still be an inner-product norm. What matters is not roundness but the parallelogram law.
:::

So the norms of this book split in two. On one side sit \( \norm{\cdot}_2 \), the Frobenius norm and every weighted Euclidean norm, where Chapters 11 to 13 apply in full. On the other sit \( \norm{\cdot}_1 \), \( \norm{\cdot}_\infty \) and the sup norm, where there is no orthogonality and no adjoint, and the only tools are the three axioms. The next section shows that for questions about convergence the split does not matter at all.

## Exercises

### A. Check your understanding

:::: {#exr-vector-norms-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the three clauses of @def-norm, and say which one fails for \( N(\x) = \lvert x_1\rvert \) on \( F^2 \).
2. Deduce \( \norm{\0} = 0 \) from (N2) alone, and explain why (N1) is therefore stated with the word **only**.
3. True or false: a function satisfying (N1) and (N3) but not (N2) cannot exist. Justify your answer.
4. Name the test that decides whether a norm is induced by an inner product, and state what @exr-inner-products-c1 had already established before this section.
5. Order \( \norm{\x}_1 \), \( \norm{\x}_2 \), \( \norm{\x}_\infty \) for a general \( \x \in F^n \), and give a vector for which all three are equal.
:::
::::

::: {.solution}
(a) (N1) positive definiteness, (N2) absolute homogeneity, (N3) the triangle inequality (@def-norm). For \( N(\x) = \lvert x_1\rvert \) only (N1) fails, and only its "only" half: \( N(\e_2) = 0 \) with \( \e_2 \ne \0 \) (@exm-norm-non-example (b)).

(b) Take \( c = 0 \) and any \( \v \): (N2) gives \( \norm{\0} = \norm{0\v} = \lvert 0\rvert\norm{\v} = 0 \). So "\( \v = \0 \Rightarrow \norm{\v} = 0 \)" is automatic, and the only content left in (N1) is the converse, which is why it is the clause that is stated.

(c) False. Take \( N(\x) = \min(\norm{\x}_2, 1) \) on \( \nR^2 \). It is \( \ge 0 \) and vanishes only at \( \0 \), so (N1) holds. For (N3), note first that \( \min(a + b, 1) \le \min(a,1) + \min(b,1) \) for all \( a, b \ge 0 \): if either \( a \ge 1 \) or \( b \ge 1 \) the right side is at least \( 1 \), which bounds the left side; and otherwise the right side is \( a + b \), which is at least \( \min(a+b, 1) \). Applying this to \( a = \norm{\u}_2 \), \( b = \norm{\v}_2 \) and using that \( s \mapsto \min(s,1) \) is increasing gives (N3). But \( N(2\e_1) = 1 \ne 2 = 2N(\e_1) \), so (N2) fails.

(d) The parallelogram law \( (\ast) \): a norm is induced by an inner product exactly when \( \norm{\u+\v}^2 + \norm{\u-\v}^2 = 2\norm{\u}^2 + 2\norm{\v}^2 \) always (@thm-parallelogram-characterization). Before this section, @exr-inner-products-c1 had proved the converse direction on \( \nR^2 \), and only modulo the granted homogeneity \( \beta(\u,t\v) = t\beta(\u,\v) \) for real \( t \); the general dimension, the real homogeneity step and the complex case are what @thm-parallelogram-characterization adds.

(e) \( \norm{\x}_\infty \le \norm{\x}_2 \le \norm{\x}_1 \) (@prp-p-norm-inequalities). All three agree at \( \x = \e_1 \), and more generally at any \( \x \) with at most one non-zero coordinate.
:::

### B. Practice

:::: {#exr-vector-norms-b1}
[B1: Three measurements]

For \( \x = (1, -1, 2, -2) \in \nR^4 \), compute \( \norm{\x}_1 \), \( \norm{\x}_2 \) and \( \norm{\x}_\infty \), and verify all four inequalities of @prp-p-norm-inequalities. Which of them is closest to being an equality?
::::

::: {.solution}
\( \norm{\x}_1 = 1 + 1 + 2 + 2 = 6 \); \( \norm{\x}_2 = (1 + 1 + 4 + 4)^{1/2} = \sqrt{10} \); \( \norm{\x}_\infty = 2 \). Here \( n = 4 \), so \( \sqrt n = 2 \). The four inequalities read
\[
2 \le \sqrt{10} \le 6, \qquad
6 \le 2\sqrt{10}, \qquad
\sqrt{10} \le 4 ,
\]
and \( \sqrt{10} \approx 3.162 \), so all four hold. The tightest is \( \norm{\x}_1 \le \sqrt n\norm{\x}_2 \), that is \( 6 \le 6.32 \); this is as expected, since equality there needs all coordinates of equal modulus, and \( \x \) has only two distinct moduli.
:::

:::: {#exr-vector-norms-b2}
[B2: Determine which are norms]

Determine which of the following define norms on \( \nR^2 \). For those that do, verify all three clauses of @def-norm; for those that do not, name the exact clause that fails and give a witness. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( N(\x) = \lvert x_1\rvert + 2\lvert x_2\rvert \).
2. \( N(\x) = \lvert x_1 - x_2\rvert \).
3. \( N(\x) = \max\bigl(\lvert x_1\rvert, \lvert x_2\rvert\bigr) - \tfrac14\min\bigl(\lvert x_1\rvert, \lvert x_2\rvert\bigr) \).
4. \( N(\x) = \lvert x_1\rvert + \lvert x_2\rvert - \tfrac12\min\bigl(\lvert x_1\rvert, \lvert x_2\rvert\bigr) \).
:::
::::

::: {.solution}
(a) A norm. It is the weighted norm of @exm-induced-and-weighted-norms (b) in its \( 1 \)-norm form: (N1) because both terms are \( \ge 0 \) and both vanish only for \( \x = \0 \); (N2) because \( \lvert cx_i\rvert = \lvert c\rvert\lvert x_i\rvert \); (N3) coordinatewise, exactly as for \( \norm{\cdot}_1 \).

(b) Not a norm. (N2) and (N3) hold, inherited from \( \lvert\cdot\rvert \) on \( \nR \). **(N1) fails**: \( N\bigl((1,1)\bigr) = 0 \) with \( (1,1) \ne \0 \).

(c) Not a norm. (N1) holds, since \( N(\x) \ge \tfrac34\max(\lvert x_1\rvert, \lvert x_2\rvert) \), which is \( > 0 \) for \( \x \ne \0 \); and (N2) holds because \( \max \) and \( \min \) of the scaled moduli both pick up the factor \( \lvert c\rvert \). **(N3) fails**: with \( \u = (1,1) \) and \( \v = (1,-1) \) we get \( N(\u) = N(\v) = 1 - \tfrac14 = \tfrac34 \), while \( \u + \v = (2,0) \) has \( N(\u + \v) = 2 - 0 = 2 > \tfrac32 \). Subtracting from the largest coordinate is exactly what a cancellation in the sum can punish.

(d) A norm, despite the minus sign. Since \( \lvert x_1\rvert + \lvert x_2\rvert = \max + \min \), the formula is \( N(\x) = \max + \tfrac12\min \), which is
\[
N(\x) = \tfrac12\norm{\x}_1 + \tfrac12\norm{\x}_\infty .
\]
A sum of two norms, each scaled by a positive number, is a norm: (N1), (N2) and (N3) are each inherited term by term, and (N1) needs only one of the two summands to detect \( \x \ne \0 \). Compare (c): there the subtracted term was large enough to break (N3), here it is not, and the way to tell is to rewrite the formula rather than to guess.
:::

:::: {#exr-vector-norms-b3}
[B3: Which of these come from an inner product?]

For each norm, determine whether it is induced by an inner product. Justify your answer, using @thm-parallelogram-characterization in each case.

::: {.enumerate options="label=(\alph*)"}
1. \( \norm{\x} = \bigl(x_1^2 + x_1x_2 + x_2^2\bigr)^{1/2} \) on \( \nR^2 \).
2. \( \norm{\A}_F \) on \( M_2(\nR) \).
3. \( N(\A) = \max_{i,j}\lvert a_{ij}\rvert \) on \( M_2(\nR) \).
:::
::::

::: {.solution}
(a) Yes. Put \( \inner{\x}{\y} = x_1y_1 + \tfrac12(x_1y_2 + x_2y_1) + x_2y_2 \). It is bilinear and symmetric by inspection, and \( \inner{\x}{\x} = x_1^2 + x_1x_2 + x_2^2 = (x_1 + \tfrac12x_2)^2 + \tfrac34x_2^2 \), which is \( > 0 \) unless \( x_2 = 0 \) and \( x_1 = 0 \); so (IP3) holds and the induced norm is the given one. (Completing the square is also how one sees that the given function is a norm at all.)

(b) Yes. The Frobenius norm is induced by the Frobenius inner product \( \inner{\A}{\B} = \tr(\B\tp\A) \) (@exm-induced-and-weighted-norms (a)), so \( (\ast) \) holds by the forward direction of @thm-parallelogram-characterization.

(c) No. Take \( \A = \E_{11} \) and \( \B = \E_{12} \), the matrix units. Then \( \A \pm \B \) has entries \( 1 \) and \( \pm 1 \) in the first row and zeros elsewhere, so \( N(\A + \B) = N(\A - \B) = 1 \) and the left side of \( (\ast) \) is \( 2 \), while the right side is \( 2 \cdot 1 + 2\cdot 1 = 4 \). By @thm-parallelogram-characterization no inner product induces \( N \).
:::

### C. Going deeper

:::: {#exr-vector-norms-c1}
[C1: Sharpness of the comparison constants]

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \norm{\x}_1 = \sqrt n\,\norm{\x}_2 \) holds if and only if all the numbers \( \lvert x_1\rvert, \dots, \lvert x_n\rvert \) are equal. *Hint: the equality case of @thm-cauchy-schwarz.*
2. Hence deduce that no constant \( C \) independent of \( n \) satisfies \( \norm{\x}_1 \le C\norm{\x}_2 \) for all \( n \) and all \( \x \in \nR^n \).
:::
::::

::: {.solution}
(a) With \( \a = (\lvert x_1\rvert, \dots, \lvert x_n\rvert) \), the proof of @prp-p-norm-inequalities reads \( \norm{\x}_1 = \inner{\a}{\1} \le \norm{\a}_2\norm{\1}_2 = \sqrt n\norm{\x}_2 \), an application of @thm-cauchy-schwarz to \( \a \) and \( \1 \). Equality in @thm-cauchy-schwarz holds exactly when \( (\a, \1) \) is dependent. Since \( \1 \ne \0 \), that means \( \a = t\1 \) for some real \( t \), which is \( t \ge 0 \) because the entries of \( \a \) are; and \( \a = t\1 \) says precisely that all the \( \lvert x_i\rvert \) are equal.

(b) By (a), \( \x = \1 \in \nR^n \) gives \( \norm{\1}_1 = n \) and \( \norm{\1}_2 = \sqrt n \), so any valid \( C \) satisfies \( C \ge n/\sqrt n = \sqrt n \). As \( n \) is arbitrary, no single \( C \) works for all \( n \). The comparison constants between two norms are genuinely functions of the dimension.
:::

:::: {#exr-vector-norms-c2}
[C2: A real norm that is not a complex norm]

Regard \( \nC \) as a one-dimensional complex vector space, and also as \( \nR^2 \) by \( z = a + bi \leftrightarrow (a,b) \). Define \( N(z) = 2\lvert a\rvert + \lvert b\rvert \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( N \) is a norm on \( \nR^2 \).
2. Prove that \( N \) is **not** a norm on \( \nC \) as a complex vector space, and name the exact clause that fails.
3. Prove that if \( \norm{\cdot} \) is any norm on a complex vector space \( V \), then it is also a norm on \( V \) regarded as a real vector space. Explain why (b) does not contradict this.
:::
::::

::: {.solution}
(a) It is the weighted \( 1 \)-norm \( \lvert x_1\rvert\cdot 2 + \lvert x_2\rvert \cdot 1 \) of @exr-vector-norms-b2 (a) with the weights swapped, so all three clauses hold as there.

(b) **(N2) fails** for the complex scalar \( c = i \). Indeed \( N(1) = 2 \) and \( N(i) = 1 \), while (N2) would demand \( N(i\cdot 1) = \lvert i\rvert N(1) = 2 \).

(c) Restricting the scalars from \( \nC \) to \( \nR \) leaves the vectors, the addition and the zero vector unchanged, so (N1) and (N3) are the same statements. (N2) for real \( c \) is a special case of (N2) for complex \( c \), the absolute value of a real number being the same in \( \nR \) and in \( \nC \). There is no contradiction with (b) because the implication runs one way only: (N2) over \( \nC \) is a **strictly stronger** demand than (N2) over \( \nR \), the extra content being \( \norm{i\v} = \norm{\v} \), and \( N \) fails exactly that.
:::

:::: {#exr-vector-norms-c3}
[C3: The ball determines the norm]

Let \( \norm{\cdot} \) and \( N \) be two norms on a vector space \( V \) with the **same** closed unit ball, in the sense of @def-unit-ball:
\[
\{\v : \norm{\v} \le 1\} = \{\v : N(\v) \le 1\} .
\]

::: {.enumerate options="label=(\alph*)"}
1. Prove that for every \( \v \in V \) and every real \( t > 0 \), we have \( \norm{\v} \le t \) if and only if \( \v/t \) lies in the closed unit ball of \( \norm{\cdot} \).
2. Hence prove that \( \norm{\v} = N(\v) \) for every \( \v \in V \).
3. Give two different norms on \( \nR^2 \) whose closed unit balls have the same area, and say why (b) does not apply to them.
:::
::::

::: {.solution}
(a) Since \( t > 0 \), (N2) gives \( \norm{\v/t} = \norm{\v}/t \). So \( \v/t \) lies in the ball exactly when \( \norm{\v}/t \le 1 \), that is, exactly when \( \norm{\v} \le t \).

(b) For \( \v = \0 \) both sides are \( 0 \) by (N1). Let \( \v \ne \0 \) and put \( t = \norm{\v} > 0 \). By (a), \( \v/t \) lies in the ball of \( \norm{\cdot} \), hence in the ball of \( N \), hence \( N(\v) \le t = \norm{\v} \) by (a) applied to \( N \). Swapping the roles of \( \norm{\cdot} \) and \( N \) gives \( \norm{\v} \le N(\v) \). Therefore \( \norm{\v} = N(\v) \).

(c) Take \( \norm{\cdot}_1 \), whose ball is the diamond with vertices \( \pm\e_1 \) and \( \pm\e_2 \), of area \( 2 \); and \( N(\x) = 2\lvert x_1\rvert + \tfrac12\lvert x_2\rvert \), whose ball is the diamond with vertices \( \pm\tfrac12\e_1 \) and \( \pm2\e_2 \), also of area \( 2 \). They differ at \( \e_1 \), where they give \( 1 \) and \( 2 \). Part (b) does not apply because equal **area** is far weaker than equal **set**: the recipe in (a) reads the norm off the ball as a set of vectors, and the area of that set retains almost none of it.
:::
