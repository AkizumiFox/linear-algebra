# Spectral Mapping, Products in Both Orders, Left Eigenvectors

Once the eigenvalues of \( T \) are known, what can we say about the eigenvalues of \( T^2 \), of \( T^2 - 3T + I \), or of any polynomial in \( T \)? And when two matrices are multiplied in the two possible orders, how are the eigenvalues of \( AB \) and \( BA \) related? This section answers both questions using the triangular forms of Section 7 and the block matrices of Chapter 7. Along the way it settles two debts: Chapter 6 showed \( p_{AB} = p_{BA} \) only when \( A \) is invertible, and Chapter 7 proved that vanishing traces of all powers force a matrix to be nilpotent by a long computation, with no explanation of why. We end with left eigenvectors, the eigenvectors of the transpose, which pair with ordinary eigenvectors in a useful way and prepare the Markov chains of Section 11.

## Eigenvalues of a polynomial in \( T \)

One half of the answer needs no theory. If \( T\v = \lambda\v \) with \( \v \ne \0 \), then \( T^k\v = \lambda^k\v \) for every \( k \), and so \( q(T)\v = q(\lambda)\v \) for every \( q \in F[x] \) (@exr-eigenvalues-and-eigenvectors-b3). So **\( q \) maps eigenvalues of \( T \) to eigenvalues of \( q(T) \)**, over every field and in every dimension.

The other half, that **every** eigenvalue of \( q(T) \) arises this way, can fail. Part (c) of @exr-eigenvalues-and-eigenvectors-b3 already met the rotation \( R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \) on \( \nR^2 \): it has no real eigenvalue, while \( R^2 = -I \) has the eigenvalue \( -1 \). The eigenvalues of \( R \) that would map to \( -1 \), namely \( \pm i \), are missing from \( \nR \). So we expect the full statement to need a characteristic polynomial that splits. With that hypothesis we even get the multiplicities, because a triangular form shows all the eigenvalues at once on its diagonal.

*The eigenvalues of \( q(T) \) are the values of \( q \) at the eigenvalues of \( T \), counted with multiplicity.*

