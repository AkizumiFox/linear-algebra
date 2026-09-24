# Krylov Subspaces

Sections 4 and 5 both consist of multiplying by \( \A \) over and over: the power method forms \( \b, \A\b, \A^2\b, \dots \) and keeps only the newest vector, and the QR algorithm, by @thm-qr-is-orthogonal-iteration, does the same thing to \( \e_1 \) inside its first column. In both cases everything computed before the last step is thrown away, and this section keeps it instead. The span of the vectors produced by \( k \) matrix-vector products is a subspace of dimension up to \( k \), and the best approximations it contains are far better than its last vector alone. That subspace, the process that builds an orthonormal basis of it, and the eigenvalue estimates it yields are the subject here.

Throughout, \( F = \nR \) or \( F = \nC \), and \( F^n \) carries the standard inner product, linear in the first slot, with \( \inner{\x}{\y} = \y^{*}\x \) and \( \norm{\cdot} = \norm{\cdot}_2 \).

## The space that k products span

A large matrix is often not available as a table of \( n^2 \) numbers at all. What is available is a rule for computing \( \A\x \) from \( \x \) — a sparse pattern of neighbors on a grid, a graph, a differential operator discretized. For such a matrix, forming \( \A\x \) is cheap and forming \( \A^{-1} \), or even looking at an entry of \( \A^2 \), is not. So the honest question is: after \( k \) multiplications, what do we possess?

We possess \( \b, \A\b, \dots, \A^{k-1}\b \), and hence every linear combination of them. The power method uses one of these vectors. That is wasteful, and the waste has a name only because the span deserves one.

*The Krylov space is everything that \( k \) matrix-vector products can reach.*

