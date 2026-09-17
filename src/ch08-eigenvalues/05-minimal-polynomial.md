# The Minimal Polynomial

Section 4 decided diagonalizability by counting eigenvectors, one eigenspace at a time. There is a second source of information about an operator, which Chapter 5 set up: the polynomials that kill it. On a finite-dimensional space they form an ideal of \( F[x] \), and that ideal has a single monic generator. This section gives the generator its name, the minimal polynomial, and shows that its roots are exactly the eigenvalues. We learn two ways to compute it and check that similar matrices share it. The next section compares it with the characteristic polynomial, and Section 8 reads diagonalizability off its factorization.

## The polynomial that divides all the others

Chapter 5 turned every polynomial identity satisfied by an operator into a statement about one ideal. For \( T \in \cL(V) \), the set
\[
I_T = \{ p \in F[x] : p(T) = 0 \}
\]
is an ideal of \( F[x] \) (@thm-annihilator-ideal (a)). If \( V \) is finite-dimensional, it contains a non-zero polynomial (@thm-annihilator-ideal (c)). Then it consists of the multiples of a unique monic polynomial (@thm-annihilator-ideal (b)).

Look at what this says for one operator. A projection \( P \) with \( P \ne 0, \id_V \) satisfies \( P^2 = P \), so \( x^2 - x \) kills it. So do \( x^3 - x^2 \), \( (x^2 - x)(x + 5) \) and \( x^{10} - x^9 \), and a short calculation shows each one is a multiple of \( x^2 - x \). This is no accident. Every annihilating polynomial of \( P \) is a multiple of \( x^2 - x \), which Chapter 5 found to be the monic generator of \( I_P \). One polynomial controls the whole list, and whenever something in mathematics is unique we give it a name.

*The minimal polynomial of \( T \) is the one monic polynomial that kills \( T \) and divides every other polynomial that kills \( T \).*

