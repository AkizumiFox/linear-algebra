# Convex Functions

The chapter so far has studied convex **sets**. Convex **functions** have been in the book for longer, as the first subsection recalls, and every finite support function of §04 is one too. This section defines the notion, ties it to convex sets through the epigraph, and proves its basic theorems: Jensen's inequality, the convexity of a supremum of affine functions, which pays a promise of Chapter 17 §06, a second-derivative test, and continuity. §11 then spends them on three classical inequalities.

**Throughout, the field is \( \nR \).** \( V \) is a real vector space, and a set \( C \subseteq V \) called convex is convex in the sense of @def-convex-set. From the second-derivative test onward we work in \( \nR^n \), with the standard inner product and its norm \( \norm{\cdot} = \norm{\cdot}_2 \). A function \( g \) on an interval of \( \nR \) is **increasing** when \( s \le t \) implies \( g(s) \le g(t) \), as in Chapter 17 §11, and **strictly increasing** when \( s < t \) implies \( g(s) < g(t) \).

## Convex functions and their epigraphs

Look again at three inequalities the book has already proved. For a norm, (N2) and (N3) of @def-norm give \( \norm{t\x + (1-t)\y} \le t\norm{\x} + (1-t)\norm{\y} \) for \( 0 \le t \le 1 \). For the top partial sum \( s_k(\A) = \sum_{i \le k}\lambda_i(\A) \) of a Hermitian matrix, Chapter 17 §06 derived \( s_k(t\A + (1-t)\B) \le ts_k(\A) + (1-t)s_k(\B) \) from @cor-ky-fan-subadditive. And the case \( n = 1 \) of operator convexity in @def-operator-monotone (b) reads \( f(t a + (1-t)b) \le tf(a) + (1-t)f(b) \) for numbers \( a, b \). It is the same inequality three times, and it deserves a name.

*A function is convex when, on every segment of its domain, its graph lies on or below the chord.*

