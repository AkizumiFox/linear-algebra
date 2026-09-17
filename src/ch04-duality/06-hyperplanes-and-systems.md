# Hyperplanes and Linear Systems Revisited

Chapter 2 met subspaces of \( F^n \) in two disguises. A **parametric** description lists spanning vectors, as in \( \col(A) \). An **implicit** description lists equations, as in \( \nul(A) \). We moved from equations to spanning vectors by elimination, but we never asked whether the reverse is always possible, or how many equations it takes. Duality answers both questions at once: the equations of a subspace \( U \) are the elements of \( U^{0} \). This section turns that sentence into an algorithm, proves once more that row rank and nullity add up to \( n \), and ends the chapter with a dictionary between a space and its dual.

## Row vectors are functionals

Recall from @thm-functionals-on-fn how functionals on \( F^n \) look. For \( \a = (a_1, \dots, a_n) \in F^n \), put
\[
\varphi_{\a} \colon F^n \to F, \qquad \varphi_{\a}(\x) = \a\tp\x = a_1x_1 + \dots + a_nx_n .
\]
By that theorem, every \( \varphi \in (F^n)^{*} \) is \( \varphi_{\a} \) for exactly one \( \a \), namely \( a_j = \varphi(\e_j) \), and \( \a \mapsto \varphi_{\a} \) is an isomorphism \( F^n \to (F^n)^{*} \).

The functional \( \varphi_{\a} \) is "multiply by the **row** vector \( \a\tp \)". So the identification is really between functionals and row vectors, and that is what makes a system of equations a dual object. Write the rows of \( A \in M_{m \times n}(F) \) as \( \a_1\tp, \dots, \a_m\tp \) with \( \a_i \in F^n \). The \( i \)-th entry of \( A\x \) is \( \a_i\tp\x = \varphi_{\a_i}(\x) \), so the homogeneous system \( A\x = \0 \) says exactly that \( \varphi_{\a_1}(\x) = \dots = \varphi_{\a_m}(\x) = 0 \). Hence
\[
\nul(A) = \ker\varphi_{\a_1} \cap \dots \cap \ker\varphi_{\a_m} .
\]
Each non-zero row contributes a hyperplane (@thm-hyperplane-kernel-functional), and the null space is their intersection. **An equation is a functional, and a system is a list of functionals.**

The identification uses the standard basis of \( F^n \), and nothing else. Under it, the coordinate functionals \( \x \mapsto x_i \), which form the dual basis of \( (\e_1, \dots, \e_n) \), correspond to \( \e_1, \dots, \e_n \), that is, to the rows \( \e_1\tp, \dots, \e_n\tp \).

## Every subspace is a solution set

To describe \( U \) by equations, we need equations that hold on \( U \), that is, functionals in \( U^{0} \), and enough of them that they hold **only** on \( U \). The first requirement is the definition of \( U^{0} \). The second follows from the separation of points, applied in the quotient.

