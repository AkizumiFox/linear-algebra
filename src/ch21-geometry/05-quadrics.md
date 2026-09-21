# Affine and Euclidean Quadrics

Chapter 13 classified quadratic forms up to congruence, and the answer over \( \nR \) was the inertia. A curve like \( 5x^2 + 4xy + 5y^2 - 14x - 14y - 7 = 0 \) is not a quadratic form, though: it has linear terms and a constant, and its zero set does not pass through the origin. This section asks what the inertia classification becomes once the origin is given up, which is exactly the question affine geometry was built for. Two answers come out, one for affine changes of coordinates and one for the rigid motions of @def-euclidean-motion, and the difference between them is the difference between "it is an ellipse" and "its semi-axes are \( \sqrt7 \) and \( \sqrt3 \)".

## Where characteristic two bites

Everything in this section needs a field in which \( 2 \ne 0 \), and it is worth seeing why before any definition is written down.

A degree-two polynomial in \( x_1, \dots, x_n \) has a homogeneous quadratic part, and we want to write that part as \( \x\tp\A\x \) with \( \A \) **symmetric**, so that Chapter 13 applies to it. For a symmetric \( \A \) the coefficient of \( x_ix_j \) with \( i \ne j \) is \( a_{ij} + a_{ji} = 2a_{ij} \). Recovering \( a_{ij} \) from the polynomial means halving, which is the division by \( 1 + 1 \) that @thm-polarization-forms performs, and on which the uniqueness of the symmetric matrix attached to a quadratic form (@def-quadratic-form) depends.

Over \( \nF_2 \) the halving is not merely inconvenient; the target is not there. Every symmetric \( \A \in M_n(\nF_2) \) gives
\[
\x\tp\A\x = \sum_i a_{ii}x_i^2 + 2\sum_{i<j}a_{ij}x_ix_j = \sum_i a_{ii}x_i^2 ,
\]
and since \( a^2 = a \) for \( a \in \nF_2 \) and squaring is additive there, this is \( \bigl(\sum_i a_{ii}x_i\bigr)^2 \), the square of a **linear** form. So over \( \nF_2 \) no expression \( \x\tp\A\x \) with \( \A \) symmetric ever has an \( xy \) term, the polynomial \( xy \) is not of that shape at all, and the ones that are have already collapsed to squares of linear forms. There is nothing left to classify.

**So: throughout this section \( F \) is a field with \( \operatorname{char} F \ne 2 \)** (@def-characteristic), and from the affine classification onward \( F = \nR \). The hypothesis will be invoked by name at each of the three places where it does work: writing the linear part as \( 2\b\tp\x \), reading off a symmetric \( \A \), and solving for a center.

## The equation of a quadric

Fix an origin \( O \) and a basis of the direction space, which by @prp-choice-of-origin identifies the affine space \( \cA \) of dimension \( n \) with \( F^n \). Every polynomial of degree \( 2 \) in the resulting coordinates can then be written in one standard shape.

*A quadric is what you get when a quadratic form is allowed to forget where the origin is.*

