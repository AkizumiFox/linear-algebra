# Orthonormal Bases and Gram–Schmidt

A basis lets us write every vector in coordinates, but finding those coordinates costs work: in @def-coordinates the scalars \( a_1, \dots, a_n \) come from solving a linear system. In an inner product space one kind of basis makes that cost disappear. If the basis vectors are mutually orthogonal unit vectors, then the \( i \)-th coordinate of \( \v \) is just \( \inner{\v}{\e_i} \), one inner product, computed without reference to the others. This section defines such bases, shows that every finite-dimensional inner product space has one, and gives the algorithm that produces them.

## Orthonormal lists

The standard basis of \( \nR^n \) has two features beyond being a basis: distinct vectors are orthogonal, and each has length \( 1 \). The two conditions can be packed into a single formula using the Kronecker delta \( \delta_{ij} \), which is \( 1 \) when \( i = j \) and \( 0 \) otherwise.

*An orthonormal list is a list of unit vectors that are pairwise perpendicular.*

::: {#def-orthonormal-list}
[Orthonormal List]

Let \( V \) be an inner product space. A list \( (\e_1, \dots, \e_k) \) of vectors of \( V \) is **orthonormal** if
\[
\inner{\e_i}{\e_j} = \delta_{ij} \qquad \text{for all } i, j \in \{1, \dots, k\},
\]
that is, if \( \inner{\e_i}{\e_j} = 0 \) whenever \( i \ne j \) (**orthogonal**) and \( \norm{\e_i} = 1 \) for every \( i \) (**normalized**).
:::

In words: the single equation \( \inner{\e_i}{\e_j} = \delta_{ij} \) carries two conditions at once, because the case \( i \ne j \) says the vectors are orthogonal and the case \( i = j \) says \( \norm{\e_i}^2 = 1 \). The list must be **ordered**, as every list in this book is, but nothing in the definition depends on the order. Note that no vector of an orthonormal list is \( \0 \), since \( \norm{\0} = 0 \ne 1 \); so by @thm-orthogonal-independent, **every orthonormal list is linearly independent**. That single sentence is why orthonormality is so useful: independence, which normally takes an argument, comes for free.

::: {#def-orthonormal-basis}
[Orthonormal Basis]

An **orthonormal basis** of an inner product space \( V \) is an orthonormal list that is a basis of \( V \).
:::

**Examples.**

- **The standard basis.** In \( F^n \) with the standard inner product, \( \inner{\e_i}{\e_j} = \delta_{ij} \) by inspection. This is the model, and the notation \( \e_i \) is deliberately reused for orthonormal vectors in a general space.
- **A rotated basis of \( \nR^2 \).** The list \( \big(\tfrac{1}{\sqrt2}(1, 1),\ \tfrac{1}{\sqrt2}(1, -1)\big) \) is orthonormal: the inner product of the two vectors is \( \tfrac12(1 - 1) = 0 \), and each has norm \( \tfrac{1}{\sqrt2}\sqrt{2} = 1 \). Geometrically it is the standard basis turned through \( \pi/4 \).
- **A basis of \( \nR^3 \).** The columns of \( \tfrac13\begin{pmatrix} 1 & 2 & 2 \\ 2 & 1 & -2 \\ 2 & -2 & 1 \end{pmatrix} \) form an orthonormal list: each has norm \( \tfrac13\sqrt{1 + 4 + 4} = 1 \), and the three pairwise inner products are \( \tfrac19(2 + 2 - 4) \), \( \tfrac19(2 - 4 + 2) \) and \( \tfrac19(4 - 2 - 2) \), all \( 0 \). Being independent and of length \( 3 = \dim \nR^3 \), it is a basis (@thm-right-size-basis (a)).
- **Matrix units.** In \( M_{m \times n}(F) \) with the Frobenius inner product, the matrix units \( \E_{ij} \) satisfy \( \inner{\E_{ij}}{\E_{pq}} = 1 \) if \( (i, j) = (p, q) \) and \( 0 \) otherwise, since only one entry of each is non-zero. So the standard basis of \( M_{m \times n}(F) \) is orthonormal.
- **The Lagrange basis.** On \( F[x]_{\le n} \) with the node inner product \( \inner{p}{q} = \sum_{i=0}^{n} p(c_i)\conj{q(c_i)} \) of the previous section, the Lagrange polynomials \( \ell_0, \dots, \ell_n \) of @def-lagrange-basis vanish at every node but their own, where they take the value \( 1 \); that is, \( \ell_i(c_j) = \delta_{ij} \). Hence \( \inner{\ell_i}{\ell_j} = \sum_{k} \ell_i(c_k)\conj{\ell_j(c_k)} = \delta_{ij} \): the Lagrange basis is an orthonormal basis for this inner product. An interpolation formula and an orthonormal expansion turn out to be the same statement.
- **The degenerate case.** The empty list is orthonormal, vacuously, and it is an orthonormal basis of \( V = \{\0\} \). This is not a joke: it is the base case of every induction below.

**Non-example by minimal change.** In \( \nR^2 \), the list \( ((1, 1), (1, -1)) \) is orthogonal, and it is a basis. It is **not** orthonormal, because \( \norm{(1,1)} = \sqrt2 \ne 1 \). The failure is only in the normalization, and it is repaired by dividing each vector by its norm, which changes neither the spans nor the orthogonality (@thm-norm-properties (b)). Scaling is always available; orthogonality is the real content.

## Coordinates in an orthonormal basis

Here is the payoff promised in the opening.

::: {#thm-orthonormal-coordinates}
[Coordinates, Inner Products and Norms in an Orthonormal Basis]

Let \( (\e_1, \dots, \e_n) \) be an orthonormal basis of an inner product space \( V \), and let \( \u, \v \in V \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \displaystyle \v = \sum_{i=1}^{n} \inner{\v}{\e_i}\,\e_i \);
2. \( \displaystyle \inner{\u}{\v} = \sum_{i=1}^{n} \inner{\u}{\e_i}\,\conj{\inner{\v}{\e_i}} \);
3. \( \displaystyle \norm{\v}^2 = \sum_{i=1}^{n} \lvert \inner{\v}{\e_i} \rvert^2 \)  (**Parseval's identity** for a finite orthonormal basis).
:::
:::

::: {.idea}
For (a) we already know that \( \v = \sum a_i\e_i \) for unique scalars \( a_i \); the only question is what they are. Pair both sides with \( \e_j \): orthonormality kills every term except the \( j \)-th, and that one survives with coefficient \( 1 \). Parts (b) and (c) then follow by expanding, since the coordinates are now known.
:::

::: {.proof}
(a) Since \( (\e_1, \dots, \e_n) \) is a basis, @thm-unique-representation gives scalars \( a_1, \dots, a_n \in F \) with \( \v = \sum_i a_i\e_i \). Fix \( j \). Pairing with \( \e_j \) and using (IP1),
\[
\inner{\v}{\e_j} = \sum_{i=1}^{n} a_i\inner{\e_i}{\e_j} = \sum_{i=1}^{n} a_i\delta_{ij} = a_j ,
\]
by @def-orthonormal-list. So \( a_j = \inner{\v}{\e_j} \) for every \( j \), which is (a).

(b) Write \( \u = \sum_i \inner{\u}{\e_i}\e_i \) and \( \v = \sum_j \inner{\v}{\e_j}\e_j \) by (a). Expanding the first slot with (IP1) and the second with @thm-inner-product-basic-properties (b),
\[
\inner{\u}{\v} = \sum_{i}\sum_{j} \inner{\u}{\e_i}\,\conj{\inner{\v}{\e_j}}\,\inner{\e_i}{\e_j} .
\]
Only the terms with \( i = j \) survive, and there \( \inner{\e_i}{\e_i} = 1 \). This is (b).

(c) Take \( \u = \v \) in (b): the \( i \)-th term becomes \( \inner{\v}{\e_i}\conj{\inner{\v}{\e_i}} = \lvert\inner{\v}{\e_i}\rvert^2 \) by @thm-conjugate-properties (c), and the left side is \( \norm{\v}^2 \).
:::

Read (b) again: in the coordinates supplied by an orthonormal basis, **every** inner product becomes the standard inner product of \( F^n \). So an orthonormal basis does not merely simplify coordinates; it turns an abstract inner product space into \( F^n \) with the dot product. We record that as a corollary below, and use it repeatedly: **to make an abstract statement concrete, fix an orthonormal basis.**

::: {#exm-orthonormal-coordinates-r3}
[Reading Off Coordinates]

Let \( \e_1 = \tfrac13(1, 2, 2) \), \( \e_2 = \tfrac13(2, 1, -2) \), \( \e_3 = \tfrac13(2, -2, 1) \), the orthonormal basis of \( \nR^3 \) found above. Write \( \v = (3, 0, 3) \) in this basis, and check Parseval's identity.
:::

::: {.solution}
By @thm-orthonormal-coordinates (a), the coordinates are
\[
\begin{aligned}
\inner{\v}{\e_1} &= \tfrac13(3 + 0 + 6) = 3, \\
\inner{\v}{\e_2} &= \tfrac13(6 + 0 - 6) = 0, \\
\inner{\v}{\e_3} &= \tfrac13(6 + 0 + 3) = 3 ,
\end{aligned}
\]
so \( \v = 3\e_1 + 0\e_2 + 3\e_3 \). No system was solved. Checking directly, \( 3\e_1 + 3\e_3 = (1, 2, 2) + (2, -2, 1) = (3, 0, 3) \). For Parseval, \( \norm{\v}^2 = 9 + 0 + 9 = 18 \), and indeed \( 3^2 + 0^2 + 3^2 = 18 \).
:::

::: {.check}
With the same \( \e_1, \e_2, \e_3 \), find the coordinates of \( \v = (1, 1, 1) \) and verify Parseval's identity.
:::

::: {.solution}
\( \inner{\v}{\e_1} = \tfrac13(1 + 2 + 2) = \tfrac53 \), \( \inner{\v}{\e_2} = \tfrac13(2 + 1 - 2) = \tfrac13 \), \( \inner{\v}{\e_3} = \tfrac13(2 - 2 + 1) = \tfrac13 \). Then \( \tfrac{25}{9} + \tfrac19 + \tfrac19 = \tfrac{27}{9} = 3 = \norm{\v}^2 \), as Parseval requires.
:::

## The Gram–Schmidt process

Everything so far assumed that an orthonormal basis was handed to us. Does one always exist? The answer is yes in finite dimension, and the proof is an algorithm that we will use constantly.

The idea comes from a picture in \( \nR^3 \). Given independent \( \v_1, \v_2 \), normalize \( \v_1 \) to get \( \e_1 \). The vector \( \v_2 \) is generally not perpendicular to \( \e_1 \); but its "shadow" on the line through \( \e_1 \) is the multiple \( \inner{\v_2}{\e_1}\e_1 \), and subtracting the shadow leaves a vector \( \w_2 \) perpendicular to \( \e_1 \). Normalize it. Then repeat with \( \v_3 \), subtracting its shadows on both \( \e_1 \) and \( \e_2 \).

\begin{center}
\begin{tikzpicture}[scale=1.4, arr/.style={->, thick}]
  \draw[arr] (0,0) -- (3,0) node[below right] {$\mathbf{v}_1$};
  \draw[arr] (0,0) -- (2,1.7) node[above right] {$\mathbf{v}_2$};
  \draw[arr, gray, thick] (0,0) -- (2,0);
  \node[below, gray] at (1.0,-0.08) {$\langle \mathbf{v}_2, \mathbf{e}_1 \rangle \mathbf{e}_1$};
  \draw[arr, dashed] (2,0) -- (2,1.7);
  \node[right] at (2.05,0.85) {$\mathbf{w}_2 = \mathbf{v}_2 - \langle \mathbf{v}_2, \mathbf{e}_1 \rangle \mathbf{e}_1$};
  \draw (1.82,0) -- (1.82,0.18) -- (2,0.18);
  \fill (1,0) circle (1.3pt);
  \node[above left] at (1.0,0.0) {$\mathbf{e}_1$};
\end{tikzpicture}
\end{center}

Project, subtract, normalize. The right angle at the foot is the only thing that has to be checked, and one line of algebra checks it.

::: {#thm-gram-schmidt}
[Gram–Schmidt Process]

Let \( V \) be an inner product space and let \( (\v_1, \dots, \v_m) \) be a **linearly independent** list in \( V \). Define recursively
\[
\w_k = \v_k - \sum_{i=1}^{k-1} \inner{\v_k}{\e_i}\,\e_i , \qquad
\e_k = \frac{\w_k}{\norm{\w_k}} \qquad (k = 1, \dots, m).
\]
Then every \( \w_k \) is non-zero, so the recursion is defined, and:

::: {.enumerate options="label=(\alph*)"}
1. \( (\e_1, \dots, \e_m) \) is an orthonormal list;
2. \( \Span(\e_1, \dots, \e_k) = \Span(\v_1, \dots, \v_k) \) for every \( k = 1, \dots, m \);
3. if \( (\v_1, \dots, \v_r) \) is already orthonormal for some \( r \le m \), then \( \e_i = \v_i \) for \( i \le r \).
:::

In particular, every finite-dimensional inner product space has an orthonormal basis.
:::

::: {.idea}
Induction on \( k \), with the statement "\( (\e_1, \dots, \e_k) \) is orthonormal and spans \( \Span(\v_1, \dots, \v_k) \)" as the hypothesis. Two things need care. First, \( \w_k \ne \0 \): if it were \( \0 \), then \( \v_k \) would lie in \( \Span(\e_1, \dots, \e_{k-1}) = \Span(\v_1, \dots, \v_{k-1}) \), contradicting independence. That is the only place independence is used, and it is used exactly there. Second, \( \w_k \perp \e_j \) for \( j < k \): pair and watch the sum collapse.
:::

::: {.proof}
We prove by induction on \( k \) that \( \w_k \ne \0 \), that \( (\e_1, \dots, \e_k) \) is orthonormal, and that \( \Span(\e_1, \dots, \e_k) = \Span(\v_1, \dots, \v_k) \).

*Base case \( k = 1 \).* The empty sum is \( \0 \), so \( \w_1 = \v_1 \), which is non-zero because a list containing \( \0 \) is dependent. Then \( \e_1 = \v_1/\norm{\v_1} \) has norm \( 1 \) by @thm-norm-properties (b), and \( \Span(\e_1) = \Span(\v_1) \) since each vector is a non-zero multiple of the other.

*Induction step.* Let \( 2 \le k \le m \) and suppose the claim holds for \( k - 1 \). Put \( U = \Span(\e_1, \dots, \e_{k-1}) = \Span(\v_1, \dots, \v_{k-1}) \).

First, \( \w_k \ne \0 \). If \( \w_k = \0 \), then \( \v_k = \sum_{i<k}\inner{\v_k}{\e_i}\e_i \in U = \Span(\v_1, \dots, \v_{k-1}) \), so \( \v_k \) would be a linear combination of the earlier \( \v_i \), making \( (\v_1, \dots, \v_m) \) dependent, contrary to hypothesis. Hence \( \norm{\w_k} > 0 \) and \( \e_k \) is defined, with \( \norm{\e_k} = 1 \).

Next, \( \e_k \perp \e_j \) for every \( j < k \). By (IP1) and the induction hypothesis \( \inner{\e_i}{\e_j} = \delta_{ij} \),
\[
\inner{\w_k}{\e_j} = \inner{\v_k}{\e_j} - \sum_{i=1}^{k-1}\inner{\v_k}{\e_i}\,\delta_{ij} = \inner{\v_k}{\e_j} - \inner{\v_k}{\e_j} = 0 ,
\]
and \( \e_k \) is a scalar multiple of \( \w_k \), so \( \inner{\e_k}{\e_j} = 0 \) as well. Together with the induction hypothesis, \( (\e_1, \dots, \e_k) \) is orthonormal, which is (a).

For (b), \( \e_k \) is a linear combination of \( \v_k \) and \( \e_1, \dots, \e_{k-1} \), hence lies in \( \Span(\v_1, \dots, \v_k) \) by the induction hypothesis; so \( \Span(\e_1, \dots, \e_k) \subseteq \Span(\v_1, \dots, \v_k) \). Conversely \( \v_k = \norm{\w_k}\e_k + \sum_{i<k}\inner{\v_k}{\e_i}\e_i \in \Span(\e_1, \dots, \e_k) \), and the earlier \( \v_i \) lie there by the induction hypothesis. The two spans are equal, completing the induction.

For (c), suppose \( (\v_1, \dots, \v_r) \) is orthonormal and that \( \e_i = \v_i \) for all \( i < k \), where \( k \le r \). Then \( \inner{\v_k}{\e_i} = \inner{\v_k}{\v_i} = 0 \) for \( i < k \), so \( \w_k = \v_k \) and \( \norm{\w_k} = 1 \), giving \( \e_k = \v_k \). Induction on \( k \) proves (c).

Finally, let \( V \) be finite-dimensional. If \( V = \{\0\} \), the empty list is an orthonormal basis. Otherwise take any basis \( (\v_1, \dots, \v_n) \) of \( V \) and apply the process: by (a) the output is orthonormal, and by (b) it spans \( \Span(\v_1, \dots, \v_n) = V \), so it is an orthonormal basis.
:::

Two remarks on the formulas. The vector subtracted from \( \v_k \) is exactly the expansion of \( \v_k \) in the orthonormal basis \( (\e_1, \dots, \e_{k-1}) \) of \( U \), which by @thm-orthonormal-coordinates (a) is the best available "copy of \( \v_k \) inside \( U \)"; the next section will call it the orthogonal projection of \( \v_k \) onto \( U \). And the subtraction is the same move that produced the vector \( \z \) in the proof of @thm-cauchy-schwarz. **Project, then subtract** is one move used twice.

::: {#cor-extend-orthonormal-basis}
[Extending an Orthonormal List]

Let \( V \) be a finite-dimensional inner product space and let \( (\e_1, \dots, \e_r) \) be an orthonormal list in \( V \). Then there are vectors \( \e_{r+1}, \dots, \e_n \in V \) such that \( (\e_1, \dots, \e_n) \) is an orthonormal basis of \( V \).
:::

::: {.proof}
The list \( (\e_1, \dots, \e_r) \) is linearly independent by @thm-orthogonal-independent, since its vectors are orthogonal and non-zero. By @thm-basis-extension there are \( \v_{r+1}, \dots, \v_n \in V \) making \( (\e_1, \dots, \e_r, \v_{r+1}, \dots, \v_n) \) a basis of \( V \). Apply @thm-gram-schmidt to that basis. By part (c) the first \( r \) output vectors are \( \e_1, \dots, \e_r \) unchanged, and by (a) and (b) the whole output is an orthonormal basis of \( V \).
:::

## Two worked examples

::: {#exm-gram-schmidt-r3}
[Gram–Schmidt in \( \nR^3 \)]

Apply the Gram–Schmidt process of @thm-gram-schmidt to \( \v_1 = (1, 1, 1) \), \( \v_2 = (0, 1, 1) \), \( \v_3 = (0, 0, 1) \) in \( \nR^3 \) with the dot product.
:::

::: {.solution}
*Step 1.* \( \norm{\v_1}^2 = 3 \), so \( \e_1 = \tfrac{1}{\sqrt3}(1, 1, 1) \).

*Step 2.* \( \inner{\v_2}{\e_1} = \tfrac{1}{\sqrt3}(0 + 1 + 1) = \tfrac{2}{\sqrt3} \), so
\[
\w_2 = (0, 1, 1) - \tfrac{2}{3}(1, 1, 1) = \tfrac13(-2, 1, 1).
\]
Then \( \norm{\w_2}^2 = \tfrac19(4 + 1 + 1) = \tfrac23 \), and \( \e_2 = \tfrac{1}{\sqrt6}(-2, 1, 1) \).

*Step 3.* \( \inner{\v_3}{\e_1} = \tfrac{1}{\sqrt3} \) and \( \inner{\v_3}{\e_2} = \tfrac{1}{\sqrt6} \), so
\[
\w_3 = (0, 0, 1) - \tfrac13(1, 1, 1) - \tfrac16(-2, 1, 1) = \big(0, -\tfrac12, \tfrac12\big).
\]
Then \( \norm{\w_3}^2 = \tfrac12 \) and \( \e_3 = \tfrac{1}{\sqrt2}(0, -1, 1) \).

*Check.* The three vectors have norm \( 1 \), and \( \inner{\e_1}{\e_2} = \tfrac{1}{\sqrt{18}}(-2 + 1 + 1) = 0 \), \( \inner{\e_1}{\e_3} = \tfrac{1}{\sqrt6}(0 - 1 + 1) = 0 \), \( \inner{\e_2}{\e_3} = \tfrac{1}{\sqrt{12}}(0 - 1 + 1) = 0 \). The span condition is visible too: \( \e_1 \) is a multiple of \( \v_1 \), and \( \e_2 \) is a combination of \( \v_1 \) and \( \v_2 \).
:::

The next example runs the same three steps in a function space, where no picture is available and only the algebra is left.

::: {#exm-gram-schmidt-legendre}
[Gram–Schmidt on \( 1, x, x^2 \)]

Apply the Gram–Schmidt process of @thm-gram-schmidt to \( (1, x, x^2) \) in \( \nR[x]_{\le 2} \) with
\[
\inner{p}{q} = \int_{-1}^{1} p(t)q(t)\,\dd t .
\]
:::

::: {.solution}
*Step 1.* \( \norm{1}^2 = \int_{-1}^1 1\,\dd t = 2 \), so \( \e_1 = 1/\sqrt2 \).

*Step 2.* \( \inner{x}{\e_1} = \tfrac{1}{\sqrt2}\int_{-1}^1 t\,\dd t = 0 \), since the integrand is odd. So \( \w_2 = x \), and \( \norm{x}^2 = \int_{-1}^1 t^2\,\dd t = \tfrac23 \), giving \( \e_2 = \sqrt{3/2}\,x \).

*Step 3.* \( \inner{x^2}{\e_1} = \tfrac{1}{\sqrt2}\cdot\tfrac23 \) and \( \inner{x^2}{\e_2} = \sqrt{3/2}\int_{-1}^1 t^3\,\dd t = 0 \), again by oddness. Hence
\[
\w_3 = x^2 - \tfrac{1}{\sqrt2}\cdot\tfrac23\cdot\tfrac{1}{\sqrt2} = x^2 - \tfrac13 .
\]
Its squared norm is
\[
\int_{-1}^{1}\Big(t^2 - \tfrac13\Big)^2\,\dd t = \tfrac25 - \tfrac49 + \tfrac29 = \tfrac{8}{45},
\]
so \( \e_3 = \tfrac{\sqrt{10}}{4}(3x^2 - 1) \).

The monic polynomials produced along the way are \( 1 \), \( x \) and \( x^2 - \tfrac13 \). These are, up to scaling, the first three **Legendre polynomials**; the usual normalization takes \( P_2 = \tfrac12(3x^2 - 1) = \tfrac32(x^2 - \tfrac13) \), fixed by the convention \( P_k(1) = 1 \) rather than by the norm. Section 10 of this chapter takes up such families in general.
:::

Notice how much work the oddness of the integrand did: two of the three inner products were \( 0 \) before any computation. Symmetry of the weight is worth looking for.

::: {.warning}
**Gram–Schmidt depends on the order of the list.** Run the process on \( ((0,1), (1,1)) \) in \( \nR^2 \): it returns \( ((0,1), (1,0)) \). Run it on \( ((1,1), (0,1)) \), the same two vectors in the other order: it returns \( \big(\tfrac{1}{\sqrt2}(1,1), \tfrac{1}{\sqrt2}(-1,1)\big) \). Both outputs are orthonormal bases of \( \nR^2 \), and they are different. An orthonormal basis is never unique (for \( \dim V \ge 1 \) one can always replace \( \e_1 \) by \( -\e_1 \)); the process returns **an** orthonormal basis adapted to the given order, not **the** orthonormal basis.
:::

::: {.check}
Run Gram–Schmidt on \( ((1, 0), (1, 1)) \) in \( \nR^2 \), and then on \( ((1, 1), (1, 0)) \). Do you get the same list?
:::

::: {.solution}
First order: \( \e_1 = (1, 0) \); \( \inner{(1,1)}{\e_1} = 1 \), so \( \w_2 = (1,1) - (1,0) = (0,1) \) and \( \e_2 = (0,1) \). Output \( ((1,0), (0,1)) \).

Second order: \( \e_1 = \tfrac{1}{\sqrt2}(1,1) \); \( \inner{(1,0)}{\e_1} = \tfrac{1}{\sqrt2} \), so \( \w_2 = (1,0) - \tfrac12(1,1) = \tfrac12(1,-1) \) and \( \e_2 = \tfrac{1}{\sqrt2}(1,-1) \). Output \( \big(\tfrac{1}{\sqrt2}(1,1), \tfrac{1}{\sqrt2}(1,-1)\big) \). Not the same list, and not even the same set of lines.
:::

::: {.warning}
**The classical process is numerically fragile.** Computed with rounding, the vectors \( \e_1, \e_2, \dots \) drift out of orthogonality, and the drift grows with \( k \) and with how nearly dependent the input list is. Nothing above is wrong — the fault is in the arithmetic, not the mathematics — but in practice one uses a rearranged version or reflections instead. Section 8 of this chapter gives the reflection-based method, and Chapter 23 explains why it is the stable one.
:::

## All inner product spaces of the same dimension look alike

::: {#cor-inner-product-spaces-isomorphic}
[Classification of Finite-Dimensional Inner Product Spaces]

Let \( V \) be an inner product space over \( F \) with \( \dim V = n \). Then there is an isomorphism \( T \colon V \to F^n \) with
\[
\inner{T\u}{T\v} = \inner{\u}{\v} \qquad \text{for all } \u, \v \in V ,
\]
where the right-hand inner product is that of \( V \) and the left-hand one is the standard inner product of \( F^n \). An isomorphism with this property is an **isometric isomorphism**, so every \( n \)-dimensional inner product space over \( F \) is isometrically isomorphic to \( F^n \).
:::

::: {.proof}
By @thm-gram-schmidt, \( V \) has an orthonormal basis \( \sE = (\e_1, \dots, \e_n) \). Let \( T \colon V \to F^n \) be the coordinate map \( T\v = \coord{\v}{\sE} \), an isomorphism by @cor-coordinate-isomorphism. By @thm-orthonormal-coordinates (a), the \( i \)-th entry of \( T\v \) is \( \inner{\v}{\e_i} \). Hence the standard inner product of \( T\u \) and \( T\v \) in \( F^n \) is \( \sum_i \inner{\u}{\e_i}\conj{\inner{\v}{\e_i}} \), which equals \( \inner{\u}{\v} \) by @thm-orthonormal-coordinates (b).
:::

So dimension is a complete invariant of finite-dimensional inner product spaces over a fixed field: there is nothing to classify. This should be compared with @thm-isomorphic-iff-same-dimension, which said the same for vector spaces; adding an inner product adds no new invariant. What becomes interesting is the interaction of the inner product with a given operator, and that is the subject of Chapter 11. Isometries in general are the subject of Section 7 of this chapter.

## Gram matrices

Given a list of vectors, all of its inner products can be collected into one matrix, and that matrix turns out to answer questions about the list.

::: {#def-gram-matrix}
[Gram Matrix]

Let \( (\v_1, \dots, \v_k) \) be a list in an inner product space \( V \) over \( F \). Its **Gram matrix** is \( \G \in M_k(F) \) with entries
\[
(\G)_{ij} = \inner{\v_j}{\v_i} \qquad (1 \le i, j \le k).
\]
:::

The order of the subscripts looks backwards and is chosen on purpose: it makes \( \G \) act on coefficient vectors the right way round, as part (b) below shows. For a real list the distinction disappears, since then \( \inner{\v_j}{\v_i} = \inner{\v_i}{\v_j} \).

For example, the Gram matrix of \( ((1,1,0), (1,0,1), (0,1,1)) \) in \( \nR^3 \) is \( \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix} \), with the squared norms on the diagonal.

Over \( \nC \) the order of the subscripts becomes visible. For \( \v_1 = (1, 0) \) and \( \v_2 = (i, 1) \) in \( \nC^2 \), the off-diagonal entries are
\[
(\G)_{12} = \inner{\v_2}{\v_1} = i, \qquad (\G)_{21} = \inner{\v_1}{\v_2} = \conj{i} = -i,
\]
so \( \G = \begin{pmatrix} 1 & i \\ -i & 2 \end{pmatrix} \), which is Hermitian but not symmetric. Part (b) below says \( \x^{*}\G\x = \norm{x_1\v_1 + x_2\v_2}^2 \); with \( \x = (1, 1) \) both sides are \( 3 \), since \( \v_1 + \v_2 = (1 + i, 1) \). Writing \( (\G)_{ij} = \inner{\v_i}{\v_j} \) instead would transpose \( \G \) and leave that identity reading \( \x^{*}\G\tp\x \).

::: {#thm-gram-matrix-properties}
[Properties of the Gram Matrix]

Let \( (\v_1, \dots, \v_k) \) be a list in an inner product space \( V \) over \( F \), with Gram matrix \( \G \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \G \) is **Hermitian**, \( \G^{*} = \G \), and its diagonal entries are the real numbers \( \norm{\v_i}^2 \ge 0 \);
2. \( \x^{*}\G\x = \big\lVert \textstyle\sum_{j} x_j\v_j \big\rVert^2 \) for every \( \x \in F^k \);
3. \( \G \) is invertible if and only if \( (\v_1, \dots, \v_k) \) is linearly independent;
4. \( \det \G \) is a real number with \( \det \G \ge 0 \), and \( \det \G > 0 \) exactly when the list is linearly independent.
:::
:::

::: {.idea}
Part (b) is the whole theorem: the quadratic expression \( \x^{*}\G\x \) is a squared length, so it vanishes only for the coefficient vectors of genuine dependence relations. That identifies \( \nul(\G) \) with the set of dependence relations and gives (c) at once. For (d), fix an orthonormal basis of the span and write \( \G = \A^{*}\A \) for a coordinate matrix \( \A \); a determinant of that shape is a squared modulus.
:::

::: {.proof}
(a) By (IP2), \( (\G^{*})_{ij} = \conj{(\G)_{ji}} = \conj{\inner{\v_i}{\v_j}} = \inner{\v_j}{\v_i} = (\G)_{ij} \). The diagonal entries are \( \inner{\v_i}{\v_i} = \norm{\v_i}^2 \), real and \( \ge 0 \) by @thm-inner-product-basic-properties (a).

(b) Write \( \u = \sum_j x_j\v_j \). Expanding by (IP1) and @thm-inner-product-basic-properties (b),
\[
\norm{\u}^2 = \sum_{i}\sum_{j} x_j\conj{x_i}\inner{\v_j}{\v_i}
= \sum_{i}\conj{x_i}\sum_{j}(\G)_{ij}x_j ,
\]
and the right-hand side is exactly the entry of the \( 1 \times 1 \) matrix \( \x^{*}\G\x \).

(c) We show \( \nul(\G) = \{\x \in F^k : \sum_j x_j\v_j = \0\} \). If \( \sum_j x_j\v_j = \0 \), then for each \( i \), \( (\G\x)_i = \sum_j \inner{\v_j}{\v_i}x_j = \inner{\sum_j x_j\v_j}{\v_i} = 0 \) by (IP1), so \( \G\x = \0 \). Conversely, if \( \G\x = \0 \), then \( \x^{*}\G\x = 0 \), so \( \lVert\sum_j x_j\v_j\rVert = 0 \) by (b) and hence \( \sum_j x_j\v_j = \0 \) by @thm-norm-properties (a). Now \( \G \) is invertible if and only if \( \G\x = \0 \) forces \( \x = \0 \) (@thm-invertible-tfae, (a) \( \Leftrightarrow \) (b)), which by the displayed equality of sets says exactly that the only dependence relation among the \( \v_j \) is the trivial one.

(d) Let \( U = \Span(\v_1, \dots, \v_k) \), let \( r = \dim U \), and let \( (\e_1, \dots, \e_r) \) be an orthonormal basis of \( U \), which exists by @thm-gram-schmidt. Let \( \A \in M_{r \times k}(F) \) have as its \( j \)-th column the coordinate vector of \( \v_j \), so that \( \v_j = \sum_p a_{pj}\e_p \). By @thm-orthonormal-coordinates (b),
\[
(\G)_{ij} = \inner{\v_j}{\v_i} = \sum_{p=1}^{r} a_{pj}\conj{a_{pi}} = (\A^{*}\A)_{ij},
\]
so \( \G = \A^{*}\A \).

If the list is dependent, then \( \G \) is singular by (c) and \( \det \G = 0 \). If it is independent, then \( r = k \) and \( \A \) is square. By @thm-det-transpose, \( \det(\A^{*}) = \det(\conj{\A}) \), and \( \det(\conj{\A}) = \conj{\det \A} \), because by the Leibniz formula (@thm-leibniz-formula-alternating) the determinant is a sum of products of entries and conjugation preserves sums and products (@thm-conjugate-properties). Hence, by @thm-det-multiplicative,
\[
\det \G = \det(\A^{*})\det(\A) = \conj{\det\A}\,\det\A = \lvert\det\A\rvert^2 .
\]
This is real and \( \ge 0 \), and it is \( > 0 \) because \( \A \) is the matrix of an isomorphism onto its coordinates, hence invertible with \( \det \A \ne 0 \) (@thm-det-nonzero-iff-invertible).
:::

Over \( \nR \), with \( V = \nR^n \) and the dot product, part (d) is the statement Chapter 6 reached from Cauchy–Binet: @cor-gram-determinant-nonnegative says that \( \det(\A\A\tp) \ge 0 \) for a real \( \A \), with equality exactly when the rows of \( \A \) are dependent. Taking the rows of \( \A \) to be \( \v_1, \dots, \v_k \) makes \( \A\A\tp \) the Gram matrix, so that corollary is the special case of (d) in which the ambient space is \( \nR^n \). The pointer left there is now paid: a Gram matrix is exactly a matrix of pairwise inner products, and its determinant is non-negative for that reason.

::: {#exm-gram-independence}
[Deciding Independence with a Gram Matrix]

Decide whether \( ((1,1,0), (1,0,1), (0,1,-1)) \) is independent in \( \nR^3 \), using its Gram matrix.
:::

::: {.solution}
The pairwise dot products give
\[
\G = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & -1 \\ 1 & -1 & 2 \end{pmatrix},
\]
and expanding along the first row, \( \det \G = 2(4 - 1) - 1(2 + 1) + 1(-1 - 2) = 6 - 3 - 3 = 0 \). By @thm-gram-matrix-properties (d) the list is dependent. Indeed \( \G\x = \0 \) for \( \x = (1, -1, -1) \), and @thm-gram-matrix-properties (c) says this is a dependence relation: \( (1,1,0) - (1,0,1) - (0,1,-1) = \0 \).
:::

Two features of this method are worth noting. It never needs coordinates in the ambient space, so it works verbatim for polynomials and functions, where writing the vectors as columns is not an option. And the answer comes with a witness: a null vector of \( \G \) is a dependence relation, ready to read off.

## Exercises

### A. Check your understanding

:::: {#exr-orthonormal-bases-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define an orthonormal list, using the Kronecker delta, and say what an orthonormal basis is.
2. Why is every orthonormal list linearly independent? Name the result used.
3. Write down the coordinates of \( \v \) in an orthonormal basis \( (\e_1, \dots, \e_n) \), and state Parseval's identity.
4. True or false: the Gram–Schmidt process (@thm-gram-schmidt) applied to a list and to the same list in reverse order produces the same orthonormal list. Justify your answer.
5. State the criterion for linear independence in terms of the Gram matrix.
6. True or false: every \( 3 \)-dimensional real inner product space is isometrically isomorphic to \( \nR^3 \) with the dot product. Justify your answer.
:::
::::

::: {.solution}
(a) A list \( (\e_1, \dots, \e_k) \) with \( \inner{\e_i}{\e_j} = \delta_{ij} \) for all \( i, j \) (@def-orthonormal-list); an orthonormal basis is such a list that is also a basis (@def-orthonormal-basis).

(b) Its vectors are pairwise orthogonal and non-zero (each has norm \( 1 \)), so @thm-orthogonal-independent applies.

(c) \( \v = \sum_i \inner{\v}{\e_i}\e_i \), and \( \norm{\v}^2 = \sum_i \lvert\inner{\v}{\e_i}\rvert^2 \) (@thm-orthonormal-coordinates).

(d) False. On \( ((0,1),(1,1)) \) the process returns \( ((0,1),(1,0)) \), while on \( ((1,1),(0,1)) \) it returns \( \big(\tfrac{1}{\sqrt2}(1,1), \tfrac{1}{\sqrt2}(-1,1)\big) \).

(e) The list is independent if and only if its Gram matrix is invertible, if and only if \( \det \G > 0 \) (@thm-gram-matrix-properties (c), (d)).

(f) True. By @cor-inner-product-spaces-isomorphic, the coordinate map with respect to any orthonormal basis is an isometric isomorphism onto \( \nR^3 \).
:::

### B. Practice

:::: {#exr-orthonormal-bases-b1}
[B1: Gram–Schmidt with numbers]

Apply the Gram–Schmidt process of @thm-gram-schmidt to each list, with the dot product.

::: {.enumerate options="label=(\alph*)"}
1. \( ((1,0,1), (1,1,0), (0,1,1)) \) in \( \nR^3 \).
2. \( ((1,1,0,0), (1,0,1,0), (0,0,1,1)) \) in \( \nR^4 \).
:::
::::

::: {.solution}
(a) \( \norm{(1,0,1)}^2 = 2 \), so \( \e_1 = \tfrac{1}{\sqrt2}(1,0,1) \). Next \( \inner{(1,1,0)}{\e_1} = \tfrac{1}{\sqrt2} \), so
\[
\w_2 = (1,1,0) - \tfrac12(1,0,1) = \tfrac12(1, 2, -1),
\]
with \( \norm{\w_2}^2 = \tfrac14 \cdot 6 = \tfrac32 \), giving \( \e_2 = \tfrac{1}{\sqrt6}(1, 2, -1) \). Finally \( \inner{(0,1,1)}{\e_1} = \tfrac{1}{\sqrt2} \) and \( \inner{(0,1,1)}{\e_2} = \tfrac{1}{\sqrt6} \), so
\[
\w_3 = (0,1,1) - \tfrac12(1,0,1) - \tfrac16(1,2,-1) = \tfrac23(-1, 1, 1),
\]
with \( \norm{\w_3}^2 = \tfrac49 \cdot 3 = \tfrac43 \), giving \( \e_3 = \tfrac{1}{\sqrt3}(-1, 1, 1) \).

(b) \( \e_1 = \tfrac{1}{\sqrt2}(1,1,0,0) \). Then \( \inner{(1,0,1,0)}{\e_1} = \tfrac{1}{\sqrt2} \), so
\[
\w_2 = (1,0,1,0) - \tfrac12(1,1,0,0) = \tfrac12(1,-1,2,0),
\]
with \( \norm{\w_2}^2 = \tfrac14 \cdot 6 = \tfrac32 \) and \( \e_2 = \tfrac{1}{\sqrt6}(1,-1,2,0) \). Finally \( \inner{(0,0,1,1)}{\e_1} = 0 \) and \( \inner{(0,0,1,1)}{\e_2} = \tfrac{2}{\sqrt6} \), so
\[
\w_3 = (0,0,1,1) - \tfrac13(1,-1,2,0) = \tfrac13(-1,1,1,3),
\]
with \( \norm{\w_3}^2 = \tfrac19 \cdot 12 = \tfrac43 \) and \( \e_3 = \tfrac{1}{2\sqrt3}(-1,1,1,3) \).
:::

:::: {#exr-orthonormal-bases-b2}
[B2: Gram–Schmidt on polynomials]

In \( \nR[x]_{\le 2} \) with \( \inner{p}{q} = \int_{0}^{1} p(t)q(t)\,\dd t \), apply the Gram–Schmidt process of @thm-gram-schmidt to \( (1, x, x^2) \). Compare the monic outputs with those of @exm-gram-schmidt-legendre and explain the difference.
::::

::: {.solution}
\( \norm{1}^2 = 1 \), so \( \e_1 = 1 \). Then \( \inner{x}{1} = \int_0^1 t\,\dd t = \tfrac12 \), so \( \w_2 = x - \tfrac12 \) and
\[
\norm{\w_2}^2 = \int_0^1 \Big(t - \tfrac12\Big)^2\,\dd t = \tfrac13 - \tfrac12 + \tfrac14 = \tfrac{1}{12},
\]
giving \( \e_2 = \sqrt3\,(2x - 1) \). Next \( \inner{x^2}{\e_1} = \tfrac13 \) and
\[
\inner{x^2}{\e_2} = \sqrt3\int_0^1 (2t^3 - t^2)\,\dd t = \sqrt3\Big(\tfrac12 - \tfrac13\Big) = \tfrac{\sqrt3}{6},
\]
so \( \w_3 = x^2 - \tfrac13 - \tfrac{\sqrt3}{6}\cdot\sqrt3(2x - 1) = x^2 - x + \tfrac16 \). Its squared norm is
\[
\int_0^1\Big(t^2 - t + \tfrac16\Big)^2\,\dd t = \tfrac{1}{180},
\]
so \( \e_3 = \sqrt5\,(6x^2 - 6x + 1) \).

The monic outputs are \( 1 \), \( x - \tfrac12 \), \( x^2 - x + \tfrac16 \), whereas on \( [-1, 1] \) they were \( 1 \), \( x \), \( x^2 - \tfrac13 \). Orthogonality is a property of the inner product, not of the polynomials: changing the interval changes which polynomials are orthogonal. These are the shifted Legendre polynomials, and the substitution \( t \mapsto 2t - 1 \) carries one family to the other.
:::

:::: {#exr-orthonormal-bases-b3}
[B3: Coordinates without solving a system]

Let \( \e_1 = \tfrac13(1,2,2) \), \( \e_2 = \tfrac13(2,1,-2) \), \( \e_3 = \tfrac13(2,-2,1) \) in \( \nR^3 \).

::: {.enumerate options="label=(\alph*)"}
1. Write \( \v = (1, -1, 4) \) in this basis.
2. Compute \( \norm{\v}^2 \) in two ways, and state which theorem says the answers agree.
3. Compute \( \inner{\v}{\u} \) for \( \u = (3, 0, 3) \) from the coordinates of \( \v \) and \( \u \), using @exm-orthonormal-coordinates-r3 for \( \u \).
:::
::::

::: {.solution}
(a) \( \inner{\v}{\e_1} = \tfrac13(1 - 2 + 8) = \tfrac73 \), \( \inner{\v}{\e_2} = \tfrac13(2 - 1 - 8) = -\tfrac73 \), \( \inner{\v}{\e_3} = \tfrac13(2 + 2 + 4) = \tfrac83 \). So \( \v = \tfrac73\e_1 - \tfrac73\e_2 + \tfrac83\e_3 \).

(b) Directly, \( \norm{\v}^2 = 1 + 1 + 16 = 18 \). From the coordinates, \( \tfrac{49}{9} + \tfrac{49}{9} + \tfrac{64}{9} = \tfrac{162}{9} = 18 \). They agree by @thm-orthonormal-coordinates (c).

(c) The coordinates of \( \u \) are \( (3, 0, 3) \) by @exm-orthonormal-coordinates-r3, so by @thm-orthonormal-coordinates (b),
\[
\inner{\v}{\u} = \tfrac73 \cdot 3 + \big(-\tfrac73\big)\cdot 0 + \tfrac83 \cdot 3 = 7 + 8 = 15 .
\]
Directly, \( \inner{\v}{\u} = 3 + 0 + 12 = 15 \).
:::

:::: {#exr-orthonormal-bases-b4}
[B4: Gram matrices]

For each list, write down the Gram matrix and use it to decide whether the list is independent.

::: {.enumerate options="label=(\alph*)"}
1. \( ((1,1,0), (1,0,1), (0,1,1)) \) in \( \nR^3 \) with the dot product.
2. \( ((1, i), (i, 1)) \) in \( \nC^2 \) with the standard inner product.
3. \( (1, x, x^2 - \tfrac13) \) in \( \nR[x]_{\le 2} \) with \( \inner{p}{q} = \int_{-1}^{1} pq \).
:::
::::

::: {.solution}
(a) \( \G = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix} \), and expanding along the first row, \( \det \G = 2(4 - 1) - 1(2 - 1) + 1(1 - 2) = 6 - 1 - 1 = 4 > 0 \). By @thm-gram-matrix-properties (d) the list is independent.

(b) \( \inner{(1,i)}{(1,i)} = 1 + 1 = 2 \) and \( \inner{(i,1)}{(1,i)} = i\conj{1} + 1\conj{i} = i - i = 0 \), so \( \G = 2\I_2 \) by @thm-gram-matrix-properties (a). Then \( \det \G = 4 > 0 \) and the list is independent; in fact it is orthogonal, so @thm-orthogonal-independent already gives the answer.

(c) These are the monic outputs of @exm-gram-schmidt-legendre, so they are pairwise orthogonal, and \( \G = \diag(2, \tfrac23, \tfrac{8}{45}) \). Its determinant is \( 2 \cdot \tfrac23 \cdot \tfrac{8}{45} = \tfrac{32}{135} > 0 \), so the list is independent. A Gram matrix is diagonal exactly when the list is orthogonal.
:::

### C. Going deeper

:::: {#exr-orthonormal-bases-c1}
[C1: The Gram matrix determines the list]

Let \( (\v_1, \dots, \v_k) \) be a list in an inner product space \( V \) and \( (\w_1, \dots, \w_k) \) a list in an inner product space \( W \), both over \( F \), with the **same** Gram matrix: \( \inner{\v_j}{\v_i} = \inner{\w_j}{\w_i} \) for all \( i, j \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \sum_j x_j\v_j = \0 \) if and only if \( \sum_j x_j\w_j = \0 \), for every \( \x \in F^k \).
2. Deduce that there is a well-defined isomorphism \( T \colon \Span(\v_1, \dots, \v_k) \to \Span(\w_1, \dots, \w_k) \) with \( T\v_j = \w_j \) for every \( j \).
3. Prove that \( T \) is an isometric isomorphism, that is, \( \inner{T\u}{T\u'} = \inner{\u}{\u'} \) for all \( \u, \u' \) in the domain.
:::
::::

::: {.solution}
(a) Let \( \G \) be the common Gram matrix. By @thm-gram-matrix-properties (b), \( \big\lVert\sum_j x_j\v_j\big\rVert^2 = \x^{*}\G\x = \big\lVert\sum_j x_j\w_j\big\rVert^2 \). By @thm-norm-properties (a), one side is \( 0 \) if and only if the other is, and a norm is \( 0 \) only at the zero vector.

(b) Every element of \( U = \Span(\v_1, \dots, \v_k) \) is \( \sum_j x_j\v_j \) for some \( \x \). Define \( T\big(\sum_j x_j\v_j\big) = \sum_j x_j\w_j \). This is well defined: if \( \sum_j x_j\v_j = \sum_j y_j\v_j \), then \( \sum_j (x_j - y_j)\v_j = \0 \), so \( \sum_j (x_j - y_j)\w_j = \0 \) by (a), that is \( \sum_j x_j\w_j = \sum_j y_j\w_j \). It is linear because the formula is linear in \( \x \), it is surjective onto \( \Span(\w_1, \dots, \w_k) \) by construction, and it is injective: if \( T(\sum x_j\v_j) = \0 \), then \( \sum x_j\w_j = \0 \), so \( \sum x_j\v_j = \0 \) by (a).

(c) Let \( \u = \sum_j x_j\v_j \) and \( \u' = \sum_i y_i\v_i \). Expanding by (IP1) and @thm-inner-product-basic-properties (b),
\[
\inner{\u}{\u'} = \sum_{i}\sum_{j} x_j\conj{y_i}\inner{\v_j}{\v_i} ,
\]
and the same computation in \( W \) gives \( \inner{T\u}{T\u'} = \sum_i\sum_j x_j\conj{y_i}\inner{\w_j}{\w_i} \). The two sums are equal term by term, since the Gram matrices agree.
:::

:::: {#exr-orthonormal-bases-c2}
[C2: Gram–Schmidt on a dependent list]

Let \( (\v_1, \dots, \v_m) \) be a list in an inner product space, **not** assumed independent, and run the recursion of @thm-gram-schmidt.

::: {.enumerate options="label=(\alph*)"}
1. Let \( k \) be the smallest index with \( \v_k \in \Span(\v_1, \dots, \v_{k-1}) \). Prove that the recursion is defined up to \( \e_{k-1} \) and that \( \w_k = \0 \), so the step \( \e_k = \w_k/\norm{\w_k} \) fails.
2. Repair the process: show that if, whenever \( \w_k = \0 \), we discard \( \v_k \) and continue with \( \v_{k+1} \), the output is an orthonormal basis of \( \Span(\v_1, \dots, \v_m) \).
3. Run the repaired process on \( ((1,1,0), (2,2,0), (1,0,1)) \) in \( \nR^3 \).
:::
::::

::: {.solution}
(a) The list \( (\v_1, \dots, \v_{k-1}) \) is independent, since a dependence among its members would, by @thm-linear-dependence-lemma, put some \( \v_j \) with \( j < k \) in the span of its predecessors, contradicting the minimality of \( k \). So @thm-gram-schmidt applies to it and produces \( \e_1, \dots, \e_{k-1} \) with \( \Span(\e_1, \dots, \e_{k-1}) = \Span(\v_1, \dots, \v_{k-1}) =: U \). Since \( \v_k \in U \), @thm-orthonormal-coordinates (a) applied inside \( U \) gives \( \v_k = \sum_{i<k}\inner{\v_k}{\e_i}\e_i \), which is precisely the vector subtracted, so \( \w_k = \0 \). Dividing by \( \norm{\w_k} = 0 \) is impossible.

(b) Let \( \e_1, \dots, \e_s \) be the vectors that the repaired process outputs. The proof of @thm-gram-schmidt shows, unchanged, that after processing \( \v_1, \dots, \v_k \) the accumulated list is orthonormal and spans \( \Span(\v_1, \dots, \v_k) \): the only step that used independence was the claim \( \w_k \ne \0 \), and in the repaired process a step with \( \w_k = \0 \) discards a \( \v_k \) that lies in the span already built, so the span does not change. Taking \( k = m \), the output is an orthonormal list spanning \( \Span(\v_1, \dots, \v_m) \), hence an orthonormal basis of it.

(c) \( \e_1 = \tfrac{1}{\sqrt2}(1,1,0) \). For \( \v_2 = (2,2,0) \): \( \inner{\v_2}{\e_1} = \tfrac{4}{\sqrt2} = 2\sqrt2 \), so \( \w_2 = (2,2,0) - 2\sqrt2 \cdot \tfrac{1}{\sqrt2}(1,1,0) = \0 \), and \( \v_2 \) is discarded. For \( \v_3 = (1,0,1) \): \( \inner{\v_3}{\e_1} = \tfrac{1}{\sqrt2} \), so \( \w_3 = (1,0,1) - \tfrac12(1,1,0) = \tfrac12(1,-1,2) \), with \( \norm{\w_3}^2 = \tfrac64 = \tfrac32 \) and \( \e_2 = \tfrac{1}{\sqrt6}(1,-1,2) \). The output \( \big(\tfrac{1}{\sqrt2}(1,1,0), \tfrac{1}{\sqrt6}(1,-1,2)\big) \) is an orthonormal basis of the plane spanned by the three given vectors.
:::