::: {#def-convex-function}
[Convex Function]

Let \( C \) be a **non-empty convex** subset of a real vector space \( V \), and let \( f \colon C \to \nR \). Then \( f \) is **convex** if
\[
f\bigl(t\x + (1-t)\y\bigr) \ \le\ tf(\x) + (1-t)f(\y)
\]
for **all** \( \x, \y \in C \) and **all** real \( t \) with \( 0 \le t \le 1 \). It is **strictly convex** if the inequality is **strict** whenever \( \x \ne \y \) and \( 0 < t < 1 \). It is **concave**, or **strictly concave**, if \( -f \) is convex, or strictly convex.

The **epigraph** of \( f \) is the subset of the real vector space \( V \times \nR \), with componentwise operations,
\[
\operatorname{epi} f = \{ (\x, s) \in V \times \nR : \x \in C,\ s \ge f(\x) \} .
\]
:::

In words: take any two points \( \x \) and \( \y \) of the domain and any point \( t\x + (1-t)\y \) between them. The left side is the value of \( f \) there. The right side is the value, at the same place, of the straight line through \( (\x, f(\x)) \) and \( (\y, f(\y)) \). So the condition says the chord is never below the graph. Strict convexity forbids the graph to touch the chord anywhere strictly between two distinct points. The epigraph is everything on or above the graph.

**The domain must be convex, and this is the only thing to check.** The point \( t\x + (1-t)\y \) must lie in \( C \), or \( f \) is not defined there. That is exactly what @def-convex-set guarantees.

\begin{center}
\begin{tikzpicture}[scale=0.95]
  \fill[gray!20] (-2.2,3.2) -- plot[smooth] coordinates
    {(-2.2,1.694) (-1.7,1.0115) (-1.2,0.504) (-0.7,0.1715) (-0.2,0.014)
     (0.3,0.0315) (0.8,0.224) (1.3,0.5915) (1.8,1.134) (2.3,1.8515) (2.8,2.744)}
    -- (2.8,3.2) -- cycle;
  \draw[->] (-2.6,0) -- (3.3,0);
  \draw[very thick] plot[smooth] coordinates
    {(-2.2,1.694) (-1.7,1.0115) (-1.2,0.504) (-0.7,0.1715) (-0.2,0.014)
     (0.3,0.0315) (0.8,0.224) (1.3,0.5915) (1.8,1.134) (2.3,1.8515) (2.8,2.744)};
  \draw[thick, dashed] (-1.5,0.7875) -- (2.5,2.1875);
  \node[circle, fill, inner sep=1.3pt] at (-1.5,0.7875) {};
  \node[circle, fill, inner sep=1.3pt] at (2.5,2.1875) {};
  \node[left] at (-1.55,0.95) {$(x, f(x))$};
  \node[right] at (2.55,2.1) {$(y, f(y))$};
  \node at (0.2,2.6) {$\operatorname{epi} f$};
\end{tikzpicture}
\end{center}

The picture shows \( f(x) = 0.35x^2 \) on \( \nR \): the dashed chord lies above the graph between its endpoints, and the shaded region is the epigraph.

::: {#exm-first-convex-functions}
[First convex functions]

Check each against @def-convex-function.

::: {.enumerate options="label=(\alph*)"}
1. An **affine function** \( a(\x) = \varphi(\x) + c \), with \( \varphi \) a linear functional on \( V \) (@def-linear-functional) and \( c \in \nR \).
2. A norm \( \norm{\cdot} \) on \( \nR^n \).
3. \( f(x) = x^2 \) on \( \nR \), and more generally \( q(\x) = \x\tp\A\x \) on \( \nR^n \) for a symmetric \( \A \succeq 0 \).
:::
:::

::: {.solution}
(a) Since \( \varphi \) is linear and \( c = tc + (1-t)c \),
\[
a\bigl(t\x + (1-t)\y\bigr) = t\varphi(\x) + (1-t)\varphi(\y) + tc + (1-t)c = ta(\x) + (1-t)a(\y) .
\]
Equality holds, so \( a \) is convex, and so is \( -a \): an affine function is both convex and concave, and neither strictly. The constant functions are the degenerate case \( \varphi = 0 \). They matter because they show that convexity by itself forces no growth at all.

(b) By (N3) and then (N2) of @def-norm, with \( \lvert t \rvert = t \) and \( \lvert 1 - t\rvert = 1 - t \) for \( 0 \le t \le 1 \),
\[
\norm{t\x + (1-t)\y} \le \norm{t\x} + \norm{(1-t)\y} = t\norm{\x} + (1-t)\norm{\y} .
\]
A norm is not strictly convex: on the ray through a non-zero \( \x \), \( \norm{s\x} = s\norm{\x} \) is linear in \( s \ge 0 \), so the chord between \( \x \) and \( 2\x \) lies on the graph.

(c) Expanding and collecting terms,
\[
tx^2 + (1-t)y^2 - \bigl(tx + (1-t)y\bigr)^2 = t(1-t)(x - y)^2 \ \ge\ 0 ,
\]
and the right side is strictly positive when \( x \ne y \) and \( 0 < t < 1 \). So \( x^2 \) is strictly convex. The same expansion with \( \A \) symmetric gives
\[
tq(\x) + (1-t)q(\y) - q\bigl(t\x + (1-t)\y\bigr) = t(1-t)\,q(\x - \y) ,
\]
and \( q(\x - \y) = \inner{\A(\x - \y)}{\x - \y} \ge 0 \) by (P2) of @def-positive-semidefinite. So \( q \) is convex. The case \( n = 1 \), \( \A = (1) \), is \( x^2 \).
:::

**A non-example by minimal change.** Replace \( x^2 \) by \( x^3 \) on \( \nR \). With \( x = -2 \), \( y = 0 \) and \( t = \tfrac12 \), the left side is \( (-1)^3 = -1 \) and the right side is \( \tfrac12(-8) + \tfrac12 \cdot 0 = -4 \), and \( -1 \le -4 \) is false. What fails is the inequality for this pair, on the negative half-line, where the graph bends downward. On the convex domain \( (0, \infty) \) the same function is convex, as the one-variable test below shows. So convexity depends on the domain.

**Why this definition.** The inequality is non-strict so that affine functions and norms, the most important examples, qualify. Requiring it for every \( t \in [0, 1] \), not just \( t = \tfrac12 \), is what makes Jensen's inequality below immediate. The name comes from the epigraph: a function is convex exactly when the set above its graph is convex.

::: {#prp-epigraph-convex}
[Convex Function, Convex Epigraph]

Let \( C \subseteq V \) be non-empty and convex, and let \( f \colon C \to \nR \). Then \( f \) is convex if and only if \( \operatorname{epi} f \) is a convex subset of \( V \times \nR \).
:::

::: {.idea}
A point \( (\x, s) \) lies in the epigraph exactly when \( s \ge f(\x) \). So the chord inequality for \( f \) and the statement that segments between points of the epigraph stay in it are one inequality, read in two directions.
:::

::: {.proof}
\( (\Rightarrow) \) Let \( (\x, s), (\y, u) \in \operatorname{epi} f \) and \( 0 \le t \le 1 \). The point \( t\x + (1-t)\y \) lies in \( C \), since \( C \) is convex, and
\[
f\bigl(t\x + (1-t)\y\bigr) \le tf(\x) + (1-t)f(\y) \le ts + (1-t)u ,
\]
the second step because \( f(\x) \le s \), \( f(\y) \le u \) and \( t, 1-t \ge 0 \). So \( t(\x, s) + (1-t)(\y, u) \in \operatorname{epi} f \).

\( (\Leftarrow) \) Let \( \x, \y \in C \) and \( 0 \le t \le 1 \). The points \( (\x, f(\x)) \) and \( (\y, f(\y)) \) lie in \( \operatorname{epi} f \), so by convexity so does \( \bigl(t\x + (1-t)\y,\ tf(\x) + (1-t)f(\y)\bigr) \). By the definition of the epigraph this says \( f(t\x + (1-t)\y) \le tf(\x) + (1-t)f(\y) \). This proves the proposition.
:::

The same one-line argument shows that every **sublevel set** \( \{\x \in C : f(\x) \le c\} \) of a convex \( f \) is convex: if \( f(\x) \le c \) and \( f(\y) \le c \), then \( f(t\x + (1-t)\y) \le tc + (1-t)c = c \).

::: {.check}
Every sublevel set of a convex function is convex. Is the converse true? Is a function \( f \colon \nR \to \nR \) whose sublevel sets are all convex necessarily convex?
:::

::: {.solution}
No. Take \( f(x) = x^3 \). It is increasing: if \( a < b \) then \( b^3 - a^3 = (b - a)(a^2 + ab + b^2) > 0 \), since \( a^2 + ab + b^2 = (a + \tfrac{b}{2})^2 + \tfrac34b^2 \) vanishes only at \( a = b = 0 \). So if \( x \le z \le y \) and \( x^3, y^3 \le c \), then \( z^3 \le y^3 \le c \). Each sublevel set is therefore an interval, which is convex. But \( x^3 \) is not convex on \( \nR \), by the non-example above.
:::

::: {.warning}
**A convex function need not be differentiable.** The function \( \lvert x \rvert \) is a norm on \( \nR \), hence convex, and it has a corner at \( 0 \): its difference quotients \( \lvert h\rvert/h \) are \( 1 \) for \( h > 0 \) and \( -1 \) for \( h < 0 \), so they have no limit. The same corner appears in linear algebra. The map \( \A \mapsto \lambda_1(\A) \) on Hermitian matrices is convex, as the next two subsections prove, and on the diagonal matrices \( \diag(t, -t) \) it equals \( \lvert t \rvert \). The corner sits at \( t = 0 \), where the top eigenvalue is repeated.
:::

## Jensen's inequality

The definition speaks of two points. Induction extends it to any finite convex combination (@def-convex-combination), and that extension is the form in which convexity is most often used.

::: {#thm-jensen}
[Jensen's Inequality]

Let \( C \subseteq V \) be non-empty and convex, and let \( f \colon C \to \nR \) be convex. Let \( \x_1, \dots, \x_m \in C \), and let \( w_1, \dots, w_m \ge 0 \) with \( w_1 + \dots + w_m = 1 \). Then \( \sum_i w_i\x_i \in C \) and
\[
f\Bigl(\sum_{i=1}^{m} w_i\x_i\Bigr) \ \le\ \sum_{i=1}^{m} w_if(\x_i) .
\]
If \( f \) is **strictly** convex and every \( w_i > 0 \), equality holds only when \( \x_1 = \x_2 = \dots = \x_m \).
:::

::: {.idea}
Split off the last point. The remaining weights add up to \( s = 1 - w_m \), and after dividing by \( s \) they are the weights of a convex combination \( \y \) of \( m - 1 \) points, to which induction applies. The whole combination is then \( s\y + w_m\x_m \), a combination of **two** points, which is where the definition applies.
:::

::: {.proof}
We prove both statements by induction on \( m \ge 1 \). For \( m = 1 \) the weight is \( w_1 = 1 \), both sides equal \( f(\x_1) \), and the equality clause is empty.

Let \( m \ge 2 \) and assume both statements for \( m - 1 \) points. If \( w_m = 1 \), every other weight is \( 0 \), both sides equal \( f(\x_m) \), and the equality clause does not apply since \( w_1 = 0 \). Otherwise \( s = 1 - w_m = w_1 + \dots + w_{m-1} > 0 \). The numbers \( w_i/s \) for \( i < m \) are non-negative with sum \( 1 \), so by the inductive hypothesis \( \y = \sum_{i<m}(w_i/s)\x_i \) lies in \( C \) and
\[
f(\y) \le \sum_{i<m}\frac{w_i}{s}f(\x_i) .
\tag{1}
\]
Now \( \sum_{i=1}^m w_i\x_i = s\y + w_m\x_m \) with \( s + w_m = 1 \), so this point lies in \( C \) because \( C \) is convex, and @def-convex-function gives
\[
\begin{aligned}
f(s\y + w_m\x_m) &\le sf(\y) + w_mf(\x_m) \\
&\le \sum_{i<m}w_if(\x_i) + w_mf(\x_m) ,
\end{aligned}
\tag{2}
\]
where the second step multiplies (1) by \( s > 0 \). This proves the inequality.

For the equality clause, let \( f \) be strictly convex and every \( w_i > 0 \), so that \( 0 < w_m < 1 \) and \( 0 < s < 1 \). If equality holds in the theorem, both inequalities in (2) are equalities. The second is \( s \) times (1), so (1) is an equality, and the inductive hypothesis gives \( \x_1 = \dots = \x_{m-1} \); then \( \y \) equals this common point. The first is the two-point inequality with weights strictly between \( 0 \) and \( 1 \), so strict convexity forces \( \y = \x_m \). Hence all \( m \) points are equal, as claimed.
:::

In the language of §01, the points \( (\x_i, f(\x_i)) \) lie in the convex set \( \operatorname{epi} f \), and Jensen's inequality says that their convex combinations stay there. That is @thm-convex-hull-combinations read inside the epigraph.

## Suprema of affine functions

Chapter 17 §06 showed that \( s_k(\A) = \sum_{i\le k}\lambda_i(\A) \) is the largest of the linear functions \( \A \mapsto \tr(\Q^{*}\A\Q) \), deduced its convexity, and ended with a promise: "Chapter 18 studies convex functions in general, and the observation that a pointwise supremum of linear functions is convex is one of its basic facts." Here is that fact, stated for affine functions, which include the linear ones.

::: {#prp-sup-of-affine-convex}
[A Supremum of Affine Functions Is Convex]

Let \( C \subseteq V \) be non-empty and convex, and let \( (a_i)_{i \in I} \) be a non-empty family of affine functions on \( V \). Suppose that for every \( \x \in C \) the set \( \{a_i(\x) : i \in I\} \) is bounded above, and put
\[
g(\x) = \sup_{i \in I} a_i(\x) \qquad (\x \in C) .
\]
Then \( g \colon C \to \nR \) is convex.
:::

::: {.idea}
Each \( a_i \) meets its own chord inequality with equality, and each lies below \( g \). So at a point between \( \x \) and \( \y \), every \( a_i \) is at most the chord of \( g \), and therefore so is their supremum.
:::

::: {.proof}
The supremum exists for each \( \x \in C \) by completeness, fact (A1) of Chapter 16's introduction. Let \( \x, \y \in C \) and \( 0 \le t \le 1 \). For each \( i \in I \), by @exm-first-convex-functions (a) and then \( a_i \le g \) at \( \x \) and at \( \y \),
\[
a_i\bigl(t\x + (1-t)\y\bigr) = ta_i(\x) + (1-t)a_i(\y) \le tg(\x) + (1-t)g(\y) ,
\]
where the inequality uses \( t \ge 0 \) and \( 1 - t \ge 0 \). So the right side is an upper bound for the set \( \{a_i(t\x + (1-t)\y) : i \in I\} \), and it is therefore at least that set's least upper bound, \( g(t\x + (1-t)\y) \). This proves the proposition.
:::

The proof never used that the \( a_i \) are affine beyond the fact that each is convex. So the same argument shows that **a pointwise supremum of convex functions is convex**, whenever it is finite. In particular the maximum of two convex functions is convex. The minimum need not be: \( \min(x, -x) = -\lvert x\rvert \) is concave and not convex.

**Instances.** Many convex functions of this chapter are suprema of linear functions, and this proposition proves their convexity at a stroke.

- \( \lvert x\rvert = \max(x, -x) \); \( \norm{\x}_\infty = \max_i\max(x_i, -x_i) \); and \( \norm{\x}_1 = \max\{\inner{\vepsilon}{\x} : \vepsilon \in \{\pm1\}^n\} \), the maximum being attained at the vector of signs of \( \x \).
- The support function \( h_K(\y) \) of @def-support-function is the supremum over \( \x \in K \) of the linear functions \( \y \mapsto \inner{\x}{\y} \). So it is convex wherever it is finite, and in particular the dual norm of @def-dual-norm is convex.
- Every norm is the maximum of \( \x \mapsto \inner{\x}{\y} \) over \( \norm{\y}_* \le 1 \) (@cor-norm-as-max). This describes the norm; it is not a new proof of its convexity, since §04 derived the corollary from the triangle inequality.
- The largest eigenvalue: by @lem-extreme-eigenvalues-quadratic-form, \( \lambda_1(\A) = \max_{\norm{\x} = 1}\inner{\A\x}{\x} \), and each \( \A \mapsto \inner{\A\x}{\x} \) is linear.
- The Ky Fan sums \( s_k \), the case that prompted the promise. They are the subject of the next subsection.

## Convex functions of a Hermitian matrix

Let \( F = \nR \) or \( F = \nC \). The Hermitian \( n \times n \) matrices over \( F \) form a **real** vector space: if \( \A^{*} = \A \), \( \B^{*} = \B \) and \( s, t \in \nR \), then \( (s\A + t\B)^{*} = s\A + t\B \). They do not form a complex one, since \( (i\I)^{*} = -i\I \). This is the space on which Chapter 17 §06 called \( s_k \) convex, and it is the setting here. When \( F = \nC \) it is an instance of the chapter's convention that a complex space is treated as a real one.

::: {#cor-eigenvalue-sums-convex}
[The Top Eigenvalue Sums Are Convex]

Let \( 1 \le k \le n \). On the real vector space of Hermitian \( n \times n \) matrices over \( F \), the function
\[
s_k(\A) = \lambda_1(\A) + \dots + \lambda_k(\A)
\]
is convex. In particular \( \A \mapsto \lambda_1(\A) \) is convex, and \( \A \mapsto \lambda_n(\A) \) is concave.
:::

::: {.idea}
Ky Fan's theorem writes \( s_k \) as a maximum of the functions \( \A \mapsto \tr(\Q^{*}\A\Q) \), each linear on the real space of Hermitian matrices, so @prp-sup-of-affine-convex applies. For \( \lambda_n \), change the sign of \( \A \).
:::

::: {.proof}
By @thm-ky-fan, \( s_k(\A) = \max\{\tr(\Q^{*}\A\Q) : \Q \in M_{n\times k}(F),\ \Q^{*}\Q = \I_k\} \). Fix such a \( \Q \). The matrix \( \Q^{*}\A\Q \) is Hermitian, so its diagonal entries, and hence its trace, are real. By @thm-trace-properties (1), \( \A \mapsto \tr(\Q^{*}\A\Q) \) respects sums and real multiples. So it is a linear functional on the real space of Hermitian matrices, and \( s_k \) is the maximum of this family. By @prp-sup-of-affine-convex, \( s_k \) is convex, and \( k = 1 \) gives \( \lambda_1 \).

For \( \lambda_n \), the eigenvalues of \( -\A \) are the negatives of those of \( \A \), so \( \lambda_n(\A) = -\lambda_1(-\A) \), as in the proof of @cor-trace-min. The map \( \A \mapsto \lambda_1(-\A) \) is convex, because it is the convex \( \lambda_1 \) composed with the linear map \( \A \mapsto -\A \), and a convex function composed with a linear map is convex, by substituting into @def-convex-function. So \( \lambda_n \) is the negative of a convex function, that is, concave.
:::

This is the fact Chapter 17 §06 anticipated, and its promise is now paid. Chapter 17 reached convexity by a different path: @cor-ky-fan-subadditive gives \( s_k(\A + \B) \le s_k(\A) + s_k(\B) \), and positive homogeneity \( s_k(t\A) = ts_k(\A) \), \( t \ge 0 \), turns subadditivity into convexity. Exercise C1 shows that the two paths are the same, and the warning at the end of Chapter 17 §06 still stands: a single \( \lambda_k \) with \( 1 < k < n \), the difference \( s_k - s_{k-1} \) of two convex functions, is neither convex nor concave.

**What is not proved here.** For a convex \( f \) on an interval, \( \A \mapsto \tr f(\A) = \sum_i f(\lambda_i(\A)) \) is convex on the Hermitian matrices with spectrum in that interval, a statement about sums over the spectrum and far weaker than the operator convexity of Chapter 17 §11. It is proved in Chapter 21, and nothing in this chapter uses it.

## A second-derivative test

For a function on an interval, convexity says the slope never decreases. The mean value theorem turns an increasing derivative into a chord inequality.

::: {#lem-convex-one-variable}
[Increasing Derivative Gives Convexity]

Let \( I \subseteq \nR \) be an open interval and let \( g \colon I \to \nR \) be differentiable. If \( g' \) is increasing on \( I \), then \( g \) is convex; if \( g' \) is strictly increasing, then \( g \) is strictly convex. In particular, if \( g \) is twice differentiable with \( g'' \ge 0 \) on \( I \), then \( g \) is convex, and if \( g'' > 0 \) on \( I \), then \( g \) is strictly convex.
:::

::: {.idea}
Split the chord at the intermediate point \( z \) into two sub-chords, over \( [x, z] \) and over \( [z, y] \). By the mean value theorem, each slope is a value of \( g' \) inside its interval, so an increasing \( g' \) makes the left slope at most the right one. A graph whose chord slopes increase in this way lies below the long chord.
:::

::: {.proof}
Let \( x, y \in I \) and \( 0 < t < 1 \); the cases \( t = 0 \), \( t = 1 \) and \( x = y \) are equalities. Exchanging \( x \) with \( y \) and \( t \) with \( 1 - t \) if necessary, we may assume \( x < y \). Put \( z = tx + (1-t)y \), so that \( x < z < y \), with
\[
z - x = (1-t)(y - x), \qquad y - z = t(y - x) .
\]
By the mean value theorem, fact (A6) of Chapter 16's introduction, applied on \( [x, z] \) and on \( [z, y] \), there are \( c_1 \in (x, z) \) and \( c_2 \in (z, y) \) with
\[
g(z) - g(x) = (1-t)(y-x)\,g'(c_1), \qquad g(y) - g(z) = t(y-x)\,g'(c_2) .
\]
Since \( c_1 < c_2 \) and \( g' \) is increasing, \( g'(c_1) \le g'(c_2) \). Multiplying by \( t(1-t)(y - x) > 0 \),
\[
\begin{aligned}
t\bigl(g(z) - g(x)\bigr) &= t(1-t)(y-x)\,g'(c_1) \\
&\le t(1-t)(y-x)\,g'(c_2) = (1-t)\bigl(g(y) - g(z)\bigr) .
\end{aligned}
\]
Rearranged, this is \( g(z) \le tg(x) + (1-t)g(y) \). If \( g' \) is strictly increasing, then \( g'(c_1) < g'(c_2) \), and every inequality is strict.

For the last sentence, let \( a < b \) in \( I \). Fact (A6) applied to \( g' \) gives \( g'(b) - g'(a) = g''(c)(b - a) \) for some \( c \in (a, b) \). This is \( \ge 0 \) when \( g'' \ge 0 \), and \( > 0 \) when \( g'' > 0 \). So \( g' \) is increasing, or strictly increasing, and the first part applies.
:::

Derivatives of polynomials, here and below, come from Chapter 10 §09: a polynomial is a power series with finitely many non-zero coefficients, so it converges for every real argument and that section's fact (A2) differentiates it term by term, while its fact (A3), the linearity of differentiation, handles sums and constant multiples; a partial derivative is such a derivative with the other variables fixed. For instance, \( g(x) = x^4 \) has \( g'(x) = 4x^3 \), which is strictly increasing (the Quick check after @prp-epigraph-convex), so \( x^4 \) is strictly convex on \( \nR \). Likewise \( x^3 \), with \( g'' = 6x \ge 0 \) on \( (0, \infty) \), is convex there, which is the claim made after the non-example.

In several variables the second derivative is the Hessian \( \H_f(\a) \) of @def-hessian, and "\( g'' \ge 0 \)" becomes "positive semidefinite". Chapter 14 §06 read the Hessian at a single critical point, where its definiteness decides a local extremum (@thm-second-derivative-test). Here the Hessian is asked to be positive semidefinite at **every** point, and what it decides is global. Restricting \( f \) to lines would need a chain rule the book has not imported, so the proof below uses only Chapter 14 §06's (A1), that \( \H_f(\a) \) is symmetric, and its (A2), Taylor's theorem with a remainder \( r(\h) \) satisfying \( r(\h)/\norm{\h}^2 \to 0 \). It works with **second differences**, which (A2) controls directly.

::: {#thm-convex-second-derivative}
[Convexity from the Hessian]

Let \( U \subseteq \nR^n \) be a non-empty open convex set, and let \( f \colon U \to \nR \) be twice continuously differentiable.

::: {.enumerate options="label=(\alph*)"}
1. \( f \) is convex on \( U \) if and only if \( \H_f(\a) \succeq 0 \) for every \( \a \in U \).
2. If \( \H_f(\a) \succ 0 \) for every \( \a \in U \), then \( f \) is strictly convex on \( U \).
:::
:::

::: {.idea}
Taylor's theorem at \( \z \), applied at \( \z + s\v \) and at \( \z - s\v \) and added, kills the gradient term:
\[
\frac{f(\z + s\v) + f(\z - s\v) - 2f(\z)}{s^2} \ \longrightarrow\ \v\tp\H_f(\z)\v .
\]
For \( (\Rightarrow) \), convexity makes the left side \( \ge 0 \), so the limit is too. For the other direction, restrict \( f \) to a segment and subtract the chord. If the difference were positive somewhere, it would have an interior maximum, and at a maximum every second difference is \( \le 0 \). That contradicts a **strictly** positive limit. So the argument handles \( \H_f \succ 0 \) first, and reaches \( \H_f \succeq 0 \) by adding \( \varepsilon\norm{\x}^2 \) and letting \( \varepsilon \to 0 \).
:::

::: {.proof}
Write \( \H(\z) = \H_f(\z) \). For \( \z \in U \), \( \v \in \nR^n \) and real \( s \ne 0 \) small enough that \( \z \pm s\v \in U \), put
\[
\Delta(\z, \v, s) = f(\z + s\v) + f(\z - s\v) - 2f(\z) .
\]

**Step 1: the second difference.** We claim \( \Delta(\z, \v, s)/s^2 \to \v\tp\H(\z)\v \) as \( s \to 0 \). If \( \v = \0 \) both sides are \( 0 \). Otherwise Chapter 14 §06's (A2) at \( \z \), with \( \h = s\v \) and with \( \h = -s\v \), gives
\[
f(\z \pm s\v) = f(\z) \pm s\,\nabla f(\z)\cdot\v + \tfrac12 s^2\,\v\tp\H(\z)\v + r(\pm s\v) .
\]
Adding the two and subtracting \( 2f(\z) \),
\[
\begin{aligned}
\frac{\Delta(\z, \v, s)}{s^2}
&= \v\tp\H(\z)\v \\
&\qquad + \norm{\v}^2\Bigl(\frac{r(s\v)}{\norm{s\v}^2} + \frac{r(-s\v)}{\norm{s\v}^2}\Bigr) ,
\end{aligned}
\]
and the bracket tends to \( 0 \) because \( \norm{\pm s\v} \to 0 \). The same expansion shows that \( f \) is continuous: \( f(\z + \h) - f(\z) = \nabla f(\z)\cdot\h + \tfrac12\h\tp\H(\z)\h + \norm{\h}^2\cdot r(\h)/\norm{\h}^2 \), and each term tends to \( 0 \) as \( \h \to \0 \).

**Step 2: (a), \( (\Rightarrow) \).** Let \( f \) be convex, \( \a \in U \) and \( \v \in \nR^n \). For small \( s \ne 0 \), \( \a = \tfrac12(\a + s\v) + \tfrac12(\a - s\v) \), so \( f(\a) \le \tfrac12 f(\a + s\v) + \tfrac12 f(\a - s\v) \), that is, \( \Delta(\a, \v, s) \ge 0 \). Dividing by \( s^2 > 0 \) and letting \( s \to 0 \), Step 1 gives \( \v\tp\H(\a)\v \ge 0 \), since a non-strict inequality survives a limit. The matrix \( \H(\a) \) is symmetric by Chapter 14 §06's (A1), so \( \H(\a) \succeq 0 \) by @def-positive-semidefinite.

**Step 3: a maximum principle.** Let \( \x \ne \y \) in \( U \), put \( \v = \y - \x \), and let \( \phi \colon U \to \nR \) be continuous with the following property: for every point \( \z = \x + t\v \) with \( 0 < t < 1 \), the limit \( L(\z) = \lim_{s\to0}\bigl(\phi(\z + s\v) + \phi(\z - s\v) - 2\phi(\z)\bigr)/s^2 \) exists and is **strictly positive**. We claim
\[
\phi\bigl(\x + t\v\bigr) < (1-t)\phi(\x) + t\phi(\y) \qquad (0 < t < 1) .
\]
Define \( h(t) = \phi(\x + t\v) - (1-t)\phi(\x) - t\phi(\y) \) on \( [0, 1] \). Every point of the segment lies in \( U \), since \( U \) is convex. So \( h \) is continuous, and \( h(0) = h(1) = 0 \). The subtracted part is affine in \( t \), so its second differences vanish, and \( h(t+s) + h(t-s) - 2h(t) = \phi(\z + s\v) + \phi(\z - s\v) - 2\phi(\z) \) with \( \z = \x + t\v \).

Suppose \( h(t_1) \ge 0 \) for some \( t_1 \in (0, 1) \). The interval \( [0, 1] \) is closed and bounded, hence compact by fact (A3) of Chapter 16's introduction, so by the extreme value theorem, fact (A4), \( h \) attains a maximum value \( M \) at some point. Then \( M \ge h(t_1) \ge 0 \). If the maximum is attained only at \( 0 \) or \( 1 \), then \( M = 0 \le h(t_1) \), so \( t_1 \) attains it too. Either way, \( M = h(t^{*}) \) for some \( t^{*} \in (0, 1) \). For \( 0 < s < \min(t^{*}, 1 - t^{*}) \), both \( h(t^{*} \pm s) \le h(t^{*}) \), so the second difference of \( h \) at \( t^{*} \) is \( \le 0 \), and so is its limit \( L(\x + t^{*}\v) \). This contradicts \( L > 0 \). Hence \( h < 0 \) on \( (0, 1) \), which is the claim.

**Step 4: (b).** Let \( \H(\z) \succ 0 \) for every \( \z \in U \). By Step 1, \( \phi = f \) has \( L(\z) = \v\tp\H(\z)\v > 0 \) whenever \( \v \ne \0 \), and it is continuous. So Step 3 gives \( f((1-t)\x + t\y) < (1-t)f(\x) + tf(\y) \) for all \( \x \ne \y \) in \( U \) and \( 0 < t < 1 \). Renaming \( t \) as \( 1 - t \), this is strict convexity.

**Step 5: (a), \( (\Leftarrow) \).** Let \( \H(\z) \succeq 0 \) for every \( \z \in U \). Let \( \x \ne \y \) in \( U \), \( \v = \y - \x \), \( 0 < t < 1 \), and \( \varepsilon > 0 \). Put \( \phi(\z) = f(\z) + \varepsilon\norm{\z}^2 \), which is continuous. Expanding the norms,
\[
\norm{\z + s\v}^2 + \norm{\z - s\v}^2 - 2\norm{\z}^2 = 2s^2\norm{\v}^2 ,
\]
so by Step 1 the limit for \( \phi \) is \( L(\z) = \v\tp\H(\z)\v + 2\varepsilon\norm{\v}^2 \ge 2\varepsilon\norm{\v}^2 > 0 \). Step 3 applies. With \( \w = (1-t)\x + t\y \), it gives
\[
\begin{aligned}
f(\w) + \varepsilon\norm{\w}^2
&< (1-t)\bigl(f(\x) + \varepsilon\norm{\x}^2\bigr) \\
&\qquad + t\bigl(f(\y) + \varepsilon\norm{\y}^2\bigr) .
\end{aligned}
\]
Let \( \varepsilon \to 0 \) through \( \varepsilon = 1/k \). The inequality survives as a non-strict one, and gives \( f(\w) \le (1-t)f(\x) + tf(\y) \). The cases \( \x = \y \), \( t = 0 \) and \( t = 1 \) are equalities. So \( f \) is convex. This proves the theorem.
:::

For \( n = 1 \), part (a) says that a twice continuously differentiable \( g \) on an open interval is convex exactly when \( g'' \ge 0 \), and its "if" half is @lem-convex-one-variable again.

::: {.check}
The function \( f(x) = x^4 \) is strictly convex on \( \nR \). Is its Hessian, the \( 1 \times 1 \) matrix \( (f''(x)) \), positive definite at every point? What does this say about part (b)?
:::

::: {.solution}
No. \( f''(x) = 12x^2 \) vanishes at \( x = 0 \), so the \( 1 \times 1 \) matrix \( (0) \) is positive semidefinite but not positive definite. Yet \( f \) is strictly convex, as shown after @lem-convex-one-variable. So the converse of part (b) fails: strict convexity does not force a positive definite Hessian.
:::

Convexity is tested segment by segment, so \( f \) is convex exactly when its restriction \( t \mapsto f(\x + t\v) \) to every line is convex. The phrase *every line* matters.

::: {.warning}
**Convex along every line through one point is not enough.** Let \( f(x, y) = x^2y^2 \) on \( \nR^2 \). On each line through the origin, \( f(t\v) = t^4\,v_1^2v_2^2 \), a non-negative multiple of the convex \( t^4 \), so each such restriction is convex. But \( f \) is not convex. On the segment from \( (1, 0) \) to \( (0, 1) \), a line that misses the origin, \( f(1 - t, t) = t^2(1-t)^2 \) is \( 0 \) at both ends and \( \tfrac1{16} \) at the midpoint. So the value at the midpoint exceeds the average \( 0 \) of the end values.
:::

The Hessian test sees the same failure without guessing the segment. Here
\[
\H_f(x, y) = \begin{pmatrix} 2y^2 & 4xy \\ 4xy & 2x^2 \end{pmatrix}, \qquad \det\H_f(x, y) = -12x^2y^2 ,
\]
so at \( (1, 1) \) the determinant is \( -12 < 0 \). The two eigenvalues of this symmetric matrix have product \( -12 \), so one is negative, and \( \H_f(1, 1) \not\succeq 0 \). Part (a) confirms that \( f \) is not convex.

## Continuity

The warning about \( \lvert x \rvert \) shows that convexity does not buy differentiability. It does buy continuity on an open set, and in finite dimension the proof is short: a bound from above near a point is enough, and Jensen's inequality supplies one.

::: {#thm-convex-continuous}
[Convex Functions Are Continuous]

Let \( U \subseteq \nR^n \) be a non-empty open convex set and let \( f \colon U \to \nR \) be convex. Then \( f \) is continuous on \( U \). More precisely, for every \( \a \in U \) there are \( \delta > 0 \) and \( L \ge 0 \) with
\[
\lvert f(\a + \h) - f(\a)\rvert \le L\norm{\h} \qquad \text{whenever } \norm{\h} \le \delta .
\]
:::

::: {.idea}
① Bound \( f \) above on a small ball around \( \a \). The ball sits inside the "diamond" spanned by the \( 2n \) points \( \a \pm \rho\e_i \), and Jensen bounds \( f \) on the diamond by its largest value at those points. ② Turn an upper bound into a two-sided linear bound. Walk from \( \a \) toward \( \a + \h \) and on to the edge of the ball: convexity makes the rise over the short step at most a fraction of the rise over the whole way. Then walk the other way for the lower bound.
:::

::: {.proof}
Fix \( \a \in U \). Since \( U \) is open, @prp-closed-open-basics (a) gives \( r > 0 \) such that every point within distance \( r \) of \( \a \) lies in \( U \). Put \( \rho = r/2 \). The \( 2n + 1 \) points \( \a \) and \( \a \pm \rho\e_i \) lie in \( U \), so let \( M \) be the largest value of \( f \) at them.

**Step 1: an upper bound.** Let \( \h = \sum_i h_i\e_i \) with \( \norm{\h}_1 \le \rho \), and let \( \sigma_i = 1 \) if \( h_i \ge 0 \) and \( \sigma_i = -1 \) otherwise, so that \( \lvert h_i\rvert\sigma_i = h_i \). Then
\[
\a + \h = \sum_{i=1}^{n}\frac{\lvert h_i\rvert}{\rho}\,(\a + \rho\sigma_i\e_i) + \Bigl(1 - \frac{\norm{\h}_1}{\rho}\Bigr)\a ,
\]
a convex combination: the weights are non-negative and add up to \( 1 \). By @thm-jensen, \( f(\a + \h) \le M \). Put \( \delta = \rho/\sqrt n \). If \( \norm{\h} \le \delta \), then \( \norm{\h}_1 \le \sqrt n\norm{\h} \le \rho \) by @prp-p-norm-inequalities, so \( f(\a + \h) \le M \).

**Step 2: the linear bound.** Put \( L = (M - f(\a))/\delta \), which is \( \ge 0 \) because \( \a \) is one of the points defining \( M \). Let \( 0 < \norm{\h} \le \delta \); for \( \h = \0 \) there is nothing to prove. Put \( s = \norm{\h}/\delta \in (0, 1] \) and \( \u = \h/s \), so that \( \norm{\u} = \delta \) and \( s\u = \h \). First,
\[
\a + \h = (1 - s)\a + s(\a + \u) ,
\]
so convexity gives \( f(\a + \h) \le (1-s)f(\a) + sf(\a + \u) \), that is,
\[
f(\a + \h) - f(\a) \le s\bigl(f(\a + \u) - f(\a)\bigr) \le s\bigl(M - f(\a)\bigr) ,
\]
using Step 1 at \( \u \). Second,
\[
\a = \frac{1}{1+s}(\a + \h) + \frac{s}{1+s}(\a - \u) ,
\]
as one checks by multiplying out and using \( s\u = \h \). Here \( \a - \u \) lies in \( U \), and convexity gives \( (1+s)f(\a) \le f(\a + \h) + sf(\a - \u) \), that is,
\[
f(\a) - f(\a + \h) \le s\bigl(f(\a - \u) - f(\a)\bigr) \le s\bigl(M - f(\a)\bigr) ,
\]
using Step 1 at \( -\u \). Together, \( \lvert f(\a + \h) - f(\a)\rvert \le s(M - f(\a)) = L\norm{\h} \).

**Step 3: continuity.** If \( \x_k \to \a \), then \( \norm{\x_k - \a} \le \delta \) for all large \( k \), and for those \( k \) Step 2 gives \( \lvert f(\x_k) - f(\a)\rvert \le L\norm{\x_k - \a} \to 0 \). So \( f \) is continuous at \( \a \), in the sequential sense of Chapter 16's introduction. As \( \a \) was arbitrary, this proves the theorem.
:::

By @thm-norm-equivalence the choice of the Euclidean norm is immaterial: every norm on \( \nR^n \) gives the same continuous functions. Both hypotheses of the theorem are needed.

::: {.warning}
**The domain must be open.** On the closed interval \( [0, 1] \), let \( f = 0 \) on \( [0, 1) \) and \( f(1) = 1 \). It is convex: the right side \( tf(x) + (1-t)f(y) \) is never negative, and the left side is \( 0 \) unless \( tx + (1-t)y = 1 \), which for \( 0 < t < 1 \) forces \( x = y = 1 \), where both sides equal \( 1 \). But \( f(1 - 1/k) = 0 \not\to 1 = f(1) \). A convex function can jump at a boundary point of its domain.
:::

::: {.remark}
**Finite dimension is needed too.** On the polynomials in \( C[0,1] \), with the sup norm \( \norm{p}_\infty = \max_{t\in[0,1]}\lvert p(t)\rvert \) of Chapter 16 §01 restricted to them, the functional \( \varphi(p) = p'(1) \) is linear, hence convex, on the whole space. The polynomials \( p_k = x^{k^2}/k \) have \( \norm{p_k}_\infty = 1/k \to 0 \) and \( \varphi(p_k) = k \to \infty \), so \( \varphi \) is not continuous at \( 0 \). Step 1 is what fails: there is no finite set of points whose convex hull contains a ball.
:::

The basic theory is now in place. A convex function is one with a convex epigraph; Jensen's inequality extends its defining inequality to every finite average; every supremum of affine functions is one, which accounts for the Ky Fan sums; the Hessian tests for it; and on an open set it is continuous. What it has not yet done is prove an inequality the book did not already know. §11 does that: with a logarithm constructed from the exponential, Jensen's inequality for \( -\log \) gives the weighted arithmetic–geometric mean inequality, and from it come Young's and Hölder's inequalities, the triangle inequality for every \( p \)-norm, and the dual norms that §04 left open.

## Exercises

### A. Check your understanding

:::: {#exr-convex-functions-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define "\( f \) is convex on \( C \)", and explain why \( C \) is required to be convex.
2. Decide whether the following is correct, and justify your answer: if \( f \) and \( g \) are convex on \( C \), then so are \( f + g \) and \( \max(f, g) \).
3. Decide whether the following is correct, and justify your answer: if \( f \) and \( g \) are convex on \( \nR \), then so is their product \( fg \).
4. Decide whether the following is correct, and justify your answer: a convex function on \( \nR \) is differentiable.
5. Decide whether the following is correct, and justify your answer: if \( f \colon \nR^2 \to \nR \) is convex along every line through the origin, then \( f \) is convex.
6. Name the facts of analysis that the proof of @thm-convex-second-derivative uses.
:::
::::

::: {.solution}
(a) Let \( C \) be a non-empty convex subset of a real vector space. Then \( f \colon C \to \nR \) is convex if \( f(t\x + (1-t)\y) \le tf(\x) + (1-t)f(\y) \) for all \( \x, \y \in C \) and all \( t \in [0, 1] \) (@def-convex-function). The left side evaluates \( f \) at \( t\x + (1-t)\y \), and this point is in the domain for every choice exactly when \( C \) is convex.

(b) Correct. Adding the inequalities for \( f \) and for \( g \) gives the inequality for \( f + g \). For the maximum, the remark after @prp-sup-of-affine-convex applies: its proof works for any family of convex functions, and here the family is \( \{f, g\} \).

(c) Incorrect. \( f(x) = x \) is affine and \( g(x) = x^2 \) is convex (@exm-first-convex-functions), but \( fg = x^3 \) is not convex on \( \nR \): at \( -2 \), \( 0 \) and their midpoint \( -1 \) the non-example after @exm-first-convex-functions gives \( -1 > -4 \).

(d) Incorrect. \( \lvert x \rvert \) is convex and not differentiable at \( 0 \), as the first warning of the section shows.

(e) Incorrect. \( f(x, y) = x^2y^2 \) is convex along every line through the origin but not convex, since \( f(\tfrac12, \tfrac12) = \tfrac1{16} > 0 = \tfrac12 f(1, 0) + \tfrac12 f(0, 1) \).

(f) Chapter 14 §06's assumptions (A1), the symmetry of the Hessian, and (A2), Taylor's theorem with a second-order remainder; facts (A3) and (A4) of Chapter 16's introduction, compactness of \( [0, 1] \) and the extreme value theorem, in the maximum principle; and the algebra of limits, in the form "a non-strict inequality survives a limit".
:::

### B. Practice

:::: {#exr-convex-functions-b1}
[B1: Which are convex?]

Determine which of the following functions are convex on the given domain. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( f(x, y) = 2x^2 - 2xy + y^2 \) on \( \nR^2 \).
2. \( f(x, y) = x^2 + 4xy + y^2 \) on \( \nR^2 \).
3. \( f(x) = \max(2x + 1,\ -x,\ 3) \) on \( \nR \).
4. \( g(x) = 1/x \) on \( (0, \infty) \).
5. \( g(x) = 1/x \) on \( \{x \in \nR : x \ne 0\} \).
:::
::::

::: {.solution}
(a) Convex, indeed strictly convex. \( f \) is a polynomial, so twice continuously differentiable, with constant Hessian \( \H = \begin{psmallmatrix} 4 & -2 \\ -2 & 2 \end{psmallmatrix} \), which is symmetric. For \( \v = (v_1, v_2) \),
\[
\v\tp\H\v = 4v_1^2 - 4v_1v_2 + 2v_2^2 = 2\bigl(v_1^2 + (v_1 - v_2)^2\bigr) ,
\]
which is positive unless \( v_1 = 0 \) and \( v_1 = v_2 \), that is, unless \( \v = \0 \). So \( \H \succ 0 \) at every point, and @thm-convex-second-derivative (b) applies.

(b) Not convex. Take \( \x = (1, -1) \) and \( \y = (-1, 1) \), with midpoint \( \0 \). Then \( f(\x) = 1 - 4 + 1 = -2 = f(\y) \), while \( f(\0) = 0 > \tfrac12(-2) + \tfrac12(-2) = -2 \). The inequality of @def-convex-function fails with \( t = \tfrac12 \).

(c) Convex. The three functions \( 2x + 1 \), \( -x \) and the constant \( 3 \) are affine, and \( f \) is their maximum, so @prp-sup-of-affine-convex applies.

(d) Strictly convex. For \( x > 0 \) and small \( h \ne 0 \),
\[
\frac{1}{h}\Bigl(\frac{1}{x+h} - \frac1x\Bigr) = -\frac{1}{x(x+h)} \ \longrightarrow\ -\frac{1}{x^2} ,
\]
so \( g'(x) = -1/x^2 \). If \( 0 < a < b \) then \( 1/a^2 > 1/b^2 \), so \( -1/a^2 < -1/b^2 \): \( g' \) is strictly increasing on \( (0, \infty) \), and @lem-convex-one-variable gives strict convexity.

(e) The question has no answer: @def-convex-function requires a convex domain, and this one is not. It contains \( -1 \) and \( 1 \) but not their midpoint \( 0 \), so the defining inequality is undefined for \( x = -1 \), \( y = 1 \), \( t = \tfrac12 \).
:::

### C. Going deeper

:::: {#exr-convex-functions-c1}
[C1: Subadditive and homogeneous]

Let \( g \colon V \to \nR \) be **positively homogeneous**: \( g(t\x) = tg(\x) \) for every \( \x \in V \) and every real \( t \ge 0 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( g \) is convex if and only if \( g(\x + \y) \le g(\x) + g(\y) \) for all \( \x, \y \in V \).
2. Deduce that every norm on \( \nR^n \) is convex, and that @cor-ky-fan-subadditive and @cor-eigenvalue-sums-convex are equivalent statements about \( s_k \).
:::
::::

::: {.solution}
(a) \( (\Rightarrow) \) Let \( g \) be convex. By homogeneity with \( t = 2 \) and then convexity with \( t = \tfrac12 \),
\[
g(\x + \y) = 2g\bigl(\tfrac12\x + \tfrac12\y\bigr) \le 2\bigl(\tfrac12g(\x) + \tfrac12g(\y)\bigr) = g(\x) + g(\y) .
\]
\( (\Leftarrow) \) Let \( g \) be subadditive, and let \( 0 \le t \le 1 \). By subadditivity and then homogeneity with the non-negative numbers \( t \) and \( 1 - t \),
\[
g\bigl(t\x + (1-t)\y\bigr) \le g(t\x) + g\bigl((1-t)\y\bigr) = tg(\x) + (1-t)g(\y) .
\]

(b) A norm is positively homogeneous by (N2) of @def-norm, since \( \lvert t \rvert = t \) for \( t \ge 0 \), and subadditive by (N3); so it is convex by (a). This is a second proof of @exm-first-convex-functions (b). The function \( s_k \) is positively homogeneous on the Hermitian matrices, since multiplying by \( t \ge 0 \) multiplies each eigenvalue by \( t \) and keeps their order. So by (a), subadditivity of \( s_k \), which is @cor-ky-fan-subadditive, holds exactly when \( s_k \) is convex, which is @cor-eigenvalue-sums-convex.
:::

:::: {#exr-convex-functions-c2}
[C2: Tangent lines]

Let \( I \subseteq \nR \) be an open interval and let \( g \colon I \to \nR \) be differentiable and convex.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( g(y) \ge g(x) + g'(x)(y - x) \) for all \( x, y \in I \).
2. Deduce that \( g(y) = \max_{x \in I}\bigl(g(x) + g'(x)(y - x)\bigr) \) for every \( y \in I \): a differentiable convex function is the maximum of its tangent lines.
:::

*Hint: in (a), apply the definition to the points \( x \) and \( y \) with weight \( s \) on \( y \), and let \( s \to 0 \).*
::::

::: {.solution}
(a) If \( y = x \) both sides are equal. Let \( y \ne x \) and \( 0 < s \le 1 \). Convexity with weight \( s \) on \( y \) gives \( g(x + s(y - x)) \le (1 - s)g(x) + sg(y) \), that is,
\[
(y - x)\cdot\frac{g\bigl(x + s(y - x)\bigr) - g(x)}{s(y - x)} \ \le\ g(y) - g(x) .
\]
The fraction is a difference quotient of \( g \) at \( x \) with step \( s(y - x) \ne 0 \). Take \( s = 1/k \); the step tends to \( 0 \), so the fraction tends to \( g'(x) \). A non-strict inequality survives the limit, so \( (y - x)g'(x) \le g(y) - g(x) \), as claimed.

(b) For fixed \( y \), each \( \ell_x(y) = g(x) + g'(x)(y - x) \) is at most \( g(y) \) by (a), and \( \ell_y(y) = g(y) \). So the maximum over \( x \) exists, is attained at \( x = y \), and equals \( g(y) \). Each \( \ell_x \) is an affine function of \( y \), so this is the converse of @prp-sup-of-affine-convex, for differentiable functions.
:::

:::: {#exr-convex-functions-c3}
[C3: Where a convex function is largest]

::: {.enumerate options="label=(\alph*)"}
1. Let \( f \colon \nR^n \to \nR \) be convex, and let \( P \) be the convex hull \( \conv\{\x_1, \dots, \x_m\} \). Prove that \( \max_{\x \in P}f(\x) = \max_i f(\x_i) \).
2. Let \( f(x, y) = x^2 - xy + y^2 \) and let \( P \) be the triangle \( \conv\{(2, 0), (0, 2), (-2, -2)\} \). Find the maximum and the minimum of \( f \) on \( P \), and say where each is attained.
:::
::::

::: {.solution}
(a) Each \( \x_i \) lies in \( P \), so the maximum over \( P \), if it exists, is at least \( \max_if(\x_i) \). Conversely, let \( \x \in P \). By @thm-convex-hull-combinations, \( \x = \sum_iw_i\x_i \) for some weights \( w_i \ge 0 \) with sum \( 1 \), and @thm-jensen gives \( f(\x) \le \sum_iw_if(\x_i) \le \max_if(\x_i) \). So \( \max_if(\x_i) \) is an upper bound for \( f \) on \( P \) that is attained, hence the maximum. Compare @cor-linear-max-at-extreme, which says the same for a linear function on any compact convex set, with extreme points in place of the \( \x_i \).

(b) The Hessian is the constant symmetric matrix \( \begin{psmallmatrix} 2 & -1 \\ -1 & 2 \end{psmallmatrix} \), and \( 2v_1^2 - 2v_1v_2 + 2v_2^2 = v_1^2 + v_2^2 + (v_1 - v_2)^2 \ge 0 \), so it is positive semidefinite and \( f \) is convex by @thm-convex-second-derivative (a). By (a) the maximum is the largest vertex value: \( f(2, 0) = 4 \), \( f(0, 2) = 4 \) and \( f(-2, -2) = 4 - 4 + 4 = 4 \). So the maximum is \( 4 \), attained at all three vertices. For the minimum, \( f(x, y) = \tfrac12\bigl(x^2 + y^2 + (x - y)^2\bigr) \ge 0 \), with equality only at \( (0, 0) \). And \( (0, 0) = \tfrac13(2, 0) + \tfrac13(0, 2) + \tfrac13(-2, -2) \) lies in \( P \). So the minimum is \( 0 \), attained only at the interior point \( (0, 0) \). The maximum of a convex function sits at vertices; its minimum need not.
:::
