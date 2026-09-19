# Which Functions Respect the Order

Chapter 12 §05 ended on two facts that sit awkwardly together. If \( \A \succeq \B \succeq 0 \), then \( \A^{1/2} \succeq \B^{1/2} \) (@prp-square-root-monotone); but \( \A^2 \succeq \B^2 \) can fail (@exm-loewner-not-monotone). For numbers, both \( t \mapsto t^{1/2} \) and \( t \mapsto t^2 \) are increasing on \( [0, \infty) \), and both preserve inequalities. This section names the property that separates them and proves it for every function the book can reach. It then compares that property with what §02's min–max theorem already gives for *every* increasing function, and states without proof the classification that settles the question. Since this is the last section of the chapter, it ends by summing up the chapter's moves and listing the promises the chapter has paid.

**Throughout, \( F = \nR \) or \( F = \nC \), and every matrix whose eigenvalues are indexed is Hermitian**, with eigenvalues \( \lambda_1(\A) \ge \dots \ge \lambda_n(\A) \) indexed decreasingly and repeated according to multiplicity. The letter \( I \) denotes an **interval** of real numbers (open, closed or half-open, bounded or not). It is plain italic, and it is not the bold identity matrix \( \I \). A function \( f \colon I \to \nR \) is **increasing** when \( s \le t \) implies \( f(s) \le f(t) \); strictness is not required. Every result below holds for either choice of \( F \), with the same proof. No analysis is used anywhere in this section except in the last part, which states a theorem without proving it.

## Functions of a Hermitian matrix

Chapter 11 §08 already applies a function to a matrix, and nothing needs rebuilding. Let \( \A \in M_n(F) \) be Hermitian. The operator \( \x \mapsto \A\x \) on \( F^n \) has an orthonormal basis of eigenvectors (@cor-spectral-complex-matrix, @cor-spectral-real-matrix), so it has a spectral resolution
\[
\A = \mu_1\P_1 + \dots + \mu_k\P_k
\]
with \( \mu_1, \dots, \mu_k \) the **distinct** eigenvalues and \( \P_j \) the orthogonal projection onto the eigenspace of \( \mu_j \) (@def-spectral-resolution, @thm-spectral-resolution). For any function \( f \) defined on \( \spec(\A) \), @def-function-of-normal-operator sets
\[
f(\A) \coloneqq f(\mu_1)\P_1 + \dots + f(\mu_k)\P_k .
\]
In this section \( f \) is always defined on an interval \( I \) containing \( \spec(\A) \), and \( f(\A) \) is formed from the restriction of \( f \) to the spectrum: the values of \( f \) off the spectrum play no part. Four facts from @thm-functional-calculus-properties are used constantly.

- **Polynomials give the expected answer** (part (a)): \( t \mapsto \alpha + \beta t \) gives \( \alpha\I + \beta\A \), and \( t \mapsto t^2 \) gives \( \A^2 \).
- **Sums and products go through** (part (b)): \( (f + g)(\A) = f(\A) + g(\A) \), \( (cf)(\A) = c\,f(\A) \) and \( (fg)(\A) = f(\A)g(\A) \).
- **Real-valued \( f \) gives a Hermitian \( f(\A) \)** (part (c)). This is what lets \( f(\A) \) be compared with anything in the Loewner order.
- **The eigenvectors do not change** (part (d)): \( f(\A) \) has the same orthonormal eigenbasis as \( \A \).

Two instances have names already. If \( 0 \notin \spec(\A) \), then \( t \mapsto 1/t \) gives \( \A^{-1} \), as Chapter 11 §08 records right after @def-function-of-normal-operator. If \( \A \succeq 0 \), then \( t \mapsto t^{1/2} \) gives the positive square root \( \A^{1/2} \) of @thm-psd-square-root, which Chapter 12 §02 constructed in exactly this way.

## Operator monotone and operator convex functions

Chapter 12 §05 introduced the Loewner order \( \A \succeq \B \), meaning \( \A - \B \succeq 0 \) (@def-loewner-order). With the functional calculus available, the natural question is which functions \( f \) carry \( \A \succeq \B \) to \( f(\A) \succeq f(\B) \).

The obvious guess is "the increasing ones", since that is the answer for numbers. It is wrong. The function \( t \mapsto t^2 \) is increasing on \( [0, \infty) \), and @exm-loewner-not-monotone gives Hermitian \( 2 \times 2 \) matrices \( \A \succeq \B \succeq 0 \) with \( \A^2 \not\succeq \B^2 \). So the property we want is stronger than being increasing, and it needs its own name.

*A function is operator monotone when applying it to Hermitian matrices never breaks the Loewner order, at every size at once.*

