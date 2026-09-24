# Algebraic and Geometric Multiplicity

An eigenvalue can be counted in two ways. It is a root of the characteristic polynomial, and a root has a multiplicity. It also has an eigenspace, and a subspace has a dimension. The two numbers need not agree, and the gap between them is exactly what can stop an operator from having a diagonal matrix. This section defines both counts, proves that the dimension never exceeds the root multiplicity, and shows that the root multiplicities package the trace and the determinant. The next section turns the comparison into a test for diagonalizability.

## Two ways to count an eigenvalue

Compare two matrices over any field \( F \):
\[
2\I_2 = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}, \qquad \J = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}.
\]
Both are triangular with diagonal \( 2, 2 \), so both have characteristic polynomial \( (x - 2)^2 \) and spectrum \( \{2\} \). By the only measure we have so far, the eigenvalue data agree. Yet the eigenvectors are very different. For \( 2\I_2 \), every non-zero vector is an eigenvector and \( E_2 = F^2 \). For \( \J \), the matrix \( \J - 2\I = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) kills exactly the multiples of \( \e_1 \), so \( E_2(\J) = \Span(\e_1) \) is a line. The root \( 2 \) "counts twice" in both characteristic polynomials, but it supplies two independent eigenvectors for \( 2\I_2 \) and only one for \( \J \). Both numbers deserve names.

*The algebraic multiplicity counts an eigenvalue as a root; the geometric multiplicity counts the independent eigenvectors it supplies.*

