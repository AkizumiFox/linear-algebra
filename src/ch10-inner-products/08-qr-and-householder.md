# QR, Householder and Hessenberg

Section 2 turned a basis into an orthonormal basis one vector at a time, and every step was bookkeeping: each new vector recorded in terms of those already produced. Collect that bookkeeping into a matrix and the Gram–Schmidt process becomes a **factorization** \( \A = \Q\R \) — an orthogonal counterpart of the \( \L\U \) factorization of @def-lu-factorization. This section proves it and its uniqueness, then builds it a second time out of reflections, a route that survives dependent columns. The same reflections, applied on **both** sides, bring any square matrix to an almost-triangular form by a unitary similarity. Throughout, \( F \) is \( \nR \) or \( \nC \), and \( F^m \) carries the standard inner product, linear in the first slot.

## Gram–Schmidt in matrix form

Let \( \A \in M_{m \times n}(F) \) have columns \( \a_1, \dots, \a_n \), and suppose they are linearly independent. Apply @thm-gram-schmidt to the list \( (\a_1, \dots, \a_n) \). It returns an orthonormal list \( (\q_1, \dots, \q_n) \) in \( F^m \) with
\[
\Span(\q_1, \dots, \q_k) = \Span(\a_1, \dots, \a_k)
\]
for every \( k \). In particular \( \a_k \) lies in \( \Span(\q_1, \dots, \q_k) \), and @thm-orthonormal-coordinates (a), applied inside that subspace, expands it:
\[
\a_k = \sum_{i=1}^{k} \inner{\a_k}{\q_i}\,\q_i \qquad (k = 1, \dots, n).
\tag{$\ast$}
\]

Now read \( (\ast) \) as a matrix product. Put \( \Q = (\q_1 \mid \dots \mid \q_n) \in M_{m \times n}(F) \) and let \( \R \in M_n(F) \) have entries
\[
r_{ik} = \begin{cases} \inner{\a_k}{\q_i}, & i \le k, \\ 0, & i > k. \end{cases}
\]
Then \( \R \) is upper triangular (@def-upper-triangular), and \( (\ast) \) says that the \( k \)-th column of \( \A \) equals \( \Q \) times the \( k \)-th column of \( \R \). That is exactly \( \A = \Q\R \). **Nothing has been computed; the factorization is the Gram–Schmidt output, rewritten.**

Two features of the rewriting matter later. First the diagonal: in the notation of @thm-gram-schmidt, \( \q_k = \w_k/\norm{\w_k} \) with \( \w_k = \a_k - \sum_{i<k}\inner{\a_k}{\q_i}\q_i \), so comparing with \( (\ast) \) gives
\[
r_{kk} = \inner{\a_k}{\q_k} = \norm{\w_k} > 0 ,
\]
**strictly positive** because \( \w_k \neq \0 \). Second, \( \R \) is recoverable from \( \Q \) and \( \A \): since the columns of \( \Q \) are orthonormal,
\[
(\Q^{*}\Q)_{ij} = \sum_{p=1}^{m} \conj{q_{pi}}\,q_{pj} = \inner{\q_j}{\q_i} = \delta_{ij},
\]
by @def-conjugate-transpose, so \( \Q^{*}\Q = \I_n \) and \( \R = \Q^{*}\A \).

