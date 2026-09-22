# Positive Matrices in Blocks

Chapter 7 cut a matrix into blocks, ran one step of elimination, and gave a name to what was left in the far corner: the Schur complement. Section 1 of this chapter met that same quantity as a single number, in the induction that proved Sylvester's criterion. This section puts the two together. For a Hermitian matrix split into blocks, positive definiteness can be decided one block at a time, and the deciding quantity is the Schur complement; two determinant inequalities, Fischer's and Hadamard's, then come almost for free.

Throughout, \( F = \nR \) or \( F = \nC \), and \( F^n \) carries the standard inner product.

## What the blocks of a positive matrix must satisfy

A Hermitian matrix cut into blocks of sizes \( k \) and \( l \) has a shape forced on it. Suppose

\[
\M = \begin{pmatrix} \A & \B \\ \D & \C \end{pmatrix} \in M_{k+l}(F),
\]

with \( \A \in M_k(F) \), \( \B \in M_{k\times l}(F) \), \( \D \in M_{l\times k}(F) \) and \( \C \in M_l(F) \). Starring a block matrix transposes the arrangement and stars each block, so \( \M^{*} = \M \) says exactly three things: \( \A^{*} = \A \), \( \C^{*} = \C \), and \( \D = \B^{*} \). A Hermitian \( \M \) is therefore always of the form

\[
\M = \begin{pmatrix} \A & \B \\ \B^{*} & \C \end{pmatrix}
\]

with \( \A \) and \( \C \) Hermitian and \( \B \) unrestricted, and we write it this way from now on.

Two necessary conditions for positivity are immediate. The vectors of \( F^{k+l} \) whose last \( l \) coordinates vanish form a copy of \( F^k \), and on them the quadratic form of \( \M \) is the quadratic form of \( \A \):

\[
\begin{pmatrix} \x \\ \0 \end{pmatrix}^{*}\M\begin{pmatrix} \x \\ \0 \end{pmatrix} = \x^{*}\A\x ,
\qquad
\begin{pmatrix} \0 \\ \y \end{pmatrix}^{*}\M\begin{pmatrix} \0 \\ \y \end{pmatrix} = \y^{*}\C\y .
\]

So \( \M \succeq 0 \) forces \( \A \succeq 0 \) and \( \C \succeq 0 \). This is the statement that a principal submatrix of a positive semidefinite matrix is positive semidefinite, used already in the proof of @thm-psd-characterizations, here for the two index blocks \( \{1, \dots, k\} \) and \( \{k+1, \dots, k+l\} \).

The two conditions are not sufficient, and the smallest counterexample has \( k = l = 1 \):

\[
\M = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}, \qquad \A = (0) \succeq 0, \quad \C = (1) \succ 0 .
\]

Here \( \det \M = -1 < 0 \), so \( \M \not\succeq 0 \) by @thm-psd-characterizations (e). Something must couple \( \B \) to \( \A \) and \( \C \), and the \( 2 \times 2 \) case already says what. For \( \M = \begin{psmallmatrix} a & b \\ \conj b & c\end{psmallmatrix} \) Hermitian, @exm-two-by-two-criterion gives \( \M \succ 0 \) if and only if \( a > 0 \) and \( ac - \lvert b\rvert^2 > 0 \). Divide the second condition by the positive number \( a \):

\[
c - \conj{b}\,a^{-1}b > 0 .
\]

Written with \( \B = (b) \), so that \( \B^{*} = (\conj b) \), the left-hand side is the Schur complement \( \M/\A \) of @def-schur-complement. The general statement now writes itself: replace the scalars by blocks.

## Testing one block at a time

