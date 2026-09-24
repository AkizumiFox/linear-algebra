# Desargues and Pappus

Two theorems from the drawing board, both of them older than coordinates. Both speak only of points, lines and incidence: no lengths, no angles, nothing a projective transformation could disturb. Both are proved here by one algebraic move, the one that makes projective arguments short — choosing, out of the whole line of vectors that represents a point, the single vector that makes the hypothesis into an equation.

## Perspective from a point, perspective from a line

Draw a triangle on a sheet of glass and let a lamp cast its shadow on the floor. The two triangles that result have their corresponding vertices joined by three lines through the lamp. That is the first of the two relations below. The second is what the same picture looks like when you attend to the sides instead of the vertices: corresponding sides, extended, meet the ground in three points, and those three points lie on one line.

Both relations need the words "the line through two points", and there is exactly one: distinct points \( A = [\a] \) and \( B = [\b] \) of \( \nP(V) \) have independent representatives and lie on the unique line \( \nP(\Span(\a,\b)) \), by @prp-two-points-determine-a-line. We write \( AB \) for it, and we use that description of it, as \( \nP(\Span(\a,\b)) \), in every proof below.

::: {#def-perspective-triangles}
[Triangles, and the Two Perspectives]

Let \( \dim V = 3 \), so that \( \nP(V) \) is a projective plane (@def-projective-subspace). A **triangle** in \( \nP(V) \) is an ordered triple \( (A, B, C) \) of **non-collinear** points, called its **vertices**; its **sides** are the three lines \( AB \), \( BC \), \( CA \).

Let \( (A,B,C) \) and \( (A',B',C') \) be triangles with \( A \ne A' \), \( B \ne B' \) and \( C \ne C' \). They are:

::: {.enumerate options="label=(\alph*)"}
1. **perspective from a point** if some point \( O \) lies on **all three** of the lines \( AA' \), \( BB' \), \( CC' \); such an \( O \) is a **center**;
2. **perspective from a line** if the three pairs of corresponding sides \( \{AB, A'B'\} \), \( \{BC, B'C'\} \), \( \{CA, C'A'\} \) consist of **distinct** lines and the three intersection points
\[
AB \cap A'B', \qquad BC \cap B'C', \qquad CA \cap C'A'
\]
are collinear; a line through all three is an **axis**.
:::
:::

In (b) each intersection is a single point: two **distinct** lines in a projective plane meet in exactly one point (@cor-two-lines-meet). That is why the clause "distinct in each pair" is part of the definition and not an afterthought; without it the phrase "the point \( AB \cap A'B' \)" names nothing.

\begin{center}
\begin{tikzpicture}[scale=0.62, lab/.style={font=\small}]
  \coordinate (O) at (-1,5);
  \coordinate (A) at (0,3);
  \coordinate (B) at (-3,-1);
  \coordinate (C) at (3,-1);
  \coordinate (Ap) at (-0.3333,3.6667);
  \coordinate (Bp) at (-2.75,-0.25);
  \coordinate (Cp) at (4.6,-3.4);
  \coordinate (R) at (-4.2,-2.6);
  \coordinate (P) at (-1,-1);
  \coordinate (Q) at (1.9091,0.4545);
  \draw[gray!60] (O) -- (0.4,2.2);
  \draw[gray!60] (O) -- (-3.3,-1.9);
  \draw[gray!60] (O) -- (4.95,-3.85);
  \draw[thick] (A) -- (R);
  \draw[thick] (B) -- (C);
  \draw[thick] (C) -- (A);
  \draw[thick,dashed] (Ap) -- (R);
  \draw[thick,dashed] (Bp) -- (Cp);
  \draw[thick,dashed] (Cp) -- (Ap);
  \draw[very thick,gray!80] (-4.9,-2.95) -- (2.7,0.85);
  \foreach \pt in {O,A,B,C,Ap,Bp,Cp,R,P,Q} \fill (\pt) circle (0.09);
  \node[lab,above] at (O) {$O$};
  \node[lab,above right] at (A) {$A$};
  \node[lab,left] at (B) {$B$};
  \node[lab,right] at (C) {$C$};
  \node[lab,right] at (Ap) {$A'$};
  \node[lab,above right] at (Bp) {$B'$};
  \node[lab,right] at (Cp) {$C'$};
  \node[lab,below left] at (R) {$R$};
  \node[lab,below] at (P) {$P$};
  \node[lab,above left] at (Q) {$Q$};
  \node[lab] at (3.6,1.3) {axis};
\end{tikzpicture}
\end{center}

The picture shows both relations at once: the three gray rays make the triangles perspective from \( O \), and the three marked points \( R = AB \cap A'B' \), \( P = BC \cap B'C' \), \( Q = CA \cap C'A' \) lie on the thick line. Desargues's theorem says that this coincidence is no coincidence.

::: {.warning}
**Two corresponding sides may be the same line, and then part (b) is not even a statement.** Take a line \( \ell \), four distinct points \( A, B, A', B' \) on it and a point \( O \) on it, and any \( C \notin \ell \). Fix representatives \( \o \) of \( O \) and \( \c \) of \( C \) and put \( C' = [\o + \c] \), a point of the line \( OC \) other than \( O \) and \( C \); it does not lie on \( \ell \), since \( OC \ne \ell \) and the two meet only at \( O \) (@cor-two-lines-meet). The triples \( (A,B,C) \) and \( (A',B',C') \) are triangles, the six vertices are distinct, and the three lines \( AA' \), \( BB' \), \( CC' \) all pass through \( O \). But \( AB = \ell = A'B' \), so "the point \( AB \cap A'B' \)" does not exist. @exr-desargues-and-pappus-c3 writes this out in coordinates. The hypothesis that rules it out is the one in the theorem below: no vertex of either triangle lies on a side of the other.
:::

## Choosing the representatives

A point of \( \nP(V) \) is a whole line of vectors, and every proof has to pick one vector per point. The pick is free, and freedom used well is the whole art. Here the hypothesis is three collinearities, and each of them becomes a clean equation as soon as the two representatives involved are scaled against each other.

::: {#lem-collinear-representatives}
[Scaling Three Collinear Points]

Let \( W \subseteq V \) be a \( 2 \)-dimensional subspace and let \( O, A, A' \) be three **distinct** points of the line \( \nP(W) \). Let \( \o \) be any non-zero vector representing \( O \). Then there are vectors \( \a \) representing \( A \) and \( \a' \) representing \( A' \) with
\[
\a' = \a + \o .
\]
:::

::: {.idea}
Two distinct points of a line give a basis of \( W \), so the third is a combination of them. Both coefficients are non-zero, precisely because the third point is neither of the first two; and scaling the two representatives by the right amounts turns that combination into a sum with coefficients \( 1 \) and \( 1 \).
:::

::: {.proof}
Pick any non-zero \( \a_0 \) representing \( A \). Since \( O \ne A \), the pair \( (\o, \a_0) \) is independent, and it lies in \( W \) with \( \dim W = 2 \), so it is a basis of \( W \). As \( A' \in \nP(W) \), a representative \( \a_0' \) of \( A' \) can be written
\[
\a_0' = \mu\,\a_0 + \nu\,\o , \qquad \mu, \nu \in F .
\]
Here \( \nu \ne 0 \): otherwise \( \a_0' = \mu\a_0 \) with \( \mu \ne 0 \), giving \( A' = A \). And \( \mu \ne 0 \): otherwise \( \a_0' = \nu\o \) with \( \nu \ne 0 \), giving \( A' = O \). Both are excluded because the three points are distinct.

Put \( \a \coloneqq (\mu/\nu)\,\a_0 \) and \( \a' \coloneqq (1/\nu)\,\a_0' \), which is legitimate since \( \mu/\nu \) and \( 1/\nu \) are non-zero scalars, so \( \a \) still represents \( A \) and \( \a' \) still represents \( A' \). Then
\[
\a' = \tfrac{1}{\nu}\bigl(\mu\a_0 + \nu\o\bigr) = \tfrac{\mu}{\nu}\a_0 + \o = \a + \o .
\]
This proves the lemma.
:::

It is @lem-projective-frame-normalization for \( n = 1 \), with the one common scalar spent on fixing \( \o \) first. The lemma is used three times in a row, always with the **same** \( \o \). That is the point: \( \o \) is chosen once and never rescaled again, while each pair \( (\a, \a') \), \( (\b, \b') \), \( (\c, \c') \) is scaled to match it.

::: {.check}
In the lemma, which conclusions survive if we drop the hypothesis \( A' \ne O \)? And if we drop \( A' \ne A \)?
:::

::: {.solution}
Neither survives. If \( A' = O \) we may take \( \a_0' = \o \), so \( \mu = 0 \); and the conclusion fails, because every representative \( \a' \) of \( A' = O \) is a multiple of \( \o \), so \( \a = \a' - \o \) would lie in \( \Span(\o) \), forcing \( \a = \0 \) or \( A = [\a] = O \), and both are impossible. If \( A' = A \) we may take \( \a_0' = \a_0 \), so \( \nu = 0 \), and \( \a' = \a + \o \) would say that two representatives of the same point \( A \) differ by \( \o \); subtracting, \( \o \) would be a multiple of \( \a \), making \( O = A \), again excluded. Each of the two scalars \( \mu, \nu \) is guarded by exactly one of the two hypotheses.
:::

## Desargues's theorem

The forward half of Desargues's theorem needs less than the full configuration, and stating it with its minimal hypotheses is what makes it reusable: the converse will apply it to a **different** pair of triangles built from the same picture.

::: {#lem-desargues-from-a-point}
[Perspective from a Point Gives an Axis]

Let \( \dim V = 3 \). Let \( (A,B,C) \) and \( (A',B',C') \) be triangles in \( \nP(V) \) with \( A \ne A' \), \( B \ne B' \), \( C \ne C' \), and suppose:

::: {.enumerate options="label=(\roman*)"}
1. some point \( O \), **distinct from all six vertices**, lies on each of \( AA' \), \( BB' \), \( CC' \);
2. \( AB \ne A'B' \), \( BC \ne B'C' \) and \( CA \ne C'A' \).
:::

Then the three points \( AB \cap A'B' \), \( BC \cap B'C' \), \( CA \cap C'A' \) are collinear.
:::

::: {.idea}
Fix one representative \( \o \) of \( O \). By @lem-collinear-representatives the three collinearities can be written as \( \a' = \a + \o \), \( \b' = \b + \o \), \( \c' = \c + \o \) for suitable representatives. Subtract two of them and \( \o \) cancels: \( \a - \b = \a' - \b' \). One vector, lying in \( \Span(\a,\b) \) and in \( \Span(\a',\b') \) at once, so its point lies on both \( AB \) and \( A'B' \). The three such vectors add to \( \0 \), so they span at most a plane; the triangles being genuine keeps them from collapsing to a line, so they span exactly a plane, and a plane of \( V \) is a line of \( \nP(V) \).
:::

::: {.proof}
Fix a non-zero \( \o \) representing \( O \). The points \( O, A, A' \) are distinct, by (i) and by \( A \ne A' \), and they are collinear, since \( O \in AA' \) and \( AA' = \nP(W) \) with \( \dim W = 2 \). So @lem-collinear-representatives gives representatives \( \a \) of \( A \) and \( \a' \) of \( A' \) with \( \a' = \a + \o \). The same lemma, with the **same** \( \o \), gives \( \b' = \b + \o \) and \( \c' = \c + \o \).

Subtracting, \( \a - \b = \a' - \b' \). Now \( \a - \b \ne \0 \), since \( \a = \b \) would give \( A = B \), contradicting that \( (A,B,C) \) is a triangle. Since \( \a - \b \in \Span(\a,\b) \) and \( AB = \nP(\Span(\a,\b)) \), the point \( [\a-\b] \) lies on \( AB \); since \( \a-\b = \a'-\b' \in \Span(\a',\b') \), it lies on \( A'B' \) as well. By (ii) these two lines are distinct, so by @cor-two-lines-meet they meet in exactly one point, and therefore
\[
AB \cap A'B' = [\a - \b] .
\]
The same argument, with the letters advanced cyclically, gives \( BC \cap B'C' = [\b - \c] \) and \( CA \cap C'A' = [\c - \a] \).

Let \( U = \Span(\a - \b,\ \b - \c,\ \c - \a) \). The three vectors sum to \( \0 \), so \( U = \Span(\a-\b,\ \b-\c) \) and \( \dim U \le 2 \). Moreover \( \dim U = 2 \): if \( \a - \b = t(\b - \c) \) for some \( t \in F \), then \( \a = (1+t)\b - t\c \in \Span(\b,\c) \), so \( A \) would lie on \( BC \), contradicting that \( (A,B,C) \) is a triangle; and \( \b - \c \ne \0 \) for the same reason as before. So \( \nP(U) \) is a line, and it contains all three points. This proves the lemma.
:::

Now the configuration of @def-perspective-triangles, with the one extra hypothesis that kept the warning above at bay.

::: {#thm-desargues}
[Desargues's Theorem]

Let \( \dim V = 3 \) and let \( (A,B,C) \) and \( (A',B',C') \) be triangles in \( \nP(V) \) such that

::: {.enumerate options="label=(\roman*)"}
1. the six vertices are distinct, and
2. no vertex of either triangle lies on a side of the other.
:::

Then the two triangles are perspective from a point if and only if they are perspective from a line.
:::

::: {.idea}
① The hypotheses (i) and (ii) are exactly what is needed to feed @lem-desargues-from-a-point: (ii) forces corresponding sides apart, and — less obviously — it also forces a center to miss all six vertices, because a center sitting on a vertex would drag a vertex of one triangle onto a side of the other. ② For the converse there is no second theorem to prove: the same lemma is applied to the auxiliary triangles \( (A,A',Q) \) and \( (B,B',P) \), which are perspective from \( R \) because the axis passes through \( R \). Their corresponding sides meet in \( AA'\cap BB' \), in \( C' \) and in \( C \); collinearity of those three puts \( AA'\cap BB' \) on the line \( CC' \), which is concurrency.
:::

::: {.proof}
Throughout, (ii) is used in the form: none of \( A, B, C \) lies on \( A'B' \), \( B'C' \) or \( C'A' \), and none of \( A', B', C' \) lies on \( AB \), \( BC \) or \( CA \).

First, the three pairs of corresponding sides are distinct. If \( AB = A'B' \) then \( A' \in AB \), contrary to (ii); the other two pairs are the same argument with the letters advanced.

\( (\Rightarrow) \) Suppose \( O \) lies on \( AA' \), \( BB' \), \( CC' \). We check that \( O \) is none of the six vertices. If \( O = A \), then \( A \in BB' \); since \( A \ne B \), the line through \( A \) and \( B \) is \( AB \), and it contains \( B' \), so \( B' \in AB \), contrary to (ii). If \( O = B \), then \( B \in AA' \) gives \( A' \in AB \) in the same way, and if \( O = C \) then \( C \in AA' \) gives \( A' \in CA \); both contradict (ii). If \( O = A' \), then \( A' \in BB' \); since \( A' \ne B' \), the line through them is \( A'B' \), and it contains \( B \), so \( B \in A'B' \), contrary to (ii). If \( O = B' \) then \( B' \in AA' \) gives \( A \in A'B' \), and if \( O = C' \) then \( C' \in AA' \) gives \( A \in C'A' \); both contradict (ii). So @lem-desargues-from-a-point applies, and its conclusion is that the two triangles are perspective from a line.

\( (\Leftarrow) \) Suppose the three points
\[
R = AB \cap A'B', \qquad P = BC \cap B'C', \qquad Q = CA \cap C'A'
\]
are collinear. We apply @lem-desargues-from-a-point to the triangles \( (A, A', Q) \) and \( (B, B', P) \), with center \( R \), and verify its hypotheses one at a time.

*The points \( Q \) and \( P \) are not vertices.* If \( Q = A \) then \( A \in C'A' \), and if \( Q = A' \) then \( A' \in CA \); both contradict (ii). Likewise \( P \ne B \) and \( P \ne B' \).

*Both triples are triangles.* Suppose \( A, A', Q \) were collinear. Since \( Q \in CA \) and \( Q \ne A \), the line \( QA \) is \( CA \); so \( AA' = QA = CA \), whence \( A' \in CA \), contrary to (ii). The triple \( (B, B', P) \) is handled the same way.

*Corresponding vertices are distinct.* \( A \ne B \) and \( A' \ne B' \) by (i). If \( Q = P \), that point lies on \( CA \) and on \( CB \); these two lines are distinct (else \( A, B, C \) would be collinear) and both contain \( C \), so by @cor-two-lines-meet they meet only at \( C \), giving \( Q = C \) and hence \( C \in C'A' \), contrary to (ii).

*The center \( R \) is none of the six vertices \( A, A', Q, B, B', P \).* If \( R = A \) then \( A \in A'B' \); if \( R = B \) then \( B \in A'B' \); if \( R = A' \) then \( A' \in AB \); if \( R = B' \) then \( B' \in AB \). All four contradict (ii). If \( R = Q \), then this point lies on \( AB \) and on \( CA \), two distinct lines through \( A \), so \( R = A \), already excluded; if \( R = P \), the same argument with \( AB \) and \( BC \) gives \( R = B \), also excluded.

*\( R \) lies on the three joins.* It lies on \( AB \) and on \( A'B' \) by definition. Since \( Q \ne P \), the line \( QP \) is defined, and it contains \( R \) because \( P, Q, R \) are collinear.

*Corresponding sides of the two auxiliary triangles are distinct.* If \( AA' = BB' \), this one line contains \( A \) and \( B \), hence equals \( AB \), and then \( A' \in AB \), contrary to (ii). Next, \( Q \in C'A' \) and \( Q \ne A' \) give \( A'Q = C'A' \), and \( P \in B'C' \) with \( P \ne B' \) give \( B'P = B'C' \); these are distinct, since \( C'A' = B'C' \) would make \( A', B', C' \) collinear. Finally \( QA = CA \) and \( PB = CB \), distinct for the same reason.

By @lem-desargues-from-a-point the three points
\[
\begin{aligned}
X &= AA' \cap BB', \\
A'Q \cap B'P &= C'A' \cap B'C' = C', \\
QA \cap PB &= CA \cap CB = C
\end{aligned}
\]
are collinear, the last two evaluations being @cor-two-lines-meet applied to two distinct lines with an evident common point. Since \( C \ne C' \) by (i), the line through \( C \) and \( C' \) is \( CC' \), and collinearity puts \( X \) on it. So \( X \) lies on \( AA' \), on \( BB' \) and on \( CC' \): the triangles are perspective from the point \( X \). This proves the theorem.
:::

Two routes to Desargues's theorem are standard. One embeds the plane in \( \nP^3 \), moves one triangle off the plane, and uses that two distinct planes of \( \nP^3 \) meet in a line; @exr-desargues-and-pappus-c1 carries that route out. The proof above is the other, purely two-dimensional route, and the step that decides whether it works is the scaling of @lem-collinear-representatives — one representative \( \o \) fixed first, every other representative matched to it afterwards.

::: {.remark}
The two halves of the theorem are dual statements: interchange "point" with "line", "lies on" with "passes through", and "perspective from a point" becomes "perspective from a line". Read through the correspondence of @thm-duality-correspondence, the converse should therefore be the dual of the direct half rather than an independent fact; **we do not carry that dualization out here**, and nothing depends on it. The proof above does not use it; it derives the converse from the direct half by applying it to a second pair of triangles, so that nothing rests on how far the duality principle of @thm-duality-principle can be pushed as a general statement.
:::

::: {#exm-desargues-in-coordinates}
[Desargues with exact coordinates]

In \( \nP^2(\nQ) \) take \( O = [1:1:1] \) and the triangle \( A = [1:0:0] \), \( B = [0:1:0] \), \( C = [0:0:1] \), and on the three lines through \( O \) take
\[
A' = [3:1:1], \qquad B' = [1:4:1], \qquad C' = [1:1:2] .
\]
Verify the hypotheses, scale the representatives as in the proof, and find the axis.
:::

::: {.solution}
Each primed point does lie on the corresponding line: \( (3,1,1) = 2(1,0,0) + (1,1,1) \), \( (1,4,1) = 3(0,1,0) + (1,1,1) \), and \( (1,1,2) = (0,0,1) + (1,1,1) \). Both triples are triangles, since \( (\e_0,\e_1,\e_2) \) is a basis and
\[
\det\begin{pmatrix} 3 & 1 & 1 \\ 1 & 4 & 1 \\ 1 & 1 & 2\end{pmatrix} = 17 \ne 0 .
\]
The six vertices are distinct. No vertex of either lies on a side of the other: the sides of \( ABC \) are the coordinate lines \( \{x_2 = 0\} \), \( \{x_0 = 0\} \), \( \{x_1 = 0\} \), and each primed point has all three coordinates non-zero; in the other direction the primed sides are
\[
\begin{aligned}
A'B' &= \{3x_0 + 2x_1 - 11x_2 = 0\}, \\
B'C' &= \{7x_0 - x_1 - 3x_2 = 0\}, \\
C'A' &= \{-x_0 + 5x_1 - 2x_2 = 0\},
\end{aligned}
\]
and no coefficient in any of them is zero, so none of \( \e_0, \e_1, \e_2 \) satisfies any of the three equations.

Now scale. With \( \o = (1,1,1) \) the relation \( \a_0' = 2\a_0 + \o \) has \( \mu = 2 \), \( \nu = 1 \), so the lemma takes \( \a = 2(1,0,0) = (2,0,0) \) and \( \a' = (3,1,1) \); similarly \( \b = (0,3,0) \), \( \b' = (1,4,1) \) and \( \c = (0,0,1) \), \( \c' = (1,1,2) \). Each check is one subtraction:
\[
\a' - \a = \b' - \b = \c' - \c = (1,1,1) = \o .
\]
The three intersection points are therefore
\[
\begin{aligned}
R &= [\a - \b] = [2:-3:0], \\
P &= [\b - \c] = [0:3:-1], \\
Q &= [\c - \a] = [-2:0:1],
\end{aligned}
\]
and indeed \( (2,-3,0) + (0,3,-1) + (-2,0,1) = \0 \). A linear form vanishing on the first two is \( 3x_0 + 2x_1 + 6x_2 \), and it vanishes on the third as well, so the axis is the line \( \{3x_0 + 2x_1 + 6x_2 = 0\} \).
:::

## Pappus's theorem

Desargues's theorem uses two triangles. Pappus's uses two lines, with three points on each, and concludes that three points built by cross-joining them lie on a line. Nothing is assumed about the two triples beyond being distinct and avoiding the one point the two lines share.

\begin{center}
\begin{tikzpicture}[scale=0.55, lab/.style={font=\small}]
  \coordinate (O) at (-5,0);
  \coordinate (A) at (-2,1.5);
  \coordinate (B) at (0,2.5);
  \coordinate (C) at (3,4);
  \coordinate (Ap) at (-1,-2);
  \coordinate (Bp) at (1,-3);
  \coordinate (Cp) at (4,-4.5);
  \coordinate (R) at (-0.6667,-0.5);
  \coordinate (Q) at (0,-0.5);
  \coordinate (P) at (1.7143,-0.5);
  \draw[gray!55] (A) -- (Bp);
  \draw[gray!55] (Ap) -- (B);
  \draw[gray!55] (A) -- (Cp);
  \draw[gray!55] (Ap) -- (C);
  \draw[gray!55] (B) -- (Cp);
  \draw[gray!55] (Bp) -- (C);
  \draw[thick] (O) -- (3.6,4.3);
  \draw[thick] (O) -- (4.5,-4.75);
  \draw[very thick,gray!85] (-1.6,-0.5) -- (2.7,-0.5);
  \foreach \pt in {O,A,B,C,Ap,Bp,Cp,R,Q,P} \fill (\pt) circle (0.1);
  \node[lab,left] at (O) {$O$};
  \node[lab,above left] at (A) {$A$};
  \node[lab,above left] at (B) {$B$};
  \node[lab,above left] at (C) {$C$};
  \node[lab,below left] at (Ap) {$A'$};
  \node[lab,below left] at (Bp) {$B'$};
  \node[lab,below left] at (Cp) {$C'$};
  \node[lab,below] at (R) {$R$};
  \node[lab,above right] at (Q) {$Q$};
  \node[lab,below] at (P) {$P$};
  \node[lab,above] at (3.2,1.0) {$\ell$};
  \node[lab,below] at (3.9,-2.6) {$m$};
\end{tikzpicture}
\end{center}

The six thin lines are the cross-joins; they meet in pairs at \( R \), \( Q \) and \( P \), and the theorem says those three points always lie on one line, the thick one.

::: {#thm-pappus}
[Pappus's Theorem]

Let \( \dim V = 3 \), let \( \ell \) and \( m \) be **distinct** lines of \( \nP(V) \) and let \( O \) be their common point. Let \( A, B, C \) be three **distinct** points of \( \ell \), none equal to \( O \), and let \( A', B', C' \) be three **distinct** points of \( m \), none equal to \( O \). Then the three points
\[
\begin{aligned}
R &= AB' \cap A'B, \\
Q &= AC' \cap A'C, \\
P &= BC' \cap B'C
\end{aligned}
\]
exist and are collinear.
:::

::: {.idea}
Coordinates, in the one basis the data offers: the common point \( O \) and one direction along each line. Every point of the configuration then costs a single parameter, each cross-join is a \( 2 \times 2 \) system, and the three answers come out as explicit vectors. What finishes the proof is not a determinant but an identity visible on the page: the vector for \( Q \) is the sum of the vectors for \( P \) and \( R \).
:::

::: {.proof}
Write \( \ell = \nP(U) \) and \( m = \nP(W) \) with \( \dim U = \dim W = 2 \). Since \( \ell \ne m \) we have \( U \ne W \) (@lem-projective-subspace-determines-subspace), and two distinct subspaces of the same dimension satisfy \( U \not\subseteq W \), so \( U + W \) strictly contains \( W \) and has dimension \( 3 = \dim V \). By the dimension formula @thm-dimension-formula-subspace-dim, \( \dim(U \cap W) = 2 + 2 - 3 = 1 \). Thus \( U \cap W = \Span(\o) \) for a non-zero \( \o \), and \( O = [\o] \) is the unique common point of \( \ell \) and \( m \).

Choose \( \u \in U \setminus \Span(\o) \) and \( \w \in W \setminus \Span(\o) \). Then \( (\o, \u) \) is a basis of \( U \) and \( (\o, \w) \) is a basis of \( W \), and \( (\u, \w, \o) \) is a basis of \( V \): it has three members and spans \( U + W = V \). Every point of \( \ell \) other than \( O \) is represented by a vector \( s\u + t\o \) with \( s \ne 0 \), hence, after dividing by \( s \), by exactly one vector of the form \( \u + t\o \); and likewise on \( m \). So there are scalars with
\[
\begin{aligned}
A &= [\u + a\o], & B &= [\u + b\o], & C &= [\u + c\o], \\
A' &= [\w + a'\o], & B' &= [\w + b'\o], & C' &= [\w + c'\o],
\end{aligned}
\]
where \( a, b, c \) are distinct and \( a', b', c' \) are distinct, because the representatives above are uniquely determined by the points.

*The three intersections exist.* The lines \( AB' \) and \( A'B \) are defined, since \( A \ne B' \) and \( A' \ne B \): a point of \( \ell \) other than \( O \) is not a point of \( m \), as \( \ell \cap m = \{O\} \). They are distinct: if \( AB' = A'B \), this line would contain \( A \) and \( B \), two distinct points of \( \ell \), hence be \( \ell \); then \( A' \in \ell \cap m = \{O\} \), contradicting \( A' \ne O \). So \( R = AB' \cap A'B \) is a single point (@cor-two-lines-meet), and the same argument gives \( Q \) and \( P \).

*Computing \( R \).* A vector in \( \Span(\u + a\o,\ \w + b'\o) \) has the form
\[
\lambda\u + \mu\w + (\lambda a + \mu b')\o ,
\]
and a vector in \( \Span(\w + a'\o,\ \u + b\o) \) has the form \( \lambda'\u + \mu'\w + (\lambda' b + \mu' a')\o \). A non-zero vector lying in both must have \( \lambda = \lambda' \) and \( \mu = \mu' \), the triple \( (\u,\w,\o) \) being a basis, and then
\[
\lambda a + \mu b' = \lambda b + \mu a'
\quad\Longleftrightarrow\quad
\lambda(a - b) = \mu(a' - b') .
\]
Taking \( \lambda = a' - b' \) and \( \mu = a - b \) solves it. The resulting vector is the same read in either span: in the first the coefficient of \( \o \) is \( (a'-b')a + (a-b)b' = aa' - bb' \), and in the second it is \( (a'-b')b + (a-b)a' = aa' - bb' \) as well. So
\[
\r = (a'-b')\,\u + (a-b)\,\w + (aa' - bb')\,\o
\]
lies on both lines, and it is non-zero since \( a \ne b \). The two lines being distinct, @cor-two-lines-meet makes \( [\r] \) their unique common point: \( R = [\r] \). Advancing the letters, \( Q = [\q] \) and \( P = [\p] \) with
\[
\begin{aligned}
\q &= (a'-c')\,\u + (a-c)\,\w + (aa' - cc')\,\o , \\
\p &= (b'-c')\,\u + (b-c)\,\w + (bb' - cc')\,\o .
\end{aligned}
\]

*The finish.* Comparing the three displayed vectors coordinate by coordinate in the basis \( (\u, \w, \o) \),
\[
\p + \r - \q = \0 .
\]
So \( \Span(\p, \q, \r) = \Span(\p, \r) \) has dimension at most \( 2 \), and it has dimension at least \( 1 \) since \( \r \ne \0 \). Any subspace of dimension \( 1 \) or \( 2 \) is contained in some \( 2 \)-dimensional subspace \( Z \) of \( V \), and then \( \nP(Z) \) is a line containing \( P \), \( Q \) and \( R \). This proves the theorem.
:::

The hypotheses did exactly three jobs, and it is worth saying which. That \( \ell \ne m \) gave the basis. That none of the six points is \( O \) let every one of them be written as \( \u + t\o \) or \( \w + t\o \) with the leading coefficient \( 1 \); a point equal to \( O \) has no such representative, and the parametrization would break down. That \( a, b, c \) are distinct and \( a', b', c' \) are distinct made the six cross-joins exist and the three vectors non-zero. Nothing else was needed — in particular the six points may interleave along their two lines in any order, and no further non-degeneracy hypothesis is required.

::: {.remark}
Over \( \nF_2 \) the theorem is vacuous: a projective line over \( \nF_2 \) has \( 2 + 1 = 3 \) points (@prp-projective-point-count), so after removing \( O \) only two remain and three distinct points \( A, B, C \) cannot be chosen. Over \( \nF_3 \) the hypotheses can just be met, and @exr-desargues-and-pappus-c2 checks the conclusion there by hand.
:::

::: {#exm-pappus-in-coordinates}
[Pappus with exact coordinates]

In \( \nP^2(\nQ) \) let \( \ell = \{x_1 = 0\} \) and \( m = \{x_0 = 0\} \), and take
\[
\begin{aligned}
A &= [1:0:0], & B &= [1:0:1], & C &= [1:0:2], \\
A' &= [0:1:0], & B' &= [0:1:1], & C' &= [0:1:3] .
\end{aligned}
\]
Find \( R \), \( Q \), \( P \) and the line through them.
:::

::: {.solution}
Here \( \o = \e_2 \), \( \u = \e_0 \), \( \w = \e_1 \), and the parameters are \( a = 0 \), \( b = 1 \), \( c = 2 \), \( a' = 0 \), \( b' = 1 \), \( c' = 3 \). The formulas of the proof give
\[
\begin{aligned}
\r &= (0-1)\e_0 + (0-1)\e_1 + (0-1)\e_2 = -(1,1,1), \\
\q &= (0-3)\e_0 + (0-2)\e_1 + (0-6)\e_2 = -(3,2,6), \\
\p &= (1-3)\e_0 + (1-2)\e_1 + (1-6)\e_2 = -(2,1,5),
\end{aligned}
\]
so \( R = [1:1:1] \), \( Q = [3:2:6] \), \( P = [2:1:5] \), and \( \p + \r - \q = \0 \) as it must be. A linear form vanishing at \( R \) and \( P \) is \( 4x_0 - 3x_1 - x_2 \), and \( 4\cdot 3 - 3\cdot 2 - 6 = 0 \), so all three lie on the line \( \{4x_0 - 3x_1 - x_2 = 0\} \).

As a check on the formulas, compute \( R \) directly: \( AB' \) is spanned by \( (1,0,0) \) and \( (0,1,1) \), so it is \( \{x_1 = x_2\} \); \( A'B \) is spanned by \( (0,1,0) \) and \( (1,0,1) \), so it is \( \{x_0 = x_2\} \). Their common point is \( [1:1:1] \).
:::

## What the two theorems measure

Both theorems have been proved here inside \( \nP(V) \) for a vector space \( V \) over a field \( F \), and the proofs used the field only through its arithmetic. It is worth recording what happens if either assumption is loosened, because the answers are among the most quoted facts in the subject — and because this book has built neither the tools to prove them nor the language to state them carefully.

::: {.remark}
An axiomatic **projective plane** is a set of points and lines satisfying incidence axioms, with no vector space given in advance. Hilbert's coordinatization theory attaches an algebraic system to such a plane and reads geometric axioms off it. Two results of that theory: Desargues's theorem holds in a plane exactly when the plane comes from a **division ring** — a field except that multiplication need not commute — and Pappus's theorem holds exactly when that division ring is **commutative**, hence a field. Consequently Pappus implies Desargues, a purely geometric implication first proved by Hessenberg; and there are non-Desarguesian planes, the Moulton plane being the standard example. None of this is proved here, and nothing in this book depends on it: we have not constructed division rings, and "projective plane" has meant \( \nP(V) \) throughout. The honest summary is that our proof of Pappus's theorem multiplied scalars in whatever order was convenient — and that commuting them is exactly what the general theory says cannot be dispensed with.
:::

## Exercises

### A. Check your understanding

::: {#exr-desargues-and-pappus-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define "perspective from a point" and "perspective from a line" for two triangles in a projective plane.
2. In @lem-collinear-representatives, which hypothesis makes \( \mu \ne 0 \) and which makes \( \nu \ne 0 \)?
3. State @thm-desargues, with both of its hypotheses on the configuration.
4. True or false, with a reason: in @thm-pappus the six points are required to be pairwise distinct.
5. Name the one place in the proof of @thm-pappus where the hypothesis \( \ell \ne m \) is used.
:::
:::

::: {.solution}
(a) @def-perspective-triangles: perspective from a point means some point lies on all three lines \( AA' \), \( BB' \), \( CC' \); perspective from a line means the three pairs of corresponding sides are pairs of distinct lines and their three intersection points are collinear.

(b) The hypothesis \( A' \ne O \) makes \( \mu \ne 0 \), and \( A' \ne A \) makes \( \nu \ne 0 \).

(c) Two triangles whose six vertices are distinct and with no vertex of either lying on a side of the other are perspective from a point if and only if they are perspective from a line.

(d) True, though it is stated in two pieces: \( A, B, C \) are required distinct and \( A', B', C' \) are required distinct, and no point of \( \ell \setminus \{O\} \) can equal a point of \( m \setminus \{O\} \), since \( \ell \cap m = \{O\} \). So all six are distinct.

(e) In the first paragraph, to get \( \dim(U \cap W) = 1 \) and hence the basis \( (\u, \w, \o) \). If \( \ell = m \) then \( U = W \) and there is no such basis.
:::

### B. Practice

::: {#exr-desargues-and-pappus-b1}
[B1: A Desargues configuration]

In \( \nP^2(\nQ) \) let \( O = [1:1:1] \), \( A = [1:0:0] \), \( B = [0:1:0] \), \( C = [0:0:1] \), and
\[
A' = [0:1:1], \qquad B' = [1:0:1], \qquad C' = [1:1:0] .
\]
Check that each primed point lies on the corresponding line through \( O \), scale the representatives as in @lem-desargues-from-a-point, and compute the axis.
:::

::: {.solution}
\( (0,1,1) = -(1,0,0) + (1,1,1) \), and similarly \( (1,0,1) = -(0,1,0) + (1,1,1) \) and \( (1,1,0) = -(0,0,1) + (1,1,1) \). In each case \( \mu = -1 \) and \( \nu = 1 \), so @lem-collinear-representatives takes \( \a = -\e_0 \), \( \a' = (0,1,1) \), and likewise \( \b = -\e_1 \), \( \b' = (1,0,1) \), \( \c = -\e_2 \), \( \c' = (1,1,0) \). Each difference \( \a' - \a \) is \( (1,1,1) \), as required.

Hence
\[
\begin{aligned}
AB \cap A'B' &= [\a - \b] = [-1:1:0], \\
BC \cap B'C' &= [\b - \c] = [0:-1:1], \\
CA \cap C'A' &= [\c - \a] = [1:0:-1],
\end{aligned}
\]
and the three vectors sum to \( \0 \). A linear form vanishing at the first two is \( x_0 + x_1 + x_2 \), which also vanishes at the third, so the axis is \( \{x_0 + x_1 + x_2 = 0\} \). (Both triples are triangles, since \( \det(\a'\mid\b'\mid\c') = 2 \ne 0 \).)
:::

::: {#exr-desargues-and-pappus-b2}
[B2: A Pappus configuration]

In \( \nP^2(\nQ) \) let \( \ell = \{x_1 = 0\} \) and \( m = \{x_0 = 0\} \), and take
\[
\begin{aligned}
A &= [1:0:1], & B &= [1:0:2], & C &= [1:0:4], \\
A' &= [0:1:1], & B' &= [0:1:3], & C' &= [0:1:4] .
\end{aligned}
\]
Compute \( R \), \( Q \), \( P \) and the line through them, and verify \( \p + \r - \q = \0 \).
:::

::: {.solution}
With \( \u = \e_0 \), \( \w = \e_1 \), \( \o = \e_2 \) the parameters are \( a = 1 \), \( b = 2 \), \( c = 4 \) and \( a' = 1 \), \( b' = 3 \), \( c' = 4 \). By the formulas in the proof of @thm-pappus,
\[
\begin{aligned}
\r &= (1-3)\e_0 + (1-2)\e_1 + (1-6)\e_2 = (-2,-1,-5), \\
\q &= (1-4)\e_0 + (1-4)\e_1 + (1-16)\e_2 = (-3,-3,-15), \\
\p &= (3-4)\e_0 + (2-4)\e_1 + (6-16)\e_2 = (-1,-2,-10) .
\end{aligned}
\]
Then \( \p + \r = (-3,-3,-15) = \q \), so \( \p + \r - \q = \0 \). The points are \( R = [2:1:5] \), \( Q = [1:1:5] \), \( P = [1:2:10] \). A linear form vanishing at \( R \) and \( Q \) is \( 5x_1 - x_2 \), and \( 5\cdot 2 - 10 = 0 \), so the three lie on \( \{5x_1 = x_2\} \).
:::

::: {#exr-desargues-and-pappus-b3}
[B3: Concurrency from collinearity]

In \( \nP^2(\nQ) \) let \( A = [1:0:0] \), \( B = [0:1:0] \), \( C = [0:0:1] \) and
\[
A' = [1:2:2], \qquad B' = [2:1:2], \qquad C' = [2:2:1] .
\]
Verify the hypotheses of @thm-desargues, then decide whether \( AA' \), \( BB' \), \( CC' \) are concurrent by computing the three points \( AB\cap A'B' \), \( BC \cap B'C' \), \( CA \cap C'A' \) and testing them for collinearity. Do **not** compute the three lines \( AA' \), \( BB' \), \( CC' \).
:::

::: {.solution}
Both triples are triangles: \( (\e_0,\e_1,\e_2) \) is a basis, and the determinant of the matrix with rows \( (1,2,2) \), \( (2,1,2) \), \( (2,2,1) \) equals \( 5 \ne 0 \). The six vertices are distinct. No vertex of \( ABC \) lies on a side of \( A'B'C' \), and conversely: the sides of \( ABC \) are the three coordinate lines and every primed point has all coordinates non-zero, while \( A'B' = \{2x_0 + 2x_1 - 3x_2 = 0\} \), \( B'C' = \{-3x_0 + 2x_1 + 2x_2 = 0\} \), \( C'A' = \{2x_0 - 3x_1 + 2x_2 = 0\} \), none of which is satisfied by \( \e_0 \), \( \e_1 \) or \( \e_2 \).

Now \( AB = \{x_2 = 0\} \), and a point of \( A'B' \) with \( x_2 = 0 \) satisfies \( 2x_0 + 2x_1 = 0 \), so \( AB \cap A'B' = [1:-1:0] \). Cyclically, \( BC \cap B'C' = [0:1:-1] \) and \( CA \cap C'A' = [-1:0:1] \). The three vectors sum to \( \0 \), so they are dependent and the points are collinear, on \( \{x_0 + x_1 + x_2 = 0\} \). By the \( (\Leftarrow) \) half of @thm-desargues the three lines \( AA' \), \( BB' \), \( CC' \) are therefore concurrent.
:::

### C. Going deeper

::: {#exr-desargues-and-pappus-c1}
[C1: Desargues in space]

Let \( \dim V = 4 \), so \( \nP(V) = \nP^3 \). Let \( (A,B,C) \) and \( (A',B',C') \) be triangles spanning **distinct** planes \( \Pi \) and \( \Pi' \) of \( \nP^3 \), with the six vertices distinct, and suppose a point \( O \notin \Pi \cup \Pi' \) lies on each of \( AA' \), \( BB' \), \( CC' \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( A \), \( B \), \( A' \), \( B' \) lie in one plane of \( \nP^3 \), and deduce that the lines \( AB \) and \( A'B' \) meet.
2. Prove that \( \Pi \cap \Pi' \) is a line.
3. Deduce that the three points \( AB \cap A'B' \), \( BC \cap B'C' \), \( CA \cap C'A' \) lie on that line, and so are collinear.
:::

*Hint: for (a), all four points lie on lines through \( O \); for (b), use the dimension formula for subspaces.*
:::

::: {.solution}
(a) Since \( O \notin \Pi \cup \Pi' \) and all six vertices lie in \( \Pi \cup \Pi' \), the point \( O \) is none of them; and \( A \ne A' \), \( B \ne B' \) because the six are distinct. Let \( \o \) represent \( O \). The points \( O, A, A' \) are distinct and collinear, so @lem-collinear-representatives gives representatives with \( \a' = \a + \o \), and the same \( \o \) gives \( \b' = \b + \o \). All four of \( \a, \b, \a', \b' \) then lie in \( Z = \Span(\o, \a, \b) \), of dimension at most \( 3 \), so the four points lie in the projective subspace \( \nP(Z) \), of dimension at most \( 2 \) — a plane or less. Subtracting, \( \a - \b = \a' - \b' \), a vector that is non-zero because \( A \ne B \) and that lies in \( \Span(\a,\b) \cap \Span(\a',\b') \); so \( [\a-\b] \) lies on both \( AB \) and \( A'B' \), and the two lines meet.

(b) \( \Pi = \nP(S) \) and \( \Pi' = \nP(S') \) with \( \dim S = \dim S' = 3 \) and \( S \ne S' \), inside a \( 4 \)-dimensional \( V \). Then \( S + S' = V \), so by @thm-dimension-formula-subspace-dim, \( \dim(S \cap S') = 3 + 3 - 4 = 2 \), and \( \nP(S \cap S') \) is a line.

(c) First, \( AB \ne A'B' \): otherwise \( A \) and \( A' \) would both lie in \( \Pi' \), hence so would the line \( AA' \) and the point \( O \) on it, contradicting \( O \notin \Pi \cup \Pi' \). Two distinct lines have at most one common point, since two distinct points determine their line (@prp-two-points-determine-a-line), and by (a) these two lines do meet; so \( AB \cap A'B' \) is a single point. It lies on \( AB \subseteq \Pi \) and on \( A'B' \subseteq \Pi' \), hence in \( \Pi \cap \Pi' \), which is the line of (b). The same holds for the other two points. Three points on one line are collinear.
:::

::: {#exr-desargues-and-pappus-c2}
[C2: Pappus over the two smallest fields]

::: {.enumerate options="label=(\alph*)"}
1. Prove that the hypotheses of @thm-pappus cannot be satisfied when \( F = \nF_2 \).
2. Over \( F = \nF_3 \), take \( \ell \), \( m \), \( \o \), \( \u \), \( \w \) as in the proof of @thm-pappus and the parameters \( a = a' = 0 \), \( b = b' = 1 \), \( c = c' = 2 \). Compute \( \r, \q, \p \) and exhibit a line containing all three points.
3. Explain why the choice of parameters in (b) is the only one available over \( \nF_3 \), up to renaming the points.
:::
:::

::: {.solution}
(a) A line of \( \nP^2(\nF_q) \) is \( \nP(U) \) with \( \dim U = 2 \), and \( U \setminus \{\0\} \) has \( q^2 - 1 \) vectors falling into \( (q^2-1)/(q-1) = q + 1 \) points (@prp-projective-point-count). For \( q = 2 \) a line has \( 3 \) points, so \( \ell \setminus \{O\} \) has only two, and three distinct points \( A, B, C \) of \( \ell \), none equal to \( O \), do not exist.

(b) With \( a=a'=0 \), \( b=b'=1 \), \( c=c'=2 \) the formulas give
\[
\begin{aligned}
\r &= (0-1)\u + (0-1)\w + (0-1)\o = (2,2,2), \\
\q &= (0-2)\u + (0-2)\w + (0-4)\o = (1,1,2), \\
\p &= (1-2)\u + (1-2)\w + (1-4)\o = (2,2,0),
\end{aligned}
\]
all read in \( \nF_3 \) and in the basis \( (\u,\w,\o) \). So \( R = [1:1:1] \), \( Q = [1:1:2] \), \( P = [1:1:0] \), and every one of them satisfies \( x_0 - x_1 = 0 \). That linear form defines a line, and the three points lie on it. As a check, \( \p + \r - \q = (2+2-1,\ 2+2-1,\ 0+2-2) = (0,0,0) \) in \( \nF_3 \).

(c) A line of \( \nP^2(\nF_3) \) has \( 3 + 1 = 4 \) points, so \( \ell \setminus \{O\} \) has exactly three, namely the ones with parameters \( 0, 1, 2 \); the same on \( m \). The three points \( A, B, C \) must therefore be those three in some order, and likewise \( A', B', C' \). Renaming amounts to permuting the parameters, which permutes \( P \), \( Q \), \( R \) and changes nothing about their collinearity.
:::

::: {#exr-desargues-and-pappus-c3}
[C3: Why the side hypothesis is there]

In \( \nP^2(\nQ) \) let
\[
\begin{aligned}
A &= [1:0:0], & B &= [0:1:0], & C &= [0:0:1], \\
A' &= [1:1:0], & B' &= [1:2:0], & C' &= [1:3:1],
\end{aligned}
\]
and let \( O = [1:3:0] \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( (A,B,C) \) and \( (A',B',C') \) are triangles with six distinct vertices, and that \( O \) lies on each of \( AA' \), \( BB' \), \( CC' \).
2. Prove that the two triangles are **not** perspective from a line, in the strict sense of @def-perspective-triangles.
3. Say which clause of hypothesis (ii) of @thm-desargues fails here.
:::
:::

::: {.solution}
(a) \( (\e_0,\e_1,\e_2) \) is a basis, so \( (A,B,C) \) is a triangle, and
\[
\det\begin{pmatrix} 1 & 1 & 0 \\ 1 & 2 & 0 \\ 1 & 3 & 1\end{pmatrix} = 1 \ne 0,
\]
so \( (A',B',C') \) is one too. The six coordinate vectors are pairwise non-proportional, so the vertices are distinct. Now \( A, A', O \) all have last coordinate \( 0 \), hence lie on the line \( \{x_2 = 0\} \), and so are collinear; the same for \( B, B', O \). Finally \( (1,3,1) = (0,0,1) + (1,3,0) \), so \( C' \) lies on the line through \( C \) and \( O \).

(b) The line \( AB \) is \( \{x_2 = 0\} \), since \( \e_0 \) and \( \e_1 \) span its underlying plane. The line \( A'B' \) is spanned by \( (1,1,0) \) and \( (1,2,0) \), an independent pair inside the same plane, so \( A'B' = \{x_2 = 0\} = AB \) as well. The pair \( \{AB, A'B'\} \) therefore does not consist of distinct lines, and clause (b) of @def-perspective-triangles fails at its first requirement: there is no point "\( AB \cap A'B' \)" to speak of, the intersection being a whole line.

(c) The clause that no vertex of one triangle lies on a side of the other. Here \( A' = [1:1:0] \) lies on \( AB = \{x_2 = 0\} \), and so do \( B' \) and \( O \).
:::
