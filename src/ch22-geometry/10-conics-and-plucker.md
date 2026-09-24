# Conics and Lines in Space

Chapter 14 classified symmetric bilinear forms and never drew a picture. This section is the picture. A quadratic form on \( V \) has a zero set in \( \nP(V) \), that zero set is unchanged when the form is scaled, and Sylvester's law becomes a list of shapes. Then a second theme, which looks unrelated and is not: a line in three-dimensional projective space is a plane in \( F^4 \), a plane in \( F^4 \) is a wedge of two vectors, and the wedges among all of \( \Lambda^2 F^4 \) are picked out by one quadratic equation. The lines in space are themselves a quadric.

**Throughout this section \( \operatorname{char} F \ne 2 \)**, except in the Plücker material at the end, which needs no hypothesis on \( F \) and says so where it begins. The reason is Chapter 14's: in characteristic \( 2 \) a quadratic form is not determined by a symmetric matrix, and every classification theorem we lean on fails.

## Quadrics in projective space

A quadratic form \( q \) on \( V \) is not a function on \( \nP(V) \): its value at \( \lambda\x \) is \( \lambda^2 \) times its value at \( \x \), so a point has no well-defined \( q \)-value. But whether the value is **zero** does not move, and that is all a zero set needs.

*A projective quadric is where a quadratic form vanishes; scaling the vector cannot change whether it does.*

::: {#def-projective-quadric}
[Projective Quadric, Conic, Smooth Quadric]

Let \( \operatorname{char} F \ne 2 \), let \( V \) be a finite-dimensional vector space over \( F \) and let \( q \) be a **non-zero** quadratic form on \( V \) (@def-quadratic-form), with associated symmetric bilinear form \( \beta \) (@thm-polarization-forms). The **projective quadric defined by \( q \)** is
\[
Z(q) \coloneqq \{\, [\x] \in \nP(V) : q(\x) = 0 \,\} .
\]
The **rank** of the quadric is \( \rank\beta \), and the quadric is **smooth** (or **non-degenerate**) when \( \beta \) is non-degenerate, that is, when the rank is \( \dim V \). A quadric in a projective **plane** is called a **conic**, the same word Section 5 used for the affine case (@def-quadric).
:::

The set is well defined: if \( \x' = \lambda\x \) with \( \lambda \ne 0 \), then \( q(\x') = \beta(\lambda\x, \lambda\x) = \lambda^2 q(\x) \), which is zero exactly when \( q(\x) \) is. The word **non-zero** in the definition rules out \( q = 0 \), whose zero set is all of \( \nP(V) \) and carries no information. And the rank is well defined because \( \beta \) is: over a field of characteristic \( \ne 2 \) a quadratic form has exactly one symmetric bilinear form behind it (@thm-polarization-forms).

Fix a basis of \( V \). Then \( q(\x) = \x\tp\A\x \) for a unique symmetric matrix \( \A \), the matrix of \( \beta \) (@def-form-matrix), and \( \rank\A \) is the rank of the quadric. Three examples in \( \nP^2 \), written in homogeneous coordinates \( [x_0:x_1:x_2] \).

- \( q = x_0^2 + x_1^2 - x_2^2 \), with \( \A = \diag(1,1,-1) \), rank \( 3 \), smooth. Over \( \nR \) its points are the projective version of the unit circle; \( [1:0:1] \) is one of them.
- \( q = x_0x_1 \), with \( \A = \begin{psmallmatrix} 0 & 1/2 & 0 \\ 1/2 & 0 & 0 \\ 0&0&0\end{psmallmatrix} \), rank \( 2 \). Its zero set is the union of the two lines \( \{x_0 = 0\} \) and \( \{x_1 = 0\} \).
- \( q = x_0^2 \), rank \( 1 \). Its zero set is the single line \( \{x_0 = 0\} \), because a field has no non-zero element whose square is \( 0 \). The form remembers something the set forgets, which is the first warning of the section.

::: {.warning}
**A quadric is named by its form, not by its set.** Over \( \nR \) the distinct forms \( x_0^2 + x_1^2 + x_2^2 \) and \( 2x_0^2 + 5x_1^2 + x_2^2 \) have the same zero set in \( \nP^2(\nR) \), namely the empty set, which records nothing at all about either of them. So "the quadric \( Z(q) \)" is always shorthand for "the quadric defined by \( q \)", and the theorem below classifies **forms** up to projective equivalence, not sets.
:::

