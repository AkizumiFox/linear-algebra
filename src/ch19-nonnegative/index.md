# Non-negative Matrices

Two chapters left debts that this one pays. Chapter 9 §11 found the long-run behavior of a Markov chain by diagonalizing its transition matrix, proved that the chain settles down under three hypotheses, that the transition matrix is diagonalizable, that \( 1 \) is a simple eigenvalue and that every other eigenvalue has modulus less than \( 1 \) (@thm-markov-limit-diagonalizable), and promised that "Chapter 19 proves the Perron–Frobenius theorem, which gives the conclusions of @thm-markov-limit-diagonalizable for every stochastic matrix with some power having all entries positive, without assuming diagonalizability and without computing eigenvalues." Chapter 18 §08 stated Birkhoff's theorem, that the extreme points of the doubly stochastic matrices are exactly the permutation matrices, proved its two forms equivalent, and left the theorem itself to this chapter.

Both debts are about matrices whose entries are all \( \ge 0 \), and the theory of such matrices is unlike anything earlier in the book. It depends on the **standard basis**: the hypothesis \( \A \ge 0 \) is destroyed by almost every change of basis, so the similarity invariants that organized Chapters 9 and 10 are joined by a new kind of information, the pattern of zero entries. What that pattern buys is striking. A matrix with every entry positive has a positive eigenvalue that is simple, strictly larger in modulus than every other eigenvalue, and equal to the spectral radius, with an eigenvector whose entries are all positive; this is Perron's theorem. When some entries are zero, most of this survives when the zeros do not split the indices into a part that the rest cannot reach, a condition read off a directed graph. From those two facts follow the convergence of Markov chains, the ranking of web pages, Birkhoff's theorem, and the theory of the matrices \( s\I - \B \) with \( \B \ge 0 \) that arise in economics and in the discretization of differential equations.

**The field is \( \nR \).** Matrices and vectors have real entries, and a real matrix is read in \( M_n(\nC) \) whenever its eigenvalues are wanted, as in Chapter 16 §04, so that its spectral radius \( \rho(\A) \) is defined (@def-spectral-radius). Two conventions hold throughout and are never switched.

- **Stochastic means column-stochastic.** As in @def-stochastic-matrix, a stochastic matrix has non-negative entries and every **column** adding up to \( 1 \), and a Markov chain is \( \x_{k+1} = \A\x_k \). Many books use rows and multiply on the left; their stochastic matrices are the transposes of ours.
- **The order is entrywise.** \( \A \ge 0 \) means every entry of \( \A \) is \( \ge 0 \), and \( \A > 0 \) means every entry is \( > 0 \), as for vectors in Chapter 18 §05; §01 defines the matrix version (@def-entrywise-order). This is **not** the Loewner order of Chapter 13, which the book always writes \( \A \succeq 0 \). A positive matrix need not be positive definite, and a positive definite matrix need not be positive: §01 gives a \( 2 \times 2 \) example of each.
- **The absolute value is entrywise.** In this chapter \( \lvert\M\rvert \) is the matrix of the moduli \( \lvert m_{ij}\rvert \) of the entries of \( \M \) (@def-entrywise-order (c)), **not** the absolute value \( (\A^{*}\A)^{1/2} \) of Chapter 13.

## The analysis this chapter imports

The list is Chapter 16's, facts (A1)–(A6) of that chapter's introduction, cited by the same name at the point of use. Three of them carry the weight, together with the algebra of limits from the same introduction. In §01, **(A3)**, compactness of closed bounded sets, and **(A4)**, the extreme value theorem, produce the eigenvalue and positive eigenvector of Perron's theorem as a maximum that is attained rather than merely approached. The passage from positive to general non-negative matrices in §03 is a limit, and it uses **(A2)**, monotone convergence, together with (A3) again. Nothing else analytic is used, and a section that needs anything more says so where it uses it.

## What you need