::: {#def-minimal-polynomial}
[Minimal Polynomial]

Let \( V \) be a **finite-dimensional** vector space over \( F \) and \( T \in \cL(V) \). The **minimal polynomial** of \( T \) is **the** unique **monic** polynomial \( m_T \in F[x] \) with
\[
I_T = \{ p \in F[x] : p(T) = 0 \} = \langle m_T \rangle .
\]
Equivalently, \( m_T \) is the monic polynomial of **least degree** with \( m_T(T) = 0 \).

For \( A \in M_n(F) \), the minimal polynomial is \( m_A \coloneqq m_{T_A} \): the monic polynomial of least degree with \( m_A(A) = 0 \).
:::

In words: we look at **all** polynomials \( p \) with \( p(T) = 0 \), where \( p(T) \) replaces \( x^k \) by \( T^k \) and the constant term \( c \) by \( c\,\id_V \) (@def-polynomial-of-operator). They are exactly the multiples of one polynomial \( m_T \). Among the generators of this ideal, which differ by non-zero constant factors, we pick **the monic** one. The second sentence of the definition gives the same polynomial described by size: it is the monic polynomial of **least degree** that kills \( T \).

**Well-definedness.** Three things need checking, and Chapter 5 did all three. *Existence:* \( I_T \ne \{0\} \) because \( V \) is finite-dimensional (@thm-annihilator-ideal (c)). *Uniqueness:* a non-zero ideal of \( F[x] \) has exactly one monic generator (@thm-ideals-principal). *The two descriptions agree:* the same theorem says that the monic generator is the unique monic polynomial of least degree in the ideal. For a matrix, \( p(T_A) = 0 \) if and only if \( p(A) = 0 \), because \( [p(T_A)]_{\sE} = p(A) \) in the standard basis \( \sE \) (@cor-matrix-of-polynomial-of-operator). So \( I_{T_A} = \{ p : p(A) = 0 \} \), and the matrix version is the operator version for \( T_A \).

The name records the second description: \( m_T \) is the annihilating polynomial of minimal degree. The first description is the one we use in proofs, because it hands us a divisibility for free.

::: {#thm-minimal-polynomial-divides}
[Annihilating Polynomials Are Multiples of the Minimal Polynomial]

Let \( V \) be finite-dimensional and \( T \in \cL(V) \). For every \( p \in F[x] \),
\[
p(T) = 0 \iff m_T \mid p .
\]
In particular, a non-zero polynomial that annihilates \( T \) has degree at least \( \deg m_T \). If \( V \ne \{\0\} \), then \( \deg m_T \ge 1 \).
:::

::: {.proof}
By @def-minimal-polynomial, \( p(T) = 0 \) means \( p \in \langle m_T \rangle \), that is, \( p = q\,m_T \) for some \( q \in F[x] \), that is, \( m_T \mid p \). If \( p \ne 0 \) and \( m_T \mid p \), then \( \deg m_T \le \deg p \) by @prp-divisibility-properties (c). Finally, the only monic polynomial of degree \( 0 \) is the constant \( 1 \), and \( 1(T) = \id_V \ne 0 \) when \( V \ne \{\0\} \); so \( m_T \ne 1 \) and \( \deg m_T \ge 1 \).
:::

This is the move we will use again and again: **a polynomial relation becomes a divisibility.** If we learn that \( T^3 = T \), we do not need to know anything else about \( T \) to conclude that \( m_T \mid x^3 - x = x(x - 1)(x + 1) \). That leaves only finitely many candidates for \( m_T \). To list candidates like these we need to know the monic divisors of a factored polynomial, and unique factorization describes them exactly.

::: {#lem-monic-divisors}
[Monic Divisors of a Factored Polynomial]

Let \( f = p_1^{e_1} \cdots p_k^{e_k} \in F[x] \), where \( k \ge 1 \), \( p_1, \dots, p_k \) are **distinct** monic irreducible polynomials and \( e_i \ge 1 \). Then the monic divisors of \( f \) are exactly the polynomials
\[
p_1^{f_1} \cdots p_k^{f_k} \qquad \text{with } 0 \le f_i \le e_i \text{ for each } i .
\]
:::

::: {.idea}
One direction is a product: the missing factors form the cofactor. For the other, factor a monic divisor \( d \) into irreducibles, multiply that factorization by one of the cofactor, and compare the result with the factorization of \( f \). Uniqueness says the two lists of irreducibles agree, so the irreducibles in \( d \) are among the \( p_i \), and none can occur more often in \( d \) than in \( f \).
:::

::: {.proof}
Each such product divides \( f \), with cofactor \( p_1^{e_1 - f_1} \cdots p_k^{e_k - f_k} \). Conversely, let \( d \) be monic with \( f = dh \). If \( d = 1 \), take every \( f_i = 0 \). Otherwise \( d \) is non-constant, and by @thm-unique-factorization-polynomials (a) it is a product \( q_1 \cdots q_s \) of monic irreducibles; the constant in front is the leading coefficient of \( d \), which is \( 1 \). The cofactor \( h \) is non-zero (as \( f \ne 0 \)), so it is either a non-zero constant \( c \) or, by the same theorem, \( c\,r_1 \cdots r_t \) with \( r_j \) monic irreducible. Multiplying, \( f = c\,q_1 \cdots q_s\,r_1 \cdots r_t \) (with no \( r \)'s in the first case) is a factorization of \( f \) into a constant and monic irreducibles. By @thm-unique-factorization-polynomials (b), after renumbering it is the factorization \( f = 1 \cdot p_1^{e_1} \cdots p_k^{e_k} \), in which \( p_i \) occurs exactly \( e_i \) times. So each \( q_j \) is one of the \( p_i \), and \( p_i \) occurs at most \( e_i \) times among \( q_1, \dots, q_s \). Hence \( d = p_1^{f_1} \cdots p_k^{f_k} \) with \( 0 \le f_i \le e_i \).
:::

**Examples.** Each computation follows the same plan: find one annihilating polynomial, list its monic divisors with @lem-monic-divisors, and discard those that do not annihilate.

- **A diagonal matrix with a repeated entry.** Let \( A = \diag(1, 1, 2) \). Diagonal matrices multiply entry by entry, so
  \[
  (A - I)(A - 2I) = \diag(0, 0, 1)\,\diag(-1, -1, 0) = 0 .
  \]
  By @thm-minimal-polynomial-divides, \( m_A \) is a monic divisor of \( (x - 1)(x - 2) \): one of \( 1 \), \( x - 1 \), \( x - 2 \), \( (x - 1)(x - 2) \). None of the first three annihilates \( A \), since \( I \), \( A - I = \diag(0, 0, 1) \) and \( A - 2I = \diag(-1, -1, 0) \) are non-zero. So \( m_A = (x - 1)(x - 2) \). The repeated diagonal entry \( 1 \) appears only **once** in \( m_A \), while the characteristic polynomial is \( p_A = (x - 1)^2(x - 2) \).
- **A matrix with too few eigenvectors.** Let \( J = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) over any field. Then \( J - I = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \ne 0 \), and \( (J - I)^2 = 0 \). So \( m_J \) is a monic divisor of \( (x - 1)^2 \), namely \( 1 \), \( x - 1 \) or \( (x - 1)^2 \), and the first two do not annihilate \( J \). Hence \( m_J = (x - 1)^2 \), which equals \( p_J \).
- **Projections.** Chapter 5 found, by this plan, that a projection \( P \) with \( P \ne 0 \) and \( P \ne \id_V \) has \( m_P = x^2 - x \) (the examples after @thm-annihilator-ideal).
- **Differentiation.** Let \( D \) be differentiation on \( \nR[x]_{\le n} \). Then \( D^{n+1} = 0 \) and \( D^n \ne 0 \) (@exm-differentiation-nilpotent). By @lem-monic-divisors, the monic divisors of \( x^{n+1} \) are the powers \( x^j \) with \( 0 \le j \le n + 1 \). For \( j \le n \), \( D^j \ne 0 \), since \( D^n = D^{n-j}D^j \) would otherwise be \( 0 \). Hence \( m_D = x^{n+1} \), of degree \( n + 1 = \dim \nR[x]_{\le n} \).
- **Degenerate cases.** On \( V \ne \{\0\} \), the identity has \( m = x - 1 \) and the zero operator has \( m = x \): each is killed by a polynomial of degree \( 1 \), which is the least possible degree. More generally \( m_{c\,\id_V} = x - c \), and every \( 1 \times 1 \) matrix \( (c) \) has \( m = x - c \). On \( V = \{\0\} \), even the constant \( 1 \) annihilates, so \( m_T = 1 \). This last case is the reason for the hypothesis \( V \ne \{\0\} \) in @thm-minimal-polynomial-divides.

**Non-example by minimal change.** For \( J \) above, take \( q = x - 1 \) instead of \( (x - 1)^2 \). It is still monic, it has the least degree a minimal polynomial can have on a non-zero space, and its only root is the eigenvalue \( 1 \) of \( J \). What fails is the clause \( q(J) = 0 \): \( q(J) = J - I \ne 0 \). In the other direction, \( (x - 1)^3 \) is monic and does annihilate \( J \), but it fails the clause \( I_J = \langle q \rangle \): the annihilating polynomial \( (x - 1)^2 \) is not a multiple of \( (x - 1)^3 \).

::: {.check}
Find the minimal polynomial of \( 2I_3 \) and of \( N = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} \in M_3(F) \).
:::

::: {.solution}
\( 2I_3 - 2I_3 = 0 \), so \( m_{2I_3} \) divides \( x - 2 \); it is not \( 1 \), since \( I_3 \ne 0 \). Hence \( m_{2I_3} = x - 2 \). For \( N \): \( N\e_1 = \0 \), \( N\e_2 = \e_1 \), \( N\e_3 = \e_2 \), so \( N^2\e_3 = \e_1 \ne \0 \) and \( N^3 \) kills \( \e_1, \e_2, \e_3 \). Thus \( N^3 = 0 \ne N^2 \). By @lem-monic-divisors, \( m_N \in \{1, x, x^2, x^3\} \), and only \( x^3 \) annihilates \( N \) (the others give \( I_3, N, N^2 \ne 0 \)). So \( m_N = x^3 \).
:::

**Why this definition.** Each clause has a job.

- *Monic.* The polynomials \( m \) and \( 5m \) generate the same ideal, so "a generator" is determined only up to a non-zero constant. Insisting on leading coefficient \( 1 \) picks one, and makes statements like "\( m_A = (x - 1)(x - 2) \)" meaningful.
- *Generator, not only least degree.* The two descriptions give the same polynomial. Stating the definition through the ideal puts @thm-minimal-polynomial-divides in front of us, and divisibility is the property we use.
- *Finite dimension.* Without it, \( I_T \) can be \( \{0\} \), and then there is nothing to name. For multiplication by \( x \) on \( F[x] \), \( p(S)(1) = p \), so \( p(S) \ne 0 \) for every \( p \ne 0 \) (the remark after @thm-annihilating-polynomial-exists). The same happens for the right shift on \( F^{\nN} \).

::: {.warning}
**The minimal polynomial is not the characteristic polynomial.** For \( I_2 \), \( m = x - 1 \) while \( p = (x - 1)^2 \); for \( \diag(1, 1, 2) \) above, \( m = (x - 1)(x - 2) \) while \( p = (x - 1)^2(x - 2) \). The two can differ in their exponents, and \( m \) can have smaller degree than the size of the matrix. How they are related is the subject of the next section. Its main theorem is one that Chapter 6 warned against "proving" by substituting \( x = A \) into \( \det(xI - A) \); that shortcut is not a proof and must not be used here either.
:::

## The roots are the eigenvalues

The minimal polynomial is defined by an ideal, and eigenvalues by vectors. They are closely linked.

::: {#thm-minimal-polynomial-roots}
[Roots of the Minimal Polynomial]

Let \( V \) be finite-dimensional, \( T \in \cL(V) \) and \( \lambda \in F \). Then \( m_T(\lambda) = 0 \) if and only if \( \lambda \) is an eigenvalue of \( T \). Consequently, if \( \dim V \ge 1 \), then \( m_T \) and \( p_T \) have the same roots in \( F \).
:::

::: {.idea}
(⇐) is a one-liner: apply \( m_T(T) = 0 \) to an eigenvector \( \v \). Since \( T \) scales \( \v \) by \( \lambda \), every polynomial in \( T \) scales \( \v \) by the value of the polynomial at \( \lambda \). For (⇒), a root gives a factor: \( m_T = (x - \lambda)q \). The cofactor \( q \) has smaller degree, so by minimality it does **not** kill \( T \), and some vector \( \w \) survives it. Then \( q(T)\w \) is non-zero and is killed by \( T - \lambda\,\id_V \). The eigenvector is manufactured by the part of \( m_T \) we removed.
:::

::: {.proof}
(⇐) Let \( \v \ne \0 \) with \( T\v = \lambda\v \). By @exr-eigenvalues-and-eigenvectors-b3 (a), \( p(T)\v = p(\lambda)\v \) for every \( p \in F[x] \). With \( p = m_T \),
\[
\0 = m_T(T)\v = m_T(\lambda)\v .
\]
Since \( \v \ne \0 \), @thm-zero-product gives \( m_T(\lambda) = 0 \).

(⇒) Suppose \( m_T(\lambda) = 0 \). By @thm-remainder-theorem (b), \( m_T = (x - \lambda)q \) for some \( q \in F[x] \), and \( q \) is monic with \( \deg q = \deg m_T - 1 \) by @thm-degree-of-product. By @thm-minimal-polynomial-divides, a non-zero polynomial of degree less than \( \deg m_T \) does not annihilate \( T \); so \( q(T) \ne 0 \), and there is \( \w \in V \) with \( \v \coloneqq q(T)\w \ne \0 \). By @thm-evaluation-homomorphism (b),
\[
(T - \lambda\,\id_V)\v = (T - \lambda\,\id_V)\,q(T)\w = m_T(T)\w = \0 .
\]
So \( T\v = \lambda\v \) with \( \v \ne \0 \), and \( \lambda \) is an eigenvalue of \( T \).

If \( \dim V \ge 1 \), the eigenvalues of \( T \) are exactly the roots of \( p_T \) in \( F \) (@thm-eigenvalue-characterizations, (a) ⇔ (e)), so \( m_T \) and \( p_T \) have the same roots in \( F \). This proves the theorem.
:::

So the minimal polynomial knows the spectrum, just as the characteristic polynomial does, although the multiplicities of the roots may differ. The examples bear this out. \( \diag(1, 1, 2) \) has spectrum \( \{1, 2\} \), the roots of \( (x - 1)(x - 2) \). \( J \) has spectrum \( \{1\} \), the root of \( (x - 1)^2 \). The rotation \( R \) of \( \nR^2 \) by a right angle has \( m_R = x^2 + 1 \) (the check after @thm-annihilator-ideal), with no real root, and indeed \( \spec(R) = \emptyset \) over \( \nR \). Its minimal polynomial has no linear factor at all.

Two consequences are worth stating.

- **Invertibility.** Taking \( \lambda = 0 \): for \( V \ne \{\0\} \), \( T \) is invertible if and only if \( m_T(0) \ne 0 \). Indeed \( m_T(0) = 0 \) if and only if \( 0 \in \spec(T) \), if and only if \( T = T - 0\,\id_V \) is not invertible (@thm-eigenvalue-characterizations, (a) ⇔ (c) with \( \lambda = 0 \); for matrices this is @thm-invertible-tfae-eigen). Chapter 5 proved the same statement without eigenvalues (@exr-polynomials-of-operators-c1 (c)).
- **Over \( \nC \).** If \( F = \nC \) and \( V \ne \{\0\} \), then \( m_T \) splits (@cor-complex-polynomial-splits), and its roots are the distinct eigenvalues \( \lambda_1, \dots, \lambda_k \). So
  \[
  m_T = (x - \lambda_1)^{s_1} \cdots (x - \lambda_k)^{s_k} \qquad \text{with every } s_i \ge 1 .
  \]
  Only the exponents remain to be found.

## Computing the minimal polynomial

There are two practical methods. The first needs nothing but elimination. The second uses the eigenvalues, when we know them, to cut the search down to a few candidates.

**Method 1: the first dependence among powers.** The proof of @thm-annihilating-polynomial-exists searched for a dependence among \( \id_V, T, T^2, \dots \). The **first** dependence that appears gives \( m_T \) exactly.

::: {#prp-minimal-polynomial-first-dependence}
[The First Dependence Among the Powers]

Let \( V \) be finite-dimensional and \( T \in \cL(V) \). Let \( d \ge 0 \) be the **least** integer such that the list \( (\id_V, T, \dots, T^d) \) in \( \cL(V) \) is linearly dependent. Then there are unique \( c_0, \dots, c_{d-1} \in F \) with
\[
T^d = c_0\,\id_V + c_1T + \dots + c_{d-1}T^{d-1},
\]
and \( m_T = x^d - c_{d-1}x^{d-1} - \dots - c_1x - c_0 \). In particular \( \deg m_T = d \). The same holds for \( A \in M_n(F) \), with powers of \( A \) in \( M_n(F) \).
:::

::: {.proof}
Such a \( d \) exists: with \( n = \dim V \), the space \( \cL(V) \) has dimension \( n^2 \) (@thm-linear-maps-isomorphic-to-matrices), so the list \( (\id_V, T, \dots, T^{n^2}) \), of length \( n^2 + 1 \), is linearly dependent (@thm-size-bounds (a)). By minimality of \( d \), the list \( (\id_V, \dots, T^{d-1}) \) is independent (for \( d = 0 \) it is empty). By @lem-append-independent, since appending \( T^d \) makes it dependent, \( T^d \in \Span(\id_V, \dots, T^{d-1}) \). The coefficients are unique by @thm-independence-unique-combination.

Let \( q = x^d - c_{d-1}x^{d-1} - \dots - c_0 \). It is monic, and \( q(T) = 0 \) by the displayed relation. Let \( p \ne 0 \) with \( \deg p < d \). Then \( p(T) = \sum_{k < d} a_kT^k \) with the \( a_k \) not all zero, and this is not \( 0 \) because \( (\id_V, \dots, T^{d-1}) \) is independent. So no non-zero polynomial of degree less than \( d \) annihilates \( T \), and \( q \) is the monic annihilating polynomial of least degree. By @def-minimal-polynomial, \( q = m_T \).
:::

::: {#exm-minimal-polynomial-by-dependence}
[The Minimal Polynomial from the First Dependence]

Find the minimal polynomial of
\[
A = \begin{pmatrix} 3 & 2 & -2 \\ -2 & -1 & 2 \\ -2 & -2 & 3 \end{pmatrix} \in M_3(\nR),
\]
the matrix of @exm-diagonalize-3x3, without using its eigenvalues.
:::

::: {.solution}
*Degree \( 1 \).* \( A \) is not a scalar multiple of \( I_3 \), since its \( (1, 2) \)-entry is non-zero. So \( (I_3, A) \) is independent.

*Degree \( 2 \).* Multiplying out,
\[
A^2 = \begin{pmatrix} 9 & 8 & -8 \\ -8 & -7 & 8 \\ -8 & -8 & 9 \end{pmatrix}.
\]
We look for \( a, b \) with \( A^2 = aA + bI_3 \). The \( (1, 2) \)-entries give \( 8 = 2a \), so \( a = 4 \). The \( (1, 1) \)-entries give \( 9 = 3a + b \), so \( b = -3 \). Now check every entry of \( 4A - 3I_3 \):
\[
4A - 3I_3 = \begin{pmatrix} 12 - 3 & 8 & -8 \\ -8 & -4 - 3 & 8 \\ -8 & -8 & 12 - 3 \end{pmatrix} = \begin{pmatrix} 9 & 8 & -8 \\ -8 & -7 & 8 \\ -8 & -8 & 9 \end{pmatrix} = A^2 .
\]
So \( (I_3, A, A^2) \) is dependent, and \( d = 2 \). By @prp-minimal-polynomial-first-dependence,
\[
m_A = x^2 - 4x + 3 = (x - 1)(x - 3).
\]
This fits @thm-minimal-polynomial-roots: @exm-diagonalize-3x3 found the eigenvalues \( 1 \) and \( 3 \), and \( p_A = (x - 1)^2(x - 3) \). Once again the repeated eigenvalue \( 1 \) appears only once in \( m_A \). Section 8 explains that this is exactly why \( A \) was diagonalizable.
:::

**Method 2: eigenvalues and trial exponents.** Suppose \( p_T \) splits, \( p_T = (x - \lambda_1)^{a_1} \cdots (x - \lambda_k)^{a_k} \) with distinct \( \lambda_i \). By @thm-minimal-polynomial-roots, every \( x - \lambda_i \) divides \( m_T \). If we find **any** annihilating polynomial of the form \( q = (x - \lambda_1)^{t_1} \cdots (x - \lambda_k)^{t_k} \), then \( m_T \mid q \). By @lem-monic-divisors, \( m_T = (x - \lambda_1)^{s_1} \cdots (x - \lambda_k)^{s_k} \) with \( 1 \le s_i \le t_i \), so only finitely many candidates remain, and we test them from the smallest degree up. The next section proves that \( q = p_T \) always annihilates \( T \), so the search always succeeds with \( t_i \le a_i \). Here we verify that directly.

::: {#exm-minimal-polynomial-by-eigenvalues}
[The Minimal Polynomial from the Eigenvalues]

Let \( A = \begin{pmatrix} 2 & 0 & 1 \\ 1 & 3 & 1 \\ 1 & 0 & 2 \end{pmatrix} \in M_3(\nR) \), with \( p_A = (x - 1)(x - 3)^2 \) (@exm-charpoly-small). Find \( m_A \).
:::

::: {.solution}
By @thm-minimal-polynomial-roots, both \( x - 1 \) and \( x - 3 \) divide \( m_A \), so the candidate of least degree is \( (x - 1)(x - 3) \). With
\[
A - I = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 2 & 1 \\ 1 & 0 & 1 \end{pmatrix}, \qquad A - 3I = \begin{pmatrix} -1 & 0 & 1 \\ 1 & 0 & 1 \\ 1 & 0 & -1 \end{pmatrix},
\]
the product is
\[
(A - I)(A - 3I) = \begin{pmatrix} 0 & 0 & 0 \\ 2 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix} \ne 0 .
\]
So \( m_A \ne (x - 1)(x - 3) \). Raise one exponent and try \( (x - 1)(x - 3)^2 \) (had this failed, the other candidate of degree \( 3 \), namely \( (x - 1)^2(x - 3) \), would come next). Polynomials in \( A \) commute (@thm-evaluation-homomorphism (c)), so we can multiply the matrix just found by \( A - 3I \) on the right:
\[
(A - I)(A - 3I)^2 = \begin{pmatrix} 0 & 0 & 0 \\ 2 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix}\begin{pmatrix} -1 & 0 & 1 \\ 1 & 0 & 1 \\ 1 & 0 & -1 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 0 \\ -2 + 2 & 0 & 2 - 2 \\ 0 & 0 & 0 \end{pmatrix} = 0 .
\]
So \( m_A \mid (x - 1)(x - 3)^2 \), and by @lem-monic-divisors, \( m_A = (x - 1)^{s}(x - 3)^{t} \) with \( 1 \le s \le 1 \) and \( 1 \le t \le 2 \). The case \( t = 1 \) was excluded, so
\[
m_A = (x - 1)(x - 3)^2 = p_A .
\]
In Section 3 we found \( g(3) = 1 < 2 = a(3) \) for this matrix. The exponent \( 2 \) of \( x - 3 \) in \( m_A \) is the polynomial trace of the same shortage of eigenvectors.
:::

The product in Method 2 need not be multiplied out completely: to rule out a candidate it is enough to find **one** non-zero entry, and to confirm one, the factored form usually makes the zero visible.

## Similar matrices and block diagonal matrices

The minimal polynomial belongs to the operator, not to a basis. That is what makes it an invariant of similarity.

::: {#thm-minimal-polynomial-similarity}
[Similar Matrices Have the Same Minimal Polynomial]

Let \( V \) be finite-dimensional with a basis \( \sB \), and let \( T \in \cL(V) \). Then \( m_T = m_{[T]_{\sB}} \). If \( A, B \in M_n(F) \) are similar, then \( m_A = m_B \).
:::

::: {.proof}
By @cor-matrix-of-polynomial-of-operator, \( [p(T)]_{\sB} = p([T]_{\sB}) \) for every \( p \in F[x] \). An operator is zero exactly when its matrix is zero (@thm-linear-maps-isomorphic-to-matrices), so \( p(T) = 0 \) if and only if \( p([T]_{\sB}) = 0 \). Thus \( T \) and \( [T]_{\sB} \) have the same ideal of annihilating polynomials, and hence the same monic generator. If \( B = P^{-1}AP \), then \( p(B) = P^{-1}p(A)P \) by @prp-similarity-invariants (c), so again \( p(A) = 0 \) if and only if \( p(B) = 0 \), and \( m_A = m_B \).
:::

The theorem gives a quick non-similarity test. For instance \( I_2 \) and \( J = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) have the same characteristic polynomial, but \( m_{I_2} = x - 1 \ne (x - 1)^2 = m_J \), so they are not similar.

Chapter 7 showed that a block diagonal matrix computes polynomials blockwise: \( p(A \oplus B) = p(A) \oplus p(B) \) (@thm-block-diagonal-arithmetic (b)). So a polynomial kills \( A \oplus B \) exactly when it kills both blocks. In the language of ideals, the answer is the least common multiple.

::: {#prp-minimal-polynomial-block-diagonal}
[Minimal Polynomial of a Block Diagonal Matrix]

Let \( A \in M_k(F) \) and \( B \in M_l(F) \) with \( k, l \ge 1 \). Then \( m_{A \oplus B} = \operatorname{lcm}(m_A, m_B) \).
:::

::: {.proof}
Let \( p \in F[x] \). By @thm-block-diagonal-arithmetic (b), \( p(A \oplus B) = p(A) \oplus p(B) \), which is zero if and only if \( p(A) = 0 \) and \( p(B) = 0 \). By @thm-minimal-polynomial-divides, this holds if and only if \( p \in \langle m_A \rangle \cap \langle m_B \rangle \). So \( I_{A \oplus B} = \langle m_A \rangle \cap \langle m_B \rangle \). This ideal contains \( m_{A \oplus B} \ne 0 \), and by @def-lcm-polynomials its monic generator is \( \operatorname{lcm}(m_A, m_B) \). By @def-minimal-polynomial its monic generator is also \( m_{A \oplus B} \), and the monic generator is unique (@thm-ideals-principal).
:::

For example, \( \diag(1, 1, 2) = I_2 \oplus (2) \) has \( m = \operatorname{lcm}(x - 1, x - 2) = (x - 1)(x - 2) \), as computed above. And \( J \oplus (1) \) has \( m = \operatorname{lcm}\big((x - 1)^2, x - 1\big) = (x - 1)^2 \): a block can contribute a factor that the other block already contains, and then the factor is not repeated. This is the difference from the characteristic polynomial, which multiplies: \( p_{A \oplus B} = p_A\,p_B \).

::: {.warning}
**Equal minimal polynomials do not make matrices similar.** \( \diag(1, 1, 2) \) and \( \diag(1, 2, 2) \) both have minimal polynomial \( (x - 1)(x - 2) \), by @prp-minimal-polynomial-block-diagonal. But their characteristic polynomials \( (x - 1)^2(x - 2) \) and \( (x - 1)(x - 2)^2 \) differ, so they are not similar (@thm-charpoly-similarity-invariant).
:::

::: {.remark}
Even the minimal and characteristic polynomials **together** do not decide similarity. With \( J = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \), the matrices \( J \oplus J \) and \( J \oplus I_2 \) in \( M_4(F) \) both have characteristic polynomial \( (x - 1)^4 \) and, by @prp-minimal-polynomial-block-diagonal, minimal polynomial \( (x - 1)^2 \), as \( \operatorname{lcm}\big((x - 1)^2, (x - 1)^2\big) \) and \( \operatorname{lcm}\big((x - 1)^2, x - 1\big) \) are both \( (x - 1)^2 \). Yet \( (J \oplus J) - I_4 \) has rank \( 2 \) and \( (J \oplus I_2) - I_4 \) has rank \( 1 \); if \( B = P^{-1}AP \), then \( B - I = P^{-1}(A - I)P \), so these ranks would have to agree (@prp-similarity-invariants (a)), and the two matrices are not similar. The invariant that does decide similarity is the subject of Chapter 9.
:::

## Exercises

### A. Check your understanding

:::: {#exr-minimal-polynomial-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the minimal polynomial of an operator \( T \) on a finite-dimensional space, and give its two equivalent descriptions.
2. True or false: \( m_A = p_A \) for every \( A \in M_n(F) \). Justify your answer.
3. State the relation between the roots of \( m_T \) and the eigenvalues of \( T \).
4. Let \( A \ne 0 \) satisfy \( A^3 = 0 \). Which polynomials can \( m_A \) be?
5. True or false: if \( m_A = m_B \), then \( A \sim B \). Justify your answer.
6. Explain why multiplication by \( x \) on \( F[x] \) has no minimal polynomial.
:::
::::

::: {.solution}
(a) \( m_T \) is the unique monic polynomial with \( \{ p : p(T) = 0 \} = \langle m_T \rangle \); equivalently, the monic polynomial of least degree with \( m_T(T) = 0 \) (@def-minimal-polynomial).

(b) False. For \( I_2 \), \( m = x - 1 \) and \( p = (x - 1)^2 \).

(c) They coincide: \( m_T(\lambda) = 0 \) if and only if \( \lambda \) is an eigenvalue of \( T \) (@thm-minimal-polynomial-roots).

(d) By @thm-minimal-polynomial-divides, \( m_A \mid x^3 \), so \( m_A \in \{1, x, x^2, x^3\} \) by @lem-monic-divisors. It is not \( 1 \) (as \( I \ne 0 \)) and not \( x \) (as \( A \ne 0 \)). So \( m_A = x^2 \) or \( m_A = x^3 \), and both occur: \( \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) and the matrix \( N \) of the Quick check.

(e) False. \( \diag(1, 1, 2) \) and \( \diag(1, 2, 2) \) have the same minimal polynomial but different characteristic polynomials.

(f) For \( S(f) = xf \), we have \( p(S)(1) = p \), so \( p(S) \ne 0 \) for all \( p \ne 0 \). The ideal \( I_S \) is \( \{0\} \) and has no monic generator. The space \( F[x] \) is infinite-dimensional, so the definition does not apply.
:::

### B. Practice

:::: {#exr-minimal-polynomial-b1}
[B1: Computing minimal polynomials]

Find the minimal polynomial of each real matrix.

::: {.enumerate options="label=(\alph*)"}
1. \( A_1 = \begin{pmatrix} 4 & -1 \\ 1 & 2 \end{pmatrix} \).
2. \( A_2 = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix} \).
3. \( A_3 = \begin{pmatrix} 2 & 1 & 1 \\ 0 & 1 & -1 \\ -1 & -1 & 1 \end{pmatrix} \), given that \( p_{A_3} = (x - 1)^2(x - 2) \).
4. \( A_4 = \begin{pmatrix} 2 & 1 & 1 \\ -1 & 0 & -1 \\ 1 & 1 & 2 \end{pmatrix} \), given that \( p_{A_4} = (x - 1)^2(x - 2) \).
:::

Hence decide whether \( A_3 \) and \( A_4 \) are similar.
::::

::: {.solution}
(a) \( A_1 \) is not scalar, so \( \deg m_{A_1} \ge 2 \). Here \( \tr A_1 = 6 \) and \( \det A_1 = 9 \), and \( A_1^2 = \begin{pmatrix} 15 & -6 \\ 6 & 3 \end{pmatrix} = 6A_1 - 9I_2 \), as one checks entry by entry. By @prp-minimal-polynomial-first-dependence, \( m_{A_1} = x^2 - 6x + 9 = (x - 3)^2 \).

(b) \( A_2 \) is not scalar. Every entry of \( A_2^2 \) is \( 1 + 1 + 1 = 3 \), so \( A_2^2 = 3A_2 \). By @prp-minimal-polynomial-first-dependence, \( m_{A_2} = x^2 - 3x = x(x - 3) \).

(c) By @thm-minimal-polynomial-roots, \( (x - 1)(x - 2) \mid m_{A_3} \). First candidate:
\[
(A_3 - I)(A_3 - 2I) = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 0 & -1 \\ -1 & -1 & 0 \end{pmatrix}\begin{pmatrix} 0 & 1 & 1 \\ 0 & -1 & -1 \\ -1 & -1 & -1 \end{pmatrix} = \begin{pmatrix} -1 & -1 & -1 \\ 1 & 1 & 1 \\ 0 & 0 & 0 \end{pmatrix} \ne 0 .
\]
Next candidate: multiplying this on the left by \( A_3 - I \), the rows of the result are \( (1, 1, 1)M \), \( (0, 0, -1)M \) and \( (-1, -1, 0)M \), where \( M \) is the matrix just found. Since the rows of \( M \) sum to zero and its third row is zero, all three products are \( \0 \). So \( (A_3 - I)^2(A_3 - 2I) = 0 \), and by @lem-monic-divisors, \( m_{A_3} = (x - 1)^2(x - 2) \).

(d) Again \( (x - 1)(x - 2) \mid m_{A_4} \), and
\[
(A_4 - I)(A_4 - 2I) = \begin{pmatrix} 1 & 1 & 1 \\ -1 & -1 & -1 \\ 1 & 1 & 1 \end{pmatrix}\begin{pmatrix} 0 & 1 & 1 \\ -1 & -2 & -1 \\ 1 & 1 & 0 \end{pmatrix} = 0,
\]
since each column of the second matrix has entries summing to \( 0 \) and each row of the first is a multiple of \( (1, 1, 1) \). So \( m_{A_4} = (x - 1)(x - 2) \).

Hence \( m_{A_3} \ne m_{A_4} \), and by @thm-minimal-polynomial-similarity \( A_3 \) and \( A_4 \) are **not** similar, although their characteristic polynomials agree. (This matches @exr-multiplicities-b1, where the same two matrices appear as \( A_2 \) and \( A_3 \), with \( g(1) = 1 \) for the first and \( g(1) = 2 \) for the second.)
:::

:::: {#exr-minimal-polynomial-b2}
[B2: Operators with \( T^2 = T \)]

Let \( V \ne \{\0\} \) be finite-dimensional and \( T \in \cL(V) \) with \( T^2 = T \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( m_T \in \{ x,\ x - 1,\ x(x - 1) \} \).
2. Show that \( m_T = x \) exactly when \( T = 0 \), and \( m_T = x - 1 \) exactly when \( T = \id_V \).
3. What is \( m_T \) on \( V = \{\0\} \)?
:::
::::

::: {.solution}
(a) \( x^2 - x = x(x - 1) \) annihilates \( T \), so \( m_T \mid x(x - 1) \) by @thm-minimal-polynomial-divides. By @lem-monic-divisors, the monic divisors are \( 1, x, x - 1, x(x - 1) \). Since \( V \ne \{\0\} \), \( \deg m_T \ge 1 \), so \( m_T \ne 1 \).

(b) If \( m_T = x \), then \( T = m_T(T) = 0 \). Conversely, if \( T = 0 \), then \( x \) annihilates \( T \), so \( m_T \mid x \), and \( m_T = x \) by (a). Likewise \( m_T = x - 1 \) if and only if \( T - \id_V = 0 \). In all other cases \( m_T = x(x - 1) \).

(c) On \( V = \{\0\} \), \( 1(T) = \id_V = 0 \), so \( m_T = 1 \).
:::

:::: {#exr-minimal-polynomial-b3}
[B3: Companion matrices]

Let \( n \ge 2 \), \( p = x^n + a_{n-1}x^{n-1} + \dots + a_1x + a_0 \in F[x] \), and let \( C = C(p) \) be its companion matrix (@exr-characteristic-polynomial-c1).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( C\e_k = \e_{k+1} \) for \( 1 \le k \le n - 1 \), so \( C^k\e_1 = \e_{k+1} \) for \( 0 \le k \le n - 1 \).
2. Deduce that no non-zero polynomial of degree less than \( n \) annihilates \( C \).
3. Show that \( p(C)\e_1 = \0 \), and hence \( p(C)\e_{k+1} = \0 \) for all \( k \le n - 1 \).
4. Deduce that \( m_C = p = p_C \).
:::
::::

::: {.solution}
(a) Column \( k \) of \( C \), for \( k \le n - 1 \), has a single \( 1 \) in row \( k + 1 \), so \( C\e_k = \e_{k+1} \). By induction on \( k \), \( C^k\e_1 = C(C^{k-1}\e_1) = C\e_k = \e_{k+1} \).

(b) Let \( q = \sum_{k=0}^{d} b_kx^k \ne 0 \) with \( d \le n - 1 \). By (a), \( q(C)\e_1 = \sum_k b_kC^k\e_1 = \sum_k b_k\e_{k+1} \), which is not \( \0 \) because some \( b_k \ne 0 \). So \( q(C) \ne 0 \).

(c) By (a), \( C^n\e_1 = C\e_n \), the last column \( (-a_0, \dots, -a_{n-1}) = -\sum_{k=0}^{n-1} a_k\e_{k+1} \). Hence
\[
p(C)\e_1 = C^n\e_1 + \sum_{k=0}^{n-1} a_kC^k\e_1 = -\sum_k a_k\e_{k+1} + \sum_k a_k\e_{k+1} = \0 .
\]
For \( k \le n - 1 \), polynomials in \( C \) commute (@thm-evaluation-homomorphism (c)), so \( p(C)\e_{k+1} = p(C)C^k\e_1 = C^kp(C)\e_1 = \0 \).

(d) By (c), \( p(C) \) kills the standard basis, so \( p(C) = 0 \) and \( m_C \mid p \). By (b), \( \deg m_C \ge n = \deg p \). Two monic polynomials, one dividing the other, with \( \deg m_C \ge \deg p \), are equal (@prp-divisibility-properties (c), (d)). So \( m_C = p \), and \( p = p_C \) by @exr-characteristic-polynomial-c1 (b). Every monic polynomial of degree \( n \ge 2 \) is therefore the minimal polynomial of some \( n \times n \) matrix.
:::

### C. Going deeper

:::: {#exr-minimal-polynomial-c1}
[C1: Cyclic vectors]

Let \( \dim V = n \ge 1 \) and \( T \in \cL(V) \). A vector \( \v \) is a **cyclic vector** for \( T \) if \( (\v, T\v, \dots, T^{n-1}\v) \) is a basis of \( V \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( T \) has a cyclic vector, then \( \deg m_T \ge n \).
2. Suppose \( \v \) is cyclic and \( T^n\v = -(a_0\v + a_1T\v + \dots + a_{n-1}T^{n-1}\v) \). Show that the matrix of \( T \) in the basis \( (\v, \dots, T^{n-1}\v) \) is the companion matrix of \( p = x^n + a_{n-1}x^{n-1} + \dots + a_0 \) (for \( n \ge 2 \)), and deduce \( m_T = p_T = p \).
3. Find a cyclic vector for \( J = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \), and show that \( I_2 \) has none.
:::

(The converse of (a), that \( \deg m_T = n \) forces a cyclic vector, is proved in Chapter 9.)
::::

::: {.solution}
(a) Let \( q = \sum_{k=0}^{d} b_kx^k \ne 0 \) with \( d \le n - 1 \). Then \( q(T)\v = \sum_k b_kT^k\v \ne \0 \), because the vectors \( T^k\v \), \( k \le n - 1 \), are independent and some \( b_k \ne 0 \). So \( q(T) \ne 0 \), and by @thm-minimal-polynomial-divides, \( \deg m_T \ge n \).

(b) Let \( \sB = (\v, T\v, \dots, T^{n-1}\v) \). For \( k \le n - 2 \), \( T(T^k\v) = T^{k+1}\v \), the \( (k + 2) \)-th basis vector, so column \( k + 1 \) of \( [T]_{\sB} \) is \( \e_{k+2} \). The last column is \( \coord{T^n\v}{\sB} = (-a_0, \dots, -a_{n-1}) \). This is \( C(p) \). By @thm-minimal-polynomial-similarity and @exr-minimal-polynomial-b3 (d), \( m_T = m_{C(p)} = p \). By @def-charpoly-operator and @exr-characteristic-polynomial-c1 (b), \( p_T = p_{C(p)} = p \). (For \( n = 1 \), \( T\v = -a_0\v \) and \( T = -a_0\,\id_V \), so \( m_T = p_T = x + a_0 \) directly.)

(c) \( J\e_2 = (1, 1) \), and \( (\e_2, (1, 1)) \) is independent, so \( \e_2 \) is cyclic. For \( I_2 \), every \( \v \) has \( I_2\v = \v \), so \( (\v, I_2\v) \) is dependent. This matches (a): \( \deg m_{I_2} = 1 < 2 \).
:::

:::: {#exr-minimal-polynomial-c2}
[C2: Minimal polynomials of the pieces]

Let \( V \) be finite-dimensional, \( T \in \cL(V) \), and \( U \) a \( T \)-invariant subspace, with restriction \( T|_U \) and induced operator \( \bar T \) on \( V/U \) (@def-restriction-operator).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( p(T|_U) = p(T)|_U \) and \( p(\bar T)(\v + U) = p(T)\v + U \) for every \( p \in F[x] \).
2. Deduce that \( m_{T|_U} \mid m_T \) and \( m_{\bar T} \mid m_T \).
3. Prove that \( m_T \mid m_{T|_U}\,m_{\bar T} \).
4. For \( J = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) and \( U = \Span(\e_1) \), compute all three minimal polynomials, and show that \( m_T \) need not equal \( \operatorname{lcm}(m_{T|_U}, m_{\bar T}) \).
:::

*Hint: for (c), apply \( m_{\bar T}(T) \) to \( \v \) and ask where the result lies.*
::::

::: {.solution}
(a) First, \( (T|_U)^k = T^k|_U \) by induction on \( k \): for \( \u \in U \), \( (T|_U)^{k+1}\u = T|_U\big((T|_U)^k\u\big) = T(T^k\u) = T^{k+1}\u \). Taking linear combinations, \( p(T|_U)\u = p(T)\u \). For the quotient, \( \bar T^k(\v + U) = T^k\v + U \) by the same induction, using @def-restriction-operator (b) at each step, and \( p(\bar T)(\v + U) = \sum_k c_k(T^k\v + U) = p(T)\v + U \) by the coset operations (@thm-quotient-space-operations-well-defined).

(b) By (a), \( m_T(T|_U) = m_T(T)|_U = 0 \) and \( m_T(\bar T)(\v + U) = \0 + U \) for all \( \v \). By @thm-minimal-polynomial-divides, applied to \( T|_U \in \cL(U) \) and to \( \bar T \in \cL(V/U) \), both finite-dimensional, \( m_{T|_U} \mid m_T \) and \( m_{\bar T} \mid m_T \).

(c) Let \( \v \in V \). By (a), \( m_{\bar T}(T)\v + U = m_{\bar T}(\bar T)(\v + U) = \0 + U \), so \( \u \coloneqq m_{\bar T}(T)\v \in U \). By (a) again, \( m_{T|_U}(T)\u = m_{T|_U}(T|_U)\u = \0 \). Hence \( (m_{T|_U}\,m_{\bar T})(T)\v = m_{T|_U}(T)\,m_{\bar T}(T)\v = \0 \) (@thm-evaluation-homomorphism (b)). As \( \v \) was arbitrary, \( m_{T|_U}m_{\bar T} \) annihilates \( T \), and \( m_T \mid m_{T|_U}m_{\bar T} \) by @thm-minimal-polynomial-divides.

(d) \( J\e_1 = \e_1 \), so \( T|_U = \id_U \) and \( m_{T|_U} = x - 1 \). The quotient \( F^2/U \) has basis \( \e_2 + U \), and \( \bar T(\e_2 + U) = (1, 1) + U = \e_2 + U \), so \( \bar T = \id \) and \( m_{\bar T} = x - 1 \). But \( m_J = (x - 1)^2 \), computed earlier. So \( m_J = m_{T|_U}m_{\bar T} \), while \( \operatorname{lcm}(m_{T|_U}, m_{\bar T}) = x - 1 \ne m_J \). Compare @prp-minimal-polynomial-block-diagonal: when \( U \) has an invariant complement the lcm is right, but in general it is not.
:::
