# The Fundamental Theorem of Algebra

Chapter 0 stated the Fundamental Theorem of Algebra (@thm-fta-statement) and promised a proof. Everything algebraic that the proof needs is now in place: division, the Factor Theorem, multiplicities, and the polar form of complex numbers with De Moivre's formula. What algebra alone cannot supply is a property of the real numbers that goes beyond the field axioms, and some such property must enter, because \( \nQ \) is a field too and there \( x^2 - 2 \) has no root. We use completeness, in the form of the extreme value theorem. This section isolates the analytic input in two clearly labeled facts, proves everything else in full, and then draws the consequences for real polynomials: conjugate pairs, irreducible factors of degree at most \( 2 \), and real roots of odd-degree polynomials.

## The goal and the plan

Here is the theorem we want, in the language of this chapter. A polynomial \( p \in \nC[x] \) of degree \( n \ge 1 \) is exactly the expression \( a_nx^n + \dots + a_0 \) with \( a_n \neq 0 \) of @thm-fta-statement.

::: {#thm-fundamental-theorem-of-algebra}
[Fundamental Theorem of Algebra]

Every non-constant polynomial \( p \in \nC[x] \) has a root in \( \nC \).
:::

We prove it after three lemmas. The proof is a minimum argument, and it runs in three steps.

① **Growth.** Far from the origin, \( \lvert p(z) \rvert \) is large, because the leading term \( a_nz^n \) outweighs all the others. We will prove this with an explicit radius.

② **A minimum exists.** On a large closed disc, the continuous function \( z \mapsto \lvert p(z) \rvert \) attains a smallest value. By ①, nothing outside the disc does better, so this is the smallest value of \( \lvert p \rvert \) on all of \( \nC \).

③ **A non-zero value is never the minimum.** If \( p(z_0) \neq 0 \), we can move from \( z_0 \) a little in a well-chosen direction and make \( \lvert p \rvert \) strictly smaller. This is d'Alembert's lemma, and it is pure algebra of \( \nC \).

Putting ② and ③ together, the minimum value must be \( 0 \), and the point where it is attained is a root.

Steps ① and ③ are proved from scratch. Step ② is where analysis enters, and we say exactly how.

::: {.remark}
**What we assume from analysis.** The proof uses exactly two facts from real analysis, and nothing else: no limits, no derivatives, no intermediate value theorem. We identify \( \nC \) with \( \nR^2 \) as in @def-complex-numbers, so that \( \lvert z - w \rvert \) is the usual distance in the plane.

::: {.enumerate options="label=(A\arabic*)"}
1. **Continuity of polynomial functions.** For every \( p \in \nC[x] \), the function \( \nC \to \nR \), \( z \mapsto \lvert p(z) \rvert \), is continuous.
2. **Extreme value theorem on a closed disc.** Let \( \rho \ge 0 \) and \( D = \{ z \in \nC : \lvert z \rvert \le \rho \} \). If \( g \colon D \to \nR \) is continuous, then there is \( w \in D \) with \( g(w) \le g(z) \) for **every** \( z \in D \).
:::

Fact (A2) is where the completeness of \( \nR \) is used. Everything else below is the arithmetic of \( \nC \) from Chapter 0, including polar form and @thm-de-moivre.
:::

## Step 1: growth

We use three small facts about the modulus repeatedly. For \( z, w, z_1, \dots, z_m \in \nC \) and \( j \in \nN \):
\[
\lvert z^j \rvert = \lvert z \rvert^j, \qquad \lvert z_1 + \dots + z_m \rvert \le \lvert z_1 \rvert + \dots + \lvert z_m \rvert, \qquad \lvert z + w \rvert \ge \lvert z \rvert - \lvert w \rvert .
\]
The first follows from @thm-conjugate-properties (d) by induction on \( j \), and the second from @thm-complex-triangle-inequality by induction on \( m \). For the third, apply the triangle inequality to \( z = (z + w) + (-w) \) and use \( \lvert -w \rvert = \lvert w \rvert \).

The leading term wins as soon as \( \lvert z \rvert \) exceeds a radius computed from the coefficients.

::: {#lem-polynomial-growth}
[Growth of a Polynomial]

Let \( p = a_nx^n + \dots + a_1x + a_0 \in \nC[x] \) with \( n \ge 1 \) and \( a_n \neq 0 \). Put
\[
A = \lvert a_0 \rvert + \lvert a_1 \rvert + \dots + \lvert a_{n-1} \rvert, \qquad R = \max\Bigl\{ 1, \frac{2A}{\lvert a_n \rvert} \Bigr\} .
\]
Then for every \( z \in \nC \) with \( \lvert z \rvert \ge R \),
\[
\lvert p(z) \rvert \ge \tfrac12 \lvert a_n \rvert\, \lvert z \rvert^n \ge \tfrac12 \lvert a_n \rvert\, \lvert z \rvert .
\]
In particular, for every real \( M \ge 0 \), we have \( \lvert p(z) \rvert > M \) whenever \( \lvert z \rvert \ge R \) and \( \lvert z \rvert > 2M / \lvert a_n \rvert \).
:::

::: {.idea}
Compare the leading term with the rest. When \( \lvert z \rvert \ge 1 \), every lower power \( \lvert z \rvert^j \) is at most \( \lvert z \rvert^{n-1} \), so the rest is at most \( A\lvert z \rvert^{n-1} \), while the leading term is \( \lvert a_n \rvert \lvert z \rvert^n \). The rest is at most half the leading term once \( A \le \tfrac12 \lvert a_n \rvert \lvert z \rvert \), which is how \( R \) was found.
:::

::: {.proof}
Let \( \lvert z \rvert \ge R \). Since \( \lvert z \rvert \ge 1 \), we have \( \lvert z \rvert^j \le \lvert z \rvert^{n-1} \) for \( 0 \le j \le n - 1 \). By the triangle inequality (@thm-complex-triangle-inequality),
\[
\Bigl\lvert \sum_{j=0}^{n-1} a_jz^j \Bigr\rvert \le \sum_{j=0}^{n-1} \lvert a_j \rvert \lvert z \rvert^j \le A \lvert z \rvert^{n-1} .
\]
Since \( \lvert z \rvert \ge 2A/\lvert a_n \rvert \), we have \( A \le \tfrac12 \lvert a_n \rvert \lvert z \rvert \). By the reverse triangle inequality,
\[
\lvert p(z) \rvert \ge \lvert a_n \rvert \lvert z \rvert^n - A\lvert z \rvert^{n-1} \ge \lvert a_n \rvert \lvert z \rvert^n - \tfrac12 \lvert a_n \rvert \lvert z \rvert^n = \tfrac12 \lvert a_n \rvert \lvert z \rvert^n .
\]
Since \( \lvert z \rvert \ge 1 \) and \( n \ge 1 \), \( \lvert z \rvert^n \ge \lvert z \rvert \), which gives the second inequality. Finally, if also \( \lvert z \rvert > 2M/\lvert a_n \rvert \), then \( \lvert p(z) \rvert \ge \tfrac12 \lvert a_n \rvert \lvert z \rvert > M \). This proves the lemma.
:::

For example, for \( p = x^3 - 5x + 1 \) we get \( A = 6 \) and \( R = 12 \), so \( \lvert p(z) \rvert \ge \tfrac12\lvert z \rvert^3 \) whenever \( \lvert z \rvert \ge 12 \). The radius is far from optimal, and it does not need to be. We only need **some** radius beyond which \( \lvert p \rvert \) is large.

## Step 2: the minimum is attained

::: {#lem-minimum-modulus-attained}
[The Minimum of \( \lvert p \rvert \) Is Attained]

Let \( p \in \nC[x] \). Then there is \( z_0 \in \nC \) with \( \lvert p(z_0) \rvert \le \lvert p(z) \rvert \) for **every** \( z \in \nC \).
:::

::: {.idea}
Use (A2) on a disc so big that outside it, \( \lvert p \rvert \) exceeds \( \lvert p(0) \rvert \). The disc contains \( 0 \), so its minimum is at most \( \lvert p(0) \rvert \), and the points outside cannot compete. @lem-polynomial-growth tells us how big "so big" is.
:::

::: {.proof}
If \( p \) is constant, every \( z_0 \) works. Suppose \( p = a_nx^n + \dots + a_0 \) with \( n \ge 1 \) and \( a_n \neq 0 \), and let \( R \) be the radius of @lem-polynomial-growth. Put \( M = \lvert p(0) \rvert \) and
\[
\rho = R + \frac{2M}{\lvert a_n \rvert}, \qquad D = \{ z \in \nC : \lvert z \rvert \le \rho \} .
\]
By (A1), \( z \mapsto \lvert p(z) \rvert \) is continuous on \( D \), so by (A2) there is \( z_0 \in D \) with \( \lvert p(z_0) \rvert \le \lvert p(z) \rvert \) for every \( z \in D \).

Now let \( z \notin D \), so \( \lvert z \rvert > \rho \). Then \( \lvert z \rvert > R \), and \( \lvert z \rvert > 2M/\lvert a_n \rvert \) because \( R \ge 1 > 0 \). By @lem-polynomial-growth, \( \lvert p(z) \rvert > M = \lvert p(0) \rvert \). Since \( 0 \in D \), \( \lvert p(0) \rvert \ge \lvert p(z_0) \rvert \). Hence \( \lvert p(z) \rvert > \lvert p(z_0) \rvert \) for \( z \notin D \), and \( \lvert p(z) \rvert \ge \lvert p(z_0) \rvert \) for \( z \in D \). This proves the lemma.
:::

## Step 3: d'Alembert's lemma

It remains to show that a non-zero value of \( \lvert p \rvert \) is never the smallest one. Near \( z_0 \), write \( p(z_0 + h) = b_0 + b_kh^k + (\text{terms of higher degree in } h) \), where \( b_0 = p(z_0) \) and \( b_kh^k \) is the first non-constant term that is actually present. For small \( h \), the term \( b_kh^k \) dominates the later ones, so we choose the direction of \( h \) to make \( b_kh^k \) point from \( b_0 \) straight toward \( 0 \).

::: {#lem-dalembert}
[d'Alembert's Lemma]

Let \( p \in \nC[x] \) be non-constant, and let \( z_0 \in \nC \) with \( p(z_0) \neq 0 \). Then there is \( z \in \nC \) with \( \lvert p(z) \rvert < \lvert p(z_0) \rvert \).
:::

::: {.idea}
Picture the values \( p(z_0 + h) \) in the plane. As \( h = tu \) runs over a small circle \( \lvert h \rvert = t \), the term \( b_0 + b_kh^k \) runs \( k \) times around the circle of radius \( t^k\lvert b_k \rvert \) centered at \( b_0 = p(z_0) \). One point of that circle lies on the segment from \( b_0 \) to \( 0 \), at distance \( \lvert b_0 \rvert - t^k\lvert b_k \rvert \) from \( 0 \). Reaching it needs a \( k \)-th root of a unit complex number, which De Moivre supplies. The higher terms move the value by at most a multiple of \( t^{k+1} \), a blur much smaller than the gain \( t^k\lvert b_k \rvert \) when \( t \) is small.

\begin{center}
\begin{tikzpicture}[scale=1.1]
    \draw[->] (-0.4,0) -- (5.6,0) node[right] {$\operatorname{Re}$};
    \draw[->] (0,-0.4) -- (0,3.6) node[above] {$\operatorname{Im}$};
    \fill (0,0) circle (1.5pt) node[below left] {$0$};
    \draw[dotted] (0,0) -- (4,2);
    \draw[dashed] (8:4.472) arc (8:52:4.472);
    \node[right] at (8:4.55) {\small radius $\lvert b_0 \rvert$};
    \draw (4,2) circle (1.2);
    \fill[gray!40] (2.927,1.463) circle (0.35);
    \draw (2.927,1.463) circle (0.35);
    \draw[very thick,->] (4,2) -- (2.95,1.475);
    \fill (4,2) circle (1.5pt);
    \node[right] at (5.45,1.75) {$b_0 = p(z_0)$};
    \draw[->] (5.45,1.75) -- (4.1,1.97);
    \node[align=center] at (4.6,3.55) {\small $b_0 + b_k h^k$, \ $\lvert h \rvert = t$};
    \draw[->] (4.2,3.3) -- (4.3,3.12);
    \node[align=left] at (1.3,2.6) {\small higher terms: \\ \small within $t^{k+1}B$};
    \draw[->] (1.6,2.2) -- (2.72,1.72);
\end{tikzpicture}
\end{center}

The dashed arc is part of the circle of radius \( \lvert b_0 \rvert \) about \( 0 \), the old value of \( \lvert p \rvert \). The solid circle shows where \( b_0 + b_kh^k \) goes for \( \lvert h \rvert = t \). The arrow is the chosen direction, and the shaded disc is the uncertainty caused by the higher terms. The whole shaded disc lies strictly inside the dashed circle, which is the inequality \( \lvert p(z_0 + h) \rvert < \lvert p(z_0) \rvert \).
:::

::: {.proof}
Let \( n = \deg p \ge 1 \).

**Step 1: re-center at \( z_0 \).** By @thm-polynomial-taylor (a), \( \bigl(1, x - z_0, \dots, (x - z_0)^n\bigr) \) is a basis of \( \nC[x]_{\le n} \), so \( p = \sum_{j=0}^{n} b_j(x - z_0)^j \) for some \( b_0, \dots, b_n \in \nC \). Evaluating at \( z_0 \) gives \( b_0 = p(z_0) \neq 0 \). The coefficient of \( x^n \) on the right is \( b_n \), since \( (x - z_0)^j \) has degree \( j \) and \( (x - z_0)^n \) is monic; so \( b_n \) is the leading coefficient of \( p \), and \( b_n \neq 0 \). By @thm-evaluation-respects-operations, for every \( h \in \nC \),
\[
p(z_0 + h) = \sum_{j=0}^{n} b_jh^j .
\]
Since \( b_n \neq 0 \) and \( n \ge 1 \), there is a **smallest** \( k \ge 1 \) with \( b_k \neq 0 \). Then \( b_1 = \dots = b_{k-1} = 0 \), and
\[
p(z_0 + h) = b_0 + b_kh^k + \sum_{j=k+1}^{n} b_jh^j . \tag{$\ast$}
\]

**Step 2: choose the direction.** Since \( b_0 \neq 0 \) and \( b_k \neq 0 \), the number \( w = -b_0/b_k \) is non-zero. Write it in polar form, \( w = \lvert w \rvert e^{i\alpha} \) with \( \alpha \in \nR \), and put \( u = e^{i\alpha/k} \). Then \( \lvert u \rvert = 1 \), and \( u^k = e^{i\alpha} \) by @thm-de-moivre. Using \( b_kw = -b_0 \) and \( \lvert w \rvert = \lvert b_0 \rvert / \lvert b_k \rvert \) (@thm-conjugate-properties (d)),
\[
b_ku^k = \frac{b_kw}{\lvert w \rvert} = -\frac{\lvert b_k \rvert}{\lvert b_0 \rvert}\, b_0 .
\]
Hence, for every real \( t > 0 \),
\[
b_0 + b_k(tu)^k = b_0\Bigl(1 - t^k\frac{\lvert b_k \rvert}{\lvert b_0 \rvert}\Bigr) .
\]

**Step 3: choose the size.** Put \( B = \lvert b_{k+1} \rvert + \dots + \lvert b_n \rvert \) (so \( B = 0 \) if \( k = n \)), and
\[
t = \min\Bigl\{ 1, \ \frac{\lvert b_0 \rvert}{\lvert b_k \rvert}, \ \frac{\lvert b_k \rvert}{2B} \Bigr\},
\]
where the last entry is omitted if \( B = 0 \). Then \( t > 0 \), and \( t \) has three properties.

(i) \( 0 < t^k\lvert b_k \rvert / \lvert b_0 \rvert \le 1 \). Indeed, if \( \lvert b_0 \rvert/\lvert b_k \rvert \ge 1 \), then \( t^k \le 1 \le \lvert b_0 \rvert/\lvert b_k \rvert \); otherwise \( t \le \lvert b_0 \rvert/\lvert b_k \rvert < 1 \), and \( t^k \le t \le \lvert b_0 \rvert/\lvert b_k \rvert \).

(ii) \( tB \le \tfrac12\lvert b_k \rvert \). This is trivial if \( B = 0 \), and follows from \( t \le \lvert b_k \rvert/(2B) \) otherwise.

(iii) \( t^j \le t^{k+1} \) for every \( j \ge k + 1 \), since \( 0 < t \le 1 \).

**Step 4: estimate.** Let \( z = z_0 + tu \). By Step 2 and (i), the number \( 1 - t^k\lvert b_k \rvert/\lvert b_0 \rvert \) is real and lies in \( [0, 1) \), so
\[
\bigl\lvert b_0 + b_k(tu)^k \bigr\rvert = \lvert b_0 \rvert\Bigl(1 - t^k\frac{\lvert b_k \rvert}{\lvert b_0 \rvert}\Bigr) = \lvert b_0 \rvert - t^k\lvert b_k \rvert .
\]
By the triangle inequality (@thm-complex-triangle-inequality), \( \lvert u \rvert = 1 \) and (iii),
\[
\Bigl\lvert \sum_{j=k+1}^{n} b_j(tu)^j \Bigr\rvert \le \sum_{j=k+1}^{n} \lvert b_j \rvert t^j \le t^{k+1}B .
\]
Combining these with \( (\ast) \), the triangle inequality and (ii),
\[
\lvert p(z) \rvert \le \lvert b_0 \rvert - t^k\lvert b_k \rvert + t^{k+1}B = \lvert b_0 \rvert - t^k\bigl(\lvert b_k \rvert - tB\bigr) \le \lvert b_0 \rvert - \tfrac12 t^k\lvert b_k \rvert < \lvert b_0 \rvert ,
\]
where the last step uses \( t > 0 \) and \( b_k \neq 0 \). Since \( \lvert b_0 \rvert = \lvert p(z_0) \rvert \), this proves the lemma.
:::

Every hypothesis did a job. Non-constant gave the index \( k \). The condition \( p(z_0) \neq 0 \) let us divide by \( \lvert b_0 \rvert \) and fix a direction toward \( 0 \). And the field \( \nC \) supplied the \( k \)-th root \( u \), the one step that has no analogue over \( \nR \).

::: {#exm-dalembert-step}
[One Step Downhill]

Let \( p = x^3 + x^2 + 1 \in \nC[x] \) and \( z_0 = 0 \). Follow the proof of @lem-dalembert to find \( z \) with \( \lvert p(z) \rvert < \lvert p(0) \rvert \).
:::

::: {.solution}
Here \( p(0) = 1 \) and the expansion at \( z_0 = 0 \) is \( p \) itself: \( b_0 = 1 \), \( b_1 = 0 \), \( b_2 = 1 \), \( b_3 = 1 \). The first non-zero \( b_j \) with \( j \ge 1 \) is \( b_2 \), so \( k = 2 \) and \( B = \lvert b_3 \rvert = 1 \).

Direction: \( w = -b_0/b_2 = -1 = e^{i\pi} \), so \( \alpha = \pi \) and \( u = e^{i\pi/2} = i \). Indeed \( b_2u^2 = -1 \) points from \( b_0 = 1 \) toward \( 0 \).

Size: \( t = \min\{1, \ 1/1, \ 1/(2 \cdot 1)\} = \tfrac12 \). So \( z = \tfrac{i}{2} \), and
\[
p\bigl(\tfrac{i}{2}\bigr) = -\tfrac{i}{8} - \tfrac14 + 1 = \tfrac34 - \tfrac{i}{8}, \qquad \bigl\lvert p\bigl(\tfrac{i}{2}\bigr) \bigr\rvert = \sqrt{\tfrac{9}{16} + \tfrac{1}{64}} = \frac{\sqrt{37}}{8} \approx 0.76 < 1 .
\]
The proof guarantees \( \lvert p(z) \rvert \le 1 - \tfrac12 \cdot \tfrac14 \cdot 1 = \tfrac78 \), and \( \sqrt{37}/8 \le \tfrac78 \) since \( 37 \le 49 \). The direction matters: along the real axis, \( p(\tfrac12) = \tfrac18 + \tfrac14 + 1 = \tfrac{11}{8} > 1 \), because there \( b_2h^2 = \tfrac14 \) points away from \( 0 \).
:::

## The proof of the theorem

The three steps now combine into a proof of @thm-fundamental-theorem-of-algebra.

::: {.proof}
Let \( p \in \nC[x] \) be non-constant. By @lem-minimum-modulus-attained there is \( z_0 \in \nC \) with \( \lvert p(z_0) \rvert \le \lvert p(z) \rvert \) for every \( z \in \nC \). Suppose, for a contradiction, that \( p(z_0) \neq 0 \). By @lem-dalembert there is \( z \) with \( \lvert p(z) \rvert < \lvert p(z_0) \rvert \), contradicting the choice of \( z_0 \). Hence \( p(z_0) = 0 \), and \( z_0 \) is a root of \( p \).
:::

This proves Chapter 0's @thm-fta-statement: a polynomial \( a_nz^n + \dots + a_0 \) with \( n \ge 1 \) and \( a_n \neq 0 \) is a non-constant element of \( \nC[x] \), and we have just shown that it has a root.

::: {.check}
The polynomial \( p = x^2 + 1 \in \nR[x] \) has no real root, yet the function \( c \mapsto \lvert p(c) \rvert \) on \( \nR \) has a minimum, at \( c = 0 \). Which step of the argument breaks if we try to run it over \( \nR \)?
:::

::: {.solution}
Growth and the attained minimum both hold on \( \nR \): the minimum value is \( \lvert p(0) \rvert = 1 \). The step that fails is d'Alembert's lemma. At \( z_0 = 0 \) we have \( b_0 = 1 \), \( k = 2 \), \( b_2 = 1 \), so we need a direction \( u \) with \( u^2 = w = -1 \). There is no such real \( u \), and indeed \( p(h) = 1 + h^2 \ge 1 \) for every real \( h \). Over \( \nC \), \( u = i \) works and \( p(ti) = 1 - t^2 < 1 \) for \( 0 < t \le 1 \).
:::

::: {.warning}
**The theorem is an existence theorem.** It says a root exists; it does not say how to find one, and the proof does not produce one. There is no formula for the roots of a general polynomial of degree \( 5 \) or more built from the coefficients by \( +, -, \times, \div \) and \( k \)-th roots (a theorem from Galois theory, which we do not prove). Numerical root-finding algorithms approximate roots; that is a different subject, and the Fundamental Theorem of Algebra is not one of those algorithms.
:::

## Complex polynomials split

Combining the theorem with the root count of the previous section gives the form in which it is used most.

::: {#cor-complex-polynomial-splits}
[Complex Polynomials Split]

::: {.enumerate options="label=(\alph*)"}
1. Every non-zero \( p \in \nC[x] \) splits over \( \nC \): if \( \deg p = n \) and \( p \) has leading coefficient \( a \), then \( p = a(x - z_1)(x - z_2)\cdots(x - z_n) \) for some \( z_1, \dots, z_n \in \nC \). In particular the multiplicities of the roots of \( p \) add up to \( n \).
2. The irreducible polynomials in \( \nC[x] \) are exactly the polynomials of degree \( 1 \).
:::
:::

::: {.proof}
(a) By @thm-roots-with-multiplicity, \( p = (x - c_1)^{m_1}\cdots(x - c_k)^{m_k}\,g \), where \( c_1, \dots, c_k \) are the distinct roots of \( p \) in \( \nC \) and \( g \in \nC[x] \) has no root in \( \nC \). By @thm-fundamental-theorem-of-algebra, \( g \) is constant, and \( g \neq 0 \) because \( p \neq 0 \). So \( p \) splits over \( \nC \), and the multiplicities add up to \( n \) by the same theorem. Comparing leading coefficients (@thm-degree-of-product), the constant is \( a \).

(b) A polynomial of degree \( 1 \) is irreducible, since a factorization into two non-constant factors would have degree at least \( 2 \). Conversely, let \( p \in \nC[x] \) be irreducible. It is non-constant (@def-irreducible-polynomial), so by (a) it has a factor \( x - z_1 \), say \( p = (x - z_1)q \). Since \( p \) is irreducible and \( x - z_1 \) is not constant, \( q \) is a non-zero constant, and \( \deg p = 1 \).
:::

So in \( \nC[x] \), unique factorization (@thm-unique-factorization-polynomials) is completely explicit: the monic irreducible factors are the \( x - z \), and the exponent of \( x - z \) is the multiplicity of \( z \). In Chapter 8 this is what gives every operator on a non-zero finite-dimensional complex vector space an eigenvalue. (That fact also has a proof using only linear algebra, and one can run the logic in the other direction; we will not need it.)

::: {#exm-factor-x4-plus-1}
[Factoring \( x^4 + 1 \) over \( \nC \) and over \( \nR \)]

Factor \( f = x^4 + 1 \) into irreducible polynomials in \( \nC[x] \) and in \( \nR[x] \).
:::

::: {.solution}
*Roots.* We solve \( z^4 = -1 = e^{i\pi} \) as in @exm-roots-of-unity. Write \( z = re^{i\theta} \) with \( r > 0 \); by @thm-de-moivre, \( z^4 = r^4e^{4i\theta} \). Comparing polar forms, \( r^4 = 1 \), so \( r = 1 \), and \( 4\theta = \pi + 2\pi j \) for an integer \( j \). The values \( j = 0, 1, 2, 3 \) give four distinct roots
\[
z_0 = e^{i\pi/4} = \tfrac{\sqrt2}{2} + \tfrac{\sqrt2}{2}i, \quad z_1 = e^{3i\pi/4} = -\tfrac{\sqrt2}{2} + \tfrac{\sqrt2}{2}i, \quad z_2 = \conj{z_1}, \quad z_3 = \conj{z_0} .
\]

*Over \( \nC \).* Four distinct roots, each of multiplicity at least \( 1 \), and \( \deg f = 4 \), so by @thm-roots-with-multiplicity each multiplicity is \( 1 \) and
\[
x^4 + 1 = (x - z_0)(x - z_1)(x - z_2)(x - z_3) ,
\]
the leading coefficient being \( 1 \). The factors are irreducible by @cor-complex-polynomial-splits (b).

*Over \( \nR \).* Pair each root with its conjugate. For any \( z \in \nC \),
\[
(x - z)(x - \conj{z}) = x^2 - (z + \conj{z})x + z\conj{z} = x^2 - 2\operatorname{Re}(z)\,x + \lvert z \rvert^2 \in \nR[x] ,
\]
by @thm-conjugate-properties (c). With \( \operatorname{Re} z_0 = \tfrac{\sqrt2}{2} \), \( \operatorname{Re} z_1 = -\tfrac{\sqrt2}{2} \) and \( \lvert z_0 \rvert = \lvert z_1 \rvert = 1 \),
\[
x^4 + 1 = \bigl(x^2 - \sqrt2\,x + 1\bigr)\bigl(x^2 + \sqrt2\,x + 1\bigr) .
\]
Check: the product is \( (x^2 + 1)^2 - 2x^2 = x^4 + 1 \). Each quadratic has non-real roots only, hence no real root, so it is irreducible over \( \nR \) by @thm-irreducible-deg-2-3. Note that \( x^4 + 1 \) has no real root but is **reducible** over \( \nR \).
:::

## Real polynomials

A real polynomial is also a complex polynomial, so the theorem applies to it; the roots it provides may be non-real. They are not scattered arbitrarily. Chapter 0 observed that non-real roots of a real polynomial come in conjugate pairs; we now show that the pairs also share their multiplicity. For \( g = \sum_j c_jx^j \in \nC[x] \) write \( \conj{g} = \sum_j \conj{c_j}\,x^j \), the polynomial with conjugated coefficients.

::: {#thm-real-roots-conjugate-pairs}
[Conjugate Roots Have Equal Multiplicity]

Let \( f \in \nR[x] \) be non-zero, regarded as an element of \( \nC[x] \), and let \( z \in \nC \). Then \( f(\conj{z}) = \conj{f(z)} \). In particular \( z \) is a root of \( f \) if and only if \( \conj{z} \) is, and
\[
\operatorname{mult}_{\conj{z}}(f) = \operatorname{mult}_z(f) .
\]
:::

::: {.idea}
Conjugation respects sums and products of complex numbers, so applying it to all coefficients respects sums and products of polynomials. A real polynomial is unchanged by it. So conjugating a factorization \( f = (x - z)^mg \) gives a factorization \( f = (x - \conj{z})^m\conj{g} \), and the cofactor test transfers.
:::

::: {.proof}
Let \( g = \sum_j c_jx^j \) and \( h = \sum_j d_jx^j \) be in \( \nC[x] \), and \( z \in \nC \). By @thm-conjugate-properties (a) and (b), the coefficient of \( x^k \) in \( \conj{gh} \) is \( \conj{\sum_{i+j=k} c_id_j} = \sum_{i+j=k} \conj{c_i}\,\conj{d_j} \), which is the coefficient of \( x^k \) in \( \conj{g}\,\conj{h} \). So \( \conj{gh} = \conj{g}\,\conj{h} \). By the same parts, \( \conj{g}(\conj{z}) = \sum_j \conj{c_j}\,\conj{z}^j = \conj{\sum_j c_jz^j} = \conj{g(z)} \).

Since \( f \) has real coefficients, \( \conj{f} = f \). Hence \( f(\conj{z}) = \conj{f}(\conj{z}) = \conj{f(z)} \), and \( f(z) = 0 \) if and only if \( f(\conj{z}) = 0 \).

Let \( m = \operatorname{mult}_z(f) \). By @lem-multiplicity-cofactor, \( f = (x - z)^mg \) with \( g \in \nC[x] \) and \( g(z) \neq 0 \). Conjugating, and using \( \conj{x - z} = x - \conj{z} \),
\[
f = \conj{f} = (x - \conj{z})^m\,\conj{g}, \qquad \conj{g}(\conj{z}) = \conj{g(z)} \neq 0 .
\]
By @lem-multiplicity-cofactor again, \( \operatorname{mult}_{\conj{z}}(f) = m \). This proves the theorem.
:::

For instance, a real polynomial with \( 2 + i \) as a root of multiplicity \( 3 \) also has \( 2 - i \) as a root of multiplicity \( 3 \), so by @thm-roots-with-multiplicity its degree is at least \( 6 \). Now the irreducible real polynomials can be listed.

::: {#cor-real-irreducibles}
[Irreducible Real Polynomials]

The irreducible polynomials in \( \nR[x] \) are exactly the polynomials of degree \( 1 \), and the polynomials of degree \( 2 \) with no real root. In particular, every irreducible polynomial in \( \nR[x] \) has degree \( 1 \) or \( 2 \).
:::

::: {.idea}
An irreducible real \( p \) has a complex root \( z \) by the theorem. If \( z \) is real, \( x - z \) is a real factor and \( p \) is linear. If not, \( \conj{z} \) is another root, and \( (x - z)(x - \conj{z}) \) is a **real** quadratic dividing \( p \). The only subtle point is that it divides \( p \) in \( \nR[x] \) and not merely in \( \nC[x] \); uniqueness of division settles that.
:::

::: {.proof}
(⇐) A polynomial of degree \( 1 \) is irreducible, since a product of two non-constant polynomials has degree at least \( 2 \) (@thm-degree-of-product). A polynomial of degree \( 2 \) with no real root is irreducible by @thm-irreducible-deg-2-3.

(⇒) Let \( p \in \nR[x] \) be irreducible. It is non-constant, so by @thm-fundamental-theorem-of-algebra it has a root \( z \in \nC \).

*Case 1: \( z \in \nR \).* By @lem-factor-theorem-linear in \( \nR[x] \), \( p = (x - z)q \) with \( q \in \nR[x] \). Since \( p \) is irreducible and \( x - z \) is not constant, \( q \) is a non-zero constant, so \( \deg p = 1 \).

*Case 2: \( z \notin \nR \).* Then \( \conj{z} \neq z \), and \( \conj{z} \) is also a root by @thm-real-roots-conjugate-pairs. Applying @cor-root-bound-general in \( \nC[x] \) to the two distinct roots \( z, \conj{z} \) gives \( p = (x - z)(x - \conj{z})\,h \) for some \( h \in \nC[x] \). Put \( q = (x - z)(x - \conj{z}) = x^2 - 2\operatorname{Re}(z)x + \lvert z \rvert^2 \), which lies in \( \nR[x] \). Divide in \( \nR[x] \) (@thm-polynomial-division): \( p = qh_1 + r \) with \( h_1, r \in \nR[x] \) and \( \deg r < 2 \). This is also a division with remainder in \( \nC[x] \), and so is \( p = qh + 0 \). By the uniqueness in @thm-polynomial-division over \( \nC \), \( r = 0 \) and \( h = h_1 \in \nR[x] \). So \( p = qh_1 \) in \( \nR[x] \). Since \( p \) is irreducible and \( q \) is not constant, \( h_1 \) is a non-zero constant, and \( \deg p = 2 \). Finally, \( p \) has no real root, because a real root \( c \) would give a factor \( x - c \) and \( p = (x - c)q' \) with \( \deg q' = 1 \), contradicting irreducibility. This proves the corollary.
:::

::: {.remark}
Completing the square decides which quadratics occur: \( x^2 + \beta x + \gamma = \bigl(x + \tfrac{\beta}{2}\bigr)^2 - \tfrac{\beta^2 - 4\gamma}{4} \) has a real root if and only if \( \beta^2 - 4\gamma \ge 0 \). So the monic irreducible real quadratics are those with \( \beta^2 < 4\gamma \).
:::

Unique factorization in \( \nR[x] \) now takes a concrete form.

::: {#cor-real-factorization}
[Factorization over \( \nR \)]

Every non-constant \( f \in \nR[x] \) can be written as
\[
f = a\,(x - c_1)\cdots(x - c_r)\;q_1\cdots q_s ,
\]
where \( a \in \nR \) is the leading coefficient of \( f \), \( c_1, \dots, c_r \in \nR \) (not necessarily distinct), and \( q_1, \dots, q_s \in \nR[x] \) are monic quadratics with no real root. Then \( r + 2s = \deg f \), and \( r \) is the sum of the multiplicities of the real roots of \( f \). The factorization is unique up to the order of the factors.
:::

::: {.proof}
By @thm-unique-factorization-polynomials, \( f = a\,p_1\cdots p_k \) with \( p_i \in \nR[x] \) monic irreducible, unique up to order. By @cor-real-irreducibles each \( p_i \) is either \( x - c \) with \( c \in \nR \) or a monic quadratic with no real root; list the first kind as \( x - c_1, \dots, x - c_r \) and the second as \( q_1, \dots, q_s \). Then \( \deg f = r + 2s \) by @thm-degree-of-product. For a real number \( c \), each \( q_j \) has multiplicity \( 0 \) at \( c \), and \( x - c_i \) has multiplicity \( 1 \) or \( 0 \) according as \( c_i = c \) or not; by @thm-multiplicity-of-product, \( \operatorname{mult}_c(f) \) is the number of indices \( i \) with \( c_i = c \). Adding over the real roots of \( f \) gives \( r \).
:::

The last consequence is one that calculus proves with the intermediate value theorem. Here it falls out of counting degrees.

::: {#cor-odd-degree-real-root}
[Odd Degree Forces a Real Root]

Every \( f \in \nR[x] \) of odd degree has a root in \( \nR \).
:::

::: {.proof}
By @cor-real-factorization, \( \deg f = r + 2s \). Since \( \deg f \) is odd, \( r \) is odd, so \( r \ge 1 \), and \( c_1 \) is a real root of \( f \).
:::

::: {.warning}
**No real root does not mean irreducible over \( \nR \).** By @cor-real-irreducibles, an irreducible real polynomial has degree at most \( 2 \); so \( x^4 + 1 \), which has no real root, is still reducible over \( \nR \) (@exm-factor-x4-plus-1). The test "reducible if and only if it has a root" is only valid in degrees \( 2 \) and \( 3 \) (@thm-irreducible-deg-2-3).
:::

## Exercises

### A. Check your understanding

:::: {#exr-fundamental-theorem-of-algebra-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the Fundamental Theorem of Algebra, and list the two facts from analysis used in its proof in this section.
2. True or false: every polynomial in \( \nR[x] \) of degree \( 4 \) has a real root. Justify your answer.
3. True or false: if \( f \in \nR[x] \) has \( 2 + i \) as a root of multiplicity \( 3 \), then \( \deg f \ge 6 \). Justify your answer.
4. True or false: every polynomial in \( \nR[x] \) of degree \( 5 \) has a real root. Justify your answer.
5. True or false: every irreducible polynomial in \( \nF_2[x] \) has degree at most \( 2 \). Justify your answer.
6. In the proof of d'Alembert's lemma (@lem-dalembert), which property of \( \nC \) is used that \( \nR \) lacks?
:::
::::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Every non-constant \( p \in \nC[x] \) has a root in \( \nC \) (@thm-fundamental-theorem-of-algebra). The analytic facts are (A1) continuity of \( z \mapsto \lvert p(z) \rvert \) on \( \nC \), and (A2) the extreme value theorem for continuous real functions on a closed disc.
2. False. \( x^4 + 1 \ge 1 \) at every real number, so it has no real root.
3. True. By @thm-real-roots-conjugate-pairs, \( 2 - i \) is also a root of multiplicity \( 3 \), and \( 2 - i \neq 2 + i \). By @thm-roots-with-multiplicity, \( \deg f \ge 3 + 3 = 6 \).
4. True, by @cor-odd-degree-real-root.
5. False. \( x^3 + x + 1 \) takes the value \( 1 \) at both \( 0 \) and \( 1 \), so it has no root in \( \nF_2 \), and a cubic without a root is irreducible by @thm-irreducible-deg-2-3. @cor-real-irreducibles is special to \( \nR \).
6. Every non-zero complex number has a \( k \)-th root; the proof takes a \( k \)-th root of a complex number of modulus \( 1 \) by @thm-de-moivre. Over \( \nR \), \( -1 \) has no square root.
:::
:::

### B. Practice

:::: {#exr-fundamental-theorem-of-algebra-b1}
[B1: \( x^4 + 4 \)]

Find all complex roots of \( x^4 + 4 \), and factor it into irreducible polynomials in \( \nC[x] \) and in \( \nR[x] \).
::::

::: {.solution}
Write \( z = re^{i\theta} \) with \( r > 0 \). By @thm-de-moivre, \( z^4 = r^4e^{4i\theta} \), and \( -4 = 4e^{i\pi} \). Comparing polar forms, \( r^4 = 4 \), so \( r = \sqrt2 \) (the only positive real number with fourth power \( 4 \), since \( t \mapsto t^4 \) is strictly increasing on positive reals), and \( 4\theta = \pi + 2\pi j \), \( j \in \nZ \). The values \( j = 0, 1, 2, 3 \) give the four distinct roots
\[
\sqrt2 e^{i\pi/4} = 1 + i, \quad \sqrt2 e^{3i\pi/4} = -1 + i, \quad \sqrt2 e^{5i\pi/4} = -1 - i, \quad \sqrt2 e^{7i\pi/4} = 1 - i .
\]
By @thm-roots-with-multiplicity, four distinct roots of a degree-\( 4 \) monic polynomial each have multiplicity \( 1 \), and
\[
x^4 + 4 = (x - 1 - i)(x - 1 + i)(x + 1 - i)(x + 1 + i) \quad \text{in } \nC[x] .
\]
Pairing conjugates with \( (x - z)(x - \conj{z}) = x^2 - 2\operatorname{Re}(z)x + \lvert z \rvert^2 \), and \( \lvert 1 \pm i \rvert^2 = \lvert -1 \pm i \rvert^2 = 2 \),
\[
x^4 + 4 = (x^2 - 2x + 2)(x^2 + 2x + 2) \quad \text{in } \nR[x] .
\]
Check: \( (x^2 + 2)^2 - (2x)^2 = x^4 + 4x^2 + 4 - 4x^2 = x^4 + 4 \). Both quadratics have \( \beta^2 - 4\gamma = 4 - 8 < 0 \), so they have no real roots and are irreducible by @cor-real-irreducibles.
:::

:::: {#exr-fundamental-theorem-of-algebra-b2}
[B2: \( x^6 + 1 \)]

Find the factorization of \( x^6 + 1 \) into irreducible polynomials in \( \nR[x] \).
::::

::: {.solution}
The roots solve \( z^6 = -1 = e^{i\pi} \). As in B1, \( z = e^{i\theta} \) with \( 6\theta = \pi + 2\pi j \), and \( j = 0, \dots, 5 \) give six distinct roots at the angles \( 30^\circ, 90^\circ, 150^\circ, 210^\circ, 270^\circ, 330^\circ \):
\[
\tfrac{\sqrt3}{2} \pm \tfrac12 i, \qquad \pm i, \qquad -\tfrac{\sqrt3}{2} \pm \tfrac12 i .
\]
Each has multiplicity \( 1 \) by @thm-roots-with-multiplicity, and none is real. They form three conjugate pairs, each of modulus \( 1 \), with real parts \( \tfrac{\sqrt3}{2} \), \( 0 \), \( -\tfrac{\sqrt3}{2} \). Pairing them as in @exm-factor-x4-plus-1,
\[
x^6 + 1 = (x^2 + 1)\bigl(x^2 - \sqrt3\,x + 1\bigr)\bigl(x^2 + \sqrt3\,x + 1\bigr) .
\]
Check: \( (x^2 - \sqrt3x + 1)(x^2 + \sqrt3x + 1) = (x^2 + 1)^2 - 3x^2 = x^4 - x^2 + 1 \), and \( (x^2 + 1)(x^4 - x^2 + 1) = x^6 + 1 \). Each quadratic factor has only non-real roots, so it is irreducible over \( \nR \) by @cor-real-irreducibles. By the uniqueness in @cor-real-factorization, this is the factorization.
:::

:::: {#exr-fundamental-theorem-of-algebra-b3}
[B3: Real cubics]

Let \( f \in \nR[x] \) have degree \( 3 \), and suppose the multiplicities of the real roots of \( f \) add up to \( 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( f = a(x - c)(x - z)(x - \conj{z}) \) for some \( a, c \in \nR \) and some \( z \in \nC \setminus \nR \), and that \( z \) and \( \conj{z} \) are simple roots.
2. Show that the hypothesis cannot be weakened to "\( f \) has exactly one real root" by considering \( (x - 1)^3 \).
:::
::::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. By @cor-real-factorization, \( f = a(x - c_1)\cdots(x - c_r)\,q_1\cdots q_s \) with \( r + 2s = 3 \) and \( r \) equal to the sum of the real multiplicities, which is \( 1 \). So \( r = 1 \), \( s = 1 \), and \( f = a(x - c)q \) with \( c \in \nR \) and \( q \) a monic real quadratic without real roots. By @thm-fundamental-theorem-of-algebra, \( q \) has a root \( z \in \nC \), which is not real. By @thm-real-roots-conjugate-pairs, \( \conj{z} \neq z \) is also a root of \( q \). The two multiplicities in \( q \) are each at least \( 1 \) and add up to at most \( 2 \) (@thm-roots-with-multiplicity), so they equal \( 1 \) and \( q = (x - z)(x - \conj{z}) \), the leading coefficient being \( 1 \). Finally, by @thm-multiplicity-of-product, \( \operatorname{mult}_z(f) = \operatorname{mult}_z(a(x - c)) + \operatorname{mult}_z(q) = 0 + 1 = 1 \), since \( a(z - c) \neq 0 \); similarly for \( \conj{z} \).
2. \( (x - 1)^3 \) has exactly one real root, \( 1 \), but no non-real roots at all: it already splits over \( \nR \). Here the real multiplicities add up to \( 3 \), not \( 1 \).
:::
:::

:::: {#exr-fundamental-theorem-of-algebra-b4}
[B4: Running the proof on an example]

Let \( p = x^4 - x^2 + 2 \in \nC[x] \).

::: {.enumerate options="label=(\alph*)"}
1. Compute the radius \( R \) of @lem-polynomial-growth for \( p \).
2. Follow the proof of @lem-dalembert at \( z_0 = 0 \): find \( k \), \( B \), \( u \) and \( t \), and verify that \( \lvert p(tu) \rvert < \lvert p(0) \rvert \).
3. Compute \( p(i/2) \), and explain why the direction \( i \) does not work here, although it did in @exm-dalembert-step.
:::
::::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Here \( a_4 = 1 \) and \( A = \lvert 2 \rvert + \lvert 0 \rvert + \lvert -1 \rvert + \lvert 0 \rvert = 3 \), so \( R = \max\{1, 6\} = 6 \). Hence \( \lvert p(z) \rvert \ge \tfrac12\lvert z \rvert^4 \) for \( \lvert z \rvert \ge 6 \).
2. At \( z_0 = 0 \) the coefficients are \( b_0 = 2 \), \( b_1 = 0 \), \( b_2 = -1 \), \( b_3 = 0 \), \( b_4 = 1 \). So \( k = 2 \) and \( B = \lvert b_3 \rvert + \lvert b_4 \rvert = 1 \). Then \( w = -b_0/b_2 = 2 = 2e^{i \cdot 0} \), so \( \alpha = 0 \) and \( u = 1 \). Next \( t = \min\{1, \ 2/1, \ 1/2\} = \tfrac12 \). So \( z = \tfrac12 \), and \( p(\tfrac12) = \tfrac1{16} - \tfrac14 + 2 = \tfrac{29}{16} < 2 = \lvert p(0) \rvert \). The proof guarantees at most \( 2 - \tfrac12 \cdot \tfrac14 \cdot 1 = \tfrac{15}{8} = \tfrac{30}{16} \), consistent with \( \tfrac{29}{16} \).
3. \( p(i/2) = \tfrac1{16} + \tfrac14 + 2 = \tfrac{37}{16} > 2 \). The right direction depends on the sign of \( b_k \) relative to \( b_0 \): we need \( b_2u^2 \) to point from \( b_0 \) toward \( 0 \), that is, \( b_2u^2 \) a negative multiple of \( b_0 = 2 \). With \( b_2 = -1 \) this means \( u^2 > 0 \), so \( u = \pm1 \); for \( u = i \), \( b_2u^2 = 1 \) points away from \( 0 \). In @exm-dalembert-step, \( b_2 = +1 \) and \( u = i \) was the right choice.
:::
:::

### C. Going deeper

:::: {#exr-fundamental-theorem-of-algebra-c1}
[C1: Fields where the theorem fails]

Call a field \( F \) **algebraically closed** if every non-constant polynomial in \( F[x] \) has a root in \( F \).

::: {.enumerate options="label=(\alph*)"}
1. Let \( p \) be a prime. Show that \( x^p - x + 1 \) has no root in \( \nF_p \). More generally, show that no finite field is algebraically closed.
2. Give explicit witnesses that \( \nR \) and \( \nQ \) are not algebraically closed.
3. For your witness over \( \nR \), explain which step of the proof of the Fundamental Theorem of Algebra (@thm-fundamental-theorem-of-algebra) breaks.
4. For \( f = x^2 - 2 \) over \( \nQ \), prove that \( r \mapsto \lvert f(r) \rvert \) has **no** minimum on \( \nQ \). Which step of the proof breaks now?
:::

*Hint for (d): if \( r_0 \) were a minimum point with \( r_0^2 > \tfrac25 \), compare \( r_0 \) with \( r_1 = \dfrac{r_0^2 + 2}{2r_0} \).*
::::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. By @exr-polynomials-c2 (c), \( a^p - a = 0 \) for every \( a \in \nF_p \), so \( a^p - a + 1 = 1 \neq 0 \). For a finite field \( F = \{c_1, \dots, c_q\} \), let \( g = (x - c_1)\cdots(x - c_q) + 1 \). It has degree \( q \ge 2 \) (@thm-degree-of-product), and \( g(c_i) = 0 + 1 = 1 \neq 0 \) for every \( i \) by @thm-evaluation-respects-operations. So \( g \) is a non-constant polynomial without a root in \( F \).
2. Over \( \nR \), \( x^2 + 1 \) has no root, since \( c^2 + 1 \ge 1 \). Over \( \nQ \), \( x^2 - 2 \) has no root, since \( \sqrt2 \) is irrational (@thm-sqrt2-irrational) and the only real roots are \( \pm\sqrt2 \).
3. For \( x^2 + 1 \) over \( \nR \), growth holds, and \( c \mapsto \lvert c^2 + 1 \rvert \) attains its minimum \( 1 \) at \( c = 0 \). The step that breaks is d'Alembert's lemma (@lem-dalembert): at \( z_0 = 0 \) we have \( b_0 = 1 \), \( k = 2 \), \( b_2 = 1 \), and we need \( u \) with \( u^2 = -1 \), which does not exist in \( \nR \).
4. Suppose \( r_0 \in \nQ \) satisfies \( \lvert r_0^2 - 2 \rvert \le \lvert r^2 - 2 \rvert \) for every \( r \in \nQ \). Put \( m = \lvert r_0^2 - 2 \rvert \); then \( m > 0 \) by (b).

   *Case 1: \( r_0^2 \le \tfrac25 \).* Then \( m = 2 - r_0^2 \ge \tfrac85 > 1 = \lvert 1^2 - 2 \rvert \), contradicting minimality at \( r = 1 \).

   *Case 2: \( r_0^2 > \tfrac25 \).* Then \( r_0 \neq 0 \), and \( r_1 = (r_0^2 + 2)/(2r_0) \in \nQ \). Expanding,
   \[
   r_1^2 - 2 = \frac{(r_0^2 + 2)^2 - 8r_0^2}{4r_0^2} = \frac{(r_0^2 - 2)^2}{4r_0^2}, \qquad \text{so} \qquad \lvert r_1^2 - 2 \rvert = m \cdot \frac{m}{4r_0^2} .
   \]
   We claim \( m < 4r_0^2 \). If \( r_0^2 \ge 2 \), then \( m = r_0^2 - 2 < 4r_0^2 \). If \( \tfrac25 < r_0^2 < 2 \), then \( m = 2 - r_0^2 < \tfrac85 < 4r_0^2 \). Hence \( \lvert r_1^2 - 2 \rvert < m \), contradicting minimality.

   So there is no minimum. The step of the proof that breaks is @lem-minimum-modulus-attained, which rests on the extreme value theorem (A2). That fact is about the completeness of \( \nR \), and \( \nQ \) is not complete: the values \( \lvert r^2 - 2 \rvert \) get arbitrarily close to \( 0 \) without reaching it.
:::
:::

:::: {#exr-fundamental-theorem-of-algebra-c2}
[C2: Sums of two squares]

Let \( f \in \nR[x] \) be monic with **no** real root.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \deg f \) is even and that \( f(c) > 0 \) for every \( c \in \nR \).
2. Prove that \( f = g^2 + h^2 \) for some \( g, h \in \nR[x] \).
:::

*Hint for (b): each irreducible factor of \( f \) is \( (x - z)(x - \conj{z}) \). Collect one root from each pair into a complex polynomial \( G \), and split \( G \) into real and imaginary parts.*
::::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. By @cor-real-factorization, \( f = (x - c_1)\cdots(x - c_r)\,q_1\cdots q_s \), with leading coefficient \( 1 \) since \( f \) is monic. A factor \( x - c_1 \) would give the real root \( c_1 \), so \( r = 0 \) and \( \deg f = 2s \) is even. (If \( s = 0 \), then \( f = 1 \) and the claims hold.) Each \( q_j = x^2 + \beta x + \gamma \) has no real root, so by the remark after @cor-real-irreducibles, \( \beta^2 < 4\gamma \). For real \( c \),
   \[
   q_j(c) = \Bigl(c + \frac{\beta}{2}\Bigr)^2 + \frac{4\gamma - \beta^2}{4} > 0 .
   \]
   By @thm-evaluation-respects-operations, \( f(c) = q_1(c)\cdots q_s(c) \) is a product of positive reals, so \( f(c) > 0 \).
2. For each \( j \), \( q_j \) is non-constant, so by @thm-fundamental-theorem-of-algebra it has a root \( z_j \in \nC \), not real. As in @exr-fundamental-theorem-of-algebra-b3 (a), \( q_j = (x - z_j)(x - \conj{z_j}) \). Let \( G = (x - z_1)\cdots(x - z_s) \in \nC[x] \). By the product rule for conjugate polynomials proved in @thm-real-roots-conjugate-pairs, \( \conj{G} = (x - \conj{z_1})\cdots(x - \conj{z_s}) \), so \( f = G\,\conj{G} \) (commutativity, @thm-polynomial-ring-laws).

   Write each coefficient of \( G \) as \( \alpha_k + i\beta_k \) with \( \alpha_k, \beta_k \in \nR \), and put \( g = \sum_k \alpha_kx^k \) and \( h = \sum_k \beta_kx^k \) in \( \nR[x] \). Then \( G = g + ih \) and \( \conj{G} = g - ih \), so
   \[
   f = (g + ih)(g - ih) = g^2 - i^2h^2 + (ihg - igh) = g^2 + h^2 .
   \]
   For example, for \( x^4 + 1 \) take \( z_1 = e^{i\pi/4} \) and \( z_2 = e^{3i\pi/4} \) from @exm-factor-x4-plus-1. Then \( z_1 + z_2 = i\sqrt2 \) and \( z_1z_2 = e^{i\pi} = -1 \), so \( G = x^2 - i\sqrt2\,x - 1 \), \( g = x^2 - 1 \), \( h = -\sqrt2\,x \), and \( x^4 + 1 = (x^2 - 1)^2 + 2x^2 \).
:::
:::
