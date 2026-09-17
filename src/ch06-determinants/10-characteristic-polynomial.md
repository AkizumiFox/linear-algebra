# The Characteristic Polynomial

For a square matrix \( A \) over \( F \) and a scalar \( c \in F \), when is \( cI - A \) invertible? The question matters: \( cI - A \) fails to be invertible exactly when \( A\v = c\v \) for some non-zero vector \( \v \), the situation Chapter 8 is built around. The determinant answers the question for each single \( c \). This section lets \( c \) vary. Replacing the number \( c \) by a variable \( x \) turns \( \det(cI - A) \) into a polynomial, the characteristic polynomial, and the scalars we are looking for become its roots. The price is that \( xI - A \) is a matrix of **polynomials**, not of field elements, so we must check which determinant facts survive there. The remarks at the ends of §4, §5 and §6 did exactly that bookkeeping, and here we cash them in.

## From a number to a variable

Take \( A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \in M_2(\nQ) \). For each \( c \in \nQ \),
\[
\det(cI - A) = \det\begin{pmatrix} c - 1 & -2 \\ -3 & c - 4 \end{pmatrix} = (c - 1)(c - 4) - 6 = c^2 - 5c - 2 .
\]
The same expression \( c^2 - 5c - 2 \) appears whatever \( c \) is. It is the value at \( c \) of one polynomial, and that polynomial deserves a name. To define it directly, without first choosing \( c \), we put the variable \( x \) into the matrix and take the determinant of
\[
xI - A = \begin{pmatrix} x - 1 & -2 \\ -3 & x - 4 \end{pmatrix},
\]
a matrix whose entries lie in \( F[x] \).

Is that allowed? \( F[x] \) is not a field, but it is a **commutative ring** in the sense of the remark in §4: all the field axioms hold except the existence of inverses (@thm-polynomial-ring-laws). The Leibniz formula of @def-determinant uses only sums, differences and products of entries, so it defines \( \det M \in F[x] \) for every \( M \in M_n(F[x]) \).

*The characteristic polynomial of \( A \) is the determinant of \( xI - A \), computed with polynomial entries.*