::: {#thm-block-psd-schur}
[Positive Definiteness Block by Block]

Let \( k, l \ge 1 \) and let

\[
\M = \begin{pmatrix} \A & \B \\ \B^{*} & \C \end{pmatrix} \in M_{k+l}(F)
\]

be Hermitian, with \( \A \in M_k(F) \), \( \B \in M_{k \times l}(F) \) and \( \C \in M_l(F) \).

::: {.enumerate options="label=(\alph*)"}
1. If \( \M \succeq 0 \), then \( \A \succeq 0 \) and \( \C \succeq 0 \). If \( \M \succ 0 \), then \( \A \succ 0 \) and \( \C \succ 0 \).
2. Suppose \( \A \succ 0 \). Then \( \A \) is invertible, the Schur complement
\[
\M/\A = \C - \B^{*}\A^{-1}\B \in M_l(F)
\]
is Hermitian, and
\[
\M \succ 0 \iff \M/\A \succ 0 , \qquad\quad \M \succeq 0 \iff \M/\A \succeq 0 .
\]
:::
:::

::: {.idea}
Everything is one congruence. Chapter 7's block elimination clears \( \B \) and \( \B^{*} \) at once and leaves \( \A \) and \( \M/\A \) on the diagonal; for a Hermitian \( \M \) the two outer factors of that elimination are adjoint to each other, because the row operation and the column operation are the same operation seen twice. So the elimination is a congruence \( \S^{*}\M\S \), and @prp-congruence-positivity says that a congruence by an invertible matrix neither creates nor destroys positivity. All that remains is to read the verdict off a block **diagonal** matrix, where the quadratic form splits into two independent pieces. This is the step \( (\ast) \) of Section 1's proof of Sylvester's criterion, with the last coordinate replaced by a block of \( l \) coordinates.
:::

::: {.proof}
(a) Let \( \x \in F^k \) and put \( \v = (\x, \0) \in F^{k+l} \). By @thm-block-multiplication, \( \M\v = (\A\x, \B^{*}\x) \), and hence \( \v^{*}\M\v = \x^{*}\A\x \). If \( \M \succeq 0 \), the left side is \( \ge 0 \) for every \( \x \), so \( \A \succeq 0 \); if \( \M \succ 0 \), then \( \x \ne \0 \) forces \( \v \ne \0 \) and the left side is \( > 0 \), so \( \A \succ 0 \). The same argument with \( \v = (\0, \y) \) gives the statements for \( \C \).

(b) Since \( \A \succ 0 \), every eigenvalue of \( \A \) is positive (@thm-pd-characterizations (b)), so \( 0 \notin \spec(\A) \) and \( \A \) is invertible (@thm-invertible-tfae-eigen). Also \( (\A^{-1})^{*} = (\A^{*})^{-1} = \A^{-1} \), so

\[
(\M/\A)^{*} = \C^{*} - \B^{*}(\A^{-1})^{*}\B = \C - \B^{*}\A^{-1}\B = \M/\A ,
\]

and \( \M/\A \) is Hermitian. Put

\[
\S = \begin{pmatrix} \I_k & -\A^{-1}\B \\ 0 & \I_l \end{pmatrix} ,
\qquad
\S^{*} = \begin{pmatrix} \I_k & 0 \\ -\B^{*}\A^{-1} & \I_l \end{pmatrix} ,
\]

the second because \( \A^{-1} \) is Hermitian. By @thm-block-triangular-inverse, \( \S \) is invertible. Two applications of @thm-block-multiplication give

\[
\begin{aligned}
\M\S &= \begin{pmatrix} \A & \B - \A\A^{-1}\B \\ \B^{*} & \C - \B^{*}\A^{-1}\B \end{pmatrix}
      = \begin{pmatrix} \A & 0 \\ \B^{*} & \M/\A \end{pmatrix} , \\[2pt]
\S^{*}(\M\S) &= \begin{pmatrix} \A & 0 \\ \B^{*} - \B^{*}\A^{-1}\A & \M/\A \end{pmatrix}
      = \begin{pmatrix} \A & 0 \\ 0 & \M/\A \end{pmatrix} .
\end{aligned}
\tag{$\ast$}
\]

Write \( \N = \A \oplus (\M/\A) \) for that block diagonal matrix. For \( \y = (\y_1, \y_2) \in F^k \times F^l \),

\[
\y^{*}\N\y = \y_1^{*}\A\y_1 + \y_2^{*}(\M/\A)\y_2 . \tag{$\dagger$}
\]

::: {.claim}
Given \( \A \succ 0 \): \( \N \succ 0 \) if and only if \( \M/\A \succ 0 \), and \( \N \succeq 0 \) if and only if \( \M/\A \succeq 0 \).
:::

::: {.proof}
Taking \( \y_1 = \0 \) in \( (\dagger) \) shows that positivity of \( \N \), weak or strict, passes to \( \M/\A \), since \( \y_2 \ne \0 \) forces \( \y \ne \0 \). Conversely, suppose \( \M/\A \succeq 0 \); then both terms of \( (\dagger) \) are \( \ge 0 \), so \( \N \succeq 0 \). If moreover \( \M/\A \succ 0 \), then for \( \y \ne \0 \) at least one of \( \y_1 \), \( \y_2 \) is non-zero, so at least one term of \( (\dagger) \) is \( > 0 \) while the other is \( \ge 0 \); hence \( \N \succ 0 \).
:::

Finally \( \S \) is invertible, so @prp-congruence-positivity (b) gives \( \M \succ 0 \) if and only if \( \S^{*}\M\S = \N \succ 0 \). For the weak version, @prp-congruence-positivity (a) applied to \( \S \) turns \( \M \succeq 0 \) into \( \N \succeq 0 \), and applied to \( \S^{-1} \), together with \( (\S^{-1})^{*}\N\S^{-1} = \M \), turns \( \N \succeq 0 \) back into \( \M \succeq 0 \). Combining with the claim proves (b).
:::

The identity \( (\ast) \) is @thm-block-ldu (a) in disguise. That theorem factors \( \M = \L\,\N\,\U \) with \( \L \) lower and \( \U \) upper block triangular; here \( \L \) and \( \U \) are \( (\S^{-1})^{*} \) and \( \S^{-1} \), so the two outer factors are adjoint to each other and the factorization is a **congruence**, not merely an equivalence. Taking determinants in \( (\ast) \) recovers @thm-schur-determinant,

\[
\det \M = \det \A \cdot \det(\M/\A) ,
\]

which is the form in which we use it below.

Chapter 7 closed its treatment of Schur complements by observing that when \( \M \) is real symmetric the complement \( \M/\A \) is symmetric again, and promising that "Chapter 12 uses Schur complements to test whether \( \M \) is positive definite one block at a time". @thm-block-psd-schur is that test, and part (b) says exactly what the promise says: once the corner block \( \A \) is known to be positive definite, the whole of \( \M \) is positive definite precisely when the smaller matrix \( \M/\A \) is. A question about \( k + l \) coordinates has become a question about \( l \) of them.

It also finishes what Section 1 started. There, in the induction proving Sylvester's criterion, the matrix was split with \( k = n-1 \) and \( l = 1 \); the shear \( \S \) was the matrix above with the column \( \b \) in place of \( \B \); and the congruence came out as \( \S^{*}\A\S = \A' \oplus (s) \) with the single number \( s = d - \b^{*}\A'^{-1}\b \) in the corner. That section promised that Section 6 would replace the scalar by a block. The scalar has become \( \M/\A \), and the argument is word for word the same one.

::: {#exm-block-test-four-by-four}
[A \( 4 \times 4 \) Tested in \( 2 \times 2 \) Blocks]

Decide whether each of

\[
\M = \left(\begin{array}{cc|cc} 2 & 1 & 1 & 0 \\ 1 & 1 & 1 & 1 \\ \hline 1 & 1 & 3 & 2 \\ 0 & 1 & 2 & 4 \end{array}\right),
\qquad
\M' = \left(\begin{array}{cc|cc} 2 & 1 & 1 & 0 \\ 1 & 1 & 1 & 1 \\ \hline 1 & 1 & 2 & 0 \\ 0 & 1 & 0 & 2 \end{array}\right)
\]

is positive definite, using the displayed partition. For the one that is not, exhibit a vector on which the quadratic form is negative.
:::

::: {.solution}
Both matrices are real symmetric with the same corner and border,

\[
\A = \begin{pmatrix} 2 & 1 \\ 1 & 1\end{pmatrix}, \qquad \B = \begin{pmatrix} 1 & 0 \\ 1 & 1\end{pmatrix} .
\]

*Step 1: the corner.* The leading principal minors of \( \A \) are \( 2 \) and \( 2 - 1 = 1 \), both positive, so \( \A \succ 0 \) by Sylvester's criterion (@thm-pd-characterizations (d)) and @thm-block-psd-schur (b) applies. Since \( \det \A = 1 \), @thm-two-by-two-inverse gives \( \A^{-1} = \begin{psmallmatrix} 1 & -1 \\ -1 & 2\end{psmallmatrix} \).

*Step 2: the coupling term.* It is the same for both matrices:

\[
\B\tp\A^{-1} = \begin{pmatrix} 0 & 1 \\ -1 & 2\end{pmatrix},
\qquad
\B\tp\A^{-1}\B = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} .
\]

*Step 3: the complements.* For \( \M \), with \( \C = \begin{psmallmatrix} 3 & 2 \\ 2 & 4\end{psmallmatrix} \),

\[
\M/\A = \begin{pmatrix} 3 & 2 \\ 2 & 4\end{pmatrix} - \begin{pmatrix} 1 & 1 \\ 1 & 2\end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} ,
\]

