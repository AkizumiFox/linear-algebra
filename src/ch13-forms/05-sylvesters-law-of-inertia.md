# Sylvester's Law of Inertia

The previous section produced a diagonal matrix and then took it away again: the diagonal entries are not invariants, because rescaling the \( i \)-th basis vector by \( t \) multiplies the \( i \)-th entry by \( t^2 \). Over \( \nR \) the squares are exactly the positive numbers, so rescaling can change the size of an entry but never its sign. This section proves that the signs are all that survives, and that they survive completely: the number of positive, negative and zero entries is the same for every diagonalization. That is the classification of real symmetric matrices up to congruence, and it is also the missing link between congruence and the spectral theorem.

**Throughout this section the field is \( \nR \).** Every form is a symmetric bilinear form on a finite-dimensional real vector space \( V \), and every matrix is a real symmetric matrix. The words "positive" and "negative" have no meaning over a general field, and almost nothing in this section survives the move to one; @cor-complex-symmetric-classification already showed that over \( \nC \) the answer is different, since rank alone classifies there.

## Normalizing the diagonal

Start from @thm-symmetric-form-diagonalizable, which applies because \( \operatorname{char}\nR = 0 \). It gives an orthogonal basis \( (\v_1, \dots, \v_n) \) for \( \beta \), with \( q(\v_i) = d_i \). Over \( \nR \) we may go one step further and scale.

By @prp-diagonal-entries-square-classes, replacing \( \v_i \) by \( t_i\v_i \) replaces \( d_i \) by \( t_i^2d_i \). Choosing \( t_i = 1/\sqrt{\lvert d_i\rvert} \) when \( d_i \ne 0 \), and \( t_i = 1 \) when \( d_i = 0 \), turns every diagonal entry into \( 1 \), \( -1 \) or \( 0 \). A permutation of the basis then sorts them, so after a further congruence by a permutation matrix the matrix of \( \beta \) is

