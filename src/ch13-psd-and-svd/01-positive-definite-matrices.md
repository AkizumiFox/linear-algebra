# Positive Semidefinite and Positive Definite Matrices

Chapter 12 sorted the operators that have an orthonormal eigenbasis. Among them the self-adjoint ones are the matrix analogue of the real numbers, since they are exactly the operators fixed by starring. Inside the real numbers sits a smaller and even more useful set, the non-negative ones, and this section finds its matrix analogue. The answer turns out to have three faces — a sign condition on the spectrum, a sign condition on a scalar function, and a factorization — and the whole of the rest of the chapter is built on the fact that the three agree.

Throughout, \( F = \nR \) or \( F = \nC \), and \( F^n \) carries the standard inner product \( \inner{\x}{\y} = \y^{*}\x \).

## Which self-adjoint matrices deserve to be called non-negative?

A real number \( t \) is non-negative in three equivalent ways: \( t \ge 0 \); \( tx^2 \ge 0 \) for every real \( x \); and \( t = s^2 \) for some real \( s \). Each of the three has a matrix reading. "Every eigenvalue is \( \ge 0 \)" copies the first. "\( \inner{\A\x}{\x} \ge 0 \) for every \( \x \)" copies the second, because \( \inner{\A\x}{\x} \) is the one scalar a matrix attaches to a single vector. "\( \A = \B^{*}\B \)" copies the third, with the star doing what nothing does for numbers but everything does for matrices.

It is not obvious that the three agree, and for a general matrix they do not: they all fail for \( \begin{pmatrix} 0 & 1 \\ 0 & 0\end{pmatrix} \) in different ways. What makes them agree is self-adjointness, and the middle condition is the one to take as the definition, because it is the one that says something about every vector at once.

*A matrix is positive semidefinite when its quadratic form never goes negative.*

