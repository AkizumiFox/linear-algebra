# Eigenvalues Move Continuously

Chapter 11 §01 proved that every complex matrix has diagonalizable matrices arbitrarily close to it (@cor-schur-normal-matrix-nearby), then admitted that the word "close" was doing work no definition supported, and handed the repair to this chapter. The repair is now in place: a norm on \( M_n(\nC) \) says how close two matrices are, and @cor-entrywise-convergence-is-the-convergence says that it does not matter which norm. This section asks the question that could not even be posed before that point. If the matrix moves a little, how far do its eigenvalues move?

The answer has two halves, and the second is the one worth remembering. The eigenvalues do move only a little — provided they are read as an unordered list, which is the only way they can be read. But "a little" is not proportional to the movement of the matrix, and for a matrix with a large Jordan block it is spectacularly larger.

**Throughout, matrices are complex**, as in Section 4, so that an \( n \times n \) matrix always has exactly \( n \) eigenvalues counted with algebraic multiplicity (@cor-complex-polynomial-splits).

## From matrices to polynomials

The eigenvalues of \( \A \) are the roots of \( p_{\A} \) (@thm-eigenvalue-characterizations), with algebraic multiplicity meaning multiplicity as a root (@def-algebraic-multiplicity). So the question splits in two: do the coefficients of \( p_{\A} \) move a little when \( \A \) does, and do the roots of a polynomial move a little when its coefficients do? The first half is easy and we do it now; the whole difficulty is in the second.

The reason the first half is easy is that everything in sight is a polynomial in the entries. It is worth isolating that observation once, because it will be used four times in this section.

