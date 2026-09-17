# The Rational Canonical Form

Everything so far has needed the characteristic polynomial to split. Section 5 removed that need from the building block: a companion matrix \( C(p) \) exists for every monic \( p \), and it is the matrix of an operator on a cyclic subspace. What is left is to cut an arbitrary space into cyclic pieces. This section does that, over an **arbitrary field**, and the result is a genuine canonical form: a list of polynomials attached to \( T \), from which the matrix is written down mechanically, and which two operators share exactly when they are similar. Along the way we learn that similarity does not change if the field is enlarged.

## The plan

The goal, stated before its parts are named:

**Every operator on a non-zero finite-dimensional space decomposes the space into cyclic subspaces \( Z(\v_1; T), \dots, Z(\v_r; T) \) whose annihilators form a divisibility chain \( d_1 \mid d_2 \mid \dots \mid d_r = m_T \), and that chain is determined by \( T \).**

In the adapted basis the matrix is then \( C(d_1) \oplus \dots \oplus C(d_r) \), by @thm-cyclic-subspace-basis (b) and @thm-direct-sum-invariant-block-diagonal. So the whole content is the decomposition, and it is the hardest theorem of the chapter. The route has three steps, and each one is a tool we already have.

- **Step 1 (one prime at a time).** Chapter 8's primary decomposition splits \( V = V_1 \oplus \dots \oplus V_k \), where \( m_{T|_{V_i}} = p_i^{e_i} \) is a power of a single monic irreducible (@thm-primary-decomposition). Nothing more is needed from the general theory.
- **Step 2 (inside one prime power).** On a piece with \( m_T = p^e \), the operator \( P = p(T) \) is nilpotent, and the structure theorem for nilpotent operators was proved by induction, with \( \im N \) as the smaller space to which the hypothesis applies (@thm-nilpotent-structure). We run the same induction with \( P \) in place of \( N \) and cyclic subspaces \( Z(\u; T) \) in place of the spans of chains. The outcome is a decomposition into cyclic pieces whose annihilators are powers \( p^{e_1} \ge p^{e_2} \ge \dots \) of the one prime.
- **Step 3 (regroup across primes).** A cyclic piece for \( p_1 \) and a cyclic piece for \( p_2 \) can be **merged**: the sum of their generators has annihilator the product, by @lem-annihilator-of-sum. Merging the largest piece of every prime gives \( d_r = m_T \), the next largest give \( d_{r-1} \), and so on; the divisibility chain is automatic because within one prime the exponents decrease.

Uniqueness is a count, exactly as for the nilpotent case: the dimensions \( \dim\ker p(T)^k \) are visible in the decomposition and see nothing but the exponents.

## One prime at a time

Here is Step 2. Compare it with @thm-nilpotent-structure, which is the special case \( p = x \): there the pieces are spanned by Jordan chains \( \u, N\u, \dots \), and here by \( \u, T\u, T^2\u, \dots \).

