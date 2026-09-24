# Graph Laplacians

Chapter 2 built the incidence matrix of a network, used it to solve flow problems, and then set one object aside with a promise: the matrix \( \N\N\tp \), the graph Laplacian, "returns in Chapter 23". Chapter 6 left a second debt at the same address. Its exercise @exr-minors-and-rank-c1 computed, for one four-vertex network, that \( \det\L_0 \) equals the number of spanning trees, and named the general statement the matrix-tree theorem, leaving a proof "which Chapter 23 completes". This section pays both debts. It also does something the two earlier chapters could not: with the spectral theory of Chapters 11 and 16 in hand, we can read the eigenvalues of \( \L \) and find the shape of the graph in them.

Throughout, a **graph** means what Chapter 2 §07 called a network with its orientation forgotten: a finite set of vertices \( 1, \dots, m \) and a finite set of edges \( 1, \dots, k \), each edge joining two **distinct** vertices. Two edges may join the same pair. An **orientation** chooses, for each edge \( e \), a tail and a head, and turns the graph back into one of Chapter 2's networks with an incidence matrix \( \N \in M_{m \times k}(\nR) \) (@def-incidence-matrix).

## The Laplacian of a graph

The matrix \( \N\N\tp \) has already appeared three times without being studied: named and postponed in the closing sentence of Chapter 2 §07's flow-network subsection; implicitly in @exr-applications-c3, where the kernel of \( \N\tp \) — which, as we shall see, is the kernel of \( \N\N\tp \) — turned out to be spanned by the indicator vectors of the components; and in @exr-minors-and-rank-c1, where its determinant counted something combinatorial. A product that keeps coming back deserves a name.

*The Laplacian of a graph is the matrix that turns a labeling of the vertices into the total squared disagreement across the edges.*

