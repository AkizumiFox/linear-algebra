# Semisimple Operators and the Jordan–Chevalley Decomposition

The Jordan canonical form says that an operator whose characteristic polynomial splits is "a diagonal matrix plus a nilpotent one" — but only after a basis has been chosen. This section turns that sentence into a statement about the operator itself: \( T = S + N \) with \( S \) diagonalizable, \( N \) nilpotent and, crucially, \( SN = NS \); and there is exactly one such pair. Before that we need a name for the operators that deserve to be called diagonalizable even when the field is too small to see it.

## Diagonalizable once the field is big enough

Two operators fail to be diagonalizable for completely different reasons. The rotation \( \R = \begin{pmatrix} 0 & -1 \\ 1 & 0\end{pmatrix} \in M_2(\nR) \) has \( p_{\R} = m_{\R} = x^2 + 1 \), with no real root, so it has no eigenvectors at all (@exm-complex-eigenvalues-real-matrix). Yet over \( \nC \) it becomes \( \diag(i, -i) \): the operator was fine, the field was too small. The shear \( \J_2(0) \) has \( m = x^2 \) and is not diagonalizable over **any** field, however large: its single eigenvalue \( 0 \) has \( a = 2 \) and \( g = 1 \), and enlarging the field changes neither.

What separates the two cases is visible in the minimal polynomial. For \( \R \) it is \( x^2 + 1 \), irreducible over \( \nR \) and appearing to the first power. For \( \J_2(0) \) it is \( x^2 \), the **square** of the irreducible \( x \). Chapter 8 proved that \( T \) is diagonalizable exactly when \( m_T \) is a product of **distinct linear** factors (@thm-diagonalizable-iff-minimal-distinct-linear). Deleting the word "linear" from that criterion gives the notion we want.

*A semisimple operator is one whose minimal polynomial is squarefree: no irreducible factor is repeated.*

