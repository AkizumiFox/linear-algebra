# Annihilators

Section 1 built the dual space \( V^{*} \), the space of linear measurements on \( V \). Now we connect subspaces of \( V \) with subspaces of \( V^{*} \). A plane in \( \nR^3 \) can be described by a spanning list or by an equation, and an equation is a functional. This section collects all the equations that a set of vectors satisfies into one subspace of \( V^{*} \), the annihilator, counts its dimension, and shows that it turns sums into intersections and intersections into sums.

## The equations a subspace satisfies

Every object comes with its subobjects. The dual space \( V^{*} \) has subspaces of its own, and the question is which of them are attached to subspaces of \( V \). The standard example shows the way.

Let \( U = \Span((1, 0, 1), (0, 1, 1)) \), a plane in \( \nR^3 \). The functional \( \varphi(x, y, z) = x + y - z \) vanishes on both spanning vectors, so by linearity it vanishes on all of \( U \): the plane satisfies the equation \( x + y - z = 0 \). So do \( 2x + 2y - 2z = 0 \) and the trivial equation \( 0 = 0 \). Which functionals vanish on \( U \)? By @thm-functionals-on-fn a functional is \( \psi(x, y, z) = ax + by + cz \). It vanishes on the two spanning vectors if and only if \( a + c = 0 \) and \( b + c = 0 \), that is, \( \psi = -c(x + y - z) = -c\,\varphi \). So the equations of the plane form the **line** \( \Span(\varphi) \) in \( (\nR^3)^{*} \).

For the \( z \)-axis \( \Span((0, 0, 1)) \), the same computation gives \( c = 0 \): the equations are \( ax + by = 0 \), a **plane** in \( (\nR^3)^{*} \). A bigger subspace satisfies fewer equations, and in both cases the dimensions add up to \( 3 \). The set of equations deserves a name, and the pattern deserves a theorem.

*The annihilator of a set of vectors is the space of all linear equations that every one of those vectors satisfies.*

