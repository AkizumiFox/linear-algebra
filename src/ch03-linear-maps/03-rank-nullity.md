# The Rank–Nullity Theorem

The examples of the last section kept producing the same coincidence. Differentiation \( \nR[x]_{\le 3} \to \nR[x]_{\le 2} \) has a kernel of dimension \( 1 \) and an image of dimension \( 3 \), and \( 1 + 3 = 4 = \dim \nR[x]_{\le 3} \). The trace on \( M_2(\nR) \) gives \( 3 + 1 = 4 \) again. For matrices, Chapter 2 proved that \( \rank \A + \nullity \A \) is the number of columns (@thm-rank-nullity-matrix). This section proves the same equation for every linear map on a finite-dimensional space, with no matrices at all, and then turns it into the most useful counting tool of the chapter.

## Rank and nullity

The two numbers in the equation are dimensions of the two subspaces of @def-kernel and @def-image, so they are defined whenever those subspaces are finite-dimensional.

::: {#def-nullity}
[Nullity]

Let \( T \colon V \to W \) be a linear map with \( \ker T \) finite-dimensional. The **nullity** of \( T \) is \( \nullity T \coloneqq \dim \ker T \).
:::

::: {#def-rank}
[Rank]

Let \( T \colon V \to W \) be a linear map with \( \im T \) finite-dimensional. The **rank** of \( T \) is \( \rank T \coloneqq \dim \im T \).
:::

If \( V \) is finite-dimensional, both numbers are defined: \( \ker T \) is a subspace of \( V \), hence finite-dimensional (@thm-subspace-dimension), and \( \im T \) is finite-dimensional by @thm-image-spanned-by-basis-images. The nullity counts the independent directions that \( T \) destroys; the rank counts the independent directions that survive in the output.

::: {#exm-nullity-rank-diff}
[Rank and Nullity in Examples]

Find the nullity and rank of (a) differentiation \( D \colon \nR[x]_{\le 3} \to \nR[x]_{\le 2} \); (b) the matrix map \( T_\A \colon F^n \to F^m \) for \( \A \in M_{m \times n}(F) \); (c) the zero map and the identity on a space of dimension \( n \).
:::

::: {.solution}
(a) By @exm-differentiation-kernel-image, \( \ker D = \Span(1) \) and \( \im D = \nR[x]_{\le 2} \). So \( \nullity D = 1 \) and \( \rank D = 3 \).

(b) By @exm-kernel-image-matrix-map, \( \ker T_\A = \nul(\A) \) and \( \im T_\A = \col(\A) \). So \( \nullity T_\A = \dim \nul(\A) = \nullity \A \) and \( \rank T_\A = \dim \col(\A) = \rank \A \) (@def-nullity-matrix, @def-rank-matrix). The new names agree with the old ones.

(c) By @exm-kernel-image-degenerate, the zero map \( V \to V \) has nullity \( n \) and rank \( 0 \), and the identity has nullity \( 0 \) and rank \( n \).
:::

**A non-example.** The integration map \( J \colon \nR[x] \to \nR[x] \) of @exm-integration-kernel-image has nullity \( 0 \), but its image contains the independent list \( (x, x^2, \dots, x^k) \) for every \( k \), so the image is not finite-dimensional (@thm-size-bounds) and \( \rank J \) is not defined. What separates \( J \) from the examples above is that its domain is infinite-dimensional.

## The theorem

We want to prove that for every linear \( T \colon V \to W \) with \( V \) finite-dimensional,
\[
\dim \ker T + \dim \im T = \dim V .
\]
This is a dimension formula, so we look for the proof pattern that proved the last one, the Dimension Formula for Sums (@thm-dimension-formula-subspace-dim): take a basis of the **smallest** space, extend it, make a Big Claim about the vectors that were added, and count. Which space is the smallest? The kernel lives in \( V \) and the image lives in \( W \), different spaces that cannot be compared. The only inclusion available is \( \ker T \subseteq V \). So we start with a basis of \( \ker T \) and extend it to a basis of \( V \). The image has to be reached by applying \( T \), and the kernel vectors contribute nothing when we do. So the natural candidate for a basis of \( \im T \) is the images of the **added** vectors.

::: {#thm-rank-nullity}
[Rank–Nullity Theorem]

Let \( V \) be a **finite-dimensional** vector space, let \( W \) be any vector space over the same field, and let \( T \colon V \to W \) be linear. Then \( \ker T \) and \( \im T \) are finite-dimensional, and
\[
\nullity T + \rank T = \dim V .
\]
:::

\begin{center}
\begin{tikzpicture}[
    lab/.style={font=\small, align=center},
    arr/.style={->, thick, shorten >=2pt, shorten <=2pt}]
    \draw[thick, rounded corners=6pt] (0,0) rectangle (4,3.4);
    \node[lab] at (0.35,3.1) {$V$};
    \draw[thick, dashed, rounded corners=4pt] (0.3,0.3) rectangle (1.9,2.7);
    \node[lab] at (1.1,2.45) {$\ker T$};
    \node[lab] at (1.1,1.4) {$\u_1, \dots, \u_k$};
    \node[lab] at (3.0,1.4) {$\v_1, \dots, \v_r$};
    \node[lab] at (3.0,2.45) {added};
    \draw[thick, rounded corners=6pt] (7,0) rectangle (11,3.4);
    \node[lab] at (10.65,3.1) {$W$};
    \draw[thick, dashed, rounded corners=4pt] (8.2,0.9) rectangle (10.6,2.7);
    \node[lab] at (9.4,2.45) {$\im T$};
    \node[lab] at (9.4,1.5) {$T\v_1, \dots, T\v_r$};
    \node[lab] at (7.7,0.45) {$\0$};
    \draw[arr] (1.6,1.1) to[out=-30, in=180] (7.55,0.45);
    \draw[arr] (3.6,1.4) -- (8.3,1.5);
    \node[lab] at (5.5,1.8) {$T$};
    \node[lab] at (4.9,0.25) {$T$ kills the $\u$'s};
\end{tikzpicture}
\end{center}

::: {.idea}
The picture is the whole proof. The \( \u \)'s all go to \( \0 \); the \( \v \)'s carry everything else.

① Take a basis \( (\u_1, \dots, \u_k) \) of \( \ker T \), the smallest space in sight.
② Extend it to a basis \( (\u_1, \dots, \u_k, \v_1, \dots, \v_r) \) of \( V \) (Basis Extension).
③ **Big Claim:** \( (T\v_1, \dots, T\v_r) \) is a basis of \( \im T \). *Spanning:* apply \( T \) to a general vector of \( V \); the \( \u \)-terms die because they are in the kernel. *Independence:* the only way to use linearity is backwards, turning \( \sum b_jT\v_j = \0 \) into \( T(\sum b_j\v_j) = \0 \). Then \( \sum b_j\v_j \) is in the kernel, where the \( \u \)'s are a basis, and the big basis of \( V \) finishes it.
④ Count: \( \dim V = k + r = \nullity T + \rank T \).

This is the move of @thm-dimension-formula-subspace-dim: basis of the smallest space, extend, Big Claim, count. The new ingredient is that the Big Claim is about the **images** of the added vectors.
:::

::: {.proof}
**Step 1: bases.** By @thm-prop-kernel, \( \ker T \) is a subspace of \( V \). Since \( V \) is finite-dimensional, so is \( \ker T \) (@thm-subspace-dimension), and it has a basis \( (\u_1, \dots, \u_k) \) with \( k = \nullity T \) (@cor-basis-existence). This list is linearly independent in \( V \), so by the Basis Extension Theorem (@thm-basis-extension) there are \( \v_1, \dots, \v_r \in V \) such that \( (\u_1, \dots, \u_k, \v_1, \dots, \v_r) \) is a basis of \( V \). Thus \( \dim V = k + r \).

**Step 2: the Big Claim.**

::: {.claim}
The list \( (T\v_1, \dots, T\v_r) \) is a basis of \( \im T \).

::: {.proof}
*Spanning.* By @thm-image-spanned-by-basis-images applied to the basis of Step 1, \( \im T = \Span(T\u_1, \dots, T\u_k, T\v_1, \dots, T\v_r) \). Each \( T\u_i = \0 \), since \( \u_i \in \ker T \), and deleting a zero vector from a list does not change its span, because \( \0 \) lies in every span (@thm-span-absorb). Hence \( \im T = \Span(T\v_1, \dots, T\v_r) \).

*Independence.* Let \( b_1, \dots, b_r \in F \) satisfy \( b_1T\v_1 + \dots + b_rT\v_r = \0 \). By @thm-linear-combination, \( T(b_1\v_1 + \dots + b_r\v_r) = \0 \), so \( b_1\v_1 + \dots + b_r\v_r \in \ker T \). Since \( (\u_1, \dots, \u_k) \) spans \( \ker T \), there are \( a_1, \dots, a_k \in F \) with
\[
b_1\v_1 + \dots + b_r\v_r = a_1\u_1 + \dots + a_k\u_k .
\]
Rearranging, \( (-a_1)\u_1 + \dots + (-a_k)\u_k + b_1\v_1 + \dots + b_r\v_r = \0 \). This is a combination of the basis \( (\u_1, \dots, \u_k, \v_1, \dots, \v_r) \) of \( V \), which is linearly independent, so all its coefficients are \( 0 \). In particular \( b_1 = \dots = b_r = 0 \). Hence \( (T\v_1, \dots, T\v_r) \) is linearly independent.
:::
:::

**Step 3: count.** By the claim, \( \im T \) has a basis of length \( r \), so it is finite-dimensional with \( \rank T = r \) (@def-dimension). Therefore
\[
\nullity T + \rank T = k + r = \dim V ,
\]
as claimed.
:::

The proof reads correctly when \( k = 0 \) (injective \( T \): the \( \v \)'s are a basis of \( V \)) and when \( r = 0 \) (\( \ker T = V \): the claim says \( \im T \) has the empty basis). Notice what was **not** used: nothing about \( W \) beyond its being a vector space. The theorem counts only in the domain.

Applied to \( T_\A \colon F^n \to F^m \), where \( \nullity T_\A = \nullity \A \) and \( \rank T_\A = \rank \A \) (@exm-nullity-rank-diff), the theorem says \( \nullity \A + \rank \A = n \). This is @thm-rank-nullity-matrix again, now with a second proof. Chapter 2 counted free and pivot columns of a reduced matrix; here we counted basis vectors, and no row operation appeared. In particular, **the solution space of a homogeneous system \( \A\x = \0 \) in \( n \) unknowns has dimension \( n - \rank \A \)**, whatever method is used to find the rank.

In the online version you can test the count on any matrix map.

```{.python .run #cell-rank-nullity}
from sympy import Matrix

A = Matrix([
    [1, 2, 0, 3],
    [2, 4, 1, 8],
    [-1, -2, 1, -1],
])
rank = A.rank()                  # dim im T_A
nullity = len(A.nullspace())     # dim ker T_A: length of a basis of the kernel
print("rank =", rank, " nullity =", nullity, " dim of domain =", A.cols)
rank + nullity == A.cols
```

## Count instead of check

Rank–Nullity links the two questions of the last section. Injectivity is about the kernel, surjectivity about the image, and the theorem says the two dimensions add up to a fixed number. So one controls the other.

::: {#cor-rank-nullity-consequences}
[Consequences of Rank–Nullity]

Let \( V \) and \( W \) be finite-dimensional vector spaces over \( F \), and let \( T \colon V \to W \) be linear.

::: {.enumerate options="label=(\alph*)"}
1. \( T \) is injective if and only if \( \rank T = \dim V \).
2. \( T \) is surjective if and only if \( \rank T = \dim W \).
3. If \( \dim V > \dim W \), then \( T \) is **not** injective.
4. If \( \dim V < \dim W \), then \( T \) is **not** surjective.
5. If \( \dim V = \dim W \), then \( T \) is injective \( \iff \) \( T \) is surjective \( \iff \) \( T \) is bijective.
:::
:::

::: {.proof}
(a) By @thm-injective-iff-trivial-kernel, \( T \) is injective if and only if \( \ker T = \{\0\} \). A finite-dimensional space is \( \{\0\} \) exactly when its dimension is \( 0 \), because the empty list is a basis of \( \{\0\} \) and a basis of length \( 0 \) spans only \( \{\0\} \). So \( T \) is injective if and only if \( \nullity T = 0 \), which by @thm-rank-nullity means \( \rank T = \dim V \).

(b) If \( T \) is surjective, then \( \im T = W \) (@thm-prop-image), so \( \rank T = \dim W \). Conversely, if \( \rank T = \dim W \), then \( \im T \) is a subspace of \( W \) of the same dimension, so \( \im T = W \) by @thm-dim-impl-eq, and \( T \) is surjective.

(c) Since \( \im T \) is a subspace of \( W \), \( \rank T \le \dim W < \dim V \) by @thm-subspace-dimension. By (a), \( T \) is not injective.

(d) By @thm-rank-nullity, \( \rank T = \dim V - \nullity T \le \dim V < \dim W \). By (b), \( T \) is not surjective.

(e) If \( \dim V = \dim W \), then (a) and (b) have the same right-hand side, so \( T \) is injective if and only if it is surjective. Hence either property gives both, which is bijectivity; and bijective maps are injective by definition.
:::

Part (e) is the linear version of the pigeonhole principle for finite sets (@thm-finite-injective-iff-surjective), with dimension in place of the number of elements. It is a **count instead of check**: to show that a map between spaces of the same finite dimension is bijective, check **only** the kernel, usually the easier half, and let the count supply surjectivity. For \( T_\A \) with \( \A \) square, it is the equivalence of (b) and (e) in the Invertible Matrix Theorem (@thm-invertible-tfae). Parts (c) and (d) are the linear version of "no injection from a bigger finite set into a smaller one, and no surjection the other way".

::: {.warning}
**Both finiteness and equal dimension are needed.** Rank–Nullity requires \( V \) to be finite-dimensional; \( W \) may be anything, as for the inclusion \( \nR[x]_{\le 2} \to \nR[x] \), with nullity \( 0 \) and rank \( 3 \). Part (e) fails when the spaces are infinite-dimensional, even for an operator \( V \to V \): the right shift \( R \) on \( F^{\nN} \) is injective but not surjective, and the left shift \( L \) is surjective but not injective (@exm-shift-kernel-image). And the hypothesis \( \dim V = \dim W \) cannot be dropped: \( T(x, y) = (2x - y,\ x + y,\ x - y) \) from \( \nR^2 \) to \( \nR^3 \) is injective but not surjective.
:::

::: {.check}
Answer each question with a count.

::: {.enumerate options="label=(\alph*)"}
1. Can a linear map \( \nR^5 \to \nR^2 \) be injective?
2. Is there a linear map \( T \colon \nR^6 \to \nR^4 \) with \( \nullity T = 1 \)?
3. A linear operator \( T \) on \( \nR[x]_{\le 3} \) satisfies \( \ker T = \{0\} \). Must \( T \) be surjective?
:::
:::

::: {.solution}
(a) No, by @cor-rank-nullity-consequences (c): \( 5 > 2 \). Concretely, the rank is at most \( 2 \), so the nullity is at least \( 3 \).

(b) No. By @thm-rank-nullity the rank would be \( 6 - 1 = 5 \), but \( \im T \subseteq \nR^4 \) has dimension at most \( 4 \).

(c) Yes. The domain and codomain are both \( \nR[x]_{\le 3} \), of dimension \( 4 \), and \( T \) is injective, so it is surjective by @cor-rank-nullity-consequences (e).
:::

## Polynomial interpolation by counting

Chapter 2 proved that through \( n + 1 \) points with distinct \( x \)-values there passes exactly one polynomial of degree at most \( n \) (@thm-interpolation-unique). Existence for **all** data and uniqueness came together there because a square matrix was involved. Rank–Nullity gives the same result as a count, with no matrix written down.

::: {#exm-interpolation-by-counting}
[Interpolation as a Count]

Let \( x_0, \dots, x_n \in F \) be distinct, and define \( E \colon F[x]_{\le n} \to F^{n+1} \) by \( E(p) = \bigl(p(x_0), \dots, p(x_n)\bigr) \). Show that \( E \) is bijective, and deduce @thm-interpolation-unique.
:::

::: {.solution}
*Linear.* For \( p, q \in F[x]_{\le n} \) and \( c \in F \), @thm-evaluation-respects-operations gives \( (cp + q)(x_i) = c\,p(x_i) + q(x_i) \) in each entry, so \( E(cp + q) = cE(p) + E(q) \), and \( E \) is linear by @thm-equivalent-condition.

*Check the kernel.* If \( E(p) = \0 \), then \( p \) has the \( n + 1 \) distinct roots \( x_0, \dots, x_n \) while \( \deg p \le n \). A non-zero polynomial of degree at most \( n \) has at most \( n \) distinct roots (@lem-root-bound), so \( p = 0 \). Hence \( \ker E = \{0\} \), and \( E \) is injective (@thm-injective-iff-trivial-kernel).

*Count.* \( \dim F[x]_{\le n} = n + 1 \), since \( (1, x, \dots, x^n) \) is a basis (@exm-standard-bases), and \( \dim F^{n+1} = n + 1 \). By @cor-rank-nullity-consequences (e), \( E \) is bijective.

Surjectivity of \( E \) says that for every \( (y_0, \dots, y_n) \in F^{n+1} \) some \( p \in F[x]_{\le n} \) has \( p(x_i) = y_i \) for all \( i \); injectivity says there is only one. This is @thm-interpolation-unique.
:::

Compare the two arguments. Both prove uniqueness for the zero data from the root bound. Chapter 2 then invoked the Invertible Matrix Theorem for the Vandermonde matrix; here the count \( n + 1 = n + 1 \) does the same job. The proof of existence never constructs a polynomial. That is the price and the power of counting: it tells us a solution exists without saying what it is.

## Existence with conditions on derivatives

The same argument works when some conditions are on derivatives, where no Vandermonde matrix is at hand.

::: {#exm-hermite-existence}
[Prescribing Values and Slopes]

Show that for all \( a, b, c, d \in \nR \) there is **exactly one** \( p \in \nR[x]_{\le 3} \) with
\[
p(0) = a, \qquad p(1) = b, \qquad p'(0) = c, \qquad p'(1) = d .
\]
Hence find the cubic that rises from \( 0 \) at \( x = 0 \) to \( 1 \) at \( x = 1 \) with slope \( 0 \) at both ends.
:::

::: {.solution}
Define \( T \colon \nR[x]_{\le 3} \to \nR^4 \) by \( T(p) = \bigl(p(0),\ p(1),\ p'(0),\ p'(1)\bigr) \). Each entry is linear in \( p \): evaluation respects sums and scalar multiples (@thm-evaluation-respects-operations), and so does differentiation (@exm-differentiation). Hence \( T \) is linear by @thm-equivalent-condition.

*Kernel.* Let \( p = c_0 + c_1x + c_2x^2 + c_3x^3 \) with \( T(p) = \0 \). Then \( p(0) = c_0 = 0 \) and \( p'(0) = c_1 = 0 \). So \( p = c_2x^2 + c_3x^3 \), and the remaining conditions read
\[
p(1) = c_2 + c_3 = 0, \qquad p'(1) = 2c_2 + 3c_3 = 0 .
\]
Subtracting twice the first from the second gives \( c_3 = 0 \), and then \( c_2 = 0 \). Hence \( \ker T = \{0\} \).

*Count.* \( \dim \nR[x]_{\le 3} = 4 = \dim \nR^4 \), so \( T \) is bijective by @cor-rank-nullity-consequences (e). Surjectivity is existence for every \( (a, b, c, d) \), and injectivity is uniqueness.

For the data \( (0, 1, 0, 0) \), try \( p = \alpha x^2 + \beta x^3 \), which already has \( p(0) = p'(0) = 0 \). Then \( p(1) = \alpha + \beta = 1 \) and \( p'(1) = 2\alpha + 3\beta = 0 \) give \( \beta = -2 \) and \( \alpha = 3 \). So \( p = 3x^2 - 2x^3 \); by uniqueness it is the only such cubic.
:::

## Dimensions of subspaces cut out by conditions

Many subspaces are defined as "all vectors satisfying some linear conditions", which is to say as the kernel of a linear map. If the map is **surjective**, Rank–Nullity gives the dimension of the kernel at once, and surjectivity is often easy to see.

::: {#exm-dimension-by-surjective-map}
[Dimension of a Kernel from a Surjective Map]

Find the dimension of each subspace.

::: {.enumerate options="label=(\alph*)"}
1. The trace-free matrices \( U = \{ \A \in M_n(F) : \tr \A = 0 \} \) (@exm-trace-free-matrices).
2. \( U' = \{ p \in \nR[x]_{\le n} : \int_0^1 p(t)\,\dd t = 0 \} \).
:::
:::

::: {.solution}
(a) \( U = \ker \tr \), where \( \tr \colon M_n(F) \to F \) is linear (@exm-trace-matrices). Its image is a subspace of \( F \) (@thm-prop-image) containing \( \tr \E_{11} = 1 \), so it contains \( c \cdot 1 = c \) for every \( c \in F \); it is all of \( F \), and \( \rank \tr = 1 \). Since \( \dim M_n(F) = n^2 \) (@exm-standard-bases), @thm-rank-nullity gives \( \dim U = n^2 - 1 \).

(b) \( U' = \ker \psi \), where \( \psi \colon \nR[x]_{\le n} \to \nR \), \( \psi(p) = \int_0^1 p(t)\,\dd t \), is linear by @exr-linear-maps-b3 (b). Since \( \psi(1) = 1 \), the image is a subspace of \( \nR \) containing \( 1 \), hence all of \( \nR \), so \( \rank \psi = 1 \). By @thm-rank-nullity, \( \dim U' = (n + 1) - 1 = n \).
:::

Without the theorem, (a) needs an explicit basis of \( n^2 - 1 \) matrices together with a proof of independence and spanning. With it, one matrix of trace \( 1 \) is enough.

## Exercises

### A. Check your understanding

::: {#exr-rank-nullity-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the rank and the nullity of a linear map.
2. State the Rank–Nullity Theorem, with its hypotheses.
3. True or false: there is an injective linear map \( \nR^4 \to \nR^3 \). Justify your answer.
4. True or false: if \( V \) is finite-dimensional and \( T \colon V \to V \) is linear with \( \im T = V \), then \( T \) is injective. Justify your answer.
5. True or false: every injective linear map \( F^{\nN} \to F^{\nN} \) is surjective. Justify your answer.
6. Name the four steps of the proof of Rank–Nullity.
:::
:::

::: {.solution}
(a) See @def-nullity and @def-rank: \( \nullity T = \dim \ker T \) and \( \rank T = \dim \im T \), when these are finite-dimensional.

(b) See @thm-rank-nullity: if \( V \) is finite-dimensional and \( T \colon V \to W \) is linear, then \( \nullity T + \rank T = \dim V \).

(c) False. \( 4 > 3 \), so no linear map \( \nR^4 \to \nR^3 \) is injective (@cor-rank-nullity-consequences (c)).

(d) True. \( T \) is surjective, and its domain and codomain are the same finite-dimensional space, so \( T \) is injective by @cor-rank-nullity-consequences (e).

(e) False. The right shift \( R \) is injective but not surjective (@exm-shift-kernel-image). The count fails because \( F^{\nN} \) is not finite-dimensional.

(f) Take a basis of \( \ker T \); extend it to a basis of \( V \); prove the Big Claim that the images of the added vectors form a basis of \( \im T \) (spanning, then independence); count.
:::

### B. Practice

::: {#exr-rank-nullity-b1}
[B1: Verifying Rank–Nullity]

For each map, find a basis of the kernel and a basis of the image, and verify that \( \nullity T + \rank T = \dim V \).

::: {.enumerate options="label=(\alph*)"}
1. \( T_\C \colon \nR^4 \to \nR^3 \), where \( \C = \begin{pmatrix} 1 & 0 & 1 & 2 \\ 0 & 1 & 1 & -1 \\ 1 & 1 & 2 & 1 \end{pmatrix} \).
2. \( T \colon \nR[x]_{\le 3} \to \nR^2 \), \( T(p) = (p(0), p(1)) \).
3. \( T \colon M_2(\nR) \to M_2(\nR) \), \( T(\A) = \A + \A\tp \).
:::
:::

::: {.solution}
(a) Row reduce: \( R_3 - R_1 \) gives \( (0, 1, 1, -1) \), and then \( R_3 - R_2 \) gives a zero row, so
\[
\C \longrightarrow \begin{pmatrix} 1 & 0 & 1 & 2 \\ 0 & 1 & 1 & -1 \\ 0 & 0 & 0 & 0 \end{pmatrix},
\]
which is the RREF. The free columns are \( 3 \) and \( 4 \). By @thm-basis-null-space, \( \ker T_\C \) has basis \( \bigl((-1, -1, 1, 0),\ (-2, 1, 0, 1)\bigr) \). By @thm-basis-column-space, \( \im T_\C \) has basis \( \bigl((1, 0, 1),\ (0, 1, 1)\bigr) \). So \( 2 + 2 = 4 = \dim \nR^4 \).

(b) \( T \) is linear by @thm-evaluation-respects-operations. *Kernel:* for \( p = a_0 + a_1x + a_2x^2 + a_3x^3 \), \( T(p) = \0 \) means \( a_0 = 0 \) and \( a_1 + a_2 + a_3 = 0 \), that is, \( p = a_2(x^2 - x) + a_3(x^3 - x) \). The list \( (x^2 - x, x^3 - x) \) spans \( \ker T \), and it is independent by @thm-distinct-degrees-independent, so it is a basis. *Image:* \( T(1) = (1, 1) \) and \( T(x) = (0, 1) \) are independent, so they span a \( 2 \)-dimensional subspace of \( \nR^2 \), which is \( \nR^2 \) (@thm-dim-impl-eq). So \( \im T = \nR^2 \) with basis \( ((1, 1), (0, 1)) \). Hence \( 2 + 2 = 4 = \dim \nR[x]_{\le 3} \).

(c) \( T \) is linear because the transpose is (@exm-trace-matrices). *Kernel:* \( \A + \A\tp = 0 \) means \( a_{11} = a_{22} = 0 \) and \( a_{21} = -a_{12} \), so \( \ker T = \Span(\E_{12} - \E_{21}) \), with basis \( (\E_{12} - \E_{21}) \). *Image:* each \( \A + \A\tp \) is symmetric, since \( (\A + \A\tp)\tp = \A\tp + \A \), and each symmetric \( \B \) equals \( T(\tfrac12 \B) \). So \( \im T \) is the space of symmetric matrices, with basis \( (\E_{11}, \E_{22}, \E_{12} + \E_{21}) \) (as in @exr-kernel-image-b2). Hence \( 1 + 3 = 4 = \dim M_2(\nR) \).
:::

::: {#exr-rank-nullity-b2}
[B2: Bijective by the Kernel Alone]

Let \( n \ge 0 \) and \( T \colon \nR[x]_{\le n} \to \nR[x]_{\le n} \), \( T(p) = p + xp' \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( T \) is a linear map into \( \nR[x]_{\le n} \) and that \( \ker T = \{0\} \). Deduce that \( T \) is bijective.
2. Hence show that there is exactly one \( p \in \nR[x]_{\le 2} \) with \( p + xp' = 1 + x + x^2 \), and find it.
:::
:::

::: {.solution}
(a) For \( p = \sum_{k=0}^n a_kx^k \), \( xp' = \sum_{k=1}^n ka_kx^k \), so
\[
T(p) = \sum_{k=0}^n (1 + k)a_kx^k \in \nR[x]_{\le n} .
\]
Linearity: \( T(cp + q) = (cp + q) + x(cp' + q') = c(p + xp') + (q + xq') = cT(p) + T(q) \), using @exm-differentiation. If \( T(p) = 0 \), then \( (1 + k)a_k = 0 \) for each \( k \); since \( 1 + k \neq 0 \) in \( \nR \), every \( a_k = 0 \). So \( \ker T = \{0\} \), and \( T \) is injective (@thm-injective-iff-trivial-kernel). Domain and codomain have the same finite dimension \( n + 1 \), so \( T \) is bijective by @cor-rank-nullity-consequences (e).

(b) With \( n = 2 \), surjectivity gives a solution and injectivity makes it unique. By the formula in (a), \( T(a_0 + a_1x + a_2x^2) = a_0 + 2a_1x + 3a_2x^2 \), so we need \( a_0 = 1 \), \( 2a_1 = 1 \), \( 3a_2 = 1 \). Hence \( p = 1 + \tfrac12 x + \tfrac13 x^2 \). Check: \( xp' = \tfrac12 x + \tfrac23 x^2 \), and \( p + xp' = 1 + x + x^2 \).
:::

::: {#exr-rank-nullity-b3}
[B3: A Dimension via a Surjective Map]

Let \( U = \{ p \in \nR[x]_{\le 4} : p(1) = p(2) = 0 \} \). Use a surjective linear map to show that \( \dim U = 3 \). Hence find a basis of \( U \).
:::

::: {.solution}
Define \( T \colon \nR[x]_{\le 4} \to \nR^2 \), \( T(p) = (p(1), p(2)) \). It is linear by @thm-evaluation-respects-operations, and \( U = \ker T \). Its image contains \( T(1) = (1, 1) \) and \( T(x) = (1, 2) \), which are independent, so \( \im T \) is a \( 2 \)-dimensional subspace of \( \nR^2 \) and equals \( \nR^2 \) (@thm-dim-impl-eq). Thus \( \rank T = 2 \), and by @thm-rank-nullity, \( \dim U = 5 - 2 = 3 \).

The polynomials \( (x - 1)(x - 2) \), \( x(x - 1)(x - 2) \) and \( x^2(x - 1)(x - 2) \) vanish at \( 1 \) and \( 2 \) and have degrees \( 2, 3, 4 \le 4 \), so they lie in \( U \). They are non-zero of distinct degrees, hence independent (@thm-distinct-degrees-independent). There are \( 3 = \dim U \) of them, so they form a basis of \( U \) (@thm-right-size-basis).
:::

### C. Going deeper

::: {#exr-rank-nullity-c1}
[C1: A Lower Bound for the Rank of a Composite]

Let \( U \) and \( V \) be finite-dimensional, let \( W \) be a vector space, all over \( F \), and let \( T \colon U \to V \) and \( S \colon V \to W \) be linear. Write \( ST \) for the composite \( S \circ T \), which is linear (see the note before @exr-kernel-image-c1). Let \( S' \colon \im T \to W \) be the restriction of \( S \) to \( \im T \), that is, \( S'(\v) = S(\v) \) for \( \v \in \im T \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( S' \) is linear, that \( \im S' = \im(ST) \) and that \( \ker S' = \ker S \cap \im T \).
2. Deduce that \( \rank(ST) = \rank T - \dim(\ker S \cap \im T) \).
3. Hence prove **Sylvester's inequality**: \( \rank(ST) \ge \rank S + \rank T - \dim V \).
4. Deduce that \( \rank(\A\B) \ge \rank \A + \rank \B - n \) for \( \A \in M_{m \times n}(F) \) and \( \B \in M_{n \times p}(F) \).
:::

*Hint: for (c), compare \( \ker S \cap \im T \) with \( \ker S \).*
:::

::: {.solution}
(a) \( S' \) satisfies (LT1) and (LT2) because \( S \) does and \( \im T \) is a subspace (@thm-prop-image) with the operations of \( V \). A vector \( \w \) lies in \( \im S' \) exactly when \( \w = S(\v) \) with \( \v = T(\u) \) for some \( \u \in U \), that is, when \( \w = ST(\u) \); so \( \im S' = \im(ST) \). A vector \( \v \in \im T \) lies in \( \ker S' \) exactly when \( S(\v) = \0 \); so \( \ker S' = \ker S \cap \im T \).

(b) \( \im T \) is finite-dimensional with \( \dim \im T = \rank T \), since \( U \) is finite-dimensional (@thm-image-spanned-by-basis-images). By @thm-rank-nullity applied to \( S' \colon \im T \to W \) and by (a),
\[
\rank T = \dim \ker S' + \dim \im S' = \dim(\ker S \cap \im T) + \rank(ST).
\]

(c) \( \ker S \cap \im T \) is a subspace of \( \ker S \), so \( \dim(\ker S \cap \im T) \le \nullity S = \dim V - \rank S \), by @thm-subspace-dimension and @thm-rank-nullity for \( S \). Substituting into (b),
\[
\rank(ST) \ge \rank T - (\dim V - \rank S) = \rank S + \rank T - \dim V .
\]

(d) Take \( T = T_\B \colon F^p \to F^n \) and \( S = T_\A \colon F^n \to F^m \). By associativity (@thm-matrix-multiplication-properties), \( T_\A T_\B(\x) = \A(\B\x) = (\A\B)\x \), so \( ST = T_{\A\B} \). By @exm-nullity-rank-diff (b), ranks of matrix maps are ranks of matrices, and \( \dim F^n = n \). So (c) gives \( \rank(\A\B) \ge \rank \A + \rank \B - n \).
:::

::: {#exr-rank-nullity-c2}
[C2: When the Kernel Equals the Image]

Let \( V \) be finite-dimensional and \( T \colon V \to V \) linear with \( \ker T = \im T \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \dim V \) is even.
2. Give an example of such a \( T \) on \( \nR^2 \), and one on \( \nR^4 \).
3. Is there such a \( T \) on \( \nR^3 \)? Justify your answer.
:::
:::

::: {.solution}
(a) By @thm-rank-nullity, \( \dim V = \nullity T + \rank T = \dim \ker T + \dim \im T = 2\dim \im T \), which is even.

(b) On \( \nR^2 \), let \( T(x, y) = (y, 0) \). Then \( T(x, y) = \0 \) exactly when \( y = 0 \), so \( \ker T \) is the \( x \)-axis; and the outputs \( (y, 0) \) fill the \( x \)-axis, so \( \im T \) is the \( x \)-axis too. On \( \nR^4 \), let \( T(x_1, x_2, x_3, x_4) = (x_2, 0, x_4, 0) \). Its kernel is \( \{ x_2 = x_4 = 0 \} = \Span(\e_1, \e_3) \), and its image is \( \{ (a, 0, b, 0) \} = \Span(\e_1, \e_3) \). Both maps are matrix maps, hence linear.

(c) No. By (a), \( \dim V \) would be even, but \( \dim \nR^3 = 3 \).
:::