::: {#def-graph-laplacian}
[Graph Laplacian]

Let \( G \) be a graph with vertices \( 1, \dots, m \) and \( k \ge 1 \) edges, and fix **any** orientation of \( G \), with incidence matrix \( \N \in M_{m \times k}(\nR) \). The **Laplacian** of \( G \) is
\[
\L \coloneqq \N\N\tp \in M_m(\nR) .
\]
:::

In words: the \( (u, v) \)-entry of \( \L \) is the dot product of row \( u \) and row \( v \) of \( \N \), that is, the sum over all edges of the product of the two incidence entries. The definition names an orientation, and the first thing to check is that the orientation leaves no trace.

Write \( \deg(v) \) for the number of edges meeting the vertex \( v \), and \( a_{uv} \) for the number of edges joining \( u \) to \( v \) when \( u \ne v \), with \( a_{vv} = 0 \). Let \( \D = \diag(\deg(1), \dots, \deg(m)) \) be the **degree matrix** and \( \A = (a_{uv}) \) the **adjacency matrix**. Neither mentions an orientation.

::: {#prp-laplacian-basic}
[First Properties of the Laplacian]

Let \( G \) be a graph on \( m \) vertices with \( k \ge 1 \) edges and Laplacian \( \L \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \L = \D - \A \); in particular \( \L \) is symmetric and does **not** depend on the orientation chosen in @def-graph-laplacian.
2. For every \( \x \in \nR^m \),
   \[
   \x\tp\L\x = \sum_{e = 1}^{k} \bigl(x_{u_e} - x_{v_e}\bigr)^2 ,
   \]
   where \( u_e \) and \( v_e \) are the two ends of the edge \( e \). Consequently \( \L \succeq 0 \).
3. \( \L\1 = \0 \), where \( \1 = (1, \dots, 1) \in \nR^m \).
:::
:::

::: {.idea}
Everything is one line of \( \N \). Part (a) reads the product \( \N\N\tp \) entry by entry, using that a column of \( \N \) has exactly one \( 1 \) and one \( -1 \). Part (b) is the observation that \( \x\tp\N\N\tp\x \) is the squared length of \( \N\tp\x \), and Chapter 2 already identified \( \N\tp\x \) as the vector of differences across the edges. Part (c) is (b) applied to a constant vector, or the fact that each column of \( \N \) sums to zero.
:::

::: {.proof}
(a) By @thm-three-views-of-product, \( (\N\N\tp)_{uv} = \sum_{e} \N_{ue}\N_{ve} \). If \( u = v \), then \( \N_{ue}^2 \) is \( 1 \) when \( e \) meets \( u \) and \( 0 \) otherwise (@def-incidence-matrix), so the sum is \( \deg(u) \). If \( u \ne v \), then \( \N_{ue}\N_{ve} \ne 0 \) only for an edge \( e \) with one end \( u \) and the other \( v \), and such an edge contributes \( 1 \cdot (-1) = -1 \) whichever way it is oriented; so the sum is \( -a_{uv} \). Hence \( \L = \D - \A \). Both \( \D \) and \( \A \) are determined by \( G \) alone, and \( \A \) is symmetric because \( a_{uv} = a_{vu} \), so \( \L\tp = \L \).

(b) As in the proof of @prp-incidence-rank-connected, entry \( e \) of \( \N\tp\x \) is \( x_{\operatorname{tail}(e)} - x_{\operatorname{head}(e)} \), which is \( \pm(x_{u_e} - x_{v_e}) \). Therefore
\[
\x\tp\L\x = \x\tp\N\N\tp\x = (\N\tp\x)\tp(\N\tp\x) = \norm{\N\tp\x}^2 ,
\]
and expanding the squared length coordinate by coordinate gives the stated sum, the signs disappearing because each term is squared. For the standard real inner product, \( \inner{\L\x}{\x} = \x\tp\L\x \), which is a sum of squares of real numbers and hence \( \ge 0 \); and \( \L \) is symmetric by (a). So \( \L \succeq 0 \) by @def-positive-semidefinite.

(c) Each column of \( \N \) has exactly one \( 1 \) and one \( -1 \), so \( \N\tp\1 = \0 \), and \( \L\1 = \N(\N\tp\1) = \0 \).
:::

Part (b) is the whole reason the Laplacian is useful. A vector \( \x \in \nR^m \) is a **labeling** of the vertices by numbers, and \( \x\tp\L\x \) measures how badly the labeling disagrees across the edges: it is zero exactly when the labeling is locally constant, and large when neighbors receive very different numbers. Every statement in this section is a consequence of that one reading.

::: {#exm-laplacian-two-ways}
[A Laplacian computed twice]

Let \( G \) be the four-vertex graph of @exr-minors-and-rank-c1: vertices \( 1, 2, 3, 4 \) and edges \( e_1 = \{1,2\} \), \( e_2 = \{2,3\} \), \( e_3 = \{3,4\} \), \( e_4 = \{4,1\} \), \( e_5 = \{1,3\} \). Compute \( \L \) from \( \D - \A \) and from \( \N\N\tp \), and check them against each other.
:::

::: {.solution}
The degrees are \( \deg(1) = 3 \), \( \deg(2) = 2 \), \( \deg(3) = 3 \), \( \deg(4) = 2 \), and every pair of vertices is joined by at most one edge, the missing pair being \( \{2, 4\} \). Hence
\[
\D - \A =
\begin{pmatrix} 3 & 0 & 0 & 0 \\ 0 & 2 & 0 & 0 \\ 0 & 0 & 3 & 0 \\ 0 & 0 & 0 & 2 \end{pmatrix}
-
\begin{pmatrix} 0 & 1 & 1 & 1 \\ 1 & 0 & 1 & 0 \\ 1 & 1 & 0 & 1 \\ 1 & 0 & 1 & 0 \end{pmatrix}
=
\begin{pmatrix} 3 & -1 & -1 & -1 \\ -1 & 2 & -1 & 0 \\ -1 & -1 & 3 & -1 \\ -1 & 0 & -1 & 2 \end{pmatrix}.
\]
Orienting the edges as \( 1 \to 2 \), \( 2 \to 3 \), \( 3 \to 4 \), \( 4 \to 1 \), \( 1 \to 3 \) gives the incidence matrix of @exr-minors-and-rank-c1,
\[
\N = \begin{pmatrix} 1 & 0 & 0 & -1 & 1 \\ -1 & 1 & 0 & 0 & 0 \\ 0 & -1 & 1 & 0 & -1 \\ 0 & 0 & -1 & 1 & 0 \end{pmatrix},
\]
whose row \( 1 \) has squared length \( 1 + 1 + 1 = 3 \), and whose rows \( 1 \) and \( 2 \) have dot product \( 1 \cdot (-1) = -1 \). Continuing entry by entry reproduces the matrix above, so the two computations agree. Reversing the orientation of the edge \( 1 \to 2 \) changes the first two rows of \( \N \) in their first entry only, from \( 1 \) and \( -1 \) to \( -1 \) and \( 1 \); the diagonal entries are unchanged because they are sums of squares, and the \( (1,2) \)-entry is still \( (-1)\cdot 1 = -1 \).
:::

::: {.warning}
**Take the oriented incidence matrix, not the unoriented one.** If one replaces the \( -1 \) in @def-incidence-matrix by \( +1 \), obtaining the matrix \( \M \) with a \( 1 \) at both ends of each edge, then \( \M\M\tp = \D + \A \), not \( \D - \A \). That matrix is also symmetric and positive semidefinite, but it is a different matrix with a different kernel: for the triangle, \( \D - \A \) is singular while \( \D + \A \) has determinant \( 4 \). The signs are what make @prp-laplacian-basic (b) a sum of **differences**, and the sign convention returns in @lem-incidence-minors-unimodular, where it is load-bearing again.
:::

::: {.check}
The graph of @exm-laplacian-two-ways has the labeling \( \x = (1, 1, 0, 0) \). Compute \( \x\tp\L\x \) from the edge formula, and say which edges contribute.
:::

::: {.solution}
By @prp-laplacian-basic (b), each edge contributes the square of the difference of the labels at its ends. The edges \( \{1,2\} \) and \( \{3,4\} \) join equal labels and contribute \( 0 \); the edges \( \{2,3\} \), \( \{4,1\} \) and \( \{1,3\} \) each join a \( 1 \) to a \( 0 \) and contribute \( 1 \). So \( \x\tp\L\x = 3 \), the number of edges crossing between \( \{1,2\} \) and \( \{3,4\} \). Directly: \( \L\x = (3 - 1, -1 + 2, -1 - 1, -1 + 0) = (2, 1, -2, -1) \) and \( \x\tp\L\x = 2 + 1 = 3 \).
:::

## The kernel counts the components

Chapter 2's @exr-applications-c3 computed \( \nul(\N\tp) \) for a network in several pieces. That was an exercise, so we prove what we need here, in the form the spectral theory will use. Recall from @exr-applications-c3 the notion we need: two vertices are **linked** if some sequence of vertices joins them with consecutive vertices sharing an edge, and the equivalence classes of this relation are the **components** of \( G \). That "linked" is an equivalence relation (@def-equivalence-relation) takes one line: it is reflexive by the sequence of length zero, symmetric because a sequence reversed is again one, and transitive because two sequences may be concatenated. So the components partition the vertices (@thm-partition), which is what Step 3 below uses.

::: {#thm-laplacian-kernel}
[The Kernel of the Laplacian]

Let \( G \) be a graph on \( m \) vertices with \( k \ge 1 \) edges, with components \( C_1, \dots, C_c \), and let \( \1_{C_r} \in \nR^m \) be the vector with entry \( 1 \) at the vertices of \( C_r \) and \( 0 \) elsewhere. Then
\[
\nul(\L) = \Span\bigl(\1_{C_1}, \dots, \1_{C_c}\bigr),
\]
this list is a basis, and the eigenvalue \( 0 \) of \( \L \) has multiplicity exactly \( c \). In particular \( \L \) is singular, and \( \nul(\L) = \Span(\1) \) exactly when \( G \) is connected.
:::

::: {.idea}
For a positive semidefinite matrix, lying in the kernel and making the quadratic form vanish are the same condition, and @prp-laplacian-basic (b) turns the second one into a statement with no linear algebra in it at all: the labeling is constant across every edge. Constant across every edge propagates along chains of edges, so it means constant on each component, which is exactly what the indicator vectors describe.
:::

::: {.proof}
**Step 1: \( \x \in \nul(\L) \) if and only if \( \x\tp\L\x = 0 \).** If \( \L\x = \0 \), then \( \x\tp\L\x = 0 \). Conversely, if \( \x\tp\L\x = 0 \), then \( \norm{\N\tp\x}^2 = 0 \) by the display in the proof of @prp-laplacian-basic (b), so \( \N\tp\x = \0 \) and \( \L\x = \N(\N\tp\x) = \0 \).

**Step 2: \( \x\tp\L\x = 0 \) if and only if \( \x \) is constant on each component.** By @prp-laplacian-basic (b), \( \x\tp\L\x \) is a sum of squares of real numbers, so it vanishes if and only if every term does, that is, if and only if \( x_u = x_v \) for every edge with ends \( u \) and \( v \). Suppose this holds and let \( u, w \) lie in the same component. By the definition of linked there is a sequence \( u = w_0, w_1, \dots, w_t = w \) with consecutive vertices joined by an edge, so \( x_u = x_{w_1} = \dots = x_w \). Hence \( \x \) is constant on each component. Conversely, if \( \x \) is constant on each component, then the two ends of any edge lie in the same component and carry the same label, so every term vanishes.

**Step 3: the indicators are a basis.** By Steps 1 and 2, \( \x \in \nul(\L) \) if and only if \( \x = \sum_{r=1}^{c} \lambda_r \1_{C_r} \), where \( \lambda_r \) is the common value of \( \x \) on \( C_r \); so the list spans \( \nul(\L) \). It is linearly independent: if \( \sum_r \lambda_r \1_{C_r} = \0 \), then reading the entry at any vertex of \( C_r \) gives \( \lambda_r = 0 \), since the components are disjoint and only the \( r \)-th vector is non-zero there. Hence \( \dim\nul(\L) = c \).

**Step 4: multiplicity.** \( \L \) is symmetric by @prp-laplacian-basic (a), so by @cor-spectral-real-matrix it is orthogonally diagonalizable, and the number of times \( 0 \) occurs in its eigenvalue list is the dimension of its \( 0 \)-eigenspace, which is \( \nul(\L) \). That dimension is \( c \ge 1 \), so \( \L \) is singular. Finally, \( G \) is connected exactly when \( c = 1 \), and then \( C_1 \) is the whole vertex set and \( \1_{C_1} = \1 \).
:::

This is the first of the two theorems that the Laplacian is for. Notice how little it costs: the entire combinatorial content sits in Step 2, and the only property of \( \L \) used is that its quadratic form is a sum of squares over the edges.

## The Fiedler value

@thm-laplacian-kernel says that \( 0 \) is always an eigenvalue and that its multiplicity detects whether the graph falls apart. The natural next question is quantitative: if the graph is connected, *how* connected is it? The eigenvalue just above \( 0 \) answers this, and the reason is @prp-laplacian-basic (b) again.

Because \( \L \succeq 0 \), all its eigenvalues are \( \ge 0 \) (@thm-psd-characterizations (b)), and it is convenient here to list them **increasingly**, against the book's usual convention. Write
\[
\mu_1(\L) \le \mu_2(\L) \le \dots \le \mu_m(\L)
\]
for the eigenvalues of \( \L \) with multiplicity in increasing order, so that \( \mu_j(\L) = \lambda_{m+1-j}(\L) \) in the decreasing notation of Chapter 16. By @thm-laplacian-kernel, \( \mu_1(\L) = 0 \).

::: {#def-fiedler-value}
[Fiedler value]

Let \( G \) be a graph on \( m \ge 2 \) vertices with at least one edge. The **Fiedler value**, or **algebraic connectivity**, of \( G \) is the **second smallest** eigenvalue \( \mu_2(\L) \) of its Laplacian, counted with multiplicity.
:::

For the complete graph \( K_m \), in which every pair of distinct vertices is joined by one edge, @prp-laplacian-basic (a) gives \( \L = m\I - \J \), where \( \J \) is the all-ones matrix. Every row of \( \J \) equals \( \1\tp \), so \( \rank\J = 1 \) and \( 0 \) is an eigenvalue of \( \J \) of multiplicity \( m-1 \) by @thm-rank-nullity-matrix; and \( \J\1 = m\1 \) supplies the last eigenvalue \( m \). Hence \( \L \) has eigenvalues \( 0 \) once and \( m \) with multiplicity \( m-1 \), and the Fiedler value of \( K_m \) is \( m \). For a graph in two or more pieces it is \( 0 \), by @thm-laplacian-kernel. A single edge on two vertices has Laplacian \( \begin{pmatrix} 1 & -1 \\ -1 & 1\end{pmatrix} \) and Fiedler value \( 2 \). The degenerate case \( m = 1 \) is excluded because there is no second eigenvalue.

::: {#prp-fiedler-positive-iff-connected}
[Positive Fiedler Value Means Connected]

Let \( G \) be a graph on \( m \ge 2 \) vertices with at least one edge. Then \( \mu_2(\L) > 0 \) if and only if \( G \) is connected.
:::

::: {.proof}
The eigenvalues of \( \L \) are \( \ge 0 \), so \( \mu_2(\L) = 0 \) if and only if the eigenvalue \( 0 \) occurs at least twice in the list, that is, if and only if its multiplicity \( c \) is at least \( 2 \) (@thm-laplacian-kernel). That happens exactly when \( G \) has two or more components, that is, exactly when \( G \) is not connected.
:::

The number \( \mu_2(\L) \) is therefore a graded version of connectedness, and the grading has a meaning that can be read off directly.

::: {#prp-fiedler-minimum}
[The Fiedler Value as a Minimum]

Let \( G \) be a graph on \( m \ge 2 \) vertices with at least one edge. Then
\[
\mu_2(\L) = \min\Bigl\{ \tfrac{\x\tp\L\x}{\x\tp\x} \ : \ \x \in \nR^m,\ \x \ne \0,\ \x\tp\1 = 0 \Bigr\} ,
\]
and the minimum is attained at an eigenvector for \( \mu_2(\L) \).
:::

::: {.idea}
The quantity being minimized is the Rayleigh quotient \( R_{\L} \) of Chapter 16. Over all of \( \nR^m \) its minimum is \( \mu_1(\L) = 0 \), attained at \( \1 \), so the constraint \( \x \perp \1 \) exactly removes the direction that achieves \( 0 \). What makes this work is that an orthonormal eigenbasis can be chosen with \( \1/\sqrt m \) as its first member; after that the computation is the weighted-average argument of Chapter 16, run once.
:::

::: {.proof}
Since \( \L \) is symmetric, @cor-spectral-real-matrix supplies an orthonormal basis \( (\q_1, \dots, \q_m) \) of \( \nR^m \) with \( \L\q_j = \mu_j(\L)\q_j \), the eigenvalues in the prescribed increasing order; moreover the basis may be chosen so that \( \q_1 = \1/\sqrt m \). Indeed, let \( E_0 = \nul(\L) \), of dimension \( c \ge 1 \) by @thm-laplacian-kernel, and note \( \1 \in E_0 \) and \( \1 \ne \0 \). Applying Gram–Schmidt (@thm-gram-schmidt) to a basis of \( E_0 \) beginning with \( \1 \) gives an orthonormal basis of \( E_0 \) whose first member is \( \1/\sqrt m \); joining it to orthonormal bases of the other eigenspaces gives the required basis, because \( \mu_1(\L) = \dots = \mu_c(\L) = 0 \) are the eigenvalues attached to \( E_0 \).

Now let \( \x \ne \0 \) with \( \x\tp\1 = 0 \), and write \( c_j = \inner{\x}{\q_j} \), so that \( \x = \sum_j c_j\q_j \) by @thm-orthonormal-coordinates (a). The constraint says \( c_1 = \inner{\x}{\1}/\sqrt m = 0 \). Hence, by @thm-orthonormal-coordinates (b), (c),
\[
\frac{\x\tp\L\x}{\x\tp\x} = \frac{\sum_{j \ge 2}\mu_j(\L)\,c_j^2}{\sum_{j\ge 2} c_j^2} \ \ge\ \mu_2(\L) ,
\]
a weighted average of \( \mu_2(\L), \dots, \mu_m(\L) \) with non-negative weights, not all zero, being at least the smallest of them. Taking \( \x = \q_2 \), which satisfies \( \q_2 \perp \q_1 = \1/\sqrt m \) and is non-zero, gives the value \( \mu_2(\L) \). So the set has minimum \( \mu_2(\L) \), attained at \( \q_2 \).
:::

::: {.remark}
This is the \( k = m-1 \) case of the max–min half of @thm-courant-fischer, read in the increasing indexing: there \( \lambda_{m-1}(\L) = \mu_2(\L) \) is the largest value that any \( (m-1) \)-dimensional subspace can guarantee for \( R_{\L} \), and the proposition says that the particular subspace \( \1^{\perp} \) already guarantees it.
:::

A vector achieving the minimum is called a **Fiedler vector**. It must have entries of both signs, since it is orthogonal to \( \1 \), and @prp-laplacian-basic (b) says it is a labeling that keeps neighbors as close together as it can while being spread out overall. Splitting the vertices by the sign of a Fiedler vector is therefore a reasonable guess at a partition that cuts few edges.

::: {#exm-fiedler-two-triangles}
[Two triangles and a bridge]

Let \( G \) have vertices \( 1, \dots, 6 \) and edges \( \{1,2\} \), \( \{1,3\} \), \( \{2,3\} \), \( \{3,4\} \), \( \{4,5\} \), \( \{4,6\} \), \( \{5,6\} \): two triangles joined by a single edge.

\begin{center}
\begin{tikzpicture}[scale=1.3]
  \fill (0,0.6) circle (2pt) node[left] {$1$};
  \fill (0,-0.6) circle (2pt) node[left] {$2$};
  \fill (1,0) circle (2pt) node[above] {$3$};
  \fill (2,0) circle (2pt) node[above] {$4$};
  \fill (3,0.6) circle (2pt) node[right] {$5$};
  \fill (3,-0.6) circle (2pt) node[right] {$6$};
  \draw[thick] (0,0.6) -- (0,-0.6) -- (1,0) -- (0,0.6);
  \draw[very thick] (1,0) -- (2,0);
  \draw[thick] (3,0.6) -- (3,-0.6) -- (2,0) -- (3,0.6);
\end{tikzpicture}
\end{center}

Find the Fiedler value and a Fiedler vector, and read off the partition.
:::

::: {.solution}
The degrees are \( 2, 2, 3, 3, 2, 2 \), so
\[
\L = \begin{pmatrix}
2 & -1 & -1 & 0 & 0 & 0 \\
-1 & 2 & -1 & 0 & 0 & 0 \\
-1 & -1 & 3 & -1 & 0 & 0 \\
0 & 0 & -1 & 3 & -1 & -1 \\
0 & 0 & 0 & -1 & 2 & -1 \\
0 & 0 & 0 & -1 & -1 & 2
\end{pmatrix}.
\]
Rather than expand a \( 6 \times 6 \) characteristic polynomial, guess the shape of the answer from the symmetry: the graph is carried to itself by the reflection \( 1 \leftrightarrow 6 \), \( 2 \leftrightarrow 5 \), \( 3 \leftrightarrow 4 \), and by the swap \( 1 \leftrightarrow 2 \). Look for an eigenvector reversed by the reflection and fixed by the swap, that is, of the form \( \x = (1, 1, b, -b, -1, -1) \). Rows \( 1 \) and \( 3 \) of \( \L\x = \mu\x \) read
\[
1 - b = \mu, \qquad -2 + 4b = \mu b ,
\]
the other four rows repeating these by symmetry. Substituting \( \mu = 1 - b \) into the second gives \( -2 + 4b = b - b^2 \), that is \( b^2 + 3b - 2 = 0 \), whose positive root is \( b = (\sqrt{17} - 3)/2 \). Then
\[
\mu = 1 - b = \frac{5 - \sqrt{17}}{2} \approx 0.4384 .
\]
The vector \( \x \) satisfies \( \x\tp\1 = 2 + b - b - 2 = 0 \), so by @prp-fiedler-minimum its Rayleigh quotient, which is \( \mu \), is at least \( \mu_2(\L) \); and \( \mu > 0 \), so \( \mu \ne \mu_1(\L) = 0 \). To see that \( \mu \) really is the second smallest, note that \( \x \) and \( \1 \) are eigenvectors for the distinct eigenvalues \( \mu \) and \( 0 \), and check that the remaining four eigenvalues are larger: the vectors \( (1,-1,0,0,0,0) \), \( (0,0,0,0,1,-1) \) and \( (1,1,-2,-2,1,1) \) are eigenvectors for the eigenvalue \( 3 \), as one verifies row by row, and they are visibly independent, so together with \( \1 \) and \( \x \) they account for five of the six. For the third of them, for instance, row \( 3 \) of \( \L \) gives \( -1 - 1 - 6 + 2 = -6 = 3\cdot(-2) \) and row \( 1 \) gives \( 2 - 1 + 2 = 3 = 3\cdot 1 \). The trace of \( \L \) is \( 2+2+3+3+2+2 = 14 \), so the sixth eigenvalue is \( 14 - (0 + \mu + 3 + 3 + 3) = 5 - \mu = (5+\sqrt{17})/2 \), also larger than \( \mu \). Hence
\[
\mu_2(\L) = \frac{5 - \sqrt{17}}{2}, \qquad
\x = \Bigl(1,\, 1,\, \tfrac{\sqrt{17}-3}{2},\, -\tfrac{\sqrt{17}-3}{2},\, -1,\, -1\Bigr)
\]
is a Fiedler vector, and the signs of its entries split the vertices as \( \{1, 2, 3\} \mid \{4, 5, 6\} \): exactly the two triangles, cut along the bridge.
:::

Compare the Fiedler value \( 0.4384\ldots \) of this graph with the value \( 6 \) for \( K_6 \). Small means "nearly disconnected", and the bridge is what makes it small. One general fact in that direction is immediate from Chapter 16.

::: {#prp-fiedler-edge-monotone .optional}
[Adding an Edge Raises No Eigenvalue]

Let \( G \) be a graph on \( m \) vertices with at least one edge, and let \( G' \) be \( G \) with one extra edge joining \( u \ne v \). Then \( \L' = \L + \w\w\tp \) with \( \w = \e_u - \e_v \), and
\[
\mu_j(\L') \ \ge\ \mu_j(\L) \qquad (j = 1, \dots, m).
\]
In particular the Fiedler value does not decrease when an edge is added.
:::

::: {.proof}
The extra edge adds \( 1 \) to \( \deg(u) \) and to \( \deg(v) \) and \( 1 \) to \( a_{uv} \) and \( a_{vu} \), so by @prp-laplacian-basic (a), \( \L' - \L \) has entries \( 1 \) at \( (u,u) \) and \( (v,v) \), \( -1 \) at \( (u,v) \) and \( (v,u) \), and \( 0 \) elsewhere; that matrix is \( \w\w\tp \). Now \( \w\w\tp \) is symmetric, and \( \x\tp\w\w\tp\x = (\w\tp\x)^2 \ge 0 \) for every \( \x \), so \( \w\w\tp \succeq 0 \) and \( \L' \succeq \L \) in the Loewner order (@def-loewner-order). By @cor-loewner-eigenvalue-monotone, \( \lambda_i(\L') \ge \lambda_i(\L) \) for every \( i \), and rewriting the decreasing index \( i = m+1-j \) as the increasing index \( j \) gives the claim.
:::

## Counting spanning trees

Now the second theorem, and the one Chapter 6 promised. Two more words are needed, and both are about the graph alone.

A **cycle** is a set of edges \( \{f_1, \dots, f_t\} \) with \( t \ge 2 \) that can be listed together with distinct vertices \( w_0, w_1, \dots, w_{t-1} \) so that, setting \( w_t = w_0 \), the edge \( f_i \) joins \( w_{i-1} \) to \( w_i \) for each \( i \). Two edges joining the same pair of vertices form a cycle with \( t = 2 \). A **spanning tree** of \( G \) is a set \( T \) of edges such that the graph with all \( m \) vertices and only the edges of \( T \) is connected and contains no cycle. In @exr-minors-and-rank-c1 the phrase was "a set of \( 3 \) edges that connects all four vertices", and the proposition below reconciles the two descriptions.

The bridge from graphs to determinants is the following lemma. It is where such proofs usually go wrong, so read the third part carefully: it is a statement about \( (m-1) \times (m-1) \) submatrices of \( \N \) with one row deleted, not about arbitrary square submatrices, and the "exactly when" is an equivalence in both directions.

::: {#lem-incidence-minors-unimodular}
[Unimodularity of Incidence Minors]

Let \( \N \in M_{m \times k}(\nR) \) be the incidence matrix of an oriented graph \( G \) with \( m \) vertices and \( k \ge 1 \) edges. Write \( \n_e \in \nR^m \) for the column of \( \N \) belonging to the edge \( e \).

::: {.enumerate options="label=(\alph*)"}
1. Every square submatrix of \( \N \) has determinant \( 0 \), \( 1 \) or \( -1 \).
2. For a set \( S \) of edges, the list \( (\n_e)_{e \in S} \) is linearly independent if and only if \( S \) contains no cycle.
3. Fix a vertex \( r \) and put \( I = [m] \setminus \{r\} \). For a set \( S \) of **exactly \( m - 1 \)** edges, \( S \) is a spanning tree of \( G \) if and only if it contains no cycle, and
   \[
   \det \N_{I,S} =
   \begin{cases}
   \pm 1 & \text{if } S \text{ is a spanning tree of } G, \\
   0 & \text{otherwise.}
   \end{cases}
   \]
:::
:::

::: {.idea}
① For (a), induct on the size of the square submatrix and look at its columns. A column of \( \N \) restricted to a subset of the rows keeps at most the one \( 1 \) and the one \( -1 \). If some column of the submatrix is zero, the determinant is \( 0 \); if some column has a single non-zero entry, expand along it and the size drops; and if **every** column has both, then the rows of the submatrix add up to zero, so they are dependent. ② For (b), a cycle gives an explicit dependence — walk around it and the telescoping sum collapses. Conversely a dependence, restricted to the edges with non-zero coefficient, forces every vertex to meet either none or at least two of them, and a finite graph with that property contains a cycle. ③ Part (c) combines the two, once one knows that deleting the row \( r \) costs no rank, which it does not, because the rows of \( \N \) already sum to zero.
:::

::: {.proof}
**(a)** We induct on \( t \), the common number of rows and columns of the square submatrix \( \B = \N_{I',S'} \). For \( t = 1 \), \( \B \) is a single entry of \( \N \), which is \( 0 \), \( 1 \) or \( -1 \) by @def-incidence-matrix. Let \( t \ge 2 \) and assume the claim for \( t - 1 \). Each column of \( \N \) has exactly one \( 1 \) and one \( -1 \), so each column of \( \B \) has at most one \( 1 \) and at most one \( -1 \) and no other non-zero entries. Three cases.

*Case 1: some column of \( \B \) is zero.* Then \( \det\B = 0 \) by @thm-alternating-properties.

*Case 2: some column of \( \B \) has exactly one non-zero entry \( \varepsilon = \pm1 \), in row \( p \) say.* Expanding along that column (@thm-laplace-expansion) gives \( \det\B = \pm\varepsilon\det\B' \), where \( \B' \) is \( \B \) with that row and column deleted. But \( \B' \) is again a square submatrix of \( \N \), of size \( t-1 \), so \( \det\B' \in \{0, 1, -1\} \) by the induction hypothesis, and hence so is \( \det\B \).

*Case 3: every column of \( \B \) has both a \( 1 \) and a \( -1 \).* Then every column sums to \( 0 \), so the sum of all \( t \) rows of \( \B \) is the zero row; the rows are linearly dependent, and \( \det\B = 0 \) by @thm-alternating-properties and @thm-det-transpose.

These three cases are exhaustive, which completes the induction.

**(b)** \( (\Leftarrow) \) We prove the contrapositive: suppose \( \sum_{e \in S} a_e\n_e = \0 \) with some \( a_e \ne 0 \), and let \( S' = \{ e \in S : a_e \ne 0 \} \), a non-empty subset of \( S \). Fix a vertex \( v \). Entry \( v \) of the sum is \( \sum_{e \in S'} a_e \N_{ve} \), and \( \N_{ve} = \pm1 \) exactly for the edges of \( S' \) meeting \( v \), and \( 0 \) otherwise. If exactly one edge \( e_0 \in S' \) met \( v \), that entry would be \( \pm a_{e_0} \ne 0 \), contradicting the sum being \( \0 \). So **every vertex meets either no edge of \( S' \) or at least two**.

Now build a walk. Pick any \( f_1 \in S' \), with ends \( w_0 \) and \( w_1 \). Having reached \( w_i \) along \( f_i \), the vertex \( w_i \) meets at least two edges of \( S' \), so we may choose \( f_{i+1} \in S' \) with \( f_{i+1} \ne f_i \) meeting \( w_i \), and let \( w_{i+1} \) be its other end. Since there are only \( m \) vertices, some vertex repeats; let \( i \) be the smallest index with \( w_i \in \{w_0, \dots, w_{i-1}\} \), and let \( j < i \) be the index with \( w_j = w_i \). Then \( w_j, w_{j+1}, \dots, w_{i-1} \) are distinct, by the minimality of \( i \), and \( f_{j+1}, \dots, f_i \) join them in a closed chain. Put \( t = i - j \). First, \( t \ge 2 \): \( t = 1 \) would mean that \( f_{j+1} \) joins \( w_j \) to itself, and an edge joins two **distinct** vertices. Second, the \( t \) edges are distinct: for \( t = 2 \) that is the construction, \( f_{j+2} \ne f_{j+1} \); and for \( t \ge 3 \) the pairs \( \{w_{a-1}, w_a\} \) for \( j+1 \le a \le i \) are pairwise different pairs of the distinct vertices \( w_j, \dots, w_{i-1} \), so the edges joining them differ. So \( \{f_{j+1}, \dots, f_i\} \) is a cycle, and it lies in \( S' \subseteq S \).

\( (\Rightarrow) \) Again by contraposition. Let \( \{f_1, \dots, f_t\} \subseteq S \) be a cycle with vertices \( w_0, \dots, w_{t-1} \) and \( w_t = w_0 \) as in the definition. For each \( i \) set \( \varepsilon_i = 1 \) if \( f_i \) is oriented from \( w_{i-1} \) to \( w_i \), and \( \varepsilon_i = -1 \) otherwise. By @def-incidence-matrix the column of an edge oriented from \( a \) to \( b \) is \( \e_a - \e_b \), so in either case \( \varepsilon_i\n_{f_i} = \e_{w_{i-1}} - \e_{w_i} \). Summing telescopes:
\[
\sum_{i=1}^{t} \varepsilon_i\n_{f_i} = \e_{w_0} - \e_{w_t} = \0 ,
\]
a dependence with all coefficients \( \pm1 \), so the list \( (\n_e)_{e \in S} \) is dependent.

**(c)** Write \( \N_S = \N_{[m],S} \in M_{m \times (m-1)}(\nR) \) for the full columns and \( \N_{I,S} \in M_{m-1}(\nR) \) for the same columns with row \( r \) deleted. Every column of \( \N \) sums to \( 0 \), so row \( r \) of \( \N_S \) is minus the sum of the other rows; deleting it therefore does not change the row space, and by @thm-row-rank-equals-column-rank
\[
\rank \N_{I,S} = \rank \N_S .
\]
Hence \( \det\N_{I,S} \ne 0 \) if and only if \( \rank\N_S = m-1 \) (@thm-invertible-tfae and @thm-det-nonzero-iff-invertible), that is, if and only if the \( m-1 \) columns \( (\n_e)_{e \in S} \) are linearly independent, which by (b) holds if and only if \( S \) contains no cycle. When it does not vanish, \( \det\N_{I,S} = \pm1 \) by (a).

It remains to check the equivalence in the statement: for a set \( S \) of \( m-1 \) edges, "no cycle" and "spanning tree" agree. A spanning tree contains no cycle by definition. Conversely, suppose \( S \) has \( m-1 \) edges and no cycle; we must show that the graph \( H \) with all \( m \) vertices and the edges of \( S \) is connected. By (b) the columns of \( \N_S \) are independent, so \( \rank\N_S = m-1 \) and \( \dim\col(\N_S) = m-1 \). Each column of \( \N_S \) lies in \( W = \{\z \in \nR^m : z_1 + \dots + z_m = 0\} \), which has dimension \( m-1 \) as computed in the proof of @cor-flow-solvable, so \( \col(\N_S) = W \) by @thm-dim-impl-eq. Suppose \( H \) were disconnected, and let \( C \) be the vertex set of one of its components, so \( \emptyset \ne C \ne [m] \). Every edge of \( S \) has both ends in \( C \) or both ends outside \( C \), so \( \1_C\tp\n_e = 0 \) for every \( e \in S \), and hence \( \1_C\tp\z = 0 \) for every \( \z \in \col(\N_S) = W \). But choosing \( u \in C \) and \( v \notin C \) gives \( \z = \e_u - \e_v \in W \) with \( \1_C\tp\z = 1 \ne 0 \), a contradiction. So \( H \) is connected, and \( S \) is a spanning tree.
:::

::: {.remark}
Part (a) says that \( \N \) is **totally unimodular**, the standard name for a matrix every square submatrix of which has determinant \( 0 \), \( 1 \) or \( -1 \). The orientation is essential: for the triangle with edges \( \{1,2\}, \{2,3\}, \{3,1\} \), the unoriented matrix of the warning above is \( \left(\begin{smallmatrix} 1&0&1 \\ 1&1&0 \\ 0&1&1\end{smallmatrix}\right) \), whose determinant is \( 2 \). Case 3 of the proof is exactly where the \( -1 \) is spent.
:::

One consequence of the last paragraph of the proof is worth recording separately, since it is what makes the sum in the theorem below a sum over spanning trees rather than over sets of every size.

::: {#prp-spanning-tree-size}
[A Spanning Tree Has \( m - 1 \) Edges]

Let \( G \) be a graph on \( m \ge 2 \) vertices. Every spanning tree of \( G \) has exactly \( m - 1 \) edges. Conversely, if a set \( S \) of exactly \( m - 1 \) edges is such that the graph on all \( m \) vertices with edge set \( S \) is connected, then \( S \) is a spanning tree.
:::

::: {.proof}
Let \( T \) be a spanning tree and let \( H \) be the graph on all \( m \) vertices with edge set \( T \). Then \( H \) is connected, so \( T \ne \emptyset \) (for \( m \ge 2 \)) and @prp-incidence-rank-connected applied to \( H \) gives \( \rank\N_T = m-1 \), where \( \N_T \) is the incidence matrix of \( H \) with some orientation, that is, the columns of \( \N \) indexed by \( T \). Also \( T \) contains no cycle, so those columns are linearly independent by @lem-incidence-minors-unimodular (b), and therefore \( \lvert T\rvert = \rank\N_T = m-1 \).

Conversely, let \( S \) have exactly \( m-1 \) edges and let \( H \) be the graph on all \( m \) vertices with edge set \( S \), assumed connected. By @prp-incidence-rank-connected applied to \( H \), \( \rank\N_S = m-1 \), where \( \N_S \) is the incidence matrix of \( H \), that is, the columns of \( \N \) indexed by \( S \); it has \( m-1 \) columns, so @thm-rank-nullity-matrix gives \( \nul(\N_S) = \{\0\} \); since \( \N_S\a = \sum_{e \in S}a_e\n_e \) by @thm-matrix-times-vector-columns, the columns \( (\n_e)_{e \in S} \) are linearly independent. By @lem-incidence-minors-unimodular (b), \( S \) contains no cycle, and \( H \) is connected, so \( S \) is a spanning tree. In particular the sets counted here are exactly the "sets of \( 3 \) edges that connect all four vertices" of @exr-minors-and-rank-c1.
:::

::: {#thm-matrix-tree}
[Matrix-Tree Theorem]

Let \( G \) be a graph on \( m \ge 2 \) vertices with \( k \ge 1 \) edges and Laplacian \( \L \). Fix a vertex \( r \), and let \( \L_0 = \L_{I,I} \in M_{m-1}(\nR) \) be \( \L \) with the row and the column of \( r \) deleted, where \( I = [m] \setminus \{r\} \). Then
\[
\det\L_0 = \#\{\text{spanning trees of } G\} .
\]
In particular the answer does not depend on which vertex \( r \) is deleted, and \( \det\L_0 = 0 \) exactly when \( G \) is disconnected.
:::

::: {.idea}
The determinant of \( \L_0 \) is the determinant of a Gram matrix, because \( \L_0 = \N_0\N_0\tp \) for the reduced incidence matrix \( \N_0 \). @cor-gram-determinant-nonnegative writes such a determinant as a sum of squares of \( (m-1) \times (m-1) \) minors, one for each set of \( m-1 \) edges. @lem-incidence-minors-unimodular says that each of those squares is \( 1 \) for a spanning tree and \( 0 \) for anything else. So the sum counts spanning trees, one apiece. Every step has already been proved; the theorem is the three of them placed in a row.
:::

::: {.proof}
Fix an orientation of \( G \), with incidence matrix \( \N \), and put \( \N_0 = \N_{I,[k]} \in M_{(m-1) \times k}(\nR) \), the matrix \( \N \) with the row of \( r \) deleted.

**Step 1: \( \L_0 = \N_0\N_0\tp \).** By @thm-three-views-of-product, the \( (u,v) \)-entry of \( \N\N\tp \) is row \( u \) of \( \N \) dotted with row \( v \) of \( \N \). Deleting the row and the column of \( r \) from \( \N\N\tp \) therefore leaves exactly the dot products of the rows indexed by \( I \), which is \( \N_0\N_0\tp \).

**Step 2: Cauchy–Binet.** Applying @cor-gram-determinant-nonnegative to \( \N_0 \in M_{(m-1)\times k}(\nR) \),
\[
\det\L_0 = \sum_{\substack{S \subseteq [k] \\ \lvert S\rvert = m-1}} \bigl(\det (\N_0)_{[m-1],S}\bigr)^2 ,
\]
one term for each set \( S \) of exactly \( m-1 \) edges. The submatrix \( (\N_0)_{[m-1],S} \) keeps all rows of \( \N_0 \) and the columns \( S \), so it is the submatrix of \( \N \) on rows \( I \) and columns \( S \), namely \( \N_{I,S} \).

**Step 3: identify the terms.** By @lem-incidence-minors-unimodular (c), \( \det\N_{I,S} = \pm1 \) when \( S \) is a spanning tree and \( 0 \) otherwise, so each term of the sum is \( 1 \) for a spanning tree and \( 0 \) otherwise. By @prp-spanning-tree-size every spanning tree has exactly \( m-1 \) edges, so every spanning tree occurs as one of the sets \( S \), and it occurs once. Hence the sum is the number of spanning trees.

The left-hand side of Step 2 was computed from a particular \( r \), and the right-hand side does not mention \( r \), so the value is the same for every choice. Finally, a disconnected graph has no spanning tree, since a spanning tree is connected on all \( m \) vertices, so the sum is empty and \( \det\L_0 = 0 \). A connected graph has at least one: by @prp-incidence-rank-connected, \( \rank\N = m-1 \), and deleting the row of \( r \) does not change the row space, since every column of \( \N \) sums to \( 0 \), so \( \rank\N_0 = m-1 \) by @thm-row-rank-equals-column-rank. As \( \N_0 \) has \( m-1 \) rows, @thm-rank-via-minors (a) gives a non-zero \( (m-1) \times (m-1) \) minor of \( \N_0 \), which uses all its rows and some set \( S \) of \( m-1 \) columns; that minor is \( \det\N_{I,S} \ne 0 \), so \( S \) is a spanning tree by @lem-incidence-minors-unimodular (c). Hence \( \det\L_0 = 0 \) exactly when \( G \) is disconnected.
:::

::: {#exm-matrix-tree-four-vertices}
[The four-vertex graph, counted both ways]

For the graph of @exm-laplacian-two-ways, compute \( \det\L_0 \) with \( r = 4 \), and list the spanning trees.
:::

::: {.solution}
Deleting the row and column of vertex \( 4 \) from the Laplacian computed in @exm-laplacian-two-ways leaves the \( 3 \times 3 \) matrix whose determinant @exr-minors-and-rank-c1 (a) expands along its first row: \( \det\L_0 = 8 \).

Now count directly. A spanning tree has \( 4 - 1 = 3 \) edges by @prp-spanning-tree-size, and there are \( \binom{5}{3} = 10 \) sets of three edges. By @lem-incidence-minors-unimodular (c) such a set fails to be a spanning tree exactly when it contains a cycle, and the only cycles with three or fewer edges are the triangles \( \{e_1, e_2, e_5\} \) on vertices \( 1,2,3 \) and \( \{e_3, e_4, e_5\} \) on vertices \( 1,3,4 \), in the edge numbering of @exm-laplacian-two-ways. So \( 10 - 2 = 8 \) of the sets are spanning trees, matching \( \det\L_0 = 8 \).

As a check on one term of the sum in the proof, the tree \( \{e_1, e_2, e_3\} \) gives, on rows \( I = \{1,2,3\} \),
\[
\N_{I,\{1,2,3\}} = \begin{pmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & -1 & 1\end{pmatrix},
\]
lower triangular with determinant \( 1 \) (@thm-det-triangular). The matching computation for a non-tree, whose minor is \( 0 \), is @exr-minors-and-rank-c1 (d).
:::

::: {.warning}
**Delete one row and the matching column, and no more.** The Laplacian itself is always singular by @thm-laplacian-kernel, so \( \det\L = 0 \) says nothing. Deleting **two** vertices does not count anything either: for the four-cycle with edges \( \{1,2\}, \{2,3\}, \{3,4\}, \{4,1\} \), striking out the rows and columns of \( 3 \) and \( 4 \) leaves \( \left(\begin{smallmatrix} 2 & -1 \\ -1 & 2\end{smallmatrix}\right) \), of determinant \( 3 \), while the graph has \( 4 \) spanning trees. And the proof needs the deleted row and the deleted column to belong to the **same** vertex, since Step 1 produces a Gram matrix \( \N_0\N_0\tp \) only then; that is a constraint on this route, and nothing above claims that a mismatched pair of deletions counts nothing. Note also that the theorem counts **sets of edges**, so parallel edges count as different trees: two vertices joined by three parallel edges have \( \L = \begin{pmatrix} 3 & -3 \\ -3 & 3\end{pmatrix} \), \( \L_0 = (3) \) and three spanning trees, one per edge.
:::

Two theorems, both proved from the single identity \( \x\tp\L\x = \sum_e (x_{u_e} - x_{v_e})^2 \) and the single factorization \( \L = \N\N\tp \). The first reads the graph's components off the spectrum of \( \L \); the second reads the number of its spanning trees off one determinant, replacing a search over all \( \binom{k}{m-1} \) edge sets by one \( O(m^3) \) elimination (@prp-lu-cost (a)). Both are statements about a graph that no purely combinatorial argument delivers as cheaply.

## Exercises

### A. Check your understanding

::: {#exr-graph-laplacians-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the Laplacian of a graph, and say why it does not depend on the orientation used to define it.
2. Write down the formula for \( \x\tp\L\x \) as a sum over edges, and deduce that \( \L \succeq 0 \).
3. State the matrix-tree theorem, including all its hypotheses.
4. True or false: a graph on \( m \) vertices is connected if and only if \( \rank\L = m - 1 \). Justify your answer.
5. True or false: if \( \L \) has eigenvalue \( 0 \) with multiplicity \( 1 \), then \( \det\L_0 > 0 \). Justify your answer.
:::
:::

::: {.solution}
(a) With \( \N \) the incidence matrix of any orientation, \( \L = \N\N\tp \) (@def-graph-laplacian). By @prp-laplacian-basic (a), \( \L = \D - \A \), and the degree matrix and the adjacency matrix are determined by the graph alone.

(b) \( \x\tp\L\x = \sum_{e}(x_{u_e} - x_{v_e})^2 \), where \( u_e, v_e \) are the ends of \( e \) (@prp-laplacian-basic (b)). This is a sum of squares of real numbers, hence \( \ge 0 \), and \( \L \) is symmetric, so \( \L \succeq 0 \) by @def-positive-semidefinite.

(c) For a graph on \( m \ge 2 \) vertices with at least one edge, and any vertex \( r \), the matrix \( \L_0 \) obtained from \( \L \) by deleting the row and the column of \( r \) satisfies \( \det\L_0 = \) the number of spanning trees (@thm-matrix-tree). Multiple edges are allowed; loops are not, since edges join distinct vertices.

(d) True. By @thm-laplacian-kernel, \( \dim\nul(\L) = c \), the number of components, so @thm-rank-nullity-matrix gives \( \rank\L = m - c \); and \( c = 1 \) is connectedness.

(e) True. Multiplicity \( 1 \) means \( c = 1 \) by @thm-laplacian-kernel, so the graph is connected and has at least one spanning tree, and \( \det\L_0 \ge 1 \) by @thm-matrix-tree.
:::

### B. Practice

::: {#exr-graph-laplacians-b1}
[B1: The four-cycle]

Let \( C_4 \) be the graph on vertices \( 1, 2, 3, 4 \) with edges \( \{1,2\}, \{2,3\}, \{3,4\}, \{4,1\} \).

::: {.enumerate options="label=(\alph*)"}
1. Write down \( \L \) and explain why it is a circulant in the sense of @def-circulant.
2. Find all eigenvalues of \( \L \), the Fiedler value, and a Fiedler vector.
3. Compute \( \det\L_0 \) and list the spanning trees.
:::
:::

::: {.solution}
(a) Every vertex has degree \( 2 \), and the vertices \( u, v \) are joined exactly when \( v - u \equiv \pm1 \pmod 4 \). So, numbering rows and columns \( 0, 1, 2, 3 \) as in Chapter 11 §09, the \( (j,k) \)-entry depends only on \( k - j \) modulo \( 4 \), which is @def-circulant; the first row is \( \c = (2, -1, 0, -1) \) and
\[
\L = \begin{pmatrix} 2 & -1 & 0 & -1 \\ -1 & 2 & -1 & 0 \\ 0 & -1 & 2 & -1 \\ -1 & 0 & -1 & 2 \end{pmatrix}.
\]

(b) By @thm-circulant-diagonalization the eigenvalues are \( p_{\c}(\omega^j) \) for \( \omega = i \), with \( p_{\c}(x) = 2 - x - x^3 \). These were computed in @exr-circulants-and-the-dft-b1 (c): \( p_{\c}(1) = 0 \), \( p_{\c}(i) = 2 \), \( p_{\c}(-1) = 4 \), \( p_{\c}(-i) = 2 \). In increasing order the eigenvalues are \( 0, 2, 2, 4 \), so the Fiedler value is \( \mu_2(\L) = 2 \). A real eigenvector for \( 2 \) is twice the real part of the Fourier vector \( \f_1 = \tfrac12(1, i, -1, -i) \), namely \( (1, 0, -1, 0) \); it is orthogonal to \( \1 \), and \( \L(1,0,-1,0) = (2, 0, -2, 0) \), confirming the eigenvalue. So \( (1,0,-1,0) \) is a Fiedler vector, splitting the cycle as \( \{1\} \mid \{3\} \) with \( 2 \) and \( 4 \) undecided.

(c) Deleting the row and column of vertex \( 4 \),
\[
\det\L_0 = \det\begin{pmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2\end{pmatrix} = 2(4-1) + 1(-2 - 0) = 4 .
\]
Directly: a spanning tree has \( 3 \) edges, and the only \( 3 \)-edge subsets that are not spanning trees would have to contain a cycle; the only cycle is all four edges, so every one of the \( \binom43 = 4 \) three-edge subsets is a spanning tree. Both counts give \( 4 \).
:::

::: {#exr-graph-laplacians-b2}
[B2: Counting trees in a bowtie]

Let \( G \) have vertices \( 1, \dots, 5 \) and edges \( \{1,2\}, \{1,3\}, \{2,3\}, \{3,4\}, \{3,5\}, \{4,5\} \): two triangles sharing the vertex \( 3 \).

::: {.enumerate options="label=(\alph*)"}
1. Write down \( \L \) and compute \( \det\L_0 \) with \( r = 1 \).
2. Count the spanning trees directly, and check that the two answers agree.
3. Verify that \( \x = (1,1,0,-1,-1) \) is an eigenvector of \( \L \), and say what its eigenvalue tells you.
:::
:::

::: {.solution}
(a) The degrees are \( 2, 2, 4, 2, 2 \), so
\[
\L = \begin{pmatrix}
2 & -1 & -1 & 0 & 0 \\
-1 & 2 & -1 & 0 & 0 \\
-1 & -1 & 4 & -1 & -1 \\
0 & 0 & -1 & 2 & -1 \\
0 & 0 & -1 & -1 & 2
\end{pmatrix},
\qquad
\L_0 = \begin{pmatrix}
2 & -1 & 0 & 0 \\
-1 & 4 & -1 & -1 \\
0 & -1 & 2 & -1 \\
0 & -1 & -1 & 2
\end{pmatrix}.
\]
Expanding \( \det\L_0 \) along the first row: \( 2\det\left(\begin{smallmatrix} 4&-1&-1\\-1&2&-1\\-1&-1&2\end{smallmatrix}\right) + 1\cdot\det\left(\begin{smallmatrix}-1&-1&-1\\0&2&-1\\0&-1&2\end{smallmatrix}\right) \). The first \( 3 \times 3 \) determinant is \( 4(4-1) + 1(-2-1) - 1(1+2) = 12 - 3 - 3 = 6 \), and the second is \( -1(4-1) = -3 \). So \( \det\L_0 = 12 - 3 = 9 \).

(b) Removing the vertex \( 3 \) separates the graph into the two triangles, and a set of edges is a spanning tree exactly when it meets each triangle in a spanning tree of that triangle: the two triangles share only the vertex \( 3 \), so no cycle can use edges from both, and connectedness of the whole is connectedness of each half through \( 3 \). Each triangle has \( 3 \) spanning trees, namely its \( 3 \) pairs of edges. Hence there are \( 3 \times 3 = 9 \) spanning trees, agreeing with (a).

(c) \( \L\x \) has entries \( 2 - 1 - 0 = 1 \), \( -1 + 2 - 0 = 1 \), \( -1 - 1 + 0 + 1 + 1 = 0 \), \( 0 - 2 + 1 = -1 \), \( 0 + 1 - 2 = -1 \), so \( \L\x = \x \) and the eigenvalue is \( 1 \). Since \( \x\tp\1 = 0 \), @prp-fiedler-minimum gives \( \mu_2(\L) \le R_{\L}(\x) = 1 \). The Fiedler value is therefore at most \( 1 \), much smaller than the value \( 5 \) for the complete graph \( K_5 \), computed after @def-fiedler-value, and the sign pattern of \( \x \) proposes the partition \( \{1,2\} \mid \{4,5\} \) with the shared vertex \( 3 \) sitting on the fence: the graph is nearly two pieces.
:::

::: {#exr-graph-laplacians-b3}
[B3: Which minors are \( \pm 1 \)?]

Let \( G \) be the graph on vertices \( 1, 2, 3 \) with edges \( e_1 = \{1,2\} \), \( e_2 = \{2,3\} \), \( e_3 = \{1,3\} \), \( e_4 = \{1,2\} \) (so \( e_1 \) and \( e_4 \) are parallel). Orient every edge from the smaller vertex to the larger, let \( r = 3 \) and \( I = \{1,2\} \).

::: {.enumerate options="label=(\alph*)"}
1. Write down \( \N \) and \( \N_0 = \N_{I,[4]} \).
2. Compute \( \det\N_{I,S} \) for all six sets \( S \) of two edges, and say in each case whether \( S \) is a spanning tree.
3. Hence find the number of spanning trees, and check it against \( \det\L_0 \).
:::
:::

::: {.solution}
(a) Column \( e \) has \( 1 \) at the tail and \( -1 \) at the head:
\[
\N = \begin{pmatrix} 1 & 0 & 1 & 1 \\ -1 & 1 & 0 & -1 \\ 0 & -1 & -1 & 0\end{pmatrix},
\qquad
\N_0 = \begin{pmatrix} 1 & 0 & 1 & 1 \\ -1 & 1 & 0 & -1 \end{pmatrix}.
\]

(b) Taking the two columns in increasing order each time,
\[
\begin{aligned}
\{e_1,e_2\}&: \det\begin{pmatrix} 1&0\\-1&1\end{pmatrix} = 1, &
\{e_1,e_3\}&: \det\begin{pmatrix} 1&1\\-1&0\end{pmatrix} = 1, \\
\{e_1,e_4\}&: \det\begin{pmatrix} 1&1\\-1&-1\end{pmatrix} = 0, &
\{e_2,e_3\}&: \det\begin{pmatrix} 0&1\\1&0\end{pmatrix} = -1, \\
\{e_2,e_4\}&: \det\begin{pmatrix} 0&1\\1&-1\end{pmatrix} = -1, &
\{e_3,e_4\}&: \det\begin{pmatrix} 1&1\\0&-1\end{pmatrix} = -1 .
\end{aligned}
\]
Five of the six are \( \pm1 \) and those five sets are spanning trees: each is a pair of edges covering all three vertices with no cycle. The exception is \( \{e_1, e_4\} \), a cycle of length \( 2 \) formed by the parallel pair, which misses the vertex \( 3 \) entirely; its minor is \( 0 \), as @lem-incidence-minors-unimodular (c) predicts.

(c) So there are \( 5 \) spanning trees. The degrees are \( \deg(1) = 3 \), \( \deg(2) = 3 \), \( \deg(3) = 2 \), and \( a_{12} = 2 \), \( a_{13} = a_{23} = 1 \), so
\[
\L = \begin{pmatrix} 3 & -2 & -1 \\ -2 & 3 & -1 \\ -1 & -1 & 2\end{pmatrix},
\qquad
\det\L_0 = \det\begin{pmatrix} 3 & -2 \\ -2 & 3\end{pmatrix} = 9 - 4 = 5 .
\]
The two answers agree.
:::

### C. Going deeper

::: {#exr-graph-laplacians-c1}
[C1: Cayley's formula]

Let \( K_m \) be the complete graph on \( m \ge 2 \) vertices, in which every pair of distinct vertices is joined by exactly one edge, and let \( \J_t \in M_t(\nR) \) be the all-ones matrix.

::: {.enumerate options="label=(\alph*)"}
1. Show that the Laplacian of \( K_m \) is \( m\I_m - \J_m \), and that \( \L_0 = m\I_{m-1} - \J_{m-1} \) for every choice of deleted vertex.
2. Prove that \( \det(m\I_{m-1} - \J_{m-1}) = m^{m-2} \).
3. Deduce **Cayley's formula**: \( K_m \) has exactly \( m^{m-2} \) spanning trees. Check it for \( m = 2, 3, 4 \) against a direct count.
:::

*Hint for (b): the eigenvalues of \( \J_t \) are visible from its rank and its row sums.*
:::

::: {.solution}
(a) Every vertex of \( K_m \) has degree \( m-1 \) and \( a_{uv} = 1 \) for \( u \ne v \), so by @prp-laplacian-basic (a),
\[
\L = (m-1)\I_m - (\J_m - \I_m) = m\I_m - \J_m .
\]
Deleting the row and column of any one vertex from \( m\I_m - \J_m \) leaves \( m\I_{m-1} - \J_{m-1} \), since the pattern of entries is the same at every vertex.

(b) Put \( t = m-1 \). The matrix \( \J_t \) is symmetric with every row equal to \( \1\tp \), so \( \rank\J_t = 1 \) and \( \dim\nul(\J_t) = t - 1 \) by @thm-rank-nullity-matrix; hence \( 0 \) is an eigenvalue of multiplicity at least \( t-1 \). Also \( \J_t\1 = t\1 \), so \( t \) is an eigenvalue. That accounts for \( t \) eigenvalues, so the eigenvalue list of \( \J_t \) is \( t, 0, \dots, 0 \). Therefore \( m\I_t - \J_t \) has eigenvalues \( m - t = 1 \) once and \( m \) with multiplicity \( t - 1 \), and since \( \J_t \) is symmetric it is diagonalizable (@cor-spectral-real-matrix), so
\[
\det(m\I_t - \J_t) = 1 \cdot m^{t-1} = m^{m-2} .
\]

(c) By @thm-matrix-tree and parts (a), (b), the number of spanning trees of \( K_m \) is \( \det\L_0 = m^{m-2} \). For \( m = 2 \): \( 2^0 = 1 \), and indeed the single edge is the only spanning tree. For \( m = 3 \): \( 3^1 = 3 \), and the triangle's spanning trees are its three pairs of edges. For \( m = 4 \): \( 4^2 = 16 \); directly, \( K_4 \) has \( \binom{6}{3} = 20 \) sets of three edges, of which the \( 4 \) triangles are the only ones containing a cycle, leaving \( 20 - 4 = 16 \).
:::

::: {#exr-graph-laplacians-c2}
[C2: Weighted graphs]

Give each edge \( e \) of a graph \( G \) on \( m \ge 2 \) vertices a weight \( w_e > 0 \), let \( \W = \diag(w_1, \dots, w_k) \), and define the **weighted Laplacian** \( \L^{\w} \coloneqq \N\W\N\tp \), with \( \N \) the incidence matrix of any orientation.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \x\tp\L^{\w}\x = \sum_{e} w_e (x_{u_e} - x_{v_e})^2 \), and deduce that \( \L^{\w} \succeq 0 \) with the same kernel as \( \L \).
2. Prove the weighted matrix-tree theorem: for any vertex \( r \),
   \[
   \det\L^{\w}_0 = \sum_{T} \ \prod_{e \in T} w_e ,
   \]
   the sum running over all spanning trees \( T \) of \( G \).
3. Check (b) on the graph of @exm-laplacian-two-ways by comparing the coefficient of \( w_1w_2w_3 \) on both sides, and confirm that setting every \( w_e = 1 \) recovers @thm-matrix-tree.
:::

*Hint for (b): \( \N\W\N\tp = (\N\W^{1/2})(\N\W^{1/2})\tp \).*
:::

::: {.solution}
(a) Let \( \W^{1/2} = \diag(\sqrt{w_1}, \dots, \sqrt{w_k}) \), so \( \W = \W^{1/2}\W^{1/2} \) and \( \W^{1/2} \) is symmetric. Put \( \M = \N\W^{1/2} \). Then \( \L^{\w} = \M\M\tp \) and, as in @prp-laplacian-basic (b),
\[
\x\tp\L^{\w}\x = \norm{\M\tp\x}^2 = \sum_{e} w_e\bigl(x_{u_e} - x_{v_e}\bigr)^2 ,
\]
since entry \( e \) of \( \M\tp\x = \W^{1/2}\N\tp\x \) is \( \sqrt{w_e} \) times entry \( e \) of \( \N\tp\x \). The matrix is symmetric because \( (\M\M\tp)\tp = \M\M\tp \), and the sum is \( \ge 0 \), so \( \L^{\w} \succeq 0 \). As in Steps 1 and 2 of the proof of @thm-laplacian-kernel, \( \x \in \nul(\L^{\w}) \) if and only if this sum vanishes; every \( w_e \) is **strictly** positive, so the sum vanishes exactly when every difference \( x_{u_e} - x_{v_e} \) does, which is the same condition as for \( \L \). Hence the kernels agree.

(b) With \( \M = \N\W^{1/2} \) as above and \( I = [m]\setminus\{r\} \), the argument of Step 1 of @thm-matrix-tree gives \( \L^{\w}_0 = \M_0\M_0\tp \) with \( \M_0 = \M_{I,[k]} \). By @cor-gram-determinant-nonnegative,
\[
\det\L^{\w}_0 = \sum_{\lvert S\rvert = m-1} \bigl(\det\M_{I,S}\bigr)^2 .
\]
Multiplying \( \N \) on the right by the diagonal matrix \( \W^{1/2} \) scales column \( e \) by \( \sqrt{w_e} \), so \( \M_{I,S} = \N_{I,S}\,\W^{1/2}_{S,S} \) and, by @thm-det-multiplicative and @thm-det-triangular,
\[
\bigl(\det\M_{I,S}\bigr)^2 = \bigl(\det\N_{I,S}\bigr)^2 \prod_{e \in S} w_e .
\]
By @lem-incidence-minors-unimodular (c) the first factor is \( 1 \) when \( S \) is a spanning tree and \( 0 \) otherwise, and by @prp-spanning-tree-size every spanning tree has \( m-1 \) edges and so occurs among the sets \( S \), once. This gives the formula.

(c) For that graph, with \( r = 4 \) and the edge numbering \( e_1 = \{1,2\} \), \( e_2 = \{2,3\} \), \( e_3 = \{3,4\} \), \( e_4 = \{4,1\} \), \( e_5 = \{1,3\} \),
\[
\L^{\w}_0 = \begin{pmatrix}
w_1 + w_4 + w_5 & -w_1 & -w_5 \\
-w_1 & w_1 + w_2 & -w_2 \\
-w_5 & -w_2 & w_2 + w_3 + w_5
\end{pmatrix}.
\]
The weight \( w_3 \) occurs only in the \( (3,3) \)-entry, so in the Leibniz expansion (@def-determinant) only the two permutations fixing \( 3 \) can produce a term containing \( w_3 \): the identity, contributing \( (w_1+w_4+w_5)(w_1+w_2)(w_2+w_3+w_5) \), and the transposition of \( 1 \) and \( 2 \), contributing \( -(-w_1)(-w_1)(w_2+w_3+w_5) \), every term of which carries a factor \( w_1^2 \). So the coefficient of \( w_1w_2w_3 \) comes from the diagonal product alone, and there it is \( 1 \). On the right, a spanning tree \( T \) contributes the single monomial \( \prod_{e\in T}w_e \), and \( T \) is recovered from that monomial, so the coefficient of \( w_1w_2w_3 \) is \( 1 \) if \( \{e_1,e_2,e_3\} \) is a spanning tree and \( 0 \) otherwise; it is one, as @exm-matrix-tree-four-vertices records. Setting every \( w_e = 1 \) gives \( \W = \I \), hence \( \L^{\w} = \L \), and the right-hand side becomes the number of spanning trees: @thm-matrix-tree.
:::
