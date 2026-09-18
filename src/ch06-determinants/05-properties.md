# Row Operations and Multiplicativity

The previous section defined the determinant by the Leibniz formula and proved it is the only normalized alternating form. The formula settles every theoretical question in principle, but with \( n! \) terms it is useless for computing, and it hides the two facts that make determinants worth having. The first is that \( \det \A \ne 0 \) exactly when \( \A \) is invertible. The second is that \( \det(\A\B) = \det \A \det \B \). This section proves both. Along the way we get a fast algorithm, and we extend the determinant from matrices to operators.

## Row operations

Row reduction is the workhorse of Chapter 2, and the three rules of a determinant say precisely how it reacts to each elementary row operation. Everything follows from @thm-det-transpose, which lets us treat \( \det \) as a function of the rows.

::: {#thm-det-row-operations}
[Row Operations and the Determinant]

Let \( \A \in M_n(F) \) and let \( \B \) be obtained from \( \A \) by one operation.

::: {.enumerate options="label=(\alph*)"}
1. **(Swap)** If \( \B \) is obtained by \( R_i \leftrightarrow R_j \) with \( i \ne j \), then \( \det \B = -\det \A \).
2. **(Scale)** If \( \B \) is obtained by \( R_i \to cR_i \) with \( c \in F \), then \( \det \B = c \det \A \).
3. **(Replace)** If \( \B \) is obtained by \( R_i \to R_i + cR_j \) with \( i \ne j \) and \( c \in F \), then \( \det \B = \det \A \).
4. The same three statements hold for the corresponding operations on **columns**.
5. For the elementary matrices of @def-elementary-matrix,
   \[
   \det \P_{ij} = -1, \qquad \det \D_i(c) = c, \qquad \det(\I_n + c\E_{ij}) = 1 \quad (i \ne j),
   \]
   and \( \det(\E\A) = \det \E \det \A \) for every elementary matrix \( \E \in M_n(F) \).
:::
:::

::: {.proof}
By @thm-det-transpose, \( \det \) is an alternating \( n \)-linear function of the rows \( \r_1, \dots, \r_n \) of \( \A \). We write \( \det(\r_1, \dots, \r_n) \) for it in this proof.

(b) This is linearity in row \( i \).

(c) By linearity in row \( i \),
\[
\det \B = \det(\dots, \r_i + c\r_j, \dots, \r_j, \dots) = \det(\dots, \r_i, \dots, \r_j, \dots) + c \det(\dots, \r_j, \dots, \r_j, \dots),
\]
where the displayed arguments sit in positions \( i \) and \( j \). The last determinant has two equal rows, so it is \( 0 \). Hence \( \det \B = \det \A \).

(a) This is the swap rule of @thm-alternating-properties, applied to the rows.

(d) By @thm-leibniz-formula-alternating, \( \det \) is an alternating \( n \)-linear function of the columns, and the arguments for (a), (b), (c) apply word for word.

(e) The matrices \( \P_{ij} \), \( \D_i(c) \) and \( \I_n + c\E_{ij} \) are obtained from \( \I_n \) by a swap, a scaling and a replacement respectively. By (a), (b), (c) and \( \det \I_n = 1 \), their determinants are \( -1 \), \( c \) and \( 1 \). Now let \( \E = \rho(\I_n) \) be elementary. By @thm-row-op-is-left-multiplication, \( \E\A = \rho(\A) \). By (a), (b) or (c), \( \det \rho(\A) \) is \( \det \A \) times \( -1 \), \( c \) or \( 1 \) respectively, and this factor is \( \det \E \). Hence \( \det(\E\A) = \det \E \det \A \). This proves the theorem.
:::

Read part (e) as a bookkeeping rule. A swap flips the sign, a scaling by \( c \) multiplies by \( c \), and a replacement changes nothing. Replacement, the operation used most in elimination, is free.

::: {.warning}
**A combined move is not a replacement.** The move \( R_2 \to 3R_2 - R_1 \) looks harmless but multiplies the determinant by \( 3 \): it is the scaling \( R_2 \to 3R_2 \) followed by the replacement \( R_2 \to R_2 - R_1 \). For \( \A = \begin{pmatrix} 1 & 2 \\ 1 & 3 \end{pmatrix} \), with \( \det \A = 1 \), it produces \( \begin{pmatrix} 1 & 2 \\ 2 & 7 \end{pmatrix} \), whose determinant is \( 3 \). Keep replacements in the form "row \( i \) plus a multiple of another row", with coefficient \( 1 \) on row \( i \).
:::

Since elimination brings any square matrix to an upper triangular one, and triangular determinants are products of diagonal entries (@thm-det-triangular), we have an algorithm.

::: {#exm-det-by-elimination}
[A \( 4 \times 4 \) Determinant by Elimination]

Compute \( \det \A \) for
\[
\A = \begin{pmatrix} 0 & 2 & 4 & 2 \\ 1 & 1 & 0 & 3 \\ 2 & 3 & 1 & 5 \\ -1 & 2 & 3 & 1 \end{pmatrix} \in M_4(\nR).
\]
:::

::: {.solution}
We record each operation and its effect, using @thm-det-row-operations.

**Step 1.** The \( (1,1) \)-entry is \( 0 \), so swap: \( R_1 \leftrightarrow R_2 \). This multiplies the determinant by \( -1 \):
\[
\det \A = -\det \begin{pmatrix} 1 & 1 & 0 & 3 \\ 0 & 2 & 4 & 2 \\ 2 & 3 & 1 & 5 \\ -1 & 2 & 3 & 1 \end{pmatrix}.
\]

**Step 2.** Clear column \( 1 \) with the replacements \( R_3 \to R_3 - 2R_1 \) and \( R_4 \to R_4 + R_1 \), which change nothing. Row \( 2 \) has a common factor \( 2 \); pulling it out is linearity in row \( 2 \):
\[
\det \A = -\det \begin{pmatrix} 1 & 1 & 0 & 3 \\ 0 & 2 & 4 & 2 \\ 0 & 1 & 1 & -1 \\ 0 & 3 & 3 & 4 \end{pmatrix} = -2 \det \begin{pmatrix} 1 & 1 & 0 & 3 \\ 0 & 1 & 2 & 1 \\ 0 & 1 & 1 & -1 \\ 0 & 3 & 3 & 4 \end{pmatrix}.
\]

**Step 3.** Clear column \( 2 \): \( R_3 \to R_3 - R_2 \) and \( R_4 \to R_4 - 3R_2 \). Then clear column \( 3 \): \( R_4 \to R_4 - 3R_3 \). None of these changes the determinant:
\[
\det \A = -2 \det \begin{pmatrix} 1 & 1 & 0 & 3 \\ 0 & 1 & 2 & 1 \\ 0 & 0 & -1 & -2 \\ 0 & 0 & -3 & 1 \end{pmatrix} = -2 \det \begin{pmatrix} 1 & 1 & 0 & 3 \\ 0 & 1 & 2 & 1 \\ 0 & 0 & -1 & -2 \\ 0 & 0 & 0 & 7 \end{pmatrix}.
\]

**Step 4.** The last matrix is upper triangular, so by @thm-det-triangular its determinant is \( 1 \cdot 1 \cdot (-1) \cdot 7 = -7 \). Hence \( \det \A = -2 \cdot (-7) = 14 \).
:::

Elimination costs roughly \( n^3/3 \) arithmetic operations, and reading off the triangular determinant takes only \( n - 1 \) more multiplications, against \( n! \, (n-1) \) multiplications for the Leibniz formula (@exr-existence-and-uniqueness-c2). For \( n = 20 \) that is a few thousand operations against about \( 4.6 \times 10^{19} \). Every practical determinant computation is some form of elimination.

## Determinant and invertibility

The same bookkeeping answers the invertibility question. Row reduction multiplies the determinant by non-zero factors only, so it cannot turn a non-zero determinant into zero or back. And the end of the reduction is either \( \I_n \) or a matrix with a zero row.

::: {#thm-det-nonzero-iff-invertible}
[Invertible if and only if Non-Zero Determinant]

A matrix \( \A \in M_n(F) \) is invertible if and only if \( \det \A \ne 0 \).
:::

::: {.proof}
Let \( \R \) be the reduced row echelon form of \( \A \) (@thm-rref-exists, @thm-rref-unique). By @def-row-equivalent and @thm-row-op-is-left-multiplication, there are elementary matrices \( \E_1, \dots, \E_k \) (possibly \( k = 0 \)) with \( \R = \E_k \cdots \E_1 \A \). Applying @thm-det-row-operations (e) \( k \) times,
\[
\det \R = \det \E_k \cdots \det \E_1 \det \A .
\]
Each \( \det \E_m \) is \( -1 \), \( 1 \), or some \( c \ne 0 \), since a scaling operation requires \( c \ne 0 \). A product of non-zero elements of a field is non-zero (@thm-field-basic-properties), so \( \det \R = 0 \) if and only if \( \det \A = 0 \).

By @lem-square-rref-identity-or-zero-row, either \( \R = \I_n \), and then \( \det \R = 1 \ne 0 \); or the last row of \( \R \) is zero. In the second case, scaling that row by \( 0 \) leaves \( \R \) unchanged, so \( \det \R = 0 \cdot \det \R = 0 \) by @thm-det-row-operations (b). Hence \( \det \A \ne 0 \) if and only if \( \R = \I_n \), which by @thm-invertible-tfae holds if and only if \( \A \) is invertible.
:::

This is the promised addition to the list of equivalent conditions. We collect it with the conditions from Chapter 3 about the map \( T_{\A} \colon \x \mapsto \A\x \), and with two conditions about rows that the determinant makes easy.

::: {#thm-invertible-tfae-det}
[Invertible Matrix Theorem, with Determinants]

Let \( \A \in M_n(F) \) and \( T_{\A} \colon F^n \to F^n \), \( \x \mapsto \A\x \). The following are equivalent, and each is equivalent to each of the eight conditions of @thm-invertible-tfae.

::: {.enumerate options="label=(\alph*)"}
1. \( \A \) is invertible.
2. \( T_{\A} \) is injective.
3. \( T_{\A} \) is surjective.
4. \( \rank \A = n \).
5. \( \A\tp \) is invertible.
6. The rows of \( \A \) are linearly independent.
7. \( \det \A \ne 0 \).
:::
:::

::: {.proof}
Item (a) is item (a) of @thm-invertible-tfae, so it suffices to connect each new item with that theorem.

**(a) ⇔ (g).** This is @thm-det-nonzero-iff-invertible.

**(a) ⇔ (b).** By @thm-invertible-operator-tfae ((b) ⇔ (c)) with \( V = F^n \), \( T_{\A} \) is injective if and only if \( \ker T_{\A} = \{\x : \A\x = \0\} \) is \( \{\0\} \). That is item (b) of @thm-invertible-tfae.

**(b) ⇔ (c).** This is @thm-invertible-operator-tfae ((b) ⇔ (d)), since \( F^n \) is finite-dimensional.

**(c) ⇔ (d).** By @thm-matrix-times-vector-columns, \( \im T_{\A} \) is the set of combinations of the columns of \( \A \), that is, \( \col(\A) \). So \( T_{\A} \) is surjective if and only if \( \col(\A) = F^n \). Since \( \col(\A) \) is a subspace of \( F^n \), this holds if and only if \( \rank \A = \dim \col(\A) = n \) (@def-rank-matrix, @thm-dim-impl-eq).

**(a) ⇔ (e).** By @thm-det-transpose, \( \det \A\tp = \det \A \). Applying (a) ⇔ (g) to \( \A \) and to \( \A\tp \), both "\( \A \) invertible" and "\( \A\tp \) invertible" are equivalent to \( \det \A \ne 0 \).

**(e) ⇔ (f).** Let \( \r_1, \dots, \r_n \) be the rows of \( \A \). The columns of \( \A\tp \) are \( \r_1\tp, \dots, \r_n\tp \). By @thm-transpose-properties, \( c_1\r_1 + \dots + c_n\r_n = \0 \) if and only if \( c_1\r_1\tp + \dots + c_n\r_n\tp = \0 \), so the rows of \( \A \) are independent exactly when the columns of \( \A\tp \) are. By @thm-invertible-tfae ((a) ⇔ (f)) applied to \( \A\tp \), this holds exactly when \( \A\tp \) is invertible. This proves the theorem.
:::

The determinant is now one more item on the menu, and for the right problems it is the best one. For a concrete matrix with a parameter, one polynomial in the parameter decides invertibility at once. For an abstract matrix, such as \( \A + \I \) when \( \A^k = 0 \), the determinant is usually hopeless, and the kernel is the item to try first.

::: {.check}
For which \( t \in \nR \) is \( \begin{pmatrix} 1 & t \\ t & 4 \end{pmatrix} \) invertible? Over \( \nF_3 \), for which \( t \)?
:::

::: {.solution}
The determinant is \( 4 - t^2 = (2 - t)(2 + t) \). Over \( \nR \) the matrix is invertible exactly for \( t \ne \pm 2 \). Over \( \nF_3 \), \( 4 = 1 \), so the determinant is \( 1 - t^2 \), which is \( 1 \) for \( t = 0 \) and \( 0 \) for \( t = 1, 2 \); the matrix is invertible only for \( t = 0 \).
:::

## Multiplicativity

Now the second fact. A natural first attempt is to multiply out the Leibniz formula for \( \A\B \), whose entries are sums, and regroup. That is legitimate, but the bookkeeping is horrible. The uniqueness theorem does the work instead: we exhibit \( \B \mapsto \det(\A\B) \) as an alternating form in the columns of \( \B \), and then it has no choice.

::: {#thm-det-multiplicative}
[Multiplicativity of the Determinant]

For all \( \A, \B \in M_n(F) \),
\[
\det(\A\B) = \det \A \det \B .
\]
:::

::: {.idea}
Fix \( \A \). The \( j \)-th column of \( \A\B \) is \( \A\b_j \), so \( g(\b_1, \dots, \b_n) = \det(\A\b_1, \dots, \A\b_n) \) is \( \det(\A\B) \) viewed as a function of the columns of \( \B \). It inherits linearity in each \( \b_j \) from \( \det \) and from matrix multiplication, and equal columns \( \b_p = \b_q \) give equal columns \( \A\b_p = \A\b_q \). So \( g \) is an alternating form, hence a multiple of \( \det \), and the multiple is \( g(\e_1, \dots, \e_n) = \det \A \).
:::

::: {.proof}
Fix \( \A \in M_n(F) \), and define \( g \colon F^n \times \dots \times F^n \to F \) by
\[
g(\b_1, \dots, \b_n) = \det(\A\b_1, \dots, \A\b_n).
\]
By @thm-three-views-of-product (columns), if \( \B \) has columns \( \b_1, \dots, \b_n \), then \( \A\B \) has columns \( \A\b_1, \dots, \A\b_n \), so \( g(\b_1, \dots, \b_n) = \det(\A\B) \).

*\( g \) is \( n \)-linear.* Fix \( k \) and all \( \b_j \) with \( j \ne k \). The map \( \b_k \mapsto \A\b_k \) is linear by @thm-matrix-multiplication-properties, and \( \det \) is linear in its \( k \)-th argument by @thm-leibniz-formula-alternating. A composite of linear maps is linear, so \( g \) is linear in \( \b_k \).

*\( g \) is alternating.* If \( \b_p = \b_q \) with \( p \ne q \), then \( \A\b_p = \A\b_q \), so \( g(\b_1, \dots, \b_n) = 0 \) since \( \det \) is alternating.

By @cor-alternating-forms-one-dimensional, \( g(\b_1, \dots, \b_n) = g(\e_1, \dots, \e_n) \det(\b_1, \dots, \b_n) \). Finally \( \A\e_j \) is the \( j \)-th column of \( \A \) (@thm-matrix-times-vector-columns), so \( g(\e_1, \dots, \e_n) = \det \A \). Hence \( \det(\A\B) = \det \A \det \B \).
:::

::: {.remark}
**Over a commutative ring.** This proof uses only @cor-alternating-forms-one-dimensional (in the explicit form of @thm-alternating-form-uniqueness), linearity of matrix multiplication, and the Leibniz formula. None of these divides. So \( \det(\A\B) = \det \A \det \B \) holds for \( \A, \B \in M_n(R) \) over any commutative ring \( R \), such as \( F[x] \).
:::

Alternatively, the building blocks of Chapter 2 give a proof. If \( \A \) is invertible, then \( \A = \E_1 \cdots \E_k \) with elementary \( \E_m \) (@thm-invertible-tfae (d)), and peeling off one factor at a time with @thm-det-row-operations (e) gives \( \det(\A\B) = \det \E_1 \cdots \det \E_k \det \B \); the case \( \B = \I_n \) of the same computation shows \( \det \A = \det \E_1 \cdots \det \E_k \). If \( \A \) is not invertible, neither is \( \A\B \): otherwise \( (\A\B)\C = \I_n \) for some \( \C \), so \( \A(\B\C) = \I_n \) and \( \A \) would be invertible by @thm-one-sided-inverse. Then both sides are \( 0 \) by @thm-det-nonzero-iff-invertible. This route leans on row reduction, which divides, so unlike the first proof it needs a field.

For reference, here are the two identities used most often, now both proved.

::: {#thm-det-properties}
[Properties of Determinants]

Let \( \A, \B \in M_n(F) \). Then:

1. \( \det(\A\B) = \det \A \det \B \);
2. \( \det \A\tp = \det \A \).
:::

::: {.proof}
Part 1 is @thm-det-multiplicative and part 2 is @thm-det-transpose.
:::

The first consequences are immediate.

::: {#cor-det-inverse}
[Determinant of the Inverse]

If \( \A \in M_n(F) \) is invertible, then \( \det \A \ne 0 \) and \( \det(\A^{-1}) = (\det \A)^{-1} \).
:::

::: {.proof}
By @thm-det-multiplicative, \( \det \A \det(\A^{-1}) = \det(\A\A^{-1}) = \det \I_n = 1 \). Hence \( \det \A \ne 0 \), and \( \det(\A^{-1}) \) is the inverse of \( \det \A \) in \( F \).
:::

::: {.warning}
**Multiplicativity does not make \( \det \) additive, and it does not make products commute.** For \( \A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \) and \( \B = \begin{pmatrix} 0 & 1 \\ 1 & 5 \end{pmatrix} \), \( \A\B = \begin{pmatrix} 2 & 11 \\ 4 & 23 \end{pmatrix} \ne \begin{pmatrix} 3 & 4 \\ 16 & 22 \end{pmatrix} = \B\A \), yet \( \det(\A\B) = \det(\B\A) = 2 \), since both equal \( \det \A \det \B = (-2)(-1) \). On the other hand, \( \det(\A + \B) \) is not determined by \( \det \A \) and \( \det \B \) at all: \( \I_2 \) and \( \I_2 \) have determinants \( 1, 1 \) and \( \det(\I_2 + \I_2) = 4 \), while \( \I_2 \) and \( \C = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} \) also have determinants \( 1, 1 \) but \( \det(\I_2 + \C) = \det \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix} = 2 \).
:::

::: {.check}
Let \( \A = \begin{pmatrix} 2 & 1 \\ 7 & 4 \end{pmatrix} \). Without multiplying any matrices, find \( \det(\A^5) \), \( \det(\A^{-1}) \) and \( \det(\A\tp \A) \).
:::

::: {.solution}
\( \det \A = 8 - 7 = 1 \). By @thm-det-multiplicative, \( \det(\A^5) = (\det \A)^5 = 1 \). By @cor-det-inverse, \( \det(\A^{-1}) = 1^{-1} = 1 \). By @thm-det-properties, \( \det(\A\tp \A) = \det \A\tp \det \A = (\det \A)^2 = 1 \).
:::

## The determinant of an operator

In Chapter 3 the trace passed from matrices to operators because similar matrices have the same trace (@def-trace-operator). Multiplicativity gives the same for determinants.

::: {#cor-det-similarity-invariant}
[Determinant Is a Similarity Invariant]

If \( \A, \B \in M_n(F) \) are similar, then \( \det \A = \det \B \).
:::

::: {.proof}
Let \( \B = \P^{-1}\A\P \) with \( \P \) invertible. By @thm-det-multiplicative and @cor-det-inverse,
\[
\det \B = \det(\P^{-1}) \det \A \det \P = (\det \P)^{-1} \det \P \det \A = \det \A,
\]
where the middle step uses commutativity of multiplication in \( F \).
:::

The converse fails: \( \I_2 \) and \( \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) both have determinant \( 1 \), but the only matrix similar to \( \I_2 \) is \( \P^{-1}\I_2\P = \I_2 \) itself.

By @thm-similar-iff-same-operator, all matrices of one operator in the various bases are similar to each other. So the corollary lets us define:

::: {#def-det-operator}
[Determinant of an operator]

Let \( V \) be a finite-dimensional vector space over \( F \) with \( \dim V \ge 1 \), and let \( T \in \cL(V) \). The **determinant** of \( T \) is
\[
\det T \coloneqq \det [T]_{\sB},
\]
where \( \sB \) is **any** basis of \( V \). For \( V = \{\0\} \) we set \( \det T = 1 \).
:::

**Well-definedness.** If \( \sB \) and \( \sC \) are bases of \( V \), then \( [T]_{\sC} = \P^{-1}[T]_{\sB}\P \) with \( \P = \mtx{\id}{\sC}{\sB} \) invertible, by @thm-change-of-basis-maps and @thm-similar-iff-same-operator (a). By @cor-det-similarity-invariant the two determinants agree. The convention for \( V = \{\0\} \) is the empty product, and it keeps the next theorem true in that case.

**Examples.**

- **Scalars.** For \( c \in F \) and \( \dim V = n \ge 1 \), \( [c\,\id_V]_{\sB} = c\I_n \) in every basis, so \( \det(c\,\id_V) = c^n \) by @thm-det-triangular.
- **A reflection.** \( R(x, y) = (y, x) \) on \( \nR^2 \) has standard matrix \( \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \), of determinant \( -1 \). In the basis \( ((1, 1), (1, -1)) \) its matrix is \( \diag(1, -1) \) (@exm-reflection-diagonal-basis), again of determinant \( -1 \), as it must be.
- **Differentiation.** On \( \nR[x]_{\le 3} \) with basis \( (1, x, x^2, x^3) \), the matrix of \( \D \) is upper triangular with zero diagonal (@exm-matrix-of-differentiation), so \( \det \D = 0 \).

The determinant of a map \( T \colon V \to W \) between **different** spaces is not defined, even when \( \dim V = \dim W \). A matrix \( \mtx{T}{\sB}{\sC} \) exists, but changing \( \sC \) alone multiplies it on the left by an arbitrary invertible matrix, which can change its determinant to any non-zero value. For \( \id \colon \nR^2 \to \nR^2 \) with input basis \( \sE \) and output basis \( ((2, 0), (0, 1)) \), the matrix is \( \diag(\frac12, 1) \), of determinant \( \frac12 \), not \( 1 \).

::: {#thm-det-operator-properties}
[Properties of the Determinant of an Operator]

Let \( V \) be a finite-dimensional vector space over \( F \) and \( S, T \in \cL(V) \). Then
\[
\det(ST) = \det S \det T, \qquad \det \id_V = 1,
\]
and \( T \) is invertible if and only if \( \det T \ne 0 \).
:::

::: {.proof}
If \( V = \{\0\} \), all determinants are \( 1 \) and the only operator is \( \id_V \), which is invertible. Otherwise fix a basis \( \sB \) of \( V \). By @thm-matrix-of-composition, \( [ST]_{\sB} = [S]_{\sB}[T]_{\sB} \), so \( \det(ST) = \det S \det T \) by @thm-det-multiplicative. Next \( [\id_V]_{\sB} = \I_n \), of determinant \( 1 \). Finally, by @thm-rank-map-equals-rank-matrix (b), \( T \) is invertible if and only if \( [T]_{\sB} \) is, which by @thm-det-nonzero-iff-invertible holds if and only if \( \det T = \det [T]_{\sB} \ne 0 \).
:::

So the determinant is a property of the operator, not of the coordinates. Differentiation on \( \nR[x]_{\le 3} \) is not invertible because its determinant is \( 0 \), whichever basis we compute in. In the section on orientation and volume we will see what the number \( \det T \) measures geometrically.

## The determinant as a homomorphism

In Chapter 0 we met groups and homomorphisms, and promised that the determinant would be one. The general linear group \( \GL_n(F) \) is the group of invertible matrices in \( M_n(F) \) under multiplication, and \( F \setminus \{0\} \) is a group under multiplication (@exm-groups).

::: {#thm-det-homomorphism}
[The Determinant Is a Group Homomorphism]

Let \( n \ge 1 \). The determinant restricts to a **surjective** group homomorphism
\[
\det \colon \GL_n(F) \to F \setminus \{0\}.
\]
Its kernel is the **special linear group** \( \SL_n(F) \coloneqq \{ \A \in M_n(F) : \det \A = 1 \} \), which is therefore a subgroup of \( \GL_n(F) \).
:::

::: {.proof}
By @thm-det-nonzero-iff-invertible, \( \det \A \ne 0 \) for \( \A \in \GL_n(F) \), so \( \det \) maps \( \GL_n(F) \) into \( F \setminus \{0\} \), and @thm-det-multiplicative says it is a homomorphism (@def-group-homomorphism). For \( c \ne 0 \), the matrix \( \diag(c, 1, \dots, 1) \) has determinant \( c \) by @thm-det-triangular, which is non-zero, so it lies in \( \GL_n(F) \); hence \( \det \) is surjective. A matrix with determinant \( 1 \) is invertible by @thm-det-nonzero-iff-invertible, so the kernel \( \{\A \in \GL_n(F) : \det \A = 1\} \) is \( \SL_n(F) \). It is a subgroup by @thm-homomorphism-basic-properties.
:::

For example, \( \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) and the elementary matrices \( \I_n + c\E_{ij} \) lie in \( \SL_n(F) \), while \( \P_{12} \), of determinant \( -1 \), does not. Over \( \nR \), the rotation matrices \( \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} \) have determinant \( \cos^2\theta + \sin^2\theta = 1 \) and lie in \( \SL_2(\nR) \). The sign \( \sgn \colon S_n \to \{1, -1\} \) of the third section is the other homomorphism promised in Chapter 0, and the two are linked: \( \det \P_\sigma = \sgn(\sigma) \) (@exr-existence-and-uniqueness-b2), and \( \P_\sigma \P_\tau = \P_{\sigma\tau} \) (@lem-permutation-matrices).

## Which proofs survive over a ring

::: {.remark}
**Commutative rings.** Over a commutative ring \( R \) (as in the remark at the end of the previous section), the following proofs of this section use no division and remain valid for matrices in \( M_n(R) \): @thm-det-row-operations, with \( c \in R \) arbitrary in (b) and (c); @thm-det-multiplicative, by its first proof; and @thm-det-properties. The proofs of @cor-det-inverse and @cor-det-similarity-invariant also survive for matrices that have an inverse in \( M_n(R) \) (then \( \det \A \det(\A^{-1}) = 1 \), so \( \det \A \) has an inverse in \( R \)), for instance an invertible \( \P \in M_n(F) \) regarded inside \( M_n(F[x]) \); this is the case needed for characteristic polynomials. What fails over a ring is the converse direction: a matrix whose determinant is non-zero need not be invertible, since \( \det \) may be a non-zero element with no inverse, such as \( 2 \in \nZ \) or \( x \in F[x] \). By contrast, @thm-det-nonzero-iff-invertible, @thm-invertible-tfae-det and the "Alternatively" proof of multiplicativity run through row reduction, which divides by pivots, and they are proved here only over a field.
:::

## Exercises

### A. Check your understanding

::: {#exr-properties-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State how each of the three elementary row operations changes the determinant.
2. True or false: the move \( R_2 \to 3R_2 - R_1 \) does not change the determinant. Justify your answer.
3. True or false: if \( \A, \B \in M_n(F) \) have \( \det \A = \det \B \), then \( \A \) and \( \B \) are similar. Justify your answer.
4. True or false: \( \det(\A\B) = \det(\B\A) \) for all \( \A, \B \in M_n(F) \). Justify your answer.
5. Explain why \( \det T \) does not depend on the basis used to compute it.
6. Is \( \det \colon M_n(F) \to F \) a group homomorphism? Explain.
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. By @thm-det-row-operations: a swap multiplies it by \( -1 \), scaling a row by \( c \) multiplies it by \( c \), and adding a multiple of one row to a different row leaves it unchanged.
2. False. The move is \( R_2 \to 3R_2 \) followed by \( R_2 \to R_2 - R_1 \), so it multiplies the determinant by \( 3 \). For \( \I_2 \) it gives \( \begin{pmatrix} 1 & 0 \\ -1 & 3 \end{pmatrix} \), of determinant \( 3 \ne 1 \).
3. False. \( \I_2 \) and \( \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) both have determinant \( 1 \), but \( \P^{-1}\I_2\P = \I_2 \) for every invertible \( \P \), so \( \I_2 \) is similar only to itself.
4. True. Both equal \( \det \A \det \B \) by @thm-det-multiplicative, since multiplication in \( F \) is commutative.
5. Matrices of \( T \) in two bases are similar (@thm-change-of-basis-maps), and similar matrices have equal determinants (@cor-det-similarity-invariant).
6. No: \( M_n(F) \) is not a group under multiplication, since the zero matrix has no inverse. The restriction \( \det \colon \GL_n(F) \to F \setminus \{0\} \) is a homomorphism (@thm-det-homomorphism).
:::
:::

### B. Practice

::: {#exr-properties-b1}
[B1: Determinants by elimination]

Compute the determinants of the following real matrices by row reduction, recording the effect of each operation.
\[
\A = \begin{pmatrix} 1 & 2 & 0 & 1 \\ 2 & 3 & 1 & 4 \\ 0 & 1 & 3 & 2 \\ -1 & 1 & 2 & 5 \end{pmatrix}, \qquad
\B = \begin{pmatrix} 2 & -1 & 3 & 1 \\ 4 & -2 & 7 & 3 \\ -2 & 2 & -1 & 4 \\ 6 & -3 & 9 & 5 \end{pmatrix}.
\]
:::

::: {.solution}
For \( \A \): the replacements \( R_2 \to R_2 - 2R_1 \) and \( R_4 \to R_4 + R_1 \) give rows \( (1, 2, 0, 1) \), \( (0, -1, 1, 2) \), \( (0, 1, 3, 2) \), \( (0, 3, 2, 6) \). Then \( R_3 \to R_3 + R_2 \) and \( R_4 \to R_4 + 3R_2 \) give \( (0, 0, 4, 4) \) and \( (0, 0, 5, 12) \). Pulling the factor \( 4 \) out of row \( 3 \) leaves \( (0, 0, 1, 1) \), and \( R_4 \to R_4 - 5R_3 \) gives \( (0, 0, 0, 7) \). None of the replacements changes the determinant (@thm-det-row-operations), so
\[
\det \A = 4 \det \begin{pmatrix} 1 & 2 & 0 & 1 \\ 0 & -1 & 1 & 2 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 7 \end{pmatrix} = 4 \cdot \big(1 \cdot (-1) \cdot 1 \cdot 7\big) = -28,
\]
by @thm-det-triangular.

For \( \B \): \( R_2 \to R_2 - 2R_1 \), \( R_3 \to R_3 + R_1 \), \( R_4 \to R_4 - 3R_1 \) give rows \( (2, -1, 3, 1) \), \( (0, 0, 1, 1) \), \( (0, 1, 2, 5) \), \( (0, 0, 0, 2) \), without changing the determinant. The \( (2, 2) \)-entry is \( 0 \), so swap \( R_2 \leftrightarrow R_3 \), which multiplies the determinant by \( -1 \). The result is upper triangular with diagonal \( 2, 1, 1, 2 \), so
\[
\det \B = -(2 \cdot 1 \cdot 1 \cdot 2) = -4 .
\]
:::

::: {#exr-properties-b2}
[B2: A parameter]

Let \( t \in \nR \) and \( \A_t = \begin{pmatrix} t & 1 & 1 \\ 1 & t & 1 \\ 1 & 1 & t \end{pmatrix} \). Find \( \det \A_t \) as a factored polynomial in \( t \). Hence determine for which \( t \) the matrix \( \A_t \) is invertible.
:::

::: {.solution}
The replacements \( R_1 \to R_1 + R_2 \) and \( R_1 \to R_1 + R_3 \) do not change the determinant and make row \( 1 \) equal to \( (t + 2, t + 2, t + 2) \). By linearity in row \( 1 \) (this holds for every value of \( t + 2 \), including \( 0 \)),
\[
\det \A_t = (t + 2) \det \begin{pmatrix} 1 & 1 & 1 \\ 1 & t & 1 \\ 1 & 1 & t \end{pmatrix} = (t + 2) \det \begin{pmatrix} 1 & 1 & 1 \\ 0 & t - 1 & 0 \\ 0 & 0 & t - 1 \end{pmatrix} = (t + 2)(t - 1)^2,
\]
where the second step uses \( R_2 \to R_2 - R_1 \), \( R_3 \to R_3 - R_1 \), and the last uses @thm-det-triangular. By @thm-det-nonzero-iff-invertible, \( \A_t \) is invertible if and only if \( t \ne 1 \) and \( t \ne -2 \).
:::

::: {#exr-properties-b3}
[B3: The shift operator]

Let \( T \colon \nR[x]_{\le 3} \to \nR[x]_{\le 3} \), \( T(p) = p(x + 1) \). Find \( \det T \). Hence show that \( T \) is invertible.
:::

::: {.solution}
In the basis \( \sB = (1, x, x^2, x^3) \), \( T(1) = 1 \), \( T(x) = 1 + x \), \( T(x^2) = 1 + 2x + x^2 \) and \( T(x^3) = 1 + 3x + 3x^2 + x^3 \). So
\[
[T]_{\sB} = \begin{pmatrix} 1 & 1 & 1 & 1 \\ 0 & 1 & 2 & 3 \\ 0 & 0 & 1 & 3 \\ 0 & 0 & 0 & 1 \end{pmatrix},
\]
which is upper triangular with ones on the diagonal. By @def-det-operator and @thm-det-triangular, \( \det T = 1 \). Since \( \det T \ne 0 \), \( T \) is invertible by @thm-det-operator-properties. (Its inverse is \( p \mapsto p(x - 1) \).)
:::

### C. Going deeper

::: {#exr-properties-c1}
[C1: Orthogonal-type matrices]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \A \in M_n(\nR) \) satisfy \( \A\tp \A = \I_n \). Prove that \( \det \A = 1 \) or \( \det \A = -1 \).
2. Show that both values occur, for every \( n \ge 1 \).
3. Over \( \nF_2 \), what can \( \det \A \) be if \( \A\tp \A = \I_n \)?
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. By @thm-det-properties, \( 1 = \det \I_n = \det(\A\tp \A) = \det \A\tp \det \A = (\det \A)^2 \). A real number with square \( 1 \) is \( 1 \) or \( -1 \).
2. \( \I_n\tp \I_n = \I_n \) and \( \det \I_n = 1 \). For \( \D = \diag(-1, 1, \dots, 1) \), \( \D\tp \D = \D^2 = \I_n \) and \( \det \D = -1 \) by @thm-det-triangular.
3. The same computation gives \( (\det \A)^2 = 1 \). In \( \nF_2 \), \( \det \A \in \{0, 1\} \) and \( 0^2 = 0 \), so \( \det \A = 1 \). This agrees with (a), since \( -1 = 1 \) in \( \nF_2 \).
:::
:::

::: {#exr-properties-c2}
[C2: Left multiplication on matrices]

Let \( \A \in M_n(F) \), and let \( L_{\A} \colon M_n(F) \to M_n(F) \), \( L_{\A}(\X) = \A\X \). This is a linear operator on a space of dimension \( n^2 \). Prove that
\[
\det L_{\A} = (\det \A)^n .
\]

::: {.enumerate options="label=(\alph*)"}
1. Order the matrix units column by column, \( \sB = (\E_{11}, \E_{21}, \dots, \E_{n1}, \E_{12}, \dots, \E_{n2}, \dots, \E_{1n}, \dots, \E_{nn}) \). Show that \( [L_{\A}]_{\sB} \) consists of \( n \) copies of \( \A \) placed along the diagonal, with zeros elsewhere.
2. Show that \( L_{\A\B} = L_{\A} L_{\B} \), and prove the formula when \( \A \) is an elementary matrix.
3. Prove the formula for invertible \( \A \), and then for non-invertible \( \A \).
:::

*Hint: for a swap matrix, identify \( [L_{\P_{ij}}]_{\sB} \) as a permutation matrix and use @exr-existence-and-uniqueness-b2.*
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. By @thm-three-views-of-product, the \( l \)-th column of \( \A\E_{kl} \) is \( \A\e_k \), the \( k \)-th column of \( \A \), and the other columns are zero. So \( \A\E_{kl} = \sum_{i} a_{ik}\E_{il} \). In \( \sB \), the coordinates of this vector are zero outside the \( l \)-th block of \( n \) positions, and inside that block they are the \( k \)-th column of \( \A \). Hence the columns of \( [L_{\A}]_{\sB} \) belonging to the \( l \)-th block are those of \( \A \), placed in the rows of the \( l \)-th block: \( [L_{\A}]_{\sB} \) has \( n \) copies of \( \A \) along the diagonal.
2. \( L_{\A\B}(\X) = \A\B\X = L_{\A}(L_{\B}(\X)) \) by associativity. Now let \( \E \) be elementary. If \( \E = \I_n + c\E_{ij} \) with \( i \ne j \), then by (a) \( [L_{\E}]_{\sB} \) is triangular (upper if \( i < j \), lower if \( i > j \)) with all diagonal entries \( 1 \), so \( \det L_{\E} = 1 = (\det \E)^n \) by @thm-det-triangular and @thm-det-row-operations (e). If \( \E = \D_i(c) \), then \( [L_{\E}]_{\sB} \) is diagonal with \( c \) appearing \( n \) times and \( 1 \) elsewhere, so \( \det L_{\E} = c^n = (\det \E)^n \). If \( \E = \P_{ij} \), then \( [L_{\E}]_{\sB} \) has exactly one \( 1 \) in each row and column, so it is a permutation matrix \( \P_\sigma \) (@def-permutation-matrix), and \( \sigma \) exchanges the positions of \( \E_{il} \) and \( \E_{jl} \) for each \( l \): \( \sigma \) is a product of \( n \) disjoint transpositions. By @exr-existence-and-uniqueness-b2, @thm-sign-multiplicative and @cor-sign-transposition, \( \det L_{\E} = \sgn(\sigma) = (-1)^n = (\det \E)^n \).
3. If \( \A \) is invertible, then \( \A = \E_1 \cdots \E_k \) with elementary \( \E_m \) (@thm-invertible-tfae (d)). By (b) and @thm-det-operator-properties, \( \det L_{\A} = \det L_{\E_1} \cdots \det L_{\E_k} = (\det \E_1)^n \cdots (\det \E_k)^n = (\det \E_1 \cdots \det \E_k)^n = (\det \A)^n \), where the last step is @thm-det-multiplicative. If \( \A \) is not invertible, there is \( \v \ne \0 \) with \( \A\v = \0 \) (@thm-invertible-tfae (b)). The matrix \( \X = \begin{pmatrix} \v & \0 & \cdots & \0 \end{pmatrix} \) is non-zero and \( \A\X = 0 \), so \( L_{\A} \) is not injective, hence not invertible, and \( \det L_{\A} = 0 \) by @thm-det-operator-properties. Also \( \det \A = 0 \) by @thm-det-nonzero-iff-invertible, so \( (\det \A)^n = 0 \) as \( n \ge 1 \).
:::
:::

::: {#exr-properties-c3}
[C3: Non-square factors]

::: {.enumerate options="label=(\alph*)"}
1. Give \( \A \in M_{2 \times 1}(\nR) \) and \( \B \in M_{1 \times 2}(\nR) \) with \( \det(\B\A) \ne \det(\A\B) \).
2. Let \( m > n \), \( \A \in M_{m \times n}(F) \) and \( \B \in M_{n \times m}(F) \). Prove that \( \det(\A\B) = 0 \).
3. Explain why (a) does not contradict @thm-det-multiplicative.
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Let \( \A = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \) and \( \B = \begin{pmatrix} 1 & 0 \end{pmatrix} \). Then \( \B\A = (1) \), of determinant \( 1 \), and \( \A\B = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \), of determinant \( 0 \).
2. By @thm-rank-product-inequality, \( \rank(\A\B) \le \rank \A \le n \), since \( \col(\A) \) is spanned by \( n \) columns. So \( \rank(\A\B) < m \), and the \( m \times m \) matrix \( \A\B \) is not invertible by @thm-invertible-tfae-det (d). Hence \( \det(\A\B) = 0 \) by @thm-det-nonzero-iff-invertible.
3. @thm-det-multiplicative concerns two **square** matrices of the same size, and then \( \det(\A\B) = \det(\B\A) \). Here \( \A \) and \( \B \) are not square, \( \det \A \) and \( \det \B \) are not defined, and \( \A\B \), \( \B\A \) have different sizes.
:::
:::
