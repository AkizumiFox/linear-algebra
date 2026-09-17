# Three Views of a Linear System

Chapter 1 kept running into the same kind of question. Is this vector in the span of those? Is this list independent? Every time, the question turned into a handful of equations in unknown coefficients, and we solved them by hand. This chapter gives those equations a name, looks at them from three sides, and turns solving them into an algorithm with a proof behind it. This first section sets up the language and answers a structural question before any computing: what can the set of all solutions look like?

## One system, three pictures

Here is a system of two equations in two unknowns, over \( \nR \):
\[
\begin{aligned}
2x - y &= 1, \\
x + y &= 5 .
\end{aligned}
\]
Adding the equations gives \( 3x = 6 \), so \( x = 2 \), and then \( y = 5 - x = 3 \). We can read this one small system in three different ways, and each will be useful.

**The row picture.** Each equation describes a line in the plane: \( y = 2x - 1 \) and \( y = 5 - x \). A solution is a point on **both** lines, so solving the system means intersecting them. The lines meet at \( (2, 3) \).

\begin{center}
\begin{tikzpicture}[scale=0.7]
  \draw[->] (-1.2,0) -- (5.6,0) node[right] {$x$};
  \draw[->] (0,-1.7) -- (0,6.4) node[above] {$y$};
  \draw[very thick] (-0.25,-1.5) -- (3.5,6) node[above right] {$2x - y = 1$};
  \draw[very thick, dashed] (-1,6) -- (5.5,-0.5) node[below left] {$x + y = 5$};
  \fill (2,3) circle (3pt);
  \node[right] at (2.15,3) {$(2, 3)$};
  \draw[dotted] (2,0) -- (2,3) -- (0,3);
\end{tikzpicture}
\end{center}

**The column picture.** Stack the coefficients of \( x \) into one column and those of \( y \) into another. The system says
\[
x \begin{pmatrix} 2 \\ 1 \end{pmatrix} + y \begin{pmatrix} -1 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 5 \end{pmatrix} .
\]
Now the unknowns are **weights**. We are asked how much of the vector \( \a_1 = (2, 1) \) and how much of \( \a_2 = (-1, 1) \) to combine to reach \( \b = (1, 5) \). The answer \( x = 2 \), \( y = 3 \) says: walk twice along \( \a_1 \), then three times along \( \a_2 \).

\begin{center}
\begin{tikzpicture}[scale=0.8]
  \draw[->] (-1.8,0) -- (4.8,0);
  \draw[->] (0,-0.5) -- (0,5.6);
  \draw[very thick, ->] (0,0) -- (2,1) node[below right] {$\mathbf{a}_1$};
  \draw[very thick, ->] (0,0) -- (-1,1) node[left] {$\mathbf{a}_2$};
  \draw[dashed, ->] (0,0) -- (4,2) node[right] {$2\mathbf{a}_1$};
  \draw[dashed, ->] (4,2) -- (1,5) node[midway, above right] {$3\mathbf{a}_2$};
  \draw[very thick, ->] (0,0) -- (1,5) node[above right] {$\mathbf{b} = 2\mathbf{a}_1 + 3\mathbf{a}_2$};
\end{tikzpicture}
\end{center}

**The matrix picture.** Collect the coefficients into a matrix and the unknowns into a column. By the definition of matrix multiplication (@def-matrix-multiplication), the system is the single equation
\[
\begin{pmatrix} 2 & -1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 1 \\ 5 \end{pmatrix}, \qquad \text{that is,} \qquad A\x = \b .
\]

The three pictures say the same thing, and they are tied together by one fact from Chapter 0: \( A\x = x_1\a_1 + \dots + x_n\a_n \), a combination of the columns of \( A \) weighted by the entries of \( \x \) (@thm-matrix-times-vector-columns). The row picture is the one we draw. The column picture connects to Chapter 1, since it asks whether \( \b \) lies in a span. The matrix picture is the one we compute and prove things with.

::: {.remark}
With more unknowns the pictures can no longer be drawn, but they do not change. An equation in three unknowns whose coefficients are not all zero describes a plane in \( \nR^3 \), and a system asks where several planes meet. In the column picture, three unknowns mean three columns, and we ask whether a combination of them hits \( \b \).
:::

## Linear systems

The example had two equations and two unknowns over \( \nR \). The general notion allows any numbers of each, and any field. Allowing any field is not generality for its own sake. Systems over \( \nF_2 \) describe parity checks and switching puzzles, and systems over \( \nQ \) are what a computer can solve exactly.

*A linear system is a finite list of equations, each saying that a fixed combination of the unknowns equals a fixed scalar.*

