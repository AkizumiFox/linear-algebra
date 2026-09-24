# Commutators and Trace-Zero Matrices

The expression \( \A \B - \B \A \) has come up several times already. In Chapter 0 its trace was \( 0 \), which showed that \( \A \B - \B \A = \I_n \) is impossible over \( \nR \) (@exr-matrices-c1). In Chapter 2 the same trace argument showed that the relation \( DS - SD = \id \) between differentiation and multiplication by \( x \) on \( F[x] \) has no finite-dimensional analogue in characteristic \( 0 \) (@exr-algebra-of-linear-maps-c1). Both arguments use one direction only: every matrix of the form \( \A \B - \B \A \) has trace zero. This section asks whether the converse holds. Is every trace-zero matrix of the form \( \A \B - \B \A \)? The answer is yes over a field of characteristic \( 0 \), and the proof is a good example of the block techniques of this chapter: move the matrix into a convenient shape by a similarity, one row and column at a time, and then solve an equation that has become entrywise.

**Which fields.** Commutators, their basic rules, the first similarity lemma and the final theorem on spans work over **every** field \( F \). The lemma on zero diagonals and Shoda's theorem assume that \( F \) has **characteristic \( 0 \)**. We point out exactly where that hypothesis is used, and what happens in characteristic \( p \).

## Commutators

Two matrices \( \A \) and \( \B \) commute when \( \A \B = \B \A \), and most pairs do not. The difference \( \A \B - \B \A \) measures the failure, and it keeps recurring: in the trace arguments above, in the relation between differentiation and multiplication by \( x \), and in the description of trace-like functionals (@exr-projections-and-trace-c2). So we give it a name.

*The commutator of two matrices is the amount by which they fail to commute.*

