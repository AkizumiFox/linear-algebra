# Linear Programming Duality

Chapter 2 ended its traffic example (@exm-traffic-network) by admitting what linear algebra alone cannot do: "Non-negativity and street capacities turn the problem into one about inequalities, which is the subject of linear programming." This section takes up that subject. A **linear program** asks for the largest value of a linear function on a region cut out by finitely many linear inequalities. The theory is almost entirely one idea. Every such maximum comes with a companion minimum, the **dual** program, and the two optimal values are equal. The proof of that equality is Farkas's lemma of §05, applied to one combined system.

The equality has a practical meaning that goes beyond the theorem. A feasible point proves a lower bound on the maximum, a dual feasible point proves an upper bound, and when the two bounds meet, the answer has been **certified**: anyone can check it by multiplying out, with no need to trust how it was found.

**Throughout, the field is \( \nR \)**, vectors are columns, and \( \x \ge \0 \), \( \u \le \v \) are the entrywise relations of §05.

## Linear programs

Here is a small instance of the kind of question we want to answer. A workshop makes two products. Each unit of the first uses \( 2 \) hours of machine time and \( 1 \) hour of labor, each unit of the second uses \( 1 \) hour of machine time and \( 3 \) hours of labor, and at most \( 3 \) units of the first can be sold. Machine time is limited to \( 7 \) hours, labor to \( 9 \), and the profits are \( 4 \) and \( 3 \) per unit. With \( x_1, x_2 \) units made, the question is:
\[
\begin{aligned}
\text{maximize}\quad & 4x_1 + 3x_2 \\
\text{subject to}\quad & 2x_1 + x_2 \le 7, \quad x_1 + 3x_2 \le 9, \quad x_1 \le 3, \\
& x_1 \ge 0, \quad x_2 \ge 0 .
\end{aligned}
\]
The objective and every constraint are linear, and there are finitely many constraints. In matrix form it reads "maximize \( \c\tp\x \) subject to \( \A\x \le \b \), \( \x \ge \0 \)". That shape deserves a name.

*A linear program is the search for the best value of a linear function over a region defined by finitely many linear inequalities.*