::: {#def-semisimple-operator}
[Semisimple Operator]

Let \( V \) be a finite-dimensional vector space over \( F \) with \( \dim V \ge 1 \), and let \( T \in \cL(V) \). We say \( T \) is **semisimple** if
\[
m_T = p_1p_2\cdots p_k
\]
for **distinct** monic irreducible \( p_1, \dots, p_k \in F[x] \); equivalently, if **no** irreducible polynomial \( p \in F[x] \) satisfies \( p^2 \mid m_T \). A matrix \( \A \in M_n(F) \) is **semisimple over \( F \)** if \( T_{\A} \) is.
:::

In words: factor \( m_T \) into irreducibles over \( F \) (@thm-unique-factorization-polynomials). Semisimplicity says every exponent in that factorization is \( 1 \). The two descriptions agree: the exponents are all \( 1 \) exactly when no \( p^2 \) divides \( m_T \), by uniqueness of factorization. Note the dependence on the field, which is built into the word "irreducible over \( F \)".

**Examples.**

- **Diagonalizable operators.** If \( T \) is diagonalizable, \( m_T \) is a product of distinct linear factors (@thm-diagonalizable-iff-minimal-distinct-linear), and linear polynomials are irreducible (@def-irreducible-polynomial). So \( T \) is semisimple.
- **The rotation.** \( \R \in M_2(\nR) \) above has \( m_{\R} = x^2 + 1 \), irreducible over \( \nR \) since it has no real root (@thm-irreducible-deg-2-3). One factor, exponent \( 1 \): semisimple over \( \nR \), though not diagonalizable over \( \nR \).
- **Any operator with irreducible minimal polynomial**, for the same reason. In particular the companion matrix \( \C(p) \) of an irreducible \( p \) is semisimple, since \( m_{\C(p)} = p \) (@thm-companion-char-min).
- **The degenerate case.** On a space of dimension \( 1 \), \( T = \lambda\,\id_V \) has \( m_T = x - \lambda \): semisimple. So is \( \id_V \) on any \( V \), with \( m = x - 1 \).

**Non-example by minimal change.** Over \( \nR \), replace \( m = x^2 + 1 \) by \( m = (x^2+1)^2 \): the companion matrix \( \C\bigl((x^2+1)^2\bigr) \in M_4(\nR) \) has \( m = (x^2+1)^2 \) (@thm-companion-char-min), so the irreducible \( x^2 + 1 \) is repeated and the matrix is **not** semisimple. The clause that fails is "distinct": there is one irreducible factor, but it occurs twice.

**Why this definition.** The word *simple* names the case in which \( V \) has no \( T \)-invariant subspace except \( \{\0\} \) and \( V \). That happens exactly when \( m_T \) is irreducible **and** \( \dim V = \deg m_T \), for then every non-zero \( \v \) has \( T \)-annihilator \( m_T \) and so \( Z(\v; T) = V \) (@thm-cyclic-subspace-basis). *Semisimple* then means "a direct sum of simple pieces", which is what @thm-primary-decomposition followed by a cyclic decomposition (@thm-cyclic-decomposition) delivers. The definition is the right one because it is exactly diagonalizability after the field has been enlarged enough to split \( m_T \) — provided the field is not pathological. Making that precise needs one small fact: the minimal polynomial does not change when the field grows.

::: {#lem-minimal-polynomial-field-extension}
[The Minimal Polynomial Does Not Notice a Larger Field]

Let \( K \subseteq L \) be fields and \( \A \in M_n(K) \), \( n \ge 1 \). Then the minimal polynomial of \( \A \) computed in \( K[x] \) equals the minimal polynomial of \( \A \) computed in \( L[x] \).
:::

::: {.idea}
The degree of \( m_{\A} \) is the position of the first linear dependence in the list \( \I, \A, \A^2, \dots \) (@prp-minimal-polynomial-first-dependence). Whether a list of matrices with entries in \( K \) is dependent is decided by row reducing one matrix with entries in \( K \), and row reduction does not care that a bigger field is available.
:::

::: {.proof}
Write \( m^K \) and \( m^L \) for the two minimal polynomials, and \( d = \deg m^K \), \( e = \deg m^L \).

Since \( m^K \in K[x] \subseteq L[x] \) annihilates \( \A \), @thm-minimal-polynomial-divides gives \( m^L \mid m^K \), so \( e \le d \).

For the reverse inequality, list the entries of \( \I, \A, \dots, \A^{e} \) as the columns of a matrix \( \B \in M_{n^2 \times (e+1)}(K) \), one column per power. A linear combination \( \sum_{i=0}^{e} c_i\A^i \) is the zero matrix exactly when \( \B\c = \0 \) for \( \c = (c_0, \dots, c_e) \). By @prp-minimal-polynomial-first-dependence applied over \( L \), the list \( (\I, \A, \dots, \A^{e}) \) is dependent over \( L \), so \( \B\c = \0 \) has a non-trivial solution in \( L^{e+1} \), and hence \( \rank_L \B < e + 1 \) (@thm-rank-nullity-matrix). Now reduce \( \B \) to reduced row echelon form by row operations performed inside \( K \) (@thm-rref-exists); the resulting matrix \( \R \) has entries in \( K \), and the definition of reduced row echelon form (@def-reduced-row-echelon-form) makes no reference to the field, so \( \R \) is also **the** reduced row echelon form of \( \B \) over \( L \), by the uniqueness in @thm-rref-unique. The rank is the number of pivots of \( \R \) (@cor-rank-from-any-echelon-form), a number read off \( \R \) alone. Hence
\[
\rank_K \B = \rank_L \B < e + 1 ,
\]
so \( \B\c = \0 \) has a non-trivial solution in \( K^{e+1} \) as well. That solution gives a non-zero \( f \in K[x] \) of degree at most \( e \) with \( f(\A) = 0 \), whence \( d = \deg m^K \le e \) by @thm-minimal-polynomial-divides and @prp-divisibility-properties.

So \( d = e \), and \( m^L \mid m^K \) with both monic of the same degree forces \( m^L = m^K \).
:::

::: {#prp-semisimple-iff-diagonalizable-over-extension}
[Semisimple Means Diagonalizable After Enlarging the Field]

Let \( K \) be a field of characteristic \( 0 \), let \( \A \in M_n(K) \) with \( n \ge 1 \), and let \( L \supseteq K \) be a field over which \( m_{\A} \) splits. Then
\[
\A \text{ is semisimple over } K \qquad \Longleftrightarrow \qquad \A \text{ is diagonalizable over } L .
\]
:::

::: {.proof}
By @lem-minimal-polynomial-field-extension the minimal polynomial is the same polynomial \( m = m_{\A} \) whether computed over \( K \) or over \( L \). By @thm-diagonalizable-iff-minimal-distinct-linear, \( \A \) is diagonalizable over \( L \) if and only if \( m \) is a product of distinct linear factors in \( L[x] \), that is, if and only if \( m \) splits over \( L \) — which it does by hypothesis — with **no repeated root**.

\( (\Leftarrow) \) Suppose \( m \) has no repeated root in \( L \). If some irreducible \( p \in K[x] \) satisfied \( m = p^2h \), then \( p \mid m \) and \( m \) splits over \( L \), so \( p \) has a root \( \lambda \in L \); by @thm-multiplicity-of-product, \( \operatorname{mult}_\lambda(m) \ge 2\operatorname{mult}_\lambda(p) \ge 2 \), and \( \lambda \) would be a repeated root of \( m \). So no such \( p \) exists and \( \A \) is semisimple over \( K \).

\( (\Rightarrow) \) Suppose \( m = p_1\cdots p_k \) with \( p_1, \dots, p_k \in K[x] \) distinct monic irreducibles. The formal derivative is computed from the coefficients (@def-formal-derivative), so each \( p_i' \) is the same polynomial whether read in \( K[x] \) or in \( L[x] \).

*No \( p_i \) has a repeated root in \( L \).* Since \( K \) has characteristic \( 0 \) and \( \deg p_i \ge 1 \), the derivative \( p_i' \) is non-zero of degree \( \deg p_i - 1 \), so \( p_i \nmid p_i' \); as \( p_i \) is irreducible, @lem-irreducible-gcd gives \( \gcd(p_i, p_i') = 1 \), and by @cor-bezout-polynomials there are \( a, b \in K[x] \) with \( ap_i + bp_i' = 1 \). If \( \lambda \in L \) were a repeated root of \( p_i \), then \( p_i(\lambda) = p_i'(\lambda) = 0 \) by @thm-repeated-root-derivative (a), applied in \( L[x] \); evaluating the identity at \( \lambda \) would give \( 1 = 0 \).

*No two \( p_i \) share a root in \( L \).* For \( i \ne j \), a monic divisor of the irreducible \( p_j \) is \( 1 \) or \( p_j \), so \( p_i \nmid p_j \), and @lem-irreducible-gcd gives \( \gcd(p_i, p_j) = 1 \). Again by @cor-bezout-polynomials, \( ap_i + bp_j = 1 \) for some \( a, b \in K[x] \), and a common root in \( L \) would give \( 1 = 0 \).

Therefore, by @thm-multiplicity-of-product, every root of \( m \) in \( L \) has multiplicity \( 1 \): it is a root of exactly one \( p_i \), and a simple one. So \( m \) is a product of distinct linear factors over \( L \), and \( \A \) is diagonalizable over \( L \).
:::

::: {.remark}
A field over which every irreducible polynomial has distinct roots in a splitting field is called **perfect**. The proof above shows that every field of characteristic \( 0 \) is perfect, and every finite field is perfect as well, although that needs an argument we do not give here. Over a non-perfect field @prp-semisimple-iff-diagonalizable-over-extension can fail: in characteristic \( p \) there are irreducible polynomials of the form \( q(x^p) \), whose derivative vanishes identically and which acquire repeated roots in a splitting field. Everything in the rest of this section takes place over a field where \( p_T \) splits, so this subtlety will not arise again.
:::

::: {.check}
Over \( \nQ \), which of \( \A = \C(x^2+1) \oplus \C(x^2+1) \in M_4(\nQ) \) and \( \B = \C\bigl((x^2+1)^2\bigr) \in M_4(\nQ) \) is semisimple? Is either diagonalizable over \( \nQ \)?
:::

::: {.solution}
\( \A \) is semisimple. Each block has minimal polynomial \( x^2 + 1 \) (@thm-companion-char-min), so \( m_{\A} = \operatorname{lcm}(x^2+1, x^2+1) = x^2+1 \) (@prp-minimal-polynomial-block-diagonal), an irreducible polynomial to the first power. \( \B \) is not: \( m_{\B} = (x^2+1)^2 \) repeats the irreducible \( x^2+1 \). Neither is diagonalizable over \( \nQ \), since \( x^2+1 \) has no rational root, so neither minimal polynomial is a product of linear factors. Over \( \nC \), however, \( \A \) becomes \( \diag(i, -i, i, -i) \), while \( \B \) becomes \( \J_2(i) \oplus \J_2(-i) \), which is not diagonal.
:::

## Splitting an operator in two

Here is the goal. **When \( p_T \) splits, \( T \) is the sum of a diagonalizable operator and a nilpotent operator that commute, in exactly one way, and both summands are polynomials in \( T \).** The Jordan form already shows *a* splitting: in a Jordan basis, \( \J = \D + \M \) where \( \D \) is the diagonal of \( \J \) and \( \M \) carries the superdiagonal ones, and these commute because \( \D \) is constant on each block. What the theorem adds is that the two pieces do not depend on which Jordan basis was used, and that they can be written down without finding one.

::: {#thm-jordan-chevalley}
[Jordan–Chevalley Decomposition]

Let \( V \) be a finite-dimensional vector space over \( F \) with \( \dim V = n \ge 1 \), and let \( T \in \cL(V) \) with \( p_T \) split over \( F \). Then:

::: {.enumerate options="label=(\alph*)"}
1. **(Existence)** There are \( S, N \in \cL(V) \) with
   \[
   T = S + N, \qquad S \text{ diagonalizable}, \qquad N \text{ nilpotent}, \qquad SN = NS ;
   \]
   moreover \( S = g(T) \) and \( N = h(T) \) for some \( g, h \in F[x] \).
2. **(Uniqueness)** If \( T = S' + N' \) with \( S' \) diagonalizable, \( N' \) nilpotent and \( S'N' = N'S' \), then \( S' = S \) and \( N' = N \).
:::

We call \( S \) the **semisimple part** and \( N \) the **nilpotent part** of \( T \).
:::

::: {.idea}
**Existence.** The generalized eigenspace decomposition already puts the answer in front of us: on \( G_\lambda \) the operator is \( \lambda\,\id + \text{nilpotent} \). Declare \( S \) to be \( \lambda\,\id \) on \( G_\lambda \) for each \( \lambda \) and let \( N \) be the rest. Then \( S \) is diagonalizable because a basis assembled from bases of the \( G_\lambda \) consists of eigenvectors of \( S \), and \( N \) is nilpotent because it is nilpotent on each piece. That \( S \) and \( N \) are polynomials in \( T \) is the extra information carried by the primary decomposition: its projections are \( h_i(T) \).

**Uniqueness.** A second decomposition \( S' + N' \) has \( S' \) commuting with \( T \), hence with every polynomial in \( T \), hence with \( S \) and with \( N \); the same for \( N' \). Then \( S - S' = N' - N \) is simultaneously diagonalizable and nilpotent, and the only such operator is \( 0 \).
:::

::: {.proof}
(a) Let \( \lambda_1, \dots, \lambda_k \) be the distinct eigenvalues of \( T \) and write
\[
m_T = (x - \lambda_1)^{s_1}\cdots(x - \lambda_k)^{s_k}, \qquad G_i = G_{\lambda_i}(T),
\]
as in @thm-generalized-eigenspace-decomposition, so that \( V = G_1 \oplus \dots \oplus G_k \) with \( G_i = \ker(T - \lambda_i\,\id_V)^{s_i} \). The factors \( (x - \lambda_i)^{s_i} \) are exactly the primary factors of \( m_T \), since \( x - \lambda_i \) is irreducible, so \( G_i \) is the \( i \)-th primary component of @thm-primary-decomposition. By part (d) of that theorem there are \( h_1, \dots, h_k \in F[x] \) such that
\[
\pi_i \coloneqq h_i(T) \in \cL(V)
\]
is the projection onto \( G_i \) along \( \bigoplus_{j \ne i}G_j \). Put
\[
\begin{aligned}
g &\coloneqq \sum_{i=1}^{k}\lambda_ih_i \in F[x], \\
S &\coloneqq g(T) = \sum_{i=1}^{k}\lambda_i\pi_i, \\
N &\coloneqq T - S = h(T) \text{ with } h = x - g .
\end{aligned}
\]

*\( S \) is diagonalizable.* Fix \( i \) and \( \v \in G_i \). Then \( \pi_i\v = \v \) and \( \pi_j\v = \0 \) for \( j \ne i \) (@thm-projection-direct-sum), so \( S\v = \lambda_i\v \). Choose a basis of each \( G_i \) and let \( \sB \) be the concatenation, a basis of \( V \) because \( V = \bigoplus_iG_i \). Every vector of \( \sB \) is an eigenvector of \( S \), so \( [S]_{\sB} \) is diagonal and \( S \) is diagonalizable (@thm-diagonalization).

*\( N \) is nilpotent.* Fix \( i \) and \( \v \in G_i \). Then \( N\v = T\v - \lambda_i\v = (T - \lambda_i\,\id_V)\v \), which lies in \( G_i \) because \( G_i \) is \( T \)-invariant, so by induction \( N^j\v = (T - \lambda_i\,\id_V)^j\v \) for every \( j \ge 0 \). With \( s = \max_i s_i \) we get \( N^{s}\v = (T - \lambda_i\,\id_V)^{s}\v = \0 \), since \( (T - \lambda_i\,\id_V)^{s_i}\v = \0 \) and \( s \ge s_i \). As every \( \v \in V \) is a sum of such vectors, \( N^{s} = 0 \) and \( N \) is nilpotent (@def-nilpotent).

*They commute.* Both \( S = g(T) \) and \( N = h(T) \) are polynomials in \( T \), and any two polynomials in \( T \) commute (@thm-evaluation-homomorphism (c)). This proves (a).

(b) Suppose \( T = S' + N' \) as stated. First, \( S' \) commutes with \( T \):
\[
S'T = S'(S' + N') = S'S' + S'N' = S'S' + N'S' = (S' + N')S' = TS' ,
\]
where the middle equality is the hypothesis \( S'N' = N'S' \). Hence \( S' \) commutes with every power of \( T \) and so with every polynomial in \( T \), in particular with \( S = g(T) \) and \( N = h(T) \). The same computation gives \( N'T = TN' \), so \( N' \) too commutes with \( S \) and \( N \).

Now set \( X \coloneqq S - S' \). From \( S + N = T = S' + N' \) we get
\[
X = S - S' = N' - N .
\]
The operators \( S \) and \( S' \) are diagonalizable and commute, so they are simultaneously diagonalizable (@thm-simultaneous-diagonalization): there is a basis \( \sC \) in which \( [S]_{\sC} \) and \( [S']_{\sC} \) are both diagonal. Then \( [X]_{\sC} = [S]_{\sC} - [S']_{\sC} \) is diagonal, so \( X \) is diagonalizable. On the other hand \( N \) and \( N' \) are nilpotent and commute, hence so do \( N' \) and \( -N \). Say \( N^{a} = 0 \) and \( (N')^{b} = 0 \) with \( a, b \ge 1 \), and put \( s = a + b - 1 \). By distributivity, \( X^{s} = (N' - N)^{s} \) is the sum of the \( 2^{s} \) products of \( s \) factors, each factor \( N' \) or \( -N \); since the two commute, each product can be rearranged, one adjacent swap at a time, into \( \pm (N')^{i}N^{\,s-i} \), where \( i \) counts the factors equal to \( N' \). If \( i \ge b \), then \( (N')^{i} = 0 \); and if \( i \le b - 1 \), then \( s - i \ge s - b + 1 = a \), so \( N^{\,s-i} = 0 \). Either way the product is \( 0 \), so \( X^{s} = 0 \) and \( X \) is nilpotent.

So \( X \) is diagonalizable and nilpotent. Being nilpotent, \( \spec(X) = \{0\} \) (@prp-nilpotent-basic (c)); being diagonalizable, \( [X]_{\sD} \) is diagonal with the eigenvalues of \( X \) on the diagonal for some basis \( \sD \) (@thm-diagonalization), so \( [X]_{\sD} = 0 \) and \( X = 0 \). Hence \( S' = S \) and, subtracting from \( T \), \( N' = N \). This proves the theorem.
:::

::: {.warning}
**Splitting a matrix into its diagonal part and its off-diagonal part is *not* the Jordan–Chevalley decomposition.** For \( \A = \begin{pmatrix} 1 & 1 \\ 0 & 2\end{pmatrix} \), the "obvious" split is \( \D = \diag(1, 2) \) plus \( \E = \begin{pmatrix} 0 & 1 \\ 0 & 0\end{pmatrix} \). Here \( \D \) is diagonal and \( \E \) is nilpotent, but
\[
\D \E = \begin{pmatrix} 0 & 1 \\ 0 & 0\end{pmatrix} \ne \begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix} = \E \D ,
\]
so the commuting requirement fails, and the split is not the one the theorem produces. Indeed \( \A \) has distinct eigenvalues, so it is diagonalizable (@cor-distinct-eigenvalues-diagonalizable) and its actual decomposition is \( \S = \A \), \( \N = 0 \). The off-diagonal part of a matrix is a feature of the basis; the nilpotent part is a feature of the operator.
:::

The formulas in the proof are also the recipe: build the projections \( \pi_i \) onto the generalized eigenspaces — by Bézout, as in @exm-primary-decomposition — and set \( S = \sum_i\lambda_i\pi_i \).

::: {#exm-jordan-chevalley-3x3}
[The Semisimple and Nilpotent Parts of a \( 3 \times 3 \) Matrix]

Let
\[
\A = \begin{pmatrix} 2 & 2 & -1 \\ -1 & 3 & -1 \\ -1 & -1 & 2 \end{pmatrix} \in M_3(\nQ), \qquad p_{\A} = (x - 2)^2(x - 3).
\]
Find the Jordan–Chevalley decomposition \( \A = \S + \N \), and exhibit \( \S \) and \( \N \) as polynomials in \( \A \).
:::

::: {.solution}
*The minimal polynomial.* Put \( \B = \A - 2\I = \begin{pmatrix} 0 & 2 & -1 \\ -1 & 1 & -1 \\ -1 & -1 & 0\end{pmatrix} \). Then
\[
\B(\A - 3\I) = \begin{pmatrix} 0 & 2 & -1 \\ -1 & 1 & -1 \\ -1 & -1 & 0\end{pmatrix}\begin{pmatrix} -1 & 2 & -1 \\ -1 & 0 & -1 \\ -1 & -1 & -1\end{pmatrix} = \begin{pmatrix} -1 & 1 & -1 \\ 1 & -1 & 1 \\ 2 & -2 & 2 \end{pmatrix} \ne 0,
\]
so \( m_{\A} \ne (x-2)(x-3) \); since \( m_{\A} \mid p_{\A} \) and \( m_{\A} \) has both \( 2 \) and \( 3 \) as roots (@thm-minimal-polynomial-roots), \( m_{\A} = (x-2)^2(x-3) \). The primary factors are \( (x-2)^2 \) and \( x - 3 \).

*Bézout.* Dividing, \( (x-2)^2 = x^2 - 4x + 4 = (x-3)(x-1) + 1 \), so
\[
1 \cdot (x-2)^2 - (x-1)(x-3) = 1 .
\]
Following @thm-kernel-splitting with \( p = (x-2)^2 \) and \( q = x-3 \): the projection onto \( \ker q(\A) = G_3(\A) \) along \( \ker p(\A) = G_2(\A) \) is \( \pi_3 = (\A - 2\I)^2 = \B^2 \), and \( \pi_2 = \I - \B^2 \).

*Compute.* Squaring,
\[
\B^2 = \begin{pmatrix} -1 & 3 & -2 \\ 0 & 0 & 0 \\ 1 & -3 & 2 \end{pmatrix}, \qquad \text{and } \B^3 = \B^2 \text{ (as } \B^2(\B - \I) = 0).
\]
Hence
\[
\begin{aligned}
\S = 2\pi_2 + 3\pi_3 &= 2\I + \B^2 = \begin{pmatrix} 1 & 3 & -2 \\ 0 & 2 & 0 \\ 1 & -3 & 4\end{pmatrix}, \\
\N = \A - \S &= \B - \B^2 = \begin{pmatrix} 1 & -1 & 1 \\ -1 & 1 & -1 \\ -2 & 2 & -2 \end{pmatrix}.
\end{aligned}
\]

*The checks.* First \( \S + \N = \A \) by construction. Next \( \N^2 = 0 \): reading the rows of \( \N \) as multiples of \( (1, -1, 1) \) shows that \( \N = \u\w\tp \) with \( \u = (1, -1, -2) \) and \( \w = (1, -1, 1) \), and \( \w\tp\u = 1 + 1 - 2 = 0 \), so \( \N^2 = \u(\w\tp\u)\w\tp = 0 \). Next \( \S \) is diagonalizable: \( (\S - 2\I)(\S - 3\I) = \B^2(\B^2 - \I) = \B^4 - \B^2 = 0 \), because \( \B^3 = \B^2 \) gives \( \B^4 = \B^2 \); so \( m_{\S} \) divides a product of distinct linear factors and \( \S \) is diagonalizable (@thm-diagonalizable-iff-minimal-distinct-linear). Finally \( \S \N = \N \S \), since both are polynomials in \( \A \): explicitly \( \S = 2\I + (\A-2\I)^2 \) and \( \N = (\A - 2\I) - (\A-2\I)^2 \), that is,
\[
\begin{aligned}
\S &= g(\A) \text{ with } g = x^2 - 4x + 6, \\
\N &= h(\A) \text{ with } h = -x^2 + 5x - 6 = -(x-2)(x-3) .
\end{aligned}
\]
As a cross-check, \( g + h = x \), so \( g(\A) + h(\A) = \A \); and \( \tr \S = 1 + 2 + 4 = 7 = 2 + 2 + 3 \) is the sum of the eigenvalues of \( \A \), while \( \tr \N = 1 + 1 - 2 = 0 \), as it must be for a nilpotent matrix (@prp-nilpotent-basic (c) and @thm-trace-det-eigenvalues).
:::

Two consequences are worth naming now. Because \( S \) and \( N \) are polynomials in \( T \), **every operator commuting with \( T \) automatically commutes with \( S \) and with \( N \)**. And the decomposition is exactly what makes functions of matrices computable in the next section: any reasonable function \( f \) will satisfy \( f(T) = f(S + N) \) with the two parts handled separately, \( S \) by its eigenvalues and \( N \) by finitely many terms, since its powers stop.

::: {.remark}
The splitting exists in greater generality. Over a perfect field, every \( T \) can be written uniquely as \( T = S + N \) with \( S \) **semisimple** in the sense of @def-semisimple-operator, \( N \) nilpotent and \( SN = NS \); the proof runs through the primary decomposition of \( m_T \) into powers of general irreducibles instead of linear ones. We prove only the split case, which is all we use.
:::

## Exercises

### A. Check your understanding

:::: {#exr-jordan-chevalley-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define a semisimple operator, and say how the definition specializes to Chapter 8's criterion for diagonalizability.
2. State the Jordan–Chevalley Decomposition Theorem, including all three conditions on \( S \) and \( N \) and the uniqueness clause.
3. True or false: \( \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \in M_2(\nR) \) is semisimple. Justify your answer.
4. True or false: if \( \A = \D + \E \) with \( \D \) the diagonal part of \( \A \) and \( \E \) the off-diagonal part, then \( \D \) is the semisimple part of \( \A \). Justify your answer.
5. Which hypothesis of the uniqueness clause does the pair \( (\D, \E) \) of part (d) typically violate?
6. Why does every operator commuting with \( T \) commute with the semisimple part of \( T \)?
:::
::::

::: {.solution}
(a) \( T \) is semisimple if \( m_T \) is a product of **distinct monic irreducible** polynomials over \( F \) (@def-semisimple-operator). Requiring those irreducibles to be **linear** gives @thm-diagonalizable-iff-minimal-distinct-linear, the criterion for diagonalizability. So diagonalizable \( \Rightarrow \) semisimple, and the converse holds when \( m_T \) splits.

(b) If \( p_T \) splits, then \( T = S + N \) with \( S \) diagonalizable, \( N \) nilpotent and \( SN = NS \); such \( S \) and \( N \) are unique, and both are polynomials in \( T \) (@thm-jordan-chevalley).

(c) True. Its minimal polynomial is \( x^2 + 1 \), which has no real root and so is irreducible over \( \nR \) (@thm-irreducible-deg-2-3); one irreducible factor, exponent \( 1 \).

(d) False. For \( \A = \begin{pmatrix} 1 & 1 \\ 0 & 2\end{pmatrix} \) the semisimple part is \( \A \) itself, since \( \A \) is diagonalizable, whereas \( \D = \diag(1,2) \ne \A \).

(e) The commuting condition \( \D \E = \E \D \); see the warning after @thm-jordan-chevalley.

(f) Because \( S = g(T) \) for some polynomial \( g \) (@thm-jordan-chevalley (a)), and an operator commuting with \( T \) commutes with every power of \( T \), hence with every polynomial in \( T \).
:::

### B. Practice

:::: {#exr-jordan-chevalley-b1}
[B1: Semisimple and nilpotent parts]

For each matrix over \( \nQ \), find the Jordan–Chevalley decomposition \( \A = \S + \N \) and express \( \S \) as a polynomial in \( \A \).

::: {.enumerate options="label=(\alph*)"}
1. \( \A_1 = \begin{pmatrix} 3 & 1 \\ 0 & 3\end{pmatrix} \).
2. \( \A_2 = \begin{pmatrix} 1 & 2 \\ 0 & 3\end{pmatrix} \).
3. \( \A_3 = \begin{pmatrix} 2 & 1 & 3 \\ 0 & 2 & 0 \\ 0 & 0 & 5 \end{pmatrix} \).
:::
::::

::: {.solution}
(a) \( m_{\A_1} = (x-3)^2 \), so there is one eigenvalue and \( G_3 = \nQ^2 \); the projection onto it is \( \I \). Hence \( \S = 3\I \) and \( \N = \A_1 - 3\I = \begin{pmatrix} 0 & 1 \\ 0 & 0\end{pmatrix} \), with \( \N^2 = 0 \). As a polynomial, \( \S = 3\I = g(\A_1) \) with \( g = 3 \) the constant polynomial. (Every scalar multiple of \( \I \) is diagonalizable, and \( \S \) commutes with everything.)

(b) \( \A_2 \) has the distinct eigenvalues \( 1 \) and \( 3 \), so it is diagonalizable (@cor-distinct-eigenvalues-diagonalizable). By uniqueness, \( \S = \A_2 \) and \( \N = 0 \); here \( g = x \). The naive split into \( \diag(1,3) \) and \( \begin{pmatrix} 0 & 2 \\ 0 & 0\end{pmatrix} \) is **not** the Jordan–Chevalley decomposition.

(c) \( p_{\A_3} = (x-2)^2(x-5) \). Put \( \M = \A_3 - 2\I = \begin{pmatrix} 0 & 1 & 3 \\ 0 & 0 & 0 \\ 0 & 0 & 3\end{pmatrix} \). Then \( \M(\A_3 - 5\I) \) has \( (1,2) \)-entry \( -3 \ne 0 \), so \( m_{\A_3} = (x-2)^2(x-5) \). Bézout: \( (x-2)^2 = (x-5)(x+1) + 9 \), so \( \tfrac19(x-2)^2 - \tfrac19(x+1)(x-5) = 1 \), and by @thm-kernel-splitting the projection onto \( G_5 \) along \( G_2 \) is \( \pi_5 = \tfrac19 \M^2 \). Computing \( \M^2 = \begin{pmatrix} 0 & 0 & 9 \\ 0 & 0 & 0 \\ 0 & 0 & 9\end{pmatrix} \),
\[
\S = 2\I + 3\pi_5 = 2\I + \tfrac13\M^2 = \begin{pmatrix} 2 & 0 & 3 \\ 0 & 2 & 0 \\ 0 & 0 & 5\end{pmatrix}, \qquad \N = \A_3 - \S = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0\end{pmatrix}.
\]
Checks: \( \N^2 = 0 \); \( \S - 2\I \) has rank \( 1 \), so \( g_{\S}(2) = 2 = a_{\S}(2) \) and \( \S \) is diagonalizable (@thm-diagonalization); and \( \S \N = \begin{pmatrix} 0 & 2 & 0 \\ 0&0&0\\0&0&0\end{pmatrix} = \N \S \). As a polynomial, \( \S = 2\I + \tfrac13(\A_3 - 2\I)^2 = g(\A_3) \) with \( g = \tfrac13x^2 - \tfrac43x + \tfrac{10}{3} \). Note that \( \S \) keeps the entry \( 3 \) in position \( (1,3) \): the diagonal part of \( \A_3 \) is the wrong answer, and it does not commute with the rest, since \( \diag(2,2,5)(\A_3 - \diag(2,2,5)) \) and the reverse product differ in position \( (1,3) \) by \( -9 \).
:::

:::: {#exr-jordan-chevalley-b2}
[B2: When is the nilpotent part zero?]

Let \( V \) be finite-dimensional with \( \dim V \ge 1 \) and let \( T \in \cL(V) \) with \( p_T \) split, with Jordan–Chevalley decomposition \( T = S + N \). Prove that \( N = 0 \) if and only if \( T \) is diagonalizable, and that \( S = 0 \) if and only if \( T \) is nilpotent.
::::

::: {.solution}
If \( N = 0 \), then \( T = S \) is diagonalizable. Conversely, if \( T \) is diagonalizable, then \( T = T + 0 \) is a decomposition into a diagonalizable and a nilpotent part that commute (\( T \cdot 0 = 0 = 0 \cdot T \)), so by the uniqueness in @thm-jordan-chevalley, \( S = T \) and \( N = 0 \).

If \( S = 0 \), then \( T = N \) is nilpotent. Conversely, if \( T \) is nilpotent, then \( T = 0 + T \) is such a decomposition, since the zero operator is diagonalizable and commutes with \( T \); uniqueness gives \( S = 0 \) and \( N = T \).
:::

:::: {#exr-jordan-chevalley-b3}
[B3: Block diagonal matrices]

Let \( \A_1 \in M_p(F) \) and \( \A_2 \in M_q(F) \) have split characteristic polynomials, with Jordan–Chevalley decompositions \( \A_i = \S_i + \N_i \). Prove that the Jordan–Chevalley decomposition of \( \A_1 \oplus \A_2 \) is
\[
\A_1 \oplus \A_2 = (\S_1 \oplus \S_2) + (\N_1 \oplus \N_2).
\]
::::

::: {.solution}
Write \( \S = \S_1 \oplus \S_2 \) and \( \N = \N_1 \oplus \N_2 \). By @thm-block-diagonal-arithmetic (a), \( \S + \N = (\S_1 + \N_1) \oplus (\S_2 + \N_2) = \A_1 \oplus \A_2 \). Also \( p_{\A_1 \oplus \A_2} = p_{\A_1}p_{\A_2} \) splits (@thm-det-block-triangular, applied over \( F[x] \) as the remark after it allows), so @thm-jordan-chevalley applies to \( \A_1 \oplus \A_2 \) and it suffices, by uniqueness, to check the three conditions.

*\( \S \) is diagonalizable.* Pick invertible \( \P_i \) with \( \P_i^{-1}\S_i\P_i \) diagonal. Then \( \P = \P_1 \oplus \P_2 \) is invertible with \( \P^{-1} = \P_1^{-1} \oplus \P_2^{-1} \), and \( \P^{-1}\S\P = (\P_1^{-1}\S_1\P_1) \oplus (\P_2^{-1}\S_2\P_2) \) is diagonal (@thm-block-diagonal-arithmetic (a), (c)).

*\( \N \) is nilpotent.* If \( \N_1^{a} = 0 \) and \( \N_2^{b} = 0 \), then \( \N^{\max(a,b)} = \N_1^{\max(a,b)} \oplus \N_2^{\max(a,b)} = 0 \) by @thm-block-diagonal-arithmetic (b).

*They commute.* \( \S \N = (\S_1\N_1) \oplus (\S_2\N_2) = (\N_1\S_1) \oplus (\N_2\S_2) = \N \S \), again by @thm-block-diagonal-arithmetic (a).

By the uniqueness in @thm-jordan-chevalley, \( \S \) and \( \N \) are the semisimple and nilpotent parts of \( \A_1 \oplus \A_2 \).
:::

### C. Going deeper

:::: {#exr-jordan-chevalley-c1}
[C1: The multiplicative version]

Call \( U \in \cL(V) \) **unipotent** if \( U - \id_V \) is nilpotent. Let \( T \in \cL(V) \) be **invertible** with \( p_T \) split, and let \( T = S + N \) be its Jordan–Chevalley decomposition.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( S \) is invertible.
2. Prove that \( S^{-1} \) commutes with \( N \), and that \( S^{-1}N \) is nilpotent.
3. Deduce that \( T = SU \) with \( S \) diagonalizable, \( U \) unipotent and \( SU = US \).
4. Prove that this multiplicative decomposition is unique: if \( T = S'U' \) with \( S' \) diagonalizable, \( U' \) unipotent and \( S'U' = U'S' \), then \( S' = S \) and \( U' = U \).
:::

*Hint: for (d), turn the multiplicative statement into an additive one by writing \( T = S' + S'(U' - \id_V) \).*
::::

::: {.solution}
(a) By the proof of @thm-jordan-chevalley, \( S\v = \lambda_i\v \) for every \( \v \in G_{\lambda_i}(T) \), so \( \spec(S) = \spec(T) \) — a basis of eigenvectors of \( S \) with these eigenvalues was exhibited there. Since \( T \) is invertible, \( 0 \notin \spec(T) \) (@thm-invertible-tfae-eigen), so \( 0 \notin \spec(S) \) and \( S \) is invertible.

(b) From \( SN = NS \), multiply on both sides by \( S^{-1} \): \( S^{-1}(SN)S^{-1} = S^{-1}(NS)S^{-1} \) gives \( NS^{-1} = S^{-1}N \). Hence \( (S^{-1}N)^{j} = S^{-j}N^{j} \) for every \( j \ge 1 \), by induction using \( NS^{-1} = S^{-1}N \). With \( N^{s} = 0 \) we get \( (S^{-1}N)^{s} = 0 \).

(c) Put \( U = \id_V + S^{-1}N \). Then \( SU = S + N = T \), and \( U - \id_V = S^{-1}N \) is nilpotent by (b), so \( U \) is unipotent. They commute: \( SU = S + N = US \), since \( S(S^{-1}N) = N = (S^{-1}N)S \) by (b).

(d) Suppose \( T = S'U' \) with \( S' \) diagonalizable, \( U' \) unipotent and \( S'U' = U'S' \). Put \( N' = S'(U' - \id_V) \), so that \( T = S' + N' \). Then \( N' \) is nilpotent: \( S' \) commutes with \( U' \), hence with \( U' - \id_V \), so \( (N')^{j} = (S')^{j}(U' - \id_V)^{j} = 0 \) once \( j \) is large. And \( S'N' = S'S'(U'-\id_V) = S'(U'-\id_V)S' = N'S' \). So \( T = S' + N' \) satisfies the hypotheses of @thm-jordan-chevalley (b), giving \( S' = S \) and \( N' = N \). Then \( U' - \id_V = (S')^{-1}N' = S^{-1}N = U - \id_V \), so \( U' = U \).
:::

:::: {#exr-jordan-chevalley-c2}
[C2: The parts inherit every symmetry]

Let \( V \) be finite-dimensional with \( \dim V \ge 1 \), let \( T \in \cL(V) \) with \( p_T \) split, and let \( T = S + N \) be its Jordan–Chevalley decomposition.

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( X \in \cL(V) \) satisfies \( XT = TX \), then \( XS = SX \) and \( XN = NX \).
2. Deduce that every \( T \)-invariant subspace is \( S \)-invariant and \( N \)-invariant, and that \( S \) and \( N \) map each \( G_\lambda(T) \) into itself.
3. Give an example of a diagonalizable \( S \) and a nilpotent \( N \) with \( SN \ne NS \) for which \( S + N \) is **not** the operator whose semisimple part is \( S \). (So the commuting hypothesis cannot be dropped from the uniqueness statement.)
:::
::::

::: {.solution}
(a) By @thm-jordan-chevalley (a), \( S = g(T) \) and \( N = h(T) \) for some \( g, h \in F[x] \). From \( XT = TX \) we get \( XT^{j} = T^{j}X \) for all \( j \ge 0 \) by induction, hence \( Xf(T) = f(T)X \) for every \( f \in F[x] \) by taking linear combinations. Applying this to \( f = g \) and \( f = h \) gives \( XS = SX \) and \( XN = NX \).

(b) Let \( U \subseteq V \) be \( T \)-invariant. Then \( U \) is \( T^{j} \)-invariant for every \( j \), hence \( f(T) \)-invariant for every \( f \in F[x] \) (a sum of vectors of \( U \) lies in \( U \)); taking \( f = g, h \) gives that \( U \) is \( S \)- and \( N \)-invariant. In particular \( G_\lambda(T) = \ker(T - \lambda\,\id_V)^{n} \) is \( T \)-invariant (@cor-generalized-eigenspace-is-kernel (b)), so \( S \) and \( N \) map it into itself.

(c) Take \( \S = \diag(1, 2) \) and \( \N = \begin{pmatrix} 0 & 1 \\ 0 & 0\end{pmatrix} \) in \( M_2(\nQ) \). Then \( \S \) is diagonal, \( \N^2 = 0 \), and \( \S \N = \begin{pmatrix} 0&1\\0&0\end{pmatrix} \ne \begin{pmatrix} 0&2\\0&0\end{pmatrix} = \N \S \). Their sum \( \A = \begin{pmatrix} 1 & 1 \\ 0 & 2\end{pmatrix} \) has distinct eigenvalues, so it is diagonalizable, and its semisimple part is \( \A \) itself, not \( \S \), with nilpotent part \( 0 \), not \( \N \) (@exr-jordan-chevalley-b2). Without the commuting hypothesis, an operator can be written as "diagonalizable plus nilpotent" in many ways: for any \( c \in \nQ \), \( \A = \begin{pmatrix} 1 & c \\ 0 & 2\end{pmatrix} + \begin{pmatrix} 0 & 1 - c \\ 0 & 0\end{pmatrix} \) is such a splitting, the first summand being diagonalizable because its eigenvalues \( 1, 2 \) are distinct.
:::
