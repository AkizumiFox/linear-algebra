# Irreducibility and Graphs

Perron's theorem (@thm-perron) asks for every entry to be positive, and most matrices that arise in practice do not oblige. The bicycle chain of Chapter 9 §11 has a zero entry, since a bicycle at station \( 3 \) never reaches station \( 1 \) in one night; the Leslie matrix of the same section is mostly zeros; the swap has only two non-zero entries. Some zeros are harmless and some are fatal: the swap keeps \( \rho = 1 \) as a simple eigenvalue with a positive eigenvector, while for \( \I_2 \) the eigenvalue \( 1 \) is double and its positive eigenvectors are no longer all multiples of one. This section finds the dividing line. It depends only on **where** the zero entries are, and the right way to read that pattern is as a map of one-step moves between the indices: a directed graph. The matrices on the good side of the line are the **irreducible** ones, and §03 proves that they enjoy nearly all of Perron's conclusions.

**Throughout, \( F \) is \( \nR \) or \( \nC \).** The definitions of this section use only whether an entry is zero, so they make sense for any matrix. The statements about powers and positivity need \( \A \ge 0 \), and say so.

## The graph of a matrix

The question that recurs is this: which entries of \( \A^{k} \) are non-zero? For a non-negative matrix, \( (\A^2)_{ij} = \sum_l a_{il}a_{lj} \) is positive exactly when some \( a_{il} \) and \( a_{lj} \) are both positive, that is, when one can go from \( j \) to some \( l \) and from \( l \) to \( i \) along non-zero entries. In a Markov chain (@def-markov-chain), \( a_{lj} \) is the probability of moving from state \( j \) to state \( l \) in one step, and the sentence says that state \( i \) can be reached from \( j \) in two steps. So we draw an arrow from \( j \) to \( i \) for each non-zero entry \( a_{ij} \) and count routes.

*The graph of a matrix has a vertex for each index and an arrow from \( j \) to \( i \) whenever the entry \( a_{ij} \) is not zero.*

