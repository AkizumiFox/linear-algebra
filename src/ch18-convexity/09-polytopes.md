# Polytopes

There are two ways to pin down a convex set with finitely many numbers. One lists finitely many points and takes their convex hull; the other lists finitely many linear inequalities and takes their common solutions. A triangle can be given either way, by its three corners or by its three sides. This section proves that for bounded sets the two descriptions always describe the same sets, which is the Minkowski–Weyl theorem. On the way it locates the optima of Section 6's linear programs over bounded regions: they occur at corners, and a corner of \( \{\x : \A\x \le \b\} \) can be recognized by a rank condition on the constraints that hold with equality there. The other direction of the theorem comes from Fourier–Motzkin elimination, an algorithm for projecting a system of inequalities that works the way Gaussian elimination does for equations.

Throughout, the field is \( \nR \) and the space is \( \nR^n \) with \( n \ge 1 \) and the dot product. An inequality between vectors is meant **entrywise**: \( \A\x \le \b \) says that \( (\A\x)_i \le b_i \) for every \( i \). For \( \A \in M_{m \times n}(\nR) \) we write \( \a_1\tp, \dots, \a_m\tp \) for its rows, so that \( \A\x \le \b \) is the list of \( m \) inequalities \( \a_i\tp\x \le b_i \).

## Two finite descriptions

The first description already appeared in Section 8, just after @prp-extreme-points-of-hull.

*A polytope is the convex hull of finitely many points; a polyhedron is the solution set of finitely many linear inequalities.*

