# The Rayleigh Quotient

Chapter 12 used the number \( \inner{\A\x}{\x} \) as a *test*: positive for every non-zero \( \x \) means positive definite, non-negative means positive semidefinite, and that was the end of it. Chapter 12 §05 then noticed that the test carries more information than the verdict — normalized, it ranges over the interval between the smallest and largest eigenvalues — and stopped there. This section makes the normalized quantity an object with a name, finds its range exactly, finds the vectors where it is flat, and extracts a first description of every eigenvalue as a maximum. The description is correct and unsatisfying, and saying precisely why is the business of §02.

**Throughout, \( F \) is \( \nR \) or \( \nC \), every matrix is Hermitian, and its eigenvalues are indexed decreasingly**, \( \lambda_1(\A) \ge \dots \ge \lambda_n(\A) \), repeated according to multiplicity. The indexing presupposes that the eigenvalues are real, which is @thm-self-adjoint-real-eigenvalues. Inner products are the standard ones of \( F^n \), linear in the first slot.

## From a test to an object

Look at what @lem-extreme-eigenvalues-quadratic-form actually says. For a unit vector \( \x \), the number \( \inner{\A\x}{\x} \) lies between \( \lambda_n(\A) \) and \( \lambda_1(\A) \), and it reaches both ends. The restriction to unit vectors is a nuisance: doubling \( \x \) quadruples \( \inner{\A\x}{\x} \), so for \( \A \ne 0 \) the raw quantity has no bounded range at all and every statement about it must carry the clause "for \( \norm{\x} = 1 \)" along. Dividing by \( \norm{\x}^2 \) removes the nuisance permanently, and the resulting expression occurs often enough in what follows to deserve a name of its own.

*The Rayleigh quotient measures how much a Hermitian matrix stretches a vector along its own direction, on a scale where the vector's length has been divided out.*