::: {#def-positive-semidefinite}
[Positive Semidefinite and Positive Definite]

Let \( \A \in M_n(F) \). Then \( \A \) is **positive semidefinite**, written \( \A \succeq 0 \), if

::: {.enumerate options="label=(P\arabic*)"}
1. \( \A \) is **Hermitian**, that is \( \A^{*} = \A \) (over \( \nR \): symmetric, \( \A\tp = \A \)); and
2. \( \inner{\A\x}{\x} \ge 0 \) for **every** \( \x \in F^n \).
:::

It is **positive definite**, written \( \A \succ 0 \), if (P1) holds and \( \inner{\A\x}{\x} > 0 \) for every **non-zero** \( \x \in F^n \).

The same words apply to an operator \( T \in \cL(V) \) on a finite-dimensional inner product space: \( T \) is positive semidefinite if \( T^{*} = T \) and \( \inner{T\v}{\v} \ge 0 \) for every \( \v \in V \), and positive definite if the inequality is strict for \( \v \ne \0 \).
:::

In words: (P1) puts \( \A \) in the class where the analogy with real numbers is available at all, and (P2) says that the number \( \inner{\A\x}{\x} = \x^{*}\A\x \) is never negative. The word **every** in (P2) is the whole content; a single vector proves nothing. In the definite case the vector \( \x = \0 \) has to be excluded, since \( \inner{\A\0}{\0} = 0 \) for every \( \A \) whatsoever.

Clause (P1) is also what makes clause (P2) meaningful. For a Hermitian \( \A \), the number \( \inner{\A\x}{\x} \) is **real** for every \( \x \), over \( \nC \) as well as over \( \nR \) (@prp-self-adjoint-immediate), so comparing it with \( 0 \) is legitimate. Without (P1) the number can be a genuine complex number, and "\( \ge 0 \)" would be meaningless.

Positive definite implies positive semidefinite, since a condition that holds strictly for \( \x \ne \0 \) holds weakly for \( \x = \0 \) too. The reverse fails, and the smallest witness is \( \diag(1, 0) \).

Before any examples, the trap.

::: {.warning}
**Over \( \nR \), clause (P1) has to be assumed; over \( \nC \) it comes free.** Let \( \A = \begin{pmatrix} 0 & -1 \\ 1 & 0\end{pmatrix} \), the quarter turn of \( \nR^2 \). Then \( \inner{\A\x}{\x} = -x_2x_1 + x_1x_2 = 0 \) for every \( \x \in \nR^2 \), so (P2) holds in the strongest possible way, and yet \( \A\tp = -\A \ne \A \). A real matrix can pass the quadratic-form test and be nowhere near symmetric, because over \( \nR \) the quadratic form cannot see the skew part of a matrix at all (@exr-self-adjoint-operators-c3). So a real definition that dropped (P1) would call the quarter turn positive semidefinite, and none of the theorems below would survive.
:::

Over \( \nC \) the situation is the opposite, and it is worth recording once.

::: {#prp-complex-positivity-forces-hermitian}
[Over \( \nC \), positivity implies Hermitian]

Let \( \A \in M_n(\nC) \) satisfy \( \inner{\A\x}{\x} \in \nR \) for every \( \x \in \nC^n \) — in particular, let \( \inner{\A\x}{\x} \ge 0 \) for every \( \x \). Then \( \A^{*} = \A \).
:::

::: {.proof}
Put \( \S = \A - \A^{*} \). For every \( \x \), moving the star across (@lem-conjugate-transpose-pairing) and using conjugate symmetry,
\[
\inner{\A^{*}\x}{\x} = \inner{\x}{\A\x} = \conj{\inner{\A\x}{\x}} = \inner{\A\x}{\x} ,
\]
the last equality because the number is real. Hence \( \inner{\S\x}{\x} = 0 \) for every \( \x \in \nC^n \), and @thm-complex-zero-test gives \( \S = 0 \).
:::

So over \( \nC \) one may state the definition with (P2) alone; over \( \nR \) one may not. We keep (P1) in the definition for both fields, so that a single sentence covers them and so that no reader has to remember which field licenses which shortcut.

Now the examples, all checked against (P1) and (P2) in turn.

::: {#exm-psd-first-examples}
[Five Positive Matrices]

Decide which of the following are positive semidefinite, and which are positive definite.

::: {.enumerate options="label=(\alph*)"}
1. \( \I_n \), and more generally \( \D = \diag(d_1, \dots, d_n) \) with every \( d_i \) real.
2. \( \x\x^{*} \) for a fixed \( \x \in F^n \).
3. The Gram matrix \( \G \) of a list \( (\v_1, \dots, \v_k) \) in an inner product space.
4. The zero matrix \( 0 \in M_n(F) \).
5. \( \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \).
:::
:::

::: {.solution}
(a) \( \D^{*} = \D \) because the \( d_i \) are real, so (P1) holds. For (P2),
\[
\inner{\D\x}{\x} = \x^{*}\D\x = \sum_{i=1}^{n} d_i \lvert x_i\rvert^2 .
\]
So \( \D \succeq 0 \) exactly when every \( d_i \ge 0 \), and \( \D \succ 0 \) exactly when every \( d_i > 0 \): if some \( d_i < 0 \), the vector \( \e_i \) refutes (P2), and if some \( d_i = 0 \), the vector \( \e_i \) refutes definiteness. In particular \( \I_n \succ 0 \), with \( \inner{\x}{\x} = \norm{\x}^2 \).

(b) \( (\x\x^{*})^{*} = \x^{**}\x^{*} = \x\x^{*} \), so (P1) holds. For (P2), using \( \inner{\u}{\w} = \w^{*}\u \) twice,
\[
\y^{*}(\x\x^{*})\y = (\y^{*}\x)(\x^{*}\y) = \inner{\x}{\y}\,\conj{\inner{\x}{\y}} = \lvert\inner{\x}{\y}\rvert^2 \ge 0 .
\]
So \( \x\x^{*} \succeq 0 \). It is never positive definite for \( n \ge 2 \), since any \( \y \ne \0 \) orthogonal to \( \x \) makes the value \( 0 \); and for \( \x = \0 \) it is the zero matrix.

(c) \( \G^{*} = \G \) by @thm-gram-matrix-properties (a), and \( \x^{*}\G\x = \norm{\sum_j x_j\v_j}^2 \ge 0 \) by part (b) of the same theorem. So \( \G \succeq 0 \) always, and by (c) of that theorem \( \G \succ 0 \) exactly when the list is linearly independent.

(d) \( 0^{*} = 0 \) and \( \inner{0\x}{\x} = 0 \ge 0 \), so \( 0 \succeq 0 \). This is the degenerate case, and it matters: it is the bottom of the order introduced in Section 5, and it shows that (P2) can hold with equality everywhere.

(e) Symmetric, so (P1) holds; but \( \inner{\A\e_2}{\e_2} = -1 < 0 \). Not positive semidefinite. This is (a) with \( d_2 = -1 \).
:::

Example (e) is the non-example by minimal change: keep (P1), change one diagonal entry, and (P2) fails at one standard basis vector. The quarter turn of the warning is the other kind of non-example, keeping (P2) and losing (P1).

Two remarks on the name and the convention. "Definite" is the older word, from the theory of quadratic forms: the form \( q(\x) = \x^{*}\A\x \) has a *definite* sign. "Semi" weakens the sign to allow zeros. Some authors write "positive" for what we call positive semidefinite and "strictly positive" for positive definite; the words differ but the two classes are the same two classes everywhere.

::: {.warning}
**A positive matrix is not a matrix with positive entries.** The all-ones matrix \( \J \in M_2(\nR) \) has every entry positive and is positive semidefinite, but \( \begin{pmatrix} 1 & 2 \\ 2 & 1\end{pmatrix} \) has every entry positive and is **not**: at \( \x = (1, -1) \) its form is \( 1 - 2 - 2 + 1 = -2 \). Conversely \( \diag(1, 1) \) has a zero entry and is positive definite. Entrywise positivity is a different subject, the one Chapter 9 met through stochastic matrices, and it shares only a word with this one.
:::

## Positivity survives a change of variable

Before the equivalences, one small result that will be used in almost every proof of this chapter. The quadratic form \( \x \mapsto \x^{*}\A\x \) is attached to \( \A \); substituting \( \x = \S\y \) turns it into the quadratic form of \( \S^{*}\A\S \). The operation \( \A \mapsto \S^{*}\A\S \) is called **congruence**, and Chapter 14 studies it for its own sake. Here we need only that it preserves the sign.

::: {#prp-congruence-positivity}
[Congruence preserves positivity]

Let \( \A \in M_n(F) \) be Hermitian and \( \S \in M_{n \times m}(F) \). Then \( \S^{*}\A\S \in M_m(F) \) is Hermitian, and:

::: {.enumerate options="label=(\alph*)"}
1. if \( \A \succeq 0 \), then \( \S^{*}\A\S \succeq 0 \);
2. if \( \A \succ 0 \) and \( \nul(\S) = \{\0\} \), then \( \S^{*}\A\S \succ 0 \). In particular, for \( m = n \) and \( \S \) invertible, \( \A \succ 0 \) if and only if \( \S^{*}\A\S \succ 0 \).
:::
:::

::: {.proof}
\( (\S^{*}\A\S)^{*} = \S^{*}\A^{*}\S^{**} = \S^{*}\A\S \), so the matrix is Hermitian. For every \( \y \in F^m \),
\[
\y^{*}(\S^{*}\A\S)\y = (\S\y)^{*}\A(\S\y) = \inner{\A(\S\y)}{\S\y} . \tag{$\ast$}
\]

(a) If \( \A \succeq 0 \), the right-hand side of \( (\ast) \) is \( \ge 0 \) for every \( \y \).

(b) If \( \A \succ 0 \) and \( \nul(\S) = \{\0\} \), then \( \y \ne \0 \) forces \( \S\y \ne \0 \), so the right-hand side of \( (\ast) \) is \( > 0 \). For the last claim, take \( \S \) invertible: one direction is what we just proved, and the other is the same statement applied to \( \S^{-1} \) and the matrix \( \S^{*}\A\S \), since \( (\S^{-1})^{*}(\S^{*}\A\S)\S^{-1} = \A \).
:::

## The equivalent descriptions

The characterization needs one determinant identity, which is worth stating on its own because it also describes every coefficient of a characteristic polynomial. Recall from @def-submatrix-minor that \( \A_{I,I} \) denotes the submatrix of \( \A \) on the rows and columns indexed by \( I \); its determinant is a **principal minor** of \( \A \), and \( \A_{I,I} \) is a **principal submatrix**.

::: {#lem-det-shift-principal-minors}
[Shifting by \( t\I \), minor by minor]

Let \( \A \in M_n(F) \) and \( t \in F \). Then
\[
\det(\A + t\I_n) = \sum_{k=0}^{n} E_k(\A)\, t^{\,n-k},
\]
where \( E_0(\A) = 1 \) and, for \( 1 \le k \le n \), \( E_k(\A) = \sum_{\lvert I\rvert = k} \det \A_{I,I} \) is the sum of all \( k \times k \) principal minors of \( \A \).
:::

::: {.idea}
Column \( j \) of \( \A + t\I \) is \( \a_j + t\e_j \), a sum of two columns, and the determinant is linear in each column separately. Expanding all \( n \) columns turns one determinant into \( 2^n \) of them, one for each choice of which columns contribute their \( t\e_j \). A determinant with \( \e_j \) in column \( j \) collapses under cofactor expansion to the determinant with row \( j \) and column \( j \) deleted, and doing that for every chosen column leaves exactly a principal submatrix.
:::

::: {.proof}
Write \( \a_1, \dots, \a_n \) for the columns of \( \A \), so that column \( j \) of \( \A + t\I \) is \( \a_j + t\e_j \). The determinant is linear in each column with the others fixed (@thm-leibniz-formula-alternating). Applying that in column \( 1 \), then in column \( 2 \), and so on through column \( n \),
\[
\det(\A + t\I) = \sum_{S \subseteq \{1, \dots, n\}} t^{\lvert S\rvert}\det \M_S ,
\]
where \( \M_S \) is the matrix whose \( j \)-th column is \( \e_j \) for \( j \in S \) and \( \a_j \) for \( j \notin S \).

Fix \( S \) and let \( j \in S \). Expanding \( \det \M_S \) along column \( j \) (@thm-laplace-expansion (a)) leaves one term, since that column is \( \e_j \): the entry is \( 1 \) in row \( j \) and \( 0 \) elsewhere, and its cofactor is \( (-1)^{j+j}M_{jj} = M_{jj} \). So \( \det \M_S \) equals the determinant of \( \M_S \) with row \( j \) and column \( j \) deleted, which is a matrix of the same shape on the index set \( \{1, \dots, n\}\setminus\{j\} \). Repeating this for each \( j \in S \) deletes every row and column indexed by \( S \) and leaves
\[
\det \M_S = \det \A_{S^{c}, S^{c}}, \qquad S^{c} = \{1, \dots, n\}\setminus S .
\]
Collecting the subsets by \( k = \lvert S^{c}\rvert \), so that \( \lvert S\rvert = n - k \), gives the stated formula.
:::

::: {.remark}
Running the same expansion over \( F[x] \) with the indeterminate \( -x \) in place of \( t \), and multiplying by \( (-1)^n \), turns this into \( p_{\A}(x) = \sum_k (-1)^k E_k(\A)x^{n-k} \): the coefficients of the characteristic polynomial are, up to sign, the sums of principal minors. The cases \( k = 1 \) and \( k = n \) recover \( \tr \A \) and \( \det \A \) from @thm-charpoly-coefficients.
:::

Here is the main theorem of the section.

::: {#thm-psd-characterizations}
[Characterizations of Positive Semidefiniteness]

Let \( \A \in M_n(F) \) be Hermitian. The following are equivalent.

::: {.enumerate options="label=(\alph*)"}
1. \( \A \succeq 0 \).
2. Every eigenvalue of \( \A \) is a non-negative real number.
3. \( \A = \B^{*}\B \) for some \( \B \in M_n(F) \).
4. \( \A = \C^2 \) for exactly one \( \C \in M_n(F) \) with \( \C \succeq 0 \).
5. Every principal minor of \( \A \) is \( \ge 0 \).
:::
:::

::: {.idea}
The spectral theorem makes (a) and (b) two readings of one diagonal matrix, since an orthonormal change of basis does not change the sign of a quadratic form. From (b) the square root of Chapter 12 produces \( \C \), and \( \C \) is its own \( \B \). The step \( (c) \Rightarrow (a) \) is the identity \( \inner{\B^{*}\B\x}{\x} = \norm{\B\x}^2 \), one line of moving \( \B^{*} \) across. For (e), a principal submatrix is what the form does to vectors supported on a few coordinates, which gives \( (a) \Rightarrow (e) \) at once; the return trip uses @lem-det-shift-principal-minors to show that \( \det(\A + t\I) > 0 \) for every \( t > 0 \), so that no \( -t \) can be an eigenvalue.
:::

::: {.proof}
**(a) \( \Leftrightarrow \) (b).** \( (\Rightarrow) \) Let \( \A\v = \lambda\v \) with \( \v \ne \0 \). By @thm-self-adjoint-real-eigenvalues, \( \lambda \in \nR \), and
\[
0 \le \inner{\A\v}{\v} = \inner{\lambda\v}{\v} = \lambda\norm{\v}^2 ,
\]
so \( \lambda \ge 0 \), as \( \norm{\v}^2 > 0 \). \( (\Leftarrow) \) By @cor-spectral-complex-matrix (over \( \nC \)) or @cor-spectral-real-matrix (over \( \nR \)), \( \A = \U\D\U^{*} \) with \( \U \) unitary and \( \D = \diag(\lambda_1, \dots, \lambda_n) \) the eigenvalues. Put \( \y = \U^{*}\x \). Then
\[
\inner{\A\x}{\x} = \x^{*}\U\D\U^{*}\x = \y^{*}\D\y = \sum_{i} \lambda_i\lvert y_i\rvert^2 \ge 0 ,
\]
every term being a product of two non-negative reals.

**(b) \( \Rightarrow \) (d).** A Hermitian matrix has an orthonormal basis of eigenvectors, so the operator \( T_{\A} \) on \( F^n \) satisfies the hypothesis of @thm-normal-square-root, whose spectral condition \( \spec(T_{\A}) \subseteq [0, \infty) \) is exactly (b). That theorem gives a unique \( \C \) with an orthonormal eigenbasis, non-negative spectrum and \( \C^2 = \A \), and it is self-adjoint; by the equivalence just proved, applied to \( \C \), this says \( \C \succeq 0 \). Conversely any \( \C \succeq 0 \) with \( \C^2 = \A \) is Hermitian with non-negative spectrum, hence is that one. So there is exactly one such \( \C \).

**(d) \( \Rightarrow \) (c).** Take \( \B = \C \); then \( \B^{*}\B = \C^{*}\C = \C^2 = \A \).

**(c) \( \Rightarrow \) (a).** Conjugate-transposing twice, \( (\B^{*}\B)^{*} = \B^{*}(\B^{*})^{*} = \B^{*}\B \), which is (P1). And for every \( \x \),
\[
\inner{\B^{*}\B\x}{\x} = \x^{*}\B^{*}\B\x = (\B\x)^{*}(\B\x) = \norm{\B\x}^2 \ \ge\ 0 ,
\]
which is (P2). Both facts are recorded in operator form in @exr-self-adjoint-operators-c1 (a), applied to the map \( \x \mapsto \B\x \).

**(a) \( \Rightarrow \) (e).** Let \( I = \{i_1 < \dots < i_k\} \). Given \( \y \in F^k \), let \( \x \in F^n \) have \( x_{i_p} = y_p \) and all other entries \( 0 \). Then \( \x^{*}\A\x = \y^{*}\A_{I,I}\y \), because the terms \( \conj{x_i}a_{ij}x_j \) with \( i \notin I \) or \( j \notin I \) vanish. So \( \A_{I,I} \) is Hermitian and satisfies (P2), that is \( \A_{I,I} \succeq 0 \). By the equivalence (a) \( \Leftrightarrow \) (b) applied to \( \A_{I,I} \), all its eigenvalues are \( \ge 0 \). Diagonalizing it as \( \A_{I,I} = \U\D\U^{*} \) as above, with \( \U^{*} = \U^{-1} \), and taking determinants (@thm-det-multiplicative, @cor-det-inverse),
\[
\det \A_{I,I} = \det \D = \lambda_1\cdots\lambda_k \ge 0 .
\]

**(e) \( \Rightarrow \) (b).** Let \( t > 0 \) be real. Every \( E_k(\A) \ge 0 \) by hypothesis and \( E_0(\A) = 1 \), so @lem-det-shift-principal-minors gives
\[
\det(\A + t\I) = \sum_{k=0}^{n} E_k(\A)t^{\,n-k} \ge t^{\,n} > 0 .
\]
In particular \( \A + t\I \) is invertible (@thm-invertible-tfae-det), so \( -t \) is not an eigenvalue of \( \A \) (@thm-invertible-tfae-eigen applied to \( \A + t\I \)). As \( t > 0 \) was arbitrary and every eigenvalue of \( \A \) is real (@thm-self-adjoint-real-eigenvalues), no eigenvalue is negative. This closes the cycle and proves the theorem.
:::

Item (c) is the one to keep in mind: **every positive semidefinite matrix is a Gram matrix**, since \( \B^{*}\B \) is the Gram matrix of the columns of \( \B \) (@def-gram-matrix). Section 3 turns that remark into a theorem. Item (d) names the square root, which Section 2 develops. Item (b) is how one *thinks*; item (e) is, for small matrices, how one *computes*.

## The definite case, and Sylvester's criterion

The definite versions of (a), (b) and (c) are proved by putting "strict" in front of the same arguments. The new item is a test that can be run by hand on a numerical matrix without finding a single eigenvalue.

::: {#thm-pd-characterizations}
[Characterizations of Positive Definiteness, with Sylvester's Criterion]

Let \( \A \in M_n(F) \) be Hermitian, and for \( 1 \le k \le n \) let \( \A_k \) be its leading principal submatrix, the top-left \( k \times k \) corner. The following are equivalent.

::: {.enumerate options="label=(\alph*)"}
1. \( \A \succ 0 \).
2. Every eigenvalue of \( \A \) is a positive real number.
3. \( \A = \B^{*}\B \) for some **invertible** \( \B \in M_n(F) \).
4. **(Sylvester's criterion)** \( \det \A_k > 0 \) for every \( k = 1, \dots, n \).
:::
:::

::: {.idea}
Steps (a) \( \Leftrightarrow \) (b) \( \Leftrightarrow \) (c) repeat the previous proof with strict inequalities. For (a) \( \Rightarrow \) (d), a leading principal submatrix inherits definiteness, and a determinant is a product of eigenvalues. The content is (d) \( \Rightarrow \) (a), and it is an induction on \( n \) that peels off the last row and column. The inductive hypothesis makes the corner \( \A_{n-1} \) definite, hence invertible, and one shear — the congruence by \( \S = \begin{psmallmatrix} \I & -\A_{n-1}^{-1}\b \\ \0\tp & 1\end{psmallmatrix} \), which is exactly the block elimination of Chapter 8 — clears the border and turns \( \A \) into \( \A_{n-1} \oplus (s) \) with one scalar \( s \) left over. Determinants identify the sign of \( s \), and @prp-congruence-positivity carries the verdict back.
:::

::: {.proof}
**(a) \( \Leftrightarrow \) (b).** As in @thm-psd-characterizations, with \( \ge \) replaced by \( > \) throughout: for \( (\Rightarrow) \), \( 0 < \lambda\norm{\v}^2 \) forces \( \lambda > 0 \); for \( (\Leftarrow) \), \( \sum_i\lambda_i\lvert y_i\rvert^2 > 0 \) whenever \( \y = \U^{*}\x \ne \0 \), which happens exactly when \( \x \ne \0 \) because \( \U^{*} \) is invertible.

**(b) \( \Rightarrow \) (c).** Let \( \C \succeq 0 \) with \( \C^2 = \A \) (@thm-psd-characterizations (d)). Since every eigenvalue of \( \A \) is positive, \( 0 \notin \spec(\A) \) and \( \A \) is invertible (@thm-invertible-tfae-eigen). If \( \C\x = \0 \) then \( \A\x = \C^2\x = \0 \), so \( \x = \0 \); hence \( \C \) is invertible too (@thm-invertible-tfae). Take \( \B = \C \).

**(c) \( \Rightarrow \) (a).** For \( \x \ne \0 \), \( \B\x \ne \0 \), so \( \inner{\B^{*}\B\x}{\x} = \norm{\B\x}^2 > 0 \).

**(a) \( \Rightarrow \) (d).** As in the proof of (a) \( \Rightarrow \) (e) of @thm-psd-characterizations with \( I = \{1, \dots, k\} \), the corner \( \A_k \) satisfies \( \y^{*}\A_k\y = \x^{*}\A\x > 0 \) for \( \y \ne \0 \), so \( \A_k \succ 0 \). Its eigenvalues are positive, and \( \det \A_k \) is their product, computed as in the proof of @thm-psd-characterizations, so \( \det \A_k > 0 \).

**(d) \( \Rightarrow \) (a).** Induct on \( n \). For \( n = 1 \), \( \A = (a_{11}) \) with \( a_{11} = \det \A_1 > 0 \), and \( \inner{\A x}{x} = a_{11}\lvert x\rvert^2 > 0 \) for \( x \ne 0 \).

Let \( n \ge 2 \), and write
\[
\A = \begin{pmatrix} \A' & \b \\ \b^{*} & d \end{pmatrix}, \qquad \A' = \A_{n-1},\ \b \in F^{n-1},\ d \in \nR .
\]
The leading principal submatrices of \( \A' \) are \( \A_1, \dots, \A_{n-1} \), so the inductive hypothesis gives \( \A' \succ 0 \); in particular \( \A' \) is invertible, since \( \det \A' = \det \A_{n-1} > 0 \). Put
\[
\S = \begin{pmatrix} \I_{n-1} & -\A'^{-1}\b \\ \0\tp & 1 \end{pmatrix},
\qquad
s = d - \b^{*}\A'^{-1}\b .
\]
Block multiplication (@thm-block-multiplication), together with \( (\A'^{-1})^{*} = \A'^{-1} \) because \( \A' \) is Hermitian, gives
\[
\S^{*}\A\S = \begin{pmatrix} \A' & \0 \\ \0\tp & s \end{pmatrix} . \tag{$\ast$}
\]
Both \( \S \) and \( \S^{*} \) are triangular with \( 1 \)s on the diagonal, so \( \det \S = \det \S^{*} = 1 \) by @thm-det-triangular. Taking determinants in \( (\ast) \) with @thm-det-multiplicative and @thm-det-block-triangular,
\[
0 < \det \A = \det(\S^{*}\A\S) = s\,\det \A' ,
\]
and \( \det \A' > 0 \), so \( s > 0 \). The right-hand side of \( (\ast) \) is therefore positive definite: for \( \y = (\y', y_n) \ne \0 \),
\[
\y^{*}\begin{pmatrix} \A' & \0 \\ \0\tp & s\end{pmatrix}\y = \y'^{*}\A'\y' + s\lvert y_n\rvert^2 > 0 ,
\]
since the two terms are \( \ge 0 \) and not both zero. Finally \( \S \) is invertible, so @prp-congruence-positivity (b) turns \( \S^{*}\A\S \succ 0 \) back into \( \A \succ 0 \). This completes the induction and proves the theorem.
:::

The number \( s = d - \b^{*}\A'^{-1}\b \) in that proof is the Schur complement \( \A/\A' \) of @def-schur-complement, and \( (\ast) \) is the block \( \L\D\U \) factorization of @thm-block-ldu written as a congruence. Section 6 replaces the scalar \( s \) by a block and gets the general test.

::: {.warning}
**For semidefiniteness, the leading principal minors are not enough.** Sylvester's criterion has no "\( \ge \)" version. Take
\[
\A = \begin{pmatrix} 0 & 0 \\ 0 & -1 \end{pmatrix} .
\]
Its leading principal minors are \( \det \A_1 = 0 \) and \( \det \A_2 = 0 \), both \( \ge 0 \), and yet \( \inner{\A\e_2}{\e_2} = -1 \), so \( \A \) is not positive semidefinite. What @thm-psd-characterizations (e) demands is **all** principal minors, and the one this matrix fails is \( \det \A_{\{2\},\{2\}} = -1 < 0 \). The leading corners simply never look at the second coordinate on its own. This is the single most common error about the subject: for the strict test \( n \) minors suffice, for the weak test one needs all \( 2^n - 1 \) of them.
:::

::: {.check}
Is \( \A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} \) positive semidefinite? Is it positive definite? Which minors did you use?
:::

::: {.solution}
It is positive semidefinite but not positive definite. The principal minors are \( 1 \), \( 4 \) and \( \det \A = 4 - 4 = 0 \), all \( \ge 0 \), so @thm-psd-characterizations (e) applies. It is not definite, since \( \det \A_2 = 0 \) violates Sylvester's criterion; concretely \( \A(2, -1) = \0 \), so \( \inner{\A\x}{\x} = 0 \) at the non-zero \( \x = (2, -1) \). One can also see everything at once from \( \A = \b\b\tp \) with \( \b = (1, 2) \), which is @exm-psd-first-examples (b).
:::

## Two by two, and where these matrices come from

The \( 2 \times 2 \) case is worth memorizing, because it is the one that appears inside larger arguments.

::: {#exm-two-by-two-criterion}
[The \( 2 \times 2 \) Test]

Let \( \A = \begin{pmatrix} a & b \\ \conj{b} & d\end{pmatrix} \) be Hermitian, so \( a, d \in \nR \) and \( b \in F \). State and justify the tests for \( \A \succ 0 \) and for \( \A \succeq 0 \).
:::

::: {.solution}
\( \A \succ 0 \) if and only if \( a > 0 \) and \( ad - \lvert b\rvert^2 > 0 \). This is Sylvester's criterion, @thm-pd-characterizations (d): the two leading principal minors are \( a \) and \( \det \A = ad - \lvert b\rvert^2 \).

\( \A \succeq 0 \) if and only if \( a \ge 0 \), \( d \ge 0 \) and \( ad - \lvert b\rvert^2 \ge 0 \). This is @thm-psd-characterizations (e): the principal minors are \( a \), \( d \) and \( \det \A \), and all three are needed. Dropping \( d \ge 0 \) readmits \( \diag(0, -1) \).

Note what the second condition says: \( \lvert b\rvert^2 \le ad \), so an off-diagonal entry can never be larger in modulus than the geometric mean of the two diagonal entries it sits between. For \( \A = \begin{pmatrix} 2 & 1+i \\ 1-i & 3\end{pmatrix} \) over \( \nC \): \( a = 2 > 0 \) and \( ad - \lvert b\rvert^2 = 6 - 2 = 4 > 0 \), so \( \A \succ 0 \).
:::

Where do positive semidefinite matrices come from? Almost always from item (c) of @thm-psd-characterizations, and the standard source is data.

::: {#exm-covariance-style}
[A Covariance-style Matrix]

Three quantities are measured on four occasions, and each column of
\[
\X = \begin{pmatrix} 2 & 1 & 0 \\ -1 & 1 & 1 \\ -1 & -1 & 0 \\ 0 & -1 & -1 \end{pmatrix} \in M_{4\times 3}(\nR)
\]
has been adjusted to sum to \( 0 \). Show that \( \A = \X\tp\X \) is positive definite, and check the verdict against Sylvester's criterion.
:::

::: {.solution}
Multiplying out, \( a_{ij} \) is the dot product of columns \( i \) and \( j \) of \( \X \):
\[
\A = \begin{pmatrix} 6 & 2 & -1 \\ 2 & 4 & 2 \\ -1 & 2 & 2 \end{pmatrix} .
\]
The columns of \( \X \) are linearly independent: if \( \X\x = \0 \), rows \( 1 \) and \( 3 \) read \( 2x_1 + x_2 = 0 \) and \( -x_1 - x_2 = 0 \), which force \( x_1 = x_2 = 0 \), and then row \( 2 \) reads \( x_3 = 0 \). So \( \nul(\X) = \{\0\} \), and taking \( \S = \X \) in @prp-congruence-positivity (b) with the positive definite matrix \( \I_4 \) gives \( \A = \X\tp\I_4\X \succ 0 \). Equivalently, \( \inner{\A\x}{\x} = \norm{\X\x}^2 > 0 \) for \( \x \ne \0 \).

Sylvester's criterion agrees: \( \det \A_1 = 6 \), \( \det \A_2 = 24 - 4 = 20 \), and expanding along the first row,
\[
\det \A = 6(8 - 4) - 2(4 + 2) + (-1)(4 + 4) = 24 - 12 - 8 = 4 ,
\]
all positive. The reason the two routes must agree is that \( \A \) is the Gram matrix of the columns of \( \X \), and @thm-gram-matrix-properties (d) already said that its determinant is positive exactly when those columns are independent.
:::

## The invertible matrix theorem grows

Chapter 2 collected the conditions equivalent to invertibility for an operator (@thm-invertible-operator-tfae); Chapter 3 gave the eight matrix conditions of the Invertible Matrix Theorem (@thm-invertible-tfae); Chapter 7 added the determinant (@thm-invertible-tfae-det) and Chapter 9 the eigenvalue \( 0 \) (@thm-invertible-tfae-eigen). Positivity adds a pair, and they are the ones used whenever a square system is attacked through least squares.

::: {#thm-invertible-tfae-positive}
[Invertible Matrix Theorem, with Positive Definiteness]

Let \( \A \in M_n(F) \) with \( F = \nR \) or \( F = \nC \). The following are equivalent, and each is equivalent to each of the conditions of @thm-invertible-tfae, @thm-invertible-tfae-det and @thm-invertible-tfae-eigen.

::: {.enumerate options="label=(\alph*)"}
1. \( \A \) is invertible.
2. \( \A^{*}\A \succ 0 \).
3. \( \A\A^{*} \succ 0 \).
:::

For a general \( \A \in M_{m \times n}(F) \), one always has \( \A^{*}\A \succeq 0 \), with \( \A^{*}\A \succ 0 \) if and only if the columns of \( \A \) are linearly independent.
:::

::: {.proof}
Let \( \A \in M_{m \times n}(F) \). Then \( \A^{*}\A \) is positive semidefinite by @thm-psd-characterizations ((c) \( \Rightarrow \) (a)). Whether it is definite is decided by the identity \( \inner{\A^{*}\A\x}{\x} = \x^{*}\A^{*}\A\x = \norm{\A\x}^2 \), computed in the proof of @thm-psd-characterizations ((c) \( \Rightarrow \) (a)) and recorded in operator form in @exr-self-adjoint-operators-c1 (a): the left side is \( > 0 \) for every \( \x \ne \0 \) exactly when \( \A\x \ne \0 \) for every \( \x \ne \0 \), that is, exactly when \( \nul(\A) = \{\0\} \), that is, exactly when the columns of \( \A \) are linearly independent. The same conclusion comes from @lem-kernel-normal-equations, which says \( \nul(\A^{*}\A) = \nul(\A) \) and so lets one read the condition off \( \A \) directly.

Now let \( \A \) be square. Then "\( \nul(\A) = \{\0\} \)" is item (b) of @thm-invertible-tfae, which gives (a) \( \Leftrightarrow \) (b). Also \( \A \) is invertible if and only if \( \A^{*} \) is, since \( (\A^{-1})^{*} \) is a two-sided inverse of \( \A^{*} \) and conversely; applying (a) \( \Leftrightarrow \) (b) to \( \A^{*} \) therefore gives (a) \( \Leftrightarrow \) (c).
:::

The two new items look like a detour — why test \( \A^{*}\A \) when \( \A \) itself is available? Because \( \A^{*}\A \) is Hermitian and positive, and everything in this chapter applies to it. Chapter 11 already used it once, in the normal equations of least squares; Section 8 will use it again, to build the singular value decomposition of a matrix that is not even square, and that decomposition supplies the last item of the list: a square matrix is invertible exactly when none of its singular values is zero.

## Exercises

### A. Check your understanding

:::: {#exr-positive-definite-matrices-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the definition of \( \A \succeq 0 \) and of \( \A \succ 0 \), including every quantifier and the field.
2. Explain why clause (P1) cannot be dropped from the real definition, with a concrete matrix.
3. True or false: if \( \A \) is Hermitian and every leading principal minor of \( \A \) is \( \ge 0 \), then \( \A \succeq 0 \). Justify your answer.
4. Write down the three conditions of the \( 2 \times 2 \) test for \( \A \succeq 0 \).
5. Name the item of @thm-psd-characterizations that says every positive semidefinite matrix is a Gram matrix.
:::
::::

::: {.solution}
(a) \( \A \in M_n(F) \) with \( F = \nR \) or \( \nC \) is positive semidefinite if \( \A^{*} = \A \) and \( \inner{\A\x}{\x} \ge 0 \) for **every** \( \x \in F^n \); positive definite if \( \A^{*} = \A \) and \( \inner{\A\x}{\x} > 0 \) for every **non-zero** \( \x \in F^n \) (@def-positive-semidefinite).

(b) Because over \( \nR \) the quadratic form does not see the skew part. The quarter turn \( \begin{pmatrix} 0 & -1 \\ 1 & 0\end{pmatrix} \) has \( \inner{\A\x}{\x} = 0 \) for every \( \x \in \nR^2 \) and is not symmetric.

(c) False. \( \diag(0, -1) \) has leading principal minors \( 0 \) and \( 0 \), and \( \inner{\A\e_2}{\e_2} = -1 \). All principal minors are needed (@thm-psd-characterizations (e)).

(d) With \( \A = \begin{pmatrix} a & b \\ \conj b & d\end{pmatrix} \) Hermitian: \( a \ge 0 \), \( d \ge 0 \) and \( ad - \lvert b\rvert^2 \ge 0 \).

(e) Item (c): \( \A = \B^{*}\B \), and \( \B^{*}\B \) is the Gram matrix of the columns of \( \B \).
:::

### B. Practice

:::: {#exr-positive-definite-matrices-b1}
[B1: Determine the definiteness]

For each matrix below, determine whether it is positive definite, positive semidefinite but not positive definite, or neither. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \begin{pmatrix} 2 & 1 \\ 1 & 2\end{pmatrix} \) over \( \nR \).
2. \( \begin{pmatrix} 0 & 0 \\ 0 & -1\end{pmatrix} \) over \( \nR \).
3. \( \begin{pmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2\end{pmatrix} \) over \( \nR \).
4. The all-ones matrix \( \J \in M_3(\nR) \).
5. \( \begin{pmatrix} 0 & 1 \\ -1 & 0\end{pmatrix} \) over \( \nR \).
6. \( \begin{pmatrix} 2 & 1+i \\ 1-i & 1\end{pmatrix} \) over \( \nC \).
:::
::::

::: {.solution}
(a) Positive definite. Symmetric, with leading principal minors \( 2 \) and \( 4 - 1 = 3 \), both positive (@thm-pd-characterizations (d)).

(b) Neither. The leading principal minors are \( 0 \) and \( 0 \), which tempts one into "semidefinite", but the principal minor \( \det \A_{\{2\},\{2\}} = -1 \) is negative, and \( \inner{\A\e_2}{\e_2} = -1 < 0 \).

(c) Positive definite. Symmetric, with leading principal minors \( 2 \), \( 4 - 1 = 3 \) and \( 2\cdot 3 - (-1)(-2) = 4 \), all positive.

(d) Positive semidefinite, not positive definite. \( \J = \1\1\tp \), which is @exm-psd-first-examples (b) with \( \x = \1 \); so \( \inner{\J\x}{\x} = \lvert\inner{\x}{\1}\rvert^2 \ge 0 \). It vanishes at the non-zero \( \x = (1, -1, 0) \), so it is not definite. (Equivalently, \( \det \J = 0 \).)

(e) Neither: it is not symmetric, so (P1) fails and it is not in the class at all. Its quadratic form is identically \( 0 \), which shows how little the form sees over \( \nR \).

(f) Positive semidefinite, not positive definite. Hermitian, with \( a = 2 \ge 0 \), \( d = 1 \ge 0 \) and \( ad - \lvert b\rvert^2 = 2 - 2 = 0 \). The determinant is \( 0 \), so definiteness fails; indeed \( \A(1+i, -2) = \0 \).
:::

:::: {#exr-positive-definite-matrices-b2}
[B2: A parameter]

For which \( t \in \nR \) is
\[
\A(t) = \begin{pmatrix} 1 & t & 0 \\ t & 2 & t \\ 0 & t & 3 \end{pmatrix}
\]
positive definite? Justify your answer.
::::

::: {.solution}
\( \A(t) \) is symmetric for every real \( t \), so Sylvester's criterion applies (@thm-pd-characterizations (d)). The leading principal minors are
\[
\det \A_1 = 1, \qquad \det \A_2 = 2 - t^2, \qquad \det \A_3 = 6 - 4t^2 ,
\]
the last by expansion along the first row: \( 1\cdot(6 - t^2) - t\cdot(3t - 0) = 6 - 4t^2 \). All three are positive exactly when \( t^2 < 2 \) and \( t^2 < 3/2 \), that is when \( t^2 < 3/2 \). Hence \( \A(t) \succ 0 \) if and only if \( \lvert t\rvert < \sqrt{6}/2 \).

At \( t = \sqrt{6}/2 \) the matrix is positive semidefinite but singular, and for \( \lvert t\rvert > \sqrt{6}/2 \) the determinant is negative, so \( \A(t) \) has an odd number of negative eigenvalues and is not even semidefinite.
:::

:::: {#exr-positive-definite-matrices-b3}
[B3: The inverse of a positive definite matrix]

Let \( \A \in M_n(F) \) with \( \A \succ 0 \). Prove that \( \A \) is invertible and that \( \A^{-1} \succ 0 \).
::::

::: {.solution}
By @thm-pd-characterizations (b), every eigenvalue of \( \A \) is positive, so \( 0 \notin \spec(\A) \) and \( \A \) is invertible (@thm-invertible-tfae-eigen). Then \( (\A^{-1})^{*} = (\A^{*})^{-1} = \A^{-1} \), so \( \A^{-1} \) is Hermitian. Apply @prp-congruence-positivity (b) with \( \S = \A^{-1} \), which is invertible:
\[
\S^{*}\A\S = \A^{-1}\A\A^{-1} = \A^{-1} \succ 0 .
\]
(Alternatively: the eigenvalues of \( \A^{-1} \) are the reciprocals \( 1/\lambda_i \) of those of \( \A \), hence positive, and @thm-pd-characterizations (b) applies again.)
:::

### C. Going deeper

:::: {#exr-positive-definite-matrices-c1}
[C1: Zero trace forces zero]

Let \( \A \in M_n(F) \) with \( \A \succeq 0 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( a_{ii} \ge 0 \) for every \( i \), and that \( \tr \A \ge 0 \).
2. Prove that if \( \tr \A = 0 \) then \( \A = 0 \).
3. Deduce that if \( \A \succeq 0 \) and \( -\A \succeq 0 \), then \( \A = 0 \).
:::
::::

::: {.solution}
(a) \( a_{ii} = \e_i^{*}\A\e_i = \inner{\A\e_i}{\e_i} \ge 0 \) by (P2). Summing, \( \tr \A = \sum_i a_{ii} \ge 0 \).

(b) Write \( \A = \U\D\U^{*} \) with \( \U \) unitary and \( \D = \diag(\lambda_1, \dots, \lambda_n) \) the eigenvalues (@cor-spectral-complex-matrix, @cor-spectral-real-matrix). Then \( \tr \A = \tr(\D\U^{*}\U) = \tr \D = \sum_i\lambda_i \) by @thm-trace-properties, and each \( \lambda_i \ge 0 \) by @thm-psd-characterizations (b). A sum of non-negative reals is \( 0 \) only if every term is \( 0 \), so \( \D = 0 \) and hence \( \A = 0 \).

Alternatively, without eigenvalues: by (a) each \( a_{ii} \ge 0 \), so \( \tr \A = 0 \) forces every \( a_{ii} = 0 \). Writing \( \A = \B^{*}\B \) (@thm-psd-characterizations (c)), the \( i \)-th diagonal entry is \( \norm{\b_i}^2 \) for the \( i \)-th column \( \b_i \) of \( \B \); so every column of \( \B \) is \( \0 \), that is \( \B = 0 \) and \( \A = 0 \).

(c) If both \( \A \succeq 0 \) and \( -\A \succeq 0 \), then by (a) \( \tr \A \ge 0 \) and \( \tr(-\A) = -\tr \A \ge 0 \), so \( \tr \A = 0 \) and (b) gives \( \A = 0 \).
:::

:::: {#exr-positive-definite-matrices-c2}
[C2: The cone of positive matrices]

Let \( \cP_n \subseteq M_n(F) \) be the set of positive semidefinite matrices.

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( \A, \B \in \cP_n \) and \( c \ge 0 \) is real, then \( \A + \B \in \cP_n \) and \( c\A \in \cP_n \). (A set with these two properties is a **convex cone**: it contains \( (1-t)\A + t\B \) for \( 0 \le t \le 1 \) as well.)
2. Prove that \( \cP_n \) contains no line through \( 0 \): if \( \A \in \cP_n \) and \( -\A \in \cP_n \) then \( \A = 0 \).
3. Prove that \( \cP_n \) is closed under congruence: if \( \A \in \cP_n \) and \( \S \in M_n(F) \), then \( \S^{*}\A\S \in \cP_n \). Give an example showing that \( \cP_n \) is **not** closed under multiplication.
:::

*Hint for (c): for the example, two positive semidefinite matrices whose product is not even Hermitian will do.*
::::

::: {.solution}
(a) Sums and real multiples of Hermitian matrices are Hermitian. For every \( \x \),
\[
\inner{(\A + \B)\x}{\x} = \inner{\A\x}{\x} + \inner{\B\x}{\x} \ge 0 ,
\]
and \( \inner{c\A\x}{\x} = c\inner{\A\x}{\x} \ge 0 \) since \( c \ge 0 \). Convexity follows by taking \( c = 1 - t \) and \( c = t \) and adding.

(b) This is @exr-positive-definite-matrices-c1 (c).

(c) Immediate from @prp-congruence-positivity (a). For the failure of multiplicativity, take
\[
\A = \begin{pmatrix} 1 & 0 \\ 0 & 0\end{pmatrix}, \qquad \B = \begin{pmatrix} 1 & 1 \\ 1 & 1\end{pmatrix} ,
\]
both positive semidefinite (\( \A = \e_1\e_1\tp \) and \( \B = \1\1\tp \)). Then
\[
\A\B = \begin{pmatrix} 1 & 1 \\ 0 & 0\end{pmatrix} ,
\]
which is not symmetric, so it is not positive semidefinite — it fails (P1), never mind (P2). Section 2 shows what does survive: \( \tr(\A\B) \ge 0 \), and \( \A\B \succeq 0 \) whenever \( \A \) and \( \B \) commute.
:::

:::: {#exr-positive-definite-matrices-c3}
[C3: The largest entry sits on the diagonal]

Let \( \A \in M_n(F) \) with \( \A \succeq 0 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \lvert a_{ij}\rvert^2 \le a_{ii}a_{jj} \) for all \( i, j \).
2. Deduce that if \( a_{ii} = 0 \) for some \( i \), then the whole \( i \)-th row and \( i \)-th column of \( \A \) are zero.
3. Deduce that \( \max_{i,j}\lvert a_{ij}\rvert = \max_i a_{ii} \).
:::

*Hint for (a): look at a \( 2 \times 2 \) principal submatrix.*
::::

::: {.solution}
(a) For \( i = j \) the claim is \( a_{ii}^2 \le a_{ii}^2 \). For \( i \ne j \), take \( I = \{i, j\} \). By the proof of @thm-psd-characterizations ((a) \( \Rightarrow \) (e)), \( \A_{I,I} \succeq 0 \), and @exm-two-by-two-criterion gives \( a_{ii}a_{jj} - \lvert a_{ij}\rvert^2 = \det \A_{I,I} \ge 0 \).

(b) If \( a_{ii} = 0 \), then (a) gives \( \lvert a_{ij}\rvert^2 \le 0 \cdot a_{jj} = 0 \) for every \( j \), so \( a_{ij} = 0 \); and \( a_{ji} = \conj{a_{ij}} = 0 \) since \( \A \) is Hermitian.

(c) Let \( M = \max_i a_{ii} \), a maximum of non-negative reals by @exr-positive-definite-matrices-c1 (a). By (a), \( \lvert a_{ij}\rvert \le \sqrt{a_{ii}a_{jj}} \le M \) for all \( i, j \), so \( \max_{i,j}\lvert a_{ij}\rvert \le M \). The reverse inequality holds because the diagonal entries are among the entries. Hence the two maxima are equal.
:::