::: {#def-krylov-subspace}
[Krylov Subspace]

Let \( \A \in M_n(F) \), let \( \b \in F^n \) and let \( k \ge 1 \) be an integer. The **\( k \)-th Krylov subspace** of the pair \( (\A, \b) \) is
\[
\cK_k(\A, \b) \coloneqq \Span\bigl(\b,\ \A\b,\ \A^2\b,\ \dots,\ \A^{k-1}\b\bigr) \subseteq F^n .
\]
:::

In words: we list the first \( k \) vectors of the sequence obtained by repeatedly applying \( \A \) to \( \b \) — **starting at \( \b \) itself**, so that the last one is \( \A^{k-1}\b \) and not \( \A^{k}\b \) — and take their span. It is a subspace for the usual reason, being a span. The index \( k \) counts **vectors**, not powers; the off-by-one is a convention, and it is the one that makes \( \dim\cK_k \le k \) with equality in the typical case.

**Examples.** Take \( F = \nR \) throughout.

- **The identity.** For \( \A = \I_n \) and any \( \b \neq \0 \), every \( \A^{j}\b \) equals \( \b \), so \( \cK_k(\I_n, \b) = \Span(\b) \) for every \( k \). One product buys nothing, and neither do a hundred.
- **A companion matrix.** Let \( \A\e_j = \e_{j+1} \) for \( j \le n-1 \), as for the companion matrix of @def-companion-matrix, and let \( \b = \e_1 \). Then \( \A^{j}\e_1 = \e_{j+1} \) for \( j \le n-1 \), so \( \cK_k(\A, \e_1) = \Span(\e_1, \dots, \e_k) \) for \( k \le n \), of dimension exactly \( k \). Here every product buys a new dimension.
- **A diagonal matrix.** Let \( \A = \diag(4, 3, 2, 1) \) and \( \b = (1,1,1,1) \). Then \( \A^{j}\b = (4^{j}, 3^{j}, 2^{j}, 1) \), and these four vectors for \( j = 0, 1, 2, 3 \) form a Vandermonde matrix with distinct nodes, hence are independent (@thm-vandermonde-determinant). So \( \dim\cK_k = k \) for \( k \le 4 \), and \( \cK_4 = \nR^4 \).
- **Degenerate cases.** \( \cK_1(\A, \b) = \Span(\b) \); and \( \cK_k(\A, \0) = \{\0\} \) for every \( k \), which is why \( \b \neq \0 \) is assumed from here on.

**Non-example by minimal change.** Drop the middle vector of the list. Let \( \A \in M_3(\nR) \) satisfy \( \A\e_1 = \e_2 \), \( \A\e_2 = \e_3 \), \( \A\e_3 = \0 \), and let \( \b = \e_1 \). The set \( \Span(\b, \A^2\b) = \Span(\e_1, \e_3) \) is a perfectly good subspace, and it is not \( \cK_k(\A,\b) \) for any \( k \), since those are \( \Span(\e_1) \), \( \Span(\e_1,\e_2) \) and \( \nR^3 \). The clause that fails is that the powers be **consecutive**, and what it costs is everything: \( \A\Span(\e_1,\e_3) = \Span(\e_2) \), which meets \( \Span(\e_1,\e_3) \) only at \( \0 \). The Krylov spaces, by contrast, are nested and almost invariant, which is the next proposition.

**Why this definition.** Chapter 10 already met the union of all of them. The cyclic subspace \( Z(\b; \A) = \Span(\b, \A\b, \A^2\b, \dots) \) of @def-cyclic-subspace is the smallest \( \A \)-invariant subspace containing \( \b \) (@prp-cyclic-subspace-smallest), and @thm-cyclic-subspace-basis says that the list stops growing exactly at the degree of the \( \A \)-annihilator \( m_{\A,\b} \). The Krylov space is that construction **truncated at \( k \)**, and the truncation is the whole point: \( Z(\b;\A) \) is a theoretical object, while \( \cK_k(\A,\b) \) is what \( k \) units of work actually deliver.

::: {#prp-krylov-properties}
[Krylov Spaces: Nesting, Dimension, Invariance]

Let \( \A \in M_n(F) \) and \( \b \in F^n \) with \( \b \neq \0 \), and let \( d = \deg m_{\A,\b} \ge 1 \) be the degree of the \( \A \)-annihilator of \( \b \) (@def-t-annihilator). Then, for every \( k \ge 1 \):

::: {.enumerate options="label=(\alph*)"}
1. \( \cK_k(\A,\b) = \{\, p(\A)\b : p \in F[x],\ \deg p \le k-1 \,\} \), and \( \cK_k \subseteq \cK_{k+1} \) and \( \A\,\cK_k \subseteq \cK_{k+1} \);
2. \( \dim\cK_k(\A,\b) = \min(k, d) \);
3. \( \cK_{k+1} = \cK_k \) if and only if \( k \ge d \), and in that case \( \cK_k = Z(\b;\A) \) is \( \A \)-invariant.
:::
:::

::: {.idea}
Everything is @thm-cyclic-subspace-basis read one index at a time. That theorem says \( (\b, \A\b, \dots, \A^{d-1}\b) \) is a basis of \( Z(\b;\A) \); so the first \( d \) vectors of our list are independent, and from \( \A^{d}\b \) on they add nothing.
:::

::: {.proof}
(a) A linear combination \( \sum_{j<k} a_j\A^{j}\b \) is \( p(\A)\b \) for \( p = \sum_{j<k}a_jx^{j} \), and conversely, which is the first statement. The inclusion \( \cK_k \subseteq \cK_{k+1} \) holds because the spanning list of \( \cK_k \) is part of that of \( \cK_{k+1} \). And \( \A\A^{j}\b = \A^{j+1}\b \in \cK_{k+1} \) for \( j \le k-1 \), so \( \A \) maps a spanning list of \( \cK_k \) into \( \cK_{k+1} \), hence maps \( \cK_k \) into \( \cK_{k+1} \).

(b) By @thm-cyclic-subspace-basis (a), the list \( (\b, \A\b, \dots, \A^{d-1}\b) \) is a basis of \( Z(\b;\A) \). If \( k \le d \), the first \( k \) entries of that list are a sublist of a basis, hence independent, so \( \dim\cK_k = k \). If \( k > d \), then \( \cK_k \subseteq Z(\b;\A) \), because every \( \A^{j}\b \) lies there (@prp-cyclic-subspace-smallest (a)); and \( \cK_k \supseteq \cK_d = Z(\b;\A) \), since \( \cK_d \) already contains a basis of it. So \( \cK_k = Z(\b;\A) \) and \( \dim\cK_k = d \). In both cases \( \dim\cK_k = \min(k,d) \).

(c) \( (\Leftarrow) \) If \( k \ge d \), then (b) gives \( \dim\cK_{k+1} = d = \dim\cK_k \), and with \( \cK_k \subseteq \cK_{k+1} \) from (a) this forces equality; and the common space is \( Z(\b;\A) \), \( \A \)-invariant by @prp-cyclic-subspace-smallest (b).
\( (\Rightarrow) \) If \( k < d \), then (b) gives \( \dim\cK_{k+1} = k+1 > k = \dim\cK_k \), so the two differ. This proves the proposition.
:::

::: {.warning}
**The list \( \b, \A\b, \dots, \A^{k-1}\b \) is a basis of \( \cK_k \) and is useless as one.** By Section 4's reading of the power method (@thm-power-method), \( \A^{j}\b \) turns towards the dominant eigenvector as \( j \) grows, so the later vectors of the list are nearly parallel to each other. Even for \( \A = \diag(4,3,2,1) \) and \( \b = (1,1,1,1) \), with its modest ratio \( \lambda_1/\lambda_2 = 4/3 \), the angle between consecutive vectors of the list falls from \( 24 \) degrees to \( 8.9 \) degrees across those four vectors, and the matrix with those four columns has \( 2 \)-norm condition number about \( 1200 \) — for a \( 4 \times 4 \) problem with one-digit data. Independent they may be; in the arithmetic of @def-floating-point-model the coordinates of a vector in that basis are computed with errors magnified by that condition number, which grows quickly with \( k \). **A Krylov method never uses this basis.** It builds an orthonormal one instead, and that is the next subsection.
:::

::: {.check}
Let \( \A \in M_n(F) \) be invertible with \( \A^2 = \I_n \), and let \( \b \neq \0 \) be a vector that is not an eigenvector of \( \A \). What is \( \dim\cK_k(\A,\b) \) for each \( k \ge 1 \)?
:::

::: {.solution}
It is \( 1 \) for \( k = 1 \) and \( 2 \) for every \( k \ge 2 \). The polynomial \( x^2 - 1 \) kills \( \b \), so \( m_{\A,\b} \) divides it and has degree at most \( 2 \) (@def-t-annihilator). Degree \( 1 \) would mean \( m_{\A,\b} = x - \lambda \), that is \( \A\b = \lambda\b \), making \( \b \) an eigenvector, which is excluded; and \( \deg m_{\A,\b} \ge 1 \) because \( \b \neq \0 \). So \( d = 2 \), and @prp-krylov-properties (b) gives \( \min(k,2) \).
:::

## Arnoldi: Gram–Schmidt with a purpose

We want an orthonormal basis \( \q_1, \dots, \q_k \) of \( \cK_k \), with the nesting preserved: \( \Span(\q_1, \dots, \q_j) = \cK_j \) for every \( j \le k \). Running @thm-gram-schmidt on the list \( \b, \A\b, \dots, \A^{k-1}\b \) would do it, and would inherit exactly the defect the warning describes, since it needs those vectors first.

The repair is one line long, and it is the idea of the whole subsection. Do not orthogonalize \( \A^{j}\b \). Orthogonalize \( \A\q_j \). The vector \( \A\q_j \) lies in \( \cK_{j+1} \) by @prp-krylov-properties (a), and subtracting its components along \( \q_1, \dots, \q_j \) leaves a vector in \( \cK_{j+1} \) orthogonal to \( \cK_j \) — which is what the next basis vector must be. The powers of \( \A \) are never formed.

::: {.algorithm}
**The Arnoldi process.** Given \( \A \in M_n(F) \) and \( \b \neq \0 \), set \( \q_1 = \b/\norm{\b} \). For \( j = 1, 2, \dots \):
\[
\begin{aligned}
&h_{ij} = \inner{\A\q_j}{\q_i} \quad (1 \le i \le j),
&&\w_j = \A\q_j - \sum_{i=1}^{j} h_{ij}\q_i , \\
&h_{j+1,j} = \norm{\w_j},
&&\q_{j+1} = \w_j/h_{j+1,j} \quad\text{if } h_{j+1,j} \neq 0 .
\end{aligned}
\]
If \( h_{j+1,j} = 0 \) the process stops; this is called a **breakdown**, and the theorem below says it is good news.
:::

Write \( \Q_j = (\q_1 \mid \dots \mid \q_j) \in M_{n \times j}(F) \), let \( \H_k \in M_k(F) \) have entries \( h_{ij} \) for \( i \le j+1 \) and zeros elsewhere, and let \( \widetilde{\H}_k \in M_{(k+1)\times k}(F) \) be \( \H_k \) with the extra row \( h_{k+1,k}\e_k\tp \) appended at the bottom.

::: {#thm-arnoldi}
[The Arnoldi Process]

Let \( \A \in M_n(F) \), let \( \b \in F^n \) be non-zero, let \( d = \deg m_{\A,\b} \), and run the Arnoldi process. Then the **Arnoldi relation**
\[
\A\Q_k = \Q_k\H_k + h_{k+1,k}\,\q_{k+1}\e_k\tp
\qquad (1 \le k \le d)
\]{#eq-arnoldi}
holds, the last term being \( \0 \) when \( k = d \). Moreover:

::: {.enumerate options="label=(\alph*)"}
1. For every \( j \le d \), the list \( (\q_1, \dots, \q_j) \) is an orthonormal basis of \( \cK_j(\A,\b) \); moreover \( h_{j+1,j} > 0 \) for \( j < d \), and \( h_{d+1,d} = 0 \), so the process breaks down at step \( d \) and at no earlier step.
2. For \( 1 \le k \le d \) we have \( \Q_k^{*}\Q_k = \I_k \), and \( \H_k = \Q_k^{*}\A\Q_k \) is **upper Hessenberg**. For \( k < d \), @eq-arnoldi can also be written \( \A\Q_k = \Q_{k+1}\widetilde{\H}_k \).
3. A breakdown means an invariant subspace: if \( h_{k+1,k} = 0 \), then \( \A\cK_k \subseteq \cK_k \), and every eigenvalue of \( \H_k \) is an eigenvalue of \( \A \).
:::
:::

::: {.idea}
Only one thing has to be checked, and it is the nesting: if \( \q_1, \dots, \q_j \) is an orthonormal basis of \( \cK_j \), then \( \A\q_j \) lies in \( \cK_{j+1} \) but generally not in \( \cK_j \), and what the step subtracts is exactly its \( \cK_j \)-component. The matrix identity is then just the definition of \( \w_j \) rearranged, column by column, and the Hessenberg shape is the statement that \( \A\q_j \) needs only \( \q_1, \dots, \q_{j+1} \) — never \( \q_{j+2} \) — because \( \A\cK_j \subseteq \cK_{j+1} \).
:::

::: {.proof}
(a) Induction on \( j \). For \( j = 1 \), \( \q_1 = \b/\norm{\b} \) is a unit vector spanning \( \cK_1 = \Span(\b) \). Let \( 1 \le j \) and suppose \( (\q_1, \dots, \q_j) \) is an orthonormal basis of \( \cK_j \). The subtraction in the process makes \( \w_j \) orthogonal to each \( \q_i \) with \( i \le j \): for such \( i \),
\[
\inner{\w_j}{\q_i} = \inner{\A\q_j}{\q_i} - \sum_{l=1}^{j} h_{lj}\inner{\q_l}{\q_i} = h_{ij} - h_{ij} = 0 ,
\]
using orthonormality. Also \( \A\q_j \in \A\cK_j \subseteq \cK_{j+1} \) by @prp-krylov-properties (a), and each \( \q_i \in \cK_j \subseteq \cK_{j+1} \), so \( \w_j \in \cK_{j+1} \).

::: {.claim}
\( \cK_{j+1} = \cK_j + \Span(\A\q_j) \).
:::

::: {.proof}
\( (\supseteq) \) Both summands lie in \( \cK_{j+1} \), by @prp-krylov-properties (a). \( (\subseteq) \) Since \( \cK_{j+1} = \cK_j + \Span(\A^{j}\b) \), it is enough to place \( \A^{j}\b \) on the right. Write \( \A^{j-1}\b = \sum_{i \le j}c_i\q_i \), possible because \( \A^{j-1}\b \in \cK_j \) and the \( \q_i \) are a basis of it. Applying \( \A \),
\[
\A^{j}\b = \sum_{i \le j} c_i\,\A\q_i ,
\]
and for \( i \le j-1 \) we have \( \A\q_i \in \A\cK_i \subseteq \cK_{i+1} \subseteq \cK_j \). So only the term \( c_j\A\q_j \) leaves \( \cK_j \).
:::

Now \( \w_j = \0 \) if and only if \( \A\q_j \in \cK_j \), and by the Claim that happens if and only if \( \cK_{j+1} = \cK_j \). Suppose first that \( j < d \). Then \( \dim\cK_{j+1} = j+1 > j = \dim\cK_j \) by @prp-krylov-properties (b), so \( \cK_{j+1} \neq \cK_j \) and \( \w_j \neq \0 \). Hence \( h_{j+1,j} > 0 \), and \( \q_{j+1} = \w_j/h_{j+1,j} \) is a unit vector in \( \cK_{j+1} \) orthogonal to \( \q_1, \dots, \q_j \). An orthogonal list of non-zero vectors is independent, so \( (\q_1, \dots, \q_{j+1}) \) is an orthonormal list of \( j+1 \) vectors in the \( (j+1) \)-dimensional space \( \cK_{j+1} \), hence a basis of it.

If instead \( j = d \), then \( \cK_{d+1} = \cK_d \) by @prp-krylov-properties (c), so \( \A\q_d \in \A\cK_d \subseteq \cK_{d+1} = \cK_d \) and \( \w_d = \0 \). This gives (a).

(b), and @eq-arnoldi. The columns of \( \Q_k \) are orthonormal by (a), which is \( \Q_k^{*}\Q_k = \I_k \). Rearranging the definition of \( \w_j \),
\[
\A\q_j = \sum_{i=1}^{j} h_{ij}\q_i + h_{j+1,j}\q_{j+1} = \sum_{i=1}^{j+1} h_{ij}\q_i ,
\]
for each \( j \le k \), where for \( j = d \) the last term is \( \0 \). For \( j < k \) the right-hand side is \( \Q_k\H_k\e_j \), since column \( j \) of \( \H_k \) has entries \( h_{1j}, \dots, h_{j+1,j} \) and zeros below and \( j+1 \le k \); for \( j = k \) it is \( \Q_k\H_k\e_k + h_{k+1,k}\q_{k+1} \). Collecting the columns gives @eq-arnoldi, and the form \( \A\Q_k = \Q_{k+1}\widetilde{\H}_k \) is the same identity with the extra column of \( \Q_{k+1} \) and the extra row of \( \widetilde{\H}_k \) absorbing the last term. The entries \( h_{ij} \) with \( i > j+1 \) are zero by definition, which is exactly upper Hessenberg form. Finally, multiplying @eq-arnoldi on the left by \( \Q_k^{*} \) and using \( \Q_k^{*}\Q_k = \I_k \) and \( \Q_k^{*}\q_{k+1} = \0 \),
\[
\Q_k^{*}\A\Q_k = \H_k + h_{k+1,k}\,\Q_k^{*}\q_{k+1}\e_k\tp = \H_k .
\]

(c) If \( h_{k+1,k} = 0 \), then @eq-arnoldi reads \( \A\Q_k = \Q_k\H_k \), so \( \A\q_j \in \cK_k \) for every \( j \le k \) and hence \( \A\cK_k \subseteq \cK_k \). If \( \H_k\y = \theta\y \) with \( \y \neq \0 \), put \( \x = \Q_k\y \), which is non-zero because the columns of \( \Q_k \) are independent; then \( \A\x = \A\Q_k\y = \Q_k\H_k\y = \theta\Q_k\y = \theta\x \). This proves the theorem.
:::

The cost of \( k \) steps is \( k \) matrix-vector products plus the orthogonalizations, which use about \( 4nj \) flops at step \( j \) — \( j \) inner products and \( j \) subtractions, about \( 2n \) flops each — so \( O(nk^2) \) in total; and all \( k+1 \) vectors must be stored. Both grow with \( k \), which is why Arnoldi is restarted in practice. For Hermitian \( \A \) neither grows, and that is the next theorem.

## Lanczos: the recurrence collapses to three terms

::: {#thm-lanczos}
[The Lanczos Recurrence]

Let \( \A \in M_n(\nC) \) be **Hermitian**, let \( \b \neq \0 \), and run the Arnoldi process. Then \( \H_k \) is Hermitian for every \( k \le d \), hence **tridiagonal**, with real diagonal entries; writing \( \alpha_j = h_{jj} \in \nR \) and \( \beta_j = h_{j+1,j} \), which is \( > 0 \) for \( j < d \) and \( 0 \) for \( j = d \), we have \( h_{j,j+1} = \beta_j \) and
\[
\A\q_j = \beta_{j-1}\q_{j-1} + \alpha_j\q_j + \beta_j\q_{j+1}
\qquad (1 \le j \le d),
\]{#eq-lanczos}
with \( \beta_0\q_0 \) read as \( \0 \) and \( \beta_d\q_{d+1} \) as \( \0 \). Consequently \( \H_k = \T_k \) is the real symmetric tridiagonal matrix with diagonal \( (\alpha_1, \dots, \alpha_k) \) and off-diagonal \( (\beta_1, \dots, \beta_{k-1}) \), and each step of the process needs only \( \q_{j-1} \) and \( \q_j \).
:::

::: {.idea}
Two facts collide. The matrix \( \H_k = \Q_k^{*}\A\Q_k \) is Hermitian because \( \A \) is, and it is upper Hessenberg by @thm-arnoldi. A Hermitian matrix with zeros below the subdiagonal has zeros above the superdiagonal too, by conjugating. Everything else is bookkeeping. The reason is worth naming separately: \( h_{ij} = \inner{\A\q_j}{\q_i} \) lets \( \A \) move to the other slot for free, and \( \A\q_i \) lives one index further along than \( \q_i \) does.
:::

::: {.proof}
By @thm-arnoldi (b), \( \H_k = \Q_k^{*}\A\Q_k \), so \( \H_k^{*} = \Q_k^{*}\A^{*}\Q_k = \Q_k^{*}\A\Q_k = \H_k \) and \( \H_k \) is Hermitian; in particular its diagonal entries are real.

Let \( i \le j - 2 \). Since \( \A^{*} = \A \) is self-adjoint,
\[
h_{ij} = \inner{\A\q_j}{\q_i} = \inner{\q_j}{\A\q_i} .
\]
Now \( \q_i \in \cK_i \), so \( \A\q_i \in \cK_{i+1} \subseteq \cK_{j-1} \) by @prp-krylov-properties (a) and \( i + 1 \le j-1 \), while \( \q_j \) is orthogonal to \( \cK_{j-1} \) by @thm-arnoldi (a). Hence \( h_{ij} = 0 \) whenever \( i \le j-2 \). Together with \( h_{ij} = 0 \) for \( i > j+1 \), this leaves only \( i \in \{j-1, j, j+1\} \), so \( \H_k \) is tridiagonal. Being Hermitian, \( h_{j,j+1} = \conj{h_{j+1,j}} = \beta_j \), which is real and positive. The displayed recurrence @eq-lanczos is then the expansion \( \A\q_j = \sum_{i}h_{ij}\q_i \) of @thm-arnoldi (b) with only three surviving terms; and \( \H_k \) has real entries, is symmetric and is tridiagonal, as claimed. Since the step needs only \( h_{j-1,j} = \beta_{j-1} \), \( h_{jj} = \alpha_j \) and \( \q_{j-1}, \q_j \), this proves the theorem.
:::

**This is Chapter 11's three-term recurrence, and for the same reason.** Chapter 11 §10 built the monic orthogonal polynomials for an inner product on \( \nR[x] \) and found (@thm-three-term-recurrence) that \( p_{k+1} = (x - a_k)p_k - b_kp_{k-1} \), with only three terms; the reason given there was @prp-multiplication-by-x-symmetric, "multiplication by \( x \) moves from one slot to the other for free". The two statements are the same statement. Given Hermitian \( \A \) and \( \b \neq \0 \), define on \( \nR[x] \)
\[
\inner{p}{q}_{\b} \coloneqq \inner{p(\A)\b}{q(\A)\b} .
\]
This is symmetric and bilinear, and on \( \nR[x]_{\le d-1} \) it is positive definite: \( \inner{p}{p}_{\b} = \norm{p(\A)\b}^2 \) vanishes only when \( p(\A)\b = \0 \), which by @def-t-annihilator means \( m_{\A,\b} \mid p \), impossible for a non-zero \( p \) of degree below \( d \). Multiplication by \( x \) is symmetric for it, since \( \A \) is Hermitian:
\[
\inner{xp}{q}_{\b} = \inner{\A\,p(\A)\b}{q(\A)\b} = \inner{p(\A)\b}{\A\,q(\A)\b} = \inner{p}{xq}_{\b} .
\]
Now @prp-krylov-properties (a) says \( \q_{j+1} \) is \( r(\A)\b \) for some \( r \) of degree at most \( j \), and orthogonality to \( \cK_j \) says \( \inner{r}{s}_{\b} = 0 \) for every \( s \) of degree below \( j \). So for \( j \le d-1 \) the polynomial \( r \) is a scalar multiple of the \( j \)-th monic orthogonal polynomial \( p_j \) for \( \inner{\cdot}{\cdot}_{\b} \), and @eq-lanczos, at those indices, **is** the recurrence of @thm-three-term-recurrence rewritten in terms of the vectors \( p_j(\A)\b \) — read, as that theorem's node inner product is read, only in the range of degrees where the form is positive definite. The last step \( j = d \) lies outside that range: there the monic polynomial of degree \( d \) orthogonal to everything of lower degree is \( m_{\A,\b} \) itself, and \( \inner{m_{\A,\b}}{m_{\A,\b}}_{\b} = 0 \). A third appearance of the same three terms is Chapter 7's: by @thm-tridiagonal-recurrence, the characteristic polynomials \( D_k(x) = \det(x\I_k - \T_k) \) of the leading blocks satisfy
\[
D_k = (x - \alpha_k)D_{k-1} - \beta_{k-1}^2\,D_{k-2} ,
\]
which is @thm-three-term-recurrence with \( a_{k-1} = \alpha_k \) and \( b_{k-1} = \beta_{k-1}^2 > 0 \). The Lanczos coefficients, the orthogonal polynomials and the determinants of the tridiagonal blocks are one object seen three ways.

::: {#exm-lanczos-breakdown}
[A breakdown at step two]

Let \( \A = \begin{pmatrix} 3 & 1 & 1 \\ 1 & 3 & 1 \\ 1 & 1 & 3\end{pmatrix} \) and \( \b = \e_1 \). Run the Lanczos recurrence of @thm-lanczos, and identify what it finds.
:::

::: {.solution}
\( \q_1 = \e_1 \), and \( \A\q_1 = (3,1,1) \). So \( \alpha_1 = \inner{\A\q_1}{\q_1} = 3 \) and
\[
\w_1 = (3,1,1) - 3(1,0,0) = (0,1,1), \qquad \beta_1 = \sqrt2, \qquad \q_2 = \tfrac{1}{\sqrt2}(0,1,1) .
\]
Next, \( \A\q_2 = \tfrac{1}{\sqrt2}(2,4,4) \), so \( \alpha_2 = \inner{\A\q_2}{\q_2} = \tfrac12(0 + 4 + 4) = 4 \) and
\[
\w_2 = \tfrac{1}{\sqrt2}(2,4,4) - 4\cdot\tfrac{1}{\sqrt2}(0,1,1) - \sqrt2\,(1,0,0) = \tfrac{1}{\sqrt2}(2,0,0) - \sqrt2(1,0,0) = \0 .
\]
The process breaks down at step \( 2 \), so \( d = 2 \) and \( \cK_2 \) is \( \A \)-invariant, by @thm-arnoldi (a), (c). Then
\[
\T_2 = \begin{pmatrix} 3 & \sqrt2 \\ \sqrt2 & 4 \end{pmatrix},
\qquad
p_{\T_2}(x) = (x-3)(x-4) - 2 = x^2 - 7x + 10 ,
\]
with roots \( 5 \) and \( 2 \). And indeed \( \spec(\A) = \{5, 2\} \), with \( 5 \) simple and \( 2 \) of multiplicity \( 2 \): the two steps have produced both eigenvalues exactly. This is @thm-arnoldi (c) in action, and it is also @prp-krylov-properties (b) with \( d = \deg m_{\A,\e_1} = 2 \), since \( m_{\A} = (x-5)(x-2) \) and neither factor alone kills \( \e_1 \).
:::

## Ritz values

An invariant subspace would give eigenvalues exactly. A Krylov space is an **almost** invariant subspace — by @eq-arnoldi it fails to be invariant only through the single vector \( h_{k+1,k}\q_{k+1} \) — so it should give almost-eigenvalues, and it should be possible to say how almost.

::: {#def-ritz-values}
[Ritz Values and Ritz Vectors]

Let \( \A \in M_n(F) \), let \( \Q_k \in M_{n\times k}(F) \) have orthonormal columns, and put \( \H_k = \Q_k^{*}\A\Q_k \). The eigenvalues \( \theta_1, \dots, \theta_k \) of \( \H_k \) are the **Ritz values** of \( \A \) from the subspace \( \Span(\q_1,\dots,\q_k) \), and for an eigenvector \( \y \) of \( \H_k \) with \( \H_k\y = \theta\y \) and \( \norm{\y} = 1 \), the vector \( \x = \Q_k\y \) is the corresponding **Ritz vector**; the pair \( (\theta, \x) \) is a **Ritz pair**.
:::

In words: project the problem onto the subspace, solve the small problem exactly, and lift the answer back. The Ritz values depend on the subspace and not on which orthonormal basis of it we chose: replacing \( \Q_k \) by \( \Q_k\V \) with \( \V \) unitary replaces \( \H_k \) by \( \V^{*}\H_k\V \), which has the same eigenvalues. Note that \( \norm{\x} = \norm{\Q_k\y} = \norm{\y} = 1 \), since \( \Q_k \) has orthonormal columns.

::: {#thm-ritz-interlacing}
[Ritz Values Interlace, and Their Residual Is One Number]

Let \( \A \in M_n(\nC) \) be Hermitian with eigenvalues \( \lambda_1(\A) \ge \dots \ge \lambda_n(\A) \), let \( 1 \le k \le d \), and let \( \theta_1 \ge \dots \ge \theta_k \) be the Ritz values from \( \cK_k(\A,\b) \), that is, the eigenvalues of \( \T_k \).

::: {.enumerate options="label=(\alph*)"}
1. \( \lambda_i(\A) \ \ge\ \theta_i \ \ge\ \lambda_{i + n - k}(\A) \) for \( 1 \le i \le k \).
2. If \( \T_k\y = \theta\y \) with \( \norm{\y} = 1 \) and \( \x = \Q_k\y \), then
\[
\A\x - \theta\x = \beta_k\,y_k\,\q_{k+1},
\qquad\text{so}\qquad
\norm{\A\x - \theta\x} = \beta_k\,\lvert y_k\rvert ,
\]
where \( y_k \) is the last coordinate of \( \y \) and \( \beta_k = h_{k+1,k} \), with \( \beta_d\q_{d+1} \) read as \( \0 \).
:::
:::

::: {.idea}
For (a), the obstacle is that \( \T_k = \Q_k^{*}\A\Q_k \) is a compression, not a principal submatrix, and Chapter 17's interlacing is about principal submatrices. The repair is to complete \( \Q_k \) to a unitary matrix: then \( \T_k \) *is* the leading principal submatrix of a matrix unitarily similar to \( \A \), and @cor-interlacing-general-submatrix applies unchanged. For (b), just apply @eq-arnoldi to \( \y \) and watch the two \( \Q_k\T_k\y \) terms cancel.
:::

::: {.proof}
(a) Extend \( \q_1, \dots, \q_k \) to an orthonormal basis \( \q_1, \dots, \q_n \) of \( \nC^n \), which is possible by @thm-gram-schmidt applied to any extension of the list to a basis (@thm-basis-extension), and let \( \U = (\q_1 \mid \dots \mid \q_n) \), which is unitary. Then \( \B = \U^{*}\A\U \) is Hermitian and unitarily similar to \( \A \), so \( \lambda_i(\B) = \lambda_i(\A) \) for every \( i \). Its entries are \( b_{ij} = \inner{\A\q_j}{\q_i} \), and for \( i, j \le k \) these are exactly the entries of \( \Q_k^{*}\A\Q_k = \T_k \). So \( \T_k = \B_{I,I} \) with \( I = \{1, \dots, k\} \), a principal submatrix of \( \B \) obtained by deleting \( m = n-k \) rows and the same columns. Now @cor-interlacing-general-submatrix gives
\[
\lambda_i(\B) \ \ge\ \lambda_i(\T_k) \ \ge\ \lambda_{i+m}(\B) \qquad (1 \le i \le k),
\]
which is the assertion, since \( \lambda_i(\T_k) = \theta_i \) and \( \lambda_i(\B) = \lambda_i(\A) \).

(b) By @eq-arnoldi, \( \A\Q_k = \Q_k\T_k + \beta_k\q_{k+1}\e_k\tp \). Applying both sides to \( \y \) and using \( \T_k\y = \theta\y \) and \( \e_k\tp\y = y_k \),
\[
\A\x = \A\Q_k\y = \Q_k\T_k\y + \beta_k\,y_k\,\q_{k+1} = \theta\,\Q_k\y + \beta_k y_k\q_{k+1} = \theta\x + \beta_k y_k\q_{k+1} .
\]
Subtracting \( \theta\x \) gives the displayed identity, and taking norms gives the second form, since \( \norm{\q_{k+1}} = 1 \) and \( \beta_k \ge 0 \). (For \( k = d \) the right-hand side is \( \0 \), and the Ritz pair is an exact eigenpair, as @thm-arnoldi (c) already said.) This proves the theorem.
:::

Part (b) is where the chapter's perturbation theory pays off, and it pays off for free. The residual \( \norm{\A\x - \theta\x} \) is the one quantity Chapter 20 §06 asks for, and here it is available **without forming \( \A\x \)**: it is the product of the number \( \beta_k \) the process has just computed and one coordinate of the small eigenvector \( \y \). So @thm-hermitian-residual-bound applies verbatim, and says that \( \A \) has an eigenvalue within \( \beta_k\lvert y_k\rvert \) of \( \theta \). Better still, \( \theta = \inner{\A\x}{\x} \) is the Rayleigh quotient of \( \x \) — because \( \inner{\A\x}{\x} = \y^{*}\Q_k^{*}\A\Q_k\y = \y^{*}\T_k\y = \theta \) — so @thm-kato-temple applies too, and turns the same number into a bound of size \( (\beta_k\lvert y_k\rvert)^2 \) divided by the distance to the rest of the spectrum. Nothing in this section had to be proved twice.

::: {.warning}
**A Ritz value that happens to equal an eigenvalue is not a converged one, and for a non-Hermitian \( \A \) there is no interlacing to fall back on.** Take
\[
\A = \begin{pmatrix} 2 & 1 & 1 \\ 0 & 2 & 1 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \b = \e_3 .
\]
Two Arnoldi steps give \( \q_1 = \e_3 \), \( \q_2 = \tfrac{1}{\sqrt2}(1,1,0) \) and \( \H_2 = \begin{pmatrix} 1 & 0 \\ \sqrt2 & \tfrac52 \end{pmatrix} \), hence the Ritz values \( \tfrac52 \) and \( 1 \); @exr-krylov-subspaces-b2 works the details. The second is an exact eigenvalue of \( \A \) — and its Ritz vector \( \tfrac{1}{\sqrt{17}}(-2,-2,3) \) is not an eigenvector of \( \A \), the residual being \( \sqrt{34}/17 \approx 0.343 \), nowhere near zero. What certifies convergence is the residual, never the agreement of a number with a number. Part (a) of @thm-ritz-interlacing needs \( \A \) Hermitian; without that hypothesis there is no interlacing and, by @thm-residual-bound, a residual bound carries the factor \( \kappa_2(\X) \).
:::

::: {#exm-ritz-diagonal}
[Ritz values closing in on the extremes]

Let \( \A = \diag(4,3,2,1) \) and \( \b = (1,1,1,1) \). Compute the Lanczos coefficients, the Ritz values for \( k = 1, 2, 3 \), and the residual of the largest Ritz pair at \( k = 3 \).
:::

::: {.solution}
Here \( \q_1 = \tfrac12(1,1,1,1) \) and \( \A\q_1 = \tfrac12(4,3,2,1) \), so \( \alpha_1 = \tfrac14(4+3+2+1) = \tfrac52 \). Then
\[
\w_1 = \tfrac12(4,3,2,1) - \tfrac52\cdot\tfrac12(1,1,1,1) = \tfrac14(3,1,-1,-3),
\qquad \beta_1 = \tfrac{\sqrt{20}}{4} = \tfrac{\sqrt5}{2},
\]
and \( \q_2 = \tfrac{1}{\sqrt{20}}(3,1,-1,-3) \). Continuing in the same way gives \( \alpha_2 = \alpha_3 = \alpha_4 = \tfrac52 \) as well, together with \( \beta_2 = \tfrac{2}{\sqrt5} \) and \( \beta_3 = \tfrac{3}{2\sqrt5} \).

The repetition of \( \tfrac52 \) is a symmetry, not an accident. Let \( \S \) be the reversal permutation matrix, \( \S\e_j = \e_{5-j} \), and put \( \B = \A - \tfrac52\I = \diag(\tfrac32, \tfrac12, -\tfrac12, -\tfrac32) \). Then \( \S \) is orthogonal with \( \S^2 = \I \), and \( \S\B\S = -\B \), \( \S\b = \b \). We show by induction, simultaneously, that \( \S\q_j = \varepsilon_j\q_j \) with \( \varepsilon_j = (-1)^{j-1} \) and that \( \alpha_j = \tfrac52 \). The first holds at \( j = 1 \). Given it at \( j \),
\[
\alpha_j - \tfrac52 = \inner{\B\q_j}{\q_j} = \inner{\S\B\q_j}{\S\q_j} = \inner{\S\B\S(\S\q_j)}{\S\q_j} = -\varepsilon_j^2\inner{\B\q_j}{\q_j} ,
\]
and \( \varepsilon_j^2 = 1 \), so this number equals its own negative and \( \alpha_j = \tfrac52 \). The Lanczos step then reads \( \w_j = \B\q_j - \beta_{j-1}\q_{j-1} \), and applying \( \S \) with \( \varepsilon_{j-1} = -\varepsilon_j \) gives \( \S\w_j = -\varepsilon_j\w_j \), so \( \S\q_{j+1} = \varepsilon_{j+1}\q_{j+1} \). The Ritz values are the eigenvalues of the leading blocks of \( \T_4 \):

| \( k \) | Ritz values | check against \( 4, 3, 2, 1 \) |
|---|---|---|
| 1 | \( \tfrac52 \) | \( 4 \ge 2.5 \ge 1 \) |
| 2 | \( \tfrac{5 \pm \sqrt5}{2} \approx 3.6180,\ 1.3820 \) | \( 4 \ge 3.618 \ge 2 \); \( 3 \ge 1.382 \ge 1 \) |
| 3 | \( \tfrac52 \pm \tfrac{\sqrt{205}}{10} \approx 3.9318,\ 1.0682 \), and \( \tfrac52 \) | \( 4 \ge 3.932 \ge 3 \); \( 3 \ge 2.5 \ge 2 \); \( 2 \ge 1.068 \ge 1 \) |
| 4 | \( 4, 3, 2, 1 \) | exact |

Every row obeys @thm-ritz-interlacing (a), with \( m = n - k \) shifting the index on the right. The extreme Ritz values close in on \( 4 \) and \( 1 \) fast, and the interior ones lag: at \( k = 3 \) the outer two are within \( 0.07 \) of \( 4 \) and \( 1 \), while the single interior value \( \tfrac52 \) is half a unit from each of \( 3 \) and \( 2 \).

*The residual at \( k = 3 \).* The eigenvector of \( \T_3 \) for \( \theta_1 = \tfrac52 + \tfrac{\sqrt{205}}{10} \) is, normalized,
\[
\y = \Bigl(\tfrac{5}{\sqrt{82}},\ \tfrac{1}{\sqrt2},\ \tfrac{4}{\sqrt{82}}\Bigr),
\]
so @thm-ritz-interlacing (b) gives \( \norm{\A\x - \theta_1\x} = \beta_3\lvert y_3\rvert = \tfrac{3}{2\sqrt5}\cdot\tfrac{4}{\sqrt{82}} = \tfrac{3\sqrt{410}}{205} \approx 0.2963 \). By @thm-hermitian-residual-bound, \( \A \) has an eigenvalue within \( 0.2963 \) of \( 3.9318 \); the truth is \( 4 \), at distance \( 0.0682 \), so the certificate costs a factor of about \( 4 \). Suppose we also know that \( \A \) has no eigenvalue in the open interval \( (3, 4) \). Then @thm-kato-temple (b) with \( \alpha = 3 \) improves the upper end to
\[
\theta_1 + \frac{(0.2963)^2}{3.9318 - 3} = 3.9318 + 0.0942 = 4.0260 ,
\]
and the lower end is \( \theta_1 \) itself by interlacing. The bracket \( [3.9318,\ 4.0260] \) has width \( 0.094 \) where the residual bound gave \( 0.593 \). That is the quadratic gain of Chapter 20 §06, obtained here from one number the process had already produced.
:::

## How fast the extreme Ritz values converge

The example suggests the extremes converge quickly. Here is why, and how much of it we can prove.

::: {#thm-ritz-extreme-convergence}
[A Rate for the Largest Ritz Value]

Let \( \A \in M_n(\nC) \) be Hermitian with eigenvalues \( \lambda_1 > \lambda_2 \ge \dots \ge \lambda_n \) and an orthonormal eigenbasis \( \v_1, \dots, \v_n \). Let \( \b \) be a unit vector with \( \b = \sum_i c_i\v_i \) and \( c_1 \neq 0 \), and put
\[
\tau^2 = \frac{\sum_{i \ge 2}\lvert c_i\rvert^2}{\lvert c_1\rvert^2},
\qquad
\rho = \frac{\lambda_2 - \lambda_n}{2\lambda_1 - \lambda_2 - \lambda_n} \in [0, 1) .
\]
Then the largest Ritz value \( \theta_1^{(k)} \) from \( \cK_k(\A,\b) \) satisfies, for \( 1 \le k \le d \),
\[
0 \ \le\ \lambda_1 - \theta_1^{(k)} \ \le\ (\lambda_1 - \lambda_n)\,\tau^2\,\rho^{2(k-1)} ,
\]
and \( \theta_1^{(k)} \) is non-decreasing in \( k \).
:::

::: {.idea}
Three moves. ① The largest Ritz value is the largest Rayleigh quotient **over the Krylov space**, by the Rayleigh principle transported through \( \Q_k \). ② Every vector of the Krylov space is \( p(\A)\b \) for a polynomial of degree below \( k \), so we may choose \( p \) and get a bound for free: whichever \( p \) makes \( p \) large at \( \lambda_1 \) and small at the other eigenvalues gives a good one. ③ Take the simplest such \( p \), the \( (k-1) \)-st power of \( x \) minus the midpoint of \( [\lambda_n, \lambda_2] \). That is not the best choice, and the best one is the subject of the next section.
:::

::: {.proof}
**Step 1.** \( \theta_1^{(k)} = \max\{R_{\A}(\x) : \x \in \cK_k(\A,\b),\ \x \neq \0\} \). Indeed \( \theta_1^{(k)} = \lambda_1(\T_k) = \max_{\y \neq \0}R_{\T_k}(\y) \) by @prp-rayleigh-basic, and the map \( \y \mapsto \Q_k\y \) is a bijection from \( \nC^{k}\setminus\{\0\} \) onto \( \cK_k\setminus\{\0\} \), because the columns of \( \Q_k \) are a basis of \( \cK_k \) (@thm-arnoldi (a)). Under it, with \( \x = \Q_k\y \),
\[
\inner{\A\x}{\x} = \y^{*}\Q_k^{*}\A\Q_k\y = \y^{*}\T_k\y,
\qquad
\inner{\x}{\x} = \y^{*}\Q_k^{*}\Q_k\y = \y^{*}\y ,
\]
so \( R_{\A}(\x) = R_{\T_k}(\y) \) and the two maxima agree. Monotonicity in \( k \) follows at once from \( \cK_k \subseteq \cK_{k+1} \) (@prp-krylov-properties (a)), and \( \theta_1^{(k)} \le \lambda_1 \) from @prp-rayleigh-basic applied on all of \( \nC^n \) — which is also @thm-ritz-interlacing (a) at \( i = 1 \).

**Step 2.** Let \( p \in \nR[x] \) have \( \deg p \le k-1 \) and \( p(\lambda_1) \neq 0 \), and put \( \x = p(\A)\b \). Then \( \x \in \cK_k \) by @prp-krylov-properties (a), and \( \x = \sum_i c_ip(\lambda_i)\v_i \) since \( \A\v_i = \lambda_i\v_i \). The list \( (\v_i) \) being orthonormal, @thm-orthonormal-coordinates gives
\[
R_{\A}(\x) = \frac{\sum_i\lvert c_i\rvert^2p(\lambda_i)^2\lambda_i}{\sum_i\lvert c_i\rvert^2p(\lambda_i)^2} ,
\]
and \( \x \neq \0 \) because its first coefficient \( c_1p(\lambda_1) \) is non-zero. Subtracting from \( \lambda_1 \),
\[
\lambda_1 - R_{\A}(\x)
= \frac{\sum_{i\ge2}\lvert c_i\rvert^2p(\lambda_i)^2(\lambda_1 - \lambda_i)}{\sum_i\lvert c_i\rvert^2p(\lambda_i)^2} ,
\]
the term \( i = 1 \) having vanished from the numerator. Every factor \( \lambda_1 - \lambda_i \) is at most \( \lambda_1 - \lambda_n \); and the denominator is at least its single term \( \lvert c_1\rvert^2p(\lambda_1)^2 \), all terms being non-negative. Hence
\[
\begin{aligned}
\lambda_1 - R_{\A}(\x)
&\ \le\ (\lambda_1 - \lambda_n)\,\frac{\sum_{i\ge2}\lvert c_i\rvert^2p(\lambda_i)^2}{\lvert c_1\rvert^2p(\lambda_1)^2}\\
&\ \le\ (\lambda_1 - \lambda_n)\,\tau^2\,\max_{i \ge 2}\Bigl(\frac{p(\lambda_i)}{p(\lambda_1)}\Bigr)^2 .
\end{aligned}
\tag{$\ast$}
\]
By Step 1, \( \lambda_1 - \theta_1^{(k)} \le \lambda_1 - R_{\A}(\x) \).

**Step 3.** Take \( \mu = \tfrac12(\lambda_2 + \lambda_n) \), the midpoint of the interval holding the unwanted eigenvalues, and \( p(x) = (x - \mu)^{k-1} \), of degree \( k-1 \). For \( i \ge 2 \) we have \( \lambda_n \le \lambda_i \le \lambda_2 \), so \( \lvert\lambda_i - \mu\rvert \le \tfrac12(\lambda_2 - \lambda_n) \). And
\[
\lambda_1 - \mu = \tfrac12(\lambda_2 - \lambda_n) + (\lambda_1 - \lambda_2) > \tfrac12(\lambda_2-\lambda_n) \ge 0 ,
\]
using \( \lambda_1 > \lambda_2 \); in particular \( p(\lambda_1) = (\lambda_1 - \mu)^{k-1} \neq 0 \). Therefore
\[
\max_{i\ge2}\Bigl\lvert\frac{p(\lambda_i)}{p(\lambda_1)}\Bigr\rvert
\le \Bigl(\frac{(\lambda_2-\lambda_n)/2}{\lambda_1 - \mu}\Bigr)^{k-1} = \rho^{\,k-1} ,
\]
since \( 2(\lambda_1 - \mu) = 2\lambda_1 - \lambda_2 - \lambda_n \). Substituting into \( (\ast) \) gives the bound, and \( \rho < 1 \) because \( \lambda_1 > \lambda_2 \). This proves the theorem.
:::

For \( \A = \diag(4,3,2,1) \) and \( \b = (1,1,1,1)/2 \) the constants are \( \tau^2 = 3 \), \( \lambda_1 - \lambda_n = 3 \) and \( \rho = \tfrac12 \), so the bound reads \( 9 \cdot 4^{-(k-1)} \): the values \( 9, 2.25, 0.5625 \) for \( k = 1, 2, 3 \), against the true gaps \( 1.5 \), \( 0.382 \), \( 0.068 \) of @exm-ritz-diagonal. The bound is correct and loose, and the looseness is in Step 3.

It is worth naming what \( \rho \) is. Assume for the rest of this subsection that \( \lambda_2 > \lambda_n \), which the theorem does not require; if instead \( \lambda_2 = \lambda_n \), then \( \rho = 0 \) and the bound of @thm-ritz-extreme-convergence is already as strong as this route can make it. Put
\[
\gamma = \frac{\lambda_1 - \lambda_2}{\lambda_2 - \lambda_n},
\]
the size of the gap above \( \lambda_2 \) measured against the spread of the rest. Then \( 2\lambda_1 - \lambda_2 - \lambda_n = 2(\lambda_1-\lambda_2) + (\lambda_2-\lambda_n) = (\lambda_2-\lambda_n)(1 + 2\gamma) \), so
\[
\rho = \frac{1}{1 + 2\gamma} .
\]
(For \( \A = \diag(4,3,2,1) \), \( \gamma = \tfrac12 \) and \( \rho = \tfrac12 \).) So Step 3 buys a factor \( (1+2\gamma)^{-(k-1)} \) per unit of \( k \), and a small gap makes it nearly worthless.

**What is not proved here.** The polynomial of Step 3 is not the best one. Minimizing \( \max_{i\ge2}\lvert p(\lambda_i)/p(\lambda_1)\rvert \) over the polynomials of degree at most \( k-1 \) with \( p(\lambda_1) = 1 \) is a question about how small a polynomial can be kept on an interval while staying large at a point outside it, and its answer is the Chebyshev polynomial \( T_{k-1} \), shifted and scaled to that interval. The resulting estimate, due to Kaniel, Paige and Saad, is
\[
0 \le \lambda_1 - \theta_1^{(k)} \le \frac{(\lambda_1-\lambda_n)\,\tau^2}{\bigl(T_{k-1}(1 + 2\gamma)\bigr)^{2}} .
\]
The next section defines the Chebyshev polynomials and proves the two facts this bound rests on: that \( T_k \) stays within \( 1 \) on \( [-1,1] \), and that it grows geometrically just outside it; the substitution into \( (\ast) \) is then immediate, but **we do not carry it out here, and nothing in this section depends on it.** The reason it is worth stating is the shape of the improvement. For small \( \gamma \), \( T_{k-1}(1+2\gamma) \) grows roughly like \( (1 + 2\sqrt\gamma)^{k-1} \), where Step 3 managed only \( (1+2\gamma)^{k-1} \). A small gap costs a square root, not a full factor. That is the same square root that the next section extracts for conjugate gradients, and it is the reason Krylov methods are used at all.

## Losing orthogonality

Everything above is exact arithmetic. In the floating-point model of @def-floating-point-model, one feature of the Lanczos recurrence fails, and it fails in a way that is worth describing honestly rather than proving badly.

The three-term recurrence never re-examines \( \q_1, \dots, \q_{j-2} \). In exact arithmetic it does not need to: @thm-lanczos proves that \( \w_j \) is automatically orthogonal to them. In floating-point arithmetic the computed vectors satisfy the recurrence to within a small multiple of \( u\norm{\A} \), and nothing removes the small components along the earlier vectors that rounding introduces. Those components do not stay small.

The mechanism is specific, and it is not random drift. The component of the computed \( \q_{k+1} \) along a Ritz vector \( \x \) grows in inverse proportion to that Ritz pair's residual \( \beta_k\lvert y_k\rvert \). So orthogonality is lost first, and most, in exactly the direction of a Ritz pair that has **converged** — the better the approximation, the faster the basis is corrupted in its direction. The visible symptom is that the computed \( \T_k \) acquires a second copy of a Ritz value that converged several steps earlier, and later a third: the spurious duplicates, which correspond to no extra multiplicity in \( \A \). An algorithm that counts eigenvalues by counting Ritz values will count wrong.

**This paragraph is a description of observed behavior, not a theorem, and this book does not prove it.** The analysis that makes it precise — that the loss of orthogonality is confined to the converged directions, and that the computed \( \T_k \) is the exact tridiagonal matrix of a larger problem — is due to Paige, and it is outside the scope of this chapter. Nothing above depends on it. The standard remedies are to reorthogonalize each new vector against all the earlier ones, which restores the guarantee and abandons the three-term economy, or to reorthogonalize only against the converged Ritz vectors, which is cheaper and rests on precisely the analysis we are not giving. Both are engineering, not theorems, and we label them as such.

## Exercises

### A. Check your understanding

:::: {#exr-krylov-subspaces-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define \( \cK_k(\A,\b) \) and state its dimension in terms of \( m_{\A,\b} \).
2. State the Arnoldi identity of @thm-arnoldi (b), naming the shape of every matrix in it.
3. True or false: for Hermitian \( \A \), the Arnoldi process needs all of \( \q_1, \dots, \q_j \) to produce \( \q_{j+1} \). Justify your answer.
4. What does a breakdown \( h_{k+1,k} = 0 \) mean, and why is it good news?
5. Give the formula for the residual of a Ritz pair, and say why it costs nothing to evaluate.
:::
::::

::: {.solution}
(a) \( \cK_k(\A,\b) = \Span(\b, \A\b, \dots, \A^{k-1}\b) \), and \( \dim\cK_k = \min(k, d) \) with \( d = \deg m_{\A,\b} \) (@prp-krylov-properties).

(b) \( \A\Q_k = \Q_{k+1}\widetilde{\H}_k \), where \( \Q_k \in M_{n\times k} \) and \( \Q_{k+1} \in M_{n\times(k+1)} \) have orthonormal columns and \( \widetilde{\H}_k \in M_{(k+1)\times k} \) is upper Hessenberg; equivalently \( \A\Q_k = \Q_k\H_k + h_{k+1,k}\q_{k+1}\e_k\tp \) with \( \H_k = \Q_k^{*}\A\Q_k \in M_k \) upper Hessenberg.

(c) False. By @thm-lanczos the recurrence has three terms, so only \( \q_{j-1} \) and \( \q_j \) are needed. The reason is that \( \H_k \) is both Hermitian and upper Hessenberg, hence tridiagonal.

(d) It means \( \cK_k \) is \( \A \)-invariant (@thm-arnoldi (c)), equivalently \( k = d \). It is good news because every eigenvalue of \( \H_k \) is then an exact eigenvalue of \( \A \): the method has finished, not failed.

(e) \( \norm{\A\x - \theta\x} = h_{k+1,k}\lvert y_k\rvert \) (@thm-ritz-interlacing (b)). Both factors are already known — \( h_{k+1,k} \) from the last step of the process, \( y_k \) from the small eigenvector — so no multiplication by \( \A \) is needed.
:::

### B. Practice

::: {#exr-krylov-subspaces-b1}
[B1: Dimensions]

For each pair \( (\A, \b) \), determine \( \dim\cK_k(\A,\b) \) for every \( k \ge 1 \). Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \A = \diag(2,2,5) \), \( \b = (1,1,1) \).
2. \( \A = \diag(2,2,5) \), \( \b = (1,-1,0) \).
3. \( \A = \begin{pmatrix} 0 & 1 \\ 0 & 0\end{pmatrix} \), \( \b = \e_2 \).
4. \( \A \) the \( 4 \times 4 \) matrix with \( \A\e_j = \e_{j+1} \) for \( j \le 3 \) and \( \A\e_4 = \0 \), \( \b = \e_1 \).
:::
:::

::: {.solution}
By @prp-krylov-properties (b) the answer is always \( \min(k, d) \) with \( d = \deg m_{\A,\b} \).

(a) \( \b \) has non-zero components in both eigenspaces, so no single factor of \( (x-2)(x-5) \) kills it, while the product does: \( d = 2 \), and the dimensions are \( 1, 2, 2, 2, \dots \).

(b) \( \A\b = (2,-2,0) = 2\b \), so \( \b \) is an eigenvector and \( m_{\A,\b} = x-2 \), \( d = 1 \). The dimensions are \( 1, 1, 1, \dots \): every further product is wasted.

(c) \( \A\e_2 = \e_1 \neq \0 \) and \( \A^2\e_2 = \0 \), so \( m_{\A,\e_2} = x^2 \) and \( d = 2 \): dimensions \( 1, 2, 2, \dots \).

(d) \( \A^{j}\e_1 = \e_{j+1} \) for \( j \le 3 \) and \( \A^4\e_1 = \0 \), so \( m_{\A,\e_1} = x^4 \) and \( d = 4 \): dimensions \( 1, 2, 3, 4, 4, \dots \). Here the Krylov spaces grow as long as they possibly can.
:::

::: {#exr-krylov-subspaces-b2}
[B2: Two Arnoldi steps]

Let
\[
\A = \begin{pmatrix} 2 & 1 & 1 \\ 0 & 2 & 1 \\ 0 & 0 & 1 \end{pmatrix},
\qquad \b = \e_3 .
\]
Carry out two Arnoldi steps. Write down \( \Q_2 \), \( \widetilde{\H}_2 \) and \( \H_2 \), verify @eq-arnoldi, and compute the two Ritz values with their residuals. Hence say which, if either, is a converged eigenvalue estimate.
:::

::: {.solution}
\( \q_1 = \e_3 \) and \( \A\q_1 = (1,1,1) \), so \( h_{11} = \inner{\A\q_1}{\q_1} = 1 \) and
\[
\w_1 = (1,1,1) - (0,0,1) = (1,1,0), \qquad h_{21} = \sqrt2, \qquad \q_2 = \tfrac{1}{\sqrt2}(1,1,0) .
\]
Next \( \A\q_2 = \tfrac{1}{\sqrt2}(3,2,0) \), so \( h_{12} = \inner{\A\q_2}{\q_1} = 0 \) and \( h_{22} = \tfrac12(3+2) = \tfrac52 \), and
\[
\w_2 = \tfrac{1}{\sqrt2}(3,2,0) - \tfrac52\cdot\tfrac{1}{\sqrt2}(1,1,0) = \tfrac{1}{2\sqrt2}(1,-1,0),
\qquad h_{32} = \tfrac12,
\]
with \( \q_3 = \tfrac{1}{\sqrt2}(1,-1,0) \). Hence
\[
\Q_2 = \begin{pmatrix} 0 & \tfrac{1}{\sqrt2} \\ 0 & \tfrac{1}{\sqrt2} \\ 1 & 0\end{pmatrix},
\qquad
\widetilde{\H}_2 = \begin{pmatrix} 1 & 0 \\ \sqrt2 & \tfrac52 \\ 0 & \tfrac12 \end{pmatrix},
\qquad
\H_2 = \begin{pmatrix} 1 & 0 \\ \sqrt2 & \tfrac52\end{pmatrix} .
\]
Check @eq-arnoldi column by column: \( \A\q_1 = (1,1,1) = 1\cdot\q_1 + \sqrt2\,\q_2 \), and \( \A\q_2 = \tfrac{1}{\sqrt2}(3,2,0) = 0\cdot\q_1 + \tfrac52\q_2 + \tfrac12\q_3 \), both correct.

\( \H_2 \) is lower triangular as well as upper Hessenberg, so its eigenvalues are \( \theta = 1 \) and \( \theta = \tfrac52 \). For \( \theta = \tfrac52 \): solving \( \H_2\y = \tfrac52\y \) gives \( y_1 = 0 \), so \( \y = (0,1) \), \( y_2 = 1 \), and the residual is \( h_{32}\lvert y_2\rvert = \tfrac12 \). For \( \theta = 1 \): \( \sqrt2\,y_1 + \tfrac32 y_2 = 0 \), so \( \y = \tfrac{1}{\sqrt{17}}(3, -2\sqrt2) \) and the residual is \( \tfrac12\cdot\tfrac{2\sqrt2}{\sqrt{17}} = \tfrac{\sqrt{34}}{17} \approx 0.343 \).

Neither is converged. The eigenvalues of \( \A \) are \( 2, 2, 1 \), so the Ritz value \( 1 \) is exactly an eigenvalue — yet its residual is \( 0.343 \), not \( 0 \), and its Ritz vector \( \Q_2\y = \tfrac{1}{\sqrt{17}}(-2,-2,3) \) is not an eigenvector: the eigenvectors for \( 1 \) are the multiples of \( (0,1,-1) \), which is not in \( \cK_2 = \Span(\e_3, (1,1,0)) \). The agreement is a coincidence of two numbers, and the residual is what says so.
:::

::: {#exr-krylov-subspaces-b3}
[B3: Lanczos on a tridiagonal matrix]

Let \( \A \in M_n(\nR) \) be symmetric tridiagonal with every subdiagonal entry non-zero, and let \( \b = \e_1 \). Prove that the Lanczos process produces \( \q_j = \pm\e_j \) for every \( j \), and hence that \( \T_n = \A \) up to signs. What does this say about the cost of Lanczos on a matrix that is already tridiagonal?
:::

::: {.solution}
We show by induction on \( j \) that
\[
\A^{j}\e_1 = \sum_{i \le j+1} c^{(j)}_i\e_i
\qquad\text{with}\qquad
c^{(j)}_{j+1} = a_{21}a_{32}\cdots a_{j+1,j} \neq 0 ,
\]
for \( 0 \le j \le n-1 \). At \( j = 0 \) the sum is \( \e_1 \) and the coefficient is the empty product \( 1 \). Suppose it holds at \( j-1 \). Since \( \A \) is tridiagonal, \( \A\e_i \in \Span(\e_{i-1}, \e_i, \e_{i+1}) \), so applying \( \A \) to \( \A^{j-1}\e_1 = \sum_{i\le j}c^{(j-1)}_i\e_i \) lands in \( \Span(\e_1,\dots,\e_{j+1}) \); and the only term contributing to \( \e_{j+1} \) is \( c^{(j-1)}_j\A\e_j \), whose \( \e_{j+1} \)-coefficient is \( c^{(j-1)}_ja_{j+1,j} \neq 0 \), both factors being non-zero. This proves the induction.

Consequently the change-of-basis matrix from \( (\e_1, \dots, \e_j) \) to \( (\e_1, \A\e_1, \dots, \A^{j-1}\e_1) \) is triangular with non-zero diagonal, so \( \cK_j(\A,\e_1) = \Span(\e_1, \dots, \e_j) \) for \( 1 \le j \le n \).

By @thm-arnoldi (a), \( \q_{j} \) is a unit vector in \( \cK_{j} \) orthogonal to \( \cK_{j-1} = \Span(\e_1,\dots,\e_{j-1}) \), hence a unit multiple of \( \e_j \); the sign is fixed by \( \beta_{j-1} > 0 \). Therefore \( (\T_n)_{ij} = \inner{\A\q_j}{\q_i} = \pm a_{ij} \), and since \( \q_j = \varepsilon_j\e_j \) with \( \varepsilon_j = \pm1 \), \( \T_n = \D\A\D \) with \( \D = \diag(\varepsilon_1,\dots,\varepsilon_n) \) — a similarity, so the two have the same eigenvalues.

The cost lesson is that Lanczos does no work at all here beyond rediscovering the matrix: on a tridiagonal matrix with \( \b = \e_1 \) it reproduces \( \A \) and finds nothing early. The method earns its keep when \( n \) is large and only the first few extreme eigenvalues are wanted, so that \( k \ll n \).
:::

### C. Going deeper

::: {#exr-krylov-subspaces-c1}
[C1: Ritz values from the other end]

Let \( \A \in M_n(\nC) \) be Hermitian and let \( \theta_1^{(k)} \ge \dots \ge \theta_k^{(k)} \) be the Ritz values from \( \cK_k(\A,\b) \), \( 1 \le k \le d \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \theta_k^{(k)} \) is non-increasing in \( k \) and that \( \theta_k^{(k)} \ge \lambda_n(\A) \).
2. Deduce a bound for \( \theta_k^{(k)} - \lambda_n(\A) \) from @thm-ritz-extreme-convergence, with no new argument.
3. Show that at \( k = d \) the Ritz values are \( d \) of the eigenvalues of \( \A \), and say which.
:::
:::

::: {.solution}
(a) The argument of Step 1 in the proof of @thm-ritz-extreme-convergence applies verbatim with minima in place of maxima, using the second half of @prp-rayleigh-basic: \( \theta_k^{(k)} = \min\{R_{\A}(\x) : \x \in \cK_k,\ \x \neq \0\} \). A minimum over a larger set is no larger, and \( \cK_k \subseteq \cK_{k+1} \), so the sequence is non-increasing; and the minimum over all of \( \nC^n \) is \( \lambda_n(\A) \), so it is bounded below by that. (Alternatively, both statements are @thm-ritz-interlacing (a) at \( i = k \).)

(b) Apply @thm-ritz-extreme-convergence to \( -\A \). Its eigenvalues are \( -\lambda_n \ge -\lambda_{n-1} \ge \dots \ge -\lambda_1 \), with the same orthonormal eigenbasis in reversed order. Its Krylov spaces from \( \b \) are the same subspaces, because \( (-\A)^{j}\b = (-1)^{j}\A^{j}\b \) and scaling the vectors of a list does not change its span. And \( R_{-\A} = -R_{\A} \), so by Step 1 of the proof the largest Ritz value of \( -\A \) from \( \cK_k \) is \( -\theta_k^{(k)} \). The theorem gives
\[
\theta_k^{(k)} - \lambda_n \le (\lambda_1 - \lambda_n)\,\tilde\tau^2\,\tilde\rho^{\,2(k-1)},
\qquad
\tilde\rho = \frac{\lambda_1 - \lambda_{n-1}}{\lambda_1 + \lambda_{n-1} - 2\lambda_n},
\]
with \( \tilde\tau^2 = \sum_{i \le n-1}\lvert c_i\rvert^2/\lvert c_n\rvert^2 \), provided \( \lambda_{n-1} > \lambda_n \) and \( c_n \neq 0 \).

(c) At \( k = d \) the process breaks down, so \( \cK_d \) is \( \A \)-invariant and every Ritz value is an eigenvalue of \( \A \) by @thm-arnoldi (c). Which ones: writing \( \b = \sum_i c_i\v_i \) in an orthonormal eigenbasis and grouping the eigenvectors by eigenvalue, \( p(\A)\b = \sum_i c_ip(\lambda_i)\v_i \), so \( \cK_d \) is contained in the span of those \( \v_i \) with \( c_i \neq 0 \). The Ritz values are therefore the distinct eigenvalues \( \lambda \) of \( \A \) for which \( \b \) has a non-zero component in \( E_{\lambda}(\A) \), each occurring once; and \( d \) is their number, as @exm-lanczos-breakdown illustrates with \( d = 2 \) for a matrix with eigenvalues \( 5, 2, 2 \).
:::

::: {#exr-krylov-subspaces-c2}
[C2: Shift invariance, and what it costs]

Let \( \A \in M_n(F) \), \( \b \neq \0 \), and let \( \sigma, c \in F \) with \( c \neq 0 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \cK_k(c\A + \sigma\I, \b) = \cK_k(\A, \b) \) for every \( k \).
2. Deduce that the Arnoldi vectors \( \q_j \) are the same for \( \A \) and for \( c\A + \sigma\I \), up to a scalar of modulus one, and that the Ritz values transform by \( \theta \mapsto c\theta + \sigma \).
3. Contrast this with Section 5: explain in two sentences why shifting accelerates the QR algorithm but does **not** accelerate a Krylov method, and what one must do instead to get the effect.
:::
:::

::: {.solution}
(a) Put \( \B = c\A + \sigma\I \). By @prp-krylov-properties (a), \( \cK_k(\B,\b) = \{p(\B)\b : \deg p \le k-1\} \) and \( p(\B) = p(c\A + \sigma\I) = \tilde p(\A) \) where \( \tilde p(x) = p(cx + \sigma) \) has the same degree, \( c \neq 0 \). The map \( p \mapsto \tilde p \) is a bijection of \( F[x]_{\le k-1} \) onto itself, with inverse \( q \mapsto q((x-\sigma)/c) \). So the two sets of vectors coincide.

(b) The Arnoldi vectors are determined by the flag \( \cK_1 \subseteq \cK_2 \subseteq \dots \) alone, up to a scalar of modulus one: \( \q_j \) is a unit vector in \( \cK_j \) orthogonal to \( \cK_{j-1} \) (@thm-arnoldi (a)), and the unit vectors of \( \cK_j \cap \cK_{j-1}^{\perp} \) are exactly the modulus-one multiples of one of them. By (a) the flag is the same for \( \B \) as for \( \A \), so the run on \( \B \) produces \( \Q_k^{\B} = \Q_k\D \) with \( \D = \diag(d_1, \dots, d_k) \) and \( \lvert d_j\rvert = 1 \). The scalars need not all be \( 1 \): each run fixes its own by \( h_{j,j-1} > 0 \), and for \( c = -1 \), \( \sigma = 0 \), \( \A = \diag(4,3,2,1) \) and \( \b = (1,1,1,1) \) the two runs give \( \q_j^{\B} = (-1)^{j-1}\q_j \). Consequently
\[
(\Q_k^{\B})^{*}\B\,\Q_k^{\B} = \D^{*}\bigl(c\,\Q_k^{*}\A\Q_k + \sigma\Q_k^{*}\Q_k\bigr)\D = \D^{*}(c\H_k + \sigma\I_k)\D ,
\]
whose eigenvalues, \( \D \) being unitary, are those of \( c\H_k + \sigma\I_k \), namely \( c\theta_i + \sigma \).

(c) The QR algorithm converges at a rate governed by ratios \( \lvert\lambda_{i+1} - \mu\rvert/\lvert\lambda_i - \mu\rvert \), and those ratios genuinely change with \( \mu \); a Krylov space does not change at all under a shift, by (a), so nothing it produces can change either. To get the analogous effect one must change the space, not the matrix: apply the method to \( (\A - \mu\I)^{-1} \), whose Krylov spaces are different, which is the Krylov version of the inverse iteration of @thm-inverse-iteration and costs a factorization of \( \A - \mu\I \) rather than a matrix-vector product.
:::

::: {#exr-krylov-subspaces-c3}
[C3: When the Krylov space is everything]

Let \( \A \in M_n(F) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that there exists \( \b \) with \( \cK_n(\A,\b) = F^n \) if and only if \( m_{\A} = p_{\A} \).
2. Prove that in that case the Arnoldi process run to \( k = n \) produces a unitary \( \Q_n \) with \( \Q_n^{*}\A\Q_n \) upper Hessenberg, all of whose subdiagonal entries are non-zero.
3. Hence give a second proof of @thm-hessenberg-form over \( \nC \) for such \( \A \), and explain why it does not replace Chapter 11's.
:::

*Hint for (a): Chapter 10 §05 calls such a \( \b \) a cyclic vector.*
:::

::: {.solution}
(a) \( \cK_n(\A,\b) = F^n \) means \( \dim\cK_n = n \), which by @prp-krylov-properties (b) means \( \deg m_{\A,\b} = n \), that is, \( Z(\b;\A) = F^n \) and \( \b \) is a cyclic vector for \( \A \) (@def-cyclic-vector). By @thm-cyclic-iff-min-equals-char, such a vector exists exactly when \( m_{\A} = p_{\A} \).

(b) With \( d = n \), @thm-arnoldi (a) says that \( h_{j+1,j} \neq 0 \) for every \( j < n \) and that \( (\q_1, \dots, \q_n) \) is an orthonormal basis of \( F^n \); so \( \Q_n \) is unitary, and \( \Q_n^{*}\A\Q_n = \H_n \) is upper Hessenberg by @thm-arnoldi (b). Its subdiagonal entries are the \( h_{j+1,j} \), all non-zero. (A Hessenberg matrix with this property is called **unreduced**, and @prp-exact-shift-deflates is about exactly these.)

(c) Part (b) exhibits a unitary \( \Q_n \) with \( \Q_n^{*}\A\Q_n \) upper Hessenberg, which is the conclusion of @thm-hessenberg-form. It does not replace that theorem for two reasons. First, it needs \( m_{\A} = p_{\A} \) by (a), while @thm-hessenberg-form holds for every square matrix; when no cyclic vector exists, the process breaks down at some \( d < n \) and delivers an invariant subspace instead of a full basis. Second, @thm-hessenberg-form is proved by reflections, each applied to the whole matrix, and its \( O(n^3) \) cost is what Section 5 assumed; the Arnoldi route needs \( n \) matrix-vector products and \( O(n^3) \) orthogonalization work as well, and in floating-point arithmetic the orthogonality it produces is exactly what the last subsection says can be lost. The two constructions agree in exact arithmetic when both apply, and the reflection route is the one that is run.
:::
