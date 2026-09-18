# Circulants and the Discrete Fourier Transform

The spectral theorem of Section 4 gives every normal matrix a unitary of its own, found by solving that matrix's eigenvalue problem. This section does something better for one particular family: it writes down a **single** unitary matrix, before any matrix of the family is named, and that one matrix diagonalizes all of them at once. The family is the circulants, the unitary is built from the \( n \)-th roots of unity, and the resulting dictionary between multiplying matrices and multiplying numbers is the discrete Fourier transform.

Two earlier pages pointed here. In @exm-normal-catalog (d) a \( 3 \times 3 \) matrix whose rows were cyclic shifts of one another turned out to be normal, with the row dot products and the column dot products agreeing entry for entry; @exr-spectral-theorem-complex-b2 met the same phenomenon again and diagonalized one such matrix by hand. Both times the agreement was described and not explained. It is explained below, and the explanation is the first theorem of the section.

Throughout, the field is \( \nC \), and **rows, columns and vector entries are numbered \( 0, 1, \dots, n-1 \)**. That is a departure from the rest of the book, and it is worth it: every formula here involves an index read modulo \( n \), and modular arithmetic starts at \( 0 \).

## Matrices whose rows walk around

Fix \( n \ge 1 \) and let \( \S \in M_n(\nC) \) be the matrix with \( (\S)_{jk} = 1 \) when \( k \equiv j + 1 \pmod n \) and \( (\S)_{jk} = 0 \) otherwise: a \( 1 \) in each position \( (j, j+1) \) for \( j \le n-2 \), one more in the corner position \( (n-1, 0) \), and zeros elsewhere. For \( n = 4 \),
\[
\S = \begin{pmatrix}
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
1 & 0 & 0 & 0
\end{pmatrix} .
\]
Applied to a vector, \( \S \) moves every entry one place up and sends the top entry around to the bottom: \( \S\x = (x_1, x_2, \dots, x_{n-1}, x_0) \). We call \( \S \) the **cyclic shift**. Each row and each column of \( \S \) carries exactly one \( 1 \), so \( \S \) is a permutation matrix (@def-permutation-matrix), and shifting \( n \) times returns every entry to where it started, so \( \S^n = \I \).

Now think of \( \S \) as a building block. The powers \( \I, \S, \S^2, \dots, \S^{n-1} \) are the \( n \) distinct "rotations of the identity", and a general linear combination of them is the object of this section.

*A circulant is a matrix that does not know where the list begins: shift the indices and nothing changes.*

