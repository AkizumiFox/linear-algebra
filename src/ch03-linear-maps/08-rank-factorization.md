# Rank, Equivalence and Factorizations

Similarity compares two matrices of one operator, where the same basis is used for input and output, and the last section showed that deciding it is hard. This section asks what happens when the two bases may be chosen independently, as they may for any map \( T \colon V \to W \). The answer is strikingly simple: the rank is then the only thing that matters. On the way we meet the column–row factorization, which writes every matrix as a product through a space of dimension equal to its rank, and we collect the basic inequalities for the rank of a composition.

## The column–row factorization

In Chapter 2 we computed the rank of a matrix by row reduction, and the reduction gave more than a number. It produced a basis of the column space, the pivot columns of \( \A \) (@thm-basis-column-space), and it expressed every other column in terms of them, with coefficients read off the reduced row echelon form. Recording both pieces of information as matrices gives a factorization.

::: {#thm-column-row-factorization}
[Column–Row Factorization]

Let \( \A \in M_{m \times n}(F) \) have rank \( r \ge 1 \), with pivot columns \( j_1 < \dots < j_r \). Let \( \C \in M_{m \times r}(F) \) be the matrix whose columns are the pivot columns \( \a_{j_1}, \dots, \a_{j_r} \) of \( \A \), and let \( \R \in M_{r \times n}(F) \) consist of the first \( r \) rows of the reduced row echelon form of \( \A \), that is, its non-zero rows. Then
\[
\A = \C\R .
\]
Moreover, the columns of \( \C \) are linearly independent and the rows of \( \R \) are linearly independent.
:::

::: {.idea}
Column \( l \) of \( \C\R \) is \( \C \) times column \( l \) of \( \R \), that is, a combination of the pivot columns of \( \A \) with the entries of column \( l \) of the RREF as coefficients. For a pivot column the coefficients are a standard basis vector, and for a free column they are exactly the coefficients that @thm-basis-column-space (b) provides. So the factorization is that theorem written as a matrix identity.
:::

::: {.proof}
Let \( \E \) be the RREF of \( \A \), with entries \( e_{kl} \). By @thm-row-rank-equals-column-rank, \( \E \) has exactly \( r \) pivots, so its non-zero rows are rows \( 1, \dots, r \). Fix a column index \( l \). By @thm-matrix-times-vector-columns, column \( l \) of \( \C\R \) is
\[
\C\begin{pmatrix} e_{1l} \\ \vdots \\ e_{rl} \end{pmatrix} = e_{1l}\a_{j_1} + \dots + e_{rl}\a_{j_r} .
\]
*Case 1: \( l = j_i \) is a pivot column.* By @lem-rref-columns (a), column \( j_i \) of \( \E \) is \( \e_i \), so the combination is \( \a_{j_i} = \a_l \).

*Case 2: \( l \) is a free column.* Let \( t \) be the number of pivot columns to the left of \( l \). For \( k > t \), the leading entry of row \( k \) of \( \E \) lies in column \( j_k > l \), so \( e_{kl} = 0 \). The combination is therefore \( e_{1l}\a_{j_1} + \dots + e_{tl}\a_{j_t} \), which equals \( \a_l \) by @thm-basis-column-space (b).

In both cases column \( l \) of \( \C\R \) is column \( l \) of \( \A \); hence \( \A = \C\R \). The columns of \( \C \) form a basis of \( \col(\A) \) by @thm-basis-column-space (a), so they are independent. The rows of \( \R \) are the non-zero rows of \( \E \), which form a basis of \( \row(\A) \) by @thm-basis-row-space, so they are independent. This proves the theorem.
:::

In words: every matrix of rank \( r \) is a "tall" matrix with independent columns times a "wide" matrix with independent rows, and the middle size is exactly \( r \). The factorization cannot be squeezed further.

::: {#prp-rank-minimal-factorization}
[Rank as the size of the thinnest factorization]

Let \( \A \in M_{m \times n}(F) \) be non-zero. Then \( \rank \A \) is the **smallest** integer \( s \ge 1 \) such that \( \A = \B\D \) for some \( \B \in M_{m \times s}(F) \) and \( \D \in M_{s \times n}(F) \).
:::

::: {.proof}
Let \( r = \rank \A \); then \( r \ge 1 \) since \( \A \ne 0 \). By @thm-column-row-factorization, a factorization with \( s = r \) exists. Conversely, suppose \( \A = \B\D \) with \( \B \in M_{m \times s}(F) \). By @thm-rank-product-inequality, \( r = \rank(\B\D) \le \rank \B \), and \( \rank \B \le s \) because \( \col(\B) \) is spanned by \( s \) columns (@thm-size-bounds). Hence \( r \le s \).
:::

This gives a second view of "row rank equals column rank". Let \( \A \ne 0 \), and let \( \B \) be the matrix whose \( s = \dim \col(\A) \) columns form a basis of \( \col(\A) \). Each column \( \a_j \) of \( \A \) is \( \B\d_j \) for its coordinate column \( \d_j \) (@thm-matrix-times-vector-columns), so \( \A = \B\D \) with \( \D = \begin{pmatrix} \d_1 & \cdots & \d_n \end{pmatrix} \). Then every row of \( \A \) is a row of \( \B \) times \( \D \), a combination of the \( s \) rows of \( \D \) (@thm-three-views-of-product (3) and the row form of @thm-matrix-times-vector-columns), so \( \dim \row(\A) \le s = \dim \col(\A) \). Applying the same argument to \( \A\tp \) gives the reverse inequality. In the language of maps, the factorization says that \( \x \mapsto \A\x \) can be done in two steps, \( F^n \to F^r \to F^m \): first a surjection onto a space of dimension \( r \), then an injection.

::: {#exm-column-row-factorization}
[A column–row factorization]

Find the column–row factorization of \( \A = \begin{pmatrix} 1 & 2 & 0 & 3 \\ 2 & 4 & 1 & 4 \\ 3 & 6 & 1 & 7 \end{pmatrix} \in M_{3 \times 4}(\nR) \).
:::

::: {.solution}
Row reduce. Subtracting \( 2 \) times row 1 from row 2 and \( 3 \) times row 1 from row 3 gives rows \( (1, 2, 0, 3) \), \( (0, 0, 1, -2) \), \( (0, 0, 1, -2) \). Subtracting row 2 from row 3 gives the RREF
\[
\begin{pmatrix} 1 & 2 & 0 & 3 \\ 0 & 0 & 1 & -2 \\ 0 & 0 & 0 & 0 \end{pmatrix}.
\]
The pivot columns are columns \( 1 \) and \( 3 \), so \( r = 2 \), and by @thm-column-row-factorization
\[
\A = \C\R = \begin{pmatrix} 1 & 0 \\ 2 & 1 \\ 3 & 1 \end{pmatrix}\begin{pmatrix} 1 & 2 & 0 & 3 \\ 0 & 0 & 1 & -2 \end{pmatrix}.
\]
Check by rows: row 2 of \( \C\R \) is \( 2(1, 2, 0, 3) + (0, 0, 1, -2) = (2, 4, 1, 4) \), and row 3 is \( 3(1, 2, 0, 3) + (0, 0, 1, -2) = (3, 6, 1, 7) \). The last column of \( \R \) says \( \a_4 = 3\a_1 - 2\a_3 \), and indeed \( 3(1, 2, 3) - 2(0, 1, 1) = (3, 4, 7) \).
:::

## Equivalent matrices

Go back to the change-of-basis square for a map \( T \colon V \to W \) (@thm-change-of-basis-maps):
\[
\mtx{T}{\sB'}{\sC'} = \mtx{\id}{\sC}{\sC'}\,\mtx{T}{\sB}{\sC}\,\mtx{\id}{\sB'}{\sB} .
\]
When \( V \ne W \), nothing ties the basis of \( V \) to the basis of \( W \). So the two outer matrices are **unrelated** invertible matrices, of sizes \( m \times m \) and \( n \times n \). Any two matrices of the same map are related in this way, and this recurring shape deserves a name.

*Two matrices are equivalent when they describe the same linear map, with the input basis and the output basis each changed freely.*

::: {#def-equivalent-matrices}
[Equivalent matrices]

Let \( \A, \B \in M_{m \times n}(F) \). We say \( \A \) is **equivalent** to \( \B \) if there **exist** invertible matrices \( \Q \in M_m(F) \) and \( \P \in M_n(F) \) such that
\[
\B = \Q\A\P .
\]
:::

In words: we may multiply on the left by **any** invertible matrix and on the right by **any** invertible matrix, and the two need not be related. Both sizes are forced: \( \Q \) acts on the \( m \) rows and \( \P \) on the \( n \) columns. This is an equivalence relation on \( M_{m \times n}(F) \): \( \A = \I_m\A\I_n \); if \( \B = \Q\A\P \) then \( \A = \Q^{-1}\B\P^{-1} \); and if also \( \C = \Q'\B\P' \), then \( \C = (\Q'\Q)\A(\P\P') \), where products of invertible matrices are invertible by @thm-inverse-matrix-properties (part 3).

**Examples.**

- **Row equivalence.** If \( \B \) is obtained from \( \A \) by row operations, then \( \B = \E\A \) with \( \E \) invertible (@thm-row-equivalent-iff-invertible-multiple), so \( \A \) and \( \B \) are equivalent with \( \Q = \E \) and \( \P = \I_n \). Column operations correspond to multiplying on the right, and they are allowed too.
- **Similarity.** If \( \B = \P^{-1}\A\P \), then \( \A \) and \( \B \) are equivalent, with \( \Q = \P^{-1} \).
- **The identity and a swap.** \( \I_2 \) and \( S = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) are equivalent, since \( S = S\I_2\I_2 \). They are not similar, because \( \I_2 \) is similar only to itself.
- **Degenerate case.** The zero matrix \( 0_{m \times n} \) is equivalent only to itself, since \( \Q0\P = 0 \). It is the matrix of the zero map in every pair of bases.

**Non-example by minimal change.** Keep \( \B = \Q\A\P \) but drop the requirement that \( \Q \) be invertible. Then every matrix could be sent to the zero matrix with \( \Q = 0 \), and the relation would not even be symmetric: \( 0 = 0 \cdot \I_2 \cdot \I_2 \), but \( \I_2 \ne \Q0\P \) for any \( \Q, \P \). The clause "invertible" is what makes \( \Q\A\P \) a change of basis rather than an arbitrary composition.

::: {.warning}
**Equivalent is much weaker than similar.** The matrices \( \I_2 \) and \( J = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) are equivalent, since \( J = J\I_2\I_2 \) and \( J \) is invertible, but they are not similar (see the warning in the previous section). For square matrices, "equivalent" allows a different change of basis on each side, and that freedom destroys almost all the structure an operator has.
:::

How much structure survives? The rank does, since multiplying by invertible matrices does not change it (@thm-rank-product-inequality). The theorem below says that nothing else survives. The target is the simplest matrix of each rank.

For \( 0 \le r \le \min(m, n) \), let \( \N_r \in M_{m \times n}(F) \) be the block matrix
\[
\N_r \coloneqq \begin{pmatrix} \I_r & 0 \\ 0 & 0 \end{pmatrix},
\]
with \( 1 \) in positions \( (1, 1), \dots, (r, r) \) and \( 0 \) everywhere else. Its first \( r \) columns are \( \e_1, \dots, \e_r \in F^m \), and its remaining columns are zero.

::: {#thm-rank-normal-form}
[Rank Normal Form]

::: {.enumerate options="label=(\alph*)"}
1. Let \( V \) and \( W \) be finite-dimensional with \( \dim V = n \) and \( \dim W = m \), and let \( T \colon V \to W \) be linear of rank \( r \). Then there are bases \( \sB \) of \( V \) and \( \sC \) of \( W \) such that \( \mtx{T}{\sB}{\sC} = \N_r \).
2. Every \( \A \in M_{m \times n}(F) \) is equivalent to \( \N_r \), where \( r = \rank \A \).
3. Two matrices \( \A, \B \in M_{m \times n}(F) \) are equivalent if and only if \( \rank \A = \rank \B \).
:::
:::

::: {.idea}
Work backwards from the goal. \( \mtx{T}{\sB}{\sC} = \N_r \) says: \( T \) sends the first \( r \) vectors of \( \sB \) to the first \( r \) vectors of \( \sC \), and sends the last \( n - r \) vectors of \( \sB \) to \( \0 \). So ① the last \( n - r \) vectors of \( \sB \) should be a basis of \( \ker T \), and by Rank–Nullity that is exactly the right number; ② the first \( r \) vectors of \( \sB \) extend it to a basis of \( V \); ③ their images are forced to be the first \( r \) vectors of \( \sC \), and we must show they are independent, which follows by counting; ④ extend them to a basis of \( W \). These are the bases of the proof of Rank–Nullity, one on each side.
:::

::: {.proof}
(a) By the Rank–Nullity Theorem (@thm-rank-nullity), \( \dim \ker T = n - r \). Let \( (\u_{r+1}, \dots, \u_n) \) be a basis of \( \ker T \), a subspace of \( V \) by @thm-prop-kernel. By the Basis Extension Theorem (@thm-basis-extension) there are \( \u_1, \dots, \u_r \in V \) such that \( \sB = (\u_1, \dots, \u_r, \u_{r+1}, \dots, \u_n) \) is a basis of \( V \); the new vectors may be listed first, since reordering a basis gives a basis. Put \( \w_i = T\u_i \) for \( i = 1, \dots, r \).

By @thm-image-spanned-by-basis-images, \( \im T = \Span(T\u_1, \dots, T\u_n) \). Since \( T\u_j = \0 \) for \( j > r \), removing these vectors does not change the span, so \( (\w_1, \dots, \w_r) \) spans \( \im T \). This list has length \( r = \dim \im T \), so it is a basis of \( \im T \) by @thm-right-size-basis (b); in particular it is linearly independent in \( W \). By the Basis Extension Theorem there are \( \w_{r+1}, \dots, \w_m \in W \) such that \( \sC = (\w_1, \dots, \w_m) \) is a basis of \( W \).

Now read off the columns of \( \mtx{T}{\sB}{\sC} \) (@def-matrix-of-linear-map). For \( i \le r \), \( T\u_i = \w_i \), whose \( \sC \)-coordinate vector is \( \e_i \). For \( j > r \), \( T\u_j = \0 \), whose coordinate vector is \( \0 \). These are the columns of \( \N_r \).

(b) Let \( T \colon F^n \to F^m \), \( T\x = \A\x \), and let \( \sE_n \), \( \sE_m \) be the standard bases. The \( j \)-th column of \( \mtx{T}{\sE_n}{\sE_m} \) is \( \coord{\A\e_j}{\sE_m} = \A\e_j \), the \( j \)-th column of \( \A \) (@thm-matrix-times-vector-columns), so \( \mtx{T}{\sE_n}{\sE_m} = \A \). By @thm-rank-map-equals-rank-matrix, \( \rank T = \rank \A = r \). Take \( \sB \), \( \sC \) as in (a). By @thm-change-of-basis-maps,
\[
\N_r = \mtx{T}{\sB}{\sC} = \mtx{\id}{\sE_m}{\sC}\,\A\,\mtx{\id}{\sB}{\sE_n},
\]
and both outer matrices are invertible by @thm-change-of-coordinates (c). Hence \( \A \) is equivalent to \( \N_r \).

(c) (⇒) If \( \B = \Q\A\P \) with \( \Q, \P \) invertible, then \( \rank \B = \rank \A \) by @thm-rank-product-inequality. (⇐) If \( \rank \A = \rank \B = r \), then by (b) both \( \A \) and \( \B \) are equivalent to \( \N_r \). Since equivalence is symmetric and transitive, \( \A \) is equivalent to \( \B \). This proves the theorem.
:::

So the equivalence classes of \( M_{m \times n}(F) \) are exactly the sets of matrices of rank \( r \), for \( r = 0, 1, \dots, \min(m, n) \): there are \( \min(m, n) + 1 \) of them, whatever the field. Every linear map between finite-dimensional spaces looks like "keep \( r \) coordinates and delete the rest" once the bases on both sides are chosen well. **The right pair of bases makes any single map trivial.**

::: {.remark}
Contrast this with operators. For \( T \in \cL(V) \) we must use **one** basis for input and output, and the relation becomes similarity. There the rank is far from the whole story: \( \I_2 \) and \( \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) have the same rank but are not similar. Classifying operators up to a change of one basis is a much harder problem, answered in Chapter 9 by the Jordan and rational canonical forms.
:::

The proof is also an algorithm. To find \( \Q \) and \( \P \) for a concrete matrix, compute a basis of \( \nul(\A) \), extend it, and take images.

::: {#exm-rank-normal-form}
[Bringing a \( 2 \times 3 \) matrix to normal form]

Let \( \A = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 4 & 3 \end{pmatrix} \in M_{2 \times 3}(\nR) \). Find invertible \( \Q \in M_2(\nR) \) and \( \P \in M_3(\nR) \) with \( \Q\A\P = \N_r \).
:::

::: {.solution}
Subtracting \( 2 \) times row 1 from row 2 gives \( \begin{pmatrix} 1 & 2 & 1 \\ 0 & 0 & 1 \end{pmatrix} \), so \( r = \rank \A = 2 \), and the solutions of \( \A\x = \0 \) satisfy \( x_3 = 0 \), \( x_1 = -2x_2 \). Hence \( \nul(\A) = \Span((-2, 1, 0)) \), as Rank–Nullity predicts (\( 3 - 2 = 1 \)).

Following the proof, let \( \u_3 = (-2, 1, 0) \), and extend with \( \u_1 = \e_1 \), \( \u_2 = \e_3 \). The list \( (\e_1, \e_3, \u_3) \) is independent: in \( a\e_1 + b\e_3 + c(-2, 1, 0) = (a - 2c, c, b) = \0 \), the second and third entries give \( c = b = 0 \), and then \( a = 0 \). So it is a basis \( \sB \) of \( \nR^3 \). The images are \( \w_1 = \A\e_1 = (1, 2) \) and \( \w_2 = \A\e_3 = (1, 3) \), which already form a basis \( \sC \) of \( \nR^2 \) since \( r = m = 2 \). Therefore
\[
\P = \mtx{\id}{\sB}{\sE_3} = \begin{pmatrix} 1 & 0 & -2 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}, \qquad \Q = \mtx{\id}{\sE_2}{\sC} = \begin{pmatrix} 1 & 1 \\ 2 & 3 \end{pmatrix}^{-1} = \begin{pmatrix} 3 & -1 \\ -2 & 1 \end{pmatrix},
\]
using @thm-change-of-coordinates (c) and @thm-two-by-two-inverse. Check: \( \A\P = \begin{pmatrix} 1 & 1 & 0 \\ 2 & 3 & 0 \end{pmatrix} \) (the columns are \( \w_1 \), \( \w_2 \), \( \0 \)), and
\[
\Q\A\P = \begin{pmatrix} 3 & -1 \\ -2 & 1 \end{pmatrix}\begin{pmatrix} 1 & 1 & 0 \\ 2 & 3 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} = \N_2 .
\]
The pair \( (\Q, \P) \) is far from unique; any choice of extension gives another.
:::

::: {.check}
How many equivalence classes does \( M_{3 \times 2}(F) \) have, and which is the class of \( \begin{pmatrix} 1 & 2 \\ 2 & 4 \\ 0 & 0 \end{pmatrix} \)?
:::

::: {.solution}
Ranks in \( M_{3 \times 2}(F) \) range over \( 0, 1, 2 \), so there are \( \min(3, 2) + 1 = 3 \) classes by @thm-rank-normal-form (c). The given matrix is non-zero and its second column is twice the first, so its rank is \( 1 \), and it lies in the class of \( \N_1 \): all matrices of rank \( 1 \).
:::

## Rank inequalities for compositions

The rank of a composition cannot exceed the rank of either factor, and it cannot fall too far either. Both facts come from the same observation: \( ST \) is \( S \) applied to the subspace \( \im T \). For a subspace \( X \subseteq W \) and a linear map \( S \colon W \to U \), the **restriction** \( S|_X \colon X \to U \), \( \x \mapsto S\x \), is linear, since its values are those of \( S \). Its kernel is \( \ker S \cap X \).

::: {#thm-rank-of-composition}
[Rank of a Composition]

Let \( T \colon V \to W \) and \( S \colon W \to U \) be linear, with \( V \) and \( W \) finite-dimensional. Then
\[
\rank(ST) \le \min(\rank S, \rank T).
\]
:::

::: {.proof}
Consider the restriction \( S' = S|_{\im T} \colon \im T \to U \). For \( \v \in V \), \( (ST)(\v) = S(T\v) = S'(T\v) \), so \( \im(ST) \subseteq \im S' \); conversely every \( S'\w \) with \( \w = T\v \in \im T \) equals \( (ST)(\v) \). Hence \( \im(ST) = \im S' \). Since \( \im T \) is finite-dimensional (a subspace of \( W \), @thm-subspace-dimension), Rank–Nullity (@thm-rank-nullity) applied to \( S' \) gives
\[
\rank(ST) = \dim \im S' = \dim \im T - \dim \ker S' \le \rank T .
\]
Also \( \im(ST) = \im S' \subseteq \im S \), and \( \im S \) is finite-dimensional by Rank–Nullity for \( S \), so \( \rank(ST) \le \rank S \) by @thm-subspace-dimension. This proves the theorem.
:::

The lower bound uses the same restriction, but now we control its kernel instead of ignoring it.

::: {#thm-sylvester-rank-inequality}
[Sylvester's Rank Inequality]

Let \( T \colon V \to W \) and \( S \colon W \to U \) be linear, with \( V \) and \( W \) finite-dimensional. Then
\[
\rank(ST) \ge \rank S + \rank T - \dim W .
\]
In matrix form: for \( \A \in M_{m \times n}(F) \) and \( \B \in M_{n \times p}(F) \), \( \rank(\A\B) \ge \rank \A + \rank \B - n \).
:::

::: {.idea}
Of the \( \rank T \) dimensions that reach \( W \), the map \( S \) can destroy only those lying in \( \ker S \), and \( \ker S \) has dimension \( \dim W - \rank S \). Rank–Nullity for the restriction \( S|_{\im T} \) turns this sentence into an inequality.
:::

::: {.proof}
Let \( S' = S|_{\im T} \), so that \( \im S' = \im(ST) \) as in the proof of @thm-rank-of-composition, and \( \ker S' = \ker S \cap \im T \subseteq \ker S \). By Rank–Nullity for \( S' \) and then for \( S \),
\[
\rank T = \rank(ST) + \dim(\ker S \cap \im T) \le \rank(ST) + \dim \ker S = \rank(ST) + \dim W - \rank S,
\]
where the inequality is @thm-subspace-dimension. Rearranging gives the claim. For matrices, apply it to \( S\y = \A\y \) on \( W = F^n \) and \( T\x = \B\x \) on \( V = F^p \): the matrix of \( ST \) in standard bases is \( \A\B \) by @thm-matrix-of-composition, and ranks of maps and matrices agree by @thm-rank-map-equals-rank-matrix.
:::

If you worked @exr-rank-nullity-c1, you have seen this proof already; we record the result here as a theorem so that later arguments can cite it. A typical use: if \( \A\B = 0 \) with \( \A \in M_{m \times n}(F) \) and \( \B \in M_{n \times p}(F) \), then \( 0 \ge \rank \A + \rank \B - n \), that is,
\[
\rank \A + \rank \B \le n .
\]
For instance, there are no \( \A, \B \in M_3(\nR) \) of rank \( 2 \) with \( \A\B = 0 \).

::: {.warning}
**The rank of a product depends on the order of the factors.** For \( \A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \) and \( \B = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \), \( \A\B = \B \) has rank \( 1 \) but \( \B\A = 0 \) has rank \( 0 \). @thm-rank-product-inequality and Sylvester's inequality bound \( \rank(\A\B) \) from both sides; they do not determine it, and they say nothing that would make \( \rank(\A\B) = \rank(\B\A) \).
:::

## Exercises

### A. Check your understanding

::: {#exr-rank-factorization-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define what it means for \( \A, \B \in M_{m \times n}(F) \) to be equivalent.
2. State the Rank Normal Form theorem for a matrix \( \A \in M_{m \times n}(F) \).
3. True or false: equivalent square matrices are similar. Justify your answer.
4. True or false: \( \rank(\A\B) = \rank(\B\A) \) for all \( \A, \B \in M_n(F) \). Justify your answer.
5. How many equivalence classes does \( M_{2 \times 5}(\nF_7) \) have?
6. In the proof of the normal form for \( T \colon V \to W \), which vectors form the end of the basis of \( V \), and which vectors form the start of the basis of \( W \)?
:::
:::

::: {.solution}
(a) There are invertible \( \Q \in M_m(F) \) and \( \P \in M_n(F) \) with \( \B = \Q\A\P \) (@def-equivalent-matrices).

(b) If \( r = \rank \A \), there are invertible \( \Q, \P \) with \( \Q\A\P = \begin{pmatrix} \I_r & 0 \\ 0 & 0 \end{pmatrix} \); and two \( m \times n \) matrices are equivalent if and only if they have the same rank (@thm-rank-normal-form).

(c) False. \( \I_2 \) and \( \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) both have rank \( 2 \), so they are equivalent, but \( \I_2 \) is similar only to itself.

(d) False. With \( \A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \) and \( \B = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \), \( \rank(\A\B) = 1 \) and \( \rank(\B\A) = 0 \).

(e) The possible ranks are \( 0, 1, 2 \), so there are \( 3 \) classes. The field plays no role.

(f) The last \( n - r \) vectors of the basis of \( V \) form a basis of \( \ker T \). The first \( r \) vectors of the basis of \( W \) are the images of the first \( r \) basis vectors of \( V \), and they form a basis of \( \im T \).
:::

### B. Practice

::: {#exr-rank-factorization-b1}
[B1: A column–row factorization]

Find the column–row factorization of
\[
\A = \begin{pmatrix} 1 & -1 & 2 & 0 \\ 2 & -2 & 5 & 1 \\ 1 & -1 & 3 & 1 \end{pmatrix} \in M_{3 \times 4}(\nR).
\]
Hence write the second and fourth columns of \( \A \) as combinations of its pivot columns.
:::

::: {.solution}
Subtract \( 2 \) times row 1 from row 2 and row 1 from row 3: the rows become \( (1, -1, 2, 0) \), \( (0, 0, 1, 1) \), \( (0, 0, 1, 1) \). Subtract row 2 from row 3, and then \( 2 \) times row 2 from row 1:
\[
\text{RREF} = \begin{pmatrix} 1 & -1 & 0 & -2 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix}.
\]
The pivot columns are \( 1 \) and \( 3 \), so \( \rank \A = 2 \), and by @thm-column-row-factorization
\[
\A = \begin{pmatrix} 1 & 2 \\ 2 & 5 \\ 1 & 3 \end{pmatrix}\begin{pmatrix} 1 & -1 & 0 & -2 \\ 0 & 0 & 1 & 1 \end{pmatrix}.
\]
Check by rows: \( 2(1, -1, 0, -2) + 5(0, 0, 1, 1) = (2, -2, 5, 1) \) and \( (1, -1, 0, -2) + 3(0, 0, 1, 1) = (1, -1, 3, 1) \); row 1 is \( (1, -1, 0, -2) + 2(0, 0, 1, 1) \). Reading columns \( 2 \) and \( 4 \) of \( \R \): \( \a_2 = -\a_1 \) and \( \a_4 = -2\a_1 + \a_3 \). Indeed \( -2(1, 2, 1) + (2, 5, 3) = (0, 1, 1) = \a_4 \).
:::

::: {#exr-rank-factorization-b2}
[B2: Normal form of a rank-one matrix]

Let \( \A = \begin{pmatrix} 1 & -1 & 2 \\ -2 & 2 & -4 \end{pmatrix} \in M_{2 \times 3}(\nR) \). Find invertible \( \Q \in M_2(\nR) \) and \( \P \in M_3(\nR) \) such that \( \Q\A\P = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} \), following the proof of @thm-rank-normal-form.
:::

::: {.solution}
Row 2 is \( -2 \) times row 1, and \( \A \ne 0 \), so \( \rank \A = 1 \). The null space is \( \{ x_1 - x_2 + 2x_3 = 0 \} \); setting the free variables \( x_2, x_3 \) to \( (1, 0) \) and \( (0, 1) \) gives the basis \( \u_2 = (1, 1, 0) \), \( \u_3 = (-2, 0, 1) \). Extend with \( \u_1 = \e_1 \): in \( a\e_1 + b\u_2 + c\u_3 = (a + b - 2c, b, c) = \0 \), the last two entries give \( b = c = 0 \) and then \( a = 0 \), so \( \sB = (\e_1, \u_2, \u_3) \) is a basis of \( \nR^3 \). Its first image is \( \w_1 = \A\e_1 = (1, -2) \), which we extend to the basis \( \sC = ((1, -2), \e_2) \) of \( \nR^2 \) (independent, since \( a(1, -2) + b(0, 1) = (a, -2a + b) = \0 \) forces \( a = b = 0 \)). Then
\[
\P = \begin{pmatrix} 1 & 1 & -2 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \Q = \begin{pmatrix} 1 & 0 \\ -2 & 1 \end{pmatrix}^{-1} = \begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix}.
\]
Check: \( \A\P \) has columns \( \A\e_1 = (1, -2) \), \( \A\u_2 = \0 \), \( \A\u_3 = \0 \), and \( \Q(1, -2) = (1, 0) \). So \( \Q\A\P = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} \). Both \( \Q \) and \( \P \) are invertible by @thm-change-of-coordinates (c).
:::

::: {#exr-rank-factorization-b3}
[B3: Rank-one pieces]

Let \( \A \in M_{m \times n}(F) \).

::: {.enumerate options="label=(\alph*)"}
1. Use @thm-column-row-factorization to show that if \( \rank \A = 1 \), then \( \A = \x\y\tp \) for some non-zero \( \x \in F^m \) and \( \y \in F^n \).
2. Show that if \( \rank \A = r \ge 1 \), then \( \A \) is a sum of \( r \) matrices of rank \( 1 \), and that it is not a sum of fewer than \( r \) matrices of rank \( 1 \).
3. Write \( \begin{pmatrix} 1 & 2 & 0 & 3 \\ 2 & 4 & 1 & 4 \\ 3 & 6 & 1 & 7 \end{pmatrix} \) as a sum of two rank-one matrices.
:::
:::

::: {.solution}
(a) With \( r = 1 \), \( \C \in M_{m \times 1}(F) \) is a single column \( \x \), and \( \R \in M_{1 \times n}(F) \) is a single row, which we write as \( \y\tp \) with \( \y \in F^n \). So \( \A = \x\y\tp \). Both are non-zero: the columns of \( \C \) and the rows of \( \R \) are linearly independent by @thm-column-row-factorization, and a list containing a zero vector is dependent. (This recovers one direction of @exr-rank-c2.)

(b) Write \( \A = \C\R \) with columns \( \c_1, \dots, \c_r \) of \( \C \) and rows \( \r_1, \dots, \r_r \) of \( \R \), and let \( c_{ik} \), \( r_{kl} \) be the entries of \( \C \), \( \R \). The \( m \times n \) matrix \( \c_k\r_k \) has \( (i, l) \)-entry \( c_{ik}r_{kl} \), so by @thm-three-views-of-product (1),
\[
(\C\R)_{il} = \sum_{k=1}^{r} c_{ik}r_{kl} = \sum_{k=1}^{r} (\c_k\r_k)_{il}, \qquad\text{that is,}\qquad \A = \c_1\r_1 + \dots + \c_r\r_r .
\]
Each \( \c_k\r_k \) has rank \( 1 \) by the (⇐) direction of @exr-rank-c2, since \( \c_k \ne \0 \) (a column of \( \C \), whose columns are independent) and \( \r_k \ne 0 \) (a row of \( \R \), whose rows are independent). If \( \A = \A_1 + \dots + \A_s \) with each \( \rank \A_i = 1 \), then by @exr-rank-c1 applied repeatedly, \( r = \rank \A \le \rank \A_1 + \dots + \rank \A_s = s \).

(c) By @exm-column-row-factorization, \( \A = \C\R \) with \( \C = \begin{pmatrix} 1 & 0 \\ 2 & 1 \\ 3 & 1 \end{pmatrix} \) and \( \R = \begin{pmatrix} 1 & 2 & 0 & 3 \\ 0 & 0 & 1 & -2 \end{pmatrix} \), so
\[
\A = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}\begin{pmatrix} 1 & 2 & 0 & 3 \end{pmatrix} + \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}\begin{pmatrix} 0 & 0 & 1 & -2 \end{pmatrix} = \begin{pmatrix} 1 & 2 & 0 & 3 \\ 2 & 4 & 0 & 6 \\ 3 & 6 & 0 & 9 \end{pmatrix} + \begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & -2 \\ 0 & 0 & 1 & -2 \end{pmatrix}.
\]
:::

### C. Going deeper

::: {#exr-rank-factorization-c1}
[C1: Frobenius's rank inequality]

Let \( \A \in M_{m \times n}(F) \), \( \B \in M_{n \times p}(F) \) and \( \C \in M_{p \times q}(F) \). Write \( N = \nul(\A) \subseteq F^n \), and let \( S \colon F^n \to F^m \) be \( S\y = \A\y \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \col(\A\B) = \{ \A\y : \y \in \col(\B) \} \), and deduce from Rank–Nullity for \( S|_{\col(\B)} \) that \( \rank(\A\B) = \rank \B - \dim(N \cap \col(\B)) \).
2. Show similarly that \( \rank(\A\B\C) = \rank(\B\C) - \dim(N \cap \col(\B\C)) \).
3. Prove that \( \col(\B\C) \subseteq \col(\B) \), and deduce **Frobenius's inequality**
   \[
   \rank(\A\B\C) + \rank \B \ge \rank(\A\B) + \rank(\B\C).
   \]
4. Deduce Sylvester's inequality for matrices from (c).
:::

*Hint: for (d), look for a special choice of the middle factor.*
:::

::: {.solution}
(a) By @thm-three-views-of-product, every vector \( \A\B\x \) equals \( \A\y \) with \( \y = \B\x \in \col(\B) \); conversely every \( \y \in \col(\B) \) is \( \B\x \) for some \( \x \), and then \( \A\y = (\A\B)\x \in \col(\A\B) \). So \( \col(\A\B) = \im(S|_{\col(\B)}) \). The kernel of \( S|_{\col(\B)} \) is \( N \cap \col(\B) \), and \( \col(\B) \) is finite-dimensional, so by @thm-rank-nullity,
\[
\rank \B = \dim \col(\B) = \rank(\A\B) + \dim(N \cap \col(\B)).
\]

(b) The same argument with \( \B\C \) in place of \( \B \) gives \( \col(\A\B\C) = \im(S|_{\col(\B\C)}) \), with kernel \( N \cap \col(\B\C) \), so \( \rank(\B\C) = \rank(\A\B\C) + \dim(N \cap \col(\B\C)) \).

(c) Every vector \( \B\C\x = \B(\C\x) \) lies in \( \col(\B) \), so \( \col(\B\C) \subseteq \col(\B) \). Hence \( N \cap \col(\B\C) \subseteq N \cap \col(\B) \), and by @thm-subspace-dimension, \( \dim(N \cap \col(\B\C)) \le \dim(N \cap \col(\B)) \). By (b) and then (a),
\[
\rank(\A\B\C) = \rank(\B\C) - \dim(N \cap \col(\B\C)) \ge \rank(\B\C) - \dim(N \cap \col(\B)) = \rank(\B\C) - \rank \B + \rank(\A\B).
\]
Rearranging gives Frobenius's inequality.

(d) Let \( \A \in M_{m \times n}(F) \) and \( \C \in M_{n \times q}(F) \), and apply (c) with \( p = n \) and \( \B = \I_n \). Then \( \rank(\A\C) + n \ge \rank \A + \rank \C \), since \( \rank \I_n = n \). This is @thm-sylvester-rank-inequality for matrices.
:::

::: {#exr-rank-factorization-c2}
[C2: Counting over \( \nF_2 \)]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( M_2(\nF_2) \) contains exactly \( 1 \) matrix of rank \( 0 \), \( 6 \) of rank \( 2 \) and \( 9 \) of rank \( 1 \).
2. Deduce the sizes of the equivalence classes of \( M_2(\nF_2) \).
3. Compare with similarity: how many matrices of \( M_2(\nF_2) \) are similar to \( \I_2 \)? Is the class of \( \I_2 \) under equivalence a union of several similarity classes?
:::
:::

::: {.solution}
(a) The only matrix of rank \( 0 \) is \( 0 \). A matrix has rank \( 2 \) exactly when its two columns span \( \nF_2^2 \), that is (@thm-right-size-basis), when they form a basis of \( \nF_2^2 \). The first column can be any of the \( 3 \) non-zero vectors of \( \nF_2^2 \). The second must lie outside the span of the first, which has \( 2 \) elements, so there are \( 4 - 2 = 2 \) choices. That gives \( 3 \cdot 2 = 6 \) matrices of rank \( 2 \). Since \( \lvert M_2(\nF_2) \rvert = 2^4 = 16 \), the remaining \( 16 - 1 - 6 = 9 \) matrices have rank \( 1 \).

(b) By @thm-rank-normal-form (c), the classes are the sets of matrices of a fixed rank, of sizes \( 1 \), \( 9 \) and \( 6 \).

(c) \( \I_2 \) is similar only to itself, so its similarity class has \( 1 \) element, while its equivalence class, the invertible matrices, has \( 6 \). Since similar matrices are equivalent, each equivalence class is a union of similarity classes, and here the class of the \( 6 \) invertible matrices contains the similarity class \( \{ \I_2 \} \) together with others. For example \( \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) is invertible but not similar to \( \I_2 \), so there are at least two similarity classes inside.
:::