::: {#def-quadric}
[Quadric]

Let \( \operatorname{char} F \ne 2 \) and let \( \cA \) be an affine space of dimension \( n \) over \( F \), identified with \( F^n \) by a choice of origin and basis (@prp-choice-of-origin). A **quadric polynomial** on \( \cA \) is a function
\[
Q(\x) = \x\tp\A\x + 2\b\tp\x + c
\]
with \( \A \in M_n(F) \) **symmetric and non-zero**, \( \b \in F^n \) and \( c \in F \). Its **quadratic part** is the quadratic form \( q(\x) = \x\tp\A\x \). The **quadric** defined by \( Q \) is its zero set
\[
\{\, \x \in F^n : Q(\x) = 0 \,\} .
\]
For \( n = 2 \) a quadric is called a **conic**.
:::

Read the clauses. "**Symmetric**" is a normalization, not a restriction: \( \x\tp\A\x = \x\tp\A\tp\x \) because a \( 1 \times 1 \) matrix equals its transpose, so \( \A \) may always be replaced by \( \tfrac12(\A + \A\tp) \), and once symmetric it is determined by \( q \) (@thm-polarization-forms). "**Non-zero**" excludes \( \A = \0 \), where \( Q \) would be affine and its zero set a flat (@def-flat) already handled in Section 2; it is the clause that makes the object genuinely quadratic. The factor \( 2 \) in \( 2\b\tp\x \) is a convention we may adopt because \( 2 \) is invertible: a linear part \( \beta_1x_1 + \dots + \beta_nx_n \) is \( 2\b\tp\x \) with \( b_i = \beta_i/2 \). It pays for itself in every formula below.

**The data are recoverable from the function.** @def-quadric calls \( Q \) a function, so before speaking of "its" quadratic part or "its" constant we must check that \( \A \), \( \b \) and \( c \) are determined by \( Q \). They are, over any field of characteristic \( \ne 2 \). First \( Q(\0) = c \). Next
\[
Q(\x) - Q(-\x) = 4\b\tp\x \qquad \text{for every } \x \in F^n ,
\]
and \( 4 = 2\cdot 2 \ne 0 \), so taking \( \x = \e_i \) recovers \( b_i \) for each \( i \). Finally \( \x\tp\A\x = Q(\x) - 2\b\tp\x - c \) is then determined as a function of \( \x \), and a **symmetric** \( \A \) is determined by that quadratic form (@thm-polarization-forms). So the triple \( (\A, \b, c) \) is unique.

**Examples.** Over \( \nR \) with \( n = 2 \):

- \( x^2 + y^2 - 1 \), with \( \A = \I_2 \), \( \b = \0 \), \( c = -1 \): the unit circle.
- \( x^2 - y \), with \( \A = \diag(1, 0) \), \( \b = (0, -\tfrac12) \), \( c = 0 \): a parabola. Here the halving convention is visible, and \( \A \) is singular.
- \( x^2 + y^2 \): the zero set is the single point \( \0 \), although the polynomial has degree \( 2 \).
- \( x^2 \): the zero set is the line \( x = 0 \), traced "twice" in the sense that \( \A = \diag(1,0) \) has rank \( 1 \) and the polynomial is a square. This is the degenerate case, and it matters because the classification must find room for it.
- \( x^2 + y^2 + 1 \): the zero set is **empty**. Over \( \nR \) a quadric may have no points at all, and the classification below has two different normal forms whose zero sets are both empty.

**Non-example by minimal change.** Replace \( x^2 + y^2 - 1 \) by \( x^4 + y^2 - 1 \): the quadratic part is no longer a quadratic form, and there is no \( \A \). Replace it instead by \( 2x + 3y - 1 \): now \( \A = \0 \), the clause "non-zero" fails, and the zero set is a line, not a quadric.

::: {.warning}
**A quadric is classified through its polynomial, not through its point set.** Over \( \nR \) the polynomials \( x^2 + y^2 + 1 \) and \( x^2 + 1 \) both have empty zero set, and no coordinate change can be expected to tell empty from empty; yet the two polynomials will land in different classes below, and rightly so, because their behavior over \( \nC \) and their intersections with lines differ. Everything in the affine classification below is a statement about the polynomial \( Q \) up to an invertible affine substitution and a non-zero scalar factor. When the zero set determines \( Q \) up to a scalar it will be said explicitly.
:::

## The matrix of a quadric

The whole point of writing the linear part as \( 2\b\tp\x \) is that \( Q \) then becomes a single quadratic form in one extra variable. Write
\[
\tilde\x = \begin{pmatrix} \x \\ 1 \end{pmatrix} \in F^{n+1},
\qquad
\widetilde{\A} = \begin{pmatrix} \A & \b \\ \b\tp & c \end{pmatrix} \in M_{n+1}(F) ,
\]
so that \( \widetilde\A \) is symmetric and
\[
\tilde\x\tp\widetilde\A\,\tilde\x = \x\tp\A\x + \x\tp\b + \b\tp\x + c = Q(\x) ,
\]
the two middle terms being equal because each is a \( 1 \times 1 \) matrix and one is the transpose of the other. We call \( \widetilde\A \) the **big matrix** of \( Q \) and \( \A \) its **small matrix**. The extra coordinate is the same trick that turned an affine map into an \( (n+1) \times (n+1) \) block matrix in @prp-affine-map-block-matrix, and the two devices fit together exactly.

::: {#prp-quadric-congruence}
[Affine Substitution Is Congruence of the Big Matrix]

Let \( Q \) have big matrix \( \widetilde\A \), let \( \M \in M_n(F) \) be invertible, let \( \t \in F^n \), and let \( g(\y) = \M\y + \t \) be the corresponding invertible affine map (@def-affine-map), with block matrix (@prp-affine-map-block-matrix)
\[
\widehat{g} = \begin{pmatrix} \M & \t \\ \0\tp & 1 \end{pmatrix} .
\]
Then \( Q \circ g \) is again a quadric polynomial, its big matrix is \( \widehat{g}\tp\widetilde\A\widehat{g} \), and its small matrix, linear vector and constant are
\[
\A' = \M\tp\A\M, \qquad \b' = \M\tp(\A\t + \b), \qquad c' = Q(\t) .
\]
:::

::: {.proof}
By @prp-affine-map-block-matrix, \( \widehat{g}\,\tilde\y = \bigl(\M\y + \t,\, 1\bigr) = \widetilde{g(\y)} \). Hence
\[
Q(g(\y)) = \widetilde{g(\y)}\tp\widetilde\A\,\widetilde{g(\y)}
= \tilde\y\tp\bigl(\widehat{g}\tp\widetilde\A\widehat{g}\bigr)\tilde\y ,
\]
and \( \widehat{g}\tp\widetilde\A\widehat{g} \) is symmetric, being a congruence of a symmetric matrix (@prp-congruence-preserves-symmetry). Multiplying the blocks out,
\[
\begin{aligned}
\begin{pmatrix} \M\tp & \0 \\ \t\tp & 1\end{pmatrix}
\begin{pmatrix} \A & \b \\ \b\tp & c\end{pmatrix}
\begin{pmatrix} \M & \t \\ \0\tp & 1\end{pmatrix}
&= \begin{pmatrix} \M\tp\A & \M\tp\b \\ \t\tp\A + \b\tp & \t\tp\b + c\end{pmatrix}
\begin{pmatrix} \M & \t \\ \0\tp & 1\end{pmatrix} \\
&= \begin{pmatrix} \M\tp\A\M & \M\tp(\A\t + \b) \\ (\A\t + \b)\tp\M & \t\tp\A\t + 2\b\tp\t + c\end{pmatrix},
\end{aligned}
\]
where the bottom-left block was transposed using \( \A\tp = \A \). Reading off the blocks gives \( \A' \), \( \b' \) and \( c' = \t\tp\A\t + 2\b\tp\t + c = Q(\t) \). Finally \( \A' = \M\tp\A\M \) is non-zero, since \( \M \) is invertible and congruence preserves rank (@thm-congruence-preserves-rank), so \( Q \circ g \) is a quadric polynomial. This proves the proposition.
:::

Three consequences are worth naming at once. The new constant is \( Q \) evaluated at the new origin — obvious in hindsight, since \( \y = \0 \) means \( \x = \t \). The new small matrix is a congruence of the old one, so **the rank of \( \A \) is an affine invariant of \( Q \)** by @thm-congruence-preserves-rank, and over \( \nR \) **so is its inertia** by @cor-real-symmetric-classification (b) — the latter only up to the simultaneous exchange of \( n_+ \) with \( n_- \) that a negative scalar factor forces, as Step 4 of the classification theorem below records. And \( \widetilde\A \) itself only undergoes congruences by matrices whose last row is \( (\0\tp, 1) \), which is a strictly smaller set than all congruences: that restriction is exactly why the affine classification is finer than Chapter 13's.

Replacing \( Q \) by \( \lambda Q \) with \( \lambda \ne 0 \) does not change the zero set and replaces \( \widetilde\A \) by \( \lambda\widetilde\A \), so a scalar factor costs nothing geometrically and is worth allowing alongside the substitution.

::: {#def-affine-equivalence}
[Affine Equivalence of Quadric Polynomials]

Two quadric polynomials \( Q_1, Q_2 \) on \( F^n \) are **affinely equivalent** when
\[
Q_2 = \lambda\,(Q_1 \circ g)
\]
for some invertible affine map \( g \) (@def-affine-map) and some \( \lambda \in F \) with \( \lambda \ne 0 \).
:::

This is an equivalence relation, because the invertible affine maps form a group and the non-zero scalars do too.

## Centers

A circle has a center and a parabola does not, and the difference is visible in the equation before any picture is drawn.

*A center is a point about which the equation is symmetric.*

::: {#def-centre}
[Center of a Quadric]

Let \( Q \) be a quadric polynomial on \( F^n \). A point \( \p \in F^n \) is a **center** of \( Q \) if
\[
Q(\p + \v) = Q(\p - \v) \qquad \text{for every } \v \in F^n .
\]
\( Q \) is **central** if it has at least one center, and **centerless** otherwise.
:::

In words: reflecting in \( \p \), the map \( \p + \v \mapsto \p - \v \), carries the quadric to itself, and more than that, leaves the whole polynomial unchanged. The next proposition turns this into a linear system.

::: {#prp-centre-exists-iff}
[When a Center Exists]

Let \( \operatorname{char} F \ne 2 \) and let \( Q(\x) = \x\tp\A\x + 2\b\tp\x + c \) be a quadric polynomial on \( F^n \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \p \) is a center of \( Q \) if and only if \( \A\p + \b = \0 \);
2. \( Q \) is central if and only if \( \b \in \col(\A) \); in particular \( Q \) is central whenever \( \A \) is invertible, and the center is then the unique point \( -\A^{-1}\b \);
3. if \( \p \) is a center then \( Q(\p + \v) = Q(\p) + \v\tp\A\v \) for every \( \v \), and the value \( Q(\p) \) is the same at every center.
:::
:::

::: {.idea}
Expand \( Q(\p \pm \v) \) and subtract. Everything even in \( \v \) cancels and what is left is \( 4\v\tp(\A\p + \b) \), a linear functional of \( \v \). A linear functional vanishes identically exactly when its vector vanishes, so the condition on \( \p \) is one linear equation per coordinate. The \( 4 \) is where \( \operatorname{char} F \ne 2 \) is spent.
:::

::: {.proof}
(a) Expanding and using \( \A\tp = \A \), so that \( \p\tp\A\v = \v\tp\A\p \),
\[
Q(\p \pm \v) = \p\tp\A\p \pm 2\v\tp\A\p + \v\tp\A\v + 2\b\tp\p \pm 2\b\tp\v + c .
\]
Subtracting the two,
\[
Q(\p+\v) - Q(\p-\v) = 4\v\tp\A\p + 4\b\tp\v = 4\,\v\tp(\A\p + \b) .
\]{#eq-center-difference}
Since \( \operatorname{char} F \ne 2 \), the element \( 4 = 2 \cdot 2 \) is non-zero. So \( \p \) is a center exactly when \( \v\tp(\A\p+\b) = 0 \) for every \( \v \). Taking \( \v = \e_i \) shows that this forces every entry of \( \A\p + \b \) to vanish; conversely \( \A\p + \b = \0 \) makes @eq-center-difference zero for every \( \v \). Hence (a).

(b) By (a), a center is a solution of \( \A\p = -\b \), and such a solution exists exactly when \( -\b \), equivalently \( \b \), lies in \( \col(\A) \) (@thm-matrix-times-vector-columns). If \( \A \) is invertible then \( \col(\A) = F^n \) and \( \p = -\A^{-1}\b \) is the only solution.

(c) With \( \A\p + \b = \0 \), the expansion above with the sign \( + \) reads
\[
Q(\p + \v) = \bigl(\p\tp\A\p + 2\b\tp\p + c\bigr) + 2\v\tp(\A\p + \b) + \v\tp\A\v = Q(\p) + \v\tp\A\v .
\]
If \( \p' \) is a second center then \( \A(\p' - \p) = (-\b) - (-\b) = \0 \), so putting \( \v = \p' - \p \) in the last identity gives \( Q(\p') = Q(\p) + \v\tp\A\v = Q(\p) + \v\tp\0 = Q(\p) \). This proves the proposition.
:::

Part (c) is the useful half. Translating the origin to a center — that is, applying @prp-quadric-congruence with \( \M = \I \) and \( \t = \p \) — gives \( \b' = \A\p + \b = \0 \), so the equation becomes \( \v\tp\A\v + Q(\p) = 0 \) with no linear term at all, and Chapter 13 applies verbatim. That single move is the engine of the classification.

::: {#exm-parabola-has-no-centre}
[The parabola is centerless]

Show that \( Q(x,y) = x^2 - y \) over \( \nR \) has no center, and find all centers of \( Q_1(x,y) = x^2 - 1 \).
:::

::: {.solution}
For \( Q \), \( \A = \diag(1,0) \) and \( \b = (0, -\tfrac12) \). Then \( \col(\A) = \Span(\e_1) \) and \( \b \notin \col(\A) \) because its second entry is non-zero, so by @prp-centre-exists-iff (b) there is no center. Concretely, \( Q(\p + \v) - Q(\p - \v) = 4\v\tp(\A\p + \b) = 4(v_1p_1 - \tfrac12 v_2) \), which is \( -2 \ne 0 \) at \( \v = \e_2 \) whatever \( \p \) is.

For \( Q_1 \), \( \A = \diag(1,0) \) and \( \b = \0 \in \col(\A) \), so the centers are the solutions of \( \A\p = \0 \), namely the whole \( y \)-axis. That is right: \( Q_1 \) defines the pair of lines \( x = \pm1 \), and reflecting in any point of the \( y \)-axis swaps them. And \( Q_1(\p) = -1 \) at every one of those centers, as @prp-centre-exists-iff (c) promises.
:::

::: {.check}
A quadric polynomial on \( F^n \) with \( \rank\A = n \) has exactly one center, and one with \( \rank\A = n - 1 \) has either none or a whole line of them. Which is it for \( x^2 + y^2 - 2x \) on \( \nR^2 \), and which for \( x^2 + 2y \)?
:::

::: {.solution}
For \( x^2 + y^2 - 2x \) we have \( \A = \I_2 \) of rank \( 2 \) and \( \b = (-1, 0) \), so the unique center is \( -\A^{-1}\b = (1,0) \); indeed the curve is the circle \( (x-1)^2 + y^2 = 1 \). For \( x^2 + 2y \) we have \( \A = \diag(1,0) \) of rank \( 1 \) and \( \b = (0,1) \notin \col(\A) = \Span(\e_1) \), so there is no center at all: it is a parabola. The line of centers occurs instead for \( x^2 - 1 \), where \( \b = \0 \) does lie in \( \col(\A) \).
:::

## The affine classification over the reals

Now the theorem. Over \( \nR \) we may diagonalize the small matrix by Sylvester (@cor-real-symmetric-classification), translate to kill as much of the linear part as a center allows, and then scale. What survives is a short list.

::: {#thm-affine-classification-of-quadrics}
[Affine Classification of Real Quadrics]

Let \( Q(\x) = \x\tp\A\x + 2\b\tp\x + c \) be a quadric polynomial on \( \nR^n \) and let \( r = \rank\A \), which is \( \ge 1 \) because \( \A \ne \0 \) (@def-quadric). Then \( Q \) is affinely equivalent to **exactly one** polynomial from the following list, for one value of \( p \) in the range shown, where \( \sigma_{r,p}(\y) = y_1^2 + \dots + y_p^2 - y_{p+1}^2 - \dots - y_r^2 \):

::: {.enumerate options="label=(\Roman*)"}
1. \( \sigma_{r,p}(\y) - 1 \), with \( 0 \le p \le r \);
2. \( \sigma_{r,p}(\y) \), with \( r \le 2p \le 2r \);
3. \( \sigma_{r,p}(\y) - y_{r+1} \), with \( r < n \) and \( r \le 2p \le 2r \).
:::

Case (III) occurs exactly when \( Q \) is centerless. The parameter \( p \) that occurs is \( n_+(\A) \) or \( n_-(\A) \), the two being interchanged by a negative scalar factor (@def-signature).
:::

::: {.idea}
Three moves, in this order, and each is a result already proved.

① **Diagonalize the quadratic part.** Sylvester's law (@cor-real-symmetric-classification) produces coordinates in which the quadratic part is \( \sigma_{r,p} \); by @prp-quadric-congruence this changes \( \b \) and \( c \) but nothing else.

② **Complete the square in the first \( r \) variables.** A translation kills the linear coefficients \( b_1, \dots, b_r \), because those are exactly the coordinates in which \( \A \) is invertible. This is @prp-centre-exists-iff read one coordinate at a time.

③ **Deal with what is left,** a polynomial \( \sigma_{r,p} + 2\sum_{i>r}b_iy_i + c \) in which the \( y_i \) with \( i > r \) appear only linearly. If they do not appear at all, scaling clears the constant to \( 0 \) or \( -1 \), giving (II) or (I). If one of them does appear, it can be used as a new coordinate that swallows the constant too, giving (III).

That the list has no repetitions is a separate, purely computational matter: the pair (inertia of \( \A \), inertia of \( \widetilde\A \)) is an affine invariant by @prp-quadric-congruence, and reading it off the three families separates them.
:::

::: {.proof}
**Step 1: diagonalize.** Write \( (p, r-p, n-r) \) for the inertia of \( \A \) (@def-signature); this \( p \) is the one carried through Steps 1 to 3. By @cor-real-symmetric-classification (a) there is an invertible \( \M_1 \) with \( \M_1\tp\A\M_1 = \D \), where \( \D = \diag(\epsilon_1, \dots, \epsilon_n) \) has \( \epsilon_i = 1 \) for \( i \le p \), \( \epsilon_i = -1 \) for \( p < i \le r \) and \( \epsilon_i = 0 \) for \( i > r \). Substituting \( \x = \M_1\y \) and applying @prp-quadric-congruence with \( \t = \0 \), the polynomial becomes
\[
Q_1(\y) = \sigma_{r,p}(\y) + 2\b_1\tp\y + c, \qquad \b_1 = \M_1\tp\b .
\]

**Step 2: complete the square.** Let \( \t \) have entries \( t_i = -\epsilon_i b_{1,i} \) for \( i \le r \) and \( t_i = 0 \) for \( i > r \), and substitute \( \y = \z + \t \). By @prp-quadric-congruence with \( \M = \I \), the new linear vector is \( \b_2 = \D\t + \b_1 \), whose \( i \)-th entry for \( i \le r \) is \( \epsilon_it_i + b_{1,i} = -\epsilon_i^2b_{1,i} + b_{1,i} = 0 \), since \( \epsilon_i^2 = 1 \) there; for \( i > r \) it is \( b_{1,i} \), unchanged. The new constant is \( c_2 = Q_1(\t) \). So
\[
Q_2(\z) = \sigma_{r,p}(\z) + 2\sum_{i>r}b_{1,i}z_i + c_2 .
\]

**Step 3, Case A: \( b_{1,i} = 0 \) for every \( i > r \).** Then \( Q_2 = \sigma_{r,p} + c_2 \).

*If \( c_2 = 0 \)*, this is \( \sigma_{r,p} \). If \( r \le 2p \) we are in case (II). Otherwise multiply by \( \lambda = -1 \) and reverse the order of the first \( r \) coordinates, which turns \( \sigma_{r,p} \) into \( \sigma_{r,\,r-p} \) with \( r \le 2(r-p) \); again case (II).

*If \( c_2 \ne 0 \)*, substitute \( z_i = \lvert c_2\rvert^{1/2}w_i \) for \( i \le r \) and \( z_i = w_i \) otherwise, an invertible linear change, and then multiply by \( \lambda = 1/\lvert c_2\rvert \). The result is \( \sigma_{r,p}(\w) + \sgn(c_2) \). If \( \sgn(c_2) = -1 \) this is case (I) with parameter \( p \). If \( \sgn(c_2) = +1 \), multiply by \( -1 \) and reverse the order of the first \( r \) coordinates to get \( \sigma_{r,\,r-p} - 1 \), case (I) with parameter \( r - p \).

**Step 3, Case B: \( b_{1,i} \ne 0 \) for some \( i > r \).** Here \( r < n \). Put \( \c = (b_{1,r+1}, \dots, b_{1,n}) \ne \0 \) in \( \nR^{n-r} \). Extend \( 2\c \) to a basis of \( \nR^{n-r} \) (@thm-basis-extension) and let \( \N \in M_{n-r}(\nR) \) be the invertible matrix whose **first row** is \( 2\c\tp \) and whose remaining rows complete it to an invertible matrix; such rows exist because a basis of \( \nR^{n-r} \) written as rows forms an invertible matrix. Define new coordinates by
\[
u_i = z_i \ (i \le r), \qquad
(u_{r+1}, \dots, u_n)\tp = \N(z_{r+1}, \dots, z_n)\tp + c_2\,\e_1 ,
\]
an invertible affine substitution, under which \( u_{r+1} = 2\c\tp(z_{r+1},\dots,z_n) + c_2 \). Hence \( Q_2 = \sigma_{r,p}(\u) + u_{r+1} \). Replacing \( u_{r+1} \) by \( -y_{r+1} \) and keeping the other coordinates gives \( \sigma_{r,p}(\y) - y_{r+1} \). If \( r > 2p \), multiply by \( -1 \), reverse the order of the first \( r \) coordinates and replace \( y_{r+1} \) by \( -y_{r+1} \); the result is \( \sigma_{r,\,r-p}(\y) - y_{r+1} \) with \( r \le 2(r-p) \). Either way we reach case (III).

**Step 4: the list has no repetitions.** By @prp-quadric-congruence an affine equivalence replaces \( \A \) by \( \lambda\M\tp\A\M \) and \( \widetilde\A \) by \( \lambda\widehat{g}\tp\widetilde\A\widehat{g} \), with \( \M \) and \( \widehat{g} \) invertible. A congruence preserves inertia (@cor-real-symmetric-classification (b)), and multiplying a real symmetric matrix by \( \lambda \) leaves the inertia alone if \( \lambda > 0 \) and exchanges \( n_+ \) with \( n_- \) if \( \lambda < 0 \). Hence the **invariant pair**
\[
\begin{aligned}
&\bigl(\operatorname{In}\A,\ \operatorname{In}\widetilde\A\bigr), \\
&\quad \text{taken up to exchanging } n_+ \text{ with } n_- \\
&\quad \text{in both entries simultaneously},
\end{aligned}
\]
in which \( \operatorname{In} \) is the inertia triple of @def-inertia-triple, is an invariant of the affine equivalence class. Write \( \D_{r,p} = \diag(\epsilon_1, \dots, \epsilon_n) \) for the small matrix shared by all three families. In family (I) the linear vector is \( \0 \) and the constant is \( -1 \), so \( \widetilde\A = \D_{r,p} \oplus (-1) \); in family (II) the constant is \( 0 \), so \( \widetilde\A = \D_{r,p} \oplus 0 \). In family (III) the linear vector is \( -\tfrac12\e_{r+1} \) and the constant is \( 0 \), so \( \widetilde\A \) is diagonal except in the four positions indexed by \( r+1 \) and \( n+1 \), where it carries the block \( \begin{psmallmatrix} 0 & -\tfrac12 \\ -\tfrac12 & 0\end{psmallmatrix} \), whose eigenvalues are \( \tfrac12 \) and \( -\tfrac12 \); the remaining diagonal entries are \( \epsilon_1, \dots, \epsilon_r \) and \( n-r-1 \) zeros. So
\[
\begin{aligned}
\text{(I)}: &\quad \operatorname{In}\A = (p,\, r-p,\, n-r), &&\operatorname{In}\widetilde\A = (p,\, r-p+1,\, n-r); \\
\text{(II)}: &\quad \operatorname{In}\A = (p,\, r-p,\, n-r), &&\operatorname{In}\widetilde\A = (p,\, r-p,\, n-r+1); \\
\text{(III)}: &\quad \operatorname{In}\A = (p,\, r-p,\, n-r), &&\operatorname{In}\widetilde\A = (p+1,\, r-p+1,\, n-r-1).
\end{aligned}
\]
Therefore \( \rank\A = r \) in all three, while \( \rank\widetilde\A \) is \( r+1 \), \( r \) and \( r+2 \) respectively. Ranks are unaffected by the exchange of \( n_+ \) and \( n_- \), so the pair \( (\rank\A, \rank\widetilde\A) \) already determines both the family and \( r \).

It remains to separate two members of one family with the same \( r \). If the invariants agree without the exchange, then \( \operatorname{In}\A \) gives \( p = p' \) at once. Suppose instead they agree after the exchange, so that \( p' = r - p \).

*Family (I).* The exchanged \( \operatorname{In}\widetilde\A \) of the \( p \)-member is \( (r-p+1,\, p,\, n-r) \), while the \( p' \)-member has \( (p',\, r-p'+1,\, n-r) = (r-p,\, p+1,\, n-r) \). Comparing first entries gives \( r-p+1 = r-p \), which is false. So family (I) has no repetitions.

*Families (II) and (III).* Here both members satisfy \( r \le 2p \) and \( r \le 2p' = 2(r-p) \), that is \( 2p \le r \). Hence \( 2p = r = 2p' \) and \( p = p' \).

So distinct entries of the list are affinely inequivalent, and Step 3 showed every \( Q \) meets one. The normal form reached has small matrix \( \D_{r,p} \), of inertia \( (p,\, r-p,\, n-r) \); since \( \operatorname{In}\A \) is preserved by affine equivalence up to the exchange of \( n_+ \) with \( n_- \), that \( p \) is \( n_+(\A) \) or \( n_-(\A) \), as claimed. Finally, \( Q \) is centerless exactly in case (III): by @prp-centre-exists-iff (b) centrality is the condition \( \b \in \col(\A) \), which is preserved by affine equivalence because centers are (if \( \p \) is a center of \( Q \) and \( g \) is invertible affine, then \( g^{-1}(\p) \) is a center of \( \lambda\,Q\circ g \), since \( \v \mapsto \M\v \) is a bijection of \( \nR^n \)); and \( \0 \) is a center in cases (I) and (II), while in case (III) the small matrix is \( \D_{r,p} \) and the linear vector is \( -\tfrac12\e_{r+1} \notin \col(\D_{r,p}) = \Span(\e_1,\dots,\e_r) \). This proves the theorem.
:::

### The nine real conics

For \( n = 2 \) the parameters run over \( r \in \{1,2\} \) and \( 0 \le p \le r \), and the list has nine entries. Here they are, with the zero set of each. The last column records the classical names, and so does the paragraph on \( n = 3 \) below; those names are not defined anywhere in this book, and each set-theoretic reading is a one-line check from the normal form — for instance \( x^2 + y^2 = -1 \) has no real solution because a sum of squares is non-negative, and \( x^2 - y^2 = 0 \) is the pair of lines \( y = \pm x \), by factoring.

| Normal form | \( (r, p) \) | Family | \( \operatorname{In}\A \) | \( \operatorname{In}\widetilde\A \) | Zero set |
|---|---|---|---|---|---|
| \( x^2 + y^2 = 1 \) | \( (2,2) \) | I | \( (2,0,0) \) | \( (2,1,0) \) | ellipse |
| \( x^2 - y^2 = 1 \) | \( (2,1) \) | I | \( (1,1,0) \) | \( (1,2,0) \) | hyperbola |
| \( x^2 + y^2 = -1 \) | \( (2,0) \) | I | \( (2,0,0) \) | \( (3,0,0) \) | empty |
| \( x^2 + y^2 = 0 \) | \( (2,2) \) | II | \( (2,0,0) \) | \( (2,0,1) \) | one point |
| \( x^2 - y^2 = 0 \) | \( (2,1) \) | II | \( (1,1,0) \) | \( (1,1,1) \) | two crossing lines |
| \( x^2 = 1 \) | \( (1,1) \) | I | \( (1,0,1) \) | \( (1,1,1) \) | two parallel lines |
| \( x^2 = -1 \) | \( (1,0) \) | I | \( (1,0,1) \) | \( (2,0,1) \) | empty |
| \( x^2 = 0 \) | \( (1,1) \) | II | \( (1,0,1) \) | \( (1,0,2) \) | one line |
| \( x^2 = y \) | \( (1,1) \) | III | \( (1,0,1) \) | \( (2,1,0) \) | parabola |

Two rows of the table are written with the parameter \( p \) of the negated polynomial: \( x^2 + y^2 = -1 \) means \( -x^2 - y^2 - 1 = 0 \), which is \( \sigma_{2,0} - 1 \) after multiplying by \( -1 \), and likewise for \( x^2 = -1 \). Reading the two inertia columns up to a simultaneous exchange of the first two entries confirms that no two rows agree: rows 1, 3, 4 have \( \operatorname{In}\A = (2,0,0) \) and differ in \( \operatorname{In}\widetilde\A \); rows 2 and 5 differ in \( \operatorname{In}\widetilde\A \); and rows 6, 7, 8, 9 have \( \operatorname{In}\A = (1,0,1) \) with four different \( \operatorname{In}\widetilde\A \). In each of those two groups the exchange changes \( \operatorname{In}\A \), so it cannot rescue a match. The one group where \( \operatorname{In}\A \) survives the exchange is rows 2 and 5, with \( \operatorname{In}\A = (1,1,0) \); there \( \operatorname{In}\widetilde\A \) is \( (1,2,0) \) against \( (1,1,1) \), and the exchanged forms \( (2,1,0) \) and \( (1,1,1) \) still disagree.

Rows 3 and 7 are the honest surprise: both zero sets are empty, and both are needed, because the polynomials are not affinely equivalent. Over \( \nC \) they are quite different objects. Row 7 is \( x^2 + 1 = (x - i)(x + i) \), a pair of distinct lines, while row 3 has an invertible small matrix. @exr-quadrics-c2 (a) below classifies affine quadrics over \( \nC \), where rank alone is the invariant and the two rows stay apart: row 3 has \( \rank\A = 2 \) and \( \rank\widetilde\A = 3 \), row 7 has \( 1 \) and \( 2 \). Read projectively, Section 10's rank criterion makes row 3 a smooth conic.

For \( n = 3 \) the same count gives \( 4 + 7 + 6 = 17 \) normal forms. The new shapes are the ellipsoid \( x^2+y^2+z^2 = 1 \), the hyperboloids of one and two sheets \( x^2+y^2-z^2 = \pm1 \), the cone \( x^2+y^2-z^2=0 \), the elliptic and hyperbolic paraboloids \( x^2 \pm y^2 = z \), and the three cylinders \( x^2+y^2=1 \), \( x^2-y^2=1 \), \( x^2=y \), which are the conics of the table dragged along the missing coordinate. The rest are a pair of intersecting planes, a pair of parallel planes, a double plane, a line, a point and three empty sets.

::: {.warning}
**The rank of \( \widetilde\A \) does not classify; the inertia does.** The ellipse \( x^2+y^2-1 \), the hyperbola \( x^2-y^2-1 \) and the empty conic \( x^2+y^2+1 \) all have \( \rank\A = 2 \) and \( \rank\widetilde\A = 3 \). Their small matrices already differ in inertia in the hyperbola's case, and the ellipse and the empty conic are told apart only by \( \operatorname{In}\widetilde\A = (2,1,0) \) against \( (3,0,0) \). A count of non-zero eigenvalues cannot distinguish a curve from nothing at all.
:::

## Euclidean quadrics and principal axes

Affine equivalence forgets shape: every ellipse is affinely a circle. To keep shape, restrict the allowed substitutions to the Euclidean motions of \( \nR^n \), which by @thm-motion-is-affine are exactly the maps \( \x = \U\y + \t \) with \( \U \in \Orth(n) \); that theorem gives one direction, and the other is that such a map preserves distances, since \( \U \) preserves norms (@thm-isometry-characterizations). Call two quadric polynomials **Euclidean equivalent** when one is \( Q \circ g \) for such a \( g \). Note that no scalar factor is allowed now, and that is deliberate: a scalar factor would rescale the lengths we are trying to measure.

The gain is immediate. Under \( \x = \U\y + \t \) the small matrix becomes \( \U\tp\A\U \), which is both a congruence and a **similarity**, since \( \U\tp = \U^{-1} \). So the eigenvalues of \( \A \), not merely their signs, are Euclidean invariants. This is the observation Chapter 11 made in @thm-principal-axes, and the classification below is that theorem with the origin allowed to move.

::: {#thm-euclidean-classification}
[Euclidean Classification of Real Quadrics]

Let \( Q(\x) = \x\tp\A\x + 2\b\tp\x + c \) be a quadric polynomial on \( \nR^n \), let \( r = \rank\A \), and let \( \lambda_1, \dots, \lambda_r \) be the non-zero eigenvalues of \( \A \), listed with multiplicity. Then there is a Euclidean motion \( \x = \U\y + \t \), with \( \U \in \Orth(n) \), after which \( Q \) becomes exactly one of

::: {.enumerate options="label=(\alph*)"}
1. \( \lambda_1y_1^2 + \dots + \lambda_ry_r^2 + c_0 \), when \( Q \) is central, where \( c_0 = Q(\p) \) at any center \( \p \);
2. \( \lambda_1y_1^2 + \dots + \lambda_ry_r^2 + 2\mu\,y_{r+1} \), when \( Q \) is centerless, where \( \mu = \norm{\b - P_{\col(\A)}\b} > 0 \).
:::

The columns of \( \U \) are an orthonormal basis of eigenvectors of \( \A \), the first \( r \) of them for \( \lambda_1, \dots, \lambda_r \); these are the **principal axes** of \( Q \). The multiset \( \{\lambda_1, \dots, \lambda_r\} \) and the number \( c_0 \), respectively \( \mu \), are unchanged by every Euclidean motion, so the normal form is unique up to the order of its terms.
:::

::: {.idea}
The spectral theorem replaces Step 1 of @thm-affine-classification-of-quadrics, and it is the only change: instead of scaling the eigenvalues away to \( \pm1 \) we keep them, because an orthogonal matrix is not allowed to rescale. Steps 2 and 3 then go through with one adjustment. In Step 3 we may no longer stretch a coordinate to absorb \( \c \); instead we **rotate** the last \( n - r \) coordinates so that \( \c \) points along one of them, which is legitimate because those coordinates carry the eigenvalue \( 0 \) and a rotation among them leaves the quadratic part untouched.
:::

::: {.proof}
**Step 1.** By @cor-spectral-real-matrix there is \( \U_1 \in \Orth(n) \) with \( \U_1\tp\A\U_1 = \D = \diag(\lambda_1, \dots, \lambda_n) \), the eigenvalues of \( \A \) with multiplicity, and we order the basis so that \( \lambda_1, \dots, \lambda_r \) are the non-zero ones; the count is right because \( \D \) is similar to \( \A \), so \( \rank\D = \rank\A = r \), and a diagonal matrix has rank equal to its number of non-zero entries. Substituting \( \x = \U_1\y \) and using @prp-quadric-congruence with \( \t = \0 \) gives
\[
Q_1(\y) = \sum_{i=1}^{r}\lambda_iy_i^2 + 2\b_1\tp\y + c, \qquad \b_1 = \U_1\tp\b .
\]

**Step 2.** Translate by \( \t_1 \) with entries \( -b_{1,i}/\lambda_i \) for \( i \le r \) and \( 0 \) otherwise, which is legitimate because those \( \lambda_i \) are non-zero. As in @thm-affine-classification-of-quadrics, Step 2, the new linear vector has \( i \)-th entry \( \lambda_it_{1,i} + b_{1,i} = 0 \) for \( i \le r \) and \( b_{1,i} \) for \( i > r \). Write \( \c = (b_{1,r+1}, \dots, b_{1,n}) \) and \( c' \) for the new constant, so
\[
Q_2(\z) = \sum_{i=1}^{r}\lambda_iz_i^2 + 2\c\tp(z_{r+1},\dots,z_n) + c' .
\]

*Claim: \( \c = \0 \) if and only if \( Q \) is central, and in general \( \norm\c = \norm{\b - P_{\col(\A)}\b} \).* The last \( n - r \) columns \( \q_{r+1}, \dots, \q_n \) of \( \U_1 \) are an orthonormal basis of the eigenspace of \( \A \) for \( 0 \), that is of \( \nul(\A) \), and the entries of \( \c \) are \( \q_i\tp\b = \inner{\b}{\q_i} \). By @thm-four-subspaces-orthogonal (b) applied to the self-adjoint operator \( \x \mapsto \A\x \), we have \( \col(\A) = \nul(\A)^{\perp} \), so by @thm-orthogonal-decomposition the component of \( \b \) in \( \nul(\A) \) is \( \b - P_{\col(\A)}\b \), and by @thm-orthonormal-coordinates its norm is \( \norm{\c} \). Hence \( \c = \0 \) exactly when \( \b \in \col(\A) \), which is centrality by @prp-centre-exists-iff (b). This proves the claim.

**Step 3, central case.** Here \( \c = \0 \), so \( Q_2 = \sum_{i\le r}\lambda_iz_i^2 + c' \), which is form (a). The new origin \( \p \) satisfies \( \A\p + \b = \0 \) by @prp-centre-exists-iff (a), because the linear part has vanished, so \( \p \) is a center and \( c' = Q(\p) = c_0 \) by @prp-quadric-congruence; @prp-centre-exists-iff (c) says the value does not depend on which center.

**Step 3, centerless case.** Here \( \c \ne \0 \). By @cor-extend-orthonormal-basis the unit vector \( \c/\norm\c \) extends to an orthonormal basis of \( \nR^{n-r} \); let \( \R \in \Orth(n-r) \) have that basis as its columns, so \( \R\e_1 = \c/\norm{\c} \) and therefore \( \R\tp\c = \norm{\c}\,\e_1 \). Put \( \U_2 = \I_r \oplus \R \), which lies in \( \Orth(n) \). Substituting \( \z = \U_2\w \) leaves the quadratic part alone, since
\[
\begin{aligned}
\U_2\tp\bigl(\diag(\lambda_1,\dots,\lambda_r) \oplus \0\bigr)\U_2
&= \diag(\lambda_1,\dots,\lambda_r) \oplus \R\tp\0\R \\
&= \diag(\lambda_1,\dots,\lambda_r) \oplus \0 ,
\end{aligned}
\]
and turns the linear part into \( 2\c\tp\R(w_{r+1},\dots,w_n)\tp = 2\norm{\c}w_{r+1} \). Finally translate \( w_{r+1} \) by \( -c'/(2\norm\c) \), which changes no quadratic term because the coefficient of \( w_{r+1}^2 \) is \( \lambda_{r+1} = 0 \). The result is form (b) with \( \mu = \norm\c > 0 \).

**Step 4: invariance.** Let \( g(\y) = \U\y + \t \) with \( \U \in \Orth(n) \). By @prp-quadric-congruence, \( Q\circ g \) has small matrix \( \U\tp\A\U \), which is similar to \( \A \) and so has the same eigenvalues with multiplicity (@thm-charpoly-similarity-invariant). Its linear vector is \( \b' = \U\tp(\A\t + \b) \). For the central case, \( g^{-1}(\p) \) is a center of \( Q \circ g \) whenever \( \p \) is a center of \( Q \), as noted at the end of @thm-affine-classification-of-quadrics, and the value there is \( (Q\circ g)(g^{-1}(\p)) = Q(\p) \); so \( c_0 \) is unchanged. For the centerless case, \( \nul(\U\tp\A\U) = \U\tp\nul(\A) \), and \( \A\t \in \col(\A) = \nul(\A)^{\perp} \), so the component of \( \b' \) in \( \nul(\U\tp\A\U) \) is \( \U\tp \) applied to the component of \( \b \) in \( \nul(\A) \); an orthogonal matrix preserves norms (@thm-isometry-characterizations), so \( \mu \) is unchanged. This proves the theorem.
:::

When \( \A \) is invertible and \( c_0 \ne 0 \), dividing form (a) by \( -c_0 \) puts it as
\[
\frac{y_1^2}{a_1^2} + \dots + \frac{y_n^2}{a_n^2} = 1
\quad\text{with}\quad
\frac{1}{a_i^2} = \frac{\lambda_i}{-c_0} ,
\]
whenever all the ratios \( \lambda_i/(-c_0) \) are positive, which is the ellipsoid case. The **semi-axes** \( a_i = \sqrt{-c_0/\lambda_i} \) lie along the eigenvectors, and a large eigenvalue gives a short axis, exactly as in @exm-principal-axes-ellipse.

::: {.remark}
That last sentence is the Rayleigh quotient in disguise. For a centered ellipsoid \( \x\tp\A\x = 1 \) with \( \A \) positive definite, any point \( \x \) on it has \( R_{\A}(\x) = \x\tp\A\x/\norm{\x}^2 = 1/\norm{\x}^2 \). By @prp-rayleigh-basic the quotient attains its maximum \( \lambda_{\max} \) at a top eigenvector, and since \( R_{\A} \) is unchanged by scaling while every non-zero vector scales to a point of the ellipsoid, the maximum over the ellipsoid is that same \( \lambda_{\max} \), attained at the scaled top eigenvector; so \( \norm{\x} \) attains its **minimum** \( 1/\sqrt{\lambda_{\max}} \) there: the shortest semi-axis points along the eigenvector of the largest eigenvalue. The longest does the same with the smallest eigenvalue. Chapter 23 uses the same picture for a vibrating chain whose masses are all equal, where the eigenvalues are squared frequencies and the principal axes are the shapes in which the chain vibrates.
:::

::: {#exm-conic-both-routes}
[One conic, two classifications]

Over \( \nR \), consider
\[
Q(x,y) = 5x^2 + 4xy + 5y^2 - 14x - 14y - 7 .
\]
Classify its zero set affinely, and then find its center, principal axes and semi-axes.
:::

::: {.solution}
The small and big matrices are
\[
\A = \begin{pmatrix} 5 & 2 \\ 2 & 5\end{pmatrix},
\qquad
\widetilde\A = \begin{pmatrix} 5 & 2 & -7 \\ 2 & 5 & -7 \\ -7 & -7 & -7 \end{pmatrix},
\]
the off-diagonal \( 2 \) being half of \( 4 \) and the \( -7 \) in the last column being half of \( -14 \).

*Center.* \( \det\A = 21 \ne 0 \), so by @prp-centre-exists-iff (b) there is exactly one center, the solution of \( \A\p = -\b = (7,7) \), namely \( \p = (1,1) \). Then \( c_0 = Q(1,1) = 5 + 4 + 5 - 14 - 14 - 7 = -21 \).

*Affine route.* By @prp-centre-exists-iff (c), translating to \( \p \) gives \( 5X^2 + 4XY + 5Y^2 - 21 \) with \( X = x-1 \), \( Y = y-1 \). Completing the square,
\[
5X^2 + 4XY + 5Y^2 = 5\Bigl(X + \tfrac25Y\Bigr)^2 + \tfrac{21}{5}Y^2 ,
\]
since \( 5 - \tfrac45 = \tfrac{21}{5} \). So with \( s = X + \tfrac25Y \) and \( t = Y \) the equation is \( 5s^2 + \tfrac{21}{5}t^2 = 21 \), and the further scaling \( w_1 = \sqrt{5/21}\,s \), \( w_2 = t/\sqrt5 \) gives \( w_1^2 + w_2^2 = 1 \). The inertia of \( \A \) is \( (2,0,0) \) and that of \( \widetilde\A \) is \( (2,1,0) \), since \( \det\widetilde\A = (\det\A)c_0 = -441 < 0 \) forces one negative eigenvalue and \( \A \) supplies two positive ones. Row 1 of the table: an **ellipse**.

*Euclidean route.* The characteristic polynomial of \( \A \) is \( x^2 - 10x + 21 = (x-3)(x-7) \), so the eigenvalues are \( 3 \) and \( 7 \) with unit eigenvectors
\[
\q_1 = \tfrac{1}{\sqrt2}(1, -1), \qquad \q_2 = \tfrac{1}{\sqrt2}(1, 1),
\]
as \( \A(1,-1) = (3,-3) \) and \( \A(1,1) = (7,7) \). By @thm-euclidean-classification the motion \( \x = \U\y + \p \) with \( \U = (\q_1\ \q_2) \) turns \( Q \) into \( 3y_1^2 + 7y_2^2 - 21 \), that is
\[
\frac{y_1^2}{7} + \frac{y_2^2}{3} = 1 .
\]
So the ellipse is centered at \( (1,1) \), with semi-axis \( \sqrt7 \) along \( \q_1 \) and semi-axis \( \sqrt3 \) along \( \q_2 \). Check the longer one: the point \( (1,1) + \sqrt7\,\q_1 = \bigl(1 + \sqrt{7/2},\, 1 - \sqrt{7/2}\bigr) \) has \( X = -Y = \sqrt{7/2} \), and \( 5X^2 + 4XY + 5Y^2 = (5 - 4 + 5)\cdot\tfrac72 = 21 \), as required.

*What each route saw.* Both say "ellipse". Only the Euclidean one says which ellipse: the affine route ended at a circle of radius \( 1 \), having first sheared the plane by \( s = X + \tfrac25Y \) and then stretched it by the unequal factors \( \sqrt{5/21} \) and \( 1/\sqrt5 \) to get there.
:::

\begin{center}
\begin{tikzpicture}[scale=0.95, lab/.style={font=\small}]
    \draw[->, gray] (-2.2,0) -- (4.4,0) node[below, black, lab] {$x$};
    \draw[->, gray] (0,-2.2) -- (0,4.4) node[left, black, lab] {$y$};
    \draw[dashed, black!45] ($(1,1)+(135:3.3)$) -- ($(1,1)+(-45:3.3)$);
    \draw[dashed, black!45] ($(1,1)+(45:2.4)$) -- ($(1,1)+(225:2.4)$);
    \draw[very thick, shift={(1,1)}, rotate=-45] (0,0) ellipse (2.6458 and 1.7321);
    \draw[->, very thick] (1,1) -- ++(-45:2.6458);
    \draw[->, very thick] (1,1) -- ++(45:1.7321);
    \fill (1,1) circle (2pt);
    \node[lab, below left] at (0.92,0.92) {$(1,1)$};
    \node[lab, right] at (3.0,-1.05) {$\sqrt7\,\q_1$};
    \node[lab, above right] at (2.25,2.15) {$\sqrt3\,\q_2$};
    \node[lab, align=center] at (1.1,-2.9)
      {$5x^2+4xy+5y^2-14x-14y-7=0$: center $(1,1)$,\\ axes along the eigenvectors of $\begin{psmallmatrix}5&2\\2&5\end{psmallmatrix}$};
\end{tikzpicture}
\end{center}

The two classifications answer two different questions, and it is worth being blunt about which is which. The affine one asks what the quadric is *made of* — a curve, a pair of lines, a point, nothing — and its invariants are two inertias. The Euclidean one asks what the quadric *looks like*, and its invariants are the eigenvalues themselves. Section 10 asks a third question, the projective one, and the answer there is shorter than both.

## Exercises

### A. Check your understanding

::: {#exr-quadrics-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State @def-quadric, including every clause on \( \A \), and say what goes wrong if the clause "non-zero" is dropped.
2. Write down the big matrix \( \widetilde\A \) of \( 3x^2 - 2xy + y^2 + 4x - 2 \) over \( \nR \).
3. Name the three places in this section where \( \operatorname{char} F \ne 2 \) is used.
4. True or false: two quadric polynomials with the same zero set are affinely equivalent. Justify your answer.
5. A quadric on \( \nR^5 \) has \( \rank\A = 3 \) and \( \rank\widetilde\A = 5 \). Which of the three families of @thm-affine-classification-of-quadrics does it belong to, and is it central?
:::
:::

::: {.solution}
(a) \( Q(\x) = \x\tp\A\x + 2\b\tp\x + c \) with \( \A \in M_n(F) \) symmetric and non-zero, \( \b \in F^n \), \( c \in F \), over a field of characteristic \( \ne 2 \). If \( \A = \0 \) were allowed, \( Q \) would be an affine function and its zero set a flat or all of \( F^n \); nothing quadratic would remain, and @thm-affine-classification-of-quadrics, whose first step diagonalizes a small matrix of rank \( r \ge 1 \), would have nothing to work on.

(b) The coefficient of \( xy \) is \( -2 \), so \( a_{12} = -1 \); the coefficient of \( x \) is \( 4 \), so \( b_1 = 2 \); there is no \( y \) term, so \( b_2 = 0 \). Hence
\[
\widetilde\A = \begin{pmatrix} 3 & -1 & 2 \\ -1 & 1 & 0 \\ 2 & 0 & -2 \end{pmatrix}.
\]

(c) Writing a linear part \( \sum\beta_ix_i \) as \( 2\b\tp\x \); recovering a **symmetric** \( \A \) from the quadratic part, where the off-diagonal entries are halves (@thm-polarization-forms); and dividing by \( 4 \) in @eq-center-difference to get the center equation \( \A\p + \b = \0 \).

(d) False. Over \( \nR \), \( x^2 + y^2 + 1 \) and \( x^2 + 1 \) both have empty zero set, but \( \rank\A \) is \( 2 \) for the first and \( 1 \) for the second, and rank is an affine invariant by @prp-quadric-congruence.

(e) \( \rank\widetilde\A = \rank\A + 2 \), so it is family (III), and family (III) is exactly the centerless case by @thm-affine-classification-of-quadrics.
:::

### B. Practice

::: {#exr-quadrics-b1}
[B1: Centers]

For each of the following quadric polynomials over \( \nR \), determine the set of centers. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( 2x^2 + 3y^2 - 4x + 6y + 1 \).
2. \( x^2 - 4xy + 4y^2 + 2x - 4y + 5 \).
3. \( x^2 - 4xy + 4y^2 + 2x + y \).
:::
:::

::: {.solution}
In each case solve \( \A\p = -\b \) (@prp-centre-exists-iff (a)).

(a) \( \A = \diag(2,3) \), \( \b = (-2, 3) \). Since \( \A \) is invertible the center is unique: \( \p = -\A^{-1}\b = (1, -1) \).

(b) \( \A = \begin{psmallmatrix} 1 & -2 \\ -2 & 4\end{psmallmatrix} \), which has rank \( 1 \) with \( \col(\A) = \Span((1,-2)) \), and \( \b = (1, -2) \in \col(\A) \). So centers exist, and they solve \( p_1 - 2p_2 = -1 \): the line \( x - 2y + 1 = 0 \). (Consistently, the polynomial is \( (x - 2y + 1)^2 + 4 \), whose zero set is empty but whose equation is symmetric about that line.)

(c) Same \( \A \), but \( \b = (1, \tfrac12) \). If \( \b \) were in \( \col(\A) = \Span((1,-2)) \) its second entry would be \( -2 \) times its first, and \( \tfrac12 \ne -2 \). So there is no center; this is a parabola.
:::

::: {#exr-quadrics-b2}
[B2: Affine type]

Classify the conic \( x^2 + 6xy + y^2 - 4x - 4y + 3 = 0 \) over \( \nR \): find \( \operatorname{In}\A \) and \( \operatorname{In}\widetilde\A \), name the row of the table, and exhibit the invertible affine substitution that reaches the normal form.
:::

::: {.solution}
Here \( \A = \begin{psmallmatrix} 1 & 3 \\ 3 & 1\end{psmallmatrix} \) and \( \b = (-2,-2) \), \( c = 3 \). The eigenvalues of \( \A \) are \( 4 \) and \( -2 \), from \( x^2 - 2x - 8 = (x-4)(x+2) \), so \( \operatorname{In}\A = (1,1,0) \) by @thm-inertia-from-eigenvalues, and \( \det\A = -8 \ne 0 \).

The unique center solves \( \A\p = (2,2) \), giving \( \p = (\tfrac12, \tfrac12) \), and \( c_0 = Q(\p) = \tfrac14 + \tfrac32 + \tfrac14 - 2 - 2 + 3 = 1 \). Translating, the equation becomes \( X^2 + 6XY + Y^2 + 1 = 0 \) with \( X = x - \tfrac12 \), \( Y = y - \tfrac12 \). Completing the square, \( X^2 + 6XY + Y^2 = (X + 3Y)^2 - 8Y^2 \), so with \( s = X + 3Y \), \( t = Y \) the equation is \( s^2 - 8t^2 = -1 \). Multiplying by \( -1 \) and setting \( w_1 = 2\sqrt2\,t \), \( w_2 = s \) gives \( w_1^2 - w_2^2 = 1 \).

So \( \widetilde\A \) is congruent to \( \diag(1,-8,1) \) up to the translation, giving \( \operatorname{In}\widetilde\A = (2,1,0) \); up to the simultaneous exchange this is the invariant \( \bigl((1,1,0),(1,2,0)\bigr) \) of row 2. The conic is a **hyperbola**.
:::

::: {#exr-quadrics-b3}
[B3: Principal axes]

Find the center, principal axes and semi-axes of \( 2x^2 - 4xy + 5y^2 - 4x + 2y - 7 = 0 \) over \( \nR \).
:::

::: {.solution}
\( \A = \begin{psmallmatrix} 2 & -2 \\ -2 & 5\end{psmallmatrix} \), \( \b = (-2, 1) \), \( c = -7 \). Since \( \det\A = 6 \ne 0 \) the center solves \( \A\p = (2,-1) \): from \( 2p_1 - 2p_2 = 2 \) and \( -2p_1 + 5p_2 = -1 \) we get \( p_2 = \tfrac13 \), \( p_1 = \tfrac43 \). Then
\[
c_0 = Q(\p) = \b\tp\p + c = (-2)\tfrac43 + 1\cdot\tfrac13 - 7 = -\tfrac{28}{3} ,
\]
using \( Q(\p) = \p\tp(\A\p + \b) + \b\tp\p + c = \b\tp\p + c \), valid because \( \A\p + \b = \0 \).

The characteristic polynomial is \( x^2 - 7x + 6 = (x-1)(x-6) \), so \( \lambda = 1, 6 \) with unit eigenvectors \( \q_1 = \tfrac{1}{\sqrt5}(2,1) \) and \( \q_2 = \tfrac{1}{\sqrt5}(1,-2) \); indeed \( \A(2,1) = (2,1) \) and \( \A(1,-2) = (6,-12) \). By @thm-euclidean-classification the normal form is \( y_1^2 + 6y_2^2 - \tfrac{28}{3} = 0 \), that is
\[
\frac{y_1^2}{28/3} + \frac{y_2^2}{14/9} = 1 .
\]
So the curve is an ellipse centered at \( (\tfrac43, \tfrac13) \), with semi-axis \( 2\sqrt{21}/3 = \sqrt{28/3} \) along \( \q_1 \) and semi-axis \( \sqrt{14}/3 \) along \( \q_2 \).
:::

### C. Going deeper

::: {#exr-quadrics-c1}
[C1: Which quadrics are determined by their points]

Work over \( \nR \) with \( n = 2 \).

::: {.enumerate options="label=(\alph*)"}
1. Give two quadric polynomials with the same zero set that are **not** proportional.
2. Prove that if \( Q \) is a quadric polynomial whose zero set contains three points of some line \( L \), then \( Q \) vanishes on all of \( L \).
3. Deduce that the zero set of a quadric polynomial is never exactly a set of three non-collinear points.
:::

*Hint for (b): restrict \( Q \) to a parametrization of \( L \).*
:::

::: {.solution}
(a) Take \( Q_1 = x^2 + y^2 \) and \( Q_2 = x^2 + 2y^2 \). Both vanish exactly at \( \0 \), since a sum of squares of reals is zero only when each is, but \( Q_2 \ne \lambda Q_1 \) for any \( \lambda \): comparing the coefficients of \( x^2 \) forces \( \lambda = 1 \), and then the coefficients of \( y^2 \) disagree.

(b) Write \( L = \{\p + t\v : t \in \nR\} \) with \( \v \ne \0 \), a flat of dimension \( 1 \) (@def-flat). Then
\[
f(t) = Q(\p + t\v) = (\v\tp\A\v)t^2 + 2\bigl(\v\tp(\A\p + \b)\bigr)t + Q(\p)
\]
by the expansion in the proof of @prp-centre-exists-iff, so \( f \) is a polynomial of degree at most \( 2 \) in \( t \). If \( Q \) vanishes at three distinct points of \( L \), then \( f \) has three distinct roots. A non-zero polynomial of degree at most \( 2 \) over a field has at most \( 2 \) roots (@cor-root-bound-general), so \( f \) is the zero polynomial and \( Q \) vanishes on all of \( L \).

(c) Suppose, for a contradiction, that the zero set of a quadric polynomial \( Q \) is exactly \( \{P_1, P_2, P_3\} \) with the three points not collinear, that is affinely independent (@def-affine-independence). Then \( (P_1, P_2, P_3) \) is an affine frame of \( \nR^2 \) (@def-affine-frame), so by @thm-affine-map-determined-by-frame there is an affine map \( f \) carrying it to the frame \( \bigl((0,0), (1,0), (0,1)\bigr) \). That \( f \) is invertible: by @thm-affine-map-is-linear-plus-translation (b) its linear part sends \( \overrightarrow{P_1P_2} \) to \( \e_1 \) and \( \overrightarrow{P_1P_3} \) to \( \e_2 \), so it carries a basis to a basis and is invertible, whence \( f \) is bijective by @prp-affine-map-block-matrix. Substituting by \( f^{-1} \), we may therefore assume the three points **are** \( (0,0) \), \( (1,0) \), \( (0,1) \), since an invertible affine substitution carries the zero set bijectively to the zero set (@prp-quadric-congruence).

Write \( Q = ax^2 + 2hxy + by^2 + 2dx + 2ey + c \). Then \( Q(0,0) = c = 0 \), \( Q(1,0) = a + 2d = 0 \) and \( Q(0,1) = b + 2e = 0 \), so
\[
Q = a\,x(x-1) + b\,y(y-1) + 2hxy .
\]
Restricting to the line \( y = 0 \) gives \( a\,x(x-1) \). If \( a = 0 \) this vanishes identically and the whole line lies in the zero set, which is impossible for a three-point set; so \( a \ne 0 \), and by the same argument on \( x = 0 \), \( b \ne 0 \).

Now fix \( m \in \nR \) with \( m \ne 0 \) and restrict to the line \( y = mx \):
\[
Q(t, mt) = t\bigl[(a + 2hm + bm^2)\,t - (a + bm)\bigr] .
\]
The only point of \( \{P_1,P_2,P_3\} \) on that line is \( (0,0) \), because \( (1,0) \) needs \( m = 0 \) and \( (0,1) \) is not of the form \( (t, mt) \). So \( t = 0 \) must be the only root. If \( a + 2hm + bm^2 \ne 0 \), the bracket vanishes at \( t = (a+bm)/(a+2hm+bm^2) \), and that must be \( 0 \), forcing \( a + bm = 0 \). Hence for every \( m \ne 0 \),
\[
a + 2hm + bm^2 = 0 \qquad \text{or} \qquad a + bm = 0 .
\]
The first equation is a quadratic in \( m \) with leading coefficient \( b \ne 0 \), so it has at most \( 2 \) roots, and the second has exactly one since \( b \ne 0 \) (@cor-root-bound-general). That is at most three permitted values of \( m \), while \( \nR \setminus \{0\} \) is infinite. Contradiction. Hence no quadric polynomial over \( \nR \) has exactly three non-collinear points as its zero set.
:::

::: {#exr-quadrics-c2}
[C2: Over another field]

::: {.enumerate options="label=(\alph*)"}
1. Over \( \nC \), prove that every quadric polynomial in \( n \) variables is equivalent, under an invertible affine substitution and a non-zero scalar, to one of \( \sigma_r(\y) - 1 \), \( \sigma_r(\y) \), or \( \sigma_r(\y) - y_{r+1} \) with \( r < n \), where \( \sigma_r(\y) = y_1^2 + \dots + y_r^2 \). How many normal forms are there for \( n = 2 \)?
2. Over \( \nF_3 \), how many points does the conic \( x^2 + y^2 - 1 = 0 \) have in \( \nF_3^2 \)? And \( x^2 + y^2 = 0 \)?
:::
:::

::: {.solution}
(a) Repeat the proof of @thm-affine-classification-of-quadrics, replacing @cor-real-symmetric-classification by @cor-complex-symmetric-classification, which says that over \( \nC \) a symmetric matrix of rank \( r \) is congruent to \( \I_r \oplus \0_{n-r} \): rank alone is the congruence invariant. Step 1 gives \( \sigma_r + 2\b_1\tp\y + c \); Step 2 is unchanged; and in Step 3 Case A with \( c_2 \ne 0 \) we substitute \( z_i = \gamma w_i \) for \( i \le r \) with \( \gamma^2 = -c_2 \), possible because every complex number has a square root, and obtain \( \sigma_r - 1 \) after dividing by \( -c_2 \). No sign remains to normalize, and no \( p \) survives, so the invariants reduce to \( (\rank\A, \rank\widetilde\A) = (r, r+1), (r,r), (r, r+2) \), which are pairwise distinct. For \( n = 2 \): \( r = 1 \) gives three forms and \( r = 2 \) gives two (family (III) needs \( r < n \)), so **five** in all, against nine over \( \nR \). The four forms that disappear are accounted for by inertia: over \( \nC \) the ellipse, the hyperbola and the empty conic \( x^2+y^2+1 \) all become \( \sigma_2 - 1 \); the point and the crossing lines both become \( \sigma_2 \); and \( x^2 = 1 \) and \( x^2 = -1 \) both become \( \sigma_1 - 1 \), the last two because \( i^2 = -1 \).

(b) The squares in \( \nF_3 \) are \( 0^2 = 0 \), \( 1^2 = 1 \), \( 2^2 = 1 \), so \( x^2 \in \{0,1\} \) and \( x^2 = 1 \) has two solutions while \( x^2 = 0 \) has one. For \( x^2 + y^2 = 1 \): either \( x^2 = 1 \) and \( y^2 = 0 \), giving \( 2 \cdot 1 = 2 \) points, or \( x^2 = 0 \) and \( y^2 = 1 \), giving \( 1 \cdot 2 = 2 \) points; and \( 1 + 1 = 2 \ne 1 \) rules out the remaining combination. Total **4** points, namely \( (\pm1, 0) \) and \( (0,\pm1) \). For \( x^2 + y^2 = 0 \): the options are \( 0 + 0 \) only, since \( 1 + 1 = 2 \ne 0 \) and \( 1 + 0 = 1 \ne 0 \). Total **1** point, the origin. So over \( \nF_3 \) this "circle" behaves like a real circle in the first case and like the real point-conic in the second, because \( -1 \) is not a square in \( \nF_3 \).
:::

::: {#exr-quadrics-c3}
[C3: The center as a projection]

Let \( Q(\x) = \x\tp\A\x + 2\b\tp\x + c \) be a central quadric polynomial on \( \nR^n \) with \( r = \rank\A \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that the set of centers is a flat of dimension \( n - r \) (@def-flat).
2. Prove that the set of centers is contained in the zero set of \( Q \) if and only if \( Q(\p) = 0 \) for one, hence every, center \( \p \).
3. Give an example on \( \nR^3 \) with a line of centers, none of which lies on the quadric.
:::
:::

::: {.solution}
(a) By @prp-centre-exists-iff (a) the centers are the solutions of \( \A\p = -\b \), a consistent linear system. By @thm-general-solution-structure its solution set is \( \p_0 + \nul(\A) \) for any particular solution \( \p_0 \), a coset of \( \nul(\A) \), hence a flat with direction space \( \nul(\A) \). Its dimension is \( \dim\nul(\A) = n - \rank\A = n - r \) by the Rank-Nullity Theorem (@thm-rank-nullity).

(b) By @prp-centre-exists-iff (c) the value \( Q(\p) \) is the same at every center, so "for one" and "for every" agree; and the set of centers lies in the zero set exactly when that common value is \( 0 \).

(c) Take \( Q(x,y,z) = x^2 + y^2 - 1 \) on \( \nR^3 \). Here \( \A = \diag(1,1,0) \) has rank \( 2 \), \( \b = \0 \in \col(\A) \), and the centers are the solutions of \( \A\p = \0 \), namely the \( z \)-axis, a line as (a) predicts with \( n - r = 1 \). The common value is \( Q(0,0,z) = -1 \ne 0 \), so no center lies on the quadric, which is the cylinder of radius \( 1 \) about the \( z \)-axis.
:::
