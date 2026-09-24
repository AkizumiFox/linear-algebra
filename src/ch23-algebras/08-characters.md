# Characters and Orthogonality

Complete reducibility (@cor-complete-reducibility) promises that every complex representation of a finite group breaks into irreducible pieces, but the promise is not constructive: it says nothing about which pieces, or how many of each. This section produces a small table of numbers that answers both questions. To each representation we attach one function \( G \to \nC \), its character, and we prove that the characters of the irreducible representations are an **orthonormal basis** of a space of functions we can compute the dimension of by counting. Everything a complex representation is, up to equivalence, is then read off from one row of numbers.

Throughout, \( G \) is a **finite** group and the field is \( \nC \). The hypothesis matters twice over: \( \operatorname{char}\nC = 0 \) never divides \( \lvert G\rvert \), so @thm-maschke applies; and \( \nC \) is algebraically closed, so Schur's lemma (@thm-schurs-lemma) gives that the only operators commuting with an irreducible representation are the scalars. The theory over a field whose characteristic divides \( \lvert G \rvert \) — modular representation theory — is a different subject, and this book does not enter it.

## Conjugacy classes

Before characters we need the sets they are constant on. The book has met them only in an exercise of Section 1 (@exr-associative-algebras-c1), so we build them here.

::: {#def-conjugacy-class}
[Conjugate elements, conjugacy class]

Let \( G \) be a group. Elements \( g, h \in G \) are **conjugate** if \( h = xgx^{-1} \) for **some** \( x \in G \). The **conjugacy class** of \( g \) is
\[
  C(g) \coloneqq \{ xgx^{-1} : x \in G \} .
\]
:::

Conjugacy is an equivalence relation (@def-equivalence-relation): \( g = 1g1^{-1} \) gives reflexivity; if \( h = xgx^{-1} \), then \( g = x^{-1}h(x^{-1})^{-1} \), which gives symmetry using @thm-group-basic-properties; and if \( h = xgx^{-1} \) and \( k = yhy^{-1} \), then \( k = (yx)g(yx)^{-1} \), which gives transitivity. Hence the conjugacy classes are the equivalence classes, and by @thm-partition they **partition** \( G \): every element lies in exactly one class. We write \( k \) for the number of conjugacy classes of \( G \), a finite number since \( G \) is finite.

In an abelian group \( xgx^{-1} = g \) for every \( x \), so every class is a single element and \( k = \lvert G\rvert \). At the other extreme, \( C(1) = \{1\} \) always.

::: {#exm-conjugacy-classes-s3}
[The conjugacy classes of the symmetric group on three letters]

Find the conjugacy classes of \( S_3 \).
:::

::: {.solution}
First a rule that does the work. For \( \sigma \in S_n \) and a cycle \( (i_1\ i_2\ \cdots\ i_r) \),
\[
  \sigma\,(i_1\ i_2\ \cdots\ i_r)\,\sigma^{-1} = (\sigma(i_1)\ \sigma(i_2)\ \cdots\ \sigma(i_r)) .
\]
Both sides are permutations, so it is enough to check they agree at every point. At \( \sigma(i_j) \): the left side applies \( \sigma^{-1} \) to get \( i_j \), then the cycle to get \( i_{j+1} \) (indices read cyclically), then \( \sigma \) to get \( \sigma(i_{j+1}) \); the right side does the same in one step. At a point \( \sigma(m) \) with \( m \notin \{i_1, \dots, i_r\} \): the left side gives \( \sigma(m) \) back, and so does the right side, since \( \sigma(m) \) is not among the \( \sigma(i_j) \) by injectivity. Every point of \( \{1, \dots, n\} \) is \( \sigma(m) \) for exactly one \( m \), so the two agree.

So conjugation relabels the entries of a cycle. In \( S_3 \), conjugating \( (1\ 2) \) by the six elements produces \( (\sigma(1)\ \sigma(2)) \), and as \( \sigma \) runs over \( S_3 \) the pair \( \{\sigma(1), \sigma(2)\} \) runs over all three two-element subsets; so \( C((1\ 2)) = \{(1\ 2), (1\ 3), (2\ 3)\} \). Conjugating \( (1\ 2\ 3) \) gives \( (\sigma(1)\ \sigma(2)\ \sigma(3)) \), which is \( (1\ 2\ 3) \) or \( (1\ 3\ 2) \) according to the cyclic order; both occur, for \( \sigma = \id \) and \( \sigma = (1\ 2) \), so \( C((1\ 2\ 3)) = \{(1\ 2\ 3), (1\ 3\ 2)\} \). The three classes are
\[
  \{\id\}, \qquad \{(1\ 2), (1\ 3), (2\ 3)\}, \qquad \{(1\ 2\ 3), (1\ 3\ 2)\},
\]
of sizes \( 1, 3, 2 \), which add to \( 6 = \lvert S_3\rvert \) as a partition must. So \( k = 3 \) for \( S_3 \) — the same number as the three irreducible complex representations found in @exm-s3-irreducibles. That is no coincidence, and the theorem explaining it is the main result of this section.
:::

## The character of a representation

A representation \( \rho \) on \( V \) is a whole family of matrices, and the matrices change when the basis does. To compare representations we want something attached to \( \rho \) that does not move. Chapter 2 already supplies the candidate: the trace of an operator does not depend on the basis (@def-trace-operator), and similar operators have equal traces.

*The character of a representation records one number per group element: the trace of the operator that element acts by.*

::: {#def-character}
[Character]

Let \( \rho \) be a representation of a finite group \( G \) on a finite-dimensional complex vector space \( V \). The **character** of \( \rho \) is the function
\[
  \chi_\rho \colon G \to \nC, \qquad \chi_\rho(g) \coloneqq \tr \rho(g) .
\]
Its **degree** is \( \chi_\rho(1) = \dim V \). A character is **irreducible** if \( \rho \) is irreducible (@def-irreducible-representation).
:::

In words: a character is a list of \( \lvert G\rvert \) complex numbers, one per group element, obtained by computing traces. It throws away a great deal — the whole matrix becomes one number — and the content of this section is that it throws away exactly the information we did not want.

**Examples.** Let \( G \) be finite.

- The trivial representation has \( \chi(g) = \tr(\id_{\nC}) = 1 \) for every \( g \). We write \( \chi_{\mathrm{triv}} \) for the constant function \( 1 \).
- The sign representation of \( S_n \) has \( \chi(\sigma) = \sgn(\sigma) \).
- The permutation representation of \( S_n \) on \( \nC^n \) has \( \chi(\sigma) = \#\{i : \sigma(i) = i\} \), the number of **fixed points**. Indeed the matrix of \( \rho(\sigma) \) in the standard basis has \( (i, i) \)-entry equal to \( 1 \) exactly when \( \sigma(i) = i \), and \( 0 \) otherwise.
- The regular representation on \( \nC[G] \) has \( \chi_{\mathrm{reg}}(1) = \lvert G\rvert \) and \( \chi_{\mathrm{reg}}(g) = 0 \) for \( g \ne 1 \). The matrix of \( \rho_{\mathrm{reg}}(g) \) in the basis \( \{\delta_h\} \) has \( (h, h) \)-entry equal to \( 1 \) exactly when \( gh = h \), that is, when \( g = 1 \) by cancellation (@thm-group-basic-properties).

One fact about finite groups is needed first, and Chapter 0 did not record it. It costs four lines, and Section 9 will use it constantly.

::: {#lem-element-has-finite-order}
[Order of an Element]

Let \( G \) be a finite group and \( g \in G \). Then there is a least integer \( m \ge 1 \) with \( g^m = 1 \), called the **order** of \( g \). Moreover \( g^k = g^l \) if and only if \( m \) divides \( k - l \), and
\[
\langle g\rangle \coloneqq \{g^k : k \in \nZ\} = \{1, g, g^2, \dots, g^{m-1}\}
\]
is a subgroup of \( G \) with exactly \( m \) elements.
:::

::: {.proof}
The \( \lvert G\rvert + 1 \) elements \( g^0, g^1, \dots, g^{\lvert G\rvert} \) cannot all be distinct, so \( g^i = g^j \) for some \( 0 \le i < j \). Canceling \( g^i \) (@thm-group-basic-properties) gives \( g^{\,j-i} = 1 \) with \( j - i \ge 1 \). Hence the set of positive integers \( p \) with \( g^p = 1 \) is non-empty, and it has a least element \( m \).

Suppose \( g^k = g^l \), so \( g^{\,k-l} = 1 \). Divide: \( k - l = qm + r \) with \( 0 \le r < m \). Then
\[
g^r = (g^m)^{-q}\,g^{\,k-l} = 1 ,
\]
and minimality of \( m \) forces \( r = 0 \), that is \( m \mid k - l \). Conversely \( m \mid k-l \) gives \( g^{\,k-l} = (g^m)^{(k-l)/m} = 1 \), so \( g^k = g^l \).

Consequently \( g^k \) depends only on \( k \) modulo \( m \), so \( \langle g\rangle = \{1, g, \dots, g^{m-1}\} \), and those \( m \) elements are distinct because \( m \nmid k - l \) whenever \( 0 \le l < k \le m-1 \). Finally \( 1 \in \langle g\rangle \), \( g^kg^l = g^{k+l} \in \langle g\rangle \) and \( (g^k)^{-1} = g^{-k} \in \langle g\rangle \), so \( \langle g\rangle \) is a subgroup (@def-subgroup).
:::

The next proposition collects the properties we use constantly. Chapter 4's trace results do all the work.

::: {#prp-character-basic}
[Basic properties of characters]

Let \( \rho \) be a representation of a finite group \( G \) on a complex space \( V \), with character \( \chi = \chi_\rho \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \chi(1) = \dim V \);
2. \( \chi \) is a **class function**: \( \chi(xgx^{-1}) = \chi(g) \) for all \( g, x \in G \);
3. equivalent representations have equal characters;
4. if \( V = U \oplus W \) with both summands \( G \)-invariant, then \( \chi = \chi_{\rho|_U} + \chi_{\rho|_W} \);
5. \( \chi(g^{-1}) = \conj{\chi(g)} \) for every \( g \in G \), and \( \lvert\chi(g)\rvert \le \chi(1) \).
:::
:::

::: {.idea}
Parts (a)–(d) are the four standard facts about the trace read in this setting: the trace of the identity, invariance under conjugation, invariance under similarity, and additivity over a block decomposition. Part (e) is different: it needs to know that \( \rho(g) \) is diagonalizable with eigenvalues on the unit circle, which comes from \( g \) having finite order.
:::

::: {.proof}
(a) \( \rho(1) = \id_V \) (@thm-homomorphism-basic-properties), and \( \tr\id_V = (\dim V)\cdot 1 = \dim V \) in \( \nC \) (@thm-trace-operator-properties).

(b) \( \chi(xgx^{-1}) = \tr\bigl(\rho(x)\rho(g)\rho(x)^{-1}\bigr) = \tr\bigl(\rho(g)\rho(x)^{-1}\rho(x)\bigr) = \tr\rho(g) = \chi(g) \), where the second equality is \( \tr(ST) = \tr(TS) \) (@thm-trace-operator-properties) applied with \( S = \rho(x) \) and \( T = \rho(g)\rho(x)^{-1} \).

(c) If \( \rho'(g) = S\rho(g)S^{-1} \) for an isomorphism \( S \) (@def-equivalent-representations), the same computation as in (b) gives \( \tr\rho'(g) = \tr\rho(g) \).

(d) Choose a basis of \( V \) formed by a basis of \( U \) followed by a basis of \( W \). Since both are invariant, the matrix of \( \rho(g) \) in this basis is block diagonal, with the matrices of \( \rho(g)|_U \) and \( \rho(g)|_W \) on the diagonal. The diagonal entries of the big matrix are those of the two blocks, so the traces add (@def-trace-operator).

(e) We may assume \( V \ne \{\0\} \), since otherwise \( \chi \) is the zero function and both claims are clear.

*Finite order.* By @lem-element-has-finite-order there is an integer \( d \ge 1 \) with \( g^d = 1 \), namely the order of \( g \).

*Diagonalizability.* Then \( \rho(g)^d = \rho(g^d) = \id_V \), so the polynomial \( x^d - 1 \) annihilates \( \rho(g) \). Over \( \nC \) it equals \( \prod_{m=0}^{d-1}(x - \zeta^m) \) with \( \zeta = e^{2\pi i/d} \), a product of **distinct** linear factors (@exm-roots-of-unity). By @thm-diagonalizable-iff-minimal-distinct-linear, (c) \( \Rightarrow \) (a), \( \rho(g) \) is diagonalizable, and every eigenvalue \( \lambda \) satisfies \( \lambda^d = 1 \), hence \( \lvert\lambda\rvert = 1 \).

*Conclusion.* Let \( \lambda_1, \dots, \lambda_n \) be the diagonal entries in an eigenbasis, \( n = \dim V \). Then \( \chi(g) = \sum_j \lambda_j \). In the same basis \( \rho(g)^{-1} = \rho(g^{-1}) \) is diagonal with entries \( \lambda_j^{-1} \), and \( \lvert\lambda_j\rvert = 1 \) gives \( \lambda_j^{-1} = \conj{\lambda_j} \). Hence \( \chi(g^{-1}) = \sum_j \conj{\lambda_j} = \conj{\chi(g)} \). Finally \( \lvert\chi(g)\rvert \le \sum_j\lvert\lambda_j\rvert = n = \chi(1) \) by the triangle inequality for complex numbers (@thm-complex-triangle-inequality), applied repeatedly. This proves the proposition.
:::

::: {.warning}
**A character is not a homomorphism.** For the standard representation of \( S_3 \) (@exm-s3-irreducibles), \( \chi((1\ 2)) = 0 \) and \( \chi((1\ 3)) = 0 \), while \( (1\ 2)(1\ 3) = (1\ 3\ 2) \) has \( \chi((1\ 3\ 2)) = -1 \ne 0 \cdot 0 \). Only characters of **degree \( 1 \)** are homomorphisms, because then \( \chi(g) \) is the whole operator. Nor need the values of a character be real: for \( \nZ/4\nZ \) they include \( \pm i \).
:::

::: {.check}
A representation of \( G \) has character \( \chi \) with \( \chi(1) = 3 \) and \( \chi(g) = 4 \) for some \( g \). What is wrong?
:::

::: {.solution}
Nothing can have such a character: by @prp-character-basic (e), \( \lvert\chi(g)\rvert \le \chi(1) = 3 \) for every \( g \), and \( 4 > 3 \). The bound says a character is largest, in absolute value, at the identity.
:::

## Class functions and their inner product

Part (b) of @prp-character-basic says every character lives in one particular space of functions, and that space is small enough to be a useful home.

::: {#def-class-function}
[Class function]

Let \( G \) be a finite group. A function \( f \colon G \to \nC \) is a **class function** if \( f(xgx^{-1}) = f(g) \) for all \( g, x \in G \); equivalently, if \( f \) is constant on each conjugacy class. The set of class functions is written \( \operatorname{Cl}(G) \).
:::

The functions \( G \to \nC \) form a complex vector space under the pointwise operations (@exm-vector-spaces (d)). The zero function is a class function, and sums and scalar multiples of class functions are class functions, so \( \operatorname{Cl}(G) \) is a subspace of it (@thm-subspace-test). Its dimension is exactly what we want to count.

**Non-example by minimal change.** On \( S_3 \), the function \( f \) that is \( 1 \) at \( (1\ 2) \) and \( 0 \) elsewhere is **not** a class function: \( (1\ 3) = \sigma(1\ 2)\sigma^{-1} \) for \( \sigma = (2\ 3) \), so \( f \) would have to take the same value at \( (1\ 3) \), and it takes \( 0 \) there. Changing \( f \) to be \( 1 \) on **all three** transpositions repairs it; that is the indicator function of a whole class, and those are the building blocks below.

::: {#prp-dimension-class-functions}
[The class functions have dimension the number of classes]

Let \( G \) be a finite group with conjugacy classes \( C_1, \dots, C_k \). For each \( j \) let \( 1_{C_j} \colon G \to \nC \) be the function that is \( 1 \) on \( C_j \) and \( 0 \) elsewhere. Then \( (1_{C_1}, \dots, 1_{C_k}) \) is a basis of \( \operatorname{Cl}(G) \), and \( \dim\operatorname{Cl}(G) = k \).
:::

::: {.proof}
Each \( 1_{C_j} \) is constant on every class — it is \( 1 \) on \( C_j \) and \( 0 \) on the others — so it lies in \( \operatorname{Cl}(G) \).

*Spanning.* Let \( f \in \operatorname{Cl}(G) \) and pick \( g_j \in C_j \) for each \( j \). Every \( g \in G \) lies in exactly one class \( C_j \) (the classes partition \( G \)), and then \( f(g) = f(g_j) \) while \( \sum_l f(g_l)1_{C_l}(g) = f(g_j) \). So \( f = \sum_{j} f(g_j)1_{C_j} \).

*Independence.* Suppose \( \sum_j c_j 1_{C_j} = 0 \). Evaluating at \( g_j \in C_j \) gives \( c_j = 0 \), since every other \( 1_{C_l} \) vanishes there. Hence the list is a basis and \( \dim\operatorname{Cl}(G) = k \).
:::

Now the pairing. It is the standard inner product of \( \nC^{\lvert G\rvert} \), with the coordinates indexed by \( G \) and normalized by \( \lvert G\rvert \) so that the trivial character has length \( 1 \).

::: {#def-character-inner-product}
[The inner product of class functions]

For functions \( f, f' \colon G \to \nC \) on a finite group \( G \), set
\[
  \inner{f}{f'} \coloneqq \frac{1}{\lvert G\rvert}\sum_{g \in G} f(g)\,\conj{f'(g)} .
\]
:::

This satisfies (IP1)–(IP3) of @def-inner-product on the space of all functions \( G \to \nC \), hence on the subspace \( \operatorname{Cl}(G) \): linearity in the first slot and conjugate symmetry are immediate from the formula, and \( \inner{f}{f} = \tfrac1{\lvert G\rvert}\sum_g \lvert f(g)\rvert^2 > 0 \) whenever \( f \ne 0 \), since some term is positive and none is negative. So \( \operatorname{Cl}(G) \) is a complex inner product space of dimension \( k \), and all of Chapter 11 is available in it.

When \( f \) and \( f' \) are class functions the sum can be shortened to one term per class: with \( c_j = \lvert C_j\rvert \) and \( g_j \in C_j \),
\[
  \inner{f}{f'} = \frac{1}{\lvert G\rvert}\sum_{j=1}^{k} c_j\, f(g_j)\,\conj{f'(g_j)} .
\]{#eq-class-inner-product}
That is the formula used for hand computation, and it is the only place the class sizes enter.

## Two averaging lemmas

Both proofs of orthogonality run through the same device as Maschke's theorem: average over \( G \), and the average is \( G \)-invariant. Here we also need its trace.

::: {#lem-average-projection}
[The average of a representation is the projection onto the fixed space]

Let \( \rho \) be a representation of a finite group \( G \) on a complex space \( V \), and set
\[
  V^{G} \coloneqq \{\v \in V : \rho(g)\v = \v \text{ for all } g \in G\},
  \qquad
  P \coloneqq \frac{1}{\lvert G\rvert}\sum_{g \in G}\rho(g) .
\]
Then \( V^{G} \) is a subspace, \( P \) is a projection with \( \im P = V^{G} \), and
\[
  \frac{1}{\lvert G\rvert}\sum_{g \in G}\chi_\rho(g) = \dim V^{G} .
\]
:::

::: {.proof}
\( V^G = \bigcap_{g \in G}\ker(\rho(g) - \id_V) \) is an intersection of subspaces, hence a subspace (@thm-intersection-subspaces).

Fix \( h \in G \). Then \( \rho(h)P = \tfrac1{\lvert G\rvert}\sum_g \rho(hg) = P \), because \( g \mapsto hg \) is a bijection of \( G \) (@thm-group-basic-properties) and so only reorders the terms. Hence \( \rho(h)(P\v) = P\v \) for every \( \v \), giving \( \im P \subseteq V^G \). Conversely, if \( \v \in V^G \) then \( P\v = \tfrac1{\lvert G\rvert}\sum_g \v = \v \). So \( P \) is the identity on \( V^G \); combined with \( \im P \subseteq V^G \) this gives \( P^2 = P \) and \( \im P = V^G \).

Thus \( P \) is a projection (@def-projection-operator) of rank \( \dim V^G \), and \( \tr P = \dim V^G \) by @thm-rank-equals-trace-projection, the field being \( \nC \). On the other hand the trace is linear (@thm-trace-operator-properties), so \( \tr P = \tfrac1{\lvert G\rvert}\sum_g \tr\rho(g) = \tfrac1{\lvert G\rvert}\sum_g \chi_\rho(g) \). This proves the lemma.
:::

::: {#lem-trace-of-sandwich}
[The trace of a two-sided multiplication]

Let \( V \) and \( W \) be finite-dimensional vector spaces over a field \( F \), let \( A \in \cL(V) \) and \( B \in \cL(W) \), and let
\[
  \Phi \colon \cL(V, W) \to \cL(V, W), \qquad \Phi(f) = B \circ f \circ A .
\]
Then \( \Phi \) is linear and \( \tr\Phi = (\tr A)(\tr B) \).
:::

::: {.idea}
Write everything in coordinates. In the basis of \( \cL(V, W) \) given by the matrix units \( \E_{ij} \), the map \( \X \mapsto \B\X\A \) sends \( \E_{ij} \) to a matrix whose \( (i, j) \)-entry is \( b_{ii}a_{jj} \); adding those diagonal coefficients factorizes as a product of two sums.
:::

::: {.proof}
Linearity of \( \Phi \) is immediate from bilinearity of composition. Fix bases of \( V \) and \( W \) and identify \( \cL(V, W) \) with \( M_{m\times n}(F) \), where \( n = \dim V \) and \( m = \dim W \) (@thm-linear-maps-isomorphic-to-matrices); let \( \A = (a_{jl}) \in M_n(F) \) and \( \B = (b_{ki}) \in M_m(F) \) be the matrices of \( A \) and \( B \). Under the identification \( \Phi \) becomes \( \X \mapsto \B\X\A \).

Let \( \E_{ij} \in M_{m \times n}(F) \) be the matrix unit with a \( 1 \) in position \( (i, j) \) and zeros elsewhere — the rectangular version of the matrix units of @lem-matrix-units; these \( mn \) matrices form a basis. By @def-matrix-multiplication,
\[
  (\B\,\E_{ij}\,\A)_{kl} = \sum_{p, q} b_{kp}(\E_{ij})_{pq}a_{ql} = b_{ki}\,a_{jl} .
\]
In the basis \( (\E_{ij}) \), the coefficient of \( \E_{ij} \) in \( \Phi(\E_{ij}) \) is the \( (i, j) \)-entry of \( \B\E_{ij}\A \), namely \( b_{ii}a_{jj} \). These coefficients are the diagonal entries of the matrix of \( \Phi \), so by @def-trace-operator,
\[
  \tr\Phi = \sum_{i=1}^{m}\sum_{j=1}^{n} b_{ii}a_{jj}
  = \Bigl(\sum_{i} b_{ii}\Bigr)\Bigl(\sum_{j} a_{jj}\Bigr) = (\tr\B)(\tr\A),
\]
and \( \tr\A = \tr A \), \( \tr\B = \tr B \) by @def-trace-operator. This proves the lemma.
:::

Now put the two together. Given representations \( \rho \) on \( V \) and \( \sigma \) on \( W \), make \( G \) act on the space \( \cL(V, W) \) of linear maps by
\[
  \pi(g)f \coloneqq \sigma(g)\circ f\circ\rho(g)^{-1} .
\]

::: {#prp-hom-representation}
[The representation on the space of linear maps]

Let \( \rho, \sigma \) be representations of a finite group \( G \) on complex spaces \( V, W \). Then \( \pi \) above is a representation of \( G \) on \( \cL(V, W) \), its character is \( \chi_\pi(g) = \chi_\sigma(g)\conj{\chi_\rho(g)} \), and its fixed space is the space
\[
  \cL_G(V, W) \coloneqq \{ f \in \cL(V, W) : f\rho(g) = \sigma(g)f \text{ for all } g \in G \}
\]
of maps intertwining \( \rho \) and \( \sigma \) (@def-equivalent-representations); for \( W = V \) and \( \sigma = \rho \) this is the commutant \( \End_{\nC[G]}(V) \) of @def-intertwining-map. Consequently
\[
  \frac{1}{\lvert G\rvert}\sum_{g \in G}\chi_\sigma(g)\conj{\chi_\rho(g)} = \dim \cL_G(V, W).
\]{#eq-intertwiner-count}
:::

::: {.proof}
*A representation.* Each \( \pi(g) \) is linear in \( f \), and \( \pi(g)\pi(h)f = \sigma(g)\sigma(h)f\rho(h)^{-1}\rho(g)^{-1} = \sigma(gh)f\rho(gh)^{-1} = \pi(gh)f \), using the homomorphism property of \( \rho \) and \( \sigma \) and @thm-group-basic-properties for the inverse of a product. Taking \( h = g^{-1} \) shows \( \pi(g) \) is invertible with inverse \( \pi(g^{-1}) \).

*Its character.* Apply @lem-trace-of-sandwich with \( A = \rho(g)^{-1} \) and \( B = \sigma(g) \):
\[
\begin{aligned}
  \chi_\pi(g) &= \tr\pi(g) = \tr\bigl(\rho(g)^{-1}\bigr)\,\tr\bigl(\sigma(g)\bigr) \\
  &= \chi_\rho(g^{-1})\chi_\sigma(g) = \conj{\chi_\rho(g)}\,\chi_\sigma(g),
\end{aligned}
\]
the last step by @prp-character-basic (e).

*Its fixed space.* \( \pi(g)f = f \) means \( \sigma(g)f\rho(g)^{-1} = f \), and composing with \( \rho(g) \) on the right turns this into \( \sigma(g)f = f\rho(g) \). So the fixed space is exactly \( \cL_G(V, W) \).

*The count.* Apply @lem-average-projection to \( \pi \) and substitute the character just computed. This proves the proposition.
:::

## Orthogonality of the irreducible characters

Everything is now in place. Schur's lemma converts the right-hand side of @eq-intertwiner-count into a \( 0 \) or a \( 1 \).

::: {#thm-character-orthogonality}
[Orthogonality of Irreducible Characters]

Let \( G \) be a finite group and let \( \rho \) on \( V \) and \( \sigma \) on \( W \) be **irreducible** complex representations of \( G \). Then
\[
  \inner{\chi_\sigma}{\chi_\rho} =
  \begin{cases}
    1, & \text{if } \rho \cong \sigma, \\
    0, & \text{if } \rho \not\cong \sigma .
  \end{cases}
\]
In particular the characters of pairwise inequivalent irreducible complex representations form an orthonormal list in \( \operatorname{Cl}(G) \).
:::

::: {.idea}
By @eq-intertwiner-count, \( \inner{\chi_\sigma}{\chi_\rho} \) counts the dimension of the space of intertwining maps \( V \to W \). Schur's lemma says that space is \( \{0\} \) when the two are inequivalent, because a non-zero intertwiner would be an isomorphism. When they are equivalent, fix one isomorphism \( S_0 \); every other intertwiner differs from it by an intertwiner of \( V \) with itself, which over \( \nC \) is a scalar. So the space is the line \( \nC S_0 \).
:::

::: {.proof}
By @eq-intertwiner-count, \( \inner{\chi_\sigma}{\chi_\rho} = \dim\cL_G(V, W) \), which is a non-negative integer. It remains to compute that dimension.

*Case 1: \( \rho \not\cong \sigma \).* By @thm-representations-are-modules-over-the-group-algebra, \( V \) and \( W \) are irreducible \( \nC[G] \)-spaces; and since the condition \( f\rho(g) = \sigma(g)f \) for all \( g \in G \) extends by linearity to all of \( \nC[G] \), the members of \( \cL_G(V, W) \) are exactly the \( \nC[G] \)-maps \( V \to W \) (@def-intertwining-map). Let \( f \in \cL_G(V, W) \) be non-zero. By @thm-schurs-lemma (a) it is an isomorphism, making \( \rho \) and \( \sigma \) equivalent (@def-equivalent-representations) — a contradiction. Hence \( \cL_G(V, W) = \{0\} \) and the inner product is \( 0 \).

*Case 2: \( \rho \cong \sigma \).* Fix an isomorphism \( S_0 \in \cL_G(V, W) \), so \( S_0\rho(g) = \sigma(g)S_0 \) for all \( g \). Applying \( S_0^{-1} \) on both sides gives \( \rho(g)S_0^{-1} = S_0^{-1}\sigma(g) \), so \( S_0^{-1} \) intertwines \( \sigma \) with \( \rho \). Let \( f \in \cL_G(V, W) \) and set \( u \coloneqq S_0^{-1}f \in \cL(V) \). Then for every \( g \),
\[
  u\rho(g) = S_0^{-1}f\rho(g) = S_0^{-1}\sigma(g)f = \rho(g)S_0^{-1}f = \rho(g)u ,
\]
so \( u \) commutes with every \( \rho(g) \). Since \( \rho \) is irreducible and the field is algebraically closed, @cor-commuting-with-irreducible gives \( u = \lambda\,\id_V \) for some \( \lambda \in \nC \), and hence \( f = S_0 u = \lambda S_0 \). Therefore \( \cL_G(V, W) = \nC S_0 \), which has dimension \( 1 \) because \( S_0 \ne 0 \).

The last sentence of the statement follows: distinct members of a list of pairwise inequivalent irreducibles pair to \( 0 \), and each pairs with itself to \( 1 \). This proves the theorem.
:::

Two consequences come for free, and both are used in every computation below.

::: {#cor-irreducibility-criterion}
[Irreducibility criterion]

Let \( \rho \) be a complex representation of a finite group \( G \) on \( V \ne \{\0\} \), with character \( \chi \). Write \( V = V_1 \oplus \dots \oplus V_r \) with each \( V_i \) irreducible (@cor-complete-reducibility), and let \( \chi_1, \dots, \chi_s \) be the distinct characters occurring among the \( \chi_{\rho|_{V_i}} \), with multiplicities \( m_1, \dots, m_s \ge 1 \). Then
\[
  \chi = \sum_{i=1}^{s} m_i\chi_i, \qquad m_i = \inner{\chi}{\chi_i}, \qquad
  \inner{\chi}{\chi} = \sum_{i=1}^{s} m_i^2 .
\]
In particular \( \inner{\chi}{\chi} = 1 \) if and only if \( \rho \) is irreducible, and two complex representations of \( G \) with the same character are equivalent.
:::

::: {.proof}
Repeated use of @prp-character-basic (d) gives \( \chi = \sum_{i=1}^{r}\chi_{\rho|_{V_i}} \), and grouping equal terms gives \( \chi = \sum_i m_i\chi_i \). Distinct characters come from inequivalent representations, since equivalent ones have equal characters (@prp-character-basic (c)); so by @thm-character-orthogonality the \( \chi_i \) are orthonormal, and \( \inner{\chi}{\chi_i} = m_i \) and, expanding the pairing in the first slot and then in the second, \( \inner{\chi}{\chi} = \sum_i m_i^2 \).

If \( \rho \) is irreducible then \( s = 1 \) and \( m_1 = 1 \), so \( \inner{\chi}{\chi} = 1 \). Conversely, a sum of squares of positive integers equals \( 1 \) only when there is a single term equal to \( 1 \); then \( r = 1 \) and \( V = V_1 \) is irreducible.

For the last claim, suppose \( \rho \) and \( \rho' \) have the same character. Every irreducible character \( \psi \) of \( G \) then has \( \inner{\chi_\rho}{\psi} = \inner{\chi_{\rho'}}{\psi} \), so each irreducible occurs with the same multiplicity in both decompositions. So the two decompositions into irreducibles use the same irreducibles with the same multiplicities, and the summands can be matched in pairs with equal characters. Two irreducible summands with equal characters are equivalent: were they inequivalent, @thm-character-orthogonality would make their characters orthogonal, hence unequal, since an irreducible character pairs with itself to \( 1 \) and not to \( 0 \). The direct sum of those equivalences is an isomorphism \( V \to V' \) intertwining \( \rho \) and \( \rho' \). This proves the corollary.
:::

::: {#exm-s3-standard-is-irreducible}
[Checking the standard representation by its character]

Use @cor-irreducibility-criterion to confirm that the two-dimensional representation of \( S_3 \) built in @exm-s3-irreducibles is irreducible, and decompose the permutation representation of \( S_3 \) on \( \nC^3 \).
:::

::: {.solution}
From @exm-s3-irreducibles the matrices give \( \chi_{\mathrm{std}}(\id) = 2 \), \( \chi_{\mathrm{std}}((1\ 2)) = -1 + 1 = 0 \) and \( \chi_{\mathrm{std}}((1\ 2\ 3)) = 0 + (-1) = -1 \); by @prp-character-basic (b) these three values determine \( \chi_{\mathrm{std}} \) on all of \( S_3 \), the classes being those of @exm-conjugacy-classes-s3. Using @eq-class-inner-product with class sizes \( 1, 3, 2 \),
\[
  \inner{\chi_{\mathrm{std}}}{\chi_{\mathrm{std}}}
  = \tfrac16\bigl(1\cdot 2^2 + 3\cdot 0^2 + 2\cdot(-1)^2\bigr)
  = \tfrac{4 + 0 + 2}{6} = 1,
\]
so the representation is irreducible.

For the permutation representation, \( \chi_{\mathrm{perm}} \) counts fixed points: \( 3 \) at \( \id \), \( 1 \) at a transposition, \( 0 \) at a \( 3 \)-cycle. Then
\[
\begin{aligned}
  \inner{\chi_{\mathrm{perm}}}{\chi_{\mathrm{triv}}} &= \tfrac16(1\cdot3 + 3\cdot1 + 2\cdot0) = 1, \\
  \inner{\chi_{\mathrm{perm}}}{\chi_{\mathrm{sgn}}} &= \tfrac16(1\cdot3 + 3\cdot1\cdot(-1) + 2\cdot0) = 0, \\
  \inner{\chi_{\mathrm{perm}}}{\chi_{\mathrm{std}}} &= \tfrac16(1\cdot3\cdot2 + 0 + 0) = 1 .
\end{aligned}
\]
So \( \chi_{\mathrm{perm}} = \chi_{\mathrm{triv}} + \chi_{\mathrm{std}} \), and by @cor-irreducibility-criterion the permutation representation is the direct sum of the trivial and the standard one. That matches the splitting \( \nC^3 = \Span(\e_1+\e_2+\e_3)\oplus W \) found by hand in @exm-s3-irreducibles, and it was found here without looking at a single vector.
:::

## The characters span the class functions

Orthonormality already bounds the number of irreducible representations: an orthonormal list in \( \operatorname{Cl}(G) \) is independent (@thm-orthogonal-independent), so there are at most \( k \) of them up to equivalence. The next theorem shows there are exactly \( k \). It is the deepest statement of the section, and its proof is the third and last averaging argument: this time we average the group elements themselves, weighted by a class function.

::: {#thm-characters-span-class-functions}
[The Irreducible Characters Are a Basis of the Class Functions]

Let \( G \) be a finite group with \( k \) conjugacy classes. Then \( G \) has exactly \( k \) irreducible complex representations up to equivalence, and their characters \( \chi_1, \dots, \chi_k \) form an orthonormal **basis** of \( \operatorname{Cl}(G) \).
:::

::: {.idea}
Suppose a class function \( f \) is orthogonal to every irreducible character; we must show \( f = 0 \). Build from \( f \) the operator \( T_f = \sum_g \conj{f(g)}\rho(g) \) on any representation \( \rho \). ① Because \( f \) is a class function, \( T_f \) commutes with every \( \rho(h) \) — conjugating by \( \rho(h) \) permutes the terms and leaves the coefficients alone. ② So on an irreducible \( \rho \) it is a scalar, and its trace, which is \( \lvert G\rvert\inner{\chi_\rho}{f} = 0 \), forces that scalar to be \( 0 \). ③ Complete reducibility (@cor-complete-reducibility) spreads this to every representation. ④ Apply it to the regular representation and evaluate at \( \delta_1 \): the result is \( \sum_g \conj{f(g)}\delta_g = 0 \), and the \( \delta_g \) are a basis.
:::

::: {.proof}
Orthonormal lists are independent (@thm-orthogonal-independent) and \( \dim\operatorname{Cl}(G) = k \) (@prp-dimension-class-functions), so by @thm-character-orthogonality any list of pairwise inequivalent irreducible representations has at most \( k \) members. Choose such a list \( \rho_1, \dots, \rho_s \) with \( s \) as large as possible; by maximality every irreducible complex representation of \( G \) is equivalent to some \( \rho_i \). Write \( \chi_i = \chi_{\rho_i} \), and let \( U = \Span(\chi_1, \dots, \chi_s) \subseteq \operatorname{Cl}(G) \), using @prp-character-basic (b).

Let \( f \in U^{\perp} \), the orthogonal complement of \( U \) in \( \operatorname{Cl}(G) \) (@def-orthogonal-complement), so \( f \) is a class function with \( \inner{f}{\chi_i} = 0 \), hence also \( \inner{\chi_i}{f} = \conj{\inner{f}{\chi_i}} = 0 \), for every \( i \). For **any** representation \( \rho \) of \( G \) on \( V \), define
\[
  T_f^{\rho} \coloneqq \sum_{g \in G}\conj{f(g)}\,\rho(g) \in \cL(V).
\]

::: {.claim}
**Claim 1.** \( T_f^\rho \) commutes with \( \rho(h) \) for every \( h \in G \).

::: {.proof}
Fix \( h \). Then
\[
  \rho(h)\,T_f^\rho\,\rho(h)^{-1} = \sum_{g \in G}\conj{f(g)}\,\rho(hgh^{-1}) .
\]
The map \( g \mapsto hgh^{-1} \) is a bijection \( G \to G \), with inverse \( g \mapsto h^{-1}gh \). Substituting \( g' = hgh^{-1} \), so that \( g = h^{-1}g'h \), the sum becomes \( \sum_{g'}\conj{f(h^{-1}g'h)}\rho(g') \). Since \( f \) is a class function, \( f(h^{-1}g'h) = f(g') \), so the sum is \( T_f^\rho \). Multiplying on the right by \( \rho(h) \) gives the claim.
:::
:::

::: {.claim}
**Claim 2.** If \( \rho \) is irreducible, then \( T_f^\rho = 0 \).

::: {.proof}
By Claim 1 and @cor-commuting-with-irreducible, over the algebraically closed field \( \nC \) we get \( T_f^\rho = \lambda\,\id_V \) for some \( \lambda \in \nC \). Taking traces and using linearity of the trace (@thm-trace-operator-properties),
\[
  \lambda\,\dim V = \tr T_f^\rho = \sum_{g}\conj{f(g)}\,\chi_\rho(g) = \lvert G\rvert\,\inner{\chi_\rho}{f} .
\]
Now \( \rho \) is equivalent to some \( \rho_i \), so \( \chi_\rho = \chi_i \) by @prp-character-basic (c), and \( \inner{\chi_i}{f} = 0 \). Since \( \dim V \ge 1 \), \( \lambda = 0 \).
:::
:::

::: {.claim}
**Claim 3.** \( T_f^\rho = 0 \) for **every** representation \( \rho \).

::: {.proof}
We may assume \( V \ne \{\0\} \). By @cor-complete-reducibility, \( V = V_1\oplus\dots\oplus V_r \) with each \( V_j \) invariant and \( \rho|_{V_j} \) irreducible. Each \( \rho(g) \) maps \( V_j \) into \( V_j \), hence so does \( T_f^\rho \), and its restriction to \( V_j \) is \( \sum_g \conj{f(g)}\,\rho|_{V_j}(g) = T_f^{\rho|_{V_j}} \), which is \( 0 \) by Claim 2. So \( T_f^\rho \) vanishes on each \( V_j \), hence on their sum \( V \).
:::
:::

Now apply Claim 3 to the regular representation \( \rho_{\mathrm{reg}} \) on \( \nC[G] \), where \( \rho_{\mathrm{reg}}(g)\delta_h = \delta_{gh} \). Evaluating at the basis vector \( \delta_1 \),
\[
  0 = T_f^{\rho_{\mathrm{reg}}}\delta_1 = \sum_{g \in G}\conj{f(g)}\,\delta_g .
\]
The \( \delta_g \) are a basis of \( \nC[G] \), so every coefficient vanishes: \( \conj{f(g)} = 0 \), that is \( f(g) = 0 \), for all \( g \). Hence \( U^{\perp} = \{0\} \).

By @thm-orthogonal-decomposition, \( \operatorname{Cl}(G) = U \oplus U^{\perp} = U \). So \( (\chi_1, \dots, \chi_s) \) is an orthonormal spanning list, hence a basis, and \( s = \dim\operatorname{Cl}(G) = k \) by @prp-dimension-class-functions. Finally, inequivalent irreducibles have different characters, since orthonormality gives \( \inner{\chi_i}{\chi_j} = 0 \ne 1 = \inner{\chi_i}{\chi_i} \) for \( i \ne j \); so the \( k \) characters correspond to the \( k \) equivalence classes of irreducible representations. This proves the theorem.
:::

::: {#cor-sum-of-squares}
[The sum of the squares of the degrees]

Let \( G \) be a finite group and let \( \rho_1, \dots, \rho_k \) on \( V_1, \dots, V_k \) be a complete list of pairwise inequivalent irreducible complex representations of \( G \), one for each of the \( k \) conjugacy classes (@thm-characters-span-class-functions). Then each \( \rho_i \) occurs in the regular representation with multiplicity exactly \( \dim V_i \), and
\[
  \lvert G\rvert = \sum_{i=1}^{k}(\dim V_i)^2 .
\]
:::

::: {.proof}
The regular character is \( \chi_{\mathrm{reg}}(1) = \lvert G\rvert \) and \( \chi_{\mathrm{reg}}(g) = 0 \) for \( g \ne 1 \), as computed after @def-character. Hence
\[
  \inner{\chi_{\mathrm{reg}}}{\chi_i}
  = \frac{1}{\lvert G\rvert}\sum_{g}\chi_{\mathrm{reg}}(g)\conj{\chi_i(g)}
  = \frac{1}{\lvert G\rvert}\,\lvert G\rvert\,\conj{\chi_i(1)} = \dim V_i,
\]
the value \( \chi_i(1) = \dim V_i \) being a real number (@prp-character-basic (a)). By @cor-irreducibility-criterion this inner product is the multiplicity of \( \rho_i \) in \( \rho_{\mathrm{reg}} \), so \( \chi_{\mathrm{reg}} = \sum_i (\dim V_i)\chi_i \). Evaluating at \( g = 1 \) gives \( \lvert G\rvert = \sum_i (\dim V_i)\chi_i(1) = \sum_i(\dim V_i)^2 \).
:::

This is @cor-dimension-count, the count \( \dim A = \sum n_i^2 \) of the structure theorem, applied to \( A = \nC[G] \): the two proofs are different and the answer is the same.

::: {#cor-column-orthogonality}
[Orthogonality of the columns]

Let \( G \) be a finite group with conjugacy classes \( C_1, \dots, C_k \), representatives \( g_j \in C_j \) and sizes \( c_j = \lvert C_j\rvert \), and irreducible characters \( \chi_1, \dots, \chi_k \). Then for all \( j, l \),
\[
  \sum_{i=1}^{k}\chi_i(g_j)\,\conj{\chi_i(g_l)} =
  \begin{cases}
    \lvert G\rvert / c_j, & j = l, \\
    0, & j \ne l .
  \end{cases}
\]
:::

::: {.idea}
@thm-characters-span-class-functions makes the table of character values a **square** array. Rescale it so that orthonormality of the rows says the matrix is unitary; then its columns are orthonormal too, because a one-sided inverse of a square matrix is two-sided.
:::

::: {.proof}
Let \( \U \in M_k(\nC) \) have entries \( u_{ij} = \sqrt{c_j/\lvert G\rvert}\ \chi_i(g_j) \); the square root is a positive real. By @eq-class-inner-product and @thm-character-orthogonality,
\[
  (\U\U^{*})_{i i'} = \sum_{j=1}^{k} u_{ij}\conj{u_{i'j}}
  = \frac{1}{\lvert G\rvert}\sum_{j=1}^{k} c_j\,\chi_i(g_j)\conj{\chi_{i'}(g_j)}
  = \inner{\chi_i}{\chi_{i'}},
\]
which is \( 1 \) for \( i = i' \) and \( 0 \) otherwise. Hence \( \U\U^{*} = \I_k \). By @thm-one-sided-inverse, \( \U^{*}\U = \I_k \) as well, so for all \( j, l \)
\[
  \sum_{i=1}^{k}\conj{u_{ij}}u_{il}
  = \frac{\sqrt{c_jc_l}}{\lvert G\rvert}\sum_{i=1}^{k}\conj{\chi_i(g_j)}\chi_i(g_l)
\]
equals \( 1 \) when \( j = l \) and \( 0 \) otherwise. For \( j = l \) this gives \( \sum_i \lvert\chi_i(g_j)\rvert^2 = \lvert G\rvert/c_j \), and for \( j \ne l \) it gives \( \sum_i \conj{\chi_i(g_j)}\chi_i(g_l) = 0 \). Conjugating the second identity, which is a sum of complex numbers, gives the stated form. This proves the corollary.
:::

## Two character tables

The **character table** of \( G \) is the \( k \times k \) array whose \( (i, j) \)-entry is \( \chi_i(g_j) \): one row per irreducible character, one column per conjugacy class. By @thm-characters-span-class-functions it is square, by @thm-character-orthogonality its rows are orthonormal, and by @cor-column-orthogonality its columns are orthogonal.

::: {#exm-character-table-s3}
[The character table of the symmetric group on three letters]

Write down the character table of \( S_3 \) and verify every orthogonality relation.
:::

::: {.solution}
By @exm-conjugacy-classes-s3 there are \( k = 3 \) classes, with representatives \( \id \), \( (1\ 2) \), \( (1\ 2\ 3) \) and sizes \( 1, 3, 2 \). So there are three irreducible complex representations (@thm-characters-span-class-functions), and @exm-s3-irreducibles produced three: the trivial, the sign and the standard one. Their characters, from the definitions and the traces computed in @exm-s3-standard-is-irreducible, are:

| | \( \id \) | \( (1\ 2) \) | \( (1\ 2\ 3) \) |
|---|---|---|---|
| class size | \( 1 \) | \( 3 \) | \( 2 \) |
| \( \chi_{\mathrm{triv}} \) | \( 1 \) | \( 1 \) | \( 1 \) |
| \( \chi_{\mathrm{sgn}} \) | \( 1 \) | \( -1 \) | \( 1 \) |
| \( \chi_{\mathrm{std}} \) | \( 2 \) | \( 0 \) | \( -1 \) |

*Degrees.* \( 1^2 + 1^2 + 2^2 = 6 = \lvert S_3\rvert \), as @cor-sum-of-squares requires.

*Row orthogonality*, from @eq-class-inner-product with weights \( 1, 3, 2 \) and divisor \( 6 \). All values are real, so conjugation does nothing:
\[
\begin{aligned}
  \inner{\chi_{\mathrm{triv}}}{\chi_{\mathrm{triv}}} &= \tfrac16(1 + 3 + 2) = 1, \\
  \inner{\chi_{\mathrm{sgn}}}{\chi_{\mathrm{sgn}}} &= \tfrac16(1 + 3 + 2) = 1, \\
  \inner{\chi_{\mathrm{std}}}{\chi_{\mathrm{std}}} &= \tfrac16(4 + 0 + 2) = 1, \\
  \inner{\chi_{\mathrm{triv}}}{\chi_{\mathrm{sgn}}} &= \tfrac16(1 - 3 + 2) = 0, \\
  \inner{\chi_{\mathrm{triv}}}{\chi_{\mathrm{std}}} &= \tfrac16(2 + 0 - 2) = 0, \\
  \inner{\chi_{\mathrm{sgn}}}{\chi_{\mathrm{std}}} &= \tfrac16(2 + 0 - 2) = 0 .
\end{aligned}
\]

*Column orthogonality*, from @cor-column-orthogonality, with no weights this time:
\[
\begin{aligned}
  \text{column } \id: &\quad 1 + 1 + 4 = 6 = 6/1, \\
  \text{column } (1\ 2): &\quad 1 + 1 + 0 = 2 = 6/3, \\
  \text{column } (1\ 2\ 3): &\quad 1 + 1 + 1 = 3 = 6/2, \\
  \id \text{ against } (1\ 2): &\quad 1\cdot1 + 1\cdot(-1) + 2\cdot 0 = 0, \\
  \id \text{ against } (1\ 2\ 3): &\quad 1 + 1 - 2 = 0, \\
  (1\ 2) \text{ against } (1\ 2\ 3): &\quad 1 - 1 + 0 = 0 .
\end{aligned}
\]
Every relation holds.
:::

::: {#exm-character-table-z4}
[The character table of a cyclic group of order four]

Write down the character table of \( \nZ/4\nZ \) and verify the orthogonality relations.
:::

::: {.solution}
The group is abelian, so every conjugacy class is a single element and \( k = 4 \). By @thm-characters-span-class-functions there are four irreducible complex representations, and @exm-cyclic-irreducibles produced four, all of degree \( 1 \): \( \chi_m([j]) = i^{jm} \), using \( \omega = e^{2\pi i/4} = i \). Their degrees satisfy \( 1^2+1^2+1^2+1^2 = 4 = \lvert G\rvert \).

| | \( [0] \) | \( [1] \) | \( [2] \) | \( [3] \) |
|---|---|---|---|---|
| \( \chi_0 \) | \( 1 \) | \( 1 \) | \( 1 \) | \( 1 \) |
| \( \chi_1 \) | \( 1 \) | \( i \) | \( -1 \) | \( -i \) |
| \( \chi_2 \) | \( 1 \) | \( -1 \) | \( 1 \) | \( -1 \) |
| \( \chi_3 \) | \( 1 \) | \( -i \) | \( -1 \) | \( i \) |

*Row orthogonality.* For characters of degree \( 1 \), \( \conj{\chi_l([j])} = i^{-jl} \), so
\[
  \inner{\chi_m}{\chi_l} = \frac14\sum_{j=0}^{3} i^{j(m-l)} .
\]
If \( m = l \) every term is \( 1 \) and the sum is \( 4/4 = 1 \). If \( m \ne l \), put \( d = m - l \), so \( i^{d} \ne 1 \) and \( (i^d)^4 = 1 \); then \( (i^d - 1)\sum_{j=0}^{3}(i^d)^j = (i^d)^4 - 1 = 0 \), and dividing by \( i^d - 1 \ne 0 \) gives \( \sum_j i^{jd} = 0 \). For instance \( \inner{\chi_1}{\chi_0} = \tfrac14(1 + i - 1 - i) = 0 \) and \( \inner{\chi_3}{\chi_1} = \tfrac14(1 - 1 + 1 - 1) = 0 \).

*Column orthogonality.* Every class has size \( 1 \), so @cor-column-orthogonality predicts \( 4 \) down the diagonal and \( 0 \) off it. The same geometric sum settles every one of them: column \( [j] \) against column \( [l] \) gives \( \sum_{m=0}^{3}\chi_m([j])\conj{\chi_m([l])} = \sum_{m=0}^{3} i^{m(j-l)} \), which is \( 4 \) when \( j = l \), and is \( 0 \) otherwise by the computation just made, read with \( d = j - l \). Three of them written out. Column \( [1] \) against itself: \( 1 + \lvert i\rvert^2 + 1 + \lvert -i\rvert^2 = 4 \). Column \( [0] \) against \( [2] \): the entries of column \( [0] \) are \( 1, 1, 1, 1 \) and those of column \( [2] \) are \( 1, -1, 1, -1 \), so the sum is \( 1\cdot 1 + 1\cdot(-1) + 1\cdot 1 + 1\cdot(-1) = 0 \). Column \( [1] \) against \( [3] \): \( 1 + i\cdot\conj{(-i)} + (-1)\conj{(-1)} + (-i)\conj{i} = 1 + i\cdot i + 1 + (-i)(-i) = 1 - 1 + 1 - 1 = 0 \).

Read as a matrix, the table is \( (i^{jm})_{m, j} \), which up to the factor \( 1/2 \) is the \( 4 \times 4 \) Fourier matrix of @exm-fourier-matrix-4. That is not a coincidence, and Section 09 explains it.
:::

::: {.warning}
**The character table does not determine the group.** Two non-isomorphic groups can have identical character tables. The standard witness is a pair of groups of order \( 8 \): the eight symmetries of a square (four rotations and four reflections), and the group \( \{\pm\I_2, \pm\i, \pm\j, \pm\k\} \) sitting inside the quaternions \( \nH \) of @def-quaternions under multiplication. Both have five conjugacy classes and degrees \( 1, 1, 1, 1, 2 \), and their tables agree entry for entry, yet the groups are not isomorphic. **This is stated on credit and not proved here**; nothing below depends on it. What the character table *does* determine is every complex representation of the group, up to equivalence (@cor-irreducibility-criterion).
:::

## Exercises

### A. Check your understanding

::: {#exr-characters-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the character of a representation, and state why it does not depend on a choice of basis.
2. State the orthogonality relation for irreducible complex characters.
3. Determine whether the following is true: "if \( \chi \) is a character of \( G \) then \( \chi(gh) = \chi(g)\chi(h) \)." Justify your answer.
4. A group of order \( 12 \) has exactly four conjugacy classes. Determine the degrees of its irreducible complex representations.
5. Explain why the number of irreducible complex representations of an abelian group \( G \) is \( \lvert G\rvert \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. \( \chi_\rho(g) = \tr\rho(g) \) (@def-character). The trace of an operator is computed from its matrix in any basis and the answer is the same for all of them (@def-trace-operator), so \( \chi_\rho \) depends only on \( \rho \).
2. For irreducible complex representations \( \rho, \sigma \) of a finite group, \( \inner{\chi_\sigma}{\chi_\rho} \) is \( 1 \) if \( \rho \cong \sigma \) and \( 0 \) otherwise (@thm-character-orthogonality).
3. False. See the warning after @prp-character-basic: for the standard representation of \( S_3 \), \( \chi((1\ 2))\chi((1\ 3)) = 0 \) but \( \chi((1\ 3\ 2)) = -1 \). It is true precisely for characters of degree \( 1 \).
4. Four classes means four irreducible representations (@thm-characters-span-class-functions), with degrees \( d_1, \dots, d_4 \ge 1 \) satisfying \( d_1^2 + d_2^2 + d_3^2 + d_4^2 = 12 \) (@cor-sum-of-squares). Every group has the trivial representation, so we may take \( d_1 = 1 \) and need \( d_2^2+d_3^2+d_4^2 = 11 \) with each \( d_i \ge 1 \). The squares available are \( 1, 4, 9 \), since \( 4^2 = 16 > 11 \). A triple containing a \( 9 \) has its other two terms summing to \( 2 \), so it is \( 9 + 1 + 1 = 11 \), which works; and a triple with no \( 9 \) is one of \( 4+4+4 = 12 \), \( 4+4+1 = 9 \), \( 4+1+1 = 6 \) and \( 1+1+1 = 3 \), none of them \( 11 \). So the degrees are \( 1, 1, 1, 3 \).
5. In an abelian group \( xgx^{-1} = g \), so every conjugacy class is a singleton and \( k = \lvert G\rvert \); now apply @thm-characters-span-class-functions.
:::
:::

### B. Practice

::: {#exr-characters-b1}
[B1: A character computed and decomposed]

Let \( \P_\tau \) be the permutation matrix of \( \tau \in S_3 \), so that \( \P_\tau\e_i = \e_{\tau(i)} \) (@def-permutation-matrix), and let \( \pi \) be the representation of \( S_3 \) on \( \cL(\nC^3) \) given by \( \pi(\tau)(f) = \P_\tau\, f\, \P_\tau^{-1} \).

::: {.enumerate options="label=(\alph*)"}
1. Compute the character of \( \pi \) on the three conjugacy classes.
2. Decompose \( \pi \) into irreducibles.
:::
:::

::: {.solution}
(a) This is the construction of @prp-hom-representation with both representations equal to the permutation representation \( \rho_{\mathrm{perm}} \) on \( \nC^3 \). So its character is \( \chi_\pi(\tau) = \chi_{\mathrm{perm}}(\tau)\conj{\chi_{\mathrm{perm}}(\tau)} = \lvert\chi_{\mathrm{perm}}(\tau)\rvert^2 \). From @exm-s3-standard-is-irreducible, \( \chi_{\mathrm{perm}} = (3, 1, 0) \) on the classes of \( \id \), \( (1\ 2) \), \( (1\ 2\ 3) \), so \( \chi_\pi = (9, 1, 0) \).

(b) With weights \( 1, 3, 2 \) and divisor \( 6 \):
\[
\begin{aligned}
  \inner{\chi_\pi}{\chi_{\mathrm{triv}}} &= \tfrac16(9 + 3 + 0) = 2, \\
  \inner{\chi_\pi}{\chi_{\mathrm{sgn}}} &= \tfrac16(9 - 3 + 0) = 1, \\
  \inner{\chi_\pi}{\chi_{\mathrm{std}}} &= \tfrac16(9\cdot2 + 0 + 0) = 3 .
\end{aligned}
\]
So \( \chi_\pi = 2\chi_{\mathrm{triv}} + \chi_{\mathrm{sgn}} + 3\chi_{\mathrm{std}} \), and the degrees check: \( 2 + 1 + 6 = 9 = \dim\cL(\nC^3) \). As a check on the arithmetic, \( \inner{\chi_\pi}{\chi_\pi} = \tfrac16(81 + 3 + 0) = 14 = 2^2+1^2+3^2 \), as @cor-irreducibility-criterion requires. In particular \( \dim\cL_G(\nC^3, \nC^3) = 2 \): the \( G \)-equivariant operators on \( \nC^3 \) form a plane, spanned by the identity and the all-ones matrix.
:::

::: {#exr-characters-b2}
[B2: Which of these are characters?]

Let \( G = S_3 \), with classes ordered \( \id \), \( (1\ 2) \), \( (1\ 2\ 3) \) of sizes \( 1, 3, 2 \). Determine which of the following class functions are characters of complex representations of \( S_3 \). Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( (4, 0, 1) \);
2. \( (3, 1, 0) \);
3. \( (2, 2, -1) \);
4. \( (1, 1, -1) \).
:::
:::

::: {.solution}
A class function is a character exactly when it is a **non-negative integer** combination of \( \chi_{\mathrm{triv}} = (1,1,1) \), \( \chi_{\mathrm{sgn}} = (1,-1,1) \) and \( \chi_{\mathrm{std}} = (2,0,-1) \), by @cor-complete-reducibility and @prp-character-basic (d); the coefficients are the inner products \( \inner{\cdot}{\chi_i} \).

(a) \( \inner{(4,0,1)}{\chi_{\mathrm{triv}}} = \tfrac16(4 + 0 + 2) = 1 \), \( \inner{\cdot}{\chi_{\mathrm{sgn}}} = \tfrac16(4 - 0 + 2) = 1 \), \( \inner{\cdot}{\chi_{\mathrm{std}}} = \tfrac16(8 + 0 - 2) = 1 \). All non-negative integers, and \( 1\cdot1+1\cdot1+1\cdot2 = 4 \) matches the degree. **Yes**: it is the character of the direct sum of the trivial, the sign and the standard representation, equivalently of the direct sum of the permutation representation and the sign representation, since \( (3,1,0) + (1,-1,1) = (4,0,1) \).

(b) Inner products \( 1, 0, 1 \) as computed in @exm-s3-standard-is-irreducible. **Yes**: the permutation representation.

(c) \( \inner{\cdot}{\chi_{\mathrm{triv}}} = \tfrac16(2 + 6 - 2) = 1 \), \( \inner{\cdot}{\chi_{\mathrm{sgn}}} = \tfrac16(2 - 6 - 2) = -1 \). A negative multiplicity is impossible, so **no**. (It is a difference of characters, called a virtual character, but not a character.)

(d) \( \inner{(1,1,-1)}{\chi_{\mathrm{triv}}} = \tfrac16(1 + 3 - 2) = \tfrac13 \), which is not an integer. So **no**: it is not even a combination of the three irreducible characters with integer coefficients, let alone non-negative ones.
:::

::: {#exr-characters-b3}
[B3: Degree-one characters of a cyclic group]

Let \( G = \nZ/6\nZ \).

::: {.enumerate options="label=(\alph*)"}
1. Write down the character table.
2. Verify \( \inner{\chi_1}{\chi_4} = 0 \) and \( \inner{\chi_2}{\chi_2} = 1 \) by direct computation.
:::
:::

::: {.solution}
(a) The group is abelian of order \( 6 \), so there are six classes, six irreducible characters, all of degree \( 1 \), given by \( \chi_m([j]) = \omega^{jm} \) with \( \omega = e^{2\pi i/6} \) (@exm-cyclic-irreducibles). The table has \( (m, j) \)-entry \( \omega^{jm} \), with \( \omega^6 = 1 \).

(b) Here
\[
\begin{aligned}
\inner{\chi_1}{\chi_4} &= \tfrac16\sum_{j=0}^{5}\omega^{j}\conj{\omega^{4j}} = \tfrac16\sum_j \omega^{-3j} \\
&= \tfrac16\sum_j(-1)^{j} = \tfrac16(1-1+1-1+1-1) = 0 ,
\end{aligned}
\]
using \( \omega^{-3} = \omega^{3} = -1 \). And \( \inner{\chi_2}{\chi_2} = \tfrac16\sum_j \omega^{2j}\conj{\omega^{2j}} = \tfrac16\sum_j \lvert\omega^{2j}\rvert^2 = \tfrac16\cdot 6 = 1 \).
:::

### C. Going deeper

::: {#exr-characters-c1}
[C1: Counting fixed points]

Let \( G \) be a finite group acting on \( \{1, \dots, n\} \) through a homomorphism \( \varphi \colon G \to S_n \), and let \( \rho(g) = \P_{\varphi(g)} \) be the corresponding permutation representation on \( \nC^n \), where \( \P_\sigma \) is the permutation matrix of @def-permutation-matrix (so \( \P_\sigma\P_\tau = \P_{\sigma\tau} \) by @lem-permutation-matrices (a)).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \inner{\chi_\rho}{\chi_{\mathrm{triv}}} \) equals the average number of fixed points of the permutations \( \varphi(g) \), and also equals \( \dim (\nC^n)^{G} \).
2. Deduce that for every \( n \ge 1 \), the average number of fixed points of a permutation in \( S_n \) is exactly \( 1 \).
3. For \( G = S_3 \) with \( \varphi = \id \), verify (a) numerically.
:::
:::

::: {.solution}
(a) By the computation after @def-character, \( \chi_\rho(g) \) is the number of \( i \) with \( \varphi(g)(i) = i \). Hence
\[
  \inner{\chi_\rho}{\chi_{\mathrm{triv}}} = \frac{1}{\lvert G\rvert}\sum_{g}\chi_\rho(g)\cdot\conj{1}
\]
is exactly the average of those counts. By @lem-average-projection applied to \( \rho \), the same quantity is \( \dim(\nC^n)^G \).

(b) Take \( G = S_n \) and \( \varphi = \id \). A vector \( \x \in \nC^n \) fixed by every \( \rho(\tau) \) has \( x_i = x_j \) for all \( i \ne j \), by taking \( \tau \) the transposition \( (i\ j) \); conversely every vector with equal coordinates is fixed. So \( (\nC^n)^{S_n} = \Span(\e_1 + \dots + \e_n) \), of dimension \( 1 \) (for \( n = 1 \) this is \( \nC \) itself). By (a) the average number of fixed points equals that dimension, namely \( 1 \).

(c) For \( S_3 \), \( \chi_\rho = (3, 1, 0) \) on classes of sizes \( 1, 3, 2 \), so the average number of fixed points is \( \tfrac16(1\cdot3 + 3\cdot1 + 2\cdot0) = 1 \). Directly: \( \id \) fixes three points, each of the three transpositions fixes one, and each of the two \( 3 \)-cycles fixes none, giving \( (3 + 3 + 0)/6 = 1 \). And \( \dim(\nC^3)^{S_3} = 1 \) by (b). The three agree.
:::

::: {#exr-characters-c2}
[C2: Degree-one characters form a group]

Let \( G \) be a finite group and let \( X(G) \) be the set of characters of degree \( 1 \) of complex representations of \( G \). (For abelian \( G \) this group is the subject of Section 09.)

::: {.enumerate options="label=(\alph*)"}
1. Prove that the pointwise product of two degree-one characters is a degree-one character, and that \( X(G) \) is a group under this product.
2. Prove that \( \lvert X(G)\rvert \le k \), the number of conjugacy classes, with equality if and only if \( G \) is abelian. *Hint: use @cor-sum-of-squares in one direction and @cor-abelian-irreducibles-are-lines in the other.*
:::
:::

::: {.solution}
(a) A degree-one character is a homomorphism \( \chi \colon G \to \nC\setminus\{0\} \) (the representation *is* the scalar it multiplies by). If \( \chi, \psi \) are two of them then \( (\chi\psi)(gh) = \chi(gh)\psi(gh) = \chi(g)\psi(g)\chi(h)\psi(h) = (\chi\psi)(g)(\chi\psi)(h) \), using commutativity of \( \nC \); so \( \chi\psi \) is again a homomorphism into \( \nC\setminus\{0\} \), hence a degree-one character. The product is associative because multiplication in \( \nC \) is; \( \chi_{\mathrm{triv}} \) is an identity; and \( g \mapsto \chi(g)^{-1} \) is a homomorphism and satisfies \( \chi \cdot \chi^{-1} = \chi_{\mathrm{triv}} \). So \( X(G) \) is a group (@def-group).

(b) Degree-one characters are irreducible (a one-dimensional representation has no non-trivial invariant subspace) and pairwise distinct elements of \( X(G) \) are inequivalent representations, since for degree one, equivalence means equality. So \( X(G) \) is a subset of the \( k \) irreducible characters (@thm-characters-span-class-functions) and \( \lvert X(G)\rvert \le k \).

Equality says every irreducible character has degree \( 1 \). If \( G \) is abelian then \( \nC[G] \) is a commutative algebra, so every irreducible \( \nC[G] \)-space is one-dimensional by @cor-abelian-irreducibles-are-lines; by @thm-representations-are-modules-over-the-group-algebra those are exactly the irreducible representations of \( G \). Conversely, if every irreducible has degree \( 1 \) then \( \lvert G\rvert = \sum_{i=1}^{k}1 = k \) by @cor-sum-of-squares, so every conjugacy class is a singleton; that is, \( xgx^{-1} = g \) for all \( x, g \), which says \( G \) is abelian.
:::

::: {#exr-characters-c3}
[C3: The second orthogonality relation]

Let \( G \) be a finite group with irreducible complex characters \( \chi_1, \dots, \chi_k \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \sum_{i=1}^{k}\lvert\chi_i(g)\rvert^2 = \lvert G\rvert/\lvert C(g)\rvert \) for every \( g \in G \).
2. Deduce that \( \sum_{i}\lvert\chi_i(g)\rvert^2 = 1 \) if and only if the class of \( g \) is all of \( G \), and that this happens only for the trivial group. *Hint: \( C(1) = \{1\} \) always.*
3. For \( G = S_3 \) compute \( \sum_i \lvert\chi_i(g)\rvert^2 \) at each of the three classes and check (a).
:::
:::

::: {.solution}
(a) This is the diagonal case \( j = l \) of @cor-column-orthogonality, with \( g = g_j \) a representative of its own class and \( c_j = \lvert C(g)\rvert \). The value is independent of the representative chosen, as it must be, since characters are class functions.

(b) By (a), the sum equals \( 1 \) exactly when \( \lvert C(g)\rvert = \lvert G\rvert \), that is, when the class of \( g \) is all of \( G \). But \( C(1) = \{1\} \), and the classes partition \( G \), so a class equal to \( G \) forces \( G = \{1\} \). Conversely for the trivial group the only class is \( \{1\} = G \) and the single character has \( \lvert\chi_1(1)\rvert^2 = 1 \).

(c) From @exm-character-table-s3: at \( \id \), \( 1 + 1 + 4 = 6 = 6/1 \); at \( (1\ 2) \), \( 1 + 1 + 0 = 2 = 6/3 \); at \( (1\ 2\ 3) \), \( 1 + 1 + 1 = 3 = 6/2 \). Each matches \( \lvert G\rvert/\lvert C(g)\rvert \) with class sizes \( 1, 3, 2 \).
:::
