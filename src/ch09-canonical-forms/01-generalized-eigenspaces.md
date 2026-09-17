# Generalized Eigenspaces

Chapter 8 left one gap wide open. When an operator has too few eigenvectors, its eigenspaces are too small to fill the space, and diagonalization fails. The remedy of this chapter is to enlarge each eigenspace until the enlarged pieces do fill the space. This section builds the enlargement, shows that the enlarging process stops after finitely many steps, and proves that the pieces split \( V \) whenever the characteristic polynomial splits.

## Enlarging an eigenspace

Take the standing counterexample of Chapter 8,
\[
J = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} \in M_2(F),
\]
and let \( N = J - 2I \). The only eigenvalue is \( 2 \), and \( E_2(J) = \ker N = \Span(\e_1) \) is a line: one eigenvector direction where we need two, so \( J \) is not diagonalizable over any field (@thm-diagonalization (e)).

Now look at what \( N \) does to the missing direction \( \e_2 \). One application does not kill \( \e_2 \), but two do:
\[
N\e_2 = \e_1, \qquad N^2\e_2 = N\e_1 = \0 .
\]
So \( \e_2 \) is killed by \( N^2 \), and \( \ker N^2 = F^2 \) is everything. The eigenspace was too small, but the kernel of the **square** is as big as we could wish.

This is the whole idea. Instead of asking for vectors killed by \( T - \lambda\,\id_V \), ask for vectors killed by **some power** of \( T - \lambda\,\id_V \). The eigenvectors are still there (they are killed at the first step), and there may be more.

*A generalized eigenvector is a vector that some power of \( T - \lambda\,\id_V \) kills, not necessarily the first power.*

## Generalized eigenvectors and generalized eigenspaces

::: {#def-generalized-eigenvector}
[Generalized Eigenvector]

Let \( V \) be a vector space over \( F \), let \( T \in \cL(V) \) and \( \lambda \in F \). A **generalized eigenvector** of \( T \) for \( \lambda \) is a vector \( \v \in V \) with \( \v \ne \0 \) such that
\[
(T - \lambda\,\id_V)^k\,\v = \0 \qquad \text{for some integer } k \ge 1 .
\]
:::

In words: the vector must be **non-zero**, exactly as for an eigenvector; the scalar \( \lambda \) must lie **in \( F \)**; and the power \( k \) is not fixed in advance — it may depend on \( \v \). Taking \( k = 1 \) recovers the eigenvector condition, so **every eigenvector for \( \lambda \) is a generalized eigenvector for \( \lambda \)**.

Collecting all of them, together with \( \0 \), gives the space we are after.

::: {#def-generalized-eigenspace}
[Generalized Eigenspace]

Let \( V \) be a vector space over \( F \), let \( T \in \cL(V) \) and \( \lambda \in F \). The **generalized eigenspace** of \( T \) for \( \lambda \) is
\[
G_\lambda(T) \coloneqq \{\, \v \in V : (T - \lambda\,\id_V)^k\,\v = \0 \text{ for some integer } k \ge 1 \,\} = \bigcup_{k \ge 1} \ker (T - \lambda\,\id_V)^k .
\]
For \( A \in M_n(F) \) we write \( G_\lambda(A) = G_\lambda(T_A) \).
:::

So \( G_\lambda(T) \) consists of \( \0 \) together with all generalized eigenvectors for \( \lambda \). Writing \( N = T - \lambda\,\id_V \) for the rest of this subsection, the definition says \( G_\lambda(T) = \ker N \cup \ker N^2 \cup \ker N^3 \cup \dots \).

**Well-definedness: it really is a subspace.** A union of subspaces is almost never a subspace (@prp-union-subspaces), so this needs a check. What saves us is that the union is **increasing**: if \( N^k\v = \0 \), then \( N^{k+1}\v = N(N^k\v) = N\0 = \0 \), so
\[
\ker N \subseteq \ker N^2 \subseteq \ker N^3 \subseteq \dots
\]
Now use the subspace test (@thm-subspace-test). We have \( \0 \in \ker N \subseteq G_\lambda(T) \), so the set is non-empty. If \( \u, \v \in G_\lambda(T) \), say \( N^j\u = \0 \) and \( N^k\v = \0 \), put \( m = \max(j, k) \); then \( \u, \v \in \ker N^m \) by the inclusions above, and \( \ker N^m \) is a subspace, so \( \u + \v \) and \( c\u \) lie in \( \ker N^m \subseteq G_\lambda(T) \) for every \( c \in F \). Hence \( G_\lambda(T) \) is a subspace of \( V \).

**Examples.**

- **The standing counterexample.** For \( J = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} \), we computed \( \ker(J - 2I) = \Span(\e_1) \) and \( \ker(J - 2I)^2 = F^2 \). So \( G_2(J) = F^2 \), while \( E_2(J) \) is only a line. The generalized eigenspace is strictly bigger than the eigenspace, and it is all of \( F^2 \).
- **A diagonalizable operator gains nothing.** Let \( A = \diag(2, 5) \) over \( \nQ \). Then \( (A - 2I)^k = \diag(0, 3^k) \), whose kernel is \( \Span(\e_1) \) for every \( k \ge 1 \). So \( G_2(A) = E_2(A) = \Span(\e_1) \), and likewise \( G_5(A) = E_5(A) = \Span(\e_2) \). Enlarging an eigenspace of a diagonalizable operator does nothing, a fact we prove in general below.
- **Differentiation.** Let \( D \in \cL(F[x]_{\le n}) \) be differentiation. Then \( D^{n+1} = 0 \) (@exm-differentiation-nilpotent), so **every** polynomial is killed by a power of \( D \), that is, of \( D - 0\,\id \), and \( G_0(D) = F[x]_{\le n} \). By contrast \( E_0(D) = \ker D \) is the line of constants when \( F = \nR \). Here the generalized eigenspace for the single eigenvalue \( 0 \) is the whole space, of dimension \( n + 1 \).
- **A scalar not among the eigenvalues.** For the same \( A = \diag(2, 5) \) and \( \lambda = 7 \), the matrix \( (A - 7I)^k = \diag((-5)^k, (-2)^k) \) is invertible, so its kernel is \( \{\0\} \) for every \( k \). Hence \( G_7(A) = \{\0\} \). The definition makes sense for every \( \lambda \in F \), and gives the zero space unless \( \lambda \) is an eigenvalue.
- **A degenerate case.** On a space of dimension \( 1 \), every operator is \( \lambda\,\id \) for one scalar \( \lambda \), and \( G_\lambda = V \), \( G_\mu = \{\0\} \) for \( \mu \ne \lambda \). Small as it is, this is the model for a \( 1 \times 1 \) Jordan block.
- **No eigenvalues at all.** The rotation \( R \) of \( \nR^2 \) by a right angle has no real eigenvalue (@exm-rotation-invariant-subspaces), and indeed \( G_\lambda(R) = \{\0\} \) for every \( \lambda \in \nR \): if \( (R - \lambda I)^k\v = \0 \) with \( \v \ne \0 \), then \( R - \lambda I \) would not be injective, so \( \lambda \) would be an eigenvalue. Over \( \nC \), where \( p_R = x^2 + 1 = (x - i)(x + i) \) splits, \( G_i(R) \) and \( G_{-i}(R) \) are the two eigenlines.

**Non-example by minimal change.** Keep \( A = \diag(2, 5) \) over \( \nQ \) and take \( \v = (1, 1) \). This vector **is** killed by a polynomial in \( A \) whose roots are eigenvalues:
\[
(A - 2I)(A - 5I)\v = \0 ,
\]
as one checks entry by entry. But it is a generalized eigenvector for **neither** eigenvalue: \( (A - 2I)^k\v = (0, 3^k) \ne \0 \) and \( (A - 5I)^k\v = ((-3)^k, 0) \ne \0 \) for every \( k \ge 1 \). The failing clause is that the definition demands a power of a **single** factor \( T - \lambda\,\id_V \), not a product of different factors. (Of course \( \v = \e_1 + \e_2 \) is a *sum* of two generalized eigenvectors; that is the decomposition theorem below, not the definition.)

**Why this definition.** Three clauses are doing work. The vector must be non-zero, or every \( G_\lambda \) would contain a "generalized eigenvector" and the word would carry no information. The exponent must be allowed to grow, because nothing tells us in advance how many steps a vector needs: for \( D \) on \( \nR[x]_{\le n} \) the polynomial \( x^n \) needs \( n + 1 \) steps. And the power is a power of one factor, which is what makes \( G_\lambda \) one piece attached to one eigenvalue. The name is the honest one: these are the vectors that behave like eigenvectors after enough applications of \( T - \lambda\,\id_V \).

::: {.warning}
**\( G_\lambda(T) \) is usually bigger than \( E_\lambda(T) \), and "generalized eigenvector" includes the ordinary ones.** The inclusion \( E_\lambda(T) \subseteq G_\lambda(T) \) always holds, and it is strict exactly when \( T \) has too few eigenvectors for \( \lambda \): for \( J = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} \), \( \dim E_2 = 1 \) and \( \dim G_2 = 2 \). So a generalized eigenvector need not satisfy \( T\v = \lambda\v \): the vector \( \e_2 \) satisfies \( J\e_2 = \e_1 + 2\e_2 \). Conversely, do not read "generalized" as "not an eigenvector": every eigenvector is a generalized eigenvector.
:::