- **Chapter 0 §06** — the modulus of a complex number and the triangle inequality: @thm-conjugate-properties, @thm-complex-triangle-inequality.
- **Chapter 1 §§06 and 07** — two counting facts, both in §07's proof of Birkhoff's theorem: the size bound on an independent list, and the dimension formula for a sum of subspaces: @thm-size-bounds, @thm-dimension-formula-subspace-dim.
- **Chapter 3 §04** — permutation matrices, which relabel coordinates: @def-permutation-matrix, @lem-permutation-matrices.
- **Chapter 2 §03** — Rank–Nullity, used once, in §06, to give the kernel of \( \x \mapsto \1\tp\x \) its dimension: @thm-rank-nullity.
- **Chapter 6 §05** — that a polynomial over \( \nC \) splits, which is how §§01 and 03 count the eigenvalues of a non-negative matrix: @cor-complex-polynomial-splits.
- **Chapters 7 and 8** — the characteristic polynomial and block triangular matrices: @thm-charpoly-similarity-invariant, @thm-det-block-triangular, @thm-block-multiplication.
- **Chapter 9** — eigenvalues and their multiplicities, invariant subspaces, left eigenvectors, the spectral mapping theorem, and the Markov chains this chapter returns to: @def-algebraic-multiplicity, @thm-invariant-subspace-matrix, @def-left-eigenvector, @prp-left-eigenvectors-transpose, @thm-left-right-biorthogonal, @thm-spectral-mapping, @def-stochastic-matrix, @def-markov-chain, @thm-markov-limit-diagonalizable.
- **Chapter 10** — generalized eigenspaces, and the convergence of matrix powers and of the Neumann series: @thm-generalized-eigenspace-decomposition, @thm-matrix-powers-converge, @cor-markov-powers-converge, @thm-neumann-series-spectral.
- **Chapter 13** — positive semidefinite and positive definite matrices, which the entrywise order must not be confused with: @def-positive-semidefinite.
- **Chapter 16** — entrywise convergence as the convergence of matrices (§02), the operator norms and their formulas (§03), and the spectral radius, Gelfand's formula and the Neumann series: @cor-entrywise-convergence-is-the-convergence, @thm-operator-norm-formulas, @thm-operator-norm-properties, @def-spectral-radius, @thm-gelfand, @cor-spectral-radius-row-column-bound, @thm-neumann-series.
- **Chapter 17 §08** — majorization, Schur's theorem, which Birkhoff's theorem reproves, and the Schur–Horn theorem: @def-majorization, @thm-schur-majorization, @thm-schur-horn.
- **Chapter 18** — the simplex, closed sets, Carathéodory's theorem, the doubly stochastic matrices, their permutation-matrix extreme points and the vertices of polyhedra: @def-standard-simplex, @def-closed-set, @thm-caratheodory, @def-doubly-stochastic, @prp-permutation-matrices-extreme, @thm-minkowski-extreme, @thm-vertices-basic-feasible.

## Roadmap

- **Positive matrices and Perron's theorem.** The entrywise order, the monotonicity of the spectral radius, and Perron's theorem for matrices with every entry positive, proved by maximizing over the simplex.
- **Irreducibility and graphs.** The directed graph of a matrix, strong connectivity, irreducible matrices and the test \( (\I + \A)^{n-1} > 0 \), and the block triangular normal form of a reducible matrix.
- **The Perron–Frobenius theorem.** Every non-negative matrix has its spectral radius as an eigenvalue with a non-negative eigenvector, and for an irreducible matrix that eigenvalue is simple with a positive eigenvector. The examples that show irreducibility cannot be dropped.
- **The Collatz–Wielandt formula.** The spectral radius of an irreducible matrix as a max–min and a min–max over test vectors, and the row-sum bounds that follow.
- **Primitive matrices.** Irreducible matrices with a positive power, the eigenvalues on the circle of radius \( \rho \), and the convergence of \( (\A/\rho)^{k} \) without any diagonalizability.
- **Markov chains.** Chapter 9's promise, paid in its own words; chains that are irreducible but not primitive, reducible chains, and absorbing chains.
- **Birkhoff's theorem.** Every extreme point of the doubly stochastic matrices is a permutation matrix, and a second proof of Schur's theorem.
- **PageRank.** The Google matrix is positive, so Perron's theorem ranks the pages, and the damping factor bounds the rate of convergence.
- **M-matrices.** The matrices \( s\I - \B \) with \( \B \ge 0 \), their many equivalent characterizations, and two applications. The chapter's summary closes this section.

## Named moves

- **Push up a slack.** If \( \A\u \ge r\u \) with \( r \) maximal, the slack \( \A\u - r\u \) must vanish: one more application of a positive matrix would make it strictly positive and leave room to increase \( r \). Perron's proof makes this move once, in its push-up claim, and then uses the claim three times.
- **Pair a slack with a positive left eigenvector.** A non-negative vector whose product with a positive vector is zero is itself zero. This is how a positive left eigenvector rules out a second Jordan block, and a non-negative eigenvector for a smaller eigenvalue.
- **Read the powers as walks.** The non-zero entries of \( \A^{k} \) record the walks of length \( k \) in a graph, so questions about positivity of powers become questions about reachability, answered by following arrows.
- **Relabel and rescale, nothing more.** The only changes of basis that respect the entrywise order are the relabelings of the coordinates, possibly combined with positive rescalings, and every normal form in the chapter uses only these.
- **Perturb to positive, then take the limit.** To prove something for a non-negative matrix, prove it for \( \A + \varepsilon\J \), which is positive, and let \( \varepsilon \to 0 \); what survives the limit is exactly the non-strict part of the conclusion.
