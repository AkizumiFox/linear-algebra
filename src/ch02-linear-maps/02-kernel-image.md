# Kernel and Image

For any function, Chapter 0 asked two questions: is it injective, and is it surjective? For a function between sets, answering them means comparing outputs pair by pair and hunting for preimages point by point. For a linear map both questions reduce to a single subspace each. This section defines the two subspaces, the kernel and the image, shows how to compute them, and proves the test that makes injectivity cheap: a linear map is injective exactly when its kernel is zero.

## Two questions, two subspaces

Let \( T \colon V \to W \) be linear. Start with injectivity. Suppose two inputs collide, \( T(\u) = T(\v) \). By @thm-preserves-negation this is the same as
\[
T(\u - \v) = T(\u) - T(\v) = \0 .
\]
So a collision between \( \u \) and \( \v \) is the same thing as their difference being sent to \( \0 \). To detect every collision at once, it is enough to know **which vectors are sent to \( \0 \)**. For a general function this trick is unavailable, because there is no subtraction; linearity turns a question about all pairs into a question about one set.

Surjectivity asks whether every \( \w \in W \) is an output, so the set to know is **the set of all outputs**. For the matrix map \( T_\A(\x) = \A\x \) both sets are concrete: the outputs are the vectors \( \b \) for which \( \A\x = \b \) can be solved, and the inputs sent to \( \0 \) are the solutions of \( \A\x = \0 \). Chapter 3 computes both. The definitions below give the two sets a name for every linear map. They are defined for what they measure.

*The kernel is everything \( T \) sends to zero; the image is everything \( T \) reaches.*

