# Minkowski Space

Sylvester's law of inertia says that a real symmetric form is nothing but a pair of counts, and that any two forms with the same counts are the same form in disguise. One pair of counts has a claim on our attention that none of the others has: the form of signature \( (1, 3) \) is the one the physical world appears to run on. This section does the linear algebra of that form. Everything in it is this chapter's machinery specialized, and the payoff is a picture — a cone dividing space into three regions — together with a classification theorem that is the hyperbolic twin of a circular one we already proved.

## The form of special relativity

Fix \( n_+ = 1 \) and \( n_- = 3 \) in the canonical form of @cor-real-symmetric-classification, and there is only one form to write down.

::: {#def-minkowski-space}
[Minkowski Space]

**Minkowski space** \( \nR^{1,3} \) is the real vector space \( \nR^4 \) equipped with the symmetric bilinear form
\[
\eta(\x, \y) \coloneqq x_1y_1 - x_2y_2 - x_3y_3 - x_4y_4 ,
\]
whose quadratic form is \( q(\x) = x_1^2 - x_2^2 - x_3^2 - x_4^2 \). The first coordinate is the **time** coordinate and the remaining three are the **space** coordinates. More generally, for \( p, m \ge 0 \), \( \nR^{p,m} \) is \( \nR^{p+m} \) with the form whose matrix in the standard basis is \( \I_p \oplus (-\I_m) \).
:::

In words: \( \eta \) is the dot product of \( \nR^4 \) with three of its four signs reversed. Its matrix in the standard basis \( \sE \) is
\[
\mtx{\eta}{\sE}{\sE} = \diag(1, -1, -1, -1),
\]
which is symmetric, so \( \eta \) is a symmetric form (@def-symmetric-form), and it is diagonal, so \( \sE \) is an orthogonal basis for \( \eta \) (@def-orthogonal-basis-form). Reading off the signs, the signature of \( \eta \) is \( (1, 3) \) and its inertia is \( (1, 3, 0) \) (@def-signature). The form is **non-degenerate**: \( \eta(\e_1, \x) = x_1 \) and \( \eta(\e_j, \x) = -x_j \) for \( j = 2, 3, 4 \), so a vector paired to zero with everything has all four coordinates zero (@def-nondegenerate).

::: {.warning}
**Two sign conventions are in use, and both are called "the" Minkowski form.** We take \( (+, -, -, -) \), signature \( (1, 3) \); many sources take \( (-, +, +, +) \), signature \( (3, 1) \), which is our \( -\eta \). The two are not congruent — congruence preserves the signature (@thm-sylvester-inertia) — but every statement below transfers by reversing each inequality on \( q \), because \( q \) changes sign. The one thing both conventions agree on is the set \( \{q = 0\} \), which is why the picture of this section is convention-free. State your convention before computing, and never mix the two.
:::

## Timelike, spacelike and null

Nothing in this section is a new notion. Section 7 studied the vectors on which a form vanishes, and called them isotropic; over \( \nR \) a non-degenerate indefinite form has plenty of them, and the ones belonging to \( \eta \) have names of their own.

*The form sorts non-zero vectors into three classes by the sign of \( q \), and the middle class — where \( q \) vanishes — is exactly the isotropy of Section 7.*

::: {#def-causal-character}
[Timelike, Spacelike, Null]

Let \( \x \in \nR^{1,3} \) with \( \x \ne \0 \). Then \( \x \) is

::: {.enumerate options="label=(\alph*)"}
1. **timelike** if \( q(\x) > 0 \);
2. **null**, or **lightlike**, if \( q(\x) = 0 \);
3. **spacelike** if \( q(\x) < 0 \).
:::

The set \( \{\x \in \nR^{1,3} : q(\x) = 0\} \) is the **light cone**. A timelike \( \x \) is **future-pointing** if \( x_1 > 0 \) and **past-pointing** if \( x_1 < 0 \).
:::

The word **null** is a second name for something already defined: a null vector is precisely a non-zero **isotropic** vector for \( \eta \) in the sense of @def-isotropic-vector, and the light cone is the isotropy locus of \( \eta \) together with \( \0 \). So "the light cone" is not new geometry; it is the locus Section 7 already forced us to take seriously, drawn for one particular form. Timelike and spacelike are then just names for the two sides that the isotropy locus separates.

The last clause of the definition is legitimate because a timelike vector cannot have \( x_1 = 0 \): if it did, then \( q(\x) = -(x_2^2 + x_3^2 + x_4^2) \le 0 \). So every timelike vector is future-pointing or past-pointing, and exactly one of the two.

::: {#exm-causal-character-samples}
[Reading off the three types]

Classify \( \e_1 \), \( \e_2 \), \( \e_1 + \e_2 \) and \( (2, 1, 1, 1) \) in \( \nR^{1,3} \), and decide which of them are isotropic.
:::

::: {.solution}
\( q(\e_1) = 1 > 0 \), so \( \e_1 \) is timelike and future-pointing. \( q(\e_2) = -1 < 0 \), so \( \e_2 \) is spacelike. \( q(\e_1 + \e_2) = 1 - 1 = 0 \), so \( \e_1 + \e_2 \) is null, hence isotropic. Finally \( q(2,1,1,1) = 4 - 3 = 1 > 0 \), timelike and future-pointing. Only \( \e_1 + \e_2 \) is isotropic; the other three are anisotropic.
:::

Section 7's structure theorem applies verbatim. A non-zero isotropic vector sits in a hyperbolic plane, and here we can point to one: take \( \u = \e_1 + \e_2 \) and \( \w = \tfrac12(\e_1 - \e_2) \). Then \( q(\u) = q(\w) = 0 \) and
\[
\eta(\u, \w) = \tfrac12\bigl(1 - (-1)\bigr) = 1 ,
\]
so the Gram matrix of \( (\u, \w) \) is \( \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix} \) and \( \Span(\u, \w) \) is a hyperbolic plane (@def-hyperbolic-plane). Splitting it off, @thm-witt-decomposition writes
\[
\nR^{1,3} \;=\; H \perp W ,
\]
with \( H \) hyperbolic of signature \( (1,1) \) and \( W \) anisotropic of signature \( (0,2) \), that is, negative definite. Only one plane splits off, because the Witt index of a real form of signature \( (n_+, n_-) \) is \( \min(n_+, n_-) \) (@prp-witt-index-real-complex), which here is \( \min(1,3) = 1 \).

::: {.check}
Is there a **plane** in \( \nR^{1,3} \) on which \( \eta \) vanishes identically?
:::

::: {.solution}
No. Suppose \( \x = (a, \u) \) and \( \y = (b, \w) \) span such a plane, where \( a, b \in \nR \) and \( \u, \w \in \nR^3 \). Then \( q(\x) = q(\y) = 0 \) gives \( a^2 = \norm{\u}^2 \) and \( b^2 = \norm{\w}^2 \), while \( \eta(\x, \y) = 0 \) gives \( ab = \u \cdot \w \). Hence \( \lvert\u \cdot \w\rvert = \lvert a\rvert\lvert b\rvert = \norm{\u}\norm{\w} \), which is the equality case of @thm-cauchy-schwarz, so \( (\u, \w) \) is dependent. If \( \u = \0 \) then \( a = 0 \) and \( \x = \0 \); otherwise \( \w = \lambda\u \), so \( b^2 = \lambda^2a^2 \) and \( ab = \lambda a^2 \), which force \( b = \lambda a \) and \( \y = \lambda\x \). Either way \( (\x, \y) \) is dependent, so no plane exists. Structurally this is the statement that the Witt index of \( \nR^{1,3} \) is \( \min(1, 3) = 1 \) (@prp-witt-index-real-complex), since by @def-witt-index no totally isotropic subspace has dimension larger than the index.
:::

The picture is easiest to draw with one space coordinate instead of three, in \( \nR^{1,1} \), where the light cone degenerates to the two lines \( x_2 = \pm x_1 \).

\begin{center}
\begin{tikzpicture}[scale=1.55, lab/.style={font=\small}]
    \fill[black!8] (0,0) -- (1.62,1.62) -- (-1.62,1.62) -- cycle;
    \fill[black!8] (0,0) -- (1.62,-1.62) -- (-1.62,-1.62) -- cycle;
    \draw[->, gray] (-1.95,0) -- (2.0,0) node[below, black, lab] {$x_2$};
    \draw[->, gray] (0,-1.95) -- (0,2.0) node[left, black, lab] {$x_1$};
    \draw[very thick] (-1.62,-1.62) -- (1.62,1.62);
    \draw[very thick] (-1.62,1.62) -- (1.62,-1.62);
    \draw[dashed, black!60] plot[smooth] coordinates
      {(-1.1,1.487) (-0.7,1.221) (-0.35,1.059) (0,1) (0.35,1.059) (0.7,1.221) (1.1,1.487)};
    \draw[dashed, black!60] plot[smooth] coordinates
      {(-1.1,-1.487) (-0.7,-1.221) (-0.35,-1.059) (0,-1) (0.35,-1.059) (0.7,-1.221) (1.1,-1.487)};
    \node[lab] at (0,1.53) {timelike, $q > 0$};
    \node[lab] at (0,-1.53) {timelike, $q > 0$};
    \node[lab, align=center] at (1.30,0.42) {spacelike\\ $q < 0$};
    \node[lab, align=center] at (-1.30,0.42) {spacelike\\ $q < 0$};
    \node[lab, right] at (1.62,1.55) {null, $q = 0$};
    \node[lab, fill=black!8, inner sep=1.5pt] at (0,0.58) {$q = 1$};
    \node[lab, align=center] at (0,-2.55)
      {The light cone $q = 0$ in the Minkowski plane separates the timelike\\
       vectors from the spacelike ones; the ``unit sphere'' $q = 1$ is the\\
       dashed hyperbola, and it is unbounded};
\end{tikzpicture}
\end{center}

Two features of the picture deserve to be said out loud. The shaded region is **not** connected: the future-pointing and past-pointing timelike vectors form two separate pieces, and no continuous path of timelike vectors joins them. That last claim is worth one line, since it is the only place in this section where a topological word is used. Suppose \( \gamma \) were a continuous path of timelike vectors from a future-pointing vector to a past-pointing one. Its first coordinate \( x_1 \) is a continuous real function that is positive at one end and negative at the other, so by the intermediate value theorem — an analysis input, quoted and not proved here, as in Section 6 — it vanishes somewhere along the path. But \( x_1 = 0 \) forces \( q(\x) = -x_2^2 - x_3^2 - x_4^2 \le 0 \), so that point of the path is not timelike, a contradiction. And the level set \( q = 1 \), which plays the role the unit circle plays for the dot product, is unbounded. Both facts come straight from the mixed signs, and both are invisible to anyone whose intuition was trained on positive definite forms.

::: {.warning}
**Orthogonality for \( \eta \) is not the perpendicularity you can see.** A null vector is \( \eta \)-orthogonal to *itself*, and the consequence is that Chapter 10's decomposition \( V = U \oplus U^{\perp} \) fails. Take \( U = \Span\bigl((1,1,0,0)\bigr) \). Since \( \eta\bigl((1,1,0,0), \x\bigr) = x_1 - x_2 \), the \( \eta \)-orthogonal complement of \( U \) is the hyperplane \( \{x_1 = x_2\} \), which **contains** \( U \). So \( U + U^{\perp} = U^{\perp} \) is three-dimensional, not four, and \( U \cap U^{\perp} = U \ne \{\0\} \). Nothing has gone wrong; positivity was doing that work in Chapter 10, and it is gone.
:::

## Hyperbolic rotations

Now the isometries. The group attached to \( \eta \) is the isometry group of its matrix (@def-isometry-group-of-form), which is \( \Orth(1,3) \) in the notation of @def-classical-groups: the matrices \( \P \) with \( \P\tp\mtx{\eta}{\sE}{\sE}\P = \mtx{\eta}{\sE}{\sE} \). Its elements are the **Lorentz transformations**. We classify them in dimension \( 2 \), where \( \eta \) becomes
\[
\eta_2(\x, \y) = x_1y_1 - x_2y_2 , \qquad \mtx{\eta_2}{\sE}{\sE} = \diag(1,-1) .
\]

The classification of \( \Orth(2) \) in @thm-orthogonal-2x2 rested on one geometric fact: a unit vector of the Euclidean plane is \( (\cos\theta, \sin\theta) \) for exactly one \( \theta \in [0, 2\pi) \). Replace the circle by the hyperbola and the same proof runs. We need the corresponding parametrization, and we take it from calculus:

\[
\begin{aligned}
\cosh t &= \tfrac12(e^{t} + e^{-t}), \qquad \sinh t = \tfrac12(e^{t} - e^{-t}) , \\
\cosh^2 t - \sinh^2 t &= 1, \qquad \cosh t > 0 , \\
\cosh(s+t) &= \cosh s\cosh t + \sinh s\sinh t , \\
\sinh(s+t) &= \sinh s\cosh t + \cosh s\sinh t ,
\end{aligned}
\]

and \( \sinh \colon \nR \to \nR \) is a strictly increasing bijection. Those facts are the only analysis used in this section.

::: {#def-lorentz-boost}
[Boost]

For \( t \in \nR \), the **boost of rapidity \( t \)** is
\[
\B_t \coloneqq \begin{pmatrix} \cosh t & \sinh t \\ \sinh t & \cosh t \end{pmatrix} \in M_2(\nR) .
\]
:::

A boost is the hyperbolic analogue of the rotation \( \R_{\theta} \) of Chapter 10: same shape, hyperbolic functions in place of circular ones, and no minus sign in the corner.

::: {#thm-lorentz-boost-form}
[Classification of the Plane Lorentz Transformations]

Let \( \P \in \Orth(1,1) \), that is, \( \P \in M_2(\nR) \) with \( \P\tp\diag(1,-1)\P = \diag(1,-1) \). Then there are a unique \( t \in \nR \) and unique signs \( \varepsilon, \mu \in \{1, -1\} \) with
\[
\P = \begin{pmatrix} \varepsilon\cosh t & \mu\sinh t \\ \sinh t & \varepsilon\mu\cosh t \end{pmatrix},
\]
and \( \det\P = \mu \). Writing \( \D = \diag(1,-1) \), this says
\[
\Orth(1,1) = \{\,\B_t,\; \B_t\D,\; -\B_t,\; -\B_t\D \;:\; t \in \nR\,\} ,
\]
a disjoint union of four families. Moreover \( \B_s\B_t = \B_{s+t} \) for all \( s, t \), so \( \{\B_t : t \in \nR\} \) is a subgroup of \( \Orth(1,1) \) isomorphic to \( (\nR, +) \).
:::

::: {.idea}
The congruence \( \P\tp\D\P = \D \) says exactly that the two columns of \( \P \) are an orthogonal basis for \( \eta_2 \) with \( q \)-values \( 1 \) and \( -1 \). So: parametrize the vectors with \( q = 1 \), which is the hyperbola; then the second column is forced, because the \( \eta_2 \)-orthogonal complement of a non-isotropic vector is a line, and on that line only two vectors have \( q = -1 \). This is @thm-orthogonal-2x2's proof with the circle replaced by the hyperbola.
:::

::: {.proof}
Write \( \P = \begin{pmatrix} a & c \\ b & d\end{pmatrix} \) with columns \( \p_1 = (a,b) \) and \( \p_2 = (c,d) \). The \( (i,j) \) entry of \( \P\tp\D\P \) is \( \eta_2(\p_i, \p_j) \), so the hypothesis says
\[
q(\p_1) = 1, \qquad q(\p_2) = -1, \qquad \eta_2(\p_1, \p_2) = 0 .
\]

**The first column.** Since \( \sinh \) is a bijection of \( \nR \), there is a unique \( t \in \nR \) with \( b = \sinh t \). Then \( a^2 = 1 + b^2 = 1 + \sinh^2 t = \cosh^2 t \), so \( a = \varepsilon\cosh t \) for a unique sign \( \varepsilon \), unique because \( \cosh t > 0 \).

**The second column.** The vector \( \z = (\sinh t, \varepsilon\cosh t) \) satisfies \( \eta_2(\p_1, \z) = \varepsilon\cosh t\sinh t - \sinh t\,\varepsilon\cosh t = 0 \), and \( \z \ne \0 \) because \( \varepsilon\cosh t \ne 0 \). The set \( \{\y : \eta_2(\p_1, \y) = 0\} \) is the null space of the non-zero row vector \( (a, -b) \), hence a line, so it equals \( \Span(\z) \). Therefore \( \p_2 = \mu'\z \) for some \( \mu' \in \nR \), and \( q(\z) = \sinh^2 t - \cosh^2 t = -1 \) gives \( -1 = q(\p_2) = (\mu')^2q(\z) = -(\mu')^2 \). Hence \( \mu' = \mu \) is a sign, and it is determined by \( \P \), since \( d = \mu\varepsilon\cosh t \) and \( \cosh t > 0 \). This is the displayed matrix, and expanding,
\[
\det\P = \mu\bigl(\varepsilon^2\cosh^2 t - \sinh^2 t\bigr) = \mu .
\]

**The four families.** For \( \varepsilon = \mu = 1 \) the matrix is \( \B_t \); for \( \varepsilon = 1, \mu = -1 \) it is \( \B_t\D \); for \( \varepsilon = -1, \mu = 1 \) it is \( -\B_{-t} \); and for \( \varepsilon = \mu = -1 \) it is \( -\B_{-t}\D \), each by multiplying out and using \( \sinh(-t) = -\sinh t \), \( \cosh(-t) = \cosh t \). As \( t \) runs over \( \nR \) so does \( -t \), which gives the displayed set equality. The families are disjoint because \( \varepsilon \) is the sign of the \( (1,1) \) entry and \( \mu = \det\P \), and both are determined by \( \P \).

**The subgroup.** By the addition formulas for \( \cosh \) and \( \sinh \),
\[
\B_s\B_t =
\begin{pmatrix} \cosh(s{+}t) & \sinh(s{+}t) \\ \sinh(s{+}t) & \cosh(s{+}t) \end{pmatrix}
= \B_{s+t} .
\]
So \( t \mapsto \B_t \) is a group homomorphism \( (\nR,+) \to \Orth(1,1) \); it is injective because \( \sinh \) is, and its image is a subgroup by @def-subgroup. This proves the theorem.
:::

The four families are sorted by two signs, and each sign has a reading. The determinant \( \mu \) says whether the space coordinate is reversed, exactly as in \( \Orth(2) \). The sign \( \varepsilon \) of the \( (1,1) \) entry says whether the future cone is sent to the future cone: for \( \B_t \) the image of \( \e_1 \) is \( (\cosh t, \sinh t) \), with positive first coordinate, while \( -\B_t \) sends it to \( (-\cosh t, -\sinh t) \). So the identity component consists of the boosts alone, and the other three families are obtained from it by reversing space, time, or both.

## Circular and hyperbolic, side by side

The comparison is the point of this section, so here it is in one table. In each column, the isometry group of the named form on \( \nR^2 \).

| | \( \Orth(2) \): form \( \I_2 \) | \( \Orth(1,1) \): form \( \diag(1,-1) \) |
|---|---|---|
| level set \( q = 1 \) | circle \( x_1^2 + x_2^2 = 1 \) | hyperbola \( x_1^2 - x_2^2 = 1 \), two branches |
| canonical element | \( \R_{\theta} = \begin{psmallmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta\end{psmallmatrix} \) | \( \B_{t} = \begin{psmallmatrix} \cosh t & \sinh t \\ \sinh t & \cosh t\end{psmallmatrix} \) |
| parameter | \( \theta \in [0, 2\pi) \), periodic | \( t \in \nR \), unbounded |
| addition law | \( \R_{\alpha}\R_{\beta} = \R_{\alpha+\beta} \) | \( \B_{s}\B_{t} = \B_{s+t} \) |
| determinant \( +1 \) part | \( \SO(2) = \{\R_{\theta}\} \) | \( \{\B_t\} \cup \{-\B_t\} \) |
| determinant \( -1 \) part | reflections \( \M_{\theta} \) | \( \{\B_t\D\} \cup \{-\B_t\D\} \) |
| number of pieces | \( 2 \) | \( 4 \) |
| entries | all of modulus \( \le 1 \) | unbounded |

The two canonical forms differ in one place only: \( \R_{\theta} \) carries a minus sign that \( \B_t \) does not, and that single sign is the difference between \( \cos^2 + \sin^2 = 1 \) and \( \cosh^2 - \sinh^2 = 1 \). Everything else in the table follows from it. In particular the last row is the unboundedness that Section 10 recorded when it observed, without proof, that \( \Orth(p,q) \) is not compact for \( p, q \ge 1 \) while \( \Orth(n) \) is.

::: {.remark}
In the physical reading, \( \tanh t \) is a velocity measured in units of the speed of light, and the additivity \( \B_s\B_t = \B_{s+t} \) of rapidities becomes the relativistic law for adding velocities. @exr-minkowski-space-c1 derives the formula from the theorem. The book verifies the algebra and stops there.
:::

## The triangle inequality, reversed

For a timelike \( \x \) the number \( q(\x) \) is positive, so it has a positive square root, and the analogy with a norm is irresistible. Write
\[
\tau(\x) \coloneqq \sqrt{q(\x)} \qquad (\x \text{ timelike}) .
\]
The analogy holds, but with every inequality upside down. First the tool.

::: {#lem-reversed-cauchy-schwarz}
[Reversed Cauchy–Schwarz Inequality]

Let \( \x, \y \in \nR^{1,3} \) be timelike and both future-pointing. Then
\[
\eta(\x, \y) \ge \tau(\x)\tau(\y) > 0 ,
\]
with equality if and only if \( \y = \lambda\x \) for some \( \lambda > 0 \).
:::

::: {.idea}
Split each vector as a time coordinate plus a space part, \( \x = (a, \u) \). Timelike and future-pointing says \( a > \norm{\u} \ge 0 \). Then \( \eta(\x,\y) = ab - \u\cdot\w \), and @thm-cauchy-schwarz bounds \( \u\cdot\w \) by \( \norm{\u}\norm{\w} \) — in the helpful direction, since it appears with a minus sign. What is left is to compare \( ab - \norm{\u}\norm{\w} \) with \( \tau(\x)\tau(\y) \), and squaring both sides turns the difference into a perfect square.
:::

::: {.proof}
Write \( \x = (a, \u) \) and \( \y = (b, \w) \) with \( a, b \in \nR \) and \( \u, \w \in \nR^3 \), so that \( q(\x) = a^2 - \norm{\u}^2 \) and \( \eta(\x,\y) = ab - \u\cdot\w \). Timelike gives \( a^2 > \norm{\u}^2 \) and \( b^2 > \norm{\w}^2 \), and future-pointing gives \( a, b > 0 \); hence \( a > \norm{\u} \ge 0 \) and \( b > \norm{\w} \ge 0 \), so \( ab > \norm{\u}\norm{\w} \ge 0 \). By @thm-cauchy-schwarz in \( \nR^3 \),
\[
\eta(\x, \y) = ab - \u\cdot\w \ge ab - \norm{\u}\norm{\w} > 0 .
\]
Both sides of the inequality to be proved are now known positive, so it suffices to compare squares. Expanding,
\[
\begin{aligned}
&\bigl(ab - \norm{\u}\norm{\w}\bigr)^2 - q(\x)q(\y) \\
&\qquad = a^2\norm{\w}^2 + b^2\norm{\u}^2 - 2ab\norm{\u}\norm{\w} \\
&\qquad = \bigl(a\norm{\w} - b\norm{\u}\bigr)^2 \ge 0 .
\end{aligned}
\]
Therefore \( ab - \norm{\u}\norm{\w} \ge \sqrt{q(\x)q(\y)} = \tau(\x)\tau(\y) \), and combining with the previous display gives \( \eta(\x,\y) \ge \tau(\x)\tau(\y) > 0 \).

For the equality case, equality forces both steps to be equalities: \( \u\cdot\w = \norm{\u}\norm{\w} \) and \( a\norm{\w} = b\norm{\u} \). Suppose first \( \u = \0 \). Then \( a\norm{\w} = 0 \) and \( a > 0 \), so \( \w = \0 \), and \( \y = (b, \0) = (b/a)\x \) with \( b/a > 0 \). Suppose instead \( \u \ne \0 \). The equality case of @thm-cauchy-schwarz makes \( (\u, \w) \) dependent, so \( \w = \lambda\u \) with \( \lambda \in \nR \), and then \( \u\cdot\w = \lambda\norm{\u}^2 = \norm{\u}\norm{\w} = \lvert\lambda\rvert\norm{\u}^2 \) forces \( \lambda \ge 0 \). Now \( a\norm{\w} = b\norm{\u} \) reads \( a\lambda\norm{\u} = b\norm{\u} \), so \( b = \lambda a \) and \( \y = \lambda\x \); and \( \lambda > 0 \) because \( b > 0 \). Conversely, if \( \y = \lambda\x \) with \( \lambda > 0 \) then \( \eta(\x,\y) = \lambda q(\x) \) and \( \tau(\x)\tau(\y) = \sqrt{\lambda^2q(\x)^2} = \lambda q(\x) \), so equality holds. This proves the lemma.
:::

::: {#thm-reversed-triangle-inequality}
[Reversed Triangle Inequality]

Let \( \x, \y \in \nR^{1,3} \) be timelike and both future-pointing. Then \( \x + \y \) is timelike and future-pointing, and
\[
\tau(\x + \y) \ge \tau(\x) + \tau(\y) ,
\]
with equality if and only if \( \y \) is a positive multiple of \( \x \).
:::

::: {.proof}
By @thm-polarization-forms, \( q(\x + \y) = q(\x) + 2\eta(\x,\y) + q(\y) \). By @lem-reversed-cauchy-schwarz, \( \eta(\x,\y) \ge \tau(\x)\tau(\y) \), so
\[
q(\x+\y) \ge q(\x) + 2\tau(\x)\tau(\y) + q(\y)
= \bigl(\tau(\x) + \tau(\y)\bigr)^2 ,
\]
where the last step uses \( q = \tau^2 \) on timelike vectors. The right-hand side is positive, so \( \x + \y \) is timelike; its first coordinate is a sum of two positive numbers, so it is future-pointing. Both sides of the last display are non-negative, so taking square roots preserves the inequality and gives \( \tau(\x+\y) \ge \tau(\x) + \tau(\y) \). Equality holds exactly when it holds in @lem-reversed-cauchy-schwarz, that is, exactly when \( \y = \lambda\x \) with \( \lambda > 0 \). This proves the theorem.
:::

::: {.remark}
Compare @cor-triangle-inequality, which gives \( \norm{\u + \v} \le \norm{\u} + \norm{\v} \) in an inner product space, and @thm-complex-triangle-inequality, its ancestor in \( \nC \). Same shape, opposite direction: the reversal is produced by the single sign change in the form, and by nothing else.
:::

Read as a statement about clocks, the reversed inequality says that a journey made in two straight legs accumulates *less* elapsed time than the single straight leg between the same endpoints, which is the algebra behind the twin paradox; whether that algebra describes the world is a question for physics, and this book answers only the algebra.

::: {.check}
Where exactly would the proof of @thm-reversed-triangle-inequality break if \( \x \) were future-pointing and \( \y \) past-pointing?
:::

::: {.solution}
At @lem-reversed-cauchy-schwarz, whose proof uses \( a, b > 0 \) to get \( ab > \norm{\u}\norm{\w} \ge 0 \). With \( b < 0 \) we have \( ab < 0 \), and \( \eta(\x,\y) = ab - \u\cdot\w \) can be negative, so the chain collapses at its first step. The conclusion genuinely fails: take \( \x = (1,0,0,0) \) and \( \y = (-1, 0, 0, 0) \), both timelike with \( \tau = 1 \), whose sum is \( \0 \) and is not timelike at all.
:::

## Exercises

### A. Check your understanding

::: {#exr-minkowski-space-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the sign convention used in this section, give the matrix of \( \eta \) in the standard basis, and say what its signature and inertia are.
2. Define timelike, null and spacelike, and say which earlier notion the word "null" renames.
3. True or false: the sum of two spacelike vectors is spacelike. Justify your answer.
4. Write down \( \det\B_t \) and \( \B_t^{-1} \), and say which row of the comparison table each answer sits in.
5. True or false: \( \Orth(1,1) \) is abelian. Justify your answer.
:::
:::

::: {.solution}
(a) The convention is \( (+,-,-,-) \), so \( \mtx{\eta}{\sE}{\sE} = \diag(1,-1,-1,-1) \), with signature \( (1,3) \) and inertia \( (1,3,0) \) (@def-signature). The opposite convention \( (-,+,+,+) \) uses \( -\eta \) and has signature \( (3,1) \).

(b) For \( \x \ne \0 \): timelike means \( q(\x) > 0 \), null means \( q(\x) = 0 \), spacelike means \( q(\x) < 0 \) (@def-causal-character). "Null" renames "non-zero isotropic vector" (@def-isotropic-vector).

(c) False. Take \( \x = (1, 2, 0, 0) \) and \( \y = (1, -2, 0, 0) \), with \( q(\x) = q(\y) = 1 - 4 = -3 < 0 \). Their sum is \( (2,0,0,0) \), with \( q = 4 > 0 \), which is timelike.

(d) \( \det\B_t = 1 \) by @thm-lorentz-boost-form with \( \mu = 1 \), and \( \B_t^{-1} = \B_{-t} \), since \( \B_t\B_{-t} = \B_0 = \I_2 \). The first sits in the "determinant \( +1 \) part" row, the second in the "addition law" row, which is what makes \( t \mapsto \B_t \) a group homomorphism.

(e) False. \( \B_1 \) and \( \D = \diag(1,-1) \) both lie in \( \Orth(1,1) \), and \( \B_1\D \) has \( (1,2) \) entry \( -\sinh 1 \) while \( \D\B_1 \) has \( (1,2) \) entry \( \sinh 1 \); these differ since \( \sinh 1 \ne 0 \).
:::

### B. Practice

::: {#exr-minkowski-space-b1}
[B1]

Determine which of the following lie in \( \Orth(1,1) \). For each one that does, give its rapidity \( t \) and the signs \( \varepsilon, \mu \) of @thm-lorentz-boost-form. Justify your answer.
\[
\A_1 = \begin{pmatrix} 5/3 & 4/3 \\ 4/3 & 5/3 \end{pmatrix}, \quad
\A_2 = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}, \quad
\A_3 = \begin{pmatrix} 5/3 & -4/3 \\ 4/3 & -5/3 \end{pmatrix}.
\]
:::

::: {.solution}
Write \( \D = \diag(1,-1) \) and test \( \P\tp\D\P = \D \) column by column, using \( q(\p_1) = 1 \), \( q(\p_2) = -1 \), \( \eta_2(\p_1,\p_2) = 0 \).

\( \A_1 \): \( (5/3)^2 - (4/3)^2 = (25-16)/9 = 1 \); \( (4/3)^2 - (5/3)^2 = -1 \); \( (5/3)(4/3) - (4/3)(5/3) = 0 \). So \( \A_1 \in \Orth(1,1) \). Here \( \sinh t = 4/3 \) and \( \cosh t = 5/3 \), so \( \varepsilon = \mu = 1 \) and \( \A_1 = \B_t \) with \( t = \log 3 \), since \( \cosh(\log 3) = \tfrac12(3 + \tfrac13) = 5/3 \) and \( \sinh(\log 3) = \tfrac12(3 - \tfrac13) = 4/3 \).

\( \A_2 \): \( 2^2 - 1^2 = 3 \ne 1 \), so the first column already fails and \( \A_2 \notin \Orth(1,1) \). (Indeed \( \A_2\tp\D\A_2 = \diag(3,-3) = 3\D \), so \( \A_2 \) scales the form rather than preserving it.)

\( \A_3 \): first column as for \( \A_1 \); second column \( (-4/3)^2 - (-5/3)^2 = -1 \); and \( (5/3)(-4/3) - (4/3)(-5/3) = 0 \). So \( \A_3 \in \Orth(1,1) \), with \( t = \log 3 \), \( \varepsilon = 1 \) and \( \mu = \det\A_3 = -25/9 + 16/9 = -1 \); that is, \( \A_3 = \B_{\log 3}\D \).
:::

::: {#exr-minkowski-space-b2}
[B2]

::: {.enumerate options="label=(\alph*)"}
1. Classify \( \x = (3, 1, 2, 2) \), \( \y = (1, 0, 1, 0) \) and \( \z = (0, 1, 1, 1) \) in \( \nR^{1,3} \) as timelike, null or spacelike.
2. The vector \( \y \) is null. Find a \( \w \in \nR^{1,3} \) such that \( (\y, \w) \) is a basis of a hyperbolic plane, that is, \( q(\w) = 0 \) and \( \eta(\y, \w) = 1 \).
:::
:::

::: {.solution}
(a) \( q(\x) = 9 - 1 - 4 - 4 = 0 \), so \( \x \) is null. \( q(\y) = 1 - 0 - 1 - 0 = 0 \), so \( \y \) is null. \( q(\z) = 0 - 1 - 1 - 1 = -3 < 0 \), so \( \z \) is spacelike.

(b) Try \( \w = (c, 0, -c, 0) \), which has \( q(\w) = c^2 - c^2 = 0 \) for every \( c \). Then \( \eta(\y, \w) = 1\cdot c - 1\cdot(-c) = 2c \), so \( c = \tfrac12 \) works: \( \w = (\tfrac12, 0, -\tfrac12, 0) \). The Gram matrix of \( (\y, \w) \) is \( \begin{psmallmatrix} 0 & 1 \\ 1 & 0\end{psmallmatrix} \), so \( \Span(\y, \w) \) is a hyperbolic plane (@def-hyperbolic-plane).
:::

::: {#exr-minkowski-space-b3}
[B3]

Let \( \x = (5, 3, 0, 0) \) and \( \y = (13, 12, 0, 0) \) in \( \nR^{1,3} \). Compute \( \tau(\x) \), \( \tau(\y) \), \( \eta(\x, \y) \) and \( \tau(\x + \y) \), and check @lem-reversed-cauchy-schwarz and @thm-reversed-triangle-inequality on this pair. Is either inequality an equality?
:::

::: {.solution}
\( q(\x) = 25 - 9 = 16 \), so \( \x \) is timelike and future-pointing with \( \tau(\x) = 4 \). \( q(\y) = 169 - 144 = 25 \), so \( \tau(\y) = 5 \). Next \( \eta(\x,\y) = 5\cdot13 - 3\cdot12 = 65 - 36 = 29 \), and \( \tau(\x)\tau(\y) = 20 \), so \( 29 \ge 20 \) as @lem-reversed-cauchy-schwarz requires. Finally \( \x + \y = (18, 15, 0, 0) \) with \( q = 324 - 225 = 99 \), so \( \tau(\x+\y) = \sqrt{99} \). Since \( 9^2 = 81 < 99 \), we get \( \tau(\x+\y) > 9 = \tau(\x) + \tau(\y) \), as @thm-reversed-triangle-inequality requires. Neither is an equality, and indeed \( \y \) is not a multiple of \( \x \), since \( 13/5 \ne 12/3 \).
:::

### C. Going deeper

::: {#exr-minkowski-space-c1}
[C1]

For \( t \in \nR \) put \( v(t) = \tanh t = \sinh t / \cosh t \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( v \colon \nR \to (-1, 1) \) is a bijection, and that \( \B_t\e_1 \) is a positive multiple of \( (1, v(t), 0, 0) \) read in \( \nR^{1,1} \).
2. Hence deduce that \( v(s + t) = \dfrac{v(s) + v(t)}{1 + v(s)v(t)} \), and say which part of @thm-lorentz-boost-form does the work.
:::
:::

::: {.solution}
(a) Since \( \cosh t > 0 \) and \( \cosh^2 t - \sinh^2 t = 1 \), we have \( \lvert\sinh t\rvert < \cosh t \), so \( \lvert v(t)\rvert < 1 \) and \( v \) maps into \( (-1,1) \). For injectivity and surjectivity, solve \( v(t) = c \) with \( \lvert c\rvert < 1 \): the equations \( \sinh t = c\cosh t \) and \( \cosh^2 t - \sinh^2 t = 1 \) give \( \cosh^2 t(1 - c^2) = 1 \), so \( \cosh t = (1-c^2)^{-1/2} \), which is a legitimate value since it is \( \ge 1 \), and then \( \sinh t = c(1-c^2)^{-1/2} \) determines \( t \) uniquely because \( \sinh \) is a bijection. So each \( c \) has exactly one preimage.

In \( \nR^{1,1} \), \( \B_t\e_1 = (\cosh t, \sinh t) = \cosh t\,(1, v(t)) \), and \( \cosh t > 0 \).

(b) By @thm-lorentz-boost-form, \( \B_s\B_t = \B_{s+t} \). Comparing entries,
\[
v(s+t) = \frac{\sinh(s+t)}{\cosh(s+t)}
= \frac{\sinh s\cosh t + \cosh s\sinh t}{\cosh s\cosh t + \sinh s\sinh t},
\]
and dividing numerator and denominator by \( \cosh s\cosh t > 0 \) gives \( (v(s)+v(t))/(1 + v(s)v(t)) \). The work is done by the addition law \( \B_s\B_t = \B_{s+t} \); the parametrization merely renames \( t \) as \( v(t) \), and because \( v \) is a bijection onto \( (-1,1) \) no information is lost in the renaming.
:::

::: {#exr-minkowski-space-c2}
[C2]

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \{\P\e_1 : \P \in \Orth(1,1)\} \) is the set of all \( \x \in \nR^{1,1} \) with \( q(\x) = 1 \), and that this set is unbounded.
2. Deduce that no bound \( \lvert p_{ij}\rvert \le c \) holds for all \( \P \in \Orth(1,1) \), and contrast this with \( \Orth(2) \), where \( \lvert p_{ij}\rvert \le 1 \) always. Which hypothesis of Chapter 10's \( \Orth(2) \) theory is responsible?
:::
:::

::: {.solution}
(a) \( (\subseteq) \) If \( \P \in \Orth(1,1) \) then \( q(\P\e_1) = (\P\e_1)\tp\D(\P\e_1) = \e_1\tp\P\tp\D\P\e_1 = \e_1\tp\D\e_1 = 1 \). \( (\supseteq) \) If \( q(\x) = 1 \), the proof of @thm-lorentz-boost-form shows \( \x = (\varepsilon\cosh t, \sinh t) \) for some \( t \) and sign \( \varepsilon \); then \( \x \) is the first column of \( \B_t \) when \( \varepsilon = 1 \), and of \( -\B_{-t} \) when \( \varepsilon = -1 \), and both lie in \( \Orth(1,1) \). The set is unbounded because \( \cosh t \to \infty \) as \( t \to \infty \).

(b) The first column of \( \P \) ranges over an unbounded set by (a), so its entries are unbounded, and no such \( c \) exists; this is the unboundedness Section 10 recorded, obtained here from the orbit rather than from a one-parameter family. In \( \Orth(2) \) the columns are unit vectors for the Euclidean norm, so every entry has modulus at most \( 1 \) and the group sits inside a bounded region. The responsible hypothesis is **positive definiteness** of the form: it is what makes \( q(\x) = 1 \) a bounded set, namely the unit sphere. Once one sign is reversed, the level set is a hyperbola and nothing is bounded.
:::

::: {#exr-minkowski-space-c3}
[C3]

The Quick check above showed that \( \nR^{1,3} \) has no plane on which the form vanishes identically. Show that \( \nR^{2,2} \) does have one, by exhibiting two vectors that span it, and reconcile the two answers with @thm-witt-decomposition.

*Hint: pair each positive coordinate with a negative one.*
:::

::: {.solution}
In \( \nR^{2,2} \) the form is \( \eta'(\x,\y) = x_1y_1 + x_2y_2 - x_3y_3 - x_4y_4 \). Put \( \u = (1,0,1,0) \) and \( \w = (0,1,0,1) \). Then
\[
q(\u) = 1 - 1 = 0, \quad q(\w) = 1 - 1 = 0, \quad \eta'(\u, \w) = 0 ,
\]
the last because every term pairs a zero with something. The list \( (\u, \w) \) is independent, since a relation \( a\u + b\w = \0 \) reads \( (a, b, a, b) = \0 \). So \( \Span(\u,\w) \) is a totally isotropic plane, and by bilinearity \( \eta' \) vanishes on all of it.

The reconciliation: by @def-witt-index the Witt index bounds the dimension of a totally isotropic subspace, it counts the hyperbolic planes of @thm-witt-decomposition, and over \( \nR \) it equals \( \min(n_+, n_-) \) (@prp-witt-index-real-complex). For \( \nR^{1,3} \) this is \( \min(1,3) = 1 \), so totally isotropic subspaces are lines at most; for \( \nR^{2,2} \) it is \( \min(2,2) = 2 \), so a totally isotropic plane is exactly what one should expect, and the two vectors above realize it. What differs is not the dimension \( 4 \) but how evenly the four signs are split.
:::
