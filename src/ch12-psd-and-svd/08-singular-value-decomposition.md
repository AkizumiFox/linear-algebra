# The Singular Value Decomposition

Chapter 11 answered one question completely: an operator has an orthonormal basis of eigenvectors exactly when it is normal. That answer is useless for a \( 3 \times 5 \) matrix, which has no eigenvalues at all — the equation \( \A\x = \lambda\x \) is not even type-correct, because \( \A\x \) and \( \x \) live in different spaces. This section shows that every matrix, of every shape, still admits an orthonormal-to-orthogonal description, and that the numbers in it are the eigenvalues of a positive semidefinite matrix we already understand. It is the most-used factorization in applied linear algebra, and the whole of it comes from applying the spectral theorem to \( \A^{*}\A \).

Throughout, \( F \) is \( \nR \) or \( \nC \), \( \A^{*} \) is the conjugate transpose (the transpose when \( F = \nR \)), and *unitary* means unitary over \( \nC \) and orthogonal over \( \nR \), as in @def-unitary-orthogonal. Both \( F^m \) and \( F^n \) carry their standard inner products.

## Where to look when there are no eigenvalues

Let \( \A \in M_{m \times n}(F) \). There is exactly one square matrix that can be built from \( \A \) at no cost, and Chapter 10 has already used it twice: the \( n \times n \) matrix \( \A^{*}\A \) of the normal equations. It is self-adjoint, since \( (\A^{*}\A)^{*} = \A^{*}\A^{**} = \A^{*}\A \), and it is positive semidefinite for the reason that makes every argument in this chapter work:

