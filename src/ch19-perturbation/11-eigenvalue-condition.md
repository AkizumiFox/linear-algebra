# Condition Numbers of Eigenvalues

The Bauer–Fike theorem of §04 bounds the movement of every eigenvalue of a diagonalizable matrix at once, by \( \kappa_2(\X)\norm{\E}_2 \) (@thm-bauer-fike). That is one number for the whole spectrum, and it depends on a choice of eigenvector matrix \( \X \). §04 warned that a well-behaved eigenvalue can sit inside a badly conditioned \( \X \), so the bound can be far too pessimistic for some eigenvalues. This section asks about **one** eigenvalue at a time. If \( \lambda \) is a simple eigenvalue of \( \A \), how fast does it move when \( \A \) is pushed in a direction \( \E \)? The answer is an exact derivative, \( \y^{*}\E\x/(\y^{*}\x) \), built from a right and a left eigenvector. Its worst size over all \( \E \) with \( \norm{\E}_2 = 1 \) is the condition number of that eigenvalue.

**The field is \( \nC \).** Throughout, \( \A, \E \in M_n(\nC) \), and \( \norm{\cdot} \) on vectors is the Euclidean norm.

## Left and right eigenvectors

Chapter 8 defined a left eigenvector as a non-zero \( \y \) with \( \y\tp\A = \lambda\y\tp \) (@def-left-eigenvector). Over \( \nC \) it is more convenient to put a conjugate on it. In this section, a **left eigenvector** of \( \A \) for \( \lambda \) is a non-zero \( \y \in \nC^n \) with
\[
\y^{*}\A = \lambda\,\y^{*} ,
\]
which is the same as \( \A^{*}\y = \conj{\lambda}\,\y \). Since \( \y^{*} = \conj{\y}\tp \), the equation \( \y^{*}\A = \lambda\y^{*} \) says exactly that \( \conj{\y} \) is a left eigenvector in the sense of @def-left-eigenvector. So the two conventions differ only by conjugating the vector. The conjugate is worth it for one reason: the number \( \y^{*}\x \) is then the standard inner product \( \inner{\x}{\y} \) of Chapter 10, and Cauchy–Schwarz applies to it.

For a **simple** eigenvalue, that is, one of algebraic multiplicity \( 1 \) (@def-algebraic-multiplicity), the right and left eigenvectors are as rigid as they can be, and they are never orthogonal. That last fact is what the whole section divides by.