::: {#def-algebraic-multiplicity}
[Algebraic Multiplicity]

Let \( V \) be a finite-dimensional vector space over \( F \) with \( \dim V \ge 1 \), let \( T \in \cL(V) \) and \( \lambda \in F \). The **algebraic multiplicity** of \( \lambda \) for \( T \) is
\[
a_T(\lambda) \coloneqq \operatorname{mult}_\lambda(p_T),
\]
the multiplicity of \( \lambda \) as a root of the characteristic polynomial (@def-root-multiplicity). For \( \A \in M_n(F) \), \( a_{\A}(\lambda) \coloneqq \operatorname{mult}_\lambda(p_{\A}) \).
:::

::: {#def-geometric-multiplicity}
[Geometric Multiplicity]

Let \( V \) be a finite-dimensional vector space over \( F \), \( T \in \cL(V) \) and \( \lambda \in F \). The **geometric multiplicity** of \( \lambda \) for \( T \) is
\[
g_T(\lambda) \coloneqq \dim E_\lambda(T) = \dim\ker(T - \lambda\,\id_V).
\]
For \( \A \in M_n(F) \), \( g_{\A}(\lambda) \coloneqq \dim E_\lambda(\A) = n - \rank(\A - \lambda \I_n) \).
:::

When \( T \) or \( \A \) is clear from context we write simply \( a(\lambda) \) and \( g(\lambda) \).

In words: \( a_T(\lambda) \) is the **largest** \( m \) such that \( (x - \lambda)^m \) divides \( p_T \). It is a statement about a polynomial and can be computed by factoring. \( g_T(\lambda) \) is the dimension of the subspace of solutions of \( T\v = \lambda\v \), including \( \0 \). It is the largest number of **linearly independent** eigenvectors for \( \lambda \), not the number of eigenvectors, which is infinite over an infinite field. For matrices the second formula comes from @thm-rank-nullity-matrix applied to \( \A - \lambda \I_n \), and it is the one we compute with: find the rank of \( \A - \lambda \I \) by elimination and subtract from \( n \).

**Well-definedness.** Both numbers are defined for every \( \lambda \in F \), eigenvalue or not. By @thm-eigenvalue-characterizations, \( \lambda \) is an eigenvalue if and only if \( p_T(\lambda) = 0 \), if and only if \( a_T(\lambda) \ge 1 \); and by @def-eigenvalue, if and only if \( E_\lambda(T) \ne \{\0\} \), that is, \( g_T(\lambda) \ge 1 \). So for a scalar that is not an eigenvalue both multiplicities are \( 0 \), and for an eigenvalue both are at least \( 1 \). Neither depends on a basis: \( p_T \) does not (@def-charpoly-operator), and \( E_\lambda(T) \) is defined without one. If \( \sB \) is a basis of \( V \), then \( a_T(\lambda) = a_{\mtx{T}{\sB}{\sB}}(\lambda) \) because \( p_T = p_{\mtx{T}{\sB}{\sB}} \), and \( g_T(\lambda) = g_{\mtx{T}{\sB}{\sB}}(\lambda) \) because the coordinate map is an isomorphism from \( \ker(T - \lambda\,\id_V) \) onto \( \nul(\mtx{T}{\sB}{\sB} - \lambda \I) \) (@thm-rank-map-equals-rank-matrix (a) and @cor-matrix-of-polynomial-of-operator).

**Examples.**

- **The hook.** For \( 2\I_2 \): \( a(2) = 2 \) and \( g(2) = 2 - \rank 0 = 2 \). For \( \J \): \( a(2) = 2 \) and \( g(2) = 2 - \rank\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = 1 \).
- **A \( 1 \times 1 \) matrix.** For \( \A = (c) \), \( p_{\A} = x - c \), so \( a(c) = 1 \), and \( \A - c\I = (0) \) has rank \( 0 \), so \( g(c) = 1 \). This degenerate case already shows the pattern of the theorem below: the two counts can only differ when there is room, a repeated root.
- **Differentiation.** On \( V = \nR[x]_{\le n} \), the matrix of \( D \) in the basis \( (1, x, \dots, x^n) \) is strictly upper triangular, so \( p_D = x^{n+1} \) and \( a_D(0) = n + 1 \). But \( E_0(D) \) is the line of constant polynomials (the examples after @def-eigenspace), so \( g_D(0) = 1 \). The gap can be as large as \( n \).
- **A matrix from Chapter 7.** For \( \A = \begin{pmatrix} 2 & 0 & 1 \\ 1 & 3 & 1 \\ 1 & 0 & 2 \end{pmatrix} \), @exm-charpoly-small found \( p_{\A} = (x - 1)(x - 3)^2 \), so \( a(1) = 1 \) and \( a(3) = 2 \). The matrix \( \A - 3\I = \begin{pmatrix} -1 & 0 & 1 \\ 1 & 0 & 1 \\ 1 & 0 & -1 \end{pmatrix} \) has a zero column, and its first two rows are independent while the third is minus the first, so its rank is \( 2 \) and \( g(3) = 3 - 2 = 1 \). Similarly \( \A - \I = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 2 & 1 \\ 1 & 0 & 1 \end{pmatrix} \) has third row equal to the first and first two rows independent, so its rank is \( 2 \) and \( g(1) = 1 \).

**Minimal change.** Take the triangular matrices
\[
\B = \begin{pmatrix} 2 & 0 & 1 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \B' = \begin{pmatrix} 2 & 1 & 1 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{pmatrix},
\]
which differ in one entry. Both have \( p = (x - 2)^2(x - 1) \), so \( a(2) = 2 \) for both: the algebraic multiplicity does not notice the change. But \( \B - 2\I \) has non-zero rows \( (0, 0, 1) \) and \( (0, 0, -1) \), rank \( 1 \), so \( g_{\B}(2) = 2 \); while \( \B' - 2\I \) has rows \( (0, 1, 1) \) and \( (0, 0, -1) \), rank \( 2 \), so \( g_{\B'}(2) = 1 \). One off-diagonal entry, invisible to \( p \), removed an eigenvector.

**Why these definitions.** The algebraic multiplicity is the natural count for a polynomial: with it, the roots of \( p_T \) add up to \( \deg p_T = \dim V \) whenever \( p_T \) splits (@thm-roots-with-multiplicity), and the trace and determinant come out right (@thm-trace-det-eigenvalues below). The geometric multiplicity is the natural count for eigenvectors: it is the number of basis vectors we can take from \( E_\lambda(T) \) when we try to build a basis of eigenvectors. The names record where each number lives, in algebra (a polynomial) or in geometry (a subspace).

::: {.warning}
**The geometric multiplicity is not read off from \( p_T \).** Two operators with the same characteristic polynomial can have different geometric multiplicities: \( 2\I_2 \) and \( \J \) above, or \( \B \) and \( \B' \). To find \( g(\lambda) \) you must compute \( \rank(\A - \lambda \I) \). Also, \( g(\lambda) \) is **not** "how many eigenvectors" \( \lambda \) has: over \( \nR \), \( E_\lambda \ne \{\0\} \) always contains infinitely many eigenvectors.
:::

::: {.check}
Find \( a(0) \) and \( g(0) \) for \( \N = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} \in M_3(F) \).
:::

::: {.solution}
\( \N \) is triangular with zero diagonal, so \( p_{\N} = x^3 \) and \( a(0) = 3 \). The rank of \( \N - 0\I = \N \) is \( 1 \), so \( g(0) = 3 - 1 = 2 \), with \( E_0(\N) = \Span(\e_1, \e_3) \).
:::

## The geometric multiplicity never exceeds the algebraic

In every example so far, \( g(\lambda) \le a(\lambda) \). That is always the case.

::: {#thm-geometric-le-algebraic}
[Geometric Multiplicity Is at Most Algebraic Multiplicity]

Let \( V \) be a finite-dimensional vector space over \( F \) with \( \dim V = n \ge 1 \), let \( T \in \cL(V) \), and let \( \lambda \in F \) be an eigenvalue of \( T \). Then
\[
1 \le g_T(\lambda) \le a_T(\lambda).
\]
:::

::: {.idea}
Start from the smallest subspace in sight, \( E_\lambda(T) \). Take a basis of it and extend it to a basis of \( V \). In that basis, the first \( g \) columns of the matrix are \( \lambda\e_1, \dots, \lambda\e_g \), so the matrix is block upper triangular with top-left block \( \lambda \I_g \). The block triangular determinant then factors \( (x - \lambda)^g \) out of \( p_T \), and a root with a factor \( (x - \lambda)^g \) has multiplicity at least \( g \). The inequality can be strict because the other block may contribute further factors \( x - \lambda \), as it does for \( \J \).
:::

::: {.proof}
Since \( \lambda \) is an eigenvalue, \( E_\lambda(T) \ne \{\0\} \), so \( g = g_T(\lambda) \ge 1 \). Let \( (\v_1, \dots, \v_g) \) be a basis of \( E_\lambda(T) \). By @thm-basis-extension, it extends to a basis \( \sB = (\v_1, \dots, \v_g, \w_1, \dots, \w_{n-g}) \) of \( V \).

*Case \( g = n \).* Then \( T\v_i = \lambda\v_i \) for every basis vector, so \( \mtx{T}{\sB}{\sB} = \lambda \I_n \) by @def-matrix-of-linear-map, and \( p_T = (x - \lambda)^n \) by the triangular case of @def-characteristic-polynomial. Hence \( a_T(\lambda) = n = g \).

*Case \( g < n \).* For \( i \le g \), \( T\v_i = \lambda\v_i \), so column \( i \) of \( \mtx{T}{\sB}{\sB} \) is \( \lambda\e_i \). Hence
\[
\mtx{T}{\sB}{\sB} = \begin{pmatrix} \lambda \I_g & \B \\ 0 & \D \end{pmatrix}, \qquad x\I_n - \mtx{T}{\sB}{\sB} = \begin{pmatrix} (x - \lambda)\I_g & -\B \\ 0 & x\I_{n-g} - \D \end{pmatrix},
\]
for some \( \B \in M_{g \times (n-g)}(F) \) and \( \D \in M_{n-g}(F) \). The second matrix is block upper triangular over \( F[x] \) with square diagonal blocks. By @thm-det-block-triangular, which holds over the commutative ring \( F[x] \) (the remark after it), and @def-charpoly-operator,
\[
p_T = \det\big((x - \lambda)\I_g\big)\,\det(x\I_{n-g} - \D) = (x - \lambda)^g\,p_{\D} ,
\]
where \( \det((x - \lambda)\I_g) = (x - \lambda)^g \) because the matrix is diagonal. So \( (x - \lambda)^g \mid p_T \). By @def-root-multiplicity, \( a_T(\lambda) \), the **largest** \( m \) with \( (x - \lambda)^m \mid p_T \), satisfies \( a_T(\lambda) \ge g \). This proves the theorem.
:::

The inequality is strict exactly when \( \lambda \) is also a root of \( p_{\D} \), the characteristic polynomial of the "rest" of the operator. For \( \J \), with \( \sB = (\e_1, \e_2) \), the block \( \D \) is \( (2) \), and \( p_{\D} = x - 2 \) contributes the second factor.

A useful consequence: if \( a(\lambda) = 1 \), then \( g(\lambda) = 1 \). A **simple** root of \( p_T \) always has a one-dimensional eigenspace, and so the only eigenvalues whose eigenspaces need checking are the repeated ones.

Both multiplicities are properties of the operator, not of the basis, so they cannot distinguish similar matrices. That makes them tools for proving that two matrices are **not** similar.

::: {#prp-multiplicities-similarity-invariant}
[Similar Matrices Have the Same Multiplicities]

Let \( \A, \B \in M_n(F) \) with \( \A \sim \B \), and let \( \lambda \in F \). Then \( a_{\A}(\lambda) = a_{\B}(\lambda) \) and \( g_{\A}(\lambda) = g_{\B}(\lambda) \).
:::

::: {.proof}
Let \( \B = \P^{-1}\A \P \). By @thm-charpoly-similarity-invariant, \( p_{\A} = p_{\B} \), so the algebraic multiplicities agree. Also \( \B - \lambda \I = \P^{-1}\A \P - \lambda \P^{-1}\P = \P^{-1}(\A - \lambda \I)\P \), so \( \B - \lambda \I \sim \A - \lambda \I \), and these have the same rank by @prp-similarity-invariants (a). Hence \( g_{\B}(\lambda) = n - \rank(\B - \lambda \I) = n - \rank(\A - \lambda \I) = g_{\A}(\lambda) \).
:::

For example, \( 2\I_2 \) and \( \J \) have the same characteristic polynomial but \( g(2) = 2 \) versus \( g(2) = 1 \), so they are not similar. The same test shows \( \B \not\sim \B' \) in the minimal change above.

::: {.warning}
**A repeated eigenvalue does not force a shortage of eigenvectors, and equal eigenvalues do not force similarity.** The identity \( \I_2 \) has the repeated eigenvalue \( 1 \), yet \( g(1) = a(1) = 2 \) and its matrix is as simple as possible. In the other direction, \( \I_2 \) and \( \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) have the same eigenvalues with the same algebraic multiplicities, and they are not similar. Even agreement of **both** multiplicities for every eigenvalue does not force similarity; @exr-multiplicities-c2 gives two \( 4 \times 4 \) matrices showing this.
:::

## Multiplicities, trace and determinant

By @thm-roots-with-multiplicity, the algebraic multiplicities of the eigenvalues of \( T \) add up to at most \( \deg p_T = \dim V \), with equality exactly when \( p_T \) splits over \( F \). Over \( \nC \) this always happens (@cor-complex-polynomial-splits). When it does, \( p_T \) is determined by the eigenvalues and their algebraic multiplicities,
\[
p_T = (x - \lambda_1)^{a(\lambda_1)} \cdots (x - \lambda_k)^{a(\lambda_k)},
\]
and two of its coefficients are familiar: by @thm-charpoly-coefficients, the coefficient of \( x^{n-1} \) is \( -\tr T \) and the constant term is \( (-1)^n\det T \). Comparing the two descriptions expresses trace and determinant through eigenvalues.

::: {#thm-trace-det-eigenvalues}
[Trace and Determinant from Eigenvalues]

Let \( V \) be a finite-dimensional vector space over \( F \) with \( \dim V = n \ge 1 \), and let \( T \in \cL(V) \). Suppose \( p_T \) splits over \( F \), and let \( \lambda_1, \dots, \lambda_k \) be the distinct eigenvalues of \( T \). Then
\[
a(\lambda_1) + \dots + a(\lambda_k) = n, \qquad \tr T = \sum_{i=1}^{k} a(\lambda_i)\,\lambda_i, \qquad \det T = \prod_{i=1}^{k} \lambda_i^{\,a(\lambda_i)} .
\]
In words: listing each eigenvalue as often as its algebraic multiplicity, the trace is the sum of the list and the determinant is its product. In particular this holds for every operator on a non-zero finite-dimensional complex space, and for every \( \A \in M_n(\nC) \).
:::

::: {.idea}
Rather than expanding a product of linear factors by hand, notice that the product is itself a characteristic polynomial: that of the diagonal matrix with the eigenvalues on its diagonal. Chapter 7 already knows the \( x^{n-1} \) coefficient and the constant term of any characteristic polynomial, so we read them off twice and compare.
:::

::: {.proof}
Since \( p_T \) splits and is monic of degree \( n \) (@thm-charpoly-coefficients), @def-polynomial-splits gives \( p_T = (x - c_1)\cdots(x - c_n) \) for some \( c_1, \dots, c_n \in F \). For \( c, \lambda \in F \), the polynomial \( x - c \) has \( \operatorname{mult}_\lambda(x - c) = 1 \) if \( c = \lambda \) and \( 0 \) otherwise, since \( \lambda \) is a root of \( x - c \) only when \( c = \lambda \) (@thm-remainder-theorem). So by @thm-multiplicity-of-product, \( \operatorname{mult}_\lambda(p_T) = \sum_j \operatorname{mult}_\lambda(x - c_j) \) is the number of indices \( j \) with \( c_j = \lambda \). In particular the values occurring among \( c_1, \dots, c_n \) are exactly the roots of \( p_T \) in \( F \), which are \( \lambda_1, \dots, \lambda_k \) by @thm-eigenvalue-characterizations, and \( \lambda_i \) occurs exactly \( a(\lambda_i) \) times. Counting the \( n \) factors gives \( \sum_i a(\lambda_i) = n \), and
\[
c_1 + \dots + c_n = \sum_i a(\lambda_i)\lambda_i, \qquad c_1\cdots c_n = \prod_i \lambda_i^{\,a(\lambda_i)} .
\]
Let \( \C = \diag(c_1, \dots, c_n) \). It is triangular, so \( p_{\C} = (x - c_1)\cdots(x - c_n) = p_T \) (the examples after @def-characteristic-polynomial). Apply @thm-charpoly-coefficients to both \( \C \) and \( T \): the coefficient of \( x^{n-1} \) in this one polynomial is \( -\tr \C = -(c_1 + \dots + c_n) \) and also \( -\tr T \); the constant term is \( (-1)^n\det \C = (-1)^n c_1\cdots c_n \) (@thm-det-triangular) and also \( (-1)^n\det T \). Hence \( \tr T = c_1 + \dots + c_n \) and \( \det T = c_1\cdots c_n \), which are the displayed formulas. The complex case follows from @cor-complex-polynomial-splits.
:::

**Examples.**

- For \( \A = \begin{pmatrix} 2 & 0 & 1 \\ 1 & 3 & 1 \\ 1 & 0 & 2 \end{pmatrix} \), with \( a(1) = 1 \) and \( a(3) = 2 \): \( \tr \A = 2 + 3 + 2 = 7 = 1 + 3 + 3 \), and \( \det \A = 9 = 1 \cdot 3 \cdot 3 \).
- For the real matrix \( \begin{pmatrix} 3 & -2 \\ 4 & -1 \end{pmatrix} \) of @exm-complex-eigenvalues-real-matrix, \( p \) does not split over \( \nR \), but it splits over \( \nC \) with roots \( 1 \pm 2i \). The theorem over \( \nC \) gives \( (1 + 2i) + (1 - 2i) = 2 = \tr \A \) and \( (1 + 2i)(1 - 2i) = 1 + 4 = 5 = \det \A \). The trace and determinant are real, while the eigenvalues are not.
- For a \( 2 \times 2 \) matrix whose characteristic polynomial splits, the theorem says the eigenvalues \( \lambda, \mu \) (listed with multiplicity) satisfy \( \lambda + \mu = \tr \A \) and \( \lambda\mu = \det \A \). This is a quick way to guess eigenvalues: for \( \begin{pmatrix} 1 & 2 \\ 3 & 2 \end{pmatrix} \), we want two numbers with sum \( 3 \) and product \( -4 \), namely \( 4 \) and \( -1 \).

**Without splitting, the theorem says nothing.** If \( p_T \) does not split, the eigenvalues in \( F \), counted with algebraic multiplicity, do not account for all of \( p_T \), and summing or multiplying them gives no information. For \( \A = \begin{pmatrix} 3 & -2 \\ 4 & -1 \end{pmatrix} \) over \( \nR \) there are no eigenvalues: the multiplicities add up to \( 0 \ne 2 \), the empty sum \( 0 \) is not \( \tr \A = 2 \), and the empty product \( 1 \) is not \( \det \A = 5 \). For the real rotation \( \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \), with trace \( 0 \) and determinant \( 1 \), the empty sum and product happen to give the right values, but only by coincidence. For real matrices the remedy is to pass to \( \nC \), where \( p_{\A} \) always splits, as in the second example above.

## Exercises

### A. Check your understanding

:::: {#exr-multiplicities-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the algebraic and the geometric multiplicity of \( \lambda \in F \) for \( \A \in M_n(F) \).
2. State the inequality between them for an eigenvalue \( \lambda \), and name the tool its proof uses.
3. True or false: if \( a(\lambda) = 1 \), then \( g(\lambda) = 1 \). Justify your answer.
4. True or false: for every \( \A \in M_n(\nC) \), the geometric multiplicities of the eigenvalues add up to \( n \). Justify your answer.
5. True or false: if \( \A, \B \in M_n(F) \) have the same characteristic polynomial, then \( g_{\A}(\lambda) = g_{\B}(\lambda) \) for every \( \lambda \). Justify your answer.
6. For \( \A \in M_3(\nC) \) with eigenvalues \( 2 \) (algebraic multiplicity \( 2 \)) and \( -1 \), what are \( \tr \A \) and \( \det \A \)?
:::
::::

::: {.solution}
(a) \( a_{\A}(\lambda) = \operatorname{mult}_\lambda(p_{\A}) \), the largest \( m \) with \( (x - \lambda)^m \mid p_{\A} \); \( g_{\A}(\lambda) = \dim E_\lambda(\A) = n - \rank(\A - \lambda \I) \) (@def-algebraic-multiplicity, @def-geometric-multiplicity).

(b) \( 1 \le g(\lambda) \le a(\lambda) \) (@thm-geometric-le-algebraic). The proof extends a basis of \( E_\lambda \) to a basis of the space and uses the block triangular determinant (@thm-det-block-triangular) over \( F[x] \).

(c) True. An eigenvalue has \( g(\lambda) \ge 1 \), and \( g(\lambda) \le a(\lambda) = 1 \).

(d) False. For \( \J = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} \), the only eigenvalue is \( 2 \), with \( g(2) = 1 \ne 2 \). (The **algebraic** multiplicities do add up to \( n \) over \( \nC \).)

(e) False. \( 2\I_2 \) and \( \J \) both have \( p = (x - 2)^2 \), but \( g(2) = 2 \) and \( g(2) = 1 \).

(f) By @thm-trace-det-eigenvalues, listing eigenvalues with algebraic multiplicity as \( 2, 2, -1 \): \( \tr \A = 3 \) and \( \det \A = -4 \).
:::

### B. Practice

:::: {#exr-multiplicities-b1}
[B1: Computing multiplicities]

For each real matrix, find every eigenvalue together with its algebraic and geometric multiplicity.

::: {.enumerate options="label=(\alph*)"}
1. \( \A_1 = \begin{pmatrix} 4 & -1 \\ 1 & 2 \end{pmatrix} \).
2. \( \A_2 = \begin{pmatrix} 2 & 1 & 1 \\ 0 & 1 & -1 \\ -1 & -1 & 1 \end{pmatrix} \).
3. \( \A_3 = \begin{pmatrix} 2 & 1 & 1 \\ -1 & 0 & -1 \\ 1 & 1 & 2 \end{pmatrix} \), given that \( p_{\A_3} = p_{\A_2} \).
4. The matrix of the operator \( S(q)(x) = q(x + 1) \) on \( \nR[x]_{\le 2} \), in the basis \( (1, x, x^2) \).
:::
::::

::: {.solution}
(a) \( \tr \A_1 = 6 \), \( \det \A_1 = 8 + 1 = 9 \), so \( p = x^2 - 6x + 9 = (x - 3)^2 \): the only eigenvalue is \( 3 \), with \( a(3) = 2 \). \( \A_1 - 3\I = \begin{pmatrix} 1 & -1 \\ 1 & -1 \end{pmatrix} \) has rank \( 1 \), so \( g(3) = 1 \).

(b) Expand \( \det(x\I - \A_2) \) along the first column:
\[
\det\begin{pmatrix} x - 2 & -1 & -1 \\ 0 & x - 1 & 1 \\ 1 & 1 & x - 1 \end{pmatrix} = (x - 2)\big[(x - 1)^2 - 1\big] + 1 \cdot \det\begin{pmatrix} -1 & -1 \\ x - 1 & 1 \end{pmatrix}.
\]
The first bracket is \( x^2 - 2x = x(x - 2) \) and the last determinant is \( -1 + (x - 1) = x - 2 \), so \( p_{\A_2} = (x - 2)(x^2 - 2x + 1) = (x - 1)^2(x - 2) \). Thus \( a(1) = 2 \) and \( a(2) = 1 \). By @thm-geometric-le-algebraic, \( g(2) = 1 \). For \( \lambda = 1 \),
\[
\A_2 - \I = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 0 & -1 \\ -1 & -1 & 0 \end{pmatrix}.
\]
Row \( 3 \) is \( -(\text{row } 1) - (\text{row } 2) \), and rows \( 1 \) and \( 2 \) are independent, so the rank is \( 2 \) and \( g(1) = 1 \).

(c) Here \( a(1) = 2 \) and \( a(2) = 1 \), as for \( \A_2 \), so \( g(2) = 1 \). Now
\[
\A_3 - \I = \begin{pmatrix} 1 & 1 & 1 \\ -1 & -1 & -1 \\ 1 & 1 & 1 \end{pmatrix}
\]
has all rows multiples of \( (1, 1, 1) \), so its rank is \( 1 \) and \( g(1) = 2 \). By @prp-multiplicities-similarity-invariant, \( \A_2 \) and \( \A_3 \) are not similar, although they have the same characteristic polynomial.

(d) \( S(1) = 1 \), \( S(x) = 1 + x \), \( S(x^2) = 1 + 2x + x^2 \), so the matrix is \( \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix} \) (as in @exm-charpoly-operators). It is triangular, so \( p = (x - 1)^3 \) and \( a(1) = 3 \). The matrix minus \( \I \) is \( \begin{pmatrix} 0 & 1 & 1 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix} \), of rank \( 2 \), so \( g(1) = 1 \): the only polynomials with \( q(x + 1) = q(x) \) in \( \nR[x]_{\le 2} \) are the constants.
:::

:::: {#exr-multiplicities-b2}
[B2: A parameter that merges eigenvalues]

For \( t \in \nR \), let \( \A_t = \begin{pmatrix} t & 1 \\ -1 & 3 \end{pmatrix} \). Find all \( t \) for which \( \A_t \) has a real eigenvalue \( \lambda \) with \( g(\lambda) < a(\lambda) \).
::::

::: {.solution}
\( \tr \A_t = t + 3 \) and \( \det \A_t = 3t + 1 \), so \( p(x) = x^2 - (t + 3)x + (3t + 1) \). For a \( 2 \times 2 \) matrix, \( g(\lambda) < a(\lambda) \) is possible only if \( a(\lambda) = 2 \), because \( a(\lambda) = 1 \) forces \( g(\lambda) = 1 \) (@thm-geometric-le-algebraic). So \( p \) must have a repeated real root, which happens exactly when its discriminant vanishes:
\[
(t + 3)^2 - 4(3t + 1) = t^2 - 6t + 5 = (t - 1)(t - 5) = 0 .
\]
If \( t = 1 \), then \( p = x^2 - 4x + 4 = (x - 2)^2 \) and \( \A_1 - 2\I = \begin{pmatrix} -1 & 1 \\ -1 & 1 \end{pmatrix} \), of rank \( 1 \), so \( g(2) = 1 < 2 = a(2) \). If \( t = 5 \), then \( p = (x - 4)^2 \) and \( \A_5 - 4\I = \begin{pmatrix} 1 & 1 \\ -1 & -1 \end{pmatrix} \), of rank \( 1 \), so \( g(4) = 1 < 2 \). Hence the answer is \( t \in \{1, 5\} \). (In both cases \( g = a \) was impossible anyway: \( g(\lambda) = 2 \) would mean \( \A_t - \lambda \I = 0 \), but the off-diagonal entries of \( \A_t \) are non-zero.)
:::

:::: {#exr-multiplicities-b3}
[B3: Eigenvalues from trace and determinant]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \A \in M_3(\nR) \) have the eigenvalue \( 1 + i \) (as a complex matrix) and \( \det \A = 6 \). Find all eigenvalues of \( \A \) over \( \nC \), and \( \tr \A \).
2. Let \( \B \in M_2(\nR) \) with \( \tr \B = 6 \) and \( \det \B = 9 \). Show that \( \spec(\B) = \{3\} \) with \( a(3) = 2 \). Give one such \( \B \) with \( g(3) = 2 \) and one with \( g(3) = 1 \).
:::
::::

::: {.solution}
(a) By @thm-real-matrix-complex-eigenvalues, \( 1 - i \) is also an eigenvalue. By @cor-complex-polynomial-splits, \( p_{\A} \) splits over \( \nC \) into three linear factors, and two of them are \( x - (1 + i) \) and \( x - (1 - i) \); let \( \mu \) be the third root. By @thm-trace-det-eigenvalues, \( 6 = \det \A = (1 + i)(1 - i)\mu = 2\mu \), so \( \mu = 3 \). Hence the eigenvalues are \( 1 + i, 1 - i, 3 \), and \( \tr \A = (1 + i) + (1 - i) + 3 = 5 \).

(b) By @thm-charpoly-coefficients, \( p_{\B} = x^2 - 6x + 9 = (x - 3)^2 \). So \( \spec(\B) = \{3\} \) and \( a(3) = 2 \). For \( \B = 3\I_2 \), \( g(3) = 2 \). For \( \B = \begin{pmatrix} 4 & -1 \\ 1 & 2 \end{pmatrix} \) of @exr-multiplicities-b1 (a), \( \tr \B = 6 \), \( \det \B = 9 \) and \( g(3) = 1 \).
:::

### C. Going deeper

:::: {#exr-multiplicities-c1}
[C1: Nilpotent matrices]

Let \( \A \in M_n(\nC) \), \( n \ge 1 \), be nilpotent (\( \A^k = 0 \) for some \( k \ge 1 \)).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( a(0) = n \) and \( g(0) = n - \rank \A \).
2. Deduce that \( g(0) = a(0) \) if and only if \( \A = 0 \).
3. For \( \N = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix} \), check that \( \N^4 = 0 \) and compute \( g(0) \). How large can \( a(0) - g(0) \) be for a nilpotent \( n \times n \) matrix?
:::
::::

::: {.solution}
(a) By @exr-eigenvalues-and-eigenvectors-c2 (b), \( p_{\A} = x^n \), so \( a(0) = \operatorname{mult}_0(x^n) = n \). By @def-geometric-multiplicity, \( g(0) = n - \rank(\A - 0\I) = n - \rank \A \).

(b) By (a), \( g(0) = a(0) \) if and only if \( n - \rank \A = n \), that is, \( \rank \A = 0 \), that is, \( \A = 0 \) (a matrix of rank \( 0 \) has no non-zero column).

(c) \( \N\e_1 = \0 \) and \( \N\e_j = \e_{j-1} \) for \( j \ge 2 \). So \( \N^j\e_i = \0 \) once \( j \ge i \), and \( \N^4\e_i = \0 \) for \( i \le 4 \); hence \( \N^4 = 0 \). The columns of \( \N \) are \( \0, \e_1, \e_2, \e_3 \), so \( \rank \N = 3 \) and \( g(0) = 1 \), while \( a(0) = 4 \). In general, a nilpotent \( \A \) has \( 0 \in \spec(\A) \) (@exr-eigenvalues-and-eigenvectors-c2 (a)), so \( g(0) \ge 1 \) and \( a(0) - g(0) \le n - 1 \); the \( n \times n \) analogue of \( \N \), with ones just above the diagonal, has rank \( n - 1 \) and attains \( a(0) - g(0) = n - 1 \).
:::

:::: {#exr-multiplicities-c2}
[C2: Multiplicities do not determine similarity]

Let
\[
\M_1 = \begin{pmatrix} 1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 1 \end{pmatrix}, \qquad \M_2 = \begin{pmatrix} 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} \in M_4(\nR).
\]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \M_1 \) and \( \M_2 \) have the same eigenvalues with the same algebraic **and** geometric multiplicities.
2. Compute \( \rank(\M_1 - \I)^2 \) and \( \rank(\M_2 - \I)^2 \). Deduce that \( \M_1 \not\sim \M_2 \).
3. Construct a matrix \( \M \in M_4(\nR) \) with \( \spec(\M) = \{2, 5\} \), \( a(2) = 3 \), \( g(2) = 1 \), and \( a(5) = g(5) = 1 \).
:::

*Hint: for (b), if \( \B = \P^{-1}\A \P \), relate \( (\B - \I)^2 \) to \( (\A - \I)^2 \).*
::::

::: {.solution}
(a) Both matrices are upper triangular with diagonal \( 1, 1, 1, 1 \), so both have \( p = (x - 1)^4 \), spectrum \( \{1\} \) and \( a(1) = 4 \). The matrix \( \M_1 - \I \) has columns \( \0, \e_1, \0, \e_3 \), of rank \( 2 \); \( \M_2 - \I \) has columns \( \0, \e_1, \e_2, \0 \), also of rank \( 2 \). So \( g(1) = 4 - 2 = 2 \) for both.

(b) Let \( \N_1 = \M_1 - \I \), so \( \N_1\e_2 = \e_1 \), \( \N_1\e_4 = \e_3 \) and \( \N_1\e_1 = \N_1\e_3 = \0 \). Then \( \N_1^2 \) kills every \( \e_j \), so \( \N_1^2 = 0 \) and \( \rank \N_1^2 = 0 \). Let \( \N_2 = \M_2 - \I \), so \( \N_2\e_2 = \e_1 \), \( \N_2\e_3 = \e_2 \), and \( \N_2\e_1 = \N_2\e_4 = \0 \). Then \( \N_2^2\e_3 = \e_1 \ne \0 \) and \( \N_2^2 \) kills \( \e_1, \e_2, \e_4 \), so \( \N_2^2 = \E_{13} \) has rank \( 1 \).

Suppose \( \M_2 = \P^{-1}\M_1\P \). With \( p(x) = (x - 1)^2 \), @prp-similarity-invariants (c) gives \( (\M_2 - \I)^2 = \P^{-1}(\M_1 - \I)^2\P \), and then (a) of the same proposition gives equal ranks, \( 1 = 0 \). This contradiction shows \( \M_1 \not\sim \M_2 \). So eigenvalues together with both multiplicities do not determine a matrix up to similarity; Chapter 10 finds invariants that do.

(c) Take
\[
\M = \begin{pmatrix} 2 & 1 & 0 & 0 \\ 0 & 2 & 1 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 5 \end{pmatrix}.
\]
It is triangular, so \( p_{\M} = (x - 2)^3(x - 5) \), \( a(2) = 3 \) and \( a(5) = 1 \), hence \( g(5) = 1 \) by @thm-geometric-le-algebraic. The matrix \( \M - 2\I \) has columns \( \0, \e_1, \e_2, 3\e_4 \), which has rank \( 3 \), so \( g(2) = 4 - 3 = 1 \).
:::