::: {#lem-subspace-cut-out-by-annihilator}
[A subspace is cut out by its annihilator]

Let \( V \) be a finite-dimensional vector space and \( U \) a subspace. For \( \v \in V \),
\[
\v \in U \quad \iff \quad \varphi(\v) = 0 \text{ for every } \varphi \in U^{0} .
\]
If \( (\varphi_1, \dots, \varphi_k) \) is a basis of \( U^{0} \), then \( U = \ker\varphi_1 \cap \dots \cap \ker\varphi_k \).
:::

::: {.proof}
(⇒) This is @def-annihilator.

(⇐) Suppose \( \v \notin U \). Then \( \v + U \) is a non-zero vector of \( V/U \) by @lem-coset-equality (b), and \( V/U \) is finite-dimensional (@thm-dimension-quotient). By @thm-functionals-separate-points there is \( \psi \in (V/U)^{*} \) with \( \psi(\v + U) \ne 0 \). By @thm-dual-of-quotient, \( \varphi = \psi \circ \pi \) lies in \( U^{0} \), and \( \varphi(\v) = \psi(\v + U) \ne 0 \). This proves the contrapositive.

For the last statement, \( U \subseteq \ker\varphi_i \) for each \( i \) since \( \varphi_i \in U^{0} \). Conversely, if \( \varphi_i(\v) = 0 \) for all \( i \), then every \( \varphi = \sum_i c_i\varphi_i \in U^{0} \) has \( \varphi(\v) = 0 \), so \( \v \in U \) by (⇐).
:::

The lemma is @cor-annihilator-of-annihilator in disguise. That corollary says \( U^{00} = U \) under \( V \cong V^{**} \); the lemma unpacks it into a statement about vectors. In \( F^n \), with rows in place of functionals, it becomes the main theorem of this section.

::: {#thm-subspace-is-solution-set}
[Every Subspace Is a Solution Set]

Let \( U \) be a subspace of \( F^n \) with \( \dim U = k \).

::: {.enumerate options="label=(\alph*)"}
1. There is a matrix \( A \in M_{(n-k) \times n}(F) \) with \( U = \nul(A) \). One may take as rows of \( A \) the vectors \( \a_1\tp, \dots, \a_{n-k}\tp \) for any \( \a_i \in F^n \) such that \( (\varphi_{\a_1}, \dots, \varphi_{\a_{n-k}}) \) is a basis of \( U^{0} \).
2. If \( B \in M_{m \times n}(F) \) and \( \nul(B) = U \), then \( m \ge n - k \).
:::

So \( U \) is the solution set of a homogeneous system of exactly \( n - k = \codim U \) equations, and of no system with fewer. (When \( k = n \), that is \( U = F^n \), this is the empty system, with no equations.)
:::

::: {.proof}
(a) By @thm-dimension-annihilator, \( \dim U^{0} = n - k \). Choose a basis of \( U^{0} \); by the identification above it is \( (\varphi_{\a_1}, \dots, \varphi_{\a_{n-k}}) \) for some \( \a_i \in F^n \). Let \( A \) have rows \( \a_1\tp, \dots, \a_{n-k}\tp \). Then
\[
\nul(A) = \ker\varphi_{\a_1} \cap \dots \cap \ker\varphi_{\a_{n-k}} = U,
\]
where the second equality is @lem-subspace-cut-out-by-annihilator.

(b) By @thm-rank-nullity-matrix, \( \rank B = n - \nullity B = n - k \). By @thm-row-rank-equals-column-rank, \( \rank B = \dim \row(B) \). The row space is spanned by the \( m \) rows of \( B \), so \( m \ge \dim\row(B) \) by @thm-size-bounds (b). Hence \( m \ge n - k \).
:::

The count is the one promised by codimension: **dimension counts free parameters, codimension counts independent equations**, and in \( F^n \) the two add up to \( n \).

::: {#exm-implicit-equations}
[Equations for a plane in \( \nR^4 \)]

Let \( U = \Span(\u_1, \u_2) \subseteq \nR^4 \), where \( \u_1 = (1, 1, 0, 1) \) and \( \u_2 = (0, 1, 1, 1) \). Find a system of linear equations whose solution set is \( U \).
:::

::: {.solution}
The two vectors are independent (compare first entries, then third), so \( \dim U = 2 \), and we expect \( 4 - 2 = 2 \) equations. For \( \a = (a_1, a_2, a_3, a_4) \), the functional \( \varphi_{\a} \) lies in \( U^{0} \) exactly when it vanishes at both spanning vectors (@thm-annihilator-properties (b)):
\[
a_1 + a_2 + a_4 = 0, \qquad a_2 + a_3 + a_4 = 0 .
\]
This is the system \( M\a = \0 \) for the matrix \( M \) whose **rows** are \( \u_1\tp \) and \( \u_2\tp \). Subtracting the second row from the first gives the RREF
\[
M = \begin{pmatrix} 1 & 1 & 0 & 1 \\ 0 & 1 & 1 & 1 \end{pmatrix} \ \longrightarrow\ \begin{pmatrix} 1 & 0 & -1 & 0 \\ 0 & 1 & 1 & 1 \end{pmatrix},
\]
with free variables \( a_3, a_4 \). By @thm-basis-null-space, a basis of the solutions is \( (1, -1, 1, 0) \) (from \( a_3 = 1, a_4 = 0 \)) and \( (0, -1, 0, 1) \) (from \( a_3 = 0, a_4 = 1 \)). The corresponding functionals form a basis of \( U^{0} \), and by @thm-subspace-is-solution-set,
\[
U = \{ \x \in \nR^4 : x_1 - x_2 + x_3 = 0, \ \ x_4 - x_2 = 0 \} .
\]
**Check.** Both equations hold at \( \u_1 \): \( 1 - 1 + 0 = 0 \) and \( 1 - 1 = 0 \); and at \( \u_2 \): \( 0 - 1 + 1 = 0 \) and \( 1 - 1 = 0 \). The coefficient matrix \( \begin{pmatrix} 1 & -1 & 1 & 0 \\ 0 & -1 & 0 & 1 \end{pmatrix} \) has rank 2, so its null space has dimension \( 4 - 2 = 2 \), and it contains the independent vectors \( \u_1, \u_2 \); hence it equals \( U \) (@thm-dim-impl-eq). The implicit description says: \( U \) consists of the vectors with \( x_4 = x_2 \) and \( x_1 + x_3 = x_2 \).
:::

## From spans to equations and back

The example is an instance of a general procedure. Both directions of the conversion are "compute a null space", applied to transposed data.

::: {.algorithm}
**Parametric to implicit.** Input: vectors \( \v_1, \dots, \v_p \in F^n \) with \( U = \Span(\v_1, \dots, \v_p) \).

1. Form \( M \in M_{p \times n}(F) \) whose \( i \)-th **row** is \( \v_i\tp \).
2. Row reduce \( M \) and find a basis \( \n_1, \dots, \n_d \) of \( \nul(M) \) as in @thm-basis-null-space.
3. Output the matrix \( A \in M_{d \times n}(F) \) whose \( j \)-th row is \( \n_j\tp \), that is, the equations \( \n_j\tp\x = 0 \) for \( j = 1, \dots, d \).

**Implicit to parametric.** Input: \( A \in M_{m \times n}(F) \). Output: a basis of \( \nul(A) \), found by row reduction as in @thm-basis-null-space.
:::

The second half was proved correct in Chapter 2. The first half is new.

::: {#thm-parametric-to-implicit}
[Correctness of the Conversion]

Let \( \v_1, \dots, \v_p \in F^n \), \( U = \Span(\v_1, \dots, \v_p) \), and let \( M \) and \( A \) be as in the algorithm. Then \( \nul(A) = U \), and \( A \) has exactly \( d = n - \dim U \) rows, which are linearly independent.
:::

::: {.idea}
The only thing to see is what step 2 computes. The \( i \)-th entry of \( M\n \) is \( \v_i\tp\n = \varphi_{\n}(\v_i) \). So \( \n \in \nul(M) \) says that the functional \( \varphi_{\n} \) vanishes at every \( \v_i \), that is, \( \varphi_{\n} \in U^{0} \). Step 2 therefore computes a basis of \( U^{0} \), and the theorem of the previous subsection does the rest.
:::

::: {.proof}
For \( \n \in F^n \), the \( i \)-th entry of \( M\n \) is \( \v_i\tp\n = \n\tp\v_i = \varphi_{\n}(\v_i) \), where the middle equality holds because both sides equal \( \sum_j (\v_i)_j n_j \). Hence
\[
\n \in \nul(M) \iff \varphi_{\n}(\v_i) = 0 \text{ for all } i \iff \varphi_{\n} \in \{\v_1, \dots, \v_p\}^{0} = U^{0},
\]
where the last equality is @thm-annihilator-properties (b). So the isomorphism \( \n \mapsto \varphi_{\n} \) maps \( \nul(M) \) onto \( U^{0} \). An isomorphism carries a basis to a basis (@thm-isomorphism-preserves-bases), so \( (\varphi_{\n_1}, \dots, \varphi_{\n_d}) \) is a basis of \( U^{0} \). In particular \( d = \dim U^{0} = n - \dim U \) by @thm-dimension-annihilator, and the \( \n_j \), hence the rows \( \n_j\tp \), are independent. By @thm-subspace-is-solution-set (a), the matrix \( A \) with rows \( \n_1\tp, \dots, \n_d\tp \) satisfies \( \nul(A) = U \).
:::

The algorithm does not need the \( \v_i \) to be independent. Redundant spanning vectors only produce zero rows in the RREF of \( M \), and the count \( d = n - \rank M \) automatically uses \( \dim U = \rank M \).

Running both halves in turn is a useful self-check. Starting from \( A \) in @exm-implicit-equations and computing \( \nul(A) \) must return a basis of \( U \); starting from that basis and running the first half must return equations with the same solution set, though not necessarily the same equations.

::: {.warning}
**Equations for a subspace are far from unique, and more equations do not mean a smaller solution set.** In @exm-implicit-equations, the system \( x_1 - x_2 + x_3 = 0 \), \( x_4 - x_2 = 0 \), \( x_1 + x_3 - x_4 = 0 \) has the **same** solution set \( U \): the third equation is the sum of the first and the negative of the second, so it adds a functional already in \( U^{0} \). Three equations in \( \nR^4 \) cut out a two-dimensional subspace here, not a one-dimensional one. Each new equation lowers the dimension by one **only if** its functional is not a combination of the previous ones. A theorem later in this section makes this precise.
:::

## Affine solution sets

An inhomogeneous equation \( \a\tp\x = b \) with \( \a \ne \0 \) defines a set that is not a subspace when \( b \ne 0 \). It is a translate of the hyperplane \( H = \ker\varphi_{\a} \): if \( \p \) is one solution, then by @thm-general-solution-structure the solutions are \( \p + H \). We call a coset \( \p + H \) of a hyperplane \( H \) (@def-coset) an **affine hyperplane**. In \( \nR^3 \), the plane \( x + y + z = 1 \) is an affine hyperplane, parallel to the hyperplane \( x + y + z = 0 \).

A system \( A\x = \b \) with rows \( \a_i\tp \) and right-hand sides \( b_i \) asks for the vectors lying on all the sets \( \{ \x : \a_i\tp\x = b_i \} \) at once. Each such set is an affine hyperplane if \( \a_i \ne \0 \); if \( \a_i = \0 \), it is all of \( F^n \) (when \( b_i = 0 \)) or empty (when \( b_i \ne 0 \)). So **the solution set of a linear system is an intersection of affine hyperplanes**, apart from these trivial rows. The duality theorems give the converse.

::: {#prp-affine-subspace-intersection}
[Cosets as intersections of affine hyperplanes]

Let \( U \) be a subspace of \( F^n \) of dimension \( k < n \), and let \( \p \in F^n \). Let \( A \in M_{(n-k) \times n}(F) \) be as in @thm-subspace-is-solution-set (a), with rows \( \a_1\tp, \dots, \a_{n-k}\tp \). Then
\[
\p + U = \{ \x \in F^n : A\x = A\p \} = \bigcap_{i=1}^{n-k} \{ \x : \a_i\tp\x = \a_i\tp\p \},
\]
an intersection of \( n - k \) affine hyperplanes.
:::

::: {.proof}
By @thm-subspace-is-solution-set, \( \nul(A) = U \). The vector \( \p \) is one solution of \( A\x = A\p \), so by @thm-general-solution-structure its solution set is \( \p + \nul(A) = \p + U \). The \( i \)-th equation reads \( \a_i\tp\x = \a_i\tp\p \). Each \( \varphi_{\a_i} \) is non-zero, because it belongs to a basis of \( U^{0} \); so \( \ker\varphi_{\a_i} \) is a hyperplane (@thm-hyperplane-kernel-functional), and \( \{ \x : \a_i\tp\x = \a_i\tp\p \} = \p + \ker\varphi_{\a_i} \) is an affine hyperplane, again by @thm-general-solution-structure applied to this one equation.
:::

Unlike hyperplanes, which all contain \( \0 \), affine hyperplanes can be disjoint: \( x_1 + x_2 = 0 \) and \( x_1 + x_2 = 1 \) are parallel lines in \( \nR^2 \). That is the geometric picture of an inconsistent system.

## The row space annihilates the null space

In Chapter 2, @thm-rank-nullity-matrix said \( \rank A + \nullity A = n \), and its proof counted pivot and free columns in the RREF. The duality of this chapter explains the same equation without elimination: the rows of \( A \) are exactly the equations satisfied by the null space.

::: {#thm-row-space-annihilates-null-space}
[The Row Space Is the Annihilator of the Null Space]

Let \( A \in M_{m \times n}(F) \). Identifying a row vector \( \a\tp \in M_{1 \times n}(F) \) with the functional \( \varphi_{\a} \in (F^n)^{*} \),
\[
\{ \varphi_{\a} : \a\tp \in \row(A) \} = \nul(A)^{0} .
\]
Consequently \( \dim \row(A) + \dim \nul(A) = n \).
:::

::: {.idea}
Let \( T = T_A \colon F^n \to F^m \). Its kernel is \( \nul(A) \), and @thm-kernel-image-dual-map says \( \im T' = (\ker T)^{0} \). So it is enough to see that \( \im T' \) is the row space. Pull back a functional \( \varphi_{\y} \) on \( F^m \): the result is \( \x \mapsto \y\tp A\x \), which is multiplication by the row \( \y\tp A \), the combination of the rows of \( A \) with coefficients \( y_1, \dots, y_m \). The transpose of Chapter 0 appears exactly here: \( \y\tp A = (A\tp\y)\tp \).
:::

::: {.proof}
Let \( T = T_A \colon F^n \to F^m \), \( T(\x) = A\x \), so that \( \ker T = \nul(A) \). Every functional on \( F^m \) is \( \varphi_{\y} \) for a unique \( \y \in F^m \), as recalled at the start of this section. By @def-dual-map, associativity of matrix multiplication, and @thm-transpose-properties,
\[
T'(\varphi_{\y})(\x) = \varphi_{\y}(A\x) = \y\tp(A\x) = (\y\tp A)\x = (A\tp\y)\tp\x = \varphi_{A\tp\y}(\x) \qquad (\x \in F^n),
\]
so \( T'(\varphi_{\y}) = \varphi_{A\tp\y} \). The columns of \( A\tp \) are \( \a_1, \dots, \a_m \), where \( \a_i\tp \) are the rows of \( A \), so \( A\tp\y = y_1\a_1 + \dots + y_m\a_m \) by @thm-matrix-times-vector-columns. As \( \y \) runs over \( F^m \), these are all the combinations of \( \a_1, \dots, \a_m \), and since transposing respects combinations (@thm-transpose-properties), they are exactly the vectors \( \a \) with \( \a\tp \in \row(A) \) (@def-row-space). Hence
\[
\im T' = \{ \varphi_{\a} : \a\tp \in \row(A) \} .
\]
By @thm-kernel-image-dual-map, \( \im T' = (\ker T)^{0} = \nul(A)^{0} \), which is the first claim.

For the count, \( \a\tp \mapsto \varphi_{\a} \) is an isomorphism \( M_{1 \times n}(F) \to (F^n)^{*} \) (transposition followed by \( \a \mapsto \varphi_{\a} \)), so \( \dim \row(A) = \dim \nul(A)^{0} = n - \dim\nul(A) \) by @thm-dimension-annihilator.
:::

The count is Rank–Nullity for matrices once more, now as a statement about annihilators: \( \rank A = \dim\row(A) \) counts independent equations and \( \nullity A \) counts free parameters. It also says that the given equations generate **all** the equations satisfied by \( \nul(A) \): any linear equation that holds on the solution set of \( A\x = \0 \) is a combination of the rows of \( A \).

::: {#cor-same-null-space-iff-same-row-space}
[Same solutions, same row space]

Let \( A \in M_{m \times n}(F) \) and \( B \in M_{p \times n}(F) \). Then \( \nul(A) = \nul(B) \) if and only if \( \row(A) = \row(B) \).
:::

::: {.proof}
(⇐) If \( \row(A) = \row(B) \), then \( \nul(A)^{0} = \nul(B)^{0} \) by @thm-row-space-annihilates-null-space, so \( \nul(A) = \nul(B) \) by @cor-subspaces-determined-by-annihilator.

(⇒) If \( \nul(A) = \nul(B) \), then \( \{ \varphi_{\a} : \a\tp \in \row(A) \} = \nul(A)^{0} = \{ \varphi_{\a} : \a\tp \in \row(B) \} \) by @thm-row-space-annihilates-null-space. Since \( \a\tp \mapsto \varphi_{\a} \) is injective, \( \row(A) = \row(B) \).
:::

Chapter 2 showed that row operations preserve the null space (@thm-row-ops-row-space). The corollary gives a converse in terms of row spaces: two systems in the same unknowns have the same solutions **exactly** when each equation of one is a combination of the equations of the other.

## Sums and intersections by duality

Parametric and implicit descriptions are good at different things. A **sum** is easy parametrically: \( U + W \) is spanned by a spanning list of \( U \) followed by one of \( W \) (@prp-sum-of-spans). An **intersection** is easy implicitly: if \( U = \nul(A) \) and \( W = \nul(B) \), then \( \x \in U \cap W \) exactly when \( \x \) satisfies both systems, so
\[
U \cap W = \nul \begin{pmatrix} A \\ B \end{pmatrix},
\]
the null space of the matrix with the rows of \( A \) above the rows of \( B \). Duality explains why each is easy where it is. The rows of the stacked matrix span \( \row(A) + \row(B) \), which corresponds to \( U^{0} + W^{0} = (U \cap W)^{0} \) by @thm-row-space-annihilates-null-space and @thm-annihilator-properties (d); and \( (U + W)^{0} = U^{0} \cap W^{0} \) says that the equations of a sum are the equations common to both pieces.

::: {#exm-intersection-via-equations}
[An intersection computed from equations]

In \( \nR^4 \), let \( U = \Span((1, 0, 1, 2), (0, 1, 1, 1)) \) and \( W = \Span((1, 1, 0, 1), (1, 3, 0, 1)) \), as in @exm-intersection-by-elimination. Find \( U \cap W \) by first finding equations for \( U \) and for \( W \).
:::

::: {.solution}
*Equations for \( U \).* A row \( (a_1, a_2, a_3, a_4) \) annihilates both spanning vectors when \( a_1 + a_3 + 2a_4 = 0 \) and \( a_2 + a_3 + a_4 = 0 \). This system is already in RREF, with free \( a_3, a_4 \); the basic solutions are \( (-1, -1, 1, 0) \) and \( (-2, -1, 0, 1) \). Changing signs, which does not change the kernels,
\[
U = \{ x_1 + x_2 - x_3 = 0, \ \ 2x_1 + x_2 - x_4 = 0 \} .
\]
*Equations for \( W \).* Here \( a_1 + a_2 + a_4 = 0 \) and \( a_1 + 3a_2 + a_4 = 0 \). Subtracting gives \( a_2 = 0 \), and then \( a_1 = -a_4 \), with \( a_3 \) free. The basic solutions are \( (0, 0, 1, 0) \) and \( (-1, 0, 0, 1) \), so
\[
W = \{ x_3 = 0, \ \ x_4 - x_1 = 0 \} .
\]
*Intersection.* Stack the four equations. From \( W \): \( x_3 = 0 \) and \( x_4 = x_1 \). Then \( x_1 + x_2 - x_3 = 0 \) gives \( x_2 = -x_1 \), and the last equation \( 2x_1 + x_2 - x_4 = 2x_1 - x_1 - x_1 = 0 \) holds automatically. So
\[
U \cap W = \{ (t, -t, 0, t) : t \in \nR \} = \Span((1, -1, 0, 1)),
\]
in agreement with Chapter 2.

The redundancy of the fourth equation is not a coincidence. The four rows span \( U^{0} + W^{0} = (U \cap W)^{0} \), which has dimension \( 4 - 1 = 3 \), so exactly one of the four equations must be a consequence of the others.

**Contrast with Chapter 2.** There we put the four spanning vectors as **columns** of one matrix and read the intersection off a null vector, a relation \( \u_1 - \u_2 = 2\w_1 - \w_2 \). Here we computed two small null spaces (the equations) and then one more (the intersection). The equation method pays off when the subspaces are given by equations in the first place, or when several intersections with the same \( U \) are needed: the equations of \( U \) are computed once.
:::

## Independent functionals

The warning above said that \( k \) equations cut out codimension \( k \) only when they are independent. We now make that precise, in any dimension. Given \( \varphi_1, \dots, \varphi_k \in V^{*} \), bundle them into one linear map
\[
\Phi \colon V \to F^k, \qquad \Phi(\v) = (\varphi_1(\v), \dots, \varphi_k(\v)),
\]
which is linear because each entry is. Its kernel is \( \ker\varphi_1 \cap \dots \cap \ker\varphi_k \), the common solution set of the \( k \) equations.

::: {#thm-independent-functionals-surjective}
[Independent Functionals]

Let \( V \) be a vector space over \( F \), of any dimension, and let \( \varphi_1, \dots, \varphi_k \in V^{*} \). The following are equivalent:

::: {.enumerate options="label=(\alph*)"}
1. \( (\varphi_1, \dots, \varphi_k) \) is linearly independent in \( V^{*} \);
2. \( \Phi \colon V \to F^k \) is surjective;
3. \( \ker\varphi_1 \cap \dots \cap \ker\varphi_k \) has codimension exactly \( k \).
:::
:::

::: {.idea}
A dependence \( \sum c_i\varphi_i = 0 \) says that \( \sum c_iy_i = 0 \) for every \( \y = \Phi(\v) \) in the image: the image lies in the kernel of a non-zero functional on \( F^k \). Conversely, if the image is a proper subspace of \( F^k \), some non-zero functional on \( F^k \) kills it, and its coefficients give a dependence. The First Isomorphism Theorem turns "surjective" into "codimension \( k \)".
:::

::: {.proof}
(a) ⇒ (b). Suppose \( \Phi \) is not surjective. Then \( \im\Phi \) is a proper subspace of \( F^k \), so \( \dim\im\Phi < k \) and, by @thm-dimension-annihilator, \( (\im\Phi)^{0} \ne \{0\} \). Take a non-zero functional in it; as at the start of this section it is \( \varphi_{\c} \), \( \y \mapsto c_1y_1 + \dots + c_ky_k \), for a non-zero \( \c \in F^k \). For every \( \v \in V \), \( \Phi(\v) \in \im\Phi \), so
\[
(c_1\varphi_1 + \dots + c_k\varphi_k)(\v) = \varphi_{\c}(\Phi(\v)) = 0 .
\]
Thus \( c_1\varphi_1 + \dots + c_k\varphi_k = 0 \) with \( \c \ne \0 \), and the list is dependent. This proves the contrapositive.

(b) ⇒ (a). Suppose \( \Phi \) is surjective and \( c_1\varphi_1 + \dots + c_k\varphi_k = 0 \). For each \( j \), choose \( \v_j \) with \( \Phi(\v_j) = \e_j \), that is, \( \varphi_i(\v_j) = \delta_{ij} \). Evaluating the relation at \( \v_j \) gives \( c_j = 0 \). So the list is independent.

(b) ⇔ (c). By @thm-first-isomorphism, \( V/\ker\Phi \cong \im\Phi \), and \( \ker\Phi = \bigcap_i \ker\varphi_i \). So the codimension of \( \bigcap_i\ker\varphi_i \) is \( \dim\im\Phi \), which equals \( k \) exactly when \( \im\Phi = F^k \) (@thm-dim-impl-eq).
:::

For \( V = F^n \) and \( \varphi_i = \varphi_{\a_i} \), the map \( \Phi \) is \( T_A \), where \( A \) has rows \( \a_i\tp \). The theorem then says: the rows of \( A \) are independent if and only if \( A\x = \b \) is solvable for **every** \( \b \in F^k \). Independent equations never contradict each other.

::: {.check}
In \( \nR^3 \), consider \( \varphi_1 = x + y \), \( \varphi_2 = y + z \), \( \varphi_3 = x - z \). What is the codimension of \( \ker\varphi_1 \cap \ker\varphi_2 \cap \ker\varphi_3 \)? Is the system \( x + y = 1 \), \( y + z = 1 \), \( x - z = 1 \) solvable?

::: {.solution}
\( \varphi_3 = \varphi_1 - \varphi_2 \), so the list is dependent, while \( (\varphi_1, \varphi_2) \) is independent (look at the coefficients of \( x \) and \( z \)). The three kernels intersect in \( \ker\varphi_1 \cap \ker\varphi_2 \), of codimension 2 by @thm-independent-functionals-surjective, so the intersection is a line, not \( \{\0\} \). The system is not solvable: any solution would give \( 1 = x - z = (x + y) - (y + z) = 1 - 1 = 0 \). This is (b) failing: \( (1, 1, 1) \notin \im\Phi \).
:::
:::

## Summary and transfer

The chapter has built a dictionary. On the left is a finite-dimensional space \( V \) of dimension \( n \), or a linear map \( T \colon V \to W \) between finite-dimensional spaces; on the right is its mirror image in the dual. Every entry has been proved in this chapter, and every arrow reverses inclusions or directions.

| In \( V \) (vectors) | In \( V^{*} \) (measurements) |
|---|---|
| a subspace \( U \), \( \dim U = k \) | its annihilator \( U^{0} \), \( \dim U^{0} = n - k \) |
| \( U \subseteq W \) | \( W^{0} \subseteq U^{0} \) |
| \( U + W \) | \( U^{0} \cap W^{0} \) |
| \( U \cap W \) | \( U^{0} + W^{0} \) |
| \( U \) itself, recovered as \( U^{00} \) | \( U^{0} \) determines \( U \) |
| the quotient \( V/U \) | the subspace \( U^{0} \cong (V/U)^{*} \) |
| the subspace \( U \) | the quotient \( V^{*}/U^{0} \cong U^{*} \) |
| a hyperplane \( H \) | a non-zero functional, up to scale |
| a spanning list (parametric form) | a list of equations (implicit form) |
| dimension (free parameters) | codimension (independent equations) |
| a basis \( (\v_1, \dots, \v_n) \) | its dual basis \( (\varphi_1, \dots, \varphi_n) \) |
| \( T \colon V \to W \) | \( T' \colon W^{*} \to V^{*} \), backwards |
| \( T \) injective | \( T' \) surjective |
| \( T \) surjective | \( T' \) injective |
| \( \ker T \) | \( \im T' = (\ker T)^{0} \) |
| \( \im T \) | \( \ker T' = (\im T)^{0} \) |
| \( \rank T \) | \( \rank T' = \rank T \) |
| the matrix \( A = \mtx{T}{\sB}{\sC} \) | the transpose \( A\tp = \mtx{T'}{\sC^{*}}{\sB^{*}} \) |
| \( \nul(A) \) | \( \row(A) \), as \( \nul(A)^{0} \) |
| \( V \) | \( V^{**} \), naturally isomorphic via \( \ev_V \) |

Three moves make the dictionary usable, and they transfer to any situation with a pairing between two spaces.

- **Test against functionals.** To show a vector is zero, or lies in a subspace, check that enough functionals vanish on it (@thm-functionals-separate-points, @lem-subspace-cut-out-by-annihilator).
- **Pass to the dual and count.** A question about a subspace can be translated into one about its annihilator, where \( \dim U + \dim U^{0} = n \) often settles it. The third proof of row rank = column rank (@cor-rank-dual-map) and the count in @thm-row-space-annihilates-null-space both work this way.
- **Prefer the natural map.** Isomorphisms such as \( V \cong V^{**} \), \( (V/U)^{*} \cong U^{0} \) and \( U^{*} \cong V^{*}/U^{0} \) are defined without a basis, so they can be used in any coordinates and survive changes of basis. Isomorphisms such as \( V \cong V^{*} \) depend on a choice, and a proof that uses one must say which.

In Chapter 10, an inner product will give a **chosen** isomorphism \( V \cong V^{*} \), and the annihilator \( U^{0} \) will reappear inside \( V \) itself as the orthogonal complement. The dictionary above is the part of that story that needs no inner product.

## Exercises

### A. Check your understanding

::: {#exr-hyperplanes-and-systems-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Explain how a row vector \( \a\tp \) (with \( \a \in F^n \)) defines a linear functional on \( F^n \), and why every functional arises this way.
2. What is the least number of homogeneous linear equations whose solution set is a given \( 3 \)-dimensional subspace of \( F^7 \)?
3. True or false: every system of three homogeneous equations in \( \nR^5 \) has a solution set of dimension \( 2 \). Justify your answer.
4. State the relation between \( \row(A) \) and \( \nul(A) \) in terms of annihilators.
5. True or false: if \( A \) and \( B \) have \( n \) columns and \( \nul(A) = \nul(B) \), then \( A \) and \( B \) have the same number of rows. Justify your answer.
6. Name the dual counterparts of: a sum of subspaces; an injective linear map; the matrix of a linear map.
:::
:::

::: {.solution}
(a) \( \varphi_{\a}(\x) = \a\tp\x \) is linear by the rules of matrix multiplication (@thm-matrix-multiplication-properties). A functional \( \varphi \) equals \( \varphi_{\a} \) with \( a_j = \varphi(\e_j) \), because both agree on the standard basis (@thm-linear-transform-basis); this is @thm-functionals-on-fn.

(b) \( 7 - 3 = 4 \), by @thm-subspace-is-solution-set.

(c) False. The equations may be dependent: \( x_1 = 0 \) written three times has a solution set of dimension \( 4 \). The dimension is \( 5 - \rank A \), which is \( 2 \) only when the three rows are independent.

(d) Identifying rows with functionals, \( \row(A) = \nul(A)^{0} \) (@thm-row-space-annihilates-null-space).

(e) False. By @cor-same-null-space-iff-same-row-space they have the same row space, but not necessarily the same number of rows: \( A = \begin{pmatrix} 1 & 0 \end{pmatrix} \) and \( B = \begin{pmatrix} 1 & 0 \\ 2 & 0 \end{pmatrix} \) both have null space \( \Span(\e_2) \).

(f) An intersection of annihilators, \( (U + W)^{0} = U^{0} \cap W^{0} \); a surjective dual map; the transpose matrix.
:::

### B. Practice

::: {#exr-hyperplanes-and-systems-b1}
[B1: Equations for a span]

Let \( U = \Span((1, 2, 0, -1), (2, 1, 1, 0), (3, 3, 1, -1)) \subseteq \nR^4 \).

::: {.enumerate options="label=(\alph*)"}
1. Find \( \dim U \).
2. Find a system of homogeneous linear equations with solution set \( U \), using as few equations as possible.
3. Hence write the affine plane \( (1, 0, 0, 0) + U \) as the solution set of a linear system.
:::
:::

::: {.solution}
(a) The third vector is the sum of the first two, so \( U = \Span((1, 2, 0, -1), (2, 1, 1, 0)) \) by @thm-span-absorb. These two vectors are independent, since neither is a multiple of the other, so they form a basis of \( U \) and \( \dim U = 2 \).

(b) By @thm-parametric-to-implicit, we need a basis of \( \nul(M) \), where \( M \) has the three vectors as rows. Row reduction gives
\[
M = \begin{pmatrix} 1 & 2 & 0 & -1 \\ 2 & 1 & 1 & 0 \\ 3 & 3 & 1 & -1 \end{pmatrix} \longrightarrow \begin{pmatrix} 1 & 0 & \tfrac23 & \tfrac13 \\ 0 & 1 & -\tfrac13 & -\tfrac23 \\ 0 & 0 & 0 & 0 \end{pmatrix}.
\]
The free variables are the third and fourth. Setting them to \( (3, 0) \) and \( (0, 3) \) to clear denominators gives the null vectors \( (-2, 1, 3, 0) \) and \( (-1, 2, 0, 3) \). So
\[
U = \{ \x \in \nR^4 : -2x_1 + x_2 + 3x_3 = 0, \ \ -x_1 + 2x_2 + 3x_4 = 0 \} .
\]
Check on the first two spanning vectors, which suffice since they span \( U \): \( -2 + 2 + 0 = 0 \), \( -1 + 4 - 3 = 0 \); \( -4 + 1 + 3 = 0 \), \( -2 + 2 + 0 = 0 \). Two equations is the minimum, by @thm-subspace-is-solution-set (b).

(c) By @prp-affine-subspace-intersection, replace each right-hand side by the value of the left-hand side at \( (1, 0, 0, 0) \):
\[
(1, 0, 0, 0) + U = \{ \x : -2x_1 + x_2 + 3x_3 = -2, \ \ -x_1 + 2x_2 + 3x_4 = -1 \} .
\]
:::

::: {#exr-hyperplanes-and-systems-b2}
[B2: A spanning list for a system]

Let \( U = \{ \x \in \nR^4 : x_1 + x_2 - x_3 + 2x_4 = 0, \ \ 2x_1 + 2x_2 + x_3 + x_4 = 0 \} \).

::: {.enumerate options="label=(\alph*)"}
1. Find a basis of \( U \).
2. Run the parametric-to-implicit algorithm on your basis, and check that the resulting equations have the same solution set as the given ones, by comparing row spaces.
:::
:::

::: {.solution}
(a) Row reduce the coefficient matrix: subtract twice row 1 from row 2 to get \( (0, 0, 3, -3) \), divide by 3, then add row 2 to row 1:
\[
\begin{pmatrix} 1 & 1 & -1 & 2 \\ 2 & 2 & 1 & 1 \end{pmatrix} \longrightarrow \begin{pmatrix} 1 & 1 & 0 & 1 \\ 0 & 0 & 1 & -1 \end{pmatrix}.
\]
The pivots are in columns 1 and 3, and \( x_2, x_4 \) are free. By @thm-basis-null-space, a basis is \( \n_1 = (-1, 1, 0, 0) \) and \( \n_2 = (-1, 0, 1, 1) \).

(b) Put \( \n_1\tp, \n_2\tp \) as the rows of \( M \) and solve \( M\a = \0 \): \( -a_1 + a_2 = 0 \) and \( -a_1 + a_3 + a_4 = 0 \). So \( a_2 = a_1 \) and \( a_3 = a_1 - a_4 \), with \( a_1, a_4 \) free; the basic solutions are \( (1, 1, 1, 0) \) and \( (0, 0, -1, 1) \). The new system is \( x_1 + x_2 + x_3 = 0 \), \( -x_3 + x_4 = 0 \). Its rows lie in the row space of the original matrix, which equals the row space of the RREF (@thm-row-ops-row-space), since \( (1, 1, 1, 0) = (1, 1, 0, 1) + (0, 0, 1, -1) \) and \( (0, 0, -1, 1) = -(0, 0, 1, -1) \). Both row spaces are two-dimensional, so they are equal (@thm-dim-impl-eq), and the two systems have the same solution set by @cor-same-null-space-iff-same-row-space.
:::

::: {#exr-hyperplanes-and-systems-b3}
[B3: Two planes in \( \nR^4 \)]

Let \( U = \Span((1, 0, 0, 1), (0, 1, 1, 0)) \) and \( W = \Span((1, 1, 0, 0), (0, 0, 1, 1)) \) in \( \nR^4 \).

::: {.enumerate options="label=(\alph*)"}
1. Find two equations for \( U \) and two for \( W \).
2. Use them to find \( U \cap W \).
3. Find a single equation for \( U + W \), using \( (U + W)^{0} = U^{0} \cap W^{0} \).
:::
:::

::: {.solution}
(a) Each pair is independent, so each plane has dimension 2 and needs two equations. The functionals \( x_1 - x_4 \) and \( x_2 - x_3 \) vanish at \( (1, 0, 0, 1) \) and \( (0, 1, 1, 0) \), and they are independent; since \( \dim U^{0} = 2 \) (@thm-dimension-annihilator), they form a basis of \( U^{0} \). So \( U = \{ x_1 = x_4, \ x_2 = x_3 \} \) by @thm-subspace-is-solution-set. In the same way \( x_1 - x_2 \) and \( x_3 - x_4 \) form a basis of \( W^{0} \), and \( W = \{ x_1 = x_2, \ x_3 = x_4 \} \).

(b) \( U \cap W \) is the solution set of all four equations: \( x_1 = x_4 \), \( x_2 = x_3 \), \( x_1 = x_2 \), \( x_3 = x_4 \). They force \( x_1 = x_2 = x_3 = x_4 \), so \( U \cap W = \Span((1, 1, 1, 1)) \).

(c) A functional in \( U^{0} \cap W^{0} \) has the form \( a(x_1 - x_4) + b(x_2 - x_3) = c(x_1 - x_2) + d(x_3 - x_4) \). Comparing coefficients of \( x_1, x_2, x_3, x_4 \): \( a = c \), \( b = -c \), \( -b = d \), \( -a = -d \). So \( a = c = d \) and \( b = -a \), and \( U^{0} \cap W^{0} = \Span(x_1 - x_2 + x_3 - x_4) \). By @thm-annihilator-properties (c) and @lem-subspace-cut-out-by-annihilator,
\[
U + W = \{ \x : x_1 - x_2 + x_3 - x_4 = 0 \},
\]
a hyperplane. Consistently, \( \dim(U + W) = 2 + 2 - 1 = 3 \) by @thm-dimension-formula-subspace-dim.
:::

### C. Going deeper

::: {#exr-hyperplanes-and-systems-c1}
[C1: Avoiding finitely many subspaces]

Let \( F \) be an **infinite** field, \( V \) a vector space over \( F \) with \( 1 \le \dim V = n < \infty \), and \( U_1, \dots, U_k \) proper subspaces of \( V \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that for each \( i \) there is a non-zero \( \varphi_i \in V^{*} \) with \( U_i \subseteq \ker\varphi_i \).
2. Let \( (\b_1, \dots, \b_n) \) be a basis of \( V \), and for \( t \in F \) put \( \v(t) = \b_1 + t\b_2 + t^2\b_3 + \dots + t^{n-1}\b_n \). Show that \( t \mapsto \varphi_i(\v(t)) \) is given by a non-zero polynomial of degree at most \( n - 1 \).
3. Deduce that some vector of \( V \) lies in none of \( U_1, \dots, U_k \). In other words, \( V \) is not a union of finitely many proper subspaces.
4. Show that the hypothesis that \( F \) is infinite cannot be dropped: over \( \nF_q \), the space \( \nF_q^2 \) is the union of \( q + 1 \) proper subspaces.
:::

*Hint: for (c), use @lem-root-bound.*
:::

::: {.solution}
(a) Since \( U_i \ne V \), pick \( \v \notin U_i \). By @lem-subspace-cut-out-by-annihilator there is \( \varphi_i \in U_i^{0} \) with \( \varphi_i(\v) \ne 0 \). Then \( \varphi_i \ne 0 \) and \( U_i \subseteq \ker\varphi_i \).

(b) By linearity, \( \varphi_i(\v(t)) = \sum_{j=1}^{n} \varphi_i(\b_j)\,t^{j-1} \), which is the value at \( t \) of the polynomial \( p_i(x) = \sum_{j=1}^{n} \varphi_i(\b_j)\,x^{j-1} \) of degree at most \( n - 1 \). Its coefficients are \( \varphi_i(\b_1), \dots, \varphi_i(\b_n) \), which are not all zero, since otherwise \( \varphi_i \) would vanish on a basis and be zero (@thm-linear-transform-basis). So \( p_i \ne 0 \).

(c) By @lem-root-bound, each \( p_i \) has at most \( n - 1 \) roots in \( F \), so together they have at most \( k(n - 1) \) roots. Since \( F \) is infinite, there is \( t_0 \in F \) that is a root of none of them. Then \( \varphi_i(\v(t_0)) = p_i(t_0) \ne 0 \), so \( \v(t_0) \notin \ker\varphi_i \supseteq U_i \), for every \( i \).

(d) \( \nF_q^2 \) has \( q^2 - 1 \) non-zero vectors, and each line through \( \0 \) contains \( q - 1 \) of them (the non-zero multiples of one vector). Two distinct lines meet only in \( \0 \), so there are \( (q^2 - 1)/(q - 1) = q + 1 \) lines, and every non-zero vector lies on one of them. Hence \( \nF_q^2 \) is the union of its \( q + 1 \) lines, each a proper subspace. For \( q = 2 \) these are \( \Span((1, 0)) \), \( \Span((0, 1)) \) and \( \Span((1, 1)) \), as in @exr-subspaces-c1. The proof of (c) breaks exactly where it used infinitely many \( t \): here \( k(n - 1) = q + 1 \) exceeds \( \lvert F \rvert = q \).
:::

::: {#exr-hyperplanes-and-systems-c2}
[C2: The least number of equations for a system]

Let \( A \in M_{m \times n}(F) \) and \( \b \in F^m \), and suppose the solution set \( S \) of \( A\x = \b \) is non-empty.

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( B \in M_{p \times n}(F) \), \( \c \in F^p \) and \( B\x = \c \) has the same solution set \( S \), then \( \nul(B) = \nul(A) \).
2. Deduce that every system with solution set \( S \) has at least \( \rank A \) equations, and that some system with solution set \( S \) has exactly \( \rank A \) equations.
3. Show by an example that (b) fails without the hypothesis \( S \ne \varnothing \).
:::
:::

::: {.solution}
(a) Fix \( \p \in S \). By @thm-general-solution-structure, \( S = \p + \nul(A) \) and also \( S = \p + \nul(B) \). For \( \h \in \nul(A) \), \( \p + \h \in S = \p + \nul(B) \), so \( \h \in \nul(B) \). Swapping the roles of \( A \) and \( B \) gives the reverse inclusion, so \( \nul(A) = \nul(B) \).

(b) Let \( k = \dim\nul(A) = n - \rank A \) (@thm-rank-nullity-matrix). If \( B\x = \c \) with \( p \) equations has solution set \( S \), then \( \nul(B) = \nul(A) \) by (a), so \( p \ge n - k = \rank A \) by @thm-subspace-is-solution-set (b). Conversely, take \( A_0 \in M_{(n-k) \times n}(F) \) with \( \nul(A_0) = \nul(A) \), which exists by @thm-subspace-is-solution-set (a) (if \( k = n \), take the empty system, whose solution set is \( F^n = S \)). By @prp-affine-subspace-intersection, or directly by @thm-general-solution-structure, the system \( A_0\x = A_0\p \) has solution set \( \p + \nul(A) = S \), and it has \( n - k = \rank A \) equations.

(c) Over any field, \( 0x_1 = 1 \) (in \( F^1 \)) has empty solution set and coefficient matrix of rank \( 0 \), yet no system with \( 0 \) equations has empty solution set, since the empty system is solved by every vector. So at least one equation is needed, which is more than \( \rank A = 0 \).
:::
