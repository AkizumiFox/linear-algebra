# PageRank

A search engine that finds thousands of pages containing a word must decide which to list first. One answer, which made a search engine famous, is to let the pages vote. Each page spreads its vote over the pages it links to, a vote counts for more when it comes from a page that is itself important, and "important" is whatever this circular description settles on. Written out, the circle is an eigenvector equation for a stochastic matrix. This section sets up that matrix, shows why the raw web does not give a well-defined ranking, repairs it with a single parameter, and uses Perron's theorem (@thm-perron) to prove that the repaired matrix has exactly one ranking, with every entry positive. We then prove how fast the ranking can be computed, and work a small web exactly.

Throughout, the field is \( \nR \), inequalities between vectors and matrices are entrywise as in §01, and **stochastic** means column-stochastic (@def-stochastic-matrix): non-negative entries, every column adding up to \( 1 \). Many accounts of PageRank use rows instead; their matrices are the transposes of ours. We write \( \1 \) for the all-ones vector and \( \J = \1\1\tp \) for the all-ones matrix.

## The web as a Markov chain

Number the pages \( 1, \dots, n \). Page \( j \) **links to** page \( i \) if it contains a link to it; we ignore links from a page to itself, and several links from \( j \) to \( i \) count as one. Let \( d_j \) be the number of pages that page \( j \) links to, its **out-degree**. A page with \( d_j = 0 \) is called **dangling**: a document with no links out, such as an image or a file.

Imagine a surfer who, on page \( j \), clicks one of its \( d_j \) links, each with probability \( 1/d_j \). If \( \x_k \) is the probability vector of the surfer's position after \( k \) clicks, then, exactly as in Chapter 9 §11, \( \x_{k+1} = \H\x_k \), where \( h_{ij} = 1/d_j \) if \( j \) links to \( i \) and \( h_{ij} = 0 \) otherwise. This hyperlink matrix \( \H \) is local to this section; elsewhere in the book \( \H \) is a Hessian. The long-run share of time the surfer spends on page \( i \) is the candidate for page \( i \)'s importance. It captures the circular description: page \( i \) receives, from each page \( j \) linking to it, the share \( 1/d_j \) of \( j \)'s own weight.

At a dangling page the surfer has nowhere to go, and column \( j \) of \( \H \) is zero. The standard patch sends the surfer to a page chosen uniformly at random.