::: {#def-kernel}
[Kernel]

Let \( T \colon V \to W \) be a linear map over \( F \). The **kernel** of \( T \) is the subset of the **domain**
\[
\ker T \coloneqq \{ \v \in V : T(\v) = \0_W \} \subseteq V .
\]
:::

::: {#def-image}
[Image]

Let \( T \colon V \to W \) be a linear map over \( F \). The **image** of \( T \) is the subset of the **codomain**
\[
\im T \coloneqq \{ T(\v) : \v \in V \} = \{ \w \in W : \w = T(\v) \text{ for some } \v \in V \} \subseteq W .
\]
:::

In words: a vector \( \v \) is in \( \ker T \) when \( \v \) lives in \( V \) **and** \( T \) sends it to the zero vector of \( W \). A vector \( \w \) is in \( \im T \) when \( \w \) lives in \( W \) **and** there **exists** at least one input with output \( \w \); the input need not be unique. In the language of @def-image-preimage, \( \ker T = T^{-1}(\{\0\}) \) is the preimage of the zero vector, and \( \im T = T(V) \) is the image of the function \( T \). The kernel is also called the **null space** of \( T \), and the image its **range**. For group homomorphisms, the kernel was defined the same way (@def-group-homomorphism), with \( \0 \) playing the role of the identity element.

There is nothing to check for well-definedness: both sets are described by conditions that either hold or fail. What does need checking is that they are **subspaces**, not just subsets.

::: {#thm-prop-kernel}
[The Kernel Is a Subspace]

Let \( T \colon V \to W \) be linear. Then \( \ker T \) is a subspace of \( V \).
:::

::: {.proof}
We use the Subspace Test (@thm-subspace-test).

(1) By @thm-zero-maps-to-zero, \( T(\0_V) = \0_W \), so \( \0_V \in \ker T \).

(2) Let \( \u, \v \in \ker T \), so \( T(\u) = T(\v) = \0_W \). By (LT1), \( T(\u + \v) = T(\u) + T(\v) = \0_W + \0_W = \0_W \). Therefore \( \u + \v \in \ker T \).

(3) Let \( \v \in \ker T \) and \( c \in F \). By (LT2), \( T(c\v) = cT(\v) = c\0_W = \0_W \), using @thm-scalar-zero-vector. Therefore \( c\v \in \ker T \).
:::

::: {#thm-prop-image}
[The Image Is a Subspace]

Let \( T \colon V \to W \) be linear. Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \im T \) is a subspace of \( W \);
2. \( T \) is surjective if and only if \( \im T = W \).
:::
:::

::: {.proof}
(a) We use the Subspace Test (@thm-subspace-test). (1) \( \0_W = T(\0_V) \) by @thm-zero-maps-to-zero, so \( \0_W \in \im T \). (2) Let \( \w_1, \w_2 \in \im T \), say \( \w_1 = T(\v_1) \) and \( \w_2 = T(\v_2) \) with \( \v_1, \v_2 \in V \). By (LT1), \( \w_1 + \w_2 = T(\v_1 + \v_2) \), and \( \v_1 + \v_2 \in V \), so \( \w_1 + \w_2 \in \im T \). (3) Let \( \w = T(\v) \in \im T \) and \( c \in F \). By (LT2), \( c\w = T(c\v) \) with \( c\v \in V \), so \( c\w \in \im T \).

(b) The inclusion \( \im T \subseteq W \) always holds. By @def-injective-surjective-bijective, \( T \) is surjective exactly when every \( \w \in W \) equals \( T(\v) \) for some \( \v \), that is, when \( W \subseteq \im T \). So \( T \) is surjective if and only if \( \im T = W \).
:::

This pays off a pattern from Chapter 1, §2. The null space of a matrix (@exm-null-space-subspace), the symmetric matrices (@exm-symmetric-matrices) and the trace-free matrices (@exm-trace-free-matrices) were each shown to be subspaces by a separate check, and that section promised a single theorem. Each is the kernel of a linear map (\( T_\A \), \( \A \mapsto \A - \A\tp \), and the trace), so @thm-prop-kernel covers them all at once.

**First examples.** Start with the maps that have the most extreme kernels and images.

::: {#exm-kernel-image-degenerate}
[The Zero Map and the Identity]

Find the kernel and image of the zero map \( 0 \colon V \to W \) and of the identity \( \id_V \colon V \to V \).
:::

::: {.solution}
The zero map sends every vector to \( \0_W \), so \( \ker 0 = V \) and \( \im 0 = \{\0_W\} \). The identity sends \( \v \) to \( \v \), which is \( \0 \) only when \( \v = \0 \), so \( \ker \id_V = \{\0\} \). Every \( \v \) is its own image, so \( \im \id_V = V \).
:::

These two are the ends of the scale. The kernel is always between \( \{\0\} \) and \( V \), and the image between \( \{\0\} \) and \( W \). The zero map kills everything and reaches nothing but \( \0 \); the identity kills nothing and reaches everything.

::: {#exm-projection-kernel-image}
[Projection onto an Axis]

Find the kernel and image of the projection \( T \colon \nR^2 \to \nR^2 \), \( T(a_1, a_2) = (a_1, 0) \), of @exm-projection.
:::

::: {.solution}
\( T(a_1, a_2) = (0, 0) \) exactly when \( a_1 = 0 \). So \( \ker T = \{ (0, a_2) : a_2 \in \nR \} \), the \( y \)-axis. Every output has second entry \( 0 \), and every \( (a_1, 0) \) is an output, namely \( T(a_1, 0) \). So \( \im T \) is the \( x \)-axis. The kernel is the direction the light shines along; the image is the screen the shadow falls on.
:::

**A non-example by minimal change.** Replace \( \0 \) by another vector: for the projection, \( \{ \v : T(\v) = (1, 0) \} = \{ (1, a_2) : a_2 \in \nR \} \). This is the vertical line through \( (1, 0) \). It does not contain \( \0 \), and it is not closed under addition, since \( (1, 0) + (1, 0) = (2, 0) \) lies off the line. So it is **not** a subspace. It is the kernel shifted by \( (1, 0) \). The same thing happens for systems in Chapter 3: the solution set of \( \A\x = \b \) is one particular solution plus the set of solutions of \( \A\x = \0 \), which is \( \ker T_\A \).

**Why the preimage of \( \0 \)?** Because \( \0 \) is the one output that every linear map is guaranteed to hit, so its preimage is never empty, and because all other preimages are translates of it. If \( T(\p) = \w \), then \( T(\v) = \w \) exactly when \( T(\v - \p) = \0 \), that is, when \( \v \in \p + \ker T \). The kernel describes the shape of every non-empty preimage at once.

::: {.warning}
**Keep track of where each subspace lives.** The kernel sits inside the **domain** \( V \); the image sits inside the **codomain** \( W \). For \( T_\A \colon F^n \to F^m \), the kernel consists of columns with \( n \) entries and the image of columns with \( m \) entries, so "\( \ker T = \im T \)" does not even make sense unless \( V = W \). And the image is **not** the codomain in general: the differentiation map \( D \colon \nR[x]_{\le 3} \to \nR[x]_{\le 3} \) has codomain \( \nR[x]_{\le 3} \), but \( x^3 \) is not the derivative of any cubic, so \( \im D \neq \nR[x]_{\le 3} \).
:::

## Injectivity via the kernel

The computation that opened the section now becomes a theorem. It is the reason to prefer the kernel over the definition of injectivity whenever a map is linear.

::: {#thm-injective-iff-trivial-kernel}
[Kernel Test for Injectivity]

Let \( T \colon V \to W \) be linear. Then \( T \) is injective **if and only if** \( \ker T = \{\0\} \).
:::

::: {.proof}
\( (\Rightarrow) \) Suppose \( T \) is injective, and let \( \v \in \ker T \). Then \( T(\v) = \0_W = T(\0_V) \) by @thm-zero-maps-to-zero. Injectivity gives \( \v = \0_V \). Hence \( \ker T \subseteq \{\0\} \), and the reverse inclusion holds because \( \ker T \) is a subspace (@thm-prop-kernel).

\( (\Leftarrow) \) Suppose \( \ker T = \{\0\} \), and let \( T(\u) = T(\v) \). By @thm-preserves-negation, \( T(\u - \v) = T(\u) - T(\v) = \0 \), so \( \u - \v \in \ker T = \{\0\} \). Hence \( \u = \v \), and \( T \) is injective.
:::

Compare the work. The definition asks: for **all pairs** \( \u, \v \), does \( T(\u) = T(\v) \) force \( \u = \v \)? The theorem asks only: for **each** \( \v \), does \( T(\v) = \0 \) force \( \v = \0 \)? The second question is usually a homogeneous linear system or a coefficient comparison. For \( T_\A \), the theorem says that \( \x \mapsto \A\x \) is injective exactly when \( \A\x = \0 \) has only the trivial solution; Chapter 3 turns that into a test that elimination can run.

## Computing the image

The image is defined by an existence condition, which is hard to check directly. When \( V \) has a spanning list, applying \( T \) to it gives a spanning list of \( \im T \).

::: {#thm-image-spanned-by-basis-images}
[The Image Is Spanned by the Images of a Spanning List]

Let \( T \colon V \to W \) be linear, and suppose \( (\v_1, \dots, \v_k) \) spans \( V \). Then
\[
\im T = \Span\bigl(T(\v_1), \dots, T(\v_k)\bigr).
\]
In particular, if \( V \) is finite-dimensional, then so is \( \im T \), even when \( W \) is not.
:::

::: {.proof}
\( (\supseteq) \) Each \( T(\v_i) \) lies in \( \im T \), which is a subspace by @thm-prop-image. By @thm-span-subspace (3), the span of these vectors is contained in \( \im T \).

\( (\subseteq) \) Let \( \w \in \im T \), say \( \w = T(\v) \) with \( \v \in V \). Since \( (\v_1, \dots, \v_k) \) spans \( V \), \( \v = a_1\v_1 + \dots + a_k\v_k \) for some \( a_i \in F \). By @thm-linear-combination, \( \w = a_1T(\v_1) + \dots + a_kT(\v_k) \in \Span(T(\v_1), \dots, T(\v_k)) \).

If \( V \) is finite-dimensional, some finite list spans \( V \) (@def-finite-dimensional), and its images form a finite list spanning \( \im T \).
:::

So the recipe for the image is: apply \( T \) to a basis (or any spanning list) of \( V \), then sift the results to a basis if one is wanted (@thm-sift). The images of a basis need not be independent; the projection sends the basis \( (\e_1, \e_2) \) to \( (\e_1, \0) \).

## Examples {#sec-kernel-image-examples}

We now compute kernels and images across the families: polynomials, matrices and sequences. In each case we then read off injectivity from the kernel and surjectivity from the image.

::: {#exm-differentiation-kernel-image}
[Differentiation]

Find the kernel and image of \( D \colon \nR[x]_{\le 3} \to \nR[x]_{\le 2} \), \( D(p) = p' \).
:::

::: {.solution}
*Kernel.* Let \( p = a_0 + a_1x + a_2x^2 + a_3x^3 \). Then \( D(p) = a_1 + 2a_2x + 3a_3x^2 \), which is the zero polynomial exactly when \( a_1 = 2a_2 = 3a_3 = 0 \). Since \( 2 \neq 0 \) and \( 3 \neq 0 \) in \( \nR \), this means \( a_1 = a_2 = a_3 = 0 \). So \( \ker D = \{ a_0 : a_0 \in \nR \} = \Span(1) \), the constants.

*Image.* By @thm-image-spanned-by-basis-images applied to the basis \( (1, x, x^2, x^3) \),
\[
\begin{aligned}
\im D &= \Span\bigl(D(1), D(x), D(x^2), D(x^3)\bigr) = \Span(0, 1, 2x, 3x^2) \\
&= \Span(1, x, x^2) = \nR[x]_{\le 2}.
\end{aligned}
\]
So \( D \) is surjective but not injective: \( p \) and \( p + 5 \) have the same derivative. Note \( \dim \ker D + \dim \im D = 1 + 3 = 4 = \dim \nR[x]_{\le 3} \).
:::

::: {#exm-trace-kernel-image}
[Trace]

Find the kernel and image of \( \tr \colon M_2(\nR) \to \nR \).
:::

::: {.solution}
*Kernel.* A matrix \( \begin{pmatrix} a & b \\ c & d \end{pmatrix} \) has trace \( 0 \) exactly when \( d = -a \), that is, when it equals
\[
\begin{pmatrix} a & b \\ c & -a \end{pmatrix} = a\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} + b\E_{12} + c\E_{21}.
\]
So \( \E_{11} - \E_{22}, \E_{12}, \E_{21} \) span \( \ker \tr \). They are independent: the combination above is the zero matrix only if \( a = b = c = 0 \). Hence they form a basis, and \( \dim \ker \tr = 3 \).

*Image.* \( \im \tr \) is a subspace of \( \nR \), and it contains \( \tr \E_{11} = 1 \). The lazy preimage \( r\E_{11} \) of any \( r \in \nR \) shows \( \im \tr = \nR \). So the trace is surjective but not injective. Again \( 3 + 1 = 4 = \dim M_2(\nR) \).
:::

The next two examples live in infinite-dimensional spaces, and the pattern "one property but not the other" goes the opposite way.

::: {#exm-integration-kernel-image}
[Integration]

Find the kernel and image of \( J \colon \nR[x] \to \nR[x] \), \( J(p)(x) = \int_0^x p(t)\,\dd t \), of @exm-integration.
:::

::: {.solution}
*Kernel.* For \( p = a_0 + a_1x + \dots + a_nx^n \), \( J(p) = a_0x + \frac{a_1}{2}x^2 + \dots + \frac{a_n}{n + 1}x^{n+1} \). This is the zero polynomial only if every \( \frac{a_k}{k + 1} = 0 \), that is, every \( a_k = 0 \). So \( \ker J = \{0\} \), and \( J \) is injective by @thm-injective-iff-trivial-kernel.

*Image.* Let \( U = \{ q \in \nR[x] : q(0) = 0 \} \), the polynomials with constant coefficient \( 0 \). Every \( J(p) \) has constant coefficient \( 0 \), so \( \im J \subseteq U \). Conversely, if \( q = b_1x + b_2x^2 + \dots + b_mx^m \in U \), then \( p = b_1 + 2b_2x + \dots + mb_mx^{m-1} \) satisfies \( J(p) = q \). Hence \( \im J = U \). Since \( 1 \notin U \), \( J \) is **not** surjective.
:::

::: {#exm-shift-kernel-image}
[The Shifts: Injective but Not Surjective, and Conversely]

Find the kernels and images of the right and left shifts \( R, L \colon F^{\nN} \to F^{\nN} \) of @exm-shift.
:::

::: {.solution}
*Right shift.* \( R(s_0, s_1, \dots) = (0, s_0, s_1, \dots) \) is the zero sequence only if every \( s_k = 0 \). So \( \ker R = \{\0\} \), and \( R \) is injective. Every output has first entry \( 0 \); conversely, \( (0, t_1, t_2, \dots) = R(t_1, t_2, \dots) \). So \( \im R = \{ \mathbf{t} \in F^{\nN} : t_0 = 0 \} \neq F^{\nN} \), and \( R \) is not surjective: \( \e_0 = (1, 0, 0, \dots) \) is never an output.

*Left shift.* \( L(s_0, s_1, s_2, \dots) = (s_1, s_2, \dots) \) is zero exactly when \( s_1 = s_2 = \dots = 0 \), with \( s_0 \) arbitrary. So \( \ker L = \Span(\e_0) \neq \{\0\} \), and \( L \) is not injective. Every sequence is an output, since \( L(R(\mathbf{t})) = \mathbf{t} \). So \( \im L = F^{\nN} \), and \( L \) is surjective.
:::

This pays off the pointer from Chapter 1, §8: \( R \) matches \( F^{\nN} \) one-to-one with its proper subspace \( \im R \). For a map \( V \to V \) on a **finite** set, injective and surjective are equivalent (@thm-finite-injective-iff-surjective). The shifts, and the pair \( J \) and \( D \) on \( \nR[x] \) (where \( D(J(p)) = p \) makes \( D \) surjective, while \( D(1) = 0 \) makes it not injective), show that for linear maps on an infinite-dimensional space this equivalence fails. The next section proves that it holds again when \( V \) is finite-dimensional.

::: {.check}
Find \( \ker T \) and \( \im T \) for the map \( T \colon \nR^2 \to \nR^3 \), \( T(x, y) = (2x - y,\ x + y,\ x - y) \), of @exm-map-from-basis-values. Is \( T \) injective? Surjective?
:::

::: {.solution}
If \( T(x, y) = \0 \), then \( x + y = 0 \) and \( x - y = 0 \), so \( x = y = 0 \). Hence \( \ker T = \{\0\} \), and \( T \) is injective. By @thm-image-spanned-by-basis-images, \( \im T = \Span(T(\e_1), T(\e_2)) = \Span\bigl((2, 1, 1), (-1, 1, -1)\bigr) \), a plane in \( \nR^3 \). A span of two vectors has dimension at most \( 2 < 3 \), so \( \im T \neq \nR^3 \) and \( T \) is not surjective.
:::

## What injective and surjective maps do to lists

Injectivity and surjectivity are statements about vectors. They translate into statements about lists: injective maps keep independent lists independent, and surjective maps keep spanning lists spanning. On a basis, the translation goes both ways.

::: {#thm-injective-preserves-independence}
[Injective Maps Preserve Independence, Surjective Maps Preserve Spanning]

Let \( T \colon V \to W \) be linear.

::: {.enumerate options="label=(\alph*)"}
1. If \( T \) is injective and \( (\v_1, \dots, \v_k) \) is linearly independent in \( V \), then \( (T(\v_1), \dots, T(\v_k)) \) is linearly independent in \( W \).
2. If \( T \) is surjective and \( (\v_1, \dots, \v_k) \) spans \( V \), then \( (T(\v_1), \dots, T(\v_k)) \) spans \( W \).
3. If \( (\v_1, \dots, \v_n) \) is a basis of \( V \), then \( T \) is injective if and only if \( (T(\v_1), \dots, T(\v_n)) \) is linearly independent, and \( T \) is surjective if and only if \( (T(\v_1), \dots, T(\v_n)) \) spans \( W \).
:::
:::

::: {.proof}
(a) Let \( a_1T(\v_1) + \dots + a_kT(\v_k) = \0 \). By @thm-linear-combination, \( T(a_1\v_1 + \dots + a_k\v_k) = \0 \), so \( a_1\v_1 + \dots + a_k\v_k \in \ker T \). Since \( T \) is injective, \( \ker T = \{\0\} \) (@thm-injective-iff-trivial-kernel), so \( a_1\v_1 + \dots + a_k\v_k = \0 \). The independence of \( (\v_1, \dots, \v_k) \) gives \( a_1 = \dots = a_k = 0 \).

(b) By @thm-image-spanned-by-basis-images, \( \Span(T(\v_1), \dots, T(\v_k)) = \im T \), and \( \im T = W \) because \( T \) is surjective (@thm-prop-image).

(c) *Injectivity.* \( (\Rightarrow) \) is (a). \( (\Leftarrow) \) Suppose the images are independent, and let \( \v \in \ker T \). Write \( \v = a_1\v_1 + \dots + a_n\v_n \). By @thm-linear-combination, \( \0 = T(\v) = a_1T(\v_1) + \dots + a_nT(\v_n) \), so all \( a_i = 0 \) and \( \v = \0 \). Hence \( \ker T = \{\0\} \), and \( T \) is injective by @thm-injective-iff-trivial-kernel.

*Surjectivity.* By @thm-image-spanned-by-basis-images, \( \im T = \Span(T(\v_1), \dots, T(\v_n)) \). By @thm-prop-image, \( T \) is surjective exactly when this span is \( W \).
:::

::: {.warning}
**Without injectivity, independence can be lost.** The projection \( T(a_1, a_2) = (a_1, 0) \) sends the independent list \( ((1, 0), (1, 1)) \) to \( ((1, 0), (1, 0)) \), which is dependent. The kernel is to blame: \( (1, 1) - (1, 0) = (0, 1) \) lies in \( \ker T \). Likewise, a map that is not surjective sends **no** list to a spanning list of \( W \), since all the images lie in \( \im T \neq W \): the inclusion \( \nR[x]_{\le 2} \to \nR[x]_{\le 3} \) sends the basis \( (1, x, x^2) \) to a list that misses \( x^3 \).
:::

Part (c) turns a question about a map into a question about \( n \) vectors in \( W \), which for vectors in \( F^m \) is a question Chapter 3 settles by elimination. In the next section, counting dimensions will let us check only **one** of injectivity and surjectivity when \( \dim V = \dim W \).

## Exercises

### A. Check your understanding

::: {#exr-kernel-image-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the kernel and the image of a linear map \( T \colon V \to W \). Of which spaces are they subspaces?
2. State the kernel test for injectivity.
3. True or false: if \( T(\u) = T(\v) \), then \( \u - \v \in \ker T \). Justify your answer.
4. True or false: for \( D \colon \nR[x]_{\le 3} \to \nR[x]_{\le 3} \), \( D(p) = p' \), we have \( \im D = \nR[x]_{\le 3} \). Justify your answer.
5. True or false: for a linear \( T \colon V \to W \) and **any** \( \w \in W \), the set \( \{ \v \in V : T(\v) = \w \} \) is a subspace of \( V \). Justify your answer.
:::
:::

::: {.solution}
(a) See @def-kernel and @def-image: \( \ker T = \{ \v \in V : T(\v) = \0 \} \), a subspace of \( V \) (@thm-prop-kernel); \( \im T = \{ T(\v) : \v \in V \} \), a subspace of \( W \) (@thm-prop-image).

(b) See @thm-injective-iff-trivial-kernel: a linear map is injective if and only if its kernel is \( \{\0\} \).

(c) True. By @thm-preserves-negation, \( T(\u - \v) = T(\u) - T(\v) = \0 \).

(d) False. Every derivative of a polynomial of degree at most \( 3 \) has degree at most \( 2 \), so \( x^3 \notin \im D \).

(e) False. If \( \w \neq \0 \), the set does not contain \( \0 \), since \( T(\0) = \0 \neq \w \). For example, for the projection of @exm-projection-kernel-image and \( \w = (1, 0) \), the set is the line \( \{ (1, a_2) \} \). It is a subspace exactly when \( \w = \0 \), in which case it is \( \ker T \).
:::

### B. Practice

::: {#exr-kernel-image-b1}
[B1: Kernel and Image from the Definitions]

For each map, find the kernel and the image, give a basis of each, and decide whether the map is injective and whether it is surjective.

::: {.enumerate options="label=(\alph*)"}
1. \( D^2 \colon \nR[x]_{\le 3} \to \nR[x]_{\le 3} \), where \( D \) is differentiation.
2. \( T \colon M_2(\nR) \to M_2(\nR) \), \( T(\A) = \A - \A\tp \).
:::
:::

::: {.solution}
(a) Write \( p = a_0 + a_1x + a_2x^2 + a_3x^3 \). Then \( D^2p = 2a_2 + 6a_3x \). *Kernel:* \( D^2p = 0 \) forces \( a_2 = a_3 = 0 \), so \( \ker D^2 = \nR[x]_{\le 1} \), with basis \( (1, x) \). *Image:* the formula shows every \( D^2p \) lies in \( \nR[x]_{\le 1} \), and conversely \( b_0 + b_1x = D^2\bigl(\tfrac{b_0}{2}x^2 + \tfrac{b_1}{6}x^3\bigr) \), so \( \im D^2 = \nR[x]_{\le 1} \), again with basis \( (1, x) \). Since \( \ker D^2 \neq \{0\} \), \( D^2 \) is not injective (@thm-injective-iff-trivial-kernel); since \( \im D^2 \neq \nR[x]_{\le 3} \) (it omits \( x^2 \)), it is not surjective.

(b) \( T \) is linear because the transpose is: \( (\A + \B)\tp = \A\tp + \B\tp \) and \( (c\A)\tp = c\A\tp \) (@thm-transpose-properties). *Kernel:* \( \A - \A\tp = 0 \) says \( \A = \A\tp \), so \( \ker T \) is the space of symmetric matrices, with basis \( (\E_{11}, \E_{22}, \E_{12} + \E_{21}) \). *Image:* each \( \A - \A\tp \) is skew-symmetric, since \( (\A - \A\tp)\tp = \A\tp - \A = -(\A - \A\tp) \); and every skew-symmetric \( \B \in M_2(\nR) \) is a multiple of \( \E_{12} - \E_{21} \), with \( \B = T(\tfrac12\B) \). So \( \im T = \Span(\E_{12} - \E_{21}) \), with basis \( (\E_{12} - \E_{21}) \). \( T \) is neither injective (the kernel is non-zero) nor surjective (the image is not all of \( M_2(\nR) \)).
:::

::: {#exr-kernel-image-b2}
[B2: Kernels and Images Beyond \( F^n \)]

For each map, find a basis of the kernel and a basis of the image, and decide whether the map is injective and whether it is surjective.

::: {.enumerate options="label=(\alph*)"}
1. \( T \colon \nR[x]_{\le 2} \to \nR[x]_{\le 2} \), \( T(p) = p' + p \).
2. \( S \colon M_2(\nR) \to M_2(\nR) \), \( S(\A) = \A - \A\tp \).
:::
:::

::: {.solution}
Both maps are linear. For \( c \in \nR \), by linearity of differentiation (@exm-differentiation), \( T(cp + q) = (cp' + q') + (cp + q) = cT(p) + T(q) \). By linearity of the transpose (@exm-trace-matrices), \( S(c\A + \B) = c\A + \B - c\A\tp - \B\tp = cS(\A) + S(\B) \). Both are linear by @thm-equivalent-condition.

(a) *Kernel.* Let \( p = a + bx + cx^2 \). Then \( T(p) = (b + 2cx) + (a + bx + cx^2) = (a + b) + (b + 2c)x + cx^2 \). This is zero exactly when \( c = 0 \), \( b + 2c = 0 \) and \( a + b = 0 \), that is, \( c = b = a = 0 \). So \( \ker T = \{0\} \), with the empty list as basis, and \( T \) is injective.

*Image.* We show \( T \) is surjective. Given \( q \in \nR[x]_{\le 2} \), let \( p = q - q' + q'' \). Then \( p \in \nR[x]_{\le 2} \), and since \( q''' = 0 \),
\[
T(p) = (q' - q'' + q''') + (q - q' + q'') = q .
\]
So \( \im T = \nR[x]_{\le 2} \), with basis \( (1, x, x^2) \), and \( T \) is surjective.

(b) *Kernel.* \( S(\A) = 0 \) exactly when \( \A\tp = \A \). A matrix \( \begin{pmatrix} a & b \\ c & d \end{pmatrix} \) is symmetric exactly when \( b = c \), that is, when it equals \( a\E_{11} + d\E_{22} + b(\E_{12} + \E_{21}) \). These three matrices are independent (compare entries), so \( (\E_{11}, \E_{22}, \E_{12} + \E_{21}) \) is a basis of \( \ker S \). \( S \) is not injective.

*Image.* By @thm-image-spanned-by-basis-images with the basis \( (\E_{11}, \E_{12}, \E_{21}, \E_{22}) \), \( \im S \) is spanned by \( S(\E_{11}) = 0 \), \( S(\E_{12}) = \E_{12} - \E_{21} \), \( S(\E_{21}) = \E_{21} - \E_{12} \) and \( S(\E_{22}) = 0 \). So \( \im S = \Span(\E_{12} - \E_{21}) \), with basis \( (\E_{12} - \E_{21}) \), the skew-symmetric matrices. Since \( \I_2 \notin \im S \), \( S \) is not surjective.
:::

### C. Going deeper

In these exercises, for linear maps \( T \colon U \to V \) and \( S \colon V \to W \) we write \( ST \) for the composite \( S \circ T \colon U \to W \), which applies \( T \) first. It is linear: \( ST(c\u + \u') = S(cT(\u) + T(\u')) = cST(\u) + ST(\u') \), by @thm-equivalent-condition for \( T \) and then for \( S \).

::: {#exr-kernel-image-c1}
[C1: Kernels and Images of a Composite]

Let \( T \colon U \to V \) and \( S \colon V \to W \) be linear.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \ker T \subseteq \ker(ST) \) and \( \im(ST) \subseteq \im S \).
2. Give an example, with \( U = V = W = \nR^2 \), where \( \ker T \neq \ker(ST) \).
3. Deduce that if \( ST \) is injective, then \( T \) is injective, and if \( ST \) is surjective, then \( S \) is surjective.
:::
:::

::: {.solution}
(a) Let \( \u \in \ker T \). Then \( ST(\u) = S(\0) = \0 \) by @thm-zero-maps-to-zero, so \( \u \in \ker(ST) \). Let \( \w \in \im(ST) \), say \( \w = S(T(\u)) \). Then \( \w = S(\v) \) with \( \v = T(\u) \in V \), so \( \w \in \im S \).

(b) Let \( T = \id_{\nR^2} \) and let \( S \) be the projection \( S(a_1, a_2) = (a_1, 0) \). Then \( \ker T = \{\0\} \), while \( \ker(ST) = \ker S \) is the \( y \)-axis (@exm-projection-kernel-image).

(c) If \( ST \) is injective, then \( \ker(ST) = \{\0\} \) (@thm-injective-iff-trivial-kernel), so \( \ker T = \{\0\} \) by (a), and \( T \) is injective. If \( ST \) is surjective, then \( W = \im(ST) \subseteq \im S \subseteq W \) by (a), so \( \im S = W \) and \( S \) is surjective (@thm-prop-image).
:::

::: {#exr-kernel-image-c2}
[C2: When Is a Composite Injective?]

Let \( T \colon U \to V \) and \( S \colon V \to W \) be linear, and suppose \( T \) is injective. Prove that \( ST \) is injective if and only if \( \ker S \cap \im T = \{\0\} \), that is, if and only if \( S \) is injective on \( \im T \). Give an example where \( S \) is not injective but \( ST \) is.
:::

::: {.solution}
\( (\Rightarrow) \) Suppose \( ST \) is injective, and let \( \v \in \ker S \cap \im T \). Then \( \v = T(\u) \) for some \( \u \in U \), and \( ST(\u) = S(\v) = \0 \). So \( \u \in \ker(ST) = \{\0\} \) (@thm-injective-iff-trivial-kernel), and \( \v = T(\0) = \0 \).

\( (\Leftarrow) \) Suppose \( \ker S \cap \im T = \{\0\} \), and let \( \u \in \ker(ST) \). Then \( T(\u) \in \im T \) and \( S(T(\u)) = \0 \), so \( T(\u) \in \ker S \cap \im T = \{\0\} \). Since \( T \) is injective, \( \u = \0 \). Hence \( \ker(ST) = \{\0\} \), and \( ST \) is injective.

Example: let \( T \colon \nR \to \nR^2 \), \( T(a) = (a, 0) \), which is injective with \( \im T \) the \( x \)-axis, and let \( S \colon \nR^2 \to \nR \), \( S(a_1, a_2) = a_1 \). Then \( \ker S \) is the \( y \)-axis, so \( S \) is not injective, but \( \ker S \cap \im T = \{\0\} \), and indeed \( ST(a) = a \) is injective.
:::

::: {#exr-kernel-image-c3}
[C3: Differentiation over \( \nF_2 \)]

Let \( D \colon \nF_2[x]_{\le 3} \to \nF_2[x]_{\le 3} \) be the formal derivative (@exm-differentiation). Find bases of \( \ker D \) and \( \im D \). Which step of @exm-differentiation-kernel-image fails over \( \nF_2 \)?
:::

::: {.solution}
For \( p = a_0 + a_1x + a_2x^2 + a_3x^3 \), \( D(p) = a_1 + 2a_2x + 3a_3x^2 \). In \( \nF_2 \), \( 2 = 0 \) and \( 3 = 1 \), so \( D(p) = a_1 + a_3x^2 \).

*Kernel.* \( D(p) = 0 \) exactly when \( a_1 = a_3 = 0 \), so \( \ker D = \{ a_0 + a_2x^2 \} \), with basis \( (1, x^2) \). The polynomials \( 1 \) and \( x^2 \) are independent by @thm-distinct-degrees-independent.

*Image.* By @thm-image-spanned-by-basis-images, \( \im D = \Span(D(1), D(x), D(x^2), D(x^3)) = \Span(0, 1, 0, x^2) \), with basis \( (1, x^2) \).

The failing step is "\( 2a_2 = 0 \) forces \( a_2 = 0 \)", which divides by \( 2 \); over \( \nF_2 \), \( 2 = 0 \), and \( D(x^2) = 2x = 0 \) although \( x^2 \) is not constant. So over \( \nF_2 \) the kernel of differentiation is bigger than the constants, and here \( \ker D = \im D \).
:::
