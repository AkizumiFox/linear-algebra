# The Exchange Theorem and Dimension

Every finite-dimensional space has a basis, and usually a great many of them. This section proves that they all have the same length, so that the length is a property of the space and not of the basis we happened to pick. That number is the dimension. The key step is the Steinitz Exchange Theorem, the most important proof of the chapter. With it we build the everyday tools of dimension counting: size bounds, "count instead of check", extension of independent lists to bases, and dimensions of subspaces.

## How big is a vector space?

We would like to say that a plane is smaller than space, and that \( M_2(\nR) \) and \( \nR[x]_{\le 3} \) are, in some sense, the same size. The naive measure is the number of elements. It fails at once: \( \nR^2 \), \( M_2(\nR) \) and \( \nR[x]_{\le 3} \) are all infinite sets, and counting elements cannot tell them apart.

A better measure counts **how many vectors it takes to build everything, without waste**, which is the length of a basis. The standard bases give
\[
\nR^2 : 2, \qquad M_2(\nR) : 4 \;\; (E_{11}, E_{12}, E_{21}, E_{22}), \qquad \nR[x]_{\le 3} : 4 \;\; (1, x, x^2, x^3).
\]
This matches intuition: a matrix \( \begin{pmatrix} a & b \\ c & d \end{pmatrix} \) and a polynomial \( a + bx + cx^2 + dx^3 \) are both described by four free numbers.

But there is a gap. A space has many bases. We counted the standard basis of \( \nR^2 \); the basis \( ((1, 1), (1, -1)) \) also has length 2, but what guarantees that no basis of \( \nR^2 \) has length 3? If some space had bases of two different lengths, "the length of a basis" would be meaningless. So before we can define anything, we need the following.

> **Goal.** Any two bases of a finite-dimensional vector space have the same length.

A basis is independent **and** spanning, and the goal follows from a single inequality about the two properties separately: *an independent list is never longer than a spanning list.* Granting this, take two bases \( \sB \) and \( \sC \). Since \( \sB \) is independent and \( \sC \) spans, \( \sB \) is not longer than \( \sC \). Swapping the roles, \( \sC \) is not longer than \( \sB \). So they have the same length. Everything rests on the inequality.

## The Steinitz Exchange Theorem

Why should an independent list be no longer than a spanning list? In \( \nR^2 \) the spanning list \( (\e_1, \e_2) \) has length 2, and three vectors in the plane always satisfy a linear relation, but "the plane is two-dimensional" is what we are trying to define, so we cannot use it. The idea is instead to feed the independent vectors into the spanning list one at a time, pushing out one spanning vector each time, while keeping the list spanning. If the independent vectors outnumbered the spanning ones, we would run out of vectors to push out.