::: {#def-characteristic-polynomial}
[Characteristic Polynomial]

Let \( n \ge 1 \) and \( A = (a_{ij}) \in M_n(F) \). The **characteristic polynomial** of \( A \) is
\[
p_A(x) \coloneqq \det(xI_n - A) = \sum_{\sigma \in S_n} \sgn(\sigma) \prod_{j=1}^{n} \big(x\,\delta_{\sigma(j)j} - a_{\sigma(j)j}\big) \ \in F[x],
\]
where \( \delta_{ij} = 1 \) if \( i = j \) and \( 0 \) otherwise, so that \( x\delta_{ij} - a_{ij} \) is the \( (i, j) \)-entry of \( xI_n - A \). The determinant is the Leibniz sum of @def-determinant, computed in the commutative ring \( F[x] \).
:::

In words: subtract \( A \) from \( x \) times the identity, so that \( x \) appears only on the diagonal; then take the determinant exactly as for a matrix of numbers, multiplying and adding polynomials instead of scalars. The result is **one** polynomial, not a number.

**Well-definedness.** Each term of the Leibniz sum is a product of \( n \) polynomials, and the sum is finite, so \( p_A \) is a polynomial. It depends only on \( A \).

**How to compute it.** By the remarks in §4, §5 and §6, the following results were proved without dividing, and so hold for matrices over \( F[x] \): @thm-det-transpose and @thm-det-triangular (§4), @thm-det-multiplicative by its first proof (§5), @thm-laplace-expansion (§6), and @thm-det-block-triangular (§8). So we may expand \( \det(xI - A) \) along any row or column, and read it off from triangular or block triangular shape. What we may **not** do is row reduce \( xI - A \) by dividing by a polynomial entry, as the warning below explains.

**Examples.**

- **\( 1 \times 1 \).** For \( A = (a) \), \( p_A(x) = x - a \).
- **\( 2 \times 2 \).** For \( A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \),
\[
p_A(x) = (x - a)(x - d) - bc = x^2 - (a + d)x + (ad - bc) = x^2 - (\tr A)\,x + \det A .
\]
For \( A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \) this is \( x^2 - 5x - 2 \), as above.
- **Triangular.** If \( A \) is upper or lower triangular, so is \( xI - A \), with diagonal entries \( x - a_{ii} \). By @thm-det-triangular over \( F[x] \), \( p_A(x) = (x - a_{11})(x - a_{22})\cdots(x - a_{nn}) \).
- **Degenerate cases.** The zero matrix has \( p_{0}(x) = x^n \), and the identity has \( p_{I_n}(x) = (x - 1)^n \); both are triangular. These two polynomials are different, although both matrices are as simple as possible, which already shows that \( p_A \) records something about \( A \).

::: {#exm-charpoly-small}
[A \( 3 \times 3 \) Characteristic Polynomial]

Find \( p_A \) for \( A = \begin{pmatrix} 2 & 0 & 1 \\ 1 & 3 & 1 \\ 1 & 0 & 2 \end{pmatrix} \in M_3(\nQ) \).
:::

::: {.solution}
We have
\[
xI - A = \begin{pmatrix} x - 2 & 0 & -1 \\ -1 & x - 3 & -1 \\ -1 & 0 & x - 2 \end{pmatrix}.
\]
Column \( 2 \) has a single non-zero entry, \( x - 3 \) in position \( (2, 2) \). Expanding along it (@thm-laplace-expansion over \( F[x] \)),
\[
p_A(x) = (x - 3)\,(-1)^{2+2}\det\begin{pmatrix} x - 2 & -1 \\ -1 & x - 2 \end{pmatrix} = (x - 3)\big((x - 2)^2 - 1\big) = (x - 1)(x - 3)^2 .
\]
Multiplied out, \( p_A(x) = x^3 - 7x^2 + 15x - 9 \). Compare with \( \tr A = 2 + 3 + 2 = 7 \) and \( \det A = 9 \) (expand \( A \) along column \( 2 \): \( 3(4 - 1) = 9 \)).
:::

**A companion-type example.** Let \( A = \begin{pmatrix} 0 & 0 & 6 \\ 1 & 0 & -11 \\ 0 & 1 & 6 \end{pmatrix} \), with ones just below the diagonal, a last column \( (6, -11, 6) \), and zeros elsewhere. Expanding \( xI - A = \begin{pmatrix} x & 0 & -6 \\ -1 & x & 11 \\ 0 & -1 & x - 6 \end{pmatrix} \) along the first row (@thm-laplace-expansion over \( F[x] \)),
\[
p_A(x) = x\det\begin{pmatrix} x & 11 \\ -1 & x - 6 \end{pmatrix} + (-6)\det\begin{pmatrix} -1 & x \\ 0 & -1 \end{pmatrix} = x(x^2 - 6x + 11) - 6 = x^3 - 6x^2 + 11x - 6 ,
\]
which factors as \( (x - 1)(x - 2)(x - 3) \). The last column of \( A \) lists the coefficients \( -6, 11, -6 \) of \( 1, x, x^2 \) in \( p_A \), with their signs changed. This is no accident: @exr-characteristic-polynomial-c1 shows that the same pattern works in every size.

**Non-example by minimal change.** Swap the order of subtraction: \( \det(A - xI) \). Each of the \( n \) columns of \( A - xI \) is \( -1 \) times the corresponding column of \( xI - A \), so by multilinearity \( \det(A - xI) = (-1)^n p_A(x) \). For \( A = (a) \) this is \( a - x \), whose leading coefficient is \( -1 \). What still works: the roots are the same. What fails: the result is **not monic** when \( n \) is odd.

**Why this definition.** Some books use \( \det(A - xI) \). We use \( xI - A \) so that the characteristic polynomial is always **monic** (@thm-charpoly-coefficients below), which makes statements like "\( p_A = (x - 1)(x - 3)^2 \)" true without sign bookkeeping. The name comes from the fact that the roots of this polynomial are the "characteristic values" of \( A \), which Chapter 8 calls eigenvalues.

::: {.warning}
**Do not row reduce \( xI - A \) by dividing by polynomials.** Over a field, a matrix with non-zero determinant is invertible (@thm-det-nonzero-iff-invertible), but that proof runs through elimination, which divides by pivots, and it fails over \( F[x] \). For \( A = (0) \in M_1(F) \), the matrix \( xI - A = (x) \) has determinant \( x \ne 0 \), yet it has no inverse in \( M_1(F[x]) \): if \( x\,q(x) = 1 \) for a polynomial \( q \), then \( q \ne 0 \), and \( 1 + \deg q = \deg 1 = 0 \) by @thm-degree-of-product, which is impossible since \( \deg q \ge 0 \). Likewise, "divide row \( 1 \) of \( xI - A \) by \( x - 1 \)" produces entries that are not polynomials and that make no sense at \( x = 1 \). Compute \( p_A \) by expansion, by triangular or block shape, or by the Leibniz formula.
:::

Before looking at the coefficients, we record the fact that makes \( p_A \) useful: evaluating it at a scalar \( c \) gives the same result as putting \( c \) in place of \( x \) before taking the determinant.

::: {#lem-charpoly-evaluation}
[Evaluating the Characteristic Polynomial]

Let \( A \in M_n(F) \) and \( c \in F \). Then \( p_A(c) = \det(cI_n - A) \).
:::

::: {.proof}
By @thm-evaluation-respects-operations, evaluation at \( c \) turns sums of polynomials into sums and products into products, and sends a constant \( a \) to \( a \). Applying it to the Leibniz sum in @def-characteristic-polynomial term by term,
\[
p_A(c) = \sum_{\sigma \in S_n} \sgn(\sigma)\prod_{j=1}^{n}\big(c\,\delta_{\sigma(j)j} - a_{\sigma(j)j}\big),
\]
and \( c\,\delta_{ij} - a_{ij} \) is the \( (i, j) \)-entry of \( cI_n - A \). By @def-determinant, the right side is \( \det(cI_n - A) \).
:::

## The shape of the characteristic polynomial

The \( 2 \times 2 \) example suggests a pattern: the leading coefficient is \( 1 \), the next coefficient is minus the trace, and the constant term is the determinant up to sign. The same holds in every size.

::: {#thm-charpoly-coefficients}
[Coefficients of the Characteristic Polynomial]

Let \( n \ge 1 \) and \( A \in M_n(F) \). Then \( p_A \) is **monic of degree \( n \)**, and
\[
p_A(x) = x^n - (\tr A)\,x^{n-1} + \dots + (-1)^n\det A,
\]
that is, the coefficient of \( x^{n-1} \) is \( -\tr A \) and the constant term is \( (-1)^n\det A \). (For \( n = 1 \) these two statements concern the same coefficient, and both say it is \( -a_{11} \).)
:::

::: {.idea}
Look at the Leibniz sum term by term and count powers of \( x \). A factor \( x\delta_{\sigma(j)j} - a_{\sigma(j)j} \) contains \( x \) only if \( \sigma(j) = j \). A permutation other than the identity moves at least **two** indices, so its term has degree at most \( n - 2 \) and cannot affect the top two coefficients. The identity contributes \( \prod_j(x - a_{jj}) \), whose top two coefficients are \( 1 \) and \( -\sum_j a_{jj} \). For the constant term, set \( x = 0 \).
:::

::: {.proof}
Write \( m_{ij} = x\delta_{ij} - a_{ij} \) for the entries of \( xI - A \). By @def-characteristic-polynomial, \( p_A = \sum_{\sigma} t_\sigma \) with \( t_\sigma = \sgn(\sigma)\prod_{j} m_{\sigma(j)j} \).

*Terms with \( \sigma \ne \id \).* If \( \sigma(j) \ne j \) for some \( j \), then \( \sigma(\sigma(j)) \ne \sigma(j) \), because \( \sigma \) is injective. So \( \sigma \) moves at least two indices, and at most \( n - 2 \) indices are fixed. For a moved index \( j \), \( m_{\sigma(j)j} = -a_{\sigma(j)j} \) has degree at most \( 0 \); for a fixed index it has degree at most \( 1 \). By @thm-degree-of-product, \( \deg t_\sigma \le n - 2 \).

*The term \( \sigma = \id \).* We show by induction on \( k \ge 1 \) that \( \prod_{j=1}^{k}(x - a_{jj}) = x^k - s_kx^{k-1} + r_k \) with \( s_k = a_{11} + \dots + a_{kk} \) and \( \deg r_k \le k - 2 \). For \( k = 1 \), take \( r_1 = 0 \). If it holds for \( k \), then with \( a = a_{k+1,k+1} \),
\[
(x^k - s_kx^{k-1} + r_k)(x - a) = x^{k+1} - (s_k + a)x^k + \big(s_kax^{k-1} + r_kx - ar_k\big),
\]
and the bracket has degree at most \( k - 1 \) by @thm-degree-of-sum and @thm-degree-of-product. This completes the induction. Since \( \sgn(\id) = 1 \), \( t_{\id} = x^n - (\tr A)\,x^{n-1} + r_n \) with \( \deg r_n \le n - 2 \).

Adding, \( p_A = x^n - (\tr A)\,x^{n-1} + \big(r_n + \sum_{\sigma \ne \id} t_\sigma\big) \), and the bracket has degree at most \( n - 2 \) by @thm-degree-of-sum. Hence \( p_A \) is monic of degree \( n \), with coefficient \( -\tr A \) at \( x^{n-1} \) (@def-trace).

*Constant term.* The constant term of a polynomial is its value at \( 0 \) (@def-polynomial-evaluation). By @lem-charpoly-evaluation with \( c = 0 \), \( p_A(0) = \det(-A) \). The matrix \( -A \) is obtained from \( A \) by multiplying each of its \( n \) columns by \( -1 \), so \( \det(-A) = (-1)^n\det A \) by @thm-det-row-operations (d). This proves the theorem.
:::

So the characteristic polynomial packages two invariants we already know, the trace and the determinant, and adds \( n - 2 \) more coefficients in between. For \( n = 2 \) nothing is in between, which is why \( p_A(x) = x^2 - (\tr A)x + \det A \) for every \( 2 \times 2 \) matrix.

::: {.check}
Without expanding any determinant, find the coefficient of \( x^2 \) and the constant term of \( p_A \) for \( A = \begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix} \), given that \( \det A = 2 \).
:::

::: {.solution}
By @thm-charpoly-coefficients, the coefficient of \( x^2 \) is \( -\tr A = 0 \), and the constant term is \( (-1)^3\det A = -2 \). (In full, \( p_A(x) = x^3 - 3x - 2 = (x - 2)(x + 1)^2 \).)
:::

## Similar matrices, same polynomial

Similar matrices describe the same operator in different bases (@thm-similar-iff-same-operator), so everything intrinsic to the operator should agree for them. The trace and determinant do (@thm-trace-similarity-invariant, @cor-det-similarity-invariant). The characteristic polynomial, which contains both, does too, and the proof is the proof for the determinant, run over \( F[x] \).

::: {#thm-charpoly-similarity-invariant}
[Similar Matrices Have the Same Characteristic Polynomial]

If \( A, B \in M_n(F) \) are similar, then \( p_A = p_B \).
:::

::: {.proof}
Let \( B = P^{-1}AP \) with \( P \in M_n(F) \) invertible. Regard \( P \), \( P^{-1} \), \( A \) and \( I \) as matrices over \( F[x] \) whose entries happen to be constants. The laws of matrix arithmetic in @thm-matrix-multiplication-properties are proved from the ring axioms alone, so they hold in \( M_n(F[x]) \). Hence
\[
P^{-1}(xI - A)P = x\,P^{-1}P - P^{-1}AP = xI - B .
\]
By @thm-det-multiplicative, valid over \( F[x] \) by the remark in §5,
\[
p_B = \det\big(P^{-1}(xI - A)P\big) = \det(P^{-1})\,\det(xI - A)\,\det P = \det(P^{-1})\det(P)\; p_A ,
\]
using commutativity of \( F[x] \) in the last step. Finally \( \det(P^{-1})\det P = \det(P^{-1}P) = \det I = 1 \) by @thm-det-multiplicative over \( F \). Hence \( p_B = p_A \).
:::

This is exactly the case singled out in the remark in §5: the proof of @cor-det-similarity-invariant survives over \( F[x] \) because \( P \) is invertible already over \( F \). The theorem lets us attach a characteristic polynomial to an operator.

::: {#def-charpoly-operator}
[Characteristic Polynomial of an Operator]

Let \( V \) be a vector space over \( F \) with \( \dim V = n \ge 1 \), and let \( T \in \cL(V) \). The **characteristic polynomial** of \( T \) is
\[
p_T(x) \coloneqq p_{[T]_{\sB}}(x) = \det\big(xI_n - [T]_{\sB}\big),
\]
where \( \sB \) is **any** basis of \( V \).
:::

This does not depend on \( \sB \): for bases \( \sB \) and \( \sC \), the matrices \( [T]_{\sB} \) and \( [T]_{\sC} \) are similar by @thm-similar-iff-same-operator (a), so they have the same characteristic polynomial by @thm-charpoly-similarity-invariant. By @thm-charpoly-coefficients, \( p_T \) is monic of degree \( \dim V \), with coefficient \( -\tr T \) at \( x^{n-1} \) and constant term \( (-1)^n\det T \) (@def-trace-operator, @def-det-operator).

::: {#exm-charpoly-operators}
[Characteristic Polynomials of Two Operators]

On \( V = \nR[x]_{\le 2} \), find the characteristic polynomials of differentiation \( D(q) = q' \) and of the shift \( S(q)(x) = q(x + 1) \).
:::

::: {.solution}
Use the basis \( \sB = (1, x, x^2) \). Since \( D(1) = 0 \), \( D(x) = 1 \), \( D(x^2) = 2x \), and \( S(1) = 1 \), \( S(x) = 1 + x \), \( S(x^2) = 1 + 2x + x^2 \),
\[
[D]_{\sB} = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix}, \qquad [S]_{\sB} = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix}.
\]
Both are upper triangular, so \( p_D(t) = t^3 \) and \( p_S(t) = (t - 1)^3 \). (We name the variable \( t \) here, since \( x \) is already the variable of the polynomials in \( V \).) As a check, \( \tr S = 3 \) and \( \det S = 1 \), matching the coefficient \( -3 \) of \( t^2 \) and the constant term \( (-1)^3 \cdot 1 \).
:::

::: {.warning}
**Equal characteristic polynomials do not make matrices similar.** The converse of @thm-charpoly-similarity-invariant is false. Recall the pair from the warning in Chapter 3, §7: \( I_2 \) and \( J = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) both have characteristic polynomial \( (x - 1)^2 \), since both are triangular with diagonal \( 1, 1 \). But \( I_2 \) is similar only to itself, so \( J \not\sim I_2 \). In particular the characteristic polynomial does not determine the matrix, not even up to similarity. Deciding similarity needs finer invariants; Chapter 9 finds a complete set.
:::

## Roots and singular matrices

We can now answer the opening question. The determinant tests invertibility of \( cI - A \) for one \( c \) at a time; the characteristic polynomial tests all \( c \) at once, and the answer is a finite set.

::: {#thm-charpoly-root-iff-singular}
[Roots of the Characteristic Polynomial]

Let \( A \in M_n(F) \) with \( n \ge 1 \), and let \( c \in F \).

::: {.enumerate options="label=(\alph*)"}
1. The following are equivalent: (i) \( p_A(c) = 0 \); (ii) \( cI - A \) is **not** invertible; (iii) there is a **non-zero** \( \v \in F^n \) with \( A\v = c\v \).
2. There are **at most \( n \)** scalars \( c \in F \) with these properties.
:::
:::

::: {.proof}
(a) By @lem-charpoly-evaluation, \( p_A(c) = \det(cI - A) \), which is a determinant of a matrix over the **field** \( F \). By @thm-det-nonzero-iff-invertible, it is zero if and only if \( cI - A \) is not invertible; this is (i) ⇔ (ii). By @thm-invertible-tfae, \( cI - A \) is not invertible if and only if \( (cI - A)\v = \0 \) for some \( \v \ne \0 \), and \( (cI - A)\v = c\v - A\v \) by @thm-matrix-multiplication-properties; this is (ii) ⇔ (iii).

(b) By @thm-charpoly-coefficients, \( p_A \) is monic of degree \( n \), in particular non-zero. By @cor-root-bound-general, it has at most \( n \) distinct roots in \( F \), and by (a) these are exactly the scalars in question.
:::

Notice where the evaluation happens: **first** substitute \( c \), getting a matrix over the field \( F \), **then** use the invertibility test, which is valid over fields. That order is what the warning about \( F[x] \) above requires.

The same holds for an operator \( T \) on \( V \) with \( \dim V = n \ge 1 \): \( p_T(c) = 0 \) if and only if \( c\,\id_V - T \) is not invertible, by (a) applied to \( [T]_{\sB} \) together with @thm-rank-map-equals-rank-matrix (b), since \( [c\,\id_V - T]_{\sB} = cI - [T]_{\sB} \).

The scalars \( c \) of this theorem are the **eigenvalues** of \( A \), and the vectors \( \v \) in (iii) its eigenvectors. They are the subject of Chapter 8, which starts from this theorem.

**Examples.**

- For \( A \) in @exm-charpoly-small, \( p_A = (x - 1)(x - 3)^2 \), so \( cI - A \) is singular exactly for \( c = 1 \) and \( c = 3 \). For instance \( 3I - A = \begin{pmatrix} 1 & 0 & -1 \\ -1 & 0 & -1 \\ -1 & 0 & 1 \end{pmatrix} \) has a zero column, and \( \v = \e_2 \) satisfies \( A\e_2 = 3\e_2 \).
- The rotation \( R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \) has \( p_R = x^2 + 1 \). Over \( \nR \) this has no root, so \( cI - R \) is invertible for **every** real \( c \): no non-zero real vector is merely stretched by a quarter-turn. Over \( \nC \), the roots \( \pm i \) appear, and for example \( R(1, -i) = (i, 1) = i\,(1, -i) \). The field matters.

::: {.check}
For which \( c \in \nQ \) is \( cI - A \) invertible, where \( A = \begin{pmatrix} 5 & -2 \\ 3 & 0 \end{pmatrix} \)?
:::

::: {.solution}
\( p_A(x) = x^2 - (\tr A)x + \det A = x^2 - 5x + 6 = (x - 2)(x - 3) \). By @thm-charpoly-root-iff-singular, \( cI - A \) is invertible exactly for \( c \ne 2, 3 \).
:::

## A tempting false proof

Here is a statement that is true, and important: **every square matrix satisfies its own characteristic polynomial**, \( p_A(A) = 0 \). This is the Cayley–Hamilton Theorem, proved in Chapter 8. Here \( p_A(A) \) means substituting the matrix \( A \) into the polynomial \( p_A \), replacing each \( x^k \) by \( A^k \) and the constant term \( a_0 \) by \( a_0I \) (@def-polynomial-of-matrix). For a \( 2 \times 2 \) matrix it says \( A^2 - (\tr A)A + (\det A)I = 0 \), which you can check by multiplying out.

A one-line "proof" suggests itself, and it is wrong.

::: {.warning}
**The fake proof of Cayley–Hamilton.** "Since \( p_A(x) = \det(xI - A) \), put \( x = A \): \( p_A(A) = \det(AI - A) = \det(0) = 0 \)." This is invalid for two reasons. First, the two sides are different kinds of object: \( p_A(A) \) is an \( n \times n \) **matrix**, while \( \det(\cdots) \) is a **scalar**, so "\( = 0 \)" compares a matrix with a number. Second, @lem-charpoly-evaluation lets us substitute only a **scalar** \( c \in F \) into the entries of \( xI - A \). Substituting a matrix for \( x \) inside the entries would produce a matrix whose entries are matrices, and "\( AI - A \)" silently treats the \( x \) in the entry \( x - a_{11} \) as if the entry became \( A - a_{11} \), which is not what substitution into a polynomial means.

The same "argument" proves false statements, which shows it is not a proof. Replace \( \det \) by \( \tr \): let \( q(x) = \tr(xI - A) = nx - \tr A \). The fake reasoning gives "\( q(A) = \tr(AI - A) = \tr 0 = 0 \)". But for \( A = \diag(1, 0) \), \( q(x) = 2x - 1 \) and \( q(A) = 2A - I = \diag(1, -1) \ne 0 \).
:::

## Exercises

### A. Check your understanding

:::: {#exr-characteristic-polynomial-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the characteristic polynomial of \( A \in M_n(F) \), and say in which ring its determinant is computed.
2. State the degree, leading coefficient, coefficient of \( x^{n-1} \) and constant term of \( p_A \).
3. True or false: \( \det(A - xI) = p_A(x) \) for every \( A \in M_3(F) \). Justify your answer.
4. True or false: if \( p_A = p_B \), then \( A \sim B \). Justify your answer.
5. What does \( p_A(c) = 0 \) say about the matrix \( cI - A \)? About vectors?
6. Explain in one sentence why "\( p_A(A) = \det(AI - A) = 0 \)" is not a proof.
:::
::::

::: {.solution}
(a) \( p_A(x) = \det(xI_n - A) \), the Leibniz sum computed in the commutative ring \( F[x] \) (@def-characteristic-polynomial).

(b) Degree \( n \), leading coefficient \( 1 \), coefficient \( -\tr A \) at \( x^{n-1} \), constant term \( (-1)^n\det A \) (@thm-charpoly-coefficients).

(c) False. \( \det(A - xI) = (-1)^3p_A(x) = -p_A(x) \), since each of the three columns changes sign. For \( A = 0 \), \( \det(-xI_3) = -x^3 \ne x^3 = p_A(x) \).

(d) False. \( I_2 \) and \( \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) both have \( p = (x - 1)^2 \) but are not similar.

(e) \( cI - A \) is not invertible; equivalently there is a non-zero \( \v \) with \( A\v = c\v \) (@thm-charpoly-root-iff-singular).

(f) \( p_A(A) \) is a matrix obtained by substituting \( A \) into a polynomial, while \( \det(AI - A) \) is a scalar, and substitution into the entries of \( xI - A \) is only justified for scalars (@lem-charpoly-evaluation).
:::

### B. Practice

:::: {#exr-characteristic-polynomial-b1}
[B1: Computing characteristic polynomials]

Find the characteristic polynomial of each matrix over \( \nQ \), factor it as far as possible over \( \nQ \), and check the trace and determinant against @thm-charpoly-coefficients.
\[
A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix}, \qquad
B = \begin{pmatrix} 2 & 1 & 0 & 0 \\ 0 & 2 & 0 & 0 \\ 0 & 0 & 1 & 3 \\ 0 & 0 & 1 & -1 \end{pmatrix}.
\]
Hence list the \( c \in \nQ \) for which \( cI - A \), respectively \( cI - B \), is not invertible.
::::

::: {.solution}
*For \( A \).* Expanding \( xI - A = \begin{pmatrix} x - 1 & -1 & 0 \\ 0 & x - 1 & -1 \\ -1 & 0 & x - 1 \end{pmatrix} \) along the first row (@thm-laplace-expansion over \( F[x] \)),
\[
p_A(x) = (x - 1)\big((x - 1)^2 - 0\big) - (-1)\big(0 - 1\big) + 0 = (x - 1)^3 - 1 = x^3 - 3x^2 + 3x - 2 .
\]
Check: \( -\tr A = -3 \); \( \det A = 1\cdot(1 - 0) - 1\cdot(0 - 1) + 0 = 2 \), and \( (-1)^3 \cdot 2 = -2 \). Since \( p_A(2) = 1 - 1 = 0 \), divide by \( x - 2 \): \( p_A = (x - 2)(x^2 - x + 1) \). The quadratic has discriminant \( 1 - 4 = -3 < 0 \), so no rational (indeed no real) root. By @thm-charpoly-root-iff-singular, \( cI - A \) is singular only for \( c = 2 \).

*For \( B \).* \( xI - B \) is block upper triangular with diagonal blocks \( xI - \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} \) and \( xI - \begin{pmatrix} 1 & 3 \\ 1 & -1 \end{pmatrix} \). By @thm-det-block-triangular over \( F[x] \) and the \( 2 \times 2 \) formula,
\[
p_B(x) = (x - 2)^2\,\big(x^2 - 0\cdot x + (-1 - 3)\big) = (x - 2)^2(x^2 - 4) = (x - 2)^3(x + 2) .
\]
Multiplied out, \( p_B = x^4 - 4x^3 + 16x - 16 \). Check: \( -\tr B = -(2 + 2 + 1 - 1) = -4 \); \( \det B = 4 \cdot (-4) = -16 \) by @thm-det-block-triangular, and \( (-1)^4(-16) = -16 \). So \( cI - B \) is singular exactly for \( c = 2 \) and \( c = -2 \).
:::

:::: {#exr-characteristic-polynomial-b2}
[B2: Transpose]

Prove that \( p_{A\tp} = p_A \) for every \( A \in M_n(F) \). Hence show that \( cI - A \) is invertible if and only if \( cI - A\tp \) is.
::::

::: {.solution}
By @thm-transpose-properties, \( (xI - A)\tp = xI\tp - A\tp = xI - A\tp \); these rules are proved entrywise from the ring axioms, so they hold over \( F[x] \). By @thm-det-transpose, which holds over \( F[x] \) by the remark in §4,
\[
p_{A\tp} = \det(xI - A\tp) = \det\big((xI - A)\tp\big) = \det(xI - A) = p_A .
\]
By @thm-charpoly-root-iff-singular, \( cI - A \) is not invertible exactly when \( p_A(c) = 0 \), which is exactly when \( p_{A\tp}(c) = 0 \), that is, when \( cI - A\tp \) is not invertible.
:::

:::: {#exr-characteristic-polynomial-b3}
[B3: \( AB \) and \( BA \)]

Let \( A, B \in M_n(F) \) with \( A \) invertible.

::: {.enumerate options="label=(\alph*)"}
1. Show that \( BA = A^{-1}(AB)A \), and deduce \( p_{AB} = p_{BA} \).
2. Deduce that \( \tr(AB) = \tr(BA) \) and \( \det(AB) = \det(BA) \) in this case.
3. Check (a) for \( A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \), \( B = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \), and note that \( AB \ne BA \).
:::

(Chapter 8 removes the hypothesis that \( A \) is invertible.)
::::

::: {.solution}
(a) By associativity, \( A^{-1}(AB)A = (A^{-1}A)(BA) = BA \). So \( BA \sim AB \) (@def-similar-matrices, with \( P = A \)), and \( p_{AB} = p_{BA} \) by @thm-charpoly-similarity-invariant.

(b) By @thm-charpoly-coefficients, the coefficient of \( x^{n-1} \) is \( -\tr(AB) \) in \( p_{AB} \) and \( -\tr(BA) \) in \( p_{BA} \); the constant terms are \( (-1)^n\det(AB) \) and \( (-1)^n\det(BA) \). Equal polynomials have equal coefficients.

(c) \( AB = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix} \) and \( BA = \begin{pmatrix} 0 & 0 \\ 1 & 1 \end{pmatrix} \), so \( AB \ne BA \). Both have trace \( 1 \) and determinant \( 0 \), so both characteristic polynomials are \( x^2 - x = x(x - 1) \).
:::

### C. Going deeper

:::: {#exr-characteristic-polynomial-c1}
[C1: Companion matrices]

Let \( n \ge 2 \) and \( p(x) = x^n + a_{n-1}x^{n-1} + \dots + a_1x + a_0 \in F[x] \). The **companion matrix** of \( p \) is the matrix \( C(p) \in M_n(F) \) with \( 1 \) in each position \( (i + 1, i) \) just below the diagonal, last column \( (-a_0, -a_1, \dots, -a_{n-1}) \), and \( 0 \) elsewhere:
\[
C(p) = \begin{pmatrix} 0 & 0 & \cdots & 0 & -a_0 \\ 1 & 0 & \cdots & 0 & -a_1 \\ 0 & 1 & \cdots & 0 & -a_2 \\ \vdots & & \ddots & & \vdots \\ 0 & 0 & \cdots & 1 & -a_{n-1} \end{pmatrix}.
\]
(The matrix \( C \) of @exr-polynomials-of-operators-b2 is \( C(x^3 - 2x^2 + x - 2) \).)

::: {.enumerate options="label=(\alph*)"}
1. Let \( M = xI - C(p) \). For each \( i \), show that deleting row \( i \) and column \( n \) of \( M \) leaves a block diagonal matrix whose blocks are an \( (i - 1) \times (i - 1) \) lower triangular matrix with diagonal \( x, \dots, x \) and an \( (n - i) \times (n - i) \) upper triangular matrix with diagonal \( -1, \dots, -1 \) (either block may be absent when \( i = 1 \) or \( i = n \)). Deduce that the cofactor \( C_{in} \) of \( M \) equals \( x^{i-1} \).
2. Deduce, by expanding along the last column, that \( p_{C(p)} = p \).
3. Verify (b) for \( p = x^4 + x^3 - 2x + 3 \) by writing \( C(p) \) and checking the coefficients predicted by @thm-charpoly-coefficients.
4. Deduce that every monic polynomial of degree \( n \ge 1 \) over \( F \) is the characteristic polynomial of some \( n \times n \) matrix over \( F \).
:::
::::

::: {.solution}
(a) The entries of \( M \) are: \( x \) at \( (j, j) \) for \( j < n \); \( -1 \) at \( (j + 1, j) \); \( a_{j-1} \) at \( (j, n) \) for \( j < n \); \( x + a_{n-1} \) at \( (n, n) \); \( 0 \) elsewhere. Delete row \( i \) and column \( n \). In the remaining matrix, rows \( 1, \dots, i - 1 \) have non-zero entries only in columns \( j - 1 \) and \( j \) for row \( j \), all at most \( i - 1 \); and rows \( i + 1, \dots, n \) have non-zero entries only in columns \( j - 1 \) and \( j \le n - 1 \), all at least \( i \). So the matrix is block diagonal with blocks on rows and columns \( \{1, \dots, i-1\} \) and on rows \( \{i + 1, \dots, n\} \), columns \( \{i, \dots, n - 1\} \). The first block has \( x \) on its diagonal and \( -1 \) just below it, so it is lower triangular. In the second block, row \( j \) of \( M \) (for \( j > i \)) has \( -1 \) in column \( j - 1 \), which is the diagonal position of the block, and \( x \) in column \( j \), one step to the right; so it is upper triangular with diagonal \( -1, \dots, -1 \). By @thm-det-block-triangular and @thm-det-triangular over \( F[x] \) (both division-free), the minor is \( M_{in} = x^{i-1}(-1)^{n-i} \), where an absent block contributes the factor \( 1 \) (for \( i = 1 \) or \( i = n \) the matrix is a single triangular block). Hence \( C_{in} = (-1)^{i+n}(-1)^{n-i}x^{i-1} = (-1)^{2n}x^{i-1} = x^{i-1} \).

(b) By @thm-laplace-expansion along column \( n \), valid over \( F[x] \),
\[
p_{C(p)} = \det M = \sum_{i=1}^{n-1} a_{i-1}\,x^{i-1} + (x + a_{n-1})\,x^{n-1} = a_0 + a_1x + \dots + a_{n-1}x^{n-1} + x^n = p .
\]

(c) Here \( a_3 = 1 \), \( a_2 = 0 \), \( a_1 = -2 \), \( a_0 = 3 \), so
\[
C(p) = \begin{pmatrix} 0 & 0 & 0 & -3 \\ 1 & 0 & 0 & 2 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & -1 \end{pmatrix}.
\]
Its trace is \( -1 \), so @thm-charpoly-coefficients predicts the coefficient \( 1 = a_3 \) at \( x^3 \), as in \( p \). Its determinant, expanding along the first row, whose only non-zero entry is \( -3 \) in position \( (1, 4) \), is \( (-3)(-1)^{1+4}\det I_3 = 3 \), since deleting row \( 1 \) and column \( 4 \) leaves \( I_3 \). So the predicted constant term is \( (-1)^4 \cdot 3 = 3 = a_0 \).

(d) For \( n \ge 2 \), take \( C(p) \) and use (b). For \( n = 1 \), \( p = x + a_0 \) is \( p_{(-a_0)} \).
:::

:::: {#exr-characteristic-polynomial-c2}
[C2: Nilpotent \( 2 \times 2 \) matrices]

Let \( A \in M_2(F) \) satisfy \( A^k = 0 \) for some \( k \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Show that the constant term of \( p_A \) is \( 0 \).
2. By multiplying out, verify that \( A^2 - (\tr A)A + (\det A)I = 0 \) for every \( A \in M_2(F) \).
3. Deduce that \( \tr A = 0 \), and hence \( p_A = x^2 \) and \( A^2 = 0 \).
4. Give an example showing that \( A^2 = 0 \) does not force \( A = 0 \).
:::
::::

::: {.solution}
(a) By @thm-det-multiplicative, \( (\det A)^k = \det(A^k) = \det 0 = 0 \), so \( \det A = 0 \) because a field has no zero divisors (@thm-field-basic-properties). The constant term is \( (-1)^2\det A = 0 \) by @thm-charpoly-coefficients.

(b) Let \( A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \). Then \( A^2 = \begin{pmatrix} a^2 + bc & ab + bd \\ ca + dc & bc + d^2 \end{pmatrix} \) and \( (a + d)A = \begin{pmatrix} a^2 + ad & ab + bd \\ ac + dc & ad + d^2 \end{pmatrix} \). The difference is \( \begin{pmatrix} bc - ad & 0 \\ 0 & bc - ad \end{pmatrix} = -(\det A)I \), as claimed.

(c) By (a) and (b), \( A^2 = (\tr A)A \). By induction, \( A^m = (\tr A)^{m-1}A \) for all \( m \ge 1 \): if it holds for \( m \), then \( A^{m+1} = (\tr A)^{m-1}A^2 = (\tr A)^mA \). If \( A = 0 \), then \( \tr A = 0 \). If \( A \ne 0 \), then \( 0 = A^k = (\tr A)^{k-1}A \) forces \( (\tr A)^{k-1} = 0 \), since a non-zero matrix times a scalar is zero only if the scalar is zero; here \( k \ge 2 \), because \( k = 1 \) would give \( A = 0 \). Hence \( \tr A = 0 \) by @thm-field-basic-properties (f), applied repeatedly. So \( p_A = x^2 - 0\cdot x + 0 = x^2 \), and \( A^2 = (\tr A)A = 0 \).

(d) \( A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) has \( A^2 = 0 \) and \( A \ne 0 \).
:::

:::: {#exr-characteristic-polynomial-c3}
[C3: Odd size over the reals]

Let \( n \) be odd and \( A \in M_n(\nR) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that there is \( c \in \nR \) and a non-zero \( \v \in \nR^n \) with \( A\v = c\v \).
2. Show by an example that (a) fails for \( n = 2 \).
3. Show that (a) holds for every \( A \in M_n(\nC) \) and every \( n \ge 1 \).
:::
::::

::: {.solution}
(a) By @thm-charpoly-coefficients, \( p_A \in \nR[x] \) has odd degree \( n \). By @cor-odd-degree-real-root, it has a real root \( c \). By @thm-charpoly-root-iff-singular, there is a non-zero \( \v \in \nR^n \) with \( A\v = c\v \).

(b) The rotation \( R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \) has \( p_R = x^2 + 1 \), with no real root; by @thm-charpoly-root-iff-singular no real \( c \) and non-zero real \( \v \) satisfy \( R\v = c\v \).

(c) \( p_A \in \nC[x] \) has degree \( n \ge 1 \), so it has a root \( c \in \nC \) by @thm-fundamental-theorem-of-algebra. Apply @thm-charpoly-root-iff-singular over \( F = \nC \).
:::