:::: {#def-operator-monotone}
[Operator Monotone and Operator Convex Functions]

Let \( I \subseteq \nR \) be an interval and let \( f \colon I \to \nR \).

::: {.enumerate options="label=(\alph*)"}
1. \( f \) is **operator monotone on \( I \)** if, **for every size \( n \ge 1 \)** and every pair of Hermitian matrices \( \A, \B \in M_n(F) \) whose spectra lie in \( I \),
\[
\A \succeq \B \quad \Longrightarrow \quad f(\A) \succeq f(\B) .
\]
2. \( f \) is **operator convex on \( I \)** if, **for every size \( n \ge 1 \)**, every pair of Hermitian matrices \( \A, \B \in M_n(F) \) whose spectra lie in \( I \), and every \( \theta \in [0, 1] \),
\[
f\bigl(\theta\A + (1 - \theta)\B\bigr) \preceq \theta f(\A) + (1 - \theta)f(\B) .
\]
It is **operator concave on \( I \)** if \( -f \) is operator convex on \( I \).
:::

Here \( f(\A) \) is the matrix of @def-function-of-normal-operator.
::::

In words: the first condition takes any two Hermitian matrices of the same size with spectra inside the domain of \( f \). If the first dominates the second, applying \( f \) must preserve that. The second condition is the matrix version of "the chord lies above the graph". Both are infinitely many conditions, one for each size \( n \). A function that passes the test for \( 2 \times 2 \) matrices has not yet passed it for \( 3 \times 3 \) ones. The clause "for every \( n \)" is why the notion is hard, and also why it is interesting.

**Everything in the definition makes sense.** Since \( \spec(\A) \subseteq I \), the matrix \( f(\A) \) is defined, and it is Hermitian because \( f \) is real-valued (@thm-functional-calculus-properties (c)). So \( f(\A) \succeq f(\B) \) is a statement about two Hermitian matrices, as @def-loewner-order requires. In (b) one more thing needs checking: the spectrum of \( \C = \theta\A + (1-\theta)\B \) must lie in \( I \), or \( f(\C) \) would not be defined. The matrix \( \C \) is Hermitian. Let \( \x \) be a unit eigenvector of \( \C \) for the eigenvalue \( \mu \). Then
\[
\mu = \inner{\C\x}{\x} = \theta\inner{\A\x}{\x} + (1 - \theta)\inner{\B\x}{\x} .
\]
By @lem-extreme-eigenvalues-quadratic-form, \( \inner{\A\x}{\x} \) lies in \( [\lambda_n(\A), \lambda_1(\A)] \). That interval is contained in \( I \), because its endpoints are eigenvalues of \( \A \) and \( I \) is an interval. Likewise \( \inner{\B\x}{\x} \in I \). So \( \mu \) is a convex combination of two points of the interval \( I \), and it therefore lies in \( I \).

The smallest size already says something, and the proof is three lines.

::: {#prp-operator-monotone-increasing}
[Operator Monotone Functions Are Increasing]

If \( f \) is operator monotone on \( I \), then \( f \) is increasing on \( I \).
:::

::: {.proof}
Let \( s \le t \) in \( I \), and take \( n = 1 \), \( \A = (t) \), \( \B = (s) \). These are Hermitian, their spectra \( \{t\} \) and \( \{s\} \) lie in \( I \), and \( \A - \B = (t - s) \succeq 0 \). Hence \( f(\A) \succeq f(\B) \), and since \( f(\A) = (f(t)) \) and \( f(\B) = (f(s)) \), this says \( f(t) - f(s) \ge 0 \). This shows that \( f \) is increasing.
:::

The converse is false, and the failure is the reason this section exists.

::: {.warning}
**Increasing is not enough.** "Increasing" is exactly the case \( n = 1 \) of the definition, and sizes \( n \ge 2 \) are where all the new content lies. The function \( t \mapsto t^2 \) is increasing on \( [0, \infty) \) and is **not** operator monotone there. The \( 2 \times 2 \) matrices \( \A = \begin{psmallmatrix} 2 & 1 \\ 1 & 1\end{psmallmatrix} \) and \( \B = \begin{psmallmatrix} 1 & 1 \\ 1 & 1\end{psmallmatrix} \) of @exm-loewner-not-monotone satisfy \( \A \succeq \B \succeq 0 \), yet \( \A^2 - \B^2 \) has negative determinant. Chapter 12 §05 traced the failure to non-commutativity: the number proof factors \( a^2 - b^2 \) as \( (a - b)(a + b) \), and for matrices that factorization needs \( \A\B = \B\A \).
:::

::: {.check}
Is \( t \mapsto t^3 \) operator monotone on \( \nR \) when only \( n = 1 \) is tested? What does the answer tell you about \( n = 2 \)?
:::

::: {.solution}
For \( n = 1 \) the condition says only that \( f \) is increasing, as the proof of @prp-operator-monotone-increasing shows, and \( t \mapsto t^3 \) is increasing on \( \nR \). So it passes at \( n = 1 \). That tells us nothing about \( n = 2 \), where the test is genuinely new. In fact \( t \mapsto t^3 \) fails at \( n = 2 \) (exercise C3).
:::

## The examples we can prove

Four families are within reach, and the first is the simplest. It includes a degenerate case, the constant functions, which respect every order because they flatten everything to one matrix.

::: {#prp-affine-operator-monotone}
[Increasing Affine Functions]

Let \( \alpha, \beta \in \nR \) with \( \beta \ge 0 \). Then \( f(t) = \alpha + \beta t \) is operator monotone on \( \nR \). Moreover, every affine function \( t \mapsto \alpha + \beta t \), with \( \beta \) of either sign, is both operator convex and operator concave on \( \nR \).
:::

::: {.proof}
By @thm-functional-calculus-properties (a), \( f(\A) = \alpha\I + \beta\A \) for every Hermitian \( \A \). Let \( \A \succeq \B \) be Hermitian of the same size. Then \( f(\A) - f(\B) = \beta(\A - \B) \), and for every \( \x \),
\[
\inner{\beta(\A - \B)\x}{\x} = \beta\inner{(\A - \B)\x}{\x} \ \ge\ 0 ,
\]
a product of two non-negative numbers. Hence \( f(\A) \succeq f(\B) \). For the second statement, with \( \C = \theta\A + (1-\theta)\B \),
\[
\begin{aligned}
f(\C) &= \alpha\I + \beta\theta\A + \beta(1-\theta)\B \\
      &= \theta(\alpha\I + \beta\A) + (1-\theta)(\alpha\I + \beta\B)
       = \theta f(\A) + (1-\theta)f(\B) ,
\end{aligned}
\]
so the inequality in @def-operator-monotone (b) holds with equality, for \( f \) and for \( -f \) alike.
:::

The second example is the one that behaves like the square root: \( t \mapsto -1/t \). For numbers, \( a \ge b > 0 \) gives \( -1/a \ge -1/b \) because one may divide by the product \( ab \). For matrices that division is unavailable, since \( \A \) and \( \B \) need not commute. Chapter 12 §05 already found the way round.

::: {#prp-inverse-operator-monotone}
[The Negative Reciprocal Is Operator Monotone]

The function \( t \mapsto -1/t \) is operator monotone on \( (0, \infty) \). Explicitly: if \( \A, \B \in M_n(F) \) are Hermitian with \( \A \succeq \B \succ 0 \), then \( \A \succ 0 \) and
\[
-\A^{-1} \ \succeq\ -\B^{-1}, \qquad\text{that is,}\qquad \B^{-1} \succeq \A^{-1} .
\]
:::

::: {.idea}
A congruence removes the non-commutativity. Conjugating by \( \B^{-1/2} \) turns \( \B \) into \( \I \) and \( \A \) into \( \C = \B^{-1/2}\A\B^{-1/2} \succeq \I \). Now one of the two matrices is the identity, which commutes with everything, so the argument for numbers applies to the eigenvalues of \( \C \): they are all \( \ge 1 \), so those of \( \C^{-1} \) are all \( \le 1 \). Undoing the congruence carries \( \I \succeq \C^{-1} \) back to \( \B^{-1} \succeq \A^{-1} \). That is exactly the proof of @thm-loewner-basic (d), so the proposition is that clause read as a statement about the function \( t \mapsto -1/t \).
:::

::: {.proof}
Let \( \A \succeq \B \) be Hermitian with spectra in \( (0, \infty) \). By @thm-pd-characterizations (b), a Hermitian matrix whose eigenvalues are all positive is positive definite, so \( \B \succ 0 \). By @thm-loewner-basic (d), \( \A \succ 0 \) and \( \B^{-1} \succeq \A^{-1} \). Put \( f(t) = -1/t \). By @def-function-of-normal-operator and the instance \( t \mapsto 1/t \) recalled above, \( f(\A) = -\A^{-1} \) and \( f(\B) = -\B^{-1} \). Hence
\[
f(\A) - f(\B) = \B^{-1} - \A^{-1} \ \succeq\ 0 ,
\]
which is the assertion. The size \( n \) was arbitrary, so \( f \) is operator monotone on \( (0, \infty) \).
:::

Two things make the whitening work, and they are worth separating. First, once one of the two matrices is \( \I \), the comparison \( \C \succeq \I \) can be settled eigenvalue by eigenvalue, because \( \I \) commutes with everything. Second, inversion gets along with congruence: \( (\S^{*}\M\S)^{-1} = \S^{-1}\M^{-1}(\S^{-1})^{*} \) is again a congruence, and that is what carries the conclusion back from \( \C \) to \( \A \). For a general \( f \) there is no such identity, since \( f(\S^{*}\M\S) \) is usually not a congruence of \( f(\M) \), so the argument does not simply transfer to other functions.

To build more examples out of these, one needs to know which ways of combining functions preserve the property.

:::: {#prp-operator-monotone-cone}
[Combining Operator Monotone Functions]

Let \( f \) and \( g \) be operator monotone on \( I \).

::: {.enumerate options="label=(\alph*)"}
1. For every \( c \ge 0 \) and every \( \alpha \in \nR \), the functions \( f + g \) and \( \alpha + cf \) are operator monotone on \( I \).
2. For every \( s \in \nR \), the translate \( t \mapsto f(t + s) \) is operator monotone on the interval \( I - s = \{ t - s : t \in I \} \).
:::
::::

::: {.proof}
(a) Let \( \A \succeq \B \) be Hermitian of the same size with spectra in \( I \). By @thm-functional-calculus-properties (b), \( (f + g)(\A) - (f + g)(\B) = \bigl(f(\A) - f(\B)\bigr) + \bigl(g(\A) - g(\B)\bigr) \). Both brackets are \( \succeq 0 \) by hypothesis, and for every \( \x \) the quadratic form of the sum is the sum of the two non-negative quadratic forms. So the sum is \( \succeq 0 \) by @def-positive-semidefinite. Likewise, using (b) and (a) of the same theorem, \( (\alpha + cf)(\A) - (\alpha + cf)(\B) = c\bigl(f(\A) - f(\B)\bigr) \), whose quadratic form is \( c \ge 0 \) times a non-negative one.

(b) Let \( g(t) = f(t + s) \) on \( I - s \), and let \( \A \) be Hermitian with spectrum in \( I - s \), with spectral resolution \( \A = \sum_j\mu_j\P_j \). By @thm-spectral-resolution (c) and (d),
\[
\A + s\I = \sum_j (\mu_j + s)\P_j ,
\]
and the numbers \( \mu_j + s \) are distinct. The \( \P_j \) are non-zero self-adjoint idempotents with \( \P_i\P_j = \0 \) for \( i \ne j \) and \( \sum_j\P_j = \I \) (@thm-spectral-resolution (b), (c)). So by @thm-spectral-resolution-unique this is the spectral resolution of \( \A + s\I \), whose spectrum \( \{\mu_j + s\} \) lies in \( I \). By @def-function-of-normal-operator, applied to each side,
\[
f(\A + s\I) = \sum_j f(\mu_j + s)\P_j = g(\A) .
\]
Now if \( \A \succeq \B \) with spectra in \( I - s \), then \( (\A + s\I) - (\B + s\I) = \A - \B \succeq 0 \), and both shifted matrices have spectra in \( I \). Hence \( g(\A) = f(\A + s\I) \succeq f(\B + s\I) = g(\B) \).
:::

Combining the last two propositions produces a whole one-parameter family. It will reappear in the final part of the section as the building block of every operator monotone function.

::: {#cor-shifted-inverse-operator-monotone}
[Shifted Reciprocals]

For every \( s \ge 0 \), the function \( t \mapsto -1/(t + s) \) is operator monotone on \( (0, \infty) \). For every \( s > 0 \), so is
\[
t \longmapsto \frac{t}{t + s} = 1 - \frac{s}{t + s} .
\]
:::

::: {.proof}
By @prp-inverse-operator-monotone and @prp-operator-monotone-cone (b), \( t \mapsto -1/(t + s) \) is operator monotone on \( (0, \infty) - s = (-s, \infty) \). Every Hermitian matrix with spectrum in \( (0, \infty) \) has spectrum in \( (-s, \infty) \), so it is in particular operator monotone on \( (0, \infty) \). For the second function, \( t/(t + s) = 1 + s\cdot\bigl(-1/(t + s)\bigr) \) with \( s > 0 \), so @prp-operator-monotone-cone (a) applies.
:::

The fourth example is the one that started the section, and it is already proved. By @prp-square-root-monotone, \( \A \succeq \B \succeq 0 \) implies \( \A^{1/2} \succeq \B^{1/2} \). A Hermitian matrix has spectrum in \( [0, \infty) \) exactly when it is \( \succeq 0 \) (@thm-psd-characterizations (b)), and \( \A^{1/2} \) is \( f(\A) \) for \( f(t) = t^{1/2} \). So Chapter 12 §05's proposition says precisely that **\( t \mapsto t^{1/2} \) is operator monotone on \( [0, \infty) \)**. It is not re-proved here. Its proof was a different kind of argument, an eigenvector of \( \A^{1/2} - \B^{1/2} \) pushed to a contradiction, and it too never needs \( \A \) and \( \B \) to commute.

**A non-example by minimal change.** The function \( t \mapsto t = t^1 \) is operator monotone on \( [0, \infty) \) by @prp-affine-operator-monotone. Raise the exponent from \( 1 \) to \( 2 \). The function is still increasing, still a polynomial, and still satisfies the case \( n = 1 \). What fails is the clause "for every \( n \)", already at \( n = 2 \), with the witness of @exm-loewner-not-monotone. Lowering the exponent from \( 1 \) to \( \tfrac12 \) instead keeps the property. Among the powers, then, the dividing line lies somewhere around the exponent \( 1 \). Chapter 12 §05 said where it lies exactly, and the last part of this section returns to that.

**Why "for every \( n \)".** Each size imposes its own condition, and the conditions differ. At \( n = 1 \), \( t \mapsto t^2 \) passes on \( [0, \infty) \) and at \( n = 2 \) it fails. A definition at one fixed size would admit functions that break at the next size, and it would not say what the functional calculus does to matrices in general. Requiring every size at once makes the class small enough to classify completely, which is what Loewner's theorem at the end of this section does. The name comes from the same place as the name of the order: both are Loewner's.

## Eigenvalues move monotonically for every increasing function

Operator monotonicity is a strong requirement, and a weaker one comes for free. §02 proved that the whole ordered list of eigenvalues respects the Loewner order: by @cor-loewner-eigenvalue-monotone, \( \A \succeq \B \) implies \( \lambda_i(\A) \ge \lambda_i(\B) \) for **every** \( i \). That paid the debt Chapter 12 §05 recorded after @thm-loewner-basic, and it holds with no hypothesis on commuting. Composing with an increasing \( f \) keeps it, once one knows what \( f \) does to the ordered list of eigenvalues.

::: {#lem-eigenvalues-of-a-function}
[The Eigenvalue List of an Increasing Function]

Let \( \A \in M_n(F) \) be Hermitian with \( \spec(\A) \subseteq I \), and let \( f \colon I \to \nR \) be increasing. Then \( f(\A) \) is Hermitian and
\[
\lambda_i\bigl(f(\A)\bigr) = f\bigl(\lambda_i(\A)\bigr) \qquad (i = 1, \dots, n) .
\]
:::

::: {.proof}
The matrix \( f(\A) \) is Hermitian by @thm-functional-calculus-properties (c). By @cor-spectral-complex-matrix (over \( \nC \)) or @cor-spectral-real-matrix (over \( \nR \)), there is an orthonormal basis \( (\q_1, \dots, \q_n) \) of \( F^n \) with \( \A\q_i = \lambda_i(\A)\q_i \). Let \( \A = \sum_j\mu_j\P_j \) be the spectral resolution, and fix \( i \). Exactly one of the distinct eigenvalues equals \( \lambda_i(\A) \); call it \( \mu_{j_0} \). Then \( \q_i \) lies in the eigenspace of \( \mu_{j_0} \), which is the image of \( \P_{j_0} \), so \( \P_{j_0}\q_i = \q_i \). For \( j \ne j_0 \), the eigenspace of \( \mu_{j_0} \) is orthogonal to that of \( \mu_j \) (@thm-spectral-resolution (a)), so \( \P_j\q_i = \0 \). By @def-function-of-normal-operator,
\[
f(\A)\q_i = \sum_j f(\mu_j)\P_j\q_i = f(\mu_{j_0})\q_i = f\bigl(\lambda_i(\A)\bigr)\q_i .
\]
Thus \( (\q_1, \dots, \q_n) \) is an orthonormal basis of eigenvectors of \( f(\A) \), and \( f(\lambda_1(\A)), \dots, f(\lambda_n(\A)) \) is its list of eigenvalues with multiplicity. Since \( \lambda_1(\A) \ge \dots \ge \lambda_n(\A) \) and \( f \) is increasing, this list is already in decreasing order. A decreasing list of all the eigenvalues with multiplicity is the list \( \lambda_1(f(\A)) \ge \dots \ge \lambda_n(f(\A)) \), so the two agree term by term.
:::

The lemma needs \( f \) increasing only for the order of the list. For a general \( f \), the numbers \( f(\lambda_i(\A)) \) are still the eigenvalues of \( f(\A) \), but they may have to be re-sorted. Two lines now give the eigenvalue-level statement.

::: {#prp-eigenvalue-monotone-increasing}
[Every Increasing Function Is Monotone on Eigenvalues]

Let \( f \colon I \to \nR \) be increasing, and let \( \A, \B \in M_n(F) \) be Hermitian with spectra in \( I \) and \( \A \succeq \B \). Then
\[
\lambda_i\bigl(f(\A)\bigr) \ \ge\ \lambda_i\bigl(f(\B)\bigr) \qquad \text{for every } i = 1, \dots, n .
\]
:::

::: {.proof}
By @cor-loewner-eigenvalue-monotone, \( \lambda_i(\A) \ge \lambda_i(\B) \) for every \( i \). Since \( f \) is increasing, \( f(\lambda_i(\A)) \ge f(\lambda_i(\B)) \). By @lem-eigenvalues-of-a-function, applied to \( \A \) and to \( \B \), the two sides are \( \lambda_i(f(\A)) \) and \( \lambda_i(f(\B)) \).
:::

So the squaring map, which is not operator monotone, is nevertheless monotone on eigenvalues. The Chapter 12 witness shows both at once.

::: {#exm-eigenvalues-of-squares}
[The Squares Are Not Ordered, but Their Eigenvalues Are]

Let \( \A = \begin{psmallmatrix} 2 & 1 \\ 1 & 1\end{psmallmatrix} \) and \( \B = \begin{psmallmatrix} 1 & 1 \\ 1 & 1\end{psmallmatrix} \), the pair of @exm-loewner-not-monotone, for which \( \A \succeq \B \succeq 0 \) and \( \A^2 \not\succeq \B^2 \). Compute the eigenvalues of \( \A^2 \) and \( \B^2 \) and compare them index by index.
:::

::: {.solution}
From @exm-loewner-not-monotone, \( \A^2 = \begin{psmallmatrix} 5 & 3 \\ 3 & 2\end{psmallmatrix} \) and \( \B^2 = \begin{psmallmatrix} 2 & 2 \\ 2 & 2\end{psmallmatrix} \). The first has trace \( 7 \) and determinant \( 10 - 9 = 1 \), so its eigenvalues are the roots of \( x^2 - 7x + 1 \):
\[
\lambda_1(\A^2) = \frac{7 + 3\sqrt5}{2} \approx 6.854, \qquad \lambda_2(\A^2) = \frac{7 - 3\sqrt5}{2} \approx 0.146 .
\]
The second has trace \( 4 \) and determinant \( 0 \), so \( \lambda_1(\B^2) = 4 \) and \( \lambda_2(\B^2) = 0 \). Index by index: \( \frac{7 + 3\sqrt5}{2} \ge 4 \) because \( 3\sqrt5 \ge 1 \), and \( \frac{7 - 3\sqrt5}{2} \ge 0 \) because \( 49 \ge 45 \). So \( \lambda_i(\A^2) \ge \lambda_i(\B^2) \) for \( i = 1, 2 \), as @prp-eigenvalue-monotone-increasing predicts for the increasing function \( t \mapsto t^2 \) on \( [0, \infty) \). Nevertheless \( \A^2 - \B^2 \) is not \( \succeq 0 \).
:::

So for every increasing \( f \), the eigenvalues of \( f(\A) \) dominate those of \( f(\B) \) one index at a time. What operator monotonicity adds is that the *matrices* are ordered, and the example shows that this is strictly more.

::: {.warning}
**Eigenvalues in order do not make matrices in order.** It is tempting to read @prp-eigenvalue-monotone-increasing as "almost" operator monotonicity. It is not, because \( \lambda_i(\M) \ge \lambda_i(\N) \) for every \( i \) does **not** imply \( \M \succeq \N \). Take \( \M = \diag(1, 0) \) and \( \N = \diag(0, 1) \): they have the same eigenvalues \( 1 \ge 0 \), yet \( \M - \N = \diag(1, -1) \) is indefinite. The Loewner order sees the eigenvectors as well as the eigenvalues, and the eigenvalue list forgets them.
:::

## Operator convexity, and where the two notions part

Operator convexity is the second notion of @def-operator-monotone, and one might expect it to behave like operator monotonicity. It does not: the function that fails to be operator monotone turns out to be operator convex.

::: {#prp-square-operator-convex}
[The Square Is Operator Convex]

The function \( t \mapsto t^2 \) is operator convex on \( \nR \). Explicitly: for Hermitian \( \A, \B \in M_n(F) \) and \( \theta \in [0, 1] \),
\[
\begin{aligned}
\theta\A^2 + (1 - \theta)\B^2 &- \bigl(\theta\A + (1 - \theta)\B\bigr)^2 \\
  &= \theta(1 - \theta)(\A - \B)^2 \ \succeq\ 0 .
\end{aligned}
\]
:::

::: {.idea}
For numbers, \( \theta a^2 + (1-\theta)b^2 - (\theta a + (1-\theta)b)^2 = \theta(1-\theta)(a - b)^2 \), which is a variance. The matrix version of the expansion produces \( \A\B + \B\A \) where the number version has \( 2ab \), and that is exactly the cross term of \( (\A - \B)^2 = \A^2 - \A\B - \B\A + \B^2 \). So this time non-commutativity cancels itself out and costs nothing. The square of a Hermitian matrix is \( \succeq 0 \), which finishes the proof.
:::

::: {.proof}
By @thm-functional-calculus-properties (a), the function \( t \mapsto t^2 \) sends a Hermitian matrix to its square, so the displayed identity is what @def-operator-monotone (b) requires. Expanding, and keeping the order of every product,
\[
\begin{aligned}
\bigl(\theta\A + (1-\theta)\B\bigr)^2
  &= \theta^2\A^2 + \theta(1-\theta)(\A\B + \B\A) \\
  &\quad + (1-\theta)^2\B^2 .
\end{aligned}
\]
Subtracting this from \( \theta\A^2 + (1-\theta)\B^2 \), and using \( \theta - \theta^2 = \theta(1-\theta) = (1-\theta) - (1-\theta)^2 \),
\[
\begin{aligned}
\theta\A^2 + (1-\theta)\B^2 - \bigl(\theta\A + (1-\theta)\B\bigr)^2
  &= \theta(1-\theta)\bigl(\A^2 - \A\B - \B\A + \B^2\bigr) \\
  &= \theta(1-\theta)(\A - \B)^2 .
\end{aligned}
\]
The matrix \( \D = \A - \B \) is Hermitian, so \( \D^2 = \D^{*}\D \succeq 0 \) by @thm-psd-characterizations (c). Since \( \theta(1-\theta) \ge 0 \), the quadratic form of \( \theta(1-\theta)\D^2 \) is non-negative, which proves the inequality.
:::

The contrast is now complete, and it runs both ways.

- \( t \mapsto t^2 \) is **operator convex but not operator monotone** on \( [0, \infty) \): @prp-square-operator-convex and @exm-loewner-not-monotone.
- \( t \mapsto -1/t \) is **operator monotone but not operator convex** on \( (0, \infty) \): @prp-inverse-operator-monotone, and at \( n = 1 \) the scalar function \( -1/t \) is not even convex, since with \( a = 1 \), \( b = 3 \) and \( \theta = \tfrac12 \) the value at the midpoint is \( -\tfrac12 \), above the chord's \( -\tfrac23 \).

So neither notion implies the other. Each implies its scalar version (increasing, convex) by taking \( n = 1 \), and they strengthen those versions in different directions. Exercise C2 adds that \( t \mapsto 1/t \) is operator convex on \( (0, \infty) \), so \( -1/t \) is operator monotone *and* operator concave there.

## What is not proved here

The question the section opened with has a complete answer, and this chapter does not prove it. Here is the statement, so that the reader knows what the answer looks like and which of the facts above are pieces of it.

:::: {#thm-loewner-statement}
[Loewner's Theorem, Statement]

Let \( f \colon (0, \infty) \to \nR \). The following are equivalent.

::: {.enumerate options="label=(\roman*)"}
1. \( f \) is operator monotone on \( (0, \infty) \).
2. There are \( \alpha \in \nR \), \( \beta \ge 0 \) and a positive measure \( \nu \) on \( [0, \infty) \) with \( \int_{[0,\infty)} \frac{\dd\nu(s)}{1 + s^2} < \infty \), such that for every \( t > 0 \)
\[
\begin{aligned}
f(t) &= \alpha + \beta t \\
  &\quad + \int_{[0, \infty)} \Bigl(\frac{s}{1 + s^2} - \frac{1}{t + s}\Bigr)\, \dd\nu(s) .
\end{aligned}
\]
3. \( f \) is the restriction to \( (0, \infty) \) of a function that is analytic on \( \nC \setminus (-\infty, 0] \) and sends every point of the upper half-plane \( \{ z : \operatorname{Im} z > 0 \} \) to a point with non-negative imaginary part.
:::
::::

We do not prove this theorem here. Its proof needs complex analysis and some measure theory, which lie outside Chapter 15's list (A1)–(A6); Chapter 20 proves it. Nothing in this chapter depends on it.

Read (ii) against what was proved above. The functions it superposes are \( t \mapsto -1/(t + s) \) for \( s \ge 0 \), the translates of \( -1/t \) that @cor-shifted-inverse-operator-monotone showed to be operator monotone. The constants \( s/(1 + s^2) \) do not depend on \( t \) and are there only to make the integral converge. The term \( \alpha + \beta t \) is @prp-affine-operator-monotone. So the theorem says that **the examples of this section are, in a precise sense, all the examples there are**: every operator monotone function on \( (0, \infty) \) is an increasing affine function plus a non-negative superposition of shifted reciprocals. The easy direction, (ii) \( \Rightarrow \) (i), is essentially @prp-operator-monotone-cone applied to an integral rather than a finite sum. What this book lacks is the analysis that carries the Loewner order through an integral, which is not on the list (A1)–(A6) in Chapter 15's introduction. The hard direction, (i) \( \Rightarrow \) (ii), is the classification itself.

Condition (iii) answers the opening question in one line. For \( z \) in the upper half-plane, \( z^{1/2} \) (the branch that is positive on \( (0, \infty) \)) halves the argument of \( z \), so its argument stays between \( 0 \) and \( \pi/2 \) and \( z^{1/2} \) stays in the upper half-plane. The square doubles the argument, which can pass \( \pi \). **The square root keeps the upper half-plane, and the square folds it over.**

::: {.check}
Find a point \( z \) of the upper half-plane whose square has negative imaginary part.
:::

::: {.solution}
Take \( z = -1 + i \), with \( \operatorname{Im} z = 1 > 0 \). Then \( z^2 = 1 - 2i + i^2 = -2i \), with imaginary part \( -2 < 0 \). So \( z \mapsto z^2 \) fails condition (iii) of @thm-loewner-statement, consistently with @exm-loewner-not-monotone.
:::

The same test settles the powers \( t \mapsto t^p \). For \( 0 < p < 1 \), the function \( z^p \) multiplies the argument by \( p \) and keeps the upper half-plane, and indeed for \( t > 0 \) (a standard integral, not proved here)
\[
t^p = \frac{\sin p\pi}{\pi}\int_0^\infty s^{p-1}\,\frac{t}{t + s}\, \dd s ,
\]
a positive superposition of the functions \( t/(t + s) \) of @cor-shifted-inverse-operator-monotone. For \( p > 1 \), the argument of \( z^p \) passes \( \pi \) for some \( z \) in the upper half-plane, and the test fails. This is the dividing line at exponent \( 1 \) that Chapter 12 §05 announced. Both halves, that \( t^p \) is operator monotone on \( (0, \infty) \) for every \( p \in (0, 1) \) and that it is not for any \( p > 1 \), are proved in Chapter 20, with Loewner's theorem. What is proved so far is the case \( p = \tfrac12 \) (@prp-square-root-monotone) and, by applying it repeatedly, the cases \( p = 1/2^k \) (exercise C1).

## Summary and transfer

The chapter began with a list of eigenvalues that the book had been able to *order* since Chapter 12 without being able to *describe*. It ends with each eigenvalue described as an optimization, and with a set of comparison theorems that follow from that description. Five moves did the work, and each transfers beyond this chapter.

- **The dimension count.** Two subspaces of an \( n \)-dimensional space whose dimensions add to more than \( n \) share a non-zero vector. This one line drives Courant–Fischer (@thm-courant-fischer) and Weyl's inequalities (§03) directly, and through Courant–Fischer everything after them. *Transfer:* whenever an extremal problem over vectors has to be compared with a fixed subspace, count dimensions before computing anything.
- **Min–max.** Describe a quantity as a minimum over subspaces of a maximum over vectors, and prove it with two inequalities of different characters: one exhibits a witness subspace and computes, and the other takes an arbitrary subspace and intersects it with a span of eigenvectors. Applying the result to \( -\A \) gives the dual form for free. *Transfer:* a description that names no eigenvector is what makes two different matrices comparable. The same shape describes singular values (§09) and inertia (§10).
- **Compress and interlace.** Restricting a Hermitian form to a subspace gives a smaller Hermitian matrix whose eigenvalues are trapped by the original's: compressing to a \( k \)-dimensional subspace puts \( \lambda_i \) of the piece between \( \lambda_i \) and \( \lambda_{i+n-k} \) of the whole, which are consecutive when \( k = n - 1 \). Deleting a row and column (§04), compressing to an orthonormal frame (§06) and deleting a row or a column of a rectangular matrix (§09) are all this move; adding a rank-one term (§05) reaches the same interlaced picture by a different route, the Loewner order together with Weyl's rank bound. *Transfer:* to bound the spectrum of a piece, look for the whole of which it is a compression.
- **Perturb in order.** Compare \( \lambda_i(\A + \E) \) with \( \lambda_i(\A) \) index by index, never "each eigenvalue with its nearest neighbor". For Hermitian perturbations the Lipschitz constant is \( 1 \) in the spectral norm, independent of \( n \), of the gaps and of the eigenvectors (§03). For singular values it needs no hypothesis on \( \E \) at all (§09). *Transfer:* where the Jordan block of Chapter 15 §07 showed that eigenvalues of general matrices can move like \( \varepsilon^{1/k} \), the Hermitian and singular-value problems are perfectly conditioned. Reduce a question to one of them whenever possible.
- **Majorize.** When the right comparison is between *sums* of the largest entries rather than individual ones, compare partial sums of decreasing rearrangements. The diagonal of a Hermitian matrix is majorized by its spectrum, and by the Schur–Horn theorem majorization describes the possible diagonals *exactly* (§08); and the Ky Fan and Lidskii sums (§§06–07) are of the same type. *Transfer:* a family of partial-sum inequalities indexed by \( k \), together with equality of the totals, is a majorization in disguise, and writing it as one lets the whole family be used at once.

Two supporting moves recur under these five: **apply the result to \( -\A \)**, which turns every max–min into a min–max and every top-\( k \) statement into a bottom-\( k \) one, and **reduce singular values to eigenvalues**, through \( \A^{*}\A \) or the Hermitian dilation. This section also reused a move from Chapter 12 §05, **whiten, then compare**: use a congruence to make one of the two matrices \( \I \). It works for \( t \mapsto -1/t \) because inversion turns a congruence into a congruence, and not for a general \( f \).

The chapter also paid a series of promises made in earlier chapters, some of them long ago.

| The promise | Made in | Paid by |
|---|---|---|
| The maximization route to eigenvalues "returns in Chapter 16, where the Rayleigh quotient and the Courant–Fischer theorem describe every eigenvalue of a self-adjoint operator by optimization" | Chapter 11 §02 | §01 (The Rayleigh quotient) and §02 (The min–max theorem), @thm-courant-fischer |
| "Chapter 16 characterizes the eigenvalues of a Hermitian matrix as maxima and minima of \( \inner{\A\x}{\x} \) — at which point the test becomes the theory" | Chapter 12 §12 | §01 and §02, @thm-courant-fischer |
| \( \A \succeq \B \) gives \( \lambda_i(\A) \ge \lambda_i(\B) \) for **every** \( i \), not only \( i = 1 \) and \( i = n \) as in @thm-loewner-basic (b) | Chapter 12 §05 | §02, @cor-loewner-eigenvalue-monotone |
| "The eigenvalues of a Hermitian matrix move by at most \( \norm{\E}_2 \) under a Hermitian perturbation" | Chapter 15 §07 | §03 (How far eigenvalues move), Weyl's perturbation bound |
| @lem-orthonormal-capture-bound is "the extreme case of a family of statements about sums of the largest eigenvalues" | Chapter 12 §10 | §06 (Subspaces and Sums of Eigenvalues), Ky Fan's theorem, of which it is a special case |
| The second half of the approximation theorem, in the spectral norm | Chapter 12 §10 and Chapter 15 §08 | §09 (The same theory for singular values), Eckart–Young in the spectral norm |
| Interlacing of the zeros of consecutive orthogonal polynomials, "Chapter 16's business" | Chapter 10 §10 | §04 (Deleting a row and a column): strict interlacing, through the bordered-matrix criterion |
| The operator monotone functions named in Chapter 12 §05 | Chapter 12 §05 | §11: definition and first examples; \( t^s \), \( \log t \) and Loewner's theorem remain Chapter 20's, as that section said |

Four earlier theorems also received second proofs from the variational side, each of which shows something the first proof did not. The positivity of principal submatrices of a positive semidefinite matrix now follows from interlacing (§04, Deleting a row and a column). Hadamard's inequality @thm-hadamard-inequality follows from AM–GM after a diagonal scaling, with Schur's theorem supplying the equal totals (§08, The diagonal and the spectrum). Sylvester's law of inertia @thm-sylvester-inertia is now a statement about the dimensions of subspaces, with no basis in it (§10, Inertia, again and additively). And the block test @thm-block-psd-schur is now a consequence of inertia additivity (§10).

Some things the chapter did not do. Bounds for the eigenvalues of non-Hermitian matrices under perturbation, beginning with Bauer–Fike, are Chapter 19's. Chapter 20 has Loewner's theorem with the powers \( t^p \), Schur-concave functions, the strongest form of Lidskii's inequality, and Eckart–Young in every unitarily invariant norm. The variational principle itself, though, is now a tool the book can use without comment: an eigenvalue of a Hermitian matrix is a min–max, and comparison theorems follow from that.

## Exercises

### A. Check your understanding

:::: {#exr-monotone-matrix-functions-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define "\( f \) is operator monotone on \( I \)", and say what the clause "for every \( n \)" ranges over.
2. Explain why an operator monotone function is increasing, and name an increasing function that is not operator monotone.
3. Decide whether the following is correct, and justify your answer: if \( f \colon I \to \nR \) is increasing and \( \A \succeq \B \) are Hermitian with spectra in \( I \), then \( \lambda_i(f(\A)) \ge \lambda_i(f(\B)) \) for every \( i \).
4. Decide whether the following is correct, and justify your answer: if \( \A, \B \) are Hermitian of the same size and \( \lambda_i(\A) \ge \lambda_i(\B) \) for every \( i \), then \( \A \succeq \B \).
5. Which of \( t \mapsto t^2 \) and \( t \mapsto -1/t \) is operator monotone on \( (0, \infty) \), and which is operator convex there?
6. What does this section prove about Loewner's theorem?
:::
::::

::: {.solution}
(a) For every \( n \ge 1 \) and all Hermitian \( \A, \B \in M_n(F) \) with spectra in \( I \), \( \A \succeq \B \) implies \( f(\A) \succeq f(\B) \), where \( f(\A) \) is formed by @def-function-of-normal-operator (@def-operator-monotone (a)). The clause ranges over all matrix sizes: the implication must hold for \( 1 \times 1 \), \( 2 \times 2 \), \( 3 \times 3 \), … matrices simultaneously.

(b) Taking \( n = 1 \) gives \( f(t) \ge f(s) \) whenever \( t \ge s \) in \( I \) (@prp-operator-monotone-increasing). The function \( t \mapsto t^2 \) on \( [0, \infty) \) is increasing and is not operator monotone (@exm-loewner-not-monotone).

(c) Correct. This is @prp-eigenvalue-monotone-increasing: @cor-loewner-eigenvalue-monotone orders the eigenvalues of \( \A \) and \( \B \) index by index, \( f \) preserves each inequality, and @lem-eigenvalues-of-a-function identifies \( f(\lambda_i(\A)) \) with \( \lambda_i(f(\A)) \).

(d) Incorrect. \( \diag(1, 0) \) and \( \diag(0, 1) \) have the same eigenvalues, but their difference \( \diag(1, -1) \) is indefinite, so neither dominates the other.

(e) \( t \mapsto -1/t \) is operator monotone on \( (0, \infty) \) (@prp-inverse-operator-monotone) and is not operator convex, since already the scalar function is not convex: at \( 1 \), \( 3 \) and their midpoint \( 2 \), \( -\tfrac12 > \tfrac12(-1 - \tfrac13) = -\tfrac23 \). \( t \mapsto t^2 \) is operator convex (@prp-square-operator-convex) and not operator monotone on \( (0, \infty) \). The witness of @exm-loewner-not-monotone has \( 0 \) in the spectrum of \( \B \), but the pair \( \A = \begin{psmallmatrix} 3 & 1 \\ 1 & 1\end{psmallmatrix} \succeq \B = \begin{psmallmatrix} 2 & 1 \\ 1 & 1\end{psmallmatrix} \succ 0 \) works: \( \A^2 - \B^2 = \begin{psmallmatrix} 5 & 1 \\ 1 & 0\end{psmallmatrix} \) has determinant \( -1 \).

(f) Only the statement (@thm-loewner-statement) and the fact that its building blocks \( t \mapsto -1/(t + s) \) are operator monotone (@cor-shifted-inverse-operator-monotone). The theorem itself is proved in Chapter 20.
:::

### B. Practice

:::: {#exr-monotone-matrix-functions-b1}
[B1: Which are operator monotone?]

Determine which of the following functions are operator monotone on the interval given. Justify your answer.

::: {.enumerate options="label=(\roman*)"}
1. \( f(t) = 5 + 4t \) on \( \nR \).
2. \( f(t) = 3 - 2t \) on \( \nR \).
3. \( f(t) = 2 - \dfrac{3}{t + 1} \) on \( (0, \infty) \).
4. \( f(t) = \dfrac{t}{t + 2} \) on \( (0, \infty) \).
5. \( f(t) = t^2 \) on \( [0, \infty) \).
:::
::::

::: {.solution}
(i) Operator monotone, by @prp-affine-operator-monotone with \( \beta = 4 \ge 0 \).

(ii) Not operator monotone. It is not increasing, since \( f(1) = 1 < 3 = f(0) \), so it fails at \( n = 1 \) with \( \A = (1) \succeq \B = (0) \); compare @prp-operator-monotone-increasing.

(iii) Operator monotone. By @cor-shifted-inverse-operator-monotone with \( s = 1 \), \( t \mapsto -1/(t + 1) \) is operator monotone on \( (0, \infty) \), and \( f = 2 + 3\cdot\bigl(-1/(t + 1)\bigr) \) with \( 3 \ge 0 \), so @prp-operator-monotone-cone (a) applies.

(iv) Operator monotone, by @cor-shifted-inverse-operator-monotone with \( s = 2 > 0 \).

(v) Not operator monotone: @exm-loewner-not-monotone gives \( \A \succeq \B \succeq 0 \), with spectra \( \{(3\pm\sqrt5)/2\} \) and \( \{0, 2\} \) in \( [0, \infty) \), and \( \A^2 \not\succeq \B^2 \).
:::

:::: {#exr-monotone-matrix-functions-b2}
[B2: One pair, three functions]

Let
\[
\A = \begin{pmatrix} 3 & 1 \\ 1 & 1 \end{pmatrix}, \qquad \B = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} .
\]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \A \succeq \B \succ 0 \).
2. Compute \( \A^{-1} \) and \( \B^{-1} \), and verify directly that \( \B^{-1} \succeq \A^{-1} \), as @prp-inverse-operator-monotone predicts.
3. Show that \( \A^2 \not\succeq \B^2 \) by exhibiting a vector \( \x \) with \( \x\tp(\A^2 - \B^2)\x < 0 \).
4. Compute the eigenvalues of \( \A^2 \) and \( \B^2 \), and verify that \( \lambda_i(\A^2) \ge \lambda_i(\B^2) \) for \( i = 1, 2 \). Hence explain which result of this section (c) and (d) illustrate together.
:::
::::

::: {.solution}
(a) \( \A - \B = \diag(1, 0) \), a diagonal matrix with non-negative entries, so \( \A - \B \succeq 0 \) and \( \A \succeq \B \). The leading principal minors of \( \B \) are \( 2 \) and \( 2 - 1 = 1 \), both positive, so \( \B \succ 0 \) by Sylvester's criterion (@thm-pd-characterizations (d)).

(b) \( \det\A = 2 \) and \( \det\B = 1 \), so
\[
\A^{-1} = \frac12\begin{pmatrix} 1 & -1 \\ -1 & 3 \end{pmatrix}, \qquad
\B^{-1} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}, \qquad
\B^{-1} - \A^{-1} = \frac12\begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix} .
\]
For every \( \x \in \nR^2 \), \( \x\tp(\B^{-1} - \A^{-1})\x = \tfrac12(x_1 - x_2)^2 \ge 0 \), so \( \B^{-1} \succeq \A^{-1} \).

(c) \( \A^2 = \begin{psmallmatrix} 10 & 4 \\ 4 & 2 \end{psmallmatrix} \) and \( \B^2 = \begin{psmallmatrix} 5 & 3 \\ 3 & 2 \end{psmallmatrix} \), so \( \A^2 - \B^2 = \begin{psmallmatrix} 5 & 1 \\ 1 & 0 \end{psmallmatrix} \), with determinant \( -1 < 0 \). With \( \x = (1, -3) \),
\[
\x\tp(\A^2 - \B^2)\x = 5 + 2\cdot(1)(-3) + 0 = -1 < 0 .
\]

(d) \( \A^2 \) has trace \( 12 \) and determinant \( (\det\A)^2 = 4 \), so its eigenvalues are \( 6 \pm \sqrt{32} = 6 \pm 4\sqrt2 \), approximately \( 11.657 \) and \( 0.343 \). \( \B^2 \) has trace \( 7 \) and determinant \( 1 \), so its eigenvalues are \( (7 \pm 3\sqrt5)/2 \), approximately \( 6.854 \) and \( 0.146 \). For \( i = 1 \), \( 12 + 8\sqrt2 \ge 7 + 3\sqrt5 \) because \( 8\sqrt2 > 3\sqrt5 \). For \( i = 2 \), \( 12 - 8\sqrt2 \ge 7 - 3\sqrt5 \) is \( 5 + 3\sqrt5 \ge 8\sqrt2 \). Both sides are positive, and squaring gives \( 70 + 30\sqrt5 \ge 128 \), that is \( \sqrt5 \ge \tfrac{29}{15} \), which holds because \( 5 \ge \tfrac{841}{225} \). Hence (c) and (d) together illustrate @prp-eigenvalue-monotone-increasing and the warning after it: the increasing function \( t \mapsto t^2 \) orders the eigenvalues but not the matrices.
:::

:::: {#exr-monotone-matrix-functions-b3}
[B3: The convexity identity in numbers]

With \( \A \) and \( \B \) as in B2 and \( \theta = \tfrac12 \), compute
\[
\M = \tfrac12\A^2 + \tfrac12\B^2 - \bigl(\tfrac12\A + \tfrac12\B\bigr)^2
\]
directly, confirm that \( \M = \tfrac14(\A - \B)^2 \), and hence conclude that \( \bigl(\tfrac12(\A + \B)\bigr)^2 \preceq \tfrac12(\A^2 + \B^2) \).
::::

::: {.solution}
From B2, \( \tfrac12\A^2 + \tfrac12\B^2 = \tfrac12\begin{psmallmatrix} 15 & 7 \\ 7 & 4 \end{psmallmatrix} = \begin{psmallmatrix} 15/2 & 7/2 \\ 7/2 & 2 \end{psmallmatrix} \). Next \( \tfrac12(\A + \B) = \begin{psmallmatrix} 5/2 & 1 \\ 1 & 1 \end{psmallmatrix} \), whose square is
\[
\begin{pmatrix} \tfrac{25}{4} + 1 & \tfrac52 + 1 \\ \tfrac52 + 1 & 1 + 1 \end{pmatrix}
= \begin{pmatrix} \tfrac{29}{4} & \tfrac72 \\ \tfrac72 & 2 \end{pmatrix} .
\]
Hence \( \M = \begin{psmallmatrix} 15/2 - 29/4 & 0 \\ 0 & 0 \end{psmallmatrix} = \diag(\tfrac14, 0) \). On the other side, \( \A - \B = \diag(1, 0) \), so \( \tfrac14(\A - \B)^2 = \diag(\tfrac14, 0) = \M \), as @prp-square-operator-convex says with \( \theta(1 - \theta) = \tfrac14 \). Since \( \diag(\tfrac14, 0) \) is diagonal with non-negative entries, \( \M \succeq 0 \), which is the displayed inequality.
:::

### C. Going deeper

:::: {#exr-monotone-matrix-functions-c1}
[C1: Iterated square roots]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \A \succeq \B \succeq 0 \). Prove that \( \A^{1/4} \succeq \B^{1/4} \), where \( \A^{1/4} \) is \( f(\A) \) for \( f(t) = t^{1/4} \) on \( [0, \infty) \).
2. Deduce that \( t \mapsto t^{1/2^k} \) is operator monotone on \( [0, \infty) \) for every integer \( k \ge 0 \).
3. Explain why the argument of (b) cannot reach \( t \mapsto t^{3/4} \), and say where the operator monotonicity of \( t^p \) for every \( p \in (0, 1) \) is proved.
:::

*Hint for (a): the positive square root is unique.*
::::

::: {.solution}
(a) Let \( g(t) = t^{1/4} \) on \( [0, \infty) \). Since \( \A \succeq 0 \), its spectrum lies in \( [0, \infty) \) (@thm-psd-characterizations (b)), and \( g(\A) = \sum_j\mu_j^{1/4}\P_j \) is Hermitian with non-negative eigenvalues by @thm-functional-calculus-properties (c) and (d), so \( g(\A) \succeq 0 \). By @thm-functional-calculus-properties (b), \( g(\A)^2 = (g^2)(\A) \), and \( g^2(t) = t^{1/2} \), so \( g(\A)^2 = \A^{1/2} \). By the uniqueness in @thm-psd-characterizations (d), applied to \( \A^{1/2} \succeq 0 \), \( g(\A) \) is the positive square root of \( \A^{1/2} \): \( \A^{1/4} = (\A^{1/2})^{1/2} \). The same holds for \( \B \). Now @prp-square-root-monotone applied to \( \A \succeq \B \succeq 0 \) gives \( \A^{1/2} \succeq \B^{1/2} \), and \( \B^{1/2} \succeq 0 \) by @thm-psd-square-root. Applying @prp-square-root-monotone again, to \( \A^{1/2} \succeq \B^{1/2} \succeq 0 \), gives \( (\A^{1/2})^{1/2} \succeq (\B^{1/2})^{1/2} \), that is \( \A^{1/4} \succeq \B^{1/4} \).

(b) Induction on \( k \). For \( k = 0 \) the function is \( t \mapsto t \), operator monotone by @prp-affine-operator-monotone. Suppose \( \A^{1/2^k} \succeq \B^{1/2^k} \) whenever \( \A \succeq \B \succeq 0 \). The argument of (a), with \( t^{1/2^{k+1}} \) in place of \( t^{1/4} \) and \( t^{1/2^k} \) in place of \( t^{1/2} \), shows that \( \A^{1/2^{k+1}} = (\A^{1/2^k})^{1/2} \), and similarly for \( \B \). Both \( \A^{1/2^k} \) and \( \B^{1/2^k} \) are \( \succeq 0 \), so @prp-square-root-monotone applied to \( \A^{1/2^k} \succeq \B^{1/2^k} \succeq 0 \) gives \( \A^{1/2^{k+1}} \succeq \B^{1/2^{k+1}} \).

(c) Each step of (b) takes a square root, which halves the exponent. Starting from \( 1 \), the exponents reached are exactly \( 1, \tfrac12, \tfrac14, \dots \), and \( \tfrac34 \) is not among them. The operator monotonicity of \( t^p \) for every \( p \in (0, 1) \) needs a new idea, an integral representation of the kind in @thm-loewner-statement, and it is proved in Chapter 20.
:::

:::: {#exr-monotone-matrix-functions-c2}
[C2: The reciprocal is operator convex]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \G \in M_n(F) \) with \( \G \succ 0 \). Prove that the \( 2n \times 2n \) matrix \( \begin{pmatrix} \G & \I_n \\ \I_n & \G^{-1} \end{pmatrix} \) is Hermitian and \( \succeq 0 \).
2. Let \( \A, \B \succ 0 \) be of the same size and \( \theta \in [0, 1] \). Prove that
\[
\bigl(\theta\A + (1 - \theta)\B\bigr)^{-1} \ \preceq\ \theta\A^{-1} + (1 - \theta)\B^{-1} ,
\]
that is, \( t \mapsto 1/t \) is operator convex on \( (0, \infty) \).
3. Deduce that \( t \mapsto -1/t \) is both operator monotone and operator concave on \( (0, \infty) \).
:::

*Hint: Schur complements.*
::::

::: {.solution}
(a) \( \G \) is Hermitian, and so is \( \G^{-1} \), since \( (\G^{-1})^{*} = (\G^{*})^{-1} = \G^{-1} \). The off-diagonal blocks are \( \I_n \) and \( \I_n^{*} = \I_n \), so the block matrix \( \M_{\G} \) is Hermitian. Its corner \( \G \) is \( \succ 0 \), and its Schur complement is
\[
\M_{\G}/\G = \G^{-1} - \I_n^{*}\G^{-1}\I_n = \0 \succeq 0 .
\]
By @thm-block-psd-schur (b), \( \M_{\G} \succeq 0 \).

(b) Put \( \C = \theta\A + (1 - \theta)\B \). For \( \x \ne \0 \), \( \inner{\C\x}{\x} = \theta\inner{\A\x}{\x} + (1 - \theta)\inner{\B\x}{\x} \). Both inner products are \( > 0 \), and \( \theta \) and \( 1 - \theta \) are \( \ge 0 \) and not both zero, so the sum is \( > 0 \). Thus \( \C \succ 0 \). By (a), \( \M_{\A} \succeq 0 \) and \( \M_{\B} \succeq 0 \), so for every \( \y \in F^{2n} \) the quadratic form of
\[
\theta\M_{\A} + (1 - \theta)\M_{\B} = \begin{pmatrix} \C & \I_n \\ \I_n & \theta\A^{-1} + (1 - \theta)\B^{-1} \end{pmatrix}
\]
is \( \theta\inner{\M_{\A}\y}{\y} + (1 - \theta)\inner{\M_{\B}\y}{\y} \ge 0 \), and this block matrix is \( \succeq 0 \). Its corner \( \C \) is \( \succ 0 \), so @thm-block-psd-schur (b) gives
\[
\theta\A^{-1} + (1 - \theta)\B^{-1} - \C^{-1} \ \succeq\ 0 ,
\]
which is the claim. Since \( t \mapsto 1/t \) sends a positive definite matrix to its inverse (@def-function-of-normal-operator), and a Hermitian matrix has spectrum in \( (0, \infty) \) exactly when it is \( \succ 0 \) (@thm-pd-characterizations (b)), this is @def-operator-monotone (b) for \( f(t) = 1/t \).

(c) Operator monotone by @prp-inverse-operator-monotone. Operator concave by definition, because its negative \( t \mapsto 1/t \) is operator convex by (b).
:::

:::: {#exr-monotone-matrix-functions-c3}
[C3: The cube needs its own witness]

::: {.enumerate options="label=(\alph*)"}
1. With \( \A \) and \( \B \) as in B2, show that \( \A^3 \not\succeq \B^3 \). Conclude that \( t \mapsto t^3 \) is not operator monotone on \( [0, \infty) \).
2. One might hope to deduce (a) from the failure of \( t \mapsto t^2 \). Suppose \( t \mapsto t^3 \) were operator monotone on \( [0, \infty) \). Applying it and \( t \mapsto t^{1/2} \) (@prp-square-root-monotone) to both sides of \( \A \succeq \B \succeq 0 \), repeatedly and in any order, yields inequalities \( \A^q \succeq \B^q \) for certain exponents \( q \). Show that every such \( q \) has the form \( 3^j/2^k \) with integers \( j, k \ge 0 \), and that \( 2 \) never has this form. Explain why this means (a) needed a witness of its own.
:::
::::

::: {.solution}
(a) From B2, \( \A \succeq \B \succeq 0 \), with spectra in \( (0, \infty) \). Multiplying the squares of B2 once more,
\[
\A^3 = \begin{pmatrix} 34 & 14 \\ 14 & 6 \end{pmatrix}, \qquad
\B^3 = \begin{pmatrix} 13 & 8 \\ 8 & 5 \end{pmatrix}, \qquad
\A^3 - \B^3 = \begin{pmatrix} 21 & 6 \\ 6 & 1 \end{pmatrix} .
\]
The determinant is \( 21 - 36 = -15 < 0 \), so the difference is indefinite. Explicitly, with \( \x = (1, -5) \),
\[
\x\tp(\A^3 - \B^3)\x = 21 + 2\cdot 6\cdot(-5) + 25 = -14 < 0 .
\]
By @thm-functional-calculus-properties (a), \( t \mapsto t^3 \) sends \( \A \) to \( \A^3 \), so it is not operator monotone on \( [0, \infty) \).

(b) Start from \( \A = \A^{3^0/2^0} \). Taking the square root of \( \A^{q} \) gives \( \A^{q/2} \), and cubing it gives \( \A^{3q} \), by @thm-functional-calculus-properties (b) and the uniqueness of the positive square root, as in C1 (a); likewise for \( \B \). If \( q = 3^j/2^k \), the results are \( 3^j/2^{k+1} \) and \( 3^{j+1}/2^k \), of the same form. By induction on the number of steps, every exponent reached has the form \( 3^j/2^k \). If \( 2 = 3^j/2^k \), then \( 3^j = 2^{k+1} \), and the left side is odd while the right side is even, since \( k + 1 \ge 1 \). So no exponent reached equals \( 2 \). The hypothetical operator monotonicity of the cube therefore cannot be converted, by these means, into that of the square. The failure of the square does not formally imply the failure of the cube, and (a) had to find a pair of matrices of its own.
:::
