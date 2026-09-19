# Measuring a Matrix

Chapter 11 §11 gave the Frobenius norm its own symbol and explained the subscript: a bare \( \norm{\cdot} \) already meant the norm of a *vector*, and a matrix, it warned, would shortly be asked to carry both kinds of measurement. This is that moment. A matrix is a list of \( mn \) numbers, and it is also a map; measuring the list is easy, measuring the map is what we usually want, and the two answers are not the same number. This section builds the second measurement, computes it in the three cases anyone computes, and says exactly where the first one fails.

**Throughout, \( F \) is \( \nR \) or \( \nC \)**, all spaces are finite-dimensional, and \( \norm{\cdot} \) with no subscript is a norm in the sense of @def-norm.

## What a matrix norm has to do

Chapter 9 §10 decided whether \( \A^{m} \to 0 \) by looking at one entry of one Jordan block at a time. A single number attached to \( \A \) would be a far better instrument — but only if it interacts with matrix multiplication, because the questions we want to answer are questions about products: \( \A^{m} \), \( \sum_k \A^{k} \), \( e^{\A} \). A norm that satisfies

\[
\norm{\A\B} \le \norm{\A}\,\norm{\B}
\]

immediately gives \( \norm{\A^{m}} \le \norm{\A}^{m} \), and with that one line a geometric series is in reach. A norm that does not satisfy it gives nothing at all about powers. So the property is not a technical nicety; it is the entire reason for the definition.

*A matrix norm is a norm on matrices that never lets a product be bigger than the product of the sizes.*

