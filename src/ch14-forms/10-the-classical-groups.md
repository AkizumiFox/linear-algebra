# Groups Defined by Forms

Chapter 11 defined the orthogonal and unitary groups by a sentence: they consist of the operators that preserve the inner product. Read that sentence again and notice that positivity never appears in it. "Preserves \( \inner{\cdot}{\cdot} \)" makes sense for any bilinear or Hermitian form at all, and it always produces a group. This section takes the definition apart and puts it back together over an arbitrary form, so that the four families of **classical groups** — orthogonal, indefinite orthogonal, unitary, symplectic — become four instances of one construction, chosen by the four kinds of form this chapter has classified.

Everything is recalled, not reproved. \( \Orth(n) \), \( \SO(n) \) and \( \Unit(n) \) were defined in Chapter 11 (@def-unitary-orthogonal, @def-unitary-orthogonal-groups), shown there to be groups with the expected determinants (@prp-orthogonal-group-properties), and classified element by element in the real case in Chapter 12 (@thm-orthogonal-canonical-form). None of that is repeated. What is new here is the pattern behind it.

## The isometry group of a form

An operator preserves a form when applying it to both arguments changes nothing. This is the same idea as an isometry of an inner product space (@def-isometry), with the norm removed from the statement because a general form has no norm.

*The isometry group of a form is the set of invertible changes of coordinates that the form cannot detect.*