::: {#def-rayleigh-quotient}
[Rayleigh Quotient]

Let \( F \) be \( \nR \) or \( \nC \) and let \( \A \in M_n(F) \) be **Hermitian**. The **Rayleigh quotient** of \( \A \) is the function
\[
R_{\A}(\x) \coloneqq \frac{\inner{\A\x}{\x}}{\inner{\x}{\x}} ,
\]
defined at **every** \( \x \in F^n \) with **\( \x \ne \0 \)**, and at no other vector.

For a self-adjoint operator \( T \) on a finite-dimensional inner product space \( V \) over \( F \), the same formula \( R_T(\v) = \inner{T\v}{\v}/\inner{\v}{\v} \), for \( \v \ne \0 \), defines the Rayleigh quotient of \( T \).
:::

Clause by clause. The word **Hermitian** is what makes the values real, and so what makes it sensible to ask for a maximum: by @prp-self-adjoint-immediate (a), \( \inner{\A\x}{\x} \in \nR \) for every \( \x \), even over \( \nC \). The condition **\( \x \ne \0 \)** is what makes the fraction mean anything: \( \inner{\x}{\x} = \norm{\x}^2 > 0 \) exactly for \( \x \ne \0 \), by positive definiteness of the inner product (@def-inner-product), and there is no value to assign at \( \0 \) — the numerator vanishes there too, and the quotient \( 0/0 \) would have to be given a value by hand, which no theorem below would thank us for. So \( R_{\A} \) is a real-valued function on \( F^n \setminus \{\0\} \).

**Well-definedness has a second half, and it is the useful one.** For a scalar \( c \ne 0 \),
\[
\begin{aligned}
\inner{\A(c\x)}{c\x} &= c\,\conj{c}\,\inner{\A\x}{\x} = \lvert c\rvert^2\inner{\A\x}{\x} ,\\
\inner{c\x}{c\x} &= \lvert c\rvert^2 \inner{\x}{\x} ,
\end{aligned}
\]
so the factor \( \lvert c\rvert^2 \) cancels and
\[
R_{\A}(c\x) = R_{\A}(\x) \qquad \text{for every } c \ne 0 .
\]
The Rayleigh quotient is therefore constant on each line through the origin with the origin removed. It is really a function on the set of lines, and the cheapest way to evaluate it is to normalize: for a **unit** vector \( \x \),
\[
R_{\A}(\x) = \inner{\A\x}{\x} .
\]
Every statement below may be read either way — over all non-zero vectors, or over the unit sphere — and we shall move between the two without comment.

::: {#exm-rayleigh-diagonal}
[A diagonal matrix, and the whole chapter in miniature]

Let \( \A = \diag(d_1, \dots, d_n) \) with real \( d_i \). Compute \( R_{\A} \).
:::

::: {.solution}
For \( \x = (x_1, \dots, x_n) \ne \0 \) we have \( \A\x = (d_1x_1, \dots, d_nx_n) \), so
\[
R_{\A}(\x) = \frac{\sum_{i} d_i\lvert x_i\rvert^2}{\sum_i \lvert x_i\rvert^2}
= \sum_{i} w_i d_i , \qquad
w_i = \frac{\lvert x_i\rvert^2}{\norm{\x}^2} .
\]
The weights \( w_i \) are non-negative and sum to \( 1 \). So \( R_{\A}(\x) \) is a **weighted average of the diagonal entries**, and \( \x \) is nothing but the recipe for the weights.
:::

That one line is the entire chapter in miniature, and it is worth pausing on. A weighted average of \( d_1, \dots, d_n \) can be any number between the smallest and the largest, and nothing else; it equals the largest only when all the weight sits on the largest entries; and to force it down to the second largest one must **forbid** the weight from sitting on the first. Every theorem in this chapter is one of those three sentences, stated for a general Hermitian matrix, where the diagonal entries are replaced by the eigenvalues and the coordinates \( x_i \) by the coefficients of \( \x \) in an orthonormal eigenbasis. The spectral theorem is what turns the general case into this one.

::: {#exm-rayleigh-two-by-two}
[A symmetric matrix on the unit circle]

Let \( \A = \begin{pmatrix} 3 & 1 \\ 1 & 3\end{pmatrix} \in M_2(\nR) \). Describe \( R_{\A} \) on the unit circle, and find its largest and smallest values.
:::

::: {.solution}
The eigenvalues are \( 4 \) and \( 2 \), with orthogonal eigenvectors \( \q_1 = \tfrac{1}{\sqrt2}(1,1) \) and \( \q_2 = \tfrac1{\sqrt2}(1,-1) \): indeed \( \A(1,1) = (4,4) \) and \( \A(1,-1) = (2,-2) \). Writing a unit vector as \( \x = (\cos\theta, \sin\theta) \),
\[
R_{\A}(\x) = \inner{\A\x}{\x}
= 3\cos^2\theta + 2\cos\theta\sin\theta + 3\sin^2\theta
= 3 + \sin 2\theta .
\]
So the values run over \( [2, 4] \); the maximum \( 4 \) occurs at \( \theta = \pi/4 \) and \( \theta = 5\pi/4 \), that is along the line through \( \q_1 \), and the minimum \( 2 \) at \( \theta = 3\pi/4 \) and \( 7\pi/4 \), along the line through \( \q_2 \). At \( \theta = 0 \) and \( \theta = \pi/2 \) the value is \( 3 \), the average of the two eigenvalues, which is also \( a_{11} = a_{22} \).
:::

\begin{center}
\begin{tikzpicture}[scale=1.8, lab/.style={font=\small}]
    \draw[->, gray] (-1.35,0) -- (1.42,0) node[above, black, lab] {$x_1$};
    \draw[->, gray] (0,-1.35) -- (0,1.42) node[left, black, lab] {$x_2$};
    \draw[thick] (0,0) circle (1);
    \draw[very thick] (-0.85,-0.85) -- (0.85,0.85);
    \draw[thick, dashed] (-0.85,0.85) -- (0.85,-0.85);
    \fill (0.7071,0.7071) circle (0.03);
    \fill (-0.7071,0.7071) circle (0.03);
    \fill (1,0) circle (0.03);
    \fill (0,1) circle (0.03);
    \node[lab] at (1.06,0.93) {$4$};
    \node[lab] at (-1.06,0.93) {$2$};
    \node[lab] at (1.12,-0.16) {$3$};
    \node[lab] at (-0.16,1.12) {$3$};
    \node[lab] at (0.62,0.34) {$\mathbf{q}_1$};
    \node[lab] at (-0.62,0.34) {$\mathbf{q}_2$};
    \node[lab, align=center] at (0,-1.78)
      {The values of $R_{\mathbf{A}}$ at four points of the unit circle, for\\
       the symmetric matrix with diagonal entries $3$ and off-diagonal\\
       entries $1$. It is largest along the eigenline through $\mathbf{q}_1$, smallest\\
       along the one through $\mathbf{q}_2$, and takes every value in between};
\end{tikzpicture}
\end{center}

::: {#exm-rayleigh-identity-and-projection}
[Two matrices whose quotient is forced]

Two further cases, at opposite extremes.

::: {.enumerate options="label=(\alph*)"}
1. **The identity.** \( R_{\I}(\x) = \inner{\x}{\x}/\inner{\x}{\x} = 1 \) for every \( \x \ne \0 \). The quotient is constant, and the constant is the only eigenvalue. More generally \( R_{c\I} \equiv c \) for real \( c \).
2. **An orthogonal projection.** Let \( \P \in M_n(F) \) be the matrix of the orthogonal projection onto a subspace \( U \), so \( \P^2 = \P \) and \( \P^{*} = \P \) (@thm-idempotent-orthogonal-iff-selfadjoint). Then \( \inner{\P\x}{\x} = \inner{\P^2\x}{\x} = \inner{\P\x}{\P\x} = \norm{\P\x}^2 \), so
\[
R_{\P}(\x) = \frac{\norm{\P\x}^2}{\norm{\x}^2} \in [0, 1] ,
\]
the fraction of \( \x \) that survives the projection. Since \( \norm{\x}^2 = \norm{\P\x}^2 + \norm{\x - \P\x}^2 \) by @thm-pythagoras, it equals \( 1 \) exactly when \( \P\x = \x \), that is on \( U \setminus\{\0\} \), and \( 0 \) exactly when \( \P\x = \0 \), that is on \( U^{\perp}\setminus\{\0\} \) — matching the eigenvalues \( 1 \) and \( 0 \) of \( \P \).
:::
:::

Case (a) is the degenerate one, and it earns its place: when all the eigenvalues coincide the interval of values collapses to a point, every non-zero vector is an eigenvector, and every theorem below becomes an equality between two copies of the same number. A statement that fails to survive \( \A = c\I \) has been stated wrongly.

::: {#exm-rayleigh-non-example}
[Change one word: drop Hermitian]

Take \( \A = \begin{pmatrix} 0 & 1 \\ 0 & 0\end{pmatrix} \in M_2(\nC) \), which is not Hermitian, and form \( \inner{\A\x}{\x}/\inner{\x}{\x} \) anyway. At \( \x = (1, i) \) the numerator is \( \inner{(i, 0)}{(1,i)} = i \cdot \conj{1} = i \) and the denominator is \( 2 \), so the quotient is \( i/2 \), which is not real. The clause that fails is the word **Hermitian** in @def-rayleigh-quotient, and it fails at the first step: @prp-self-adjoint-immediate (a) is what made the numerator real, and its hypothesis is gone.

Over \( \nR \) the failure is quieter and worse. For \( \A = \begin{pmatrix} 0 & -1 \\ 1 & 0\end{pmatrix} \in M_2(\nR) \) and real \( \x = (x_1, x_2) \),
\[
\inner{\A\x}{\x} = -x_2x_1 + x_1x_2 = 0 ,
\]
so the quotient is real, and identically \( 0 \). It is perfectly well behaved and tells us nothing: \( \A \) has no real eigenvalue at all, and there is no interval \( [\lambda_n, \lambda_1] \) for the quotient to describe.
:::

Why this definition, then. Dropping "Hermitian" costs the reality of the values, hence any notion of largest; the real \( 2\times 2 \) example above shows that it also destroys the link with the spectrum even when the values happen to stay real. Dropping the denominator costs scale invariance, and with it the possibility of writing \( \max \) without a side condition. Keeping the denominator but allowing \( \x = \0 \) costs nothing but sense.

::: {.warning}
**\( R_{\A}(\x) \) and \( \inner{\A\x}{\x} \) are the same number only for unit \( \x \).** The bound \( \inner{\A\x}{\x} \le \lambda_1(\A) \) of @lem-extreme-eigenvalues-quadratic-form is stated for unit vectors and is false without that hypothesis: for \( \A = \I_2 \) and \( \x = (10, 0) \) it would read \( 100 \le 1 \). The bound \( R_{\A}(\x) \le \lambda_1(\A) \), by contrast, holds for every \( \x \ne \0 \). Whenever a maximum over "all \( \x \)" appears below, it is a maximum of the **quotient**; the un-normalized form of the same statement always carries \( \norm{\x} = 1 \) with it.
:::

## What values it takes

@lem-extreme-eigenvalues-quadratic-form gives the two ends of the range. The following proposition adds that nothing in between is missing, which is a smaller statement than it looks and is worth proving explicitly rather than quoting a continuity argument.

::: {#prp-rayleigh-basic}
[The Range of the Rayleigh Quotient]

Let \( \A \in M_n(F) \) be Hermitian, \( n \ge 1 \). Then
\[
\bigl\{ R_{\A}(\x) : \x \in F^n,\ \x \ne \0 \bigr\}
= \bigl[\lambda_n(\A),\ \lambda_1(\A)\bigr] ,
\]
the whole closed interval. In particular
\[
\lambda_1(\A) = \max_{\x \ne \0} R_{\A}(\x), \qquad
\lambda_n(\A) = \min_{\x \ne \0} R_{\A}(\x) ,
\]
and both are attained, at unit eigenvectors for \( \lambda_1(\A) \) and \( \lambda_n(\A) \).
:::

::: {.idea}
Two inclusions of quite different weights. \( (\subseteq) \) is @lem-extreme-eigenvalues-quadratic-form with the normalization divided out, and costs one line. \( (\supseteq) \) asks for a vector realizing each intermediate value; the natural instinct is to move continuously along the sphere from a top eigenvector to a bottom one and quote the intermediate value theorem, but there is no need to import anything. Mixing a top eigenvector and a bottom eigenvector in the proportion \( t : 1-t \) puts weight \( t \) on \( \lambda_1 \) and \( 1-t \) on \( \lambda_n \), and the weighted average of @exm-rayleigh-diagonal sweeps the interval as \( t \) does.
:::

::: {.proof}
By the spectral theorem for matrices — @cor-spectral-complex-matrix over \( \nC \), @cor-spectral-real-matrix over \( \nR \) — there is an orthonormal basis \( (\q_1, \dots, \q_n) \) of \( F^n \) with \( \A\q_i = \lambda_i(\A)\q_i \) for every \( i \).

\( (\subseteq) \) Let \( \x \ne \0 \) and put \( \u = \x/\norm{\x} \), a unit vector. By the scale invariance established above, \( R_{\A}(\x) = R_{\A}(\u) = \inner{\A\u}{\u} \), which lies in \( [\lambda_n(\A), \lambda_1(\A)] \) by @lem-extreme-eigenvalues-quadratic-form.

\( (\supseteq) \) Let \( \mu \in [\lambda_n(\A), \lambda_1(\A)] \). If \( \lambda_1(\A) = \lambda_n(\A) \) the interval is the single point \( \mu = \lambda_1(\A) = R_{\A}(\q_1) \), and we are done. Otherwise put
\[
t = \frac{\mu - \lambda_n(\A)}{\lambda_1(\A) - \lambda_n(\A)} \in [0, 1],
\qquad
\x = \sqrt{t}\,\q_1 + \sqrt{1-t}\,\q_n ,
\]
which is legitimate because the denominator is non-zero and both square roots are of non-negative reals. Note \( n \ge 2 \) here, since \( \lambda_1 \ne \lambda_n \), so \( \q_1 \) and \( \q_n \) are distinct members of an orthonormal list. By @thm-orthonormal-coordinates (c),
\[
\norm{\x}^2 = t + (1-t) = 1 ,
\]
so in particular \( \x \ne \0 \). Since \( \A\x = \sqrt t\,\lambda_1(\A)\q_1 + \sqrt{1-t}\,\lambda_n(\A)\q_n \), @thm-orthonormal-coordinates (b) gives
\[
R_{\A}(\x) = \inner{\A\x}{\x}
= t\,\lambda_1(\A) + (1-t)\,\lambda_n(\A) = \mu ,
\]
the last equality by the choice of \( t \). So every point of the interval is a value.

For the attainment, \( R_{\A}(\q_1) = \lambda_1(\A) \) and \( R_{\A}(\q_n) = \lambda_n(\A) \). This proves the proposition.
:::

So the range is an **interval**, not a finite set, even though \( \A \) has at most \( n \) eigenvalues. That single fact is responsible for most of the confusion this chapter has to clear up, and the warning below spells out why.

::: {.check}
For \( \A = \diag(6, 3, 0) \), write down two unit vectors with Rayleigh quotient \( 4 \), each having one zero coordinate, in different positions.
:::

::: {.solution}
Mixing \( \e_1 \) and \( \e_3 \) as in the proof: \( 4 = 6t + 0(1-t) \) gives \( t = 2/3 \) and \( \x = \bigl(\sqrt{2/3},\, 0,\, \sqrt{1/3}\bigr) \), for which \( R_{\A}(\x) = 6\cdot\tfrac23 + 0\cdot\tfrac13 = 4 \). Mixing \( \e_1 \) and \( \e_2 \) instead: \( 4 = 6t + 3(1-t) \) gives \( t = 1/3 \) and \( \y = \bigl(\sqrt{1/3},\, \sqrt{2/3},\, 0\bigr) \), for which \( R_{\A}(\y) = 6\cdot\tfrac13 + 3\cdot\tfrac23 = 4 \). A value of \( R_{\A} \) is realized by many vectors, and they need not resemble each other.
:::

## Where the quotient is flat

The maximum and the minimum are attained at eigenvectors. There is a converse, and it identifies the eigenvectors among all vectors by a condition that does not mention eigenvalues: they are the places where \( R_{\A} \) does not move to first order. Everything needed is one algebraic identity, exact for every \( t \), so no calculus enters.

::: {#prp-rayleigh-critical-points}
[Critical Points of the Rayleigh Quotient]

Let \( \A \in M_n(F) \) be Hermitian, let \( \x \in F^n \) be a **unit** vector and put \( \mu = R_{\A}(\x) = \inner{\A\x}{\x} \). For every \( \v \in F^n \) and every \( t \in \nR \) with \( \x + t\v \ne \0 \),
\[
\begin{aligned}
&R_{\A}(\x + t\v) - \mu \\
&\qquad = \frac{2t\operatorname{Re}\inner{\A\x - \mu\x}{\v} + t^2\bigl(\inner{\A\v}{\v} - \mu\norm{\v}^2\bigr)}{\norm{\x + t\v}^2} .
\end{aligned}
\]{#eq-rayleigh-expansion}
Moreover:

::: {.enumerate options="label=(\alph*)"}
1. \( \operatorname{Re}\inner{\A\x - \mu\x}{\v} = 0 \) for every \( \v \in F^n \) **if and only if** \( \A\x = \mu\x \); that is, if and only if \( \x \) is an eigenvector of \( \A \), necessarily for the eigenvalue \( \mu \).
2. If \( R_{\A}(\x) \ge R_{\A}(\y) \) for every \( \y \ne \0 \), then the condition in (a) holds. The same is true if \( R_{\A}(\x) \le R_{\A}(\y) \) for every \( \y \ne \0 \).
:::
:::

::: {.idea}
Expand the numerator and the denominator of \( R_{\A}(\x + t\v) \) in powers of \( t \) and subtract \( \mu \) times the denominator from the numerator. The constant terms cancel by the definition of \( \mu \), and what is left is exactly @eq-rayleigh-expansion. The coefficient of \( t \) is the object of interest: (a) says it vanishes in every direction precisely at eigenvectors, and (b) says that at a maximum it must vanish, since otherwise a small step in the right direction would increase the quotient — the \( t^2 \) term cannot interfere, because for small \( t \) it is smaller than the \( t \) term.
:::

::: {.proof}
*The identity.* Expanding by sesquilinearity,
\[
\begin{aligned}
\inner{\A(\x + t\v)}{\x + t\v}
&= \inner{\A\x}{\x} + t\inner{\A\x}{\v} + t\inner{\A\v}{\x} + t^2\inner{\A\v}{\v} \\
&= \mu + 2t\operatorname{Re}\inner{\A\x}{\v} + t^2\inner{\A\v}{\v} ,
\end{aligned}
\]
where the second line used \( \inner{\A\v}{\x} = \inner{\v}{\A\x} = \conj{\inner{\A\x}{\v}} \), the first equality because \( \A \) is Hermitian and the second by conjugate symmetry (@def-inner-product), together with \( \inner{\A\x}{\x} = \mu \) for the unit vector \( \x \). The same computation with \( \A \) replaced by \( \I \), where the constant term is \( \norm{\x}^2 = 1 \), gives
\[
\norm{\x + t\v}^2 = 1 + 2t\operatorname{Re}\inner{\x}{\v} + t^2\norm{\v}^2 .
\]
Since \( \mu \) is real, \( \mu\operatorname{Re}\inner{\x}{\v} = \operatorname{Re}\inner{\mu\x}{\v} \). Subtracting \( \mu\norm{\x+t\v}^2 \) from the first display therefore leaves
\[
2t\operatorname{Re}\inner{\A\x - \mu\x}{\v} + t^2\bigl(\inner{\A\v}{\v} - \mu\norm{\v}^2\bigr) ,
\]
and dividing by \( \norm{\x + t\v}^2 \ne 0 \) gives @eq-rayleigh-expansion.

(a) Put \( \w = \A\x - \mu\x \). \( (\Leftarrow) \) If \( \A\x = \mu\x \) then \( \w = \0 \) and every \( \inner{\w}{\v} \) vanishes. \( (\Rightarrow) \) Take \( \v = \w \): the hypothesis gives \( \operatorname{Re}\inner{\w}{\w} = \norm{\w}^2 = 0 \), so \( \w = \0 \) by positive definiteness, that is \( \A\x = \mu\x \). Since \( \x \ne \0 \), this exhibits \( \x \) as an eigenvector for the eigenvalue \( \mu \).

(b) Suppose \( \x \) maximizes \( R_{\A} \) and, for a contradiction, that \( c \coloneqq 2\operatorname{Re}\inner{\A\x - \mu\x}{\v} \ne 0 \) for some \( \v \); then \( \v \ne \0 \). Put \( d = \inner{\A\v}{\v} - \mu\norm{\v}^2 \), and let \( t \) be any real number with
\[
0 < \lvert t\rvert < \frac{1}{2\norm{\v}}, \qquad
\lvert t \rvert\,\lvert d\rvert < \tfrac12\lvert c\rvert ,
\qquad \text{$t$ of the same sign as $c$} ,
\]
which is possible because the two upper bounds are positive. The first bound gives \( \norm{\x + t\v} \ge \norm{\x} - \lvert t\rvert\norm{\v} > 1 - \tfrac12 > 0 \), by the triangle inequality (@cor-triangle-inequality), so \( \x + t\v \ne \0 \) and the identity applies. The second gives \( \lvert td\rvert < \lvert c \rvert/2 \), so \( c + td \) has the same sign as \( c \), and hence \( t(c + td) > 0 \). By @eq-rayleigh-expansion,
\[
R_{\A}(\x + t\v) - \mu = \frac{t\,(c + t d)}{\norm{\x+t\v}^2} > 0 ,
\]
contradicting the maximality of \( R_{\A}(\x) \). So \( c = 0 \) for every \( \v \). For a minimizer, apply what has just been proved to \( -\A \), whose Rayleigh quotient is \( -R_{\A} \), so that a minimizer of \( R_{\A} \) is a maximizer of \( R_{-\A} \); the condition in (a) for \( -\A \) and \( -\mu \) is the same condition. This proves the proposition.
:::

Call a unit vector \( \x \) a **critical point** of \( R_{\A} \) when the condition in (a) holds, that is, when the coefficient of \( t \) in @eq-rayleigh-expansion vanishes in every direction \( \v \) — when \( R_{\A} \) moves away from \( R_{\A}(\x) \) only at second order. Parts (a) and (b) then say: *the critical points of \( R_{\A} \) on the unit sphere are exactly the unit eigenvectors of \( \A \), the critical values are exactly the eigenvalues, and every maximizer and every minimizer is among them.* That the eigenvalues are all realized as critical values is a direct computation: \( R_{\A}(\q_i) = \inner{\lambda_i\q_i}{\q_i} = \lambda_i \), and each \( \q_i \) is a unit eigenvector, hence a critical point by (b).

::: {.remark}
A reader who knows calculus will recognize @eq-rayleigh-expansion as saying that the directional derivative of \( R_{\A} \) at a unit vector \( \x \) in the direction \( \v \) is \( 2\operatorname{Re}\inner{\A\x - \mu\x}{\v} \), so that "critical point" has its usual meaning of a vanishing gradient. Nothing above uses derivatives: the identity @eq-rayleigh-expansion is exact for every \( t \), not an approximation, and the argument in (b) compares two explicit numbers. This matters for the accounting in the next remark.
:::

::: {.remark}
**The promise from Chapter 11 §02, and what it cost.** Chapter 11 §02 proved that a real self-adjoint operator has an eigenvalue by an algebraic route, and then described the alternative it was declining: "the function \( \v \mapsto \inner{T\v}{\v} \) is real-valued and continuous on the unit sphere of \( V \), which is closed and bounded, so it attains a maximum, and a vector where it does so turns out to be an eigenvector for the largest eigenvalue. That argument is shorter to state but it is analysis, not algebra, and it needs the extreme value theorem; we keep to the algebraic route so that nothing in this chapter depends on it. The maximization picture returns in Chapter 16, where the Rayleigh quotient and the Courant–Fischer theorem describe every eigenvalue of a self-adjoint operator by optimization."

The picture has now returned, and the account can be settled exactly. The clause "a vector where it does so turns out to be an eigenvector" is @prp-rayleigh-critical-points (b) and (a), and that the eigenvalue is the *largest* one is @prp-rayleigh-basic; neither invokes an analytic fact. What Chapter 11 would have had to import is only the *existence* of the maximizer, which is the extreme value theorem — fact (A4) of Chapter 15's introduction — applied to a continuous function on the unit sphere, compact by fact (A3). This chapter does not import it, because it does not have to: the spectral theorem is available here and it hands over the maximizer by name, namely \( \q_1 \), in @prp-rayleigh-basic. So the optimization description of eigenvalues in this chapter is a **consequence** of the spectral theorem, not an independent proof of it. One honest qualification: the spectral theorem itself rests on the fundamental theorem of algebra, which Chapter 5 §05 proved with the extreme value theorem on a disc. So the analysis is not absent from the foundations — it was spent once, there, and nothing here spends it again. Section 2 completes the promise for the intermediate eigenvalues, on the same terms.
:::

## Why the second eigenvalue is not a second maximum

::: {.warning}
**\( \lambda_2(\A) \) is not "the second largest value of \( R_{\A} \)", and there is no sense in which it could be.** Take \( \A = \diag(3, 1, -1) \), so \( \lambda_1 = 3 \), \( \lambda_2 = 1 \), \( \lambda_3 = -1 \). By @prp-rayleigh-basic the set of values of \( R_{\A} \) is the whole interval \( [-1, 3] \). Three things go wrong at once.

- **There is no second largest value.** The values below \( 3 \) form the interval \( [-1, 3) \), which has no largest element. So the phrase does not describe a number.
- **The value \( \lambda_2 \) is attained, but so is every other value, and not only at eigenvectors.** At \( \x = \tfrac1{\sqrt2}(1, 0, 1) \) the quotient is \( \tfrac12(3) + \tfrac12(-1) = 1 = \lambda_2(\A) \), and \( \x \) is not an eigenvector of \( \A \): it mixes the eigenvectors \( \e_1 \) and \( \e_3 \) of the first and the *third* eigenvalues, and \( \lambda_2 \) plays no part in it.
- **Removing a direction does not help by itself.** At \( \y = \tfrac1{\sqrt2}(1,1,0) \), which is orthogonal to the eigenvector \( \e_3 \) of \( \lambda_3 \), the quotient is \( \tfrac12(3) + \tfrac12(1) = 2 \), strictly between \( \lambda_1 \) and \( \lambda_2 \). Constraining \( \x \) to a subspace changes the answer, and which subspace is everything.

Whatever describes \( \lambda_2 \) must be a maximum over something smaller than the sphere.
:::

The last bullet says what to try. Cutting the sphere down by orthogonality to the top eigenvector does work, and the proof is @exm-rayleigh-diagonal again, with the top entry removed from the average.

::: {#prp-rayleigh-deflation}
[Eigenvalues by Deflation]

Let \( \A \in M_n(F) \) be Hermitian and let \( (\q_1, \dots, \q_n) \) be an orthonormal basis of \( F^n \) with \( \A\q_i = \lambda_i(\A)\q_i \) for every \( i \). Then for every \( k \) with \( 1 \le k \le n \),
\[
\lambda_k(\A) = \max\bigl\{ R_{\A}(\x) : \x \ne \0,\ \x \perp \q_1, \dots, \q_{k-1} \bigr\} ,
\]
the maximum being attained at \( \x = \q_k \). For \( k = 1 \) the list of constraints is empty and the statement is @prp-rayleigh-basic.
:::

::: {.idea}
The constraints do one thing: they delete the first \( k-1 \) coordinates in the eigenbasis. What is left is the weighted average of @exm-rayleigh-diagonal over the remaining eigenvalues \( \lambda_k \ge \dots \ge \lambda_n \), whose largest member is \( \lambda_k \).
:::

::: {.proof}
Let \( W = \{\x \in F^n : \inner{\x}{\q_i} = 0 \text{ for } 1 \le i \le k-1\} \). By @thm-orthonormal-coordinates (a) every \( \x \in F^n \) satisfies \( \x = \sum_{i=1}^{n}\inner{\x}{\q_i}\q_i \), so \( \x \in W \) exactly when \( \x \in \Span(\q_k, \dots, \q_n) \).

Let \( \x \in W \) with \( \x \ne \0 \), and write \( c_i = \inner{\x}{\q_i} \), so that \( \x = \sum_{i \ge k}c_i\q_i \). Then \( \A\x = \sum_{i\ge k}\lambda_i(\A)c_i\q_i \), and @thm-orthonormal-coordinates (b), (c) give
\[
\inner{\A\x}{\x} = \sum_{i \ge k}\lambda_i(\A)\lvert c_i\rvert^2 ,
\qquad
\norm{\x}^2 = \sum_{i\ge k}\lvert c_i\rvert^2 > 0 .
\]
Hence \( R_{\A}(\x) \) is a weighted average of \( \lambda_k(\A), \dots, \lambda_n(\A) \) with non-negative weights \( \lvert c_i\rvert^2/\norm{\x}^2 \) summing to \( 1 \). The largest of those eigenvalues is \( \lambda_k(\A) \), because the list is indexed decreasingly, so \( R_{\A}(\x) \le \lambda_k(\A) \).

Finally \( \q_k \in W \), since the \( \q_i \) are orthonormal, and \( R_{\A}(\q_k) = \inner{\lambda_k(\A)\q_k}{\q_k} = \lambda_k(\A) \). So the bound is attained and the supremum is a maximum. This proves the proposition.
:::

::: {.check}
In @prp-rayleigh-deflation, does the value of the maximum depend on which orthonormal eigenbasis \( (\q_1, \dots, \q_n) \) is chosen? Does the *maximizing vector*?
:::

::: {.solution}
The value does not: it is \( \lambda_k(\A) \), a number attached to \( \A \) alone. The maximizing vector generally does, and so does the constraint set \( W \). For \( \A = \diag(1, 1, 0) \) and \( k = 2 \), one admissible eigenbasis is \( (\e_1, \e_2, \e_3) \), giving \( W = \Span(\e_2, \e_3) \) and maximizer \( \e_2 \); another is \( \bigl(\tfrac1{\sqrt2}(1,1,0), \tfrac1{\sqrt2}(1,-1,0), \e_3\bigr) \), giving a different \( W \) and the maximizer \( \tfrac1{\sqrt2}(1,-1,0) \). Both maxima equal \( \lambda_2(\A) = 1 \).
:::

## What is still wrong

@prp-rayleigh-deflation is a complete answer to the question "what is \( \lambda_k(\A) \), as an optimization?" and it is nearly useless. The reason is visible in its statement: the constraint set is built from \( \q_1, \dots, \q_{k-1} \), which are eigenvectors of \( \A \). To use the formula one must already know the eigenvectors, and to know the eigenvectors one must already have solved the problem the formula claims to describe. It is a description of \( \lambda_k(\A) \) in terms of \( \A \)'s own answer.

The cost is not merely aesthetic. The whole point of turning an eigenvalue into an optimization is to compare the eigenvalues of **different** matrices: to say that \( \A \succeq \B \) forces \( \lambda_i(\A) \ge \lambda_i(\B) \), or that perturbing \( \A \) moves \( \lambda_i \) only a little. A comparison needs the two optimizations to run over the *same* set. Deflation gives \( \lambda_i(\A) \) as a maximum over the orthogonal complement of \( \A \)'s top eigenvectors, and \( \lambda_i(\B) \) as a maximum over the orthogonal complement of \( \B \)'s top eigenvectors, and those two subspaces have nothing to do with each other. Nothing can be concluded.

Chapter 12 §12 promised that "Chapter 16 characterizes the eigenvalues of a Hermitian matrix as maxima and minima of \( \inner{\A\x}{\x} \) — at which point the test becomes the theory". @prp-rayleigh-basic and @prp-rayleigh-deflation are the first installment of that, and they show that the promise can be kept. The test has already become a statement about a single number: \( \A \succ 0 \) exactly when \( \lambda_n(\A) = \min_{\x\ne\0}R_{\A}(\x) \) is positive, and \( \A \succeq 0 \) exactly when it is non-negative, which is the eigenvalue criterion of @thm-pd-characterizations and @thm-psd-characterizations read through @prp-rayleigh-basic. The rest of it is the removal of the eigenvectors from the statement, which §02 achieves by a device that looks extravagant and is exactly right: keep the maximum over a subspace, but let the subspace vary over **all** subspaces of the appropriate dimension, and take the minimum of what comes out.

## Exercises

### A. Check your understanding

:::: {#exr-rayleigh-quotient-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State @def-rayleigh-quotient, naming both hypotheses, and say what each one is for.
2. Prove that \( R_{\A}(c\x) = R_{\A}(\x) \) for every scalar \( c \ne 0 \), and explain why this makes \( R_{\A} \) a function on lines.
3. Determine whether the following is correct, and justify your answer: if \( \A \in M_3(\nR) \) is symmetric with three distinct eigenvalues, then \( R_{\A} \) takes exactly three values.
4. State @prp-rayleigh-deflation, and say in one sentence why it is not a satisfactory description of \( \lambda_k(\A) \).
5. Give a Hermitian \( \A \) and a vector \( \x \) that is **not** an eigenvector of \( \A \) but has \( R_{\A}(\x) \) equal to an eigenvalue of \( \A \).
:::
::::

::: {.solution}
(a) Let \( F \) be \( \nR \) or \( \nC \) and \( \A \in M_n(F) \) Hermitian. For \( \x \ne \0 \), the Rayleigh quotient is \( R_{\A}(\x) = \inner{\A\x}{\x}/\inner{\x}{\x} \). Hermitian makes the numerator real (@prp-self-adjoint-immediate (a)) and ties the values to the spectrum; \( \x \ne \0 \) makes the denominator non-zero (@def-inner-product).

(b) \( \inner{\A(c\x)}{c\x} = c\conj{c}\inner{\A\x}{\x} = \lvert c\rvert^2\inner{\A\x}{\x} \) and likewise \( \inner{c\x}{c\x} = \lvert c\rvert^2\inner{\x}{\x} \); the factor \( \lvert c\rvert^2 \ne 0 \) cancels. So \( R_{\A} \) is constant on \( \{c\x : c \ne 0\} \), the punctured line through \( \x \), and its value depends only on which line \( \x \) lies on.

(c) Incorrect. By @prp-rayleigh-basic the set of values is the whole of the interval \( [\lambda_3(\A), \lambda_1(\A)] \), which is infinite whenever \( \lambda_1(\A) \ne \lambda_3(\A) \), and distinct eigenvalues guarantee that.

(d) With \( (\q_1, \dots, \q_n) \) an orthonormal eigenbasis ordered so that \( \A\q_i = \lambda_i(\A)\q_i \), \( \lambda_k(\A) \) is the maximum of \( R_{\A} \) over the non-zero vectors orthogonal to \( \q_1, \dots, \q_{k-1} \). It is unsatisfactory because the constraint set is built from eigenvectors of \( \A \), so the formula presupposes the answer and cannot compare two different matrices.

(e) \( \A = \diag(3, 1, -1) \) and \( \x = (1, 0, 1) \): \( R_{\A}(\x) = (3 - 1)/2 = 1 = \lambda_2(\A) \), while \( \A\x = (3, 0, -1) \) is not a multiple of \( \x \). (Any mixture of a top and a bottom eigenvector in the right proportion does the same job.)
:::

### B. Practice

:::: {#exr-rayleigh-quotient-b1}
[B1: Locating four values]

Let
\[
\A = \begin{pmatrix} 2 & 2 & 0 \\ 2 & 3 & 2 \\ 0 & 2 & 4 \end{pmatrix} \in M_3(\nR) .
\]
Its eigenvalues are \( 6, 3, 0 \), with eigenvectors \( (1,2,2) \), \( (2,1,-2) \) and \( (2,-2,1) \) respectively; you may take this as given. Compute \( R_{\A}(\x) \) for \( \x = \e_1 \), \( \x = (1,1,1) \), \( \x = (1,1,0) \) and \( \x = (1,0,-1) \), and check each value against @prp-rayleigh-basic. Hence exhibit a non-eigenvector at which \( R_{\A} \) equals an eigenvalue.
::::

::: {.solution}
The three given vectors are pairwise orthogonal, each of norm \( 3 \), so \( \q_1 = \tfrac13(1,2,2) \), \( \q_2 = \tfrac13(2,1,-2) \), \( \q_3 = \tfrac13(2,-2,1) \) is an orthonormal eigenbasis with \( \lambda_1 = 6 \), \( \lambda_2 = 3 \), \( \lambda_3 = 0 \). By @prp-rayleigh-basic every value must lie in \( [0, 6] \).

For \( \x = \e_1 \): \( \A\e_1 = (2,2,0) \), so \( \inner{\A\x}{\x} = 2 \) and \( \norm{\x}^2 = 1 \), giving \( R_{\A}(\e_1) = 2 \). (This is the diagonal entry \( a_{11} \), as it must be for a standard basis vector.)

For \( \x = (1,1,1) \): \( \A\x = (4, 7, 6) \) and \( \inner{\A\x}{\x} = 4 + 7 + 6 = 17 \), while \( \norm{\x}^2 = 3 \); so \( R_{\A}(\x) = 17/3 \approx 5.67 \).

For \( \x = (1,1,0) \): \( \A\x = (4, 5, 2) \) and \( \inner{\A\x}{\x} = 9 \), \( \norm{\x}^2 = 2 \); so \( R_{\A}(\x) = 9/2 \).

For \( \x = (1,0,-1) \): \( \A\x = (2, 0, -4) \) and \( \inner{\A\x}{\x} = 2 + 4 = 6 \), \( \norm{\x}^2 = 2 \); so \( R_{\A}(\x) = 3 \).

All four values lie in \( [0,6] \). The last one equals \( \lambda_2(\A) = 3 \), yet \( \A(1,0,-1) = (2,0,-4) \) is not a multiple of \( (1,0,-1) \), so \( (1,0,-1) \) is not an eigenvector. This is the trap of the warning above, in a concrete matrix.
:::

:::: {#exr-rayleigh-quotient-b2}
[B2: A prescribed value]

With \( \A \) and the orthonormal eigenbasis of @exr-rayleigh-quotient-b1, use the construction in the proof of @prp-rayleigh-basic to produce a unit vector \( \x \) with \( R_{\A}(\x) = 2 \). Then find, by mixing \( \q_1 \) and \( \q_2 \) in equal proportion, a vector with integer entries whose Rayleigh quotient is \( 9/2 \).
::::

::: {.solution}
For the first, \( \mu = 2 \) with \( \lambda_1 = 6 \) and \( \lambda_3 = 0 \) gives \( t = (2-0)/(6-0) = 1/3 \), so
\[
\x = \sqrt{\tfrac13}\,\q_1 + \sqrt{\tfrac23}\,\q_3 ,
\]
a unit vector with \( R_{\A}(\x) = \tfrac13\cdot 6 + \tfrac23\cdot 0 = 2 \).

For the second, \( \y = \q_1 + \q_2 = \tfrac13\bigl((1,2,2) + (2,1,-2)\bigr) = (1,1,0) \), whose Rayleigh quotient is the average \( \tfrac12(6) + \tfrac12(3) = 9/2 \) — matching the direct computation in @exr-rayleigh-quotient-b1. Equal proportions of two orthonormal eigenvectors give the plain average of their eigenvalues.
:::

:::: {#exr-rayleigh-quotient-b3}
[B3: The quotient of a projection]

Let \( U = \Span\{(1,1,0), (0,0,1)\} \subseteq \nR^3 \) and let \( \P \) be the matrix of the orthogonal projection onto \( U \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \P \), and list the eigenvalues of \( \P \) with multiplicity.
2. Compute \( R_{\P}(\x) \) for \( \x = \e_1 \), \( \x = (1,-1,0) \) and \( \x = (1,-1,1) \), and check each against @prp-rayleigh-basic.
:::
::::

::: {.solution}
(a) The two spanning vectors are orthogonal, of norms \( \sqrt2 \) and \( 1 \), so \( \u_1 = \tfrac1{\sqrt2}(1,1,0) \) and \( \u_2 = (0,0,1) \) form an orthonormal basis of \( U \) and \( \P = \u_1\u_1\tp + \u_2\u_2\tp \), that is
\[
\P = \begin{pmatrix} 1/2 & 1/2 & 0 \\ 1/2 & 1/2 & 0 \\ 0 & 0 & 1\end{pmatrix} .
\]
Its eigenvalues are \( 1 \) with multiplicity \( 2 \) (on \( U \)) and \( 0 \) with multiplicity \( 1 \) (on \( U^{\perp} = \Span\{(1,-1,0)\} \)), so \( \lambda_1 = \lambda_2 = 1 \) and \( \lambda_3 = 0 \).

(b) By @exm-rayleigh-identity-and-projection (b), \( R_{\P}(\x) = \norm{\P\x}^2/\norm{\x}^2 \).
For \( \x = \e_1 \): \( \P\e_1 = (\tfrac12, \tfrac12, 0) \), so \( \norm{\P\x}^2 = \tfrac12 \) and \( R_{\P}(\e_1) = \tfrac12 \).
For \( \x = (1,-1,0) \): \( \P\x = \0 \), so \( R_{\P}(\x) = 0 \).
For \( \x = (1,-1,1) \): \( \P\x = (0,0,1) \), so \( \norm{\P\x}^2 = 1 \) and \( \norm{\x}^2 = 3 \), giving \( R_{\P}(\x) = 1/3 \).
All three lie in \( [\lambda_3, \lambda_1] = [0,1] \), and the middle one attains the lower end, as it must, being a non-zero vector of \( U^{\perp} \).
:::

### C. Going deeper

:::: {#exr-rayleigh-quotient-c1}
[C1: Why the quotient estimates eigenvalues so well]

Let \( \A \in M_n(F) \) be Hermitian with orthonormal eigenbasis \( (\q_1, \dots, \q_n) \), \( \A\q_i = \lambda_i(\A)\q_i \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that for every unit vector \( \x \),
\[
\lambda_1(\A) - R_{\A}(\x) \ \le\ \bigl(\lambda_1(\A) - \lambda_n(\A)\bigr)\,\norm{\x - \q_1}^2 .
\]
2. Deduce that if \( \norm{\x - \q_1} \le \varepsilon \) then \( R_{\A}(\x) \) approximates \( \lambda_1(\A) \) with error at most \( (\lambda_1 - \lambda_n)\varepsilon^2 \): an error in the eigen*vector* of size \( \varepsilon \) costs only \( \varepsilon^2 \) in the eigen*value*.
3. Show that the exponent \( 2 \) cannot be improved, by computing both sides for \( \A = \diag(1,0) \) and \( \x = (\cos\varepsilon, \sin\varepsilon) \).
:::

*Hint for (a): expand \( \x \) in the eigenbasis and compare the two sums term by term.*
::::

::: {.solution}
(a) Write \( c_i = \inner{\x}{\q_i} \), so \( \sum_i\lvert c_i\rvert^2 = 1 \) by @thm-orthonormal-coordinates (c). As in @prp-rayleigh-deflation, \( R_{\A}(\x) = \sum_i\lambda_i(\A)\lvert c_i\rvert^2 \), so
\[
\lambda_1(\A) - R_{\A}(\x)
= \sum_{i=1}^{n}\bigl(\lambda_1(\A) - \lambda_i(\A)\bigr)\lvert c_i\rvert^2
\le \bigl(\lambda_1(\A) - \lambda_n(\A)\bigr)\sum_{i \ge 2}\lvert c_i\rvert^2 ,
\]
where the \( i = 1 \) term was dropped because it is \( 0 \) and each remaining factor \( \lambda_1 - \lambda_i \) was enlarged to \( \lambda_1 - \lambda_n \), legitimate since \( \lvert c_i\rvert^2 \ge 0 \) and the eigenvalues decrease. On the other side, again by @thm-orthonormal-coordinates (c),
\[
\norm{\x - \q_1}^2 = \lvert c_1 - 1\rvert^2 + \sum_{i\ge2}\lvert c_i\rvert^2
\ \ge\ \sum_{i\ge2}\lvert c_i\rvert^2 .
\]
Combining the two displays gives the inequality.

(b) Immediate from (a), since the right-hand side is increasing in \( \norm{\x - \q_1} \).

(c) Here \( \lambda_1 = 1 \), \( \lambda_2 = 0 \) and \( \q_1 = \e_1 \). The vector \( \x = (\cos\varepsilon, \sin\varepsilon) \) is a unit vector with
\[
R_{\A}(\x) = \cos^2\varepsilon , \qquad
\lambda_1 - R_{\A}(\x) = \sin^2\varepsilon ,
\]
while \( \norm{\x - \e_1}^2 = (\cos\varepsilon - 1)^2 + \sin^2\varepsilon = 2 - 2\cos\varepsilon \). The bound in (a) reads \( \sin^2\varepsilon \le 2 - 2\cos\varepsilon \), which is true, and the ratio of the two sides is
\[
\frac{\sin^2\varepsilon}{2 - 2\cos\varepsilon}
= \frac{(1-\cos\varepsilon)(1+\cos\varepsilon)}{2(1 - \cos\varepsilon)}
= \frac{1 + \cos\varepsilon}{2} ,
\]
which tends to \( 1 \) as \( \varepsilon \to 0 \). So the error really is of order \( \varepsilon^2 \), not smaller, and the constant in (a) is sharp in the limit. This second-order accuracy is why the Rayleigh quotient is the standard way to read an eigenvalue off an approximate eigenvector, and Chapter 23 builds an iteration on it.
:::

:::: {#exr-rayleigh-quotient-c2}
[C2: The equality case at the top]

Let \( \A \in M_n(F) \) be Hermitian and let \( E_{\lambda_1}(\A) = \ker(\A - \lambda_1(\A)\I) \) be the eigenspace of the largest eigenvalue.

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( \x \ne \0 \) and \( R_{\A}(\x) = \lambda_1(\A) \), then \( \x \in E_{\lambda_1}(\A) \).
2. Deduce that \( \{\x \ne \0 : R_{\A}(\x) = \lambda_1(\A)\} \cup \{\0\} = E_{\lambda_1}(\A) \).
3. Show that the corresponding statement for an intermediate eigenvalue is **false**, by naming a matrix, an index \( k \) with \( 1 < k < n \), and a vector.
:::
::::

::: {.solution}
(a) We may assume \( \norm{\x} = 1 \), by scale invariance and because \( E_{\lambda_1}(\A) \) is a subspace. Write \( c_i = \inner{\x}{\q_i} \) for an orthonormal eigenbasis as above, so \( \sum_i\lvert c_i\rvert^2 = 1 \) and \( R_{\A}(\x) = \sum_i\lambda_i(\A)\lvert c_i\rvert^2 \). Then
\[
0 = \lambda_1(\A) - R_{\A}(\x) = \sum_{i=1}^{n}\bigl(\lambda_1(\A) - \lambda_i(\A)\bigr)\lvert c_i\rvert^2 ,
\]
a sum of non-negative terms. Every term is therefore \( 0 \), so \( c_i = 0 \) whenever \( \lambda_i(\A) < \lambda_1(\A) \). Hence \( \x = \sum_{i : \lambda_i = \lambda_1}c_i\q_i \), a combination of eigenvectors for \( \lambda_1(\A) \), so \( \x \in E_{\lambda_1}(\A) \).

(b) \( (\subseteq) \) is (a), together with \( \0 \in E_{\lambda_1}(\A) \). \( (\supseteq) \) If \( \0 \ne \x \in E_{\lambda_1}(\A) \) then \( \A\x = \lambda_1(\A)\x \), so \( R_{\A}(\x) = \lambda_1(\A)\inner{\x}{\x}/\inner{\x}{\x} = \lambda_1(\A) \).

(c) Take \( \A = \diag(3,1,-1) \), \( k = 2 \) and \( \x = (1,0,1) \). Then \( R_{\A}(\x) = 1 = \lambda_2(\A) \), but \( \A\x = (3,0,-1) \) is not a multiple of \( \x \), so \( \x \notin E_{\lambda_2}(\A) = \Span\{\e_2\} \). The argument in (a) breaks because the terms \( (\lambda_2 - \lambda_i)\lvert c_i\rvert^2 \) are no longer all of the same sign: the \( i = 1 \) term is negative and cancels against the \( i = 3 \) term instead of forcing both to vanish.
:::

:::: {#exr-rayleigh-quotient-c3}
[C3: What the quotient cannot see]

Let \( \M \in M_n(F) \) be an arbitrary matrix, not assumed Hermitian, and put
\[
\A = \tfrac12(\M + \M^{*}), \qquad \B = \tfrac12(\M - \M^{*}) ,
\]
so that \( \M = \A + \B \) with \( \A^{*} = \A \) and \( \B^{*} = -\B \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \operatorname{Re}\inner{\M\x}{\x} = \inner{\A\x}{\x} \) for every \( \x \in F^n \).
2. Deduce that over \( \nR \), the function \( \x \mapsto \inner{\M\x}{\x} \) determines \( \A \) and nothing whatever about \( \B \). Give two distinct real \( 2\times2 \) matrices with the same such function.
3. Over \( \nC \), determine whether \( \inner{\M\x}{\x} = 0 \) for all \( \x \) forces \( \M = 0 \). Justify your answer.
:::
::::

::: {.solution}
(a) By conjugate symmetry and the definition of the adjoint, \( \inner{\M^{*}\x}{\x} = \inner{\x}{\M\x} = \conj{\inner{\M\x}{\x}} \). Hence
\[
\inner{\A\x}{\x} = \tfrac12\bigl(\inner{\M\x}{\x} + \conj{\inner{\M\x}{\x}}\bigr)
= \operatorname{Re}\inner{\M\x}{\x} .
\]

(b) Over \( \nR \) every inner product value is real, so (a) reads \( \inner{\M\x}{\x} = \inner{\A\x}{\x} \) for all \( \x \): the function sees only \( \A \). It determines \( \A \) completely, since two symmetric matrices with the same quadratic form are equal (@thm-self-adjoint-zero-test applied to their difference). It sees nothing of \( \B \): for
\[
\M_1 = \begin{pmatrix} 0 & 0 \\ 0 & 0\end{pmatrix},
\qquad
\M_2 = \begin{pmatrix} 0 & -1 \\ 1 & 0\end{pmatrix},
\]
both functions are identically \( 0 \), since \( \inner{\M_2\x}{\x} = -x_2x_1 + x_1x_2 = 0 \), yet \( \M_1 \ne \M_2 \). This is @exr-self-adjoint-operators-c3 in matrix language.

(c) Yes, over \( \nC \) it does force \( \M = 0 \). This is @thm-complex-zero-test, and the reason the complex theory is the cleaner one: a complex quadratic form determines its matrix, so nothing is invisible. Concretely, (a) gives \( \A = 0 \), and applying the hypothesis to \( i\M \) — or expanding \( \inner{\M(\x + \y)}{\x+\y} \) and \( \inner{\M(\x+i\y)}{\x+i\y} \) — kills \( \B \) as well. The real \( 2 \times 2 \) matrix \( \M_2 \) of (b) shows that the same statement over \( \nR \) is false, so this is genuinely a fact about the field.
:::