::: {#thm-steinitz}
[Steinitz Exchange Theorem]

Let \( V \) be a vector space over \( F \). Suppose that \( (\u_1, \dots, \u_m) \) is a **linearly independent** list in \( V \) and that \( (\w_1, \dots, \w_n) \) is a list that **spans** \( V \). Then

::: {.enumerate options="label=(\alph*)"}
1. \( m \le n \), and
2. after renumbering \( \w_1, \dots, \w_n \) suitably, the list \( (\u_1, \dots, \u_m, \w_{m+1}, \dots, \w_n) \) spans \( V \).
:::
:::

In words: an independent list is at most as long as a spanning list, and the independent vectors can **replace** \( m \) of the spanning vectors without losing the spanning property. "Renumbering" means listing the \( \w \)'s in a different order; which \( \w \)'s get replaced depends on the \( \u \)'s.

::: {.idea}
Picture a row of \( n \) slots holding \( \w_1, \dots, \w_n \); the row spans \( V \). We push \( \u_1 \) into the row and push one \( \w \) out, then \( \u_2 \), and so on, keeping the row spanning after every exchange. Here is the picture for \( m = 3 \), \( n = 4 \), with the \( \w \)'s numbered in the order they leave.

\begin{center}
\begin{tikzpicture}[x=1.3cm, y=1.05cm,
    slot/.style={draw, minimum width=1.05cm, minimum height=0.62cm},
    uslot/.style={slot, fill=black!12, very thick}]
  \foreach \row/\k in {0/0, 1/1, 2/2, 3/3} {
    \node[anchor=east] at (-0.5, -\row) {after $\k$};
  }
  \node[slot] at (0,0) {$\w_1$}; \node[slot] at (1,0) {$\w_2$}; \node[slot] at (2,0) {$\w_3$}; \node[slot] at (3,0) {$\w_4$};
  \node[uslot] at (0,-1) {$\u_1$}; \node[slot] at (1,-1) {$\w_2$}; \node[slot] at (2,-1) {$\w_3$}; \node[slot] at (3,-1) {$\w_4$};
  \node[uslot] at (0,-2) {$\u_1$}; \node[uslot] at (1,-2) {$\u_2$}; \node[slot] at (2,-2) {$\w_3$}; \node[slot] at (3,-2) {$\w_4$};
  \node[uslot] at (0,-3) {$\u_1$}; \node[uslot] at (1,-3) {$\u_2$}; \node[uslot] at (2,-3) {$\u_3$}; \node[slot] at (3,-3) {$\w_4$};
  \foreach \row/\k in {1/1, 2/2, 3/3} {
    \node[anchor=west] at (3.7, -\row) {$\u_{\k}$ in, $\w_{\k}$ out};
  }
  \node[anchor=west] at (3.7, 0) {spans $V$};
  \node at (1.5, -3.8) {every row spans $V$};
\end{tikzpicture}
\end{center}

Which \( \w \) may leave? Write the incoming \( \u_{k+1} \) as a combination of the current row. Any \( \w \) with a **non-zero** coefficient can be solved for, so it lies in the span of the other entries together with \( \u_{k+1} \), and removing it costs nothing. Such a \( \w \) must exist: otherwise \( \u_{k+1} \) would be a combination of \( \u_1, \dots, \u_k \) alone, which independence forbids. In particular, while \( \u \)'s remain to be inserted, a \( \w \) remains to be removed, and that is why \( m \le n \).

*Step roadmap.* Induction on the number \( k \) of exchanges, with the invariant

> \( P(k) \): \( k \le n \), and after renumbering the \( \w \)'s, the list \( (\u_1, \dots, \u_k, \w_{k+1}, \dots, \w_n) \) spans \( V \).

**Step 1** is the base case \( k = 0 \). **Step 2** writes \( \u_{k+1} \) in the current list. **Step 3** is the Claim that some remaining \( \w \) has a non-zero coefficient. **Step 4** exchanges that \( \w \) for \( \u_{k+1} \) and checks the span.
:::

::: {.proof}
We prove \( P(k) \) for \( k = 0, 1, \dots, m \) by induction on \( k \). The case \( k = m \) is the theorem.

**Step 1 (base case).** For \( k = 0 \) the list in \( P(0) \) is \( (\w_1, \dots, \w_n) \), which spans \( V \) by hypothesis, and \( 0 \le n \). So \( P(0) \) holds.

**Step 2.** Let \( 0 \le k < m \) and suppose \( P(k) \) holds. Renumber the \( \w \)'s as \( P(k) \) allows, so that
\[
L_k = (\u_1, \dots, \u_k, \w_{k+1}, \dots, \w_n)
\]
spans \( V \). Since \( k < m \), the vector \( \u_{k+1} \) exists, and \( \u_{k+1} \in V = \Span(L_k) \). Hence there are scalars \( a_1, \dots, a_k, b_{k+1}, \dots, b_n \in F \) with
\[
\u_{k+1} = a_1\u_1 + \dots + a_k\u_k + b_{k+1}\w_{k+1} + \dots + b_n\w_n. \tag{$\ast$}
\]
(If \( k = n \), the list \( L_k \) contains no \( \w \)'s and the second group of terms is empty.)

**Step 3.**

::: {.claim}
We have \( k + 1 \le n \), and \( b_j \ne 0 \) for some \( j \) with \( k + 1 \le j \le n \).
:::

::: {.proof}
Suppose not. Then either \( k = n \), so that there are no \( b \)'s at all, or \( k < n \) and \( b_{k+1} = \dots = b_n = 0 \). In both cases \( (\ast) \) reads \( \u_{k+1} = a_1\u_1 + \dots + a_k\u_k \). Therefore
\[
a_1\u_1 + \dots + a_k\u_k + (-1)\u_{k+1} + 0\u_{k+2} + \dots + 0\u_m = \0
\]
is a linear relation among \( \u_1, \dots, \u_m \) in which the coefficient of \( \u_{k+1} \) is \( -1 \ne 0 \). This contradicts the linear independence of \( (\u_1, \dots, \u_m) \). Hence there is at least one \( \w \) in \( L_k \), so \( k + 1 \le n \), and some \( b_j \) with \( j \ge k + 1 \) is non-zero.
:::

**Step 4.** Renumber \( \w_{k+1}, \dots, \w_n \) among themselves so that \( b_{k+1} \ne 0 \). This only changes the order of entries of \( L_k \), so \( L_k \) still spans \( V \) (the span of a list does not depend on the order of its entries), and \( (\ast) \) still holds with the coefficients renumbered in the same way. Put
\[
L_{k+1} = (\u_1, \dots, \u_{k+1}, \w_{k+2}, \dots, \w_n).
\]
Since \( b_{k+1} \ne 0 \), the scalar \( b_{k+1}^{-1} \) exists, and solving \( (\ast) \) for \( \w_{k+1} \) gives
\[
\w_{k+1} = b_{k+1}^{-1}\big( \u_{k+1} - a_1\u_1 - \dots - a_k\u_k - b_{k+2}\w_{k+2} - \dots - b_n\w_n \big).
\]
The right side is a combination of the entries of \( L_{k+1} \), so \( \w_{k+1} \in \Span(L_{k+1}) \). By @thm-span-absorb, inserting \( \w_{k+1} \) into \( L_{k+1} \) does not change the span:
\[
\Span(L_{k+1}) = \Span(\u_1, \dots, \u_{k+1}, \w_{k+1}, \w_{k+2}, \dots, \w_n).
\]
The list on the right contains every entry of \( L_k \), so its span is a subspace containing all entries of \( L_k \), and hence contains \( \Span(L_k) = V \) by @thm-span-subspace. Therefore \( \Span(L_{k+1}) = V \). Together with \( k + 1 \le n \) from the Claim, this is \( P(k + 1) \).

By induction, \( P(m) \) holds: \( m \le n \), and after renumbering the \( \w \)'s, \( (\u_1, \dots, \u_m, \w_{m+1}, \dots, \w_n) \) spans \( V \). This proves the theorem.
:::

Part (a) is the inequality our goal needed. Part (b), the exchange itself, is a bonus that we will spend later in this section, to extend independent lists to bases.

::: {.warning}
The \( \w \) that leaves must have a **non-zero** coefficient; an arbitrary \( \w \) will not do. In \( \nR^2 \), take the spanning list \( (\w_1, \w_2) = ((1, 0), (0, 1)) \) and the independent vector \( \u_1 = (1, 0) = 1\w_1 + 0\w_2 \). Exchanging \( \u_1 \) for \( \w_1 \) gives \( ((1, 0), (0, 1)) \), which spans. Exchanging \( \u_1 \) for \( \w_2 \), whose coefficient is \( 0 \), gives \( ((1, 0), (1, 0)) \), which does not reach \( (0, 1) \).
:::

The theorem already settles questions that would otherwise need a computation.

::: {.check}
Can the four polynomials \( 1 + x \), \( x + x^2 \), \( x^2 + 1 \), \( 1 + x + x^2 \) be linearly independent in \( \nR[x]_{\le 2} \)?

::: {.solution}
No. The list \( (1, x, x^2) \) spans \( \nR[x]_{\le 2} \) and has length \( 3 \), so by @thm-steinitz every independent list there has length at most \( 3 < 4 \). Indeed \( (1 + x) + (x + x^2) + (x^2 + 1) - 2(1 + x + x^2) = 0 \).
:::
:::

## Dimension

The goal of the section is now one line away.

::: {#thm-basis-theorem}
[Basis Theorem]

Let \( V \) be a finite-dimensional vector space. Then \( V \) has a basis, and any two bases of \( V \) have the same length.
:::

::: {.proof}
By @cor-basis-existence, \( V \) has a basis. Let \( (\v_1, \dots, \v_n) \) and \( (\w_1, \dots, \w_m) \) be bases of \( V \). The first is linearly independent and the second spans \( V \), so \( n \le m \) by @thm-steinitz. Swapping the roles of the two bases gives \( m \le n \). Hence \( m = n \).
:::

We started from a question: how big is a vector space? The Basis Theorem says that one number, the length of a basis, answers it without depending on any choice. So we give that number a name.

*The dimension of a space is the number of vectors in any basis: how many independent directions the space has.*

::: {#def-dimension}
[Dimension]

Let \( V \) be a finite-dimensional vector space over \( F \). The **dimension** of \( V \) over \( F \), written \( \dim_F V \) or simply \( \dim V \), is the length of **any** basis of \( V \).
:::

In words: pick a basis of \( V \), any basis at all, and count its vectors. The dimension is defined only for finite-dimensional spaces (@def-finite-dimensional); a space spanned by no finite list is infinite-dimensional, and we do not assign it a number here. The subscript \( F \) records the field of scalars, which, as we will see, matters.

**Well-definedness.** Two things could go wrong with "the length of any basis": there might be no basis to count, or different bases might give different counts. The first is ruled out by @cor-basis-existence and the second by @thm-basis-theorem. That is exactly what the word **any** in the definition needs.

::: {#exm-dimensions}
[Dimensions of the Running Examples]

Find the dimension of each space.

::: {.enumerate options="label=(\alph*)"}
1. \( F^n \), \( M_{m \times n}(F) \) and \( F[x]_{\le n} \).
2. The zero space \( \{\0\} \).
3. \( \nC \) over \( \nC \), and \( \nC \) over \( \nR \).
4. \( U = \{ A \in M_2(\nR) : A\tp = A \} \), the symmetric \( 2 \times 2 \) real matrices.
5. \( \nQ(\sqrt 2) = \{ a + b\sqrt 2 : a, b \in \nQ \} \) over \( \nQ \) (@exm-q-adjoin-sqrt2).
:::
:::

::: {.solution}
In each case we exhibit one basis and count it.

(a) The standard bases of @exm-standard-bases have lengths \( n \), \( mn \) and \( n + 1 \). So \( \dim F^n = n \), \( \dim M_{m \times n}(F) = mn \), and \( \dim F[x]_{\le n} = n + 1 \).

(b) The empty list is a basis of \( \{\0\} \) (@exm-more-bases), so \( \dim \{\0\} = 0 \).

(c) Over \( \nC \), the list \( (1) \) is a basis of \( \nC \): every \( z \) equals \( z \cdot 1 \), and \( z \cdot 1 = 0 \) forces \( z = 0 \). So \( \dim_\nC \nC = 1 \). Over \( \nR \), the list \( (1, i) \) is a basis (@exm-more-bases), so \( \dim_\nR \nC = 2 \).

(d) A symmetric matrix has the form \( \begin{pmatrix} a & b \\ b & d \end{pmatrix} = aE_{11} + b(E_{12} + E_{21}) + dE_{22} \), and this combination is the zero matrix only when \( a = b = d = 0 \). So \( (E_{11}, E_{12} + E_{21}, E_{22}) \) is a basis of \( U \), as in @exr-basis-b3, and \( \dim U = 3 \).

(e) Every element is \( a \cdot 1 + b\sqrt 2 \) with \( a, b \in \nQ \), so \( (1, \sqrt 2) \) spans. Let \( a + b\sqrt 2 = 0 \) with \( a, b \in \nQ \). If \( b \ne 0 \), then \( \sqrt 2 = -a/b \in \nQ \), contradicting @thm-sqrt2-irrational. So \( b = 0 \), and then \( a = 0 \). Hence \( (1, \sqrt 2) \) is a basis, and \( \dim_\nQ \nQ(\sqrt 2) = 2 \).
:::

The zero space in (b) is the degenerate case: it has dimension \( 0 \) because its basis is empty, not because it has no elements. It has one element, \( \0 \).

**Non-example by minimal change.** Remove the degree bound from \( F[x]_{\le n} \). The space \( F[x] \) is not spanned by any finite list (@thm-polynomials-infinite-dimensional), so it has no finite basis and no dimension in the sense of @def-dimension. The hypothesis "finite-dimensional" in the Basis Theorem is exactly what fails.

**Why this definition.** Why a basis, and not some other list? Spanning lists can be made as long as we like by repeating vectors, and independent lists can be made as short as we like by deleting vectors, so neither length alone is an invariant. A basis sits exactly where the two meet: it is the longest possible independent list and the shortest possible spanning list, as we prove next. And why not count elements? Over \( \nR \) every non-zero space is infinite, so the count says nothing. Over a finite field the count does carry information, but it is determined by the dimension; see @exr-dimension-c3.

::: {.warning}
The dimension of \( F[x]_{\le n} \) is \( n + 1 \), **not** \( n \). The basis \( (1, x, \dots, x^n) \) has one vector for each exponent \( 0, 1, \dots, n \), and the constant \( 1 \) is easy to forget. For instance \( \dim \nR[x]_{\le 2} = 3 \).
:::

::: {.warning}
Dimension depends on the field. The set \( \nC \) has dimension \( 1 \) over \( \nC \) but dimension \( 2 \) over \( \nR \), because over \( \nR \) the scalar \( i \) is no longer available and \( i \) must be counted as a separate basis vector. When more than one field is in sight, write \( \dim_F \).
:::

::: {.check}
What are \( \dim M_{2 \times 3}(F) \) and \( \dim F[x]_{\le 5} \)? Which of them equals \( \dim F^6 \)?

::: {.solution}
\( \dim M_{2 \times 3}(F) = 2 \cdot 3 = 6 \) and \( \dim F[x]_{\le 5} = 5 + 1 = 6 \). Both equal \( \dim F^6 = 6 \).
:::
:::

## Size bounds

The first payoff turns the Exchange Theorem into statements about the number \( \dim V \).

::: {#thm-size-bounds}
[Size Bounds]

Let \( V \) be a vector space over \( F \) with \( \dim V = n \).

::: {.enumerate options="label=(\alph*)"}
1. Every linearly independent list in \( V \) has length at most \( n \). Hence every list in \( V \) of length **greater than** \( n \) is linearly dependent.
2. Every list that spans \( V \) has length at least \( n \). Hence no list of length **less than** \( n \) spans \( V \).
:::
:::

::: {.proof}
Let \( \sB \) be a basis of \( V \); it has length \( n \).

(a) Let \( \sL \) be an independent list of length \( \ell \). Since \( \sB \) spans \( V \), @thm-steinitz gives \( \ell \le n \). The second sentence is the contrapositive.

(b) Let \( \sL \) be a list of length \( \ell \) that spans \( V \). Since \( \sB \) is independent, @thm-steinitz gives \( n \le \ell \). The second sentence is the contrapositive.
:::

So in a space of dimension \( n \),
\[
\text{length of an independent list} \;\le\; n \;\le\; \text{length of a spanning list}.
\]
This settles many questions with no computation. The four vectors \( (1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 0, 0) \) in \( \nR^3 \) are dependent, because \( 4 > 3 \). Three matrices never span \( M_2(F) \), because \( 3 < 4 \).

## Count instead of check

To show a list is a basis we normally check two things, independence and spanning. When the length of the list equals the dimension, one check is enough. This is one of the most used facts in the book.

::: {#thm-right-size-basis}
[Count Instead of Check]

Let \( V \) be a vector space with \( \dim V = n \), and let \( \sL = (\v_1, \dots, \v_n) \) be a list in \( V \) of length exactly \( n \).

::: {.enumerate options="label=(\alph*)"}
1. If \( \sL \) is linearly independent, then \( \sL \) is a basis of \( V \).
2. If \( \sL \) spans \( V \), then \( \sL \) is a basis of \( V \).
:::
:::

::: {.idea}
For (a), the exchange part of @thm-steinitz does the work: we can push all \( n \) vectors of \( \sL \) into a basis of length \( n \), and then no old vectors are left, so \( \sL \) alone spans. For (b), sift \( \sL \): the result is a basis, so it has length \( n \), so nothing was discarded.
:::

::: {.proof}
(a) Let \( (\w_1, \dots, \w_n) \) be a basis of \( V \); in particular it spans \( V \). Since \( \sL \) is independent of length \( n \), @thm-steinitz (b) with \( m = n \) says that, after renumbering the \( \w \)'s, the list \( (\v_1, \dots, \v_n, \w_{n+1}, \dots, \w_n) \) spans \( V \). This list contains no \( \w \)'s: it is \( \sL \). So \( \sL \) is independent and spans \( V \), and it is a basis.

(b) By @thm-sift, \( \sL \) contains a sub-list that is a basis of \( V \). By @thm-basis-theorem, that sub-list has length \( \dim V = n \). The only sub-list of length \( n \) of a list of length \( n \) is the list itself. Hence \( \sL \) is a basis.
:::

The theorem lets us choose the easier check, and independence is almost always easier: it is a single equation equal to \( \0 \), while spanning asks us to solve for an arbitrary vector.

::: {#exm-count-instead-of-check}
[A Basis by Counting]

Show that \( (1, \; 1 + x, \; (1 + x)^2) \) is a basis of \( \nR[x]_{\le 2} \).
:::

::: {.solution}
By @exm-dimensions, \( \dim \nR[x]_{\le 2} = 3 \), and the list has length \( 3 \). So by @thm-right-size-basis (a) it suffices to check independence. Let
\[
a \cdot 1 + b(1 + x) + c(1 + x)^2 = 0.
\]
Expanding, the left side is \( (a + b + c) + (b + 2c)x + cx^2 \). Comparing coefficients with the zero polynomial: \( c = 0 \); then \( b + 2c = 0 \) gives \( b = 0 \); then \( a + b + c = 0 \) gives \( a = 0 \). Hence the list is independent, with \( 3 = \dim \nR[x]_{\le 2} \) elements, and therefore it is a basis.
:::

We never had to show that every polynomial of degree at most 2 is a combination of \( 1, 1 + x, (1 + x)^2 \). The dimension count did it for us.

## Extending to a basis

Sifting finds a basis **inside** a spanning list. The opposite direction starts from an independent list and grows it into a basis. This is the tool behind every dimension formula later in the book: start from a basis of the smallest space, then extend.

::: {#thm-basis-extension}
[Basis Extension Theorem]

Let \( V \) be a finite-dimensional vector space with \( \dim V = n \), and let \( (\u_1, \dots, \u_m) \) be a linearly independent list in \( V \). Then \( m \le n \), and there are vectors \( \v_{m+1}, \dots, \v_n \in V \) such that
\[
(\u_1, \dots, \u_m, \v_{m+1}, \dots, \v_n)
\]
is a basis of \( V \). Moreover, the \( \v \)'s can be chosen from any given basis of \( V \).
:::

::: {.proof}
Let \( (\w_1, \dots, \w_n) \) be a basis of \( V \). It spans \( V \), so by @thm-steinitz, \( m \le n \), and after renumbering the \( \w \)'s the list \( (\u_1, \dots, \u_m, \w_{m+1}, \dots, \w_n) \) spans \( V \). This list has length \( m + (n - m) = n = \dim V \), so it is a basis by @thm-right-size-basis (b). Take \( \v_j = \w_j \) for \( m < j \le n \).
:::

Alternatively, sift the list \( (\u_1, \dots, \u_m, \w_1, \dots, \w_n) \). It spans \( V \), and sifting keeps every \( \u_k \): the sub-list \( (\u_1, \dots, \u_k) \) is independent (@exr-independence-b3), so \( \u_k \notin \Span(\u_1, \dots, \u_{k-1}) \) by @lem-append-independent. Sifting has the advantage of telling us **which** \( \w \)'s to add.

::: {#exm-extend-to-basis}
[Extending an Independent List]

Extend the list \( ((1, 1, 0), (0, 1, 1)) \) to a basis of \( \nR^3 \).
:::

::: {.solution}
The list is independent: \( a(1, 1, 0) + b(0, 1, 1) = (a, a + b, b) = \0 \) forces \( a = b = 0 \). By @thm-basis-extension, one vector from the standard basis will do, so we try \( \e_1 \). Let
\[
a(1, 1, 0) + b(0, 1, 1) + c(1, 0, 0) = (a + c, \; a + b, \; b) = (0, 0, 0).
\]
Then \( b = 0 \), so \( a = 0 \) from the second entry, so \( c = 0 \) from the first. Hence \( ((1, 1, 0), (0, 1, 1), (1, 0, 0)) \) is independent, with \( 3 = \dim \nR^3 \) elements, and therefore a basis by @thm-right-size-basis (a).
:::

The extension is far from unique. The same computation with \( \e_2 \) gives \( (a, a + b + c, b) = \0 \), and with \( \e_3 \) gives \( (a, a + b, b + c) = \0 \); both force \( a = b = c = 0 \). So any one of \( \e_1, \e_2, \e_3 \) completes this list to a basis.

## Largest independent lists and smallest spanning lists

We claimed that a basis is where independence and spanning meet. Here is the precise statement. It does not need finite dimension, and it is the form of "basis" that generalizes to infinite-dimensional spaces later in this chapter.

Call an independent list \( (\v_1, \dots, \v_n) \) in \( V \) **maximal independent** if for **every** \( \v \in V \) the longer list \( (\v_1, \dots, \v_n, \v) \) is dependent. Call a spanning list **minimal spanning** if deleting **any one** of its entries gives a list that does not span \( V \).

::: {#thm-maximal-indep}
[Maximal Independent and Minimal Spanning Lists]

Let \( V \) be a vector space and \( \sL = (\v_1, \dots, \v_n) \) a list in \( V \).

::: {.enumerate options="label=(\alph*)"}
1. \( \sL \) is a basis of \( V \) if and only if \( \sL \) is maximal independent.
2. \( \sL \) is a basis of \( V \) if and only if \( \sL \) is minimal spanning.
:::
:::

::: {.proof}
(a) (⇒) Let \( \sL \) be a basis and \( \v \in V \). Then \( \v \in \Span(\sL) = V \), so \( (\v_1, \dots, \v_n, \v) \) is dependent by @lem-append-independent. Hence \( \sL \) is maximal independent.

(⇐) Let \( \sL \) be maximal independent and \( \v \in V \). The list \( (\v_1, \dots, \v_n, \v) \) is dependent while \( \sL \) is independent, so \( \v \in \Span(\sL) \) by @lem-append-independent. Hence \( \sL \) spans \( V \), and \( \sL \) is a basis.

(b) (⇒) Let \( \sL \) be a basis, and suppose that deleting \( \v_j \) gives a list that still spans \( V \). Then \( \v_j = \sum_{i \ne j} c_i\v_i \) for some scalars, so \( \sum_{i \ne j} c_i\v_i + (-1)\v_j = \0 \), a linear relation with the coefficient \( -1 \ne 0 \). This contradicts independence. Hence \( \sL \) is minimal spanning.

(⇐) Let \( \sL \) be minimal spanning. By @thm-sift, some sub-list \( S \) of \( \sL \) is a basis of \( V \). Suppose \( S \ne \sL \). Then \( S \) omits some entry \( \v_j \), so every entry of \( S \) is an entry of the list \( \sL' \) obtained by deleting \( \v_j \). By @thm-span-subspace, \( \Span(\sL') \) contains \( \Span(S) = V \), so \( \sL' \) spans \( V \), contradicting minimality. Hence \( S = \sL \), and \( \sL \) is a basis.
:::

"Maximal" means "cannot be enlarged", which is different from "longest possible". In a finite-dimensional space the two agree: by @thm-size-bounds a longest independent list has length \( \dim V \), and by @thm-right-size-basis every independent list of that length is a basis.

## Dimensions of subspaces

A subspace should be no bigger than the space containing it. Proving this needs care, because of a tempting circular argument.

::: {#thm-subspace-dimension}
[Dimension of a Subspace]

Let \( V \) be a finite-dimensional vector space and \( U \) a subspace of \( V \). Then \( U \) is finite-dimensional, and \( \dim U \le \dim V \).
:::

::: {.idea}
The tempting proof is: "take a basis of \( U \); it is independent in \( V \), so its length is at most \( \dim V \)". But we do not yet know that \( U \) **has** a basis. @cor-basis-existence needs a finite spanning list of \( U \), and that is exactly what we are trying to prove. So we build from below instead. Independent lists inside \( U \) are independent in \( V \), so their lengths are bounded by \( \dim V \). Take one of the largest possible length. If it did not span \( U \), we could append a vector of \( U \) outside its span and get a longer one.
:::

::: {.proof}
Let \( n = \dim V \). Independence of a list depends only on its vectors and the operations of \( V \), which \( U \) shares, so every independent list in \( U \) is an independent list in \( V \), and has length at most \( n \) by @thm-size-bounds. The empty list is independent in \( U \). Hence the set of lengths of independent lists in \( U \) is a non-empty set of integers in \( \{0, 1, \dots, n\} \), and it has a largest element \( k \le n \). Choose an independent list \( (\u_1, \dots, \u_k) \) in \( U \) of this length.

We claim \( \Span(\u_1, \dots, \u_k) = U \). Since \( U \) is a subspace containing every \( \u_i \), @thm-span-subspace gives \( \Span(\u_1, \dots, \u_k) \subseteq U \). Conversely, let \( \u \in U \), and suppose \( \u \notin \Span(\u_1, \dots, \u_k) \). By @lem-append-independent, \( (\u_1, \dots, \u_k, \u) \) is an independent list in \( U \) of length \( k + 1 \), contradicting the maximality of \( k \). Hence \( \u \in \Span(\u_1, \dots, \u_k) \).

Therefore \( (\u_1, \dots, \u_k) \) spans \( U \), so \( U \) is finite-dimensional (@def-finite-dimensional), and the list is a basis of \( U \). Hence \( \dim U = k \le n = \dim V \).
:::

When the dimensions are equal, there is no room left.

::: {#thm-dim-impl-eq}
[Equal Dimension Forces Equality]

Let \( V \) be a finite-dimensional vector space and \( U \) a subspace of \( V \). If \( \dim U = \dim V \), then \( U = V \).
:::

::: {.proof}
Let \( n = \dim U = \dim V \); \( U \) is finite-dimensional by @thm-subspace-dimension. Let \( (\u_1, \dots, \u_n) \) be a basis of \( U \) (@cor-basis-existence). It is an independent list in \( V \) of length \( n = \dim V \), so it is a basis of \( V \) by @thm-right-size-basis (a). Hence \( V = \Span(\u_1, \dots, \u_n) \subseteq U \), where the inclusion is @thm-span-subspace (3) applied to the subspace \( U \). Since also \( U \subseteq V \), we get \( U = V \).
:::

This is the dimension version of "count instead of check": to prove two subspaces are equal, prove **one** inclusion and compare dimensions. It is usually much less work than proving both inclusions.

::: {.check}
Let \( U \) be a subspace of \( \nR[x]_{\le 2} \) that contains \( 1 \), \( 1 + x \) and \( (1 + x)^2 \). Must \( U = \nR[x]_{\le 2} \)?

::: {.solution}
Yes. By @exm-count-instead-of-check, \( (1, 1 + x, (1 + x)^2) \) is independent, and it lies in \( U \), so \( \dim U \ge 3 \) by @thm-size-bounds applied in \( U \) (which is finite-dimensional by @thm-subspace-dimension). Also \( \dim U \le \dim \nR[x]_{\le 2} = 3 \). So \( \dim U = 3 \), and @thm-dim-impl-eq gives \( U = \nR[x]_{\le 2} \).
:::
:::

::: {.warning}
Both hypotheses of @thm-dim-impl-eq matter. Containment is needed: the \( xy \)-plane and the \( xz \)-plane in \( \nR^3 \) both have dimension 2, but neither contains the other, and they are different. Without finite dimension it fails too. In \( F[x] \), the subspace \( U \) of polynomials with constant coefficient \( 0 \) has the basis-like list \( x, x^2, x^3, \dots \), which matches \( 1, x, x^2, \dots \) one for one; yet \( 1 \notin U \). Later in this chapter we make this precise for infinite-dimensional spaces.
:::

## Exercises

### A. Check your understanding

::: {#exr-dimension-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the Steinitz Exchange Theorem.
2. True or false: \( \dim \nR[x]_{\le 3} = 3 \). Justify your answer.
3. True or false: in a vector space of dimension \( 3 \), every spanning list of length \( 3 \) is a basis. Justify your answer.
4. True or false: \( M_2(\nR) \) contains a linearly independent list of length \( 5 \). Justify your answer.
5. True or false: if \( U \) and \( W \) are subspaces of \( \nR^4 \) with \( \dim U = \dim W = 2 \), then \( U = W \). Justify your answer.
6. What are \( \dim_\nC \nC^2 \) and \( \dim_\nR \nC^2 \)?
:::
:::

::: {.solution}
(a) See @thm-steinitz: if \( (\u_1, \dots, \u_m) \) is independent and \( (\w_1, \dots, \w_n) \) spans \( V \), then \( m \le n \), and after renumbering the \( \w \)'s, \( (\u_1, \dots, \u_m, \w_{m+1}, \dots, \w_n) \) spans \( V \).

(b) False. The basis \( (1, x, x^2, x^3) \) has length \( 4 \), so \( \dim \nR[x]_{\le 3} = 4 \).

(c) True, by @thm-right-size-basis (b).

(d) False. \( \dim M_2(\nR) = 4 \), and by @thm-size-bounds (a) every list of length \( 5 > 4 \) is dependent.

(e) False. The subspaces \( \Span(\e_1, \e_2) \) and \( \Span(\e_3, \e_4) \) both have dimension \( 2 \), but \( \e_1 \) lies in the first and not in the second. @thm-dim-impl-eq needs one subspace to be contained in the other.

(f) \( \dim_\nC \nC^2 = 2 \), with basis \( (\e_1, \e_2) \). Over \( \nR \), the list \( (\e_1, i\e_1, \e_2, i\e_2) \) is a basis: every \( (a + bi, c + di) \) with \( a, b, c, d \in \nR \) equals \( a\e_1 + b(i\e_1) + c\e_2 + d(i\e_2) \), and this is \( \0 \) only if \( a + bi = 0 \) and \( c + di = 0 \), that is, \( a = b = c = d = 0 \). So \( \dim_\nR \nC^2 = 4 \).
:::

### B. Practice

::: {#exr-dimension-b1}
[B1: Dimension and a Basis of a Subspace]

Find a basis and the dimension of each subspace.

::: {.enumerate options="label=(\alph*)"}
1. \( U_1 = \{ (x_1, x_2, x_3, x_4) \in \nR^4 : x_1 + x_2 = 0 \text{ and } x_3 - x_4 = 0 \} \).
2. \( U_2 = \{ A \in M_3(\nR) : \tr A = 0 \} \).
3. \( U_3 = \{ p \in \nR[x]_{\le 3} : p(1) = p(-1) = 0 \} \).
:::
:::

::: {.solution}
(a) A vector lies in \( U_1 \) exactly when \( x_2 = -x_1 \) and \( x_3 = x_4 \), that is, when it equals
\[
(x_1, -x_1, x_4, x_4) = x_1(1, -1, 0, 0) + x_4(0, 0, 1, 1).
\]
So \( ((1, -1, 0, 0), (0, 0, 1, 1)) \) spans \( U_1 \). It is independent: \( a(1, -1, 0, 0) + b(0, 0, 1, 1) = (a, -a, b, b) = \0 \) forces \( a = b = 0 \). Hence it is a basis, and \( \dim U_1 = 2 \).

(b) Write \( A = (a_{ij}) \). The condition \( a_{11} + a_{22} + a_{33} = 0 \) says \( a_{33} = -a_{11} - a_{22} \), so
\[
A = \sum_{i \ne j} a_{ij}E_{ij} + a_{11}(E_{11} - E_{33}) + a_{22}(E_{22} - E_{33}).
\]
All eight matrices on the right have trace \( 0 \), so the list of the six \( E_{ij} \) with \( i \ne j \), followed by \( E_{11} - E_{33} \) and \( E_{22} - E_{33} \), spans \( U_2 \). For independence, let \( \sum_{i \ne j} c_{ij}E_{ij} + d_1(E_{11} - E_{33}) + d_2(E_{22} - E_{33}) = 0 \). The entry \( (i, j) \) with \( i \ne j \) of the left side is \( c_{ij} \), the entry \( (1, 1) \) is \( d_1 \), and the entry \( (2, 2) \) is \( d_2 \); all must be \( 0 \). Hence the list is a basis, and \( \dim U_2 = 8 \).

(c) Let \( p = a_0 + a_1x + a_2x^2 + a_3x^3 \). Then \( p(1) = a_0 + a_1 + a_2 + a_3 \) and \( p(-1) = a_0 - a_1 + a_2 - a_3 \). Adding and subtracting, \( p \in U_3 \) exactly when \( a_0 + a_2 = 0 \) and \( a_1 + a_3 = 0 \). Hence \( p \in U_3 \) exactly when
\[
p = -a_2 - a_3x + a_2x^2 + a_3x^3 = a_2(x^2 - 1) + a_3(x^3 - x).
\]
So \( (x^2 - 1, x^3 - x) \) spans \( U_3 \). It is independent: \( a(x^2 - 1) + b(x^3 - x) = 0 \) has \( x^3 \)-coefficient \( b \) and \( x^2 \)-coefficient \( a \), so \( a = b = 0 \). Hence it is a basis, and \( \dim U_3 = 2 \).
:::

::: {#exr-dimension-b2}
[B2: Extending to a Basis of \( \nR^4 \)]

Show that \( ((1, 1, 0, 0), (0, 1, 1, 0)) \) is linearly independent, and extend it to a basis of \( \nR^4 \) using vectors from the standard basis.
:::

::: {.solution}
Let \( \u_1 = (1, 1, 0, 0) \) and \( \u_2 = (0, 1, 1, 0) \). If \( a\u_1 + b\u_2 = (a, a + b, b, 0) = \0 \), then \( a = b = 0 \), so the list is independent. By @thm-basis-extension, two standard basis vectors complete it; we sift \( (\u_1, \u_2, \e_1, \e_2, \e_3, \e_4) \) to find which.

- \( \u_1 \ne \0 \): keep. \( \u_2 \notin \Span(\u_1) \), since a multiple \( (a, a, 0, 0) \) of \( \u_1 \) has third entry \( 0 \): keep.
- \( \e_1 \): if \( (a, a + b, b, 0) = (1, 0, 0, 0) \), then \( a = 1 \) and \( b = 0 \), but then \( a + b = 1 \ne 0 \). So \( \e_1 \notin \Span(\u_1, \u_2) \): keep.
- \( \e_2 = \u_1 - \e_1 \): discard.
- \( \e_3 = -\u_1 + \u_2 + \e_1 \), since \( -(1, 1, 0, 0) + (0, 1, 1, 0) + (1, 0, 0, 0) = (0, 0, 1, 0) \): discard.
- \( \e_4 \): every combination of \( \u_1, \u_2, \e_1 \) has fourth entry \( 0 \): keep.

The sifted list \( (\u_1, \u_2, \e_1, \e_4) \) is independent by @thm-sift. It has \( 4 = \dim \nR^4 \) entries, so it is a basis of \( \nR^4 \) by @thm-right-size-basis (a).
:::

::: {#exr-dimension-b3}
[B3: Count Instead of Check]

Show that \( (1, \; x - 1, \; (x - 1)^2) \) is a basis of \( \nR[x]_{\le 2} \). Hence find the coordinate vector of \( x^2 \) with respect to this basis.
:::

::: {.solution}
Let \( a + b(x - 1) + c(x - 1)^2 = 0 \). Expanding, \( (a - b + c) + (b - 2c)x + cx^2 = 0 \). Comparing coefficients, \( c = 0 \), then \( b = 2c = 0 \), then \( a = b - c = 0 \). So the list is independent, with \( 3 = \dim \nR[x]_{\le 2} \) elements, and it is a basis by @thm-right-size-basis (a).

Writing \( x = (x - 1) + 1 \),
\[
x^2 = \big((x - 1) + 1\big)^2 = 1 + 2(x - 1) + (x - 1)^2.
\]
Hence the coordinate vector of \( x^2 \) is \( (1, 2, 1) \).
:::

### C. Going deeper

::: {#exr-dimension-c1}
[C1: Symmetric and Skew-Symmetric Matrices]

Let \( n \ge 1 \). For a field \( F \), let \( U_+ \) and \( U_- \) be the subspaces of symmetric and of skew-symmetric matrices in \( M_n(F) \) (@def-symmetric-matrix): \( U_+ = \{ A : A\tp = A \} \) and \( U_- = \{ A : A\tp = -A \} \).

::: {.enumerate options="label=(\alph*)"}
1. For \( F = \nR \), prove that \( \dim U_+ = \frac{n(n + 1)}{2} \).
2. For \( F = \nR \), prove that \( \dim U_- = \frac{n(n - 1)}{2} \).
3. For \( F = \nF_2 \), show that \( U_- = U_+ \), and find its dimension. Which step of (b) fails?
:::
:::

::: {.solution}
(a) Consider the list \( \sS \) consisting of \( E_{ii} \) for \( 1 \le i \le n \) and \( E_{ij} + E_{ji} \) for \( 1 \le i < j \le n \). Each is symmetric. If \( A = (a_{ij}) \) is symmetric, then \( a_{ji} = a_{ij} \), so
\[
A = \sum_{i} a_{ii}E_{ii} + \sum_{i < j} a_{ij}(E_{ij} + E_{ji}),
\]
because both sides have \( a_{ij} \) in entry \( (i, j) \) and \( a_{ij} = a_{ji} \) in entry \( (j, i) \). So \( \sS \) spans \( U_+ \). If \( \sum_i c_{ii}E_{ii} + \sum_{i < j} c_{ij}(E_{ij} + E_{ji}) = 0 \), then for \( i \le j \) the entry \( (i, j) \) of the left side is \( c_{ij} \), so every coefficient is \( 0 \). Hence \( \sS \) is a basis, of length \( n + \frac{n(n - 1)}{2} = \frac{n(n + 1)}{2} \).

(b) If \( A\tp = -A \), then comparing diagonal entries gives \( a_{ii} = -a_{ii} \), so \( 2a_{ii} = 0 \), and \( a_{ii} = 0 \) because \( 2 \ne 0 \) in \( \nR \). Off the diagonal, \( a_{ji} = -a_{ij} \). Hence
\[
A = \sum_{i < j} a_{ij}(E_{ij} - E_{ji}).
\]
Each \( E_{ij} - E_{ji} \) is skew-symmetric, so these matrices span \( U_- \), and as in (a) the entry \( (i, j) \) with \( i < j \) of a combination is its coefficient, so they are independent. There are \( \frac{n(n - 1)}{2} \) pairs \( i < j \), so \( \dim U_- = \frac{n(n - 1)}{2} \).

(c) In \( \nF_2 \), \( -1 = 1 \), so \( -A = A \) for every matrix \( A \), and the conditions \( A\tp = -A \) and \( A\tp = A \) coincide. Hence \( U_- = U_+ \) over \( \nF_2 \), which has dimension \( \frac{n(n + 1)}{2} \) by the argument of (a), which works over any field. The step of (b) that fails is "\( 2a_{ii} = 0 \) implies \( a_{ii} = 0 \)", which divides by \( 2 = 0 \). For example, \( I_n \in U_- \) over \( \nF_2 \), although its diagonal entries are not \( 0 \).
:::

::: {#exr-dimension-c2}
[C2: A complex space viewed over the reals]

Let \( V \) be a vector space over \( \nC \) with \( \dim_\nC V = n \). Restricting the scalars to real numbers makes \( V \) a vector space over \( \nR \). Prove that \( \dim_\nR V = 2n \).

*Hint: start from a basis \( (\v_1, \dots, \v_n) \) over \( \nC \), and consider the vectors \( i\v_k \).*
:::

::: {.solution}
Let \( (\v_1, \dots, \v_n) \) be a basis of \( V \) over \( \nC \). We show that \( \sB = (\v_1, i\v_1, \dots, \v_n, i\v_n) \) is a basis of \( V \) over \( \nR \).

*Spanning.* Let \( \v \in V \). Then \( \v = \sum_k z_k\v_k \) with \( z_k \in \nC \). Write \( z_k = a_k + b_ki \) with \( a_k, b_k \in \nR \). By the distributive and associative axioms of scalar multiplication, \( z_k\v_k = a_k\v_k + (b_ki)\v_k = a_k\v_k + b_k(i\v_k) \). Hence \( \v = \sum_k \big(a_k\v_k + b_k(i\v_k)\big) \), a real combination of \( \sB \).

*Independence.* Let \( \sum_k \big(a_k\v_k + b_k(i\v_k)\big) = \0 \) with \( a_k, b_k \in \nR \). Reading the same axioms backwards, \( \sum_k (a_k + b_ki)\v_k = \0 \). Since \( (\v_1, \dots, \v_n) \) is independent over \( \nC \), every \( a_k + b_ki = 0 \), so \( a_k = b_k = 0 \).

Hence \( \sB \) is a basis over \( \nR \) of length \( 2n \), and \( \dim_\nR V = 2n \).
:::

::: {#exr-dimension-c3}
[C3: Counting Elements over a Finite Field]

Let \( p \) be a prime.

::: {.enumerate options="label=(\alph*)"}
1. Let \( V \) be a vector space over \( \nF_p \) with \( \dim V = k \). Prove that \( V \) has exactly \( p^k \) elements.
2. Deduce that no vector space over \( \nF_2 \) has exactly \( 6 \) elements.
3. Let \( K \) be a finite field that contains \( \nF_p \), with the same addition and multiplication. Explain why \( K \) is a finite-dimensional vector space over \( \nF_p \), and deduce that \( K \) has \( p^k \) elements for some integer \( k \ge 1 \).
:::

*Hint: for (a), use coordinates.*
:::

::: {.solution}
(a) Let \( \sB \) be a basis of \( V \), of length \( k \). By @thm-coordinates-linear, \( \v \mapsto \coord{\v}{\sB} \) is a bijection from \( V \) to \( \nF_p^k \): every column is the coordinate vector of exactly one vector. So \( V \) has as many elements as \( \nF_p^k \). A column in \( \nF_p^k \) is a choice of \( k \) entries, each from the \( p \) elements of \( \nF_p \), so there are \( p^k \) columns. Hence \( V \) has \( p^k \) elements.

(b) A vector space over \( \nF_2 \) with finitely many elements is spanned by the finite list of all its elements, so it is finite-dimensional, of some dimension \( k \). By (a) it has \( 2^k \) elements. Since \( 6 \) is not a power of \( 2 \), no such space has \( 6 \) elements.

(c) Define scalar multiplication \( \nF_p \times K \to K \) by the multiplication of \( K \). The vector space axioms are then instances of the field axioms of \( K \): addition in \( K \) is commutative and associative with zero and negatives, multiplication is associative, \( 1 \cdot a = a \), and multiplication distributes over addition. So \( K \) is a vector space over \( \nF_p \). It is spanned by the finite list of all its elements, so it is finite-dimensional; let \( k = \dim_{\nF_p} K \). By (a), \( K \) has \( p^k \) elements. Since \( K \) contains \( 0 \ne 1 \), it is not the zero space, so \( k \ge 1 \).
:::