::: {#def-commutator}
[Commutator]

Let \( n \ge 1 \) and \( \A, \B \in M_n(F) \). The **commutator** of \( \A \) and \( \B \) is
\[
[\A, \B] \coloneqq \A \B - \B \A \in M_n(F) .
\]
A matrix \( \C \in M_n(F) \) is **a commutator** if \( \C = [\X, \Y] \) for **some** \( \X, \Y \in M_n(F) \). For operators \( S, T \in \cL(V) \) on a vector space \( V \), we write likewise \( [S, T] \coloneqq ST - TS \in \cL(V) \).
:::

In words: \( [\A, \B] \) is "\( \A \) then \( \B \)" minus "\( \B \) then \( \A \)", in that order, and it is the zero matrix exactly when \( \A \) and \( \B \) commute. The second sentence of the definition is about a single matrix: being a commutator means that **there exist** two matrices whose commutator it is, and it says nothing about which ones.

**Examples.**

1. **Degenerate cases.** \( [\A, \A] = 0 \) and \( [\A, c\I_n] = c\A - c\A = 0 \) for every \( c \in F \). So the zero matrix is a commutator, in many ways. In \( M_1(F) = F \) every commutator is \( ab - ba = 0 \), so for \( n = 1 \) the only commutator is \( 0 \); this is the smallest case, and it already matches the trace condition, since the only \( 1 \times 1 \) matrix of trace \( 0 \) is \( (0) \).
2. **Matrix units.** Recall that \( \E_{ij}\E_{kl} \) is \( \E_{il} \) if \( j = k \) and \( 0 \) otherwise (@def-matrix-multiplication). So for \( i \ne k \),
\[
[\E_{ij}, \E_{jk}] = \E_{ik} - 0 = \E_{ik}, \qquad\text{and}\qquad [\E_{ij}, \E_{ji}] = \E_{ii} - \E_{jj} \quad (i \ne j).
\]
For instance \( [\E_{12}, \E_{21}] = \diag(1, -1) \) in \( M_2(F) \), and \( [\E_{11}, \E_{12}] = \E_{12} \). Both have trace \( 0 \).
3. **Operators on an infinite-dimensional space.** On \( F[x] \), with \( D \) differentiation and \( S \) multiplication by \( x \), @exr-algebra-of-linear-maps-c1 (a) shows \( [D, S] = \id \). So the identity **is** a commutator of operators on \( F[x] \). This does not contradict anything, because there is no trace on \( \cL(F[x]) \): the trace was defined only on finite-dimensional spaces (@def-trace-operator).

**Non-example by minimal change.** Change the minus sign to a plus: \( \A \B + \B \A \). It is still linear in \( \A \) and in \( \B \), and it is still built from the two products \( \A \B \) and \( \B \A \). What is lost is the trace: \( \tr(\A \B + \B \A) = 2\tr(\A \B) \), which has no reason to vanish. For example \( \E_{12}\E_{21} + \E_{21}\E_{12} = \E_{11} + \E_{22} = \I_2 \), with trace \( 2 \). It also no longer detects commuting: \( \A \A + \A \A = 2\A^2 \) is non-zero for \( \A = \I_n \) over \( \nQ \), although \( \A \) commutes with itself.

**Why this definition.** The order in \( \A \B - \B \A \) is a convention; the other order gives \( [\B, \A] = -[\A, \B] \), which is a commutator too. The notion is invariant under a change of basis: a similarity applied to \( \X \) and \( \Y \) applies to \( [\X, \Y] \). So "being a commutator" is a property of the operator \( \x \mapsto \C\x \), not of the basis used to write \( \C \), and we are free to choose a convenient basis. This is what the proof of the main theorem exploits.

The basic rules are collected here.

::: {#prp-commutator-properties}
[Rules for Commutators]

Let \( \A, \A', \B \in M_n(F) \), \( c \in F \), and let \( \P \in M_n(F) \) be invertible. Then:

::: {.enumerate options="label=(\alph*)"}
1. \( [\A + \A', \B] = [\A, \B] + [\A', \B] \), \( [c\A, \B] = c[\A, \B] \), and \( [\B, \A] = -[\A, \B] \); in particular the commutator is linear in each slot.
2. \( \P^{-1}[\A, \B]\P = [\P^{-1}\A \P, \P^{-1}\B \P] \).
3. \( \tr [\A, \B] = 0 \).
:::
:::

::: {.proof}
(a) By @thm-matrix-multiplication-properties, \( (\A + \A')\B - \B(\A + \A') = (\A \B - \B \A) + (\A'\B - \B \A') \) and \( (c\A)\B - \B(c\A) = c(\A \B - \B \A) \). The last identity is \( \B \A - \A \B = -(\A \B - \B \A) \). Linearity in the second slot follows from the first slot and antisymmetry.

(b) Inserting \( \P \P^{-1} = \I_n \), \( \P^{-1}\A \B \P = (\P^{-1}\A \P)(\P^{-1}\B \P) \), and likewise for \( \B \A \). Subtract, using distributivity.

(c) By @thm-trace-properties (1) and (3), \( \tr(\A \B - \B \A) = \tr(\A \B) - \tr(\B \A) = 0 \).
:::

So every commutator lies in the subspace of trace-zero matrices of @exm-trace-free-matrices. The question of this section is whether it fills that subspace.

## The identity in characteristic \( p \)

Rule (c) is the whole content of the Heisenberg exercises: if \( [\X, \Y] = \I_n \), then \( n \cdot 1 = \tr \I_n = 0 \), which is impossible when \( F \) has characteristic \( 0 \) (@def-characteristic). The obstruction is the number \( n \cdot 1 \), not the identity matrix itself. In characteristic \( p \), the \( p \times p \) identity has trace \( p \cdot 1 = 0 \), and the obstruction disappears. In fact the pair \( D, S \) of Example 3 survives in a finite form.

::: {#exm-heisenberg-characteristic-p}
[The Identity as a Commutator in Characteristic \( p \)]

Let \( F \) have prime characteristic \( p \) (for instance \( F = \nF_p \)). Let \( \D_p \in M_p(F) \) have \( (k, k+1) \)-entry \( k \cdot 1 \) for \( 1 \le k \le p - 1 \), and let \( \S_p \in M_p(F) \) have \( (k+1, k) \)-entry \( 1 \) for \( 1 \le k \le p - 1 \), all other entries \( 0 \). Show that \( [\D_p, \S_p] = \I_p \).
:::

::: {.solution}
The columns of these matrices describe differentiation and multiplication by \( x \) on the list \( 1, x, \dots, x^{p-1} \), where \( x^p \) is replaced by \( 0 \). By @thm-three-views-of-product, \( \S_p\e_k = \e_{k+1} \) for \( k < p \) and \( \S_p\e_p = \0 \), while \( \D_p\e_1 = \0 \) and \( \D_p\e_k = (k-1)\e_{k-1} \) for \( k \ge 2 \). Hence
\[
\D_p\S_p\e_k = k\,\e_k \ (k < p), \quad \D_p\S_p\e_p = \0, \qquad \S_p\D_p\e_k = (k-1)\,\e_k \ (1 \le k \le p),
\]
where for \( k = 1 \) we used \( \S_p\D_p\e_1 = \0 = 0\,\e_1 \). Subtracting, \( [\D_p, \S_p]\e_k = \e_k \) for \( k < p \), and \( [\D_p, \S_p]\e_p = -(p-1)\e_p = (1 - p)\e_p = \e_p \), because \( p \cdot 1 = 0 \) in \( F \) (@def-characteristic, @lem-integer-multiples). So every column of \( [\D_p, \S_p] \) is the corresponding column of \( \I_p \). For \( p = 2 \) this is the pair of @exr-algebra-of-linear-maps-c1 (d), transposed.
:::

::: {.warning}
**"The identity is never a commutator" is a statement about characteristic \( 0 \).** The trace test says that a commutator has trace \( 0 \), and \( \tr \I_n = n \cdot 1 \). Over \( \nR \) this is \( n \ne 0 \); over \( \nF_p \) it is \( 0 \) whenever \( p \) divides \( n \), and then the test is silent. The example above shows that \( \I_p \) really is a commutator over \( \nF_p \). Whenever an argument ends with "\( n \cdot 1 = 0 \), contradiction", check which fields it covers.
:::

## Trace-zero matrices with zero diagonal

We want to write a given trace-zero \( \A \) as \( [\X, \Y] \). Look first at the easiest choice of \( \X \), a diagonal matrix \( \X = \diag(x_1, \dots, x_n) \). For any \( \Y = (y_{ij}) \), @def-matrix-multiplication gives \( (\X \Y)_{ij} = x_iy_{ij} \) and \( (\Y \X)_{ij} = y_{ij}x_j \), so
\[
[\X, \Y]_{ij} = (x_i - x_j)\,y_{ij} . \tag{$\ast$}
\]
The diagonal entries of \( [\X, \Y] \) are all \( 0 \), and each off-diagonal entry can be anything, provided \( x_i \ne x_j \). So a diagonal \( \X \) with distinct entries produces **exactly** the matrices with zero diagonal. A trace-zero matrix need not have zero diagonal, but by @prp-commutator-properties (b) we may replace \( \A \) by any matrix similar to it. The plan is therefore:

① find a similarity that makes the diagonal of \( \A \) zero;
② solve \( (\ast) \) entrywise.

Step ① is the heart of the matter. We do it one diagonal entry at a time, starting with the \( (1, 1) \)-entry.

A matrix is **scalar** if it equals \( \lambda \I_n \) for some \( \lambda \in F \). A scalar matrix is similar only to itself, since \( \P^{-1}(\lambda \I_n)\P = \lambda \I_n \), so its diagonal cannot be changed. Every other matrix can at least be given a zero in the corner. This first lemma holds over every field.

::: {#lem-nonscalar-similar-zero-diagonal-entry}
[A Non-Scalar Matrix Has a Similar Matrix with Zero Corner]

Let \( F \) be any field, let \( n \ge 2 \), and let \( \A \in M_n(F) \) be **not** scalar. Then there is an invertible \( \P \in M_n(F) \) such that the first column of \( \P^{-1}\A \P \) is \( \e_2 \). In particular
\[
\P^{-1}\A \P = \begin{pmatrix} 0 & \r\tp \\ \e_1 & \A_1 \end{pmatrix}
\]
for some \( \r \in F^{n-1} \) and \( \A_1 \in M_{n-1}(F) \) with \( \tr \A_1 = \tr \A \), where \( \e_1 \in F^{n-1} \).
:::

::: {.idea}
Work backwards from the goal. The first column of \( \P^{-1}\A \P \) is the coordinate vector of \( \A\p_1 \) in the basis formed by the columns \( \p_1, \dots, \p_n \) of \( \P \). For it to be \( \e_2 \), we need \( \A\p_1 = \p_2 \). So we want a vector \( \v \) such that \( \v \) and \( \A\v \) are independent, and then we build a basis starting \( \v, \A\v \). Such a \( \v \) exists unless \( \A \) sends every vector to a multiple of itself, and a short argument shows that this forces \( \A \) to be scalar.
:::

::: {.proof}
We first show that there is \( \v \in F^n \) with \( (\v, \A\v) \) linearly independent. Suppose not. Then for every \( \v \ne \0 \) there are \( a, b \in F \), not both zero, with \( a\v + b\A\v = \0 \). If \( b = 0 \), then \( a \ne 0 \) and \( a\v = \0 \), which forces \( \v = \0 \) (@thm-zero-product), a contradiction; so \( b \ne 0 \) and \( \A\v = \lambda_{\v}\v \) with \( \lambda_{\v} = -a/b \). Apply this to \( \e_i \), \( \e_j \) and \( \e_i + \e_j \) for \( i \ne j \):
\[
\lambda_{\e_i + \e_j}\e_i + \lambda_{\e_i + \e_j}\e_j = \A(\e_i + \e_j) = \A\e_i + \A\e_j = \lambda_{\e_i}\e_i + \lambda_{\e_j}\e_j .
\]
Since \( \e_i, \e_j \) are linearly independent, comparing coefficients (@thm-independence-unique-combination) gives \( \lambda_{\e_i} = \lambda_{\e_i + \e_j} = \lambda_{\e_j} \). Hence all \( \lambda_{\e_i} \) equal a common \( \lambda \), so \( \A\e_i = \lambda\e_i \) for every \( i \), and by @thm-three-views-of-product the columns of \( \A \) are those of \( \lambda \I_n \). So \( \A = \lambda \I_n \) is scalar, contrary to the hypothesis.

Take such a \( \v \). By @thm-basis-extension, the independent list \( (\v, \A\v) \) extends to a basis \( (\v, \A\v, \w_3, \dots, \w_n) \) of \( F^n \). Let \( \P \) be the matrix with these columns; it is invertible by @thm-invertible-tfae. Then \( \P\e_1 = \v \) and \( \P\e_2 = \A\v \) (@thm-matrix-times-vector-columns), so the first column of \( \P^{-1}\A \P \) is
\[
\P^{-1}\A \P\e_1 = \P^{-1}\A\v = \P^{-1}\P\e_2 = \e_2 .
\]
Partitioning \( \P^{-1}\A \P \) after the first row and column gives the displayed form. Finally, \( \tr(\P^{-1}\A \P) = \tr \A \) by @thm-trace-similarity-invariant, and \( \tr(\P^{-1}\A \P) = 0 + \tr \A_1 \) by @def-trace, so \( \tr \A_1 = \tr \A \).
:::

::: {.check}
Over \( \nQ \), let \( \A = \begin{pmatrix} 2 & 1 \\ 0 & -2 \end{pmatrix} \). Using \( \v = \e_2 \) in the proof of @lem-nonscalar-similar-zero-diagonal-entry, find \( \P \) and \( \P^{-1}\A \P \), and check that its diagonal is zero.
:::

::: {.solution}
\( \A\e_2 = (1, -2) \), which is not a multiple of \( \e_2 \), so \( (\e_2, \A\e_2) \) is independent and already a basis of \( \nQ^2 \). Then \( \P = \begin{pmatrix} 0 & 1 \\ 1 & -2 \end{pmatrix} \), with \( \det \P = -1 \) and \( \P^{-1} = \begin{pmatrix} 2 & 1 \\ 1 & 0 \end{pmatrix} \). We get \( \A \P = \begin{pmatrix} 1 & 0 \\ -2 & 4 \end{pmatrix} \) and \( \P^{-1}\A \P = \begin{pmatrix} 0 & 4 \\ 1 & 0 \end{pmatrix} \). The first column is \( \e_2 \), as the lemma promises; the \( (2, 2) \)-entry is \( 0 \) as well, because the trace is \( 0 \) and trace is a similarity invariant.
:::

The lemma controls one diagonal entry and hands us a smaller matrix \( \A_1 \) with the same trace. That is exactly the setting for induction on the size. The only thing that can stop the induction is a scalar \( \A_1 \), and here the trace saves us, provided the field has characteristic \( 0 \).

::: {#lem-trace-zero-similar-zero-diagonal}
[Trace Zero Means Similar to Zero Diagonal]

Let \( F \) be a field of **characteristic \( 0 \)**, let \( n \ge 1 \), and let \( \A \in M_n(F) \) with \( \tr \A = 0 \). Then \( \A \) is similar to a matrix all of whose diagonal entries are \( 0 \).
:::

::: {.idea}
Induction on \( n \). If \( \A \) is scalar, \( \A = \lambda \I_n \) with \( n\lambda = 0 \), and characteristic \( 0 \) forces \( \lambda = 0 \): then \( \A = 0 \) already has zero diagonal. Otherwise, @lem-nonscalar-similar-zero-diagonal-entry puts a \( 0 \) in the corner and leaves a trace-zero block \( \A_1 \) of size \( n - 1 \). The induction hypothesis conjugates \( \A_1 \) by some \( \Q \) into zero diagonal. Conjugating the whole matrix by the block diagonal matrix \( (1) \oplus \Q \) does this to the lower block without disturbing the corner.
:::

::: {.proof}
We use induction on \( n \) (@thm-induction). For \( n = 1 \), \( \A = (\tr \A) = (0) \), which has zero diagonal.

Let \( n \ge 2 \), and assume the statement for trace-zero matrices of size \( n - 1 \).

*Case 1: \( \A \) is scalar,* say \( \A = \lambda \I_n \). Then \( 0 = \tr \A = n \cdot \lambda = (n \cdot 1)\lambda \) by @def-trace and @lem-integer-multiples. Since \( F \) has characteristic \( 0 \) and \( n \ge 1 \), \( n \cdot 1 \ne 0 \) (@def-characteristic), so \( \lambda = 0 \). Hence \( \A = 0 \), which has zero diagonal and is similar to itself.

*Case 2: \( \A \) is not scalar.* By @lem-nonscalar-similar-zero-diagonal-entry there is an invertible \( \P \) with
\[
\M \coloneqq \P^{-1}\A \P = \begin{pmatrix} 0 & \r\tp \\ \e_1 & \A_1 \end{pmatrix}, \qquad \tr \A_1 = \tr \A = 0 .
\]
By the induction hypothesis there is an invertible \( \Q \in M_{n-1}(F) \) such that \( \Z_1 \coloneqq \Q^{-1}\A_1\Q \) has zero diagonal. Let \( \R = (1) \oplus \Q = \begin{pmatrix} 1 & \0\tp \\ \0 & \Q \end{pmatrix} \). By @thm-block-diagonal-arithmetic, \( \R \) is invertible with \( \R^{-1} = (1) \oplus \Q^{-1} \). By @thm-block-multiplication,
\[
\begin{aligned}
\R^{-1}\M \R
  &= \begin{pmatrix} 1 & \0\tp \\ \0 & \Q^{-1} \end{pmatrix}\begin{pmatrix} 0 & \r\tp \\ \e_1 & \A_1 \end{pmatrix}\begin{pmatrix} 1 & \0\tp \\ \0 & \Q \end{pmatrix} \\
  &= \begin{pmatrix} 0 & \r\tp \Q \\ \Q^{-1}\e_1 & \Q^{-1}\A_1\Q \end{pmatrix} = \begin{pmatrix} 0 & \r\tp \Q \\ \Q^{-1}\e_1 & \Z_1 \end{pmatrix}.
\end{aligned}
\]
Its \( (1, 1) \)-entry is \( 0 \), and its other diagonal entries are those of \( \Z_1 \), which are \( 0 \). Since \( \R^{-1}\M \R = (\P \R)^{-1}\A(\P \R) \) by @thm-inverse-matrix-properties (3), and \( \P \R \) is invertible, \( \A \) is similar to a matrix with zero diagonal. This completes the induction.
:::

::: {.remark}
The characteristic was used only in Case 1, and only through \( k \cdot 1 \ne 0 \) for the sizes \( k = 2, \dots, n \) that the induction passes through. So the lemma holds, with the same proof, whenever \( F \) has characteristic \( 0 \) or characteristic \( p > n \). Some hypothesis on the characteristic is needed: for \( n = p \), over \( \nF_p \), the matrix \( \I_p \) has trace \( p \cdot 1 = 0 \), but it is scalar, so it is similar only to itself, and its diagonal entries are \( 1 \). The same happens for \( \lambda \I_n \) with \( \lambda \ne 0 \) whenever \( p \) divides \( n \).
:::

## Shoda's theorem

With a zero diagonal available, the diagonal choice of \( \X \) in \( (\ast) \) finishes the job. All we need are \( n \) distinct scalars for the diagonal of \( \X \), and characteristic \( 0 \) provides them.

::: {#thm-shoda}
[Shoda's Theorem]

Let \( F \) be a field of **characteristic \( 0 \)**, let \( n \ge 1 \), and let \( \A \in M_n(F) \). Then \( \A \) is a commutator, that is \( \A = [\X, \Y] \) for some \( \X, \Y \in M_n(F) \), if and only if \( \tr \A = 0 \).
:::

::: {.idea}
One direction is @prp-commutator-properties (c). For the other: ① by @lem-trace-zero-similar-zero-diagonal, \( \A = \P \Z \P^{-1} \) with \( \Z \) of zero diagonal; ② take \( \X_0 = \diag(0, 1, \dots, n-1) \), whose entries are distinct in characteristic \( 0 \); ③ solve \( [\X_0, \Y_0] = \Z \) entrywise with \( (\ast) \), dividing by \( x_i - x_j \ne 0 \); ④ conjugate back with @prp-commutator-properties (b).
:::

::: {.proof}
\( (\Rightarrow) \) If \( \A = [\X, \Y] \), then \( \tr \A = 0 \) by @prp-commutator-properties (c).

\( (\Leftarrow) \) Suppose \( \tr \A = 0 \). By @lem-trace-zero-similar-zero-diagonal there is an invertible \( \P \) such that \( \Z = (z_{ij}) \coloneqq \P^{-1}\A \P \) has \( z_{ii} = 0 \) for all \( i \).

For \( 1 \le i \le n \) let \( x_i \coloneqq (i-1) \cdot 1 \in F \), and \( \X_0 \coloneqq \diag(x_1, \dots, x_n) \). For \( i < j \), @lem-integer-multiples gives \( x_j - x_i = (j - i) \cdot 1 \), which is non-zero because \( j - i \ge 1 \) and \( F \) has characteristic \( 0 \) (@def-characteristic). So the \( x_i \) are distinct, and we may define \( \Y_0 = (y_{ij}) \in M_n(F) \) by
\[
y_{ij} \coloneqq \frac{z_{ij}}{x_i - x_j} \quad (i \ne j), \qquad y_{ii} \coloneqq 0 .
\]
By \( (\ast) \), \( [\X_0, \Y_0]_{ij} = (x_i - x_j)y_{ij} = z_{ij} \) for \( i \ne j \), and \( [\X_0, \Y_0]_{ii} = 0 = z_{ii} \). Hence \( [\X_0, \Y_0] = \Z \).

Let \( \X = \P \X_0\P^{-1} \) and \( \Y = \P \Y_0\P^{-1} \). Applying @prp-commutator-properties (b) with the invertible matrix \( \P^{-1} \),
\[
[\X, \Y] = [\P \X_0\P^{-1}, \P \Y_0\P^{-1}] = \P[\X_0, \Y_0]\P^{-1} = \P \Z \P^{-1} = \A .
\]
This proves that \( \A \) is a commutator.
:::

The proof used characteristic \( 0 \) twice: in the lemma, to rule out non-zero scalar blocks of trace zero, and here, to find \( n \) distinct diagonal entries. The second use needs only \( (j - i) \cdot 1 \ne 0 \) for \( 1 \le j - i \le n - 1 \), and with the remark after @lem-trace-zero-similar-zero-diagonal, the same proof works whenever the characteristic of \( F \) is \( 0 \) or larger than \( n \). Neither use is essential for the **theorem**. In fact the statement "a square matrix over a field is a commutator if and only if its trace is \( 0 \)" is true over **every** field. The proof in positive characteristic needs a different normal form and more work, and we do not give it. @exm-heisenberg-characteristic-p is a small instance: \( \I_p \) over \( \nF_p \) is a commutator, although @lem-trace-zero-similar-zero-diagonal fails for it.

The proof is constructive, and it is worth running once in full.

::: {#exm-commutator-3x3}
[Writing a Trace-Zero \( 3 \times 3 \) Matrix as a Commutator]

Over \( \nQ \), write \( \A = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & -2 \end{pmatrix} \) as a commutator \( [\X, \Y] \).
:::

::: {.solution}
The trace is \( 1 + 1 - 2 = 0 \). We follow the proofs step by step.

*First corner.* \( \A \) is not scalar. Take \( \v = \e_1 \); then \( \A\v = (1, 0, 1) \) is not a multiple of \( \e_1 \). Extend \( (\e_1, \A\e_1) \) by \( \e_2 \), which is not in their span, to a basis, and let
\[
\P_1 = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}, \qquad \M = \P_1^{-1}\A \P_1 = \begin{pmatrix} 0 & 2 & 2 \\ 1 & -1 & 0 \\ 0 & 1 & 1 \end{pmatrix}.
\]
(To check \( \M \) without inverting, verify \( \P_1\M = \A \P_1 \): both equal \( \begin{pmatrix} 1 & 1 & 2 \\ 0 & 1 & 1 \\ 1 & -1 & 0 \end{pmatrix} \).) The first column is \( \e_2 \), and the lower block is \( \A_1 = \begin{pmatrix} -1 & 0 \\ 1 & 1 \end{pmatrix} \), with trace \( 0 \).

*Second corner.* \( \A_1 \) is not scalar. With \( \w = \e_1 \in \nQ^2 \), \( \A_1\w = (-1, 1) \) is independent of \( \e_1 \), so
\[
\Q = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}, \qquad \Q^{-1} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \qquad \Z_1 = \Q^{-1}\A_1\Q = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}.
\]

*Assemble.* With \( \r\tp = (2, 2) \), the proof of @lem-trace-zero-similar-zero-diagonal gives \( \r\tp \Q = (2, 0) \) and \( \Q^{-1}\e_1 = \e_1 \), so for \( \P = \P_1\big((1) \oplus \Q\big) \),
\[
\P = \begin{pmatrix} 1 & 1 & -1 \\ 0 & 0 & 1 \\ 0 & 1 & -1 \end{pmatrix}, \qquad \Z = \P^{-1}\A \P = \begin{pmatrix} 0 & 2 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}, \qquad \P^{-1} = \begin{pmatrix} 1 & 0 & -1 \\ 0 & 1 & 1 \\ 0 & 1 & 0 \end{pmatrix}.
\]

*Solve entrywise.* With \( \X_0 = \diag(0, 1, 2) \), the rule \( y_{ij} = z_{ij}/(x_i - x_j) \) gives \( y_{12} = \frac{2}{-1} = -2 \), \( y_{21} = \frac{1}{1} = 1 \), \( y_{23} = \frac{1}{-1} = -1 \), \( y_{32} = \frac11 = 1 \), and \( y_{13} = y_{31} = 0 \):
\[
\Y_0 = \begin{pmatrix} 0 & -2 & 0 \\ 1 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix}.
\]

*Conjugate back.* \( \X = \P \X_0\P^{-1} \) and \( \Y = \P \Y_0\P^{-1} \) are
\[
\X = \begin{pmatrix} 0 & -1 & 1 \\ 0 & 2 & 0 \\ 0 & -1 & 1 \end{pmatrix}, \qquad \Y = \begin{pmatrix} 1 & -4 & -4 \\ 0 & 1 & 1 \\ 1 & -2 & -2 \end{pmatrix}.
\]
*Check:* \( \X \Y = \begin{pmatrix} 1 & -3 & -3 \\ 0 & 2 & 2 \\ 1 & -3 & -3 \end{pmatrix} \) and \( \Y \X = \begin{pmatrix} 0 & -5 & -3 \\ 0 & 1 & 1 \\ 0 & -3 & -1 \end{pmatrix} \), and \( \X \Y - \Y \X = \A \).
:::

Nothing about these \( \X \) and \( \Y \) is unique. Adding to \( \Y \) any matrix that commutes with \( \X \), for instance a polynomial in \( \X \), gives another solution, by @prp-commutator-properties (a).

## The span of the commutators

Shoda's theorem is about single commutators. A weaker question, with an easier answer that holds over **every** field, is which matrices are **sums** of commutators. Since the trace-zero matrices form a subspace and contain all commutators, the span of the commutators lies inside it. Matrix units show that it is all of it.

::: {#thm-span-of-commutators}
[Commutators Span the Trace-Zero Matrices]

Let \( F \) be any field and \( n \ge 1 \). The span of all commutators \( [\X, \Y] \) with \( \X, \Y \in M_n(F) \) is the subspace \( \{ \A \in M_n(F) : \tr \A = 0 \} \). More precisely, every trace-zero matrix is a linear combination of the commutators
\[
\E_{ij} = [\E_{ii}, \E_{ij}] \ (i \ne j) \qquad\text{and}\qquad \E_{ii} - \E_{nn} = [\E_{in}, \E_{ni}] \ (1 \le i \le n - 1).
\]
:::

::: {.proof}
Let \( W = \{ \A \in M_n(F) : \tr \A = 0 \} \), a subspace by @exm-trace-free-matrices. By @prp-commutator-properties (c), every commutator lies in \( W \), so their span is contained in \( W \) (@thm-span-subspace, the span being the smallest subspace containing them).

For the reverse inclusion, the displayed identities hold by Example 2 after @def-commutator: for \( i \ne j \), \( [\E_{ii}, \E_{ij}] = \E_{ij} \), and for \( i < n \), \( [\E_{in}, \E_{ni}] = \E_{ii} - \E_{nn} \). Now let \( \A = (a_{ij}) \in W \). Writing \( \A \) in the basis of matrix units (@exm-standard-bases) and using \( a_{nn} = -\sum_{i<n} a_{ii} \),
\[
\A = \sum_{i \ne j} a_{ij}\E_{ij} + \sum_{i=1}^{n-1} a_{ii}\E_{ii} + a_{nn}\E_{nn} = \sum_{i \ne j} a_{ij}\E_{ij} + \sum_{i=1}^{n-1} a_{ii}\,(\E_{ii} - \E_{nn}) .
\]
So \( \A \) is a linear combination of commutators, hence lies in their span. (For \( n = 1 \), \( W = \{0\} \) and both sides are \( \{0\} \).)
:::

The theorem lists \( n(n-1) + (n-1) = n^2 - 1 \) commutators spanning the trace-zero matrices. Since \( \tr \colon M_n(F) \to F \) is onto (\( \tr(c\E_{11}) = c \)), the Rank–Nullity Theorem (@thm-rank-nullity) gives that its kernel has dimension \( n^2 - 1 \), so by @thm-right-size-basis (b) these commutators form a basis of it. Over a field of characteristic \( 0 \), Shoda's theorem says much more: the sum of commutators produced here can always be collapsed into a single commutator. In general the set of commutators is not obviously closed under addition, and that is exactly what makes Shoda's theorem a theorem.

::: {.warning}
**The span of a set is not the set.** @thm-span-of-commutators shows that every trace-zero matrix is a **sum** of commutators, over any field, by a two-line argument. It does not show that every trace-zero matrix **is** a commutator. For comparison, in \( M_2(F) \) the matrices of rank at most \( 1 \) span everything (the four matrix units have rank \( 1 \)), yet \( \I_2 \) has rank \( 2 \): a set can span a subspace without filling it. For commutators it happens that the set does fill the subspace, but the proof needs the similarity argument of @lem-trace-zero-similar-zero-diagonal, not just matrix units.
:::

The span theorem gives a clean proof of a fact from Chapter 4: a linear functional \( \varphi \) on \( M_n(F) \) with \( \varphi(\A \B) = \varphi(\B \A) \) is a multiple of the trace. Such a \( \varphi \) kills every commutator, hence their span, which is the kernel of the trace; @exr-commutators-and-shoda-c1 below completes the argument.

## Exercises

### A. Check your understanding

:::: {#exr-commutators-and-shoda-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the commutator \( [\A, \B] \), and state what it means for a matrix to be a commutator.
2. State Shoda's theorem, including the hypothesis on the field.
3. True or false: \( [\A, \B] = [\B, \A] \) for all \( \A, \B \in M_n(F) \). Justify your answer.
4. True or false: over every field, every trace-zero matrix is similar to a matrix with zero diagonal. Justify your answer.
5. Name the two places where the proof of Shoda's theorem uses characteristic \( 0 \).
6. Explain why @thm-span-of-commutators does not by itself prove Shoda's theorem.
:::
::::

::: {.solution}
(a) \( [\A, \B] = \A \B - \B \A \) (@def-commutator). A matrix \( \C \in M_n(F) \) is a commutator if \( \C = [\X, \Y] \) for some \( \X, \Y \in M_n(F) \).

(b) If \( F \) has characteristic \( 0 \) and \( \A \in M_n(F) \), then \( \A = [\X, \Y] \) for some \( \X, \Y \in M_n(F) \) if and only if \( \tr \A = 0 \) (@thm-shoda).

(c) False. \( [\B, \A] = -[\A, \B] \) (@prp-commutator-properties (a)), so equality holds only when \( [\A, \B] = 0 \). For example \( [\E_{12}, \E_{21}] = \diag(1, -1) \) and \( [\E_{21}, \E_{12}] = \diag(-1, 1) \) over \( \nQ \).

(d) False. Over \( \nF_2 \), \( \I_2 \) has trace \( 1 + 1 = 0 \), but it is scalar, so every matrix similar to it equals \( \P^{-1}\I_2\P = \I_2 \), whose diagonal entries are \( 1 \).

(e) In @lem-trace-zero-similar-zero-diagonal, to conclude from \( (n \cdot 1)\lambda = 0 \) that a trace-zero scalar matrix \( \lambda \I_n \) is \( 0 \); and in @thm-shoda, to find \( n \) distinct scalars \( x_i = (i-1) \cdot 1 \) so that we can divide by \( x_i - x_j \).

(f) It says every trace-zero matrix is a **linear combination** of commutators. Shoda's theorem says it is a **single** commutator. A sum of commutators need not visibly be a commutator, since \( [\X, \Y] + [\X', \Y'] \) has no evident expression as \( [\X'', \Y''] \).
:::

### B. Practice

:::: {#exr-commutators-and-shoda-b1}
[B1: A \( 2 \times 2 \) commutator]

Over \( \nQ \), let \( \A = \begin{pmatrix} 3 & -2 \\ 1 & -3 \end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Using \( \v = \e_1 \) as in @lem-nonscalar-similar-zero-diagonal-entry, find an invertible \( \P \) such that \( \Z = \P^{-1}\A \P \) has zero diagonal.
2. With \( \X_0 = \diag(0, 1) \), find \( \Y_0 \) with \( [\X_0, \Y_0] = \Z \).
3. Hence write \( \A = [\X, \Y] \), and check your answer by multiplying out.
:::
::::

::: {.solution}
(a) \( \tr \A = 0 \), and \( \A\e_1 = (3, 1) \) is not a multiple of \( \e_1 \), so \( (\e_1, \A\e_1) \) is a basis of \( \nQ^2 \). Let \( \P = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix} \), so \( \P^{-1} = \begin{pmatrix} 1 & -3 \\ 0 & 1 \end{pmatrix} \). Then \( \A \P = \begin{pmatrix} 3 & 7 \\ 1 & 0 \end{pmatrix} \) and
\[
\Z = \P^{-1}\A \P = \begin{pmatrix} 0 & 7 \\ 1 & 0 \end{pmatrix}.
\]
The first column is \( \e_2 \) by @lem-nonscalar-similar-zero-diagonal-entry, and the \( (2, 2) \)-entry is \( 0 \) because the trace is \( 0 \).

(b) By \( (\ast) \), \( [\X_0, \Y]_{12} = (0 - 1)y_{12} \) and \( [\X_0, \Y]_{21} = (1 - 0)y_{21} \), while the diagonal of \( [\X_0, \Y] \) is zero. So \( y_{12} = -7 \), \( y_{21} = 1 \), and we may take \( y_{11} = y_{22} = 0 \): \( \Y_0 = \begin{pmatrix} 0 & -7 \\ 1 & 0 \end{pmatrix} \).

(c) By the proof of @thm-shoda, \( \X = \P \X_0\P^{-1} \) and \( \Y = \P \Y_0\P^{-1} \):
\[
\X = \begin{pmatrix} 0 & 3 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & -3 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 3 \\ 0 & 1 \end{pmatrix}, \qquad \Y = \begin{pmatrix} 3 & -7 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 1 & -3 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 3 & -16 \\ 1 & -3 \end{pmatrix},
\]
using \( \P \X_0 = \begin{pmatrix} 0 & 3 \\ 0 & 1 \end{pmatrix} \) and \( \P \Y_0 = \begin{pmatrix} 3 & -7 \\ 1 & 0 \end{pmatrix} \). *Check:* \( \X \Y = \begin{pmatrix} 3 & -9 \\ 1 & -3 \end{pmatrix} \), \( \Y \X = \begin{pmatrix} 0 & -7 \\ 0 & 0 \end{pmatrix} \), and \( \X \Y - \Y \X = \begin{pmatrix} 3 & -2 \\ 1 & -3 \end{pmatrix} = \A \).
:::

:::: {#exr-commutators-and-shoda-b2}
[B2: A commutator over \( \nF_2 \)]

Work over \( \nF_2 \), and let \( \A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \tr \A = 0 \) and that \( \A \) is not scalar.
2. Explain why \( \v = \e_1 \) cannot be used in @lem-nonscalar-similar-zero-diagonal-entry, and use \( \v = \e_2 \) instead to find \( \P \) with \( \P^{-1}\A \P \) of zero diagonal.
3. The field \( \nF_2 \) has exactly two elements. Use them as the diagonal of \( \X_0 \) to write \( \A \) as a commutator, by hand.
4. Explain why the same method cannot write \( \I_2 \in M_2(\nF_2) \) as a commutator, and recall a pair \( \X, \Y \) that does.
:::
::::

::: {.solution}
(a) \( \tr \A = 1 + 1 = 0 \) in \( \nF_2 \). \( \A \) has a non-zero off-diagonal entry, while every scalar matrix has zero off-diagonal entries.

(b) \( \A\e_1 = \e_1 \), so \( (\e_1, \A\e_1) \) is dependent. With \( \v = \e_2 \), \( \A\e_2 = (1, 1) \), which is not a multiple of \( \e_2 \), so \( (\e_2, \A\e_2) \) is a basis. Let \( \P = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix} \); since \( \det \P = -1 = 1 \), \( \P^{-1} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} \) (check: \( \P \P^{-1} = \begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix} = \I_2 \) in \( \nF_2 \)). Then \( \A \P = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} \) and \( \Z = \P^{-1}\A \P = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \).

(c) Take \( \X_0 = \diag(0, 1) \). By \( (\ast) \), \( [\X_0, \Y]_{12} = (0 - 1)y_{12} = y_{12} \) (as \( -1 = 1 \)) and \( [\X_0, \Y]_{21} = y_{21} \). So \( \Y_0 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) gives \( [\X_0, \Y_0] = \Z \). Conjugating back, \( \P \X_0 = \begin{pmatrix} 0 & 1 \\ 0 & 1 \end{pmatrix} \) and \( \P \Y_0 = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} \), so
\[
\X = \P \X_0\P^{-1} = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}, \qquad \Y = \P \Y_0\P^{-1} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}.
\]
*Check:* \( \X \Y = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \), \( \Y \X = \begin{pmatrix} 2 & 0 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \), so \( [\X, \Y] = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \A \). (Here \( \Y = \A \): indeed \( [\X, \A] = \A \).)

(d) The method writes \( \Z = \P^{-1}\I_2\P \) as \( [\X_0, \Y_0] \) with \( \X_0 \) diagonal, and by \( (\ast) \) such a commutator has zero diagonal. But \( \I_2 \) is scalar, so \( \P^{-1}\I_2\P = \I_2 \) for every invertible \( \P \), and its diagonal entries are \( 1 \). So the method cannot start. Nevertheless \( \I_2 \) is a commutator: with \( \X = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \) and \( \Y = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \), \( [\X, \Y] = \diag(-1, 1) = \I_2 \) in \( \nF_2 \) (@exr-algebra-of-linear-maps-c1 (d), or @exm-heisenberg-characteristic-p with \( p = 2 \)).
:::

:::: {#exr-commutators-and-shoda-b3}
[B3: Commuting with a diagonal matrix]

Let \( F \) be any field, let \( d_1, \dots, d_n \in F \) be **distinct**, let \( \D = \diag(d_1, \dots, d_n) \), and define \( L \colon M_n(F) \to M_n(F) \) by \( L(\X) = [\D, \X] \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( L \) is linear.
2. Prove that \( \ker L \) is the set of diagonal matrices and \( \im L \) is the set of matrices with zero diagonal.
3. Check that your answer to (b) agrees with the Rank–Nullity Theorem.
4. Hence decide whether \( \begin{pmatrix} 0 & 1 & 2 \\ 3 & 0 & 4 \\ 5 & 6 & 0 \end{pmatrix} \in M_3(\nQ) \) is a commutator with \( \X = \diag(1, 2, 3) \), and if so find \( \Y \).
:::
::::

::: {.solution}
(a) By @prp-commutator-properties (a), \( [\D, \X + \X'] = [\D, \X] + [\D, \X'] \) and \( [\D, c\X] = c[\D, \X] \).

(b) By \( (\ast) \), \( L(\X)_{ij} = (d_i - d_j)x_{ij} \). Since \( d_i - d_j \ne 0 \) for \( i \ne j \), \( L(\X) = 0 \) if and only if \( x_{ij} = 0 \) for all \( i \ne j \), that is, \( \X \) is diagonal. Every \( L(\X) \) has zero diagonal. Conversely, if \( \Z \) has zero diagonal, the matrix \( \Y \) with \( y_{ij} = z_{ij}/(d_i - d_j) \) for \( i \ne j \) and \( y_{ii} = 0 \) satisfies \( L(\Y) = \Z \). So \( \im L \) is exactly the set of zero-diagonal matrices.

(c) The diagonal matrices have basis \( \E_{11}, \dots, \E_{nn} \), so \( \nullity L = n \). The zero-diagonal matrices have basis \( \E_{ij} \) (\( i \ne j \)), so \( \rank L = n^2 - n \). Their sum is \( n^2 = \dim M_n(F) \), as @thm-rank-nullity requires.

(d) Yes, since the matrix has zero diagonal and \( 1, 2, 3 \) are distinct. With \( d = (1, 2, 3) \), \( y_{ij} = z_{ij}/(d_i - d_j) \) gives
\[
\Y = \begin{pmatrix} 0 & \frac{1}{-1} & \frac{2}{-2} \\ \frac{3}{1} & 0 & \frac{4}{-1} \\ \frac{5}{2} & \frac{6}{1} & 0 \end{pmatrix} = \begin{pmatrix} 0 & -1 & -1 \\ 3 & 0 & -4 \\ \frac52 & 6 & 0 \end{pmatrix},
\]
and by (b), \( [\diag(1, 2, 3), \Y] \) is the given matrix.
:::

### C. Going deeper

:::: {#exr-commutators-and-shoda-c1}
[C1: Trace-like functionals, again]

Let \( F \) be any field, \( n \ge 1 \), and let \( \varphi \colon M_n(F) \to F \) be linear with \( \varphi(\A \B) = \varphi(\B \A) \) for all \( \A, \B \in M_n(F) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \varphi \) vanishes on every trace-zero matrix.
2. Deduce that \( \varphi = c\,\tr \), where \( c = \varphi(\E_{11}) \).
3. Suppose \( F \) has characteristic \( 0 \) and, in addition, \( \varphi(\I_n) = n \cdot 1 \). Deduce that \( \varphi = \tr \).
4. Show that the conclusion of (c) fails over \( \nF_p \) when \( n = p \).
:::

*Hint: for (a), use @thm-span-of-commutators.*
::::

::: {.solution}
(a) For all \( \X, \Y \), \( \varphi([\X, \Y]) = \varphi(\X \Y) - \varphi(\Y \X) = 0 \) by linearity and the hypothesis. So the kernel of \( \varphi \), a subspace, contains every commutator, hence their span (@thm-span-subspace), which is the set of trace-zero matrices by @thm-span-of-commutators.

(b) Let \( \A \in M_n(F) \). Since \( \tr \E_{11} = 1 \), the matrix \( \A - (\tr \A)\E_{11} \) has trace \( 0 \) (@thm-trace-properties (1)), so by (a) and linearity,
\[
0 = \varphi\big(\A - (\tr \A)\E_{11}\big) = \varphi(\A) - (\tr \A)\,\varphi(\E_{11}) .
\]
Hence \( \varphi(\A) = c\,\tr \A \) with \( c = \varphi(\E_{11}) \). This recovers @exr-projections-and-trace-c2 by a different route: the matrix-unit computations are now packaged in @thm-span-of-commutators.

(c) By (b), \( n \cdot 1 = \varphi(\I_n) = c\,\tr \I_n = c\,(n \cdot 1) \). Since \( F \) has characteristic \( 0 \), \( n \cdot 1 \ne 0 \), so \( c = 1 \) and \( \varphi = \tr \).

(d) Over \( \nF_p \) with \( n = p \), take \( \varphi = 0 \). It is linear, satisfies \( \varphi(\A \B) = 0 = \varphi(\B \A) \), and \( \varphi(\I_p) = 0 = p \cdot 1 \). But \( \varphi \ne \tr \), since \( \tr \E_{11} = 1 \). The step that fails is canceling \( n \cdot 1 = 0 \) in (c).
:::

:::: {#exr-commutators-and-shoda-c2}
[C2: When \( \A \) commutes with \( [\A, \B] \)]

Let \( F \) be a field of characteristic \( 0 \), let \( \A, \B \in M_n(F) \), put \( \C = [\A, \B] \), and suppose that \( \A \C = \C \A \). The goal is to prove that \( \C \) is **nilpotent**, that is, \( \C^s = 0 \) for some \( s \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \C^k = [\A, \B \C^{k-1}] \) for every \( k \ge 1 \). Deduce that \( \tr \C^k = 0 \) for every \( k \ge 1 \).
2. Show that there are an integer \( s \ge 1 \) and \( g \in F[x] \) with \( g(0) \ne 0 \) such that \( \C^sg(\C) = 0 \).
3. Let \( U = \col(\C^s) \) and \( r = \dim U \), and suppose \( r \ge 1 \). Extend a basis of \( U \) to a basis of \( F^n \), and let \( \P \) be the matrix with these columns. Show that
\[
\P^{-1}\C \P = \begin{pmatrix} \D & \ast \\ 0 & \N \end{pmatrix}, \qquad \D \in M_r(F),
\]
with \( \N^s = 0 \) and \( g(\D) = 0 \).
4. Write \( g = g_0 + xh \) with \( g_0 = g(0) \ne 0 \). Show that \( \I_r \) is a linear combination of \( \D^s, \D^{s+1}, \dots, \D^{d} \) for some \( d \ge s \), and use (a) to reach a contradiction.
5. Conclude that \( \C^s = 0 \).
:::

*Hint: in (c), compare the columns of \( \P^{-1}\C^k\P \) for \( k = 1 \) and \( k = s \) with the coordinates of vectors of \( U \); in (d), take traces.*
::::

::: {.solution}
(a) First, \( \C^{k-1}\A = \A \C^{k-1} \) for all \( k \ge 1 \), by induction on \( k \) from \( \C \A = \A \C \). Hence
\[
\begin{aligned}
[\A, \B \C^{k-1}]
  &= \A \B \C^{k-1} - \B \C^{k-1}\A = \A \B \C^{k-1} - \B \A \C^{k-1} \\
  &= (\A \B - \B \A)\C^{k-1} = \C^k .
\end{aligned}
\]
By @prp-commutator-properties (c), \( \tr \C^k = 0 \).

(b) By @thm-annihilating-polynomial-exists there is a non-zero \( f \in F[x] \) with \( f(\C) = 0 \). Let \( t \ge 0 \) be the largest integer with \( x^t \) dividing \( f \), and write \( f = x^tg \); then \( x \nmid g \), so \( g(0) \ne 0 \) by @thm-remainder-theorem. Put \( s = t + 1 \ge 1 \). By @thm-polynomial-of-matrix-properties, \( \C^sg(\C) = \C\,f(\C) = 0 \).

(c) Let \( \P \) have columns \( \p_1, \dots, \p_n \), where \( (\p_1, \dots, \p_r) \) is a basis of \( U \); \( \P \) is invertible by @thm-invertible-tfae. For any \( k \ge 1 \), column \( j \) of \( \P^{-1}\C^k\P \) is \( \P^{-1}(\C^k\p_j) \), the vector \( \c \) with \( \P\c = \C^k\p_j \), that is, the coefficients of \( \C^k\p_j \) in terms of \( \p_1, \dots, \p_n \) (@thm-matrix-times-vector-columns). If \( \y \in U \), then \( \y = \C^s\z \) and \( \C\y = \C^s(\C\z) \in U \), so \( \C \) maps \( U \) into \( U \); hence for \( j \le r \) the vector \( \C\p_j \) is a combination of \( \p_1, \dots, \p_r \), and column \( j \) of \( \P^{-1}\C \P \) has zeros below row \( r \). This gives the block form. By @thm-block-multiplication and induction on \( k \), \( (\P^{-1}\C \P)^k = \begin{pmatrix} \D^k & \ast \\ 0 & \N^k \end{pmatrix} \), and by @prp-similarity-invariants (c) this is \( \P^{-1}\C^k\P \); more generally \( \P^{-1}q(\C)\P = \begin{pmatrix} q(\D) & \ast \\ 0 & q(\N) \end{pmatrix} \) for every \( q \in F[x] \).

For \( k = s \), every vector \( \C^s\p_j \) lies in \( U \), so every column of \( \P^{-1}\C^s\P \) is zero below row \( r \), and \( \N^s = 0 \). For \( q = g \): for \( j \le r \), \( \p_j \in U \) is \( \C^s\z \) for some \( \z \), so \( g(\C)\p_j = g(\C)\C^s\z = \0 \) by (b) and @thm-polynomial-of-matrix-properties. So the first \( r \) columns of \( \P^{-1}g(\C)\P \) are zero, and in particular \( g(\D) = 0 \).

(d) From \( g(\D) = g_0\I_r + \D h(\D) = 0 \) we get \( \I_r = \D\,h_1(\D) \) with \( h_1 = -g_0^{-1}h \). Since polynomials in \( \D \) commute (@thm-polynomial-of-matrix-properties),
\[
\I_r = \big(\D\,h_1(\D)\big)^s = \D^s\,h_1(\D)^s = \sum_{k=s}^{d} c_k\D^k
\]
for some \( c_k \in F \), as every term of \( x^sh_1(x)^s \) has degree at least \( s \). For \( k \ge s \), \( \N^k = \N^s\N^{k-s} = 0 \), so by (c), @thm-trace-similarity-invariant and @def-trace, \( \tr \C^k = \tr(\P^{-1}\C^k\P) = \tr \D^k + \tr \N^k = \tr \D^k \). Taking traces,
\[
r \cdot 1 = \tr \I_r = \sum_{k=s}^{d} c_k\tr \D^k = \sum_{k=s}^{d} c_k\tr \C^k = 0
\]
by (a). But \( r \ge 1 \) and \( F \) has characteristic \( 0 \), so \( r \cdot 1 \ne 0 \), a contradiction.

(e) By (d), \( r = 0 \), so \( \col(\C^s) = \{\0\} \) and \( \C^s = 0 \). For example, with \( \A = \E_{12} + \E_{23} \) and \( \B = \diag(0, 1, 2) \) in \( M_3(\nQ) \), \( \C = [\A, \B] = \E_{12} + \E_{23} = \A \), which commutes with \( \A \), and indeed \( \C^3 = 0 \). In Chapter 9 the statement "\( \tr \C^k = 0 \) for all \( k \ge 1 \) forces nilpotency in characteristic \( 0 \)" becomes a statement about eigenvalues.
:::
