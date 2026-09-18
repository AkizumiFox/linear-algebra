# The Sylvester Equation

Chapter 7 wrote an operator with an invariant subspace as a block triangular matrix, with a corner block \( \C \) recording how the subspace fails to have an invariant complement (@thm-invariant-subspace-block-triangular). Chapter 9 spent its length on what to do when that corner cannot be cleared. The question of *when* it can be cleared has an exact answer, and the answer is a linear equation in the unknown matrix \( \X \):
\[
\A\X - \X\B = \C .
\]
Chapter 7 already turned this equation into an ordinary linear system with the Kronecker product, and stopped one step short of the criterion because that step needs eigenvalues. We have eigenvalues now, and Schur's factorization of Section 1 to organize them. This section proves the criterion, uses it to clear corners, and reads off what it says about the matrices that commute with a given one.

Throughout, the field is \( \nC \) unless stated otherwise, and \( \A \in M_m(\nC) \), \( \B \in M_n(\nC) \), while the unknown \( \X \) and the data \( \C \) live in \( M_{m \times n}(\nC) \).

## The Sylvester operator

The left-hand side of the equation is linear in \( \X \): replacing \( \X \) by \( \X + \X' \) or by \( c\X \) does the same to \( \A\X - \X\B \), because matrix multiplication is bilinear (@thm-matrix-multiplication-properties). So the whole question is about one linear map, and it deserves a name.

*Solving \( \A\X - \X\B = \C \) means inverting a single linear operator on the space of \( m \times n \) matrices.*

::: {#def-sylvester-operator}
[Sylvester operator]

Let \( \A \in M_m(F) \) and \( \B \in M_n(F) \). The **Sylvester operator** of the pair \( (\A, \B) \) is
\[
\cS_{\A,\B} \colon M_{m \times n}(F) \to M_{m \times n}(F), \qquad \cS_{\A,\B}(\X) = \A\X - \X\B .
\]
The equation \( \A\X - \X\B = \C \), for a given \( \C \in M_{m \times n}(F) \), is the **Sylvester equation**.
:::

In words: \( \cS_{\A,\B} \) multiplies by \( \A \) on the left, multiplies by \( \B \) on the right, and subtracts. It is an operator on a space of dimension \( mn \), not on \( F^m \) or \( F^n \), and that is the only thing that makes the equation look harder than \( \A\x = \b \).

Three special cases are worth keeping in view.

1. **\( \B = \0 \).** Then \( \cS_{\A,\0}(\X) = \A\X \), and the equation is \( n \) copies of \( \A\x = \b \), one for each column of \( \X \) (@exr-kronecker-product-b2). It is uniquely solvable for every \( \C \) exactly when \( \A \) is invertible, that is, when \( 0 \notin \spec(\A) \). Since \( \spec(\0) = \{0\} \), this already matches the criterion we are heading for.
2. **\( \B = \A \) and \( \C = \0 \).** Then \( \ker \cS_{\A,\A} \) is the **commutant** of \( \A \), the set of matrices commuting with \( \A \). This is the question Chapter 7 opened with, and Chapter 9 §04 studied it for a single Jordan or Weyr block.
3. **\( m = n = 1 \).** Then \( \cS_{a,b}(x) = (a - b)x \), which is invertible exactly when \( a \neq b \). The general criterion will be this one, run over all pairs of eigenvalues.

**Non-example by minimal change.** The map \( \X \mapsto \A\X - \X\B - \X\tp \) is still linear on \( M_n(F) \), but it is not a Sylvester operator: the transpose is not of the form "multiply on one side". Everything below uses the two-sided product shape and nothing else.

Chapter 7 already wrote the matrix of \( \cS_{\A,\B} \). Stacking the columns of \( \X \) with the vectorization \( \vecop \) of @def-vec-operator and applying the vec identity @thm-vec-identity twice, once with \( \B = \I_n \) and once with \( \A = \I_m \),
\[
\begin{aligned}
\vecop\big(\cS_{\A,\B}(\X)\big) &= \K\,\vecop \X, \\
\K &\coloneqq \I_n \otimes \A - \B\tp \otimes \I_m .
\end{aligned}
\]{#eq-sylvester-kronecker}
Here \( \K \in M_{mn}(F) \), and \( \vecop \colon M_{m \times n}(F) \to F^{mn} \) is an isomorphism. So @eq-sylvester-kronecker says that \( \K \) *is* the matrix of \( \cS_{\A,\B} \) with respect to the basis of matrix units ordered column by column. In particular \( \cS_{\A,\B} \) is invertible if and only if \( \K \) is.

That is exactly where Chapter 7 left the problem. What it could not do was compute the eigenvalues of \( \K \).

## The spectrum of a Kronecker sum

Chapter 7 proved how the Kronecker product treats rank, trace and determinant (@thm-kronecker-rank-trace-det) and how it treats products, transposes and inverses (@thm-kronecker-properties). It proved nothing about eigenvalues, and @exr-kronecker-product-c2 got only as far as the case where both factors are already triangular. Schur closes the gap, because over \( \nC \) every matrix can be made triangular unitarily, and the mixed product rule carries a pair of unitary conjugations through the Kronecker product in one step.

::: {#lem-kronecker-sum-spectrum}
[The Eigenvalues of a Kronecker Sum]

Let \( \A \in M_m(\nC) \) with eigenvalues \( \lambda_1, \dots, \lambda_m \) and let \( \B \in M_n(\nC) \) with eigenvalues \( \mu_1, \dots, \mu_n \), each list repeated according to algebraic multiplicity. Then the \( mn \) eigenvalues of
\[
\K = \I_n \otimes \A - \B\tp \otimes \I_m \in M_{mn}(\nC),
\]
listed with algebraic multiplicity, are the \( mn \) differences \( \lambda_i - \mu_j \) \( (1 \le i \le m,\ 1 \le j \le n) \).
:::

::: {.idea}
Triangularize both ingredients at once. Schur (@cor-schur-matrix) writes \( \A = \U\T\U^{*} \) and \( \B\tp = \V\S\V^{*} \) with \( \T, \S \) upper triangular. The mixed product rule then conjugates *both* summands of \( \K \) by the single unitary matrix \( \V \otimes \U \), because \( \I_n \otimes \A \) and \( \B\tp \otimes \I_m \) each have one trivial factor to absorb the other conjugation. What is left is \( \I_n \otimes \T - \S \otimes \I_m \), and a Kronecker product with one triangular and one identity factor is triangular, so the eigenvalues are visible on the diagonal.
:::

::: {.proof}
By @cor-schur-matrix there are a unitary \( \U \in M_m(\nC) \) and an upper triangular \( \T \in M_m(\nC) \) with \( \A = \U\T\U^{*} \) and \( t_{ii} = \lambda_i \). By @prp-left-eigenvectors-transpose (b), \( p_{\B\tp} = p_{\B} \), so \( \B\tp \) has eigenvalue list \( \mu_1, \dots, \mu_n \); applying @cor-schur-matrix to \( \B\tp \) gives a unitary \( \V \in M_n(\nC) \) and an upper triangular \( \S \in M_n(\nC) \) with \( \B\tp = \V\S\V^{*} \) and \( s_{jj} = \mu_j \).

Put \( \W = \V \otimes \U \in M_{mn}(\nC) \). Conjugating every entry of \( \A \otimes \B \) conjugates every block \( a_{ij}\B \), so \( \conj{\A \otimes \B} = \conj{\A} \otimes \conj{\B} \) (@def-kronecker-product), and combining this with @thm-kronecker-properties (d) gives \( (\A \otimes \B)^{*} = \A^{*} \otimes \B^{*} \) whenever the product is defined. Hence \( \W^{*} = \V^{*} \otimes \U^{*} \), and by the mixed product rule @thm-kronecker-properties (c),
\[
\W^{*}\W = (\V^{*}\V) \otimes (\U^{*}\U) = \I_n \otimes \I_m = \I_{mn},
\]
so \( \W \) is unitary. Using the mixed product rule twice more,
\[
\begin{aligned}
\W(\I_n \otimes \T)\W^{*} &= (\V\I_n\V^{*}) \otimes (\U\T\U^{*}) = \I_n \otimes \A, \\
\W(\S \otimes \I_m)\W^{*} &= (\V\S\V^{*}) \otimes (\U\I_m\U^{*}) = \B\tp \otimes \I_m .
\end{aligned}
\]
Subtracting, \( \W(\I_n \otimes \T - \S \otimes \I_m)\W^{*} = \K \), so \( \K \) is similar to
\[
\R \coloneqq \I_n \otimes \T - \S \otimes \I_m .
\]

**\( \R \) is upper triangular.** Label the rows and columns of an \( mn \times mn \) matrix by pairs as in @def-kronecker-product: row \( (j-1)m + i \) with \( 1 \le j \le n \), \( 1 \le i \le m \), and likewise column \( (l-1)m + k \). In those labels the entries of the two summands are
\[
\begin{aligned}
(\I_n \otimes \T)_{(j-1)m+i,\,(l-1)m+k} &= \delta_{jl}\,t_{ik}, \\
(\S \otimes \I_m)_{(j-1)m+i,\,(l-1)m+k} &= s_{jl}\,\delta_{ik} .
\end{aligned}
\]
The first is non-zero only when \( j = l \) and \( i \le k \), since \( \T \) is upper triangular; then \( (j-1)m + i \le (l-1)m + k \). The second is non-zero only when \( j \le l \) and \( i = k \); if \( j = l \) the two labels are equal, and if \( j < l \) then
\[
(j-1)m + i \le (j-1)m + m = jm \le (l-1)m < (l-1)m + k ,
\]
using \( i \le m \), \( j \le l - 1 \) and \( k \ge 1 \). So each summand vanishes below the diagonal, and so does \( \R \).

**The diagonal.** Taking \( j = l \) and \( i = k \) above, the diagonal entry of \( \R \) in position \( (j-1)m + i \) is \( t_{ii} - s_{jj} = \lambda_i - \mu_j \). As \( (i, j) \) runs over all \( mn \) pairs, so does the position \( (j-1)m + i \), by division with remainder.

By @thm-diagonal-of-triangular-form (a), applied to the operator \( T_{\R} \) on \( \nC^{mn} \) and the standard basis, \( p_{\R} = \prod_{i,j}\big(x - (\lambda_i - \mu_j)\big) \). Since \( \K \sim \R \), @thm-charpoly-similarity-invariant gives \( p_{\K} = p_{\R} \). This proves the lemma.
:::

Two remarks on what the proof used. The hypothesis \( F = \nC \) entered once, in Schur, and through Schur it is the Fundamental Theorem of Algebra again. And the unitarity of \( \W \) was a convenience, not a necessity: any similarity triangularizing \( \A \) and \( \B\tp \) would do, but Schur hands us one for free and the Kronecker product of two unitary matrices is unitary, which is worth recording on its own.

## When the equation is uniquely solvable

The criterion now costs one line.

::: {#thm-sylvester-equation}
[Sylvester's Theorem]

Let \( \A \in M_m(\nC) \) and \( \B \in M_n(\nC) \). The following are equivalent.

::: {.enumerate options="label=(\alph*)"}
1. \( \spec(\A) \cap \spec(\B) = \varnothing \): the two matrices have **no common eigenvalue**.
2. The Sylvester operator \( \cS_{\A,\B} \colon \X \mapsto \A\X - \X\B \) is invertible on \( M_{m \times n}(\nC) \).
3. For every \( \C \in M_{m \times n}(\nC) \), the equation \( \A\X - \X\B = \C \) has **exactly one** solution \( \X \).
4. The only \( \X \in M_{m \times n}(\nC) \) with \( \A\X = \X\B \) is \( \X = \0 \).
:::
:::

::: {.proof}
By @eq-sylvester-kronecker the isomorphism \( \vecop \) turns \( \cS_{\A,\B} \) into the matrix \( \K = \I_n \otimes \A - \B\tp \otimes \I_m \): a matrix \( \X \) solves \( \A\X - \X\B = \C \) if and only if the vector \( \vecop\X \) solves \( \K\y = \vecop\C \), and every \( \y \in \nC^{mn} \) and every \( \z \in \nC^{mn} \) arise this way. Transported through \( \vecop \), statements (b), (c) and (d) say respectively that \( \K \) is invertible, that \( \K\y = \z \) has exactly one solution for every \( \z \), and that \( \K\y = \0 \) forces \( \y = \0 \). These three are equivalent by @thm-invertible-tfae, parts (a), (e) and (b): (e) gives existence for every \( \z \), and (b) upgrades it to uniqueness, since two solutions differ by a member of the null space.

It remains to match (a) with (b). By @thm-invertible-tfae-eigen, \( \K \) is invertible if and only if \( 0 \notin \spec(\K) \). By @lem-kronecker-sum-spectrum, \( \spec(\K) = \{\lambda_i - \mu_j\} \), where \( \lambda_1, \dots, \lambda_m \) and \( \mu_1, \dots, \mu_n \) list the eigenvalues of \( \A \) and of \( \B \). So \( 0 \in \spec(\K) \) if and only if \( \lambda_i = \mu_j \) for some pair \( (i, j) \), that is, if and only if \( \A \) and \( \B \) have a common eigenvalue. Negating both sides matches (a) with (b), and the proof is complete.
:::

This is the statement Chapter 7 promised. At the end of @exm-sylvester-equation-vec it was said that over \( \nC \) the equation \( \A\X - \X\B = \C \) is uniquely solvable for every \( \C \) exactly when \( \A \) and \( \B \) have no common eigenvalue, and that the criterion needs eigenvalues and would be proved in Chapter 11. Parts (a) and (c) of @thm-sylvester-equation are that sentence, and the eigenvalues it needed were supplied by @lem-kronecker-sum-spectrum. The quantitative version — *how badly* conditioned the equation is when the spectra are close but disjoint — is a separate matter, and belongs with perturbation theory in Chapter 19.

Part (d) is the version used most often in practice, because it is a statement with no data in it: to show that some matrix is zero, exhibit it as a solution of \( \A\X = \X\B \) for a pair with disjoint spectra. The corollary on commutants below is that move and nothing else.

::: {#exm-sylvester-solve-2x2}
[Solving a Sylvester Equation]

Over \( \nC \), solve \( \A\X - \X\B = \C \) for
\[
\A = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}, \quad \B = \begin{pmatrix} 1 & 0 \\ 2 & -1 \end{pmatrix}, \quad \C = \begin{pmatrix} 4 & -2 \\ 0 & 4 \end{pmatrix}.
\]
:::

::: {.solution}
The matrix \( \A \) is upper triangular, so \( \spec(\A) = \{2, 3\} \) (@thm-diagonal-of-triangular-form); \( \B \) is lower triangular, so \( \spec(\B) = \{1, -1\} \). The spectra are disjoint, and by @thm-sylvester-equation there is exactly one solution.

To find it, use @eq-sylvester-kronecker. Here \( \B\tp = \begin{pmatrix} 1 & 2 \\ 0 & -1 \end{pmatrix} \), so by @def-kronecker-product
\[
\I_2 \otimes \A = \begin{pmatrix} 2 & 1 & 0 & 0 \\ 0 & 3 & 0 & 0 \\ 0 & 0 & 2 & 1 \\ 0 & 0 & 0 & 3 \end{pmatrix}, \qquad \B\tp \otimes \I_2 = \begin{pmatrix} 1 & 0 & 2 & 0 \\ 0 & 1 & 0 & 2 \\ 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & -1 \end{pmatrix},
\]
and their difference is
\[
\K = \begin{pmatrix} 1 & 1 & -2 & 0 \\ 0 & 2 & 0 & -2 \\ 0 & 0 & 3 & 1 \\ 0 & 0 & 0 & 4 \end{pmatrix}.
\]
Its diagonal entries are \( 1, 2, 3, 4 \), which are the four differences \( 2 - 1 \), \( 3 - 1 \), \( 2 - (-1) \), \( 3 - (-1) \), as @lem-kronecker-sum-spectrum predicts; none is zero, confirming invertibility.

With \( \vecop \X = (x_{11}, x_{21}, x_{12}, x_{22}) \) and \( \vecop \C = (4, 0, -2, 4) \), back substitution in \( \K\vecop \X = \vecop \C \) gives \( 4x_{22} = 4 \), so \( x_{22} = 1 \); then \( 3x_{12} + 1 = -2 \), so \( x_{12} = -1 \); then \( 2x_{21} - 2 = 0 \), so \( x_{21} = 1 \); then \( x_{11} + 1 + 2 = 4 \), so \( x_{11} = 1 \). Hence
\[
\X = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}.
\]
*Check:* \( \A\X = \begin{pmatrix} 3 & -1 \\ 3 & 3 \end{pmatrix} \) and \( \X\B = \begin{pmatrix} -1 & 1 \\ 3 & -1 \end{pmatrix} \), and their difference is \( \C \).
:::

::: {.check}
Let \( \A \in M_3(\nC) \) have eigenvalues \( 1, 2, 2 \) and let \( \B \in M_2(\nC) \) have eigenvalues \( 0, 3 \). List the eigenvalues of \( \cS_{\A,\B} \) with multiplicity, and decide whether \( \A\X - \X\B = \C \) is uniquely solvable for every \( \C \in M_{3 \times 2}(\nC) \).
:::

::: {.solution}
By @lem-kronecker-sum-spectrum the six eigenvalues are the differences \( \lambda_i - \mu_j \):
\[
1 - 0 = 1, \quad 2 - 0 = 2, \quad 2 - 0 = 2, \quad 1 - 3 = -2, \quad 2 - 3 = -1, \quad 2 - 3 = -1 .
\]
None is zero — equivalently \( \spec(\A) = \{1, 2\} \) and \( \spec(\B) = \{0, 3\} \) are disjoint — so by @thm-sylvester-equation the equation has exactly one solution for every \( \C \).
:::

::: {.warning}
**The criterion depends on the sign.** For the equation \( \A\X + \X\B = \C \), which is the form Chapter 7 used in @exm-sylvester-equation-vec, the relevant operator is \( \cS_{\A,-\B} \), and \( \spec(-\B) = \{-\mu_j\} \). So the condition is \( \lambda_i + \mu_j \neq 0 \) for all \( i, j \), **not** \( \spec(\A) \cap \spec(\B) = \varnothing \). The two conditions are genuinely different: with \( \A = \diag(1, 2) \) and \( \B = \begin{pmatrix} -1 & 5 \\ 0 & 3 \end{pmatrix} \) the spectra \( \{1, 2\} \) and \( \{-1, 3\} \) are disjoint, yet \( 1 + (-1) = 0 \), so \( \A\X + \X\B = \C \) is not solvable for every \( \C \). Read the sign off the equation before quoting the criterion.
:::

## Clearing the corner

We can now answer the question the section opened with.

::: {#cor-block-diagonalization}
[Block Diagonalization by a Sylvester Solution]

Let \( \A \in M_m(F) \), \( \B \in M_n(F) \) and \( \C \in M_{m \times n}(F) \), and put
\[
\M = \begin{pmatrix} \A & \C \\ \0 & \B \end{pmatrix} \in M_{m+n}(F).
\]

::: {.enumerate options="label=(\alph*)"}
1. If \( \X \in M_{m \times n}(F) \) satisfies \( \A\X - \X\B = -\C \), then with \( \P = \begin{pmatrix} \I_m & \X \\ \0 & \I_n \end{pmatrix} \) we have \( \P^{-1}\M\P = \A \oplus \B \). In particular \( \M \sim \A \oplus \B \).
2. Conversely, if \( \P^{-1}\M\P = \A \oplus \B \) for some \( \X \in M_{m \times n}(F) \) and the matrix \( \P \) built from it as in (a), then that \( \X \) satisfies \( \A\X - \X\B = -\C \).
3. If \( F = \nC \) and \( \spec(\A) \cap \spec(\B) = \varnothing \), then a solution \( \X \) exists, and it is unique; so \( \M \sim \A \oplus \B \) for **every** corner \( \C \).
:::
:::

::: {.idea}
The matrices \( \begin{pmatrix} \I_m & \X \\ \0 & \I_n \end{pmatrix} \) are exactly the changes of basis that add multiples of the first block of basis vectors to the second and leave the first alone. Conjugating \( \M \) by one of them cannot touch the two diagonal blocks or create anything below the diagonal; all it can do is move the corner, and the block multiplication shows it moves the corner by \( \A\X - \X\B \). So the corner can be driven to \( \0 \) precisely when \( -\C \) lies in the image of the Sylvester operator.
:::

::: {.proof}
(a) First, \( \P \) is invertible with
\[
\P^{-1} = \begin{pmatrix} \I_m & -\X \\ \0 & \I_n \end{pmatrix},
\]
since multiplying the two matrices in either order gives \( \I_{m+n} \) by @thm-block-multiplication, the partitions being conformable. The same theorem gives
\[
\M\P = \begin{pmatrix} \A & \A\X + \C \\ \0 & \B \end{pmatrix},
\]
and then
\[
\P^{-1}\M\P = \begin{pmatrix} \A & \A\X + \C - \X\B \\ \0 & \B \end{pmatrix}.
\]
By hypothesis \( \A\X - \X\B = -\C \), so the corner is \( \0 \) and the result is \( \A \oplus \B \) (@def-block-diagonal).

(b) The computation in (a) used nothing about \( \X \) until the last sentence. So if that \( \P \) satisfies \( \P^{-1}\M\P = \A \oplus \B \), comparing the corners of the two sides gives \( \A\X + \C - \X\B = \0 \), which is the equation.

(c) By @thm-sylvester-equation ((a) \( \Rightarrow \) (c)), the equation \( \A\X - \X\B = -\C \) has exactly one solution. Apply (a).
:::

::: {#exm-block-diagonalize-corner}
[Clearing a Corner]

Block-diagonalize
\[
\M = \begin{pmatrix} 2 & 1 & -4 & 2 \\ 0 & 3 & 0 & -4 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 2 & -1 \end{pmatrix} \in M_4(\nQ) .
\]
:::

::: {.solution}
Partition \( \M \) into \( 2 \times 2 \) blocks. The diagonal blocks are the matrices \( \A \) and \( \B \) of @exm-sylvester-solve-2x2, and the corner is
\[
\begin{pmatrix} -4 & 2 \\ 0 & -4 \end{pmatrix} = -\C
\]
for the \( \C \) of that example. So the equation to solve is \( \A\X - \X\B = -(-\C) = \C \), which is the one already solved there, with the unique solution \( \X = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} \). By @cor-block-diagonalization (a), taking
\[
\P = \begin{pmatrix} 1 & 0 & 1 & -1 \\ 0 & 1 & 1 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}
\]
gives \( \P^{-1}\M\P = \A \oplus \B \), that is,
\[
\P^{-1}\M\P = \begin{pmatrix} 2 & 1 & 0 & 0 \\ 0 & 3 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 2 & -1 \end{pmatrix}.
\]
The eigenvalues \( 2, 3, 1, -1 \) are of course unchanged; what has changed is that the space has been split into two invariant pieces of dimension \( 2 \).
:::

::: {.remark}
Part (b) restricts the shape of \( \P \), and one may ask whether that is a real restriction: if \( \M \) is similar to \( \A \oplus \B \) by *any* invertible matrix, must the Sylvester equation be solvable? The answer is yes over every field. This is **Roth's removal rule**, and the proof is not a block computation: it goes through the characteristic matrix and the criterion \( \A \sim \B \) if and only if \( x\I - \A \approx x\I - \B \) over \( F[x] \) (@thm-similar-iff-xi-minus-a-equivalent). We do not need it here and do not prove it; nothing later in the book depends on it.
:::

**Primary decomposition, seen again.** Put @cor-block-diagonalization next to Schur and a familiar theorem drops out with no extra work. Let \( \A \in M_N(\nC) \) have distinct eigenvalues \( \lambda_1, \dots, \lambda_k \) with algebraic multiplicities \( a_1, \dots, a_k \). By @cor-schur-matrix we may prescribe the order of the diagonal in a Schur factorization, so choose the order that lists all copies of \( \lambda_1 \) first, then all copies of \( \lambda_2 \), and so on. Partitioning the resulting triangular matrix along \( N = a_1 + \dots + a_k \) makes it block upper triangular with diagonal blocks \( \T_1, \dots, \T_k \), where \( \T_i \) is triangular with the single diagonal value \( \lambda_i \), so \( \spec(\T_i) = \{\lambda_i\} \). Now peel the blocks off one at a time: \( \spec(\T_1) \) is disjoint from the spectrum of the rest, so @cor-block-diagonalization (c) splits off \( \T_1 \), and induction on \( k \) finishes. The conclusion is that \( \A \sim \T_1 \oplus \dots \oplus \T_k \) with \( \spec(\T_i) = \{\lambda_i\} \) — the matrix form of the primary decomposition of @thm-primary-decomposition, here obtained from a triangular form and a linear equation rather than from the kernel-splitting lemma.

## Commuting with a matrix of disjoint spectra

Here is the promised use of @thm-sylvester-equation (d). It says that disjoint spectra force a block structure on anything that commutes.

::: {#cor-commutant-block-diagonal}
[Disjoint Spectra Split the Commutant]

Let \( \A_1 \in M_{n_1}(\nC), \dots, \A_r \in M_{n_r}(\nC) \) have **pairwise disjoint** spectra, and put \( \D = \A_1 \oplus \dots \oplus \A_r \in M_N(\nC) \), \( N = n_1 + \dots + n_r \). Let \( \Z \in M_N(\nC) \) satisfy \( \D\Z = \Z\D \), and partition \( \Z \) into blocks \( \Z_{pq} \in M_{n_p \times n_q}(\nC) \) for the partition \( N = n_1 + \dots + n_r \). Then
\[
\Z_{pq} = \0 \quad \text{for all } p \neq q,
\]
so \( \Z = \Z_{11} \oplus \dots \oplus \Z_{rr} \) is block **diagonal**, and each diagonal block satisfies \( \A_p\Z_{pp} = \Z_{pp}\A_p \).
:::

::: {.proof}
By @thm-block-multiplication, the \( (p, q) \) block of \( \D\Z \) is \( \A_p\Z_{pq} \) and the \( (p, q) \) block of \( \Z\D \) is \( \Z_{pq}\A_q \), because \( \D \) has only one non-zero block in each block row and in each block column. So \( \D\Z = \Z\D \) is equivalent to
\[
\A_p\Z_{pq} = \Z_{pq}\A_q \qquad (1 \le p, q \le r).
\]
Let \( p \neq q \). Then \( \spec(\A_p) \cap \spec(\A_q) = \varnothing \) by hypothesis, so @thm-sylvester-equation ((a) \( \Rightarrow \) (d)) forces \( \Z_{pq} = \0 \). The diagonal equations \( \A_p\Z_{pp} = \Z_{pp}\A_p \) are the remaining cases \( p = q \), and they carry no information beyond commuting.
:::

Read the statement twice, because a similar-sounding claim is false.

::: {.warning}
**It is the disjointness of the spectra that does the work, not the block diagonal shape.** Nothing here says that a matrix commuting with a block diagonal matrix is block diagonal, and nothing here says that a commutant consists of triangular matrices. Both fail as soon as two diagonal blocks share an eigenvalue. Chapter 9 §04 computes the commutant of \( \J = \J_2(0) \oplus \J_1(0) \) explicitly and finds it to be
\[
\left\{ \begin{pmatrix} a & b & c \\ 0 & a & 0 \\ 0 & h & i \end{pmatrix} : a, b, c, h, i \in F \right\},
\]
which contains matrices with a non-zero entry **below** the diagonal, in position \( (3, 2) \). That does not contradict @cor-commutant-block-diagonal: the two blocks \( \J_2(0) \) and \( \J_1(0) \) have the same spectrum \( \{0\} \), so the corollary has nothing to say about them. What is true for a single repeated eigenvalue is weaker and needs a different normal form: the commutant of a basic **Weyr** matrix is block upper triangular for the Weyr partition (@prp-weyr-commutant), and the Jordan form has no such property. Note too that even when @cor-commutant-block-diagonal applies, it says nothing about the diagonal blocks \( \Z_{pp} \) themselves, which range over the whole commutant of \( \A_p \).
:::

The corollary is the reason spectral separation is so useful. Combined with the primary decomposition above, it says that over \( \nC \) the commutant of any matrix splits along its distinct eigenvalues: after the change of basis that block-diagonalizes \( \A \) by spectrum, everything commuting with \( \A \) becomes block diagonal too, and the hard part of describing a commutant is always the single-eigenvalue part. The pleasant case of the same phenomenon appeared in @thm-simultaneous-unitary-diagonalization, where the pieces are honest eigenspaces and the splitting is orthogonal.

## Lyapunov's equation

One specialization is important enough to have its own name.

::: {#def-lyapunov-equation}
[Lyapunov equation]

Let \( \A \in M_n(\nC) \) and \( \Q \in M_n(\nC) \). The **Lyapunov equation** for the pair \( (\A, \Q) \) is
\[
\A\X + \X\A^{*} = -\Q ,
\]
with unknown \( \X \in M_n(\nC) \). Call \( \A \) **stable** when every \( \lambda \in \spec(\A) \) has \( \operatorname{Re}\lambda < 0 \).
:::

This is the Sylvester equation with \( \B = -\A^{*} \), since \( \A\X - \X(-\A^{*}) = \A\X + \X\A^{*} \). To apply @thm-sylvester-equation we need \( \spec(-\A^{*}) \).

The eigenvalues of \( \A^{*} \) are the conjugates of those of \( \A \). Indeed \( \det(\M^{*}) = \conj{\det \M} \) for every \( \M \in M_n(\nC) \), because \( \det(\M\tp) = \det \M \) (@thm-det-transpose) and the determinant is a sum of products of entries with coefficients \( \pm 1 \) (@def-determinant), so conjugating every entry conjugates the value. Applying this to \( \M = \lambda\I - \A \), whose conjugate transpose is \( \conj\lambda\I - \A^{*} \), gives \( \det(\conj\lambda\I - \A^{*}) = \conj{\det(\lambda\I - \A)} \). So one determinant vanishes exactly when the other does, and \( \lambda \in \spec(\A) \) if and only if \( \conj\lambda \in \spec(\A^{*}) \) (@thm-eigenvalue-characterizations).

Therefore \( \spec(-\A^{*}) = \{-\conj\lambda : \lambda \in \spec(\A)\} \), and @thm-sylvester-equation says the Lyapunov equation has exactly one solution for every \( \Q \) precisely when
\[
\lambda + \conj\mu \neq 0 \qquad \text{for all } \lambda, \mu \in \spec(\A).
\]
If \( \A \) is stable this holds, because then \( \operatorname{Re}(\lambda + \conj\mu) = \operatorname{Re}\lambda + \operatorname{Re}\mu < 0 \). So a stable matrix gives a uniquely solvable Lyapunov equation, whatever \( \Q \) is.

What makes the equation important is a statement we are not yet equipped to prove. Call a Hermitian matrix \( \X \) **positive definite** when \( \x^{*}\X\x > 0 \) for every non-zero \( \x \in \nC^n \). Then: *if \( \A \) is stable and \( \Q \) is positive definite, the unique solution \( \X \) of \( \A\X + \X\A^{*} = -\Q \) is positive definite; and conversely, if some positive definite \( \X \) solves the equation for some positive definite \( \Q \), then \( \A \) is stable.* Positivity is the subject of Chapter 12, where the tools to handle \( \x^{*}\X\x \) are built, and the consequence for differential equations — that a stable \( \A \) makes every solution of \( \dot{\x} = \A\x \) decay, with \( \x^{*}\X\x \) as the quantity that measures the decay — belongs to Chapter 15. We record the equation here because its *solvability*, which is the part Sylvester's theorem settles, is exactly what makes the rest possible.

## Exercises

### A. Check your understanding

:::: {#exr-sylvester-equation-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the Sylvester operator of a pair \( (\A, \B) \) with \( \A \in M_m(F) \), \( \B \in M_n(F) \), and state the dimension of the space it acts on.
2. Write down the matrix of the Sylvester operator with respect to the vectorization \( \vecop \), and say which Chapter 7 result produces it.
3. State the criterion for \( \A\X - \X\B = \C \) to have exactly one solution for every \( \C \), over \( \nC \).
4. True or false: if \( \A\X - \X\B = \C \) has at least one solution for every \( \C \), then that solution is unique. Justify your answer.
5. True or false: if \( \spec(\A) \cap \spec(\B) = \varnothing \), then \( \A\X + \X\B = \C \) has exactly one solution for every \( \C \). Justify your answer.
:::
::::

::: {.solution}
(a) \( \cS_{\A,\B}(\X) = \A\X - \X\B \) for \( \X \in M_{m \times n}(F) \) (@def-sylvester-operator). It acts on \( M_{m \times n}(F) \), of dimension \( mn \).

(b) \( \K = \I_n \otimes \A - \B\tp \otimes \I_m \), by @eq-sylvester-kronecker; it comes from the vec identity @thm-vec-identity applied twice, with \( \vecop(\A\X) = (\I_n \otimes \A)\vecop\X \) and \( \vecop(\X\B) = (\B\tp \otimes \I_m)\vecop\X \).

(c) Exactly when \( \A \) and \( \B \) have no common eigenvalue, that is \( \spec(\A) \cap \spec(\B) = \varnothing \) (@thm-sylvester-equation).

(d) True. Existence for every \( \C \) says \( \cS_{\A,\B} \) is surjective; an operator on the finite-dimensional space \( M_{m \times n}(F) \) is surjective if and only if it is injective (@thm-invertible-tfae through \( \vecop \), or Rank–Nullity), and injectivity is uniqueness.

(e) False. The criterion for the \( + \) form is \( \lambda + \mu \neq 0 \) for all \( \lambda \in \spec(\A) \), \( \mu \in \spec(\B) \), since \( \A\X + \X\B = \cS_{\A,-\B}(\X) \). With \( \A = \diag(1, 2) \) and \( \B = \diag(-1, 3) \) the spectra are disjoint but \( 1 + (-1) = 0 \), so the equation is not uniquely solvable.
:::

### B. Practice

:::: {#exr-sylvester-equation-b1}
[B1: A Sylvester equation by vectorization]

Over \( \nQ \), let
\[
\A = \begin{pmatrix} 3 & 1 \\ 0 & 1 \end{pmatrix}, \qquad \B = \begin{pmatrix} -1 & 0 \\ 1 & 0 \end{pmatrix}, \qquad \C = \begin{pmatrix} 2 & 1 \\ 0 & -2 \end{pmatrix}.
\]

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \spec(\A) \) and \( \spec(\B) \), and decide whether \( \A\X - \X\B = \C \) has exactly one solution.
2. Write down \( \K = \I_2 \otimes \A - \B\tp \otimes \I_2 \), and check that its diagonal entries are the four differences \( \lambda_i - \mu_j \).
3. Solve the equation.
:::
::::

::: {.solution}
(a) \( \A \) is upper triangular with diagonal \( 3, 1 \), so \( \spec(\A) = \{3, 1\} \) (@thm-diagonal-of-triangular-form). For \( \B \), \( p_{\B} = \det\begin{pmatrix} x+1 & 0 \\ -1 & x \end{pmatrix} = x(x+1) \), so \( \spec(\B) = \{0, -1\} \). The spectra are disjoint, so by @thm-sylvester-equation there is exactly one solution for this (or any) \( \C \).

(b) \( \B\tp = \begin{pmatrix} -1 & 1 \\ 0 & 0 \end{pmatrix} \), so
\[
\I_2 \otimes \A = \begin{pmatrix} 3 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 3 & 1 \\ 0 & 0 & 0 & 1 \end{pmatrix}, \quad \B\tp \otimes \I_2 = \begin{pmatrix} -1 & 0 & 1 & 0 \\ 0 & -1 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix},
\]
and
\[
\K = \begin{pmatrix} 4 & 1 & -1 & 0 \\ 0 & 2 & 0 & -1 \\ 0 & 0 & 3 & 1 \\ 0 & 0 & 0 & 1 \end{pmatrix}.
\]
Its diagonal is \( 4, 2, 3, 1 \), and the differences \( \lambda_i - \mu_j \) are \( 3 - (-1) = 4 \), \( 1 - (-1) = 2 \), \( 3 - 0 = 3 \), \( 1 - 0 = 1 \), as @lem-kronecker-sum-spectrum asserts.

(c) With \( \vecop\X = (x_{11}, x_{21}, x_{12}, x_{22}) \) and \( \vecop\C = (2, 0, 1, -2) \), back substitution gives \( x_{22} = -2 \); then \( 3x_{12} + x_{22} = 1 \), so \( x_{12} = 1 \); then \( 2x_{21} - x_{22} = 0 \), so \( x_{21} = -1 \); then \( 4x_{11} + x_{21} - x_{12} = 2 \), so \( x_{11} = 1 \). Hence
\[
\X = \begin{pmatrix} 1 & 1 \\ -1 & -2 \end{pmatrix}.
\]
*Check:* \( \A\X = \begin{pmatrix} 2 & 1 \\ -1 & -2 \end{pmatrix} \) and \( \X\B = \begin{pmatrix} 0 & 0 \\ -1 & 0 \end{pmatrix} \), and their difference is \( \C \).
:::

:::: {#exr-sylvester-equation-b2}
[B2: Block-diagonalizing a 3 × 3 matrix]

Let
\[
\M = \begin{pmatrix} 2 & 1 & 2 \\ 0 & 2 & 3 \\ 0 & 0 & 5 \end{pmatrix} \in M_3(\nQ) .
\]

::: {.enumerate options="label=(\alph*)"}
1. Partition \( \M \) as \( 3 = 2 + 1 \), name the blocks \( \A \), \( \B \), \( \C \), and explain why @cor-block-diagonalization applies.
2. Solve the corresponding Sylvester equation.
3. Write down \( \P \) and verify that \( \P^{-1}\M\P = \A \oplus \B \).
:::
::::

::: {.solution}
(a) The blocks are \( \A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} \), \( \B = (5) \) and \( \C = \begin{pmatrix} 2 \\ 3 \end{pmatrix} \). Both diagonal blocks are triangular, so \( \spec(\A) = \{2\} \) and \( \spec(\B) = \{5\} \) (@thm-diagonal-of-triangular-form); these are disjoint, so @cor-block-diagonalization (c) applies and a unique \( \X \in M_{2 \times 1}(\nQ) \) exists.

(b) With \( \X = \x = (x_1, x_2) \), the equation \( \A\x - 5\x = -\C \) reads \( (\A - 5\I_2)\x = -\C \), that is
\[
\begin{pmatrix} -3 & 1 \\ 0 & -3 \end{pmatrix}\begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} -2 \\ -3 \end{pmatrix}.
\]
The second row gives \( x_2 = 1 \), and the first then gives \( -3x_1 + 1 = -2 \), so \( x_1 = 1 \). Hence \( \x = (1, 1) \).

(c) Taking
\[
\P = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \P^{-1} = \begin{pmatrix} 1 & 0 & -1 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{pmatrix},
\]
we get \( \M\P = \begin{pmatrix} 2 & 1 & 5 \\ 0 & 2 & 5 \\ 0 & 0 & 5 \end{pmatrix} \) and then
\[
\P^{-1}\M\P = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 5 \end{pmatrix} = \A \oplus \B ,
\]
as @cor-block-diagonalization (a) predicts.
:::

:::: {#exr-sylvester-equation-b3}
[B3: Which equations are uniquely solvable?]

Determine, for each of the following, whether the stated equation has exactly one solution \( \X \in M_2(\nC) \) for **every** right-hand side \( \C \in M_2(\nC) \). Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \A\X - \X\B = \C \) with \( \A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \), \( \B = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix} \).
2. \( \A\X - \X\B = \C \) with \( \A = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} \), \( \B = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \).
3. \( \A\X + \X\B = \C \) with \( \A = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix} \), \( \B = \begin{pmatrix} -1 & 5 \\ 0 & 3 \end{pmatrix} \).
4. \( \A\X - \X\B = \C \) with \( \A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \), \( \B = \begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix} \).
5. \( \A\X - \X\B = \C \) with \( \A \in M_2(\nC) \) nilpotent and \( \B \in M_2(\nC) \) invertible.
:::
::::

::: {.solution}
(a) Yes. \( \spec(\A) = \{1\} \) and \( \spec(\B) = \{2, 3\} \) are disjoint (@thm-diagonal-of-triangular-form), so @thm-sylvester-equation applies.

(b) No. Both characteristic polynomials are \( x^2 + 1 \), so \( \spec(\A) = \spec(\B) = \{i, -i\} \), which is as far from disjoint as possible. A witness is easy to produce here: \( \X = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \) gives \( \A\X = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix} = \X\B \), so \( \X \) is a non-zero member of \( \ker\cS_{\A,\B} \) and condition (d) of @thm-sylvester-equation fails.

(c) No. This is the \( + \) form, so the operator is \( \cS_{\A,-\B} \) and the condition is \( \lambda + \mu \neq 0 \). Here \( \spec(\A) = \{1, 2\} \) and \( \spec(\B) = \{-1, 3\} \), and \( 1 + (-1) = 0 \).

(d) No. Both are triangular with diagonal \( 1, 1 \), so \( \spec(\A) = \spec(\B) = \{1\} \).

(e) Yes. A nilpotent matrix has \( \spec(\A) = \{0\} \), since \( \A^k = \0 \) forces \( \lambda^k = 0 \) for every eigenvalue \( \lambda \); and \( 0 \notin \spec(\B) \) because \( \B \) is invertible (@thm-invertible-tfae-eigen). So the spectra are disjoint.
:::

### C. Going deeper

:::: {#exr-sylvester-equation-c1}
[C1: Eigenvectors of the Sylvester operator]

Let \( \A \in M_m(\nC) \) and \( \B \in M_n(\nC) \), and let \( \cS = \cS_{\A,\B} \).

::: {.enumerate options="label=(\alph*)"}
1. Suppose \( \A\x = \lambda\x \) with \( \x \in \nC^m \) non-zero, and suppose \( \y \in \nC^n \) is a left eigenvector of \( \B \) for \( \mu \), so that \( \y\tp\B = \mu\y\tp \) (@def-left-eigenvector). Prove that \( \x\y\tp \neq \0 \) and that \( \cS(\x\y\tp) = (\lambda - \mu)\,\x\y\tp \).
2. Deduce that every difference \( \lambda - \mu \) with \( \lambda \in \spec(\A) \) and \( \mu \in \spec(\B) \) is an eigenvalue of \( \cS \).
3. Hence give a second proof that \( \cS \) is not invertible when \( \A \) and \( \B \) have a common eigenvalue, one that uses no Kronecker products.
:::
::::

::: {.solution}
(a) Choose \( i \) with \( x_i \neq 0 \) and \( j \) with \( y_j \neq 0 \); these exist because \( \x \) and \( \y \) are non-zero. The \( (i, j) \) entry of \( \x\y\tp \) is \( x_iy_j \neq 0 \), so \( \x\y\tp \neq \0 \). For the eigenvalue equation, associativity of matrix multiplication (@thm-matrix-multiplication-properties) gives
\[
\cS(\x\y\tp) = (\A\x)\y\tp - \x(\y\tp\B) = \lambda\x\y\tp - \mu\x\y\tp,
\]
which is \( (\lambda - \mu)\x\y\tp \).

(b) Let \( \lambda \in \spec(\A) \) and \( \mu \in \spec(\B) \). A right eigenvector \( \x \) for \( \lambda \) exists by @def-eigenvalue, and a left eigenvector \( \y \) for \( \mu \) exists by @prp-left-eigenvectors-transpose (b). By (a), \( \x\y\tp \) is a non-zero matrix with \( \cS(\x\y\tp) = (\lambda - \mu)\x\y\tp \), so \( \lambda - \mu \) is an eigenvalue of \( \cS \) with eigenvector \( \x\y\tp \).

(c) If \( \lambda \in \spec(\A) \cap \spec(\B) \), apply (b) with \( \mu = \lambda \): then \( 0 \) is an eigenvalue of \( \cS \), so \( \ker \cS \neq \{\0\} \) and \( \cS \) is not invertible. This shows one implication of @thm-sylvester-equation directly. (It does not give the converse: knowing every \( \lambda - \mu \) is an eigenvalue does not by itself show there are no others.)
:::

:::: {#exr-sylvester-equation-c2}
[C2: The kernel when the spectra meet]

Let \( \A \in M_m(\nC) \) and \( \B \in M_n(\nC) \) have eigenvalue lists \( \lambda_1, \dots, \lambda_m \) and \( \mu_1, \dots, \mu_n \) with algebraic multiplicity, and let \( d = \#\{(i, j) : \lambda_i = \mu_j\} \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \dim\ker\cS_{\A,\B} \ge 1 \) if and only if \( d \ge 1 \).
2. Prove that \( \dim\ker\cS_{\A,\B} \le d \).
3. Show that the inequality in (b) can be strict, by computing \( \ker\cS_{\A,\B} \) for \( \A = \B = \J_2(0) \).
:::
::::

::: {.solution}
(a) \( d \ge 1 \) says exactly that \( \A \) and \( \B \) have a common eigenvalue, and by @thm-sylvester-equation ((a) \( \Leftrightarrow \) (d)) that is exactly the failure of \( \ker\cS_{\A,\B} = \{\0\} \).

(b) The operator \( \cS_{\A,\B} \) has matrix \( \K \) (@eq-sylvester-kronecker), so \( \dim\ker\cS_{\A,\B} = g_{\K}(0) \), the geometric multiplicity of \( 0 \) as an eigenvalue of \( \K \) (when \( 0 \notin \spec(\K) \) both sides are \( 0 \) and there is nothing to prove). By @lem-kronecker-sum-spectrum the eigenvalue list of \( \K \) consists of the \( mn \) differences \( \lambda_i - \mu_j \), so the algebraic multiplicity is \( a_{\K}(0) = d \). By @thm-geometric-le-algebraic, \( g_{\K}(0) \le a_{\K}(0) = d \).

(c) Here \( m = n = 2 \) and \( \lambda_1 = \lambda_2 = \mu_1 = \mu_2 = 0 \), so \( d = 4 \). The kernel is the commutant of \( \J = \J_2(0) \): writing \( \X = \begin{pmatrix} p & q \\ r & s \end{pmatrix} \),
\[
\J\X = \begin{pmatrix} r & s \\ 0 & 0 \end{pmatrix}, \qquad \X\J = \begin{pmatrix} 0 & p \\ 0 & r \end{pmatrix},
\]
so \( \J\X = \X\J \) forces \( r = 0 \) and \( s = p \), and leaves \( q \) free. Hence \( \ker\cS_{\J,\J} = \Span(\I_2, \J) \), of dimension \( 2 < 4 = d \).
:::

:::: {#exr-sylvester-equation-c3}
[C3: Only the scalars commute with everything]

Let \( F \) be a field, \( n \ge 2 \), and let \( \E_{ij} \in M_n(F) \) be the matrix unit with \( 1 \) in position \( (i, j) \) and \( 0 \) elsewhere.

::: {.enumerate options="label=(\alph*)"}
1. Suppose \( \A \in M_n(F) \) satisfies \( \A\E_{ij} = \E_{ij}\A \) for all \( i \neq j \). Prove that \( \A = c\I_n \) for some \( c \in F \).
2. Deduce that the only matrices commuting with every \( \X \in M_n(F) \) are the scalar matrices, that is, \( \ker\cS_{\A,\A} = M_n(F) \) forces \( \A \) scalar.
3. Deduce that the only matrices commuting with every **invertible** matrix are again the scalar matrices.
:::

*Hint for (c): \( \I_n + \E_{ij} \) is invertible when \( i \neq j \).*
::::

::: {.solution}
(a) Fix \( i \neq j \). By @thm-three-views-of-product, \( \A\E_{ij} \) has column \( j \) equal to \( \A\e_i \), that is column \( i \) of \( \A \), and all other columns zero; while \( \E_{ij}\A \) has row \( i \) equal to row \( j \) of \( \A \), and all other rows zero. Compare entries.

Take \( k \neq i \). The \( (k, j) \) entry of \( \A\E_{ij} \) is \( a_{ki} \), and the \( (k, j) \) entry of \( \E_{ij}\A \) is \( 0 \), because row \( k \neq i \) of \( \E_{ij}\A \) is zero. Hence \( a_{ki} = 0 \) whenever \( k \neq i \). Since \( n \ge 2 \), every index \( i \) has some \( j \neq i \) available, so this holds for every \( i \), and \( \A \) is diagonal.

Now the \( (i, j) \) entry: on the left it is \( a_{ii} \) (the \( i \)-th entry of column \( i \) of \( \A \)), and on the right it is \( a_{jj} \) (the \( j \)-th entry of row \( j \) of \( \A \)). So \( a_{ii} = a_{jj} \) for all \( i \neq j \). Writing \( c \) for this common value, \( \A = c\I_n \).

(b) If \( \A\X = \X\A \) for every \( \X \in M_n(F) \), then in particular for \( \X = \E_{ij} \) with \( i \neq j \), so (a) gives \( \A = c\I_n \). Conversely every scalar matrix commutes with everything. Hence \( \ker\cS_{\A,\A} = M_n(F) \) if and only if \( \A \) is scalar.

(c) For \( i \neq j \) we have \( \E_{ij}^2 = \0 \), so \( (\I_n + \E_{ij})(\I_n - \E_{ij}) = \I_n \) and \( \I_n + \E_{ij} \) is invertible. If \( \A \) commutes with every invertible matrix, it commutes with \( \I_n + \E_{ij} \), hence with \( \E_{ij} \) (subtract \( \A\I_n = \I_n\A \)), for all \( i \neq j \). By (a), \( \A = c\I_n \).
:::
