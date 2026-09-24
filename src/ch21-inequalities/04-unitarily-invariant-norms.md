# Unitarily Invariant Norms

Chapter 16 ended its survey of norms with a list of what it had left undone, and one entry read: "It has not said which norms are invariant under unitary multiplication, which is Chapter 21." This section says it. The answer is that such a norm is nothing but a symmetric gauge function applied to the singular values, so §03's inequality transfers wholesale from vectors to matrices — and the Ky Fan functionals that failed to be norms on Hermitian matrices become norms as soon as they are read on singular values instead.

**Throughout, \( F = \nR \) or \( F = \nC \)**, \( \A, \B \in M_{m\times n}(F) \), \( p = \min(m,n) \), and \( \sigma(\A) = (\sigma_1(\A), \dots, \sigma_p(\A)) \in \nR^p \) is the decreasing list of singular values (@def-singular-values). Symmetric gauge functions are §03's (@def-symmetric-gauge) and live on \( \nR^p \). For \( \x \in \nR^p \) we write
\[
\diag_{m,n}(\x) \in M_{m\times n}(F)
\]
for the matrix with \( x_1, \dots, x_p \) down the main diagonal and every other entry \( 0 \); for \( m = n \) this is the usual \( \diag(x_1, \dots, x_n) \). Finally, one consequence of @thm-svd and @thm-singular-values-unique is used constantly: if \( \A = \W\vSigma\X^{*} \) is a singular value decomposition and \( \U \in M_m(F) \), \( \V \in M_n(F) \) are unitary, then
\[
\U\A\V = (\U\W)\,\vSigma\,(\V^{*}\X)^{*}
\]
is again of that shape, with \( \U\W \) and \( \V^{*}\X \) unitary, so
\[
\sigma(\U\A\V) = \sigma(\A) .
\]{#eq-singular-values-unitary-invariant}

## Norms that do not see the unitary factors

Two matrix norms in the book already ignore unitary factors. The Frobenius norm does, by @lem-frobenius-unitarily-invariant; the spectral norm does, by @lem-spectral-frobenius-toolkit (c). Both facts were proved separately and both were used the same way: to replace \( \A \) by \( \vSigma \) and reduce a question about a matrix to a question about a list of numbers. That is a property worth isolating, and it is the property Chapter 16 left unnamed.

*A norm is unitarily invariant when rotating the domain and the codomain does not change the measurement.*

::: {#def-unitarily-invariant-norm}
[Unitarily Invariant Norm]

A **unitarily invariant norm** on \( M_{m\times n}(F) \) is a norm \( \uinorm{\cdot} \) on \( M_{m\times n}(F) \), regarded as a vector space over \( F \), such that
\[
\uinorm{\U\A\V} = \uinorm{\A}
\]
for **every** \( \A \in M_{m\times n}(F) \) and **all** unitary \( \U \in M_m(F) \), \( \V \in M_n(F) \).
:::

The triple bars are standard and are used from here on for a norm known to be unitarily invariant; a single bar with a subscript, as in \( \norm{\A}_2 \) or \( \norm{\A}_F \), keeps naming a specific one. In words: the condition is not invariance under similarity, and not invariance under transposition; it is invariance under multiplying on the **left** by any unitary and on the **right** by any unitary, independently. The two unitaries are unrelated, which is what makes the condition strong. Asking only for invariance under \( \A \mapsto \U\A\U^{*} \), with the same unitary on both sides, is a much weaker demand: \( \lvert\tr\A\rvert \) has it, since \( \tr(\U\A\U^{*}) = \tr\A \) by @thm-trace-properties (3), yet it is not determined by \( \sigma(\A) \), because \( \I_2 \) and \( \diag(1,-1) \) both have singular values \( 1, 1 \) while their traces have absolute values \( 2 \) and \( 0 \).

::: {#exm-ui-norm-examples}
[The two familiar norms]

Check each against @def-unitarily-invariant-norm.

::: {.enumerate options="label=(\alph*)"}
1. The Frobenius norm \( \norm{\A}_F \).
2. The spectral norm \( \norm{\A}_2 \).
:::
:::

::: {.solution}
(a) It is a norm, being the norm of the Frobenius inner product of Chapter 11 §01, and \( \norm{\U\A\V}_F = \norm{\A}_F \) is @lem-frobenius-unitarily-invariant.

(b) It is a norm by @thm-operator-norm-properties (b), and @lem-spectral-frobenius-toolkit (c) gives \( \norm{\U\A\V}_2 = \norm{\A}_2 \) for unitary \( \U, \V \). By @thm-operator-norm-formulas (c), \( \norm{\A}_2 = \sigma_1(\A) \), so this norm too is a function of \( \sigma(\A) \) alone — and @eq-singular-values-unitary-invariant gives a second proof of its invariance.
:::

Both are built from \( \sigma(\A) \). The largest singular value and the square root of the sum of their squares are two entries in a whole family, and the family is the point of the section.

::: {#def-ky-fan-norm}
[Ky Fan k-Norms]

For \( 1 \le k \le p \), the **Ky Fan \( k \)-norm** of \( \A \in M_{m\times n}(F) \) is
\[
\uinorm{\A}_{(k)} = \sum_{i=1}^{k}\sigma_i(\A) ,
\]
the sum of the \( k \) largest singular values. For \( k = 1 \) it is the spectral norm \( \norm{\A}_2 \); for \( k = p \) it is called the **trace norm**.
:::

Chapter 17 §06 measured a Hermitian matrix by \( s_k(\A) = \lambda_1(\A) + \dots + \lambda_k(\A) \) and found in @exr-poincare-and-ky-fan-c2 that this is no norm: \( s_1(\diag(0,-1)) = 0 \) although \( \diag(0,-1) \ne \0 \). The exercise said that "the repair is to apply \( N_k \) [its name there for \( s_k \)] to the singular values instead of the eigenvalues, which is what Chapter 21 does". @def-ky-fan-norm is that repair, and the repair works. Positive definiteness now holds because singular values are non-negative, so they can only sum to \( 0 \) by all vanishing, which by @thm-svd forces \( \A = \0 \); absolute homogeneity holds because \( (c\A)^{*}(c\A) = \lvert c\rvert^{2}\A^{*}\A \) gives \( \sigma(c\A) = \lvert c\rvert\sigma(\A) \) through @def-singular-values; and unitary invariance is @eq-singular-values-unitary-invariant. The triangle inequality is the one axiom still outstanding, and @lem-singular-value-subadditive below supplies it.

**Non-examples by minimal change.** Both are honest norms on \( M_2(\nR) \) that fail only the invariance clause, and one witness refutes both. Let
\[
\U = \frac{1}{\sqrt2}\begin{pmatrix} 1 & -1 \\ 1 & 1\end{pmatrix} ,
\]
a rotation through half a right angle, which is orthogonal since its columns are orthonormal.

- *The entrywise maximum* \( N(\A) = \max_{i,j}\lvert a_{ij}\rvert \) is a norm (it is the \( \infty \)-norm of the entry list). But \( N(\I_2) = 1 \) while \( N(\U\I_2\I_2) = N(\U) = 1/\sqrt2 \).
- *The operator \( 1 \)-norm* \( \norm{\A}_1 \), the largest column sum of absolute values (@thm-operator-norm-formulas (a)), is a norm. But \( \norm{\I_2}_1 = 1 \) while \( \norm{\U}_1 = 1/\sqrt2 + 1/\sqrt2 = \sqrt2 \).

Both failures are visible in the same picture: \( \I_2 \) and \( \U \) have the same singular values, namely \( 1, 1 \), because both are orthogonal, and a unitarily invariant norm is therefore forced to give them the same value. A norm that reads individual entries or individual columns is reading a basis, and a unitary change of basis is exactly what @def-unitarily-invariant-norm forbids it to notice.

**Why this definition.** The clause is exactly what makes a norm a function of the singular values and nothing else, as the next lemma shows; that is its whole purpose. Weakening it to one-sided invariance \( \uinorm{\U\A} = \uinorm{\A} \) is not enough. The largest Euclidean length among the columns of \( \A \) is a norm with that property, since a unitary matrix preserves the length of each column; but it gives \( \diag(2,1) \) the value \( 2 \), while \( \diag(2,1)\U\tp = \tfrac{1}{\sqrt2}\begin{psmallmatrix} 2 & 2\\ -1 & 1\end{psmallmatrix} \) has both columns of length \( \sqrt{5/2} \), and the two matrices have the same singular values. Strengthening it to include all invertible \( \U, \V \) is far too much, since every non-zero matrix of a given rank would then have the same norm.

::: {.check}
Is \( \A \mapsto \sigma_2(\A) \) a unitarily invariant norm on \( M_2(\nR) \)? Is \( \A \mapsto \sigma_1(\A) - \sigma_2(\A) \)?
:::

::: {.solution}
Neither, and both fail (N1) of @def-norm rather than the invariance clause: they are unitarily invariant by @eq-singular-values-unitary-invariant, but they are not norms. The matrix \( \A = \e_1\e_1\tp \) has \( \sigma(\A) = (1, 0) \), so \( \sigma_2(\A) = 0 \) with \( \A \ne \0 \). The identity has \( \sigma(\I_2) = (1,1) \), so \( \sigma_1(\I_2) - \sigma_2(\I_2) = 0 \) with \( \I_2 \ne \0 \). This is the same failure Chapter 17 met with \( s_k \), and it says that not every symmetric-looking formula in the singular values is a norm; the correspondence below says exactly which are.
:::

## A unitarily invariant norm is a function of the singular values

::: {#lem-ui-norm-of-diagonal}
[The Gauge of a Unitarily Invariant Norm]

Let \( \uinorm{\cdot} \) be a unitarily invariant norm on \( M_{m\times n}(F) \) and define
\[
\Phi(\x) = \uinorm{\diag_{m,n}(\x)} \qquad (\x \in \nR^p) .
\]
Then \( \Phi \) is a symmetric gauge function on \( \nR^p \), and
\[
\uinorm{\A} = \Phi\bigl(\sigma(\A)\bigr) \qquad \text{for every } \A \in M_{m\times n}(F) .
\]
In particular \( \uinorm{\A} \) depends on \( \A \) only through \( \sigma(\A) \).
:::

::: {.idea}
The map \( \x \mapsto \diag_{m,n}(\x) \) is linear and injective, so the norm axioms for \( \Phi \) are inherited entry for entry. The two invariance clauses are the two families of unitary matrices that act diagonally: a permutation matrix on each side rearranges the diagonal, a diagonal matrix of signs on one side flips its signs. The last formula is the singular value decomposition, read once.
:::

::: {.proof}
**\( \Phi \) is a norm.** The map \( L(\x) = \diag_{m,n}(\x) \) is linear from \( \nR^p \) to \( M_{m\times n}(F) \) and injective, since \( L(\x) = \0 \) reads off as \( \x = \0 \). Hence \( \Phi = \uinorm{\cdot}\circ L \) satisfies (N1) — \( \Phi(\x) = 0 \) gives \( L(\x) = \0 \) and \( \x = \0 \) — and (N2) for real scalars, and (N3), all directly from the corresponding axioms for \( \uinorm{\cdot} \).

**(G1).** The letter \( \sigma \) is taken here, so write \( \pi \) for a permutation of \( \{1, \dots, p\} \). Extend it to a permutation \( \widehat\pi \) of \( \{1, \dots, m\} \) and to one \( \widetilde\pi \) of \( \{1, \dots, n\} \) by fixing every index greater than \( p \), and let \( \P \in M_m(F) \) and \( \Q \in M_n(F) \) be their permutation matrices (@def-permutation-matrix), which are unitary by @lem-permutation-matrices (b). Writing \( \D = \diag_{m,n}(\x) \), multiplying by \( \P \) on the left moves row \( k \) to row \( \widehat\pi(k) \) and multiplying by \( \Q\tp \) on the right moves column \( l \) to column \( \widetilde\pi(l) \); no entry is created or destroyed. The only non-zero entries of \( \D \) are \( d_{kk} = x_k \) for \( k \le p \), and they land in positions \( (\widehat\pi(k), \widetilde\pi(k)) = (\pi(k), \pi(k)) \), again on the main diagonal. Hence
\[
\P\,\diag_{m,n}(\x)\,\Q\tp = \diag_{m,n}(\P_\pi\x) .
\]
Taking \( \uinorm{\cdot} \) of both sides and using @def-unitarily-invariant-norm gives \( \Phi(\P_\pi\x) = \Phi(\x) \).

**(G2).** Let \( \varepsilon_1, \dots, \varepsilon_p \) be signs. The matrix \( \diag(\varepsilon_1, \dots, \varepsilon_p, 1, \dots, 1) \in M_m(F) \) is real diagonal with entries of modulus \( 1 \), hence unitary, and multiplying on the left by it multiplies row \( k \) by \( \varepsilon_k \). So it carries \( \diag_{m,n}(\x) \) to \( \diag_{m,n}(\varepsilon_1x_1, \dots, \varepsilon_px_p) \), and invariance gives (G2).

**The formula.** Let \( \A = \U\vSigma\V^{*} \) be a singular value decomposition (@thm-svd). Then \( \vSigma = \diag_{m,n}(\sigma(\A)) \), and \( \A = \U\vSigma\V^{*} \) with \( \U \) and \( \V^{*} \) unitary, so \( \uinorm{\A} = \uinorm{\vSigma} = \Phi(\sigma(\A)) \). This proves the lemma.
:::

So the map \( \uinorm{\cdot}\mapsto\Phi \) loses nothing. The question is whether it is onto: does every symmetric gauge come from a unitarily invariant norm? Evaluating \( \Phi \) at \( \sigma(\A) \) certainly produces a unitarily invariant *function*, by @eq-singular-values-unitary-invariant, and (N1) and (N2) are easy. Everything hangs on the triangle inequality, and the triangle inequality hangs on one majorization.

## Singular values are subadditive

::: {#lem-singular-value-subadditive}
[Weak Subadditivity of the Singular Values]

Let \( \A, \B \in M_{m\times n}(F) \). Then
\[
\sigma(\A + \B) \prec_w \sigma(\A) + \sigma(\B) ,
\]
that is, \( \displaystyle\sum_{i=1}^{k}\sigma_i(\A+\B) \le \sum_{i=1}^{k}\bigl(\sigma_i(\A) + \sigma_i(\B)\bigr) \) for every \( 1 \le k \le p \).
:::

::: {.idea}
The statement is about singular values, and the tool — @cor-ky-fan-subadditive, which says that the top \( k \) eigenvalues of a Hermitian sum are subadditive — is about eigenvalues. The Hermitian dilation \( \cH \) of @prp-hermitian-dilation converts one into the other, and it does so **linearly**: \( \cH(\A+\B) = \cH(\A) + \cH(\B) \), because the blocks add. Since the top \( p \) eigenvalues of \( \cH(\A) \) are exactly \( \sigma_1(\A), \dots, \sigma_p(\A) \), the corollary transfers verbatim.
:::

::: {.proof}
Write \( \cH(\M) = \begin{psmallmatrix} \0 & \M \\ \M^{*} & \0\end{psmallmatrix} \in M_{m+n}(F) \) for the Hermitian dilation of @prp-hermitian-dilation. Adding block by block, \( \cH(\A+\B) = \cH(\A) + \cH(\B) \).

By @prp-hermitian-dilation the eigenvalue list of \( \cH(\M) \), with multiplicity, consists of \( \sigma_1(\M), \dots, \sigma_p(\M) \), then \( m+n-2p \) zeros, then \( -\sigma_p(\M), \dots, -\sigma_1(\M) \). Every singular value is \( \ge 0 \) and every listed negative number is \( \le 0 \), so this list, read in the order written, is already decreasing. Hence
\[
\lambda_i\bigl(\cH(\M)\bigr) = \sigma_i(\M) \qquad (1 \le i \le p) ,
\]
for every \( \M \in M_{m\times n}(F) \).

Now fix \( 1 \le k \le p \). The matrices \( \cH(\A) \) and \( \cH(\B) \) are Hermitian of the same size, so @cor-ky-fan-subadditive applies to them:
\[
\sum_{i=1}^{k}\lambda_i\bigl(\cH(\A)+\cH(\B)\bigr) \ \le\ \sum_{i=1}^{k}\lambda_i\bigl(\cH(\A)\bigr) + \sum_{i=1}^{k}\lambda_i\bigl(\cH(\B)\bigr) .
\]
Replacing \( \cH(\A) + \cH(\B) \) by \( \cH(\A+\B) \) on the left and using the displayed identity three times turns this into
\[
\sum_{i=1}^{k}\sigma_i(\A+\B) \ \le\ \sum_{i=1}^{k}\sigma_i(\A) + \sum_{i=1}^{k}\sigma_i(\B) .
\]
Finally, \( \sigma(\A)+\sigma(\B) \) is a sum of two decreasing vectors, hence decreasing, so it is its own decreasing rearrangement, and the displayed inequalities for \( k = 1, \dots, p \) are precisely (M1) for \( \prec_w \) in @def-majorization. This proves the lemma.
:::

Two remarks on the route. The dilation was chosen because it reduces the statement to a corollary already proved, in four lines and with no new variational argument; the alternative is to establish a Ky Fan maximum principle for singular values directly, maximizing \( \sum_{i\le k}\lvert\inner{\A\w_i}{\q_i}\rvert \) over pairs of orthonormal lists, which is a genuine theorem in its own right and is not needed here. And the conclusion really is only **weak** majorization: for \( \A = \I_2 \) and \( \B = \diag(-1, 1) \) we have \( \sigma(\A) = \sigma(\B) = (1,1) \) and \( \A + \B = \diag(0, 2) \), so \( \sigma(\A+\B) = (2, 0) \) has total \( 2 \) while \( \sigma(\A)+\sigma(\B) = (2,2) \) has total \( 4 \). Section 6 records this as a negative result: no strengthening to \( \prec \) is available.

The debts of the last two examples are now paid. By @lem-singular-value-subadditive with \( k \) fixed,
\[
\uinorm{\A+\B}_{(k)} \ \le\ \uinorm{\A}_{(k)} + \uinorm{\B}_{(k)} ,
\]
so the Ky Fan \( k \)-norms of @def-ky-fan-norm really are norms, and so is the trace norm, the case \( k = p \). Chapter 17 §06's Ky Fan functionals have been repaired exactly as that section promised.

## The correspondence

::: {#thm-von-neumann-correspondence}
[Unitarily Invariant Norms Are Symmetric Gauges]

Let \( m, n \ge 1 \) and \( p = \min(m,n) \). The assignments
\[
\uinorm{\cdot} \ \longmapsto\ \Phi_{\uinorm{\cdot}}(\x) = \uinorm{\diag_{m,n}(\x)} ,
\qquad
\Phi \ \longmapsto\ \uinorm{\A}_\Phi = \Phi\bigl(\sigma(\A)\bigr)
\]
are mutually inverse bijections between the unitarily invariant norms on \( M_{m\times n}(F) \) and the symmetric gauge functions on \( \nR^p \).
:::

::: {.idea}
@lem-ui-norm-of-diagonal is one direction and already contains the fact that the round trip \( \uinorm{\cdot}\mapsto\Phi\mapsto\uinorm{\cdot} \) is the identity. For the other direction the only issue is the triangle inequality for \( \A \mapsto \Phi(\sigma(\A)) \), and it splits into two steps that have just been prepared: \( \sigma(\A+\B) \prec_w \sigma(\A)+\sigma(\B) \), then §03's theorem, then the triangle inequality for \( \Phi \) itself.
:::

::: {.proof}
**Step 1: \( \uinorm{\cdot}_\Phi \) is a unitarily invariant norm.** Let \( \Phi \) be a symmetric gauge function on \( \nR^p \) and put \( \uinorm{\A}_\Phi = \Phi(\sigma(\A)) \).

(N1). \( \Phi(\sigma(\A)) \ge 0 \), and it vanishes only if \( \sigma(\A) = \0 \), which by @thm-svd forces \( \A = \U\0\V^{*} = \0 \).

(N2). For \( c \in F \), \( (c\A)^{*}(c\A) = \lvert c\rvert^{2}\A^{*}\A \), so each eigenvalue of \( (c\A)^{*}(c\A) \) is \( \lvert c\rvert^2 \) times the matching eigenvalue of \( \A^{*}\A \) and @def-singular-values gives \( \sigma(c\A) = \lvert c\rvert\sigma(\A) \). Hence \( \uinorm{c\A}_\Phi = \Phi(\lvert c\rvert\sigma(\A)) = \lvert c\rvert\uinorm{\A}_\Phi \).

(N3). The vectors \( \sigma(\A+\B) \) and \( \sigma(\A)+\sigma(\B) \) have non-negative entries, and @lem-singular-value-subadditive gives \( \sigma(\A+\B) \prec_w \sigma(\A)+\sigma(\B) \). So @thm-gauge-monotone-under-majorization (b) applies, and then the triangle inequality for the norm \( \Phi \):
\[
\begin{aligned}
\uinorm{\A+\B}_\Phi = \Phi\bigl(\sigma(\A+\B)\bigr)
&\le \Phi\bigl(\sigma(\A) + \sigma(\B)\bigr) \\
&\le \Phi\bigl(\sigma(\A)\bigr) + \Phi\bigl(\sigma(\B)\bigr) = \uinorm{\A}_\Phi + \uinorm{\B}_\Phi .
\end{aligned}
\]

Invariance. By @eq-singular-values-unitary-invariant, \( \sigma(\U\A\V) = \sigma(\A) \) for unitary \( \U, \V \), so \( \uinorm{\U\A\V}_\Phi = \uinorm{\A}_\Phi \).

**Step 2: the round trips.** Start from a unitarily invariant norm \( \uinorm{\cdot} \). By @lem-ui-norm-of-diagonal its \( \Phi = \Phi_{\uinorm{\cdot}} \) is a symmetric gauge and \( \uinorm{\A} = \Phi(\sigma(\A)) = \uinorm{\A}_\Phi \) for every \( \A \), so the second assignment undoes the first.

Start instead from a symmetric gauge \( \Phi \) on \( \nR^p \), and let \( \Psi \) be the gauge of the norm \( \uinorm{\cdot}_\Phi \). For \( \x \in \nR^p \), the matrix \( \diag_{m,n}(\x) \) has \( \diag_{m,n}(\x)^{*}\diag_{m,n}(\x) = \diag(x_1^2, \dots, x_p^2, 0, \dots, 0) \), whose eigenvalue list in decreasing order is \( (\lvert\x\rvert^{\downarrow})^2 \) padded with zeros; so @def-singular-values gives \( \sigma(\diag_{m,n}(\x)) = \lvert\x\rvert^{\downarrow} \). Hence
\[
\Psi(\x) = \uinorm{\diag_{m,n}(\x)}_\Phi = \Phi\bigl(\lvert\x\rvert^{\downarrow}\bigr) = \Phi(\x) ,
\]
the last equality by @eq-gauge-depends-on-sorted-moduli. So the first assignment undoes the second, and the two maps are mutually inverse bijections. This proves the theorem.
:::

The theorem is a machine for producing matrix norms: choose any symmetric gauge and it hands back a unitarily invariant norm, with the triangle inequality free of charge. Feeding it the gauges of @exm-symmetric-gauge-examples (a) gives the most-used family.

::: {#exm-schatten-norms}
[The Schatten norms]

The letter \( p \) is reserved in this section for \( \min(m,n) \), so write the exponent as \( r \). For \( 1 \le r \le \infty \), the **Schatten \( r \)-norm** is
\[
\uinorm{\A}_{S_r} = \norm{\sigma(\A)}_r = \Bigl(\sum_{i=1}^{p}\sigma_i(\A)^{r}\Bigr)^{1/r} ,
\]
read as \( \uinorm{\A}_{S_\infty} = \sigma_1(\A) \) at \( r = \infty \). Identify \( S_1 \), \( S_2 \) and \( S_\infty \), and explain why each \( \uinorm{\cdot}_{S_r} \) is a unitarily invariant norm.
:::

::: {.solution}
By @exm-symmetric-gauge-examples (a), \( \norm{\cdot}_r \) is a symmetric gauge function on \( \nR^{p} \) for every \( 1 \le r \le \infty \). So @thm-von-neumann-correspondence makes \( \A \mapsto \norm{\sigma(\A)}_r \) a unitarily invariant norm, with no further checking. At the three familiar exponents: \( \uinorm{\cdot}_{S_1} \) is the trace norm, since \( \norm{\sigma(\A)}_1 = \sum_i\sigma_i(\A) \); \( \uinorm{\cdot}_{S_2} \) is the Frobenius norm, since \( \norm{\A}_F^2 = \norm{\vSigma}_F^2 = \sum_i\sigma_i(\A)^2 \) by @lem-frobenius-unitarily-invariant applied to \( \A = \U\vSigma\V^{*} \); and \( \uinorm{\cdot}_{S_\infty} \) is the spectral norm, by @thm-operator-norm-formulas (c). The three norms Chapter 16 measured matrices with are three points of one family. A concrete reading: the symmetric \( \A = \begin{psmallmatrix} 2 & 1\\ 1 & 2\end{psmallmatrix} \) has eigenvalues \( 3 \) and \( 1 \), both positive, so \( \A^{*}\A = \A^2 \) has eigenvalues \( 9 \) and \( 1 \) and \( \sigma(\A) = (3,1) \) by @def-singular-values. Hence \( \uinorm{\A}_{S_1} = 4 \), \( \uinorm{\A}_{S_2} = \sqrt{10} \) — which matches \( \norm{\A}_F = \sqrt{4+1+1+4} \) — and \( \uinorm{\A}_{S_\infty} = 3 \).
:::

## What every unitarily invariant norm satisfies

Chapter 20 §09 collected the facts it needed about moving factors in and out of the spectral and Frobenius norms (@lem-spectral-frobenius-toolkit). Part (b) of that lemma — \( \norm{\X\M\Y} \le \norm{\X}_2\norm{\M}\norm{\Y}_2 \) — was proved separately for the two norms. It holds for all of them at once.

::: {#prp-ui-norm-properties}
[Basic Properties]

Let \( \uinorm{\cdot} \) be a unitarily invariant norm on \( M_{m\times n}(F) \), with gauge \( \Phi \) as in @lem-ui-norm-of-diagonal, and let \( \A \in M_{m\times n}(F) \).

::: {.enumerate options="label=(\alph*)"}
1. \( \sigma(\A^{*}) = \sigma(\A) \); consequently, if \( \uinorm{\cdot}' \) is the unitarily invariant norm on \( M_{n\times m}(F) \) attached to the same gauge \( \Phi \) by @thm-von-neumann-correspondence, then \( \uinorm{\A^{*}}' = \uinorm{\A} \). For \( m = n \) this reads \( \uinorm{\A^{*}} = \uinorm{\A} \).
2. \( \uinorm{\X\A} \le \norm{\X}_2\,\uinorm{\A} \) for every \( \X \in M_m(F) \), and \( \uinorm{\A\Y} \le \uinorm{\A}\,\norm{\Y}_2 \) for every \( \Y \in M_n(F) \).
3. If \( \uinorm{\cdot} \) is **normalized**, meaning \( \uinorm{\e_1\e_1^{*}} = 1 \) for the \( m\times n \) matrix \( \e_1\e_1^{*} \) with a single \( 1 \) in position \( (1,1) \), then
\[
\norm{\A}_2 \ \le\ \uinorm{\A} \ \le\ \uinorm{\A}_{(p)} .
\]
4. A normalized unitarily invariant norm on \( M_n(F) \) is submultiplicative: \( \uinorm{\A\B} \le \uinorm{\A}\,\uinorm{\B} \).
:::
:::

::: {.idea}
Everything reduces to one inequality between singular values, \( \sigma_i(\X\A) \le \norm{\X}_2\sigma_i(\A) \), and then to §03's monotonicity @prp-gauge-monotone. That inequality is one line of the min–max theorem: the subspace on which \( \A \) stretches by at most \( \sigma_i(\A) \) also works for \( \X\A \), with the factor \( \norm{\X}_2 \) paid once. Part (c) is @cor-gauge-between-infinity-and-one, read through the correspondence, and (d) is (b) and (c) combined.
:::

::: {.proof}
(a) By @thm-svd write \( \A = \U\vSigma\V^{*} \); then \( \A^{*} = \V\vSigma^{*}\U^{*} \), and \( \vSigma^{*} = \diag_{n,m}(\sigma(\A)) \) has the same diagonal. By @thm-singular-values-unique applied to \( \A^{*} \), \( \sigma(\A^{*}) = \sigma(\A) \). The consequence is @lem-ui-norm-of-diagonal used twice: \( \uinorm{\A^{*}}' = \Phi(\sigma(\A^{*})) = \Phi(\sigma(\A)) = \uinorm{\A} \).

(b) Everything rests on one inequality between singular values.

::: {.claim}
\( \sigma_k(\X\A) \le \norm{\X}_2\,\sigma_k(\A) \) for every \( 1 \le k \le n \), with the convention \( \sigma_k = 0 \) for \( k > p \).
:::

::: {.proof}
Fix a singular value decomposition of \( \A \) with right singular vectors \( \v_1, \dots, \v_n \), and let \( T_k = \Span(\v_k, \dots, \v_n) \), a subspace of \( F^n \) of dimension \( n-k+1 \). By @lem-stretch-in-singular-coordinates (a), \( \norm{\A\x} \le \sigma_k(\A)\norm{\x} \) for every \( \x \in T_k \). By @thm-operator-norm-properties (a), \( \norm{\X(\A\x)} \le \norm{\X}_2\norm{\A\x} \), so
\[
\norm{(\X\A)\x} \le \norm{\X}_2\,\sigma_k(\A)\,\norm{\x} \qquad (\x \in T_k) .
\]
The matrices \( \X\A \) and \( \A \) both have \( n \) columns, so @thm-singular-value-minmax applies to \( \X\A \) with subspaces of \( F^n \): \( \sigma_k(\X\A) \) is the **minimum** over subspaces of dimension \( n-k+1 \) of the largest stretch on them, and \( T_k \) is one competitor. Hence \( \sigma_k(\X\A) \le \norm{\X}_2\sigma_k(\A) \).
:::

Now \( \X\A \) and \( \A \) lie in the same space \( M_{m\times n}(F) \), and the claim says \( \lvert\sigma_i(\X\A)\rvert \le \lvert\norm{\X}_2\sigma_i(\A)\rvert \) for \( 1 \le i \le p \). By @prp-gauge-monotone and then (N2) for \( \Phi \),
\[
\uinorm{\X\A} = \Phi\bigl(\sigma(\X\A)\bigr) \le \Phi\bigl(\norm{\X}_2\sigma(\A)\bigr) = \norm{\X}_2\,\Phi\bigl(\sigma(\A)\bigr) = \norm{\X}_2\uinorm{\A} .
\]
For the second inequality, apply the first to \( \A^{*} \) and \( \Y^{*} \) inside \( M_{n\times m}(F) \), with the norm \( \uinorm{\cdot}' \) of part (a): \( \uinorm{(\A\Y)^{*}}' = \uinorm{\Y^{*}\A^{*}}' \le \norm{\Y^{*}}_2\uinorm{\A^{*}}' \). By (a) the left side is \( \uinorm{\A\Y} \) and \( \uinorm{\A^{*}}' = \uinorm{\A} \), while \( \norm{\Y^{*}}_2 = \norm{\Y}_2 \) by @lem-spectral-frobenius-toolkit (a).

(c) The matrix \( \e_1\e_1^{*} \) is \( \diag_{m,n}(\e_1) \), so the normalization says \( \Phi(\e_1) = 1 \). By @cor-gauge-between-infinity-and-one, \( \Phi(\e_1)\norm{\x}_\infty \le \Phi(\x) \le \Phi(\e_1)\norm{\x}_1 \) for every \( \x \in \nR^p \). At \( \x = \sigma(\A) \) this reads
\[
\sigma_1(\A) \ \le\ \Phi\bigl(\sigma(\A)\bigr) \ \le\ \sum_{i=1}^{p}\sigma_i(\A) ,
\]
which is the claim, since \( \sigma_1(\A) = \norm{\A}_2 \) by @thm-operator-norm-formulas (c) and the right-hand side is \( \uinorm{\A}_{(p)} \) by @def-ky-fan-norm.

(d) By (b) and then (c), \( \uinorm{\A\B} \le \norm{\A}_2\uinorm{\B} \le \uinorm{\A}\,\uinorm{\B} \). This proves the proposition.
:::

Applying (b) twice, once on each side, gives \( \uinorm{\X\A\Y} \le \norm{\X}_2\uinorm{\A}\norm{\Y}_2 \). That is @lem-spectral-frobenius-toolkit (b) with the two named norms replaced by any unitarily invariant one, so the debt announced at the head of this subsection is paid. Taking \( \X = \U \) and \( \Y = \V \) unitary recovers @def-unitarily-invariant-norm itself: a unitary matrix has orthonormal columns, so \( \norm{\U}_2 = \norm{\V}_2 = 1 \) by @lem-spectral-frobenius-toolkit (c), and the bound reads \( \uinorm{\U\A\V} \le \uinorm{\A} \); applying it again to \( \U^{*}(\U\A\V)\V^{*} = \A \) gives \( \uinorm{\A} \le \uinorm{\U\A\V} \), and the two together give equality.

::: {.warning}
**A unitarily invariant norm need not be submultiplicative, and the normalization in (d) is what supplies the lower bound that rules it out.** Half the spectral norm, \( \uinorm{\A} = \tfrac12\norm{\A}_2 \), is a unitarily invariant norm — it is \( \Phi(\sigma(\A)) \) for the symmetric gauge \( \Phi = \tfrac12\norm{\cdot}_\infty \). At \( \A = \B = \I_n \) it gives \( \uinorm{\A\B} = \tfrac12 \) while \( \uinorm{\A}\uinorm{\B} = \tfrac14 \), so submultiplicativity fails. Doubling instead of halving is harmless: \( 2\norm{\cdot}_2 \) is submultiplicative. What @prp-ui-norm-properties (d) really needs is \( \norm{\A}_2 \le \uinorm{\A} \), and @cor-gauge-between-infinity-and-one delivers that as soon as \( \uinorm{\e_1\e_1^{*}} \ge 1 \), normalized or not; here \( \uinorm{\e_1\e_1^{*}} = \tfrac12 \), and the bound runs the wrong way. Submultiplicativity is a property of the **scaling** of a norm, not of its shape.
:::

@thm-von-neumann-correspondence is the section's payment of Chapter 16 §08's debt: the norms invariant under unitary multiplication are exactly the symmetric gauges of the singular values, and there are as many of them as there are norms on \( \nR^p \) that ignore order and sign. What the correspondence buys is that any inequality between two singular value lists in the weak majorization order becomes an inequality between the matrices in **every** one of these norms at once. Section 6 makes that the definition of dominance and uses it to settle low-rank approximation and the nearest unitary matrix; Section 7 does the same for Lidskii's and Mirsky's theorems.

## Exercises

### A. Check your understanding

:::: {#exr-unitarily-invariant-norms-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State @def-unitarily-invariant-norm, saying exactly which matrices \( \U \) and \( \V \) range over.
2. Explain in one sentence why a unitarily invariant norm can be computed from \( \sigma(\A) \) alone.
3. True or false, with a reason: \( \A \mapsto \max_{i,j}\lvert a_{ij}\rvert \) is a unitarily invariant norm on \( M_2(\nR) \).
4. Which axiom of @def-norm is the only hard one for \( \A \mapsto \Phi(\sigma(\A)) \), and which two earlier results prove it?
:::
::::

::: {.solution}
(a) A norm \( \uinorm{\cdot} \) on \( M_{m\times n}(F) \) with \( \uinorm{\U\A\V} = \uinorm{\A} \) for every \( \A \) and all unitary \( \U \in M_m(F) \) and \( \V \in M_n(F) \), the two chosen independently.

(b) Because \( \A = \U\vSigma\V^{*} \) with \( \vSigma = \diag_{m,n}(\sigma(\A)) \), so invariance gives \( \uinorm{\A} = \uinorm{\vSigma} \), a quantity built from \( \sigma(\A) \) alone (@lem-ui-norm-of-diagonal).

(c) False. It is a norm but not unitarily invariant: \( \I_2 \) and the rotation \( \U = \tfrac{1}{\sqrt2}\begin{psmallmatrix} 1 & -1\\ 1 & 1\end{psmallmatrix} \) have entrywise maxima \( 1 \) and \( 1/\sqrt2 \), while \( \U = \U\I_2\I_2 \).

(d) The triangle inequality (N3). It follows from @lem-singular-value-subadditive, which gives \( \sigma(\A+\B) \prec_w \sigma(\A)+\sigma(\B) \), together with @thm-gauge-monotone-under-majorization (b), which turns a weak majorization of non-negative vectors into an inequality of gauges.
:::

### B. Practice

:::: {#exr-unitarily-invariant-norms-b1}
[B1: Which of these are unitarily invariant norms]

Determine which of the following are unitarily invariant norms on \( M_2(\nR) \). Justify your answer, naming the clause that fails when one does.

::: {.enumerate options="label=(\alph*)"}
1. \( \uinorm{\A} = \sigma_1(\A) + \sigma_2(\A) \).
2. \( \uinorm{\A} = \lvert a_{11}\rvert + \lvert a_{12}\rvert + \lvert a_{21}\rvert + \lvert a_{22}\rvert \).
3. \( \uinorm{\A} = \bigl(\sigma_1(\A)^3 + \sigma_2(\A)^3\bigr)^{1/3} \).
4. \( \uinorm{\A} = \lvert\tr\A\rvert \).
5. \( \uinorm{\A} = \max\bigl(\sigma_1(\A),\ 2\sigma_2(\A)\bigr) \).
:::
::::

::: {.solution}
(a) Yes: this is the trace norm, the Ky Fan \( 2 \)-norm of @def-ky-fan-norm, equivalently \( \uinorm{\cdot}_{S_1} \) of @exm-schatten-norms. Alternatively, it is \( \Phi(\sigma(\A)) \) for \( \Phi = \norm{\cdot}_1 \), so @thm-von-neumann-correspondence applies.

(b) No. It is a norm — the \( 1 \)-norm of the entry list — but it is not unitarily invariant: it gives \( \I_2 \) the value \( 2 \) and the rotation \( \U \) above the value \( 4/\sqrt2 = 2\sqrt2 \), although \( \sigma(\I_2) = \sigma(\U) = (1,1) \).

(c) Yes: it is \( \Phi(\sigma(\A)) \) for \( \Phi = \norm{\cdot}_3 \), a symmetric gauge by @exm-symmetric-gauge-examples (a), so @thm-von-neumann-correspondence applies. This is the Schatten \( 3 \)-norm.

(d) No. It is unitarily *similarity* invariant but not a norm: \( \tr\begin{psmallmatrix} 1 & 0\\ 0 & -1\end{psmallmatrix} = 0 \) with the matrix non-zero, so (N1) fails. It is not unitarily invariant either, since \( \tr(\U\A\V) \) generally differs from \( \tr\A \).

(e) No. By @thm-von-neumann-correspondence the question is whether \( \Phi(\x) = \max(\lvert x\rvert^{\downarrow}_1,\ 2\lvert x\rvert^{\downarrow}_2) \) is a symmetric gauge on \( \nR^2 \), and it is not a norm: subadditivity fails. Take \( \x = (1, \tfrac12) \) and \( \y = (\tfrac12, 1) \). Then \( \Phi(\x) = \max(1, 1) = 1 \) and \( \Phi(\y) = 1 \), while \( \x + \y = (\tfrac32, \tfrac32) \) gives \( \Phi(\x+\y) = \max(\tfrac32, 3) = 3 > 2 \). The failure is easy to see in the matrices as well: \( \diag(1, \tfrac12) \) and \( \diag(\tfrac12, 1) \) each get the value \( 1 \), and their sum \( \tfrac32\I_2 \) gets \( 3 \). The trap is that \( \x \mapsto 2\lvert x\rvert^{\downarrow}_2 \) is not a norm — it vanishes at \( \e_1 \) — so the maximum of it with \( \Phi_1 \) inherits nothing. Contrast exercise C1 below, where both members of the maximum are norms.
:::

:::: {#exr-unitarily-invariant-norms-b2}
[B2: Measuring one matrix in every way]

Let
\[
\A = \begin{pmatrix} 2 & 1 \\ 1 & 2\end{pmatrix} ,
\qquad
\B = \begin{pmatrix} 2 & -1 \\ -1 & 2\end{pmatrix} .
\]

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \sigma(\A) \) and \( \sigma(\B) \), and then \( \norm{\A}_2 \), \( \norm{\A}_F \), \( \uinorm{\A}_{(1)} \) and \( \uinorm{\A}_{(2)} \).
2. Compute \( \sigma(\A+\B) \) and verify \( \sigma(\A+\B) \prec_w \sigma(\A)+\sigma(\B) \) directly, saying for which \( k \) the inequality is strict.
3. Verify @prp-ui-norm-properties (c) for \( \A \) and the Frobenius norm, and check that the Frobenius norm is normalized.
:::
::::

::: {.solution}
(a) \( \A \) is real symmetric with eigenvectors \( (1,1) \) and \( (1,-1) \) for the eigenvalues \( 3 \) and \( 1 \). Hence \( \A^{*}\A = \A^{2} \) has eigenvalues \( 9 \) and \( 1 \), and @def-singular-values gives \( \sigma(\A) = (3,1) \), as in @exm-schatten-norms. Likewise \( \B \) has eigenvectors \( (1,-1) \) and \( (1,1) \) for \( 3 \) and \( 1 \), so \( \sigma(\B) = (3,1) \). Hence \( \norm{\A}_2 = 3 \), \( \norm{\A}_F = \sqrt{9+1} = \sqrt{10} \) (which agrees with \( \sqrt{4+1+1+4} \)), \( \uinorm{\A}_{(1)} = 3 \) and \( \uinorm{\A}_{(2)} = 4 \).

(b) \( \A + \B = \diag(4,4) \), so \( \sigma(\A+\B) = (4,4) \), while \( \sigma(\A)+\sigma(\B) = (6,2) \). The partial sums are \( 4, 8 \) against \( 6, 8 \): strict at \( k = 1 \), equality at \( k = 2 \). So \( \sigma(\A+\B) \prec_w \sigma(\A)+\sigma(\B) \), and here the totals happen to agree, so the relation is even a majorization.

(c) The Frobenius norm has \( \norm{\e_1\e_1\tp}_F = 1 \), so it is normalized. The chain reads \( 3 = \norm{\A}_2 \le \sqrt{10} \le 4 = \uinorm{\A}_{(2)} \), and \( 9 \le 10 \le 16 \) confirms it.
:::

:::: {#exr-unitarily-invariant-norms-b3}
[B3: Moving a factor across]

Let \( \A \in M_{m\times n}(F) \), let \( \uinorm{\cdot} \) be a unitarily invariant norm on \( M_{m\times n}(F) \), and let \( P \) be an orthogonal projection of \( F^m \) onto a subspace, with matrix \( \P \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \norm{\P}_2 \le 1 \).
2. Deduce that \( \uinorm{\P\A} \le \uinorm{\A} \).
3. Give an example with \( m = n = 2 \) in which the inequality in (b) is strict for the Frobenius norm.
:::
::::

::: {.solution}
(a) For \( \x \in F^m \), write \( \x = \P\x + (\x - \P\x) \), an orthogonal decomposition, so \( \norm{\x}^2 = \norm{\P\x}^2 + \norm{\x - \P\x}^2 \ge \norm{\P\x}^2 \) by @thm-pythagoras. Hence \( \norm{\P\x} \le \norm{\x} \) for every \( \x \), and \( \norm{\P}_2 \le 1 \) by @def-operator-norm.

(b) By @prp-ui-norm-properties (b) with \( \X = \P \), \( \uinorm{\P\A} \le \norm{\P}_2\uinorm{\A} \le \uinorm{\A} \).

(c) Take \( \P = \e_1\e_1\tp \) and \( \A = \I_2 \). Then \( \P\A = \e_1\e_1\tp \) has \( \norm{\P\A}_F = 1 \), while \( \norm{\I_2}_F = \sqrt2 \).
:::

### C. Going deeper

:::: {#exr-unitarily-invariant-norms-c1}
[C1: A gauge built from two Ky Fan gauges]

On \( \nR^p \) let \( \Phi(\x) = \max\bigl(\Phi_1(\x),\ \tfrac{2}{k}\Phi_k(\x)\bigr) \) for a fixed \( 2 \le k \le p \), with \( \Phi_1 \) and \( \Phi_k \) the Ky Fan gauges of @def-ky-fan-gauge.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \Phi \) is a symmetric gauge function.
2. Write down the unitarily invariant norm it induces on \( M_{m\times n}(F) \), and decide whether it is normalized.
3. For \( p = k = 2 \), show that \( \Phi(\x) = \max(\lvert x\rvert^{\downarrow}_1,\ \lvert x_1\rvert + \lvert x_2\rvert) = \lvert x_1\rvert + \lvert x_2\rvert \), and conclude that the norm of (b) is the trace norm in that case.
:::
::::

::: {.solution}
(a) A maximum of finitely many norms is a norm: it is non-negative, absolutely homogeneous and subadditive because each member is, and it vanishes only where all members do, hence only at \( \0 \). Here both members are symmetric gauges by @exm-symmetric-gauge-examples (b), and a maximum of permutation invariant and sign invariant functions has the same invariances. So \( \Phi \) satisfies @def-symmetric-gauge.

(b) By @thm-von-neumann-correspondence the induced norm is
\[
\uinorm{\A} = \max\Bigl(\sigma_1(\A),\ \tfrac{2}{k}\sum_{i\le k}\sigma_i(\A)\Bigr) .
\]
It is normalized: at \( \A = \e_1\e_1^{*} \) the singular values are \( 1, 0, \dots, 0 \), so the two candidates are \( 1 \) and \( 2/k \le 1 \), and the maximum is \( 1 \).

(c) With \( p = k = 2 \), \( \tfrac22\Phi_2(\x) = \lvert x_1\rvert + \lvert x_2\rvert \), which is at least \( \Phi_1(\x) = \lvert x\rvert^{\downarrow}_1 \). So \( \Phi = \norm{\cdot}_1 \), and the induced norm is \( \sigma_1(\A) + \sigma_2(\A) \), the trace norm.
:::

:::: {#exr-unitarily-invariant-norms-c2}
[C2: How much scaling submultiplicativity can stand]

Let \( c > 0 \) and consider \( N_c(\A) = c\,\norm{\A}_2 \) on \( M_n(F) \), \( n \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( N_c \) is a unitarily invariant norm for every \( c > 0 \), and compute its gauge.
2. Determine exactly which \( c \) make \( N_c \) submultiplicative. *Hint: test at \( \A = \B = \I_n \).*
3. Do the same for \( M_c(\A) = c\,\uinorm{\A}_{(n)} \), the scaled trace norm. Show that \( \A = \B = \I_n \) is now the **wrong** test matrix, and find one that gives the sharp answer.
:::
::::

::: {.solution}
(a) A positive multiple of a norm is a norm, and multiplying by \( c \) does not disturb \( N_c(\U\A\V) = N_c(\A) \). Its gauge is \( \x \mapsto N_c(\diag(\x)) = c\norm{\x}_\infty \), since the largest singular value of \( \diag(\x) \) is \( \norm{\x}_\infty \).

(b) Exactly \( c \ge 1 \). If \( c \ge 1 \), then \( N_c(\A\B) = c\norm{\A\B}_2 \le c\norm{\A}_2\norm{\B}_2 \le c^2\norm{\A}_2\norm{\B}_2 = N_c(\A)N_c(\B) \), using submultiplicativity of the spectral norm (@thm-operator-norm-properties (d)) and \( c \le c^2 \). If \( c < 1 \), take \( \A = \B = \I_n \): then \( N_c(\A\B) = c \) while \( N_c(\A)N_c(\B) = c^2 < c \).

(c) The answer is again exactly \( c \ge 1 \). Sufficiency: by @prp-ui-norm-properties (b) and (c), \( \uinorm{\A\B}_{(n)} \le \norm{\A}_2\uinorm{\B}_{(n)} \le \uinorm{\A}_{(n)}\uinorm{\B}_{(n)} \), so for \( c \ge 1 \),
\[
M_c(\A\B) = c\uinorm{\A\B}_{(n)} \le c\uinorm{\A}_{(n)}\uinorm{\B}_{(n)} \le c^{2}\uinorm{\A}_{(n)}\uinorm{\B}_{(n)} = M_c(\A)M_c(\B) .
\]
Necessity: at \( \A = \B = \I_n \) one gets \( M_c(\I_n) = cn \) and the requirement \( cn \le c^{2}n^{2} \), that is \( c \ge 1/n \) — a weaker condition, so for \( n \ge 2 \) the identity is the wrong test matrix. Take instead \( \A = \B = \e_1\e_1\tp \), which is idempotent with singular values \( 1, 0, \dots, 0 \). Then \( M_c(\A\B) = c \) while \( M_c(\A)M_c(\B) = c^{2} \), and \( c \le c^{2} \) forces \( c \ge 1 \). The moral: submultiplicativity is tested by matrices of the **smallest** rank, where the trace norm and the spectral norm agree, not by the identity, where they differ by a factor of \( n \).
:::

:::: {#exr-unitarily-invariant-norms-c3}
[C3: The correspondence in the smallest case]

::: {.enumerate options="label=(\alph*)"}
1. Describe all unitarily invariant norms on \( M_{1\times n}(F) \), the row vectors. *Hint: what is \( p \)?*
2. Deduce that on \( M_{1\times n}(F) \) every unitarily invariant norm is a positive multiple of the Euclidean norm of the row.
3. Explain why the answer to (a) does not contradict the existence of many different unitarily invariant norms on \( M_2(F) \).
:::
::::

::: {.solution}
(a) Here \( p = \min(1, n) = 1 \), so @thm-von-neumann-correspondence matches unitarily invariant norms on \( M_{1\times n}(F) \) with symmetric gauge functions on \( \nR^1 \). By @exm-symmetric-gauge-examples (c), every norm on \( \nR^1 \) is such a gauge, and each is \( \Phi(t) = c\lvert t\rvert \) with \( c > 0 \). So the unitarily invariant norms are exactly \( \A \mapsto c\,\sigma_1(\A) \), \( c > 0 \).

(b) A row vector \( \a\tp \) has \( \A^{*}\A = \conj{\a}\a\tp \) of rank at most \( 1 \), with the single non-zero eigenvalue \( \a^{*}\a = \norm{\a}_2^2 \); so \( \sigma_1(\A) = \norm{\a}_2 \). Hence every unitarily invariant norm on \( M_{1\times n}(F) \) is \( c\norm{\a}_2 \).

(c) Because the correspondence is with norms on \( \nR^{p} \), and \( p = 1 \) leaves only one shape. For \( M_2(F) \), \( p = 2 \), and there are many norms on \( \nR^2 \) that are permutation and sign invariant — the whole family \( \norm{\cdot}_q \) for \( 1 \le q \le \infty \), for instance, giving the Schatten norms of @exm-schatten-norms. The rigidity in (a) is a statement about \( \nR^1 \), not about matrices.
:::
