# Convex Sets and Hulls

Convexity has turned up in this book four times without being asked for: in the unit balls of Chapter 15, the positive semidefinite matrices of Chapter 12, and the Ky Fan sums and the possible diagonals of Chapter 16 (the chapter introduction lists the places). Each time the property was checked by hand and set aside. This section gives it a name, finds the smallest convex set containing a given set, and fixes the words **closed** and **open** that the rest of the chapter needs.

**The field is \( \nR \), throughout the chapter.** The definition below asks for a scalar \( t \) with \( 0 \le t \le 1 \), which needs an order on the scalars; \( \nC \) has none. A complex space is treated as a real one by allowing only real scalars. That is how the Hermitian matrices enter below: they form a vector space over \( \nR \), and not over \( \nC \), since \( i\A \) is not Hermitian when \( \A \ne \0 \) is. Unless a statement says otherwise, \( V \) is a real vector space; where a result needs a finite dimension, a norm or an inner product, it says so.

## Segments, and sets that contain them

Chapter 15 §01 checked the convexity of a unit ball with one line: if \( \norm{\u}, \norm{\v} \le 1 \) and \( 0 \le t \le 1 \), then \( \norm{t\u + (1-t)\v} \le 1 \). The expression \( t\x + (1-t)\y \), with \( t \) running over \( [0, 1] \), keeps recurring, so it deserves a name, and so does the property of containing all of it.

Picture it first. At \( t = 1 \) the expression is \( \x \), at \( t = 0 \) it is \( \y \), and at \( t = \tfrac12 \) it is the midpoint. Writing it as \( \y + t(\x - \y) \) shows the rest: we start at \( \y \) and travel the fraction \( t \) of the way to \( \x \). As \( t \) runs over \( [0,1] \), the point runs along the straight **segment** from \( \y \) to \( \x \), and nowhere else.

*A convex set is one that contains the whole straight segment between any two of its points.*

