# Bessel, Parseval and Fourier Series

Section 3 measured a vector against a finite-dimensional subspace and produced the nearest point in it. Read that answer coefficient by coefficient and it becomes an inequality: the numbers \( \inner{\v}{\e_i} \) collected against an orthonormal list can never carry more squared length than \( \v \) itself has. That is Bessel's inequality. It costs nothing in dimension, it holds in spaces far too large for Chapter 1's machinery, and its equality case is Parseval's identity. This section proves both, applies them to the sines and cosines, and then stops at the exact place where linear algebra stops and analysis begins.

Throughout, \( V \) is an inner product space over \( F = \nR \) or \( F = \nC \), with inner product \( \inner{\cdot}{\cdot} \) (@def-inner-product) and induced norm \( \norm{\cdot} \) (@def-induced-norm). **We do not assume that \( V \) is finite-dimensional.** What we assume each time is that the *list* we compute against is finite.

## Coefficients against an orthonormal list

In @thm-orthonormal-coordinates the list was an orthonormal **basis**, and the coefficients \( \inner{\v}{\e_i} \) recovered \( \v \) exactly. Suppose now the list is only a list: too short to be a basis, or sitting inside a space that has no finite basis at all, like the continuous functions on an interval. The numbers \( \inner{\v}{\e_i} \) are still there. What can be said about them when they no longer determine \( \v \)?

*Against a shorter list you can only lose length, never gain it.*