::: {#thm-qr-factorization}
[QR Factorization]

Let \( \A \in M_{m \times n}(F) \) have **linearly independent** columns. Then there are matrices \( \Q \in M_{m \times n}(F) \) and \( \R \in M_n(F) \) with

::: {.enumerate options="label=(\alph*)"}
1. the columns of \( \Q \) orthonormal, equivalently \( \Q^{*}\Q = \I_n \);
2. \( \R \) upper triangular with **positive real** diagonal entries;
3. \( \A = \Q\R \).
:::

Moreover \( \Q \) and \( \R \) are **unique**: any pair satisfying (a), (b), (c) is this one. The pair \( (\Q, \R) \) is the **QR factorization** of \( \A \).
:::

::: {.idea}
Existence is the paragraph above: run Gram–Schmidt and read off the coefficients. For uniqueness, suppose \( \Q_1\R_1 = \Q_2\R_2 \). We cannot cancel \( \Q \), which is not square, but \( \Q^{*}\Q = \I \) turns \( \A^{*}\A \) into \( \R^{*}\R \) and makes the \( \Q \)'s vanish. That leaves \( \R_1^{*}\R_1 = \R_2^{*}\R_2 \), so the matrix \( \S \) carrying \( \R_1 \) to \( \R_2 \) is upper triangular with positive diagonal and satisfies \( \S^{*}\S = \I \). Such a matrix has no room to be anything but \( \I \): column by column, orthogonality to the earlier columns kills every entry above the diagonal.
:::

::: {.proof}
*Existence.* Apply @thm-gram-schmidt to the columns of \( \A \), which is legitimate because they are independent, and define \( \Q \) and \( \R \) as above. Then (a) holds by orthonormality of the output, (b) holds because \( r_{kk} = \norm{\w_k} > 0 \), and (c) is \( (\ast) \).

*Uniqueness.* Suppose \( \A = \Q_1\R_1 = \Q_2\R_2 \) with both pairs satisfying (a) and (b). Each \( \R_t \) has non-zero diagonal entries, hence is invertible by @lem-triangular-invertible. Using \( \Q_t^{*}\Q_t = \I_n \) twice,
\[
\R_1^{*}\R_1 = \R_1^{*}\Q_1^{*}\Q_1\R_1 = \A^{*}\A = \R_2^{*}\Q_2^{*}\Q_2\R_2 = \R_2^{*}\R_2 .
\]
Put \( \S = \R_2\R_1^{-1} \), so that \( \R_2 = \S\R_1 \). The matrix \( \R_1^{-1} \) is upper triangular: its \( j \)-th column is the solution \( \x \) of \( \R_1\x = \e_j \), and solving from the bottom row upward gives \( x_i = 0 \) for every \( i > j \), exactly as in the proof of @lem-triangular-invertible. Hence \( \S \) is upper triangular, being a product of upper triangular matrices: in \( (\S)_{ij} = \sum_k (\R_2)_{ik}(\R_1^{-1})_{kj} \) a term can be non-zero only when \( i \le k \) and \( k \le j \), which is impossible for \( i > j \), and for \( i = j \) only the term \( k = i \) survives. So its diagonal entries are \( (\S)_{kk} = (\R_2)_{kk}(\R_1)_{kk}^{-1} > 0 \), a quotient of positive reals. Substituting \( \R_2 = \S\R_1 \) into the display gives \( \R_1^{*}\R_1 = \R_1^{*}\S^{*}\S\R_1 \), and multiplying by \( (\R_1^{*})^{-1} = (\R_1^{-1})^{*} \) on the left and \( \R_1^{-1} \) on the right leaves
\[
\S^{*}\S = \I_n .
\]

::: {.claim}
An upper triangular \( \S \in M_n(F) \) with \( \S^{*}\S = \I_n \) and positive real diagonal entries is \( \I_n \).
:::

::: {.proof}
Write \( \s_1, \dots, \s_n \) for the columns of \( \S \). As computed before the theorem, \( \S^{*}\S = \I_n \) says \( \inner{\s_j}{\s_i} = \delta_{ij} \). We show \( \s_j = \e_j \) by induction on \( j \). Let \( 1 \le j \le n \) and suppose \( \s_i = \e_i \) for every \( i < j \) (no assumption when \( j = 1 \)). For \( i < j \),
\[
0 = \inner{\s_j}{\s_i} = \inner{\s_j}{\e_i} = s_{ij},
\]
so every entry of \( \s_j \) above the diagonal vanishes; and \( s_{ij} = 0 \) for \( i > j \) because \( \S \) is upper triangular. Hence \( \s_j = s_{jj}\e_j \), and \( 1 = \inner{\s_j}{\s_j} = \lvert s_{jj}\rvert^2 \) forces \( \lvert s_{jj}\rvert = 1 \). Since \( s_{jj} > 0 \), this gives \( s_{jj} = 1 \) and \( \s_j = \e_j \).
:::

By the Claim, \( \S = \I_n \), so \( \R_2 = \R_1 \) and therefore \( \Q_2 = \A\R_2^{-1} = \A\R_1^{-1} = \Q_1 \). This proves uniqueness.
:::

The positivity in (b) is a normalization and nothing deeper: without it, scaling \( \q_k \) by any \( c \) of modulus \( 1 \) and row \( k \) of \( \R \) by \( \conj{c} \) gives another factorization. @exr-qr-and-householder-c1 describes all of them.

::: {.warning}
**In \( \A = \Q\R \) the matrix \( \Q \) is usually not square, and \( \Q\Q^{*} \neq \I \).** Only \( \Q^{*}\Q = \I_n \) holds. For the \( 3 \times 2 \) matrix of @exm-qr-3x2 below,
\[
\Q\Q^{*} = \tfrac{1}{18}\begin{pmatrix} 2 & 4 & 4 \\ 4 & 17 & -1 \\ 4 & -1 & 17 \end{pmatrix},
\]
whose trace is \( 2 \), not \( 3 \). This is the "identity on what?" trap of @thm-isometry-characterizations: the columns of \( \Q \) are an orthonormal basis of a **plane**, and \( \Q\Q^{*} \) is the orthogonal projection onto it (@thm-projection-formula).
:::

::: {.check}
Each factor of a QR factorization is recoverable from the other: \( \R = \Q^{*}\A \) and \( \Q = \A\R^{-1} \). One of the two recoveries needs an invertibility hypothesis and the other does not. Which, and why?
:::

::: {.solution}
The second. Multiplying \( \A = \Q\R \) on the left by \( \Q^{*} \) gives \( \Q^{*}\Q\R = \R \), which uses only \( \Q^{*}\Q = \I_n \): nothing is inverted, and \( \Q \) is not even square. Multiplying on the right by \( \R^{-1} \) presupposes that \( \R \) is invertible — true by @lem-triangular-invertible, but only because clause (b) makes the diagonal positive.
:::

## Least squares through QR

An inconsistent system \( \A\x = \b \) was handled in Section 4 by the normal equations \( \A^{*}\A\x = \A^{*}\b \) (@thm-least-squares). When the columns of \( \A \) are independent, the QR factorization simplifies those equations to a triangular system.

Substituting \( \A = \Q\R \) and using \( \Q^{*}\Q = \I_n \),
\[
\A^{*}\A = \R^{*}\Q^{*}\Q\R = \R^{*}\R,
\qquad
\A^{*}\b = \R^{*}\Q^{*}\b ,
\]
so the normal equations read \( \R^{*}\R\x = \R^{*}\Q^{*}\b \). Now \( \R \) is invertible by @lem-triangular-invertible, hence so is \( \R^{*} \), with \( (\R^{*})^{-1} = (\R^{-1})^{*} \) — conjugate-transpose \( \R\R^{-1} = \I_n \). So \( \R^{*} \) cancels:
\[
\R\x = \Q^{*}\b .
\tag{$\dagger$}
\]
By @cor-least-squares-unique the least-squares solution is unique here, and \( (\dagger) \) is a triangular system, solved by back substitution. The deeper reason to prefer it is not the operation count: forming \( \A^{*}\A \) squares the sensitivity of the problem to rounding, while \( (\dagger) \) never forms that product at all. Chapter 23 makes "sensitivity" precise and proves the comparison; here we record only the practice.

::: {#exm-qr-3x2}
[A \( 3 \times 2 \) QR, and a least-squares problem]

Let
\[
\A = \begin{pmatrix} 1 & 1 \\ 2 & 1 \\ 2 & 3 \end{pmatrix},
\qquad
\b = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} .
\]

::: {.enumerate options="label=(\alph*)"}
1. Find the QR factorization of \( \A \).
2. Find the \( \x \in \nR^2 \) minimizing \( \norm{\A\x - \b} \), using (a).
:::
:::

::: {.solution}
(a) Write \( \a_1 = (1,2,2) \) and \( \a_2 = (1,1,3) \). They are independent, since neither is a multiple of the other.

*Step 1.* \( \norm{\a_1}^2 = 1 + 4 + 4 = 9 \), so \( r_{11} = 3 \) and \( \q_1 = \tfrac13(1,2,2) \).

*Step 2.* \( r_{12} = \inner{\a_2}{\q_1} = \tfrac13(1 + 2 + 6) = 3 \), so
\[
\w_2 = (1,1,3) - 3 \cdot \tfrac13(1,2,2) = (0,-1,1),
\]
with \( \norm{\w_2} = \sqrt2 = r_{22} \) and \( \q_2 = \tfrac{1}{\sqrt2}(0,-1,1) \). Hence
\[
\Q = \begin{pmatrix}
\tfrac13 & 0 \\[2pt]
\tfrac23 & -\tfrac{1}{\sqrt2} \\[2pt]
\tfrac23 & \tfrac{1}{\sqrt2}
\end{pmatrix},
\qquad
\R = \begin{pmatrix} 3 & 3 \\ 0 & \sqrt2 \end{pmatrix}.
\]
*Check.* \( \Q\R \) has first column \( 3\q_1 = (1,2,2) \) and second column \( 3\q_1 + \sqrt2\,\q_2 = (1,2,2) + (0,-1,1) = (1,1,3) \), which is \( \A \).

(b) By \( (\dagger) \) we need \( \Q^{*}\b \). Here \( \inner{\b}{\q_1} = \tfrac13(1+2+2) = \tfrac53 \) and \( \inner{\b}{\q_2} = \tfrac{1}{\sqrt2}(0 - 1 + 1) = 0 \), so the system is
\[
\begin{pmatrix} 3 & 3 \\ 0 & \sqrt2 \end{pmatrix}\x = \begin{pmatrix} \tfrac53 \\ 0 \end{pmatrix}.
\]
Back substitution gives \( \sqrt2\,x_2 = 0 \), so \( x_2 = 0 \), and then \( 3x_1 = \tfrac53 \), so \( x_1 = \tfrac59 \). The minimizer is \( \x = (\tfrac59, 0) \).

*Check against the normal equations.* \( \A\tp\A = \begin{pmatrix} 9 & 9 \\ 9 & 11\end{pmatrix} \) and \( \A\tp\b = (5, 5) \). Subtracting the first equation from the second gives \( 2x_2 = 0 \), and then \( 9x_1 = 5 \). The same answer, with the same arithmetic done in a worse order.
:::

## Reflections

Gram–Schmidt builds \( \Q \) out of the columns of \( \A \). There is an entirely different route to a triangular \( \R \), modeled on elimination: hit \( \A \) on the left with simple matrices that create zeros, one column at a time, and collect the inverses. Chapter 2 used shears and got \( \A = \L\U \); if every matrix we hit \( \A \) with is **unitary** instead, the collected product is unitary and we get \( \A = \Q\R \). Which unitary matrices are simple enough? A rotation in the plane of two coordinates is one answer, taken up below. The more efficient answer is a reflection, because one reflection can flatten an entire column at once.

*A reflection in a hyperplane sends a vector to its mirror image: keep the part perpendicular to \( \w \), and reverse the part along \( \w \).*

::: {#def-householder-reflection}
[Householder Reflection]

Let \( \w \in F^m \) be **non-zero**. The **Householder reflection** determined by \( \w \) is
\[
\H_{\w} = \I_m - \frac{2\,\w\w^{*}}{\norm{\w}^2} \in M_m(F) .
\]
:::

In words: \( \w\w^{*} \) is an \( m \times m \) matrix (a column times a row), and for any \( \v \in F^m \) the product \( \w^{*}\v \) is the scalar \( \sum_p \conj{w_p}v_p = \inner{\v}{\w} \). So the definition says
\[
\H_{\w}\v = \v - 2\,\frac{\inner{\v}{\w}}{\norm{\w}^2}\,\w
= \v - 2P_{\Span(\w)}\v ,
\tag{$\ddagger$}
\]
where the last equality is @thm-projection-formula with the orthonormal basis \( (\w/\norm{\w}) \) of the line \( \Span(\w) \). Writing \( \v = P_{\Span(\w)}\v + (\v - P_{\Span(\w)}\v) \) as in @thm-orthogonal-decomposition, we see that \( \H_{\w} \) keeps the component of \( \v \) in \( \Span(\w)^{\perp} \) and reverses the component along \( \w \). That is a mirror reflection in the hyperplane \( \Span(\w)^{\perp} \).

Note at once that \( \H_{c\w} = \H_{\w} \) for every non-zero scalar \( c \), since \( (c\w)(c\w)^{*} = \lvert c\rvert^2\w\w^{*} \) and \( \norm{c\w}^2 = \lvert c\rvert^2\norm{\w}^2 \). **Only the line through \( \w \) matters.**

**Examples.**

- **The smallest case.** In \( F^1 \) take \( \w = 1 \): then \( \H_{\w} = -1 \), the map \( x \mapsto -x \). The "hyperplane" is \( \{0\} \), and this is the only non-trivial isometry of the line.
- **A coordinate reflection.** In \( \nR^2 \) take \( \w = \e_2 \), so \( \w\w\tp = \begin{pmatrix} 0&0\\0&1\end{pmatrix} \) and \( \H_{\w} = \diag(1, -1) \): the reflection in the \( x \)-axis.
- **A diagonal reflection.** In \( \nR^2 \) take \( \w = (1, -1) \), so \( \norm{\w}^2 = 2 \) and \( \H_{\w} = \I_2 - \begin{pmatrix} 1&-1\\-1&1\end{pmatrix} = \begin{pmatrix} 0&1\\1&0\end{pmatrix} \), which swaps the coordinates. It is the reflection in the line \( y = x \), and \( \Span(\w)^{\perp} \) is that line.
- **A complex one.** In \( \nC^m \) take \( \w = \e_1 \): then \( \H_{\w} = \diag(-1, 1, \dots, 1) \), over either field.

**Non-example by minimal change.** Drop the factor \( 2 \): the matrix \( \I_m - \w\w^{*}/\norm{\w}^2 \) is \( \I_m - P_{\Span(\w)} \), the orthogonal projection onto \( \Span(\w)^{\perp} \). It is Hermitian, as \( \H_{\w} \) is, but **not** unitary and not invertible: it sends \( \w \) to \( \0 \). Halving the coefficient turns "reverse the component along \( \w \)" into "delete it", an isometry into a shadow.

::: {#prp-householder-properties}
[Properties of a Householder Reflection]

Let \( \w \in F^m \) be non-zero and \( \H = \H_{\w} \). Then

::: {.enumerate options="label=(\alph*)"}
1. \( \H^{*} = \H \) (\( \H \) is Hermitian);
2. \( \H^2 = \I_m \), so \( \H^{-1} = \H \);
3. \( \H \) is unitary;
4. \( \H\w = -\w \), and \( \H\v = \v \) for every \( \v \perp \w \);
5. \( \det \H = -1 \).
:::
:::

::: {.proof}
(a) By @def-conjugate-transpose, \( (\w\w^{*})^{*} = \w^{**}\w^{*} = \w\w^{*} \), and \( \norm{\w}^2 \) is a real number (@thm-inner-product-basic-properties (a)), so \( \H^{*} = \I_m - 2\w\w^{*}/\norm{\w}^2 = \H \).

(b) Since \( \w^{*}\w = \inner{\w}{\w} = \norm{\w}^2 \),
\[
\H^2 = \I_m - \frac{4\w\w^{*}}{\norm{\w}^2} + \frac{4\,\w(\w^{*}\w)\w^{*}}{\norm{\w}^4}
= \I_m ,
\]
because the last two terms cancel.

(c) By (a) and (b), \( \H^{*}\H = \H^2 = \I_m \), which is the criterion of @def-unitary-orthogonal.

(d) Both statements are read off \( (\ddagger) \): \( P_{\Span(\w)}\w = \w \) gives \( \H\w = \w - 2\w = -\w \), and \( \inner{\v}{\w} = 0 \) gives \( \H\v = \v \).

(e) Extend the unit vector \( \w/\norm{\w} \) to an orthonormal basis \( (\f_1, \dots, \f_m) \) of \( F^m \) with \( \f_1 = \w/\norm{\w} \), which is possible by @cor-extend-orthonormal-basis, and let \( \P = (\f_1 \mid \dots \mid \f_m) \). By (d), \( \H\f_1 = -\f_1 \) and \( \H\f_i = \f_i \) for \( i \ge 2 \), that is, \( \H\P = \P\D \) with \( \D = \diag(-1, 1, \dots, 1) \). The matrix \( \P \) is unitary, hence invertible, so \( \H = \P\D\P^{-1} \). Taking determinants, \( \det \H = \det\D \) by @thm-det-multiplicative and @cor-det-inverse, and \( \det \D = -1 \) by @thm-det-triangular.
:::

So a Householder reflection is a unitary involution of determinant \( -1 \): cheap to store (one vector) and cheap to apply, by \( (\ddagger) \). What makes it useful is the following choice of \( \w \).

::: {#thm-householder-maps-vector}
[A Reflection Flattening a Vector]

Let \( \x \in F^m \) be non-zero, and let
\[
\alpha = \begin{cases} x_1/\lvert x_1\rvert, & x_1 \neq 0, \\ 1, & x_1 = 0, \end{cases}
\qquad
\w = \x + \alpha\norm{\x}\,\e_1 .
\]
Then \( \w \neq \0 \) and
\[
\H_{\w}\,\x = -\alpha\norm{\x}\,\e_1 .
\]
In particular \( \H_{\w}\x \) is a multiple of \( \e_1 \) of length \( \norm{\x} \). Over \( \nR \), \( \alpha \) is the sign of \( x_1 \) (or \( 1 \) if \( x_1 = 0 \)), and \( \H_{\w}\x = \mp\norm{\x}\e_1 \) according to that sign.
:::

::: {.idea}
Picture the real plane. We want a mirror line taking \( \x \) to a point on the first axis at the same distance from the origin. There are two such points, \( \pm\norm{\x}\e_1 \), and for each the mirror is the perpendicular bisector of the segment joining \( \x \) to it — whose normal direction is the **difference** \( \x \mp \norm{\x}\e_1 \). So the vector \( \w \) is forced, up to which of the two targets we aim at, and all that remains is to check that the coefficient \( 2\inner{\x}{\w}/\norm{\w}^2 \) in \( (\ddagger) \) comes out exactly \( 1 \), so that \( \H_{\w}\x = \x - \w \). The role of \( \alpha \) is to choose the target on the far side from \( \x \).
:::

::: {.proof}
Note first that \( \conj{\alpha}x_1 = \lvert x_1\rvert \) in both cases, and \( \lvert \alpha\rvert = 1 \). Expanding with (IP1) and @thm-inner-product-basic-properties (b),
\[
\begin{aligned}
\norm{\w}^2 &= \norm{\x}^2 + \conj{\alpha}\norm{\x}\inner{\x}{\e_1} + \alpha\norm{\x}\inner{\e_1}{\x} + \lvert\alpha\rvert^2\norm{\x}^2 \\
&= 2\norm{\x}^2 + 2\norm{\x}\,\lvert x_1\rvert ,
\end{aligned}
\]
where the second line uses \( \inner{\x}{\e_1} = x_1 \), \( \inner{\e_1}{\x} = \conj{x_1} \) and \( \conj{\alpha}x_1 + \alpha\conj{x_1} = 2\lvert x_1\rvert \). Since \( \x \neq \0 \) we have \( \norm{\x} > 0 \), so \( \norm{\w}^2 > 0 \) and \( \w \neq \0 \). Likewise
\[
\inner{\x}{\w} = \norm{\x}^2 + \conj{\alpha}\norm{\x}\,x_1 = \norm{\x}^2 + \norm{\x}\lvert x_1\rvert ,
\]
so that \( 2\inner{\x}{\w} = \norm{\w}^2 \). Hence by \( (\ddagger) \),
\[
\H_{\w}\x = \x - \frac{2\inner{\x}{\w}}{\norm{\w}^2}\,\w = \x - \w = -\alpha\norm{\x}\,\e_1 .
\]
Finally \( \norm{-\alpha\norm{\x}\e_1} = \lvert\alpha\rvert\norm{\x} = \norm{\x} \) by @thm-norm-properties (b), as it must be, since \( \H_{\w} \) is unitary. This proves the theorem.
:::

**Why that sign.** The opposite choice \( \w' = \x - \alpha\norm{\x}\e_1 \) also works whenever \( \w' \neq \0 \), giving \( \H_{\w'}\x = +\alpha\norm{\x}\e_1 \); in exact arithmetic the two are equally good, and in floating point they are not. The first entry of \( \w' \) is \( x_1 - \alpha\norm{\x} \), a difference of two numbers of modulus \( \lvert x_1\rvert \) and \( \norm{\x} \) — and when \( \x \) is close to a multiple of \( \e_1 \) those two are nearly equal, so the leading digits cancel and the computed first entry keeps only the few digits they did not share. The other entries of \( \w' \) are copied from \( \x \) and stay exact, so the computed \( \w' \) points in a noticeably wrong direction, and so does the reflection built from it. With \( \w = \x + \alpha\norm{\x}\e_1 \) the first entry has modulus \( \lvert x_1\rvert + \norm{\x} \): like-signed quantities, nothing to cancel. (The same computation shows \( \w \ne \0 \) always, whereas \( \w' = \0 \) exactly when \( \x = \alpha\norm{\x}\e_1 \), the extreme case of that cancellation.) Chapter 23 quantifies the loss; the summary here is that both signs are correct mathematics and only one is correct arithmetic.

::: {.warning}
**Do not build the matrix \( \H_{\w} \) in order to use it.** Forming it and multiplying costs \( m^2 \) operations per column, while \( (\ddagger) \) applies the same reflection with one inner product and one scaled subtraction, about \( 4m \). Every "multiply by \( \H \)" below is really an instance of \( (\ddagger) \); the matrix is a proof device.
:::

::: {.check}
Let \( \x = (0, 3, 4) \in \nR^3 \). Find \( \w \) and \( \H_{\w}\x \) as in @thm-householder-maps-vector, and say why the sign question does not arise here.
:::

::: {.solution}
\( \norm{\x} = 5 \) and \( x_1 = 0 \), so \( \alpha = 1 \) and \( \w = (0,3,4) + 5(1,0,0) = (5,3,4) \). Then \( \H_{\w}\x = -5\e_1 = (-5,0,0) \). With \( x_1 = 0 \) there is no cancellation to avoid: the first entry of \( \w \) is \( 0 \pm 5 \) either way, and both choices are equally accurate. The convention \( \alpha = 1 \) is only a convention.
:::

## QR by reflections

One reflection makes the first column a multiple of \( \e_1 \) — exactly the zeros an upper triangular matrix needs in column \( 1 \). Repeating on the trailing submatrix triangularizes everything.

::: {#thm-qr-householder}
[QR by Householder Reflections]

Let \( \A \in M_{m \times n}(F) \). Then there are a **unitary** \( \Q \in M_m(F) \) and an \( \R \in M_{m \times n}(F) \) with \( r_{ij} = 0 \) whenever \( i > j \), such that
\[
\A = \Q\R .
\]
Moreover \( \Q \) can be taken to be a product of at most \( \min(n, m-1) \) Householder reflections. **No hypothesis on the columns of \( \A \) is needed.**
:::

::: {.idea}
Induction on the number of columns. Step one is @thm-householder-maps-vector applied to the first column: after it, the first column is \( \rho\e_1 \) and what is left to triangularize is the trailing \( (m-1) \times (n-1) \) block. Feed that block to the induction hypothesis, and lift the unitary matrix it returns to \( F^m \) by putting a \( 1 \) in the top-left corner — a block matrix of that shape does not touch the first row or the first column, so it cannot spoil the zeros just created.
:::

::: {.proof}
We induct on \( n \), the statement being asserted for every \( m \ge 1 \) at once.

If \( m = 1 \), then \( \A \) has no entries below its diagonal, so \( \Q = \I_1 \) and \( \R = \A \) work. Assume from now on that \( m \ge 2 \).

Let \( \a \) be the first column of \( \A \). If \( \a = \0 \), put \( \H = \I_m \) and \( \rho = 0 \); otherwise let \( \H = \H_{\w} \) be the reflection of @thm-householder-maps-vector for \( \x = \a \), and \( \rho = -\alpha\norm{\a} \). In both cases \( \H \) is unitary and Hermitian with \( \H^{-1} = \H \) — by @prp-householder-properties (a)–(c) for a reflection, and because \( \I_m^{*} = \I_m = \I_m^{-1} \) in the degenerate case — and \( \H\a = \rho\e_1 \). Hence, by @thm-block-multiplication,
\[
\H\A = \begin{pmatrix} \rho & \b^{*} \\ \0 & \A' \end{pmatrix}
\]
for some \( \b \in F^{n-1} \) and \( \A' \in M_{(m-1)\times(n-1)}(F) \), where the \( \0 \) is a column of \( m - 1 \) zeros.

*Base case \( n = 1 \).* There is no block \( \A' \), and \( \H\A = \rho\e_1 \) already has \( r_{i1} = 0 \) for \( i > 1 \). So \( \A = \H(\H\A) \) is of the required form with \( \Q = \H \).

*Induction step.* Let \( n \ge 2 \) and assume the statement for \( n - 1 \) columns. Applied to \( \A' \), which has \( m - 1 \ge 1 \) rows, it gives a unitary \( \Q' \in M_{m-1}(F) \) and an \( \R' \) with zeros below the diagonal and \( \A' = \Q'\R' \). Put
\[
\U = \begin{pmatrix} 1 & \0^{*} \\ \0 & \Q' \end{pmatrix},
\qquad
\R = \begin{pmatrix} \rho & \b^{*} \\ \0 & \R' \end{pmatrix} .
\]
Then \( \U^{*}\U = \I_m \) by @thm-block-multiplication, so \( \U \) is unitary, and \( \U\R = \H\A \) by the same computation. Also \( \R \) has zeros below its diagonal: in column \( 1 \) this is the block \( \0 \); and for \( j \ge 2 \) and \( i > j \), the \( (i, j) \)-entry of \( \R \) is the \( (i-1, j-1) \)-entry of \( \R' \), which vanishes because \( i - 1 > j - 1 \).

Therefore \( \A = \H\U\R \), and \( \Q = \H\U \) is unitary as a product of unitary matrices (@prp-orthogonal-group-properties). Unwinding the induction, \( \Q \) is a product of one reflection (or \( \I_m \)) for each of the columns \( 1, \dots, \min(n, m-1) \), since the recursion stops once one row is left. This proves the theorem.
:::

::: {#exm-householder-3x3}
[A \( 3 \times 3 \) QR by reflections]

Triangularize
\[
\A = \begin{pmatrix} 2 & 0 & 1 \\ 1 & 5 & 2 \\ 2 & 5 & 4 \end{pmatrix}
\]
by Householder reflections, and read off \( \Q \) and \( \R \).
:::

::: {.solution}
*Step 1.* The first column is \( \a = (2,1,2) \) with \( \norm{\a} = 3 \) and \( a_1 = 2 > 0 \), so \( \alpha = 1 \) and
\[
\w_1 = (2,1,2) + 3(1,0,0) = (5,1,2), \qquad \norm{\w_1}^2 = 30 .
\]
Apply \( (\ddagger) \) to each column: \( \H_1\v = \v - \tfrac{1}{15}\inner{\v}{\w_1}\w_1 \). All three columns pair with \( \w_1 \) to give \( 15 \), so each loses exactly one copy of \( \w_1 \):
\[
\H_1\A = \begin{pmatrix} -3 & -5 & -4 \\ 0 & 4 & 1 \\ 0 & 3 & 2 \end{pmatrix}.
\]
(As predicted, the first column is \( -\norm{\a}\e_1 \).)

*Step 2.* Work now in the trailing \( 2 \times 2 \) block, whose first column is \( \y = (4,3) \) with \( \norm{\y} = 5 \) and \( y_1 > 0 \). So \( \w_2 = (9,3) \), and inside \( \nR^3 \) we reflect in \( \widetilde{\w}_2 = (0,9,3) \), which fixes \( \e_1 \) and so leaves column \( 1 \) alone; here \( \H_2\v = \v - \tfrac{1}{45}\inner{\v}{\widetilde{\w}_2}\,\widetilde{\w}_2 \). The second and third columns of \( \H_1\A \) pair with \( \widetilde{\w}_2 \) to give \( 36 + 9 = 45 \) and \( 9 + 6 = 15 \), so they lose one copy and a third of a copy respectively:
\[
\R = \H_2\H_1\A = \begin{pmatrix} -3 & -5 & -4 \\ 0 & -5 & -2 \\ 0 & 0 & 1 \end{pmatrix}.
\]

*The unitary factor.* By @prp-householder-properties (b), \( \A = \H_1\H_2\R \), so \( \Q = \H_1\H_2 \). Computing the product,
\[
\Q = \tfrac13\begin{pmatrix} -2 & 2 & -1 \\ -1 & -2 & -2 \\ -2 & -1 & 2 \end{pmatrix},
\]
whose columns have length \( 1 \) and are pairwise orthogonal, as one checks from the integer entries: for instance \( (-2)(2) + (-1)(-2) + (-2)(-1) = 0 \).

*Check.* \( \det \A = 15 \) by expansion along the first row, and \( \det \R = (-3)(-5)(1) = 15 \) by @thm-det-triangular, consistent with \( \det \Q = (-1)(-1) = 1 \) from @prp-householder-properties (e).
:::

The diagonal of \( \R \) here is \( (-3, -5, 1) \), not positive: the reflection route produces **a** factorization, not **the** one of @thm-qr-factorization. The two are related by flipping the sign of each row of \( \R \) with a negative diagonal entry, and of the matching column of \( \Q \); @exr-qr-and-householder-b2 carries this out on the matrix of @exm-qr-3x2.

::: {.warning}
**"The QR factorization" is definite only with the positivity normalization.** @thm-qr-factorization pins the pair down by demanding \( r_{kk} > 0 \); the reflection algorithm ignores that demand and chooses signs for stability instead. So two correct computations of "the QR factorization of \( \A \)" can differ by signs. Compare \( \lvert r_{kk}\rvert \), and the lines spanned by the columns of \( \Q \).
:::

**Where Gram–Schmidt cannot follow.** @thm-qr-householder assumed nothing about the columns, and that is a genuine gain. Let the columns of \( \A \) be dependent, and let \( k \) be the first index with \( \a_k \in \Span(\a_1, \dots, \a_{k-1}) \). The Gram–Schmidt recursion then produces \( \w_k = \0 \) and stops, because the next step divides by \( \norm{\w_k} \); @exr-orthonormal-bases-c2 works this out. Nor is the failure an artifact of the method: if \( \A = \Q\R \) with \( \Q^{*}\Q = \I_n \) and \( \R \) upper triangular with positive diagonal, then \( \R \) is invertible by @lem-triangular-invertible, so \( \rank \A = \rank \Q = n \) and the columns were independent after all. **A QR factorization in the sense of @thm-qr-factorization exists exactly for matrices of full column rank.** The reflection route is untroubled: a dependent column simply puts a zero on the diagonal of \( \R \) where the dependence appears, and the algorithm continues (@exr-qr-and-householder-c2).

## Givens rotations

A reflection zeroes a whole column at once. Sometimes that is too much: if \( \A \) is nearly triangular already, we would rather kill the few offending entries one at a time and leave the rest alone.

::: {#def-givens-rotation}
[Givens Rotation]

Let \( 1 \le i < j \le m \) and let \( c, s \in \nR \) with \( c^2 + s^2 = 1 \). The **Givens rotation** \( \G(i, j; c, s) \in M_m(\nR) \) is the identity matrix with the four entries in rows and columns \( i, j \) replaced by
\[
\begin{pmatrix} g_{ii} & g_{ij} \\ g_{ji} & g_{jj} \end{pmatrix}
= \begin{pmatrix} c & s \\ -s & c \end{pmatrix} .
\]
:::

The two columns involved are orthonormal, since \( c^2 + s^2 = 1 \) and \( cs - sc = 0 \), and every other column of \( \G \) is a standard basis vector, orthogonal to both; so \( \G\tp\G = \I_m \) and \( \G \) is orthogonal, with \( \det\G = c^2 + s^2 = 1 \) by expansion along those other columns (@thm-laplace-expansion). Moreover \( \G \) acts as the identity on every coordinate other than \( i \) and \( j \). Given a vector \( \v \) with \( (v_i, v_j) \neq (0,0) \), set
\[
r = \sqrt{v_i^2 + v_j^2}, \qquad c = \frac{v_i}{r}, \qquad s = \frac{v_j}{r} .
\]
Then the \( i \)-th entry of \( \G\v \) is \( (v_i^2 + v_j^2)/r = r \) and the \( j \)-th is \( (-v_jv_i + v_iv_j)/r = 0 \), while every other entry is unchanged. **One rotation, one new zero.**

Here is one rotation at work. To clear the \( (3,1) \)-entry of the matrix \( \A \) below, take \( i = 1 \), \( j = 3 \) and for \( \v \) its first column, so that \( (v_1, v_3) = (3, 4) \) and \( r = 5 \), \( c = \tfrac35 \), \( s = \tfrac45 \). Then \( \G = \G(1, 3; \tfrac35, \tfrac45) \) replaces row \( 1 \) by \( \tfrac35(\text{row } 1) + \tfrac45(\text{row } 3) \) and row \( 3 \) by \( -\tfrac45(\text{row } 1) + \tfrac35(\text{row } 3) \), and leaves row \( 2 \) alone:
\[
\A = \begin{pmatrix} 3 & 5 & 0 \\ 0 & 2 & 1 \\ 4 & 0 & 5 \end{pmatrix},
\qquad
\G\A = \begin{pmatrix} 5 & 3 & 4 \\ 0 & 2 & 1 \\ 0 & -4 & 3 \end{pmatrix} .
\]
The new \( (1,1) \)-entry is \( \tfrac15(3 \cdot 3 + 4 \cdot 4) = 5 = r \) and the new \( (3,1) \)-entry is \( \tfrac15(-4 \cdot 3 + 3 \cdot 4) = 0 \), as designed; the zero already sitting in position \( (2,1) \) survives because row \( 2 \) was never touched. A reflection would have flattened the whole first column in one step, at the price of rewriting row \( 2 \) as well.

Applied in a suitable order, rotations triangularize any real matrix, which is a second proof of @thm-qr-householder over \( \nR \) at the cost of more steps: a full \( m \times n \) matrix needs about \( mn \) rotations where reflections need \( n \). For a nearly triangular matrix the count reverses, which is why the Hessenberg matrices below are handled with rotations in practice. Over \( \nC \) one takes \( c \in \nR \), \( s \in \nC \) with \( c^2 + \lvert s\rvert^2 = 1 \), and \( -\conj{s} \) in place of \( -s \); to zero the \( j \)-th entry of \( \v \) one puts \( r = \sqrt{\lvert v_i\rvert^2 + \lvert v_j\rvert^2} \) and takes \( c = \lvert v_i\rvert/r \) and \( s = (v_i/\lvert v_i\rvert)\conj{v_j}/r \) when \( v_i \neq 0 \), and \( c = 0 \), \( s = 1 \) when \( v_i = 0 \).

## Hessenberg form

So far the unitary matrices acted on one side. A similarity needs both: to preserve eigenvalues we must pass from \( \A \) to \( \Q^{*}\A\Q \), not to \( \Q^{*}\A \). What can reflections achieve under that constraint?

Not triangularity, and the reason is worth seeing before the theorem. Suppose we reflect so that the first column becomes \( \rho\e_1 \). Multiplying on the right must not disturb column \( 1 \), so the right factor must fix \( \e_1 \) — and so must the left factor, since they are the same matrix. But a reflection fixing \( \e_1 \) acts only on the coordinates \( 2, \dots, n \), so in column \( 1 \) the best it can do is compress rows \( 2, \dots, n \) into row \( 2 \). **The entry just below the diagonal survives, by necessity.** That is exactly the pattern we can reach.

::: {#thm-hessenberg-form}
[Reduction to Hessenberg Form]

Let \( \A \in M_n(F) \), \( n \ge 1 \). Then there is a unitary \( \Q \in M_n(F) \) such that \( \Z = \Q^{*}\A\Q \) is **upper Hessenberg**, that is,
\[
z_{ij} = 0 \qquad \text{whenever } i > j + 1 .
\]
The matrix \( \Q \) can be taken to be a product of \( n - 2 \) factors, each a Householder reflection or an identity matrix (and \( \Q = \I_n \) when \( n \le 2 \)). For \( n = 4 \) the pattern is
\[
\Z = \begin{pmatrix}
\ast & \ast & \ast & \ast \\
\ast & \ast & \ast & \ast \\
0 & \ast & \ast & \ast \\
0 & 0 & \ast & \ast
\end{pmatrix}.
\]
:::

::: {.idea}
Work column by column, as in @thm-qr-householder, but apply each reflection on both sides. At step \( k \) it is chosen to fix \( \e_1, \dots, \e_k \) and to flatten the part of column \( k \) in rows \( k+1, \dots, n \). Two observations do the bookkeeping. On the **left** it only recombines rows \( k+1, \dots, n \), and in the earlier columns those rows are already zero, so a combination of them is still zero. On the **right** it only recombines columns \( k+1, \dots, n \), so the columns already in shape are untouched.
:::

::: {.proof}
For \( 0 \le k \le n-2 \) say that \( \B \in M_n(F) \) satisfies \( (\ast_k) \) if \( b_{ij} = 0 \) whenever \( j \le k \) and \( i \ge j + 2 \). Every matrix satisfies \( (\ast_0) \) vacuously, and \( (\ast_{n-2}) \) says precisely that \( \B \) is upper Hessenberg, since the conditions with \( j = n-1 \) and \( j = n \) are empty.

Put \( \A_0 = \A \). Let \( 1 \le k \le n - 2 \) and suppose \( \A_{k-1} \) satisfies \( (\ast_{k-1}) \). Let \( \a \in F^{n-k} \) be the vector of entries in rows \( k+1, \dots, n \) of column \( k \) of \( \A_{k-1} \). If \( \a = \0 \), put \( \H_k = \I_{n-k} \); otherwise let \( \H_k \in M_{n-k}(F) \) be the reflection of @thm-householder-maps-vector with \( \H_k\a = \rho\e_1 \), where \( \rho = -\alpha\norm{\a} \). Set
\[
\Q_k = \begin{pmatrix} \I_k & \0 \\ \0 & \H_k\end{pmatrix} \in M_n(F),
\qquad
\A_k = \Q_k\A_{k-1}\Q_k .
\]
The block \( \H_k \) is unitary and Hermitian with \( \H_k^{-1} = \H_k \) — by @prp-householder-properties (a)–(c) for a reflection, and because \( \I_{n-k}^{*} = \I_{n-k} = \I_{n-k}^{-1} \) otherwise — so by @thm-block-multiplication \( \Q_k \) is unitary and Hermitian with \( \Q_k^{-1} = \Q_k \), and \( \Q_k\e_j = \e_j \) for every \( j \le k \).

**Claim 1.** \( \Q_k\A_{k-1} \) satisfies \( (\ast_{k-1}) \), and its entries in rows \( i \ge k+2 \) of column \( k \) are \( 0 \).

::: {.proof}
By @thm-block-multiplication, the rows \( 1, \dots, k \) of \( \Q_k\A_{k-1} \) are those of \( \A_{k-1} \), and each of the rows \( k+1, \dots, n \) is a linear combination of the rows \( k+1, \dots, n \) of \( \A_{k-1} \). Fix a column \( j \le k - 1 \). By \( (\ast_{k-1}) \), the entries of that column in rows \( i \ge j+2 \) vanish, and \( k + 1 \ge j + 2 \), so all the entries being combined are \( 0 \) and the combination is \( 0 \). Hence \( (\ast_{k-1}) \) survives. In column \( k \), the entries in rows \( k+1, \dots, n \) form the vector \( \H_k\a = \rho\e_1 \), whose entries after the first are \( 0 \); these sit in rows \( k+2, \dots, n \).
:::

**Claim 2.** \( \A_k = (\Q_k\A_{k-1})\Q_k \) has the same first \( k \) columns as \( \Q_k\A_{k-1} \).

::: {.proof}
For \( j \le k \), the \( j \)-th column of \( \B\Q_k \) is \( \B(\Q_k\e_j) = \B\e_j \), the \( j \)-th column of \( \B \).
:::

Combining the two claims, \( \A_k \) satisfies \( (\ast_k) \): columns \( 1, \dots, k-1 \) keep the zeros guaranteed by Claim 1, and column \( k \) has zeros in rows \( k+2, \dots, n \), also by Claim 1, and both survive the right multiplication by Claim 2.

Running \( k = 1, \dots, n-2 \) produces \( \A_{n-2} \) satisfying \( (\ast_{n-2}) \), that is, upper Hessenberg. Put \( \Q = \Q_1\Q_2\cdots\Q_{n-2} \), unitary as a product of unitary matrices (@prp-orthogonal-group-properties). Since each \( \Q_k^{*} = \Q_k \),
\[
\Q^{*}\A\Q = \Q_{n-2}\cdots\Q_1\,\A\,\Q_1\cdots\Q_{n-2} = \A_{n-2},
\]
which proves the theorem. (For \( n \le 2 \) there are no steps and every matrix is already Hessenberg.)
:::

Because \( \Q^{-1} = \Q^{*} \), the matrices \( \A \) and \( \Z \) are similar (@def-similar-matrices), so they share their characteristic polynomial, their eigenvalues and their trace. The reduction is not merely tidying: it removes \( \binom{n-1}{2} \) entries and keeps **the whole spectrum**.

::: {#exm-hessenberg-3x3}
[Hessenberg form of a \( 3 \times 3 \) matrix]

Reduce
\[
\A = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 3 & 1 \\ 1 & 0 & 4 \end{pmatrix}
\]
to upper Hessenberg form by a unitary similarity.
:::

::: {.solution}
Only \( k = 1 \) occurs, and only the entry \( a_{31} \) has to be killed. The relevant vector is \( \a = (a_{21}, a_{31}) = (0, 1) \in \nR^2 \), with \( \norm{\a} = 1 \) and \( a_1 = 0 \), so \( \alpha = 1 \) and
\[
\w = (0,1) + (1,0) = (1,1), \qquad \norm{\w}^2 = 2 .
\]
Hence \( \H_1 = \I_2 - \w\w\tp = \begin{pmatrix} 0 & -1 \\ -1 & 0\end{pmatrix} \), and
\[
\Q_1 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & -1 & 0\end{pmatrix}.
\]
Left multiplication by \( \Q_1 \) exchanges rows \( 2 \) and \( 3 \) and negates them, and right multiplication does the same to columns \( 2 \) and \( 3 \):
\[
\Q_1\A = \begin{pmatrix} 2 & 1 & 0 \\ -1 & 0 & -4 \\ 0 & -3 & -1\end{pmatrix},
\qquad
\Q_1\A\Q_1 = \begin{pmatrix} 2 & 0 & -1 \\ -1 & 4 & 0 \\ 0 & 1 & 3\end{pmatrix} .
\]
Entry \( (3,1) \) is \( 0 \) and entry \( (2,1) \) is \( -1 = -\norm{\a} \), as @thm-householder-maps-vector predicts. Watch column \( 1 \) through the second multiplication: it is untouched, because \( \Q_1\e_1 = \e_1 \). Both matrices have trace \( 9 \), as similarity requires.
:::

::: {.warning}
**Hessenberg form is not one small step from triangular form.** A few more reflections will not clear the subdiagonal, and not merely because the argument above breaks. The diagonal of a triangular matrix similar to \( \A \) lists the eigenvalues of \( \A \) (@thm-diagonal-of-triangular-form), so a finite procedure using only arithmetic and square roots that always produced one would extract the roots of an arbitrary polynomial from its coefficients by those operations alone. No such procedure exists: from degree five on, the roots of a general polynomial cannot be written with arithmetic and radicals at all. That is a theorem of Abel and Ruffini, which this book does not prove and which nothing later depends on; we quote it only to explain why the algorithms of Chapter 23 iterate instead of terminating. Over \( \nC \) a triangularizing unitary does exist (@thm-triangularization); what does not exist is a finite algorithm of this kind producing it. Over \( \nR \) even the existence fails: a rotation in \( \Orth(2) \) with no real eigenvalue is already Hessenberg and is orthogonally similar to no real triangular matrix.
:::

Hessenberg form is where the practical computation of eigenvalues begins. One applies the reduction once, then iterates a cheap step that preserves the pattern: factor \( \Z = \Q\R \) and replace \( \Z \) by \( \R\Q = \Q^{*}\Z\Q \), again a unitary similarity. Chapter 23 develops that iteration and explains why every implementation starts with the reduction proved here.

::: {.check}
In the reduction of a \( 5 \times 5 \) matrix, how many reflections are used, and how many entries does the second one set to zero?
:::

::: {.solution}
Three, namely \( k = 1, 2, 3 \). The step \( k = 2 \) chooses a reflection acting on the coordinates \( 3, 4, 5 \) and sets the entries in rows \( 4 \) and \( 5 \) of column \( 2 \) to zero: two entries. (Step \( 1 \) sets three, step \( 3 \) sets one, for \( \binom{4}{2} = 6 \) in total.)
:::

## Exercises

### A. Check your understanding

:::: {#exr-qr-and-householder-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State @thm-qr-factorization in full, including the two normalizations that make \( \Q \) and \( \R \) unique.
2. Which hypothesis on \( \A \) does @thm-qr-factorization need, and which does @thm-qr-householder need? Explain the difference in one sentence.
3. Write down the Householder reflection determined by \( \w \), and list three of its properties.
4. In @thm-householder-maps-vector, which of the two possible targets \( \pm\norm{\x}\e_1 \) is chosen, and why?
5. True or false: applying reflections on both sides, as in @thm-hessenberg-form, can be pushed to make every complex matrix unitarily similar to an upper triangular one. Justify your answer.
6. Why must the reflection used at step \( k \) of @thm-hessenberg-form fix \( \e_1, \dots, \e_k \)?
:::
::::

::: {.solution}
(a) If the columns of \( \A \in M_{m\times n}(F) \) are independent, then \( \A = \Q\R \) with \( \R \) upper triangular; the normalizations are that the columns of \( \Q \) are **orthonormal** and that the diagonal of \( \R \) is **positive real**. With both, the pair is unique.

(b) @thm-qr-factorization needs independent columns; @thm-qr-householder needs nothing. A positive diagonal forces \( \R \) to be invertible and hence \( \rank\A = n \), while the reflection route is content to put a zero on the diagonal where a dependence occurs.

(c) \( \H_{\w} = \I_m - 2\w\w^{*}/\norm{\w}^2 \) (@def-householder-reflection); it is Hermitian, unitary, equal to its own inverse, and has determinant \( -1 \) (@prp-householder-properties).

(d) The target \( -\alpha\norm{\x}\e_1 \), where \( \alpha \) is the phase (over \( \nR \), the sign) of \( x_1 \) — that is, the target on the **opposite** side from \( x_1 \). The reason is arithmetic: this makes the first entry of \( \w = \x + \alpha\norm{\x}\e_1 \) a sum of like-signed quantities, with no cancellation of leading digits.

(e) False. A reflection preserving the zeros already created must fix \( \e_1, \dots, \e_k \), and then it cannot touch the entry in row \( k+1 \) of column \( k \). More decisively, such a finite procedure would compute the roots of an arbitrary polynomial by arithmetic and square roots alone, which the theorem of Abel and Ruffini quoted in the warning rules out.

(f) Because the same matrix multiplies on the right, and right multiplication by \( \Q_k \) changes column \( j \) only if \( \Q_k\e_j \neq \e_j \). Fixing \( \e_1, \dots, \e_k \) is exactly what leaves columns \( 1, \dots, k \), and the zeros in them, alone.
:::

### B. Practice

:::: {#exr-qr-and-householder-b1}
[B1: QR by Gram–Schmidt]

Find the QR factorization of
\[
\A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix}
\]
in the sense of @thm-qr-factorization, and verify that \( \R = \Q\tp\A \) for the top-left \( 2 \times 2 \) entries.
::::

::: {.solution}
*Step 1.* \( \a_1 = (1,1,1) \) has \( \norm{\a_1} = \sqrt3 \), so \( r_{11} = \sqrt3 \) and \( \q_1 = \tfrac{1}{\sqrt3}(1,1,1) \).

*Step 2.* \( r_{12} = \inner{\a_2}{\q_1} = \tfrac{2}{\sqrt3} \), so
\[
\w_2 = (1,1,0) - \tfrac23(1,1,1) = \tfrac13(1,1,-2),
\]
with \( \norm{\w_2}^2 = \tfrac19 \cdot 6 = \tfrac23 \). Hence \( r_{22} = \sqrt{2/3} \) and \( \q_2 = \tfrac{1}{\sqrt6}(1,1,-2) \).

*Step 3.* \( r_{13} = \inner{\a_3}{\q_1} = \tfrac{1}{\sqrt3} \) and \( r_{23} = \inner{\a_3}{\q_2} = \tfrac{1}{\sqrt6} \), so
\[
\w_3 = (1,0,0) - \tfrac13(1,1,1) - \tfrac16(1,1,-2) = \big(\tfrac12, -\tfrac12, 0\big),
\]
with \( \norm{\w_3} = \tfrac{1}{\sqrt2} = r_{33} \) and \( \q_3 = \tfrac{1}{\sqrt2}(1,-1,0) \). Therefore
\[
\Q = \begin{pmatrix}
\tfrac{1}{\sqrt3} & \tfrac{1}{\sqrt6} & \tfrac{1}{\sqrt2} \\[2pt]
\tfrac{1}{\sqrt3} & \tfrac{1}{\sqrt6} & -\tfrac{1}{\sqrt2} \\[2pt]
\tfrac{1}{\sqrt3} & -\tfrac{2}{\sqrt6} & 0
\end{pmatrix},
\qquad
\R = \begin{pmatrix}
\sqrt3 & \tfrac{2}{\sqrt3} & \tfrac{1}{\sqrt3} \\[2pt]
0 & \tfrac{2}{\sqrt6} & \tfrac{1}{\sqrt6} \\[2pt]
0 & 0 & \tfrac{1}{\sqrt2}
\end{pmatrix},
\]
where \( r_{22} = \sqrt{2/3} = 2/\sqrt6 \). All three diagonal entries are positive, as required.

For the verification, \( (\Q\tp\A)_{11} = \inner{\a_1}{\q_1} = 3/\sqrt3 = \sqrt3 = r_{11} \) and \( (\Q\tp\A)_{12} = \inner{\a_2}{\q_1} = 2/\sqrt3 = r_{12} \); also \( (\Q\tp\A)_{21} = \inner{\a_1}{\q_2} = (1 + 1 - 2)/\sqrt6 = 0 = r_{21} \) and \( (\Q\tp\A)_{22} = \inner{\a_2}{\q_2} = 2/\sqrt6 = r_{22} \).
:::

:::: {#exr-qr-and-householder-b2}
[B2: The same matrix by reflections]

Let \( \A = \begin{pmatrix} 1 & 1 \\ 2 & 1 \\ 2 & 3\end{pmatrix} \), the matrix of @exm-qr-3x2.

::: {.enumerate options="label=(\alph*)"}
1. Find \( \w_1 \) and the reflection \( \H_1 \) of @thm-householder-maps-vector for the first column of \( \A \), and compute \( \H_1\A \).
2. Find the second reflection and hence a factorization \( \A = \Q\R \) with \( \Q \in M_3(\nR) \) orthogonal and \( \R \in M_{3\times2}(\nR) \) upper triangular.
3. Compare the \( \R \) of (b) with the \( \R \) of @exm-qr-3x2, and say exactly how the two factorizations differ.
:::
::::

::: {.solution}
(a) The first column is \( \a = (1,2,2) \) with \( \norm{\a} = 3 \) and \( a_1 = 1 > 0 \), so \( \alpha = 1 \) and \( \w_1 = (1,2,2) + 3\e_1 = (4,2,2) \), with \( \norm{\w_1}^2 = 24 \). By \( (\ddagger) \), \( \H_1\v = \v - \tfrac{1}{12}\inner{\v}{\w_1}\w_1 \). Since \( \inner{\a}{\w_1} = 4 + 4 + 4 = 12 \) and \( \inner{(1,1,3)}{\w_1} = 4 + 2 + 6 = 12 \), each column loses one copy of \( \w_1 \):
\[
\H_1\A = \begin{pmatrix} -3 & -3 \\ 0 & -1 \\ 0 & 1 \end{pmatrix}.
\]

(b) The trailing vector is \( \y = (-1, 1) \), with \( \norm{\y} = \sqrt2 \) and \( y_1 = -1 < 0 \), so \( \alpha = -1 \) and \( \w_2 = (-1,1) - \sqrt2(1,0) = (-1-\sqrt2,\,1) \). By @thm-householder-maps-vector, the reflection sends \( \y \) to \( +\sqrt2\,\e_1 \). Embedding it as \( \H_2 = \I_1 \oplus \H_{\w_2} \), we get
\[
\R = \H_2\H_1\A = \begin{pmatrix} -3 & -3 \\ 0 & \sqrt2 \\ 0 & 0\end{pmatrix},
\qquad
\Q = \H_1\H_2 ,
\]
and \( \A = \Q\R \) because each \( \H_i \) is its own inverse (@prp-householder-properties (b)).

(c) In @exm-qr-3x2, \( \R_0 = \begin{pmatrix} 3 & 3 \\ 0 & \sqrt2\end{pmatrix} \). Deleting the zero row of \( \R \) leaves \( \R_0 \) with its **first row negated**, and correspondingly the first column of \( \Q \) is \( -\q_1 \) while the second is \( \q_2 \). The reflection route did not aim for a positive diagonal, and by the uniqueness in @thm-qr-factorization signs are the only discrepancy possible.
:::

:::: {#exr-qr-and-householder-b3}
[B3: A least-squares fit through QR]

Fit a line \( y = c_0 + c_1t \) to the data \( (t, y) = (0,1), (1,3), (2,2) \) in the least-squares sense, by finding the QR factorization of the design matrix and solving \( \R\x = \Q\tp\b \). Compute the residual and check the answer against the normal equations.
::::

::: {.solution}
The system is \( \A\x = \b \) with
\[
\A = \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 1 & 2\end{pmatrix},
\qquad
\b = \begin{pmatrix} 1 \\ 3 \\ 2 \end{pmatrix},
\qquad
\x = (c_0, c_1).
\]
Gram–Schmidt: \( \norm{\a_1} = \sqrt3 \), so \( r_{11} = \sqrt3 \) and \( \q_1 = \tfrac{1}{\sqrt3}(1,1,1) \). Then \( r_{12} = \inner{\a_2}{\q_1} = 3/\sqrt3 = \sqrt3 \) and
\[
\w_2 = (0,1,2) - (1,1,1) = (-1,0,1),
\]
so \( r_{22} = \sqrt2 \) and \( \q_2 = \tfrac{1}{\sqrt2}(-1,0,1) \). Now \( \inner{\b}{\q_1} = 6/\sqrt3 = 2\sqrt3 \) and \( \inner{\b}{\q_2} = (-1 + 0 + 2)/\sqrt2 = 1/\sqrt2 \), so \( (\dagger) \) reads
\[
\begin{pmatrix} \sqrt3 & \sqrt3 \\ 0 & \sqrt2 \end{pmatrix}\x = \begin{pmatrix} 2\sqrt3 \\ 1/\sqrt2\end{pmatrix}.
\]
Back substitution gives \( c_1 = \tfrac12 \) and then \( \sqrt3(c_0 + \tfrac12) = 2\sqrt3 \), so \( c_0 = \tfrac32 \). The fitted line is \( y = \tfrac32 + \tfrac12 t \), with residual \( \A\x - \b = (\tfrac12, -1, \tfrac12) \) and \( \norm{\A\x - \b}^2 = \tfrac32 \).

*Check.* \( \A\tp\A = \begin{pmatrix} 3 & 3 \\ 3 & 5\end{pmatrix} \) and \( \A\tp\b = (6, 7) \). Subtracting the first normal equation from the second gives \( 2c_1 = 1 \), and then \( 3c_0 + \tfrac32 = 6 \), so \( c_0 = \tfrac32 \). The residual is orthogonal to both columns of \( \A \): \( \tfrac12 - 1 + \tfrac12 = 0 \) and \( 0 \cdot \tfrac12 - 1 \cdot 1 + 2 \cdot \tfrac12 = 0 \), which is what the normal equations of @thm-least-squares say.
:::

:::: {#exr-qr-and-householder-b4}
[B4: Determine which are QR factorizations]

Determine which of the following are QR factorizations of the matrix on the left in the sense of @thm-qr-factorization. Justify your answer; for those that are not, name the clause that fails and repair it if possible.

::: {.enumerate options="label=(\alph*)"}
1. \( \begin{pmatrix} 3 & 1 \\ 4 & 7\end{pmatrix} = \tfrac15\begin{pmatrix} 3 & -4 \\ 4 & 3\end{pmatrix}\begin{pmatrix} 5 & \tfrac{31}{5} \\ 0 & \tfrac{17}{5}\end{pmatrix} \).
2. \( \begin{pmatrix} 1 & 0 \\ 1 & 1\end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 1 & 1\end{pmatrix}\begin{pmatrix} 1 & \tfrac12 \\ 0 & \tfrac12\end{pmatrix} \).
3. \( \begin{pmatrix} -1 & 0 \\ 0 & 1\end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1\end{pmatrix}\begin{pmatrix} -1 & 0 \\ 0 & 1\end{pmatrix} \).
:::
::::

::: {.solution}
(a) Yes. The product is
\[
\tfrac15\begin{pmatrix} 15 & \tfrac{93}{5} - \tfrac{68}{5} \\ 20 & \tfrac{124}{5} + \tfrac{51}{5}\end{pmatrix}
= \tfrac15\begin{pmatrix} 15 & 5 \\ 20 & 35\end{pmatrix}
= \begin{pmatrix} 3 & 1 \\ 4 & 7\end{pmatrix},
\]
the columns of the left factor are \( \tfrac15(3,4) \) and \( \tfrac15(-4,3) \), both of length \( 1 \) and orthogonal, and the diagonal entries \( 5 \) and \( \tfrac{17}{5} \) are positive. All three clauses hold, so by the uniqueness in @thm-qr-factorization this is **the** QR factorization.

(b) No. The identity is correct, and \( \R \) is upper triangular with positive diagonal, but the columns of the left factor have length \( \sqrt2 \), not \( 1 \), so clause (a) of @thm-qr-factorization fails. Repair it by dividing each column of \( \Q \) by \( \sqrt2 \) and multiplying the matching row of \( \R \) by \( \sqrt2 \):
\[
\Q = \tfrac{1}{\sqrt2}\begin{pmatrix} 1 & -1 \\ 1 & 1\end{pmatrix},
\qquad
\R = \begin{pmatrix} \sqrt2 & \tfrac{1}{\sqrt2} \\ 0 & \tfrac{1}{\sqrt2}\end{pmatrix}.
\]

(c) No. The identity is correct and the columns of \( \Q = \I_2 \) are orthonormal, but \( r_{11} = -1 < 0 \), so clause (b) fails. Repair it by moving the sign across: \( \Q = \diag(-1, 1) \), whose columns are still orthonormal, and \( \R = \I_2 \), whose diagonal is positive. This is the move described in @exr-qr-and-householder-c1 with \( \D = \diag(-1,1) \).
:::

### C. Going deeper

:::: {#exr-qr-and-householder-c1}
[C1: All the QR factorizations of a matrix]

Let \( \A \in M_{m\times n}(F) \) have independent columns, with QR factorization \( \A = \Q\R \) as in @thm-qr-factorization.

::: {.enumerate options="label=(\alph*)"}
1. Prove that an upper triangular \( \S \in M_n(F) \) with \( \S^{*}\S = \I_n \) is diagonal, with diagonal entries of modulus \( 1 \).
2. Deduce that the pairs \( (\Q_1, \R_1) \) with \( \Q_1^{*}\Q_1 = \I_n \), \( \R_1 \) upper triangular and invertible, and \( \A = \Q_1\R_1 \), are exactly the pairs \( (\Q\D^{-1}, \D\R) \) for \( \D = \diag(d_1, \dots, d_n) \) with \( \lvert d_k\rvert = 1 \).
3. Hence give a second proof of the uniqueness statement of @thm-qr-factorization.
:::
::::

::: {.solution}
(a) Let \( \s_1, \dots, \s_n \) be the columns of \( \S \); as in the proof of @thm-qr-factorization, \( \S^{*}\S = \I_n \) says \( \inner{\s_j}{\s_i} = \delta_{ij} \). We show \( \s_j = s_{jj}\e_j \) with \( \lvert s_{jj}\rvert = 1 \), by induction on \( j \). Suppose this holds for every \( i < j \). For such \( i \),
\[
0 = \inner{\s_j}{\s_i} = \conj{s_{ii}}\inner{\s_j}{\e_i} = \conj{s_{ii}}\,s_{ij},
\]
and \( s_{ii} \ne 0 \), so \( s_{ij} = 0 \). Together with upper triangularity this gives \( \s_j = s_{jj}\e_j \), and \( \norm{\s_j} = 1 \) gives \( \lvert s_{jj}\rvert = 1 \).

(b) \( (\Leftarrow) \) If \( \lvert d_k\rvert = 1 \) for all \( k \), then \( \D^{*}\D = \I_n \), so \( (\Q\D^{-1})^{*}(\Q\D^{-1}) = (\D^{-1})^{*}\Q^{*}\Q\D^{-1} = (\D\D^{*})^{-1} = \I_n \); the matrix \( \D\R \) is upper triangular and invertible; and \( (\Q\D^{-1})(\D\R) = \Q\R = \A \).

\( (\Rightarrow) \) Suppose \( \A = \Q_1\R_1 \) as stated. Exactly as in the proof of @thm-qr-factorization, \( \R_1^{*}\R_1 = \A^{*}\A = \R^{*}\R \), and \( \S = \R_1\R^{-1} \) is upper triangular with \( \S^{*}\S = \I_n \). By (a), \( \S = \D \) is diagonal with \( \lvert d_k\rvert = 1 \). Then \( \R_1 = \D\R \) and \( \Q_1 = \A\R_1^{-1} = \Q\R\R^{-1}\D^{-1} = \Q\D^{-1} \).

(c) If in addition both \( \R \) and \( \R_1 = \D\R \) have positive real diagonal entries, then \( d_k = (\R_1)_{kk}/(\R)_{kk} \) is a positive real number of modulus \( 1 \), so \( d_k = 1 \) for every \( k \). Hence \( \D = \I_n \), \( \R_1 = \R \) and \( \Q_1 = \Q \).
:::

:::: {#exr-qr-and-householder-c2}
[C2: Reflections do not mind dependence]

Let
\[
\A = \begin{pmatrix} 1 & 1 & 2 \\ 2 & 1 & 3 \\ 2 & 3 & 5 \end{pmatrix},
\]
whose third column is the sum of the first two.

::: {.enumerate options="label=(\alph*)"}
1. Run the Gram–Schmidt process of @thm-gram-schmidt on the columns of \( \A \) and say precisely which step fails.
2. Carry out the Householder reduction of @thm-qr-householder on \( \A \) and exhibit \( \R \).
3. Explain, using @thm-qr-factorization, why no factorization \( \A = \Q\R \) with \( \Q^{*}\Q = \I_3 \) and \( \R \) upper triangular with positive diagonal can exist.
:::
::::

::: {.solution}
(a) Steps \( 1 \) and \( 2 \) go through: \( \q_1 = \tfrac13(1,2,2) \) and, since \( \inner{\a_2}{\q_1} = \tfrac13(1 + 2 + 6) = 3 \), \( \w_2 = (1,1,3) - (1,2,2) = (0,-1,1) \) and \( \q_2 = \tfrac{1}{\sqrt2}(0,-1,1) \). At step \( 3 \), \( \a_3 = \a_1 + \a_2 \) lies in \( \Span(\a_1,\a_2) = \Span(\q_1,\q_2) \), so by @thm-orthonormal-coordinates (a) the vector subtracted from \( \a_3 \) is \( \a_3 \) itself and \( \w_3 = \0 \). The normalization \( \q_3 = \w_3/\norm{\w_3} \) divides by \( 0 \) and fails. This is the situation of @exr-orthonormal-bases-c2.

(b) The first column is \( (1,2,2) \), so as in @exr-qr-and-householder-b2 we take \( \w_1 = (4,2,2) \) with \( \norm{\w_1}^2 = 24 \), and \( \H_1\v = \v - \tfrac{1}{12}\inner{\v}{\w_1}\w_1 \). The inner products of the three columns with \( \w_1 \) are \( 12 \), \( 12 \) and \( 24 \), so
\[
\H_1\A = \begin{pmatrix} -3 & -3 & -6 \\ 0 & -1 & -1 \\ 0 & 1 & 1\end{pmatrix}.
\]
The trailing vector of column \( 2 \) is \( (-1,1) \), which by @exr-qr-and-householder-b2 (b) the second reflection sends to \( \sqrt2\,\e_1 \); it sends the trailing vector of column \( 3 \), which is the same vector \( (-1,1) \), to the same place. Hence
\[
\R = \begin{pmatrix} -3 & -3 & -6 \\ 0 & \sqrt2 & \sqrt2 \\ 0 & 0 & 0 \end{pmatrix},
\]
upper triangular, with a zero in position \( (3,3) \) exactly where the dependence sits. No step of the algorithm divided by zero.

(c) Such an \( \R \) would be invertible by @lem-triangular-invertible, so \( \rank\A = \rank(\Q\R) = \rank\Q = 3 \). But \( \a_3 = \a_1 + \a_2 \), so the columns are dependent and \( \rank\A \le 2 \), a contradiction. The positive-diagonal factorization exists precisely for matrices of full column rank.
:::

:::: {#exr-qr-and-householder-c3}
[C3: Triangularizing with rotations]

::: {.enumerate options="label=(\alph*)"}
1. Let \( (a, b) \in \nR^2 \) be non-zero and \( r = \sqrt{a^2+b^2} \). Verify that the Givens rotation \( \G \) of @def-givens-rotation with \( c = a/r \) and \( s = b/r \) satisfies \( \G(a,b) = (r, 0) \), and that \( \G \in \SO(2) \).
2. Use (a) to write \( \A = \begin{pmatrix} 3 & 1 \\ 4 & 2\end{pmatrix} \) as \( \Q\R \) with \( \Q \in \SO(2) \) and \( \R \) upper triangular with positive diagonal.
3. How many Givens rotations does it take to triangularize a general \( 3\times3 \) real matrix, and which entries does each one kill? Compare with the number of Householder reflections.
:::
::::

::: {.solution}
(a) \( \G(a,b) = (ca + sb,\ -sa + cb) = \big((a^2+b^2)/r,\ (-ab+ab)/r\big) = (r, 0) \). Also \( c^2 + s^2 = 1 \), so the columns of \( \G \) are orthonormal and \( \det\G = c^2 + s^2 = 1 \); hence \( \G \in \SO(2) \).

(b) The first column is \( (3,4) \), so \( r = 5 \), \( c = \tfrac35 \), \( s = \tfrac45 \) and \( \G = \tfrac15\begin{pmatrix} 3 & 4 \\ -4 & 3\end{pmatrix} \). Then
\[
\G\A = \tfrac15\begin{pmatrix} 9 + 16 & 3 + 8 \\ -12 + 12 & -4 + 6 \end{pmatrix}
= \begin{pmatrix} 5 & \tfrac{11}{5} \\ 0 & \tfrac25 \end{pmatrix} =: \R ,
\]
whose diagonal entries \( 5 \) and \( \tfrac25 \) are positive. Since \( \G^{-1} = \G\tp \in \SO(2) \), we get \( \A = \Q\R \) with \( \Q = \G\tp = \tfrac15\begin{pmatrix} 3 & -4 \\ 4 & 3\end{pmatrix} \). As a check, \( \det\A = 2 = 5 \cdot \tfrac25 = \det\R \).

(c) Three: one for \( a_{21} \) (rows \( 1, 2 \)), one for \( a_{31} \) (rows \( 1, 3 \)), and one for the new \( (3,2) \)-entry (rows \( 2, 3 \)). The last acts on rows \( 2 \) and \( 3 \), which by then have zeros in column \( 1 \), so it does not undo the earlier work. Householder needs two reflections, one per column, since each clears a whole column at once.
:::