\[
\I_{n_+} \oplus (-\I_{n_-}) \oplus \0_{n_0},
\]{#eq-real-canonical-form}

where \( n_+ \) counts the positive \( d_i \), \( n_- \) the negative ones and \( n_0 \) the zeros, and \( n_+ + n_- + n_0 = n \). Nothing yet says that these three counts do not depend on the orthogonal basis we started from. That is the theorem.

::: {.check}
One of the three counts is already known to be an invariant, by a result of Section 2. Which one, and why?
:::

::: {.solution}
The count \( n_0 \). A diagonal matrix has rank equal to its number of non-zero entries, so \( n_+ + n_- = \rank\mtx{\beta}{\sB}{} \), and congruence preserves rank (@thm-congruence-preserves-rank). Hence \( n_+ + n_- \) is the same for every orthogonal basis, and so is \( n_0 = n - (n_+ + n_-) \). What is **not** yet known is how that total splits into positives and negatives — which is exactly the work left for the theorem below.
:::

## The law of inertia

::: {#thm-sylvester-inertia}
[Sylvester's Law of Inertia]

Let \( \beta \) be a symmetric bilinear form on a real vector space \( V \) with \( \dim V = n \), and let \( \sB \) and \( \sB' \) be two orthogonal bases for \( \beta \). Let \( (n_+, n_-, n_0) \) be the numbers of positive, negative and zero diagonal entries of \( \mtx{\beta}{\sB}{} \), and \( (n_+', n_-', n_0') \) the corresponding numbers for \( \mtx{\beta}{\sB'}{} \). Then
\[
n_+ = n_+', \qquad n_- = n_-', \qquad n_0 = n_0' .
\]
:::

::: {.idea}
Rank has already delivered \( n_+ + n_- = n_+' + n_-' \), so it is enough to prove \( n_+ = n_+' \), and for that we may suppose \( n_+ > n_+' \) and look for a disaster. The two bases carve out two subspaces with incompatible behavior: on \( U = \Span(\v_1, \dots, \v_{n_+}) \) the form is **strictly positive** away from \( \0 \), because @eq-diagonal-quadratic-form has only positive coefficients there; on \( U' = \Span(\v_{n_+'+1}', \dots, \v_n') \) it is \( \le 0 \) everywhere, because there the coefficients are all \( \le 0 \). A non-zero vector in both would have \( q(\v) > 0 \) and \( q(\v) \le 0 \) at once, so the two subspaces meet only in \( \0 \). But their dimensions add up to more than \( n \), and two such subspaces of an \( n \)-dimensional space cannot meet only in \( \0 \). Contradiction plus a dimension count.
:::

::: {.proof}
Write \( \sB = (\v_1, \dots, \v_n) \) and \( \sB' = (\v_1', \dots, \v_n') \), and order each so that the positive entries come first, then the negative ones, then the zeros; reordering a basis does not change the three counts. Put \( d_i = q(\v_i) \) and \( d_j' = q(\v_j') \), so that
\[
d_1, \dots, d_{n_+} > 0, \qquad d_{n_+'+1}', \dots, d_n' \le 0 .
\]

As in the Quick check, \( n_+ + n_- = \rank\mtx{\beta}{\sB}{} = \rank\mtx{\beta}{\sB'}{} = n_+' + n_-' \) by @thm-congruence-preserves-rank, and \( n_0 = n - (n_+ + n_-) \). So it suffices to prove \( n_+ = n_+' \); the other two equalities then follow.

Suppose not. Swapping the names of the two bases if necessary, we may assume \( n_+ > n_+' \). Put
\[
U = \Span(\v_1, \dots, \v_{n_+}), \qquad
U' = \Span(\v_{n_+'+1}', \dots, \v_n') ,
\]
so that \( \dim U = n_+ \) and \( \dim U' = n - n_+' \).

*Claim: \( U \cap U' = \{\0\} \).* Let \( \v \in U \cap U' \) with \( \v \ne \0 \). Writing \( \v = \sum_{i \le n_+} c_i\v_i \) and using @eq-diagonal-quadratic-form for the basis \( \sB \), whose later coordinates of \( \v \) are zero,
\[
q(\v) = \sum_{i=1}^{n_+} d_i c_i^2 > 0 ,
\]
because every \( d_i \) with \( i \le n_+ \) is positive, every \( c_i^2 \ge 0 \), and at least one \( c_i \ne 0 \) since \( \v \ne \0 \). Writing instead \( \v = \sum_{j > n_+'} b_j\v_j' \) and using @eq-diagonal-quadratic-form for \( \sB' \),
\[
q(\v) = \sum_{j = n_+'+1}^{n} d_j' b_j^2 \le 0 ,
\]
because every \( d_j' \) with \( j > n_+' \) is \( \le 0 \) and every \( b_j^2 \ge 0 \). A real number cannot be both \( > 0 \) and \( \le 0 \), so no such \( \v \) exists, which proves the claim.

On the other hand, \( U + U' \) is a subspace of \( V \), so \( \dim(U + U') \le n \), and the dimension formula (@thm-dimension-formula-subspace-dim) gives
\[
\begin{aligned}
\dim(U \cap U') &= \dim U + \dim U' - \dim(U + U') \\
&\ge n_+ + (n - n_+') - n \\
&= n_+ - n_+' > 0 .
\end{aligned}
\]
So \( U \cap U' \) contains a non-zero vector, contradicting the claim. Therefore \( n_+ = n_+' \), and with it \( n_- = n_-' \) and \( n_0 = n_0' \). This proves the theorem.
:::

The name comes from mechanics, where the form is an inertia tensor and the theorem says that a change of coordinates cannot turn a direction of positive inertia into one of negative inertia. The invariant has a name of its own.

::: {#def-signature}
[Inertia and Signature]

Let \( \beta \) be a symmetric bilinear form on a real vector space \( V \) of dimension \( n \), diagonalized in some orthogonal basis. The triple
\[
(n_+, n_-, n_0)
\]
of numbers of positive, negative and zero diagonal entries is the **inertia** of \( \beta \), and it is well defined by @thm-sylvester-inertia. The pair \( (n_+, n_-) \) is the **signature** of \( \beta \), and \( n_+ + n_- = \rank\beta \) while \( n_0 = n - \rank\beta \). The same words are used for a real symmetric matrix \( \A \), through the form \( \beta(\x,\y) = \x\tp\A\y \), and we write \( n_+(\A) \), \( n_-(\A) \), \( n_0(\A) \).
:::

Two conventions are in circulation and both are called the signature: the pair \( (n_+, n_-) \), used here, and the single integer \( n_+ - n_- \). They carry the same information once the rank is known, and the difference is only ever notational; where a source writes "signature \( 2 \)" it means \( n_+ - n_- = 2 \). The triple \( (n_+, n_-, n_0) \) is the safest thing to quote, since it also records the degeneracy.

## The classification over the reals

::: {#cor-real-symmetric-classification}
[Classification of Real Symmetric Matrices by Signature]

Let \( \A, \B \in M_n(\nR) \) be symmetric. Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \A \) is congruent to \( \I_{n_+} \oplus (-\I_{n_-}) \oplus \0_{n_0} \), where \( (n_+, n_-, n_0) \) is the inertia of \( \A \), and to no other matrix of this shape;
2. \( \A \simeq \B \) if and only if \( \A \) and \( \B \) have the same inertia;
3. the number of congruence classes of symmetric matrices in \( M_n(\nR) \) is \( \tfrac12(n+1)(n+2) \).
:::
:::

::: {.proof}
(a) The congruence to \( \I_{n_+} \oplus (-\I_{n_-}) \oplus \0_{n_0} \) is @eq-real-canonical-form, obtained from @thm-symmetric-form-diagonalizable followed by the scaling and sorting described above. That matrix is itself diagonal with inertia \( (n_+, n_-, n_0) \), so by @thm-sylvester-inertia no matrix of the same shape with a different triple can be congruent to \( \A \).

(b) \( (\Rightarrow) \) A congruence \( \B = \P\tp\A\P \) with \( \P \) invertible is a change of basis for the form (@thm-change-of-basis-form), so an orthogonal basis diagonalizing \( \B \) yields one diagonalizing \( \A \) with the same diagonal, and @thm-sylvester-inertia makes the inertia equal.

\( (\Leftarrow) \) If \( \A \) and \( \B \) have the same inertia, each is congruent to the same matrix \( \I_{n_+} \oplus (-\I_{n_-}) \oplus \0_{n_0} \) by (a), hence to each other, since congruence is an equivalence relation (@prp-congruence-equivalence).

(c) By (b) the classes correspond to the triples \( (n_+, n_-, n_0) \) of non-negative integers summing to \( n \), equivalently to the pairs \( (n_+, n_-) \) with \( n_+ + n_- \le n \). For each value \( k = n_+ + n_- \in \{0, 1, \dots, n\} \) there are \( k + 1 \) choices of \( n_+ \), so the total is \( 1 + 2 + \dots + (n+1) = \tfrac12(n+1)(n+2) \). This proves the corollary.
:::

So congruence over \( \nR \) has a complete and finite list of invariants, in sharp contrast to similarity, where even \( 2 \times 2 \) real symmetric matrices fall into infinitely many classes (one for each unordered pair of eigenvalues). Congruence forgets a great deal; the point of the law of inertia is that what it forgets is precisely everything except the signs.

## Reconciling congruence with the spectral theorem

Chapter 11 diagonalized a real symmetric matrix a different way, by an **orthogonal** \( \Q \), and got the eigenvalues on the diagonal. Chapter 11 also pointed out why that theorem is special: because \( \Q\tp = \Q^{-1} \), the one equation \( \Q\tp\A\Q = \D \) can be read twice, and "an orthogonal change of variables is a similarity *and* a congruence, so it keeps the eigenvalues and the geometry at once". Reading the same equation twice is all that is needed to identify the inertia.

::: {#thm-inertia-from-eigenvalues}
[Inertia Is the Sign Pattern of the Spectrum]

Let \( \A \in M_n(\nR) \) be symmetric. Then \( n_+(\A) \) is the number of positive eigenvalues of \( \A \), counted with multiplicity, \( n_-(\A) \) the number of negative ones, and \( n_0(\A) \) the multiplicity of \( 0 \).
:::

::: {.proof}
By @cor-spectral-real-matrix there is an orthogonal \( \Q \in \Orth(n) \) and a real diagonal \( \D = \diag(\lambda_1, \dots, \lambda_n) \) with \( \A = \Q\D\Q\tp \), where \( \lambda_1, \dots, \lambda_n \) is the eigenvalue list of \( \A \) with multiplicity. Equivalently \( \D = \Q\tp\A\Q \).

Read as a **similarity**: \( \Q\tp = \Q^{-1} \), so \( \D = \Q^{-1}\A\Q \) and the diagonal entries of \( \D \) are the eigenvalues of \( \A \).

Read as a **congruence**: \( \Q \) is invertible, so \( \D = \Q\tp\A\Q \) exhibits \( \D \) as congruent to \( \A \) (@def-congruent). Being diagonal, \( \D \) is the matrix of the form of \( \A \) in an orthogonal basis, namely the columns of \( \Q \). By @thm-sylvester-inertia its numbers of positive, negative and zero entries are the inertia of \( \A \).

The same list of numbers is being counted both times, so the counts agree. This proves the theorem.
:::

This is what Chapter 12 promised when, having diagonalized a pencil and found \( \S\tp\B\S = \diag(-1, 3) \) while the eigenvalues of \( \B \) were \( 3 \pm 3\sqrt2 \), it observed that the signs \( (-, +) \) "match the signs of the eigenvalues of \( \B \) itself" and said that Chapter 13 would show this is no coincidence. It is not: the congruence \( \S\tp\B\S \) has the inertia of \( \B \) by @thm-sylvester-inertia, and that inertia is the sign pattern of the spectrum by @thm-inertia-from-eigenvalues. Here \( 3 + 3\sqrt2 > 0 \) and \( 3 - 3\sqrt2 < 0 \) — since \( 3\sqrt2 > 4 \) — so the inertia of \( \B \) is \( (1, 1, 0) \), and any congruent diagonal matrix must show exactly one positive and one negative entry, as \( \diag(-1,3) \) does.

The same reading settles the definiteness tests of Chapter 12 in one line: \( \A \succ 0 \) means \( \x\tp\A\x > 0 \) for all \( \x \ne \0 \), which by @thm-pd-characterizations is the statement that every eigenvalue is positive, which by @thm-inertia-from-eigenvalues is the statement that the inertia is \( (n, 0, 0) \). Section 6 takes that dictionary further.

::: {.warning}
**Congruent matrices have the same inertia and unrelated eigenvalues.** Take \( \A = \diag(1, -1) \) and \( \P = \diag(2, 3) \). Then
\[
\P\tp\A\P = \diag(4, -9),
\]
so \( \A \simeq \diag(4,-9) \), yet the eigenvalues have moved from \( 1, -1 \) to \( 4, -9 \). Nothing about their sizes, their ratios, their sum or their product is preserved — \( \tr \) goes from \( 0 \) to \( -5 \), \( \det \) from \( -1 \) to \( -36 \) — and only the pattern \( (+, -) \) survives. For a second witness with no scaling in sight, \( \I_2 \) is congruent to \( \S\tp\S = \begin{psmallmatrix} 1 & 1 \\ 1 & 2\end{psmallmatrix} \) with \( \S = \begin{psmallmatrix} 1 & 1 \\ 0 & 1\end{psmallmatrix} \); the eigenvalues change from \( 1, 1 \) to \( (3 \pm \sqrt5)/2 \), and the inertia stays \( (2,0,0) \).
:::

## Computing a signature

@thm-inertia-from-eigenvalues gives a method — find the eigenvalues and count signs — but it is the expensive one, since it needs the roots of a degree-\( n \) polynomial. The cheap method is the algorithm of the previous section, which needs only arithmetic: diagonalize by paired row and column operations and read off the signs. The eigenvalues are never computed and never needed.

::: {#exm-inertia-by-elimination}
[A signature by symmetric elimination]

Find the inertia of
\[
\A = \begin{pmatrix} 1 & 1 & 2 \\ 1 & 2 & 3 \\ 2 & 3 & 1 \end{pmatrix},
\]
and say whether the form \( q(\x) = \x\tp\A\x \) is positive definite.
:::

::: {.solution}
The corner entry is \( 1 \), so no repair move is needed.

*Clear the first row and column.* Subtract row \( 1 \) from row \( 2 \) and \( 2\times \) row \( 1 \) from row \( 3 \), then do the same two operations on columns:
\[
\begin{pmatrix} 1 & 1 & 2 \\ 0 & 1 & 1 \\ 0 & 1 & -3 \end{pmatrix}
\ \longrightarrow\
\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 1 & -3 \end{pmatrix}.
\]

*Clear the second row and column.* The pivot is \( 1 \) and \( a_{23} = 1 \), so subtract row \( 2 \) from row \( 3 \) and then column \( 2 \) from column \( 3 \):
\[
\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & -4 \end{pmatrix}
\ \longrightarrow\
\diag(1, 1, -4).
\]

So the inertia is \( (2, 1, 0) \) and the signature is \( (2,1) \). The form is **not** positive definite: it is negative at the third basis vector of the new basis, namely the third column of
\[
\P = \begin{pmatrix} 1 & -1 & -1 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{pmatrix},
\]
which is \( \p_3 = (-1,-1,1) \). Checking directly, \( \A\p_3 = (0, 0, -4) \) and \( \p_3 \cdot (0,0,-4) = -4 < 0 \).

The eigenvalue route would have to factor \( \det(x\I - \A) = x^3 - 4x^2 - 9x + 4 \), whose roots are irrational; the elimination never met them. As a partial check on the arithmetic, \( \det\A = -4 \) and \( \det\diag(1,1,-4) = -4 \), consistent with \( \det\P = 1 \).
:::

Over \( \nR \), then, a symmetric matrix carries exactly two pieces of congruence data, and both are cheap: its rank and how that rank splits into positive and negative directions. The next section reads the same two numbers as a statement about definiteness, and uses them to decide maxima and minima.

## Exercises

### A. Check your understanding

:::: {#exr-sylvesters-law-of-inertia-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the **inertia** and the **signature** of a real symmetric matrix.
2. State @thm-sylvester-inertia, with all hypotheses.
3. Which part of the inertia is already an invariant before the law of inertia is proved, and by which earlier result?
4. Determine whether the following statement is correct, and justify your answer: congruent real symmetric matrices have the same trace.
5. Explain in one sentence why an orthogonal change of basis lets the spectral theorem compute an inertia.
:::
::::

::: {.solution}
(a) Diagonalize the associated form in an orthogonal basis. The inertia is the triple \( (n_+, n_-, n_0) \) of numbers of positive, negative and zero diagonal entries, and the signature is the pair \( (n_+, n_-) \).

(b) If \( \beta \) is a symmetric bilinear form on a finite-dimensional real vector space and \( \sB, \sB' \) are two orthogonal bases for \( \beta \), then the two matrices \( \mtx{\beta}{\sB}{} \) and \( \mtx{\beta}{\sB'}{} \) have the same numbers of positive, negative and zero diagonal entries.

(c) The count \( n_0 \), equivalently the sum \( n_+ + n_- \), because that sum is the rank and congruence preserves rank (@thm-congruence-preserves-rank).

(d) Incorrect. \( \diag(1,-1) \) and \( \diag(4,-9) \) are congruent, by the congruence with \( \P = \diag(2,3) \), and their traces are \( 0 \) and \( -5 \). Trace is a similarity invariant (@thm-trace-similarity-invariant), not a congruence invariant.

(e) For an orthogonal \( \Q \) we have \( \Q\tp = \Q^{-1} \), so the single equation \( \Q\tp\A\Q = \D \) is simultaneously a similarity, which puts the eigenvalues on the diagonal, and a congruence, which makes that diagonal compute the inertia.
:::

### B. Practice

:::: {#exr-sylvesters-law-of-inertia-b1}
[B1: Signatures by elimination]

Find the inertia of each of the following real symmetric matrices by paired row and column operations. Do not compute any eigenvalues.

::: {.enumerate options="label=(\alph*)"}
1. \( \A = \begin{pmatrix} 1 & 2 & 0 \\ 2 & 1 & 3 \\ 0 & 3 & 1 \end{pmatrix} \).
2. \( \B = \begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix} \).
3. \( \C = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} \).
:::
::::

::: {.solution}
(a) By @exr-diagonalizing-symmetric-forms-b1, \( \A \) is congruent to \( \diag(1,-3,4) \). Inertia \( (2,1,0) \).

(b) By @exm-symmetric-elimination-3x3, \( \B \) is congruent to \( \diag(2,-2,-2) \). Inertia \( (1,2,0) \).

(c) Subtract \( 2\times \) row \( 1 \) from row \( 2 \), then \( 2\times \) column \( 1 \) from column \( 2 \):
\[
\begin{pmatrix} 1 & 2 \\ 0 & 0 \end{pmatrix}
\ \longrightarrow\
\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}.
\]
Inertia \( (1,0,1) \): the form \( q(\x) = (x_1 + 2x_2)^2 \) is degenerate, vanishing on the line \( x_1 = -2x_2 \).
:::

:::: {#exr-sylvesters-law-of-inertia-b2}
[B2: Which of these are congruent?]

Sort the following real symmetric matrices into congruence classes, justifying each answer.
\[
\A_1 = \diag(1, 1, -1), \quad
\A_2 = \diag(5, 2, -7), \quad
\A_3 = \diag(1, -1, -1),
\]
\[
\A_4 = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix},
\qquad
\A_5 = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & -3 \end{pmatrix}.
\]
::::

::: {.solution}
Compute each inertia and apply @cor-real-symmetric-classification (b).

\( \A_1 \): \( (2,1,0) \). \( \A_2 \): \( (2,1,0) \). \( \A_3 \): \( (1,2,0) \). \( \A_5 \): \( (1,1,1) \).

For \( \A_4 \), the top-left \( 2\times2 \) block is the form \( 2x_1x_2 \), which @exr-diagonalizing-symmetric-forms-b2 diagonalizes to \( \diag(2,-2) \); so \( \A_4 \) is congruent to \( \diag(2,-2,1) \), with inertia \( (2,1,0) \).

Therefore the classes are \( \{\A_1, \A_2, \A_4\} \), \( \{\A_3\} \) and \( \{\A_5\} \). Note that \( \A_1 \) and \( \A_3 \) have the same rank and are still not congruent, so rank alone does not classify over \( \nR \) — unlike over \( \nC \) (@cor-complex-symmetric-classification).
:::

:::: {#exr-sylvesters-law-of-inertia-b3}
[B3: Inertia from a characteristic polynomial]

Let \( \A \in M_3(\nR) \) be symmetric with \( \det(x\I - \A) = x^3 - 2x^2 - 5x + 6 \).

::: {.enumerate options="label=(\alph*)"}
1. Find the inertia of \( \A \).
2. Is \( \A \) congruent to \( \diag(1, 1, -1) \)? Is it similar to it?
:::
::::

::: {.solution}
(a) The polynomial factors as \( (x-1)(x+2)(x-3) \), since \( 1 \) is a root and dividing gives \( x^2 - x - 6 \). The eigenvalues are \( 1, 3, -2 \), so by @thm-inertia-from-eigenvalues the inertia is \( (2, 1, 0) \).

(b) Congruent: yes, since \( \diag(1,1,-1) \) also has inertia \( (2,1,0) \) and @cor-real-symmetric-classification (b) applies. Similar: no, because similar matrices have equal characteristic polynomials, and \( \diag(1,1,-1) \) has \( (x-1)^2(x+1) \ne (x-1)(x-3)(x+2) \).
:::

### C. Going deeper

:::: {#exr-sylvesters-law-of-inertia-c1}
[C1: An intrinsic description of \( n_+ \)]

Let \( \beta \) be a symmetric bilinear form on a real vector space \( V \) of dimension \( n \), with quadratic form \( q \). Call a subspace \( U \subseteq V \) **positive** if \( q(\v) > 0 \) for every \( \v \in U \) with \( \v \ne \0 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( n_+ \) is the largest dimension of a positive subspace of \( V \).
2. Deduce @thm-sylvester-inertia again from (a), in two lines.
3. State and prove the corresponding description of \( n_- \).
:::

*Hint: for (a), use an orthogonal basis to produce one positive subspace of dimension \( n_+ \), and the dimension formula to rule out a larger one.*
::::

::: {.solution}
(a) Fix an orthogonal basis \( (\v_1, \dots, \v_n) \) ordered so that \( d_1, \dots, d_{n_+} > 0 \) and \( d_j \le 0 \) for \( j > n_+ \).

*A positive subspace of dimension \( n_+ \).* Put \( U = \Span(\v_1, \dots, \v_{n_+}) \). For \( \v = \sum_{i \le n_+} c_i\v_i \) non-zero, @eq-diagonal-quadratic-form gives \( q(\v) = \sum_{i \le n_+} d_ic_i^2 > 0 \), since all \( d_i > 0 \) and some \( c_i \ne 0 \). So \( U \) is positive and \( \dim U = n_+ \).

*No larger one.* Let \( X \) be positive with \( \dim X = k \), and put \( W = \Span(\v_{n_++1}, \dots, \v_n) \), of dimension \( n - n_+ \). Every \( \w \in W \) has \( q(\w) = \sum_{j > n_+} d_jc_j^2 \le 0 \). If \( k > n_+ \) then by @thm-dimension-formula-subspace-dim,
\[
\dim(X \cap W) \ge k + (n - n_+) - n = k - n_+ > 0,
\]
so there is a non-zero \( \v \in X \cap W \) with \( q(\v) > 0 \) and \( q(\v) \le 0 \), which is impossible. Hence \( k \le n_+ \), and the maximum is \( n_+ \).

(b) The right-hand side of (a) — the largest dimension of a positive subspace — is defined from \( \beta \) alone and mentions no basis. So the number \( n_+ \) computed from any orthogonal basis equals that basis-free quantity, hence is the same for all of them. Then \( n_+ + n_- = \rank\beta \) is basis-free too (@thm-congruence-preserves-rank), so \( n_- \) and \( n_0 \) are determined as well.

(c) \( n_- \) is the largest dimension of a **negative** subspace, one on which \( q(\v) < 0 \) for every \( \v \ne \0 \). Apply (a) to the form \( -\beta \), whose diagonal entries in any orthogonal basis are the negatives of those of \( \beta \), so that \( n_+(-\beta) = n_-(\beta) \), and whose positive subspaces are exactly the negative subspaces of \( \beta \).
:::

:::: {#exr-sylvesters-law-of-inertia-c2}
[C2: Congruence cannot be read off the eigenvalues, and inertia can]

::: {.enumerate options="label=(\alph*)"}
1. Give two real symmetric \( 2\times2 \) matrices that are congruent but have no eigenvalue in common.
2. Prove that if \( \A \) and \( \B \) are real symmetric and **similar**, then they are congruent.
3. Give two real symmetric \( 2\times2 \) matrices that are congruent but not similar, so that the converse of (b) fails.
:::
::::

::: {.solution}
(a) \( \diag(1,-1) \) and \( \diag(4,-9) \), congruent by \( \P = \diag(2,3) \). Their spectra are \( \{1,-1\} \) and \( \{4,-9\} \), which are disjoint.

(b) Similar matrices have the same characteristic polynomial (@thm-charpoly-similarity-invariant), hence the same eigenvalues with multiplicity. By @thm-inertia-from-eigenvalues they then have the same inertia, and by @cor-real-symmetric-classification (b) they are congruent. (Alternatively and more directly: by @cor-spectral-real-matrix each is orthogonally congruent to the diagonal matrix of its eigenvalues, and those diagonal matrices agree up to a permutation.)

(c) The pair in (a) again: \( \diag(1,-1) \) and \( \diag(4,-9) \) are congruent, but their characteristic polynomials are \( x^2 - 1 \) and \( x^2 + 5x - 36 \), so they are not similar (@thm-charpoly-similarity-invariant). Congruence is strictly coarser than similarity on real symmetric matrices.
:::

:::: {#exr-sylvesters-law-of-inertia-c3}
[C3: Inertia of a block matrix]

Let \( \A \in M_m(\nR) \) and \( \B \in M_k(\nR) \) be symmetric. Let also \( \D \in M_n(\nR) \) be symmetric and invertible, let \( \b \in \nR^n \), let \( c \in \nR \), and put
\[
\M = \begin{pmatrix} \D & \b \\ \b\tp & c \end{pmatrix} \in M_{n+1}(\nR).
\]

::: {.enumerate options="label=(\alph*)"}
1. Prove that the inertia of \( \A \oplus \B \) is the entrywise sum of the inertias of \( \A \) and \( \B \).
2. Prove that \( \M \) is congruent to \( \D \oplus (c - \b\tp\D^{-1}\b) \).
3. Hence find the inertia of \( \M \) when \( \D = \diag(1,-1) \), \( \b = (1,1) \) and \( c = 0 \).
:::

*Hint: for (b), the congruence is the block elimination of Chapter 7, and the leftover scalar is a Schur complement.*
::::

::: {.solution}
(a) Let \( \P\tp\A\P \) and \( \Q\tp\B\Q \) be the canonical forms of @cor-real-symmetric-classification (a). Then \( \P \oplus \Q \) is invertible and
\[
(\P\oplus\Q)\tp(\A\oplus\B)(\P\oplus\Q) = (\P\tp\A\P)\oplus(\Q\tp\B\Q),
\]
a diagonal matrix whose positive, negative and zero entries are those of the two blocks together. By @thm-sylvester-inertia those counts are the inertia of \( \A\oplus\B \).

(b) Put
\[
\S = \begin{pmatrix} \I_n & -\D^{-1}\b \\ \0\tp & 1 \end{pmatrix},
\]
which is invertible, being unit upper triangular. Multiplying, the first block row of \( \M\S \) is \( (\D \mid \D(-\D^{-1}\b) + \b) = (\D \mid \0) \), and then
\[
\S\tp\M\S = \begin{pmatrix} \D & \0 \\ \0\tp & c - \b\tp\D^{-1}\b \end{pmatrix},
\]
using \( \D\tp = \D \). This is \( \D \oplus (c - \b\tp\D^{-1}\b) \), the Schur complement \( \M/\D \) sitting in the corner.

(c) Here \( \D^{-1} = \diag(1,-1) \), so \( \b\tp\D^{-1}\b = 1 - 1 = 0 \) and the leftover scalar is \( c - 0 = 0 \). By (b) and (a), the inertia of \( \M \) is the inertia of \( \diag(1,-1) \) plus that of the \( 1\times1 \) zero matrix, namely \( (1,1,0) + (0,0,1) = (1,1,1) \). In particular \( \M \) is singular.
:::