::: {#def-annihilator}
[Annihilator]

Let \( V \) be a vector space over \( F \), and let \( S \subseteq V \) be **any subset**. The **annihilator** of \( S \) is
\[
S^{0} \coloneqq \{ \varphi \in V^{*} : \varphi(\s) = 0 \text{ for all } \s \in S \}.
\]
:::

In words: \( S^{0} \) is a subset of the **dual space** \( V^{*} \), not of \( V \). A functional belongs to it when it vanishes at **every** vector of \( S \); a single non-zero value disqualifies it. The set \( S \) needs no structure: it may be a subspace, a finite list of vectors, or even empty. The superscript \( 0 \) recalls the value that the functionals take on \( S \).

**Well-definedness.** The definition makes sense for every subset. What needs checking is that the result is a subspace, which is what makes its dimension meaningful.

::: {#prp-annihilator-subspace}
[The Annihilator Is a Subspace]

Let \( V \) be a vector space over \( F \), and let \( S \subseteq V \). Then \( S^{0} \) is a subspace of \( V^{*} \).
:::

::: {.proof}
We use the subspace test (@thm-subspace-test) in \( V^{*} \). The zero functional sends every \( \s \in S \) to \( 0 \), so it lies in \( S^{0} \). Let \( \varphi, \psi \in S^{0} \) and \( c \in F \). For every \( \s \in S \), the pointwise operations of @def-dual-space give
\[
(\varphi + \psi)(\s) = \varphi(\s) + \psi(\s) = 0 + 0 = 0, \qquad (c\varphi)(\s) = c\,\varphi(\s) = c \cdot 0 = 0 .
\]
Hence \( \varphi + \psi \in S^{0} \) and \( c\varphi \in S^{0} \), and \( S^{0} \) is a subspace of \( V^{*} \).
:::

:::: {#exm-annihilators}
[First Annihilators]

::: {.enumerate options="label=(\alph*)"}
1. For any vector space \( V \), find \( \{\0\}^{0} \), \( \varnothing^{0} \) and \( V^{0} \).
2. In \( M_2(F) \), find the annihilator of the single matrix \( E_{11} \).
3. In \( \nR[x]_{\le 2} \), find the annihilator of \( S = \{1, x\} \).
:::
::::

::: {.solution}
(a) Every functional sends \( \0 \) to \( 0 \) (@thm-zero-maps-to-zero), so \( \{\0\}^{0} = V^{*} \). The condition "for all \( \s \in \varnothing \)" holds vacuously, so \( \varnothing^{0} = V^{*} \). A functional in \( V^{0} \) takes the value \( 0 \) at every vector, so it is the zero functional, and \( V^{0} = \{0\} \). These degenerate cases fix the direction of everything that follows: the smallest subspace of \( V \) has the largest annihilator, and the largest has the smallest.

(b) Let \( \varepsilon_{ij}(A) = a_{ij} \) be the dual basis of the standard basis \( (E_{11}, E_{12}, E_{21}, E_{22}) \). By @thm-dual-basis (c), every \( \psi \in M_2(F)^{*} \) is \( \psi = \sum_{i,j} \psi(E_{ij})\,\varepsilon_{ij} \). Such a \( \psi \) lies in \( \{E_{11}\}^{0} \) exactly when \( \psi(E_{11}) = 0 \). Hence
\[
\{E_{11}\}^{0} = \Span(\varepsilon_{12}, \varepsilon_{21}, \varepsilon_{22}) ,
\]
the functionals \( A \mapsto c_{12}a_{12} + c_{21}a_{21} + c_{22}a_{22} \). It has dimension \( 3 \), and \( 3 + 1 = 4 = \dim M_2(F) \).

(c) Let \( (\varphi_0, \varphi_1, \varphi_2) \) be the dual basis of \( (1, x, x^2) \), so \( \varphi_k \) reads off the coefficient of \( x^k \). A functional \( \psi = \psi(1)\varphi_0 + \psi(x)\varphi_1 + \psi(x^2)\varphi_2 \) lies in \( S^{0} \) exactly when \( \psi(1) = \psi(x) = 0 \), that is, when \( \psi = \psi(x^2)\varphi_2 \). So \( S^{0} = \Span(\varphi_2) \): the only equations satisfied by both \( 1 \) and \( x \) are the multiples of "the coefficient of \( x^2 \) is \( 0 \)".
:::

**Non-example by minimal change.** Shift the plane of the opening example off the origin: \( A = \{ (x, y, z) \in \nR^3 : x + y - z = 1 \} \). The set is still cut out by the same left-hand side, but \( \varphi(x, y, z) = x + y - z \) takes the value \( 1 \), not \( 0 \), on \( A \), so the defining clause \( \varphi(\s) = 0 \) fails and \( \varphi \notin A^{0} \). In fact \( A^{0} = \{0\} \): the set \( A \) contains \( (1, 0, 0) \), \( (0, 1, 0) \) and \( (0, 0, -1) \), and a functional \( ax + by + cz \) vanishing at these three vectors has \( a = b = c = 0 \). Annihilators record only **homogeneous** equations.

**Why this definition.** We allow any subset \( S \), not only subspaces, because subspaces are usually handed to us by spanning lists, and we want to test a functional on the list alone. The theorem at the end of this section shows that this loses nothing: \( S^{0} = (\Span S)^{0} \). The name is literal. To annihilate is to reduce to nothing, and the functionals in \( S^{0} \) reduce every vector of \( S \) to \( 0 \).

::: {.warning}
**\( U^{0} \) lives in \( V^{*} \), and it is not a complement of \( U \).** It is tempting to turn the functional \( ax + by \) into the vector \( (a, b) \) and to picture \( U^{0} \) as a subspace of \( F^2 \) "perpendicular" to \( U \). Over \( \nF_2 \) this picture fails completely. Let \( U = \Span((1, 1)) \subseteq \nF_2^2 \). A functional \( ax + by \) vanishes on \( (1, 1) \) exactly when \( a + b = 0 \), that is, \( a = b \), so \( U^{0} = \{0,\ x + y\} \). The functional \( x + y \) corresponds to the vector \( (1, 1) \), which lies **in** \( U \). So the "picture" of \( U^{0} \) is \( U \) itself, not a complement. Perpendicularity needs an inner product, which is the orthogonal complement of Chapter 10; the annihilator needs nothing.
:::

The payoff of the definition is the pattern we saw in the opening example. The equations of a subspace take up exactly the dimensions that the subspace leaves free.

## Counting equations

::: {#thm-dimension-annihilator}
[Dimension of the Annihilator]

Let \( V \) be a finite-dimensional vector space over \( F \), and let \( U \) be a subspace of \( V \). Then
\[
\dim U + \dim U^{0} = \dim V .
\]
More precisely, if \( (\u_1, \dots, \u_m, \v_{m+1}, \dots, \v_n) \) is a basis of \( V \) extending a basis \( (\u_1, \dots, \u_m) \) of \( U \), with dual basis \( (\varphi_1, \dots, \varphi_n) \), then \( (\varphi_{m+1}, \dots, \varphi_n) \) is a basis of \( U^{0} \).
:::

::: {.idea}
This is a dimension formula, so we start from the smallest subspace, \( U \), take a basis and extend it to \( V \). The dual basis now splits in two. The last \( n - m \) functionals vanish on every \( \u_i \), by the delta, so they vanish on \( U \). The first \( m \) do not. To see that nothing else is in \( U^{0} \), expand a functional \( \psi \in U^{0} \) in the dual basis: its coefficients are its values on the basis, and the first \( m \) values are \( \psi(\u_i) = 0 \).
:::

::: {.proof}
Since \( U \) is a subspace of the finite-dimensional space \( V \), it has a basis \( (\u_1, \dots, \u_m) \) (@thm-subspace-dimension, @cor-basis-existence), and by the Basis Extension Theorem (@thm-basis-extension) it extends to a basis \( \sB = (\u_1, \dots, \u_m, \v_{m+1}, \dots, \v_n) \) of \( V \), where \( n = \dim V \). Let \( (\varphi_1, \dots, \varphi_n) \) be the dual basis of \( \sB \) (@thm-dual-basis).

*The \( \varphi_j \) with \( j > m \) lie in \( U^{0} \).* Let \( j > m \) and \( \u \in U \), say \( \u = a_1\u_1 + \dots + a_m\u_m \). By @thm-linear-combination, \( \varphi_j(\u) = \sum_{i=1}^{m} a_i\varphi_j(\u_i) = 0 \), since \( \varphi_j(\u_i) = \delta_{ji} = 0 \) for \( i \le m < j \).

*They span \( U^{0} \).* Let \( \psi \in U^{0} \). By @thm-dual-basis (c),
\[
\psi = \sum_{i=1}^{m} \psi(\u_i)\,\varphi_i + \sum_{j=m+1}^{n} \psi(\v_j)\,\varphi_j = \sum_{j=m+1}^{n} \psi(\v_j)\,\varphi_j ,
\]
because \( \psi(\u_i) = 0 \) for \( \u_i \in U \). Hence \( U^{0} \subseteq \Span(\varphi_{m+1}, \dots, \varphi_n) \), and the reverse inclusion holds because \( U^{0} \) is a subspace (@prp-annihilator-subspace, @thm-span-subspace).

*They are independent,* being part of the basis \( (\varphi_1, \dots, \varphi_n) \) of \( V^{*} \). Therefore \( (\varphi_{m+1}, \dots, \varphi_n) \) is a basis of \( U^{0} \), and \( \dim U^{0} = n - m = \dim V - \dim U \). This proves the theorem.
:::

Alternatively, restrict functionals to \( U \). The map \( R \colon V^{*} \to U^{*} \), \( \varphi \mapsto \varphi|_U \), is linear, and its kernel is \( U^{0} \) by definition. It is surjective: given \( \xi \in U^{*} \), @thm-linear-transform-basis gives \( \varphi \in V^{*} \) with \( \varphi(\u_i) = \xi(\u_i) \) and \( \varphi(\v_j) = 0 \), and then \( \varphi|_U = \xi \) because both agree on a basis of \( U \). By the Rank–Nullity Theorem (@thm-rank-nullity) and @cor-dimension-dual-space, \( \dim V = \dim V^{*} = \dim U^{0} + \dim U^{*} = \dim U^{0} + \dim U \). This route shows **why** the formula holds: a functional on \( V \) is a functional on \( U \) plus a choice of values off \( U \), and \( U^{0} \) measures that choice.

The theorem is the second signature move of the chapter: **pass to the dual and count.** One immediate consequence: if \( U \) is a **proper** subspace of a finite-dimensional \( V \), then \( \dim U^{0} > 0 \), so some **non-zero** functional vanishes on \( U \). Equivalently, a list spans a finite-dimensional \( V \) if and only if the only functional that kills every vector of the list is \( 0 \): apply the previous sentence to the span \( U \) of the list, and note that a functional kills every vector of the list exactly when it kills \( U \), by @thm-linear-combination.

In \( F^n \) the whole computation becomes elimination, because functionals are rows.

:::: {#exm-annihilator-via-null-space}
[An Annihilator as a Null Space]

Find a basis of \( U^{0} \) for \( U = \Span((1, 2, 0), (0, 1, 1)) \subseteq \nR^3 \), and check the dimension formula.
::::

::: {.solution}
By @thm-functionals-on-fn, every functional is \( \varphi_{\a}(\x) = \a\tp\x \) for a unique \( \a = (a_1, a_2, a_3) \). By linearity, \( \varphi_{\a} \) vanishes on \( U \) if and only if it vanishes on the two spanning vectors (a combination of vectors killed by \( \varphi_{\a} \) is killed, by @thm-linear-combination). These two conditions are
\[
a_1 + 2a_2 = 0, \qquad a_2 + a_3 = 0, \qquad \text{that is,} \qquad A\a = \0 \quad \text{with} \quad A = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \end{pmatrix},
\]
the matrix whose **rows** are the spanning vectors. So \( \varphi_{\a} \in U^{0} \) if and only if \( \a \in \nul(A) \). Subtracting twice row 2 from row 1 gives the RREF
\[
\begin{pmatrix} 1 & 0 & -2 \\ 0 & 1 & 1 \end{pmatrix},
\]
with \( a_3 \) free. By @thm-basis-null-space, \( \nul(A) = \Span((2, -1, 1)) \). Hence \( U^{0} = \Span(\psi) \) with
\[
\psi(x, y, z) = 2x - y + z .
\]
Check: \( \psi(1, 2, 0) = 2 - 2 + 0 = 0 \) and \( \psi(0, 1, 1) = -1 + 1 = 0 \). The two spanning vectors are independent (neither is a multiple of the other), so \( \dim U = 2 \), and \( \dim U + \dim U^{0} = 2 + 1 = 3 \), as @thm-dimension-annihilator predicts. As a by-product, \( U \) is the plane \( 2x - y + z = 0 \): \( U \subseteq \ker\psi \), both have dimension \( 2 \) (@prp-nonzero-functional-surjective), and @thm-dim-impl-eq gives equality.

The same recipe works in general. For \( U = \Span(\u_1, \dots, \u_m) \subseteq F^n \), let \( A \) have rows \( \u_1\tp, \dots, \u_m\tp \). Then \( U^{0} = \{ \varphi_{\a} : \a \in \nul(A) \} \), and the isomorphism of @thm-functionals-on-fn carries a basis of \( \nul(A) \) to a basis of \( U^{0} \).
:::

Away from \( F^n \), counting often replaces the computation entirely.

:::: {#exm-annihilator-of-evaluation-kernel}
[The Equations of a Root Condition]

Let \( U = \{ p \in \nR[x]_{\le 2} : p(1) = 0 \} \). Find \( U^{0} \).
::::

::: {.solution}
Let \( \varepsilon_1(p) = p(1) \), a linear functional (@exm-linear-functionals). By definition \( U = \ker\varepsilon_1 \), so \( \varepsilon_1 \in U^{0} \). Since \( \varepsilon_1(1) = 1 \), \( \varepsilon_1 \neq 0 \), and @prp-nonzero-functional-surjective gives \( \dim U = 3 - 1 = 2 \). By @thm-dimension-annihilator, \( \dim U^{0} = 3 - 2 = 1 \). Now \( \Span(\varepsilon_1) \) is a subspace of \( U^{0} \) (@prp-annihilator-subspace) of dimension \( 1 \), so \( U^{0} = \Span(\varepsilon_1) \) by @thm-dim-impl-eq.

We never found a basis of \( U \) and never solved an equation. The conclusion is concrete: a functional on \( \nR[x]_{\le 2} \) vanishes on every polynomial with a root at \( 1 \) **only if** it is a multiple of \( p \mapsto p(1) \).
:::

::: {.check}
Let \( U = \Span((1, 1, 1)) \subseteq \nR^3 \). What is \( \dim U^{0} \)? Name a basis of \( U^{0} \) without solving a system.
:::

::: {.solution}
\( \dim U^{0} = 3 - 1 = 2 \) by @thm-dimension-annihilator. The functionals \( x - y \) and \( y - z \) vanish at \( (1, 1, 1) \), hence on \( U \), and they are independent: in \( a(x - y) + b(y - z) = 0 \), the coefficient of \( x \) gives \( a = 0 \), and then \( b = 0 \). Two independent vectors in a \( 2 \)-dimensional space form a basis (@thm-right-size-basis).
:::

## Sums, intersections and spans

Taking annihilators reverses inclusions: more vectors satisfy fewer common equations. It also exchanges sums with intersections. In \( \nR^3 \), let \( U \) be the \( xy \)-plane and \( W \) the \( xz \)-plane. Then \( U^{0} = \Span(z) \) and \( W^{0} = \Span(y) \), writing \( x, y, z \) for the coordinate functionals. The intersection \( U \cap W \) is the \( x \)-axis, with annihilator \( \Span(y, z) = U^{0} + W^{0} \). The sum \( U + W = \nR^3 \) has annihilator \( \{0\} = U^{0} \cap W^{0} \). The theorem says this always happens.

::: {#thm-annihilator-properties}
[Properties of Annihilators]

Let \( V \) be a vector space over \( F \).

::: {.enumerate options="label=(\alph*)"}
1. If \( S \subseteq T \subseteq V \), then \( T^{0} \subseteq S^{0} \).
2. For every subset \( S \subseteq V \), \( S^{0} = (\Span S)^{0} \).
3. For subspaces \( U, W \) of \( V \), \( (U + W)^{0} = U^{0} \cap W^{0} \).
4. If \( V \) is **finite-dimensional**, then for subspaces \( U, W \) of \( V \), \( (U \cap W)^{0} = U^{0} + W^{0} \).
:::
:::

::: {.idea}
Parts (a)–(c) are unwinding definitions: fix a functional in one side and test it on the vectors of the other. In (d), the inclusion \( U^{0} + W^{0} \subseteq (U \cap W)^{0} \) is also direct. The reverse inclusion is the hard half. Given \( \varphi \) vanishing on \( U \cap W \), we would have to **split** it as \( \psi + \chi \) with \( \psi \) killing \( U \) and \( \chi \) killing \( W \), and nothing in sight tells us how. So we count instead: one inclusion plus equal dimensions gives equality. The plan is ① compute \( \dim(U^{0} + W^{0}) \) by the dimension formula for sums inside \( V^{*} \); ② replace \( U^{0} \cap W^{0} \) by \( (U + W)^{0} \) using (c); ③ turn every annihilator dimension into a dimension in \( V \) with @thm-dimension-annihilator; ④ recognize the dimension formula in \( V \). Finite dimension is spent in step ③.
:::

::: {.proof}
(a) Let \( \varphi \in T^{0} \). Every \( \s \in S \) lies in \( T \), so \( \varphi(\s) = 0 \). Hence \( \varphi \in S^{0} \).

(b) Since \( S \subseteq \Span S \) (@thm-span-subspace), part (a) gives \( (\Span S)^{0} \subseteq S^{0} \). Conversely, let \( \varphi \in S^{0} \) and \( \v \in \Span S \), say \( \v = a_1\s_1 + \dots + a_k\s_k \) with \( \s_i \in S \) and \( k \ge 0 \). By @thm-linear-combination, \( \varphi(\v) = \sum_i a_i\varphi(\s_i) = 0 \). Hence \( \varphi \in (\Span S)^{0} \).

(c) Since \( U \subseteq U + W \) and \( W \subseteq U + W \) (@thm-subspace-sum), part (a) gives \( (U + W)^{0} \subseteq U^{0} \) and \( (U + W)^{0} \subseteq W^{0} \), so \( (U + W)^{0} \subseteq U^{0} \cap W^{0} \). Conversely, let \( \varphi \in U^{0} \cap W^{0} \), and let \( \u + \w \in U + W \) with \( \u \in U \), \( \w \in W \). Then \( \varphi(\u + \w) = \varphi(\u) + \varphi(\w) = 0 + 0 = 0 \). Hence \( \varphi \in (U + W)^{0} \).

(d) (⊇) Let \( \varphi = \psi + \chi \) with \( \psi \in U^{0} \) and \( \chi \in W^{0} \), and let \( \v \in U \cap W \). Since \( \v \in U \) and \( \v \in W \), \( \varphi(\v) = \psi(\v) + \chi(\v) = 0 + 0 = 0 \). Hence \( U^{0} + W^{0} \subseteq (U \cap W)^{0} \).

(⊆) Let \( n = \dim V \). The subspaces \( U \), \( W \), \( U \cap W \) (@thm-intersection-subspaces) and \( U + W \) (@thm-subspace-sum) of \( V \) are finite-dimensional by @thm-subspace-dimension. The space \( V^{*} \) has dimension \( n \) by @cor-dimension-dual-space, so its subspaces \( U^{0} \), \( W^{0} \) are finite-dimensional too. By the Dimension Formula for Sums (@thm-dimension-formula-subspace-dim) in \( V^{*} \), then (c),
\[
\dim(U^{0} + W^{0}) = \dim U^{0} + \dim W^{0} - \dim(U^{0} \cap W^{0}) = \dim U^{0} + \dim W^{0} - \dim(U + W)^{0} .
\]
By @thm-dimension-annihilator applied to \( U \), \( W \) and \( U + W \), the right-hand side is
\[
(n - \dim U) + (n - \dim W) - \bigl(n - \dim(U + W)\bigr) = n - \bigl(\dim U + \dim W - \dim(U + W)\bigr) = n - \dim(U \cap W),
\]
where the last equality is @thm-dimension-formula-subspace-dim in \( V \). By @thm-dimension-annihilator once more, \( n - \dim(U \cap W) = \dim(U \cap W)^{0} \). So \( U^{0} + W^{0} \) is a subspace of \( (U \cap W)^{0} \) (by (⊇) and @thm-subspace-sum) with the same finite dimension, and @thm-dim-impl-eq gives \( U^{0} + W^{0} = (U \cap W)^{0} \). This proves the theorem.
:::

Part (b) is what made the computations of this section legitimate: to find the annihilator of a subspace, test functionals on a spanning list only. Parts (c) and (d) form a dictionary. A subspace given as a **sum** has equations obtained by **intersecting** equation spaces; a subspace given as an **intersection** has equations obtained by **adding** them. Later in this chapter this dictionary becomes a practical method for computing sums and intersections of subspaces.

::: {.remark}
Parts (a)–(c) and the inclusion (⊇) in (d) hold in every vector space; only the counting step used finite dimension. The equality (d) is in fact true for **every** \( V \), but the proof must then construct the splitting \( \varphi = \psi + \chi \) by hand; Exercise C1 below does this. In finite dimension, (a) also becomes strict: if \( U \subsetneq W \), then \( \dim U < \dim W \) (@thm-dim-impl-eq), so \( \dim W^{0} < \dim U^{0} \) and \( W^{0} \subsetneq U^{0} \).
:::

## Exercises

### A. Check your understanding

:::: {#exr-annihilators-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the annihilator \( S^{0} \) of a subset \( S \) of a vector space \( V \).
2. True or false: \( U^{0} \) is a subspace of \( V \). Justify your answer.
3. Let \( U \) be a \( 2 \)-dimensional subspace of \( \nR^5 \). What is \( \dim U^{0} \)?
4. For a finite-dimensional \( V \), what are \( \{\0\}^{0} \) and \( V^{0} \)?
5. True or false: if \( U \subsetneq W \) are subspaces of a finite-dimensional \( V \), then \( W^{0} \subsetneq U^{0} \). Justify your answer.
6. To compute \( U^{0} \) for \( U = \Span(\u_1, \dots, \u_m) \subseteq F^n \), which matrix do you row reduce, and why?
:::
::::

::: {.solution}
(a) \( S^{0} = \{ \varphi \in V^{*} : \varphi(\s) = 0 \text{ for all } \s \in S \} \) (@def-annihilator).

(b) False. \( U^{0} \) is a subspace of the dual space \( V^{*} \) (@prp-annihilator-subspace); its elements are functionals, not vectors of \( V \).

(c) \( \dim U^{0} = 5 - 2 = 3 \), by @thm-dimension-annihilator.

(d) \( \{\0\}^{0} = V^{*} \) and \( V^{0} = \{0\} \), by @exm-annihilators (a).

(e) True. By @thm-annihilator-properties (a), \( W^{0} \subseteq U^{0} \). Since \( U \subsetneq W \), \( \dim U < \dim W \) by @thm-dim-impl-eq, so \( \dim W^{0} = \dim V - \dim W < \dim V - \dim U = \dim U^{0} \). Hence the inclusion is strict.

(f) The matrix \( A \) whose **rows** are \( \u_1\tp, \dots, \u_m\tp \). By @thm-functionals-on-fn a functional is \( \x \mapsto \a\tp\x \), and it kills every \( \u_i \) exactly when \( A\a = \0 \); so \( U^{0} \) corresponds to \( \nul(A) \) (@exm-annihilator-via-null-space).
:::

### B. Practice

:::: {#exr-annihilators-b1}
[B1: Computing annihilators]

::: {.enumerate options="label=(\alph*)"}
1. Let \( U = \Span((1, 2, 1, 0), (2, 4, 3, 1), (1, 2, 2, 1)) \subseteq \nR^4 \). Find a basis of \( U^{0} \), and verify that \( \dim U + \dim U^{0} = 4 \).
2. Let \( U = \{ p \in \nR[x]_{\le 3} : p(1) = p(-1) = 0 \} \). Show that \( U^{0} = \Span(\varepsilon_1, \varepsilon_{-1}) \), where \( \varepsilon_c(p) = p(c) \).
:::
::::

::: {.solution}
(a) Let \( A \) have the three spanning vectors as rows. As in @exm-annihilator-via-null-space, \( \varphi_{\a} \in U^{0} \) if and only if \( A\a = \0 \). Subtracting \( 2 \) times row 1 from row 2 and row 1 from row 3 gives rows \( (1, 2, 1, 0) \), \( (0, 0, 1, 1) \), \( (0, 0, 1, 1) \); subtracting row 2 from row 3 and then row 2 from row 1 gives the RREF
\[
\begin{pmatrix} 1 & 2 & 0 & -1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix}.
\]
The free variables are \( a_2 \) and \( a_4 \), and @thm-basis-null-space gives \( \nul(A) = \Span((-2, 1, 0, 0), (1, 0, -1, 1)) \). Hence \( U^{0} \) has the basis
\[
\psi_1(x_1, x_2, x_3, x_4) = -2x_1 + x_2, \qquad \psi_2(x_1, x_2, x_3, x_4) = x_1 - x_3 + x_4 .
\]
Check on the first two spanning vectors: \( \psi_1(1, 2, 1, 0) = 0 \), \( \psi_2(1, 2, 1, 0) = 0 \), \( \psi_1(2, 4, 3, 1) = 0 \), \( \psi_2(2, 4, 3, 1) = 2 - 3 + 1 = 0 \); the third vector is their difference, \( (2, 4, 3, 1) - (1, 2, 1, 0) \). The RREF has two pivots, so \( \dim U = \dim\row(A) = 2 \) (@thm-row-rank-equals-column-rank), and \( 2 + 2 = 4 \).

(b) By definition \( \varepsilon_1, \varepsilon_{-1} \in U^{0} \). *Independent:* if \( a\varepsilon_1 + b\varepsilon_{-1} = 0 \), applying it to \( x + 1 \) gives \( 2a = 0 \) and applying it to \( x - 1 \) gives \( -2b = 0 \). *Dimension of \( U \):* the map \( T \colon \nR[x]_{\le 3} \to \nR^2 \), \( p \mapsto (p(1), p(-1)) \), is linear with kernel \( U \), and its image contains \( T(x + 1) = (2, 0) \) and \( T(x - 1) = (0, -2) \), which span \( \nR^2 \). So \( \rank T = 2 \) and \( \dim U = 4 - 2 = 2 \) by @thm-rank-nullity. By @thm-dimension-annihilator, \( \dim U^{0} = 2 \). Hence the \( 2 \)-dimensional subspace \( \Span(\varepsilon_1, \varepsilon_{-1}) \) of \( U^{0} \) is all of \( U^{0} \) (@thm-dim-impl-eq).
:::

:::: {#exr-annihilators-b2}
[B2: Equations of the symmetric matrices]

Let \( U = \{ A \in M_2(\nR) : A\tp = A \} \). Find \( U^{0} \), and verify the dimension formula.
::::

::: {.solution}
Every symmetric matrix is \( aE_{11} + b(E_{12} + E_{21}) + cE_{22} \), so \( U = \Span(E_{11}, E_{12} + E_{21}, E_{22}) \). Let \( (\varepsilon_{ij}) \) be the dual basis of the standard basis, so that every \( \psi \in M_2(\nR)^{*} \) is \( \psi = \sum_{i,j} c_{ij}\varepsilon_{ij} \) with \( c_{ij} = \psi(E_{ij}) \) (@thm-dual-basis (c)). By @thm-annihilator-properties (b), \( \psi \in U^{0} \) if and only if \( \psi \) kills the three spanning matrices:
\[
c_{11} = 0, \qquad c_{12} + c_{21} = 0, \qquad c_{22} = 0 .
\]
So \( \psi = c_{12}(\varepsilon_{12} - \varepsilon_{21}) \), and \( U^{0} = \Span(\varepsilon_{12} - \varepsilon_{21}) \): the only equation of the symmetric matrices, up to scaling, is \( a_{12} - a_{21} = 0 \). The three spanning matrices are independent (they involve disjoint sets of entries), so \( \dim U = 3 \), and \( \dim U + \dim U^{0} = 3 + 1 = 4 = \dim M_2(\nR) \).
:::

:::: {#exr-annihilators-b3}
[B3: The equations of a hyperplane]

Let \( V \) be a finite-dimensional vector space over \( F \), and let \( \varphi \in V^{*} \) be non-zero. Prove that \( (\ker\varphi)^{0} = \Span(\varphi) \).
::::

::: {.solution}
By definition of the kernel, \( \varphi \) vanishes on \( \ker\varphi \), so \( \varphi \in (\ker\varphi)^{0} \), and \( \Span(\varphi) \subseteq (\ker\varphi)^{0} \) by @prp-annihilator-subspace. Since \( \varphi \neq 0 \), \( \dim\Span(\varphi) = 1 \), and @prp-nonzero-functional-surjective gives \( \dim\ker\varphi = \dim V - 1 \). By @thm-dimension-annihilator, \( \dim(\ker\varphi)^{0} = \dim V - (\dim V - 1) = 1 \). A \( 1 \)-dimensional subspace of a \( 1 \)-dimensional space is the whole space (@thm-dim-impl-eq), so \( (\ker\varphi)^{0} = \Span(\varphi) \).
:::

### C. Going deeper

:::: {#exr-annihilators-c1}
[C1: The intersection formula without counting]

Let \( U, W \) be subspaces of a vector space \( V \) over \( F \), and let \( \varphi \in (U \cap W)^{0} \).

::: {.enumerate options="label=(\alph*)"}
1. Suppose \( V \) is finite-dimensional. Construct \( \psi \in U^{0} \) and \( \chi \in W^{0} \) with \( \varphi = \psi + \chi \), without using any dimension formula.
2. Explain how to modify the construction when \( V \) is infinite-dimensional. Deduce that \( (U \cap W)^{0} = U^{0} + W^{0} \) holds in every vector space.
:::

*Hint: extend a basis of \( U \cap W \) to a basis of \( U \) and, separately, to a basis of \( W \).*
::::

::: {.solution}
(a) Let \( (\x_1, \dots, \x_k) \) be a basis of \( U \cap W \) (@thm-intersection-subspaces, @thm-subspace-dimension). Extend it to a basis \( (\x_1, \dots, \x_k, \u_1, \dots, \u_p) \) of \( U \) and to a basis \( (\x_1, \dots, \x_k, \w_1, \dots, \w_q) \) of \( W \) (@thm-basis-extension).

*The combined list \( (\x_1, \dots, \x_k, \u_1, \dots, \u_p, \w_1, \dots, \w_q) \) is independent.* Let \( \sum a_i\x_i + \sum b_i\u_i + \sum c_j\w_j = \0 \). Then \( \sum c_j\w_j = -\sum a_i\x_i - \sum b_i\u_i \) lies in \( W \) and in \( U \), hence in \( U \cap W \), so \( \sum c_j\w_j = \sum d_i\x_i \) for some \( d_i \in F \). Since \( (\x, \w) \) is a basis of \( W \), all \( c_j \) and \( d_i \) are \( 0 \). Then \( \sum a_i\x_i + \sum b_i\u_i = \0 \), and since \( (\x, \u) \) is a basis of \( U \), all \( a_i \) and \( b_i \) are \( 0 \).

Extend the combined list to a basis of \( V \) by vectors \( \y_1, \dots, \y_r \) (@thm-basis-extension). By @thm-linear-transform-basis there is \( \psi \in V^{*} \) with
\[
\psi(\x_i) = 0, \qquad \psi(\u_i) = 0, \qquad \psi(\w_j) = \varphi(\w_j), \qquad \psi(\y_l) = 0 .
\]
Then \( \psi \) kills a basis of \( U \), so \( \psi \in U^{0} \) (@thm-annihilator-properties (b)). Put \( \chi \coloneqq \varphi - \psi \). Then \( \chi(\x_i) = \varphi(\x_i) - 0 = 0 \), because \( \x_i \in U \cap W \) and \( \varphi \in (U \cap W)^{0} \); and \( \chi(\w_j) = \varphi(\w_j) - \varphi(\w_j) = 0 \). So \( \chi \) kills a basis of \( W \), and \( \chi \in W^{0} \). Hence \( \varphi = \psi + \chi \in U^{0} + W^{0} \).

(b) Replace the finite lists by sets. By @thm-every-space-has-basis, \( U \cap W \) has a basis \( X \), and by @thm-basis-extension-general it extends to a basis \( X \cup P \) of \( U \) and to a basis \( X \cup Q \) of \( W \), with \( P \cap X = Q \cap X = \varnothing \). First, \( P \cap Q = \varnothing \): a vector of \( P \cap Q \) lies in \( U \cap W = \Span X \), which contradicts the independence of \( X \cup P \). So every vector of \( X \cup P \cup Q \) lies in exactly one of \( X \), \( P \), \( Q \). A linear relation among finitely many distinct vectors of \( X \cup P \cup Q \) splits into an \( X \)-part, a \( P \)-part and a \( Q \)-part, and the independence argument of (a) applies word for word; so \( X \cup P \cup Q \) is independent. By @thm-basis-extension-general it extends to a basis \( B \) of \( V \). Every \( \v \in V \) is a finite combination \( \v = \sum_{\b} c_{\b}\b \) of distinct vectors of \( B \), with unique coefficients because \( B \) is independent. Define
\[
\psi(\v) \coloneqq \sum_{\b \in Q} c_{\b}\,\varphi(\b),
\]
a finite sum over the vectors of \( Q \) that occur. Adding or scaling expansions gives expansions, so by uniqueness the coefficients add and scale, and \( \psi \) is linear. It vanishes on \( X \cup P \) and agrees with \( \varphi \) on \( Q \), so the rest of (a) is unchanged: \( \psi \in U^{0} \) and \( \chi = \varphi - \psi \) kills the basis \( X \cup Q \) of \( W \). Together with the inclusion (⊇) of @thm-annihilator-properties (d), which used no finiteness, this gives \( (U \cap W)^{0} = U^{0} + W^{0} \) in every vector space.
:::

:::: {#exr-annihilators-c2}
[C2: Equations of a double root]

Let \( U = \{ p \in \nR[x]_{\le 3} : p(1) = 0 \text{ and } p'(1) = 0 \} \), and let \( \varepsilon_1(p) = p(1) \) and \( \eta_1(p) = p'(1) \). Prove that \( U^{0} = \Span(\varepsilon_1, \eta_1) \). Deduce that \( \psi(p) = p(0) - p(2) + 2p'(1) \) does **not** vanish on \( U \).
::::

::: {.solution}
Both \( \varepsilon_1 \) and \( \eta_1 \) are linear (evaluation, and differentiation followed by evaluation), and they vanish on \( U \) by definition. *Independent:* if \( a\varepsilon_1 + b\eta_1 = 0 \), applying it to \( 1 \) gives \( a = 0 \), and applying it to \( x - 1 \) gives \( b = 0 \). *Dimension of \( U \):* the linear map \( T \colon \nR[x]_{\le 3} \to \nR^2 \), \( p \mapsto (p(1), p'(1)) \), has kernel \( U \), and \( T(1) = (1, 0) \), \( T(x - 1) = (0, 1) \), so \( T \) is surjective. By @thm-rank-nullity, \( \dim U = 4 - 2 = 2 \), and by @thm-dimension-annihilator, \( \dim U^{0} = 2 \). The \( 2 \)-dimensional subspace \( \Span(\varepsilon_1, \eta_1) \) of \( U^{0} \) is therefore all of \( U^{0} \) (@thm-dim-impl-eq).

For the deduction, suppose \( \psi \in U^{0} \). Then \( \psi = a\varepsilon_1 + b\eta_1 \). Applying both sides to \( 1 \) gives \( 1 - 1 + 0 = a \), so \( a = 0 \); applying them to \( x - 1 \) gives \( -1 - 1 + 2 = b \), so \( b = 0 \). Then \( \psi = 0 \). But \( \psi(x^2) = 0 - 4 + 4 = 0 \) and \( \psi(x^3) = 0 - 8 + 6 = -2 \neq 0 \), a contradiction. Hence \( \psi \notin U^{0} \). Check with an explicit witness: \( p = x(x - 1)^2 \in U \) has \( \psi(p) = 0 - 2 + 0 = -2 \neq 0 \).
:::

:::: {#exr-annihilators-c3}
[C3: Dual of a direct sum decomposition]

::: {.enumerate options="label=(\alph*)"}
1. Let \( V \) be finite-dimensional with \( V = U \oplus W \). Prove that \( V^{*} = U^{0} \oplus W^{0} \).
2. In \( \nR^2 \), let \( U = \Span((1, 0)) \) and \( W = \Span((1, 1)) \). Write \( \psi(x, y) = x \) as \( \psi_U + \psi_W \) with \( \psi_U \in U^{0} \) and \( \psi_W \in W^{0} \).
:::
::::

::: {.solution}
(a) Since the sum is direct, \( U \cap W = \{\0\} \) (@thm-direct-sum-criteria), and \( U + W = V \). By @thm-annihilator-properties (c) and @exm-annihilators (a), \( U^{0} \cap W^{0} = (U + W)^{0} = V^{0} = \{0\} \). By @thm-annihilator-properties (d), \( U^{0} + W^{0} = (U \cap W)^{0} = \{\0\}^{0} = V^{*} \). So \( V^{*} = U^{0} + W^{0} \), and the sum is direct by @thm-direct-sum-criteria.

(b) A functional \( ax + by \) vanishes on \( (1, 0) \) if and only if \( a = 0 \), so \( U^{0} = \Span(y) \). It vanishes on \( (1, 1) \) if and only if \( b = -a \), so \( W^{0} = \Span(x - y) \). Solving \( x = s\,y + t(x - y) \) gives \( t = 1 \) and \( s - t = 0 \), so \( s = 1 \):
\[
\psi = \underbrace{y}_{\in U^{0}} + \underbrace{(x - y)}_{\in W^{0}} .
\]
By (a) this decomposition is unique.
:::