\[
\inner{\A^{*}\A\x}{\x} = \inner{\A\x}{\A\x} = \norm{\A\x}^2 \ge 0 .
\]{#eq-svd-psd}

So \( \A^{*}\A \succeq 0 \), and @thm-psd-characterizations says its eigenvalues are non-negative real numbers, while the spectral theorem supplies an orthonormal basis of \( F^n \) consisting of its eigenvectors. Those eigenvalues are attached to \( \A \), they exist for every shape of \( \A \), and @eq-svd-psd says what they measure: how much \( \A \) stretches.

*A rectangular matrix has no eigenvalues of its own, but \( \A^{*}\A \) does, and their square roots are the stretching factors of \( \A \).*

::: {#def-singular-values}
[Singular Values]

Let \( \A \in M_{m \times n}(F) \) and put \( p = \min(m, n) \). Let
\[
\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_n \ge 0
\]
be the eigenvalues of \( \A^{*}\A \in M_n(F) \), listed **with multiplicity** in decreasing order. The **singular values** of \( \A \) are
\[
\sigma_i(\A) \coloneqq \sqrt{\lambda_i} \qquad (i = 1, \dots, p),
\]
so that \( \sigma_1(\A) \ge \sigma_2(\A) \ge \dots \ge \sigma_p(\A) \ge 0 \). We write \( \sigma_i \) when \( \A \) is clear.
:::

Clause by clause. The list has exactly \( p = \min(m, n) \) entries, not \( n \): when \( n > m \) the matrix \( \A^{*}\A \) has rank \( \rank \A \le m < n \) by @cor-rank-adjoint (b), so \( \lambda_{m+1} = \dots = \lambda_n = 0 \) and the discarded eigenvalues are all zero. The square root is the ordinary non-negative real square root, available because every \( \lambda_i \ge 0 \). The ordering is **decreasing**, matching the book's convention \( \lambda_1(\A) \ge \dots \ge \lambda_n(\A) \) for the eigenvalues of a Hermitian matrix, and it is part of the definition: "the second singular value" means a definite number. Finally, the singular values are attached to \( \A \) itself, with no choices made, because the eigenvalue list of \( \A^{*}\A \) is.

Four examples, simplest first.

1. **The identity.** \( \A = \I_n \) gives \( \A^{*}\A = \I_n \), so every \( \sigma_i = 1 \). More generally a unitary \( \U \in M_n(F) \) has \( \U^{*}\U = \I \), so all its singular values are \( 1 \). A unitary matrix stretches nothing in any direction, and the list of singular values says exactly that.
2. **A rectangular diagonal matrix.** If \( \A \in M_{m \times n}(F) \) has \( a_{ii} = d_i \) for \( i \le p \) and all other entries \( 0 \), then \( \A^{*}\A = \diag(\lvert d_1\rvert^2, \dots) \) and the singular values are \( \lvert d_1 \rvert, \dots, \lvert d_p \rvert \) **sorted downwards**. The absolute value matters: the singular values of \( \diag(1, -2) \) are \( 2, 1 \).
3. **A positive semidefinite matrix.** If \( \A \succeq 0 \) then \( \A^{*}\A = \A^2 \), whose eigenvalues are \( \lambda_i(\A)^2 \) with \( \lambda_i(\A) \ge 0 \), so \( \sigma_i(\A) = \lambda_i(\A) \). For the matrices this chapter started with, singular values and eigenvalues coincide.
4. **A single row.** For \( \A = \a^{*} \in M_{1 \times n}(F) \) with \( \a \ne \0 \), \( p = 1 \) and \( \A^{*}\A = \a\a^{*} \), whose non-zero eigenvalue is \( \norm{\a}^2 \). So \( \sigma_1 = \norm{\a} \). The degenerate case \( \A = \0 \) has every \( \sigma_i = 0 \), and it matters: it is the only matrix with \( \sigma_1 = 0 \), since \( \sigma_1 = 0 \) forces \( \A^{*}\A = \0 \) and then \( \norm{\A\x}^2 = 0 \) for every \( \x \) by @eq-svd-psd.

Now the non-example, by minimal change. Replace "square roots of the eigenvalues of \( \A^{*}\A \)" by "absolute values of the eigenvalues of \( \A \)". For \( \A \succeq 0 \), and more generally for any normal \( \A \), the two agree (@exr-singular-value-decomposition-c3). But the second recipe is undefined for a non-square matrix, and for
\[
\N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}
\]
it returns \( 0, 0 \), while \( \N^{*}\N = \diag(0, 1) \) gives the singular values \( 1, 0 \). The clause that fails is the one that does all the work: \( \A^{*}\A \) is positive semidefinite for **every** \( \A \), whereas \( \A \) itself may have no useful spectrum.

::: {.warning}
**Singular values are not eigenvalues.** The matrix \( \N \) above has both eigenvalues equal to \( 0 \) and largest singular value \( 1 \): it annihilates \( \e_1 \) but sends \( \e_2 \) to a unit vector, so calling it "small" because its spectrum is \( \{0\} \) is wrong. Singular values are always real and non-negative; eigenvalues need not be either. The two lists agree, after taking absolute values, exactly for normal matrices — this is @exr-singular-value-decomposition-c3, and Chapter 11's Schur inequality is what makes the converse true.
:::

::: {.check}
What are the singular values of an orthogonal projection \( \P \in M_n(F) \) onto an \( r \)-dimensional subspace?
:::

::: {.solution}
\( \P^{*}\P = \P^2 = \P \), because an orthogonal projection is self-adjoint and idempotent. So the eigenvalues of \( \P^{*}\P \) are those of \( \P \), namely \( 1 \) with multiplicity \( r \) and \( 0 \) with multiplicity \( n - r \). Sorted downwards, the singular values are \( \sigma_1 = \dots = \sigma_r = 1 \) and \( \sigma_{r+1} = \dots = \sigma_n = 0 \). This is also Example 3 above, since \( \P \succeq 0 \).
:::

## The theorem

Here is the payoff. The eigenvectors of \( \A^{*}\A \) are an orthonormal basis of the domain; the claim is that \( \A \) carries them to an **orthogonal** list in the codomain, whose lengths are the singular values.

::: {#thm-svd}
[Singular Value Decomposition]

Let \( \A \in M_{m \times n}(F) \), let \( p = \min(m, n) \) and let \( \sigma_1 \ge \dots \ge \sigma_p \ge 0 \) be its singular values. Then there are unitary matrices \( \U \in M_m(F) \) and \( \V \in M_n(F) \) such that
\[
\A = \U\vSigma\V^{*} ,
\]
where \( \vSigma \in M_{m \times n}(\nR) \) has \( (\vSigma)_{ii} = \sigma_i \) for \( i = 1, \dots, p \) and every other entry \( 0 \). Moreover the number of non-zero \( \sigma_i \) equals \( \rank \A \).
:::

::: {.idea}
Picture the \( 2 \times 2 \) real case. A matrix carries the unit circle to an ellipse, and an ellipse has two perpendicular axes; the theorem says that the two unit vectors sent to the ends of those axes are themselves perpendicular. That is exactly what Chapter 11's principal axis theorem said about the level curves of a quadratic form, and the link is that \( \norm{\A\x}^2 = \x^{*}(\A^{*}\A)\x \) **is** a quadratic form, with matrix \( \A^{*}\A \). So the plan is: ① diagonalize \( \A^{*}\A \) by the spectral theorem, getting an orthonormal basis \( \v_1, \dots, \v_n \) with \( \A^{*}\A\v_i = \sigma_i^2\v_i \); ② compute \( \inner{\A\v_i}{\A\v_j} \) and watch the eigenvalue equation force it to be \( \sigma_i^2\delta_{ij} \), so the images are already orthogonal; ③ normalize the non-zero ones to unit vectors \( \u_i \), and, if there are fewer than \( m \) of them, pad the list out to an orthonormal basis of \( F^m \); ④ read \( \A\V = \U\vSigma \) off column by column.
:::

::: {.proof}
**Step 1: diagonalize \( \A^{*}\A \).** The matrix \( \A^{*}\A \in M_n(F) \) is self-adjoint, and @eq-svd-psd makes it positive semidefinite in the sense of @def-positive-semidefinite. By the spectral theorem in matrix form — @cor-spectral-real-matrix when \( F = \nR \), @cor-spectral-complex-matrix when \( F = \nC \), each of which allows the eigenvalues to be listed in a prescribed order — there is a unitary \( \V \in M_n(F) \) with columns \( \v_1, \dots, \v_n \) such that
\[
\A^{*}\A\,\v_i = \lambda_i\v_i, \qquad \lambda_1 \ge \dots \ge \lambda_n \ge 0 ,
\]
the eigenvalues being non-negative by @thm-psd-characterizations. Set \( \sigma_i = \sqrt{\lambda_i} \) for all \( i \le n \); for \( i \le p \) these are the singular values of @def-singular-values.

**Step 2: the images are orthogonal.** For all \( i, j \), using \( \inner{\x}{\y} = \y^{*}\x \) and the eigenvalue equation,
\[
\inner{\A\v_i}{\A\v_j} = \inner{\A^{*}\A\v_i}{\v_j} = \lambda_i\inner{\v_i}{\v_j} = \lambda_i\delta_{ij} ,
\]
the first equality by @def-adjoint and the last because \( \V \) is unitary, so its columns are orthonormal (@thm-isometry-characterizations (f)). In particular \( \norm{\A\v_i}^2 = \lambda_i = \sigma_i^2 \), so

\[
\A\v_i = \0 \iff \sigma_i = 0 .
\]{#eq-svd-kernel-test}

**Step 3: normalize, and count.** Let \( r \) be the number of indices with \( \sigma_i > 0 \); since the \( \sigma_i \) decrease, these are \( i = 1, \dots, r \). For \( i \le r \) put
\[
\u_i \coloneqq \frac{1}{\sigma_i}\A\v_i ,
\]
which is legitimate because \( \sigma_i \neq 0 \). By Step 2, \( \inner{\u_i}{\u_j} = \lambda_i\delta_{ij}/(\sigma_i\sigma_j) = \delta_{ij} \) for \( i, j \le r \), so \( (\u_1, \dots, \u_r) \) is an orthonormal list in \( F^m \).

We claim \( r = \rank \A \). Any \( \x \in F^n \) is \( \x = \sum_i c_i\v_i \) since \( (\v_1, \dots, \v_n) \) is a basis, and then \( \A\x = \sum_{i \le r} c_i\sigma_i\u_i \) by @eq-svd-kernel-test. Hence \( \im \A = \Span(\u_1, \dots, \u_r) \), and the \( \u_i \) are orthonormal, hence independent (@thm-orthogonal-independent), so \( \rank \A = r \). In particular \( r \le \min(m, n) = p \), so every index \( i \) with \( \sigma_i > 0 \) satisfies \( i \le p \), and the non-zero singular values are exactly \( \sigma_1, \dots, \sigma_r \).

**Step 4: pad the list.** If \( r = m \) the list \( (\u_1, \dots, \u_r) \) is already an orthonormal basis of \( F^m \), and we set \( \U = (\u_1 \mid \dots \mid \u_m) \). If \( r < m \), apply @cor-extend-orthonormal-basis to the orthonormal list \( (\u_1, \dots, \u_r) \) in \( F^m \): there are \( \u_{r+1}, \dots, \u_m \) making \( (\u_1, \dots, \u_m) \) an orthonormal basis of \( F^m \). Either way let \( \U \in M_m(F) \) have these columns; it is unitary because its columns are orthonormal (@thm-isometry-characterizations (f)). Note that the padding vectors are **not** determined by \( \A \), and nothing below uses any property of them beyond orthonormality.

**Step 5: read off the columns.** Let \( \vSigma \in M_{m \times n}(\nR) \) be as in the statement. Column \( i \) of \( \U\vSigma \) is \( \U \) times column \( i \) of \( \vSigma \), which is \( \sigma_i\e_i \) for \( i \le p \) and \( \0 \) for \( i > p \); so column \( i \) of \( \U\vSigma \) is \( \sigma_i\u_i \) for \( i \le p \) and \( \0 \) for \( i > p \). Column \( i \) of \( \A\V \) is \( \A\v_i \). Compare:

- for \( i \le r \), \( \A\v_i = \sigma_i\u_i \) by the definition of \( \u_i \);
- for \( r < i \le p \), \( \sigma_i = 0 \), so both columns are \( \0 \) by @eq-svd-kernel-test;
- for \( i > p \) (possible only when \( n > m \)), we have \( i > p \ge r \), so \( \sigma_i = 0 \) and \( \A\v_i = \0 \), and both columns are \( \0 \).

Hence \( \A\V = \U\vSigma \). Since \( \V \) is unitary, \( \V^{-1} = \V^{*} \), so \( \A = \U\vSigma\V^{*} \). This proves the theorem.
:::

A factorization \( \A = \U\vSigma\V^{*} \) as in the theorem is called **a singular value decomposition** of \( \A \), the columns \( \u_i \) of \( \U \) are **left singular vectors** and the columns \( \v_i \) of \( \V \) are **right singular vectors**. The two equations to keep in mind are the ones the proof produced,
\[
\A\v_i = \sigma_i\u_i, \qquad \A^{*}\u_i = \sigma_i\v_i \qquad (i \le r),
\]{#eq-singular-vector-pairing}
the second obtained by applying \( \A^{*} \) to the first and using \( \A^{*}\A\v_i = \sigma_i^2\v_i \). In words: \( \A \) matches up two orthonormal bases, one in each space, stretching the \( i \)-th direction by \( \sigma_i \), and \( \A^{*} \) runs the same correspondence backwards with the same factors.

Here is the picture the Idea described, in the real \( 2 \times 2 \) case.

\begin{center}
\begin{tikzpicture}[scale=1.35, lab/.style={font=\small}]
    \begin{scope}[shift={(-2.3,0)}]
        \draw[->, gray] (-1.35,0) -- (1.35,0);
        \draw[->, gray] (0,-1.35) -- (0,1.35);
        \draw[very thick] (0,0) circle (1);
        \draw[->, very thick] (0,0) -- (0.866,0.5);
        \draw[->, very thick] (0,0) -- (-0.5,0.866);
        \node[lab] at (1.09,0.68) {$\v_1$};
        \node[lab] at (-0.64,1.09) {$\v_2$};
        \node[lab] at (0,-1.62) {the unit circle};
    \end{scope}
    \draw[->, thick] (-0.62,0) -- (0.62,0) node[midway, above, lab] {$\A$};
    \begin{scope}[shift={(2.9,0)}]
        \draw[->, gray] (-1.95,0) -- (1.95,0);
        \draw[->, gray] (0,-1.35) -- (0,1.35);
        \draw[very thick, rotate=20] (0,0) ellipse (1.7 and 0.6);
        \draw[->, very thick] (0,0) -- (1.597,0.581);
        \draw[->, very thick] (0,0) -- (-0.205,0.564);
        \node[lab] at (0.62,0.62) {$\sigma_1\u_1$};
        \node[lab] at (-0.98,0.84) {$\sigma_2\u_2$};
        \node[lab] at (0,-1.62) {its image, an ellipse};
    \end{scope}
    \node[lab, align=center] at (0.3,-2.25)
      {$\A$ carries a pair of perpendicular unit vectors to the\\ semi-axes of an ellipse; their lengths are $\sigma_1$ and $\sigma_2$};
\end{tikzpicture}
\end{center}

Compare the principal axes figure of Chapter 11 §05. There the ellipse was a level curve \( \x\tp\A\x = 1 \) of a quadratic form and the axes lay along the eigenvectors of a symmetric \( \A \); here the ellipse is the *image* of the unit circle under an arbitrary \( \A \). The two pictures are the same picture, because \( \norm{\A\x}^2 = \x^{*}(\A^{*}\A)\x \) is a quadratic form with matrix \( \A^{*}\A \), and the right singular vectors of \( \A \) are its principal axes. A large \( \sigma_i \) now means a **long** semi-axis, whereas in @thm-principal-axes a large \( \lambda_i \) meant a short one; the reason is that the two pictures are related by taking reciprocals of square roots.

## What is unique and what is not

The singular values were defined before the theorem, so they cannot depend on any choice. What needs saying is the converse: any factorization of the stated shape recovers them.

::: {#thm-singular-values-unique}
[The Singular Values Are Determined]

Let \( \A \in M_{m \times n}(F) \) and suppose \( \A = \U\vSigma\V^{*} \) with \( \U, \V \) unitary and \( \vSigma \in M_{m \times n}(\nR) \) of the shape in @thm-svd, with diagonal entries \( s_1 \ge \dots \ge s_p \ge 0 \). Then \( s_i = \sigma_i(\A) \) for every \( i \). Moreover:

::: {.enumerate options="label=(\alph*)"}
1. the columns of \( \V \) are forced to be an orthonormal basis of \( F^n \) consisting of eigenvectors of \( \A^{*}\A \), with \( \A^{*}\A\v_i = \sigma_i^2\v_i \) for every \( i \le n \), where \( \sigma_i \coloneqq 0 \) for \( p < i \le n \); and any such basis occurs;
2. once \( \V \) is chosen, \( \u_i = \A\v_i/\sigma_i \) is forced for every \( i \le r = \rank\A \), while \( \u_{r+1}, \dots, \u_m \) may be any orthonormal basis of \( (\im\A)^{\perp} \).
:::
:::

::: {.proof}
From \( \A = \U\vSigma\V^{*} \) and \( \U^{*}\U = \I_m \),
\[
\A^{*}\A = \V\vSigma^{*}\U^{*}\U\vSigma\V^{*} = \V(\vSigma^{*}\vSigma)\V^{*} ,
\]
and \( \vSigma^{*}\vSigma \in M_n(\nR) \) is the diagonal matrix with entries \( s_1^2, \dots, s_p^2 \) followed by zeros. So \( \A^{*}\A \) is unitarily diagonalized with this diagonal, and its eigenvalue list in decreasing order is therefore \( s_1^2 \ge \dots \ge s_p^2 \ge 0 \ge \dots \) — already sorted, since the \( s_i \) are. Comparing with @def-singular-values gives \( s_i^2 = \sigma_i(\A)^2 \), hence \( s_i = \sigma_i(\A) \) because both are non-negative.

(a) The displayed equation says the \( i \)-th column of \( \V \) satisfies \( \A^{*}\A\v_i = \sigma_i^2\v_i \), and the columns of a unitary matrix are orthonormal. Conversely, given any orthonormal basis of eigenvectors of \( \A^{*}\A \) ordered by decreasing eigenvalue, Steps 2–5 of the proof of @thm-svd build a factorization from it.

(b) For \( i \le r \) we have \( \sigma_i \neq 0 \), and comparing column \( i \) of \( \A\V = \U\vSigma \) gives \( \A\v_i = \sigma_i\u_i \), so \( \u_i = \A\v_i/\sigma_i \). For \( i > r \) the corresponding column of \( \vSigma \) is zero, so \( \u_i \) is unconstrained by the equation \( \A\V = \U\vSigma \); the only constraint left is that \( (\u_1, \dots, \u_m) \) be orthonormal, which says exactly that \( (\u_{r+1}, \dots, \u_m) \) is an orthonormal basis of \( \Span(\u_1, \dots, \u_r)^{\perp} = (\im\A)^{\perp} \).
:::

So \( \vSigma \) is unique and \( \U, \V \) are not. The freedom is of two kinds, and both are visible in small cases. If \( \A^{*}\A \) has a repeated eigenvalue, any orthonormal basis of that eigenspace may be used: \( \A = \I_2 \) has \( \vSigma = \I_2 \) and \( \I_2 = \U\I_2\U^{*} \) for **every** unitary \( \U \), with \( \V = \U \). If the eigenvalues are distinct, each \( \v_i \) is still free up to a scalar of modulus \( 1 \), and replacing \( \v_i \) by \( c\v_i \) replaces \( \u_i \) by \( c\u_i \), leaving \( \sigma_i\u_i\v_i^{*} \) unchanged because \( c\conj{c} = 1 \).

::: {.remark}
That last observation is why the factorization is worth having even though it is not unique: the *products* \( \sigma_i\u_i\v_i^{*} \) are what later sections use, and those are unchanged by the phase freedom. Section 11 will define the pseudoinverse through a singular value decomposition and will have to check exactly this.
:::

## The compact form, and the four subspaces

Steps 3 and 5 of the proof produced more than the statement recorded: they located \( \im\A \) and \( \ker\A \) inside the two bases. Writing the factorization so that only the non-zero singular values appear makes this visible.

::: {#thm-compact-svd}
[Compact Singular Value Decomposition]

Let \( \A \in M_{m \times n}(F) \) have rank \( r \) and let \( \A = \U\vSigma\V^{*} \) be as in @thm-svd, with columns \( \u_1, \dots, \u_m \) and \( \v_1, \dots, \v_n \). Then
\[
\A = \sum_{i=1}^{r} \sigma_i\,\u_i\v_i^{*} ,
\]
a sum of \( r \) matrices of rank \( 1 \). Equivalently \( \A = \U_r\vSigma_r\V_r^{*} \), where \( \U_r \in M_{m \times r}(F) \) and \( \V_r \in M_{n \times r}(F) \) hold the first \( r \) columns of \( \U \) and \( \V \), and \( \vSigma_r = \diag(\sigma_1, \dots, \sigma_r) \) is square and **invertible**.
:::

::: {.proof}
Write \( \A = (\U\vSigma)\V^{*} \). The columns of \( \U\vSigma \) are \( \sigma_1\u_1, \dots, \sigma_p\u_p \) followed by zero columns, as computed in Step 5 of @thm-svd, and the rows of \( \V^{*} \) are \( \v_1^{*}, \dots, \v_n^{*} \). By the outer product expansion of a matrix product (@cor-outer-product-expansion),
\[
\A = \sum_{i=1}^{p} (\sigma_i\u_i)\v_i^{*} = \sum_{i=1}^{r} \sigma_i\,\u_i\v_i^{*} ,
\]
the terms with \( i > r \) vanishing because \( \sigma_i = 0 \) there. Each \( \u_i\v_i^{*} \) is non-zero with all columns multiples of \( \u_i \), hence of rank \( 1 \). The same computation with the truncated matrices gives \( \U_r\vSigma_r\V_r^{*} = \sum_{i \le r}\sigma_i\u_i\v_i^{*} \), and \( \vSigma_r \) is invertible because its diagonal entries \( \sigma_1, \dots, \sigma_r \) are non-zero.
:::

::: {#cor-svd-four-subspaces}
[The Four Fundamental Subspaces from the Compact Form]

With the notation of @thm-compact-svd:

::: {.enumerate options="label=(\alph*)"}
1. \( (\u_1, \dots, \u_r) \) is an orthonormal basis of \( \im\A = \col(\A) \);
2. \( (\u_{r+1}, \dots, \u_m) \) is an orthonormal basis of \( \ker\A^{*} \);
3. \( (\v_1, \dots, \v_r) \) is an orthonormal basis of \( \im\A^{*} \);
4. \( (\v_{r+1}, \dots, \v_n) \) is an orthonormal basis of \( \ker\A \).
:::
:::

::: {.idea}
Two of the four were proved on the way to @thm-svd. The other two come for free by applying the same statements to \( \A^{*} \), whose singular value decomposition is \( \A^{*} = \V\vSigma^{*}\U^{*} \) — the roles of \( \u \) and \( \v \) simply swap.
:::

::: {.proof}
*Part (a).* Step 3 of @thm-svd showed \( \im\A = \Span(\u_1, \dots, \u_r) \), and these \( r \) vectors are orthonormal.

*Part (d).* By @eq-svd-kernel-test, \( \A\v_i = \0 \) exactly for \( i > r \), and for \( \x = \sum_i c_i\v_i \) we computed \( \A\x = \sum_{i \le r} c_i\sigma_i\u_i \). Since the \( \u_i \) are independent and the \( \sigma_i \) non-zero for \( i \le r \), \( \A\x = \0 \) if and only if \( c_1 = \dots = c_r = 0 \), that is, \( \x \in \Span(\v_{r+1}, \dots, \v_n) \).

*Parts (b) and (c).* Taking conjugate transposes, \( \A^{*} = \V\vSigma^{*}\U^{*} \), and \( \vSigma^{*} \in M_{n \times m}(\nR) \) has the same diagonal \( \sigma_1, \dots, \sigma_p \). So this is a singular value decomposition of \( \A^{*} \), with the columns of \( \V \) as left singular vectors and those of \( \U \) as right singular vectors, and \( \rank\A^{*} = \rank\A = r \) by @cor-rank-adjoint (a). Now the two parts just proved, applied to \( \A^{*} \) instead of \( \A \), give exactly (c) and (b).
:::

This is the cleanest possible form of @thm-four-subspaces-orthogonal. That theorem said the four subspaces come in two orthogonal pairs, \( F^n = \ker\A \oplus \im\A^{*} \) and \( F^m = \im\A \oplus \ker\A^{*} \). The corollary hands over **orthonormal bases of all four at once**, out of two matrices, and adds the missing piece of information: how \( \A \) maps one pair to the other. Restricted to \( \im\A^{*} \), the map \( \A \) is a bijection onto \( \im\A \), and in the bases \( (\v_1, \dots, \v_r) \) and \( (\u_1, \dots, \u_r) \) its matrix is the diagonal \( \vSigma_r \). Every matrix, after an orthonormal change of basis on each side, is a positive diagonal matrix padded with zeros.

::: {.check}
Let \( \A \in M_{m \times n}(F) \) have rank \( r \). Using @cor-svd-four-subspaces, what is \( \dim\ker\A^{*} \), and why does the answer not depend on which singular value decomposition was used?
:::

::: {.solution}
The list \( (\u_{r+1}, \dots, \u_m) \) has \( m - r \) members, so \( \dim\ker\A^{*} = m - r \). It cannot depend on the factorization because \( r = \rank\A \) is determined by \( \A \) (@thm-singular-values-unique), and in any case the answer agrees with \( \dim(\im\A)^{\perp} = m - \rank\A \) from @thm-four-subspaces-orthogonal and @thm-orthogonal-decomposition.
:::

## Two computations and one comparison

**The Frobenius norm.** From \( \norm{\A}_F^2 = \tr(\A^{*}\A) \) and \( \A^{*}\A = \V(\vSigma^{*}\vSigma)\V^{*} \), or directly from @lem-frobenius-unitarily-invariant,
\[
\norm{\A}_F^2 = \norm{\U\vSigma\V^{*}}_F^2 = \norm{\vSigma}_F^2 = \sum_{i=1}^{p} \sigma_i^2 .
\]
So the Frobenius norm is the Euclidean length of the singular value list. Section 10 turns this one identity into the best low-rank approximation theorem.

**The largest stretch.** Let \( \x = \sum_i c_i\v_i \) be a unit vector, so \( \sum_i \lvert c_i\rvert^2 = 1 \) by @thm-parseval-identity. Then \( \A\x = \sum_{i \le r} c_i\sigma_i\u_i \), and since the \( \u_i \) are orthonormal, Pythagoras (@thm-pythagoras) gives
\[
\norm{\A\x}^2 = \sum_{i \le r} \sigma_i^2\lvert c_i\rvert^2 \le \sigma_1^2\sum_i \lvert c_i\rvert^2 = \sigma_1^2 ,
\]
with equality at \( \x = \v_1 \). So \( \sigma_1 = \max\{\norm{\A\x} : \norm{\x} = 1\} \): the largest singular value is the largest factor by which \( \A \) can lengthen a vector. Chapter 15 gives that quantity a name, the operator norm \( \norm{\A}_2 \), and this computation is why \( \norm{\A}_2 = \sigma_1 \).

**Against the eigenvalues.** For a normal \( \A \in M_n(\nC) \), write \( \A = \U\D\U^{*} \) with \( \D = \diag(\lambda_1, \dots, \lambda_n) \) by @cor-spectral-complex-matrix. Then
\[
\A^{*}\A = \U\D^{*}\D\U^{*} = \U\diag\bigl(\lvert\lambda_1\rvert^2, \dots, \lvert\lambda_n\rvert^2\bigr)\U^{*} ,
\]
so the singular values of \( \A \) are the moduli \( \lvert\lambda_i\rvert \), sorted downwards. For a general matrix there is no relation at all in one direction — \( \N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) has spectrum \( \{0\} \) and \( \sigma_1 = 1 \) — and only the crude bound \( \lvert\lambda\rvert \le \sigma_1 \) in the other, since \( \A\x = \lambda\x \) with \( \norm{\x} = 1 \) gives \( \lvert\lambda\rvert = \norm{\A\x} \le \sigma_1 \).

::: {#exm-svd-2x3}
[A singular value decomposition of a 2 by 3 matrix]

Find a singular value decomposition of
\[
\A = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & -1 \end{pmatrix} \in M_{2 \times 3}(\nR),
\]
and read off orthonormal bases of its four fundamental subspaces.
:::

::: {.solution}
Here \( m = 2 \), \( n = 3 \), \( p = 2 \). The proof asks for the eigenvectors of the \( 3 \times 3 \) matrix \( \A\tp\A \), but there is a shortcut worth taking whenever \( m < n \): run the proof on \( \A\tp \) instead. It produces \( \A\tp = \V\vSigma\tp\U\tp \), and transposing that equation gives \( \A = \U\vSigma\V\tp \), which is what we want. The eigenvalue computation then lives in the smaller matrix
\[
\A\A\tp = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}.
\]

*Step 1.* The characteristic polynomial of \( \A\A\tp \) is \( x^2 - 4x + 3 = (x-1)(x-3) \), so the eigenvalues are \( 3 \) and \( 1 \) and the singular values are \( \sigma_1 = \sqrt3 \), \( \sigma_2 = 1 \). For \( \lambda = 3 \), \( \A\A\tp - 3\I = \begin{pmatrix} -1 & -1 \\ -1 & -1\end{pmatrix} \) gives \( x_1 = -x_2 \), and for \( \lambda = 1 \) we get \( x_1 = x_2 \). Normalizing,
\[
\u_1 = \tfrac{1}{\sqrt2}(1,-1),
\qquad
\u_2 = \tfrac{1}{\sqrt2}(1,1).
\]
Both singular values are non-zero, so \( r = \rank\A = 2 \).

*Steps 2–4.* The roles of \( \u \) and \( \v \) are swapped along with the roles of \( \A \) and \( \A\tp \), so here \( \v_i = \A\tp\u_i/\sigma_i \):
\[
\v_1 = \tfrac{\A\tp(1,-1)}{\sqrt2\,\sqrt3} = \tfrac{1}{\sqrt6}(1,-1,2),
\qquad
\v_2 = \tfrac{\A\tp(1,1)}{\sqrt2} = \tfrac{1}{\sqrt2}(1,1,0).
\]
This time the padding step is needed, since \( r = 2 < 3 \): a unit vector orthogonal to both is
\[
\v_3 = \tfrac{1}{\sqrt3}(-1,1,1).
\]

*Step 5.* Assembling,
\[
\U = \tfrac{1}{\sqrt2}\begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix},
\qquad
\vSigma = \begin{pmatrix} \sqrt3 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix},
\]
\[
\V = \begin{pmatrix}
\tfrac{1}{\sqrt6} & \tfrac{1}{\sqrt2} & -\tfrac{1}{\sqrt3} \\[3pt]
-\tfrac{1}{\sqrt6} & \tfrac{1}{\sqrt2} & \tfrac{1}{\sqrt3} \\[3pt]
\tfrac{2}{\sqrt6} & 0 & \tfrac{1}{\sqrt3}
\end{pmatrix},
\qquad
\A = \U\vSigma\V\tp .
\]
As a check, \( \norm{\A}_F^2 = 1 + 0 + 1 + 0 + 1 + 1 = 4 \) and \( \sigma_1^2 + \sigma_2^2 = 3 + 1 = 4 \).

*The four subspaces* (@cor-svd-four-subspaces), with \( r = 2 \): \( \col(\A) \) has the orthonormal basis \( \u_1, \u_2 \), which is all of \( \nR^2 \), so \( \nul(\A\tp) = \{\0\} \); \( \row(\A) = \col(\A\tp) \) has the orthonormal basis \( \v_1, \v_2 \); and \( \nul(\A) = \Span(\v_3) \) is the line through \( (-1,1,1) \). The last is easy to verify directly: \( \A(-1,1,1) = (-1+1, 1-1) = \0 \).
:::

## Exercises

### A. Check your understanding

::: {#exr-singular-value-decomposition-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the singular values of a matrix \( \A \in M_{m \times n}(F) \). How many are there?
2. State the singular value decomposition, with the size and the defining property of each factor.
3. True or false: the singular values of \( \A \) are the absolute values of its eigenvalues. Justify your answer.
4. How many non-zero singular values does \( \A \) have, and why?
5. Given a compact singular value decomposition \( \A = \sum_{i \le r}\sigma_i\u_i\v_i^{*} \), write down orthonormal bases of all four fundamental subspaces of \( \A \).
6. True or false: in \( \A = \U\vSigma\V^{*} \) the three factors are determined by \( \A \). Justify your answer.
:::
:::

::: {.solution}
(a) They are \( \sigma_i = \sqrt{\lambda_i} \) for \( i = 1, \dots, \min(m,n) \), where \( \lambda_1 \ge \dots \ge \lambda_n \ge 0 \) are the eigenvalues of \( \A^{*}\A \) with multiplicity (@def-singular-values). There are \( \min(m, n) \) of them.

(b) @thm-svd: \( \A = \U\vSigma\V^{*} \) with \( \U \in M_m(F) \) unitary, \( \V \in M_n(F) \) unitary and \( \vSigma \in M_{m \times n}(\nR) \) having \( \sigma_1 \ge \dots \ge \sigma_p \ge 0 \) in positions \( (i,i) \) and zeros elsewhere.

(c) False. \( \N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) has both eigenvalues \( 0 \) and singular values \( 1, 0 \). The statement is true for normal matrices (@exr-singular-value-decomposition-c3), and for a non-square matrix it does not even make sense.

(d) Exactly \( \rank\A \), by @thm-svd. The reason is that \( \A\v_i = \0 \) precisely when \( \sigma_i = 0 \), so the \( \v_i \) with \( \sigma_i = 0 \) span \( \ker\A \).

(e) \( (\u_1, \dots, \u_r) \) for \( \im\A \); \( (\u_{r+1}, \dots, \u_m) \) for \( \ker\A^{*} \); \( (\v_1, \dots, \v_r) \) for \( \im\A^{*} \); \( (\v_{r+1}, \dots, \v_n) \) for \( \ker\A \) (@cor-svd-four-subspaces).

(f) False for \( \U \) and \( \V \), true for \( \vSigma \) (@thm-singular-values-unique). For instance \( \I_2 = \U\I_2\U^{*} \) for every unitary \( \U \). The freedom is: any orthonormal eigenbasis of \( \A^{*}\A \) may be used for \( \V \), and the last \( m - r \) columns of \( \U \) may be any orthonormal basis of \( (\im\A)^{\perp} \).
:::

### B. Practice

::: {#exr-singular-value-decomposition-b1}
[B1: A 2 by 2 decomposition]

Find a singular value decomposition \( \A = \U\vSigma\V\tp \) of
\[
\A = \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix} \in M_2(\nR),
\]
and compare the singular values with the eigenvalues of \( \A \).
:::

::: {.solution}
\( \A\tp\A = \begin{pmatrix} 25 & 20 \\ 20 & 25 \end{pmatrix} \), with characteristic polynomial \( x^2 - 50x + (625 - 400) = x^2 - 50x + 225 \), whose roots are \( 45 \) and \( 5 \). So \( \sigma_1 = 3\sqrt5 \) and \( \sigma_2 = \sqrt5 \).

For \( \lambda = 45 \) the equation \( -20x_1 + 20x_2 = 0 \) gives \( \v_1 = \tfrac1{\sqrt2}(1,1) \); for \( \lambda = 5 \), \( \v_2 = \tfrac1{\sqrt2}(1,-1) \). Then
\[
\u_1 = \frac{\A\v_1}{3\sqrt5} = \frac{(3,9)}{3\sqrt{10}} = \tfrac{1}{\sqrt{10}}(1,3),
\qquad
\u_2 = \frac{\A\v_2}{\sqrt5} = \frac{(3,-1)}{\sqrt{10}} .
\]
Hence
\[
\U = \tfrac{1}{\sqrt{10}}\begin{pmatrix} 1 & 3 \\ 3 & -1 \end{pmatrix},
\quad
\vSigma = \begin{pmatrix} 3\sqrt5 & 0 \\ 0 & \sqrt5 \end{pmatrix},
\quad
\V = \tfrac{1}{\sqrt2}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix},
\]
and \( \U\vSigma\V\tp = \A \). Check: \( \sigma_1^2 + \sigma_2^2 = 45 + 5 = 50 = 9 + 16 + 25 = \norm{\A}_F^2 \).

The eigenvalues of \( \A \) are \( 3 \) and \( 5 \), the diagonal entries of a triangular matrix. They are not the singular values, not even after reordering: \( \A \) is not normal, since \( \A\tp\A \neq \A\A\tp = \begin{pmatrix} 9 & 12 \\ 12 & 41 \end{pmatrix} \). Note, however, that \( \sigma_1\sigma_2 = 15 = \lvert\det\A\rvert \), as @exr-singular-value-decomposition-c2 explains.
:::

::: {#exr-singular-value-decomposition-b2}
[B2: When the left singular vectors must be padded]

Find a singular value decomposition of
\[
\A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 0 \end{pmatrix} \in M_{3 \times 2}(\nR),
\]
saying explicitly where the padding step of @thm-svd is used.
:::

::: {.solution}
\( \A\tp\A = \diag(2, 1) \), already diagonal with decreasing diagonal, so \( \V = \I_2 \), \( \v_1 = \e_1 \), \( \v_2 = \e_2 \), and \( \sigma_1 = \sqrt2 \), \( \sigma_2 = 1 \). Both are non-zero, so \( r = 2 \). Then
\[
\u_1 = \tfrac{1}{\sqrt2}\A\e_1 = \tfrac{1}{\sqrt2}(1,0,1),
\qquad
\u_2 = \A\e_2 = (0,1,0).
\]
Here \( r = 2 < 3 = m \), so Step 4 of @thm-svd applies: extend \( (\u_1, \u_2) \) to an orthonormal basis of \( \nR^3 \). A vector orthogonal to both is \( (1,0,-1) \), so take \( \u_3 = \tfrac1{\sqrt2}(1,0,-1) \). Then
\[
\U = \begin{pmatrix}
\tfrac{1}{\sqrt2} & 0 & \tfrac{1}{\sqrt2} \\[3pt]
0 & 1 & 0 \\[3pt]
\tfrac{1}{\sqrt2} & 0 & -\tfrac{1}{\sqrt2}
\end{pmatrix},
\qquad
\vSigma = \begin{pmatrix} \sqrt2 & 0 \\ 0 & 1 \\ 0 & 0 \end{pmatrix},
\qquad
\V = \I_2 ,
\]
and \( \U\vSigma\V\tp = \U\vSigma = \A \). The vector \( \u_3 \) is not determined by \( \A \) beyond its line: \( -\u_3 \) would do just as well. By @cor-svd-four-subspaces, \( \nul(\A\tp) = \Span(\u_3) \), which is confirmed by \( \A\tp(1,0,-1) = (1 - 1, 0) = \0 \).
:::

::: {#exr-singular-value-decomposition-b3}
[B3: Compact form and the four subspaces]

For
\[
\A = \begin{pmatrix} 2 & 2 \\ 1 & 1 \\ 2 & 2 \end{pmatrix} \in M_{3 \times 2}(\nR),
\]
find the compact singular value decomposition \( \A = \sum_{i \le r}\sigma_i\u_i\v_i\tp \), and hence orthonormal bases of all four fundamental subspaces.
:::

::: {.solution}
\( \A\tp\A = \begin{pmatrix} 9 & 9 \\ 9 & 9 \end{pmatrix} \), with eigenvalues \( 18 \) and \( 0 \), so \( \sigma_1 = 3\sqrt2 \), \( \sigma_2 = 0 \) and \( r = 1 \). An eigenvector for \( 18 \) is \( \v_1 = \tfrac1{\sqrt2}(1,1) \), and for \( 0 \) it is \( \v_2 = \tfrac1{\sqrt2}(1,-1) \). Then
\[
\u_1 = \frac{\A\v_1}{3\sqrt2} = \frac{(4,2,4)}{\sqrt2 \cdot 3\sqrt2} = \tfrac13(2,1,2),
\]
a unit vector since \( 4 + 1 + 4 = 9 \). The compact form is \( \A = 3\sqrt2\,\u_1\v_1\tp \), and multiplying out gives back \( \A \).

Four subspaces: \( \col(\A) = \Span\bigl(\tfrac13(2,1,2)\bigr) \) and \( \row(\A) = \Span\bigl(\tfrac1{\sqrt2}(1,1)\bigr) \), both one-dimensional; \( \nul(\A) = \Span\bigl(\tfrac1{\sqrt2}(1,-1)\bigr) \); and \( \nul(\A\tp) \) is the plane \( \{\y : 2y_1 + y_2 + 2y_3 = 0\} \), for which an orthonormal basis is \( \tfrac1{\sqrt2}(1,0,-1) \) and \( \tfrac1{3\sqrt2}(1,-4,1) \). (Any orthonormal basis of that plane is a legitimate \( (\u_2, \u_3) \), which is the freedom described in @thm-singular-values-unique (b).)
:::

::: {#exr-singular-value-decomposition-b4}
[B4: Determine whether]

Determine which of the following statements are correct. For those that are correct, prove them; for those that are not, give a counterexample.

::: {.enumerate options="label=(\alph*)"}
1. If every eigenvalue of \( \A \in M_n(\nC) \) is \( 0 \), then every singular value of \( \A \) is \( 0 \).
2. \( \sigma_i(c\A) = \lvert c\rvert\,\sigma_i(\A) \) for every scalar \( c \).
3. \( \sigma_i(\A^2) = \sigma_i(\A)^2 \) for every square \( \A \).
4. \( \A \) is invertible if and only if \( n = m \) and every singular value of \( \A \) is non-zero.
:::
:::

::: {.solution}
(a) Incorrect. \( \N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \) has spectrum \( \{0\} \), while \( \N^{*}\N = \diag(0,1) \) gives \( \sigma_1 = 1 \).

(b) Correct. \( (c\A)^{*}(c\A) = \conj{c}c\,\A^{*}\A = \lvert c\rvert^2\A^{*}\A \), whose eigenvalues are \( \lvert c\rvert^2\lambda_i \); taking square roots and noting that multiplying by \( \lvert c\rvert^2 \ge 0 \) preserves the decreasing order gives the claim.

(c) Incorrect, with the same \( \N \): \( \N^2 = \0 \) has both singular values \( 0 \), while \( \sigma_1(\N)^2 = 1 \). (It is correct for \( \A \succeq 0 \), and more generally for normal \( \A \), because then the singular values are the moduli of the eigenvalues and \( \A^2 \) has eigenvalues \( \lambda_i^2 \).)

(d) Correct. If \( \A \in M_n(F) \) then, by @thm-svd, the number of non-zero singular values is \( \rank\A \), and \( \A \) is invertible exactly when \( \rank\A = n \) (@thm-invertible-tfae). A non-square matrix is never invertible.
:::

### C. Going deeper

::: {#exr-singular-value-decomposition-c1}
[C1: The Frobenius norm and the largest singular value]

Let \( \A \in M_{m \times n}(F) \) with singular values \( \sigma_1 \ge \dots \ge \sigma_p \).

::: {.enumerate options="label=(\alph*)"}
1. The text obtained \( \norm{\A}_F^2 = \sum_{i=1}^{p}\sigma_i^2 \) from unitary invariance. Prove it a second way, directly from \( \norm{\A}_F^2 = \tr(\A^{*}\A) \) and the eigenvalues of \( \A^{*}\A \), without invoking @lem-frobenius-unitarily-invariant.
2. Deduce that \( \sigma_1 \le \norm{\A}_F \), and determine exactly when equality holds.
:::
:::

::: {.solution}
(a) Take a singular value decomposition \( \A = \U\vSigma\V^{*} \) (@thm-svd). By @lem-frobenius-unitarily-invariant, applied once on each side, \( \norm{\A}_F = \norm{\U\vSigma\V^{*}}_F = \norm{\vSigma}_F \). The only non-zero entries of \( \vSigma \) are \( \sigma_1, \dots, \sigma_p \) on the diagonal, so \( \norm{\vSigma}_F^2 = \sum_i \sigma_i^2 \).

(b) Every term of \( \sum_i\sigma_i^2 \) is non-negative, so \( \sigma_1^2 \le \sum_i\sigma_i^2 = \norm{\A}_F^2 \), and taking non-negative square roots gives \( \sigma_1 \le \norm{\A}_F \). Equality holds if and only if \( \sigma_2 = \dots = \sigma_p = 0 \), that is, if and only if \( \rank\A \le 1 \) (@thm-svd).
:::

::: {#exr-singular-value-decomposition-c2}
[C2: The adjoint and the determinant]

Let \( \A \in M_{m \times n}(F) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \A \) and \( \A^{*} \) have the same non-zero singular values, with the same multiplicities.
2. Suppose \( m = n \). Prove that \( \lvert\det\A\rvert = \sigma_1\sigma_2\cdots\sigma_n \).
3. Hence give a formula for \( \lvert\det\A\rvert \) in terms of \( \A^{*}\A \) only, and check it on \( \A = \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix} \).
:::
:::

::: {.solution}
(a) If \( \A = \U\vSigma\V^{*} \) is a singular value decomposition, then \( \A^{*} = \V\vSigma^{*}\U^{*} \) with \( \V, \U \) unitary and \( \vSigma^{*} \in M_{n \times m}(\nR) \) carrying the same diagonal entries \( \sigma_1, \dots, \sigma_p \). By @thm-singular-values-unique this is a singular value decomposition of \( \A^{*} \), so the singular value list of \( \A^{*} \) is \( \sigma_1, \dots, \sigma_p \) as well. (The two lists have the same length \( p = \min(m,n) \), so they are in fact equal, not merely equal in their non-zero parts.)

(b) Take determinants in \( \A = \U\vSigma\V^{*} \). By @thm-det-multiplicative, \( \det\A = \det\U \cdot \det\vSigma \cdot \det\V^{*} \). A unitary \( \U \) has \( \lvert\det\U\rvert = 1 \), since \( \det(\U^{*})\det(\U) = \det(\I) = 1 \) and \( \det(\U^{*}) = \conj{\det\U} \), so \( \lvert\det\U\rvert^2 = 1 \). The same holds for \( \V^{*} \). And \( \det\vSigma = \sigma_1\cdots\sigma_n \) by @thm-det-triangular. Taking absolute values gives \( \lvert\det\A\rvert = \sigma_1\cdots\sigma_n \).

(c) Squaring, \( \lvert\det\A\rvert^2 = \prod_i\sigma_i^2 = \det(\A^{*}\A) \), so \( \lvert\det\A\rvert = \sqrt{\det(\A^{*}\A)} \). For the given \( \A \), \( \det\A = 15 \) and \( \det(\A\tp\A) = 625 - 400 = 225 = 15^2 \).
:::

::: {#exr-singular-value-decomposition-c3}
[C3: Singular values equal to eigenvalue moduli]

Let \( \A \in M_n(\nC) \) have eigenvalues \( \lambda_1, \dots, \lambda_n \) listed with algebraic multiplicity and ordered so that \( \lvert\lambda_1\rvert \ge \dots \ge \lvert\lambda_n\rvert \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( \A \) is normal, then \( \sigma_i(\A) = \lvert\lambda_i\rvert \) for every \( i \).
2. Prove the converse: if \( \sigma_i(\A) = \lvert\lambda_i\rvert \) for every \( i \), then \( \A \) is normal.
:::

*Hint for (b): compare two expressions for \( \norm{\A}_F^2 \).*
:::

::: {.solution}
(a) Suppose \( \A \) is normal. By @cor-spectral-complex-matrix, \( \A = \U\D\U^{*} \) with \( \U \) unitary and \( \D = \diag(\lambda_1, \dots, \lambda_n) \). Then
\[
\A^{*}\A = \U\D^{*}\U^{*}\U\D\U^{*} = \U\,\diag\bigl(\lvert\lambda_i\rvert^2\bigr)\,\U^{*} ,
\]
so the eigenvalues of \( \A^{*}\A \) are \( \lvert\lambda_1\rvert^2, \dots, \lvert\lambda_n\rvert^2 \) with multiplicity. These are already in decreasing order by hypothesis, so \( \sigma_i(\A) = \lvert\lambda_i\rvert \) for every \( i \) by @def-singular-values.

(b) Suppose \( \sigma_i(\A) = \lvert\lambda_i\rvert \) for every \( i \). By @exr-singular-value-decomposition-c1 (a),
\[
\sum_{i=1}^{n}\lvert\lambda_i\rvert^2 = \sum_{i=1}^{n}\sigma_i^2 = \norm{\A}_F^2 .
\]
Schur's inequality (@thm-schur-inequality) says \( \sum_i\lvert\lambda_i\rvert^2 \le \norm{\A}_F^2 \) with equality **if and only if** \( \A \) is normal. We have equality, so \( \A \) is normal.
:::