::: {#lem-simple-eigenvalue-left-right}
[Left and Right Eigenvectors of a Simple Eigenvalue]

Let \( \A \in M_n(\nC) \) and let \( \lambda \) be a simple eigenvalue of \( \A \), with a right eigenvector \( \x \) and a left eigenvector \( \y \).

::: {.enumerate options="label=(\alph*)"}
1. The right eigenvectors of \( \A \) for \( \lambda \) are exactly the non-zero multiples of \( \x \), and the left eigenvectors are exactly the non-zero multiples of \( \y \).
2. \( \y^{*}\x \neq 0 \).
:::
:::

::: {.idea}
Split \( \lambda \) off from the rest of the spectrum. In a basis that begins with \( \x \), the matrix becomes block triangular with the \( 1 \times 1 \) block \( (\lambda) \) in the corner and a block \( \B \) with \( \lambda \notin \spec(\B) \). Chapter 11 §10 clears the off-diagonal corner whenever the two diagonal blocks have disjoint spectra, so \( \A \) is similar to \( (\lambda) \oplus \B \). In that picture everything is visible: \( \e_1 \) is the right eigenvector, \( \e_1^{*} \) the left one, and \( \e_1^{*}\e_1 = 1 \).
:::

::: {.proof}
If \( n = 1 \), both claims hold because every non-zero vector of \( \nC^1 \) is a multiple of every other, and \( \y^{*}\x = \conj{y_1}x_1 \) is a product of two non-zero numbers. Let \( n \ge 2 \).

By @thm-basis-extension, extend the independent list \( (\x) \) to a basis of \( \nC^n \), and let \( \P_0 \) be the invertible matrix with these columns, so that \( \P_0\e_1 = \x \). Then \( \P_0^{-1}\A\P_0\e_1 = \P_0^{-1}\lambda\x = \lambda\e_1 \), so
\[
\P_0^{-1}\A\P_0 = \begin{pmatrix} \lambda & \c \\ \0 & \B \end{pmatrix}
\]
for some \( \c \in M_{1 \times (n-1)}(\nC) \) and \( \B \in M_{n-1}(\nC) \). By @thm-charpoly-similarity-invariant and @thm-det-block-triangular, \( p_{\A}(x) = (x - \lambda)\,p_{\B}(x) \). If \( p_{\B}(\lambda) = 0 \), then \( x - \lambda \) would divide \( p_{\B} \) by the Factor Theorem (@lem-factor-theorem-linear), so \( (x - \lambda)^2 \) would divide \( p_{\A} \), against \( a_{\A}(\lambda) = 1 \). Hence \( \lambda \notin \spec(\B) \) (@thm-eigenvalue-characterizations). The spectra \( \{\lambda\} \) and \( \spec(\B) \) are disjoint, so by @cor-block-diagonalization (c) and (a) there is \( \Q = \begin{psmallmatrix} 1 & \z \\ \0 & \I_{n-1} \end{psmallmatrix} \) with \( \Q^{-1}\P_0^{-1}\A\P_0\Q = (\lambda) \oplus \B \). Put \( \P = \P_0\Q \). Then
\[
\P^{-1}\A\P = (\lambda) \oplus \B,
\qquad
\P\e_1 = \P_0\Q\e_1 = \P_0\e_1 = \x .
\]

(a) Let \( \A\v = \lambda\v \) and write \( \P^{-1}\v = (u_1, \u') \) with \( \u' \in \nC^{n-1} \). Then \( ((\lambda) \oplus \B)\P^{-1}\v = \lambda\P^{-1}\v \), whose last \( n - 1 \) rows say \( (\B - \lambda\I)\u' = \0 \). Since \( \lambda \notin \spec(\B) \), the matrix \( \B - \lambda\I \) is invertible (@thm-eigenvalue-characterizations), so \( \u' = \0 \) and \( \v = u_1\P\e_1 = u_1\x \). For the left side, let \( \w^{*}\A = \lambda\w^{*} \) and write \( \w^{*}\P = (w_1, \w'^{*}) \). Then \( (\w^{*}\P)((\lambda) \oplus \B) = \lambda\,\w^{*}\P \), whose last \( n - 1 \) entries say \( \w'^{*}(\B - \lambda\I) = \0 \). Multiplying on the right by \( (\B - \lambda\I)^{-1} \) gives \( \w' = \0 \), so \( \w^{*} = w_1\e_1^{*}\P^{-1} \). Every left eigenvector is therefore a multiple of the non-zero row \( \e_1^{*}\P^{-1} \), and in particular every left eigenvector is a multiple of any other. This proves (a).

(b) By the computation just made, \( \y^{*} = w_1\e_1^{*}\P^{-1} \) with \( w_1 \ne 0 \), because \( \y \ne \0 \). Hence
\[
\y^{*}\x = w_1\,\e_1^{*}\P^{-1}\P\e_1 = w_1\,\e_1^{*}\e_1 = w_1 \neq 0 .
\]
This proves the lemma.
:::

The proof produced a little more than was asked: the left eigenvector \( \e_1^{*}\P^{-1} \) is normalized against \( \x \), in the sense that \( (\e_1^{*}\P^{-1})\x = 1 \). This is the one-eigenvalue version of the biorthogonal normalization \( \y_i\tp\v_i = 1 \) of @prp-left-right-eigen-expansion, and it exists for a simple eigenvalue of any matrix, diagonalizable or not.

::: {.warning}
**Simple is essential: at a Jordan block, the two eigenvectors are orthogonal.** For \( \J_2(0) = \begin{psmallmatrix} 0 & 1 \\ 0 & 0 \end{psmallmatrix} \) the only eigenvalue is \( 0 \), twice. The right eigenvectors are the multiples of \( \x = \e_1 \), since \( \J_2(0)\e_1 = \0 \). The left eigenvectors are the multiples of \( \y = \e_2 \), since \( \e_2^{*}\J_2(0) \) is the second row, which is zero. So \( \y^{*}\x = 0 \). Every formula in this section that divides by \( \y^{*}\x \) is meaningless here, and §03's example shows why it must be: the eigenvalues of \( \J_2(0) + t\E_{21} \) are \( \pm\sqrt t \), which have no derivative at \( t = 0 \).
:::

::: {.check}
Let \( \A = \begin{psmallmatrix} 1 & 1 \\ 0 & 2 \end{psmallmatrix} \). Find a right and a left eigenvector for the eigenvalue \( 1 \), and check that \( \y^{*}\x \ne 0 \).
:::

::: {.solution}
\( \A\e_1 = \e_1 \), so \( \x = \e_1 \). A left eigenvector solves \( \y^{*}(\A - \I) = \0 \), and \( \A - \I = \begin{psmallmatrix} 0 & 1 \\ 0 & 1 \end{psmallmatrix} \); for \( \y^{*} = (a, b) \) this reads \( (0, a + b) = (0, 0) \), so \( \y = (1, -1) \) will do. Then \( \y^{*}\x = 1 \ne 0 \), as @lem-simple-eigenvalue-left-right (b) requires. Here \( \y \) is not a multiple of \( \x \): the matrix is not normal.
:::

## The derivative of a simple eigenvalue

Now move \( \A \) along a straight line \( \A + t\E \), with \( t \) real. Chapter 15 proved that the eigenvalues move continuously (@cor-eigenvalues-continuous), but only as an unnumbered list, and @prp-no-continuous-root-selection showed that no single eigenvalue can be followed continuously in general. A simple eigenvalue is the exception: it stays isolated from the rest for small \( t \), so "the eigenvalue near \( \lambda \)" makes sense. The theorem says that this eigenvalue is differentiable at \( t = 0 \), and it names the derivative.

::: {#thm-simple-eigenvalue-derivative}
[Derivative of a Simple Eigenvalue]

Let \( \A \in M_n(\nC) \), let \( \lambda \) be a simple eigenvalue of \( \A \) with a right eigenvector \( \x \) and a left eigenvector \( \y \), and let \( \E \in M_n(\nC) \). Then there are \( r > 0 \) and \( t_0 > 0 \) with the following properties.

::: {.enumerate options="label=(\alph*)"}
1. For every **real** \( t \) with \( \lvert t\rvert < t_0 \), the matrix \( \A + t\E \) has **exactly one** eigenvalue, counted with algebraic multiplicity, in the open disc \( \{z \in \nC : \lvert z - \lambda\rvert < r\} \). Call it \( \lambda(t) \). Thus \( \lambda(0) = \lambda \), and \( \lambda(t) \) is a simple eigenvalue of \( \A + t\E \).
2. \( \lambda(t) \to \lambda \) as \( t \to 0 \).
3. The function \( t \mapsto \lambda(t) \) is differentiable at \( t = 0 \), and
\[
\lambda'(0) = \lim_{t \to 0}\frac{\lambda(t) - \lambda}{t} = \frac{\y^{*}\E\x}{\y^{*}\x} .
\]
:::
:::

In other words, \( \lambda(t) = \lambda + t\,\y^{*}\E\x/(\y^{*}\x) + \rho(t) \) with \( \rho(t)/t \to 0 \). The denominator is non-zero by @lem-simple-eigenvalue-left-right (b), and the quotient does not change when \( \x \) or \( \y \) is rescaled, which by part (a) of the lemma is the only freedom there is.

::: {.idea}
The target identity falls out of one line if we have eigenvectors \( \x_t \) of \( \A + t\E \) that converge to an eigenvector of \( \A \): multiply \( (\A + t\E)\x_t = \lambda(t)\x_t \) on the left by \( \y^{*} \) and use \( \y^{*}\A = \lambda\y^{*} \), to get
\[
(\lambda(t) - \lambda)\,\y^{*}\x_t = t\,\y^{*}\E\x_t .
\]
Divide by \( t\,\y^{*}\x_t \) and let \( t \to 0 \). So the plan has three steps.

① Isolate \( \lambda(t) \) from the rest of the spectrum with @cor-eigenvalues-continuous.

② Produce the eigenvectors \( \x_t \) **by a formula**. A column of the adjugate \( \adj(\lambda(t)\I - \A - t\E) \) is an eigenvector, and its entries are polynomials in \( \lambda(t) \) and \( t \), so it converges because \( \lambda(t) \) does.

③ Check that the limit is a non-zero multiple of \( \x \), and pass to the limit in the quotient.
:::

::: {.proof}
Let \( \lambda_1 = \lambda, \lambda_2, \dots, \lambda_n \) be the eigenvalues of \( \A \), listed with algebraic multiplicity. Since \( \lambda \) is simple, \( \lambda_j \ne \lambda \) for \( j \ge 2 \).

**Step 1: the isolated eigenvalue.** Put \( r = \tfrac12\min_{j \ge 2}\lvert\lambda_j - \lambda\rvert \) if \( n \ge 2 \), and \( r = 1 \) if \( n = 1 \); in both cases \( r > 0 \). By @cor-eigenvalues-continuous with the norm \( \norm{\cdot}_2 \) and with \( \varepsilon = r \), there is \( \delta > 0 \) such that every \( \B \) with \( \norm{\B - \A}_2 < \delta \) has eigenvalues \( \mu_1, \dots, \mu_n \) that can be numbered so that \( \lvert\mu_i - \lambda_i\rvert < r \) for every \( i \). Put \( t_0 = \delta/(\norm{\E}_2 + 1) \). If \( \lvert t\rvert < t_0 \), then \( \norm{(\A + t\E) - \A}_2 = \lvert t\rvert\norm{\E}_2 < \delta \), so the eigenvalues of \( \A + t\E \) can be so numbered. Then \( \lvert\mu_1 - \lambda\rvert < r \), while for \( j \ge 2 \)
\[
\lvert\mu_j - \lambda\rvert \ge \lvert\lambda_j - \lambda\rvert - \lvert\mu_j - \lambda_j\rvert > 2r - r = r
\]
by @thm-complex-triangle-inequality. So exactly one entry of the list lies in the open disc of radius \( r \) about \( \lambda \). This proves (a).

**Step 2: continuity.** Let \( 0 < \varepsilon < r \). By @cor-eigenvalues-continuous again, now with this \( \varepsilon \), there is \( \delta' > 0 \) such that for \( \lvert t\rvert\norm{\E}_2 < \delta' \) the eigenvalues of \( \A + t\E \) can be numbered as \( \mu_1', \dots, \mu_n' \) with \( \lvert\mu_i' - \lambda_i\rvert < \varepsilon \). If moreover \( \lvert t\rvert < t_0 \), then \( \mu_1' \) is an eigenvalue of \( \A + t\E \) in the disc of radius \( \varepsilon < r \) about \( \lambda \), so \( \mu_1' = \lambda(t) \) by (a). Hence \( \lvert\lambda(t) - \lambda\rvert < \varepsilon \) whenever \( \lvert t\rvert < \min\bigl(t_0, \delta'/(\norm{\E}_2 + 1)\bigr) \). This proves (b).

**Step 3: an eigenvector given by a formula.** Put \( \N(t) = \lambda(t)\I - \A - t\E \) for \( \lvert t\rvert < t_0 \), so \( \N(0) = \lambda\I - \A \). We first find a column of \( \adj\N(0) \) that is not zero. If \( n = 1 \), then \( \adj\N(0) = (1) \) by @def-adjugate. If \( n \ge 2 \), then \( 1 \le g_{\A}(\lambda) \le a_{\A}(\lambda) = 1 \) by @thm-geometric-le-algebraic, so \( \rank\N(0) = n - 1 \ge 1 \) by @thm-rank-nullity-matrix. By @thm-rank-via-minors (a), \( \N(0) \) has a non-zero \( (n-1) \times (n-1) \) minor \( M_{ij} \). Then the cofactor \( C_{ij} = (-1)^{i+j}M_{ij} \) is non-zero, and it is the \( (j, i) \) entry of \( \adj\N(0) \) (@def-adjugate). In either case some column \( k \) of \( \adj\N(0) \) is non-zero. Define
\[
\x_t = \adj\bigl(\N(t)\bigr)\,\e_k \qquad (\lvert t\rvert < t_0).
\]
Since \( \lambda(t) \) is an eigenvalue of \( \A + t\E \), we have \( \det\N(t) = p_{\A + t\E}(\lambda(t)) = 0 \) (@thm-eigenvalue-characterizations). So @thm-adjugate-identity gives \( \N(t)\adj\N(t) = \0 \), and in particular
\[
(\A + t\E)\,\x_t = \lambda(t)\,\x_t \qquad (\lvert t\rvert < t_0).
\]
At \( t = 0 \) this says \( \A\x_0 = \lambda\x_0 \), and \( \x_0 \ne \0 \) by the choice of \( k \). By @lem-simple-eigenvalue-left-right (a), \( \x_0 = c\,\x \) for some \( c \ne 0 \).

Next, \( \x_t \to \x_0 \) as \( t \to 0 \). Each entry of \( \adj\B \) is \( \pm \) the determinant of a submatrix of \( \B \), or the constant \( 1 \) when \( n = 1 \), hence a polynomial in the entries of \( \B \) by @thm-leibniz-formula-alternating. So \( \B \mapsto \adj\B \) is continuous by @lem-entrywise-polynomial-continuous. And \( \norm{\N(t) - \N(0)}_2 \le \lvert\lambda(t) - \lambda\rvert + \lvert t\rvert\norm{\E}_2 \), which tends to \( 0 \) by (b). Hence \( \adj\N(t) \to \adj\N(0) \), and \( \norm{\x_t - \x_0} \le \norm{\adj\N(t) - \adj\N(0)}_2 \) by @thm-operator-norm-properties (a), since \( \norm{\e_k} = 1 \). So \( \x_t \to \x_0 \).

**Step 4: the derivative.** Multiply the eigen-equation of Step 3 on the left by \( \y^{*} \), and use \( \y^{*}\A = \lambda\y^{*} \):
\[
\lambda\,\y^{*}\x_t + t\,\y^{*}\E\x_t = \lambda(t)\,\y^{*}\x_t ,
\qquad\text{so}\qquad
(\lambda(t) - \lambda)\,\y^{*}\x_t = t\,\y^{*}\E\x_t .
\]
By Cauchy–Schwarz (@thm-cauchy-schwarz), \( \lvert\y^{*}\x_t - \y^{*}\x_0\rvert \le \norm{\y}\norm{\x_t - \x_0} \to 0 \), and likewise \( \y^{*}\E\x_t \to \y^{*}\E\x_0 \), because \( \norm{\E\x_t - \E\x_0} \le \norm{\E}_2\norm{\x_t - \x_0} \). The limit \( \y^{*}\x_0 = c\,\y^{*}\x \) is non-zero by @lem-simple-eigenvalue-left-right (b). So there is \( t_1 \in (0, t_0] \) with \( \lvert\y^{*}\x_t - \y^{*}\x_0\rvert < \lvert\y^{*}\x_0\rvert \), and hence \( \y^{*}\x_t \ne 0 \), for \( \lvert t\rvert < t_1 \). For \( 0 < \lvert t\rvert < t_1 \) we may divide:
\[
\begin{aligned}
\frac{\lambda(t) - \lambda}{t} = \frac{\y^{*}\E\x_t}{\y^{*}\x_t}
&\;\longrightarrow\; \frac{\y^{*}\E\x_0}{\y^{*}\x_0} \qquad (t \to 0), \\
\frac{\y^{*}\E\x_0}{\y^{*}\x_0} &= \frac{c\,\y^{*}\E\x}{c\,\y^{*}\x} = \frac{\y^{*}\E\x}{\y^{*}\x} ,
\end{aligned}
\]
by the algebra of limits, the denominator's limit being non-zero. This proves (c).
:::

**No implicit function theorem was needed.** The usual textbook route to this formula differentiates \( \det(z\I - \A - t\E) = 0 \) implicitly, which presupposes that a differentiable solution \( z = \lambda(t) \) exists; that is the implicit function theorem, a piece of analysis this book has not imported. The proof above needed only the continuity of @cor-eigenvalues-continuous and the fact that the adjugate writes down an eigenvector whose entries are polynomials. The analysis consists of limits of polynomials, which is the algebra of limits.

::: {.remark}
Since \( \lambda(s) \) is a simple eigenvalue of \( \A + s\E \) for every \( \lvert s\rvert < t_0 \), the theorem applies again at \( \A + s\E \) in place of \( \A \). The eigenvalue it isolates there is \( \lambda(s + h) \) for small \( h \), by the uniqueness in (a). So \( \lambda \) is differentiable on the whole interval \( (-t_0, t_0) \), with \( \lambda'(s) = \y_s^{*}\E\x_s/(\y_s^{*}\x_s) \) for right and left eigenvectors \( \x_s, \y_s \) of \( \A + s\E \) for \( \lambda(s) \). We need only \( s = 0 \).
:::

The formula has a transparent special case. If \( \A \) is Hermitian, then \( \A^{*}\x = \A\x = \lambda\x \) with \( \lambda \) real, so \( \x \) is also a left eigenvector and we may take \( \y = \x \):
\[
\lambda'(0) = \frac{\x^{*}\E\x}{\x^{*}\x} .
\]
When \( \E \) is Hermitian too, this is the Rayleigh quotient \( R_{\E}(\x) \) of Chapter 16 (@def-rayleigh-quotient), which lies in \( [\lambda_n(\E), \lambda_1(\E)] \) by @prp-rayleigh-basic. So \( \lvert\lambda'(0)\rvert \le \norm{\E}_2 \) by @lem-hermitian-spectral-norm, which is the first-order shadow of Weyl's bound \( \lvert\lambda_i(\A + \E) - \lambda_i(\A)\rvert \le \norm{\E}_2 \) (@cor-weyl-perturbation).

::: {.check}
Let \( \A = \diag(d_1, \dots, d_n) \) with distinct \( d_i \), and let \( \E = (e_{ij}) \) be arbitrary. What is the derivative at \( t = 0 \) of the eigenvalue of \( \A + t\E \) near \( d_i \)?
:::

::: {.solution}
The eigenvalue \( d_i \) is simple, with \( \x = \e_i \) and \( \y = \e_i \), since \( \e_i^{*}\A = d_i\e_i^{*} \). So \( \lambda'(0) = \e_i^{*}\E\e_i/(\e_i^{*}\e_i) = e_{ii} \). To first order, the eigenvalues of a perturbed diagonal matrix with distinct diagonal entries move by the diagonal of the perturbation, and the off-diagonal entries of \( \E \) enter only at second order.
:::

## The condition number of a simple eigenvalue

The derivative \( \y^{*}\E\x/(\y^{*}\x) \) depends on the direction \( \E \). To measure how sensitive \( \lambda \) itself is, bound it over all directions of a given size. By Cauchy–Schwarz and the definition of \( \norm{\E}_2 \),
\[
\lvert\lambda'(0)\rvert
= \frac{\lvert\y^{*}\E\x\rvert}{\lvert\y^{*}\x\rvert}
\le \frac{\norm{\y}\,\norm{\E\x}}{\lvert\y^{*}\x\rvert}
\le \frac{\norm{\x}\,\norm{\y}}{\lvert\y^{*}\x\rvert}\,\norm{\E}_2 .
\]
The factor in front of \( \norm{\E}_2 \) depends on \( \A \) and \( \lambda \) only. It recurs in every estimate below, so we give it a name.

*The condition number of an eigenvalue is the largest factor by which a perturbation of the matrix can move that eigenvalue, to first order.*

::: {#def-eigenvalue-condition-number}
[Condition Number of a Simple Eigenvalue]

Let \( \A \in M_n(\nC) \) and let \( \lambda \) be a **simple** eigenvalue of \( \A \), with a right eigenvector \( \x \) and a left eigenvector \( \y \), so \( \y^{*}\A = \lambda\y^{*} \). The **condition number** of \( \lambda \) is
\[
\kappa_{\A}(\lambda) \coloneqq \frac{\norm{\x}\,\norm{\y}}{\lvert\y^{*}\x\rvert} .
\]
:::

In words: take any right eigenvector and any left eigenvector for \( \lambda \), multiply their lengths, and divide by the modulus of their inner product. The definition is made only for a **simple** eigenvalue, which is what makes the denominator non-zero (@lem-simple-eigenvalue-left-right (b)). It is also what makes the number well defined: by part (a) of the lemma, any other choice is \( \alpha\x \) and \( \beta\y \) with \( \alpha, \beta \ne 0 \), and then
\[
\frac{\norm{\alpha\x}\,\norm{\beta\y}}{\lvert(\beta\y)^{*}(\alpha\x)\rvert}
= \frac{\lvert\alpha\rvert\,\lvert\beta\rvert\,\norm{\x}\,\norm{\y}}{\lvert\conj{\beta}\alpha\rvert\,\lvert\y^{*}\x\rvert}
= \kappa_{\A}(\lambda) .
\]
The subscript \( \A \) and the argument \( \lambda \) are part of the notation. They keep \( \kappa_{\A}(\lambda) \) apart from the condition number \( \kappa(\A) = \norm{\A}\norm{\A^{-1}} \) of a matrix (@def-condition-number).

**Examples.**

- **A \( 1 \times 1 \) matrix.** For \( \A = (a) \) the eigenvalue \( a \) is simple, with \( x = y = 1 \), so \( \kappa_{\A}(a) = 1 \). This is the degenerate case, and it is the right answer: the eigenvalue of \( (a + te) \) is \( a + te \), which moves exactly as fast as the matrix.
- **A diagonal matrix with distinct entries.** For \( d_i \), the Quick check above found \( \x = \y = \e_i \), so \( \kappa_{\A}(d_i) = 1 \). Every eigenvalue is perfectly conditioned.
- **A triangular \( 2 \times 2 \).** For \( \A = \begin{psmallmatrix} 1 & 1 \\ 0 & 2 \end{psmallmatrix} \) and the eigenvalue \( 1 \), the Quick check after the lemma found \( \x = \e_1 \) and \( \y = (1, -1) \), with \( \y^{*}\x = 1 \). So \( \kappa_{\A}(1) = 1 \cdot \sqrt2/1 = \sqrt2 \). The single off-diagonal entry has made the eigenvalue somewhat more sensitive.

**Non-example by minimal change.** Change the entry \( 2 \) of the last example to \( 1 + s \), and let \( s \to 0 \). For real \( s \ne 0 \) the matrix \( \B_s = \begin{psmallmatrix} 1 & 1 \\ 0 & 1 + s \end{psmallmatrix} \) has the simple eigenvalue \( 1 \), with \( \x = \e_1 \) and \( \y = (s, -1) \), so \( \kappa_{\B_s}(1) = \sqrt{1 + s^2}/\lvert s\rvert \). At \( s = 0 \) the matrix is \( \J_2(1) \), and the eigenvalue \( 1 \) is no longer simple. The right and left eigenvectors still exist, \( \e_1 \) and \( \e_2 \), but \( \y^{*}\x = 0 \), so the clause "simple" fails and the quotient is undefined. The formula for \( s \ne 0 \) shows that it blows up on the way.

**Why this definition.** Three choices in it can be checked.

- **Both lengths go in the numerator.** This makes \( \kappa_{\A}(\lambda) \) independent of the scaling of \( \x \) and \( \y \), as just computed. A normalization such as \( \y^{*}\x = 1 \) alone would leave one length free.
- **The norm is the Euclidean one,** because then the bound \( \lvert\lambda'(0)\rvert \le \kappa_{\A}(\lambda)\norm{\E}_2 \) above is attained by some \( \E \), as part (b) of the proposition below shows. So \( \kappa_{\A}(\lambda) \) is the exact worst case, not merely an upper bound. The same number is also the worst case over \( \norm{\E}_F = 1 \): the bound survives because \( \norm{\E}_2 \le \norm{\E}_F \) (@prp-spectral-vs-frobenius), and the extremal \( \E \) has rank one, so its two norms agree by the same proposition.
- **The name** matches @def-condition-number. There, \( \kappa(\A) \) is the worst factor by which \( \A \) magnifies a relative error in \( \b \) into a relative error in the solution of \( \A\x = \b \). Here \( \kappa_{\A}(\lambda) \) is the worst factor by which a change in the matrix is magnified into a change in one eigenvalue, to first order.

::: {.warning}
**A condition number is a first-order statement, not a bound.** It governs \( \lambda(t) \) only for small \( t \), through \( \lambda(t) - \lambda = t\lambda'(0) + \rho(t) \), and the remainder \( \rho(t) \) can be as large as the first-order term while \( t\norm{\E}_2 \) still looks small. Take \( \A = \begin{psmallmatrix} 1 & M \\ 0 & 2 \end{psmallmatrix} \) with \( M > 0 \), for which \( \kappa_{\A}(1) = \sqrt{1 + M^2} \), as the worked example below computes, and \( \E = \E_{21} \). At \( t = -1/(4M) \) the matrix \( \A + t\E \) has trace \( 3 \) and determinant \( 2 + \tfrac14 \), so both its eigenvalues equal \( \tfrac32 \). The eigenvalue \( 1 \) has moved by \( \tfrac12 \), while the first-order prediction is \( \kappa_{\A}(1)\,\lvert t\rvert\,\norm{\E}_2 = \sqrt{1 + M^2}/(4M) \), which is close to \( \tfrac14 \) for large \( M \). At that point the eigenvalue is no longer simple, and the square root in the exact formula \( (3 - \sqrt{1 + 4Mt})/2 \) has no derivative there.
:::

The first payoff is a list of properties, which together say what kind of number \( \kappa_{\A}(\lambda) \) is.

::: {#prp-eigenvalue-condition-properties}
[Properties of the Eigenvalue Condition Number]

Let \( \A \in M_n(\nC) \) and let \( \lambda \) be a simple eigenvalue of \( \A \) with right eigenvector \( \x \) and left eigenvector \( \y \).

::: {.enumerate options="label=(\alph*)"}
1. \( \kappa_{\A}(\lambda) \) does not depend on the choice of \( \x \) and \( \y \), and \( \kappa_{\A}(\lambda) \ge 1 \), with equality if and only if \( \y \) is a multiple of \( \x \).
2. For every \( \E \in M_n(\nC) \), the eigenvalue \( \lambda(t) \) of @thm-simple-eigenvalue-derivative satisfies \( \lvert\lambda'(0)\rvert \le \kappa_{\A}(\lambda)\norm{\E}_2 \). Equality holds for \( \E = \y\x^{*}/(\norm{\x}\norm{\y}) \), which has \( \norm{\E}_2 = 1 \). Hence \( \kappa_{\A}(\lambda) = \max\{\lvert\lambda'(0)\rvert : \norm{\E}_2 = 1\} \).
3. If \( \A \) is normal, then \( \kappa_{\A}(\mu) = 1 \) for every simple eigenvalue \( \mu \) of \( \A \).
4. If \( \A = \X\vLambda\X^{-1} \) with \( \X \) invertible and \( \vLambda = \diag(\lambda_1, \dots, \lambda_n) \), and \( \lambda_i \) is simple, then \( \kappa_{\A}(\lambda_i) \le \kappa_2(\X) \).
5. \( \kappa_{\A}(\lambda) = 1/\cos\theta \), where \( \theta \in [0, \pi/2) \) is the principal angle between the lines \( \Span(\x) \) and \( \Span(\y) \) (@def-principal-angles).
:::
:::

::: {.proof}
(a) Independence of the choice was checked after @def-eigenvalue-condition-number. By @thm-cauchy-schwarz, \( \lvert\y^{*}\x\rvert = \lvert\inner{\x}{\y}\rvert \le \norm{\x}\norm{\y} \), so \( \kappa_{\A}(\lambda) \ge 1 \), with equality if and only if \( (\x, \y) \) is linearly dependent, that is, since both are non-zero, if and only if \( \y \) is a multiple of \( \x \).

(b) The inequality is the display before @def-eigenvalue-condition-number, with \( \lambda'(0) \) given by @thm-simple-eigenvalue-derivative (c). For the equality, put \( \E = \y\x^{*}/(\norm{\x}\norm{\y}) \). For every \( \v \), \( \y\x^{*}\v = (\x^{*}\v)\,\y \), so \( \norm{\y\x^{*}\v} = \lvert\inner{\v}{\x}\rvert\,\norm{\y} \le \norm{\x}\norm{\y}\norm{\v} \) by Cauchy–Schwarz, with equality at \( \v = \x \). Hence \( \norm{\y\x^{*}}_2 = \norm{\x}\norm{\y} \) by @def-operator-norm, and \( \norm{\E}_2 = 1 \). Moreover
\[
\y^{*}\E\x = \frac{(\y^{*}\y)(\x^{*}\x)}{\norm{\x}\norm{\y}} = \norm{\x}\,\norm{\y},
\qquad\text{so}\qquad
\lvert\lambda'(0)\rvert = \frac{\norm{\x}\,\norm{\y}}{\lvert\y^{*}\x\rvert} = \kappa_{\A}(\lambda) .
\]
The maximum formula restates the inequality and its equality case.

(c) Let \( \A\x = \mu\x \) with \( \x \ne \0 \). By @thm-normal-eigenvector-shared, \( \A^{*}\x = \conj{\mu}\,\x \), and taking conjugate transposes gives \( \x^{*}\A = \mu\,\x^{*} \). So \( \x \) is also a left eigenvector for \( \mu \), and (a) gives \( \kappa_{\A}(\mu) = 1 \).

(d) Write \( \x_i = \X\e_i \) and \( \y_i^{*} = \e_i^{*}\X^{-1} \). From \( \A\X = \X\vLambda \) and \( \X^{-1}\A = \vLambda\X^{-1} \), column \( i \) and row \( i \) give \( \A\x_i = \lambda_i\x_i \) and \( \y_i^{*}\A = \lambda_i\y_i^{*} \), and both vectors are non-zero because \( \X \) is invertible. Also \( \y_i^{*}\x_i = \e_i^{*}\X^{-1}\X\e_i = 1 \). Now \( \norm{\x_i} \le \norm{\X}_2\norm{\e_i} = \norm{\X}_2 \) by @thm-operator-norm-properties (a). For \( \y_i \), Cauchy–Schwarz gives
\[
\norm{\y_i}^2 = \y_i^{*}\y_i = \e_i^{*}\X^{-1}\y_i
\le \norm{\X^{-1}\y_i}
\le \norm{\X^{-1}}_2\,\norm{\y_i} ,
\]
so \( \norm{\y_i} \le \norm{\X^{-1}}_2 \), after dividing by \( \norm{\y_i} > 0 \). Therefore \( \kappa_{\A}(\lambda_i) = \norm{\x_i}\norm{\y_i}/1 \le \norm{\X}_2\norm{\X^{-1}}_2 = \kappa_2(\X) \), by (a) and @def-condition-number.

(e) The vectors \( \x/\norm{\x} \) and \( \y/\norm{\y} \) are orthonormal bases of the two lines, so by @def-principal-angles the single principal angle satisfies \( \cos\theta = \sigma_1(c) \), where \( c = \y^{*}\x/(\norm{\x}\norm{\y}) \) is a \( 1 \times 1 \) matrix. Its only singular value is \( \lvert c\rvert \), the square root of the eigenvalue \( \conj{c}c \) of \( c^{*}c \) (@def-singular-values). Hence \( \cos\theta = \lvert\y^{*}\x\rvert/(\norm{\x}\norm{\y}) = 1/\kappa_{\A}(\lambda) \), which is positive by @lem-simple-eigenvalue-left-right (b), so \( \theta < \pi/2 \). This proves the proposition.
:::

Part (e) is the picture to keep. An eigenvalue is well conditioned when its right and left eigenvectors point in nearly the same direction, and ill conditioned when they are nearly perpendicular. For a normal matrix they coincide, by (c). At a Jordan block they are exactly perpendicular, by the warning after the lemma.

Part (d) places the new number beside §04. Bauer–Fike bounds the movement of every eigenvalue by \( \kappa_2(\X)\norm{\E}_2 \), for every size of \( \E \). Part (d) says that, to first order, each simple eigenvalue individually does at least as well, with its own constant \( \kappa_{\A}(\lambda_i) \), and that constant involves no choice of \( \X \). This is the refinement §04's warning promised. The first-order statement is sharper. The Bauer–Fike bound is global and needs no smallness.

## A worked example

Upper triangular \( 2 \times 2 \) matrices show everything, because their eigenvectors can be written down at once.

::: {#exm-triangular-eigenvalue-condition}
[The condition numbers of a triangular \( 2 \times 2 \) matrix]

Let \( a, b, d \in \nC \) with \( a \ne d \), and \( \A = \begin{psmallmatrix} a & b \\ 0 & d \end{psmallmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \kappa_{\A}(a) \) and \( \kappa_{\A}(d) \).
2. For \( a = 1 \), \( b = M > 0 \), \( d = 2 \), compare with the smallest value of \( \kappa_2(\X) \) over all diagonalizing \( \X \).
3. For the same matrix and \( \E = \E_{21} \), compute \( \lambda'(0) \) for the eigenvalue \( 1 \) from @thm-simple-eigenvalue-derivative, and compare with the exact eigenvalues of \( \A + t\E \) for \( M = 100 \) and \( t = 10^{-4} \).
:::
:::

::: {.solution}
(a) Both eigenvalues are simple, since \( a \ne d \). For \( a \): \( \A\e_1 = a\e_1 \), so \( \x = \e_1 \). A left eigenvector solves \( \y^{*}(\A - a\I) = \0 \), where \( \A - a\I = \begin{psmallmatrix} 0 & b \\ 0 & d - a \end{psmallmatrix} \). For a row \( \y^{*} = (u, v) \) the product is \( (0,\ ub + v(d - a)) \), so \( \y^{*} = (d - a, -b) \) works. Then \( \y^{*}\x = d - a \), and
\[
\kappa_{\A}(a) = \frac{1 \cdot \sqrt{\lvert d - a\rvert^2 + \lvert b\rvert^2}}{\lvert d - a\rvert} = \sqrt{1 + \frac{\lvert b\rvert^2}{\lvert a - d\rvert^2}} .
\]
For \( d \): \( \y = \e_2 \) is a left eigenvector, because \( \e_2^{*}\A = (0, d) = d\,\e_2^{*} \). A right eigenvector is \( \x = (b, d - a) \), since \( (\A - d\I)\x = \bigl((a - d)b + b(d - a),\ 0\bigr) = \0 \). Then \( \y^{*}\x = d - a \), and \( \kappa_{\A}(d) \) is given by the same formula. The two condition numbers are equal. They are large exactly when the off-diagonal entry is large compared with the gap between the eigenvalues.

(b) Here \( \kappa_{\A}(1) = \kappa_{\A}(2) = \sqrt{1 + M^2} \). §04 computed \( \kappa_2 \) for two diagonalizing matrices of this \( \A \) (@exm-bauer-fike-two-by-two), and the better one, with unit columns, gave \( M + \sqrt{1 + M^2} \). We show that no choice does better. The eigenvectors are the multiples of \( \e_1 \) and of \( (M, 1) \), and the columns of a diagonalizing \( \X \) are eigenvectors (@thm-diagonalization). So, up to the order of its columns, which does not change \( \kappa_2(\X) \), every diagonalizing \( \X \) has the form \( \X = \begin{psmallmatrix} \alpha & \beta M \\ 0 & \beta \end{psmallmatrix} \) with \( \alpha, \beta \ne 0 \), by @lem-simple-eigenvalue-left-right (a). Multiplying \( \X \) by a scalar does not change \( \kappa_2(\X) \), so we may take \( \alpha = 1 \). Let \( \sigma_1 \ge \sigma_2 > 0 \) be the singular values of \( \X \). They are the square roots of the eigenvalues of \( \X^{*}\X \) (@def-singular-values), so \( \sigma_1^2\sigma_2^2 = \det(\X^{*}\X) = \lvert\det\X\rvert^2 \), giving \( \sigma_1\sigma_2 = \lvert\beta\rvert \), and \( \sigma_1^2 + \sigma_2^2 = \tr(\X^{*}\X) = 1 + \lvert\beta\rvert^2(1 + M^2) \). With \( k = \kappa_2(\X) = \sigma_1/\sigma_2 \),
\[
k + \frac1k = \frac{\sigma_1^2 + \sigma_2^2}{\sigma_1\sigma_2}
= \frac{1}{\lvert\beta\rvert} + \lvert\beta\rvert(1 + M^2)
\ge 2\sqrt{1 + M^2} ,
\]
by the inequality \( u + v \ge 2\sqrt{uv} \) for \( u, v > 0 \), with equality exactly when \( \lvert\beta\rvert = 1/\sqrt{1 + M^2} \), that is, when both columns of \( \X \) are unit vectors. The function \( k \mapsto k + 1/k \) is increasing for \( k \ge 1 \), so the smallest possible \( \kappa_2(\X) \) is the root \( k \ge 1 \) of \( k + 1/k = 2\sqrt{1 + M^2} \), namely
\[
\min_{\X}\kappa_2(\X) = M + \sqrt{1 + M^2} .
\]
Indeed \( (M + \sqrt{1 + M^2})^{-1} = \sqrt{1 + M^2} - M \), and the two add up to \( 2\sqrt{1 + M^2} \). So the per-eigenvalue constant \( \sqrt{1 + M^2} \) is smaller than the best Bauer–Fike constant, by a factor that tends to \( 2 \) as \( M \) grows, in agreement with @prp-eigenvalue-condition-properties (d).

(c) With \( \x = \e_1 \) and \( \y^{*} = (1, -M) \) from (a), \( \y^{*}\E_{21}\x = \y^{*}\e_2 = -M \) and \( \y^{*}\x = 1 \), so
\[
\lambda'(0) = -M ,
\qquad
\lvert\lambda'(0)\rvert = M \le \sqrt{1 + M^2}\,\norm{\E_{21}}_2 = \kappa_{\A}(1)\,\norm{\E}_2 .
\]
Exactly: \( \A + t\E = \begin{psmallmatrix} 1 & M \\ t & 2 \end{psmallmatrix} \) has trace \( 3 \) and determinant \( 2 - Mt \), so its eigenvalues are
\[
\lambda_{\pm}(t) = \frac{3 \pm \sqrt{1 + 4Mt}}{2} ,
\]
and the one near \( 1 \) is \( \lambda_-(t) \). For \( M = 100 \) and \( t = 10^{-4} \) we get \( 4Mt = 0.04 \), and \( \lambda_-(t) = (3 - \sqrt{1.04})/2 \approx 0.990098 \). The eigenvalue has moved by about \( 0.0099 \), and the first-order prediction \( \lvert t\lambda'(0)\rvert = Mt \) is \( 0.01 \). Differentiating \( \lambda_-(t) \) directly gives \( \lambda_-'(0) = -\tfrac14 \cdot 4M = -M \), as the theorem says.
:::

§04 set this matrix beside Chapter 11's @exm-eigenvalue-sensitivity, which perturbed the same corner of \( \begin{psmallmatrix} 1 & M \\ 0 & 1 \end{psmallmatrix} \). There the diagonal entries are equal, and the eigenvalue \( 1 \) moved by \( \sqrt{Mt} \); with \( M = 100 \) and \( t = 10^{-4} \) that is \( 0.1 \), ten times the movement found in (c). The derivative explains the difference. With a gap of \( 1 \) between the eigenvalues, the movement is linear in \( t \) to first order, with slope \( M \), at most \( \kappa_{\A}(1) = \sqrt{1 + M^2} \). With no gap there is no derivative at all. Chapter 11's closing remark, that a matrix with well-separated eigenvalues and a large defect behaves less dramatically, is now a formula.

## When eigenvalues coalesce

The two computations just compared are the ends of a single family. Put
\[
\A_s = \begin{pmatrix} 1 & M \\ 0 & 1 + s \end{pmatrix} \qquad (M > 0,\ s > 0).
\]
By @exm-triangular-eigenvalue-condition (a), with \( b = M \) and \( a - d = -s \),
\[
\kappa_{\A_s}(1) = \kappa_{\A_s}(1 + s) = \sqrt{1 + \frac{M^2}{s^2}} \;\longrightarrow\; \infty \qquad (s \to 0^{+}) .
\]
As the two eigenvalues move together, the left eigenvector \( (s, -M) \) of the eigenvalue \( 1 \) turns towards \( \e_2 \), perpendicular to the right eigenvector \( \e_1 \). At \( s = 0 \) the matrix is a Jordan block in disguise, as Chapter 11 observed, the product \( \y^{*}\x \) is \( 0 \), and the derivative no longer exists. Instead the eigenvalue moves by \( \sqrt{Mt} \) (@exm-eigenvalue-sensitivity), the case \( n = 2 \) of the \( n \)-th root behavior of §03 (@exm-jordan-root-perturbation).

So the first-order theory and the Hölder behavior of §03 are not two separate phenomena. In this family a large condition number is the sign of a nearby coalescence. Near such a coalescence, the linear regime \( \lvert\lambda(t) - \lambda\rvert \approx \kappa\lvert t\rvert\norm{\E}_2 \) holds only for smaller and smaller \( t \), and beyond it the square root takes over. The warning above showed the same thing from the other side: for \( \begin{psmallmatrix} 1 & M \\ 0 & 2 \end{psmallmatrix} \), a perturbation of size \( 1/(4M) \), about \( 1/(4\kappa) \), is enough to make the two eigenvalues collide.

::: {.remark}
This completes the thread that Chapter 9 §03 started when it warned that the Jordan form is not stable and said that "Chapter 19 returns to this point". §03 measured the instability, a movement of \( \varepsilon^{1/n} \) for a block of size \( n \), and showed that the exponent is the worst possible (@exm-jordan-root-perturbation, @thm-elsner-spectral-variation). §04 bounded it for every matrix, with an \( m \)-th root for a largest block of size \( m \) (@thm-bauer-fike-defective). This section adds the first-order view. A **defective** eigenvalue, one with a Jordan block of size \( m \ge 2 \), has no finite condition number in any sense: along \( \J_m(\lambda) + t\E_{m1} \) every eigenvalue satisfies \( \lvert\lambda(t) - \lambda\rvert/\lvert t\rvert = \lvert t\rvert^{1/m - 1} \), which is unbounded as \( t \to 0 \). Any defective eigenvalue inherits this by similarity: if \( \A = \S\J\S^{-1} \) with \( \J \) in Jordan form (@thm-jordan-canonical-form) and \( \E = \S\E'\S^{-1} \), where \( \E' \) carries a single \( 1 \) in the lower-left corner of a block \( \J_m(\lambda) \) and zeros elsewhere, then \( \A + t\E \) is similar to \( \J + t\E' \), so among its eigenvalues are the \( m \) roots of \( (z - \lambda)^m = t \), at distance \( \lvert t\rvert^{1/m} \) from \( \lambda \). And, as the family \( \A_s \) shows, simple eigenvalues that are about to merge into such a block have condition numbers that blow up. A multiple eigenvalue that is **not** defective is different. For \( \A = \I_2 \), every eigenvalue of \( \I_2 + t\E \) lies within \( \lvert t\rvert\norm{\E}_2 \) of \( 1 \) by @cor-bauer-fike-normal (a), so nothing is infinite. What fails there is only the numbering: the two eigenvalues of \( \I_2 + t\E \) cannot in general be told apart as "the one that came from \( 1 \)", so @def-eigenvalue-condition-number does not apply.
:::

## Summary and transfer

The chapter set out to answer four questions about a perturbed matrix \( \A + \E \): where its eigenvalues are, how far they move, which one goes where, and what happens to eigenvectors, invariant subspaces, singular values and polar factors.

- **Where.** Gershgorin's discs (§01) and the other inclusion regions (§02) locate the eigenvalues without computing any of them.
- **How far.** The continuity of roots (§03) is now a theorem of the book, proved by compactness. It comes with Elsner's Hölder bound, whose exponent \( 1/n \) cannot be improved, and with a matching version of that bound. Bauer–Fike (§04) replaces the exponent by \( 1 \) for diagonalizable matrices, at the price of the factor \( \kappa_2(\X) \).
- **Which goes where.** Hoffman–Wielandt (§05) matches the eigenvalues of two normal matrices in the Frobenius norm.
- **Hermitian matrices** (§06) got sharper tools: residual bounds, a quadratic bound for the Rayleigh quotient, and relative bounds under congruence.
- **Eigenvectors and subspaces.** The Sylvester equation (§07) and principal angles (§08) together give Davis–Kahan (§09): an invariant subspace moves by at most the perturbation divided by the gap.
- **Singular values and polar factors** (§10) follow by the dilation and by the Sylvester bounds.
- **To first order.** This section gave each simple eigenvalue its own derivative and condition number.

Nine moves did the work.

- **Dominant coordinate plus the triangle inequality.** Look at the row of the eigen-equation where the eigenvector is largest (§01), or at the two largest coordinates (§02). *Transfer:* to locate an eigenvalue without computing it, read the eigen-equation at the coordinate where the eigenvector peaks. There the eigenvalue cannot hide behind the other terms.
- **A determinant bounded two ways.** The product of the distances from \( \mu \) to the eigenvalues of \( \A \) is \( \lvert\det(\A - \mu\I)\rvert \), and Hadamard's inequality bounds that determinant by column lengths (§03, Elsner). *Transfer:* when a product of unknown quantities is a determinant, bound the determinant from above and the product from below, and read off the smallest factor.
- **Compactness plus uniqueness.** Roots are bounded, so a subsequence of root vectors converges. Its limit is a root vector of the limit polynomial, and unique factorization says which one (§03). *Transfer:* to prove that a solution depends continuously on the data, bound the solutions, extract a convergent subsequence, and let uniqueness of the limiting solution do the rest.
- **An integer-valued continuous function is constant.** Deform \( \A \) to its diagonal, and count the eigenvalues in a region whose boundary no eigenvalue crosses (§03, the counting theorem). *Transfer:* to count objects that move continuously, move to a case where the count is obvious, along a path that never lets one of them escape.
- **Factor out the resolvent.** Write \( \A + \E - \mu\I = (\A - \mu\I)\bigl(\I + (\A - \mu\I)^{-1}\E\bigr) \), so that the Neumann series makes the second factor invertible whenever \( \norm{(\A - \mu\I)^{-1}\E} < 1 \) (§04). *Transfer:* to show a perturbed matrix is invertible, factor out the unperturbed one and ask whether what remains is close to \( \I \).
- **Birkhoff turns a doubly stochastic weight into a permutation.** The weights \( \lvert w_{ij}\rvert^2 \) of a unitary matrix form a doubly stochastic matrix, and a linear function on those attains its minimum at a permutation matrix (§05). *Transfer:* to optimize over matchings, relax to doubly stochastic matrices. A linear objective has its optimum at a vertex, and the vertices are the matchings.
- **The perturbation of a subspace is a Sylvester equation.** The block that couples the old invariant subspace to the new complement satisfies \( \widetilde\vLambda_2\X - \X\vLambda_1 = \) (a piece of \( \E \)), so the separation of the two spectra is the conditioning (§07, §09). *Transfer:* to measure how far an invariant subspace moves, write down the coupling block and recognize the equation it solves.
- **The singular-pair trick.** Test a matrix equation against the top singular pair of the unknown \( \X \). This turns \( \norm{\X}_2 \) into a scalar that the hypotheses bound directly (§07, used twice in §10). *Transfer:* to bound the spectral norm of the solution of a linear matrix equation, evaluate the equation at the vectors where that norm is attained.
- **The adjugate as a polynomial eigenvector.** A column of \( \adj(\mu\I - \B) \) is an eigenvector of \( \B \) whenever \( \mu \) is an eigenvalue, and its entries are polynomials in \( \mu \) and the entries of \( \B \). So it moves continuously when they do (this section). *Transfer:* when an object must be chosen continuously and there is no canonical choice, look for a formula that is polynomial in the data. The implicit function theorem then becomes unnecessary.

The chapter also paid promises made in earlier chapters.

| The promise | Made in | Paid by |
|---|---|---|
| "This chapter quotes this theorem, and Chapter 19 proves it" (continuous dependence of roots on coefficients) | Chapter 15 §07 | §03 (Continuity of roots) |
| "Chapter 19 returns to this point" (the Jordan form is not stable) | Chapter 9 §03 | §03, §04 and this section |
| "Chapter 19 develops both and proves it" (Bauer–Fike) | Chapter 11 §11 | §04 (The Bauer–Fike theorem) |
| "Chapter 19 proves the theorem of Bauer and Fike" | Chapter 15 §07 | §04 |
| "the theorem of Bauer and Fike, in Chapter 19" | Chapter 16 §03 | §04 |
| "the bounds that do exist, Weyl's and Bauer–Fike's, are Chapters 16 and 19" | Chapter 15 §08 | §04 |
| "Bounds for the eigenvalues of non-Hermitian matrices under perturbation, beginning with Bauer–Fike, are Chapter 19's" | Chapter 16 §11 | §§03–05 |
| "its quantitative form appears in Chapter 19" (the Sylvester equation) | Chapter 7 §04 | §07 (The Sylvester equation) |
| "belongs with perturbation theory in Chapter 19" (conditioning of the Sylvester equation) | Chapter 11 §10 | §07 |
| "Chapter 19 leans on it for perturbation bounds" (the Hermitian dilation) | Chapter 16 §09 | §10 (Singular values and polar factors) |

Some things the chapter did not do. The matching form of Elsner's bound in §03 carries a factor \( 2n - 1 \), which is not the best possible, and the better constants were not pursued. The spectral-norm form of Davis–Kahan for a cluster lying between two parts of the rest of the spectrum was stated without proof (§09), and nothing depends on it. The bounds of §05, and Mirsky's theorem in §10, hold in the Frobenius norm; §10's square-root and polar bounds hold in the spectral norm as well. Their extension to every unitarily invariant norm belongs to Chapter 20. Finally, the residual bounds of §04 and §06 say that a computed eigenpair is an exact eigenpair of a nearby matrix. Turning that into a theory of backward error, and into algorithms that compute eigenvalues, is the subject of Chapter 23.

## Exercises

### A. Check your understanding

:::: {#exr-eigenvalue-condition-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the condition number \( \kappa_{\A}(\lambda) \), saying for which \( \lambda \) it is defined.
2. State the formula for the derivative of a simple eigenvalue of \( \A + t\E \) at \( t = 0 \).
3. True or false: for every eigenvalue of every \( \A \in M_n(\nC) \), a right eigenvector \( \x \) and a left eigenvector \( \y \) satisfy \( \y^{*}\x \ne 0 \). Justify your answer.
4. True or false: if \( \A = \X\vLambda\X^{-1} \) with \( \kappa_2(\X) \ge 10^{6} \), then some eigenvalue of \( \A \) has \( \kappa_{\A}(\lambda) \ge 10^{6} \). Justify your answer.
5. True or false: \( \kappa_{2\A + 3\I}(2\lambda + 3) = \kappa_{\A}(\lambda) \) for every simple eigenvalue \( \lambda \) of \( \A \). Justify your answer.
6. The proof of @thm-simple-eigenvalue-derivative needed eigenvectors of \( \A + t\E \) that converge as \( t \to 0 \). Where did they come from?
:::
::::

::: {.solution}
(a) For a **simple** eigenvalue \( \lambda \) of \( \A \in M_n(\nC) \) with right eigenvector \( \x \) and left eigenvector \( \y \) (\( \y^{*}\A = \lambda\y^{*} \)), \( \kappa_{\A}(\lambda) = \norm{\x}\norm{\y}/\lvert\y^{*}\x\rvert \) (@def-eigenvalue-condition-number).

(b) \( \lambda'(0) = \y^{*}\E\x/(\y^{*}\x) \), where \( \lambda(t) \) is the unique eigenvalue of \( \A + t\E \) near \( \lambda \) (@thm-simple-eigenvalue-derivative).

(c) False. For \( \J_2(0) \) the eigenvectors are the multiples of \( \x = \e_1 \) and of \( \y = \e_2 \), and \( \y^{*}\x = 0 \), as in the warning after @lem-simple-eigenvalue-left-right. The eigenvalue \( 0 \) is not simple, and simplicity is the hypothesis of that lemma.

(d) False. Let \( \A = \diag(1, 2) \) and \( \X = \diag(1, 10^{6}) \). Then \( \X\A\X^{-1} = \A \) because diagonal matrices commute, so \( \A = \X\A\X^{-1} \), and \( \kappa_2(\X) = 10^{6} \). But \( \A \) is normal, so both eigenvalues have condition number \( 1 \) by @prp-eigenvalue-condition-properties (c). A large \( \kappa_2(\X) \) may just reflect a poor choice of \( \X \).

(e) True. The eigenvalue \( 2\lambda + 3 \) of \( 2\A + 3\I \) is simple, since \( p_{2\A + 3\I}(x) = 2^n p_{\A}((x - 3)/2) \). From \( \A\x = \lambda\x \) and \( \y^{*}\A = \lambda\y^{*} \) we get \( (2\A + 3\I)\x = (2\lambda + 3)\x \) and \( \y^{*}(2\A + 3\I) = (2\lambda + 3)\y^{*} \). So the same \( \x \) and \( \y \) serve, and the formula gives the same number.

(f) From the adjugate: a non-zero column of \( \adj(\lambda\I - \A) \) was fixed, and the same column of \( \adj(\lambda(t)\I - \A - t\E) \) is an eigenvector of \( \A + t\E \) for \( \lambda(t) \) by @thm-adjugate-identity. Its entries are polynomials in \( \lambda(t) \), \( t \) and the entries of \( \A \) and \( \E \), so it converges because \( \lambda(t) \) does (@cor-eigenvalues-continuous). No implicit function theorem was used.
:::

### B. Practice

:::: {#exr-eigenvalue-condition-b1}
[B1: Three condition numbers]

Let
\[
\A = \begin{pmatrix} 1 & 3 & 0 \\ 0 & 5 & 4 \\ 0 & 0 & 2 \end{pmatrix} .
\]

::: {.enumerate options="label=(\alph*)"}
1. For each eigenvalue of \( \A \), find a right and a left eigenvector with integer entries, and compute \( \kappa_{\A}(1) \), \( \kappa_{\A}(2) \) and \( \kappa_{\A}(5) \).
2. Hence decide which eigenvalue is the most sensitive to first order, and find \( \E \) with \( \norm{\E}_2 = 1 \) for which that eigenvalue of \( \A + t\E \) has \( \lvert\lambda'(0)\rvert \) as large as possible.
:::
::::

::: {.solution}
(a) The matrix is upper triangular with diagonal \( 1, 5, 2 \), so these are the eigenvalues, each simple.

*Eigenvalue \( 1 \).* \( \x = \e_1 \). For \( \y^{*} = (u, v, w) \), the equation \( \y^{*}(\A - \I) = \0 \) reads \( (0,\ 3u + 4v,\ 4v + w) = \0 \). Take \( u = 4 \), \( v = -3 \), \( w = 12 \), so \( \y = (4, -3, 12) \), with \( \norm{\y} = \sqrt{16 + 9 + 144} = 13 \) and \( \y^{*}\x = 4 \). Hence \( \kappa_{\A}(1) = 13/4 \).

*Eigenvalue \( 2 \).* \( \y = \e_3 \), since \( \e_3^{*}\A = (0, 0, 2) \). For \( \x = (p, q, r) \), the equation \( (\A - 2\I)\x = \0 \) reads \( -p + 3q = 0 \), \( 3q + 4r = 0 \). Take \( r = 3 \), \( q = -4 \), \( p = -12 \), so \( \x = (-12, -4, 3) \), with \( \norm{\x} = \sqrt{144 + 16 + 9} = 13 \) and \( \y^{*}\x = 3 \). Hence \( \kappa_{\A}(2) = 13/3 \).

*Eigenvalue \( 5 \).* For \( \x = (p, q, 0) \), \( (\A - 5\I)\x = (-4p + 3q, 0, 0) \), so \( \x = (3, 4, 0) \). For \( \y^{*} = (0, v, w) \), \( \y^{*}(\A - 5\I) = (0, 0, 4v - 3w) \), so \( \y = (0, 3, 4) \). Both have length \( 5 \), and \( \y^{*}\x = 12 \). Hence \( \kappa_{\A}(5) = 25/12 \).

(b) Since \( 13/3 > 13/4 > 25/12 \), the eigenvalue \( 2 \) is the most sensitive, although the eigenvalue \( 1 \) is exactly as close to its nearest neighbor and less sensitive: the gaps alone do not decide. By @prp-eigenvalue-condition-properties (b), the worst direction is
\[
\E = \frac{\y\x^{*}}{\norm{\x}\norm{\y}} = \frac{1}{13}\begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ -12 & -4 & 3 \end{pmatrix} ,
\]
with \( \norm{\E}_2 = 1 \) and \( \lambda'(0) = \norm{\x}\norm{\y}/(\y^{*}\x) = 13/3 \). Hence, to first order, a perturbation of size \( 10^{-3} \) in this direction moves the eigenvalue \( 2 \) by about \( 4.3 \times 10^{-3} \).
:::

:::: {#exr-eigenvalue-condition-b2}
[B2: A derivative checked against the exact answer]

Let \( \A = \begin{psmallmatrix} 0 & 1 \\ -2 & 3 \end{psmallmatrix} \) and \( \E = \E_{12} \).

::: {.enumerate options="label=(\alph*)"}
1. Find the eigenvalues of \( \A \) with right and left eigenvectors, and compute both condition numbers.
2. Use @thm-simple-eigenvalue-derivative to find \( \lambda'(0) \) for each eigenvalue of \( \A + t\E \).
3. Find the eigenvalues of \( \A + t\E \) exactly. Hence compare the first-order estimate with the exact value at \( t = 10^{-3} \).
:::
::::

::: {.solution}
(a) \( p_{\A}(x) = x^2 - 3x + 2 = (x - 1)(x - 2) \). For \( 1 \): \( \A - \I = \begin{psmallmatrix} -1 & 1 \\ -2 & 2 \end{psmallmatrix} \), so \( \x_1 = (1, 1) \), and \( \y^{*}(\A - \I) = \0 \) for \( \y^{*} = (u, v) \) means \( -u - 2v = 0 \), so \( \y_1 = (2, -1) \). Then \( \y_1^{*}\x_1 = 1 \) and \( \kappa_{\A}(1) = \sqrt2\sqrt5 = \sqrt{10} \). For \( 2 \): \( \A - 2\I = \begin{psmallmatrix} -2 & 1 \\ -2 & 1 \end{psmallmatrix} \), so \( \x_2 = (1, 2) \) and \( \y_2 = (1, -1) \), with \( \y_2^{*}\x_2 = -1 \) and \( \kappa_{\A}(2) = \sqrt5\sqrt2 = \sqrt{10} \).

(b) \( \y^{*}\E_{12}\x = \conj{y_1}\,x_2 \). For \( 1 \): \( 2 \cdot 1/1 = 2 \). For \( 2 \): \( 1 \cdot 2/(-1) = -2 \).

(c) \( \A + t\E = \begin{psmallmatrix} 0 & 1 + t \\ -2 & 3 \end{psmallmatrix} \) has trace \( 3 \) and determinant \( 2 + 2t \), so its eigenvalues are \( (3 \mp \sqrt{1 - 8t})/2 \), for \( t < 1/8 \). Differentiating at \( t = 0 \) gives \( \pm 2 \), as in (b). At \( t = 10^{-3} \), the first-order estimates are \( 1.002 \) and \( 1.998 \), and the exact values are \( (3 \mp \sqrt{0.992})/2 \approx 1.002004 \) and \( 1.997996 \). Hence the error of the first-order estimate is about \( 4 \times 10^{-6} \), which is of the order of \( t^2 \), as expected of a first-order approximation.
:::

:::: {#exr-eigenvalue-condition-b3}
[B3: Invariance of the condition number]

Let \( \lambda \) be a simple eigenvalue of \( \A \in M_n(\nC) \). Prove that:

::: {.enumerate options="label=(\alph*)"}
1. \( \conj{\lambda} \) is a simple eigenvalue of \( \A^{*} \), and \( \kappa_{\A^{*}}(\conj{\lambda}) = \kappa_{\A}(\lambda) \);
2. \( \kappa_{\U^{*}\A\U}(\lambda) = \kappa_{\A}(\lambda) \) for every unitary \( \U \).
3. Explain why (b) fails for a general invertible \( \S \) in place of \( \U \), using \( \A = \diag(1, 2) \).
:::
::::

::: {.solution}
(a) The characteristic polynomial of \( \A^{*} \) has as roots the conjugates of those of \( \A \), with the same multiplicities: \( p_{\A^{*}}(x) = \det(x\I - \A^{*}) = \conj{\det(\conj{x}\I - \A)} \), because the determinant of the conjugate transpose is the conjugate of the determinant. So \( \conj{\lambda} \) is a simple eigenvalue of \( \A^{*} \). If \( \A\x = \lambda\x \) and \( \y^{*}\A = \lambda\y^{*} \), then taking conjugate transposes gives \( \x^{*}\A^{*} = \conj{\lambda}\x^{*} \) and \( \A^{*}\y = \conj{\lambda}\y \). So for \( \A^{*} \) and \( \conj{\lambda} \), the vector \( \y \) is a right eigenvector and \( \x \) a left one. Hence \( \kappa_{\A^{*}}(\conj{\lambda}) = \norm{\y}\norm{\x}/\lvert\x^{*}\y\rvert = \kappa_{\A}(\lambda) \), since \( \lvert\x^{*}\y\rvert = \lvert\conj{\y^{*}\x}\rvert = \lvert\y^{*}\x\rvert \).

(b) \( \U^{*}\A\U \) has the same characteristic polynomial as \( \A \) (@thm-charpoly-similarity-invariant), so \( \lambda \) is simple for it. From \( \A\x = \lambda\x \) and \( \y^{*}\A = \lambda\y^{*} \) we get \( (\U^{*}\A\U)(\U^{*}\x) = \lambda\,\U^{*}\x \) and \( (\U^{*}\y)^{*}(\U^{*}\A\U) = \y^{*}\A\U = \lambda\,(\U^{*}\y)^{*} \). Since \( \U^{*} \) is unitary, \( \norm{\U^{*}\x} = \norm{\x} \) and \( \norm{\U^{*}\y} = \norm{\y} \) (@thm-isometry-characterizations), and \( (\U^{*}\y)^{*}(\U^{*}\x) = \y^{*}\U\U^{*}\x = \y^{*}\x \). So all three ingredients of @def-eigenvalue-condition-number are unchanged.

(c) For \( \S = \begin{psmallmatrix} 1 & 1 \\ 0 & 1 \end{psmallmatrix} \), \( \S^{-1}\A\S = \begin{psmallmatrix} 1 & -1 \\ 0 & 1 \end{psmallmatrix}\begin{psmallmatrix} 1 & 1 \\ 0 & 2 \end{psmallmatrix} = \begin{psmallmatrix} 1 & -1 \\ 0 & 2 \end{psmallmatrix} \). By @exm-triangular-eigenvalue-condition (a) with \( b = -1 \) and \( \lvert a - d\rvert = 1 \), its eigenvalue \( 1 \) has condition number \( \sqrt2 \), whereas \( \kappa_{\A}(1) = 1 \) because \( \A \) is normal. A non-unitary similarity changes lengths and angles, so it changes the angle between \( \x \) and \( \y \) in @prp-eigenvalue-condition-properties (e).
:::

### C. Going deeper

:::: {#exr-eigenvalue-condition-c1}
[C1: Perfect conditioning characterizes normality]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \A \in M_n(\nC) \) have \( n \) distinct eigenvalues. Prove that \( \A \) is normal if and only if \( \kappa_{\A}(\lambda) = 1 \) for every eigenvalue \( \lambda \).
2. Show that the hypothesis of distinct eigenvalues cannot be replaced by "\( \kappa_{\A}(\lambda) = 1 \) for every **simple** eigenvalue \( \lambda \)": give a non-normal \( \A \in M_3(\nC) \) with a simple eigenvalue, all of whose simple eigenvalues have condition number \( 1 \).
:::

*Hint: in (a), what does \( \kappa = 1 \) say about \( \y \), and what does the computation in @thm-left-right-biorthogonal say about \( \y_j^{*}\x_i \)?*
::::

::: {.solution}
(a) \( (\Rightarrow) \) This is @prp-eigenvalue-condition-properties (c).

\( (\Leftarrow) \) Let \( \lambda_1, \dots, \lambda_n \) be the distinct eigenvalues, with right eigenvectors \( \x_1, \dots, \x_n \). Since \( \kappa_{\A}(\lambda_j) = 1 \), @prp-eigenvalue-condition-properties (a) says that a left eigenvector for \( \lambda_j \) is a multiple of \( \x_j \), so \( \x_j \) itself is one: \( \x_j^{*}\A = \lambda_j\x_j^{*} \). Let \( i \ne j \). Computing \( \x_j^{*}\A\x_i \) in two ways,
\[
\lambda_j\,\x_j^{*}\x_i = (\x_j^{*}\A)\x_i = \x_j^{*}(\A\x_i) = \lambda_i\,\x_j^{*}\x_i ,
\]
so \( (\lambda_j - \lambda_i)\x_j^{*}\x_i = 0 \), and \( \x_j^{*}\x_i = 0 \) because \( \lambda_i \ne \lambda_j \). So the vectors \( \x_i/\norm{\x_i} \) form an orthonormal list of \( n \) vectors in \( \nC^n \), hence an orthonormal basis of eigenvectors. With \( \U \) the unitary matrix having these columns, \( \A = \U\diag(\lambda_1, \dots, \lambda_n)\U^{*} \), so \( \A \) is normal by @cor-spectral-complex-matrix.

(b) Let \( \A = \J_2(0) \oplus (1) = \begin{psmallmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{psmallmatrix} \). Its eigenvalues are \( 0, 0, 1 \), so \( 1 \) is the only simple eigenvalue. Its right and left eigenvectors are both \( \e_3 \), since \( \A\e_3 = \e_3 \) and \( \e_3^{*}\A = \e_3^{*} \), so \( \kappa_{\A}(1) = 1 \). But \( \A \) is not normal: \( \A^{*}\A = \diag(0, 1, 1) \) while \( \A\A^{*} = \diag(1, 0, 1) \).
:::

:::: {#exr-eigenvalue-condition-c2}
[C2: The derivatives add up to the trace]

Let \( \A \in M_n(\nC) \) have \( n \) distinct eigenvalues \( \lambda_1, \dots, \lambda_n \), and let \( \E \in M_n(\nC) \). Write \( \lambda_i(t) \) for the eigenvalue of \( \A + t\E \) near \( \lambda_i \), from @thm-simple-eigenvalue-derivative.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \lambda_1'(0) + \dots + \lambda_n'(0) = \tr\E \).
2. Deduce this again from \( \tr(\A + t\E) = \lambda_1(t) + \dots + \lambda_n(t) \), valid for all small \( t \), and explain why the two arguments agree.
:::

*Hint: in (a), use a diagonalizing \( \X \) and the rows of \( \X^{-1} \) as left eigenvectors.*
::::

::: {.solution}
(a) \( \A \) is diagonalizable by @cor-distinct-eigenvalues-diagonalizable, say \( \A = \X\vLambda\X^{-1} \). As in the proof of @prp-eigenvalue-condition-properties (d), \( \x_i = \X\e_i \) and \( \y_i^{*} = \e_i^{*}\X^{-1} \) are right and left eigenvectors for \( \lambda_i \), with \( \y_i^{*}\x_i = 1 \). So by @thm-simple-eigenvalue-derivative,
\[
\sum_{i=1}^{n}\lambda_i'(0)
= \sum_{i=1}^{n}\e_i^{*}\X^{-1}\E\X\e_i
= \tr(\X^{-1}\E\X) = \tr\E ,
\]
where the middle equality sums the diagonal entries of \( \X^{-1}\E\X \) and the last uses \( \tr(\B\C) = \tr(\C\B) \) (@thm-trace-properties (3)).

(b) Let \( g \) be the smallest distance between two of the \( \lambda_i \). By @thm-simple-eigenvalue-derivative (b), \( \lvert\lambda_i(t) - \lambda_i\rvert < g/2 \) for every \( i \) once \( \lvert t\rvert \) is small enough, so \( \lambda_1(t), \dots, \lambda_n(t) \) are \( n \) distinct eigenvalues of \( \A + t\E \). They are therefore all of its eigenvalues, each simple, and @thm-trace-det-eigenvalues gives \( \tr(\A + t\E) = \sum_i\lambda_i(t) \). The left side is \( \tr\A + t\tr\E \) and \( \tr\A = \sum_i\lambda_i \), so \( \sum_i(\lambda_i(t) - \lambda_i)/t = \tr\E \) for small \( t \ne 0 \). Letting \( t \to 0 \) and using (c) of the theorem for each \( i \) gives the claim. The two arguments agree because both express the same fact: the sum of the eigenvalues is a linear function of the matrix, so its derivative in the direction \( \E \) is \( \tr\E \), whatever the individual derivatives are.
:::

:::: {#exr-eigenvalue-condition-c3}
[C3: The adjugate at a simple eigenvalue]

Let \( n \ge 2 \), let \( \lambda \) be a simple eigenvalue of \( \A \in M_n(\nC) \) with right eigenvector \( \x \) and left eigenvector \( \y \), and put \( \N = \lambda\I - \A \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \adj\N = c\,\x\y^{*} \) for some scalar \( c \ne 0 \).
2. Prove that \( \tr(\adj\N) = p_{\A}'(\lambda) \), the derivative of the characteristic polynomial at \( \lambda \).
3. Deduce a second proof that \( \y^{*}\x \ne 0 \), and the formula
\[
\adj(\lambda\I - \A) = p_{\A}'(\lambda)\,\frac{\x\y^{*}}{\y^{*}\x} .
\]
:::

*Hint: for (a), use both products in @thm-adjugate-identity; for (b), apply @thm-derivative-of-det to \( t \mapsto (\lambda + t)\I - \A \).*
::::

::: {.solution}
(a) Since \( \lambda \) is an eigenvalue, \( \det\N = 0 \), so @thm-adjugate-identity gives \( \N\adj\N = \0 \) and \( \adj\N\,\N = \0 \). The first says every column of \( \adj\N \) lies in \( \ker(\lambda\I - \A) \), so by @lem-simple-eigenvalue-left-right (a) every column is a multiple of \( \x \): \( \adj\N = \x\w^{*} \) for some \( \w \in \nC^n \), whose conjugated entries are those multiples. Step 3 of the proof of @thm-simple-eigenvalue-derivative showed that \( \adj\N \ne \0 \), so \( \w \ne \0 \). The second identity gives \( \x(\w^{*}\N) = \0 \), and since \( \x \ne \0 \) this forces \( \w^{*}\N = \0 \), that is, \( \w^{*}\A = \lambda\w^{*} \). So \( \w \) is a left eigenvector, hence \( \w = \conj{c}\,\y \) for some \( c \ne 0 \) by @lem-simple-eigenvalue-left-right (a), and \( \adj\N = c\,\x\y^{*} \).

(b) Let \( \B(t) = (\lambda + t)\I - \A \) for real \( t \), so \( \B'(0) = \I \) and \( \B(0) = \N \). By @thm-derivative-of-det, \( t \mapsto \det\B(t) \) is differentiable at \( 0 \) with derivative \( \tr(\adj\N\,\I) = \tr(\adj\N) \). On the other hand \( \det\B(t) = p_{\A}(\lambda + t) \). Expanding each power \( (\lambda + t)^k \) by the binomial theorem gives \( p_{\A}(\lambda + t) = p_{\A}(\lambda) + p_{\A}'(\lambda)\,t + t^2h(t) \) for a polynomial \( h \), because the coefficient of \( t \) in \( \sum_k c_k(\lambda + t)^k \) is \( \sum_k kc_k\lambda^{k-1} = p_{\A}'(\lambda) \). So the difference quotient at \( 0 \) is \( p_{\A}'(\lambda) + t\,h(t) \to p_{\A}'(\lambda) \). The two derivatives agree: \( \tr(\adj\N) = p_{\A}'(\lambda) \).

(c) By (a) and (b), \( p_{\A}'(\lambda) = \tr(c\,\x\y^{*}) = c\,\y^{*}\x \), since the trace of \( \x\y^{*} \) is \( \sum_i x_i\conj{y_i} = \y^{*}\x \). Because \( \lambda \) is a simple root of \( p_{\A} \), @thm-repeated-root-derivative (a) gives \( p_{\A}'(\lambda) \ne 0 \). Hence \( \y^{*}\x \ne 0 \), which reproves @lem-simple-eigenvalue-left-right (b) from (a) of that lemma. Moreover \( c = p_{\A}'(\lambda)/(\y^{*}\x) \), which is the displayed formula. For example, for \( \A = \begin{psmallmatrix} 1 & M \\ 0 & 2 \end{psmallmatrix} \) and \( \lambda = 1 \), we have \( \adj(\I - \A) = \begin{psmallmatrix} -1 & M \\ 0 & 0 \end{psmallmatrix} \) and \( p_{\A}'(1) = -1 \), while \( \x\y^{*}/(\y^{*}\x) = \begin{psmallmatrix} 1 & -M \\ 0 & 0 \end{psmallmatrix} \), in agreement.
:::
