# Invariant Subspaces

Chapter 3 raised a question it could not answer: given an operator \( T \) on a finite-dimensional space, how simple can its matrix \( \mtx{T}{\sB}{\sB} \) be made by choosing the basis \( \sB \) well? Chapter 7 found the first piece of an answer. A zero block in the lower-left corner of \( \mtx{T}{\sB}{\sB} \) appears exactly when the first few basis vectors span a subspace that \( T \) maps into itself. This section gives that property a name, collects the standard examples, and shows that it can fail badly: some operators map almost no subspace into itself. It ends by recording how such subspaces cut an operator, and its characteristic polynomial, into smaller pieces. The next section looks at the smallest non-zero case, a line, and finds eigenvectors there.

## Subspaces an operator maps into itself

After a vector space we studied its subspaces, and after linear maps their kernels and images. For an operator \( T \in \cL(V) \), the domain and the codomain are the same space, so a new question makes sense: which subspaces of \( V \) are compatible with \( T \)?

Here is the result that makes the question worth asking. Let \( V \) be finite-dimensional, \( T \in \cL(V) \), and \( U \) a subspace with \( \{\0\} \ne U \ne V \). Take a basis \( (\u_1, \dots, \u_k) \) of \( U \) and extend it to a basis \( \sB = (\u_1, \dots, \u_k, \w_1, \dots, \w_l) \) of \( V \). By @thm-invariant-subspace-block-triangular, the lower-left \( l \times k \) block of \( \mtx{T}{\sB}{\sB} \) is zero **if and only if** \( T\u \in U \) for every \( \u \in U \). For example, the cyclic shift \( T(x, y, z) = (y, z, x) \) on \( \nR^3 \) keeps the plane \( x + y + z = 0 \) in place, and in @exm-cyclic-shift-block-triangular this produced a matrix with a zero corner. The property "\( T \) maps \( U \) into \( U \)" is what we need to control, so it gets a name.

*A subspace is invariant under \( T \) when \( T \) never moves a vector of the subspace out of it.*

::: {#def-invariant-subspace}
[Invariant Subspace]

Let \( V \) be a vector space over \( F \) and \( T \in \cL(V) \). A subspace \( U \) of \( V \) is **invariant under \( T \)**, or **\( T \)-invariant**, if
\[
T\u \in U \qquad \text{for every } \u \in U,
\]
that is, if \( T(U) \subseteq U \).
:::

In words: we start from a **subspace** \( U \), not an arbitrary subset. We apply \( T \) to **every** vector of \( U \), and each image must land back **in \( U \)**. Nothing is required of vectors outside \( U \), and nothing says that a vector of \( U \) stays where it is: \( T\u \) may be a different vector of \( U \). The condition is an inclusion \( T(U) \subseteq U \), not an equality.

Checking "for every \( \u \in U \)" looks like infinitely many checks. Linearity reduces it to finitely many when \( U \) has a finite spanning list.

::: {#lem-invariance-on-spanning-list}
[Invariance Can Be Checked on a Spanning List]

Let \( T \in \cL(V) \) and \( U = \Span(\u_1, \dots, \u_k) \). Then \( U \) is \( T \)-invariant if and only if \( T\u_i \in U \) for each \( i = 1, \dots, k \).
:::

::: {.proof}
\( (\Rightarrow) \) Each \( \u_i \) lies in \( U \). \( (\Leftarrow) \) Let \( \u = c_1\u_1 + \dots + c_k\u_k \in U \). By @thm-linear-combination, \( T\u = c_1T\u_1 + \dots + c_kT\u_k \), a linear combination of vectors of \( U \), which lies in \( U \) because \( U \) is a subspace (@thm-subspace-test).
:::

**Examples.**

- **The trivial subspaces.** For every \( T \in \cL(V) \), both \( \{\0\} \) and \( V \) are \( T \)-invariant: \( T\0 = \0 \) (@thm-zero-maps-to-zero), and \( T\v \in V \) always. These are the degenerate cases, and they matter as a warning about what the word does **not** tell us: invariance carries information only for subspaces strictly between \( \{\0\} \) and \( V \). At the other extreme, for \( T = c\,\id_V \) **every** subspace is invariant, since \( c\u \in U \) whenever \( \u \in U \).
- **Kernel and image.** \( \ker T \) is invariant: if \( \u \in \ker T \), then \( T\u = \0 \in \ker T \). So is \( \im T \): if \( \w \in \im T \), then \( T\w \) is \( T \) of something, so \( T\w \in \im T \). More generally, for every polynomial \( p \in F[x] \), the subspaces \( \ker p(T) \) and \( \im p(T) \) are \( T \)-invariant, by @thm-kernel-image-of-polynomial-invariant (b). For instance \( \ker(T - c\,\id_V) \) is invariant for every scalar \( c \).
- **A line in the plane.** Let \( \A = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix} \) act on \( \nR^2 \). The line \( \Span(\e_1) \) is invariant, by @lem-invariance-on-spanning-list, because \( \A\e_1 = (2, 0) = 2\e_1 \in \Span(\e_1) \). The line \( \Span((1, 1)) \) is invariant as well, since \( \A(1, 1) = (3, 3) = 3\,(1, 1) \).
- **Polynomials of bounded degree.** Let \( D \colon F[x] \to F[x] \) be differentiation (@exm-differentiation). For each \( k \in \nN \), the subspace \( F[x]_{\le k} \) is \( D \)-invariant, because differentiating does not raise the degree. It is spanned by \( 1, x, \dots, x^k \), and \( D(x^j) = jx^{j-1} \in F[x]_{\le k} \).

**Non-example by minimal change.** Keep \( \A = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix} \) and replace the line \( \Span(\e_1) \) by the line \( \Span(\e_2) \). It is still a subspace, and \( \A\e_2 = (1, 3) \) is still some vector of \( \nR^2 \). What fails is the clause "\( T\u \in U \) for every \( \u \in U \)" at \( \u = \e_2 \): the vector \( (1, 3) \) is not a multiple of \( \e_2 \). In the same way, \( \Span(x, x^2) \) inside \( \nR[x]_{\le 3} \) is not \( D \)-invariant, because \( D(x) = 1 \notin \Span(x, x^2) \).

