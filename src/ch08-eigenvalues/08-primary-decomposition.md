# Primary Decomposition

Chapter 5 ended with a lemma about any polynomial that kills an operator: if it factors into coprime pieces, the space splits into the kernels of the pieces. The previous sections produced the best polynomial to feed it, the minimal polynomial, which factors into powers of distinct irreducibles. This section runs the lemma on that factorization. The result, the primary decomposition, cuts \( V \) into invariant pieces, one for each irreducible factor of \( m_T \), and on each piece the operator has a minimal polynomial that is a single prime power. Two answers follow at once. An operator is diagonalizable exactly when its minimal polynomial is a product of distinct linear factors. And every complex matrix with \( \A^k = \I \) is diagonalizable, a promise from Section 4. Finally, when \( m_T \) splits, the pieces are the spaces on which Chapter 9 builds the Jordan form.

## Splitting the space along the minimal polynomial

Here is the question. Diagonalization splits \( V \) into eigenspaces, and it can fail. What splitting survives for **every** operator? The minimal polynomial suggests one. By @thm-unique-factorization-polynomials, if \( V \ne \{\0\} \), then \( m_T \) (monic, of degree at least \( 1 \) by @thm-minimal-polynomial-divides) factors as
\[
m_T = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k},
\]
with \( p_1, \dots, p_k \) **distinct** monic irreducible polynomials and exponents \( e_i \ge 1 \). Powers of distinct irreducibles have no common factor, so the kernel splitting lemma of Chapter 5, in its form with \( k \) factors (@exr-polynomials-of-operators-c2), applies to them. It gives a direct sum. The new information is what happens on the pieces.

*The primary decomposition splits \( V \) into one invariant piece for each irreducible factor of \( m_T \), and on that piece the operator is killed by exactly that factor's power.*