::: {#def-fourier-coefficients}
[Fourier Coefficients With Respect to an Orthonormal List]

Let \( (\e_1, \dots, \e_k) \) be an orthonormal list in an inner product space \( V \) and let \( \v \in V \). The scalars
\[
\inner{\v}{\e_1},\ \dots,\ \inner{\v}{\e_k} \in F
\]
are the **Fourier coefficients** of \( \v \) with respect to the list.
:::

The name is borrowed from the classical case below, where the \( \e_i \) are sines and cosines; nothing in the definition mentions trigonometry. When the list happens to be a basis, these are exactly the coordinates of \( \v \), by @thm-orthonormal-coordinates (a). When it is not, they are the coordinates of a *shadow* of \( \v \), and the next theorem measures that shadow.

::: {#thm-bessel-inequality}
[Bessel's Inequality]

Let \( V \) be an inner product space over \( F \), **not assumed finite-dimensional**, and let \( (\e_1, \dots, \e_k) \) be an orthonormal list in \( V \). Then for **every** \( \v \in V \),
\[
\sum_{i=1}^{k} \lvert \inner{\v}{\e_i} \rvert^2 \;\le\; \norm{\v}^2 .
\]
:::

::: {.idea}
The left-hand side is not a quantity out of nowhere. Let \( U \) be the span of the list. By the projection formula, \( P_U\v \) is exactly \( \sum_i \inner{\v}{\e_i}\e_i \), and its summands are pairwise orthogonal, so Pythagoras turns its squared length into precisely that sum. The inequality then says no more than "a shadow is no longer than what casts it", which we already proved. The one point needing care is that \( V \) may be infinite-dimensional; it does not matter, because Section 3 only ever asked the **subspace** to be finite-dimensional.
:::

::: {.proof}
Put \( U = \Span(\e_1, \dots, \e_k) \). The vectors \( \e_i \) are orthogonal and non-zero, so the list is linearly independent by @thm-orthogonal-independent; being a spanning list of \( U \) as well, it is an orthonormal basis of \( U \), and \( \dim U = k \) is finite. Hence @thm-projection-formula applies to \( U \) even though \( V \) need not be finite-dimensional, and part (a) of it gives
\[
P_U\v = \sum_{i=1}^{k} \inner{\v}{\e_i}\,\e_i .
\]
The summands \( \inner{\v}{\e_i}\e_i \) are pairwise orthogonal, since \( \e_i \perp \e_j \) for \( i \ne j \) and scalars come out of both slots. So @thm-pythagoras and @thm-norm-properties (b) give
\[
\norm{P_U\v}^2 = \sum_{i=1}^{k} \lvert \inner{\v}{\e_i} \rvert^2 \norm{\e_i}^2
= \sum_{i=1}^{k} \lvert \inner{\v}{\e_i} \rvert^2 ,
\]
using \( \norm{\e_i} = 1 \). By @thm-projection-formula (c), \( \norm{P_U\v} \le \norm{\v} \). Both sides are non-negative, so squaring preserves the inequality, and this proves the theorem.
:::

The proof gives more than the inequality, and the surplus is worth recording. The vector \( \v - P_U\v \) lies in \( U^{\perp} \) by @thm-orthogonal-decomposition, so it is orthogonal to \( P_U\v \in U \), and @thm-pythagoras turns \( \v = P_U\v + (\v - P_U\v) \) into \( \norm{\v}^2 = \norm{P_U\v}^2 + \norm{\v - P_U\v}^2 \). Rearranging, and substituting \( \norm{P_U\v}^2 = \sum_{i=1}^{k}\lvert\inner{\v}{\e_i}\rvert^2 \) from the proof above,
\[
\norm{\v - P_U\v}^2 = \norm{\v}^2 - \sum_{i=1}^{k} \lvert \inner{\v}{\e_i} \rvert^2 .
\tag{$\ast$}
\]
In words: **the deficit in Bessel's inequality is the squared distance from \( \v \) to the span of the list** (@def-distance-to-subspace). An inequality with a known defect is much more useful than an inequality, and we will read \( (\ast) \) from both sides.

::: {.remark}
For an infinite orthonormal list \( (\e_1, \e_2, \e_3, \dots) \), apply the theorem to the first \( k \) terms for each \( k \). The partial sums \( \sum_{i \le k}\lvert\inner{\v}{\e_i}\rvert^2 \) increase with \( k \) and are all bounded above by \( \norm{\v}^2 \), so they converge, and \( \sum_{i=1}^{\infty}\lvert\inner{\v}{\e_i}\rvert^2 \le \norm{\v}^2 \). This is the only fact from analysis used in the present paragraph: a bounded increasing sequence of real numbers converges.
:::

Now the equality case, which is where the word *basis* returns.

::: {#thm-parseval-identity}
[Parseval's Identity]

Let \( (\e_1, \dots, \e_k) \) be an orthonormal list in an inner product space \( V \) and let \( \v \in V \). Then
\[
\sum_{i=1}^{k} \lvert \inner{\v}{\e_i} \rvert^2 = \norm{\v}^2
\quad\text{if and only if}\quad
\v \in \Span(\e_1, \dots, \e_k) .
\]
In particular, if \( (\e_1, \dots, \e_k) \) is an orthonormal **basis** of \( V \), the identity holds for every \( \v \in V \).
:::

::: {.proof}
Keep the notation of the proof of @thm-bessel-inequality, where we showed \( \sum_i \lvert\inner{\v}{\e_i}\rvert^2 = \norm{P_U\v}^2 \) with \( U = \Span(\e_1, \dots, \e_k) \). So the stated equality says \( \norm{P_U\v} = \norm{\v} \), and by @thm-projection-formula (c) this holds if and only if \( \v \in U \). If the list is a basis of \( V \), then \( U = V \) and every \( \v \in V \) lies in \( U \).
:::

For an orthonormal basis of a finite-dimensional space this is @thm-orthonormal-coordinates (c) again; what is new is the equality **case**, which identifies exactly the vectors for which no length is lost. Keep the two statements apart:

- **Bessel** is about an orthonormal **list**, in **any** inner product space, and it is an inequality.
- **Parseval** is the equality, and it holds exactly for the vectors the list already spans.

The whole difference is whether the list reaches \( \v \).

::: {.warning}
**An orthonormal list is not an orthonormal basis, and the deficit in Bessel can be everything.** In \( C[-\pi, \pi] \) below, the list \( (\cos x, \sin x) \) is orthonormal, and for the constant function \( f = 1 \) both coefficients are \( 0 \), so the left-hand side of Bessel is \( 0 \) while \( \norm{f}^2 = 2 \). Nothing at all is captured. A short orthonormal list is not a bad basis; it is not a basis.
:::

::: {.check}
In \( \nR^4 \) with the dot product, let \( \e_1 = \tfrac12(1, 1, 1, 1) \) and \( \e_2 = \tfrac12(1, 1, -1, -1) \), and let \( \v = (1, 2, 3, 4) \). Check that \( (\e_1, \e_2) \) is orthonormal, compute both sides of Bessel's inequality, and say what the deficit equals.
:::

::: {.solution}
Each has norm \( \tfrac12\sqrt{4} = 1 \), and \( \inner{\e_1}{\e_2} = \tfrac14(1 + 1 - 1 - 1) = 0 \), so the list is orthonormal. The coefficients are \( \inner{\v}{\e_1} = \tfrac12(1 + 2 + 3 + 4) = 5 \) and \( \inner{\v}{\e_2} = \tfrac12(1 + 2 - 3 - 4) = -2 \), so the left-hand side is \( 25 + 4 = 29 \), while \( \norm{\v}^2 = 1 + 4 + 9 + 16 = 30 \). The inequality is strict, and by \( (\ast) \) the deficit \( 1 \) is the squared distance from \( \v \) to \( \Span(\e_1, \e_2) \). Indeed \( P_U\v = 5\e_1 - 2\e_2 = \big(\tfrac32, \tfrac32, \tfrac72, \tfrac72\big) \) and \( \v - P_U\v = \tfrac12(-1, 1, -1, 1) \), whose squared norm is \( 4 \cdot \tfrac14 = 1 \).
:::

## The trigonometric system

The classical home of these two statements is a space of functions, and the first thing to fix is the inner product, constant included.

Let \( V = C[-\pi, \pi] \) be the space of continuous functions \( f \colon [-\pi, \pi] \to \nR \), a real vector space, and define
\[
\inner{f}{g} = \frac{1}{\pi}\int_{-\pi}^{\pi} f(t)\,g(t)\,\dd t .
\]
This is the continuous-function inner product of @def-inner-product on a different interval and rescaled by the positive constant \( 1/\pi \); rescaling by a positive constant preserves all three axioms, and positive definiteness is the argument given there. The constant is chosen for one reason only: it makes the sines and cosines unit vectors. With \( 1/(2\pi) \) in front they would have norm \( 1/\sqrt2 \), and with no constant at all, norm \( \sqrt{\pi} \).

::: {.warning}
**Always state the normalizing constant before computing.** Formulas for Fourier coefficients differ between books by exactly such a factor, and a misplaced \( \pi \) or \( 2 \) changes every number below. In this section \( \inner{f}{g} = \frac1\pi\int_{-\pi}^{\pi} fg \), and every coefficient, norm and inequality is written for that choice.
:::

Here are the facts we assume. From calculus: the integral of a finite sum is the sum of the integrals; \( \int_{-\pi}^{\pi} \dd t = 2\pi \); \( \int_{-\pi}^{\pi}\sin(mt)\,\dd t = 0 \) for every integer \( m \) and \( \int_{-\pi}^{\pi}\cos(mt)\,\dd t = 0 \) for every **non-zero** integer \( m \) (for \( m \neq 0 \) evaluate the antiderivative \( -\cos(mt)/m \), respectively \( \sin(mt)/m \), each of which takes the same value at \( t = -\pi \) as at \( t = \pi \); for \( m = 0 \) the sine integrand is \( 0 \)); integration by parts, and the substitution \( t \mapsto -t \), both of which we use later in the section when computing particular Fourier coefficients. From trigonometry: the product-to-sum identities. **No theorem about convergence is used anywhere in this section**; every integral we compute is the integral of a finite sum of sines and cosines.

::: {#exm-trigonometric-orthonormal}
[The Trigonometric System Is Orthonormal]

Fix \( n \ge 1 \). Show that the list of \( 2n + 1 \) functions
\[
\frac{1}{\sqrt2},\ \cos x,\ \sin x,\ \cos 2x,\ \sin 2x,\ \dots,\ \cos nx,\ \sin nx
\]
is orthonormal in \( V = C[-\pi, \pi] \) with \( \inner{f}{g} = \frac1\pi\int_{-\pi}^{\pi} fg \).
:::

::: {.solution}
There are five kinds of pair. Write \( j, k \) for indices in \( \{1, \dots, n\} \).

*The constant with itself.* \( \norm{1/\sqrt2}^2 = \frac1\pi\int_{-\pi}^{\pi}\tfrac12\,\dd t = \frac1\pi \cdot \pi = 1 \).

*The constant against \( \cos kx \) or \( \sin kx \).* These are \( \frac{1}{\pi\sqrt2}\int_{-\pi}^{\pi}\cos(kt)\,\dd t = 0 \) and \( \frac{1}{\pi\sqrt2}\int_{-\pi}^{\pi}\sin(kt)\,\dd t = 0 \), since \( k \ne 0 \).

*Two cosines.* By \( \cos A\cos B = \tfrac12[\cos(A - B) + \cos(A + B)] \),
\[
\inner{\cos jx}{\cos kx}
= \frac{1}{2\pi}\int_{-\pi}^{\pi}\!\big[\cos((j - k)t) + \cos((j + k)t)\big]\dd t .
\]
If \( j \ne k \), both \( j - k \) and \( j + k \) are non-zero integers, so both integrals vanish and the value is \( 0 \). If \( j = k \), the first integrand is the constant \( 1 \) and the second has non-zero frequency \( 2k \), so the value is \( \frac{1}{2\pi}(2\pi + 0) = 1 \).

*Two sines.* By \( \sin A\sin B = \tfrac12[\cos(A - B) - \cos(A + B)] \), the same two integrals appear with a minus sign, giving \( 0 \) for \( j \ne k \) and \( \frac{1}{2\pi}(2\pi - 0) = 1 \) for \( j = k \).

*A sine against a cosine.* By \( \sin A\cos B = \tfrac12[\sin(A + B) + \sin(A - B)] \),
\[
\inner{\sin jx}{\cos kx}
= \frac{1}{2\pi}\int_{-\pi}^{\pi}\!\big[\sin((j + k)t) + \sin((j - k)t)\big]\dd t = 0 ,
\]
because every integral of a sine over \( [-\pi, \pi] \) vanishes, including the case \( j = k \) where the second integrand is \( \sin 0 = 0 \).

So each of the \( 2n + 1 \) functions is a unit vector and distinct ones are orthogonal, which is @def-orthonormal-list.
:::

Write \( W_n = \Span(1, \cos x, \sin x, \dots, \cos nx, \sin nx) \), the space of **trigonometric polynomials of degree at most \( n \)**. The list above is an orthonormal list, hence independent (@thm-orthogonal-independent), and it spans \( W_n \), since \( 1 = \sqrt2 \cdot \tfrac{1}{\sqrt2} \). So it is an orthonormal basis of \( W_n \) and \( \dim W_n = 2n + 1 \).

For \( f \in V \) the classical **Fourier coefficients** of \( f \) are
\[
a_k = \frac1\pi\int_{-\pi}^{\pi} f(t)\cos(kt)\,\dd t, \qquad
b_k = \frac1\pi\int_{-\pi}^{\pi} f(t)\sin(kt)\,\dd t ,
\]
for \( k \ge 0 \) and \( k \ge 1 \) respectively. Comparing with the inner product, \( a_k = \inner{f}{\cos kx} \) and \( b_k = \inner{f}{\sin kx} \), while the coefficient against the constant of the orthonormal list is \( \inner{f}{1/\sqrt2} = a_0/\sqrt2 \). These are exactly the Fourier coefficients of @def-fourier-coefficients for this list.

::: {#thm-fourier-best-approximation}
[Fourier Partial Sums Are Best Approximations]

Let \( f \in C[-\pi, \pi] \), let \( n \ge 1 \), and let \( a_k, b_k \) be the Fourier coefficients of \( f \). Put
\[
S_nf = \frac{a_0}{2} + \sum_{k=1}^{n}\big(a_k\cos kx + b_k\sin kx\big) .
\]
Then, with \( \inner{f}{g} = \frac1\pi\int_{-\pi}^{\pi} fg \):

::: {.enumerate options="label=(\alph*)"}
1. \( S_nf = P_{W_n}f \);
2. \( \norm{f - S_nf} \le \norm{f - g} \) for every \( g \in W_n \), with equality **only** for \( g = S_nf \);
3. \( \displaystyle \frac{a_0^2}{2} + \sum_{k=1}^{n}\big(a_k^2 + b_k^2\big) \le \frac1\pi\int_{-\pi}^{\pi} f(t)^2\,\dd t \).
:::
:::

::: {.idea}
Nothing new happens here. The subspace \( W_n \) is finite-dimensional and we have an orthonormal basis of it, so Section 3 answers the approximation question and @thm-bessel-inequality answers the coefficient question; the work is only to match the classical notation to ours. The one thing to watch is the factor \( \tfrac12 \) in front of \( a_0 \): it is not a convention pulled from the air, it is what \( \inner{f}{1/\sqrt2} \cdot \tfrac{1}{\sqrt2} \) equals.
:::

::: {.proof}
(a) By @exm-trigonometric-orthonormal the list \( \big(\tfrac{1}{\sqrt2}, \cos x, \sin x, \dots, \cos nx, \sin nx\big) \) is an orthonormal basis of \( W_n \). By @thm-projection-formula (a),
\[
P_{W_n}f = \Big\langle f, \tfrac{1}{\sqrt2} \Big\rangle \tfrac{1}{\sqrt2}
+ \sum_{k=1}^{n}\big(\inner{f}{\cos kx}\cos kx + \inner{f}{\sin kx}\sin kx\big).
\]
The first term is \( \frac{a_0}{\sqrt2}\cdot\frac{1}{\sqrt2} = \frac{a_0}{2} \), and the remaining terms are \( a_k\cos kx + b_k\sin kx \). Hence \( P_{W_n}f = S_nf \).

(b) This is @thm-best-approximation applied to the subspace \( U = W_n \), which is legitimate because \( \dim W_n = 2n + 1 \) is finite, together with (a).

(c) This is @thm-bessel-inequality for the same orthonormal list, since \( \lvert\inner{f}{1/\sqrt2}\rvert^2 = a_0^2/2 \) and \( \norm{f}^2 = \frac1\pi\int_{-\pi}^{\pi} f^2 \).
:::

So the Fourier partial sum is not a guess at \( f \) that happens to work: it **is** the orthogonal projection of \( f \) onto the trigonometric polynomials of degree at most \( n \), and by @thm-best-approximation it is the unique trigonometric polynomial of that degree closest to \( f \) in this norm. The mysterious \( a_0/2 \) of the classical formula is an artifact of normalizing the constant function.

## A worked computation

::: {#exm-fourier-of-x}
[The Fourier Coefficients of \( f(x) = x \)]

In \( C[-\pi, \pi] \) with \( \inner{f}{g} = \frac1\pi\int_{-\pi}^{\pi} fg \), let \( f(x) = x \). Find all \( a_k \) and \( b_k \), write down \( S_nf \), and say what @thm-fourier-best-approximation (c) gives.
:::

::: {.solution}
We use one further calculus fact: a continuous **odd** function integrates to \( 0 \) over \( [-\pi, \pi] \), and a continuous **even** one integrates to twice its integral over \( [0, \pi] \). Both come from the substitution \( t \mapsto -t \).

*The cosine coefficients.* For every \( k \ge 0 \) the function \( t\cos(kt) \) is odd, so \( a_k = 0 \). In particular \( a_0 = 0 \).

*The sine coefficients.* The function \( t\sin(kt) \) is even, so for \( k \ge 1 \),
\[
b_k = \frac1\pi\int_{-\pi}^{\pi} t\sin(kt)\,\dd t = \frac2\pi\int_{0}^{\pi} t\sin(kt)\,\dd t .
\]
Integrating by parts, with \( \dd(-\cos(kt)/k) = \sin(kt)\,\dd t \),
\[
\int_{0}^{\pi} t\sin(kt)\,\dd t
= \Big[\frac{-t\cos(kt)}{k}\Big]_0^{\pi} + \frac1k\int_0^{\pi}\cos(kt)\,\dd t
= \frac{-\pi\cos(k\pi)}{k} ,
\]
since the last integral is \( [\sin(kt)/k^2]_0^\pi = 0 \). As \( \cos(k\pi) = (-1)^k \), this equals \( \pi(-1)^{k+1}/k \), and therefore
\[
b_k = \frac{2(-1)^{k+1}}{k} .
\]

*The partial sums.* Hence
\[
S_nf = \sum_{k=1}^{n}\frac{2(-1)^{k+1}}{k}\sin kx
= 2\sin x - \sin 2x + \tfrac23\sin 3x - \dots ,
\]
and by @thm-fourier-best-approximation (b) this is the closest trigonometric polynomial of degree at most \( n \) to the function \( x \) in this norm.

*What Bessel's inequality (@thm-bessel-inequality) gives.* First \( \norm{f}^2 = \frac1\pi\int_{-\pi}^{\pi} t^2\,\dd t = \frac1\pi\cdot\frac{2\pi^3}{3} = \frac{2\pi^2}{3} \). Since \( a_k = 0 \) and \( b_k^2 = 4/k^2 \), part (c) of @thm-fourier-best-approximation reads
\[
\sum_{k=1}^{n}\frac{4}{k^2} \le \frac{2\pi^2}{3},
\qquad\text{that is}\qquad
\sum_{k=1}^{n}\frac{1}{k^2} \le \frac{\pi^2}{6}
\]
for **every** \( n \). The partial sums on the left increase and are bounded above, so they converge, and \( \sum_{k=1}^{\infty} 1/k^2 \le \pi^2/6 \).
:::

That bound is sharp: the true value of the sum is \( \pi^2/6 \). But sharpness is not something Bessel can deliver. By @thm-parseval-identity, equality for a fixed finite list holds only when \( f \) lies in the span of that list, and the function \( x \) lies in no \( W_n \) — it is not a trigonometric polynomial, since every element of \( W_n \) takes the same value at \( -\pi \) and at \( \pi \). Getting the equality requires a statement about the **infinite** system, and that statement is an input from analysis; @exr-bessel-parseval-fourier-c1 carries it out and flags it.

::: {.check}
Let \( g(x) = \cos^2 x \) in \( C[-\pi, \pi] \). Using \( \cos^2 x = \tfrac12 + \tfrac12\cos 2x \), write down all Fourier coefficients of \( g \), find \( S_1g \), and compute the deficit in Bessel's inequality for \( n = 1 \).
:::

::: {.solution}
The right-hand side \( \tfrac12 + \tfrac12\cos 2x \) already lies in \( W_2 \), and coefficients against an orthonormal basis are unique (@thm-orthonormal-coordinates (a)), so, applying that result inside \( W_2 \) and reading the coefficients off: \( a_0 = 1 \), \( a_2 = \tfrac12 \), and all other \( a_k \) and all \( b_k \) are \( 0 \). Hence \( S_1g = a_0/2 = \tfrac12 \), a constant. For the deficit, \( \norm{g}^2 = \frac1\pi\int_{-\pi}^{\pi}\cos^4 t\,\dd t = \frac1\pi\cdot\frac{3\pi}{4} = \tfrac34 \), while the Bessel sum for \( n = 1 \) is \( a_0^2/2 = \tfrac12 \). The deficit is \( \tfrac14 \), and by \( (\ast) \) it should be \( \norm{g - S_1g}^2 = \big\lVert\tfrac12\cos 2x\big\rVert^2 = \tfrac14\cdot 1 = \tfrac14 \). It is.
:::

## What best approximation does and does not say

It is worth being exact about the boundary here, because it is easy to read more into @thm-fourier-best-approximation than it contains.

Identity \( (\ast) \) applied to \( U = W_n \) says
\[
\norm{f - S_nf}^2 = \norm{f}^2 - \frac{a_0^2}{2} - \sum_{k=1}^{n}\big(a_k^2 + b_k^2\big) .
\]
The subtracted sum never decreases as \( n \) grows, so the numbers \( \norm{f - S_nf}^2 \) never increase, and they are bounded below by \( 0 \). Hence they converge to some limit \( L \ge 0 \). Everything up to this sentence is linear algebra plus one fact about monotone bounded sequences.

Whether \( L = 0 \) is a different kind of question. It asks whether the trigonometric polynomials come arbitrarily close, in this norm, to every continuous function, and no argument in this book decides it. The statement is true, and it is the analytic content of the theory of Fourier series; it is what makes the *infinite* trigonometric system behave like an orthonormal basis even though it is not a basis in the sense of Chapter 1.

And even \( L = 0 \) would not be a statement about individual points. Our norm averages the error over the whole interval, so it tolerates a large error on a short interval. The function \( f(x) = x \) shows this at once:
\[
S_nf(\pi) = \sum_{k=1}^{n}\frac{2(-1)^{k+1}}{k}\sin(k\pi) = 0
\]
for every \( n \), while \( f(\pi) = \pi \). The error at the single point \( x = \pi \) never shrinks at all.

::: {.warning}
**Mean-square best approximation is not pointwise approximation.** @thm-fourier-best-approximation says that \( S_nf \) minimizes \( \int_{-\pi}^{\pi}(f - g)^2 \) over \( g \in W_n \). It does not say that \( S_nf(x) \) is close to \( f(x) \) for a given \( x \), and for \( f(x) = x \) at \( x = \pi \) it is not. Whether a Fourier series converges at a point is a question in analysis with a delicate answer; it is not decided by anything in this chapter, and a projection theorem cannot decide it.
:::

## Legendre and Chebyshev

Two families of orthogonal polynomials show the same two theorems at work with a different weight.

**Legendre.** @exm-gram-schmidt-legendre ran Gram–Schmidt on \( (1, x, x^2) \) in \( \nR[x]_{\le 2} \) with \( \inner{p}{q} = \int_{-1}^{1} pq \), producing the orthogonal list \( 1,\ x,\ x^2 - \tfrac13 \) and, after normalizing, the orthonormal basis
\[
\e_1 = \tfrac{1}{\sqrt2}, \qquad \e_2 = \sqrt{3/2}\,x, \qquad \e_3 = \tfrac{\sqrt{10}}{4}\big(3x^2 - 1\big).
\]
Inside \( \nR[x]_{\le 2} \) this is a **basis**, so @thm-parseval-identity gives \( \norm{p}^2 = \sum_{i=1}^{3}\lvert\inner{p}{\e_i}\rvert^2 \) for every quadratic \( p \). Viewed inside the larger space \( C[-1, 1] \) of continuous functions, the same three vectors are only a **list**, and for an \( f \) outside \( \nR[x]_{\le 2} \) @thm-bessel-inequality is strict, the deficit being the squared distance from \( f \) to \( \nR[x]_{\le 2} \) by \( (\ast) \). That deficit is what @exm-best-quadratic-approximation computed for \( f = x^3 \). One list, two readings, and which reading applies depends on the ambient space, not on the list. In practice one projects with the orthogonal list \( 1,\ x,\ x^2 - \tfrac13 \) through @cor-projection-orthogonal-basis and avoids the square roots entirely.

**Chebyshev.** Change the weight. On \( \nR[x] \) define
\[
\inner{p}{q}_w = \int_{-1}^{1}\frac{p(t)\,q(t)}{\sqrt{1 - t^2}}\,\dd t .
\]
The integrand is unbounded at \( t = \pm 1 \), so this is an improper integral; it converges for polynomials, because \( \lvert pq \rvert \) is bounded on \( [-1, 1] \) and \( \int_{-1}^{1}\dd t/\sqrt{1 - t^2} = \pi \). The three axioms are checked as in @def-inner-product, positivity because \( 1/\sqrt{1 - t^2} > 0 \) on \( (-1, 1) \).

The **Chebyshev polynomials** are defined by the requirement
\[
T_n(\cos\theta) = \cos n\theta \qquad \text{for all } \theta,
\]
which does determine a polynomial of degree \( n \), and determines it uniquely, since \( \cos\theta \) runs over the whole of \( [-1, 1] \) and two polynomials agreeing on an infinite set are equal (@cor-root-bound-general). The first few are \( T_0 = 1 \), \( T_1 = x \), \( T_2 = 2x^2 - 1 \) (from \( \cos 2\theta = 2\cos^2\theta - 1 \)), and @exr-bessel-parseval-fourier-c2 handles the general case. They are orthogonal for \( \inner{\cdot}{\cdot}_w \):
\[
\inner{T_m}{T_n}_w = 0 \quad (m \ne n), \qquad
\inner{T_n}{T_n}_w = \begin{cases} \pi, & n = 0, \\ \pi/2, & n \ge 1. \end{cases}
\]
For \( m, n \le 2 \) this can be checked by hand, using \( \int_{-1}^{1}\dd t/\sqrt{1 - t^2} = \pi \) and \( \int_{-1}^{1} t^2\,\dd t/\sqrt{1 - t^2} = \pi/2 \) (both come from \( t = \cos\theta \)). The pairs \( (T_0, T_1) \) and \( (T_1, T_2) \) have odd integrands on a symmetric interval, so those integrals are \( 0 \) by the substitution \( t \mapsto -t \). For the remaining pair,
\[
\inner{T_0}{T_2}_w = \int_{-1}^{1}\frac{2t^2 - 1}{\sqrt{1 - t^2}}\,\dd t
= 2\cdot\frac{\pi}{2} - \pi = 0 .
\]

Why should such a weight produce orthogonality? Because it is the trigonometric system in disguise. Substituting \( t = \cos\theta \) turns \( \inner{p}{q}_w \) into \( \int_0^{\pi} p(\cos\theta)q(\cos\theta)\,\dd\theta \), and on the Chebyshev polynomials that integrand is \( \cos m\theta\cos n\theta \) — the very product whose integral we computed in @exm-trigonometric-orthonormal. @exr-bessel-parseval-fourier-c2 asks for this in full.

Since the \( T_n \) are orthogonal but not normalized, projections onto their span are computed with @cor-projection-orthogonal-basis rather than @thm-projection-formula. Section 10 of this chapter takes up orthogonal polynomials as a subject in their own right, including the recurrence that generates the \( T_n \) and the quadrature rules they produce.

## Exercises

### A. Check your understanding

:::: {#exr-bessel-parseval-fourier-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State Bessel's inequality, saying exactly what is assumed about the space and what is assumed about the list.
2. State Parseval's identity, including the condition under which equality holds for a given vector.
3. True or false: Bessel's inequality requires the ambient space to be finite-dimensional. Justify your answer.
4. Write down the inner product used on \( C[-\pi, \pi] \) in this section, including its normalizing constant, and say what the constant is for.
5. State what @thm-fourier-best-approximation gives about \( S_nf \), and name one thing it does not give.
6. True or false: if \( (\e_1, \dots, \e_k) \) is an orthonormal list and \( \sum_i\lvert\inner{\v}{\e_i}\rvert^2 = \norm{\v}^2 \) for one particular \( \v \ne \0 \), then the list is an orthonormal basis of \( V \). Justify your answer.
:::
::::

::: {.solution}
(a) If \( (\e_1, \dots, \e_k) \) is an orthonormal list in an inner product space \( V \) over \( \nR \) or \( \nC \), then \( \sum_{i=1}^{k}\lvert\inner{\v}{\e_i}\rvert^2 \le \norm{\v}^2 \) for every \( \v \in V \) (@thm-bessel-inequality). The list is assumed **finite and orthonormal**; the space is assumed only to be an inner product space, with no dimension hypothesis.

(b) Equality \( \sum_i\lvert\inner{\v}{\e_i}\rvert^2 = \norm{\v}^2 \) holds if and only if \( \v \in \Span(\e_1, \dots, \e_k) \); in particular it holds for every \( \v \) when the list is an orthonormal basis of \( V \) (@thm-parseval-identity).

(c) False. Only the span of the list has to be finite-dimensional, and it automatically is, being spanned by \( k \) vectors. The proof uses @thm-projection-formula, whose hypothesis is that the **subspace** projected onto is finite-dimensional. The application to \( C[-\pi, \pi] \) is exactly a case where \( V \) is not finite-dimensional.

(d) \( \inner{f}{g} = \frac1\pi\int_{-\pi}^{\pi} f(t)g(t)\,\dd t \). The constant \( 1/\pi \) makes \( \cos kx \) and \( \sin kx \) unit vectors for every \( k \ge 1 \); without it their norms would be \( \sqrt{\pi} \).

(e) It gives that \( S_nf \) is the orthogonal projection of \( f \) onto \( W_n \), hence the unique element of \( W_n \) minimizing \( \norm{f - g} \), and it gives Bessel's inequality for the coefficients. It does **not** give that \( S_nf(x) \to f(x) \) at any particular \( x \), nor even that \( \norm{f - S_nf} \to 0 \).

(f) False. Equality for one \( \v \) says only that \( \v \in \Span(\e_1, \dots, \e_k) \) (@thm-parseval-identity). In \( \nR^3 \) take the list \( (\e_1) \) and \( \v = \e_1 \): equality holds, and the list is not a basis.
:::

### B. Practice

:::: {#exr-bessel-parseval-fourier-b1}
[B1: Fourier coefficients]

Work in \( C[-\pi, \pi] \) with \( \inner{f}{g} = \frac1\pi\int_{-\pi}^{\pi} fg \). Find all Fourier coefficients \( a_k \) and \( b_k \) of each of the following, and in each case write down \( S_2f \).

::: {.enumerate options="label=(\alph*)"}
1. \( f(x) = \lvert x \rvert \).
2. \( f(x) = x^2 \).
3. \( f(x) = 3 - 2\sin x + \sin 3x \).
:::
::::

::: {.solution}
(a) \( \lvert t \rvert \sin(kt) \) is odd, so \( b_k = 0 \) for all \( k \). For the cosines, \( \lvert t \rvert\cos(kt) \) is even, so \( a_k = \frac2\pi\int_0^{\pi} t\cos(kt)\,\dd t \). For \( k = 0 \) this is \( \frac2\pi\cdot\frac{\pi^2}{2} = \pi \). For \( k \ge 1 \), integrating by parts,
\[
\int_0^{\pi} t\cos(kt)\,\dd t
= \Big[\frac{t\sin(kt)}{k}\Big]_0^{\pi} - \frac1k\int_0^{\pi}\sin(kt)\,\dd t
= \frac{(-1)^k - 1}{k^2},
\]
since the bracket vanishes and \( \int_0^\pi \sin(kt)\,\dd t = (1 - (-1)^k)/k \). Hence
\[
a_k = \frac{2\big((-1)^k - 1\big)}{\pi k^2} =
\begin{cases} -\dfrac{4}{\pi k^2}, & k \text{ odd},\\[2pt] 0, & k \text{ even},\end{cases}
\]
and \( S_2f = \dfrac{\pi}{2} - \dfrac{4}{\pi}\cos x \).

(b) \( t^2\sin(kt) \) is odd, so \( b_k = 0 \). Also \( a_0 = \frac2\pi\int_0^\pi t^2\,\dd t = \frac{2\pi^2}{3} \). For \( k \ge 1 \), integrating by parts twice gives
\[
\int_0^{\pi} t^2\cos(kt)\,\dd t
= \Big[\frac{t^2\sin(kt)}{k}\Big]_0^\pi - \frac2k\int_0^\pi t\sin(kt)\,\dd t
= \frac{2\pi(-1)^{k}}{k^2},
\]
using \( \int_0^\pi t\sin(kt)\,\dd t = \pi(-1)^{k+1}/k \) from @exm-fourier-of-x. Hence \( a_k = \frac2\pi\cdot\frac{2\pi(-1)^k}{k^2} = \frac{4(-1)^k}{k^2} \), so \( a_1 = -4 \), \( a_2 = 1 \), and
\[
S_2f = \frac{\pi^2}{3} - 4\cos x + \cos 2x .
\]

(c) The function already lies in \( W_3 \). Coefficients against an orthonormal basis are unique (@thm-orthonormal-coordinates (a)), so, applying that result inside \( W_3 \), we may read them off: \( a_0/2 = 3 \), that is \( a_0 = 6 \), together with \( b_1 = -2 \) and \( b_3 = 1 \); every other coefficient is \( 0 \). Hence \( S_2f = 3 - 2\sin x \), which is **not** \( f \): the term \( \sin 3x \) lies outside \( W_2 \) and is discarded by the projection. (From \( n = 3 \) on, \( S_nf = f \), as @thm-projection-formula (a) predicts, since \( f \in W_3 \) and a projection fixes its own subspace.)
:::

:::: {#exr-bessel-parseval-fourier-b2}
[B2: Verifying Bessel for a truncation]

::: {.enumerate options="label=(\alph*)"}
1. In \( \nR^4 \) with the dot product let \( \e_1 = \tfrac12(1, 1, 1, 1) \), \( \e_2 = \tfrac12(1, -1, 1, -1) \) and \( \v = (2, 0, 0, 2) \). Verify @thm-bessel-inequality for \( \v \) and this list, compute the deficit, and check against \( (\ast) \) by computing \( \norm{\v - P_U\v} \) directly, where \( U = \Span(\e_1, \e_2) \).
2. For \( f(x) = \lvert x \rvert \) and \( n = 1 \), write out both sides of @thm-fourier-best-approximation (c) using @exr-bessel-parseval-fourier-b1 (a), and show that the resulting inequality is equivalent to \( 96 \le \pi^4 \).
:::
::::

::: {.solution}
(a) Both vectors have norm \( \tfrac12\sqrt4 = 1 \) and \( \inner{\e_1}{\e_2} = \tfrac14(1 - 1 + 1 - 1) = 0 \), so the list is orthonormal. The coefficients are \( \inner{\v}{\e_1} = \tfrac12(2 + 0 + 0 + 2) = 2 \) and \( \inner{\v}{\e_2} = \tfrac12(2 - 0 + 0 - 2) = 0 \), so the left-hand side of Bessel is \( 4 \), while \( \norm{\v}^2 = 4 + 4 = 8 \). The inequality \( 4 \le 8 \) holds, with deficit \( 4 \). By @thm-projection-formula (a), \( P_U\v = 2\e_1 = (1, 1, 1, 1) \), so \( \v - P_U\v = (1, -1, -1, 1) \) and \( \norm{\v - P_U\v}^2 = 4 \), matching \( (\ast) \).

(b) With \( a_0 = \pi \) and \( a_1 = -4/\pi \), and \( b_1 = 0 \), the left-hand side of (c) for \( n = 1 \) is
\[
\frac{a_0^2}{2} + a_1^2 = \frac{\pi^2}{2} + \frac{16}{\pi^2} .
\]
The right-hand side is \( \norm{f}^2 = \frac1\pi\int_{-\pi}^{\pi} t^2\,\dd t = \frac{2\pi^2}{3} \). So the inequality reads
\[
\frac{\pi^2}{2} + \frac{16}{\pi^2} \le \frac{2\pi^2}{3} ,
\]
that is \( 16/\pi^2 \le 2\pi^2/3 - \pi^2/2 = \pi^2/6 \), that is \( 96 \le \pi^4 \). Since \( \pi > 3.14 \) and \( 3.14^4 > 97 \), the inequality is true, and it is tight: the deficit is \( \pi^2/6 - 16/\pi^2 \approx 0.024 \), so the single cosine \( \cos x \) already captures almost all of \( \lvert x \rvert \).
:::

:::: {#exr-bessel-parseval-fourier-b3}
[B3: The best approximation by \( \Span(1, \cos x) \)]

In \( C[-\pi, \pi] \) with \( \inner{f}{g} = \frac1\pi\int_{-\pi}^{\pi} fg \), let \( U = \Span(1, \cos x) \) and \( f(x) = x^2 \). Find \( P_Uf \) and \( d(f, U)^2 \). *Hint: the list \( (1, \cos x) \) is orthogonal but not orthonormal.*
::::

::: {.solution}
The two functions are orthogonal, since \( \inner{1}{\cos x} = \frac1\pi\int_{-\pi}^{\pi}\cos t\,\dd t = 0 \), and both are non-zero, with \( \inner{1}{1} = 2 \) and \( \inner{\cos x}{\cos x} = 1 \) by @exm-trigonometric-orthonormal. So \( (1, \cos x) \) is an orthogonal basis of \( U \), and @cor-projection-orthogonal-basis gives
\[
P_Uf = \frac{\inner{f}{1}}{2}\cdot 1 + \frac{\inner{f}{\cos x}}{1}\cdot\cos x .
\]
By @exr-bessel-parseval-fourier-b1 (b), \( \inner{f}{1} = a_0 = 2\pi^2/3 \) and \( \inner{f}{\cos x} = a_1 = -4 \). Hence
\[
P_Uf = \frac{\pi^2}{3} - 4\cos x .
\]
For the distance, normalize: \( (1/\sqrt2,\ \cos x) \) is an orthonormal basis of the same \( U \), with coefficients \( \inner{f}{1/\sqrt2} = a_0/\sqrt2 \) and \( \inner{f}{\cos x} = a_1 \). Now \( \norm{f}^2 = \frac1\pi\int_{-\pi}^{\pi} t^4\,\dd t = \frac1\pi\cdot\frac{2\pi^5}{5} = \frac{2\pi^4}{5} \) and the Bessel sum is \( a_0^2/2 + a_1^2 = 2\pi^4/9 + 16 \), so \( (\ast) \) gives
\[
d(f, U)^2 = \frac{2\pi^4}{5} - \frac{2\pi^4}{9} - 16 = \frac{8\pi^4}{45} - 16 \approx 1.32 .
\]
It is positive, as it must be, since \( x^2 \notin U \).
:::

### C. Going deeper

:::: {#exr-bessel-parseval-fourier-c1}
[C1: Parseval for the full trigonometric system]

This exercise uses an **input from analysis that this book does not prove**: the trigonometric system is *complete* in \( C[-\pi, \pi] \), meaning that for every \( f \in C[-\pi, \pi] \),
\[
\frac{a_0^2}{2} + \sum_{k=1}^{\infty}\big(a_k^2 + b_k^2\big) = \frac1\pi\int_{-\pi}^{\pi} f(t)^2\,\dd t .
\]

::: {.enumerate options="label=(\alph*)"}
1. Apply this to \( f(x) = x \) and deduce that \( \sum_{k=1}^{\infty} 1/k^2 = \pi^2/6 \).
2. Hence deduce that \( \sum_{k=1}^{\infty} 1/(2k - 1)^2 = \pi^2/8 \).
3. Say precisely which step used the analysis input, and explain why no result of this section can supply it.
:::
::::

::: {.solution}
(a) By @exm-fourier-of-x, \( a_k = 0 \) for all \( k \) and \( b_k = 2(-1)^{k+1}/k \), so \( b_k^2 = 4/k^2 \); and \( \norm{f}^2 = 2\pi^2/3 \). The stated identity becomes
\[
\sum_{k=1}^{\infty}\frac{4}{k^2} = \frac{2\pi^2}{3},
\]
so \( \sum_{k=1}^{\infty} 1/k^2 = \pi^2/6 \).

(b) All terms are positive and the series converges, so it may be split into its even-index and odd-index parts. The even part is
\[
\sum_{j=1}^{\infty}\frac{1}{(2j)^2} = \frac14\sum_{j=1}^{\infty}\frac{1}{j^2} = \frac{\pi^2}{24}.
\]
Hence the odd part is \( \pi^2/6 - \pi^2/24 = (4\pi^2 - \pi^2)/24 = \pi^2/8 \), which is the claim.

(c) The analysis input is used exactly once, at the equality sign in (a). This section proves only the inequality \( \sum_{k\le n} 4/k^2 \le 2\pi^2/3 \) for each \( n \) (@thm-bessel-inequality), and @thm-parseval-identity turns that inequality into an equality only when \( f \) lies in the span of the finitely many functions used. The function \( x \) lies in no \( W_n \), since every element of \( W_n \) takes equal values at \( -\pi \) and \( \pi \) while \( f(-\pi) = -\pi \ne \pi = f(\pi) \). Passing to the infinite system is a statement about a limit of functions, and nothing in this book proves such a statement.

*Remark.* The classical route to \( \sum 1/(2k-1)^2 = \pi^2/8 \) applies the same identity to the square wave, the function equal to \( -1 \) on \( [-\pi, 0) \) and \( 1 \) on \( [0, \pi] \), whose coefficients are \( b_k = 4/(\pi k) \) for odd \( k \) and \( 0 \) otherwise. That function is not continuous, so it does not live in the space \( C[-\pi, \pi] \) of this section, and enlarging the space to all integrable functions destroys positive definiteness, as the third non-example of Section 1 shows. Working with \( f(x) = x \) keeps everything inside a genuine inner product space.
:::

:::: {#exr-bessel-parseval-fourier-c2}
[C2: Chebyshev orthogonality by substitution]

Let \( \inner{p}{q}_w = \int_{-1}^{1} p(t)q(t)(1 - t^2)^{-1/2}\,\dd t \) on \( \nR[x] \), the Chebyshev inner product of the text.

::: {.enumerate options="label=(\alph*)"}
1. Prove that for every \( n \ge 0 \) there is a polynomial \( T_n \) of degree \( n \) with \( T_n(\cos\theta) = \cos n\theta \) for all \( \theta \), and find \( T_0, T_1, T_2, T_3 \).
2. Prove that \( \inner{p}{q}_w = \int_0^{\pi} p(\cos\theta)\,q(\cos\theta)\,\dd\theta \) for all polynomials \( p, q \).
3. Deduce that \( \inner{T_m}{T_n}_w = 0 \) for \( m \ne n \), and compute \( \inner{T_n}{T_n}_w \).
:::

*Hint for (a): the identity \( \cos((n+1)\theta) + \cos((n-1)\theta) = 2\cos\theta\cos n\theta \).*
::::

::: {.solution}
(a) Induction on \( n \). Take \( T_0 = 1 \) and \( T_1 = x \), which satisfy \( T_0(\cos\theta) = 1 = \cos 0\theta \) and \( T_1(\cos\theta) = \cos\theta \), of degrees \( 0 \) and \( 1 \). Suppose \( T_{n-1} \) and \( T_n \) exist, of degrees \( n - 1 \) and \( n \). Put \( T_{n+1} = 2xT_n - T_{n-1} \). Then for every \( \theta \),
\[
T_{n+1}(\cos\theta) = 2\cos\theta\cos n\theta - \cos((n-1)\theta) = \cos((n+1)\theta)
\]
by the stated identity. Its degree is \( n + 1 \), since the leading term of \( 2xT_n \) has degree \( n + 1 \) and \( T_{n-1} \) has degree \( n - 1 \). This completes the induction, and the recurrence gives \( T_2 = 2x^2 - 1 \) and \( T_3 = 2x(2x^2 - 1) - x = 4x^3 - 3x \).

(b) The integral is improper at both endpoints, so it means the limit as \( \delta \to 0^{+} \) of the integrals over \( [-1 + \delta,\ 1 - \delta] \). On each such interval the integrand is continuous, and \( t = \cos\theta \) is a continuously differentiable bijection from the corresponding \( \theta \)-interval, so the change-of-variables rule applies there. With \( t = \cos\theta \), \( \theta \) running from \( \pi \) down to \( 0 \), we have \( \dd t = -\sin\theta\,\dd\theta \) and \( \sqrt{1 - t^2} = \sin\theta \), which is \( \ge 0 \) on \( [0, \pi] \). The two minus signs cancel when the limits are reversed, and letting \( \delta \to 0^{+} \),
\[
\int_{-1}^{1}\frac{p(t)q(t)}{\sqrt{1 - t^2}}\,\dd t
= \int_{0}^{\pi} p(\cos\theta)\,q(\cos\theta)\,\dd\theta .
\]
The right-hand side is a proper integral of a continuous function, so both sides converge, and the limits agree.

(c) By (a) and (b), \( \inner{T_m}{T_n}_w = \int_0^{\pi}\cos m\theta\cos n\theta\,\dd\theta \). Using \( \cos A\cos B = \tfrac12[\cos(A-B) + \cos(A+B)] \) and \( \int_0^{\pi}\cos(p\theta)\,\dd\theta = [\sin(p\theta)/p]_0^{\pi} = 0 \) for every non-zero integer \( p \):

if \( m \ne n \), then \( m - n \ne 0 \), and \( m + n \ge 1 \) because the two indices differ, so both integrals vanish and the value is \( 0 \);

if \( m = n \ge 1 \), the value is \( \tfrac12\big(\int_0^\pi 1\,\dd\theta + 0\big) = \pi/2 \);

if \( m = n = 0 \), the integrand is \( 1 \) and the value is \( \pi \).

So the \( T_n \) are orthogonal for \( \inner{\cdot}{\cdot}_w \), with \( \inner{T_0}{T_0}_w = \pi \) and \( \inner{T_n}{T_n}_w = \pi/2 \) for \( n \ge 1 \). Consequently \( \big(T_0/\sqrt{\pi},\ T_1\sqrt{2/\pi},\ \dots,\ T_n\sqrt{2/\pi}\big) \) is an orthonormal list, and @thm-bessel-inequality applies to it verbatim.
:::
