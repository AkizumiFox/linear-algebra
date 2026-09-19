# The Cayley–Hamilton Theorem

An operator on an \( n \)-dimensional space now carries two monic polynomials. The characteristic polynomial \( p_T \) comes from determinants and has degree exactly \( n \). The minimal polynomial \( m_T \) comes from the ideal of polynomials that kill \( T \), and the previous section showed that it has the same roots as \( p_T \). Chapter 6 stated, without proof, the fact that ties the two together: every square matrix satisfies its own characteristic polynomial. Chapter 6 also warned against a one-line fake proof of that statement. This section gives a real proof, built on the adjugate identity of Chapter 6 read over \( F[x] \). It then draws the consequences: \( m_T \) divides \( p_T \), inverses are polynomials, and high powers of a matrix reduce to low ones.

## The statement, and a proof that is not one

Chapter 5 proved that every operator on an \( n \)-dimensional space is killed by some non-zero polynomial of degree at most \( n^2 \) (@thm-annihilating-polynomial-exists). The bound came from counting: \( \cL(V) \) has dimension \( n^2 \). Counting cannot do better, yet in every example so far a polynomial of degree at most \( n \) sufficed. The characteristic polynomial always has degree \( n \), and it is the natural candidate.

::: {#thm-cayley-hamilton}
[Cayley–Hamilton Theorem]

Let \( n \ge 1 \) and \( \A \in M_n(F) \). Then
\[
p_{\A}(\A) = 0 .
\]
Likewise, if \( V \) is a finite-dimensional vector space over \( F \) with \( \dim V \ge 1 \) and \( T \in \cL(V) \), then \( p_T(T) = 0 \).
:::

Here \( p_{\A}(\A) \) means what it always means (@def-polynomial-of-matrix): if \( p_{\A} = x^n + c_{n-1}x^{n-1} + \dots + c_1x + c_0 \), then
\[
p_{\A}(\A) = \A^n + c_{n-1}\A^{n-1} + \dots + c_1\A + c_0\I_n ,
\]
an \( n \times n \) matrix, with the constant term becoming \( c_0\I_n \).

For \( n = 2 \) the theorem can be checked by hand. With \( \A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \), \( p_{\A} = x^2 - (\tr \A)x + \det \A \), and @exr-characteristic-polynomial-c2 (b) multiplied out
\[
\A^2 - (a + d)\A + (ad - bc)\I_2 = 0 .
\]
For \( n = 3 \), the same brute force already involves cubic expressions in nine entries, and for general \( n \) it is hopeless. We need an argument. There is a tempting one, and we name it before it can do any harm.

::: {.warning}
**The fake proof of Cayley–Hamilton, again.** "Since \( p_{\A}(x) = \det(x\I - \A) \), substitute \( x = \A \) to get \( p_{\A}(\A) = \det(\A \I - \A) = \det 0 = 0 \)." Chapter 6 (the warning at the end of its §10) explained why this is not a proof. The left side \( p_{\A}(\A) \) is a **matrix**, while \( \det(\cdots) \) is a **scalar**, so the equation compares objects of different kinds. And substituting \( \A \) for \( x \) **inside the entries** of \( x\I - \A \) is not what substituting into a polynomial means: the entry \( x - a_{11} \) would have to become the matrix \( \A - a_{11}\I \), and the determinant of a matrix whose entries are matrices is undefined. The same "argument" applied to \( q(x) = \tr(x\I - \A) = nx - \tr \A \) would prove \( q(\A) = 0 \), which is false for \( \A = \diag(1, 0) \): there \( q(\A) = 2\A - \I = \diag(1, -1) \). Any correct proof must keep \( x \) a polynomial variable until the very end, and only then put a matrix in its place.
:::

## A proof through the adjugate

The adjugate identity of Chapter 6 says \( \M \adj \M = (\det \M)\,\I \) for every square matrix \( \M \), and the remark after @thm-adjugate-identity notes that its proof works over any commutative ring. Over \( F[x] \), with \( \M = x\I - \A \), it reads
\[
(x\I - \A)\,\adj(x\I - \A) = p_{\A}(x)\,\I . \tag{1}
\]
This is an identity between matrices of **polynomials**, and it contains \( p_{\A} \) on the right. The proof extracts \( p_{\A}(\A) \) from it legally.

::: {.idea}
Try \( n = 2 \) first. By @exr-cofactor-expansion-c3 (b) (done there over \( \nR \), but the computation works over any field), \( \adj(x\I - \A) = x\I - \adj \A \), a polynomial in \( x \) with **matrix coefficients** \( \B_1 = \I \) and \( \B_0 = -\adj \A \). Expanding the left side of (1),
\[
(x\I - \A)(x\I - \adj \A) = x^2\,\I - x\,(\A + \adj \A) + \A\adj \A .
\]
Comparing the coefficients of \( x^2 \), \( x \) and \( 1 \) with those of \( \big(x^2 - (\tr \A)x + \det \A\big)\I \) gives three matrix equations:
\[
\I = \I, \qquad -(\A + \adj \A) = -(\tr \A)\,\I, \qquad \A\adj \A = (\det \A)\,\I .
\]
Now multiply the first by \( \A^2 \), the second by \( \A \), the third by \( \I \), and add. The right sides add up to \( \A^2 - (\tr \A)\A + (\det \A)\I = p_{\A}(\A) \). The left sides add up to \( \A^2 - \A^2 - \A\adj \A + \A\adj \A \), in which every term cancels against its neighbor. So \( p_{\A}(\A) = 0 \). This is the whole proof; for general \( n \) there are \( n + 1 \) equations and the cancellation is a telescoping sum. The variable \( x \) is never replaced by a matrix: we compare coefficients first, and only then multiply the resulting **matrix** equations by powers of \( \A \).
:::

::: {.proof}
Let \( p_{\A} = c_nx^n + c_{n-1}x^{n-1} + \dots + c_1x + c_0 \) with \( c_n = 1 \) (@thm-charpoly-coefficients).

**Step 1: the adjugate as a polynomial with matrix coefficients.** If \( n = 1 \), then \( \adj(x\I - \A) = (1) \) by @def-adjugate. If \( n \ge 2 \), each entry of \( \adj(x\I - \A) \) is a cofactor \( \pm\det \N \), where \( \N \) is an \( (n - 1) \times (n - 1) \) submatrix of \( x\I - \A \) (@def-adjugate, @def-minor-cofactor). Every entry of \( \N \) lies in \( F[x]_{\le 1} \). A product of \( n - 1 \) such polynomials lies in \( F[x]_{\le n-1} \) (@thm-degree-of-product, the zero polynomial being harmless), and so does a sum of such products (@thm-degree-of-sum); in particular the Leibniz sum \( \det \N \) does (@def-determinant). In both cases every entry of \( \adj(x\I - \A) \) lies in \( F[x]_{\le n - 1} \). For \( 0 \le k \le n - 1 \), let \( \B_k \in M_n(F) \) be the matrix whose \( (i, j) \)-entry is the coefficient of \( x^k \) in the \( (i, j) \)-entry of \( \adj(x\I - \A) \). Then, entry by entry,
\[
\adj(x\I - \A) = \sum_{k=0}^{n-1} x^k \B_k .
\]
Put \( \B_{-1} = \B_n = 0 \) for convenience.

**Step 2: compare coefficients.** By (1), which holds by @thm-adjugate-identity over the commutative ring \( F[x] \) (the remark after it), the \( (i, j) \)-entries of both sides of (1) agree. On the left, by @def-matrix-multiplication,
\[
\sum_{l=1}^{n} (x\delta_{il} - a_{il}) \sum_{k=0}^{n-1} (\B_k)_{lj}\,x^k = \sum_{k=0}^{n-1} (\B_k)_{ij}\,x^{k+1} - \sum_{k=0}^{n-1} (\A \B_k)_{ij}\,x^k ,
\]
where \( \delta_{il} = 1 \) if \( i = l \) and \( 0 \) otherwise. So for \( 0 \le k \le n \), the coefficient of \( x^k \) is \( (\B_{k-1})_{ij} - (\A \B_k)_{ij} \). On the right the \( (i, j) \)-entry is \( p_{\A}\,\delta_{ij} \), whose coefficient of \( x^k \) is \( c_k\delta_{ij} \). Two polynomials are equal exactly when their coefficients are equal (@def-polynomial). Since this holds for every \( (i, j) \),
\[
\B_{k-1} - \A \B_k = c_k\,\I \qquad (0 \le k \le n) . \tag{2}
\]

**Step 3: telescope.** Multiply equation (2) for \( k \) on the left by \( \A^k \), and add the \( n + 1 \) equations. On the right we get \( \sum_{k=0}^{n} c_k\A^k = p_{\A}(\A) \) by @def-polynomial-of-matrix. On the left, writing \( \S_k = \A^k\B_{k-1} \) for \( 0 \le k \le n + 1 \),
\[
\sum_{k=0}^{n} \big(\A^k\B_{k-1} - \A^{k+1}\B_k\big) = \sum_{k=0}^{n} (\S_k - \S_{k+1}) = \S_0 - \S_{n+1} = \B_{-1} - \A^{n+1}\B_n = 0 ,
\]
since \( \B_{-1} = \B_n = 0 \). Hence \( p_{\A}(\A) = 0 \).

**The operator version.** Let \( \sB \) be a basis of \( V \) and \( \A = [T]_{\sB} \). By @def-charpoly-operator, \( p_T = p_{\A} \). By @cor-matrix-of-polynomial-of-operator, \( [p_T(T)]_{\sB} = p_T(\A) = p_{\A}(\A) = 0 \), so \( p_T(T) = 0 \) (@thm-linear-maps-isomorphic-to-matrices). This proves the theorem.
:::

Compare with the fake proof. There, \( \A \) was pushed into the entries of \( x\I - \A \). Here, (1) is first unpacked into the \( n + 1 \) matrix equations (2), which contain no \( x \) at all, and \( \A \) enters only when we multiply those equations by \( \A^k \). Every multiplication is on the **left**, so no commutativity of matrices was used; the only commutativity used is inside \( F[x] \), in the adjugate identity.

Nothing in the proof divides. The determinant, the adjugate identity, coefficient comparison and matrix multiplication all make sense over a commutative ring, and @exr-cayley-hamilton-c1 asks you to check that the theorem holds, with the same proof, for matrices with entries in a commutative ring such as \( \nZ \) or \( \nR[t] \).

The proof also produced more than it was asked for. Equation (2) with \( k = n \) says \( \B_{n-1} = \I \), and the others say \( \B_{k-1} = \A \B_k + c_k\I \). Working down from \( \B_{n-1} \), every \( \B_k \) is a polynomial in \( \A \); @exr-cayley-hamilton-c2 turns this into a formula for \( \adj \A \).

## Consequences

The first consequence is the promised comparison of the two polynomials.

::: {#cor-minimal-divides-characteristic}
[The Minimal Polynomial Divides the Characteristic Polynomial]

Let \( V \) be finite-dimensional with \( \dim V = n \ge 1 \), and let \( T \in \cL(V) \).

::: {.enumerate options="label=(\alph*)"}
1. \( m_T \mid p_T \); in particular \( 1 \le \deg m_T \le n \).
2. If \( p_T \) splits over \( F \), say \( p_T = (x - \lambda_1)^{a_1} \cdots (x - \lambda_k)^{a_k} \) with distinct \( \lambda_i \), then
\[
m_T = (x - \lambda_1)^{s_1} \cdots (x - \lambda_k)^{s_k} \qquad \text{with } 1 \le s_i \le a_i = a_T(\lambda_i) .
\]
:::

The same holds for \( \A \in M_n(F) \) with \( m_{\A} \) and \( p_{\A} \). In particular, over \( \nC \), (b) applies to every \( \A \in M_n(\nC) \).
:::

::: {.proof}
(a) By @thm-cayley-hamilton, \( p_T(T) = 0 \), so \( m_T \mid p_T \) by @thm-minimal-polynomial-divides. Since \( p_T \) is monic of degree \( n \) (@thm-charpoly-coefficients), \( \deg m_T \le n \) by @prp-divisibility-properties (c), and \( \deg m_T \ge 1 \) by @thm-minimal-polynomial-divides, as \( V \ne \{\0\} \).

(b) A polynomial \( x - \lambda \) of degree \( 1 \) is irreducible: if \( x - \lambda = gh \), then \( \deg g + \deg h = 1 \) (@thm-degree-of-product), so one factor is constant. The \( x - \lambda_i \) are distinct and monic. By (a) and @lem-monic-divisors, \( m_T = \prod_i (x - \lambda_i)^{s_i} \) with \( 0 \le s_i \le a_i \). Each \( \lambda_i \) is a root of \( p_T \), hence an eigenvalue (@thm-eigenvalue-characterizations), hence a root of \( m_T \) (@thm-minimal-polynomial-roots), so \( s_i \ge 1 \). Finally \( a_i = \operatorname{mult}_{\lambda_i}(p_T) = a_T(\lambda_i) \) by @lem-multiplicity-cofactor, since the other factors do not vanish at \( \lambda_i \). The matrix case is the operator \( T_{\A} \), and over \( \nC \) every \( p_{\A} \) splits (@cor-complex-polynomial-splits).
:::

This pays off a promise from Chapter 5: the bound \( n^2 \) of @thm-annihilating-polynomial-exists improves to \( n \), and \( p_T \) is an explicit annihilating polynomial of degree exactly \( n \). It also makes Method 2 of the previous section a finite search that always succeeds. For a matrix with \( p_{\A} = (x - 2)^2(x - 3) \), the corollary leaves exactly two candidates, \( (x - 2)(x - 3) \) and \( (x - 2)^2(x - 3) \), and one matrix product decides between them.

::: {.warning}
**Cayley–Hamilton gives an annihilating polynomial, not the minimal one.** From \( p_{\A}(\A) = 0 \) we may **not** conclude \( m_{\A} = p_{\A} \); only \( m_{\A} \mid p_{\A} \). For \( \A = \diag(1, 1, 2) \), \( p_{\A} = (x - 1)^2(x - 2) \) kills \( \A \), and so does the proper divisor \( (x - 1)(x - 2) = m_{\A} \). Nor may we conclude that every divisor of \( p_{\A} \) with the right roots kills \( \A \): for \( \J = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \), \( x - 1 \) has the right root and does not.
:::

The second consequence expresses inverses through powers.

::: {#cor-inverse-polynomial}
[The Inverse Is a Polynomial in the Matrix]

Let \( n \ge 1 \), \( \A \in M_n(F) \), and \( p_{\A} = x^n + c_{n-1}x^{n-1} + \dots + c_1x + c_0 \). Then \( c_0 = (-1)^n\det \A \). If \( \A \) is invertible, then \( c_0 \ne 0 \) and
\[
\A^{-1} = -\frac{1}{c_0}\big(\A^{n-1} + c_{n-1}\A^{n-2} + \dots + c_2\A + c_1\I\big).
\]
(For \( n = 1 \) the bracket is \( \I \) alone, and the formula reads \( \A^{-1} = -c_0^{-1}\I \).) The same holds for an invertible operator \( T \) on a space of dimension \( n \ge 1 \), with \( \id_V \) in place of \( \I \).
:::

::: {.proof}
By @thm-charpoly-coefficients, \( c_0 = (-1)^n\det \A \), which is non-zero when \( \A \) is invertible (@thm-invertible-tfae-det). By @thm-cayley-hamilton,
\[
\A\big(\A^{n-1} + c_{n-1}\A^{n-2} + \dots + c_1\I\big) = \A^n + c_{n-1}\A^{n-1} + \dots + c_1\A = -c_0\I .
\]
Multiplying by \( -c_0^{-1} \), the matrix in parentheses times \( -c_0^{-1} \) is a right inverse of \( \A \), hence the inverse by @thm-one-sided-inverse. For an operator, apply this to \( [T]_{\sB} \) and use @cor-matrix-of-polynomial-of-operator.
:::

So inverting an \( n \times n \) matrix never requires more than its first \( n - 1 \) powers and the coefficients of \( p_{\A} \). The theorem also reduces **every** power of \( \A \) to the first \( n - 1 \). Divide \( x^N \) by \( p_{\A} \) (@thm-polynomial-division): \( x^N = q\,p_{\A} + r \) with \( \deg r < n \). Then by @thm-evaluation-homomorphism and @thm-cayley-hamilton,
\[
\A^N = q(\A)\,p_{\A}(\A) + r(\A) = r(\A) .
\]
When \( p_{\A} \) has \( n \) distinct roots \( \lambda_1, \dots, \lambda_n \), the remainder can be found without long division. Substituting \( x = \lambda_i \) in \( x^N = q\,p_{\A} + r \) gives \( r(\lambda_i) = \lambda_i^N \) for each \( i \), and these \( n \) conditions determine \( r \in F[x]_{\le n-1} \) by Lagrange interpolation (@thm-lagrange-interpolation). This substitution is legal: \( \lambda_i \) is a **scalar** plugged into an identity of polynomials.

::: {#exm-cayley-hamilton-3x3}
[Cayley–Hamilton for a \( 3 \times 3 \) Matrix]

Let
\[
\A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 1 \end{pmatrix} \in M_3(\nQ).
\]
Compute \( p_{\A} \) and verify \( p_{\A}(\A) = 0 \). Then use it to find \( \A^{-1} \) and \( \A^5 \), and write down the matrices \( \B_k \) of the proof.
:::

::: {.solution}
*Characteristic polynomial.* Expand \( \det(x\I - \A) \) along the first row (@thm-laplace-expansion over \( \nQ[x] \)):
\[
\begin{aligned}
p_{\A} &= \det\begin{pmatrix} x - 1 & -1 & 0 \\ 0 & x & -1 \\ -1 & 0 & x - 1 \end{pmatrix} \\
  &= (x - 1)\det\begin{pmatrix} x & -1 \\ 0 & x - 1 \end{pmatrix} + (-1)(-1)^{1+2}\det\begin{pmatrix} 0 & -1 \\ -1 & x - 1 \end{pmatrix}.
\end{aligned}
\]
The two minors are \( x(x - 1) \) and \( -1 \), so \( p_{\A} = x(x - 1)^2 - 1 = x^3 - 2x^2 + x - 1 \). As a check, \( \tr \A = 2 \) matches the coefficient \( -2 \) of \( x^2 \), and \( c_0 = -1 = (-1)^3\det \A \) says \( \det \A = 1 \).

*Verification.* Multiplying out,
\[
\A^2 = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 0 & 1 \\ 2 & 1 & 1 \end{pmatrix}, \qquad \A^3 = \A\,\A^2 = \begin{pmatrix} 2 & 1 & 2 \\ 2 & 1 & 1 \\ 3 & 2 & 2 \end{pmatrix}.
\]
Then \( \A^3 - 2\A^2 + \A - \I \) has first row \( (2 - 2 + 1 - 1,\ 1 - 2 + 1,\ 2 - 2 + 0) = (0, 0, 0) \), second row \( (2 - 2 + 0,\ 1 - 0 + 0 - 1,\ 1 - 2 + 1) = (0, 0, 0) \), and third row \( (3 - 4 + 1,\ 2 - 2 + 0,\ 2 - 2 + 1 - 1) = (0, 0, 0) \). So \( p_{\A}(\A) = 0 \), as the theorem predicts.

*Inverse.* Here \( c_0 = -1 \), \( c_1 = 1 \), \( c_2 = -2 \). By @cor-inverse-polynomial,
\[
\A^{-1} = \A^2 - 2\A + \I = \begin{pmatrix} 0 & -1 & 1 \\ 1 & 1 & -1 \\ 0 & 1 & 0 \end{pmatrix}.
\]
Check: the first row of \( \A\,\A^{-1} \) is \( (0 + 1,\ -1 + 1,\ 1 - 1) = (1, 0, 0) \), and the other rows work the same way. The entries are integers, as they must be for an integer matrix of determinant \( 1 \) (@cor-integer-inverse).

*Fifth power.* The relation \( \A^3 = 2\A^2 - \A + \I \) lets us lower degrees step by step:
\[
\A^4 = 2\A^3 - \A^2 + \A = 2(2\A^2 - \A + \I) - \A^2 + \A = 3\A^2 - \A + 2\I,
\]
\[
\A^5 = 3\A^3 - \A^2 + 2\A = 3(2\A^2 - \A + \I) - \A^2 + 2\A = 5\A^2 - \A + 3\I .
\]
(Equivalently, \( x^5 = (x^2 + 2x + 3)\,p_{\A} + (5x^2 - x + 3) \).) Hence
\[
\A^5 = 5\begin{pmatrix} 1 & 1 & 1 \\ 1 & 0 & 1 \\ 2 & 1 & 1 \end{pmatrix} - \begin{pmatrix} 1 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 1 \end{pmatrix} + 3\I = \begin{pmatrix} 7 & 4 & 5 \\ 5 & 3 & 4 \\ 9 & 5 & 7 \end{pmatrix}.
\]

*The matrices of the proof.* By (2), \( \B_2 = \I \), \( \B_1 = \A \B_2 + c_2\I = \A - 2\I \) and \( \B_0 = \A \B_1 + c_1\I = \A^2 - 2\A + \I \). So
\[
\begin{aligned}
\adj(x\I - \A) &= x^2 \I + x(\A - 2\I) + (\A^2 - 2\A + \I) \\
  &= \begin{pmatrix} x^2 - x & x - 1 & 1 \\ 1 & x^2 - 2x + 1 & x - 1 \\ x & 1 & x^2 - x \end{pmatrix},
\end{aligned}
\]
which one can confirm entry by entry from cofactors of \( x\I - \A \); for instance the \( (1, 3) \)-entry is the cofactor \( C_{31} = \det\begin{pmatrix} -1 & 0 \\ x & -1 \end{pmatrix} = 1 \). The last equation of (2), \( -\A \B_0 = c_0\I = -\I \), is the statement \( \A^{-1} = \B_0 \) found above.
:::

::: {.check}
Let \( \A \in M_2(\nR) \) with \( \tr \A = 5 \) and \( \det \A = 6 \). Write \( \A^2 \) and \( \A^3 \) as combinations of \( \A \) and \( \I \), and write \( \A^{-1} \) the same way.
:::

::: {.solution}
\( p_{\A} = x^2 - 5x + 6 \), so by @thm-cayley-hamilton \( \A^2 = 5\A - 6\I \). Then \( \A^3 = 5\A^2 - 6\A = 5(5\A - 6\I) - 6\A = 19\A - 30\I \). By @cor-inverse-polynomial with \( c_0 = 6 \) and \( c_1 = -5 \), \( \A^{-1} = -\tfrac16(\A - 5\I) = \tfrac16(5\I - \A) \).
:::

**Alternatively.** When \( p_T \) splits, there is a second proof that avoids determinants of polynomial matrices entirely. The next section shows that such an operator has an upper triangular matrix, and a triangular matrix reveals directly why the product \( (T - \lambda_1\id_V) \cdots (T - \lambda_n\id_V) \) is zero. That proof is set out as an exercise there. The adjugate proof has the advantage of working over every field at once, with no splitting hypothesis.

## Exercises

### A. Check your understanding

:::: {#exr-cayley-hamilton-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the Cayley–Hamilton Theorem for \( \A \in M_n(F) \).
2. True or false: \( \deg m_{\A} \le n \) for every \( \A \in M_n(F) \), \( n \ge 1 \). Justify your answer.
3. In one sentence, why is "\( p_{\A}(\A) = \det(\A \I - \A) = 0 \)" not a proof?
4. Suppose \( p_{\A} = (x - 1)^2(x + 2) \). Which polynomials can \( m_{\A} \) be?
5. True or false: if \( p_{\A}(\A) = 0 \), then \( p_{\A} \) is the minimal polynomial of \( \A \). Justify your answer.
6. How do you write \( \A^{-1} \) as a polynomial in \( \A \) when \( \A \) is invertible?
:::
::::

::: {.solution}
(a) If \( n \ge 1 \) and \( \A \in M_n(F) \), then \( p_{\A}(\A) = 0 \) (@thm-cayley-hamilton).

(b) True. By @cor-minimal-divides-characteristic, \( m_{\A} \mid p_{\A} \), and \( \deg p_{\A} = n \).

(c) It substitutes a matrix into the entries of \( x\I - \A \) and then equates the matrix \( p_{\A}(\A) \) with the scalar \( \det 0 \), neither of which is legitimate.

(d) By @cor-minimal-divides-characteristic (b), \( m_{\A} = (x - 1)^{s}(x + 2)^{t} \) with \( 1 \le s \le 2 \) and \( t = 1 \): so \( (x - 1)(x + 2) \) or \( (x - 1)^2(x + 2) \). Both occur, for \( \diag(1, 1, -2) \) and for \( \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \oplus (-2) \) (@prp-minimal-polynomial-block-diagonal).

(e) False. \( p_{\I_2} = (x - 1)^2 \) kills \( \I_2 \), but \( m_{\I_2} = x - 1 \).

(f) If \( p_{\A} = x^n + c_{n-1}x^{n-1} + \dots + c_0 \), then \( c_0 = (-1)^n\det \A \ne 0 \) and \( \A^{-1} = -c_0^{-1}(\A^{n-1} + c_{n-1}\A^{n-2} + \dots + c_1\I) \) (@cor-inverse-polynomial).
:::

### B. Practice

:::: {#exr-cayley-hamilton-b1}
[B1: Inverse and a hundredth power]

Let \( \A = \begin{pmatrix} 3 & -2 \\ 1 & 0 \end{pmatrix} \in M_2(\nR) \).

::: {.enumerate options="label=(\alph*)"}
1. Find \( p_{\A} \), and use the Cayley–Hamilton Theorem to compute \( \A^{-1} \).
2. Hence find \( \A^{100} \) as a combination \( a\A + b\I \), and write it as a matrix.
:::
::::

::: {.solution}
(a) \( \tr \A = 3 \) and \( \det \A = 2 \), so \( p_{\A} = x^2 - 3x + 2 = (x - 1)(x - 2) \). By @thm-cayley-hamilton, \( \A^2 - 3\A + 2\I = 0 \), that is, \( \A(3\I - \A) = 2\I \). By @cor-inverse-polynomial,
\[
\A^{-1} = \tfrac12(3\I - \A) = \begin{pmatrix} 0 & 1 \\ -\frac12 & \frac32 \end{pmatrix}.
\]
Check: \( \A\,\A^{-1} = \begin{pmatrix} 0 + 1 & 3 - 3 \\ 0 & 1 \end{pmatrix} = \I \).

(b) By @thm-polynomial-division, \( x^{100} = q\,p_{\A} + (ax + b) \) for some \( q \) and scalars \( a, b \). Substituting the roots \( x = 1 \) and \( x = 2 \) of \( p_{\A} \) gives \( 1 = a + b \) and \( 2^{100} = 2a + b \). So \( a = 2^{100} - 1 \) and \( b = 2 - 2^{100} \). By @thm-cayley-hamilton, \( \A^{100} = q(\A)p_{\A}(\A) + a\A + b\I = a\A + b\I \), that is,
\[
\A^{100} = (2^{100} - 1)\A + (2 - 2^{100})\I = \begin{pmatrix} 2^{101} - 1 & 2 - 2^{101} \\ 2^{100} - 1 & 2 - 2^{100} \end{pmatrix}.
\]
For \( k = 1 \) in place of \( 100 \), the same recipe gives \( a = 1 \), \( b = 0 \), and returns \( \A \), as it should.
:::

:::: {#exr-cayley-hamilton-b2}
[B2: Trace zero in size two]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \A \in M_2(F) \) with \( \tr \A = 0 \). Prove that \( \A^2 = -(\det \A)\,\I \).
2. Deduce that for all \( \X, \Y \in M_2(F) \), the matrix \( (\X \Y - \Y \X)^2 \) is a scalar multiple of \( \I \).
3. Show that the converse of (a) fails: give \( \A \in M_2(\nR) \) with \( \A^2 \) scalar and \( \tr \A \ne 0 \).
:::
::::

::: {.solution}
(a) By @thm-cayley-hamilton, \( \A^2 - (\tr \A)\A + (\det \A)\I = 0 \). With \( \tr \A = 0 \), this is \( \A^2 = -(\det \A)\I \).

(b) By @thm-trace-operator-properties applied to \( T_{\X}, T_{\Y} \), or directly by \( \tr(\X \Y) = \tr(\Y \X) \), we have \( \tr(\X \Y - \Y \X) = 0 \). By (a), \( (\X \Y - \Y \X)^2 = -\det(\X \Y - \Y \X)\,\I \).

(c) \( \A = \I_2 \) has \( \A^2 = \I_2 \) and \( \tr \A = 2 \ne 0 \).
:::

:::: {#exr-cayley-hamilton-b3}
[B3: Minimal polynomial from one product]

Each of the real matrices
\[
\M_1 = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 0 \\ -1 & 1 & 3 \end{pmatrix}, \qquad \M_2 = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ -1 & 0 & 3 \end{pmatrix}
\]
has characteristic polynomial \( (x - 2)^2(x - 3) \). Find \( m_{\M_1} \) and \( m_{\M_2} \). Are \( \M_1 \) and \( \M_2 \) similar?
::::

::: {.solution}
By @cor-minimal-divides-characteristic (b), each minimal polynomial is \( (x - 2)(x - 3) \) or \( (x - 2)^2(x - 3) \), and only the first needs testing.

For \( \M_1 \): \( \M_1 - 2\I = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ -1 & 1 & 1 \end{pmatrix} \) and \( \M_1 - 3\I = \begin{pmatrix} -1 & 1 & 0 \\ 0 & -1 & 0 \\ -1 & 1 & 0 \end{pmatrix} \). The first row of the product \( (\M_1 - 2\I)(\M_1 - 3\I) \) is row \( 2 \) of \( \M_1 - 3\I \), namely \( (0, -1, 0) \ne \0 \). So \( m_{\M_1} = (x - 2)^2(x - 3) \).

For \( \M_2 \): \( \M_2 - 2\I = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ -1 & 0 & 1 \end{pmatrix} \) and \( \M_2 - 3\I = \begin{pmatrix} -1 & 0 & 0 \\ 0 & -1 & 0 \\ -1 & 0 & 0 \end{pmatrix} \). The only non-zero row of the product is \( -(\text{row } 1) + (\text{row } 3) \) of \( \M_2 - 3\I \), which is \( (1, 0, 0) + (-1, 0, 0) = \0 \). So the product is \( 0 \), and \( m_{\M_2} = (x - 2)(x - 3) \).

The minimal polynomials differ, so \( \M_1 \not\sim \M_2 \) by @thm-minimal-polynomial-similarity.
:::

### C. Going deeper

:::: {#exr-cayley-hamilton-c1}
[C1: Cayley–Hamilton over a commutative ring]

Let \( R \) be a commutative ring (the remark in Chapter 6, §4), and suppose, as for \( F[x] \), that the polynomials in \( x \) with coefficients in \( R \) form a commutative ring \( R[x] \) in which two polynomials are equal exactly when all their coefficients are equal. For \( \A \in M_n(R) \), define \( p_{\A} = \det(x\I - \A) \in R[x] \).

::: {.enumerate options="label=(\alph*)"}
1. Go through the proof of @thm-cayley-hamilton and name, for each step, the fact it uses. Explain why each fact holds over \( R \) and \( R[x] \), and conclude that \( p_{\A}(\A) = 0 \) for every \( \A \in M_n(R) \).
2. Let \( R = \nR[t] \) and \( \A = \begin{pmatrix} t & 1 \\ t^2 & 0 \end{pmatrix} \). Compute \( p_{\A} \) and verify \( p_{\A}(\A) = 0 \) directly.
3. Let \( \A \in M_n(\nZ) \) with \( \det \A = \pm 1 \). Using (a) with \( R = \nZ \), show that \( \A^{-1} \) has integer entries.
:::
::::

::: {.solution}
(a) *The shape of \( p_{\A} \).* In the Leibniz sum for \( \det(x\I - \A) \), the identity permutation contributes \( (x - a_{11})\cdots(x - a_{nn}) \), of degree \( n \) with leading coefficient \( 1 \), and every other term omits at least two diagonal entries, so it has degree at most \( n - 2 \). Hence \( p_{\A} = x^n + c_{n-1}x^{n-1} + \dots + c_0 \) with \( c_k \in R \), which is what the proof uses in place of @thm-charpoly-coefficients; only sums and products of entries appear. *Step 1* uses the Leibniz formula over \( R[x] \) (which only multiplies and adds entries) and the degree bounds for sums and products, which hold because the degree of a product of polynomials is at most the sum of the degrees; no inverse is needed for the upper bound. *Step 2* uses the adjugate identity over the commutative ring \( R[x] \), which holds by the remark after @thm-adjugate-identity, and coefficient comparison in \( R[x] \), which is the assumption on \( R[x] \). *Step 3* uses only associativity and distributivity of matrix multiplication over \( R \) and a telescoping sum. No step divides, so each works verbatim over \( R \), and \( p_{\A}(\A) = 0 \).

(b) \( x\I - \A = \begin{pmatrix} x - t & -1 \\ -t^2 & x \end{pmatrix} \), so \( p_{\A} = x(x - t) - t^2 = x^2 - tx - t^2 \). Then
\[
\A^2 = \begin{pmatrix} t^2 + t^2 & t \\ t^3 & t^2 \end{pmatrix}, \qquad \A^2 - t\A - t^2\I = \begin{pmatrix} 2t^2 - t^2 - t^2 & t - t \\ t^3 - t^3 & t^2 - 0 - t^2 \end{pmatrix} = 0 .
\]

(c) The Leibniz formula for \( \det(x\I - \A) \) only adds and multiplies integers and \( x \), so the coefficients \( c_k \) of \( p_{\A} \) are integers. Regarding \( \A \) as a rational matrix, @thm-charpoly-coefficients gives \( c_0 = (-1)^n\det \A = \pm 1 \). By (a), \( \A(\A^{n-1} + c_{n-1}\A^{n-2} + \dots + c_1\I) = -c_0\I \). Since \( c_0^2 = 1 \), multiplying by \( -c_0 \) gives \( \A\,\B = \I \) with \( \B = -c_0(\A^{n-1} + \dots + c_1\I) \in M_n(\nZ) \). Regarding \( \A \) and \( \B \) as rational matrices, @thm-one-sided-inverse gives \( \B = \A^{-1} \), which therefore has integer entries. (This reproves part of @cor-integer-inverse.)
:::

:::: {#exr-cayley-hamilton-c2}
[C2: The adjugate is a polynomial in the matrix]

Let \( n \ge 2 \), \( \A \in M_n(F) \), \( p_{\A} = x^n + c_{n-1}x^{n-1} + \dots + c_0 \), and let \( \B_0, \dots, \B_{n-1} \) be as in the proof of @thm-cayley-hamilton.

::: {.enumerate options="label=(\alph*)"}
1. Using equation (2) of the proof, show that \( \B_0 = \A^{n-1} + c_{n-1}\A^{n-2} + \dots + c_2\A + c_1\I \).
2. Show that the constant matrix \( \B_0 \) equals \( \adj(-\A) \), and that \( \adj(-\A) = (-1)^{n-1}\adj \A \).
3. Deduce that for **every** \( \A \in M_n(F) \), invertible or not,
\[
\adj \A = (-1)^{n-1}\big(\A^{n-1} + c_{n-1}\A^{n-2} + \dots + c_2\A + c_1\I\big).
\]
4. Check (c) for \( \S = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 1 & 0 & 1 \end{pmatrix} \), whose adjugate Chapter 6 computed (the warning after @cor-inverse-formula), given that \( p_{\S} = x^3 - 6x^2 + 2x \).
:::
::::

::: {.solution}
(a) Equation (2) with \( k = n \) gives \( \B_{n-1} = c_n\I = \I \), and for \( 1 \le k \le n - 1 \) it gives \( \B_{k-1} = \A \B_k + c_k\I \). By downward induction on \( k \), \( \B_{k-1} = \A^{n-k} + c_{n-1}\A^{n-k-1} + \dots + c_k\I \): this holds for \( k = n \), and if it holds for \( k \), then \( \B_{k-2} = \A \B_{k-1} + c_{k-1}\I = \A^{n-k+1} + c_{n-1}\A^{n-k} + \dots + c_k\A + c_{k-1}\I \). The case \( k = 1 \) is the claim.

(b) Each entry of \( \adj(x\I - \A) \) is a cofactor \( \pm\det \N \) of \( x\I - \A \), and its constant coefficient is its value at \( 0 \). By @lem-evaluate-polynomial-matrix, \( (\det \N)(0) = \det \N(0) \), and \( \N(0) \) is the corresponding submatrix of \( -\A \). So the matrix of constant coefficients, \( \B_0 \), is \( \adj(-\A) \). Each cofactor of \( -\A \) is \( \pm \) the determinant of an \( (n - 1) \times (n - 1) \) submatrix of \( -\A \), which is \( -1 \) times the corresponding submatrix of \( \A \). Multiplying each of the \( n - 1 \) rows by \( -1 \) multiplies the determinant by \( (-1)^{n-1} \) (@thm-det-row-operations). Hence \( \adj(-\A) = (-1)^{n-1}\adj \A \).

(c) By (a) and (b), \( (-1)^{n-1}\adj \A = \B_0 = \A^{n-1} + c_{n-1}\A^{n-2} + \dots + c_1\I \); multiply by \( (-1)^{n-1} \). Nothing assumed \( \det \A \ne 0 \).

(d) Here \( n = 3 \), \( c_2 = -6 \), \( c_1 = 2 \), so the formula predicts \( \adj \S = \S^2 - 6\S + 2\I \). Now
\[
\begin{aligned}
\S^2 &= \begin{pmatrix} 8 & 10 & 18 \\ 16 & 20 & 36 \\ 2 & 2 & 4 \end{pmatrix}, \\
\S^2 - 6\S + 2\I &= \begin{pmatrix} 8 - 6 + 2 & 10 - 12 & 18 - 18 \\ 16 - 12 & 20 - 24 + 2 & 36 - 36 \\ 2 - 6 & 2 & 4 - 6 + 2 \end{pmatrix} \\
  &= \begin{pmatrix} 4 & -2 & 0 \\ 4 & -2 & 0 \\ -4 & 2 & 0 \end{pmatrix},
\end{aligned}
\]
which is the adjugate found in Chapter 6.
:::

:::: {#exr-cayley-hamilton-c3}
[C3: Nilpotent matrices of size \( n \)]

Let \( F \) be any field, \( n \ge 1 \), and \( \A \in M_n(F) \) with \( \A^k = 0 \) for some \( k \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( m_{\A} = x^s \) for some \( s \) with \( 1 \le s \le n \).
2. Deduce that \( \A^n = 0 \).
3. Give a \( 3 \times 3 \) example with \( \A^2 \ne 0 \), and explain why no \( 3 \times 3 \) matrix has \( \A^3 \ne 0 = \A^4 \).
:::
::::

::: {.solution}
(a) \( x^k \) annihilates \( \A \), so \( m_{\A} \mid x^k \) (@thm-minimal-polynomial-divides). The polynomial \( x \) is monic and irreducible (degree \( 1 \)), so by @lem-monic-divisors, \( m_{\A} = x^s \) with \( 0 \le s \le k \). By @cor-minimal-divides-characteristic (a), \( 1 \le s = \deg m_{\A} \le n \).

(b) \( x^n = x^{n-s}\,x^s \), so \( m_{\A} \mid x^n \) and \( \A^n = 0 \) by @thm-minimal-polynomial-divides.

(c) The matrix \( \N \) of the Quick check in Section 5 has \( \N^2 \ne 0 = \N^3 \). If \( \A \in M_3(F) \) satisfies \( \A^4 = 0 \), then \( \A \) is nilpotent and \( \A^3 = 0 \) by (b), so \( \A^3 \ne 0 = \A^4 \) is impossible. Note that no splitting or complex numbers were needed; compare @exr-eigenvalues-and-eigenvectors-c2, which worked over \( \nC \).
:::
