# Polynomials of an Operator

Chapter 3 taught us to substitute an operator into a polynomial: for \( T \in \cL(V) \) and \( p \in F[x] \), the operator \( p(T) \) replaces each \( x^k \) by \( T^k \) (@def-polynomial-of-operator). That section used the idea for a few examples. With the arithmetic of this chapter in hand, the idea becomes a method. Divisibility, ideals and Bézout's identity in \( F[x] \) turn into statements about \( T \): every operator on a finite-dimensional space satisfies a polynomial equation, the polynomials it satisfies form an ideal, and a factorization of such a polynomial into coprime pieces splits the space. The last statement, the kernel splitting lemma, is the engine that Chapter 8 will run to take operators apart.

## Evaluating at an operator

Fix \( T \in \cL(V) \), where \( V \) is any vector space over \( F \). @thm-polynomial-of-operator-properties already says that substituting \( T \) respects sums and products of polynomials, and that any two polynomials in \( T \) commute. The new point of view is to treat "substitute \( T \)" as a single map from \( F[x] \) to \( \cL(V) \), and to ask what it preserves. Both sides are vector spaces, and both have a multiplication. The map respects all of the structure.

::: {#thm-evaluation-homomorphism}
[Evaluation at an Operator]

Let \( V \) be a vector space over \( F \) and \( T \in \cL(V) \). Then the map
\[
F[x] \to \cL(V), \qquad p \mapsto p(T),
\]
has the following properties.

::: {.enumerate options="label=(\alph*)"}
1. It is **linear**: \( (cp + q)(T) = c\,p(T) + q(T) \) for all \( p, q \in F[x] \) and \( c \in F \).
2. It is **multiplicative** and sends \( 1 \) to \( \id_V \): \( (pq)(T) = p(T)\,q(T) \) and \( 1(T) = \id_V \).
3. Its image \( \{ p(T) : p \in F[x] \} \) is a subspace of \( \cL(V) \), closed under composition, in which any two operators commute.
4. If \( S \in \cL(V) \) commutes with \( T \), then \( S \) commutes with \( p(T) \) for every \( p \in F[x] \).
:::
:::

::: {.proof}
(a) Let \( p = \sum_k a_kx^k \) and \( q = \sum_k b_kx^k \). The coefficient of \( x^k \) in \( cp + q \) is \( ca_k + b_k \), so by @def-polynomial-of-operator and the vector space laws in \( \cL(V) \) (@thm-linear-maps-vector-space),
\[
(cp + q)(T) = \sum_k (ca_k + b_k)T^k = c\sum_k a_kT^k + \sum_k b_kT^k = c\,p(T) + q(T).
\]

(b) The product rule is @thm-polynomial-of-operator-properties (b). The constant polynomial \( 1 \) gives \( 1 \cdot T^0 = \id_V \).

(c) The image of a linear map is a subspace (@thm-prop-image). For polynomials \( p, q \), the composite \( p(T)q(T) \) equals \( (pq)(T) \) by (b), so it lies in the image, and \( p(T)q(T) = q(T)p(T) \) by @thm-polynomial-of-operator-properties (c).

(d) Suppose \( ST = TS \). We show \( ST^k = T^kS \) by induction on \( k \). For \( k = 0 \), both sides are \( S \). If \( ST^k = T^kS \), then by associativity (@thm-composition-linear)
\[
ST^{k+1} = (ST^k)T = T^k(ST) = T^k(TS) = T^{k+1}S .
\]
For \( p = \sum_k a_kx^k \), distributivity (@thm-composition-linear) gives \( S\,p(T) = \sum_k a_k\,ST^k = \sum_k a_k\,T^kS = p(T)\,S \).
:::

Parts (a) and (b) together say that \( p \mapsto p(T) \) is a **homomorphism of algebras**: it translates every identity built from sums, scalar multiples and products of polynomials into the same identity for operators. (This map should not be confused with the evaluation map \( V \to V^{**} \) of Chapter 4; here we evaluate polynomials, not functionals.) Part (d) is what we will use most. It says that anything commuting with \( T \) commutes with the whole family of polynomials in \( T \).

For matrices nothing new is needed. If \( V \) is finite-dimensional with basis \( \sB \), then \( [p(T)]_{\sB} = p([T]_{\sB}) \) by @cor-matrix-of-polynomial-of-operator. So every statement in this section holds verbatim for \( \A \in M_n(F) \), applied to the operator \( T_{\A} \).

::: {#exm-polynomial-of-2x2}
[Two Ways to Evaluate]

Let \( \A = \begin{pmatrix} 3 & 1 \\ -1 & 1 \end{pmatrix} \in M_2(\nQ) \). Compute \( p(\A) \) for \( p = x^2 - 4x + 4 \) and \( q = x^2 - 3x \), once by expanding and once by factoring.
:::

::: {.solution}
*Expanding.* \( \A^2 = \begin{pmatrix} 9 - 1 & 3 + 1 \\ -3 - 1 & -1 + 1 \end{pmatrix} = \begin{pmatrix} 8 & 4 \\ -4 & 0 \end{pmatrix} \). Hence
\[
p(\A) = \begin{pmatrix} 8 - 12 + 4 & 4 - 4 \\ -4 + 4 & 0 - 4 + 4 \end{pmatrix} = 0, \qquad
q(\A) = \begin{pmatrix} 8 - 9 & 4 - 3 \\ -4 + 3 & 0 - 3 \end{pmatrix} = \begin{pmatrix} -1 & 1 \\ -1 & -3 \end{pmatrix}.
\]
*Factoring.* \( p = (x - 2)^2 \), so \( p(\A) = (\A - 2\I)^2 \) by @thm-evaluation-homomorphism (b). Here \( \A - 2\I = \begin{pmatrix} 1 & 1 \\ -1 & -1 \end{pmatrix} \), whose square is \( \begin{pmatrix} 1 - 1 & 1 - 1 \\ -1 + 1 & -1 + 1 \end{pmatrix} = 0 \). Likewise \( q = x(x - 3) \), so
\[
q(\A) = \A(\A - 3\I) = \begin{pmatrix} 3 & 1 \\ -1 & 1 \end{pmatrix}\begin{pmatrix} 0 & 1 \\ -1 & -2 \end{pmatrix} = \begin{pmatrix} -1 & 1 \\ -1 & -3 \end{pmatrix},
\]
in agreement with the expansion. The factored form showed at a glance why \( p(\A) = 0 \): the matrix \( \A - 2\I \) squares to zero.
:::

::: {.warning}
**A product of polynomials in \( T \) can vanish without either factor vanishing.** In \( F[x] \), \( pq = 0 \) forces \( p = 0 \) or \( q = 0 \) (@cor-polynomial-no-zero-divisors). Evaluation at \( T \) does not carry this over. For the projection \( P(x, y) = (x, 0) \) on \( F^2 \), the polynomials \( p = x \) and \( q = x - 1 \) give \( p(P)\,q(P) = P^2 - P = 0 \), while \( p(P) = P \ne 0 \) and \( q(P) = P - \id \ne 0 \). The map \( p \mapsto p(T) \) respects products, but it is not injective, and it is exactly its kernel that makes this possible.
:::

## Annihilating polynomials

In Chapter 3 we saw operators satisfying polynomial equations: a projection satisfies \( P^2 - P = 0 \), the rotation of \( \nR^2 \) by a right angle satisfies \( R^2 + \id = 0 \) (@exm-operator-polynomial-relations), and differentiation on \( F[x]_{\le n} \) satisfies \( D^{n+1} = 0 \) (@exm-differentiation-nilpotent). Each such equation is a non-zero polynomial in the kernel of \( p \mapsto p(T) \). Does every operator have one? We need a word for these polynomials.

::: {#def-annihilating-polynomial}
[Annihilating Polynomial]

Let \( T \in \cL(V) \). A polynomial \( p \in F[x] \) **annihilates** \( T \) if \( p(T) = 0 \), the zero operator on \( V \).
:::

For example, \( x^2 - x \) annihilates every projection, \( x^2 + 1 \) annihilates the rotation \( R \), and the zero polynomial annihilates every operator. On the zero space \( V = \{\0\} \), even the constant \( 1 \) annihilates \( T \), because \( 1(T) = \id_V \) is the zero map there. On \( V \ne \{\0\} \), a non-zero constant \( c \) never annihilates, since \( c\,\id_V \ne 0 \). (The word "annihilate" is also used for the annihilator \( U^0 \) of Chapter 4; the two uses share the idea "sends to zero" and nothing more.)

In finite dimension a counting argument settles existence. The space \( \cL(V) \) is finite-dimensional, so the powers of \( T \) cannot all be independent.

::: {#thm-annihilating-polynomial-exists}
[Every Operator Satisfies a Polynomial]

Let \( V \) be a finite-dimensional vector space over \( F \) with \( \dim V = n \), and let \( T \in \cL(V) \). Then there is a **non-zero** \( p \in F[x] \) with \( \deg p \le n^2 \) and \( p(T) = 0 \). The same holds for every \( \A \in M_n(F) \).
:::

::: {.proof}
If \( n = 0 \), the constant \( 1 \) works, as noted above. Let \( n \ge 1 \). By @thm-linear-maps-isomorphic-to-matrices, \( \dim \cL(V) = n \cdot n = n^2 \). The list \( (\id_V, T, T^2, \dots, T^{n^2}) \) in \( \cL(V) \) has length \( n^2 + 1 > n^2 \), so it is linearly dependent by @thm-size-bounds (a). Hence there are \( a_0, \dots, a_{n^2} \in F \), **not all zero**, with \( a_0\id_V + a_1T + \dots + a_{n^2}T^{n^2} = 0 \). The polynomial \( p = a_0 + a_1x + \dots + a_{n^2}x^{n^2} \) is non-zero, has degree at most \( n^2 \), and satisfies \( p(T) = 0 \) by @def-polynomial-of-operator. For \( \A \in M_n(F) \), apply the same argument in \( M_n(F) \), which has dimension \( n^2 \) (@exm-dimensions).
:::

The bound \( n^2 \) is crude. In Chapter 8, the Cayley–Hamilton Theorem will produce an annihilating polynomial of degree exactly \( n \). The finite dimension is essential: on \( F[x] \), let \( S \) be multiplication by \( x \), \( S(f) = xf \). Then \( S^k(1) = x^k \), so \( p(S)(1) = p \) for every \( p \in F[x] \), and \( p(S) \ne 0 \) whenever \( p \ne 0 \).

The proof is also an algorithm: search for the first power of \( \A \) that is a combination of the earlier ones. This is a question about linear dependence, which elimination answers (@thm-independence-spanning-by-rank).

::: {#exm-annihilating-polynomial-3x3}
[Finding an Annihilating Polynomial]

Find a non-zero polynomial of least possible degree that annihilates \( \B = \begin{pmatrix} 2 & 1 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \in M_3(\nQ) \).
:::

::: {.solution}
*Degree \( 1 \).* \( \B \) is not a scalar multiple of \( \I_3 \) (its \( (1, 2) \)-entry is non-zero), so \( (\I_3, \B) \) is independent, and no non-zero polynomial of degree at most \( 1 \) annihilates \( \B \).

*Degree \( 2 \).* Compute
\[
\B^2 = \begin{pmatrix} 4 & 3 & 3 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}.
\]
We look for \( a, b, c \) with \( a\I_3 + b\B + c\B^2 = 0 \). Reading entries: position \( (1, 2) \) gives \( b + 3c = 0 \); position \( (1, 1) \) gives \( a + 2b + 4c = 0 \); position \( (2, 2) \) gives \( a + b + c = 0 \). The positions \( (1, 3) \) and \( (3, 3) \) repeat the \( (1, 2) \) and \( (2, 2) \) equations, and all other entries are \( 0 = 0 \). With \( c = 1 \): \( b = -3 \) and \( a = 2 \), and indeed \( 2 - 6 + 4 = 0 \). So
\[
\B^2 - 3\B + 2\I_3 = 0,
\]
and \( p = x^2 - 3x + 2 = (x - 1)(x - 2) \) annihilates \( \B \). Check with the factored form: \( \B - \I_3 = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} \) and \( \B - 2\I_3 = \begin{pmatrix} 0 & 1 & 1 \\ 0 & -1 & 0 \\ 0 & 0 & -1 \end{pmatrix} \), whose product is \( \begin{pmatrix} 0 & 1 - 1 & 1 - 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} = 0 \).

The bound of @thm-annihilating-polynomial-exists allowed degree \( 9 \); the search stopped at degree \( 2 \).
:::

Annihilating polynomials are far from unique: if \( p \) annihilates \( T \), so does every multiple \( qp \), since \( (qp)(T) = q(T)p(T) = q(T) \cdot 0 = 0 \). In @exm-annihilating-polynomial-3x3, \( x^3 - 3x^2 + 2x \) annihilates \( \B \) too. This closure under multiplication is the defining property of an ideal, and ideals of \( F[x] \) are completely understood (@thm-ideals-principal).

::: {#thm-annihilator-ideal}
[The Annihilating Polynomials Form an Ideal]

Let \( V \) be a vector space over \( F \) and \( T \in \cL(V) \), and let
\[
I_T \coloneqq \{ p \in F[x] : p(T) = 0 \}.
\]

::: {.enumerate options="label=(\alph*)"}
1. \( I_T \) is an ideal of \( F[x] \).
2. Either \( I_T = \{0\} \), or there is a **unique monic** \( m \in F[x] \) with \( I_T = \langle m \rangle \). In the second case, for every \( p \in F[x] \),
   \[
   p(T) = 0 \iff m \mid p ,
   \]
   and \( m \) has the least degree among the non-zero polynomials annihilating \( T \).
3. If \( V \) is finite-dimensional, then \( I_T \ne \{0\} \), and \( \deg m \le (\dim V)^2 \).
:::
:::

::: {.proof}
(a) By @thm-evaluation-homomorphism (a), \( I_T \) is the kernel of a linear map, so it is a subspace (@thm-prop-kernel); in particular it contains \( 0 \) and is closed under addition. If \( p \in I_T \) and \( q \in F[x] \), then \( (qp)(T) = q(T)\,p(T) = 0 \) by @thm-evaluation-homomorphism (b), so \( qp \in I_T \). By @def-ideal-polynomials, \( I_T \) is an ideal.

(b) By @thm-ideals-principal, either \( I_T = \{0\} \), or \( I_T = \langle m \rangle \) for a unique monic \( m \), which has least degree among the non-zero elements of \( I_T \). In the second case, \( p(T) = 0 \) means \( p \in \langle m \rangle \), that is, \( p = qm \) for some \( q \), that is, \( m \mid p \).

(c) By @thm-annihilating-polynomial-exists, \( I_T \) contains a non-zero polynomial of degree at most \( (\dim V)^2 \). So \( I_T \ne \{0\} \), and \( \deg m \le (\dim V)^2 \) because \( m \) has the least degree.
:::

This monic generator is one of the most important invariants of an operator. **Chapter 8 names it the minimal polynomial of \( T \)** and relates its roots to eigenvalues; here it is simply "the monic generator of \( I_T \)". Part (b) turns every polynomial identity satisfied by \( T \) into a divisibility statement about one fixed polynomial.

**Examples.**

- **Projections.** Let \( P \) be a projection with \( P \ne 0 \) and \( P \ne \id_V \). Then \( x^2 - x = x(x - 1) \in I_P \), so the monic generator divides \( x(x - 1) \). By unique factorization (@thm-unique-factorization-polynomials), its monic divisors are \( 1 \), \( x \), \( x - 1 \) and \( x(x - 1) \). The first three do not annihilate \( P \): \( 1(P) = \id_V \ne 0 \), \( x(P) = P \ne 0 \) and \( (x - 1)(P) = P - \id_V \ne 0 \). So the generator is \( x^2 - x \).
- **Degenerate cases.** For the identity on \( V \ne \{\0\} \), the generator is \( x - 1 \); for the zero operator on \( V \ne \{\0\} \), it is \( x \); on \( V = \{\0\} \), it is \( 1 \).
- **The matrix \( \B \).** In @exm-annihilating-polynomial-3x3, no non-zero polynomial of degree at most \( 1 \) annihilates \( \B \), and \( x^2 - 3x + 2 \) does, so the generator is \( x^2 - 3x + 2 \).
- **Infinite dimension.** For multiplication by \( x \) on \( F[x] \), we saw that \( I_S = \{0\} \).

::: {.check}
Let \( R(x, y) = (-y, x) \) be the rotation of \( \nR^2 \) by a right angle. What is the monic generator of \( I_R \subseteq \nR[x] \)?
:::

::: {.solution}
\( R^2 = -\id \), so \( x^2 + 1 \in I_R \), and the generator divides \( x^2 + 1 \). Over \( \nR \), \( x^2 + 1 \) has no root, so its only monic divisors are \( 1 \) and \( x^2 + 1 \) (a monic divisor of degree \( 1 \) would be \( x - c \) with \( c \) a root). Since \( 1(R) = \id \ne 0 \), the generator is \( x^2 + 1 \).
:::

## Kernels of polynomials in \( T \)

The subspaces we can build from \( T \) and a polynomial \( p \) are \( \ker p(T) \) and \( \im p(T) \). For \( p = x - \lambda \), the kernel \( \ker(T - \lambda\id_V) \) consists of the vectors that \( T \) merely scales by \( \lambda \); for a projection, \( \ker P \) and \( \ker(P - \id_V) \) are the two pieces of the direct sum. These subspaces have a property that general subspaces lack: \( T \) does not move vectors out of them.

::: {#thm-kernel-image-of-polynomial-invariant}
[\( T \) Preserves Kernels and Images of Polynomials in \( T \)]

::: {.enumerate options="label=(\alph*)"}
1. Let \( R, S \in \cL(V) \) with \( SR = RS \). Then \( S\v \in \ker R \) for every \( \v \in \ker R \), and \( S\w \in \im R \) for every \( \w \in \im R \).
2. In particular, for \( T \in \cL(V) \) and \( p, q \in F[x] \), the operator \( q(T) \) maps \( \ker p(T) \) into \( \ker p(T) \) and \( \im p(T) \) into \( \im p(T) \). Taking \( q = x \): \( T \) maps \( \ker p(T) \) and \( \im p(T) \) into themselves.
:::
:::

::: {.proof}
(a) Let \( \v \in \ker R \). Then \( R(S\v) = S(R\v) = S\0 = \0 \), so \( S\v \in \ker R \). Let \( \w = R\u \in \im R \). Then \( S\w = S(R\u) = R(S\u) \in \im R \).

(b) By @thm-evaluation-homomorphism (c), \( q(T) \) commutes with \( p(T) \), so (a) applies with \( R = p(T) \) and \( S = q(T) \). For \( q = x \), \( q(T) = T \).
:::

In Chapter 8, a subspace that an operator maps into itself will be called an invariant subspace, and the notion will be developed properly there. For now the theorem is what matters: whenever \( U = \ker p(T) \), the rule \( \u \mapsto T\u \) is an operator on \( U \), and so is \( \u \mapsto q(T)\u \).

The inclusion can fail for subspaces not built from \( T \). For the rotation \( R \) of the check above, \( R \) moves the \( x \)-axis to the \( y \)-axis, so the \( x \)-axis is not of the form \( \ker p(R) \) or \( \im p(R) \) for any \( p \).

## The kernel splitting lemma

Chapter 3 contains two theorems with the same shape. A projection satisfies \( P(P - \id_V) = 0 \), and @thm-projection-direct-sum splits \( V \) as \( \im P \oplus \ker P \). An involution in characteristic not \( 2 \) satisfies \( (T - \id_V)(T + \id_V) = 0 \), and @thm-involution-decomposition splits \( V \) as \( \ker(T - \id_V) \oplus \ker(T + \id_V) \). In both, a polynomial annihilating \( T \) factors into two pieces with no common factor, and \( V \) is the direct sum of the kernels of the pieces. In both, the projections turned out to be polynomials in \( T \): \( P \) itself, and \( \frac12(\id_V + T) \). The general statement needs only the arithmetic of \( F[x] \).

::: {#thm-kernel-splitting}
[Kernel Splitting Lemma]

Let \( V \) be a vector space over \( F \), let \( T \in \cL(V) \), and let \( p, q \in F[x] \) be **coprime**. Choose \( a, b \in F[x] \) with \( ap + bq = 1 \) (@cor-bezout-polynomials), and put
\[
W = \ker (pq)(T), \qquad E_1 = b(T)\,q(T), \qquad E_2 = a(T)\,p(T).
\]
Then:

::: {.enumerate options="label=(\alph*)"}
1. \( W = \ker p(T) \oplus \ker q(T) \);
2. \( E_1 + E_2 = \id_V \), and for every \( \w \in W \), the splitting of \( \w \) in (a) is
   \[
   \w = E_1\w + E_2\w, \qquad E_1\w \in \ker p(T), \quad E_2\w \in \ker q(T);
   \]
   so \( E_1 \) maps \( W \) into \( W \) and acts on \( W \) as the projection onto \( \ker p(T) \) along \( \ker q(T) \), and \( E_2 \) acts on \( W \) as the projection onto \( \ker q(T) \) along \( \ker p(T) \);
3. in particular, if \( (pq)(T) = 0 \), then
   \[
   V = \ker p(T) \oplus \ker q(T),
   \]
   and the projections of \( V \) onto the two summands along each other are the polynomials \( (bq)(T) \) and \( (ap)(T) \) in \( T \).
:::
:::

::: {.idea}
Substitute \( T \) into Bézout's identity: \( \id_V = a(T)p(T) + b(T)q(T) \). Applied to a vector \( \w \), this writes \( \w = E_1\w + E_2\w \), and it does so for **every** vector of \( V \). Now look at the pieces. ① \( p(T) \) kills \( E_1\w = b(T)q(T)\w \), because \( p(T)b(T)q(T) = b(T)\,(pq)(T) \) and \( (pq)(T)\w = \0 \) for \( \w \in W \): the factor \( q \) in \( E_1 \) combines with \( p \) to the whole product. Symmetrically \( q(T) \) kills \( E_2\w \). ② If \( \w \) is killed by both \( p(T) \) and \( q(T) \), then both pieces are \( \0 \), so \( \w = \0 \). ③ Direct sum by the intersection criterion; the projections are read off from uniqueness. Coprimality enters only through the identity \( ap + bq = 1 \), and without it step ② has nothing to stand on.
:::

::: {.proof}
Since \( ap + bq = 1 \), @thm-evaluation-homomorphism gives
\[
\id_V = a(T)p(T) + b(T)q(T) = E_2 + E_1 .
\]
Throughout, polynomials in \( T \) commute with each other (@thm-evaluation-homomorphism (c)).

*The kernels lie in \( W \).* If \( p(T)\v = \0 \), then \( (pq)(T)\v = q(T)\,p(T)\v = \0 \); so \( \ker p(T) \subseteq W \), and likewise \( \ker q(T) \subseteq W \).

*The pieces.* Let \( \w \in W \). Then \( \w = \id_V\w = E_1\w + E_2\w \). Moreover
\[
p(T)(E_1\w) = p(T)\,b(T)\,q(T)\w = b(T)\,(pq)(T)\w = b(T)\0 = \0,
\]
so \( E_1\w \in \ker p(T) \), and similarly \( q(T)(E_2\w) = a(T)\,(pq)(T)\w = \0 \), so \( E_2\w \in \ker q(T) \). Hence \( W = \ker p(T) + \ker q(T) \).

*The intersection.* Let \( \v \in \ker p(T) \cap \ker q(T) \). Then \( E_1\v = b(T)\,q(T)\v = \0 \) and \( E_2\v = a(T)\,p(T)\v = \0 \), so \( \v = E_1\v + E_2\v = \0 \). By @thm-direct-sum-criteria, the sum is direct, which proves (a).

*The projections.* The splitting of \( \w \in W \) in (a) is unique (@def-direct-sum), and we have exhibited it as \( \w = E_1\w + E_2\w \); this proves the formula in (b). In particular \( E_1\w \in \ker p(T) \subseteq W \), so \( E_1 \) maps \( W \) into \( W \). As an operator on \( W \), \( E_1 \) is linear, fixes every \( \u \in \ker p(T) \) (whose splitting is \( \u = \u + \0 \)) and kills every vector of \( \ker q(T) \) (whose splitting is \( \0 + \v \)). By the uniqueness in @thm-projection-direct-sum (b), applied to \( W = \ker p(T) \oplus \ker q(T) \), it is the projection onto \( \ker p(T) \) along \( \ker q(T) \). Swapping the roles of \( p \) and \( q \) gives the statement for \( E_2 \).

(c) If \( (pq)(T) = 0 \), then \( W = V \), and (a) and (b) become the statements in (c), with \( E_1 = (bq)(T) \) and \( E_2 = (ap)(T) \) by @thm-evaluation-homomorphism (b). This proves the theorem.
:::

Bézout's coefficients \( a, b \) are not unique, but the projections on \( W \) are, by @thm-projection-direct-sum (b). So different choices of \( a, b \) give polynomials \( bq \) that may differ, while \( (bq)(T) \) always does the same thing on \( W \). When \( (pq)(T) = 0 \), the lemma turns a factorization of an annihilating polynomial into a direct sum decomposition of the whole space, with explicit projections, and each summand is carried into itself by \( T \) (@thm-kernel-image-of-polynomial-invariant).

::: {#exm-splitting-projection}
[Recovering Projections and Direct Sums]

Let \( P \in \cL(V) \) be a projection. Apply @thm-kernel-splitting with \( p = x \) and \( q = x - 1 \), and compare with @thm-projection-direct-sum (a).
:::

::: {.solution}
*Coprime.* \( 1 \cdot x + (-1)(x - 1) = 1 \), so we may take \( a = 1 \), \( b = -1 \), and any common divisor of \( x \) and \( x - 1 \) divides \( 1 \). *Annihilating.* \( (pq)(P) = P^2 - P = 0 \) because \( P \) is a projection.

By @thm-kernel-splitting (c),
\[
V = \ker P \oplus \ker(P - \id_V),
\]
with projection \( E_1 = b(P)q(P) = -(P - \id_V) = \id_V - P \) onto \( \ker P \) along \( \ker(P - \id_V) \), and \( E_2 = a(P)p(P) = P \) onto \( \ker(P - \id_V) \) along \( \ker P \).

To compare, note that \( \ker(P - \id_V) = \im P \). (⊆) If \( P\v = \v \), then \( \v \in \im P \). (⊇) If \( \v = P\u \), then \( P\v = P^2\u = P\u = \v \). So the lemma gives \( V = \im P \oplus \ker P \), with \( P \) the projection onto \( \im P \) along \( \ker P \): this is @thm-projection-direct-sum (a). It also reproves @exr-projections-and-trace-b2, that \( \id_V - P \) is the complementary projection.
:::

::: {#exm-splitting-involution}
[Recovering the Involution Decomposition]

Let \( F \) have characteristic not \( 2 \), and let \( T \in \cL(V) \) with \( T^2 = \id_V \). Apply @thm-kernel-splitting with \( p = x - 1 \) and \( q = x + 1 \), and compare with @thm-involution-decomposition. What goes wrong in characteristic \( 2 \)?
:::

::: {.solution}
*Coprime.* Since \( 2 \ne 0 \) in \( F \) (@def-characteristic),
\[
-\tfrac12(x - 1) + \tfrac12(x + 1) = 1,
\]
so \( a = -\tfrac12 \) and \( b = \tfrac12 \) work, and a common divisor of \( p \) and \( q \) divides \( 1 \). *Annihilating.* \( (pq)(T) = T^2 - \id_V = 0 \).

By @thm-kernel-splitting (c),
\[
V = \ker(T - \id_V) \oplus \ker(T + \id_V) = E_{+} \oplus E_{-},
\]
and the projection onto \( E_{+} \) along \( E_{-} \) is \( b(T)q(T) = \tfrac12(T + \id_V) \). These are exactly the conclusions of @thm-involution-decomposition. The other projection is \( a(T)p(T) = \tfrac12(\id_V - T) \).

In characteristic \( 2 \), \( x + 1 = x - 1 \), so \( p = q \) and \( \gcd(p, q) = x - 1 \ne 1 \). The lemma does not apply, and the warning after @thm-involution-decomposition shows that the conclusion really fails there.
:::

The lemma applies just as well when neither factor is linear, and then it finds subspaces that are not visible from single vectors.

::: {#exm-splitting-3x3}
[A Splitting with a Repeated Factor]

Let \( \A = \begin{pmatrix} 0 & 1 & -1 \\ 0 & 0 & 1 \\ 0 & 0 & 1 \end{pmatrix} \in M_3(\nQ) \). Verify that \( \A^2(\A - \I_3) = 0 \), and use @thm-kernel-splitting with \( p = x^2 \), \( q = x - 1 \) to split \( \nQ^3 \), giving both projections as polynomials in \( \A \).
:::

::: {.solution}
*The relation.* \( \A^2 = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 1 \end{pmatrix} \), and \( \A^3 = \A \cdot \A^2 = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 1 \end{pmatrix} = \A^2 \). So \( \A^2(\A - \I_3) = \A^3 - \A^2 = 0 \).

*Bézout.* \( x^2 = (x + 1)(x - 1) + 1 \), so \( 1 \cdot x^2 + \bigl(-(x + 1)\bigr)(x - 1) = 1 \): take \( a = 1 \), \( b = -(x + 1) \). Then
\[
\E_1 = b(\A)q(\A) = -(\A + \I_3)(\A - \I_3) = \I_3 - \A^2 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & -1 \\ 0 & 0 & 0 \end{pmatrix}, \qquad \E_2 = a(\A)p(\A) = \A^2 .
\]
*The summands.* \( \ker \A^2 = \{ (x, y, z) : z = 0 \} = \Span(\e_1, \e_2) \), and \( \ker(\A - \I_3) \) is cut out by \( -x + y - z = 0 \), \( -y + z = 0 \), \( 0 = 0 \), so it is \( \Span((0, 1, 1)) \). By @thm-kernel-splitting (c),
\[
\nQ^3 = \Span(\e_1, \e_2) \oplus \Span((0, 1, 1)),
\]
and for \( \v = (x, y, z) \), the splitting is \( \E_1\v + \E_2\v = (x, y - z, 0) + (0, z, z) \). One checks directly that \( (x, y - z, 0) \) has third entry \( 0 \) and \( (0, z, z) \) is a multiple of \( (0, 1, 1) \).

Note that \( \ker \A = \Span(\e_1) \) is strictly smaller than \( \ker \A^2 \). The factor \( p = x^2 \) could not be replaced by \( x \): the polynomial \( x(x - 1) \) does not annihilate \( \A \), since \( \A^2 - \A \ne 0 \).
:::

::: {.warning}
**Without coprimality the kernels need not fill \( \ker(pq)(T) \), or even form a direct sum.** Let \( T = T_{\N} \) with \( \N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) on \( F^2 \), and \( p = q = x \). Then \( (pq)(T) = \N^2 = 0 \), so \( \ker(pq)(T) = F^2 \). But \( \ker p(T) = \ker q(T) = \ker \N = \Span(\e_1) \). The two kernels are equal, so their sum is not direct, and \( \Span(\e_1) + \Span(\e_1) = \Span(\e_1) \ne F^2 \). Here \( \gcd(x, x) = x \), and no identity \( ax + bx = 1 \) exists, since its left side vanishes at \( 0 \).
:::

::: {.check}
Let \( T \in \cL(V) \) satisfy \( T^2 = 3T \), over a field with \( 3 \ne 0 \). Split \( V \) with the lemma, and write the projection onto \( \ker T \) as a polynomial in \( T \).
:::

::: {.solution}
\( x(x - 3) \) annihilates \( T \). Since \( \tfrac13 x - \tfrac13(x - 3) = 1 \), \( p = x \) and \( q = x - 3 \) are coprime with \( a = \tfrac13 \), \( b = -\tfrac13 \). By @thm-kernel-splitting (c), \( V = \ker T \oplus \ker(T - 3\id_V) \), and the projection onto \( \ker T \) along \( \ker(T - 3\id_V) \) is \( b(T)q(T) = -\tfrac13(T - 3\id_V) = \id_V - \tfrac13T \).
:::

In Chapter 8 the lemma is used with an annihilating polynomial factored into powers of distinct irreducibles, \( m = p_1^{e_1} \cdots p_k^{e_k} \). Distinct monic irreducibles are coprime, and so are their powers, so the lemma with \( k \) factors (@exr-polynomials-of-operators-c2) splits \( V \) into the pieces \( \ker p_i(T)^{e_i} \). That is the primary decomposition, and the canonical forms of Chapter 9 are built on it.

## Exercises

### A. Check your understanding

:::: {#exr-polynomials-of-operators-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State what it means that \( p \mapsto p(T) \) is linear and multiplicative.
2. True or false: if \( p(T)\,q(T) = 0 \), then \( p(T) = 0 \) or \( q(T) = 0 \). Justify your answer.
3. Why does every operator on a finite-dimensional space have a non-zero annihilating polynomial? Is the same true on \( F[x] \)?
4. True or false: if \( p \) annihilates \( T \) and \( p \mid q \), then \( q \) annihilates \( T \). Justify your answer.
5. State the kernel splitting lemma for \( (pq)(T) = 0 \), and say where coprimality is used in its proof.
6. True or false: for every subspace \( U \) of \( V \) and every \( T \in \cL(V) \), \( T \) maps \( U \) into \( U \). Justify your answer.
:::
::::

::: {.solution}
(a) \( (cp + q)(T) = c\,p(T) + q(T) \) and \( (pq)(T) = p(T)\,q(T) \) for all \( p, q \in F[x] \) and \( c \in F \) (@thm-evaluation-homomorphism).

(b) False. For the projection \( P(x, y) = (x, 0) \), \( P(P - \id) = 0 \) while \( P \ne 0 \) and \( P - \id \ne 0 \).

(c) \( \cL(V) \) has dimension \( n^2 \), so the \( n^2 + 1 \) operators \( \id_V, T, \dots, T^{n^2} \) are linearly dependent, and a dependence is a non-zero annihilating polynomial (@thm-annihilating-polynomial-exists). On \( F[x] \), multiplication by \( x \) has no non-zero annihilating polynomial, since \( p(S)(1) = p \).

(d) True. If \( q = hp \), then \( q(T) = h(T)\,p(T) = 0 \). This is the ideal property (@thm-annihilator-ideal).

(e) If \( p, q \) are coprime and \( (pq)(T) = 0 \), then \( V = \ker p(T) \oplus \ker q(T) \), and the projections are polynomials in \( T \) (@thm-kernel-splitting). Coprimality gives \( ap + bq = 1 \), hence \( \id_V = a(T)p(T) + b(T)q(T) \), which both produces the splitting of each vector and shows the intersection is \( \{\0\} \).

(f) False. The rotation \( R(x, y) = (-y, x) \) maps the \( x \)-axis to the \( y \)-axis. The statement is true for \( U = \ker p(T) \) and \( U = \im p(T) \) (@thm-kernel-image-of-polynomial-invariant).
:::

### B. Practice

:::: {#exr-polynomials-of-operators-b1}
[B1: A polynomial of a \( 2 \times 2 \) matrix]

Let \( \A = \begin{pmatrix} 1 & 2 \\ 3 & -1 \end{pmatrix} \in M_2(\nQ) \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( p(\A) \) for \( p = x^2 - 7 \) and for \( q = x^2 + x - 5 \).
2. Hence show that \( \A \) is invertible and find \( \A^{-1} \) as a polynomial in \( \A \).
:::
::::

::: {.solution}
(a) \( \A^2 = \begin{pmatrix} 1 + 6 & 2 - 2 \\ 3 - 3 & 6 + 1 \end{pmatrix} = 7\I_2 \). Hence \( p(\A) = \A^2 - 7\I_2 = 0 \). For \( q \), divide: \( q = (x^2 - 7) + (x + 2) \), so by @thm-evaluation-homomorphism \( q(\A) = p(\A) + \A + 2\I_2 = \begin{pmatrix} 3 & 2 \\ 3 & 1 \end{pmatrix} \). (Directly: \( 7\I_2 + \A - 5\I_2 = \A + 2\I_2 \).)

(b) From \( \A^2 = 7\I_2 \), \( \A\bigl(\tfrac17\A\bigr) = \bigl(\tfrac17\A\bigr)\A = \I_2 \). So \( \A \) is invertible with \( \A^{-1} = \tfrac17\A = \begin{pmatrix} \frac17 & \frac27 \\ \frac37 & -\frac17 \end{pmatrix} \).
:::

:::: {#exr-polynomials-of-operators-b2}
[B2: An annihilating polynomial by elimination]

Let \( \C = \begin{pmatrix} 0 & 0 & 2 \\ 1 & 0 & -1 \\ 0 & 1 & 2 \end{pmatrix} \in M_3(\nQ) \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \C^2 \) and \( \C^3 \), and show that \( (\I_3, \C, \C^2) \) is linearly independent.
2. Find a linear dependence among \( \I_3, \C, \C^2, \C^3 \), and hence a monic polynomial \( p \) of degree \( 3 \) with \( p(\C) = 0 \).
3. Hence show that \( \C \) is invertible and write \( \C^{-1} \) as a polynomial in \( \C \).
:::
::::

::: {.solution}
(a) Multiplying out,
\[
\C^2 = \begin{pmatrix} 0 & 2 & 4 \\ 0 & -1 & 0 \\ 1 & 2 & 3 \end{pmatrix}, \qquad \C^3 = \C \cdot \C^2 = \begin{pmatrix} 2 & 4 & 6 \\ -1 & 0 & 1 \\ 2 & 3 & 6 \end{pmatrix}.
\]
Let \( a\I_3 + b\C + c\C^2 = 0 \). The \( (2, 1) \)-entry gives \( b = 0 \); the \( (3, 1) \)-entry gives \( c = 0 \); then the \( (1, 1) \)-entry gives \( a = 0 \). So the list is independent.

(b) Let \( a\I_3 + b\C + c\C^2 + d\C^3 = 0 \). Reading entries: \( (2, 1) \): \( b - d = 0 \); \( (3, 1) \): \( c + 2d = 0 \); \( (1, 1) \): \( a + 2d = 0 \). With \( d = 1 \): \( b = 1 \), \( c = -2 \), \( a = -2 \). Check all entries of \( -2\I_3 + \C - 2\C^2 + \C^3 \): row 1 is \( (-2 + 0 - 0 + 2,\ 0 - 4 + 4,\ 2 - 8 + 6) = (0, 0, 0) \); row 2 is \( (1 - 0 - 1,\ -2 + 0 + 2 + 0,\ -1 - 0 + 1) = (0, 0, 0) \); row 3 is \( (0 - 2 + 2,\ 1 - 4 + 3,\ -2 + 2 - 6 + 6) = (0, 0, 0) \). Hence
\[
p = x^3 - 2x^2 + x - 2 = (x - 2)(x^2 + 1)
\]
satisfies \( p(\C) = 0 \). By (a) no non-zero polynomial of degree at most \( 2 \) annihilates \( \C \), so \( p \) is the monic generator of \( I_C \) (@thm-annihilator-ideal).

(c) \( \C^3 - 2\C^2 + \C = 2\I_3 \), that is, \( \C\,(\C^2 - 2\C + \I_3) = (\C^2 - 2\C + \I_3)\,\C = 2\I_3 \), using @thm-evaluation-homomorphism (c) for the second equality. Since \( 2 \ne 0 \) in \( \nQ \), \( \C \) is invertible with
\[
\C^{-1} = \tfrac12\bigl(\C^2 - 2\C + \I_3\bigr) = \begin{pmatrix} \frac12 & 1 & 0 \\ -1 & 0 & 1 \\ \frac12 & 0 & 0 \end{pmatrix}.
\]
:::

:::: {#exr-polynomials-of-operators-b3}
[B3: Operators with \( T^3 = T \)]

Let \( F \) have characteristic not \( 2 \), and let \( T \in \cL(V) \) with \( T^3 = T \).

::: {.enumerate options="label=(\alph*)"}
1. Use @thm-kernel-splitting with \( p = x \) and \( q = x^2 - 1 \) to show \( V = \ker T \oplus \ker(T^2 - \id_V) \), with projection \( \id_V - T^2 \) onto \( \ker T \).
2. Show that \( V = \ker T \oplus \ker(T - \id_V) \oplus \ker(T + \id_V) \).
3. Verify that the projections onto the three summands in (b) are \( \id_V - T^2 \), \( \tfrac12(T^2 + T) \) and \( \tfrac12(T^2 - T) \), in the sense that these three operators sum to \( \id_V \) and each maps \( V \) into the corresponding kernel.
:::
::::

::: {.solution}
(a) \( x \cdot x + (-1)(x^2 - 1) = 1 \): take \( a = x \), \( b = -1 \). Then \( p \) and \( q \) are coprime, and \( (pq)(T) = T^3 - T = 0 \). By @thm-kernel-splitting (c), \( V = \ker T \oplus \ker(T^2 - \id_V) \), and the projection onto \( \ker T \) is \( b(T)q(T) = -(T^2 - \id_V) = \id_V - T^2 \).

(b) Let \( W = \ker(T^2 - \id_V) \). Apply @thm-kernel-splitting (a) with \( p_1 = x - 1 \), \( q_1 = x + 1 \), which are coprime as in @exm-splitting-involution: \( W = \ker(p_1q_1)(T) = \ker(T - \id_V) \oplus \ker(T + \id_V) \). Write \( K_0 = \ker T \), \( K_{+} = \ker(T - \id_V) \), \( K_{-} = \ker(T + \id_V) \). Then \( V = K_0 + K_{+} + K_{-} \) by (a). If \( \u_0 + \u_{+} + \u_{-} = \0 \) with \( \u_0 \in K_0 \), \( \u_{\pm} \in K_{\pm} \), then \( \u_{+} + \u_{-} \in W \), so directness in (a) gives \( \u_0 = \0 \) and \( \u_{+} + \u_{-} = \0 \), and directness of \( W = K_{+} \oplus K_{-} \) gives \( \u_{+} = \u_{-} = \0 \). By @thm-direct-sum-k-criteria ((b) ⇒ (a)), the sum is direct.

(c) The sum is \( \id_V - T^2 + \tfrac12T^2 + \tfrac12T + \tfrac12T^2 - \tfrac12T = \id_V \). Using \( T^3 = T \): \( T(\id_V - T^2) = T - T^3 = 0 \); \( (T - \id_V)\tfrac12(T^2 + T) = \tfrac12(T^3 - T) = 0 \); \( (T + \id_V)\tfrac12(T^2 - T) = \tfrac12(T^3 - T) = 0 \). So the three operators map \( V \) into \( K_0 \), \( K_{+} \), \( K_{-} \) respectively. For \( \v \in V \), \( \v \) is the sum of its three images, and by the uniqueness of the splitting in (b) these are the components of \( \v \). Hence each operator is the projection onto its summand along the sum of the other two.
:::

### C. Going deeper

:::: {#exr-polynomials-of-operators-c1}
[C1: Inverses are polynomials]

Let \( V \) be a vector space over \( F \) and \( T \in \cL(V) \).

::: {.enumerate options="label=(\alph*)"}
1. Suppose \( p(T) = 0 \) for some \( p \in F[x] \) with \( p(0) \ne 0 \). Prove that \( T \) is invertible and that \( T^{-1} = g(T) \) for some \( g \in F[x] \).
2. Deduce that if \( V \) is finite-dimensional and \( T \) is invertible, then \( T^{-1} \) is a polynomial in \( T \).
3. Show that the monic generator \( m \) of \( I_T \), for \( V \) finite-dimensional and non-zero, satisfies \( m(0) \ne 0 \) if and only if \( T \) is invertible.
:::

*Hint: for (b), write a non-zero annihilating polynomial as \( x^kp_1 \) with \( p_1(0) \ne 0 \).*
::::

::: {.solution}
(a) Write \( p = c + xg_0 \), where \( c = p(0) \ne 0 \) and \( g_0 \in F[x] \). Then \( 0 = p(T) = c\,\id_V + T\,g_0(T) \), so \( T\,g_0(T) = -c\,\id_V \). Put \( g = -c^{-1}g_0 \). Then \( T\,g(T) = \id_V \), and \( g(T)\,T = T\,g(T) = \id_V \) by @thm-evaluation-homomorphism (c). Hence \( T \) is invertible with \( T^{-1} = g(T) \).

(b) If \( V = \{\0\} \), then \( T^{-1} = \id_V = 1(T) \). Otherwise, by @thm-annihilating-polynomial-exists there is a non-zero \( p \) with \( p(T) = 0 \). Let \( k \) be the least index with a non-zero coefficient in \( p \); then \( p = x^kp_1 \) with \( p_1(0) \ne 0 \). Now \( 0 = p(T) = T^k\,p_1(T) \). Since \( T \) is invertible, so is \( T^k \), with inverse \( (T^{-1})^k \), and composing on the left with it gives \( p_1(T) = 0 \). By (a), \( T^{-1} \) is a polynomial in \( T \).

(c) (⇒) If \( m(0) \ne 0 \), apply (a) to \( m \). (⇐) Suppose \( T \) is invertible and \( m(0) = 0 \). Then \( m = x\,m_1 \) with \( m_1 \) monic of degree \( \deg m - 1 \), and \( 0 = m(T) = T\,m_1(T) \). Composing with \( T^{-1} \) gives \( m_1(T) = 0 \), so \( m \mid m_1 \) by @thm-annihilator-ideal (b). Since \( V \ne \{\0\} \), \( m \) is not constant, so \( m_1 \ne 0 \) and \( \deg m \le \deg m_1 = \deg m - 1 \) by @thm-degree-of-product, a contradiction. Hence \( m(0) \ne 0 \).
:::

:::: {#exr-polynomials-of-operators-c2}
[C2: Splitting with \( k \) coprime factors]

Let \( T \in \cL(V) \), and let \( p_1, \dots, p_k \in F[x] \) be non-zero and pairwise coprime, with \( k \ge 2 \). Put \( p = p_1 \cdots p_k \) and \( W = \ker p(T) \).

::: {.enumerate options="label=(\alph*)"}
1. Use @thm-crt-polynomials to find \( e_1, \dots, e_k \in F[x] \) with \( e_i \equiv 1 \pmod{p_i} \) and \( e_i \equiv 0 \pmod{p_j} \) for \( j \ne i \). Show that \( p \mid e_1 + \dots + e_k - 1 \) and that \( p \mid p_ie_i \) for each \( i \).
2. Prove that for every \( \w \in W \), \( \w = e_1(T)\w + \dots + e_k(T)\w \) with \( e_i(T)\w \in \ker p_i(T) \).
3. Prove that \( W = \ker p_1(T) \oplus \dots \oplus \ker p_k(T) \), and that \( e_i(T) \) is the identity on \( \ker p_i(T) \) and zero on \( \ker p_j(T) \) for \( j \ne i \).
4. Deduce: if \( p(T) = 0 \), then \( V = \ker p_1(T) \oplus \dots \oplus \ker p_k(T) \), and the projection onto the \( i \)-th summand along the others is the polynomial \( e_i(T) \).
:::

*Hint: for the second divisibility in (a), use @lem-coprime-product (b).*
::::

::: {.solution}
(a) By @thm-crt-polynomials (a), applied to the pairwise coprime moduli \( p_1, \dots, p_k \) with \( r_i = 1 \) and \( r_j = 0 \) for \( j \ne i \), such an \( e_i \) exists. The sum \( s = e_1 + \dots + e_k \) satisfies \( s \equiv 1 \pmod{p_j} \) for each \( j \), since exactly one summand is \( \equiv 1 \) and the others are \( \equiv 0 \). The constant \( 1 \) satisfies the same congruences, so \( s \equiv 1 \pmod{p} \) by @thm-crt-polynomials (b). For the second claim, \( p_j \mid e_i \) for every \( j \ne i \), and these \( p_j \) are pairwise coprime, so \( \prod_{j \ne i} p_j \mid e_i \) by @lem-coprime-product (b). Multiplying by \( p_i \), \( p \mid p_ie_i \).

(b) Write \( e_1 + \dots + e_k = 1 + hp \) and \( p_ie_i = h_ip \). By @thm-evaluation-homomorphism, for \( \w \in W \),
\[
e_1(T)\w + \dots + e_k(T)\w = \w + h(T)\,p(T)\w = \w, \qquad p_i(T)\bigl(e_i(T)\w\bigr) = h_i(T)\,p(T)\w = \0 .
\]

(c) Each \( \ker p_i(T) \subseteq W \), since \( p(T) = \bigl(\prod_{j \ne i} p_j\bigr)(T)\,p_i(T) \). With (b), \( W = \ker p_1(T) + \dots + \ker p_k(T) \). Let \( \u_j \in \ker p_j(T) \). For \( j \ne i \), \( p_j \mid e_i \), say \( e_i = g\,p_j \), so \( e_i(T)\u_j = g(T)\,p_j(T)\u_j = \0 \). And \( e_i = 1 + g'p_i \), so \( e_i(T)\u_i = \u_i + g'(T)\,p_i(T)\u_i = \u_i \). This proves the second statement. Now suppose \( \u_1 + \dots + \u_k = \0 \) with \( \u_j \in \ker p_j(T) \). Applying \( e_i(T) \) gives \( \u_i = \0 \), for each \( i \). By @thm-direct-sum-k-criteria ((b) ⇒ (a)), the sum is direct.

(d) If \( p(T) = 0 \), then \( W = V \). By (c), \( V \) is the direct sum, and \( e_i(T) \in \cL(V) \) is the identity on the \( i \)-th summand and zero on the others. For \( \v = \u_1 + \dots + \u_k \), \( e_i(T)\v = \u_i \), which is the projection onto \( \ker p_i(T) \) along the sum of the other summands. For \( k = 2 \) this is @thm-kernel-splitting (c).
:::

:::: {#exr-polynomials-of-operators-c3}
[C3: The same rotation over \( \nR \) and over \( \nC \)]

Let \( \A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \), so that \( \A^2 + \I_2 = 0 \).

::: {.enumerate options="label=(\alph*)"}
1. Over \( \nC \), apply @thm-kernel-splitting to \( T_{\A} \) on \( \nC^2 \) with \( p = x - i \) and \( q = x + i \). Find both kernels and write the projection onto \( \ker(\A - i\I_2) \) as a polynomial in \( \A \).
2. Over \( \nR \), show that the only subspaces of \( \nR^2 \) that \( T_{\A} \) maps into themselves are \( \{\0\} \) and \( \nR^2 \). Explain why this matches the fact that \( x^2 + 1 \) admits no factorization into coprime non-constant factors in \( \nR[x] \).
:::
::::

::: {.solution}
(a) \( (x + i) - (x - i) = 2i \), so \( \tfrac{i}{2}(x - i) - \tfrac{i}{2}(x + i) = \tfrac{i}{2}(-2i) = 1 \): take \( a = \tfrac{i}{2} \) and \( b = -\tfrac{i}{2} \). So \( p, q \) are coprime, and \( (pq)(\A) = \A^2 + \I_2 = 0 \). By @thm-kernel-splitting (c), \( \nC^2 = \ker(\A - i\I_2) \oplus \ker(\A + i\I_2) \). Solving, \( (\A - i\I_2)(z, w) = (-iz - w,\ z - iw) = \0 \) gives \( w = -iz \), so \( \ker(\A - i\I_2) = \Span((1, -i)) \); similarly \( \ker(\A + i\I_2) = \Span((1, i)) \). The projection onto \( \ker(\A - i\I_2) \) is
\[
b(\A)q(\A) = -\tfrac{i}{2}(\A + i\I_2) = \tfrac12(\I_2 - i\A) = \begin{pmatrix} \frac12 & \frac{i}{2} \\ -\frac{i}{2} & \frac12 \end{pmatrix}.
\]
Check: it sends \( (1, -i) \) to \( (\tfrac12 + \tfrac12,\ -\tfrac{i}{2} - \tfrac{i}{2}) = (1, -i) \) and \( (1, i) \) to \( (\tfrac12 - \tfrac12,\ -\tfrac{i}{2} + \tfrac{i}{2}) = \0 \).

(b) A subspace of \( \nR^2 \) other than \( \{\0\} \) and \( \nR^2 \) has dimension \( 1 \) (@thm-subspace-dimension), so it is \( \Span(\v) \) with \( \v = (s, t) \ne \0 \). If \( \A\v \in \Span(\v) \), then \( (-t, s) = c(s, t) \) for some \( c \in \nR \), so \( -t = cs \) and \( s = ct \), giving \( s = -c^2s \) and \( t = -c^2t \). Since \( 1 + c^2 > 0 \), \( s = t = 0 \), a contradiction. So only \( \{\0\} \) and \( \nR^2 \) are mapped into themselves.

Over \( \nR \), \( x^2 + 1 \) has no root, so its only monic divisors are \( 1 \) and \( x^2 + 1 \), and the only factorizations \( x^2 + 1 = pq \) into monic factors have \( p = 1 \) or \( q = 1 \). The lemma then gives only \( \ker p(T) \oplus \ker q(T) = \{\0\} \oplus \nR^2 \), and by (b) there is no finer splitting into subspaces preserved by \( T_{\A} \) at all. Enlarging the field to \( \nC \) creates the coprime factors \( x \mp i \), and with them the splitting of (a).
:::