::: {#thm-primary-decomposition}
[Primary Decomposition Theorem]

Let \( V \ne \{\0\} \) be a finite-dimensional vector space over \( F \), let \( T \in \cL(V) \), and let \( m_T = p_1^{e_1} \cdots p_k^{e_k} \), where \( p_1, \dots, p_k \) are distinct monic irreducible polynomials and \( e_i \ge 1 \). Put
\[
V_i \coloneqq \ker p_i(T)^{e_i} \qquad (i = 1, \dots, k).
\]
Then:

::: {.enumerate options="label=(\alph*)"}
1. \( V = V_1 \oplus V_2 \oplus \dots \oplus V_k \);
2. each \( V_i \) is \( T \)-invariant and non-zero;
3. the restriction \( T|_{V_i} \) has minimal polynomial \( m_{T|_{V_i}} = p_i^{e_i} \);
4. for each \( i \) there is \( h_i \in F[x] \) such that \( h_i(T) \) is the projection of \( V \) onto \( V_i \) along \( \bigoplus_{j \ne i} V_j \).
:::
:::

In words: (a) every vector is **uniquely** a sum of pieces, one from each \( V_i \). (b) \( T \) maps each piece into itself, so \( T \) is determined by the \( k \) restrictions, and in a basis made of bases of the \( V_i \) its matrix is block diagonal (@thm-direct-sum-invariant-block-diagonal). (c) Nothing is wasted: on \( V_i \) the operator is killed by \( p_i^{e_i} \), and by no proper divisor of it. (d) The pieces can be computed with polynomials in \( T \) alone. The word *primary* refers to the prime powers \( p_i^{e_i} \).

::: {.idea}
① The splitting is Chapter 5's lemma: distinct irreducible powers are pairwise coprime, and their product \( m_T \) kills \( T \). ② Invariance holds for every kernel of a polynomial in \( T \). ③ For (c), each restriction is killed by \( p_i^{e_i} \), so its minimal polynomial is some \( p_i^{f_i} \) with \( f_i \le e_i \). Conversely, the product of these minimal polynomials kills \( T \) piece by piece, hence on all of \( V \), so it is a multiple of \( m_T \). A degree count then forces \( f_i = e_i \).
:::

::: {.proof}
*Coprime.* Let \( i \ne j \) and \( d = \gcd(p_i^{e_i}, p_j^{e_j}) \), which is monic. By @lem-monic-divisors, \( d = p_i^{f} \) and \( d = p_j^{g} \) for some \( f, g \ge 0 \). By the uniqueness in @thm-unique-factorization-polynomials, and since \( p_i \ne p_j \), this forces \( f = g = 0 \), so \( d = 1 \).

(a) and (d). If \( k = 1 \), then \( V_1 = \ker m_T(T) = V \) and \( h_1 = 1 \) works. If \( k \ge 2 \), apply @exr-polynomials-of-operators-c2 (d) to the pairwise coprime polynomials \( p_1^{e_1}, \dots, p_k^{e_k} \), whose product \( m_T \) annihilates \( T \). It gives \( V = V_1 \oplus \dots \oplus V_k \), with the projections given by polynomials \( h_i(T) \).

(b) Each \( V_i \) is the kernel of a polynomial in \( T \), so it is \( T \)-invariant by @thm-kernel-image-of-polynomial-invariant (b). That \( V_i \ne \{\0\} \) will follow from (c): the minimal polynomial of an operator on the zero space is \( 1 \), and \( p_i^{e_i} \ne 1 \).

(c) Let \( q_i = m_{T|_{V_i}} \). By @exr-minimal-polynomial-c2 (a), \( p_i^{e_i}(T|_{V_i}) = p_i^{e_i}(T)|_{V_i} = 0 \), so \( q_i \mid p_i^{e_i} \) (@thm-minimal-polynomial-divides), and \( q_i = p_i^{f_i} \) with \( 0 \le f_i \le e_i \) by @lem-monic-divisors. Put \( q = q_1 \cdots q_k \). For \( \v_i \in V_i \), polynomials in \( T \) commute (@thm-evaluation-homomorphism (c)), so
\[
q(T)\v_i = \Big(\prod_{j \ne i} q_j\Big)(T)\; q_i(T)\v_i = \Big(\prod_{j \ne i} q_j\Big)(T)\; q_i(T|_{V_i})\v_i = \0 ,
\]
using @exr-minimal-polynomial-c2 (a) again. By (a), every \( \v \in V \) is a sum of such \( \v_i \), so \( q(T) = 0 \), and \( m_T \mid q \) by @thm-minimal-polynomial-divides. Comparing degrees (@prp-divisibility-properties (c), @thm-degree-of-product),
\[
\sum_{i=1}^{k} e_i \deg p_i = \deg m_T \le \deg q = \sum_{i=1}^{k} f_i \deg p_i .
\]
Since \( f_i \le e_i \) and \( \deg p_i \ge 1 \) for every \( i \), each term on the right is at most the matching term on the left, so equality holds term by term, and \( f_i = e_i \). Hence \( m_{T|_{V_i}} = p_i^{e_i} \). This proves the theorem.
:::

The theorem reduces the study of \( T \) to the study of operators whose minimal polynomial is a power of **one** irreducible. For a matrix, choose a basis of each \( V_i \) and put them together: \( \A \) is similar to a block diagonal matrix \( \A_1 \oplus \dots \oplus \A_k \) with \( m_{\A_i} = p_i^{e_i} \), and then \( m_{\A} = \operatorname{lcm}(m_{\A_1}, \dots, m_{\A_k}) \) by @prp-minimal-polynomial-block-diagonal, applied \( k - 1 \) times, consistent with (c).

::: {#exm-primary-decomposition}
[A Primary Decomposition with an Irreducible Quadratic]

Let \( \C = \begin{pmatrix} 0 & 0 & 2 \\ 1 & 0 & -1 \\ 0 & 1 & 2 \end{pmatrix} \in M_3(\nR) \). Chapter 5 showed that its minimal polynomial is \( m_{\C} = (x - 2)(x^2 + 1) \) (@exr-polynomials-of-operators-b2). Find the primary decomposition of \( \nR^3 \), the projections as polynomials in \( \C \), and the matrix of \( \C \) in an adapted basis.
:::

::: {.solution}
*The factorization.* \( x - 2 \) is irreducible (degree \( 1 \)), and \( x^2 + 1 \) is irreducible over \( \nR \) because it has no real root (@thm-irreducible-deg-2-3 (b)). So \( k = 2 \), \( p_1 = x - 2 \), \( p_2 = x^2 + 1 \), \( e_1 = e_2 = 1 \).

*The pieces.* \( V_1 = \ker(\C - 2\I) \): the matrix \( \C - 2\I = \begin{pmatrix} -2 & 0 & 2 \\ 1 & -2 & -1 \\ 0 & 1 & 0 \end{pmatrix} \) gives \( y = 0 \) and \( x = z \), so \( V_1 = \Span((1, 0, 1)) \). For \( V_2 = \ker(\C^2 + \I) \), multiply out:
\[
\C^2 = \begin{pmatrix} 0 & 2 & 4 \\ 0 & -1 & 0 \\ 1 & 2 & 3 \end{pmatrix}, \qquad \C^2 + \I = \begin{pmatrix} 1 & 2 & 4 \\ 0 & 0 & 0 \\ 1 & 2 & 4 \end{pmatrix}.
\]
So \( V_2 \) is the plane \( x + 2y + 4z = 0 \), with basis \( (-2, 1, 0) \), \( (-4, 0, 1) \). As the theorem predicts, \( \dim V_1 + \dim V_2 = 3 \), and \( (1, 0, 1) \notin V_2 \) since \( 1 + 0 + 4 \ne 0 \).

*The projections.* Bézout's identity for \( p_1, p_2 \): since \( x^2 + 1 = (x + 2)(x - 2) + 5 \),
\[
\tfrac15(x^2 + 1) - \tfrac15(x + 2)(x - 2) = 1 .
\]
Following @thm-kernel-splitting (c) with \( p = x - 2 \), \( q = x^2 + 1 \), \( a = -\tfrac15(x + 2) \) and \( b = \tfrac15 \), the projection onto \( V_1 \) along \( V_2 \) is \( h_1(\C) = b(\C)q(\C) = \tfrac15(\C^2 + \I) \), and the projection onto \( V_2 \) along \( V_1 \) is \( h_2(\C) = \I - h_1(\C) \). Concretely,
\[
h_1(\C)\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \frac{x + 2y + 4z}{5}\begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix},
\]
which lies in \( V_1 \), is \( \0 \) on \( V_2 \), and fixes \( (1, 0, 1) \).

*The adapted basis.* \( \C(1, 0, 1) = (2, 0, 2) \). On \( V_2 \), \( \C(-2, 1, 0) = (0, -2, 1) = -2(-2, 1, 0) + (-4, 0, 1) \) and \( \C(-4, 0, 1) = (2, -5, 2) = -5(-2, 1, 0) + 2(-4, 0, 1) \). So in the basis \( \big((1, 0, 1), (-2, 1, 0), (-4, 0, 1)\big) \),
\[
[\C] = (2) \oplus \begin{pmatrix} -2 & -5 \\ 1 & 2 \end{pmatrix}.
\]
The second block has trace \( 0 \) and determinant \( -4 + 5 = 1 \), so its characteristic polynomial is \( x^2 + 1 \); it is not a scalar matrix, so its minimal polynomial is also \( x^2 + 1 \), as (c) says. Over \( \nR \), no further splitting of \( V_2 \) is possible, since \( \C \) has no eigenvector in \( V_2 \). Over \( \nC \), the factor \( x^2 + 1 = (x - i)(x + i) \) splits, and so does the plane.
:::

::: {.warning}
**The pieces are kernels of the powers \( p_i^{e_i} \), not of the \( p_i \).** Replacing \( \ker p_i(T)^{e_i} \) by \( \ker p_i(T) \) can lose most of the space. For \( \J = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \), \( m_{\J} = (x - 1)^2 \), and the primary decomposition has the single piece \( \ker(\J - \I)^2 = F^2 \); but \( \ker(\J - \I) = \Span(\e_1) \) is only a line. The sum of the kernels \( \ker p_i(T) \) is still direct, but it equals \( V \) only when every \( e_i = 1 \), which is the subject of the next subsection.
:::

::: {.check}
Let \( T \in \cL(V) \), \( V \ne \{\0\} \) finite-dimensional over \( \nQ \), satisfy \( T^3 = T^2 \) but \( T^2 \ne T \). Which polynomials can \( m_T \) be? What are the pieces of the primary decomposition?
:::

::: {.solution}
\( x^3 - x^2 = x^2(x - 1) \) annihilates \( T \), so by @lem-monic-divisors \( m_T = x^a(x - 1)^b \) with \( a \le 2 \), \( b \le 1 \), not both \( 0 \). Since \( x(x - 1) \) does not annihilate \( T \), and neither do its divisors \( x \) and \( x - 1 \) (they would give \( T = 0 \) or \( T = \id_V \), both satisfying \( T^2 = T \)), we need \( a = 2 \). So \( m_T = x^2 \) or \( m_T = x^2(x - 1) \). In the first case the only piece is \( \ker T^2 = V \); in the second, \( V = \ker T^2 \oplus \ker(T - \id_V) \).
:::

## Diagonalizability and the minimal polynomial

When every \( p_i \) is linear and every \( e_i = 1 \), the pieces are kernels of \( T - \lambda_i\,\id_V \), that is, eigenspaces. That is exactly diagonalizability, and it gives the criterion Chapter 5 promised.

::: {#thm-diagonalizable-iff-minimal-distinct-linear}
[Diagonalizability via the Minimal Polynomial]

Let \( V \) be a finite-dimensional vector space over \( F \) with \( \dim V \ge 1 \), and let \( T \in \cL(V) \). The following are equivalent:

::: {.enumerate options="label=(\alph*)"}
1. \( T \) is diagonalizable;
2. \( m_T = (x - \lambda_1)(x - \lambda_2)\cdots(x - \lambda_k) \) for some **distinct** \( \lambda_1, \dots, \lambda_k \in F \), that is, \( m_T \) splits over \( F \) with no repeated root;
3. some polynomial \( (x - \mu_1)\cdots(x - \mu_r) \) with **distinct** \( \mu_1, \dots, \mu_r \in F \) annihilates \( T \).
:::

In that case \( \lambda_1, \dots, \lambda_k \) are the distinct eigenvalues of \( T \). The same holds for \( \A \in M_n(F) \).
:::

::: {.idea}
(a) \( \Rightarrow \) (b): the polynomial \( \prod_i (x - \lambda_i) \) over the distinct eigenvalues kills each vector of an eigenbasis, hence kills \( T \); and \( m_T \) must contain every factor \( x - \lambda_i \), because its roots are the eigenvalues. (b) \( \Rightarrow \) (c) is free. (c) \( \Rightarrow \) (a): \( m_T \) divides a product of distinct linear factors, so it is one, and the primary decomposition with every \( e_i = 1 \) splits \( V \) into eigenspaces.
:::

::: {.proof}
(a) \( \Rightarrow \) (b). Let \( \lambda_1, \dots, \lambda_k \) be the distinct eigenvalues of \( T \), let \( \sB \) be a basis of eigenvectors (@thm-diagonalization (b)), and put \( q = (x - \lambda_1)\cdots(x - \lambda_k) \). For \( \v \in \sB \) with eigenvalue \( \lambda_j \), @exr-eigenvalues-and-eigenvectors-b3 (a) gives \( q(T)\v = q(\lambda_j)\v = \0 \), as \( x - \lambda_j \) is a factor of \( q \). So \( q(T) \) and the zero operator agree on a basis, and \( q(T) = 0 \) by the uniqueness in @thm-linear-transform-basis. Hence \( m_T \mid q \), and by @lem-monic-divisors \( m_T \) is a product of some of the factors \( x - \lambda_i \). Each \( \lambda_i \) is a root of \( m_T \) by @thm-minimal-polynomial-roots, so no factor is missing, and \( m_T = q \).

(b) \( \Rightarrow \) (c). Take \( q = m_T \).

(c) \( \Rightarrow \) (a). Let \( q = (x - \mu_1)\cdots(x - \mu_r) \) with distinct \( \mu_j \) annihilate \( T \). Each factor \( x - \mu_j \) is monic irreducible, being of degree \( 1 \) (@thm-degree-of-product: a factorization would leave one factor constant). By @thm-minimal-polynomial-divides and @lem-monic-divisors, \( m_T = (x - \lambda_1)\cdots(x - \lambda_k) \) for some distinct \( \lambda_i \) among the \( \mu_j \), and \( k \ge 1 \) since \( V \ne \{\0\} \). By @thm-minimal-polynomial-roots, \( \lambda_1, \dots, \lambda_k \) are exactly the eigenvalues of \( T \). Apply @thm-primary-decomposition with \( p_i = x - \lambda_i \) and \( e_i = 1 \):
\[
V = \ker(T - \lambda_1\id_V) \oplus \dots \oplus \ker(T - \lambda_k\id_V) = E_{\lambda_1}(T) \oplus \dots \oplus E_{\lambda_k}(T).
\]
This is condition (c) of @thm-diagonalization, so \( T \) is diagonalizable. The statement for matrices follows by applying this to \( T_{\A} \), since \( m_{\A} = m_{T_{\A}} \).
:::

This is the promise of Chapter 5 kept: **diagonalizable means the minimal polynomial splits with distinct roots.** The criterion is often the fastest test, because it needs no eigenvectors, only one polynomial identity. Chapter 5 also supplied a way to detect repeated factors without finding roots: if \( \gcd(m_T, m_T') = 1 \), then no irreducible factor of \( m_T \) is repeated (@cor-squarefree-gcd-derivative (a)). So \( T \) is diagonalizable as soon as \( m_T \) splits and is coprime to its derivative.

Condition (c) is especially useful because it does not require knowing \( m_T \) at all.

- **Projections.** If \( P^2 = P \), then \( x(x - 1) \) annihilates \( P \), and \( 0 \ne 1 \) in every field. So every projection on a finite-dimensional space is diagonalizable, over every field.
- **Involutions.** If \( T^2 = \id_V \) and the characteristic of \( F \) is not \( 2 \), then \( (x - 1)(x + 1) \) annihilates \( T \), and \( 1 \ne -1 \) because \( 2 \ne 0 \). So \( T \) is diagonalizable. In characteristic \( 2 \) this fails: over \( \nF_2 \), \( \J = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) has \( \J^2 = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} = \I \), but \( m_{\J} = (x - 1)^2 \).
- **Too few eigenvectors.** \( \J \) over any field has \( m_{\J} = (x - 1)^2 \), with a repeated root, so it is not diagonalizable, confirming Section 4 without any rank computation. Likewise the matrix of @exm-minimal-polynomial-by-eigenvalues, with \( m = (x - 1)(x - 3)^2 \), is not diagonalizable, while that of @exm-minimal-polynomial-by-dependence, with \( m = (x - 1)(x - 3) \), is.

The most striking use settles the question left open in Section 4 (@exr-diagonalization-c1).

::: {#exm-finite-order-diagonalizable}
[Complex Matrices of Finite Order Are Diagonalizable]

Let \( \A \in M_n(\nC) \), \( n \ge 1 \), satisfy \( \A^k = \I \) for some \( k \ge 1 \). Show that \( \A \) is diagonalizable, with eigenvalues among the \( k \)-th roots of unity. Show that both "over \( \nC \)" and "characteristic \( 0 \)" matter.
:::

::: {.solution}
*Diagonalizable.* The polynomial \( q = x^k - 1 \) annihilates \( \A \). By @cor-complex-polynomial-splits, \( q = (x - \zeta_1)\cdots(x - \zeta_k) \) for some \( \zeta_j \in \nC \). The \( \zeta_j \) are distinct: if \( c \) were a multiple root, then \( q(c) = 0 \) and \( q'(c) = kc^{k-1} = 0 \) by @thm-repeated-root-derivative (a). But \( q(c) = 0 \) means \( c^k = 1 \), so \( c \ne 0 \); and \( k \ne 0 \) in \( \nC \); so \( kc^{k-1} \ne 0 \), a contradiction. By @thm-diagonalizable-iff-minimal-distinct-linear ((c) \( \Rightarrow \) (a)), \( \A \) is diagonalizable. Its eigenvalues are roots of \( m_{\A} \), which divides \( q \), so each eigenvalue \( \lambda \) satisfies \( \lambda^k = 1 \). (Explicitly, the \( \zeta_j \) are \( e^{2\pi ij/k} \), \( j = 0, \dots, k - 1 \).)

*Over \( \nR \) it fails.* The rotation \( \R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \) has \( \R^4 = \I \) but is not diagonalizable over \( \nR \), since \( m_{\R} = x^2 + 1 \) does not split. The step that breaks is the splitting of \( x^4 - 1 = (x - 1)(x + 1)(x^2 + 1) \).

*In characteristic \( p \) it fails.* Over \( \nF_p \), \( \J = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) has \( \J^p = \begin{pmatrix} 1 & p \\ 0 & 1 \end{pmatrix} = \I \) (the powers of \( \J \) computed in Section 4), but \( m_{\J} = (x - 1)^2 \). The step that breaks is distinctness: the derivative of \( x^p - 1 \) is \( px^{p-1} = 0 \) in \( \nF_p \), and indeed \( 1 \) is a multiple root of \( x^p - 1 \).
:::

## Restrictions and polynomials of diagonalizable operators

The criterion in terms of a single annihilating polynomial passes easily to smaller spaces.

::: {#cor-restriction-diagonalizable}
[Restrictions of Diagonalizable Operators]

Let \( V \) be finite-dimensional, \( T \in \cL(V) \) diagonalizable, and \( U \) a \( T \)-invariant subspace. Then \( T|_U \) is diagonalizable. Moreover \( U = \bigoplus_{\lambda \in \spec(T)} \big(U \cap E_\lambda(T)\big) \).
:::

::: {.proof}
If \( U = \{\0\} \), the empty basis gives the empty (diagonal) matrix, and both statements are trivial. Let \( U \ne \{\0\} \). By @thm-diagonalizable-iff-minimal-distinct-linear ((a) \( \Rightarrow \) (b)), \( m_T = (x - \lambda_1)\cdots(x - \lambda_k) \) with distinct \( \lambda_i \), the eigenvalues of \( T \). By @exr-minimal-polynomial-c2 (a), \( m_T(T|_U) = m_T(T)|_U = 0 \), so \( m_T \) is a product of distinct linear factors annihilating \( T|_U \). By @thm-diagonalizable-iff-minimal-distinct-linear ((c) \( \Rightarrow \) (a)), \( T|_U \) is diagonalizable.

For the decomposition, @thm-diagonalization (c) applied to \( T|_U \) gives \( U = \bigoplus_\mu E_\mu(T|_U) \), over the eigenvalues \( \mu \) of \( T|_U \). An eigenvector of \( T|_U \) is an eigenvector of \( T \) lying in \( U \), so \( E_\mu(T|_U) = U \cap E_\mu(T) \), and every such \( \mu \) is in \( \spec(T) \). For \( \lambda \in \spec(T) \) that is not an eigenvalue of \( T|_U \), \( U \cap E_\lambda(T) = \{\0\} \), and adding zero summands does not change a direct sum.
:::

The second statement says that an invariant subspace of a diagonalizable operator is spanned by the eigenvectors it contains. It will be the key step in Section 9, where two commuting diagonalizable operators are diagonalized by a single basis.

Diagonalizability is also preserved by polynomials: if \( T \) is diagonalizable and \( p \in F[x] \), then every eigenvector of \( T \) for \( \lambda \) is an eigenvector of \( p(T) \) for \( p(\lambda) \) (@exr-eigenvalues-and-eigenvectors-b3 (a)), so a basis of eigenvectors of \( T \) is also one for \( p(T) \). This is the operator form of @exr-diagonalization-c2. The converse fails, as that exercise shows.

## When the minimal polynomial splits: a first look at Chapter 9

Suppose \( p_T \) splits, \( p_T = (x - \lambda_1)^{a_1} \cdots (x - \lambda_k)^{a_k} \) with distinct \( \lambda_i \); this always happens over \( \nC \). By @cor-minimal-divides-characteristic, \( m_T = (x - \lambda_1)^{s_1} \cdots (x - \lambda_k)^{s_k} \) with \( 1 \le s_i \le a_i \), and the primary decomposition reads
\[
V = \ker(T - \lambda_1\id_V)^{s_1} \oplus \dots \oplus \ker(T - \lambda_k\id_V)^{s_k}.
\]
On the \( i \)-th piece, \( T|_{V_i} = \lambda_i\,\id_{V_i} + N_i \), where \( N_i = (T - \lambda_i\id_V)|_{V_i} \) satisfies \( N_i^{s_i} = 0 \), because \( V_i = \ker(T - \lambda_i\id_V)^{s_i} \). So every operator whose characteristic polynomial splits is, piece by piece, a scalar plus a nilpotent operator. Chapter 9 calls the pieces **generalized eigenspaces** and finds the best basis for each nilpotent part, which leads to the Jordan form. Here we record only their dimensions.

::: {#cor-primary-components-dimension}
[Dimensions of the Primary Components]

Let \( V \) be finite-dimensional with \( \dim V \ge 1 \), \( T \in \cL(V) \), and suppose \( p_T \) splits over \( F \), with distinct eigenvalues \( \lambda_1, \dots, \lambda_k \) and \( m_T = \prod_i (x - \lambda_i)^{s_i} \). Let \( V_i = \ker(T - \lambda_i\id_V)^{s_i} \). Then
\[
p_{T|_{V_i}} = (x - \lambda_i)^{\dim V_i} \qquad \text{and} \qquad \dim V_i = a_T(\lambda_i) .
\]
Moreover \( E_{\lambda_i}(T) \subseteq V_i \), with equality if and only if \( s_i = 1 \).
:::

::: {.idea}
The decomposition makes \( p_T \) the product of the characteristic polynomials of the restrictions. Each of those factors is a monic divisor of \( p_T \), and its roots are the eigenvalues of the restriction, which the minimal polynomial \( (x - \lambda_i)^{s_i} \) pins down to the single value \( \lambda_i \). So the \( i \)-th factor is \( (x - \lambda_i)^{\dim V_i} \), and multiplying the factors back together identifies \( \dim V_i \) as the multiplicity of \( \lambda_i \) in \( p_T \).
:::

::: {.proof}
By @thm-primary-decomposition, \( V = V_1 \oplus \dots \oplus V_k \) with each \( V_i \) invariant, non-zero, and \( m_{T|_{V_i}} = (x - \lambda_i)^{s_i} \). By @thm-direct-sum-invariant-block-diagonal, \( p_T = p_{T|_{V_1}} \cdots p_{T|_{V_k}} \). So each \( p_{T|_{V_i}} \) is a monic divisor of \( p_T \), and by @lem-monic-divisors it is a product of powers of the \( x - \lambda_j \). Its roots are the eigenvalues of \( T|_{V_i} \) (@thm-eigenvalue-characterizations), which are the roots of \( m_{T|_{V_i}} = (x - \lambda_i)^{s_i} \) (@thm-minimal-polynomial-roots), that is, only \( \lambda_i \). So \( p_{T|_{V_i}} = (x - \lambda_i)^{d_i} \), with \( d_i = \deg p_{T|_{V_i}} = \dim V_i \) (@thm-charpoly-coefficients). Then \( p_T = \prod_i (x - \lambda_i)^{d_i} \), and since the \( \lambda_i \) are distinct, @lem-multiplicity-cofactor gives \( a_T(\lambda_i) = d_i \).

If \( T\v = \lambda_i\v \), then \( (T - \lambda_i\id_V)^{s_i}\v = \0 \) since \( s_i \ge 1 \), so \( E_{\lambda_i}(T) \subseteq V_i \). If \( s_i = 1 \), the two spaces are equal by definition. Conversely, if \( E_{\lambda_i}(T) = V_i \), then \( x - \lambda_i \) annihilates \( T|_{V_i} \), so \( m_{T|_{V_i}} = (x - \lambda_i)^{s_i} \) divides \( x - \lambda_i \), and \( s_i = 1 \).
:::

So, when \( p_T \) splits, the dimension of the \( i \)-th piece is the algebraic multiplicity \( a(\lambda_i) \), and inside it the eigenspace has dimension \( g(\lambda_i) \). The operator is diagonalizable exactly when all these pieces are eigenspaces, which ties together the three criteria of this chapter: \( g(\lambda_i) = a(\lambda_i) \) for all \( i \) (Section 4), every \( s_i = 1 \) (this section), and every piece \( \ker(T - \lambda_i\id_V)^{s_i} \) equal to \( \ker(T - \lambda_i\id_V) \).

::: {.warning}
**A single eigenvalue gives a single piece, whatever the operator looks like.** If \( p_T = (x - \lambda)^n \), then the primary decomposition is \( V = \ker(T - \lambda\id_V)^{s} \), all of \( V \), and says nothing new. For instance \( 2\I_3 \), \( \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} \oplus (2) \) and the matrix \( \A \) of @exm-triangularize-3x3 all have \( p = (x - 2)^3 \) and a primary decomposition with one piece, yet they are pairwise non-similar: their minimal polynomials are \( x - 2 \), \( (x - 2)^2 \) (@prp-minimal-polynomial-block-diagonal) and \( (x - 2)^3 \), the last because \( (\A - 2\I)^2 = \begin{pmatrix} 1 & -1 & 0 \\ 1 & -1 & 0 \\ 0 & 0 & 0 \end{pmatrix} \ne 0 \), and equal minimal polynomials are necessary for similarity (@thm-minimal-polynomial-similarity). Distinguishing operators within one piece is the work of Chapter 9.
:::

## Exercises

### A. Check your understanding

:::: {#exr-primary-decomposition-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the Primary Decomposition Theorem.
2. State the criterion for diagonalizability in terms of the minimal polynomial.
3. True or false: if \( m_{\A} = x(x - 1)(x + 1) \) over \( \nQ \), then \( \A \) is diagonalizable over \( \nQ \). Justify your answer.
4. True or false: if \( \A \in M_n(\nR) \) and \( \A^k = \I \) for some \( k \ge 1 \), then \( \A \) is diagonalizable over \( \nR \). Justify your answer.
5. Let \( m_T = (x - 2)^2(x + 1) \). What are the summands of the primary decomposition, and is \( T \) diagonalizable?
6. True or false: the restriction of a diagonalizable operator to an invariant subspace is diagonalizable. Justify your answer.
:::
::::

::: {.solution}
(a) If \( V \ne \{\0\} \) is finite-dimensional and \( m_T = p_1^{e_1} \cdots p_k^{e_k} \) with distinct monic irreducible \( p_i \), then \( V = \bigoplus_i \ker p_i(T)^{e_i} \); the summands are invariant and non-zero, \( T \) restricted to the \( i \)-th has minimal polynomial \( p_i^{e_i} \), and the projections are polynomials in \( T \) (@thm-primary-decomposition).

(b) \( T \) is diagonalizable if and only if \( m_T \) is a product of distinct monic linear factors over \( F \) (@thm-diagonalizable-iff-minimal-distinct-linear).

(c) True: \( m_{\A} \) splits over \( \nQ \) with distinct roots \( 0, 1, -1 \).

(d) False. The rotation by a right angle satisfies \( \R^4 = \I \) but has no real eigenvalue (@exm-finite-order-diagonalizable).

(e) \( \ker(T - 2\id_V)^2 \) and \( \ker(T + \id_V) \). \( T \) is not diagonalizable, since \( m_T \) has the repeated root \( 2 \).

(f) True, by @cor-restriction-diagonalizable.
:::

### B. Practice

:::: {#exr-primary-decomposition-b1}
[B1: Diagonalizable or not?]

Determine whether each matrix is diagonalizable over the given field. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \A_1 = \begin{pmatrix} 2 & 1 & 1 \\ -1 & 0 & -1 \\ 1 & 1 & 2 \end{pmatrix} \) over \( \nR \) (see @exr-minimal-polynomial-b1).
2. \( \M_1 = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 0 \\ -1 & 1 & 3 \end{pmatrix} \) over \( \nR \) (see @exr-cayley-hamilton-b3).
3. Any \( \A \in M_5(\nQ) \) with \( \A^3 = 4\A \).
4. Any \( \A \in M_2(\nR) \) with \( \A^2 + \I = 0 \), over \( \nR \) and over \( \nC \).
:::
::::

::: {.solution}
(a) By @exr-minimal-polynomial-b1 (d), \( m_{\A_1} = (x - 1)(x - 2) \), which has distinct linear factors. Diagonalizable, by @thm-diagonalizable-iff-minimal-distinct-linear.

(b) By @exr-cayley-hamilton-b3, \( m_{\M_1} = (x - 2)^2(x - 3) \), with a repeated root. Not diagonalizable.

(c) \( x^3 - 4x = x(x - 2)(x + 2) \) annihilates \( \A \), and \( 0, 2, -2 \) are distinct in \( \nQ \). Diagonalizable, by condition (c) of @thm-diagonalizable-iff-minimal-distinct-linear.

(d) \( m_{\A} \mid x^2 + 1 \). Over \( \nR \), \( x^2 + 1 \) has no root, so it is irreducible (@thm-irreducible-deg-2-3), and \( m_{\A} = x^2 + 1 \) (it is not \( 1 \) since \( \A \) acts on \( \nR^2 \ne \{\0\} \)). It does not split over \( \nR \), so \( \A \) is not diagonalizable over \( \nR \). Over \( \nC \), \( x^2 + 1 = (x - i)(x + i) \) with \( i \ne -i \), so condition (c) holds and \( \A \) is diagonalizable over \( \nC \).
:::

:::: {#exr-primary-decomposition-b2}
[B2: Decomposing \( \nR^3 \)]

Let \( \A = \begin{pmatrix} 2 & 1 & 1 \\ 0 & 1 & -1 \\ -1 & -1 & 1 \end{pmatrix} \in M_3(\nR) \), which has \( m_{\A} = (x - 1)^2(x - 2) \) (@exr-minimal-polynomial-b1 (c)).

::: {.enumerate options="label=(\alph*)"}
1. Find bases of \( V_1 = \ker(\A - \I)^2 \) and \( V_2 = \ker(\A - 2\I) \), and check that \( \nR^3 = V_1 \oplus V_2 \).
2. Compare \( V_1 \) with \( E_1(\A) \).
3. Using \( (x - 1)^2 - x(x - 2) = 1 \), write the two projections as polynomials in \( \A \), and compute them.
4. Write the matrix of \( T_{\A} \) in the basis formed by your bases of \( V_1 \) and \( V_2 \).
:::
::::

::: {.solution}
(a) \( (\A - \I)^2 = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 0 & -1 \\ -1 & -1 & 0 \end{pmatrix}^2 = \begin{pmatrix} 0 & 0 & 0 \\ 1 & 1 & 0 \\ -1 & -1 & 0 \end{pmatrix} \), whose kernel is \( x + y = 0 \), with basis \( (-1, 1, 0) \), \( (0, 0, 1) \). \( \A - 2\I = \begin{pmatrix} 0 & 1 & 1 \\ 0 & -1 & -1 \\ -1 & -1 & -1 \end{pmatrix} \) gives \( y + z = 0 \) and \( x = -y - z = 0 \), so \( V_2 = \Span((0, -1, 1)) \). The three vectors form a basis of \( \nR^3 \): the matrix with these columns has determinant \( -1 \cdot (0 \cdot 1 - 1 \cdot (-1)) - 0 + 0 = -1 \ne 0 \), expanding along the first row. So \( \nR^3 = V_1 \oplus V_2 \), as @thm-primary-decomposition guarantees.

(b) \( \A - \I \) has rank \( 2 \) (its third row is minus the sum of the first two, and the first two are independent), so \( E_1(\A) \) is a line, \( \Span((-1, 1, 0)) \), strictly inside the plane \( V_1 \). This matches @cor-primary-components-dimension: \( \dim V_1 = a(1) = 2 \), \( g(1) = 1 \), \( s_1 = 2 \).

(c) With \( p = (x - 1)^2 \), \( q = x - 2 \), \( a = 1 \), \( b = -x \) in @thm-kernel-splitting (c), the projection onto \( V_1 \) along \( V_2 \) is \( b(\A)q(\A) = -\A(\A - 2\I) \), and onto \( V_2 \) along \( V_1 \) it is \( a(\A)p(\A) = (\A - \I)^2 \). Computing,
\[
-\A(\A - 2\I) = \begin{pmatrix} 1 & 0 & 0 \\ -1 & 0 & 0 \\ 1 & 1 & 1 \end{pmatrix}, \qquad (\A - \I)^2 = \begin{pmatrix} 0 & 0 & 0 \\ 1 & 1 & 0 \\ -1 & -1 & 0 \end{pmatrix}.
\]
They add up to \( \I \). The columns of the first satisfy \( x + y = 0 \), so they lie in \( V_1 \); the columns of the second are multiples of \( (0, -1, 1) \), so they lie in \( V_2 \).

(d) \( \A(-1, 1, 0) = (-1, 1, 0) \), \( \A(0, 0, 1) = (1, -1, 1) = -(-1, 1, 0) + (0, 0, 1) \), and \( \A(0, -1, 1) = (0, -2, 2) = 2(0, -1, 1) \). So the matrix is
\[
\begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} \oplus (2),
\]
block diagonal as @thm-direct-sum-invariant-block-diagonal predicts, with first block of minimal polynomial \( (x - 1)^2 \).
:::

:::: {#exr-primary-decomposition-b3}
[B3: Matrices with \( \A^3 = \A \)]

Let \( F \) have characteristic not \( 2 \), and let \( \A \in M_n(F) \), \( n \ge 1 \), satisfy \( \A^3 = \A \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \A \) is diagonalizable, with \( \spec(\A) \subseteq \{0, 1, -1\} \).
2. Now let \( F = \nR \). Prove that \( \rank \A = \tr(\A^2) \).
:::
::::

::: {.solution}
(a) \( x^3 - x = x(x - 1)(x + 1) \) annihilates \( \A \). The roots \( 0, 1, -1 \) are distinct: \( 1 \ne 0 \), \( -1 \ne 0 \), and \( 1 \ne -1 \) because \( 2 \ne 0 \). By @thm-diagonalizable-iff-minimal-distinct-linear ((c) \( \Rightarrow \) (a)), \( \A \) is diagonalizable, and its eigenvalues are roots of \( m_{\A} \mid x^3 - x \), so they lie in \( \{0, 1, -1\} \).

(b) Write \( \A = \P\D \P^{-1} \) with \( \D \) diagonal, entries in \( \{0, 1, -1\} \). Then \( \rank \A = \rank \D \) (@prp-similarity-invariants (a)), which is the number \( r \) of non-zero diagonal entries. Also \( \A^2 = \P\D^2\P^{-1} \) (@thm-powers-diagonalizable), and \( \D^2 \) is diagonal with \( r \) entries \( 1 \) and the rest \( 0 \). By @thm-trace-similarity-invariant, \( \tr \A^2 = \tr \D^2 = r \).
:::

### C. Going deeper

:::: {#exr-primary-decomposition-c1}
[C1: \( \A^p = \A \) over \( \nF_p \)]

Let \( p \) be a prime and \( \A \in M_n(\nF_p) \), \( n \ge 1 \), with \( \A^p = \A \).

::: {.enumerate options="label=(\alph*)"}
1. Let \( a \in \nF_p \) be non-zero. Show that \( b \mapsto ab \) is a bijection of \( \nF_p \setminus \{0\} \), and deduce \( a^{p-1} = 1 \). Conclude that \( a^p = a \) for **every** \( a \in \nF_p \).
2. Deduce that \( x^p - x = \prod_{a \in \nF_p} (x - a) \) in \( \nF_p[x] \).
3. Prove that \( \A \) is diagonalizable over \( \nF_p \).
4. Show that \( \J = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) satisfies \( \J^p = \I \) over \( \nF_p \) but is not diagonalizable, and explain why this does not contradict (c).
:::

*Hint: for (a), compare the product of all non-zero elements with the product of all their multiples by \( a \).*
::::

::: {.solution}
(a) The map \( b \mapsto ab \) sends non-zero elements to non-zero elements (@thm-field-basic-properties), and it is injective, since \( ab = ab' \) gives \( b = b' \) after multiplying by \( a^{-1} \). An injective map from the finite set \( \nF_p \setminus \{0\} \) to itself is bijective (@thm-finite-injective-iff-surjective). So the elements \( ab \), for \( b \ne 0 \), are the non-zero elements in another order. Let \( c \) be the product of all non-zero elements; it is non-zero. Multiplying the \( p - 1 \) elements \( ab \) gives \( a^{p-1}c = c \), by commutativity, so \( a^{p-1} = 1 \). Multiplying by \( a \) gives \( a^p = a \), which also holds for \( a = 0 \).

(b) By (a), each of the \( p \) distinct elements of \( \nF_p \) is a root of \( f = x^p - x \). By @thm-roots-with-multiplicity, the multiplicities of these roots, each at least \( 1 \), add up to at most \( \deg f = p \). So each multiplicity is \( 1 \), the sum equals \( p \), and \( f \) splits; as \( f \) is monic, \( f = \prod_{a \in \nF_p}(x - a) \).

(c) By (b), \( x^p - x \) is a product of distinct monic linear factors, and it annihilates \( \A \). By @thm-diagonalizable-iff-minimal-distinct-linear ((c) \( \Rightarrow \) (a)), \( \A \) is diagonalizable, with eigenvalues in \( \nF_p \).

(d) As in @exm-finite-order-diagonalizable, \( \J^p = \begin{pmatrix} 1 & p \\ 0 & 1 \end{pmatrix} = \I \) in \( \nF_p \), while \( m_{\J} = (x - 1)^2 \), so \( \J \) is not diagonalizable. There is no contradiction: \( \J \) satisfies \( \J^p = \I \), not \( \J^p = \J \) (for \( p \ge 2 \), \( \J^p = \I \ne \J \)). The polynomial \( x^p - 1 \) has the multiple root \( 1 \), because its derivative \( px^{p-1} \) is \( 0 \) in \( \nF_p \) (@thm-repeated-root-derivative (a)).
:::

:::: {#exr-primary-decomposition-c2}
[C2: Irreducible minimal polynomials]

Let \( V \ne \{\0\} \) be finite-dimensional, \( T \in \cL(V) \), and suppose \( m_T \) is **irreducible**, of degree \( d \). For \( \v \in V \), let \( W_\v = \{ q(T)\v : q \in F[x] \} \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( W_\v \) is the smallest \( T \)-invariant subspace of \( V \) containing \( \v \).
2. Let \( \v \ne \0 \). Prove that \( (\v, T\v, \dots, T^{d-1}\v) \) is a basis of \( W_\v \). In particular \( \dim W_\v = d \).
3. Deduce that the only \( T \)-invariant subspaces of \( W_\v \) are \( \{\0\} \) and \( W_\v \).
4. Prove that \( V \) is a direct sum of subspaces of the form \( W_\v \), and hence that \( d \) divides \( \dim V \).
5. Illustrate with the rotation \( \R \) of \( \nR^2 \) and with \( \R \oplus \R \) on \( \nR^4 \).
:::

*Hint: for (b), use the gcd of \( m_T \) with a polynomial of degree less than \( d \). For (d), take a direct sum \( W_{\v_1} \oplus \dots \oplus W_{\v_s} \) that is as large as possible.*
::::

::: {.solution}
(a) \( W_\v \) is the image of the linear map \( F[x] \to V \), \( q \mapsto q(T)\v \) (linear by @thm-evaluation-homomorphism (a)), so it is a subspace (@thm-prop-image). It contains \( \v = 1(T)\v \), and \( T(q(T)\v) = (xq)(T)\v \in W_\v \), so it is invariant. If \( W \) is any invariant subspace containing \( \v \), then \( T^k\v \in W \) for all \( k \) by induction, so every \( q(T)\v \in W \), and \( W_\v \subseteq W \).

(b) *Independence.* Suppose \( q(T)\v = \0 \) for some non-zero \( q \) of degree less than \( d \). Let \( g = \gcd(q, m_T) \). It is a monic divisor of the irreducible \( m_T \), so \( g = 1 \) or \( g = m_T \) (@def-irreducible-polynomial). It is not \( m_T \), since \( m_T \nmid q \) for degree reasons (@prp-divisibility-properties (c)). So \( g = 1 \), and \( aq + bm_T = 1 \) for some \( a, b \) (@cor-bezout-polynomials). Then \( \v = a(T)q(T)\v + b(T)m_T(T)\v = \0 \), a contradiction. So no non-trivial combination of \( \v, \dots, T^{d-1}\v \) is \( \0 \).

*Spanning.* For \( q \in F[x] \), divide: \( q = s\,m_T + r \) with \( \deg r < d \) (@thm-polynomial-division). Then \( q(T)\v = r(T)\v \), a combination of \( \v, \dots, T^{d-1}\v \).

(c) Let \( W \subseteq W_\v \) be invariant and non-zero, and take \( \w \in W \) with \( \w \ne \0 \). By (a), \( W_\w \subseteq W \). By (b), \( \dim W_\w = d = \dim W_\v \), so \( W_\w = W_\v \) (@thm-dim-impl-eq), and hence \( W = W_\v \).

(d) Among all families \( \v_1, \dots, \v_s \) of non-zero vectors for which the sum \( S = W_{\v_1} + \dots + W_{\v_s} \) is direct, choose one with \( s \) as large as possible; this is possible since \( \dim S = sd \le \dim V \) by (b) and @thm-direct-sum-k-criteria. Suppose \( S \ne V \), and take \( \v \in V \setminus S \). The subspace \( W_\v \cap S \) is invariant (@prp-invariant-sum-intersection) and lies in \( W_\v \), but does not contain \( \v \); by (c) it is \( \{\0\} \). Then the sum \( S + W_\v \) is direct: if \( \u_1 + \dots + \u_s + \w = \0 \) with \( \u_j \in W_{\v_j} \) and \( \w \in W_\v \), then \( \w \in W_\v \cap S = \{\0\} \), and directness of \( S \) gives all \( \u_j = \0 \). This contradicts the maximality of \( s \). So \( V = W_{\v_1} \oplus \dots \oplus W_{\v_s} \), and \( \dim V = sd \).

(e) For the rotation \( \R \), \( m_{\R} = x^2 + 1 \) is irreducible over \( \nR \), \( d = 2 \), and \( W_\v = \nR^2 \) for every \( \v \ne \0 \): no line is invariant (@exm-rotation-invariant-subspaces). For \( \R \oplus \R \), \( m = \operatorname{lcm}(x^2 + 1, x^2 + 1) = x^2 + 1 \) (@prp-minimal-polynomial-block-diagonal), and \( \nR^4 = W_{\e_1} \oplus W_{\e_3} \) with \( W_{\e_1} = \Span(\e_1, \e_2) \) and \( W_{\e_3} = \Span(\e_3, \e_4) \); indeed \( 2 \mid 4 \).
:::
