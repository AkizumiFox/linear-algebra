# Congruence

The matrix of a form in @def-form-matrix depends on a basis, and a basis is a choice. As with linear maps in Chapter 3, the useful question is therefore not "what is the matrix?" but "which matrices arise from the same form?". The answer here is \( \P\tp\A\P \) rather than \( \P^{-1}\A\P \), and one symbol's difference changes the whole theory: the new relation keeps the rank and the symmetry type of a matrix and throws its eigenvalues away. This section proves the change-of-basis rule, names the relation, sorts the invariants from the casualties, and settles the debt Chapters 11 and 12 ran up when they kept postponing all of this.

Throughout, \( V \) is a vector space over an arbitrary field \( F \) with \( \dim V = n \ge 1 \), and \( \beta \) is a bilinear form on \( V \). **No hypothesis on the characteristic of \( F \) is needed in this section.**

## The change-of-basis rule for a form

Two bases \( \sB \) and \( \sB' \) of \( V \) give two matrices for one form. The link between them is the change-of-coordinates matrix of @def-change-of-coordinates-matrix, and the computation is three lines, because @thm-form-matrix-determines (a) already expresses the form through coordinates.

::: {#thm-change-of-basis-form}
[Change of Basis for a Form]

Let \( \beta \) be a bilinear form on a finite-dimensional \( V \), let \( \sB \) and \( \sB' \) be ordered bases of \( V \), and let \( \P = \mtx{\id}{\sB'}{\sB} \) be the change-of-coordinates matrix from \( \sB' \) to \( \sB \). Then
\[
\mtx{\beta}{\sB'}{} = \P\tp\,\mtx{\beta}{\sB}{}\,\P .
\]
:::

::: {.idea}
There is nothing to discover: write the form in \( \sB \)-coordinates, substitute \( \coord{\v}{\sB} = \P\coord{\v}{\sB'} \) in both slots, and read off the matrix that appears between the two coordinate vectors. The uniqueness clause of @thm-form-matrix-determines then says that matrix is the one we want, with no further checking.
:::

::: {.proof}
Write \( \A = \mtx{\beta}{\sB}{} \). By @thm-change-of-coordinates (a), \( \coord{\v}{\sB} = \P\coord{\v}{\sB'} \) for every \( \v \in V \). So for all \( \u, \v \in V \), using @thm-form-matrix-determines (a) and then @thm-transpose-properties (d),
\[
\begin{aligned}
\beta(\u, \v)
&= \coord{\u}{\sB}\tp\,\A\,\coord{\v}{\sB} \\
&= \bigl(\P\coord{\u}{\sB'}\bigr)\tp\A\,\bigl(\P\coord{\v}{\sB'}\bigr) \\
&= \coord{\u}{\sB'}\tp\,\bigl(\P\tp\A\P\bigr)\,\coord{\v}{\sB'} .
\end{aligned}
\]
Thus \( \P\tp\A\P \) is a matrix with the property that characterizes \( \mtx{\beta}{\sB'}{} \), and by the uniqueness in @thm-form-matrix-determines (b) it **is** \( \mtx{\beta}{\sB'}{} \). This proves the theorem.
:::

Notice that \( \P \) is the same matrix as in @thm-change-of-basis-maps: the change-of-coordinates matrix from the **new** basis to the **old** one, whose columns are the new basis vectors written in old coordinates. Only the way it acts has changed, from \( \P^{-1}\A\P \) to \( \P\tp\A\P \).

::: {#exm-form-in-a-new-basis}
[Killing the cross term]

On \( \nR^2 \), let \( \beta(\x, \y) = x_1y_1 + 2x_1y_2 + 2x_2y_1 + x_2y_2 \), so that
\[
\A = \mtx{\beta}{\sE}{} = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}.
\]
Compute \( \mtx{\beta}{\sB'}{} \) for \( \sB' = \bigl((1, 0),\ (-2, 1)\bigr) \), both by @thm-change-of-basis-form and directly from @def-form-matrix.
:::

::: {.solution}
The columns of \( \P = \mtx{\id}{\sB'}{\sE} \) are the vectors of \( \sB' \) in standard coordinates, so
\[
\P = \begin{pmatrix} 1 & -2 \\ 0 & 1 \end{pmatrix},
\qquad
\A\P = \begin{pmatrix} 1 & 0 \\ 2 & -3 \end{pmatrix},
\]
and therefore
\[
\P\tp\A\P
= \begin{pmatrix} 1 & 0 \\ -2 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 2 & -3 \end{pmatrix}
= \begin{pmatrix} 1 & 0 \\ 0 & -3 \end{pmatrix}.
\]
Directly: with \( \v'_1 = (1,0) \) and \( \v'_2 = (-2,1) \), the four values are \( \beta(\v'_1, \v'_1) = 1 \), \( \beta(\v'_1, \v'_2) = \beta(\v'_2, \v'_1) = 0 \) and \( \beta(\v'_2, \v'_2) = -3 \). The two computations agree.

The new basis was not guessed. In coordinates the form reads \( q(\x) = x_1^2 + 4x_1x_2 + x_2^2 = (x_1 + 2x_2)^2 - 3x_2^2 \), a perfect square plus a leftover, and the substitution \( y_1 = x_1 + 2x_2 \), \( y_2 = x_2 \) — that is, \( \x = \P\y \) — is what completing the square asks for. A later section turns this into a theorem and an algorithm.
:::

## Congruent matrices

Every invertible \( \P \) is a change-of-coordinates matrix between some pair of bases (@prp-invertible-matrix-change-of-basis), so @thm-change-of-basis-form says exactly this: the matrices of one form, over all bases, are the matrices \( \P\tp\A\P \) with \( \P \) invertible. That set deserves a name, and the name is the organizing idea of the chapter.

*Two matrices are congruent when they record the same form in two bases.*

::: {#def-congruent}
[Congruent Matrices]

Let \( \A, \B \in M_n(F) \). We say \( \A \) is **congruent** to \( \B \), written \( \A \simeq \B \), if there **exists** an **invertible** \( \P \in M_n(F) \) such that
\[
\B = \P\tp\A\P .
\]
:::

In words: congruence allows one matrix to be sandwiched by an invertible matrix and its transpose. The word **invertible** is essential; without it, \( \A \mapsto \P\tp\A\P \) with \( \P = 0 \) would relate everything to \( 0 \). The **transpose**, not the inverse, is what distinguishes the relation from similarity (@def-similar-matrices), and the symbol \( \simeq \) is chosen to sit near \( \sim \) without being it.

Three immediate readings. First, by @thm-change-of-basis-form, \( \A \simeq \B \) if and only if \( \A \) and \( \B \) are the matrices of a single bilinear form in two bases. Second, in the language of quadratic expressions on \( F^n \), \( \A \simeq \B \) says that the substitution \( \x = \P\y \) turns \( \x\tp\A\x \) into \( \y\tp\B\y \): congruence is invertible change of variables in a quadratic expression. Third, over \( \nR \) it is the relation \( \A \mapsto \S^{*}\A\S \) of Chapter 12, because there the star is the transpose.

::: {#exm-congruence-first}
[Congruences and a non-congruence]

::: {.enumerate options="label=(\alph*)"}
1. \( \I_2 \simeq \begin{psmallmatrix} 1 & 1 \\ 1 & 2\end{psmallmatrix} \) over any field.
2. \( \I_2 \simeq \diag(4, 1) \) over \( \nQ \).
3. \( \A \simeq \A \) for every \( \A \).
4. \( \I_2 \not\simeq \begin{psmallmatrix} 1 & 1 \\ 0 & 1\end{psmallmatrix} \) over any field.
:::
:::

::: {.solution}
(a) Take \( \P = \begin{psmallmatrix} 1 & 1 \\ 0 & 1\end{psmallmatrix} \), which is invertible with determinant \( 1 \). Then \( \P\tp\I_2\P = \P\tp\P = \begin{psmallmatrix} 1 & 1 \\ 1 & 2\end{psmallmatrix} \).

(b) Take \( \P = \diag(2, 1) \), invertible over \( \nQ \). Then \( \P\tp\I_2\P = \diag(4, 1) \). Scaling a basis vector by \( c \) scales the corresponding diagonal entry by \( c^2 \), which is the single most useful congruence to have in mind.

(c) Take \( \P = \I_n \).

(d) Suppose \( \begin{psmallmatrix} 1 & 1 \\ 0 & 1\end{psmallmatrix} = \P\tp\I_2\P = \P\tp\P \) for some \( \P \). Then, by @thm-transpose-properties, \( (\P\tp\P)\tp = \P\tp\P \), so the matrix would be symmetric; it is not. This is the non-example by minimal change: one entry of \( \begin{psmallmatrix} 1 & 1 \\ 1 & 2\end{psmallmatrix} \) in (a) is altered, and congruence to \( \I_2 \) is lost — not for a subtle reason, but because the altered matrix is not the matrix of a symmetric form in any basis. The general statement is @prp-congruence-preserves-symmetry below.
:::

Before using the word "congruent" in both directions, we owe the usual check.

::: {#prp-congruence-equivalence}
[Congruence is an equivalence relation]

Congruence is an equivalence relation on \( M_n(F) \) (@def-equivalence-relation).
:::

::: {.proof}
*Reflexive:* \( \A = \I_n\tp\A\I_n \).

*Symmetric:* suppose \( \B = \P\tp\A\P \) with \( \P \) invertible, and put \( \Q = \P^{-1} \), which is invertible. By @thm-transpose-properties (d), \( \Q\tp\P\tp = (\P\Q)\tp = \I_n\tp = \I_n \), so
\[
\Q\tp\B\Q = \bigl(\Q\tp\P\tp\bigr)\A\bigl(\P\Q\bigr) = \I_n\A\I_n = \A .
\]

*Transitive:* if \( \B = \P\tp\A\P \) and \( \C = \Q\tp\B\Q \) with \( \P, \Q \) invertible, then \( \P\Q \) is invertible and \( \C = \Q\tp\P\tp\A\P\Q = (\P\Q)\tp\A(\P\Q) \). This proves the proposition.
:::

So the matrices in \( M_n(F) \) fall into congruence classes, and the classification problem of this chapter is to describe them. The rest of the section collects the tools for telling classes apart.

## What congruence preserves

Three invariants come out of the definition with almost no work. The first is the rank, which we already know is the co-dimension of the radical (@prp-nondegenerate-iff-invertible).

::: {#thm-congruence-preserves-rank}
[Congruence preserves rank]

Let \( \A, \B \in M_n(F) \) with \( \A \simeq \B \). Then \( \rank\A = \rank\B \). Consequently, whether the associated form is non-degenerate is a property of the congruence class, and it is legitimate to speak of the **rank of a bilinear form**, meaning the rank of its matrix in any basis.
:::

::: {.proof}
Write \( \B = \P\tp\A\P \) with \( \P \) invertible. Then \( \P\tp \) is invertible, with inverse \( (\P^{-1})\tp \) (@thm-transpose-properties). Multiplying by invertible matrices on either side does not change the rank (@thm-rank-product-inequality), so \( \rank\B = \rank(\A\P) = \rank\A \). Non-degeneracy is the condition \( \rank\A = n \) by @prp-nondegenerate-iff-invertible (c), so it too depends only on the class. The last sentence follows because, by @thm-change-of-basis-form, any two matrices of one form are congruent.
:::

The second invariant is the symmetry type. Here "alternating" is used in the matrix sense that @def-alternating-form suggests: a **zero diagonal** on top of skew-symmetry. The next section separates the three conditions carefully; for now we only need that congruence respects each of them.

::: {#prp-congruence-preserves-symmetry}
[Congruence preserves the symmetry type]

Let \( \A, \B \in M_n(F) \) with \( \B = \P\tp\A\P \) for an invertible \( \P \).

::: {.enumerate options="label=(\alph*)"}
1. If \( \A\tp = \A \), then \( \B\tp = \B \).
2. If \( \A\tp = -\A \), then \( \B\tp = -\B \).
3. If \( \A\tp = -\A \) and every diagonal entry of \( \A \) is \( 0 \), the same holds for \( \B \).
:::

Each implication is an equivalence, since congruence is symmetric (@prp-congruence-equivalence).
:::

::: {.proof}
By @thm-transpose-properties, \( \B\tp = (\P\tp\A\P)\tp = \P\tp\A\tp\P \).

(a) If \( \A\tp = \A \), this is \( \P\tp\A\P = \B \).

(b) If \( \A\tp = -\A \), it is \( \P\tp(-\A)\P = -\B \).

(c) Assume the hypothesis of (c). Then \( \B \) is skew-symmetric by (b), so only the diagonal is left to check. For any \( \x \in F^n \), grouping the terms of the double sum in pairs,
\[
\x\tp\A\x = \sum_{i<j}(a_{ij} + a_{ji})x_ix_j + \sum_i a_{ii}x_i^2 = 0 ,
\]
since \( a_{ij} + a_{ji} = 0 \) by skew-symmetry and \( a_{ii} = 0 \) by hypothesis. Writing \( \p_1, \dots, \p_n \) for the columns of \( \P \), the \( i \)-th diagonal entry of \( \B = \P\tp\A\P \) is \( b_{ii} = \e_i\tp\P\tp\A\P\e_i = \p_i\tp\A\p_i \), which is \( 0 \) by the display. This proves the proposition.
:::

The third invariant is the determinant, but only in a weakened sense: congruence multiplies it by a square.

::: {#thm-congruence-determinant-class}
[Congruence changes the determinant by a square]

Let \( \A, \B \in M_n(F) \) with \( \B = \P\tp\A\P \) for an invertible \( \P \). Then
\[
\det\B = (\det\P)^2\,\det\A ,
\]
with \( \det\P \ne 0 \). In particular \( \det\A = 0 \) if and only if \( \det\B = 0 \), and when they are non-zero, \( \det\B = c^2\det\A \) for some \( c \in F \setminus\{0\} \).
:::

::: {.proof}
By @thm-det-multiplicative and @thm-det-transpose,
\[
\det\B = \det(\P\tp)\det\A\det\P = (\det\P)^2\det\A .
\]
Since \( \P \) is invertible, \( \det\P \ne 0 \) (@thm-det-nonzero-iff-invertible), so \( (\det\P)^2 \ne 0 \) and the two determinants vanish together. Taking \( c = \det\P \) gives the last claim.
:::

The determinant itself is therefore **not** a congruence invariant — @exm-congruence-first (b) moved it from \( 1 \) to \( 4 \). What is invariant is the determinant read modulo squares. Write \( F^{\times} = F \setminus\{0\} \), and for \( a, b \in F^{\times} \) declare \( a \) and \( b \) equivalent when \( a = c^2b \) for some \( c \in F^{\times} \). This is an equivalence relation on \( F^{\times} \) (@def-equivalence-relation): it is reflexive with \( c = 1 \), symmetric with \( c^{-1} \), and transitive by multiplying the two scalars. Its classes are called **square classes**, and the set of them is commonly written \( F^{\times}/(F^{\times})^2 \).

::: {#def-discriminant}
[Discriminant]

Let \( \beta \) be a **non-degenerate** bilinear form on an \( n \)-dimensional \( V \). The **discriminant** of \( \beta \) is the square class of \( \det\mtx{\beta}{\sB}{} \) in \( F^{\times} \), for any ordered basis \( \sB \) of \( V \).
:::

This is well defined by @thm-congruence-determinant-class and @thm-change-of-basis-form: another basis changes the determinant by the square \( (\det\P)^2 \), hence not its class. The discriminant is coarse but genuinely useful, and how much it sees depends entirely on the field. Over \( \nC \) every non-zero number is a square, so there is only one class and the discriminant says nothing. Over \( \nR \) there are two, \( \{t > 0\} \) and \( \{t < 0\} \), so the discriminant records one bit: the sign of the determinant. Over \( \nQ \) there are infinitely many, and the discriminant is a strong invariant.

::: {.check}
Over \( \nR \), are \( \diag(1, 1) \) and \( \diag(-1, -1) \) distinguished by their discriminants?
:::

::: {.solution}
No. Both determinants equal \( 1 \), so the discriminants agree. And yet the two matrices are not congruent over \( \nR \). Suppose \( \diag(-1,-1) = \P\tp\I_2\P = \P\tp\P \) for an invertible \( \P \). Evaluating both sides on \( \x = \e_1 \) gives
\[
-1 = \e_1\tp\diag(-1,-1)\e_1 = \e_1\tp\P\tp\P\e_1 = \norm{\P\e_1}^2 \ge 0 ,
\]
a contradiction. So the discriminant is not a complete invariant, even over \( \nR \) and even for \( 2 \times 2 \) matrices. Proving that the full "sign pattern" *is* an invariant, and that it is the complete one over \( \nR \), is the law of inertia, proved later in this chapter.
:::

## What congruence destroys

Now the negative result of the section, and the reason the previous three chapters could not have been this one.

::: {#exm-congruent-different-eigenvalues}
[Congruent, with no eigenvalue in common]

::: {.enumerate options="label=(\alph*)"}
1. \( \I_2 \simeq \begin{psmallmatrix} 1 & 1 \\ 1 & 2\end{psmallmatrix} \) by @exm-congruence-first (a). Compare their eigenvalues.
2. \( \begin{psmallmatrix} 1 & 2 \\ 2 & 1\end{psmallmatrix} \simeq \diag(1, -3) \) by @exm-form-in-a-new-basis. Compare their eigenvalues.
:::
:::

::: {.solution}
(a) \( \I_2 \) has the single eigenvalue \( 1 \), twice. The characteristic polynomial of \( \begin{psmallmatrix} 1 & 1 \\ 1 & 2\end{psmallmatrix} \) is \( x^2 - 3x + 1 \), whose roots are \( (3 \pm \sqrt5)/2 \), that is, approximately \( 2.618 \) and \( 0.382 \). The two matrices share no eigenvalue. They do share a rank, \( 2 \); a symmetry type, symmetric; and a discriminant, since \( \det = 1 \) for both.

(b) The characteristic polynomial of \( \begin{psmallmatrix} 1 & 2 \\ 2 & 1\end{psmallmatrix} \) is \( x^2 - 2x - 3 = (x-3)(x+1) \), so its eigenvalues are \( 3 \) and \( -1 \). Those of \( \diag(1,-3) \) are \( 1 \) and \( -3 \). Again no eigenvalue in common — but this time one positive and one negative on each side, and the determinants are \( -3 \) both times. The signs survived; the numbers did not. That is the pattern the law of inertia will explain.
:::

Chapter 12 introduced this operation twice and both times deferred it to here. Section 1 of that chapter wrote that "the operation \( \A \mapsto \S^{*}\A\S \) is called **congruence**, and Chapter 13 studies it for its own sake", keeping only that it preserves the sign of a positive form (@prp-congruence-positivity). Section 4 repeated the promise in fuller form: "Chapter 13 studies congruence in its own right, including what it does preserve; for now, note that it certainly does **not** preserve eigenvalues, since \( \S^{*}\I\S = \S^{*}\S \) can be any positive definite matrix at all."

Both debts are now paid, and it is worth saying the answer in one place. **What congruence preserves:** the rank (@thm-congruence-preserves-rank), and with it non-degeneracy and the dimension of the radical; the symmetry type (@prp-congruence-preserves-symmetry); and the square class of the determinant when that is non-zero (@thm-congruence-determinant-class), the discriminant. Over \( \nR \) it preserves one thing more, the triple of signs, and that is the deepest of the four; it is proved in the section on inertia. **What congruence destroys:** the eigenvalues, and therefore the characteristic polynomial, the trace and the determinant itself. Not every similarity invariant is lost — rank and invertibility, parts (a) and (b) of @prp-similarity-invariants, survive both relations — but every invariant that reads the eigenvalues is. Chapter 12's parenthetical remark is exactly right and can be made sharper: taking \( \A = \I_n \) in @def-congruent, the congruence class of \( \I_n \) over \( \nR \) is the set of all matrices \( \P\tp\P \) with \( \P \) invertible, which by @thm-pd-characterizations (c) is the set of **all** positive definite matrices. One class, every spectrum with all eigenvalues positive.

::: {.warning}
**Congruent and similar are different relations, and neither implies the other.** By @exm-congruent-different-eigenvalues (a), \( \I_2 \simeq \begin{psmallmatrix} 1 & 1 \\ 1 & 2\end{psmallmatrix} \), while the only matrix similar to \( \I_2 \) is \( \I_2 \) itself, since \( \P^{-1}\I_2\P = \I_2 \) for every invertible \( \P \). In the other direction, \( \diag(1,2) \) is similar to \( \begin{psmallmatrix} 1 & -1 \\ 0 & 2\end{psmallmatrix} \) — conjugate by \( \begin{psmallmatrix} 1 & 1 \\ 0 & 1\end{psmallmatrix} \) — but not congruent to it, because \( \diag(1,2) \) is symmetric and the other matrix is not (@prp-congruence-preserves-symmetry). So do not carry any habit across. In particular, "diagonalizable" means two different things in this chapter, and a matrix that is diagonalizable by congruence need not be diagonalizable by similarity, nor conversely.
:::

## Where the two relations meet

There is exactly one situation in which the confusion is harmless: when the change-of-basis matrix satisfies \( \P\tp = \P^{-1} \), that is, when \( \P \) is orthogonal (@def-unitary-orthogonal-groups).

::: {#prp-orthogonal-congruence-similarity}
[An orthogonal change of basis is both]

Let \( \A \in M_n(\nR) \) and \( \Q \in \Orth(n) \). Then \( \Q\tp\A\Q = \Q^{-1}\A\Q \), so this matrix is at once congruent and similar to \( \A \). Consequently, if \( \A \) is symmetric, then \( \A \) is congruent to the diagonal matrix \( \D \) of its eigenvalues, listed with multiplicity in any prescribed order.
:::

::: {.proof}
The first statement is the definition of an orthogonal matrix, \( \Q\tp\Q = \I_n \), which gives \( \Q\tp = \Q^{-1} \); the matrix \( \Q\tp\A\Q \) is then congruent to \( \A \) by @def-congruent, since \( \Q \) is invertible, and similar to \( \A \) by @def-similar-matrices.

For the second statement, let \( \A \) be symmetric. By @cor-spectral-real-matrix there are \( \Q \in \Orth(n) \) and a real diagonal \( \D \), carrying the eigenvalues of \( \A \) in any prescribed order, with \( \A = \Q\D\Q\tp \). Multiplying on the left by \( \Q\tp \) and on the right by \( \Q \) gives \( \D = \Q\tp\A\Q \), which is a congruence. This proves the proposition.
:::

This is why the real spectral theorem is so strong, and it is what Chapter 11 meant when it said, of the principal axis theorem, that "an orthogonal change of variables is a similarity *and* a congruence, so it keeps the eigenvalues and the geometry at once". The general theory of this chapter has no orthogonal matrices to call on — a general field has no inner product, hence no orthogonal group in that sense — so the two relations part company and only congruence remains. What @prp-orthogonal-congruence-similarity gives over \( \nR \) is a bridge: it says that every real symmetric matrix is congruent to a diagonal matrix, and it identifies the diagonal entries as eigenvalues. The section on inertia will show that the entries are free to move but their signs are not, which is how the two pictures are finally reconciled.

::: {.check}
Over \( \nR \), which matrices are congruent to \( \I_n \)?
:::

::: {.solution}
Exactly the positive definite symmetric matrices. If \( \B = \P\tp\I_n\P = \P\tp\P \) with \( \P \) invertible, then \( \B \) is symmetric and \( \x\tp\B\x = \norm{\P\x}^2 > 0 \) for \( \x \ne \0 \), since \( \P\x \ne \0 \). Conversely every positive definite \( \B \) is \( \P\tp\P \) for an invertible \( \P \) by @thm-pd-characterizations. Compare the similarity class of \( \I_n \), which contains \( \I_n \) alone: one relation collapses this class to a point, the other spreads it over every positive definite matrix there is.
:::

## Exercises

### A. Check your understanding

::: {#exr-congruence-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the change-of-basis rule for the matrix of a bilinear form, saying which matrix \( \P \) appears.
2. Define what it means for \( \A, \B \in M_n(F) \) to be congruent.
3. For each of rank, symmetry, determinant, eigenvalues and the square class of a non-zero determinant, say whether it is a congruence invariant.
4. Determine whether the following is correct, with a reason: congruent matrices are similar.
5. State the one circumstance in which a change of basis is simultaneously a similarity and a congruence.
:::
:::

::: {.solution}
(a) @thm-change-of-basis-form: \( \mtx{\beta}{\sB'}{} = \P\tp\mtx{\beta}{\sB}{}\P \), where \( \P = \mtx{\id}{\sB'}{\sB} \) is the change-of-coordinates matrix from the new basis to the old one.

(b) @def-congruent: \( \B = \P\tp\A\P \) for some invertible \( \P \in M_n(F) \).

(c) Invariant: rank (@thm-congruence-preserves-rank); symmetry (@prp-congruence-preserves-symmetry); the square class of a non-zero determinant (@thm-congruence-determinant-class). Not invariant: the determinant itself, and the eigenvalues (@exm-congruent-different-eigenvalues).

(d) Incorrect. \( \I_2 \simeq \begin{psmallmatrix} 1 & 1 \\ 1 & 2\end{psmallmatrix} \), but the only matrix similar to \( \I_2 \) is \( \I_2 \).

(e) When the change-of-coordinates matrix \( \P \) satisfies \( \P\tp = \P^{-1} \), that is, when \( \P \) is orthogonal (@prp-orthogonal-congruence-similarity).
:::

### B. Practice

::: {#exr-congruence-b1}
[B1: A congruence in \( \nQ \)]

Let \( \A = \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix} \) and \( \P = \begin{psmallmatrix} 1 & 1 \\ 1 & -1 \end{psmallmatrix} \), both over \( \nQ \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \P\tp\A\P \), and hence write down a matrix congruent to \( \A \) that is diagonal.
2. Find the eigenvalues of both matrices and compare them.
3. Compute the discriminant of the form \( \x\tp\A\y \) and check that it agrees for the two matrices.
:::
:::

::: {.solution}
(a) \( \P \) is invertible, with \( \det\P = -2 \ne 0 \). Then
\[
\A\P = \begin{pmatrix} 1 & -1 \\ 1 & 1\end{pmatrix},
\qquad
\P\tp\A\P = \begin{pmatrix} 2 & 0 \\ 0 & -2\end{pmatrix}.
\]
So \( \A \simeq \diag(2, -2) \) over \( \nQ \).

(b) The characteristic polynomial of \( \A \) is \( x^2 - 1 \), so its eigenvalues are \( 1 \) and \( -1 \); those of \( \diag(2,-2) \) are \( 2 \) and \( -2 \). No eigenvalue is shared, and each matrix has one positive and one negative eigenvalue.

(c) \( \det\A = -1 \) and \( \det\diag(2,-2) = -4 = (-2)^2 \cdot (-1) \), which is the relation \( \det\B = (\det\P)^2\det\A \) of @thm-congruence-determinant-class. The two determinants differ by the square \( 4 \), so they lie in the same square class of \( \nQ^{\times} \) and the discriminants agree, as @def-discriminant requires.
:::

::: {#exr-congruence-b2}
[B2: A non-congruence over \( \nQ \)]

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \diag(1,1) \) and \( \diag(1,2) \) are **not** congruent over \( \nQ \).
2. Prove that they **are** congruent over \( \nR \), by exhibiting \( \P \).
3. Explain in one sentence why (a) and (b) are consistent.
:::
:::

::: {.solution}
(a) Suppose \( \diag(1,2) = \P\tp\diag(1,1)\P \) with \( \P \in M_2(\nQ) \) invertible. By @thm-congruence-determinant-class, \( 2 = (\det\P)^2 \cdot 1 \), so \( \det\P \in \nQ \) would satisfy \( (\det\P)^2 = 2 \). No rational number squares to \( 2 \) (@thm-sqrt2-irrational), a contradiction. Hence the two are not congruent over \( \nQ \).

(b) Take \( \P = \diag(1, 1/\sqrt2) \), which is invertible over \( \nR \). Then \( \P\tp\diag(1,2)\P = \diag(1, 1) \), and congruence is symmetric (@prp-congruence-equivalence).

(c) Congruence is a relation **over a specified field**: the matrix \( \P \) is required to have entries in that field, and \( 1/\sqrt2 \) is available in \( \nR \) but not in \( \nQ \). Equivalently, \( 2 \) is a square in \( \nR^{\times} \) and not in \( \nQ^{\times} \), so the discriminant separates the two matrices over \( \nQ \) and not over \( \nR \).
:::

::: {#exr-congruence-b3}
[B3: Completing the square, again]

On \( \nR^2 \), let \( \beta(\x, \y) = x_1y_1 - x_1y_2 - x_2y_1 + 2x_2y_2 \).

::: {.enumerate options="label=(\alph*)"}
1. Write down \( \A = \mtx{\beta}{\sE}{} \) and expand \( q(\x) = \beta(\x, \x) \) as a polynomial in \( x_1, x_2 \).
2. Complete the square to find a basis \( \sB' \) with \( \mtx{\beta}{\sB'}{} = \I_2 \). Verify by computing \( \P\tp\A\P \).
3. Hence find the eigenvalues of \( \A \) and compare them with those of \( \I_2 \).
:::
:::

::: {.solution}
(a) \( \A = \begin{psmallmatrix} 1 & -1 \\ -1 & 2\end{psmallmatrix} \), and \( q(\x) = x_1^2 - 2x_1x_2 + 2x_2^2 \).

(b) \( q(\x) = (x_1 - x_2)^2 + x_2^2 \). So the substitution \( y_1 = x_1 - x_2 \), \( y_2 = x_2 \), that is \( x_1 = y_1 + y_2 \) and \( x_2 = y_2 \), makes \( q = y_1^2 + y_2^2 \). This is \( \x = \P\y \) with
\[
\P = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix},
\qquad
\A\P = \begin{pmatrix} 1 & 0 \\ -1 & 1\end{pmatrix},
\qquad
\P\tp\A\P = \I_2 .
\]
By @thm-change-of-basis-form the basis is \( \sB' = \bigl((1,0),\ (1,1)\bigr) \), the columns of \( \P \).

(c) The characteristic polynomial of \( \A \) is \( x^2 - 3x + 1 \), with roots \( (3 \pm \sqrt5)/2 \); \( \I_2 \) has the eigenvalue \( 1 \) twice. The two matrices are congruent with no eigenvalue in common. What they share is that all eigenvalues are positive on both sides, which by the check above is no accident: the congruence class of \( \I_2 \) over \( \nR \) consists of exactly the positive definite matrices.
:::

### C. Going deeper

::: {#exr-congruence-c1}
[C1: Congruence versus equivalence]

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( \A \simeq \B \) then \( \A \) and \( \B \) are equivalent in the sense of @def-equivalent-matrices.
2. Give two matrices in \( M_2(\nQ) \) that are equivalent but not congruent, and justify your example.
3. Hence explain what "the congruence classes refine the equivalence classes" means, and say what extra information a congruence class carries that a rank does not.
:::
:::

::: {.solution}
(a) If \( \B = \P\tp\A\P \) with \( \P \) invertible, then \( \P\tp \) is invertible (@thm-transpose-properties), so \( \B = \Q\A\P \) with \( \Q = \P\tp \) and \( \P \) both invertible, which is @def-equivalent-matrices.

(b) Take \( \diag(1,1) \) and \( \diag(1,2) \). Both have rank \( 2 \), so they are equivalent by @thm-rank-normal-form (c). They are not congruent over \( \nQ \) by @exr-congruence-b2 (a).

(c) By (a), each congruence class lies inside a single equivalence class, and by (b) an equivalence class may split into more than one congruence class; that is what "refine" means. An equivalence class is named by the rank alone (@thm-rank-normal-form (c)). A congruence class remembers the rank, and in addition the symmetry type and the discriminant — and over \( \nR \), the signs. Equivalence allows two independent changes of basis, one in each slot; congruence allows only one, used twice, and the extra invariants are the price of that constraint.
:::

::: {#exr-congruence-c2}
[C2: Orthogonal congruence]

Let \( \A \in M_n(\nR) \) be symmetric with eigenvalues \( \lambda_1, \dots, \lambda_n \), listed with multiplicity.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \A \simeq \diag(\lambda_1, \dots, \lambda_n) \).
2. Deduce that if every \( \lambda_i \) is non-zero, then \( \A \) is congruent to a diagonal matrix all of whose entries are \( \pm1 \).
3. Give two real symmetric \( 2 \times 2 \) matrices that are congruent and have no eigenvalue in common.
:::

*Hint for (b): recall from @exm-congruence-first (b) what scaling a basis vector does to a diagonal entry.*
:::

::: {.solution}
(a) This is @prp-orthogonal-congruence-similarity: by @cor-spectral-real-matrix there is \( \Q \in \Orth(n) \) with \( \Q\tp\A\Q = \D = \diag(\lambda_1, \dots, \lambda_n) \), and \( \Q \) is invertible, so \( \A \simeq \D \).

(b) Let \( \S = \diag(c_1, \dots, c_n) \) with \( c_i = 1/\sqrt{\lvert\lambda_i\rvert} \), which is defined and non-zero because \( \lambda_i \ne 0 \). Then \( \S \) is invertible and \( \S\tp\D\S = \diag(c_1^2\lambda_1, \dots, c_n^2\lambda_n) \), whose \( i \)-th entry is \( \lambda_i/\lvert\lambda_i\rvert = \pm1 \) according to the sign of \( \lambda_i \). By (a) and transitivity (@prp-congruence-equivalence), \( \A \) is congruent to that matrix.

(c) By (b), \( \diag(1, -3) \) and \( \diag(2, -1) \) are both congruent to \( \diag(1,-1) \), hence to each other by @prp-congruence-equivalence; explicitly, \( \P = \diag(\sqrt2, 1/\sqrt3) \) gives \( \P\tp\diag(1,-3)\P = \diag(2,-1) \). Their eigenvalues are \( \{1, -3\} \) and \( \{2, -1\} \), which are disjoint. Note that the **signs** match, one positive and one negative on each side; part (b) is the reason, and the law of inertia will say it is forced.
:::

::: {#exr-congruence-c3}
[C3: How much the discriminant sees]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \nC^{\times} \) has exactly one square class, and that \( \nR^{\times} \) has exactly two.
2. List the squares in \( \nF_5^{\times} \) and show that \( \nF_5^{\times} \) has exactly two square classes.
3. Hence determine, for each of \( \nC \), \( \nR \) and \( \nF_5 \), the largest number of pairwise non-congruent invertible matrices in \( M_n \) that the discriminant alone can distinguish.
:::
:::

::: {.solution}
(a) Over \( \nC \), every \( a \ne 0 \) has a square root (@exm-complex-square-root), so \( a = c^2 \cdot 1 \) and every element is equivalent to \( 1 \): one class. Over \( \nR \), squares of non-zero reals are exactly the positive reals, so \( a \) and \( b \) are equivalent precisely when \( a/b > 0 \), which happens exactly when they have the same sign. The classes are the positive reals and the negative reals: two classes, and they are distinct since \( 1 \) and \( -1 \) are not related.

(b) The squares are \( 1^2 = 1 \), \( 2^2 = 4 \), \( 3^2 = 4 \), \( 4^2 = 1 \), so the set of non-zero squares is \( \{1, 4\} \). Multiplying \( \{1,4\} \) by \( 2 \) gives \( \{2, 3\} \), so the classes are \( \{1, 4\} \) and \( \{2, 3\} \): two classes, each of size \( 2 \), covering all four elements of \( \nF_5^{\times} \).

(c) The discriminant takes one value per square class, so it can separate at most as many classes as there are square classes: one over \( \nC \), two over \( \nR \) and two over \( \nF_5 \). Over \( \nC \) it is therefore useless, and over \( \nR \) and \( \nF_5 \) it sorts invertible matrices into at most two piles. By @exr-congruence-c2 (b), over \( \nR \) every invertible symmetric matrix is congruent to one of the \( n + 1 \) matrices \( \I_p \oplus -\I_{n-p} \), whose determinant is \( (-1)^{n-p} \); so the discriminant sees only the parity of \( n - p \), and for \( n \ge 2 \) it cannot separate, say, \( \I_2 \) from \( -\I_2 \). That the \( n+1 \) matrices really are pairwise non-congruent is the law of inertia, not anything the discriminant can deliver.
:::