::: {#def-linear-system}
[Linear system]

Let \( F \) be a field and let \( m, n \ge 1 \). A **system of \( m \) linear equations in \( n \) unknowns** \( x_1, \dots, x_n \) **over \( F \)** is a list of equations
\[
\begin{aligned}
a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n &= b_1, \\
a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n &= b_2, \\
&\ \ \vdots \\
a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n &= b_m,
\end{aligned}
\]
where all \( a_{ij} \) and \( b_i \) lie in \( F \).

- The **coefficient matrix** is \( A = (a_{ij}) \in M_{m \times n}(F) \), the **right-hand side** is \( \b = (b_1, \dots, b_m) \in F^m \), and the system is written \( A\x = \b \).
- The **augmented matrix** is the \( m \times (n + 1) \) matrix \( [\, A \mid \b \,] \) obtained by appending \( \b \) to \( A \) as a last column.
- A **solution** is a vector \( \s = (s_1, \dots, s_n) \in F^n \) such that **every** equation holds when \( x_j = s_j \) for all \( j \); equivalently, \( A\s = \b \). The **solution set** is the set of all solutions, a subset of \( F^n \).
- The system is **consistent** if it has **at least one** solution, and **inconsistent** if its solution set is empty.
:::

In words: the coefficient matrix records the left-hand sides, row \( i \) for equation \( i \) and column \( j \) for unknown \( x_j \). The augmented matrix records the whole system, and it is the object we will manipulate in the next section. A solution is a single vector of \( F^n \), and it must satisfy all \( m \) equations at once, not just some of them. "Equivalently, \( A\s = \b \)" holds because the \( i \)-th entry of \( A\s \) is \( a_{i1}s_1 + \dots + a_{in}s_n \) by @def-matrix-multiplication, and two columns are equal exactly when all their entries agree.

Two small words deserve attention. A solution lives in \( F^n \), with entries in **the field \( F \)**: the equation \( 2x = 1 \) has the solution \( \tfrac12 \) over \( \nQ \), but over \( \nF_2 \) it reads \( 0 = 1 \) and has none. And "consistent" means **at least one** solution, not exactly one.

::: {#exm-three-kinds-of-solution-sets}
[None, one, or a whole line]

Find the solution set of each system over \( \nR \), and describe it in the row picture.

::: {.enumerate options="label=(\alph*)"}
1. \( x + 2y = 1 \), \( 2x + 4y = 5 \).
2. \( 2x - y = 1 \), \( x + y = 5 \).
3. \( x + 2y = 1 \), \( 2x + 4y = 2 \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Suppose \( (x, y) \) is a solution. Doubling the first equation gives \( 2x + 4y = 2 \), while the second says \( 2x + 4y = 5 \). Then \( 2 = 5 \), which is false. So there is no solution, and the system is **inconsistent**. In the row picture, the lines \( y = \tfrac12 - \tfrac12 x \) and \( y = \tfrac54 - \tfrac12 x \) have the same slope and different intercepts: they are parallel and never meet.
2. As computed at the start of the section, any solution has \( x = 2 \) and \( y = 3 \); conversely \( 2 \cdot 2 - 3 = 1 \) and \( 2 + 3 = 5 \). The solution set is \( \{ (2, 3) \} \), the single point where two non-parallel lines cross.
3. The second equation is twice the first, so a pair \( (x, y) \) satisfies both exactly when it satisfies \( x + 2y = 1 \), that is, when \( x = 1 - 2y \). Writing \( t \) for \( y \), the solution set is \( \{ (1 - 2t, t) : t \in \nR \} \). Both equations describe the **same** line, and every point on it is a solution.
:::
:::

The three answers are the three things two lines can do: miss, cross, or coincide. Over \( \nR \), and over any infinite field, no other sizes are possible: once we know the shape of the solution set (@thm-general-solution-structure below), this is a short argument, which you will give in @exr-linear-systems-c1. For instance, no system over \( \nR \) has exactly two solutions. Over a finite field the picture is different.

::: {#exm-system-over-f2-two-solutions}
[Exactly two solutions over \( \nF_2 \)]

Find all solutions of the system \( x + y + z = 1 \), \( y + z = 0 \) over \( \nF_2 \). Then compare with the same system over \( \nR \).
:::

::: {.solution}
In \( \nF_2 \) we have \( -1 = 1 \), so the second equation says \( y = -z = z \). Substituting into the first gives \( x + 2z = 1 \), and \( 2z = 0 \) in \( \nF_2 \), so \( x = 1 \). Conversely, every \( (1, z, z) \) satisfies both equations: \( 1 + z + z = 1 + 2z = 1 \) and \( z + z = 0 \). Since \( z \) can only be \( 0 \) or \( 1 \), the solution set is
\[
\{ (1, 0, 0),\ (1, 1, 1) \},
\]
with exactly two elements.

Over \( \nR \) the second equation gives \( y = -z \), and then the first gives \( x = 1 \). The solution set is \( \{ (1, -t, t) : t \in \nR \} \), a line in \( \nR^3 \) with infinitely many points. The equations are the same, but the field decides how many values the free unknown can take.
:::

Now a non-example, by a minimal change. The equation \( x + y^2 = 1 \) looks like one of the equations above, and it still has a left side built from the unknowns and a constant on the right. But the unknown \( y \) appears squared, so the left side is not of the form \( a_1x_1 + a_2x_2 \) with **fixed scalars** \( a_1, a_2 \). The clause that fails is "a fixed combination of the unknowns". Its solution set in \( \nR^2 \) is a parabola, not a line, and nothing in this chapter applies to it.

::: {.warning}
**"Consistent" does not mean "has exactly one solution".** The system \( x + 2y = 1 \), \( 2x + 4y = 2 \) of @exm-three-kinds-of-solution-sets (c) is consistent, and it has infinitely many solutions. Consistency only rules out the empty solution set. Whether the solution is unique is a separate question, answered by @cor-unique-solution-iff-trivial-kernel below.
:::

Why record the augmented matrix at all, when \( A\x = \b \) is shorter? Because solving a system never touches the names of the unknowns. Adding two equations adds their coefficients and their right-hand sides, and nothing else. The augmented matrix keeps exactly this data and throws away the symbols \( x_1, \dots, x_n \) and the plus signs. In the next section every manipulation is performed on it.

One kind of system is always consistent, because it has an obvious solution.

::: {#def-homogeneous-system}
[Homogeneous system]

A linear system \( A\x = \b \) over \( F \) is **homogeneous** if \( \b = \0 \). The vector \( \0 \in F^n \) is a solution of every homogeneous system \( A\x = \0 \), called the **trivial solution**. For any system \( A\x = \b \), the system \( A\x = \0 \), with the same coefficient matrix, is its **associated homogeneous system**.
:::

The trivial solution exists by the zero rule of @thm-matrix-multiplication-properties: \( A\0 = \0 \). So for a homogeneous system the interesting question is never "is there a solution?" but "is there a **non-trivial** one?". For example, \( x + 2y = 0 \), \( 2x + 4y = 0 \) has the non-trivial solution \( (-2, 1) \), while \( 2x - y = 0 \), \( x + y = 0 \) has only the trivial one: adding the equations gives \( 3x = 0 \), so \( x = 0 \), and then \( y = -x = 0 \).

:::: {.check}
Over \( \nR \), write the system \( x_1 - x_2 + 3x_3 = 4 \), \( 2x_2 + x_3 = 0 \) in the matrix picture and the column picture, and give its augmented matrix. Is \( (4, 0, 0) \) a solution? Is \( (1, 0, 1) \)?

::: {.solution}
With \( A = \begin{pmatrix} 1 & -1 & 3 \\ 0 & 2 & 1 \end{pmatrix} \) and \( \b = (4, 0) \), the system is \( A\x = \b \). In the column picture it reads \( x_1(1, 0) + x_2(-1, 2) + x_3(3, 1) = (4, 0) \). The augmented matrix is
\[
[\, A \mid \b \,] = \left[ \begin{array}{ccc|c} 1 & -1 & 3 & 4 \\ 0 & 2 & 1 & 0 \end{array} \right].
\]
For \( (4, 0, 0) \): \( 4 - 0 + 0 = 4 \) and \( 0 + 0 = 0 \), so it is a solution. For \( (1, 0, 1) \): the first equation gives \( 1 - 0 + 3 = 4 \), but the second gives \( 0 + 1 = 1 \neq 0 \). One failing equation is enough, so it is not a solution.
:::
::::

## Consistency is a question about span

The column picture turns "does this system have a solution?" into a question from Chapter 1.

::: {#thm-consistent-iff-column-span}
[Consistency and the span of the columns]

Let \( A \in M_{m \times n}(F) \) have columns \( \a_1, \dots, \a_n \in F^m \), and let \( \b \in F^m \). Then the system \( A\x = \b \) is consistent **if and only if** \( \b \in \Span(\a_1, \dots, \a_n) \). More precisely, \( \s = (s_1, \dots, s_n) \) is a solution exactly when \( \b = s_1\a_1 + \dots + s_n\a_n \).
:::

::: {.proof}
By @thm-matrix-times-vector-columns, \( A\s = s_1\a_1 + \dots + s_n\a_n \) for every \( \s \in F^n \). Hence \( \s \) is a solution, that is \( A\s = \b \), exactly when \( \b = s_1\a_1 + \dots + s_n\a_n \). This proves the second statement.

(⇒) If the system is consistent, it has a solution \( \s \), and then \( \b = s_1\a_1 + \dots + s_n\a_n \) is a linear combination of the columns. By @def-span, \( \b \in \Span(\a_1, \dots, \a_n) \).

(⇐) If \( \b \in \Span(\a_1, \dots, \a_n) \), then \( \b = s_1\a_1 + \dots + s_n\a_n \) for some \( s_1, \dots, s_n \in F \), and \( \s = (s_1, \dots, s_n) \) is a solution by the first paragraph. Hence the system is consistent.
:::

Read backwards, the theorem is a recipe for Chapter 1 questions: to decide whether \( \b \) lies in the span of some vectors of \( F^m \), put the vectors as the columns of a matrix and ask whether the system is consistent.

::: {#exm-span-membership-by-system}
[Span membership as a system]

In \( \nR^3 \), let \( \v_1 = (1, 2, 3) \) and \( \v_2 = (0, 1, 2) \). Decide whether \( (1, 4, 7) \) and \( (1, 4, 8) \) lie in \( \Span(\v_1, \v_2) \).
:::

::: {.solution}
Let \( A \) be the \( 3 \times 2 \) matrix with columns \( \v_1, \v_2 \). By @thm-consistent-iff-column-span, \( (1, 4, 7) \in \Span(\v_1, \v_2) \) if and only if the system
\[
a = 1, \qquad 2a + b = 4, \qquad 3a + 2b = 7
\]
in the unknowns \( a, b \) is consistent. The first equation gives \( a = 1 \), and then the second gives \( b = 2 \). The third equation must also hold, and it does: \( 3 + 4 = 7 \). Hence \( (1, 4, 7) = \v_1 + 2\v_2 \) lies in the span.

For \( (1, 4, 8) \), the first two equations are the same, so any solution has \( a = 1 \) and \( b = 2 \). The third equation now demands \( 3 + 4 = 8 \), which is false. The system is inconsistent, so \( (1, 4, 8) \notin \Span(\v_1, \v_2) \).
:::

Geometrically, \( \Span(\v_1, \v_2) \) is a plane through \( \0 \) in \( \nR^3 \). The first right-hand side lies on that plane and the second does not.

## The shape of the solution set

We now describe the solution set of an arbitrary system, starting with the homogeneous case. Chapter 1 already did the work there: in @exm-null-space-subspace we checked, with the three conditions of the subspace test, that the solutions of \( A\x = \0 \) form a subspace.

::: {#thm-homogeneous-solutions-subspace}
[Homogeneous solutions form a subspace]

Let \( A \in M_{m \times n}(F) \). The solution set \( N = \{ \x \in F^n : A\x = \0 \} \) of the homogeneous system \( A\x = \0 \) is a subspace of \( F^n \).
:::

::: {.proof}
This is @exm-null-space-subspace: \( A\0 = \0 \), and for \( \x, \y \in N \) and \( c \in F \), the rules of @thm-matrix-multiplication-properties give \( A(\x + \y) = A\x + A\y = \0 \) and \( A(c\x) = c(A\x) = \0 \). By the subspace test (@thm-subspace-test), \( N \) is a subspace of \( F^n \).
:::

The solutions of \( A\x = \b \) with \( \b \neq \0 \) behave differently.

::: {.warning}
**The solution set of \( A\x = \b \) with \( \b \neq \0 \) is never a subspace.** A subspace must contain \( \0 \), but \( A\0 = \0 \neq \b \), so \( \0 \) is not a solution. For example, the solutions of \( x - y = 1 \) in \( \nR^2 \) form a line that misses the origin. The sum of the solutions \( (1, 0) \) and \( (2, 1) \) is \( (3, 1) \), and \( 3 - 1 = 2 \neq 1 \): adding two solutions does not give a solution.
:::

What does survive is this: the **difference** of two solutions of \( A\x = \b \) solves the homogeneous system, since \( A(\s - \s') = \b - \b = \0 \). So once one solution is known, every other one differs from it by a homogeneous solution. That is the whole structure.

::: {#thm-general-solution-structure}
[Structure of the solution set]

Let \( A \in M_{m \times n}(F) \) and \( \b \in F^m \), let \( N \) be the solution set of \( A\x = \0 \), and suppose \( \p \in F^n \) is **one** solution of \( A\x = \b \). Then the solution set of \( A\x = \b \) is
\[
\p + N = \{ \p + \h : \h \in N \}.
\]
:::

::: {.idea}
The theorem is "particular plus homogeneous". To prove equality of two sets, prove both inclusions. Going from a solution \( \s \) to \( \p + N \) uses the difference \( \s - \p \), as observed above; going back uses the sum \( A(\p + \h) = A\p + A\h \).
:::

::: {.proof}
Let \( S \) be the solution set of \( A\x = \b \). We use @thm-double-inclusion.

(⊆) Let \( \s \in S \), and put \( \h = \s - \p \). By distributivity (@thm-matrix-multiplication-properties), \( A\h = A\s - A\p = \b - \b = \0 \), so \( \h \in N \). Hence \( \s = \p + \h \in \p + N \).

(⊇) Let \( \h \in N \). Then \( A(\p + \h) = A\p + A\h = \b + \0 = \b \), again by distributivity, so \( \p + \h \in S \).

Therefore \( S = \p + N \), as claimed.
:::

The theorem splits solving \( A\x = \b \) into two independent jobs: find **one** solution, and find **all** solutions of the homogeneous system. The set \( \p + N \) is a translate of the subspace \( N \) by the vector \( \p \), the kind of set that the picture in @exm-line-not-subspace showed. For \( x - y = 1 \) in \( \nR^2 \), the homogeneous solutions form the line \( N = \Span((1, 1)) \) through \( \0 \), one solution is \( \p = (1, 0) \), and the solution set is the parallel line through \( \p \).

\begin{center}
\begin{tikzpicture}[scale=0.8]
  \draw[->] (-2.4,0) -- (3.6,0) node[right] {$x$};
  \draw[->] (0,-2.4) -- (0,3) node[above] {$y$};
  \draw[very thick] (-2.2,-2.2) -- (2.8,2.8) node[above] {$N$: $x - y = 0$};
  \draw[very thick, dashed] (-1.2,-2.2) -- (3.4,2.4) node[below right] {$\mathbf{p} + N$: $x - y = 1$};
  \fill (0,0) circle (2pt) node[above left] {$\mathbf{0}$};
  \draw[->, thick] (0,0) -- (1,0) node[below] {$\mathbf{p}$};
  \draw[->, thick] (0,0) -- (1.5,1.5) node[above left] {$\mathbf{h}$};
  \draw[dotted, thick] (1.5,1.5) -- (2.5,1.5);
  \fill (2.5,1.5) circle (2pt) node[below right] {$\mathbf{p} + \mathbf{h}$};
\end{tikzpicture}
\end{center}

A system solved by substitution fits the same pattern once we collect the free parameter.

::: {#exm-solution-set-p-plus-span}
[Particular plus homogeneous]

Solve \( x_1 + 2x_2 - x_3 = 4 \), \( x_2 + x_3 = 1 \) over \( \nR \), and write the solution set in the form \( \p + \Span(\h) \).
:::

::: {.solution}
The second equation gives \( x_2 = 1 - x_3 \). Substituting into the first, \( x_1 = 4 - 2(1 - x_3) + x_3 = 2 + 3x_3 \). The value of \( x_3 \) is not constrained, so write \( x_3 = t \). Conversely, for every \( t \in \nR \) the vector \( (2 + 3t, 1 - t, t) \) satisfies both equations, since \( (2 + 3t) + 2(1 - t) - t = 4 \) and \( (1 - t) + t = 1 \). Hence the solution set is
\[
\{ (2 + 3t, 1 - t, t) : t \in \nR \} = \{ (2, 1, 0) + t(3, -1, 1) : t \in \nR \} = \p + \Span(\h),
\]
with \( \p = (2, 1, 0) \) and \( \h = (3, -1, 1) \). As @thm-general-solution-structure predicts, \( \p \) is a solution (take \( t = 0 \)), and \( \h \) solves the homogeneous system: \( 3 - 2 - 1 = 0 \) and \( -1 + 1 = 0 \). In the row picture, two planes in \( \nR^3 \) meet in a line, and this line does not pass through \( \0 \).
:::

## When is the solution unique?

A consistent system has a unique solution exactly when there is nothing to add to the particular solution. The theorem just proved turns this into a statement about the homogeneous system, and the column picture turns that into independence.

::: {#cor-unique-solution-iff-trivial-kernel}
[Uniqueness of solutions]

Let \( A \in M_{m \times n}(F) \) have columns \( \a_1, \dots, \a_n \), and let \( \b \in F^m \) be such that \( A\x = \b \) is **consistent**. The following are equivalent:

::: {.enumerate options="label=(\alph*)"}
1. \( A\x = \b \) has exactly one solution;
2. \( A\x = \0 \) has only the trivial solution;
3. the list \( (\a_1, \dots, \a_n) \) is linearly independent.
:::
:::

::: {.proof}
Let \( N \) be the solution set of \( A\x = \0 \). Since the system is consistent, it has a solution \( \p \), and by @thm-general-solution-structure its solution set is \( \p + N \).

(a ⇔ b) The function \( N \to \p + N \), \( \h \mapsto \p + \h \), is surjective by definition of \( \p + N \), and injective because \( \p + \h = \p + \h' \) implies \( \h = \h' \) by adding \( -\p \) to both sides. So it is a bijection, and \( \p + N \) has exactly one element if and only if \( N \) does. Since \( \0 \in N \) always, \( N \) has exactly one element if and only if \( N = \{ \0 \} \), which is (b).

(b ⇔ c) By @thm-matrix-times-vector-columns, \( A\x = x_1\a_1 + \dots + x_n\a_n \) for every \( \x \in F^n \). So (b) says: for all \( x_1, \dots, x_n \in F \), \( x_1\a_1 + \dots + x_n\a_n = \0 \) implies \( x_1 = \dots = x_n = 0 \). This is word for word @def-linear-independence for the list \( (\a_1, \dots, \a_n) \).
:::

Two remarks on the hypotheses. The equivalence of (b) and (c) does not need consistency; only (a) does. And consistency cannot be dropped from (a ⇔ b): the system \( x = 0 \), \( x = 1 \) in one unknown has only the trivial solution in its homogeneous version (\( x = 0 \), \( x = 0 \)), but it has no solution at all, so it certainly does not have exactly one.

So the three pictures answer the two basic questions about \( A\x = \b \) in the language of Chapter 1: a solution **exists** when \( \b \) is in the span of the columns, and it is **unique** when the columns are independent. What we still lack is a reliable way to decide either question for a given matrix. That is the job of Gaussian elimination, in the next section.

## Exercises

### A. Check your understanding

::: {#exr-linear-systems-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define what it means for a linear system \( A\x = \b \) over \( F \) to be consistent, and what its augmented matrix is. What is the size of the augmented matrix of a system of \( m \) equations in \( n \) unknowns?
2. Determine whether the following statement is true: "the solution set of \( A\x = \b \) is a subspace of \( F^n \)." Justify your answer.
3. Determine whether the following statement is true: "if \( A\x = \b \) has two different solutions, then \( A\x = \0 \) has a non-trivial solution." Justify your answer.
4. Let \( A \in M_{3 \times 5}(\nR) \). In which spaces do the unknown vector \( \x \) and the right-hand side \( \b \) of \( A\x = \b \) live?
5. Name the theorem that turns "is \( \b \) in the span of \( \a_1, \dots, \a_n \)?" into a question about a linear system, and state which system.
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. It is consistent if it has at least one solution \( \s \in F^n \), that is, some \( \s \) with \( A\s = \b \). The augmented matrix is \( [\, A \mid \b \,] \), the matrix \( A \) with \( \b \) appended as an extra last column. It has size \( m \times (n + 1) \).
2. False in general. If \( \b \neq \0 \), then \( A\0 = \0 \neq \b \), so \( \0 \) is not a solution and the solution set is not a subspace. (If \( \b = \0 \), it is a subspace, by @thm-homogeneous-solutions-subspace.)
3. True. If \( \s \neq \s' \) are solutions, then \( A(\s - \s') = \b - \b = \0 \) by distributivity, and \( \s - \s' \neq \0 \).
4. \( \x \in \nR^5 \), one entry per column of \( A \), and \( \b \in \nR^3 \), one entry per row.
5. @thm-consistent-iff-column-span: \( \b \in \Span(\a_1, \dots, \a_n) \) if and only if \( A\x = \b \) is consistent, where \( A \) is the matrix with columns \( \a_1, \dots, \a_n \).
:::
:::

### B. Practice

::: {#exr-linear-systems-b1}
[B1: Three views]

::: {.enumerate options="label=(\alph*)"}
1. Write the system \( x_1 - x_2 + 2x_3 = 3 \), \( 2x_1 + x_3 = 1 \) over \( \nR \) in the matrix picture and in the column picture, and give its augmented matrix.
2. Write out, as a list of equations, the system with augmented matrix \( \left[ \begin{array}{cc|c} 1 & 4 & 0 \\ 0 & 1 & 2 \\ 3 & -1 & 5 \end{array} \right] \) over \( \nR \). How many equations and unknowns does it have? Hence decide whether it is consistent.
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. The matrix picture is
\[
\begin{pmatrix} 1 & -1 & 2 \\ 2 & 0 & 1 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 3 \\ 1 \end{pmatrix}.
\]
The column picture is \( x_1(1, 2) + x_2(-1, 0) + x_3(2, 1) = (3, 1) \). The augmented matrix is \( \left[ \begin{array}{ccc|c} 1 & -1 & 2 & 3 \\ 2 & 0 & 1 & 1 \end{array} \right] \).
2. The system is \( x_1 + 4x_2 = 0 \), \( x_2 = 2 \), \( 3x_1 - x_2 = 5 \): three equations in two unknowns. The second equation gives \( x_2 = 2 \), and then the first gives \( x_1 = -8 \). The third equation would require \( -24 - 2 = 5 \), which is false. Hence no vector satisfies all three equations, and the system is inconsistent.
:::
:::

::: {#exr-linear-systems-b2}
[B2: In the span or not?]

Determine whether the vector \( \b \) lies in the span of the given vectors. Justify your answer, and when it does, write \( \b \) as a linear combination of them.

::: {.enumerate options="label=(\alph*)"}
1. \( \b = (2, 1, 4) \) and \( (1, 0, 1), (0, 1, 2) \) in \( \nR^3 \).
2. \( \b = (1, 1, 1) \) and \( (1, 2, 0), (2, 4, 1) \) in \( \nR^3 \).
3. \( \b = (1, 1, 0) \) and \( (1, 0, 1), (0, 1, 1) \) in \( \nF_2^3 \). Is the answer the same in \( \nR^3 \)?
:::
:::

::: {.solution}
By @thm-consistent-iff-column-span, in each case we decide whether the system \( a\v_1 + b\v_2 = \b \) in the unknowns \( a, b \) is consistent.

::: {.enumerate options="label=(\alph*)"}
1. The system is \( a = 2 \), \( b = 1 \), \( a + 2b = 4 \). The first two equations force \( a = 2 \), \( b = 1 \), and then \( a + 2b = 4 \) holds. Hence \( (2, 1, 4) = 2(1, 0, 1) + (0, 1, 2) \) is in the span.
2. The system is \( a + 2b = 1 \), \( 2a + 4b = 1 \), \( b = 1 \). Doubling the first equation gives \( 2a + 4b = 2 \), contradicting the second, since \( 2 \neq 1 \). Hence the system is inconsistent and \( (1, 1, 1) \) is not in the span.
3. The system is \( a = 1 \), \( b = 1 \), \( a + b = 0 \). The first two force \( a = b = 1 \), and then \( a + b = 1 + 1 = 0 \) in \( \nF_2 \). Hence \( (1, 1, 0) = (1, 0, 1) + (0, 1, 1) \) is in the span over \( \nF_2 \). In \( \nR^3 \) the same first two equations force \( a = b = 1 \), but \( 1 + 1 = 2 \neq 0 \), so the system is inconsistent and \( \b \) is **not** in the span. The answer depends on the field.
:::
:::

::: {#exr-linear-systems-b3}
[B3: Solve and describe]

Solve each system over \( \nR \) by substitution, and write its solution set in the form \( \p + \Span(\dots) \). Check that your \( \p \) is a solution and that your spanning vectors solve the associated homogeneous system.

::: {.enumerate options="label=(\alph*)"}
1. \( x_1 + x_2 + x_3 = 2 \), \( x_2 - x_3 = 1 \).
2. \( x_1 - 2x_2 + x_3 - x_4 = 1 \), \( x_3 + 2x_4 = 3 \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. The second equation gives \( x_2 = 1 + x_3 \), and then the first gives \( x_1 = 2 - (1 + x_3) - x_3 = 1 - 2x_3 \). With \( x_3 = t \) free, every solution is \( (1 - 2t, 1 + t, t) \), and conversely each such vector satisfies both equations. So the solution set is \( (1, 1, 0) + \Span((-2, 1, 1)) \). Check: \( 1 + 1 + 0 = 2 \) and \( 1 - 0 = 1 \); and \( -2 + 1 + 1 = 0 \), \( 1 - 1 = 0 \).
2. The second equation gives \( x_3 = 3 - 2x_4 \). The first then gives \( x_1 = 1 + 2x_2 - (3 - 2x_4) + x_4 = -2 + 2x_2 + 3x_4 \). The unknowns \( x_2 = s \) and \( x_4 = t \) are free, and every solution is
\[
(-2 + 2s + 3t,\ s,\ 3 - 2t,\ t) = (-2, 0, 3, 0) + s(2, 1, 0, 0) + t(3, 0, -2, 1),
\]
and conversely each such vector is a solution. So the solution set is \( (-2, 0, 3, 0) + \Span((2, 1, 0, 0), (3, 0, -2, 1)) \). Check: \( -2 - 0 + 3 - 0 = 1 \) and \( 3 + 0 = 3 \); for \( (2, 1, 0, 0) \): \( 2 - 2 + 0 - 0 = 0 \) and \( 0 + 0 = 0 \); for \( (3, 0, -2, 1) \): \( 3 - 0 - 2 - 1 = 0 \) and \( -2 + 2 = 0 \).
:::
:::

### C. Going deeper

::: {#exr-linear-systems-c1}
[C1: How many solutions?]

Let \( A \in M_{m \times n}(F) \) and \( \b \in F^m \), and let \( N \) be the solution set of \( A\x = \0 \).

::: {.enumerate options="label=(\alph*)"}
1. Suppose \( F \) is **infinite**. Prove that \( A\x = \b \) has either no solution, exactly one solution, or infinitely many solutions.
2. Suppose \( F \) is **finite**. Prove that \( A\x = \b \) has either no solution or exactly \( \lvert N \rvert \) solutions.
3. Give a system over \( \nF_3 \) with exactly three solutions.
:::

*Hint: for (a), if \( N \) contains a non-zero vector \( \h \), look at its multiples.*
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Suppose the system is consistent, with a solution \( \p \). By @thm-general-solution-structure its solution set is \( \p + N \), and as in the proof of @cor-unique-solution-iff-trivial-kernel the map \( \h \mapsto \p + \h \) is a bijection \( N \to \p + N \). If \( N = \{ \0 \} \), there is exactly one solution. Otherwise, let \( \h \in N \) with \( \h \neq \0 \). Since \( N \) is a subspace (@thm-homogeneous-solutions-subspace), \( c\h \in N \) for every \( c \in F \). If \( c\h = c'\h \), then \( (c - c')\h = \0 \), and since \( \h \neq \0 \), @thm-zero-product gives \( c = c' \). So \( c \mapsto c\h \) is injective, and \( N \) contains infinitely many vectors because \( F \) is infinite. Hence \( \p + N \) is infinite.
2. If the system is consistent with solution \( \p \), the bijection \( N \to \p + N \) from (a) shows that the solution set has exactly \( \lvert N \rvert \) elements. Otherwise it has none.
3. The single equation \( x + y = 1 \) over \( \nF_3 \) (a system with \( m = 1 \), \( n = 2 \)). For each of the three values of \( y \in \nF_3 \) there is exactly one \( x = 1 - y \), so the solutions are \( (1, 0), (0, 1), (2, 2) \). Consistently with (b), the homogeneous equation \( x + y = 0 \) has the three solutions \( (0, 0), (2, 1), (1, 2) \).
:::
:::

::: {#exr-linear-systems-c2}
[C2: The right-hand sides that work]

Let \( A \in M_{m \times n}(F) \) have columns \( \a_1, \dots, \a_n \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that the set \( C = \{ \b \in F^m : A\x = \b \text{ is consistent} \} \) is a subspace of \( F^m \).
2. Deduce that if \( n < m \), then there is some \( \b \in F^m \) for which \( A\x = \b \) is inconsistent.
3. For \( A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \\ 0 & 1 \end{pmatrix} \) over \( \nR \), find one such \( \b \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. By @thm-consistent-iff-column-span, \( \b \in C \) if and only if \( \b \in \Span(\a_1, \dots, \a_n) \). So \( C = \Span(\a_1, \dots, \a_n) \), which is a subspace of \( F^m \) by @thm-span-subspace.
2. By (a), \( C \) is spanned by the \( n \) vectors \( \a_1, \dots, \a_n \). Since \( \dim F^m = m \) (@exm-dimensions), @thm-size-bounds says no list of fewer than \( m \) vectors spans \( F^m \). As \( n < m \), \( C \neq F^m \), so some \( \b \in F^m \) is not in \( C \), and for that \( \b \) the system is inconsistent.
3. Take \( \b = (1, 0, 0) \). A solution would satisfy \( x + 2y = 1 \) and \( 2x + 4y = 0 \). Doubling the first gives \( 2x + 4y = 2 \neq 0 \), a contradiction. So \( A\x = (1, 0, 0) \) is inconsistent.
:::
:::