::: {#def-linear-program}
[Linear Program]

Let \( \A \in M_{m \times n}(\nR) \), \( \b \in \nR^m \) and \( \c \in \nR^n \). The **linear program** with these data, in **inequality form**, is the problem
\[
\text{(P)}\qquad
\text{maximize } \c\tp\x \quad \text{subject to} \quad \A\x \le \b,\ \ \x \ge \0 .
\]
A vector \( \x \in \nR^n \) with \( \A\x \le \b \) and \( \x \ge \0 \) is a **feasible point**, and the set of all of them is the **feasible region**. The program is **feasible** if it has a feasible point and **infeasible** otherwise. It is **unbounded** if it is feasible and \( \c\tp\x \) takes **arbitrarily large** values on the feasible region. A feasible \( \x^{\star} \) is an **optimal solution** if \( \c\tp\x^{\star} \ge \c\tp\x \) for **every** feasible \( \x \), and then \( \c\tp\x^{\star} \) is the **optimal value**.
:::

Clause by clause. The function \( \x \mapsto \c\tp\x \) is the **objective**. The \( m \) rows of \( \A\x \le \b \) are the **constraints**, and \( \x \ge \0 \) adds \( n \) more. An optimal solution is a feasible point at which the objective is **as large as anywhere** on the feasible region, and it need not be unique. The optimal value is unique when it exists. A program can fail to have an optimal solution in two ways: it can have no feasible point, or its objective can be unbounded above. Whether those are the **only** two ways is the question the section's second theorem settles.

**Examples.** The workshop problem is (P) with
\[
\A = \begin{pmatrix} 2 & 1 \\ 1 & 3 \\ 1 & 0 \end{pmatrix},
\qquad
\b = \begin{pmatrix} 7 \\ 9 \\ 3 \end{pmatrix},
\qquad
\c = \begin{pmatrix} 4 \\ 3 \end{pmatrix} .
\]

- **One variable.** With \( n = m = 1 \), "maximize \( x \) subject to \( x \le 2 \), \( x \ge 0 \)" has the optimal solution \( x = 2 \). "Maximize \( x \) subject to \( -x \le -1 \), \( x \ge 0 \)" asks for the largest \( x \ge 1 \), and it is unbounded. "Maximize \( x \) subject to \( x \le -1 \), \( x \ge 0 \)" is infeasible.
- **Degenerate case.** If \( \c = \0 \), every feasible point is optimal, with value \( 0 \). The program then asks only whether the system \( \A\x \le \b \), \( \x \ge \0 \) has a solution. So the feasibility question of @cor-farkas-inequality is itself a linear program, the one with no objective.

**Non-example by minimal change.** Make one inequality strict: "maximize \( x \) subject to \( x < 2 \), \( x \ge 0 \)". Everything is still linear, but the supremum \( 2 \) is not attained, and no feasible point is optimal. The definition allows only non-strict inequalities. They define **closed** regions, and closedness will again be what the proofs need.

**Why this form.** Every problem with a linear objective and finitely many linear constraints can be brought to the shape (P). To minimize \( \c\tp\x \), maximize \( (-\c)\tp\x \). A constraint \( \a\tp\x \ge \beta \) is \( (-\a)\tp\x \le -\beta \). An equation \( \a\tp\x = \beta \) is the pair \( \a\tp\x \le \beta \), \( -\a\tp\x \le -\beta \). A variable \( x_j \) without a sign constraint can be written \( x_j = u_j - v_j \) with \( u_j, v_j \ge 0 \). @exr-linear-programming-duality-c2 carries out the last conversion. The form (P), with its sign constraints on \( \x \), is chosen because its dual, below, has the same shape, which makes the theory symmetric.

::: {#exm-lp-workshop}
[The workshop problem, drawn]

Find the optimal solution of the workshop problem, and explain why it is optimal.
:::

::: {.solution}
The feasible region is the pentagon with corners \( (0, 0) \), \( (3, 0) \), \( (3, 1) \), \( \bigl(\tfrac{12}{5}, \tfrac{11}{5}\bigr) \) and \( (0, 3) \). For example, \( (3, 1) \) is where \( x_1 = 3 \) meets \( 2x_1 + x_2 = 7 \), and \( \bigl(\tfrac{12}{5}, \tfrac{11}{5}\bigr) \) solves \( 2x_1 + x_2 = 7 \), \( x_1 + 3x_2 = 9 \): subtracting twice the second equation from the first gives \( -5x_2 = -11 \).

\begin{center}
\begin{tikzpicture}[scale=1.15, lab/.style={font=\small}]
  \fill[black!10] (0,0) -- (3,0) -- (3,1) -- (2.4,2.2) -- (0,3) -- cycle;
  \draw[->, gray] (-0.3,0) -- (4.8,0) node[below, black, lab] {$x_1$};
  \draw[->, gray] (0,-0.3) -- (0,3.9) node[left, black, lab] {$x_2$};
  \draw[thick] (1.6,3.8) -- (3.6,-0.2);
  \node[lab, right] at (1.62,3.75) {$2x_1 + x_2 = 7$};
  \draw[thick] (-0.3,3.1) -- (4.6,1.4667) node[right, lab] {$x_1 + 3x_2 = 9$};
  \draw[thick] (3,-0.2) -- (3,3.2);
  \node[lab, right] at (3,3.2) {$x_1 = 3$};
  \draw[thick, dashed] (1.5,3.4) -- (3.7,0.4667);
  \fill (2.4,2.2) circle (0.06);
  \node[lab, left] at (2.35,2.05) {$\mathbf{x}^{\star}$};
  \draw[->, very thick] (2.4,2.2) -- (3.2,2.8) node[right, lab] {$\mathbf{c}$};
  \node[lab, align=center] at (2.1,-1.2)
    {The feasible region (shaded). The dashed line is the level set\\
     $4x_1 + 3x_2 = 81/5$. Moving it in the direction $\mathbf{c} = (4, 3)$\\
     leaves the region, which it last touches at $\mathbf{x}^{\star} = (12/5, 11/5)$};
\end{tikzpicture}
\end{center}

The level sets \( 4x_1 + 3x_2 = \text{const} \) are parallel lines, and the value grows in the direction \( \c = (4, 3) \). Sliding the line in that direction, the last point of the region it meets appears to be \( \x^{\star} = \bigl(\tfrac{12}{5}, \tfrac{11}{5}\bigr) \), with value
\[
4\cdot\tfrac{12}{5} + 3\cdot\tfrac{11}{5} = \tfrac{48 + 33}{5} = \tfrac{81}{5} .
\]
Comparing the corners supports this: they give \( 0 \), \( 12 \), \( 15 \), \( \tfrac{81}{5} = 16.2 \) and \( 9 \).

A picture is not a proof, and neither is a list of five corners, since we have not proved that an optimum sits at a corner. Here is a proof. Multiply the first constraint by \( \tfrac95 \) and the second by \( \tfrac25 \), both non-negative, and add:
\[
\tfrac95(2x_1 + x_2) + \tfrac25(x_1 + 3x_2) \le \tfrac95\cdot 7 + \tfrac25\cdot 9 = \tfrac{81}{5} .
\]
The left side is \( \bigl(\tfrac{18}{5} + \tfrac25\bigr)x_1 + \bigl(\tfrac95 + \tfrac65\bigr)x_2 = 4x_1 + 3x_2 \). So **every** feasible point has \( 4x_1 + 3x_2 \le \tfrac{81}{5} \), and \( \x^{\star} \), which is feasible (\( \tfrac{12}{5} \le 3 \) as well), reaches this bound. It is optimal, and the optimal value is \( \tfrac{81}{5} \).
:::

The multipliers \( \tfrac95 \) and \( \tfrac25 \) are the heart of the matter. They were chosen so that the combined constraint had exactly the objective as its left side. The best upper bound obtainable this way is itself the answer to a linear program.

## The dual program

Multiply the \( i \)-th constraint of (P) by a number \( y_i \ge 0 \) and add. For every feasible \( \x \) this gives \( \y\tp\A\x \le \y\tp\b \). If the combination dominates the objective coefficient by coefficient, \( \A\tp\y \ge \c \), then, since \( \x \ge \0 \),
\[
\c\tp\x \le (\A\tp\y)\tp\x = \y\tp\A\x \le \y\tp\b .
\]
Each such \( \y \) proves an upper bound \( \b\tp\y \) on the objective, and the natural question is how small that bound can be made.

*The dual program searches for the best upper bound that non-negative combinations of the constraints can prove.*

::: {#def-dual-program}
[Dual Program]

The **dual** of the linear program (P) of @def-linear-program is the problem
\[
\text{(D)}\qquad
\text{minimize } \b\tp\y \quad \text{subject to} \quad \A\tp\y \ge \c,\ \ \y \ge \0 ,
\]
with \( \y \in \nR^m \). The words **feasible**, **infeasible** and **optimal** are used as for (P). (D) is **unbounded** if it is feasible and \( \b\tp\y \) takes **arbitrarily negative** values on its feasible region. In this context (P) is called the **primal** program.
:::

The dual has one variable for each constraint of the primal and one constraint for each variable of the primal. The matrix is transposed, the roles of \( \b \) and \( \c \) are exchanged, and maximization becomes minimization. The dual of (D), written back in inequality form, is (P) again. @exr-linear-programming-duality-c1 checks this, and it explains why a statement about (P) always has a mirror statement about (D).

For the workshop problem the dual is
\[
\begin{aligned}
\text{minimize}\quad & 7y_1 + 9y_2 + 3y_3 \\
\text{subject to}\quad & 2y_1 + y_2 + y_3 \ge 4, \quad y_1 + 3y_2 \ge 3, \\
& y_1, y_2, y_3 \ge 0 ,
\end{aligned}
\]
and the multipliers of @exm-lp-workshop form the dual feasible point \( \y^{\star} = \bigl(\tfrac95, \tfrac25, 0\bigr) \), with \( \b\tp\y^{\star} = \tfrac{81}{5} \). The dual has an economic reading too. \( y_i \) is a price for one unit of the \( i \)-th resource, and the constraints say that at these prices the resources used by one unit of each product are worth at least the profit it brings.

## Weak duality

The computation that motivated (D) is the first theorem, and it is one line long.

::: {#thm-weak-duality}
[Weak Duality]

If \( \x \) is feasible for (P) and \( \y \) is feasible for (D), then
\[
\c\tp\x \le \b\tp\y .
\]
:::

::: {.proof}
Since \( \A\tp\y - \c \ge \0 \) and \( \x \ge \0 \), the number \( (\A\tp\y - \c)\tp\x \) is a sum of products of non-negative numbers, so \( \c\tp\x \le (\A\tp\y)\tp\x = \y\tp(\A\x) \). Since \( \b - \A\x \ge \0 \) and \( \y \ge \0 \), in the same way \( \y\tp(\A\x) \le \y\tp\b = \b\tp\y \). Chaining the two inequalities proves the theorem.
:::

::: {#cor-duality-certificate}
[Certificates from Weak Duality]

::: {.enumerate options="label=(\alph*)"}
1. If \( \x \) is feasible for (P), \( \y \) is feasible for (D), and \( \c\tp\x = \b\tp\y \), then \( \x \) is optimal for (P) and \( \y \) is optimal for (D).
2. If (P) is unbounded, then (D) is infeasible. If (D) is unbounded, then (P) is infeasible.
:::
:::

::: {.idea}
Weak duality makes every dual value an upper bound for every primal value. A primal value that meets one of these bounds cannot be beaten, and neither can the bound; an unbounded program leaves no room for any bound at all.
:::

::: {.proof}
(a) For every feasible \( \x' \), @thm-weak-duality gives \( \c\tp\x' \le \b\tp\y = \c\tp\x \), so \( \x \) is optimal. For every dual feasible \( \y' \), it gives \( \b\tp\y' \ge \c\tp\x = \b\tp\y \), so \( \y \) is optimal.

(b) If (D) had a feasible point \( \y \), @thm-weak-duality would bound \( \c\tp\x \) above by \( \b\tp\y \) for every feasible \( \x \), so (P) would not be unbounded. The second statement is the same argument with the roles exchanged.
:::

Part (a) is exactly what @exm-lp-workshop did: \( \c\tp\x^{\star} = \tfrac{81}{5} = \b\tp\y^{\star} \), so both points are optimal. It gives a certificate of optimality that can be checked by arithmetic alone. The question is whether such a certificate **always** exists. Weak duality allows the best lower bound to stay strictly below the best upper bound.

::: {.check}
Without solving anything, give an upper bound for \( 4x_1 + 3x_2 \) on the workshop's feasible region using only the second constraint \( x_1 + 3x_2 \le 9 \) and \( x \ge \0 \). Which dual feasible point is that?
:::

::: {.solution}
We need \( y_2 \ge 0 \) with \( y_2 \ge 4 \) and \( 3y_2 \ge 3 \), so \( y_2 = 4 \). Then \( 4x_1 + 3x_2 \le 4x_1 + 12x_2 = 4(x_1 + 3x_2) \le 36 \), using \( x_2 \ge 0 \). This is the dual feasible point \( \y = (0, 4, 0) \), with \( \b\tp\y = 36 \). It is a valid bound, but a poor one compared with the optimal \( \tfrac{81}{5} \).
:::

## Strong duality

The main theorem says that the gap allowed by weak duality never occurs, and it gives the complete list of what can happen.

::: {#thm-strong-duality}
[Strong Duality for Linear Programs]

Let \( \A \in M_{m \times n}(\nR) \), \( \b \in \nR^m \) and \( \c \in \nR^n \), and let (P) and (D) be as in @def-linear-program and @def-dual-program.

::: {.enumerate options="label=(\alph*)"}
1. If (P) and (D) are both feasible, then both have optimal solutions, and their optimal values are **equal**: there are feasible \( \x^{\star} \) and \( \y^{\star} \) with \( \c\tp\x^{\star} = \b\tp\y^{\star} \).
2. If (P) is feasible and (D) is infeasible, then (P) is unbounded.
3. If (D) is feasible and (P) is infeasible, then (D) is unbounded.
:::
:::

::: {.idea}
Parts (b) and (c) are each one application of @cor-farkas-inequality. The infeasibility of one program yields a vector that the other program can move along forever, with its objective improving without bound.

For (a) we want a single pair \( (\x, \y) \) that is feasible for both programs and has \( \c\tp\x \ge \b\tp\y \). Weak duality then forces equality, and @cor-duality-certificate forces optimality. The pair is a solution of one big system of inequalities in \( (\x, \y) \), so we ask Farkas whether it has one. If it had none, Farkas would hand us a certificate \( (\u, \v, t) \). The number \( t \) is the multiplier on the row \( \b\tp\y \le \c\tp\x \). If \( t > 0 \), rescaling the certificate by \( 1/t \) produces a primal and a dual feasible point that violate weak duality. If \( t = 0 \), the certificate is a pair of directions along which one of the two programs is unbounded, which contradicts weak duality against a feasible point of the other.
:::

::: {.proof}
**(b)** Let \( \x_0 \) be feasible for (P). That (D) is infeasible says that the system \( (-\A\tp)\y \le -\c \), \( \y \ge \0 \) has no solution. By @cor-farkas-inequality, applied with \( \M = -\A\tp \) and \( \d = -\c \), there is \( \w \in \nR^n \) with \( \w \ge \0 \), \( (-\A\tp)\tp\w = -\A\w \ge \0 \) and \( -\c\tp\w < 0 \). That is, \( \A\w \le \0 \) and \( \c\tp\w > 0 \). For every \( s \ge 0 \) the point \( \x_0 + s\w \) is feasible, since \( \A(\x_0 + s\w) = \A\x_0 + s\A\w \le \b \) and \( \x_0 + s\w \ge \0 \). Its objective value is \( \c\tp\x_0 + s\,\c\tp\w \), which is larger than any given number once \( s \) is large enough, because \( \c\tp\w > 0 \). So (P) is unbounded.

**(c)** Let \( \y_0 \) be feasible for (D). That (P) is infeasible says that \( \A\x \le \b \), \( \x \ge \0 \) has no solution. By @cor-farkas-inequality with \( \M = \A \) and \( \d = \b \), there is \( \w \in \nR^m \) with \( \w \ge \0 \), \( \A\tp\w \ge \0 \) and \( \b\tp\w < 0 \). For \( s \ge 0 \) the point \( \y_0 + s\w \) is feasible for (D), since \( \A\tp(\y_0 + s\w) \ge \A\tp\y_0 \ge \c \) and \( \y_0 + s\w \ge \0 \). Its value \( \b\tp\y_0 + s\,\b\tp\w \) is below any given number for large \( s \). So (D) is unbounded.

**(a)** Let \( \x_0 \) be feasible for (P) and \( \y_0 \) feasible for (D). Consider the \( (m + n + 1) \times (n + m) \) matrix and the vector
\[
\M = \begin{pmatrix} \A & \0 \\ \0 & -\A\tp \\ -\c\tp & \b\tp \end{pmatrix},
\qquad
\d = \begin{pmatrix} \b \\ -\c \\ 0 \end{pmatrix} .
\]
For \( \z = (\x, \y) \) with \( \x \in \nR^n \) and \( \y \in \nR^m \), the system \( \M\z \le \d \), \( \z \ge \0 \) says exactly that
\[
\A\x \le \b, \quad \A\tp\y \ge \c, \quad \b\tp\y \le \c\tp\x, \quad \x \ge \0, \quad \y \ge \0 .
\]{#eq-strong-duality-system}

*Suppose @eq-strong-duality-system has a solution \( (\x^{\star}, \y^{\star}) \).* Then \( \x^{\star} \) is feasible for (P) and \( \y^{\star} \) is feasible for (D), so @thm-weak-duality gives \( \c\tp\x^{\star} \le \b\tp\y^{\star} \). Together with \( \b\tp\y^{\star} \le \c\tp\x^{\star} \), this gives equality, and by @cor-duality-certificate (a) both points are optimal. That is (a).

*It remains to show that @eq-strong-duality-system has a solution.* Suppose not. By @cor-farkas-inequality there is \( \w \ge \0 \) with \( \M\tp\w \ge \0 \) and \( \d\tp\w < 0 \). Write \( \w = (\u, \v, t) \) with \( \u \in \nR^m \), \( \v \in \nR^n \) and \( t \in \nR \), all \( \ge 0 \). Since
\[
\M\tp = \begin{pmatrix} \A\tp & \0 & -\c \\ \0 & -\A & \b \end{pmatrix} ,
\]
the conditions read
\[
\A\tp\u \ge t\c, \qquad \A\v \le t\b, \qquad \b\tp\u < \c\tp\v .
\]{#eq-strong-duality-certificate}

*Case 1: \( t > 0 \).* Dividing @eq-strong-duality-certificate by \( t \) shows that \( \v/t \ge \0 \) is feasible for (P), that \( \u/t \ge \0 \) is feasible for (D), and that \( \b\tp(\u/t) < \c\tp(\v/t) \). This contradicts @thm-weak-duality.

*Case 2: \( t = 0 \).* Now \( \A\tp\u \ge \0 \), \( \A\v \le \0 \) and \( \b\tp\u < \c\tp\v \), with \( \u, \v \ge \0 \). The strict inequality forces \( \c\tp\v > 0 \) or \( \b\tp\u < 0 \), since otherwise \( \b\tp\u \ge 0 \ge \c\tp\v \). If \( \c\tp\v > 0 \), then, exactly as in the proof of (b), the points \( \x_0 + s\v \) with \( s \ge 0 \) are feasible for (P) with objective values tending to \( +\infty \). That contradicts the bound \( \c\tp\x \le \b\tp\y_0 \) that @thm-weak-duality gives for every feasible \( \x \). If \( \b\tp\u < 0 \), then, as in the proof of (c), the points \( \y_0 + s\u \) are feasible for (D) with values tending to \( -\infty \), which contradicts \( \b\tp\y \ge \c\tp\x_0 \).

Both cases are impossible, so @eq-strong-duality-system has a solution, and (a) is proved. This proves the theorem.
:::

Together with @cor-duality-certificate (b), the theorem sorts every pair (P), (D) into exactly one of four cases:

| (P) | (D) | what happens |
|---|---|---|
| feasible | feasible | both optimal, equal values (a) |
| feasible | infeasible | (P) unbounded (b) |
| infeasible | feasible | (D) unbounded (c) |
| infeasible | infeasible | nothing more to say |

All four occur. The workshop problem is the first. The one-variable program "maximize \( x \) subject to \( -x \le -1 \), \( x \ge 0 \)" is the second: its dual, "minimize \( -y \) subject to \( -y \ge 1 \), \( y \ge 0 \)", is infeasible. "Maximize \( 0 \cdot x \) subject to \( x \le -1 \), \( x \ge 0 \)" is the third: its dual, "minimize \( -y \) subject to \( y \ge 0 \)", is unbounded. For the fourth, take
\[
\A = \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}, \qquad \b = \begin{pmatrix} -1 \\ -1 \end{pmatrix}, \qquad \c = \begin{pmatrix} 1 \\ 1 \end{pmatrix} .
\]
Adding the two primal constraints gives \( 0 \le -2 \), and adding the two dual constraints gives \( 0 \ge 2 \), so neither program is feasible.

The table has a consequence that is easy to state and not at all obvious.

::: {#cor-lp-optimum-attained}
[Bounded Linear Programs Attain Their Optimum]

If (P) is feasible and its objective is bounded above on the feasible region, that is, \( \c\tp\x \le N \) for some \( N \) and every feasible \( \x \), then (P) has an optimal solution. The same holds for (D) with "bounded below".
:::

::: {.proof}
Since (P) is feasible and not unbounded, part (b) of @thm-strong-duality shows that (D) is not infeasible. So both programs are feasible, and part (a) gives an optimal solution of (P). The statement for (D) follows in the same way from part (c).
:::

Why is this not obvious? The feasible region is closed, but it may be unbounded, so the extreme value theorem (A4) of Chapter 15's introduction does not apply to it. And a linear function that is bounded above on a closed convex set need not attain its supremum. On the region \( R = \{ (x_1, x_2) : x_1 > 0,\ x_1x_2 \ge 1 \} \), bounded by a branch of a hyperbola, the linear function \( -x_2 \) is negative everywhere, and it takes values arbitrarily close to \( 0 \) at the points \( (k, 1/k) \), so its supremum is \( 0 \). That supremum is never reached. The region \( R \) is the set \( A \) of @exm-hyperbola-asymptote, since \( x_1 > 0 \) and \( x_1x_2 \ge 1 \) force \( x_2 > 0 \), and that example shows it is closed and convex. But it is not cut out by **finitely many** linear inequalities. That finiteness is what made the cones in the proof finitely generated, and hence closed, by @thm-finitely-generated-cone-closed. The corollary is where finite generation pays off.

::: {.warning}
**Strong duality is a theorem about linear programs, not about optimization in general.** For programs whose objective or constraints are convex but not linear, one can still write down a dual problem, and weak duality still holds, but the two optimal values may differ: a **duality gap**. Extra hypotheses are needed to close it, of which the best known is a strictly feasible point (Slater's condition). That theory belongs to convex optimization and is not developed in this book. For linear programs no hypothesis beyond feasibility is needed, as @thm-strong-duality shows.
:::

## Complementary slackness

Strong duality says that at the optimum the two chains of inequalities in the proof of @thm-weak-duality are equalities. Reading that off term by term gives a test that locates the dual solution once the primal one is known.

::: {#thm-complementary-slackness}
[Complementary Slackness]

Let \( \x \) be feasible for (P) and \( \y \) feasible for (D). Then \( \x \) and \( \y \) are **both** optimal if and only if

::: {.enumerate options="label=(\roman*)"}
1. for every \( i \), \( y_i > 0 \) implies \( (\A\x)_i = b_i \); and
2. for every \( j \), \( x_j > 0 \) implies \( (\A\tp\y)_j = c_j \).
:::
:::

::: {.idea}
The gap \( \b\tp\y - \c\tp\x \) is a sum of products of non-negative numbers, one product for each constraint of either program. Optimality means the gap is zero, which means every product is zero.
:::

::: {.proof}
Expanding and using \( \y\tp\A\x = \x\tp\A\tp\y \),
\[
\b\tp\y - \c\tp\x = \y\tp(\b - \A\x) + \x\tp(\A\tp\y - \c) .
\]{#eq-complementary-slackness}
The first term on the right is \( \sum_i y_i(\b - \A\x)_i \), a sum of products of non-negative numbers, and so is the second. Condition (i) says that every product in the first sum is zero, and (ii) says the same for the second. So (i) and (ii) together hold exactly when the right side of @eq-complementary-slackness is \( 0 \), because a sum of non-negative numbers is zero only when every term is.

\( (\Leftarrow) \) If (i) and (ii) hold, then \( \c\tp\x = \b\tp\y \), and both points are optimal by @cor-duality-certificate (a).

\( (\Rightarrow) \) If both are optimal, then both programs are feasible, and by @thm-strong-duality (a) their optimal values are equal. So \( \c\tp\x = \b\tp\y \), the right side of @eq-complementary-slackness is \( 0 \), and (i) and (ii) hold.
:::

In words: a constraint with a positive price must be tight, and a product that is actually made must exactly pay for its resources. For the workshop problem, \( \x^{\star} = \bigl(\tfrac{12}{5}, \tfrac{11}{5}\bigr) \) has both entries positive, so (ii) requires both dual constraints to be tight:
\[
2y_1 + y_2 + y_3 = 4, \qquad y_1 + 3y_2 = 3 .
\]
The third primal constraint is slack at \( \x^{\star} \), since \( \tfrac{12}{5} < 3 \), so (i) forces \( y_3 = 0 \). The two equations then give \( y_1 = \tfrac95 \) and \( y_2 = \tfrac25 \), both \( \ge 0 \), which recovers the multipliers of @exm-lp-workshop. So the multipliers were not a lucky guess: complementary slackness **finds** them from the primal solution.

## Traffic, with inequalities

We return to Chapter 2's town center, to answer the remark made there. Recall from @exm-traffic-network the four intersections, the five one-way streets \( 1 \to 2 \), \( 2 \to 3 \), \( 3 \to 4 \), \( 4 \to 1 \), \( 1 \to 3 \) with flows \( f_1, \dots, f_5 \), and the incidence matrix \( \N \). Conservation of cars is \( \N\f = \s \) with \( \s = (40, 20, -35, -25) \), and the flows that conserve cars are
\[
\f = (40 - \beta + \alpha,\ 60 - \beta + \alpha,\ 25 + \alpha,\ \alpha,\ \beta), \qquad \alpha, \beta \in \nR .
\]
Chapter 2 asked, with street \( 4 \to 1 \) closed, for the largest possible flow on the diagonal \( 1 \to 3 \), and found \( 40 \) by inspecting the one remaining parameter. That was already a linear program: maximize \( f_5 \) subject to \( \N\f = \s \), \( \f \ge \0 \), \( f_4 = 0 \). Its answer has a one-line certificate. The first row of \( \N\f = \s \), the balance at intersection 1, reads \( f_1 - f_4 + f_5 = 40 \), so \( f_5 = 40 - f_1 + f_4 = 40 - f_1 \le 40 \) because \( f_1 \ge 0 \).

::: {#exm-traffic-lp}
[Capacities on every street]

Suppose street \( 4 \to 1 \) is open again, but every street can carry at most \( 35 \) cars per minute. What is the **smallest** flow the diagonal street \( 1 \to 3 \) can carry, and how would you convince someone that it cannot be smaller?
:::

::: {.solution}
The linear program is: minimize \( f_5 \) subject to \( \N\f = \s \) and \( \0 \le \f \le 35\cdot\1 \). In the parameters, the capacity of street \( 2 \to 3 \) reads \( 60 - \beta + \alpha \le 35 \), so \( \beta \ge 25 + \alpha \ge 25 \), since \( \alpha = f_4 \ge 0 \). The value \( \beta = 25 \) is achieved: with \( \alpha = 0 \) the flow is
\[
\f = (15, 35, 25, 0, 25) ,
\]
every entry of which lies between \( 0 \) and \( 35 \). So the minimum is \( 25 \).

The certificate, in the spirit of the dual, is a non-negative combination of the constraints. Add the balance equations at intersections 1 and 2, \( f_1 - f_4 + f_5 = 40 \) and \( -f_1 + f_2 = 20 \):
\[
f_2 - f_4 + f_5 = 60,
\qquad\text{so}\qquad
f_5 = 60 - f_2 + f_4 \ \ge\ 60 - 35 + 0 = 25 ,
\]
using the capacity \( f_2 \le 35 \) and the sign constraint \( f_4 \ge 0 \). In words: at least sixty cars per minute arrive at the pair of intersections \( \{1, 2\} \) (sixty from outside, plus whatever street \( 4 \to 1 \) brings), and only two streets leave that pair, \( 2 \to 3 \) and the diagonal. The first can take at most \( 35 \), so the diagonal must take at least \( 25 \). This is a **cut** argument, and it is exactly what the dual program of a flow problem computes. The balance equations carry multipliers of either sign, the "potentials" of the intersections, and here they are \( 1 \) at intersections 1 and 2 and \( 0 \) at the others.
:::

This is the answer to Chapter 2's remark. Linear algebra describes the conserving flows as a coset of the null space of \( \N \). Linear programming chooses among them, and duality explains each choice with a certificate that can be read as a statement about the network.

::: {.remark}
Computing optimal solutions of large linear programs is a subject in its own right. The best known method, the simplex method, moves from corner to corner of the feasible region, each time improving the objective. This book does not develop algorithms for linear programming. Section 9 returns to the corners themselves, as the vertices of a polyhedron.
:::

## Exercises

### A. Check your understanding

:::: {#exr-linear-programming-duality-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Write down the dual of: maximize \( 2x_1 + x_2 \) subject to \( x_1 + x_2 \le 3 \), \( x_1 - x_2 \le 1 \), \( \x \ge \0 \).
2. State weak duality and strong duality.
3. Determine whether the following is correct, and justify your answer: if (P) is infeasible, then (D) is unbounded.
4. Determine whether the following is correct, and justify your answer: if (P) is feasible and \( \c\tp\x \le 100 \) for every feasible \( \x \), then (P) has an optimal solution.
5. At an optimal pair \( \x, \y \), suppose \( x_2 > 0 \). What does complementary slackness say about the second constraint of (D)?
:::
::::

::: {.solution}
(a) Minimize \( 3y_1 + y_2 \) subject to \( y_1 + y_2 \ge 2 \), \( y_1 - y_2 \ge 1 \), \( \y \ge \0 \). The columns of \( \A \) become the rows of \( \A\tp \), and \( \b = (3, 1) \) and \( \c = (2, 1) \) exchange roles.

(b) Weak duality (@thm-weak-duality): if \( \x \) is feasible for (P) and \( \y \) for (D), then \( \c\tp\x \le \b\tp\y \). Strong duality (@thm-strong-duality): if both are feasible, both have optimal solutions with equal values. If exactly one is feasible, that one is unbounded.

(c) Incorrect. Both programs can be infeasible, as for \( \A = \begin{psmallmatrix} 1 & -1 \\ -1 & 1\end{psmallmatrix} \), \( \b = (-1, -1) \), \( \c = (1, 1) \) in this section. What is true, by @thm-strong-duality (c), is that if (P) is infeasible **and** (D) is feasible, then (D) is unbounded.

(d) Correct, by @cor-lp-optimum-attained. The bound shows that (P) is not unbounded, so by @thm-strong-duality (b) the dual is feasible, and then (a) gives an optimal solution.

(e) By @thm-complementary-slackness (ii), the second dual constraint is tight: \( (\A\tp\y)_2 = c_2 \).
:::

### B. Practice

:::: {#exr-linear-programming-duality-b1}
[B1: Solve and certify]

Consider: maximize \( x_1 + 2x_2 \) subject to
\[
x_1 + x_2 \le 5, \qquad -x_1 + x_2 \le 1, \qquad 2x_1 - x_2 \le 4, \qquad \x \ge \0 .
\]

::: {.enumerate options="label=(\alph*)"}
1. Sketch the feasible region and guess an optimal solution.
2. Write down the dual, and use complementary slackness to find a candidate dual solution.
3. Prove that both candidates are optimal, and state the optimal value.
:::
::::

::: {.solution}
(a) The region is the pentagon with corners \( (0, 0) \), \( (2, 0) \), \( (3, 2) \), \( (2, 3) \) and \( (0, 1) \), where the objective takes the values \( 0, 2, 7, 8, 2 \). The guess is \( \x^{\star} = (2, 3) \), where \( x_1 + x_2 = 5 \) meets \( -x_1 + x_2 = 1 \).

(b) The dual is: minimize \( 5y_1 + y_2 + 4y_3 \) subject to \( y_1 - y_2 + 2y_3 \ge 1 \), \( y_1 + y_2 - y_3 \ge 2 \), \( \y \ge \0 \). At \( \x^{\star} \) the third constraint is slack, since \( 2\cdot 2 - 3 = 1 < 4 \), so (i) of @thm-complementary-slackness requires \( y_3 = 0 \). Both \( x_j^{\star} > 0 \), so (ii) requires both dual constraints to be tight: \( y_1 - y_2 = 1 \) and \( y_1 + y_2 = 2 \). Hence \( \y^{\star} = \bigl(\tfrac32, \tfrac12, 0\bigr) \).

(c) \( \x^{\star} \) is feasible: \( 5 \le 5 \), \( 1 \le 1 \), \( 1 \le 4 \), and \( \x^{\star} \ge \0 \). \( \y^{\star} \) is feasible: \( \y^{\star} \ge \0 \), \( \tfrac32 - \tfrac12 = 1 \ge 1 \) and \( \tfrac32 + \tfrac12 = 2 \ge 2 \). The objective values are \( \c\tp\x^{\star} = 2 + 6 = 8 \) and \( \b\tp\y^{\star} = \tfrac{15}{2} + \tfrac12 = 8 \). They are equal, so both points are optimal by @cor-duality-certificate (a), and the optimal value is \( 8 \).
:::

:::: {#exr-linear-programming-duality-b2}
[B2: Which case?]

For each program, write down its dual, and determine which of the four cases of @thm-strong-duality occurs. Justify your answer, giving the optimal values where they exist.

::: {.enumerate options="label=(\alph*)"}
1. Maximize \( x_1 + x_2 \) subject to \( x_1 - x_2 \le 1 \), \( \x \ge \0 \).
2. Maximize \( -x_1 \) subject to \( x_1 \le 2 \), \( -x_1 \le -1 \), \( x_1 \ge 0 \).
3. Maximize \( x_1 \) subject to \( x_1 + x_2 \le -1 \), \( \x \ge \0 \).
:::
::::

::: {.solution}
(a) The dual is: minimize \( y \) subject to \( y \ge 1 \), \( -y \ge 1 \), \( y \ge 0 \). The last two constraints conflict, so the dual is infeasible. The primal is feasible, with \( \0 \) a feasible point, so by @thm-strong-duality (b) it is unbounded. Directly, \( (0, s) \) is feasible for every \( s \ge 0 \), with value \( s \).

(b) The dual is: minimize \( 2y_1 - y_2 \) subject to \( y_1 - y_2 \ge -1 \), \( \y \ge \0 \). Both programs are feasible: \( x_1 = 1 \) and \( \y = (0, 1) \). Their values are \( -1 \) and \( 2\cdot 0 - 1 = -1 \), which are equal, so both are optimal by @cor-duality-certificate (a), with optimal value \( -1 \). This is the first case.

(c) The primal is infeasible, since \( x_1 + x_2 \ge 0 > -1 \) for \( \x \ge \0 \). The dual is: minimize \( -y \) subject to \( y \ge 1 \), \( y \ge 0 \), \( y \ge 0 \). It is feasible, and \( -y \) takes arbitrarily negative values, so it is unbounded, as @thm-strong-duality (c) predicts.
:::

:::: {#exr-linear-programming-duality-b3}
[B3: A network with one flow]

In the traffic network of this section, close street \( 4 \to 1 \) and give every other street a capacity of \( 30 \) cars per minute. Show that there is exactly one feasible flow. For its diagonal flow \( f_5 = 30 \), give a certificate, in the style of @exm-traffic-lp, that \( f_5 \ge 30 \) for every feasible flow, and one that \( f_5 \le 30 \).
::::

::: {.solution}
With \( f_4 = \alpha = 0 \) the conserving flows are \( \f = (40 - \beta, 60 - \beta, 25, 0, \beta) \). The capacity of street \( 2 \to 3 \) gives \( 60 - \beta \le 30 \), so \( \beta \ge 30 \). The capacity of the diagonal gives \( \beta \le 30 \). So \( \beta = 30 \), and the only candidate is \( \f = (10, 30, 25, 0, 30) \), which satisfies \( 0 \le f_i \le 30 \) for every street. It is the unique feasible flow.

Lower bound: adding the balance equations at intersections 1 and 2 gives \( f_2 - f_4 + f_5 = 60 \), so \( f_5 = 60 - f_2 + f_4 = 60 - f_2 \ge 30 \) by the capacity \( f_2 \le 30 \), using \( f_4 = 0 \). Upper bound: \( f_5 \le 30 \) is itself a capacity constraint. Each certificate is a non-negative combination of constraints, with free multipliers on the balance equations, as in the example.
:::

### C. Going deeper

:::: {#exr-linear-programming-duality-c1}
[C1: The dual of the dual]

::: {.enumerate options="label=(\alph*)"}
1. Rewrite (D) as a program in the inequality form of @def-linear-program, with data \( (-\A\tp, -\c, -\b) \). Show that the dual of that program, rewritten as a maximization, is (P).
2. Deduce part (c) of @thm-strong-duality from part (b).
:::
::::

::: {.solution}
(a) Minimizing \( \b\tp\y \) is maximizing \( (-\b)\tp\y \), and \( \A\tp\y \ge \c \) is \( (-\A\tp)\y \le -\c \). So (D) is the inequality-form program (D\( ' \)): maximize \( (-\b)\tp\y \) subject to \( (-\A\tp)\y \le -\c \), \( \y \ge \0 \), whose data are \( \A' = -\A\tp \), \( \b' = -\c \), \( \c' = -\b \). By @def-dual-program its dual is: minimize \( \b'^{\top}\x = (-\c)\tp\x \) subject to \( \A'^{\top}\x = -\A\x \ge \c' = -\b \), \( \x \ge \0 \). That is: maximize \( \c\tp\x \) subject to \( \A\x \le \b \), \( \x \ge \0 \), which is (P). Its optimal value is the negative of the minimum above.

(b) Suppose (D) is feasible and (P) is infeasible. Then (D\( ' \)) is feasible, with the same feasible points, and its dual, which by (a) has the same feasible points as (P), is infeasible. By @thm-strong-duality (b) applied to (D\( ' \)), the objective \( (-\b)\tp\y \) takes arbitrarily large values on the feasible region. So \( \b\tp\y \) takes arbitrarily negative values, and (D) is unbounded.
:::

:::: {#exr-linear-programming-duality-c2}
[C2: Free variables]

Let \( \A \in M_{m \times n}(\nR) \), \( \b \in \nR^m \), \( \c \in \nR^n \), and consider the program with **no sign constraint** on \( \x \):
\[
\text{(P}_{\text{free}}\text{)}\qquad \text{maximize } \c\tp\x \ \text{ subject to } \ \A\x \le \b .
\]

::: {.enumerate options="label=(\alph*)"}
1. Prove weak duality between (P\( _{\text{free}} \)) and (D\( _{\text{eq}} \)): minimize \( \b\tp\y \) subject to \( \A\tp\y = \c \), \( \y \ge \0 \).
2. Writing \( \x = \u - \v \) with \( \u, \v \ge \0 \), show that (P\( _{\text{free}} \)) has the same values as an inequality-form program whose dual is (D\( _{\text{eq}} \)). Deduce that if both are feasible, both have optimal solutions with equal values.
:::
::::

::: {.solution}
(a) If \( \A\x \le \b \) and \( \A\tp\y = \c \) with \( \y \ge \0 \), then \( \c\tp\x = (\A\tp\y)\tp\x = \y\tp\A\x \le \y\tp\b \), the last step because \( \y \ge \0 \) and \( \b - \A\x \ge \0 \). No sign condition on \( \x \) is needed, because the first step is an equality.

(b) Every \( \x \in \nR^n \) can be written as \( \u - \v \) with \( \u, \v \ge \0 \): take \( u_j = \max(x_j, 0) \) and \( v_j = \max(-x_j, 0) \). So (P\( _{\text{free}} \)) has the same feasible objective values as the inequality-form program
\[
\text{maximize } \begin{pmatrix} \c \\ -\c \end{pmatrix}\tp\begin{pmatrix} \u \\ \v \end{pmatrix}
\ \text{ subject to } \
\begin{pmatrix} \A & -\A \end{pmatrix}\begin{pmatrix} \u \\ \v \end{pmatrix} \le \b,
\quad \begin{pmatrix} \u \\ \v \end{pmatrix} \ge \0 ,
\]
with an optimal \( (\u, \v) \) giving an optimal \( \x = \u - \v \), and conversely. By @def-dual-program its dual is: minimize \( \b\tp\y \) subject to \( \begin{pmatrix} \A & -\A\end{pmatrix}\tp\y \ge (\c, -\c) \), \( \y \ge \0 \). The constraint reads \( \A\tp\y \ge \c \) and \( -\A\tp\y \ge -\c \), that is, \( \A\tp\y = \c \). So the dual is (D\( _{\text{eq}} \)). If both programs are feasible, @thm-strong-duality (a) gives optimal \( (\u^{\star}, \v^{\star}) \) and \( \y^{\star} \) with equal values, and \( \x^{\star} = \u^{\star} - \v^{\star} \) is optimal for (P\( _{\text{free}} \)).
:::