::: {#def-polytope}
[Polytope]

A **polytope** in \( \nR^n \) is a set of the form \( \conv\{\v_1, \dots, \v_k\} \) for **finitely many** points \( \v_1, \dots, \v_k \in \nR^n \), \( k \ge 0 \).
:::

::: {#def-polyhedron}
[Polyhedron]

A **polyhedron** in \( \nR^n \) is a set of the form
\[
P = \{\x \in \nR^n : \A\x \le \b\}
\]
for some \( m \ge 0 \), \( \A \in M_{m \times n}(\nR) \) and \( \b \in \nR^m \); that is, the intersection of **finitely many** sets \( \{\x : \a_i\tp\x \le b_i\} \). An extreme point of a polyhedron or of a polytope (@def-extreme-point) is called a **vertex**.
:::

In words: a polytope is built from the inside, by mixing finitely many given points; a polyhedron is carved from the outside, by finitely many cuts. When \( \a_i \ne \0 \), the set \( \{\x : \a_i\tp\x \le b_i\} \) is a closed half-space, bounded by the hyperplane \( \a_i\tp\x = b_i \) (@def-hyperplane). A zero row \( \a_i = \0 \) is allowed and harmless: the condition \( 0 \le b_i \) either holds for every \( \x \) or for none. An **equation** \( \a\tp\x = \beta \) is allowed too, as the two inequalities \( \a\tp\x \le \beta \) and \( -\a\tp\x \le -\beta \). By @thm-convex-hull-combinations, the polytope \( \conv\{\v_1, \dots, \v_k\} \) is the set of all \( \sum_j t_j\v_j \) with every \( t_j \ge 0 \) and \( \sum_j t_j = 1 \).

Some examples, simplest first.

1. **The empty set and a point** are both. \( \emptyset = \conv\emptyset \), and \( \emptyset = \{\x : 0 \le -1\} \) with the single zero row. A point \( \v = \conv\{\v\} \) is the solution set of the \( 2n \) inequalities \( x_i \le v_i \) and \( -x_i \le -v_i \).
2. **All of \( \nR^n \)** is a polyhedron, with \( m = 0 \) (or with the one row \( 0 \le 0 \)). So is a closed half-space. Neither is a polytope, because a polytope is bounded: if \( \norm{\v_j} \le R \) for every \( j \), then \( \norm{\sum_j t_j\v_j} \le \sum_j t_j\norm{\v_j} \le R \).
3. **The triangle** \( T \subseteq \nR^2 \) with corners \( (0,0), (3,0), (0,3) \) is \( \conv\{(0,0), (3,0), (0,3)\} \), and it is the polyhedron \( \{x_1 \ge 0,\ x_2 \ge 0,\ x_1 + x_2 \le 3\} \). That the two descriptions agree is not a definition but a fact; the worked example in the section on Fourier–Motzkin elimination below derives each from the other.
4. **The cube** \( B_\infty = [-1, 1]^n \) is the polyhedron given by the \( 2n \) inequalities \( \pm x_i \le 1 \), and by Section 8 it is the hull of its \( 2^n \) sign vectors (@exm-extreme-points-unit-balls and @thm-minkowski-extreme). So it is both.

**A non-example by minimal change.** Replace the cube's square \( B_\infty \subseteq \nR^2 \) by the disk \( B_2 \). It is still compact and convex, still the unit ball of a norm, and still the solution set of inequalities \( \a\tp\x \le 1 \), one for **every** unit vector \( \a \): by @thm-cauchy-schwarz, \( \a\tp\x \le \norm{\x} \le 1 \) on the disk, and a point with \( \norm{\x} > 1 \) violates the inequality for \( \a = \x/\norm{\x} \). What fails is the word **finitely**. The disk is not a polytope: by @prp-extreme-points-of-hull a polytope has finitely many extreme points, while the disk has a whole circle of them (@exm-extreme-points-unit-balls). We will see after the Minkowski–Weyl theorem that it is not a polyhedron either.

**Why these definitions.** Both allow only finite data, and that is the point: finitely many inequalities can be checked, finitely many points can be listed, and the whole theory of this section is about moving between two finite lists. An infinite family of inequalities describes every closed convex set, by the separation theorem (@thm-separation-point), so dropping "finitely many" would make the second definition say nothing new.

Section 1 already showed that every polyhedron is convex and closed; we record it for citation.

::: {#prp-polyhedron-closed-convex}
[Polyhedra Are Closed and Convex]

Every polyhedron \( P = \{\x : \A\x \le \b\} \) is convex and closed.
:::

::: {.proof}
With the linear functional \( \varphi_i(\x) = \a_i\tp\x \), each set \( \{\x : \a_i\tp\x \le b_i\} = \{\varphi_i \le b_i\} \) is closed by @prp-closed-open-basics (c), and convex by @prp-convexity-operations (b), as the preimage of the interval \( (-\infty, b_i] \) under \( \varphi_i \). So their intersection \( P \) is closed by @prp-closed-open-basics (b) and convex by @prp-convexity-operations (a).
:::

::: {.warning}
**A polyhedron need not have any vertices, even when it is not empty.** The strip \( \{\x \in \nR^2 : -1 \le x_1 + x_2 \le 1\} \) is a closed convex set with no extreme points at all: every point \( \x \) of it is the midpoint of \( \x \pm (1, -1) \), which lie in it. Minkowski's theorem (@thm-minkowski-extreme) does not apply because the strip is unbounded, and in the language of the next theorem, its constraint rows \( \pm(1, 1) \) have rank \( 1 < 2 \).
:::

## Vertices are basic feasible points

Section 8 showed that a linear function on a non-empty compact convex set attains its maximum at an extreme point (@cor-linear-max-at-extreme). For a linear program over a bounded region \( \{\x : \A\x \le \b\} \), that shrinks the search to the vertices. To make it a finite search we need a way to recognize a vertex from the data \( \A, \b \), and a proof that there are finitely many.

Stand at a point \( \x \) of \( P \) and look at the inequalities that are tight there. Each tight inequality \( \a_i\tp\x = b_i \) confines \( \x \) to a hyperplane. If the tight rows are rich enough to pin \( \x \) down, there is no room to move in any direction, and \( \x \) should be a corner. If not, there should be a direction along which one can move both ways without leaving \( P \).

::: {#def-basic-feasible-point}
[Active Set, Basic Feasible Point]

Let \( P = \{\x \in \nR^n : \A\x \le \b\} \) and \( \x \in P \). The **active set** of \( \x \) is \( I(\x) = \{i : \a_i\tp\x = b_i\} \), the indices of the inequalities that hold with equality at \( \x \). The point \( \x \) is a **basic feasible point** of the system if among the active rows \( \{\a_i : i \in I(\x)\} \) there are \( n \) **linearly independent** ones.
:::

Equivalently, the matrix \( \A_{I(\x)} \) formed by the active rows has a row space of dimension \( n \), that is, rank \( n \) (@thm-row-rank-equals-column-rank); by @thm-rank-nullity-matrix this says that its null space is \( \{\0\} \), which means that \( \x \) is the **only** solution of the equations \( \a_i\tp\y = b_i \), \( i \in I(\x) \). The word "feasible" records that \( \x \) lies in \( P \); a solution of \( n \) independent equations \( \a_i\tp\y = b_i \) that violates some other inequality is a **basic point** but not a basic feasible one. Note that the definition depends on the system \( \A\x \le \b \), not only on the set \( P \); the theorem shows that the resulting notion depends only on \( P \).

::: {#thm-vertices-basic-feasible}
[Vertices Are Basic Feasible Points]

Let \( P = \{\x \in \nR^n : \A\x \le \b\} \) and \( \x \in P \). Then \( \x \) is a vertex of \( P \) if and only if \( \x \) is a basic feasible point.
:::

::: {.idea}
Both directions are about the directions \( \u \) with \( \a_i\tp\u = 0 \) for every active \( i \), the directions along which every tight constraint stays tight. If the active rows have rank \( n \), the only such direction is \( \0 \), and an averaging argument pins down any segment through \( \x \). If their rank is less than \( n \), a non-zero such \( \u \) exists by rank–nullity, and a short step \( \pm\varepsilon\u \) keeps the tight constraints tight and, because there are finitely many, keeps the slack ones slack.
:::

::: {.proof}
Write \( I = I(\x) \) and let \( \A_I \) be the matrix of active rows (empty if \( I = \emptyset \)).

\( (\Leftarrow) \) Suppose \( \A_I \) has rank \( n \), and let \( \x = \frac12(\y + \z) \) with \( \y, \z \in P \). For \( i \in I \),
\[
b_i = \a_i\tp\x = \tfrac12\a_i\tp\y + \tfrac12\a_i\tp\z ,
\]
with \( \a_i\tp\y \le b_i \) and \( \a_i\tp\z \le b_i \); if either were strict, the average would be less than \( b_i \). So \( \a_i\tp\y = b_i = \a_i\tp\x \), that is, \( \A_I(\y - \x) = \0 \). Since \( \A_I \) has \( n \) columns and rank \( n \), its null space is \( \{\0\} \) by @thm-rank-nullity-matrix, so \( \y = \x \), and then \( \z = 2\x - \y = \x \). By @lem-extreme-midpoint, \( \x \) is a vertex.

\( (\Rightarrow) \) Suppose \( \A_I \) has rank less than \( n \) (this includes \( I = \emptyset \)). By @thm-rank-nullity-matrix its null space is non-zero; choose \( \u \ne \0 \) with \( \a_i\tp\u = 0 \) for every \( i \in I \). For \( i \notin I \), the slack \( b_i - \a_i\tp\x \) is positive. Let \( \varepsilon > 0 \) be smaller than \( (b_i - \a_i\tp\x)/\lvert\a_i\tp\u\rvert \) for every \( i \notin I \) with \( \a_i\tp\u \ne 0 \); there are finitely many such \( i \), so such an \( \varepsilon \) exists, and if there are none, take \( \varepsilon = 1 \). Then for \( i \in I \), \( \a_i\tp(\x \pm \varepsilon\u) = b_i \), and for \( i \notin I \),
\[
\a_i\tp(\x \pm \varepsilon\u) \le \a_i\tp\x + \varepsilon\lvert\a_i\tp\u\rvert \le b_i .
\]
So \( \x \pm \varepsilon\u \in P \), they differ because \( \u \ne \0 \), and \( \x \) is their midpoint. Hence \( \x \) is not a vertex. This proves the theorem.
:::

The payoff is finiteness.

::: {#cor-finitely-many-vertices}
[A Polyhedron Has Finitely Many Vertices]

Let \( P = \{\x \in \nR^n : \A\x \le \b\} \) with \( \A \in M_{m \times n}(\nR) \). Every vertex of \( P \) is the unique solution of \( \A_J\x = \b_J \) for some set \( J \) of \( n \) row indices with \( \A_J \) invertible. In particular \( P \) has at most \( \binom{m}{n} \) vertices.
:::

::: {.idea}
By the theorem, \( n \) independent active rows pin a vertex down, so a vertex is determined by which \( n \) rows those are.
:::

::: {.proof}
Let \( \x \) be a vertex. By @thm-vertices-basic-feasible, some \( n \) active rows, with index set \( J \subseteq I(\x) \), are linearly independent. The \( n \times n \) matrix \( \A_J \) then has independent rows, so its rank is \( n \) (@thm-row-rank-equals-column-rank), its null space is \( \{\0\} \) (@thm-rank-nullity-matrix), and it is invertible (@thm-invertible-tfae (b)). As \( J \subseteq I(\x) \), \( \A_J\x = \b_J \), so \( \x = \A_J^{-1}\b_J \) is determined by \( J \). Different vertices therefore come from different sets \( J \), and there are \( \binom{m}{n} \) sets of \( n \) indices.
:::

This gives the finite recipe for a vertex list: for each choice of \( n \) rows with \( \A_J \) invertible, solve \( \A_J\x = \b_J \) and keep the solution if it satisfies the remaining inequalities.

::: {#exm-vertices-quadrilateral}
[The vertices of a quadrilateral]

Find the vertices of
\[
P = \{\x \in \nR^2 : x_1 \ge 0,\ x_2 \ge 0,\ x_1 + 2x_2 \le 4,\ 3x_1 + x_2 \le 6\} ,
\]
and the maximum of \( \varphi(\x) = x_1 + x_2 \) over \( P \).
:::

::: {.solution}
Number the constraints (1) \( -x_1 \le 0 \), (2) \( -x_2 \le 0 \), (3) \( x_1 + 2x_2 \le 4 \), (4) \( 3x_1 + x_2 \le 6 \). Any two of the four rows are linearly independent, so each of the \( \binom42 = 6 \) pairs gives one basic point. We solve each pair as equations and test the other two inequalities.
\[
\begin{array}{c|c|l}
\text{pair} & \text{basic point} & \text{other constraints} \\ \hline
(1),(2) & (0, 0) & 0 \le 4,\ 0 \le 6: \text{ feasible} \\
(1),(3) & (0, 2) & -2 \le 0,\ 2 \le 6: \text{ feasible} \\
(1),(4) & (0, 6) & 12 \le 4 \text{ fails} \\
(2),(3) & (4, 0) & 12 \le 6 \text{ fails} \\
(2),(4) & (2, 0) & -2 \le 0,\ 2 \le 4: \text{ feasible} \\
(3),(4) & (\tfrac85, \tfrac65) & -\tfrac85 \le 0,\ -\tfrac65 \le 0: \text{ feasible}
\end{array}
\]
For the last pair, subtracting (3) from twice (4) gives \( 5x_1 = 8 \), so \( x_1 = \frac85 \) and \( x_2 = 6 - 3x_1 = \frac65 \); check \( \frac85 + \frac{12}5 = 4 \). By @thm-vertices-basic-feasible the vertices are the four feasible basic points \( (0,0) \), \( (0,2) \), \( (2,0) \) and \( (\frac85, \frac65) \), and \( P \) is a quadrilateral. The two infeasible basic points are where two of the lines cross outside \( P \).

\( P \) is bounded, since \( 0 \le x_1 \le 2 \) and \( 0 \le x_2 \le 2 \) on it, so it is compact (@prp-polyhedron-closed-convex, @cor-closed-bounded-compact) and non-empty. By @cor-linear-max-at-extreme the maximum of \( \varphi \) is attained at a vertex. The values are \( 0, 2, 2, \frac{14}5 \), so the maximum is \( \frac{14}{5} \), at \( (\frac85, \frac65) \).
:::

::: {.check}
A polyhedron in \( \nR^2 \) is given by \( m = 5 \) inequalities. What is the largest number of vertices the corollary allows? Could a polyhedron in \( \nR^3 \) given by \( m = 2 \) inequalities have a vertex?
:::

::: {.solution}
At most \( \binom52 = 10 \). In \( \nR^3 \) a vertex needs \( 3 \) linearly independent active rows, and there are only \( 2 \) rows in all, so no: the rank of the active rows is at most \( 2 < 3 \), and by @thm-vertices-basic-feasible such a polyhedron has no vertices. Geometrically, the intersection of two half-spaces in \( \nR^3 \) always contains a whole line through each of its points.
:::

The recipe is honest but slow: \( \binom{m}{n} \) grows very fast. The **simplex method**, the classical algorithm for linear programs, uses the same theorem more cleverly. It moves from a vertex to a neighboring vertex, one sharing \( n - 1 \) of its independent active constraints, along an edge on which the objective improves, and stops at a vertex where no edge improves it.

## Fourier–Motzkin elimination

Now the other direction. Given a polytope \( \conv\{\v_1, \dots, \v_k\} \), how do we find inequalities for it? The hull is the set of \( \x \) for which **there exist** weights \( \t \ge \0 \) with \( \sum_j t_j = 1 \) and \( \x = \sum_j t_j\v_j \). The conditions on the pair \( (\x, \t) \) are linear inequalities, so the set of pairs is a polyhedron in \( \nR^{n+k} \), and the polytope is its image under the projection that forgets \( \t \). So we need to know that a projection of a polyhedron is a polyhedron, and a way to compute it. For equations, eliminating a variable is Gaussian elimination. For inequalities the device is to pair every upper bound on the variable with every lower bound.

Write a point of \( \nR^{n+1} \) as \( (\x, s) \) with \( \x \in \nR^n \) and \( s \in \nR \), and let \( \pi(\x, s) = \x \).

::: {#lem-fourier-motzkin}
[Fourier–Motzkin Elimination]

Let \( P = \{(\x, s) \in \nR^{n} \times \nR : \a_i\tp\x + c_is \le b_i \text{ for } i = 1, \dots, m\} \). Split the indices by the sign of the coefficient of \( s \): \( I_+ = \{i : c_i > 0\} \), \( I_- = \{i : c_i < 0\} \), \( I_0 = \{i : c_i = 0\} \). Then \( \pi(P) \) is the set of \( \x \in \nR^n \) satisfying
\[
\begin{aligned}
\a_i\tp\x &\le b_i && \text{for } i \in I_0 , \\
(c_i\a_j - c_j\a_i)\tp\x &\le c_ib_j - c_jb_i && \text{for } i \in I_+,\ j \in I_- .
\end{aligned}
\]
In particular \( \pi(P) \) is a polyhedron, and if every \( b_i = 0 \), every right-hand side above is \( 0 \).
:::

::: {.idea}
For fixed \( \x \), each row with \( c_i > 0 \) is an upper bound on \( s \), each row with \( c_i < 0 \) is a lower bound, and a row with \( c_i = 0 \) does not mention \( s \). A number \( s \) satisfying all of them exists exactly when every lower bound is at most every upper bound, and those comparisons are the new rows. Each new row is the combination \( c_i \cdot(\text{row } j) + (-c_j)\cdot(\text{row } i) \), with both multipliers positive and chosen to cancel \( s \).
:::

::: {.proof}
Let \( Q \) be the set described by the new rows. For \( i \in I_+ \) and \( j \in I_- \), put
\[
U_i(\x) = \frac{b_i - \a_i\tp\x}{c_i} , \qquad L_j(\x) = \frac{b_j - \a_j\tp\x}{c_j} .
\]
Dividing row \( i \) by \( c_i > 0 \) shows that it says \( s \le U_i(\x) \), and dividing row \( j \) by \( c_j < 0 \), which reverses the inequality, shows that it says \( s \ge L_j(\x) \). Multiplying \( L_j(\x) \le U_i(\x) \) by the positive number \( -c_ic_j \) and rearranging gives exactly the new row for the pair \( (i, j) \):
\[
L_j(\x) \le U_i(\x) \iff (c_i\a_j - c_j\a_i)\tp\x \le c_ib_j - c_jb_i .
\]

\( (\subseteq) \) If \( (\x, s) \in P \), then \( L_j(\x) \le s \le U_i(\x) \) for every pair, and the rows in \( I_0 \) hold since they do not involve \( s \). So \( \x \in Q \).

\( (\supseteq) \) Let \( \x \in Q \). If \( I_- \ne \emptyset \), let \( s = \max_{j \in I_-} L_j(\x) \); if \( I_- = \emptyset \) and \( I_+ \ne \emptyset \), let \( s = \min_{i \in I_+} U_i(\x) \); if both are empty, let \( s = 0 \). In each case \( L_j(\x) \le s \le U_i(\x) \) for all \( j \in I_- \) and \( i \in I_+ \): in the first case because every \( L_j(\x) \le s \) by the choice of \( s \), and \( s = L_{j_0}(\x) \le U_i(\x) \) for every \( i \) since \( \x \in Q \); the second case is the same with the roles exchanged. The rows in \( I_0 \) hold because \( \x \in Q \). So \( (\x, s) \in P \) and \( \x \in \pi(P) \).

The last sentence is visible: the new right-hand sides are \( b_i \) and \( c_ib_j - c_jb_i \).
:::

As an algorithm:

::: {.algorithm}
**Fourier–Motzkin elimination of one variable.** Input: a system of \( m \) inequalities \( \a_i\tp\x + c_is \le b_i \) in the unknowns \( \x \in \nR^n \) and \( s \in \nR \).

1. Sort the rows into \( I_+ \) (\( c_i > 0 \)), \( I_- \) (\( c_i < 0 \)) and \( I_0 \) (\( c_i = 0 \)).
2. Copy every row of \( I_0 \), without its \( s \) term.
3. For every pair \( i \in I_+ \), \( j \in I_- \), write down the row \( c_i\cdot(\text{row } j) + (-c_j)\cdot(\text{row } i) \), which is \( (c_i\a_j - c_j\a_i)\tp\x \le c_ib_j - c_jb_i \).
4. (Optional.) Delete every new row of the form \( 0 \le \beta \) with \( \beta \ge 0 \), which every \( \x \) satisfies. A row \( 0 \le \beta \) with \( \beta < 0 \) means the projection is empty.

Output: \( \lvert I_0\rvert + \lvert I_+\rvert\,\lvert I_-\rvert \) inequalities in \( \x \) alone, at most, whose solution set is the projection of the input's solution set. To eliminate several variables, repeat.
:::

When the variable to be eliminated appears in an **equation** with a non-zero coefficient, there is a shortcut: solve the equation for it and substitute into the other rows. The projection is unchanged, since the equation determines the eliminated variable from the others, and substitution is exactly Gaussian elimination.

::: {#exm-fourier-motzkin-triangle}
[A triangle, both ways]

Let \( Q = \conv\{(0,0), (3,0), (0,3), (1,1)\} \subseteq \nR^2 \). Find a system of inequalities describing \( Q \), and then recover the vertices of \( Q \) from it.
:::

::: {.solution}
*From points to inequalities.* By @thm-convex-hull-combinations, \( \x \in Q \) if and only if there are \( t_1, \dots, t_4 \ge 0 \) with \( \sum_j t_j = 1 \) and
\[
\x = t_1(0,0) + t_2(3,0) + t_3(0,3) + t_4(1,1) ,
\]
that is,
\[
x_1 = 3t_2 + t_4 , \qquad x_2 = 3t_3 + t_4 .
\]
Three equations involve the weights, so we substitute three of them away and keep \( s = t_4 \): \( t_2 = \frac13(x_1 - s) \), \( t_3 = \frac13(x_2 - s) \), and
\[
t_1 = 1 - t_2 - t_3 - s = 1 - \tfrac13(x_1 + x_2 + s) .
\]
The four conditions \( t_j \ge 0 \), each multiplied by \( 3 \) where needed, become a system in \( (x_1, x_2, s) \):
\[
\begin{aligned}
&(1)\ \ x_1 + x_2 + s \le 3 , \qquad && (2)\ \ -x_1 + s \le 0 , \\
&(3)\ \ -x_2 + s \le 0 , && (4)\ \ -s \le 0 .
\end{aligned}
\]
Run the algorithm on \( s \). The coefficients of \( s \) are \( 1, 1, 1, -1 \), so \( I_+ = \{1, 2, 3\} \), \( I_- = \{4\} \) and \( I_0 = \emptyset \). Each pair \( (i, 4) \) has \( c_i = 1 \) and \( -c_4 = 1 \), so the new row is row \( i \) plus row \( 4 \), which just deletes the \( s \):
\[
x_1 + x_2 \le 3 , \qquad -x_1 \le 0 , \qquad -x_2 \le 0 .
\]
By @lem-fourier-motzkin, \( Q = \{x_1 \ge 0,\ x_2 \ge 0,\ x_1 + x_2 \le 3\} \), the triangle \( T \) of the examples above. The generator \( (1,1) \) left no trace, as it should: it lies inside the triangle.

*From inequalities to vertices.* The three rows \( (-1, 0) \), \( (0, -1) \), \( (1, 1) \) are pairwise independent, so each of the \( \binom32 = 3 \) pairs gives a basic point: \( (0,0) \), \( (0, 3) \) and \( (3, 0) \). Each satisfies the third inequality, so all three are vertices by @thm-vertices-basic-feasible. At \( (1, 1) \) no constraint is active, so \( I = \emptyset \) and it is not a vertex, which matches @prp-extreme-points-of-hull: the extreme points of the hull are among the four generators, and \( (1,1) \) is not one of them.
:::

::: {.warning}
**Fourier–Motzkin does not return a minimal description.** Eliminating \( s \) from \( -x_1 + s \le 0 \), \( s \le 1 \), \( -s \le 0 \) and \( x_1 - s \le 1 \) pairs two upper bounds with two lower bounds, and gives \( -x_1 \le 0 \), \( x_1 \le 2 \), and twice the useless row \( 0 \le 1 \). Even without trivial rows, the output can contain inequalities implied by the others. A single step can turn \( m \) rows into as many as \( (m/2)^2 \), and eliminating many variables compounds this, so the method is a proof device and a hand tool for small systems, not an efficient algorithm.
:::

## The Minkowski–Weyl theorem

Cones get the same treatment. Section 5 wrote \( \operatorname{cone}(\v_1, \dots, \v_k) \) for the set of all non-negative combinations \( \sum_j c_j\v_j \), \( c_j \ge 0 \), a convex cone (@def-convex-cone), and called such cones **finitely generated**; we allow \( k = 0 \), with \( \operatorname{cone}() = \{\0\} \). The inequality side is a homogeneous system.

::: {#def-polyhedral-cone}
[Polyhedral Cone]

A **polyhedral cone** in \( \nR^n \) is a set of the form \( C = \{\x \in \nR^n : \A\x \le \0\} \) for some \( m \ge 0 \) and \( \A \in M_{m \times n}(\nR) \).
:::

A polyhedral cone is a polyhedron, and it is a convex cone: it contains \( \0 \), and if \( \A\u \le \0 \), \( \A\v \le \0 \) and \( a, b \ge 0 \), then \( \A(a\u + b\v) = a\A\u + b\A\v \le \0 \). By @prp-polyhedron-closed-convex it is closed, while for finitely generated cones closedness took the work of @thm-finitely-generated-cone-closed.

::: {#thm-minkowski-weyl}
[Minkowski–Weyl Theorem]

::: {.enumerate options="label=(\alph*)"}
1. A subset of \( \nR^n \) is a polytope if and only if it is a bounded polyhedron.
2. A subset of \( \nR^n \) is a finitely generated cone if and only if it is a polyhedral cone.
:::
:::

::: {.idea}
Four implications, two tools.

① *Bounded polyhedron \( \Rightarrow \) polytope.* This is Section 8 plus the vertex theorem: a bounded polyhedron is compact, so it is the hull of its vertices by Minkowski's theorem, and it has finitely many vertices.

② *Polyhedral cone \( \Rightarrow \) finitely generated.* Cut the cone with the cube \( [-1, 1]^n \). The result is a bounded polyhedron, hence by ① the hull of finitely many points, and scaling those points generates the cone.

③ *Polytope \( \Rightarrow \) polyhedron*, and ④ *finitely generated \( \Rightarrow \) polyhedral.* Write the set as the projection of a polyhedron in a bigger space, with the weights as extra coordinates, and eliminate the weights one at a time by Fourier–Motzkin. For a cone all right-hand sides are \( 0 \) and stay \( 0 \).
:::

::: {.proof}
**① A bounded polyhedron is a polytope.** Let \( P = \{\x : \A\x \le \b\} \) be bounded. If \( P = \emptyset \), then \( P = \conv\emptyset \). Otherwise \( P \) is closed and convex by @prp-polyhedron-closed-convex, and bounded, so it is compact by @cor-closed-bounded-compact. By @thm-minkowski-extreme, \( P = \conv(\operatorname{ext} P) \), and \( \operatorname{ext} P \) is finite by @cor-finitely-many-vertices. So \( P \) is a polytope.

**② A polyhedral cone is finitely generated.** Let \( C = \{\x : \A\x \le \0\} \), and let \( P = C \cap [-1, 1]^n \), the polyhedron given by the rows of \( \A \) together with the \( 2n \) rows \( \pm x_i \le 1 \). It is bounded and contains \( \0 \), so by ① \( P = \conv\{\v_1, \dots, \v_k\} \), where \( \v_1, \dots, \v_k \) are its vertices; in particular every \( \v_j \in P \subseteq C \). We claim \( C = \operatorname{cone}(\v_1, \dots, \v_k) \). If \( \c \ge \0 \), then \( \A\sum_j c_j\v_j = \sum_j c_j\A\v_j \le \0 \), since each \( \A\v_j \le \0 \) and each \( c_j \ge 0 \); so every such combination lies in \( C \). Conversely let \( \x \in C \). If \( \x = \0 \), take all \( c_j = 0 \). Otherwise put \( r = \norm{\x}_\infty > 0 \). Then \( \A(\x/r) = \frac1r\A\x \le \0 \) and every entry of \( \x/r \) lies in \( [-1, 1] \), so \( \x/r \in P \), say \( \x/r = \sum_j t_j\v_j \) with \( t_j \ge 0 \). Then \( \x = \sum_j (rt_j)\v_j \) with \( rt_j \ge 0 \).

**③ A polytope is a bounded polyhedron.** Let \( Q = \conv\{\v_1, \dots, \v_k\} \), and let \( \V \) have columns \( \v_j \). It is bounded, as in example 2 after @def-polyhedron. By @thm-convex-hull-combinations, \( Q \) is the image, under the map \( (\x, \t) \mapsto \x \) that forgets the last \( k \) coordinates, of
\[
\begin{aligned}
\widehat{P} = \bigl\{(\x, \t) \in \nR^{n} \times \nR^{k} :\ & \x - \V\t \le \0,\ \ -\x + \V\t \le \0, \\
& -\t \le \0,\ \ \1\tp\t \le 1,\ \ -\1\tp\t \le -1\bigr\} ,
\end{aligned}
\]
a polyhedron in \( \nR^{n+k} \). Forgetting the last \( k \) coordinates is forgetting one coordinate \( k \) times in a row, and by @lem-fourier-motzkin each step takes a polyhedron to a polyhedron. So \( Q \) is a polyhedron.

**④ A finitely generated cone is polyhedral.** Let \( C = \operatorname{cone}(\v_1, \dots, \v_k) = \{\V\c : \c \ge \0\} \), where \( \V \) has columns \( \v_j \). It is the image under the same map of \( \{(\x, \c) : \x - \V\c \le \0,\ -\x + \V\c \le \0,\ -\c \le \0\} \), whose right-hand sides are all \( 0 \). By the last sentence of @lem-fourier-motzkin, eliminating the \( k \) coordinates of \( \c \) one at a time keeps every right-hand side \( 0 \), and the rows copied from \( I_0 \) keep theirs as well. So \( C = \{\x : \B\x \le \0\} \) for the matrix \( \B \) of the final rows (if no rows remain, \( C = \nR^n = \{\x : 0 \le 0\} \)). This completes the proof.
:::

Two consequences show what the theorem is for. First, **the intersection of two polytopes is a polytope**. By (a) each is a bounded polyhedron; putting the two systems of inequalities together describes the intersection, which is therefore a bounded polyhedron, hence a polytope by (a) again. From the point description alone this is not obvious at all: the corners of the intersection are, in general, new points found nowhere in the two lists. Second, (b) gives a new proof of @thm-finitely-generated-cone-closed, since every polyhedral cone is closed. In that proof the difficulty of Section 5 has moved into Fourier–Motzkin elimination. The same elimination shows that a linear image \( \M(C) \) of a polyhedral cone \( C = \{\x : \A\x \le \0\} \) is polyhedral: it is the image, under the map forgetting \( \x \), of \( \{(\y, \x) : \y - \M\x \le \0,\ -\y + \M\x \le \0,\ \A\x \le \0\} \), and the argument of ④ applies. So a linear image of a polyhedral cone is closed, and a closed convex cone with a non-closed linear image, like the one in Section 5, can never be polyhedral.

The disk \( B_2 \) is not a polyhedron. If it were, it would be a bounded polyhedron, hence a polytope by (a), and it is not one.

## The cube and the cross-polytope

The two unit balls with corners from Section 8 are the standard example of the theorem, and they illustrate a duality between the two descriptions.

::: {#exm-cube-cross-polytope}
[The cube and the cross-polytope]

For \( n \ge 1 \), describe \( B_\infty \) and \( B_1 \) both as polytopes and as polyhedra, and find their vertices from the inequalities by @thm-vertices-basic-feasible.
:::

::: {.solution}
*The cube.* \( B_\infty \) is the polyhedron given by the \( 2n \) rows \( \e_i\tp\x \le 1 \) and \( -\e_i\tp\x \le 1 \). At a point \( \x \) of it, the active rows are \( \e_i \) for each \( i \) with \( x_i = 1 \) and \( -\e_i \) for each \( i \) with \( x_i = -1 \); they are distinct standard vectors up to sign, so they are linearly independent, and their number is the rank. The rank is \( n \) exactly when every \( \lvert x_i \rvert = 1 \). So the vertices are the \( 2^n \) sign vectors, as @exm-extreme-points-unit-balls found directly, and \( B_\infty \) is their hull.

*The cross-polytope.* By @exm-extreme-points-unit-balls and @thm-minkowski-extreme, \( B_1 = \conv\{\pm\e_1, \dots, \pm\e_n\} \). For its inequalities, let \( \s \) run over the \( 2^n \) sign vectors. For every \( \s \), \( \s\tp\x = \sum_i s_ix_i \le \sum_i\lvert x_i\rvert = \norm{\x}_1 \), with equality when \( s_i = 1 \) for \( x_i \ge 0 \) and \( s_i = -1 \) for \( x_i < 0 \). So \( \norm{\x}_1 = \max_{\s}\s\tp\x \), and
\[
B_1 = \{\x \in \nR^n : \s\tp\x \le 1 \text{ for every sign vector } \s\} ,
\]
a polyhedron with \( 2^n \) rows. At \( \e_1 \), the active rows are the \( \s \) with \( s_1 = 1 \). They have rank \( n \): they include \( \1 \), and for each \( j \ge 2 \) the vector \( \1 - 2\e_j \), so their span contains \( \frac12(\1 - (\1 - 2\e_j)) = \e_j \) for \( j \ge 2 \) and then \( \e_1 = \1 - \sum_{j \ge 2}\e_j \). The same holds at every \( \pm\e_i \). Every other point \( \x \) of \( B_1 \) has active rows of rank less than \( n \). If \( \norm{\x}_1 < 1 \), no row is active. If \( \norm{\x}_1 = 1 \), then \( \x \) has two non-zero entries \( x_i, x_j \) with \( i \ne j \), since a point with one non-zero entry and \( \norm{\x}_1 = 1 \) is some \( \pm\e_i \); let \( \sigma_i, \sigma_j \in \{\pm 1\} \) be their signs. An active \( \s \) has \( \sum_k s_kx_k = \sum_k \lvert x_k\rvert \) with each \( s_kx_k \le \lvert x_k\rvert \), so \( s_kx_k = \lvert x_k\rvert \) for every \( k \), and in particular \( s_i = \sigma_i \), \( s_j = \sigma_j \). Hence \( \u = \sigma_i\e_i - \sigma_j\e_j \ne \0 \) has \( \s\tp\u = \sigma_i^2 - \sigma_j^2 = 0 \) for every active \( \s \), and the matrix of active rows has rank less than \( n \) by @thm-rank-nullity-matrix. By @thm-vertices-basic-feasible, the vertices are exactly the \( 2n \) points \( \pm\e_i \).

*Duality.* The rows of the cube are \( \pm\e_i \), which are the vertices of the cross-polytope; the rows of the cross-polytope are the sign vectors, which are the vertices of the cube. In \( \nR^3 \), the cube has \( 8 \) vertices and \( 6 \) inequalities, the octahedron \( 6 \) vertices and \( 8 \) inequalities. This exchange is the polytope form of the fact that \( \norm{\cdot}_1 \) and \( \norm{\cdot}_\infty \) are dual norms (@def-dual-norm): the maximum of \( \y\tp\x \) over \( \x \in B_1 \) is \( \norm{\y}_\infty \), and over \( \x \in B_\infty \) it is \( \norm{\y}_1 \).
:::

## Exercises

### A. Check your understanding

:::: {#exr-polytopes-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the definitions of a polytope and of a polyhedron in \( \nR^n \).
2. True or false: every polyhedron is a polytope. Justify your answer.
3. True or false: the intersection of two polytopes in \( \nR^n \) is a polytope. Justify your answer.
4. State the criterion of @thm-vertices-basic-feasible for a point of \( \{\x : \A\x \le \b\} \) to be a vertex.
5. True or false: every inequality produced by Fourier–Motzkin elimination (@lem-fourier-motzkin) is needed to describe the projection. Justify your answer.
:::
::::

::: {.solution}
(a) A polytope is the convex hull of finitely many points of \( \nR^n \). A polyhedron is a set \( \{\x \in \nR^n : \A\x \le \b\} \) for some \( \A \in M_{m \times n}(\nR) \) and \( \b \in \nR^m \), that is, an intersection of finitely many sets \( \{\x : \a_i\tp\x \le b_i\} \).

(b) False. The half-plane \( \{x_2 \ge 0\} \subseteq \nR^2 \) is a polyhedron, with one row, but it is unbounded, while every polytope is bounded.

(c) True. By @thm-minkowski-weyl (a), each is a bounded polyhedron. Listing both systems of inequalities together describes the intersection, which is therefore a polyhedron, and it is bounded because it lies inside one of the two. By @thm-minkowski-weyl (a) again, it is a polytope.

(d) A point \( \x \) with \( \A\x \le \b \) is a vertex if and only if the rows \( \a_i \) with \( \a_i\tp\x = b_i \) include \( n \) linearly independent ones.

(e) False. In the warning after @exm-fourier-motzkin-triangle, two of the four output rows are \( 0 \le 1 \), which every point satisfies.
:::

### B. Practice

:::: {#exr-polytopes-b1}
[B1: Vertices of a pentagon]

Find all vertices of
\[
P = \{\x \in \nR^2 : x_1 \ge 0,\ x_2 \ge 0,\ x_1 + x_2 \le 4,\ x_1 - x_2 \le 2,\ -x_1 + 2x_2 \le 5\} ,
\]
and the maximum of \( 2x_1 + 3x_2 \) over \( P \). Hence write \( P \) as a polytope.
::::

::: {.solution}
Number the rows (1) \( -x_1 \le 0 \), (2) \( -x_2 \le 0 \), (3) \( x_1 + x_2 \le 4 \), (4) \( x_1 - x_2 \le 2 \), (5) \( -x_1 + 2x_2 \le 5 \). Any two rows are independent (no two are multiples of each other), so each of the \( \binom52 = 10 \) pairs gives one basic point.
\[
\begin{array}{c|c|l}
\text{pair} & \text{point} & \text{verdict} \\ \hline
(1),(2) & (0, 0) & \text{feasible} \\
(1),(3) & (0, 4) & (5)\colon 8 \le 5 \text{ fails} \\
(1),(4) & (0, -2) & (2) \text{ fails} \\
(1),(5) & (0, \tfrac52) & \text{feasible} \\
(2),(3) & (4, 0) & (4)\colon 4 \le 2 \text{ fails} \\
(2),(4) & (2, 0) & \text{feasible} \\
(2),(5) & (-5, 0) & (1) \text{ fails} \\
(3),(4) & (3, 1) & \text{feasible} \\
(3),(5) & (1, 3) & \text{feasible} \\
(4),(5) & (9, 7) & (3)\colon 16 \le 4 \text{ fails}
\end{array}
\]
For instance, (3) and (4) added give \( 2x_1 = 6 \), so \( \x = (3, 1) \); (3) and (5) added give \( 3x_2 = 9 \), so \( \x = (1, 3) \); (4) and (5) added give \( x_2 = 7 \), then \( x_1 = 9 \). For the feasible points, the checks are routine: at \( (0, \frac52) \), \( 0 + \frac52 \le 4 \) and \( -\frac52 \le 2 \); at \( (2, 0) \), \( 2 \le 4 \) and \( -2 \le 5 \); at \( (3, 1) \), \( -3 + 2 \le 5 \); at \( (1, 3) \), \( 1 - 3 \le 2 \). By @thm-vertices-basic-feasible the vertices are \( (0,0) \), \( (2,0) \), \( (3,1) \), \( (1,3) \), \( (0, \frac52) \).

\( P \) is bounded, since \( 0 \le x_1, x_2 \le 4 \) on it by rows (1) to (3), and non-empty. So by @cor-linear-max-at-extreme the maximum of \( 2x_1 + 3x_2 \) is attained at a vertex. The values are \( 0, 4, 9, 11, \frac{15}{2} \), so the maximum is \( 11 \), at \( (1, 3) \). By the proof of @thm-minkowski-weyl (a), \( P = \conv\{(0,0), (2,0), (3,1), (1,3), (0, \frac52)\} \).
:::

:::: {#exr-polytopes-b2}
[B2: Inequalities for a quadrilateral]

Use Fourier–Motzkin elimination to find a system of inequalities describing the quadrilateral
\[
Q = \conv\{(0,0), (2,0), (2,1), (0,2)\} .
\]
Hence find the vertices of \( Q \).

*Hint: substitute away \( t_1, t_2, t_4 \) and keep \( s = t_3 \), the weight of \( (2,1) \).*
::::

::: {.solution}
\( \x \in Q \) if and only if there are \( t_1, \dots, t_4 \ge 0 \) with \( \sum t_j = 1 \), \( x_1 = 2t_2 + 2t_3 \) and \( x_2 = t_3 + 2t_4 \). With \( s = t_3 \): \( t_2 = \frac12(x_1 - 2s) \), \( t_4 = \frac12(x_2 - s) \), and
\[
t_1 = 1 - t_2 - s - t_4 = 1 - \tfrac12x_1 - \tfrac12x_2 + \tfrac12 s .
\]
The conditions \( 2t_1 \ge 0 \), \( 2t_2 \ge 0 \), \( 2t_4 \ge 0 \), \( t_3 \ge 0 \) read
\[
\begin{aligned}
&(1)\ \ x_1 + x_2 - s \le 2 , \qquad && (2)\ \ -x_1 + 2s \le 0 , \\
&(3)\ \ -x_2 + s \le 0 , && (4)\ \ -s \le 0 .
\end{aligned}
\]
The coefficients of \( s \) are \( -1, 2, 1, -1 \), so \( I_+ = \{2, 3\} \) and \( I_- = \{1, 4\} \). The four pairs give:
\[
\begin{aligned}
(2),(1)&\colon\ 2\cdot(1) + 1\cdot(2) = \ x_1 + 2x_2 \le 4 , \\
(2),(4)&\colon\ 2\cdot(4) + 1\cdot(2) = \ -x_1 \le 0 , \\
(3),(1)&\colon\ 1\cdot(1) + 1\cdot(3) = \ x_1 \le 2 , \\
(3),(4)&\colon\ 1\cdot(4) + 1\cdot(3) = \ -x_2 \le 0 .
\end{aligned}
\]
So \( Q = \{0 \le x_1 \le 2,\ x_2 \ge 0,\ x_1 + 2x_2 \le 4\} \) by @lem-fourier-motzkin. Its rows are \( (-1,0), (1,0), (0,-1), (1,2) \). The pair \( \pm(1,0) \) is dependent; the other five pairs give the basic points \( (0,0) \), \( (0,2) \), \( (2,0) \), \( (2,1) \) and \( (4, 0) \) (from \( x_2 = 0 \), \( x_1 + 2x_2 = 4 \)), and the last violates \( x_1 \le 2 \). So by @thm-vertices-basic-feasible the vertices are the four given points, and none of them was redundant.
:::

:::: {#exr-polytopes-b3}
[B3: Which of these are vertices?]

Let \( P = \{\x \in \nR^3 : \x \ge \0,\ x_1 + x_2 + x_3 \le 3,\ x_1 + x_2 \le 2\} \). Determine which of the following points are vertices of \( P \). Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( (0, 2, 1) \)
2. \( (1, 1, 1) \)
3. \( (0, 0, 3) \)
4. \( (3, 0, 0) \)
5. \( (1, 0, 0) \)
:::
::::

::: {.solution}
We use @thm-vertices-basic-feasible: check that the point lies in \( P \), list its active rows, and compute their rank. The rows are \( -\e_1, -\e_2, -\e_3 \), \( (1,1,1) \) and \( (1,1,0) \).

(a) \( (0,2,1) \in P \): the entries are \( \ge 0 \), \( 0 + 2 + 1 = 3 \le 3 \), \( 0 + 2 \le 2 \). Active: \( -\e_1 \), \( (1,1,1) \), \( (1,1,0) \). Their span contains \( (1,1,1) - (1,1,0) = \e_3 \), \( \e_1 \), and \( (1,1,0) - \e_1 = \e_2 \), so it is \( \nR^3 \). Rank \( 3 \): **a vertex**.

(b) \( (1,1,1) \in P \), with active rows \( (1,1,1) \) and \( (1,1,0) \) only. Rank \( 2 < 3 \): **not a vertex**. Indeed it is the midpoint of \( (0,2,1) \) and \( (2,0,1) \), both in \( P \).

(c) \( (0,0,3) \in P \), with active rows \( -\e_1 \), \( -\e_2 \), \( (1,1,1) \), which are independent (the third has a non-zero third entry, the first two do not). Rank \( 3 \): **a vertex**.

(d) \( (3, 0, 0) \notin P \), since \( 3 + 0 = 3 > 2 \). It is a basic point, the solution of \( x_2 = 0 \), \( x_3 = 0 \), \( x_1 + x_2 + x_3 = 3 \), but not a feasible one: **not a vertex**.

(e) \( (1, 0, 0) \in P \), with active rows \( -\e_2 \) and \( -\e_3 \) only. Rank \( 2 < 3 \): **not a vertex**. It is the midpoint of \( (0,0,0) \) and \( (2,0,0) \).
:::

### C. Going deeper

:::: {#exr-polytopes-c1}
[C1: Unbounded polyhedra]

Let \( P = \{\x \in \nR^n : \A\x \le \b\} \) be a **non-empty** polyhedron, and let \( C = \{(\x, t) \in \nR^n \times \nR : \A\x - t\b \le \0,\ -t \le 0\} \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \x \in P \) if and only if \( (\x, 1) \in C \).
2. By @thm-minkowski-weyl (b), \( C \) is generated by finitely many vectors \( (\w_j, t_j) \), \( j = 1, \dots, k \). Prove that every \( t_j \ge 0 \), and that
\[
P = \conv\{\w_j/t_j : t_j > 0\} + \Bigl\{\sum_{t_j = 0} c_j\w_j : c_j \ge 0\Bigr\} ,
\]
the set of sums of a point of the polytope and a point of the cone. So every non-empty polyhedron is a polytope plus a finitely generated cone.
3. Check the statement for \( P = \{\x \in \nR^2 : x_1 \ge 0,\ 0 \le x_2 \le 1\} \), with the polytope \( \conv\{(0,0), (0,1)\} \) and the cone generated by \( \e_1 \).
:::
::::

::: {.solution}
(a) \( (\x, 1) \in C \) says \( \A\x - \b \le \0 \) and \( -1 \le 0 \), which is \( \x \in P \).

(b) Each generator lies in \( C \), so \( -t_j \le 0 \). Split the indices into \( J_+ = \{j : t_j > 0\} \) and \( J_0 = \{j : t_j = 0\} \).

\( (\subseteq) \) Let \( \x \in P \). By (a), \( (\x, 1) = \sum_j c_j(\w_j, t_j) \) with \( c_j \ge 0 \). The last coordinate gives \( 1 = \sum_{j \in J_+} c_jt_j \), so \( J_+ \ne \emptyset \), and
\[
\x = \sum_{j \in J_+} (c_jt_j)\,\frac{\w_j}{t_j} + \sum_{j \in J_0} c_j\w_j ,
\]
where the weights \( c_jt_j \) are non-negative and add up to \( 1 \). So \( \x \) lies in the right-hand side.

\( (\supseteq) \) Let \( \x = \sum_{j \in J_+} s_j\w_j/t_j + \sum_{j \in J_0} c_j\w_j \) with \( s_j \ge 0 \), \( \sum s_j = 1 \) and \( c_j \ge 0 \). Then
\[
(\x, 1) = \sum_{j \in J_+} \frac{s_j}{t_j}(\w_j, t_j) + \sum_{j \in J_0} c_j(\w_j, 0) ,
\]
a non-negative combination of generators, so \( (\x, 1) \in C \) and \( \x \in P \) by (a).

(c) A point \( (0, u) + c\e_1 \) with \( 0 \le u \le 1 \) and \( c \ge 0 \) is \( (c, u) \), which satisfies \( x_1 \ge 0 \) and \( 0 \le x_2 \le 1 \). Conversely \( (x_1, x_2) \in P \) is \( (0, x_2) + x_1\e_1 \) with \( (0, x_2) \in \conv\{(0,0), (0,1)\} \) and \( x_1 \ge 0 \). So \( P = \conv\{(0,0),(0,1)\} + \{c\e_1 : c \ge 0\} \).
:::

:::: {#exr-polytopes-c2}
[C2: Linear images of polyhedra]

Let \( \M \in M_{p \times n}(\nR) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( P \subseteq \nR^n \) is a polyhedron, then \( \M(P) = \{\M\x : \x \in P\} \) is a polyhedron in \( \nR^p \), and that if \( P \) is a polyhedral cone, so is \( \M(P) \).
2. Prove that if \( Q \) is a polytope, then \( \M(Q) \) is a polytope, directly from @def-polytope.
3. Deduce that a linear image of a polyhedral cone is closed. Why does this not contradict the existence of a closed convex cone with a non-closed linear image?
:::
::::

::: {.solution}
(a) Let \( P = \{\x : \A\x \le \b\} \). Then \( \y \in \M(P) \) if and only if there is \( \x \) with \( (\y, \x) \) in
\[
\widehat{P} = \{(\y, \x) \in \nR^p \times \nR^n : \y - \M\x \le \0,\ -\y + \M\x \le \0,\ \A\x \le \b\} ,
\]
a polyhedron in \( \nR^{p+n} \). So \( \M(P) \) is the image of \( \widehat{P} \) under the map forgetting the last \( n \) coordinates, and \( n \) applications of @lem-fourier-motzkin show that it is a polyhedron. If \( \b = \0 \), every right-hand side in \( \widehat{P} \) is \( 0 \), and stays \( 0 \) under elimination, so \( \M(P) \) is a polyhedral cone.

(b) If \( Q = \conv\{\v_1, \dots, \v_k\} \), then by @thm-convex-hull-combinations and linearity,
\[
\M\Bigl(\sum_j t_j\v_j\Bigr) = \sum_j t_j\M\v_j ,
\]
so \( \M(Q) = \conv\{\M\v_1, \dots, \M\v_k\} \), a polytope.

(c) By (a), the image of a polyhedral cone is a polyhedral cone, which is closed by @prp-polyhedron-closed-convex. So a closed convex cone whose linear image is not closed cannot be polyhedral; by @thm-minkowski-weyl (b), it cannot be finitely generated either. This is consistent with Section 5, where closedness was proved only for finitely generated cones.
:::

:::: {#exr-polytopes-c3}
[C3: Vertices in standard form]

Let \( \A \in M_{m \times n}(\nR) \) have columns \( \c_1, \dots, \c_n \), let \( \b \in \nR^m \), and let \( P = \{\x \in \nR^n : \A\x = \b,\ \x \ge \0\} \), the feasible region of a linear program in standard form.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \x \in P \) is a vertex of \( P \) if and only if the columns \( \c_j \) with \( x_j > 0 \) are linearly independent.
2. Deduce that a vertex of \( P \) has at most \( \rank \A \) positive entries.
3. Find the vertices of \( P = \{\x \in \nR^3 : x_1 + x_2 + x_3 = 1,\ \x \ge \0\} \), the standard triangle.
:::
::::

::: {.solution}
(a) Write \( P \) as a polyhedron with the rows \( \A\x \le \b \), \( -\A\x \le -\b \) and \( -\e_j\tp\x \le 0 \). At \( \x \in P \), every row of \( \pm\A \) is active, and \( -\e_j \) is active exactly when \( x_j = 0 \). Let \( S = \{j : x_j > 0\} \). By @thm-vertices-basic-feasible, \( \x \) is a vertex if and only if the active rows have rank \( n \), that is (@thm-rank-nullity-matrix), if and only if the only \( \u \) with \( \A\u = \0 \) and \( u_j = 0 \) for all \( j \notin S \) is \( \u = \0 \). For such \( \u \), \( \A\u = \sum_{j \in S}u_j\c_j \). So the condition says that \( \sum_{j \in S}u_j\c_j = \0 \) forces every \( u_j = 0 \), which is the linear independence of \( \{\c_j : j \in S\} \).

(b) The columns \( \c_j \) lie in \( \col(\A) \), of dimension \( \rank\A \), and an independent list in it has at most \( \rank\A \) vectors by @thm-size-bounds (a). By (a), a vertex has at most that many positive entries.

(c) Here \( \A = (1\ 1\ 1) \), of rank \( 1 \). By (b) a vertex has at most one positive entry, and since the entries add up to \( 1 \), exactly one, equal to \( 1 \). Conversely \( \e_j \in P \), and its one positive entry corresponds to the column \( (1) \ne \0 \), an independent list. So the vertices are \( \e_1, \e_2, \e_3 \).
:::