::: {#thm-primary-cyclic-decomposition}
[Cyclic Decomposition for a Single Prime Power]

Let \( V \ne \{\0\} \) be a finite-dimensional vector space over \( F \), let \( T \in \cL(V) \), and suppose
\[
m_T = p^{e}, \qquad p \in F[x] \text{ monic irreducible of degree } d, \quad e \ge 1 .
\]
Then there are an integer \( m \ge 1 \), vectors \( \u_1, \dots, \u_m \in V \) and exponents
\[
e = k_1 \ge k_2 \ge \dots \ge k_m \ge 1
\]
such that
\[
V = Z(\u_1; T) \oplus Z(\u_2; T) \oplus \dots \oplus Z(\u_m; T), \qquad m_{T,\u_i} = p^{k_i} \quad (1 \le i \le m) .
\]
In particular \( \dim V = d(k_1 + \dots + k_m) \).
:::

::: {.idea}
Induction on \( \dim V \), with the smaller object found inside: \( W = \im p(T) \). It is \( T \)-invariant, the minimal polynomial of \( T|_W \) is \( p^{e-1} \), and \( \dim W < \dim V \) because \( p(T) \) is not injective. So \( W \) already breaks into cyclic pieces \( Z(\w_i; T) \). Each is one step short of what we want: \( \w_i = p(T)\u_i \) for some \( \u_i \in V \), and \( Z(\u_i; T) \) is a longer piece, with annihilator \( p \) times that of \( \w_i \). What is still missing is counted by \( U = \ker p(T) \), on which \( T \) has **irreducible** minimal polynomial \( p \), so that \( U \) is a direct sum of cyclic pieces of dimension \( d \) each and no proper cyclic piece inside one of them exists (Chapter 8, @exr-primary-decomposition-c2). The ends \( p^{k_i-1}(T)\u_i \) of the lengthened pieces sit inside \( U \); complete them to a decomposition of \( U \), and the extra generators supply the pieces with annihilator \( p \). Then Rank–Nullity makes the dimensions add up exactly, and directness is proved by applying \( p(T) \) once, as in the nilpotent case.
:::

::: {.proof}
We argue by induction on \( n = \dim V \ge 1 \), the statement being: for every field \( F \), every monic irreducible \( p \in F[x] \), every \( e \ge 1 \) and every \( T \) on a space of dimension \( n \) with \( m_T = p^e \), a decomposition as described exists.

Write \( P = p(T) \) and \( U = \ker P \), and recall that \( Z(\v; T|_{V'}) = Z(\v; T) \) whenever \( V' \) is a \( T \)-invariant subspace containing \( \v \), since the two operators agree on \( \v \) and on everything \( T \) produces from it.

*The case \( e = 1 \).* Then \( m_T = p \) is irreducible, and @exr-primary-decomposition-c2 (d) gives \( V = Z(\u_1; T) \oplus \dots \oplus Z(\u_m; T) \) with every \( \u_i \ne \0 \) (the subspace called \( W_\v \) there is \( Z(\v; T) \), by @prp-cyclic-subspace-smallest (a)). For \( \u \ne \0 \) we have \( m_{T,\u} \mid m_T = p \) and \( m_{T,\u} \ne 1 \), so \( m_{T,\u} = p \) and every \( k_i = 1 = e \). This settles \( e = 1 \), and in particular the base case \( n = 1 \), where \( m_T \) is linear.

*The case \( e \ge 2 \).* Let \( n \ge 2 \) and assume the statement for all dimensions less than \( n \).

**Step 1. Cyclic pieces inside \( \im P \).** Put \( W = \im P \). Since \( e \ge 2 \), the polynomial \( p \) does not annihilate \( T \) (else \( m_T = p^e \) would divide \( p \), @thm-minimal-polynomial-divides), so \( P \ne 0 \) and \( W \ne \{\0\} \). Also \( P \) is not injective: otherwise \( P^{e} = m_T(T) = 0 \) would be injective on \( V \ne \{\0\} \) (@thm-composition-preserves), which is false. So \( 1 \le \dim W < n \) by @thm-rank-nullity. The subspace \( W \) is \( T \)-invariant (@thm-kernel-image-of-polynomial-invariant (b)), and
\[
m_{T|_W} = p^{e-1} .
\]
Indeed \( p^{e-1}(T) \) kills \( W \), because \( p^{e-1}(T)P\v = m_T(T)\v = \0 \) for every \( \v \); and \( p^{e-2}(T) \) does not, because \( p^{e-2}(T)P \ne 0 \) — that operator is \( p^{e-1}(T) \), which is non-zero since \( m_T = p^e \nmid p^{e-1} \) — so some \( P\v \in W \) survives it. Hence \( m_{T|_W} \) is a monic divisor of \( p^{e-1} \) but not of \( p^{e-2} \), and @lem-monic-divisors leaves only \( p^{e-1} \). By the induction hypothesis applied to \( T|_W \),
\[
W = Z(\w_1; T) \oplus \dots \oplus Z(\w_q; T), \qquad m_{T,\w_i} = p^{l_i}, \qquad e - 1 = l_1 \ge \dots \ge l_q \ge 1 .
\]

**Step 2. Lengthen each piece by one step.** Each \( \w_i \) lies in \( W = \im P \), so we may choose \( \u_i \in V \) with \( P\u_i = \w_i \), for \( i = 1, \dots, q \). Put \( k_i = l_i + 1 \). Then \( p^{k_i}(T)\u_i = p^{l_i}(T)\w_i = \0 \), so \( m_{T,\u_i} \mid p^{k_i} \); and \( p^{l_i}(T)\u_i \ne \0 \), since otherwise \( p^{l_i - 1}(T)\w_i = p^{l_i}(T)\u_i = \0 \), contradicting \( m_{T,\w_i} = p^{l_i} \). By @lem-monic-divisors,
\[
m_{T,\u_i} = p^{k_i} = p^{l_i + 1} \qquad (1 \le i \le q) .
\]

**Step 3. Fill up \( \ker P \).** Put \( \z_i = p^{l_i}(T)\u_i \) for \( i \le q \). Each is non-zero by Step 2, lies in \( U = \ker P \) because \( P\z_i = p^{k_i}(T)\u_i = \0 \), and lies in \( Z(\w_i; T) \), since \( l_i \ge 1 \) gives \( \z_i = p^{l_i-1}(T)p(T)\u_i = p^{l_i-1}(T)\w_i \). Consequently \( Z(\z_i; T) \subseteq Z(\w_i; T) \) (@prp-cyclic-subspace-smallest (b), (c)), so the sum \( Z(\z_1;T) + \dots + Z(\z_q;T) \) is direct: a vanishing sum of vectors \( \c_i \in Z(\z_i;T) \subseteq Z(\w_i;T) \) forces every \( \c_i = \0 \) by the directness of Step 1 (@thm-direct-sum-k-criteria).

Now \( U \ne \{\0\} \), \( U \) is \( T \)-invariant (@thm-kernel-image-of-polynomial-invariant (b)), and \( p(T|_U) = 0 \) with \( p \) irreducible, so \( m_{T|_U} = p \) as in the case \( e = 1 \). Among all lists \( (\z_1, \dots, \z_q, \z_{q+1}, \dots, \z_s) \) of non-zero vectors of \( U \) extending \( \z_1, \dots, \z_q \) and with \( Z(\z_1;T) + \dots + Z(\z_s;T) \) direct, choose one with \( s \) as large as possible; this is possible because each summand has dimension \( d \) (@exr-primary-decomposition-c2 (b)), so \( s d \le \dim U \). Let \( S \) be that direct sum. If \( S \ne U \), pick \( \y \in U \setminus S \). The subspace \( Z(\y;T) \cap S \) is \( T \)-invariant (@prp-invariant-sum-intersection), lies inside \( Z(\y;T) \), and does not contain \( \y \); by @exr-primary-decomposition-c2 (c), applied to \( T|_U \), it is therefore \( \{\0\} \). Then \( S + Z(\y;T) \) is direct — a relation \( \c_1 + \dots + \c_s + \c = \0 \) with \( \c_j \in Z(\z_j;T) \) and \( \c \in Z(\y;T) \) puts \( \c \in Z(\y;T) \cap S = \{\0\} \), and directness of \( S \) kills the rest (@thm-direct-sum-k-criteria) — contradicting the maximality of \( s \). Hence
\[
U = Z(\z_1; T) \oplus \dots \oplus Z(\z_s; T), \qquad m_{T,\z_j} = p \ \text{ for every } j .
\]
Put \( m = s \), and for \( q < i \le m \) put \( \u_i = \z_i \) and \( k_i = 1 \), so that \( m_{T,\u_i} = p^{k_i} \) for those \( i \) as well.

**Step 4. The pieces fill \( V \).** First count. By @thm-cyclic-subspace-basis (a), \( \dim Z(\u_i; T) = \deg p^{k_i} = dk_i \). Hence
\[
\sum_{i=1}^{m} \dim Z(\u_i;T) = \sum_{i=1}^{q} d(l_i + 1) + (m - q)d = \Big(\sum_{i=1}^{q} dl_i\Big) + md = \dim W + \dim U = n ,
\]
where \( \sum_i dl_i = \sum_i \dim Z(\w_i;T) = \dim W \) by Step 1, \( md = \sum_j \dim Z(\z_j;T) = \dim U \) by Step 3, and the last equality is @thm-rank-nullity.

Next, directness. Let \( \y_1 + \dots + \y_m = \0 \) with \( \y_i \in Z(\u_i;T) \), say \( \y_i = f_i(T)\u_i \) (@prp-cyclic-subspace-smallest (a)). Apply \( P \). For \( i > q \) we get \( P\y_i = f_i(T)P\u_i = \0 \), since \( \u_i \in U \). For \( i \le q \) we get \( P\y_i = f_i(T)\w_i \in Z(\w_i;T) \). So
\[
\sum_{i=1}^{q} f_i(T)\w_i = \0 ,
\]
and the directness of Step 1 forces \( f_i(T)\w_i = \0 \) for every \( i \le q \), that is, \( p^{l_i} \mid f_i \) (@def-t-annihilator). Write \( f_i = p^{l_i}g_i \) for \( i \le q \); then
\[
\y_i = g_i(T)\,p^{l_i}(T)\u_i = g_i(T)\z_i \in Z(\z_i; T) \qquad (i \le q) .
\]
For \( i > q \), \( \y_i \in Z(\u_i;T) = Z(\z_i;T) \) by definition. So the relation \( \y_1 + \dots + \y_m = \0 \) is a relation between vectors of the independent subspaces \( Z(\z_1;T), \dots, Z(\z_m;T) \) of Step 3, and every \( \y_i = \0 \). By @thm-direct-sum-k-criteria ((b) ⇒ (a)) the sum \( \sum_i Z(\u_i;T) \) is direct, and by the count its dimension is \( n \), so it is all of \( V \) (@thm-dim-impl-eq).

Finally the exponents. We have \( k_1 = l_1 + 1 = e \), the \( k_i \) with \( i \le q \) decrease because the \( l_i \) do, and the remaining ones equal \( 1 \le k_q \); so after listing the pieces in this order, \( e = k_1 \ge \dots \ge k_m \ge 1 \). The dimension formula \( \dim V = d\sum_i k_i \) is the count above. This completes the induction.
:::

Two sanity checks. For \( p = x \), so that \( T \) is nilpotent with \( m_T = x^e \), the theorem returns @thm-nilpotent-structure: \( Z(\u; T) = \Span(\u, T\u, \dots, T^{k-1}\u) \) is the span of a Jordan chain written backwards, and \( d = 1 \), so \( \dim V = \sum_i k_i \). And for \( e = 1 \) it returns @exr-primary-decomposition-c2: all pieces have dimension \( d \), so \( d \mid \dim V \).

## Invariant factors

Now Steps 1 and 3 of the plan. Merging pieces across different primes is where @lem-annihilator-of-sum earns its keep.

::: {#thm-cyclic-decomposition}
[Cyclic Decomposition Theorem]

Let \( V \ne \{\0\} \) be a finite-dimensional vector space over \( F \) and let \( T \in \cL(V) \). Then there are an integer \( r \ge 1 \), vectors \( \v_1, \dots, \v_r \in V \) and monic **non-constant** polynomials \( d_1, \dots, d_r \in F[x] \) such that
\[
V = Z(\v_1; T) \oplus \dots \oplus Z(\v_r; T), \qquad m_{T,\v_j} = d_j ,
\]
and

::: {.enumerate options="label=(\alph*)"}
1. \( d_1 \mid d_2 \mid \dots \mid d_r \);
2. \( d_r = m_T \);
3. \( d_1d_2\cdots d_r = p_T \); in particular \( \sum_j \deg d_j = \dim V \);
4. there is a **finer** decomposition \( V = \bigoplus_{i,j} Z(\v_{ij}; T) \) into cyclic subspaces whose annihilators \( m_{T,\v_{ij}} \) are powers of monic irreducibles, and the list of these prime powers, with repetitions, consists exactly of the prime powers occurring in the factorizations of \( d_1, \dots, d_r \).
:::
:::

::: {.idea}
Run the plan. Primary decomposition gives one piece per prime; @thm-primary-cyclic-decomposition breaks each piece into cyclic subspaces with annihilators \( p_i^{e_{i1}}, p_i^{e_{i2}}, \dots \), the exponents decreasing. Arrange these in an array, one row per prime, with the largest exponent of each prime in the **first** column. Multiplying down a column gives one member of the chain, and the columns are numbered **backwards**: the first column, which carries the largest exponent of every prime, gives \( d_r = m_T \); the second gives \( d_{r-1} \); the last gives \( d_1 \). The chain \( d_1 \mid \dots \mid d_r \) comes out for free, because the exponents in a row decrease from left to right. The generator for a column is the sum of the generators in it, whose annihilator is the product by @lem-annihilator-of-sum.
:::

::: {.proof}
**Step 1.** By @thm-unique-factorization-polynomials, \( m_T = p_1^{e_1}\cdots p_k^{e_k} \) with \( p_1, \dots, p_k \) distinct monic irreducibles and \( e_i \ge 1 \); here \( \deg m_T \ge 1 \) since \( V \ne \{\0\} \) (@thm-minimal-polynomial-divides). By @thm-primary-decomposition, \( V = V_1 \oplus \dots \oplus V_k \) with \( V_i \) non-zero and \( T \)-invariant and \( m_{T|_{V_i}} = p_i^{e_i} \).

**Step 2.** Fix \( i \) and apply @thm-primary-cyclic-decomposition to \( T|_{V_i} \). Since \( Z(\v; T|_{V_i}) = Z(\v; T) \) for \( \v \in V_i \), it gives vectors \( \v_{i1}, \dots, \v_{i m_i} \in V_i \) and exponents \( e_i = e_{i1} \ge \dots \ge e_{i m_i} \ge 1 \) with
\[
V_i = Z(\v_{i1}; T) \oplus \dots \oplus Z(\v_{i m_i}; T), \qquad m_{T,\v_{ij}} = p_i^{e_{ij}} .
\]
Combining with Step 1, \( V \) is the direct sum of **all** the subspaces \( Z(\v_{ij}; T) \): a basis of \( V \) is obtained by concatenating bases of the \( V_i \), each of which is a concatenation of bases of its own pieces, so @thm-direct-sum-k-criteria ((d) ⇒ (a)) applies.

**Step 3.** Let \( r = \max_i m_i \) and, for \( 1 \le j \le r \), put \( j' = r + 1 - j \) and
\[
d_j = \prod_{i \,:\, m_i \ge j'} p_i^{e_{i j'}}, \qquad \v_j = \sum_{i \,:\, m_i \ge j'} \v_{i j'} .
\]
So \( d_r \) collects the largest exponent of every prime and \( d_1 \) the smallest ones still present.

*The divisibility chain.* The exponent of \( p_i \) in \( d_j \) is \( e_{ij'} \) if \( m_i \ge j' \) and \( 0 \) otherwise. As \( j \) increases, \( j' \) decreases, so this exponent is non-decreasing in \( j \) (the exponents \( e_{i1} \ge e_{i2} \ge \dots \) decrease in the second index, and a \( 0 \) is followed only by values \( \ge 0 \)). Hence \( d_j \mid d_{j+1} \) for every \( j \) (@lem-monic-divisors), which is (a). Taking \( j = r \), so \( j' = 1 \), gives \( d_r = \prod_i p_i^{e_{i1}} = \prod_i p_i^{e_i} = m_T \), which is (b). Each \( d_j \) is non-constant: choosing \( i_0 \) with \( m_{i_0} = r \), we have \( m_{i_0} \ge j' \) for every \( j \), so the factor \( p_{i_0}^{e_{i_0 j'}} \) occurs in \( d_j \), with exponent at least \( 1 \).

*The annihilators and the pieces.* For fixed \( j \), the polynomials \( p_i^{e_{ij'}} \) appearing in \( d_j \) are pairwise coprime, being powers of distinct monic irreducibles: a monic common divisor of \( p_i^{a} \) and \( p_{i'}^{b} \) with \( i \ne i' \) is a power of each, hence \( 1 \) by the uniqueness of factorization (@lem-monic-divisors, @thm-unique-factorization-polynomials (b)). So @lem-annihilator-of-sum gives \( m_{T,\v_j} = d_j \). Moreover
\[
Z(\v_j; T) = \bigoplus_{i \,:\, m_i \ge j'} Z(\v_{ij'}; T) :
\]
the left side is contained in the right, because the right side is a \( T \)-invariant subspace containing \( \v_j \) (@prp-invariant-sum-intersection, @prp-cyclic-subspace-smallest (c)), and the two have the same dimension,
\[
\dim Z(\v_j;T) = \deg d_j = \sum_{i} \deg p_i^{e_{ij'}} = \sum_{i} \dim Z(\v_{ij'};T),
\]
by @thm-cyclic-subspace-basis (a) and @thm-direct-sum-k-criteria ((a) ⇒ (e)); so they are equal (@thm-dim-impl-eq).

*The decomposition.* Each subspace \( Z(\v_{i j_0};T) \), with \( 1 \le j_0 \le m_i \), occurs in exactly one of the sums just displayed, namely the one with \( j = r + 1 - j_0 \); so every pair \( (i, j_0) \) is used exactly once and
\[
\sum_{j=1}^{r} Z(\v_j; T) = \sum_{i,j} Z(\v_{ij}; T) = V ,
\]
and \( \sum_j \dim Z(\v_j;T) = \sum_{i,j}\dim Z(\v_{ij};T) = \dim V \). By @thm-direct-sum-k-criteria ((e) ⇒ (a)) the sum over \( j \) is direct, and it equals \( V \).

(c) Each \( Z(\v_j;T) \) is \( T \)-invariant and non-zero, so by @thm-direct-sum-invariant-block-diagonal there is a basis \( \sB \) of \( V \) with \( [T]_{\sB} = [T|_{Z(\v_1;T)}] \oplus \dots \oplus [T|_{Z(\v_r;T)}] \). Then \( xI - [T]_{\sB} \) is block diagonal with the blocks \( xI - [T|_{Z(\v_j;T)}] \), so @thm-det-block-triangular, applied \( r - 1 \) times, gives
\[
p_T = \det\big(xI - [T]_{\sB}\big) = \prod_{j=1}^{r} p_{T|_{Z(\v_j;T)}}
\]
(@def-charpoly-operator). By @thm-cyclic-subspace-basis (c), \( p_{T|_{Z(\v_j;T)}} = m_{T,\v_j} = d_j \). Hence \( p_T = d_1\cdots d_r \), and comparing degrees gives \( \sum_j \deg d_j = \deg p_T = \dim V \) (@thm-charpoly-coefficients).

(d) Step 2 already produced the finer decomposition \( V = \bigoplus_{i,j} Z(\v_{ij};T) \), with \( m_{T,\v_{ij}} = p_i^{e_{ij}} \) a prime power. By the definition of \( d_j \) in Step 3, the exponent of \( p_i \) in \( d_j \) is \( e_{i,r+1-j} \) when \( m_i \ge r + 1 - j \) and \( 0 \) otherwise, and each pair \( (i,j) \) with \( 1 \le j \le m_i \) is used exactly once. So the prime powers occurring in \( d_1, \dots, d_r \) are exactly the polynomials \( p_i^{e_{ij}} \), with the same repetitions.
:::

The polynomials in the chain, and the prime powers they are built from, are the data we are after — but first we must know that they do not depend on the decomposition we happened to construct. The count that settles this is the count of Section 2 in disguise: there the chain lengths were read off from the ranks of the powers of \( N \), and here the exponents are read off from the dimensions of the kernels of the powers of \( p(T) \). Write \( v_p(f) \) for the exponent of a monic irreducible \( p \) in the factorization of a non-zero \( f \in F[x] \), so that \( v_p(f) \ge 1 \) exactly when \( p \mid f \).

::: {#prp-elementary-divisors-from-kernels}
[Counting the Exponents]

Let \( V \ne \{\0\} \) be finite-dimensional over \( F \), let \( T \in \cL(V) \), and suppose
\[
V = Z(\u_1; T) \oplus \dots \oplus Z(\u_N; T), \qquad m_{T,\u_i} = g_i ,
\]
with every \( g_i \) monic and non-constant. Then for every monic irreducible \( p \in F[x] \):

::: {.enumerate options="label=(\alph*)"}
1. \( \displaystyle \dim\ker p(T)^{k} = \deg p \cdot \sum_{i=1}^{N} \min\big(k, v_p(g_i)\big) \) for every integer \( k \ge 0 \);
2. for every \( k \ge 1 \),
   \[
   \#\{\, i : v_p(g_i) \ge k \,\} = \frac{\dim\ker p(T)^{k} - \dim\ker p(T)^{k-1}}{\deg p} ,
   \]
   a number depending only on \( T \), \( p \) and \( k \).
:::
:::

::: {.idea}
Kernels respect the decomposition, so we may work inside one piece. There a vector is \( h(T)\u \), and it is killed by \( p(T)^k \) exactly when \( g \mid p^kh \), which after canceling the common factor \( \gcd(g, p^k) \) says that \( h \) is a multiple of \( g/\gcd(g,p^k) \). The surviving vectors are therefore a cyclic subspace again, generated by that multiple of \( \u \), and its annihilator is \( \gcd(g, p^k) = p^{\min(k, v_p(g))} \). Summing over the pieces and taking differences in \( k \) then counts exponents.
:::

::: {.proof}
(a) Write \( Z_i = Z(\u_i;T) \) and \( S = p(T)^k \). Each \( Z_i \) is \( T \)-invariant, hence \( S \)-invariant (@thm-kernel-image-of-polynomial-invariant (b)). If \( \v = \v_1 + \dots + \v_N \) with \( \v_i \in Z_i \), then \( S\v = S\v_1 + \dots + S\v_N \) with \( S\v_i \in Z_i \), so \( S\v = \0 \) if and only if every \( S\v_i = \0 \), by the uniqueness of the splitting (@thm-direct-sum-k-criteria). Therefore
\[
\ker S = (\ker S \cap Z_1) \oplus \dots \oplus (\ker S \cap Z_N),
\]
and it suffices to compute each \( \dim(\ker S \cap Z_i) \). Fix \( i \) and write \( \u = \u_i \), \( g = g_i \), \( Z = Z_i \). Put
\[
c = \gcd(g, p^{k}) = p^{\min(k,\, v_p(g))} \qquad\text{and}\qquad t = g/c ,
\]
the formula for \( c \) holding because a monic common divisor of \( g \) and \( p^k \) is a power of \( p \) (@lem-monic-divisors) dividing both, and \( p^{s} \mid g \) exactly when \( s \le v_p(g) \) (@thm-unique-factorization-polynomials).

Every element of \( Z \) is \( h(T)\u \) for some \( h \in F[x] \) (@prp-cyclic-subspace-smallest (a)), and
\[
p(T)^{k}h(T)\u = \0 \iff g \mid p^{k}h \iff t \mid h ,
\]
where the second equivalence holds because \( g = ct \) and \( p^k = c\,(p^k/c) \) with \( \gcd(t, p^k/c) = 1 \): from \( ct \mid c(p^k/c)h \) we get \( t \mid (p^k/c)h \), hence \( t \mid h \) (@thm-coprime-divides-product), and conversely \( t \mid h \) gives \( g = ct \mid c\,h \mid p^{k}h \) since \( c \mid p^k \). So
\[
\ker S \cap Z = \{\, h(T)\u : t \mid h \,\} = \{\, s(T)\big(t(T)\u\big) : s \in F[x] \,\} = Z\big(t(T)\u;\, T\big) .
\]
Its generator has annihilator \( c \): for \( s \in F[x] \), \( s(T)t(T)\u = \0 \) if and only if \( g \mid st \), that is, \( c \mid s \), because \( g = ct \). Taking \( s = 1 \) shows that \( t(T)\u \ne \0 \) unless \( c = 1 \), so @thm-cyclic-subspace-basis (a) applies whenever \( c \ne 1 \) and gives
\[
\dim(\ker S \cap Z_i) = \deg c = \min\big(k, v_p(g_i)\big)\deg p ,
\]
where for \( c = 1 \) the cyclic subspace is \( \{\0\} \) of dimension \( 0 \), in agreement. Adding over \( i \) gives (a).

(b) Subtract the values of (a) at \( k \) and \( k-1 \). Each term \( \min(k, v_p(g_i)) - \min(k-1, v_p(g_i)) \) equals \( 1 \) if \( v_p(g_i) \ge k \) and \( 0 \) otherwise, so the difference is \( \deg p \) times the number of indices \( i \) with \( v_p(g_i) \ge k \). The left-hand side is defined from \( T \), \( p \) and \( k \) alone.
:::

::: {#cor-invariant-factors-unique}
[Uniqueness of the Chain and of the Prime Powers]

Let \( V \ne \{\0\} \) be finite-dimensional over \( F \) and \( T \in \cL(V) \).

::: {.enumerate options="label=(\alph*)"}
1. Any two decompositions as in @thm-cyclic-decomposition give the **same** ordered list \( d_1 \mid \dots \mid d_r \).
2. Any decomposition \( V = Z(\u_1;T) \oplus \dots \oplus Z(\u_N;T) \) whose annihilators \( m_{T,\u_i} \) are powers of monic irreducibles gives the same list of annihilators, up to order, namely the prime powers occurring in \( d_1, \dots, d_r \).
3. Explicitly, writing
   \[
   c_p(k) = \frac{\dim\ker p(T)^{k} - \dim\ker p(T)^{k-1}}{\deg p} \qquad (p \text{ monic irreducible},\ k \ge 1),
   \]
   the list is recovered by \( r = \max_p c_p(1) \) and
   \[
   v_p(d_j) = \#\{\, k \ge 1 : c_p(k) \ge r + 1 - j \,\} \qquad (1 \le j \le r) .
   \]
   In particular the invariant factors of \( T \) are determined by the numbers \( \dim\ker p(T)^{k} \) alone.
:::
:::

::: {.idea}
Divisibility puts the zeros first: in the list \( v_p(d_1) \le \dots \le v_p(d_r) \), the indices where \( p \) actually occurs are a block at the **right** end. So a count of how many \( d_j \) are divisible by \( p^k \) pins down *which* ones they are, and therefore each individual exponent. The counts are supplied by @prp-elementary-divisors-from-kernels, which sees only \( T \).
:::

::: {.proof}
(a) and (c). Let \( V = \bigoplus_{j=1}^{r} Z(\v_j;T) \) be such a decomposition, with annihilators \( d_1 \mid \dots \mid d_r \), all monic and non-constant. Fix a monic irreducible \( p \). By @prp-elementary-divisors-from-kernels (b), applied to this decomposition,
\[
c_p(k) = \#\{\, j : v_p(d_j) \ge k \,\} \qquad (k \ge 1) ,
\]
so the left-hand side, which is defined from \( T \), \( p \) and \( k \) alone, computes the right-hand side. Divisibility makes the exponents non-decreasing, \( v_p(d_1) \le \dots \le v_p(d_r) \), so for each \( k \) the set \( \{\, j : v_p(d_j) \ge k \,\} \) is the set of the **last** \( c_p(k) \) indices:
\[
v_p(d_j) \ge k \iff j \ge r + 1 - c_p(k) \iff c_p(k) \ge r + 1 - j . \tag{$\ast$}
\]
First, \( r \) is determined. Each \( d_j \) is non-constant, so \( v_p(d_1) \ge 1 \) for some monic irreducible \( p \); for that \( p \), \( (\ast) \) with \( k = 1 \) and \( j = 1 \) gives \( c_p(1) \ge r \), while \( c_p(1) \le r \) always. Hence \( r = \max_p c_p(1) \). Next, for each \( p \) and each \( j \), counting the \( k \ge 1 \) for which \( (\ast) \) holds gives
\[
v_p(d_j) = \#\{\, k \ge 1 : c_p(k) \ge r + 1 - j \,\} ,
\]
a finite number, since \( c_p(k) = 0 \) for \( k > \deg m_T \). This proves (c). Finally each \( d_j \) is monic with determined exponents \( v_p(d_j) \) for every \( p \), so \( d_j \) is determined (@thm-unique-factorization-polynomials), which proves (a).

(b) Let \( V = \bigoplus_{i} Z(\u_i;T) \) with \( m_{T,\u_i} = q_i^{f_i} \), \( q_i \) monic irreducible and \( f_i \ge 1 \). For a monic irreducible \( p \) we have \( v_p(q_i^{f_i}) = f_i \) if \( q_i = p \) and \( 0 \) otherwise. Applying @prp-elementary-divisors-from-kernels (b) to this decomposition and to the one in (a) gives, for every \( p \) and every \( k \ge 1 \),
\[
\#\{\, i : q_i = p,\ f_i \ge k \,\} = c_p(k) = \#\{\, j : v_p(d_j) \ge k \,\} .
\]
Hence, for each \( p \), the exponents \( f_i \) with \( q_i = p \) and the positive exponents \( v_p(d_j) \) form the same multiset. So the list \( (q_i^{f_i})_i \) is exactly the list of prime powers occurring in \( d_1, \dots, d_r \), with the same repetitions. By @thm-cyclic-decomposition (d) such a decomposition exists, so both lists are non-empty and agree.
:::

::: {#def-invariant-factors}
[Invariant Factors, Elementary Divisors]

Let \( V \ne \{\0\} \) be finite-dimensional over \( F \) and \( T \in \cL(V) \). The **invariant factors** of \( T \) are the monic non-constant polynomials
\[
d_1 \mid d_2 \mid \dots \mid d_r
\]
of @thm-cyclic-decomposition, which by @cor-invariant-factors-unique (a) do not depend on the decomposition. The **elementary divisors** of \( T \) are the prime powers occurring in the factorizations of \( d_1, \dots, d_r \), listed with repetition; by @cor-invariant-factors-unique (b) they are the annihilators of the pieces in any decomposition of \( V \) into cyclic subspaces with prime-power annihilators. For \( A \in M_n(F) \) the invariant factors and elementary divisors are those of \( T_A \).
:::

In words: the invariant factors are the annihilators of the cyclic pieces, ordered so that each divides the next; the largest is \( m_T \), and their product is \( p_T \). The elementary divisors are the same information cut along the primes. Each list determines the other: one by factoring, the other by the regrouping recipe of Step 3 in the proof of @thm-cyclic-decomposition, which @cor-invariant-factors-unique (c) shows to be forced.

**Non-example by minimal change.** Drop the divisibility clause and keep only the product. For an operator on a \( \nQ \)-space of dimension \( 3 \) with \( p_T = (x-1)(x-2)^2 \), the pair
\[
d_1 = x - 1, \qquad d_2 = (x-2)^2
\]
multiplies to \( p_T \) and consists of monic non-constant polynomials of the right total degree. It is still not a list of invariant factors of anything, because \( d_1 \nmid d_2 \). The clause that fails is (a) of @thm-cyclic-decomposition, and with it (b): the largest member of the list has to be \( m_T \), and \( m_T(T) \) kills every vector of \( V \), so \( m_T \) is a multiple of the annihilator of every piece (@thm-cyclic-subspace-basis (d)). The genuine lists here are \( \big((x-1)(x-2)^2\big) \) and \( \big(x - 2,\ (x-1)(x-2)\big) \).

::: {.check}
Let \( T \) be an operator on a \( \nQ \)-vector space with \( p_T = (x^2+1)^2 \). How many possibilities are there for the list of elementary divisors, and what are the corresponding invariant factors?
:::

::: {.solution}
The product of the elementary divisors is \( p_T \) (by @thm-cyclic-decomposition (c) and @def-invariant-factors), and \( x^2 + 1 \) is irreducible over \( \nQ \) (no rational root, @thm-irreducible-deg-2-3 (b)). So the elementary divisors are powers of \( x^2+1 \) with exponents forming a partition of \( 2 \): either \( (x^2+1)^2 \) alone, or \( x^2+1 \) twice. The invariant factors are \( d_1 = (x^2+1)^2 \) in the first case (one piece, \( r = 1 \)) and \( d_1 = d_2 = x^2+1 \) in the second. The two are told apart by \( m_T \), which is \( d_r \): \( (x^2+1)^2 \) against \( x^2+1 \).
:::

## The rational canonical form

Everything is now assembled. Writing the matrix down is @thm-cyclic-subspace-basis (b), one piece at a time.

*Every operator over every field has a block diagonal matrix whose blocks are companion matrices of a divisibility chain, and the chain is unique.*

::: {#thm-rational-canonical-form}
[Rational Canonical Form]

Let \( V \ne \{\0\} \) be a finite-dimensional vector space over **any** field \( F \), and let \( T \in \cL(V) \) have invariant factors \( d_1 \mid d_2 \mid \dots \mid d_r \). Then there is a basis \( \sB \) of \( V \) with
\[
[T]_{\sB} = C(d_1) \oplus C(d_2) \oplus \dots \oplus C(d_r) ,
\]
and this matrix is determined by \( T \). It is called the **rational canonical form** of \( T \). Equivalently, every \( A \in M_n(F) \) with \( n \ge 1 \) is similar to exactly one matrix of the form \( C(d_1) \oplus \dots \oplus C(d_r) \) with \( d_1 \mid \dots \mid d_r \) monic and non-constant.
:::

::: {.proof}
By @thm-cyclic-decomposition, \( V = Z(\v_1;T) \oplus \dots \oplus Z(\v_r;T) \) with \( m_{T,\v_j} = d_j \). Each piece is \( T \)-invariant and non-zero, and by @thm-cyclic-subspace-basis (a), (b) the list \( \sB_j = (\v_j, T\v_j, \dots, T^{\deg d_j - 1}\v_j) \) is a basis of \( Z(\v_j;T) \) in which the matrix of the restriction is \( C(d_j) \). Let \( \sB \) be \( \sB_1, \dots, \sB_r \) written one after another; by @thm-direct-sum-invariant-block-diagonal, \( \sB \) is a basis of \( V \) and \( [T]_{\sB} = C(d_1) \oplus \dots \oplus C(d_r) \). The blocks are determined by \( T \), since the \( d_j \) are (@cor-invariant-factors-unique (a)).

For a matrix \( A \in M_n(F) \), apply this to \( T_A \) and use @thm-similar-iff-same-operator. For the uniqueness in the matrix form, suppose \( A \sim C(f_1) \oplus \dots \oplus C(f_s) \) with \( f_1 \mid \dots \mid f_s \) monic and non-constant. By @thm-similar-iff-same-operator there is a basis \( \sC \) of \( F^n \) with \( [T_A]_{\sC} = C(f_1) \oplus \dots \oplus C(f_s) \). Let \( U_j \) be the span of the segment of \( \sC \) belonging to the \( j \)-th block; then \( F^n = U_1 \oplus \dots \oplus U_s \) with each \( U_j \) invariant and \( [T_A|_{U_j}] = C(f_j) \) (@thm-direct-sum-invariant-block-diagonal). By @thm-companion-char-min, @thm-minimal-polynomial-similarity and @def-charpoly-operator, \( m_{T_A|_{U_j}} = p_{T_A|_{U_j}} = f_j \), so \( T_A|_{U_j} \) is cyclic (@thm-cyclic-iff-min-equals-char) and \( U_j = Z(\u_j; T_A) \) for some \( \u_j \) with \( m_{T_A,\u_j} = f_j \) (@thm-cyclic-subspace-basis (c)). This is a decomposition as in @thm-cyclic-decomposition, so \( (f_1, \dots, f_s) = (d_1, \dots, d_r) \) by @cor-invariant-factors-unique (a). Hence the matrix is the rational canonical form of \( A \).
:::

This pays off the promise made in Section 3: **there is a canonical form over every field.** No hypothesis on \( F \) was used, and none is needed. The form is canonical in the strong sense: the blocks come in a prescribed order, dictated by divisibility, so two operators have the *same* form, not merely similar forms.

::: {#cor-similar-iff-same-invariant-factors}
[Similarity via the Invariant Factors]

Let \( A, B \in M_n(F) \) with \( n \ge 1 \). The following are equivalent:

::: {.enumerate options="label=(\alph*)"}
1. \( A \sim B \);
2. \( A \) and \( B \) have the same invariant factors;
3. \( A \) and \( B \) have the same elementary divisors, up to order;
4. \( \dim\ker p(A)^{k} = \dim\ker p(B)^{k} \) for every monic irreducible \( p \in F[x] \) and every \( k \ge 1 \).
:::
:::

::: {.proof}
(a) ⇒ (d). If \( B = P^{-1}AP \), then \( p(B)^k = P^{-1}p(A)^kP \) (@prp-similarity-invariants (c)), so the two have the same rank (@prp-similarity-invariants (a)) and hence the same nullity (@thm-rank-nullity-matrix).

(d) ⇒ (b). By @cor-invariant-factors-unique (c), the invariant factors of a matrix are computed from the numbers \( \dim\ker p(\cdot)^{k} \) alone: those numbers give the counts \( c_p(k) \), which give the length \( r \) and the exponents \( v_p(d_j) \). Equal numbers therefore give equal invariant factors.

(b) ⇔ (c). The elementary divisors are the prime powers in the factorizations of the invariant factors (@def-invariant-factors), so (b) ⇒ (c). Conversely, \( c_p(k) \) is the number of elementary divisors of the form \( p^{f} \) with \( f \ge k \) (@cor-invariant-factors-unique (b) and (c)), so the list of elementary divisors determines every \( c_p(k) \), hence the invariant factors by @cor-invariant-factors-unique (c); so (c) ⇒ (b).

(b) ⇒ (a). Both matrices are similar to \( C(d_1) \oplus \dots \oplus C(d_r) \) (@thm-rational-canonical-form), and similarity is an equivalence relation (@exm-similarity).
:::

So the invariant factors are a **complete set of similarity invariants over every field**, which is the promise of Chapter 6 kept in full; @cor-similar-iff-same-jordan-form was the special case in which \( p_A \) splits. Counting similarity classes becomes counting divisibility chains: over any field, the classes of \( n \times n \) matrices with a given characteristic polynomial \( p \) correspond to the ways of writing \( p = d_1\cdots d_r \) with \( d_1 \mid \dots \mid d_r \) monic and non-constant.

::: {.warning}
**The invariant factors are not the factors of \( p_A \) in any naive sense, and \( m_A \) alone is only the last of them.** For \( A = \diag(1,1,2) \) over \( \nQ \) the invariant factors are \( d_1 = x - 1 \) and \( d_2 = (x-1)(x-2) = m_A \), and \( d_1d_2 = (x-1)^2(x-2) = p_A \); the factorization of \( p_A \) into linear factors plays no role in the chain. Nor does the chain have length \( \deg p_A \): here \( r = 2 \) for a \( 3 \times 3 \) matrix, and \( r = 1 \) exactly when \( A \) is cyclic (@thm-cyclic-iff-min-equals-char).
:::

## Elementary divisors, and the way back to Jordan

Cutting the pieces as finely as possible gives a second form, usually with more and smaller blocks.

::: {#thm-elementary-divisor-form}
[Elementary Divisor Form]

Let \( V \ne \{\0\} \) be finite-dimensional over \( F \), let \( T \in \cL(V) \), and let \( q_1, \dots, q_N \) be the elementary divisors of \( T \). Then there is a basis \( \sB \) of \( V \) with
\[
[T]_{\sB} = C(q_1) \oplus C(q_2) \oplus \dots \oplus C(q_N) ,
\]
and the blocks are determined by \( T \) up to their order.
:::

::: {.proof}
By @thm-cyclic-decomposition (d) there is a decomposition \( V = \bigoplus_{i,j} Z(\v_{ij}; T) \) into cyclic subspaces whose annihilators are prime powers, and by @cor-invariant-factors-unique (b) those annihilators are exactly the elementary divisors \( q_1, \dots, q_N \) of \( T \), up to order. Take the basis of @thm-cyclic-subspace-basis (a) in each piece and concatenate; @thm-cyclic-subspace-basis (b) and @thm-direct-sum-invariant-block-diagonal give the displayed matrix. The list of blocks depends on \( T \) alone, again by @cor-invariant-factors-unique (b).
:::

When the characteristic polynomial splits, this is the Jordan form in disguise, because a companion block for a power of a linear polynomial is a Jordan block.

::: {#cor-companion-linear-power-is-jordan}
[Companion Blocks of Linear Powers Are Jordan Blocks]

Let \( \lambda \in F \) and \( k \ge 1 \). Then
\[
C\big((x - \lambda)^k\big) \sim J_k(\lambda) .
\]
Consequently, if \( p_T \) splits over \( F \), then the elementary divisors of \( T \) are the polynomials \( (x - \lambda)^k \) for the Jordan blocks \( J_k(\lambda) \) of \( T \), and the elementary divisor form of @thm-elementary-divisor-form and the Jordan form of \( T \) are obtained from one another by replacing each block \( C\big((x-\lambda)^k\big) \) by \( J_k(\lambda) \) and conversely.
:::

::: {.proof}
Put \( J = J_k(\lambda) \). Then \( J - \lambda I = J_k(0) \) satisfies \( J_k(0)^k = 0 \ne J_k(0)^{k-1} \), so \( (x - \lambda)^k \) annihilates \( J \) and no smaller power does; by @lem-monic-divisors and @thm-minimal-polynomial-divides, \( m_J = (x-\lambda)^k \). Also \( p_J = (x - \lambda)^k \) (@thm-det-triangular), so \( m_J = p_J \) and \( J \) is cyclic (@thm-cyclic-iff-min-equals-char). By the last sentence of that theorem, \( J \) is similar to \( C(m_J) = C\big((x-\lambda)^k\big) \).

Now suppose \( p_T \) splits and let \( \sB \) be a Jordan basis, with \( [T]_{\sB} = J_{k_1}(\mu_1) \oplus \dots \oplus J_{k_m}(\mu_m) \) (@thm-jordan-canonical-form). Each block corresponds to a \( T \)-invariant subspace \( U_l \), spanned by the segment of \( \sB \) belonging to it, with \( V = U_1 \oplus \dots \oplus U_m \) and \( [T|_{U_l}] = J_{k_l}(\mu_l) \). By the first paragraph, \( m_{T|_{U_l}} = p_{T|_{U_l}} = (x - \mu_l)^{k_l} \), so \( T|_{U_l} \) is cyclic: there is \( \v_l \in U_l \) with \( U_l = Z(\v_l; T) \) and \( m_{T,\v_l} = (x-\mu_l)^{k_l} \) (@thm-cyclic-iff-min-equals-char, @thm-cyclic-subspace-basis (c)). Since \( x - \mu_l \) is irreducible, being of degree \( 1 \), this exhibits \( V \) as a direct sum of cyclic subspaces with prime-power annihilators, so by @cor-invariant-factors-unique (b) the elementary divisors of \( T \) are exactly the polynomials \( (x - \mu_l)^{k_l} \). Replacing each Jordan block by the similar companion block, or conversely, therefore turns one form into the other.
:::

::: {.remark}
The two forms carry the same information in different shapes, and each is better for something. The rational canonical form of @thm-rational-canonical-form has the fewest blocks and reads off \( m_T = d_r \) at a glance; the elementary divisor form has the most blocks and reads off the primes, and over a splitting field it is the Jordan form. The rational form is also called the **Frobenius normal form**. The word *rational* refers to the field: the form is computed by rational operations in \( F \), with no root extraction, which is exactly why it exists over every field.
:::

## Similarity does not depend on the field

Here is a striking consequence, and one that would be hard to guess. Two rational matrices might conceivably be conjugate by a complex matrix and by no rational one. They cannot be.

::: {#lem-rank-field-independent}
[Rank Does Not Change with the Field]

Let \( K \) be a subfield of a field \( L \) and let \( M \in M_{m \times n}(K) \). Then the rank of \( M \) computed over \( K \) equals its rank computed over \( L \).
:::

::: {.proof}
If \( M = 0 \), both ranks are \( 0 \). Otherwise, by @thm-rank-via-minors (a), each rank is the largest \( k \) such that some \( k \times k \) minor of \( M \) is non-zero. The minors are determinants of submatrices of \( M \), computed by the Leibniz formula from the entries of \( M \) (@def-determinant), so they are the **same elements of \( K \)** whichever field we regard \( M \) in. And an element of \( K \) is zero in \( K \) if and only if it is zero in \( L \). So the two largest such \( k \) agree.
:::

::: {#cor-similarity-field-independent}
[Similarity Is Independent of the Field]

Let \( K \) be a subfield of \( L \) and let \( A, B \in M_n(K) \), \( n \ge 1 \). If \( A \) and \( B \) are similar over \( L \), then they are similar over \( K \):
\[
A = Q^{-1}BQ \ \text{ for some invertible } Q \in M_n(L) \implies A = P^{-1}BP \ \text{ for some invertible } P \in M_n(K) .
\]
:::

::: {.idea}
Similarity over \( K \) is decided by the numbers \( \dim\ker p(A)^k \) for the monic irreducibles \( p \) of \( K[x] \) (@cor-similar-iff-same-invariant-factors). Each such number is a nullity of a matrix with entries in \( K \), and nullities do not notice a larger field. Similarity over \( L \) makes the numbers agree when computed over \( L \), hence over \( K \).
:::

::: {.proof}
Let \( p \in K[x] \) be monic irreducible and \( k \ge 1 \). The matrices \( p(A)^k \) and \( p(B)^k \) have entries in \( K \). Since \( A \) and \( B \) are similar over \( L \), say \( A = Q^{-1}BQ \), we have \( p(A)^k = Q^{-1}p(B)^kQ \) (@prp-similarity-invariants (c)), so these two matrices have the same rank over \( L \) (@prp-similarity-invariants (a)). By @lem-rank-field-independent their ranks over \( K \) are the same numbers, hence
\[
\dim\ker p(A)^{k} = n - \rank p(A)^k = n - \rank p(B)^k = \dim\ker p(B)^{k}
\]
over \( K \), by @thm-rank-nullity-matrix. As \( p \) and \( k \) were arbitrary, @cor-similar-iff-same-invariant-factors ((d) ⇒ (a)) gives \( A \sim B \) over \( K \).
:::

The invariant factors are computed in \( K[x] \) and never need a root; that is the whole reason. Note what the corollary does **not** say: the invariant factors themselves do change with the field, since the irreducible polynomials do. Over \( \nQ \) the matrix \( C\big((x^2+1)^2\big) \) has the single invariant factor \( (x^2+1)^2 \) and the single elementary divisor \( (x^2+1)^2 \); over \( \nC \) its invariant factor is unchanged, but its elementary divisors are \( (x-i)^2 \) and \( (x+i)^2 \), and its Jordan form is \( J_2(i) \oplus J_2(-i) \). What is field-independent is the **answer to the similarity question**, not the bookkeeping.

## Computing the forms

::: {.algorithm}
**Invariant factors, elementary divisors and the two forms of \( A \in M_n(F) \).**

1. Compute \( p_A \) and factor it into monic irreducibles over \( F \): \( p_A = p_1^{a_1}\cdots p_k^{a_k} \).
2. For each \( i \) and each \( k \ge 1 \), compute \( \dim\ker p_i(A)^k \) until it stops growing, and read off the exponents of the elementary divisors for \( p_i \) from @prp-elementary-divisors-from-kernels, subtracting twice for exact counts. (Equivalently: find \( m_A \) and, in small cases, use \( \sum_{i,j} e_{ij}\deg p_i = n \) with \( \max_j e_{ij} = \) the exponent of \( p_i \) in \( m_A \).)
3. Group the exponents of each prime into a row, in decreasing order, and multiply down the columns, numbering them backwards: the first column gives \( d_r = m_A \), the second \( d_{r-1} \), the last \( d_1 \).
4. Write \( C(d_1) \oplus \dots \oplus C(d_r) \), or \( \bigoplus_{i,j} C(p_i^{e_{ij}}) \).
5. For a basis: find a cyclic generator for each piece, as in Section 5.
:::

::: {#exm-invariant-factors-from-data}
[Invariant Factors from Polynomial Data]

Let \( T \) be an operator on a \( 6 \)-dimensional \( \nQ \)-vector space with
\[
p_T = (x-1)^2(x^2+1)^2, \qquad m_T = (x-1)(x^2+1)^2 .
\]
Find the elementary divisors, the invariant factors, the rational canonical form (@thm-rational-canonical-form) and the elementary divisor form (@thm-elementary-divisor-form).
:::

::: {.solution}
*The primes.* \( x - 1 \) and \( x^2+1 \) are monic irreducible over \( \nQ \) (the second has no rational root, @thm-irreducible-deg-2-3 (b)), and \( \deg p_T = 2 + 4 = 6 \) as it must be.

*The exponents.* The elementary divisors are powers \( (x-1)^{a} \) and \( (x^2+1)^{b} \). For each prime, the largest exponent occurring is its exponent in \( m_T = d_r \) (@thm-cyclic-decomposition (b), @def-invariant-factors), and the exponents weighted by the degrees sum to \( \deg p_T \) (@thm-cyclic-decomposition (c)). For \( x - 1 \): the largest exponent is \( 1 \) and the total contribution is \( 2 \), so there are two elementary divisors \( x-1 \). For \( x^2+1 \): the largest exponent is \( 2 \) and the total contribution is \( 4 = 2\cdot 2 \), so there is exactly one elementary divisor \( (x^2+1)^2 \). Hence the elementary divisors are
\[
x - 1, \qquad x-1, \qquad (x^2+1)^2 .
\]

*The invariant factors.* Arrange the exponents by prime in decreasing order:
\[
x - 1 : \ 1, 1; \qquad x^2 + 1 : \ 2 .
\]
So \( r = \max(2, 1) = 2 \), and multiplying down the columns, the first giving \( d_2 \) and the second \( d_1 \),
\[
d_2 = (x-1)(x^2+1)^2 = m_T, \qquad d_1 = x - 1 .
\]
Check: \( d_1 \mid d_2 \) and \( d_1d_2 = (x-1)^2(x^2+1)^2 = p_T \).

*The forms.* With \( d_2 = (x-1)(x^2+1)^2 = (x-1)(x^4+2x^2+1) = x^5 - x^4 + 2x^3 - 2x^2 + x - 1 \),
\[
C(d_1) \oplus C(d_2) = (1) \oplus \begin{pmatrix} 0 & 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 & -1 \\ 0 & 1 & 0 & 0 & 2 \\ 0 & 0 & 1 & 0 & -2 \\ 0 & 0 & 0 & 1 & 1 \end{pmatrix},
\]
of total size \( 1 + 5 = 6 \). The elementary divisor form is smaller-blocked:
\[
C(x-1) \oplus C(x-1) \oplus C\big((x^2+1)^2\big) = (1) \oplus (1) \oplus \begin{pmatrix} 0 & 0 & 0 & -1 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & -2 \\ 0 & 0 & 1 & 0 \end{pmatrix},
\]
of total size \( 1 + 1 + 4 = 6 \). Read as a complex matrix, the second form splits further: over \( \nC \) we have \( x^2 + 1 = (x-i)(x+i) \), so the elementary divisors become \( x-1, x-1, (x-i)^2, (x+i)^2 \) — the invariant factors \( d_1, d_2 \) are unchanged — and @cor-companion-linear-power-is-jordan turns the elementary divisor form into the Jordan form \( (1) \oplus (1) \oplus J_2(i) \oplus J_2(-i) \). Over \( \nQ \) no further splitting is possible, since \( x^2+1 \) is irreducible there.
:::

::: {#exm-rational-form-4x4}
[The Rational Canonical Form of a Matrix over the Rationals]

Let
\[
A = \begin{pmatrix} 0 & -1 & 1 & 0 \\ 1 & 0 & 0 & 1 \\ 0 & 0 & 0 & -1 \\ 0 & 0 & 1 & 0 \end{pmatrix} \in M_4(\nQ), \qquad p_A = (x^2+1)^2 .
\]
Find the invariant factors of \( A \), its rational canonical form (@thm-rational-canonical-form), and an invertible \( P \in M_4(\nQ) \) realizing it.
:::

::: {.solution}
*The characteristic polynomial.* In \( 2 \times 2 \) blocks, \( A = \begin{pmatrix} R & I_2 \\ 0 & R \end{pmatrix} \) with \( R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \), so \( xI - A \) is block upper triangular and \( p_A = (\det(xI_2 - R))^2 = (x^2+1)^2 \) (@thm-det-block-triangular), as stated.

*The minimal polynomial.* By @thm-minimal-polynomial-divides and @lem-monic-divisors, \( m_A \) is \( x^2+1 \) or \( (x^2+1)^2 \). Compute \( A^2 \): its columns are \( A \) applied to the columns of \( A \). With \( \c_1, \dots, \c_4 \) the columns of \( A \),
\[
A\c_1 = A(0,1,0,0) = (-1,0,0,0), \qquad A\c_2 = A(-1,0,0,0) = (0,-1,0,0),
\]
\[
A\c_3 = A(1,0,0,1) = (0,1,0,0) + (0,1,-1,0) = (0,2,-1,0), \qquad A\c_4 = A(0,1,-1,0) = (-1,0,0,0) + (-1,0,0,-1) = (-2,0,0,-1).
\]
So
\[
A^2 = \begin{pmatrix} -1 & 0 & 0 & -2 \\ 0 & -1 & 2 & 0 \\ 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & -1 \end{pmatrix}, \qquad A^2 + I = \begin{pmatrix} 0 & 0 & 0 & -2 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} \ne 0 .
\]
Hence \( m_A = (x^2+1)^2 = p_A \), and \( A \) is cyclic (@thm-cyclic-iff-min-equals-char). So \( r = 1 \), the single invariant factor is \( d_1 = (x^2+1)^2 = x^4 + 2x^2 + 1 \), and the rational canonical form is
\[
C(d_1) = \begin{pmatrix} 0 & 0 & 0 & -1 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & -2 \\ 0 & 0 & 1 & 0 \end{pmatrix}.
\]
The elementary divisor form (@thm-elementary-divisor-form) is the same matrix, since \( x^2+1 \) is irreducible over \( \nQ \) and \( d_1 \) is already a prime power.

*A cyclic vector.* By @thm-cyclic-iff-min-equals-char we need \( \v \) with \( m_{A,\v} = m_A \); since \( A^2 + I \ne 0 \), pick \( \v \) with \( (A^2+I)\v \ne \0 \). The third column of \( A^2 + I \) is non-zero, so \( \v = \e_3 \) works: then \( (A^2+I)\v \ne \0 \), so \( m_{A,\v} \nmid x^2+1 \), and as \( m_{A,\v} \) divides \( (x^2+1)^2 \) it must equal \( (x^2+1)^2 \) (@lem-monic-divisors). Its chain is
\[
\v = (0,0,1,0), \quad A\v = (1,0,0,1), \quad A^2\v = (0,2,-1,0), \quad A^3\v = A(0,2,-1,0) = (-2,0,0,0) + (-1,0,0,-1) = (-3,0,0,-1) ,
\]
reading columns of \( A \) as before. Hence
\[
P = \begin{pmatrix} 0 & 1 & 0 & -3 \\ 0 & 0 & 2 & 0 \\ 1 & 0 & -1 & 0 \\ 0 & 1 & 0 & -1 \end{pmatrix}, \qquad P^{-1}AP = C\big((x^2+1)^2\big) .
\]
*Invertibility of \( P \).* Expanding \( \det P \) along the third row, whose entries are \( (1, 0, -1, 0) \) (@thm-laplace-expansion), and then each \( 3 \times 3 \) determinant along its own first column,
\[
\det P = 1\cdot\det\begin{pmatrix} 1 & 0 & -3 \\ 0 & 2 & 0 \\ 1 & 0 & -1 \end{pmatrix} + (-1)(-1)^{3+3}\det\begin{pmatrix} 0 & 1 & -3 \\ 0 & 0 & 0 \\ 0 & 1 & -1 \end{pmatrix} = 1\cdot\big(2(-1+3)\big) - 0 = 4 \ne 0 ,
\]
the second determinant vanishing because it has a zero row, and the first being \( 2\det\begin{pmatrix} 1 & -3 \\ 1 & -1 \end{pmatrix} = 2 \cdot 2 = 4 \) by expansion along its second row.

*The check.* The identity \( AP = P\,C(d_1) \) reads column by column as \( A\v = A\v \), \( A(A\v) = A^2\v \), \( A(A^2\v) = A^3\v \) — true by construction — and
\[
A(A^3\v) = -\v - 2A^2\v ,
\]
which is the annihilator relation \( A^4 + 2A^2 + I = 0 \) applied to \( \v \). Verifying it directly: \( A(-3,0,0,-1) = -3(0,1,0,0) - (0,1,-1,0) = (0,-4,1,0) \), while
\[
-\v - 2A^2\v = -(0,0,1,0) - 2(0,2,-1,0) = (0, -4, 2 - 1, 0) = (0,-4,1,0) . \checkmark
\]
:::

## Exercises

### A. Check your understanding

:::: {#exr-rational-canonical-form-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the Cyclic Decomposition Theorem, including the divisibility chain and what \( d_r \) and \( \prod_j d_j \) are.
2. Define the invariant factors and the elementary divisors of \( T \).
3. What is the rational canonical form of \( T \), and over which fields does it exist?
4. True or false: two matrices in \( M_n(\nQ) \) that are similar over \( \nC \) are similar over \( \nQ \). Justify your answer.
5. An operator on a \( 5 \)-dimensional \( \nQ \)-space has \( p_T = (x-3)^5 \) and \( m_T = (x-3)^2 \). What are its elementary divisors and invariant factors?
6. True or false: \( r = 1 \) if and only if \( T \) is cyclic. Justify your answer.
:::
::::

::: {.solution}
(a) For \( V \ne \{\0\} \) finite-dimensional and \( T \in \cL(V) \), there are \( \v_1, \dots, \v_r \) with \( V = Z(\v_1;T) \oplus \dots \oplus Z(\v_r;T) \) and \( m_{T,\v_j} = d_j \), where \( d_1 \mid d_2 \mid \dots \mid d_r \) are monic and non-constant, \( d_r = m_T \) and \( d_1\cdots d_r = p_T \) (@thm-cyclic-decomposition).

(b) The invariant factors are the polynomials \( d_1 \mid \dots \mid d_r \) of that theorem; the elementary divisors are the prime powers occurring in their factorizations, listed with repetition (@def-invariant-factors). Both are determined by \( T \) (@cor-invariant-factors-unique).

(c) The matrix \( C(d_1) \oplus \dots \oplus C(d_r) \), which is \( [T]_{\sB} \) for a suitable basis; it exists over **every** field (@thm-rational-canonical-form).

(d) True, by @cor-similarity-field-independent with \( K = \nQ \) and \( L = \nC \).

(e) Elementary divisors are powers of \( x - 3 \) with largest exponent \( 2 \) and exponents summing to \( 5 \): so \( (x-3)^2, (x-3)^2, x-3 \). The exponents, in decreasing order, are \( 2, 2, 1 \); numbering the columns backwards gives \( d_3 = (x-3)^2 = m_T \), \( d_2 = (x-3)^2 \) and \( d_1 = x - 3 \).

(f) True. \( r = 1 \) means \( V = Z(\v_1;T) \), that is, \( \v_1 \) is a cyclic vector; conversely if \( \v \) is cyclic, then \( d_1 = m_{T,\v} = m_T = p_T \) is the only invariant factor, by @thm-cyclic-iff-min-equals-char and the uniqueness in @cor-invariant-factors-unique.
:::

### B. Practice

:::: {#exr-rational-canonical-form-b1}
[B1: Invariant factors from given data]

In each case \( T \) is an operator on a \( \nQ \)-vector space with the stated characteristic and minimal polynomials. Find the elementary divisors, the invariant factors, and the rational canonical form (@thm-rational-canonical-form).

::: {.enumerate options="label=(\alph*)"}
1. \( p_T = (x-2)^4 \), \( m_T = (x-2)^2 \).
2. \( p_T = (x^2 - 2)^3 \), \( m_T = (x^2-2)^2 \).
3. \( p_T = (x-1)^2(x+1)^2 \), \( m_T = (x-1)(x+1) \).
:::
::::

::: {.solution}
(a) Powers of \( x - 2 \) with largest exponent \( 2 \) and exponents summing to \( 4 \): either \( 2, 2 \) or \( 2, 1, 1 \). So the data do **not** determine the answer; both
\[
\text{elementary divisors } (x-2)^2, (x-2)^2 \quad\text{and}\quad (x-2)^2, x-2, x-2
\]
are possible, with invariant factors \( \big((x-2)^2, (x-2)^2\big) \) and \( \big(x-2, x-2, (x-2)^2\big) \) and rational forms
\[
C\big((x-2)^2\big) \oplus C\big((x-2)^2\big), \qquad (2) \oplus (2) \oplus C\big((x-2)^2\big),
\]
where \( C\big((x-2)^2\big) = C(x^2 - 4x + 4) = \begin{pmatrix} 0 & -4 \\ 1 & 4 \end{pmatrix} \). (The extra datum that decides is \( \dim\ker(T - 2\,\id) \), which is \( 2 \) in the first case and \( 3 \) in the second, by @prp-elementary-divisors-from-kernels.)

(b) \( x^2 - 2 \) is irreducible over \( \nQ \), since \( \sqrt2 \notin \nQ \) (@thm-sqrt2-irrational, @thm-irreducible-deg-2-3 (b)). The exponents are powers of \( x^2-2 \) with largest \( 2 \) summing to \( 3 \): only \( 2, 1 \). So the elementary divisors are \( (x^2-2)^2 \) and \( x^2 - 2 \), the invariant factors are \( d_1 = x^2 - 2 \) and \( d_2 = (x^2-2)^2 = x^4 - 4x^2 + 4 \), and the rational form is
\[
C(x^2-2) \oplus C\big((x^2-2)^2\big) = \begin{pmatrix} 0 & 2 \\ 1 & 0 \end{pmatrix} \oplus \begin{pmatrix} 0 & 0 & 0 & -4 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 4 \\ 0 & 0 & 1 & 0 \end{pmatrix},
\]
of size \( 2 + 4 = 6 = \deg p_T \).

(c) Both primes have largest exponent \( 1 \) and total contribution \( 2 \), so the elementary divisors are \( x-1, x-1, x+1, x+1 \). Arranging by prime, \( x-1: 1,1 \) and \( x+1 : 1,1 \), so \( r = 2 \) and \( d_2 = (x-1)(x+1) = m_T \), \( d_1 = (x-1)(x+1) \). The rational form is
\[
C(x^2-1) \oplus C(x^2-1) = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \oplus \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} .
\]
(This operator is diagonalizable, with \( \diag(1,1,-1,-1) \) as its Jordan form; the rational form is a different matrix representing the same operator.)
:::

:::: {#exr-rational-canonical-form-b2}
[B2: Rational forms of matrices]

For each matrix, find \( p_A \), \( m_A \), the invariant factors, the rational canonical form (@thm-rational-canonical-form) and the elementary divisor form (@thm-elementary-divisor-form).

::: {.enumerate options="label=(\alph*)"}
1. \( A_1 = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix} \in M_3(\nQ) \).
2. \( A_2 = \diag(1, 1, 2) \in M_3(\nQ) \).
3. \( A_3 = \begin{pmatrix} 0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & -1 \\ 0 & 0 & 1 & 0 \end{pmatrix} \in M_4(\nQ) \).
:::
::::

::: {.solution}
(a) Reading the columns, \( A_1\e_1 = \e_3 \), \( A_1\e_3 = \e_2 \) and \( A_1\e_2 = \e_1 \), so \( A_1^3 = I \) and the polynomial \( x^3 - 1 \) annihilates \( A_1 \). Also \( A_1^2\e_1 = A_1\e_3 = \e_2 \), so \( (\e_1, A_1\e_1, A_1^2\e_1) = (\e_1, \e_3, \e_2) \) is a basis of \( \nQ^3 \) and \( \e_1 \) is a cyclic vector. Hence \( \deg m_{A_1} = 3 \) (@thm-cyclic-iff-min-equals-char), and since \( m_{A_1} \) is monic of degree \( 3 \) dividing \( x^3 - 1 \), we get \( m_{A_1} = p_{A_1} = x^3 - 1 \). The single invariant factor is \( d_1 = x^3 - 1 \), and the rational canonical form is
\[
C(x^3-1) = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} .
\]
Over \( \nQ \), \( x^3 - 1 = (x-1)(x^2+x+1) \) with both factors irreducible (the quadratic has no rational root). So the elementary divisors are \( x - 1 \) and \( x^2+x+1 \), and the elementary divisor form is
\[
(1) \oplus C(x^2+x+1) = (1) \oplus \begin{pmatrix} 0 & -1 \\ 1 & -1 \end{pmatrix} .
\]

(b) \( p_{A_2} = (x-1)^2(x-2) \) and \( m_{A_2} = (x-1)(x-2) \) (@prp-minimal-polynomial-block-diagonal). Elementary divisors: \( x - 1, x-1, x-2 \). Invariant factors: \( d_2 = (x-1)(x-2) = m_{A_2} \) and \( d_1 = x-1 \). Rational form
\[
(1) \oplus C\big((x-1)(x-2)\big) = (1) \oplus \begin{pmatrix} 0 & -2 \\ 1 & 3 \end{pmatrix},
\]
elementary divisor form \( (1) \oplus (1) \oplus (2) = \diag(1,1,2) = A_2 \) itself.

(c) \( A_3 = R \oplus R \) with \( R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \), and \( p_R = x^2+1 \), \( m_R = x^2+1 \), so \( p_{A_3} = (x^2+1)^2 \) (@thm-det-block-triangular applied to \( xI - A_3 \), which is block diagonal over \( \nQ[x] \)) and \( m_{A_3} = \operatorname{lcm}(x^2+1, x^2+1) = x^2+1 \) (@prp-minimal-polynomial-block-diagonal). Since \( x^2+1 \) is irreducible over \( \nQ \), the elementary divisors are \( x^2+1 \) and \( x^2+1 \); \( r = 2 \) and \( d_1 = d_2 = x^2+1 \). Both forms are
\[
C(x^2+1) \oplus C(x^2+1) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \oplus \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = A_3 .
\]
Compare @exm-rational-form-4x4: that matrix has the same characteristic polynomial but a different minimal polynomial, so the two are **not** similar.
:::

:::: {#exr-rational-canonical-form-b3}
[B3: Counting similarity classes over a finite field]

Work over \( F = \nF_2 \). For each polynomial \( p \), find the number of similarity classes of matrices \( A \in M_3(\nF_2) \) with \( p_A = p \), and list the invariant factors of each class.

::: {.enumerate options="label=(\alph*)"}
1. \( p = (x+1)^3 \).
2. \( p = x(x+1)^2 \).
3. \( p = x^3 + x + 1 \).
:::

*Hint: by @cor-similar-iff-same-invariant-factors, a class is a way of writing \( p = d_1\cdots d_r \) with \( d_1 \mid \dots \mid d_r \).*
::::

::: {.solution}
(a) The only prime involved is \( x+1 \), so the elementary divisors are powers \( (x+1)^{a} \) with exponents forming a partition of \( 3 \). The three partitions \( (3) \), \( (2,1) \), \( (1,1,1) \) give
\[
\big((x+1)^3\big), \qquad \big(x+1,\ (x+1)^2\big), \qquad \big(x+1,\ x+1,\ x+1\big)
\]
as lists of invariant factors. So there are \( 3 \) classes, with representatives \( C\big((x+1)^3\big) \), \( (1) \oplus C\big((x+1)^2\big) \) and \( I_3 \) (note \( -1 = 1 \) in \( \nF_2 \)).

(b) Now two primes, \( x \) with total exponent \( 1 \) and \( x+1 \) with total exponent \( 2 \). For \( x \) the only option is the single elementary divisor \( x \); for \( x+1 \) the options are \( (x+1)^2 \) or \( x+1, x+1 \). So there are \( 2 \) classes, with invariant factors
\[
\big(x(x+1)^2\big) \qquad\text{and}\qquad \big(x+1,\ x(x+1)\big) .
\]
In the first case \( r = 1 \) and the matrix is cyclic; in the second \( r = 2 \).

(c) \( x^3 + x + 1 \) has no root in \( \nF_2 \) (its values at \( 0 \) and \( 1 \) are \( 1 \) and \( 1 \)), so it is irreducible (@thm-irreducible-deg-2-3 (b)). A prime of degree \( 3 \) in a characteristic polynomial of degree \( 3 \) can occur only with exponent \( 1 \), so the only possible list of elementary divisors is \( (x^3+x+1) \) itself: \( 1 \) class, represented by \( C(x^3+x+1) \).
:::

### C. Going deeper

:::: {#exr-rational-canonical-form-c1}
[C1: Which matrices are companion matrices]

Let \( A \in M_n(F) \) with \( n \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( A \) is similar to a companion matrix if and only if \( m_A = p_A \), and that the companion matrix is then \( C(p_A) \).
2. Deduce that \( A \) is similar to a companion matrix if and only if its rational canonical form has exactly one block.
3. Give an example of a matrix in \( M_2(F) \) that is not similar to any companion matrix.
:::
::::

::: {.solution}
(a) (⇐) If \( m_A = p_A \), then \( A \) is cyclic (@thm-cyclic-iff-min-equals-char) and, in the basis generated by a cyclic vector, its matrix is \( C(m_A) = C(p_A) \); so \( A \sim C(p_A) \) (@thm-similar-iff-same-operator).

(⇒) Suppose \( A \sim C(q) \) for some monic \( q \). By @thm-companion-char-min, \( m_{C(q)} = p_{C(q)} = q \). Similar matrices share both polynomials (@thm-charpoly-similarity-invariant, @thm-minimal-polynomial-similarity), so \( m_A = p_A = q \), and the companion matrix is \( C(p_A) \).

(b) By @thm-rational-canonical-form the form has one block exactly when \( r = 1 \), that is, when \( d_1 = m_A = p_A \) (@thm-cyclic-decomposition (b), (c)). Now apply (a).

(c) \( I_2 \): here \( m = x - 1 \ne (x-1)^2 = p \). Concretely, \( I_2 \) is similar only to itself, and no companion matrix of a monic quadratic is \( I_2 \), since the \( (2,1) \) entry of \( C(q) \) is \( 1 \ne 0 \).
:::

:::: {#exr-rational-canonical-form-c2}
[C2: All similarity classes of two by two matrices over the smallest field]

Work over \( F = \nF_2 \), so that \( M_2(\nF_2) \) has \( 16 \) elements.

::: {.enumerate options="label=(\alph*)"}
1. List the four monic polynomials of degree \( 2 \) over \( \nF_2 \) and factor each into irreducibles.
2. For each, list the possible lists of invariant factors of a matrix \( A \in M_2(\nF_2) \) with that characteristic polynomial.
3. Conclude the total number of similarity classes in \( M_2(\nF_2) \), and give a representative of each.
4. Check your count against the orbit sizes: \( \lvert \GL_2(\nF_2)\rvert = 6 \), and the class of \( A \) has \( 6/\lvert\{P : P^{-1}AP = A\}\rvert \) elements.
:::
::::

::: {.solution}
(a) \( x^2 \); \( x^2 + 1 = (x+1)^2 \); \( x^2 + x = x(x+1) \); and \( x^2+x+1 \), which has no root in \( \nF_2 \) and is therefore irreducible (@thm-irreducible-deg-2-3 (b)).

(b) For \( p = x^2 \): elementary divisors \( x^2 \) (invariant factors \( (x^2) \)) or \( x, x \) (invariant factors \( (x, x) \)) — two options. For \( p = (x+1)^2 \): likewise two, \( \big((x+1)^2\big) \) and \( (x+1, x+1) \). For \( p = x(x+1) \): each prime occurs once, so the elementary divisors are \( x, x+1 \) and there is a single list of invariant factors, \( \big(x(x+1)\big) \). For the irreducible \( p = x^2+x+1 \): one option, \( (x^2+x+1) \).

(c) Total \( 2 + 2 + 1 + 1 = 6 \) classes, with representatives
\[
C(x^2) = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}, \quad 0, \quad C\big((x+1)^2\big) = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad I_2, \quad \diag(0,1), \quad C(x^2+x+1) = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix},
\]
using \( -1 = 1 \) in \( \nF_2 \). (For \( (x+1)^2 = x^2+1 \) the coefficients are \( a_0 = 1, a_1 = 0 \), so \( C = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \), the coordinate swap.)

(d) The two scalar matrices \( 0 \) and \( I_2 \) commute with everything, so their classes have \( 6/6 = 1 \) element each. For \( \diag(0,1) \), a matrix commutes with it exactly when it is diagonal (compare entries), and the invertible diagonal matrices over \( \nF_2 \) are only \( I_2 \), so the class has \( 6 \) elements. For \( C(x^2) \) and \( C(x^2+1) \) the commutant inside \( \GL_2 \) has \( 2 \) elements — by @exr-cyclic-subspaces-and-companion-matrices-c1 the commutant of a cyclic matrix is \( \{aI + bA\} \), which here has \( 4 \) elements, of which \( 2 \) are invertible — so each class has \( 3 \) elements. For \( C(x^2+x+1) \), whose order is \( 3 \) in \( \GL_2(\nF_2) \), the commutant is \( \{aI + bA\} \) again, with \( 3 \) invertible elements, so the class has \( 2 \) elements. Total:
\[
1 + 1 + 6 + 3 + 3 + 2 = 16 = \lvert M_2(\nF_2)\rvert . \checkmark
\]
:::

:::: {#exr-rational-canonical-form-c3}
[C3: A matrix over the rationals is similar to its transpose]

::: {.enumerate options="label=(\alph*)"}
1. Let \( A, B \in M_n(\nQ) \) have the same Jordan form over \( \nC \). Prove that \( A \) and \( B \) are similar over \( \nQ \).
2. Deduce that \( A \sim A\tp \) over \( \nQ \) for every \( A \in M_n(\nQ) \).
3. Which step of (b) would fail for a general field \( K \) in place of \( \nQ \)?
:::

*Hint for (b): @exr-jordan-canonical-form-c1.*
::::

::: {.solution}
(a) A matrix in \( M_n(\nQ) \) is also a matrix in \( M_n(\nC) \), and \( p_A \) splits over \( \nC \) (@cor-complex-polynomial-splits), so both have Jordan forms there. Having the same Jordan form, they are similar over \( \nC \) (@cor-similar-iff-same-jordan-form). By @cor-similarity-field-independent with \( K = \nQ \) and \( L = \nC \), they are similar over \( \nQ \).

(b) Let \( A \in M_n(\nQ) \). Over \( \nC \), \( p_A \) splits, so @exr-jordan-canonical-form-c1 (c) gives \( A \sim A\tp \) over \( \nC \). Both matrices lie in \( M_n(\nQ) \), so @cor-similarity-field-independent gives \( A \sim A\tp \) over \( \nQ \).

(c) The step that fails is the splitting: over a general field \( K \) there is no reason for \( p_A \) to split, and we have not constructed a larger field where it does. (The conclusion is nevertheless true over every field; Section 7 proves it without any splitting, using the Smith normal form of \( xI - A \).) Note that @cor-similarity-field-independent itself needs no hypothesis on \( K \) — only the existence of a suitable \( L \) does.
:::