::: {#def-circulant}
[Circulant matrix]

Let \( n \ge 1 \) and let \( \c = (c_0, c_1, \dots, c_{n-1}) \in \nC^n \). The **circulant** with first row \( \c \) is the matrix \( \C \in M_n(\nC) \) whose entries are
\[
(\C)_{jk} = c_{k-j} \qquad (0 \le j, k \le n-1),
\]
where the subscript \( k - j \) is read **modulo \( n \)**. The polynomial
\[
p_{\c}(x) = c_0 + c_1x + c_2x^2 + \dots + c_{n-1}x^{n-1} \in \nC[x]
\]
is called the **symbol** of \( \C \).
:::

In words: the entry in a given position depends only on how far the column is to the right of the diagonal, counted cyclically. Written out,
\[
\C = \begin{pmatrix}
c_0 & c_1 & \cdots & c_{n-1} \\
c_{n-1} & c_0 & \cdots & c_{n-2} \\
\vdots & \vdots & \ddots & \vdots \\
c_1 & c_2 & \cdots & c_0
\end{pmatrix} ,
\]
so each row is the row above it moved one step to the right, with the entry that falls off the right-hand end reappearing on the left. The columns behave the same way going down. Note that the data is one vector of length \( n \), not \( n^2 \) numbers: a circulant is a very small object wearing a large costume.

Three examples, simplest first. The vector \( \c = (1, 0, \dots, 0) \) gives \( \C = \I \), and \( \c = (0, 1, 0, \dots, 0) \) gives \( \C = \S \); in both cases the definition is checked by reading off \( (\C)_{jk} = c_{k-j} \), which is \( 1 \) exactly when \( k = j \), respectively \( k = j+1 \), modulo \( n \). The vector \( \c = (1, 1, \dots, 1) \) gives the all-ones matrix. The \( 3 \times 3 \) matrix of @exm-normal-catalog (d) is the circulant with first row \( (1, 2, 3) \), and the matrix of @exr-spectral-theorem-complex-b2 is the circulant with first row \( (1, 1, 0) \).

Our running example for the whole section is the \( 4 \times 4 \) circulant with first row \( (1, 2, 3, 4) \):
\[
\C = \begin{pmatrix}
1 & 2 & 3 & 4 \\
4 & 1 & 2 & 3 \\
3 & 4 & 1 & 2 \\
2 & 3 & 4 & 1
\end{pmatrix},
\qquad
p_{\c}(x) = 1 + 2x + 3x^2 + 4x^3 .
\]

A non-example by minimal change. Keep the first row \( (1, 2, 3, 4) \) but let the entries that fall off the end vanish instead of wrapping around, giving a matrix \( \B \) with rows \( (1,2,3,4) \), \( (0,1,2,3) \), \( (0,0,1,2) \), \( (0,0,0,1) \). Every diagonal of \( \B \) is still constant, and its first row is still \( \c \), but \( (\B)_{10} = 0 \) while the definition demands \( c_{0-1} = c_{3} = 4 \). The clause that fails is the one that does all the work here: the subscript must be read modulo \( n \). Matrices with constant diagonals and no wrap-around have their own name and their own theory, and the warning at the end of the section says why they do not fit into this one.

The reason a circulant is worth a name is that it is a polynomial in the shift.

::: {#thm-circulant-is-polynomial-in-shift}
[Circulants Are Exactly the Polynomials in the Shift]

Let \( \c \in \nC^n \) and let \( \C \) be the circulant with first row \( \c \), with symbol \( p_{\c} \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \C = p_{\c}(\S) \); conversely, \( q(\S) \) is a circulant for every \( q \in \nC[x] \).
2. \( \C^{*} \) is the circulant with first row \( (\conj{c_0}, \conj{c_{n-1}}, \conj{c_{n-2}}, \dots, \conj{c_1}) \).
3. \( \C \) is normal, and any two circulants of the same size commute.
:::
:::

::: {.idea}
For (a), read off the entries of \( \S^m \): it has a \( 1 \) in position \( (j, k) \) exactly when \( k = j + m \) modulo \( n \). So \( \S^m \) is the circulant that picks out the coefficient \( c_m \), and summing over \( m \) rebuilds \( \C \) one coefficient at a time. Once (a) is in hand, (b) and (c) are arithmetic with the single relation \( \S^{*} = \S^{n-1} \): the adjoint of a polynomial in \( \S \) is again a polynomial in \( \S \), and two polynomials in one matrix always commute (@thm-polynomial-of-matrix-properties).
:::

::: {.proof}
(a) We claim that \( (\S^m)_{jk} = 1 \) if \( k \equiv j + m \pmod n \) and \( (\S^m)_{jk} = 0 \) otherwise, for every \( m \ge 0 \). For \( m = 0 \) this says \( \S^0 = \I \). Assuming it for \( m \), expand one product: \( (\S^{m+1})_{jk} = \sum_i (\S)_{ji}(\S^{m})_{ik} \), and the only non-zero factor \( (\S)_{ji} \) sits at \( i \equiv j+1 \), so the sum is \( (\S^{m})_{j+1, k} \), which is \( 1 \) exactly when \( k \equiv j + 1 + m \). This proves the claim by induction. Hence, for each \( j \) and \( k \),
\[
\bigl(p_{\c}(\S)\bigr)_{jk} = \sum_{m=0}^{n-1} c_m (\S^m)_{jk} = c_{k-j},
\]
because exactly one value of \( m \) in \( \{0, \dots, n-1\} \) satisfies \( m \equiv k - j \pmod n \). So \( p_{\c}(\S) = \C \). Conversely, let \( q \in \nC[x] \). Dividing by \( x^n - 1 \) (@thm-polynomial-division) gives \( q = h \cdot (x^n - 1) + r \) with \( \deg r < n \), and \( \S^n = \I \) gives \( q(\S) = h(\S)(\S^n - \I) + r(\S) = r(\S) \), which is the circulant whose first row is the coefficient list of \( r \).

(b) \( \S \) is a permutation matrix with real entries, so \( \S^{*} = \S\tp = \S^{-1} \) (@lem-permutation-matrices (b)), and \( \S^{-1} = \S^{n-1} \) because \( \S^n = \I \). Therefore
\[
\C^{*} = \sum_{m=0}^{n-1} \conj{c_m}\,(\S^{*})^{m} = \sum_{m=0}^{n-1} \conj{c_m}\,\S^{-m} .
\]
For \( m = 0 \) the term is \( \conj{c_0}\I \), and for \( 1 \le m \le n-1 \) we have \( \S^{-m} = \S^{n-m} \). So the coefficient of \( \S^{r} \) is \( \conj{c_0} \) when \( r = 0 \) and \( \conj{c_{n-r}} \) when \( 1 \le r \le n-1 \), which is the stated first row.

(c) By (a) and (b), both \( \C \) and \( \C^{*} \) are polynomials in \( \S \), and any two polynomials in the same matrix commute (@thm-polynomial-of-matrix-properties). Hence \( \C^{*}\C = \C\C^{*} \). The same argument applies to two circulants \( \C = p(\S) \) and \( \C' = q(\S) \).
:::

That settles the coincidence noticed in @exm-normal-catalog (d) and again in @exr-spectral-theorem-complex-b2 (a). It is worth seeing it once at the level of entries, because the entries are what those pages compared. For any \( \A \in M_n(\nC) \), writing \( \a_0, \dots, \a_{n-1} \) for its columns and \( \r_0, \dots, \r_{n-1} \) for its rows, the definition of the matrix product gives
\[
(\A^{*}\A)_{jk} = \inner{\a_k}{\a_j},
\qquad
(\A\A^{*})_{jk} = \inner{\r_j}{\r_k} .
\]
So "normal" says exactly that the table of column inner products and the table of row inner products agree. Now let \( \A = \C \) be a circulant, so that \( (\C)_{ik} = c_{k-i} \). Re-index the first sum by \( t = j - i \) and the second by \( t = i - k \); as \( i \) runs through all residues modulo \( n \), so does \( t \) in each case. This gives
\[
\inner{\a_k}{\a_j} = \sum_{t=0}^{n-1} c_{t + k - j}\,\conj{c_t} = \inner{\r_j}{\r_k} ,
\]
all subscripts modulo \( n \). Both tables depend only on \( k - j \), and they are literally the same sum. Cyclic shifting is what makes the re-indexing legal, and that is the whole of the coincidence.

::: {.check}
Which vectors \( \c \in \nC^n \) give a circulant that is Hermitian? Answer for \( n = 4 \) with real entries.
:::

::: {.solution}
By @thm-circulant-is-polynomial-in-shift (b), \( \C^{*} = \C \) forces \( \conj{c_0} = c_0 \) and \( \conj{c_{n-m}} = c_m \) for \( 1 \le m \le n-1 \). For \( n = 4 \) with real entries this reads \( c_1 = c_3 \), with \( c_0 \) and \( c_2 \) unconstrained: the symmetric real \( 4 \times 4 \) circulants are exactly those whose first row has the form \( (c_0, c_1, c_2, c_1) \).
:::

## The eigenvectors of the shift

Everything now follows from one eigenvalue problem, the one for \( \S \). Since \( \S^n = \I \), any eigenvalue \( \lambda \) satisfies \( \lambda^n = 1 \), so the candidates are the \( n \)-th roots of unity of @exm-roots-of-unity. There are \( n \) of them and \( \S \) is an \( n \times n \) matrix, which is encouraging. The eigenvectors are equally explicit.

Fix
\[
\omega \coloneqq e^{2\pi i/n},
\]
so that \( 1, \omega, \omega^2, \dots, \omega^{n-1} \) are the \( n \) distinct \( n \)-th roots of unity, and \( \omega^{r} = 1 \) if and only if \( n \) divides \( r \) (@exm-roots-of-unity).

::: {#thm-shift-eigenvectors}
[Eigenvectors of the Cyclic Shift]

For \( j = 0, 1, \dots, n-1 \) let
\[
\f_j \coloneqq \tfrac{1}{\sqrt n}\bigl(1,\ \omega^{j},\ \omega^{2j},\ \dots,\ \omega^{(n-1)j}\bigr) \in \nC^n,
\]
that is, \( (\f_j)_m = \omega^{jm}/\sqrt n \). Then \( \S\f_j = \omega^{j}\f_j \). Consequently \( \S \) is a unitary matrix with the \( n \) distinct eigenvalues \( 1, \omega, \dots, \omega^{n-1} \), and each eigenspace \( E_{\omega^j}(\S) \) is the line \( \Span(\f_j) \).
:::

::: {.idea}
The shift moves entry \( m+1 \) into slot \( m \). If the entries are the successive powers of a fixed number \( z \), that is the same as multiplying the whole vector by \( z \) — provided the wrap-around at the end also multiplies by \( z \), which is exactly the condition \( z^n = 1 \). So the geometric vectors \( (1, z, z^2, \dots) \) with \( z^n = 1 \) are forced on us, and there are \( n \) of them.
:::

::: {.proof}
Fix \( j \) and let \( 0 \le m \le n-1 \). By the description of \( \S \), the \( m \)-th entry of \( \S\f_j \) is the \( (m+1) \)-st entry of \( \f_j \), indices modulo \( n \). For \( m < n-1 \) this is
\[
\frac{\omega^{j(m+1)}}{\sqrt n} = \omega^{j}\cdot\frac{\omega^{jm}}{\sqrt n} = \omega^{j}(\f_j)_m,
\]
and for \( m = n-1 \) it is \( (\f_j)_0 = 1/\sqrt n \), while \( \omega^{j}(\f_j)_{n-1} = \omega^{j}\omega^{j(n-1)}/\sqrt n = \omega^{jn}/\sqrt n = 1/\sqrt n \) because \( \omega^n = 1 \). The two agree, so \( \S\f_j = \omega^{j}\f_j \). Each \( \f_j \) is non-zero, since its \( 0 \)-th entry is \( 1/\sqrt n \), so \( \omega^j \) is an eigenvalue.

The matrix \( \S \) is a real permutation matrix, so \( \S\tp\S = \I \) by @lem-permutation-matrices (b), and \( \S^{*} = \S\tp \); hence \( \S \) is unitary (@def-unitary-orthogonal). The \( n \) numbers \( 1, \omega, \dots, \omega^{n-1} \) are distinct, so \( \S \) has \( n \) distinct eigenvalues, and the sum of their eigenspaces is direct (@cor-eigenspaces-direct-sum). Each of those \( n \) eigenspaces has dimension at least \( 1 \) and their dimensions add up to at most \( \dim\nC^n = n \), so each has dimension exactly \( 1 \). Since \( \f_j \in E_{\omega^j}(\S) \) is non-zero, that eigenspace is \( \Span(\f_j) \).
:::

The vectors \( \f_0, \dots, \f_{n-1} \) are called the **Fourier vectors**. They are already known to be pairwise orthogonal: \( \S \) is unitary, hence normal, and eigenvectors of a normal matrix for distinct eigenvalues are orthogonal (@cor-normal-orthogonal-eigenspaces). But the direct computation is short, it produces the normalization at the same time, and it is the computation on which the rest of the section runs. So we do it.

::: {#thm-fourier-matrix-unitary}
[The Fourier Matrix Is Unitary]

The list \( (\f_0, \f_1, \dots, \f_{n-1}) \) is an orthonormal basis of \( \nC^n \). Equivalently, the **Fourier matrix**
\[
\F \coloneqq \frac{1}{\sqrt n}
\begin{pmatrix}
1 & 1 & \cdots & 1 \\
1 & \omega & \cdots & \omega^{n-1} \\
\vdots & \vdots & & \vdots \\
1 & \omega^{n-1} & \cdots & \omega^{(n-1)^2}
\end{pmatrix},
\qquad (\F)_{mj} = \frac{\omega^{mj}}{\sqrt n},
\]
whose \( j \)-th column is \( \f_j \), is unitary: \( \F^{*}\F = \F\F^{*} = \I \).
:::

::: {.proof}
Let \( 0 \le j, k \le n-1 \). Since \( \lvert\omega\rvert = 1 \) we have \( \conj{\omega} = \omega^{-1} \), hence \( \conj{\omega^{km}} = \omega^{-km} \), and so
\[
\inner{\f_j}{\f_k}
= \frac{1}{n}\sum_{m=0}^{n-1} \omega^{jm}\,\conj{\omega^{km}}
= \frac{1}{n}\sum_{m=0}^{n-1} \bigl(\omega^{j-k}\bigr)^{m} ,
\]
the inner product being linear in the first slot and conjugate-linear in the second.

*Case \( j = k \).* Then \( \omega^{j-k} = \omega^{0} = 1 \), so every one of the \( n \) terms equals \( 1 \) and the sum is \( n \). Hence \( \inner{\f_j}{\f_j} = n/n = 1 \), and \( \norm{\f_j} = 1 \).

*Case \( j \neq k \).* Put \( z \coloneqq \omega^{j-k} \). Then \( z^{n} = (\omega^{n})^{j-k} = 1 \). Also \( z \neq 1 \): by @exm-roots-of-unity, \( \omega^{j-k} = 1 \) would force \( n \) to divide \( j - k \), and \( 0 < \lvert j - k\rvert \le n-1 \) makes that impossible. Now use the factorization
\[
(z - 1)\bigl(1 + z + z^{2} + \dots + z^{n-1}\bigr) = z^{n} - 1 = 0 ,
\]
which is a polynomial identity valid for every complex \( z \). Since \( z - 1 \neq 0 \), we may divide by it, and
\[
\sum_{m=0}^{n-1} z^{m} = 0 .
\]
Hence \( \inner{\f_j}{\f_k} = 0 \).

So the list is orthonormal; it has \( n = \dim\nC^n \) members and is independent (@thm-orthogonal-independent), hence a basis (@thm-right-size-basis). A matrix whose columns form an orthonormal basis of \( \nC^n \) is unitary (@thm-isometry-characterizations (f)), which gives \( \F^{*}\F = \F\F^{*} = \I \).
:::

The second case is where the whole section lives. A sum of \( n \) unit complex numbers, spread evenly around the circle, cancels — and it cancels for the cheapest possible reason, that a geometric series with ratio \( z \neq 1 \) and \( z^n = 1 \) telescopes to zero.

::: {#exm-fourier-matrix-4}
[The Fourier matrix of size four]

Write out \( \F \) for \( n = 4 \), and check one orthogonality relation by hand.
:::

::: {.solution}
For \( n = 4 \), \( \omega = e^{2\pi i/4} = i \), and the powers cycle \( i^0 = 1 \), \( i^1 = i \), \( i^2 = -1 \), \( i^3 = -i \). So
\[
\F = \frac12\begin{pmatrix}
1 & 1 & 1 & 1 \\
1 & i & -1 & -i \\
1 & -1 & 1 & -1 \\
1 & -i & -1 & i
\end{pmatrix} .
\]
Take \( j = 1 \), \( k = 3 \). Then \( \omega^{j-k} = i^{-2} = -1 \), and
\[
\inner{\f_1}{\f_3} = \tfrac14\bigl(1 + (-1) + 1 + (-1)\bigr) = 0 ,
\]
matching the geometric-series computation with \( z = -1 \), for which \( 1 + z + z^2 + z^3 = 0 \). Note that \( \F \) is symmetric, \( \F\tp = \F \), but **not** Hermitian: \( \F^{*} = \conj{\F} \neq \F \), since \( (\F)_{12} = i/2 \).
:::

## One unitary for every circulant

::: {#thm-circulant-diagonalization}
[Circulant Diagonalization]

Let \( \C \in M_n(\nC) \) be the circulant with first row \( \c \) and symbol \( p_{\c} \). Then every Fourier vector is an eigenvector of \( \C \),
\[
\C\f_j = p_{\c}(\omega^{j})\,\f_j \qquad (j = 0, 1, \dots, n-1),
\]
and consequently
\[
\F^{*}\C\F = \diag\bigl(p_{\c}(1),\ p_{\c}(\omega),\ \dots,\ p_{\c}(\omega^{n-1})\bigr) .
\]
The same unitary \( \F \) works for every circulant of size \( n \), and \( \det\C = \prod_{j=0}^{n-1} p_{\c}(\omega^{j}) \).
:::

::: {.idea}
There is nothing left to prove. A circulant is a polynomial in \( \S \) by @thm-circulant-is-polynomial-in-shift, and a polynomial in a matrix acts on an eigenvector of that matrix by the same polynomial applied to the eigenvalue. The point is not the proof but the statement: \( \F \) was written down without reference to \( \c \), so a single change of orthonormal basis handles the entire family at once.
:::

::: {.proof}
By @thm-circulant-is-polynomial-in-shift (a), \( \C = p_{\c}(\S) \), and by @thm-shift-eigenvectors, \( \S\f_j = \omega^{j}\f_j \). Iterating the latter gives \( \S^{m}\f_j = \omega^{jm}\f_j \) for every \( m \ge 0 \), so
\[
\C\f_j = \sum_{m=0}^{n-1} c_m\,\S^{m}\f_j = \Bigl(\sum_{m=0}^{n-1} c_m\omega^{jm}\Bigr)\f_j = p_{\c}(\omega^{j})\,\f_j .
\]

The \( j \)-th column of \( \F \) is \( \f_j \), so the \( j \)-th column of \( \C\F \) is \( p_{\c}(\omega^j)\f_j \), which is the \( j \)-th column of \( \F\D \) for \( \D = \diag(p_{\c}(1), \dots, p_{\c}(\omega^{n-1})) \). Hence \( \C\F = \F\D \), and multiplying on the left by \( \F^{*} = \F^{-1} \) (@thm-fourier-matrix-unitary) gives \( \F^{*}\C\F = \D \). Taking determinants, \( \det\C = \det\D = \prod_j p_{\c}(\omega^j) \), since \( \det\F^{*}\det\F = \det(\F^{*}\F) = 1 \) (@thm-det-multiplicative).
:::

This re-proves normality from the other side, and closes the account opened in @exm-normal-catalog (d): \( \C = \F\D\F^{*} \) with \( \F \) unitary and \( \D \) diagonal is precisely the factorization that @cor-spectral-complex-matrix reserves for normal matrices. The eigenvalues \( p_{\c}(\omega^j) \) need no characteristic polynomial either: they are \( n \) evaluations of a polynomial of degree less than \( n \).

::: {#exm-circulant-4x4-eigenvalues}
[The running example, diagonalized]

Find the eigenvalues and the determinant of the circulant \( \C \) with first row \( (1, 2, 3, 4) \), and write down \( \F^{*}\C\F \).
:::

::: {.solution}
Here \( n = 4 \), \( \omega = i \) and \( p_{\c}(x) = 1 + 2x + 3x^2 + 4x^3 \). Evaluate at the four fourth roots of unity, using \( i^2 = -1 \) and \( i^3 = -i \):
\[
\begin{aligned}
p_{\c}(1) &= 1 + 2 + 3 + 4 = 10, \\
p_{\c}(i) &= 1 + 2i - 3 - 4i = -2 - 2i, \\
p_{\c}(-1) &= 1 - 2 + 3 - 4 = -2, \\
p_{\c}(-i) &= 1 - 2i - 3 + 4i = -2 + 2i .
\end{aligned}
\]
So \( \F^{*}\C\F = \diag(10,\, -2-2i,\, -2,\, -2+2i) \) with \( \F \) as in @exm-fourier-matrix-4, and
\[
\det\C = 10 \cdot (-2-2i) \cdot (-2) \cdot (-2+2i) = -20\bigl(4 + 4\bigr) = -160 ,
\]
using \( (-2-2i)(-2+2i) = 4 + 4 = 8 \). As a check on the first eigenvalue: every row of \( \C \) sums to \( 10 \), so \( \C\1 = 10\cdot\1 \), and \( \f_0 = \tfrac12\1 \).
:::

::: {.check}
The matrix of @exm-circulant-4x4-eigenvalues is real, and two of its eigenvalues are not. Why must those two be complex conjugates of each other, and which two are they in general?
:::

::: {.solution}
If every \( c_m \) is real then \( \conj{p_{\c}(z)} = p_{\c}(\conj z) \) for every \( z \). Taking \( z = \omega^{j} \) and using \( \conj{\omega^{j}} = \omega^{-j} = \omega^{n-j} \),
\[
\conj{p_{\c}(\omega^{j})} = p_{\c}(\omega^{n-j}),
\]
so the eigenvalue attached to \( \f_j \) and the one attached to \( \f_{n-j} \) are conjugate. Here \( n = 4 \) and the pair is \( j = 1, 3 \): \( \conj{-2-2i} = -2+2i \). The eigenvalues for \( j = 0 \) and, when \( n \) is even, \( j = n/2 \) are their own conjugates, hence real — which is why \( 10 \) and \( -2 \) came out real. (This is also @thm-real-matrix-complex-eigenvalues, seen here with the eigenvectors named.)
:::

Once every circulant is \( \F\D\F^{*} \), the family closes up on itself.

::: {#cor-circulants-algebra}
[Circulants Form a Commutative Algebra]

Let \( \cC_n \subseteq M_n(\nC) \) be the set of circulants of size \( n \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \cC_n \) is a subspace of \( M_n(\nC) \) of dimension \( n \), with basis \( \I, \S, \dots, \S^{n-1} \);
2. \( \cC_n \) is closed under products, and any two of its members commute;
3. \( \A \in \cC_n \) if and only if \( \F^{*}\A\F \) is diagonal;
4. a circulant \( \C \) is invertible if and only if \( p_{\c}(\omega^{j}) \neq 0 \) for every \( j \), and then \( \C^{-1} \) is again a circulant.
:::
:::

::: {.proof}
(a) The map \( \c \mapsto p_{\c}(\S) \) from \( \nC^n \) to \( M_n(\nC) \) is linear and, by @thm-circulant-is-polynomial-in-shift (a), its image is exactly \( \cC_n \). It is injective, because the first row of \( p_{\c}(\S) \) is \( \c \). So \( \cC_n \) is a subspace of dimension \( n \), and the images \( \I, \S, \dots, \S^{n-1} \) of the standard basis form a basis of it.

(b) If \( \C = p(\S) \) and \( \C' = q(\S) \), then \( \C\C' = (pq)(\S) \) (@thm-polynomial-of-matrix-properties), which is a circulant by @thm-circulant-is-polynomial-in-shift (a). Commutativity is part (c) of that theorem.

(c) \( (\Rightarrow) \) is @thm-circulant-diagonalization. \( (\Leftarrow) \) Suppose \( \F^{*}\A\F = \D = \diag(d_0, \dots, d_{n-1}) \). The \( n \) numbers \( 1, \omega, \dots, \omega^{n-1} \) are distinct, so by Lagrange interpolation (@thm-lagrange-interpolation) there is \( q \in \nC[x] \) with \( q(\omega^{j}) = d_j \) for every \( j \). By @thm-circulant-diagonalization applied to the circulant \( q(\S) \), which has symbol the remainder of \( q \) on division by \( x^n - 1 \),
\[
\F^{*}q(\S)\F = \diag\bigl(q(1), \dots, q(\omega^{n-1})\bigr) = \D .
\]
Multiplying both sides by \( \F \) on the left and \( \F^{*} \) on the right gives \( q(\S) = \A \), so \( \A \) is a circulant.

(d) From \( \C = \F\D\F^{*} \), \( \det\C = \det\D \), so \( \C \) is invertible exactly when no diagonal entry \( p_{\c}(\omega^j) \) vanishes (@thm-det-nonzero-iff-invertible). In that case \( \C^{-1} = \F\D^{-1}\F^{*} \), and \( \F^{*}\C^{-1}\F = \D^{-1} \) is diagonal, so \( \C^{-1} \) is a circulant by (c).
:::

Part (c) is the sharpest statement of the section: being a circulant is not a statement about the pattern of the entries at all, but a statement about which orthonormal basis diagonalizes the matrix. The pattern was only ever a way of recognizing it.

## Multiplying circulants is convolution

A circulant is its first row. So the product of two circulants must be computable from the two first rows, and it is worth knowing what that computation is.

Given \( \c, \d \in \nC^n \), define their **cyclic convolution** \( \c \ast \d \in \nC^n \) by
\[
(\c \ast \d)_r \coloneqq \sum_{l=0}^{n-1} c_l\, d_{r-l} \qquad (r = 0, \dots, n-1),
\]
subscripts modulo \( n \). In words: to get entry \( r \), slide the reversed list \( \d \) along \( \c \) so that the indices add up to \( r \), and add the products. It is the multiplication of polynomials with the exponents read modulo \( n \), and the next theorem says so.

::: {#thm-convolution-theorem}
[Convolution Theorem]

Let \( \c, \d \in \nC^n \) with circulants \( \C, \C' \) and symbols \( p_{\c}, p_{\d} \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \C\C' \) is the circulant with first row \( \c \ast \d \);
2. for every \( j \), \( \; p_{\c \ast \d}(\omega^{j}) = p_{\c}(\omega^{j})\,p_{\d}(\omega^{j}) \).
:::

In words: convolving the first rows corresponds to multiplying the eigenvalue lists entry by entry.
:::

::: {.idea}
Both parts are the identity \( p_{\c}p_{\d} \equiv p_{\c \ast \d} \pmod{x^n - 1} \), looked at twice. Multiplying the two symbols produces a polynomial of degree up to \( 2n-2 \); reducing the exponents modulo \( n \) folds the coefficients back into \( n \) slots, and the fold is precisely the convolution sum. Evaluating at a root of \( x^n - 1 \) makes the reduction invisible, which is (b); substituting \( \S \), for which \( \S^n = \I \), makes it invisible as well, which is (a).
:::

::: {.proof}
Expand the product of the symbols and collect exponents modulo \( n \):
\[
p_{\c}(x)\,p_{\d}(x) = \sum_{l=0}^{n-1}\sum_{m=0}^{n-1} c_l d_m x^{l+m} .
\]
For each \( r \in \{0, \dots, n-1\} \), the pairs \( (l, m) \) with \( l + m \equiv r \pmod n \) are exactly those with \( m \equiv r - l \), one value of \( m \) for each \( l \). Hence, working modulo \( x^n - 1 \) and using \( x^{l+m} \equiv x^{(l+m) \bmod n} \),
\[
p_{\c}(x)\,p_{\d}(x) \equiv \sum_{r=0}^{n-1}\Bigl(\sum_{l=0}^{n-1} c_l d_{r-l}\Bigr) x^{r} = p_{\c \ast \d}(x) \pmod{x^n - 1}.
\]

(a) Substitute \( \S \). Since \( \S^n = \I \), the multiple of \( x^n - 1 \) contributes nothing, so
\[
\C\C' = p_{\c}(\S)\,p_{\d}(\S) = p_{\c \ast \d}(\S),
\]
the first equality by @thm-circulant-is-polynomial-in-shift (a) and @thm-polynomial-of-matrix-properties. By @thm-circulant-is-polynomial-in-shift (a) again, \( p_{\c \ast \d}(\S) \) is the circulant with first row \( \c \ast \d \), the coefficient list having length \( n \).

(b) Substitute \( x = \omega^{j} \), a root of \( x^n - 1 \), so that the multiple of \( x^n - 1 \) again contributes nothing. This gives \( p_{\c}(\omega^j)p_{\d}(\omega^j) = p_{\c \ast \d}(\omega^j) \).
:::

Part (b) deserves its own sentence, because it is the reason the discrete Fourier transform is used at all. Define the **discrete Fourier transform** of \( \c \in \nC^n \) to be the vector of eigenvalues,
\[
\widehat{\c} \coloneqq \bigl(p_{\c}(1),\ p_{\c}(\omega),\ \dots,\ p_{\c}(\omega^{n-1})\bigr) = \sqrt n\,\F\c ,
\]
the second expression because the \( j \)-th entry of \( \F\c \) is \( n^{-1/2}\sum_m \omega^{jm}c_m \). Then (b) reads
\[
\bigl(\widehat{\c \ast \d}\bigr)_j = \widehat{\c}_j\,\widehat{\d}_j \qquad (j = 0, \dots, n-1) :
\]
the transform turns convolution into entrywise multiplication. Convolution is a tangled sum of \( n^2 \) products; after one unitary change of basis it is \( n \) ordinary multiplications. Everything the transform buys comes from this line.

::: {#exm-convolution-4x4}
[Convolution in size four]

Let \( \c = (1, 2, 3, 4) \) and \( \d = (1, 1, 0, 0) \). Compute \( \c \ast \d \), and verify @thm-convolution-theorem (b) at all four roots of unity.
:::

::: {.solution}
Since \( d_0 = d_1 = 1 \) and \( d_2 = d_3 = 0 \), the sum \( \sum_l c_l d_{r-l} \) keeps only the terms with \( r - l \equiv 0 \) or \( 1 \), that is \( l = r \) and \( l = r - 1 \). So \( (\c\ast\d)_r = c_r + c_{r-1} \), subscripts modulo \( 4 \):
\[
\c \ast \d = (1 + 4,\ 2 + 1,\ 3 + 2,\ 4 + 3) = (5, 3, 5, 7) .
\]
The three symbols are \( p_{\c}(x) = 1 + 2x + 3x^2 + 4x^3 \), \( p_{\d}(x) = 1 + x \) and \( p_{\c\ast\d}(x) = 5 + 3x + 5x^2 + 7x^3 \). Evaluating each at \( 1, i, -1, -i \), with \( p_{\c} \) already computed in @exm-circulant-4x4-eigenvalues:
\[
\begin{aligned}
j = 0: &\quad 10 \cdot 2 = 20, &&\quad 5 + 3 + 5 + 7 = 20; \\
j = 1: &\quad (-2-2i)(1+i) = -4i, &&\quad 5 + 3i - 5 - 7i = -4i; \\
j = 2: &\quad (-2)\cdot 0 = 0, &&\quad 5 - 3 + 5 - 7 = 0; \\
j = 3: &\quad (-2+2i)(1-i) = 4i, &&\quad 5 - 3i - 5 + 7i = 4i .
\end{aligned}
\]
All four agree. For the middle line, \( (-2-2i)(1+i) = -2 - 2i - 2i - 2i^2 = -4i \).
:::

## Solving a circulant system, and a word about speed

If \( \C\x = \b \) with \( \C \) an invertible circulant, then in the Fourier basis the system falls apart into \( n \) scalar equations. Writing \( \C = \F\D\F^{*} \) and setting \( \y = \F^{*}\x \), \( \g = \F^{*}\b \), the system becomes \( \D\y = \g \), that is \( y_j = g_j/\lambda_j \) with \( \lambda_j = p_{\c}(\omega^j) \). Then \( \x = \F\y \). Three steps: transform, divide, transform back.

::: {#exm-circulant-solve-system}
[A circulant system]

Solve \( \C\x = \b \) for the circulant \( \C \) with first row \( (1, 2, 3, 4) \) and \( \b = (1, 1, -1, -1) \).
:::

::: {.solution}
The eigenvalues are \( \lambda = (10,\, -2-2i,\, -2,\, -2+2i) \) by @exm-circulant-4x4-eigenvalues. First transform \( \b \): the \( j \)-th entry of \( \F^{*}\b \) is \( \tfrac12\sum_m \conj{\omega^{jm}}b_m = \tfrac12\sum_m (-i)^{jm}b_m \), so
\[
\begin{aligned}
g_0 &= \tfrac12(1 + 1 - 1 - 1) = 0, \\
g_1 &= \tfrac12\bigl(1 + (-i) - (-1) - (i)\bigr) = 1 - i, \\
g_2 &= \tfrac12(1 - 1 - 1 + 1) = 0, \\
g_3 &= \tfrac12\bigl(1 + i + 1 + i\bigr) = 1 + i .
\end{aligned}
\]
Now divide. The two zero entries stay zero, and
\[
y_1 = \frac{1-i}{-2-2i} = \frac{(1-i)(-2+2i)}{8} = \frac{4i}{8} = \frac{i}{2},
\qquad
y_3 = \conj{y_1} = -\frac{i}{2},
\]
where the middle step multiplies numerator and denominator by \( \conj{-2-2i} = -2+2i \), whose product with \( -2-2i \) is \( 8 \). Finally \( \x = \F\y \), whose \( m \)-th entry is \( \tfrac12(i^{m}y_1 + i^{3m}y_3) = \tfrac12\cdot\tfrac{i}{2}\bigl(i^{m} - (-i)^{m}\bigr) \):
\[
\x = \Bigl(0,\ -\tfrac12,\ 0,\ \tfrac12\Bigr) .
\]
Check directly: the second row of \( \C \) is \( (4, 1, 2, 3) \), and \( -\tfrac12 + \tfrac32 = 1 = b_1 \); the third row is \( (3, 4, 1, 2) \), and \( -2 + 1 = -1 = b_2 \). The answer is real, as it must be: \( \C \) and \( \b \) are real, so \( \x = \C^{-1}\b \) is real, and this shows up in the transform as the conjugate symmetry \( y_3 = \conj{y_1} \).
:::

Counted honestly, the recipe above saves something, but not yet very much. Forming \( \F^{*}\b \) as a matrix–vector product costs about \( n^2 \) multiplications, and so does forming \( \F\y \), so the whole solve costs on the order of \( n^2 \). That beats general elimination, which is on the order of \( n^3 \), but it is no better than multiplying \( \b \) by \( \C^{-1} \) once that inverse has been found. What changes the picture is that \( \F \) does not have to be applied as a general matrix. The powers of \( \omega \) repeat, and splitting the sum \( \sum_m \omega^{jm}b_m \) into its even and odd \( m \) reduces one transform of length \( n \) to two of length \( n/2 \); iterating brings the cost down to about \( n\log n \). That algorithm is the **fast Fourier transform**. It proves no new theorem: the matrix \( \F \), the factorization \( \C = \F\D\F^{*} \) and everything above are unchanged, and the fast Fourier transform is only a way of applying \( \F \) quickly. Chapter 23 develops it, together with the cost accounting that makes "quickly" precise.

::: {.warning}
A **Toeplitz** matrix — one with constant diagonals, \( (\A)_{jk} = a_{k-j} \) with the subscript **not** reduced modulo \( n \) — is not a circulant, and \( \F \) does not diagonalize it. Take
\[
\A = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix} .
\]
Every diagonal of \( \A \) is constant, so \( \A \) is Toeplitz, but the circulant with first row \( (0, 1, 0) \) is \( \S \), whose second row is \( (0, 0, 1) \), not \( (1, 0, 1) \). And \( \F \) fails at the very first column: \( \f_0 = \tfrac{1}{\sqrt3}(1,1,1) \) and \( \A\f_0 = \tfrac{1}{\sqrt3}(1, 2, 1) \), which is not a multiple of \( \f_0 \), so \( \f_0 \) is not an eigenvector and \( \F^{*}\A\F \) is not diagonal. Normality is not the issue: \( \A \) is symmetric, hence normal, and @thm-spectral-real does hand it an orthonormal eigenbasis. It is simply a different basis, with the irrational eigenvalues \( 0, \pm\sqrt2 \) in place of evaluations of a polynomial at roots of unity. What the wrap-around buys is not diagonalizability; it is the *same* diagonalizing basis for everybody.
:::

## Exercises

### A. Check your understanding

::: {#exr-circulants-and-the-dft-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the circulant with first row \( \c = (c_0, \dots, c_{n-1}) \), and write down its symbol.
2. State the eigenvalues and the eigenvectors of the cyclic shift \( \S \) on \( \nC^n \).
3. Give the eigenvalues of the circulant with first row \( \c \), and say how many multiplications are needed to compute all of them from \( \c \) by direct evaluation.
4. Determine whether the following are true, with a reason. (i) Every Toeplitz matrix is a circulant. (ii) Every circulant is normal. (iii) The Fourier matrix \( \F \) is Hermitian.
5. Explain in one sentence why two circulants of the same size commute, without computing any entries.
:::
:::

::: {.solution}
(a) The matrix \( \C \in M_n(\nC) \) with \( (\C)_{jk} = c_{k-j} \), subscripts modulo \( n \) and indices running from \( 0 \) to \( n-1 \) (@def-circulant). Its symbol is \( p_{\c}(x) = c_0 + c_1x + \dots + c_{n-1}x^{n-1} \).

(b) With \( \omega = e^{2\pi i/n} \): the eigenvalues are \( 1, \omega, \dots, \omega^{n-1} \), all distinct, and \( \omega^{j} \) has the one-dimensional eigenspace spanned by \( \f_j = n^{-1/2}(1, \omega^{j}, \dots, \omega^{(n-1)j}) \) (@thm-shift-eigenvectors).

(c) The eigenvalues are \( p_{\c}(\omega^{j}) \) for \( j = 0, \dots, n-1 \) (@thm-circulant-diagonalization). Each evaluation is a sum of \( n \) products, so all \( n \) of them cost about \( n^2 \) multiplications done directly.

(d) (i) False: the \( 3 \times 3 \) matrix in the warning above has constant diagonals but is not a circulant. (ii) True, by @thm-circulant-is-polynomial-in-shift (c); equivalently by @cor-spectral-complex-matrix, since \( \C = \F\D\F^{*} \). (iii) False. \( \F \) is symmetric, but \( \F^{*} = \conj{\F} \), and for \( n = 4 \) the entry \( (\F)_{12} = i/2 \) is not real (@exm-fourier-matrix-4). \( \F \) is Hermitian only for \( n = 1, 2 \), where all its entries are real.

(e) Both are polynomials in the single matrix \( \S \) (@thm-circulant-is-polynomial-in-shift (a)), and two polynomials in one matrix always commute (@thm-polynomial-of-matrix-properties).
:::

### B. Practice

::: {#exr-circulants-and-the-dft-b1}
[B1: Eigenvalues of small circulants]

For each vector \( \c \), write down the symbol, compute all eigenvalues of the circulant with first row \( \c \), and give its determinant.

::: {.enumerate options="label=(\alph*)"}
1. \( \c = (1, 1, 1) \), \( n = 3 \).
2. \( \c = (0, 1, 0, 0) \), \( n = 4 \).
3. \( \c = (2, -1, 0, -1) \), \( n = 4 \).
:::
:::

::: {.solution}
(a) \( p_{\c}(x) = 1 + x + x^2 \). With \( \omega = e^{2\pi i/3} \), the eigenvalues are \( p_{\c}(1) = 3 \) and \( p_{\c}(\omega^{j}) = 1 + \omega^{j} + \omega^{2j} \) for \( j = 1, 2 \). For \( j \neq 0 \), \( z = \omega^{j} \) satisfies \( z \neq 1 \) and \( z^3 = 1 \), so \( 1 + z + z^2 = (z^3-1)/(z-1) = 0 \) — the geometric-series computation of @thm-fourier-matrix-unitary again. The eigenvalues are \( 3, 0, 0 \) and \( \det\C = 0 \). (This matrix is the all-ones matrix, of rank \( 1 \).)

(b) \( p_{\c}(x) = x \), so \( \C = \S \). The eigenvalues are \( \omega^{j} = i^{j} \), namely \( 1, i, -1, -i \), and
\[
\det\S = 1 \cdot i \cdot (-1) \cdot (-i) = \bigl(i \cdot (-i)\bigr)\bigl(1 \cdot (-1)\bigr) = -1 .
\]
This agrees with the sign of the permutation: \( \S \) permutes the coordinates in one \( 4 \)-cycle, which is odd.

(c) \( p_{\c}(x) = 2 - x - x^3 \). Then \( p_{\c}(1) = 0 \); \( p_{\c}(i) = 2 - i - i^3 = 2 - i + i = 2 \); \( p_{\c}(-1) = 2 + 1 + 1 = 4 \); \( p_{\c}(-i) = 2 + i - i = 2 \). The eigenvalues are \( 0, 2, 4, 2 \), and \( \det\C = 0 \). The kernel contains \( \f_0 \), that is the all-ones vector, as one sees directly: every row of \( \C \) sums to \( 0 \).
:::

::: {#exr-circulants-and-the-dft-b2}
[B2: Solve a circulant system by transforming]

Let \( \C \) be the \( 4 \times 4 \) circulant with first row \( (3, 1, 0, 1) \) and let \( \b = (1, 0, 0, 0) \). Compute the eigenvalues of \( \C \), and solve \( \C\x = \b \) by transforming, dividing and transforming back. Check your answer against the first two rows of \( \C \).
:::

::: {.solution}
The symbol is \( p_{\c}(x) = 3 + x + x^3 \), and with \( \omega = i \),
\[
p_{\c}(1) = 5, \quad p_{\c}(i) = 3 + i - i = 3, \quad p_{\c}(-1) = 1, \quad p_{\c}(-i) = 3 .
\]
All four are non-zero, so \( \C \) is invertible (@cor-circulants-algebra (d)), with \( \det\C = 5\cdot3\cdot1\cdot3 = 45 \).

Transform: \( (\F^{*}\b)_j = \tfrac12\sum_m \conj{\omega^{jm}}b_m = \tfrac12 \) for every \( j \), since \( \b = \e_0 \). Divide: \( y_j = \tfrac12\lambda_j^{-1} \), giving \( \y = \tfrac12(\tfrac15, \tfrac13, 1, \tfrac13) \). Transform back: the \( m \)-th entry of \( \x = \F\y \) is
\[
x_m = \tfrac12\sum_{j=0}^{3} i^{mj}y_j = \tfrac14\Bigl(\tfrac15 + \tfrac{i^{m}}{3} + (-1)^{m} + \tfrac{i^{3m}}{3}\Bigr).
\]
For \( m = 1 \) and \( m = 3 \) the two middle terms cancel, since \( i^{m} + i^{3m} = i^m + \conj{i^m} \) is \( 0 \) when \( i^m = \pm i \); the bracket is \( \tfrac15 - 1 \), so \( x_1 = x_3 = -\tfrac15 \). For \( m = 0 \) the bracket is \( \tfrac15 + \tfrac13 + 1 + \tfrac13 = \tfrac{28}{15} \), so \( x_0 = \tfrac{7}{15} \). For \( m = 2 \) it is \( \tfrac15 - \tfrac13 + 1 - \tfrac13 = \tfrac{8}{15} \), so \( x_2 = \tfrac{2}{15} \). Hence
\[
\x = \Bigl(\tfrac{7}{15},\ -\tfrac15,\ \tfrac{2}{15},\ -\tfrac15\Bigr).
\]
Check: row \( 0 \) of \( \C \) is \( (3,1,0,1) \) and \( 3\cdot\tfrac7{15} - \tfrac15 - \tfrac15 = \tfrac{21-3-3}{15} = 1 \); row \( 1 \) is \( (1,3,1,0) \) and \( \tfrac7{15} - \tfrac35 + \tfrac2{15} = \tfrac{7-9+2}{15} = 0 \).
:::

::: {#exr-circulants-and-the-dft-b3}
[B3: The convolution theorem in an example]

Let \( \c = (1, 0, 2, 0) \) and \( \d = (0, 1, 0, 3) \) in \( \nC^4 \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \c \ast \d \).
2. Verify \( p_{\c\ast\d}(\omega^{j}) = p_{\c}(\omega^{j})p_{\d}(\omega^{j}) \) for \( j = 0, 1, 2, 3 \).
3. Hence write down the first row of the product of the two circulants, without multiplying any matrices.
:::
:::

::: {.solution}
(a) Only \( c_0 = 1 \) and \( c_2 = 2 \) are non-zero, so \( (\c\ast\d)_r = d_r + 2d_{r-2} \), subscripts modulo \( 4 \). With \( \d = (0,1,0,3) \):
\[
\c \ast \d = (0 + 0,\ 1 + 6,\ 0 + 0,\ 3 + 2) = (0, 7, 0, 5).
\]

(b) The symbols are \( p_{\c}(x) = 1 + 2x^2 \), \( p_{\d}(x) = x + 3x^3 \) and \( p_{\c\ast\d}(x) = 7x + 5x^3 \). With \( \omega = i \):
\[
\begin{aligned}
j = 0: &\quad 3 \cdot 4 = 12, &&\quad 7 + 5 = 12; \\
j = 1: &\quad (-1)(-2i) = 2i, &&\quad 7i - 5i = 2i; \\
j = 2: &\quad 3 \cdot (-4) = -12, &&\quad -7 - 5 = -12; \\
j = 3: &\quad (-1)(2i) = -2i, &&\quad -7i + 5i = -2i .
\end{aligned}
\]
Here \( p_{\c}(i) = 1 + 2i^2 = -1 \) and \( p_{\d}(i) = i + 3i^3 = i - 3i = -2i \), and similarly at the other roots. All four rows agree.

(c) By @thm-convolution-theorem (a), the product is the circulant with first row \( \c\ast\d = (0, 7, 0, 5) \).
:::

### C. Going deeper

::: {#exr-circulants-and-the-dft-c1}
[C1: What commutes with the shift]

Let \( \A \in M_n(\nC) \) satisfy \( \A\S = \S\A \). Prove that \( \A \) is a circulant. *Hint: consider the eigenspaces of \( \S \).*
:::

::: {.solution}
By @thm-shift-eigenvectors, \( \S \) has the \( n \) distinct eigenvalues \( \omega^{j} \), and \( E_{\omega^j}(\S) = \Span(\f_j) \) is one-dimensional. Since \( \A \) commutes with \( \S \), each eigenspace of \( \S \) is invariant under \( \A \) (@thm-commuting-preserves-eigenspaces). So \( \A\f_j \in \Span(\f_j) \), that is \( \A\f_j = d_j\f_j \) for some \( d_j \in \nC \).

Therefore the \( j \)-th column of \( \A\F \) is \( d_j\f_j \), which is the \( j \)-th column of \( \F\D \) for \( \D = \diag(d_0, \dots, d_{n-1}) \). Hence \( \A\F = \F\D \) and \( \F^{*}\A\F = \D \) is diagonal, so \( \A \) is a circulant by @cor-circulants-algebra (c). This proves the converse of @thm-circulant-is-polynomial-in-shift (c) for the single matrix \( \S \): the commutant of the cyclic shift is exactly the algebra of circulants.
:::

::: {#exr-circulants-and-the-dft-c2}
[C2: Determinant and invertibility]

Let \( \C \) be the circulant with first row \( \c \in \nC^n \) and symbol \( p_{\c} \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \det\C = \prod_{j=0}^{n-1} p_{\c}(\omega^{j}) \), and use it to compute the determinant of the \( n \times n \) all-ones matrix for every \( n \ge 2 \).
2. Prove that \( \C \) is invertible if and only if \( p_{\c} \) and \( x^n - 1 \) are coprime in \( \nC[x] \).
3. Give an example of a \( 4 \times 4 \) circulant with integer entries, none of them \( 0 \), whose determinant is \( 0 \).
:::
:::

::: {.solution}
(a) This is the last claim of @thm-circulant-diagonalization: from \( \C = \F\D\F^{*} \) and \( \det(\F^{*})\det(\F) = \det(\F^{*}\F) = 1 \), multiplicativity of the determinant (@thm-det-multiplicative) gives \( \det\C = \det\D \), which is the product of the diagonal entries \( p_{\c}(\omega^{j}) \).

For the all-ones matrix, \( \c = (1, 1, \dots, 1) \) and \( p_{\c}(x) = 1 + x + \dots + x^{n-1} \). Then \( p_{\c}(1) = n \), while for \( 1 \le j \le n-1 \) the number \( z = \omega^{j} \) satisfies \( z^n = 1 \) and \( z \neq 1 \), so \( p_{\c}(z) = (z^n - 1)/(z - 1) = 0 \). Hence \( \det\C = n \cdot 0 \cdots 0 = 0 \) for every \( n \ge 2 \), as it must be, since all the rows are equal.

(b) By (a), \( \det\C \neq 0 \) if and only if \( p_{\c}(\omega^{j}) \neq 0 \) for every \( j \), that is, if and only if \( p_{\c} \) and \( x^n - 1 \) have no common root, the roots of \( x^n - 1 \) being exactly \( 1, \omega, \dots, \omega^{n-1} \) (@exm-roots-of-unity). Over \( \nC \), having no common root is the same as having no common non-constant factor: such a factor would have a root by @thm-fundamental-theorem-of-algebra, and that root would be common to both; conversely a common root \( \alpha \) makes \( x - \alpha \) a common factor. So invertibility of \( \C \) is equivalent to \( p_{\c} \) and \( x^n - 1 \) being coprime (@def-coprime). Combined with @thm-det-nonzero-iff-invertible, this is the statement asked for.

(c) Take \( \c = (1, 2, 1, 2) \), so
\[
\C = \begin{pmatrix} 1 & 2 & 1 & 2 \\ 2 & 1 & 2 & 1 \\ 1 & 2 & 1 & 2 \\ 2 & 1 & 2 & 1 \end{pmatrix},
\qquad p_{\c}(x) = 1 + 2x + x^2 + 2x^3 .
\]
Here \( p_{\c}(i) = 1 + 2i - 1 - 2i = 0 \), so \( \det\C = 0 \) by (a). The reason is visible without any of the theory — rows \( 0 \) and \( 2 \) are equal — and the Fourier picture names a kernel vector: \( \C\f_1 = \0 \), and since \( \C \) is real, the real and imaginary parts of \( \f_1 \) are in the kernel too, giving \( \C(1, 0, -1, 0) = \0 \).
:::

::: {#exr-circulants-and-the-dft-c3}
[C3: The real orthogonal form of a real circulant]

Let \( \C \in M_4(\nR) \) be the circulant with first row \( (1, 2, 3, 4) \), with eigenvalues \( 10, -2-2i, -2, -2+2i \) as in @exm-circulant-4x4-eigenvalues. Put
\[
\g \coloneqq \sqrt2\,\operatorname{Re}\f_1, \qquad \h \coloneqq \sqrt2\,\operatorname{Im}\f_1,
\]
the real and imaginary parts taken entrywise.

::: {.enumerate options="label=(\alph*)"}
1. Write \( \g \) and \( \h \) out, and show that \( (\f_0, \f_2, \g, \h) \) is an orthonormal basis of \( \nR^4 \).
2. Writing \( a + bi \coloneqq -2 + 2i \), prove that \( \C\g = a\g + b\h \) and \( \C\h = -b\g + a\h \).
3. Hence write down the matrix of \( \C \) in the ordered basis of (a), and identify it as an instance of @thm-real-normal-form.
:::

*Hint for (b): apply \( \C \) to \( \f_3 = (\g - i\h)/\sqrt2 \) and compare real and imaginary parts.*
:::

::: {.solution}
(a) With \( \omega = i \), \( \f_1 = \tfrac12(1, i, -1, -i) \), so
\[
\g = \tfrac{1}{\sqrt2}(1, 0, -1, 0), \qquad \h = \tfrac{1}{\sqrt2}(0, 1, 0, -1).
\]
Also \( \f_0 = \tfrac12(1,1,1,1) \) and \( \f_2 = \tfrac12(1,-1,1,-1) \) are real, so all four vectors lie in \( \nR^4 \). Each has norm \( 1 \): for instance \( \norm{\g}^2 = \tfrac12(1 + 1) = 1 \) and \( \norm{\f_0}^2 = \tfrac14 \cdot 4 = 1 \). They are pairwise orthogonal for the real dot product. First \( \g\cdot\h = 0 \), because the non-zero entries sit in different slots, and \( \f_0\cdot\f_2 = \tfrac14(1 - 1 + 1 - 1) = 0 \). The four remaining pairings are
\[
\begin{aligned}
\f_0 \cdot \g &= \tfrac{1}{2\sqrt2}(1 - 1) = 0, &
\f_2 \cdot \g &= \tfrac{1}{2\sqrt2}(1 - 1) = 0, \\
\f_0 \cdot \h &= \tfrac{1}{2\sqrt2}(1 - 1) = 0, &
\f_2 \cdot \h &= \tfrac{1}{2\sqrt2}(-1 + 1) = 0 .
\end{aligned}
\]
Four orthonormal vectors are independent (@thm-orthogonal-independent) and there are \( \dim\nR^4 = 4 \) of them, so they form a basis (@thm-right-size-basis).

(b) From \( \f_1 = \tfrac{1}{\sqrt2}(\g + i\h) \) and \( \f_3 = \conj{\f_1} \) we get \( \f_3 = \tfrac{1}{\sqrt2}(\g - i\h) \). Its eigenvalue is \( p_{\c}(\omega^{3}) = p_{\c}(-i) = -2 + 2i = a + bi \), so \( a = -2 \) and \( b = 2 \), and \( \C\f_3 = (a+bi)\f_3 \) reads
\[
\tfrac{1}{\sqrt2}\bigl(\C\g - i\,\C\h\bigr)
= \tfrac{1}{\sqrt2}(a + bi)(\g - i\h)
= \tfrac{1}{\sqrt2}\bigl((a\g + b\h) + i(b\g - a\h)\bigr).
\]
Both \( \C\g \) and \( \C\h \) are real vectors, because \( \C \), \( \g \) and \( \h \) are real. Comparing real parts gives \( \C\g = a\g + b\h \), and comparing imaginary parts gives \( -\C\h = b\g - a\h \), that is \( \C\h = -b\g + a\h \). With \( a = -2 \) and \( b = 2 \),
\[
\C\g = -2\g + 2\h, \qquad \C\h = -2\g - 2\h .
\]
A direct check: \( \sqrt2\,\C\g = \C(1,0,-1,0) = (1 - 3,\ 4 - 2,\ 3 - 1,\ 2 - 4) = (-2, 2, 2, -2) \), while \( \sqrt2\,(-2\g + 2\h) = (-2, 2, 2, -2) \).

(c) Reading the coordinates of the images off (b), the matrix in the ordered basis \( (\f_0, \f_2, \g, \h) \) is
\[
\begin{pmatrix}
10 & 0 & 0 & 0 \\
0 & -2 & 0 & 0 \\
0 & 0 & -2 & -2 \\
0 & 0 & 2 & -2
\end{pmatrix}
= (10) \oplus (-2) \oplus \vLambda(-2 + 2i),
\]
since \( \vLambda(a + bi) \) has rows \( (a, -b) \) and \( (b, a) \). This is exactly the shape promised by @thm-real-normal-form for a real normal operator: two \( 1 \times 1 \) blocks for the real eigenvalues, and one rotation-scaling block for the conjugate pair, with \( b = 2 > 0 \). The change of basis is orthogonal, because the basis is orthonormal.
:::