## The kernel chain stabilizes

The definition of \( G_\lambda(T) \) is an infinite union, which is awkward: to decide membership we would have to try every \( k \). In finite dimension this is an illusion. The chain \( \ker N \subseteq \ker N^2 \subseteq \dots \) is a chain of subspaces of \( V \), and their dimensions cannot keep growing. Once the chain stops growing, it stops forever.

::: {#thm-kernel-chain-stabilizes}
[The Kernel Chain Stabilizes]

Let \( V \) be a finite-dimensional vector space over \( F \) with \( \dim V = n \), let \( N \in \cL(V) \), and write \( K_k = \ker N^k \) for \( k \ge 0 \), so that \( K_0 = \{\0\} \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( K_0 \subseteq K_1 \subseteq K_2 \subseteq \dots \), and every \( K_k \) is \( N \)-invariant;
2. if \( K_m = K_{m+1} \) for some \( m \ge 0 \), then \( K_{m+j} = K_m \) for **every** \( j \ge 0 \);
3. there is a **least** index \( s \ge 0 \) with \( K_s = K_{s+1} \); it satisfies \( s \le n \), the inclusions
   \[
   K_0 \subsetneq K_1 \subsetneq \dots \subsetneq K_s
   \]
   are **strict**, and \( K_k = K_s \) for every \( k \ge s \);
4. in particular \( \ker N^n = \ker N^{n+j} \) for every \( j \ge 0 \).
:::
:::

::: {.idea}
The only real point is (b): equality at one step propagates. Read it backwards. To put \( \v \in K_{m+j+1} \) into \( K_{m+j} \), look at \( \w = N^j\v \). It lies in \( K_{m+1} \), which by hypothesis is \( K_m \), and that is exactly the statement \( N^{m+j}\v = \0 \). Then (c) and (d) are bookkeeping: while the inclusions are strict the dimensions go up by at least \( 1 \), so strictness cannot survive past step \( n \).
:::

::: {.proof}
(a) If \( N^k\v = \0 \), then \( N^{k+1}\v = N(N^k\v) = \0 \), so \( K_k \subseteq K_{k+1} \). Each \( K_k = \ker N^k \) is the kernel of a polynomial in \( N \), hence \( N \)-invariant by @thm-kernel-image-of-polynomial-invariant (b).

(b) Suppose \( K_m = K_{m+1} \). We prove \( K_{m+j} = K_m \) by induction on \( j \ge 0 \). For \( j = 0 \) there is nothing to prove. Assume \( K_{m+j} = K_m \), and let \( \v \in K_{m+j+1} \). Then
\[
N^{m+1}(N^j\v) = N^{m+j+1}\v = \0 ,
\]
so \( N^j\v \in K_{m+1} = K_m \), which says \( N^{m+j}\v = N^m(N^j\v) = \0 \). Hence \( \v \in K_{m+j} = K_m \). Together with \( K_m \subseteq K_{m+j+1} \) from (a), this gives \( K_{m+j+1} = K_m \).

(c) First, some \( m \) with \( 0 \le m \le n \) satisfies \( K_m = K_{m+1} \). Otherwise \( K_m \subsetneq K_{m+1} \) for every \( m = 0, 1, \dots, n \), so \( \dim K_{m+1} \ge \dim K_m + 1 \) for those \( m \), and hence \( \dim K_{n+1} \ge n + 1 \), contradicting \( \dim K_{n+1} \le \dim V = n \) (@thm-subspace-dimension). By the well-ordering principle (@thm-well-ordering) there is a least such index; call it \( s \), and \( s \le n \). For \( k < s \) minimality gives \( K_k \ne K_{k+1} \), so the inclusion \( K_k \subseteq K_{k+1} \) of (a) is strict. For \( k \ge s \), (b) gives \( K_k = K_s \).

(d) Since \( s \le n \), (c) gives \( K_n = K_s = K_{n+j} \) for every \( j \ge 0 \).
:::

::: {.check}
Can \( \ker N \subsetneq \ker N^2 = \ker N^3 \) happen? Can \( \ker N = \ker N^2 \subsetneq \ker N^3 \) happen?
:::

::: {.solution}
The first can: for \( N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) on \( F^2 \) we have \( \ker N = \Span(\e_1) \) and \( \ker N^2 = F^2 = \ker N^3 \), since \( N^2 = 0 \). Here \( s = 2 \).

The second cannot, by @thm-kernel-chain-stabilizes (b) with \( m = 1 \): equality at one step forces equality at every later step. This is why the theorem says the strict inclusions come **first** and the equalities **after**; the chain never resumes growing.
:::

The index \( s \) will come up often enough to name. We call the least \( s \ge 0 \) with \( \ker N^s = \ker N^{s+1} \) the **stabilization index** of \( N \). Part (d) is the useful form: the chain has certainly stopped by step \( n = \dim V \), whatever \( N \) is. Applying this to \( N = T - \lambda\,\id_V \) turns the infinite union in @def-generalized-eigenspace into a single kernel.

::: {#cor-generalized-eigenspace-is-kernel}
[The Generalized Eigenspace Is One Kernel]

Let \( V \) be a finite-dimensional vector space over \( F \) with \( \dim V = n \), let \( T \in \cL(V) \) and \( \lambda \in F \), and put \( N = T - \lambda\,\id_V \) with stabilization index \( s \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( G_\lambda(T) = \ker N^{s} = \ker N^{n} \);
2. \( G_\lambda(T) \) is \( T \)-invariant, and \( E_\lambda(T) \subseteq G_\lambda(T) \);
3. \( G_\lambda(T) \ne \{\0\} \) if and only if \( \lambda \) is an eigenvalue of \( T \);
4. if \( \v \in G_\lambda(T) \) is non-zero and \( k \ge 1 \) is **least** with \( N^k\v = \0 \), then \( N^{k-1}\v \) is an eigenvector of \( T \) for \( \lambda \).
:::
:::

::: {.proof}
(a) Every \( \ker N^k \) with \( k \ge 1 \) is contained in \( \ker N^{\max(k, n)} = \ker N^n \) by @thm-kernel-chain-stabilizes (a) and (d), so the union \( G_\lambda(T) \) equals \( \ker N^n \); and \( \ker N^n = \ker N^s \) by (c) of the same theorem, since \( s \le n \).

(b) By (a), \( G_\lambda(T) = \ker N^n \) is the kernel of a polynomial in \( T \), so \( T \) maps it into itself (@thm-kernel-image-of-polynomial-invariant (b)). And \( E_\lambda(T) = \ker N \subseteq \ker N^n \).

(c) (⇐) If \( \lambda \) is an eigenvalue, then \( E_\lambda(T) \ne \{\0\} \) (@thm-eigenvalue-characterizations), and \( E_\lambda(T) \subseteq G_\lambda(T) \) by (b). (⇒) If \( \v \in G_\lambda(T) \) is non-zero, take \( k \ge 1 \) least with \( N^k\v = \0 \), which exists by the definition of \( G_\lambda(T) \) and @thm-well-ordering. Then \( \w = N^{k-1}\v \ne \0 \) by minimality of \( k \) (for \( k = 1 \) this reads \( \w = \v \ne \0 \)), while \( N\w = N^k\v = \0 \). So \( \w \in \ker N \) is non-zero and \( \lambda \) is an eigenvalue.

(d) This is the computation just made: \( \w = N^{k-1}\v \) is non-zero and lies in \( \ker N = E_\lambda(T) \).
:::

Part (d) is a move worth remembering: **to get a genuine eigenvector out of a generalized one, apply \( T - \lambda\,\id_V \) as many times as possible without reaching \( \0 \).** It is the reason the enlargement never produces eigenvalues out of thin air, and it will start every Jordan chain in Section 2.

## The generalized eigenspace decomposition

We can now state the payoff. Chapter 8's primary decomposition (@thm-primary-decomposition) already splits \( V \) into invariant pieces, one for each irreducible factor of \( m_T \). When \( p_T \) splits, all those factors are linear, the pieces are kernels of powers of \( T - \lambda_i\,\id_V \) — and those are exactly the generalized eigenspaces. The extra information here is that the piece attached to \( \lambda_i \) has dimension \( a_T(\lambda_i) \), so the sizes are read off the characteristic polynomial.

*When the characteristic polynomial splits, the generalized eigenspaces fill the space, and the one for \( \lambda \) has dimension the algebraic multiplicity of \( \lambda \).*

::: {#thm-generalized-eigenspace-decomposition}
[Generalized Eigenspace Decomposition]

Let \( V \) be a finite-dimensional vector space over \( F \) with \( \dim V = n \ge 1 \), let \( T \in \cL(V) \), and suppose \( p_T \) **splits** over \( F \), with distinct eigenvalues \( \lambda_1, \dots, \lambda_k \) and
\[
p_T = (x - \lambda_1)^{a_1} \cdots (x - \lambda_k)^{a_k}, \qquad m_T = (x - \lambda_1)^{s_1} \cdots (x - \lambda_k)^{s_k},
\]
where \( a_i = a_T(\lambda_i) \) and \( 1 \le s_i \le a_i \). Write \( G_i = G_{\lambda_i}(T) \) and \( N_i = (T - \lambda_i\,\id_V)|_{G_i} \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( G_i = \ker(T - \lambda_i\,\id_V)^{s_i} \), and
   \[
   V = G_1 \oplus G_2 \oplus \dots \oplus G_k ;
   \]
2. each \( G_i \) is \( T \)-invariant and non-zero, with \( E_{\lambda_i}(T) \subseteq G_i \), and \( E_{\lambda_i}(T) = G_i \) if and only if \( s_i = 1 \);
3. \( \dim G_i = a_i \) and \( p_{T|_{G_i}} = (x - \lambda_i)^{a_i} \);
4. \( N_i^{a_i} = 0 \); that is, \( T|_{G_i} = \lambda_i\,\id_{G_i} + N_i \) with \( N_i \) nilpotent, of stabilization index \( s_i \);
5. if \( \sB \) is a basis of \( V \) obtained by writing bases of \( G_1, \dots, G_k \) one after another, then
   \[
   [T]_{\sB} = [T|_{G_1}]\ \oplus\ \dots\ \oplus\ [T|_{G_k}]
   \]
   is block diagonal, with the \( i \)-th block of size \( a_i \).
:::
:::

::: {.idea}
Almost everything is already proved; the one new step is (a), the identification \( G_i = \ker(T - \lambda_i\,\id_V)^{s_i} \). One inclusion is free, since \( \ker(T - \lambda_i)^{s_i} \) sits inside the union defining \( G_i \). For the other, count. Chapter 8 says the primary piece \( \ker(T - \lambda_i)^{s_i} \) has dimension \( a_i \), so it is enough to show \( \dim G_i \le a_i \). Now \( G_i \) is invariant, and the only eigenvalue of \( T \) on \( G_i \) is \( \lambda_i \): an eigenvector in \( G_i \) for \( \mu \) is killed by \( (\mu - \lambda_i)^n \), which forces \( \mu = \lambda_i \). So the characteristic polynomial of the restriction is a power of \( x - \lambda_i \) dividing \( p_T \), and its degree \( \dim G_i \) is at most \( a_i \).
:::

::: {.proof}
Since \( p_T \) splits and \( m_T \mid p_T \), @cor-minimal-divides-characteristic (b) gives the displayed factorization of \( m_T \) with \( 1 \le s_i \le a_i \). Put \( V_i = \ker(T - \lambda_i\,\id_V)^{s_i} \). The polynomials \( x - \lambda_i \) are distinct monic irreducibles, so @thm-primary-decomposition applies to \( m_T = \prod_i (x - \lambda_i)^{s_i} \) and gives
\[
V = V_1 \oplus \dots \oplus V_k ,
\]
with each \( V_i \) invariant and non-zero. By @cor-primary-components-dimension, \( \dim V_i = a_i \), \( p_{T|_{V_i}} = (x - \lambda_i)^{a_i} \), and \( E_{\lambda_i}(T) \subseteq V_i \) with equality if and only if \( s_i = 1 \).

*Claim: \( G_i = V_i \).* Fix \( i \) and write \( G = G_i \), \( \lambda = \lambda_i \), \( a = a_i \), \( N = T - \lambda\,\id_V \).

(⊇) \( V_i = \ker N^{s_i} \subseteq \bigcup_{j \ge 1}\ker N^j = G \).

(⊆) It suffices to prove \( \dim G \le a \): then \( V_i \subseteq G \) and \( \dim V_i = a \ge \dim G \) force \( \dim V_i = \dim G \), and @thm-dim-impl-eq, applied to the subspace \( V_i \) of \( G \), gives \( V_i = G \).

First, *the only eigenvalue of \( T|_G \) is \( \lambda \)*. Indeed, \( G \) is \( T \)-invariant (@cor-generalized-eigenspace-is-kernel (b)), so the restriction makes sense (@def-restriction-operator). Let \( \mu \in F \) be an eigenvalue of \( T|_G \), with eigenvector \( \v \in G \), \( \v \ne \0 \). From \( T\v = \mu\v \) we get \( N\v = (\mu - \lambda)\v \), hence \( N^n\v = (\mu - \lambda)^n\v \) by induction. But \( G = \ker N^n \) by @cor-generalized-eigenspace-is-kernel (a), so \( (\mu - \lambda)^n\v = \0 \) with \( \v \ne \0 \), which forces the scalar \( (\mu - \lambda)^n \) to be \( 0 \) (@thm-zero-product), and so \( \mu = \lambda \), since a field has no zero divisors (@thm-field-basic-properties).

Now compare characteristic polynomials. \( G \ne \{\0\} \), since \( \lambda \) is an eigenvalue of \( T \) (@cor-generalized-eigenspace-is-kernel (c)). If \( G = V \), then every root of \( p_T \) is an eigenvalue of \( T = T|_G \) (@thm-eigenvalue-characterizations), so \( \lambda \) is the only root; as \( p_T \) splits and is monic of degree \( n \) (@thm-charpoly-coefficients), \( p_T = (x - \lambda)^n \) and \( a = n = \dim G \). If \( G \ne V \), then @thm-invariant-subspace-matrix (b) applies to the invariant subspace \( G \) and gives
\[
p_T = p_{T|_G}\; p_{\bar T} ,
\]
so \( p_{T|_G} \) is a monic divisor of \( p_T = \prod_j (x - \lambda_j)^{a_j} \). By @lem-monic-divisors, \( p_{T|_G} = \prod_j (x - \lambda_j)^{c_j} \) with \( 0 \le c_j \le a_j \). Its roots are the eigenvalues of \( T|_G \) (@thm-eigenvalue-characterizations, applied to \( T|_G \)), which we just showed to be \( \lambda \) alone, so \( c_j = 0 \) for \( j \ne i \). Hence \( p_{T|_G} = (x - \lambda)^{c_i} \), and comparing degrees (@thm-charpoly-coefficients) gives \( \dim G = c_i \le a \). This proves the claim, and with it (a), (b) and (c), since \( G_i = V_i \).

(d) By @thm-primary-decomposition (c) and the claim, \( m_{T|_{G_i}} = (x - \lambda_i)^{s_i} \). For an integer \( j \ge 0 \), the operator \( N_i^{\,j} \) is \( (x - \lambda_i)^j \) evaluated at \( T|_{G_i} \), so \( N_i^{\,j} = 0 \) if and only if \( (x - \lambda_i)^{s_i} \) divides \( (x - \lambda_i)^{j} \) (@thm-minimal-polynomial-divides), that is, if and only if \( j \ge s_i \). Since \( s_i \le a_i \), this gives \( N_i^{\,a_i} = 0 \), and it identifies \( s_i \) as the least exponent killing \( N_i \). Hence \( \ker N_i^{\,s_i} = G_i \) while \( \ker N_i^{\,s_i - 1} \subsetneq G_i \), so the stabilization index of \( N_i \) is \( s_i \).

(e) Each \( G_i \) is invariant and non-zero, and \( V = \bigoplus_i G_i \), so @thm-direct-sum-invariant-block-diagonal gives the block diagonal shape, the \( i \)-th block being \( [T|_{G_i}] \) in the chosen basis of \( G_i \), of size \( \dim G_i = a_i \).
:::

Read (d) again, since it is the plan for the rest of the chapter. **On its generalized eigenspace, \( T \) is a scalar plus a nilpotent operator.** The scalar part is as simple as an operator can be. So the only question left is what a nilpotent operator looks like in a well-chosen basis, and that is the subject of the next section. Once it is answered, (e) assembles the answers for the different eigenvalues into one matrix for \( T \).

Two consistency checks. Summing dimensions in (a) and using (c) gives \( \sum_i a_i = n \), which is the degree count for a split \( p_T \). And if \( T \) is diagonalizable, then every \( s_i = 1 \) (@thm-diagonalizable-iff-minimal-distinct-linear), so (b) says \( G_i = E_{\lambda_i}(T) \) and (a) becomes the eigenspace decomposition \( V = \bigoplus_i E_{\lambda_i}(T) \) of @thm-diagonalization (c). Nothing is lost, and nothing new is gained, in the diagonalizable case.

::: {#exm-generalized-eigenspaces-4x4}
[Generalized Eigenspaces of a \( 4 \times 4 \) Matrix]

Let
\[
A = \begin{pmatrix} 2 & 1 & -1 & -2 \\ -3 & 3 & -1 & 1 \\ 3 & -1 & 3 & -1 \\ -3 & 1 & -1 & 3 \end{pmatrix} \in M_4(\nQ), \qquad p_A = (x - 2)^3(x - 5).
\]
Find \( E_2(A) \), \( G_2(A) \), \( G_5(A) \), the stabilization index of \( A - 2I \), and the minimal polynomial. Verify @thm-generalized-eigenspace-decomposition on this matrix.
:::

::: {.solution}
*The eigenspace.* Write \( N = A - 2I \), so
\[
N = \begin{pmatrix} 0 & 1 & -1 & -2 \\ -3 & 1 & -1 & 1 \\ 3 & -1 & 1 & -1 \\ -3 & 1 & -1 & 1 \end{pmatrix}.
\]
Rows \( 2 \) and \( 4 \) are equal and row \( 3 \) is their negative, so the row space is spanned by rows \( 1 \) and \( 2 \), which are not proportional; hence \( \rank N = 2 \) and \( \nullity N = 2 \) (@thm-rank-nullity-matrix). The kernel is cut out by
\[
x_2 - x_3 - 2x_4 = 0, \qquad -3x_1 + x_2 - x_3 + x_4 = 0 .
\]
Subtracting the first equation from the second gives \( -3x_1 + 3x_4 = 0 \), so \( x_1 = x_4 \), and then \( x_2 = x_3 + 2x_4 \). With \( x_3 = s \) and \( x_4 = t \) free,
\[
E_2(A) = \{ (t,\, s + 2t,\, s,\, t) \} = \Span\big((0, 1, 1, 0),\ (1, 2, 0, 1)\big), \qquad g_A(2) = 2 .
\]
Since \( a_A(2) = 3 > 2 \), the matrix is not diagonalizable (@thm-diagonalization (e)).

*The generalized eigenspace.* Squaring,
\[
N^2 = 9\begin{pmatrix} 0 & 0 & 0 & 0 \\ -1 & 0 & 0 & 1 \\ 1 & 0 & 0 & -1 \\ -1 & 0 & 0 & 1 \end{pmatrix},
\]
which has rank \( 1 \), so \( \ker N^2 \) has dimension \( 3 \) and is the hyperplane
\[
\ker N^2 = \{\, \x : x_1 = x_4 \,\}= \Span\big(\e_2,\ \e_3,\ \e_1 + \e_4\big).
\]
The chain of kernels has dimensions \( 0, 2, 3 \) so far. Since \( \ker N^2 \subseteq G_2(A) \) and \( \dim G_2(A) = a_A(2) = 3 = \dim \ker N^2 \) by part (c) of the theorem, we get \( G_2(A) = \ker N^2 \), and the stabilization index is \( s = 2 \). One can see the stabilization by hand as well: multiplying out gives \( N^3 = 3N^2 \), so \( \ker N^3 = \ker N^2 \) directly.

*The second generalized eigenspace.* Here \( a_A(5) = 1 \), so \( \dim G_5(A) = 1 \) and \( G_5(A) = E_5(A) \) by part (b) — its \( s \) must be \( 1 \). Solving \( (A - 5I)\x = \0 \) gives \( G_5(A) = E_5(A) = \Span\big((0, 1, -1, 1)\big) \). As a check, \( A(0, 1, -1, 1) = (1 + 1 - 2,\ 3 + 1 + 1,\ -1 - 3 - 1,\ 1 + 1 + 3) = (0, 5, -5, 5) \).

*The decomposition.* \( \nQ^4 = G_2(A) \oplus G_5(A) \), of dimensions \( 3 + 1 = 4 \), and the sum is direct because \( (0, 1, -1, 1) \notin G_2(A) \): its first and last coordinates are \( 0 \ne 1 \).

*The minimal polynomial.* The stabilization indices are \( s_1 = 2 \) at \( \lambda = 2 \) and \( s_2 = 1 \) at \( \lambda = 5 \), and part (d) of the theorem identifies these indices as the exponents in \( m_A \), so \( m_A = (x - 2)^2(x - 5) \). Consistently, \( (A - 2I)(A - 5I) \ne 0 \): the two factors are coprime, so the kernel of the product is \( \ker(A - 2I) \oplus \ker(A - 5I) \) (@thm-kernel-splitting (a)), of dimension \( 2 + 1 = 3 < 4 \).

*A basis adapted to the splitting.* Take \( \sB = \big(\e_2,\ \e_3,\ \e_1 + \e_4,\ (0, 1, -1, 1)\big) \), a basis of \( G_2 \) followed by one of \( G_5 \). By part (e), \( [T_A]_{\sB} \) is block diagonal with a \( 3 \times 3 \) block and the \( 1 \times 1 \) block \( (5) \).
:::

::: {.warning}
**The dimension of \( G_\lambda \) is the algebraic multiplicity, not the number of steps the chain takes.** In the example, \( \dim G_2 = 3 \) while the chain \( \{\0\} \subsetneq \ker N \subsetneq \ker N^2 = G_2 \) stabilizes after \( s = 2 \) steps. The two numbers measure different things: \( a(\lambda) = \dim G_\lambda \) is the total size of the piece, and \( s \) is the exponent of \( x - \lambda \) in the minimal polynomial. All that holds in general is \( 1 \le s \le a(\lambda) \) and \( g(\lambda) \le a(\lambda) \) (@thm-geometric-le-algebraic).
:::

Finally, a word on what we may not yet assume. The decomposition needs \( p_T \) to split, which is automatic over \( \nC \) (@cor-complex-polynomial-splits) but fails, for instance, for a rotation of \( \nR^2 \), whose generalized eigenspaces over \( \nR \) are all \( \{\0\} \) and certainly do not fill \( \nR^2 \). Operators over an arbitrary field need the coarser primary decomposition of Chapter 8, whose pieces we return to in Section 6.

## Exercises

### A. Check your understanding

:::: {#exr-generalized-eigenspaces-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define a generalized eigenvector and the generalized eigenspace \( G_\lambda(T) \).
2. State what @thm-kernel-chain-stabilizes says about the chain \( \ker N \subseteq \ker N^2 \subseteq \dots \), including the bound on where it stabilizes.
3. True or false: every generalized eigenvector of \( T \) for \( \lambda \) satisfies \( T\v = \lambda\v \). Justify your answer.
4. True or false: if \( \lambda \) is not an eigenvalue of \( T \), then \( G_\lambda(T) = \{\0\} \). Justify your answer.
5. Let \( \dim V = 6 \) and let \( p_T = (x - 1)^4(x - 3)^2 \) split over \( F \). What are \( \dim G_1(T) \) and \( \dim G_3(T) \)?
6. In the situation of (e), what can you say about \( \dim E_1(T) \)?
:::
::::

::: {.solution}
(a) A generalized eigenvector of \( T \) for \( \lambda \in F \) is a **non-zero** \( \v \in V \) with \( (T - \lambda\,\id_V)^k\v = \0 \) for **some** \( k \ge 1 \) (@def-generalized-eigenvector); \( G_\lambda(T) \) is the set of all of them together with \( \0 \), that is, \( \bigcup_{k \ge 1}\ker(T - \lambda\,\id_V)^k \) (@def-generalized-eigenspace).

(b) The kernels increase; once two consecutive ones are equal, all later ones equal them; the strict inclusions come first, and the chain has stabilized by step \( \dim V \), so \( G_\lambda(T) = \ker(T - \lambda\,\id_V)^{\dim V} \).

(c) False. For \( J = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} \), the vector \( \e_2 \) lies in \( G_2(J) \) but \( J\e_2 = \e_1 + 2\e_2 \ne 2\e_2 \). Only the vectors of \( E_\lambda(T) \subseteq G_\lambda(T) \) satisfy the eigenvector equation.

(d) True, by @cor-generalized-eigenspace-is-kernel (c).

(e) \( \dim G_1(T) = a_T(1) = 4 \) and \( \dim G_3(T) = a_T(3) = 2 \) (@thm-generalized-eigenspace-decomposition (c)).

(f) Only \( 1 \le \dim E_1(T) \le 4 \), since \( E_1(T) \subseteq G_1(T) \) and \( 1 \le g_T(1) \le a_T(1) \) (@thm-geometric-le-algebraic). All four values occur, as the Jordan forms of Section 3 will show.
:::

### B. Practice

:::: {#exr-generalized-eigenspaces-b1}
[B1: Computing generalized eigenspaces]

For each operator, find all generalized eigenspaces, and compare each with the corresponding eigenspace.

::: {.enumerate options="label=(\alph*)"}
1. \( A_1 = \begin{pmatrix} 3 & 1 \\ 0 & 3 \end{pmatrix} \in M_2(\nQ) \).
2. \( A_2 = \begin{pmatrix} 2 & 1 & 1 \\ 0 & 1 & -1 \\ -1 & -1 & 1 \end{pmatrix} \in M_3(\nR) \), which has \( m_{A_2} = (x - 1)^2(x - 2) \) (@exr-primary-decomposition-b2).
3. \( D \in \cL(\nR[x]_{\le 3}) \), differentiation.
4. The rotation \( R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \), first over \( \nR \) and then over \( \nC \).
:::
::::

::: {.solution}
(a) \( p_{A_1} = (x - 3)^2 \), so \( 3 \) is the only eigenvalue, and \( G_\lambda = \{\0\} \) for \( \lambda \ne 3 \) (@cor-generalized-eigenspace-is-kernel (c)). Since \( (A_1 - 3I)^2 = 0 \), \( G_3(A_1) = \nQ^2 \), while \( E_3(A_1) = \ker\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = \Span(\e_1) \) is a line.

(b) From \( m_{A_2} = (x - 1)^2(x - 2) \) and @thm-generalized-eigenspace-decomposition (a), \( G_1 = \ker(A_2 - I)^2 \) and \( G_2 = \ker(A_2 - 2I) \). Chapter 8 computed these: \( G_1 = \Span((-1, 1, 0), (0, 0, 1)) \), the plane \( x + y = 0 \), and \( G_2 = \Span((0, -1, 1)) \). The eigenspace \( E_1(A_2) = \Span((-1, 1, 0)) \) is a line strictly inside \( G_1 \), while \( E_2(A_2) = G_2 \) because \( s_2 = 1 \). All other \( G_\lambda \) are \( \{\0\} \).

(c) \( D^4 = 0 \) (@exm-differentiation-nilpotent), so \( G_0(D) = \nR[x]_{\le 3} \), of dimension \( 4 \), while \( E_0(D) = \ker D = \nR \) is the line of constants. Since \( p_D = x^4 \) has \( 0 \) as its only root, every other generalized eigenspace is \( \{\0\} \).

(d) Over \( \nR \), \( p_R = x^2 + 1 \) has no root, so \( R \) has no eigenvalue and \( G_\lambda(R) = \{\0\} \) for every \( \lambda \in \nR \). The generalized eigenspaces do **not** fill \( \nR^2 \); the hypothesis that \( p_R \) splits fails. Over \( \nC \), \( p_R = (x - i)(x + i) \) splits with \( a(i) = a(-i) = 1 \), so \( G_i(R) = E_i(R) = \Span((1, -i)) \) and \( G_{-i}(R) = E_{-i}(R) = \Span((1, i)) \), and \( \nC^2 = G_i \oplus G_{-i} \). (Check: \( R(1, -i) = (i, 1) = i(1, -i) \).)
:::

:::: {#exr-generalized-eigenspaces-b2}
[B2: The image chain stabilizes too]

Let \( V \) be finite-dimensional with \( \dim V = n \), and let \( N \in \cL(V) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \im N \supseteq \im N^2 \supseteq \im N^3 \supseteq \dots \), and that each \( \im N^k \) is \( N \)-invariant.
2. Prove that \( \im N^{m} = \im N^{m+1} \) if and only if \( \ker N^{m} = \ker N^{m+1} \).
3. Deduce that \( \im N^n = \im N^{n+j} \) for every \( j \ge 0 \), and that the image chain stabilizes at exactly the same index \( s \) as the kernel chain.
:::
::::

::: {.solution}
(a) \( \im N^{k+1} = \{ N^{k+1}\v : \v \in V \} = \{ N^k(N\v) : \v \in V \} \subseteq \im N^k \). Each \( \im N^k \) is the image of a polynomial in \( N \), hence \( N \)-invariant (@thm-kernel-image-of-polynomial-invariant (b)).

(b) By @thm-rank-nullity, \( \dim\im N^{k} + \dim\ker N^{k} = n \) for every \( k \). The inclusions \( \im N^{m+1} \subseteq \im N^m \) and \( \ker N^m \subseteq \ker N^{m+1} \) are equalities exactly when the dimensions agree (@thm-dim-impl-eq), and \( \dim\im N^m = \dim\im N^{m+1} \) if and only if \( \dim\ker N^m = \dim\ker N^{m+1} \) by the displayed identity.

(c) By @thm-kernel-chain-stabilizes (d), \( \ker N^n = \ker N^{n+j} \); iterating (b) at each step from \( n \) to \( n + j \) gives \( \im N^n = \im N^{n+j} \). And by (b), the least index at which two consecutive images agree is the least index at which two consecutive kernels agree, namely \( s \).
:::

:::: {#exr-generalized-eigenspaces-b3}
[B3: Reading the dimensions off a triangular matrix]

Let
\[
A = \begin{pmatrix} 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 2 & 1 \\ 0 & 0 & 0 & 2 \end{pmatrix} \in M_4(\nQ).
\]

::: {.enumerate options="label=(\alph*)"}
1. Write down \( p_A \) and the algebraic multiplicities.
2. Compute \( E_1(A) \), \( G_1(A) \), \( E_2(A) \) and \( G_2(A) \), and check \( \dim G_\lambda = a_A(\lambda) \).
3. Verify that \( \nQ^4 = G_1(A) \oplus G_2(A) \), and find \( m_A \).
:::
::::

::: {.solution}
(a) \( A \) is upper triangular, so \( p_A = (x - 1)^2(x - 2)^2 \) (@thm-det-triangular), and \( a_A(1) = a_A(2) = 2 \).

(b) \( A - I = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 1 \end{pmatrix} \) has rank \( 3 \) (rows \( 1, 2, 4 \) are independent and row \( 3 \) is the sum of rows \( 2 \) and \( 4 \)), so \( E_1(A) = \Span(\e_1) \). Squaring,
\[
(A - I)^2 = \begin{pmatrix} 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 1 \end{pmatrix},
\]
of rank \( 2 \), with kernel \( \Span(\e_1, \e_2) \); so \( G_1(A) = \Span(\e_1, \e_2) \), of dimension \( 2 = a_A(1) \). (Membership can be seen directly: \( (A - I)\e_2 = \e_1 \) and \( (A - I)\e_1 = \0 \).)

Similarly \( A - 2I = \begin{pmatrix} -1 & 1 & 0 & 0 \\ 0 & -1 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix} \) has rank \( 3 \), so \( E_2(A) \) is a line; solving gives \( E_2(A) = \Span((1, 1, 1, 0)) \). And \( (A - 2I)^2 = \begin{pmatrix} 1 & -2 & 1 & 0 \\ 0 & 1 & -1 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} \) has rank \( 2 \); its kernel is cut out by \( x_1 - 2x_2 + x_3 = 0 \) and \( x_2 - x_3 + x_4 = 0 \), so \( G_2(A) = \Span((1, 1, 1, 0), (-2, -1, 0, 1)) \), of dimension \( 2 = a_A(2) \). (Check: \( (A - 2I)(-2, -1, 0, 1) = (1, 1, 1, 0) \), the eigenvector.)

(c) The four vectors \( \e_1, \e_2, (1,1,1,0), (-2,-1,0,1) \) form a basis of \( \nQ^4 \): the matrix with these columns is upper triangular with diagonal \( 1, 1, 1, 1 \), hence invertible. So the sum is direct and equals \( \nQ^4 \), as @thm-generalized-eigenspace-decomposition (a) predicts. Both stabilization indices are \( 2 \) (the eigenspaces are lines, the generalized eigenspaces planes), so \( m_A = (x - 1)^2(x - 2)^2 = p_A \).
:::

### C. Going deeper

:::: {#exr-generalized-eigenspaces-c1}
[C1: The Fitting decomposition]

Let \( V \) be finite-dimensional with \( \dim V = n \), and let \( N \in \cL(V) \) be **any** operator. Put \( U = \ker N^n \) and \( W = \im N^n \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( U \cap W = \{\0\} \), and deduce \( V = U \oplus W \).
2. Prove that \( U \) and \( W \) are \( N \)-invariant, that \( N|_U \) is nilpotent, and that \( N|_W \) is invertible.
3. Identify \( U \) as a generalized eigenspace of \( N \).
4. Compute \( U \) and \( W \) for \( N = \begin{pmatrix} 0 & 1 \\ 0 & 1 \end{pmatrix} \in M_2(\nQ) \).
:::

*Hint: for (a), if \( \v = N^n\w \) and \( N^n\v = \0 \), look at which kernel \( \w \) lies in.*
::::

::: {.solution}
(a) Let \( \v \in U \cap W \), say \( \v = N^n\w \) with \( N^n\v = \0 \). Then \( N^{2n}\w = N^n\v = \0 \), so \( \w \in \ker N^{2n} = \ker N^n \) by @thm-kernel-chain-stabilizes (d), and therefore \( \v = N^n\w = \0 \). By @thm-rank-nullity, \( \dim U + \dim W = n \), so \( \dim(U + W) = \dim U + \dim W - \dim(U \cap W) = n \) (@thm-dimension-formula-subspace-dim), whence \( U + W = V \) (@thm-dim-impl-eq) and the sum is direct (@thm-direct-sum-criteria).

(b) Both are invariant by @thm-kernel-image-of-polynomial-invariant (b). On \( U \) we have \( (N|_U)^n = 0 \) by definition of \( U \), so \( N|_U \) is nilpotent. On \( W \), the map \( N|_W \colon W \to W \) is surjective: \( N(W) = N(\im N^n) = \im N^{n+1} = \im N^n = W \) by @exr-generalized-eigenspaces-b2 (c). A surjective operator on a finite-dimensional space is invertible (@cor-rank-nullity-consequences (e)).

(c) \( U = \ker N^n = G_0(N) \), by @cor-generalized-eigenspace-is-kernel (a) with \( \lambda = 0 \). So the Fitting decomposition splits \( V \) into the generalized eigenspace for \( 0 \) and a part on which \( N \) is invertible.

(d) Here \( n = 2 \) and \( N^2 = \begin{pmatrix} 0 & 1 \\ 0 & 1 \end{pmatrix} = N \), so \( U = \ker N = \Span(\e_1) \) and \( W = \im N = \Span((1, 1)) \). Indeed \( \nQ^2 = \Span(\e_1) \oplus \Span((1,1)) \), \( N \) is zero on \( U \), and \( N(1, 1) = (1, 1) \), so \( N|_W \) is the identity.
:::

:::: {#exr-generalized-eigenspaces-c2}
[C2: Commuting operators preserve generalized eigenspaces]

Let \( V \) be finite-dimensional, and let \( S, T \in \cL(V) \) with \( ST = TS \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( S\big(G_\lambda(T)\big) \subseteq G_\lambda(T) \) for every \( \lambda \in F \).
2. Deduce that if \( p_T \) splits, then every generalized eigenspace of \( T \) is invariant under every polynomial in \( T \) and under \( S \), and that \( V \) has a basis in which both \( S \) and \( T \) have block diagonal matrices with blocks of sizes \( a_T(\lambda_1), \dots, a_T(\lambda_k) \).
3. Show by example that part (a) can be vacuous: find commuting \( S, T \) on \( \nQ^2 \) and a \( \lambda \) with \( E_\lambda(T) \) a line, \( G_\lambda(T) = \nQ^2 \), and \( S \) not a scalar multiple of the identity.
:::
::::

::: {.solution}
(a) Since \( ST = TS \), \( S \) commutes with every polynomial in \( T \) (@thm-evaluation-homomorphism (d)), in particular with \( N^k \), where \( N = T - \lambda\,\id_V \). Let \( \v \in G_\lambda(T) \), say \( N^k\v = \0 \). Then
\[
N^k(S\v) = S(N^k\v) = S\0 = \0 ,
\]
so \( S\v \in \ker N^k \subseteq G_\lambda(T) \). (This is @thm-kernel-image-of-polynomial-invariant (a) with \( R = N^k \).)

(b) Invariance under polynomials in \( T \) is @thm-kernel-image-of-polynomial-invariant (b), and invariance under \( S \) is (a). If \( p_T \) splits, then \( V = \bigoplus_i G_{\lambda_i}(T) \) with \( \dim G_{\lambda_i}(T) = a_T(\lambda_i) \) (@thm-generalized-eigenspace-decomposition), and a basis assembled from bases of the summands makes both matrices block diagonal, by @thm-direct-sum-invariant-block-diagonal applied to \( T \) and to \( S \).

(c) Take \( T = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} \) and \( S = T \). They commute, \( E_2(T) = \Span(\e_1) \) is a line, \( G_2(T) = \nQ^2 \), and \( S \) is not a scalar matrix. Consistently with @thm-commuting-preserves-eigenspaces, \( S \) maps the line \( \Span(\e_1) \) into itself, and by (a) it maps \( G_2(T) = \nQ^2 \) into itself, which says nothing. The lesson is that (a) is informative only when \( G_\lambda(T) \ne V \).
:::
