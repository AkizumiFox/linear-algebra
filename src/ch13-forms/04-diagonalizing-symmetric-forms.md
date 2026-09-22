# Completing the Square

Every symmetric matrix over \( \nR \) can be diagonalized by an orthogonal matrix, which is Chapter 11's spectral theorem. That theorem needs \( \nR \), an inner product and the existence of eigenvalues. This section proves a weaker conclusion under far weaker hypotheses: over **any** field of characteristic \( \ne 2 \), with no inner product, no order and no eigenvalues available, every symmetric form still becomes diagonal after a change of basis — provided we ask only for congruence, not for similarity. The proof is one algebraic manipulation, completing the square, run by induction; and the induction has a case that a careless proof loses.

Throughout, \( F \) is a field with \( \operatorname{char} F \ne 2 \) (@def-characteristic), \( V \) is a finite-dimensional vector space over \( F \), \( \beta \) is a **symmetric** bilinear form on \( V \) (@def-symmetric-form), and \( q(\v) = \beta(\v,\v) \) is its quadratic form (@def-quadratic-form).

## Orthogonality without an inner product

Chapter 10 called two vectors orthogonal when their inner product vanished. The word survives the loss of positivity unchanged, because only the vanishing was ever used.

::: {#def-orthogonal-basis-form}
[Orthogonal Basis for a Form]

Let \( \beta \) be a bilinear form on \( V \). Vectors \( \u, \v \in V \) are **orthogonal with respect to \( \beta \)** if \( \beta(\u,\v) = 0 \). An ordered basis \( \sB = (\v_1, \dots, \v_n) \) of \( V \) is an **orthogonal basis for \( \beta \)** if
\[
\beta(\v_i, \v_j) = 0 \qquad \text{whenever } i \ne j .
\]
:::

The definition is engineered to say exactly one thing about matrices: by @def-form-matrix, \( \sB \) is an orthogonal basis for \( \beta \) precisely when \( \mtx{\beta}{\sB}{\sB} \) is a **diagonal** matrix, with \( q(\v_1), \dots, q(\v_n) \) down the diagonal. Two warnings come free. The vectors of such a basis are not required to satisfy \( q(\v_i) = 1 \), and over a general field they usually cannot be rescaled to. And a vector may be orthogonal to itself: \( q(\v_i) = 0 \) is allowed, and for a degenerate form it is unavoidable.

What an orthogonal basis buys is that \( q \) becomes a sum of squares with no cross terms. If \( \v = c_1\v_1 + \dots + c_n\v_n \) and \( d_i = q(\v_i) \), then expanding by bilinearity and deleting the \( i \ne j \) terms,

\[
q(\v) = \sum_{i=1}^{n} d_i\,c_i^2 .
\]{#eq-diagonal-quadratic-form}

That is the "sum of squares" a reader has met when completing the square in two variables, and @eq-diagonal-quadratic-form is the reason the whole section is called what it is.

## The theorem, and the case that breaks it

Here is the naive argument, and it is worth seeing it fail. To make \( q(\v) = ax_1^2 + 2bx_1x_2 + cx_2^2 \) into a sum of squares, write
\[
q = a\Bigl(x_1 + \frac{b}{a}x_2\Bigr)^{2} + \Bigl(c - \frac{b^2}{a}\Bigr)x_2^2 ,
\]
which is exactly a change of variable. The step divides by \( a = q(\e_1) \). If \( a = 0 \) there is nothing to complete, and one may hope to start with \( x_2 \) instead — but \( q(\x) = 2x_1x_2 \) has \( q(\e_1) = q(\e_2) = 0 \), and neither variable offers a foothold. The repair is to change the vector, not the variable: \( q(\e_1 + \e_2) = 2 \ne 0 \). That repair is a lemma, and it is where \( \operatorname{char} F \ne 2 \) is spent.

::: {#lem-anisotropic-vector-exists}
[A Non-Zero Form Is Non-Zero Somewhere on the Diagonal]

Let \( \operatorname{char} F \ne 2 \) and let \( \beta \) be a symmetric bilinear form on \( V \) with \( \beta \ne 0 \). Then there exists \( \v \in V \) with \( q(\v) \ne 0 \).
:::

::: {.proof}
Since \( \beta \ne 0 \), there are \( \u, \w \in V \) with \( a = \beta(\u,\w) \ne 0 \). If \( q(\u) \ne 0 \) or \( q(\w) \ne 0 \) we are done. So suppose \( q(\u) = q(\w) = 0 \). Expanding by bilinearity and using symmetry,
\[
q(\u + \w) = q(\u) + 2\beta(\u,\w) + q(\w) = (1+1)a .
\]
Since \( \operatorname{char} F \ne 2 \), the element \( 1 + 1 \) is non-zero, and a product of two non-zero elements of a field is non-zero, so \( q(\u+\w) \ne 0 \). This proves the lemma.
:::

Contrapositively: if \( q \) vanishes identically then \( \beta = 0 \). That is the case the induction must handle separately, and the lemma is what lets it be handled in one line.

::: {#thm-symmetric-form-diagonalizable}
[Diagonalization of a Symmetric Form]

Let \( F \) be a field with \( \operatorname{char} F \ne 2 \), let \( V \) be a finite-dimensional vector space over \( F \), and let \( \beta \) be a symmetric bilinear form on \( V \). Then \( V \) has an orthogonal basis for \( \beta \).

Equivalently: every symmetric \( \A \in M_n(F) \) is congruent to a diagonal matrix, that is, there is an invertible \( \P \in M_n(F) \) with \( \P\tp\A\P \) diagonal.
:::

::: {.idea}
Induction on \( \dim V \). The step wants to peel off one basis vector and recurse on a complement, exactly as "peel off an eigenvector" does in Chapter 8 — but the complement here is the set of vectors orthogonal to the chosen one, not an invariant subspace, and it is available only if the chosen \( \v_1 \) has \( q(\v_1) \ne 0 \). So the proof splits into two steps: ① if \( q \) vanishes everywhere, the form is zero and **every** basis is orthogonal; ② otherwise @lem-anisotropic-vector-exists supplies a \( \v_1 \) with \( q(\v_1) \ne 0 \), the linear functional \( \w \mapsto \beta(\v_1,\w) \) is non-zero, its kernel \( W \) is a hyperplane meeting \( \Span(\v_1) \) trivially, and the induction hypothesis applies to \( \beta \) restricted to \( W \). Step ① is not a formality: without it the argument has no base for the recursion when the form degenerates, and the word "equivalently" in the statement would be unearned.
:::

::: {.proof}
We induct on \( n = \dim V \). If \( n = 0 \) the empty basis is orthogonal, vacuously; if \( n = 1 \) any basis \( (\v_1) \) is orthogonal, since there is no pair \( i \ne j \). Let \( n \ge 2 \) and suppose the result holds for all spaces of dimension \( n - 1 \) over \( F \).

**Step 1: the form vanishes on the diagonal.** Suppose \( q(\v) = 0 \) for every \( \v \in V \). By @lem-anisotropic-vector-exists, read contrapositively, \( \beta = 0 \). Then \( \beta(\v_i,\v_j) = 0 \) for every pair of vectors whatsoever, so **any** basis of \( V \) is an orthogonal basis for \( \beta \), and its matrix is \( \0 \), which is diagonal.

**Step 2: the form does not vanish on the diagonal.** Otherwise there is \( \v_1 \in V \) with \( c = q(\v_1) \ne 0 \); in particular \( \v_1 \ne \0 \). Define
\[
\varphi \colon V \to F, \qquad \varphi(\w) = \beta(\v_1, \w) .
\]
Then \( \varphi \) is linear, because \( \beta \) is linear in its second argument, and \( \varphi(\v_1) = c \ne 0 \), so \( \varphi \ne 0 \). A non-zero functional is surjective onto \( F \) (@prp-nonzero-functional-surjective), so \( \rank\varphi = 1 \) and, by the Rank–Nullity Theorem (@thm-rank-nullity), \( W = \ker\varphi \) has \( \dim W = n - 1 \).

Moreover \( \Span(\v_1) \cap W = \{\0\} \): if \( a\v_1 \in W \) then \( 0 = \varphi(a\v_1) = ac \), and \( c \ne 0 \) forces \( a = 0 \). So the sum \( \Span(\v_1) + W \) is direct, and \( \dim(\Span(\v_1) + W) = 1 + (n-1) = n \), both by @thm-direct-sum-criteria. A subspace of \( V \) of dimension \( \dim V \) is all of \( V \) (@thm-dim-impl-eq), so
\[
V = \Span(\v_1) \oplus W .
\]

The restriction of \( \beta \) to \( W \times W \) is a bilinear form on \( W \), and it is symmetric because \( \beta \) is. As \( \dim W = n - 1 \), the induction hypothesis provides an orthogonal basis \( (\v_2, \dots, \v_n) \) of \( W \) for that restriction.

Concatenating bases of the summands of a direct sum gives a basis of it (@thm-direct-sum-k-criteria, (a) \( \Leftrightarrow \) (d)), so \( \sB = (\v_1, \v_2, \dots, \v_n) \) is a basis of \( V \). It is orthogonal for \( \beta \): for \( j \ge 2 \) we have \( \v_j \in W = \ker\varphi \), so \( \beta(\v_1, \v_j) = \varphi(\v_j) = 0 \), and \( \beta(\v_j, \v_1) = 0 \) by symmetry; and for \( 2 \le i \ne j \) the value \( \beta(\v_i,\v_j) \) is \( 0 \) by the choice of the basis of \( W \). This completes the induction.

For the matrix statement, let \( \A \in M_n(F) \) be symmetric and let \( \beta(\x,\y) = \x\tp\A\y \) on \( V = F^n \), which is symmetric by @prp-form-symmetry-matrix and has \( \mtx{\beta}{\sE}{\sE} = \A \) in the standard basis \( \sE \). Take an orthogonal basis \( \sB \) as above and let \( \P = \mtx{\id}{\sB}{\sE} \), the matrix whose columns are the vectors of \( \sB \), which is invertible. By @thm-change-of-basis-form, \( \mtx{\beta}{\sB}{\sB} = \P\tp\A\P \), and this matrix is diagonal. This proves the theorem.
:::

Two hypotheses did visible work. Symmetry was used twice: to make \( \beta(\v_j,\v_1) \) vanish along with \( \beta(\v_1,\v_j) \), and to keep the restriction to \( W \) symmetric so the induction could run. The characteristic hypothesis was used exactly once, inside @lem-anisotropic-vector-exists — and that single use is essential: Exercise C2 below exhibits a symmetric matrix over \( \nF_2 \) that is congruent to no diagonal matrix at all.

::: {.warning}
**Diagonal does not mean "the diagonal entries are eigenvalues".** The matrix \( \P\tp\A\P \) of @thm-symmetric-form-diagonalizable is congruent to \( \A \), not similar to it, and its entries are the values \( q(\v_i) \) at whatever basis the algorithm happened to produce. Over \( \nR \) they can be scaled at will: replacing \( \v_i \) by \( t\v_i \) replaces \( d_i \) by \( t^2d_i \). There is no canonical list of numbers here. The next section finds what there *is*.
:::

::: {.check}
In @thm-symmetric-form-diagonalizable, how many of the diagonal entries \( d_i \) are zero?
:::

::: {.solution}
Exactly \( n - \rank\A \) of them. A diagonal matrix has rank equal to its number of non-zero entries, and congruence preserves rank (@thm-congruence-preserves-rank), so the count is the same for every orthogonal basis even though the individual \( d_i \) are not. In the language of Section 1, those \( \v_i \) with \( d_i = 0 \) span the radical \( \operatorname{rad}(\beta) \) of @def-radical, since in an orthogonal basis such a \( \v_i \) pairs to zero with every basis vector; and \( \beta \) is non-degenerate (@def-nondegenerate) exactly when no \( d_i \) is zero.
:::

## The algorithm: symmetric row and column operations

The proof is constructive, but running it by hand means chasing kernels of functionals. There is a bookkeeping device that does the same work on the matrix directly, and it is the practical content of this section.

The key observation is that a congruence by an elementary matrix is a **pair** of operations. Let \( \E \) be an elementary matrix (@def-elementary-matrix). Right multiplication \( \A\E \) performs a column operation, and left multiplication \( \E\tp\A \) performs the corresponding row operation. So \( \A \mapsto \E\tp\A\E \) performs both, and the result is congruent to \( \A \) and again symmetric. Doing the operations in pairs is exactly what keeps the matrix symmetric, and that is the whole idea.

::: {.algorithm}
To diagonalize a symmetric \( \A \in M_n(F) \) by congruence, write \( \A \) and \( \I_n \) side by side and repeat, for \( i = 1, 2, \dots, n \) in turn:

- **If \( a_{ii} = 0 \) but some \( a_{jj} \ne 0 \) with \( j > i \)**, swap rows \( i, j \) and then columns \( i, j \).
- **If \( a_{ii} = 0 \) and every \( a_{jj} = 0 \) for \( j \ge i \)**, look for an entry \( a_{ij} \ne 0 \) with \( j > i \). If there is none, then row \( i \) and column \( i \) are already zero in every position, so move on to \( i + 1 \). If there is one, add row \( j \) to row \( i \), then column \( j \) to column \( i \); the new \( a_{ii} \) is \( 2a_{ij} \ne 0 \).
- **Now \( a_{ii} \ne 0 \).** For each \( j > i \) with \( a_{ij} \ne 0 \), subtract \( (a_{ij}/a_{ii}) \) times row \( i \) from row \( j \), then \( (a_{ij}/a_{ii}) \) times column \( i \) from column \( j \).

Over a field where division is inconvenient — \( \nQ \) or \( \nZ \)-valued data by hand — the clearing step may instead be done as \( \text{row } j \mapsto a_{ii}\,\text{row } j - a_{ij}\,\text{row } i \), with the matching column operation. That is the same move composed with scaling row and column \( j \) by \( a_{ii} \ne 0 \), which is itself a congruence, so it is legitimate; it keeps the entries integral and changes the diagonal result only by square factors. The worked example below takes this route.

Perform only the **column** half of each operation on the matrix standing to the right. When \( \A \) has become diagonal, that matrix is \( \P \), and \( \P\tp\A\P \) is the diagonal result.
:::

The second bullet is @lem-anisotropic-vector-exists made mechanical, and the factor \( 2 = 1 + 1 \) in it is where the algorithm would stop in characteristic \( 2 \). The right-hand matrix works because applying the column operations \( \E_1, \E_2, \dots, \E_k \) in order turns \( \I \) into \( \E_1\E_2\cdots\E_k \), which is the product whose transpose and self sandwich \( \A \).

::: {#exm-symmetric-elimination-3x3}
[Diagonalizing a symmetric matrix with zero diagonal]

Over \( \nQ \), diagonalize
\[
\A = \begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix}
\]
by congruence, producing an invertible \( \P \) with \( \P\tp\A\P \) diagonal.
:::

::: {.solution}
The form is \( q(\x) = 2x_1x_2 + 2x_1x_3 + 2x_2x_3 \): every diagonal entry is \( 0 \), so there is no square to complete yet, and the second bullet applies.

*Step 1 (create a pivot).* Add row \( 2 \) to row \( 1 \), then column \( 2 \) to column \( 1 \). The matrix becomes
\[
\begin{pmatrix} 1 & 1 & 2 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix}
\ \longrightarrow\
\begin{pmatrix} 2 & 1 & 2 \\ 1 & 0 & 1 \\ 2 & 1 & 0 \end{pmatrix},
\]
the left matrix after the row operation and the right one after the matching column operation. The new corner entry is \( q(\e_1 + \e_2) = 2 \).

*Step 2 (clear the first row and column, in two paired moves).* Rather than divide by \( 2 \), use the operation "row \( 2 \mapsto 2\cdot\text{row } 2 - \text{row } 1 \)", which is a scaling followed by an addition, hence a congruence by a product of two elementary matrices, and legitimate because \( 2 \ne 0 \) in \( \nQ \). Apply it and its column partner. This keeps every entry an integer:
\[
\begin{pmatrix} 2 & 1 & 2 \\ 0 & -1 & 0 \\ 2 & 1 & 0 \end{pmatrix}
\ \longrightarrow\
\begin{pmatrix} 2 & 0 & 2 \\ 0 & -2 & 0 \\ 2 & 0 & 0 \end{pmatrix}.
\]
Then "row \( 3 \mapsto \text{row } 3 - \text{row } 1 \)" and its column partner:
\[
\begin{pmatrix} 2 & 0 & 2 \\ 0 & -2 & 0 \\ 0 & 0 & -2 \end{pmatrix}
\ \longrightarrow\
\begin{pmatrix} 2 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -2 \end{pmatrix}.
\]

*The transforming matrix.* Applying the three **column** operations to \( \I_3 \) in the same order gives
\[
\I_3 \to \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}
\to \begin{pmatrix} 1 & -1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}
\to \begin{pmatrix} 1 & -1 & -1 \\ 1 & 1 & -1 \\ 0 & 0 & 1 \end{pmatrix} = \P .
\]
Here \( \det\P = 2 \ne 0 \), so \( \P \) is invertible, and
\[
\P\tp\A\P = \diag(2, -2, -2).
\]
The check is one column at a time: with \( \p_1 = (1,1,0) \), \( \p_2 = (-1,1,0) \) and \( \p_3 = (-1,-1,1) \), we get \( q(\p_1) = 2 \), \( q(\p_2) = -2 \) and \( q(\p_3) = 2 - 2 - 2 = -2 \), while \( \beta(\p_1,\p_2) = \p_1\tp\A\p_2 = (1,1,0)\cdot(1,-1,0) = 0 \) and similarly for the other two pairs.
:::

Two observations about that example. The determinants are \( \det\A = 2 \) and \( \det(\P\tp\A\P) = 8 \), and they differ by \( (\det\P)^2 = 4 \): a congruence multiplies the determinant by a square, which is the discriminant statement of Section 2. And the eigenvalues of \( \A \) are \( 2, -1, -1 \), whose signs are \( +, -, - \) — the same pattern of signs as \( 2, -2, -2 \), with none of the same numbers. That coincidence is Section 5.

## Over the complex numbers, and over a general field

The diagonal entries produced by the algorithm are not canonical, but there is a precise statement of how much freedom remains.

::: {#prp-diagonal-entries-square-classes}
[Diagonal Entries Are Defined Only up to Squares]

Let \( \sB = (\v_1, \dots, \v_n) \) be an orthogonal basis for \( \beta \) with \( d_i = q(\v_i) \), and let \( t_1, \dots, t_n \in F \) be non-zero. Then \( (t_1\v_1, \dots, t_n\v_n) \) is again an orthogonal basis for \( \beta \), with diagonal entries \( t_i^2d_i \).
:::

::: {.proof}
Scaling basis vectors by non-zero scalars again gives a basis. For \( i \ne j \), bilinearity gives \( \beta(t_i\v_i, t_j\v_j) = t_it_j\beta(\v_i,\v_j) = 0 \), so the new basis is orthogonal; and \( q(t_i\v_i) = t_i^2q(\v_i) = t_i^2d_i \).
:::

So each non-zero \( d_i \) can be changed to any other element of its coset in the group \( F^{\times}/(F^{\times})^2 \) of **square classes**, and no further, by this move. How much that costs depends entirely on the arithmetic of \( F \):

- Over \( \nC \), every element is a square, so there is exactly one non-zero square class and every non-zero \( d_i \) can be turned into \( 1 \).
- Over \( \nR \), the squares are the positive numbers, so there are two classes and every non-zero \( d_i \) can be turned into \( 1 \) or \( -1 \), according to its sign — the subject of the next section.
- Over \( \nQ \) there are infinitely many classes (\( 2, 3, 5, \dots \) are pairwise inequivalent), so the \( 1 \)-dimensional forms \( q(x) = x^2 \) and \( q(x) = 2x^2 \) are already non-congruent.
- Over \( \nF_p \) with \( p \) odd there are exactly two classes, as for \( \nR \), but "which class" is not a matter of sign.

The complex case collapses completely.

::: {#cor-complex-symmetric-classification}
[Classification of Complex Symmetric Matrices by Rank]

Let \( \A \in M_n(\nC) \) be symmetric of rank \( r \). Then \( \A \) is congruent to
\[
\I_r \oplus \0_{n-r} = \diag(\underbrace{1, \dots, 1}_{r}, 0, \dots, 0).
\]
Consequently two symmetric matrices in \( M_n(\nC) \) are congruent if and only if they have the same rank, and there are exactly \( n + 1 \) congruence classes.
:::

::: {.proof}
By @thm-symmetric-form-diagonalizable (with \( \operatorname{char}\nC = 0 \)) there is an invertible \( \P_1 \) with \( \P_1\tp\A\P_1 = \D = \diag(d_1, \dots, d_n) \) diagonal. Congruence preserves rank (@thm-congruence-preserves-rank), and the rank of a diagonal matrix is its number of non-zero entries, so exactly \( r \) of the \( d_i \) are non-zero. Permuting the basis vectors is a congruence by a permutation matrix \( \P_2 \), so we may assume \( d_1, \dots, d_r \ne 0 \) and \( d_{r+1} = \dots = d_n = 0 \).

Every non-zero complex number has a square root, so choose \( s_i \in \nC \) with \( s_i^2 = d_i \) for \( i \le r \), and set \( t_i = 1/s_i \) for \( i \le r \) and \( t_i = 1 \) otherwise. By @prp-diagonal-entries-square-classes the congruence by \( \P_3 = \diag(t_1, \dots, t_n) \) replaces \( d_i \) by \( t_i^2d_i \), which is \( 1 \) for \( i \le r \) and \( 0 \) otherwise. So \( \P\tp\A\P = \I_r \oplus \0_{n-r} \) with \( \P = \P_1\P_2\P_3 \).

For the classification: congruent matrices have equal rank by @thm-congruence-preserves-rank, and matrices of equal rank are both congruent to the same normal form, hence to each other by @prp-congruence-equivalence. The possible ranks are \( 0, 1, \dots, n \), giving \( n+1 \) classes. This proves the corollary.
:::

Contrast this with similarity, where complex symmetric matrices are not classified by anything so simple: the matrix \( \begin{psmallmatrix} 1 & i \\ i & -1\end{psmallmatrix} \) is symmetric, non-zero, and satisfies \( \A^2 = \0 \), so it is not even diagonalizable as an operator. Congruence is a coarser relation than similarity on symmetric matrices, and over \( \nC \) it is coarse enough to be finite.

## Exercises

### A. Check your understanding

:::: {#exr-diagonalizing-symmetric-forms-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define what it means for an ordered basis to be an **orthogonal basis for a bilinear form** \( \beta \), and say what that means about \( \mtx{\beta}{\sB}{\sB} \).
2. State @thm-symmetric-form-diagonalizable with all of its hypotheses.
3. Which step of the proof uses \( \operatorname{char} F \ne 2 \), and what exactly is divided by?
4. Determine whether the following statement is correct, and justify your answer: if \( \P\tp\A\P = \diag(d_1, \dots, d_n) \), then the \( d_i \) are the eigenvalues of \( \A \).
5. Describe the pair of operations that a congruence by an elementary matrix performs.
:::
::::

::: {.solution}
(a) \( \sB = (\v_1,\dots,\v_n) \) is orthogonal for \( \beta \) if \( \beta(\v_i,\v_j) = 0 \) whenever \( i \ne j \). Equivalently \( \mtx{\beta}{\sB}{\sB} \) is diagonal, with entries \( q(\v_i) \).

(b) If \( \operatorname{char} F \ne 2 \), \( V \) is finite-dimensional over \( F \) and \( \beta \) is a symmetric bilinear form on \( V \), then \( V \) has an orthogonal basis for \( \beta \); equivalently every symmetric \( \A \in M_n(F) \) is congruent to a diagonal matrix.

(c) @lem-anisotropic-vector-exists, inside Step 2 of the proof. It produces \( q(\u+\w) = (1+1)\beta(\u,\w) \) and needs \( 1 + 1 \ne 0 \) to conclude that this is non-zero. Equivalently, the algorithm's repair move multiplies by \( 2 \), so it needs \( 2 \ne 0 \).

(d) Incorrect. The relation is congruence, not similarity. In @exm-symmetric-elimination-3x3 the diagonal entries are \( 2, -2, -2 \) while the eigenvalues are \( 2, -1, -1 \). Only the signs matched there, and Section 5 explains why.

(e) A column operation and the matching row operation: \( \A \mapsto \E\tp\A\E \). Performing both keeps the matrix symmetric and keeps it in the same congruence class.
:::

### B. Practice

:::: {#exr-diagonalizing-symmetric-forms-b1}
[B1: Symmetric elimination]

Over \( \nQ \), let
\[
\A = \begin{pmatrix} 1 & 2 & 0 \\ 2 & 1 & 3 \\ 0 & 3 & 1 \end{pmatrix}.
\]
Diagonalize \( \A \) by paired row and column operations, exhibiting \( \P \) and \( \P\tp\A\P \).
::::

::: {.solution}
Here \( a_{11} = 1 \ne 0 \), so the pivot is already available.

*Clear the first row and column.* Subtract \( 2 \times \) row \( 1 \) from row \( 2 \), then \( 2 \times \) column \( 1 \) from column \( 2 \). The entry \( a_{13} \) is already \( 0 \), so nothing else is needed in this round:
\[
\begin{pmatrix} 1 & 2 & 0 \\ 0 & -3 & 3 \\ 0 & 3 & 1 \end{pmatrix}
\ \longrightarrow\
\begin{pmatrix} 1 & 0 & 0 \\ 0 & -3 & 3 \\ 0 & 3 & 1 \end{pmatrix}.
\]

*Clear the second row and column.* The pivot is \( -3 \), and \( a_{23} = 3 \), so add row \( 2 \) to row \( 3 \) and then column \( 2 \) to column \( 3 \):
\[
\begin{pmatrix} 1 & 0 & 0 \\ 0 & -3 & 3 \\ 0 & 0 & 4 \end{pmatrix}
\ \longrightarrow\
\begin{pmatrix} 1 & 0 & 0 \\ 0 & -3 & 0 \\ 0 & 0 & 4 \end{pmatrix}.
\]

*The transforming matrix.* Applying the two column operations to \( \I_3 \) gives
\[
\P = \begin{pmatrix} 1 & -2 & -2 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix},
\qquad
\P\tp\A\P = \diag(1, -3, 4).
\]
As a check, \( \det\P = 1 \) and \( \det\A = -12 = \det\diag(1,-3,4) \).
:::

:::: {#exr-diagonalizing-symmetric-forms-b2}
[B2: No pivot on the diagonal]

Over \( \nQ \), let \( \A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) and \( q(\x) = 2x_1x_2 \).

::: {.enumerate options="label=(\alph*)"}
1. Find a vector \( \v \) with \( q(\v) \ne 0 \), as in @lem-anisotropic-vector-exists.
2. Diagonalize \( \A \) by paired operations and exhibit \( \P \).
3. Write \( q \) as a difference of two squares in the new coordinates.
:::
::::

::: {.solution}
(a) Both \( \e_1 \) and \( \e_2 \) give \( q = 0 \), so take \( \v = \e_1 + \e_2 \): \( q(\v) = 2 \ne 0 \).

(b) Add row \( 2 \) to row \( 1 \), then column \( 2 \) to column \( 1 \), reaching \( \begin{psmallmatrix} 2 & 1 \\ 1 & 0 \end{psmallmatrix} \). Then apply "row \( 2 \mapsto 2\cdot\text{row } 2 - \text{row } 1 \)" and its column partner, reaching \( \diag(2,-2) \). Applying the same two column operations to \( \I_2 \) gives
\[
\P = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}, \qquad \P\tp\A\P = \diag(2,-2).
\]
Check directly: \( \P\tp\A = \begin{psmallmatrix} 1 & 1 \\ 1 & -1\end{psmallmatrix} \) and multiplying by \( \P \) gives \( \begin{psmallmatrix} 2 & 0 \\ 0 & -2\end{psmallmatrix} \).

(c) With \( \x = \P\y \), that is \( x_1 = y_1 - y_2 \) and \( x_2 = y_1 + y_2 \), we get \( q = 2(y_1-y_2)(y_1+y_2) = 2y_1^2 - 2y_2^2 \). This is the familiar identity \( ab = \bigl(\tfrac{a+b}{2}\bigr)^2 - \bigl(\tfrac{a-b}{2}\bigr)^2 \) read as a change of variable, and it needs \( 2 \) to be invertible.
:::

:::: {#exr-diagonalizing-symmetric-forms-b3}
[B3: Reading off the rank]

Let \( \A \in M_4(\nC) \) be symmetric with \( \rank\A = 3 \). Write down the normal form of \( \A \) under congruence, and say how many congruence classes of symmetric matrices there are in \( M_4(\nC) \).
::::

::: {.solution}
By @cor-complex-symmetric-classification, \( \A \) is congruent to \( \I_3 \oplus \0_1 = \diag(1,1,1,0) \). Since rank is a complete invariant there, the classes correspond to the possible ranks \( 0, 1, 2, 3, 4 \), so there are \( 5 \) of them.
:::

### C. Going deeper

:::: {#exr-diagonalizing-symmetric-forms-c1}
[C1: Square classes over a finite field]

Work over \( \nF_5 \), whose non-zero squares are \( 1 \) and \( 4 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that the \( 1 \times 1 \) matrices \( (1) \) and \( (2) \) are not congruent over \( \nF_5 \).
2. Prove that \( \I_2 \) and \( 2\I_2 \) **are** congruent over \( \nF_5 \), by exhibiting a \( \P \).
3. Explain why (a) and (b) are consistent with @prp-diagonal-entries-square-classes.
:::

*Hint: for (b), look for two vectors \( \p_1, \p_2 \) with \( \p_i \cdot \p_i = 2 \) and \( \p_1 \cdot \p_2 = 0 \).*
::::

::: {.solution}
(a) A congruence of \( 1 \times 1 \) matrices is \( (a) \mapsto (p^2a) \) with \( p \ne 0 \). So \( (1) \) and \( (2) \) are congruent exactly when \( 2 = p^2 \) for some \( p \in \nF_5^{\times} \). The squares of \( 1, 2, 3, 4 \) are \( 1, 4, 4, 1 \), so \( 2 \) is not a square and the two are not congruent.

(b) Take \( \p_1 = (1,1) \) and \( \p_2 = (1,4) \). Then \( \p_1 \cdot \p_1 = 2 \), \( \p_2 \cdot \p_2 = 1 + 16 = 17 = 2 \) and \( \p_1 \cdot \p_2 = 1 + 4 = 5 = 0 \) in \( \nF_5 \). With
\[
\P = \begin{pmatrix} 1 & 1 \\ 1 & 4 \end{pmatrix},
\qquad \det\P = 4 - 1 = 3 \ne 0,
\]
we get \( \P\tp\I_2\P = \P\tp\P = \diag(2,2) = 2\I_2 \).

(c) @prp-diagonal-entries-square-classes only says what **rescaling a single basis vector** can do, and that move cannot change a square class. Part (b) does not contradict it, because the congruence there is not diagonal: it mixes the two coordinates, and both diagonal entries change square class at once. What is invariant is the class of their product, the **determinant**: \( \det\I_2 = 1 \) and \( \det(2\I_2) = 4 \) differ by \( 4 = 2^2 \), a square.
:::

:::: {#exr-diagonalizing-symmetric-forms-c2}
[C2: Is this still true over \( \nF_2 \)?]

Let \( \A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) over \( \nF_2 \), and let \( \beta(\x,\y) = \x\tp\A\y \) on \( \nF_2^2 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \beta \) is alternating.
2. Prove that if \( \P \in M_2(\nF_2) \) is invertible, then every diagonal entry of \( \P\tp\A\P \) is \( 0 \).
3. Deduce that \( \A \) is congruent to **no** diagonal matrix except the zero matrix, and hence that @thm-symmetric-form-diagonalizable fails over \( \nF_2 \).
:::
::::

::: {.solution}
(a) By @prp-alternating-form-matrix (b): over \( \nF_2 \) we have \( -\A = \A \), so \( \A\tp = \A = -\A \), and the diagonal entries of \( \A \) are \( 0 \). (Directly: \( \beta(\x,\x) = 2x_1x_2 = 0 \).)

(b) The \( i \)-th diagonal entry of \( \P\tp\A\P \) is \( \p_i\tp\A\p_i = q(\p_i) \), where \( \p_i \) is the \( i \)-th column of \( \P \). By (a), \( q \) vanishes identically, so every diagonal entry is \( 0 \).

(c) A diagonal matrix congruent to \( \A \) has all diagonal entries \( 0 \) by (b), hence is the zero matrix. But congruence preserves rank (@thm-congruence-preserves-rank) and \( \rank\A = 2 \ne 0 = \rank\0 \). So no diagonal matrix is congruent to \( \A \). Since \( \A \) is symmetric over \( \nF_2 \), the conclusion of @thm-symmetric-form-diagonalizable fails there, and the hypothesis \( \operatorname{char} F \ne 2 \) cannot be dropped.
:::

:::: {#exr-diagonalizing-symmetric-forms-c3}
[C3: Diagonalizing the restriction]

Let \( \operatorname{char} F \ne 2 \), let \( \beta \) be a symmetric bilinear form on \( V \), and let \( U \subseteq V \) be a subspace.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( U \) has an orthogonal basis for the restriction of \( \beta \) to \( U \).
2. Give an example, with \( \dim V = 2 \), in which \( \beta \) is non-degenerate but its restriction to some \( 1 \)-dimensional \( U \) is the zero form.
3. Deduce that an orthogonal basis of \( U \) cannot always be extended to an orthogonal basis of \( V \) by adding vectors of \( U \) alone, and say in one sentence what @thm-symmetric-form-diagonalizable does guarantee instead.
:::
::::

::: {.solution}
(a) The restriction \( \beta|_{U \times U} \) is bilinear, since it is the same function on a smaller domain, and symmetric for the same reason. \( U \) is finite-dimensional, being a subspace of a finite-dimensional space (@thm-subspace-dimension). So @thm-symmetric-form-diagonalizable applies to \( (U, \beta|_{U\times U}) \) directly.

(b) Over \( \nQ \) take \( \beta(\x,\y) = x_1y_2 + x_2y_1 \) on \( \nQ^2 \), with matrix \( \begin{psmallmatrix} 0&1\\1&0\end{psmallmatrix} \), which is invertible, so \( \beta \) is non-degenerate. Put \( U = \Span(\e_1) \). Then \( \beta(a\e_1, b\e_1) = 0 \) for all \( a, b \), so the restriction is the zero form even though \( \beta \) is not.

(c) In (b) the single vector \( \e_1 \) is an orthogonal basis of \( U \), but no vector of \( U \) can be added to it, and any orthogonal basis of \( V \) for this \( \beta \) must consist of vectors \( \v \) with \( q(\v) \ne 0 \) (its matrix is diagonal and invertible), so \( \e_1 \) belongs to none of them. What the theorem guarantees is only the existence of *some* orthogonal basis of \( V \), built from scratch; it promises nothing about extending a given orthogonal list, and Section 8 is where a correct extension statement finally appears.
:::