::: {#def-matrix-norm}
[Matrix Norm]

Let \( n \ge 1 \). A **matrix norm** on \( M_n(F) \) is a function \( \norm{\cdot} \colon M_n(F) \to \nR \) which is a norm on \( M_n(F) \) as a vector space (@def-norm) and which is in addition **submultiplicative**: for **all** \( \A, \B \in M_n(F) \),

\[
\norm{\A\B} \le \norm{\A}\,\norm{\B} .
\]
:::

In words: the first requirement is the ordinary one — clauses (N1), (N2), (N3) of @def-norm — and it sees \( M_n(F) \) only as the vector space \( F^{n^2} \) in disguise. The second requirement is the one that notices the multiplication. Note that submultiplicativity is an inequality, not an equality: it is easy for a norm to make \( \norm{\A\B} \) far smaller than \( \norm{\A}\norm{\B} \), and impossible for a matrix norm to make it larger.

The condition needs a square matrix only so that \( \A\B \) is defined for every pair; nothing else in the definition cares about the shape.

::: {#exm-frobenius-is-a-matrix-norm}
[The Frobenius norm is submultiplicative]

Show that \( \norm{\A\B}_F \le \norm{\A}_F\norm{\B}_F \) for all \( \A, \B \in M_n(F) \), so that \( \norm{\cdot}_F \) is a matrix norm.
:::

::: {.solution}
The entry \( (\A\B)_{ij} = \sum_k a_{ik}b_{kj} \) is the inner product in \( F^n \) of the \( i \)-th row of \( \A \) with the \( j \)-th column of \( \B \) (up to a conjugation, which does not change moduli). By @thm-cauchy-schwarz,

\[
\lvert (\A\B)_{ij}\rvert^2 \le
\Bigl(\sum_k \lvert a_{ik}\rvert^2\Bigr)
\Bigl(\sum_k \lvert b_{kj}\rvert^2\Bigr) .
\]

Summing over all \( i \) and \( j \), and noting that the two bracketed factors depend only on \( i \) and only on \( j \) respectively,

\[
\norm{\A\B}_F^2 \le
\Bigl(\sum_{i,k}\lvert a_{ik}\rvert^2\Bigr)
\Bigl(\sum_{k,j}\lvert b_{kj}\rvert^2\Bigr)
= \norm{\A}_F^2\,\norm{\B}_F^2 .
\]

Both sides are non-negative, so taking square roots gives the claim. That \( \norm{\cdot}_F \) is a norm was settled in Chapter 10: it is the norm induced by the Frobenius inner product (@def-induced-norm), so @thm-norm-properties and @cor-triangle-inequality apply.
:::

Now the minimal change that breaks it. Keep the idea "read the matrix as a list of numbers" but measure the list with the maximum instead of the Euclidean length.

::: {#exm-entrywise-max-not-submultiplicative}
[The entrywise maximum is not submultiplicative]

For \( \A \in M_n(F) \) put \( N(\A) = \max_{i,j}\lvert a_{ij}\rvert \). Show that \( N \) is a norm on \( M_n(F) \) but not a matrix norm for \( n \ge 2 \).
:::

::: {.solution}
\( N \) is the \( \infty \)-norm of the list of \( n^2 \) entries, so it is a norm (@def-norm): it vanishes only on the zero matrix, \( N(c\A) = \lvert c\rvert N(\A) \), and (N3) holds entry by entry.

Submultiplicativity fails already for \( n = 2 \). Take \( \A = \B = \J = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \). Then \( N(\J) = 1 \), while

\[
\J^2 = \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix}, \qquad N(\J^2) = 2 > 1 = N(\J)N(\J) .
\]

The mechanism is plain: an entry of a product is a sum of \( n \) terms, each as large as the largest entry, and a maximum taken entry by entry has no way of charging for the length of that sum. For \( n \times n \) the same matrix gives \( N(\J^2) = n \).
:::

::: {.warning}
**Submultiplicativity is a property of the norm, not of matrices.** The failure above is not caused by \( \J \) being special; it is caused by \( N \) being the wrong yardstick. @exr-matrix-and-operator-norms-c2 shows that the single rescaling \( \A \mapsto nN(\A) \) repairs it, which is a good way to see that nothing deep is being violated — only a normalization.
:::

## The norm a vector norm induces

The definition above is a filter, not a construction: it says which norms are usable, not where to find one. The construction comes from remembering what \( \A \) is for. It sends vectors to vectors, and if both are already measured, we can ask how much \( \A \) magnifies.

This is exactly the question Chapter 12 §08 asked of the singular value decomposition, and the question Chapter 12 §12 asked of an oblique projection, in each case computing \( \max\{\norm{\A\x} : \norm{\x} = 1\} \) and then promising that the number would get a name here.

Before naming it, we must know that the maximum exists. "Take the largest value of a function over infinitely many vectors" is not something one may write without a reason, and the reason is compactness, already packaged for us in @cor-closed-bounded-compact.

::: {#lem-operator-norm-attained}
[The Largest Stretch Is Attained]

Let \( n, m \ge 1 \), let \( \norm{\cdot} \) be a norm on \( F^n \) and also a norm on \( F^m \), and let \( \A \in M_{m \times n}(F) \). Then the function \( \x \mapsto \norm{\A\x} \) attains a maximum on the unit sphere \( S = \{\x \in F^n : \norm{\x} = 1\} \).
:::

::: {.idea}
Two steps, and the second is already packaged for us. ① The function is Lipschitz, hence continuous: @lem-reverse-triangle-norm converts a difference of norms into the norm of a difference, and a crude expansion in the standard basis bounds \( \norm{\A\z} \) by a constant times \( \norm{\z} \). ② The unit sphere is closed and bounded, hence compact, and a continuous real function on it attains its bounds — which is exactly what @cor-closed-bounded-compact says.
:::

::: {.proof}
**Step 1: a Lipschitz bound.** Write \( \z = \sum_{j=1}^{n} z_j\e_j \). By subadditivity and homogeneity,

\[
\norm{\A\z} \le \sum_{j=1}^{n}\lvert z_j\rvert\,\norm{\A\e_j}
\le \Bigl(\max_{j}\norm{\A\e_j}\Bigr)\norm{\z}_1 .
\]

By @thm-norm-equivalence, applied on \( F^n \) to the norms \( \norm{\cdot}_1 \) and \( \norm{\cdot} \), there is a constant \( c > 0 \) with \( \norm{\z}_1 \le c\norm{\z} \) for every \( \z \). Hence \( \norm{\A\z} \le M\norm{\z} \) with \( M = c\max_j\norm{\A\e_j} \), a constant depending on \( \A \) but not on \( \z \).

**Step 2: continuity.** Let \( \x, \y \in F^n \). By @lem-reverse-triangle-norm, applied to the vectors \( \A\x \) and \( \A\y \) of \( F^m \), and then by Step 1,

\[
\bigl\lvert\,\norm{\A\x} - \norm{\A\y}\,\bigr\rvert
\le \norm{\A(\x - \y)} \le M\norm{\x - \y} .
\]

So \( \x \mapsto \norm{\A\x} \) is Lipschitz with constant \( M \), and in particular continuous.

**Step 3: compactness.** The set \( S \) is non-empty, since \( n \ge 1 \) and \( \e_1/\norm{\e_1} \in S \), the division being legal because \( \e_1 \ne \0 \). By @cor-closed-bounded-compact the unit sphere of any norm on a finite-dimensional space is compact, and a continuous real-valued function on it attains a maximum. That corollary is where this chapter's imported facts (A3), the compactness of closed bounded sets, and (A4), the extreme value theorem, are cashed in; here we only apply it, to the continuous function of Step 2. This proves the lemma.
:::

*The operator norm of a matrix is the worst stretching it can do to a unit vector.*

::: {#def-operator-norm}
[Operator Norm]

Let \( n, m \ge 1 \) and let a norm \( \norm{\cdot} \) be given on \( F^n \) and on \( F^m \); we write both with the same symbol, the argument saying which is meant. The **operator norm** of \( \A \in M_{m \times n}(F) \) **induced by** those norms is

\[
\norm{\A} \coloneqq \max\{\,\norm{\A\x} : \x \in F^n,\ \norm{\x} = 1\,\} ,
\]

which exists by @lem-operator-norm-attained. When the vector norm is \( \norm{\cdot}_p \) on both sides we write \( \norm{\A}_p \), and \( \norm{\A}_2 \) is also called the **spectral norm**.
:::

Clause by clause: the maximum is over **unit** vectors only, so a matrix that stretches one long vector enormously is not thereby given a large norm — what counts is the *factor*. The norm on the source and the norm on the target may be different, and then \( \norm{\A} \) depends on both; the notation hides that, which is why the vector norm must always be named. And the word **induced** is doing real work: not every matrix norm arises this way, as the end of this section shows.

Three equivalent descriptions are worth having at once. For \( \A \ne 0 \),

\[
\norm{\A}
= \max_{\norm{\x} = 1}\norm{\A\x}
= \max_{\x \ne \0}\frac{\norm{\A\x}}{\norm{\x}}
= \max_{\norm{\x} \le 1}\norm{\A\x} .
\]

The middle expression equals the first because \( \norm{\A\x}/\norm{\x} = \norm{\A(\x/\norm{\x})} \) by homogeneity, and \( \x/\norm{\x} \) runs over \( S \) as \( \x \) runs over the non-zero vectors. The third equals the first because scaling any \( \x \) with \( 0 < \norm{\x} \le 1 \) up to the sphere only increases \( \norm{\A\x} \), and \( \x = \0 \) contributes \( 0 \).

The smallest cases are worth seeing before any real example, because they pin the scale. For \( \A = \0 \) every \( \A\x \) is \( \0 \), so \( \norm{\0} = 0 \), as (N1) demands. For \( m = n = 1 \), a matrix is a scalar \( (a) \), the only unit vectors are the scalars of modulus \( 1 \), and \( \norm{(a)} = \lvert a\rvert \): the operator norm of a number is its absolute value, so the definition extends the one-dimensional case rather than replacing it. And for \( \A = \I \), every unit vector satisfies \( \norm{\I\x} = \norm{\x} = 1 \), so \( \norm{\I} = 1 \) **for every choice of vector norm** — a fact used so often below that it is worth fixing now.

::: {.check}
Why is the maximum in @def-operator-norm taken over \( \norm{\x} = 1 \) rather than over all \( \x \)? What would the supremum over all \( \x \in F^n \) be?
:::

::: {.solution}
For a non-zero \( \A \) it would be infinite: pick \( \x_0 \) with \( \A\x_0 \ne \0 \); then \( \norm{\A(t\x_0)} = t\norm{\A\x_0} \to \infty \) as \( t \to \infty \). Restricting to unit vectors measures the *ratio* of output size to input size, which is what "how much does \( \A \) magnify?" means, and by homogeneity the ratio is already known on all of \( F^n \) once it is known on the sphere.
:::

::: {#thm-operator-norm-properties}
[Properties of the Operator Norm]

Let \( \norm{\cdot} \) be a norm on each of \( F^n \), \( F^m \), \( F^{\ell} \), and let \( \A \in M_{m \times n}(F) \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \norm{\A\x} \le \norm{\A}\,\norm{\x} \) for **every** \( \x \in F^n \), and \( \norm{\A} \) is the smallest constant with this property;
2. \( \norm{\cdot} \) is a norm on the vector space \( M_{m \times n}(F) \);
3. \( \norm{\I_n} = 1 \);
4. \( \norm{\A\B} \le \norm{\A}\,\norm{\B} \) for every \( \B \in M_{n \times \ell}(F) \). In particular the operator norm induced on \( M_n(F) \) by a single norm on \( F^n \) is a matrix norm in the sense of @def-matrix-norm.
:::
:::

::: {.idea}
Everything is the definition plus homogeneity. The one move worth naming is in (a): a general \( \x \ne \0 \) is \( \norm{\x} \) times a unit vector, so the inequality on the sphere upgrades to an inequality everywhere; and once (a) is available, (d) is two applications of it.
:::

::: {.proof}
(a) For \( \x = \0 \) both sides are \( 0 \). For \( \x \ne \0 \), the vector \( \u = \x/\norm{\x} \) satisfies \( \norm{\u} = 1 \), so \( \norm{\A\u} \le \norm{\A} \) by @def-operator-norm; multiplying by \( \norm{\x} \) and using homogeneity gives \( \norm{\A\x} \le \norm{\A}\norm{\x} \). If \( K \) is any constant with \( \norm{\A\x} \le K\norm{\x} \) for all \( \x \), then taking a unit \( \x_0 \) at which the maximum is attained (@lem-operator-norm-attained) gives \( \norm{\A} = \norm{\A\x_0} \le K \).

(b) Each value is a maximum of non-negative numbers, so \( \norm{\A} \ge 0 \). If \( \norm{\A} = 0 \) then \( \A\u = \0 \) for every unit \( \u \), hence \( \A\x = \0 \) for every \( \x \) by (a), hence \( \A = 0 \). For a scalar \( c \), \( \norm{c\A} = \max_{\norm{\x}=1}\lvert c\rvert\norm{\A\x} = \lvert c\rvert\norm{\A} \). For subadditivity, let \( \x \) be a unit vector; then \( \norm{(\A + \B)\x} \le \norm{\A\x} + \norm{\B\x} \le \norm{\A} + \norm{\B} \), and taking the maximum over \( \x \) gives \( \norm{\A + \B} \le \norm{\A} + \norm{\B} \).

(c) \( \norm{\I_n\x} = \norm{\x} = 1 \) for every unit \( \x \), so the maximum is \( 1 \).

(d) Let \( \x \in F^{\ell} \) be a unit vector. By (a) applied twice, first to \( \A \) and then to \( \B \),

\[
\norm{\A\B\x} \le \norm{\A}\,\norm{\B\x} \le \norm{\A}\,\norm{\B}\,\norm{\x} = \norm{\A}\,\norm{\B} .
\]

Taking the maximum over unit \( \x \) gives \( \norm{\A\B} \le \norm{\A}\norm{\B} \). This proves the theorem.
:::

Part (c) is small and will do a large amount of work: it is the single property that separates the operator norms from the rest of the matrix norms.

## The three formulas

A definition by maximization is not yet a computation. For the three standard vector norms the maximization can be carried out completely, and in two of the three cases the answer is read straight off the entries.

::: {#thm-operator-norm-formulas}
[Computing the 1-, 2- and Infinity-Norms]

Let \( \A = (a_{ij}) \in M_{m \times n}(F) \) with \( m, n \ge 1 \). Then

::: {.enumerate options="label=(\alph*)"}
1. \( \displaystyle \norm{\A}_1 = \max_{1 \le j \le n}\ \sum_{i=1}^{m}\lvert a_{ij}\rvert \), the largest absolute column sum;
2. \( \displaystyle \norm{\A}_{\infty} = \max_{1 \le i \le m}\ \sum_{j=1}^{n}\lvert a_{ij}\rvert \), the largest absolute row sum;
3. \( \norm{\A}_2 = \sigma_1(\A) \), the largest singular value of \( \A \) (@def-singular-values).
:::
:::

::: {.idea}
Each part is an upper bound and a witness. ① For \( \norm{\cdot}_1 \) the upper bound is subadditivity of the modulus with the column sums pulled out, and the witness is a standard basis vector \( \e_k \) selecting the heaviest column. ② For \( \norm{\cdot}_\infty \) the upper bound is the same estimate read along a row, and the witness is a vector of unimodular entries chosen to rotate every term of the heaviest row into the positive reals, so that no cancellation occurs. ③ For \( \norm{\cdot}_2 \) the witness is the first right singular vector, and the upper bound is the singular value decomposition: unitary factors are invisible to the Euclidean norm, so only the diagonal matrix \( \vSigma \) is left, and a diagonal matrix stretches most along its largest entry, because it scales each coordinate separately.
:::

::: {.proof}
Write \( C = \max_j\sum_i\lvert a_{ij}\rvert \) and \( R = \max_i\sum_j\lvert a_{ij}\rvert \).

*(a).* Let \( \norm{\x}_1 = 1 \). Then

\[
\norm{\A\x}_1
= \sum_{i}\Bigl\lvert \sum_j a_{ij}x_j \Bigr\rvert
\le \sum_{j}\lvert x_j\rvert \sum_{i}\lvert a_{ij}\rvert
\le C\sum_j \lvert x_j\rvert = C ,
\]

where the first inequality is subadditivity of the modulus together with an exchange of two finite sums. So \( \norm{\A}_1 \le C \). For the reverse, choose \( k \) with \( \sum_i\lvert a_{ik}\rvert = C \). The vector \( \e_k \) has \( \norm{\e_k}_1 = 1 \) and \( \A\e_k \) is the \( k \)-th column of \( \A \), so \( \norm{\A\e_k}_1 = C \). Hence \( \norm{\A}_1 \ge C \).

*(b).* Let \( \norm{\x}_{\infty} = 1 \). For each \( i \),

\[
\Bigl\lvert \sum_j a_{ij}x_j \Bigr\rvert
\le \sum_j \lvert a_{ij}\rvert\,\lvert x_j\rvert
\le \sum_j \lvert a_{ij}\rvert \le R ,
\]

so \( \norm{\A\x}_{\infty} \le R \) and \( \norm{\A}_{\infty} \le R \). For the reverse, choose \( k \) with \( \sum_j\lvert a_{kj}\rvert = R \) and define \( \x \) by \( x_j = \conj{a_{kj}}/\lvert a_{kj}\rvert \) when \( a_{kj} \ne 0 \) and \( x_j = 1 \) otherwise. Every \( x_j \) has modulus \( 1 \), so \( \norm{\x}_{\infty} = 1 \); and \( a_{kj}x_j = \lvert a_{kj}\rvert \) for every \( j \), the choice being legal exactly because we checked \( a_{kj} \ne 0 \) before dividing. Hence the \( k \)-th entry of \( \A\x \) is \( \sum_j\lvert a_{kj}\rvert = R \), giving \( \norm{\A\x}_{\infty} \ge R \).

*(c).* Let \( \A = \U\vSigma\V^{*} \) be a singular value decomposition (@thm-svd), with \( \U, \V \) unitary and \( \vSigma \) carrying \( \sigma_1 \ge \dots \ge \sigma_p \ge 0 \) on its diagonal, \( p = \min(m,n) \). Let \( \norm{\x}_2 = 1 \) and put \( \y = \V^{*}\x \). A unitary matrix is an isometry for \( \norm{\cdot}_2 \) (@thm-isometry-characterizations, (a) and (f)), so \( \norm{\y}_2 = 1 \) and \( \norm{\A\x}_2 = \norm{\U\vSigma\y}_2 = \norm{\vSigma\y}_2 \). The vector \( \vSigma\y \) has entries \( \sigma_i y_i \) for \( i \le p \) and zeros below, so

\[
\norm{\A\x}_2^2 = \sum_{i=1}^{p}\sigma_i^2\lvert y_i\rvert^2
\le \sigma_1^2\sum_{i=1}^{n}\lvert y_i\rvert^2 = \sigma_1^2 .
\]

Hence \( \norm{\A}_2 \le \sigma_1 \). For the reverse, take \( \x = \v_1 \), the first column of \( \V \); then \( \y = \V^{*}\v_1 = \e_1 \), so \( \norm{\A\v_1}_2 = \norm{\vSigma\e_1}_2 = \sigma_1 \), and \( \norm{\v_1}_2 = 1 \) because the columns of a unitary matrix are orthonormal. This proves the theorem.
:::

Part (c) is the promise this section was written to keep. Chapter 12 §08 computed \( \sigma_1 = \max\{\norm{\A\x} : \norm{\x} = 1\} \) and said that Chapter 15 would give that quantity a name, the operator norm \( \norm{\A}_2 \), "and this computation is why \( \norm{\A}_2 = \sigma_1 \)". The name is @def-operator-norm; the reason has now been separated from the name, so that the equality is a theorem about two independently defined numbers rather than a definition dressed up as one. Chapter 12 §12 measured an oblique projection by the same maximum and deferred the word twice; @exm-oblique-projection-norm below supplies it. And Chapter 11 §11, when it wrote \( \norm{\A}_F \) with an obligatory subscript, explained that the bare symbol was reserved because a matrix would soon be asked to be measured both as a list and as a map: parts (a)–(c) are that second measurement, and the rest of this section is the difference between the two.

::: {#exm-three-norms-of-a-matrix}
[One matrix, four numbers]

For \( \A = \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix} \in M_2(\nR) \), compute \( \norm{\A}_1 \), \( \norm{\A}_{\infty} \), \( \norm{\A}_F \) and \( \norm{\A}_2 \).
:::

::: {.solution}
The column sums of absolute values are \( 3 + 4 = 7 \) and \( 0 + 5 = 5 \), so \( \norm{\A}_1 = 7 \) by @thm-operator-norm-formulas (a). The row sums are \( 3 \) and \( 9 \), so \( \norm{\A}_{\infty} = 9 \) by (b). The Frobenius norm is \( \sqrt{9 + 16 + 25} = 5\sqrt2 \).

For the spectral norm, form

\[
\A\tp\A = \begin{pmatrix} 25 & 20 \\ 20 & 25 \end{pmatrix} .
\]

This matrix is \( 25\I + 20\begin{psmallmatrix} 0 & 1 \\ 1 & 0\end{psmallmatrix} \), whose eigenvalues are \( 25 \pm 20 \), namely \( 45 \) and \( 5 \). So the singular values are \( \sigma_1 = 3\sqrt5 \) and \( \sigma_2 = \sqrt5 \), and \( \norm{\A}_2 = 3\sqrt5 \approx 6.708 \) by (c).

Two checks come for free. The product \( \sigma_1\sigma_2 = 15 \) equals \( \lvert\det\A\rvert = 15 \), and \( \sigma_1^2 + \sigma_2^2 = 50 = \norm{\A}_F^2 \). The four numbers \( 7 \), \( 9 \), \( 5\sqrt2 \approx 7.071 \) and \( 3\sqrt5 \approx 6.708 \) are all different, which is the point: "the size of \( \A \)" is not a well-posed phrase until the norm is named.
:::

::: {#exm-oblique-projection-norm}
[The oblique projection, finally measured]

Chapter 12 §12 studied a projection \( P \) of \( F^2 \) onto a line, with matrix \( \begin{psmallmatrix} 1 & x \\ 0 & 0 \end{psmallmatrix} \) in a suitable orthonormal basis, and found that the largest value of \( \norm{P\v} \) over unit \( \v \) is \( \sqrt{1 + \lvert x\rvert^2} \), which over \( \nR \) is \( 1/\sin\theta \) for the angle \( \theta \) between image and kernel. Confirm this with @thm-operator-norm-formulas (c) for \( x = -1 \), the matrix \( \P' = \begin{psmallmatrix} 1 & -1 \\ 0 & 0\end{psmallmatrix} \) of @exm-oblique-projection-2x2.
:::

::: {.solution}
\( (\P')\tp\P' = \begin{psmallmatrix} 1 & -1 \\ -1 & 1\end{psmallmatrix} \), with eigenvalues \( 2 \) and \( 0 \); so \( \sigma_1 = \sqrt2 \) and \( \norm{\P'}_2 = \sqrt2 \). This agrees with \( \sqrt{1 + \lvert -1\rvert^2} = \sqrt2 \), and with \( 1/\sin\theta \) for \( \theta = \pi/4 \), the angle between the two lines. An orthogonal projection, by contrast, has \( \norm{P_U}_2 = 1 \) whenever \( U \ne \{\0\} \), since it fixes every unit vector of \( U \) and shortens the rest.
:::

The two matrix norms now in play compare in a way worth recording, because the Frobenius norm is far cheaper to compute and the spectral norm is usually the one wanted.

::: {#prp-spectral-vs-frobenius}
[Frobenius Against Spectral]

Let \( \A \in M_{m \times n}(F) \) be non-zero, of rank \( r \). Then

\[
\norm{\A}_2 \le \norm{\A}_F \le \sqrt{r}\,\norm{\A}_2 ,
\]

and the left inequality is an equality if and only if \( r = 1 \).
:::

::: {.idea}
Write both norms in terms of the singular values: \( \norm{\A}_2 = \sigma_1 \) and \( \norm{\A}_F^2 = \sigma_1^2 + \dots + \sigma_r^2 \). The claim is then the statement that one term of a sum of \( r \) non-negative numbers is at most the sum, which is at most \( r \) times the largest — and that the first is an equality exactly when there is only one term.
:::

::: {.proof}
By @lem-frobenius-unitarily-invariant and \( \A = \U\vSigma\V^{*} \) (@thm-svd), \( \norm{\A}_F = \norm{\vSigma}_F \), so \( \norm{\A}_F^2 = \sum_{i=1}^{p}\sigma_i^2 \). Exactly \( r \) of the \( \sigma_i \) are non-zero (@thm-svd), and each satisfies \( \sigma_i \le \sigma_1 \). Hence

\[
\sigma_1^2 \le \sum_{i=1}^{p}\sigma_i^2 \le r\sigma_1^2 ,
\]

which is the displayed chain after taking square roots and using \( \norm{\A}_2 = \sigma_1 \) (@thm-operator-norm-formulas (c)). The left inequality is an equality exactly when \( \sigma_i = 0 \) for all \( i \ge 2 \), that is, when \( r = 1 \).
:::

So the two norms never differ by a factor worse than \( \sqrt{r} \le \sqrt{\min(m,n)} \), and they agree exactly on the rank-one matrices. What they do *not* agree on is more interesting.

## What submultiplicativity does not buy

The Frobenius norm is a matrix norm: @exm-frobenius-is-a-matrix-norm proved it submultiplicative. It is tempting to conclude that it is therefore the operator norm induced by some vector norm — perhaps a cleverly chosen one. It is not, and the obstruction is a single line.

::: {.warning}
**Submultiplicative does not mean induced.** Every operator norm satisfies \( \norm{\I_n} = 1 \) by @thm-operator-norm-properties (c), whereas

\[
\norm{\I_n}_F = \sqrt{\underbrace{1 + 1 + \dots + 1}_{n}} = \sqrt{n} .
\]

So for \( n \ge 2 \) the Frobenius norm is **not** induced by any norm on \( F^n \) whatsoever — not by a bad choice, but by no choice at all. It is a matrix norm and not an operator norm, and the two phrases must be kept apart.
:::

The identity is the cheapest witness, and it is decisive because \( \norm{\I} = 1 \) is forced: the identity stretches nothing, so a norm that measures stretching must give it \( 1 \). A norm that assigns the identity the value \( \sqrt{n} \) is measuring something else — the amount of material in the matrix, which for \( \I_n \) grows with \( n \).

::: {.warning}
**Two different objects are called \( \norm{\A}_{\infty} \) in the wild.** In this book \( \norm{\A}_{\infty} \) is the operator norm induced by \( \norm{\cdot}_{\infty} \) on vectors, that is, the largest row sum. The entrywise maximum \( N(\A) = \max_{i,j}\lvert a_{ij}\rvert \) of @exm-entrywise-max-not-submultiplicative is a different function, and it is not even submultiplicative. Whenever a source writes \( \norm{\A}_{\infty} \), check which one is meant by evaluating it at \( \I_2 \): the row-sum norm gives \( 1 \), the entrywise maximum gives \( 1 \) as well — so evaluate instead at \( \J \), where the row-sum norm gives \( 2 \) and the entrywise maximum gives \( 1 \).
:::

::: {.check}
The Frobenius norm satisfies \( \norm{\A\x}_2 \le \norm{\A}_F\norm{\x}_2 \) for every \( \x \), by @prp-spectral-vs-frobenius and @thm-operator-norm-properties (a). Does that make it an operator norm?
:::

::: {.solution}
No. Being *compatible* with a vector norm — satisfying \( \norm{\A\x} \le \norm{\A}\norm{\x} \) — is weaker than being induced by it. The induced norm is the **smallest** constant that works (@thm-operator-norm-properties (a)), and for \( \A = \I_n \) with \( n \ge 2 \) the smallest constant is \( 1 \) while \( \norm{\I_n}_F = \sqrt n \). Compatibility says the number is big enough; being induced says it is exactly right.
:::

Where this leaves us: we have a supply of matrix norms (@def-matrix-norm), among them a distinguished family, the induced ones (@def-operator-norm), and inside that family three that are computable (@thm-operator-norm-formulas). The next section asks which quantity all of these norms are simultaneously bounding from above, and finds that the answer is the spectral radius.

## Exercises

### A. Check your understanding

:::: {#exr-matrix-and-operator-norms-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define a **matrix norm** on \( M_n(F) \), and define the **operator norm** induced by a vector norm.
2. State the three formulas of @thm-operator-norm-formulas.
3. Which analysis facts make @def-operator-norm legitimate, and where is each used?
4. Determine whether the following statement is correct, and justify your answer: every matrix norm on \( M_n(\nR) \) is the operator norm induced by some norm on \( \nR^n \).
5. Determine whether the following statement is correct, and justify your answer: for every \( \A \in M_n(F) \) and every operator norm, \( \norm{\A^2} = \norm{\A}^2 \).
:::
::::

::: {.solution}
(a) A matrix norm is a norm on the vector space \( M_n(F) \) that also satisfies \( \norm{\A\B} \le \norm{\A}\norm{\B} \) for all \( \A, \B \) (@def-matrix-norm). Given norms on \( F^n \) and \( F^m \), the operator norm of \( \A \in M_{m \times n}(F) \) is \( \norm{\A} = \max\{\norm{\A\x} : \norm{\x} = 1\} \) (@def-operator-norm).

(b) \( \norm{\A}_1 \) is the largest absolute column sum, \( \norm{\A}_{\infty} \) the largest absolute row sum, and \( \norm{\A}_2 = \sigma_1(\A) \).

(c) Two: the compactness of closed bounded sets, fact (A3) of the chapter introduction, used for the unit sphere \( S \); and the extreme value theorem, fact (A4), used for \( \x \mapsto \norm{\A\x} \). Both enter through @cor-closed-bounded-compact, quoted in Step 3 of @lem-operator-norm-attained. The continuity needed for the second is proved, not imported, and rests on @thm-norm-equivalence and @lem-reverse-triangle-norm.

(d) Incorrect. The Frobenius norm is a matrix norm, and \( \norm{\I_n}_F = \sqrt n \ne 1 \) for \( n \ge 2 \), whereas every operator norm has \( \norm{\I_n} = 1 \) by @thm-operator-norm-properties (c).

(e) Incorrect; only \( \le \) holds, by @thm-operator-norm-properties (d). Take \( \A = \begin{psmallmatrix} 0 & 1 \\ 0 & 0 \end{psmallmatrix} \), for which \( \norm{\A}_2 = 1 \) but \( \A^2 = 0 \), so \( \norm{\A^2}_2 = 0 \).
:::

### B. Practice

:::: {#exr-matrix-and-operator-norms-b1}
[B1: Four numbers for one matrix]

Let \( \A = \begin{pmatrix} 2 & -1 \\ 2 & 2 \end{pmatrix} \in M_2(\nR) \). Compute \( \norm{\A}_1 \), \( \norm{\A}_{\infty} \), \( \norm{\A}_F \) and \( \norm{\A}_2 \), and verify that \( \norm{\A}_2 \le \norm{\A}_F \).
::::

::: {.solution}
Absolute column sums: \( 2 + 2 = 4 \) and \( 1 + 2 = 3 \), so \( \norm{\A}_1 = 4 \). Absolute row sums: \( 2 + 1 = 3 \) and \( 2 + 2 = 4 \), so \( \norm{\A}_{\infty} = 4 \). Also \( \norm{\A}_F = \sqrt{4 + 1 + 4 + 4} = \sqrt{13} \).

For the spectral norm,

\[
\A\tp\A = \begin{pmatrix} 8 & 2 \\ 2 & 5 \end{pmatrix},
\]

with trace \( 13 \) and determinant \( 40 - 4 = 36 \), so its eigenvalues solve \( \lambda^2 - 13\lambda + 36 = 0 \), giving \( \lambda = 9 \) and \( \lambda = 4 \). Hence \( \sigma_1 = 3 \), \( \sigma_2 = 2 \) and \( \norm{\A}_2 = 3 \) by @thm-operator-norm-formulas (c). Finally \( 3 \le \sqrt{13} \), as @prp-spectral-vs-frobenius requires; the inequality is strict because \( \rank\A = 2 \).
:::

:::: {#exr-matrix-and-operator-norms-b2}
[B2: A rank-one matrix]

Let \( \u \in F^m \) and \( \v \in F^n \) be non-zero and put \( \A = \u\v^{*} \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \norm{\A}_2 = \norm{\u}_2\norm{\v}_2 \).
2. Verify the formula for \( \u = (1, 2) \) and \( \v = (2, -1) \) in \( \nR^2 \) by computing \( \sigma_1(\A) \) directly.
:::
::::

::: {.solution}
(a) For \( \x \in F^n \) we have \( \A\x = (\v^{*}\x)\u \), so \( \norm{\A\x}_2 = \lvert\v^{*}\x\rvert\,\norm{\u}_2 \). By @thm-cauchy-schwarz, \( \lvert\v^{*}\x\rvert = \lvert\inner{\x}{\v}\rvert \le \norm{\x}_2\norm{\v}_2 \), with equality when \( \x = \v/\norm{\v}_2 \). Hence for unit \( \x \) the quantity \( \norm{\A\x}_2 \) is at most \( \norm{\u}_2\norm{\v}_2 \) and attains that value, so \( \norm{\A}_2 = \norm{\u}_2\norm{\v}_2 \).

(b) Here \( \A = \begin{psmallmatrix} 2 & -1 \\ 4 & -2 \end{psmallmatrix} \) and \( \A\tp\A = \begin{psmallmatrix} 20 & -10 \\ -10 & 5\end{psmallmatrix} \), of trace \( 25 \) and determinant \( 100 - 100 = 0 \). So the eigenvalues are \( 25 \) and \( 0 \), giving \( \sigma_1 = 5 \). And \( \norm{\u}_2\norm{\v}_2 = \sqrt5 \cdot \sqrt5 = 5 \), in agreement. Note also \( \norm{\A}_F = 5 = \norm{\A}_2 \), as @prp-spectral-vs-frobenius predicts for a rank-one matrix.
:::

:::: {#exr-matrix-and-operator-norms-b3}
[B3: The star trick]

Let \( \A \in M_{m \times n}(F) \). Prove that \( \norm{\A^{*}\A}_2 = \norm{\A}_2^2 \). *Hint: the eigenvalues of \( \A^{*}\A \).*
::::

::: {.solution}
By @def-singular-values the eigenvalues of \( \A^{*}\A \) are \( \sigma_1^2 \ge \dots \ge \sigma_n^2 \ge 0 \), where the \( \sigma_i \) are the singular values of \( \A \) padded with zeros if \( n > m \). The matrix \( \A^{*}\A \) is positive semidefinite, hence Hermitian, so by @cor-spectral-complex-matrix it is \( \W\D\W^{*} \) with \( \W \) unitary and \( \D = \diag(\sigma_1^2, \dots, \sigma_n^2) \). Then \( (\A^{*}\A)^{*}(\A^{*}\A) = \W\D^2\W^{*} \), whose eigenvalues are \( \sigma_i^4 \), so the singular values of \( \A^{*}\A \) are the \( \sigma_i^2 \) and its largest is \( \sigma_1^2 \). By @thm-operator-norm-formulas (c), applied to \( \A^{*}\A \) and then to \( \A \),

\[
\norm{\A^{*}\A}_2 = \sigma_1^2 = \norm{\A}_2^2 .
\]

This proves the claim. Notice that it is an equality, whereas @thm-operator-norm-properties (d) alone would give only \( \norm{\A^{*}\A}_2 \le \norm{\A^{*}}_2\norm{\A}_2 \).
:::

### C. Going deeper

:::: {#exr-matrix-and-operator-norms-c1}
[C1: The spectral norm between the other two]

Let \( \A \in M_{m \times n}(F) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \norm{\A}_2 \le \sqrt{\norm{\A}_1\norm{\A}_{\infty}} \).
2. Check the inequality on the matrix of @exm-three-norms-of-a-matrix, and say how far it is from equality.
:::

*Hint for (a): apply @thm-cauchy-schwarz to the splitting \( \lvert a_{ij}\rvert = \lvert a_{ij}\rvert^{1/2}\cdot\lvert a_{ij}\rvert^{1/2}\lvert x_j\rvert \) inside one row.*
::::

::: {.solution}
(a) Write \( C = \norm{\A}_1 \) and \( R = \norm{\A}_{\infty} \) for the largest column and row sums (@thm-operator-norm-formulas). Let \( \norm{\x}_2 = 1 \). For each \( i \), @thm-cauchy-schwarz applied to the vectors with entries \( \lvert a_{ij}\rvert^{1/2} \) and \( \lvert a_{ij}\rvert^{1/2}\lvert x_j\rvert \) gives

\[
\Bigl\lvert\sum_j a_{ij}x_j\Bigr\rvert^2
\le \Bigl(\sum_j \lvert a_{ij}\rvert\Bigr)
\Bigl(\sum_j \lvert a_{ij}\rvert\,\lvert x_j\rvert^2\Bigr)
\le R\sum_j \lvert a_{ij}\rvert\,\lvert x_j\rvert^2 .
\]

Summing over \( i \) and exchanging the two finite sums,

\[
\norm{\A\x}_2^2 \le R\sum_j \lvert x_j\rvert^2\sum_i \lvert a_{ij}\rvert
\le RC\sum_j\lvert x_j\rvert^2 = RC .
\]

Taking the maximum over unit \( \x \) gives \( \norm{\A}_2^2 \le RC \), as claimed.

(b) There \( \norm{\A}_1 = 7 \) and \( \norm{\A}_{\infty} = 9 \), so the bound is \( \sqrt{63} \approx 7.937 \), while \( \norm{\A}_2 = 3\sqrt5 \approx 6.708 \). The bound overestimates by about 18 per cent. It is sharp in general: for \( \A = \I_n \) all three numbers are \( 1 \).
:::

:::: {#exr-matrix-and-operator-norms-c2}
[C2: Repairing the entrywise maximum]

For \( \A \in M_n(F) \) let \( N(\A) = \max_{i,j}\lvert a_{ij}\rvert \), as in @exm-entrywise-max-not-submultiplicative.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( N(\A\B) \le nN(\A)N(\B) \), and deduce that \( \A \mapsto nN(\A) \) **is** a matrix norm.
2. Deduce that \( nN(\cdot) \) is not an operator norm for any \( n \ge 2 \).
3. Explain why (a) and (b) together show that submultiplicativity and \( \norm{\I} = 1 \) are independent requirements.
:::
::::

::: {.solution}
(a) For all \( i, j \),

\[
\lvert(\A\B)_{ij}\rvert = \Bigl\lvert\sum_k a_{ik}b_{kj}\Bigr\rvert
\le \sum_k \lvert a_{ik}\rvert\,\lvert b_{kj}\rvert \le n\,N(\A)N(\B),
\]

so \( N(\A\B) \le nN(\A)N(\B) \). Put \( \norm{\A} = nN(\A) \). It is a norm, being a positive multiple of the norm \( N \), and

\[
\norm{\A\B} = nN(\A\B) \le n^2N(\A)N(\B) = \norm{\A}\,\norm{\B} .
\]

(b) \( \norm{\I_n} = nN(\I_n) = n \ne 1 \) for \( n \ge 2 \), while every operator norm gives the identity the value \( 1 \) (@thm-operator-norm-properties (c)).

(c) \( N \) itself is a norm with \( N(\I_n) = 1 \) that is not submultiplicative; \( nN \) is submultiplicative with \( nN(\I_n) = n \). So neither property implies the other, and an operator norm is precisely a matrix norm that also passes the identity test — a necessary condition which, as \( \norm{\cdot}_F \) already showed, is still not sufficient on its own for \( n \) large.
:::

:::: {#exr-matrix-and-operator-norms-c3}
[C3: When is a bound an equality?]

Let \( \A \in M_{m \times n}(F) \) be non-zero.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \norm{\A}_2 = \norm{\A}_F \) if and only if \( \rank\A = 1 \).
2. Give an example with \( m = n = 2 \) where \( \norm{\A}_F = \sqrt2\,\norm{\A}_2 \), the worst case allowed by @prp-spectral-vs-frobenius.
3. Is there a non-zero \( \A \) with \( \norm{\A}_F < \norm{\A}_2 \)? Justify your answer.
:::
::::

::: {.solution}
(a) This is the equality case of @prp-spectral-vs-frobenius, proved there: \( \norm{\A}_F^2 = \sum_i\sigma_i^2 \) and \( \norm{\A}_2^2 = \sigma_1^2 \), so the two agree exactly when \( \sigma_i = 0 \) for every \( i \ge 2 \), which by @thm-svd says \( \rank\A = 1 \).

(b) Take \( \A = \I_2 \). Its singular values are \( 1, 1 \), so \( \norm{\A}_2 = 1 \) and \( \norm{\A}_F = \sqrt2 \). Any matrix with two equal non-zero singular values does the same, for instance any \( 2 \times 2 \) unitary matrix.

(c) No. \( \norm{\A}_2 = \sigma_1 \le \bigl(\sum_i \sigma_i^2\bigr)^{1/2} = \norm{\A}_F \) always, since every term of the sum is non-negative. The Frobenius norm counts all the singular values and the spectral norm only the largest, so the Frobenius norm can never be the smaller of the two.
:::