::: {#def-isometry-group-of-form}
[Isometry Group of a Form]

Let \( V \) be a finite-dimensional vector space over \( F \) and \( \beta \) a **non-degenerate** bilinear form on \( V \) (@def-nondegenerate). An operator \( T \in \cL(V) \) is an **isometry of \( \beta \)** if
\[
\beta(T\u, T\v) = \beta(\u, \v) \qquad \text{for all } \u, \v \in V ,
\]
and the set of all of them is written \( \operatorname{Isom}(\beta) \).

For a **non-singular** \( \A \in M_n(F) \), the corresponding matrix group is
\[
\operatorname{Isom}(\A) \coloneqq \{\, \P \in M_n(F) : \P\tp\A\P = \A \,\} .
\]
When \( F = \nC \) and \( \A^{*} = \A \) is non-singular Hermitian, \( \operatorname{Isom}(\A) \) means instead \( \{\, \P : \P^{*}\A\P = \A \,\} \).
:::

Read the clauses. The condition is required **for all** pairs, not just for a basis — though checking it on a basis is enough, since both sides are bilinear in \( \u \) and in \( \v \). The matrix condition \( \P\tp\A\P = \A \) is the matrix condition of @thm-change-of-basis-form with the new Gram matrix required to be the *old* one: an isometry is a change of basis that leaves the Gram matrix alone. And the two versions match, because if \( \A = \mtx{\beta}{\sB}{\sB} \) then \( T \in \operatorname{Isom}(\beta) \) if and only if \( \mtx{T}{\sB}{\sB} \in \operatorname{Isom}(\A) \), by @thm-form-matrix-determines (a) applied twice.

Two clauses need defending. First, **non-degeneracy**. Without it the definition is worthless: for \( \A = \0 \) the condition \( \P\tp\0\P = \0 \) holds for every \( \P \), including \( \P = \0 \), and the "group" is all of \( M_n(F) \), which has no inverses. Second, the definition does **not** require \( \P \) to be invertible. It does not have to: invertibility comes free, as the next result records, and this is exactly what non-degeneracy buys.

::: {#thm-classical-groups-are-groups}
[Isometry Groups Are Groups]

Let \( \A \in M_n(F) \) be non-singular. Then every \( \P \in \operatorname{Isom}(\A) \) is invertible, and \( \operatorname{Isom}(\A) \) is a subgroup of \( \GL_n(F) \). The same holds for \( \operatorname{Isom}(\beta) \) inside the group of invertible operators on \( V \), and for the Hermitian version.
:::

::: {.proof}
Let \( \P \in \operatorname{Isom}(\A) \). Taking determinants in \( \P\tp\A\P = \A \) and using @thm-det-multiplicative and @thm-det-transpose,
\[
(\det\P)^2\det\A = \det\A .
\]
Since \( \A \) is non-singular, \( \det\A \ne 0 \) (@thm-det-nonzero-iff-invertible), and canceling it in the field \( F \) gives \( (\det\P)^2 = 1 \). Hence \( \det\P \ne 0 \) and \( \P \) is invertible, again by @thm-det-nonzero-iff-invertible.

Now the three subgroup checks. \( \I_n\tp\A\I_n = \A \), so \( \I_n \in \operatorname{Isom}(\A) \). If \( \P, \Q \in \operatorname{Isom}(\A) \) then
\[
(\P\Q)\tp\A(\P\Q) = \Q\tp(\P\tp\A\P)\Q = \Q\tp\A\Q = \A ,
\]
using @thm-transpose-properties for the first equality, so \( \P\Q \in \operatorname{Isom}(\A) \). And if \( \P \in \operatorname{Isom}(\A) \), multiply \( \P\tp\A\P = \A \) on the left by \( (\P\tp)^{-1} = (\P^{-1})\tp \) and on the right by \( \P^{-1} \), which is legitimate because \( \P \) is invertible; this gives \( \A = (\P^{-1})\tp\A\P^{-1} \), so \( \P^{-1} \in \operatorname{Isom}(\A) \). Associativity is inherited from \( M_n(F) \).

For the Hermitian version replace \( \tp \) by \( {}^{*} \) throughout; the determinant step becomes \( \conj{\det\P}\det\P\,\det\A = \det\A \), that is \( \lvert\det\P\rvert^2 = 1 \), which again forces \( \det\P \ne 0 \). The operator version is the matrix version read through a basis. This proves the theorem.
:::

The proof is the one Chapter 11 gave for \( \Orth(n) \) and \( \Unit(n) \) in @prp-orthogonal-group-properties (a), with \( \I_n \) replaced by \( \A \); nothing in it used what \( \A \) was, only that it was non-singular. That is the whole point of the section: the group structure never depended on positivity, on symmetry, or on the field.

## Congruent forms give conjugate groups

Before listing the families, one observation makes the list a classification rather than a list of unrelated examples. Congruent matrices have the "same" isometry group, in the strongest sense available.

::: {#prp-congruent-forms-conjugate-groups}
[Congruence Conjugates the Isometry Group]

Let \( \A, \B \in M_n(F) \) be non-singular with \( \B = \Q\tp\A\Q \) for an invertible \( \Q \) (@def-congruent). Then
\[
\operatorname{Isom}(\B) = \Q^{-1}\operatorname{Isom}(\A)\,\Q ,
\]
so the two groups are conjugate subgroups of \( \GL_n(F) \); in particular they are isomorphic as groups, by \( \P \mapsto \Q\P\Q^{-1} \).
:::

::: {.proof}
Let \( \P \in M_n(F) \). Substituting \( \B = \Q\tp\A\Q \) and writing \( \R = \Q\P\Q^{-1} \),
\[
\begin{aligned}
\P\tp\B\P = \B
&\iff \P\tp\Q\tp\A\Q\P = \Q\tp\A\Q \\
&\iff (\Q\P\Q^{-1})\tp\A(\Q\P\Q^{-1}) = \A ,
\end{aligned}
\]
where the second step multiplies on the left by \( (\Q\tp)^{-1} \) and on the right by \( \Q^{-1} \) and uses @thm-transpose-properties; both operations are reversible because \( \Q \) is invertible. So \( \P \in \operatorname{Isom}(\B) \) if and only if \( \R = \Q\P\Q^{-1} \in \operatorname{Isom}(\A) \), which is the claimed equality of sets. Conjugation by \( \Q \) is an isomorphism of groups, being a bijection that respects products.
:::

So the isometry group depends only on the congruence class of the form, and this chapter has already listed the congruence classes. Over \( \nR \), @cor-real-symmetric-classification says a non-degenerate symmetric form is congruent to exactly one \( \I_{n_+}\oplus(-\I_{n_-}) \); over \( \nC \), @cor-complex-symmetric-classification says a non-degenerate symmetric form is congruent to \( \I_n \) and nothing else; and @thm-symplectic-standard-form says a symplectic form is congruent to \( \vOmega_{2m} \) and nothing else. Each classification theorem of this chapter therefore doubles as a list of groups.

## The four families

::: {#def-classical-groups}
[The Indefinite Orthogonal and Symplectic Groups]

For \( p, q \ge 0 \) with \( p + q = n \), set \( \I_{p,q} \coloneqq \I_p \oplus (-\I_q) \in M_n(\nR) \) and
\[
\Orth(p, q) \coloneqq \operatorname{Isom}(\I_{p,q}) = \{\, \P \in M_n(\nR) : \P\tp\I_{p,q}\P = \I_{p,q} \,\} ,
\]
the **indefinite orthogonal group** of signature \( (p, q) \). For \( m \ge 1 \) and any field \( F \), set
\[
\Sp(2m, F) \coloneqq \operatorname{Isom}(\vOmega_{2m}) = \{\, \P \in M_{2m}(F) : \P\tp\vOmega_{2m}\P = \vOmega_{2m} \,\} ,
\]
the **symplectic group**, where \( \vOmega_{2m} \) is the standard alternating matrix of @eq-standard-alternating-matrix.
:::

With Chapter 11's groups recalled, the four families line up as four choices of form.

| Family | Form preserved | Kind of form | Section |
|---|---|---|---|
| \( \Orth(n) \) | \( \I_n \) over \( \nR \) | symmetric, positive definite | Ch 11 §07 |
| \( \Orth(p,q) \) | \( \I_{p,q} \) over \( \nR \) | symmetric, signature \( (p,q) \) | §05 |
| \( \Unit(n) \) | \( \I_n \) over \( \nC \) | Hermitian, positive definite | Ch 11 §07 |
| \( \Sp(2m, F) \) | \( \vOmega_{2m} \) over \( F \) | alternating, non-degenerate | §09 |

Two remarks on the list. \( \Orth(n) = \Orth(n, 0) \), so the ordinary orthogonal group is the extreme case of the indefinite one; and \( \Orth(p,q) \) and \( \Orth(q,p) \) are conjugate, because negating a form does not change which maps preserve it, and \( -\I_{p,q} = (-\I_p)\oplus\I_q \) becomes \( \I_{q,p} \) after a permutation of the coordinates, which is a congruence. There is no \( \Sp \) for odd size: a non-degenerate alternating form exists only in even dimension (@thm-symplectic-standard-form (b)).

::: {#exm-elements-of-the-classical-groups}
[Members of Each Family]

Verify the following memberships, with \( \vOmega_{2m} \) as above.

::: {.enumerate options="label=(\alph*)"}
1. \( \begin{psmallmatrix} \cosh t & \sinh t \\ \sinh t & \cosh t\end{psmallmatrix} \in \Orth(1,1) \) for every \( t \in \nR \).
2. \( \begin{psmallmatrix} \M & \0 \\ \0 & (\M\tp)^{-1}\end{psmallmatrix} \in \Sp(2m, F) \) for every invertible \( \M \in M_m(F) \).
3. \( \begin{psmallmatrix} \I_m & \S \\ \0 & \I_m\end{psmallmatrix} \in \Sp(2m, F) \) if and only if \( \S\tp = \S \).
:::
:::

::: {.solution}
(a) With \( \A = \I_{1,1} = \diag(1,-1) \), \( c = \cosh t \) and \( s = \sinh t \),
\[
\begin{pmatrix} c & s \\ s & c\end{pmatrix}
\begin{pmatrix} 1 & 0 \\ 0 & -1\end{pmatrix}
\begin{pmatrix} c & s \\ s & c\end{pmatrix}
= \begin{pmatrix} c^2 - s^2 & 0 \\ 0 & s^2 - c^2 \end{pmatrix}
= \I_{1,1},
\]
using \( \cosh^2 t - \sinh^2 t = 1 \) and the symmetry of the outer matrix.

(b) Write \( \P = \M \oplus \N \) with \( \N = (\M\tp)^{-1} \). Multiplying the blocks,
\[
\P\tp\vOmega_{2m}\P
= \begin{pmatrix} \M\tp & \0 \\ \0 & \N\tp \end{pmatrix}
\begin{pmatrix} \0 & \N \\ -\M & \0 \end{pmatrix}
= \begin{pmatrix} \0 & \M\tp\N \\ -\N\tp\M & \0 \end{pmatrix},
\]
which equals \( \vOmega_{2m} \) exactly when \( \M\tp\N = \I_m \), that is \( \N = (\M\tp)^{-1} \).

(c) With \( \P = \begin{psmallmatrix} \I_m & \S \\ \0 & \I_m\end{psmallmatrix} \),
\[
\P\tp\vOmega_{2m}\P
= \begin{pmatrix} \I_m & \0 \\ \S\tp & \I_m \end{pmatrix}
\begin{pmatrix} \0 & \I_m \\ -\I_m & -\S \end{pmatrix}
= \begin{pmatrix} \0 & \I_m \\ -\I_m & \S\tp - \S \end{pmatrix} ,
\]
which equals \( \vOmega_{2m} \) exactly when \( \S\tp = \S \). Such a \( \P \) is a **symplectic shear**; part (c) is the first sign that symmetric matrices appear inside the symplectic group, and the dimension count below will make that precise.
:::

## Determinants

For the orthogonal family the determinant argument is already inside the proof of @thm-classical-groups-are-groups, and it costs nothing to state it over any field.

::: {#thm-classical-group-determinants}
[Determinants in the Classical Groups]

::: {.enumerate options="label=(\alph*)"}
1. Let \( F \) be any field and \( \A \in M_n(F) \) non-singular. Then \( \det\P = \pm 1 \) for every \( \P \in \operatorname{Isom}(\A) \). In particular \( \det\P = \pm 1 \) for \( \P \in \Orth(p,q) \), and both signs occur when \( n \ge 1 \).
2. If \( \A \in M_n(\nC) \) is Hermitian and non-singular, then \( \lvert\det\P\rvert = 1 \) for every \( \P \in \operatorname{Isom}(\A) \); in particular for \( \P \in \Unit(n) \).
3. \( \Sp(2, F) = \SL_2(F) \). In particular every \( \P \in \Sp(2,F) \) has \( \det\P = 1 \) exactly, and \( -1 \) does not occur.
:::
:::

::: {.proof}
(a) The proof of @thm-classical-groups-are-groups established \( (\det\P)^2 = 1 \). The polynomial \( x^2 - 1 = (x-1)(x+1) \) has at most two roots in a field (@cor-root-bound-general), and \( 1 \) and \( -1 \) are roots, so \( \det\P \in \{1, -1\} \). For \( \Orth(p,q) \), the identity has determinant \( 1 \); and \( \D \coloneqq \diag(-1, 1, \dots, 1) \) satisfies \( \D\tp\I_{p,q}\D = \I_{p,q} \), since \( \D \) is diagonal and squaring its entries gives \( \I_n \), while \( \det\D = -1 \).

(b) Also established in that proof: \( \lvert\det\P\rvert^2 = 1 \), and a non-negative real with square \( 1 \) is \( 1 \). This is @prp-orthogonal-group-properties (b) for \( \A = \I_n \).

(c) Write \( \J = \vOmega_2 = \begin{psmallmatrix} 0 & 1 \\ -1 & 0 \end{psmallmatrix} \) and let \( \P = \begin{psmallmatrix} a & b \\ c & d\end{psmallmatrix} \) be arbitrary. Multiplying out,
\[
\P\tp\J\P
= \begin{pmatrix} a & c \\ b & d \end{pmatrix}\begin{pmatrix} c & d \\ -a & -b \end{pmatrix}
= \begin{pmatrix} 0 & ad - bc \\ bc - ad & 0 \end{pmatrix}
= (\det\P)\,\J .
\]
Since \( \J \ne \0 \), the equation \( \P\tp\J\P = \J \) holds if and only if \( \det\P = 1 \). This proves the theorem.
:::

::: {.warning}
**Every symplectic matrix has determinant \( +1 \), not \( \pm 1 \).** The general argument of part (a) applies to \( \vOmega_{2m} \) as well and gives only \( (\det\P)^2 = 1 \), so it leaves \( -1 \) open. It is nevertheless true that \( \Sp(2m, F) \subseteq \SL_{2m}(F) \) for every \( m \), so \( -1 \) never occurs. Part (c) proves this for \( m = 1 \); **the general case is not proved in this book.** The clean route runs through the Pfaffian of Section 9 and its transformation rule \( \operatorname{Pf}(\P\tp\A\P) = \det(\P)\operatorname{Pf}(\A) \): applied to \( \A = \vOmega_{2m} \), whose Pfaffian is \( 1 \), it turns \( \P\tp\vOmega_{2m}\P = \vOmega_{2m} \) directly into \( \det\P = 1 \). We stated that rule without proof, so we state its consequence without proof too. Do not use the statement as a step in an argument elsewhere in this book; treat it as information about the wider subject, like the fact that the general polynomial of degree five has no solution by radicals.
:::

There is a consequence worth noticing. \( \Orth(n) \) has the proper subgroup \( \SO(n) \) cut out by \( \det = 1 \), and Chapter 12 made heavy use of it: rotations against reflections. The symplectic group has no such subgroup, because — by the fact just recorded, which this book does not prove — the determinant condition is already satisfied by everything in it. A symplectic form has no notion of reflection to detect.

## Counting parameters

How big is each group? "Big" has an honest answer in this book only as a count, so here is the count, and here is what it does and does not mean.

The equation \( \P\tp\A\P = \A \) is a system of scalar equations in the \( n^2 \) unknown entries of \( \P \). If the system consisted of \( k \) independent equations we would expect the solutions to form a family described by \( n^2 - k \) free parameters, and that number is what everybody calls the **dimension** of the group. The key observation is that the \( n^2 \) equations are far from independent, because the matrix \( \P\tp\A\P - \A \) is not an arbitrary matrix: it has the same symmetry type as \( \A \), by @prp-congruence-preserves-symmetry. So the equations repeat, and only the independent ones should be counted.

- If \( \A \) is **symmetric**, then \( \P\tp\A\P - \A \) is symmetric, and a symmetric \( n \times n \) matrix has \( \tfrac12 n(n+1) \) independent entries. Expected dimension: \( n^2 - \tfrac12 n(n+1) = \tfrac12 n(n-1) \).
- If \( \A \) is **alternating**, then \( \P\tp\A\P - \A \) is alternating, and an alternating \( n\times n \) matrix has \( \tfrac12 n(n-1) \) independent entries. Expected dimension: \( n^2 - \tfrac12 n(n-1) = \tfrac12 n(n+1) \).
- If \( \A \) is **Hermitian** over \( \nC \), count real parameters: \( \P \) has \( 2n^2 \) of them, and a Hermitian matrix has \( n \) real diagonal entries and \( \tfrac12 n(n-1) \) complex entries above the diagonal, in total \( n^2 \) real conditions. Expected real dimension: \( 2n^2 - n^2 = n^2 \).

| Group | Entries in \( \P \) | Independent conditions | Dimension |
|---|---|---|---|
| \( \Orth(n) \), \( \Orth(p,q) \), \( p+q = n \) | \( n^2 \) | \( \tfrac12 n(n+1) \) | \( \tfrac12 n(n-1) \) |
| \( \Unit(n) \) (real parameters) | \( 2n^2 \) | \( n^2 \) | \( n^2 \) |
| \( \Sp(2m, \nR) \) | \( 4m^2 \) | \( m(2m-1) \) | \( m(2m+1) \) |

Small cases are a sanity check. \( \Orth(2) \) comes out at dimension \( 1 \), and Chapter 11 found that its elements are described by a single angle. \( \Orth(3) \) comes out at \( 3 \), matching the axis-and-angle description of @cor-so3-is-rotation: two parameters for the axis direction, one for the angle. \( \Unit(1) \) comes out at \( 1 \), and \( \Unit(1) \) is the unit circle in \( \nC \). And \( \Sp(2,\nR) = \SL_2(\nR) \) comes out at \( 3 \), which is right: four entries subject to the single equation \( ad - bc = 1 \).

Compare the orthogonal and symplectic rows of the table at \( n = 2m \). The orthogonal group is smaller than the symplectic group of the same size, by exactly \( \tfrac12 n(n+1) - \tfrac12 n(n-1) = n \). The gap is the gap between symmetric and alternating matrices, which is the \( n \) diagonal entries — the same diagonal that Section 3 found separating the two notions in the first place.

::: {.warning}
**This count is a heuristic, not a theorem of this book.** "Dimension" here means the number of free parameters one expects a solution set to have, and the step from "\( k \) independent-looking equations" to "\( n^2 - k \) parameters" is not justified by anything proved above; for a non-linear system it can fail. Making it precise requires the notion of a smooth manifold and the implicit function theorem, which belong to analysis and differential geometry, not here. What is proved here is only the count of conditions. Every number in the table is nevertheless correct.
:::

::: {.check}
The family \( \Orth(p,q) \) is indexed by two integers, yet the table gives it a dimension depending only on \( n = p + q \), not on how \( n \) splits. Does that mean \( \Orth(3,0) \) and \( \Orth(2,1) \) are the same group?
:::

::: {.solution}
No. The count of conditions only sees that \( \I_{p,q} \) is symmetric, not which symmetric matrix it is, so it cannot distinguish the two. They are genuinely different groups: \( \Orth(3) = \Orth(3,0) \) consists of matrices all of whose entries have absolute value at most \( 1 \), since its columns are unit vectors, whereas \( \Orth(2,1) \) contains matrices with arbitrarily large entries, as the next warning shows. Conjugate groups come from **congruent** forms (@prp-congruent-forms-conjugate-groups), and \( \I_{3,0} \) and \( \I_{2,1} \) are not congruent, because their signatures differ (@cor-real-symmetric-classification).
:::

## Boundedness and its absence

::: {.warning}
**\( \Orth(p,q) \) is not compact when \( p, q \ge 1 \), unlike \( \Orth(n) \).** Compactness is a topological notion that this book does not develop, so the statement is **recorded here, not proved**. What can be seen without topology is the underlying reason, which is that the entries are unbounded. Take the hyperbolic plane \( \A = \begin{psmallmatrix} 0 & 1 \\ 1 & 0\end{psmallmatrix} \), a non-degenerate symmetric real form of signature \( (1,1) \), hence congruent to \( \I_{1,1} \). For every real \( t \ne 0 \),
\[
\begin{pmatrix} t & 0 \\ 0 & t^{-1}\end{pmatrix}\tp
\begin{pmatrix} 0 & 1 \\ 1 & 0\end{pmatrix}
\begin{pmatrix} t & 0 \\ 0 & t^{-1}\end{pmatrix}
= \begin{pmatrix} 0 & 1 \\ 1 & 0\end{pmatrix} ,
\]
so \( \diag(t, t^{-1}) \) lies in \( \operatorname{Isom}(\A) \), and its entries are unbounded as \( t \to \infty \). By @prp-congruent-forms-conjugate-groups the same unbounded family sits inside \( \Orth(1,1) \), and padding with an identity block puts it inside every \( \Orth(p,q) \) with \( p, q \ge 1 \). By contrast every entry of a matrix in \( \Orth(n) \) has absolute value at most \( 1 \), because each column is a unit vector for the Euclidean norm.
:::

The same phenomenon shows up in \( \Sp(2m,\nR) \), by @exm-elements-of-the-classical-groups (b) with \( \M = [t] \): the symplectic group is unbounded too. Only the two positive definite families, \( \Orth(n) \) and \( \Unit(n) \), are bounded, and positivity is exactly why — the form itself controls the size of the columns. Definiteness, which this chapter spent nine sections learning to do without, turns out to be what made Chapter 11's groups small.

Section 11 takes the indefinite case that physics uses, signature \( (1,3) \), and works out what its isometry group does to the geometry of spacetime.

## Exercises

### A. Check your understanding

::: {#exr-the-classical-groups-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define \( \operatorname{Isom}(\A) \) for a non-singular \( \A \in M_n(F) \), and explain why its elements are automatically invertible.
2. Which form does \( \Orth(p,q) \) preserve, and which does \( \Sp(2m,F) \) preserve?
3. Determine whether the following is correct: if \( \A \simeq \B \), then \( \operatorname{Isom}(\A) = \operatorname{Isom}(\B) \). Justify your answer.
4. State what is known here about \( \det\P \) for \( \P \in \Sp(2m,F) \), distinguishing what is proved from what is only recorded.
5. In the parameter count, what exactly does the word "dimension" mean, and what is not being claimed?
:::
:::

::: {.solution}
(a) \( \operatorname{Isom}(\A) = \{\P : \P\tp\A\P = \A\} \) (@def-isometry-group-of-form). Taking determinants gives \( (\det\P)^2\det\A = \det\A \), and \( \det\A \ne 0 \), so \( (\det\P)^2 = 1 \) and \( \det\P \ne 0 \) (@thm-classical-groups-are-groups).

(b) \( \Orth(p,q) \) preserves the real symmetric form with matrix \( \I_{p,q} = \I_p \oplus (-\I_q) \), of signature \( (p,q) \). \( \Sp(2m,F) \) preserves the standard alternating form with matrix \( \vOmega_{2m} \) (@def-classical-groups).

(c) Incorrect as stated: the two groups are **conjugate**, \( \operatorname{Isom}(\B) = \Q^{-1}\operatorname{Isom}(\A)\Q \), not equal (@prp-congruent-forms-conjugate-groups). For a witness take \( \A = \I_2 \) and \( \B = \diag(1,4) = \Q\tp\A\Q \) with \( \Q = \diag(1,2) \). Then \( \begin{psmallmatrix} 0 & 1 \\ -1 & 0\end{psmallmatrix} \in \Orth(2) = \operatorname{Isom}(\A) \), but the corresponding element \( \Q^{-1}\begin{psmallmatrix} 0 & 1 \\ -1 & 0\end{psmallmatrix}\Q = \begin{psmallmatrix} 0 & 2 \\ -1/2 & 0\end{psmallmatrix} \) of \( \operatorname{Isom}(\B) \) is not in \( \Orth(2) \). What is always true is that the two groups are isomorphic.

(d) Proved here: \( (\det\P)^2 = 1 \), hence \( \det\P = \pm 1 \), for every \( m \) (@thm-classical-group-determinants (a)); and \( \det\P = 1 \) exactly, for \( m = 1 \), since \( \Sp(2,F) = \SL_2(F) \) (part (c)). Recorded but not proved: \( \det\P = 1 \) for every \( m \), which follows from the transformation rule of the Pfaffian.

(e) The number of free parameters expected in the solution set of \( \P\tp\A\P = \A \), computed as \( n^2 \) minus the number of independent scalar conditions. It is not claimed that the solution set really is a family described by that many free parameters; that statement needs the implicit function theorem and is not proved here.
:::

### B. Practice

::: {#exr-the-classical-groups-b1}
[B1: Determine which of the following]

For each matrix, determine whether it lies in \( \Orth(2) \), in \( \Orth(1,1) \), in \( \Sp(2,\nR) \) — where the relevant forms are \( \I_2 \), \( \I_{1,1} = \diag(1,-1) \) and \( \vOmega_2 \) — listing all that apply. Justify each answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \begin{psmallmatrix} 1 & 0 \\ 0 & -1\end{psmallmatrix} \).
2. \( \begin{psmallmatrix} 0 & -1 \\ 1 & 0\end{psmallmatrix} \).
3. \( \begin{psmallmatrix} 3 & 0 \\ 0 & 1/3\end{psmallmatrix} \).
4. \( \begin{psmallmatrix} 5/3 & 4/3 \\ 4/3 & 5/3\end{psmallmatrix} \).
:::
:::

::: {.solution}
Throughout, membership in \( \Sp(2,\nR) \) is decided by \( \det\P = 1 \) alone (@thm-classical-group-determinants (c)), and membership in \( \Orth(2) \) by orthonormality of the columns.

(a) \( \Orth(2) \): yes, the columns are \( \e_1 \) and \( -\e_2 \), orthonormal. \( \Orth(1,1) \): yes, \( \P \) is diagonal with entries \( \pm 1 \), so \( \P\tp\I_{1,1}\P = \I_{1,1} \). \( \Sp(2,\nR) \): no, \( \det\P = -1 \).

(b) \( \Orth(2) \): yes, a rotation by \( \pi/2 \). \( \Orth(1,1) \): no — \( \P\tp\I_{1,1}\P = \begin{psmallmatrix} -1 & 0 \\ 0 & 1\end{psmallmatrix} = -\I_{1,1} \ne \I_{1,1} \). \( \Sp(2,\nR) \): yes, \( \det\P = 1 \).

(c) \( \Orth(2) \): no, the first column has norm \( 3 \). \( \Orth(1,1) \): no — for diagonal \( \P = \diag(s,t) \) the condition is \( \diag(s^2, -t^2) = \diag(1,-1) \), that is \( s, t = \pm 1 \), and \( 3 \ne \pm 1 \). \( \Sp(2,\nR) \): yes, \( \det\P = 3\cdot\tfrac13 = 1 \).

(d) \( \Orth(2) \): no, the first column has norm \( \sqrt{25/9 + 16/9} = \sqrt{41}/3 \ne 1 \). \( \Orth(1,1) \): yes — this is \( \begin{psmallmatrix} \cosh t & \sinh t \\ \sinh t & \cosh t \end{psmallmatrix} \) with \( \cosh t = 5/3 \), \( \sinh t = 4/3 \) and \( (5/3)^2 - (4/3)^2 = 1 \), so @exm-elements-of-the-classical-groups (a) applies. \( \Sp(2,\nR) \): yes, \( \det\P = 25/9 - 16/9 = 1 \).
:::

::: {#exr-the-classical-groups-b2}
[B2: A symplectic matrix of size four]

Let \( \M = \begin{psmallmatrix} 1 & 2 \\ 0 & 1\end{psmallmatrix} \) and \( \S = \begin{psmallmatrix} 0 & 1 \\ 1 & 0\end{psmallmatrix} \), and put
\[
\P_1 = \begin{pmatrix} \M & \0 \\ \0 & (\M\tp)^{-1}\end{pmatrix},
\qquad
\P_2 = \begin{pmatrix} \I_2 & \S \\ \0 & \I_2\end{pmatrix} .
\]

::: {.enumerate options="label=(\alph*)"}
1. Write out \( \P_1 \) explicitly and verify \( \P_1 \in \Sp(4, \nQ) \) directly from the definition.
2. Explain why \( \P_1\P_2 \in \Sp(4,\nQ) \) without computing the product.
3. Compute \( \det\P_1 \) and \( \det\P_2 \), and check them against @thm-classical-group-determinants.
:::
:::

::: {.solution}
(a) \( \M\tp = \begin{psmallmatrix} 1 & 0 \\ 2 & 1\end{psmallmatrix} \), so \( (\M\tp)^{-1} = \begin{psmallmatrix} 1 & 0 \\ -2 & 1\end{psmallmatrix} \) and
\[
\P_1 = \begin{pmatrix} 1 & 2 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & -2 & 1 \end{pmatrix}.
\]
By the block computation of @exm-elements-of-the-classical-groups (b), \( \P_1\tp\vOmega_4\P_1 = \begin{psmallmatrix} \0 & \M\tp\N \\ -\N\tp\M & \0\end{psmallmatrix} \) with \( \N = (\M\tp)^{-1} \), and \( \M\tp\N = \M\tp(\M\tp)^{-1} = \I_2 \). So \( \P_1\tp\vOmega_4\P_1 = \vOmega_4 \).

(b) \( \S \) is symmetric, so \( \P_2 \in \Sp(4,\nQ) \) by @exm-elements-of-the-classical-groups (c). A product of two elements of a group is again in the group, and \( \Sp(4,\nQ) \) is a group by @thm-classical-groups-are-groups.

(c) \( \P_1 = \M \oplus (\M\tp)^{-1} \) is block diagonal, so by @thm-det-block-triangular and @cor-det-inverse,
\[
\det\P_1 = \det\M\,\det\bigl((\M\tp)^{-1}\bigr) = \det\M\,(\det\M)^{-1} = 1 ,
\]
using \( \det\M\tp = \det\M \) (@thm-det-transpose). And \( \P_2 \) is block upper triangular with both diagonal blocks equal to \( \I_2 \), so \( \det\P_2 = 1 \) by @thm-det-block-triangular. Both equal \( +1 \), consistent with the recorded fact \( \Sp(2m,F) \subseteq \SL_{2m}(F) \); part (a) of the theorem only guarantees \( \pm 1 \).
:::

::: {#exr-the-classical-groups-b3}
[B3: Counting parameters]

::: {.enumerate options="label=(\alph*)"}
1. Compute the expected dimensions of \( \Orth(4) \), \( \Orth(2,2) \), \( \Unit(3) \) and \( \Sp(4,\nR) \).
2. For which \( n \) and \( m \) do \( \Orth(n) \) and \( \Sp(2m,\nR) \) have the same expected dimension? Solve the resulting equation.
3. The group \( \SO(n) \) is cut out of \( \Orth(n) \) by the single equation \( \det\P = 1 \). Why does this **not** reduce the expected dimension by one?
:::
:::

::: {.solution}
(a) \( \Orth(4) \) and \( \Orth(2,2) \) both have \( n = 4 \), so \( \tfrac12\cdot 4\cdot 3 = 6 \). \( \Unit(3) \): \( 3^2 = 9 \) real parameters. \( \Sp(4,\nR) \): \( m = 2 \), so \( m(2m+1) = 10 \).

(b) The equation is \( \tfrac12 n(n-1) = m(2m+1) \), that is \( n(n-1) = (2m+1)(2m) \). Reading the right-hand side as \( n(n-1) \) with \( n = 2m+1 \) shows that \( n = 2m+1 \) is a solution for **every** \( m \), and it is the only one: \( n \mapsto n(n-1) \) is strictly increasing for \( n \ge 1 \), so it takes each value at most once. Hence
\[
\dim\Orth(2m+1) = \dim\Sp(2m, \nR) = m(2m+1) ,
\]
and no other pairing of the two families matches. The smallest case is \( \Orth(3) \) and \( \Sp(2,\nR) = \SL_2(\nR) \), both of dimension \( 3 \).

(c) Because \( \det\P = \pm 1 \) already, by @thm-classical-group-determinants (a). The condition \( \det\P = 1 \) does not shrink a continuum of possibilities to a smaller one; it selects one of two discrete alternatives. So \( \SO(n) \) has the same expected dimension \( \tfrac12 n(n-1) \) as \( \Orth(n) \), and the two groups differ only in how many separate pieces they have — which is a topological statement of the kind this section does not prove.
:::

### C. Going deeper

::: {#exr-the-classical-groups-c1}
[C1: Isometries of a degenerate form]

Let \( \A = \begin{psmallmatrix} 1 & 0 \\ 0 & 0 \end{psmallmatrix} \in M_2(\nR) \) and let
\( G = \{\, \P \in M_2(\nR) : \P\tp\A\P = \A \,\} \), the set produced by dropping the non-degeneracy hypothesis from @def-isometry-group-of-form.

::: {.enumerate options="label=(\alph*)"}
1. Determine \( G \) explicitly.
2. Exhibit an element of \( G \) that is not invertible, and explain which step of the proof of @thm-classical-groups-are-groups it defeats.
3. Prove that the invertible elements of \( G \) do form a group.
:::
:::

::: {.solution}
(a) Write \( \P = \begin{psmallmatrix} a & b \\ c & d\end{psmallmatrix} \). Then
\[
\P\tp\A\P = \begin{pmatrix} a & c \\ b & d\end{pmatrix}\begin{pmatrix} a & b \\ 0 & 0\end{pmatrix} = \begin{pmatrix} a^2 & ab \\ ab & b^2 \end{pmatrix},
\]
so the condition is \( a^2 = 1 \), \( ab = 0 \), \( b^2 = 0 \). The last two say \( b = 0 \), and the first says \( a = \pm 1 \). Hence
\[
G = \left\{ \begin{pmatrix} \pm 1 & 0 \\ c & d \end{pmatrix} : c, d \in \nR \right\} .
\]

(b) Take \( c = d = 0 \) and \( a = 1 \): the matrix \( \begin{psmallmatrix} 1 & 0 \\ 0 & 0\end{psmallmatrix} \) lies in \( G \) and has determinant \( 0 \). The step it defeats is the cancellation of \( \det\A \) in \( (\det\P)^2\det\A = \det\A \). Here \( \det\A = 0 \), the equation reads \( 0 = 0 \), and it says nothing about \( \det\P \).

(c) Let \( G^{\times} \) be the set of invertible elements of \( G \); from (a) these are the matrices above with \( d \ne 0 \). It contains \( \I_2 \). It is closed under products, since \( G \) is (the computation in @thm-classical-groups-are-groups needs only \( \P\tp\A\P = \A \) and \( \Q\tp\A\Q = \A \), not invertibility) and a product of invertible matrices is invertible. And it is closed under inverses: if \( \P \in G^{\times} \) then multiplying \( \P\tp\A\P = \A \) by \( (\P^{-1})\tp \) and \( \P^{-1} \) gives \( \P^{-1} \in G \), and \( \P^{-1} \) is invertible. So \( G^{\times} \) is a group — but it is *not* all of \( G \), which is the reason @def-isometry-group-of-form assumes non-degeneracy rather than repairing the damage afterwards.
:::

::: {#exr-the-classical-groups-c2}
[C2: The symplectic group of a two-dimensional form, revisited]

Let \( F \) be any field and let \( \beta \) be a non-degenerate alternating form on a two-dimensional vector space \( V \) over \( F \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \operatorname{Isom}(\beta) = \{\, T \in \cL(V) : \det T = 1 \,\} \).
2. Deduce that for \( F = \nF_2 \) the group \( \Sp(2, \nF_2) \) has exactly \( 6 \) elements, and that \( \Sp(2,\nF_2) = \GL_2(\nF_2) \).
3. Is \( \Sp(2,\nF_3) = \GL_2(\nF_3) \)? Justify your answer by a count.
:::

*Hint for (b) and (c): count the invertible matrices over \( \nF_q \) by choosing the columns in turn.*
:::

::: {.solution}
(a) Choose a symplectic basis \( \sB \) for \( \beta \), which exists by @thm-symplectic-standard-form (b); then \( \mtx{\beta}{\sB}{\sB} = \vOmega_2 \). By the correspondence after @def-isometry-group-of-form, \( T \in \operatorname{Isom}(\beta) \) if and only if \( \P \coloneqq \mtx{T}{\sB}{\sB} \) lies in \( \operatorname{Isom}(\vOmega_2) = \Sp(2,F) \), which by @thm-classical-group-determinants (c) says \( \det\P = 1 \). Finally \( \det T = \det\P \) by @def-det-operator, since the determinant of an operator is that of its matrix in any basis.

(b) By (a), \( \Sp(2,\nF_2) = \SL_2(\nF_2) \). Count \( \GL_2(\nF_2) \) first: the first column may be any of the \( 4 - 1 = 3 \) non-zero vectors, and the second any of the \( 4 - 2 = 2 \) vectors outside the span of the first, giving \( 6 \). Over \( \nF_2 \) the only non-zero scalar is \( 1 \), so every invertible matrix has \( \det = 1 \); hence \( \SL_2(\nF_2) = \GL_2(\nF_2) \) has \( 6 \) elements.

(c) No. The same count over \( \nF_3 \) gives \( \lvert\GL_2(\nF_3)\rvert = (9-1)(9-3) = 48 \). The determinant is a surjective homomorphism \( \GL_2(\nF_3) \to \nF_3^{\times} \), whose target has \( 2 \) elements, and its fibers all have the same size; so \( \lvert\SL_2(\nF_3)\rvert = 24 \ne 48 \). Concretely \( \diag(1, -1) \) is invertible with determinant \( -1 \ne 1 \), so it lies in \( \GL_2(\nF_3) \) and not in \( \Sp(2,\nF_3) \).
:::

::: {#exr-the-classical-groups-c3}
[C3: Bounded and unbounded]

::: {.enumerate options="label=(\alph*)"}
1. Prove that every entry of a matrix \( \P \in \Orth(n) \) satisfies \( \lvert p_{ij}\rvert \le 1 \).
2. Prove that for every \( n \ge 2 \) and every real \( M \), the group \( \Orth(n-1, 1) \) contains a matrix with an entry larger than \( M \).
3. Explain in two sentences why (a) and (b) together make it plausible that \( \Orth(n) \) is compact and \( \Orth(n-1,1) \) is not, and say precisely what has and has not been proved.
:::
:::

::: {.solution}
(a) The columns of \( \P \in \Orth(n) \) are orthonormal in \( \nR^n \) (@thm-isometry-characterizations (f)), so for each \( j \) we have \( \sum_i p_{ij}^2 = 1 \). Each term of a sum of non-negative reals is at most the sum, so \( p_{ij}^2 \le 1 \) and \( \lvert p_{ij}\rvert \le 1 \).

(b) Put \( \B_t \coloneqq \begin{psmallmatrix} \cosh t & \sinh t \\ \sinh t & \cosh t\end{psmallmatrix} \), which lies in \( \Orth(1,1) \) for every real \( t \) by @exm-elements-of-the-classical-groups (a), and consider
\[
\P_t \coloneqq \I_{n-2} \oplus \B_t \in M_n(\nR) .
\]
(For \( n = 2 \) read \( \P_t = \B_t \).) As a block diagonal matrix \( \I_{n-1,1} = \I_{n-2}\oplus\I_{1,1} \), and each block of \( \P_t \) preserves its own block of the form: \( \I_{n-2}\tp\,\I_{n-2}\,\I_{n-2} = \I_{n-2} \), and \( \B_t\tp\I_{1,1}\B_t = \I_{1,1} \) by @exm-elements-of-the-classical-groups (a). Multiplying block by block gives \( \P_t\tp\I_{n-1,1}\P_t = \I_{n-1,1} \), so \( \P_t \in \Orth(n-1,1) \). Its \( (n,n) \) entry is \( \cosh t = \tfrac12(e^t + e^{-t}) \ge \tfrac12 e^t \), and \( e^t \) grows without bound, so some \( t \) makes this entry exceed the given \( M \).

(c) A compact subset of \( M_n(\nR) \cong \nR^{n^2} \) must be bounded, so (b) rules out compactness for \( \Orth(n-1,1) \), while (a) supplies half of what \( \Orth(n) \) would need. What has been **proved** here is only the statement about entries: \( \Orth(n) \) is bounded and \( \Orth(n-1,1) \) is not. That "bounded and closed implies compact" in \( \nR^{n^2} \), and that \( \Orth(n) \) is closed, are theorems of analysis that this book does not prove, so the compactness claim itself remains recorded rather than established.
:::