::: {#def-directed-graph-of-matrix}
[Directed Graph of a Matrix; Walks and Paths]

Let \( n \ge 1 \) and \( \A = (a_{ij}) \in M_n(F) \).

::: {.enumerate options="label=(\alph*)"}
1. The **directed graph** \( G(\A) \) of \( \A \) has **vertices** \( 1, 2, \dots, n \), and an **edge from \( j \) to \( i \)**, written \( j \to i \), for **each** pair \( (i, j) \) with \( a_{ij} \ne 0 \). An edge \( j \to j \), from a non-zero diagonal entry, is a **loop**.
2. A **walk of length \( k \ge 0 \) from \( j \) to \( i \)** is a list of vertices \( j = i_0, i_1, \dots, i_k = i \) such that \( i_{t-1} \to i_t \) is an edge for **every** \( t = 1, \dots, k \).
3. A **path** is a walk whose vertices \( i_0, \dots, i_k \) are distinct.
:::
:::

In words: (a) turns each non-zero entry into an arrow, and the arrow for \( a_{ij} \) points **from the column index to the row index**. That is the direction in which \( \A \) moves things: in \( \x \mapsto \A\x \), entry \( j \) of \( \x \) contributes \( a_{ij}x_j \) to entry \( i \) of the image, and in a column-stochastic chain \( a_{ij} \) is the probability of the move from \( j \) to \( i \). Clause (b) allows \( k = 0 \): the one-vertex list \( (j) \) is a walk of length \( 0 \) from \( j \) to itself, whatever the matrix. A walk may revisit vertices and use an edge several times; a path may not.

::: {.remark}
Many books draw the arrow for \( a_{ij} \ne 0 \) from \( i \) to \( j \). The two graphs differ by reversing every edge, and nothing below depends on the choice except the wording "from \( j \) to \( i \)". We take the direction that matches \( \x_{k+1} = \A\x_k \) and the column-stochastic convention of Chapter 9 §11.
:::

Examples, simplest first.

- **\( n = 1 \).** \( G((a)) \) has one vertex, with a loop if \( a \ne 0 \) and no edge if \( a = 0 \). In either case there is the walk of length \( 0 \) from \( 1 \) to \( 1 \).
- **The zero matrix** \( 0 \in M_n(F) \) has \( n \) vertices and no edges at all. **A positive matrix** has every possible edge, loops included.
- **A cycle.** The permutation matrix \( \C = \begin{psmallmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{psmallmatrix} \) has \( c_{21} = c_{32} = c_{13} = 1 \), so its edges are \( 1 \to 2 \), \( 2 \to 3 \) and \( 3 \to 1 \).
- **A path.** \( \begin{psmallmatrix} 0 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{psmallmatrix} \) has the edges \( 1 \to 2 \) and \( 2 \to 3 \) only. There is a walk from \( 1 \) to \( 3 \), and none from \( 3 \) to anywhere but \( 3 \) itself.
- \( \A = \begin{psmallmatrix} 0 & 2 & 0 \\ 0 & 0 & 1 \\ 3 & 0 & 1 \end{psmallmatrix} \) has the edges \( 2 \to 1 \), \( 3 \to 2 \), \( 1 \to 3 \) and the loop \( 3 \to 3 \), drawn below. The values of the entries play no part in the graph.

\begin{center}
\begin{tikzpicture}[scale=1.5, vert/.style={circle, draw, thick, minimum size=7mm, inner sep=0pt}, arr/.style={-{Stealth[length=2.4mm]}, thick}]
  \node[vert] (v1) at (90:1) {$1$};
  \node[vert] (v2) at (210:1) {$2$};
  \node[vert] (v3) at (330:1) {$3$};
  \draw[arr] (v1) -- node[right=2pt, font=\small] {$a_{31}$} (v3);
  \draw[arr] (v3) -- node[below=2pt, font=\small] {$a_{23}$} (v2);
  \draw[arr] (v2) -- node[left=2pt, font=\small] {$a_{12}$} (v1);
  \draw[arr] (v3) to[out=-20, in=40, looseness=7] node[right=2pt, font=\small] {$a_{33}$} (v3);
\end{tikzpicture}
\end{center}

**Non-example by minimal change.** The graph records whether an entry is zero, not how large it is. Change the entry \( 3 \) of the last matrix to \( 10^{-9} \): the graph is unchanged. Change it to \( 0 \): the edge \( 1 \to 3 \) disappears, and with it every walk out of vertex \( 1 \) other than the one of length \( 0 \).

The graph was built to count routes, and it does, for non-negative matrices. The same lemma handles \( \I + \A \), whose graph is that of \( \A \) with a loop added at every vertex; a loop lets a walk wait, so walks of length **at most** \( k \) become walks of length exactly \( k \).

::: {#lem-powers-and-walks}
[Powers Count Walks]

Let \( \A \in M_n(\nR) \) be non-negative, and let \( k \ge 0 \) and \( i, j \in \{1, \dots, n\} \).

::: {.enumerate options="label=(\alph*)"}
1. \( (\A^{k})_{ij} > 0 \) if and only if \( G(\A) \) has a walk of length \( k \) from \( j \) to \( i \).
2. \( \bigl((\I + \A)^{k}\bigr)_{ij} > 0 \) if and only if \( G(\A) \) has a walk of length **at most** \( k \) from \( j \) to \( i \).
:::
:::

::: {.idea}
Induction on \( k \), peeling off the first step of a walk. Expanding \( (\A^{k+1})_{ij} = \sum_l (\A^{k})_{il}a_{lj} \) gives a sum of non-negative terms, so it is positive exactly when one term is: a first step \( j \to l \) followed by a walk of length \( k \) from \( l \) to \( i \). For \( \I + \A \) the diagonal \( 1 \) adds the option of waiting at \( j \) instead of stepping.
:::

::: {.proof}
(a) Induction on \( k \). For \( k = 0 \), \( (\I)_{ij} > 0 \) exactly when \( i = j \), which is exactly when there is a walk of length \( 0 \) from \( j \) to \( i \). Suppose (a) holds for \( k \). By @lem-entrywise-order-rules (c), \( \A^{k} \ge 0 \), so
\[
(\A^{k+1})_{ij} = \sum_{l=1}^{n}(\A^{k})_{il}\,a_{lj}
\]
is a sum of non-negative terms. It is positive if and only if some term is, that is, if and only if there is an \( l \) with \( a_{lj} > 0 \) and \( (\A^{k})_{il} > 0 \). By the definition of \( G(\A) \) and the induction hypothesis, this says: there is an edge \( j \to l \) and a walk of length \( k \) from \( l \) to \( i \). Putting \( j \) in front of that walk gives a walk of length \( k + 1 \) from \( j \) to \( i \), and every such walk arises this way, with \( l \) its second vertex.

(b) Induction on \( k \), with the same base case, since \( (\I + \A)^0 = \I \). Suppose (b) holds for \( k \). As \( (\I + \A)^{k} \ge 0 \) and \( \I + \A \ge 0 \),
\[
\bigl((\I + \A)^{k+1}\bigr)_{ij} = \sum_{l=1}^{n}\bigl((\I + \A)^{k}\bigr)_{il}\,(\delta_{lj} + a_{lj})
\]
is positive if and only if there is an \( l \) with \( ((\I + \A)^{k})_{il} > 0 \) and either \( l = j \) or \( a_{lj} > 0 \). By the induction hypothesis this says: there is a walk of length at most \( k \) from \( l \) to \( i \), where either \( l = j \) or \( j \to l \) is an edge. In the first case we have a walk of length at most \( k \) from \( j \) to \( i \); in the second, putting \( j \) in front gives one of length at most \( k + 1 \). Conversely, let a walk of length \( m \le k + 1 \) from \( j \) to \( i \) be given. If \( m \le k \), take \( l = j \). If \( m = k + 1 \ge 1 \), take \( l \) to be its second vertex, so that \( j \to l \) is an edge and the rest of the walk has length \( k \). This proves the lemma.
:::

For the matrix drawn above, \( \A^2 = \begin{psmallmatrix} 0 & 0 & 2 \\ 3 & 0 & 1 \\ 3 & 6 & 1 \end{psmallmatrix} \). Its \( (1, 1) \) entry is \( 0 \), and indeed the shortest walk from \( 1 \) back to \( 1 \) is \( 1 \to 3 \to 2 \to 1 \), of length \( 3 \). Its \( (1, 3) \) entry is \( 2 \), from the walk \( 3 \to 2 \to 1 \).

A long walk can always be shortened to a path, and a path is short.

::: {#lem-walk-contains-path}
[Shortening a Walk to a Path]

Let \( \A \in M_n(F) \). If \( G(\A) \) has a walk from \( j \) to \( i \), then it has a path from \( j \) to \( i \), and every path has length at most \( n - 1 \).
:::

::: {.idea}
Take a shortest walk. If it visited some vertex twice, the loop between the two visits could be cut out, leaving a shorter walk; so a shortest walk is a path. A path visits distinct vertices, and there are only \( n \) of them.
:::

::: {.proof}
Among the walks from \( j \) to \( i \), choose one of least length \( k \) (@thm-well-ordering), say \( j = i_0, i_1, \dots, i_k = i \). Suppose two of its vertices coincide, \( i_s = i_t \) with \( s < t \). Deleting \( i_{s+1}, \dots, i_t \) leaves the list \( i_0, \dots, i_s, i_{t+1}, \dots, i_k \), which is still a walk, because the edge \( i_t \to i_{t+1} \) (if \( t < k \)) is the edge \( i_s \to i_{t+1} \). It has length \( k - (t - s) < k \), contradicting the choice of \( k \). So the vertices are distinct, and the walk is a path. A path of length \( k \) has \( k + 1 \) distinct vertices among the \( n \) vertices of \( G(\A) \), so \( k + 1 \le n \).
:::

## Strong connectivity

Positivity of \( \A \) says every vertex has an edge to every vertex. The useful weakening is to ask only for a **walk**.

*A graph is strongly connected when every vertex can be reached from every vertex.*

::: {#def-strongly-connected}
[Strongly Connected]

Let \( \A \in M_n(F) \). The graph \( G(\A) \) is **strongly connected** if, for **every** ordered pair \( (j, i) \) of vertices, there is a walk from \( j \) to \( i \).
:::

In words: whichever vertex we start from, every vertex can be reached, and the pair is **ordered**, so a walk from \( j \) to \( i \) and a walk from \( i \) back to \( j \) are both required. By @lem-walk-contains-path, the walks may be taken to be paths of length at most \( n - 1 \). For \( n = 1 \) the walk of length \( 0 \) suffices, so the graph of every \( 1 \times 1 \) matrix, \( (0) \) included, is strongly connected.

The cycle \( \C \) above is strongly connected: from any vertex, follow the arrows round. So is the graph drawn above, since it contains the cycle \( 1 \to 3 \to 2 \to 1 \), and so is the graph of every positive matrix. The path is not: there is no walk from \( 3 \) to \( 1 \). Removing one edge from the cycle, by changing \( c_{13} = 1 \) to \( 0 \), gives exactly the path, so the clause that fails is the one for the pair \( (3, 1) \); the walks from \( 1 \) to \( 2 \), from \( 1 \) to \( 3 \) and from \( 2 \) to \( 3 \) survive.

## Irreducible matrices

Now the notion this chapter is built on. We want to single out the matrices whose eigenvalue problem cannot be split into two smaller ones. For a matrix with a zero block in the lower left, it can:
\[
\A = \begin{pmatrix} \B & \C \\ 0 & \D \end{pmatrix} \quad\Longrightarrow\quad p_{\A} = p_{\B}\,p_{\D} ,
\]
by @thm-det-block-triangular applied to \( x\I - \A \), and the subspace spanned by the first few standard basis vectors is mapped into itself. For such a matrix Perron's conclusions fail in general: \( \I_2 \) and \( \diag(2, 1) \) are of this shape. In this chapter a change of basis must preserve non-negativity, and the ones that do so while keeping the entries themselves are the relabelings of the coordinates. So the definition asks whether a relabeling produces the zero block.

*A matrix is irreducible if no relabeling of the coordinates puts it in block upper triangular form.*

::: {#def-irreducible}
[Irreducible Matrix]

Let \( \A \in M_n(F) \).

::: {.enumerate options="label=(\alph*)"}
1. For \( n \ge 2 \), \( \A \) is **reducible** if there are a permutation matrix \( \P \) and an integer \( k \) with \( 1 \le k \le n - 1 \) such that
   \[
   \P\tp\A\P = \begin{pmatrix} \B & \C \\ 0 & \D \end{pmatrix}, \qquad \B \in M_k(F),\ \D \in M_{n-k}(F) ,
   \]
   with \( 0 \) the \( (n - k) \times k \) zero matrix. It is **irreducible** if it is **not** reducible.
2. For \( n = 1 \), **every** matrix \( (a) \in M_1(F) \) is irreducible, including \( (0) \).
:::
:::

In words: by @lem-permutation-matrices (b), \( \P\tp = \P^{-1} \), so \( \P\tp\A\P \) is similar to \( \A \). It is the matrix of \( T_{\A} \) in the standard basis taken in another order, and in (a) we ask whether some order has a zero block below the diagonal with **both** diagonal blocks non-empty, which is what \( 1 \le k \le n - 1 \) says. Irreducible means that **no** order does. Clause (b) is a convention, justified below.

To see what relabeling does to the entries, we compute it once.

::: {#lem-permutation-similarity-entries}
[Relabeling the Coordinates]

Let \( \sigma \in S_n \) and \( \A \in M_n(F) \). Then \( (\P_\sigma\tp\A\P_\sigma)_{st} = a_{\sigma(s)\sigma(t)} \) for all \( s, t \). Consequently \( t \to s \) is an edge of \( G(\P_\sigma\tp\A\P_\sigma) \) if and only if \( \sigma(t) \to \sigma(s) \) is an edge of \( G(\A) \).
:::

::: {.proof}
By @def-permutation-matrix, \( \P_\sigma\e_t = \e_{\sigma(t)} \). The \( (s, t) \) entry of a matrix \( \M \) is \( \e_s\tp\M\e_t \), so by @thm-transpose-properties,
\[
(\P_\sigma\tp\A\P_\sigma)_{st} = \e_s\tp\P_\sigma\tp\A\P_\sigma\e_t = (\P_\sigma\e_s)\tp\A(\P_\sigma\e_t) = \e_{\sigma(s)}\tp\A\,\e_{\sigma(t)} = a_{\sigma(s)\sigma(t)} .
\]
The statement about edges is the statement that one of these entries is non-zero exactly when the other is.
:::

So the graph of \( \P_\sigma\tp\A\P_\sigma \) is \( G(\A) \) with the vertex \( \sigma(s) \) renamed \( s \). In particular, @def-strongly-connected holds for one exactly when it holds for the other. The zero block of @def-irreducible becomes a statement about a set of vertices that no edge leaves.

::: {#lem-reducible-closed-set}
[Reducible Means a Set of Vertices With No Exit]

Let \( n \ge 2 \) and \( \A \in M_n(F) \). Then \( \A \) is reducible if and only if there is a set \( S \subseteq \{1, \dots, n\} \) with \( S \ne \emptyset \) and \( S \ne \{1, \dots, n\} \) such that
\[
a_{ij} = 0 \qquad\text{whenever } j \in S \text{ and } i \notin S ,
\]
that is, such that no edge of \( G(\A) \) goes from a vertex in \( S \) to a vertex outside \( S \).
:::

::: {.idea}
The zero block of @def-irreducible sits in the columns of the first \( k \) relabeled vertices and the rows of the others. So take \( S \) to be the first \( k \) vertices in the new order; conversely, given \( S \), choose the order that lists \( S \) first. @lem-permutation-similarity-entries translates between the entries and the vertices.
:::

::: {.proof}
\( (\Leftarrow) \) Let \( k \) be the number of elements of \( S \), so \( 1 \le k \le n - 1 \), and choose \( \sigma \in S_n \) listing the elements of \( S \) first: \( \sigma(1), \dots, \sigma(k) \) are the elements of \( S \) and \( \sigma(k+1), \dots, \sigma(n) \) the others. For \( t \le k < s \) we have \( \sigma(t) \in S \) and \( \sigma(s) \notin S \), so by @lem-permutation-similarity-entries, \( (\P_\sigma\tp\A\P_\sigma)_{st} = a_{\sigma(s)\sigma(t)} = 0 \). That is, the lower-left \( (n - k) \times k \) block of \( \P_\sigma\tp\A\P_\sigma \) is zero, and \( \A \) is reducible.

\( (\Rightarrow) \) Let \( \P \) and \( k \) be as in @def-irreducible (a). By @def-permutation-matrix, \( \P = \P_\sigma \) for some \( \sigma \in S_n \). Put \( S = \{\sigma(1), \dots, \sigma(k)\} \), which has \( k \) elements, so it is neither empty nor everything. If \( j \in S \) and \( i \notin S \), then \( j = \sigma(t) \) with \( t \le k \) and \( i = \sigma(s) \) with \( s > k \), and \( a_{ij} = (\P_\sigma\tp\A\P_\sigma)_{st} = 0 \) because \( (s, t) \) lies in the zero block.
:::

The condition says that the coordinate subspace \( \Span\{\e_j : j \in S\} \) is mapped into itself by \( \A \), since column \( j \) of \( \A \) is \( \A\e_j \) and its entries outside \( S \) vanish. So a reducible matrix is one with an invariant subspace spanned by some of the standard basis vectors, other than \( \{\0\} \) and \( F^n \), and @thm-invariant-subspace-matrix is the source of the block form.

Now some examples, simplest first.

- **\( n = 1 \).** Irreducible by (b).
- **Positive matrices** are irreducible: no entry is \( 0 \), so no set \( S \) as in @lem-reducible-closed-set exists.
- **The swap** \( \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) is irreducible. For \( n = 2 \), the candidates are \( S = \{1\} \), which needs \( a_{21} = 0 \), and \( S = \{2\} \), which needs \( a_{12} = 0 \); both entries are \( 1 \). So a matrix may have zeros, even mostly zeros, and be irreducible.
- **Triangular matrices** with \( n \ge 2 \) are reducible. An upper triangular one already has the block form with \( \P = \I \) and \( k = 1 \). A lower triangular one, such as the path matrix, is reducible too, by @lem-reducible-closed-set with \( S = \{n\} \): column \( n \) has its only possible non-zero entry on the diagonal. Reversing the order of the coordinates, \( \sigma(s) = n + 1 - s \), turns the path matrix into \( \J_3(0) \), which is upper triangular.
- **The zero matrix** of size \( n \ge 2 \) is reducible, and so is \( \I_n \): any \( S \) will do.

**Non-example by minimal change.** The cycle \( \C \) is irreducible, as the next theorem will show. Change its entry \( c_{13} \) from \( 1 \) to \( 0 \): the result is the path matrix, and \( S = \{3\} \) now has no exit, because the only non-zero entry of column \( 3 \) outside row \( 3 \), the entry \( c_{13} \), has become \( 0 \). That single clause of @lem-reducible-closed-set is what changed.

::: {#exm-hidden-reducible}
[A reducible matrix that does not look it]

Decide whether \( \A = \begin{pmatrix} 1 & 0 & 2 \\ 3 & 4 & 5 \\ 6 & 0 & 7 \end{pmatrix} \) is irreducible, and if not, put it in block triangular form.
:::

::: {.solution}
Column \( 2 \) has its only non-zero entry in row \( 2 \), so \( S = \{2\} \) has no exit: \( a_{12} = a_{32} = 0 \). By @lem-reducible-closed-set, \( \A \) is reducible. Following the proof, list \( 2 \) first: \( \sigma(1) = 2 \), \( \sigma(2) = 1 \), \( \sigma(3) = 3 \). By @lem-permutation-similarity-entries, the \( (s, t) \) entry of \( \P_\sigma\tp\A\P_\sigma \) is \( a_{\sigma(s)\sigma(t)} \), so
\[
\P_\sigma\tp\A\P_\sigma = \begin{pmatrix} a_{22} & a_{21} & a_{23} \\ a_{12} & a_{11} & a_{13} \\ a_{32} & a_{31} & a_{33} \end{pmatrix} = \begin{pmatrix} 4 & 3 & 5 \\ 0 & 1 & 2 \\ 0 & 6 & 7 \end{pmatrix} .
\]
Hence \( p_{\A}(x) = (x - 4)(x^2 - 8x - 5) \), and the eigenvalues are \( 4 \) and \( 4 \pm \sqrt{21} \). In the graph, vertex \( 2 \) has only a loop leaving it: a chain that reaches state \( 2 \) stays there.
:::

**Why this definition, and why every \( 1 \times 1 \) matrix is irreducible.** The block form is the matrix picture of an invariant coordinate subspace, and it is exactly what splits \( p_{\A} \) into two factors and lets the conclusions of Perron's theorem fail, as \( \I_2 \) shows. For \( n = 1 \) there is no room for two non-empty blocks, and a convention is needed. Some books call \( (0) \) reducible. We call every \( 1 \times 1 \) matrix irreducible because that is the choice that makes the two theorems below true with no exception: the graph of a \( 1 \times 1 \) matrix is always strongly connected, through the walk of length \( 0 \), and \( (\I + \A)^{1 - 1} = \I = (1) \) is always positive. The price is paid in §03: the irreducible matrix \( (0) \) has spectral radius \( 0 \), so the statement there that an irreducible non-negative matrix has \( \rho(\A) > 0 \) carries the hypothesis \( n \ge 2 \).

::: {.warning}
**Irreducibility depends only on which entries are zero, never on their size.** For every \( t \ne 0 \), however small, \( \A_t = \begin{pmatrix} 1 & t \\ 1 & 1 \end{pmatrix} \) is irreducible, and for \( t > 0 \) its eigenvalues \( 1 \pm \sqrt t \) are distinct, with the positive eigenvector \( (\sqrt t, 1) \) for \( 1 + \sqrt t \). At \( t = 0 \) it is lower triangular, hence reducible, and \( 1 \) becomes a double eigenvalue with the eigenvector \( \e_2 \) only. An entry of \( 10^{-9} \) and an entry of \( 10^{9} \) count the same; an entry of \( 0 \) is different in kind. The property is not preserved by powers either: the swap is irreducible and its square is \( \I_2 \), which is not.
:::

The first theorem says that irreducibility, defined through relabelings, is exactly strong connectivity of the graph.

::: {#thm-irreducible-iff-strongly-connected}
[Irreducible If and Only If Strongly Connected]

Let \( n \ge 1 \) and \( \A \in M_n(F) \). Then \( \A \) is irreducible if and only if \( G(\A) \) is strongly connected.
:::

::: {.idea}
Both sides are about a set of vertices with no exit. If some vertex \( i \) cannot be reached from \( j \), the set of vertices that **can** be reached from \( j \) contains \( j \), misses \( i \), and has no exit, since an exit would reach one more vertex. Conversely, a set with no exit traps every walk that starts inside it.
:::

::: {.proof}
If \( n = 1 \), both sides hold, by @def-irreducible (b) and the walk of length \( 0 \). Let \( n \ge 2 \). By @lem-reducible-closed-set it suffices to show: \( G(\A) \) fails to be strongly connected if and only if there is a set \( S \), neither empty nor all of \( \{1, \dots, n\} \), from which no edge leaves.

\( (\Rightarrow) \) Suppose there are \( j \) and \( i \) with no walk from \( j \) to \( i \). Let \( S \) be the set of vertices \( l \) such that there is a walk from \( j \) to \( l \). Then \( j \in S \), by the walk of length \( 0 \), and \( i \notin S \). If \( l \in S \) and \( l \to m \) is an edge, then appending \( m \) to a walk from \( j \) to \( l \) gives a walk from \( j \) to \( m \), so \( m \in S \). Hence no edge leaves \( S \).

\( (\Leftarrow) \) Suppose no edge leaves \( S \), and choose \( j \in S \) and \( i \notin S \). Let \( j = i_0, i_1, \dots, i_k \) be any walk from \( j \). Then every \( i_t \) lies in \( S \), by induction on \( t \): \( i_0 = j \in S \), and if \( i_{t-1} \in S \), the edge \( i_{t-1} \to i_t \) does not leave \( S \), so \( i_t \in S \). Hence no walk from \( j \) ends at \( i \), and \( G(\A) \) is not strongly connected. This proves the theorem.
:::

So the cycle \( \C \) is irreducible, and so is the matrix drawn earlier: their graphs are strongly connected. Deciding irreducibility from the definition means looking at \( n! \) relabelings; deciding it from the graph means following arrows.

::: {.check}
Is \( \M = \begin{psmallmatrix} 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{psmallmatrix} \) irreducible? Every row and every column of \( \M \) contains a non-zero entry off the diagonal.
:::

::: {.solution}
No. The edges of \( G(\M) \) are \( 1 \to 2 \), \( 2 \to 1 \), \( 3 \to 4 \) and \( 4 \to 3 \), so there is no walk from \( 1 \) to \( 3 \), and \( \M \) is reducible by @thm-irreducible-iff-strongly-connected. Directly, \( S = \{1, 2\} \) has no exit, and indeed \( \M = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \oplus \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) is already block diagonal, with \( \P = \I \) and \( k = 2 \). Having an off-diagonal entry in every row and column is necessary for irreducibility when \( n \ge 2 \) (Exercise C1), but it is not sufficient.
:::

## A test by one matrix power

For a non-negative matrix, @lem-powers-and-walks turns strong connectivity into positivity of a single matrix, and that is the bridge back to Perron's theorem.

::: {#thm-irreducible-power-positive}
[Irreducibility Through a Power of \( \I + \A \)]

Let \( n \ge 1 \) and let \( \A \in M_n(\nR) \) be non-negative. Then \( \A \) is irreducible if and only if
\[
(\I + \A)^{n-1} > 0 .
\]
:::

::: {.idea}
Read both sides as statements about walks. Positivity of \( (\I + \A)^{n-1} \) asks for a walk of length **at most** \( n - 1 \) between every ordered pair of vertices, and strong connectivity asks for a walk of any length. The two agree because a walk can always be shortened to a path, and a path has at most \( n - 1 \) edges.
:::

::: {.proof}
By @lem-powers-and-walks (b), \( (\I + \A)^{n-1} > 0 \) if and only if, for every ordered pair \( (j, i) \), there is a walk of length at most \( n - 1 \) from \( j \) to \( i \). By @lem-walk-contains-path, if there is any walk from \( j \) to \( i \) then there is one of length at most \( n - 1 \), namely a path; so the condition is equivalent to asking for a walk of any length from \( j \) to \( i \), for every ordered pair. That is @def-strongly-connected, and by @thm-irreducible-iff-strongly-connected it is equivalent to irreducibility.
:::

Both sides always hold for \( n = 1 \), as the convention intends. The hypothesis \( \A \ge 0 \) cannot be dropped: \( \begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix} \) is irreducible, but adding \( \I \) cancels its diagonal and leaves the swap, which is not positive. Cancellation is exactly what non-negativity rules out, since a sum of non-negative terms is zero only when every term is.

::: {#exm-cycle-power}
[The cycle, by one power]

For the cycle \( \C = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} \), compute \( (\I + \C)^2 \), and compare with the powers \( \C^{k} \).
:::

::: {.solution}
\( \C \) is the permutation matrix of \( 1 \mapsto 2 \mapsto 3 \mapsto 1 \), so \( \C^2 = \begin{psmallmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{psmallmatrix} \) and \( \C^3 = \I \) by @lem-permutation-matrices (a). As \( \I \) and \( \C \) commute,
\[
(\I + \C)^2 = \I + 2\C + \C^2 = \begin{pmatrix} 1 & 1 & 2 \\ 2 & 1 & 1 \\ 1 & 2 & 1 \end{pmatrix} > 0 ,
\]
so \( \C \) is irreducible by @thm-irreducible-power-positive, as the graph already showed. On the other hand every power \( \C^{k} \) is \( \I \), \( \C \) or \( \C^2 \), each with six zero entries, so **no** power of \( \C \) is positive. In the graph, the walks from \( j \) have lengths forced modulo \( 3 \) by where they end. The loops of \( \I + \C \) let a walk wait, which is what \( \C \) alone cannot do. §05 returns to this difference; it is the difference between irreducible and primitive.
:::

The theorem is the reason irreducibility is enough for most of Perron's conclusions. If \( \A \ge 0 \) is irreducible, then \( \B = (\I + \A)^{n-1} \) is positive, so @thm-perron applies to \( \B \), and \( \B \) is a polynomial in \( \A \), so every eigenvector of \( \A \) is an eigenvector of \( \B \). §03 turns this observation into the Perron–Frobenius theorem.

## The reducible normal form

A reducible matrix splits into two diagonal blocks, and each block may be reducible again. Splitting until nothing splits gives a normal form.

::: {#thm-reducible-normal-form}
[Reducible Normal Form]

Let \( n \ge 1 \) and \( \A \in M_n(F) \).

::: {.enumerate options="label=(\alph*)"}
1. There are a permutation matrix \( \P \) and an integer \( m \ge 1 \) such that
   \[
   \P\tp\A\P = \begin{pmatrix} \A_{11} & \A_{12} & \cdots & \A_{1m} \\ 0 & \A_{22} & \cdots & \A_{2m} \\ \vdots & & \ddots & \vdots \\ 0 & \cdots & 0 & \A_{mm} \end{pmatrix} ,
   \]
   block upper triangular, with every diagonal block \( \A_{ii} \) square and **irreducible**.
2. In that case \( p_{\A} = p_{\A_{11}}\,p_{\A_{22}}\cdots p_{\A_{mm}} \), so the eigenvalues of \( \A \), with their algebraic multiplicities, are those of the diagonal blocks taken together.
3. \( \rho(\A) = \max_i \rho(\A_{ii}) \); if \( \A \ge 0 \), every \( \A_{ii} \ge 0 \).
:::
:::

::: {.idea}
Strong induction on \( n \): if \( \A \) is irreducible there is nothing to do, and otherwise one relabeling gives two smaller diagonal blocks, which the induction hypothesis puts in normal form. The only work is to check that the two relabelings of the blocks combine into one relabeling of \( \A \), and block multiplication does that.
:::

::: {.proof}
(a) Strong induction on \( n \) (@thm-strong-induction). If \( \A \) is irreducible, which includes the case \( n = 1 \), take \( \P = \I \) and \( m = 1 \). Otherwise \( n \ge 2 \), and there are a permutation matrix \( \P_0 \) and \( 1 \le k \le n - 1 \) with
\[
\P_0\tp\A\P_0 = \begin{pmatrix} \B & \C \\ 0 & \D \end{pmatrix}, \qquad \B \in M_k(F),\ \D \in M_{n-k}(F) .
\]
Both sizes are less than \( n \), so by the induction hypothesis there are permutation matrices \( \Q_1 = \P_\alpha \) (\( \alpha \in S_k \)) and \( \Q_2 = \P_\beta \) (\( \beta \in S_{n-k} \)) such that \( \Q_1\tp\B\Q_1 \) and \( \Q_2\tp\D\Q_2 \) are block upper triangular with square irreducible diagonal blocks. The direct sum \( \Q = \Q_1 \oplus \Q_2 \) (@def-block-diagonal) is the permutation matrix \( \P_\gamma \) of the permutation \( \gamma \) with \( \gamma(t) = \alpha(t) \) for \( t \le k \) and \( \gamma(k + q) = k + \beta(q) \) for \( q \le n - k \), since its columns are \( \e_{\gamma(1)}, \dots, \e_{\gamma(n)} \). By @prp-block-transpose, \( \Q\tp = \Q_1\tp \oplus \Q_2\tp \), and by @thm-block-multiplication,
\[
\Q\tp\bigl(\P_0\tp\A\P_0\bigr)\Q = \begin{pmatrix} \Q_1\tp\B\Q_1 & \Q_1\tp\C\Q_2 \\ 0 & \Q_2\tp\D\Q_2 \end{pmatrix} .
\]
This is block upper triangular, and its diagonal blocks are those of \( \Q_1\tp\B\Q_1 \) followed by those of \( \Q_2\tp\D\Q_2 \), all square and irreducible. With \( \P = \P_0\Q \), which is a permutation matrix by @lem-permutation-matrices (a), the left side is \( \P\tp\A\P \) by @thm-transpose-properties. This proves (a).

(b) \( \P\tp = \P^{-1} \) by @lem-permutation-matrices (b), so \( \P\tp\A\P \) is similar to \( \A \), and \( p_{\A} = p_{\P\tp\A\P} \) by @thm-charpoly-similarity-invariant. The matrix \( x\I - \P\tp\A\P \) is block upper triangular with diagonal blocks \( x\I - \A_{ii} \). Applying @thm-det-block-triangular over \( F[x] \), as the paragraph after it notes, to the first diagonal block and the rest, and then to the rest by induction on \( m \), gives \( p_{\A} = \prod_i p_{\A_{ii}} \). The roots of a product, with multiplicities, are those of the factors together.

(c) By (b), \( \spec(\A) = \bigcup_i\spec(\A_{ii}) \), and the largest modulus over a union is the largest of the largest moduli. If \( \A \ge 0 \), then by @lem-permutation-similarity-entries the entries of \( \P\tp\A\P \) are entries of \( \A \), so they are \( \ge 0 \), and so are those of each \( \A_{ii} \).
:::

The diagonal blocks of the normal form correspond to groups of vertices of \( G(\A) \) that can all reach one another. The first block is a group with no exit, and each later block can send edges only to the blocks before it. In a Markov chain the first block is therefore a set of states that the chain, once inside, never leaves; §06 uses exactly this. The blocks are unique up to their order and up to relabeling within each block, but we shall not need this and do not prove it.

::: {#exm-normal-form-four}
[A normal form with three blocks]

Put \( \A = \begin{pmatrix} 0 & 0 & 1 & 0 \\ 1 & 2 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 3 \end{pmatrix} \) in reducible normal form, and find \( \rho(\A) \).
:::

::: {.solution}
Read the edges column by column. Column \( 1 \) gives \( 1 \to 2 \) and \( 1 \to 3 \); column \( 2 \) gives the loop \( 2 \to 2 \); column \( 3 \) gives \( 3 \to 1 \) and \( 3 \to 4 \); column \( 4 \) gives \( 4 \to 2 \) and the loop \( 4 \to 4 \). So \( 1 \) and \( 3 \) reach each other, and from them one can go to \( 4 \) and then to \( 2 \), but never back. The groups are \( \{2\} \), \( \{4\} \) and \( \{1, 3\} \). Vertex \( 2 \) has no exit, so it comes first; the edges from \( 4 \) go only to \( 2 \) and \( 4 \), so \( 4 \) comes next; then \( 1, 3 \). With \( \sigma = (2, 4, 1, 3) \), that is \( \sigma(1) = 2 \), \( \sigma(2) = 4 \), \( \sigma(3) = 1 \), \( \sigma(4) = 3 \), @lem-permutation-similarity-entries gives
\[
\P_\sigma\tp\A\P_\sigma = \begin{pmatrix} 2 & 1 & 1 & 0 \\ 0 & 3 & 0 & 1 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix} ,
\]
with diagonal blocks \( (2) \), \( (3) \) and the swap \( \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \), each irreducible. By @thm-reducible-normal-form (b), \( p_{\A}(x) = (x - 2)(x - 3)(x^2 - 1) \), so the eigenvalues are \( 2, 3, 1, -1 \), and \( \rho(\A) = 3 \), the spectral radius of the second block.
:::

## Exercises

### A. Check your understanding

:::: {#exr-irreducibility-and-graphs-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the directed graph \( G(\A) \), a walk, and strong connectivity. Which way does the edge for \( a_{ij} \ne 0 \) point?
2. Define **irreducible**, including the case \( n = 1 \), and state @thm-irreducible-power-positive.
3. True or false: a matrix with a zero entry is reducible. Justify your answer.
4. True or false: if \( \A \ge 0 \) is irreducible, then so is \( \A^2 \). Justify your answer.
5. True or false: \( \A \) is irreducible if and only if \( \A\tp \) is. Justify your answer.
6. True or false: the \( 2 \times 2 \) zero matrix is irreducible. Justify your answer.
:::
::::

::: {.solution}
(a) \( G(\A) \) has vertices \( 1, \dots, n \) and an edge \( j \to i \) for each \( a_{ij} \ne 0 \), pointing from the column index to the row index. A walk of length \( k \) from \( j \) to \( i \) is a list \( j = i_0, \dots, i_k = i \) with each \( i_{t-1} \to i_t \) an edge. \( G(\A) \) is strongly connected if there is a walk from \( j \) to \( i \) for every ordered pair \( (j, i) \).

(b) For \( n \ge 2 \), \( \A \) is reducible if \( \P\tp\A\P = \begin{psmallmatrix} \B & \C \\ 0 & \D \end{psmallmatrix} \) for some permutation matrix \( \P \) and square blocks \( \B \), \( \D \) of sizes \( k \) and \( n - k \), \( 1 \le k \le n - 1 \); irreducible means not reducible. Every \( 1 \times 1 \) matrix is irreducible. The theorem: a non-negative \( \A \in M_n(\nR) \) is irreducible if and only if \( (\I + \A)^{n-1} > 0 \).

(c) False. The swap \( \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix} \) has two zero entries and is irreducible, since its graph \( 1 \to 2 \to 1 \) is strongly connected (@thm-irreducible-iff-strongly-connected).

(d) False. The swap is irreducible and its square \( \I_2 \) is reducible, being triangular.

(e) True. \( G(\A\tp) \) is \( G(\A) \) with every edge reversed, since \( (\A\tp)_{ij} = a_{ji} \). Reversing a walk from \( j \) to \( i \) in \( G(\A) \) gives a walk from \( i \) to \( j \) in \( G(\A\tp) \), so one graph is strongly connected exactly when the other is, and @thm-irreducible-iff-strongly-connected finishes.

(f) False. With \( n = 2 \), the zero matrix is already upper triangular, so it is reducible with \( \P = \I \), \( k = 1 \). Only the \( 1 \times 1 \) zero matrix is irreducible, and that by convention.
:::

### B. Practice

:::: {#exr-irreducibility-and-graphs-b1}
[B1: Deciding irreducibility]

Determine which of the following matrices are irreducible. Justify your answers, and for each reducible one give a permutation matrix that puts it in block upper triangular form.

::: {.enumerate options="label=(\alph*)"}
1. \( \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix} \)
2. \( \begin{pmatrix} 1 & 2 & 0 \\ 0 & 3 & 0 \\ 4 & 5 & 6 \end{pmatrix} \)
3. \( \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 1 & 0 & 0 \end{pmatrix} \)
4. \( \begin{pmatrix} 1 & 1 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 1 \\ 0 & 0 & 1 & 1 \end{pmatrix} \)
:::
::::

::: {.solution}
(a) The non-zero entries \( a_{12}, a_{23}, a_{31} \) give the edges \( 2 \to 1 \), \( 3 \to 2 \), \( 1 \to 3 \): the cycle \( 1 \to 3 \to 2 \to 1 \), which is strongly connected. Irreducible, by @thm-irreducible-iff-strongly-connected.

(b) Column \( 3 \) has its only non-zero entry in row \( 3 \), so \( S = \{3\} \) has no exit, and the matrix is reducible by @lem-reducible-closed-set. With \( \sigma(1) = 3 \), \( \sigma(2) = 1 \), \( \sigma(3) = 2 \), @lem-permutation-similarity-entries gives \( \P_\sigma\tp\A\P_\sigma = \begin{psmallmatrix} 6 & 4 & 5 \\ 0 & 1 & 2 \\ 0 & 0 & 3 \end{psmallmatrix} \), which is even triangular.

(c) The edges are \( 1 \to 4 \) (from \( a_{41} \)), \( 2 \to 1 \) and \( 2 \to 4 \) (from \( a_{12}, a_{42} \)), \( 3 \to 2 \) (from \( a_{23} \)) and \( 4 \to 3 \) (from \( a_{34} \)). The walk \( 1 \to 4 \to 3 \to 2 \to 1 \) passes through every vertex and returns, so any vertex reaches any other by following it. Irreducible.

(d) Columns \( 3 \) and \( 4 \) have zeros in rows \( 1 \) and \( 2 \), so \( S = \{3, 4\} \) has no exit: reducible. With \( \sigma = (3, 4, 1, 2) \), \( \P_\sigma\tp\A\P_\sigma = \begin{psmallmatrix} 1 & 1 & 0 & 1 \\ 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 1 & 1 \end{psmallmatrix} \). The edge \( 2 \to 3 \) goes into \( S \), which is allowed; only edges out of \( S \) are forbidden.
:::

:::: {#exr-irreducibility-and-graphs-b2}
[B2: One power decides]

For each matrix, compute \( (\I + \A)^2 \) and decide whether \( \A \) is irreducible. For the reducible one, read off from \( (\I + \A)^2 \) a set of vertices with no exit.

::: {.enumerate options="label=(\alph*)"}
1. \( \A = \begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} \)
2. \( \A = \begin{pmatrix} 1 & 0 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix} \)
:::
::::

::: {.solution}
(a) \( \I + \A = \begin{psmallmatrix} 1 & 1 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{psmallmatrix} \), and multiplying out,
\[
(\I + \A)^2 = \begin{pmatrix} 2 & 3 & 2 \\ 2 & 2 & 1 \\ 1 & 2 & 1 \end{pmatrix} > 0 .
\]
Hence \( \A \) is irreducible by @thm-irreducible-power-positive.

(b) \( \I + \A = \begin{psmallmatrix} 2 & 0 & 0 \\ 1 & 1 & 1 \\ 0 & 1 & 1 \end{psmallmatrix} \), and
\[
(\I + \A)^2 = \begin{pmatrix} 4 & 0 & 0 \\ 3 & 2 & 2 \\ 1 & 2 & 2 \end{pmatrix} ,
\]
which has zero entries, so \( \A \) is reducible. By @lem-powers-and-walks (b), column \( j \) of \( (\I + \A)^{2} \) is positive exactly in the rows \( i \) reachable from \( j \). Column \( 2 \) is positive in rows \( 2, 3 \) only, so the vertices reachable from \( 2 \) form \( S = \{2, 3\} \), and by the proof of @thm-irreducible-iff-strongly-connected no edge leaves it. Indeed \( a_{12} = a_{13} = 0 \).
:::

:::: {#exr-irreducibility-and-graphs-b3}
[B3: Eigenvalues from the normal form]

Let \( \A = \begin{pmatrix} 1 & 0 & 2 \\ 1 & 3 & 0 \\ 4 & 0 & 5 \end{pmatrix} \). Put \( \A \) in reducible normal form, and hence find its eigenvalues and \( \rho(\A) \).
::::

::: {.solution}
The edges are \( 1 \to 1 \), \( 1 \to 2 \), \( 1 \to 3 \) (column \( 1 \)), the loop \( 2 \to 2 \) (column \( 2 \)), and \( 3 \to 1 \), \( 3 \to 3 \) (column \( 3 \)). Vertex \( 2 \) has no exit, and \( 1 \), \( 3 \) reach each other. List \( 2 \) first: \( \sigma(1) = 2 \), \( \sigma(2) = 1 \), \( \sigma(3) = 3 \). By @lem-permutation-similarity-entries,
\[
\P_\sigma\tp\A\P_\sigma = \begin{pmatrix} 3 & 1 & 0 \\ 0 & 1 & 2 \\ 0 & 4 & 5 \end{pmatrix} .
\]
The blocks \( (3) \) and \( \begin{psmallmatrix} 1 & 2 \\ 4 & 5 \end{psmallmatrix} \) are irreducible, the second because both its off-diagonal entries are non-zero. By @thm-reducible-normal-form (b), \( p_{\A}(x) = (x - 3)(x^2 - 6x - 3) \), so the eigenvalues are \( 3 \) and \( 3 \pm 2\sqrt3 \), and by (c), \( \rho(\A) = 3 + 2\sqrt3 \approx 6.46 \), coming from the second block.
:::

### C. Going deeper

:::: {#exr-irreducibility-and-graphs-c1}
[C1: A necessary condition that is not sufficient]

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( n \ge 2 \) and \( \A \in M_n(F) \) is irreducible, then every row and every column of \( \A \) contains a non-zero entry off the diagonal.
2. Show that the converse fails for every even \( n \ge 4 \).
:::
::::

::: {.solution}
(a) Suppose column \( j \) has no non-zero entry off the diagonal: \( a_{ij} = 0 \) for all \( i \ne j \). Then \( S = \{j\} \) has no exit, and \( S \) is neither empty nor everything because \( n \ge 2 \), so \( \A \) is reducible by @lem-reducible-closed-set. Suppose instead row \( i \) has \( a_{ij} = 0 \) for all \( j \ne i \). Then \( S = \{1, \dots, n\} \setminus \{i\} \) has no exit, since the only entries \( a_{i'j} \) with \( j \in S \) and \( i' \notin S \) are the \( a_{ij} \) with \( j \ne i \); again \( \A \) is reducible.

(b) Let \( n = 2m \) with \( m \ge 2 \), and let \( \M \) be the direct sum of \( m \) copies of the swap \( \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix} \). Every row and column has a \( 1 \) off the diagonal. But \( S = \{1, 2\} \) has no exit, since column \( 1 \) and column \( 2 \) are zero outside rows \( 1, 2 \), so \( \M \) is reducible. The Quick check is the case \( m = 2 \).
:::

:::: {#exr-irreducibility-and-graphs-c2}
[C2: The exponent \( n - 1 \) is sharp]

Let \( n \ge 2 \) and let \( \C_n \) be the cyclic permutation matrix with \( \C_n\e_j = \e_{j+1} \) for \( j < n \) and \( \C_n\e_n = \e_1 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \C_n \) is irreducible, but that \( (\I + \C_n)^{n-2} \) is not positive.
2. Prove that if \( \A \ge 0 \) is irreducible, then \( (\I + \A)^{k} > 0 \) for every \( k \ge n - 1 \).
:::
::::

::: {.solution}
(a) The non-zero entries of \( \C_n \) are \( (\C_n)_{j+1,j} = 1 \) for \( j < n \) and \( (\C_n)_{1n} = 1 \), so the edges of \( G(\C_n) \) are \( j \to j + 1 \) and \( n \to 1 \), and there are no others. Following them from any vertex visits every vertex, so \( G(\C_n) \) is strongly connected and \( \C_n \) is irreducible (@thm-irreducible-iff-strongly-connected). Each vertex has exactly one outgoing edge, so the only walk from \( 1 \) of length \( m \le n - 1 \) is \( 1 \to 2 \to \dots \to m + 1 \). In particular the shortest walk from \( 1 \) to \( n \) has length \( n - 1 \), and there is no walk of length at most \( n - 2 \) from \( 1 \) to \( n \). By @lem-powers-and-walks (b), \( \bigl((\I + \C_n)^{n-2}\bigr)_{n1} = 0 \).

(b) By @lem-powers-and-walks (b), \( ((\I + \A)^{k})_{ij} > 0 \) exactly when there is a walk of length at most \( k \) from \( j \) to \( i \). For \( k \ge n - 1 \), a walk of length at most \( n - 1 \) is one of length at most \( k \), and such walks exist for every pair by the proof of @thm-irreducible-power-positive. Hence \( (\I + \A)^{k} > 0 \).
:::

:::: {#exr-irreducibility-and-graphs-c3}
[C3: Irreducibility as growth of supports]

Let \( n \ge 2 \) and \( \A \in M_n(\nR) \) with \( \A \ge 0 \). For \( \x \ge \0 \), call \( \{i : x_i > 0\} \) the **support** of \( \x \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that the support of \( (\I + \A)\x \) is the support \( S \) of \( \x \) together with every vertex \( i \) for which there is an edge \( j \to i \) with \( j \in S \).
2. Prove that \( \A \) is irreducible if and only if, for every \( \x \ge \0 \) with at least one zero entry and at least one positive entry, \( (\I + \A)\x \) has more positive entries than \( \x \).
3. Deduce, without using walks, that \( (\I + \A)^{n-1}\x > \0 \) for every non-zero \( \x \ge \0 \) when \( \A \) is irreducible, and hence that \( (\I + \A)^{n-1} > 0 \).
:::

*Hint for (b): use @lem-reducible-closed-set.*
::::

::: {.solution}
(a) \( ((\I + \A)\x)_i = x_i + \sum_j a_{ij}x_j \) is a sum of non-negative terms, so it is positive if and only if \( x_i > 0 \) or some \( a_{ij}x_j > 0 \), that is, \( i \in S \) or there is \( j \in S \) with \( a_{ij} > 0 \), which is an edge \( j \to i \).

(b) Let \( \x \) be as stated, with support \( S \), which is neither empty nor everything. By (a), \( (\I + \A)\x \) has support containing \( S \), and strictly larger exactly when some edge goes from \( S \) to a vertex outside \( S \). \( (\Rightarrow) \) If \( \A \) is irreducible, @lem-reducible-closed-set says every such \( S \) has an exit, so the support grows. \( (\Leftarrow) \) If \( \A \) were reducible, take \( S \) with no exit from @lem-reducible-closed-set, and let \( \x \) have entry \( 1 \) on \( S \) and \( 0 \) elsewhere. Then \( (\I + \A)\x \) has support exactly \( S \), with the same number of positive entries, contradicting the hypothesis.

(c) Let \( \x \ge \0 \), \( \x \ne \0 \), and put \( \x_k = (\I + \A)^{k}\x \ge \0 \). By (a) the supports never shrink, and by (b) the support grows by at least one element at each step until it is everything. It starts with at least one element, so after at most \( n - 1 \) steps it has \( n \), and then stays so: \( \x_{n-1} > \0 \). Applying this to \( \x = \e_j \) shows that column \( j \) of \( (\I + \A)^{n-1} \) is positive, for every \( j \).
:::