The examples with lines all have the same shape, which is worth recording now, because the whole next section grows out of it.

::: {#prp-one-dimensional-invariant}
[Invariant Lines]

Let \( T \in \cL(V) \) and \( \v \in V \) with \( \v \ne \0 \). Then \( \Span(\v) \) is \( T \)-invariant if and only if \( T\v = \lambda\v \) for some \( \lambda \in F \).
:::

::: {.proof}
By @lem-invariance-on-spanning-list, \( \Span(\v) \) is invariant if and only if \( T\v \in \Span(\v) \), and \( \Span(\v) = \{ \lambda\v : \lambda \in F \} \) by @def-span.
:::

So an invariant line is a line on which \( T \) acts by stretching with a single factor \( \lambda \). Does every operator have one? Not over \( \nR \).

::: {#exm-rotation-invariant-subspaces}
[A Rotation Has No Invariant Lines]

Let \( R \colon \nR^2 \to \nR^2 \), \( R(x, y) = (-y, x) \), be the rotation by a right angle. Find all \( R \)-invariant subspaces of \( \nR^2 \).
:::

::: {.solution}
A subspace \( U \) of \( \nR^2 \) has \( \dim U \in \{0, 1, 2\} \) by @thm-subspace-dimension. If \( \dim U = 0 \), then \( U = \{\0\} \); if \( \dim U = 2 \), then \( U = \nR^2 \) by @thm-dim-impl-eq. Both are invariant.

Suppose \( \dim U = 1 \). A basis of \( U \) is a single vector \( \v = (a, b) \ne \0 \), and \( U = \Span(\v) \). If \( U \) were invariant, then by @prp-one-dimensional-invariant there would be \( \lambda \in \nR \) with \( R\v = \lambda\v \), that is,
\[
-b = \lambda a, \qquad a = \lambda b .
\]
Substituting the first equation into the second gives \( a = \lambda b = \lambda(-\lambda a) = -\lambda^2a \), so \( (1 + \lambda^2)a = 0 \). Since \( \lambda \) is real, \( 1 + \lambda^2 \ge 1 > 0 \), so \( a = 0 \). Then \( b = -\lambda a = 0 \) by the first equation, and \( \v = \0 \), a contradiction.

Hence the only \( R \)-invariant subspaces of \( \nR^2 \) are \( \{\0\} \) and \( \nR^2 \). Geometrically, a quarter-turn moves every line through the origin onto the perpendicular line.
:::

The same computation over \( \nC \) does not end in a contradiction: \( 1 + \lambda^2 = 0 \) has the solutions \( \lambda = \pm i \), and we will see in the next section that \( \nC^2 \) does contain \( R \)-invariant lines. Whether invariant lines exist depends on the field.

**Why this definition.** Two variations suggest themselves, and both are worse.

- *Demand \( T(U) = U \).* Then \( \ker T \) would fail whenever \( T \) is not injective, since then \( T(\ker T) = \{\0\} \ne \ker T \). But the kernel is exactly the kind of subspace that produces a zero block, and @thm-invariant-subspace-block-triangular needs only the inclusion.
- *Demand \( T\u = \u \) for every \( \u \in U \).* That says \( T \) acts as the identity on \( U \), a far stronger condition. The line \( \Span((1, 1)) \) above is invariant under \( \A \), but \( \A \) triples its vectors.

The name records that the subspace, as a whole, is unchanged in the sense that it is carried into itself; its individual vectors may move.

::: {.warning}
**Invariant does not mean fixed.** The vectors of a \( T \)-invariant subspace may move, as long as they stay inside it. For the swap \( T(x, y) = (y, x) \) on \( \nR^2 \), the whole plane is invariant, yet \( T(1, 0) = (0, 1) \ne (1, 0) \). Conversely, containing a fixed vector does not make a subspace invariant. For \( T(x, y, z) = (x, z, y + z) \) on \( \nR^3 \), the plane \( z = 0 \) contains \( \e_1 \), and \( T\e_1 = \e_1 \); but it also contains \( \e_2 \), and \( T\e_2 = \e_3 \) leaves the plane.
:::

::: {.check}
Let \( T(x, y) = (x + y, y) \) on \( \nR^2 \). Is the \( x \)-axis \( T \)-invariant? Is the \( y \)-axis?
:::

::: {.solution}
By @lem-invariance-on-spanning-list it suffices to test one spanning vector. \( T\e_1 = (1, 0) = \e_1 \), which lies on the \( x \)-axis, so the \( x \)-axis is invariant. \( T\e_2 = (1, 1) \), which is not a multiple of \( \e_2 \), so the \( y \)-axis is **not** invariant.
:::

## Restriction and the induced operator

An invariant subspace \( U \) lets us split \( T \) into two smaller operators. One lives on \( U \): since \( T \) sends \( U \) into \( U \), we may simply forget the rest of \( V \). The other lives on the quotient \( V/U \), which records what \( U \) cannot see. Chapter 7 met both in the proof of @thm-invariant-subspace-block-triangular, and Chapter 3 constructed the second in @exr-products-and-quotients-c2. We now give them names.

::: {#def-restriction-operator}
[Restriction and Induced Operator]

Let \( T \in \cL(V) \) and let \( U \) be a \( T \)-invariant subspace of \( V \).

::: {.enumerate options="label=(\alph*)"}
1. The **restriction** of \( T \) to \( U \) is the operator \( T|_U \colon U \to U \), \( \u \mapsto T\u \).
2. The **induced operator** (or quotient operator) on \( V/U \) is \( \bar T \colon V/U \to V/U \), \( \v + U \mapsto T\v + U \).
:::
:::

**Well-definedness.** For (a), the rule makes sense as a map **into \( U \)** only because \( U \) is invariant; it is linear because \( T \) is, and \( U \) carries the operations of \( V \). For (b), the rule is phrased in terms of a representative \( \v \) of the coset, so we must check that it does not depend on that choice. Suppose \( \v + U = \v' + U \). Then \( \v - \v' \in U \) (@lem-coset-equality), so \( T\v - T\v' = T(\v - \v') \in U \) by invariance, and hence \( T\v + U = T\v' + U \). Linearity follows from the coset operations (@thm-quotient-space-operations-well-defined): for instance
\[
\begin{aligned}
\bar T\big((\v + U) + (\w + U)\big) &= \bar T(\v + \w + U) = T\v + T\w + U \\
&= \bar T(\v + U) + \bar T(\w + U),
\end{aligned}
\]
and scalars work the same way. Invariance was used exactly once in each part, which is where the hypothesis earns its place.

**Examples.**

- **Differentiation.** Let \( D \) act on \( V = \nR[x]_{\le 2} \) and \( U = \nR[x]_{\le 1} \), which is \( D \)-invariant. The restriction \( D|_U \) is differentiation on \( \nR[x]_{\le 1} \). The quotient \( V/U \) has dimension \( 1 \) (@thm-dimension-quotient), with basis \( x^2 + U \), and \( \bar D(x^2 + U) = 2x + U = \0 + U \), because \( 2x \in U \). So \( \bar D = 0 \).
- **The cyclic shift.** For \( T(x, y, z) = (y, z, x) \) and the plane \( U \) where \( x + y + z = 0 \), @exm-cyclic-shift-block-triangular showed that \( \bar T \) is the identity of the line \( \nR^3/U \): the shift permutes coordinates and so never changes their sum.
- **Degenerate cases.** For \( U = V \), the restriction is \( T \) itself and \( V/V \) is the zero space. For \( U = \{\0\} \), the restriction is the operator on the zero space, and \( \bar T \) is \( T \) in disguise, since \( \v + \{\0\} \) is just \( \v \).

With these names, the matrix theorem of Chapter 7 reads as follows. We add the consequence for determinants and characteristic polynomials, which is what the rest of this chapter uses.

::: {#thm-invariant-subspace-matrix}
[Invariant Subspaces and Block Triangular Matrices]

Let \( V \) be finite-dimensional, \( T \in \cL(V) \), and \( U \) a subspace with \( \{\0\} \ne U \ne V \). Let \( \sB_U = (\u_1, \dots, \u_k) \) be a basis of \( U \), extended to a basis \( \sB = (\u_1, \dots, \u_k, \w_1, \dots, \w_l) \) of \( V \), and put \( \bar\sB = (\w_1 + U, \dots, \w_l + U) \).

::: {.enumerate options="label=(\alph*)"}
1. \( U \) is \( T \)-invariant if and only if \( \mtx{T}{\sB}{\sB} \) has zero lower-left \( l \times k \) block.
2. In that case
\[
\mtx{T}{\sB}{\sB} = \begin{pmatrix} \mtx{T|_U}{\sB_U}{\sB_U} & \B \\ 0 & \mtx{\bar T}{\bar\sB}{\bar\sB} \end{pmatrix}
\]
for some \( \B \in M_{k \times l}(F) \), and
\[
\det T = \det(T|_U)\,\det \bar T, \qquad p_T = p_{T|_U}\; p_{\bar T} .
\]
:::
:::

::: {.proof}
Part (a), and the block form in (b), are @thm-invariant-subspace-block-triangular in the language of @def-invariant-subspace and @def-restriction-operator; \( \bar\sB \) is a basis of \( V/U \) by @thm-dimension-quotient.

Write \( \A = \mtx{T|_U}{\sB_U}{\sB_U} \in M_k(F) \) and \( \D = \mtx{\bar T}{\bar\sB}{\bar\sB} \in M_l(F) \). By @def-det-operator and @thm-det-block-triangular, \( \det T = \det\mtx{T}{\sB}{\sB} = \det \A \det \D = \det(T|_U)\det\bar T \). For the characteristic polynomials,
\[
x\I_{k+l} - \mtx{T}{\sB}{\sB} = \begin{pmatrix} x\I_k - \A & -\B \\ 0 & x\I_l - \D \end{pmatrix}
\]
is block upper triangular with square diagonal blocks, as a matrix over \( F[x] \). The block triangular determinant holds over the commutative ring \( F[x] \) (the remark after @thm-det-block-triangular), so \( \det(x\I - \mtx{T}{\sB}{\sB}) = \det(x\I_k - \A)\det(x\I_l - \D) \). By @def-charpoly-operator, this says \( p_T = p_{T|_U}\,p_{\bar T} \).
:::

The theorem is the reason invariant subspaces matter. It splits the study of \( T \) into the study of two operators on smaller spaces, and every quantity that sees only the diagonal blocks splits with it. For differentiation on \( \nR[x]_{\le 2} \), with \( U = \nR[x]_{\le 1} \) and \( \sB = (1, x, x^2) \),
\[
\mtx{D}{\sB}{\sB} = \left(\begin{array}{cc|c} 0 & 1 & 0 \\ 0 & 0 & 2 \\ \hline 0 & 0 & 0 \end{array}\right),
\]
with upper-left block \( \mtx{D|_U}{\sB_U}{\sB_U} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \), lower-right block \( \mtx{\bar D}{\bar\sB}{\bar\sB} = (0) \), and \( p_D = x^3 = x^2 \cdot x \). Section 7 of this chapter will run this splitting repeatedly, by induction on the dimension.

## Sums, intersections and direct sums

Invariant subspaces can be combined. Sums and intersections of invariant subspaces are invariant, in contrast to many other properties, and the proof is one line each.

::: {#prp-invariant-sum-intersection}
[Sums and Intersections of Invariant Subspaces]

Let \( T \in \cL(V) \) and let \( U_1, \dots, U_k \) be \( T \)-invariant subspaces of \( V \). Then \( U_1 + \dots + U_k \) and \( U_1 \cap \dots \cap U_k \) are \( T \)-invariant.
:::

::: {.proof}
Both are subspaces, by @thm-subspace-sum and @thm-intersection-subspaces. Let \( \u = \u_1 + \dots + \u_k \) with \( \u_i \in U_i \). Then \( T\u = T\u_1 + \dots + T\u_k \) with \( T\u_i \in U_i \) by invariance, so \( T\u \in U_1 + \dots + U_k \). If \( \u \in U_1 \cap \dots \cap U_k \), then \( T\u \in U_i \) for each \( i \), by invariance of each \( U_i \), so \( T\u \in U_1 \cap \dots \cap U_k \).
:::

When \( V \) is a **direct** sum of invariant subspaces, all the off-diagonal blocks vanish, not just one corner. Chapter 7 proved this for two summands (@thm-direct-sum-block-diagonal). The diagonalization theorem of Section 4 needs any number of summands.

::: {#thm-direct-sum-invariant-block-diagonal}
[Invariant Direct Sums and Block Diagonal Matrices]

Let \( V \) be finite-dimensional with \( V = U_1 \oplus \dots \oplus U_k \), where each \( U_i \ne \{\0\} \) has a basis \( \sB_i \) of length \( n_i \). Let \( \sB \) be the list \( \sB_1, \dots, \sB_k \) written one after another, and \( T \in \cL(V) \). Then \( \sB \) is a basis of \( V \), and the following are equivalent:

::: {.enumerate options="label=(\alph*)"}
1. each \( U_i \) is \( T \)-invariant;
2. \( \mtx{T}{\sB}{\sB} \) is block diagonal with respect to the partition \( n_1, \dots, n_k \).
:::

In that case
\[
\mtx{T}{\sB}{\sB} = \mtx{T|_{U_1}}{\sB_1}{\sB_1} \oplus \dots \oplus \mtx{T|_{U_k}}{\sB_k}{\sB_k}, \qquad p_T = p_{T|_{U_1}} \cdots\, p_{T|_{U_k}} .
\]
:::

::: {.idea}
Read the matrix one block of columns at a time. The columns of block \( j \) are the coordinates of \( T\b \) for the vectors \( \b \) of \( \sB_j \). Such a \( T\b \) lies in \( U_j \) exactly when all its coordinates outside block \( j \) vanish, because a vector of \( U_j \) is already a combination of \( \sB_j \), and coordinates are unique.
:::

::: {.proof}
By @thm-direct-sum-k-criteria ((a) \( \Rightarrow \) (d)), \( \sB \) is a basis of \( V \). Fix \( j \) and a vector \( \b \) of \( \sB_j \); the column of \( \mtx{T}{\sB}{\sB} \) belonging to \( \b \) is \( \coord{T\b}{\sB} \) (@def-matrix-of-linear-map). We claim: \( T\b \in U_j \) if and only if the entries of this column outside the rows of block \( j \) are all \( 0 \). If \( T\b \in U_j = \Span(\sB_j) \), then \( T\b \) is a combination of \( \sB_j \) alone, which is a representation in the basis \( \sB \) with zero coefficients outside block \( j \); by @thm-unique-representation, it is **the** coordinate vector. Conversely, if those entries vanish, then \( T\b \) is a combination of \( \sB_j \), so it lies in \( U_j \).

(a) \( \Rightarrow \) (b). If \( U_j \) is invariant, then \( T\b \in U_j \) for each \( \b \) in \( \sB_j \), so by the claim every block \( (i, j) \) with \( i \ne j \) is zero. As \( j \) was arbitrary, \( \mtx{T}{\sB}{\sB} \) is block diagonal. Moreover the entries of column \( \b \) in the rows of block \( j \) are the coordinates of \( T\b = T|_{U_j}\b \) in \( \sB_j \), so the \( (j, j) \) block is \( \mtx{T|_{U_j}}{\sB_j}{\sB_j} \).

(b) \( \Rightarrow \) (a). If the blocks \( (i, j) \) with \( i \ne j \) vanish, the claim gives \( T\b \in U_j \) for every \( \b \) in \( \sB_j \), and \( U_j \) is invariant by @lem-invariance-on-spanning-list.

Finally, \( x\I - \mtx{T}{\sB}{\sB} \) is block diagonal with diagonal blocks \( x\I_{n_j} - \mtx{T|_{U_j}}{\sB_j}{\sB_j} \). Its determinant over \( F[x] \) is the product of the determinants of these blocks (the remark after @thm-det-block-triangular, applied by induction on the number of blocks), which is \( p_T = \prod_j p_{T|_{U_j}} \) by @def-charpoly-operator.
:::

So an operator that preserves each piece of a direct sum decomposition is, in a suitable basis, a list of independent smaller operators. The best possible case is a decomposition into invariant **lines**: then every block is \( 1 \times 1 \), and \( \mtx{T}{\sB}{\sB} \) is diagonal. By @prp-one-dimensional-invariant, that happens exactly when \( V \) has a basis of vectors \( \v \) with \( T\v = \lambda\v \). This observation is the starting point of the next section.

A tempting shortcut is to assume that once one invariant subspace is found, a complement of it can be chosen invariant too, and the matrix becomes block diagonal. This fails.

::: {.warning}
**The complement of an invariant subspace need not be invariant.** Let \( \N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) act on \( F^2 \). The line \( U = \Span(\e_1) \) is invariant, since \( \N\e_1 = \0 \). Every complement of \( U \) is a line \( W = \Span((a, 1)) \) for some \( a \in F \) (a line not equal to \( U \) contains a vector with second entry \( 1 \)). But \( \N(a, 1) = (1, 0) \), which is not a multiple of \( (a, 1) \). So **no** complement of \( U \) is \( \N \)-invariant, and no basis \( \sB \) makes \( \mtx{T_{\N}}{\sB}{\sB} \) block diagonal with two \( 1 \times 1 \) blocks.
:::

::: {.check}
Let \( U_1, U_2 \) be \( T \)-invariant. Must the union \( U_1 \cup U_2 \) be \( T \)-invariant? Must it even be a subspace?
:::

::: {.solution}
The question has a trap: "invariant subspace" requires a subspace, and a union of two subspaces is usually not one (@prp-union-subspaces). For \( T = \id_{\nR^2} \), the two axes are invariant, but their union is not a subspace, so the word does not apply. The subspace that plays the role of the union is the sum \( U_1 + U_2 \), which is invariant by @prp-invariant-sum-intersection.
:::

## Exercises

### A. Check your understanding

:::: {#exr-invariant-subspaces-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define what it means for a subspace \( U \) of \( V \) to be invariant under \( T \in \cL(V) \).
2. True or false: for every \( T \in \cL(V) \), the subspaces \( \ker T \) and \( \im T \) are \( T \)-invariant. Justify your answer.
3. True or false: if \( U \) is \( T \)-invariant, then \( T\u = \u \) for every \( \u \in U \). Justify your answer.
4. True or false: if \( U \) is invariant under \( S \) and under \( T \), then \( U \) is invariant under \( S + T \) and under \( ST \). Justify your answer.
5. For \( \v \ne \0 \), what condition on \( T\v \) makes \( \Span(\v) \) invariant?
6. In a basis whose first \( k \) vectors form a basis of a \( T \)-invariant subspace \( U \), which block of \( \mtx{T}{\sB}{\sB} \) is zero, and what are the two diagonal blocks?
:::
::::

::: {.solution}
(a) \( U \) is \( T \)-invariant if \( T\u \in U \) for every \( \u \in U \) (@def-invariant-subspace).

(b) True. If \( \u \in \ker T \), then \( T\u = \0 \in \ker T \). If \( \w \in \im T \), then \( T\w \in \im T \) by definition of the image.

(c) False. For \( T = 2\,\id_{\nR^2} \), the subspace \( \nR^2 \) is invariant, but \( T\e_1 = 2\e_1 \ne \e_1 \).

(d) True. For \( \u \in U \), both \( S\u \) and \( T\u \) lie in \( U \), so \( (S + T)\u = S\u + T\u \in U \) since \( U \) is a subspace. Also \( T\u \in U \), so \( (ST)\u = S(T\u) \in U \) by invariance under \( S \).

(e) \( T\v = \lambda\v \) for some scalar \( \lambda \) (@prp-one-dimensional-invariant).

(f) The lower-left block is zero. The upper-left block is \( \mtx{T|_U}{\sB_U}{\sB_U} \) and the lower-right block is the matrix of the induced operator \( \bar T \) on \( V/U \) (@thm-invariant-subspace-matrix).
:::

### B. Practice

:::: {#exr-invariant-subspaces-b1}
[B1: All invariant subspaces of a diagonal matrix]

Let \( \A = \diag(1, 2) \) act on \( \nR^2 \). Find all \( \A \)-invariant subspaces of \( \nR^2 \).
::::

::: {.solution}
As in @exm-rotation-invariant-subspaces, a subspace of \( \nR^2 \) is \( \{\0\} \), \( \nR^2 \), or a line \( \Span(\v) \) with \( \v = (a, b) \ne \0 \). The first two are invariant. By @prp-one-dimensional-invariant, the line is invariant if and only if \( \A\v = \lambda\v \) for some \( \lambda \in \nR \), that is,
\[
a = \lambda a, \qquad 2b = \lambda b .
\]
If \( a \ne 0 \), the first equation gives \( \lambda = 1 \), and then \( 2b = b \) gives \( b = 0 \); so \( \v \) is a multiple of \( \e_1 \). If \( a = 0 \), then \( b \ne 0 \), the second equation gives \( \lambda = 2 \), and \( \v \) is a multiple of \( \e_2 \). Conversely \( \A\e_1 = \e_1 \) and \( \A\e_2 = 2\e_2 \). Hence the invariant subspaces are exactly
\[
\{\0\}, \qquad \Span(\e_1), \qquad \Span(\e_2), \qquad \nR^2 .
\]
Compare with the identity \( \I_2 \), for which every line is invariant: changing one diagonal entry from \( 1 \) to \( 2 \) destroys all lines except the two axes.
:::

:::: {#exr-invariant-subspaces-b2}
[B2: Kernels of \( T - c\,\id \)]

Let \( T \in \cL(V) \) and \( c \in F \).

::: {.enumerate options="label=(\alph*)"}
1. Prove directly from the definition that \( \ker(T - c\,\id_V) \) is \( T \)-invariant.
2. Hence show that **every** subspace of \( \ker(T - c\,\id_V) \) is \( T \)-invariant.
:::
::::

::: {.solution}
(a) Let \( K = \ker(T - c\,\id_V) \), a subspace by @thm-prop-kernel. For \( \u \in K \) we have \( T\u - c\u = \0 \), that is, \( T\u = c\u \). Since \( K \) is a subspace, \( c\u \in K \). Hence \( T\u \in K \), and \( K \) is \( T \)-invariant.

(b) Let \( W \) be a subspace of \( K \) and \( \w \in W \). Since \( \w \in K \), part (a) gives \( T\w = c\w \), and \( c\w \in W \) because \( W \) is a subspace. Hence \( W \) is \( T \)-invariant. (On \( K \), \( T \) acts as \( c\,\id \), and for a scalar operator every subspace is invariant.)
:::

:::: {#exr-invariant-subspaces-b3}
[B3: Invariance under differentiation]

Let \( D \) be differentiation on \( V = \nR[x]_{\le 3} \). Determine which of the following subspaces are \( D \)-invariant. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( U_1 = \Span(1, x) \).
2. \( U_2 = \Span(x, x^2) \).
3. \( U_3 = \{ p \in V : p(0) = 0 \} \).
4. \( U_4 = \Span(x^2 + 2x,\ 2x + 2,\ 2) \).
5. \( U_5 = \Span(1, x^2) \), the even polynomials in \( V \).
:::
::::

::: {.solution}
We use @lem-invariance-on-spanning-list throughout.

(a) Invariant: \( D(1) = 0 \in U_1 \) and \( D(x) = 1 \in U_1 \).

(b) Not invariant: \( D(x) = 1 \), and \( 1 \notin \Span(x, x^2) \) since every element of \( U_2 \) has constant term \( 0 \).

(c) Not invariant: \( x \in U_3 \), but \( D(x) = 1 \) and \( 1 \) evaluated at \( 0 \) is \( 1 \ne 0 \).

(d) Invariant: \( D(x^2 + 2x) = 2x + 2 \), \( D(2x + 2) = 2 \) and \( D(2) = 0 \), all in \( U_4 \). (In fact \( U_4 = \nR[x]_{\le 2} \), since the three spanning polynomials have degrees \( 2, 1, 0 \) and so are independent by @thm-distinct-degrees-independent.)

(e) Not invariant: \( D(x^2) = 2x \), which is odd and non-zero, so it is not in \( \Span(1, x^2) \).
:::

### C. Going deeper

:::: {#exr-invariant-subspaces-c1}
[C1: A chain of invariant subspaces]

Let \( F \) be any field and
\[
\N = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} \in M_3(F),
\]
acting on \( F^3 \), so \( \N\e_1 = \0 \), \( \N\e_2 = \e_1 \), \( \N\e_3 = \e_2 \). Put \( W_0 = \{\0\} \), \( W_1 = \Span(\e_1) \), \( W_2 = \Span(\e_1, \e_2) \), \( W_3 = F^3 \).

::: {.enumerate options="label=(\alph*)"}
1. Show that each \( W_j \) is \( \N \)-invariant.
2. Let \( U \) be an \( \N \)-invariant subspace, and let \( j \) be the largest index such that some vector of \( U \) has a non-zero \( j \)-th entry (put \( j = 0 \) if \( U = \{\0\} \)). Prove that \( U = W_j \).
3. Deduce that the \( \N \)-invariant subspaces are exactly \( W_0 \subset W_1 \subset W_2 \subset W_3 \), and that any two of them are comparable under inclusion.
:::

*Hint: for (b), apply \( \N \) and \( \N^2 \) to a vector with non-zero \( j \)-th entry.*
::::

::: {.solution}
(a) \( W_0 \) and \( W_3 \) are invariant for every operator. By @lem-invariance-on-spanning-list, \( W_1 \) is invariant since \( \N\e_1 = \0 \), and \( W_2 \) is invariant since \( \N\e_1 = \0 \) and \( \N\e_2 = \e_1 \) lie in \( W_2 \).

(b) If \( U = \{\0\} \), then \( j = 0 \) and \( U = W_0 \). Otherwise \( j \ge 1 \). By the choice of \( j \), every vector of \( U \) has entries \( 0 \) beyond position \( j \), so \( U \subseteq W_j \). Pick \( \v = (a, b, c) \in U \) with non-zero \( j \)-th entry. We have \( \N\v = (b, c, 0) \) and \( \N^2\v = (c, 0, 0) \), and all of these lie in \( U \) by invariance.

*Case \( j = 3 \).* Here \( c \ne 0 \). Then \( \e_1 = c^{-1}\N^2\v \in U \), \( \e_2 = c^{-1}(\N\v - b\e_1) \in U \) and \( \e_3 = c^{-1}(\v - a\e_1 - b\e_2) \in U \). So \( W_3 \subseteq U \).

*Case \( j = 2 \).* Here \( c = 0 \) and \( b \ne 0 \). Then \( \e_1 = b^{-1}\N\v \in U \) and \( \e_2 = b^{-1}(\v - a\e_1) \in U \), so \( W_2 \subseteq U \).

*Case \( j = 1 \).* Here \( b = c = 0 \) and \( a \ne 0 \), so \( \e_1 = a^{-1}\v \in U \) and \( W_1 \subseteq U \).

In each case \( W_j \subseteq U \subseteq W_j \), so \( U = W_j \).

(c) By (a) each \( W_j \) is invariant, and by (b) every invariant subspace is one of them. Since \( W_0 \subset W_1 \subset W_2 \subset W_3 \), any two are comparable. In particular \( \N \) has exactly one invariant line, \( W_1 \), and exactly one invariant plane, \( W_2 \). Contrast @exr-invariant-subspaces-b1, where \( \diag(1, 2) \) has two invariant lines (in the sense of @prp-one-dimensional-invariant), neither containing the other.
:::

:::: {#exr-invariant-subspaces-c2}
[C2: Invariance under the inverse]

::: {.enumerate options="label=(\alph*)"}
1. Let \( V \) be finite-dimensional, \( T \in \cL(V) \) invertible, and \( U \) a \( T \)-invariant subspace. Prove that \( T(U) = U \), and deduce that \( U \) is \( T^{-1} \)-invariant.
2. Show that (a) fails without finite dimension. On \( V = F^{\nZ} \), the space of all functions \( \nZ \to F \) written as two-sided sequences \( (s_n)_{n \in \nZ} \), let \( (Ss)_n = s_{n-1} \). Show that \( S \) is invertible, that \( U = \{ s : s_n = 0 \text{ for all } n < 0 \} \) is \( S \)-invariant, and that \( U \) is **not** \( S^{-1} \)-invariant.
:::

*Hint: for (a), consider the restriction \( T|_U \) and its kernel.*
::::

::: {.solution}
(a) The restriction \( T|_U \in \cL(U) \) exists by invariance. Its kernel is \( \ker T \cap U = \{\0\} \), since \( T \) is injective, so \( T|_U \) is injective (@thm-injective-iff-trivial-kernel). The space \( U \) is finite-dimensional (@thm-subspace-dimension), so by @thm-invertible-operator-tfae, \( T|_U \) is surjective onto \( U \). That is, \( T(U) = U \).

Now let \( \u \in U \). By surjectivity of \( T|_U \), there is \( \u' \in U \) with \( T\u' = \u \). Applying \( T^{-1} \) gives \( T^{-1}\u = \u' \in U \). Hence \( U \) is \( T^{-1} \)-invariant.

(b) \( V = F^{\nZ} \) is a vector space with pointwise operations (@exm-vector-spaces), and \( S \) is linear because it only re-indexes entries. Define \( (S's)_n = s_{n+1} \). Then \( (S'Ss)_n = (Ss)_{n+1} = s_n \) and \( (SS's)_n = (S's)_{n-1} = s_n \), so \( S \) is invertible with \( S^{-1} = S' \).

\( U \) is a subspace (the conditions \( s_n = 0 \) are preserved by sums and scalar multiples). If \( s \in U \) and \( n < 0 \), then \( n - 1 < 0 \), so \( (Ss)_n = s_{n-1} = 0 \); thus \( Ss \in U \), and \( U \) is \( S \)-invariant.

Let \( \delta \in U \) be the sequence with \( \delta_0 = 1 \) and \( \delta_n = 0 \) for \( n \ne 0 \). Then \( (S^{-1}\delta)_{-1} = \delta_0 = 1 \ne 0 \), so \( S^{-1}\delta \notin U \). Hence \( U \) is not \( S^{-1} \)-invariant. In (a), the step that breaks is "\( T|_U \) injective, hence surjective", which needs finite dimension: here \( S|_U \) is injective but its image misses \( \delta \).
:::