::: {#thm-spectral-mapping}
[Spectral Mapping Theorem]

Let \( V \) be a finite-dimensional vector space over \( F \) with \( \dim V = n \ge 1 \), and let \( T \in \cL(V) \). Suppose \( p_T \) splits over \( F \), say
\[
p_T(x) = (x - \lambda_1)(x - \lambda_2)\cdots(x - \lambda_n),
\]
where each eigenvalue appears as often as its algebraic multiplicity. Then for every \( q \in F[x] \),
\[
p_{q(T)}(x) = \big(x - q(\lambda_1)\big)\big(x - q(\lambda_2)\big)\cdots\big(x - q(\lambda_n)\big),
\]
and consequently
\[
\spec\big(q(T)\big) = q\big(\spec(T)\big) = \{ q(\lambda) : \lambda \in \spec(T) \} .
\]
In particular this holds for every operator on a non-zero finite-dimensional complex space, and for every \( A \in M_n(\nC) \).
:::

::: {.idea}
Choose a basis in which \( T \) is upper triangular (Section 7). Its diagonal is \( \lambda_1, \dots, \lambda_n \). Products and sums of upper triangular matrices are upper triangular, and their diagonals are computed position by position, so \( q([T]) \) is upper triangular with diagonal \( q(\lambda_1), \dots, q(\lambda_n) \). The characteristic polynomial of a triangular matrix is read off its diagonal.
:::

::: {.proof}
By @thm-triangularization there is a basis \( \sB \) of \( V \) such that \( U = [T]_{\sB} \) is upper triangular. By @thm-diagonal-of-triangular-form, its diagonal entries are \( \lambda_1, \dots, \lambda_n \) in some order; renumbering the \( \lambda_i \), we may assume \( u_{ii} = \lambda_i \).

::: {.claim}
If \( X, Y \in M_n(F) \) are upper triangular, then so are \( X + Y \), \( cX \) for \( c \in F \), and \( XY \), with diagonal entries \( x_{ii} + y_{ii} \), \( cx_{ii} \) and \( x_{ii}y_{ii} \).

::: {.proof}
The statements for \( X + Y \) and \( cX \) are entrywise. For the product, \( (XY)_{ij} = \sum_{k=1}^{n} x_{ik}y_{kj} \) (@def-matrix-multiplication). If \( i > j \), every \( k \) has \( k < i \) or \( k \ge i > j \), so \( x_{ik} = 0 \) or \( y_{kj} = 0 \), and the sum is \( 0 \). If \( i = j \), the only term that can be non-zero has \( k \ge i \) and \( k \le i \), so \( (XY)_{ii} = x_{ii}y_{ii} \).
:::
:::

By the claim and induction on \( k \), \( U^k \) is upper triangular with diagonal entries \( \lambda_1^k, \dots, \lambda_n^k \) (for \( k = 0 \), \( U^0 = I \)). Writing \( q = \sum_k a_kx^k \), the claim again shows that \( q(U) = \sum_k a_kU^k \) is upper triangular with diagonal entries \( \sum_k a_k\lambda_i^k = q(\lambda_i) \). By @cor-matrix-of-polynomial-of-operator, \( [q(T)]_{\sB} = q(U) \), so by @def-charpoly-operator and the examples after @def-characteristic-polynomial,
\[
p_{q(T)} = p_{q(U)} = \prod_{i=1}^{n} \big(x - q(\lambda_i)\big).
\]
For the spectra: by @thm-eigenvalue-characterizations, \( \mu \in F \) is an eigenvalue of \( q(T) \) if and only if \( p_{q(T)}(\mu) = \prod_i (\mu - q(\lambda_i)) = 0 \), that is, if and only if \( \mu = q(\lambda_i) \) for some \( i \), since a product of non-zero field elements is non-zero. The \( \lambda_i \) are exactly the eigenvalues of \( T \), each listed at least once (@thm-eigenvalue-characterizations). Hence \( \spec(q(T)) = \{ q(\lambda) : \lambda \in \spec(T) \} \). Over \( \nC \), \( p_T \) always splits by @cor-complex-polynomial-splits.
:::

The formula for \( p_{q(T)} \) carries more than the spectrum. The algebraic multiplicity of \( \mu \) as an eigenvalue of \( q(T) \) is the number of indices \( i \) with \( q(\lambda_i) = \mu \) (@lem-multiplicity-cofactor), so several eigenvalues of \( T \) can merge into one eigenvalue of \( q(T) \), and their multiplicities add. Combined with @thm-trace-det-eigenvalues, applied to \( q(T) \), whose characteristic polynomial splits by the theorem, we get the most used consequence.

::: {#cor-trace-det-of-polynomial}
[Trace and Determinant of a Polynomial in \( T \)]

Under the hypotheses of @thm-spectral-mapping, for every \( q \in F[x] \),
\[
\tr q(T) = q(\lambda_1) + \dots + q(\lambda_n), \qquad \det q(T) = q(\lambda_1)\cdots q(\lambda_n).
\]
In particular \( \tr T^k = \lambda_1^k + \dots + \lambda_n^k \) for every \( k \in \nN \).
:::

::: {.proof}
By @thm-spectral-mapping, \( p_{q(T)} = \prod_i (x - q(\lambda_i)) \) splits. Group equal values: if \( \mu_1, \dots, \mu_s \) are the distinct values among the \( q(\lambda_i) \), then \( \mu_j \) occurs exactly \( a_{q(T)}(\mu_j) \) times in the list (@lem-multiplicity-cofactor). By @thm-trace-det-eigenvalues applied to \( q(T) \), \( \tr q(T) = \sum_j a_{q(T)}(\mu_j)\,\mu_j = \sum_i q(\lambda_i) \) and \( \det q(T) = \prod_j \mu_j^{\,a_{q(T)}(\mu_j)} = \prod_i q(\lambda_i) \). Take \( q = x^k \) for the last statement.
:::

::: {#exm-spectral-mapping-3x3}
[A Polynomial in a Non-Diagonalizable Matrix]

Let \( A = \begin{pmatrix} 1 & 1 & 1 \\ 2 & 0 & 1 \\ -3 & 3 & 2 \end{pmatrix} \in M_3(\nR) \), for which @exr-diagonalization-b1 found \( p_A = (x + 1)(x - 2)^2 \) and showed that \( A \) is not diagonalizable. Without computing any eigenvectors, find \( p_{A^2} \), \( \tr A^2 \) and \( \det A^2 \). Then find \( p_{q(A)} \) for \( q = x^2 - x - 2 \), and decide whether \( q(A) = 0 \).
:::

::: {.solution}
*The square.* \( p_A \) splits over \( \nR \) with the list \( \lambda_1 = -1 \), \( \lambda_2 = \lambda_3 = 2 \). By @thm-spectral-mapping with \( q = x^2 \), the list for \( A^2 \) is \( 1, 4, 4 \), so
\[
p_{A^2} = (x - 1)(x - 4)^2, \qquad \tr A^2 = 1 + 4 + 4 = 9, \qquad \det A^2 = 1 \cdot 4 \cdot 4 = 16
\]
by @cor-trace-det-of-polynomial. *Check.* Multiplying out,
\[
A^2 = \begin{pmatrix} 0 & 4 & 4 \\ -1 & 5 & 4 \\ -3 & 3 & 4 \end{pmatrix},
\]
whose trace is \( 0 + 5 + 4 = 9 \); and \( \det A = (-1)\cdot 2 \cdot 2 = -4 \) by @thm-trace-det-eigenvalues, so \( \det A^2 = (\det A)^2 = 16 \) by @thm-det-multiplicative.

*The polynomial \( q \).* Here \( q = (x - 2)(x + 1) \), so \( q(-1) = 0 \) and \( q(2) = 0 \). The list for \( q(A) \) is \( 0, 0, 0 \), and \( p_{q(A)} = x^3 \): the only eigenvalue of \( q(A) \) is \( 0 \). Yet \( q(A) \ne 0 \). Indeed
\[
q(A) = A^2 - A - 2I = \begin{pmatrix} -3 & 3 & 3 \\ -3 & 3 & 3 \\ 0 & 0 & 0 \end{pmatrix},
\]
and one checks \( q(A)^2 = 0 \). The spectral mapping theorem sees only eigenvalues, and a non-zero matrix can have \( 0 \) as its only eigenvalue. That \( q(A) \ne 0 \) here is no accident: if \( q(A) = 0 \), the minimal polynomial of \( A \) would divide (@thm-minimal-polynomial-divides) \( (x - 2)(x + 1) \), which has distinct roots, and \( A \) would be diagonalizable by @thm-diagonalizable-iff-minimal-distinct-linear.
:::

::: {.warning}
**Without splitting, spectral mapping fails.** For the real rotation \( R \) above, \( \spec(R) = \varnothing \) in \( \nR \), so \( q(\spec(R)) = \varnothing \) for \( q = x^2 \), while \( \spec(R^2) = \spec(-I) = \{-1\} \). Over \( \nC \) the theorem is restored: \( \spec(R) = \{i, -i\} \), both square to \( -1 \), and \( p_{R^2} = (x + 1)^2 \). Also, the theorem is about eigenvalues and algebraic multiplicities only: \( T = \diag(1, -1) \) has two one-dimensional eigenspaces, while \( T^2 = I \) has the single eigenspace \( \nR^2 \).
:::

::: {.check}
Let \( A \in M_2(\nC) \) have eigenvalues \( i \) and \( -i \). Find \( p_{A^2} \) and \( \det(A^2 + I) \).
:::

::: {.solution}
The list for \( A \) is \( i, -i \) (two distinct roots of the degree-\( 2 \) polynomial \( p_A \)). By @thm-spectral-mapping with \( q = x^2 \), the list for \( A^2 \) is \( -1, -1 \), so \( p_{A^2} = (x + 1)^2 \). With \( q = x^2 + 1 \), @cor-trace-det-of-polynomial gives \( \det(A^2 + I) = q(i)\,q(-i) = 0 \cdot 0 = 0 \).
:::

## Traces of powers detect nilpotency

Chapter 7 proved, in @exr-commutators-and-shoda-c2, that a matrix \( C \) over a field of characteristic \( 0 \) with \( \tr C^k = 0 \) for every \( k \ge 1 \) is nilpotent, by a careful argument with annihilating polynomials that gave no reason for the result. Here is the view through eigenvalues, for complex matrices. The traces of the powers are the **power sums** \( \lambda_1^k + \dots + \lambda_n^k \) of the eigenvalues (@cor-trace-det-of-polynomial), and a nilpotent matrix is one whose eigenvalues are all \( 0 \). So the question becomes: if all power sums of \( n \) complex numbers vanish, must the numbers vanish? A Vandermonde determinant says yes.

::: {#thm-nilpotent-trace-powers}
[Nilpotent Matrices via Eigenvalues and Traces]

Let \( n \ge 1 \) and \( A \in M_n(\nC) \). The following are equivalent:

::: {.enumerate options="label=(\alph*)"}
1. \( A \) is nilpotent, that is, \( A^s = 0 \) for some \( s \ge 1 \);
2. \( \spec(A) = \{0\} \);
3. \( p_A = x^n \);
4. \( A^n = 0 \);
5. \( \tr A^k = 0 \) for \( k = 1, 2, \dots, n \).
:::

The same holds for \( A \in M_n(F) \) when \( F \) is a subfield of \( \nC \), such as \( \nQ \) or \( \nR \), with \( \spec(A) \) in (b) taken over \( \nC \).
:::

::: {.idea}
**Plan:** (a) ⇒ (b) ⇒ (c) ⇒ (d) ⇒ (a), and (c) ⇒ (e) ⇒ (b). All but one arrow are short. For (e) ⇒ (b), suppose some eigenvalue is non-zero. Group the non-zero eigenvalues into distinct values \( \mu_1, \dots, \mu_r \) with multiplicities \( m_1, \dots, m_r \ge 1 \). The vanishing traces say \( \sum_j m_j\mu_j^k = 0 \) for \( k = 1, \dots, r \): a square linear system for the vector \( (m_1, \dots, m_r) \), whose matrix is a Vandermonde matrix times the invertible \( \diag(\mu_j) \). So the \( m_j \) would be \( 0 \), but they are positive integers, and positive integers are non-zero in \( \nC \).
:::

::: {.proof}
(a) ⇒ (b). This is @exr-eigenvalues-and-eigenvectors-c2 (a), applied to \( T_A \) on \( \nC^n \ne \{\0\} \).

(b) ⇒ (c). By @cor-complex-polynomial-splits, \( p_A = (x - z_1)\cdots(x - z_n) \) with \( z_i \in \nC \). Each \( z_i \) is an eigenvalue (@thm-eigenvalue-characterizations), hence \( 0 \), so \( p_A = x^n \).

(c) ⇒ (d). By @cor-complex-triangularizable, \( A = PUP^{-1} \) with \( P \) invertible and \( U \) upper triangular, and by @thm-diagonal-of-triangular-form the diagonal entries of \( U \) are the roots of \( p_A = x^n \), all \( 0 \). Then \( U\e_1 = \0 \) and \( U\e_j \in \Span(\e_1, \dots, \e_{j-1}) \) for \( j \ge 2 \), since column \( j \) of \( U \) has zeros from row \( j \) down. By induction on \( j \), \( U^j\e_j = \0 \), hence \( U^n\e_j = U^{n-j}U^j\e_j = \0 \) for every \( j \), and \( U^n = 0 \). By @prp-similarity-invariants (c), \( A^n = PU^nP^{-1} = 0 \).

(d) ⇒ (a). Take \( s = n \).

(c) ⇒ (e). The list of eigenvalues of \( A \) with multiplicity is \( 0, \dots, 0 \), so by @cor-trace-det-of-polynomial, \( \tr A^k = 0^k + \dots + 0^k = 0 \) for every \( k \ge 1 \).

(e) ⇒ (b). By @cor-complex-polynomial-splits, \( p_A \) splits; let \( \lambda_1, \dots, \lambda_n \) be the list of its roots with multiplicity. Since \( n \ge 1 \), \( \spec(A) \) is non-empty, so it suffices to show that every \( \lambda_i = 0 \). Suppose not, let \( \mu_1, \dots, \mu_r \) (\( 1 \le r \le n \)) be the distinct non-zero values among the \( \lambda_i \), and let \( m_j \ge 1 \) be the number of indices \( i \) with \( \lambda_i = \mu_j \). For \( 1 \le k \le r \), the zero eigenvalues contribute \( 0^k = 0 \), so by @cor-trace-det-of-polynomial and (e),
\[
\sum_{j=1}^{r} m_j\,\mu_j^{\,k} = \tr A^k = 0 .
\]
In matrix form, \( W\m = \0 \), where \( \m = (m_1, \dots, m_r) \in \nC^r \) and \( W \in M_r(\nC) \) has \( (k, j) \)-entry \( \mu_j^{\,k} = \mu_j^{\,k-1}\mu_j \). Hence \( W = V(\mu_1, \dots, \mu_r)\tp\,\diag(\mu_1, \dots, \mu_r) \), where \( V(\mu_1, \dots, \mu_r) \) is the Vandermonde matrix with \( (j, k) \)-entry \( \mu_j^{\,k-1} \) (@thm-vandermonde-determinant). The \( \mu_j \) are distinct, so \( V \) is invertible (@cor-vandermonde-nonzero), and so is \( V\tp \), with inverse \( (V^{-1})\tp \) (@thm-transpose-properties). The \( \mu_j \) are non-zero, so \( \diag(\mu_1, \dots, \mu_r) \) is invertible. Therefore \( W \) is invertible, and \( \m = W^{-1}\0 = \0 \). But \( m_1 \) is a positive integer, and \( m_1 \ne 0 \) in \( \nC \). This contradiction shows that every \( \lambda_i = 0 \), so \( \spec(A) = \{0\} \).

For a subfield \( F \subseteq \nC \), regard \( A \) as a complex matrix. Its powers, their traces, its characteristic polynomial and the condition \( A^s = 0 \) are computed by the same arithmetic in \( F \) and in \( \nC \), so (a), (c), (d) and (e) mean the same thing over \( F \) and over \( \nC \), and the equivalences carry over.
:::

In the setting of @exr-commutators-and-shoda-c2, where \( C = [A, B] \) commutes with \( A \), part (a) of that exercise gives \( \tr C^k = 0 \) for all \( k \ge 1 \), and for complex matrices the theorem now shows at once that \( C^n = 0 \). That exercise remains the route for a general field of characteristic \( 0 \).

::: {.warning}
**The characteristic matters.** Over \( \nF_p \), the identity \( I_p \in M_p(\nF_p) \) has \( \tr I_p^{\,k} = p \cdot 1 = 0 \) for every \( k \), yet \( I_p^{\,k} = I_p \ne 0 \). The proof above breaks exactly where it used that the positive integer \( m_1 \) is non-zero in the field: here the multiplicity \( m_1 = p \) of the eigenvalue \( 1 \) is \( 0 \) in \( \nF_p \).
:::

## \( AB \) and \( BA \)

Chapter 6, in @exr-characteristic-polynomial-b3, showed that \( p_{AB} = p_{BA} \) for square \( A \) and \( B \) **when \( A \) is invertible**, because then \( BA = A^{-1}(AB)A \) is similar to \( AB \). Without invertibility the two products need not be similar, and for rectangular \( A \) and \( B \) they do not even have the same size: if \( A \) is \( m \times n \) and \( B \) is \( n \times m \), then \( AB \) is \( m \times m \) and \( BA \) is \( n \times n \). Their characteristic polynomials have degrees \( m \) and \( n \). Multiplying by powers of \( x \) repairs the degrees, and the identity then holds in general.

::: {#thm-ab-ba-eigenvalues}
[\( AB \) and \( BA \) Have the Same Non-zero Eigenvalues]

Let \( m, n \ge 1 \), \( A \in M_{m \times n}(F) \) and \( B \in M_{n \times m}(F) \). Then
\[
x^n\,p_{AB}(x) = x^m\,p_{BA}(x).
\]
Consequently:

::: {.enumerate options="label=(\alph*)"}
1. for every \( \lambda \ne 0 \) in \( F \), \( a_{AB}(\lambda) = a_{BA}(\lambda) \); in particular \( AB \) and \( BA \) have the same non-zero eigenvalues;
2. if \( m = n \), then \( p_{AB} = p_{BA} \); and if \( m \ge n \), then \( p_{AB} = x^{m-n}\,p_{BA} \).
:::
:::

::: {.idea}
We want one big matrix that "contains" \( AB \) and another that "contains" \( BA \), and that are similar to each other. Put them in \( (m + n) \times (m + n) \) block form:
\[
M = \begin{pmatrix} AB & 0 \\ B & 0 \end{pmatrix}, \qquad N = \begin{pmatrix} 0 & 0 \\ B & BA \end{pmatrix}.
\]
Both are block triangular, so their characteristic polynomials are \( p_{AB} \cdot x^n \) and \( x^m \cdot p_{BA} \). The invertible block matrix \( S = \begin{pmatrix} I_m & A \\ 0 & I_n \end{pmatrix} \) turns one into the other: \( MS \) and \( SN \) are both \( \begin{pmatrix} AB & ABA \\ B & BA \end{pmatrix} \).
:::

::: {.proof}
Let \( M, N, S \in M_{m+n}(F) \) be the block matrices displayed in the Idea, partitioned by \( m, n \) in rows and columns. By @thm-block-multiplication,
\[
MS = \begin{pmatrix} AB\cdot I_m + 0 & AB\cdot A + 0 \\ B\cdot I_m + 0 & B\cdot A + 0 \end{pmatrix} = \begin{pmatrix} AB & ABA \\ B & BA \end{pmatrix}, \qquad
SN = \begin{pmatrix} 0 + AB & 0 + A\cdot BA \\ 0 + B & 0 + BA \end{pmatrix} = \begin{pmatrix} AB & ABA \\ B & BA \end{pmatrix},
\]
using associativity (@thm-matrix-multiplication-properties). So \( MS = SN \). The matrix \( S \) is invertible: by @thm-block-multiplication, \( \begin{pmatrix} I_m & A \\ 0 & I_n \end{pmatrix}\begin{pmatrix} I_m & -A \\ 0 & I_n \end{pmatrix} = \begin{pmatrix} I_m & -A + A \\ 0 & I_n \end{pmatrix} = I_{m+n} \), and @thm-one-sided-inverse applies. Hence \( S^{-1}MS = N \), and \( p_M = p_N \) by @thm-charpoly-similarity-invariant.

Now compute both sides. The matrix \( xI_{m+n} - M = \begin{pmatrix} xI_m - AB & 0 \\ -B & xI_n \end{pmatrix} \) is lower block triangular with square diagonal blocks, so by @thm-det-block-triangular, which holds over the commutative ring \( F[x] \) (the remarks before @exm-charpoly-small), and by @thm-det-triangular for \( xI_n \),
\[
p_M(x) = \det(xI_m - AB)\,\det(xI_n) = p_{AB}(x)\,x^n .
\]
Likewise \( xI_{m+n} - N = \begin{pmatrix} xI_m & 0 \\ -B & xI_n - BA \end{pmatrix} \) gives \( p_N(x) = x^m\,p_{BA}(x) \). Since \( p_M = p_N \), this proves \( x^np_{AB} = x^mp_{BA} \).

(a) Let \( \lambda \ne 0 \). Then \( \lambda \) is not a root of \( x^n \), so \( \operatorname{mult}_\lambda(x^n) = 0 \), and similarly for \( x^m \). By @thm-multiplicity-of-product,
\[
a_{AB}(\lambda) = \operatorname{mult}_\lambda(x^np_{AB}) = \operatorname{mult}_\lambda(x^mp_{BA}) = a_{BA}(\lambda).
\]
A scalar is an eigenvalue exactly when its algebraic multiplicity is positive (@thm-eigenvalue-characterizations, @def-root-multiplicity), so the non-zero eigenvalues agree.

(b) If \( m \ge n \), then \( x^np_{AB} = x^n\big(x^{m-n}p_{BA}\big) \), and canceling the non-zero polynomial \( x^n \) (@cor-polynomial-no-zero-divisors) gives \( p_{AB} = x^{m-n}p_{BA} \). For \( m = n \) this is \( p_{AB} = p_{BA} \).
:::

This pays off the promise of @exr-characteristic-polynomial-b3: \( p_{AB} = p_{BA} \) for **all** square \( A \) and \( B \), invertible or not. Comparing coefficients (@thm-charpoly-coefficients) recovers \( \tr(AB) = \tr(BA) \) and \( \det(AB) = \det(BA) \) once more.

The eigenvectors travel between the two products as well, and by hand. If \( AB\w = \lambda\w \) with \( \lambda \ne 0 \), then
\[
BA(B\w) = B(AB\w) = \lambda\,B\w ,
\]
and \( B\w \ne \0 \), since \( A(B\w) = \lambda\w \ne \0 \). So \( B\w \) is an eigenvector of \( BA \) for the same \( \lambda \): multiplying an eigenvector of \( AB \) by \( B \) produces one of \( BA \). For \( \lambda = 0 \) the recipe can fail, because \( B\w \) may be \( \0 \) — which is the warning below in another guise.

**A rank-one example.** Let \( \u, \v \in F^n \) with \( n \ge 2 \). Take \( A = \u \in M_{n \times 1}(F) \) and \( B = \v\tp \in M_{1 \times n}(F) \). Then \( AB = \u\v\tp \) is \( n \times n \), and \( BA = \v\tp\u \) is the \( 1 \times 1 \) matrix whose entry is the number \( c = \v\tp\u \), so \( p_{BA} = x - c \). Applying the theorem with its \( m \) equal to our \( n \), and its \( n \) equal to \( 1 \), gives \( x\,p_{\u\v\tp} = x^n(x - c) \), and canceling \( x \),
\[
p_{\u\v\tp}(x) = x^{n-1}\,(x - \v\tp\u).
\]
For instance, the all-ones matrix \( \1\1\tp \in M_n(\nR) \), with \( \1 = (1, \dots, 1) \), has \( p = x^{n-1}(x - n) \): eigenvalue \( 0 \) with multiplicity \( n - 1 \), and eigenvalue \( n \). Evaluating at \( -1 \) recovers @thm-matrix-determinant-lemma: \( \det(I + \u\v\tp) = (-1)^n\det(-I - \u\v\tp) = (-1)^n\,p_{\u\v\tp}(-1) = (-1)^n(-1)^{n-1}(-1 - \v\tp\u) = 1 + \v\tp\u \).

::: {.warning}
**The zero eigenvalue behaves differently, and \( AB \) need not be similar to \( BA \).** Take \( A = E_{12} \) and \( B = E_{11} \) in \( M_2(F) \). Then \( AB = E_{12}E_{11} = 0 \) and \( BA = E_{11}E_{12} = E_{12} \). Both have \( p = x^2 \), as the theorem demands. But \( g_{AB}(0) = 2 \) while \( g_{BA}(0) = 1 \), and \( AB = 0 \) is similar only to \( 0 \), so \( AB \not\sim BA \). For rectangular matrices even the algebraic multiplicities of \( 0 \) differ, by \( |m - n| \).
:::

::: {.check}
Let \( A \in M_{2 \times 5}(\nR) \) and \( B \in M_{5 \times 2}(\nR) \) with \( p_{AB} = x^2 - 3x + 2 \). What is \( p_{BA} \), and what are \( \tr(BA) \) and \( \det(BA) \)?
:::

::: {.solution}
By @thm-ab-ba-eigenvalues with \( m = 2 \), \( n = 5 \), \( x^5p_{AB} = x^2p_{BA} \), so \( p_{BA} = x^3(x^2 - 3x + 2) = x^5 - 3x^4 + 2x^3 \). By @thm-charpoly-coefficients, \( \tr(BA) = 3 \) (equal to \( \tr(AB) \)), and \( \det(BA) = (-1)^5 \cdot 0 = 0 \), as it must be, since \( BA \) has rank at most \( 2 < 5 \).
:::

## Left eigenvectors

An eigenvector multiplies \( A \) from the right: \( A\v = \lambda\v \). Row vectors can multiply from the left, and in applications, especially Markov chains, the row version is often the one with a meaning.

*A left eigenvector is a row that \( A \) only stretches when it acts from the right of the row.*

::: {#def-left-eigenvector}
[Left Eigenvector]

Let \( A \in M_n(F) \) and \( \lambda \in F \). A **left eigenvector** of \( A \) for \( \lambda \) is a **non-zero** \( \y \in F^n \) with
\[
\y\tp A = \lambda\,\y\tp .
\]
To distinguish them, the eigenvectors of @def-eigenvalue are also called **right eigenvectors**.
:::

In words: \( \y\tp \) is a \( 1 \times n \) row, \( \y\tp A \) is again a row, and we ask that it be a multiple of \( \y\tp \). For example, \( A = \begin{pmatrix} 1 & 2 \\ 3 & 2 \end{pmatrix} \) and \( \y = (1, 1) \) give \( \y\tp A = \begin{pmatrix} 4 & 4 \end{pmatrix} = 4\y\tp \), so \( (1, 1) \) is a left eigenvector for \( 4 \), whereas the right eigenvectors for \( 4 \) are the multiples of \( (2, 3) \) (@exm-eigenvalues-2x2). For a diagonal matrix, \( \e_i \) is both a left and a right eigenvector for the \( i \)-th diagonal entry. And \( \y = \0 \) always satisfies the equation, which is why it is excluded, exactly as for right eigenvectors.

**Non-example by minimal change.** For the same \( A \), change \( \y = (1, 1) \) to \( \y = (1, -1) \). Then \( \y\tp A = \begin{pmatrix} 1 - 3 & 2 - 2 \end{pmatrix} = \begin{pmatrix} -2 & 0 \end{pmatrix} \), which is not a multiple of \( \begin{pmatrix} 1 & -1 \end{pmatrix} \): the row is non-zero, but the defining equation \( \y\tp A = \lambda\y\tp \) has no solution \( \lambda \). Note that \( (1, -1) \) **is** a right eigenvector of \( A \), for \( -1 \); the two notions do not agree.

Transposing turns the definition into one we know.

::: {#prp-left-eigenvectors-transpose}
[Left Eigenvectors Are Eigenvectors of the Transpose]

Let \( A \in M_n(F) \) and \( \lambda \in F \).

::: {.enumerate options="label=(\alph*)"}
1. \( \y \) is a left eigenvector of \( A \) for \( \lambda \) if and only if \( \y \) is an eigenvector of \( A\tp \) for \( \lambda \).
2. \( A \) has a left eigenvector for \( \lambda \) if and only if \( \lambda \in \spec(A) \). Moreover \( p_{A\tp} = p_A \), and \( a_{A\tp}(\lambda) = a_A(\lambda) \), \( g_{A\tp}(\lambda) = g_A(\lambda) \).
:::
:::

::: {.proof}
(a) By @thm-transpose-properties, \( (\y\tp A)\tp = A\tp\y \) and \( (\lambda\y\tp)\tp = \lambda\y \). Since transposing twice gives back the original, \( \y\tp A = \lambda\y\tp \) if and only if \( A\tp\y = \lambda\y \).

(b) By @exr-characteristic-polynomial-b2, \( p_{A\tp} = p_A \), so \( a_{A\tp}(\lambda) = a_A(\lambda) \), and \( \spec(A\tp) = \spec(A) \) by @thm-eigenvalue-characterizations. With (a), \( A \) has a left eigenvector for \( \lambda \) if and only if \( \lambda \in \spec(A\tp) = \spec(A) \). Finally, \( A\tp - \lambda I = (A - \lambda I)\tp \), which has the same rank as \( A - \lambda I \) (@thm-row-rank-equals-column-rank), so by @thm-rank-nullity-matrix, \( g_{A\tp}(\lambda) = n - \rank(A - \lambda I)\tp = n - \rank(A - \lambda I) = g_A(\lambda) \).
:::

::: {.remark}
For an operator \( T \) on \( V \), left eigenvectors correspond to eigenvectors of the dual map \( T' \) on \( V^{*} \) (Chapter 4), whose matrix in the dual bases is the transpose (@thm-matrix-of-dual-map): an eigenvector of \( T' \) is a functional \( \varphi \ne 0 \) with \( \varphi \circ T = \lambda\varphi \).
:::

Left and right eigenvectors for the **same** eigenvalue are usually unrelated, as \( (1, 1) \) and \( (2, 3) \) show. For **different** eigenvalues, though, they are always orthogonal in the sense of the plain product \( \y\tp\v \).

::: {#thm-left-right-biorthogonal}
[Left and Right Eigenvectors Are Biorthogonal]

Let \( A \in M_n(F) \), let \( \y \) be a left eigenvector of \( A \) for \( \mu \), and let \( \v \) be a right eigenvector of \( A \) for \( \lambda \). If \( \lambda \ne \mu \), then \( \y\tp\v = 0 \).
:::

::: {.proof}
Compute the \( 1 \times 1 \) matrix \( \y\tp A\v \) in two ways, using associativity (@thm-matrix-multiplication-properties):
\[
\mu\,\y\tp\v = (\y\tp A)\v = \y\tp A\v = \y\tp(A\v) = \lambda\,\y\tp\v .
\]
Hence \( (\lambda - \mu)\,\y\tp\v = 0 \). Since \( \lambda - \mu \ne 0 \), this forces \( \y\tp\v = 0 \) (@thm-field-basic-properties).
:::

For the example, \( (1, 1) \) is a left eigenvector for \( 4 \) and \( (1, -1) \) a right eigenvector for \( -1 \), and indeed \( 1 - 1 = 0 \).

For a diagonalizable matrix the left eigenvectors come for free with the diagonalization, and they give a formula for all powers that we use in Section 11.

::: {#prp-left-right-eigen-expansion}
[Expansion in Left and Right Eigenvectors]

Let \( A = PDP^{-1} \) with \( P \in M_n(F) \) invertible and \( D = \diag(\lambda_1, \dots, \lambda_n) \). Let \( \v_1, \dots, \v_n \) be the columns of \( P \), and let \( \y_1\tp, \dots, \y_n\tp \) be the rows of \( P^{-1} \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \v_i \) is a right eigenvector and \( \y_i \) a left eigenvector of \( A \) for \( \lambda_i \);
2. \( \y_i\tp\v_j = 1 \) if \( i = j \) and \( 0 \) if \( i \ne j \);
3. for every \( q \in F[x] \),
\[
q(A) = \sum_{i=1}^{n} q(\lambda_i)\,\v_i\y_i\tp, \qquad\text{in particular}\qquad A^k = \sum_{i=1}^{n} \lambda_i^{\,k}\,\v_i\y_i\tp \quad (k \in \nN).
\]
:::
:::

::: {.proof}
(a) From \( AP = PD \), column \( i \) reads \( A\v_i = \lambda_i\v_i \) (Section 4), and \( \v_i \ne \0 \) because \( P \) is invertible. From \( P^{-1}A = DP^{-1} \), row \( i \) reads \( \y_i\tp A = \lambda_i\y_i\tp \) (@thm-three-views-of-product), and \( \y_i \ne \0 \) because \( P^{-1} \) is invertible.

(b) The \( (i, j) \)-entry of \( P^{-1}P = I \) is row \( i \) of \( P^{-1} \) times column \( j \) of \( P \), that is, \( \y_i\tp\v_j \).

(c) By @thm-powers-diagonalizable, \( q(A) = P\,q(D)\,P^{-1} \). The columns of \( P\,q(D) \) are \( q(\lambda_i)\v_i \), and the rows of \( P^{-1} \) are \( \y_i\tp \), so @cor-outer-product-expansion gives \( q(A) = \sum_i q(\lambda_i)\v_i\y_i\tp \). Take \( q = x^k \).
:::

Part (b) is biorthogonality with a normalization: \( \y_i\tp\v_i = 1 \). Part (c) splits \( A \) into rank-one pieces \( \v_i\y_i\tp \), one per eigenvalue, and each piece is simply multiplied by \( \lambda_i^k \) when \( A \) is raised to the power \( k \). In the running example, \( P = \begin{pmatrix} 2 & 1 \\ 3 & -1 \end{pmatrix} \) and \( D = \diag(4, -1) \) give \( P^{-1} = \frac15\begin{pmatrix} 1 & 1 \\ 3 & -2 \end{pmatrix} \), so \( \y_1 = \frac15(1, 1) \) and \( \y_2 = \frac15(3, -2) \), and
\[
A^k = \frac{4^k}{5}\begin{pmatrix} 2 & 2 \\ 3 & 3 \end{pmatrix} + \frac{(-1)^k}{5}\begin{pmatrix} 3 & -2 \\ -3 & 2 \end{pmatrix}.
\]
For \( k = 1 \) this is \( \frac15\begin{pmatrix} 8 - 3 & 8 + 2 \\ 12 + 3 & 12 - 2 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 3 & 2 \end{pmatrix} \), as it should be.

## Exercises

### A. Check your understanding

:::: {#exr-spectral-mapping-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the Spectral Mapping Theorem, including its hypothesis on \( p_T \).
2. True or false: for every \( A \in M_n(\nR) \), every real eigenvalue of \( A^2 \) is the square of a real eigenvalue of \( A \). Justify your answer.
3. True or false: if \( A \in M_{2 \times 3}(F) \) and \( B \in M_{3 \times 2}(F) \), then \( p_{AB} = p_{BA} \). Justify your answer.
4. True or false: for all \( A, B \in M_n(F) \), \( AB \) is similar to \( BA \). Justify your answer.
5. Define a left eigenvector of \( A \in M_n(F) \), and say how left eigenvectors of \( A \) are related to \( A\tp \).
6. True or false: a matrix \( A \in M_3(\nC) \) with \( \tr A = \tr A^2 = \tr A^3 = 0 \) satisfies \( A^3 = 0 \). Justify your answer.
:::
::::

::: {.solution}
(a) If \( V \) is finite-dimensional with \( \dim V = n \ge 1 \), \( T \in \cL(V) \), and \( p_T = \prod_{i=1}^{n}(x - \lambda_i) \) splits over \( F \), then for every \( q \in F[x] \), \( p_{q(T)} = \prod_i (x - q(\lambda_i)) \) and \( \spec(q(T)) = q(\spec(T)) \) (@thm-spectral-mapping).

(b) False. The rotation \( R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \) has no real eigenvalue, while \( R^2 = -I \) has the real eigenvalue \( -1 \).

(c) False. They have different degrees, \( 2 \) and \( 3 \). The correct identity is \( x^3p_{AB} = x^2p_{BA} \), that is, \( p_{BA} = x\,p_{AB} \) (@thm-ab-ba-eigenvalues).

(d) False. \( A = E_{12} \), \( B = E_{11} \) give \( AB = 0 \) and \( BA = E_{12} \ne 0 \), and the only matrix similar to \( 0 \) is \( 0 \).

(e) A non-zero \( \y \in F^n \) with \( \y\tp A = \lambda\y\tp \) for some \( \lambda \in F \). Equivalently, \( \y \) is an eigenvector of \( A\tp \) for \( \lambda \) (@prp-left-eigenvectors-transpose).

(f) True. By @thm-nilpotent-trace-powers with \( n = 3 \), (e) ⇒ (d).
:::

### B. Practice

:::: {#exr-spectral-mapping-b1}
[B1: Eigenvalues of a polynomial in \( A \)]

Let \( A \in M_3(\nC) \) have \( p_A = (x - 1)^2(x + 2) \).

::: {.enumerate options="label=(\alph*)"}
1. Find \( p_{A^2 + A + I} \), \( \tr(A^2 + A + I) \) and \( \det(A^2 + A + I) \). Is \( A^2 + A + I \) invertible?
2. Find \( p_{A^2 + A - 2I} \). Hence show that \( A^2 + A - 2I \) is nilpotent.
3. Find \( \tr A^{5} \) and \( \det(A^{-1}) \).
:::
::::

::: {.solution}
The list of eigenvalues of \( A \) with multiplicity is \( 1, 1, -2 \), since \( p_A \) splits.

(a) With \( q = x^2 + x + 1 \), \( q(1) = 3 \) and \( q(-2) = 4 - 2 + 1 = 3 \). By @thm-spectral-mapping, \( p_{q(A)} = (x - 3)^3 \), and by @cor-trace-det-of-polynomial, \( \tr q(A) = 9 \) and \( \det q(A) = 27 \ne 0 \). So \( A^2 + A + I \) is invertible (@thm-invertible-tfae-det).

(b) With \( r = x^2 + x - 2 = (x - 1)(x + 2) \), \( r(1) = r(-2) = 0 \), so \( p_{r(A)} = x^3 \) by @thm-spectral-mapping. By @thm-nilpotent-trace-powers ((c) ⇒ (d)), \( r(A)^3 = 0 \), so \( A^2 + A - 2I \) is nilpotent.

(c) By @cor-trace-det-of-polynomial, \( \tr A^5 = 1 + 1 + (-2)^5 = -30 \). Also \( \det A = 1 \cdot 1 \cdot (-2) = -2 \ne 0 \) (@thm-trace-det-eigenvalues), so \( A \) is invertible and \( \det(A^{-1}) = (\det A)^{-1} = -\frac12 \) (@cor-det-inverse).
:::

:::: {#exr-spectral-mapping-b2}
[B2: \( AB \) and \( BA \) for a \( 2 \times 3 \) example]

Let \( A = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 2 & 0 \end{pmatrix} \) and \( B = \begin{pmatrix} 1 & 0 \\ 0 & -1 \\ 1 & 1 \end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( AB \), \( BA \), \( p_{AB} \) and \( p_{BA} \), and verify that \( x^3p_{AB} = x^2p_{BA} \).
2. Hence list the eigenvalues of \( BA \) without further computation, and find an eigenvector of \( BA \) for each non-zero eigenvalue by applying \( B \) to eigenvectors of \( AB \).
:::
::::

::: {.solution}
(a) By row-times-column,
\[
AB = \begin{pmatrix} 2 & 1 \\ 0 & -2 \end{pmatrix}, \qquad BA = \begin{pmatrix} 1 & 0 & 1 \\ 0 & -2 & 0 \\ 1 & 2 & 1 \end{pmatrix}.
\]
\( AB \) is upper triangular, so \( p_{AB} = (x - 2)(x + 2) = x^2 - 4 \). Expanding \( \det(xI - BA) \) along the second row, whose only non-zero entry is \( x + 2 \) in position \( (2, 2) \),
\[
p_{BA} = (x + 2)\det\begin{pmatrix} x - 1 & -1 \\ -1 & x - 1 \end{pmatrix} = (x + 2)\big((x - 1)^2 - 1\big) = (x + 2)\,x\,(x - 2) = x^3 - 4x .
\]
Then \( x^3p_{AB} = x^5 - 4x^3 = x^2(x^3 - 4x) = x^2p_{BA} \).

(b) The eigenvalues of \( BA \) are the roots of \( x(x - 2)(x + 2) \): \( 0, 2, -2 \), matching @thm-ab-ba-eigenvalues (the non-zero ones are those of \( AB \)). If \( AB\w = \lambda\w \), then \( BA(B\w) = B(AB\w) = \lambda B\w \), so \( B\w \) is an eigenvector of \( BA \) as long as \( B\w \ne \0 \). For \( \lambda = 2 \): \( \w = (1, 0) \), \( B\w = (1, 0, 1) \), and \( BA(1, 0, 1) = (2, 0, 2) \). For \( \lambda = -2 \): \( AB + 2I = \begin{pmatrix} 4 & 1 \\ 0 & 0 \end{pmatrix} \) gives \( \w = (1, -4) \), \( B\w = (1, 4, -3) \), and \( BA(1, 4, -3) = (1 - 3, -8, 1 + 8 - 3) = (-2, -8, 6) = -2(1, 4, -3) \).
:::

:::: {#exr-spectral-mapping-b3}
[B3: Left eigenvectors of a \( 2 \times 2 \) matrix]

Let \( A = \begin{pmatrix} 0 & 1 \\ -6 & 5 \end{pmatrix} \in M_2(\nR) \), whose right eigenvectors \( (1, 2) \) for \( 2 \) and \( (1, 3) \) for \( 3 \) were found in @exr-diagonalization-b1.

::: {.enumerate options="label=(\alph*)"}
1. Find a left eigenvector of \( A \) for each eigenvalue.
2. Verify @thm-left-right-biorthogonal for these vectors, and rescale the left eigenvectors so that \( \y_i\tp\v_i = 1 \).
3. Hence write \( A^k \) as a combination of two rank-one matrices, and check the formula for \( k = 0 \) and \( k = 1 \).
:::
::::

::: {.solution}
(a) By @prp-left-eigenvectors-transpose, we need eigenvectors of \( A\tp = \begin{pmatrix} 0 & -6 \\ 1 & 5 \end{pmatrix} \). For \( 2 \): \( A\tp - 2I = \begin{pmatrix} -2 & -6 \\ 1 & 3 \end{pmatrix} \) gives \( y_1 = -3y_2 \), so \( (3, -1) \). For \( 3 \): \( A\tp - 3I = \begin{pmatrix} -3 & -6 \\ 1 & 2 \end{pmatrix} \) gives \( y_1 = -2y_2 \), so \( (2, -1) \). Check: \( \begin{pmatrix} 3 & -1 \end{pmatrix}A = \begin{pmatrix} 6 & -2 \end{pmatrix} \) and \( \begin{pmatrix} 2 & -1 \end{pmatrix}A = \begin{pmatrix} 6 & -3 \end{pmatrix} \).

(b) \( (3, -1)\cdot(1, 3) = 0 \) and \( (2, -1)\cdot(1, 2) = 0 \), as the theorem predicts for different eigenvalues. Also \( (3, -1)\cdot(1, 2) = 1 \) and \( (2, -1)\cdot(1, 3) = -1 \), so take \( \y_1 = (3, -1) \) and \( \y_2 = (-2, 1) \).

(c) With \( P = \begin{pmatrix} 1 & 1 \\ 2 & 3 \end{pmatrix} \), the rows of \( P^{-1} = \begin{pmatrix} 3 & -1 \\ -2 & 1 \end{pmatrix} \) are exactly \( \y_1\tp, \y_2\tp \), and by @prp-left-right-eigen-expansion,
\[
A^k = 2^k\begin{pmatrix} 1 \\ 2 \end{pmatrix}\begin{pmatrix} 3 & -1 \end{pmatrix} + 3^k\begin{pmatrix} 1 \\ 3 \end{pmatrix}\begin{pmatrix} -2 & 1 \end{pmatrix} = 2^k\begin{pmatrix} 3 & -1 \\ 6 & -2 \end{pmatrix} + 3^k\begin{pmatrix} -2 & 1 \\ -6 & 3 \end{pmatrix}.
\]
For \( k = 0 \): \( \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \). For \( k = 1 \): \( \begin{pmatrix} 6 - 6 & -2 + 3 \\ 12 - 18 & -4 + 9 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ -6 & 5 \end{pmatrix} = A \).
:::

### C. Going deeper

:::: {#exr-spectral-mapping-c1}
[C1: Traces of powers of \( AB \) and \( BA \)]

Let \( A \in M_{m \times n}(F) \) and \( B \in M_{n \times m}(F) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( B(AB)^{k-1}A = (BA)^k \) for every \( k \ge 1 \), and deduce that \( \tr\big((AB)^k\big) = \tr\big((BA)^k\big) \).
2. Now let \( F = \nC \). Give a second proof of the trace identity from @thm-ab-ba-eigenvalues and @cor-trace-det-of-polynomial.
:::
::::

::: {.solution}
(a) By induction on \( k \). For \( k = 1 \) both sides are \( BA \). If \( B(AB)^{k-1}A = (BA)^k \), then by associativity
\[
B(AB)^kA = B(AB)^{k-1}(AB)A = \big(B(AB)^{k-1}A\big)(BA) = (BA)^k(BA) = (BA)^{k+1}.
\]
Now \( (AB)^k = A\,\big(B(AB)^{k-1}\big) \), with \( A \) of size \( m \times n \) and \( B(AB)^{k-1} \) of size \( n \times m \). By @thm-trace-properties (c),
\[
\tr\big((AB)^k\big) = \tr\big(A \cdot B(AB)^{k-1}\big) = \tr\big(B(AB)^{k-1} \cdot A\big) = \tr\big((BA)^k\big).
\]

(b) Over \( \nC \), \( p_{AB} \) and \( p_{BA} \) split. Suppose \( m \ge n \) (otherwise swap the roles of \( A \) and \( B \)). By @thm-ab-ba-eigenvalues, \( p_{AB} = x^{m-n}p_{BA} \), so if \( \lambda_1, \dots, \lambda_n \) is the list of eigenvalues of \( BA \) with multiplicity, then the list for \( AB \) is \( \lambda_1, \dots, \lambda_n \) together with \( m - n \) zeros. For \( k \ge 1 \) the zeros contribute \( 0^k = 0 \), so by @cor-trace-det-of-polynomial, \( \tr\big((AB)^k\big) = \sum_i \lambda_i^k = \tr\big((BA)^k\big) \).
:::

:::: {#exr-spectral-mapping-c2}
[C2: Adding a commuting nilpotent matrix]

Let \( A, N \in M_n(\nC) \), \( n \ge 1 \), with \( AN = NA \) and \( N \) nilpotent.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( p_{A + N} = p_A \); in particular \( \spec(A + N) = \spec(A) \) and \( \det(A + N) = \det A \).
2. Deduce that if \( A \) is invertible, so is \( A + N \).
3. Show that (a) fails without \( AN = NA \).
:::

*Hint: triangularize \( A \) and \( N \) together.*
::::

::: {.solution}
(a) By @thm-simultaneous-triangularization there is an invertible \( P \) with \( U = P^{-1}AP \) and \( U' = P^{-1}NP \) upper triangular. Since \( N \) is nilpotent, \( \spec(N) = \{0\} \) (@exr-eigenvalues-and-eigenvectors-c2), so every diagonal entry of \( U' \) is \( 0 \) by @thm-diagonal-of-triangular-form. Then \( P^{-1}(A + N)P = U + U' \) is upper triangular with the same diagonal as \( U \). By @thm-charpoly-similarity-invariant and the examples after @def-characteristic-polynomial,
\[
p_{A + N} = p_{U + U'} = \prod_i (x - u_{ii}) = p_U = p_A .
\]
Equal characteristic polynomials have the same roots (@thm-eigenvalue-characterizations) and the same constant term \( (-1)^n\det \) (@thm-charpoly-coefficients).

(b) By (a), \( \det(A + N) = \det A \ne 0 \), so \( A + N \) is invertible (@thm-invertible-tfae-det).

(c) Let \( A = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \) and \( N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \). Both are nilpotent, so \( p_A = x^2 \), but \( A + N = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) has \( p = x^2 - 1 \) and eigenvalues \( \pm 1 \). Here \( AN = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} \ne \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} = NA \).
:::

:::: {#exr-spectral-mapping-c3}
[C3: How many traces, and which field?]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \omega = e^{2\pi i/3} \in \nC \) and \( C = \diag(1, \omega, \omega^2) \). Show that \( \tr C = \tr C^2 = 0 \) but \( C \) is not nilpotent. Explain why this does not contradict @thm-nilpotent-trace-powers.
2. Let \( n \ge 2 \). Give a matrix \( C \in M_n(\nC) \) with \( \tr C^k = 0 \) for \( k = 1, \dots, n - 1 \) that is not nilpotent.
3. Let \( A, B \in M_n(\nC) \) and suppose \( C = AB - BA \) commutes with \( A \). Prove that \( C^n = 0 \).
4. Over \( \nF_2 \), find a non-nilpotent \( C \in M_2(\nF_2) \) with \( \tr C^k = 0 \) for every \( k \ge 1 \).
:::
::::

::: {.solution}
(a) \( \omega^3 = 1 \) and \( \omega \ne 1 \), so \( 0 = \omega^3 - 1 = (\omega - 1)(\omega^2 + \omega + 1) \) gives \( 1 + \omega + \omega^2 = 0 \). Hence \( \tr C = 1 + \omega + \omega^2 = 0 \), and \( \tr C^2 = 1 + \omega^2 + \omega^4 = 1 + \omega^2 + \omega = 0 \). But \( C^k = \diag(1, \omega^k, \omega^{2k}) \ne 0 \) for every \( k \). No contradiction: the theorem, for \( n = 3 \), requires \( \tr C^k = 0 \) for \( k = 1, 2, 3 \), and \( \tr C^3 = 1 + 1 + 1 = 3 \ne 0 \).

(b) Let \( \zeta = e^{2\pi i/n} \) and \( C = \diag(1, \zeta, \dots, \zeta^{n-1}) \). For \( 1 \le k \le n - 1 \), \( \zeta^k \ne 1 \) and \( (\zeta^k)^n = 1 \), so \( \tr C^k = \sum_{j=0}^{n-1} (\zeta^k)^j = \frac{(\zeta^k)^n - 1}{\zeta^k - 1} = 0 \) by the geometric sum. But \( C^k \) has the entry \( 1 \) in position \( (1, 1) \) for all \( k \), so \( C \) is not nilpotent.

(c) By @exr-commutators-and-shoda-c2 (a), \( \tr C^k = 0 \) for every \( k \ge 1 \), in particular for \( k = 1, \dots, n \). By @thm-nilpotent-trace-powers ((e) ⇒ (d)), \( C^n = 0 \).

(d) \( C = I_2 \): \( \tr C^k = 1 + 1 = 0 \) in \( \nF_2 \) for every \( k \), and \( C^k = I_2 \ne 0 \).
:::
