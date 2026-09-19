# Nilpotent Operators

Section 1 reduced our problem to one piece at a time: on the generalized eigenspace \( G_\lambda(T) \), the operator is \( \lambda\,\id + N \) with some power of \( N \) equal to zero (@thm-generalized-eigenspace-decomposition (d)). The scalar part needs no work, so everything now depends on a single question: what does an operator all of whose powers eventually vanish look like in the right basis? This section answers it completely, and the answer is a list of numbers — the sizes of the staircases the operator builds.

## Operators killed by a power

The objects have already appeared several times. Differentiation on \( F[x]_{\le n} \) satisfies \( D^{n+1} = 0 \) (@exm-differentiation-nilpotent). The matrix \( \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) has square \( 0 \). Over a field of characteristic \( 0 \), a commutator \( [\A, \B] \) that commutes with \( \A \) has some power equal to \( 0 \) (@exr-commutators-and-shoda-c2). Chapter 3 gave these operators their name in passing; here is the definition in full, with the one extra piece of data we shall need.

*A nilpotent operator is one that some power annihilates: repeated application destroys every vector.*

::: {#def-nilpotent}
[Nilpotent Operator, Index of Nilpotency]

Let \( V \) be a vector space over \( F \) and \( N \in \cL(V) \). We say \( N \) is **nilpotent** if
\[
N^{s} = 0 \qquad \text{for some integer } s \ge 1 .
\]
If \( V \ne \{\0\} \) and \( N \) is nilpotent, the **index of nilpotency** of \( N \) is the **least** such \( s \); equivalently, \( N^{s} = 0 \) and \( N^{s-1} \ne 0 \). A matrix \( \A \in M_n(F) \) is **nilpotent** if \( \A^{s} = 0 \) for some \( s \ge 1 \), that is, if \( T_{\A} \) is nilpotent.
:::

In words: one **single** exponent must kill **every** vector at once, and the exponent is at least \( 1 \), so the zero operator is nilpotent (index \( 1 \)) but the identity on \( V \ne \{\0\} \) is not. The index is well defined: the exponents \( s \ge 1 \) with \( N^s = 0 \) form a non-empty set of positive integers, which has a least element (@thm-well-ordering).

**Examples.**

- **The shift.** On \( F^k \), let \( N\e_1 = \0 \) and \( N\e_j = \e_{j-1} \) for \( j \ge 2 \). Then \( N^{k} \) kills every \( \e_j \), while \( N^{k-1}\e_k = \e_1 \ne \0 \), so \( N \) is nilpotent of index \( k \). Its matrix in the standard basis has a \( 1 \) in each position \( (j-1, j) \) and zeros elsewhere. This matrix is the model for everything in this section, and we write it
  \[
  \J_k(0) \coloneqq \begin{pmatrix} 0 & 1 & & \\ & 0 & \ddots & \\ & & \ddots & 1 \\ & & & 0 \end{pmatrix} \in M_k(F),
  \]
  with \( 1 \) in every **superdiagonal** entry \( (j, j+1) \) and \( 0 \) everywhere else. (Section 3 writes \( \J_k(\lambda) = \lambda \I_k + \J_k(0) \) and calls it a Jordan block.) For \( k = 1 \), \( \J_1(0) = (0) \).
- **Differentiation.** \( D \) on \( F[x]_{\le n} \) has \( D^{n+1} = 0 \), and over \( \nR \) the index is exactly \( n + 1 \), since \( D^n x^n = n! \ne 0 \) (@exm-differentiation-nilpotent). Over \( \nR \), in the basis \( (1, x, x^2/2!, \dots, x^n/n!) \), its matrix is exactly \( \J_{n+1}(0) \), because \( D(x^j/j!) = x^{j-1}/(j-1)! \).
- **All entries non-zero.** \( \A = \begin{pmatrix} 2 & 4 \\ -1 & -2 \end{pmatrix} \) has \( \A^2 = \begin{pmatrix} 4 - 4 & 8 - 8 \\ -2 + 2 & -4 + 4 \end{pmatrix} = 0 \), so \( \A \) is nilpotent of index \( 2 \), although no entry of \( \A \) is \( 0 \). Nilpotency is not visible from the shape of the entries.
- **The degenerate case.** On a space of dimension \( 1 \) the only nilpotent operator is \( 0 \): if \( N = c\,\id \) and \( N^s = 0 \), then \( c^s = 0 \), so \( c = 0 \). Small as it is, this is why a \( 1 \times 1 \) block in a nilpotent normal form carries a \( 0 \) and nothing else.

**Non-example by minimal change.** Move the \( 1 \) in \( \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) to the other off-diagonal position and take \( \S = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \), the swap of the two coordinates. It is just as sparse, but \( \S^2 = \I \), so \( \S^{2k} = \I \ne 0 \) and \( \S^{2k+1} = \S \ne 0 \) for every \( k \): **no** power vanishes, and the defining clause fails outright. A gentler non-example is \( \diag(0, 1) \), which is singular and has \( 0 \) as an eigenvalue, yet \( \diag(0,1)^k = \diag(0, 1) \ne 0 \); being non-invertible is far from being nilpotent.

**Why this definition.** The clause "for some \( s \)" cannot be replaced by a fixed exponent without losing the class, since on \( \nR[x]_{\le n} \) differentiation needs \( n + 1 \) steps. On the other hand the exponent may always be taken to be \( \dim V \), as the next proposition shows, so the definition is not as open-ended as it looks. The name says "zero power": *nil* (nothing) and *potens* (power).

::: {.warning}
**Nilpotent is a statement about one exponent killing everything, not about each vector separately, and not about the entries.** Differentiation on \( \nR[x] \) (**all** polynomials) kills every **single** polynomial after enough steps, yet no power of it is \( 0 \), because the number of steps needed is unbounded; the space is infinite-dimensional. And the matrix \( \begin{pmatrix} 2 & 4 \\ -1 & -2 \end{pmatrix} \) is nilpotent with no zero entry, while \( \diag(0, 1) \) has a zero entry, a zero eigenvalue, and is not nilpotent.
:::

The first payoff collects the facts we shall use constantly. Note the interplay with Section 1: a nilpotent operator is one whose generalized eigenspace for \( 0 \) is everything.

::: {#prp-nilpotent-basic}
[Basic Properties of Nilpotent Operators]

Let \( V \) be a finite-dimensional vector space over \( F \) with \( \dim V = n \ge 1 \), and let \( N \in \cL(V) \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( N \) is nilpotent if and only if \( N^{n} = 0 \), if and only if \( G_0(N) = V \);
2. if \( N \) is nilpotent with index \( s \), then \( s \le n \), \( m_N = x^{s} \) and \( p_N = x^{n} \);
3. if \( N \) is nilpotent, then \( \spec(N) = \{0\} \), and there is a basis in which the matrix of \( N \) is upper triangular with zero diagonal;
4. conversely, if \( p_N = x^n \), then \( N \) is nilpotent.
:::
:::

::: {.idea}
For (a) and (b), the kernel chain of Section 1 does the work: \( N^s = 0 \) says \( \ker N^s = V \), and the chain has stopped growing by step \( n \). For the triangular matrix in (c), build the basis along the chain: take a basis of \( \ker N \), extend it to one of \( \ker N^2 \), and so on. A vector first appearing at level \( k \) is sent by \( N \) into \( \ker N^{k-1} \), which is spanned by vectors listed **earlier**, so every column has zeros from the diagonal down.
:::

::: {.proof}
(a) If \( N^s = 0 \) for some \( s \ge 1 \), then \( \ker N^s = V \), so \( V = \ker N^{\max(s,n)} = \ker N^n \) by @thm-kernel-chain-stabilizes (a) and (d), that is, \( N^n = 0 \). The converse is the definition with \( s = n \). And \( G_0(N) = \ker N^n \) by @cor-generalized-eigenspace-is-kernel (a) with \( \lambda = 0 \), so \( G_0(N) = V \) if and only if \( N^n = 0 \).

(c) Let \( s \) be the index and put \( K_k = \ker N^k \), so \( \{\0\} = K_0 \subseteq K_1 \subseteq \dots \subseteq K_s = V \) by (a) and @thm-kernel-chain-stabilizes (a). Choose a basis \( \sB_1 \) of \( K_1 \); extend it to a basis \( \sB_2 \) of \( K_2 \); and continuing, extend \( \sB_{k-1} \) to a basis \( \sB_k \) of \( K_k \) for \( k = 2, \dots, s \) (@thm-basis-extension, legitimate because \( \sB_{k-1} \) is an independent list in \( K_k \)). Then \( \sB = \sB_s = (\v_1, \dots, \v_n) \) is a basis of \( V \), and for each \( k \) the first \( \dim K_k \) of its vectors form a basis of \( K_k \). Let \( 1 \le j \le n \) and let \( k \) be the level at which \( \v_j \) was added, so \( \v_j \in K_k \) and \( \dim K_{k-1} < j \). Then \( N\v_j \in K_{k-1} = \Span(\v_1, \dots, \v_{\dim K_{k-1}}) \subseteq \Span(\v_1, \dots, \v_{j-1}) \). So the \( j \)-th column of \( [N]_{\sB} \) has zeros in rows \( j, j+1, \dots, n \) (@def-matrix-of-linear-map, @thm-unique-representation): the matrix is upper triangular with zero diagonal. Its diagonal entries are, with multiplicity, the eigenvalues of \( N \) (@thm-diagonal-of-triangular-form (b)), and they are all \( 0 \), so \( \spec(N) = \{0\} \).

(b) By (a), \( N^n = 0 \), so \( s \le n \). The polynomial \( x^s \) annihilates \( N \), and \( x^{s-1} \) does not, so \( m_N \mid x^s \) and \( m_N \nmid x^{s-1} \) (@thm-minimal-polynomial-divides). Every monic divisor of \( x^s \) is \( x^j \) with \( 0 \le j \le s \) (@lem-monic-divisors), so \( m_N = x^{s} \). For \( p_N \), use the basis \( \sB \) of (c): there \( x\I_n - [N]_{\sB} \) is upper triangular with every diagonal entry equal to \( x \), so \( p_N = x^n \) by @thm-det-triangular and @def-charpoly-operator.

(d) If \( p_N = x^n \), then \( p_N(N) = N^n = 0 \) by @thm-cayley-hamilton.
:::

So nilpotency is detected by the characteristic polynomial: \( N \) is nilpotent exactly when \( p_N = x^n \), which over \( \nC \) is exactly \( \spec(N) = \{0\} \), as Chapter 8 found by a different route (@thm-nilpotent-trace-powers). Part (c) also follows abstractly from @thm-triangularization, since \( x^n \) splits over every field; the proof above builds the basis explicitly. But a strictly upper triangular matrix still has \( n(n-1)/2 \) entries to describe, and almost all of them can be cleared away. That is the content of the structure theorem.

## What one chain looks like

Look again at \( \J_k(0) \) and read its columns, which is where a matrix always tells us what the operator does to basis vectors. With \( \sB = (\b_1, \dots, \b_k) \) the standard basis of \( F^k \), the matrix \( \J_k(0) \) says
\[
N\b_1 = \0, \qquad N\b_2 = \b_1, \qquad N\b_3 = \b_2, \quad \dots, \quad N\b_k = \b_{k-1} .
\]
Reading this from the right, the last basis vector \( \b_k \) generates all the others: \( \b_{k-1} = N\b_k \), \( \b_{k-2} = N^2\b_k \), and so on down to \( \b_1 = N^{k-1}\b_k \), which is an eigenvector, killed at the next step. So one Jordan block is one vector together with its successive images, a staircase descending to \( \0 \). Such a list deserves a name.

::: {#def-jordan-chain}
[Jordan Chain]

Let \( V \) be a vector space over \( F \), let \( N \in \cL(V) \) and let \( \u \in V \) with \( \u \ne \0 \). Suppose \( N^{k}\u = \0 \) and \( N^{k-1}\u \ne \0 \) for an integer \( k \ge 1 \). The **Jordan chain generated by \( \u \)** is the ordered list
\[
\big(N^{k-1}\u,\ N^{k-2}\u,\ \dots,\ N\u,\ \u\big),
\]
of **length** \( k \), and \( \u \) is called the **top** of the chain. For \( T \in \cL(V) \) and \( \lambda \in F \), a Jordan chain of \( T \) for \( \lambda \) means a Jordan chain of \( N = T - \lambda\,\id_V \).
:::

The order matters, and we always write it with the **eigenvector first** and the top last, so that \( N \) moves each entry to the one before it and kills the first. The first entry \( N^{k-1}\u \) is indeed an eigenvector for \( 0 \), by the argument of @cor-generalized-eigenspace-is-kernel (d). For example, the chain generated by \( \e_2 \) under \( \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) is \( (\e_1, \e_2) \), of length \( 2 \).

A chain is automatically independent, which is the first sign that chains are good building blocks.

::: {#lem-jordan-chain-independent}
[A Jordan Chain Is Independent]

Let \( N \in \cL(V) \) and let \( (N^{k-1}\u, \dots, N\u, \u) \) be a Jordan chain, so \( N^k\u = \0 \ne N^{k-1}\u \). Then:

::: {.enumerate options="label=(\alph*)"}
1. the list is linearly independent, so \( k \le \dim V \) when \( V \) is finite-dimensional;
2. \( C = \Span(\u, N\u, \dots, N^{k-1}\u) \) is \( N \)-invariant of dimension \( k \), and the matrix of \( N|_{C} \) in the chain, taken in the order of @def-jordan-chain, is \( \J_k(0) \).
:::
:::

::: {.proof}
(a) Suppose \( a_0\u + a_1N\u + \dots + a_{k-1}N^{k-1}\u = \0 \) with \( a_j \in F \). Apply \( N^{k-1} \). Every term with \( j \ge 1 \) becomes \( a_jN^{k-1+j}\u = \0 \), since \( N^k\u = \0 \) and \( k - 1 + j \ge k \). What remains is \( a_0N^{k-1}\u = \0 \), and \( N^{k-1}\u \ne \0 \), so \( a_0 = 0 \) (@thm-zero-product). Now apply \( N^{k-2} \) to the relation with \( a_0 = 0 \): by the same cancellation only \( a_1N^{k-1}\u = \0 \) survives, so \( a_1 = 0 \). Repeating this for \( N^{k-3}, \dots, N^0 \) gives \( a_2 = \dots = a_{k-1} = 0 \). Hence the list is independent, and an independent list has at most \( \dim V \) entries (@thm-basis-extension).

(b) By (a) the \( k \) spanning vectors are independent, so \( \dim C = k \). Write \( \b_j = N^{k-j}\u \) for \( j = 1, \dots, k \), the chain in order. Then \( N\b_1 = N^{k}\u = \0 \) and \( N\b_j = N^{k-j+1}\u = \b_{j-1} \) for \( j \ge 2 \), so all images lie in \( C \) and \( C \) is \( N \)-invariant (@lem-invariance-on-spanning-list). The \( j \)-th column of the matrix of \( N|_C \) is the coordinate vector of \( N\b_j \), which is \( \0 \) for \( j = 1 \) and \( \e_{j-1} \) for \( j \ge 2 \) (@def-matrix-of-linear-map). That is precisely \( \J_k(0) \).
:::

## The structure theorem

Now the goal. If a nilpotent operator could be split into chains, its matrix would be a direct sum of blocks \( \J_{k_i}(0) \), and nothing would be left to describe except the list of lengths. That is exactly what happens.

*Every nilpotent operator is a disjoint union of staircases: the space breaks into chains, and the operator shifts each chain one step down.*

::: {#thm-nilpotent-structure}
[Structure Theorem for Nilpotent Operators]

Let \( V \) be a finite-dimensional vector space over \( F \) with \( \dim V = n \ge 1 \), and let \( N \in \cL(V) \) be nilpotent. Then there are an integer \( r \ge 1 \), vectors \( \u_1, \dots, \u_r \in V \) and integers
\[
k_1 \ge k_2 \ge \dots \ge k_r \ge 1, \qquad k_1 + k_2 + \dots + k_r = n,
\]
such that:

::: {.enumerate options="label=(\alph*)"}
1. \( N^{k_i}\u_i = \0 \) for each \( i \), and the list \( \sB \) obtained by writing the \( r \) Jordan chains one after another,
   \[
   \sB = \big(\underbrace{N^{k_1-1}\u_1, \dots, N\u_1, \u_1}_{\text{chain } 1},\ \dots,\ \underbrace{N^{k_r-1}\u_r, \dots, N\u_r, \u_r}_{\text{chain } r}\big),
   \]
   is a basis of \( V \);
2. with \( C_i = \Span(\u_i, N\u_i, \dots, N^{k_i-1}\u_i) \), each \( C_i \) is \( N \)-invariant, \( V = C_1 \oplus \dots \oplus C_r \), and
   \[
   [N]_{\sB} = \J_{k_1}(0) \oplus \J_{k_2}(0) \oplus \dots \oplus \J_{k_r}(0) .
   \]
:::
:::

A basis as in (a) is called a **Jordan basis** for \( N \). Before the proof, here is the picture the proof builds. Each chain is a row of boxes, the top of the chain on the right, and \( N \) moves one box to the left, off the diagram at the left edge. For lengths \( (3, 1) \):

\begin{center}
\begin{tikzpicture}[scale=1, bx/.style={draw, minimum width=1.7cm, minimum height=0.9cm, font=\small}]
  \node[bx] (a1) at (0,0) {$N^{2}\mathbf{u}_1$};
  \node[bx] (a2) at (2.7,0) {$N\mathbf{u}_1$};
  \node[bx] (a3) at (5.4,0) {$\mathbf{u}_1$};
  \node[bx] (b1) at (0,-1.6) {$\mathbf{u}_2$};
  \node (z1) at (-2.1,0) {$\mathbf{0}$};
  \node (z2) at (-2.1,-1.6) {$\mathbf{0}$};
  \draw[->, thick] (a3) -- node[above, font=\small] {$N$} (a2);
  \draw[->, thick] (a2) -- node[above, font=\small] {$N$} (a1);
  \draw[->, thick] (a1) -- node[above, font=\small] {$N$} (z1);
  \draw[->, thick] (b1) -- node[above, font=\small] {$N$} (z2);
  \node[font=\small, align=left] at (2.3,-2.7) {the boxes in the left column, $N^{2}\mathbf{u}_1$ and $\mathbf{u}_2$, form a basis of $\ker N$};
\end{tikzpicture}
\end{center}

::: {.idea}
Induction on \( \dim V \), with the smaller object found inside: \( W = \im N \). It is \( N \)-invariant, \( N|_W \) is nilpotent, and \( \dim W < \dim V \) because a nilpotent operator on a non-zero space is not injective. So \( W \) already has chains. Each chain of \( W \) is one box short of what we want: its top \( \w_i \) lies in \( \im N \), so \( \w_i = N\u_i \) for some \( \u_i \in V \), and we can extend the chain by one box on the right, gaining \( \u_i \). What is still missing is counted by \( \ker N \): the ends \( N^{l_i}\u_i \) of the extended chains are independent vectors of \( \ker N \), and any basis extension of them inside \( \ker N \) supplies the chains of length \( 1 \). Then the count comes out exactly right, by Rank–Nullity (@thm-rank-nullity), and independence follows by applying \( N \) once and using the basis of \( W \).
:::

::: {.proof}
We argue by induction on \( n = \dim V \ge 1 \), the statement being: for every nilpotent \( N \) on a space of dimension \( n \), chains as in (a) exist.

*Base case \( n = 1 \).* Here \( N = 0 \), as noted after @def-nilpotent. Take \( r = 1 \), \( k_1 = 1 \) and \( \u_1 \) any non-zero vector; then \( N^{1}\u_1 = \0 \) and \( \sB = (\u_1) \) is a basis.

*Induction step.* Let \( n \ge 2 \) and assume the statement for all spaces of dimension less than \( n \). Let \( N \in \cL(V) \) be nilpotent with \( \dim V = n \).

\( N \) is not injective: if it were, then \( N^s \) would be injective for every \( s \) (a composition of injective maps is injective, @thm-composition-preserves (a)), contradicting \( N^s = 0 \) on \( V \ne \{\0\} \). So \( \nullity N \ge 1 \), and with \( W = \im N \) Rank–Nullity gives \( \dim W = n - \nullity N \le n - 1 \) (@thm-rank-nullity).

**Step 1. Chains inside \( \im N \).** If \( W = \{\0\} \), then \( N = 0 \); take \( r = n \), all \( k_i = 1 \) and \( (\u_1, \dots, \u_n) \) any basis of \( V \), and (a) holds. So assume \( W \ne \{\0\} \). Then \( W \) is \( N \)-invariant (@thm-kernel-image-of-polynomial-invariant (b)), \( N|_W \) is nilpotent (\( (N|_W)^s = (N^s)|_W = 0 \)), and \( 1 \le \dim W < n \). By the induction hypothesis there are \( \w_1, \dots, \w_q \in W \) and \( l_1 \ge \dots \ge l_q \ge 1 \) with \( \sum_i l_i = \dim W \), \( (N|_W)^{l_i}\w_i = \0 \), and
\[
\sC = \big(N^{l_1-1}\w_1, \dots, \w_1,\ \dots,\ N^{l_q-1}\w_q, \dots, \w_q\big)
\]
a basis of \( W \).

**Step 2. Lift each chain by one box.** Each \( \w_i \) lies in \( W = \im N \), so we may choose \( \u_i \in V \) with \( N\u_i = \w_i \) for \( i = 1, \dots, q \). Put \( k_i = l_i + 1 \). Then
\[
N^{j}\u_i = N^{j-1}\w_i \quad (j \ge 1), \qquad \text{so} \qquad N^{k_i}\u_i = N^{l_i}\w_i = \0 .
\]

**Step 3. Fill up \( \ker N \).** The \( q \) vectors \( N^{l_i}\u_i = N^{l_i - 1}\w_i \) (\( i = 1, \dots, q \)) are members of the basis \( \sC \), hence linearly independent, and each lies in \( \ker N \), because \( N(N^{l_i}\u_i) = N^{k_i}\u_i = \0 \). By @thm-basis-extension applied inside \( \ker N \), there are vectors \( \u_{q+1}, \dots, \u_r \in \ker N \) such that
\[
\big(N^{l_1}\u_1, \dots, N^{l_q}\u_q,\ \u_{q+1}, \dots, \u_r\big)
\]
is a basis of \( \ker N \); in particular \( r = \nullity N \). Put \( k_i = 1 \) for \( q < i \le r \), so that \( N^{k_i}\u_i = N\u_i = \0 \) for those \( i \) as well.

**Step 4. The combined list is a basis.** Let \( \sB \) be the list of all \( N^{j}\u_i \) with \( 1 \le i \le r \) and \( 0 \le j \le k_i - 1 \), the chains written one after another as in (a). Its length is
\[
\sum_{i=1}^{q}(l_i + 1) + (r - q) = \dim W + q + (r - q) = \rank N + \nullity N = n
\]
by Step 1 and @thm-rank-nullity. So by @thm-right-size-basis (a) it is enough to prove independence.

Suppose
\[
\sum_{i=1}^{r}\ \sum_{j=0}^{k_i-1} a_{ij}\,N^{j}\u_i = \0 \tag{$\ast$}
\]
with \( a_{ij} \in F \). Apply \( N \) to \( (\ast) \). For \( i > q \) we have \( k_i = 1 \) and \( N\u_i = \0 \), so those terms die. For \( i \le q \) and \( j = k_i - 1 = l_i \) we get \( N^{l_i + 1}\u_i = \0 \) by Step 2, so those terms die too. The rest is, using \( N^{j+1}\u_i = N^{j}\w_i \),
\[
\sum_{i=1}^{q}\ \sum_{j=0}^{l_i-1} a_{ij}\,N^{j}\w_i = \0 .
\]
This is a linear combination of the members of the basis \( \sC \) of \( W \), so
\[
a_{ij} = 0 \qquad \text{for } 1 \le i \le q,\ 0 \le j \le l_i - 1 .
\]
Substituting these zeros back into \( (\ast) \) leaves only the terms with \( i \le q,\ j = l_i \) and those with \( i > q,\ j = 0 \):
\[
\sum_{i=1}^{q} a_{i l_i} N^{l_i}\u_i + \sum_{i=q+1}^{r} a_{i0}\u_i = \0 .
\]
This is a linear combination of the members of the basis of \( \ker N \) from Step 3, so all the remaining coefficients vanish as well. Hence \( \sB \) is independent, and therefore a basis of \( V \). The lengths satisfy \( \sum_i k_i = n \) by the count above, and reindexing the chains so that the lengths decrease — a permutation of the chains — arranges \( k_1 \ge \dots \ge k_r \). This proves (a), and completes the induction.

(b) Each \( C_i \) is \( N \)-invariant of dimension \( k_i \), with \( [N|_{C_i}] = \J_{k_i}(0) \) in its chain, by @lem-jordan-chain-independent (b). The chains together form the basis \( \sB \) of \( V \), so \( V = C_1 + \dots + C_r \). The sum is direct: if \( \c_1 + \dots + \c_r = \0 \) with \( \c_i \in C_i \), then writing each \( \c_i \) in terms of its own chain turns this into a linear combination of the members of the basis \( \sB \) equal to \( \0 \), so every coefficient is \( 0 \) and every \( \c_i = \0 \); now apply @thm-direct-sum-k-criteria ((b) \( \Rightarrow \) (a)). Finally @thm-direct-sum-invariant-block-diagonal gives that \( [N]_{\sB} \) is block diagonal with blocks \( [N|_{C_i}] = \J_{k_i}(0) \).
:::

The theorem says that a nilpotent operator carries no information beyond the list of chain lengths. In matrix terms: **every nilpotent \( \A \in M_n(F) \) is similar to \( \J_{k_1}(0) \oplus \dots \oplus \J_{k_r}(0) \) for some \( k_1 \ge \dots \ge k_r \ge 1 \) summing to \( n \)** (apply the theorem to \( T_{\A} \) and use @thm-similar-iff-same-operator). The index of nilpotency is \( k_1 \), the largest block (it is also the stabilization index of the kernel chain of @thm-kernel-chain-stabilizes, since \( \ker N^{k_1} = V \)): \( \J_{k}(0)^{k} = 0 \) and \( \J_k(0)^{k-1} \ne 0 \), and powers of a block diagonal matrix act blockwise (@thm-block-diagonal-arithmetic (b)). Two questions remain: are the lengths unique, and how do we find them without finding the chains? One computation answers both.

## Block sizes from the ranks of the powers

The lengths are visible in the ranks of the powers of \( N \), which are similarity invariants. This is the practical algorithm and the uniqueness proof at once.

::: {#thm-nilpotent-block-sizes-from-ranks}
[Block Sizes from Ranks of Powers]

Let \( V \) be finite-dimensional with \( \dim V = n \ge 1 \), let \( N \in \cL(V) \) be nilpotent, and suppose \( \sB \) is a Jordan basis for \( N \) with chain lengths \( k_1 \ge \dots \ge k_r \ge 1 \), as in @thm-nilpotent-structure. Write \( r_j = \rank N^{j} \) for \( j \ge 0 \), so \( r_0 = n \). Then:

::: {.enumerate options="label=(\alph*)"}
1. for every integer \( j \ge 0 \),
   \[
   \rank N^{j} = \sum_{i=1}^{r} \max(k_i - j,\, 0) \qquad \text{and} \qquad \dim\ker N^{j} = \sum_{i=1}^{r}\min(k_i,\, j) ;
   \]
2. for every integer \( j \ge 1 \), the number of chains of length **at least** \( j \) is
   \[
   \#\{\, i : k_i \ge j \,\} = r_{j-1} - r_{j} ;
   \]
3. for every integer \( j \ge 1 \), the number of chains of length **exactly** \( j \) is
   \[
   \#\{\, i : k_i = j \,\} = r_{j-1} - 2r_{j} + r_{j+1} ;
   \]
4. consequently the list \( k_1 \ge \dots \ge k_r \) is determined by \( N \) alone: any two Jordan bases for \( N \) have the same chain lengths. Moreover \( r = n - \rank N = \nullity N \) and \( k_1 \) is the index of nilpotency of \( N \).
:::
:::

::: {.idea}
Everything follows from what \( N^j \) does to the basis: it shifts each chain \( j \) boxes to the left, so the surviving images are the boxes at least \( j \) steps from the left edge. They are members of the basis, hence independent, and we can just count them: chain \( i \) contributes \( k_i - j \) of them, or none if it is too short. Then (b) is a telescoping difference, because lengthening the shift by one step loses one box from every chain that still had one.
:::

::: {.proof}
(a) The basis \( \sB \) consists of the vectors \( N^{m}\u_i \) with \( 1 \le i \le r \) and \( 0 \le m \le k_i - 1 \). Fix \( j \ge 0 \). Applying \( N^{j} \) to a member gives \( N^{j}(N^{m}\u_i) = N^{m+j}\u_i \), which is \( \0 \) when \( m + j \ge k_i \), because \( N^{k_i}\u_i = \0 \), and is a member of \( \sB \), hence non-zero, when \( m + j \le k_i - 1 \). Since the image is spanned by the images of a basis (@thm-image-spanned-by-basis-images),
\[
\im N^{j} = \Span\big(\, N^{m}\u_i : 1 \le i \le r,\ j \le m \le k_i - 1 \,\big).
\]
This spanning list is a sublist of the basis \( \sB \), hence linearly independent, so it is a basis of \( \im N^j \) and \( \rank N^j \) is its length: for each \( i \), the number of integers \( m \) with \( j \le m \le k_i - 1 \) is \( k_i - j \) if \( k_i > j \), and \( 0 \) otherwise, that is \( \max(k_i - j, 0) \). This gives the first formula, and the second follows from @thm-rank-nullity and \( \sum_i k_i = n \):
\[
\dim\ker N^j = n - \rank N^j = \sum_{i=1}^{r}\big(k_i - \max(k_i - j, 0)\big) = \sum_{i=1}^{r}\min(k_i, j) .
\]

(b) By (a), \( r_{j-1} - r_j = \sum_i \big(\max(k_i - j + 1, 0) - \max(k_i - j, 0)\big) \). For a single \( i \), the bracket is \( (k_i - j + 1) - (k_i - j) = 1 \) if \( k_i \ge j \), and \( 0 - 0 = 0 \) if \( k_i \le j - 1 \). Summing over \( i \) counts the indices with \( k_i \ge j \).

(c) Subtract the count in (b) for \( j + 1 \) from the count for \( j \): a chain has length exactly \( j \) if and only if its length is at least \( j \) but not at least \( j + 1 \). This gives \( (r_{j-1} - r_j) - (r_j - r_{j+1}) \).

(d) The numbers \( r_j = \rank N^j \) are defined from \( N \) with no reference to a basis, so by (c) the number of chains of each length is determined by \( N \); hence so is the list of lengths in decreasing order. Taking \( j = 1 \) in (b) gives \( r = \#\{i : k_i \ge 1\} = r_0 - r_1 = n - \rank N \), which is \( \nullity N \) by @thm-rank-nullity. Finally \( N^{k_1} = 0 \) and \( N^{k_1 - 1} \ne 0 \), since by (a) \( \rank N^{k_1} = 0 \) and \( \rank N^{k_1 - 1} \ge k_1 - (k_1 - 1) = 1 \); so \( k_1 \) is the index.
:::

::: {#cor-nilpotent-similar-iff-ranks}
[Similarity of Nilpotent Matrices]

Let \( \A, \B \in M_n(F) \), \( n \ge 1 \), both nilpotent. Then \( \A \sim \B \) if and only if
\[
\rank \A^{j} = \rank \B^{j} \qquad \text{for every } j = 1, 2, \dots, n - 1 .
\]
Equivalently, \( \A \sim \B \) if and only if their chain lengths, as lists in decreasing order, agree.
:::

::: {.proof}
\( (\Rightarrow) \) If \( \A \sim \B \), say \( \B = \P^{-1}\A \P \), then \( \B^j = \P^{-1}\A^j\P \) (@prp-similarity-invariants (c)), so \( \rank \A^j = \rank \B^j \) (@prp-similarity-invariants (a)).

\( (\Leftarrow) \) Since \( \rank T_{\A}^{\,j} = \rank \A^{j} \) and \( \rank T_{\B}^{\,j} = \rank \B^{j} \) for every \( j \) (@thm-rank-map-equals-rank-matrix (a)), the hypothesis is a statement about the operators. By @thm-nilpotent-structure applied to \( T_{\A} \) and to \( T_{\B} \), together with @thm-similar-iff-same-operator, \( \A \) is similar to \( \J_{k_1}(0) \oplus \dots \oplus \J_{k_r}(0) \) and \( \B \) to \( \J_{k'_1}(0) \oplus \dots \oplus \J_{k'_{r'}}(0) \), with both lists decreasing. Equal ranks of all powers force equal lists, by @thm-nilpotent-block-sizes-from-ranks (c) (the ranks for \( j \ge n \) are all \( 0 \), so the listed range suffices). Hence \( \A \) and \( \B \) are similar to the same matrix, and \( \A \sim \B \) because similarity is an equivalence relation (@exm-similarity).
:::

::: {.warning}
**The successive differences count the blocks of size at least \( j \), not the blocks of size exactly \( j \); to get the exact counts, subtract twice.** Suppose \( n = 5 \) and \( \rank N = 3 \), \( \rank N^2 = 1 \), \( \rank N^3 = 0 \). Then \( r_0 - r_1 = 2 \) chains have length \( \ge 1 \), \( r_1 - r_2 = 2 \) have length \( \ge 2 \), and \( r_2 - r_3 = 1 \) has length \( \ge 3 \). Reading these as exact counts would suggest two chains of length \( 1 \), two of length \( 2 \) and one of length \( 3 \), that is, lengths \( 1, 1, 2, 2, 3 \), summing to \( 9 \) instead of \( 5 \). The correct counts are the second differences of @thm-nilpotent-block-sizes-from-ranks (c): exactly \( 2 - 2 = 0 \) chains of length \( 1 \), exactly \( 2 - 1 = 1 \) of length \( 2 \), and exactly \( 1 - 0 = 1 \) of length \( 3 \). The partition is \( (3, 2) \), and \( 3 + 2 = 5 \) as it must be.
:::

::: {.check}
A nilpotent \( N \) on a space of dimension \( 6 \) has \( \rank N = 3 \) and \( \rank N^2 = 1 \). What are its chain lengths?
:::

::: {.solution}
Here \( r_0 = 6 \), \( r_1 = 3 \) and \( r_2 = 1 \), so there are \( r_0 - r_1 = 3 \) chains by part (b) of @thm-nilpotent-block-sizes-from-ranks. Also \( r_3 = 0 \): a chain of length \( \ge 4 \) would contribute at least \( 2 \) to \( r_2 = \sum_i\max(k_i - 2, 0) = 1 \), so every \( k_i \le 3 \) and \( r_3 = \sum_i\max(k_i - 3, 0) = 0 \). By part (c) the exact counts are \( r_0 - 2r_1 + r_2 = 1 \) chain of length \( 1 \), \( r_1 - 2r_2 + r_3 = 1 \) of length \( 2 \), and \( r_2 - 2r_3 + r_4 = 1 \) of length \( 3 \). So the lengths are \( (3, 2, 1) \), which indeed sum to \( 6 \).
:::

## Partitions and Young diagrams

The data left over is a list of decreasing positive integers with a given sum. Such lists have a name.

::: {#def-partition-of-n}
[Partition of an Integer, Young Diagram, Dual Partition]

Let \( n \ge 1 \). A **partition of \( n \)** is a finite list of integers
\[
k_1 \ge k_2 \ge \dots \ge k_r \ge 1 \qquad \text{with} \qquad k_1 + k_2 + \dots + k_r = n .
\]
Its **Young diagram** is the left-justified array of \( n \) boxes with \( k_i \) boxes in row \( i \). The **dual partition** \( k_1^{*} \ge k_2^{*} \ge \dots \) is the list of **column** lengths of the diagram,
\[
k_j^{*} = \#\{\, i : k_i \ge j \,\},
\]
which is again a partition of \( n \).
:::

(The word *partition* is also used for a partition of a **set** into blocks (@def-partition) and for a partition of the row and column indices of a block matrix (@def-block-partition). Those are different notions; here the blocks are boxes in a diagram and the data is a list of numbers.)

For a nilpotent \( N \) on a space of dimension \( n \), the chain lengths form a partition of \( n \), and @thm-nilpotent-block-sizes-from-ranks (b) identifies the dual partition:
\[
k_j^{*} = \#\{i : k_i \ge j\} = r_{j-1} - r_j = \dim\ker N^{j} - \dim\ker N^{j-1},
\]
using @thm-rank-nullity for the last equality. **The rows of the diagram are the chains; the columns are the jumps of the kernel chain.** In particular the first column is a basis of \( \ker N \) (its boxes are the vectors \( N^{k_i - 1}\u_i \)), the first two columns span \( \ker N^2 \), and so on. Here is the diagram for the partition \( (4, 2, 2, 1) \) of \( 9 \), with the columns marked:

\begin{center}
\begin{tikzpicture}[scale=0.62, every node/.style={font=\small}]
  \foreach \r/\len in {0/4, 1/2, 2/2, 3/1} {
    \foreach \c in {1,...,\len} {
      \draw (\c-1, -\r) rectangle ++(1,-1);
    }
  }
  \foreach \r in {0,1,2,3} { \draw[very thick] (0,-\r) rectangle ++(1,-1); }
  \node at (0.5,0.75) {$4$};
  \node at (1.5,0.75) {$3$};
  \node at (2.5,0.75) {$1$};
  \node at (3.5,0.75) {$1$};
  \node at (-1.3,-0.5) {$k_1 = 4$};
  \node at (-1.3,-1.5) {$k_2 = 2$};
  \node at (-1.3,-2.5) {$k_3 = 2$};
  \node at (-1.3,-3.5) {$k_4 = 1$};
  \node[align=left, anchor=west] at (5,-1.2) {column lengths, above: the dual partition $(4,3,1,1)$\\ rows: the chain lengths $(4,2,2,1)$\\ the thick first column: a basis of $\ker N$\\ $\dim\ker N^{j} = 4, 7, 8, 9$ for $j = 1,2,3,4$};
\end{tikzpicture}
\end{center}

Reading the diagram by rows gives the Jordan blocks; reading it by columns gives the dimensions \( \dim\ker N^j = k_1^* + \dots + k_j^* \). Transposing the diagram exchanges a partition with its dual.

::: {.remark}
For each \( n \), the nilpotent operators on an \( n \)-dimensional space, up to similarity, correspond exactly to the partitions of \( n \), and the correspondence does not depend on the field. For \( n = 4 \) the partitions are
\[
(4), \quad (3, 1), \quad (2, 2), \quad (2, 1, 1), \quad (1, 1, 1, 1),
\]
so there are exactly five similarity classes of nilpotent \( 4 \times 4 \) matrices over any field, with indices of nilpotency \( 4, 3, 2, 2, 1 \).
:::

## Finding a Jordan basis

The proof of @thm-nilpotent-structure is an algorithm, but run from the inside out. For small matrices it is easier to work from the longest chain down, using the rank data to know what to look for.

::: {.algorithm}
**Jordan basis of a nilpotent operator.**

1. Compute \( r_j = \rank N^j \) until \( r_j = 0 \), and read off the chain lengths by @thm-nilpotent-block-sizes-from-ranks (c).
2. For each length in decreasing order, choose a top \( \u \) with \( N^{k-1}\u \ne \0 \), keeping the chains collected so far independent, and write down its chain.
3. Chains of length \( 1 \) are vectors completing a basis of \( \ker N \) together with the ends \( N^{k_i - 1}\u_i \) of the longer chains. Once \( n \) vectors are collected, @thm-right-size-basis confirms a basis.
:::

::: {#exm-nilpotent-jordan-basis}
[A Jordan Basis for a \( 4 \times 4 \) Nilpotent Matrix]

Let
\[
\N = \begin{pmatrix} 1 & 0 & 1 & 1 \\ 1 & -1 & 1 & 1 \\ 1 & -1 & 1 & 1 \\ -1 & 0 & -1 & -1 \end{pmatrix} \in M_4(\nQ).
\]
Show that \( \N \) is nilpotent, find its chain lengths, and find a Jordan basis together with an invertible \( \P \) with \( \P^{-1}\N\P \) a direct sum of blocks \( \J_k(0) \).
:::

::: {.solution}
*Nilpotency and ranks.* Multiplying out,
\[
\N^2 = \begin{pmatrix} 1 & -1 & 1 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ -1 & 1 & -1 & -1 \end{pmatrix}, \qquad \N^3 = 0 ,
\]
the last because every row of \( \N^2 \) is a multiple of \( (1, -1, 1, 1) \), while
\[
\begin{aligned}
(1, -1, 1, 1)\,\N
  &= (1 - 1 + 1 - 1,\ \ 0 + 1 - 1 + 0,\ \ 1 - 1 + 1 - 1,\ \ 1 - 1 + 1 - 1) \\
  &= 0 .
\end{aligned}
\]
Since \( \N^2 \ne 0 \), the index is \( 3 \). Rows \( 2 \) and \( 3 \) of \( \N \) are equal and row \( 4 = -\)row \( 1 \), so \( \rank \N = 2 \), and \( \rank \N^2 = 1 \). Thus
\[
r_0 = 4, \quad r_1 = 2, \quad r_2 = 1, \quad r_3 = 0 .
\]
By @thm-nilpotent-block-sizes-from-ranks (c), the number of chains of length \( 1 \) is \( r_0 - 2r_1 + r_2 = 4 - 4 + 1 = 1 \), of length \( 2 \) is \( r_1 - 2r_2 + r_3 = 2 - 2 + 0 = 0 \), and of length \( 3 \) is \( r_2 - 2r_3 + r_4 = 1 - 0 + 0 = 1 \). The partition is \( (3, 1) \): one chain of length \( 3 \) and one of length \( 1 \), matching the picture drawn after @thm-nilpotent-structure.

*The long chain.* We need \( \u_1 \notin \ker \N^{2} \). Try \( \u_1 = \e_1 \): the first column of \( \N^2 \) is \( (1, 0, 0, -1) \ne \0 \), so \( \N^2\e_1 \ne \0 \) and \( \e_1 \) works. Its chain, read off the first columns of \( \N \) and \( \N^2 \), is
\[
\N^2\e_1 = (1, 0, 0, -1), \qquad \N\e_1 = (1, 1, 1, -1), \qquad \e_1 .
\]

*The short chain.* \( \ker \N \) has dimension \( 2 \) (@thm-rank-nullity-matrix). The equations \( x_1 + x_3 + x_4 = 0 \) (row \( 1 \)) and \( x_1 - x_2 + x_3 + x_4 = 0 \) (row \( 2 \)) give \( x_2 = 0 \) and \( x_1 = -x_3 - x_4 \), so
\[
\ker \N = \Span\big((-1, 0, 1, 0),\ (-1, 0, 0, 1)\big).
\]
The end of the long chain, \( \N^2\e_1 = (1, 0, 0, -1) \), is the second of these basis vectors with a minus sign, so we complete it to a basis of \( \ker \N \) with \( \u_2 = (-1, 0, 1, 0) \).

*The basis and the matrix.* Take
\[
\begin{aligned}
\sB &= \big(\,(1, 0, 0, -1),\ (1, 1, 1, -1),\ \e_1,\ (-1, 0, 1, 0)\,\big), \\
\P &= \begin{pmatrix} 1 & 1 & 1 & -1 \\ 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 1 \\ -1 & -1 & 0 & 0 \end{pmatrix},
\end{aligned}
\]
the matrix whose columns are the vectors of \( \sB \). Its third column has a single non-zero entry, the \( 1 \) in row \( 1 \), so expanding along that column (@thm-laplace-expansion) gives
\[
\det \P = \det\begin{pmatrix} 0 & 1 & 0 \\ 0 & 1 & 1 \\ -1 & -1 & 0 \end{pmatrix} = -1 ,
\]
the last determinant computed by expanding along its own first column. So \( \P \) is invertible and \( \sB \) is a basis. Then
\[
\P^{-1}N\P = \J_3(0) \oplus \J_1(0) = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}.
\]
There is no need to invert \( \P \) to check this: the claim \( \P^{-1}N\P = \J \) is the same as \( N\P = \P \J \), which reads column by column as
\[
\begin{aligned}
\N(1,0,0,-1) &= \0, \\
\N(1,1,1,-1) &= (1,0,0,-1), \\
\N\e_1 &= (1,1,1,-1), \\
\N(-1,0,1,0) &= \0 ,
\end{aligned}
\]
and these four statements are exactly how the chains were built (the first and last say that the two chain ends lie in \( \ker \N \)). As a sample verification, the second row of \( \N(1,1,1,-1) \) is \( 1 - 1 + 1 - 1 = 0 \), matching the second coordinate of \( (1, 0, 0, -1) \).
:::

## Exercises

### A. Check your understanding

:::: {#exr-nilpotent-operators-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define a nilpotent operator and its index of nilpotency.
2. State the structure theorem for nilpotent operators, and say what a Jordan basis is.
3. Write down the formula for the number of chains of length at least \( j \) in terms of the ranks of the powers.
4. True or false: a singular matrix is nilpotent. Justify your answer.
5. True or false: two nilpotent matrices in \( M_n(F) \) with the same rank are similar. Justify your answer.
6. How many similarity classes of nilpotent matrices are there in \( M_3(F) \), and what are their indices of nilpotency?
:::
::::

::: {.solution}
(a) \( N \in \cL(V) \) is nilpotent if \( N^s = 0 \) for **some** integer \( s \ge 1 \); the index is the least such \( s \) (@def-nilpotent).

(b) For nilpotent \( N \) on \( V \) with \( \dim V = n \ge 1 \), there are chains generated by \( \u_1, \dots, \u_r \) of lengths \( k_1 \ge \dots \ge k_r \ge 1 \) summing to \( n \) whose concatenation is a basis of \( V \) — a Jordan basis — and in it \( [N] = \J_{k_1}(0) \oplus \dots \oplus \J_{k_r}(0) \) (@thm-nilpotent-structure).

(c) \( \#\{i : k_i \ge j\} = \rank N^{j-1} - \rank N^{j} \) (@thm-nilpotent-block-sizes-from-ranks (b)).

(d) False. \( \diag(0, 1) \) is singular, and \( \diag(0,1)^k = \diag(0,1) \ne 0 \) for every \( k \ge 1 \). What is true is the converse: a nilpotent matrix on a non-zero space is singular, since \( 0 \in \spec(N) \) (@prp-nilpotent-basic (c)).

(e) False for \( n \ge 4 \). The partitions \( (3, 1) \) and \( (2, 2) \) of \( 4 \) both give rank \( 2 \), but \( \rank N^2 \) is \( 1 \) and \( 0 \) respectively, so the matrices are not similar (@cor-nilpotent-similar-iff-ranks). (For \( n \le 3 \) the rank does determine the partition.)

(f) Three, one for each partition of \( 3 \): \( (3), (2,1), (1,1,1) \), with indices \( 3, 2, 1 \).
:::

### B. Practice

:::: {#exr-nilpotent-operators-b1}
[B1: Block sizes from rank data]

In each case \( N \) is nilpotent on a space of dimension \( n \) over \( F \). Determine the chain lengths, or explain why no such operator exists.

::: {.enumerate options="label=(\alph*)"}
1. \( n = 7 \), \( \rank N = 4 \), \( \rank N^2 = 2 \), \( \rank N^3 = 1 \), \( \rank N^4 = 0 \).
2. \( n = 6 \), \( \rank N = 3 \), \( \rank N^2 = 1 \), \( \rank N^3 = 0 \).
3. \( n = 6 \), \( \rank N = 4 \), \( \rank N^2 = 3 \), \( \rank N^3 = 0 \).
:::
::::

::: {.solution}
(a) With \( r_0, \dots, r_4 = 7, 4, 2, 1, 0 \), the exact counts from @thm-nilpotent-block-sizes-from-ranks (c) are: length \( 1 \): \( 7 - 8 + 2 = 1 \); length \( 2 \): \( 4 - 4 + 1 = 1 \); length \( 3 \): \( 2 - 2 + 0 = 0 \); length \( 4 \): \( 1 - 0 + 0 = 1 \). The lengths are \( (4, 2, 1) \), and \( 4 + 2 + 1 = 7 \).

(b) With \( r_0, \dots, r_3 = 6, 3, 1, 0 \): length \( 1 \): \( 6 - 6 + 1 = 1 \); length \( 2 \): \( 3 - 2 + 0 = 1 \); length \( 3 \): \( 1 - 0 + 0 = 1 \). The lengths are \( (3, 2, 1) \), summing to \( 6 \).

(c) No such operator exists. By (b) of the theorem, the number of chains of length \( \ge 2 \) would be \( r_1 - r_2 = 1 \), while the number of length \( \ge 3 \) would be \( r_2 - r_3 = 3 \), which is impossible: a chain of length \( \ge 3 \) has length \( \ge 2 \), so the counts must be non-increasing in \( j \). (Equivalently, @thm-nilpotent-block-sizes-from-ranks (c) would give \( r_1 - 2r_2 + r_3 = 4 - 6 + 0 = -2 \) chains of length \( 2 \), which is absurd.)
:::

:::: {#exr-nilpotent-operators-b2}
[B2: The five classes in dimension four]

Let \( F \) be any field.

::: {.enumerate options="label=(\alph*)"}
1. List the five partitions of \( 4 \), and for each write down the corresponding nilpotent matrix in \( M_4(F) \) as a direct sum of blocks \( \J_k(0) \).
2. For each, compute \( \rank \N \), \( \rank \N^2 \), \( \rank \N^3 \) and the index of nilpotency.
3. Which pairs among them share the same rank? Which invariant separates each such pair?
4. Deduce that \( \rank \N \) alone is not a complete invariant of nilpotent matrices, but the full list of ranks of powers is.
:::
::::

::: {.solution}
(a) \( (4) \): \( \J_4(0) \); \( (3,1) \): \( \J_3(0) \oplus \J_1(0) \); \( (2,2) \): \( \J_2(0) \oplus \J_2(0) \); \( (2,1,1) \): \( \J_2(0) \oplus \J_1(0) \oplus \J_1(0) \); \( (1,1,1,1) \): the zero matrix.

(b) Using \( \rank \N^j = \sum_i\max(k_i - j, 0) \) (@thm-nilpotent-block-sizes-from-ranks (a)), the ranks \( (\rank \N, \rank \N^2, \rank \N^3) \) and the index are:

- \( (4) \): ranks \( 3, 2, 1 \); index \( 4 \).
- \( (3,1) \): ranks \( 2, 1, 0 \); index \( 3 \).
- \( (2,2) \): ranks \( 2, 0, 0 \); index \( 2 \).
- \( (2,1,1) \): ranks \( 1, 0, 0 \); index \( 2 \).
- \( (1,1,1,1) \): ranks \( 0, 0, 0 \); index \( 1 \).

(c) Only \( (3,1) \) and \( (2,2) \) share a rank, namely \( 2 \). They are separated by \( \rank \N^2 \) (\( 1 \) against \( 0 \)), equivalently by the index (\( 3 \) against \( 2 \)) or the minimal polynomial (\( x^3 \) against \( x^2 \), @prp-nilpotent-basic (b)).

(d) The pair in (c) shows that equal rank does not imply similarity, while equality of \( \rank \N^j \) for all \( j \) does (@cor-nilpotent-similar-iff-ranks).
:::

:::: {#exr-nilpotent-operators-b3}
[B3: A Jordan basis by hand]

Let
\[
\M = \begin{pmatrix} -1 & -1 & 1 & -1 \\ 1 & 2 & -2 & 1 \\ 1 & 2 & -2 & 1 \\ 1 & 1 & -1 & 1 \end{pmatrix} \in M_4(\nQ).
\]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \M^2 = 0 \) and compute \( \rank \M \).
2. Determine the chain lengths of \( \M \).
3. Find a Jordan basis and an invertible \( \P \) with \( \P^{-1}\M \P \) a direct sum of blocks \( \J_k(0) \). Verify your answer by checking \( \M \P = \P \J \) column by column.
:::

*Hint: for (c), the tops of the chains may be taken among the standard basis vectors.*
::::

::: {.solution}
(a) Write \( \m_1, \dots, \m_4 \) for the columns of \( \M \), so \( \m_1 = (-1,1,1,1) \), \( \m_2 = (-1,2,2,1) \), \( \m_3 = -\m_2 \) and \( \m_4 = \m_1 \). The columns of \( \M^2 \) are \( \M\m_1, \dots, \M\m_4 \), so it is enough to check the first two. Row by row,
\[
\begin{aligned}
\M\m_1 &= (1 - 1 + 1 - 1,\ -1 + 2 - 2 + 1,\ -1 + 2 - 2 + 1,\ -1 + 1 - 1 + 1) \\
  &= \0,
\end{aligned}
\]
\[
\begin{aligned}
\M\m_2 &= (1 - 2 + 2 - 1,\ -1 + 4 - 4 + 1,\ -1 + 4 - 4 + 1,\ -1 + 2 - 2 + 1) \\
  &= \0 .
\end{aligned}
\]
Hence \( \M\m_3 = -\M\m_2 = \0 \) and \( \M\m_4 = \M\m_1 = \0 \), so \( \M^2 = 0 \). Also \( \im \M = \Span(\m_1, \m_2) \) by the relations among the columns, and \( \m_1, \m_2 \) are not proportional, so \( \rank \M = 2 \).

(b) \( r_0, r_1, r_2 = 4, 2, 0 \). Chains of length \( 1 \): \( r_0 - 2r_1 + r_2 = 4 - 4 + 0 = 0 \); of length \( 2 \): \( r_1 - 2r_2 + r_3 = 2 \). So the partition is \( (2, 2) \): two chains of length \( 2 \).

(c) We need two tops \( \u, \w \) with \( \M\u, \M\w \) independent; since \( \rank \M = 2 \) and \( \im \M = \Span(\m_1, \m_2) \), the vectors \( \u = \e_1 \) and \( \w = \e_2 \) do it, with \( \M\e_1 = \m_1 = (-1, 1, 1, 1) \) and \( \M\e_2 = \m_2 = (-1, 2, 2, 1) \). Take
\[
\sB = \big(\,(-1,1,1,1),\ \e_1,\ (-1,2,2,1),\ \e_2\,\big), \qquad \P = \begin{pmatrix} -1 & 1 & -1 & 0 \\ 1 & 0 & 2 & 1 \\ 1 & 0 & 2 & 0 \\ 1 & 0 & 1 & 0 \end{pmatrix} .
\]
The last column of \( \P \) has a single non-zero entry, the \( 1 \) in row \( 2 \), so expanding along it (@thm-laplace-expansion) gives
\[
\det \P = \det\begin{pmatrix} -1 & 1 & -1 \\ 1 & 0 & 2 \\ 1 & 0 & 1 \end{pmatrix} = -1 \cdot (1 \cdot 1 - 2 \cdot 1) = 1 \ne 0,
\]
where the second determinant was expanded along its second column. So \( \sB \) is a basis, and
\[
\P^{-1}\M \P = \J_2(0) \oplus \J_2(0).
\]
Column by column, \( \M \P = \P \J \) says: \( \M(-1,1,1,1) = \0 \) (first column of \( \P \J \) is \( \0 \)); \( \M\e_1 = (-1,1,1,1) \) (second column of \( \P \J \) is the first column of \( \P \)); \( \M(-1,2,2,1) = \0 \); and \( \M\e_2 = (-1,2,2,1) \). All four were verified in (a) and (c).
:::

### C. Going deeper

:::: {#exr-nilpotent-operators-c1}
[C1: A nilpotent matrix is similar to its transpose]

Let \( \A \in M_n(F) \) be nilpotent.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \A^{\tp} \) is nilpotent and that \( \rank (\A^{\tp})^{j} = \rank \A^{j} \) for every \( j \ge 1 \).
2. Deduce that \( \A \sim \A^{\tp} \).
3. For \( \A = \J_3(0) \), find an explicit \( \P \) with \( \P^{-1}\A \P = \A^{\tp} \).
:::
::::

::: {.solution}
(a) \( (\A^{\tp})^{j} = (\A^{j})^{\tp} \) (@thm-transpose-properties), so \( (\A^{\tp})^{n} = (\A^n)^{\tp} = 0 \) by @prp-nilpotent-basic (a), and \( \A^{\tp} \) is nilpotent. A matrix and its transpose have the same rank (@thm-row-rank-equals-column-rank), so \( \rank(\A^{\tp})^j = \rank (\A^j)^{\tp} = \rank \A^j \).

(b) Both matrices are nilpotent with equal ranks of all powers, so @cor-nilpotent-similar-iff-ranks gives \( \A \sim \A^{\tp} \).

(c) \( \J_3(0) \) sends \( \e_1 \mapsto \0 \), \( \e_2 \mapsto \e_1 \), \( \e_3 \mapsto \e_2 \), while \( \J_3(0)^{\tp} \) sends \( \e_1 \mapsto \e_2 \mapsto \e_3 \mapsto \0 \), that is, it is the shift in the reversed basis. So take the reversal permutation matrix
\[
\P = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix}, \qquad \P^{-1} = \P .
\]
Then \( \P^{-1}\J_3(0)\P = \J_3(0)^{\tp} \), as one checks column by column: \( \J_3(0)\P \) has columns \( \J_3(0)\e_3 = \e_2 \), \( \J_3(0)\e_2 = \e_1 \), \( \J_3(0)\e_1 = \0 \), and \( \P\,\J_3(0)^{\tp} \) has columns \( \P\e_2 = \e_2 \), \( \P\e_3 = \e_1 \), \( \P\0 = \0 \). (The same reversal works for every \( \J_k(0) \), and hence, blockwise, for every nilpotent matrix in Jordan form.)
:::

:::: {#exr-nilpotent-operators-c2}
[C2: One long chain]

Let \( V \) be finite-dimensional with \( \dim V = n \ge 1 \), and let \( N \in \cL(V) \) be nilpotent with \( N^{n-1} \ne 0 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that there is a basis of \( V \) in which the matrix of \( N \) is \( \J_n(0) \).
2. Deduce that \( m_N = p_N = x^n \), and that \( \nullity N = 1 \).
3. Show that the conclusion of (a) fails for \( \N = \J_2(0) \oplus \J_1(0) \) on a space of dimension \( 3 \), and say which hypothesis fails.
:::

*Hint: for (a), take a vector outside \( \ker N^{n-1} \), which exists precisely because \( N^{n-1} \ne 0 \).*
::::

::: {.solution}
(a) Since \( N^{n-1} \ne 0 \), there is \( \u \in V \) with \( N^{n-1}\u \ne \0 \), while \( N^{n}\u = \0 \) by @prp-nilpotent-basic (a). So \( \u \) generates a Jordan chain of length \( n \) (@def-jordan-chain), which is a linearly independent list of \( n = \dim V \) vectors (@lem-jordan-chain-independent (a)), hence a basis of \( V \) (@thm-right-size-basis (a)). In it the matrix of \( N \) is \( \J_n(0) \), by @lem-jordan-chain-independent (b) with \( C = V \).

(b) In that basis \( \rank N^j = n - j \) for \( 0 \le j \le n \) (@thm-nilpotent-block-sizes-from-ranks (a) with the single length \( k_1 = n \)), so \( \nullity N = 1 \) by @thm-rank-nullity and the index of nilpotency is \( n \). Hence \( m_N = x^n \) by @prp-nilpotent-basic (b), and \( p_N = x^n \) as well; they coincide, which by @cor-minimal-divides-characteristic is the extreme case \( \deg m_N = n \).

(c) For \( \N = \J_2(0) \oplus \J_1(0) \) on \( F^3 \) we have \( \N^2 = 0 \), so \( \N^{n-1} = \N^2 = 0 \) and the hypothesis \( \N^{n-1} \ne 0 \) fails. Accordingly \( \N \) is not similar to \( \J_3(0) \): its rank is \( 1 \), while \( \rank \J_3(0) = 2 \), and similar matrices have equal ranks (@prp-similarity-invariants (a)). Its partition is \( (2, 1) \), not \( (3) \).
:::