::: {#def-link-matrix}
[Link Matrix]

Let a web have pages \( 1, \dots, n \), with \( n \ge 1 \), and out-degrees \( d_1, \dots, d_n \). Its **link matrix** is the \( n \times n \) matrix \( \P \) whose column \( j \) is:

::: {.enumerate options="label=(\alph*)"}
1. if \( d_j \ge 1 \): the vector with entry \( 1/d_j \) in each position \( i \) such that page \( j \) links to page \( i \), and \( 0 \) elsewhere;
2. if \( d_j = 0 \) (page \( j \) is **dangling**): the vector \( \tfrac1n\1 \).
:::
:::

Each column is a probability vector: in case (a) it has \( d_j \) entries equal to \( 1/d_j \), and in case (b) \( n \) entries equal to \( 1/n \). So \( \P \) is stochastic. For instance, the web on three pages in which page \( 1 \) links to pages \( 2 \) and \( 3 \), page \( 2 \) links to page \( 3 \), and page \( 3 \) links nowhere, has
\[
\P = \begin{pmatrix} 0 & 0 & \tfrac13 \\ \tfrac12 & 0 & \tfrac13 \\ \tfrac12 & 1 & \tfrac13 \end{pmatrix} .
\]

A ranking should then be a steady state of \( \P \) (@def-markov-chain): a probability vector \( \x \) with \( \P\x = \x \). When \( \P \) is irreducible (@def-irreducible), there is exactly one, with every entry positive, by @prp-stochastic-perron (c); part (a) of the same proposition gives \( \rho(\P) = 1 \) for every stochastic \( \P \). The real web is very far from irreducible, and the three failures below are the typical ones.

::: {#exm-link-matrix-failures}
[Three ways a web can fail to rank]

For each web, describe what goes wrong with the surfer's chain.

::: {.enumerate options="label=(\alph*)"}
1. Two pages; page \( 1 \) links to page \( 2 \), and page \( 2 \) is dangling, but we use \( \H \), without the patch.
2. Four pages; pages \( 1 \) and \( 2 \) link to each other, and so do pages \( 3 \) and \( 4 \).
3. Two pages that link to each other.
:::
:::

::: {.solution}
(a) \( \H = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \) has a zero column, so it is not stochastic, and \( \H^2 = \0 \). From any start the surfer is gone after two clicks: \( \H^2\x_0 = \0 \) is not a probability vector, and \( \H \) has no steady state at all, since \( \H\x = \x \) forces \( x_1 = 0 \) and then \( x_2 = x_1 = 0 \). The patched \( \P \) has second column \( (\tfrac12, \tfrac12) \) and the steady state \( (\tfrac13, \tfrac23) \), since \( \P(1, 2) = (0 \cdot 1 + \tfrac12 \cdot 2,\ 1 \cdot 1 + \tfrac12 \cdot 2) = (1, 2) \).

(b) \( \P \) is block diagonal with two copies of the swap \( \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \). Both \( (\tfrac12, \tfrac12, 0, 0) \) and \( (0, 0, \tfrac12, \tfrac12) \) are steady states, and so is every average of the two. The chain cannot say whether page \( 1 \) matters more than page \( 3 \): the ranking is not unique.

(c) \( \P \) is the swap. Its steady state \( (\tfrac12, \tfrac12) \) is unique, but from \( \x_0 = \e_1 \) the chain alternates \( \e_1, \e_2, \e_1, \dots \) and never settles. The eigenvalue \( -1 \) of the swap has the same modulus as \( 1 \).
:::

In (b) the matrix is reducible, and in (c) it is irreducible but not primitive (@def-primitive): the powers of the swap are \( \I \) and the swap, and neither is positive. Real webs have all three features, on a vast scale.

## The Google matrix

The dangling patch of @def-link-matrix already repairs failure (a). One modification repairs the remaining two at once. Let the surfer, at every step, toss a biased coin: with probability \( \alpha \) follow a link as before, and with probability \( 1 - \alpha \) get bored and jump to a page chosen uniformly at random from all \( n \). The jump is called **teleportation**, and \( \alpha \) the **damping factor**; a value around \( 0.85 \) is customary.

*The Google matrix mixes following links with jumping to a random page; its fixed probability vector is the ranking.*

::: {#def-google-matrix}
[Google Matrix, PageRank Vector]

Let \( \P \in M_n(\nR) \) be the link matrix of a web with \( n \ge 1 \) pages, and let \( 0 < \alpha < 1 \). The matrix
\[
\G = \alpha\P + \frac{1 - \alpha}{n}\,\J
\]
is called the **Google matrix** in the literature, with damping factor \( \alpha \).
A **PageRank vector** of the web is a probability vector \( \vpi \in \nR^n \) with \( \G\vpi = \vpi \). Page \( i \) is ranked above page \( k \) when \( \pi_i > \pi_k \).
:::

In words: column \( j \) of \( \G \) is \( \alpha \) times column \( j \) of \( \P \), the link step, plus \( 1 - \alpha \) times the uniform vector \( \tfrac1n\1 \), the jump. A PageRank vector is a steady state of the surfer's new chain. The letter \( \G \) is local to this section; elsewhere in the book \( \G \) is a Gram matrix. The theorem below shows that there is exactly one, which justifies calling it **the** PageRank vector.

Two properties of \( \G \) do all the work.

- **\( \G \) is stochastic.** Its entries are non-negative, and column \( j \) adds up to \( \alpha \cdot 1 + (1 - \alpha)\cdot\tfrac1n \cdot n = 1 \).
- **\( \G \) is positive.** Every entry is at least \( \tfrac{1 - \alpha}{n} > 0 \), because \( \alpha\P \ge \0 \) and \( \alpha < 1 \) **strictly**.

Two degenerate values of \( \alpha \) are excluded, and each shows why. With \( \alpha = 1 \), \( \G = \P \), and the failures (b) and (c) of @exm-link-matrix-failures come back. With \( \alpha = 0 \), \( \G = \tfrac1n\J \) for every web, the PageRank vector is \( \tfrac1n\1 \), and the links are ignored: every page ties. The damping factor trades faithfulness to the links against the good behavior of the chain, and we will see that the speed of the computation is governed by \( \alpha \) alone.

For the three-page web above, with \( \alpha = \tfrac12 \),
\[
\G = \frac12\P + \frac16\J = \begin{pmatrix} \tfrac16 & \tfrac16 & \tfrac13 \\ \tfrac5{12} & \tfrac16 & \tfrac13 \\ \tfrac5{12} & \tfrac23 & \tfrac13 \end{pmatrix} ,
\]
with columns adding up to \( 1 \) and every entry positive.

**A non-example by minimal change.** Replace the uniform jump by a jump to page \( 1 \) only: \( \G' = \alpha\P + (1 - \alpha)\e_1\1\tp \). It is still stochastic, since each column of \( \e_1\1\tp \) is \( \e_1 \). What fails is positivity: in the web of @exm-link-matrix-failures (b), \( \G' \) has zeros in rows \( 3 \) and \( 4 \) of columns \( 1 \) and \( 2 \), so Perron's theorem no longer applies. (Here the ranking is still unique, but it gives pages \( 3 \) and \( 4 \) weight zero, since no surfer ever returns to them from pages \( 1 \) and \( 2 \).) Exercise B3 shows that any jump distribution with all entries positive works as well as the uniform one.

::: {.warning}
**PageRank is not a count of incoming links.** A link is worth the rank of the page it comes from, divided by that page's out-degree. In the four-page example at the end of this section, page \( 3 \) has more incoming links than any other page, yet page \( 1 \), with a single incoming link, ranks above it, because that link comes from page \( 3 \) and is page \( 3 \)'s only link.
:::

## A unique positive ranking

Perron's theorem, applied to the positive matrix \( \G \), settles existence, uniqueness and positivity at once. It also turns the eigenvector problem into a linear system.

::: {#thm-pagerank-vector}
[The PageRank Vector]

Let \( \P \in M_n(\nR) \) be stochastic, \( 0 < \alpha < 1 \), and \( \G = \alpha\P + \frac{1-\alpha}{n}\J \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \rho(\G) = 1 \), and \( 1 \) is an eigenvalue of \( \G \) of algebraic multiplicity one;
2. there is **exactly one** probability vector \( \vpi \) with \( \G\vpi = \vpi \), and every entry of \( \vpi \) is **positive**;
3. \( \I - \alpha\P \) is invertible, and \( \vpi \) is the unique solution of
\[
(\I - \alpha\P)\,\vpi = \frac{1 - \alpha}{n}\,\1 .
\]
:::
:::

::: {.idea}
Perron's theorem hands us a simple eigenvalue \( \rho(\G) \) with a positive eigenvector, so the only question is the value of \( \rho(\G) \); the column sums pin it at \( 1 \). For (c), on probability vectors the rank-one part \( \frac{1-\alpha}{n}\J\x \) is the constant vector \( \frac{1-\alpha}{n}\1 \), so the eigenvector equation becomes linear with a right-hand side.
:::

::: {.proof}
(a) By @thm-operator-norm-formulas (a), \( \norm{\G}_1 \) is the largest column sum of \( \lvert\G\rvert \), which is \( 1 \) since \( \G \) is stochastic; so \( \rho(\G) \le 1 \) by @thm-spectral-radius-le-norm (a). By @prp-stochastic-properties (c), \( 1 \) is an eigenvalue of \( \G \). Hence \( \rho(\G) = 1 \). Since every entry of \( \G \) is at least \( \frac{1-\alpha}{n} > 0 \), Perron's theorem (@thm-perron) applies: by its parts (a) and (b), \( \rho(\G) = 1 \) is an eigenvalue of algebraic multiplicity one, with an eigenvector \( \v > \0 \) spanning \( E_1(\G) \).

(b) Put \( \vpi = \v/(\1\tp\v) \), which is defined because \( \1\tp\v > 0 \). It is a probability vector with positive entries and \( \G\vpi = \vpi \). If \( \vpi' \) is another probability vector with \( \G\vpi' = \vpi' \), then \( \vpi' \) lies in \( E_1(\G) = \Span(\v) \), so \( \vpi' = c\vpi \) for some \( c \), and comparing entry sums gives \( 1 = c \). Hence \( \vpi' = \vpi \). In the language of §01, \( \vpi \) is the Perron vector of \( \G \) (@def-perron-vector).

(c) If \( (\I - \alpha\P)\z = \0 \) with \( \z \ne \0 \), then \( \P\z = \alpha^{-1}\z \), so \( \alpha^{-1} > 1 \) is an eigenvalue of \( \P \); but \( \rho(\P) \le \norm{\P}_1 = 1 \) as in (a). So \( 0 \) is not an eigenvalue of \( \I - \alpha\P \), and \( \I - \alpha\P \) is invertible by @thm-invertible-tfae-eigen. For a probability vector \( \x \), \( \J\x = \1(\1\tp\x) = \1 \), so
\[
\G\x = \alpha\P\x + \frac{1 - \alpha}{n}\,\1 ,
\]
and \( \G\vpi = \vpi \) is the equation \( (\I - \alpha\P)\vpi = \frac{1-\alpha}{n}\1 \). So \( \vpi \) solves the system, and by invertibility it is the only solution.
:::

So the ranking exists, is unique, and gives every page a positive score: no page is ignored, however obscure. Part (c) is how one computes it for a small web: solve an \( n \times n \) linear system, with no eigenvalue in sight. A useful bonus is that the solution of (c) is automatically a probability vector. Multiplying the system on the left by \( \1\tp \), and using \( \1\tp\P = \1\tp \),
\[
(1 - \alpha)\,\1\tp\vpi = \frac{1 - \alpha}{n}\,\1\tp\1 = 1 - \alpha ,
\]
so \( \1\tp\vpi = 1 \) without being imposed.

::: {.check}
Two pages link to each other, and \( \alpha = \tfrac12 \). Write down \( \G \), find \( \vpi \), and find the eigenvalues of \( \G \).
:::

::: {.solution}
\( \P \) is the swap, so
\[
\G = \frac12\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} + \frac14\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} \tfrac14 & \tfrac34 \\ \tfrac34 & \tfrac14 \end{pmatrix} .
\]
Then \( \G(1, 1) = (1, 1) \) and \( \G(1, -1) = (-\tfrac12, \tfrac12) = -\tfrac12(1, -1) \). So \( \vpi = (\tfrac12, \tfrac12) \), and the eigenvalues are \( 1 \) and \( -\tfrac12 \). The swap has eigenvalues \( 1 \) and \( -1 \): the second one has been multiplied by \( \alpha \). The next theorem says that this always happens.
:::

## The second eigenvalue

The PageRank vector of a real web is computed by iterating \( \x_{k+1} = \G\x_k \), since the web has billions of pages and no one solves a system of that size exactly. How fast the iterates settle depends on the eigenvalues of \( \G \) other than \( 1 \). For a general positive matrix, Perron's theorem says only that they are strictly smaller than \( \rho \) in modulus, with no bound on how much smaller. For the Google matrix there is an exact description.

::: {#thm-google-matrix-eigenvalues}
[The Eigenvalues of the Google Matrix]

Let \( n \ge 2 \), let \( \P \in M_n(\nR) \) be stochastic, let \( 0 \le \alpha \le 1 \), and let \( \G = \alpha\P + \frac{1-\alpha}{n}\J \). Since \( 1 \) is an eigenvalue of \( \P \) (@prp-stochastic-properties) and \( p_{\P} \) splits over \( \nC \) (@thm-fundamental-theorem-of-algebra), it factors as \( p_{\P}(x) = (x - 1)(x - \mu_2)\cdots(x - \mu_n) \) with \( \mu_2, \dots, \mu_n \in \nC \). Then
\[
p_{\G}(x) = (x - 1)(x - \alpha\mu_2)\cdots(x - \alpha\mu_n) .
\]
In particular, if \( \alpha < 1 \), every eigenvalue \( \lambda \ne 1 \) of \( \G \) satisfies \( \lvert\lambda\rvert \le \alpha \).
:::

::: {.idea}
Both \( \P \) and \( \G \) have \( \1\tp \) as a left eigenvector for \( 1 \). Change basis so that \( \1\tp \) becomes the first coordinate functional \( \e_1\tp \); then both matrices become block lower triangular with a \( 1 \) in the corner. The teleportation term \( \frac1n\J = \frac1n\1\1\tp \) only touches the first column in the new basis, so the lower-right blocks are \( \P_1 \) and \( \alpha\P_1 \) for the **same** \( \P_1 \). The eigenvalues of \( \P \) other than the \( 1 \) in the corner are those of \( \P_1 \); those of \( \G \) are \( \alpha \) times them.
:::

::: {.proof}
Let \( \N = \e_1(\1 - \e_1)\tp \), the matrix whose first row is \( (0, 1, \dots, 1) \) and whose other rows are zero, and let \( \S = \I + \N \). Its first row is \( \1\tp \) and its other rows are those of \( \I \), so \( \e_1\tp\S = \1\tp \). Since \( (\1 - \e_1)\tp\e_1 = 0 \), \( \N^2 = \e_1\bigl((\1 - \e_1)\tp\e_1\bigr)(\1 - \e_1)\tp = \0 \), and therefore \( (\I + \N)(\I - \N) = \I - \N^2 = \I \). So \( \S \) is invertible with \( \S^{-1} = \I - \N \) (@thm-one-sided-inverse).

::: {.claim}
**Claim.** If \( \M \in M_n(\nR) \) satisfies \( \1\tp\M = \1\tp \), then the first row of \( \S\M\S^{-1} \) is \( \e_1\tp \).
:::

::: {.proof}
The first row is \( \e_1\tp\S\M\S^{-1} = \1\tp\M\S^{-1} = \1\tp\S^{-1} = \e_1\tp\S\S^{-1} = \e_1\tp \).
:::

Since \( \P \) is stochastic, \( \1\tp\P = \1\tp \), and the claim gives
\[
\S\P\S^{-1} = \begin{pmatrix} 1 & \0\tp \\ \b & \P_1 \end{pmatrix}
\]
for some \( \b \in \nR^{n-1} \) and \( \P_1 \in M_{n-1}(\nR) \). For the teleportation term,
\[
\S\bigl(\tfrac1n\1\1\tp\bigr)\S^{-1} = \tfrac1n(\S\1)(\1\tp\S^{-1}) = \tfrac1n(\S\1)\,\e_1\tp ,
\]
using \( \1\tp\S^{-1} = \e_1\tp \) from the proof of the claim. Its only non-zero column is the first, \( \tfrac1n\S\1 \), whose first entry is \( \tfrac1n\1\tp\1 = 1 \). So it equals \( \begin{pmatrix} 1 & \0\tp \\ \c & \0 \end{pmatrix} \) for some \( \c \in \nR^{n-1} \), and
\[
\begin{aligned}
\S\G\S^{-1} &= \alpha\,\S\P\S^{-1} + (1 - \alpha)\,\S\bigl(\tfrac1n\J\bigr)\S^{-1} \\
&= \begin{pmatrix} 1 & \0\tp \\ \alpha\b + (1-\alpha)\c & \alpha\P_1 \end{pmatrix} .
\end{aligned}
\]
Similar matrices have the same characteristic polynomial (@thm-charpoly-similarity-invariant), and \( x\I \) minus a block lower triangular matrix is block lower triangular, so by @thm-det-block-triangular
\[
p_{\P}(x) = (x - 1)\,p_{\P_1}(x) , \qquad p_{\G}(x) = (x - 1)\,p_{\alpha\P_1}(x) .
\]
Comparing the first with \( p_{\P}(x) = (x - 1)(x - \mu_2)\cdots(x - \mu_n) \) and canceling the non-zero factor \( x - 1 \) (in \( \nC[x] \), a product of non-zero polynomials is non-zero) gives \( p_{\P_1}(x) = (x - \mu_2)\cdots(x - \mu_n) \). If \( \alpha > 0 \), then
\[
\begin{aligned}
p_{\alpha\P_1}(x) &= \det(x\I - \alpha\P_1) = \alpha^{n-1}\det\bigl(\tfrac{x}{\alpha}\I - \P_1\bigr) \\
&= \alpha^{n-1}\prod_{j=2}^{n}\Bigl(\frac{x}{\alpha} - \mu_j\Bigr) = \prod_{j=2}^{n}(x - \alpha\mu_j) ,
\end{aligned}
\]
where the second step takes the factor \( \alpha \) out of each of the \( n - 1 \) rows. If \( \alpha = 0 \), then \( p_{\alpha\P_1}(x) = \det(x\I) = x^{n-1} = \prod_j(x - 0\cdot\mu_j) \). Either way the formula for \( p_{\G} \) follows.

For the last sentence, each \( \mu_j \) is an eigenvalue of \( \P \), so \( \lvert\mu_j\rvert \le \rho(\P) \le \norm{\P}_1 = 1 \) by @thm-spectral-radius-le-norm (a) and @thm-operator-norm-formulas (a). The eigenvalues of \( \G \) are the roots of \( p_{\G} \): the number \( 1 \) and the \( \alpha\mu_j \), each of modulus at most \( \alpha \). If \( \alpha < 1 \), none of the \( \alpha\mu_j \) equals \( 1 \), so every eigenvalue \( \lambda \ne 1 \) is some \( \alpha\mu_j \), and \( \lvert\lambda\rvert \le \alpha \). This proves the theorem.
:::

The theorem gives more than a bound. It shows again that \( 1 \) is a simple eigenvalue of \( \G \) when \( \alpha < 1 \), without Perron's theorem, and it says that the rest of the spectrum of \( \G \) is the rest of the spectrum of \( \P \), shrunk by the factor \( \alpha \). The bound is attained whenever \( \P \) itself has \( 1 \) as a repeated eigenvalue, as for the two separate webs of @exm-link-matrix-failures (b) (Exercise C2), and whenever \( \P \) has \( -1 \) as an eigenvalue, as in the Quick check. So for a web with two or more pieces that no link leaves, as large webs typically have, the second eigenvalue of \( \G \) has modulus exactly \( \alpha \), and no better bound is possible.

## How fast the iteration converges

The eigenvalue bound predicts that iterates approach \( \vpi \) at a rate like \( \alpha^k \). For this particular matrix the prediction can be proved directly, with an explicit constant, by measuring errors in the \( 1 \)-norm of Chapter 16.

::: {#prp-pagerank-contraction}
[Convergence at the Damping Rate]

Let \( \P \), \( \alpha \), \( \G \) and \( \vpi \) be as in @thm-pagerank-vector, let \( \x_0 \) be any probability vector, and let \( \x_k = \G^k\x_0 \). Then for every \( k \ge 0 \),
\[
\norm{\x_k - \vpi}_1 \le \alpha^k\norm{\x_0 - \vpi}_1 \le 2\alpha^k .
\]
In particular, \( \x_k \to \vpi \) entrywise.
:::

::: {.idea}
The error \( \vepsilon_k = \x_k - \vpi \) is a difference of probability vectors, so its entries add up to \( 0 \), and the teleportation term kills it. What remains is \( \alpha\P \), and a stochastic matrix never increases the \( 1 \)-norm.
:::

::: {.proof}
Each \( \x_k \) is a probability vector by @prp-stochastic-properties (a), since \( \G \) is stochastic. Put \( \vepsilon_k = \x_k - \vpi \), so \( \1\tp\vepsilon_k = 1 - 1 = 0 \). Since \( \G\vpi = \vpi \),
\[
\vepsilon_{k+1} = \G\x_k - \G\vpi = \G\vepsilon_k = \alpha\P\vepsilon_k + \frac{1 - \alpha}{n}\,\1(\1\tp\vepsilon_k) = \alpha\P\vepsilon_k .
\]
By @thm-operator-norm-formulas (a), \( \norm{\P}_1 = 1 \), the largest column sum of the non-negative matrix \( \P \), so \( \norm{\P\vepsilon_k}_1 \le \norm{\vepsilon_k}_1 \) (@def-operator-norm). Hence \( \norm{\vepsilon_{k+1}}_1 \le \alpha\norm{\vepsilon_k}_1 \), and by induction on \( k \), \( \norm{\vepsilon_k}_1 \le \alpha^k\norm{\vepsilon_0}_1 \). Finally \( \norm{\vepsilon_0}_1 \le \norm{\x_0}_1 + \norm{\vpi}_1 = 2 \), as both are probability vectors. Each entry of \( \vepsilon_k \) has modulus at most \( \norm{\vepsilon_k}_1 \le 2\alpha^k \), and \( \alpha^k \to 0 \) because \( 0 < \alpha < 1 \), one of the calculus facts recorded in Chapter 9 §11. A sequence whose terms are at most \( 2\alpha^k \) in absolute value, with \( 2\alpha^k \to 0 \), tends to \( 0 \) straight from the definition of a limit: once \( 2\alpha^k < \varepsilon \), so is every such term. So \( \x_k \to \vpi \) entrywise.
:::

The bound does not depend on the web at all: not on the number of pages, not on how they link. With \( \alpha = 0.85 \), fifty steps guarantee \( \norm{\x_{50} - \vpi}_1 \le 2(0.85)^{50} < 6 \cdot 10^{-4} \), and ninety guarantee an error below \( 10^{-6} \), for a web of any size. Each step is cheap, because \( \G \) is never formed: by the proof of @thm-pagerank-vector (c), \( \G\x = \alpha\P\x + \frac{1-\alpha}{n}\1 \) for a probability vector \( \x \), and \( \P\x \) needs one operation per link, plus one shared correction for the dangling pages.

In the language of §05, \( \G \) is primitive (@def-primitive), since \( \G^1 \) is already positive, and @thm-primitive-limit gives \( \G^k \to \vpi\1\tp \), with right Perron vector \( \vpi \) and left Perron vector \( \1 \), normalized by \( \1\tp\vpi = 1 \). The proposition adds the rate, and the rate is what makes the method practical. The iteration \( \x_{k+1} = \G\x_k \) is the **power method**; Chapter 24 studies it for general matrices, where the rate is governed by the ratio of the two largest eigenvalue moduli, here at most \( \alpha \).

## A small web, exactly

::: {#exm-pagerank-four-pages}
[Four pages, one dangling]

A web has four pages. Page \( 1 \) links to pages \( 2 \) and \( 3 \); page \( 2 \) links to pages \( 3 \) and \( 4 \); page \( 3 \) links to page \( 1 \); page \( 4 \) is dangling. With \( \alpha = \tfrac45 \), find the Google matrix, the PageRank vector and the ranking, and compare \( \lvert\lambda_2\rvert \) with \( \alpha \).
:::

::: {.solution}
*The link matrix.* Pages \( 1 \) and \( 2 \) have out-degree \( 2 \), page \( 3 \) has out-degree \( 1 \), and page \( 4 \) is dangling, so by @def-link-matrix
\[
\P = \begin{pmatrix} 0 & 0 & 1 & \tfrac14 \\ \tfrac12 & 0 & 0 & \tfrac14 \\ \tfrac12 & \tfrac12 & 0 & \tfrac14 \\ 0 & \tfrac12 & 0 & \tfrac14 \end{pmatrix} , \qquad
20\,\G = 16\,\P + \J = \begin{pmatrix} 1 & 1 & 17 & 5 \\ 9 & 1 & 1 & 5 \\ 9 & 9 & 1 & 5 \\ 1 & 9 & 1 & 5 \end{pmatrix} ,
\]
since \( 20\alpha = 16 \) and \( 20 \cdot \frac{1-\alpha}{4} = 1 \). Every column of \( 20\G \) adds up to \( 20 \), and every entry is positive.

*The linear system.* By @thm-pagerank-vector (c), \( (\I - \tfrac45\P)\vpi = \tfrac1{20}\1 \). Multiplying by \( 5 \) gives \( (5\I - 4\P)\vpi = \tfrac14\1 \), that is,
\[
\begin{aligned}
5\pi_1 - 4\pi_3 - \pi_4 &= \tfrac14 , &\qquad -2\pi_1 + 5\pi_2 - \pi_4 &= \tfrac14 , \\
-2\pi_1 - 2\pi_2 + 5\pi_3 - \pi_4 &= \tfrac14 , &\qquad -2\pi_2 + 4\pi_4 &= \tfrac14 .
\end{aligned}
\]
Express everything through \( \pi_4 \). The fourth equation gives \( \pi_2 = 2\pi_4 - \tfrac18 \). The second then gives \( 2\pi_1 = 5\pi_2 - \pi_4 - \tfrac14 = 9\pi_4 - \tfrac78 \), so \( \pi_1 = \tfrac92\pi_4 - \tfrac7{16} \). The first gives \( 4\pi_3 = 5\pi_1 - \pi_4 - \tfrac14 = \tfrac{43}{2}\pi_4 - \tfrac{39}{16} \), so \( \pi_3 = \tfrac{43}{8}\pi_4 - \tfrac{39}{64} \). Substituting into the third,
\[
\Bigl(-9 - 4 + \tfrac{215}{8} - 1\Bigr)\pi_4 + \Bigl(\tfrac78 + \tfrac14 - \tfrac{195}{64}\Bigr) = \tfrac{103}{8}\pi_4 - \tfrac{123}{64} = \tfrac14 ,
\]
so \( \tfrac{103}{8}\pi_4 = \tfrac{139}{64} \) and \( \pi_4 = \tfrac{139}{824} \). Back-substituting,
\[
\vpi = \frac{1}{824}\,(265,\ 175,\ 245,\ 139) .
\]
*Check.* The entries add up to \( 824/824 = 1 \), as they must. With \( \y = (265, 175, 245, 139) \), the first row of \( 20\G \) gives \( 265 + 175 + 17 \cdot 245 + 5 \cdot 139 = 5300 = 20 \cdot 265 \), and the other rows give \( 3500 = 20 \cdot 175 \), \( 4900 = 20 \cdot 245 \) and \( 2780 = 20 \cdot 139 \). So \( \G\vpi = \vpi \).

*The ranking.* Page \( 1 \) first (\( \approx 0.322 \)), then page \( 3 \) (\( \approx 0.297 \)), page \( 2 \) (\( \approx 0.212 \)) and page \( 4 \) (\( \approx 0.169 \)). Page \( 3 \) is linked from pages \( 1 \) and \( 2 \), while the dangling page \( 4 \) feeds every page equally; page \( 1 \) is linked only from page \( 3 \). Yet page \( 1 \) wins, because page \( 3 \) passes its whole weight to it, while pages \( 1 \), \( 2 \) and \( 4 \) split theirs.

*The second eigenvalue.* Expanding the determinant gives
\[
\begin{aligned}
p_{\P}(x) &= (x - 1)\Bigl(x^3 + \tfrac34x^2 + \tfrac18x - \tfrac1{16}\Bigr) , \\
p_{\G}(x) &= (x - 1)\Bigl(x^3 + \tfrac35x^2 + \tfrac{2}{25}x - \tfrac{4}{125}\Bigr) ,
\end{aligned}
\]
and the second cubic is \( \alpha^3 \) times the first evaluated at \( x/\alpha \), as @thm-google-matrix-eigenvalues predicts: \( \tfrac34 \cdot \tfrac45 = \tfrac35 \), \( \tfrac18 \cdot \tfrac{16}{25} = \tfrac{2}{25} \), \( \tfrac1{16} \cdot \tfrac{64}{125} = \tfrac{4}{125} \). The cubic for \( \P \) has one real root near \( 0.199 \) and two complex ones of modulus about \( 0.560 \). So \( \lvert\lambda_2(\G)\rvert \approx 0.8 \times 0.560 \approx 0.448 \), comfortably below \( \alpha = 0.8 \): for this web the iteration converges faster than @prp-pagerank-contraction guarantees.
:::

## Exercises

### A. Check your understanding

:::: {#exr-pagerank-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the Google matrix of a web and its PageRank vector.
2. Why is every entry of \( \G \) positive, and which three conclusions does @thm-perron then give?
3. True or false: with \( \alpha = 1 \), every web has exactly one PageRank vector. Justify your answer.
4. True or false: the page with the most incoming links always has the highest PageRank. Justify your answer.
5. For \( \alpha = 0.85 \), what does @thm-google-matrix-eigenvalues say about the eigenvalues of \( \G \) other than \( 1 \)? Can the bound be improved for every web?
6. True or false: after \( 10 \) steps of \( \x_{k+1} = \G\x_k \) from any probability vector, \( \norm{\x_{10} - \vpi}_1 \le 2\alpha^{10} \). Justify your answer.
:::
::::

::: {.solution}
(a) For a web with link matrix \( \P \) (@def-link-matrix) and \( 0 < \alpha < 1 \), \( \G = \alpha\P + \frac{1-\alpha}{n}\J \). A PageRank vector is a probability vector \( \vpi \) with \( \G\vpi = \vpi \).

(b) \( \alpha\P \) has non-negative entries and \( \frac{1-\alpha}{n}\J \) has every entry equal to \( \frac{1-\alpha}{n} > 0 \), since \( \alpha < 1 \). Perron's theorem then gives: \( \rho(\G) \) is an eigenvalue of algebraic multiplicity one; it has an eigenvector with all entries positive; every other eigenvalue has modulus strictly less than \( \rho(\G) \). Here \( \rho(\G) = 1 \).

(c) False. With \( \alpha = 1 \), \( \G = \P \), and for two pairs of pages linking only to each other, @exm-link-matrix-failures (b) gives two different steady states.

(d) False. In @exm-pagerank-four-pages, page \( 3 \) has the most incoming links, but page \( 1 \) ranks first.

(e) Every eigenvalue \( \lambda \ne 1 \) has \( \lvert\lambda\rvert \le 0.85 \). The bound cannot be improved for every web: when the link matrix has \( -1 \) or a repeated \( 1 \) among its eigenvalues, \( \G \) has an eigenvalue of modulus exactly \( 0.85 \) (the Quick check, and Exercise C2).

(f) True, by @prp-pagerank-contraction with \( k = 10 \).
:::

### B. Practice

:::: {#exr-pagerank-b1}
[B1: A three-page web]

For the three-page web after @def-link-matrix (page \( 1 \) links to pages \( 2 \) and \( 3 \), page \( 2 \) to page \( 3 \), page \( 3 \) is dangling), with \( \alpha = \tfrac12 \), find the PageRank vector by solving the system of @thm-pagerank-vector (c). Hence rank the pages.
::::

::: {.solution}
With \( \P \) as in the text, \( (\I - \tfrac12\P)\vpi = \tfrac16\1 \). Multiplying by \( 12 \) gives \( (12\I - 6\P)\vpi = 2\,\1 \):
\[
\begin{aligned}
12\pi_1 - 2\pi_3 &= 2 , \\
-3\pi_1 + 12\pi_2 - 2\pi_3 &= 2 , \\
-3\pi_1 - 6\pi_2 + 10\pi_3 &= 2 .
\end{aligned}
\]
The first gives \( \pi_3 = 6\pi_1 - 1 \). The second becomes \( -3\pi_1 + 12\pi_2 - 12\pi_1 + 2 = 2 \), so \( \pi_2 = \tfrac54\pi_1 \). The third becomes \( -3\pi_1 - \tfrac{15}{2}\pi_1 + 60\pi_1 - 10 = 2 \), so \( \tfrac{99}{2}\pi_1 = 12 \) and \( \pi_1 = \tfrac{8}{33} \). Then \( \pi_2 = \tfrac{10}{33} \) and \( \pi_3 = \tfrac{48}{33} - 1 = \tfrac{15}{33} \). So
\[
\vpi = \frac{1}{33}(8,\ 10,\ 15) ,
\]
whose entries add up to \( 1 \). Check against the original system: \( 12 \cdot 8 - 2 \cdot 15 = 66 = 2 \cdot 33 \), \( -24 + 120 - 30 = 66 \), \( -24 - 60 + 150 = 66 \). Hence page \( 3 \) ranks first, then page \( 2 \), then page \( 1 \).
:::

:::: {#exr-pagerank-b2}
[B2: A cycle of three pages]

Three pages link in a cycle: \( 1 \) to \( 2 \), \( 2 \) to \( 3 \), \( 3 \) to \( 1 \). Let \( 0 < \alpha < 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Write down \( \P \) and show that \( p_{\P}(x) = x^3 - 1 \).
2. Use @thm-google-matrix-eigenvalues to find the eigenvalues of \( \G \), and check your answer against \( \tr\G \).
3. Find \( \vpi \), and explain why the bound of @thm-google-matrix-eigenvalues is attained.
:::
::::

::: {.solution}
(a) Column \( j \) of \( \P \) is \( \e_{j+1} \), with \( \e_4 \) read as \( \e_1 \):
\[
\begin{aligned}
\P &= \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} , \qquad
\det(x\I - \P) = \det\begin{pmatrix} x & 0 & -1 \\ -1 & x & 0 \\ 0 & -1 & x \end{pmatrix} \\
&= x \cdot x^2 + (-1)\cdot\bigl((-1)(-1) - x \cdot 0\bigr) = x^3 - 1 ,
\end{aligned}
\]
expanding along the first row.

(b) \( x^3 - 1 = (x - 1)(x - \omega)(x - \conj\omega) \) with \( \omega = -\tfrac12 + \tfrac{\sqrt3}{2}i \), so \( \mu_2 = \omega \), \( \mu_3 = \conj\omega \), and the eigenvalues of \( \G \) are \( 1, \alpha\omega, \alpha\conj\omega \). Their sum is \( 1 + \alpha(\omega + \conj\omega) = 1 - \alpha \). Directly, \( \tr\G = \alpha\tr\P + \frac{1-\alpha}{3}\tr\J = 0 + (1 - \alpha) \), which agrees (@thm-trace-det-eigenvalues).

(c) \( \P\1 = \1 \) and \( \J\1 = 3\,\1 \), so \( \G\1 = \alpha\1 + (1 - \alpha)\1 = \1 \), and \( \vpi = \tfrac13\1 \) by the uniqueness in @thm-pagerank-vector. The eigenvalues \( \alpha\omega \) and \( \alpha\conj\omega \) have modulus \( \alpha\lvert\omega\rvert = \alpha \), so the bound \( \lvert\lambda\rvert \le \alpha \) holds with equality.
:::

:::: {#exr-pagerank-b3}
[B3: Personalized jumps]

Let \( \P \in M_n(\nR) \) be stochastic, \( 0 < \alpha < 1 \), and let \( \v \) be a probability vector with **every** \( v_i > 0 \). Put \( \G_{\v} = \alpha\P + (1 - \alpha)\v\1\tp \): the surfer now jumps to page \( i \) with probability \( v_i \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \G_{\v} \) is stochastic and positive, and deduce that it has exactly one probability vector \( \vpi \) with \( \G_{\v}\vpi = \vpi \), and that \( \vpi > \0 \).
2. Prove that \( \vpi \) is the unique solution of \( (\I - \alpha\P)\vpi = (1 - \alpha)\v \).
3. For two pages linking to each other, \( \alpha = \tfrac12 \) and \( \v = (\tfrac34, \tfrac14) \), find \( \vpi \).
:::
::::

::: {.solution}
(a) The entries of \( \G_{\v} \) are \( \alpha p_{ij} + (1 - \alpha)v_i \ge (1 - \alpha)v_i > 0 \). Column \( j \) adds up to \( \alpha + (1 - \alpha)\1\tp\v = \alpha + 1 - \alpha = 1 \). So \( \G_{\v} \) is stochastic and positive. The proof of @thm-pagerank-vector (a) and (b) used only these two facts, so it applies word for word: \( \rho(\G_{\v}) = 1 \) is an eigenvalue of algebraic multiplicity one with a positive eigenvector, and its normalization \( \vpi \) is the only probability vector fixed by \( \G_{\v} \).

(b) For a probability vector \( \x \), \( \G_{\v}\x = \alpha\P\x + (1 - \alpha)\v(\1\tp\x) = \alpha\P\x + (1 - \alpha)\v \), so \( \G_{\v}\vpi = \vpi \) says \( (\I - \alpha\P)\vpi = (1 - \alpha)\v \). The matrix \( \I - \alpha\P \) is invertible, as in the proof of @thm-pagerank-vector (c), so the solution is unique.

(c) \( \P \) is the swap, and the system is \( \pi_1 - \tfrac12\pi_2 = \tfrac38 \), \( -\tfrac12\pi_1 + \pi_2 = \tfrac18 \). The first gives \( \pi_1 = \tfrac38 + \tfrac12\pi_2 \), and the second becomes \( -\tfrac3{16} + \tfrac34\pi_2 = \tfrac18 \), so \( \pi_2 = \tfrac{5}{12} \) and \( \pi_1 = \tfrac38 + \tfrac5{24} = \tfrac{7}{12} \). So \( \vpi = (\tfrac7{12}, \tfrac5{12}) \): the preferred page \( 1 \) gains, but less than its jump weight \( \tfrac34 \), because half the time the surfer follows the link to page \( 2 \).
:::

### C. Going deeper

:::: {#exr-pagerank-c1}
[C1: PageRank as a sum over paths]

Let \( \P \), \( \alpha \), \( \G \) and \( \vpi \) be as in @thm-pagerank-vector.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \displaystyle \vpi = \frac{1 - \alpha}{n}\sum_{k=0}^{\infty}\alpha^k\P^k\1 \).
2. Deduce that \( \pi_i \ge \frac{1-\alpha}{n} \) for every \( i \).
3. Suppose no page is dangling and no page links to page \( i \). Prove that \( \pi_i = \frac{1-\alpha}{n} \) exactly.
:::

*Hint for (a): @thm-neumann-series with the \( 1 \)-norm.*
::::

::: {.solution}
(a) By @thm-operator-norm-formulas (a), \( \norm{\alpha\P}_1 = \alpha\norm{\P}_1 = \alpha < 1 \), the largest column sum of \( \alpha\P \). By @thm-neumann-series (a), \( \I - \alpha\P \) is invertible and \( (\I - \alpha\P)^{-1} = \sum_{k \ge 0}\alpha^k\P^k \). By @thm-pagerank-vector (c), \( \vpi = \frac{1-\alpha}{n}(\I - \alpha\P)^{-1}\1 \), which is the stated series.

(b) Every term \( \alpha^k\P^k\1 \) has non-negative entries, and the term \( k = 0 \) is \( \1 \). So each entry of the sum is at least \( 1 \), since a limit of partial sums that are all at least \( 1 \) is at least \( 1 \), and \( \pi_i \ge \frac{1-\alpha}{n} \).

(c) From \( \G\vpi = \vpi \) and the proof of @thm-pagerank-vector (c), \( \vpi = \alpha\P\vpi + \frac{1-\alpha}{n}\1 \). Row \( i \) of \( \P \) is zero: \( p_{ij} \ne 0 \) only if page \( j \) links to page \( i \) or page \( j \) is dangling, and neither happens. So \( (\P\vpi)_i = 0 \) and \( \pi_i = \frac{1-\alpha}{n} \), the smallest possible value by (b).
:::

:::: {#exr-pagerank-c2}
[C2: When the bound is attained]

Let \( \P \in M_n(\nR) \) be stochastic, \( 0 < \alpha < 1 \), and \( \G = \alpha\P + \frac{1-\alpha}{n}\J \).

::: {.enumerate options="label=(\alph*)"}
1. Suppose \( \P \) has two **different** steady states \( \u \ne \w \). Prove that \( \G(\u - \w) = \alpha(\u - \w) \), so that \( \alpha \) is an eigenvalue of \( \G \).
2. For the web of @exm-link-matrix-failures (b), find all eigenvalues of \( \G \), with multiplicity, and check your answer against (a).
:::
::::

::: {.solution}
(a) Put \( \z = \u - \w \ne \0 \). Both are probability vectors, so \( \1\tp\z = 0 \) and \( \J\z = \1(\1\tp\z) = \0 \). Hence \( \G\z = \alpha\P\u - \alpha\P\w + \0 = \alpha(\u - \w) = \alpha\z \), and \( \alpha \) is an eigenvalue of \( \G \) with eigenvector \( \z \).

(b) \( \P \) is block diagonal with two blocks \( \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \), each with characteristic polynomial \( x^2 - 1 \), so \( p_{\P}(x) = (x^2 - 1)^2 = (x - 1)(x - 1)(x + 1)(x + 1) \) by @thm-det-block-triangular. By @thm-google-matrix-eigenvalues, with \( \mu_2 = 1 \) and \( \mu_3 = \mu_4 = -1 \), the eigenvalues of \( \G \) are \( 1, \alpha, -\alpha, -\alpha \). The eigenvalue \( \alpha \) is the one found in (a), with \( \u = (\tfrac12, \tfrac12, 0, 0) \), \( \w = (0, 0, \tfrac12, \tfrac12) \) and eigenvector \( \z = \tfrac12(1, 1, -1, -1) \); indeed \( \P\z = \z \) and \( \J\z = \0 \), so \( \G\z = \alpha\z \).
:::