A projective transformation \( [\x] \mapsto [T\x] \) (@def-projective-transformation) carries \( Z(q) \) to \( Z(q \circ T^{-1}) \), and \( Z(q) = Z(cq) \) for every \( c \ne 0 \). So the right relation on forms is: \( q \) and \( q' \) are **projectively equivalent** when \( q' = c\,(q \circ T) \) for some \( c \in F^{\times} \) and some \( T \in \GL(V) \). In matrices: \( \A' = c\,\P\tp\A\P \) with \( \P \) invertible, which is congruence (@def-congruent) followed by a scaling.

::: {#thm-projective-classification}
[Classification of Projective Quadrics]

Let \( \operatorname{char} F \ne 2 \) and \( \dim V = n+1 \), and let \( q, q' \) be non-zero quadratic forms on \( V \) with matrices \( \A, \A' \) in some basis.

::: {.enumerate options="label=(\alph*)"}
1. If \( F \) is algebraically closed, then \( q \) and \( q' \) are projectively equivalent if and only if \( \rank\A = \rank\A' \). There are exactly \( n+1 \) classes, one for each rank \( r = 1, \dots, n+1 \), with normal form \( x_0^2 + \dots + x_{r-1}^2 \).
2. If \( F = \nR \), then \( q \) and \( q' \) are projectively equivalent if and only if their inertias \( (n_+, n_-, n_0) \) and \( (n_+', n_-', n_0') \) agree **up to interchanging \( n_+ \) with \( n_- \)**. A normal form is \( x_0^2 + \dots + x_{n_+-1}^2 - x_{n_+}^2 - \dots - x_{r-1}^2 \) with \( n_+ \ge n_- \), \( r = n_+ + n_- \).
:::
:::

::: {.idea}
Both parts reduce the extra freedom — the scalar \( c \) — to something already classified. Over an algebraically closed field \( c \) has a square root, so scaling is itself a congruence and adds nothing: the answer is Chapter 14's. Over \( \nR \) a positive \( c \) is again a congruence, and the only new move is \( c = -1 \), which turns \( q \) into \( -q \) and swaps the two counts.
:::

::: {.proof}
(a) \( (\Leftarrow) \) It is enough to show that a symmetric \( \A \) of rank \( r \ge 1 \) is congruent to \( \I_r \oplus \0 \), since a congruence is the case \( c = 1 \) and congruence is an equivalence relation (@prp-congruence-equivalence). By @thm-symmetric-form-diagonalizable, \( \A \simeq \D = \diag(d_1, \dots, d_{n+1}) \), and congruence preserves rank (@thm-congruence-preserves-rank), so exactly \( r \) of the \( d_i \) are non-zero; permuting the basis, a congruence by a permutation matrix, we may assume these are \( d_1, \dots, d_r \). Since \( F \) is algebraically closed, choose \( s_i \) with \( s_i^2 = d_i \) for \( i \le r \) and put \( t_i = 1/s_i \) for \( i \le r \), \( t_i = 1 \) otherwise; by @prp-diagonal-entries-square-classes the congruence by \( \diag(t_1, \dots, t_{n+1}) \) replaces \( d_i \) by \( t_i^2d_i \), giving \( \I_r \oplus \0 \). (For \( F = \nC \) this is @cor-complex-symmetric-classification.)

\( (\Rightarrow) \) Suppose \( \A' = c\,\P\tp\A\P \) with \( c \ne 0 \). Choose \( s \in F \) with \( s^2 = c \); then \( \A' = (s\P)\tp\A(s\P) \) with \( s\P \) invertible, so \( \A' \simeq \A \) and @thm-congruence-preserves-rank gives \( \rank\A' = \rank\A \). The ranks of a non-zero form run over \( 1, \dots, n+1 \), and the normal form is the \( \I_r \oplus \0 \) produced above, whose quadratic form is \( x_0^2 + \dots + x_{r-1}^2 \).

(b) \( (\Leftarrow) \) If the inertias agree, @cor-real-symmetric-classification (b) gives \( \A' \simeq \A \), which is the case \( c = 1 \). If they agree after interchanging \( n_+ \) and \( n_- \), then \( \A' \) has the same inertia as \( -\A \), so \( \A' \simeq -\A = (-1)\A \), which is the case \( c = -1 \) composed with a congruence.

\( (\Rightarrow) \) Let \( \A' = c\,\P\tp\A\P \). If \( c > 0 \), put \( s = \sqrt c \) and argue as in (a): \( \A' \simeq \A \), so the inertias agree by @cor-real-symmetric-classification (b). If \( c < 0 \), put \( s = \sqrt{-c} \); then \( \A' = (s\P)\tp(-\A)(s\P) \simeq -\A \). Diagonalizing \( \A \) with \( n_+ \) positive and \( n_- \) negative entries diagonalizes \( -\A \) with the two counts interchanged, so the inertia of \( -\A \), hence of \( \A' \), is \( (n_-, n_+, n_0) \) by @thm-sylvester-inertia. This proves the theorem.
:::

For \( n = 2 \) the list is short enough to write out, and worth memorizing.

::: {#cor-conics-in-the-projective-plane}
[The Conics of a Projective Plane]

Let \( \operatorname{char} F \ne 2 \) and let \( q \) be a non-zero quadratic form on a \( 3 \)-dimensional space.

::: {.enumerate options="label=(\alph*)"}
1. Over an algebraically closed \( F \) there are three classes, with zero sets: a line (rank \( 1 \)), two distinct lines (rank \( 2 \)), a smooth conic (rank \( 3 \)).
2. Over \( \nR \) there are five classes, listed by \( (n_+, n_-) \) with \( n_+ \ge n_- \), with zero sets:
\[
\begin{aligned}
(1,0) &: \ \text{a line}, &\quad (2,0) &: \ \text{a single point}, \\
(1,1) &: \ \text{two distinct lines}, &\quad (3,0) &: \ \text{empty}, \\
(2,1) &: \ \text{a smooth conic, non-empty.} & &
\end{aligned}
\]
:::
:::

::: {.proof}
The classes are those of @thm-projective-classification; only the zero sets need identifying, and each is read off a normal form.

\( x_0^2 = 0 \) holds exactly when \( x_0 = 0 \), a field having no non-zero square root of \( 0 \); the set is the line \( \{x_0 = 0\} \). Next, \( x_0^2 + x_1^2 \) factors over an algebraically closed field as \( (x_0 + ix_1)(x_0 - ix_1) \) with \( i^2 = -1 \), and the two linear forms are not proportional since \( i \ne -i \) (as \( \operatorname{char} F \ne 2 \)), so the set is two distinct lines; over \( \nR \) instead \( x_0^2 + x_1^2 = 0 \) forces \( x_0 = x_1 = 0 \), leaving the single point \( [0:0:1] \). The form \( x_0^2 - x_1^2 = (x_0-x_1)(x_0+x_1) \) gives two distinct lines over every field of characteristic \( \ne 2 \). Over \( \nR \), \( x_0^2 + x_1^2 + x_2^2 = 0 \) forces \( \x = \0 \), which is not a point of \( \nP^2 \), so the set is empty. Finally \( x_0^2 + x_1^2 - x_2^2 \) has rank \( 3 \), so its quadric is smooth, and it contains \( [1:0:1] \). This proves the corollary.
:::

::: {.remark}
Section 5 classified **affine** quadrics and produced a longer real list, because an affine classification must also record whether a center exists and whether the constant can be cleared. There is no conflict: the affine group is smaller than the projective one — an invertible affine substitution is exactly a projectivity fixing the hyperplane at infinity (@thm-projectivities-fixing-infinity) — so the affine classification is the finer of the two, and the list above is what Section 5 pointed forward to for the complex case.
:::

::: {.warning}
**Rank alone does not classify real conics; inertia does.** The forms \( x_0^2 + x_1^2 + x_2^2 \) and \( x_0^2 + x_1^2 - x_2^2 \) both have rank \( 3 \), and one zero set is empty while the other has infinitely many points. One rank lower, \( x_0^2 + x_1^2 \) and \( x_0^2 - x_1^2 \) both have rank \( 2 \), and the zero sets are a point and a pair of lines. Over \( \nC \) each pair collapses: rank is a complete invariant there, so the two forms of each pair become projectively equivalent.
:::

::: {#exm-classify-a-conic}
[Classifying a conic by hand]

Classify the conic \( x_0^2 + 4x_0x_1 + 5x_1^2 + 2x_1x_2 + 2x_2^2 = 0 \) in \( \nP^2(\nR) \), and say what happens over \( \nC \).
:::

::: {.solution}
Complete the square in \( x_0 \) first, since \( x_0^2 \) appears:
\[
x_0^2 + 4x_0x_1 = (x_0 + 2x_1)^2 - 4x_1^2 ,
\]
so the form equals \( (x_0+2x_1)^2 + x_1^2 + 2x_1x_2 + 2x_2^2 \). Completing the square in \( x_1 \) in what is left, \( x_1^2 + 2x_1x_2 = (x_1+x_2)^2 - x_2^2 \), and therefore
\[
q = (x_0+2x_1)^2 + (x_1+x_2)^2 + x_2^2 .
\]
The three linear forms \( x_0+2x_1 \), \( x_1+x_2 \), \( x_2 \) are independent — the matrix with these rows is upper triangular with determinant \( 1 \) — so this is a diagonalization with inertia \( (3,0,0) \). By @cor-conics-in-the-projective-plane (b) the conic is **empty** over \( \nR \).

Over \( \nC \) the same three squares have rank \( 3 \), so by (a) the conic is smooth, and it is not empty: take \( x_2 = 1 \) and \( x_1 = -1 \), so that the second square vanishes and the equation becomes \( (x_0-2)^2 = -1 \), solved by \( x_0 = 2+i \). The point \( [2+i : -1 : 1] \) lies on it. The real conic was empty not because the form was degenerate but because it was definite, which is a statement no algebraically closed field can make.
:::

::: {.check}
A conic in \( \nP^2(\nR) \) consists of exactly one point. What is the rank of its form, and what is its inertia?
:::

::: {.solution}
By the list in @cor-conics-in-the-projective-plane (b) the only class with a one-point zero set is \( (n_+, n_-) = (2,0) \), of rank \( 2 \); up to sign the form is \( x_0^2 + x_1^2 \) in suitable coordinates. Rank \( 1 \) gives a line and rank \( 3 \) gives either nothing or a curve, so no other class can produce one point.
:::

## Five points determine a conic

Six coefficients, five conditions, one answer. The existence half is a count; the uniqueness half is where the work is, and it is exactly where "in general position" earns its keep.

"In general position" is @def-general-position read with \( m = 5 \) and \( n = 2 \): every subset of at most three of the five points has independent representatives. In a projective plane that says exactly that the five points are pairwise distinct and that no three of them are collinear.

The lemma below is what forbids a conic from swallowing a line, and it is used twice more later.

::: {#lem-quadric-containing-a-line}
[A Conic Containing a Line Is Degenerate]

Let \( \operatorname{char} F \ne 2 \), let \( \dim V = 3 \) and let \( q \ne 0 \) be a quadratic form on \( V \) vanishing on every vector of a \( 2 \)-dimensional subspace \( W \). Then \( q = \varphi\chi \) for two non-zero linear functionals \( \varphi, \chi \) on \( V \) with \( \ker\varphi = W \), and the rank of \( q \) is at most \( 2 \). In particular a **smooth** conic contains no line.
:::

::: {.proof}
Let \( \beta \) be the symmetric form of \( q \) and choose a basis \( (\w_0, \w_1, \v_2) \) of \( V \) with \( W = \Span(\w_0, \w_1) \). Evaluating \( q \) at \( \w_0 \), at \( \w_1 \) and at \( \w_0 + \w_1 \), all of which lie in \( W \), gives
\[
\beta(\w_0,\w_0) = 0, \quad \beta(\w_1,\w_1) = 0, \quad 2\beta(\w_0,\w_1) = 0 ,
\]
the third because \( q(\w_0+\w_1) = \beta(\w_0,\w_0) + 2\beta(\w_0,\w_1) + \beta(\w_1,\w_1) \). Since \( 2 \) is invertible, \( \beta(\w_0,\w_1) = 0 \) too. Put \( c_0 = \beta(\w_0,\v_2) \), \( c_1 = \beta(\w_1,\v_2) \) and \( c = \beta(\v_2,\v_2) \). In the coordinates \( \x = (x_0,x_1,x_2) \) of this basis,
\[
q(\x) = 2c_0x_0x_2 + 2c_1x_1x_2 + cx_2^2 = x_2\bigl(2c_0x_0 + 2c_1x_1 + cx_2\bigr) ,
\]
a product \( \varphi\chi \) with \( \varphi(\x) = x_2 \), whose kernel is \( W \), and \( \chi \) the second factor, which is non-zero because \( q \ne 0 \). The Gram matrix of \( \beta \) in this basis (@def-form-matrix) has rows \( (0,0,c_0) \), \( (0,0,c_1) \) and \( (c_0,c_1,c) \); the first two lie in a \( 1 \)-dimensional subspace, so the three of them span at most a \( 2 \)-dimensional one and the rank is at most \( 2 \).

If \( q \) is smooth its rank is \( 3 \), so no such \( W \) exists, and a line \( \nP(W) \) contained in \( Z(q) \) would supply one. This proves the lemma.
:::

::: {#thm-five-points-determine-a-conic}
[Five Points Determine a Conic]

Let \( \operatorname{char} F \ne 2 \) and let \( P_1, \dots, P_5 \) be five points of \( \nP^2 \) in general position (@def-general-position), that is, pairwise distinct with no three collinear. Then there is a non-zero quadratic form \( q \) on \( F^3 \) vanishing at all five, and it is unique up to a non-zero scalar. Consequently exactly one conic passes through the five points.
:::

::: {.idea}
The symmetric \( 3 \times 3 \) matrices form a \( 6 \)-dimensional space and each point imposes one linear equation on it, so five points leave at least a line of solutions: that is existence, and it is only counting. For uniqueness suppose the solution space had dimension \( 2 \). Then a whole pencil of conics passes through the five points, and a pencil is big enough to be forced through a **sixth** point, chosen on the line \( P_1P_2 \). A conic through three points of a line contains the line, so by @lem-quadric-containing-a-line it splits into two lines; one of them is \( P_1P_2 \), and the other must then carry \( P_3, P_4, P_5 \) — three collinear points, which general position forbids.
:::

::: {.proof}
Let \( S \subseteq M_3(F) \) be the subspace of symmetric matrices. A symmetric \( 3\times3 \) matrix is determined by its three diagonal entries and its three entries above the diagonal, each of which may be chosen freely, so \( \dim S = 6 \). By @thm-polarization-forms the map \( \A \mapsto q_{\A} \), \( q_{\A}(\x) = \x\tp\A\x \), is a bijection from \( S \) onto the quadratic forms on \( F^3 \), and it is linear.

*Existence.* Write \( P_i = [\x_i] \). For each \( i \) the map \( \A \mapsto \x_i\tp\A\x_i \) is a linear functional on \( S \), because the expression is linear in the entries of \( \A \). The five functionals give a homogeneous linear system of \( 5 \) equations in the \( 6 \) coordinates of \( \A \), which by @cor-more-unknowns-than-equations (a) has a non-trivial solution \( \A \ne \0 \). The corresponding \( q_{\A} \) is a non-zero quadratic form vanishing at every \( \x_i \), hence at every \( P_i \). (Vanishing does not depend on the representative, by the homogeneity noted after @def-projective-quadric.)

*Uniqueness.* Let \( N \subseteq S \) be the solution space of that system, and suppose \( \dim N \ge 2 \). Pick independent \( \A_1, \A_2 \in N \), and write \( q_1, q_2 \) for the corresponding forms, which are independent as forms since \( \A \mapsto q_{\A} \) is a bijection that is linear.

The line \( L = P_1P_2 \) contains at least three points: it is \( \nP(U) \) with \( \dim U = 2 \), so it contains \( [\u_1] \), \( [\u_2] \) and \( [\u_1 + \u_2] \) for a basis \( (\u_1, \u_2) \) of \( U \), and these are three distinct points. Choose \( R = [\y] \) on \( L \) with \( R \ne P_1 \) and \( R \ne P_2 \). The condition \( \lambda\,\y\tp\A_1\y + \mu\,\y\tp\A_2\y = 0 \) is one homogeneous linear equation in \( (\lambda, \mu) \), so by @cor-more-unknowns-than-equations (a) it has a solution with \( (\lambda,\mu) \ne (0,0) \). Put \( \A = \lambda\A_1 + \mu\A_2 \), which is non-zero because \( \A_1, \A_2 \) are independent, and let \( q = q_{\A} \), a non-zero quadratic form.

Now \( q \) vanishes at the three distinct points \( P_1, P_2, R \) of \( L \). Restrict \( q \) to \( U \): in the basis \( (\u_1, \u_2) \) it reads \( g(s,t) = \alpha s^2 + \gamma st + \delta t^2 \). A non-zero \( g \) vanishes at at most two points of \( \nP(U) \). Indeed, if \( \alpha \ne 0 \) then \( g(s,0) = \alpha s^2 \ne 0 \) whenever \( s \ne 0 \), so every zero has \( t \ne 0 \) and is therefore \( [m:1] \) for a scalar \( m \) with \( \alpha m^2 + \gamma m + \delta = 0 \) — a polynomial in \( m \) of degree at most \( 2 \), non-zero because its leading coefficient is \( \alpha \), so with at most two roots (@lem-root-bound); if \( \alpha = 0 \) then \( g = t(\gamma s + \delta t) \), whose zeros are \( [1:0] \) together with the at most one point where \( \gamma s + \delta t = 0 \), and \( (\gamma,\delta) \ne (0,0) \) since \( g \ne 0 \). Three zeros therefore force \( g = 0 \), that is, \( q \) vanishes on all of \( U \).

By @lem-quadric-containing-a-line, \( q = \varphi\chi \) with \( \ker\varphi = U \). For \( i = 3, 4, 5 \) we have \( q(\x_i) = 0 \), and \( \varphi(\x_i) \ne 0 \), since \( \varphi(\x_i) = 0 \) would put \( P_i \) on \( L = P_1P_2 \), making \( P_1, P_2, P_i \) collinear. Hence \( \chi(\x_i) = 0 \) for \( i = 3,4,5 \), so \( P_3, P_4, P_5 \) all lie on the line \( \{\chi = 0\} \) — three collinear points among the five, contradicting general position.

So \( \dim N = 1 \): the form is unique up to a non-zero scalar, and \( Z(q) \) is the unique conic through the five points. This proves the theorem.
:::

::: {#exm-five-points}
[A conic through five points]

Find the conic of \( \nP^2(\nQ) \) through \( [1:0:0] \), \( [0:1:0] \), \( [0:0:1] \), \( [1:1:1] \) and \( [1:2:4] \), and decide whether it is smooth.
:::

::: {.solution}
Write \( q = ax_0^2 + bx_1^2 + cx_2^2 + dx_0x_1 + ex_0x_2 + fx_1x_2 \). The first three points give \( a = b = c = 0 \) at once. Then \( [1:1:1] \) gives \( d + e + f = 0 \) and \( [1:2:4] \) gives \( 2d + 4e + 8f = 0 \), that is \( d + 2e + 4f = 0 \). Subtracting, \( e + 3f = 0 \), so \( e = -3f \) and \( d = -e-f = 2f \). Taking \( f = 1 \),
\[
q = 2x_0x_1 - 3x_0x_2 + x_1x_2 ,
\]
and the solution space is indeed one-dimensional, as @thm-five-points-determine-a-conic promises. (No three of the five points are collinear: taking the ten triples in the order \( 123 \), \( 124 \), \( 125 \), \( 134 \), \( 135 \), \( 145 \), \( 234 \), \( 235 \), \( 245 \), \( 345 \), the determinants of the corresponding coordinate matrices are
\[
1,\ 1,\ 4,\ -1,\ -2,\ 2,\ 1,\ 1,\ -3,\ 1 ,
\]
none of them zero.)

Its matrix is
\[
\A = \begin{pmatrix} 0 & 1 & -3/2 \\ 1 & 0 & 1/2 \\ -3/2 & 1/2 & 0 \end{pmatrix},
\qquad \det\A = -\tfrac32 \ne 0 ,
\]
so the conic is smooth. Over \( \nR \) its inertia is \( (2,1,0) \): the three eigenvalues are real (@cor-spectral-real-matrix) and the inertia counts their signs (@thm-inertia-from-eigenvalues); their product is \( \det\A < 0 \), so an odd number of them is negative, and \( \tr\A = 0 \) rules out all three, leaving exactly one.
:::

## Projecting a conic onto a line

Here is the payoff a reader can take home. A smooth conic looks like a curve, and the next theorem says that as a set it **is** a projective line, provided it has one point to start from. Over \( \nQ \) that converts one solution of a Diophantine equation into all of them; over \( \nF_q \) it says a smooth conic with a point has exactly \( q+1 \) of them.

::: {#thm-conic-parametrization}
[Projection from a Point of a Conic]

Let \( \operatorname{char} F \ne 2 \), let \( C = Z(q) \) be a **smooth** conic in \( \nP(V) \), \( \dim V = 3 \), and suppose \( C \) contains a point \( P_0 = [\p] \). Let \( \ell \) be any line of \( \nP(V) \) with \( P_0 \notin \ell \). Then the map
\[
\psi \colon \ell \to C, \qquad
\psi([\x]) = \bigl[\, -q(\x)\,\p + 2\beta(\p,\x)\,\x \,\bigr]
\]
is a well-defined bijection. In particular \( C \) is in bijection with \( \nP^1 \).
:::

::: {.idea}
Each point \( X \) of \( \ell \) is joined to \( P_0 \), and the line \( P_0X \) meets \( C \) in \( P_0 \) and in exactly one further point — "further" understood so that a tangent line counts \( P_0 \) twice. Expanding \( q(\lambda\p + \mu\x) \) and using \( q(\p) = 0 \) makes \( \mu \) a factor, so the quadratic equation is linear once the known root is removed, and the displayed formula is that root written out. Every line through \( P_0 \) other than \( \ell \) itself meets \( \ell \) once, which is where the inverse comes from.
:::

::: {.proof}
Write \( \ell = \nP(U) \) with \( \dim U = 2 \); since \( P_0 \notin \ell \), we have \( \p \notin U \), so \( \x \notin \Span(\p) \) for every \( \0 \ne \x \in U \).

*The formula is well defined.* Replacing \( \x \) by \( c\x \) with \( c \ne 0 \) multiplies \( -q(\x)\p + 2\beta(\p,\x)\x \) by \( c^2 \), so the point is unchanged. The vector is non-zero: if both \( q(\x) = 0 \) and \( \beta(\p,\x) = 0 \), then for all \( \lambda, \mu \),
\[
q(\lambda\p + \mu\x) = \lambda^2q(\p) + 2\lambda\mu\,\beta(\p,\x) + \mu^2q(\x) = 0 ,
\]
so \( q \) vanishes on the \( 2 \)-dimensional subspace \( \Span(\p,\x) \), contradicting @lem-quadric-containing-a-line since \( C \) is smooth. If instead \( \beta(\p,\x) \ne 0 \) the vector has a non-zero component along \( \x \) modulo \( \Span(\p) \); and if \( \beta(\p,\x) = 0 \) with \( q(\x) \ne 0 \), the vector is \( -q(\x)\p \ne \0 \).

*The value lies on \( C \).* Put \( \z = -q(\x)\p + 2\beta(\p,\x)\x \). Using \( q(\p) = 0 \) and bilinearity,
\[
\begin{aligned}
q(\z) &= q(\x)^2q(\p) - 2\cdot 2q(\x)\beta(\p,\x)\,\beta(\p,\x) + 4\beta(\p,\x)^2q(\x) \\
&= 0 - 4q(\x)\beta(\p,\x)^2 + 4\beta(\p,\x)^2q(\x) = 0 .
\end{aligned}
\]

*A fact used twice.* If \( [\y] \in C \) and \( [\y] \ne P_0 \), then \( \beta(\p,\y) \ne 0 \); otherwise \( q \) would vanish on \( \Span(\p,\y) \), a \( 2 \)-dimensional subspace since \( \p, \y \) represent distinct points, contradicting @lem-quadric-containing-a-line again.

*Surjectivity.* Let \( [\y] \in C \). Suppose first \( [\y] \ne P_0 \). The line \( P_0[\y] \) is distinct from \( \ell \), since \( P_0 \notin \ell \), so by @cor-two-lines-meet it meets \( \ell \) in a single point \( [\x] \), and \( \x = \lambda\p + \mu\y \) with \( \mu \ne 0 \) (else \( [\x] = P_0 \in \ell \)). Then \( q(\x) = 2\lambda\mu\,\beta(\p,\y) \) and \( \beta(\p,\x) = \mu\,\beta(\p,\y) \), so
\[
\begin{aligned}
-q(\x)\p + 2\beta(\p,\x)\x
&= -2\lambda\mu\beta(\p,\y)\,\p + 2\mu\beta(\p,\y)(\lambda\p + \mu\y) \\
&= 2\mu^2\beta(\p,\y)\,\y ,
\end{aligned}
\]
which is a non-zero multiple of \( \y \) by the fact just proved. So \( \psi([\x]) = [\y] \). Now suppose \( [\y] = P_0 \). The set \( T = \{[\z] : \beta(\p,\z) = 0\} \) is a line, \( \beta \) being non-degenerate so that \( \beta(\p,\cdot) \) is a non-zero functional; it contains \( P_0 \), because \( \beta(\p,\p) = q(\p) = 0 \), hence \( T \ne \ell \), and \( T \) meets \( \ell \) in one point \( [\x] \). There \( \beta(\p,\x) = 0 \) and \( q(\x) \ne 0 \) by the non-vanishing argument above, so \( \psi([\x]) = [-q(\x)\p] = P_0 \).

*Injectivity.* Suppose \( \psi([\x']) = \psi([\x'']) = [\y] \), with \( [\x'], [\x''] \in \ell \). For any \( \x \) the vector \( -q(\x)\p + 2\beta(\p,\x)\x \) lies in \( \Span(\p,\x) \), so \( [\y] \) lies on the line joining \( P_0 \) to \( [\x] \). If \( [\y] \ne P_0 \), then both \( [\x'] \) and \( [\x''] \) lie on the line joining \( P_0 \) to \( [\y] \), and both lie on \( \ell \); these two lines are distinct because \( P_0 \notin \ell \), so by @cor-two-lines-meet they meet in one point and \( [\x'] = [\x''] \). If \( [\y] = P_0 \), then \( 2\beta(\p,\x')\x' \in \Span(\p) \); since \( \x' \notin \Span(\p) \) and \( 2 \) is invertible, \( \beta(\p,\x') = 0 \), and likewise for \( \x'' \). So \( [\x'] \) and \( [\x''] \) both lie on \( T \cap \ell \), again a single point.

Finally \( \ell \) is a projective line, hence in bijection with \( \nP^1 \) by any choice of basis of \( U \). This proves the theorem.
:::

::: {#exm-pythagorean-triples}
[Pythagorean triples from one point]

Parametrize the rational points of the conic \( x_0^2 + x_1^2 = x_2^2 \) in \( \nP^2(\nQ) \), starting from \( P_0 = [-1:0:1] \).
:::

::: {.solution}
Here \( q(\x) = x_0^2 + x_1^2 - x_2^2 \), with \( \beta(\x,\y) = x_0y_0 + x_1y_1 - x_2y_2 \), and \( \A = \diag(1,1,-1) \) is invertible, so the conic is smooth. Also \( q(-1,0,1) = 1 - 1 = 0 \), so \( P_0 \in C \). Take \( \ell = \{x_0 = 0\} \), which misses \( P_0 \), and write its points as \( [0:u:v] \) with \( (u,v) \ne (0,0) \).

With \( \x = (0,u,v) \) we get \( q(\x) = u^2 - v^2 \) and \( \beta(\p,\x) = -v \), so
\[
\begin{aligned}
\psi([0:u:v]) &= \bigl[-(u^2-v^2)(-1,0,1) + 2(-v)(0,u,v)\bigr] \\
&= \bigl[\, u^2 - v^2 \ :\ -2uv \ :\ -u^2 - v^2 \,\bigr] \\
&= \bigl[\, v^2 - u^2 \ :\ 2uv \ :\ u^2 + v^2 \,\bigr] .
\end{aligned}
\]
Taking \( u, v \) to be integers, not both zero, the three coordinates are integers, and
\[
(v^2 - u^2)^2 + (2uv)^2 = u^4 + 2u^2v^2 + v^4 = (u^2+v^2)^2 ,
\]
a Pythagorean triple; the identity is exactly the statement that \( \psi \) lands in \( C \).

By @thm-conic-parametrization every point of \( C \) arises from exactly one point \( [0:u:v] \) of \( \ell \). So if \( (a,b,c) \) are integers with \( a^2 + b^2 = c^2 \) and \( c \ne 0 \), then \( [a:b:c] \) is a rational point of \( C \), hence
\[
(a, b, c) = \lambda\,(v^2 - u^2,\ 2uv,\ u^2 + v^2)
\]
for some rational \( \lambda \ne 0 \) and integers \( u, v \): every Pythagorean triple is proportional to one of this shape. (If \( c = 0 \) then \( a^2 + b^2 = 0 \) forces \( a = b = 0 \).) Deciding **which** proportionality factors give primitive triples is arithmetic about parities and common factors, not linear algebra, and we do not do it here.

Two checks. At \( [u:v] = [1:0] \), that is at the point \( [0:1:0] \) of \( \ell \), the formula returns \( [-1:0:1] = P_0 \). That is as it should be: the line joining \( P_0 \) to \( [0:1:0] \) consists of the points \( [-\lambda : \mu : \lambda] \), and \( q(-\lambda,\mu,\lambda) = \lambda^2 + \mu^2 - \lambda^2 = \mu^2 \), which vanishes only for \( \mu = 0 \). So that line meets \( C \) at \( P_0 \) alone, and \( P_0 \) is the only value \( \psi \) can take there. At \( [u:v] = [1:2] \) the formula gives \( [3:4:5] \).
:::

## Pole, polar and the dual conic

A smooth conic carries an invertible symmetric matrix, and an invertible symmetric matrix is a perfect pairing. Every point therefore names a line, and the dictionary this sets up is where tangency comes from.

::: {#def-pole-and-polar}
[Polar Line, Tangent Line]

Let \( C = Z(q) \) be a smooth conic in \( \nP(V) \), \( \dim V = 3 \), with symmetric bilinear form \( \beta \), and let \( P = [\x] \). The **polar** of \( P \) with respect to \( C \) is
\[
P^{\beta} \coloneqq \{\, [\y] \in \nP(V) : \beta(\x,\y) = 0 \,\} ,
\]
and \( P \) is the **pole** of that line. For \( P \in C \), the polar \( P^{\beta} \) is called the **tangent line** to \( C \) at \( P \).
:::

Because \( \beta \) is non-degenerate, \( \beta(\x,\cdot) \) is a non-zero functional (@prp-nondegenerate-iff-invertible (c)), so its kernel is \( 2 \)-dimensional and \( P^{\beta} \) really is a line; and replacing \( \x \) by \( c\x \) scales the functional, leaving the line alone. The next proposition says the word "tangent" is deserved.

::: {#prp-polar-properties}
[Reciprocity and Tangency]

With the notation of @def-pole-and-polar, let \( P = [\x] \) and \( Q = [\y] \).

::: {.enumerate options="label=(\alph*)"}
1. \( Q \in P^{\beta} \) if and only if \( P \in Q^{\beta} \).
2. \( P \in C \) if and only if \( P \in P^{\beta} \).
3. Let \( P \in C \) and let \( L \) be a line through \( P \). Then \( L \cap C = \{P\} \) if and only if \( L = P^{\beta} \); every other line through \( P \) meets \( C \) in exactly two points.
:::
:::

::: {.proof}
(a) Both conditions say \( \beta(\x,\y) = 0 \), since \( \beta \) is symmetric.

(b) \( P \in P^{\beta} \) says \( \beta(\x,\x) = 0 \), which is \( q(\x) = 0 \).

(c) Write \( L = \nP(\Span(\x,\y)) \) with \( \y \notin \Span(\x) \). A point of \( L \) is \( [\lambda\x + \mu\y] \), and since \( q(\x) = 0 \),
\[
q(\lambda\x + \mu\y) = \mu\bigl(2\lambda\,\beta(\x,\y) + \mu\,q(\y)\bigr) .
\]
*Case 1: \( L = P^{\beta} \),* that is, \( \beta(\x,\y) = 0 \). Then \( q(\lambda\x+\mu\y) = \mu^2 q(\y) \), and \( q(\y) \ne 0 \): otherwise \( q \) would vanish on \( \Span(\x,\y) \), contradicting @lem-quadric-containing-a-line. So the expression vanishes only when \( \mu = 0 \), giving the single point \( P \).

*Case 2: \( L \ne P^{\beta} \),* so \( \beta(\x,\y) \ne 0 \). Then the factorization above vanishes when \( \mu = 0 \), giving \( P \), and when \( 2\lambda\beta(\x,\y) + \mu q(\y) = 0 \), which has the solution \( (\lambda, \mu) = (-q(\y),\, 2\beta(\x,\y)) \) with \( \mu \ne 0 \), giving a point of \( C \) different from \( P \). Every point of \( L \cap C \) is one of these two, since the two cases \( \mu = 0 \) and \( 2\lambda\beta(\x,\y) + \mu q(\y) = 0 \) exhaust the factorization and each determines \( [\lambda:\mu] \). This proves the proposition.
:::

::: {#cor-dual-conic}
[The Dual Conic]

Let \( C \) be a smooth conic in \( \nP(V) \) with matrix \( \A \) in some basis, and identify each line of \( \nP(V) \) with the point \( [\varphi] \) of \( \nP(V^{*}) \) for which the line is \( \nP(\ker\varphi) \), as @prp-points-of-dual-are-hyperplanes allows. Then the set of tangent lines of \( C \) is the smooth conic of \( \nP(V^{*}) \) with matrix \( \A^{-1} \).
:::

::: {.proof}
The tangent at \( [\x] \in C \) is the zero set of the functional \( \y \mapsto \beta(\x,\y) = \x\tp\A\y \), whose coordinate vector in the dual basis (@thm-dual-basis) is \( \A\x \). As \( [\x] \) runs over \( C \), the corresponding point of \( \nP(V^{*}) \) is \( [\A\x] \) with \( \x\tp\A\x = 0 \). Since \( \A \) is invertible, putting \( \z = \A\x \) gives \( \x = \A^{-1}\z \) and
\[
0 = \x\tp\A\x = \z\tp(\A^{-1})\tp\A\A^{-1}\z = \z\tp\A^{-1}\z ,
\]
using \( (\A^{-1})\tp = (\A\tp)^{-1} = \A^{-1} \). Conversely every non-zero \( \z \) with \( \z\tp\A^{-1}\z = 0 \) arises this way, from \( \x = \A^{-1}\z \), which satisfies \( \x\tp\A\x = \z\tp\A^{-1}\z = 0 \). The matrix \( \A^{-1} \) is symmetric and invertible, so the set is a smooth conic. This proves the corollary.
:::

## Lines in space: Plücker coordinates

The definition, the proposition, the theorem and the warning that follow work over **any** field; no characteristic hypothesis is needed, and none is used. Only the paragraph closing the subsection returns to quadrics, and it re-imposes \( \operatorname{char} F \ne 2 \) where it does.

Chapter 15 built the exterior powers and hinted that the \( k \times k \) minors of an \( n \times k \) matrix turn a \( k \)-dimensional subspace into a single point. Here it is. A line of \( \nP^3 = \nP(F^4) \) is \( \nP(W) \) with \( \dim W = 2 \); a basis \( (\u,\w) \) of \( W \) has a wedge \( \u\wedge\w \in \Lambda^2F^4 \), which is non-zero by @thm-wedge-nonzero-iff-independent; and \( \dim\Lambda^2F^4 = \binom42 = 6 \) by @thm-exterior-power-basis. So a line in space becomes a point of \( \nP^5 \). The only questions are whether the point depends on the basis, whether different lines give different points, and which points of \( \nP^5 \) occur.

**Index convention.** In this part we number the standard basis of \( F^4 \) as \( \e_0, \e_1, \e_2, \e_3 \), matching the homogeneous coordinates \( [x_0 : x_1 : x_2 : x_3] \) on \( \nP^3 \), and we write \( \e_{ij} = \e_i\wedge\e_j \) for \( i < j \) and \( \e_{0123} = \e_0\wedge\e_1\wedge\e_2\wedge\e_3 \).

::: {#def-plucker-coordinates}
[Plücker Coordinates of a Line]

Let \( L = \nP(W) \) be a line of \( \nP^3 \) and let \( (\u, \w) \) be a basis of \( W \). The **Plücker coordinates** of \( L \) relative to that basis are the six scalars
\[
p_{ij} \coloneqq u_iw_j - u_jw_i , \qquad 0 \le i < j \le 3 ,
\]
that is, the \( 2 \times 2 \) minors of the \( 4\times 2 \) matrix with columns \( \u \) and \( \w \). By @thm-wedge-coordinates-are-minors they are the coordinates of the wedge:
\[
\u\wedge\w = \sum_{i<j} p_{ij}\,\e_{ij} .
\]
The point \( [\u\wedge\w] \in \nP(\Lambda^2F^4) = \nP^5 \) is the **Plücker point** of \( L \), written \( [L] \).
:::

::: {#prp-plucker-well-defined}
[The Plücker Point Determines the Line]

Let \( L = \nP(W) \) be a line of \( \nP^3 \) and let \( (\u,\w) \) be a basis of \( W \).

::: {.enumerate options="label=(\alph*)"}
1. \( \u\wedge\w \ne \0 \), and \( [\u\wedge\w] \) does not depend on the choice of basis \( (\u,\w) \) of \( W \), so \( [L] \) is well defined.
2. \( W = \{\, \v \in F^4 : \v\wedge\u\wedge\w = \0 \,\} \). Consequently \( L \mapsto [L] \) is injective on lines.
:::
:::

::: {.proof}
(a) A basis is independent, so @thm-wedge-nonzero-iff-independent gives \( \u\wedge\w \ne \0 \). Any other basis is \( \u' = a\u + c\w \), \( \w' = b\u + d\w \) for a change-of-basis matrix with columns \( (a,c) \) and \( (b,d) \), which is invertible, so \( ad - bc \ne 0 \). Expanding,
\[
\u'\wedge\w' = ad\,\u\wedge\w + cb\,\w\wedge\u = (ad-bc)\,\u\wedge\w ,
\]
the terms \( \u\wedge\u \) and \( \w\wedge\w \) vanishing. A non-zero scalar multiple represents the same point of \( \nP^5 \).

(b) By @thm-wedge-nonzero-iff-independent, \( \v\wedge\u\wedge\w = \0 \) exactly when \( (\v,\u,\w) \) is dependent, and since \( (\u,\w) \) is independent this happens exactly when \( \v \in \Span(\u,\w) = W \). So \( W \), hence \( L \), is recovered from any representative of \( [L] \); and if \( [L] = [L'] \) their representatives differ by a scalar, which does not change the set in the display, so \( W = W' \) and \( L = L' \). This proves the proposition.
:::

Which points of \( \nP^5 \) are Plücker points? Exactly one equation decides it.

::: {#thm-plucker-relation}
[The Plücker Relation and the Klein Quadric]

Let \( F \) be any field and let \( \0 \ne \omega = \sum_{i<j} p_{ij}\e_{ij} \in \Lambda^2F^4 \). Then \( \omega = \u\wedge\w \) for some \( \u,\w \in F^4 \) if and only if
\[
p_{01}p_{23} - p_{02}p_{13} + p_{03}p_{12} = 0 .
\]{#eq-plucker-relation}
Consequently \( L \mapsto [L] \) is a **bijection** from the set of lines of \( \nP^3 \) onto the set
\[
\cK \coloneqq \bigl\{\, [\omega] \in \nP^5 : p_{01}p_{23} - p_{02}p_{13} + p_{03}p_{12} = 0 \,\bigr\} ,
\]
the **Klein quadric**.
:::

::: {.idea}
\( (\Rightarrow) \) is an identity: substitute \( p_{ij} = u_iw_j - u_jw_i \) and watch twelve terms cancel in six pairs. \( (\Leftarrow) \) needs a way to produce the two vectors, and the right one is to look for them in a kernel. The map \( \v \mapsto \v\wedge\omega \) has a matrix, and pairing it against a second vector turns it into a bilinear form \( B(\v,\v')\,\e_{0123} = \v\wedge\v'\wedge\omega \) — which is alternating, because \( \v\wedge\v = \0 \). Two facts about alternating matrices then finish it: the determinant of a \( 4\times4 \) one is the square of its Pfaffian, which here is the left-hand side of @eq-plucker-relation, and the rank of an alternating matrix is even. A vanishing Pfaffian therefore drops the rank from \( 4 \) to \( 2 \), leaving a kernel of dimension \( 2 \), and the two vectors are there.
:::

::: {.proof}
\( (\Rightarrow) \) Suppose \( p_{ij} = u_iw_j - u_jw_i \). Expanding the three products,
\[
\begin{aligned}
p_{01}p_{23} &= u_0u_2w_1w_3 - u_0u_3w_1w_2 - u_1u_2w_0w_3 + u_1u_3w_0w_2 , \\
p_{02}p_{13} &= u_0u_1w_2w_3 - u_0u_3w_1w_2 - u_1u_2w_0w_3 + u_2u_3w_0w_1 , \\
p_{03}p_{12} &= u_0u_1w_2w_3 - u_0u_2w_1w_3 - u_1u_3w_0w_2 + u_2u_3w_0w_1 .
\end{aligned}
\]
Each of the six monomials appears in exactly two of the three lines, and forming \( p_{01}p_{23} - p_{02}p_{13} + p_{03}p_{12} \) cancels both copies every time. Monomial by monomial: \( u_0u_2w_1w_3 \) carries \( +1 \) in the first line and \( -1 \) in the third, contributing \( (+1) - 0 + (-1) = 0 \); \( u_0u_3w_1w_2 \) carries \( -1 \) in the first and \( -1 \) in the second, contributing \( (-1) - (-1) + 0 = 0 \); \( u_1u_2w_0w_3 \) likewise \( (-1) - (-1) + 0 = 0 \); \( u_1u_3w_0w_2 \) gives \( (+1) - 0 + (-1) = 0 \); \( u_0u_1w_2w_3 \) gives \( 0 - 1 + 1 = 0 \); and \( u_2u_3w_0w_1 \) gives \( 0 - 1 + 1 = 0 \). The total is \( 0 \). This direction used nothing about \( F \) and did not need \( \u\wedge\w \ne \0 \).

\( (\Leftarrow) \) Suppose \( \omega \ne \0 \) satisfies @eq-plucker-relation. Since \( \dim\Lambda^4F^4 = 1 \) with basis \( \e_{0123} \) (@cor-top-exterior-power-is-a-line), there is a unique scalar \( B(\v,\v') \) with
\[
\v\wedge\v'\wedge\omega = B(\v,\v')\,\e_{0123} ,
\]
where, expanding \( \omega \) in the basis, \( \v\wedge\v'\wedge\omega = \sum_{i<j} p_{ij}\,\v\wedge\v'\wedge\e_i\wedge\e_j \) is a combination of wedges of **four** vectors. So \( B \) is bilinear, the wedge being linear in each slot, and alternating: \( B(\v,\v)\e_{0123} = \v\wedge\v\wedge\omega = \0 \). Let \( \G \) be its matrix in the basis \( (\e_0,\e_1,\e_2,\e_3) \); by @prp-alternating-form-matrix (b), \( \G \) is an alternating matrix. Each entry is read off \( \e_a\wedge\e_b\wedge\e_i\wedge\e_j \), which is \( \pm\e_{0123} \) when \( \{a,b,i,j\} = \{0,1,2,3\} \) and \( \0 \) otherwise: for instance \( B(\e_0,\e_1) = p_{23} \) because only the term \( \e_0\wedge\e_1\wedge\e_2\wedge\e_3 = \e_{0123} \) survives, and \( B(\e_0,\e_2) = -p_{13} \) because \( \e_0\wedge\e_2\wedge\e_1\wedge\e_3 = -\e_{0123} \) by @lem-alternating-map-properties (a). In full,
\[
\G = \begin{pmatrix}
0 & p_{23} & -p_{13} & p_{12} \\
-p_{23} & 0 & p_{03} & -p_{02} \\
p_{13} & -p_{03} & 0 & p_{01} \\
-p_{12} & p_{02} & -p_{01} & 0
\end{pmatrix} .
\]
By @exm-pfaffian-small, a \( 4\times 4 \) alternating matrix with entries \( a, b, c, d, e, f \) above the diagonal, read in the order \( a_{12}, a_{13}, a_{14}, a_{23}, a_{24}, a_{34} \), has determinant \( (af - be + cd)^2 \). Here that reads
\[
\det\G = \bigl(p_{23}p_{01} - (-p_{13})(-p_{02}) + p_{12}p_{03}\bigr)^2 = 0
\]
by @eq-plucker-relation. So \( \rank\G \le 3 \), and \( \rank\G \) is **even** by @cor-alternating-even-rank (a), hence \( \rank\G \le 2 \).

Next, \( \operatorname{rad}(B) = \{\v : \v\wedge\omega = \0\} \). Indeed if \( \v\wedge\omega = \0 \) then \( B(\v,\v') = 0 \) for every \( \v' \). Conversely suppose \( \eta = \v\wedge\omega \ne \0 \) and write \( \eta = \sum_S c_S\e_S \) over the four \( 3 \)-element subsets \( S \subseteq \{0,1,2,3\} \), with some \( c_S \ne 0 \); let \( k \) be the index not in \( S \). Then \( \e_k\wedge\eta = \pm c_S\,\e_{0123} \ne \0 \), every other term having a repeated factor. Exchanging the first two arguments of a wedge of four vectors changes its sign (@lem-alternating-map-properties (a)), so \( \v\wedge\e_k\wedge\omega = -\,\e_k\wedge\v\wedge\omega = -\,\e_k\wedge\eta \ne \0 \), and therefore \( B(\v,\e_k) \ne 0 \). (The two one-sided radicals agree because \( B \) is alternating, hence skew-symmetric by @thm-alternating-vs-skew (a).)

By @prp-nondegenerate-iff-invertible (b), \( \dim\operatorname{rad}(B) = 4 - \rank\G \ge 2 \). Choose independent \( \u, \w \) with \( \u\wedge\omega = \w\wedge\omega = \0 \) and extend to a basis \( (\u,\w,\x,\y) \) of \( F^4 \) (@thm-basis-extension). By @thm-exterior-power-basis the six wedges of pairs from this basis form a basis of \( \Lambda^2F^4 \), so
\[
\omega = c_1\,\u\wedge\w + c_2\,\u\wedge\x + c_3\,\u\wedge\y + c_4\,\w\wedge\x + c_5\,\w\wedge\y + c_6\,\x\wedge\y .
\]
Wedging with \( \u \) kills the three terms containing \( \u \) and leaves
\[
\0 = \u\wedge\omega = c_4\,\u\wedge\w\wedge\x + c_5\,\u\wedge\w\wedge\y + c_6\,\u\wedge\x\wedge\y ,
\]
three distinct members of the basis of \( \Lambda^3F^4 \) given by @thm-exterior-power-basis, hence independent; so \( c_4 = c_5 = c_6 = 0 \). Wedging what remains with \( \w \),
\[
\0 = \w\wedge\omega = -c_2\,\u\wedge\w\wedge\x - c_3\,\u\wedge\w\wedge\y ,
\]
so \( c_2 = c_3 = 0 \). Hence \( \omega = c_1\,\u\wedge\w \) with \( c_1 \ne 0 \), and \( \omega = (c_1\u)\wedge\w \) is a wedge.

*The bijection.* If \( L \) is a line then \( [L] = [\u\wedge\w] \) satisfies @eq-plucker-relation by \( (\Rightarrow) \), and the relation is a homogeneous condition of degree \( 2 \), so it depends only on the point of \( \nP^5 \). Injectivity is @prp-plucker-well-defined (b). For surjectivity, let \( [\omega] \in \cK \). By \( (\Leftarrow) \), \( \omega = \u\wedge\w \), and \( \omega \ne \0 \) forces \( (\u,\w) \) independent by @thm-wedge-nonzero-iff-independent, so \( W = \Span(\u,\w) \) is \( 2 \)-dimensional and \( L = \nP(W) \) is a line with \( [L] = [\omega] \). This proves the theorem.
:::

::: {.remark}
Chapter 15 reaches the same equation by a different route, in @exr-grassmann-and-clifford-c1: there \( \omega\wedge\omega = 2\bigl(p_{01}p_{23} - p_{02}p_{13} + p_{03}p_{12}\bigr)\e_{0123} \), so in characteristic \( \ne 2 \) a decomposable \( \omega \), for which \( \omega\wedge\omega = \0 \), forces the bracket to vanish. That route is credited here, not used. The proof above stands on results proved in the text, and it needs no assumption on the characteristic, which the \( \omega\wedge\omega \) route does; @exr-conics-and-plucker-c2 develops the \( \omega\wedge\omega \) identity for its own sake.
:::

::: {.warning}
**Not every point of \( \nP^5 \) is a line.** The element \( \omega = \e_{01} + \e_{23} \) has \( p_{01} = p_{23} = 1 \) and all other coordinates \( 0 \), so the left-hand side of @eq-plucker-relation equals \( 1 \), and \( 1 \ne 0 \) in every field. It is therefore not a wedge, and \( [\omega] \notin \cK \). Six numbers are two too many to describe a line freely; the relation removes one dimension and the projective scaling another.
:::

When \( \operatorname{char} F \ne 2 \), the left-hand side of @eq-plucker-relation is a quadratic form on the \( 6 \)-dimensional space \( \Lambda^2F^4 \), so \( \cK \) is a projective quadric in \( \nP^5 \) in the exact sense of @def-projective-quadric. That is the sentence the section was built to reach: the set of all lines in three-dimensional space is itself a quadric, and everything proved about quadrics in the first half applies to it. Which quadric it is, @exr-conics-and-plucker-c2 works out: it computes the Gram matrix and finds the quadric smooth, with inertia \( (3,3,0) \) over \( \nR \). That computation is left to the exercise, and nothing here rests on it.

::: {#exm-plucker-line}
[A line, its Plücker point, and back]

Find the Plücker coordinates of the line \( L \) of \( \nP^3(\nQ) \) through \( [1:0:1:0] \) and \( [0:1:0:2] \), check the relation, and recover \( L \) from the coordinates.
:::

::: {.solution}
With \( \u = (1,0,1,0) \) and \( \w = (0,1,0,2) \), the six minors are
\[
\begin{aligned}
p_{01} &= 1, & p_{02} &= 0, & p_{03} &= 2, \\
p_{12} &= -1, & p_{13} &= 0, & p_{23} &= 2,
\end{aligned}
\]
so \( \u\wedge\w = \e_{01} + 2\e_{03} - \e_{12} + 2\e_{23} \). The relation holds:
\[
p_{01}p_{23} - p_{02}p_{13} + p_{03}p_{12} = 1\cdot 2 - 0\cdot 0 + 2\cdot(-1) = 0 .
\]
To go back, build the matrix \( \G \) of the proof:
\[
\G = \begin{pmatrix}
0 & 2 & 0 & -1 \\
-2 & 0 & 2 & 0 \\
0 & -2 & 0 & 1 \\
1 & 0 & -1 & 0
\end{pmatrix} ,
\]
whose rank is \( 2 \): row \( 3 \) is \( -1 \) times row \( 1 \) and row \( 4 \) is \( -\tfrac12 \) times row \( 2 \), while rows \( 1 \) and \( 2 \) are independent. Its null space is cut out by \( 2v_1 - v_3 = 0 \) and \( v_0 - v_2 = 0 \), that is, by \( v_2 = v_0 \) and \( v_3 = 2v_1 \), and is spanned by \( (1,0,1,0) \) and \( (0,1,0,2) \) — the two points we started from, as @prp-plucker-well-defined (b) promises.
:::

## Summary and transfer

The chapter began by removing the origin and ended by adding points at infinity, and both moves paid for themselves in theorems that have no exceptional cases. Four habits are worth carrying away.

**A geometry is a group acting on a set, and the invariants name the subject.** Affine maps preserve parallelism and ratios along a line; Euclidean motions preserve distance; projectivities preserve only incidence and the cross-ratio. Each time, the theorems of the geometry are exactly the statements its group cannot disturb, and the group was a matrix group in disguise: an \( (n+1)\times(n+1) \) block matrix for the affine group, an orthogonal matrix plus a translation for motions, and \( \GL(V) \) modulo scalars for projectivities.

**Adding points removes cases.** The affine formula for the dimension of a join needed two cases; its projective counterpart needs none. Two lines in a projective plane always meet. A quadratic form in three variables has one classification list, not a longer one split by whether a center exists. The extra points cost nothing, since \( \nP(V) \) is built from the same vector space.

**Choose the representative.** A point of \( \nP(V) \) is a line of vectors, and nearly every projective proof in this chapter began by picking one vector per point so that the hypothesis became an equation: \( \a' = \a + \o \) in Desargues, \( \u + t\o \) in Pappus, the normalized second intersection point in the conic parametrization. The choice is where the content is, and it is worth stating out loud each time which scalings are still free afterwards.

**Homogeneous means algebraic.** A condition that survives scaling is a condition on \( \nP(V) \): \( q(\x) = 0 \), the Plücker relation, membership of a subspace. That is why each of the objects in this chapter turned out to be the solution set of homogeneous polynomial equations — and the last of them, the Klein quadric, made the lines of \( \nP^3 \) into points of a quadric in \( \nP^5 \), so that a question about lines becomes a question about a symmetric matrix. Chapter 14's classification of forms and Chapter 15's exterior powers were the two tools that made it possible, and neither was built with geometry in mind.

What the chapter did **not** do is also worth recording. It developed no analysis of its own: no limits and no continuity arguments. The only topological words used inside a proof, in Section 3, are quoted from Chapters 16 and 18's theorems, and nothing is said about the topology of \( \nP^2(\nR) \), which is a subject of its own. Quadrics required \( \operatorname{char} F \ne 2 \) everywhere, as Chapter 14 warned they would; Desargues, Pappus and the Plücker correspondence did not. And the axiomatic side of projective geometry — planes not of the form \( \nP(V) \), coordinatization by division rings — was pointed at once, in Section 9, and proved nowhere.

## Exercises

### A. Check your understanding

::: {#exr-conics-and-plucker-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State @def-projective-quadric and say why the zero set is well defined on \( \nP(V) \).
2. Which invariant classifies quadrics over an algebraically closed field, and which over \( \nR \)?
3. List the five projective equivalence classes of conics in \( \nP^2(\nR) \) with their zero sets.
4. State the Plücker relation, and say what the six coordinates are the minors of.
5. True or false, with a reason: a smooth conic over \( \nR \) is never empty.
:::
:::

::: {.solution}
(a) The zero set \( Z(q) = \{[\x] : q(\x) = 0\} \) of a non-zero quadratic form \( q \), over a field of characteristic \( \ne 2 \). It is well defined because \( q(\lambda\x) = \lambda^2q(\x) \), so for \( \lambda \ne 0 \) one value is zero exactly when the other is.

(b) Rank alone over an algebraically closed field (@thm-projective-classification (a)); rank together with inertia up to interchanging \( n_+ \) and \( n_- \) over \( \nR \) (part (b) of the same theorem).

(c) By @cor-conics-in-the-projective-plane (b): \( (1,0) \) a line; \( (2,0) \) a point; \( (1,1) \) two distinct lines; \( (3,0) \) the empty set; \( (2,1) \) a smooth non-empty conic.

(d) \( p_{01}p_{23} - p_{02}p_{13} + p_{03}p_{12} = 0 \), where the \( p_{ij} \) are the six \( 2\times2 \) minors of the \( 4\times2 \) matrix whose columns are two points spanning the line.

(e) False. \( x_0^2 + x_1^2 + x_2^2 \) has rank \( 3 \), so its conic is smooth, and the zero set in \( \nP^2(\nR) \) is empty.
:::

### B. Practice

::: {#exr-conics-and-plucker-b1}
[B1: Classify these conics]

Classify each of the following conics of \( \nP^2 \) over \( \nR \) and over \( \nC \), giving the rank, the real inertia and the zero set. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( 2x_0x_1 + 2x_0x_2 + 2x_1x_2 = 0 \).
2. \( x_0^2 + 2x_0x_1 + x_1^2 = 0 \).
3. \( x_0^2 + 2x_0x_1 + x_1^2 + x_2^2 = 0 \).
:::
:::

::: {.solution}
(a) Put \( y_0 = x_0 + x_1 \) and \( y_1 = x_0 - x_1 \), so \( 2x_0x_1 = \tfrac12(y_0^2 - y_1^2) \) and \( 2x_0x_2 + 2x_1x_2 = 2y_0x_2 \). Then
\[
q = \tfrac12\bigl(y_0^2 + 4y_0x_2\bigr) - \tfrac12 y_1^2 = \tfrac12(y_0+2x_2)^2 - 2x_2^2 - \tfrac12 y_1^2 .
\]
The three forms \( y_0 + 2x_2 = x_0+x_1+2x_2 \), \( y_1 = x_0 - x_1 \) and \( x_2 \) are independent, the matrix with those rows having determinant \( -2 \). So the rank is \( 3 \) and the real inertia is \( (1,2,0) \), which is \( (2,1,0) \) after a sign change; by @cor-conics-in-the-projective-plane the zero set is a smooth non-empty conic over \( \nR \) and a smooth conic over \( \nC \). For instance \( [1:0:0] \) lies on it, every term of \( q \) having a factor \( x_1 \) or \( x_2 \).

(b) \( q = (x_0+x_1)^2 \), rank \( 1 \), inertia \( (1,0,2) \). The zero set is the line \( \{x_0 + x_1 = 0\} \) over either field.

(c) \( q = (x_0+x_1)^2 + x_2^2 \), rank \( 2 \), inertia \( (2,0,1) \). Over \( \nR \) the zero set is the single point \( [1:-1:0] \). Over \( \nC \) the form factors as \( (x_0+x_1+ix_2)(x_0+x_1-ix_2) \), so the zero set is two distinct lines.
:::

::: {#exr-conics-and-plucker-b2}
[B2: A conic through five points]

Find the conic of \( \nP^2(\nQ) \) through \( [1:0:0] \), \( [0:1:0] \), \( [0:0:1] \), \( [1:1:1] \) and \( [1:-1:2] \), verify that no three of the five points are collinear, and decide whether the conic is smooth.
:::

::: {.solution}
Write \( q = ax_0^2 + bx_1^2 + cx_2^2 + dx_0x_1 + ex_0x_2 + fx_1x_2 \). The three standard basis points give \( a = b = c = 0 \). Then \( [1:1:1] \) gives \( d + e + f = 0 \) and \( [1:-1:2] \) gives \( -d + 2e - 2f = 0 \). Adding, \( 3e - f = 0 \), so \( f = 3e \) and \( d = -e - f = -4e \). Taking \( e = 1 \),
\[
q = -4x_0x_1 + x_0x_2 + 3x_1x_2 .
\]
No three of the five are collinear: the determinants of the \( 3\times3 \) matrices formed by any three of the five coordinate vectors are, in the order \( 123 \), \( 124 \), \( 125 \), \( 134 \), \( 135 \), \( 145 \), \( 234 \), \( 235 \), \( 245 \), \( 345 \),
\[
1,\ 1,\ 2,\ -1,\ 1,\ 3,\ 1,\ 1,\ -1,\ -2 ,
\]
none of them zero.

The matrix is
\[
\A = \begin{pmatrix} 0 & -2 & 1/2 \\ -2 & 0 & 3/2 \\ 1/2 & 3/2 & 0\end{pmatrix},
\qquad \det\A = -3 \ne 0 ,
\]
so the conic is smooth, and by the argument of @exm-five-points (product of eigenvalues negative, trace zero) its real inertia is \( (2,1,0) \).
:::

::: {#exr-conics-and-plucker-b3}
[B3: Plücker coordinates]

::: {.enumerate options="label=(\alph*)"}
1. Compute the Plücker coordinates of the line of \( \nP^3(\nQ) \) through \( [1:1:0:0] \) and \( [0:0:1:1] \), and check @eq-plucker-relation.
2. Determine whether \( [\omega] \) with \( (p_{01},p_{02},p_{03},p_{12},p_{13},p_{23}) = (1,0,0,0,0,1) \) is the Plücker point of a line. Justify your answer.
3. The six numbers \( (1,1,0,0,-1,-1) \), in the same order, satisfy @eq-plucker-relation. Find the line they come from.
:::
:::

::: {.solution}
(a) With \( \u = (1,1,0,0) \) and \( \w = (0,0,1,1) \),
\[
\begin{aligned}
p_{01} &= 0, & p_{02} &= 1, & p_{03} &= 1, \\
p_{12} &= 1, & p_{13} &= 1, & p_{23} &= 0 ,
\end{aligned}
\]
and \( 0\cdot 0 - 1\cdot 1 + 1\cdot 1 = 0 \).

(b) No. The left-hand side of @eq-plucker-relation is \( 1\cdot 1 - 0 + 0 = 1 \ne 0 \), so by @thm-plucker-relation the element \( \e_{01} + \e_{23} \) is not a wedge and its point is not on the Klein quadric.

(c) First, \( 1\cdot(-1) - 1\cdot(-1) + 0\cdot 0 = 0 \), as stated. Build \( \G \) as in the proof of @thm-plucker-relation:
\[
\G = \begin{pmatrix}
0 & -1 & 1 & 0 \\
1 & 0 & 0 & -1 \\
-1 & 0 & 0 & 1 \\
0 & 1 & -1 & 0
\end{pmatrix} .
\]
Its null space is given by \( -v_1 + v_2 = 0 \) and \( v_0 - v_3 = 0 \), so it is spanned by \( (1,0,0,1) \) and \( (0,1,1,0) \). The line is the one through \( [1:0:0:1] \) and \( [0:1:1:0] \); as a check, its minors are \( p_{01}=1 \), \( p_{02}=1 \), \( p_{03}=0 \), \( p_{12}=0 \), \( p_{13}=-1 \), \( p_{23}=-1 \), as given.
:::

### C. Going deeper

::: {#exr-conics-and-plucker-c1}
[C1: All rational points of a circle]

Work in \( \nP^2(\nQ) \) with \( C = Z(x_0^2 + x_1^2 - x_2^2) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( C \) is smooth and that \( P_0 = [0:1:1] \) lies on it.
2. Using @thm-conic-parametrization with \( \ell = \{x_1 = 0\} \), compute the resulting parametrization of \( C \) explicitly.
3. Deduce that every solution of \( a^2 + b^2 = c^2 \) in integers with \( c \ne 0 \) is a rational multiple of \( (2uv,\ u^2 - v^2,\ u^2 + v^2) \) for some integers \( u, v \), and exhibit the triple obtained at \( [u:v] = [2:1] \).
:::
:::

::: {.solution}
(a) The matrix is \( \diag(1,1,-1) \), invertible, so \( C \) is smooth; and \( 0 + 1 - 1 = 0 \), so \( P_0 \in C \). Also \( P_0 \notin \ell \), since its \( x_1 \)-coordinate is \( 1 \ne 0 \).

(b) Here \( \p = (0,1,1) \) and \( \beta(\x,\y) = x_0y_0 + x_1y_1 - x_2y_2 \). A point of \( \ell \) is \( [u:0:v] \), with \( q(\x) = u^2 - v^2 \) and \( \beta(\p,\x) = -v \). So
\[
\begin{aligned}
\psi([u:0:v]) &= \bigl[-(u^2-v^2)(0,1,1) - 2v(u,0,v)\bigr] \\
&= \bigl[-2uv \ :\ v^2-u^2 \ :\ -u^2 - v^2\bigr] \\
&= \bigl[2uv \ :\ u^2 - v^2 \ :\ u^2+v^2\bigr] .
\end{aligned}
\]
Indeed \( (2uv)^2 + (u^2-v^2)^2 = (u^2+v^2)^2 \).

(c) Let \( a^2+b^2 = c^2 \) with \( a,b,c \) integers and \( c \ne 0 \). Then \( [a:b:c] \) is a point of \( C \) with rational coordinates, so by @thm-conic-parametrization it equals \( \psi([u:0:v]) \) for exactly one point of \( \ell \), which has rational, hence after clearing denominators integer, coordinates \( u, v \). Therefore \( (a,b,c) \) is a rational multiple of \( (2uv,\, u^2-v^2,\, u^2+v^2) \). At \( [u:v] = [2:1] \) this is \( (4, 3, 5) \).
:::

::: {#exr-conics-and-plucker-c2}
[C2: The Klein quadric]

Let \( \operatorname{char} F \ne 2 \), write \( Q(\omega) = p_{01}p_{23} - p_{02}p_{13} + p_{03}p_{12} \) for \( \omega \in \Lambda^2F^4 \), and let \( \beta_Q \) be the symmetric bilinear form with \( \beta_Q(\omega,\omega) = Q(\omega) \), which exists and is unique by @thm-polarization-forms.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \omega\wedge\omega = 2Q(\omega)\,\e_{0123} \) for every \( \omega \in \Lambda^2F^4 \), and deduce \( \omega\wedge\omega' = 2\beta_Q(\omega,\omega')\,\e_{0123} \).
2. Prove that two lines \( L, L' \) of \( \nP^3 \) meet if and only if \( \beta_Q([L],[L']) = 0 \), the value being computed from any representatives.
3. Compute the matrix of \( \beta_Q \) in the basis ordered \( (\e_{01}, \e_{23}, \e_{02}, \e_{13}, \e_{03}, \e_{12}) \). Deduce that \( Q \) has rank \( 6 \), so that the Klein quadric is smooth, and that over \( \nR \) its inertia is \( (3,3,0) \).
:::

*Hint: for (a), expand and note that only complementary pairs of index sets survive; the same computation appears in @exr-grassmann-and-clifford-c1 (a).*
:::

::: {.solution}
(a) Expanding \( \omega\wedge\omega = \sum_{S,T}p_Sp_T\,\e_S\wedge\e_T \) over \( 2 \)-element index sets, a term vanishes unless \( S \) and \( T \) are disjoint, so only the pairs \( \{01\},\{23\} \), \( \{02\},\{13\} \), \( \{03\},\{12\} \) and their reverses survive. A reversal does not change \( \e_S\wedge\e_T \) for \( \lvert S\rvert = \lvert T\rvert = 2 \): passing each of the two factors of \( \e_T \) across the two factors of \( \e_S \) costs four transpositions, and a permutation that is a product of four transpositions has sign \( +1 \) (@cor-parity-well-defined), so by @lem-alternating-map-properties (b) the value is unchanged. Sorting, \( \e_{01}\wedge\e_{23} = \e_{0123} \), \( \e_{02}\wedge\e_{13} = -\e_{0123} \) (one transposition) and \( \e_{03}\wedge\e_{12} = \e_{0123} \) (two). So \( \omega\wedge\omega = 2(p_{01}p_{23} - p_{02}p_{13} + p_{03}p_{12})\e_{0123} \).

For the second identity expand \( (\omega+\omega')\wedge(\omega+\omega') \) in two ways. Wedging is symmetric on \( 2 \)-vectors, by bilinearity and the remark just made, so the cross terms combine: \( 2Q(\omega+\omega')\e_{0123} = 2Q(\omega)\e_{0123} + 2\,\omega\wedge\omega' + 2Q(\omega')\e_{0123} \). Since \( \beta_Q(\omega,\omega') = \tfrac12\bigl(Q(\omega+\omega') - Q(\omega) - Q(\omega')\bigr) \) by @thm-polarization-forms, this rearranges to \( \omega\wedge\omega' = 2\beta_Q(\omega,\omega')\e_{0123} \).

(b) Write \( L = \nP(W) \), \( L' = \nP(W') \) with bases \( (\u,\w) \) and \( (\u',\w') \). By (a), \( \beta_Q = 0 \) on the pair exactly when \( \u\wedge\w\wedge\u'\wedge\w' = \0 \), which by @thm-wedge-nonzero-iff-independent happens exactly when \( (\u,\w,\u',\w') \) is dependent, that is, when \( \dim(W+W') \le 3 \). By @thm-dimension-formula-subspace-dim this says \( \dim(W\cap W') \ge 2+2-3 = 1 \), which says \( L \cap L' \ne \emptyset \). Rescaling a representative rescales \( \beta_Q \) by a non-zero factor, so vanishing does not depend on the choice.

(c) In that order the matrix is block diagonal with the three \( 2\times 2 \) blocks
\[
\begin{pmatrix} 0 & 1/2 \\ 1/2 & 0\end{pmatrix}, \qquad
\begin{pmatrix} 0 & -1/2 \\ -1/2 & 0\end{pmatrix}, \qquad
\begin{pmatrix} 0 & 1/2 \\ 1/2 & 0\end{pmatrix} ,
\]
since \( Q \) is a sum of three products of complementary coordinates. Each block has determinant \( -1/4 \ne 0 \), so the whole matrix is invertible and \( \rank Q = 6 \): the quadric is smooth. Over \( \nR \) each block has eigenvalues \( \pm 1/2 \), one positive and one negative, so the inertia is \( (3,3,0) \).
:::