::: {#def-convex-set}
[Convex Set]

Let \( V \) be a vector space **over \( \nR \)**. A subset \( C \subseteq V \) is **convex** if, **for all** \( \x, \y \in C \) and **every** real \( t \) with \( 0 \le t \le 1 \),
\[
t\x + (1-t)\y \in C .
\]
The set \( \{ t\x + (1-t)\y : 0 \le t \le 1 \} \) is the **segment** joining \( \x \) and \( \y \), written \( [\x, \y] \).
:::

In words: pick any two points of \( C \), possibly equal; the segment joining them must lie inside \( C \). The quantifier "for all \( \x, \y \)" is what makes this a property of the set rather than of a pair; one segment escaping \( C \) is enough to make it non-convex. The restriction \( 0 \le t \le 1 \) is the other half of the content, and the end of this subsection shows what happens without it. There is nothing to check for well-definedness: a subset either has the property or it does not.

::: {#exm-convex-first-examples}
[The first convex sets]

Check each of the following against @def-convex-set.

::: {.enumerate options="label=(\alph*)"}
1. The empty set, and a single point \( \{\p\} \).
2. A subspace \( U \) of \( V \), and a coset \( \p + U \) of it (@def-coset).
3. A **closed half-space** \( \{\x \in V : \varphi(\x) \le c\} \), where \( \varphi \) is a non-zero linear functional on \( V \) (@def-linear-functional) and \( c \in \nR \).
4. A closed ball \( \{\x \in V : \norm{\x - \p} \le r\} \) of any norm on \( V \), with center \( \p \) and radius \( r \ge 0 \).
5. The set of positive semidefinite matrices (@def-positive-semidefinite) in the real vector space of \( n \times n \) Hermitian matrices.
:::
:::

::: {.solution}
(a) The empty set has no two points, so the condition holds vacuously; for \( \{\p\} \), \( t\p + (1-t)\p = \p \). These degenerate cases matter because an intersection of convex sets, which we meet shortly, is often empty or a single point, and the statements below must allow for both.

(b) Let \( \x = \p + \u \) and \( \y = \p + \w \) with \( \u, \w \in U \). Then
\[
t\x + (1-t)\y = \p + \bigl(t\u + (1-t)\w\bigr) ,
\]
and \( t\u + (1-t)\w \in U \) because a subspace is closed under linear combinations. Taking \( \p = \0 \) gives the subspace itself. Here the restriction on \( t \) was not used at all; we return to this below.

(c) Let \( \varphi(\x) \le c \) and \( \varphi(\y) \le c \). By linearity,
\[
\varphi\bigl(t\x + (1-t)\y\bigr) = t\varphi(\x) + (1-t)\varphi(\y) \le tc + (1-t)c = c ,
\]
where the inequality multiplies the first hypothesis by \( t \) and the second by \( 1 - t \). Multiplying an inequality by a number preserves it only when the number is \( \ge 0 \), so both \( t \ge 0 \) and \( 1 - t \ge 0 \) were used. In \( \nR^n \) every linear functional is \( \x \mapsto \a\tp\x \) for some \( \a \) (@thm-functionals-on-fn), so the closed half-spaces of \( \nR^n \) are the sets \( \{\x : \a\tp\x \le c\} \) with \( \a \ne \0 \). The same computation shows that the **open half-space** \( \{\x : \varphi(\x) < c\} \) is convex, and that the **affine hyperplane** \( \{\x : \varphi(\x) = c\} \) is convex.

(d) Let \( \norm{\x - \p} \le r \) and \( \norm{\y - \p} \le r \). Since \( t\x + (1-t)\y - \p = t(\x - \p) + (1-t)(\y - \p) \), (N3) and (N2) of @def-norm give
\[
\norm{t\x + (1-t)\y - \p} \le t\norm{\x - \p} + (1-t)\norm{\y - \p} \le r ,
\]
where homogeneity used \( \lvert t \rvert = t \) and \( \lvert 1 - t\rvert = 1 - t \). With \( \p = \0 \) and \( r = 1 \) this is the closed unit ball of @def-unit-ball, and the computation is the one Chapter 15 §01 made there.

(e) The Hermitian matrices form a real vector space: a real linear combination of Hermitian matrices is Hermitian. Let \( \A \succeq 0 \) and \( \B \succeq 0 \). Then \( t\A + (1-t)\B \) is Hermitian, and for every \( \x \in \nC^n \),
\[
\inner{(t\A + (1-t)\B)\x}{\x} = t\inner{\A\x}{\x} + (1-t)\inner{\B\x}{\x} \ge 0 ,
\]
since both inner products on the right are \( \ge 0 \) by (P2) and both coefficients are \( \ge 0 \). So (P1) and (P2) hold, and \( t\A + (1-t)\B \succeq 0 \). The same computation with any \( s, t \ge 0 \) in place of \( t \) and \( 1 - t \) shows \( s\A + t\B \succeq 0 \), so the positive semidefinite matrices form a convex cone, in the sense of §05. (This is what @exr-positive-definite-matrices-c2 (a) asks.)
:::

The standard example of a convex set in coordinates gets its own name, because the rest of this section keeps returning to it.

::: {#def-standard-simplex}
[Standard Simplex]

For \( n \ge 1 \), the **standard simplex** in \( \nR^n \) is
\[
\Delta_n \coloneqq \Bigl\{ \t = (t_1, \dots, t_n) \in \nR^n : t_i \ge 0 \text{ for every } i,\ \ t_1 + \dots + t_n = 1 \Bigr\} .
\]
:::

\( \Delta_1 = \{1\} \) is a point, \( \Delta_2 \) is the segment from \( (1, 0) \) to \( (0, 1) \), and \( \Delta_3 \) is the triangle with corners \( \e_1, \e_2, \e_3 \). It is convex: it is the intersection of the \( n \) closed half-spaces \( \{t_i \ge 0\} \) with the affine hyperplane \( \{t_1 + \dots + t_n = 1\} \), and each of these is convex by @exm-convex-first-examples (c). (That an intersection of convex sets is convex is the first item of @prp-convexity-operations below; it is also immediate here, because a point that lies in each set lies in their intersection.) An element of \( \Delta_n \) is a list of \( n \) **weights**: non-negative, and adding up to \( 1 \).

\begin{center}
\begin{tikzpicture}[scale=1.25, lab/.style={font=\small}]
  \fill[black!10] (0,0) ellipse (1.1 and 0.7);
  \draw[thick] (0,0) ellipse (1.1 and 0.7);
  \draw[thick] (-0.6,-0.3) -- (0.7,0.35);
  \fill (-0.6,-0.3) circle (0.035);
  \fill (0.7,0.35) circle (0.035);
  \node[lab, below left] at (-0.6,-0.3) {$\mathbf{y}$};
  \node[lab, above right] at (0.7,0.35) {$\mathbf{x}$};
  \node[lab] at (0,-1.1) {convex};
  \begin{scope}[xshift=3.6cm]
    \fill[black!10] (-1,-0.7) -- (1,-0.7) -- (1,-0.1) -- (-0.3,-0.1) -- (-0.3,0.7) -- (-1,0.7) -- cycle;
    \draw[thick] (-1,-0.7) -- (1,-0.7) -- (1,-0.1) -- (-0.3,-0.1) -- (-0.3,0.7) -- (-1,0.7) -- cycle;
    \draw[thick, dashed] (-0.65,0.45) -- (0.7,-0.4);
    \fill (-0.65,0.45) circle (0.035);
    \fill (0.7,-0.4) circle (0.035);
    \node[lab, left] at (-0.65,0.45) {$\mathbf{x}$};
    \node[lab, below] at (0.7,-0.4) {$\mathbf{y}$};
    \node[lab] at (0,-1.1) {not convex: the dashed segment leaves the set};
  \end{scope}
\end{tikzpicture}
\end{center}

**A non-example by minimal change.** Keep the closed unit ball \( B_2 \) of \( \nR^2 \) but take only its edge, the unit circle \( \{\x : \norm{\x}_2 = 1\} \). Much survives: the circle is symmetric under \( \x \mapsto -\x \), bounded, and as round as the disc. But the clause "for all \( \x, \y \)" fails at \( \x = \e_1 \), \( \y = -\e_1 \), \( t = \tfrac12 \): the midpoint is \( \0 \), and \( \norm{\0}_2 = 0 \ne 1 \). What was lost is exactly the inequality \( \le 1 \) that absorbed the triangle inequality in @exm-convex-first-examples (d); with an equality there is nothing to absorb it.

**Why this definition.** Two variations are worth trying.

- *Let \( t \) range over all of \( \nR \).* Then \( C \) must contain the whole **line** through any two of its points. The subspaces and cosets of @exm-convex-first-examples meet this demand, which is why (b) never used \( 0 \le t \le 1 \); the half-spaces and balls do not. @exr-convex-sets-c3 shows that, apart from \( \emptyset \), the sets meeting it are exactly the cosets.
- *Ask only for \( t = \tfrac12 \).* A set containing the midpoint of any two of its points is **midpoint convex**, which is genuinely weaker: \( \nQ^2 \) is midpoint convex, yet it misses \( \tfrac{1}{\sqrt 2}\e_1 \in [\0, \e_1] \). @exr-convex-sets-c1 shows that the gap disappears for closed sets, defined at the end of this section.

The name is the everyday word: a convex lens has no dents.

::: {.warning}
**A union of convex sets need not be convex.** The two coordinate axes in \( \nR^2 \) are subspaces, hence convex, but their union contains \( \e_1 \) and \( \e_2 \) and not their midpoint \( (\tfrac12, \tfrac12) \), which lies on neither axis. Even two points fail: \( \{\0\} \cup \{\e_1\} \) is a union of two convex sets and misses \( \tfrac12\e_1 \). The operation that does respect convexity is intersection (@prp-convexity-operations), and the convex replacement for a union is the hull of the union, defined below.
:::

::: {.check}
Is \( \{(x, y) \in \nR^2 : y \ge \lvert x\rvert\} \) convex? Is \( \{(x, y) \in \nR^2 : y \le \lvert x\rvert\} \) convex?
:::

::: {.solution}
The first is convex. It is the set where both \( y - x \ge 0 \) and \( y + x \ge 0 \), an intersection of two closed half-spaces, and a point on a segment between two points of both half-spaces lies in both by @exm-convex-first-examples (c). The second is not: \( (1, 1) \) and \( (-1, 1) \) belong to it, since \( 1 \le 1 \), but their midpoint \( (0, 1) \) does not, since \( 1 \le 0 \) is false. The two sets differ only in the direction of the inequality, and the direction decides everything; a convex function such as \( \lvert x \rvert \) has a convex region **above** its graph (§10).
:::

Here is a payoff. Chapter 16 §08 met a set of vectors that it could describe exactly, but whose convexity it proved only in an exercise. Everything needed to prove it is now in place.

::: {#exm-majorization-set-convex}
[The vectors majorized by a fixed vector]

Let \( \vlambda \in \nR^n \). Prove that the set \( \{\d \in \nR^n : \d \prec \vlambda\} \) of vectors majorized by \( \vlambda \) (@def-majorization) is convex, and deduce that the diagonals of the Hermitian matrices with spectrum \( \vlambda \) form a convex set.
:::

::: {.solution}
For \( \x \in \nR^n \) and \( 1 \le k \le n \), write \( s_k(\x) = x^{\downarrow}_1 + \dots + x^{\downarrow}_k \), the sum of the \( k \) largest entries.

*Step 1: any \( k \) entries add up to at most \( s_k(\x) \).* List the entries \( x_i \) at a set \( I \) of \( k \) positions decreasingly as \( v_1 \ge \dots \ge v_k \). Since \( \x \) has \( j \) entries \( v_1, \dots, v_j \ge v_j \), we get \( x^{\downarrow}_j \ge v_j \) for each \( j \). Summing gives \( \sum_{i \in I} x_i \le s_k(\x) \), with equality when \( I \) holds the positions of the \( k \) largest entries.

*Step 2: \( s_k \) respects averages.* Let \( \x, \y \in \nR^n \) and \( 0 \le t \le 1 \), and let \( I \) hold the positions of the \( k \) largest entries of \( \z = t\x + (1-t)\y \). By Step 1, used once with equality and twice as an inequality,
\[
s_k(\z) = t\sum_{i \in I}x_i + (1-t)\sum_{i \in I}y_i \le t\,s_k(\x) + (1-t)\,s_k(\y) ,
\]
where the inequality again needs \( t \ge 0 \) and \( 1 - t \ge 0 \).

*Step 3: convexity.* Let \( \d \prec \vlambda \) and \( \d' \prec \vlambda \), and put \( \z = t\d + (1-t)\d' \). For \( k \le n - 1 \), Step 2 and (M1) for both vectors give \( s_k(\z) \le t\,s_k(\vlambda) + (1-t)\,s_k(\vlambda) = s_k(\vlambda) \). The total of \( \z \) is \( t\sum_i\lambda_i + (1-t)\sum_i\lambda_i = \sum_i\lambda_i \) by (M2) for both. So \( \z \prec \vlambda \), and the set is convex.

For the deduction, the Schur–Horn Theorem (@thm-schur-horn) says that the diagonals of the Hermitian matrices with eigenvalues \( \vlambda \) are **exactly** the vectors \( \d \prec \vlambda \). So the set of those diagonals is the set just shown to be convex.
:::

This is the statement of @exr-majorization-and-schur-c3, now with a proof in the text, and Step 2 is a first glimpse of §10's convex functions: \( s_k \) satisfies \( s_k(t\x + (1-t)\y) \le t\,s_k(\x) + (1-t)\,s_k(\y) \) because it is a maximum of linear functions.

## Operations that preserve convexity

Checking the definition directly is rarely the fastest route. Most convex sets are built from simpler ones by a few operations, and the following proposition lists those that preserve convexity. It needs one construction. For subsets \( A, B \subseteq V \) and a real \( c \), the **Minkowski sum** and the **scalar multiple** are
\[
A + B \coloneqq \{\a + \b : \a \in A,\ \b \in B\} , \qquad
cA \coloneqq \{c\a : \a \in A\} .
\]
A **translate** \( \p + A \) is the Minkowski sum \( \{\p\} + A \); a coset (@def-coset) is a translate of a subspace.

::: {#prp-convexity-operations}
[Operations Preserving Convexity]

Let \( V \) and \( W \) be real vector spaces.

::: {.enumerate options="label=(\alph*)"}
1. The intersection of **any** family of convex subsets of \( V \) is convex.
2. If \( T \colon V \to W \) is linear, \( C \subseteq V \) is convex and \( D \subseteq W \) is convex, then the image \( T(C) \) and the preimage \( T^{-1}(D) = \{\v \in V : T\v \in D\} \) are convex.
3. If \( A, B \subseteq V \) are convex and \( c \in \nR \), then \( A + B \), \( cA \) and every translate \( \p + A \) are convex.
:::
:::

::: {.idea}
Rewrite the point of the segment so that convexity of the given sets applies: linearity moves the weights through \( T \), and a Minkowski sum regroups term by term.
:::

::: {.proof}
Throughout, let \( 0 \le t \le 1 \).

(a) Let \( (C_\alpha) \) be a family of convex sets and \( \x, \y \in \bigcap_\alpha C_\alpha \). For each \( \alpha \), both points lie in \( C_\alpha \), so \( t\x + (1-t)\y \in C_\alpha \) by convexity of \( C_\alpha \). Hence the point lies in every \( C_\alpha \), that is, in the intersection. (The intersection of the empty family is \( V \) by convention, and \( V \) is convex.)

(b) Let \( T\x, T\y \in T(C) \) with \( \x, \y \in C \). By linearity, \( tT\x + (1-t)T\y = T\bigl(t\x + (1-t)\y\bigr) \), and \( t\x + (1-t)\y \in C \) by convexity; so the point lies in \( T(C) \). For the preimage, let \( T\x, T\y \in D \). Then \( T\bigl(t\x + (1-t)\y\bigr) = tT\x + (1-t)T\y \in D \) by convexity of \( D \), so \( t\x + (1-t)\y \in T^{-1}(D) \).

(c) Let \( \a + \b \) and \( \a' + \b' \) lie in \( A + B \). Rearranging,
\[
t(\a + \b) + (1-t)(\a' + \b') = \bigl(t\a + (1-t)\a'\bigr) + \bigl(t\b + (1-t)\b'\bigr) ,
\]
and the two brackets lie in \( A \) and in \( B \) by convexity. So the point lies in \( A + B \). The scalar multiple \( cA \) is the image of \( A \) under the linear map \( \v \mapsto c\v \), and is convex by (b). A translate \( \p + A = \{\p\} + A \) is convex because a single point is convex (@exm-convex-first-examples (a)). This proves the proposition.
:::

The proposition turns many checks into one line. The solution set of a system of linear inequalities,
\[
\{\x \in \nR^n : \A\x \le \b\} = \bigcap_{i=1}^{m} \{\x : \a_i\tp\x \le b_i\} ,
\]
where \( \a_i\tp \) is the \( i \)-th row of \( \A \in M_{m \times n}(\nR) \) and \( \A\x \le \b \) means \( \le \) in every entry, is an intersection of closed half-spaces (a zero row gives \( \nR^n \) or \( \emptyset \)), hence convex by (a). This is the kind of set that the closing remark of Chapter 2 §07 points to, where non-negativity and capacities are added to a flow problem, and §06 of this chapter optimizes over it. The set of **density matrices** \( \{\A : \A \succeq 0,\ \tr\A = 1\} \) is convex for the same reason: it is the intersection of the positive semidefinite set of @exm-convex-first-examples (e) with the preimage of \( \{1\} \) under the linear map \( \tr \).

## Convex combinations and the convex hull

A convex set contains the segment between any two of its points. Apply that twice: it contains \( \x_1 \), \( \x_2 \) and hence every point of \( [\x_1, \x_2] \), and then every point on a segment from such a point to \( \x_3 \). The points reached are the averages of \( \x_1, \x_2, \x_3 \) with non-negative weights, and the pattern deserves a name.

::: {#def-convex-combination}
[Convex Combination]

Let \( V \) be a real vector space and \( \x_1, \dots, \x_k \in V \), with \( k \ge 1 \). A **convex combination** of \( \x_1, \dots, \x_k \) is a vector
\[
t_1\x_1 + t_2\x_2 + \dots + t_k\x_k \qquad\text{with } (t_1, \dots, t_k) \in \Delta_k ,
\]
that is, with **every** \( t_i \ge 0 \) and \( t_1 + \dots + t_k = 1 \).
:::

It is a linear combination with two restrictions on the coefficients, and each restriction has a job. Dropping "\( t_i \ge 0 \)" gives the affine combinations of the next subsection; dropping "sum to \( 1 \)" as well gives all linear combinations, and the span. A convex combination of two points is a point of the segment joining them, with \( (t, 1-t) \) as the weights. The weights may be read as masses placed at the points, and the combination is then their center of mass. The case \( k = 1 \) is included and is \( 1 \cdot \x_1 = \x_1 \).

::: {#lem-convex-contains-combinations}
[Convex Sets Contain Their Convex Combinations]

Let \( C \) be a convex subset of a real vector space. Then every convex combination of points of \( C \) lies in \( C \).
:::

::: {.idea}
Peel off the last point. A convex combination of \( k \) points is a combination of two points, one of which is a convex combination of the first \( k - 1 \) points, rescaled so that its weights again add up to \( 1 \). Induction on \( k \) does the rest; the only care needed is not to divide by zero while rescaling.
:::

::: {.proof}
We use induction on the number \( k \) of points. For \( k = 1 \), the combination is \( \x_1 \in C \). Let \( k \ge 2 \), suppose the statement holds for \( k - 1 \) points, and let \( \x = \sum_{i=1}^{k} t_i\x_i \) with \( \x_i \in C \) and \( (t_1, \dots, t_k) \in \Delta_k \).

*Case 1: \( t_k = 1 \).* Then the other weights are non-negative and add up to \( 0 \), so all of them are \( 0 \), and \( \x = \x_k \in C \).

*Case 2: \( t_k < 1 \).* Put \( s = 1 - t_k > 0 \) and \( \y = \sum_{i=1}^{k-1} (t_i/s)\x_i \). The division is legal because \( s \ne 0 \). The coefficients \( t_i/s \) are \( \ge 0 \) and add up to \( (1 - t_k)/s = 1 \), so \( \y \) is a convex combination of \( k - 1 \) points of \( C \), and \( \y \in C \) by the inductive hypothesis. Then
\[
\x = s\y + t_k\x_k = (1 - t_k)\y + t_k\x_k ,
\]
which lies in \( C \) by @def-convex-set, applied to the points \( \x_k \) and \( \y \) of \( C \) with \( t = t_k \in [0, 1] \). This completes the induction.
:::

A set that is not convex can be enlarged to one that is. We want the most economical enlargement: nothing added that convexity does not force.

*The convex hull of a set is the smallest convex set containing it.*

::: {#def-convex-hull}
[Convex Hull]

Let \( S \) be a subset of a real vector space \( V \). The **convex hull** of \( S \) is the intersection of **all** convex subsets of \( V \) that contain \( S \):
\[
\conv S \coloneqq \bigcap\,\{ C \subseteq V : C \text{ is convex and } S \subseteq C \} .
\]
:::

The family being intersected is never empty, because \( V \) itself is convex and contains \( S \). By @prp-convexity-operations (a), \( \conv S \) is convex; it contains \( S \), since each set in the family does; and it lies inside every convex set containing \( S \), since it is the intersection of all of them. So "smallest" in the slogan is literal: \( \conv S \) is a convex set containing \( S \) and contained in every other one. In particular, \( \conv C = C \) **exactly when** \( C \) is convex. This description from outside is clean but gives no way to decide whether a given point lies in the hull. The next theorem gives the description from inside.

::: {#thm-convex-hull-combinations}
[The Hull Is the Set of Convex Combinations]

Let \( S \) be a subset of a real vector space \( V \). Then \( \conv S \) is the set of all convex combinations of points of \( S \):
\[
\conv S = \Bigl\{ \sum_{i=1}^{k} t_i\x_i : k \ge 1,\ \x_1, \dots, \x_k \in S,\ (t_1, \dots, t_k) \in \Delta_k \Bigr\} .
\]
:::

::: {.idea}
Call the right-hand side \( D \). One inclusion is @lem-convex-contains-combinations applied to the convex set \( \conv S \). For the other, \( \conv S \) is the smallest convex set containing \( S \), so it suffices to show that \( D \) is **some** convex set containing \( S \). An average of two averages is again an average, of the combined list.
:::

::: {.proof}
Let \( D \) denote the right-hand side.

\( (\supseteq) \) The set \( \conv S \) is convex and contains \( S \). By @lem-convex-contains-combinations it contains every convex combination of its own points, in particular of points of \( S \). Hence \( D \subseteq \conv S \).

\( (\subseteq) \) Each \( \x \in S \) is the convex combination \( 1 \cdot \x \), so \( S \subseteq D \). To see that \( D \) is convex, let \( \x = \sum_{i=1}^{k} a_i\x_i \) and \( \y = \sum_{j=1}^{l} b_j\y_j \) be points of \( D \), with all \( \x_i, \y_j \in S \), and let \( 0 \le t \le 1 \). Then
\[
t\x + (1-t)\y = \sum_{i=1}^{k} (ta_i)\x_i + \sum_{j=1}^{l} \bigl((1-t)b_j\bigr)\y_j ,
\]
a combination of the \( k + l \) points \( \x_1, \dots, \x_k, \y_1, \dots, \y_l \) of \( S \), with coefficients \( ta_i \ge 0 \) and \( (1-t)b_j \ge 0 \) adding up to \( t \cdot 1 + (1-t) \cdot 1 = 1 \). So \( t\x + (1-t)\y \in D \), and \( D \) is convex. Since \( \conv S \) is contained in every convex set containing \( S \), we get \( \conv S \subseteq D \).

This proves \( \conv S = D \).
:::

A combination needs a point, so \( \conv\emptyset = \emptyset \); and, padding with zero weights and merging repeated points, \( \conv\{\x_1, \dots, \x_m\} \) is the set of all \( \sum_i t_i\x_i \) with \( \t \in \Delta_m \); since \( \sum_i t_i\e_i = (t_1, \dots, t_n) \), **the standard simplex is the hull of the standard basis**.

The theorem does not say how many points a combination needs. Every \( k \) is allowed, and for an infinite \( S \) nothing in it bounds \( k \). That question is the business of §02.

::: {#exm-hull-membership}
[Deciding membership in a triangle]

Let \( \p_1 = (1, 0) \), \( \p_2 = (3, 1) \), \( \p_3 = (0, 2) \) in \( \nR^2 \). Decide whether \( \x = (\tfrac54, \tfrac34) \) and \( \y = (2, 2) \) lie in \( \conv\{\p_1, \p_2, \p_3\} \).
:::

::: {.solution}
By @thm-convex-hull-combinations and the remark after it, a point \( \z \) lies in the hull exactly when \( \z = t_1\p_1 + t_2\p_2 + t_3\p_3 \) for some \( \t \in \Delta_3 \). The two coordinates and the condition \( t_1 + t_2 + t_3 = 1 \) give three linear equations in \( t_1, t_2, t_3 \), with coefficient matrix
\[
\M = \begin{pmatrix} 1 & 3 & 0 \\ 0 & 1 & 2 \\ 1 & 1 & 1 \end{pmatrix} , \qquad \det\M = 5 \ne 0 .
\]
So each \( \z \) has exactly one solution \( \t \), and \( \z \) is in the hull if and only if that solution has no negative entry.

For \( \x \), the solution is \( \t = (\tfrac12, \tfrac14, \tfrac14) \). Check: \( \tfrac12(1, 0) + \tfrac14(3, 1) + \tfrac14(0, 2) = (\tfrac12 + \tfrac34, \tfrac14 + \tfrac12) = (\tfrac54, \tfrac34) \), and the weights add up to \( 1 \). All three are \( \ge 0 \), so \( \x \) lies in the hull.

For \( \y \), the solution is \( \t = (-\tfrac25, \tfrac45, \tfrac35) \). Check: \( -\tfrac25(1, 0) + \tfrac45(3, 1) + \tfrac35(0, 2) = (-\tfrac25 + \tfrac{12}5, \tfrac45 + \tfrac65) = (2, 2) \), and \( -\tfrac25 + \tfrac45 + \tfrac35 = 1 \). The only solution has \( t_1 < 0 \), so **no** convex combination equals \( \y \), and \( \y \notin \conv\{\p_1, \p_2, \p_3\} \). The negative weight even says where \( \y \) is: on the far side of the line through \( \p_2 \) and \( \p_3 \) from \( \p_1 \).
:::

::: {.check}
Is \( (\tfrac12, \tfrac12, \tfrac12) \) in the convex hull of \( \0, \ \e_1 + \e_2, \ \e_2 + \e_3, \ \e_1 + \e_3 \) in \( \nR^3 \)?
:::

::: {.solution}
Yes. Give each of the four points weight \( \tfrac14 \): the weights are \( \ge 0 \) and add up to \( 1 \), and
\[
\tfrac14\bigl(\0 + (\e_1 + \e_2) + (\e_2 + \e_3) + (\e_1 + \e_3)\bigr) = \tfrac14(2, 2, 2) = (\tfrac12, \tfrac12, \tfrac12) .
\]
By @thm-convex-hull-combinations, the point lies in the hull. One convex combination is a complete certificate of membership; proving **non**-membership, as for \( \y \) above, needs an argument about all combinations at once.
:::

## Affine combinations and the affine hull

Dropping the sign condition from a convex combination gives the other natural kind of average. It describes the flat pieces of \( V \): lines, planes, and their analogues, not necessarily through \( \0 \). Chapter 3 §09 already has these objects, as cosets \( \p + U \) of subspaces, and the point of this subsection is to connect them with combinations.

::: {#def-affine-hull}
[Affine Combination, Affine Hull]

Let \( V \) be a real vector space.

::: {.enumerate options="label=(\alph*)"}
1. An **affine combination** of \( \x_1, \dots, \x_k \in V \), \( k \ge 1 \), is a vector \( \sum_{i=1}^{k} t_i\x_i \) with real \( t_i \) satisfying \( t_1 + \dots + t_k = 1 \). No sign condition is imposed.
2. An **affine subspace** of \( V \) is a coset \( \p + U \) of a subspace \( U \) (@def-coset). Its **dimension** is \( \dim U \).
3. The **affine hull** of \( S \subseteq V \), written \( \operatorname{aff} S \), is the set of all affine combinations of points of \( S \).
:::
:::

The dimension in (b) is well defined, because the coset determines its subspace: \( U = \{\a - \b : \a, \b \in \p + U\} \). Indeed each such difference is \( (\p + \u) - (\p + \w) = \u - \w \in U \), and each \( \u \in U \) is the difference \( (\p + \u) - \p \). So a line in \( \nR^3 \) not through \( \0 \) is an affine subspace of dimension \( 1 \), and a single point \( \{\p\} = \p + \{\0\} \) is one of dimension \( 0 \).

::: {#prp-affine-hull-coset}
[The Affine Hull Is a Coset]

Let \( S \) be a **non-empty** subset of a real vector space \( V \), let \( \x_0 \in S \), and put \( U = \Span\{\x - \x_0 : \x \in S\} \). Then
\[
\operatorname{aff} S = \x_0 + U ,
\]
and \( \operatorname{aff} S \) is contained in every affine subspace of \( V \) that contains \( S \). In particular \( U \) does not depend on the choice of \( \x_0 \in S \).
:::

::: {.idea}
Since the weights add up to \( 1 \), an affine combination is \( \x_0 \) plus a linear combination of the differences \( \x_i - \x_0 \); that identity, read in both directions, gives the equality, and minimality follows because an affine subspace through \( \x_0 \) is \( \x_0 \) plus a subspace.
:::

::: {.proof}
\( (\subseteq) \) Let \( \x = \sum_i t_i\x_i \) with \( \x_i \in S \) and \( \sum_i t_i = 1 \). Since the \( t_i \) add up to \( 1 \), \( \x_0 = \sum_i t_i\x_0 \), and therefore
\[
\x = \x_0 + \sum_i t_i(\x_i - \x_0) \in \x_0 + U .
\]

\( (\supseteq) \) An element of \( \x_0 + U \) is \( \x_0 + \sum_{j} c_j(\y_j - \x_0) \) for some \( \y_j \in S \) and real \( c_j \), by @def-span. It equals
\[
\Bigl(1 - \sum_j c_j\Bigr)\x_0 + \sum_j c_j\y_j ,
\]
a combination of points of \( S \) whose coefficients add up to \( 1 \), hence an affine combination.

Now let \( \p + W \) be an affine subspace containing \( S \). Since \( \x_0 \in \p + W \), @lem-coset-equality (b) gives \( \p + W = \x_0 + W \). Each \( \x \in S \) also lies in \( \x_0 + W \), so \( \x - \x_0 \in W \). Thus \( W \) is a subspace containing every \( \x - \x_0 \), and \( U \subseteq W \) by @thm-span-subspace. Hence \( \operatorname{aff} S = \x_0 + U \subseteq \x_0 + W \). Finally, \( U \) is the subspace determined by the coset \( \operatorname{aff} S \), by the remark after @def-affine-hull, and that coset does not mention \( \x_0 \). This proves the proposition.
:::

So the affine hull is to affine subspaces what the span is to subspaces, and what the convex hull is to convex sets: the smallest one containing \( S \). It also gives every convex set a dimension. The **dimension** of a non-empty convex set \( C \) is \( \dim \operatorname{aff} C \). A segment in \( \nR^3 \) has dimension \( 1 \) and a triangle dimension \( 2 \). For \( \Delta_n \), take \( \x_0 = \e_1 \) in @prp-affine-hull-coset: each \( \t - \e_1 \) has coordinates adding up to \( 0 \), so \( U \) lies in the kernel \( H \) of \( \t \mapsto t_1 + \dots + t_n \), which has dimension \( n - 1 \) by @thm-rank-nullity (the map is onto \( \nR \)); and \( U \) contains the \( n - 1 \) vectors \( \e_i - \e_1 \) (\( i \ge 2 \)), independent because the \( i \)-th coordinate of \( \sum_{j \ge 2} c_j(\e_j - \e_1) \) is \( c_i \), so \( U = H \) by @thm-dim-impl-eq. Hence \( \Delta_n \) has dimension \( n - 1 \), and it is flat inside \( \nR^n \): no ball of positive radius fits inside it.

## Closed and open sets

The later sections take limits: §03 needs a nearest point of a convex set to exist, and §02 needs the hull of a compact set to be compact. Chapter 15 §02 used the right notion in passing, inside @cor-closed-bounded-compact; here it is given a name, together with its partner.

Throughout this subsection, \( V \) is a **finite-dimensional** real vector space with a norm \( \norm{\cdot} \). By @exm-induced-and-weighted-norms (a), an inner product space is a special case, with the induced norm. A sequence \( (\x_k) \) **converges** to \( \x \), written \( \x_k \to \x \), if \( \norm{\x_k - \x} \to 0 \). By @cor-convergence-norm-independent (a), whether \( \x_k \to \x \) does not depend on which norm is used, so neither does anything defined from it below.

*A closed set keeps the limits of its sequences. An open set is one that every sequence converging to one of its points must eventually enter.*

::: {#def-closed-set}
[Closed Set, Open Set]

Let \( V \) be a finite-dimensional real vector space with a norm, and let \( K, U \subseteq V \).

::: {.enumerate options="label=(\alph*)"}
1. \( K \) is **closed** if, **whenever** \( (\x_k) \) is a sequence of points **of \( K \)** with \( \x_k \to \x \) for some \( \x \in V \), the limit \( \x \) lies in \( K \).
2. \( U \) is **open** if, **whenever** \( \x_k \to \x \) with \( \x \in U \), there is an index \( N \) such that \( \x_k \in U \) for **every** \( k \ge N \).
:::

By @cor-convergence-norm-independent (a), both properties are the same for every norm on \( V \). Closedness in (a) is the notion used in @cor-closed-bounded-compact.
:::

In words: (a) demands that no convergent sequence inside \( K \) has its limit outside, and (b) that every sequence converging to a point of \( U \) is eventually inside \( U \). This is the sequential form, matching the way Chapter 15's introduction defines continuity; it is the form taken as the definition, and @prp-closed-open-basics (a) gives the equivalent ball form, which §03 and §10 use.

Continuity will be needed for linear maps, and in finite dimension it costs nothing.

::: {#lem-linear-map-lipschitz}
[Linear Maps Are Lipschitz]

Let \( V \) and \( W \) be finite-dimensional real vector spaces with norms, and let \( T \colon V \to W \) be linear. There is a constant \( M \ge 0 \) such that
\[
\norm{T\x - T\y} \le M\norm{\x - \y} \qquad \text{for all } \x, \y \in V .
\]
In particular \( \x_k \to \x \) implies \( T\x_k \to T\x \); and every linear functional \( \varphi \colon V \to \nR \), with \( \lvert\cdot\rvert \) as the norm on \( \nR \), is continuous.
:::

::: {.idea}
In a basis, \( \norm{T\x} \) is at most a constant times the \( 1 \)-norm of the coordinates of \( \x \), and norm equivalence trades that norm for the given one.
:::

::: {.proof}
If \( V = \{\0\} \), then \( T = 0 \) and \( M = 0 \) works. Otherwise let \( (\v_1, \dots, \v_n) \) be a basis of \( V \), and write \( \x = \sum_i x_i\v_i \). The function \( N(\x) = \sum_i \lvert x_i\rvert \) is a norm on \( V \): it is the \( 1 \)-norm of the coordinate vector (@exm-p-norms), and the coordinate map is linear (@thm-coordinates-linear) and injective, so (N1), (N2) and (N3) transfer. By @thm-norm-equivalence there is \( c > 0 \) with \( N(\x) \le c\norm{\x} \) for every \( \x \). By (N3) and (N2) of @def-norm in \( W \),
\[
\norm{T\x} = \Bigl\lVert \sum_i x_i T\v_i \Bigr\rVert \le \sum_i \lvert x_i\rvert\,\norm{T\v_i} \le \Bigl(\max_i \norm{T\v_i}\Bigr) N(\x) \le M\norm{\x} ,
\]
with \( M = c\max_i\norm{T\v_i} \). Applying this to \( \x - \y \) and using \( T\x - T\y = T(\x - \y) \) gives the inequality. If \( \norm{\x_k - \x} \to 0 \), then \( \norm{T\x_k - T\x} \le M\norm{\x_k - \x} \to 0 \). The statement about \( \varphi \) is the case \( W = \nR \).
:::

This is Step 1 of @lem-operator-norm-attained, with a basis of \( V \) in place of the standard basis of \( F^n \).

::: {#prp-closed-open-basics}
[Closed and Open Sets: First Facts]

Let \( V \) be a finite-dimensional real vector space with a norm.

::: {.enumerate options="label=(\alph*)"}
1. A subset \( U \subseteq V \) is open **if and only if** for every \( \x \in U \) there is a real \( r > 0 \) with \( \{\y \in V : \norm{\y - \x} < r\} \subseteq U \).
2. The intersection of any family of closed sets is closed, and the union of finitely many closed sets is closed.
3. For a linear functional \( \varphi \) on \( V \) and \( c \in \nR \), the sets \( \{\varphi \le c\} \), \( \{\varphi \ge c\} \) and \( \{\varphi = c\} \) are closed. Every closed ball \( \{\x : \norm{\x - \p} \le r\} \) is closed, and every subspace and every coset of a subspace is closed.
:::
:::

::: {.idea}
Each part unwinds the definitions. For the converse in (a), radii \( 1/k \) build a sequence breaking openness; for unions in (b), some set catches infinitely many terms.
:::

::: {.proof}
(a) \( (\Leftarrow) \) Let \( \x_k \to \x \in U \), and take \( r \) as in the hypothesis. Since \( \norm{\x_k - \x} \to 0 \), there is \( N \) with \( \norm{\x_k - \x} < r \) for \( k \ge N \), and then \( \x_k \in U \).

\( (\Rightarrow) \) Suppose some \( \x \in U \) has no such \( r \). Then for each \( k \ge 1 \) the radius \( r = 1/k \) fails, so there is \( \x_k \notin U \) with \( \norm{\x_k - \x} < 1/k \). Hence \( \x_k \to \x \in U \) while no \( \x_k \) lies in \( U \), and \( U \) is not open.

(b) Let \( (K_\alpha) \) be closed, and \( \x_k \to \x \) with every \( \x_k \in \bigcap_\alpha K_\alpha \). For each \( \alpha \), the sequence lies in \( K_\alpha \), so \( \x \in K_\alpha \). Hence \( \x \) lies in the intersection. For a union \( K_1 \cup \dots \cup K_m \): if \( \x_k \to \x \) with every \( \x_k \) in the union, then some \( K_i \) contains \( \x_k \) for infinitely many \( k \), because there are only \( m \) sets. Those terms form a subsequence of points of \( K_i \) converging to \( \x \), so \( \x \in K_i \) by closedness of \( K_i \).

(c) Let \( \varphi(\x_k) \le c \) for every \( k \), and \( \x_k \to \x \). By @lem-linear-map-lipschitz, \( \varphi(\x_k) \to \varphi(\x) \), and a non-strict inequality survives a limit, so \( \varphi(\x) \le c \). The same argument handles \( \ge \), and \( \{\varphi = c\} \) is the intersection of the two, closed by (b). For the ball, let \( \norm{\x_k - \p} \le r \) and \( \x_k \to \x \). By @lem-reverse-triangle-norm, \( \bigl\lvert\norm{\x_k - \p} - \norm{\x - \p}\bigr\rvert \le \norm{\x_k - \x} \to 0 \), so \( \norm{\x - \p} \) is the limit of numbers \( \le r \), and is \( \le r \).

Finally let \( U \) be a subspace, with basis \( (\u_1, \dots, \u_m) \). By @thm-basis-extension extend it to a basis \( (\u_1, \dots, \u_m, \v_{m+1}, \dots, \v_n) \) of \( V \), and let \( \varphi_j \), for \( m < j \le n \), send a vector to its coefficient on \( \v_j \); each \( \varphi_j \) is linear by @thm-coordinates-linear. A vector lies in \( U \) exactly when these coefficients all vanish, since the basis expansion is unique (@thm-unique-representation). So \( U = \bigcap_{j > m}\{\varphi_j = 0\} \), which is closed by the previous paragraph and (b); when \( m = n \), \( U = V \), which is closed because every limit lies in \( V \). A coset \( \p + U \) is closed because \( \x_k \to \x \) with \( \x_k \in \p + U \) gives \( \x_k - \p \to \x - \p \) with \( \x_k - \p \in U \), hence \( \x - \p \in U \). This proves the proposition.
:::

By (b) and (c), the solution set \( \{\x : \A\x \le \b\} \) of a system of linear inequalities is closed as well as convex, and so is \( \Delta_n \). An open ball \( \{\x : \norm{\x - \p} < r\} \) is open by (a): for \( \x \) in it, the radius \( r - \norm{\x - \p} > 0 \) works, by the triangle inequality.

::: {.warning}
**"Closed" is not the opposite of "open", and it is not "closed under an operation".** The interval \( [0, 1) \subseteq \nR \) is neither: \( 1 - 1/k \) stays inside and converges to \( 1 \notin [0, 1) \), and \( -1/k \) converges to \( 0 \in [0, 1) \) without ever entering it. At the other extreme, \( \emptyset \) and \( V \) are both closed and open. And \( \nQ^2 \) is closed under addition and midpoints, yet not a closed subset of \( \nR^2 \): by fact (A1) of Chapter 15's introduction, \( \sqrt2 \) is a limit of rationals \( q_k \), and \( (q_k, 0) \to (\sqrt2, 0) \).
:::

::: {.check}
Is the open half-plane \( \{(x, y) \in \nR^2 : x > 0\} \) closed? Is \( \Delta_n \) open in \( \nR^n \)?
:::

::: {.solution}
Neither. The points \( (1/k, 0) \) lie in the half-plane and converge to \( (0, 0) \), which does not, so the half-plane is not closed. For \( \Delta_n \), take \( \x = \e_1 \in \Delta_n \) and \( \x_k = (1 + 1/k)\e_1 \to \e_1 \); no \( \x_k \) lies in \( \Delta_n \), because its coordinates add up to \( 1 + 1/k \ne 1 \). So \( \Delta_n \) is not open, which is the flatness of the simplex seen through sequences. (It is closed, by (b) and (c) of @prp-closed-open-basics.)
:::

With convex sets, hulls and closed sets in hand, the question left open by @thm-convex-hull-combinations can be asked precisely: how many points does a convex combination need? The answer, in §02, depends only on the dimension, and it is what makes the hull of a compact set compact.

## Exercises

### A. Check your understanding

:::: {#exr-convex-sets-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State @def-convex-set and @def-convex-combination.
2. True or false: the union of two convex sets is convex. Justify your answer.
3. True or false: the intersection of two convex sets is convex. Justify your answer.
4. Explain why the sphere \( \{\x \in \nR^3 : \norm{\x}_2 = 1\} \) is **not** convex, naming the clause that fails.
5. Describe \( \conv S \) and \( \operatorname{aff} S \) for \( S = \{\e_1, \e_2\} \subseteq \nR^2 \).
6. Give a subset of \( \nR \) that is neither open nor closed, and one that is both.
:::
::::

::: {.solution}
(a) A subset \( C \) of a real vector space is convex if \( t\x + (1-t)\y \in C \) for all \( \x, \y \in C \) and every \( t \in [0, 1] \). A convex combination of \( \x_1, \dots, \x_k \) is \( \sum_i t_i\x_i \) with every \( t_i \ge 0 \) and \( \sum_i t_i = 1 \).

(b) False. The two coordinate axes of \( \nR^2 \) are convex, and their union contains \( \e_1, \e_2 \) but not \( \tfrac12(\e_1 + \e_2) \).

(c) True, by @prp-convexity-operations (a): a point of a segment between two points of both sets lies in each set, by convexity of each.

(d) The clause "for all \( \x, \y \in C \)" fails for \( \x = \e_1 \), \( \y = -\e_1 \), \( t = \tfrac12 \): both points lie on the sphere, and the midpoint \( \0 \) does not.

(e) By @thm-convex-hull-combinations, \( \conv S = \{t\e_1 + (1-t)\e_2 : 0 \le t \le 1\} \), the segment from \( \e_1 \) to \( \e_2 \), which is \( \Delta_2 \). By @def-affine-hull, \( \operatorname{aff} S = \{t\e_1 + (1-t)\e_2 : t \in \nR\} \), the whole line \( x_1 + x_2 = 1 \).

(f) \( [0, 1) \) is neither (see the warning above). \( \nR \) is both: every limit of real numbers lies in \( \nR \), so it is closed, and every sequence lies in \( \nR \), so it is open; the same holds for \( \emptyset \) vacuously.
:::

### B. Practice

:::: {#exr-convex-sets-b1}
[B1: Determine which are convex]

Determine which of the following sets are convex. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \{(x, y) \in \nR^2 : y \ge x^2\} \).
2. \( \{(x, y) \in \nR^2 : xy \ge 1\} \).
4. \( \{\A \in M_2(\nR) : \A\tp = \A,\ \det\A \ge 0\} \).
5. \( \{\x \in \nR^3 : x_1 + 2x_2 - x_3 = 4\} \).
:::
::::

::: {.solution}
Throughout, let \( 0 \le t \le 1 \).

(a) Convex. Let \( y \ge x^2 \) and \( y' \ge x'^2 \), and put \( x_t = tx + (1-t)x' \). Expanding,
\[
tx^2 + (1-t)x'^2 - x_t^2 = t(1-t)(x - x')^2 \ge 0 ,
\]
so \( ty + (1-t)y' \ge tx^2 + (1-t)x'^2 \ge x_t^2 \).

(b) Not convex. The points \( (1, 1) \) and \( (-1, -1) \) satisfy \( xy = 1 \), but their midpoint \( (0, 0) \) has \( xy = 0 < 1 \).

(c) Not convex. \( \A = \diag(1, 0) \) and \( \B = \diag(0, -1) \) are symmetric with \( \det\A = \det\B = 0 \), but \( \tfrac12(\A + \B) = \diag(\tfrac12, -\tfrac12) \) has determinant \( -\tfrac14 < 0 \).

(d) Convex. It is the affine hyperplane \( \{\varphi = 4\} \) for the linear functional \( \varphi(\x) = x_1 + 2x_2 - x_3 \), convex by @exm-convex-first-examples (c). It is also a coset of \( \ker\varphi \), convex by @exm-convex-first-examples (b).
:::

:::: {#exr-convex-sets-b2}
[B2: Membership in a hull]

Let \( \p_1 = (0, 0) \), \( \p_2 = (4, 1) \), \( \p_3 = (1, 3) \) in \( \nR^2 \). Decide whether \( (2, 2) \) and \( (3, 3) \) lie in \( \conv\{\p_1, \p_2, \p_3\} \). Justify your answer.
::::

::: {.solution}
As in @exm-hull-membership, \( \z \) lies in the hull exactly when the system \( t_1\p_1 + t_2\p_2 + t_3\p_3 = \z \), \( t_1 + t_2 + t_3 = 1 \) has a solution with every \( t_i \ge 0 \). Its coefficient matrix
\[
\begin{pmatrix} 0 & 4 & 1 \\ 0 & 1 & 3 \\ 1 & 1 & 1 \end{pmatrix}
\]
has determinant \( 11 \ne 0 \) (expand along the first column: \( 1 \cdot (4\cdot 3 - 1 \cdot 1) = 11 \)), so the solution is unique.

For \( \z = (2, 2) \): \( \t = (\tfrac1{11}, \tfrac4{11}, \tfrac6{11}) \). Check: \( \tfrac4{11}(4, 1) + \tfrac6{11}(1, 3) = (\tfrac{16 + 6}{11}, \tfrac{4 + 18}{11}) = (2, 2) \), and \( \tfrac{1 + 4 + 6}{11} = 1 \). All weights are \( \ge 0 \), so \( (2, 2) \) is in the hull.

For \( \z = (3, 3) \): \( \t = (-\tfrac4{11}, \tfrac6{11}, \tfrac9{11}) \). Check: \( \tfrac6{11}(4, 1) + \tfrac9{11}(1, 3) = (\tfrac{24 + 9}{11}, \tfrac{6 + 27}{11}) = (3, 3) \), and \( \tfrac{-4 + 6 + 9}{11} = 1 \). The unique solution has \( t_1 < 0 \), so no convex combination equals \( (3, 3) \), and it is not in the hull.
:::

### C. Going deeper

:::: {#exr-convex-sets-c1}
[C1: Midpoint convexity]

Let \( V \) be a finite-dimensional real vector space with a norm, and let \( C \subseteq V \) be **midpoint convex**: \( \tfrac12(\x + \y) \in C \) whenever \( \x, \y \in C \).

::: {.enumerate options="label=(\alph*)"}
1. Prove by induction on \( m \) that \( t\x + (1-t)\y \in C \) for all \( \x, \y \in C \) and every **dyadic** \( t = j/2^m \) with \( 0 \le j \le 2^m \).
2. Prove that if \( C \) is also closed, then \( C \) is convex.
3. Give a midpoint convex subset of \( \nR \) that is not convex, and say which hypothesis of (b) it violates.
:::

*Hint for (b): approximate \( t \) by \( \lfloor 2^m t\rfloor / 2^m \) (the floor exists and \( 2^{-m} \to 0 \) by the completeness of \( \nR \), fact (A1) of Chapter 15's introduction).*
::::

::: {.solution}
(a) For \( m = 0 \), \( t \in \{0, 1\} \) and the point is \( \y \) or \( \x \). Suppose the claim holds for \( m \), and let \( t = j/2^{m+1} \). If \( j \) is even, \( t = (j/2)/2^m \) and the inductive hypothesis applies. If \( j \) is odd, then \( t = \tfrac12(t_- + t_+) \) with \( t_\pm = (j \pm 1)/2^{m+1} = \tfrac{(j \pm 1)/2}{2^m} \), which are dyadic of level \( m \) and lie in \( [0, 1] \). By the inductive hypothesis \( \z_\pm = t_\pm\x + (1 - t_\pm)\y \in C \), and
\[
\tfrac12(\z_- + \z_+) = \tfrac12(t_- + t_+)\x + \bigl(1 - \tfrac12(t_- + t_+)\bigr)\y = t\x + (1-t)\y ,
\]
which lies in \( C \) by midpoint convexity.

(b) Let \( \x, \y \in C \) and \( t \in [0, 1] \). Put \( t_m = \lfloor 2^m t\rfloor/2^m \), a dyadic number in \( [0, 1] \) with \( 0 \le t - t_m < 2^{-m} \) (the floor exists and \( 2^{-m} \to 0 \) by the completeness of \( \nR \), fact (A1) of Chapter 15's introduction). By (a), \( \z_m = t_m\x + (1 - t_m)\y \in C \). Then
\[
\norm{\z_m - \bigl(t\x + (1-t)\y\bigr)} = \lvert t_m - t\rvert\,\norm{\x - \y} < 2^{-m}\norm{\x - \y} \to 0 ,
\]
so \( \z_m \to t\x + (1-t)\y \), and closedness of \( C \) puts the limit in \( C \). Hence \( C \) is convex.

(c) \( \nQ \subseteq \nR \). The midpoint of two rationals is rational, but \( 0, 1 \in \nQ \) while \( t\cdot 1 + (1-t)\cdot 0 = t \notin \nQ \) for \( t = 1/\sqrt2 \). The set is not closed: the rationals \( \lfloor 10^k/\sqrt2\rfloor/10^k \) converge to \( 1/\sqrt2 \) (the floor exists and \( 10^{-k} \to 0 \) by the completeness of \( \nR \), fact (A1) of Chapter 15's introduction).
:::

:::: {#exr-convex-sets-c3}
[C3: Sets that contain lines]

Let \( V \) be a real vector space and \( A \subseteq V \) a **non-empty** set containing \( t\x + (1-t)\y \) for all \( \x, \y \in A \) and **every** real \( t \).

::: {.enumerate options="label=(\alph*)"}
1. Fix \( \a \in A \) and put \( U = \{\x - \a : \x \in A\} \). Prove that \( U \) is a subspace of \( V \), so that \( A = \a + U \) is an affine subspace.
2. Hence prove that a non-empty \( S \subseteq V \) is an affine subspace if and only if \( S = \operatorname{aff} S \).
:::

*Hint for (a): for closure under addition, use a midpoint and then a scaling.*
::::

::: {.solution}
(a) \( \0 = \a - \a \in U \). *Scalars:* let \( \u = \x - \a \in U \) and \( c \in \nR \). The point \( c\x + (1-c)\a \) lies in \( A \) by hypothesis, and it equals \( \a + c\u \); so \( c\u \in U \). *Sums:* let \( \u = \x - \a \) and \( \w = \y - \a \) with \( \x, \y \in A \). The midpoint \( \m = \tfrac12\x + \tfrac12\y \in A \), so \( \tfrac12(\u + \w) = \m - \a \in U \), and by the scalar step with \( c = 2 \), \( \u + \w \in U \). By @thm-subspace-test, \( U \) is a subspace, and \( A = \a + U \) by the definition of \( U \).

(b) \( (\Leftarrow) \) If \( S = \operatorname{aff} S \), then \( S \) is a coset by @prp-affine-hull-coset. \( (\Rightarrow) \) If \( S = \p + W \) is an affine subspace, then \( \operatorname{aff} S \subseteq S \) by the minimality clause of @prp-affine-hull-coset, and \( S \subseteq \operatorname{aff} S \) because each \( \x \in S \) is the affine combination \( 1 \cdot \x \). So \( S = \operatorname{aff} S \).
:::
