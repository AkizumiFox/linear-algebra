# Functions of Matrices, the Exponential and Linear Differential Equations

We have known since Chapter 3 what \( p(\A) \) means for a polynomial \( p \). This section gives a meaning to \( f(\A) \) for a much larger class of functions — square roots, logarithms, sines, and above all \( e^{\A} \) — and the Jordan form is what makes it possible. The definition needs a well-definedness proof, which turns out to be Hermite interpolation from Chapter 5: whatever \( f \) is, \( f(\A) \) is really \( p(\A) \) for a polynomial \( p \) that agrees with \( f \) to the right order at each eigenvalue. With \( e^{t\A} \) in hand, every linear system of differential equations with constant coefficients is solved in one formula.

Throughout this section \( F = \nC \) (or \( \nR \), when we say so), so that every characteristic polynomial splits (@cor-complex-polynomial-splits) and Jordan forms exist.

## What a polynomial does to a Jordan block

Start with what we already have. A Jordan block is a scalar plus a nilpotent matrix whose powers stop, and a polynomial applied to it can be read off from a Taylor expansion.

::: {#lem-polynomial-of-jordan-block}
[A Polynomial of a Jordan Block]

Let \( F \) have characteristic \( 0 \), let \( k \ge 1 \), \( \lambda \in F \) and \( p \in F[x] \). Then \( p(\J_k(\lambda)) \) is the upper triangular matrix whose \( (r, r+j) \)-entry is
\[
\bigl(p(\J_k(\lambda))\bigr)_{r, r+j} = \frac{p^{(j)}(\lambda)}{j!} \qquad (0 \le j \le k - 1, \ 1 \le r \le k - j),
\]
with all entries below the diagonal equal to \( 0 \). In particular the value \( p(\lambda) \) fills the diagonal, \( p'(\lambda) \) the superdiagonal, and only the first \( k \) derivatives of \( p \) at \( \lambda \) are involved.
:::

::: {.proof}
Write \( \J = \J_k(\lambda) = \lambda \I_k + \M \) with \( \M = \J_k(0) \) (@def-jordan-block). Reading off the columns of \( \M \), we have \( \M\e_1 = \0 \) and \( \M\e_r = \e_{r-1} \) for \( r \ge 2 \), so by induction \( \M^{j}\e_r = \e_{r-j} \) when \( r > j \) and \( \M^{j}\e_r = \0 \) when \( r \le j \). Hence, for \( 0 \le j \le k-1 \), the matrix \( \M^{j} \) has \( 1 \) in each position \( (r, r+j) \) and \( 0 \) elsewhere, and \( \M^{k} = 0 \). Let \( d = \deg p \). By @thm-polynomial-taylor (b), applied with \( c = \lambda \) and \( n = d \),
\[
p(x) = \sum_{j=0}^{d} \frac{p^{(j)}(\lambda)}{j!}\,(x - \lambda)^{j} .
\]
Substituting \( \J \) for \( x \) — legitimate because evaluation at \( \J \) is a ring homomorphism (@thm-evaluation-homomorphism) — and using \( \J - \lambda \I_k = \M \),
\[
p(\J) = \sum_{j=0}^{d} \frac{p^{(j)}(\lambda)}{j!}\,\M^{j} = \sum_{j=0}^{\min(d,\,k-1)} \frac{p^{(j)}(\lambda)}{j!}\,\M^{j},
\]
since \( \M^{j} = 0 \) for \( j \ge k \). Each \( \M^{j} \) contributes its coefficient to every position \( (r, r+j) \) and to no other position, which is the claim.
:::

For \( p = x^{m} \) this reads \( p^{(j)}(\lambda)/j! = \binom{m}{j}\lambda^{m-j} \), so
\[
\bigl(\J_k(\lambda)^{m}\bigr)_{r,\,r+j} = \binom{m}{j}\lambda^{\,m-j} ,
\]
which is the formula behind everything that follows, here and in the next section.

## Functions of a matrix

Reading @lem-polynomial-of-jordan-block backwards suggests the definition. The formula for \( p(\J_k(\lambda)) \) uses nothing about \( p \) except the numbers \( p(\lambda), p'(\lambda), \dots, p^{(k-1)}(\lambda) \). Any function that has those derivatives can be inserted instead.

*To apply \( f \) to a matrix, apply it to each Jordan block, putting \( f^{(j)}(\lambda)/j! \) on the \( j \)-th superdiagonal.*

::: {#def-matrix-function-jordan}
[Function of a Matrix]

Let \( \A \in M_n(\nC) \) with Jordan form \( \J = \J_{k_1}(\lambda_1) \oplus \dots \oplus \J_{k_m}(\lambda_m) \) and \( \A = \P \J \P^{-1} \). Let \( f \) be a complex-valued function that is defined and **at least \( k_i - 1 \) times differentiable at \( \lambda_i \)** for every \( i \) — for instance, a function given by a convergent power series on a disc around each eigenvalue. Define
\[
f\bigl(\J_k(\lambda)\bigr) \coloneqq \begin{pmatrix}
f(\lambda) & f'(\lambda) & \tfrac{f''(\lambda)}{2!} & \cdots & \tfrac{f^{(k-1)}(\lambda)}{(k-1)!} \\
& f(\lambda) & f'(\lambda) & \ddots & \vdots \\
& & \ddots & \ddots & \tfrac{f''(\lambda)}{2!} \\
& & & f(\lambda) & f'(\lambda) \\
& & & & f(\lambda)
\end{pmatrix} \in M_k(\nC),
\]
the upper triangular matrix with \( f^{(j)}(\lambda)/j! \) in every position \( (r, r+j) \), and
\[
f(\A) \coloneqq \P\,\Bigl( f\bigl(\J_{k_1}(\lambda_1)\bigr) \oplus \dots \oplus f\bigl(\J_{k_m}(\lambda_m)\bigr) \Bigr)\,\P^{-1} .
\]
:::

In words: the diagonal of \( f(\J) \) records the values \( f(\lambda_i) \), and each further superdiagonal records the next derivative, divided by a factorial. For a diagonalizable \( \A \) every block has size \( 1 \), no derivatives are needed, and the definition says the familiar thing: \( f(\A) = \P\diag(f(\lambda_1), \dots, f(\lambda_n))\P^{-1} \).

**Well-definedness.** Two choices were made: the invertible \( \P \) and the order of the blocks. The Jordan form itself is unique only up to the order of the blocks (@thm-jordan-canonical-form), and even for a fixed \( \J \) there are many \( \P \) with \( \A = \P \J \P^{-1} \). The next theorem removes both worries at once, by identifying \( f(\A) \) with \( p(\A) \) for a suitable **polynomial** \( p \), an expression in which no choice appears.

::: {#thm-matrix-function-hermite}
[Functions of a Matrix Are Polynomials in It]

Let \( \A \in M_n(\nC) \) with distinct eigenvalues \( \mu_1, \dots, \mu_d \), and write
\[
m_{\A} = (x - \mu_1)^{s_1}\cdots(x - \mu_d)^{s_d},
\]
so that \( s_l \) is the largest size of a \( \mu_l \)-block of the Jordan form of \( \A \) (@cor-jordan-invariants (c)). Let \( f \) be as in @def-matrix-function-jordan. Then:

::: {.enumerate options="label=(\alph*)"}
1. there is a polynomial \( p \in \nC[x] \) with \( \deg p < \deg m_{\A} \) and
   \[
   p^{(j)}(\mu_l) = f^{(j)}(\mu_l) \qquad \text{for all } l = 1, \dots, d \text{ and } j = 0, \dots, s_l - 1 ,
   \]
   and \( p \) is the **only** such polynomial of degree less than \( \deg m_{\A} \);
2. for **every** polynomial \( q \in \nC[x] \) satisfying those \( \deg m_{\A} \) equations, \( q(\A) = p(\A) \);
3. \( f(\A) = p(\A) \). In particular \( f(\A) \) does not depend on the choice of \( \P \) or on the order of the blocks, and \( f(\A) \) is determined by the finitely many numbers \( f^{(j)}(\mu_l) \).
:::

The polynomial \( p \) of (a) is the **Hermite interpolating polynomial** of \( f \) on the spectrum of \( \A \).
:::

::: {.idea}
The list of conditions "match \( f \) and its first \( s_l - 1 \) derivatives at \( \mu_l \)" is exactly a congruence modulo \( (x - \mu_l)^{s_l} \), by the Taylor expansion; and the moduli \( (x-\mu_l)^{s_l} \) are pairwise coprime. So the Chinese Remainder Theorem produces \( p \) and shows it is unique below the degree of the product \( m_{\A} \) — this is @exm-hermite-via-crt with more nodes and higher orders. Once \( p \) exists, @lem-polynomial-of-jordan-block says that \( p \) and \( f \) do the same thing to every Jordan block of \( \A \), because a \( \mu_l \)-block has size at most \( s_l \) and only derivatives up to order \( s_l - 1 \) are consulted.
:::

::: {.proof}
(a) For each \( l \) let \( r_l \coloneqq \sum_{j=0}^{s_l-1}\frac{f^{(j)}(\mu_l)}{j!}(x - \mu_l)^{j} \in \nC[x] \). For \( g \in \nC[x] \), the Taylor expansion of @thm-polynomial-taylor (b) at \( \mu_l \), together with the uniqueness of the remainder on division by \( (x - \mu_l)^{s_l} \) (@thm-polynomial-division), gives
\[
g \equiv r_l \pmod{(x - \mu_l)^{s_l}} \qquad \Longleftrightarrow \qquad g^{(j)}(\mu_l) = f^{(j)}(\mu_l) \text{ for } j = 0, \dots, s_l - 1 ,
\]
exactly as in @exm-hermite-via-crt (a) for \( s_l = 2 \): the remainder of \( g \) on division by \( (x-\mu_l)^{s_l} \) is \( \sum_{j<s_l}\frac{g^{(j)}(\mu_l)}{j!}(x-\mu_l)^{j} \), and two polynomials of degree less than \( s_l \) are equal precisely when their coefficients in the basis \( \bigl(1, x - \mu_l, \dots, (x-\mu_l)^{s_l-1}\bigr) \) agree (@thm-polynomial-taylor (a)).

The moduli \( (x - \mu_1)^{s_1}, \dots, (x-\mu_d)^{s_d} \) are pairwise coprime: for \( l \ne l' \), any common divisor divides both, and a monic common divisor would be a power of \( x - \mu_l \) and a power of \( x - \mu_{l'} \) with \( \mu_l \ne \mu_{l'} \), hence \( 1 \) (@lem-monic-divisors, @thm-unique-factorization-polynomials). Their product is \( m_{\A} \). So @thm-crt-polynomials (c) provides exactly one \( p \) with \( \deg p < \deg m_{\A} \) and \( p \equiv r_l \pmod{(x-\mu_l)^{s_l}} \) for every \( l \), which by the displayed equivalence is (a).

(b) Let \( q \) satisfy the same equations. By the equivalence again, \( q \equiv r_l \equiv p \pmod{(x-\mu_l)^{s_l}} \) for every \( l \), so @thm-crt-polynomials (b) gives \( m_{\A} \mid q - p \). Writing \( q - p = m_{\A}h \) and evaluating at \( \A \), \( q(\A) - p(\A) = m_{\A}(\A)h(\A) = 0 \) since \( m_{\A}(\A) = 0 \) (@def-minimal-polynomial). Hence \( q(\A) = p(\A) \).

(c) Let \( \J = \J_{k_1}(\lambda_1) \oplus \dots \oplus \J_{k_m}(\lambda_m) \) be any Jordan form of \( \A \) and \( \A = \P \J \P^{-1} \). Fix \( i \) and let \( l \) be the index with \( \lambda_i = \mu_l \). By @cor-jordan-invariants (c), \( k_i \le s_l \), so @lem-polynomial-of-jordan-block and the equations in (a) give
\[
\bigl(p(\J_{k_i}(\lambda_i))\bigr)_{r, r+j} = \frac{p^{(j)}(\lambda_i)}{j!} = \frac{f^{(j)}(\lambda_i)}{j!} = \bigl(f(\J_{k_i}(\lambda_i))\bigr)_{r,r+j} \qquad (0 \le j \le k_i - 1),
\]
the derivatives involved having order at most \( k_i - 1 \le s_l - 1 \). So \( p(\J_{k_i}(\lambda_i)) = f(\J_{k_i}(\lambda_i)) \) for every \( i \). Since evaluating a polynomial blockwise gives the polynomial of the block diagonal matrix (@thm-block-diagonal-arithmetic (a), (b)),
\[
\begin{aligned}
p(\A) = p(\P \J \P^{-1})
  &= \P\,p(\J)\,\P^{-1}
   = \P\Bigl(\bigoplus_i p\bigl(\J_{k_i}(\lambda_i)\bigr)\Bigr)\P^{-1} \\
  &= \P\Bigl(\bigoplus_i f\bigl(\J_{k_i}(\lambda_i)\bigr)\Bigr)\P^{-1} = f(\A),
\end{aligned}
\]
the second equality by @prp-similarity-invariants (c). The left-hand side mentions neither \( \P \) nor the order of the blocks, so neither does the right-hand side. This proves the theorem.
:::

So the definition is consistent with the old one: if \( f \) happens to be a polynomial, then \( f \) itself satisfies the interpolation conditions, and (b) gives \( f(\A) \) in the new sense \( = f(\A) \) in the old sense.

::: {.warning}
**\( f(\A) \) is not \( f \) applied to the entries of \( \A \).** Even for \( f(x) = x^2 \) this fails: with \( \A = \begin{pmatrix} 1 & 1 \\ 0 & 1\end{pmatrix} \), squaring each entry gives \( \begin{pmatrix} 1 & 1 \\ 0 & 1\end{pmatrix} \), while \( \A^2 = \begin{pmatrix} 1 & 2 \\ 0 & 1\end{pmatrix} \). The definition is designed so that \( f(\A) \) is a polynomial in \( \A \), and entrywise application is not.
:::

::: {#exm-matrix-square-root}
[Square Roots of Two Matrices]

Using @def-matrix-function-jordan with \( f(x) = \sqrt{x} \), the branch with \( \sqrt{4} = 2 \) and \( \sqrt{9} = 3 \), compute a square root of

::: {.enumerate options="label=(\alph*)"}
1. \( \A = \begin{pmatrix} 5 & 4 \\ 4 & 5 \end{pmatrix} \);
2. \( \B = \begin{pmatrix} 4 & 1 \\ 0 & 4 \end{pmatrix} \).
:::
:::

::: {.solution}
(a) \( p_{\A} = (x-5)^2 - 16 = x^2 - 10x + 9 = (x-1)(x-9) \), so the eigenvalues are \( 1 \) and \( 9 \), distinct, and \( \A \) is diagonalizable. Solving \( (\A - \I)\x = \0 \) gives \( \Span((1,-1)) \) and \( (\A - 9\I)\x = \0 \) gives \( \Span((1,1)) \). With \( \P = \begin{pmatrix} 1 & 1 \\ -1 & 1\end{pmatrix} \), \( \det \P = 2 \) and \( \P^{-1} = \tfrac12\begin{pmatrix} 1 & -1 \\ 1 & 1\end{pmatrix} \), we have \( \P^{-1}\A \P = \diag(1,9) \) and
\[
f(\A) = \P\diag(1, 3)\P^{-1} = \tfrac12\begin{pmatrix} 1 & 3 \\ -1 & 3\end{pmatrix}\begin{pmatrix} 1 & -1 \\ 1 & 1\end{pmatrix} = \tfrac12\begin{pmatrix} 4 & 2 \\ 2 & 4\end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 2\end{pmatrix}.
\]
*Check.* \( \begin{pmatrix} 2 & 1 \\ 1 & 2\end{pmatrix}^2 = \begin{pmatrix} 5 & 4 \\ 4 & 5\end{pmatrix} = \A \).

(b) \( \B = \J_2(4) \) is its own Jordan form, with \( \P = \I \). Here \( f(4) = 2 \) and \( f'(x) = \tfrac{1}{2\sqrt x} \), so \( f'(4) = \tfrac14 \), and @def-matrix-function-jordan gives
\[
f(\B) = \begin{pmatrix} 2 & \tfrac14 \\ 0 & 2\end{pmatrix}.
\]
*Check.* \( \begin{pmatrix} 2 & 1/4 \\ 0 & 2\end{pmatrix}^2 = \begin{pmatrix} 4 & 2\cdot\tfrac14 + \tfrac14\cdot 2 \\ 0 & 4\end{pmatrix} = \begin{pmatrix} 4 & 1 \\ 0 & 4\end{pmatrix} = \B \).

*The Hermite polynomial.* For (b), \( m_{\B} = (x-4)^2 \), and the interpolating polynomial of degree \( < 2 \) with \( p(4) = 2 \), \( p'(4) = \tfrac14 \) is \( p = 2 + \tfrac14(x - 4) = \tfrac14x + 1 \). Indeed \( p(\B) = \tfrac14\B + \I = \begin{pmatrix} 2 & 1/4 \\ 0 & 2\end{pmatrix} \), as @thm-matrix-function-hermite (c) predicts.
:::

::: {.check}
A matrix \( \A \in M_5(\nC) \) has Jordan form \( \J_3(2) \oplus \J_1(2) \oplus \J_1(7) \). Which values of \( f \) and its derivatives does \( f(\A) \) depend on?
:::

::: {.solution}
On \( f(2), f'(2), f''(2) \) and \( f(7) \): four numbers. Indeed \( m_{\A} = (x-2)^3(x-7) \) by @cor-jordan-invariants (c), so \( s_1 = 3 \) for \( \mu_1 = 2 \) and \( s_2 = 1 \) for \( \mu_2 = 7 \), and @thm-matrix-function-hermite lists the derivatives of order \( 0, 1, 2 \) at \( 2 \) and order \( 0 \) at \( 7 \). Note \( \deg m_{\A} = 4 \), matching the number of conditions and the degree bound on the interpolating polynomial. Nothing about \( f \) away from \( \{2, 7\} \) matters, and no third derivative is consulted even though \( \dim = 5 \).
:::

## The matrix exponential

The most important function of a matrix is the exponential, and it has a second description, as the sum of a series. We check that the series converges, and that its sum is the matrix \( \exp(\A) \) that @def-matrix-function-jordan produces. Convergence is meant **entrywise**, as in Chapter 8: a sequence \( \M_1, \M_2, \dots \) in \( M_n(\nC) \) converges to \( \M \) if for each position \( (r,s) \) the number sequence \( (\M_m)_{rs} \) converges to \( \M_{rs} \), and a series of matrices converges if its sequence of partial sums does. No notion of length of a matrix is used anywhere in this section.

::: {.remark}
**What we assume from analysis.** Everything below uses exactly the following facts about real and complex numbers, and nothing else. Chapter 15 will develop the tools that make such statements routine; here they are quoted.

::: {.enumerate options="label=(A\arabic*)"}
1. **The scalar exponential.** For every \( z \in \nC \) the series \( \sum_{i \ge 0} z^{i}/i! \) converges; its sum is written \( e^{z} \). It satisfies \( e^{z+w} = e^{z}e^{w} \), \( e^{0} = 1 \), and \( e^{\,i\theta} = \cos\theta + i\sin\theta \) for real \( \theta \). For real \( s \ge 0 \), \( e^{s} \ge 1 \).
2. **Termwise differentiation.** If a power series \( \sum_{m \ge 0}c_mt^{m} \) with \( c_m \in \nC \) converges for **every** real \( t \), then the function \( t \mapsto \sum_m c_mt^{m} \) is differentiable on \( \nR \) with derivative \( \sum_{m \ge 1}mc_mt^{m-1} \).
3. **Limits and products.** Limits of convergent sequences of complex numbers respect sums, scalar multiples and products. The derivative of a product of two differentiable functions \( \nR \to \nC \) obeys the product rule, and differentiation is linear.
4. **Zero derivative.** A differentiable function \( \nR \to \nC \) whose derivative vanishes everywhere is constant.
5. **Decay.** For every integer \( j \ge 0 \) and every real \( c < 0 \), \( t^{j}e^{ct} \to 0 \) as \( t \to \infty \).
:::

Fact (A5) is used only in the last exercise of this section. Nothing else about \( \exp \), \( \cos \) or \( \sin \) is assumed: the derivative \( \frac{d}{dt}e^{zt} = z\,e^{zt} \) for \( z \in \nC \) is the \( 1 \times 1 \) case of @thm-exponential-properties (b) below, proved from (A2), and the derivatives of \( \cos \) and \( \sin \) used in the examples follow from it through Euler's formula in (A1).
:::

::: {#def-matrix-exponential}
[Matrix Exponential]

Let \( \A \in M_n(\nC) \). The **matrix exponential** of \( \A \) is
\[
e^{\A} \coloneqq \sum_{m=0}^{\infty}\frac{\A^{m}}{m!} = \lim_{\M \to \infty}\ \sum_{m=0}^{\M}\frac{\A^{m}}{m!},
\]
the limit taken entrywise, provided it exists; \( \A^{0} = \I \).
:::

That the limit does exist, and what it is, is the content of the next theorem. The Jordan form reduces the question to a single block, where the series can be summed exactly.

::: {#thm-exponential-series-converges}
[The Exponential Series Converges to the Jordan Definition]

Let \( \A \in M_n(\nC) \). Then the series \( \sum_m \A^{m}/m! \) converges entrywise, and its sum is the matrix \( \exp(\A) \) given by @def-matrix-function-jordan for the function \( f = \exp \). In particular, for a single Jordan block,
\[
e^{\J_k(\lambda)} = e^{\lambda}\begin{pmatrix} 1 & 1 & \tfrac{1}{2!} & \cdots & \tfrac{1}{(k-1)!} \\ & 1 & 1 & \ddots & \vdots \\ & & \ddots & \ddots & \tfrac{1}{2!} \\ & & & 1 & 1 \\ & & & & 1\end{pmatrix},
\]
the upper triangular matrix with \( e^{\lambda}/j! \) in every position \( (r, r+j) \).
:::

::: {.idea}
For one block the entries of the partial sums are themselves partial sums of a scalar series, and that series can be recognized: the terms \( \binom{m}{j}\lambda^{m-j}/m! \) simplify to \( \lambda^{m-j}/(j!\,(m-j)!) \), which is \( 1/j! \) times the \( (m-j) \)-th term of the series for \( e^{\lambda} \). For general \( \A \), conjugation by a fixed \( \P \) turns each entry of a partial sum into a fixed finite linear combination of entries of the block partial sums, and limits pass through finite linear combinations.
:::

::: {.proof}
**Step 1. One block.** Fix \( k \ge 1 \), \( \lambda \in \nC \) and a position \( (r, r+j) \) with \( 0 \le j \le k-1 \). By @lem-polynomial-of-jordan-block applied to \( p = x^{m} \),
\[
\Bigl(\frac{\J_k(\lambda)^{m}}{m!}\Bigr)_{r,\,r+j} = \frac{1}{m!}\binom{m}{j}\lambda^{\,m-j} = \begin{cases} \dfrac{\lambda^{\,m-j}}{j!\,(m-j)!}, & m \ge j, \\ 0, & m < j, \end{cases}
\]
using \( \binom{m}{j}/m! = 1/(j!\,(m-j)!) \) for \( m \ge j \) and \( \binom{m}{j} = 0 \) for \( m < j \). Hence the partial sums satisfy
\[
\sum_{m=0}^{\M}\Bigl(\frac{\J_k(\lambda)^{m}}{m!}\Bigr)_{r,\,r+j} = \frac{1}{j!}\sum_{i=0}^{\M-j}\frac{\lambda^{i}}{i!} \qquad (\M \ge j),
\]
after the substitution \( i = m - j \). By (A1) the right-hand side converges to \( e^{\lambda}/j! \) as \( \M \to \infty \). Entries with \( j < 0 \), that is entries below the diagonal, are \( 0 \) in every term. So the series converges entrywise and
\[
e^{\J_k(\lambda)} = \Bigl(\text{upper triangular with } \tfrac{e^{\lambda}}{j!} \text{ on the } j\text{-th superdiagonal}\Bigr) = \exp\bigl(\J_k(\lambda)\bigr),
\]
the last equality being @def-matrix-function-jordan for \( f = \exp \), whose derivatives are \( f^{(j)} = \exp \), so \( f^{(j)}(\lambda)/j! = e^{\lambda}/j! \).

**Step 2. A Jordan matrix.** If \( \J = \J_{k_1}(\lambda_1) \oplus \dots \oplus \J_{k_m}(\lambda_m) \), then \( \J^{m}/m! \) is the direct sum of the corresponding blocks (@thm-block-diagonal-arithmetic (b)), so each entry of a partial sum of \( \sum_m \J^{m}/m! \) is either identically \( 0 \) or an entry of a partial sum from one block. By Step 1 all of them converge, and \( e^{\J} = \bigoplus_i e^{\J_{k_i}(\lambda_i)} \).

**Step 3. General \( \A \).** By @thm-jordan-canonical-form there are a Jordan matrix \( \J \) and an invertible \( \P \) with \( \A = \P \J \P^{-1} \). Then \( \A^{m} = \P \J^{m}\P^{-1} \) (@prp-similarity-invariants (c)), so
\[
\sum_{m=0}^{\M}\frac{\A^{m}}{m!} = \P\Bigl(\sum_{m=0}^{\M}\frac{\J^{m}}{m!}\Bigr)\P^{-1} .
\]
Each entry of the left-hand side is a fixed finite linear combination — with coefficients built from the entries of \( \P \) and \( \P^{-1} \), independent of \( \M \) — of the entries of the middle partial sum. By Step 2 those entries converge, so by (A3) the left-hand side converges entrywise, with
\[
e^{\A} = \P\,e^{\J}\,\P^{-1} = \P\Bigl(\bigoplus_i e^{\J_{k_i}(\lambda_i)}\Bigr)\P^{-1} = \exp(\A),
\]
the last equality by @def-matrix-function-jordan. This proves the theorem.
:::

From now on we write \( e^{\A} \) for this matrix and use both descriptions freely. Note one consequence of @thm-matrix-function-hermite: \( e^{\A} \) is a **polynomial** in \( \A \), namely \( p(\A) \) for the Hermite interpolant of \( \exp \) on \( \spec(\A) \). Everything that commutes with \( \A \) therefore commutes with \( e^{\A} \).

::: {#thm-exponential-properties}
[Properties of the Matrix Exponential]

Let \( \A, \B \in M_n(\nC) \) and let \( \P \in M_n(\nC) \) be invertible.

::: {.enumerate options="label=(\alph*)"}
1. \( e^{0} = \I \) and \( e^{\P^{-1}\A \P} = \P^{-1}e^{\A}\P \).
2. The function \( \nR \to M_n(\nC) \), \( t \mapsto e^{t\A} \), is differentiable entrywise, with
   \[
   \frac{d}{dt}\,e^{t\A} = \A e^{t\A} = e^{t\A}\A .
   \]
3. \( e^{\A} \) is invertible, with \( (e^{\A})^{-1} = e^{-\A} \).
4. If \( \A \B = \B \A \), then \( e^{\A+\B} = e^{\A}e^{\B} \).
5. \( \det e^{\A} = e^{\tr \A} \).
:::
:::

::: {.idea}
Part (b) is termwise differentiation, entry by entry. Everything after it is the same two-line trick: to prove \( \X(t) = \Y(t) \) for two matrix functions, show that \( \Z(t) = e^{-t\C}\X(t) \) has derivative \( 0 \) for a suitable \( \C \), so \( \Z \) is constant and equals \( \Z(0) \). That is why (c) and (d) come after (b), even though the series would also give them. Part (e) is read off the Jordan form: \( e^{\J} \) is triangular with \( e^{\lambda_i} \) on the diagonal.
:::

::: {.proof}
(a) \( 0^{m} = 0 \) for \( m \ge 1 \) and \( 0^{0} = \I \), so the series is \( \I \). For the second claim, Step 3 of the previous proof applies verbatim with \( \J \) replaced by \( \P^{-1}\A \P \): the partial sums of \( \sum_m (\P^{-1}\A \P)^{m}/m! \) are \( \P^{-1}\bigl(\sum_m \A^{m}/m!\bigr)\P \), and (A3) lets the limit pass through.

(b) Fix a position \( (r,s) \). By @thm-exponential-series-converges the series \( \sum_m t^{m}(\A^{m})_{rs}/m! \) converges for every real \( t \), since \( (t\A)^{m} = t^{m}\A^{m} \). So (A2) applies with \( c_m = (\A^{m})_{rs}/m! \) and gives
\[
\begin{aligned}
\frac{d}{dt}\,\bigl(e^{t\A}\bigr)_{rs}
  &= \sum_{m \ge 1}\frac{m\,t^{m-1}}{m!}(\A^{m})_{rs}
   = \sum_{m \ge 1}\frac{t^{m-1}}{(m-1)!}\bigl(\A\cdot \A^{m-1}\bigr)_{rs} \\
  &= \Bigl(\A\sum_{l \ge 0}\frac{t^{l}\A^{l}}{l!}\Bigr)_{rs},
\end{aligned}
\]
where the last step moves the constant matrix \( \A \) outside the limit: each entry of \( \A\bigl(\sum_{l \le L}t^l\A^l/l!\bigr) \) is a fixed linear combination of entries of the partial sum, so (A3) applies. Hence \( \frac{d}{dt}e^{t\A} = \A e^{t\A} \). The same computation with \( \A^{m} = \A^{m-1}\A \) gives \( e^{t\A}\A \).

(c) Put \( \H(t) = e^{t\A}e^{-t\A} \) for \( t \in \nR \). Each entry of \( \H \) is a finite sum of products of differentiable functions, so by (A3) and (b),
\[
\H'(t) = \bigl(\A e^{t\A}\bigr)e^{-t\A} + e^{t\A}\bigl(-\A e^{-t\A}\bigr) = \A e^{t\A}e^{-t\A} - \A e^{t\A}e^{-t\A} = 0 ,
\]
where the second equality uses \( e^{t\A}\A = \A e^{t\A} \) from (b). By (A4) every entry of \( \H \) is constant, so \( \H(t) = \H(0) = e^{0}e^{0} = \I \) for all \( t \). At \( t = 1 \), \( e^{\A}e^{-\A} = \I \), and @thm-one-sided-inverse finishes it.

(d) Suppose \( \A \B = \B \A \). Then \( \B \) commutes with every partial sum of \( \sum_m t^{m}\A^{m}/m! \), so by (A3) it commutes with the limit: \( \B e^{t\A} = e^{t\A}\B \) for every \( t \). Put
\[
\G(t) = e^{-t(\A+\B)}e^{t\A}e^{t\B} .
\]
Differentiating entrywise with the product rule (A3) and (b),
\[
\G'(t) = -(\A+\B)e^{-t(\A+\B)}e^{t\A}e^{t\B} + e^{-t(\A+\B)}\A e^{t\A}e^{t\B} + e^{-t(\A+\B)}e^{t\A}\B e^{t\B} .
\]
In the third term replace \( e^{t\A}\B \) by \( \B e^{t\A} \); in the first, use \( (\A+\B)e^{-t(\A+\B)} = e^{-t(\A+\B)}(\A+\B) \) from (b). The three terms become
\[
e^{-t(\A+\B)}\bigl(-(\A+\B) + \A + \B\bigr)e^{t\A}e^{t\B} = 0 .
\]
By (A4), \( \G \) is constant, so \( \G(t) = \G(0) = \I \). Multiplying on the left by \( e^{t(\A+\B)} \) and using (c), \( e^{t\A}e^{t\B} = e^{t(\A+\B)} \); put \( t = 1 \).

(e) Write \( \A = \P \J \P^{-1} \) with \( \J = \bigoplus_i \J_{k_i}(\lambda_i) \) a Jordan matrix. By (a) and @thm-exponential-series-converges,
\[
\det e^{\A} = \det\bigl(\P e^{\J}\P^{-1}\bigr) = \det e^{\J}
\]
(@cor-det-similarity-invariant), and \( e^{\J} = \bigoplus_i e^{\J_{k_i}(\lambda_i)} \) is upper triangular with \( e^{\lambda_i} \) repeated \( k_i \) times along the diagonal. By @thm-det-triangular and (A1),
\[
\det e^{\J} = \prod_{i}\bigl(e^{\lambda_i}\bigr)^{k_i} = e^{\,\sum_i k_i\lambda_i} = e^{\tr \J} = e^{\tr \A},
\]
the last equality because similar matrices have equal traces (@thm-trace-similarity-invariant). This proves the theorem.
:::

Part (e) says something striking: \( \det e^{\A} \ne 0 \) always, which re-proves (c), and if \( \tr \A = 0 \) then \( e^{\A} \in \SL_n(\nC) \).

The following corollary is the formula actually used in computations. Note that \( t\J_k(\lambda) \) is **not** a Jordan block for \( k \ge 2 \) and \( t \ne 1 \), since its superdiagonal entries are \( t \); the commuting law does the work instead.

::: {#cor-exponential-of-jordan-block}
[Exponential of a Jordan Block, with a Parameter]

Let \( k \ge 1 \), \( \lambda \in \nC \) and \( t \in \nR \). Then \( e^{t\J_k(\lambda)} \) is the upper triangular matrix with
\[
\bigl(e^{t\J_k(\lambda)}\bigr)_{r,\,r+j} = \frac{t^{j}e^{\lambda t}}{j!} \qquad (0 \le j \le k-1)
\]
and zeros below the diagonal. Consequently, if \( \A = \P \J \P^{-1} \) with \( \J = \J_{k_1}(\lambda_1) \oplus \dots \oplus \J_{k_m}(\lambda_m) \), then
\[
e^{t\A} = \P\Bigl(e^{t\J_{k_1}(\lambda_1)} \oplus \dots \oplus e^{t\J_{k_m}(\lambda_m)}\Bigr)\P^{-1} .
\]
In particular, for a diagonal \( \D = \diag(d_1, \dots, d_n) \), \( e^{t\D} = \diag(e^{td_1}, \dots, e^{td_n}) \).
:::

::: {.proof}
Write \( t\J_k(\lambda) = (t\lambda)\I_k + t\M \) with \( \M = \J_k(0) \). The two summands commute, since \( \I_k \) commutes with everything, so @thm-exponential-properties (d) gives \( e^{t\J_k(\lambda)} = e^{(t\lambda)\I_k}e^{t\M} \). For the first factor, \( \bigl((t\lambda)\I_k\bigr)^{m} = (t\lambda)^{m}\I_k \), so the partial sums are \( \bigl(\sum_{m \le \M}(t\lambda)^{m}/m!\bigr)\I_k \) and \( e^{(t\lambda)\I_k} = e^{\lambda t}\I_k \) by (A1). For the second, \( \M^{j} = 0 \) for \( j \ge k \), so the series terminates:
\[
e^{t\M} = \sum_{j=0}^{k-1}\frac{t^{j}}{j!}\M^{j},
\]
and \( \M^{j} \) has \( 1 \) in each position \( (r, r+j) \), as computed in the proof of @lem-polynomial-of-jordan-block. Multiplying by the scalar \( e^{\lambda t} \) gives the entry formula. The second display follows from \( t\A = \P(t\J)\P^{-1} \) with @thm-exponential-properties (a) and @thm-block-diagonal-arithmetic (b), exactly as in Step 2 of the proof of @thm-exponential-series-converges. The diagonal case is the case in which every block has size \( 1 \).
:::

::: {.warning}
**\( e^{\A+\B} = e^{\A}e^{\B} \) fails when \( \A \) and \( \B \) do not commute.** Take
\[
\A = \begin{pmatrix} 0 & 1 \\ 0 & 0\end{pmatrix}, \qquad \B = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} .
\]
Both square to \( 0 \), so the series stop after two terms: \( e^{\A} = \I + \A = \begin{pmatrix} 1 & 1 \\ 0 & 1\end{pmatrix} \) and \( e^{\B} = \I + \B = \begin{pmatrix} 1 & 0 \\ 1 & 1\end{pmatrix} \). Then
\[
e^{\A}e^{\B} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \ne \begin{pmatrix} 1 & 1 \\ 1 & 2\end{pmatrix} = e^{\B}e^{\A} .
\]
Since \( \A + \B = \B + \A \), at most one of the two products can equal \( e^{\A+\B} \), so the identity must fail for one of the pairs \( (\A, \B) \), \( (\B, \A) \). (In fact it fails for both: \( (\A+\B)^2 = \I \), so \( e^{\A+\B} \) has all four entries non-zero and none of them equal to \( 2 \).) The moral: check \( \A \B = \B \A \) before splitting an exponential.
:::

## Linear systems of differential equations

A system of \( n \) linear differential equations with constant coefficients,
\[
x_1' = a_{11}x_1 + \dots + a_{1n}x_n, \quad \dots, \quad x_n' = a_{n1}x_1 + \dots + a_{nn}x_n ,
\]
is the single equation \( \x' = \A\x \) for a vector-valued function \( \x \colon \nR \to \nC^{n} \), differentiated entrywise. In one dimension the answer is \( x(t) = e^{ta}x_0 \); the matrix exponential makes the general answer look exactly the same.

::: {#thm-linear-ode-solution}
[Solution of a Linear System]

Let \( \A \in M_n(\nC) \) and \( \x_0 \in \nC^{n} \). Then the function
\[
\x(t) = e^{t\A}\x_0 \qquad (t \in \nR)
\]
is differentiable and satisfies \( \x'(t) = \A\x(t) \) for all \( t \) and \( \x(0) = \x_0 \); and it is the **only** differentiable function \( \nR \to \nC^{n} \) with these two properties.
:::

::: {.idea}
Existence is @thm-exponential-properties (b) applied to a fixed vector. For uniqueness, take any solution \( \y \) and multiply it by \( e^{-t\A} \), the one factor that can undo the growth: the product has derivative \( 0 \), hence is constant. This is the same move as in the proofs of parts (c) and (d) above.
:::

::: {.proof}
*Existence.* Each entry of \( \x(t) = e^{t\A}\x_0 \) is a linear combination of entries of \( e^{t\A} \) with constant coefficients, so \( \x \) is differentiable with \( \x'(t) = \bigl(\frac{d}{dt}e^{t\A}\bigr)\x_0 \) by the linearity of differentiation (A3). By @thm-exponential-properties (b), \( \x'(t) = \A e^{t\A}\x_0 = \A\x(t) \). And \( \x(0) = e^{0}\x_0 = \x_0 \) by @thm-exponential-properties (a).

*Uniqueness.* Let \( \y \colon \nR \to \nC^{n} \) be differentiable with \( \y' = \A\y \) and \( \y(0) = \x_0 \). Put \( \z(t) = e^{-t\A}\y(t) \). By the product rule (A3) and @thm-exponential-properties (b) applied to \( -\A \),
\[
\z'(t) = \bigl(-\A e^{-t\A}\bigr)\y(t) + e^{-t\A}\y'(t) = -\A e^{-t\A}\y(t) + e^{-t\A}\A\y(t) = \0 ,
\]
where the last step uses \( e^{-t\A}\A = \A e^{-t\A} \) from @thm-exponential-properties (b). By (A4) each entry of \( \z \) is constant, so \( \z(t) = \z(0) = \x_0 \) for all \( t \). Multiplying by \( e^{t\A} \) and using @thm-exponential-properties (c),
\[
\y(t) = e^{t\A}\z(t) = e^{t\A}\x_0 = \x(t) .
\]
This proves the theorem.
:::

The formula is only as useful as our ability to compute \( e^{t\A} \), and the Jordan form does that. Two shapes of answer occur, and they are worth seeing side by side.

::: {#exm-ode-oscillation-and-resonance}
[Two Two-Dimensional Systems]

Solve \( \x' = \A\x \) with \( \x(0) = (1, 0) \) for

::: {.enumerate options="label=(\alph*)"}
1. \( \A = \begin{pmatrix} 1 & -2 \\ 2 & 1\end{pmatrix} \) (complex eigenvalues);
2. \( \A = \begin{pmatrix} 2 & 1 \\ 0 & 2\end{pmatrix} \) (one eigenvalue, one block of size \( 2 \)).
:::
:::

::: {.solution}
(a) \( p_{\A} = (x-1)^2 + 4 \), with roots \( \lambda = 1 \pm 2i \), distinct, so \( \A \) is diagonalizable over \( \nC \) and every block has size \( 1 \). Solving \( (\A - (1+2i)\I)\x = \0 \): the first row reads \( -2ix_1 - 2x_2 = 0 \), so \( x_2 = -ix_1 \) and \( (1, -i) \) is an eigenvector; \( (1, i) \) is one for \( 1 - 2i \). With \( \P = \begin{pmatrix} 1 & 1 \\ -i & i\end{pmatrix} \) we get \( \det \P = 2i \) and \( \P^{-1} = \tfrac{1}{2i}\begin{pmatrix} i & -1 \\ i & 1\end{pmatrix} = \tfrac12\begin{pmatrix} 1 & i \\ 1 & -i \end{pmatrix} \), so \( \P^{-1}\A \P = \diag(1+2i, 1-2i) \). By @cor-exponential-of-jordan-block,
\[
\begin{aligned}
e^{t\A}
  &= \P\diag\bigl(e^{(1+2i)t},\, e^{(1-2i)t}\bigr)\P^{-1} \\
  &= \tfrac12\begin{pmatrix} e^{(1+2i)t} + e^{(1-2i)t} & i\bigl(e^{(1+2i)t} - e^{(1-2i)t}\bigr) \\ -i\bigl(e^{(1+2i)t} - e^{(1-2i)t}\bigr) & e^{(1+2i)t} + e^{(1-2i)t}\end{pmatrix}.
\end{aligned}
\]
By (A1), \( e^{(1 \pm 2i)t} = e^{t}(\cos 2t \pm i\sin 2t) \), so \( e^{(1+2i)t} + e^{(1-2i)t} = 2e^{t}\cos 2t \) and \( e^{(1+2i)t} - e^{(1-2i)t} = 2ie^{t}\sin 2t \). Substituting, and using \( i \cdot 2i = -2 \),
\[
e^{t\A} = e^{t}\begin{pmatrix} \cos 2t & -\sin 2t \\ \sin 2t & \cos 2t \end{pmatrix}, \qquad \x(t) = e^{t\A}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = e^{t}\begin{pmatrix} \cos 2t \\ \sin 2t\end{pmatrix}.
\]
The solution spirals outwards: rotation at angular speed \( 2 \), growth at rate \( 1 \). The entries are real, as they must be for a real \( \A \) and a real \( \x_0 \).

*Check.* \( \x'(t) = e^{t}(\cos 2t - 2\sin 2t,\ \sin 2t + 2\cos 2t) \), and \( \A\x(t) = e^{t}(\cos 2t - 2\sin 2t,\ 2\cos 2t + \sin 2t) \). They agree, and \( \x(0) = (1,0) \).

(b) \( \A = \J_2(2) \) is its own Jordan form. Writing \( \A = 2\I + \M \) with \( \M = \begin{pmatrix} 0&1\\0&0\end{pmatrix} \), the two summands commute and \( \M^2 = 0 \), so @cor-exponential-of-jordan-block with \( k = 2 \) gives
\[
e^{t\A} = e^{2t}\bigl(\I + t\M\bigr) = e^{2t}\begin{pmatrix} 1 & t \\ 0 & 1\end{pmatrix}.
\]
So \( \x(t) = e^{2t}(1, 0) \). A different initial vector shows the new phenomenon: \( \x(0) = (0,1) \) gives \( \x(t) = e^{2t}(t, 1) \), whose first entry is \( te^{2t} \). **A repeated eigenvalue with a block of size \( k \) produces solutions containing \( t^{j}e^{\lambda t} \) for \( j < k \).** This is the same \( t^{j}\lambda^{m} \) pattern that Chapter 8 met for recurrences with repeated roots, now in continuous time.
:::

A scalar equation of higher order is a system in disguise, and the translation is the companion matrix of Section 5.

::: {#exm-second-order-scalar-ode}
[A Second-Order Equation with a Repeated Root]

Solve \( y'' - 4y' + 4y = 0 \) with \( y(0) = 1 \) and \( y'(0) = 3 \).
:::

::: {.solution}
*Make it a system.* Put \( \u = (y, y') \). Then \( \u' = (y', y'') = (y', 4y' - 4y) \), so \( \u' = \M\u \) with
\[
\M = \begin{pmatrix} 0 & 1 \\ -4 & 4\end{pmatrix}, \qquad \u(0) = (1, 3).
\]
Note that \( p_{\M} = x(x - 4) + 4 = x^2 - 4x + 4 \) is the polynomial of the equation, and that \( \M = \C(p_{\M})\tp \) for the companion matrix \( \C(p_{\M}) = \begin{pmatrix} 0 & -4 \\ 1 & 4\end{pmatrix} \) of @def-companion-matrix; by @cor-a-similar-to-transpose the two are similar, so which of them one uses is immaterial.

*Exponentiate.* \( p_{\M} = (x-2)^2 \). Put \( \N = \M - 2\I = \begin{pmatrix} -2 & 1 \\ -4 & 2\end{pmatrix} \); then \( \N^2 = \begin{pmatrix} 4 - 4 & -2+2 \\ 8-8 & -4+4\end{pmatrix} = 0 \), so \( 2\I \) and \( \N \) commute and @thm-exponential-properties (d) gives, as in the previous example,
\[
e^{t\M} = e^{2t}(\I + t\N) = e^{2t}\begin{pmatrix} 1 - 2t & t \\ -4t & 1 + 2t\end{pmatrix}.
\]
(No basis change was needed: \( \M \) is a scalar plus a nilpotent matrix on the nose.)

*Read off the answer.*
\[
\u(t) = e^{t\M}\begin{pmatrix} 1 \\ 3\end{pmatrix} = e^{2t}\begin{pmatrix} (1 - 2t) + 3t \\ -4t + 3(1 + 2t)\end{pmatrix} = e^{2t}\begin{pmatrix} 1 + t \\ 3 + 2t \end{pmatrix},
\]
so \( y(t) = (1+t)e^{2t} \).

*Check.* \( y' = e^{2t} + 2(1+t)e^{2t} = (3 + 2t)e^{2t} \), which is the second entry of \( \u \), as it should be, and \( y'(0) = 3 \). Then \( y'' = 2e^{2t} + 2(3+2t)e^{2t} = (8 + 4t)e^{2t} \), and
\[
y'' - 4y' + 4y = \bigl[(8 + 4t) - 4(3 + 2t) + 4(1 + t)\bigr]e^{2t} = 0 .
\]
The repeated root \( 2 \) produces the term \( te^{2t} \), exactly as the size-\( 2 \) block predicts.
:::

Chapter 15 will return to \( e^{\A} \) with norms available, which give quantitative bounds instead of exact formulas. The next section stays with exact formulas and asks the discrete-time question: what happens to \( \A^{m} \)?

## Exercises

### A. Check your understanding

:::: {#exr-functions-of-matrices-and-odes-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the formula for \( p(\J_k(\lambda)) \) and say where the factorials come from.
2. Define \( f(\A) \) for \( \A \in M_n(\nC) \) with a given Jordan form, and list the two choices whose irrelevance has to be checked.
3. Which values of \( f \) and its derivatives does \( f(\A) \) depend on? How many numbers is that?
4. State the five properties of \( e^{\A} \) proved in @thm-exponential-properties, with their hypotheses.
5. True or false: \( e^{\A+\B} = e^{\A}e^{\B} \) for all \( \A, \B \in M_n(\nC) \). Justify your answer.
6. True or false: \( e^{\A} \) can be singular. Justify your answer.
:::
::::

::: {.solution}
(a) \( p(\J_k(\lambda)) \) is upper triangular with \( p^{(j)}(\lambda)/j! \) in every position \( (r, r+j) \) (@lem-polynomial-of-jordan-block). The factorials come from the Taylor expansion \( p = \sum_j \frac{p^{(j)}(\lambda)}{j!}(x-\lambda)^j \) (@thm-polynomial-taylor), whose \( j \)-th term contributes \( \J_k(0)^{j} \), the matrix with ones on the \( j \)-th superdiagonal.

(b) \( f(\A) = \P\bigl(\bigoplus_i f(\J_{k_i}(\lambda_i))\bigr)\P^{-1} \) with \( f(\J_k(\lambda)) \) as in (a) (@def-matrix-function-jordan). The choices are the matrix \( \P \) and the order in which the blocks are listed; both are irrelevant because \( f(\A) = p(\A) \) for the Hermite interpolating polynomial \( p \) (@thm-matrix-function-hermite).

(c) On \( f^{(j)}(\mu) \) for each eigenvalue \( \mu \) and each \( j < s_\mu \), where \( s_\mu \) is the exponent of \( x - \mu \) in \( m_{\A} \), that is, the largest \( \mu \)-block size. The total number is \( \sum_\mu s_\mu = \deg m_{\A} \) (@thm-matrix-function-hermite).

(d) \( e^{\P^{-1}\A \P} = \P^{-1}e^{\A}\P \) for invertible \( \P \); \( \frac{d}{dt}e^{t\A} = \A e^{t\A} = e^{t\A}\A \); \( (e^{\A})^{-1} = e^{-\A} \); \( e^{\A+\B} = e^{\A}e^{\B} \) **provided \( \A \B = \B \A \)**; and \( \det e^{\A} = e^{\tr \A} \) with no hypothesis.

(e) False. With \( \A = \begin{pmatrix} 0&1\\0&0\end{pmatrix} \) and \( \B = \A\tp \), the matrices \( e^{\A}e^{\B} \) and \( e^{\B}e^{\A} \) differ, so the identity cannot hold for both orders; see the warning after @thm-exponential-properties.

(f) False. \( \det e^{\A} = e^{\tr \A} \ne 0 \) by @thm-exponential-properties (e) and (A1), so \( e^{\A} \) is always invertible (@thm-det-nonzero-iff-invertible).
:::

### B. Practice

:::: {#exr-functions-of-matrices-and-odes-b1}
[B1: Computing exponentials]

Compute \( e^{t\A} \) for each of the following.

::: {.enumerate options="label=(\alph*)"}
1. \( \A = \begin{pmatrix} 1 & 3 \\ 3 & 1\end{pmatrix} \).
2. \( \A = \begin{pmatrix} 5 & 1 \\ 0 & 5\end{pmatrix} \).
3. \( \A = \begin{pmatrix} 3 & 1 & 0 \\ 0 & 3 & 1 \\ 0 & 0 & 3\end{pmatrix} = \J_3(3) \).
:::
::::

::: {.solution}
(a) \( p_{\A} = (x-1)^2 - 9 \), with roots \( 4 \) and \( -2 \). Eigenvectors: \( (\A - 4\I)\x = \0 \) gives \( \Span((1,1)) \); \( (\A + 2\I)\x = \0 \) gives \( \Span((1,-1)) \). With \( \P = \begin{pmatrix} 1 & 1 \\ 1 & -1\end{pmatrix} \) we have \( \det \P = -2 \), \( \P^{-1} = \tfrac12\begin{pmatrix} 1 & 1 \\ 1 & -1\end{pmatrix} \) and \( \P^{-1}\A \P = \diag(4, -2) \), so by @cor-exponential-of-jordan-block
\[
e^{t\A} = \P\diag(e^{4t}, e^{-2t})\P^{-1} = \tfrac12\begin{pmatrix} e^{4t} + e^{-2t} & e^{4t} - e^{-2t} \\ e^{4t} - e^{-2t} & e^{4t} + e^{-2t}\end{pmatrix}.
\]
*Check at \( t = 0 \):* both diagonal entries give \( 1 \) and both off-diagonal ones \( 0 \), so \( e^{0} = \I \).

(b) \( \A = \J_2(5) \), so @cor-exponential-of-jordan-block with \( k = 2 \) gives
\[
e^{t\A} = e^{5t}(\I + t\M) = e^{5t}\begin{pmatrix} 1 & t \\ 0 & 1\end{pmatrix}.
\]

(c) By @cor-exponential-of-jordan-block with \( k = 3 \) and \( \lambda = 3 \), or directly from \( \A = 3\I + \M \) with \( \M = \J_3(0) \) and \( \M^3 = 0 \), giving \( e^{t\A} = e^{3t}\bigl(\I + t\M + \tfrac{t^2}{2}\M^2\bigr) \):
\[
e^{t\A} = e^{3t}\begin{pmatrix} 1 & t & \tfrac{t^2}{2} \\ 0 & 1 & t \\ 0 & 0 & 1\end{pmatrix}.
\]
This is @def-matrix-function-jordan for \( f(x) = e^{tx} \): the \( j \)-th superdiagonal carries \( f^{(j)}(3)/j! = t^{j}e^{3t}/j! \).
:::

:::: {#exr-functions-of-matrices-and-odes-b2}
[B2: Solving systems]

Solve each initial value problem, and verify your answer by differentiating.

::: {.enumerate options="label=(\alph*)"}
1. \( x' = x + 3y \), \( y' = 3x + y \), with \( x(0) = 2 \), \( y(0) = 0 \).
2. \( \x' = \begin{pmatrix} 0 & -3 \\ 3 & 0\end{pmatrix}\x \) with \( \x(0) = (0, 1) \).
3. \( y''' = 0 \) with \( y(0) = 1 \), \( y'(0) = 0 \), \( y''(0) = 2 \), by turning it into a system.
:::
::::

::: {.solution}
(a) This is \( \x' = \A\x \) for the matrix of @exr-functions-of-matrices-and-odes-b1 (a). By @thm-linear-ode-solution,
\[
\x(t) = e^{t\A}\begin{pmatrix} 2 \\ 0\end{pmatrix} = \begin{pmatrix} e^{4t} + e^{-2t} \\ e^{4t} - e^{-2t}\end{pmatrix},
\]
that is, \( x = e^{4t} + e^{-2t} \) and \( y = e^{4t} - e^{-2t} \). *Check.* \( x' = 4e^{4t} - 2e^{-2t} \) and \( x + 3y = e^{4t} + e^{-2t} + 3e^{4t} - 3e^{-2t} = 4e^{4t} - 2e^{-2t} \); similarly for \( y' \). And \( x(0) = 2 \), \( y(0) = 0 \).

(b) Write \( \A = 3\R \) with \( \R = \begin{pmatrix} 0&-1\\1&0\end{pmatrix} \), whose eigenvalues are \( \pm i \) (@exm-complex-eigenvalues-real-matrix), so those of \( \A \) are \( \pm 3i \), distinct. Repeating the computation of @exm-ode-oscillation-and-resonance (a) with \( 1 \pm 2i \) replaced by \( \pm 3i \) — eigenvectors \( (1, -i) \) for \( 3i \) and \( (1, i) \) for \( -3i \) — gives
\[
e^{t\A} = \begin{pmatrix} \cos 3t & -\sin 3t \\ \sin 3t & \cos 3t\end{pmatrix}, \qquad \x(t) = \begin{pmatrix} -\sin 3t \\ \cos 3t\end{pmatrix}.
\]
*Check.* \( \x'(t) = (-3\cos 3t, -3\sin 3t) \) and \( \A\x(t) = (-3\cos 3t, -3\sin 3t) \); and \( \x(0) = (0,1) \). The solution runs around the unit circle: no growth, since the eigenvalues are purely imaginary.

(c) Put \( \u = (y, y', y'') \). Then \( \u' = (y', y'', 0) = \M\u \) with \( \M = \J_3(0) \), and \( \u(0) = (1, 0, 2) \). By @cor-exponential-of-jordan-block with \( \lambda = 0 \) and \( k = 3 \),
\[
e^{t\M} = \begin{pmatrix} 1 & t & t^2/2 \\ 0 & 1 & t \\ 0 & 0 & 1\end{pmatrix}, \qquad \u(t) = e^{t\M}\begin{pmatrix} 1 \\ 0 \\ 2\end{pmatrix} = \begin{pmatrix} 1 + t^2 \\ 2t \\ 2\end{pmatrix}.
\]
So \( y(t) = 1 + t^2 \). *Check.* \( y' = 2t \), \( y'' = 2 \), \( y''' = 0 \), and the three initial values are \( 1, 0, 2 \). The eigenvalue \( 0 \) with one block of size \( 3 \) gives polynomial solutions \( t^{j}e^{0t} = t^{j} \) for \( j < 3 \).
:::

:::: {#exr-functions-of-matrices-and-odes-b3}
[B3: A square root and a logarithm]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \A = \begin{pmatrix} 2 & 1 \\ 1 & 2\end{pmatrix} \). Compute \( f(\A) \) for \( f(x) = \sqrt x \) (positive branch) and verify that \( f(\A)^2 = \A \).
2. Let \( \B = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \). Compute \( f(\B) \) for \( f(x) = \log x \) with \( \log 1 = 0 \), and verify that \( e^{f(\B)} = \B \).
3. Explain why the same method produces **no** square root of \( \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \).
:::
::::

::: {.solution}
(a) \( p_{\A} = (x-2)^2 - 1 = (x-1)(x-3) \), eigenvalues \( 1, 3 \). Eigenvectors \( (1,-1) \) for \( 1 \) and \( (1,1) \) for \( 3 \). With \( \P = \begin{pmatrix} 1 & 1 \\ -1 & 1\end{pmatrix} \) and \( \P^{-1} = \tfrac12\begin{pmatrix} 1 & -1 \\ 1 & 1\end{pmatrix} \),
\[
f(\A) = \P\diag(1, \sqrt3)\P^{-1} = \tfrac12\begin{pmatrix} 1 + \sqrt3 & -1 + \sqrt3 \\ -1 + \sqrt3 & 1 + \sqrt3\end{pmatrix}.
\]
Squaring, the diagonal entry is \( \tfrac14\bigl[(1+\sqrt3)^2 + (\sqrt3 - 1)^2\bigr] = \tfrac14(4 + 2\sqrt3 + 4 - 2\sqrt3) = 2 \), and the off-diagonal entry is \( \tfrac14\cdot 2(1+\sqrt3)(\sqrt3-1) = \tfrac12(3 - 1) = 1 \). So \( f(\A)^2 = \A \).

(b) Here \( m_{\B} = (x-1)^2 \), since \( (\B - \I)^2 = 0 \ne \B - \I \), so by @thm-matrix-function-hermite the answer is \( p(\B) \) for the polynomial of degree \( < 2 \) with \( p(1) = f(1) = 0 \) and \( p'(1) = f'(1) = 1 \), namely \( p = x - 1 \). Hence
\[
f(\B) = \B - \I = \begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix}.
\]
Its square is \( 0 \), so \( e^{f(\B)} = \I + f(\B) = \begin{pmatrix} 1 & 2 \\ 0 & 1\end{pmatrix} = \B \). The Jordan route gives the same thing: with \( \Q = \diag(2, 1) \) we get \( \Q^{-1}\B \Q = \J_2(1) \), and \( f(\J_2(1)) = \begin{pmatrix} 0 & 1 \\ 0 & 0\end{pmatrix} \), so \( f(\B) = \Q f(\J_2(1))\Q^{-1} = \begin{pmatrix} 0 & 2 \\ 0 & 0\end{pmatrix} \).

(c) The matrix is \( \J_2(0) \), with the single eigenvalue \( 0 \) and a block of size \( 2 \). @def-matrix-function-jordan needs \( f \) and \( f' \) at \( 0 \), and \( f(x) = \sqrt x \) is not differentiable at \( 0 \) — the entry \( f'(0) \) does not exist. In fact \( \J_2(0) \) has no square root at all: if \( \X^2 = \J_2(0) \), then \( \X^4 = \J_2(0)^2 = 0 \), so \( \X \) is nilpotent, so \( \X^2 = 0 \) by @prp-nilpotent-basic (a) with \( n = 2 \), contradicting \( \X^2 = \J_2(0) \ne 0 \).
:::

### C. Going deeper

:::: {#exr-functions-of-matrices-and-odes-c1}
[C1: How badly the exponential law fails]

Let \( \A = \begin{pmatrix} 0 & 1 \\ 0 & 0\end{pmatrix} \) and \( \B = \begin{pmatrix} 0 & 0 \\ 1 & 0\end{pmatrix} \) in \( M_2(\nR) \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( e^{\A} \), \( e^{\B} \), \( e^{\A}e^{\B} \) and \( e^{\B}e^{\A} \).
2. Compute \( e^{\A+\B} \) in closed form. *Hint: \( (\A+\B)^2 = \I \), so split the series into even and odd terms.*
3. Verify \( \det e^{\A+\B} = e^{\tr(\A+\B)} \) and \( \det(e^{\A}e^{\B}) = e^{\tr \A}e^{\tr \B} \), and explain why equal determinants do not rescue the identity.
4. Show that \( e^{\A}e^{\B} = e^{\C} \) for **some** \( \C \in M_2(\nR) \), and find \( \tr \C \).
:::
::::

::: {.solution}
(a) \( \A^2 = \B^2 = 0 \), so \( e^{\A} = \I + \A = \begin{pmatrix} 1 & 1 \\ 0 & 1\end{pmatrix} \) and \( e^{\B} = \I + \B = \begin{pmatrix} 1 & 0 \\ 1 & 1\end{pmatrix} \). Then
\[
e^{\A}e^{\B} = \begin{pmatrix} 2 & 1 \\ 1 & 1\end{pmatrix}, \qquad e^{\B}e^{\A} = \begin{pmatrix} 1 & 1 \\ 1 & 2\end{pmatrix}.
\]

(b) Let \( \K = \A + \B = \begin{pmatrix} 0&1\\1&0\end{pmatrix} \). Then \( \K^2 = \I \), so \( \K^{2l} = \I \) and \( \K^{2l+1} = \K \). Splitting the partial sums by parity, which is legitimate because each entry sequence is a sum of two convergent sequences (A3),
\[
\begin{aligned}
e^{\K}
  &= \Bigl(\sum_{l \ge 0}\frac{1}{(2l)!}\Bigr)\I + \Bigl(\sum_{l \ge 0}\frac{1}{(2l+1)!}\Bigr)\K \\
  &= \frac{e + e^{-1}}{2}\I + \frac{e - e^{-1}}{2}\K
   = \begin{pmatrix} \tfrac{e+e^{-1}}{2} & \tfrac{e - e^{-1}}{2} \\ \tfrac{e-e^{-1}}{2} & \tfrac{e+e^{-1}}{2}\end{pmatrix},
\end{aligned}

\]
where the two scalar sums were identified by adding and subtracting the series for \( e^{1} \) and \( e^{-1} \) term by term (A1). Numerically the diagonal entries are about \( 1.543 \), not \( 2 \), so \( e^{\A+\B} \ne e^{\A}e^{\B} \).

(c) \( \tr(\A+\B) = 0 \) and \( \det e^{\A+\B} = \bigl(\tfrac{e+e^{-1}}{2}\bigr)^2 - \bigl(\tfrac{e-e^{-1}}{2}\bigr)^2 = \tfrac14\bigl[(e+e^{-1})^2 - (e - e^{-1})^2\bigr] = \tfrac14\cdot 4 = 1 = e^{0} \). Also \( \det(e^{\A}e^{\B}) = 2 - 1 = 1 = e^{0}e^{0} \). The determinants agree because both matrices are products of exponentials of trace-zero matrices; a determinant is one number and cannot distinguish two matrices, so it gives no information about the identity either way. The entries do.

(d) \( \X = e^{\A}e^{\B} = \begin{pmatrix} 2&1\\1&1\end{pmatrix} \) is symmetric with \( \det \X = 1 \) and \( \tr \X = 3 \), so \( p_{\X} = x^2 - 3x + 1 \), whose roots \( \tfrac{3 \pm \sqrt5}{2} \) are real, distinct and positive. So \( \X = \P\diag(\alpha, \beta)\P^{-1} \) with \( \alpha\beta = 1 \), \( \alpha, \beta > 0 \). Put \( \C = \P\diag(\log\alpha, \log\beta)\P^{-1} \), a real matrix because \( \P \) can be taken real (the eigenvalues are real) and the logarithms are real. By @def-matrix-function-jordan applied to \( f = \exp \), \( e^{\C} = \P\diag(\alpha, \beta)\P^{-1} = \X \). Finally \( \tr \C = \log\alpha + \log\beta = \log(\alpha\beta) = \log 1 = 0 \), as @thm-exponential-properties (e) requires, since \( \det \X = 1 \).
:::

:::: {#exr-functions-of-matrices-and-odes-c2}
[C2: When does every solution die out?]

Let \( \A \in M_n(\nC) \). Prove that the following are equivalent:

::: {.enumerate options="label=(\roman*)"}
1. every solution of \( \x' = \A\x \) satisfies \( \x(t) \to \0 \) entrywise as \( t \to \infty \);
2. every eigenvalue \( \lambda \) of \( \A \) has \( \operatorname{Re}\lambda < 0 \).
:::

*Hint: compute the entries of \( e^{t\J_k(\lambda)} \) and use (A5). For the failing direction, an eigenvector gives a solution you can write down.*
::::

::: {.solution}
(ii) \( \Rightarrow \) (i). By @thm-linear-ode-solution every solution is \( \x(t) = e^{t\A}\x_0 \), so it suffices to show \( e^{t\A} \to 0 \) entrywise. Write \( \A = \P \J \P^{-1} \) with \( \J = \bigoplus_i \J_{k_i}(\lambda_i) \) (@thm-jordan-canonical-form). Each entry of \( e^{t\A} = \P e^{t\J}\P^{-1} \) is a fixed linear combination of entries of \( e^{t\J} \), so by (A3) it is enough that \( e^{t\J} \to 0 \). By @cor-exponential-of-jordan-block, the non-zero entries of \( e^{t\J_k(\lambda)} \) are
\[
\frac{t^{j}e^{\lambda t}}{j!} \qquad (0 \le j \le k-1).
\]
Writing \( \lambda = c + i\omega \) with \( c = \operatorname{Re}\lambda < 0 \), we get \( |t^{j}e^{\lambda t}| = t^{j}e^{ct}|e^{i\omega t}| = t^{j}e^{ct} \) for \( t \ge 0 \), since \( |e^{i\omega t}| = |\cos\omega t + i\sin\omega t| = 1 \) by (A1). By (A5) this tends to \( 0 \), and a complex sequence tends to \( 0 \) exactly when its moduli do. Hence \( e^{t\J} \to 0 \).

(i) \( \Rightarrow \) (ii). Suppose some eigenvalue \( \lambda \) has \( \operatorname{Re}\lambda = c \ge 0 \), and let \( \v \ne \0 \) be an eigenvector. Then \( \x(t) = e^{\lambda t}\v \) is a solution: it is differentiable with \( \x'(t) = \lambda e^{\lambda t}\v = e^{\lambda t}\A\v = \A\x(t) \), and \( \x(0) = \v \). Pick a coordinate with \( v_r \ne 0 \); then
\[
\bigl|x_r(t)\bigr| = \bigl|e^{\lambda t}\bigr|\,|v_r| = e^{ct}|v_r| \ge |v_r| > 0
\]
for every \( t \ge 0 \), because \( e^{ct} \ge 1 \) when \( c \ge 0 \). So \( x_r(t) \) does not tend to \( 0 \), and (i) fails. This proves the equivalence.
:::