::: {#lem-entrywise-polynomial-continuous}
[Polynomial Maps of the Entries Are Continuous]

Let \( \Phi \colon M_{p \times q}(\nC) \to M_{r \times s}(\nC) \) be a map each of whose output entries is given by a fixed polynomial, with complex coefficients, in the \( pq \) entries of the input. Fix any norm on the source and any norm on the target. Then \( \Phi \) is **continuous**: whenever \( \norm{\A_k - \A} \to 0 \) we have \( \norm{\Phi(\A_k) - \Phi(\A)} \to 0 \), and equivalently, for every \( \A \) and every \( \varepsilon > 0 \) there is \( \delta > 0 \) such that \( \norm{\B - \A} < \delta \) forces \( \norm{\Phi(\B) - \Phi(\A)} < \varepsilon \). The same holds for a map into \( \nC \).
:::

::: {.idea}
Two reductions and one piece of arithmetic. Convergence in any norm is entrywise convergence, by @cor-entrywise-convergence-is-the-convergence, in the source and in the target alike; so the claim is about \( pq \) complex sequences producing \( rs \) complex sequences. That reduces it to the statement that a polynomial in finitely many complex variables respects limits, which is the algebra of limits.
:::

::: {.proof}
Suppose \( \norm{\A_k - \A} \to 0 \). By @cor-entrywise-convergence-is-the-convergence, each entry \( (\A_k)_{ij} \to a_{ij} \). Sums and products of convergent complex sequences converge to the sum and the product of the limits: for sums this is @thm-complex-triangle-inequality, and for products it follows from
\[
\lvert z_kw_k - zw \rvert \le \lvert z_k \rvert\,\lvert w_k - w \rvert + \lvert w \rvert\,\lvert z_k - z \rvert
\]
together with the fact that a convergent sequence is bounded. A polynomial is built from its variables and constants by finitely many sums and products, so each entry of \( \Phi(\A_k) \) converges to the corresponding entry of \( \Phi(\A) \). Applying @cor-entrywise-convergence-is-the-convergence in \( M_{r \times s}(\nC) \) gives \( \norm{\Phi(\A_k) - \Phi(\A)} \to 0 \).

For the equivalence of the two formulations, suppose the \( \varepsilon \)–\( \delta \) statement failed at some \( \A \) for some \( \varepsilon > 0 \). Then for each \( k \ge 1 \) the value \( \delta = 1/k \) is not good enough, so there is \( \B_k \) with \( \norm{\B_k - \A} < 1/k \) and \( \norm{\Phi(\B_k) - \Phi(\A)} \ge \varepsilon \). The sequence \( (\B_k) \) contradicts the sequential statement just proved. This proves the lemma.
:::

Now the first half of the question is answered. Write \( p_{\A}(x) = x^n + c_{n-1}(\A)x^{n-1} + \dots + c_0(\A) \), which is legitimate because \( p_{\A} \) is monic of degree \( n \) (@thm-charpoly-coefficients). Each \( c_j \) is a polynomial in the entries of \( \A \): the Leibniz sum of @def-characteristic-polynomial expresses \( \det(x\I - \A) \) as a signed sum of products of the entries of \( x\I - \A \), each of which is \( x - a_{jj} \) or \( -a_{ij} \), and collecting the powers of \( x \) leaves every coefficient a polynomial with integer coefficients in the \( a_{ij} \). So \( \A \mapsto (c_0(\A), \dots, c_{n-1}(\A)) \) is continuous by @lem-entrywise-polynomial-continuous.

That leaves the second half: roots against coefficients. Before stating what is true there, we settle what cannot be true.

## Why the answer must be about the multiset

The statement a reader would write down first is *"each eigenvalue is a continuous function of the matrix"*. It is not merely unproved; it is meaningless as written, because the eigenvalues come with no numbering — and the natural repair, "there is a way of numbering them that makes each one continuous", is false. One two-by-two family shows it, and the failure is the ordinary square root.

::: {#prp-no-continuous-root-selection}
[There Is No Continuous Choice of a Single Eigenvalue]

For \( t \in \nC \) put
\[
\A(t) = \begin{pmatrix} 0 & 1 \\ t & 0 \end{pmatrix},
\]
so that \( p_{\A(t)}(x) = x^2 - t \) and the eigenvalues of \( \A(t) \) are the two square roots of \( t \). Then there is **no** continuous function \( \lambda \colon D \to \nC \) on the closed unit disc \( D = \{t \in \nC : \lvert t\rvert \le 1\} \) such that \( \lambda(t) \) is an eigenvalue of \( \A(t) \) for every \( t \in D \). Consequently there is no continuous \( \Lambda \colon M_2(\nC) \to \nC \) with \( \Lambda(\B) \in \spec(\B) \) for every \( \B \).
:::

::: {.idea}
Walk \( t \) once around the unit circle. The two roots \( \pm\sqrt{t} \) trade places on the way round, so a choice that is continuous along the walk comes home as the *other* root. The bookkeeping is done by dividing the chosen root by one fixed root, which turns the walk into a continuous function with only the two values \( 1 \) and \( -1 \); on an interval such a function cannot jump, and it must.
:::

::: {.proof}
The characteristic polynomial is \( \det\begin{psmallmatrix} x & -1 \\ -t & x\end{psmallmatrix} = x^2 - t \), so \( \mu \) is an eigenvalue of \( \A(t) \) if and only if \( \mu^2 = t \) (@thm-eigenvalue-characterizations).

Suppose such a \( \lambda \) exists, so \( \lambda(t)^2 = t \) for all \( \lvert t \rvert \le 1 \). Define \( g \colon [0, 2\pi] \to \nC \) by
\[
g(\theta) = \lambda\bigl(e^{i\theta}\bigr)\,e^{-i\theta/2} .
\]
It is continuous, being a composite and a product of continuous functions — the elementary algebra of limits recorded in the chapter introduction, applied to \( \theta \mapsto e^{i\theta} \), to \( \lambda \), and to \( \theta \mapsto e^{-i\theta/2} \). Squaring,
\[
g(\theta)^2 = \lambda\bigl(e^{i\theta}\bigr)^2 e^{-i\theta} = e^{i\theta}e^{-i\theta} = 1 ,
\]
so \( g(\theta) \in \{1, -1\} \) for every \( \theta \). In particular \( g \) is real-valued, and a continuous real-valued function on an interval taking only the values \( 1 \) and \( -1 \) is constant: if it took both, the intermediate value theorem would produce a \( \theta \) with \( g(\theta) = 0 \). Hence \( g(2\pi) = g(0) \).

But \( e^{i \cdot 0} = e^{i \cdot 2\pi} = 1 \), so \( g(0) = \lambda(1) \) while \( g(2\pi) = \lambda(1)e^{-i\pi} = -\lambda(1) \). Therefore \( \lambda(1) = -\lambda(1) \), that is \( \lambda(1) = 0 \), contradicting \( \lambda(1)^2 = 1 \). So no such \( \lambda \) exists.

For the last sentence, if \( \Lambda \) were such a function then \( t \mapsto \Lambda(\A(t)) \) would be continuous, because \( t \mapsto \A(t) \) is continuous by @lem-entrywise-polynomial-continuous, and it would select an eigenvalue of \( \A(t) \) for each \( t \). This proves the proposition.
:::

The intermediate value theorem is quoted here, and it is the only place in this chapter that uses it; it is fact (A5) of the chapter introduction, borrowed and not proved.

Two things are worth reading off the argument. First, the obstruction is not exotic: \( \A(0) = \J_2(0) \) is the standard nilpotent matrix, and the trouble happens exactly at the parameter where the two eigenvalues collide. Second, nothing is wrong with the *pair* \( \{\sqrt t, -\sqrt t\} \), which shrinks to \( \{0, 0\} \) as \( t \to 0 \) in any reasonable sense. It is only the attempt to call one of them "the first" that fails. This is why the correct statement speaks of the roots as a **multiset**: a list with multiplicities and no order.

## The imported fact

Here is what is true. It is the one statement in this chapter that the book neither proves nor can prove with the tools it has built.

::: {#thm-roots-depend-continuously}
[Continuous Dependence of the Roots on the Coefficients]

Let \( n \ge 1 \) and let
\[
p(x) = x^n + c_{n-1}x^{n-1} + \dots + c_1x + c_0 \in \nC[x]
\]
be monic, with roots \( \mu_1, \dots, \mu_n \in \nC \) listed with multiplicity (@cor-complex-polynomial-splits). Let \( \varepsilon > 0 \). Then there is \( \delta > 0 \) with the following property. If
\[
q(x) = x^n + b_{n-1}x^{n-1} + \dots + b_1x + b_0
\]
is monic of the **same degree** \( n \) and \( \lvert b_j - c_j \rvert < \delta \) for every \( j \), then the roots \( \nu_1, \dots, \nu_n \) of \( q \), listed with multiplicity, can be **numbered** so that
\[
\lvert \nu_i - \mu_i \rvert < \varepsilon \qquad (i = 1, \dots, n).
\]
:::

**This book does not prove this theorem, and quotes it.** A proof needs complex analysis: one encircles each root of \( p \) by a small circle on which \( p \) does not vanish, counts the roots inside by a contour integral, and observes that an integer-valued quantity depending continuously on the coefficients cannot change. Nothing of that machinery is available here, and manufacturing a substitute would take a chapter. The statement is therefore recorded in the manner this book has used before — Chapter 13 §06 with Taylor's theorem, Chapter 10 with the theorem of Abel and Ruffini: named at the point of use, never buried inside a proof that presents itself as self-contained, and never strengthened in passing. What *can* be proved with the tools at hand is that the numbering in the statement has to be chosen afresh for each \( q \), and that was @prp-no-continuous-root-selection.

Two clauses of the statement carry weight. **Monic of the same degree** is essential: the roots of \( \delta x^2 + x \) are \( 0 \) and \( -1/\delta \), which runs off to infinity as \( \delta \to 0 \), while the limit polynomial \( x \) has the single root \( 0 \). Allowing the leading coefficient to vanish destroys everything, and monic polynomials of a fixed degree are exactly the family where it cannot. And **numbered so that** is the multiset formulation: the permutation matching up the two lists depends on \( q \), and @prp-no-continuous-root-selection says it must.

## Eigenvalues, and the spectral radius

Now the two halves are assembled.

::: {#cor-eigenvalues-continuous}
[Eigenvalues Depend Continuously on the Matrix]

Let \( \A \in M_n(\nC) \) with eigenvalues \( \lambda_1, \dots, \lambda_n \) listed with algebraic multiplicity, let \( \norm{\cdot} \) be any norm on \( M_n(\nC) \), and let \( \varepsilon > 0 \). Then there is \( \delta > 0 \) such that every \( \B \in M_n(\nC) \) with \( \norm{\B - \A} < \delta \) has eigenvalues \( \mu_1, \dots, \mu_n \), listed with algebraic multiplicity, which can be numbered so that \( \lvert \mu_i - \lambda_i \rvert < \varepsilon \) for every \( i \).
:::

::: {.idea}
The characteristic polynomial's coefficients are polynomials in the entries, so they move continuously with \( \A \); the quoted root theorem then moves the roots. The only work is composing the two estimates, choosing the tolerance for the coefficients small enough that the roots come out within \( \varepsilon \).
:::

::: {.proof}
By @thm-charpoly-coefficients the polynomials \( p_{\A} \) and \( p_{\B} \) are monic of degree \( n \), and by @thm-eigenvalue-characterizations together with @def-algebraic-multiplicity their root lists with multiplicity are the eigenvalue lists with algebraic multiplicity. Let \( \delta' > 0 \) be the number supplied by @thm-roots-depend-continuously for \( p = p_{\A} \) and this \( \varepsilon \). The map \( \B \mapsto (c_0(\B), \dots, c_{n-1}(\B)) \) is continuous by @lem-entrywise-polynomial-continuous, as noted after that lemma, so there is \( \delta > 0 \) such that \( \norm{\B - \A} < \delta \) forces \( \lvert c_j(\B) - c_j(\A) \rvert < \delta' \) for every \( j \). For such a \( \B \), @thm-roots-depend-continuously applies to \( q = p_{\B} \). This proves the corollary.
:::

The corollary says exactly as much as @thm-roots-depend-continuously and no more: the numbering is not canonical and depends on \( \B \). Any quantity that ignores the numbering, however, inherits honest continuity, and the spectral radius of Section 4 is the first example.

::: {.check}
Does @cor-eigenvalues-continuous make \( \rho \colon M_n(\nC) \to \nR \) continuous, given that no individual eigenvalue is a continuous function of \( \A \)?
:::

::: {.solution}
Yes. Let \( \varepsilon > 0 \) and take \( \delta \) from @cor-eigenvalues-continuous. If \( \norm{\B - \A} < \delta \), fix a numbering with \( \lvert \mu_i - \lambda_i \rvert < \varepsilon \). Then \( \lvert \mu_i \rvert \le \lvert \lambda_i \rvert + \varepsilon \le \rho(\A) + \varepsilon \) for each \( i \) by @def-spectral-radius, so \( \rho(\B) \le \rho(\A) + \varepsilon \); the same numbering read the other way gives \( \lvert\lambda_i\rvert \le \lvert\mu_i\rvert + \varepsilon \le \rho(\B) + \varepsilon \) for each \( i \), hence \( \rho(\A) \le \rho(\B) + \varepsilon \), so \( \lvert \rho(\B) - \rho(\A) \rvert \le \varepsilon \). The argument never names an individual eigenvalue, which is why it survives: \( \rho \) is a function of the multiset alone.
:::

## The limit argument, made routine

Chapter 11 §01 called @cor-schur-normal-matrix-nearby "the tool behind a standard strategy: *prove it for diagonalizable matrices, then take a limit*", and said that this chapter, "where matrices acquire norms and limits can be spoken of properly, runs arguments of exactly this shape". Here is the shape. It costs two corollaries, and afterwards the strategy is three lines every time.

::: {#cor-diagonalizable-dense-again}
[Diagonalizable Matrices Are Dense]

Let \( \norm{\cdot} \) be any norm on \( M_n(\nC) \). For every \( \A \in M_n(\nC) \) and every \( \varepsilon > 0 \) there is a **diagonalizable** \( \A' \in M_n(\nC) \) with \( \norm{\A - \A'} < \varepsilon \). Equivalently, every complex square matrix is the limit of a sequence of diagonalizable matrices, in every norm.
:::

::: {.idea}
Chapter 11 produced a diagonalizable matrix near \( \A \) with the *entries* close. "Close in every norm" is now the same thing, by @cor-entrywise-convergence-is-the-convergence, so the only task is to convert one tolerance into the other.
:::

::: {.proof}
Let \( N_{\infty}(\M) = \max_{i,j}\lvert m_{ij} \rvert \), which is a norm on \( M_n(\nC) \): it is the \( \infty \)-norm of @exm-p-norms read on the list of \( n^2 \) entries. By @thm-norm-equivalence there is \( C > 0 \) with \( \norm{\M} \le C\,N_{\infty}(\M) \) for every \( \M \). Apply @cor-schur-normal-matrix-nearby with the tolerance \( \varepsilon/C \): it supplies a diagonalizable \( \A' \) with \( \lvert a_{ij} - a'_{ij} \rvert < \varepsilon/C \) for all \( i, j \), hence with \( N_{\infty}(\A - \A') < \varepsilon/C \), a maximum of finitely many numbers each below that bound. Therefore \( \norm{\A - \A'} \le C\,N_{\infty}(\A - \A') < \varepsilon \). Taking \( \varepsilon = 1/k \) gives a sequence \( \A_k \) of diagonalizable matrices with \( \norm{\A - \A_k} \to 0 \). This proves the corollary.
:::

::: {#cor-identity-by-density}
[Proving an Identity by Density]

Let \( \Phi \colon M_n(\nC) \to M_{r \times s}(\nC) \) be a map each of whose output entries is a polynomial in the entries of the input. If \( \Phi(\A) = 0 \) for every **diagonalizable** \( \A \in M_n(\nC) \), then \( \Phi(\A) = 0 \) for every \( \A \in M_n(\nC) \).
:::

::: {.idea}
Both sides of the identity are continuous in \( \A \), and they agree on the diagonalizable matrices, which are dense. A continuous function is determined by its values on a dense set, so they agree everywhere.
:::

::: {.proof}
Fix \( \A \) and a norm on each side. By @cor-diagonalizable-dense-again choose diagonalizable \( \A_k \) with \( \norm{\A - \A_k} \to 0 \). By @lem-entrywise-polynomial-continuous, \( \norm{\Phi(\A_k) - \Phi(\A)} \to 0 \). Since \( \Phi(\A_k) = 0 \) by hypothesis, that says \( \norm{\Phi(\A)} \to 0 \); but \( \norm{\Phi(\A)} \) does not depend on \( k \), so \( \norm{\Phi(\A)} = 0 \) and \( \Phi(\A) = 0 \) by the positivity clause of @def-norm. This proves the corollary.
:::

The hypothesis "each output entry is a polynomial in the input entries" is the one to check, and it is usually free: any expression built from \( \A \) by addition, multiplication, transposition, conjugate transposition of a real matrix, determinants, adjugates, traces and the coefficients of \( p_{\A} \) qualifies. What does *not* qualify is anything built from an inverse, an eigenvector or a choice of ordering. Here is the strategy in action, on the theorem that Chapter 8 proved the long way.

::: {#exm-cayley-hamilton-by-density}
[Cayley–Hamilton, by a limit]

Prove that \( p_{\A}(\A) = 0 \) for every \( \A \in M_n(\nC) \), using density rather than the adjugate identity of @thm-adjugate-identity.
:::

::: {.solution}
Put \( \Phi(\A) = p_{\A}(\A) \). Each entry of \( \Phi(\A) \) is a polynomial in the entries of \( \A \): the coefficients \( c_j(\A) \) are, as noted after @lem-entrywise-polynomial-continuous, and \( \Phi(\A) = \A^n + c_{n-1}(\A)\A^{n-1} + \dots + c_0(\A)\I \) is then built from them by products and sums.

Let \( \A \) be diagonalizable, say \( \A = \P\D\P^{-1} \) with \( \D = \diag(d_1, \dots, d_n) \). By @thm-powers-diagonalizable, \( p_{\A}(\A) = \P\,\diag\bigl(p_{\A}(d_1), \dots, p_{\A}(d_n)\bigr)\,\P^{-1} \). Each \( d_i \) is an eigenvalue of \( \A \), hence a root of \( p_{\A} \) (@thm-eigenvalue-characterizations), so every diagonal entry is \( 0 \) and \( \Phi(\A) = 0 \).

By @cor-identity-by-density, \( \Phi(\A) = 0 \) for every \( \A \in M_n(\nC) \), which is @thm-cayley-hamilton over \( \nC \).
:::

That is the whole strategy: check the identity where the matrix is diagonal in some basis, where everything is a scalar computation, and let density carry it to the rest. It proves nothing new here — @thm-cayley-hamilton holds over every field, and the density argument is confined to \( \nC \) — but the three lines at the end are the part to transfer. @exr-continuity-of-eigenvalues-c2 runs the same argument with a different dense set.

## The warning: continuous is not Lipschitz

Everything so far has been qualitative. The quantitative question is whether there is a constant \( L \) with
\[
\text{(eigenvalue movement)} \;\le\; L\,\norm{\B - \A} ,
\]
which is what "continuous" is usually imagined to mean and what a numerical analyst actually needs. There is not, and the failure is severe.

::: {#exm-jordan-block-perturbation}
[A Jordan block's eigenvalues move like \( \varepsilon^{1/k} \)]

Let \( k \ge 2 \), let \( \varepsilon > 0 \), and perturb the nilpotent Jordan block in its bottom left corner:
\[
\A = \J_k(0), \qquad \A_{\varepsilon} = \J_k(0) + \varepsilon\E_{k1} .
\]
Find the eigenvalues of \( \A_{\varepsilon} \) and compare their distance from \( \spec(\A) = \{0\} \) with \( \norm{\A_{\varepsilon} - \A} \).
:::

::: {.solution}
*The characteristic polynomial is \( x^k - \varepsilon \).* Write \( \M = x\I - \A_{\varepsilon} \), so \( \M \) has \( x \) on the diagonal, \( -1 \) on the superdiagonal, \( -\varepsilon \) in position \( (k, 1) \), and zeros elsewhere. Expand along the first column (@thm-laplace-expansion (a)), whose only non-zero entries are \( m_{11} = x \) and \( m_{k1} = -\varepsilon \).

Deleting row \( 1 \) and column \( 1 \) leaves the \( (k-1) \times (k-1) \) upper triangular matrix with \( x \) on the diagonal, of determinant \( x^{k-1} \) (@thm-det-triangular). Deleting row \( k \) and column \( 1 \) leaves the matrix with rows \( 1, \dots, k-1 \) and columns \( 2, \dots, k \) of \( \M \); its \( (i, j) \) entry is \( m_{i, j+1} \), which is \( -1 \) when \( j = i \) and \( x \) when \( i = j + 1 \), so it is lower triangular with \( -1 \) all along its diagonal and determinant \( (-1)^{k-1} \). The cofactor signs are \( (-1)^{1+1} = 1 \) and \( (-1)^{k+1} \), so
\[
\det\M = x \cdot x^{k-1} + (-\varepsilon)(-1)^{k+1}(-1)^{k-1} = x^{k} - \varepsilon ,
\]
since \( (-1)^{k+1}(-1)^{k-1} = (-1)^{2k} = 1 \).

*The eigenvalues.* They are the \( k \)-th roots of \( \varepsilon \), namely \( \varepsilon^{1/k}e^{2\pi i j/k} \) for \( j = 0, \dots, k-1 \), each of modulus \( \varepsilon^{1/k} \). For \( k = 2 \) this is the pair \( \pm\sqrt{\varepsilon} \), and \( \A_{\varepsilon} \) is the matrix \( \A(\varepsilon) \) of @prp-no-continuous-root-selection.

*The comparison.* The perturbation \( \E = \varepsilon\E_{k1} \) has a single non-zero entry, so its largest absolute row sum and largest absolute column sum are both \( \varepsilon \), and \( \E^{*}\E = \varepsilon^2\E_{11} \) has largest eigenvalue \( \varepsilon^2 \); hence \( \norm{\E}_1 = \norm{\E}_{\infty} = \norm{\E}_2 = \varepsilon \) by @thm-operator-norm-formulas. Every eigenvalue of \( \A \) is \( 0 \), so the eigenvalues have moved a distance \( \varepsilon^{1/k} \) while the matrix moved a distance \( \varepsilon \). The ratio is
\[
\frac{\varepsilon^{1/k}}{\varepsilon} = \varepsilon^{-(k-1)/k} \xrightarrow[\;\varepsilon \to 0^{+}\;]{} \infty .
\]

*A by-product worth keeping.* The \( k \) roots \( \varepsilon^{1/k}e^{2\pi ij/k} \) are **distinct** for every \( \varepsilon > 0 \), so \( \A_{\varepsilon} \) has \( k \) distinct eigenvalues and is diagonalizable by @cor-distinct-eigenvalues-diagonalizable. A single nilpotent Jordan block, which is as far from diagonalizable as a matrix gets, therefore has diagonalizable matrices arbitrarily close to it, and here they are written down. That is @cor-diagonalizable-dense-again made concrete for one family.
:::

Put numbers on it. For \( k = 2 \) and \( \varepsilon = 10^{-6} \) the matrix moves by one part in a million and the eigenvalues move to \( \pm 10^{-3} \): an amplification of a thousand. For \( k = 10 \) and \( \varepsilon = 10^{-10} \) the matrix moves by \( 10^{-10} \) and the eigenvalues land on the circle of radius \( 10^{-1} \), an amplification of a billion. No constant \( L \) survives this, so the continuity of @cor-eigenvalues-continuous cannot be upgraded to a Lipschitz bound, and the \( \delta \) it produces genuinely depends on \( \A \) and not only on \( n \).

::: {.warning}
**Continuous does not mean stable.** @cor-eigenvalues-continuous guarantees that a small enough perturbation moves the eigenvalues a little, and says nothing whatever about how small "small enough" is. For \( \J_{10}(0) \) a perturbation of size \( 10^{-10} \) — the kind of change one would call negligible in data recorded to ten digits — scatters the eigenvalues over a circle of radius \( 0.1 \). Reading a printed eigenvalue of a matrix with a large Jordan block as a property of the matrix, rather than of the matrix plus whatever noise reached it, is the mistake this example exists to prevent.
:::

The opposite extreme is worth seeing beside it. Take the Hermitian \( \A = \diag(1, 2) \) and the Hermitian perturbation \( \E = \varepsilon(\E_{12} + \E_{21}) \), of norm \( \norm{\E}_2 = \varepsilon \). The matrix \( \A + \E = \begin{psmallmatrix} 1 & \varepsilon \\ \varepsilon & 2 \end{psmallmatrix} \) has trace \( 3 \) and determinant \( 2 - \varepsilon^2 \), so its eigenvalues are
\[
\frac{3 \pm \sqrt{1 + 4\varepsilon^2}}{2} ,
\]
and since \( \sqrt{1 + u} \le 1 + u/2 \) for \( u \ge 0 \), each of them lies within \( \varepsilon^2 \) of the corresponding eigenvalue of \( \A \). Here the eigenvalues move *less* than the matrix does, by a whole order in \( \varepsilon \). That is not an accident of the example: Chapter 16 proves that the eigenvalues of a Hermitian matrix move by at most \( \norm{\E}_2 \) under a Hermitian perturbation, and Chapter 19 proves the theorem of Bauer and Fike, which bounds the movement for a diagonalizable matrix by \( \norm{\E}_2 \) times a factor measuring how far its eigenvector basis is from orthonormal.

So the exponent \( 1/k \) in @exm-jordan-block-perturbation is not about size; it is about shape. It is decided by the largest Jordan block at the eigenvalue (@thm-jordan-canonical-form), and block size is precisely what Chapter 11 §11 was measuring when @exm-defect-jordan-block computed
\[
\Delta(\J_k(\lambda)) = \sqrt{k - 1}
\]
for the departure from normality of @def-departure-from-normality. The two statements match at both ends: \( \Delta = 0 \) exactly for the normal matrices, whose eigenvalues are the stable ones, and \( \Delta \) grows with the block that makes them fragile. They do not match in between, and it would be wrong to read \( \Delta \) as a formula for the exponent — \( \Delta \) is one number for the whole matrix, so it cannot report which eigenvalue carries which block, and @exm-defect-jordan-block records that it does not depend on \( \lambda \) at all. What \( \Delta(\A) \) does is tell you whether the question needs asking at all.

## Exercises

### A. Check your understanding

:::: {#exr-continuity-of-eigenvalues-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State @thm-roots-depend-continuously, paying attention to the two hypotheses on \( q \).
2. Explain in one sentence why the theorem is stated for the multiset of roots rather than for a list of \( n \) individual roots.
3. Decide whether the following is correct, and justify your answer: "the function sending \( \A \in M_2(\nC) \) to its eigenvalue of largest modulus is continuous".
4. For the \( k \times k \) Jordan block, how far do the eigenvalues move under a perturbation of norm \( \varepsilon \), and what does that say about a Lipschitz bound?
:::
::::

::: {.solution}
(a) See @thm-roots-depend-continuously. The two hypotheses are that \( q \) is **monic** and of the **same degree** \( n \) as \( p \); without them the roots can escape to infinity, as \( \delta x^2 + x \) shows.

(b) Because no continuous choice of an individual root exists: @prp-no-continuous-root-selection shows that following one square root of \( t \) once around the unit circle returns the other one, so the matching numbering must be allowed to depend on \( q \).

(c) Incorrect as stated, because a matrix can have two eigenvalues of equal largest modulus and then the phrase does not name a number; and incorrect even where it does name a number, since \( \A(t) \) of @prp-no-continuous-root-selection has the two eigenvalues \( \pm\sqrt t \) of equal modulus for every \( t \ne 0 \). The modulus itself, that is \( \rho \), is continuous — see the Quick check.

(d) They move a distance \( \varepsilon^{1/k} \) (@exm-jordan-block-perturbation), so the ratio of eigenvalue movement to matrix movement is \( \varepsilon^{-(k-1)/k} \), which is unbounded as \( \varepsilon \to 0^{+} \). No Lipschitz constant exists.
:::

### B. Practice

:::: {#exr-continuity-of-eigenvalues-b1}
[B1: Two perturbations of the same size]

Let \( \varepsilon = 10^{-8} \). Compute the eigenvalues of
\[
\B = \begin{pmatrix} 0 & 1 \\ \varepsilon & 0 \end{pmatrix}
\qquad\text{and}\qquad
\C = \begin{pmatrix} \varepsilon & 1 \\ 0 & 0 \end{pmatrix},
\]
each of which differs from \( \J_2(0) \) by a matrix of \( 2 \)-norm \( \varepsilon \). Hence explain why the constant in @cor-eigenvalues-continuous cannot depend on \( \norm{\B - \A} \) alone.
::::

::: {.solution}
For \( \B \): \( p_{\B}(x) = x^2 - \varepsilon \) by @exm-jordan-block-perturbation with \( k = 2 \), so the eigenvalues are \( \pm 10^{-4} \).

For \( \C \): the matrix is upper triangular, so its eigenvalues are its diagonal entries \( \varepsilon = 10^{-8} \) and \( 0 \) (@thm-diagonal-of-triangular-form (b)).

Both perturbations have \( 2 \)-norm \( \varepsilon = 10^{-8} \), since each is \( \varepsilon \) times a single matrix unit. The eigenvalues of \( \B \) have moved \( 10^{-4} \) from \( \spec(\J_2(0)) = \{0\} \), those of \( \C \) only \( 10^{-8} \): a factor of \( 10^{4} \) between two perturbations of exactly the same size. So the movement is not a function of \( \norm{\E} \), and the \( \delta \) of @cor-eigenvalues-continuous cannot be computed from \( \varepsilon \) and \( n \) alone.
:::

:::: {#exr-continuity-of-eigenvalues-b2}
[B2: A diagonalizable neighbor, explicitly]

Let \( \A = \begin{pmatrix} 2 & 1 \\ 0 & 2\end{pmatrix} \) and let \( \varepsilon > 0 \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \A \) is not diagonalizable.
2. Exhibit a diagonalizable \( \A' \) with \( \norm{\A - \A'}_2 < \varepsilon \), and say which theorem certifies that your \( \A' \) is diagonalizable.
3. What are the eigenvalues of your \( \A' \), and how far have they moved?
:::
::::

::: {.solution}
(a) The only eigenvalue is \( 2 \), with algebraic multiplicity \( 2 \) (@thm-diagonal-of-triangular-form (b)). But \( \A - 2\I = \begin{psmallmatrix} 0 & 1 \\ 0 & 0\end{psmallmatrix} \) has rank \( 1 \), so \( g_{\A}(2) = 1 < 2 = a_{\A}(2) \) and \( \A \) is not diagonalizable by @thm-diagonalization (e).

(b) Take \( \delta \) with \( 0 < \delta < \varepsilon \) and \( \A' = \begin{psmallmatrix} 2 & 1 \\ 0 & 2 + \delta\end{psmallmatrix} \). It is upper triangular with distinct diagonal entries \( 2 \) and \( 2 + \delta \), hence has two distinct eigenvalues (@thm-diagonal-of-triangular-form (b)) and is diagonalizable by @cor-distinct-eigenvalues-diagonalizable. And \( \A - \A' = -\delta\E_{22} \), so \( \norm{\A - \A'}_2 = \delta < \varepsilon \) by @thm-operator-norm-formulas (c).

(c) They are \( 2 \) and \( 2 + \delta \). One eigenvalue has not moved and the other has moved \( \delta \), which is exactly \( \norm{\A - \A'}_2 \): here the movement is Lipschitz with constant \( 1 \). The failure in @exm-jordan-block-perturbation needed a perturbation *below* the diagonal, which is the direction a triangular form cannot absorb.
:::

:::: {#exr-continuity-of-eigenvalues-b3}
[B3: The determinant and the trace, by density]

Let \( \A, \B \in M_n(\nC) \). Use @cor-identity-by-density to prove that \( \tr(\A\B) = \tr(\B\A) \) — after first checking that the map in question satisfies the hypothesis of that corollary — and then explain why this is a bad way to prove it.
::::

::: {.solution}
Fix \( \B \) and put \( \Phi(\A) = \tr(\A\B) - \tr(\B\A) \), a \( 1 \times 1 \) matrix whose single entry is \( \sum_{i,j}(a_{ij}b_{ji} - b_{ij}a_{ji}) \), a polynomial in the entries of \( \A \); so the hypothesis of @cor-identity-by-density holds.

Let \( \A = \P\D\P^{-1} \) be diagonalizable, \( \D = \diag(d_1, \dots, d_n) \), and put \( \X = \P^{-1}\B\P \). By @thm-trace-similarity-invariant, similar matrices have equal traces, and \( \A\B = \P(\D\X)\P^{-1} \) while \( \B\A = \P(\X\D)\P^{-1} \), so \( \tr(\A\B) = \tr(\D\X) \) and \( \tr(\B\A) = \tr(\X\D) \). For a diagonal \( \D \) both of those are \( \sum_i d_ix_{ii} \), by inspection of the diagonal entries of the two products. Hence \( \Phi(\A) = 0 \) for every diagonalizable \( \A \), and @cor-identity-by-density extends it to every \( \A \).

It is a bad way to prove it because the identity is a two-line computation from the definition, \( \tr(\A\B) = \sum_{i,j}a_{ij}b_{ji} = \tr(\B\A) \), valid over every field; the density argument needs \( \nC \), an imported theorem and two corollaries, and delivers less. A density argument earns its keep only when the diagonalizable case is genuinely easier, as in @exm-cayley-hamilton-by-density.
:::

### C. Going deeper

:::: {#exr-continuity-of-eigenvalues-c1}
[C1: How close to singular a nearby eigenvalue forces you to be]

Let \( \A \in M_n(\nC) \), let \( \norm{\cdot} \) be an operator norm on \( M_n(\nC) \) (@def-operator-norm) and let \( \E \in M_n(\nC) \) with \( \E \neq 0 \).

::: {.enumerate options="label=(\alph*)"}
1. Suppose \( \mu \) is an eigenvalue of \( \A + \E \) and \( \mu \notin \spec(\A) \). Prove that
   \[
   \norm{(\A - \mu\I)^{-1}} \ge \frac{1}{\norm{\E}} .
   \]
2. Deduce that if \( \norm{(\A - z\I)^{-1}} \le M \) for every \( z \) with \( \lvert z - \lambda\rvert = r \), then no eigenvalue of \( \A + \E \) lies on that circle as soon as \( \norm{\E} < 1/M \).
:::

*Hint: for (a), factor \( \A + \E - \mu\I \) and use @thm-neumann-series.*
::::

::: {.solution}
(a) Since \( \mu \notin \spec(\A) \), the matrix \( \A - \mu\I \) is invertible (@thm-eigenvalue-characterizations). Write
\[
\A + \E - \mu\I = (\A - \mu\I)\bigl(\I + (\A - \mu\I)^{-1}\E\bigr) .
\]
The left side is singular, because \( \mu \) is an eigenvalue of \( \A + \E \). The first factor on the right is invertible, so the second factor is singular: a product with an invertible left factor is invertible as soon as the right factor is. Put \( \X = -(\A - \mu\I)^{-1}\E \), so \( \I - \X \) is singular. By @thm-neumann-series, \( \norm{\X} < 1 \) would make \( \I - \X \) invertible; hence \( \norm{\X} \ge 1 \). Submultiplicativity (@thm-operator-norm-properties) gives
\[
1 \le \norm{\X} \le \norm{(\A - \mu\I)^{-1}}\,\norm{\E},
\]
and dividing by \( \norm{\E} > 0 \) gives the claim.

(b) Suppose \( \mu \) is an eigenvalue of \( \A + \E \) with \( \lvert \mu - \lambda \rvert = r \). Then \( \norm{(\A - \mu\I)^{-1}} \le M \) by hypothesis, and in particular \( \A - \mu\I \) is invertible, so \( \mu \notin \spec(\A) \) and part (a) applies: \( M \ge 1/\norm{\E} \), that is \( \norm{\E} \ge 1/M \). Contrapositively, \( \norm{\E} < 1/M \) leaves no eigenvalue of \( \A + \E \) on the circle.
:::

:::: {#exr-continuity-of-eigenvalues-c2}
[C2: Density of the invertible matrices, and \( \A\B \) versus \( \B\A \)]

::: {.enumerate options="label=(\alph*)"}
1. Prove that for every \( \A \in M_n(\nC) \) and every \( \varepsilon > 0 \) there is an **invertible** \( \A' \) with \( \norm{\A - \A'} < \varepsilon \), in any norm. *Hint: consider \( \A - t\I \).*
2. Prove a version of @cor-identity-by-density with "invertible" in place of "diagonalizable".
3. Hence give a second proof that \( p_{\A\B} = p_{\B\A} \) for all \( \A, \B \in M_n(\nC) \), a statement first proved in @thm-ab-ba-eigenvalues (b).
:::
::::

::: {.solution}
(a) The matrix \( \A - t\I \) is singular exactly when \( t \in \spec(\A) \) (@thm-eigenvalue-characterizations), and \( \spec(\A) \) has at most \( n \) elements. Let \( N_{\infty} \) and \( C \) be as in the proof of @cor-diagonalizable-dense-again, so \( \norm{\M} \le C\,N_{\infty}(\M) \). Choose \( t \ne 0 \) with \( \lvert t \rvert < \varepsilon/C \) and \( t \notin \spec(\A) \), possible because the disc of radius \( \varepsilon/C \) is infinite and only finitely many of its points are forbidden. Then \( \A' = \A - t\I \) is invertible and \( N_{\infty}(\A - \A') = \lvert t \rvert \), so \( \norm{\A - \A'} < \varepsilon \).

(b) Verbatim the proof of @cor-identity-by-density, with the sequence of diagonalizable matrices replaced by the sequence of invertible matrices supplied by (a) with \( \varepsilon = 1/k \).

(c) Fix \( \B \) and set \( \Phi(\A) = \bigl(c_0(\A\B) - c_0(\B\A), \dots, c_{n-1}(\A\B) - c_{n-1}(\B\A)\bigr) \), a row of \( n \) entries. Each entry of \( \A\B \) and of \( \B\A \) is a polynomial in the entries of \( \A \), and each \( c_j \) is a polynomial in the entries of its argument, so \( \Phi \) satisfies the hypothesis of (b). For invertible \( \A \) we have \( \B\A = \A^{-1}(\A\B)\A \), so \( \A\B \) and \( \B\A \) are similar and \( p_{\A\B} = p_{\B\A} \) by @thm-charpoly-similarity-invariant; that is exactly \( \Phi(\A) = 0 \), and it is @exr-characteristic-polynomial-b3 (a). By (b), \( \Phi(\A) = 0 \) for every \( \A \), and two monic polynomials of degree \( n \) with the same lower coefficients are equal.
:::

:::: {#exr-continuity-of-eigenvalues-c3}
[C3: Distinct eigenvalues is an open condition]

Let \( \A \in M_n(\nC) \) have \( n \) **distinct** eigenvalues \( \lambda_1, \dots, \lambda_n \), and let \( \norm{\cdot} \) be a norm on \( M_n(\nC) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that there is \( \delta > 0 \) such that every \( \B \) with \( \norm{\B - \A} < \delta \) also has \( n \) distinct eigenvalues, and is therefore diagonalizable.
2. Deduce that the set of matrices in \( M_n(\nC) \) with a repeated eigenvalue contains no ball, that is, that its complement is dense.
3. Is the set of diagonalizable matrices open? Justify your answer.
:::
::::

::: {.solution}
(a) Put \( 2\varepsilon = \min_{i \ne j}\lvert \lambda_i - \lambda_j \rvert \), which is positive because the \( \lambda_i \) are distinct and there are finitely many pairs. Let \( \delta \) be the number that @cor-eigenvalues-continuous supplies for this \( \varepsilon \). If \( \norm{\B - \A} < \delta \), number the eigenvalues of \( \B \) so that \( \lvert \mu_i - \lambda_i \rvert < \varepsilon \) for every \( i \). For \( i \ne j \), @thm-complex-triangle-inequality gives
\[
\lvert \mu_i - \mu_j \rvert \ge \lvert \lambda_i - \lambda_j \rvert - \lvert \mu_i - \lambda_i \rvert - \lvert \mu_j - \lambda_j \rvert > 2\varepsilon - \varepsilon - \varepsilon = 0 ,
\]
so the \( \mu_i \) are pairwise distinct. There are \( n \) of them, so \( \B \) is diagonalizable by @cor-distinct-eigenvalues-diagonalizable.

(b) Let \( \A \) be arbitrary and \( \varepsilon > 0 \). By @exr-schur-triangularization-c3 (a) there is \( \A' \) with \( n \) distinct eigenvalues and \( \lvert a_{ij} - a'_{ij}\rvert < \varepsilon/C \) for all \( i, j \), with \( C \) as in the proof of @cor-diagonalizable-dense-again; hence \( \norm{\A - \A'} < \varepsilon \). So every ball meets the set of matrices with \( n \) distinct eigenvalues, and no ball is contained in its complement.

(c) No. The zero matrix is diagonalizable, and in \( M_2(\nC) \) every ball around it contains \( \varepsilon\J_2(0) \), whose only eigenvalue is \( 0 \), with eigenspace of dimension \( 1 \) and algebraic multiplicity \( 2 \); so it is not diagonalizable by @thm-diagonalization (e). Dense (@cor-diagonalizable-dense-again) and open are independent properties, and the diagonalizable matrices are the first without being the second.
:::