whose leading principal minors are \( 2 \) and \( 3 \). So \( \M/\A \succ 0 \), hence \( \M \succ 0 \). As a by-product, \( \det \M = \det \A\cdot\det(\M/\A) = 1 \cdot 3 = 3 \).

For \( \M' \), with \( \C' = \begin{psmallmatrix} 2 & 0 \\ 0 & 2\end{psmallmatrix} \),

\[
\M'/\A = \begin{pmatrix} 2 & 0 \\ 0 & 2\end{pmatrix} - \begin{pmatrix} 1 & 1 \\ 1 & 2\end{pmatrix} = \begin{pmatrix} 1 & -1 \\ -1 & 0 \end{pmatrix} ,
\]

whose determinant is \( -1 \). So \( \M'/\A \) is not even positive semidefinite, and \( \M' \) is not positive definite.

*Step 4: the witness.* The congruence \( (\ast) \) turns a bad vector for \( \M'/\A \) into a bad vector for \( \M' \). Here \( \y_2 = (1, 1) \) gives \( \y_2\tp(\M'/\A)\y_2 = 1 - 1 - 1 + 0 = -1 \), so \( \y = (0, 0, 1, 1) \) satisfies \( \y\tp(\S\tp\M'\S)\y = -1 \), and \( \x = \S\y \) satisfies \( \x\tp\M'\x = -1 \). Since \( -\A^{-1}\B = \begin{psmallmatrix} 0 & 1 \\ -1 & -2\end{psmallmatrix} \), we get \( \x = (1, -3, 1, 1) \). Checking directly, \( \M'\x = (0, 0, 0, -1) \) and \( \x\tp(\M'\x) = 0 + 0 + 0 - 1 = -1 \).
:::

One \( 2 \times 2 \) inverse and one \( 2 \times 2 \) product replaced four leading principal minors of a \( 4 \times 4 \) matrix. And when the answer is "no", the congruence hands back an explicit vector, which a determinant test never does.

::: {.check}
Let \( \A \succ 0 \). What is \( \M/\A \) when \( \B = 0 \), and what does @thm-block-psd-schur (b) say in that case?
:::

::: {.solution}
When \( \B = 0 \) the Schur complement is \( \M/\A = \C - 0 = \C \), so the criterion reads: \( \M \succ 0 \) if and only if \( \C \succ 0 \). That is the right answer, since \( \M = \A \oplus \C \) is then block diagonal and \( (\dagger) \) says its quadratic form is the sum of the two separate quadratic forms. The general case is this case after the change of variable \( \S \).
:::

::: {.warning}
**The corner must be definite, not merely semidefinite.** If \( \A \) is singular, then \( \A^{-1} \) does not exist, \( \M/\A \) is undefined, and @thm-block-psd-schur (b) says nothing whatsoever. This is a real obstruction, not a gap in the proof. The matrix \( \begin{psmallmatrix} 0 & 1 \\ 1 & 1\end{psmallmatrix} \) above has \( \A \succeq 0 \) and \( \C \succ 0 \) and is **not** positive semidefinite, while \( \begin{psmallmatrix} 0 & 0 \\ 0 & 1\end{psmallmatrix} \), with the same \( \A \) and the same \( \C \), **is**. The two differ only in \( \B \), so no criterion that ignores \( \B \) can separate them.
:::

::: {.remark}
There is a criterion for the semidefinite case with a singular corner, and it has three clauses instead of one: for Hermitian \( \M \), one has \( \M \succeq 0 \) exactly when \( \A \succeq 0 \), every column of \( \B \) lies in the column space of \( \A \), and \( \C - \B^{*}\A^{+}\B \succeq 0 \). The middle clause is what the warning's first matrix violates. The matrix \( \A^{+} \) in the third clause is the Moore–Penrose pseudoinverse; it agrees with \( \A^{-1} \) when \( \A \) is invertible, and it is built from the singular values of \( \A \) in Section 11 of this chapter. The statement and its proof belong there, with the tools they need. This section keeps the definite case, which is the one the rest of the chapter consumes.
:::

## Fischer's inequality

The congruence \( (\ast) \) computes \( \det \M \) as \( \det \A \cdot \det(\M/\A) \). If the Schur complement could be compared with \( \C \), that would bound \( \det \M \) by \( \det \A\det \C \) — and it can be, because \( \C \) is the Schur complement plus something positive:

\[
\C = (\M/\A) + \B^{*}\A^{-1}\B .
\]

So what is needed is that adding a positive semidefinite matrix never decreases a determinant. That is the next lemma, and it is where the square root of Section 2 earns its keep.

::: {#lem-det-psd-increment}
[Adding a positive matrix does not decrease the determinant]

Let \( \P, \Q \in M_n(F) \) with \( \P \succ 0 \) and \( \Q \succeq 0 \). Then

\[
\det(\P + \Q) \ge \det \P > 0 ,
\]

with equality if and only if \( \Q = 0 \).
:::

::: {.idea}
Whiten: divide the problem by \( \P \) on both sides, using the inverse of \( \P^{1/2} \). The sum \( \P + \Q \) becomes \( \I + \K \) with \( \K \succeq 0 \), and the determinant of \( \I + \K \) is \( \prod_i(1 + \mu_i) \) over the eigenvalues \( \mu_i \ge 0 \) of \( \K \). A product of numbers \( \ge 1 \) is \( \ge 1 \), and it equals \( 1 \) only when every factor does.
:::

::: {.proof}
By @thm-psd-square-root the matrix \( \P^{1/2} \succeq 0 \) exists, and it is invertible because \( \P \) is (@thm-psd-square-root (c)). Write \( \R = (\P^{1/2})^{-1} \), which is Hermitian, being the inverse of a Hermitian matrix. Since \( \P^{1/2}\R = \I \) and \( (\P^{1/2})^2 = \P \),

\[
\P^{1/2}\bigl(\I + \R\Q\R\bigr)\P^{1/2} = \P + \Q .
\]

Put \( \K = \R^{*}\Q\R = \R\Q\R \), so that \( \K \succeq 0 \) by @prp-congruence-positivity (a). Taking determinants with @thm-det-multiplicative, and using \( (\det \P^{1/2})^2 = \det \P \),

\[
\det(\P + \Q) = \det \P \cdot \det(\I + \K) .
\]

Now \( \K \) is Hermitian, so \( \K = \U\diag(\mu_1, \dots, \mu_n)\U^{*} \) with \( \U \) unitary, by @cor-spectral-complex-matrix over \( \nC \) and @cor-spectral-real-matrix over \( \nR \); and every \( \mu_i \ge 0 \) by @thm-psd-characterizations (b). Then \( \I + \K = \U\diag(1 + \mu_1, \dots, 1 + \mu_n)\U^{*} \), so

\[
\det(\I + \K) = \prod_{i=1}^{n}(1 + \mu_i) \ge 1 ,
\]

each factor being \( \ge 1 \). Also \( \det \P > 0 \), since the eigenvalues of \( \P \) are positive (@thm-pd-characterizations (b)) and the determinant is their product. Hence \( \det(\P + \Q) \ge \det \P > 0 \).

For the equality case, the product equals \( 1 \) exactly when every \( \mu_i = 0 \), that is when \( \K = \U\,0\,\U^{*} = 0 \), and then \( \Q = \P^{1/2}\K\P^{1/2} = 0 \). Conversely \( \Q = 0 \) gives equality. This proves the lemma.
:::

::: {.remark}
Section 5 states this in its natural generality: the determinant is monotone for the Loewner order, so \( \A \succeq \B \succeq 0 \) implies \( \det \A \ge \det \B \). The special case proved here, in which the smaller of the two matrices is definite, is all this section and the next one need, and its proof is short enough to keep local.
:::

::: {#cor-fischer-inequality}
[Fischer's Inequality]

Let \( \M = \begin{psmallmatrix} \A & \B \\ \B^{*} & \C\end{psmallmatrix} \in M_{k+l}(F) \) with \( \M \succeq 0 \), where \( \A \in M_k(F) \) and \( \C \in M_l(F) \). Then

\[
\det \M \le \det \A \cdot \det \C .
\]

If \( \M \succ 0 \), equality holds if and only if \( \B = 0 \).
:::

::: {.idea}
Do the definite case first and reach the general case by a limit. For \( \M \succ 0 \) the Schur complement exists, the determinant splits as \( \det \A\det(\M/\A) \), and \( \det \C \ge \det(\M/\A) \) by @lem-det-psd-increment applied to \( \C = (\M/\A) + \B^{*}\A^{-1}\B \). For \( \M \succeq 0 \), apply the definite case to \( \M + t\I \) and let \( t \) shrink to \( 0 \): both sides are polynomials in \( t \).
:::

::: {.proof}
*Case 1: \( \M \succ 0 \).* By @thm-block-psd-schur (a), \( \A \succ 0 \), and by (b), \( \M/\A \succ 0 \). By @thm-schur-determinant,

\[
\det \M = \det \A \cdot \det(\M/\A) .
\]

The matrix \( \A^{-1} \) is positive definite. Indeed the eigenvalues of \( \A \) are positive (@thm-pd-characterizations (b)), so \( \A \) is invertible (@thm-invertible-tfae-eigen); the identity \( (\A^{-1})^{*} = (\A^{*})^{-1} = \A^{-1} \) makes \( \A^{-1} \) Hermitian; and @prp-congruence-positivity (b) with the invertible \( \S = \A^{-1} \) turns \( \S^{*}\A\S = \A^{-1}\A\A^{-1} = \A^{-1} \) into \( \A^{-1} \succ 0 \). (This is @exr-positive-definite-matrices-b3.) So \( \Q \coloneqq \B^{*}\A^{-1}\B \succeq 0 \) by @prp-congruence-positivity (a) with \( \S = \B \). Since \( \C = (\M/\A) + \Q \), @lem-det-psd-increment with \( \P = \M/\A \) gives \( \det \C \ge \det(\M/\A) \), with equality if and only if \( \Q = 0 \). Multiplying by \( \det \A > 0 \),

\[
\det \M = \det \A\det(\M/\A) \le \det \A\det \C ,
\]

with equality if and only if \( \B^{*}\A^{-1}\B = 0 \).

It remains to see that \( \B^{*}\A^{-1}\B = 0 \) holds only for \( \B = 0 \). Let \( \R = (\A^{1/2})^{-1} \), a Hermitian matrix with \( \R^2 = \A^{-1} \), as in the proof of @lem-det-psd-increment. Then \( \B^{*}\A^{-1}\B = (\R\B)^{*}(\R\B) \), whose \( (j, j) \) entry is the squared norm of the \( j \)-th column of \( \R\B \). If the whole matrix is \( 0 \), every column of \( \R\B \) is \( \0 \), so \( \R\B = 0 \) and \( \B = \A^{1/2}(\R\B) = 0 \). The converse is clear.

*Case 2: \( \M \succeq 0 \).* For real \( t > 0 \) the matrix \( \M + t\I_{k+l} \) is Hermitian with \( \v^{*}(\M + t\I)\v = \v^{*}\M\v + t\norm{\v}^2 > 0 \) for \( \v \ne \0 \), so \( \M + t\I \succ 0 \). Its blocks are \( \A + t\I_k \), \( \B \) and \( \C + t\I_l \), so Case 1 gives

\[
\det(\M + t\I) \le \det(\A + t\I_k)\cdot\det(\C + t\I_l)
\]

for every \( t > 0 \). A determinant is a polynomial in the entries (@thm-leibniz-formula-alternating), and the entries here are polynomials in \( t \), so both sides are polynomial, hence continuous, functions of \( t \). Letting \( t \) decrease to \( 0 \) preserves the inequality, and at \( t = 0 \) it reads \( \det \M \le \det \A\det \C \). This proves the corollary.
:::

The inequality says that for a positive matrix the off-diagonal blocks are a liability: they can only shrink the determinant, and they cost nothing only when they are absent. Applying it repeatedly, to finer and finer partitions, gives the classical case in which every block is \( 1 \times 1 \). That is the next result.

## Hadamard's inequality

::: {#thm-hadamard-inequality}
[Hadamard's Inequality]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \A \in M_n(F) \) with \( \A \succeq 0 \). Then
\[
\det \A \le a_{11}a_{22}\cdots a_{nn} ,
\]
with equality if and only if \( \A \) is diagonal or some \( a_{ii} = 0 \).
2. Let \( \B \in M_n(F) \) have columns \( \b_1, \dots, \b_n \). Then
\[
\lvert\det \B\rvert \le \norm{\b_1}\,\norm{\b_2}\cdots\norm{\b_n} ,
\]
with equality if and only if the columns are pairwise orthogonal or some column is \( \0 \).
:::
:::

::: {.idea}
Part (a) is Fischer's inequality with \( k = 1 \), applied again and again: peel off the first row and column, bound \( \det \A \) by \( a_{11}\det \A' \), and induct on the size. Part (b) is part (a) for the Gram matrix \( \A = \B^{*}\B \), whose diagonal entries are the squared lengths \( \norm{\b_j}^2 \) and whose determinant is \( \lvert\det \B\rvert^2 \). The equality conditions transfer along the same dictionary: \( \A \) diagonal says the columns of \( \B \) are orthogonal, and \( a_{jj} = 0 \) says \( \b_j = \0 \).
:::

::: {.proof}
(a) Induct on \( n \). For \( n = 1 \) both sides are \( a_{11} \).

Let \( n \ge 2 \) and split \( \A \) with \( k = 1 \):

\[
\A = \begin{pmatrix} a_{11} & \b^{*} \\ \b & \A' \end{pmatrix},
\qquad \b \in F^{n-1},\quad \A' \in M_{n-1}(F) ,
\]

so that \( \A' \) is the submatrix on rows and columns \( 2, \dots, n \). By @thm-block-psd-schur (a), \( \A' \succeq 0 \), and by @cor-fischer-inequality,

\[
\det \A \le a_{11}\det \A' \le a_{11}\,(a_{22}\cdots a_{nn}) ,
\]

the second step being the inductive hypothesis applied to \( \A' \). This is the inequality.

For equality, suppose first that some \( a_{ii} = 0 \). Fix \( j \ne i \) and put \( I = \{i, j\} \). By @thm-psd-characterizations ((a) \( \Rightarrow \) (e)) the principal minor on the rows and columns \( I \) is \( \ge 0 \), so
\[
0 \le \det \A_{I,I} = a_{ii}a_{jj} - \lvert a_{ij}\rvert^2 = -\lvert a_{ij}\rvert^2 ,
\]
forcing \( a_{ij} = 0 \); and \( a_{ji} = \conj{a_{ij}} = 0 \) because \( \A \) is Hermitian. As \( j \ne i \) was arbitrary, row \( i \) and column \( i \) of \( \A \) are zero (which is @exr-positive-definite-matrices-c3 (b)) and \( \det \A = 0 \); the right-hand side is \( 0 \) too, so equality holds. If \( \A \) is diagonal, both sides are the product of the diagonal entries. Conversely, suppose equality holds and every \( a_{ii} > 0 \). Then \( \det \A = a_{11}\cdots a_{nn} > 0 \), so \( \A \) is invertible, and a positive semidefinite matrix with no zero eigenvalue is positive definite (@thm-pd-characterizations (b)). Both inequalities in the display are therefore equalities. The first is the equality case of @cor-fischer-inequality for the positive definite \( \A \), so \( \b = \0 \): the first row and column vanish off the diagonal. The second is the equality case of the inductive hypothesis for \( \A' \), whose diagonal entries are positive, so \( \A' \) is diagonal. Hence \( \A \) is diagonal, and the induction is complete.

(b) Put \( \A = \B^{*}\B \), which is positive semidefinite by @thm-psd-characterizations (c). Its \( (j, j) \) entry is \( \b_j^{*}\b_j = \norm{\b_j}^2 \). By @thm-det-multiplicative, and because \( \det(\B^{*}) = \conj{\det \B} \) — the star transposes, which does not change the determinant (@thm-det-transpose), and conjugates every entry, which conjugates the determinant —

\[
\det \A = \conj{\det \B}\,\det \B = \lvert\det \B\rvert^2 .
\]

Part (a) now reads \( \lvert\det \B\rvert^2 \le \norm{\b_1}^2\cdots\norm{\b_n}^2 \), and taking non-negative square roots gives the inequality.

For equality, note that \( a_{jj} = 0 \) says \( \b_j = \0 \), and that \( \A \) is diagonal exactly when \( \inner{\b_j}{\b_i} = a_{ij} = 0 \) for all \( i \ne j \), that is, exactly when the columns are pairwise orthogonal. So the equality condition of (a) translates into the stated one. This proves the theorem.
:::

::: {.remark}
Part (b) has a geometric reading, and it is the reason the inequality is remembered. Over \( \nR \), \( \lvert\det \B\rvert \) is the volume of the parallelepiped with edges \( \b_1, \dots, \b_n \) (@def-parallelepiped-volume), and the right-hand side is the volume of the box with the same edge lengths. So among all parallelepipeds with prescribed edge lengths, the rectangular one has the largest volume, and up to degenerate cases it is the only one. Tilting an edge costs volume.
:::

\begin{center}
\begin{tikzpicture}[scale=1.25, lab/.style={font=\small}]
    \draw[dashed, black!55] (0,0) -- (2,0) -- (2,1.803) -- (0,1.803) -- cycle;
    \filldraw[fill=black!10, draw=black, thick] (0,0) -- (2,0) -- (3.5,1) -- (1.5,1) -- cycle;
    \draw[->, very thick] (0,0) -- (2,0);
    \draw[->, very thick] (0,0) -- (1.5,1);
    \node[lab, below] at (1.0,-0.04) {$\b_1$};
    \node[lab, above left] at (0.8,0.52) {$\b_2$};
    \node[lab] at (2.6,0.52) {area $\lvert\det\B\rvert$};
    \node[lab, right] at (2.05,1.6) {area $\norm{\b_1}\,\norm{\b_2}$};
    \node[lab, align=center] at (1.5,-0.66)
      {the shaded parallelogram and the dashed rectangle\\ have the same two edge lengths};
\end{tikzpicture}
\end{center}

::: {#exm-hadamard-two-bounds}
[Two Determinant Bounds]

Bound \( \lvert\det \B\rvert \) using @thm-hadamard-inequality (b) for

\[
\B_1 = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix},
\qquad
\B_2 = \begin{pmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2 \end{pmatrix},
\]

and compare each bound with the exact value.
:::

::: {.solution}
For \( \B_1 \), both columns have norm \( \sqrt2 \), so the bound is \( 2 \). The determinant is \( -1 - 1 = -2 \), so \( \lvert\det \B_1\rvert = 2 \) and the bound is attained. The equality case predicts this: \( \inner{(1,-1)}{(1,1)} = 1 - 1 = 0 \), so the columns are orthogonal.

For \( \B_2 \), the columns have norms \( \sqrt5 \), \( \sqrt6 \) and \( \sqrt5 \), so the bound is \( 5\sqrt6 \approx 12.25 \). Expanding along the first row, \( \det \B_2 = 2(4 - 1) - 1(2 - 0) = 4 \). The bound holds and is far from sharp, as it must be, since \( \inner{(1,2,1)}{(2,1,0)} = 4 \ne 0 \) means the columns are not orthogonal.
:::

::: {.warning}
**Part (a) needs positivity; without it the inequality can fail in either direction.** The symmetric matrix

\[
\A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & -1 & 0 \\ 1 & 0 & -1 \end{pmatrix}
\]

has \( \det \A = 3 \), while \( a_{11}a_{22}a_{33} = 1\cdot(-1)\cdot(-1) = 1 \). So \( \det \A > \prod_i a_{ii} \), and a diagonal entry of an indefinite matrix carries no information about the size of the determinant. Part (b), by contrast, has no hypothesis at all — but it bounds by **column** norms. For rows, apply the same result to \( \B\tp \), whose determinant is unchanged (@thm-det-transpose).
:::

## Exercises

### A. Check your understanding

:::: {#exr-block-positive-matrices-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Write down the general form of a Hermitian matrix in \( 2 \times 2 \) block form, and say what each block must satisfy.
2. State @thm-block-psd-schur (b) in full, including its hypothesis.
3. True or false: if \( \M = \begin{psmallmatrix} \A & \B \\ \B^{*} & \C\end{psmallmatrix} \) is Hermitian with \( \A \succeq 0 \) and \( \C \succeq 0 \), then \( \M \succeq 0 \). Justify your answer.
4. State both forms of Hadamard's inequality, and say what hypothesis each one needs.
5. In the proof of Fischer's inequality, which matrix plays the role of \( \Q \) in @lem-det-psd-increment, and which plays the role of \( \P \)?
:::
::::

::: {.solution}
(a) \( \M = \begin{psmallmatrix} \A & \B \\ \B^{*} & \C\end{psmallmatrix} \) with \( \A \in M_k(F) \) and \( \C \in M_l(F) \) Hermitian and \( \B \in M_{k\times l}(F) \) arbitrary. The condition \( \M^{*} = \M \) forces the lower-left block to be \( \B^{*} \) and both diagonal blocks to be Hermitian.

(b) If \( \A \succ 0 \), then \( \A \) is invertible, \( \M/\A = \C - \B^{*}\A^{-1}\B \) is Hermitian, \( \M \succ 0 \) if and only if \( \M/\A \succ 0 \), and \( \M \succeq 0 \) if and only if \( \M/\A \succeq 0 \).

(c) False. Take \( \A = (0) \), \( \B = (1) \) and \( \C = (1) \), so \( \M = \begin{psmallmatrix} 0 & 1 \\ 1 & 1\end{psmallmatrix} \). Both diagonal blocks are positive semidefinite, but \( \det \M = -1 < 0 \), so \( \M \not\succeq 0 \) by @thm-psd-characterizations (e).

(d) By @thm-hadamard-inequality: for \( \A \succeq 0 \), \( \det \A \le a_{11}\cdots a_{nn} \), and the hypothesis is positive semidefiniteness. For any square \( \B \): \( \lvert\det \B\rvert \le \norm{\b_1}\cdots\norm{\b_n} \) over the columns, with no hypothesis.

(e) In @cor-fischer-inequality, \( \P = \M/\A \) and \( \Q = \B^{*}\A^{-1}\B \), so that \( \P + \Q = \C \).
:::

### B. Practice

:::: {#exr-block-positive-matrices-b1}
[B1: Definiteness by blocks]

Each matrix below is real symmetric and is displayed with a \( 2, 2 \) partition. Determine whether it is positive definite. Justify your answer, and for any that is not, give a vector \( \x \) with \( \x\tp\M\x < 0 \).

::: {.enumerate options="label=(\alph*)"}
1. \[ \M_1 = \left(\begin{array}{cc|cc} 1 & 0 & 1 & 1 \\ 0 & 1 & 1 & -1 \\ \hline 1 & 1 & 3 & 0 \\ 1 & -1 & 0 & 3\end{array}\right) \]
2. \[ \M_2 = \left(\begin{array}{cc|cc} 1 & 0 & 1 & 1 \\ 0 & 1 & 1 & -1 \\ \hline 1 & 1 & 2 & 0 \\ 1 & -1 & 0 & 1\end{array}\right) \]
:::
::::

::: {.solution}
In both cases \( \A = \I_2 \succ 0 \) and \( \B = \begin{psmallmatrix} 1 & 1 \\ 1 & -1\end{psmallmatrix} \), so @thm-block-psd-schur (b) applies with \( \A^{-1} = \I_2 \) and

\[
\B\tp\A^{-1}\B = \B\tp\B = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} .
\]

(a) \( \M_1/\A = \begin{psmallmatrix} 3 & 0 \\ 0 & 3\end{psmallmatrix} - \begin{psmallmatrix} 2 & 0 \\ 0 & 2\end{psmallmatrix} = \I_2 \succ 0 \). Hence \( \M_1 \succ 0 \), and \( \det \M_1 = \det \A\det(\M_1/\A) = 1 \).

(b) \( \M_2/\A = \begin{psmallmatrix} 2 & 0 \\ 0 & 1\end{psmallmatrix} - \begin{psmallmatrix} 2 & 0 \\ 0 & 2\end{psmallmatrix} = \begin{psmallmatrix} 0 & 0 \\ 0 & -1\end{psmallmatrix} \). This is the matrix of Section 1's warning: its leading principal minors are \( 0 \) and \( 0 \), and yet it is not positive semidefinite. So \( \M_2 \) is not positive definite, and not even positive semidefinite.

For the witness, \( \y_2 = (0, 1) \) gives \( \y_2\tp(\M_2/\A)\y_2 = -1 \). With \( \S = \begin{psmallmatrix} \I_2 & -\B \\ 0 & \I_2\end{psmallmatrix} \) and \( \y = (0, 0, 0, 1) \), the vector \( \x = \S\y = (-1, 1, 0, 1) \) satisfies \( \x\tp\M_2\x = -1 \).
:::

:::: {#exr-block-positive-matrices-b2}
[B2: A bordered matrix]

Let

\[
\M = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 0 \\ 1 & 0 & 2 \end{pmatrix} .
\]

::: {.enumerate options="label=(\alph*)"}
1. Using the partition with \( k = 1 \), compute \( \M/\A \) and decide whether \( \M \succ 0 \).
2. Hence compute \( \det \M \), and check Fischer's inequality for this partition.
:::
::::

::: {.solution}
(a) Here \( \A = (2) \succ 0 \), \( \B = \begin{pmatrix} 1 & 1\end{pmatrix} \) and \( \C = \begin{psmallmatrix} 2 & 0 \\ 0 & 2\end{psmallmatrix} \). Then

\[
\B^{*}\A^{-1}\B = \tfrac12\begin{pmatrix} 1 \\ 1\end{pmatrix}\begin{pmatrix} 1 & 1\end{pmatrix} = \tfrac12\begin{pmatrix} 1 & 1 \\ 1 & 1\end{pmatrix},
\qquad
\M/\A = \begin{pmatrix} 3/2 & -1/2 \\ -1/2 & 3/2 \end{pmatrix} .
\]

The leading principal minors of \( \M/\A \) are \( 3/2 \) and \( 9/4 - 1/4 = 2 \), both positive, so \( \M/\A \succ 0 \) and \( \M \succ 0 \) by @thm-block-psd-schur (b).

(b) By @thm-schur-determinant, \( \det \M = 2 \cdot 2 = 4 \). Fischer's inequality (@cor-fischer-inequality) for this partition reads \( \det \M \le \det \A\det \C = 2\cdot 4 = 8 \), and indeed \( 4 \le 8 \). The inequality is strict, as it must be, since \( \B \ne 0 \).
:::

:::: {#exr-block-positive-matrices-b3}
[B3: Hadamard bounds]

::: {.enumerate options="label=(\alph*)"}
1. Bound \( \lvert\det \B\rvert \) for \( \B = \begin{psmallmatrix} 1 & 2 \\ 3 & 4\end{psmallmatrix} \), and compare with the exact value.
2. Let
\[
\H = \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & 1 & -1 & -1 \\ 1 & -1 & 1 & -1 \\ 1 & -1 & -1 & 1\end{pmatrix} .
\]
Compute \( \H\tp\H \), and deduce \( \lvert\det \H\rvert \) without expanding the determinant.
:::
::::

::: {.solution}
(a) The columns are \( (1, 3) \) and \( (2, 4) \), with norms \( \sqrt{10} \) and \( \sqrt{20} \), so the bound is \( \sqrt{200} = 10\sqrt2 \approx 14.14 \). The determinant is \( 4 - 6 = -2 \), so \( \lvert\det \B\rvert = 2 \). The bound is true and very weak, because the columns are far from orthogonal.

(b) Every column of \( \H \) has norm \( 2 \), and any two distinct columns are orthogonal: each of the six pairs agrees in two positions and disagrees in the other two, so the dot product is \( 1 + 1 - 1 - 1 = 0 \). Hence \( \H\tp\H = 4\I_4 \). Taking determinants with @thm-det-multiplicative and @thm-det-transpose, \( (\det \H)^2 = 4^4 = 256 \), so \( \lvert\det \H\rvert = 16 \). This is exactly the Hadamard bound \( \norm{\h_1}\cdots\norm{\h_4} = 2^4 = 16 \), as the equality case of @thm-hadamard-inequality (b) predicts for orthogonal columns.
:::

### C. Going deeper

:::: {#exr-block-positive-matrices-c1}
[C1: A zero corner kills its border]

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( \P \succeq 0 \) and \( \x^{*}\P\x = 0 \), then \( \P\x = \0 \).
2. Deduce that if \( \M = \begin{psmallmatrix} \A & \B \\ \B^{*} & \C\end{psmallmatrix} \succeq 0 \) and \( \A = 0 \), then \( \B = 0 \).
3. Deduce that if \( \M \succeq 0 \) and \( \A \) is singular, then \( \M \) is singular. What does Fischer's inequality say in that case?
:::

*Hint for (a): write \( \P = \N^{*}\N \).*
::::

::: {.solution}
(a) By @thm-psd-characterizations (c), \( \P = \N^{*}\N \) for some \( \N \). Then \( 0 = \x^{*}\P\x = \norm{\N\x}^2 \), so \( \N\x = \0 \) and \( \P\x = \N^{*}(\N\x) = \0 \).

(b) Let \( \x \in F^k \) and put \( \v = (\x, \0) \). As computed in the proof of @thm-block-psd-schur (a), \( \v^{*}\M\v = \x^{*}\A\x = 0 \). By (a), \( \M\v = \0 \). But \( \M\v = (\A\x, \B^{*}\x) = (\0, \B^{*}\x) \), so \( \B^{*}\x = \0 \) for every \( \x \in F^k \), that is \( \B^{*} = 0 \) and \( \B = 0 \).

(c) Choose \( \x \ne \0 \) with \( \A\x = \0 \), which is possible since \( \A \) is singular (@thm-invertible-tfae), and put \( \v = (\x, \0) \ne \0 \). Then \( \v^{*}\M\v = \x^{*}\A\x = 0 \), so \( \M\v = \0 \) by (a), and \( \M \) is singular. Hence \( \det \M = 0 \), while \( \det \A\det \C = 0 \) as well, so @cor-fischer-inequality holds with both sides equal to \( 0 \). It is true, and it says nothing; the informative case is \( \A \succ 0 \).
:::

:::: {#exr-block-positive-matrices-c2}
[C2: A Cauchy–Schwarz inequality for blocks]

Let \( \M = \begin{psmallmatrix} \A & \B \\ \B^{*} & \C\end{psmallmatrix} \succeq 0 \) with \( \A \in M_k(F) \) and \( \C \in M_l(F) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that for all \( \x \in F^k \) and \( \y \in F^l \),
\[
\lvert\x^{*}\B\y\rvert^2 \le (\x^{*}\A\x)\,(\y^{*}\C\y) .
\]
2. Deduce the Cauchy–Schwarz inequality \( \lvert\inner{\y}{\x}\rvert \le \norm{\x}\,\norm{\y} \) in \( F^n \).
:::

*Hint for (a): apply the definition of \( \M \succeq 0 \) to the vector \( (\x, t\y) \), and choose the scalar \( t \) well.*
::::

::: {.solution}
(a) Write \( p = \x^{*}\A\x \ge 0 \), \( q = \y^{*}\C\y \ge 0 \) and \( z = \x^{*}\B\y \). For a scalar \( t \in F \), block multiplication (@thm-block-multiplication) gives, for \( \v = (\x, t\y) \),

\[
\v^{*}\M\v = p + \conj{t}\,\conj{z} + tz + \lvert t\rvert^2 q = p + 2\operatorname{Re}(tz) + \lvert t\rvert^2 q \ge 0 ,
\]

where the middle step uses \( \conj{t}\,\conj{z} = \conj{tz} \) and \( w + \conj w = 2\operatorname{Re}(w) \). Now take \( t = r\omega \) with \( r \ge 0 \) real and \( \omega \) a scalar of modulus \( 1 \) chosen so that \( \omega z = -\lvert z\rvert \) (over \( \nR \), \( \omega = \pm1 \)). Then

\[
p - 2r\lvert z\rvert + r^2 q \ge 0 \qquad\text{for every } r \ge 0 . \tag{$\ast$}
\]

If \( q = 0 \), then \( (\ast) \) says \( p \ge 2r\lvert z\rvert \) for all \( r \ge 0 \), which forces \( \lvert z\rvert = 0 \), and the claim reads \( 0 \le 0 \). If \( q > 0 \), take \( r = \lvert z\rvert/q \ge 0 \) in \( (\ast) \):

\[
p - \frac{2\lvert z\rvert^2}{q} + \frac{\lvert z\rvert^2}{q} = p - \frac{\lvert z\rvert^2}{q} \ge 0 ,
\]

so \( \lvert z\rvert^2 \le pq \), as claimed.

(b) Take \( k = l = n \) and \( \A = \B = \C = \I_n \), so that \( \M = \begin{psmallmatrix} \I_n & \I_n \\ \I_n & \I_n\end{psmallmatrix} \). This \( \M \) is positive semidefinite, since \( \M = \W^{*}\W \) for \( \W = \begin{psmallmatrix} \I_n & \I_n \\ 0 & 0\end{psmallmatrix} \) (@thm-psd-characterizations (c)). Part (a) then reads \( \lvert\x^{*}\y\rvert^2 \le \norm{\x}^2\norm{\y}^2 \), and \( \x^{*}\y = \inner{\y}{\x} \) by the definition of the standard inner product. This is @thm-cauchy-schwarz for \( F^n \).
:::

:::: {#exr-block-positive-matrices-c3}
[C3: How large can a determinant be?]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \B \in M_n(F) \) have every entry of modulus at most \( 1 \). Prove that \( \lvert\det \B\rvert \le n^{n/2} \).
2. Show that the bound is attained for \( n = 1 \), \( n = 2 \) and \( n = 4 \).
3. Let \( \B \in M_3(\nR) \) have every entry equal to \( 1 \) or \( -1 \). Prove that \( \det \B \) is a multiple of \( 4 \), and deduce that \( \lvert\det \B\rvert \le 4 \). Hence the bound of (a) is **not** attained for \( n = 3 \).
:::

*Hint for (c): normalize the first row and the first column, then subtract the first column from the other two.*
::::

::: {.solution}
(a) Each column \( \b_j \) has \( n \) entries of modulus \( \le 1 \), so \( \norm{\b_j}^2 = \sum_i\lvert b_{ij}\rvert^2 \le n \) and \( \norm{\b_j} \le \sqrt n \). By @thm-hadamard-inequality (b), \( \lvert\det \B\rvert \le (\sqrt n)^n = n^{n/2} \).

(b) For \( n = 1 \), \( \B = (1) \) gives \( 1 = 1^{1/2} \). For \( n = 2 \), \( \B = \begin{psmallmatrix} 1 & 1 \\ 1 & -1\end{psmallmatrix} \) has \( \lvert\det \B\rvert = 2 = 2^{2/2} \). For \( n = 4 \), the matrix \( \H \) of @exr-block-positive-matrices-b3 (b) has \( \lvert\det \H\rvert = 16 = 4^{4/2} \). In each case all entries have modulus \( 1 \) and the columns are orthogonal, which is exactly what is needed for equality both in \( \norm{\b_j} \le \sqrt n \) and in @thm-hadamard-inequality (b).

(c) Multiplying a row or a column by \( -1 \) multiplies \( \det \B \) by \( -1 \) (@thm-det-row-operations (b) and (d)) and keeps all entries \( \pm 1 \), so we may assume that the first row **and** the first column both consist of \( 1 \)s: first scale the three columns to make the first row \( (1, 1, 1) \), then scale rows \( 2 \) and \( 3 \) to make the first column \( (1, 1, 1) \), which leaves the first row alone. Subtracting column \( 1 \) from columns \( 2 \) and \( 3 \) leaves the determinant unchanged (@thm-det-row-operations (c) and (d)) and gives a matrix whose first row is \( (1, 0, 0) \) and whose remaining entries are \( c_{ij} = b_{ij} - 1 \) for \( i, j \in \{2, 3\} \); each lies in \( \{0, -2\} \), since \( b_{ij} \in \{1, -1\} \). Expanding along the first row (@thm-laplace-expansion),

\[
\det \B = c_{22}c_{33} - c_{23}c_{32}
\]

with every \( c_{ij} \in \{0, -2\} \). Each product lies in \( \{0, 4\} \), so \( \det \B \in \{-4, 0, 4\} \) and in particular \( \lvert\det \B\rvert \le 4 \). Since \( 3^{3/2} = 3\sqrt3 \approx 5.196 > 4 \), the bound of (a) is not attained. The value \( 4 \) does occur, for instance for \( \begin{psmallmatrix} 1 & 1 & 1 \\ 1 & -1 & 1 \\ 1 & 1 & -1\end{psmallmatrix} \).
:::
