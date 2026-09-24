# All Norms Agree

§01 left a worry. There are many norms on \( F^n \), they give different answers, and every statement of the form "this quantity is small" now has to say small in which norm. This section removes the worry in finite dimension, in the strongest way available: any two norms on a finite-dimensional space are trapped between fixed multiples of each other, so they agree about every limit, every bounded set and every continuous function. It also says what the theorem costs — constants that grow with the dimension — and where it stops being true.

## Trapped between multiples

Look again at @prp-p-norm-inequalities. Its four inequalities say that on \( F^n \),
\[
\tfrac{1}{\sqrt n}\,\norm{\x}_1 \ \le\ \norm{\x}_2 \ \le\ \norm{\x}_1 ,
\]
so \( \norm{\cdot}_2 \) never differs from \( \norm{\cdot}_1 \) by a factor worse than \( \sqrt n \), in either direction. Whatever \( \norm{\cdot}_1 \) calls small, \( \norm{\cdot}_2 \) calls small too, at the cost of a fixed factor. That is a relation worth naming.

*Two norms are equivalent when each is sandwiched between two fixed multiples of the other, so that neither can be small while the other is large.*

::: {#def-equivalent-norms}
[Equivalent Norms]

Let \( V \) be a vector space over \( F = \nR \) or \( \nC \), and let \( \norm{\cdot}_a \) and \( \norm{\cdot}_b \) be norms on \( V \). They are **equivalent** if there exist real constants \( c, C > 0 \), **not depending on the vector**, such that
\[
c\,\norm{\v}_b \ \le\ \norm{\v}_a \ \le\ C\,\norm{\v}_b
\qquad \text{for every } \v \in V .
\]
:::

In words. The two inequalities are read separately: the right one says \( \norm{\cdot}_a \) is *no larger than* a fixed multiple of \( \norm{\cdot}_b \), and the left one says it is *no smaller than* a fixed positive multiple. The phrase **not depending on the vector** is the whole content, since for each individual \( \v \ne \0 \) the ratio \( \norm{\v}_a/\norm{\v}_b \) is some positive number and one could always take that number as the constant. What is being asked is that one pair of constants works for all \( \v \) at once. Note also that the definition says nothing about the two norms being close; \( c \) may be \( 10^{-6} \).

::: {#exm-norm-equivalence-constants}
[The three \( p \)-norms, with best constants]

On \( F^n \), @prp-p-norm-inequalities gives
\[
\begin{aligned}
\norm{\x}_\infty &\le \norm{\x}_2 \le \sqrt n\,\norm{\x}_\infty ,\\
\norm{\x}_\infty &\le \norm{\x}_1 \le n\,\norm{\x}_\infty ,\\
\tfrac{1}{\sqrt n}\norm{\x}_1 &\le \norm{\x}_2 \le \norm{\x}_1 ,
\end{aligned}
\]
so the three are pairwise equivalent. The middle line's upper constant comes from \( \norm{\x}_1 \le \sqrt n\norm{\x}_2 \le \sqrt n\cdot\sqrt n\,\norm{\x}_\infty \). Every constant shown is attained, so none of them can be improved. On the first two lines the lower constant is attained at \( \e_1 \) and the upper one at \( \1 \). **The third line runs the other way**: at \( \1 \) the lower inequality reads \( \tfrac{1}{\sqrt n}\cdot n = \sqrt n \le \sqrt n \), and at \( \e_1 \) the upper one reads \( 1 \le 1 \).
:::

Before the theorem, one small fact makes the proof strategy possible: it is enough to compare every norm with a single one of our choosing.

::: {#prp-equivalence-of-norms-relation}
[Equivalence of Norms Is an Equivalence Relation]

On a fixed vector space \( V \) over \( F \), the relation of @def-equivalent-norms is reflexive, symmetric and transitive.
:::

::: {.proof}
Reflexive: take \( c = C = 1 \). Symmetric: if \( c\norm{\v}_b \le \norm{\v}_a \le C\norm{\v}_b \) for all \( \v \), then dividing through by the positive constants gives \( C^{-1}\norm{\v}_a \le \norm{\v}_b \le c^{-1}\norm{\v}_a \). Transitive: if in addition \( c'\norm{\v}_d \le \norm{\v}_b \le C'\norm{\v}_d \), then multiplying the first chain's outer inequalities by the positive constants \( c \) and \( C \) gives
\[
cc'\norm{\v}_d \le c\norm{\v}_b \le \norm{\v}_a
\le C\norm{\v}_b \le CC'\norm{\v}_d ,
\]
and \( cc', CC' > 0 \). This proves all three properties.
:::

So to prove that *any two* norms on \( V \) are equivalent, it suffices to prove that *every* norm is equivalent to one fixed reference norm. We take the reference to be the Euclidean norm of a chosen basis, because that is where compactness lives.

## Compactness enters the book

::: {#thm-norm-equivalence}
[Equivalence of Norms in Finite Dimension]

Let \( V \) be a vector space over \( F = \nR \) or \( \nC \) with \( \dim V = n < \infty \). Then **any two** norms on \( V \) are equivalent. Explicitly, if \( \sB = (\v_1, \dots, \v_n) \) is a basis of \( V \), if \( \norm{\cdot}_2 \) denotes the Euclidean norm of the coordinate vector,
\[
\Bigl\lVert \sum_i x_i\v_i \Bigr\rVert_2
\coloneqq \bigl(\lvert x_1\rvert^2 + \dots + \lvert x_n\rvert^2\bigr)^{1/2} ,
\]
and if \( N \) is any norm on \( V \), then there are constants \( 0 < m \le M \) with
\[
m\,\norm{\v}_2 \ \le\ N(\v) \ \le\ M\,\norm{\v}_2
\qquad \text{for every } \v \in V .
\]
:::

::: {.idea}
The two inequalities are not symmetric, and it is worth seeing why before starting. The **upper** bound is cheap: write \( \v \) in the basis, apply the triangle inequality once, and the constant \( M \) is built out of the numbers \( N(\v_i) \). The **lower** bound cannot be obtained the same way; there is no inequality running from \( N(\sum x_i\v_i) \) down to the individual coordinates, and the temptation to assume that the two norms are comparable on the basis and then "extend by linearity" is exactly the error the theorem exists to forbid — @exm-two-norms-agree-on-a-basis below shows two norms agreeing on a basis and differing by a factor of \( n \) elsewhere.

The route is therefore ① upper bound by the triangle inequality; ② use that upper bound to show \( N \) is continuous as a function of the coordinates; ③ restrict \( N \) to the Euclidean unit sphere, which is compact, so \( N \) attains a minimum \( m \) there; ④ the minimum is positive because \( N \) vanishes only at \( \0 \), which is not on the sphere; ⑤ scale back. Compactness is what turns the infimum over infinitely many unit vectors into a value attained at a particular unit vector, and a value attained at a vector can be tested for positivity one vector at a time.
:::

::: {.proof}
By @prp-equivalence-of-norms-relation it suffices to prove the displayed two-sided bound, since then any two norms \( N_1, N_2 \) are each equivalent to \( \norm{\cdot}_2 \) and hence to each other. If \( n = 0 \) then \( V = \{\0\} \), both norms are the zero function and \( m = M = 1 \) works; assume \( n \ge 1 \). The coordinate map \( \Phi \colon F^n \to V \), \( \x \mapsto \sum_i x_i\v_i \), is an isomorphism (@cor-coordinate-isomorphism), and by construction \( \norm{\Phi(\x)}_2 = \norm{\x}_2 \) is the Euclidean norm of @exm-p-norms. It is enough to prove the two bounds for \( \x \in F^n \) with \( N \) replaced by \( f(\x) \coloneqq N(\Phi(\x)) \).

**Step 1. The upper bound.** Let \( M = \bigl(\sum_{i=1}^{n} N(\v_i)^2\bigr)^{1/2} \). For \( \x \in F^n \), the triangle inequality (N3) applied \( n - 1 \) times and then (N2) give
\[
f(\x) = N\Bigl(\sum_i x_i\v_i\Bigr)
\le \sum_i \lvert x_i\rvert\,N(\v_i) ,
\]
and @thm-cauchy-schwarz in \( \nR^n \), applied to the vectors \( (\lvert x_1\rvert, \dots, \lvert x_n\rvert) \) and \( (N(\v_1), \dots, N(\v_n)) \), bounds the right-hand side by \( M\norm{\x}_2 \). Hence \( f(\x) \le M\norm{\x}_2 \) for every \( \x \). Also \( M > 0 \), since \( N(\v_1) > 0 \) by (N1) and \( \v_1 \ne \0 \).

**Step 2. \( f \) is continuous on \( F^n \) for the Euclidean norm.** By @lem-reverse-triangle-norm applied to \( N \), and then Step 1 applied to \( \x - \y \),
\[
\lvert f(\x) - f(\y)\rvert \le N\bigl(\Phi(\x - \y)\bigr)
\le M\,\norm{\x - \y}_2 .
\]
So \( f \) changes by at most \( M \) times the distance moved: it is continuous, and the continuity was **deduced** from Step 1 rather than assumed.

**Step 3. The minimum on the unit sphere.** Let
\[
S = \{\x \in F^n : \norm{\x}_2 = 1\} ,
\]
which is non-empty because \( n \ge 1 \) (it contains \( \e_1 \)). It is bounded, and it is closed: if \( \norm{\x_k - \x}_2 \to 0 \) with every \( \norm{\x_k}_2 = 1 \), then @lem-reverse-triangle-norm gives \( \bigl\lvert \norm{\x}_2 - 1\bigr\rvert \le \norm{\x - \x_k}_2 \to 0 \), so \( \norm{\x}_2 = 1 \) and \( \x \in S \). By **the compactness of closed bounded sets in \( F^n \), fact (A3) of the chapter introduction**, \( S \) is compact; by **the extreme value theorem, fact (A4)**, the continuous function \( f \) of Step 2 attains a minimum value on \( S \). Say \( m = f(\x_0) \) with \( \x_0 \in S \).

**Step 4. The minimum is positive.** Since \( \x_0 \in S \) we have \( \norm{\x_0}_2 = 1 \ne 0 \), so \( \x_0 \ne \0 \) and hence \( \Phi(\x_0) \ne \0 \), \( \Phi \) being injective. By (N1) for \( N \), \( m = N(\Phi(\x_0)) > 0 \). This is the step that needs a minimum rather than an infimum: an infimum of positive numbers can be \( 0 \), while a minimum is the value at an actual vector, and there (N1) can be applied.

**Step 5. Scaling back.** Let \( \x \ne \0 \). Then \( \x/\norm{\x}_2 \in S \), so \( f(\x/\norm{\x}_2) \ge m \), and (N2) for \( N \) gives \( f(\x) \ge m\norm{\x}_2 \). For \( \x = \0 \) both sides are \( 0 \). Combining with Step 1,
\[
m\,\norm{\x}_2 \ \le\ f(\x) \ \le\ M\,\norm{\x}_2
\qquad (\x \in F^n),
\]
and transporting along \( \Phi \) gives the statement for \( V \). Since \( m \le f(\x_0) \le M\norm{\x_0}_2 = M \), the constants satisfy \( 0 < m \le M \). This proves the theorem.
:::

The proof used the finite dimension twice, and it is worth saying where: once in Step 1, where the triangle inequality was applied finitely many times to a finite basis expansion, and once in Step 3, where \( F^n \) is the space in which closed bounded sets are compact. Remove either and the argument collapses, as the last part of this section shows.

::: {#exm-two-norms-agree-on-a-basis}
[Agreeing on a basis is not enough]

On \( F^n \), the norms \( \norm{\cdot}_1 \) and \( \norm{\cdot}_\infty \) both give every standard basis vector the value \( 1 \). Yet \( \norm{\1}_1 = n \) and \( \norm{\1}_\infty = 1 \). So the data "\( N_1(\v_i) = N_2(\v_i) \) for every basis vector" implies no inequality between \( N_1 \) and \( N_2 \) beyond what @thm-norm-equivalence gives for any pair at all.
:::

::: {.check}
In Step 1 the constant was \( M = \bigl(\sum_i N(\v_i)^2\bigr)^{1/2} \). Where would the proof break if we tried the symmetric guess \( m = \min_i N(\v_i) \) for the lower bound?
:::

::: {.solution}
It breaks immediately, and @exm-two-norms-agree-on-a-basis is the witness. Take \( V = F^2 \) with the basis \( (\e_1, \e_2) \), \( N = \norm{\cdot}_\infty \) and \( \norm{\cdot}_2 \) the Euclidean norm. Then \( \min_i N(\e_i) = 1 \), and the guessed inequality \( \norm{\x}_\infty \ge \norm{\x}_2 \) fails at \( \x = \1 \), where the two sides are \( 1 \) and \( \sqrt 2 \). The reason is that the triangle inequality only ever bounds \( N(\sum x_i\v_i) \) from **above**; there is no lower bound in the axioms, because a sum of long vectors can be short. Getting a lower bound needs a genuinely different mechanism, and compactness is that mechanism.
:::

## What the theorem buys

The point of the theorem is that whole sentences may now drop the words "in which norm".

::: {#cor-convergence-norm-independent}
[Convergence and Boundedness Do Not Depend on the Norm]

Let \( V \) be finite-dimensional over \( \nR \) or \( \nC \), let \( \norm{\cdot}_a \) and \( \norm{\cdot}_b \) be norms on \( V \), and let \( (\u_k) \) be a sequence in \( V \) with \( \u \in V \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \norm{\u_k - \u}_a \to 0 \) if and only if \( \norm{\u_k - \u}_b \to 0 \);
2. \( (\u_k) \) is bounded for \( \norm{\cdot}_a \) if and only if it is bounded for \( \norm{\cdot}_b \);
3. \( (\u_k) \) is Cauchy for \( \norm{\cdot}_a \) if and only if it is Cauchy for \( \norm{\cdot}_b \).
:::
:::

::: {.proof}
By @thm-norm-equivalence there are \( c, C > 0 \) with \( c\norm{\v}_b \le \norm{\v}_a \le C\norm{\v}_b \) for every \( \v \in V \). For (a), apply this to \( \v = \u_k - \u \): if \( \norm{\u_k - \u}_b \to 0 \) then \( 0 \le \norm{\u_k - \u}_a \le C\norm{\u_k - \u}_b \to 0 \), and conversely \( \norm{\u_k - \u}_b \le c^{-1}\norm{\u_k - \u}_a \to 0 \). For (b), a bound \( \norm{\u_k}_b \le K \) for all \( k \) gives \( \norm{\u_k}_a \le CK \), and conversely with \( c^{-1} \). For (c), apply the same two estimates to \( \v = \u_k - \u_l \). This proves all three.
:::

Now the connection this chapter was built for. Chapter 10 §10 defined convergence of matrices **entrywise** (@def-entrywise-convergence) and said, in its opening paragraph, that no notion of the size of a matrix was used and that Chapter 16 would supply one. Here is the reconciliation.

::: {#cor-entrywise-convergence-is-the-convergence}
[Entrywise Convergence Is Convergence in Every Norm]

Let \( \M_1, \M_2, \dots \) and \( \M \) lie in \( M_{p\times q}(\nC) \), and let \( \norm{\cdot} \) be **any** norm on \( M_{p\times q}(\nC) \). Then \( \M_k \to \M \) entrywise in the sense of @def-entrywise-convergence if and only if \( \norm{\M_k - \M} \to 0 \). Likewise \( (\M_k) \) is bounded in the sense of @def-entrywise-convergence if and only if \( \bigl(\norm{\M_k}\bigr) \) is a bounded sequence of real numbers.
:::

::: {.idea}
Entrywise convergence is convergence in one particular norm, the entrywise maximum. @thm-norm-equivalence says every other norm is trapped between two multiples of it, and a quantity squeezed between two multiples of something tending to \( 0 \) tends to \( 0 \) as well. Both directions are that one sentence.
:::

::: {.proof}
The space \( M_{p\times q}(\nC) \) is a complex vector space of dimension \( pq \), and
\[
N_\infty(\M) = \max_{r,s}\lvert m_{rs}\rvert
\]
is a norm on it: it is the \( \infty \)-norm of @exm-p-norms read on the list of entries, through the coordinate isomorphism of @cor-coordinate-isomorphism that sends a matrix to its \( pq \) entries. By @def-entrywise-convergence (a), \( \M_k \to \M \) entrywise means \( (\M_k)_{rs} \to \M_{rs} \) for each of the finitely many positions \( (r,s) \), and since a maximum of finitely many non-negative sequences tends to \( 0 \) exactly when each of them does, this says precisely \( N_\infty(\M_k - \M) \to 0 \). By @thm-norm-equivalence the norms \( N_\infty \) and \( \norm{\cdot} \) are equivalent, so @cor-convergence-norm-independent (a) converts this into \( \norm{\M_k - \M} \to 0 \). The statement about boundedness is @def-entrywise-convergence (b) together with @cor-convergence-norm-independent (b), read the same way.
:::

::: {#exm-frobenius-distance-to-a-limit}
[Watching one sequence converge]

In \( M_2(\nR) \) let
\[
\M_k = \begin{pmatrix} \tfrac1k & 2 \\[2pt] 0 & 1 - \tfrac1k \end{pmatrix} ,
\qquad k \ge 1 .
\]
Entry by entry, \( \tfrac1k \to 0 \), \( 2 \to 2 \), \( 0 \to 0 \) and \( 1 - \tfrac1k \to 1 \), so \( \M_k \to \M = \begin{psmallmatrix} 0 & 2 \\ 0 & 1\end{psmallmatrix} \) in the sense of @def-entrywise-convergence. The corollary says this is convergence in *every* norm, and here one can see it directly: \( \M_k - \M = \diag(\tfrac1k, -\tfrac1k) \), so
\[
\norm{\M_k - \M}_F = \sqrt{\tfrac{1}{k^2} + \tfrac{1}{k^2}} = \frac{\sqrt2}{k} \longrightarrow 0 ,
\]
and \( \norm{\M_k - \M}_\infty \), the largest absolute row sum, is \( \tfrac1k \). Different norms, different constants, the same verdict — which is the content of the corollary.
:::

So Chapter 10 §10 lost nothing by working entrywise. Its @thm-matrix-powers-converge-to-zero, @thm-matrix-powers-bounded, @thm-matrix-powers-converge and @thm-neumann-series-spectral are statements about *the* convergence of matrices, and every norm this chapter introduces — the Frobenius norm, the operator norms of §03, anything at all — measures the same thing. What the norms add is not a new notion of limit but a **rate**: a single number \( \norm{\A^{k}} \) that can be bounded, compared and summed, where an entrywise statement gives \( pq \) separate sequences and no way to combine them.

One more corollary, which §03 will use to know that the operator norm exists at all.

::: {#cor-closed-bounded-compact}
[Closed and Bounded Is Compact, in Every Norm]

Let \( V \) be finite-dimensional over \( \nR \) or \( \nC \). Call a subset \( K \subseteq V \) **bounded** for a norm if \( K \subseteq \{\v : \norm{\v} \le R\} \) for some real \( R \), and **closed** for that norm if whenever \( \norm{\u_k - \u} \to 0 \) with every \( \u_k \in K \), also \( \u \in K \). Then a subset that is closed and bounded for one norm is closed and bounded for every norm, and is **compact**: every sequence in it has a subsequence converging to a point of it. In particular, when \( V \ne \{\0\} \), the unit sphere \( \{\v : \norm{\v} = 1\} \) of any norm is non-empty and compact, and a continuous real-valued function on it attains a maximum and a minimum.
:::

::: {.idea}
Both words in "closed and bounded" are defined by a norm, so the first thing to check is that changing the norm changes neither. That is @thm-norm-equivalence again. Once the words are norm-free, the statement is @thm-norm-equivalence's own compactness step read in a coordinate-free way: carry \( K \) to \( F^n \) by coordinates, apply (A3), and carry the limit back.
:::

::: {.proof}
Fix a basis and transport everything to \( F^n \) by the coordinate isomorphism (@cor-coordinate-isomorphism), as in the proof of @thm-norm-equivalence. Let \( \norm{\cdot}_a \) and \( \norm{\cdot}_b \) be norms, with \( c\norm{\cdot}_b \le \norm{\cdot}_a \le C\norm{\cdot}_b \) from @thm-norm-equivalence. A set bounded for one is bounded for the other by the same two estimates as in @cor-convergence-norm-independent (b). A set closed for one is closed for the other, because by @cor-convergence-norm-independent (a) the two norms have the same convergent sequences with the same limits, and the notion of closed defined in the statement asks exactly that limits of convergent sequences stay in the set.

For compactness, let \( K \subseteq F^n \) be closed and bounded for some norm; by the previous paragraph it is closed and bounded for \( \norm{\cdot}_2 \). By **the compactness of closed bounded sets in \( F^n \), fact (A3) of the chapter introduction**, every sequence in \( K \) has a subsequence converging in \( \norm{\cdot}_2 \) to a point of \( K \), and by @cor-convergence-norm-independent (a) that subsequence converges in every norm to the same point. The unit sphere of a norm \( N \) is bounded, and it is closed because \( \lvert N(\v) - N(\u_k)\rvert \le N(\v - \u_k) \) by @lem-reverse-triangle-norm, so a limit of vectors with \( N = 1 \) has \( N = 1 \); it is non-empty when \( V \ne \{\0\} \), since \( N(\v)^{-1}\v \) lies on it for any \( \v \ne \0 \). The last sentence is then **the extreme value theorem, fact (A4)**, applied to that non-empty compact set. This proves the corollary.
:::

## Two warnings, and where the theorem stops

The theorem is not permission to forget which norm is in use. Here is the first reason.

::: {.warning}
**The constants depend on the dimension, and grow.** @exm-norm-equivalence-constants gives \( \norm{\x}_1 \le n\norm{\x}_\infty \) on \( F^n \), and @exr-vector-norms-c1 shows the constant \( \sqrt n \) in \( \norm{\x}_1 \le \sqrt n\norm{\x}_2 \) is attained, hence best possible. So a statement such as "the error is at most \( 10^{-6} \) in the \( \infty \)-norm" translates into the \( 1 \)-norm as "at most \( n \cdot 10^{-6} \)", which is a different statement when \( n \) is a million. @thm-norm-equivalence says the two norms cannot disagree about **whether** something tends to zero; it says nothing about **how fast**, and every quantitative estimate in the rest of this chapter names its norm for that reason.
:::

The second reason is that the theorem is false without the finite dimension, and not by a narrow margin.

::: {#exm-norms-not-equivalent-infinite-dimension}
[Two inequivalent norms on a space of polynomials]

Let \( V = \nR[x] \), the real polynomials — equivalently, the sequences of real coefficients with only finitely many non-zero terms. For \( p = a_0 + a_1x + \dots + a_dx^d \) put
\[
\norm{p}_1 = \lvert a_0\rvert + \dots + \lvert a_d\rvert ,
\qquad
\norm{p}_\infty = \max_i \lvert a_i\rvert .
\]
Both are norms, by the same coordinatewise checks as in @exm-p-norms; the only difference is that the number of coordinates is unbounded. One inequality survives: \( \norm{p}_\infty \le \norm{p}_1 \) always. The other fails completely. Put
\[
p_k = 1 + x + x^2 + \dots + x^{k-1} .
\]
Then \( \norm{p_k}_1 = k \) while \( \norm{p_k}_\infty = 1 \), so a constant \( C \) with \( \norm{p}_1 \le C\norm{p}_\infty \) for all \( p \) would have to satisfy \( C \ge k \) for every \( k \). No such \( C \) exists, and the two norms are not equivalent.
:::

Look at what the sequence \( \bigl(\tfrac1k p_k\bigr) \) does: it tends to \( 0 \) in \( \norm{\cdot}_\infty \), since \( \norm{\tfrac1k p_k}_\infty = 1/k \), while \( \norm{\tfrac1k p_k}_1 = 1 \) for every \( k \). So the two norms disagree about which sequences converge — not about the rate, about the fact. Everything in @cor-convergence-norm-independent and @cor-closed-bounded-compact fails here at once, and it fails because Step 3 of the proof of @thm-norm-equivalence has nothing to stand on. The general reason is recorded, and not proved, in the warning below.

::: {.warning}
**Infinite dimension is outside the scope of this book.** The closed unit ball of a normed space is compact **only** when the space is finite-dimensional. That is a genuine theorem, due to Riesz, and it is **recorded here, not proved**: it lies outside the four imported facts of the chapter introduction, this book never uses it as a step in an argument, and it is stated only so that @exm-norms-not-equivalent-infinite-dimension is not mistaken for an accident of a badly chosen pair. Every result of this chapter carries the hypothesis \( \dim V < \infty \), and on \( C[0,1] \) or \( \nR[x] \) none of them is available. The study of norms on infinite-dimensional spaces is functional analysis, and there the choice of norm is the main content rather than an irrelevance.
:::

::: {.check}
On \( C[0,1] \), compare the sup norm \( \norm{f}_\infty \) of @exm-induced-and-weighted-norms (c) with \( \norm{f}_1 = \int_0^1\lvert f\rvert \), which is a norm because a continuous \( f \ge 0 \) with \( \int_0^1 f = 0 \) is the zero function — the one fact from analysis that Chapter 11 §01 recorded when it put an inner product on \( C[0,1] \), quoted again here. Which of the two inequalities of @def-equivalent-norms holds, and which fails?
:::

::: {.solution}
The inequality \( \norm{f}_1 \le \norm{f}_\infty \) holds, since \( \int_0^1\lvert f\rvert \le \int_0^1\norm{f}_\infty = \norm{f}_\infty \). The other fails. Take \( f_k(t) = \max(0, 1 - kt) \) for \( k \ge 1 \), the spike that drops from \( 1 \) to \( 0 \) on \( [0, 1/k] \). Then \( \norm{f_k}_\infty = f_k(0) = 1 \), while
\[
\norm{f_k}_1 = \int_0^{1/k}(1 - kt)\,\dd t = \frac{1}{2k} ,
\]
the area of a triangle of base \( 1/k \) and height \( 1 \), so no integration theory is needed to evaluate it.
A constant \( C \) with \( \norm{f}_\infty \le C\norm{f}_1 \) would need \( C \ge 2k \) for every \( k \). A tall thin spike has small integral and large maximum, and in infinite dimension nothing stops it from being arbitrarily thin.
:::

With the choice of norm made harmless in finite dimension, the next section can measure matrices without apologizing for which measurement it uses — and then, when the estimates start to matter, name the norm on purpose.

## Exercises

### A. Check your understanding

:::: {#exr-equivalence-of-norms-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State @def-equivalent-norms, and explain why the phrase "not depending on the vector" cannot be dropped.
2. State @thm-norm-equivalence, including its hypothesis on \( V \).
3. Which two of the four imported analysis facts does the proof of @thm-norm-equivalence use, and at which step is each used?
4. True or false: if two norms on \( \nR^n \) are equivalent, then some sequence converges in one and not the other. Justify your answer.
5. True or false: equivalent norms give the same value to every vector. Justify your answer.
:::
::::

::: {.solution}
(a) Two norms \( \norm{\cdot}_a, \norm{\cdot}_b \) on \( V \) are equivalent if there are constants \( c, C > 0 \), independent of the vector, with \( c\norm{\v}_b \le \norm{\v}_a \le C\norm{\v}_b \) for every \( \v \in V \) (@def-equivalent-norms). Without the phrase the condition is vacuous: for each \( \v \ne \0 \) the number \( \norm{\v}_a/\norm{\v}_b \) is positive and could be taken as both \( c \) and \( C \) at that one vector, so every pair of norms would qualify.

(b) On a finite-dimensional vector space over \( \nR \) or \( \nC \), any two norms are equivalent (@thm-norm-equivalence). Finite dimension is essential — see @exm-norms-not-equivalent-infinite-dimension.

(c) Fact (A3), the compactness of closed bounded sets in \( F^n \), at Step 3, to know the Euclidean unit sphere is compact; and fact (A4), the extreme value theorem, also at Step 3, to know that the continuous function \( f \) attains a minimum there rather than merely approaching an infimum.

(d) False, and this is the content of @cor-convergence-norm-independent (a): equivalent norms have exactly the same convergent sequences with exactly the same limits.

(e) False. \( \norm{\cdot}_1 \) and \( \norm{\cdot}_\infty \) on \( \nR^2 \) are equivalent by @exm-norm-equivalence-constants, yet \( \norm{\1}_1 = 2 \ne 1 = \norm{\1}_\infty \). Equivalence constrains ratios, not values.
:::

### B. Practice

:::: {#exr-equivalence-of-norms-b1}
[B1: Best constants for a weighted norm]

On \( \nR^2 \) let \( N(\x) = \bigl(x_1^2 + 4x_2^2\bigr)^{1/2} \). Find the **best** constants \( c, C > 0 \) with
\[
c\,\norm{\x}_\infty \le N(\x) \le C\,\norm{\x}_\infty
\qquad (\x \in \nR^2),
\]
and give a vector attaining each. Hence deduce that \( N \) and \( \norm{\cdot}_\infty \) are equivalent.
::::

::: {.solution}
Write \( a = \lvert x_1\rvert \), \( b = \lvert x_2\rvert \) and \( M = \max(a,b) = \norm{\x}_\infty \). Then \( N(\x)^2 = a^2 + 4b^2 \).

Upper: \( a^2 + 4b^2 \le M^2 + 4M^2 = 5M^2 \), so \( N(\x) \le \sqrt5\,\norm{\x}_\infty \). Equality needs \( a = b = M \), and \( \x = (1,1) \) gives \( N(\x) = \sqrt5 \) and \( \norm{\x}_\infty = 1 \). So \( C = \sqrt5 \) and it cannot be lowered.

Lower: if \( M = a \) then \( a^2 + 4b^2 \ge a^2 = M^2 \), and if \( M = b \) then \( a^2 + 4b^2 \ge 4b^2 \ge M^2 \). Either way \( N(\x) \ge \norm{\x}_\infty \), so \( c = 1 \) works, and \( \x = \e_1 \) gives \( N(\x) = \norm{\x}_\infty = 1 \), so it cannot be raised.

Since \( 1 \) and \( \sqrt5 \) are positive constants independent of \( \x \), the two norms are equivalent by @def-equivalent-norms.
:::

:::: {#exr-equivalence-of-norms-b2}
[B2: Reading a convergence off the entries]

In \( M_2(\nR) \) let
\[
\M_k = \begin{pmatrix} 1 + \frac{1}{k} & \frac{(-1)^k}{k^2} \\
\frac{1}{2^k} & 3 - \frac{5}{k} \end{pmatrix} .
\]
Determine \( \lim_k \M_k \) in the sense of @def-entrywise-convergence, and compute \( \norm{\M_k - \M}_F \) explicitly. Hence confirm @cor-entrywise-convergence-is-the-convergence for this sequence and the Frobenius norm.
::::

::: {.solution}
Each entry converges: \( 1 + 1/k \to 1 \), \( (-1)^k/k^2 \to 0 \), \( 2^{-k} \to 0 \), \( 3 - 5/k \to 3 \). So \( \M_k \to \M = \begin{pmatrix} 1 & 0 \\ 0 & 3\end{pmatrix} \) entrywise. Then
\[
\norm{\M_k - \M}_F
= \Bigl(\tfrac{1}{k^2} + \tfrac{1}{k^4} + \tfrac{1}{4^k} + \tfrac{25}{k^2}\Bigr)^{1/2} ,
\]
which is at most \( \bigl(28/k^2\bigr)^{1/2} = \sqrt{28}/k \) for \( k \ge 1 \), since \( 1/k^4 \le 1/k^2 \) and \( 4^{-k} \le 1/k^2 \) for \( k \ge 1 \). Hence \( \norm{\M_k - \M}_F \to 0 \), as @cor-entrywise-convergence-is-the-convergence predicts. Note what the norm added: a single sequence \( \sqrt{28}/k \) bounding the whole matrix, where the entrywise statement gave four unrelated sequences.
:::

:::: {#exr-equivalence-of-norms-b3}
[B3: An equivalence with the constants written down]

Let \( V = \nR[x]_{\le 2} \) with basis \( \sB = (1, x, x^2) \). For \( p \in V \) let \( \norm{p}_{\sB} \) be the Euclidean norm of the coefficient vector, and let \( N(p) = \lvert p(0)\rvert + \lvert p(1)\rvert + \lvert p(-1)\rvert \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( N \) is a norm on \( V \).
2. Find an explicit \( M \) with \( N(p) \le M\norm{p}_{\sB} \), following Step 1 of the proof of @thm-norm-equivalence.
3. Explain, without computing it, why a constant \( m > 0 \) with \( N(p) \ge m\norm{p}_{\sB} \) exists.
:::
::::

::: {.solution}
(a) (N2) and (N3) are inherited pointwise from \( \lvert\cdot\rvert \) on \( \nR \), exactly as for \( \norm{\cdot}_1 \) in @exm-p-norms. For (N1): \( N(p) = 0 \) forces \( p(0) = p(1) = p(-1) = 0 \), so \( p \) has three distinct roots while \( \deg p \le 2 \), hence \( p = 0 \). This is the only clause with any content, and it is where \( \dim V = 3 \) and the three sample points match up.

(b) Step 1 takes \( M = \bigl(\sum_i N(\v_i)^2\bigr)^{1/2} \) over the basis. Here \( N(1) = 1 + 1 + 1 = 3 \), \( N(x) = 0 + 1 + 1 = 2 \) and \( N(x^2) = 0 + 1 + 1 = 2 \), so
\[
M = \bigl(9 + 4 + 4\bigr)^{1/2} = \sqrt{17} .
\]

(c) \( V \) is finite-dimensional, so @thm-norm-equivalence applies to the pair \( N \), \( \norm{\cdot}_{\sB} \) and delivers both constants at once. Only the upper one is computable by hand from the basis; the lower one comes from compactness and the proof gives no formula for it.
:::

### C. Going deeper

:::: {#exr-equivalence-of-norms-c1}
[C1: Every linear map out of a finite-dimensional space is continuous]

Let \( V \) be finite-dimensional over \( F \) with norm \( \norm{\cdot}_V \), let \( W \) be a normed space over \( F \) with norm \( \norm{\cdot}_W \), and let \( T \colon V \to W \) be linear. Fix a basis \( \sB = (\v_1, \dots, \v_n) \) of \( V \) and write \( \norm{\cdot}_1 \) for the \( 1 \)-norm of the coordinate vector in the basis \( \sB \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \norm{T\v}_W \le K\norm{\v}_1 \) for every \( \v \in V \), where \( K = \max_i\norm{T\v_i}_W \).
2. Hence prove that there is a constant \( L \) with \( \norm{T\u - T\v}_W \le L\norm{\u - \v}_V \) for all \( \u, \v \in V \).
3. Explain why (b) may fail when \( V \) is infinite-dimensional, using @exm-norms-not-equivalent-infinite-dimension.
:::
::::

::: {.solution}
(a) Write \( \v = \sum_i x_i\v_i \). By linearity of \( T \), then (N3) and (N2) in \( W \),
\[
\norm{T\v}_W = \Bigl\lVert \sum_i x_iT\v_i \Bigr\rVert_W
\le \sum_i \lvert x_i\rvert\,\norm{T\v_i}_W
\le K\norm{\v}_1 .
\]

(b) The function \( \norm{\cdot}_1 \) is a norm on \( V \) (it is \( \norm{\cdot}_1 \) of @exm-p-norms transported by the coordinate isomorphism @cor-coordinate-isomorphism), and \( V \) is finite-dimensional, so by @thm-norm-equivalence there is \( C > 0 \) with \( \norm{\v}_1 \le C\norm{\v}_V \) for all \( \v \). Put \( L = KC \). By linearity, \( T\u - T\v = T(\u - \v) \), so (a) gives
\[
\norm{T\u - T\v}_W \le K\norm{\u - \v}_1 \le L\norm{\u - \v}_V .
\]

(c) Part (a) needs a **finite** basis expansion, and part (b) needs @thm-norm-equivalence, which is false in infinite dimension. Concretely, take \( V = \nR[x] \) with the coefficient norm \( \norm{\cdot}_\infty \) of @exm-norms-not-equivalent-infinite-dimension, \( W = \nR \) with \( \lvert\cdot\rvert \), and the linear functional \( T(p) = p(1) \), which adds up the coefficients. With \( p_k = 1 + x + \dots + x^{k-1} \) as there, the polynomials \( q_k = \tfrac1k p_k \) satisfy \( \norm{q_k}_\infty = 1/k \to 0 \) while \( T(q_k) = 1 \) for every \( k \). So \( T \) sends a sequence tending to \( 0 \) to a sequence that does not, and no constant \( L \) can exist.
:::

:::: {#exr-equivalence-of-norms-c2}
[C2: No dimension-free constants]

For each \( n \ge 1 \) let \( c_n, C_n > 0 \) be the best constants with
\[
c_n\norm{\x}_\infty \le \norm{\x}_1 \le C_n\norm{\x}_\infty
\qquad (\x \in F^n) .
\]

::: {.enumerate options="label=(\alph*)"}
1. Determine \( c_n \) and \( C_n \), with a vector attaining each.
2. Deduce that there is no pair of constants \( c, C > 0 \) working simultaneously for every \( n \).
3. A statement about \( \nR^n \) says "the error \( \e \) satisfies \( \norm{\e}_\infty \le 10^{-6} \)". What is the strongest bound on \( \norm{\e}_1 \) that follows, and for which \( n \) does it stop being informative if the entries of \( \e \) are themselves of size about \( 10^{-6} \)?
:::
::::

::: {.solution}
(a) \( c_n = 1 \) and \( C_n = n \). Indeed \( \norm{\x}_\infty = \lvert x_k\rvert \) for some \( k \), and \( \lvert x_k\rvert \le \sum_i\lvert x_i\rvert = \norm{\x}_1 \), with equality at \( \x = \e_1 \); and \( \norm{\x}_1 = \sum_i\lvert x_i\rvert \le n\max_i\lvert x_i\rvert = n\norm{\x}_\infty \), with equality at \( \x = \1 \). Both constants are therefore attained and cannot be improved.

(b) A dimension-free \( C \) would need \( C \ge C_n = n \) for every \( n \), which is impossible. (The constant \( c = 1 \) does happen to work for all \( n \); it is the upper constant that blows up, and one blown-up constant is enough.)

(c) The strongest bound is \( \norm{\e}_1 \le n\cdot 10^{-6} \), by (a), and it is attained when all entries have modulus \( 10^{-6} \) — which is exactly the situation described. So for \( n = 10^{6} \) the bound reads \( \norm{\e}_1 \le 1 \), which says nothing useful about a quantity that is itself of order \( 1 \). The two norms agree that the error tends to \( 0 \) as the computation improves; they disagree, by a factor of \( n \), about whether it is currently small.
:::

:::: {#exr-equivalence-of-norms-c3}
[C3: A finite-dimensional subspace is closed]

Let \( W \) be a normed space over \( F \) with norm \( \norm{\cdot} \), and let \( U \subseteq W \) be a **finite-dimensional** subspace. Let \( (\u_k) \) be a sequence in \( U \) with \( \norm{\u_k - \w} \to 0 \) for some \( \w \in W \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( (\u_k) \) is bounded in \( U \) for the restricted norm.
2. Using @cor-closed-bounded-compact, produce a subsequence \( (\u_{k_j}) \) converging to some \( \u \in U \).
3. Deduce that \( \w = \u \), so that \( U \) contains the limit of every convergent sequence of its own elements. *Hint: the triangle inequality, through \( \u_{k_j} \).*
:::
::::

::: {.solution}
(a) By @lem-reverse-triangle-norm, \( \bigl\lvert\norm{\u_k} - \norm{\w}\bigr\rvert \le \norm{\u_k - \w} \), and the right side tends to \( 0 \). So there is \( K \) with \( \norm{\u_k - \w} \le 1 \) for \( k \ge K \), whence \( \norm{\u_k} \le \norm{\w} + 1 \) for those \( k \); the finitely many earlier terms are bounded by their maximum. Hence \( (\u_k) \) is bounded.

(b) The restriction of \( \norm{\cdot} \) to \( U \) is a norm on \( U \), and \( U \) is finite-dimensional. The set \( K = \{\u \in U : \norm{\u} \le R\} \), with \( R \) the bound from (a), is closed and bounded in \( U \), hence compact by @cor-closed-bounded-compact. The sequence \( (\u_k) \) lies in \( K \), so some subsequence \( (\u_{k_j}) \) converges to a point \( \u \in K \subseteq U \).

(c) For every \( j \), by (N3),
\[
\norm{\w - \u} \le \norm{\w - \u_{k_j}} + \norm{\u_{k_j} - \u} .
\]
Both terms on the right tend to \( 0 \) as \( j \to \infty \): the first because \( (\u_k) \) converges to \( \w \) and a subsequence of a convergent sequence has the same limit, the second by (b). The left side does not depend on \( j \), so \( \norm{\w - \u} = 0 \), and (N1) gives \( \w = \u \in U \). Hence \( U \) contains every such limit, which is what it means for \( U \) to be closed in \( W \). Note that \( W \) itself was never assumed finite-dimensional; only \( U \) was, and that is exactly where @cor-closed-bounded-compact was applied.
:::
